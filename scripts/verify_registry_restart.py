"""Actual API process restart check on the disposable browser SQLite fixture."""

import argparse
import base64
import hashlib
import json
import os
import site
import subprocess
import sys
import time
from pathlib import Path

import httpx
from dotenv import load_dotenv

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--exercise-throttle", action="store_true")
args = parser.parse_args()
load_dotenv(root / ".env")
db = max((root / "data/pytest-temp").glob("phase5-browser-*/fixture.db"), key=lambda p: p.stat().st_mtime)
assert db.resolve().is_relative_to((root / "data/pytest-temp").resolve())
env = {
    **os.environ,
    "DATABASE_URL": "sqlite:///" + db.as_posix(),
    "REQUIRED_DATABASE_BACKEND": "sqlite",
    "AI_SPENDING_MODE": "ZERO_COST_ONLY",
    "PROVIDER_SECRET_KEY": base64.urlsafe_b64encode(b"c" * 32).decode(),
    "JWT_SECRET": "phase5-browser-fixture-only-auth-secret-32chars",
    "OWNER_EMAIL": "phase5-owner@fixture.test",
    "OWNER_PASSWORD": "phase5-fixture-owner-password",
    "WEB_ORIGIN": "http://localhost:3001",
    "APP_ENV": "test",
    "OIDC_ISSUER": "",
    "ISOLATED_TEST_ENVIRONMENT": "true",
    "FIXTURE_CATALOG_ENABLED": "true",
    "EMBEDDING_PROVIDER": "deterministic_test",
    "ARTIFACT_ROOT": str(db.parent / "artifacts"),
    "REPOSITORY_ROOT": str(db.parent / "repositories"),
    "GITHUB_PUBLICATION_TOKEN_ENV": "BROWSER_DISABLED_GITHUB_TOKEN",
    "GITHUB_PUBLICATION_REPOSITORIES": "",
    "PYTHONPATH": os.pathsep.join([str(root / "apps/api"), *site.getsitepackages()]),
}
for key in list(env):
    if key.endswith("_API_KEY") or key in {"AIVENTRA_GITHUB_TOKEN", "GITHUB_TOKEN", "GH_TOKEN"}:
        env[key] = ""
snapshots = []
for iteration in range(2):
    with (root / "data/catalog-process-recovery.log").open("ab") as logs:
        process = subprocess.Popen(
            [
                sys._base_executable,
                "-m",
                "uvicorn",
                "company_os.api:app",
                "--host",
                "127.0.0.1",
                "--port",
                "8002",
            ],
            cwd=root,
            env=env,
            stdout=logs,
            stderr=logs,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
        try:
            with httpx.Client(base_url="http://127.0.0.1:8002", trust_env=False, timeout=15) as client:
                deadline = time.monotonic() + 40
                while True:
                    try:
                        if client.get("/health/live").status_code == 200:
                            break
                    except httpx.HTTPError:
                        pass
                    if time.monotonic() > deadline or process.poll() is not None:
                        raise RuntimeError("Disposable API startup failed; inspect private recovery log")
                    time.sleep(0.25)

                def login():
                    return client.post(
                        "/auth/login",
                        headers={"Origin": "http://localhost:3001"},
                        json={
                            "email": "phase5-owner@fixture.test",
                            "password": "phase5-fixture-owner-password",
                        },
                    )

                if args.exercise_throttle and iteration == 0:
                    for _attempt in range(12):
                        response = login()
                        if response.status_code == 429:
                            break
                        response.raise_for_status()
                    assert response.status_code == 429, "Persistent login throttle was not exercised"
                # Browser contracts can end inside the real persistent rate window.
                # Wait for it; never reset counters, weaken limits or accept 429 as success.
                deadline = time.monotonic() + 65
                while True:
                    response = login()
                    if response.status_code != 429:
                        break
                    if time.monotonic() >= deadline:
                        raise RuntimeError("Isolated owner login throttle did not clear within 65 seconds")
                    time.sleep(5)
                response.raise_for_status()
                client.headers["Authorization"] = "Bearer " + response.json()["access_token"]
                catalog = client.get("/model-catalog").json()
                state = client.get("/state").json()
                assert (
                    len([p for p in catalog["providers"] if p["name"].startswith("Catalog contract fixture")])
                    == 3
                )
                models = [m for m in catalog["models"] if m["identifier"].startswith("browser-contract-")]
                assert all(
                    p["configured"] and not p["credential_error"]
                    for p in catalog["providers"]
                    if p["name"].startswith("Catalog contract fixture")
                )
                assert len(models) == 3 and all(not m["eligibility"]["allowed"] for m in models)
                prefs = [
                    {"id": p["id"], "preferred_model_id": p["preferred_model_id"]}
                    for p in state["model_policies"]
                ]
                records = client.get("/project-drafts").json()
                tasks = [
                    client.get(f"/projects/{p['id']}/staffing").json()
                    for p in state["projects"]
                    if p["name"] == "Catalog task contract"
                ]
                assert len(tasks) == 1 and tasks[0]["content"]["tasks"][0]["preferred_model_id"] in {
                    m["id"] for m in models
                }
                task_preferences = [
                    {"content_hash": p["content_hash"], "content": p["content"], "tasks": p["tasks"]}
                    for p in tasks
                ]
                # The persisted API catalog and owner choices must survive a fresh server process.
                value = {"models": models, "preferences": prefs, "drafts": records, "tasks": task_preferences}
                snapshots.append(hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest())
        finally:
            process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)
assert snapshots[0] == snapshots[1]
print(
    json.dumps(
        {
            "verification": "actual API process restart, disposable SQLite, synthetic credentials only; no inference",
            "models": 3,
            "auth_throttle_exercised": args.exercise_throttle,
            "sha256": snapshots[0],
        },
        sort_keys=True,
    )
)
