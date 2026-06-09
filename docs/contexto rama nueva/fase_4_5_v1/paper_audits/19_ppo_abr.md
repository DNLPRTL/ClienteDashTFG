# 19 - PPO-ABR

PDF: `PPO-ABR_Proximal_Policy_Optimization_based_Deep_Reinforcement_Learning_for_Adaptive_BitRate_streaming.pdf`

Titulo: PPO-ABR: Proximal Policy Optimization based Deep Reinforcement Learning
for Adaptive BitRate streaming.

## Que hace

Propone usar PPO para entrenar una politica ABR en lugar de metodos anteriores
como A3C.

## Tecnica

- Estado ABR con throughput/buffer/bitrate reciente.
- Accion discreta de bitrate.
- Reward QoE con calidad, rebuffer y smoothness.
- PPO como algoritmo on-policy con objetivo clipped.

## Evaluacion del paper

Evalua en datasets de red y compara con metodos DRL/ABR existentes. El aporte
principal es cambiar el optimizador RL a PPO.

## Relevancia para el proyecto

Util como soporte secundario para PPO, pero no resuelve por si solo:

- balanceo de trazas;
- incertidumbre;
- safe action;
- generalizacion por regimen.

## Decision

No implementarlo como controller independiente. PPO puede ser la tecnica de
fine-tuning del Plan A, pero con BC previo y safety.
