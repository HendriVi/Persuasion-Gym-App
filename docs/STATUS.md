# Persuasion Gym — verified Phase 0 status

Updated: 2026-10-11. Repository: `HendriVi/Persuasion-Gym-App` (public).

## Source and milestones

- **DESIGN_RECOVERED**: YES. Original canonical `PROJECT_SPEC.md`, `ARCHITECTURE.md`, `EVALUATION.md`, `REQUIREMENTS.md`, `DECISIONS.md`, `IMPLEMENTATION_PLAN.md`, `SOURCE_ARTIFACT_MANIFEST.*` and `reference/` sources have been imported on this pull-request branch.
- **PUBLIC_SOURCE_INTEGRITY**: VERIFIED LOCALLY. The exact 108 public-safe ZIP members were byte-matched to their originals in the offline package. The original SHA-256 controller reported `Inventory: 316 original files, public: 74, restricted/review: 242` and PASS. All 108 Git blob SHA-1 hashes also matched on the GitHub branch immediately after import.
- **PRIVATE_BENCHMARK_VAULT**: NOT CONFIGURED. The original restricted archive, private gold, holdouts and adjudication ledgers have not been committed, and must remain outside the public GitHub repository, app prompts and CI artifacts.
- **SOCIAL_IDENTITY_AND_BELONGING**: Public exploratory curriculum and specification merged, preserved without modification. Six synthetic exercises, including one matched identity-reversal pair. No qualified grading, learner persistence, or UI integration.
- **ENGINEERING_PLATFORM**: OPEN (see `docs/adr/ADR-0001-implementation-platform-OPEN.md`). No arbitrary provider/frontend/storage commitment.
- **EVALUATION_VAULT_AND_INDEPENDENCE**: OPEN (see `docs/adr/ADR-0002-evaluation-vault-OPEN.md`).
- **BUILD_IN_PROGRESS**: NO APPLICATION RUNTIME YET. This repository currently contains source reference and build-governance code, not a functional deployed analysis/training web app.
- **MODEL**: NOT_EVALUATED. **RELEASE**: BLOCKED. **MASTER_SKILL**: GATED.

## Phase checklist

- [x] Identify only the NEW repository as target; preserve existing social-identity feature.
- [x] Reconstruct public-safe bootstrap from the user-provided original package; byte-comparison with nested original and valid ZIP safety checks.
- [x] Import 108 public-safe source files into an isolated GitHub branch; compare all Git object SHA-1 hashes.
- [x] Retain all existing feature files and keep original canonical schema/registry unchanged.
- [x] Record open technology and evaluator-vault decisions instead of choosing silently.
- [x] Add source-to-requirement traceability and deterministic public checks.
- [ ] Obtain owner review and merge the Phase 0 pull request; run and confirm actual GitHub CI status.
- [ ] Approve engineering platform and access/retention approach before authenticated application implementation.
- [ ] Approve independent B/C adjudicator staffing and a restricted external evaluation vault.
- [ ] Deliver the first functional preliminary analysis/training path, with no scored mastery or qualified release claims.
- [ ] Complete independent adjudication, held-out benchmark and original five-run release gate.

## Evidence and limits

Passing checksum or public schema tests is **source integrity**, not proof of specialist accuracy. The original project documents and scientific release policy remain normative. Commit history contains no intentionally imported restricted archive. Changes after this document must use an explicit dated status update, not overwrite original source truth. See `docs/TRACEABILITY.md` and `evaluation/instructions/RELEASE_POLICY.md`.
