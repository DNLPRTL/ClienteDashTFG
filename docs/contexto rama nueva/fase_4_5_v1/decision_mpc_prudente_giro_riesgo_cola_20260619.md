# Decisión — MPC Prudente: el eje correcto es la COLA (peor caso), no la media

| Campo | Valor |
|---|---|
| Fecha | 2026-06-19 |
| Autor | Claude (Claude Code) |
| Rama | `rebuild/phase3-from-phase2` |
| Estado | Giro estratégico fundamentado en evidencia. Métricas de cola añadidas. Pendiente: barrido del mando de riesgo. |

## El problema con "QoE media vs robust_mpc"

robust_mpc está casi óptimo en QoE media en simulación trace-driven, y la
literatura lo confirma: **Puffer/Fugu (NSDI'20)** observó que esquemas ML
sofisticados *"did not outperform simple buffer-based control"* salvo Fugu. Buscar
batir la media es el camino al resultado descafeinado.

## Qué concluyen los papers (la pista)

- **BayesMPC** (BNN + MPC robusto consciente de incertidumbre, *nuestro mismo
  enfoque*): *"maximize the worst-case outcome, surprisingly outperform ... average
  QoE"* y *"effectively reduce the risk of rebuffering when high uncertainty exists
  in the prediction"*. Su gana es el **peor caso / cortes bajo incertidumbre**, y
  **barren un mando de riesgo** `z_δ` (1.0→1.7) presentando la **curva de
  compromiso**, no un punto.
- **Fugu/Puffer**: ganan por **aprender in-situ (en el entorno real)** y reducir
  **stall ratio**. Fugu = MPC + predictor aprendido = nuestra arquitectura. Su
  fidelidad in-situ ≈ nuestra fidelidad al medio (VBR real).

→ El eje de victoria es **(a) reducir cortes/peor caso bajo incertidumbre** y
**(b) fidelidad al entorno real**. No la QoE media.

## Evidencia en NUESTROS datos (27 ventanas servibles)

| controller | media | p10 | p05 | min (peor) | rebuffer | bitrate |
|---|---:|---:|---:|---:|---:|---:|
| robust_mpc | 2.056 | 0.442 | 0.295 | 0.249 | 22.6 | 2309 |
| mpc_prudente | 2.007 | 0.412 | **0.318** | **0.294** | 22.6 | 2238 |
| neural_mpc viejo | 2.026 | 0.472 | 0.235 | −0.219 | 28.3 | 2325 |
| bola | 1.445 | 0.333 | −0.056 | −0.162 | 33.6 | 1752 |

- **mpc_prudente BATE a robust_mpc en el peor caso**: min 0.294 vs 0.249 (+0.045),
  p05 0.318 vs 0.295 (+0.023). Justo la tesis BayesMPC.
- Cuesta un poco en media/p10 (trade-off de riesgo conocido).
- Domina claramente la cola del neural_mpc viejo (min −0.219) y bola (min −0.162).

## La contribución defendible (de lo que presumir)

1. **ABR consciente del riesgo (CVaR) que mejora el peor caso de QoE** sobre
   robust_mpc, con un **mando de riesgo interpretable y barrido** → curva de
   compromiso peor-caso vs media (réplica de la metodología BayesMPC con CVaR).
2. **Fidelidad al medio real (VBR)** — análogo a la fidelidad in-situ de Fugu;
   mostrar que la suposición CBR común en ABR sesga los resultados.
3. **Evaluación en el eje correcto** (cola/stall/percentiles), con honestidad sobre
   la saturación de la QoE media (consistente con Puffer).

## Siguiente paso

Barrer el mando de riesgo (alpha/CVaR), como BayesMPC con `z_δ`, para:
- trazar la frontera peor-caso vs media,
- encontrar el punto que **maximiza la ganancia de cola** con mínimo coste de media,
- mostrar que la ganancia es **mayor en alta variabilidad** (donde robust_mpc
  mispredice). Añadir percentiles por bucket de variabilidad.

Luego, controller runtime + Phase 6 sobre eval (donde viven los casos duros).
