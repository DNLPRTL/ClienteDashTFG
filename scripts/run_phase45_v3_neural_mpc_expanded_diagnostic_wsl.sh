#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

DATASET_DIR="${PHASE45_V3_NEURAL_MPC_EXPANDED_DATASET_DIR:-$HOME/TFG/datasets_normalizados/phase45_v3/throughput_quantile_expanded_diag_v1}"
MODEL_ROOT="${PHASE45_V3_NEURAL_MPC_EXPANDED_MODEL_ROOT:-$HOME/TFG/modelos/phase45_v3/throughput_quantile_predictor/expanded_diag_v1}"
RUN_ROOT="${PHASE45_V3_NEURAL_MPC_EXPANDED_RUN_ROOT:-$HOME/TFG/runs_phase45_v3/neural_mpc_expanded_diag_v1}"
SEEDS="${PHASE45_V3_NEURAL_MPC_EXPANDED_SEEDS:-451001 451002 451003}"
EVAL_WINDOWS="${PHASE45_V3_NEURAL_MPC_EXPANDED_EVAL_WINDOWS:-32}"
EPOCHS="${PHASE45_V3_NEURAL_MPC_EXPANDED_EPOCHS:-40}"

echo "== Phase45 v3 Neural-MPC expanded diagnostic =="
echo "diagnostic_only=true benchmark_performed=false ranking_performed=false"
echo "dataset_dir=${DATASET_DIR}"
echo "model_root=${MODEL_ROOT}"
echo "run_root=${RUN_ROOT}"
echo "seeds=${SEEDS}"
echo "eval_windows=${EVAL_WINDOWS}"

python3 scripts/generate_phase45_v3_throughput_quantile_dataset.py \
  --profile pilot \
  --output-dir "$DATASET_DIR" \
  --horizon 5 \
  --overwrite

for SEED in ${SEEDS}; do
  MODEL_DIR="${MODEL_ROOT}/seed_${SEED}"
  RUN_DIR="${RUN_ROOT}/seed_${SEED}"
  echo "== seed ${SEED}: train throughput quantile predictor =="
  python3 scripts/train_phase45_v3_throughput_quantile_predictor.py \
    --profile pilot \
    --dataset-dir "$DATASET_DIR" \
    --output-dir "$MODEL_DIR" \
    --run-name "expanded_diag_v1_seed${SEED}" \
    --device auto \
    --epochs "$EPOCHS" \
    --batch-size 1024 \
    --learning-rate 0.0003 \
    --hidden-sizes 256,128,64 \
    --quantiles 0.10,0.25,0.50,0.75 \
    --horizon 5 \
    --pinball-loss-weight 1.0 \
    --quantile-crossing-loss-weight 0.10 \
    --temporal-smoothness-loss-weight 0.05 \
    --seed "$SEED" \
    --overwrite

  echo "== seed ${SEED}: evaluate ${EVAL_WINDOWS} validation windows =="
  python3 scripts/evaluate_phase45_v3_neural_mpc_closedloop.py \
    --profile pilot \
    --predictor-checkpoint "$MODEL_DIR/modelo_phase45_v3_throughput_quantile.pt" \
    --controllers robust_mpc,bola,throughput_rule,neural_mpc \
    --output-dir "$RUN_DIR" \
    --preset expanded_diagnostic \
    --max-validation-windows "$EVAL_WINDOWS" \
    --overwrite
done

echo "== pasteable summary =="
bash scripts/print_phase45_v3_neural_mpc_expanded_diagnostic_summary_wsl.sh
