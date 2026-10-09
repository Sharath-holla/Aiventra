# Deployment

## Current enterprise deployment restrictions

Compose migration/API/worker pin AI_SPENDING_MODE=ZERO_COST_ONLY. Apply additive migrations before starting the updated API. No remote inference is enabled by credentials alone. Host-loopback local inference does not make an Ollama service available inside Docker; an approved local inference service design is still needed. Existing Compose/runner CI checks remain required, including the new saved zero-cost restart snapshot. No local Docker execution, cloud rollout or production certification is claimed. BACKUP_RESTORE.md records current data preservation and remaining restore-drill work.


Use the [Windows/Compose/backup guide](docs/operations.md). Generate private configuration first, stop any local processes occupying ports 3000/8000, then run `docker compose up --build -d --wait --wait-timeout 180`. Check `/health/ready` and the web page; preserve volumes during restart.

API liveness/database health and worker heartbeat health are distinct. The API has no runner socket; code execution stays disabled in Compose. Real Docker/PostgreSQL startup, monetary/concurrency/audit contracts, schema drift and browser checks passed in ephemeral GitHub CI on `ca51145`. Docker remains unavailable on this Windows host. Inspect subsequent source runs for newer changes; this evidence does not certify production operations or the restricted coding runner.

Kubernetes manifests/cluster testing and production staging/rollback connectors remain pending production work. Do not deploy this foundation publicly on the strength of local tests. HTTPS, secure cookies, verified identity configuration, secret storage, least-privilege DB roles, independent runner containment and restore evidence are prerequisites.

For the Milestone A schema, stop managed processes, make a private SQLite backup, run scripts/configure.py (which preserves existing .env and adds a missing independent vault key), then company_os.cli init and alembic check. Restart API/worker/web and verify /health/ready. Migration b02442d39feb is additive. Preserve PROVIDER_SECRET_KEY across container restarts and database restores; a different key cannot decrypt saved credentials.

Live inference remains optional at startup. Configure a real provider/account model and documented prices/capabilities, test its catalog and explicitly request a capped inference probe before claiming live readiness. Do not include secrets in the Docker image, Git history, logs or public test artifacts. Later dedicated runner, staging and client-delivery verification are separate milestones.
