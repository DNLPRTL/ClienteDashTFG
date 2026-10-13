#!/usr/bin/env bash
# Replica del experimento final con ventanas de evaluacion no usadas en el desarrollo.
# Se ejecuta en la VM cliente. Uso:
#   bash ~/TFG/replica_ventanas_nuevas/replica.sh comprobar   # 6 comprobaciones, no ejecuta sesiones
#   bash ~/TFG/replica_ventanas_nuevas/replica.sh lanzar      # lanza las 300 sesiones (unas 10-11 h)
#   bash ~/TFG/replica_ventanas_nuevas/replica.sh estado      # progreso y, al final, resultado de las compuertas
#   bash ~/TFG/replica_ventanas_nuevas/replica.sh reanudar    # solo si la ejecucion se corto
set -uo pipefail

KIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TFG="$HOME/TFG"
CODIGO="$TFG/ClienteDashTFG"
BUNDLE="$TFG/modelos/modelo_propio/bundle"
CATALOGO="$TFG/catalogo_trazas.json"
CONFIG="$KIT/evaluacion.replica.json"
SALIDA="$TFG/validacion_comparativa_replica"
LOG="$KIT/ejecucion_replica.log"
SERVIDOR="http://192.168.1.132/dash"
RUNNER="$CODIGO/scripts/3_evaluacion/ejecutar_evaluacion.py"
export PYTHONDONTWRITEBYTECODE=1

fallo() {
  echo "   FALLO: $1"
  echo "No lances la replica hasta corregirlo (ver LEEME.md)."
  exit 1
}

en_marcha() {
  pgrep -f "ejecutar_evaluacion.py --config $CONFIG" > /dev/null
}

comprobar() {
  echo "1/6 El codigo de la VM es identico al del material de entrega"
  (cd "$CODIGO" && sha256sum -c --quiet "$KIT/hashes_codigo_entrega.sha256") || fallo "el codigo de $CODIGO no coincide con el de entrega"
  echo "   OK"
  echo "2/6 El modelo (bundle) es identico al de 03_modelos"
  (cd "$BUNDLE" && sha256sum -c --quiet "$KIT/hashes_bundle.sha256") || fallo "el bundle de $BUNDLE no coincide"
  echo "   OK"
  echo "3/6 El catalogo de trazas es identico al de 02_corpus_red"
  (cd "$TFG" && sha256sum -c --quiet "$KIT/hashes_catalogo.sha256") || fallo "el catalogo $CATALOGO no coincide"
  echo "   OK"
  echo "4/6 El servidor DASH responde para los 4 videos"
  for v in Paseo_Almunecar_10min_30fps Blender_Sunflower_10min_30fps Paseo_Almunecar_10min_60fps Blender_Sunflower_10min_60fps; do
    codigo=$(curl -s -o /dev/null -w "%{http_code}" "$SERVIDOR/$v/4sec/${v}_simple_4s.mpd")
    [ "$codigo" = "200" ] || fallo "el MPD de $v no responde (HTTP $codigo): enciende la VM servidor"
  done
  echo "   OK"
  echo "5/6 Catalogo de la replica (sin los grupos ya evaluados)"
  python3 "$KIT/generar_catalogo_replica.py" "$CODIGO" "$CATALOGO" "$KIT/grupos_excluidos.txt" "$KIT/catalogo_trazas_replica.json" || fallo "no se pudo generar el catalogo de la replica"
  echo "6/6 Plan en seco: seleccion de ventanas sin ejecutar sesiones"
  rm -rf /tmp/replica_plan_seco
  python3 "$RUNNER" --config "$CONFIG" --raiz-salida /tmp/replica_plan_seco --solo-plan > /tmp/replica_plan_seco.log 2>&1 || fallo "el plan en seco fallo (ver /tmp/replica_plan_seco.log)"
  plan=$(ls -d /tmp/replica_plan_seco/*/ | head -1)
  python3 "$KIT/comparar_ventanas.py" "${plan}00_protocolo/ventanas_trazas.csv" "$KIT/ventanas_esperadas.txt" || fallo "las ventanas seleccionadas no son las esperadas"
  echo
  echo "TODO CORRECTO. Lanza la replica con: bash $KIT/replica.sh lanzar"
}

lanzar() {
  [ -f "$KIT/catalogo_trazas_replica.json" ] || fallo "ejecuta antes: bash $KIT/replica.sh comprobar"
  en_marcha && fallo "ya hay una replica en marcha (bash $KIT/replica.sh estado)"
  nohup python3 "$RUNNER" --config "$CONFIG" > "$LOG" 2>&1 &
  echo "Replica lanzada (PID $!). Dura unas 10-11 horas."
  echo "Puedes cerrar la terminal, pero NO apagues ni suspendas el PC ni las VM."
  echo "Seguimiento: bash $KIT/replica.sh estado"
}

estado() {
  if en_marcha; then echo "Estado: EN MARCHA"; else echo "Estado: PARADA"; fi
  grep PROGRESO_EVALUACION "$LOG" 2>/dev/null | tail -1 | sed 's/^PROGRESO_EVALUACION /Progreso: /'
  paquete=$(ls -d "$SALIDA"/*/ 2>/dev/null | tail -1)
  [ -n "$paquete" ] && echo "Paquete: $paquete"
  if ! en_marcha && [ -n "$paquete" ] && [ -f "${paquete}02_resultados/resumen_resultados.md" ]; then
    grep -m1 "Gates superados" "${paquete}02_resultados/resumen_resultados.md"
    tail -4 "$LOG"
  fi
}

reanudar() {
  en_marcha && fallo "la replica sigue en marcha; no hace falta reanudar"
  paquete=$(ls -d "$SALIDA"/*/ 2>/dev/null | tail -1)
  [ -n "$paquete" ] || fallo "no hay ningun paquete que reanudar en $SALIDA"
  nohup python3 "$RUNNER" --config "$CONFIG" --raiz-paquete "$paquete" >> "$LOG" 2>&1 &
  echo "Replica reanudada sobre $paquete (PID $!): las sesiones completadas se omiten."
}

case "${1:-}" in
  comprobar) comprobar ;;
  lanzar) lanzar ;;
  estado) estado ;;
  reanudar) reanudar ;;
  *) echo "Uso: bash $0 comprobar|lanzar|estado|reanudar"; exit 2 ;;
esac
