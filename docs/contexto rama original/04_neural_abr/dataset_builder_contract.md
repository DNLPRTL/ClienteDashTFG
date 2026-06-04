# Dataset builder contract

## Purpose

Define the future dataset builder without implementing it in Phase 4C.

## Future command shape

The future command may look like:

```powershell
python scripts/build_neural_abr_dataset.py `
  --trace-manifest C:\Users\danie\Documents\TFG\_datasets\phase4_AI\manifests\trace_manifest.json `
  --split-manifest C:\Users\danie\Documents\TFG\_datasets\phase4_AI\manifests\split_manifest.json `
  --teacher robust_mpc `
  --reward-version qoe_linear_v1 `
  --output C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\dataset_v1
```

This is a contract example, not an implementation request.

## Required outputs

```text
dataset_manifest.json
train_samples
validation_samples
ood_diagnostic_samples
normalization_stats.json
teacher_label_report.json
leakage_audit_report.json
```

## Build gates

A dataset build is invalid if:

- any sample is missing action mask;
- any label is outside the ladder;
- any validation/OOD trace appears in train;
- normalization stats use non-train data;
- a prohibited feature is present;
- trace units are ambiguous;
- source dataset is undocumented;
- generated files are inside the repository.
