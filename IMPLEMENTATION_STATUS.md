# Implementation status

Updated October 9, 2026. The authoritative request is [Phases 2–5](docs/PHASES_2_5_SPEC.md). Earlier roadmap phase numbers are historical. The audit began on clean `master` at `ae10711`; the previous tested application source was `4de41f5`.

**Current increment: Milestone A — Phase 2 workforce/provider foundation. Phase 2 is partially implemented; Phases 3–5 are not complete.** This increment adds real backend and UI functionality without certifying live AI or production deployment.

Published application source: **c28582ee6aa3ac9ba936c149a428feeaf01a1d60**. [All four GitHub Actions jobs passed](https://github.com/Sharath-holla/Aiventra/actions/runs/37829944013), including 98 Linux backend tests, nine real Compose/PostgreSQL browser tests and an actual container restart/integrity comparison. Local agent-work restart evidence and exact limits are recorded in TEST_REPORT.md.

## Implemented in this increment

- AES-GCM provider credential vault with an independent 32-byte key, tenant/provider/version-bound authenticated encryption, write-only owner API, replacement and revocation. Environment fallback and vault availability are reported separately. No ciphertext or saved key is returned in application state.
- Read-only, bounded account model discovery for OpenAI, Anthropic, Gemini, xAI, Ollama and explicitly allowed compatible endpoints. Catalog checks persist success/failure/time and account identifiers; capability/quality/pricing assertions are not inferred from a model name. Credential rotation invalidates an in-flight catalog check.
- Explicit owner-capped durable inference probes using the real gateway and an exact registered model. Successful structured inference is recorded separately from catalog connectivity. Missing eligible models wait without a paid call or reservation. No live account was verified during local development.
- Optimistic, organization-scoped employee/provider/project model preferences and intersecting allowlists. Manual probe/job overrides preserve capabilities, quality, sensitivity, context, fresh price evidence, independent review and every spend cap. Unaffordable preferences can fall back to cheaper qualified candidates without making an unaffordable call.
- Task-specific owner evaluations tied to successful real-provider run records, evaluator identity and notes. Their averages and recorded latency inform routing. This is not an automatic benchmark certification.
- Persisted agent invocation states, validated transitions and ordered event history. RUNNING requires an actual durable call marker; expired/revoked work is shown as blocked. Runtime totals are actual SQL aggregates. Registered roles remain on-demand, with fixture/live mode explicit.
- Owner-directed, scoped durable agent messages with UUID request deduplication, artifact boundary checks, correlation IDs and a two-hop reply bound. A recipient model produces a saved artifact before acknowledgement and a recorded response. Response messages do not recursively start more inference.
- General project meetings with 2–8 selected agents, 1–2 rounds and a bounded CEO synthesis. First-round participants receive the same saved project evidence without earlier verdicts; round two can inspect round one. Decisions persist and optional document follow-ups share the original job cap. Model output cannot create coding or deployment authority.
- Fenced cancellation for agent work. Late provider usage remains charged/recorded; cancelled output cannot publish an artifact or acknowledgement. Company/project/employee permissions are rechecked around inference.
- Connected provider key/discovery/default/restriction/probe controls, employee runtime/history/preferences, message/meeting forms, job results/cancellation and human evaluations. Retry of the same unresolved form submission retains its request ID.
- Additive migration `b02442d39feb`, retaining existing data and 13 monetary BIGINT columns. A private pre-migration SQLite backup was created. Dashboard redaction now reuses one secret snapshot per value tree, and runtime statistics avoid loading full model outputs.

## Verification and limits

See [TEST_REPORT.md](TEST_REPORT.md) for exact final counts, repaired failures and CI evidence. Controlled HTTP adapters and explicit fixtures test contracts; they do not establish live provider access. The local app was migrated and schema drift checked. Docker and Ollama remain unavailable on this Windows host.

Provider-native token streaming, native tool-call adapters/dispatch, model-specific automatic capability/benchmark probes, broader tool registry/templates, comprehensive recovery/load certification and lifecycle retention remain Phase 2 work. Existing workflow SSE streams committed snapshots. Job bodies and responses remain bounded; general autonomous delegation is not enabled.

## Remaining milestones

| Milestone | Actual state |
|---|---|
| A — Phase 2 | Core vault/catalog/routing/runtime/messages/meetings implemented; 98 backend and nine browser checks passed locally. Remote verification is recorded in TEST_REPORT.md. Live verification and remaining adapter/tool work pending |
| B — Phase 3 memory | Scoped keyword memory and saved conversation/artifact history exist; semantic embeddings/indexing, layered memory, version/provenance/retention still missing |
| C — Phase 3 workforce | Registered roles and fixed approved planning tasks exist; requirements-based team plans, staffing approval and distributed scheduling still missing |
| D — Phase 4 coding | Approved Git worktrees, actual patch/diff workflow and restricted runner implementation exist; Docker runner evidence, bounded repair, commits/PR/merge lifecycle and broader QA incomplete |
| E — Phase 5 delivery | Real intake, consultation, proposal and exact approval exist; complete engineering/final review/delivery/client acceptance incomplete |
| F–H | Dark/light shell and several connected screens exist. Full UX integration, production certification and publication of later milestones remain pending |

[Gap analysis](docs/PHASES_2_5_GAP_ANALYSIS.md) preserves the audit classification before this increment. Historical evidence remains in TEST_REPORT.md and Git history. No crypto repository, live cross-model collaboration, completed client software delivery or staging deployment is claimed.
