"""Disposable, network-denied Phase 5 browser contracts. NEVER use active app data.

This test entry point creates synthetic saved live-shaped provenance using test
helpers. It is not imported by the application or included in production routes.
"""

import argparse
import asyncio
import json
import logging
import os
import sys
import time
from pathlib import Path
from uuid import uuid4


async def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8001)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    os.chdir(root)
    private = root / "data" / "pytest-temp" / ("phase5-browser-" + str(uuid4()))
    private.mkdir(parents=True, exist_ok=False)
    os.environ.update(
        {
            "DATABASE_URL": "sqlite:///" + (private / "fixture.db").as_posix(),
            "REQUIRED_DATABASE_BACKEND": "sqlite",
            "AI_SPENDING_MODE": "ZERO_COST_ONLY",
            "JWT_SECRET": "phase5-browser-fixture-only-auth-secret-32chars",
            "OWNER_EMAIL": "phase5-owner@fixture.test",
            "OWNER_PASSWORD": "phase5-fixture-owner-password",
            "ARTIFACT_ROOT": str(private / "artifacts"),
            "REPOSITORY_ROOT": str(private / "repositories"),
            "MOCK_ENABLED": "true",
            "OIDC_ISSUER": "",
            "WEB_ORIGIN": "http://localhost:3001",
            "APP_ENV": "development",
        }
    )
    sys.path.insert(0, str(root / "tests"))
    sys.path.insert(0, str(root))
    import httpx
    import uvicorn
    from alembic import command
    from alembic.config import Config
    from company_os import models as m
    from company_os import repository_checkouts
    from company_os.api import app
    from company_os.config import settings
    from company_os.db import SessionLocal, engine
    from company_os.health import heartbeat
    from company_os.organization import seed
    from company_os.security import token_for
    from company_os.workflows import tick
    from fastapi.testclient import TestClient
    from sqlalchemy import select
    from test_client_delivery import release_fixture

    logging.getLogger("aiventra").setLevel(logging.WARNING)

    def no_network(*_args, **_kwargs):
        raise AssertionError("Phase 5 browser fixture attempted outbound inference/network access")

    async def no_async_network(*args, **kwargs):
        no_network(*args, **kwargs)

    httpx.HTTPTransport.handle_request = no_network
    httpx.AsyncHTTPTransport.handle_async_request = no_async_network
    command.upgrade(Config(str(root / "alembic.ini")), "head")
    with SessionLocal() as session:
        org = seed(session)
        owner = session.scalar(select(m.User).where(m.User.role == "owner"))
        client = session.scalar(select(m.Client))
        token = token_for(owner, session)
        session.commit()
        original_kinds = {row.id: row.kind for row in session.scalars(select(m.Provider))}
    company = {"factory": SessionLocal, "org": org, "owner": owner, "client": client, "root": private}
    saved = {"label": "DETERMINISTIC CONTRACT FIXTURE; NO LIVE AI OR REAL CLIENT DELIVERY", "packages": {}}
    with TestClient(app) as http:
        http.headers["Authorization"] = "Bearer " + token
        for name in ("acceptance", "changes", "defect", "fixture"):
            with SessionLocal() as session:
                for provider in session.scalars(select(m.Provider)):
                    provider.kind = original_kinds[provider.id]
                session.commit()
            requirement = http.post(
                "/requirements",
                json={
                    "client_id": client.id,
                    "title": "Phase 5 isolated " + name,
                    "text": "Controlled deterministic delivery contract. Analyze requirements, preserve evidence and verify access.",
                    "mode": "mock",
                    "budget_micro": 5000000,
                },
            ).json()
            project, package, _invitation, identity = await release_fixture(
                http, company, requirement, live_shape=name != "fixture"
            )
            saved["packages"][name] = {
                "project_id": project["id"],
                "id": package["id"],
                "version": package["version"],
                "manifest_hash": package["manifest_hash"],
                "client_email": identity["user"]["email"],
            }
        # Keep every synthetic historical author/review provider live-shaped,
        # with a distinct explicit mock adapter for newly queued fixture tasks.
        with SessionLocal() as session:
            for provider in session.scalars(select(m.Provider)):
                provider.kind = "ollama"
            provider = m.Provider(
                org_id=org.id,
                name="Explicit deterministic browser fixture",
                kind="mock",
                base_url="http://fixture.invalid",
            )
            session.add(provider)
            session.flush()
            session.add(
                m.ModelConfig(
                    org_id=org.id,
                    provider_id=provider.id,
                    identifier="deterministic-phase5-fixture",
                    capabilities=["structured", "reasoning", "coding", "tools"],
                    quality=95,
                    sensitivity="confidential",
                    price_source="Deterministic fixture only",
                )
            )
            session.commit()
        invitation = http.post(
            f"/projects/{saved['packages']['acceptance']['project_id']}/client-invitations",
            json={
                "request_id": str(uuid4()),
                "email": "new-browser-client@fixture.test",
                "can_respond": False,
            },
        ).json()
        saved["unredeemed_invitation"] = invitation["token"]
        # Private checkout UI contract. Neither GitHub nor Docker is contacted.
        with SessionLocal() as session:
            repository = m.Repository(
                org_id=org.id,
                project_id=saved["packages"]["acceptance"]["project_id"],
                name="Deterministic checkout UI fixture",
                path="remote-metadata-only",
                baseline_commit="a" * 40,
                report={
                    "remote_metadata_only": True,
                    "repository": "fixture/checkout-ui",
                    "branch": "main",
                    "verification": "DETERMINISTIC FIXTURE; NO GITHUB OR DOCKER",
                },
            )
            session.add(repository)
            session.commit()
            saved["checkout_repository"] = repository.id
        settings().execution_enabled = True
        receipts = {}
        execution_receipts = {}

        async def fixture_broker(method, path, data=None, params=None, timeout=200):
            if path == "/checkouts":
                value = {
                    **data,
                    "status": "ready",
                    "source_digest": "d" * 64,
                    "expires_at": int(time.time()) + 3600,
                    "file_count": 1,
                    "bytes": 80,
                    "notice": "DETERMINISTIC UI FIXTURE; NO GITHUB OR DOCKER EXECUTION",
                }
                receipts[data["job_id"]] = value
                return value
            identity = path.split("/")[2]
            if method == "GET":
                return receipts[identity]
            if path.endswith("/cleanup"):
                receipts[identity] = {**receipts[identity], "status": "cleaned"}
                return receipts[identity]
            if path.endswith("/execute"):
                value = {
                    "job_id": data["job_id"],
                    "status": "completed",
                    "exit_code": 0,
                    "build": {"exit_code": 0},
                    "logs": "DETERMINISTIC RUNNER ADAPTER; NO GITHUB OR DOCKER EXECUTION",
                }
                execution_receipts[data["job_id"]] = value
                return value
            raise AssertionError("Unexpected fixture broker request")

        repository_checkouts.broker = fixture_broker

        async def fixture_result(identity):
            return execution_receipts[identity]

        from company_os import sandbox

        sandbox.stored_result = fixture_result
    (root / "data" / "phase5-browser-state.json").write_text(json.dumps(saved), encoding="utf-8")

    worker_id = str(uuid4())

    async def worker():
        while True:
            with SessionLocal() as session:
                heartbeat(session, worker_id)
            await tick(SessionLocal)
            await asyncio.sleep(0.25)

    server = uvicorn.Server(uvicorn.Config(app, host="127.0.0.1", port=args.port, log_level="warning"))
    work = asyncio.create_task(worker())
    try:
        await server.serve()
    finally:
        work.cancel()
        engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
