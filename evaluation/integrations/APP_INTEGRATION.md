# Integrating this folder into the TanStack Start / Supabase / AI SDK app

## Directory and responsibility

1. Keep the full bundle in a secured backend/evaluation repository; do NOT copy `benchmarks/internal/**/private`, gold labels or adjudication artifacts into public assets, `src/`, npm distribution, frontend bundles or prompt context.
2. Place release-controller public code, `config/release.json`, the registry and example under an `evaluation/` folder in the backend repo. Put real locked gold and score records in an external access-controlled vault (`.private_evaluation` in CI example must be provisioned securely).
3. Build a server-side adapter that converts the app's staged analysis schema into standardized benchmark outputs with case ID and version stamps. Keep the canonical schema and normalized adapters versioned. Validate with Zod or JSON Schema.
4. Execute specialist owner stages in order; do not substitute the beta lexical cue detector for the full model. Keep Fact-Check independent. For all unverified/pending results keep current `training.scoringAllowed=false`.
5. Record raw model response and any abstentions for each case. Independent scorers or human auditors emit `judgments.jsonl`. Do not permit the model under test to write its own correctness fields.
6. Upload complete frozen run metadata; verify actual deployed model/prompt/pipeline commit hashes. Run `release_gate.py` in release CI on each candidate.
7. Production deployment checks signed `release_report.json` and an independent human/QA approval matching the *exact* production artifact hash; if mismatched, the validated feature flag remains disabled.
8. Evaluate source verification, correct rejection of invented citations, calibration, political mirrors, non-manipulative persuasion, intent overclaim and causal overclaim. Run ongoing periodic operational checks after launch.

## Suggested server contract (illustrative TypeScript)

```ts
// NEVER copy hidden gold or grade keys to the browser.
type Qualification = {
  release: 'PASS' | 'BLOCKED';
  model_fingerprint: string;
  locked_manifest_sha256: string;
  target_floor: number;
};

function canEnableValidatedStack(q: Qualification | null, deployedModel: string): boolean {
  return Boolean(q && q.release === 'PASS' && q.target_floor >= .95 &&
    q.model_fingerprint === deployedModel);
}
```

`canEnableValidatedStack` is ONLY illustrative; production must ALSO validate signature, timestamps, hash of the executable pipeline and human approval, and must disable itself when evidence expires.

## Cost/latency

A demanding 95% confidence floor across eight competences, several adversarial slices and five complete runs requires many thousands of independent scored outputs. Do not reduce statistical tests just to make the release cheaper; budget evaluations separately and use smaller development sets before spending on locked release candidates.
