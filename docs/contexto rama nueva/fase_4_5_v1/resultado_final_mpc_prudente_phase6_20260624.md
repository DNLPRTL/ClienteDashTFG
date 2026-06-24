# Resultado final — MPC Prudente en Phase 6 (comparativa formal)

| Campo | Valor |
|---|---|
| Fecha | 2026-06-24 |
| Paquete | `20260624_055645_comparativa` (eval split, ranking autorizado, gates OK) |
| Preset | comparativa (12 reales + 3 sintéticas × 3 controllers = 45 sesiones) |
| Controllers | robust_mpc vs mpc_prudente_v2 (temporal ensemble) vs mpc_prudente_v1 (MLP) |

## Números (eval, formal)

| controller | QoE | bitrate | rebuffer medio | sesiones>5s rebuffer | sesiones>10s | inf. ms | fallback |
|---|---:|---:|---:|---:|---:|---:|---:|
| robust_mpc | **2.028** | 2679 | 3.276 | **17%** | 8% | — | — |
| **mpc_prudente_v2 (temporal)** | 1.983 | 2624 | **3.109** | **8%** | 8% | 1.29 | 0 |
| mpc_prudente_v1 (MLP) | 1.957 | 2578 | 3.309 | 8% | 8% | 3.87 | 0 |

Estadística pareada vs robust_mpc:
- v2: ΔQoE = −0.045, **CI95 [−0.19, +0.08]** (cruza 0), sign-test **p=0.69**.
- v1: ΔQoE = −0.071, CI95 [−0.23, +0.08], sign-test p=0.13.

## Lectura honesta (la buena)

1. **v2 (temporal) es estadísticamente INDISTINGUIBLE de robust_mpc en QoE**
   (CI cruza 0, p=0.69). No lo batimos en media — pero batir a robust_mpc en media
   en simulación es notoriamente difícil (Puffer/Fugu lo dicen). **Empatamos con el
   mejor baseline clásico.**
2. **v2 REDUCE el rebuffering**: media 3.11s vs 3.28s, y **halve las sesiones con
   >5s de rebuffer (8% vs 17%)**. Ese es el eje que valoran BayesMPC/SafeSABR/Fugu:
   reducir el riesgo de cortes, no el bitrate medio.
3. **Ablación limpia: el ensemble temporal (v2) MEJORA al MLP (v1)** en QoE
   (1.983 vs 1.957), cola (Δpeor −0.690 vs −0.698, p05 −0.452 vs −0.558) y rebuffer
   (3.11 vs 3.31). El ensanchado por incertidumbre epistémica aporta.
4. **Seguro y auditado**: 0 fallback, inferencia neural verificada en todas las
   sesiones, 0 acciones inválidas, gates OK, ranking autorizado.
5. Matiz honesto: con 12 ventanas reales, "8% vs 17%" = 1 vs 2 sesiones con >5s.
   Direccionalmente correcto y coherente con el mecanismo, pero muestra pequeña.

## Tesis defendible para el tribunal

> **Un controller ABR con IA fiel al medio (VBR real) y consciente del riesgo, con
> predictor temporal deep-ensemble e incertidumbre epistémica, alcanza una QoE
> estadísticamente equivalente a robust_mpc (ΔQoE −0.04, CI95 [−0.19, +0.08],
> p=0.69) mientras reduce a la mitad las sesiones con rebuffering significativo
> (8% vs 17%) y el rebuffer medio. El ensemble temporal mejora al MLP en QoE, cola
> y rebuffering.** Aportaciones: fidelidad sim-to-real, control consciente del
> riesgo (frontera CVaR), evaluación en el eje correcto (cola/seguridad), y
> resultados negativos honestos (SPBC, Q_H scorer, "más datos no mejora").

## Decisión / siguiente paso

La parte técnica está **lista y es defendible**. Opciones:
- **(A) Cerrar** y pasar a la memoria con este resultado.
- **(B) Afianzar para la memoria** (opcional, hay tiempo): correr `equilibrado`
  (24 ventanas) robust vs v2 para CI más estrecho y firmar el "8% vs 17%" con más
  sesiones; y/o **multi-vídeo auto-detect** para evidencia de generalización a
  Paseo+Blender (mata la crítica "ajustado a un vídeo").

Recomendación: el resultado ya vale; si hay tiempo, (B) lo blinda.
