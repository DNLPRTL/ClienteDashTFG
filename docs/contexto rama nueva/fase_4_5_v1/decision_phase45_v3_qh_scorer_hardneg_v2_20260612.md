# Decision Phase45 v3 QH scorer hard-negative v2 - 2026-06-12

## Estado de entrada

El perfil `pilot_adv_regret_hardneg_v1` se ejecuto sobre el dataset pilot
cerrado de Phase45 v3:

- run: `qh_scorer_pilot_adv_regret_hardneg_dataset_pilot_seed450926_v1`
- status: `REVIEW`
- gate fallido: `mean_regret_q_h`
- `top1_accuracy=0.797177`
- `mean_regret_q_h=0.401737`
- `p95_regret_q_h=1.550001`
- `high_capacity_predicted_action0_rate=0.004714`
- `regret_gt_2_0_rate=0.041667`
- `training_sample_weight_summary.mean=3.854708`
- `training_sample_weight_summary.p95=5.0`
- `training_sample_weight_summary.max=5.0`

## Lectura tecnica

El perfil v1 no colapsa a accion 0 en alta capacidad y mejora top-1, pero no
supera el gate de regret. El resumen de pesos indica saturacion: demasiadas
muestras alcanzan el peso maximo, por lo que el entrenamiento deja de ser un
hard-negative focalizado y se convierte en un objetivo deformado.

El analisis de errores muestra que el dano se concentra especialmente en:

- throughput `2_5_mbps`
- buffers `04_08s`, `08_16s` y `16_32s`
- rollouts `qh_plus_one` y `startup_conservative`
- trazas variables, especialmente movilidad activa y segmentos con alta
  variabilidad

## Decision

Crear `pilot_adv_regret_hardneg_v2` como variante mas quirurgica, no mas
agresiva. La v2 mantiene el aprendizaje por regret/ventaja, pero reduce la
saturacion de pesos y desplaza el coste catastrofico a errores realmente graves.

Cambios principales frente a v1:

- `slice_weight_max`: `5.0 -> 3.0`
- `catastrophic_regret_threshold`: `2.0 -> 5.0`
- `catastrophic_prob_loss_weight`: `2.40 -> 0.85`
- `structured_cost_hinge_loss_weight`: `2.00 -> 0.75`
- `structured_cost_margin_scale`: `0.55 -> 0.35`
- `slice_weight_throughput_2_5`: `1.25 -> 0.35`
- `slice_weight_buffer_16_32`: `0.35 -> 0.0`
- `slice_weight_rollout_qh_plus_one`: `1.00 -> 0.35`
- `slice_weight_max_regret_5`: `1.25 -> 0.60`
- `slice_weight_max_regret_20`: `1.50 -> 0.80`

## Criterio de avance

No pasar a full, multi-seed ni runtime si el pilot v2 no mejora con claridad el
bloqueo actual. El criterio minimo de avance es:

- `mean_regret_q_h <= 0.35`, o
- mejora clara frente al mejor pilot anterior con reduccion simultanea de
  `mean_regret_q_h` y cola severa.

Si v2 no aporta avance real, se debe actualizar el informe objetivo de bloqueo
antes de lanzar mas variantes.
