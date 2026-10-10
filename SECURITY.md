# Security

## Frozen delivery evidence

Owner/tenant-only package routes recheck exact review/source provenance before preparation. The existing organization lock serializes versions and duplicate requests; worker checkpoints retain lease/cancellation fences. SQLite/PostgreSQL migration guards reject finalized manifest/input/identity edits and package deletion. Private hash-derived file paths reject traversal/linked directories; reads verify byte length and SHA-256 and downloads use no-store/nosniff attachments. No private file path or arbitrary binary enters a client response. Fixture classification cannot grant release authority. Release/client grants and tightening historical client artifact/memory access are the following increments, not completed controls in this source.

## Mandatory zero-cost inference boundary

ZERO_COST_AI_POLICY.md is authoritative for current inference eligibility. The sole accepted mode is ZERO_COST_ONLY. Neither credentials, owner model preferences, CEO instructions, claimed zero rates nor budget approval can authorize remote paid/unknown-cost inference. Raw structured/native transports also enforce the guard, and local embeddings reject cloud aliases. Catalog operations are distinct from inference and never prove zero billing.

Only trusted local Ollama with current installed-GGUF metadata may infer, with no provider token charges. This is not cryptographic host/daemon attestation. Malicious local proxies, compromised hosts and production egress containment require additional operational controls. The new table exposes only metadata digests/fingerprints, never credentials; endpoint/model changes invalidate evidence. Owner resume is tenant-scoped and cannot bypass execution approvals, review independence or uncertain-usage reconciliation. Publicly disclosed credentials must be revoked/replaced privately; none were stored or used here. Runtime redaction and publication scanning now recognize Groq-style and fine-grained GitHub token formats as well as existing formats.


[Detailed threat model and controls](docs/security.md) remain authoritative. Local authentication now binds each JWT to an expiring database session. Logout revokes that session on the server; other sessions remain valid. The migration invalidates older sessionless tokens. Owner provisioning preserves existing credentials and public registration is deliberately absent.

Account/source login counters are atomic persistent hashes. The browser proxy's source is shared; trusted edge client-address integration and retention policies are pending. Never trust arbitrary forwarded-address headers for authorization or throttling.

Review policy is part of the exact approved coding scope. Strict diversity cannot be weakened by model output, and duplicate registry records do not count as independent services/models. Deterministic execution evidence is still mandatory. Docker isolation is unverified on this host and requires independent hardening.

Publication excludes private `.env`, database, artifacts, dependencies, runner worktrees and diagnostic logs. Run `scripts/secret_scan.py --history` after staging. It detects configured secret values and several token/key formats, but is not a full DLP/security audit. Report defects privately to the repository owner; never post credentials or client data in public issues.

Provider credentials are encrypted with AES-GCM and an independent base64-encoded 32-byte PROVIDER_SECRET_KEY. Tenant/provider/version are authenticated associated data. Keys are write-only through owner routes; serialized state excludes ciphertext and no credential value enters audit details. Provider errors are generic, known credentials are scrubbed from parsed responses, catalog bytes/pages/time are bounded and redirects are refused. Environment references remain optional fallbacks.

Bootstrap adds a missing vault key without replacing existing configuration. Keep that key private and preserve it with encrypted backups; do not derive it from JWT_SECRET. Master-key rotation and managed vault integration remain pending. HTTPS and secure cookies are required for remote credential entry.

Employee/provider/project model policies intersect and use optimistic versions. UUID request hashes, artifact/project boundaries, shared spend caps, bounded meeting/reply loops and lease-token cancellation protect durable agent work. A paid result cannot grant tools, coding scope, deployment or client acceptance. Tests exercise credential transplantation, rotation during checks, duplicate jobs, cancellation and actual recorded usage with controlled adapters; this is not live provider or production-security certification.
