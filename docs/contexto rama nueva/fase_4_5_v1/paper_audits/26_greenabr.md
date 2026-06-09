# 26 - GreenABR

PDF: `3524273.3528188.pdf`

Titulo: GreenABR: Energy-Aware Adaptive Bitrate Streaming with Deep
Reinforcement Learning.

## Que hace

GreenABR incorpora consumo energetico al problema ABR, buscando reducir energia
sin degradar QoE.

## Tecnica

- DRL para bitrate.
- Reward multiobjetivo: QoE y energia.
- Considera modelos de energia/dispositivo.
- Evalua trade-off QoE/consumo.

## Evaluacion del paper

Compara contra ABR baselines y variantes con diferentes pesos de energia. Usa
trazas y escenarios sinteticos/reales.

## Relevancia para el proyecto

Secundaria:

- nuestro Phase 6 no mide energia;
- no tenemos telemetria de consumo del cliente;
- si se incluyera, cambiaria la pregunta del TFG.

## Decision

No implementar. Citar como extension futura de QoE multiobjetivo.
