"""Persisted task routing contracts; all inference here is explicitly deterministic."""

from copy import deepcopy

import pytest
from company_os import models as m
from company_os.db import now, uid
from company_os.project_setup import routing
from company_os.staffing import task_ready
from company_os.workflows import tick
from sqlalchemy import select

from tests.test_staffing import approve, project_plan, revise


def alternate(company, *, kind="mock", quality=95, capabilities=None):
    with company["factory"]() as session:
        provider = session.scalar(select(m.Provider).where(m.Provider.kind == kind))
        if not provider:
            provider = m.Provider(
                org_id=company["org"].id,
                name="Explicit test provider",
                kind=kind,
                base_url="https://example.invalid",
            )
            session.add(provider)
            session.flush()
        model = m.ModelConfig(
            id=uid(),
            org_id=company["org"].id,
            provider_id=provider.id,
            identifier="explicit-fixture-" + uid(),
            quality=quality,
            capabilities=capabilities or ["structured", "coding", "reasoning"],
            context_tokens=131072,
            sensitivity="confidential",
        )
        session.add(model)
        session.commit()
        return model.id


async def test_task_decisions_persist_exact_override_and_immutable_approval(http, company, requirement):
    _, plan = await project_plan(http, company, requirement)
    assert all(
        row["model_selection"]["state"] == "WAITING_FOR_FREE_PROVIDER" for row in plan["content"]["tasks"]
    )
    model_id = alternate(company)
    content = deepcopy(plan["content"])
    content.update(mode="mock", routing_mode="hybrid")
    content["tasks"][0].update(
        model_override=model_id,
        workstream="analysis",
        skills=["requirements"],
        required_tools=["write_artifact"],
        qa_requirements=["Trace every requirement to evidence"],
    )
    plan = revise(http, plan, **content)
    chosen = plan["content"]["tasks"][0]
    assert chosen["model_selection"]["model_id"] == model_id
    assert "Exact owner" in chosen["model_selection"]["reason"]
    active = approve(http, plan)
    task = next(row for row in active["tasks"] if row["payload"]["plan_key"] == chosen["key"])
    assert task["payload"]["task_requirements"]["model_override"] == model_id
    company["factory"].kw["bind"].dispose()
    recovered = http.get(f"/projects/{plan['project_id']}/staffing").json()
    assert recovered["content_hash"] == plan["content_hash"]
    assert recovered["tasks"] == active["tasks"]
    assert (
        http.patch(
            f"/staffing/{plan['id']}", json={"version": plan["version"], "content": content}
        ).status_code
        == 409
    )
    with company["factory"]() as session:
        saved = session.get(m.Task, task["id"])
        # Ignore dependencies only for the pure authority assertion.
        assert saved.payload["task_requirements"] == {
            key: chosen[key] for key in saved.payload["task_requirements"]
        }
        workflow = m.Workflow(org_id=saved.org_id, task_id=saved.id, mode="mock")
        agent = session.get(m.Agent, saved.assigned_agent_id)
        assert (
            routing(session, workflow, agent, "document", session.get(m.Project, saved.project_id), None)[0]
            == model_id
        )
        saved.payload = {
            **saved.payload,
            "task_requirements": {**saved.payload["task_requirements"], "model_override": "tampered"},
        }
        assert not task_ready(session, saved)


@pytest.mark.parametrize("bad", ["unknown", "paid", "tools", "capability", "automatic"])
async def test_task_model_and_tool_rejections(http, company, requirement, bad):
    _, plan = await project_plan(http, company, requirement)
    content = deepcopy(plan["content"])
    content.update(mode="mock", routing_mode="hybrid")
    row = content["tasks"][0]
    row["model_override"] = (
        "unknown"
        if bad == "unknown"
        else alternate(
            company,
            kind="openai" if bad == "paid" else "mock",
            capabilities=["coding"] if bad == "capability" else None,
        )
    )
    if bad == "paid":
        content["mode"] = "live"
    if bad == "tools":
        row["required_tools"] = ["deploy"]
    if bad == "automatic":
        content["routing_mode"] = "automatic"
    response = http.patch(f"/staffing/{plan['id']}", json={"version": plan["version"], "content": content})
    assert response.status_code == 422, response.text
    assert http.get(f"/projects/{plan['project_id']}/staffing").json()["version"] == plan["version"]


