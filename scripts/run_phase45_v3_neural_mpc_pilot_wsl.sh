#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

DATASET_DIR="${PHASE45_V3_NEURAL_MPC_DATASET_DIR:-$HOME/TFG/datasets_normalizados/phase45_v3/throughput_quantile_pilot_v1}"
MODEL_DIR="${PHASE45_V3_NEURAL_MPC_MODEL_DIR:-$HOME/TFG/modelos/phase45_v3/throughput_quantile_predictor/pilot_v1_seed451001}"
RUN_DIR="${PHASE45_V3_NEURAL_MPC_RUN_DIR:-$HOME/TFG/runs_phase45_v3/neural_mpc_pilot_v1_seed451001}"

python3 scripts/generate_phase45_v3_throughput_quantile_dataset.py \
  --profile pilot \
  --output-dir "$DATASET_DIR" \
  --horizon 5 \
  --overwrite

python3 scripts/train_phase45_v3_throughput_quantile_predictor.py \
  --profile pilot \
  --dataset-dir "$DATASET_DIR" \
  --output-dir "$MODEL_DIR" \
  --device auto \
  --epochs 40 \
  --batch-size 1024 \
  --learning-rate 0.0003 \
  --hidden-sizes 256,128,64 \
  --quantiles 0.10,0.25,0.50,0.75 \
  --horizon 5 \
  --pinball-loss-weight 1.0 \
  --quantile-crossing-loss-weight 0.10 \
  --temporal-smoothness-loss-weight 0.05 \
  --seed 451001 \
  --overwrite

python3 scripts/evaluate_phase45_v3_neural_mpc_closedloop.py \
  --profile pilot \
  --predictor-checkpoint "$MODEL_DIR/modelo_phase45_v3_throughput_quantile.pt" \
  --controllers robust_mpc,bola,throughput_rule,neural_mpc \
  --output-dir "$RUN_DIR" \
  --preset diagnostic \
  --fail-on-collapse \
  --overwrite
