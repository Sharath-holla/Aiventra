import time
import uuid
from collections.abc import Generator

from sqlalchemy import create_engine, event
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from .config import settings


def uid() -> str:
    return str(uuid.uuid4())


def now() -> int:
    return int(time.time())


class Base(DeclarativeBase):
    pass


def make_engine(url: str):
    args = {"check_same_thread": False, "timeout": 30} if url.startswith("sqlite") else {}
    result = create_engine(url, connect_args=args, pool_pre_ping=True)
    if url.startswith("sqlite"):

        @event.listens_for(result, "connect")
        def configure(connection, _):
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.execute("PRAGMA journal_mode=WAL")
            cursor.close()

    return result


settings().artifact_root.mkdir(parents=True, exist_ok=True)
settings().repository_root.mkdir(parents=True, exist_ok=True)
engine = make_engine(settings().database_url)
SessionLocal = sessionmaker(engine, expire_on_commit=False)


def session_dependency() -> Generator[Session, None, None]:
    with SessionLocal() as session:
        yield session
