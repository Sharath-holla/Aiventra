"""Read-only digest for comparing actual conversation state across service restarts.

Run before/after restart against the same database; compare JSON byte-for-byte.
Only record counts and digests are emitted, never conversation content or credentials.
"""

import hashlib
import json

from company_os.config import settings
from company_os.db import SessionLocal
from company_os.models import Artifact, Conversation, ConversationTurn, Workflow
from sqlalchemy import select


def snapshot():
    with SessionLocal() as session:
        conversations = list(session.scalars(select(Conversation).order_by(Conversation.id)))
        assert conversations, "Run conversation integration checks first"
        ids = [row.id for row in conversations]
        turns = list(
            session.scalars(
                select(ConversationTurn)
                .where(ConversationTurn.conversation_id.in_(ids))
                .order_by(ConversationTurn.id)
            )
        )
        turn_ids = [row.id for row in turns]
        workflows = list(
            session.scalars(
                select(Workflow).where(Workflow.conversation_turn_id.in_(turn_ids)).order_by(Workflow.id)
            )
        )
        assert any(row.status == "completed" for row in workflows), "No completed conversation"
        assert any(row.status == "cancelled" for row in workflows), "No persisted cancellation"
        assert all(row.status in {"completed", "cancelled"} for row in workflows), "Wait for active turns"
        attachments = list(
            session.scalars(select(Artifact).where(Artifact.conversation_id.in_(ids)).order_by(Artifact.id))
        )
        assert attachments, "No uploaded document"
        for row in attachments:
            assert hashlib.sha256(row.content.encode()).hexdigest() == row.sha256, "Document integrity failed"
            stored = (settings().artifact_root / row.storage_key).read_text(encoding="utf-8")
            assert hashlib.sha256(stored.encode()).hexdigest() == row.sha256, "Private file integrity failed"
        rows = [*conversations, *turns, *workflows, *attachments]
        payload = [
            {
                "table": row.__tablename__,
                **{column.name: getattr(row, column.name) for column in row.__table__.columns},
            }
            for row in rows
        ]
        return {
            "conversations": len(conversations),
            "turns": len(turns),
            "documents": len(attachments),
            "sha256": hashlib.sha256(
                json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
            ).hexdigest(),
        }


if __name__ == "__main__":
    print(json.dumps(snapshot(), sort_keys=True))
