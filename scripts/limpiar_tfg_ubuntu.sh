#!/usr/bin/env bash
# Limpieza de ~/TFG en el UBUNTU CLIENTE (05/08/2026): deja solo las piezas
# imprescindibles para replicar el experimento final y mueve TODO lo demas a
# ~/TFG/legacy (mover, no borrar). Ademas recoloca el paquete final en su ruta
# canonica: runs_trazas/phase6/validacion_comparativa/20260624_182747_tfg_final.
#
# QUEDA: ClienteDashTFG/, manifests_trazas/phase3/final/,
#        datasets_normalizados/phase3/, modelos/mpc_prudente/,
#        runs_trazas/phase6/validacion_comparativa/20260624_182747_tfg_final/
set -euo pipefail
R="$HOME/TFG"
L="$R/legacy"
mkdir -p "$L"

mover() {
    if [ -e "$1" ]; then
        rel="${1#"$R"/}"
        mkdir -p "$L/$(dirname "$rel")"
        mv "$1" "$L/$rel"
        echo "legacy <- $rel"
    fi
}

# fases cerradas / lineas abandonadas
mover "$R/datasets_normalizados/phase4"
mover "$R/manifests_trazas/phase4"
mover "$R/modelos/phase4"
mover "$R/modelos/phase45_v1"
mover "$R/modelos/phase45_v3"
mover "$R/auditorias_trazas"

# runs historicos de fases cerradas
mover "$R/runs_trazas/fase_verificacion_cliente_y_controllers_clasicos"
mover "$R/runs_trazas/phase3"
mover "$R/runs_trazas/phase3_5"
mover "$R/runs_trazas/phase4"
mover "$R/runs_trazas/phase5"

# paquetes phase6 antiguos (diagnosticos/rapidos/etc. previos al final)
mover "$R/runs_trazas/phase6/validacion_comparativa_mpc_prudente"
mover "$R/runs_trazas/phase6/validacion_comparativa_mpc_prudente_v1_v2"
for d in "$R"/runs_trazas/phase6/validacion_comparativa/2026*; do
    [ -e "$d" ] || continue
    case "$(basename "$d")" in
        20260624_182747_tfg_final) ;;
        *) mover "$d" ;;
    esac
done

# recolocar el paquete FINAL en su ruta canonica y retirar la carpeta smoke
if [ -d "$R/runs_trazas/phase6/tfg_final_smoke24/20260624_182747_tfg_final" ]; then
    mv "$R/runs_trazas/phase6/tfg_final_smoke24/20260624_182747_tfg_final" \
       "$R/runs_trazas/phase6/validacion_comparativa/"
    echo "RECOLOCADO -> runs_trazas/phase6/validacion_comparativa/20260624_182747_tfg_final"
fi
mover "$R/runs_trazas/phase6/tfg_final_smoke24"

# inventario temporal de la limpieza
[ -f "$HOME/inventario_tfg_ubuntu.tar.gz" ] && mv "$HOME/inventario_tfg_ubuntu.tar.gz" "$L/"

cat > "$R/LEEME_ESTRUCTURA.md" <<'FIN'
# Estructura de ~/TFG (Ubuntu cliente) — tras la limpieza del 05/08/2026

| Carpeta | Que es |
|---|---|
| ClienteDashTFG/ | Repo del proyecto (git). Config local: config/phase6.local.json |
| manifests_trazas/phase3/final/ | Manifest CURADO del corpus de trazas (el que usa Phase 6) |
| datasets_normalizados/phase3/ | Trazas de red normalizadas (CSV que reproduce el cliente) |
| modelos/mpc_prudente/ | Bundles de los modelos propios: runtime_bundle_v1 (MLP) y temporal_runtime_bundle_v1 (v2, el del resultado final) |
| runs_trazas/phase6/validacion_comparativa/20260624_182747_tfg_final/ | EVIDENCIA FINAL (360 sesiones). Ruta canonica |
| runs_trazas/phase6/validacion_comparativa/_gui_configs/ | Configs guardadas por la GUI |
| legacy/ | Todo lo demas (fases cerradas, pilots, paquetes antiguos). Movido, no borrado |
FIN
echo "== LEEME escrito en $R/LEEME_ESTRUCTURA.md =="
echo "== Limpieza Ubuntu terminada =="
du -sh "$R"/* 2>/dev/null | sort -hr
