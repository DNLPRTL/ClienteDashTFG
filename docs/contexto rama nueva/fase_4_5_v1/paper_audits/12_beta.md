# 12 - BETA

PDF: `BETA.pdf`

Titulo: A Novel Spatial-Temporal Learning Method for Enhancing Generalization
in Adaptive Video Streaming.

## Que hace

BETA define el problema de "ABR under-generalization": modelos DRL entrenados
en muchas trazas aun fallan en subconjuntos dificiles. Propone una parte
espacial para detectar condiciones problematicas y una temporal para entrenar
con recompensas multi-step.

## Tecnica

- Mide gap frente a optimo offline por sesion.
- Etiqueta trazas donde el modelo base falla.
- Entrena detector de condiciones dificiles.
- Entrena modelos complementarios para normal/dificil.
- Usa secuencias multi-step estado-accion-reward para decisiones mas lejanas.

## Evaluacion del paper

Evalua varios algoritmos DRL (A3C, PPO, TD3, DDPG, DQN, SAC) y muestra que solo
alcanzan una fraccion del optimo en condiciones heterogeneas. Reporta fuertes
reducciones de rebuffer y mejoras en QoE con BETA.

## Relevancia para el proyecto

Altisima:

- exactamente nuestro sintoma: promedio aceptable, fallos graves en redes bajas
  o con caidas;
- sugiere entrenar contra casos donde el modelo falla, no solo contra una media;
- justifica acceptance tests por escenario dificil.

## Decision

Usar en Plan A para construir un conjunto "danger traces" y en Plan B para
detector de condicion dificil.
