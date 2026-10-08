# Security

[Detailed threat model and controls](docs/security.md) remain authoritative. Local authentication now binds each JWT to an expiring database session. Logout revokes that session on the server; other sessions remain valid. The migration invalidates older sessionless tokens. Owner provisioning preserves existing credentials and public registration is deliberately absent.

Account/source login counters are atomic persistent hashes. The browser proxy's source is shared; trusted edge client-address integration and retention policies are pending. Never trust arbitrary forwarded-address headers for authorization or throttling.

Review policy is part of the exact approved coding scope. Strict diversity cannot be weakened by model output, and duplicate registry records do not count as independent services/models. Deterministic execution evidence is still mandatory. Docker isolation is unverified on this host and requires independent hardening.

Publication excludes private `.env`, database, artifacts, dependencies, runner worktrees and diagnostic logs. Run `scripts/secret_scan.py --history` after staging. It detects configured secret values and several token/key formats, but is not a full DLP/security audit. Report defects privately to the repository owner; never post credentials or client data in public issues.

Provider credentials are encrypted with AES-GCM and an independent base64-encoded 32-byte PROVIDER_SECRET_KEY. Tenant/provider/version are authenticated associated data. Keys are write-only through owner routes; serialized state excludes ciphertext and no credential value enters audit details. Provider errors are generic, known credentials are scrubbed from parsed responses, catalog bytes/pages/time are bounded and redirects are refused. Environment references remain optional fallbacks.

Bootstrap adds a missing vault key without replacing existing configuration. Keep that key private and preserve it with encrypted backups; do not derive it from JWT_SECRET. Master-key rotation and managed vault integration remain pending. HTTPS and secure cookies are required for remote credential entry.

Employee/provider/project model policies intersect and use optimistic versions. UUID request hashes, artifact/project boundaries, shared spend caps, bounded meeting/reply loops and lease-token cancellation protect durable agent work. A paid result cannot grant tools, coding scope, deployment or client acceptance. Tests exercise credential transplantation, rotation during checks, duplicate jobs, cancellation and actual recorded usage with controlled adapters; this is not live provider or production-security certification.
