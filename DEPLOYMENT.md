# Deployment

Use the [Windows/Compose/backup guide](docs/operations.md). Generate private configuration first, stop any local processes occupying ports 3000/8000, then run `docker compose up --build -d --wait --wait-timeout 180`. Check `/health/ready` and the web page; preserve volumes during restart.

API liveness/database health and worker heartbeat health are distinct. The API has no runner socket; code execution stays disabled in Compose. Real Docker/PostgreSQL startup, monetary/concurrency/audit contracts, schema drift and browser checks passed in ephemeral GitHub CI on `ca51145`. Docker remains unavailable on this Windows host. Inspect subsequent source runs for newer changes; this evidence does not certify production operations or the restricted coding runner.

Kubernetes manifests/cluster testing and production staging/rollback connectors remain pending Phase 10 work. Do not deploy this foundation publicly on the strength of local tests. HTTPS, secure cookies, verified identity configuration, secret storage, least-privilege DB roles, independent runner containment and restore evidence are prerequisites.
