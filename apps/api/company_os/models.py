from typing import Any

from sqlalchemy import JSON, BigInteger, ForeignKey, Index, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .db import Base, now, uid

# SQLite INTEGER already stores signed 64-bit values. PostgreSQL requires BIGINT.
MONEY = BigInteger().with_variant(Integer(), "sqlite")


class Record:
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uid)
    created_at: Mapped[int] = mapped_column(default=now)


class Tenant(Record):
    org_id: Mapped[str] = mapped_column(ForeignKey("organizations.id"), index=True)


class Organization(Record, Base):
    __tablename__ = "organizations"
    name: Mapped[str] = mapped_column(String(200))
    paused: Mapped[bool] = mapped_column(default=False)
    deployments_paused: Mapped[bool] = mapped_column(default=True)
    version: Mapped[int] = mapped_column(default=1)
    audit_head: Mapped[str] = mapped_column(default="0" * 64)


class Client(Tenant, Base):
    __tablename__ = "clients"
    name: Mapped[str] = mapped_column(String(200))


class User(Tenant, Base):
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(String(254), unique=True)
    password_hash: Mapped[str] = mapped_column(Text, default="")
    role: Mapped[str] = mapped_column(default="client")
    client_id: Mapped[str | None] = mapped_column(ForeignKey("clients.id"))
    oidc_subject: Mapped[str | None] = mapped_column(String(300), unique=True)
    enabled: Mapped[bool] = mapped_column(default=True)


class AuthSession(Tenant, Base):
    __tablename__ = "auth_sessions"
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    expires_at: Mapped[int] = mapped_column(index=True)
    revoked_at: Mapped[int | None] = mapped_column()


class LoginThrottle(Base):
    __tablename__ = "login_throttles"
    key_hash: Mapped[str] = mapped_column(String(64), primary_key=True)
    attempts: Mapped[int] = mapped_column(default=0)
    resets_at: Mapped[int] = mapped_column(index=True)


class WorkerHeartbeat(Base):
    __tablename__ = "worker_heartbeats"
    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    started_at: Mapped[int] = mapped_column(default=now)
    last_seen: Mapped[int] = mapped_column(index=True)
    status: Mapped[str] = mapped_column(default="running")


class Department(Tenant, Base):
    __tablename__ = "departments"
    name: Mapped[str] = mapped_column(String(200))
    independent: Mapped[bool] = mapped_column(default=False)
    __table_args__ = (UniqueConstraint("org_id", "name"),)


class Agent(Tenant, Base):
    __tablename__ = "agents"
    department_id: Mapped[str] = mapped_column(ForeignKey("departments.id"))
    name: Mapped[str] = mapped_column(String(200))
    role: Mapped[str] = mapped_column(String(200))
    reports_to: Mapped[str] = mapped_column(default="CEO")
    responsibilities: Mapped[list[str]] = mapped_column(JSON, default=list)
    tools: Mapped[list[str]] = mapped_column(JSON, default=list)
    policies: Mapped[list[str]] = mapped_column(JSON, default=list)
    routing_policy: Mapped[str] = mapped_column(default="economy")
    objectives: Mapped[list[str]] = mapped_column(JSON, default=list)
    memory_scope: Mapped[str] = mapped_column(default="assigned_project")
    max_iterations: Mapped[int] = mapped_column(default=3)
    max_runtime_seconds: Mapped[int] = mapped_column(default=180)
    max_cost_micro: Mapped[int] = mapped_column(MONEY, default=500000)
    enabled: Mapped[bool] = mapped_column(default=True)


class Provider(Tenant, Base):
    __tablename__ = "providers"
    name: Mapped[str] = mapped_column(String(200))
    kind: Mapped[str] = mapped_column(String(40))
    base_url: Mapped[str] = mapped_column(String(500))
    credential_env: Mapped[str] = mapped_column(String(100), default="")
    enabled: Mapped[bool] = mapped_column(default=True)


class ModelConfig(Tenant, Base):
    __tablename__ = "model_configs"
    provider_id: Mapped[str] = mapped_column(ForeignKey("providers.id"))
    identifier: Mapped[str] = mapped_column(String(200))
    capabilities: Mapped[list[str]] = mapped_column(JSON, default=list)
    context_tokens: Mapped[int] = mapped_column(default=32768)
    quality: Mapped[int] = mapped_column(default=50)
    reliability: Mapped[int] = mapped_column(default=100)
    latency_ms: Mapped[int] = mapped_column(default=1000)
    input_price_micro_per_million: Mapped[int] = mapped_column(MONEY, default=0)
    output_price_micro_per_million: Mapped[int] = mapped_column(MONEY, default=0)
    price_source: Mapped[str] = mapped_column(Text, default="")
    price_checked_at: Mapped[int] = mapped_column(default=now)
    sensitivity: Mapped[str] = mapped_column(default="internal")
    enabled: Mapped[bool] = mapped_column(default=True)
    __table_args__ = (UniqueConstraint("provider_id", "identifier"),)


