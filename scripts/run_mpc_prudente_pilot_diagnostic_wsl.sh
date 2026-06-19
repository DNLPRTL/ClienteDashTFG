#!/usr/bin/env bash
# MPC Prudente — diagnóstico closed-loop offline (entorno FIEL, ventanas de
# validación). Compara el controller prudente vs robust_mpc/bola/neural_mpc viejo.
#
# CPU (no necesita GPU). No es benchmark ni ranking.
#
# Uso:
#   wsl -d Ubuntu-24.04
#   cd ~/TFG/DashClientModular4
#   git pull
#   source ~/venvs/rocm721/bin/activate
#   bash scripts/run_mpc_prudente_pilot_diagnostic_wsl.sh
set -euo pipefail
cd "$(dirname "$0")/.."

PROFILE="${MPC_PRUDENTE_DIAG_PROFILE:-pilot}"
MEDIA="${MPC_PRUDENTE_MEDIA_PROFILE_ID:-paseo_almunecar_10min_30fps_4s}"
SEED="${MPC_PRUDENTE_TRAIN_SEED:-451001}"
MAX_WINDOWS="${MPC_PRUDENTE_DIAG_MAX_WINDOWS:-32}"
CKPT="${MPC_PRUDENTE_PREDICTOR_CKPT:-$HOME/TFG/modelos/mpc_prudente/throughput_quantile_predictor/${PROFILE}_${MEDIA}_seed${SEED}/modelo_phase45_v3_throughput_quantile.pt}"
OUT="${MPC_PRUDENTE_DIAG_DIR:-$HOME/TFG/runs_mpc_prudente/diagnostico_${PROFILE}_${MEDIA}}"

echo "== MPC Prudente: diagnóstico closed-loop (entorno fiel) =="
echo "diagnostic_only=true benchmark_performed=false ranking_performed=false"
echo "profile=${PROFILE} media=${MEDIA} max_windows=${MAX_WINDOWS}"
echo "predictor=${CKPT}"
echo "output=${OUT}"

python3 scripts/evaluar_mpc_prudente_closedloop.py \
  --profile "$PROFILE" \
  --media-profile-id "$MEDIA" \
  --predictor-checkpoint "$CKPT" \
  --output-dir "$OUT" \
  --max-validation-windows "$MAX_WINDOWS" \
  --device cpu \
  --overwrite

echo
echo "LISTO. Pega la linea que empieza por: MPC_PRUDENTE_DIAGNOSTIC status=..."
