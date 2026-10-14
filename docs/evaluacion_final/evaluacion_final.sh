#!/usr/bin/env bash
# Comprobaciones de la evaluacion final en la VM cliente. El experimento se lanza como siempre,
# desde la interfaz grafica. Uso:
#   bash ~/TFG/evaluacion_final/evaluacion_final.sh comprobar   # 7 comprobaciones, no ejecuta sesiones
#   bash ~/TFG/evaluacion_final/evaluacion_final.sh humo        # 5 sesiones reales de prueba en /tmp (unos 11 min)
#   bash ~/TFG/evaluacion_final/evaluacion_final.sh estado      # avance del experimento y, al final, compuertas
set -uo pipefail

KIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TFG="$HOME/TFG"
CODIGO="$TFG/ClienteDashTFG"
BUNDLE="$TFG/modelos/modelo_propio/bundle"
SALIDA="$TFG/validacion_comparativa"
SERVIDOR="http://192.168.1.132/dash"
RUNNER="$CODIGO/scripts/3_evaluacion/ejecutar_evaluacion.py"
export PYTHONDONTWRITEBYTECODE=1

fallo() {
  echo "   FALLO: $1"
  echo "No lances el experimento hasta corregirlo (ver LEEME.md)."
  exit 1
}

comprobar() {
  echo "1/7 El codigo de la VM es identico al del material de entrega (version final)"
  (cd "$CODIGO" && sha256sum -c --quiet "$KIT/hashes_codigo_final.sha256") || fallo "el codigo de $CODIGO no coincide"
  echo "   OK"
  echo "2/7 El modelo (bundle) es identico al de 03_modelos"
  (cd "$BUNDLE" && sha256sum -c --quiet "$KIT/hashes_bundle.sha256") || fallo "el bundle no coincide"
  echo "   OK"
  echo "3/7 El catalogo de trazas es identico al de 02_corpus_red"
  (cd "$TFG" && sha256sum -c --quiet "$KIT/hashes_catalogo.sha256") || fallo "el catalogo no coincide"
  echo "   OK"
  echo "4/7 Python tiene numpy y torch"
  python3 -c "import numpy, torch; print('   numpy', numpy.__version__, '| torch', torch.__version__)" || fallo "falta numpy o torch"
  echo "5/7 El servidor DASH responde para los 4 videos"
  for v in Paseo_Almunecar_10min_30fps Blender_Sunflower_10min_30fps Paseo_Almunecar_10min_60fps Blender_Sunflower_10min_60fps; do
    codigo=$(curl -s -o /dev/null -w "%{http_code}" "$SERVIDOR/$v/4sec/${v}_simple_4s.mpd")
    [ "$codigo" = "200" ] || fallo "el MPD de $v no responde (HTTP $codigo): enciende la VM servidor"
  done
  echo "   OK"
  echo "6/7 Plan en seco con la configuracion de siempre: ventanas esperadas"
  rm -rf /tmp/final_plan_seco
  python3 "$RUNNER" --raiz-salida /tmp/final_plan_seco --solo-plan > /tmp/final_plan_seco.log 2>&1 || fallo "el plan en seco fallo (ver /tmp/final_plan_seco.log)"
  plan=$(ls -d /tmp/final_plan_seco/*/ | head -1)
  python3 "$KIT/comparar_ventanas.py" "${plan}00_protocolo/ventanas_trazas.csv" "$KIT/ventanas_esperadas_final.txt" || fallo "las ventanas no son las esperadas"
  echo "7/7 Velocidad del planificador en esta VM"
  (cd "$CODIGO" && python3 "$KIT/medir_planificador.py") || fallo "el planificador no funciona"
  echo
  echo "TODO CORRECTO. Siguiente paso: bash $KIT/evaluacion_final.sh humo"
}

humo() {
  rm -rf /tmp/final_humo
  echo "Ejecutando 5 sesiones reales (los 5 controladores en la primera ventana), unos 11 minutos..."
  python3 "$RUNNER" --raiz-salida /tmp/final_humo --max-sesiones 5 > /tmp/final_humo.log 2>&1
  paquete=$(ls -d /tmp/final_humo/*/ | head -1)
  python3 "$KIT/resumen_humo.py" "$paquete" || fallo "la prueba de humo no es correcta (ver /tmp/final_humo.log)"
  echo
  echo "HUMO CORRECTO. Ya puedes lanzar el experimento desde la interfaz grafica (ver LEEME.md)."
}

estado() {
  paquete=$(ls -d "$SALIDA"/*_tfg_final/ 2>/dev/null | tail -1)
  [ -n "$paquete" ] || { echo "Todavia no hay ningun paquete tfg_final en $SALIDA"; exit 0; }
  echo "Paquete: $paquete"
  completadas=$(grep -l '"estado": "completado"' "${paquete}"01_ejecucion/ejecuciones/*/ejecucion_*/manifiesto_ejecucion.json 2>/dev/null | wc -l)
  echo "Sesiones completadas: $completadas de 300"
  if [ -f "${paquete}02_resultados/resumen_resultados.md" ]; then
    grep -m1 "Gates superados" "${paquete}02_resultados/resumen_resultados.md"
    grep -m1 "Veredicto" "${paquete}02_resultados/verificacion_paquete.md"
  fi
}

case "${1:-}" in
  comprobar) comprobar ;;
  humo) humo ;;
  estado) estado ;;
  *) echo "Uso: bash $0 comprobar|humo|estado"; exit 2 ;;
esac
