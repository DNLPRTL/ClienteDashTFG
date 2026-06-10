# Decision tecnica 7B.4 - DAgger-2 para spbc_abr_v2_dpo

## Estado

No aceptar todavia `spbc_abr_v2_dpo/full_v1_utility_risk_v1` como candidato
offline cerrado.

El full es util como politica base para recopilar estados, pero la auditoria
residual muestra que los errores se concentran en:

- estados `spbc_v1_on_policy`;
- bucket `2_5_mbps`;
- regret de utilidad y rebuffer frente a `best_immediate_action`;
- sobre-agresividad con rebuffer y sub-agresividad con perdida de QoE.

## Evidencia desde los papers MD

- Comyco: el aprendizaje supervisado/off-policy acumula error cuando la politica
  visita estados no cubiertos por el experto; la receta es ejecutar la politica,
  pedir etiqueta al experto y agregar esas muestras al buffer.
- SABR y SafeSABR: usan pretraining BC/DPO con agregacion estilo DAgger y experto
  beam-search.
- Gelato/Plume: los fallos de cola no se corrigen solo en la funcion de perdida;
  hay que balancear/priorizar los regimenes de traza problematicos.
- Oboe: un unico comportamiento global puede no especializar bien en rangos
  concretos de throughput; `2_5_mbps` debe quedar auditado de forma separada.
- Puffer/Fugu y CausalSim: no declarar victoria por simulacion offline; usar la
  evidencia para reducir riesgo antes de Phase 6.

## Cambio decidido

Crear un contrato hermano:

```text
phase45_v2_preference_onpolicy_dagger2_dataset_v1
```

La salida externa recomendada es:

```text
~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1/
```

El dataset agrega una tercera fuente de rollout:

```text
spbc_v2_dpo_on_policy
```

junto a las existentes:

```text
oracle_rollout
spbc_v1_on_policy
```

La politica `spbc_abr_v2_dpo/full_v1_utility_risk_v1` se ejecuta en el replay
offline, los estados resultantes se reetiquetan con `oracle_qoe_beam_v1`, y se
preservan `per_action_outcomes` y `preference_pairs`. `rollout_policy_action`,
`rollout_policy_model_key`, `metadata`, `per_action_outcomes`, `reward_n`,
`qoe_gap` y `rollout_source` siguen siendo targets/auditoria, nunca inputs.

## Uso

Entrenar el siguiente 7B sobre este dataset nuevo con:

```text
--dataset-dir ~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1
```

No lanzar Phase 6 ni registrar controllers por este cambio. Sigue siendo trabajo
offline de preparacion.

## Flags anti-benchmark

Todos los artefactos deben mantener:

```text
benchmark_performed=false
ranking_performed=false
no_final_ranking=true
ia_training_performed=false
```

El entrenamiento posterior 7B debe mantener:

```text
benchmark_performed=false
ranking_performed=false
no_final_ranking=true
bundle_exported=false
controller_registered=false
```
