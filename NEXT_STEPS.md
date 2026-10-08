# Work queue

See `IMPLEMENTATION_STATUS.md` for verified progress. Continue in dependency order, updating evidence after each milestone.

## Immediate Aiventra continuation

Current phase: **Phase 1 — Production Foundation**. Preserve the verified 0.2.0 modules. The authorized Git remote is `origin` → `https://github.com/Sharath-holla/Aiventra.git`; push only with ordinary Git updates, never force.
Source milestone `ca51145` is published on `master`. [All four CI jobs passed](https://github.com/Sharath-holla/Aiventra/actions/runs/37804290311): 66 Linux backend tests, frontend build/audit, secret scan and real PostgreSQL/Compose plus 3 browser tests. PostgreSQL BIGINT storage, large concurrent reservations, concurrent login counters, audit mutation rejection and schema drift checks passed. Windows backend tests also passed 66 checks. The first run's Linux import/hostname failures are repaired.

1. Configure one supported real provider in the private environment, or a running local Ollama instance. Register the exact available model/capabilities and documented pricing. Run a small owner-capped consultation, verify persisted usage and compare actual account billing; configure a distinct reviewer model/service for live review evidence.
2. Make a dedicated Docker runner available. Compose services already pass remotely, but code execution remains disabled there. Exercise an approved Python/Node coding task with nonempty actual tests, independent review and failed-test/timeout/output-limit behavior. Then validate service/host restart persistence and PostgreSQL load beyond these contract checks. Existing loopback development services must be stopped before local Compose startup.
3. Finish operational validation: pin/review deployed images, test encrypted backup/restore and real failures, and verify trusted proxy source limits plus session/heartbeat retention. The passing ephemeral CI stack is not a production restore/load certificate.
4. Finish foundation: secure invitation provisioning/client scope, browser OIDC if required, trusted source-rate-limit integration, operational session/heartbeat retention, robust health/error monitoring and restore drill. Then proceed to Phase 2 registry/runtime depth and Phase 3 benchmarks/memory. Do not jump to a decorative Phase 8 redesign in place of these gates.

Later phase priorities remain dynamic workforce allocation, autonomous repair and security/PM acceptance, client delivery/acceptance, semantic memory, durable communication and supported staging connectors. The actual crypto repository is required for Phase 11 evidence.

## Next verification milestones

1. Configure one real provider in the private server environment and register an account-supported model with official capabilities and source-backed prices. Run a small capped live consultation; compare actual usage, failures and account billing. Keep fixture and live evidence separate.
2. Use a dedicated Docker runner in a suitable environment. Basic PostgreSQL migrations, audit triggers and concurrent cap/login contracts are verified remotely; extend distributed claims/load/restart evidence and exercise an approved Python/Node coding task with actual nonempty tests. Validate failed-test, timeout, output-limit and independent-review behavior. Do not execute generated code directly on the host.
3. Supply a copy of the owner's actual crypto repository under the configured root, preserving uncommitted work and excluding wallet/exchange secrets. Inspect its discovery report before selecting its runner/test framework. Record genuine baseline evidence; authorize specific changes only after the scope is concrete.

## Core workflow extensions

- Add measured benchmark/evaluation records, routing override and configurable cost/quality weights. Import provider invoices and reconcile cached/reasoning usage. Sync agent cost-setting changes with existing cap records and define approval semantics for cap increases.
- Add exact approval records for budget changes, environment changes and external actions. Revocable local sessions and database login limits are now implemented; add invitation provisioning, OIDC browser login, retention and the client review portal.
- Expand PM planning to epics/sprints, capacity, deadlines, accepted deliverables and parallel isolated coding tasks. Add bounded repair, dependency installation with approval, framework runners, coverage, commits, reviewed PRs and merge-conflict handling.
- Build a general durable communication delivery service with idempotent receivers, acknowledgments, bounded retries and escalation. Preserve correlation and authorization throughout the dispatch.
- Improve retrieval with permission-scoped pgvector indexing and citation provenance. Add supported rich document ingestion and memory retention/erasure policy. Do not mix client/project context.
- Add pagination/search for all collections, richer run/approval details, direct employee conversations and agent/organization performance metrics. Keep every visible action connected to a meaningful server operation.

## External operations

- Implement staging deployment with QA evidence, exact environment approvals, smoke tests and rollback before offering production deployment.
- Implement supported OAuth mail/calendar connectors, drafts/replies and explicit external-effect approval. Add authorized lead research and CRM integrations. Never treat a saved draft as a sent message.
- Provide normalized department workflows for HR, sales, marketing, finance, support and legal work; generic document tasks alone do not fulfill their entire operating scope.

## Production hardening

- Adopt/test Temporal or a comparably verified distributed workflow engine, preserving uncertain-request reconciliation and idempotency.
- Exercise encrypted backup/restore and real process/host/network failures. Add metrics, trace export, log retention, alert delivery and independent audit anchoring.
- Use a managed secret store, least-privilege database roles and dedicated hardened runner hosts. Complete adversarial sandbox/tenant tests, PostgreSQL/load tests and security review before public deployment.
- Preserve the passing remote backend/frontend/secret/Compose/browser gates and add container/image scans. Record each source commit's actual result; local success is not remote CI evidence.

Update IMPLEMENTATION_STATUS.md, TEST_REPORT.md and CHANGELOG.md after each milestone. Keep the full original brief as the acceptance target.
