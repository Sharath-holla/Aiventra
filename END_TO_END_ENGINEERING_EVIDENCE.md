# Controlled Task API engineering evidence

The automated journey in tests/test_phase6_engineering.py uses the existing persisted intake, BA/CTO/PM, staffing, engineering, QA and package services. It does not create another workflow engine. All model output is explicitly deterministic and all invocation receipts are FIXTURE_TESTED, including when Docker executes real tests.

The bounded sample implements create/list/update/complete/delete, input validation, SQLite persistence and parameterized SQL. Nine sample unit tests plus one baseline test are stored as .txt until the restricted snapshot is constructed. The sample is never imported or executed on the API/worker/test host. A deliberately invalid first patch fails build; one allowed repair replaces it. Exact workforce/task approval, independent reviewer/QA identity, saved diffs, a candidate commit and original repository preservation are asserted.

Workstation: the runner is a clearly labeled deterministic contract. Three execution results and one repair are checked, but that adapter cannot satisfy nonproduction engineering packaging. No local Docker execution or live AI is claimed.

CI: PHASE6_REAL_RUNNER is accepted only under CI and points to the authenticated broker on loopback. The same persisted workflow runs real compilation and unittest in the dedicated restricted Docker environment. Only after those tests pass may the explicit mock-only final review create an immutable fixture_nonproduction package. Package integrity, default publication rejection, live readiness rejection and unconditional fixture release refusal are asserted. Exact run/commit results are in TEST_REPORT.md after observation.

Real application: a separately saved NONPRODUCTION Task API requirement retains the unavailable GPT-6.1 Sol preference and automatic worker mode, with zero model runs and durable waiting across managed API/worker/web restart. The verified SQLite backup preserves all 49,640 pre-existing row identities. No model was installed, genuine AI invoked, external generated PR published, production package released or client delivery accepted.
