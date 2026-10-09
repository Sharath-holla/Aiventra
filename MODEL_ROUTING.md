# Model routing and provider evidence

## Current mandatory filter: zero-cost eligibility

Before every routing preference or budget decision, ZERO_COST_ONLY blocks remote paid/unknown-cost models. Registry zero prices, keys and catalog success are not free-entitlement proof. Local Ollama requires credential-free loopback configuration and installed-GGUF metadata before each inference. Missing eligibility preserves WAITING_FOR_FREE_PROVIDER for explicit scoped owner resumption. See ZERO_COST_AI_POLICY.md and PROVIDER_ELIGIBILITY.md; historical remote adapter contracts below are fixture tests, not live authorization.


The gateway supports OpenAI Responses, Anthropic Messages, Gemini generateContent, xAI/compatible chat completions and Ollama generate. All output is validated against an explicit schema; malformed output retains real usage before bounded fallback. Native streaming and complete-response function interfaces now use the bounded adapters described in NATIVE_EXECUTION.md.

Catalog discovery uses actual account identifiers and bounded pages/bytes/time. It does not infer capability, quality, price, or successful inference. Catalog status and successful structured inference time/model are distinct persisted facts. Replacing a vault credential resets its evidence; rotation during a check prevents stale certification.

Mandatory filters precede preference/scoring: tenant, enabled provider/model, explicit live/fixture mode, capability, minimum quality, reliability, data sensitivity, context size, current price evidence, credentials, scoped allowlists, review diversity and atomic overlapping budgets. Project, agent and provider allowlists intersect. Preferences never bypass these filters. Explicit job/probe overrides select exactly that registered eligible model; they cannot silently switch models. Unaffordable preferences may yield to cheaper eligible candidates.

Economy, balanced, quality and fastest policies now incorporate fresh fingerprint-bound benchmark profiles, recorded latency and task-class owner evaluations. Manual policy requires an exact job override or employee model preference. Advisory recommendations enforce default quality/context/security/price constraints; every job separately enforces its actual scoped restrictions and caps. Evaluations retain actual run/model/evaluator provenance and cannot be attached to fixtures or a different workflow class. This is a human-evaluation framework, not an automatic benchmark claim. Inference fallback makes at most three distinct eligible paid attempts within runtime/deadline limits.

Every call records model, reason, usage, computed cost basis, held reservation, errors and result status. Company/project/task/conversation/turn/job/agent/model/day/month caps overlap. Unknown billing outcomes retain reservations for explicit reconciliation. Provider pricing and capability assertions must be supplied from documented account models; no live IDs or fabricated rates are seeded.

Official catalog contracts checked during implementation: [OpenAI](https://developers.openai.com/api/reference/resources/models/methods/list), [Anthropic](https://platform.claude.com/docs/en/api/models/list), [Gemini](https://ai.google.dev/api/models), [xAI](https://docs.x.ai/developers/rest-api-reference/inference/models), [Ollama](https://docs.ollama.com/api/tags). Live account verification remains pending credentials.
