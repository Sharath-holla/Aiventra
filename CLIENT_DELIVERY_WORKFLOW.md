# Client-to-delivery workflow

## Current implemented workflow

Approved requirement/proposal → exact approved staffing → authorized task execution/restricted engineering/independent QA → five-role final review → immutable package validation/freeze → separate exact owner release approval → explicit release → intended invited client files/response → approved follow-up work or acceptance → separate owner closure approval/close. These are enforced backend gates with connected UI; no stage establishes live AI quality by itself.

Owner Project → Delivery now exposes package documents/disclosures, recipient grants, expiring invitations, exact approval/release/withdrawal, cases, analysis artifacts, scope approvals, follow-up tasks, timeline and closure/reopen. Clients redeem an invitation at login, then see only their granted projects and intended released versions. Withdrawn/unreleased/internal files cannot be downloaded. The portal shows real saved hashes, files, requirements, limitations, issues and deployment not_verified rather than a fabricated deployed preview.

Formal acceptance/rejection/changes bind exact version/hash and deadline with an explicit reason; duplicates are idempotent and decisions cannot rewrite history. Defects/support additionally save severity, priority, reproduction, feature/criteria references and bounded text attachments. BA/PM impact analysis is owner-started and budgeted. Exact owner impact approval precedes new document/coding work; coding retains separate repository authorization. Resolution checks actual task/result/QA evidence. A revision requires a fresh review/package/release; the original package never changes. Fixture analysis/work is visibly fixture_verified and still blocks live completion.

Closing checks the latest intact live release and acceptance, all work/cases, settled reservations/spending and audit validity, then requires a separate exact expiring owner approval. Explicit reopening keeps package/response/closure history. Notifications are internal persisted records; no email, external client message, generated PR, deployment or real release was sent during development. The following sections retain historical design/status statements.

## Increment A — frozen packages

Completed final review → owner selects exact reviewed source/documents → durable artifact-validation checkpoint → freeze checkpoint → package_ready or package_blocked. Each version has canonical manifest/file hashes, actual provenance, bounded private immutable files and a supersedes reference. Missing required documents persist as blockers. Fixture packages retain fixture_nonproduction and cannot certify client release. The owner Delivery workspace and authenticated downloads consume real saved state. Separate release approval/client access/acceptance/closure are the next increments; historical unimplemented statements below refer to earlier source.

## Current implemented transitions

Approved requirement/proposal → active project/foundation tasks → exact owner workforce approval → dependency-based execution → validated evidence → owner-requested final review. CTO → QA Director → Security Architect → Project Manager → CFO each save a checkpoint/artifact/model-run reference; four hash-bound inter-agent handoffs are acknowledged. Existing scoped memory, budgets, leases, agent authorization and ZERO_COST_ONLY remain authoritative.

Owner `GET /projects/{id}/delivery-readiness?mode=live|mock` returns actual blockers/source hash. `POST /projects/{id}/final-review` requires that current hash and an idempotent UUID. A second active chain is refused. Changed/expired approvals, documents/tasks/budget or invalid engineering evidence block further stages, including changes during inference. Complete source paragraphs are deduplicated losslessly within bounded context; oversize projects require partitioning. Project → Delivery exposes readiness/queue/results and existing workflow pause/resume/cancel controls. Cancellation preserves history and allows a fresh review after readiness is restored.

Findings end at `changes_required`; deterministic document fixtures end at `fixture_reviewed`, with `delivery_released=false` and `client_accepted=false`. Fixtures cannot certify coding execution. Live review requires live author evidence and independent restricted-runner QA/review; success would only reach `awaiting_delivery_approval`. Engineering fixtures do not establish live AI quality or completed delivery.

Still unimplemented: immutable delivery bundle, separate exact owner release approval, client-visible package and versioned acceptance/change/rejection, defects/support and authorized staging/deployment. Do not infer these from completed tasks/reviews. The older roadmap below is retained as historical context.

Implemented: persisted client requirements/clarifications/text evidence, specialist consultation, architecture alternatives, partial source-backed deterministic costs, version/hash proposal approval, actual project creation and dependent planning artifacts. CEO conversations link to their exact consultation, proposal and resulting project.

The new agent messages/meetings operate only in an approved active project and publish scoped artifacts/decisions. These outputs do not constitute completed client software delivery.

Milestone E must connect approved requirements-based staffing, real coding/repair/reviews/tests, CTO/QA final review, delivery artifact bundles, scoped client acceptance/change requests and follow-up defects. Invitation-only client accounts/portal and approved staging connectors remain incomplete. Missing deployment credentials or verified test evidence must remain visible blockers; do not fabricate delivered status, progress or preview URLs.
