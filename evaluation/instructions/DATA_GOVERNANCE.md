# Gold governance and anti-leakage

The ZIP contains private answer candidates and design manifests so the evaluator custodian can adjudicate them. **Do not upload this entire ZIP to a public or client-delivered app repository.** Separate privileged evaluation service and benchmark vault are prerequisites.

- Public model input: public passage/test instruction, authorized closed-world packet only when scenario requires it, no gold constraint, no privileged design manifest.
- Annotator B: blinding to Annotator A labels and model outputs. Another prompt by the same model/instance is not automatically an independent annotation.
- Adjudicator C: independently reconcile A/B disagreements; freeze accepted answers and ambiguity policy.
- Locked test: versioned hash, separate access control, release attestation; never used for prompt development or training.
- Failed holdout: treat as spent for future tuning. Build fresh families from new provenance before claiming improvement.
- Authentic real-world data: verify provenance and permissions, redact personal/sensitive information, limit retention, ban model training use absent authorization.
- Commercial restrictions: review every upstream dataset. AVeriTeC is noncommercial by default.
- Reliability: compute per-layer agreement; consider multiple legitimate answers. Human-rater agreement and machine accuracy are distinct metrics.
- Label conflicts: do not force false precision; classify as adjudication pending until resolved.
- Model changes: any model, prompt, adapter, label mapping, dependency or schema version change resets the release gate.
