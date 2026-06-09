# 05 - CausalSim

PDF: `CausalSim.pdf`

Titulo: CausalSim: A Causal Framework for Unbiased Trace-Driven Simulation.

## Que hace

CausalSim advierte que la simulacion trace-driven puede estar sesgada: las
trazas observadas dependen de las decisiones del algoritmo que las genero. Si se
replaya una traza como si fuera independiente, la evaluacion de una intervencion
nueva puede ser parcial o erronea.

## Tecnica

- Modela causalmente el sistema observado.
- Distingue entre variables exogenas e intervenidas.
- Corrige o estima efectos de intervenciones sobre componentes simulados.
- Evalua exactitud de simulacion frente a datos reales.

## Evaluacion del paper

Usa Puffer como caso principal y muestra que simuladores trace-driven ingenuos
pueden estimar mal el resultado de nuevos algoritmos.

## Relevancia para el proyecto

Muy relevante para honestidad cientifica:

- nuestras trazas tienen semanticas distintas: FCC, Puffer, GAViST, sinteticas;
- no debemos convertir resultados de replay en claims real-world universales;
- las conclusiones deben separarse por tipo de traza.

## Decision

Usar como guardrail metodologico. No implementar CausalSim completo en Fase 4-5
v1, pero documentar sesgos y mantener la separacion real/sintetica/semantica en
training y Phase 6.
