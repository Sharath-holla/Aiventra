# AI Company OS development

Read ARCHITECTURE.md, AUDIT_REPORT.md, IMPLEMENTATION_STATUS.md, TEST_REPORT.md and NEXT_STEPS.md before continuing. The authoritative upgrade target is docs/AIVENTRA_MASTER_SPEC.md; preserve the earlier docs/MASTER_BUILD_PROMPT.md too. Do not claim production readiness, live provider verification, Docker execution, cloud deployment or imported-crypto success without real evidence.

Keep API routers and domain modules separate. Preserve tenant/client scope, exact versioned approval, atomic finance reservations, independent QA, bounded retries and append-only audit. Never execute repository/generated code directly in the API or worker host; only the restricted runner is authorized. Never reset user repositories or disclose .env contents.

Use uv.lock and npm package-lock.json, strict TypeScript, Ruff and tests appropriate to changed behavior. Test temp files stay under data/pytest-temp. Update durable status and test evidence. Additional instructions for Next.js are under apps/web/AGENTS.md and its locally installed documentation.
