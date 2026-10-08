"""Verify a disposable migrated PostgreSQL stack; creates labeled test records."""

import argparse
from concurrent.futures import ThreadPoolExecutor

from company_os.authentication import count_attempt
from company_os.config import settings
from company_os.db import Base, SessionLocal, engine, uid
from company_os.finance import BudgetExceeded, reserve
from company_os.models import AuditEvent, Budget, Organization
from company_os.security import audit, verify_audit
from sqlalchemy import BigInteger, inspect, select, text
from sqlalchemy.exc import DBAPIError


def verify():
    if engine.dialect.name != "postgresql" or settings().app_env == "production":
        raise RuntimeError("Use a disposable non-production PostgreSQL stack")
    inspector = inspect(engine)
    checked = 0
    for table in Base.metadata.sorted_tables:
        stored = {column["name"]: column["type"] for column in inspector.get_columns(table.name)}
        for column in table.columns:
            if column.name.endswith("_micro") or column.name.endswith("_micro_per_million"):
                assert isinstance(stored[column.name], BigInteger), f"Narrow money column: {table.name}"
                checked += 1
    assert checked == 13

    marker = uid()
    with SessionLocal() as session:
        org = Organization(name="CI PostgreSQL verification " + marker)
        session.add(org)
        session.flush()
        budget = Budget(org_id=org.id, scope="ci-verification:" + marker, limit_micro=5_000_000_000)
        session.add(budget)
        session.commit()
        org_id, budget_id = org.id, budget.id

    def attempt(_):
        with SessionLocal() as session:
            try:
                reserve(session, [session.get(Budget, budget_id)], 3_000_000_000)
                session.commit()
                return True
            except BudgetExceeded:
                session.rollback()
                return False

    with ThreadPoolExecutor(max_workers=4) as pool:
        assert sorted(pool.map(attempt, range(4))) == [False, False, False, True]
    with SessionLocal() as session:
        budget = session.get(Budget, budget_id)
        assert (budget.limit_micro, budget.reserved_micro, budget.spent_micro) == (
            5_000_000_000,
            3_000_000_000,
            0,
        )

    def increment(_):
        with SessionLocal() as session:
            count = count_attempt(session, "ci-postgres-counter:" + marker)
            session.commit()
            return count

    with ThreadPoolExecutor(max_workers=4) as pool:
        assert sorted(pool.map(increment, range(8))) == list(range(1, 9))

    with SessionLocal() as session:
        audit(session, org_id, "ci-verifier", "verification.postgres", budget_id)
        session.commit()
        assert verify_audit(session, org_id)["valid"]
        event_id = session.scalar(select(AuditEvent.id).where(AuditEvent.org_id == org_id))
        for command in (
            "UPDATE audit_events SET action='tampered' WHERE id=:id",
            "DELETE FROM audit_events WHERE id=:id",
        ):
            try:
                with session.begin_nested():
                    session.execute(text(command), {"id": event_id})
            except DBAPIError as error:
                assert "audit append only" in str(error.orig)
            else:
                raise AssertionError("Database allowed audit mutation")
        assert verify_audit(session, org_id)["valid"]
    print(
        "PostgreSQL verified: 13 BIGINT money columns, large atomic caps, concurrent login counters, append-only audit"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--allow-test-records", action="store_true", required=True)
    parser.parse_args()
    verify()
