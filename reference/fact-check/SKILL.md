---
name: persuasion-fact-check
description: >-
  Independent final verification pass for Persuasion Gym. Use only after the
  rhetorical, argument, mechanism, systems, or educational analysis has been generated
  and frozen. Extract every materially verifiable claim from the original artifact and
  the generated analysis, verify each against external authoritative sources, assign an
  explicit evidence status, and return a verification ledger plus correction requests.
  Never perform verification implicitly during generation, never use model memory as
  evidence, and never rewrite rhetorical or psychological conclusions merely because a
  factual claim passes or fails verification.
license: MIT-compatible original adaptation; see README.md for upstream inspiration
compatibility: AgentSkills-compatible agents and app orchestration pipelines
metadata:
  version: "0.1.0"
  project: "Persuasion Gym"
  role: "independent post-generation factual verification"
---

# Persuasion Fact-Check

## Purpose

Provide an **independent final verification pass** after Persuasion Gym has completed
its substantive analysis.

The skill exists to prevent five common errors:

1. a persuasive artifact contains a factual claim that was never checked;
2. the AI analysis introduces a factual claim that sounds plausible but is unsupported;
3. an attribution, quote, statistic, date, or source is wrong;
4. a psychological mechanism is described more strongly than the evidence allows;
5. a factual correction silently changes a separate rhetorical, logical, or systems judgment.

Core principle:

> **Generation and verification are different jobs. Finish one, freeze it, then run the other.**

This skill is quality control. It does not generate the Persuasion Gym analysis and it
does not replace the specialist skills that produced it.

---

# 1. Non-negotiable separation rule

## Verification must be a separate pass

Before this skill starts, the upstream analysis must be treated as a frozen input.

Do not:

- continue drafting while fact-checking;
- change a claim and then immediately "verify" the changed wording from memory;
- allow stylistic coherence to substitute for evidence;
- ask the same generative reasoning process whether its own unsupported claim "sounds right";
- silently repair factual problems inside the verification ledger.

Instead:

1. freeze the artifact and analysis snapshot;
2. extract claims without judging them;
3. verify against external sources;
4. record findings;
5. issue correction requests where needed;
6. return the result to the orchestrator or drafting layer for a separate revision pass.

A revised analysis, if produced, should receive another verification pass for any changed
material claims.

---

# 2. This skill owns

- extraction of materially verifiable claims;
- classification of claim type and origin;
- source selection for verification;
- source provenance recording;
- exact verification of numbers, dates, names, quotations, attributions, definitions,
  empirical findings, and externally checkable causal claims;
- recency checks for time-sensitive claims;
- contradiction and qualification detection;
- claim-level confidence and evidence status;
- correction requests;
- a final verification gate for public or scored outputs.

# 3. This skill does not own

- rhetorical-device identification;
- argument validity or fallacy analysis;
- speaker intent;
- manipulation classification;
- psychological profiling;
- causal-loop construction;
- learner scoring;
- rewriting the analysis;
- deciding that a persuasive claim is misleading merely because a technique is present;
- deciding that a rhetorical technique disappears merely because the underlying fact is true.

Route those questions to their specialist modules.

---

# 4. Verification targets

Every claim must record its `claim_origin`.

## A. Artifact claim

A factual claim made by the speech, article, advertisement, post, debate, negotiation,
or other persuasive artifact being analyzed.

Example:

> "Crime increased 40% last year."

Verify the statistic independently. Do not infer whether the speaker deliberately lied.

## B. Analysis claim

A factual assertion introduced by Persuasion Gym's own analysis.

Example:

> "The campaign launched in 2024."

This is especially important because an analysis can correctly identify rhetoric while
hallucinating background facts.

## C. Attribution / provenance claim

A statement about who said, published, produced, funded, edited, or originated something.

Example:

> "This quotation is from the WHO report."

Verify the attribution and, when material, the original context.

## D. Empirical mechanism claim

