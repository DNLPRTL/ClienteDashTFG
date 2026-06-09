# 27 - Visual sensitivity aware ABR

PDF: `3591108.pdf`

Titulo: A Visual Sensitivity Aware ABR Algorithm for DASH via Deep
Reinforcement Learning.

## Que hace

Introduce sensibilidad visual/HVS y caracteristicas de contenido para asignar
bitrate de forma mas alineada con calidad percibida.

## Tecnica

- Preprocesa video para extraer features de contenido.
- Modela efecto de enmascaramiento/sensibilidad visual.
- Politica DRL usa red, buffer y sensibilidad visual.
- Reward orientado a QoE perceptual.

## Evaluacion del paper

Evalua el modelo de sensibilidad visual y el ABR resultante frente a baselines.
Incluye overhead del sistema.

## Relevancia para el proyecto

Conceptualmente util:

- recuerda que bitrate no equivale a calidad percibida;
- podria mejorar memoria si algun dia se integra VMAF/content-aware features.

Limitacion:

- nuestro contrato Phase 3.5 dejo VMAF deferred;
- Phase 6 formal no tiene features visuales por segmento;
- extraer features de contenido aumentaria pipeline y artifacts.

## Decision

No usar en Fase 4-5 v1. Mantener como trabajo futuro content-aware/VMAF.
