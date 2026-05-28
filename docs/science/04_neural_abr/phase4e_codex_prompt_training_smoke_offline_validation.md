# Codex prompt — Phase 4E training smoke + offline validation

You are working on DashClientModular4, Phase 4E.

## Phase state

Phase 4D implemented the offline NeuralABR-Lite pipeline. Phase 4E must run and document controlled training smoke/offline validation.

## Selected method

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

## Read first

```text
docs/science/04_neural_abr/phase4d_implementation_report.md
docs/science/04_neural_abr/phase4d_code_traceability_matrix.md
docs/science/04_neural_abr/phase4d_test_report.md
docs/science/04_neural_abr/phase4e_training_smoke_plan.md
docs/science/04_neural_abr/phase4e_model_acceptance_gates.md
docs/science/04_neural_abr/phase4e_no_benchmark_policy.md
docs/science/04_neural_abr/phase4e_training_commands_windows.md
docs/science/04_neural_abr/phase4e_defense_material_requirements.md
```

## Mission

Run Phase 4E Tier 0 synthetic smoke and produce complete reports. If the existing Phase 4D CLIs have defects, fix only the minimal allowed files and update tests.

## Strict non-goals

```text
Do not register a neural ABR controller.
Do not touch player/runtime/media.
Do not modify classical controllers.
Do not integrate the model in the client.
Do not run or create benchmark/ranking.
Do not use legacy dry-runs as training data.
Do not put checkpoints/logs/CSV/JSONL datasets inside the repo.
Do not introduce GPU dependencies.
Do not choose PPO or RL-first.
Do not make SOTA or real-world claims.
```

## Allowed edits

Preferred documentation edits:

```text
docs/science/04_neural_abr/phase4e_training_smoke_report.md
docs/science/04_neural_abr/phase4e_offline_validation_report.md
docs/science/04_neural_abr/phase4e_model_selection_notes.md
docs/science/04_neural_abr/phase4e_artifact_manifest.md
docs/science/04_neural_abr/phase4e_model_card_draft.md
docs/science/04_neural_abr/phase4e_defense_talking_points.md
docs/science/04_neural_abr/phase4e_open_limitations.md
docs/science/04_neural_abr/phase4e_closure_report.md
```

Allowed code/test fixes only if necessary:

```text
core/neural_abr/*.py
scripts/build_neural_abr_dataset.py
scripts/validate_neural_abr_dataset.py
scripts/train_neural_abr.py
scripts/validate_neural_abr_offline.py
tests/test_neural_abr_*.py
```

If any other file seems necessary, stop and explain.

## Exact Phase 4E smoke commands

Run in PowerShell from the repository root:

```powershell
$Stamp = Get-Date -Format "yyyyMMdd_HHmmss"
$DatasetDir = "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E_synthetic_smoke_$Stamp"
$RunDir = "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E\smoke_$Stamp"
$ValidationDir = "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E\validation_$Stamp"

New-Item -ItemType Directory -Path $DatasetDir -Force | Out-Null
New-Item -ItemType Directory -Path $RunDir -Force | Out-Null
New-Item -ItemType Directory -Path $ValidationDir -Force | Out-Null

python scripts/build_neural_abr_dataset.py --synthetic-smoke --output-dir $DatasetDir --overwrite
python scripts/validate_neural_abr_dataset.py --dataset-dir $DatasetDir
python scripts/train_neural_abr.py --dataset-dir $DatasetDir --output-dir $RunDir --epochs 3 --batch-size 8 --seed 123 --device cpu --smoke
python scripts/validate_neural_abr_offline.py --dataset-dir $DatasetDir --run-dir $RunDir --output-dir $ValidationDir
python -m unittest discover
python scripts/check_client_readiness.py --strict
```

## Report requirements

Write the exact commands, paths, test results and limitations. Include one final decision:

```text
PHASE4E_SYNTHETIC_SMOKE_PASS_READY_FOR_TRACE_DATA
PHASE4E_PARTIAL_FIX_REQUIRED
PHASE4E_FAIL
```

Do not mark `PHASE4E_OFFLINE_CANDIDATE_READY_FOR_PHASE4F` unless external traces, trace-level train/validation/OOD split and no-leakage validation were actually used.

## Acceptance

Phase 4E Tier 0 passes if:

```text
dataset build PASS
dataset validation PASS
training smoke PASS
offline validation PASS
python -m unittest discover PASS
check_client_readiness PASS
no forbidden artifacts in repo
reports written
no benchmark/ranking claims
```

## Final response

Report:

```text
files changed
commands executed
artifact paths
unit tests result
readiness result
Phase 4E decision
limitations
next step
```