A scientific statement used to justify a persuasion mechanism.

Example:

> "Repeated statements are often rated as more truthful than novel statements."

Verify that the literature supports the stated effect and its scope. Do not automatically
convert a group-level experimental result into a claim about what happened inside one
specific person.

## E. Current-state claim

A claim that can change with time: office-holder, law, policy, product feature, price,
platform behavior, public statistic, organizational status, etc.

These require an explicit recency check.

---

# 5. Claim extraction

Read the **entire frozen analysis** and the relevant original artifact before verifying.

Extract every material statement whose truth can be checked externally.

Prioritize:

- numbers and percentages;
- dates and chronology;
- names and identities;
- quotations;
- source attributions;
- definitions presented as authoritative;
- research findings;
- causal claims presented as empirical facts;
- prevalence or frequency claims;
- "first", "largest", "most", "only", "all", "none", and similar superlatives;
- current laws, roles, policies, product behavior, or institutional facts;
- historical claims;
- claims that materially support a verdict, mechanism, or training answer.

Do not force verification of:

- clearly marked opinions;
- explicitly hypothetical examples;
- normative preferences;
- pure logical deductions from already stated premises;
- transparent system-map hypotheses already labeled speculative;
- speaker intent unless supported by independent evidence.

When uncertain, include the claim but classify it `scope_uncertain` rather than dropping it.

Load `references/claim-types-and-statuses.md` when extracting claims.

---

# 6. Preserve exact claim wording

For every claim create a ledger entry containing:

- `claim_id`;
- `claim_origin`;
- exact claim text;
- location in source/analysis;
- claim type;
- materiality;
- time sensitivity;
- source required;
- verification status;
- evidence summary;
- correction request if needed.

Do not paraphrase the claim before deciding what is being verified. A small wording change
can change the burden of evidence.

For compound claims, split them.

Bad:

> "The study was randomized, replicated, and proved that fear causes sharing."

Better:

1. The study was randomized.
2. The finding has been independently replicated.
3. The study supports a causal effect of fear on sharing.
4. The evidence justifies the word "proved".

---

# 7. Select the source that can actually settle the claim

Use the source hierarchy in `references/source-hierarchy.md`.

General rule:

> Prefer the **closest authoritative source of truth for the exact proposition**, not the most polished secondary explanation.

Examples:

- empirical result → original paper, dataset, trial registration, or systematic review when the claim itself is about the broader evidence base;
- law or regulation → statute, regulator, court, or official legal text;
- company behavior → official documentation, filing, source code when appropriate, or direct measurement;
- public statistics → original statistical agency or dataset;
- quotation → original transcript, recording, publication, or archival source;
- historical event → primary record where feasible, otherwise high-quality scholarly secondary source;
- current office/status → official institution or authoritative current record;
- media provenance → original publisher / asset provenance; C2PA credentials may support provenance when present but do not establish factual truth.

A search-result snippet is discovery evidence, not final verification evidence.

---

# 8. Lateral verification

Do not judge credibility only from the page making the claim.

For material claims:

1. identify the originating or canonical source;
2. inspect the source directly;
3. check date, scope, definitions, population, denominators, and methods;
4. find independent corroboration when the claim is consequential or the source has a material conflict of interest;
5. actively search for the strongest credible contradiction or qualification.

Do not treat ten reposts of one source as ten independent confirmations.

---

# 9. Scientific mechanism verification

When verifying a persuasion-mechanism claim, use the scientific standard rather than a
simple web-consensus standard.

Record:

- construct being claimed;
- population/context studied;
- experimental vs observational evidence;
- effect direction;
- uncertainty / heterogeneity;
- replication or review status where available;
- whether the upstream wording matches the strength of evidence.

Distinguish:

**Evidence supports an average effect under studied conditions**

from

**This mechanism caused this individual's response.**

The first may be empirically supported. The second usually requires person-specific evidence
and should remain an inference unless directly established.

