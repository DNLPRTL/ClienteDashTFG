# Phase 4E.1 Phase 3 Trace Reuse Decision

## Decision

Use Phase 3 normalized trace CSVs as external trace smoke input for Phase 4E.1, subject to strict constraints.

## Allowed input

Allowed:

```text
C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_normalized\schema_v1\phase3_4a_smoke\**\*.csv
C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_manifests\phase3_4a_conversion_smoke\**\*.json
```

The Phase 4 workspace will stage copies under:

```text
C:\Users\danie\Documents\TFG\_datasets\phase4_AI\external_trace_intake\phase3_4a_smoke
```

## Forbidden input

Forbidden:

```text
_runs\phase3_4c_dry_run_smoke
controlled QoE smokes
legacy dry-run outputs
benchmark outputs
controller ranking artifacts
raw candidate datasets as direct training samples
```

Raw sources remain useful for provenance only. Training must consume normalized traces or documented conversions.

## Why this is safe enough for a smoke, not a final dataset

This is only a small conversion-smoke subset. It is strong enough to validate external trace ingestion and trace-level splitting. It is not enough to make final scientific claims about superiority.

## Visible normalized subset

Phase 3 trace material inspected from the uploaded `_datasets.zip`:

- Local root represented by the ZIP: `_datasets/phase3_traces_replay/`.
- Raw candidates exist outside the repo and must remain outside the repo.
- Normalized trace subset exists under `_normalized/schema_v1/phase3_4a_smoke/`.
- Manifests exist under `_manifests/phase3_4a_conversion_smoke/`.
- Converted smoke subset currently visible:
  - `hsdpa_norway_mmsys2013`: 5 normalized CSV traces, 4170 rows, roughly low/mobile throughput.
  - `ghent_4g_lte_bandwidth_logs`: 5 normalized CSV traces, 3100 rows, LTE/4G mobile traces.
  - `lancaster_abr_throughput_traces`: 5 normalized CSV traces, 150 rows, HAS/CDN-like throughput traces.
- The normalized CSV schema uses `timestamp_s`, `duration_s`, and `throughput_kbps` as required columns.
- Manifests include `trace_id`, `dataset_id`, `leakage_group`, throughput stats, mobility/network tags and path policy.
- `_runs/phase3_4c_dry_run_smoke` exists but is diagnostic-only and must not be used as training data.

## Required Phase 4E.1 handling

- Split at trace level, never row level.
- Use `leakage_group` from manifests when available.
- Fit normalization on train only.
- Keep OOD diagnostic out of tuning.
- Preserve `dataset_id`, `trace_id`, `leakage_group`, and source provenance in the generated dataset manifest.
- Mark all external-trace smoke outputs as `diagnostic_only`.

## Markers

- PHASE4E1_TRACE_REUSE: phase3_normalized_schema_v1_only
- PHASE4E1_DRY_RUN_REUSE: forbidden
- PHASE4E1_FINAL_TRAINING_DATASET: false
