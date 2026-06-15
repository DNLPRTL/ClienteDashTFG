# Decision Phase45 v3 Neural-MPC full v2 tras preset rapido

Fecha: 2026-06-15

## Estado previo

La linea `phase45_v3_neural_throughput_calibrated_mpc_v1` ya dispone de:

- predictor neural de cuantiles futuros de throughput;
- planner MPC con QoE explicita `qoe_linear_v1`;
- bundle experimental validado por hashes;
- controller integrado en Ubuntu cliente;
- ejecuciones Phase 6 `diagnostico` y `rapido` sin fallback neural ni acciones invalidas.

Las salidas siguen siendo diagnosticas:

```text
benchmark_performed=false
ranking_performed=false
no_final_ranking=true
qoe_claims_authorized=false
```

## Observacion del preset rapido

El paquete `20260615_112752_rapido` mostro que la integracion runtime es limpia,
pero revelo una debilidad localizada: una ventana real media-variable produjo un
rebuffer alto en Neural-MPC frente a Robust MPC.

Interpretacion:

- no es un fallo de carga del bundle;
- no es ausencia de inferencia neural;
- no es fallback;
- no es accion invalida;
- no es colapso global a accion baja;
- parece un problema de cobertura/calibracion del predictor/planner ante
  condiciones medias variables.

## Decision

Se aprueba una iteracion `v2` orientada a full dataset/full training antes de
pasar a presets capaces de benchmark.

El primer cambio sera escalar de dataset/entrenamiento pilot a perfil `full_v1`
manteniendo la misma familia tecnica:

```text
modelo: predictor de cuantiles de throughput
planner: NeuralThroughputCalibratedMpcController
QoE: qoe_linear_v1
ladder: [300, 750, 1200, 1850, 2850, 4300] kbps
media_profile_id: paseo_10min_30fps_4s
```

La razon de no cambiar primero arquitectura, loss o planner es aislar la causa.
Si se modifican a la vez datos, entrenamiento, arquitectura y reglas de
decision, no se puede atribuir la mejora o el empeoramiento observado.

## Perfil v2

Dataset externo previsto:

```text
~/TFG/datasets_normalizados/phase45_v3/throughput_quantile_full_v1_neural_mpc_v2
```

Modelo externo previsto:

```text
~/TFG/modelos/phase45_v3/throughput_quantile_predictor/full_v1_neural_mpc_v2
```

Runs diagnosticos externos previstos:

```text
~/TFG/runs_phase45_v3/neural_mpc_full_v1_v2
```

Semillas previstas:

```text
452001 452002 452003
```

El perfil `full_v1` aumenta cobertura respecto al pilot:

```text
train_window_count=4096
validation_window_count=1024
qh_horizon_segments=5
qh_beam_width=24
max_windows_per_trace=4
```

## Gates de lectura

La iteracion no autoriza ranking ni claims. Para plantear bundle v2 debera
mostrar, como minimo:

- training `PASS`;
- evaluacion closed-loop offline `PASS`;
- fallback neural `0`;
- acciones invalidas `0`;
- ausencia de colapso en alta capacidad;
- sin spikes claros de rebuffer frente a Robust MPC en auditoria emparejada;
- resumen pasteable disponible por script versionado.

Si `full_v1` no corrige el caso de riesgo, la siguiente iteracion debera cambiar
una sola hipotesis adicional, por ejemplo calibracion de riesgo/planner, y
compararse contra `v1` y `v2_full`.
