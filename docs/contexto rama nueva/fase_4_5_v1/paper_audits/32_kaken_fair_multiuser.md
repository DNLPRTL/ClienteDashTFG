# 32 - KAKEN fair multi-user report

PDF: `kaken.nii.ac.jp_20K14740seika.pdf`

Titulo identificado: Adaptive bitrate control strategy for ensuring high-QoE
and fair video streaming in multi-user networks.

## Que hace

Es un informe de resultados de investigacion, no un paper ABR convencional. El
tema es control ABR para QoE alto y fairness en redes multi-usuario.

## Tecnica

El PDF esta mayoritariamente en japones y resume una linea de investigacion
sobre fairness/QoE multiusuario. No aporta una especificacion implementable
directa comparable a Pensieve, Comyco, SODA o BETA.

## Evaluacion del paper

No se ha identificado una evaluacion reproducible completa util para nuestro
pipeline Phase 6. Sirve como referencia de area.

## Relevancia para el proyecto

Baja para Fase 4-5 v1:

- Phase 6 evalua sesiones independientes;
- no hay fairness multi-cliente en el contrato actual;
- servidor Ubuntu no coordina clientes.

## Decision

No implementar. Mantener como referencia de fairness multiusuario para trabajo
futuro.
