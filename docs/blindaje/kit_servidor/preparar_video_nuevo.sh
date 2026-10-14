#!/usr/bin/env bash
# Prepara en la VM servidor el video nuevo de la evaluacion final (fase de blindaje):
# Tears of Steel, (CC) Blender Foundation | mango.blender.org, licencia CC-BY 3.0.
#
# Pasos, con las mismas herramientas que los cuatro videos ya servidos:
#   1. descarga el original oficial (zip de 583 774 281 bytes) y lo descomprime;
#   2. master: primeros 10 minutos a 30 fps, H.264, sin audio (mismos ajustes de ffmpeg
#      que scripts/1_contenido/herramienta_video.sh; el audio se descarta igual en el paso 3);
#   3. scripts/1_contenido/generar_dash_lote.sh en una carpeta aparte que solo contiene
#      este video (asi no se toca ningun video ya servido). Se usa la imagen de GPAC ya
#      instalada, sin actualizarla, para empaquetar con la misma version que los demas;
#   4. publica la carpeta en /var/www/html/dash sin sobrescribir nada;
#   5. comprueba que el MPD responde y cuenta los segmentos.
#
# Uso (en la VM servidor, con los dos scripts copiados en ~/):
#   bash ~/preparar_video_nuevo.sh
set -euo pipefail

NOMBRE="Tears_of_Steel_10min_30fps"
URL_ZIP="https://download.blender.org/demo/movies/ToS/tears_of_steel_1080p.mov.zip"
BYTES_ZIP=583774281
DURACION_S=600
FPS=30
TRABAJO="$HOME/tfg_video_nuevo"
LOTE="$TRABAJO/lote"
WEB="/var/www/html/dash"
REFERENCIA="$WEB/Paseo_Almunecar_10min_30fps"
GENERADOR_ORIGINAL="$HOME/generar_dash_lote.sh"
IMAGEN_GPAC="jjlin/gpac:latest"

fallo() { echo "FALLO: $1"; exit 1; }
paso() { echo; echo "== $1"; }

paso "0/6 Comprobaciones previas"
for herramienta in curl ffmpeg ffprobe docker sudo python3 sha256sum; do
  command -v "$herramienta" >/dev/null 2>&1 || fallo "falta $herramienta"
done
[ -f "$GENERADOR_ORIGINAL" ] || fallo "no esta $GENERADOR_ORIGINAL (copialo junto a este script)"
# Pide la contrasena de sudo una vez y la mantiene viva mientras dura la codificacion.
sudo -v || fallo "hace falta sudo"
( while true; do sudo -n true; sleep 60; done ) 2>/dev/null &
MANTENER_SUDO=$!
trap 'kill $MANTENER_SUDO 2>/dev/null' EXIT
[ -d "$REFERENCIA" ] || fallo "no existe $REFERENCIA: ¿es esta la VM servidor?"
[ ! -e "$WEB/$NOMBRE" ] || fallo "$WEB/$NOMBRE ya existe; no se sobrescribe (si quieres rehacerlo, apartalo tu antes)"
sudo docker image inspect "$IMAGEN_GPAC" >/dev/null 2>&1 || fallo "la imagen $IMAGEN_GPAC no esta instalada"
mkdir -p "$TRABAJO/descarga" "$LOTE/$NOMBRE"
libre_gb=$(df -BG --output=avail "$TRABAJO" | tail -1 | tr -dc '0-9')
[ "$libre_gb" -ge 8 ] || fallo "hacen falta unos 8 GB libres en $TRABAJO (hay ${libre_gb} GB)"
echo "   OK (${libre_gb} GB libres)"

paso "1/6 Descarga del original (unos 557 MiB)"
ZIP="$TRABAJO/descarga/tears_of_steel_1080p.mov.zip"
if [ ! -f "$ZIP" ] || [ "$(stat -c %s "$ZIP")" != "$BYTES_ZIP" ]; then
  curl -fL --retry 3 -C - -o "$ZIP" "$URL_ZIP" || fallo "la descarga ha fallado"
