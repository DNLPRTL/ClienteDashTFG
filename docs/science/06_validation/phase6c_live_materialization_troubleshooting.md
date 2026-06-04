# Phase 6C Live Materialization Troubleshooting

Status: Phase 6C-H1 operational guidance. No benchmark authorization.

Phase 6C download and extraction can pass while normalization still has substantial file discovery and parsing work. A stall or interrupt during normalization does not mean the user should manually create configs, manifests or code patches.

## First Retry

Use the safe primary-source command:

```powershell
python -u scripts\run_phase6c_trace_materialization.py ^
  --external-root C:\Users\danie\Documents\TFG\_datasets\phase6_validation ^
  --phase4-dataset-manifest C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E2_expanded_candidate_20260529_080755\dataset_manifest.json ^
  --sources primary ^
  --download ^
  --extract ^
  --normalize ^
  --build-reference ^
  --build-candidate ^
  --validate ^
  --audit ^
  --freeze ^
  --strict ^
  --resume ^
  --skip-existing ^
  --clean-derived ^
  --progress-every 10
```

`primary` means Raca 4G LTE and Raca 5G only. Lumos5G is optional; Ghent and HSDPA are diagnostic unless explicitly selected; Lancaster remains excluded.

## What To Inspect

- `logs/phase6c_normalize.log`: live child output captured per step.
- `reports/phase6c_normalization_progress.json`: selected sources, current source and counts.
- `reports/phase6c_normalization_report.json`: normalized and excluded records.
- `receipts/phase6c_download_receipts.json`: downloaded or skipped-existing source files.
- `receipts/phase6c_extract_receipts.json`: extracted or skipped-existing archives.

The orchestrator keeps only a bounded stdout tail in `phase6c_materialization_summary.json`; the full step output is in the per-step log.

## Controls

- `--step-timeout-s`: timeout for non-normalization child steps.
- `--normalize-timeout-s`: timeout for normalization.
- `--max-files-per-source`: cap candidate files per selected source.
- `--max-file-size-mb`: skip oversized candidate files.
- `--max-sniff-bytes`: bound delimiter/header sniffing.
- `--progress-every`: print and persist progress more often.
- `--skip-existing`: reuse existing downloads/extractions/derived reports when safe.
- `--clean-derived`: rebuild selected-source normalized outputs and current-run manifests/reports.

Do not delete downloaded archives for a normalization retry unless intentionally reacquiring sources. Do not manually edit the frozen manifest.

## Boundary

Troubleshooting live materialization still does not run dry-runs, controllers, QoE, plots, rankings or benchmarks. `ready_for_benchmark=false` and `benchmark_authorized=false` remain mandatory.
