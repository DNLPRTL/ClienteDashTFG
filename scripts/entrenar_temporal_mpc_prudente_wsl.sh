#!/usr/bin/env bash
# MPC Prudente — entrenar el predictor TEMPORAL (GRU) ensemble (full) en GPU.
#
#   wsl -d Ubuntu-24.04
#   cd ~/TFG/ClienteDashPrudente
#   git pull
#   source ~/venvs/rocm721/bin/activate
#   bash scripts/entrenar_temporal_mpc_prudente_wsl.sh
set -euo pipefail
cd "$(dirname "$0")/.."

# Por defecto entrena sobre el dataset MULTI-VÍDEO (sin sesgo a un solo vídeo).
MEDIA="${MPC_PRUDENTE_MEDIA_PROFILE_ID:-multimedia}"
PROFILE="${MPC_PRUDENTE_TEMPORAL_PROFILE:-full}"
DATASET_DIR="${MPC_PRUDENTE_DATASET_DIR:-$HOME/TFG/datasets_normalizados/mpc_prudente/throughput_quantile_full_v1_${MEDIA}}"
MODEL_DIR="${MPC_PRUDENTE_TEMPORAL_MODEL_DIR:-$HOME/TFG/modelos/mpc_prudente/temporal_predictor/${PROFILE}_${MEDIA}}"

echo "== MPC Prudente: entrenamiento predictor TEMPORAL (GRU ensemble) =="
echo "diagnostic_only=true benchmark_performed=false ranking_performed=false"
echo "profile=${PROFILE} media=${MEDIA}"
echo "dataset_dir=${DATASET_DIR}"
echo "model_dir=${MODEL_DIR}"

python3 scripts/entrenar_predictor_temporal_mpc_prudente.py \
  --profile "$PROFILE" \
  --media-profile-id "$MEDIA" \
  --dataset-dir "$DATASET_DIR" \
  --output-dir "$MODEL_DIR" \
  --device auto \
  --overwrite

echo
echo "LISTO. Pega: MPC_PRUDENTE_TEMPORAL status=..."
