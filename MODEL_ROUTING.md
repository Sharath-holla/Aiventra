# Model routing and provider evidence

The gateway supports OpenAI Responses, Anthropic Messages, Gemini generateContent, xAI/compatible chat completions and Ollama generate. All output is validated against an explicit schema; malformed output retains real usage before bounded fallback. Native provider token streaming and tool-call interfaces are not complete.

Catalog discovery uses actual account identifiers and bounded pages/bytes/time. It does not infer capability, quality, price, or successful inference. Catalog status and successful structured inference time/model are distinct persisted facts. Replacing a vault credential resets its evidence; rotation during a check prevents stale certification.

Mandatory filters precede preference/scoring: tenant, enabled provider/model, explicit live/fixture mode, capability, minimum quality, reliability, data sensitivity, context size, current price evidence, credentials, scoped allowlists, review diversity and atomic overlapping budgets. Project, agent and provider allowlists intersect. Preferences never bypass these filters. Explicit job/probe overrides select exactly that registered eligible model; they cannot silently switch models. Unaffordable preferences may yield to cheaper eligible candidates.

Economy, balanced, quality and fastest policies use configured data plus recorded latency and task-class owner evaluations when available. Evaluations retain actual run/model/evaluator provenance and cannot be attached to fixtures or a different workflow class. This is a human-evaluation framework, not an automatic benchmark claim. Inference fallback makes at most three distinct eligible paid attempts within runtime/deadline limits.

Every call records model, reason, usage, computed cost basis, held reservation, errors and result status. Company/project/task/conversation/turn/job/agent/model/day/month caps overlap. Unknown billing outcomes retain reservations for explicit reconciliation. Provider pricing and capability assertions must be supplied from documented account models; no live IDs or fabricated rates are seeded.

Official catalog contracts checked during implementation: [OpenAI](https://developers.openai.com/api/reference/resources/models/methods/list), [Anthropic](https://platform.claude.com/docs/en/api/models/list), [Gemini](https://ai.google.dev/api/models), [xAI](https://docs.x.ai/developers/rest-api-reference/inference/models), [Ollama](https://docs.ollama.com/api/tags). Live account verification remains pending credentials.
