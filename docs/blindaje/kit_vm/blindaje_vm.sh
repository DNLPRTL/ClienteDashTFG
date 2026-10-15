#!/usr/bin/env bash
# Kit de la VM cliente para la fase de blindaje. Uso:
#   bash ~/TFG/kit_vm/blindaje_vm.sh comprobar   # instala los cuantiles fijos y hace 9 comprobaciones
#   bash ~/TFG/kit_vm/blindaje_vm.sh humo        # 8 sesiones reales de prueba en /tmp (unos 20 min)
#   bash ~/TFG/kit_vm/blindaje_vm.sh final       # experimento final, 1208 sesiones (unas 42 h)
#   bash ~/TFG/kit_vm/blindaje_vm.sh estado      # avance del experimento y como copiarlo a Windows
#   bash ~/TFG/kit_vm/blindaje_vm.sh reanudar    # continua el experimento final si se corto
#   bash ~/TFG/kit_vm/blindaje_vm.sh previa      # prueba corta sobre validacion (ya hecha el 14/10)
set -uo pipefail

KIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TFG="$HOME/TFG"
CODIGO="$TFG/ClienteDashTFG"
BUNDLE="$TFG/modelos/modelo_propio/bundle"
CUANTILES="$TFG/modelos/cuantiles_fijos"
SALIDA="$TFG/validacion_comparativa"
SERVIDOR="http://192.168.1.132/dash"
RUNNER="$CODIGO/scripts/3_evaluacion/ejecutar_evaluacion.py"
LOG_FINAL="$TFG/final_blindaje.log"
export PYTHONDONTWRITEBYTECODE=1

fallo() {
  echo "   FALLO: $1"
  echo "Para aqui y pega esta salida a Claude."
  exit 1
}

en_marcha() {
  pgrep -f "ejecutar_evaluacion.py --preset $1" > /dev/null
}

