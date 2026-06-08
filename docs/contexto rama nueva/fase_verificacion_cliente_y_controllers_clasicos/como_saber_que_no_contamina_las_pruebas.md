# Como Saber Que No Contamina Las Pruebas

La verificacion revisa que los runs clasicos no arrastran informacion que haria
injusta una evaluacion posterior.

## Datos permitidos para controllers

Los controllers reciben feedback runtime del cliente:

- buffer actual;
- nivel actual;
- ladder del MPD;
- ultimo tamano descargado;
- ultimo tiempo de descarga;
- throughput medido a partir de descargas ya completadas;
- duracion de segmento;
- indice de segmento runtime.

## Datos que no deben aparecer como entrada

Un controller clasico no debe ver:

```text
trace_id
dataset_id
source_id
split
group_id
leakage_group
future throughput
future QoE
winner
ranking
```

## Separacion de CSV

`segment_telemetry.csv` es el artifact completo de diagnostico runtime.

`evaluation_segments.csv` debe seguir compacto. En esta fase se comprueba que no
contiene columnas internas de controllers ni columnas de IA.

## Nombres legacy

Los nombres antiguos:

```text
dataset.csv
dataset_training.csv
```

no deben aparecer en runs nuevos. Si aparecen, la verificacion falla.

## IA fuera de los runs clasicos

Los runs de esta fase son solo de controllers clasicos. Por eso se rechazan
columnas `feedback_neural_*` en esos runs.

