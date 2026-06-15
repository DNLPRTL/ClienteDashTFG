#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

DATASET_DIR="${PHASE45_V3_NEURAL_MPC_FULL_V2_DATASET_DIR:-$HOME/TFG/datasets_normalizados/phase45_v3/throughput_quantile_full_v1_neural_mpc_v2}"
HORIZON="${PHASE45_V3_NEURAL_MPC_FULL_V2_HORIZON:-5}"

echo "== Phase45 v3 Neural-MPC full dataset v2 =="
echo "diagnostic_only=true benchmark_performed=false ranking_performed=false"
echo "dataset_profile=full_v1"
echo "dataset_dir=${DATASET_DIR}"
echo "horizon=${HORIZON}"

python3 scripts/generate_phase45_v3_throughput_quantile_dataset.py \
  --profile full_v1 \
  --output-dir "$DATASET_DIR" \
  --horizon "$HORIZON" \
  --overwrite

echo "== pasteable full dataset v2 summary =="
bash scripts/print_phase45_v3_neural_mpc_full_dataset_v2_summary_wsl.sh
