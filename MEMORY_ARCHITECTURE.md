# Memory architecture

Authoritative project, requirement, proposal, task, message, decision, run and artifact records live in the database. Workflows checkpoint their completed steps rather than replaying external calls. Artifact content/hash plus private file storage preserve evidence.

`company_os.memory.retrieve` performs bounded keyword retrieval over exactly scoped project knowledge/artifacts. `GET /memory/search` enforces project/client access before retrieval. Retrieved data remains untrusted and does not expand tool permissions. Agent document tasks reuse this scoped context.

Structured conversation summaries, organizational/agent retention, semantic pgvector search, provenance/deletion/expiry programs and richer shared knowledge remain pending. Database/process recovery tests are not a complete production memory/backup restore drill.
