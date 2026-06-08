# Contrato de Verificacion

Esta fase acepta una verificacion solo si se cumplen todas estas condiciones.

## Verificacion valida

Una verificacion valida debe demostrar:

- el cliente carga un MPD real o local valido;
- descarga inicializaciones y segmentos por la ruta normal del cliente;
- mantiene estado de buffer;
- construye feedback con senales runtime;
- llama al controller registrado por `core.controller.registry`;
- el controller devuelve un target rate en bytes por segundo;
- el player convierte ese rate a un indice de representacion valido;
- se escriben artifacts canonicos;
- los artifacts se pueden auditar despues de la ejecucion.

## Artifacts obligatorios

Cada run debe contener:

```text
run_manifest.json
config.resolved.json
environment.json
run.log
segment_telemetry.csv
evaluation_segments.csv
```

No deben aparecer:

```text
dataset.csv
dataset_training.csv
```

## Frontera metodologica

Esta fase no autoriza:

- benchmark;
- ranking;
- ganador;
- comparacion QoE;
- afirmacion de mejora;
- uso de red rapida como evidencia de rendimiento;
- uso de dry-runs como dataset de entrenamiento;
- mezcla de fake engine y GStreamer como resultados equivalentes.

## Criterio de cierre

La fase se cierra cuando los cinco controllers clasicos pasan:

- probes controlados de comportamiento teorico;
- reproduccion estructural contra el servidor DASH;
- auditoria de artifacts;
- comprobacion de no contaminacion.

