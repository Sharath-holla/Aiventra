from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models as m
from .security import clean


def serialize(row, secrets=None):
    return clean(
        {
            column.name: getattr(row, column.name)
            for column in row.__table__.columns
            if column.name not in {"password_hash", "audit_head", "ciphertext"}
        },
        secrets,
    )


def tenant_rows(session: Session, model, user: m.User, limit=500):
    return session.scalars(
        select(model)
        .where(model.org_id == user.org_id)
        .order_by(model.created_at.desc(), model.id.desc())
        .limit(limit)
    ).all()
