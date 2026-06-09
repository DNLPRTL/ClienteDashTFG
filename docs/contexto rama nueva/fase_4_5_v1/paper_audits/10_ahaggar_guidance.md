# 10 - Ahaggar bitrate guidance

PDF: `Bitrate_Adaptation_and_Guidance_With_Meta_Reinforcement_Learning.pdf`

Titulo: Bitrate Adaptation and Guidance With Meta Reinforcement Learning.

## Que hace

Ahaggar desplaza parte de la inteligencia al servidor/edge: un modelo meta-RL da
guia de bitrate a clientes que siguen ejecutando heuristicas. Considera multiples
clientes, resoluciones y condiciones de red.

## Tecnica

- MARL/POMDP con clientes como agentes.
- Centralized training, decentralized execution.
- Meta-RL con MAML y actualizaciones tipo A2C/DPPO.
- Usa CMCD/CMSD para intercambiar estado cliente-servidor.
- Entrada: red, cliente, resolucion/dispositivo y contenido.
- Accion: guia de bitrate por cliente.

## Evaluacion del paper

Evalua trazas reales, multiples clientes, resoluciones y escenarios
heterogeneos. Reporta mejoras en QoE, rebuffer y consumo de ancho de banda.

## Relevancia para el proyecto

Interesante para memoria y futuro multi-cliente, pero no encaja como primer v1:

- nuestro servidor Ubuntu solo sirve contenido DASH;
- Phase 6 formal evalua controller cliente bajo replay, no edge guidance;
- CMCD/CMSD no forma parte del contrato actual.

## Decision

No implementar en Fase 4-5 v1. Extraer dos ideas: fairness multi-cliente como
trabajo futuro y "guia segura" como analogia para un guardrail runtime local.
