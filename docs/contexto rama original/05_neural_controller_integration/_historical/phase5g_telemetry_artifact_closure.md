# Phase 5G telemetry and artifact closure

## Segment telemetry

`segment_telemetry.csv` may contain diagnostic NeuralABR-Lite fields when `neural_abr_lite` is selected.

The expected field family is:

```text
feedback_neural_*
```

These fields describe loader state, feature-vector status, action-mask count, raw/safe action, fallback state, inference timing, non-finite score detection, invalid-action detection, and diagnostic-only status.

## Evaluation telemetry

`evaluation_segments.csv` must not contain neural diagnostic fields.

Neural diagnostics are not evaluation rows, scoring fields, QoE metrics, benchmark evidence, ranking fields, or retraining labels.

## Canonical run artifacts

Canonical runtime artifacts remain:

- `run_manifest.json`
- `config.resolved.json`
- `environment.json`
- `run.log`
- `segment_telemetry.csv`
- `evaluation_segments.csv`

These are runtime outputs and stay outside Git unless explicitly handled by a separate artifact policy. Phase 5G commits no run outputs.

## Forbidden telemetry contamination

Phase 5 closure preserves the absence of:

- benchmark fields;
- ranking fields;
- winner fields;
- improvement fields;
- p-value fields;
- neural diagnostic fields in `evaluation_segments.csv`.

## Artifact boundary

The real bundle remains a local artifact outside the repository. No `.pt`, `.pth`, `.onnx`, `.pkl`, `.joblib`, `.npz`, `.npy`, CSV, log, dataset, zip, PDF, media, or run-output artifact is part of the Phase 5G commit.

## Boundary

Telemetry is diagnostic-only structural integration evidence. It is not a benchmark result.
