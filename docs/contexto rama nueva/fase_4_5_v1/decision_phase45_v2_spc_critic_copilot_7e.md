# Decision tecnica 7E - SPC critic/copilot calibrado

## Estado

`SPC solo` queda descartado como policy/conductor autonomo. Tambien queda
descartado el camino `SPC safe-rank` como policy, porque deformo la calibracion
de riesgo y empeoro utility, rebuffer y sobre-agresividad frente al SPBC
congelado.

Esto no descarta el rol original mas defendible del SPC:

```text
SPBC = conductor / policy decisora
SPC  = critico predictivo por accion / copiloto
```

Tras el fallo del piloto `SPBC residual safe-rank v1`, no conviene seguir
tocando la policy SPBC con nuevas perdidas invasivas. El candidato offline
SPBC principal sigue siendo:

```text
~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt
```

## Cambio decidido

Crear un perfil nuevo de entrenamiento:

```text
spc_abr_v2_reward_risk / critic_v1
```

Su objetivo no es ganar como `SPC only`. Su objetivo es producir cabezas
predictivas calibradas para que el evaluador hibrido pueda decidir si conviene
mantener, vetar o reordenar localmente una accion del SPBC.

Cambios de filosofia:

- neutralizar el score compuesto como fuerza principal;
- bajar CE/pairwise para que no conviertan el modelo en policy;
- reforzar targets predictivos por accion: `reward_n`, rebuffer, riesgo,
  `qoe_gap` y smoothness;
- reforzar falsos negativos de riesgo en seleccion de checkpoint;
- ponderar mas `2_5_mbps`, errores severos y acciones con rebuffer agresivo;
- no usar `safe_utility_rank_loss` ni `over_aggressive_score_loss` como martillo
  de policy.

## Evaluador offline

El evaluador hibrido queda reforzado para medir si el copiloto interviene de
forma real y util:

- `intervention_rate`;
- `useful_intervention_rate`;
- `harmful_intervention_rate`;
- delta medio de reward y rebuffer en las intervenciones;
- tasa de arreglos/regresiones de sobre-agresividad;
- gates opcionales de intervencion minima para evitar aprobar un copiloto que
  no hace nada.

Los modos evaluados siguen siendo:

```text
SPBC only
SPC only reward-only                 # diagnostico
SPBC + SPC veto-only
SPBC top-k + SPC rerank, k=2
```

## Runner WSL

Ejecutar:

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/run_phase45_v2_spc_critic_copilot_wsl.sh
```

El runner entrena tres seeds:

```text
critic_copilot_dagger2_seed_450871_v1
critic_copilot_dagger2_seed_450872_v1
critic_copilot_dagger2_seed_450873_v1
```

y las evalua como copiloto con cuatro configuraciones:

```text
strict         risk=0.35 rb=0.03
balanced       risk=0.45 rb=0.05
risk_guard     risk=0.35 rb=0.10
rebuffer_guard risk=0.50 rb=0.03
```

Resumen:

```bash
python3 scripts/summarize_phase45_v2_spc_critic_copilot.py
```

## Criterio de lectura

No aceptar `SPC only` como criterio principal. Mirar primero `veto_only` y
`topk_rerank` frente a `SPBC only`.

Un resultado prometedor debe cumplir:

- no empeorar `over_aggressive` global, `2_5_mbps` ni
  `spbc_v2_dpo_on_policy`;
- no empeorar rebuffer regret;
- mantener falsos negativos de riesgo bajos;
- intervenir de forma no trivial;
- tener `useful_intervention_rate` razonable;
- no comprar las mejoras con una perdida grande de utility.

Si no aparece un copiloto no trivial y estable, la conclusion correcta sera
mantener `SPBC only` como candidato principal y no gastar Phase 6 ni integracion
en este SPC.

## Guardrails

Este bloque no exporta bundle, no registra controller y no ejecuta Phase 6. No
hay benchmark, ranking, ganador ni afirmacion de mejora QoE.
