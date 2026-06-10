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

## Addendum 2026-06-10 - anchor_safe_rank

El ajuste `safe_margin_v1` no queda aceptado para escalar a `full_v1`: la
confirmacion multi-seed full-samples termino en fallback (`best_epoch=0`) en
las tres seeds observadas. El fallo dominante no fue ya la sobre-agresividad
global, sino no sostener el regret de utilidad en `2_5_mbps` y
`spbc_v2_dpo_on_policy` frente al gate relativo. No relajar el gate.

La receta posterior `anchor_safe_rank` anade una perdida positiva dentro del
conjunto seguro (`safe_utility_rank_loss`) y mantiene el anclaje al checkpoint
inicial. La confirmacion multi-seed con profile `pilot` y full-samples queda
aceptada como condicion operativa previa: 3/3 seeds tuvieron `best_epoch=6`,
`gate=true` y metricas estables.

Resultado observado del entrenamiento normal `--profile full_v1`:

```text
best_epoch=8
gate=true
global_over=0.009878
focus_over=0.026312
spbc2_over=0.005187
global_u=0.053229
focus_u=0.062015
spbc2_u=0.044244
safe_rank=0.018196476
```

Deltas frente a `full_v1_utility_risk_v1` en la misma validacion:

```text
global utility_regret delta=-0.015430
global rebuffer_regret delta=-0.003992
global over_aggressive delta=-0.005777
global predicted_rebuffer_s_mean delta=-0.004228

2_5_mbps utility_regret delta=-0.026998
2_5_mbps rebuffer_regret delta=-0.007969
2_5_mbps over_aggressive delta=-0.018583
2_5_mbps predicted_rebuffer_s_mean delta=-0.008934
```

La lectura tecnica es positiva para preparacion offline: el run selecciona un
epoch entrenado, pasa el safety gate y mejora simultaneamente regret de
utilidad, regret de rebuffer y sobre-agresividad, tambien en el foco
`2_5_mbps`. Como contrapartida diagnostica, baja `top1_accuracy`,
`balanced_accuracy` y `macro_f1`, sube `under_aggressive_rate_vs_oracle`
(`+0.059409` global, `+0.163059` en `2_5_mbps`) y baja el bitrate medio
predicho (`-127.600217` kbps global, `-340.249597` kbps en `2_5_mbps`). Esto
indica una politica mas conservadora, aceptable como candidato offline pero
obligatoria de monitorizar antes de integracion.

Decision: aceptar
`~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt`
como candidato offline SPBC 7B para la siguiente fase de preparacion. No
exportar bundle, no registrar controller, no ejecutar Phase 6 y no declarar
ranking, ganador, mejora QoE ni generalizacion. Antes de cualquier integracion,
capturar el `checkpoint_sha256` desde el reporte de entrenamiento y mantenerlo
en la documentacion/runbook.

Siguiente paso recomendado: congelar el artefacto con ruta y SHA, y continuar
con el modelo complementario `spc_abr_v2_reward_risk` usando el mismo criterio:
pilots/summaries versionados, gates estrictos y ninguna afirmacion comparativa
antes de Phase 6.
