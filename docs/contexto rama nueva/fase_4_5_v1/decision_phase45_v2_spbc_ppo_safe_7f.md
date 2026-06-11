# Decision tecnica 7F - PPO seguro offline para SPBC

## Estado

El candidato SPBC operativo sigue siendo:

```text
~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt
```

Ese checkpoint queda aceptado solo como candidato offline de preparacion: paso
el safety gate y redujo regret/sobre-agresividad frente a la referencia
anterior, pero desplazo la politica hacia mayor conservadurismo. En particular,
subio `under_aggressive_rate_vs_oracle` y bajo el bitrate medio predicho, asi
que no es prudente integrarlo como conclusion final sin una fase posterior.

Los intentos `safe_margin_v1`, `residual_safe_rank_v1`, SPC como politica, SPC
safe-rank y SPC critic/copilot v1 no sustituyen a este anchor. Quedan como
diagnostico historico, no como controlador aceptado.

## Hipotesis

Los papers que motivan la fase 4-5 v1 no obligan a hacer PPO online dentro del
cliente. Para esta rama, el paso responsable es probar una mejora tipo PPO
offline:

- politica inicial congelada como comportamiento de referencia;
- superficie de recompensa por accion ya calculada en el dataset DAgger-2;
- ventaja por accion centrada contra la expectativa de la politica inicial;
- clipping PPO para impedir saltos grandes respecto a la referencia;
- penalizaciones explicitas en la ventaja para acciones over-aggressive,
  rebuffer y target-risk;
- KL y safety gate relativos al checkpoint aceptado.

Esto no es benchmark, no es Phase 6, no registra controller y no autoriza
ranking ni afirmacion de mejora de QoE.

## Cambio

Se anade al trainer `spbc_abr_v2_dpo` una perdida opcional:

```text
ppo_clip_loss = - E_a~pi_ref[min(ratio * advantage, clipped_ratio * advantage)]
```

La ventaja se calcula desde `per_action_outcomes`, nunca desde inputs del
modelo. `rollout_source`, `trace_id`, metadata, labels de auditoria y futuro
throughput siguen fuera del contrato de entrada.

Con peso cero, el entrenamiento historico queda igual. El pilot PPO-safe activa
la perdida solo desde el runner versionado.

## Ejecucion WSL

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/run_phase45_v2_spbc_ppo_safe_pilot_wsl.sh
```

El runner usa:

```text
dataset=~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1
init_checkpoint=~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt
seeds=450881,450882,450883
epochs=4
```

Si una seed termina en `best_epoch=0` o `gate=false`, el script se detiene antes
de gastar las siguientes seeds.

## Criterios de lectura

Aceptar la via PPO-safe solo si:

- al menos la primera seed selecciona un epoch entrenado (`best_epoch>0`) y
  `gate=true`;
- idealmente 3/3 seeds terminan `TRAINED_PASS`;
- no hay regresion en sobre-agresividad global, `2_5_mbps` ni
  `spbc_v2_dpo_on_policy` mas alla del gate;
- no hay regresion de utility/rebuffer regret mas alla del gate;
- se monitoriza explicitamente si baja `under_aggressive_rate_vs_oracle` o
  recupera bitrate medio sin reabrir sobre-agresividad.

Cerrar la via PPO-safe si:

- la primera seed vuelve a fallback;
- el safety gate falla por over-aggressive en foco o en `spbc_v2_dpo_on_policy`;
- la mejora aparente solo viene de bajar bitrate/subir under-aggressive sin
  reducir regret.

## Estado cientifico

Este pilot puede producir un nuevo candidato offline SPBC, pero no cambia la
conclusion experimental del TFG por si solo. Cualquier afirmacion comparativa
requiere la validacion formal de Phase 6 con protocolo congelado.
