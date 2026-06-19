# Catálogo de métricas de evaluación ABR (de los papers) → Phase 6

| Campo | Valor |
|---|---|
| Fecha | 2026-06-19 |
| Autor | Claude (Claude Code) |
| Objetivo | Verificar qué midió cada paper de ABR/IA, fijar las métricas que de verdad importan y mapearlas a Phase 6 sin duplicar. |
| Fuente | Lectura dirigida de los papers de `docs/todos los estudios pdf convertidos a md/` (énfasis en los marcados por Daniel) + source cards + conocimiento de dominio. |

## 1. Ejes canónicos de evaluación ABR (lo que mide todo el campo)

1. **Calidad de vídeo**: bitrate medio y/o calidad perceptual (SSIM, VMAF).
2. **Rebuffering**: tiempo total, ratio (%), frecuencia (nº stalls), **fracción de
   sesiones con stall**, **peor caso (P95)**.
3. **Suavidad / cambios de calidad**: frecuencia de switches + magnitud.
4. **Startup delay**.
5. **QoE compuesta** (lineal/log): media + **distribución (CDF)** + **cola (peor
   caso, percentiles bajos)** + **varianza/estabilidad**.
6. **Por régimen de red** (buckets de capacidad/variabilidad) + **estadística
   emparejada** vs baseline (CI95, sign-test).
7. **Perceptual** (SSIM/VMAF/P.1203).
8. **Despliegue real / fidelidad sim-to-real** (in-situ).

## 2. Qué midió cada paper clave (verificación)

| Paper | Métrica(s) de evaluación | En qué aporta / dónde gana |
|---|---|---|
| **Yin et al. MPC, SIGCOMM'15** | QoE = Σ calidad − λ·\|variación\| − μ·rebuffer − startup; componentes separados; por régimen | define la QoE compuesta y el tradeoff calidad/rebuffer/suavidad |
| **BOLA, INFOCOM'16 / ToN'20** | utilidad(bitrate) − rebuffer; bitrate medio + rebuffer ratio | óptimo utilidad-buffer; tradeoff |
| **Spiteri DASH, MMSys'18** | rebuffer + bitrate + switches; multi-red | robustez práctica en el reproductor real |
| **Pensieve, SIGCOMM'17** | QoE lineal y log (Yin); **CDF de QoE**; componentes; redes no vistas | generalización; reporta distribución, no solo media |
| **Comyco** | QoE perceptual (VMAF): calidad+rebuffer+suavidad; eficiencia de muestras | calidad perceptual + aprender con pocas muestras |
| **Puffer / Fugu, NSDI'20** | **% tiempo en stall**, SSIM medio, **variación de SSIM**, duración de sesión; CDF; cola pesada | gana por **in-situ (entorno real)** y **reducir stalls**; admite que ML sofisticado raramente bate baselines en media |
| **BayesMPC** | **peor-caso de QoE (worst-case)**, riesgo de rebuffer bajo incertidumbre, varianza de calidad; **barrido del mando z_δ** | gana en el **peor caso** maximizando worst-case QoE; mando de riesgo + frontera |
| **Oboe** | QoE/rebuffer por condición de red (auto-tuning) | adaptación por régimen |
| **MERINA / A2BR / Fortuna / EAStream** | generalización entre redes, **varianza/robustez de QoE**, cola | consistencia y generalización (meta-RL) |
| **SODA** | consistencia/suavidad, menos switches | estabilidad de calidad |
| **Surveys (Bentaleb'19, learning-review'25, Peroni'24 pitfalls)** | dimensiones QoE; Peroni: **reportar distribuciones y por régimen, no solo medias** | guía metodológica |

**Conclusión clave (la vara correcta):** salvo casos perceptuales, la victoria
de los métodos avanzados sobre robust_mpc NO está en la **QoE media** (saturada),
sino en **(a) cola / peor caso bajo incertidumbre** (BayesMPC) y **(b) reducir
stalls + fidelidad al entorno real** (Fugu). Por eso la cola es nuestra métrica de
contribución, y la fidelidad VBR nuestra aportación metodológica.

## 3. Lo que YA tenía Phase 6 (no se duplica)

QoE lineal+log media, **CI95 bootstrap**, **sign-test**, **deltas emparejados** vs
robust_mpc; bitrate/calidad medio, rebuffer total+ratio, stall_event_count,
suavidad (pos/neg, magnitud, switching_rate), buffer, latencia de decisión,
auditoría neural; **CDFs** (qoe, rebuffer, smoothness, bitrate, buffer),
componentes, **QoE por dificultad y por condición de red**, caso temporal.
SSIM/VMAF/P.1203 quedan **diferidos** (sin artifacts perceptuales).

## 4. Lo que se AÑADIÓ ahora (el eje que faltaba: cola / estabilidad)

En `core/phase6/analysis.py` (nativo, con gráfica y markdown):

- **Por controller** (`aggregate_summaries`): `qoe_linear_min`, `qoe_linear_p05`,
  `qoe_linear_p10`, `qoe_linear_p25`, `qoe_linear_median`, `qoe_linear_std`
  (estabilidad), `rebuffer_ratio_p95` (peor rebuffering), `stall_session_rate`
  (fracción de sesiones con stall).
- **Delta vs baseline** (`paired_statistics`): `delta_qoe_linear_p05`,
  `delta_qoe_linear_p25`, `delta_qoe_linear_worst` (peor caso relativo a robust_mpc).
- **Gráfica**: `qoe_robustez_peor_caso` (media / mediana / P5 por controller).
- **Markdown**: secciones "Robustez y peor caso (cola de QoE)" y "Peor caso vs
  baseline".

## 5. Métricas para defender NUESTRO controller

- **Primaria contractual** (no se cambia): `qoe_linear_mean` con CI95 + sign-test.
- **Eje de contribución**: **cola / peor caso** (BayesMPC) — `qoe_linear_p05/min`,
  `delta_qoe_linear_worst` vs robust_mpc; **estabilidad** (`qoe_linear_std`);
  **reducción de stalls** (`stall_session_rate`, `rebuffer_ratio_p95`),
  especialmente en alta variabilidad.
- **Metodológico**: fidelidad al medio VBR (análogo in-situ de Fugu) + crítica al
  sesgo CBR común en la literatura.
- Perceptual (SSIM/VMAF): honestamente diferido como trabajo futuro.
