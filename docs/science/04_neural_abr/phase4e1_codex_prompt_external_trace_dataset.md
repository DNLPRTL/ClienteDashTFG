# Codex Prompt — Phase 4E.1 External Trace Dataset Smoke

You are working on DashClientModular4, branch `main`, after Phase 4E synthetic smoke.

Current expected HEAD after pull:

```text
37c71c5 test(neural-abr): validate Phase 4E offline training smoke
```

## Objective

Extend the existing offline NeuralABR-Lite pipeline so it can consume Phase 3 normalized external trace CSVs and run a small external-trace smoke.

This is still Phase 4E.1. It is not Phase 4F. Do not export a model for client integration.

## Read first

Read these docs before coding:

```text
docs/science/04_neural_abr/phase4e1_trace_data_intake_report.md
docs/science/04_neural_abr/phase4e1_phase3_trace_reuse_decision.md
docs/science/04_neural_abr/phase4e1_external_trace_split_plan.md
docs/science/04_neural_abr/phase4e1_qoe_reward_context_reconciliation.md
docs/science/04_neural_abr/phase4e1_acceptance_gates.md
docs/science/04_neural_abr/phase4e1_no_phase4f_yet.md
docs/science/04_neural_abr/training_data_contract.md
docs/science/04_neural_abr/trace_split_contract.md
docs/science/04_neural_abr/leakage_prevention_for_ia.md
docs/science/04_neural_abr/teacher_policy_contract.md
docs/science/04_neural_abr/phase4e_model_acceptance_gates.md
docs/science/03_qoe_reward/reward_definition.md
docs/science/03_qoe_reward/evaluation_gate_policy.md
```

If some Phase 3 docs are not present in the current repo, use the Phase 4E.1 docs as the local decision source.

## Allowed files

You may modify or create only:

```text
core/neural_abr/**
scripts/build_neural_abr_dataset.py
scripts/validate_neural_abr_dataset.py
scripts/train_neural_abr.py
scripts/validate_neural_abr_offline.py
tests/test_neural_abr_*.py
docs/science/04_neural_abr/phase4e1_*.md
```

## Forbidden files and actions

Do not modify:

```text
controllers/**
player.py
runtime/**
core/media_engine/**
main.py
media files
benchmark code
```

Do not:

- register a neural controller;
- integrate inference into the client;
- run benchmark/ranking;
- use dry-run outputs as training data;
- store datasets, checkpoints, logs or generated CSVs inside the repo;
- claim SOTA or real-world validity.

## Required implementation

### 1. External trace ingestion

Add support to `scripts/build_neural_abr_dataset.py` for:

```text
--trace-csv-root <path>
--trace-manifest-root <path>
--split-policy phase4e1_trace_level_regime_v1
--representation-kbps 300,750,1200,1850,2850
--segment-duration-s 4.0
--teacher robust_mpc
--seed 123
--diagnostic-only
--overwrite
```

Keep existing `--synthetic-smoke` behavior unchanged.

### 2. Input schema

Each external trace CSV must have at least:

```text
timestamp_s
duration_s
throughput_kbps
```

Optional columns must be preserved as metadata where useful:

```text
source_dataset
source_file
mobility_label
network_type
scenario_label
notes
```

### 3. Manifest use

If matching manifest JSON exists, preserve:

```text
trace_id
dataset_id
leakage_group
mean_throughput_kbps
min_throughput_kbps
max_throughput_kbps
sample_count
mobility_tags
network_tags
scenario_tags
source_url_or_reference
converter_name
converter_version_or_commit
checksum_sha256
```

If a manifest is missing, generate conservative metadata and set `manifest_missing=true`.

### 4. Split policy

Implement `phase4e1_trace_level_regime_v1`:

- split by `leakage_group` if present, otherwise `trace_id`;
- never split rows from the same trace into different splits;
- create `train`, `validation`, and `ood_diagnostic`;
- store split reason per trace;
- fit normalization on train only;
- mark OOD diagnostic as not for tuning.

For the current 15-trace Phase 3 smoke subset, a deterministic split is acceptable. Prefer balanced coverage across visible datasets, but do not overfit. The exact split must be written to the dataset manifest.

### 5. Teacher labels

Use the existing NeuralABR-Lite teacher/replay machinery. The primary teacher remains `robust_mpc`.

The representation ladder for Phase 4E.1 external trace smoke is fixed:

```text
300,750,1200,1850,2850 kbps
```

Segment duration:

```text
4.0 seconds
```

Generated samples must preserve action masks and must never contain labels outside the ladder.

### 6. Reports

Create or update:

```text
docs/science/04_neural_abr/phase4e1_external_trace_smoke_report.md
docs/science/04_neural_abr/phase4e1_dataset_manifest_summary.md
docs/science/04_neural_abr/phase4e1_external_trace_model_card.md
docs/science/04_neural_abr/phase4e1_external_trace_validation_report.md
docs/science/04_neural_abr/phase4e1_defense_talking_points.md
docs/science/04_neural_abr/phase4e1_open_limitations.md
docs/science/04_neural_abr/phase4e1_closure_report.md
```

Every report must state that this is diagnostic-only unless the gates explicitly pass.

### 7. Tests

Add or update unit tests for:

- external trace CSV loading;
- manifest matching;
- split by trace/leakage group;
- no row-level split leakage;
- train-only normalization;
- label/action-mask validity;
- missing manifest handling;
- CLI smoke using a temporary external trace fixture.

## Required commands to pass

```powershell
python -m unittest discover
python scripts\check_client_readiness.py --strict
```

And after staging real local Phase 3 traces outside the repo:

```powershell
python scripts\build_neural_abr_dataset.py --trace-csv-root "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\external_trace_intake\phase3_4a_smoke\normalized" --trace-manifest-root "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\external_trace_intake\phase3_4a_smoke\manifests" --output-dir "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E1_external_trace_smoke_TEST" --split-policy phase4e1_trace_level_regime_v1 --representation-kbps 300,750,1200,1850,2850 --segment-duration-s 4.0 --teacher robust_mpc --seed 123 --diagnostic-only --overwrite
python scripts\validate_neural_abr_dataset.py --dataset-dir "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E1_external_trace_smoke_TEST"
python scripts\train_neural_abr.py --dataset-dir "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E1_external_trace_smoke_TEST" --output-dir "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E1\external_trace_smoke_TEST" --epochs 5 --batch-size 16 --seed 123 --device cpu --smoke
python scripts\validate_neural_abr_offline.py --dataset-dir "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E1_external_trace_smoke_TEST" --run-dir "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E1\external_trace_smoke_TEST" --output-dir "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E1\validation_TEST"
```

## Decision output

At the end, write one of:

```text
PHASE4E1_EXTERNAL_TRACE_SMOKE_PASS_NOT_CANDIDATE
PHASE4E1_EXTERNAL_TRACE_CANDIDATE_READY_FOR_PHASE4F
PHASE4E1_BLOCKED_NEEDS_FIX
```

Default to `PASS_NOT_CANDIDATE` unless no-collapse and validation gates are genuinely satisfied.
