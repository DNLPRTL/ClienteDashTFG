#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

DATASET_DIR="${PHASE45_V3_NEURAL_MPC_FULL_V2_DATASET_DIR:-$HOME/TFG/datasets_normalizados/phase45_v3/throughput_quantile_full_v1_neural_mpc_v2}"
MODEL_ROOT="${PHASE45_V3_NEURAL_MPC_FULL_V2_MODEL_ROOT:-$HOME/TFG/modelos/phase45_v3/throughput_quantile_predictor/full_v1_neural_mpc_v2}"
RUN_ROOT="${PHASE45_V3_NEURAL_MPC_FULL_V2_RUN_ROOT:-$HOME/TFG/runs_phase45_v3/neural_mpc_full_v1_v2}"
SEEDS="${PHASE45_V3_NEURAL_MPC_FULL_V2_SEEDS:-452001 452002 452003}"
EVAL_WINDOWS="${PHASE45_V3_NEURAL_MPC_FULL_V2_EVAL_WINDOWS:-128}"

echo "== Phase45 v3 Neural-MPC full training v2 =="
echo "diagnostic_only=true benchmark_performed=false ranking_performed=false"
echo "dataset_dir=${DATASET_DIR}"
echo "model_root=${MODEL_ROOT}"
echo "run_root=${RUN_ROOT}"
echo "seeds=${SEEDS}"
echo "eval_windows=${EVAL_WINDOWS}"

python3 scripts/generate_phase45_v3_throughput_quantile_dataset.py \
  --output-dir "$DATASET_DIR" \
  --validate-only

for SEED in ${SEEDS}; do
  MODEL_DIR="${MODEL_ROOT}/seed_${SEED}"
  RUN_DIR="${RUN_ROOT}/seed_${SEED}"

  echo "== seed ${SEED}: train full_v1 throughput quantile predictor =="
  python3 scripts/train_phase45_v3_throughput_quantile_predictor.py \
    --profile full_v1 \
    --dataset-profile full_v1 \
    --dataset-dir "$DATASET_DIR" \
    --output-dir "$MODEL_DIR" \
    --run-name "full_v1_neural_mpc_v2_seed${SEED}" \
    --device auto \
    --seed "$SEED" \
    --overwrite

  echo "== seed ${SEED}: offline closed-loop diagnostic on ${EVAL_WINDOWS} validation windows =="
  python3 scripts/evaluate_phase45_v3_neural_mpc_closedloop.py \
    --profile full_v1 \
    --predictor-checkpoint "$MODEL_DIR/modelo_phase45_v3_throughput_quantile.pt" \
    --controllers robust_mpc,bola,throughput_rule,neural_mpc \
    --output-dir "$RUN_DIR" \
    --preset full_v1_v2_diagnostic \
    --max-validation-windows "$EVAL_WINDOWS" \
    --overwrite
done

echo "== pasteable full training v2 summary =="
bash scripts/print_phase45_v3_neural_mpc_full_training_v2_summary_wsl.sh
