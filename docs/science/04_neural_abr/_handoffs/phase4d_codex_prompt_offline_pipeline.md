# Codex prompt â€” Phase 4D offline training pipeline implementation

You are implementing Phase 4D of DashClientModular4: the offline NeuralABR-Lite training pipeline.

## NON-NEGOTIABLE CONTEXT

The repository is a Python DASH client project. Previous phases implemented classical ABR controllers, trace replay, QoE calculation and Phase 4 scientific documentation.

The selected method is:

```text
NeuralABR-Lite Candidate Scorer
  small CPU-first neural ABR
  behavior cloning / imitation learning
  score per valid representation candidate
  action = representation_index inside the MPD ladder
  reward = qoe_linear_v1 / reward_n
  teacher = robust_mpc primary, mpc secondary, bounded oracle diagnostic-only
  safety = action mask + fallback policy
```

This choice is based on the Phase 4 source cards/evidence matrix and must not be replaced by PPO, full meta-RL, offline RL, AIRL, MoE, transformer or any large model.

## READ THESE DOCUMENTS FIRST

Before editing code, inspect and follow:

```text
docs/science/04_neural_abr/_historical/phase4a2_method_decision_report.md
docs/science/04_neural_abr/neural_abr_lite_candidate_scorer_decision.md
docs/science/04_neural_abr/_historical/phase4b_contracts_report.md
docs/science/04_neural_abr/state_representation.md
docs/science/04_neural_abr/action_space_decision.md
docs/science/04_neural_abr/reward_usage_contract.md
docs/science/04_neural_abr/training_data_contract.md
docs/science/04_neural_abr/leakage_prevention_for_ia.md
docs/science/04_neural_abr/_historical/phase4c_training_environment_report.md
docs/science/04_neural_abr/training_environment_spec.md
docs/science/04_neural_abr/simulator_vs_client_boundary.md
docs/science/04_neural_abr/dataset_builder_contract.md
docs/science/04_neural_abr/offline_validation_protocol.md
docs/science/04_neural_abr/_historical/phase4d_offline_pipeline_specs_report.md
docs/science/04_neural_abr/offline_pipeline_architecture_spec.md
docs/science/04_neural_abr/_historical/neural_abr_lite_module_plan.md
docs/science/04_neural_abr/tests_acceptance_phase4d.md
docs/science/04_neural_abr/memory_defense_traceability_phase4d.md
```

## FORBIDDEN

Do not do any of the following:

```text
Do not register a neural ABR controller.
Do not touch player/runtime/media integration.
Do not modify core/controller/ classical controllers except by reading them.
Do not modify main.py/player.py/downloader/media_engine.
Do not run or create a benchmark/ranking.
Do not use legacy dry-runs as training data.
Do not create datasets/checkpoints/logs inside the repo.
Do not introduce Ray/RLlib, Stable-Baselines, TensorFlow, gymnasium, pandas, scikit-learn, CUDA, ROCm, DirectML or WSL requirements.
Do not choose PPO or RL-first.
Do not add VMAF, learned reward, AIRL, transformer, MoE or large models.
Do not make SOTA or real-world claims.
```

## ALLOWED FILE CHANGES

You may create/edit only these categories:

```text
core/neural_abr/*.py
scripts/build_neural_abr_dataset.py
scripts/validate_neural_abr_dataset.py
scripts/train_neural_abr.py
scripts/validate_neural_abr_offline.py
tests/test_neural_abr_*.py
docs/science/04_neural_abr/_historical/phase4d_implementation_report.md
docs/science/04_neural_abr/phase4d_code_traceability_matrix.md
docs/science/04_neural_abr/_historical/phase4d_test_report.md
docs/science/04_neural_abr/_historical/phase4d_defense_talking_points.md
docs/science/04_neural_abr/_historical/phase4d_open_limitations.md
```

If you believe another file must change, stop and explain why instead of editing it.

## REQUIRED IMPLEMENTATION

Create the package:

```text
core/neural_abr/
  __init__.py
  constants.py
  schemas.py
  trace_source.py
  content_ladder.py
  replay_env.py
  features.py
  action_mask.py
  teacher_policy.py
  dataset_builder.py
  normalization.py
  model.py
  training.py
  validation.py
  artifacts.py
```

Required scripts:

```text
scripts/build_neural_abr_dataset.py
scripts/validate_neural_abr_dataset.py
scripts/train_neural_abr.py
scripts/validate_neural_abr_offline.py
```

Required tests:

```text
tests/test_neural_abr_schema.py
tests/test_neural_abr_action_mask.py
tests/test_neural_abr_features.py
tests/test_neural_abr_replay_env.py
tests/test_neural_abr_teacher_policy.py
tests/test_neural_abr_dataset_builder.py
tests/test_neural_abr_normalization.py
tests/test_neural_abr_model.py
tests/test_neural_abr_cli_smoke.py
```

## IMPLEMENTATION DETAILS

### Trace handling

Reuse existing Phase 3 trace modules:

