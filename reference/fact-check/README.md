# Persuasion Fact-Check

A Persuasion Gym-specific adaptation of the public `fact-check` skill pattern: verification is an independent post-generation pass, not a subroutine mixed into generation.

## Why this version exists

Generic fact-checking is not enough for Persuasion Gym because the app must keep several dimensions separate:

- whether the artifact's factual claim is true;
- whether the AI's background statement is true;
- whether an attribution or quotation is authentic;
- whether a persuasion mechanism is scientifically supported;
- whether an argument is valid;
- whether rhetoric or manipulation is present.

This skill owns only factual / empirical verification and downstream invalidation signals.

## Package

- `SKILL.md` — operational skill
- `references/source-hierarchy.md` — source-of-truth selection
- `references/claim-types-and-statuses.md` — taxonomy and verdict rules
- `assets/verification-report-template.md` — standardized output
- `TESTING.md` — regression and behavioral tests

## Upstream inspiration

The public MIT-licensed `jwynia/agent-skills` fact-check skill emphasizes a separate verification pass, explicit source checking, claim extraction, and claim-level outcomes. This package retains that architecture but specializes it for Persuasion Gym and adds claim-origin separation, scientific-mechanism verification, provenance/truth separation, downstream invalidation, and an answer-key publication gate.
