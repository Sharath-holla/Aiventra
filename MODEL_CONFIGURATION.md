# Model configuration

[Supported adapters and official interfaces](docs/providers.md) describe setup. Add server credentials to the private environment and configure real model identifiers/capabilities/source-backed prices. Restart API/worker when environment values change. Fixture mode never substitutes for a live request.

The registry now reports `missing_credentials`, `disabled` or `configured_unverified`. A live workflow without eligible configuration persists `waiting_for_provider` without a model run, spending reservation or failure attempt. Eligibility is reevaluated; an expired wait escalates instead of silently extending the deadline.

Coding review choices are `prefer_provider`, `require_provider` and `require_model`, with one/two review passes. Strict policies exclude the author and earlier reviewers; preferred policies record achieved diversity. Duplicate rows pointing to the same service/model do not satisfy strict independence. Two strict reviewers can require three configured identities. No live diversity was verified during this milestone.
