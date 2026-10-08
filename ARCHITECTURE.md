# Aiventra OS architecture

The FastAPI/Next.js modular monolith is retained. [Detailed boundaries and diagrams](docs/architecture.md) describe the implementation. The authoritative roadmap is now [PRODUCTION_UPGRADE_SPEC.md](docs/PRODUCTION_UPGRADE_SPEC.md); both earlier specifications remain preserved.

The API owns authenticated, organization/client/project-scoped mutations. A separate worker owns durable database workflows, real model calls and restricted runner requests. SQLAlchemy/Alembic hold authoritative state; SQLite is verified locally and PostgreSQL/Compose is exercised in ephemeral CI. Monetary quantities use 64-bit storage. Private files plus database content hold artifacts. Generated code never executes directly in API/worker hosts.

The new default CEO workspace uses persisted `conversations` and `conversation_turns`. A unique conversation/request key, optimistic version and unique turn/workflow association prevent duplicate dispatch. Advisory turns use existing gateway policy/reservations/usage; consultation turns stage the existing seven-step consulting flow within the same fenced transaction. Exact proposal approval creates the existing project/tasks; URL links keep the conversation, requirement and project connected.

Conversation and turn caps join existing overlapping organization/project/agent/model/day/month caps. Cancellation invalidates the workflow lease, suppressing a late answer without pretending an in-flight provider charge disappeared. Missing models/credentials wait durably with no synthetic live answer. Uploaded text is untrusted context; CEO answers do not authorize tools or external actions.

Server-sent events transmit committed snapshot changes and heartbeats through the authenticated Next proxy. Fresh short-lived DB sessions recheck identity, JWT expiry and session revocation; browser reconnect/polling reloads authoritative history. Provider token streaming is pending. Bounded text uploads use generated private storage keys, hashes and owner-only conversation access.

Design tokens support dark/light themes across preserved operational views. The shell provides persistent desktop collapse, mobile navigation, recent conversations and exact record deep links. Markdown rendering disables raw HTML and external image loads. No third-party font service is needed.

Latest Phase 2 UI foundation milestone is implemented; the next phase is Phase 3 real provider runtime/verification. Full UI integration, semantic memory, general message dispatch, measured benchmarks, dynamic workforce planning, dedicated runner evidence, production deployment and final client delivery remain incomplete. See IMPLEMENTATION_STATUS.md, AUDIT_REPORT.md and TEST_REPORT.md.