class Requirement(Tenant, Base):
    __tablename__ = "requirements"
    client_id: Mapped[str] = mapped_column(ForeignKey("clients.id"))
    title: Mapped[str] = mapped_column(String(200))
    text: Mapped[str] = mapped_column(Text)
    mode: Mapped[str] = mapped_column(default="mock")
    sensitivity: Mapped[str] = mapped_column(default="internal")
    budget_micro: Mapped[int] = mapped_column(MONEY, default=5000000)
    deadline: Mapped[str | None] = mapped_column(String(100))
    constraints: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    answers: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    rates: Mapped[list[dict[str, Any]]] = mapped_column(JSON, default=list)
    analysis: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    status: Mapped[str] = mapped_column(default="queued")
    version: Mapped[int] = mapped_column(default=1)


class Proposal(Tenant, Base):
    __tablename__ = "proposals"
    requirement_id: Mapped[str] = mapped_column(ForeignKey("requirements.id"))
    version: Mapped[int] = mapped_column()
    content: Mapped[dict[str, Any]] = mapped_column(JSON)
    content_hash: Mapped[str] = mapped_column(String(64))
    status: Mapped[str] = mapped_column(default="awaiting_approval")
    __table_args__ = (UniqueConstraint("requirement_id", "version"),)


class Approval(Tenant, Base):
    __tablename__ = "approvals"
    category: Mapped[str] = mapped_column(String(100))
    subject_id: Mapped[str] = mapped_column(String(36))
    subject_hash: Mapped[str] = mapped_column(String(64))
    version: Mapped[int] = mapped_column()
    owner_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    selection: Mapped[str] = mapped_column(default="")
    expires_at: Mapped[int] = mapped_column()
    __table_args__ = (UniqueConstraint("org_id", "category", "subject_id", "version"),)


class Project(Tenant, Base):
    __tablename__ = "projects"
    client_id: Mapped[str] = mapped_column(ForeignKey("clients.id"))
    proposal_id: Mapped[str] = mapped_column(ForeignKey("proposals.id"), unique=True)
    approval_id: Mapped[str] = mapped_column(ForeignKey("approvals.id"))
    name: Mapped[str] = mapped_column(String(200))
    status: Mapped[str] = mapped_column(default="active")
    selected_alternative: Mapped[str] = mapped_column(String(200))
    budget_micro: Mapped[int] = mapped_column(MONEY, default=5000000)
    version: Mapped[int] = mapped_column(default=1)


class Milestone(Tenant, Base):
    __tablename__ = "milestones"
    project_id: Mapped[str] = mapped_column(ForeignKey("projects.id"))
    name: Mapped[str] = mapped_column(String(200))
    position: Mapped[int] = mapped_column()


class Task(Tenant, Base):
    __tablename__ = "tasks"
    project_id: Mapped[str] = mapped_column(ForeignKey("projects.id"), index=True)
    milestone_id: Mapped[str | None] = mapped_column(ForeignKey("milestones.id"))
    assigned_agent_id: Mapped[str] = mapped_column(ForeignKey("agents.id"))
    objective: Mapped[str] = mapped_column(Text)
    kind: Mapped[str] = mapped_column(default="document")
    status: Mapped[str] = mapped_column(default="ready")
    acceptance: Mapped[list[str]] = mapped_column(JSON, default=list)
    payload: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    evidence: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    budget_micro: Mapped[int] = mapped_column(MONEY, default=500000)
    version: Mapped[int] = mapped_column(default=1)


class TaskDependency(Base):
    __tablename__ = "task_dependencies"
    task_id: Mapped[str] = mapped_column(ForeignKey("tasks.id"), primary_key=True)
    depends_on: Mapped[str] = mapped_column(ForeignKey("tasks.id"), primary_key=True)


class Workflow(Tenant, Base):
    __tablename__ = "workflows"
    requirement_id: Mapped[str | None] = mapped_column(ForeignKey("requirements.id"))
    task_id: Mapped[str | None] = mapped_column(ForeignKey("tasks.id"))
    conversation_turn_id: Mapped[str | None] = mapped_column(ForeignKey("conversation_turns.id"))
    kind: Mapped[str] = mapped_column(default="consulting")
    mode: Mapped[str] = mapped_column(default="mock")
    revision: Mapped[int] = mapped_column(default=1)
    status: Mapped[str] = mapped_column(default="queued", index=True)
    step: Mapped[int] = mapped_column(default=0)
    attempts: Mapped[int] = mapped_column(default=0)
    max_attempts: Mapped[int] = mapped_column(default=3)
    deadline_at: Mapped[int] = mapped_column(default=lambda: now() + 1800)
    lease_until: Mapped[int] = mapped_column(default=0)
    lease_token: Mapped[str] = mapped_column(default="")
    last_error: Mapped[str] = mapped_column(Text, default="")
    wait_context: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    __table_args__ = (
        Index("uq_workflows_conversation_turn", "conversation_turn_id", unique=True),
        Index("uq_workflows_task", "task_id", unique=True),
        Index("uq_workflows_requirement_revision", "requirement_id", "revision", unique=True),
    )


