# Aiventra verification report

## Phase 4 runner broker — verification in progress

Added a dedicated authenticated broker/DinD execution stack and closed snapshot protocol; no local Docker or host execution fallback. **28 affected local checks passed** in 20.34 seconds, covering protocol paths/limits/commands, disabled execution, secret/binary snapshots and existing repository/coding behavior. Ruff passed. An actual Docker isolation/build/test/cancellation/restart CI job is added and its results must be observed before claiming container verification. Bounded repair/PR preparation follow this broker increment.

## Workforce verification in progress — October 9, 2026

First staffing remote run 37951263042 passed backend/frontend/secrets and 11 browser checks. Its new twelfth login hit the real persistent 10-per-minute account throttle in fast CI. The browser check now waits within the existing throttle window and accepts only 200/429 while waiting; production limits and authorization assertions are unchanged. The complete remote restart comparison will be rerun.

Final local staffing verification: **145 backend tests passed**, zero failed, one existing dependency warning, 132.52 seconds; **12 real-service browser checks passed**, zero failed, 3.0 minutes. Ruff lint/format (86 files), Prettier, strict TypeScript and optimized production build passed. The actual managed API/worker/web processes were stopped and restarted; the byte-identical paused-workforce digest and readiness passed. Remote Compose/PostgreSQL restart checks are included in CI and remain to be observed for this source increment.

