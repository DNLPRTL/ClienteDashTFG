#!/usr/bin/env bash
# Limpieza de ~/TFG en WSL (05/08/2026): deja solo las piezas necesarias para
# RE-ENTRENAR el modelo final y mueve todo lo demas a ~/TFG/legacy (mover, no
# borrar).
#
# QUEDA: ClienteDashTFG/, manifests_trazas/phase3/,
#        datasets_normalizados/phase3/,
#        datasets_normalizados/mpc_prudente/throughput_quantile_full_v1_multimedia/,
#        modelos/mpc_prudente/
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

# datasets de lineas cerradas/abandonadas (lo gordo: ~18 GB)
mover "$R/datasets_normalizados/phase4"
mover "$R/datasets_normalizados/phase45_v1"
mover "$R/datasets_normalizados/phase45_v3"
# datasets mpc_prudente superados (pilot y full de un solo video)
mover "$R/datasets_normalizados/mpc_prudente/throughput_quantile_pilot_paseo_almunecar_10min_30fps_4s"
mover "$R/datasets_normalizados/mpc_prudente/throughput_quantile_full_v1_paseo_almunecar_10min_30fps_4s"

mover "$R/manifests_trazas/phase4"
mover "$R/modelos/phase4"
mover "$R/modelos/phase45_v1"
mover "$R/modelos/phase45_v3"

mover "$R/runs_phase45_v3"
mover "$R/runs_mpc_prudente"
mover "$R/logs_phase45_v2"
mover "$R/runs_trazas"
mover "$R/auditorias_trazas"
mover "$R/paquetes_transfer"
mover "$R/20260611_202406_rapido"

cat > "$R/LEEME_ESTRUCTURA.md" <<'FIN'
# Estructura de ~/TFG (WSL, entrenamiento GPU) — tras la limpieza del 05/08/2026

| Carpeta | Que es |
|---|---|
| ClienteDashTFG/ | Repo del proyecto (git). Venv GPU: ~/venvs/rocm721 |
| manifests_trazas/phase3/final/ | Manifest curado (entrada del generador de datasets) |
| datasets_normalizados/phase3/ | Trazas normalizadas (entrada del generador de datasets) |
| datasets_normalizados/mpc_prudente/throughput_quantile_full_v1_multimedia/ | Dataset de ENTRENAMIENTO final (multi-video, el del modelo v2) |
| modelos/mpc_prudente/ | Entrenamientos y bundles propios (temporal_predictor = ensemble v2; runtime_bundle_v1 y temporal_runtime_bundle_v1 = bundles exportados) |
| legacy/ | Todo lo demas (lineas abandonadas, pilots, runs). Movido, no borrado |

Flujo de re-entrenamiento: generar_dataset_multimedia_mpc_prudente_wsl.sh ->
entrenar_temporal_mpc_prudente_wsl.sh -> exportar_bundle_temporal_mpc_prudente_wsl.sh
FIN
echo "== LEEME escrito en $R/LEEME_ESTRUCTURA.md =="
echo "== Limpieza WSL terminada =="
du -sh "$R"/* 2>/dev/null | sort -hr