comprobar() {
  echo "1/9 El codigo de la VM es identico al del material de entrega"
  (cd "$CODIGO" && sha256sum -c --quiet "$KIT/hashes_codigo.sha256") || fallo "el codigo de $CODIGO no coincide"
  sobran=$(cd "$CODIGO" && find . -type f -not -path "*/__pycache__/*" -not -path "./.idea/*" -not -path "*/.ruff_cache/*" | sort \
    | comm -23 - <(awk '{print $2}' "$KIT/hashes_codigo.sha256" | sort))
  [ -z "$sobran" ] || fallo "sobran ficheros de una version anterior en $CODIGO: $sobran"
  echo "   OK"
  echo "2/9 El modelo (bundle) es identico al de 03_modelos"
  (cd "$BUNDLE" && sha256sum -c --quiet "$KIT/hashes_bundle.sha256") || fallo "el bundle no coincide"
  echo "   OK"
  echo "3/9 El catalogo de trazas es identico al de 02_corpus_red"
  (cd "$TFG" && sha256sum -c --quiet "$KIT/hashes_catalogo.sha256") || fallo "el catalogo no coincide"
  echo "   OK"
  echo "4/9 Cuantiles fijos instalados en $CUANTILES"
  mkdir -p "$CUANTILES" && cp "$KIT/cuantiles_fijos.json" "$CUANTILES/cuantiles_fijos.json"
  (cd "$CUANTILES" && sha256sum -c --quiet "$KIT/hashes_cuantiles_fijos.sha256") || fallo "los cuantiles fijos no coinciden"
  echo "   OK"
  echo "5/9 Python tiene numpy y torch"
  python3 -c "import numpy, torch; print('   numpy', numpy.__version__, '| torch', torch.__version__)" || fallo "falta numpy o torch"
  echo "6/9 Las pruebas automaticas del codigo pasan en la VM (1 min)"
  (cd "$CODIGO" && python3 -m unittest discover -s pruebas > /tmp/pruebas_codigo.log 2>&1) || fallo "alguna prueba falla (ver /tmp/pruebas_codigo.log)"
  echo "   OK ($(grep -o 'Ran [0-9]* tests' /tmp/pruebas_codigo.log))"
  echo "7/9 El servidor DASH responde para los 5 videos"
  for v in Paseo_Almunecar_10min_30fps Blender_Sunflower_10min_30fps Paseo_Almunecar_10min_60fps Blender_Sunflower_10min_60fps Tears_of_Steel_10min_30fps; do
    codigo=$(curl -s -o /dev/null -w "%{http_code}" "$SERVIDOR/$v/4sec/${v}_simple_4s.mpd")
    [ "$codigo" = "200" ] || fallo "el MPD de $v no responde (HTTP $codigo): enciende la VM servidor"
  done
  echo "   OK"
  echo "8/9 Plan en seco: ventanas esperadas de la prueba corta y del experimento final"
  for p in previa_vm final_blindaje; do
    rm -rf "/tmp/plan_seco_$p"
    python3 "$RUNNER" --preset "$p" --raiz-salida "/tmp/plan_seco_$p" --solo-plan > "/tmp/plan_seco_$p.log" 2>&1 || fallo "el plan en seco de $p fallo (ver /tmp/plan_seco_$p.log)"
    plan=$(ls -d /tmp/plan_seco_$p/*/ | head -1)
    esperadas="$KIT/ventanas_esperadas_previa.txt"
    [ "$p" = "final_blindaje" ] && esperadas="$KIT/ventanas_esperadas_final.txt"
    python3 "$KIT/comparar_ventanas.py" "${plan}00_protocolo/ventanas_trazas.csv" "$esperadas" || fallo "las ventanas de $p no son las esperadas"
  done
  echo "9/9 Los 8 controladores se crean con los 5 videos y deciden rapido"
  (cd "$CODIGO" && python3 "$KIT/comprobar_controladores.py") || fallo "algun controlador no se crea o es lento"
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
  echo "HUMO CORRECTO. Siguiente paso: bash $KIT/blindaje_vm.sh final"
}

final() {
  if en_marcha final_blindaje; then
    echo "El experimento final ya esta en marcha. Mira el avance con: bash $KIT/blindaje_vm.sh estado"
    exit 0
  fi
  existente=$(ls -d "$SALIDA"/*_final_blindaje/ 2>/dev/null | tail -1)
  if [ -n "$existente" ]; then
    echo "Ya hay un paquete del experimento final: $existente"
    echo "No se lanza otro. Si se corto, continualo con: bash $KIT/blindaje_vm.sh reanudar"
    exit 1
  fi
  nohup python3 "$RUNNER" --preset final_blindaje > "$LOG_FINAL" 2>&1 &
  sleep 30
  en_marcha final_blindaje || fallo "el experimento no arranco (ver $LOG_FINAL)"
  echo "Experimento final lanzado en segundo plano (1208 sesiones, unas 42 horas). Puedes cerrar esta terminal."
  echo "Para ver el avance: bash $KIT/blindaje_vm.sh estado"
}

reanudar() {
  if en_marcha final_blindaje; then
    echo "El experimento final ya esta en marcha; no hace falta reanudarlo."
    exit 0
  fi
  paquete=$(ls -d "$SALIDA"/*_final_blindaje/ 2>/dev/null | tail -1)
  [ -n "$paquete" ] || fallo "no hay ningun paquete del experimento final que reanudar"
  nohup python3 "$RUNNER" --preset final_blindaje --raiz-paquete "${paquete%/}" --reanudar >> "$LOG_FINAL" 2>&1 &
  sleep 30
  en_marcha final_blindaje || fallo "no se pudo reanudar (ver $LOG_FINAL)"
  echo "Reanudado en el mismo paquete: $paquete"
  echo "Las sesiones ya completadas se omiten. Avance: bash $KIT/blindaje_vm.sh estado"
}

estado() {
  preset=final_blindaje
  paquete=$(ls -d "$SALIDA"/*_final_blindaje/ 2>/dev/null | tail -1)
  log="$LOG_FINAL"
  if [ -z "$paquete" ]; then
    preset=previa_vm
    paquete=$(ls -d "$SALIDA"/*_previa_vm/ 2>/dev/null | tail -1)
    log="$TFG/previa_vm.log"
  fi
  [ -n "$paquete" ] || { echo "Todavia no hay ningun paquete en $SALIDA"; exit 0; }
  total=$(grep -c '"id_sesion"' "${paquete}00_protocolo/plan_sesiones.json")
  completadas=$(grep -l '"estado": "completado"' "${paquete}"01_ejecucion/ejecuciones/*/ejecucion_*/manifiesto_ejecucion.json 2>/dev/null | wc -l)
  echo "Paquete: $paquete"
  echo "Sesiones completadas: $completadas de $total"
  if en_marcha "$preset"; then
    ultima=$(grep PROGRESO_EVALUACION "$log" 2>/dev/null | tail -1)
    fallidas=$(echo "$ultima" | grep -o 'fallidas=[0-9]*' | cut -d= -f2)
    eta=$(echo "$ultima" | grep -o 'eta_s=[0-9.]*' | cut -d= -f2)
    [ -n "$eta" ] && echo "Sigue en marcha. Fallidas: ${fallidas:-0}. Faltan unas $(awk -v s="$eta" 'BEGIN{printf "%.1f", s/3600}') horas."
    [ -z "$eta" ] && echo "Sigue en marcha."
  elif [ "$completadas" -lt "$total" ]; then
    echo "NO esta en marcha y faltan sesiones: se corto. Continualo con: bash $KIT/blindaje_vm.sh reanudar"
  else
    echo "Terminado. En Windows (PowerShell), copialo con:"
    # Sin barra final: en PowerShell, \" al final de una ruta con espacios rompe el argumento.
    destino="C:\\Users\\danie\\Documents\\TFG\\legacy\\evidencia_desarrollo"
    [ "$preset" = "final_blindaje" ] && destino="C:\\Users\\danie\\Documents\\TFG Material\\04_evidencia_final"
    echo "scp -r daniel@192.168.1.160:${paquete%/} \"$destino\""
  fi
}

previa() {
  if en_marcha previa_vm; then
    echo "La prueba corta ya esta en marcha. Mira el avance con: bash $KIT/blindaje_vm.sh estado"
    exit 0
  fi
  nohup python3 "$RUNNER" --preset previa_vm > "$TFG/previa_vm.log" 2>&1 &
  sleep 20
  echo "Prueba corta lanzada en segundo plano (160 sesiones, unas 6,5 horas). Puedes cerrar esta terminal."
}

case "${1:-}" in
  comprobar) comprobar ;;
  humo) humo ;;
  final) final ;;
  estado) estado ;;
  reanudar) reanudar ;;
  previa) previa ;;
  *) echo "Uso: bash $0 comprobar|humo|final|estado|reanudar|previa"; exit 2 ;;
esac
