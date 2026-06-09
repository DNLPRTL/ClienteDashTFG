# 02 - Comyco

PDF: `1908.02270v1.pdf`

Titulo: Comyco: Quality-Aware Adaptive Video Streaming via Imitation Learning.

## Que hace

Comyco acelera el entrenamiento ABR aprendiendo de trayectorias expertas en vez
de explorar desde cero. El sistema usa imitation learning, quality-aware video
utility y lifelong learning con trazas nuevas.

## Tecnica

- Entrena una red para imitar decisiones de un solver/experto.
- Usa VMAF o calidad perceptual para evitar optimizar solo bitrate.
- Filtra trazas utiles para aprendizaje continuo.
- Usa replay/virtual player para producir muestras estado-accion.
- Busca reducir coste de entrenamiento frente a RL puro.

## Evaluacion del paper

Evalua con trazas reales y experimentos reales. Compara contra RobustMPC,
Pensieve y otros baselines. El punto fuerte no es solo QoE, sino eficiencia:
converge con muchas menos muestras que Pensieve.

## Relevancia para el proyecto

Muy transferible:

- ya tenemos teachers clasicos reales y replay offline;
- podemos generar labels robust_mpc, rate_based, bba, mpc o hibridos;
- es compatible con bundles CPU;
- permite pretraining estable antes de fine-tuning.

Limitacion:

- si el experto o el filtro de datos son malos, el modelo hereda agresividad;
- VMAF no esta cerrado en nuestro contrato actual.

## Decision

Usar para el pretraining de `neural_abr_risk_guard_v1`, pero cambiar el experto:
no solo robust_mpc global, sino experto hibrido/risk-aware por escenario.
