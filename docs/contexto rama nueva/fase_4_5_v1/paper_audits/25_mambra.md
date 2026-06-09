# 25 - MamBRA

PDF: `v1_covered_4254418a-5dc6-4da1-be54-5ccdcf966b39.pdf`

Titulo: MamBRA: Session-Level Bandwidth Prediction for Adaptive Video Streaming
using Selective State Space Models.

## Que hace

MamBRA usa Mamba/SSM para prediccion de bandwidth a nivel de sesion, con
separacion estricta por sesiones para evitar leakage temporal.

## Tecnica

- Supervised time-series learning.
- Datos reorganizados por sesiones disjuntas.
- Modelo selectivo state-space tipo Mamba.
- Inferencia eficiente con complejidad lineal.
- Evalua error de prediccion, estabilidad temporal y QoE derivada.

## Evaluacion del paper

Reporta alta accuracy de prediccion y QoE mas consistente frente a un enfoque
PPO usado como comparacion.

## Relevancia para el proyecto

Interesante para Plan C, sobre todo por:

- split por sesion/grupo sin leakage;
- estabilidad temporal de predicciones;
- eficiencia de inferencia.

Riesgos:

- preprint 2026, no necesariamente revisado;
- librerias Mamba/SSM pueden ser fragiles en Windows/Python 3.12/AMD;
- predictor no equivale a controller ABR completo.

## Decision

No empezar con Mamba. Disenar primero predictor causal simple y auditable. Mamba
queda como variante avanzada si el entorno lo permite.
