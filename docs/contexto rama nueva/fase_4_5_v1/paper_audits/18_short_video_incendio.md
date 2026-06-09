# 18 - Incendio short-video MARL

PDF: `3592473.3592564.pdf`

Titulo: Improving ABR Performance for Short Video Streaming Using Multi-Agent
Reinforcement Learning with Expert Guidance.

## Que hace

Incendio aborda short video streaming, donde el sistema debe decidir que video
prefetchar y a que bitrate. Separa el problema en dos agentes: buffer management
y bitrate adaptation.

## Tecnica

- MARL jerarquico con dos agentes.
- BM-agent: decide dormir o que video de la cola prefetchar.
- BA-agent: decide bitrate del chunk del video elegido.
- Pretraining por imitation learning desde reglas expertas.
- Fine-tuning con multi-agent PPO.
- Reward: QoE menos penalizacion por rebuffer y ancho de banda desperdiciado,
  incluyendo user retention.

## Evaluacion del paper

Compara contra PDAS, MPC y otros metodos short-video. Reporta mejor utility,
menos desperdicio y baja latencia de inferencia.

## Relevancia para el proyecto

Interesante y actual, pero no encaja directamente con Phase 6 actual:

- Phase 6 evalua un stream DASH, no una cola de short videos;
- no tenemos decision de video-id ni user retention;
- no hay prefetch multi-video en el cliente actual.

## Decision

Dejarlo para el final como pidio Daniel. Si se implementa, debe ser una rama
experimental separada: short sessions, chunk duration corto, posible prefetch
policy y metricas de desperdicio. No bloquear Plan A.
