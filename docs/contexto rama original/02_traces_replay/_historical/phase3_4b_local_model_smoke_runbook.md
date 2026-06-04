# Phase 3.4B Local Model Smoke Runbook

This smoke runbook checks the trace-driven network model using local normalized traces. It does not run controllers and does not create benchmark results.

## Inputs

Use normalized CSVs produced outside the repository by Phase 3.4A, for example under:

```text
C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_normalized\schema_v1\phase3_4a_smoke
```

Do not copy normalized real CSVs or generated manifests into the repository.

## Minimal Interactive Smoke

From the repository root, a local manual smoke can load one external normalized CSV and estimate one segment download:

```text
python -c "from core.trace_replay.loader import load_normalized_trace_csv; from core.trace_replay.network_model import TraceDrivenNetworkModel; t=load_normalized_trace_csv(r'<external-normalized-csv>'); m=TraceDrivenNetworkModel(t); print(m.download(250000))"
```

Expected behavior:

- a `SegmentDownloadResult` is printed if the trace can deliver the requested bytes;
- `TraceReplayError` is raised if the trace exhausts under `END_POLICY_FAIL`;
- no files are written.

## Repository Hygiene

After a smoke:

```text
git status --short
```

No real normalized CSV, manifest, log, ZIP, media file, run directory, `__pycache__` or `.pyc` should be added to the repository.

## Non-Goals

This smoke does not run a replay runner, player, controller, Mahimahi, `tc/netem`, QoE/reward calculation, benchmark ranking or IA/RL training.
