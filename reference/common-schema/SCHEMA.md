# Canonical Object Guide

The JSON Schema is normative; this file explains the reasoning model.

```text
Artifact / segments
      ↓
Canonical claims ───────────────┐
      ↓                         │
Rhetoric annotations            │
      ↓                         │
Argument structure              │
      ↓                         │
Candidate mechanism pathways    │
      ↓                         │
Person-specific evidence        │
      ↓                         │
System variables / relations    │
      ↓                         │
Manipulation assessment         │
      ↓                         │
Countermeasures                 │
                                │
Independent verification ◀─────┘
      ↓
Routing / re-analysis gate
      ↓
Validated training answer key
      ↓
Learner attempt / calibration / transfer
```

`assertions[]` cuts across every layer. It is the provenance-bearing graph of what each specialist claims about another object. `sources[]` and `evidence[]` support or contradict assertions without duplicating specialist records.

## Why one object rather than prose merging?

A prose merger cannot reliably distinguish "authority cue observed" from "authority mechanism supported" from "this person trusted the authority". The common schema can represent all three separately and force downstream code to inspect the exact status.
