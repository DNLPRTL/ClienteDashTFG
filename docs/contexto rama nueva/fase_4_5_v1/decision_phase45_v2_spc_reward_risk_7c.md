# Decision - Bloque 7C spc_abr_v2_reward_risk

## Decision

Implementar `spc_abr_v2_reward_risk` como critico predictivo por accion para
el dataset `phase45v2_preference_onpolicy_dataset_v1` y sus iteraciones
DAgger-2.

Este bloque no registra controllers, no exporta bundles, no toca runtime y no
autoriza benchmark/ranking/ganador/mejora QoE. Su funcion es entrenar una pieza
predictiva auditable para que el Bloque 7D compare combinaciones de policy +
critico con evidencia offline.

Decision actual tras los pilots v1/v2: SPC no se debe optimizar como un segundo
SPBC ni seleccionarse por ganar como policy autonoma. Su rol principal es
predecir consecuencias por accion (`reward_n`, rebuffer, gap QoE, smoothness y
riesgo) para auditar, vetar o reordenar de forma local las acciones propuestas
por el SPBC congelado.

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

El contrato historico exponia un score compuesto:

```text
score =
  reward
  - rebuffer_weight * estimated_rebuffer_s
  - risk_weight * target_risk_probability
  - smoothness_weight * smoothness_mbps
  - qoe_gap_weight * qoe_gap
```

Ese score compuesto queda degradado a diagnostico historico. El plan activo
separa ranking y restricciones:

- ranking primario: `predicted_reward_n_by_action`
- restricciones/guardias: `predicted_rebuffer_s_by_action` y
  `predicted_target_risk_probability_by_action`
- auxiliares de calibracion: `qoe_gap` y `smoothness_mbps`

No volver a restar de forma lineal rebuffer/smoothness/gap sobre `reward_n`
como receta principal, porque `reward_n = bitrate_mbps - 4.3 * rebuffer_s -
smoothness_mbps` ya contiene la penalizacion QoE principal.

## Loss

- CE contra `best_immediate_action` como ancla.
- Pairwise ranking sobre `preference_pairs`.
- SmoothL1 para `reward_n`, rebuffer, `qoe_gap` y smoothness.
- BCE para `target_risk`, con peso positivo configurable.
- Pesos por `2_5_mbps`, errores graves, `safe_vs_rebuffer` y
  `over_aggressive_rebuffer`, normalizados/capados.

## Seleccion de checkpoint

El checkpoint historico se elegia por `validation_selection_score`, no por loss
pura. Para la siguiente iteracion, este criterio debe pasar a ser secundario:
sirve para diagnosticar `SPC solo`, pero la aceptacion fuerte debe venir de una
gate hibrida con el SPBC congelado.

El score historico penaliza:

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

## Addendum 2026-06-10 - arranque DAgger-2 tras SPBC anchor_safe_rank

Tras aceptar como candidato offline el SPBC 7B
`full_v2_anchor_safe_rank_v1`, el siguiente entrenamiento SPC debe usar el
dataset mas avanzado disponible:

```text
~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1
```

La comparacion offline de referencia debe apuntar al candidato SPBC congelado:

```text
checkpoint=/home/danie/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt
checkpoint_sha256=43b4d012448e12885fac8cbfec914aab6450e0c1b146a4bb8534e8b90b61c227
```

Lectura conceptual:

- `spbc_abr_v2_dpo` aprende directamente una politica: decide que bitrate
  elegir.
- `spc_abr_v2_reward_risk` aprende una superficie de consecuencias por accion:
  recompensa, rebuffer, gap QoE, smoothness y riesgo.
- SPC puede ser mas facil como tarea predictiva porque ve targets por accion,
  pero puede ser mas delicado como decisor porque un error de calibracion en
  riesgo/rebuffer puede mover la accion seleccionada.

Por tanto, el primer paso no debe ser `full_v1`. Debe ser un pilot multi-seed
con limites de `pilot`, DAgger-2, referencia al SPBC congelado y pesos mas
sensibles a `2_5_mbps`, rebuffer y riesgo. La aceptacion exige mirar global,
`2_5_mbps`, `spbc_v2_dpo_on_policy`, regret, rebuffer, over/under-aggressive,
`risk_brier` y `risk_false_negative_rate`. No aceptar un scorer por mejorar solo
una media global.

## Addendum 2026-06-10 - resultado pilot anchor_ref v1

El pilot multi-seed `pilot_dagger2_reward_risk_anchor_ref_seed_*_v1` no debe
escalar a `full_v1`.

Lectura agregada:

