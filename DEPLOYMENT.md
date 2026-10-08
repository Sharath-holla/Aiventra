# Deployment

Use the [Windows/Compose/backup guide](docs/operations.md). Generate private configuration first, stop any local processes occupying ports 3000/8000, then run `docker compose up --build -d --wait --wait-timeout 180`. Check `/health/ready` and the web page; preserve volumes during restart.

API liveness/database health and worker heartbeat health are distinct. The API has no runner socket; code execution stays disabled in Compose. Real Docker/PostgreSQL startup has not been verified on this machine. CI includes an ephemeral container/browser integration job; its outcome must be checked after publication.

Kubernetes manifests/cluster testing and production staging/rollback connectors remain pending Phase 10 work. Do not deploy this foundation publicly on the strength of local tests. HTTPS, secure cookies, verified identity configuration, secret storage, least-privilege DB roles, independent runner containment and restore evidence are prerequisites.
