# 17 - SODA

PDF: `SODA.pdf`

Titulo: SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video
Streaming.

## Que hace

SODA disena un controller ABR centrado en calidad consistente, pocos switches y
seguridad de buffer, especialmente en live streaming con buffers cortos.

## Tecnica

- Reformula ABR desde una perspectiva time-based.
- Usa smoothed online convex optimization.
- Penaliza alejarse de un buffer target antes de llegar a buffer 0.
- Incorpora predicciones de throughput de forma robusta.
- Busca suavidad sin sacrificar calidad ni provocar rebuffer.

## Evaluacion del paper

Evalua en simulaciones, prototipo y produccion. Reporta reducciones fuertes de
switching y mejoras de QoE/duracion de visionado frente a baselines.

## Relevancia para el proyecto

Critico para Fase 4-5 v1:

- nuestro fallo es rebuffer por acciones agresivas;
- penalizar solo rebuffer observado llega tarde;
- necesitamos una funcion de riesgo que crezca cuando el buffer se acerca a una
  zona peligrosa.

## Decision

Usar como principio de safe layer y reward shaping. Plan A debe incluir
`low_buffer_penalty`, `buffer_target_penalty`, estimacion conservadora de descarga
y limite de saltos.
