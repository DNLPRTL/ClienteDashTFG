# Phase 6B Preflight Contract

Status: Phase 6B readiness/audit code contract. No benchmark authorization.

Phase 6B adds structural gates that must pass before Phase 6C can materialize real datasets outside Git. It does not execute benchmark runs, dry-runs over real traces, QoE computation over real outputs, result aggregation, plots, rankings, winner declarations, retraining, or claims that `neural_abr_lite` improves QoE.

## Scripts

Phase 6B introduces:

- `scripts/validate_phase6_trace_manifest.py`
- `scripts/check_phase6_evaluation_readiness.py`

Phase 6B also hardens:

- `scripts/audit_phase6_trace_eligibility.py`

## Readiness Checks

`check_phase6_evaluation_readiness.py` verifies:

- required Phase 6 protocol documents exist;
- required readiness/audit scripts exist;
- controller registry contains the Phase 6 controller set;
- QoE modules and scripts are importable enough for readiness;
- no obvious generated artifacts exist under validation `results`, `plots` or `generated` directories;
- optional manifests pass strict schema validation and Phase 4 overlap audit.

When manifests are missing, the script reports `manifest_audit_not_run`. This is a warning unless `--require-manifests` is set.

## Manifest Checks

When manifests are provided, the preflight runs:

```powershell
python scripts\validate_phase6_trace_manifest.py --manifest <phase6> --output <json> --strict-final --fail-on-error
python scripts\audit_phase6_trace_eligibility.py --phase4-dataset-manifest <phase4> --phase6-candidate-manifest <phase6> --output <json>
```

The audit blocks Phase 6 evaluation overlap with Phase 4 by:

- `trace_id`;
- `leakage_group`;
- `checksum_sha256`;
- `canonical_content_fingerprint`.

Phase 6B closes the previous `canonical_content_fingerprint` audit gap. The checksum and fingerprint identities remain separate in reports.

## Ghent Rule

Ghent must use `logs_all` OR per-mobility folders, not both, unless records are deduplicated by checksum or canonical content fingerprint before split. The audit's Ghent duplicate grouping now prefers `canonical_content_fingerprint` when present and falls back to `checksum_sha256`.

## Lancaster Rule

Lancaster remains excluded from primary final evaluation unless a source note/card and eligibility audit authorize it. Without that evidence, Lancaster material can only remain excluded or `diagnostic_only`.

## Readiness Meaning

`ready_for_phase6c=true` means the repository-side structural gates are ready for the next materialization phase. It does not mean the benchmark is ready.

Phase 6B reports must always keep:

```json
{
  "ready_for_benchmark": false,
  "benchmark_authorized": false
}
```

The benchmark remains unauthorized until a later phase explicitly opens execution after external manifests and evidence are in place.
