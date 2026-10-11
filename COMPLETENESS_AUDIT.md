# Completeness audit — Persuasion Gym conversation → Codex implementation

**Audit basis:** supplied conversation and actual files currently available in the working container on 2026-10-08, with SHA256 source mapping. A statement was not silently filled using external assumptions. The full 316-member benchmark-system ZIP is preserved **byte for byte** in the downloadable package's `offline-restricted/` directory. Other separately created first-party source ZIPs and standalone skills are preserved in `reference/`. The target repo was **PUBLIC and EMPTY** on initial audit (GitHub API); a short safe `README.md` was subsequently added as the first documentation-only commit, so privileged materials are intentionally not committed there.

## A. Scope coverage — all recovered and represented

| Item required by user | Covered in | Status |
|---|---|---|
| Project purpose, scientific architecture, product behavior | `PROJECT_SPEC.md`, original ontology | RECOVERED |
| Master persuasion system/master skill | architectural role in `PROJECT_SPEC.md`, `CODEX.md`, `IMPLEMENTATION_PLAN.md` | **GATED / NO QUALIFIED MASTER FILE EXISTS** |
| Rhetoric | canonical taxonomy, rhetorical structure `SKILL.md`; 80 adversarial cases | RECOVERED |
| Argument structure, logical validity, critical thinking | standalone `Critical Thinking .md`, logic constraints, MAFALDA/FOLIO mapping | RECOVERED |
| De-Spin/factual verification | standalone `DeSpin.md`, Fact-Check skill, claim contract, SciFact/AVeriTeC/FActScore | RECOVERED |
| Psychological mechanism candidate reasoning | mechanism registry and skill, activation ceiling, PP distinction | RECOVERED |
| Intent inference discipline | original 64-case suite, 5 exact statuses, separate motive test | RECOVERED |
| Causal discipline | original 80-case suite, causal-proof burden, CLadder/Corr2Cause | RECOVERED |
| Level separation | original 80-case suite, separate layer verdicts, contamination metrics | RECOVERED |
| Manipulation boundary and risk dimensions | boundary original and risk statuses | RECOVERED |
| Systems thinking and influence graph reasoning | skills, ontology L7, causal loop evidence requirements | RECOVERED |
| Adversarial 80-case suite/political mirrors | benchmark archive and specs | RECOVERED |
| 96 base contrastive corpus + first pass, 32/16/48 splits | benchmark archive and ZIP mapping | RECOVERED; **NOT GOLD** |
| 400 internal cases (96+80+64+80+80) | source archive, `CANDIDATE_CASE_INDEX.jsonl` | RECOVERED; **NOT GOLD** |
| Blinded A/B annotation, C adjudication + reliability | bundled annotation infrastructure and 5 specialist skills | RECOVERED; **NOT EXECUTED** |
| User skill model, error codes, calibration, transfer and delayed verification | separate original 34KB ZIP and project spec/requirements | RECOVERED; **APP NOT WIRED** |
| Agentic Learning, Fact-Check, rhetoric/mechanism/systems/training skills | original `skills/*` and separate first-party ZIPs | RECOVERED |
| Common schema, ontology, taxonomy, uncertainty and policies | original full canonical files, public-safe reference export | RECOVERED |
| External registry + nine benchmark recommendations | original registry copied intact; EVALUATION / DECISIONS | RECOVERED **metadata only** |
| Promptfoo, Inspect AI, Argilla, Cleanlab, FActScore, Langfuse, DVC, Pandera, irrCAC | DECISIONS, technical roles, source references | RECOVERED as recommendations, NOT automatically installed |
| DSPy, PaperQA, STORM, GPT Researcher, Loopy, PySD, SDEverywhere | DECISIONS / source inventory | CANDIDATE REFERENCE ONLY; not silently mandatory |
| Release-gate script + original `release.json`, controller `SKILL.md`, CI template | public-safe evaluation source export, EVALUATION | RECOVERED, controllers not running real scores |
| Per-competency and per-slice gate rather than average | EVALUATION exact 8+6+6 cells | RECOVERED |
| ≥95% lower-bound minimum, 97%, advance 98–99 | EVALUATION/REQUIREMENTS/CODEX | RECOVERED; **NOT ACHIEVED** |
| Five frozen complete runs, distinct seeds, locked hashes | EVALUATION | RECOVERED; **NOT RUN** |
| Bonferroni one-sided 95% Wilson LCB, ECE≤0.05 | EVALUATION, original controller | RECOVERED |
| Min 1600, per-cell breadth, ≥30 families | EVALUATION exact counts | RECOVERED; **NOT SATISFIED** |
| Zero observed critical errors and exact error taxonomy | EVALUATION | RECOVERED; **NOT DEMONSTRATED** |
| Provenance/citation and holdout security | EVALUATION, ARCHITECTURE, CODEX | RECOVERED; **SECURITY SETUP OPEN** |
| Training answer-key eligibility and performance rollback | PROJECT_SPEC/ARCHITECTURE/REQUIREMENTS | RECOVERED |
| App implementation plan, first Codex action, project persistence | IMPLEMENTATION_PLAN, FIRST_CODEX_PROMPT, CODEX, AGENTS | RECOVERED |
| Every file within original consolidated ZIP | SOURCE_ARTIFACT_MANIFEST.json (one row/member), preserved ORIGINAL archive | RECOVERED **as offline bytes** |
| Prior checklist | original `IMPLEMENTATION_CHECKLIST.md` copied without changing gate | RECOVERED |
| Reference schematic images | original five `systemkarte*.png` under package `reference/visuals/` | RECOVERED; optional visual references |

