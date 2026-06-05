# Phase 5 - Integracion de dos controllers NeuralABR-Lite

Status: implemented_on_windows_pending_ubuntu_real_bundle_smokes.

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

## Documentos

```text
phase5_contracto_integracion_dos_controllers.md
phase5_feature_mapping_runtime.md
phase5_fallback_y_telemetria.md
phase5_tests_y_runbook_ubuntu.md
phase5_5_nota_verificacion_futura.md
phase5_cierre_windows.md
```
