# Decision Phase45 v3 - Q_H scorer hard-negative pilot

Fecha: 2026-06-12

Estado: decision operativa para un experimento trainer-only. No es benchmark, no
integra runtime, no autoriza ranking ni afirmaciones de mejora de QoE.

## Contexto

El bloqueo documentado para `phase45_v3_qh_scorer` muestra que el mejor pilot
actual es:

```text
run=qh_scorer_pilot_adv_regret_dataset_pilot_seed450924_v1
profile=pilot_adv_regret_v1
architecture=shared_mlp_qh_candidate_scorer
status=REVIEW
mean_regret_q_h=0.395739
gate_mean_regret_q_h=0.35
```

Los gates de `top1_accuracy` y anti-colapso en alta capacidad pasan. El bloqueo
restante se concentra en la cola de regret y en slices concretos:

```text
2_5_mbps
qh_plus_one
buffers bajos/medios
predicciones con alto regret en acciones alternativas
```

El GRU `pilot_adv_regret_gru_v1` empeoro frente al MLP, por lo que no se cambia
arquitectura en este paso.

## Decision

Crear un perfil nuevo:

```text
pilot_adv_regret_hardneg_v1
```

La decision consiste en mantener el scorer MLP y anadir objetivo hard-negative
cost-sensitive:

```text
structured_cost_hinge_loss
catastrophic_prob_loss
slice-aware sample weighting
```

Los pesos de slice se calculan con metadata y targets de entrenamiento, pero no
entran al forward del modelo ni se registran como feature visible por el
controller.

## Limites

No se hace:

```text
full dataset
runtime integration
relajar gates
repetir GRU
volver a SPBC/PPO
benchmark
ranking
winner
QoE improvement claim
```

## Criterio inmediato

El single-seed pilot solo desbloquea el siguiente paso si pasa:

```text
top1_accuracy >= 0.55
mean_regret_q_h <= 0.35
high_capacity_predicted_action0_rate <= 0.05
```

Si pasa, el siguiente paso sigue siendo multi-seed pilot, no full ni runtime.
