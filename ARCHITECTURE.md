# Aiventra OS architecture

The current increment follows [LIVE_EXECUTION_SPEC.md](docs/LIVE_EXECUTION_SPEC.md), continuing the four-phase specification. [NATIVE_EXECUTION.md](NATIVE_EXECUTION.md) describes native streaming/complete-response adapters, the closed tool registry, persisted traces and versioned microbenchmarks. The existing gateway still owns financial reservations and usage; tools run only after lease, role and exact project-approval checks. Peer document tasks share the parent cap and cancellation fences. No host command or deployment tool is exposed.

Migration 4666ed0d2d17 adds run_traces, tool_invocations, benchmark_results and benchmark_profiles. Native traces join authorized conversation SSE; final schema validation remains separate from provisional text. Benchmarks checkpoint cases and bind profiles to model/price/credential fingerprints; routing recommendations use current measured evidence without granting registry capabilities. Phases 3–5 remain incomplete.

The FastAPI/Next.js modular monolith is retained. [Detailed boundaries and diagrams](docs/architecture.md) describe the implementation. The authoritative roadmap is now [PHASES_2_5_SPEC.md](docs/PHASES_2_5_SPEC.md); both earlier specifications remain preserved.

The API owns authenticated, organization/client/project-scoped mutations. A separate worker owns durable database workflows, real model calls and restricted runner requests. SQLAlchemy/Alembic hold authoritative state; SQLite is verified locally and PostgreSQL/Compose is exercised in ephemeral CI. Monetary quantities use 64-bit storage. Private files plus database content hold artifacts. Generated code never executes directly in API/worker hosts.

The new default CEO workspace uses persisted `conversations` and `conversation_turns`. A unique conversation/request key, optimistic version and unique turn/workflow association prevent duplicate dispatch. Advisory turns use existing gateway policy/reservations/usage; consultation turns stage the existing seven-step consulting flow within the same fenced transaction. Exact proposal approval creates the existing project/tasks; URL links keep the conversation, requirement and project connected.

Conversation and turn caps join existing overlapping organization/project/agent/model/day/month caps. Cancellation invalidates the workflow lease, suppressing a late answer without pretending an in-flight provider charge disappeared. Missing models/credentials wait durably with no synthetic live answer. Uploaded text is untrusted context; CEO answers do not authorize tools or external actions.

Server-sent events transmit committed snapshot changes and heartbeats through the authenticated Next proxy. Fresh short-lived DB sessions recheck identity, JWT expiry and session revocation; browser reconnect/polling reloads authoritative history. Native model streams now persist provisional traces; final answers require validated output and usage. Bounded text uploads use generated private storage keys, hashes and owner-only conversation access.

Design tokens support dark/light themes across preserved operational views. The shell provides persistent desktop collapse, mobile navigation, recent conversations and exact record deep links. Markdown rendering disables raw HTML and external image loads. No third-party font service is needed.

Milestone A adds encrypted provider credentials and separate catalog/inference evidence, scoped model policies/evaluations, durable agent work and ordered invocation-state events. The existing gateway, financial ledger, worker leases/checkpoints, approvals and artifact storage remain authoritative. Message/meeting follow-ups are bounded server operations, not arbitrary model tool execution. A job cap overlaps all participants and optional document follow-ups.

A credential rotation invalidates connection evidence; cancelled work revokes its lease and suppresses late publication while preserving usage. Provider catalogs never infer undocumented capabilities/prices. Runtime statistics aggregate recorded runs in SQL, and recursive redaction snapshots environment secrets once per value tree. The additive migration preserves existing records and audit guards.

The authoritative phase numbers now refer to the Phases 2–5 specification. Phase 2 remains partial; semantic memory, dynamic staffing, complete engineering and client delivery are still unfinished. Historical UI milestone evidence remains in TEST_REPORT.md and Git history.
