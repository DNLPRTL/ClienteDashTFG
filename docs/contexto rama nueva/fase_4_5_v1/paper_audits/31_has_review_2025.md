# 31 - HAS review 2025

PDF: `3736306.pdf`

Titulo: HTTP Adaptive Streaming: A Review on Current Advances and Future
Challenges.

## Que hace

Survey amplio de HTTP Adaptive Streaming: codificacion, entrega, consumo, ABR,
QoE, energia, low latency, codecs y retos futuros.

## Tecnica

No propone un controller concreto. Situa ABR dentro del pipeline HAS completo y
discute avances recientes.

## Evaluacion del paper

No hay benchmark propio de controller. Es una fuente de contexto y taxonomia.

## Relevancia para el proyecto

Alta para memoria y para mantener limites:

- nuestro TFG se centra en cliente ABR y evaluacion trace-driven;
- energia, codecs, per-title encoding y live son extensiones, no requisitos de
  Fase 4-5 v1;
- ayuda a explicar por que Phase 6 no mezcla servidor DASH con red experimental.

## Decision

Usar en antecedentes y trabajo futuro. No usar como spec de controller.
