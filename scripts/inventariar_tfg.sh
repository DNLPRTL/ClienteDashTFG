#!/usr/bin/env bash
# Inventario de ~/TFG para la fase de ordenacion y limpieza (2026-08).
# Genera un tar.gz PEQUENO con:
#   - tamanos por carpeta (du, 3 niveles)
#   - conteo de ficheros por directorio
#   - listado de ficheros hasta profundidad 5 (tamano + fecha)
#   - copia de los metadatos ligeros (.json/.md/.yaml/.yml/.txt < 512 KB)
# NO copia datasets, trazas, modelos ni runs pesados.
#
# Uso:
#   bash scripts/inventariar_tfg.sh <etiqueta> [dir_destino]
#   p. ej.:  bash scripts/inventariar_tfg.sh ubuntu
#            bash scripts/inventariar_tfg.sh wsl /mnt/c/Users/danie/Documents/TFG/inventarios
set -euo pipefail

ETIQUETA="${1:?falta la etiqueta (ubuntu|wsl)}"
DESTINO="${2:-$HOME}"
RAIZ="$HOME/TFG"
TRABAJO="$(mktemp -d)"
SALIDA="$TRABAJO/inventario_tfg_$ETIQUETA"
mkdir -p "$SALIDA/metadatos"

echo "== Inventariando $RAIZ (etiqueta: $ETIQUETA) =="

du -h --max-depth=3 "$RAIZ" 2>/dev/null | sort -hr > "$SALIDA/tamanos_carpetas.txt"

find "$RAIZ" -xdev -type d 2>/dev/null | while read -r d; do
    n=$(find "$d" -maxdepth 1 -type f 2>/dev/null | wc -l)
    s=$(du -sb "$d" 2>/dev/null | cut -f1)
    echo -e "${n}\t${s}\t${d}"
done > "$SALIDA/directorios_conteo_y_bytes.txt"

find "$RAIZ" -maxdepth 5 -type f -printf "%s\t%TY-%Tm-%Td\t%p\n" 2>/dev/null \
    | sort -t$'\t' -k3 > "$SALIDA/ficheros_hasta_nivel5.txt"

# metadatos ligeros (sin el repo, que ya esta en git)
find "$RAIZ" -type f \
    \( -name "*.json" -o -name "*.md" -o -name "*.yaml" -o -name "*.yml" -o -name "*.txt" \) \
    -size -512k 2>/dev/null \
    | grep -v "/ClienteDashTFG/" | grep -v "/DashClientModular4/" \
    | while read -r f; do
        rel="${f#"$RAIZ"/}"
        mkdir -p "$SALIDA/metadatos/$(dirname "$rel")"
        cp "$f" "$SALIDA/metadatos/$rel" 2>/dev/null || true
    done

TAR="$DESTINO/inventario_tfg_${ETIQUETA}.tar.gz"
tar -czf "$TAR" -C "$TRABAJO" "inventario_tfg_$ETIQUETA"
rm -rf "$TRABAJO"
echo "== Inventario escrito en: $TAR =="
du -h "$TAR"
