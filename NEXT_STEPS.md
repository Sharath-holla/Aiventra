# Next steps

Follow [the current Phases 2–5 specification](docs/PHASES_2_5_SPEC.md). Preserve existing working modules and publish verified increments to [the authorized repository](https://github.com/Sharath-holla/Aiventra) with ordinary pushes.

## Finish Milestone A — Phase 2

The core increment is published at c28582e, with all four GitHub Actions jobs passing. Exact verification is in TEST_REPORT.md.

1. Add provider-native token streaming and native tool-call/cancellation contracts with a server tool registry, permission-bound dispatch and uncertain-usage handling. Current SSE streams saved workflow state, and current agent tools are server-directed workflow operations.
2. Add explicit model-specific capability probes and a reproducible quality benchmark suite. Current catalog IDs are account facts; manually configured capabilities and owner grades are distinct from automatic verification.
3. With a real API account or actual Ollama endpoint, discover a real model, configure documented capabilities/current prices, run the capped inference probe and verify usage/account charges. Run a real CEO answer, document task, message and bounded meeting. Configure distinct services/models for actual independent coding review.
4. Extend role templates/tool metadata and recovery/dead-letter handling, then exercise concurrent/restart/failure behavior. Preserve no-charge waits, duplicate-request protection, lease fences and owner reconciliation for interrupted paid calls.

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
