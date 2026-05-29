# Phase 4E.2 Ubuntu validation

```bash
cd ~/TFG/DashClientModular4

git pull --ff-only
git status --short --branch
git rev-parse --short HEAD
git log --oneline -5

git diff --check
python3 -m unittest discover
python3 scripts/check_client_readiness.py --strict

git status --porcelain | grep -E '\.pdf$|\.zip$|\.csv$|\.log$|\.mp4$|\.m4s$|\.ts$|__pycache__|\.pyc|\.venv|\.idea|\.htm$|\.html$|\.pt$|\.pth$|\.onnx$|\.ckpt$|events\.out|\.npy$|\.npz$|\.pkl$|\.joblib$' && exit 1 || true
```