```text
core.trace_replay.loader
core.trace_replay.schema
core.trace_replay.validation
core.trace_replay.network_model
```

Do not invent another raw trace schema. Consume `normalized_trace_schema_v1`.

### Replay environment

Implement deterministic replay for segment decisions:

```text
download_time_s = trace network model download duration
rebuffer_s = max(download_time_s - buffer_s, 0)
buffer_s = max(buffer_s - download_time_s, 0) + segment_duration_s
buffer_s = min(buffer_s, max_buffer_s)
```

### Features

`K_CONTEXT = 5`.

Context features:

```text
throughput_history_bps[5]
download_time_history_s[5]
buffer_s
last_representation_index
last_bitrate_bps
recent_rebuffer_s
recent_switch_abs
chunks_remaining_norm
has_chunks_remaining
```

Candidate features:

```text
candidate_representation_index
candidate_ladder_position_norm
candidate_bitrate_bps
candidate_bitrate_norm_ladder
candidate_delta_from_last_bitrate_norm
candidate_chunk_size_bytes
candidate_chunk_size_available
```

Reject or never include forbidden model inputs:

```text
future throughput
future download time
teacher_action as input
teacher_reward as input
split as input
trace_id as input
source_dataset as numeric input
regime label as numeric input
benchmark result
```

### Action mask

All model decisions and teacher labels must satisfy:

```text
0 <= representation_index < representation_count
action_mask[representation_index] == true
```

### Dataset builder

Implement synthetic smoke mode:

```text
python scripts/build_neural_abr_dataset.py --synthetic-smoke --output-dir <dir> --overwrite
```

Output outside repo:

```text
dataset_manifest.json
train.jsonl
validation.jsonl
ood_diagnostic.jsonl
feature_schema.json
label_schema.json
leakage_audit.json
```

Synthetic smoke is diagnostic-only and not a benchmark.

### Normalization

Fit statistics on train only. Applying validation/OOD samples during fit must fail.

### Model

Implement a small shared MLP candidate scorer:

```text
score_r = MLP(concat(normalized_context, normalized_candidate_features_r))
masked_scores = score_r over valid candidates only
loss = cross_entropy(masked_scores, teacher_action)
```

Default device: CPU.

### CLIs

Required CLI behavior:

```text
python scripts/validate_neural_abr_dataset.py --dataset-dir <dir>
python scripts/train_neural_abr.py --dataset-dir <dir> --output-dir <run_dir> --epochs 1 --batch-size 8 --seed 123 --device cpu --smoke
python scripts/validate_neural_abr_offline.py --dataset-dir <dir> --run-dir <run_dir> --output-dir <validation_dir>
```

Each CLI must print a summary and write a JSON report.

## MEMORY AND DEFENSE

After implementing code, create/update:

```text
docs/science/04_neural_abr/_historical/phase4d_implementation_report.md
docs/science/04_neural_abr/phase4d_code_traceability_matrix.md
docs/science/04_neural_abr/_historical/phase4d_test_report.md
docs/science/04_neural_abr/_historical/phase4d_defense_talking_points.md
docs/science/04_neural_abr/_historical/phase4d_open_limitations.md
```

The implementation report must explain:

```text
what was implemented;
why it follows the papers and method decision;
how traces become supervised samples;
how teacher labels are produced;
how leakage is prevented;
how action masking works;
how train-only normalization is enforced;
how CPU-first reproducibility is enforced;
why this is not benchmark/ranking;
why client integration is still blocked.
```

The traceability matrix must include:

```text
implemented_file | implemented_symbol | contract_source | paper_decision_source | purpose | leakage_gate | test_file | memory_section
```

## ACCEPTANCE COMMANDS

Run these commands before finishing:

```powershell
python -m unittest discover
python scripts/check_client_readiness.py --strict
```

Also run the local synthetic smoke. Use local-only directories outside the repo:

```powershell
$DatasetDir = "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4D_synthetic_smoke"
$RunDir = "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4D\smoke"
$ValidationDir = "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4D\validation"

python scripts/build_neural_abr_dataset.py --synthetic-smoke --output-dir $DatasetDir --overwrite
python scripts/validate_neural_abr_dataset.py --dataset-dir $DatasetDir
python scripts/train_neural_abr.py --dataset-dir $DatasetDir --output-dir $RunDir --epochs 1 --batch-size 8 --seed 123 --device cpu --smoke
python scripts/validate_neural_abr_offline.py --dataset-dir $DatasetDir --run-dir $RunDir --output-dir $ValidationDir
python -m unittest discover
python scripts/check_client_readiness.py --strict
```

## FINAL RESPONSE REQUIREMENTS

When done, report:

```text
files created/changed;
commands run;
test results;
readiness result;
local artifact paths;
limitations;
whether Phase 4D is PASS, PARTIAL or FAIL.
```

Do not claim that the model is final. Do not claim benchmark superiority. Do not claim real-world validation. Do not say Phase 5 integration is allowed.

