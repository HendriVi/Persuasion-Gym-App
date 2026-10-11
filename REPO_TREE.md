# Persuasion Gym — canonical target repository tree and external vault map

**The new application is initially EMPTY.** This is the **dependency-ordered destination map**, not a claim these modules currently exist. `repo-root/` in the download is the SAFE starter contents intended for `HendriVi/Persuasion-Gym-App`; `offline-restricted/` and `reference/first-party-zips/` in the DOWNLOAD are **not** GitHub-upload directories.

```
HendriVi/Persuasion-Gym-App/                    # USER-SPECIFIED FINAL APP REPO
├── README.md                                    # safe starter / status
├── AGENTS.md                                    # Codex auto-read entrypoint
├── CODEX.md                                     # required agent operating policy
├── PROJECT_SPEC.md                              # canonical conceptual product spec
├── ARCHITECTURE.md                              # system boundaries/interfaces
├── IMPLEMENTATION_PLAN.md                      # phase-by-phase build order
├── EVALUATION.md                                # per-slice five-run 95/97 gates
├── REQUIREMENTS.md                              # functional/nonfunctional checks
├── DECISIONS.md                                 # adopted/open decisions; ADRs
├── REPO_TREE.md                                 # this destination map
├── SOURCE_ARTIFACT_MANIFEST.md                  # summary and safety rules
├── SOURCE_ARTIFACT_MANIFEST.json                # EVERY original ZIP member and hash
├── COMPLETENESS_AUDIT.md                       # transferred/pending/missing
├── FIRST_CODEX_PROMPT.md                        # first Codex task
├── docs/
│   ├── STATUS.md                                # TODO (not yet created)
│   ├── adr/                                     # TODO decision records
│   ├── ux/                                      # TODO (wireframes not yet approved)
│   └── provenance/                              # public source checksums only
├── reference/                                   # copied verbatim FIRST-PARTY safe source
│   ├── ontology/                                # ONTOLOGY.md, README, TESTING
│   ├── rhetoric-taxonomy/                       # TAXONOMY.md + guides
│   ├── mechanism-registry/                      # REGISTRY.md + guides
│   ├── common-schema/                           # original full JSON Schema + example
│   ├── uncertainty-rules/                       # UNCERTAINTY.md and supporting policies
│   ├── manipulation-boundary/                   # original boundary + examples, scripts
│   ├── rhetorical-structure-analysis/           # SKILL.md, README, TESTING
│   ├── mechanism-analysis/                      # SKILL.md, README, TESTING
│   ├── influence-systems-analysis/              # SKILL.md, README, TESTING
│   ├── fact-check/                              # SKILL.md, README, TESTING
│   ├── agentic-learning/                        # SKILL.md, README, TESTING
│   ├── systems-thinking/                        # SKILL.md, README
│   ├── training/                                # SKILL.md, README, TESTING
│   ├── learner-skill-model/                     # TODO import verified safe source
│   └── standalone/                              # TODO source: Critical Thinking, De-Spin
├── evaluation/                                  # safe release CONTROLLER, not test gold
│   ├── SKILL.md                                 # evaluator instructions NOT master skill
│   ├── README.md
│   ├── IMPLEMENTATION_CHECKLIST.md
│   ├── DO_NOT_UPLOAD_ENTIRE_ZIP_TO_APP.md
│   ├── instructions/                            # release/data/mapping/iteration policies
│   ├── config/release.json                      # ORIGINAL exact strict thresholds
│   ├── scripts/                                 # original stdlib release gate and tests
│   ├── integrations/                            # app guidance + secure CI TEMPLATE
│   └── benchmarks/external/                     # 9 source descriptions and rights
├── apps/                                        # TODO after framework ADR
│   └── web/                                     # client UI (implementation pending)
├── services/                                    # TODO after server ADR
│   ├── api/                                     # auth, routing, model adapters
│   ├── verification/                            # canonical retrieval and citations
│   └── learner/                                 # event model and practice scheduler
├── packages/                                    # TODO production typed module packages
│   ├── contracts/                               # exact schema projection + compatibility
│   ├── ontology/                                # shared stable concepts
│   ├── rhetoric/                                # owned rhetoric annotation
│   ├── argument/                                # owned logic/warrant validation
│   ├── de-spin/                                 # claims and implications
│   ├── mechanisms/                              # candidate pathways
│   ├── causality/                               # evidence proof-burden
│   ├── intent/                                  # documented vs unknown
│   ├── manipulation/                            # autonomy/materiality dims
│   ├── systems/                                 # hypothesized graphs and arrows
│   ├── cross-layer/                             # epistemic promotion firewall
│   ├── report/                                  # generated-language evidence boundary
│   └── learner/                                 # specific mistakes, calibration/transfer
├── tests/                                       # TODO contract/security/UX integration
└── .github/workflows/                           # TODO vetted CI; no vault exposure

OUTSIDE THE GIT REPOSITORY, TRUSTED EVALUATOR ONLY
vault://persuasion-gym/
├── source-archives/
│   ├── persuasion-gym-95-97-benchmark-system.zip # EXACT ORIGINAL SOURCE; 316 files
│   └── individual-first-party-source-zips/       # historical original packages
├── benchmarks/internal/                          # original 231 restricted members
│   ├── gold-corpus/                              # 96 base cases / split detail
│   ├── gold-annotations-candidates/              # FIRST PASS + private candidate keys
│   ├── blinded-adjudication/                      # actual A/B/C process, restricted manifests
│   ├── adversarial/                              # 80 cases / private constraints
│   ├── intent-discipline/                        # 64 cases / private constraints
│   ├── causal-discipline/                        # 80 cases / private constraints
│   ├── level-separation/                         # 80 cases / private constraints
│   └── learner-skill-model/                      # contained reference/fixtures; audit before public export
├── locked-holdout/                              # TODO, *not yet real*
│   ├── locked_manifest.jsonl                     # TODO independently adjudicated only
│   ├── adjudicated_answer_keys/                  # TODO private, never seen by model
│   └── signatures/                               # TODO trusted reviewer
├── annotation/                                  # TODO truly independent A/B/C ledgers
├── frozen-runs/                                 # TODO five complete evaluated run outputs
├── independent-judgments/                       # TODO human/adjudicated scoring rows
└── reports/                                     # TODO signed release attestation and audits
```

