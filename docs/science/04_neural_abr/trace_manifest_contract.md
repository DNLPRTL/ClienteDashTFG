# Trace manifest contract

## Purpose

Trace manifests are the canonical record of what traces exist, where they came from, how they were converted, and how they are assigned to train/validation/OOD.

## Required top-level fields

```json
{
  "manifest_version": "phase4c_trace_manifest_v1",
  "dataset_id": "...",
  "created_at_utc": "...",
  "source": {
    "name": "...",
    "url_or_citation": "...",
    "license_note": "..."
  },
  "conversion": {
    "tool": "...",
    "tool_version": "...",
    "unit_mapping": {},
    "missing_value_policy": "..."
  },
  "traces": [],
  "split_policy": {},
  "artifact_policy": {
    "repo_safe": false,
    "local_only": true
  }
}
```

## Per-trace metadata

```json
{
  "trace_id": "...",
  "path": "converted/<trace_id>.csv",
  "duration_s": 0.0,
  "samples": 0,
  "throughput_bps_mean": 0.0,
  "throughput_bps_p05": 0.0,
  "throughput_bps_p95": 0.0,
  "throughput_cv": 0.0,
  "network_regime_label": "unknown",
  "split": "train|validation|ood_diagnostic|unassigned",
  "diagnostic_only": false
}
```

## Split immutability

Once a manifest is used for model training, split assignments must not be changed without a new manifest version and a documented reason.

## Trace-level split

Splits must be by trace/session, never by random segment rows from the same trace.
