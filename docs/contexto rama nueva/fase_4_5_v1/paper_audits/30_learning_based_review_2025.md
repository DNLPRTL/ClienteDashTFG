# 30 - Review learning-based 2025

PDF: `A_Review_of_Learning-Based_Methods_for_Adaptive_Video_Streaming_Over_HTTP.pdf`

Titulo: A Review of Learning-Based Methods for Adaptive Video Streaming Over
HTTP.

## Que hace

Survey actualizado de metodos learning-based para streaming adaptativo HTTP.
Cubre adaptacion inteligente, encoding, QoE, super-resolution y otras etapas del
pipeline.

## Tecnica

No propone un controller unico. Clasifica familias:

- supervised learning;
- reinforcement learning;
- imitation learning;
- meta-learning;
- content-aware y QoE-aware;
- optimizacion multiobjetivo.

## Evaluacion del paper

Al ser survey, no ejecuta un benchmark propio comparable a Phase 6. Su valor es
taxonomico y bibliografico.

## Relevancia para el proyecto

Alta para memoria:

- permite ubicar Pensieve, Comyco, meta-RL, offline RL y predictors;
- ayuda a justificar por que Fase 4-5 v1 no es "solo otro modelo";
- sirve para estado del arte hasta 2025.

## Decision

Usar para capitulo de antecedentes y para validar que nuestros planes cubren
familias representativas: IL, RL, offline RL, predictor y meta/context-aware.
