# 04 - Oboe

PDF: `Oboe.pdf`

Titulo: Oboe: Auto-tuning Video ABR Algorithms to Network Conditions.

## Que hace

Oboe no crea una politica ABR desde cero. Auto-ajusta parametros de algoritmos
existentes, como BOLA o MPC, segun la condicion de red detectada.

## Tecnica

- Representa el estado de red con estadisticos de throughput.
- Precalcula offline los mejores parametros por condicion.
- En runtime detecta condicion y cambia parametros del ABR.
- Mantiene el controller interpretable porque parte de algoritmos conocidos.

## Evaluacion del paper

Compara versiones auto-tuneadas contra algoritmos base en redes distintas.
Muestra que un mismo set de parametros no es universal.

## Relevancia para el proyecto

Transferible como capa de entorno:

- podemos detectar regimen de red sin exponer metadata prohibida;
- sirve para explicar por que rate_based, BBA o robust_mpc son mejores en
  escenarios distintos;
- puede integrarse como selector/condicionador de experts.

Limitacion:

- usa estadisticos simples; papers posteriores como ANT/BETA muestran que
  promedio/desviacion no siempre diferencian dinamicas temporales.

## Decision

Usar en Plan B como idea de selector interpretable, pero mejorar la deteccion
con features de variabilidad, caidas y low-buffer risk.
