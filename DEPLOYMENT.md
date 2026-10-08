# Deployment

Use the [Windows/Compose/backup guide](docs/operations.md). Generate private configuration first, stop any local processes occupying ports 3000/8000, then run `docker compose up --build -d --wait --wait-timeout 180`. Check `/health/ready` and the web page; preserve volumes during restart.

API liveness/database health and worker heartbeat health are distinct. The API has no runner socket; code execution stays disabled in Compose. Real Docker/PostgreSQL startup is verified in ephemeral GitHub CI, with all service health and browser checks passing on `3ade79d`. Docker remains unavailable on this Windows host. Inspect subsequent runs for newer commits; this evidence does not certify production operations or the restricted coding runner.

Kubernetes manifests/cluster testing and production staging/rollback connectors remain pending Phase 10 work. Do not deploy this foundation publicly on the strength of local tests. HTTPS, secure cookies, verified identity configuration, secret storage, least-privilege DB roles, independent runner containment and restore evidence are prerequisites.
