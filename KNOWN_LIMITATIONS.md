# Known limitations

The current phase is Production Foundation; the full master specification is incomplete. [Implementation status](IMPLEMENTATION_STATUS.md), [audit](AUDIT_REPORT.md) and [next steps](NEXT_STEPS.md) distinguish actual code from verification gaps.

- Docker/PostgreSQL/Compose, live providers, object storage, browser OIDC, dedicated sandbox, staging/rollback, cluster deployment and actual crypto repository behavior are unverified here.
- Existing SQL Integer monetary fields need PostgreSQL range review/migration before large production values. SQLite success does not prove Postgres concurrency/type safety.
- Worker readiness means a recently alive process, not a certified healthy model/runner. Provider readiness means configuration exists, not successful API access.
- No semantic pgvector indexing, general durable message bus, measured model benchmarks, full retention/erasure controls or distributed orchestration certification.
- Fixed planning tasks and specialist artifacts do not implement dynamic workforce allocation or final client delivery. Document completion verifies saved structure/integrity, not semantic accuracy.
- Coding supports Python/Node built-in tests. Dependency installation, autonomous repairs, coverage, security/PM acceptance, commits/PR merging and deployments remain future work. Strict two-review diversity can require three distinct services/models (author plus reviewers); the system waits if configuration cannot satisfy it.
- OIDC upstream token/session logout remains the identity provider's responsibility; browser OIDC is absent. Client invitation/account management and review/delivery portals remain incomplete. No public registration is intended.
- Source throttling is currently shared behind the Next.js proxy; session/throttle/heartbeat retention and trusted edge client-source handling remain operational work.
- UI is an incremental light workspace, not the requested Phase 8 dark conversation design. Snapshot collections remain capped at 300.

No production readiness, verified live AI collaboration, successful container QA, deployment or trading action is claimed.
