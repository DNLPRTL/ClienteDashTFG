#!/usr/bin/env bash
# Kit de la VM cliente para la fase de blindaje. Uso:
#   bash ~/TFG/kit_vm/blindaje_vm.sh comprobar   # instala los cuantiles fijos y hace 8 comprobaciones
#   bash ~/TFG/kit_vm/blindaje_vm.sh humo        # 8 sesiones reales de prueba en /tmp (unos 20 min)
#   bash ~/TFG/kit_vm/blindaje_vm.sh previa      # prueba corta sobre validacion, 160 sesiones (unas 6,5 h)
#   bash ~/TFG/kit_vm/blindaje_vm.sh estado      # avance de la prueba corta y como copiarla a Windows
set -uo pipefail

KIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TFG="$HOME/TFG"
CODIGO="$TFG/ClienteDashTFG"
BUNDLE="$TFG/modelos/modelo_propio/bundle"
CUANTILES="$TFG/modelos/cuantiles_fijos"
SALIDA="$TFG/validacion_comparativa"
SERVIDOR="http://192.168.1.132/dash"
RUNNER="$CODIGO/scripts/3_evaluacion/ejecutar_evaluacion.py"
export PYTHONDONTWRITEBYTECODE=1

fallo() {
  echo "   FALLO: $1"
  echo "Para aqui y pega esta salida a Claude."
  exit 1
}

comprobar() {
  echo "1/8 El codigo de la VM es identico al del material de entrega"
  (cd "$CODIGO" && sha256sum -c --quiet "$KIT/hashes_codigo.sha256") || fallo "el codigo de $CODIGO no coincide"
  echo "   OK"
  echo "2/8 El modelo (bundle) es identico al de 03_modelos"
  (cd "$BUNDLE" && sha256sum -c --quiet "$KIT/hashes_bundle.sha256") || fallo "el bundle no coincide"
  echo "   OK"
  echo "3/8 El catalogo de trazas es identico al de 02_corpus_red"
  (cd "$TFG" && sha256sum -c --quiet "$KIT/hashes_catalogo.sha256") || fallo "el catalogo no coincide"
  echo "   OK"
  echo "4/8 Cuantiles fijos instalados en $CUANTILES"
  mkdir -p "$CUANTILES" && cp "$KIT/cuantiles_fijos.json" "$CUANTILES/cuantiles_fijos.json"
  (cd "$CUANTILES" && sha256sum -c --quiet "$KIT/hashes_cuantiles_fijos.sha256") || fallo "los cuantiles fijos no coinciden"
  echo "   OK"
  echo "5/8 Python tiene numpy y torch"
  python3 -c "import numpy, torch; print('   numpy', numpy.__version__, '| torch', torch.__version__)" || fallo "falta numpy o torch"
  echo "6/8 El servidor DASH responde para los 5 videos"
  for v in Paseo_Almunecar_10min_30fps Blender_Sunflower_10min_30fps Paseo_Almunecar_10min_60fps Blender_Sunflower_10min_60fps Tears_of_Steel_10min_30fps; do
    codigo=$(curl -s -o /dev/null -w "%{http_code}" "$SERVIDOR/$v/4sec/${v}_simple_4s.mpd")
    [ "$codigo" = "200" ] || fallo "el MPD de $v no responde (HTTP $codigo): enciende la VM servidor"
  done
  echo "   OK"
  echo "7/8 Plan en seco: ventanas esperadas de la prueba corta y del experimento final"
  for p in previa_vm final_blindaje; do
    rm -rf "/tmp/plan_seco_$p"
    python3 "$RUNNER" --preset "$p" --raiz-salida "/tmp/plan_seco_$p" --solo-plan > "/tmp/plan_seco_$p.log" 2>&1 || fallo "el plan en seco de $p fallo (ver /tmp/plan_seco_$p.log)"
    plan=$(ls -d /tmp/plan_seco_$p/*/ | head -1)
    esperadas="$KIT/ventanas_esperadas_previa.txt"
    [ "$p" = "final_blindaje" ] && esperadas="$KIT/ventanas_esperadas_final.txt"
    python3 "$KIT/comparar_ventanas.py" "${plan}00_protocolo/ventanas_trazas.csv" "$esperadas" || fallo "las ventanas de $p no son las esperadas"
  done
  echo "8/8 Los 8 controladores se crean con los 5 videos y el planificador es rapido"
  (cd "$CODIGO" && python3 "$KIT/comprobar_controladores.py") || fallo "algun controlador no se crea"
  echo
  echo "TODO CORRECTO. Siguiente paso: bash $KIT/blindaje_vm.sh humo"
}

humo() {
  rm -rf /tmp/blindaje_humo
  echo "Ejecutando 8 sesiones reales (los 8 controladores en la primera ventana de la prueba corta), unos 20 minutos..."
  python3 "$RUNNER" --preset previa_vm --raiz-salida /tmp/blindaje_humo --max-sesiones 8 > /tmp/blindaje_humo.log 2>&1
  paquete=$(ls -d /tmp/blindaje_humo/*/ | head -1)
  python3 "$KIT/resumen_humo.py" "$paquete" || fallo "la prueba de humo no es correcta (ver /tmp/blindaje_humo.log)"
  echo
  echo "HUMO CORRECTO. Siguiente paso: bash $KIT/blindaje_vm.sh previa"
}

previa() {
  if pgrep -f "ejecutar_evaluacion.py --preset previa_vm" > /dev/null; then
    echo "La prueba corta ya esta en marcha. Mira el avance con: bash $KIT/blindaje_vm.sh estado"
    exit 0
  fi
  nohup python3 "$RUNNER" --preset previa_vm > "$TFG/previa_vm.log" 2>&1 &
  sleep 20
  echo "Prueba corta lanzada en segundo plano (160 sesiones, unas 6,5 horas). Puedes cerrar esta terminal."
  echo "Por la manana: bash $KIT/blindaje_vm.sh estado"
}

estado() {
  paquete=$(ls -d "$SALIDA"/*_previa_vm/ 2>/dev/null | tail -1)
  [ -n "$paquete" ] || { echo "Todavia no hay ningun paquete previa_vm en $SALIDA"; exit 0; }
  completadas=$(grep -l '"estado": "completado"' "${paquete}"01_ejecucion/ejecuciones/*/ejecucion_*/manifiesto_ejecucion.json 2>/dev/null | wc -l)
  echo "Paquete: $paquete"
  echo "Sesiones completadas: $completadas de 160"
  if pgrep -f "ejecutar_evaluacion.py --preset previa_vm" > /dev/null; then
    echo "Sigue en marcha."
  else
    echo "Terminado. En Windows (PowerShell), copialo con:"
    echo "scp -r daniel@192.168.1.160:${paquete%/} \"C:\\Users\\danie\\Documents\\TFG\\legacy\\evidencia_desarrollo\\\""
  fi
}

case "${1:-}" in
  comprobar) comprobar ;;
  humo) humo ;;
  previa) previa ;;
  estado) estado ;;
  *) echo "Uso: bash $0 comprobar|humo|previa|estado"; exit 2 ;;
esac
