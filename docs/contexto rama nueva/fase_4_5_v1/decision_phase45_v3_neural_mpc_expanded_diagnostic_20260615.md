# Decision Phase45 v3 Neural-MPC Expanded Diagnostic - 2026-06-15

## Proposito

Preparar una ejecucion diagnostica ampliada de
`phase45_v3_neural_throughput_calibrated_mpc_v1`.

Esta ejecucion no es benchmark, no produce ranking, no declara ganador, no
autoriza afirmaciones de mejora QoE y no sustituye a Phase 6 ni a la validacion
formal en Ubuntu cliente.

El objetivo es comprobar si el PASS del piloto de 8 ventanas se mantiene al
subir cobertura diagnostica:

```text
3 seeds de entrenamiento
32 ventanas de validacion por seed
perfil de dataset pilot
```

## Estado reconstruido de la implementacion

### 1. Linea anterior bloqueada

La linea `phase45_v3_qh_scorer` quedo bloqueada como driver principal. El mejor
piloto no cerraba el gate de regret y las variantes de hard-negatives, GRU y
losses no daban una mejora suficiente.

Lectura tecnica aceptada:

- el scorer intentaba aprender una accion o valor `Q_H(s,a)`;
- el target dependia de futuro usado solo como target;
- estados visibles parecidos podian tener acciones oracle distintas por futuro
  inmediato no observable;
- seguir ajustando loss sobre accion/score no parecia la via principal.

### 2. Cambio de enfoque

Se abrio:

```text
phase45_v3_neural_throughput_calibrated_mpc_v1
```

La red neuronal no elige bitrate directamente. La arquitectura queda:

```text
estado visible del cliente
-> predictor neuronal de cuantiles de throughput futuro
-> planner MPC explicito con qoe_linear_v1
-> accion ABR
```

Esto separa aprendizaje y control:

- aprendizaje: estimar incertidumbre de throughput futuro;
- control: elegir accion con MPC auditable y formula QoE cerrada.

### 3. Dataset derivado

El dataset nuevo no es V2/V3/V4 formal. Es un dataset derivado de Phase45 v3:

```text
throughput_quantile
```

Usa trazas normalizadas y manifest curado de Phase 3. No usa CSVs runtime ni
dry-runs legacy.

Entradas del modelo:

- features visibles en runtime;
- historial de throughput;
- buffer;
- informacion de escalera y estado que un controller podria conocer.

Targets:

```text
base_tp = harmonic_mean(throughput_history_bps)
target_log_ratio_h = log((future_tp_h + eps) / (base_tp + eps))
horizon=5
quantiles=0.10,0.25,0.50,0.75
```

El futuro throughput solo se usa como target offline. No se entrega al
controller durante la decision.

### 4. Modelo

Modelo actual:

```text
MLP(context_features) -> horizon x quantiles
loss = pinball + crossing_penalty + temporal_smoothness_penalty
```

Esto es mas defendible que imitation learning directo de `robust_mpc`, porque
no se limita a copiar acciones de un teacher. Aprende una variable fisica
intermedia: throughput futuro calibrado por cuantiles.

### 5. Controller

El controller:

- carga el predictor de cuantiles;
- selecciona una curva de throughput segun buffer;
- enumera secuencias MPC;
- puntua con `qoe_linear_v1`;
- registra telemetria de cuantil elegido, secuencia y fallback;
- cae a `robust_mpc` solo si hay error de prediccion o carga.

Tras calibracion v1.1, la seleccion de cuantiles es:

```text
buffer < 4s         -> q10
4s <= buffer < 12s  -> q25
12s <= buffer <20s  -> blend(q25,q50)
buffer >=20s        -> q50
```

### 6. Pilotos ejecutados

Primer piloto:

- `status=REVIEW`;
- no hubo colapso a accion 0 en high-capacity;
- fallo: rebuffer extra en bucket `2_5_mbps`;
- `bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean=+1.3203728087318694 s`.

Calibracion aplicada:

