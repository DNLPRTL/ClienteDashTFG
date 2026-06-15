#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

BUNDLE_DIR="${PHASE45_V3_NEURAL_MPC_BUNDLE_DIR:-$HOME/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1}"

echo "== Phase45 v3 Neural-MPC bundle validation: Ubuntu cliente =="
echo "benchmark_performed=false ranking_performed=false controller_integrated=false"
echo "bundle_dir=${BUNDLE_DIR}"

python3 scripts/validate_phase45_v3_neural_mpc_experimental_bundle.py \
  --bundle-dir "$BUNDLE_DIR"

echo "== pasteable bundle summary =="
bash scripts/print_phase45_v3_neural_mpc_experimental_bundle_summary_ubuntu_cliente.sh
