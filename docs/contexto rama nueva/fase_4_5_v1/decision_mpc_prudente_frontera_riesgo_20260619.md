# Decisión — MPC Prudente: frontera del mando de riesgo (afinado) + conclusión honesta

| Campo | Valor |
|---|---|
| Fecha | 2026-06-19 |
| Autor | Claude (Claude Code) |
| Rama | `rebuild/phase3-from-phase2` |
| Estado | Afinado hecho (barrido del riesgo). Conclusión honesta + operating point. |

## Qué se hizo

1. Se probó un planner adaptativo tipo límite-inferior-de-confianza (LCB). **Salió
   PEOR** (mean 1.953, perdió el peor-caso) porque el predictor tiene q50
   conservador y q10 muy bajo. **Revertido al CVaR.**
2. Se barrió el mando de riesgo CVaR (alpha) como BayesMPC con `z_δ`, sobre 27
   ventanas servibles, prudente vs robust_mpc.

## Frontera (peor-caso ↔ media)

| alpha | media | p10 | p05 | min | rebuffer | delta media vs robust |
|---|---:|---:|---:|---:|---:|---:|
| adaptativo | 2.007 | 0.412 | 0.318 | 0.294 | 22.6 | −0.049 |
| 0.25 | 1.998 | 0.412 | 0.324 | 0.318 | 22.6 | −0.058 |
| 0.50 | 2.006 | 0.412 | 0.324 | 0.318 | 22.6 | −0.049 |
| 0.75 | 2.013 | 0.412 | 0.324 | **0.318** | 22.6 | −0.043 |
| 1.00 | 2.024 | 0.412 | 0.318 | 0.309 | 22.7 | −0.032 |
| **robust_mpc** | **2.056** | **0.442** | 0.295 | 0.249 | 22.6 | 0.000 |

## Lectura honesta (sin vender humo)

- **La frontera es PLANA**: afinar alpha mueve la media ~1% (1.998→2.024). El
  afinado **no amplifica mucho**. Es lo que hay.
- **Win robusto pero modesto vs robust_mpc**: en TODO el rango de alpha, el
  prudente bate a robust en el **peor caso** (min 0.29–0.32 vs 0.249; p05
  0.32 vs 0.295). Es estructural, no un punto de suerte.
- **robust_mpc sigue ganando la media** (2.056) y p10 (0.442). No lo batimos ahí.
- **El win GRANDE es vs el AI viejo**: prudente min 0.318 vs neural_mpc viejo
  **−0.219** vs bola **−0.162**. Pasamos de un AI con sesiones catastróficas a uno
  seguro que iguala/mejora la cola de robust_mpc.
- **Operating point Pareto-óptimo: alpha = 0.75** (mejor peor-caso, min 0.318, con
  el menor coste de media entre los puntos de cola fuerte). Se fijará en el bundle
  del controller runtime.

## Por qué no más, y cómo se conseguiría más

El cuello de botella para batir a robust_mpc en MEDIA no es el planner (ya
saturado), es el **predictor**: sus cuantiles no son mucho más precisos que la
media armónica que usa robust_mpc. Para ganar también en media haría falta un
**predictor más preciso** (modelo temporal/atención, más features, estilo
CS2P/Fugu/MamBRA) — más esfuerzo y otra iteración. Es opcional según tiempo.

## Tesis defendible (honesta, alineada con BayesMPC/Fugu/SafeSABR)

> El controller neural híbrido con predicción cuantílica y planificación MPC
> **fiel al medio (VBR real)** y **consciente del riesgo (CVaR)** elimina el
> rebuffer catastrófico que hundía a las versiones previas y mejora el **peor caso
> de QoE** sobre robust_mpc, manteniendo QoE media competitiva (~3% por debajo),
> con un mando de riesgo interpretable y su frontera.

## Siguiente paso

Integrar el controller runtime (bundle con alpha=0.75 + fallback + safety + hash),
moverlo a Ubuntu cliente, y **validar en Phase 6 sobre eval** (el juez real, con
las métricas de cola ya añadidas). Opcional posterior: predictor mejorado para
intentar ganar también la media.
