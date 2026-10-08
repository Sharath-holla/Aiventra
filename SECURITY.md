# Security

[Detailed threat model and controls](docs/security.md) remain authoritative. Local authentication now binds each JWT to an expiring database session. Logout revokes that session on the server; other sessions remain valid. The migration invalidates older sessionless tokens. Owner provisioning preserves existing credentials and public registration is deliberately absent.

Account/source login counters are atomic persistent hashes. The browser proxy's source is shared; trusted edge client-address integration and retention policies are pending. Never trust arbitrary forwarded-address headers for authorization or throttling.

Review policy is part of the exact approved coding scope. Strict diversity cannot be weakened by model output, and duplicate registry records do not count as independent services/models. Deterministic execution evidence is still mandatory. Docker isolation is unverified on this host and requires independent hardening.

Publication excludes private `.env`, database, artifacts, dependencies, runner worktrees and diagnostic logs. Run `scripts/secret_scan.py --history` after staging. It detects configured secret values and several token/key formats, but is not a full DLP/security audit. Report defects privately to the repository owner; never post credentials or client data in public issues.
