# Phase 4E — Windows command runbook

## 0. Move to repo

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
Set-Location "C:\Users\danie\Documents\TFG\DashClientModular4"
$RepoRoot = git rev-parse --show-toplevel
```

## 1. Validate current repository

```powershell
git status --short --branch
git diff --check
python -m unittest discover
python scripts\check_client_readiness.py --strict
```

## 2. Phase 4E synthetic smoke run

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
Set-Location "C:\Users\danie\Documents\TFG\DashClientModular4"

$Stamp = Get-Date -Format "yyyyMMdd_HHmmss"
$DatasetDir = "C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E_synthetic_smoke_$Stamp"
$RunDir = "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E\smoke_$Stamp"
$ValidationDir = "C:\Users\danie\Documents\TFG\_runs\phase4_AI\phase4E\validation_$Stamp"

New-Item -ItemType Directory -Path $DatasetDir -Force | Out-Null
New-Item -ItemType Directory -Path $RunDir -Force | Out-Null
New-Item -ItemType Directory -Path $ValidationDir -Force | Out-Null

python scripts\build_neural_abr_dataset.py --synthetic-smoke --output-dir $DatasetDir --overwrite
python scripts\validate_neural_abr_dataset.py --dataset-dir $DatasetDir
python scripts\train_neural_abr.py --dataset-dir $DatasetDir --output-dir $RunDir --epochs 3 --batch-size 8 --seed 123 --device cpu --smoke
python scripts\validate_neural_abr_offline.py --dataset-dir $DatasetDir --run-dir $RunDir --output-dir $ValidationDir

python -m unittest discover
python scripts\check_client_readiness.py --strict

Write-Host "DatasetDir=$DatasetDir"
Write-Host "RunDir=$RunDir"
Write-Host "ValidationDir=$ValidationDir"
```

## 3. Forbidden artifact check

```powershell
$Forbidden = git status --porcelain | Where-Object { $_ -match "\.pdf$|\.zip$|\.csv$|\.log$|\.mp4$|\.m4s$|\.ts$|__pycache__|\.pyc|\.venv|\.idea|\.htm$|\.html$|\.pt$|\.pth$|\.onnx$|\.ckpt$|events\.out|\.npy$|\.npz$|\.pkl$|\.joblib$" }
if ($Forbidden) {
  $Forbidden
  throw "Forbidden generated artifact detected in repository status."
}
```

## 4. Commit after approval

Do not run this until the phase report is reviewed.

```powershell
git add docs/science/04_neural_abr core/neural_abr scripts/build_neural_abr_dataset.py scripts/validate_neural_abr_dataset.py scripts/train_neural_abr.py scripts/validate_neural_abr_offline.py tests/test_neural_abr_*.py
git diff --cached --check
git commit -m "feat(neural-abr): validate Phase 4E offline training smoke"
git push origin main
```
