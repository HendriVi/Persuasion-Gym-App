# Persuasion Gym Canonical Ontology

Version: 0.1.0  
Status: canonical domain vocabulary for the Persuasion Gym analysis stack

## Purpose

This package defines the shared entities, roles, relations, epistemic labels, and validation rules that every Persuasion Gym specialist skill must use.

It exists to prevent level-of-analysis drift such as:

- treating a rhetorical device as a psychological mechanism;
- treating a hypothesized mechanism as an observed fact;
- treating a mediator or moderator as a permanent kind of variable;
- treating factual truth as argument validity;
- treating persuasion as manipulation;
- treating speaker intent as equivalent to functional effect;
- treating an individual response as a social or system outcome;
- treating a systems arrow as causal evidence.

The ontology is deliberately modular. Specialist skills may extend it, but may not redefine the canonical terms without an ontology version change.

## Core architecture

The canonical analytical chain is:

**artifact → proposition/claim → argument structure → message feature → influence pathway → internal response → belief/attitude → action tendency → behavior → social/system consequence → feedback → countermeasure**

Not every analysis needs every stage. Missing stages must remain missing rather than being inferred merely to complete the chain.

## Design influences

The ontology is original to Persuasion Gym, but its structure is informed by:

- Toulmin-style separation of claim, grounds, warrant, backing, qualifier, and rebuttal;
- Friestad & Wright's Persuasion Knowledge Model distinction between persuasion agent, target, persuasion attempt/episode, tactics, and coping knowledge;
- social-psychological separation of mediator and moderator roles;
- W3C PROV-style provenance discipline;
- the existing Persuasion Gym De-Spin, Critical Thinking, Systems Thinking, Agentic Learning, and Fact-Check skills.

These influences constrain vocabulary and provenance discipline; they do not imply that Persuasion Gym is an implementation of any one theory.

## Package contents

- `ONTOLOGY.md` — normative ontology specification
- `references/entity-types.md` — canonical entity definitions
- `references/relation-types.md` — canonical relation vocabulary and allowed edge types
- `references/epistemic-status.md` — observation, inference, evidence, verification, and intent-status rules
- `references/manipulation-assessment.md` — manipulation-risk object and its dimensions
- `assets/analysis-object-schema.yaml` — machine-readable canonical analysis object
- `TESTING.md` — ontology validation and regression tests

## Canonical rule

A term is canonical only if it is defined in this package. Specialist skills may add local fields, but when exchanging data across skills they must map local terminology to these canonical terms.
