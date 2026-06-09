# 15 - SABR BC + PPO

PDF: `2509.10486v1.pdf`

Titulo: SABR: A Stable Adaptive Bitrate Framework Using Behavior Cloning
Pretraining and Reinforcement Learning Fine-Tuning.

## Que hace

SABR combina pretraining por behavior cloning con fine-tuning RL. La idea es
arrancar desde una politica estable aprendida de expertos y luego mejorar con
PPO.

## Tecnica

- BC pretraining, descrito como DPO-based BC en el paper.
- RL fine-tuning con PPO.
- Benchmarks ABRBench-3G y OOD.
- Compara contra Pensieve, Comyco, NetLLM, RobustMPC, BOLA y otros.
- Evalua generalizacion por conjuntos de trazas, no solo media global.

## Evaluacion del paper

Reporta mejor ranking medio en test y OOD frente a baselines. El valor central
es la estabilidad del entrenamiento con pretraining + fine-tuning.

## Relevancia para el proyecto

Muy transferible:

- nuestros modelos anteriores ya hicieron BC, pero no fine-tuning RL real;
- PPO es mas facil de controlar que A3C;
- podemos mantener CPU/bundle final aunque el entrenamiento sea largo.

Limitacion:

- el paper es reciente y el PDF parece arXiv/preprint;
- hay que adaptar el reward a `qoe_linear_v1` y al safety goal.

## Decision

Usar como receta principal de entrenamiento para Plan A: BC primero, PPO/offline
fine-tuning despues, con reward risk-aware.
