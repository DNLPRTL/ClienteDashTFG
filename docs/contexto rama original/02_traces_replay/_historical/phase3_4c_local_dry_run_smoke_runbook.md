# Phase 3.4C Local Dry-Run Smoke Runbook

This runbook is for local smoke execution against already-normalized CSVs. Outputs must stay outside the repository.

## Input Location

Use normalized smoke CSVs under:

```text
C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_normalized\schema_v1\phase3_4a_smoke
```

Do not copy normalized real CSVs into the repository.

## Output Location

Write dry-run outputs outside the repository, for example:

```text
C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_runs\phase3_4c_dry_run_smoke
C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_audit\phase3_4c_dry_run_smoke
```

Do not commit generated manifests, segment CSVs, summaries, logs, ZIPs, PDFs or media.

## Example Command

PowerShell example:

```powershell
python scripts/run_trace_dry_run.py `
  --trace-csv "C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_normalized\schema_v1\phase3_4a_smoke\example.csv" `
  --controller min_rate `
  --output-dir "C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_runs\phase3_4c_dry_run_smoke\example_min_rate" `
  --segment-count 8 `
  --segment-duration-s 2.0 `
  --representation-kbps 300,750,1200,1850,2850 `
  --end-policy loop `
  --max-loops 3 `
  --overwrite
```

## Expected Files

The output directory should contain exactly the dry-run artifact set:

- `trace_dry_run_manifest.json`;
- `trace_dry_run_segments.csv`;
- `trace_dry_run_summary.json`.

Each file must state:

- `phase = phase3_4c_dry_run`;
- `outputs_are_benchmark_results = false`;
- `final_qoe_reward_defined = false`;
- `row_eval_gate = do_not_use_for_eval`;
- `no_final_ranking = true`.

## Interpretation

This smoke confirms that normalized traces, the trace-driven network model, the fake replay adapter and existing controller contract can work together in a controlled loop.

It must not be used for final QoE/reward, controller ranking, parameter tuning, IA/RL training or performance claims.