- no se cambio dataset;
- no se cambio predictor;
- no se cambio training;
- no se relajaron gates;
- se hizo mas prudente el planner en buffer medio.

Segundo piloto:

- `status=PASS`;
- `failed_gates=[]`;
- `bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean=+0.08001783155587106 s`;
- `fallback_rate=0.0`;
- `invalid_action_count=0`;
- `high_capacity_action0_rate=0.0`;
- `high_capacity_mean_bitrate_ratio_vs_robust_mpc=1.0`;
- `qoe_delta_vs_robust_mpc_mean=-0.010293264076880151`.

Lectura permitida:

- el bloqueo de colapso a accion 0 no reaparece;
- el fallo puntual de rebuffer queda corregido en el piloto;
- no se debe seguir afinando contra las mismas 8 ventanas;
- hace falta diagnostico ampliado.

## Influencia de investigaciones de apoyo

### Comyco

Comyco justifica que el aprendizaje por imitacion puede servir para obtener
controllers ABR ligeros, pero tambien muestra el riesgo de clonar decisiones de
un experto offline cuando la distribucion de estados cambia.

Influencia en esta via:

- se evita volver a una imitacion simple de `robust_mpc`;
- el aprendizaje se desplaza hacia una prediccion intermedia;
- `Q_H scorer` queda como experimento negativo/ablacion, no driver principal.

### Puffer/Fugu

Puffer/Fugu apoya usar ML para predicciones medibles y dejar la decision final
en un esquema de control interpretable.

Influencia en esta via:

- la red predice throughput futuro;
- el MPC toma la decision final;
- la telemetria permite auditar cuantiles, secuencias y rebuffer estimado.

### Oboe y ANT

Oboe y ANT motivan adaptar decisiones ABR a condiciones de red y variabilidad,
en vez de usar una politica unica no condicionada.

Influencia en esta via:

- el planner cambia cuantil segun buffer;
- el predictor aprende distribuciones de throughput condicionadas al estado;
- la calibracion v1.1 aumenta prudencia en zonas de red media-baja.

### Robust MPC

`robust_mpc` deja de ser un teacher que se copia. Ahora funciona como:

- baseline tecnico de referencia diagnostica;
- fallback auditado;
- punto de comparacion para gates internos.

## Diagnostico ampliado definido

Script:

```bash
bash scripts/run_phase45_v3_neural_mpc_expanded_diagnostic_wsl.sh
```

Valores por defecto:

```text
dataset_dir=~/TFG/datasets_normalizados/phase45_v3/throughput_quantile_expanded_diag_v1
model_root=~/TFG/modelos/phase45_v3/throughput_quantile_predictor/expanded_diag_v1
run_root=~/TFG/runs_phase45_v3/neural_mpc_expanded_diag_v1
seeds=451001 451002 451003
eval_windows=32
epochs=40
```

Se puede cambiar sin editar codigo:

```bash
PHASE45_V3_NEURAL_MPC_EXPANDED_SEEDS="451001 451002 451003" \
PHASE45_V3_NEURAL_MPC_EXPANDED_EVAL_WINDOWS=32 \
bash scripts/run_phase45_v3_neural_mpc_expanded_diagnostic_wsl.sh
```

El script genera dataset derivado, entrena un predictor por seed y evalua cada
checkpoint en closed-loop offline diagnostico.

Flags conceptuales esperados:

```text
diagnostic_only=true
benchmark_performed=false
ranking_performed=false
no_final_ranking=true
qoe_claims_authorized=false
```

## Script para pegar resultados

Tras ejecutar el diagnostico ampliado:

```bash
bash scripts/print_phase45_v3_neural_mpc_expanded_diagnostic_summary_wsl.sh
```

El script imprime un JSON compacto con:

- estado por seed;
- gates fallidos por seed;
- deltas QoE/rebuffer principales;
- maximos/minimos agregados;
- rutas de outputs;
- flags de no benchmark/no ranking.

Ese JSON es el contenido que Daniel debe pegar en el chat.

