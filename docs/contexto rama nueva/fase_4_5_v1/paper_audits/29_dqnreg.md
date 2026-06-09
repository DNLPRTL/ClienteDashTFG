# 29 - DQNReg

PDF: `v1_covered.pdf`

Titulo: Reinforcement Learning-Based Rate Adaptation in Dynamic Video Streaming.

## Que hace

Presenta una adaptacion de bitrate basada en reinforcement learning y DQNReg
para entornos dinamicos.

## Tecnica

- Estado con throughput, bitrate y buffer.
- Accion: nivel de calidad/bitrate.
- Reward QoE con calidad, starvation/rebuffer, switching y estabilidad.
- Usa DQN/regresion para aprender politica.

## Evaluacion del paper

Evalua en simulacion con entornos de red dinamicos y metricas QoE. Reporta QoE,
rebuffer/starvation, switches y convergencia.

## Relevancia para el proyecto

Secundaria:

- DQN es valido historicamente, pero menos atractivo que PPO/offline RL para
  nuestro nuevo ciclo;
- no resuelve el problema de generalizacion por si solo.

## Decision

No implementar. Mantener como referencia de DRL alternativo y reward QoE.
