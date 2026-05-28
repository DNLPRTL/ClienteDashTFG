# CLI and artifact contract for Phase 4D

## Required CLIs

```text
python scripts/build_neural_abr_dataset.py --synthetic-smoke --output-dir <dir> --overwrite
python scripts/validate_neural_abr_dataset.py --dataset-dir <dir>
python scripts/train_neural_abr.py --dataset-dir <dir> --output-dir <run_dir> --epochs 1 --batch-size 8 --seed 123 --device cpu --smoke
python scripts/validate_neural_abr_offline.py --dataset-dir <dir> --run-dir <run_dir> --output-dir <validation_dir>
```

## CLI output requirements

Each CLI must print a concise summary and write a JSON report into the output directory.

## Artifact policy

Generated datasets, runs, logs, reports and checkpoints must be outside the repository.

Allowed inside repo:

```text
source code
tests
documentation
```

Forbidden inside repo:

```text
*.pt
*.pth
*.onnx
*.csv generated datasets
*.jsonl generated datasets
*.npy
*.npz
*.pkl
*.joblib
TensorBoard logs
training logs
model checkpoints
```
