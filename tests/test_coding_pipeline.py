import subprocess

import pytest
from company_os.config import settings
from company_os.workflows import tick


@pytest.mark.parametrize("baseline_success,baseline_exit", [(True, 0), (False, 0), (False, 1)])
@pytest.mark.parametrize("review_count", [1, 2])
async def test_c_isolated_patch_and_independent_fixture_review_cannot_certify_live_code(
    http, company, requirement, monkeypatch, baseline_success, baseline_exit, review_count
):
    for _ in range(7):
        await tick(company["factory"])
    proposal = http.get("/state").json()["proposals"][0]
    project = http.post(
        f"/proposals/{proposal['id']}/approve",
        json={
            "version": 1,
            "content_hash": proposal["content_hash"],
            "selection": proposal["content"]["recommendation"],
        },
    ).json()
    repo = settings().repository_root / "baseline"
    repo.mkdir(parents=True)
    (repo / "README.md").write_text("Test baseline repository\n")
    for args in (
        ["init"],
        ["config", "user.email", "test@local.invalid"],
        ["config", "user.name", "Test Fixture"],
        ["add", "README.md"],
        ["commit", "-m", "test baseline"],
    ):
        subprocess.run(["git", "-C", str(repo), *args], capture_output=True, check=True, timeout=20)
    imported = http.post(
        "/repositories",
        json={"project_id": project["id"], "name": "Test baseline", "relative_path": "baseline"},
    )
    assert imported.status_code == 201, imported.text
    task = http.post(
        f"/projects/{project['id']}/coding",
        json={
            "repository_id": imported.json()["id"],
            "objective": "Create a decimal-safe quote calculation with regression tests",
            "acceptance": ["Decimal arithmetic preserves precision"],
            "mode": "mock",
            "test_suite": "python-unittest",
            "review_count": review_count,
        },
    ).json()
    assert (
        http.post(f"/tasks/{task['id']}/approve", json={"content_hash": task["approval_hash"]}).status_code
        == 200
    )

    async def runner_fixture(*_args, **_kwargs):
        return {
            "command": ["python", "-m", "unittest"],
            "environment": "MOCKED runner contract: not Docker evidence",
            "exit_code": baseline_exit,
            "logs": "MOCKED runner contract\nRan 1 test\nOK"
            if baseline_success
            else "MOCKED runner contract\nRan 0 tests\nOK",
        }

    monkeypatch.setattr("company_os.engineering.run_tests", runner_fixture)
    for _ in range(12):
        await tick(company["factory"])
    state = http.get("/state").json()
    executed = next(row for row in state["tasks"] if row["id"] == task["id"])
    if not baseline_success:
        assert executed["status"] == "failed" and executed["evidence"]["baseline_passed"] is False
        assert not any(row["task_id"] == task["id"] for row in state["runs"])
        assert not any(row["task_id"] == task["id"] for row in state["artifacts"])
        return
    assert executed["status"] == "failed"  # Fixture review deliberately cannot approve.
    assert executed["evidence"]["reviewer_approved"] is False
    assert len(executed["evidence"]["reviews"]) == review_count
    assert all(
        row["diversity"] == "same_model_independent_context" for row in executed["evidence"]["reviews"]
    )
    assert not (repo / "quote.py").exists()
    workspace = settings().repository_root / ".worktrees" / project["id"] / task["id"]
    assert (workspace / "quote.py").exists()
    results = [row for row in state["executions"] if row["task_id"] == task["id"]]
    assert len(results) == 2
    assert all(row["agent_id"] != executed["assigned_agent_id"] for row in results)
    assert any(row["kind"] == "code_diff" and row["task_id"] == task["id"] for row in state["artifacts"])
