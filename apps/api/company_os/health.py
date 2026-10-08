"""Runtime health facts; liveness does not imply worker or provider readiness."""

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .config import settings
from .db import now
from .models import WorkerHeartbeat


def workers(session: Session) -> dict:
    latest = session.scalar(
        select(func.max(WorkerHeartbeat.last_seen)).where(WorkerHeartbeat.status == "running")
    )
    return {
        "status": "ready" if latest and now() - latest <= settings().worker_stale_seconds else "unavailable",
        "last_seen": latest,
        "stale_after_seconds": settings().worker_stale_seconds,
    }


def heartbeat(session: Session, worker_id: str, status="running"):
    record = session.get(WorkerHeartbeat, worker_id)
    if record is None:
        record = WorkerHeartbeat(id=worker_id, last_seen=now(), status=status)
        session.add(record)
    else:
        record.last_seen, record.status = now(), status
    session.commit()