class WorkflowStep(Tenant, Base):
    __tablename__ = "workflow_steps"
    workflow_id: Mapped[str] = mapped_column(ForeignKey("workflows.id"))
    name: Mapped[str] = mapped_column(String(100))
    result: Mapped[dict[str, Any]] = mapped_column(JSON)
    __table_args__ = (UniqueConstraint("workflow_id", "name"),)


class Meeting(Tenant, Base):
    __tablename__ = "meetings"
    requirement_id: Mapped[str | None] = mapped_column(ForeignKey("requirements.id"))
    project_id: Mapped[str | None] = mapped_column(ForeignKey("projects.id"))
    agenda: Mapped[str] = mapped_column(Text)
    mode: Mapped[str] = mapped_column()
    rounds: Mapped[int] = mapped_column(default=1)
    contributions: Mapped[list[dict[str, Any]]] = mapped_column(JSON, default=list)
    decision: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)


class Message(Tenant, Base):
    __tablename__ = "messages"
    sender: Mapped[str] = mapped_column(String(200))
    recipient: Mapped[str] = mapped_column(String(200))
    project_id: Mapped[str | None] = mapped_column(ForeignKey("projects.id"))
    task_id: Mapped[str | None] = mapped_column(ForeignKey("tasks.id"))
    type: Mapped[str] = mapped_column(String(100))
    correlation_id: Mapped[str] = mapped_column(String(36), index=True)
    priority: Mapped[str] = mapped_column(default="normal")
    content: Mapped[dict[str, Any]] = mapped_column(JSON)
    expected_schema: Mapped[str] = mapped_column(default="Acknowledgement")
    authorization: Mapped[str] = mapped_column(default="internal scoped workflow")
    status: Mapped[str] = mapped_column(default="delivered")
    acknowledged_at: Mapped[int | None] = mapped_column()


class Budget(Tenant, Base):
    __tablename__ = "budgets"
    scope: Mapped[str] = mapped_column(String(100), unique=True)
    limit_micro: Mapped[int] = mapped_column(MONEY)
    spent_micro: Mapped[int] = mapped_column(MONEY, default=0)
    reserved_micro: Mapped[int] = mapped_column(MONEY, default=0)
    version: Mapped[int] = mapped_column(default=1)


class ModelRun(Tenant, Base):
    __tablename__ = "model_runs"
    workflow_id: Mapped[str] = mapped_column(ForeignKey("workflows.id"))
    agent_id: Mapped[str] = mapped_column(ForeignKey("agents.id"))
    model_id: Mapped[str] = mapped_column(ForeignKey("model_configs.id"))
    project_id: Mapped[str | None] = mapped_column(ForeignKey("projects.id"))
    task_id: Mapped[str | None] = mapped_column(ForeignKey("tasks.id"))
    step_name: Mapped[str] = mapped_column(String(100))
    attempt: Mapped[int] = mapped_column()
    status: Mapped[str] = mapped_column(default="started")
    routing_reason: Mapped[str] = mapped_column(Text)
    input_tokens: Mapped[int] = mapped_column(default=0)
    output_tokens: Mapped[int] = mapped_column(default=0)
    cost_micro: Mapped[int] = mapped_column(MONEY, default=0)
    reserved_micro: Mapped[int] = mapped_column(MONEY, default=0)
    budget_ids: Mapped[list[str]] = mapped_column(JSON, default=list)
    cost_basis: Mapped[str] = mapped_column(default="computed_estimate")
    duration_ms: Mapped[int] = mapped_column(default=0)
    response: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    error: Mapped[str] = mapped_column(Text, default="")
    __table_args__ = (UniqueConstraint("workflow_id", "step_name", "attempt"),)


class Transaction(Tenant, Base):
    __tablename__ = "spending_transactions"
    run_id: Mapped[str] = mapped_column(ForeignKey("model_runs.id"), unique=True)
    amount_micro: Mapped[int] = mapped_column(MONEY)
    basis: Mapped[str] = mapped_column()


