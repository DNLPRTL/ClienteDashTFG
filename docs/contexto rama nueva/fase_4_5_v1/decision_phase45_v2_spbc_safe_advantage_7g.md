# Decision tecnica 7G - Safe Advantage probe para SPBC

## Diagnostico

El pilot `pilot_dagger2_ppo_safe_seed_450881_v1` no queda aceptado. El script
se detuvo correctamente tras la primera seed porque ningun epoch entrenado paso
el gate:

```text
best_epoch=0
fallback_to_reference=true
gate=true en el checkpoint final de fallback
```

Los epochs entrenados redujeron ligeramente la sobre-agresividad, pero fallaron
por `2_5_mbps_utility_regret_non_regression`. Es decir, PPO-safe v1 compro mas
seguridad a costa de empeorar utilidad justo en el bucket critico.

No relajar el gate. El fallo contiene informacion: el anchor aceptado ya es
conservador y la siguiente receta debe recuperar utilidad segura, no volver a
empujar la politica hacia menos bitrate.

## Cambio decidido

Anadir una perdida opcional `safe_advantage_policy_loss` al trainer
`spbc_abr_v2_dpo`.

La perdida:

- toma como referencia la accion que elegiria el checkpoint anchor congelado;
- busca solo acciones validas no marcadas como over-aggressive;
- aplica penalizacion de rebuffer y target-risk a la recompensa por accion;
- crea objetivo solo si la accion segura supera a la referencia por un margen
  claro;
- no empuja nada cuando no hay mejora segura.

Esto complementa `copy_baseline_loss`: copiar el anchor donde no hay mejora
segura y moverse solo donde el dataset DAgger-2 muestra una ganancia segura.

## Ejecucion probe

Ejecutar primero una sola seed corta:

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/run_phase45_v2_spbc_safe_advantage_probe_wsl.sh
```

Por defecto:

```text
seed=450891
epochs=3
```

El probe vuelve a usar:

```text
dataset=~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1
init_checkpoint=~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt
```

## Criterio

Aceptar escalar a multi-seed solo si la seed probe imprime `TRAINED_PASS`, con:

- `best_epoch>0`;
- `gate=true`;
- sin regresion de utility/rebuffer en `2_5_mbps`;
- sin abrir sobre-agresividad global, `2_5_mbps` ni
  `spbc_v2_dpo_on_policy`;
- lectura de `under` y bitrate coherente con recuperacion de utilidad, no con
  desplazamiento inseguro.

Si vuelve a fallback, no insistir con mas PPO/advantage global. En ese caso el
siguiente movimiento debe ser integrar el anchor SPBC actual como candidato
controller offline o pasar a un evaluador/copiloto separado, sin reclamar
mejora hasta Phase 6.

## Limite

Este probe sigue siendo entrenamiento offline. No es benchmark, no registra
controller, no exporta bundle y no autoriza ranking ni afirmacion de mejora QoE.
