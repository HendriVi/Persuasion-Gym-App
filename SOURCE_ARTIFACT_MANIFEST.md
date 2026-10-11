# Persuasion Gym — complete source artifact mapping

**Machine-readable authoritative inventory:** `SOURCE_ARTIFACT_MANIFEST.json` lists EACH original non-directory source ZIP member (all 316 members as discovered at audit) with exact original ZIP path, SHA256, size, visibility and designated destination. **Do not interpret presence in a source bundle as scientific validation.**

- Consolidated source ZIP SHA256: `5d7528d846188e30ca1f5764656a331ba7eeedcaa91d6c75c42186242a7c6b62`.
- Source ZIP members inventoried: **316**.
- First-party separately generated ZIPs preserved offline: **21**.
- Additional standalone specialist sources preserved: **2** (Critical Thinking, De-Spin).
- Systems reference images preserved: **5**.
- External scientific benchmark datasets: **NOT INCLUDED**, only 9 metadata entries/links; obtain under rights and verify original scorers.
- Existing master `persuasion-gym/SKILL.md`: **NOT YET CREATED/QUALIFIED**; this is an explicit missing-gated artifact, not a forgotten source.

## Classification and planned destination
| Classification | Count | Destination |
|---|---:|---|
| `REVIEW_BEFORE_EXPORT` | 4 | vault until reviewed |
| `PUBLIC_EVALUATION_INFRASTRUCTURE` | 20 | `evaluation/**` in target repository, safe code and governance |
| `RESTRICTED_CANDIDATE_AND_BENCHMARK_SOURCE` | 231 | private external vault **ONLY** |
| `RESTRICTED_OR_FIXTURE_REVIEW` | 6 | vault until hand classified |
| `SOURCE_PROVENANCE_OFFLINE` | 1 | vault until reviewed |
| `PUBLIC_CANONICAL_REFERENCE` | 54 | `reference/**` in target repository, original skills/schemas |

## Original source archives, all preserved as-is in the downloadable offline package

| Original artifact | SHA256 (prefix) | Size bytes |
|---|---|---:|
| `persuasion-agentic-learning-skill.zip` | `e8a43fb27c92c1a2` | 19952 |
| `persuasion-fact-check-skill.zip` | `9d2c10f2cb7112ec` | 14272 |
| `persuasion-gym-adversarial-tests.zip` | `f036fc0970c887bd` | 47339 |
| `persuasion-gym-blinded-annotation-stack.zip` | `6a7c7cf9c1299c6b` | 356319 |
| `persuasion-gym-causal-discipline-tests.zip` | `432e6aeb49e335bf` | 22971 |
| `persuasion-gym-common-schema.zip` | `e89ee8a063c5a13f` | 23126 |
| `persuasion-gym-gold-annotations.zip` | `1d7341cf569517e1` | 42736 |
| `persuasion-gym-gold-corpus.zip` | `0da445e10e36b9eb` | 34968 |
| `persuasion-gym-intent-discipline-tests.zip` | `81ab36c0727c99a0` | 22611 |
| `persuasion-gym-level-separation-tests.zip` | `1b7330d104f0652e` | 21792 |
| `persuasion-gym-manipulation-boundary.zip` | `f70c7f5e441e835f` | 16263 |
| `persuasion-gym-ontology.zip` | `2682546ec55e2722` | 18127 |
| `persuasion-gym-uncertainty-rules.zip` | `a18186bb727b0080` | 17328 |
| `persuasion-influence-systems-analysis-skill.zip` | `091f5d7e7e05c273` | 22297 |
| `persuasion-mechanism-analysis-skill.zip` | `068f70431519ce46` | 19983 |
| `persuasion-psychological-mechanism-registry.zip` | `555d72b5baf0643a` | 20299 |
| `persuasion-rhetoric-taxonomy.zip` | `2282846907e79b53` | 16625 |
| `persuasion-rhetorical-structure-analysis-skill.zip` | `7d34357a208416b0` | 17703 |
| `persuasion-systems-thinking-skill.zip` | `1af60f9dca5dc823` | 15495 |
| `persuasion-training-skill.zip` | `2c45144191d825dc` | 18144 |
| `persuasion-user-skill-model.zip` | `a09d961b0f350036` | 34662 |

## Standalone source documents

| File | Original hash | Destination |
|---|---|---|
| `Critical Thinking .md` | `acc60b70f3d7f9b6` | `reference/standalone/Critical Thinking .md` |
| `DeSpin.md` | `f209d2cbf8698770` | `reference/standalone/DeSpin.md` |

## External/recommended repositories (NOT vendored)

The locally available auxiliary ZIPs listed below are preserved by hash/reference only (not bundled in public spec and not automatically installed):
- `PromptFoo-main(20261007-123209).zip` — available, SHA256 `60622874e044106f`
- `dspy-main(20261007-123211).zip` — available, SHA256 `0a7ad72cb3df41f6`
- `gpt-researcher-main(20261007-123211).zip` — available, SHA256 `82f580069e491362`
- `paper-qa-main(20261007-123213).zip` — available, SHA256 `a703a702b178a678`
- `paper-qa-main(20261007-142141).zip` — available, SHA256 `d5eb6d96db0b0be1`
- `storm-main(20261007-123211).zip` — available, SHA256 `0facaacfffe11976`
- `storm-main(20261007-142134).zip` — available, SHA256 `0facaacfffe11976`
- `loopy-gh-pages(3).zip` — available, SHA256 `b6eb1fafead189ae`
- `SDEverywhere-main(1).zip` — available, SHA256 `e25c5a19b7811d23`
- `scientific-agent-skills-main(20261007-142137).zip` — available, SHA256 `dad52daa77428bb9`
- `thinkgpt-main(1).zip` — available, SHA256 `6ed6e976b85f84a5`
- `avoid-ai-writing-main(20261007-142134).zip` — available, SHA256 `b525f2c287398839`
- `think-in-systems-webstudio(1).zip` — available, SHA256 `642f8bbbed52f981`

## Rule for Codex

Read this manifest before imports. Import only `PUBLIC_*` into GitHub by default. Do not upload nested ZIPs or use a convenient recursive copy. Copy `RESTRICTED_*` only into a separate approved controlled vault after a security decision; do not use the public app repo as that vault. Check the full source-to-target mapping in `SOURCE_ARTIFACT_MANIFEST.json` rather than assuming all files should live in the repo.

The previously discussed older app PR and its beta code are NOT part of this manifest because the user explicitly prohibited treating it as the source of truth. Architecture and release requirements are reconstructed from original Persuasion Gym files here.
