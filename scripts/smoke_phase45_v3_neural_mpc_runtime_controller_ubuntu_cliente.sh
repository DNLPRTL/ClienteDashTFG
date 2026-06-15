#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

BUNDLE_DIR="${PHASE45_V3_NEURAL_MPC_BUNDLE_DIR:-$HOME/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1}"
CONTROLLER_KEY="${PHASE45_V3_NEURAL_MPC_CONTROLLER_KEY:-phase45_v3_neural_throughput_calibrated_mpc_v1}"

echo "== Phase45 v3 Neural-MPC runtime controller smoke: Ubuntu cliente =="
echo "benchmark_performed=false ranking_performed=false phase6_formal_evaluation_performed=false"
echo "bundle_dir=${BUNDLE_DIR}"
echo "controller_key=${CONTROLLER_KEY}"

python3 scripts/smoke_phase45_v3_neural_mpc_runtime_controller.py \
  --bundle-dir "$BUNDLE_DIR" \
  --controller-key "$CONTROLLER_KEY"