If upstream language says `causes`, `proves`, `always`, `works because`, or similar language,
check whether the source justifies that strength.

---

# 10. Verification statuses

Use exactly one primary status per claim:

- **VERIFIED** — the authoritative evidence supports the claim within its stated scope.
- **VERIFIED_WITH_QUALIFICATION** — the central claim is supported but requires a material
  condition, narrower scope, denominator, timeframe, population, or uncertainty statement.
- **CONTRADICTED** — credible evidence directly conflicts with the claim as stated.
- **UNVERIFIED** — no adequate source was found or supplied; absence of evidence is not evidence
  of falsity.
- **OUTDATED** — the claim was previously accurate or source-backed but no longer represents the
  relevant current state.
- **UNRESOLVED** — credible evidence conflicts, source mapping is ambiguous, or the available
  evidence cannot settle the proposition.
- **NOT_APPLICABLE** — the item was extracted but is not a factual proposition suitable for
  external verification.

Do not use model confidence as a verification status.

Load `references/claim-types-and-statuses.md` for decision rules.

---

# 11. Confidence is separate from status

Each material claim also receives confidence:

- **High** — direct authoritative evidence; wording and scope align closely;
- **Moderate** — credible evidence supports the conclusion but interpretation or scope remains;
- **Low** — indirect, incomplete, conflicting, or weakly mapped evidence.

`VERIFIED + Low confidence` is possible when the source is the best available authority but
has limitations. `UNRESOLVED + High confidence` is possible when it is very clear that the
evidence base itself is genuinely unresolved.

---

# 12. Verification must not overwrite other analytical dimensions

Maintain these as separate judgments:

**factual truth** ≠ **argument validity** ≠ **rhetorical function** ≠ **psychological mechanism** ≠ **manipulation risk**

Examples:

### True but rhetorically selective

A statistic may be factually correct while the framing omits a relevant denominator.
Fact-check result: `VERIFIED`.
De-Spin/rhetoric result may still identify selective framing.

### False premise, valid form

An argument can be logically valid while depending on a contradicted factual premise.
Fact-check marks the premise `CONTRADICTED`; Critical Thinking owns the validity judgment.

### Manipulative technique, true proposition

An urgency cue can accompany a true factual claim. Verification does not erase the urgency cue.

### Weakly supported mechanism, true artifact claim

The underlying statement may be true while the AI's explanation of *why it persuaded people*
is scientifically overconfident. Verify those as separate claims.

---

# 13. Media and provenance

If the artifact's origin, editing history, or authenticity materially affects the analysis:

1. locate the original or earliest reliable source;
2. compare the supplied version with the original context;
3. inspect available provenance metadata or content credentials when relevant;
4. record what provenance evidence establishes;
5. do not infer truth from provenance alone.

A valid provenance chain can help establish **where content came from and how it changed**.
It does not establish that claims inside the content are true.

---

# 14. Correction requests, not silent corrections

When a claim fails verification, emit a structured correction request:

- original claim;
- status;
- reason;
- evidence;
- minimal safe correction;
- whether downstream reasoning may need re-analysis.

Examples:

> Replace "proved" with "found evidence consistent with" unless stronger causal evidence is supplied.

> Correct 43% to 34%; rerun any downstream argument that depends materially on the magnitude.

The fact-check skill must **not itself rewrite the entire analysis**.

---

# 15. Downstream invalidation

For every contradicted or materially qualified claim ask:

> Which downstream conclusions depended on this proposition?

Mark those outputs:

- `NO_MATERIAL_EFFECT`;
- `REVIEW_REQUIRED`;
- `REANALYSIS_REQUIRED`.

Do not automatically declare the entire rhetorical analysis invalid because one factual claim failed.
Conversely, do not leave a mechanism or conclusion untouched when its evidence premise was essential.

---

# 16. Publication / scoring gate

Before a Persuasion Gym analysis is presented as verified, used as an answer key, or used to
score a learner:

