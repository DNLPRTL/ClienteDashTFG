# Phase 4B artifact policy

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Repo policy

Allowed in Git:

```text
Markdown documentation
small config examples if later approved
small templates
```

Forbidden in Git:

```text
PDFs
raw traces
datasets
converted trace archives
teacher label files
normalization manifests from real runs
training logs
TensorBoard logs
model checkpoints
.pt / .pth / .onnx files
large CSVs
large JSONL/NPZ artifacts
zips
media files
screenshots
```

## Local-only roots

Recommended local-only roots:

```text
C:\Users\danie\Documents\TFG\_literature\phase4_AI
C:\Users\danie\Documents\TFG\_datasets\phase4_AI
C:\Users\danie\Documents\TFG\_runs\phase4_AI
C:\Users\danie\Documents\TFG\_models\phase4_AI
```

## Future generated artifacts

Future generated artifacts must include manifests and remain outside Git unless converted into short Markdown summaries.

Examples:

```text
dataset_manifest.json
split_manifest.json
teacher_label_manifest.json
normalization_manifest.json
training_run_manifest.json
validation_report.json
model_card.md
```

`model_card.md` may be committed later if it contains no binary weights and no large data.

## Phase 4B decision

Phase 4B commits only documentation. No generated ML artifact belongs in the repo.