## Criterio de lectura

Si el diagnostico ampliado pasa:

- no afirmar ganador;
- no afirmar mejora QoE;
- documentar estabilidad diagnostica;
- preparar siguiente paso hacia candidato IA experimental.

Si falla:

- no relajar gates;
- no ajustar contra una sola ventana;
- separar fallo por seed, bucket y ventana;
- decidir si el problema esta en predictor, dataset, planner o cobertura.

## Posibles pasos futuros

### Paso A - Si el ampliado pasa

1. Documentar PASS ampliado.
2. Preparar `candidate_model_experimental_v1` como concepto, no como ganador.
3. Definir empaquetado reproducible del checkpoint seleccionado.
4. Integrar controller guarded en registry solo con contrato explicito.
5. Ejecutar validacion diagnostica en Ubuntu cliente.
6. Preparar entrada a Phase 6 formal cuando el protocolo lo autorice.

### Paso B - Si el ampliado queda REVIEW

1. Analizar resumen por seed.
2. Localizar gates fallidos.
3. Revisar ventanas problematicas.
4. Evitar sobreajuste a una sola traza.
5. Decidir entre calibracion de planner, aumento de dataset o ajuste de loss.

### Paso C - Si aparece colapso a accion 0

1. Parar la linea como candidata.
2. Auditar predicciones por cuantil y action histogram.
3. Comparar contra el fallo Q_H/SPBC.
4. Generar informe de bloqueo si se repite en mas de dos ejecuciones.

## Estado permitido tras esta decision

El proyecto puede ejecutar diagnostico ampliado en WSL2/ROCm.

No queda autorizado:

- benchmark;
- ranking;
- ganador;
- claim de mejora QoE;
- integracion runtime del controller sin contrato posterior.

## Resultado del primer diagnostico ampliado

Ejecucion WSL/ROCm:

```text
run_root=/home/danie/TFG/runs_phase45_v3/neural_mpc_expanded_diag_v1
model_root=/home/danie/TFG/modelos/phase45_v3/throughput_quantile_predictor/expanded_diag_v1
seeds=451001,451002,451003
window_count=32 por seed
session_count=128 por seed
```

Resultado:

```text
status=REVIEW
all_reports_passed=false
failed_gate_counts={"fallback_rate": 3}
```

Lectura objetiva:

- el diagnostico ampliado no permite avanzar todavia a candidato IA
  experimental;
- todos los fallos son por `fallback_rate`;
- no reaparece colapso high-capacity a accion 0:
  `high_capacity_action0_rate_max=0.0`;
- no hay acciones invalidas: `invalid_action_count_max=0.0`;
- el ratio high-capacity frente a `robust_mpc` se mantiene:
  `high_capacity_mean_bitrate_ratio_min=1.0`;
- el rebuffer extra en `2_5_mbps` queda bajo el umbral diagnostico:
  `bucket_2_5_mbps_rebuffer_delta_max=0.27579423542196324`;
- `qoe_delta_vs_robust_mpc_mean_across_seeds=-0.03270654207442248`.

Se inspeccionaron ventanas con `fallback_count` alto y la causa reproducida fue:

```text
Phase45V3NeuralMpcError: prediction quantiles cross
```

Decision:

- no relajar el gate `fallback_rate == 0`;
- no declarar candidato;
- no ajustar contra QoE ni rebuffer, porque esos gates no son el problema;
- aplicar postproceso monotono determinista sobre las filas de cuantiles
  emitidas por el predictor cargado desde checkpoint;
- repetir el diagnostico ampliado con el mismo runbook.

Justificacion:

El modelo se entrena con penalizacion de cruce de cuantiles, pero esa
penalizacion no garantiza monotonia exacta en todos los estados closed-loop.
Ordenar las filas de cuantiles en inferencia es un postproceso estandar y
auditable para convertir la salida neural en una funcion cuantilica valida
antes de entregarla al MPC. No usa futuro, no cambia el dataset, no relaja
gates y no convierte la ejecucion en benchmark.
