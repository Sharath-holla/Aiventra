import re

from sqlalchemy import select
from sqlalchemy.orm import Session

from .artifacts import save_artifact
from .config import settings
from .db import now, uid
from .gateway import execute
from .models import (
    Agent,
    Approval,
    BusinessRecord,
    Execution,
    ModelConfig,
    ModelRun,
    Notification,
    Project,
    Provider,
    Repository,
    Task,
    Workflow,
    WorkflowStep,
)
from .organization import agent_for
from .providers import model_identity, provider_identity
from .repositories import apply_files, git, source_context, worktree
from .sandbox import run_tests
from .schemas import PatchResult, ReviewResult
from .security import audit, check_agent, digest
from .workflows import checkpoint, project_authority


def passed_tests(result: dict, suite: str) -> bool:
    pattern = r"^Ran (\d+) tests?\b" if suite == "python-unittest" else r"^# tests (\d+)\b"
    counts = re.findall(pattern, result["logs"], re.MULTILINE)
    return result["exit_code"] == 0 and bool(counts) and int(counts[-1]) > 0


async def coding_step(session: Session, workflow: Workflow, token: str) -> None:
    task = session.get(Task, workflow.task_id)
    project = session.get(Project, task.project_id)
    project_authority(session, project)
    approval = session.scalar(
        select(Approval).where(
            Approval.org_id == workflow.org_id,
            Approval.category == "repository_change",
            Approval.subject_id == task.id,
        )
    )
    if not approval or approval.expires_at <= now() or approval.subject_hash != digest(task.payload):
        raise PermissionError("Approved repository-change scope required")
    repository = session.get(Repository, task.payload["repository_id"])
    agent = session.get(Agent, task.assigned_agent_id)
    workspace = settings().repository_root.resolve() / ".worktrees" / project.id / task.id
    context = source_context(__import__("pathlib").Path(repository.path), task.objective)
    context["acceptance"] = task.acceptance
    if workflow.step == 0:
        check_agent(session, agent, "propose_patch", project)
        from pathlib import Path

        baseline = worktree(Path(repository.path), workspace, task.id)
        task.evidence = {"baseline_commit": baseline, "workspace": str(workspace)}
        qa = agent_for(session, workflow.org_id, "QA Director")
        check_agent(session, qa, "run_tests", project)
        existing = session.scalar(
            select(Execution).where(Execution.task_id == task.id, Execution.status == "running")
        )
        if existing:
            raise PermissionError("Interrupted test execution requires owner reconciliation")
        execution = Execution(
            id=uid(),
            org_id=workflow.org_id,
            task_id=task.id,
            agent_id=qa.id,
            workspace=str(workspace),
            command=[task.payload["test_suite"]],
            environment="restricted Docker",
            commit_hash=baseline,
        )
        session.add(execution)
        session.commit()
        result = await run_tests(workspace, task.payload["test_suite"])
        execution.status, execution.exit_code, execution.ended_at, execution.logs = (
            "completed",
            result["exit_code"],
            now(),
            result["logs"],
        )
        execution.command, execution.environment = result["command"], result["environment"]
        passed = passed_tests(result, task.payload["test_suite"])
        checkpoint(
            session,
            workflow,
            token,
            "baseline",
            {"execution_id": execution.id, **result},
            complete=not passed,
        )
        if not passed:
            task.status = "failed"
            task.evidence = {
                **task.evidence,
                "baseline_execution_id": execution.id,
                "baseline_passed": False,
                "reason": "Baseline failed or discovered no tests; code generation blocked",
            }
            session.add(
                Notification(
                    org_id=workflow.org_id,
                    severity="error",
                    title=task.evidence["reason"],
                    subject_id=task.id,
                )
            )
            audit(
                session,
                workflow.org_id,
                qa.id,
                "coding.baseline_failed",
                task.id,
                task.evidence,
                project_id=project.id,
                task_id=task.id,
                authorization=f"approval:{approval.id}",
            )
            return
    elif workflow.step == 1:
        result = await execute(
            session,
            workflow,
            agent,
            "patch",
            PatchResult,
            context,
            quality=85,
            capabilities={"structured", "coding"},
            project=project,
        )
        session.refresh(project)
        check_agent(session, agent, "propose_patch", project)
        if result.tests != task.payload["test_suite"]:
            raise PermissionError("Model cannot change approved test command")
        apply_files(workspace, [file.model_dump() for file in result.files])
        diff = git(workspace, "diff", "--no-ext-diff", "--no-textconv")
        untracked = git(workspace, "ls-files", "--others", "--exclude-standard")
        artifact = save_artifact(
            session,
            workflow.org_id,
            "Proposed code changes",
            diff + "\nNew files:\n" + untracked,
            kind="code_diff",
            project_id=project.id,
            task_id=task.id,
            agent_id=agent.id,
        )
        checkpoint(
            session,
            workflow,
            token,
            "patch",
            {"files": [file.model_dump() for file in result.files], "artifact_id": artifact.id},
        )
        task.status = "review"
    elif workflow.step < 2 + task.payload.get("review_count", 1):
        patch = session.scalar(
            select(WorkflowStep).where(WorkflowStep.workflow_id == workflow.id, WorkflowStep.name == "patch")
        )
        reviewer = agent_for(session, workflow.org_id, "Code Reviewer")
        if reviewer.id == agent.id:
            raise PermissionError("Code author cannot review own change")
        check_agent(session, reviewer, "review_diff", project)
        context["proposed_files"] = patch.result["files"]
        context["actual_diff"] = git(workspace, "diff", "--no-ext-diff", "--no-textconv")
        authored = session.scalar(
            select(ModelRun).where(
                ModelRun.workflow_id == workflow.id,
                ModelRun.step_name == "patch",
                ModelRun.status == "succeeded",
            )
        )
        if not authored:
            raise PermissionError("Persisted successful author run required before independent review")
        previous_reviews = list(
            session.scalars(
                select(ModelRun).where(
                    ModelRun.workflow_id == workflow.id,
                    ModelRun.step_name.in_(["review", "review_2"]),
                    ModelRun.status == "succeeded",
                )
            )
        )
        review_name = "review" if workflow.step == 2 else "review_2"
        # Initial reviewers receive the same diff/criteria; other verdicts are never supplied.
        result = await execute(
            session,
            workflow,
            reviewer,
            review_name,
            ReviewResult,
            context,
            quality=85,
            capabilities={"structured", "coding"},
            project=project,
            review_against=[authored.model_id, *[run.model_id for run in previous_reviews]],
            review_policy=task.payload.get("review_policy", "prefer_provider"),
        )
        reviewed = session.scalar(
            select(ModelRun).where(
                ModelRun.workflow_id == workflow.id,
                ModelRun.step_name == review_name,
                ModelRun.status == "succeeded",
            )
        )
        author_model, reviewer_model = (
            session.get(ModelConfig, authored.model_id),
            session.get(ModelConfig, reviewed.model_id),
        )
        author_provider = session.get(Provider, author_model.provider_id)
        reviewer_provider = session.get(Provider, reviewer_model.provider_id)
        diversity = (
            "different_provider"
            if provider_identity(author_provider) != provider_identity(reviewer_provider)
            else "different_model"
            if model_identity(author_model, author_provider)
            != model_identity(reviewer_model, reviewer_provider)
            else "same_model_independent_context"
        )
        evidence = {
            **result.model_dump(),
            "author_run_id": authored.id,
            "review_run_id": reviewed.id,
            "author_model_id": authored.model_id,
            "review_model_id": reviewed.model_id,
            "diversity": diversity,
            "review_policy": task.payload.get("review_policy", "prefer_provider"),
        }
        checkpoint(session, workflow, token, review_name, evidence)
        task.evidence = {**task.evidence, "reviews": [*task.evidence.get("reviews", []), evidence]}
        task.status = "testing" if workflow.step >= 2 + task.payload.get("review_count", 1) else "review"
    else:
        qa = agent_for(session, workflow.org_id, "QA Director")
        if qa.id == agent.id:
            raise PermissionError("Code author cannot independently verify own change")
        check_agent(session, qa, "run_tests", project)
        if session.scalar(
            select(Execution).where(Execution.task_id == task.id, Execution.status == "running")
        ):
            raise PermissionError("Interrupted test execution requires owner reconciliation")
        execution = Execution(
            id=uid(),
            org_id=workflow.org_id,
            task_id=task.id,
            agent_id=qa.id,
            workspace=str(workspace),
            command=[task.payload["test_suite"]],
            environment="restricted Docker",
            commit_hash=task.evidence["baseline_commit"],
        )
        session.add(execution)
        session.commit()
        result = await run_tests(workspace, task.payload["test_suite"])
        execution.status, execution.exit_code, execution.ended_at, execution.logs = (
            "completed",
            result["exit_code"],
            now(),
            result["logs"],
        )
        execution.command, execution.environment = result["command"], result["environment"]
        reviews = list(
            session.scalars(
                select(WorkflowStep).where(
                    WorkflowStep.workflow_id == workflow.id, WorkflowStep.name.in_(["review", "review_2"])
                )
            )
        )
        reviewer_approved = len(reviews) == task.payload.get("review_count", 1) and all(
            review.result["approved"] for review in reviews
        )
        approved = reviewer_approved and passed_tests(result, task.payload["test_suite"])
        task.status = "completed" if approved else "failed"
        task.evidence = {
            **task.evidence,
            "execution_id": execution.id,
            "reviewer_approved": reviewer_approved,
            "qa_agent_id": qa.id,
            "mode": workflow.mode,
            "exit_code": result["exit_code"],
            "patch_sha256": digest(
                session.scalar(
                    select(WorkflowStep).where(
                        WorkflowStep.workflow_id == workflow.id, WorkflowStep.name == "patch"
                    )
                ).result
            ),
        }
        if not approved:
            session.add(
                BusinessRecord(
                    org_id=workflow.org_id,
                    project_id=project.id,
                    kind="incident",
                    title="Coding task needs repair or owner review",
                    data=task.evidence,
                )
            )
        checkpoint(session, workflow, token, "qa", task.evidence, complete=True)
    audit(
        session,
        workflow.org_id,
        agent.id,
        "coding.step",
        task.id,
        {"step": workflow.step, "status": task.status},
        project_id=project.id,
        task_id=task.id,
        authorization=f"approval:{approval.id}",
    )
