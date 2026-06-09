# 14 - Fortuna

PDF: `Fortuna.pdf`

Titulo: Optimizing Adaptive Video Streaming: Offline Reinforcement Learning and
Meta-Learning in Diverse Networks.

## Que hace

Fortuna propone un ABR de offline RL + meta-learning para aprender desde datos
existentes y adaptarse a redes diversas sin depender de exploracion online
costosa.

## Tecnica

- Offline RL con advantage-weighted regression.
- Usa demostraciones/datos previos, incluido MPC como fuente experta.
- Curriculum learning con longitudes crecientes de streaming.
- Meta-learning para inicializacion/politica adaptable.
- Busca robustez ante datos de internet pesados, diversos y con colas.

## Evaluacion del paper

Evalua en trazas y escenarios reales, compara contra RL y baselines SOTA, e
incluye despliegue o evaluacion real-world segun el paper.

## Relevancia para el proyecto

Muy transferible:

- nosotros tenemos datos offline y replay;
- no queremos exploracion online en runtime;
- advantage-weighted updates pueden superar BC puro sin perder estabilidad.

Limitacion:

- offline RL mal controlado puede aprender acciones fuera de distribucion;
- exige gates de accion valida y conservative/risk training.

## Decision

Usar como inspiracion para fine-tuning offline de Plan A despues de BC. Mantener
guardrails y action mask para evitar extrapolacion peligrosa.
