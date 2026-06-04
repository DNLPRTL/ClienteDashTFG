# Phase 6C Trace Manifest Freeze Contract

Status: Phase 6C freeze contract. The final manifest is external.

The final Phase 6 trace manifest is:

```text
<external_root>/manifests/phase6_trace_manifest_final.json
```

It is produced by automation only. The user should not manually write or edit it.

The recommended first live freeze attempt uses `--sources primary`, so only Raca 4G LTE and Raca 5G are materialized as primary OOD candidates. Lumos5G, Ghent and HSDPA are added only by explicit source selection flags. This keeps the first materialization small enough to audit and resume.

## Freeze Preconditions

`freeze_phase6_trace_manifest.py` freezes a candidate only when:

- `validate_phase6_trace_manifest.py --strict-final` reports `valid=true`;
- `audit_phase6_trace_eligibility.py` reports `use_for_phase6_eval=true`;
- candidate records are preserved without converting `diagnostic_only` records to `use_for_eval`.

Eligibility audit blocks overlap with Phase 4 by:

- `trace_id`
- `leakage_group`
- `checksum_sha256`
- `canonical_content_fingerprint`

## Freeze Metadata

The frozen manifest includes:

- `frozen_at`
- `frozen_by_script`
- `source_candidate_manifest`
- `source_validation_report`
- `source_eligibility_audit_report`
- `phase6c_freeze_only=true`
- `ready_for_benchmark=false`
- `benchmark_authorized=false`

Final trace IDs are frozen only after acquisition, extraction, normalization, candidate manifest build, validation, eligibility audit and freeze.

If materialization is interrupted before freeze, rerun the orchestrator with `--resume --skip-existing --clean-derived`. The automation rebuilds selected-source derived outputs and reports; the user should not manually create or edit candidate/final manifests.

## Dataset Gate Meaning

Raca 4G and Raca 5G are the primary OOD candidates.

Lumos5G is optional. If Google Drive blocks acquisition, the pipeline records the provider block and does not invent Lumos traces.

Ghent and HSDPA are same-family diagnostic by default.

Lancaster is excluded from primary Phase 6 evaluation and must not be frozen as `use_for_eval`.

## Non-Authorization

`phase6_trace_manifest_final.json` is a trace identity freeze artifact. It is not a benchmark run, not a result table, not a ranking, not a plot source and not a QoE improvement claim.
