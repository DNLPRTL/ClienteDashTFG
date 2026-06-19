#!/usr/bin/env bash
# Paso 0 de la linea de controller fiel-al-medio: extraer tamanos reales (VBR)
# de los segmentos DASH desde el servidor de contenidos.
#
# Se ejecuta en la VM cliente Ubuntu (la unica que alcanza el servidor DASH).
# Genera media_profiles/segment_sizes/<perfil>.json y los sube por git.
#
# Uso:
#   cd ~/TFG/DashClientModular4
#   git pull
#   bash scripts/extraer_tamanos_reales_segmentos_ubuntu_cliente.sh
set -euo pipefail

BASE_URL="${BASE_URL:-http://192.168.1.132/dash}"
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

echo "== Sincronizando repo =="
git pull --rebase --autostash || true

echo "== Comprobando acceso al servidor DASH: $BASE_URL =="
if ! curl -sfI "$BASE_URL/" >/dev/null; then
  echo "ERROR: no se alcanza $BASE_URL desde esta VM. Revisa IP/Apache/firewall." >&2
  exit 2
fi

echo "== Extrayendo tamanos reales de segmento (8 perfiles 4s) =="
python3 scripts/extraer_tamanos_reales_segmentos.py --all --base-url "$BASE_URL"

echo
echo "LISTO. Solo se han GENERADO los descriptores en media_profiles/segment_sizes/."
echo "NO se commitea ni se sube nada desde aqui (de eso se encarga Claude en Windows)."
echo "Pega la linea que empieza por: SEGMENT_SIZE_EXTRACTION status=..."
