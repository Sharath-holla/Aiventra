# Memory architecture

Current implemented memory is persisted conversation history, approved project records, private artifacts and project-scoped keyword retrieval. It is not semantic vector retrieval. Text is untrusted context; memory cannot authorize tools, change approval or expose other clients/projects.

The new message workflow reads scoped project memory and validates explicit artifact attachments. A meeting saves one project evidence snapshot for every independent first-round participant; a second round may inspect earlier contributions. Saved artifacts have content hashes and generated private storage keys. Conversation documents remain owner-only and cannot become message attachments for another project.

Milestone B must add real embedding adapters, scope-filtered vector indexing/retrieval, layered memory, provenance/versioning, stale-source invalidation, retention/deletion and recovery tests. Postgres/pgvector exists in Compose infrastructure, but no application semantic index is currently implemented. Controlled vectors may test contracts; they must never be reported as live embedding evidence.
