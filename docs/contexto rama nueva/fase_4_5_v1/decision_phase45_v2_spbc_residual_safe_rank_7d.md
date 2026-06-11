# Decision tecnica 7D - piloto SPBC residual safe-rank

## Estado

No sustituir todavia el candidato offline
`spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1`.

Los estudios criticos adjuntos no invalidan por completo el SPBC actual, pero
si senalan una tension real:

- el informe orientado a PPO trata el SPBC como baseline fuerte y recomienda
  fine-tuning seguro, no un reemplazo inmediato;
- el informe residual critica el antiguo `safe_margin_v1`, especialmente el
  fallback `best_epoch=0`;
- esa critica directa queda parcialmente superada por `anchor_safe_rank`, que
  ya selecciono un epoch entrenado y paso el gate;
- la critica conceptual sigue viva: el SPBC aceptado es conservador y puede
  dejar utilidad por la via de `under_aggressive_rate_vs_oracle`.

Por tanto, el siguiente paso no es integrar controller ni lanzar Phase 6. El
siguiente paso es un piloto offline barato que introduzca anclaje residual en
el entrenador actual.

## Cambio decidido

Extender `spbc_abr_v2_dpo` solo a nivel de entrenamiento con tres perdidas
nuevas:

- `safe_improvement_rank_loss`: empuja la mejor accion segura solo si supera
  con margen de reward a la accion elegida por la referencia congelada.
- `copy_baseline_loss`: copia la distribucion de la referencia cuando no existe
  una mejora segura clara.
- `residual_logit_l2_loss`: limita la deriva de logits frente a la referencia
  en acciones validas.

Esto aproxima la recomendacion residual sin crear todavia una arquitectura
SPIBB completa ni un wrapper residual de runtime. El checkpoint sigue usando el
contrato normal `spbc_abr_v2_dpo`, y la referencia congelada recomendada es:

```text
~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt
```

## Piloto WSL

Ejecutar en WSL2/ROCm:

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/run_phase45_v2_spbc_residual_safe_rank_pilot_wsl.sh
```

El script genera tres seeds:

```text
pilot_dagger2_residual_safe_rank_seed_450861_v1
pilot_dagger2_residual_safe_rank_seed_450862_v1
pilot_dagger2_residual_safe_rank_seed_450863_v1
```

y resume con:

```bash
python3 scripts/summarize_phase45_v2_spbc_residual_safe_rank_pilot.py
```

## Criterio de lectura

Este piloto no es benchmark. La lectura debe revisar, como minimo:

- `selected_checkpoint_safety_gate.passed`;
- `best_epoch` frente a fallback;
- over-aggressive global, `2_5_mbps` y `spbc_v2_dpo_on_policy`;
- regret de utilidad y rebuffer global, `2_5_mbps` y `spbc_v2_dpo_on_policy`;
- `under_aggressive_rate_vs_oracle` y bitrate medio como coste de
  conservadurismo;
- nuevas perdidas `safe_improvement_rank_loss`, `copy_baseline_loss` y
  `residual_logit_l2_loss`.

Si el piloto vuelve a fallback o compra utilidad con mas sobre-agresividad, se
rechaza y se conserva `full_v2_anchor_safe_rank_v1`. Si pasa de forma estable,
se podra decidir si escalar a full o pasar a una etapa PPO/controlada.

## Guardrails

No registrar controller, no exportar bundle y no ejecutar Phase 6 por este
cambio.

Los artefactos deben mantener:

```text
benchmark_performed=false
outputs_are_benchmark_results=false
ranking_performed=false
no_final_ranking=true
bundle_exported=false
controller_registered=false
qoe_improvement_claimed=false
```

Decision: autorizar solo el piloto offline multi-seed residual safe-rank. No
hay ganador, ranking ni afirmacion de mejora QoE.
