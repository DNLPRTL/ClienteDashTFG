# Phase 4C artifact layout

## Repository

Only Markdown methodology files are allowed in:

```text
docs/science/04_neural_abr/
```

## Local-only roots

```text
C:\Users\danie\Documents\TFG\_datasets\phase4_AI
C:\Users\danie\Documents\TFG\_runs\phase4_AI
C:\Users\danie\Documents\TFG\_models\phase4_AI
```

## Dataset layout

```text
_datasets\phase4_AI\
  raw\
  converted\
  manifests\
  neural_abr_lite\
    dataset_v1\
      dataset_manifest.json
      train\
      validation\
      ood_diagnostic\
      normalization_stats.json
      leakage_audit_report.json
      teacher_label_report.json
```

## Runs layout

```text
_runs\phase4_AI\
  neural_abr_lite\
    run_<timestamp>\
      training_config.json
      metrics.json
      validation_report.json
      ood_diagnostic_report.json
      environment.json
      run.log
```

## Models layout

```text
_models\phase4_AI\
  neural_abr_lite\
    candidate_<timestamp>\
      model_state.pt
      model_card.json
      feature_schema.json
      normalization_stats.json
      inference_contract.json
      export_manifest.json
```

## Forbidden in repo

```text
*.pdf
*.zip
*.pt
*.pth
*.onnx
*.csv
*.npy
*.npz
*.pkl
*.joblib
*.mp4
*.m4s
*.mpd
*.log
```
