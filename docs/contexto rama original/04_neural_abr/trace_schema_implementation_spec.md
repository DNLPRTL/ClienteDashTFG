# Trace schema implementation spec

## Reuse existing Phase 3 trace schema

Phase 4D must consume already-normalized Phase 3 traces:

```text
normalized_trace_schema_v1
required columns:
  timestamp_s
  duration_s
  throughput_kbps
```

Use existing modules when possible:

```text
core.trace_replay.loader
core.trace_replay.schema
core.trace_replay.validation
core.trace_replay.network_model
```

Do not create a competing raw-trace converter in Phase 4D.

## Trace manifest

A trace manifest must be JSON and must identify trace-level split membership:

```json
{
  "schema_version": "neural_abr_lite_trace_manifest_v1",
  "dataset_id": "phase4d_synthetic_sanity",
  "created_by": "Phase 4D offline pipeline",
  "traces": [
    {
      "trace_id": "synthetic_train_001",
      "path": ".../synthetic_train_001.csv",
      "split": "train",
      "regime": "medium_stable",
      "source_dataset": "synthetic_sanity",
      "diagnostic_only": false
    }
  ]
}
```

## Split values

Allowed values:

```text
train
validation
ood_diagnostic
```

No `test` split is created in Phase 4D because formal benchmark/ranking is still blocked.
