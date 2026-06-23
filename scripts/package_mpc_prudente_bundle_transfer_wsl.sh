#!/usr/bin/env bash
# MPC Prudente — empaquetar el bundle para moverlo a la VM cliente Ubuntu.
#
#   bash scripts/package_mpc_prudente_bundle_transfer_wsl.sh
set -euo pipefail

BUNDLE_DIR="${MPC_PRUDENTE_BUNDLE_DIR:-$HOME/TFG/modelos/mpc_prudente/runtime_bundle_v1}"
OUT="${MPC_PRUDENTE_BUNDLE_TAR:-$HOME/TFG/paquetes_transfer/mpc_prudente_runtime_bundle_v1.tar.gz}"

mkdir -p "$(dirname "$OUT")"
tar -czf "$OUT" -C "$(dirname "$BUNDLE_DIR")" "$(basename "$BUNDLE_DIR")"

echo "Bundle empaquetado en: $OUT"
echo
echo "Muévelo a la VM cliente Ubuntu (scp / carpeta compartida) y descomprímelo así en la VM cliente:"
echo "  mkdir -p ~/TFG/modelos/mpc_prudente"
echo "  tar -xzf <ruta_del_tar>/mpc_prudente_runtime_bundle_v1.tar.gz -C ~/TFG/modelos/mpc_prudente/"
