# Offline pipeline architecture spec

## Pipeline

```text
normalized_trace_schema_v1 CSVs
  -> trace manifest
  -> content ladder / segment-size fixture
  -> deterministic replay environment
  -> teacher policy replay
  -> supervised samples JSONL
  -> train-only normalization statistics
  -> NeuralABR-Lite model training smoke
  -> offline sanity validation report
```

## Boundary

The pipeline is an offline scientific artifact. It must not be used as a player, controller registry entry, benchmark runner, or runtime component.

## Required architectural properties

| Property | Requirement |
|---|---|
| Determinism | Same seed + same manifest must produce same samples and model-smoke metrics. |
| Trace-level split | Never split segments from the same trace across train/validation/OOD. |
| Train-only normalization | Fit statistics only on train samples. Apply to validation/OOD. |
| Action validity | Model output is scored only over valid representations. |
| Leakage prevention | No future throughput, teacher action, reward, split, trace id, OOD label or benchmark result as model input. |
| CPU-first | No CUDA/ROCm/DirectML/WSL requirement. |
| Artifact hygiene | Datasets, runs, checkpoints and logs outside the repo. |

## Minimal implementation dependency policy

Use Python standard library plus PyTorch CPU for model/training. Do not introduce Ray/RLlib, TensorFlow 1.x, Stable-Baselines, gymnasium, pandas, scikit-learn or heavyweight dependencies in Phase 4D.
