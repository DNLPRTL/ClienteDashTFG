# 22 - DRL con quality distance factor

PDF: `applsci-13-11697.pdf`

Titulo: Deep Reinforcement Learning-Based Approach for Video Streaming:
Dynamic Adaptive Video Streaming over HTTP.

## Que hace

Propone un ABR DRL que introduce un factor de distancia de calidad entre
segmentos consecutivos para suavizar cambios percibidos.

## Tecnica

- MDP por segmento.
- Estado: throughput/bandwidth, buffer y calidad anterior.
- Accion: bitrate/calidad del siguiente segmento.
- Reward/QoE: calidad menos rebuffer y penalizacion por distancia de calidad.
- Entrenamiento DRL con proceso en dos pasos segun el paper.

## Evaluacion del paper

Evalua en simulacion con redes wireless y varias secuencias de video. Compara
contra metodos del estado del arte y reporta mejor QoE/suavidad.

## Relevancia para el proyecto

Transferible parcialmente:

- nuestro `smoothness_mbps` ya penaliza saltos;
- podemos anadir una penalizacion mas fuerte a saltos grandes cuando el buffer
  o throughput sea incierto.

Limitacion:

- no aborda de forma profunda generalizacion ni safety;
- no aporta tanto como SODA/BETA/Gelato.

## Decision

Usar como soporte para `large_jump_penalty`, no como arquitectura principal.
