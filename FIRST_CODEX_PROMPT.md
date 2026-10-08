# First Codex prompt — paste exactly once Codex is connected to HendriVi/Persuasion-Gym-App

> **Precondition:** Codex is pointed to `https://github.com/HendriVi/Persuasion-Gym-App`, NOT `HendriVi/persuasion-gym`, and the safe `Persuasion-Gym-Codex-Public-Bootstrap.zip` has been uploaded to the ROOT of that repository (it may still be compressed). This small bootstrap ZIP contains **no restricted original answer-key vault**. The separate comprehensive offline package must NEVER be uploaded to this public repo.

```text
You are the implementation engineer for the NEW Persuasion Gym app repository:
https://github.com/HendriVi/Persuasion-Gym-App

IMPORTANT: This repository—not HendriVi/persuasion-gym—is the application to build. Do not clone, rely on, import from, or modify the older repo. Do not use generic persuasion app templates.

Your task is PHASE 0 ONLY: first import and audit the safe source-of-truth documentation package, then prepare the first safe, dependency-ordered engineering milestone. Do NOT create UI/application code, enable an unvalidated master skill, select a model/provider without an approved decision, claim an AI benchmark passed, or upload hidden benchmark gold/holdouts.

FIRST, confirm the uploaded file `Persuasion-Gym-Codex-Public-Bootstrap.zip` exists. Inspect its contents for path traversal and for any forbidden paths (`offline-restricted`, `private`, `gold_constraints`, `holdout_gold_candidate`, `adjudication ledger`, `.env`, `vault`). The ZIP should contain a single `repo-root/` directory and its SAFE docs/reference/evaluation-code children; it must contain no hidden gold. Only if the archive is clean, extract `repo-root/` into the actual repository root, overwriting the starter README with its canonical version. Do not commit the compressed ZIP itself after import; remove it from the working tree in the same commit if safe to do so. Do not extract a source archive that includes private benchmark material. If the ZIP is absent, STOP and ask for the safe bootstrap upload, do not reconstruct requirements from your own memory.

THEN READ THESE ROOT FILES IN THIS ORDER, FULLY:
1. AGENTS.md and CODEX.md
2. PROJECT_SPEC.md
3. SOURCE_ARTIFACT_MANIFEST.md and SOURCE_ARTIFACT_MANIFEST.json
4. COMPLETENESS_AUDIT.md
5. DECISIONS.md
6. ARCHITECTURE.md
7. EVALUATION.md
8. REQUIREMENTS.md
9. IMPLEMENTATION_PLAN.md and REPO_TREE.md
10. evaluation/SKILL.md, evaluation/config/release.json, evaluation/instructions/RELEASE_POLICY.md, evaluation/instructions/DATA_GOVERNANCE.md
11. Relevant original normative reference files in reference/, especially original ontology, full common schema, rhetoric taxonomy, mechanism registry, manipulation boundary, uncertainty and learner model.

Verify the exact original source hashes and count/identify the safe public files that are present. Explain any unavailable source referenced by a document rather than inventing it. Verify the target GitHub repository visibility and confirm no privileged test answers, provisional gold labels, hidden manifests, annotated holdout, model secrets or other private material are tracked. Do not access, extract or transmit the offline vault ZIP; it was deliberately not committed.

Produce the following deliverables in a small, reviewable documentation-only branch/PR **after safe bootstrap extraction**:
(A) docs/STATUS.md with precise verified state and milestone checklist.
(B) docs/adr/ADR-0001-implementation-platform-OPEN.md: compare minimal viable frontend/backend options WITHOUT choosing by assumption; recommend only a reversible baseline and explicitly identify approval required.
(C) docs/adr/ADR-0002-evaluation-vault-OPEN.md: propose secure storage, independent annotator B and adjudicator C roles, forbidden public paths and gate access. Do not create fake locked gold or use the app repository as the vault.
(D) docs/TRACEABILITY.md linking each canonical capability and release gate to original reference sources and planned future tests, including statuses NOT_IMPLEMENTED/NOT_EVALUATED.
(E) A source-integrity script/test for the public files only that does not require or expose restricted benchmark materials. Keep the ORIGINAL strict evaluator unmodified.

Acceptance criteria:
- Source manifest and original canonical schema preserved; no replaced statuses or invented requirements.
- All 8 competencies, six challenge slices, six high-risk cross-slices, five frozen runs, >=.95 adjusted Wilson lower-bound gate, >=.97 stretch, future .98/.99, zero observed critical errors, ECE<=.05, lock/adjudication/holdout controls remain documented exactly.
- No actual model evaluation is claimed. RELEASE=BLOCKED, MODEL=NOT_EVALUATED, MASTER_SKILL=GATED.
- Do not copy existing code from the older repo or start speculative application scaffolding.
- No privileged benchmark materials or API keys in commits, workflows, logs, or prompts.
- Tests run against actually available files and are reported truthfully. If repo/permissions prevent writes, stop and explain one nontechnical action required.

Finally report ONLY:
1. Files changed + branch/PR link.
2. Source integrity/check results and scientific gate state.
3. Missing/blocked source artifacts and open decisions.
4. ONE highest-priority next step in nontechnical terms that I, the owner, can approve.
```

## Why first task stops there

This is intentionally not a prompt to build a guesswork application. The new repo started empty; the complete original intellectual property, canonical schemas, scientific proof burdens and release gates must be in place before choosing the runtime, rewriting any stage or emitting an authority-sounding analyst. Later prompts advance one phase after owner review and verified tests.
