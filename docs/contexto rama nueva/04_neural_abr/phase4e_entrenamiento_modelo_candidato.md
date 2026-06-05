# Phase 4E - Entrenamiento del modelo candidato

Status: robust_mpc_controller_real_rebuild_in_progress.

## Proposito

Este bloque entrena el modelo offline `NeuralABR-Lite Candidate Scorer` con los
datos generados en Phase 4B. Es entrenamiento real de IA offline, pero todavia
no es benchmark, no es ranking, no integra controller y no afirma mejora QoE.

La revision del candidato queda separada del entrenamiento: entrenar genera un
checkpoint externo; revisar decide si ese checkpoint esta listo para Phase 4F
export.

## Entradas

Datos offline ya validados:

```text
C:\Users\danie\Documents\TFG\datasets_normalizados\phase4\phase4B_datos_para_entrenamiento
```

En Ubuntu cliente:

```text
/home/daniel/TFG/datasets_normalizados/phase4/phase4B_datos_para_entrenamiento
```

## Salida externa

Directorio del modelo candidato:

```text
C:\Users\danie\Documents\TFG\modelos\phase4\phase4E_modelo_candidato_neural_abr_lite
```

En Ubuntu cliente:

```text
/home/daniel/TFG/modelos/phase4/phase4E_modelo_candidato_neural_abr_lite
```

Archivos principales:

```text
modelo_candidato_neural_abr_lite.pt
configuracion_modelo.json
estadisticas_normalizacion_train_only.json
reporte_entrenamiento_modelo.json
reporte_revision_modelo_candidato.json
```

## Contrato

- Modelo: `NeuralABR-Lite Candidate Scorer`.
- Metodo: behavior cloning.
- Teacher: `robust_mpc`.
- Fuente del teacher: controller real `core.controller.robust_mpc.RobustMpcController`
  ejecutado dentro del entorno offline de replay.
- Reward: `qoe_linear_v1`.
- Dispositivo: CPU.
- Segmento primario: `4s`.
- Normalizacion: la de Phase 4B, ajustada solo con entrenamiento.
- Metadata de trazas: solo auditoria, nunca feature.

## Comando Windows corto

Solo para comprobar mecanica:

```powershell
python scripts/entrenar_phase4_modelo_candidato.py --overwrite --epochs 1 --batch-size 8 --max-training-samples 256 --max-validation-samples 128
python scripts/revisar_phase4_modelo_candidato.py --min-training-samples 1 --min-validation-samples 1 --min-training-teacher-agreement 0.0 --min-validation-teacher-agreement 0.0
```

## Comando Ubuntu cliente largo

Ejecutar en Ubuntu cliente, despues de sincronizar el repo:

```bash
cd ~/TFG/DashClientModular4
git pull --ff-only origin rebuild/phase3-from-phase2
python scripts/validate_phase4_datos_entrenamiento.py
python scripts/entrenar_phase4_modelo_candidato.py --overwrite --epochs 20 --batch-size 64
python scripts/revisar_phase4_modelo_candidato.py
```

Resultado esperado si el modelo queda listo para export:

```text
status=PASS
decision=PHASE4E_MODELO_CANDIDATO_READY_FOR_PHASE4F
candidate_ready_for_phase4f=true
benchmark_performed=false
ranking_performed=false
controller_integrated=false
export_bundle_created=false
```

Si sale `PASS_NOT_CANDIDATE`, el entrenamiento termino sin romper contratos,
pero el modelo no debe exportarse aun. En ese caso hay que pegar el JSON de
`reporte_revision_modelo_candidato.json`.

Si sale `BLOCKED_NEEDS_FIX`, hay un fallo de contrato o artifact y hay que
corregirlo antes de seguir.

## Nota sobre ZIP para Ubuntu

No hace falta preparar ZIP nuevo en este punto porque Ubuntu ya genero el plan
de trazas y los datos de Phase 4B. Para esta ejecucion basta con `git pull`.
El ZIP de directorios hermanos de `TFG` se preparara cuando haga falta mover o
congelar artifacts externos, normalmente al cerrar Phase 4 o antes de una
ejecucion que necesite sustituir carpetas completas en Ubuntu.
