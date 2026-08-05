#!/usr/bin/env bash
# Recopila la informacion del entorno de una maquina del experimento para la
# seccion "componentes del experimento" (docs/defensa/componentes_experimento.md).
# Solo LEE informacion; no instala ni cambia nada.
#
# Uso:
#   bash scripts/recopilar_info_entorno.sh cliente     (VM Ubuntu cliente)
#   bash scripts/recopilar_info_entorno.sh servidor    (VM Ubuntu servidor)
#   bash scripts/recopilar_info_entorno.sh wsl         (WSL entrenamiento)
# Salida: ~/info_entorno_<etiqueta>.txt  (en WSL ademas copia a /mnt/c/...)
set -uo pipefail

ETIQUETA="${1:?falta etiqueta: cliente|servidor|wsl}"
SALIDA="$HOME/info_entorno_${ETIQUETA}.txt"

seccion() { echo; echo "=============== $1 ==============="; }

{
echo "INFORME DE ENTORNO: $ETIQUETA  ($(date '+%Y-%m-%d %H:%M'))"

seccion "SISTEMA OPERATIVO"
lsb_release -a 2>/dev/null
uname -a
echo "virtualizacion: $(systemd-detect-virt 2>/dev/null || echo desconocida)"

seccion "HARDWARE"
echo "CPU: $(grep -m1 'model name' /proc/cpuinfo | cut -d: -f2-)"
echo "nucleos visibles: $(nproc)"
free -h | head -2
df -h / | tail -1
echo "IPs: $(hostname -I 2>/dev/null)"

seccion "PYTHON Y PAQUETES PIP"
python3 --version
pip3 --version 2>/dev/null
echo "--- pip3 freeze (entorno por defecto) ---"
pip3 freeze 2>/dev/null | sort

seccion "PAQUETES DEL SISTEMA RELEVANTES (dpkg)"
dpkg -l 2>/dev/null | grep -Ei "python3(-| )|gstreamer|gir1.2-gst|apache2|nginx|ffmpeg|gpac|openssh-server" | awk '{printf "%-45s %s\n", $2, $3}'

if [ "$ETIQUETA" = "cliente" ]; then
    seccion "CLIENTE: GSTREAMER Y TORCH"
    gst-launch-1.0 --version 2>/dev/null || echo "gst-launch-1.0 no disponible"
    python3 - <<'PY' 2>/dev/null || echo "torch no importable"
import torch
print("torch:", torch.__version__)
PY
    seccion "CLIENTE: REPO Y CONFIG"
    cd "$HOME/TFG/ClienteDashTFG" 2>/dev/null && git log --oneline -1 && ls config/
fi

if [ "$ETIQUETA" = "servidor" ]; then
    seccion "SERVIDOR WEB"
    apache2 -v 2>/dev/null || /usr/sbin/apache2 -v 2>/dev/null || echo "apache2 no encontrado"
    nginx -v 2>&1 | head -1 || true
    systemctl is-active apache2 2>/dev/null && echo "apache2 ACTIVO"
    systemctl is-active nginx 2>/dev/null && echo "nginx ACTIVO"

    seccion "SERVIDOR: CONTENIDO DASH (/var/www/html/dash)"
    du -sh /var/www/html/dash 2>/dev/null
    find /var/www/html/dash -maxdepth 2 -type d 2>/dev/null | sort
    echo "--- conteo de segmentos y MPDs por video ---"
    for d in /var/www/html/dash/*/; do
        echo "$d : $(find "$d" -name '*.m4s' 2>/dev/null | wc -l) segmentos, $(find "$d" -name '*.mpd' 2>/dev/null | wc -l) MPD, $(find "$d" -name '*init*' 2>/dev/null | wc -l) inits"
    done

    seccion "SERVIDOR: UN MPD COMPLETO (formato exacto)"
    MPD=$(find /var/www/html/dash -name "*10min_30fps*simple_4s.mpd" 2>/dev/null | head -1)
    echo "fichero: $MPD"
    cat "$MPD" 2>/dev/null

    seccion "SERVIDOR: HERRAMIENTAS DE GENERACION"
    ffmpeg -version 2>/dev/null | head -1 || echo "ffmpeg no instalado"
    MP4Box -version 2>&1 | head -1 || echo "MP4Box (gpac) no instalado"

    seccion "SERVIDOR: SCRIPTS DE GENERACION ENCONTRADOS"
    find "$HOME" /var/www/html -maxdepth 4 -type f \( -name "*.sh" -o -name "*.txt" -o -name "*.md" \) 2>/dev/null | grep -vi "\.cache\|snap/" | head -30
    echo "--- contenido de los .sh encontrados en HOME (posibles scripts de generacion) ---"
    find "$HOME" -maxdepth 3 -type f -name "*.sh" 2>/dev/null | while read -r f; do
        echo; echo "### $f ###"; cat "$f"
    done

    seccion "SERVIDOR: VIDEOS FUENTE"
    find "$HOME" /var/www/html -maxdepth 4 -type f \( -name "*.mp4" -o -name "*.mkv" -o -name "*.y4m" \) ! -name "*init*" -printf "%s\t%p\n" 2>/dev/null | sort -nr | head -10
fi

if [ "$ETIQUETA" = "wsl" ]; then
    seccion "WSL: GPU / ROCM / TORCH (venv rocm721)"
    ls /dev/dxg 2>/dev/null && echo "/dev/dxg presente (GPU expuesta a WSL)"
    rocminfo 2>/dev/null | grep -m2 "Marketing Name" || echo "rocminfo no disponible"
    # shellcheck disable=SC1090
    source "$HOME/venvs/rocm721/bin/activate" 2>/dev/null && {
        python3 --version
        python3 - <<'PY'
import torch
print("torch:", torch.__version__)
print("gpu disponible:", torch.cuda.is_available())
print("gpu:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "-")
PY
        echo "--- pip freeze del venv rocm721 ---"
        pip freeze | sort
    }
fi

echo
echo "=============== FIN ==============="
} > "$SALIDA" 2>&1

echo "Informe escrito en: $SALIDA"
if [ "$ETIQUETA" = "wsl" ] && [ -d "/mnt/c/Users/danie/Documents/TFG Material" ]; then
    mkdir -p "/mnt/c/Users/danie/Documents/TFG Material/00_info_entorno"
    cp "$SALIDA" "/mnt/c/Users/danie/Documents/TFG Material/00_info_entorno/"
    echo "Copiado tambien a TFG Material/00_info_entorno/"
fi
