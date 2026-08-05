#!/usr/bin/env bash
# Script REAL usado para preparar los masters de video del experimento
# (aportado por Daniel el 05/08/2026): recortar a 10min/1min, convertir a
# 30 fps (las variantes 30fps salen del master 60fps) y normalizar a MP4
# H.264 limpio antes de pasar por generar_dash_lote.sh.
# ==========================================
# video_tool.sh
# Herramienta interactiva profesional vídeo
# ==========================================

set -euo pipefail

need() { command -v "$1" >/dev/null 2>&1 || { echo "❌ Falta $1"; exit 1; }; }
need ffmpeg
need ffprobe

echo
echo "🔍 Buscando vídeos en el directorio actual..."
echo

# Buscar formatos comunes
mapfile -t VIDEOS < <(ls *.mp4 *.mov *.mkv *.avi 2>/dev/null || true)

if [ ${#VIDEOS[@]} -eq 0 ]; then
    echo "❌ No se encontraron vídeos en este directorio."
    exit 1
fi

# Mostrar lista numerada
for i in "${!VIDEOS[@]}"; do
    echo "$((i+1))) ${VIDEOS[$i]}"
done

echo
read -p "🎬 ¿Con qué vídeo quieres trabajar? (número): " SELECTION

INDEX=$((SELECTION-1))
INPUT="${VIDEOS[$INDEX]}"

if [ ! -f "$INPUT" ]; then
    echo "❌ Selección inválida."
    exit 1
fi

echo
echo "Has elegido: $INPUT"
echo
echo "¿Qué operación quieres realizar?"
echo "1) Convertir a 30 FPS"
echo "2) Recortar vídeo"
echo "3) Convertir a MP4 limpio (H264)"
echo
read -p "Selecciona opción (1/2/3): " OPTION

echo
read -p "📝 Nombre del archivo de salida (sin extensión): " OUTNAME
OUTFILE="${OUTNAME}.mp4"

if [ -f "$OUTFILE" ]; then
    echo "⚠️ El archivo ya existe."
    exit 1
fi

# --------------------------------------------------
# OPCIÓN 1 — Convertir a 30 FPS
# --------------------------------------------------
if [ "$OPTION" == "1" ]; then
    echo "🔄 Convirtiendo a 30 FPS..."

    ffmpeg -y -i "$INPUT" \
      -r 30 \
      -c:v libx264 -preset fast -profile:v high \
      -pix_fmt yuv420p \
      -c:a copy \
      -movflags +faststart \
      "$OUTFILE"

    echo "✅ Conversión completada."

# --------------------------------------------------
# OPCIÓN 2 — Recortar vídeo
# --------------------------------------------------
elif [ "$OPTION" == "2" ]; then
    echo
    read -p "⏱ Inicio (formato MM.SS, ej 00.00): " START
    read -p "⏱ Fin (formato MM.SS, ej 05.00): " END

    # Convertir MM.SS a segundos
    START_SEC=$(echo "$START" | awk -F. '{print ($1*60)+$2}')
    END_SEC=$(echo "$END" | awk -F. '{print ($1*60)+$2}')

    DURATION=$((END_SEC - START_SEC))

    echo "✂ Recortando desde ${START_SEC}s durante ${DURATION}s..."

    ffmpeg -y -ss "$START_SEC" -i "$INPUT" -t "$DURATION" \
      -c:v libx264 -preset fast -profile:v high \
      -pix_fmt yuv420p \
      -c:a copy \
      -movflags +faststart \
      "$OUTFILE"

    echo "✅ Recorte completado."

# --------------------------------------------------
# OPCIÓN 3 — Convertir a MP4 limpio
# --------------------------------------------------
elif [ "$OPTION" == "3" ]; then
    echo "🔄 Convirtiendo a MP4 limpio H.264..."

    ffmpeg -y -i "$INPUT" \
      -c:v libx264 -preset fast -profile:v high \
      -pix_fmt yuv420p \
      -c:a aac -b:a 192k \
      -movflags +faststart \
      "$OUTFILE"

    echo "✅ Conversión completada."

else
    echo "❌ Opción inválida."
    exit 1
fi

echo
echo "🎯 Proceso terminado correctamente."
