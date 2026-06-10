# Decision - Bloque 7C spc_abr_v2_reward_risk

## Decision

Implementar `spc_abr_v2_reward_risk` como scorer offline nuevo para el
dataset `phase45v2_preference_onpolicy_dataset_v1`.

Este bloque no registra controllers, no exporta bundles, no toca runtime y no
autoriza benchmark/ranking/ganador/mejora QoE. Su funcion es entrenar una pieza
predictiva auditable para que el Bloque 7D compare combinaciones de policy +
scorer con evidencia offline.

## Evidencia usada

- Comyco/SABR: la imitacion estatica no basta; los estados on-policy y el
  replay etiquetado por oracle reducen error compuesto.
- Puffer/Fugu: la parte aprendida mas defendible es un predictor de
  consecuencias verificables, usado despues para decision segura.
- ANT/BETA/Oboe: un modelo unico tiende a fallar por regimen; hay que reportar
  y ponderar buckets, especialmente redes bajas y variables.
- Gelato/Plume: el skew de trazas y las colas raras degradan controladores; el
  entrenamiento debe priorizar casos con bajo retorno o errores graves.
- SODA/SafeSABR: antes de desplegar hay que auditar riesgo, smoothness y colas
  severas; no basta con accuracy.

## Contrato

El forward consume solo:

```text
model_inputs.context
model_inputs.candidates
action_mask
```

Nunca son inputs:

```text
preference_pairs
per_action_outcomes
qoe_gap
reward_n
rollout_source
metadata
```

## Targets

El modelo predice por accion:

- `reward_n`
- `estimated_rebuffer_s`
- `qoe_gap`
- `smoothness_mbps`
- `target_risk`

La decision offline se calcula como:

```text
score =
  reward
  - rebuffer_weight * estimated_rebuffer_s
  - risk_weight * target_risk_probability
  - smoothness_weight * smoothness_mbps
  - qoe_gap_weight * qoe_gap
```

## Loss

- CE contra `best_immediate_action` como ancla.
- Pairwise ranking sobre `preference_pairs`.
- SmoothL1 para `reward_n`, rebuffer, `qoe_gap` y smoothness.
- BCE para `target_risk`, con peso positivo configurable.
- Pesos por `2_5_mbps`, errores graves, `safe_vs_rebuffer` y
  `over_aggressive_rebuffer`, normalizados/capados.

## Seleccion de checkpoint

El mejor checkpoint se elige por `validation_selection_score`, no por loss pura.
El score penaliza:

- `selected_utility_regret_vs_best_immediate_mean`
- `selected_rebuffer_regret_vs_best_immediate_mean`
- `over_aggressive_rate_vs_oracle`
- `invalid_action_rate`
- error predictivo
- el mismo patron con peso extra en `2_5_mbps`

## Salida externa

```text
~/TFG/modelos/phase45_v1/spc_abr_v2_reward_risk/<profile>/
```

No commitear checkpoints, reportes ni logs generados.
