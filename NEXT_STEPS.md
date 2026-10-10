# Next steps

## Milestone 2 continuation

1. Preserve the verified `af5b85c` transfer/recovery increment: [all five source CI jobs passed](https://github.com/Sharath-holla/Aiventra/actions/runs/38018391046), including actual database restart/separate restore equality. Read docs/ENTERPRISE_MILESTONE_2_SPEC.md, DATABASE_MIGRATION.md and TEST_REPORT.md. Keep ZERO_COST_ONLY and all existing tenant/approval/audit/runner boundaries; do not rerun/rebuild completed modules without a relevant change.
2. Configure an authorized private `MIGRATION_DATABASE_URL` for a **new empty** local PostgreSQL database; verify pgvector availability/permissions. No password reset or credential guessing is authorized. Dry-run the transfer, stop every writer, apply and compare the retained snapshot, explicitly select PostgreSQL for API/worker with `REQUIRED_DATABASE_BACKEND=postgresql`, then test actual login/scoped workflows/memory/restart before admitting writes. SQLite remains active until that succeeds.
3. Install Ollama and an explicitly approved small local model only after sufficient memory is available. MODEL_CONFIGURATION.md records measured hardware, official installation/download commands and remaining quality tests. Disable cloud features, verify local metadata and measure real conversation/extraction/planning/coding/repair/tools/structured output. Exercise saved BA → CTO → PM handoffs and restart persistence. Failed/unsupported tasks remain waiting; fixtures never count as live results.
4. Implement PR_PUBLICATION_WORKFLOW.md's missing least-privilege GitHub connector with exact commit/diff/target preview, versioned owner approval, non-force push, draft PR idempotency, persisted URL, CI/review retrieval and repair updates. Verify only against an explicitly authorized disposable repository; no generated PR has been published.
5. Connect verified engineering/QA/final review to delivery artifacts/client acceptance. Finish encrypted offsite backups/PITR, runtime-role least privilege, production identity/monitoring, cluster/staging/rollback and load verification separately. Current CI restore is a disposable database drill, not production disaster recovery.

External needs: authorized local PostgreSQL access/pgvector and local Ollama installation/model approval; a scoped publication connector/repository authorization for generated PRs. No paid AI API key is required or requested.

## Current enterprise continuation — after zero-cost milestone

Enterprise milestone 1 is published as **0e8797d1e255af68bb80d9db868eb818151c7719** with [all five CI jobs passing](https://github.com/Sharath-holla/Aiventra/actions/runs/37983863735). Continue milestone 2; do not rebuild the preserved foundations or relax ZERO_COST_ONLY.


1. Keep `AI_SPENDING_MODE=ZERO_COST_ONLY`. Revoke credentials disclosed in chat; none were installed or used by this milestone. Do not enable remote inference from zero prices, subscriptions, credits or catalog success.
2. Enterprise milestone 2: obtain authorized access to the existing local PostgreSQL 18 instance, inspect database ownership/migrations/pgvector, and prepare a backed-up, reversible SQLite-to-PostgreSQL transition. Preserve all records and explicitly select one authoritative database. Do not guess credentials or silently replace the current SQLite database.
3. Provision an approved local Ollama service/model without automatic large downloads; read-only inventory reports 7.3 GiB system RAM, six CPU cores and an RX 6500M, with compatibility still unverified. Verify installed GGUF metadata and real local inference, then capability benchmarks and independent review. Docker Compose needs an explicit isolated local inference service design; host loopback is not container loopback.
4. Implement remote-free entitlement verifiers only where provider-enforced no-billing evidence is available. Until then remote inference stays denied. No paid fallback or mode is implemented.
5. Continue exact-approved generated branch/PR publication using PR_PUBLICATION_WORKFLOW.md; then client delivery/acceptance, invitations/OIDC, independent watchdog, encrypted offsite restore drills and production hardening.

Current implementation: enterprise milestone 1, with Phase 3 foundations and the verified Phase 4 runner increment preserved. No production deployment, live provider success, generated remote PR publication or imported-crypto execution is claimed. Historical next-step lists below retain prior numbering.


## Current verified milestone order

Phase 3 memory, staffing and persistent orchestration are complete. Published source c6dd90e has all five CI jobs green, including actual PostgreSQL/pgvector recovery and dedicated Docker runner isolation/build/test/cancellation/restart evidence. Provider credentials remain deferred. Older "not implemented" entries below are historical, not the current source audit.

## Current owner order — complete Phase 3, continue Phase 4

The provider-free Phase 3 specification and the current runner recovery/repair increment are complete and published. Continue with scoped GitHub PR publication and provider-backed coding only after the owner connects credentials.

1. The runner recovery/repair/PR-draft increment is published and passed local tests plus all five CI jobs. Preserve the backend's owner reconciliation and exact approval fencing as follow-on work proceeds.
2. Add bounded authenticated GitHub PR publication for persisted, reviewed drafts, with owner approval and idempotent retry. Do not enable automatic merge or expose a GitHub token to model input or the generated-code container.
3. Exercise a real provider-backed patch and independent review only after the owner connects credentials; keep no-provider operation explicit and do not represent deterministic adapters as live AI.
4. Continue Phase 5 client delivery from verified coding results: final QA/PM/security approval, delivery bundle and scoped client acceptance. Preserve Phase 1–3 regression requirements.

The prior provider-first roadmap below is historical; it does not override the owner's explicit provider-free development order.

Follow [the current Phases 2–5 specification](docs/PHASES_2_5_SPEC.md). Preserve existing working modules and publish verified increments to [the authorized repository](https://github.com/Sharath-holla/Aiventra) with ordinary pushes.

## Finish Milestone A — Phase 2

The vault/workforce core and native execution/microbenchmark increments are implemented. The latest continuation is [LIVE_EXECUTION_SPEC.md](docs/LIVE_EXECUTION_SPEC.md); TEST_REPORT.md records exact tested source and publication evidence.

Completed publication: source **8263fbd**, ordinary origin/master push, [all four CI jobs passed](https://github.com/Sharath-holla/Aiventra/actions/runs/37929934962). A documentation-only follow-up records the result. Begin the next increment from the actual current Git HEAD and preserve this tested implementation.

1. With a real provider account or actual Ollama, register a documented model/current rates, run bounded streaming/complete-response inference, a native tool task and a selected peer handoff, then micro-v1. Compare recorded usage to actual account billing; verify distinct real reviewer models. No live account has been verified.
2. Broaden model evaluation beyond micro-v1: representative business/architecture/coding/repair cases, independent assessment and reproducible isolated code-test evidence. Current keyword/AST/calculator scores are limited measurements, not broad semantic-quality certification.
3. Extend role templates/tool metadata, dead letters, distributed capacity/recovery/load coverage and retention. Preserve closed tools, no-charge waits, paid-call reconciliation, lease fences and shared handoff caps. Provider idle cancellation is bounded by the 15-second read timeout and cannot guarantee upstream billing stopped.
4. Proceed to Milestone B's provider-independent/local embeddings and scoped semantic persistence, then C–E below. Do not rebuild current working workflows or claim generated-code execution from native document tools.

## Milestone B — Phase 3 memory

Implement provider-backed semantic embeddings and a scope-filtered vector index, with an explicitly labeled keyword fallback. Add company/client/project/agent/task/conversation layers, source provenance, versioning, invalidation, retention and deletion. Connect semantic context to agents and UI; test tenant/client isolation and restart recovery. No semantic retrieval is currently implemented.

## Milestone C — Phase 3 workforce

Generate requirements-based team/task plans using registered role skills and real models. Persist plan versions and exact staffing/budget approval; allocate tasks only after approval. Add distributed capacity/concurrency constraints, budget-aware scheduling and actual assignment UI. Avoid permanent per-role inference processes and uncontrolled paid parallelism.

## Milestone D — Phase 4 engineering

Verify actual dedicated Docker runner isolation, nonempty Python/Node tests, timeout/output/cancellation cleanup and restart recovery in CI. Add bounded diagnosis/repair cycles with fresh independent reviews, then safe Git commits/PR/merge lifecycle and QA/PM/security acceptance. Never execute generated repository code on the API/worker host or modify a dirty original checkout.

## Milestone E — Phase 5 client delivery

Connect the existing intake/consultation/exact approval to approved team allocation, engineering, real test evidence, CTO/QA final review, delivery bundles and scoped client acceptance/change requests. Add invitation-only client accounts. Staging requires a real connector, environment approval and observed health/rollback; no fabricated preview URL or deployment status.

## Milestones F–H

Finish premium accessible UI integration, pagination and production performance checks; verify security, monitoring and recovery; run appropriate local tests, secret/dependency scans and CI before every commit/push. Update all status documents around actual evidence.

## External configuration

A real provider API credential and account model, or running Ollama; distinct reviewer models/services; a dedicated Docker runner; the actual owner crypto repository; and production identity, staging/cloud, optional private S3 and mail/calendar OAuth accounts when their integrations are implemented. GitHub authentication for this application's publication is available. Keep private .env, vault key, database, logs and user artifacts out of Git.
