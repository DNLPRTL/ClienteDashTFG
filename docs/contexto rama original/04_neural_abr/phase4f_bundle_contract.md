# Phase 4F bundle contract

The NeuralABR-Lite bundle is a local-only artifact stored outside the repository.

Required bundle files:

```text
bundle_manifest.json
model_card.json
feature_schema.json
normalization_stats.json
ladder_schema.json
inference_contract.json
fallback_policy.json
model_state.pt
```

Optional diagnostic files:

```text
export_log.json
bundle_validation_report.json
inference_latency_report.json
sample_inference_report.json
```

Required manifest fields:

- phase: `phase4f`;
- source_phase: `phase4e2`;
- model_family: `NeuralABR-Lite Candidate Scorer`;
- training_method: `behavior_cloning` / `imitation_learning`;
- teacher: `robust_mpc` unless explicitly documented otherwise;
- action_space: `representation_index`;
- reward_context: `qoe_linear_v1 / reward_n`;
- model_file;
- feature_schema_file;
- normalization_stats_file;
- fallback_policy_file;
- created_at_utc;
- source_run_dir;
- source_dataset_dir;
- source_validation_dir;
- sha256 hashes for bundle files.

Repository rule: no `.pt`, `.pth`, `.onnx`, `.npy`, `.npz`, `.pkl`, `.joblib`, generated `.csv`, logs, checkpoints or datasets may be committed.
