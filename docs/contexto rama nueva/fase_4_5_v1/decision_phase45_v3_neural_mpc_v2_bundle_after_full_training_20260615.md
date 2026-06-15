# Decision Phase45 v3 Neural-MPC v2 tras full training

Fecha: 2026-06-15

## Estado

Se ejecuto full training v2 sobre:

```text
dataset_dir=/home/danie/TFG/datasets_normalizados/phase45_v3/throughput_quantile_full_v1_neural_mpc_v2
model_root=/home/danie/TFG/modelos/phase45_v3/throughput_quantile_predictor/full_v1_neural_mpc_v2
run_root=/home/danie/TFG/runs_phase45_v3/neural_mpc_full_v1_v2
seeds=452001,452002,452003
```

Las salidas son diagnosticas:

```text
benchmark_performed=false
ranking_performed=false
no_final_ranking=true
qoe_claims_authorized=false
```

## Lectura de resultados

Las tres seeds tienen:

- training `PASS`;
- evaluacion closed-loop offline `PASS`;
- checkpoints presentes;
- fallback neural `0`;
- acciones invalidas `0`;
- sin accion 0 en alta capacidad.

El resumen global queda en `REVIEW` porque la seed `452001` activa el warning
`paired_rebuffer_spike_vs_robust_mpc` con un peor delta de rebuffer de
`+5.409446542610964 s` frente a Robust MPC.

Las seeds `452002` y `452003` no activan warnings. La seed `452003` presenta la
mejor media diagnostica entre las limpias:

```text
qoe_delta_vs_robust_mpc_mean=+0.009815398069525623
rebuffer_delta_vs_robust_mpc_mean=-0.15886832955482982
bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean=-0.356756950579267
worst_rebuffer_delta_s=+3.1147564535331327
min_qoe_delta=-0.4781150916730823
```

## Decision

No se declara que v2 haya ganado ni que mejore QoE formalmente.

Se aprueba exportar un bundle experimental `v2` usando como seed canonica:

```text
canonical_seed=452003
controller_key=phase45_v3_neural_throughput_calibrated_mpc_v2
```

Motivo:

- `452003` mejora las metricas medias offline frente a Robust MPC;
- no activa warnings de riesgo configurados;
- reduce rebuffer medio frente a Robust MPC en el diagnostico offline;
- mantiene fallback `0` y acciones invalidas `0`;
- permite comparar v1 y v2 en Ubuntu cliente sin sobrescribir v1.

## Siguiente validacion

La validacion correcta no es pasar directamente a `equilibrado`.

Secuencia recomendada:

```text
exportar bundle v2 en WSL
-> empaquetar y mover a Ubuntu cliente
-> validar bundle v2
-> smoke runtime controller v2
-> Phase 6 diagnostico con v1 y v2
-> si pasa, Phase 6 rapido con v1 y v2
-> solo despues decidir si equilibrado tiene sentido
```

El paquete Phase 6 recomendado debe incluir:

```text
Rate Based
BOLA
Robust MPC
Propio Neural-MPC v1
Propio Neural-MPC v2
```

Asi la comparacion v1 vs v2 se hace en las mismas ventanas y con el mismo
protocolo, sin reutilizar el paquete anterior como unico punto de comparacion.
