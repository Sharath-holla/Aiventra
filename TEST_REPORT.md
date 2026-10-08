# Aiventra verification report

## 0.2.0 — October 8, 2026

The original 44-test baseline was rerun successfully before changes. After the foundation work, portability fixes and monetary migration, the latest combined backend suite passed **66 tests, 0 failed, 1 dependency deprecation warning in 64.76 seconds**. Ruff lint and formatting passed across 49 API/test/script files. The warning does not establish an application failure.

- Browser: **3 passed in 27.2 seconds**, against real running API/worker/web. Coverage now checks worker readiness, request correlation, provider configuration display and coding review-policy/count controls. No live provider calls were made.
- Frontend strict typecheck, Prettier and optimized production build passed; production npm audit reported **0 vulnerabilities**.
- Ruff lint/format passed across API/tests/scripts. Alembic head is `f20b34705a81`; metadata check reports no drift. Migration tests upgrade populated previous schemas and verify workflow/data/large monetary balance preservation, default wait context and retained audit triggers.
- The real running `/health/ready` returned `{"status":"ready","worker":"ready"}`. Worker/API were stopped/restarted with private database/artifacts retained.
- New automated checks cover logout reuse rejection, independent sessions, expiry, persistent/concurrent login counters, heartbeat expiry, positive/stale schema readiness, correlation, provider waiting without spending, same-step controlled-adapter resume and wait deadlines.
- Cross-model controls are tested with **controlled adapters and synthetic configuration/rates**. Strict policies reject duplicate registry identities. No live multi-provider verification is claimed.
- Real temporary Git worktree tests cover one/two review passes and successful/empty/failed baseline contracts. Runner results are explicitly mocked; actual container execution and successful autonomous code delivery remain unverified.
- `pip_audit` reported no known dependency vulnerabilities; the local application package is not audited by PyPI (installed package version remains 0.1.0; API milestone version is 0.2.0).
- The final staged publication scan checked **121 blobs, 0 findings**. Synthetic redaction fixtures have file/value-specific allowances. Re-run staged and public branch history scans before pushes. App-owned unpublished checkpoint refs are not pushed or counted as public history.
- Verified source commit **`d71a072e44a1e2db0f0df9c3d36db16527a769d6`** was pushed normally to `origin/master` at `https://github.com/Sharath-holla/Aiventra.git`. `git ls-remote` confirmed that exact remote SHA. No force push was used; private configuration/database/artifacts remain ignored.
- [GitHub Actions run 37801518599](https://github.com/Sharath-holla/Aiventra/actions/runs/37801518599) completed with frontend/secret checks passing and backend/integration failing. Linux's pytest console entry point could not import `scripts.secret_scan`; the standalone web container inherited Docker's `HOSTNAME` and failed its loopback health check. PostgreSQL, migrations, API and worker became healthy. The pytest root path and explicit `HOSTNAME=0.0.0.0` fixes follow in a separate commit; a fresh CI run must verify them.
- After these fixes the actual pytest console entry point passed **64 tests, 0 failed, 1 dependency warning in 63.69 seconds**. The standalone production server was started with the corrected hostname on an isolated port; its loopback HTTP health returned **200**, and the server was stopped. This checks generated-server binding without claiming local Docker execution.
- [GitHub Actions run 37802879819](https://github.com/Sharath-holla/Aiventra/actions/runs/37802879819) completed **successfully in all four jobs** for `3ade79d8127ffc12482326cebe8918715c45aa4a`: Linux backend **64 passed in 33.56 seconds**, lint/audit passed; frontend typecheck/format/build/audit passed; secret scan passed; real Compose PostgreSQL/migrations/API/worker/web all became healthy, readiness returned 200, and browser **3 passed in 10.8 seconds**. No generated code ran in this stack.
- Follow-up monetary changes use PostgreSQL BIGINT for all 12 monetary columns and retain SQLite's already-wide INTEGER storage. Two regression tests cover large reservations and upgrade preservation; the targeted finance/migration group passed **9 tests in 11.60 seconds**.
- [GitHub Actions run 37804290311](https://github.com/Sharath-holla/Aiventra/actions/runs/37804290311) completed **successfully in all four jobs** for source commit `ca511457ee9c8ddb163d2ecdff6eb22ca2190bb0`. Linux backend **66 passed in 41.25 seconds**, lint and dependency audit passed; frontend format/typecheck/build/production audit and secret scan passed. Real Compose/PostgreSQL integration verified **all 12 BIGINT monetary columns**, a 5-billion-micro budget with competing 3-billion reservations accepting exactly one, eight concurrent persistent login increments, and database rejection of audit UPDATE/DELETE. Alembic reported no drift, readiness returned 200, and browser **3 passed in 10.1 seconds**. This is genuine database/container evidence; it does not include live AI calls or generated-code execution.
- The final source publication scan checked **254 staged/history blobs, 0 findings**. Ordinary push and `git ls-remote` confirmed `ca511457ee9c8ddb163d2ecdff6eb22ca2190bb0` on `origin/master`. The final documentation-only commit records these observed results and deliberately skips redundant CI; application code is identical to this successful source run.

The suite has one Starlette TestClient `httpx` deprecation warning. Alembic's configuration warning was removed using `path_separator=os`. Docker/Compose/PostgreSQL startup and browser integration are now verified in ephemeral GitHub CI; local Docker, the restricted coding runner, cluster, real provider billing, S3 and actual crypto verification remain pending.

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
- PostgreSQL/Compose startup and browser integration were tested in GitHub CI. Dedicated coding runner, S3 account storage, browser OIDC, OAuth connectors, staging deployment/rollback, production backup/restore, load and hostile multi-tenant behavior remain untested.
- Local record persistence across process restarts was observed. No full production backup restore drill or distributed failure certification was performed.
- Remote CI passed for the portability milestone as recorded above. The currently served Windows app uses the local development server; its Docker runtime remains unavailable.
- Screenshots and fixture records remain private under `artifacts/` and `data/`. An earlier diagnostic captured a previous local password; diagnostics were scrubbed, the password/signing key rotated and tests changed to avoid credential entry in the page.

Consult IMPLEMENTATION_STATUS.md before interpreting any feature as complete. Remaining work is in NEXT_STEPS.md.
