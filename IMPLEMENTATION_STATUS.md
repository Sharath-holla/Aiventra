# Implementation status

Updated October 8, 2026. Version 0.2.0 extends the existing local foundation; the current Aiventra phase is **Phase 1 — Production Foundation, in progress**. Phase 0 source/test audit is complete. **The full product remains incomplete and is not production-certified.** File existence, a fixture response and a mocked runner result are not live evidence.

The authoritative upgrade target is [AIVENTRA_MASTER_SPEC.md](docs/AIVENTRA_MASTER_SPEC.md); the [earlier brief](docs/MASTER_BUILD_PROMPT.md) remains preserved. See [AUDIT_REPORT.md](AUDIT_REPORT.md), [TEST_REPORT.md](TEST_REPORT.md) and [NEXT_STEPS.md](NEXT_STEPS.md).

## Verified 0.2.0 progress

- Local JWTs bind persisted, expiring sessions. Server logout revokes one session; clearing a cookie alone is no longer the security boundary. Existing older JWTs without a session ID require signing in again. Owner credentials and project data are preserved.
- Login counters are atomic database records keyed by hashes of account/source identifiers. They survive API restarts. The proxied deployment's source address is shared unless a trusted edge integration is implemented; that limitation remains explicit.
- Liveness and readiness are separate. Readiness requires the current migration head and a fresh persisted worker heartbeat. Authenticated runtime state exposes provider configuration facts without secret values or live-connectivity claims.
- Missing eligible live models/credentials or strict review diversity produces `waiting_for_provider`, persists exact routing needs, uses no paid call/reservation and consumes no failure attempt. Configuration changes requeue the same step; wait expiry escalates. This is not a live-success claim.
- Coding task scope includes owner-selected diversity and one/two reviews. Endpoint/model identities prevent duplicate registry rows from fabricating diversity. Reviewer verdicts are not shared before their initial assessments. Evidence records author/reviewer run/model IDs and achieved diversity. Strict choices wait when impossible; preferred diversity reports reduction.
- Failed/empty baseline tests prevent patch generation. Both baseline and final QA detect interrupted running execution records, preventing blind replay. Real Docker validation, security/PM acceptance and bounded repairs remain incomplete.
- Requests carry correlation IDs through browser proxy and API logs; worker logs use workflow correlation. Structured application logs avoid request bodies, secrets and raw exception details.
- A staged/branch-history secret scanner and CI secret/container/browser checks are included. Compose worker/web health checks and container Git availability were repaired; those container changes remain unverified locally because Docker is absent.
- All four remote CI jobs passed on `3ade79d`, including real PostgreSQL/Compose startup and 3 browser tests. Monetary storage now has a 64-bit PostgreSQL migration, with populated SQLite preservation checks; extended PostgreSQL contract checks must pass on its subsequent CI run.

## Aiventra phase coverage

| Phase | Current status |
|---|---|
| 0 — Audit | Complete local source/test audit; not an external security certification |
| 1 — Production foundation | Local repairs tested; Compose/PostgreSQL/browser CI passed. Live providers, production identity/operations and extended PostgreSQL checks outstanding |
| 2 — Core execution | Existing bounded role/tool/document/coding runtime retained; live execution and richer employee capabilities incomplete |
| 3 — Routing/memory | Filtering/caps/keyword persistence functional; benchmarks, semantic memory and full memory lifecycle incomplete |
| 4 — Enterprise orchestration | DB durable flows/approvals/watchdog functional; general bus/Temporal and full delegation incomplete |
| 5 — Consulting | Fixture end-to-end consultation/owner approval functional; live research quality and client portal incomplete |
| 6 — Workforce allocation | Fixed dependent plan and manual assignment functional; dynamic approved team/concurrency planning incomplete |
| 7 — Engineering | Git worktree/patch and review gates functional; cross-provider contracts tested. Actual Docker/live coding/repair/security/PM acceptance unverified or incomplete |
| 8 — UI redesign | Connected essential views retained; comprehensive dark conversation workspace not implemented |
| 9 — Business departments | Persistent records and artifact tasks functional; external/departmental programs incomplete |
| 10 — DevOps hardening | Local/CI definitions exist; cluster manifests, actual infrastructure validation and hardening pending |
| 11 — Crypto readiness | Synthetic generic import tested; actual owner repository and regression evidence absent |
| 12 — Publication/final verification | Milestones published normally to authorized `origin/master`; all CI jobs passed on `3ade79d`. Full final product acceptance is not achieved |

## What an owner can use now

The Next.js dashboard and FastAPI backend persist real state in SQLite. A separate worker extracts a requirement, collects CTO, Cloud Architect, Security Architect, FinOps Engineer and CFO contributions, creates alternatives and a proposal, then stops for exact owner approval. Approval creates a project, ordered milestones and four dependent planning tasks. Their saved artifacts have integrity hashes. This flow has automated backend and browser coverage using **explicit local fixtures**.

Owners can configure employees and providers, inspect routing and usage, change caps, pause work, acknowledge alerts, assign document work to a permitted specialist, maintain business records and verify the audit chain. Model calls, code execution and external effects have separate boundaries. Planning/artifact completion does not mean software was implemented, semantically validated or deployed.

