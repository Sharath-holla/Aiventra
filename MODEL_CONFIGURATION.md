# Model configuration

## Milestone 2 local inventory and next setup

ZERO_COST_ONLY remains mandatory. Remote inference is blocked even if a credential/catalog is available; no free entitlement verifier is implemented. No disclosed chat key was installed or used. Existing encrypted vault, adapters, streaming/tool traces, benchmarks and guarded resume are preserved. No live LLM output or new provider capability is claimed.

The Windows workstation has a Ryzen 5 5600H (6 cores/12 threads), 7.34 GiB visible RAM, RX 6500M with approximately 4 GiB reported VRAM, integrated graphics and 338.31 GiB free C: disk space. Only 0.72 GiB RAM was free at the inventory point while development services/tests were running. GPU compatibility and usable inference memory remain unverified. Ollama is absent at the standard installation path, no daemon responds at 127.0.0.1:11434 and no model was downloaded. This is insufficient evidence to provision a larger model automatically.

After owner-authorized installation using the [official Windows instructions](https://docs.ollama.com/windows), disable cloud features (`OLLAMA_NO_CLOUD=1`), keep the daemon loopback-only and restart it as described in the [official FAQ](https://docs.ollama.com/faq). Start with one loaded model and one inference at a time; free RAM first and use a bounded context. The following are candidates for measurement, **not certified agent assignments**:

| Purpose | Candidate and explicit download command | Published download size |
|---|---|---|
| Small smoke test | `ollama pull qwen3:0.6b` | [523 MB](https://ollama.com/library/qwen3:0.6b) |
| Medium general comparison, after memory headroom is available | `ollama pull qwen3:1.7b` | [1.4 GB](https://ollama.com/library/qwen3:1.7b) |
| Small coding comparison | `ollama pull qwen2.5-coder:1.5b` | [986 MB](https://ollama.com/library/qwen2.5-coder:1.5b) |

Download size is not runtime RAM/VRAM usage. Official catalog capabilities do not demonstrate quality on this machine. Register an installed local model with zero rates and the loopback Ollama adapter; verify installed GGUF metadata through the existing UI before explicitly resuming a saved task. Run existing micro-v1 and then business/architecture/PM/coding acceptance workflows, recording actual outputs, errors, duration, usage and resource observations. Do not assign complex roles if quality fails. Real local inference, BA → CTO → PM handoffs, independent review quality and autonomous coding remain pending this installation/measurement step. Deterministic tests are infrastructure evidence only. No paid fallback is allowed.

The setup notes below describe existing interfaces; they do not authorize remote inference or override current spending policy.

[Supported adapters and official interfaces](docs/providers.md) describe setup. Store credentials through the encrypted owner-only provider controls or use a dedicated private environment reference and configure real model identifiers/capabilities/source-backed prices. Restart API/worker when environment values change. Fixture mode never substitutes for a live request.

The registry now reports `missing_credentials`, `disabled` or `configured_unverified`. A live workflow without eligible configuration persists `waiting_for_provider` without a model run, spending reservation or failure attempt. Eligibility is reevaluated; an expired wait escalates instead of silently extending the deadline.

Coding review choices are `prefer_provider`, `require_provider` and `require_model`, with one/two review passes. Strict policies exclude the author and earlier reviewers; preferred policies record achieved diversity. Duplicate rows pointing to the same service/model do not satisfy strict independence. Two strict reviewers can require three configured identities. No live diversity was verified during this milestone.

Catalog connectivity and successful inference are persisted separately. Catalog IDs do not automatically establish capabilities, quality or pricing. The independent PROVIDER_SECRET_KEY enables encrypted storage; removing a stored key can reveal an existing environment fallback. See MODEL_ROUTING.md for scoped preferences/allowlists, owner evaluations and bounded inference probes. Native streaming and complete-response tool adapters, a closed server tool registry and automatic microbenchmarks are implemented. Add the streaming capability explicitly for supporting models. See NATIVE_EXECUTION.md for scope and live-verification limits.
