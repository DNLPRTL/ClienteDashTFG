#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

DATASET_DIR="${PHASE45_V3_SPBC_POLICY_FULL_DATASET_DIR:-$HOME/TFG/datasets_normalizados/phase45_v3/closedloop_spbc_spc_full_v1}"
RUN_NAME="${PHASE45_V3_SPBC_POLICY_RUN_NAME:-spbc_policy_pilot_from_full_seed453001_v1}"
OUTPUT_DIR="${PHASE45_V3_SPBC_POLICY_OUTPUT_DIR:-$HOME/TFG/modelos/phase45_v3/spbc_policy/$RUN_NAME}"
LOG="/tmp/phase45_v3_spbc_policy_pilot_from_full_$(date +%Y%m%d_%H%M%S).log"

echo "== Phase45 v3 SPBC policy pilot-from-full =="
echo "benchmark_performed=false ranking_performed=false"
echo "dataset_dir=${DATASET_DIR}"
echo "run_name=${RUN_NAME}"
echo "output_dir=${OUTPUT_DIR}"
echo "log=${LOG}"

python3 scripts/train_phase45_v3_spbc_policy.py \
  --profile pilot_from_full_v1 \
  --dataset-profile full_v1 \
  --dataset-dir "$DATASET_DIR" \
  --output-dir "$OUTPUT_DIR" \
  --run-name "$RUN_NAME" \
  --overwrite 2>&1 | tee "$LOG"

echo "Salida ${RUN_NAME}: ${LOG}"
