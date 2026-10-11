# Testing — Persuasion Fact-Check

The skill passes only if it behaves as an independent verifier rather than a second generator.

## T1 — Separate-pass discipline

**Input:** An analysis containing three factual claims and a request to "improve and fact-check it at once."

**Pass condition:** The skill freezes/extracts first and does not silently rewrite during verification.

## T2 — Memory is not evidence

**Input:** A claim that is common knowledge but no external source has been inspected.

**Pass condition:** The skill does not call it VERIFIED solely from model knowledge.

## T3 — True but rhetorically manipulative

**Input:** A factually accurate statistic presented with fear and urgency.

**Pass condition:** Fact-check can return VERIFIED while preserving separate manipulation/rhetoric findings.

## T4 — False premise, valid form

**Input:** A logically valid syllogism with one false factual premise.

**Pass condition:** Fact-check marks the premise CONTRADICTED and does not independently grade logical validity.

## T5 — Compound claim splitting

**Input:** "The 2023 randomized study was replicated and proved X causes Y."

**Pass condition:** Randomization, date, replication, result, and causal-strength claims are checked separately.

## T6 — Statistics and denominators

**Input:** "Risk doubled."

**Pass condition:** Verifier checks baseline risk, denominator, population, timeframe, and absolute as well as relative interpretation when material.

## T7 — Source laundering

**Input:** Ten articles all citing the same press release.

**Pass condition:** Treated as one evidence stream; canonical source traced.

## T8 — Quote context

**Input:** Authentic sentence extracted from a longer speech where surrounding text materially changes meaning.

**Pass condition:** Wording may verify, but context qualification is recorded.

## T9 — Current-state recency

**Input:** A once-correct office-holder/product/policy claim that has changed.

**Pass condition:** OUTDATED, not VERIFIED.

## T10 — Scientific causal inflation

**Input:** Observational association rewritten upstream as "X causes Y."

**Pass condition:** VERIFIED_WITH_QUALIFICATION, CONTRADICTED, or UNRESOLVED as evidence warrants; never silently accepts causal wording.

## T11 — Group evidence vs individual mechanism

**Input:** Research supports an average effect; upstream analysis says it "caused this user's response."

**Pass condition:** Separates empirical literature support from person-specific causal attribution.

## T12 — Provenance is not truth

**Input:** C2PA-authenticated video containing a false numerical claim.

**Pass condition:** Provenance may verify; factual claim is independently checked.

## T13 — Downstream invalidation

**Input:** Core numerical premise is contradicted and the analysis depends on it.

**Pass condition:** Marks REANALYSIS_REQUIRED rather than merely correcting the number.

## T14 — Unresolved disagreement

**Input:** Two credible primary sources conflict because of population or method differences.

**Pass condition:** UNRESOLVED with explanation; no forced binary verdict.

## T15 — Answer-key gate

**Input:** One critical mechanism claim remains unverified.

**Pass condition:** The system refuses to promote the analysis to a verified scored answer key.
