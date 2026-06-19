# Decision Phase45 v3 SPBC policy v1 - 2026-06-19

## Proposito

Abrir el primer entrenamiento de la linea `phase45_v3_closedloop_spbc_spc_v1`
como **SPBC puro**:

```text
model_inputs -> policy logits por accion -> bitrate
```

No se integra controller todavia. No se crea bundle. No se ejecuta Phase 6. No
hay benchmark, ranking ni claims de QoE.

## Motivo

El dataset full cerrado ya ha pasado auditorias:

```text
status=PASS
profile=full_v1
samples training=490680 validation=111660
max_buffer_s=60.0
targets=PASS
leakage=PASS
fallback_count=0
high_capacity_safe_target_action0_rate=0.005697
safe_action_presence_rate=1.0
```

La distribucion de targets esta muy cargada a accion 5:

```text
policy_targets={'0': 63617, '1': 36380, '2': 32346, '3': 32612, '4': 44098, '5': 393287}
```

Por tanto, no se debe entrenar una copia ingenua de clase mayoritaria. El primer
SPBC debe ser una policy directa pero entrenada con:

- soft labels del oracle;
- regret por accion;
- penalizacion de probabilidad esperada en acciones de alto regret;
- guardas anti-colapso en alta capacidad;
- reporte por distribucion de acciones.

## Separacion frente a SPC y Neural-MPC

SPC no se usa como segundo modelo runtime en esta decision. Los targets critic
del dataset se usan como supervision para entrenar mejor la policy, no como
copiloto obligatorio.

Neural-MPC no se toca:

```text
phase45_v3_neural_throughput_calibrated_mpc_v1
```

## Dataset

Entrada esperada WSL:

```text
~/TFG/datasets_normalizados/phase45_v3/closedloop_spbc_spc_full_v1
```

El entrenamiento pilot puede usar un subconjunto determinista del full para no
quemar GPU antes de comprobar aprendizaje.

## Gates iniciales

El primer entrenamiento queda en `PASS` solo si:

```text
top1_accuracy >= perfil.top1_accuracy_floor
mean_regret_q_h <= perfil.mean_regret_tolerance
high_capacity_predicted_action0_rate <= perfil.high_capacity_action0_tolerance
catastrophic_predicted_rate <= perfil.catastrophic_action_tolerance
```

Si no pasa, queda `REVIEW` y se analiza antes de lanzar otra variante.

## Siguiente paso autorizado

Implementar:

- modulo `core/phase45_v3/spbc_policy_training.py`;
- script `scripts/train_phase45_v3_spbc_policy.py`;
- wrapper WSL corto para pilot desde full;
- tests unitarios smoke CPU.

No se autoriza todavia:

- bundle;
- controller runtime;
- registro en GUI;
- Phase 6;
- comparativa formal.
