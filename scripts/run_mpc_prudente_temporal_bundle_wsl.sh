#!/usr/bin/env bash
# MPC Prudente — exporta el bundle runtime del predictor TEMPORAL (ensemble).
# Se ejecuta en WSL (donde está el modelo entrenado). Luego se MUEVE el bundle a
# Ubuntu cliente para Phase 6.
#
#   wsl -d Ubuntu-24.04
#   cd ~/TFG/DashClientModular4 && git pull
#   source ~/venvs/rocm721/bin/activate
#   bash scripts/run_mpc_prudente_temporal_bundle_wsl.sh
set -euo pipefail
cd "$(dirname "$0")/.."

TRAIN_DIR="${MPC_PRUDENTE_TEMPORAL_MODEL_DIR:-$HOME/TFG/modelos/mpc_prudente/temporal_predictor/full_multimedia}"
BUNDLE_DIR="${MPC_PRUDENTE_TEMPORAL_BUNDLE_DIR:-$HOME/TFG/modelos/mpc_prudente/temporal_runtime_bundle_v1}"
MEDIA="${MPC_PRUDENTE_MEDIA_PROFILE_ID:-paseo_almunecar_10min_30fps_4s}"
RISK_ALPHA="${MPC_PRUDENTE_RISK_ALPHA:-0.75}"

echo "== MPC Prudente: export bundle TEMPORAL (ensemble) =="
echo "train_dir=${TRAIN_DIR}"
echo "bundle_dir=${BUNDLE_DIR}"
echo "media=${MEDIA} risk_alpha=${RISK_ALPHA}"

python3 scripts/exportar_bundle_temporal_mpc_prudente.py \
  --training-dir "$TRAIN_DIR" \
  --bundle-dir "$BUNDLE_DIR" \
  --media-profile-id "$MEDIA" \
  --risk-alpha "$RISK_ALPHA" \
  --overwrite

echo
echo "== empaquetar para mover a Ubuntu cliente =="
TARBALL="$HOME/TFG/mpc_prudente_temporal_runtime_bundle_v1.tar.gz"
tar -czf "$TARBALL" -C "$(dirname "$BUNDLE_DIR")" "$(basename "$BUNDLE_DIR")"
echo "tarball=${TARBALL}"
echo
echo "LISTO. Pega: MPC_PRUDENTE_TEMPORAL_BUNDLE status=..."
echo "Luego mueve ${TARBALL} a Ubuntu cliente y descomprímelo en ~/TFG/modelos/mpc_prudente/"