async def test_manual_missing_assignment_waits_and_spoofed_explanation_is_replaced(
    http, company, requirement
):
    _, plan = await project_plan(http, company, requirement)
    for _ in range(4):
        await tick(company["factory"])
    content = deepcopy(plan["content"])
    content.update(routing_mode="manual")
    content["tasks"][0]["model_selection"] = {"state": "READY", "model_id": "invented"}
    plan = revise(http, plan, **content)
    assert plan["content"]["tasks"][0]["model_selection"]["model_id"] is None
    approve(http, plan)
    await tick(company["factory"])
    current = http.get(f"/projects/{plan['project_id']}/staffing").json()
    assert any(row["status"] == "waiting_for_free_provider" for row in current["tasks"])
    assert current["budget"]["spent_micro"] == current["budget"]["reserved_micro"] == 0


async def test_task_override_never_pins_independent_reviewer(http, company, requirement):
    _, plan = await project_plan(http, company, requirement)
    model_id = alternate(company)
    content = deepcopy(plan["content"])
    content.update(mode="mock", routing_mode="hybrid")
    content["tasks"][0]["model_override"] = model_id
    active = approve(http, revise(http, plan, **content))
    with company["factory"]() as session:
        task = session.get(m.Task, active["tasks"][0]["id"])
        reviewer = session.scalar(select(m.Agent).where(m.Agent.role == "Code Reviewer"))
        workflow = m.Workflow(org_id=task.org_id, task_id=task.id, mode="mock")
        assert (
            routing(session, workflow, reviewer, "review", session.get(m.Project, task.project_id), None)[0]
            is None
        )
        approval = session.scalar(
            select(m.Approval).where(m.Approval.category == "staffing", m.Approval.subject_id == plan["id"])
        )
        approval.expires_at = now() - 1
        assert not task_ready(session, task)


async def test_automatic_task_failure_reassigns_with_persisted_attempts(
    http, company, requirement, monkeypatch
):
    from company_os import gateway
    from company_os.providers import ProviderError

    _, plan = await project_plan(http, company, requirement)
    for _ in range(4):
        await tick(company["factory"])
    model_id = alternate(company)
    content = deepcopy(plan["content"])
    content.update(mode="mock", routing_mode="automatic")
    content["tasks"] = [content["tasks"][0]]
    content["tasks"][0]["recommended_model_id"] = model_id
    active = approve(http, revise(http, plan, **content))
    original = gateway.fixture
    attempts = []

    def fail_once(schema, context):
        attempts.append(schema)
        if len(attempts) == 1:
            raise ProviderError("Explicit deterministic first-model failure")
        return original(schema, context)

    monkeypatch.setattr(gateway, "fixture", fail_once)
    assert await tick(company["factory"])
    with company["factory"]() as session:
        task = session.get(m.Task, active["tasks"][0]["id"])
        runs = list(
            session.scalars(
                select(m.ModelRun).where(m.ModelRun.task_id == task.id).order_by(m.ModelRun.attempt)
            )
        )
        assert task.status == "completed" and [run.status for run in runs] == ["failed", "succeeded"]
        assert runs[0].model_id == model_id and runs[1].model_id != model_id
        assert all("task_routing=automatic" in run.routing_reason for run in runs)
        assert all(run.cost_micro == 0 for run in runs)


async def test_task_benchmark_case_filters_weak_model(http, company, requirement, monkeypatch):
    from types import SimpleNamespace

    _, plan = await project_plan(http, company, requirement)
    strong = alternate(company)
    weak = alternate(company)
    monkeypatch.setattr(
        "company_os.benchmarks.current_profile",
        lambda session, model, provider: SimpleNamespace(
            metrics={
                "quality": 95,
                "reliability": 100,
                "cases": {"business": 100 if model.id == strong else 50},
            }
        ),
    )
    content = deepcopy(plan["content"])
    content["mode"] = "mock"
    selected = revise(http, plan, **content)["content"]["tasks"][0]["model_selection"]
    assert selected["model_id"] == strong
    assert weak not in [row["id"] for row in selected["model_options"]]
    assert selected["candidates"][0]["quality_basis"] == "current fingerprint-bound microbenchmark"
