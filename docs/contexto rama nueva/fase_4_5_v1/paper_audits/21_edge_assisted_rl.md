# 21 - Edge-assisted RL

PDF: `1-s2.0-S1084804523000231-main.pdf`

Titulo: HTTP adaptive streaming scheme based on reinforcement learning with edge
computing assistance.

## Que hace

Propone un esquema de streaming adaptativo con asistencia edge para multiples
clientes. La politica RL busca equilibrar QoE individual y fairness.

## Tecnica

- Edge server recibe informacion QoE/cliente.
- Actor-critic para generar politica de adaptacion.
- Considera subjetive quality, VMAF, multiples videos y multiples clientes.
- Accion: bitrate/calidad para el siguiente segmento.
- Reward: QoE individual + fairness entre clientes.

## Evaluacion del paper

Usa trazas reales y videos con caracteristicas distintas. Compara contra
esquemas edge/heuristicos y mide QoE/fairness.

## Relevancia para el proyecto

Ideas utiles:

- calidad perceptual no lineal;
- fairness multi-cliente;
- edge con mas computo.

Pero no encaja ahora:

- servidor Ubuntu no decide la red ni ejecuta controller;
- Phase 6 evalua un cliente por sesion;
- VMAF esta deferred.

## Decision

No implementar en v1. Mantener como trabajo futuro y como referencia de por que
no debemos optimizar solo bitrate bruto.
