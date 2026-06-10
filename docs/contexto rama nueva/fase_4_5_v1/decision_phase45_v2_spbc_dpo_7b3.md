# Decision tecnica 7B.3 - spbc_abr_v2_dpo utility/risk multitask

## Contexto

Los pilots 7B.2 mostraron una mejora fuerte frente al entrenamiento CE+DPO
inicial: menor `qoe_gap`, menor rebuffer estimado y mejor comportamiento en
`2_5_mbps`. Aun asi, el ajuste `focus` solo aporto ganancias pequenas y seguia
dejando una decision pendiente antes de gastar `full_v1`.

La evidencia sugiere que seguir moviendo pesos globales tiene rendimiento
decreciente. El dataset v2 ya contiene una superficie completa por accion
(`reward_n`, `estimated_rebuffer_s`, `qoe_gap`, riesgo diagnostico), pero el
modelo la estaba usando sobre todo como objetivo indirecto sobre logits.

## Decision

Mantener intacto el dataset `phase45v2_preference_onpolicy_dataset_v1` y mejorar
solo el entrenamiento `spbc_abr_v2_dpo`:

- seleccionar el mejor checkpoint por `validation_selection_score`, no por
  `validation_loss` cruda;
- calcular ese score con regret de utilidad, regret de rebuffer, tasa
  over-aggressive, invalid actions y foco explicito en `2_5_mbps`;
- anadir cabezas auxiliares por accion para predecir `reward_n`, rebuffer
  capado y target risk;
- fusionar logits de politica con utilidad/riesgo predichos, manteniendo que el
  forward solo consuma `context`, `candidates` y `action_mask`;
- inicializar las cabezas auxiliares a cero para que un checkpoint
  `spbc_abr_v1/full_v1` arranque semanticamente como la referencia congelada.

## Justificacion academica

La decision combina tres lecturas del corpus operativo:

- Comyco: la imitacion debe usar estados on-policy y feedback experto, no solo
  etiquetas estaticas.
- Puffer/Fugu: los learned components son mas defendibles cuando predicen algo
  verificable y el control sigue siendo auditable.
- Especializacion por regimen: los promedios globales esconden fallos de cola;
  `2_5_mbps` debe pesar en la seleccion de checkpoint.

## Limites

Esto sigue siendo entrenamiento offline. No registra controller, no exporta
bundle, no ejecuta Phase 6 y no autoriza benchmark, ranking, ganador ni mejora
QoE. Las cabezas auxiliares usan targets solo durante entrenamiento; esos campos
siguen prohibidos como inputs.
