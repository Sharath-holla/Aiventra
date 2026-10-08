from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .observability import configure_logging, request_trace
from .routes import (
    administration,
    agent_operations,
    business,
    consultation,
    conversations,
    engineering,
    identity,
    provider_operations,
)


@asynccontextmanager
async def lifespan(_app):
    settings().validate_startup()
    yield


configure_logging()
app = FastAPI(title="Aiventra OS", version="0.2.0", lifespan=lifespan)
app.middleware("http")(request_trace)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings().web_origin],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PATCH"],
    allow_headers=["Authorization", "Content-Type", "X-Request-ID"],
    expose_headers=["X-Request-ID"],
)
for router in (
    identity.router,
    consultation.router,
    administration.router,
    engineering.router,
    business.router,
    conversations.router,
    provider_operations.router,
    agent_operations.router,
):
    app.include_router(router)
