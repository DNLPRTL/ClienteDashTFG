#!/usr/bin/env bash
# Script REAL usado en la VM servidor para generar el contenido DASH del
# experimento (aportado por Daniel el 05/08/2026). Se ejecuta en el directorio
# padre que contiene una carpeta por video (cada una con su master .mp4).
# Salida por carpeta: _reps_<video>/ (6 representaciones VBR) + 2sec/ y 4sec/
# (segmentos .m4s + MPD). El experimento final usa la variante de 4 s.
# ============================================================
# DASH BATCH TOOL — ORDEN REAL GARANTIZADO (carpeta por carpeta)
# - Ejecuta en el directorio "padre" que contiene N carpetas
# - En cada carpeta busca 1 mp4 (si hay varios, coge el primero)
# - Genera _reps_*, y MPDs 2s y 4s (en 2sec/ y 4sec/)
# - Mantiene la lógica del test que funciona (bandwidth forzado)
# ============================================================

set -euo pipefail

IMG="jjlin/gpac:latest"

need() { command -v "$1" >/dev/null 2>&1 || { echo "❌ Falta $1"; exit 1; }; }

need ffmpeg
need ffprobe
need docker
need sudo
need python3

# ORDEN MAYOR → MENOR (mismo ladder que tu test)
LADDER=(
"1920 1080 4300"
"1280 720 2850"
"854 480 1850"
"640 360 1200"
"426 240 750"
"256 144 300"
)

BASE_DIR="$(pwd)"

echo "📁 Directorio base: $BASE_DIR"
echo "🐳 Verificando imagen Docker (si tarda, es normal la primera vez)..."
sudo docker pull "$IMG" >/dev/null 2>&1 || true
echo "   ✔ OK"
echo

# Procesa todas las carpetas directas dentro del directorio base
shopt -s nullglob
DIRS=( "$BASE_DIR"/*/ )
shopt -u nullglob

if [ ${#DIRS[@]} -eq 0 ]; then
  echo "❌ No hay subcarpetas dentro de: $BASE_DIR"
  exit 1
fi

echo "🔍 Encontradas ${#DIRS[@]} carpetas."
echo

for DIR in "${DIRS[@]}"; do
  echo "============================================================"
  echo "📦 Procesando carpeta: $DIR"
  echo "============================================================"

  cd "$DIR"

  # Buscar mp4(s) en la carpeta (no entra en subcarpetas)
  shopt -s nullglob
  MP4S=( *.mp4 )
  shopt -u nullglob

  if [ ${#MP4S[@]} -eq 0 ]; then
    echo "⚠️  No hay .mp4 en esta carpeta. Saltando..."
    echo
    cd "$BASE_DIR"
    continue
  fi

  if [ ${#MP4S[@]} -gt 1 ]; then
    echo "⚠️  Hay varios mp4. Usaré el primero:"
    echo "    → ${MP4S[0]}"
  fi

  INPUT="${MP4S[0]}"
  BASENAME="${INPUT%.*}"
  REPS_DIR="_reps_${BASENAME}"

  echo
  echo "🎞 Input: $INPUT"
  echo "📂 REPS:  $REPS_DIR"

  # Limpiar outputs previos
  rm -rf "$REPS_DIR" "2sec" "4sec"
  mkdir -p "$REPS_DIR"

  # Detectar FPS (redondeado)
  FPS_RAW=$(ffprobe -v error -select_streams v:0 \
      -show_entries stream=r_frame_rate \
      -of default=nokey=1:noprint_wrappers=1 "$INPUT")

  FPS=$(python3 - <<EOF
num,den="$FPS_RAW".split("/")
print(round(float(num)/float(den)))
EOF
  )

  if [ -z "${FPS:-}" ] || [ "$FPS" -le 0 ]; then
    echo "❌ No se pudo detectar FPS correctamente. Saltando carpeta."
    echo
    cd "$BASE_DIR"
    continue
  fi

  KEYINT=$((FPS*2))
  echo "🎥 FPS: $FPS | GOP: $KEYINT (2s)"

  echo
  echo "🚀 Generando representations..."

  for ENTRY in "${LADDER[@]}"; do
      read -r W H BR <<< "$ENTRY"
      OUT="${REPS_DIR}/${BASENAME}_${H}p_${BR}k.mp4"

      echo "→ ${W}x${H} @ ${BR}k"

      ffmpeg -y -hide_banner -loglevel error -i "$INPUT" \
          -vf "scale=${W}:${H}:force_original_aspect_ratio=decrease,\
pad=${W}:${H}:(ow-iw)/2:(oh-ih)/2,setsar=1,setdar=16/9" \
          -c:v libx264 \
          -preset slow \
          -profile:v high \
          -pix_fmt yuv420p \
          -b:v ${BR}k \
          -maxrate ${BR}k \
          -bufsize $((2*BR))k \
          -x264-params keyint=${KEYINT}:min-keyint=${KEYINT}:scenecut=0 \
          -movflags +faststart \
          -an \
          "$OUT"
  done

  echo "✅ Representations generadas."

  # Construir lista explícita con bandwidth forzado (ORDEN REAL)
  INPUTS=()
  for ENTRY in "${LADDER[@]}"; do
      read -r W H BR <<< "$ENTRY"
      FILE="${REPS_DIR}/${BASENAME}_${H}p_${BR}k.mp4"
      if [ ! -f "$FILE" ]; then
        echo "❌ Falta rep esperada: $FILE"
        echo "   Saltando generación de MPD en esta carpeta."
        INPUTS=()
        break
      fi
      INPUTS+=( "/data/${FILE}#video:bandwidth=$((BR*1000))" )
  done

  if [ ${#INPUTS[@]} -ne 6 ]; then
    echo
    cd "$BASE_DIR"
    continue
  fi

  for S in 2 4; do
      echo
      echo "📦 Generando MPD ${S}s..."

      OUTDIR="${S}sec"
      rm -rf "$OUTDIR"
      mkdir -p "$OUTDIR"

      sudo docker run --rm \
          -u "$(id -u)":"$(id -g)" \
          -v "$(pwd)":/data \
          "$IMG" \
          MP4Box \
          -dash $((S*1000)) \
          -frag $((S*1000)) \
          -rap \
          -profile live \
          -bs-switching no \
          -segment-ext m4s \
          -segment-name "chunk_\$Bandwidth\$bps/${BASENAME}_${S}s" \
          -init-seg "chunk_\$Bandwidth\$bps/${BASENAME}_${S}s_init.mp4" \
          -out "/data/${OUTDIR}/${BASENAME}_simple_${S}s.mpd" \
          "${INPUTS[@]}"

      echo "✔ MPD ${S}s generado → ${OUTDIR}/${BASENAME}_simple_${S}s.mpd"
  done

  echo
  echo "🎓 OK carpeta: $DIR"
  echo "   Orden esperado:"
  echo "   id=1 → 1080p"
  echo "   id=2 → 720p"
  echo "   id=3 → 480p"
  echo "   id=4 → 360p"
  echo "   id=5 → 240p"
  echo "   id=6 → 144p"
  echo

  cd "$BASE_DIR"
done

echo "✅ Terminado. Carpeta por carpeta procesada."