1. all **material** factual claims must have a verification status;
2. all `CONTRADICTED` claims must have correction requests;
3. all `UNVERIFIED`, `OUTDATED`, or `UNRESOLVED` material claims must be visibly qualified;
4. empirical mechanism claims used as scoring keys must have adequate scientific support;
5. any `REANALYSIS_REQUIRED` dependency must be returned upstream before final scoring;
6. no pending delegated source checks may remain hidden.

If the gate fails, the output may still be shown as **unverified analysis**, but it must not be
represented as a validated answer key.

---

# 17. Output format

Use `assets/verification-report-template.md`.

The final verification report must contain:

1. **Verification status** — PASS / PASS WITH QUALIFICATIONS / FAIL / UNRESOLVED.
2. **Scope** — exactly what artifact and analysis snapshot were checked.
3. **Material claim ledger** — every material claim, origin, status, confidence, and source.
4. **Corrections required** — concise, actionable changes.
5. **Downstream impact** — which conclusions require review or reanalysis.
6. **Unverified remainder** — claims not settled and why.
7. **Source ledger** — canonical source, access date, role, limitations.

Do not bury failed claims inside prose.

---

# 18. Anti-patterns

## Verify while generating

**Problem:** coherence pressure and prior output anchor the verifier.

**Fix:** freeze first; verify second.

## Memory-as-source

**Problem:** "I know this is true" is not external verification.

**Fix:** require an inspectable source or mark `UNVERIFIED`.

## Search-snippet verification

**Problem:** snippets truncate context and may reflect secondary summaries.

**Fix:** open and inspect the source that can settle the proposition.

## Majority-vote verification

**Problem:** repeated copies of one claim create fake independence.

**Fix:** trace provenance and count evidence streams, not pages.

## Authority theater

**Problem:** prestigious source cited outside its area or not actually supporting the claim.

**Fix:** verify exact relevance and scope.

## Fact/rhetoric collapse

**Problem:** true claim assumed non-manipulative or false claim assumed manipulative.

**Fix:** keep dimensions separate.

## Causal inflation

**Problem:** correlational or group-level evidence rewritten as individual causal certainty.

**Fix:** narrow the claim to what the study actually establishes.

## Silent repair

**Problem:** verifier edits the claim and then reports it as verified.

**Fix:** preserve original claim; issue a correction request; verify the revised claim in a new pass.

## Citation laundering

**Problem:** secondary source cites a paper; analysis cites the secondary source as though the paper
were inspected.

**Fix:** retrieve the primary source when the claim depends on it.

## Provenance = truth

**Problem:** authenticated media treated as factually accurate.

**Fix:** provenance and truth are separate checks.

---

# 19. Integration with Persuasion Gym

Recommended orchestration order:

1. artifact ingestion;
2. rhetorical structure analysis;
3. Critical Thinking / argument analysis;
4. De-Spin when relevant;
5. persuasion-mechanism analysis;
6. systems analysis when dynamics matter;
7. **freeze analysis**;
8. **Persuasion Fact-Check**;
9. correction / reanalysis if required;
10. second verification of materially changed claims;
11. Agentic Learning converts reconciled results into exercises;
12. only then may the result become a scored answer key.

The fact-checker should have access to the frozen output and source-retrieval tools, but should
not be instructed to optimize prose, pedagogical flow, or persuasive quality during verification.

---

# 20. Exit criteria

Stop only when:

- every material verifiable claim has a status;
- each material status has source evidence or an explicit evidence gap;
- quotations, numbers, dates, and attributions have been checked at appropriate precision;
- time-sensitive claims have a recency check;
- empirical mechanism claims match the strength and scope of their evidence;
- correction requests are explicit;
- downstream dependencies have been marked;
- no unresolved material claim is disguised as verified;
- the publication/scoring gate is clearly PASS, PASS WITH QUALIFICATIONS, FAIL, or UNRESOLVED.
