# 13 - EAStream

PDF: `EAStream.pdf`

Titulo: EAStream: An Environment-Aware Adaptive Bitrate Algorithm for Reliable
Video Streaming Services.

## Que hace

EAStream modela la incertidumbre del entorno como una variable latente
probabilistica. La politica ABR recibe el estado actual y una creencia del
entorno inferida desde la historia, sin requerir fine-tuning online.

## Tecnica

- Formula ABR como BAMDP.
- Usa encoder tipo GRU/VAE sobre trayectoria historica.
- Reconstruye transiciones y rewards para aprender belief.
- Politica DRL condicionada por estado fisico y belief.
- Adaptacion por contexto, no por actualizacion de pesos en runtime.

## Evaluacion del paper

Evalua con trazas reales diversas y escenarios OOD. Reporta mejor generalizacion
que baselines learning-based y meta-RL que requieren fine-tuning online.

## Relevancia para el proyecto

Muy buena idea de segunda generacion:

- inference-only encaja mejor con Phase 6 que MAML online;
- modela incertidumbre, clave para no subir demasiado en redes variables;
- puede extender Plan B con un embedding de entorno.

Limitacion:

- VAE/latent context aumenta complejidad y requiere mucha validacion;
- puede ser opaco si no se acompana de telemetria clara.

## Decision

No empezar por EAStream completo. Usar una version simplificada: features de
incertidumbre y contexto de red, con telemetria explicable.