## Earlier brief coverage retained

| Master phase | Implemented and locally tested | Remaining or unverified |
|---|---|---|
| 1. Engineering foundation | Modular FastAPI/Next.js monorepo, persisted authentication/throttling, tenant/RBAC checks, migrations, health, HttpOnly proxy, Windows startup/stop, responsive UI, locked dependencies; real PostgreSQL/Compose/browser CI passed | Browser OIDC flow, trusted edge source limits, production deployment and operational validation |
| 2. Organization and agents | 16 departments, 136 initial roles, reporting hierarchy, policies, responsibilities/objectives, tools, instance cloning, pause/routing settings, scoped document execution and persisted run history | Department-specific autonomous tool programs, measured employee evaluations, training/skill registry, recruitment and comprehensive working-memory controls |
| 3. Model routing and finance | Five HTTP adapters with official-format contract fixtures; capability/quality/context/sensitivity/freshness filtering; economy/balanced/quality/fastest ordering; three-model bounded fallback; usage ledger, atomic overlapping caps and uncertain-call reconciliation | Live account verification, benchmarks, learned/custom scoring weights, explicit per-task model override, invoice ingestion and provider billing reconciliation |
| 4. Client consulting | Versioned intake/clarification, text evidence upload, allowlisted source retrieval, persisted specialist meeting contributions, CFO interpretation, deterministic partial rate arithmetic, alternatives, exact proposal approval/rejection/change requests | Live recommendation quality, comprehensive research and rate extraction, PDF/diagram ingestion, cost completeness certification and client-facing approval portal |
| 5. Project management | Proposal-to-project creation, milestones, assigned tasks, actual dependencies, durable dispatch, cancel/pause, artifacts, owner specialist-task assignment | Epics/sprints, resource/capacity scheduling, deadlines/critical path, dynamic PM delegation and full autonomous implementation planning |
| 6. Engineering and QA | Read-only discovery, owner-approved isolated real Git worktree, batch-validated files, actual diff artifact, independent review identity and QA runner interface; fixture review cannot certify code | Docker execution unavailable on this host; live coding not verified. Framework/dependency installation, autonomous repair, coverage, commits/PRs/merges, conflict resolution and parallel developer coordination pending |
| 7. Deployment and operations | Deployment attempts are rejected, audited and alerted; Compose and operational instructions included | Supported staging/production connector, environment approval, smoke/health verification, release records, rollback and deployed observability |
| 8. Enterprise departments | Persistent clients/CRM/support/knowledge/incidents/campaign/email/calendar drafts, optimistic record updates, bounded owner command interface, specialist document tasks, independent watchdog, scoped keyword memory | OAuth/email/calendar execution, authorized outreach, lead discovery, invoicing/payment integrations, structured departmental programs and semantic retrieval |
| 9. Existing crypto project | Optional eight specialist roles; generic repository discovery and source protection tested on synthetic repositories; trading/transfer effects unavailable | Actual owner repository has not been supplied. Real stack discovery, baseline/regression results, approved feature changes and testnet integration pending |
| 10. Hardening | Local workflow restarts, concurrent claims/caps, tenant controls, stale approvals, path/secret controls, audit SQL mutation guard, dependency scans and browser checks | PostgreSQL load/concurrency, restore drill, hardened dedicated runner adversarial testing, distributed fault tests, metrics/tracing backend, external immutable audit anchoring and security review |

## Implementation boundaries

- The worker is a transactional database state machine with leases and checkpoints. Temporal migration remains pending. Message records have correlation/status and owner acknowledgments; a general delivery/retry bus is not implemented.
- Live adapter payloads are covered by mocked HTTP contracts. No live model identifiers or token prices are preloaded. Owner-entered quality scores are not measured benchmark results.
- Live runs display computed token-cost estimates. Cloud comparisons remain partial or unknown. Budget counters overlap and must never be summed as total spending; the transaction ledger is the spending source.
- Private local files plus database content hold artifacts. Optional S3 writes exist but have not been verified against a real account. Keyword project retrieval is implemented; pgvector retrieval is not.
- Docker commands are restricted and code execution is disabled by default. The coding test uses real Git operations and an explicitly mocked runner. It proves control flow, source preservation and review separation, not containment or real test success.
- The default client browser provides basic scoped intake; invitation provisioning and comprehensive client proposal/project portals remain incomplete. Owner chat supports documented commands, not unrestricted natural-language or direct-agent tool orchestration. Public registration is deliberately excluded by the Aiventra brief.
- Snapshot collections are capped at 300 records; complete pagination is pending. Structured telemetry/export and large-company performance have not been certified.
- SQLite is for private local use. OIDC bearer verification exists, but the browser login does not implement an OIDC authorization-code flow. Public hosting is not an appropriate next step without the tracked hardening.

## Current local handoff

Use `scripts/start.ps1` to start the web/API/worker, or `scripts/stop.ps1` to stop managed processes without deleting data. Owner credentials live only in private `.env`. Browser tests leave clearly named fixture requirements/projects for inspection. Original user repositories have not been modified.
