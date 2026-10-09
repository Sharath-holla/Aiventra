# Next steps

## Current verified milestone order

Memory source 4e57760 has all four CI jobs green, with actual PostgreSQL vectors/versions retained across service restarts. Workforce planning and orchestration now have implementation and connected UI; finish their regression/restart/publication checks, then immediately implement the dedicated Docker broker, real sample-repository isolation/build/test evidence, bounded repairs and PR preparation. Provider credentials remain deferred. Older "not implemented" entries below are historical, not the current source audit.

## Current owner order — Phase 3, then Phase 4

Follow [PHASE3_MEMORY_WORKFORCE_SPEC.md](docs/PHASE3_MEMORY_WORKFORCE_SPEC.md). Provider keys are deferred; do not request them as a prerequisite.

1. Finish and publish the semantic-memory vertical increment after actual PostgreSQL/pgvector/local-model and restart CI evidence. Preserve bounded source/version/ACL behavior, local cached embeddings and honest keyword fallback.
2. Implement requirements-based workforce plans, editable exact approval, logical worker capacity, model/skill/cost evidence, dependency scheduling, pause/resume/reassignment/utilization and connected monitoring. Preserve existing approved document tasks and avoid duplicate work or uncontrolled model concurrency.
3. Complete actual dedicated runner isolation checks using a harmless sample, then bounded repair/build/test/diff/independent-review and PR preparation. Do not execute generated code on API/worker hosts or pass host secrets/Docker control into generated-code containers.
4. Continue client delivery and operational certification only from verified execution evidence. Existing Phase 1–2 features and tests remain regression requirements.

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
