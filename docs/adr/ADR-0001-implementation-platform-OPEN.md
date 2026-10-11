# ADR-0001 — application platform, OPEN

Date: 2026-10-11. Status: **OPEN — owner approval required**.

## Decision context

Source: `DECISIONS.md` D-028–D-031 and D-036; `ARCHITECTURE.md`; `REQUIREMENTS.md` F-01–F-18, S-01–S-12, U-01–U-08. No frontend, inference provider, storage, hosting, authentication or pricing decision is binding. The old beta is explicitly not authoritative.

## Essential constraints

- Preserve the canonical JSON schema as source of truth, exact-text anchors, specialist field ownership and uncertainty/status separation.
- No LLM API credentials, factual retrieval keys, private answer keys, or hidden holdouts in a browser/public repository.
- Users commit their unaided attempt/confidence before seeing feedback; provisional items cannot alter mastery.
- Security: minimal retention, bounded artifact ingestion, prompt-injection controls, authentication and role boundaries before real user history is stored.
- Small, testable vertical slices; avoid speculative orchestration frameworks and unreviewed dependencies.

## Options for owner review

| Option | Advantages | Tradeoffs |
|---|---|---|
| Server-rendered Python backend + minimal progressive HTML frontend | Straightforward reuse of original Python evaluation utilities; small dependency surface; accessible deterministic tests | Rich training interactivity may require additional client code; operating hosted web and API together still needs architecture |
| TypeScript frontend + small server-side API, original Python evaluator isolated | Strong interactive UI ecosystem and typed client; separation from trusted evaluation zone | More cross-language adapters, security and versioning work; higher initial complexity |
| Single Python web application with lightweight component layer | Fewer services for prototype, quick local forms and evidence tables | UI flexibility, accessibility and scaling need evaluation before irreversible choice |

**Reversible engineering recommendation (not adopted):** run a minimal local, nonproduction prototype using generated validators from the original schema, stub/mock inference, and no persistent sensitive user data. Treat provider, auth and hosting as separate ADRs. Do not install framework dependencies or commit production scaffolding before owner chooses among alternatives.

## Approval questions and future tests

Approve (1) first local implementation stack, (2) language target and deployment assumptions, (3) whether accounts/persistence are deferred until security/retention design. On selection, version the ADR; test schema contracts, freeze-before-feedback, candidate-only mechanism claims, role boundaries, local build and secret absence. Never infer consent from a drafted ADR.
