# Phase 5 - Fallback y telemetria

## Fallback

El controller cae a respaldo si ocurre cualquiera de estos casos:

- `bundle_dir` ausente;
- bundle inexistente o incompleto;
- hash o schema invalido;
- teacher esperado incompatible;
- carga de checkpoint insegura o fallida;
- features incompletas o contaminadas;
- action mask vacia;
- inferencia con NaN/Inf;
- accion fuera de mascara;
- latencia de inferencia por encima del limite;
- fallo del fallback clasico.

El fallback primario por defecto es:

```text
robust_mpc
```

Si el fallback clasico tambien falla, se elige la representacion valida mas
baja. Si ni siquiera hay ladder valida, se devuelve `0.0` como fallo cerrado.

## Telemetria

Los campos `feedback_neural_*` se escriben solo en `segment_telemetry.csv`.
`evaluation_segments.csv` permanece limpio.

Campos principales:

```text
feedback_neural_controller_key
feedback_neural_model_label
feedback_neural_bundle_path
feedback_neural_bundle_loaded
feedback_neural_feature_vector_ok
feedback_neural_action_mask_valid_count
feedback_neural_raw_action
feedback_neural_safe_action
feedback_neural_selected_representation_index
feedback_neural_fallback_used
feedback_neural_fallback_reason
feedback_neural_inference_ms
feedback_neural_diagnostic_only
```

No se escriben scores completos por defecto para no ensuciar el CSV de
telemetria estructural.

## Interpretacion

Esta telemetria es diagnostica. Sirve para explicar si el controller cargo,
infirio, uso fallback o selecciono una accion valida. No es evidencia de
benchmark ni comparacion QoE.

