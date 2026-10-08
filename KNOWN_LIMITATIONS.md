# Known limitations

The current phase is Production Foundation; the full master specification is incomplete. [Implementation status](IMPLEMENTATION_STATUS.md), [audit](AUDIT_REPORT.md) and [next steps](NEXT_STEPS.md) distinguish actual code from verification gaps.

- PostgreSQL/Compose startup and browser integration passed in ephemeral remote CI. Local Docker, live providers, object storage, browser OIDC, dedicated coding sandbox, staging/rollback, cluster deployment and actual crypto repository behavior remain unverified.
- Monetary fields use PostgreSQL BIGINT and SQLite's native 64-bit INTEGER. Large-balance preservation and PostgreSQL concurrent cap/login/audit contracts passed on `ca51145`; production load, distributed failures and restore behavior remain unverified.
- Worker readiness means a recently alive process, not a certified healthy model/runner. Provider readiness means configuration exists, not successful API access.
- No semantic pgvector indexing, general durable message bus, measured model benchmarks, full retention/erasure controls or distributed orchestration certification.
- Fixed planning tasks and specialist artifacts do not implement dynamic workforce allocation or final client delivery. Document completion verifies saved structure/integrity, not semantic accuracy.
- Coding supports Python/Node built-in tests. Dependency installation, autonomous repairs, coverage, security/PM acceptance, commits/PR merging and deployments remain future work. Strict two-review diversity can require three distinct services/models (author plus reviewers); the system waits if configuration cannot satisfy it.
- OIDC upstream token/session logout remains the identity provider's responsibility; browser OIDC is absent. Client invitation/account management and review/delivery portals remain incomplete. No public registration is intended.
- Source throttling is currently shared behind the Next.js proxy; session/throttle/heartbeat retention and trusted edge client-source handling remain operational work.
- UI is an incremental light workspace, not the requested Phase 8 dark conversation design. Snapshot collections remain capped at 300.

No production readiness, verified live AI collaboration, successful container QA, deployment or trading action is claimed.
