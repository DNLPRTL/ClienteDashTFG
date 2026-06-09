# 11 - ANT

PDF: `ANT.pdf`

Titulo: Learning Accurate Network Dynamics for Enhanced Adaptive Video
Streaming.

## Que hace

ANT detecta dinamicas de red con mas detalle que media/desviacion y activa un
modelo ABR especializado para la condicion detectada.

## Tecnica

- Segmenta trazas en Network Trace Segments.
- Usa clustering para condiciones de red.
- Entrena un detector 1D-CNN sobre medidas temporales de throughput.
- Entrena multiples modelos RL, uno por condicion.
- Runtime: detecta condicion y selecciona el modelo correspondiente.

## Evaluacion del paper

Compara en VoD y live streaming contra Pensieve, Oboe y otros en datasets
publicos y un dataset propietario. Mide QoE y robustez ante cambios de condicion.

## Relevancia para el proyecto

Muy transferible para Plan B:

- nuestras ventanas de Phase 6 ya pueden agruparse por regimen de throughput;
- el error actual de modelos propios parece regimen-dependiente;
- selector de expert es facil de auditar.

Limitacion:

- multiples modelos aumentan complejidad de bundles;
- el detector debe usar solo historial pasado en runtime.

## Decision

Usar como base conceptual para `neural_abr_env_expert_v1`. Para Plan A, tomar
solo la idea de features de dinamica como entrada/riesgo.
