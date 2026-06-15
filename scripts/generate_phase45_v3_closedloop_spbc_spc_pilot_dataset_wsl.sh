#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

DATASET_DIR="${PHASE45_V3_CLOSEDLOOP_SPBC_SPC_PILOT_DATASET_DIR:-$HOME/TFG/datasets_normalizados/phase45_v3/closedloop_spbc_spc_pilot_v1}"

echo "== Phase45 v3 closed-loop SPBC/SPC pilot dataset =="
echo "diagnostic_only=true benchmark_performed=false ranking_performed=false"
echo "dataset_profile=pilot"
echo "dataset_dir=${DATASET_DIR}"

python3 scripts/generate_phase45_v3_closedloop_spbc_spc_dataset.py \
  --profile pilot \
  --output-dir "$DATASET_DIR" \
  --overwrite

echo "== pasteable pilot dataset summary =="
python3 scripts/summarize_phase45_v3_closedloop_spbc_spc_dataset.py \
  --profile pilot \
  --dataset-dir "$DATASET_DIR"
