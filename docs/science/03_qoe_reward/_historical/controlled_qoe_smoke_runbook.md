# Controlled QoE Smoke Runbook

Phase 3.5D validates the QoE artifact path with controlled synthetic inputs:

`synthetic dry-run-like artifacts -> QoE post-processor -> QoE artifacts -> smoke report`

The runbook does not execute real dry-runs, does not modify the dry-run runner, does not compare controllers and does not create benchmark evidence.

## Objective

The smoke runner creates four deterministic dry-run-like scenarios outside the repository, invokes the Phase 3.5C post-processor through its Python API and checks that:

- `qoe_run_summary.json`, `qoe_segment_rewards.csv` and `qoe_artifact_manifest.json` are written for each scenario;
- `outputs_are_benchmark_results=false` remains true for every QoE artifact;
- `no_final_ranking=true` remains true for every QoE artifact;
- legacy, incomplete or source-conflicting inputs are gated as `do_not_use_for_eval`;
- no scenario is ordered or summarized as a controller ranking.

## Recommended External Path

Use a path outside Git:

```powershell
$smokeRoot = "C:\Users\danie\Documents\TFG\_runs\phase3.5D_qoe_smoke"
```

The script rejects output roots inside the repository.

## Windows Command

```powershell
$smokeRoot = "C:\Users\danie\Documents\TFG\_runs\phase3.5D_qoe_smoke"
python scripts\run_qoe_smoke_scenarios.py --output-root $smokeRoot --overwrite
```

Expected console markers:

```text
all_checks_passed=true
outputs_are_benchmark_results=false
no_final_ranking=true
ranking_performed=false
benchmark_performed=false
```

## Ubuntu Command

```bash
smoke_root="$HOME/TFG/_runs/phase3.5D_qoe_smoke"
python scripts/run_qoe_smoke_scenarios.py --output-root "$smoke_root" --overwrite
```

## Expected Outputs

Top-level output:

- `qoe_smoke_report.json`

Per scenario:

- `source_dry_run/trace_dry_run_segments.csv`
- `source_dry_run/trace_dry_run_summary.json`
- `source_dry_run/trace_dry_run_manifest.json`
- `qoe_outputs/qoe_segment_rewards.csv`
- `qoe_outputs/qoe_run_summary.json`
- `qoe_outputs/qoe_artifact_manifest.json`

All outputs are generated outside the repository and must not be versioned.

## Reading qoe_smoke_report.json

The report is a validation artifact, not a result table. Read it by scenario name:

- `complete_use_for_eval` checks the happy path and expects `qoe_linear_sum=2.0`;
- `legacy_do_not_use_for_eval` checks legacy gates;
- `incomplete_session` checks the incomplete-session gate;
- `source_claims_benchmark` checks that source benchmark claims are not propagated.

Scenario order is fixed and is not a score ordering.

## Why This Is Not A Benchmark

The inputs are synthetic, use one synthetic controller name and do not come from real trace dry-runs. The script performs no aggregation across controllers, no statistical comparison and no winner selection. Its purpose is schema and gate validation only.

## Why This Is Not Ranking

The runner never sorts scenarios by QoE, never names a best controller and never compares real controllers. It checks that the no-ranking boundary survives artifact computation.

## Validation markers

- PHASE_3_5D_SMOKE_RUNS: controlled_external_artifacts_only
- PHASE_3_5D_NO_RANKING: true
- PHASE_3_5D_NO_BENCHMARK: true
- PHASE_3_5D_NO_IA: true
