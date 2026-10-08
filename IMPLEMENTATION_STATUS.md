# Implementation status

Updated October 8, 2026. The current roadmap is [PRODUCTION_UPGRADE_SPEC.md](docs/PRODUCTION_UPGRADE_SPEC.md), supplied in the latest request. It supersedes the implementation order in the preserved [previous specification](docs/AIVENTRA_MASTER_SPEC.md) and [original brief](docs/MASTER_BUILD_PROMPT.md). Phase numbers below refer to the latest roadmap.

**Phase 2 — Premium UI Foundation: verified and published conversation milestone. Next implementation phase: Phase 3 — Real AI Runtime.** The wider UI redesign in Part 2 and Phase 9 remains incomplete. This application is not production-certified.

## Functionality added in this increment

- Dark default design tokens, optional persistent light theme, reusable surfaces/forms/status styling, collapsible desktop sidebar, mobile navigation, recent conversations, company search shortcut and default CEO workspace. Existing connected operational views are retained.
- Persisted, organization-scoped owner conversations and ordered turns, live mode by default, UUID request deduplication, optimistic concurrency, actual worker dispatch and fenced cancellation. Reload and server restarts preserve history; a cancellation cannot publish a delayed provider answer.
- Read-only CEO answers call the existing real model gateway with scoped project memory, prior turns and explicitly attached documents. Company/project/agent/model/period caps remain enforced; conversation and per-turn caps are added. Missing credentials/models persist a truthful provider wait without a fabricated answer, paid run or reservation.
- Server-sent events deliver actual persisted snapshots, with heartbeat/reconnect and polling recovery. They recheck identity, expiry and session revocation. This is **workflow-state streaming**, not token-by-token provider streaming; the latter remains a Phase 3 task.
- Actual private UTF-8 document uploads, integrity hashes and a keyboard-accessible preview. Supported types: `.txt`, `.md`, `.csv`, `.json`, maximum 16 KB, four documents per message and 20 per conversation. PDF/image/repository URL ingestion is not implemented here.
- Markdown responses with tables/code blocks, safe links, copy, explicit resubmission, real model/run/cost details, bounded recovery controls and visible loading/wait/error/cancel states. No fabricated active workforce or simulated word streaming.
- An explicit consultation action stages the existing seven-step specialist workflow atomically. Uploaded text feeds scoped consultation evidence. The conversation opens its exact requirement/proposal; existing version/hash approval opens the exact resulting project with four dependent planning tasks. This reuses working consultation/approval modules.
- Paginated conversation history (50 per page), search and durable URL links. Snapshots expose the latest 100 turns and their total count; navigation to earlier turns within a conversation is pending.
- Additive conversation migration `771bb4c719ce`, retaining populated SQLite data and audit protection; PostgreSQL conversation cap uses BIGINT (13 monetary columns total).
- CI now checks migration formatting and compares conversation/document digests across actual API/worker/web container restarts. Local restart comparison also checks private file integrity. All four remote CI jobs passed on `4de41f5`, including seven browser tests against real Compose/PostgreSQL and identical conversation/document digests after API/worker/web container restarts. Details are in TEST_REPORT.md.

Fixture answers remain **explicitly selected local fixtures**, show no live inference, and carry no fabricated billing. The consultation coordinator acknowledgement is a deterministic saved-workflow acknowledgement; specialist model work appears separately.

## Source and verification baseline

The clean local and remote starting commit was `b9e43cf` on `master`; source milestone `ca51145` previously passed all four CI jobs, 66 backend tests and three real Compose/PostgreSQL browser tests. This turn reran those 66 backend/three browser tests before editing. Earlier completed session/throttle/readiness/provider-wait/review-diversity/BIGINT repairs remain intact. Current source **`4de41f57c3d0c999a98a9f453ded8f368dc29443`** was pushed normally to `origin/master`; local/remote SHA matched. [All four CI jobs passed](https://github.com/Sharath-holla/Aiventra/actions/runs/37818487850): 81 Linux backend tests, seven real Compose/PostgreSQL browser tests, 13 BIGINT monetary columns, atomic finance/login/audit contracts and actual container restart persistence. Current evidence and repaired failures are in TEST_REPORT.md.

## Latest phase coverage

| Phase | Current implementation and limits |
|---|---|
| 1 — Audit and stabilization | Required documents, Git and actual source inspected; prior tests rerun; existing modules retained. Broader production security/operations are pending |
| 2 — Premium UI foundation | Design system, shell, primary CEO chat, navigation and real-state connections implemented in this milestone. Full-screen redesign belongs to Phase 9; provider token streaming remains pending |
| 3 — Real AI runtime | Five HTTP adapters, real bounded gateway/worker and configuration-aware waits exist. Connection tests/model discovery, capability probes and capped live inference are next; no live provider verified |
| 4 — Intelligent routing | Filtering, ordering, fallback and atomic usage/caps exist. Measured benchmarks, configurable scoring and invoice reconciliation pending |
| 5 — Persistent memory | Scoped keyword project memory, conversation history and text context persist. Semantic indexing, retention/version lifecycle and earlier-turn retrieval pending |
| 6 — Orchestration | Database leases/checkpoints, bounded specialist meetings, dependencies, watchdog and owner controls exist. General message delivery, dynamic delegation and Temporal/distributed operations pending |
| 7 — Consulting/workforce | Saved consulting, exact approvals and fixed assigned planning tasks work with fixtures. Dynamic approved staffing, live research quality and client portal incomplete |
| 8 — Coding/QA | Real Git discovery/worktrees/diffs and independent review policies exist. Dedicated runner/live coding, repair, security/PM acceptance and delivery remain unverified/incomplete |
| 9 — Full UI integration | Connected legacy operational views inherit the design tokens. Full workforce/organization/project/provider interaction redesign and accessibility audit pending |
| 10 — DevOps/security | Local and ephemeral remote Compose contracts exist. Browser OIDC, trusted proxy limits, hardened runner, restore/load drills, managed secrets and external monitoring pending |
| 11 — End-to-end delivery | No live coding/deployment/client acceptance completed. Actual owner crypto repository is still required |
| 12 — Publication | Ordinary authenticated pushes are authorized. This source milestone is published with passing CI; final product acceptance is not achieved |

## Operational boundaries

- SQLite remains a trusted local development database; PostgreSQL is used by remote integration CI. A passing disposable stack is not a production restore/load certificate.
- Existing 16 departments/136 seeded roles are registry entries. Agent availability, workflow status and recorded runs are shown as separate facts; registration does not mean agents are actively working.
- The CEO advisory route has no tool execution. Consultation and approved planning produce documented artifacts, not completed software. Generated/repository code must run only through the restricted runner.
- Provider configuration is not connectivity verification. Live prices/identifiers are owner-configured, token costs are estimates, and no real account billing has been checked.
- Public registration remains intentionally absent. Owner credentials are in private `.env`; invitation provisioning and full client project/proposal/delivery access remain pending.
- Most legacy snapshot collections are capped at 300. Conversation list pagination is implemented, but company-wide pagination/load performance and cross-tab updates are not certified.
- Deployment is rejected until an approved connector exists. OAuth mail/calendar, actual sending, S3 account verification, semantic memory, actual crypto tests and production backup/restore remain external or unfinished.

## Local handoff

Use `scripts/start.ps1` / `scripts/stop.ps1`; both preserve private data. The current default page is Executive chat; the previous bounded operations interface remains under Company commands. Select Local fixture explicitly for offline demonstrations; Live AI waits until an eligible real model is configured. Browser tests create clearly labeled persistent fixture conversations/projects. No user repository has been reset or modified by generated code.
