# Phase 6 - Validacion Comparativa Formal

Status: implementation_ready_for_ubuntu_execution.

Phase 6 introduce el primer pipeline formal de comparacion bajo red controlada
por trazas. La ejecucion formal se hace en Ubuntu cliente. Windows queda para
desarrollo, tests rapidos, commit y push.

## Contrato cerrado

- Motor formal: `fake` + `network_replay.enabled=true`.
- Motor GStreamer: disponible solo como diagnostico separado desde la GUI.
- Las trazas se compactan a tiempo continuo antes de recortar ventanas. Esto
  evita que datasets con timestamps absolutos y huecos grandes fallen aunque
  tengan duracion util suficiente.
- El preset `diagnostico` evalua 6 segmentos de media de 4 s. Sirve para
  verificar en pocos minutos que seleccion, replay, controllers, metricas,
  graficas, informes y auditoria estan bien cableados. No es benchmark.
- La sesion formal evalua 30 segmentos de media de 4 s; el presupuesto de red
  por defecto es una ventana de replay de 300 s para permitir rebuffering sin
  convertir una red dificil en fallo tecnico.
- Las ventanas reales formalmente comparables aplican un suelo conservador de
  throughput medio/maximo para excluir trazas fisicamente incapaces de servir
  siquiera la calidad minima del MPD. Las sinteticas siguen separadas como
  diagnostico.
- QoE primaria: `qoe_linear_v1`, `qoe_linear_mean`.
- Split formal: solo `eval`.
- Media formal: MPDs de 10 min con segmentos de 4 s, recortados a 30 segmentos
  reales por sesion.
- Sinteticas: diagnosticas y reportadas separadas.
- Controllers debug/test excluidos del modo comparable.
- Controllers nuevos: entran automaticamente si estan en el registry y no estan
  en la lista de exclusion.
- Controllers propios: las filas evaluables deben conservar auditoria neural
  por chunk (`bundle_loaded`, `bundle_hash_ok`, `inference_ms`,
  `fallback_reason=success_neural`, accion cruda/segura y `fallback_used=0`).

## Scripts

```bash
python scripts/phase6_gui.py
python scripts/run_phase6_validacion_comparativa.py --preset diagnostico
python scripts/run_phase6_validacion_comparativa.py --preset rapido
python scripts/run_phase6_validacion_comparativa.py --preset equilibrado
python scripts/analyze_phase6_results.py /home/daniel/TFG/runs_trazas/phase6/validacion_comparativa/<paquete>
python scripts/verificar_paquete_phase6.py /home/daniel/TFG/runs_trazas/phase6/validacion_comparativa/<paquete>
python scripts/run_phase6_verificacion_clasica_controlada.py --preset rapido
```

## Presets

- `diagnostico`: 2 ventanas reales + 1 sintetica diagnostica, 1 MPD, todos los
  controllers comparables, 6 segmentos por sesion, ventana de red de 90 s.
  Esperado con 7 controllers actuales: 21 sesiones y unos 6-10 min segun red,
  stalls y overhead. No autoriza benchmark ni ranking.
- `rapido`: 8 ventanas reales + 2 sinteticas diagnosticas, 1 MPD, 30 segmentos
  por sesion, ventana de red de 300 s. Smoke operativo de Phase 6.
- `equilibrado`: 24 ventanas reales + 4 sinteticas diagnosticas, 2 MPDs, 30
  segmentos por sesion. Primer preset recomendado para resultados defendibles
  si todos los gates y la verificacion de paquete pasan.
- `extendido`: 48 ventanas reales + 8 sinteticas diagnosticas, 4 MPDs, 30
  segmentos por sesion. Disponible para evidencia ampliada.

## Salida externa

```text
/home/daniel/TFG/runs_trazas/phase6/validacion_comparativa/<timestamp>_<preset>/
  00_protocolo/
  01_ejecucion/
  02_resultados/
  03_graficas/
  04_informe/
```

`02_resultados/resultados_para_validar.md`,
`02_resultados/resultados_para_validar.json`,
`02_resultados/verificacion_paquete.md` y
`02_resultados/verificacion_paquete.json` son los archivos pensados para auditar
el experimento sin abrir imagenes. El analizador y el verificador pueden leer
paquetes copiados entre Ubuntu y Windows usando la estructura interna del
paquete, aunque el plan contenga rutas absolutas de la maquina que ejecuto el
experimento.

`03_graficas/plot_manifest.json` registra cada grafica como `generated`,
`skipped`, `deferred` o `error`, por lo que las graficas vacias o no generadas
quedan auditables sin inspeccion manual.

La GUI muestra progreso por sesiones procesadas, sesiones totales, porcentaje,
fallos, sesiones reanudadas, tiempo transcurrido, duracion de la ultima sesion,
media por sesion y ETA restante.

## Autorizacion

`diagnostico` y `rapido` no autorizan ranking final. `equilibrado` y
`extendido` pueden autorizar benchmark/ranking si pasan todos los gates y la
verificacion de paquete: sesiones reales completadas/evaluables, split eval,
MPDs 4 s, inferencia neural verificada en controllers propios, sin fallback en
controllers propios, sin artifacts legacy, graficas esperadas auditables y
sinteticas separadas.
