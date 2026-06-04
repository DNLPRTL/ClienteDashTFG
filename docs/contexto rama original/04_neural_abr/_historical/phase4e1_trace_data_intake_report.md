# Phase 4E.1 Trace Data Intake Report

Current status before Phase 4E.1:

- Phase 4D offline pipeline implementation is already committed as `109ced8 feat(neural-abr): add Phase 4 method docs and offline pipeline`.
- Phase 4E synthetic smoke is already committed as `37c71c5 test(neural-abr): validate Phase 4E offline training smoke`.
- The synthetic smoke passed dataset build, dataset validation, CPU training smoke, offline validation, 381 unit tests, and strict client readiness.
- The synthetic smoke model predicted only representation 3, so it is not an offline candidate for Phase 4F.
- Therefore the next block is Phase 4E.1: documented external trace intake and external-trace smoke, not Phase 4F.

## Purpose

Phase 4E.1 bridges the synthetic NeuralABR-Lite smoke and the first external-trace smoke.
It does not open Phase 4F yet.

The goal is to take the Phase 3 normalized trace work, stage it safely for Phase 4, and make Codex implement or verify external trace ingestion in the offline training pipeline.

## Why Phase 4F is not allowed yet

Phase 4F requires an exportable offline candidate. The current synthetic Tier 0 smoke only proves the machinery works. It is not an external-trace model, and it collapsed to a single representation in the smoke model. That is acceptable for Tier 0 but not sufficient for an export/inference contract.

## PowerShell issue diagnosis

The observed `NativeCommandError` in `phase4e_run_synthetic_smoke_windows.ps1` happens at the wrapper level when `cmd /c ... 2>&1 | Tee-Object` captures output from `python -m unittest discover`. Python unittest writes progress dots to stderr in some environments; with `$ErrorActionPreference = "Stop"`, Windows PowerShell can surface that as a native command error record even when later validation proves the repo is clean.

The fix is to replace the local smoke wrapper with a version that temporarily relaxes `$ErrorActionPreference` inside the logging helper, captures `$LASTEXITCODE`, and throws only on non-zero exit code.

## Phase 3 dataset context

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

## Phase 3.5 reward context

Phase 3.5 QoE/reward material inspected from the uploaded `03_qoe_reward.zip`:

- Primary formula: `qoe_linear_v1`.
- Primary session metric: `qoe_linear_mean`.
- Segment reward candidate for IA: `reward_n = q_n - 4.3 * rebuffer_s_n - smoothness_n`.
- `q_n = bitrate_kbps_n / 1000.0`.
- `smoothness_n = 0.0` for the first segment, otherwise the absolute Mbps utility delta.
- Startup remains report-only.
- VMAF remains deferred.
- Evaluation gates remain `use_for_eval`, `diagnostic_only`, and `do_not_use_for_eval`.
- Dry-runs and smokes are not formal benchmarks and are not training datasets.

## Decision

Proceed to Phase 4E.1 external trace intake and external-trace smoke.

Do not proceed to Phase 4F until an external-trace model passes the Phase 4E candidate gates.

## Markers

- PHASE4E1_STATUS: ready_for_external_trace_intake
- PHASE4E_SYNTHETIC_TIER0: pass_not_candidate
- PHASE4F_ALLOWED: false
- DRY_RUNS_AS_TRAINING_DATA: forbidden
