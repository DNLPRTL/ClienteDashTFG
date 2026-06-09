# 08 - MERINA

PDF: `MERINA.pdf`

Titulo: Improving Generalization for Neural Adaptive Video Streaming via Meta
Reinforcement Learning.

## Que hace

MERINA busca mejorar la generalizacion de ABR neuronal separando la inferencia
de dinamicas de throughput del mecanismo universal de control. Usa meta-RL para
adaptar politica a cambios de red.

## Tecnica

- Modela incertidumbre de inferencia.
- Busca una meta-politica que funcione sobre dinamicas mezcladas.
- Entrena con replay buffer y busqueda de politica sobre tareas.
- Se centra en adaptacion rapida a entornos nuevos.

## Evaluacion del paper

Compara contra baselines clasicos y neurales en datasets de trazas. Mide QoE y
adaptacion a nuevas condiciones.

## Relevancia para el proyecto

Transferible como argumento de que un modelo unico puede comprometerse
demasiado entre redes. Encaja con Plan B: condicionamiento por entorno o experts.

Limitacion:

- meta-RL completo puede ser pesado de implementar y explicar;
- online adaptation debe controlarse para no romper reproducibilidad.

## Decision

Usar como soporte de diseno para separar "detectar dinamica" y "decidir
bitrate". No implementar MERINA literal en v1.