fi
[ "$(stat -c %s "$ZIP")" = "$BYTES_ZIP" ] || fallo "el zip no mide $BYTES_ZIP bytes"
echo "   sha256 del zip: $(sha256sum "$ZIP" | cut -d' ' -f1)"

paso "2/6 Descompresion"
MOV="$TRABAJO/descarga/tears_of_steel_1080p.mov"
if [ ! -f "$MOV" ]; then
  python3 -m zipfile -e "$ZIP" "$TRABAJO/descarga/" || fallo "no se pudo descomprimir"
  encontrado=$(find "$TRABAJO/descarga" -name "*.mov" | head -1)
  [ -n "$encontrado" ] || fallo "el zip no contiene un .mov"
  [ "$encontrado" = "$MOV" ] || mv "$encontrado" "$MOV"
fi
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,r_frame_rate:format=duration \
  -of default=noprint_wrappers=1 "$MOV" | sed 's/^/   original: /'

paso "3/6 Master: primeros ${DURACION_S} s a ${FPS} fps, sin audio"
MASTER="$LOTE/$NOMBRE/$NOMBRE.mp4"
if [ ! -f "$MASTER" ]; then
  ffmpeg -y -hide_banner -loglevel error -ss 0 -i "$MOV" -t "$DURACION_S" -r "$FPS" \
    -c:v libx264 -preset fast -profile:v high -pix_fmt yuv420p -an -movflags +faststart "$MASTER" \
    || fallo "ffmpeg no pudo crear el master"
fi
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate:format=duration \
  -of default=noprint_wrappers=1 "$MASTER" | sed 's/^/   master: /'

paso "4/6 Representaciones y MPD con generar_dash_lote.sh (la parte larga, unos 30-60 min)"
# Copia del generador sin la linea "docker pull": se empaqueta con la version de GPAC ya
# instalada, la misma con la que se empaquetaron los cuatro videos del experimento. Tambien
# se quitan los finales de linea de Windows (la copia del material los tiene).
sed -e 's/\r$//' -e '/docker pull/d' "$GENERADOR_ORIGINAL" > "$TRABAJO/generar_dash_lote_sin_pull.sh"
echo "   GPAC: $(sudo docker run --rm "$IMAGEN_GPAC" MP4Box -version 2>&1 | head -1)"
echo "   imagen: $(sudo docker image inspect --format '{{.Id}}' "$IMAGEN_GPAC")"
if [ ! -f "$LOTE/$NOMBRE/4sec/${NOMBRE}_simple_4s.mpd" ]; then
  (cd "$LOTE" && bash "$TRABAJO/generar_dash_lote_sin_pull.sh") || fallo "generar_dash_lote.sh ha fallado"
fi
[ -f "$LOTE/$NOMBRE/4sec/${NOMBRE}_simple_4s.mpd" ] || fallo "no se genero el MPD de 4 s"

paso "5/6 Publicacion en $WEB (sin sobrescribir)"
sudo cp -a "$LOTE/$NOMBRE" "$WEB/$NOMBRE"
sudo chown -R --reference="$REFERENCIA" "$WEB/$NOMBRE"
sudo chmod -R a+rX "$WEB/$NOMBRE"
echo "   OK: $WEB/$NOMBRE"

paso "6/6 Comprobacion"
MPD_URL="http://localhost/dash/$NOMBRE/4sec/${NOMBRE}_simple_4s.mpd"
codigo=$(curl -s -o /dev/null -w "%{http_code}" "$MPD_URL")
[ "$codigo" = "200" ] || fallo "el MPD no responde por HTTP ($codigo)"
for carpeta in "$WEB/$NOMBRE"/4sec/chunk_*bps; do
  echo "   $(basename "$carpeta"): $(ls "$carpeta" | grep -c '\.m4s$') segmentos"
done
echo
echo "VIDEO NUEVO CORRECTO. MPD: http://192.168.1.132/dash/$NOMBRE/4sec/${NOMBRE}_simple_4s.mpd"
echo "Pega esta salida a Claude. Si quieres liberar espacio: rm -rf $TRABAJO/descarga"
