#!/usr/bin/env bash
# MPC Prudente — entrenar el predictor de cuantiles sobre el dataset pilot FIEL.
#
# Ejecuta en WSL2 con GPU (ROCm). No es benchmark ni ranking.
#
# Uso:
#   wsl -d Ubuntu-24.04
#   cd ~/TFG/ClienteDashTFG
#   git pull
#   source ~/venvs/rocm721/bin/activate
#   bash scripts/entrenar_piloto_mpc_prudente_wsl.sh
set -euo pipefail
cd "$(dirname "$0")/.."

PROFILE="${MPC_PRUDENTE_TRAIN_PROFILE:-pilot}"
MEDIA="${MPC_PRUDENTE_MEDIA_PROFILE_ID:-paseo_almunecar_10min_30fps_4s}"
SEED="${MPC_PRUDENTE_TRAIN_SEED:-451001}"
DATASET_DIR="${MPC_PRUDENTE_DATASET_DIR:-$HOME/TFG/datasets_normalizados/mpc_prudente/throughput_quantile_${PROFILE}_${MEDIA}}"
MODEL_DIR="${MPC_PRUDENTE_MODEL_DIR:-$HOME/TFG/modelos/mpc_prudente/throughput_quantile_predictor/${PROFILE}_${MEDIA}_seed${SEED}}"

echo "== MPC Prudente: entrenamiento predictor (dataset fiel) =="
echo "diagnostic_only=true benchmark_performed=false ranking_performed=false"
echo "train_profile=${PROFILE} media_profile=${MEDIA} seed=${SEED}"
echo "dataset_dir=${DATASET_DIR}"
echo "model_dir=${MODEL_DIR}"

python3 scripts/entrenar_predictor_mpc_prudente.py \
  --profile "$PROFILE" \
  --media-profile-id "$MEDIA" \
  --dataset-dir "$DATASET_DIR" \
  --output-dir "$MODEL_DIR" \
  --device auto \
  --seed "$SEED" \
  --overwrite

echo
echo "LISTO. Pega la linea que empieza por: MPC_PRUDENTE_TRAINING status=..."
