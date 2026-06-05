# Phase 4B/C/D - Datos offline y prueba rapida

Status: robust_mpc_controller_real_rebuild_in_progress.

## Proposito

Este bloque convierte el plan de trazas de Phase 4A en datos offline para
entrenar NeuralABR-Lite mas adelante. Tambien deja una prueba rapida de
entrenamiento en CPU para comprobar que el pipeline funciona.

No es entrenamiento final. No genera modelo candidato. No hay benchmark, ranking
ni afirmacion de mejora QoE.

## Entradas

Plan de trazas generado en Phase 4A:

```text
C:\Users\danie\Documents\TFG\manifests_trazas\phase4\phase4A_plan_de_trazas_para_entrenamiento\phase4_plan_de_trazas_para_entrenamiento.json
```

## Salidas externas

Datos para entrenamiento:

```text
C:\Users\danie\Documents\TFG\datasets_normalizados\phase4\phase4B_datos_para_entrenamiento
```

Archivos principales:

```text
datos_entrenamiento.jsonl
datos_validacion.jsonl
resumen_datos_entrenamiento.json
esquema_features_modelo.json
esquema_labels_teacher.json
auditoria_no_contaminacion.json
estadisticas_normalizacion_train_only.json
```

Prueba rapida de entrenamiento:

```text
C:\Users\danie\Documents\TFG\runs_trazas\phase4\phase4D_prueba_rapida_entrenamiento
```

Archivo principal:

```text
reporte_prueba_rapida_entrenamiento.json
```

## Contrato tecnico

- Teacher principal: `robust_mpc`.
- Fuente del teacher: controller real de Phase 2 ejecutado en replay offline.
- Modulo del teacher: `core.controller.robust_mpc.RobustMpcController`.
- Reward version: `qoe_linear_v1`.
- Accion: `representation_index`.
- Segmento primario: `4s`.
- Ladder por defecto: `300,750,1200,1850,2850,4300` kbps.
- Normalizacion: ajustada solo con `datos_entrenamiento.jsonl`.
- Metadata como `trace_id`, `dataset_id`, `semantics`, `source_split` y
  `leakage_group` se conserva solo para auditoria, nunca como feature.

## Comandos Windows

Build pequeno para comprobar:

```powershell
python scripts/build_phase4_datos_entrenamiento.py --overwrite --max-training-windows 8 --max-validation-windows 4
python scripts/validate_phase4_datos_entrenamiento.py
python scripts/run_phase4_prueba_rapida_entrenamiento.py --max-samples 64
```

Build completo se reserva preferentemente para Ubuntu cliente.

## Comandos Ubuntu cliente

```bash
cd ~/TFG/DashClientModular4
git pull --ff-only origin rebuild/phase3-from-phase2
python scripts/build_phase4_datos_entrenamiento.py --overwrite
python scripts/validate_phase4_datos_entrenamiento.py
python scripts/run_phase4_prueba_rapida_entrenamiento.py --max-samples 256
```

Resultado esperado:

```text
status=PASS
benchmark_performed=false
ia_training_performed=false
ranking_performed=false
candidate_model_created=false
```

El resumen del dataset debe declarar:

```text
label_teacher=robust_mpc
label_teacher_source=phase2_controller_real_en_replay_offline
label_teacher_controller_module=core.controller.robust_mpc.RobustMpcController
```

## Nota sobre mover artifacts a Ubuntu

No hace falta crear ZIP en cada paso. Cuando haya que ejecutar el build completo
o cerrar Phase 4, se preparara un paquete externo con los directorios necesarios
para sustituir los artifacts actuales en Ubuntu cliente.
