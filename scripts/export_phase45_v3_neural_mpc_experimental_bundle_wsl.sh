#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

MODEL_ROOT="${PHASE45_V3_NEURAL_MPC_EXPANDED_MODEL_ROOT:-$HOME/TFG/modelos/phase45_v3/throughput_quantile_predictor/expanded_diag_v1}"
RUN_ROOT="${PHASE45_V3_NEURAL_MPC_EXPANDED_RUN_ROOT:-$HOME/TFG/runs_phase45_v3/neural_mpc_expanded_diag_v1}"
BUNDLE_DIR="${PHASE45_V3_NEURAL_MPC_BUNDLE_DIR:-$HOME/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1}"
CANONICAL_SEED="${PHASE45_V3_NEURAL_MPC_CANONICAL_SEED:-451001}"
SEEDS="${PHASE45_V3_NEURAL_MPC_EXPANDED_SEEDS_CSV:-451001,451002,451003}"

echo "== Phase45 v3 Neural-MPC experimental bundle export =="
echo "benchmark_performed=false ranking_performed=false controller_integrated=false"
echo "model_root=${MODEL_ROOT}"
echo "run_root=${RUN_ROOT}"
echo "bundle_dir=${BUNDLE_DIR}"
echo "canonical_seed=${CANONICAL_SEED}"
echo "seeds=${SEEDS}"

python3 scripts/export_phase45_v3_neural_mpc_experimental_bundle.py \
  --model-root "$MODEL_ROOT" \
  --run-root "$RUN_ROOT" \
  --output-dir "$BUNDLE_DIR" \
  --canonical-seed "$CANONICAL_SEED" \
  --seeds "$SEEDS" \
  --overwrite

python3 scripts/validate_phase45_v3_neural_mpc_experimental_bundle.py \
  --bundle-dir "$BUNDLE_DIR"

echo "== pasteable bundle summary =="
bash scripts/print_phase45_v3_neural_mpc_experimental_bundle_summary_wsl.sh
