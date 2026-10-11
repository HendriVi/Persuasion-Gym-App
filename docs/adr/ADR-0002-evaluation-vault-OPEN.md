# ADR-0002 — independent evaluation vault and annotation roles, OPEN

Date: 2026-10-11. Status: **OPEN — security architecture and human signoff required**.

## Source contracts

`EVALUATION.md`, `CODEX.md`, `evaluation/instructions/DATA_GOVERNANCE.md`, `evaluation/instructions/RELEASE_POLICY.md`, `evaluation/config/release.json`, and `DECISIONS.md` D-015, D-017–D-024, D-032. Gold candidates are not gold. Do not bring the offline restricted archive into the public repository, this project's LLM context, app prompt, public GitHub Actions cache/artifacts, log stream, or client bundle.

## Candidate approaches (undecided)

A. Encrypted offline evaluator workstation with physically/logically separate source archive, signed local output and trusted custodians. Suitable initial low-volume human annotation; limited auditable shared access and operational resilience.

B. Private encrypted cloud object store + isolated evaluator service, per-role access, short-lived credentials and independent human B/C reviewers. Suitable for scaling when access, region, vendor terms and operational security are approved; increases cost, configuration and audit burden.

C. A separate private organization repository for controller code and metadata *only*, with encrypted storage for private payloads outside repository history. Better version control than a shared filesystem but repository-private status alone does **not** constitute sufficient role separation.

No selection is approved. A GitHub public repo and its CI are **not** a permitted vault.

## Required roles and restrictions

- Original annotator A produces initial candidate assessment; independently blinded annotator B receives only necessary case material, not A answers/model judgments/hidden-pair design; adjudicator C handles disagreement under documented independence and conflict policies.
- Evaluator operator configures hidden partitions, keyed access and immutable audit; app inference service sees no gold, signatures, confidential benchmark catalogs or grader internals.
- Prevent answer/model contamination in development, monitoring, search retrieval, imports, trace logs and downstream UI; pre-register versions and frozen holdout identities.
- Require license/rights review for each external dataset, redaction/minimization, backup/retention/deletion policy, key rotation, access review and incident recovery.
- Record one source for each verdict, admissible alternative answers, disagreements and lock/promotion authorization; treat manipulated/unadjudicated annotations as provisional.

## Release gates remain unchanged

At least 1,600 distinct `LOCKED_ADJUDICATED` cases, minimum 200 per each of eight competencies, 100 per six challenge slices, 150 per six designated cross-slices, 30 independent families per cell; five complete preregistered frozen runs; in each run all mandatory cells must meet Bonferroni-adjusted one-sided 95% Wilson lower bound >=0.95 (0.97 stretch), observed critical errors zero and ten-bin ECE <=0.05. Errors/missing/abstain count as wrong for strict primary metric. Original `evaluation/scripts/release_gate.py` controls this; source tests alone certify nothing.

## Required human decision and acceptance

Owner must approve vault method and operator custody, identify genuinely independent B/C reviewers, and approve retention/security boundaries. Acceptance requires a security design review, test proving app/service role cannot fetch hidden answers, blind annotation drill, audit and restore drill, and owner authorization for promotion. Until then `MODEL=NOT_EVALUATED; RELEASE=BLOCKED; MASTER_SKILL=GATED`.
