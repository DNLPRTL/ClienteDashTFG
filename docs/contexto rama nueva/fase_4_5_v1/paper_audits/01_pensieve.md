# 01 - Pensieve

PDF: `pensievee.pdf`

Titulo: Neural Adaptive Video Streaming with Pensieve.

## Que hace

Pensieve entrena una politica ABR mediante deep reinforcement learning. La red
elige el bitrate del siguiente chunk a partir de observaciones del player, sin
reglas fijas de throughput o buffer.

## Tecnica

- MDP por chunk.
- Estado: throughput reciente, download time reciente, buffer, ultimo bitrate,
  tamanos de chunks futuros y chunks restantes.
- Accion: bitrate discreto del siguiente chunk.
- Reward clasico: calidad/bitrate menos penalizacion por rebuffer y smoothness.
- Entrenamiento: A3C sobre simulador trace-driven.
- Ejecucion: inferencia de politica neural en cliente.

## Evaluacion del paper

Compara contra rate-based, buffer-based, MPC y RobustMPC en trazas y pruebas
reales. Reporta mejoras de QoE frente a baselines bajo sus condiciones, aunque
la generalizacion depende del corpus de entrenamiento y del reward.

## Relevancia para el proyecto

Es la referencia base obligatoria para justificar ABR con RL, pero no basta para
Fase 4-5 v1:

- el problema observado en nuestros modelos es precisamente el riesgo de que una
  politica neural sea agresiva si el reward/training no castiga suficiente el
  rebuffer;
- A3C no es la opcion mas estable para nuestro siguiente ciclo;
- el estado de Pensieve incluye seniales que en nuestro runtime solo pueden
  usarse si estan disponibles sin leakage.

## Decision

Usar como baseline conceptual y estructura de estado/accion/reward, no como
modelo directo. Fase 4-5 v1 debe anadir guardrails de buffer, balanceo de trazas
y entrenamiento mas estable.
