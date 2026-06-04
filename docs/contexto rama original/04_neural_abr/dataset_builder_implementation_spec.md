# Dataset builder implementation spec

## Dataset output

A built dataset must be stored outside the repository, normally under:

```text
C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\samples
```

## Files

```text
dataset_manifest.json
train.jsonl
validation.jsonl
ood_diagnostic.jsonl
feature_schema.json
label_schema.json
leakage_audit.json
```

## Sample JSONL schema

```json
{
  "schema_version": "neural_abr_lite_sample_v1",
  "sample_id": "synthetic_train_001:0003",
  "trace_id": "synthetic_train_001",
  "split": "train",
  "segment_index": 3,
  "context_features": {"buffer_s": 4.0},
  "candidates": [
    {"representation_index": 0, "valid": true, "features": {"candidate_bitrate_bps": 300000}}
  ],
  "action_mask": [true, true, true, true],
  "teacher_action": 1,
  "teacher_name": "robust_mpc",
  "reward_n": 0.0,
  "metadata": {"regime": "medium_stable", "diagnostic_only": false}
}
```

## Synthetic smoke mode

Phase 4D must provide a synthetic smoke path so the pipeline can be tested without real datasets:

```text
scripts/build_neural_abr_dataset.py --synthetic-smoke --output-dir <local_dir> --overwrite
```

The synthetic smoke dataset is not a benchmark and must be marked as `diagnostic_only`.