```text
best_epoch: 9, 12, 5
global_utility_regret_vs_best_immediate=0.068708..0.071663
global_rebuffer_regret_vs_best_immediate=0.004038..0.004795
global_over_aggressive=0.010500..0.013833
focus_2_5_mbps_over_aggressive=0.031790..0.041975
risk_false_negative_rate=0.001289..0.001978
```

Frente al SPBC congelado, el scorer mejora ligeramente rebuffer regret
(`-0.001214`, `-0.000692`, `-0.000457`), pero empeora utility regret
(`+0.006017`, `+0.003062`, `+0.003898`) y over-aggressive
(`+0.000833`, `+0.004166`, `+0.001500`). Esto confirma que el scorer aprendio
una senal util de riesgo/rebuffer, pero como decisor compra esa mejora con
demasiado coste de utilidad y seguridad.

Decision: no full, no bundle, no controller. La hipotesis siguiente fue
convertir el fallo en loss/seleccion, igual que se hizo con SPBC: anadir una
perdida positiva de ranking dentro del conjunto seguro
(`safe_utility_rank_loss`) y una penalizacion explicita de masa de score sobre
acciones `over_aggressive_rebuffer`. El resultado safe-rank v2 invalido esa
hipotesis para SPC.

## Addendum 2026-06-10 - resultado safe-rank v2

El pilot multi-seed `pilot_dagger2_reward_risk_safe_rank_seed_*_v2` tampoco
debe escalar. Dos de las tres seeds seleccionaron `best_epoch=1` y degradaron
drasticamente la calibracion de riesgo:

```text
seed_450851 risk_brier=0.152982 risk_fn=0.034779
seed_450852 risk_brier=0.011859 risk_fn=0.002133
seed_450853 risk_brier=0.147532 risk_fn=0.035576
```

Frente al SPBC congelado, todas las seeds empeoran utility regret, rebuffer
regret y over-aggressive. El foco `2_5_mbps` tambien empeora de forma clara. La
lectura tecnica es que las perdidas sobre el score compuesto del SPC son
demasiado invasivas: a diferencia del SPBC, el score del SPC se construye con
cabezas predictivas (`reward`, `rebuffer`, `risk`, `smoothness`, `qoe_gap`), y
empujar fuerte ese score puede deformar la calibracion de las cabezas.

Decision: no full, no bundle, no controller. El camino safe-rank/SPC-como-policy
queda cerrado.

## Addendum 2026-06-11 - reinicio conceptual tras revision externa

Los informes externos convergen con la evidencia local:

- SPC v1 ya mostro senal util de rebuffer/riesgo (`risk_brier` sano en dos
  seeds y `risk_false_negative_rate` bajo), pero no gano como decisor autonomo.
- SPC v2 demostro que copiar el safe-rank de SPBC deforma las cabezas
  predictivas, especialmente riesgo.
- La funcion natural de SPC no es conducir, sino criticar acciones candidatas.

Rumbo activo:

```text
spbc_abr_v2_dpo          = conductor / policy decisora
spc_abr_v2_reward_risk   = copiloto / critico predictivo por accion
controller futuro        = SPBC propone + SPC audita/veta/reordena localmente
PPO futuro, si procede   = fine-tuning del SPBC, no del SPC
```

El siguiente bloque no debe ser `full_v1` ni otro pilot pensado para demostrar
que `SPC solo` supera al SPBC. El siguiente bloque debe construir primero la
evaluacion offline hibrida:

```text
SPBC only
SPC only reward-only                         # diagnostico, no criterio final
SPBC + SPC veto-only conservador             # el SPC solo mantiene o baja
SPBC top-k + SPC rerank con restricciones    # k=2 primero, k=3 despues
```

La aceptacion de SPC se hara por sistema combinado, no por ego del copiloto. Los
hard gates internos deben mirar global, `2_5_mbps` y
`spbc_v2_dpo_on_policy`:

- no empeorar `over_aggressive` frente a `SPBC only`
- no empeorar `selected_rebuffer_regret_vs_best_immediate_mean`
- permitir como mucho una degradacion minima y explicita de utility regret si
  reduce seguridad/rebuffer de forma consistente
- mantener `risk_brier` y `risk_false_negative_rate` en banda sana
- reportar `intervention_rate` y `useful_intervention_rate`

Despues de tener ese evaluador, entrenar un `SPC reward-only calibrated` tiene
sentido, pero su objetivo debe ser predictivo/calibrado: `reward_n` como ranking
primario; rebuffer/riesgo como restricciones; gap/smoothness como auxiliares.
No usar perdidas fuertes sobre score compuesto ni seleccionar el modelo solo por
`SPC solo`.
