# 16 - Gelato / Plume

PDF: `Gelato.pdf`

Titulo: Practically High Performant Neural Adaptive Video Streaming.

## Que hace

Gelato muestra que buena parte del problema de DRL ABR viene de la distribucion
sesgada de trazas. Plume identifica features criticas, clusteriza trazas y
prioriza clusters raros o importantes durante entrenamiento.

## Tecnica

- Analiza skew de input traces, no solo skew de estados en replay buffer.
- Critical feature identification para caracterizar trazas.
- Clustering de trazas.
- Prioritized trace sampling en el paso de acting.
- Controller Gelato entrenado con ese muestreo.

## Evaluacion del paper

Evalua en Puffer durante mas de un ano y tambien en entornos controlados. El
mensaje fuerte: balancear trazas tail-end mejora stalls y rendimiento global sin
depender solo de PER.

## Relevancia para el proyecto

Probablemente el paper mas importante para nuestro fallo actual:

- redes bajas y con caidas son minoritarias pero decisivas;
- el preset rapido ya separa buckets de throughput;
- Phase 3 manifest permite sampler por grupos sin leakage.

## Decision

Aplicar Plume-lite en Fase 4-5 v1: clustering/buckets por throughput medio,
minimo, varianza, caidas a cero, low-percentile y burstiness. Oversamplear
escenarios donde los controllers propios actuales rebufferizan.
