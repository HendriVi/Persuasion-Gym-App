# Persuasion Gym — requirements and acceptance criteria

This file turns *already stated requirements* into testable conditions; no new commercial/product promises are implied. Source IDs are semantic references back to the original canonical ontology, specialist skill files and 95/97 benchmark policy. All status terms are the actual original schema enums wherever available.

## A. Functional requirements

| ID | Requirement | Observable acceptance |
|---|---|---|
| F-01 | Accept and preserve bounded artifact with provenance, segments, modality and context | stable IDs, round-trip exact spans, no text alteration without canonical offsets |
| F-02 | Produce independent multilevel canonical Analysis object | JSON validates against **original** common schema; every required module and version field present |
| F-03 | Identify rhetorical operations using original 12-family taxonomy, multi-label anchors | annotated quote and offset grounded in raw artifact; taxonomy IDs not invented |
| F-04 | Parse argument structure and distinguish validity/strength from true premises | fixtures covering valid argument with false premises; true premises/invalid conclusion; genuine binary decision without fallacy |
| F-05 | De-Spin literal claim vs likely inference vs missing context and baselines | claim ledger includes conditions/denominators/omissions and requires corroboration |
| F-06 | Independently verify factual claims against canonical sources | claim-level status, URL/title/issuer/date/excerpt/authority/independence and contrary evidence record; otherwise UNVERIFIED/UNRESOLVED |
| F-07 | Link rhetoric to psychological *candidate* pathways via original registry | mechanism IDs from registry; alternatives/moderators; activation never automatically asserted |
| F-08 | Enforce documented vs inferred/private intent status | UNKNOWN default; EXPLICIT/DOCUMENTED only with relevant proof; no motive read from tone/benefit |
| F-09 | Enforce causal identification scope and mediation/mechanism firewall | random treatment effect scoped; observational/mediated claims cannot auto-promote to mechanistic causality |
| F-10 | Represent system factors and feedback as hypotheses unless edges supported | each edge tagged with direction/evidence/identification assumptions; no arrow laundering |
| F-11 | Assess manipulation independently on nine dimensions + voluntariness/materiality | valid INDETERMINATE; true persuasion may be nonmanipulative; false claim not automatic intent |
| F-12 | Cross-layer integrity/consistency check and dependency invalidation | forbidden inferred promotions rejected; material verification changes mark dependencies REANALYSIS_REQUIRED |
| F-13 | Generate clear analytic report, countermeasures and alternative interpretations | claims visibly sourced/qualified; unresolved not hidden; explanations do not rewrite status |
| F-14 | Teach with commit-first judgment/confidence, then adjudicated feedback | user answer locked before feedback; incomplete key blocks graded result |
| F-15 | Maintain evidence-backed learner model with specific error codes and transfer | original states+skill registry; attempts and versioned key; practice routing; no stigmatizing traits |
| F-16 | Provide cross-domain exercises and political-mirror controls | exercises evaluate structure symmetrically across congruent/incongruent political positions |
| F-17 | Maintain complete research, benchmark and source provenance | SHA256 source file manifest, trace from module to original source/owner |
| F-18 | Provide opt-in preliminary analysis during development, distinctly not certified | `PRELIMINARY_UNVERIFIED`, scoring disabled, can be disabled with server flag |

## B. Evaluation, evidence and quality requirements

| ID | Requirement | Release condition |
|---|---|---|
| E-01 | Original 400 constructed cases: 96+80+64+80+80 | imported only as candidates, counts/family hashes validated; no fake 'gold' promotion |
| E-02 | Blinded independent annotation plus adjudication | A/B blind procedure, per-layer agreement, adjudication C ledger, accepted alternatives, gold lock |
| E-03 | Holdout breadth | ≥1600 distinct adjudicated cases; ≥200/competence; ≥100/challenge; ≥150/intersection; ≥30 families per cell; enough statistical power |
| E-04 | Frozen runs | 5 complete preregistered runs, same model/prompt/pipeline/rubric/holdout fingerprint, distinct seeds, all rows |
| E-05 | Per-cell statistical floor | in each run each of 8 competencies, 6 named slices and 6 intersections reaches multiplicity-adjusted one-sided Wilson LCB ≥.95 |
| E-06 | Stretch / continuous improvement | same gate at .97, later .98/.99 only under new version + holdout and enough samples |
| E-07 | Critical failures | zero **observed**, independently adjudicated, from original 11-code taxonomy; zero observed ≠ true risk zero |
| E-08 | Calibration | 10-bin ECE ≤0.05 in EACH frozen run, pre-feedback confidence present |
| E-09 | Coverage | errors, missing outputs and abstention count as failures on all-attempt metric, not dropouts |
| E-10 | Original external benchmarks | preserve all 9 in registry with official metrics, acquisition, attribution and license; report separately |
| E-11 | Independent evaluation | independent scorers and real model calls; original release-gate script, not LLM self-scores or synthetic fixture accuracy |
| E-12 | No benchmark leakage | gold/private/holdout absent from public repo/browser/model prompts/CI logs, isolation demonstrably tested |
| E-13 | Repeatability | pinned manifests/hashes, full reports, immutable release attestations, CI reproducibility, no cherry-picked five runs |
| E-14 | Drift | deploy-only matching signed artifact, monitor per-slice degradation, rerun/roll back on critical failures |

