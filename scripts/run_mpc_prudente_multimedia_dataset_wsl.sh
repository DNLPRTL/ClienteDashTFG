#!/usr/bin/env bash
# MPC Prudente — dataset FULL MULTI-VÍDEO fiel: rota los 8 vídeos de 4s por ventana.
# Misma cobertura de red, pero las dinámicas de buffer cubren TODOS los vídeos
# (sin sesgo a uno solo). Para el predictor temporal.
#
#   wsl -d Ubuntu-24.04
#   cd ~/TFG/DashClientModular4 && git pull
#   source ~/venvs/rocm721/bin/activate
#   bash scripts/run_mpc_prudente_multimedia_dataset_wsl.sh
set -euo pipefail
cd "$(dirname "$0")/.."

OUT="${MPC_PRUDENTE_DATASET_DIR:-$HOME/TFG/datasets_normalizados/mpc_prudente/throughput_quantile_full_v1_multimedia}"

echo "== MPC Prudente: dataset FULL MULTI-VÍDEO fiel (8 perfiles de 4s) =="
echo "diagnostic_only=true benchmark_performed=false ranking_performed=false"
echo "profile=full_v1 media=multimedia"
echo "dataset_dir=${OUT}"

python3 scripts/generar_dataset_mpc_prudente.py \
  --profile full_v1 \
  --multimedia \
  --output-dir "$OUT" \
  --overwrite

echo
echo "LISTO. Pega: MPC_PRUDENTE_DATASET status=..."
