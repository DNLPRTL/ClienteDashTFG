# 23 - PLL-ABR / PPO LSTM local attention

PDF: `075042_1_5.0277381.pdf`

Titulo: Deep reinforcement learning enhanced optimization algorithm for adaptive
bitrate video streaming.

## Que hace

Propone un ABR DRL basado en PPO con LSTM y mecanismo de local attention para
capturar dependencias temporales en throughput, buffer y estado del player.

## Tecnica

- PPO con dual clipping.
- Red LSTM-LA para dependencia temporal y atencion local.
- Estado: buffer, throughput historico, download state y seniales del player.
- Accion: bitrate del siguiente chunk.
- Reward: QoE con calidad/bitrate, rebuffer y smoothness.

## Evaluacion del paper

Compara contra buffer-based, rate-based, RobustMPC, BOLA y otros. Reporta mejora
media de QoE, bitrate utilization, rebuffer penalty y smoothness penalty.

## Relevancia para el proyecto

Util como variante de arquitectura secuencial:

- LSTM/GRU puede captar caidas y tendencias mejor que features agregadas;
- PPO con clipping puede ser mas estable que A3C.

Limitacion:

- no resuelve por si solo riesgo de buffer;
- el paper parece mas centrado en arquitectura que en metodologia de evaluacion.

## Decision

Usar GRU/LSTM ligero si Plan A necesita memoria temporal. No priorizar local
attention salvo que el dataset lo justifique.
