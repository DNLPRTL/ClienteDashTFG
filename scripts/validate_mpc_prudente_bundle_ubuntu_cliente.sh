#!/usr/bin/env bash
# MPC Prudente — validar el bundle ya copiado en la VM cliente Ubuntu.
#
#   cd ~/TFG/ClienteDashPrudente
#   git pull
#   bash scripts/validate_mpc_prudente_bundle_ubuntu_cliente.sh
set -euo pipefail
cd "$(dirname "$0")/.."

BUNDLE_DIR="${MPC_PRUDENTE_BUNDLE_DIR:-$HOME/TFG/modelos/mpc_prudente/runtime_bundle_v1}"

echo "== MPC Prudente: validar bundle (Ubuntu cliente) =="
echo "bundle_dir=${BUNDLE_DIR}"

python3 scripts/validar_bundle_mpc_prudente.py --bundle-dir "$BUNDLE_DIR"

echo
echo "LISTO. Pega: MPC_PRUDENTE_BUNDLE_VALIDATION status=..."
