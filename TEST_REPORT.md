# Aiventra verification report

## 0.2.0 — October 8, 2026

The original 44-test baseline was rerun successfully before changes. The final combined backend suite passed **64 tests, 0 failed, 1 dependency deprecation warning in 65.84 seconds**. Ruff lint and formatting passed across 48 API/test/script files. The warning does not establish an application failure.

- Browser: **3 passed in 27.2 seconds**, against real running API/worker/web. Coverage now checks worker readiness, request correlation, provider configuration display and coding review-policy/count controls. No live provider calls were made.
- Frontend strict typecheck, Prettier and optimized production build passed; production npm audit reported **0 vulnerabilities**.
- Ruff lint/format passed across API/tests/scripts. Alembic head is `e9c9f1ed55a6`; metadata check reports no drift. Migration tests upgrade a populated previous schema and verify workflow step/data preservation plus default wait context.
- The real running `/health/ready` returned `{"status":"ready","worker":"ready"}`. Worker/API were stopped/restarted with private database/artifacts retained.
- New automated checks cover logout reuse rejection, independent sessions, expiry, persistent/concurrent login counters, heartbeat expiry, positive/stale schema readiness, correlation, provider waiting without spending, same-step controlled-adapter resume and wait deadlines.
- Cross-model controls are tested with **controlled adapters and synthetic configuration/rates**. Strict policies reject duplicate registry identities. No live multi-provider verification is claimed.
- Real temporary Git worktree tests cover one/two review passes and successful/empty/failed baseline contracts. Runner results are explicitly mocked; actual container execution and successful autonomous code delivery remain unverified.
- `pip_audit` reported no known dependency vulnerabilities; the local application package is not audited by PyPI (installed package version remains 0.1.0; API milestone version is 0.2.0).
- The staged publication scan checked 113 blobs with **0 findings** before final document additions. Synthetic redaction fixtures have file/value-specific allowances. Re-run staged and public branch history scans before pushes. App-owned unpublished checkpoint refs are not pushed or counted as public history.
- GitHub publication is pending at this point. The authorized remote responds to a read query with no advertised refs; write permission and remote CI are not yet asserted.

The suite has one Starlette TestClient `httpx` deprecation warning. Alembic's configuration warning was removed using `path_separator=os`. Docker/Compose/PostgreSQL, cluster, real provider billing, S3 and actual crypto verification remain pending; none were substituted with simulated production evidence.

## Historical 0.1.0 evidence

Observed October 8, 2026, on Windows with Python 3.12.14, Node 24.21.0, npm 11.19.0, uv 0.12.3 and Git 2.55.0. The local API, worker and browser use SQLite. No live provider credentials, Docker runtime, PostgreSQL service or owner crypto repository were available for verification.

## Executed checks

| Check | Observed result |
|---|---|
| `python -m pytest -q` | **44 passed**, 1 dependency deprecation warning; 26.18 seconds |
| Ruff lint / formatting | All checks passed; 37 Python files already formatted |
| Alembic upgrade in isolated test | Succeeded; real SQLite tables and append-only audit trigger exercised |
| `alembic current` / `alembic check` | Head `b411d790aa01`; no new upgrade operations detected |
| `uv lock --check` / locked sync | Lock valid; 77 installed packages checked against locked environment |
| `npm run format:check` | All matched files pass Prettier |
| `npm run typecheck` | Strict TypeScript check passed |
| `npm run build` | Next.js optimized build succeeded, including static page generation and dynamic proxy route |
| `npm run test:e2e` | **3 passed**, 16.4 seconds, against real running API/worker/web |
| `python -m pip_audit` | No known vulnerabilities in audited dependencies; local `ai-company-os` package skipped because it is not a PyPI package |
| `npm audit --omit=dev` | 0 known vulnerabilities in production dependencies |
| Windows process lifecycle | Managed API/worker/web stopped and restarted while preserving database and artifacts; correct loopback ports inspected |
| Browser visual inspection | Desktop and 390px mobile dashboard screenshots reviewed; mobile document width fits viewport |

