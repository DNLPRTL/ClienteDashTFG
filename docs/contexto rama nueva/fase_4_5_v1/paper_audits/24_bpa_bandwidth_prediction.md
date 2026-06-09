# 24 - BPA bandwidth prediction + DRL

PDF: `Enhancing_Adaptive_Video_Streaming_through_Bandwidth_Prediction_with_Deep_Reinforcement_Learning.pdf`

Titulo: Enhancing Adaptive Video Streaming through Bandwidth Prediction with
Deep Reinforcement Learning.

## Que hace

Combina un modelo de prediccion de ancho de banda con un modelo actor-critic de
seleccion de bitrate. La prediccion se integra en la recompensa y en la decision.

## Tecnica

- BPM: BiLSTM para prediccion de throughput/bandwidth.
- BSM: actor-critic para bitrate.
- Reward incluye QoE y precision de prediccion.
- Entrenamiento conjunto/end-to-end.
- Busca suavidad y mejor QoE bajo redes variables.

## Evaluacion del paper

Compara BiLSTM frente a LSTM y BPA frente a baselines ABR/DRL. Reporta mejoras
en QoE y smoothness.

## Relevancia para el proyecto

Muy util para Plan C:

- podemos entrenar predictor supervisado sobre trazas normalizadas;
- la decision debe usar prediccion conservadora, no solo media;
- throughput future real no entra al controller, solo inferencia desde pasado.

Limitacion:

- optimizar precision de prediccion no garantiza menos rebuffer;
- usar BiLSTM en runtime puede ser conceptualmente problematico si implica mirar
  futuro dentro de la secuencia; debe implementarse causal, no bidireccional
  sobre futuro no disponible.

## Decision

Usar como inspiracion para predictor causal GRU/TCN cuantile. Evitar BiLSTM
runtime si no se puede garantizar causalidad.
