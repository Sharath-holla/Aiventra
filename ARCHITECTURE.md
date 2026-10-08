# Aiventra OS architecture

The existing FastAPI/Next.js modular monolith is retained. [Detailed boundaries and diagrams](docs/architecture.md) describe the current implementation. The authoritative upgrade target is [AIVENTRA_MASTER_SPEC.md](docs/AIVENTRA_MASTER_SPEC.md); the earlier brief remains preserved separately.

The API owns authenticated, scoped business mutations. A separately scalable worker owns durable database workflows, model calls and restricted runner requests. SQLAlchemy/Alembic hold authoritative state; SQLite is verified locally and PostgreSQL is configured but unverified. Private files plus database content hold artifacts. Generated code never executes directly in the API or worker host.

The next implementation phase is **Phase 1: Production Foundation**. Existing later-phase modules are reused, without labeling the intervening phases complete. Work targets persistent authentication controls, health/readiness, correlated logs, truthful provider waiting, safe publication and stronger routing/review boundaries.

Temporal, semantic pgvector retrieval, general message dispatch, measured benchmarks, dynamic workforce planning, production deployments and client delivery remain incomplete. See IMPLEMENTATION_STATUS.md and AUDIT_REPORT.md.