## B. Explicitly NOT yet transferred into the PUBLIC app repository

These omissions are deliberate or unavoidable; **do not mark them COMPLETE**:

1. **The 316 original benchmark ZIP members have not all been committed to public GitHub**. Public-safe sources are staged for selective import. 231 `benchmarks/internal/*` members and other review-required assets must remain out of this public repository to protect first-pass answer candidates, private constraint labels and hidden split details. The **complete original ZIP is transferred into the DOWNLOAD package only**, not the public repo.
2. **21 individually created first-party ZIP archives** are preserved as original offline artifacts in the downloadable package; these are not blindly extracted/committed as duplicates to the public app repo.
3. **The two standalone Markdown skills** (`Critical Thinking .md`, `DeSpin.md`) are preserved in the downloadable package. Their supplementary referenced `references/*.md` files may be absent as separate standalones; audit references before using any unprovided file as an authority.
4. **Five original visual system diagrams** are preserved in the package but not yet added to app assets/UX; they are conceptual visuals, not binding implementation wireframes.
5. **Third-party downloaded repository ZIPs**, even if present locally (DSPy, PaperQA, STORM, Promptfoo, Loopy, SDEverywhere etc.), are listed by hash but intentionally **not re-vendored** pending license and dependency review. Inspect AI, Argilla, Cleanlab and other recommended upstream repos were never bundled here as complete vendor source.
6. **All nine external scientific datasets** are metadata references only. No dataset redistribution/license grants, downloads or official complete benchmark runs are provided.
7. **Actual independently adjudicated gold/locked holdout DOES NOT EXIST** yet at required breadth. A separate truly blind Annotator B and independent C must still perform the work; first-pass candidates are not verified gold.
8. **No real model evaluation** achieved a measured 95% / 97% under the original eight-competency, six-slice, six-intersection gate. The original six controller tests only check scripts with synthetic fixtures.
9. **The active qualified master `persuasion-gym/SKILL.md` was expressly never created** because the specialist release gate was not passed. `CODEX.md`, `AGENTS.md` and original evaluation `SKILL.md` DO NOT replace or falsely certify it.
10. **A concrete running app implementation in the NEW repository does not exist** yet. The older beta PR belongs to a different repository and was explicitly excluded. The app framework, hosting, model/provider, auth, database, UI branding/billing and deployment are not binding from this conversation; codify choices in ADRs with explicit user approval.
11. **A real independent fact-check provider and source retrieval ledger** are not implemented; therefore no production claim may be declared externally verified by the app.
12. **Actual user skill event persistence/adaptive content routing** against gold answer keys is not wired in new app. The standalone model and update scripts are specifications/prototypes requiring real tests and privacy rules.
13. **Statistical power for 95% multiplicity-corrected lower-bound across all cells** is not shown. The original hard sample minima do not alone guarantee ability to pass.
14. **Potential tooling gaps** identified previously: original blind packet generator must be checked not to expose split/design clues; legacy compare_annotations field paths/IDs and promote_gold enforcement need audit before use; dependency lock versions and Python vs Node Promptfoo identity need recheck. These were not silently declared repaired.
15. **The public new repo was empty at initial audit and has since received one safe README commit**. This package is prepared for documentation-first initialization; GitHub build/test CI cannot yet be claimed on this new repo.

## C. Conflicts/precision notes that Codex must NOT gloss over

- “Test intent/causal/level separation — DONE” in prior messages meant **suite built**, not model passed. The stricter user wording “test” does not imply evaluated accuracy.
- “Build gold-standard corpus” in earlier checklist means **candidate design**. First-pass labels are marked pending independent adjudication, so **actual gold readiness is false**.
- The original benchmark suite requires extremely conservative **adjusted confidence lower bounds**, not simply 95% point accuracy or five-run average. Statistical power might require far more than 1,600 examples.
- Original FActScore is both an external registry entry and a diagnostic tool; external registries contain nine entries exactly, no physical datasets.
- `SKILL.md` exists in several *specialist* folders and evaluation controller. That is **not** proof an active master persuasion skill exists.
- The older beta app's `PRELIMINARY_UNVERIFIED` object was a limited projection. The full **canonical schema** is authoritative for final app.
- Release-gate policy uses frozen model and hash consistency. Changing a prompt, model, schema, dependency, scorer, benchmark labels or evaluator invalidates prior qualification and requires a new release record.
- The user asked for a new repository and restricted reliance on the old one. Prior *principles* recovered from conversation are allowed; copying old code is not.

## D. Audit completion standard

The implementation-package **inventory** is complete for source artifacts in the current working environment: source ZIP integrity and exact 316 member hashes, all available first-party archive copies, original 2 standalone skills and five diagram files are mapped. It does **not** mean every historical item ever referenced in an unavailable older chat or remote repo can be inspected now; any such link is separately marked `REFERENCE_ONLY` or `OPEN`. No missing scientific/engineering requirement has been invented to fill that gap.

**File checks:** 316-member source inventory; 74 safe imported files match SHA256; 22 preserved first-party source ZIPs have valid integrity. Original `check_package.py` passes with 400 provisional cases and 9 external references; all 6 controller unit tests pass; incomplete held-out fixture returns `BLOCKED` (these are infrastructure checks, not real model accuracy).

**Final status:** `DOCUMENTATION_RECOVERED`, `SOURCE_PACKAGE_PRESERVED_OFFLINE`, `PUBLIC_REFERENCE_EXPORT_PREPARED`, `IMPLEMENTATION_NOT_STARTED`, `SCIENTIFIC_RELEASE_BLOCKED`.
