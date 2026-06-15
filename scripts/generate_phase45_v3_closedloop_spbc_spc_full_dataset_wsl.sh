#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

DATASET_DIR="${PHASE45_V3_CLOSEDLOOP_SPBC_SPC_FULL_DATASET_DIR:-$HOME/TFG/datasets_normalizados/phase45_v3/closedloop_spbc_spc_full_v1}"

echo "== Phase45 v3 closed-loop SPBC/SPC full dataset =="
echo "diagnostic_only=true benchmark_performed=false ranking_performed=false"
echo "dataset_profile=full_v1"
echo "dataset_dir=${DATASET_DIR}"

python3 scripts/generate_phase45_v3_closedloop_spbc_spc_dataset.py \
  --profile full_v1 \
  --output-dir "$DATASET_DIR" \
  --overwrite

echo "== pasteable full dataset summary =="
python3 scripts/summarize_phase45_v3_closedloop_spbc_spc_dataset.py \
  --profile full_v1 \
  --dataset-dir "$DATASET_DIR"
