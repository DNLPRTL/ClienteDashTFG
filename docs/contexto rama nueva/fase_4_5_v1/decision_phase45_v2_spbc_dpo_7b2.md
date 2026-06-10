# Decision tecnica 7B.2 - spbc_abr_v2_dpo utility/risk-aware

## Contexto

El Bloque 7B entreno `spbc_abr_v2_dpo` sobre
`phase45v2_preference_onpolicy_dataset_v1` con CE contra `oracle_action`, DPO
con pares `preferred/rejected` y ranking loss por gaps.

Los pilots WSL2 mostraron que el entrenamiento era tecnicamente sano:
checkpoint de referencia `spbc_abr_v1/full_v1` cargado, inputs limpios,
`invalid_action_rate=0`, banderas anti-benchmark correctas y aprendizaje
estable. Pero el objetivo todavia era insuficiente para el regimen critico
`2_5_mbps`.

## Evidencia local

Pilot base:

- mejoro `top1` frente a `spbc_v1`;
- aumento bitrate y over-aggressive en `2_5_mbps`;
- empeoro reward/rebuffer estimado en ese bucket.

Pilot conservador:

- redujo over-aggressive y bitrate en `2_5_mbps`;
- aumento under-aggressive;
- no mejoro reward estimado.

Conclusion: la loss global CE+DPO+ranking mueve el modo de fallo, pero no
optimiza directamente utilidad inmediata ni coste de rebuffer.

## Decision

Mantener dataset v2 intacto y mejorar solo el entrenamiento:

- CE queda como ancla contra `oracle_action`, no como objetivo dominante.
- Anadir `utility_loss`: cross entropy contra una distribucion softmax de
  `reward_n` por accion valida.
- Anadir `rebuffer_loss`: penalizacion esperada de rebuffer bajo la
  distribucion de la politica.
- Ponderar muestras/pares por `2_5_mbps`, errores `over_aggressive_rebuffer` y
  preferencias `safe_vs_rebuffer`.
- Reportar selected utility regret y selected rebuffer regret contra oracle y
  contra mejor accion inmediata.

## Limites

Esto sigue siendo entrenamiento offline. No registra controller, no exporta
bundle, no ejecuta Phase 6 y no autoriza benchmark, ranking, ganador ni mejora
QoE.
