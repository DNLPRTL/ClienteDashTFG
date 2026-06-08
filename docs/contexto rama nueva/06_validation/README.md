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

## Scripts

```bash
python scripts/phase6_gui.py
python scripts/run_phase6_validacion_comparativa.py --preset rapido
python scripts/run_phase6_validacion_comparativa.py --preset equilibrado
python scripts/analyze_phase6_results.py /home/daniel/TFG/runs_trazas/phase6/validacion_comparativa/<paquete>
python scripts/run_phase6_verificacion_clasica_controlada.py --preset rapido
```

## Salida externa

```text
/home/daniel/TFG/runs_trazas/phase6/validacion_comparativa/<timestamp>_<preset>/
  00_protocolo/
  01_ejecucion/
  02_resultados/
  03_graficas/
  04_informe/
```

`02_resultados/resultados_para_validar.md` y
`02_resultados/resultados_para_validar.json` son los archivos pensados para
auditar el experimento sin abrir imagenes. El analizador puede leer paquetes
copiados entre Ubuntu y Windows usando la estructura interna del paquete, aunque
el plan contenga rutas absolutas de la maquina que ejecuto el experimento.

La GUI muestra progreso por sesiones procesadas, sesiones totales, porcentaje,
fallos y sesiones reanudadas.

## Autorizacion

`rapido` es smoke operativo de Phase 6 y no autoriza ranking final.
`equilibrado` y `extendido` pueden autorizar benchmark/ranking si pasan todos
los gates: sesiones reales completadas/evaluables, split eval, MPDs 4 s,
sin fallback en controllers propios, sin artifacts legacy y sinteticas
separadas.
