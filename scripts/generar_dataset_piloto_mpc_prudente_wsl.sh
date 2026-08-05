#!/usr/bin/env bash
# MPC Prudente — paso: dataset pilot FIEL (medio VBR real + trazas curadas).
#
# Ejecuta en WSL2 (CPU; usa el manifest curado de Phase 3 bajo ~/TFG).
#
# Uso:
#   wsl -d Ubuntu-24.04
#   cd ~/TFG/ClienteDashPrudente
#   git pull
#   source ~/venvs/rocm721/bin/activate
#   bash scripts/generar_dataset_piloto_mpc_prudente_wsl.sh
set -euo pipefail
cd "$(dirname "$0")/.."

PROFILE="${MPC_PRUDENTE_DATASET_PROFILE:-pilot}"
MEDIA="${MPC_PRUDENTE_MEDIA_PROFILE_ID:-paseo_almunecar_10min_30fps_4s}"
OUT="${MPC_PRUDENTE_DATASET_DIR:-$HOME/TFG/datasets_normalizados/mpc_prudente/throughput_quantile_${PROFILE}_${MEDIA}}"

echo "== MPC Prudente: dataset pilot FIEL (medio VBR real) =="
echo "diagnostic_only=true benchmark_performed=false ranking_performed=false"
echo "dataset_profile=${PROFILE} media_profile=${MEDIA}"
echo "dataset_dir=${OUT}"

python3 scripts/generar_dataset_mpc_prudente.py \
  --profile "$PROFILE" \
  --media-profile-id "$MEDIA" \
  --output-dir "$OUT" \
  --overwrite

echo
echo "LISTO. Pega la linea que empieza por: MPC_PRUDENTE_DATASET status=..."
