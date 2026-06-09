# 09 - MetaABR

PDF: `MetaABR_A_Meta-Learning_Approach_on_Adaptative_Bitrate_Selection_for_Video_Streaming.pdf`

Titulo: MetaABR: A Meta-Learning Approach on Adaptative Bitrate Selection for
Video Streaming.

## Que hace

MetaABR usa meta-learning para transferir conocimiento entre tareas de streaming
y adaptar la seleccion de bitrate a diferentes condiciones y objetivos QoE.

## Tecnica

- Define tareas ABR con distintas trazas, videos o QoE.
- Entrena actores especificos y un mecanismo de transferencia/meta-critic.
- Evalua trade-offs entre metricas QoE.
- Busca mejor generalizacion multi-video y multi-entorno.

## Evaluacion del paper

Evalua en datasets de red distintos y compara contra algoritmos clasicos y
learning-based. Reporta transferencia de conocimiento entre entornos.

## Relevancia para el proyecto

Util para Plan B y para memoria:

- refuerza que no basta con un modelo entrenado sobre media global;
- ayuda a justificar conditioning por perfil de red/video.

Limitacion:

- nuestra Phase 6 actual usa MPDs concretos y no VMAF;
- no queremos online training en runtime.

## Decision

Usar como referencia secundaria de meta-learning. No priorizarlo frente a
SODA/Gelato/SABR/Fortuna para el primer controller.