Commands are in README.md. The Starlette TestClient warning concerns deprecated `httpx` integration and a future `httpx2` transition; it did not fail tests. Playwright also emitted a terminal color-environment warning. Dependency scans do not constitute a source-code/security audit or guarantee absence of vulnerabilities.

## Master acceptance scenarios

| Scenario | Evidence and limit |
|---|---|
| A. New client consulting | Seven persisted model steps, specialist contributions, alternatives, unknown/partial cloud costs and no project before approval. Explicit fixture mode; live quality pending |
| B. Approval | Exact version/hash/selection, duplicate approval idempotency, four assigned dependent planning tasks and artifacts; stale revision pauses the project |
| C. Coding | Real temporary Git repo and isolated worktree, actual file patch/diff, author/reviewer/QA separation, preserved original source. Runner is explicitly mocked; fixture review correctly refuses completion. **Real container tests and successful live coding remain unverified** |
| D. Cost optimization | Economy filters/order, structured-output quality escalation and deterministic recorded usage using synthetic configured test rates; no published provider prices or account benchmark claimed |
| E. Provider failure | HTTP fixture 429 rejection falls back to a distinct model. Interrupted/uncertain calls retain reservation and are not repeated blindly |
| F. Agent failure | Disabled employee and missing eligible models stop/escalate; owner retry remains bounded |
| G. Security | Auth/expiry, client/organization boundaries, CEO tool denial, agent permission audit, pause, origin rejection, secret/endpoint controls, deployment rejection audit/notification |
| H. Budget | Concurrent reservations cannot overspend, failed multi-cap reservation rolls back all updates; requirement/project exhaustion stops before a run/spend and alerts the owner |
| I. Crypto import | Synthetic read-only repository discovery excludes secrets; traversal/secret patch paths rejected; file batches validated before writing. **Owner crypto repository and real regression tests pending** |
| J. Recovery | Checkpointed runs reused across closed sessions and seven separate worker subprocess starts; concurrent lease claim exclusive; unique dispatch constraints present |

Additional tests cover actual HR specialist artifact work, scoped keyword memory, CRM optimistic versions, real migration execution and audit tamper detection/database mutation prevention.

Browser coverage signs in via the actual HttpOnly proxy, submits a fixture cloud brief, waits for a proposal, approves a project, inspects three stored dependencies, assigns HR artifact work, reads an artifact, verifies audit, opens the CEO employee and signs out. The other tests check mobile sizing and unauthenticated/invalid-origin rejection. Credentials are sent through the test request context and not entered into page snapshots; traces are off.

## Verification boundaries and remaining evidence

- Provider contract tests cover OpenAI, Anthropic, Gemini, Ollama and a compatible endpoint using mocked HTTP. Official request formats were checked; account access, model-specific behavior, latency and billing were not tested live.
- Restricted Docker commands are implemented, but Docker was unavailable. The mocked coding-runner test is control-flow evidence only. It does not prove execution success, real test coverage or sandbox security.
- PostgreSQL, Compose images, dedicated runner, S3 account storage, browser OIDC, OAuth connectors, staging deployment/rollback, production backup/restore, load and hostile multi-tenant behavior were not tested.
- Local record persistence across process restarts was observed. No full production backup restore drill or distributed failure certification was performed.
- CI files are included and use lockfiles; no remote CI job was run. Frontend production artifacts built locally; the currently served app uses the local development server.
- Screenshots and fixture records remain private under `artifacts/` and `data/`. An earlier diagnostic captured a previous local password; diagnostics were scrubbed, the password/signing key rotated and tests changed to avoid credential entry in the page.

Consult IMPLEMENTATION_STATUS.md before interpreting any feature as complete. Remaining work is in NEXT_STEPS.md.
