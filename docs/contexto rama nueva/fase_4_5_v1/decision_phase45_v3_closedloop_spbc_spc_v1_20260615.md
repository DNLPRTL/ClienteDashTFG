# Decision Phase45 v3 Closed-loop SPBC/SPC v1 - 2026-06-15

## Proposito

Abrir una linea paralela de investigacion IA ABR basada en policy/critic
cerrados en el entorno Phase45 v3, sin alterar la linea viva
`phase45_v3_neural_throughput_calibrated_mpc_v1`.

Esta decision no crea codigo todavia, no entrena modelos, no registra
controllers, no exporta bundles y no ejecuta Phase 6. Su funcion es fijar el
contrato antes del primer dataset pilot.

## Motivacion

El fracaso del SPBC historico no invalida necesariamente la idea de una policy
neural o un critic neural. Lo que invalida es el modo en que se entreno y se
interpreto:

- la dinamica offline antigua no reproducia completamente el cliente;
- el modelo se evaluo/integro sin haber descubierto antes el colapso runtime;
- el entorno antiguo usaba una dinamica de buffer incompatible con el cliente
  final observado;
- los surrogates offline no predijeron el comportamiento real en Phase 6
  diagnostico/rapido;
- varios intentos posteriores solo pasaban por fallback o empeoraban gates.

La nueva oportunidad existe porque Phase45 v3 ya dispone de un entorno cerrado
compatible con la dinamica ABR del cliente:

```text
segment_duration_s=4.0
max_buffer_s=60.0
bitrates_kbps=[300,750,1200,1850,2850,4300]
qoe_formula_version=qoe_linear_v1
reward=bitrate_mbps - 4.3 * rebuffer_s - smoothness_mbps
inputs_runtime_visible_only=true
future_information_target_only=true
```

## Separacion frente a Neural-MPC v1

La linea actual viva es:

```text
phase45_v3_neural_throughput_calibrated_mpc_v1
```

Su filosofia es:

```text
predictor neuronal de cuantiles de throughput
+
planner MPC explicito
```

La nueva linea propuesta es:

```text
phase45_v3_closedloop_spbc_spc_v1
```

Su filosofia es:

```text
SPBC-v3 = policy neural candidata
SPC-v3  = critic predictivo por accion
hybrid  = SPBC propone + SPC audita/veta/reordena localmente
```

Prohibido en esta linea:

- tocar codigo, pesos, runbooks o bundle de Neural-MPC v1;
- cambiar el registry del controller Neural-MPC;
- reutilizar el dataset Phase45 v1/v2 SPBC como evidencia principal;
- llamar a esta linea continuacion directa de `spbc_abr_v2_dpo`;
- saltar directamente a full, bundle o runtime.

## Hipotesis tecnica

Si SPBC/SPC se entrenan desde cero en el entorno cerrado que replica el cliente,
pueden producir una policy/critic mas coherente que los modelos historicos
entrenados con dinamica desalineada.

La hipotesis no es que SPBC deba ganar a Neural-MPC. La hipotesis es que una
linea policy/critic cerrada puede servir como:

- candidato alternativo;
- ablation de filosofia aprendizaje-directo frente a predictor+planner;
- evidencia academica de por que una ruta funciona o falla;
- posible hybrid controller si pasa gates estrictos.

## Dataset nuevo requerido

Hace falta un dataset nuevo. No basta con ampliar V2 ni reutilizar el viejo
dataset SPBC.

Nombre propuesto:

```text
phase45_v3_closedloop_spbc_spc_pilot_v1
```

Ruta WSL propuesta:

```text
~/TFG/datasets_normalizados/phase45_v3/closedloop_spbc_spc_pilot_v1
```

Debe generarse desde:

- manifest curado Phase 3;
- entorno `core/phase45_v3/abr_closed_loop_env.py`;
- media profile `paseo_10min_30fps_4s`;
- dinamica de 30 segmentos;
- fragmentos de 4 s;
- buffer maximo 60 s;
- escalera real de seis bitrates;
- reward `qoe_linear_v1`;
- splits sin leakage.

## Targets previstos

El dataset debe soportar dos tareas hermanas:

### SPBC-v3 policy

Entradas:

```text
model_inputs.context
model_inputs.candidates
action_mask
```

Targets offline:

```text
best_action_by_closed_loop_oracle
per_action_reward_n
per_action_rebuffer_s
per_action_smoothness_mbps
per_action_valid
```

### SPC-v3 critic

Entradas:

```text
model_inputs.context
model_inputs.candidates
action_mask
```

Targets por accion:

```text
reward_n
estimated_rebuffer_s
smoothness_mbps
target_risk
qoe_gap_or_regret
```

`trace_id`, `dataset_id`, `split`, `group_id`, `leakage_group`, metadata,
rollout labels y futuro throughput no pueden ser inputs.

## Evaluacion pilot

El primer bloque debe ser barato:

```text
dataset pilot
training pilot 1 seed
summary
error analysis
```

Solo si hay avance real:

```text
pilot multi-seed
closed-loop diagnostic offline
```

Solo despues:

```text
bundle experimental
smoke runtime
Phase 6 diagnostico
Phase 6 rapido
```

Full dataset/full training queda prohibido hasta superar ese embudo.

## Gates minimos desde el primer pilot

No aceptar un modelo que:

- selecciona `best_epoch=0`;
- pasa por fallback;
- colapsa a accion 0 en alta capacidad;
- tiene acciones invalidas;
- empeora de forma clara `2_5_mbps`;
- compra bitrate con rebuffer;
- copia una referencia sin aprendizaje real;
- requiere relajar gates para avanzar.

Gates diagnosticos iniciales:

```text
high_capacity_action0_rate <= 0.05
invalid_action_count == 0
fallback_rate == 0 para evaluacion offline nominal
bucket_2_5_mbps_rebuffer_delta controlado
under_aggressive y bitrate medio reportados
error por accion y por bucket reportado
```

## Primer paso autorizado

El primer paso autorizado tras esta decision es:

```text
disenar e implementar generador de dataset pilot closedloop_spbc_spc_v1
```

Ese paso debe producir:

- constantes/schema;
- generador versionado;
- validador/auditorias;
- resumen de dataset;
- tests unitarios de paridad/leakage/schema;
- runbook WSL corto.

No se autoriza todavia:

- entrenamiento;
- bundle;
- controller runtime;
- Phase 6;
- ranking;
- claim de QoE.

## Relacion con el proceso estandar

Esta linea debe seguir:

```text
docs/contexto rama nueva/fase_4_5_v1/proceso_desarrollo_ia_abr.md
```

Si se bloquea durante mas de dos ejecuciones sin avance de paso, se debe crear
informe autosuficiente de bloqueo antes de continuar.
