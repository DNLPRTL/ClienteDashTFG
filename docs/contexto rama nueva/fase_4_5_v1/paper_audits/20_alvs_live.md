# 20 - ALVS live DRL

PDF: `1-s2.0-S1084804522001035-main.pdf`

Titulo: ALVS: Adaptive Live Video Streaming using deep reinforcement learning.

## Que hace

ALVS optimiza live streaming tomando dos decisiones juntas: bitrate y velocidad
de reproduccion. Busca QoE alto sin sacrificar latencia live ni saltar contenido.

## Tecnica

- Actor-critic/A3C.
- Estado: bitrate actual, throughput, download time, buffer, live latency,
  tamanos proximos y segmentos restantes.
- Accion: combinacion de bitrate discreto y playback speed.
- Reward: QoE + latencia live.
- Simulador DASH/CMAF para live.

## Evaluacion del paper

Evalua con trazas 4G reales frente a soluciones DRL y heuristicas de live. Mide
QoE, latencia, freezes y estabilidad.

## Relevancia para el proyecto

No es primer objetivo:

- nuestro Phase 6 formal es VoD/fake playback, no live;
- el cliente actual no expone playback speed como accion ABR;
- anadir speed cambiaria contrato de player/runtime.

## Decision

Usar como referencia de memoria para live streaming. No implementar en Fase 4-5
v1 salvo que se abra una fase live separada.
