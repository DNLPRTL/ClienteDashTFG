# Phase 4F - Export del bundle de inferencia

Status: implemented_on_windows_pending_ubuntu_validation.

## Proposito

Este bloque convierte el modelo candidato de Phase 4E en un bundle local de
inferencia offline. El bundle puede cargarse en CPU, validar hashes y ejecutar
una prueba de inferencia con action mask.

No integra un controller. No registra `neural_abr_lite` en el cliente. No es
benchmark, ranking ni afirmacion de mejora QoE.

## Entrada

Modelo candidato validado en Ubuntu cliente:

```text
/home/daniel/TFG/modelos/phase4/phase4E_modelo_candidato_neural_abr_lite
```

Datos usados para prueba de inferencia:

```text
/home/daniel/TFG/datasets_normalizados/phase4/phase4B_datos_para_entrenamiento
```

## Salidas externas

Bundle:

```text
/home/daniel/TFG/modelos/phase4/phase4F_bundle_para_inferencia_neural_abr_lite
```

Archivos del bundle:

```text
manifiesto_bundle_inferencia.json
modelo_para_inferencia.pt
configuracion_modelo.json
estadisticas_normalizacion_train_only.json
esquema_features_modelo.json
esquema_ladder_contenido.json
tarjeta_modelo.json
contrato_inferencia.json
politica_respaldo.json
reporte_export_bundle_inferencia.json
```

Validacion:

```text
/home/daniel/TFG/runs_trazas/phase4/phase4F_validacion_bundle_inferencia
```

Archivos principales:

```text
reporte_validacion_bundle_inferencia.json
reporte_prueba_inferencia_bundle.json
reporte_latencia_inferencia.json
```

## Contrato

- Modelo: `NeuralABR-Lite Candidate Scorer`.
- Carga: CPU.
- Accion: `representation_index`.
- Normalizacion: `estadisticas_normalizacion_train_only.json`.
- Feature schema: sin metadata de traza ni throughput futuro.
- Action mask: obligatorio.
- Fallback: documentado para integracion futura, no ejecutado en Phase 4F.

## Comandos Ubuntu cliente

```bash
cd ~/TFG/DashClientModular4
git pull --ff-only origin rebuild/phase3-from-phase2
python scripts/exportar_phase4_bundle_inferencia.py --overwrite
python scripts/validar_phase4_bundle_inferencia.py
```

Resultado esperado:

```text
status=PASS
decision=PHASE4F_EXPORT_BUNDLE_READY_FOR_PHASE4G
valid_action_rate=1.0
deterministic_rate=1.0
no_nan_inf_scores=true
controller_integrated=false
ranking_performed=false
benchmark_performed=false
```

Si se quiere repetir solo la prueba de inferencia:

```bash
python scripts/probar_phase4_inferencia_bundle.py --max-samples 512
```

## Nota sobre ZIP para Ubuntu

No hace falta ZIP nuevo para ejecutar Phase 4F porque el modelo candidato ya se
genero en Ubuntu cliente. El bundle tambien se generara alli. El ZIP de
directorios externos se reserva para cierre de fase o para trasladar artifacts
completos entre maquinas.