## C. Safety, privacy, security

- `S-01` User-supplied artifacts and retrieved web/docs treated as untrusted *data*, not instructions; prompt-injection protection and scoped tool access.
- `S-02` No invented/fake citations or unsupported truth/causal/mechanism claims; source chain auditable.
- `S-03` No asserted hidden speaker intent, diagnosis of recipient or protected-characteristic inference.
- `S-04` Material misleadingness, invalid argument, manipulation and coercion have independent evidence standards. No ideological double standard.
- `S-05` Backend-only secrets/model keys; authenticated access; rate limiting, payload limits, abuse controls, access-control and logging minimization.
- `S-06` No real/private passages or gold in frontend bundles, analytics, public CI logs or optional third-party observability by default.
- `S-07` Legal and licensing review for benchmarks, model providers, datasets, third-party skills and copyrighted content before commercial use.
- `S-08` Privacy consent and retention policy must be approved before production storage of full messages/learner histories; do not invent law-specific promises.
- `S-09` Role segregation of user, model, annotators A/B, adjudicator C, release operator; original hidden tests never accessible to model generation tools.
- `S-10` Safe abstention with user-facing next evidence requests; abstention counted as incorrect for strict release accuracy.
- `S-11` No irreversible learner decisions based on low confidence or provisional answer key; ability to invalidate/refit prior events when official key changes.
- `S-12` Sensitive persuasion/propaganda analytics may analyze harmful text but should not generate targeted exploitative persuasion or personally exploit known vulnerabilities.

## D. UX and educational requirements

- `U-01` Multiple differentiated explanations: what text **does**, what it **claims**, what evidence shows, what is merely **hypothesized**, and how to independently check.
- `U-02` Show original exact quote/anchor for each relevant rhetoric/argument claim; user can inspect alternative interpretations, uncertainty and verification status.
- `U-03` Disclose scope and unverified state prominently; avoid false certainty or graphics that visually turn hypotheses into proven arrows.
- `U-04` Commit first: user must answer/declare confidence before AI reveals full analysis in scored training; no pedagogical cheating via premature reveal.
- `U-05` Provide exact recurring misses by skill + eligible opportunities, correction rationale, cross-domain transfer/delay, calibration without fixed personality labels.
- `U-06` Support comprehension by nontechnical users; compact progression and plain-language mechanism explanations alongside canonical drill-down.
- `U-07` Avoid addictive streak/badge pressure unless separately approved. Learnability, realistic decisions and visible improvement are design values (from prior established project context; confirm detailed UI later).
- `U-08` Mobile/responsive and keyboard/screen-reader accessible **subject to concrete implementation ADR**; accessibility is engineering quality, not a prior finished visual design.

## E. Reliability/operational requirements

- `N-01` Reproducible tests and pinned versions; deterministic evaluation controller, bounded/observable model execution.
- `N-02` Stage-specific errors, timeouts and retries cannot silently produce unsupported conclusions.
- `N-03` Audit logs record data/evidence hashes and stage versions without leaking protected content.
- `N-04` Production validated feature flag OFF before approved signed release.
- `N-05` Runtime efficiency, cost/latency budgets and availability numerical SLOs are **UNDECIDED**; gather real baselines before setting them. No fabricated 99.9% uptime claim.
- `N-06` Stable schema migration and idempotent attempts; corrupted label/version invalidates scores rather than silently remapping.
- `N-07` Preserve official native benchmark metrics and official releases; normalized item correctness only from a documented independent rubric.
- `N-08` Newly generated public exercises must never duplicate hidden lockbox families; use provenance checking and family-based split boundaries.

## F. Unresolved decisions require explicit approval (not mandatory prior facts)

Framework/hosting and deployment, storage/auth/billing provider, target jurisdictions and retention policy, primary language rollout, exact visual design, community/social features, pricing, model selection/temperature/provider, external data acquisition rights, and independent adjudicator staffing. No percentage claim should be made until tested; no 'near 100%' guarantee for arbitrary future inputs.
