# Agent orchestration

The existing [modular architecture](docs/architecture.md) uses a separate database worker with bounded role-specific model calls, conditional leases and fenced checkpoints. Organization/agent/project permissions and approval/cost limits remain server decisions. Workers are invoked on demand; registering a role does not start an LLM.

Provider waits, checkpoints, run IDs, failures and review evidence persist across processes. Every worker publishes a heartbeat while its event loop runs; stale heartbeat changes readiness. Requests and workflow failures carry correlation IDs. Independent watch monitoring remains active even when dispatch is paused.

The coding author cannot self-review or execute QA. Initial reviews share code/acceptance context without earlier verdicts; achieved model diversity is recorded. Actual container tests are still required. Temporal, general message delivery, dynamic workforce planning, rich employee programs and parallel developer coordination remain incomplete.