Memory source **4e57760**: [all four remote jobs passed](https://github.com/Sharath-holla/Aiventra/actions/runs/37948166635). Actual PostgreSQL pgvector/HNSW and local 384-dimensional paraphrase retrieval passed. The restart snapshots matched for two entries, three versions and three vectors, in addition to prior conversation recovery. The intermediate 8863d36 integration run also passed, with 11 browser checks in 51.4 seconds; its lean backend dependency regression was corrected in 4e57760.

Workforce additions include eight backend scenarios for exact/idempotent approval and saved artifacts, requirement-specific roles, cycles/caps/foreign scope/stale edits, pause/resume/uncertain usage, concurrent SQL claims/lease recovery, no-provider/no-charge waits, approved department reassignment/history and changed-approval fencing. The new actual-service browser flow passed in 26.7 seconds: saved v2, exact staffing approval, stored task artifacts, pause/reload/resume and mobile width. Full combined results and actual restart evidence will be recorded after completion.

Repaired during verification: populated SQLite rejected a new non-null capacity column without a default; a private backup was restored before the corrected additive upgrade, which passes Alembic check. Disabled-agent capacity lookup now leaves failure reporting to the existing worker handler. Admission prioritizes expired running leases. A memory test's seven-global-tick assumption was replaced with a bounded wait for its own proposal because multiple projects can now interleave; its original scope/ACL assertions remain intact. No live AI or local Docker execution is claimed.

## Phase 3 semantic memory — October 9, 2026

Starting source was clean 1670e83, preserving CI-tested 8263fbd. Re-ran all 129 original backend tests: passed in 72.05 seconds. Docker/Ollama remain absent locally. Installed locked pgvector and optional CPU-local embedding dependencies; explicitly downloaded BAAI/bge-small-en-v1.5 weights and observed real 384-dimensional inference without paid credentials. Baseline features were retained.

- Combined backend: **136 passed**, zero failed, one existing Starlette/httpx deprecation warning, final run 115.88 seconds. Seven new checks cover version history/stale edits/purge, scoped vector ranking/revocation/automatic context, source capture/restart sessions, provider-free fallback/no paid runs, production rejection of deterministic vectors, concurrent revisions and foreign scope rejection. Affected memory checks after hybrid retrieval also passed.
- Local SQLite backup taken before additive dc1275532cfb migration; upgrade/check passed with no metadata drift. Ruff and strict TypeScript passed. Dependency audit found no known vulnerabilities; local application package skipped.
- Browser: all ten existing journeys passed; the new memory save/revise/search/reload/mobile/purge journey passed in 21.1 seconds after repairing labels. Initial new-browser failures were exact accessible-label matching for selects and a populated textarea; explicit labels now remain stable across revisions. No assertions were removed. TypeScript/Prettier/production build and npm production audit passed; zero vulnerabilities. Final post-label TypeScript/Prettier/optimized build passed; publication scan checked 475 staged/history blobs with zero findings.
- Actual offline CPU-local paraphrase retrieval passed against two fixture documents using the real cached model (payment recovery ranked above gardening, cosine 0.71571). Actual PostgreSQL/pgvector/HNSW/local-model/restart evidence is recorded after CI execution below. Added CI checks are not claimed as passed merely because the script exists.

Repaired failures: missing ORM relationship ordering initially violated memory foreign keys; explicit relationships now order entry/version/chunk inserts. Memory context initially made an existing native-handoff prompt exceed its registered context limit; retrieval now has a compact remaining-context budget and the original handoff checks pass. Backfill scope initialization was misplaced and corrected. SQL bulk business-record updates now capture source revisions explicitly; the history test verifies both versions. A new test mistakenly created a duplicate workflow for an already scheduled task and now inspects the actual existing workflow.

Default cached local-model semantics and explicitly labeled deterministic vector tests are distinct. The hash test adapter is not live semantic-model evidence. No paid-model inference is claimed. Semantic memory is an implemented increment; staffing, complete Phase 3 orchestration and Phase 4 runner work remain next.

First memory CI source 165e772, run 37947164061: frontend/backend/secrets passed, with **136 backend tests** and **11 Compose/PostgreSQL browser tests** passing. Actual vector extension/HNSW and real local-model paraphrase retrieval passed. The restart digest then failed before restart because pgvector 0.5 returned a Python list while the helper assumed NumPy `.tolist()`. The helper now normalizes either representation and a new regression covers both. A successful restart is not claimed until the corrective CI run passes.

The corrective backend run exposed a test-only optional-dependency assumption: NumPy is installed with local embeddings, while the lean backend intentionally starts without that extra. The portable regression now uses the standard-library float array and list representations; production startup does not gain an unnecessary NumPy dependency.

## Native execution and microbenchmarks — October 9, 2026

Audited clean local/remote master 1d50728, with prior tested source c28582e. The latest continuation is preserved in docs/LIVE_EXECUTION_SPEC.md. Before editing, the existing 98 backend tests passed in 90.80 seconds. Docker/Ollama CLIs remain absent locally; no live provider account was verified.

| Check | Observed result |
|---|---|
| Backend regression | 129 tests passed in 142.04 seconds, zero failed, one Starlette/httpx deprecation warning; remote run is recorded below |
| New native/backend checks | 31 checks include six streaming and six complete-response protocols, native call/result round trips and Gemini signatures, incomplete/unknown usage and bounds, split-secret redaction, no-provider deduplication, actual controlled-adapter peer artifact, peer cancellation, in-flight cancellation/transport closure, rejected arguments/scope, eight-case benchmark completion/rejection/costs/profiles, profile invalidation, constrained recommendations and exact manual routing |
| Browser regression | Ten real-service checks passed in 2.4 minutes; new UI flow queues benchmark/tools, verifies reload/no-charge waiting, cancels and checks mobile sizing. Recommendation-control follow-up passed in 59.0 seconds; the final affected flow after delegated-cost aggregation passed again in 56.8 seconds. Remote evidence is recorded below |
| Web verification | TypeScript, Prettier and optimized production build passed; npm production audit: zero vulnerabilities |
| Python verification | Ruff lint passed, all 75 files formatted; pip-audit: no known vulnerabilities, local application package skipped |
| Publication secret scan | 427 staged/history blobs checked, zero findings; private configuration, database, logs and screenshots remain ignored |
| Migration | Private pre-migration SQLite backup; additive 4666ed0d2d17 applied; Alembic check: no drift. Existing 13 monetary columns retained |
| Persistence | Independent database sessions/checkpoints exercise native jobs, results, traces and artifacts. The actual Compose restart comparison passed with three conversations/turns, one uploaded document, four agent jobs and nine project artifacts; limits are recorded below |
| Remote verification | Source **8263fbde21b06b0b23408045f2a5219f60f109f4**, [Actions run 37929934962](https://github.com/Sharath-holla/Aiventra/actions/runs/37929934962): **all four jobs passed**. Linux backend: **129 passed**, one warning, 50.07 seconds. Compose/PostgreSQL browser suite: **ten passed**, 36.5 seconds. Remote secret scan: **461 blobs, zero findings** |

Repaired failures: two new tests initially expected a nested approval response instead of the existing direct project object. Final benchmark profile creation exposed a required-field autoflush defect and is fixed. Registering streaming was initially blocked by the model input enum and is now supported. The first expanded browser run passed nine and failed one on duplicate accessible labels between meeting and handoff checkboxes; peer controls now have distinct names and all ten passed afterward. Assertions were retained. Screenshots now capture the relevant tab/form after navigation settles rather than old provider/history rows.

The benchmark is explicitly micro-v1: small arithmetic/instruction/keyword/AST/calculator checks. Generated code is never executed on the host. Scores do not establish general architecture/coding ability, production correctness or invoice accuracy; costs use current registered rates and actual recorded usage. Controlled adapters are deterministic contract tests, not successful live inference. Live provider streams/tool calls/benchmark suites, dedicated coding containers, semantic memory, dynamic staffing, staging and complete delivery remain unverified or unfinished. Phase 2/Milestone A has advanced; Phases 3–5 are incomplete.

The successful integration job applied the additive migration to actual PostgreSQL, reported no drift, and verified all 13 BIGINT monetary columns, competing large reservations, concurrent persistent login counters/probe creation and audit UPDATE/DELETE rejection. API/worker/web containers were healthy before and after restart. The byte-identical digest covered three conversations/turns, one uploaded document, four jobs (one each message, meeting, benchmark and tools), nine project artifacts and scoped related evidence. It contained zero tool invocations and zero benchmark results: native browser jobs exercised honest missing-provider waiting, reload and cancellation. Completed native calls, peer artifacts and benchmark profiles are established by the controlled-adapter backend tests, not by live-provider or completed native-job Docker evidence. This recovery check is not a semantic-memory or complete requirements/task backup certification. The generated-code runner remained disabled.

Tested source was committed and pushed normally to origin/master; git ls-remote confirmed its exact SHA. A documentation-only follow-up records these results without changing the tested application source. Historical sections below remain unchanged in meaning.

## Milestone A workforce/provider core — October 9, 2026

Starting repository: clean master ae10711; existing application source 4de41f5. The new authoritative request is docs/PHASES_2_5_SPEC.md. Before editing, 81 backend tests (63.74 seconds), seven browser tests (2.1 minutes), TypeScript and formatting passed. Docker/Ollama were checked and remain unavailable locally.

| Check | Observed result |
|---|---|
| Full backend pytest | **98 passed, 0 failed**, one Starlette/httpx dependency deprecation warning, 86.40 seconds |
| New provider/agent contracts | 17 included checks: encrypted no-readback vault/rotation/transplantation, six catalog protocols/pagination, xAI inference/secret scrubbing, message persistence/idempotence/ack, independent two-round meeting/follow-up cap, provider waits/probes, scoped preferences/evaluations, foreign/disabled scope and budgets, credential rotation during catalog, concurrent duplicate jobs, in-flight cancellation/charged usage, affordability fallback and illegal state transitions |
| Full real-service browser suite | **Nine passed, 0 failed**, final rerun 1.8 minutes; explicit fixture workflows, real API/worker/storage, no mocked UI backend |
| Follow-up UI checks | Provider vault/catalog browser flow passed; the affected message/meeting desktop/mobile/history flow passed again after the wrapping repair and stable navigation capture (30.2 seconds) |
| Ruff | Lint passed; all 70 API/test/script/migration files formatted |
| Web checks | TypeScript, Prettier and optimized production builds passed |
| Migration | Existing SQLite backed up privately, additive b02442d39feb applied, populated data retained; alembic check reported no drift |
| Actual local agent-work restart | API/worker/web stopped and restarted; byte-identical digest for 12 completed jobs/workflows, 24 executions/runs, 96 transition events, six meetings, 36 messages and 30 project artifacts. Database content and private artifact files matched their SHA-256; readiness restored |
| Dependency checks | npm production audit: zero vulnerabilities. Python audit: no known vulnerabilities; the local application package is not on PyPI and is skipped |
| Populated dashboard | One actual state request measured 1.241 seconds with worker ready after redaction/SQL aggregation improvements; this is not a load certification |
| Publication secret scan | **360 staged/history blobs checked, 0 findings**; private configuration, database, logs and screenshots remain ignored |
| Remote verification | Source **c28582ee6aa3ac9ba936c149a428feeaf01a1d60**, [Actions run 37829944013](https://github.com/Sharath-holla/Aiventra/actions/runs/37829944013): **all four jobs passed**. Linux backend: **98 passed**, one warning, 44.15 seconds. Real Compose/PostgreSQL browser suite: **nine passed**, 32.3 seconds |

Failures repaired: initial new test fixtures had an expired detached ORM reference, an incorrect approval HTTP expectation and empty acceptance checks. An evaluation duplicate exposed an autoflush-before-error-handler defect; the transactional handler now returns a conflict. Event ordering needed a persisted per-execution sequence. Credential rotation and concurrent probe creation are fenced. The browser fixture initially used the wrong view URL and exact label matching without explicit select names. After those repairs, later status badges exposed a 20-pixel mobile summary overflow; summaries now wrap, bounded history expansion reduces accumulated page height, and meaningful screenshots wait for loaded state. Failed assertions were retained and repaired; no fake response substituted for the running backend.

Controlled adapters test provider contracts and usage accounting; they do not prove a real account or live model. Fixture meeting/message outputs are explicitly labeled. Native provider streaming/tools, semantic retrieval, approved dynamic staffing, actual dedicated coding runner execution, repair/PR/merge, staging and complete client delivery remain unfinished. The current phase is a verified **Milestone A core increment**, not completion of all Phases 2–5.

The successful integration job applied the migrations to real PostgreSQL, reported no schema drift, verified all 13 BIGINT monetary columns and competing large reservations, concurrent persistent login increments and single-row probe creation, and rejected audit UPDATE/DELETE. API/worker/web containers became healthy. Following the nine browser checks, actual container restarts preserved a byte-identical digest for three conversations/turns and one private uploaded document, with readiness restored. Compose execution keeps the coding runner disabled; it does not establish generated-code containment or live AI success.

The tested source was committed and pushed normally to origin/master; git ls-remote confirmed its exact SHA. A documentation-only follow-up records this evidence and the completed publication step without changing the tested application source. Private configuration, recovery snapshots, screenshots and CI logs remain ignored.

The sections below preserve historical milestones; their previous roadmap phase numbers and 'latest' labels refer to those historical source versions.

## Premium conversation foundation — October 8, 2026

The clean starting source was local/remote `b9e43cf`, preserving the previously CI-verified `ca51145`. Before editing, the current 66 backend tests and three browser tests were rerun successfully against actual code/services. The latest production specification is preserved in docs/PRODUCTION_UPGRADE_SPEC.md; its phase ordering now governs development.

| Check | Observed result |
|---|---|
| Full backend `pytest -q` | **81 passed, 0 failed**, 1 Starlette/httpx dependency warning, 58.72 seconds |
| New conversation checks | 15 checks: saved history/idempotence, concurrent duplicate dispatch, conflict/pending rejection, private uploads and scope, live no-provider/no-charge waiting, linked consultation, budget refusal, cancellation of delayed output, SSE revocation and missing JWT expiry |
| Actual browser/API/worker `npm run test:e2e` | **7 passed, 0 failed**, 1.6 minutes. Three existing acceptance tests retained plus four conversation tests |
| Browser conversation coverage | Explicit fixture upload/Markdown table/code/run evidence, saved URL/reload/search, real SSE snapshots, keyboard preview focus, persistent theme/sidebar, honest live waiting/cancel/reload, 390px mobile/1280px laptop sizing, chat → specialist proposal → exact approval → persistent project/four tasks |
| Frontend checks | Strict typecheck, Prettier and optimized Next.js production build passed; production npm audit **0 vulnerabilities** |
| Python checks | Ruff lint/format across **60 files** passed; locked dependencies valid; `pip-audit`: no known vulnerabilities in audited packages (local app package skipped) |
| Database | Populated local migration head **771bb4c719ce**; Alembic metadata check reports no drift; existing migration preservation tests pass in combined suite |
| Local restart | API/worker/web stopped and restarted; byte-identical conversation/message/workflow/document digest observed. Document DB hashes verified; subsequent recovery check also verifies private UTF-8 files |
| Visual review | Actual desktop 1440px, laptop 1280px, mobile 390px chat captures plus connected project/old dashboard reviewed; private screenshots remain ignored under artifacts/ |
| Publication secret scan | **288 blobs checked, 0 findings** before the source commit; private data/artifacts remain ignored |
| Remote verification | Source **`4de41f57c3d0c999a98a9f453ded8f368dc29443`**, [Actions run 37818487850](https://github.com/Sharath-holla/Aiventra/actions/runs/37818487850): **all four jobs passed**, 81 Linux backend checks in 42.07 seconds, **seven browser checks in 26.2 seconds**, real Compose/PostgreSQL migrations and 13 BIGINT monetary/cap/login/audit contracts |

Two browser failures found a missing accessible mode label and a saved-URL race behind a slower company-state refresh. The label and navigation sequence were repaired. Subsequent local startup/reload checks exceeded Playwright's default five-second expectation with accumulated real records, so asynchronous UI expectations now allow 15 seconds; the complete seven-test rerun passes. Expanded migration lint/format exposed generated legacy import/format issues; formatting-only repairs pass. No tests were removed, assertions replaced with fake responses, or live outcomes invented.

Fixtures/control adapters in backend and browser tests are explicit. No real AI provider inference or account billing was verified. SSE coverage establishes real saved-state updates, not provider-token streaming. The actual container restart comparison passed: three saved conversations/turns and one private uploaded document had identical digests before/after API/worker/web restart, with readiness restored. This is persistence evidence, not a production backup/restore drill. Full company pagination/load, dedicated coding-runner containment, semantic memory, client delivery, S3/OIDC/OAuth and staging/production remain unverified or incomplete.

Source was committed and pushed normally; `git ls-remote` confirmed its exact SHA. A documentation-only follow-up records final CI evidence without changing tested application code.

All sections below preserve historical verification milestones; their old phase labels/source SHAs are not the latest increment.

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
