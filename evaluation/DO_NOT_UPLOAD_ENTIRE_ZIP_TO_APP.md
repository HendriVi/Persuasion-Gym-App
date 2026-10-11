# Security boundary — read before importing

The **full ZIP is an evaluator-custodian bundle**, not a frontend/runtime distribution. It contains candidate gold answers in `benchmarks/internal/**/private` and source context to resolve them. Do not commit or upload the complete archive to frontend code, published GitHub repositories, static assets, model context or user-accessible server paths.

Copy **only** `scripts/` controller code, `config/release.json`, approved runtime schemas and public-case adapters into a private evaluation service. Keep actual gold and adjudication records in a separate restricted vault. Public UI should receive only graded output summaries and non-sensitive explanations.

Before any production activation: independently adjudicate gold, run frozen fivefold eval, check the gate and obtain authorized human signoff for the exact deployment hash.
