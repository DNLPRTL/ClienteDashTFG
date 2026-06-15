# Decision Phase45 v3 Neural-MPC Experimental Candidate - 2026-06-15

## Proposito

Preparar `phase45_v3_neural_throughput_calibrated_mpc_v1` como candidato IA
experimental reproducible, sin convertirlo todavia en controller integrado de
runtime ni en resultado de benchmark.

Esta decision nace despues de:

- piloto diagnostico de 8 ventanas con PASS;
- diagnostico ampliado de 3 seeds x 32 ventanas con PASS tras postproceso
  monotono de cuantiles;
- mantenimiento de flags de no benchmark, no ranking y no claims.

## Estado de entrada

Ruta de ejecucion diagnostica ampliada:

```text
/home/danie/TFG/runs_phase45_v3/neural_mpc_expanded_diag_v1
```

Ruta de checkpoints:

```text
/home/danie/TFG/modelos/phase45_v3/throughput_quantile_predictor/expanded_diag_v1
```

Resultado resumido:

```text
all_reports_passed=true
report_count=3
status_counts={"PASS": 3}
failed_gate_counts={}
fallback_rate_max=0.0
invalid_action_count_max=0.0
high_capacity_action0_rate_max=0.0
high_capacity_mean_bitrate_ratio_min=1.0
```

## Decision

Se autoriza preparar un candidato IA experimental:

```text
candidate_model_experimental_v1
```

Esto significa:

- consolidar rutas, hashes y reportes necesarios para reproducibilidad;
- definir una seed canonica inicial;
- conservar las tres seeds como evidencia diagnostica;
- preparar un siguiente contrato de integracion;
- no integrar todavia en el registry principal;
- no ejecutar Phase 6 formal todavia.

No significa:

- benchmark;
- ranking;
- ganador;
- mejora QoE;
- modelo final;
- integracion runtime autorizada.

## Seed canonica inicial

Seed canonica:

```text
451001
```

Motivo:

- es la seed base ya usada por la linea `pilot_v1_seed451001`;
- se elige por politica previa y estabilidad operativa;
- no se elige por ser la seed "ganadora";
- no se descartan las otras seeds.

Checkpoint canonico inicial:

```text
/home/danie/TFG/modelos/phase45_v3/throughput_quantile_predictor/expanded_diag_v1/seed_451001/modelo_phase45_v3_throughput_quantile.pt
```

Hash observado:

```text
8a07e0d88355f51893bcc8812d647e435d9aaad51e0cc50cee52ff23fa5d8599
```

## Script de readiness

Script:

```bash
bash scripts/print_phase45_v3_neural_mpc_experimental_candidate_readiness_wsl.sh
```

Este script no copia modelos ni crea bundles. Solo lee los reportes externos y
emite un JSON pegable con:

- estado de readiness;
- seed canonica;
- hashes de modelo;
- rutas de checkpoints;
- estado de gates;
- flags de no benchmark/no ranking.

Ese JSON debe pegarse en el chat antes de preparar cualquier bundle o
integracion.

## Siguiente paso si readiness pasa

1. Definir formato de bundle experimental externo.
2. Crear script de exportacion fuera de Git.
3. Validar carga del checkpoint/bundle en Windows.
4. Validar carga del checkpoint/bundle en Ubuntu cliente.
5. Solo despues abrir contrato de integracion del controller en registry.

## Siguiente paso si readiness falla

1. No avanzar a bundle.
2. Revisar reportes externos por seed.
3. Confirmar que el run ampliado se ejecuto despues del commit con
   postproceso monotono.
4. Repetir diagnostico ampliado si hay mezcla de artefactos antiguos.

## Restricciones

Permanece prohibido:

- declarar mejora QoE;
- declarar ganador;
- llamar benchmark al diagnostico;
- commitear modelos, datasets, runs o reportes externos;
- integrar runtime sin contrato explicito posterior.