class Artifact(Tenant, Base):
    __tablename__ = "artifacts"
    project_id: Mapped[str | None] = mapped_column(ForeignKey("projects.id"), index=True)
    conversation_id: Mapped[str | None] = mapped_column(ForeignKey("conversations.id"), index=True)
    task_id: Mapped[str | None] = mapped_column(ForeignKey("tasks.id"))
    agent_id: Mapped[str | None] = mapped_column(ForeignKey("agents.id"))
    name: Mapped[str] = mapped_column(String(200))
    kind: Mapped[str] = mapped_column(String(100))
    content: Mapped[str] = mapped_column(Text)
    sha256: Mapped[str] = mapped_column(String(64))
    storage_key: Mapped[str] = mapped_column(default="")


class Repository(Tenant, Base):
    __tablename__ = "repositories"
    project_id: Mapped[str] = mapped_column(ForeignKey("projects.id"))
    name: Mapped[str] = mapped_column(String(200))
    path: Mapped[str] = mapped_column(Text)
    baseline_commit: Mapped[str] = mapped_column(String(64), default="")
    report: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)


class Execution(Tenant, Base):
    __tablename__ = "executions"
    task_id: Mapped[str] = mapped_column(ForeignKey("tasks.id"))
    agent_id: Mapped[str] = mapped_column(ForeignKey("agents.id"))
    workspace: Mapped[str] = mapped_column(Text)
    command: Mapped[list[str]] = mapped_column(JSON)
    environment: Mapped[str] = mapped_column(String(200))
    commit_hash: Mapped[str] = mapped_column(String(64), default="")
    status: Mapped[str] = mapped_column(default="running")
    exit_code: Mapped[int | None] = mapped_column()
    started_at: Mapped[int] = mapped_column(default=now)
    ended_at: Mapped[int | None] = mapped_column()
    logs: Mapped[str] = mapped_column(Text, default="")


class BusinessRecord(Tenant, Base):
    __tablename__ = "business_records"
    kind: Mapped[str] = mapped_column(String(100), index=True)
    project_id: Mapped[str | None] = mapped_column(ForeignKey("projects.id"))
    client_id: Mapped[str | None] = mapped_column(ForeignKey("clients.id"))
    title: Mapped[str] = mapped_column(String(200))
    status: Mapped[str] = mapped_column(default="open")
    data: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    version: Mapped[int] = mapped_column(default=1)


class AuditEvent(Tenant, Base):
    __tablename__ = "audit_events"
    actor: Mapped[str] = mapped_column(String(200))
    action: Mapped[str] = mapped_column(String(200))
    subject: Mapped[str] = mapped_column(String(200))
    project_id: Mapped[str | None] = mapped_column(ForeignKey("projects.id"))
    task_id: Mapped[str | None] = mapped_column(ForeignKey("tasks.id"))
    authorization: Mapped[str] = mapped_column(String(200))
    detail: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    previous_hash: Mapped[str] = mapped_column(String(64))
    event_hash: Mapped[str] = mapped_column(String(64))


class Notification(Tenant, Base):
    __tablename__ = "notifications"
    severity: Mapped[str] = mapped_column(String(20))
    title: Mapped[str] = mapped_column(String(200))
    subject_id: Mapped[str] = mapped_column(String(36))
    acknowledged: Mapped[bool] = mapped_column(default=False)


class Conversation(Tenant, Base):
    __tablename__ = "conversations"
    owner_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    client_id: Mapped[str] = mapped_column(ForeignKey("clients.id"))
    project_id: Mapped[str | None] = mapped_column(ForeignKey("projects.id"))
    title: Mapped[str] = mapped_column(String(200), default="New conversation")
    mode: Mapped[str] = mapped_column(default="live")
    budget_micro: Mapped[int] = mapped_column(MONEY, default=1_000_000)
    version: Mapped[int] = mapped_column(default=1)
    updated_at: Mapped[int] = mapped_column(default=now, index=True)


class ConversationTurn(Tenant, Base):
    __tablename__ = "conversation_turns"
    conversation_id: Mapped[str] = mapped_column(ForeignKey("conversations.id"), index=True)
    request_id: Mapped[str] = mapped_column(String(36))
    request_hash: Mapped[str] = mapped_column(String(64))
    position: Mapped[int] = mapped_column()
    intent: Mapped[str] = mapped_column(default="chat")
    content: Mapped[str] = mapped_column(Text)
    response: Mapped[str] = mapped_column(Text, default="")
    attachment_ids: Mapped[list[str]] = mapped_column(JSON, default=list)
    requirement_id: Mapped[str | None] = mapped_column(ForeignKey("requirements.id"))
    __table_args__ = (
        UniqueConstraint("conversation_id", "request_id"),
        UniqueConstraint("conversation_id", "position"),
    )
