# Backup and recovery status

Before the local zero-cost migration, the managed services were stopped and Python sqlite3 online backup created a private snapshot under `data/backups/`. SQLite `quick_check` passed. All row counts across 51 preexisting tables matched after additive migration to `a31d07edc482`; no records were reset. Keep backups outside Git with restricted access. This snapshot is not encrypted and is not an offsite backup service.

For restore, stop managed services, back up the current database first, restore to a separate candidate file, run integrity/migration checks and verify scoped business records before explicitly changing the configured path. Do not overwrite the active database during an unverified restore. Preserve the private vault key, artifacts and repository data in encrypted backups; never publish them.

Actual service restart comparisons exist for PostgreSQL/pgvector memory, conversations, staffing and runner results in GitHub Actions. `scripts/verify_zero_cost_recovery.py` adds digest comparison of saved zero-cost waits and verification records. These restart checks are not disaster-recovery restoration drills. Automated encrypted PostgreSQL backups, PITR, retention and offsite restore drills remain incomplete.
