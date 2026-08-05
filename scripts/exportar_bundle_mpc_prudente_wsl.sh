#!/usr/bin/env bash
# MPC Prudente — exportar el bundle runtime desde el modelo entrenado (WSL).
#
#   wsl -d Ubuntu-24.04
#   cd ~/TFG/ClienteDashTFG
#   git pull
#   source ~/venvs/rocm721/bin/activate
#   bash scripts/exportar_bundle_mpc_prudente_wsl.sh
set -euo pipefail
cd "$(dirname "$0")/.."

MEDIA="${MPC_PRUDENTE_MEDIA_PROFILE_ID:-paseo_almunecar_10min_30fps_4s}"
SEED="${MPC_PRUDENTE_TRAIN_SEED:-451001}"
ALPHA="${MPC_PRUDENTE_RISK_ALPHA:-0.75}"
BUNDLE_DIR="${MPC_PRUDENTE_BUNDLE_DIR:-$HOME/TFG/modelos/mpc_prudente/runtime_bundle_v1}"

echo "== MPC Prudente: export bundle runtime =="
echo "media=${MEDIA} seed=${SEED} risk_alpha=${ALPHA}"
echo "bundle_dir=${BUNDLE_DIR}"

python3 scripts/exportar_bundle_mpc_prudente.py \
  --media-profile-id "$MEDIA" \
  --seed "$SEED" \
  --risk-alpha "$ALPHA" \
  --bundle-dir "$BUNDLE_DIR" \
  --overwrite

echo
echo "LISTO. Pega: MPC_PRUDENTE_BUNDLE status=..."
