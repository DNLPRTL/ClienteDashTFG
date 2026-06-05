# Phase 5 - Contrato de integracion de dos controllers

## Objetivo

Integrar los dos bundles `NeuralABR-Lite Candidate Scorer` de Phase 4 como
controllers separados del cliente, sin cambiar el contrato general del player.

## Controllers publicos

```text
neural_abr_lite_robust_mpc
neural_abr_lite_teacher_hibrido
```

Ambos deben:

- recibir feedback mediante `setPlayerFeedback`;
- decidir mediante `calcControlAction`;
- devolver siempre un rate existente en `feedback["rates"]`;
- usar `representation_index` como accion interna;
- funcionar con fake engine y sin GStreamer;
- cargar bundles desde rutas externas configurables;
- mantenerse en modo diagnostico en Phase 5.

## Parametros publicos

```yaml
controller:
  name: "neural_abr_lite_robust_mpc"
  params:
    bundle_dir: "/ruta/externa/al/bundle"
    fallback_controller: "robust_mpc"
    verify_hashes: true
    max_inference_latency_ms: 50.0
```

`neural_abr_lite_teacher_hibrido` usa el mismo formato, pero espera un bundle
con `teacher=teacher_hibrido`.

## Carga del bundle

La carga runtime valida:

- archivos obligatorios del bundle Phase 4;
- hashes SHA-256 del manifiesto;
- teacher esperado;
- schema de features `phase4_esquema_features_modelo_v1`;
- dimensiones del modelo;
- checkpoint con `torch.load(..., weights_only=True)`.

Si no se puede cargar de forma segura, se usa fallback.

## Limite metodologico

La integracion prueba que los controllers existen y se comportan de forma
segura dentro del cliente. No prueba que sean mejores que los baselines.

