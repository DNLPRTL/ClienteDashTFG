# Phase 5 - Integracion de dos controllers NeuralABR-Lite

Status: closed_on_ubuntu.

Phase 5 integra los dos bundles offline cerrados en Phase 4 como controllers
reales del cliente:

```text
neural_abr_lite_robust_mpc
neural_abr_lite_teacher_hibrido
```

Ambos usan la misma implementacion comun `guarded neural scorer`: el modelo
puntua representaciones candidatas, se aplica una mascara de acciones validas,
se valida la accion, y cualquier fallo cae a un controller clasico de respaldo.

Esta fase no ejecuta benchmark, no hace ranking, no declara ganador y no afirma
mejora de QoE. La comparacion formal queda reservada para Phase 6.

## Cierre

Ubuntu cliente valido:

- `python -m unittest discover`: `333` tests OK.
- `python scripts/check_client_readiness.py --strict`: `87 OK / 0 WARN / 0 FAIL`.
- Smoke con bundle real `robust_mpc`: `status=completed`, bundle cargado,
  telemetria neural en `segment_telemetry.csv`, sin columnas neural en
  `evaluation_segments.csv`.
- Smoke con bundle real `teacher_hibrido`: `status=completed`, bundle cargado,
  telemetria neural en `segment_telemetry.csv`, sin columnas neural en
  `evaluation_segments.csv`.

Estos smokes usaron red rapida por adaptador puente. Eso es valido para Phase 5
porque solo se verifica integracion estructural; no es valido como benchmark ni
como evidencia de rendimiento ABR.

## Documentos

```text
phase5_contracto_integracion_dos_controllers.md
phase5_feature_mapping_runtime.md
phase5_fallback_y_telemetria.md
phase5_tests_y_runbook_ubuntu.md
phase5_cierre_windows.md
```

La verificacion posterior del cliente y de los controllers clasicos vive en:

```text
docs/contexto rama nueva/fase_verificacion_cliente_y_controllers_clasicos/
```
