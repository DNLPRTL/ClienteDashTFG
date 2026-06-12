# Decision Phase45 v3 Neural Throughput-Calibrated MPC v1 - 2026-06-12

## Estado de entrada

La linea `phase45_v3_qh_scorer` queda bloqueada como controller directo:

- mejor pilot actual: `pilot_adv_regret_v1`;
- `top1_accuracy=0.788844`;
- `high_capacity_predicted_action0_rate=0.002946`;
- `mean_regret_q_h=0.395739`;
- gate pendiente: `mean_regret_q_h <= 0.35`;
- GRU y hard-negative v1/v2 no mejoran el gate principal.

La lectura aceptada es que el bloqueo no es solo de loss. El scorer intenta
clonar el argmax de un oracle `Q_H(s,a)` cuyo target usa futuro como
`target-only`. En estados de alta variabilidad, dos estados visibles pueden
tener targets muy distintos por futuro inmediato no observable. Por tanto,
seguir ajustando losses sobre `Q_H` no es la via principal.

## Decision

Parar `Q_H scorer` como driver de controller directo.

No ejecutar:

- `full` Q_H scorer;
- mas hard-negative Q_H;
- mas GRU Q_H;
- relajacion del gate `mean_regret_q_h`;
- PPO;
- revival SPBC.

Abrir la linea:

```text
phase45_v3_neural_throughput_calibrated_mpc_v1
```

El controller candidato se formula como:

```text
predictor neuronal de cuantiles de throughput futuro
+
planner MPC explicito sobre qoe_linear_v1
```

La red no elige bitrate. La red predice log-ratios de throughput futuro frente
a una base robusta de throughput reciente. El planner elige la accion mediante
MPC auditable.

## Justificacion tecnica

La linea queda alineada con el corpus operativo:

- Comyco motiva imitation learning eficiente, pero tambien muestra el riesgo de
  clonar expertos offline cuando los estados ejecutados se desplazan.
- Puffer/Fugu motiva limitar ML a predicciones comprobables y usar control
  clasico MPC para la decision.
- Oboe/ANT motivan especializar o condicionar decisiones por dinamica de red,
  throughput y variabilidad.

Para este proyecto, la formulacion Neural-MPC evita que el modelo tenga que
aprender directamente una accion oracle parcialmente no identificable desde los
inputs visibles. La incertidumbre se convierte en cuantiles usados por el MPC.

## Contrato implementado

Archivos principales:

```text
core/phase45_v3/throughput_quantile_dataset.py
core/phase45_v3/throughput_quantile_model.py
core/phase45_v3/neural_mpc_controller.py
core/phase45_v3/neural_mpc_training.py
core/phase45_v3/neural_mpc_evaluation.py
scripts/generate_phase45_v3_throughput_quantile_dataset.py
scripts/train_phase45_v3_throughput_quantile_predictor.py
scripts/evaluate_phase45_v3_neural_mpc_closedloop.py
scripts/run_phase45_v3_neural_mpc_pilot_wsl.sh
```

El dataset usa:

- mismas trazas y ventanas Phase45 v3;
- estado closed-loop con `max_buffer_s=60.0`;
- `qoe_linear_v1`;
- features runtime-visible;
- futuro solo como target;
- split `eval` excluido;
- metadatos separados de `model_inputs`.

Targets:

```text
base_tp = harmonic_mean(throughput_history_bps)
target_log_ratio_h = log((future_tp_h + eps) / (base_tp + eps))
horizon=5
quantiles=0.10,0.25,0.50,0.75
```

Modelo:

```text
MLP(context_features) -> horizon x quantiles
loss = pinball + crossing_penalty + temporal_smoothness_penalty
```

Planner:

```text
buffer < 4s         -> q10
4s <= buffer < 12s  -> q25
12s <= buffer <20s  -> blend(q25,q50)
buffer >=20s        -> q50
```

El MPC enumera secuencias con:

```text
reward = bitrate_mbps - 4.3 * rebuffer_s - smoothness_mbps
```

## Runbook WSL

```bash
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate
bash scripts/run_phase45_v3_neural_mpc_pilot_wsl.sh
```

Salidas externas por defecto:

```text
~/TFG/datasets_normalizados/phase45_v3/throughput_quantile_pilot_v1
~/TFG/modelos/phase45_v3/throughput_quantile_predictor/pilot_v1_seed451001
~/TFG/runs_phase45_v3/neural_mpc_pilot_v1_seed451001
```

## Gates diagnosticos

La evaluacion closed-loop es diagnostica, no benchmark.

Gates internos:

- `high_capacity_action0_rate <= 0.05`;
- `high_capacity_mean_bitrate_ratio_vs_robust_mpc >= 0.70`;
- `fallback_rate == 0`;
- `invalid_action_count == 0`;
- rebuffer en bucket `2_5_mbps` no debe explotar frente a `robust_mpc`;
- QoE media no debe ser catastroficamente peor que `robust_mpc`.

Estos gates no autorizan ganador ni mejora de QoE. Si pasan, el siguiente paso
seria multi-seed, dataset mayor y Phase6 diagnostico. Si fallan, el fallo queda
separado entre predictor, cuantiles, planner o features.

## Rol restante de Q_H scorer

`Q_H scorer` queda como experimento negativo, diagnostico y posible ablation.
No se borra, pero no debe seguir consumiendo ejecuciones como via principal
salvo auditoria objetiva de inconsistencia en oracle, mascara, buffer, reward o
features.

## Calibracion posterior al primer piloto diagnostico

Primer piloto WSL/ROCm:

```text
~/TFG/runs_phase45_v3/neural_mpc_pilot_v1_seed451001
```

Lectura objetiva del reporte:

- no hubo colapso high-capacity a accion 0;
- `fallback_rate=0.0`;
- `invalid_action_count=0`;
- `high_capacity_mean_bitrate_ratio_vs_robust_mpc=1.0`;
- estado global `REVIEW` por fallo en
  `bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean`;
- valor observado: `+1.3203728087318694 s`;
- umbral diagnostico: `<= +1.0 s`.

El fallo no corresponde al bloqueo previo de Q_H/SPBC. El sintoma nuevo es
agresividad excesiva en una ventana `2_5_mbps`, especialmente en:

```text
trace_fcc_measuring_broadband_america_unit_26710_curr_httpgetmt_csv_acb8d18f84f0
```

Decision de calibracion:

- mantener predictor, dataset y training intactos;
- no abrir otra arquitectura;
- no relajar gates;
- hacer mas prudente solo la seleccion de cuantiles por buffer medio;
- retrasar la mezcla `q25/q50` para no usar prediccion mediana con colchones de
  buffer todavia fragiles en redes `2_5_mbps`.

Esta calibracion sigue siendo diagnostica. No autoriza benchmark, ranking,
ganador ni afirmacion de mejora QoE.
