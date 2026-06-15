#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

MODEL_ROOT="${PHASE45_V3_NEURAL_MPC_FULL_V2_MODEL_ROOT:-$HOME/TFG/modelos/phase45_v3/throughput_quantile_predictor/full_v1_neural_mpc_v2}"
RUN_ROOT="${PHASE45_V3_NEURAL_MPC_FULL_V2_RUN_ROOT:-$HOME/TFG/runs_phase45_v3/neural_mpc_full_v1_v2}"
BUNDLE_DIR="${PHASE45_V3_NEURAL_MPC_V2_BUNDLE_DIR:-$HOME/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v2}"
CANONICAL_SEED="${PHASE45_V3_NEURAL_MPC_V2_CANONICAL_SEED:-452003}"
SEEDS="${PHASE45_V3_NEURAL_MPC_FULL_V2_SEEDS_CSV:-452001,452002,452003}"
CONTROLLER_KEY="phase45_v3_neural_throughput_calibrated_mpc_v2"

echo "== Phase45 v3 Neural-MPC experimental bundle v2 export =="
echo "benchmark_performed=false ranking_performed=false controller_integrated=false"
echo "model_root=${MODEL_ROOT}"
echo "run_root=${RUN_ROOT}"
echo "bundle_dir=${BUNDLE_DIR}"
echo "canonical_seed=${CANONICAL_SEED}"
echo "seeds=${SEEDS}"
echo "controller_key=${CONTROLLER_KEY}"

python3 scripts/export_phase45_v3_neural_mpc_experimental_bundle.py \
  --model-root "$MODEL_ROOT" \
  --run-root "$RUN_ROOT" \
  --output-dir "$BUNDLE_DIR" \
  --canonical-seed "$CANONICAL_SEED" \
  --seeds "$SEEDS" \
  --controller-key "$CONTROLLER_KEY" \
  --candidate-key "$CONTROLLER_KEY" \
  --overwrite

python3 scripts/validate_phase45_v3_neural_mpc_experimental_bundle.py \
  --bundle-dir "$BUNDLE_DIR"

echo "== pasteable bundle v2 summary =="
bash scripts/print_phase45_v3_neural_mpc_experimental_bundle_v2_summary_wsl.sh
