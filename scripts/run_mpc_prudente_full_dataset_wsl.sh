#!/usr/bin/env bash
# MPC Prudente — dataset FULL fiel (medio VBR real). Para el predictor temporal.
#
#   wsl -d Ubuntu-24.04
#   cd ~/TFG/DashClientModular4
#   git pull
#   source ~/venvs/rocm721/bin/activate
#   bash scripts/run_mpc_prudente_full_dataset_wsl.sh
set -euo pipefail
cd "$(dirname "$0")/.."

MEDIA="${MPC_PRUDENTE_MEDIA_PROFILE_ID:-paseo_almunecar_10min_30fps_4s}"
OUT="${MPC_PRUDENTE_DATASET_DIR:-$HOME/TFG/datasets_normalizados/mpc_prudente/throughput_quantile_full_v1_${MEDIA}}"

echo "== MPC Prudente: dataset FULL fiel (medio VBR real) =="
echo "diagnostic_only=true benchmark_performed=false ranking_performed=false"
echo "profile=full_v1 media=${MEDIA}"
echo "dataset_dir=${OUT}"

python3 scripts/generar_dataset_mpc_prudente.py \
  --profile full_v1 \
  --media-profile-id "$MEDIA" \
  --output-dir "$OUT" \
  --overwrite

echo
echo "LISTO. Pega: MPC_PRUDENTE_DATASET status=..."