## Explicit mapping of each source file

The above displays the semantic tree; the *exhaustive* individual-file map is `SOURCE_ARTIFACT_MANIFEST.json`. It records **all 316 original source ZIP members**, original ZIP-relative paths, SHA256 and a `target_destination` for each. Files mapped to `vault://` are **not** supposed to appear in `HendriVi/Persuasion-Gym-App`. Files mapped to `reference/...` and `evaluation/...` are included in `repo-root` (safe source package) for approved import.

Individual separately generated first-party ZIPs are maintained *unchanged offline* under `reference/first-party-zips/` in the **download package**. The original aggregate ZIP's 316 files are preserved *unchanged* under `offline-restricted/` in the **download package**. Standalone docs and five source diagrams are in the **download package** for vetted later import.

### Mapping of 400 original test items

| Source | Count | Design groups | Final destination |
|---|---:|---|---|
| Base 'gold' corpus — candidate | 96 | 24 × four variants, 12 domains | private evaluator, original family split kept |
| Adversarial suite | 80 | 20 × four variants | private evaluator / public dev probes only after classification |
| Intent discipline | 64 | 16 × four variants | private evaluator |
| Causal discipline | 80 | 20 × four variants | private evaluator |
| Level separation | 80 | 20 × four variants | private evaluator |
| **Total** | **400** | | Not independently locked gold |

The first-pass labels, `holdout_gold_candidate.jsonl`, private `gold_constraints.jsonl`, design manifests and other privileged files **MUST NOT** be added to the public repository, including under `.github/`, `public/`, `test/fixtures/` or `.private/` folders (Git history remains visible).

### External benchmarks: metadata vs raw data

The nine entries belong to `evaluation/benchmarks/external/BENCHMARK_REGISTRY.json` (safe metadata). **Their datasets and code are not in the first-party ZIP**. Authorized downloaded upstream release + official scorer should be installed in the restricted evaluator under versioned acquisition records after rights review. The target app must not vendor a noncommercial dataset by default.

### Source hierarchy reminder

`reference/**` = authored specialist normative source. `evaluation/**` = **release controller, not master skill**. `packages/**` / `services/**` = **future implementations**, required to conform to those sources. The master `persuasion-gym/SKILL.md` remains **NOT PRESENT / RELEASE BLOCKED** and must only be authored after passing real evaluation.
