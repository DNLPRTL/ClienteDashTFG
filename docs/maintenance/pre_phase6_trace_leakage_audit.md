# Pre-Phase6 Trace Leakage Audit

Phase 6 must not start with trace leakage in the `neural_abr_lite` evaluation set.

## Rule

If a checksum was used in Phase 4 train, validation, or OOD, it must not enter Phase 6 evaluation splits for `neural_abr_lite`.

The guardrail also reports overlaps by `trace_id` and `leakage_group`, because those remain useful signals even though the Phase 4 issue was found by checksum.

## Script

Use:

```powershell
python scripts\audit_phase6_trace_eligibility.py `
  --phase4-dataset-manifest C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E2_expanded_candidate_20260529_080755\dataset_manifest.json `
  --phase6-candidate-manifest C:\path\to\phase6_candidate_manifest.json `
  --output C:\Users\danie\Documents\TFG\_audits\phase6_trace_eligibility.json
```

Optional strict shell behavior:

```powershell
python scripts\audit_phase6_trace_eligibility.py `
  --phase4-dataset-manifest C:\path\to\phase4_manifest.json `
  --phase6-candidate-manifest C:\path\to\phase6_candidate_manifest.json `
  --output C:\path\to\audit.json `
  --fail-on-block
```

## Output

The JSON output includes:

- `use_for_phase6_eval`
- `reasons`
- counts for Phase 4 and Phase 6 records
- overlaps by checksum, `trace_id`, and `leakage_group`
- internal duplicate groups inside each manifest
- `logs_all` versus specific-folder duplicate groups

## Interpretation

`use_for_phase6_eval = false` means the candidate manifest must not be used as the fair evaluation set for `neural_abr_lite` against baselines.

It does not mean historical data must be deleted. It means the data belongs only in a separate diagnostic or provenance context unless a later phase explicitly justifies a different use.

## Phase 5 Boundary

This audit does not reopen Phase 5. Phase 5 remains a structural integration and safety-hardening closure, not a performance claim.
