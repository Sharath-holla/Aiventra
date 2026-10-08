# Work queue

Follow [the latest production specification](docs/PRODUCTION_UPGRADE_SPEC.md), with evidence in IMPLEMENTATION_STATUS.md and TEST_REPORT.md. Prior master briefs remain preserved; their phase numbers are historical. Authorized remote: `origin` → `https://github.com/Sharath-holla/Aiventra.git`, ordinary pushes only.

Tested source `4de41f57c3d0c999a98a9f453ded8f368dc29443` is published on `master`. [CI 37818487850](https://github.com/Sharath-holla/Aiventra/actions/runs/37818487850) passed all four jobs: 81 Linux backend tests, seven Compose/PostgreSQL browser tests, schema/13-column monetary contracts and real service-restart conversation/document recovery. Local tests passed 81 backend/seven browser checks; the app is running with worker readiness verified.

## Next phase — Phase 3: Real AI Runtime

1. Add server-side provider connection tests and account-supported model discovery with timeouts, persisted outcomes, secret-free diagnostics and explicit owner controls. Configuration alone must never show Connected. Reuse the five existing adapters and registry instead of rebuilding them.
2. Probe model-specific structured-output/capability support, surface actual failure/retry/fallback details and integrate verified provider state into the UI. Add provider-native token streaming with fenced cancellation and uncertain-call accounting; current conversation SSE streams saved workflow snapshots only.
3. With a real API credential or running Ollama endpoint, register an available model with documented capabilities/prices. Run a small owner-capped CEO answer and consultation, verify saved model identity, usage/ledger/failure recovery and actual account charges. A distinct second model/provider is required for genuine cross-model review evidence.
4. Confirm pause/readiness/revocation and same-step recovery using real provider failure/restart evidence. Preserve no-charge waits and uncertain paid-request reconciliation; never silently fall back to fixtures.

No API credentials or running Ollama instance were available for this milestone. Steps 1-2 can be implemented without inventing live results; step 3 requires the external configuration.

## Remaining UI foundation and full integration

- Add navigation for conversation turns older than the latest 100, optional title editing/retention controls, syntax highlighting, direct specialist discussions and links from completed approvals to project delivery context.
- Finish the Phase 9 workforce drawer/organization map, richer project activity/memory/task tabs, provider diagnostics and full accessible mobile/keyboard behavior. Current private document preview has focus trapping/restoration; no comprehensive accessibility certification is claimed.
- Paginate legacy state collections and test large-company latency. Conversation history already has search/50-record pagination; snapshot/query load still needs production measurements.
- Add PDF/image ingestion and permission-scoped repository URL import with real evidence extraction. Current attachments are small UTF-8 text files; local repository discovery remains a separate approved engineering operation.

## Later phases in dependency order

4. Routing: measured capability/quality/latency evaluations, explicit model overrides, adjustable scoring, invoice and cached/reasoning usage reconciliation.
5. Memory: scoped semantic indexing/retrieval, provenance, versioning and retention/erasure, preserving client/project boundaries.
6. Orchestration: durable message dispatch/acknowledgement/retries, dynamic approved delegation, dead letters and distributed restart/load tests.
7. Consulting/workforce: invitation-based client access, live research/complete rate comparisons, exact staffing and budget approvals, dynamic PM/team plans.
8. Coding/QA: dedicated hardened Docker runner, successful nonempty baseline/final tests, real independent reviews, bounded repair and security/PM acceptance. Compose integration does not certify the separate code runner.
9. UI integration: complete the remaining connected workspaces against real backend data/actions.
10. DevOps/security: browser OIDC if required, trusted edge address limits, session/heartbeat retention, encrypted restore drills, metrics/traces, secret manager and adversarial isolation/load verification.
11. Delivery: approved staging connector, health/smoke/rollback, client acceptance and genuine end-to-end implementation. Supply the actual owner crypto repository before its baseline/feature/testnet work.
12. Publication: run local/CI checks, staged/history secret scans, ordinary commits/pushes, verify remote SHA and record CI outcomes. Never mark the whole product complete based on fixture workflows.

## External configuration still required

- One supported provider API key and available model, or an actual running local Ollama instance; second independent model/provider for live verification.
- Dedicated Docker runner access for generated-code tests. Docker is absent on the current Windows host; Compose services can run in ephemeral GitHub CI.
- Actual owner crypto repository, excluding wallet/exchange secrets.
- Production identity/invitations, optional S3 storage, staging/cloud and OAuth mail/calendar accounts only when those phases are implemented and authorized.

Do not expose private `.env`, credentials, database contents or uploaded documents in commits, logs or screenshots. Keep code execution disabled until the dedicated runner is verified.
