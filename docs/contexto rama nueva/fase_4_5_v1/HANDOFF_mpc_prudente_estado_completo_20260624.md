# HANDOFF maestro — MPC Neuronal Prudente (estado completo del TFG)

> **Léeme primero al abrir sesión nueva.** Resume TODO lo hecho con Claude en el
> controller IA del TFG: qué es, resultado final, validez, mapa de código y cómo
> retomar. Convive con `CLAUDE.md`, `AGENTS.md` y los `decision_*.md` de esta carpeta.

| Campo | Valor |
|---|---|
| Fecha | 2026-06-24 |
| Rama | `rebuild/phase3-from-phase2` |
| Estado | **Parte técnica TERMINADA**. Falta escribir la memoria. |
| Controller | **MPC Neuronal Prudente** (`mpc_prudente_v1` MLP, `mpc_prudente_v2` temporal ensemble) |

## 1. Qué construimos (1 párrafo)

Un controller ABR con IA **fiel al medio (VBR real)** y **consciente del riesgo**:
un **predictor neuronal de cuantiles de throughput** (aprendizaje supervisado, no
RL ni imitation) + un **planner MPC prudente (CVaR)** que usa los **tamaños reales**
de cada segmento del vídeo. Dos versiones: v1 = MLP; **v2 = deep-ensemble temporal
(GRU) con incertidumbre epistémica** que ensancha la cola inferior cuando los
modelos discrepan. Paradigma Fugu/Puffer/BayesMPC (predictor + control), no caja
negra. Causa raíz que arreglamos: el viejo Neural-MPC asumía **CBR** y el cliente
reproduce **VBR**.

## 2. RESULTADO FINAL — Phase 6 `tfg_final` (paquete `20260624_182747_tfg_final`)

360 sesiones (288 reales + 72 sintéticas), 6 controllers, 4 vídeos (Paseo+Blender ×
30/60fps), eval split, **ranking autorizado, gates OK, 0 fallback, 1740/1740
inferencias auditadas por propio**.

| controller | QoE media | bitrate | rebuffer medio | stalls/sesión | sesiones>5s | sesiones>10s |
|---|---:|---:|---:|---:|---:|---:|
| **v2 temporal** | **2.013** | 2636 | 3.05 | 0.29 | 12% | 10% |
| rate_based | 1.979 | 2350 | 1.43 | 0.17 | 8% | 8% |
| robust_mpc | 1.953 | 2685 | 3.82 | 0.44 | 23% | 12% |
| v1 MLP | 1.935 | 2600 | 3.54 | 0.42 | 17% | 12% |
| bba | 1.790 | 2535 | 3.17 | 0.31 | 12% | 8% |
| bola | 1.161 | 2118 | 5.59 | 1.88 | 17% | 17% |

Estadística pareada vs robust_mpc (n=48): v2 ΔQoE=**+0.060** CI95 [−0.05,+0.21]
sign_p=**0.54** (TIE, no significativo); v1 −0.018 (tie); rate_based +0.026; bba
−0.16 (sig.); bola −0.79 (sig.).

**Lectura honesta:**
- **v2 tiene la QoE media MÁS ALTA de los 6** y está **estadísticamente empatado**
  con robust_mpc (no es win significativo) — pero además **REDUCE el rebuffering**
  vs robust (stalls 0.29 vs 0.44, >5s 12% vs 23%, rebuffer 3.05 vs 3.82).
- **v2 mejora claramente al v1 MLP** (2.013 vs 1.935) → ablación que valida el
  ensemble temporal.
- **rate_based** es el "seguro" (rebuffer 1.43, mejor peor-caso P5=−1.50) a costa de
  bitrate; v2 es más agresivo (más calidad + menos stalls que robust, pero peor
  cola extrema P5=−3.7, concentrada en el vídeo más duro Blender 60fps + traza
  outage real_012).
- Los clásicos se comportan como dice la literatura (BOLA-basic peor, robust fuerte).

**Tesis para la memoria:** *"Controller ABR híbrido fiel al medio (VBR) y consciente
del riesgo, con predictor temporal deep-ensemble e incertidumbre epistémica:
**QoE media más alta de todos los controllers, estadísticamente equivalente a
robust_mpc, reduciendo el rebuffering** (menos stalls y sesiones de corte). El
ensemble temporal mejora al MLP."* (NO afirmar "gano a todos" — es empate honesto.)

## 3. Validez y honestidad (verificado por Claude)

- **Baselines FIELES a sus papers** (verificado código vs literatura): rate_based
  (Liu 2011), bba (Huang 2014 BBA-0 reservoir/cushion), bola (Spiteri 2016, variante
  **BOLA-BASIC** con V/γ fijos — documentado), mpc (Yin 2015 FastMPC), **robust_mpc
  (Yin 2015 RobustMPC, fórmula `media_armónica/(1+max_error)` exacta — canónico)**.
  Cada uno con `paper_card.md` + `source_evidence.md` en `docs/contexto rama original/01_baselines/`.
- **Comparación justa**: TODOS corren en el mismo cliente, mismas trazas (pareadas),
  misma QoE congelada, mismos vídeos, mismas semillas. Eval split reservado (sin
  fuga). Validez relativa = condiciones idénticas, no "binario canónico".
- **No hay trampa**: robust_mpc es fuerte y empata/casi-gana → prueba de que no se
  amañó. Resultados negativos reportados (SPBC, Q_H, "más datos no mejora").
- **Sutileza honesta**: los MPC clásicos optimizan internamente calidad log-rate-ratio;
  la eval usa QoE bitrate-lineal. Es decisión de modelado defendible y va EN CONTRA
  de nuestro controller (robust_mpc no optimiza la métrica de eval y aun así empata).
- **Multi-vídeo SIN sesgo**: dataset rota los 8 vídeos de 4s; en runtime cada sesión
  inyecta el media del vídeo activo → el planner usa sus tamaños VBR reales. Mata la
  crítica "ajustado a un vídeo".

## 4. Mapa de código (línea mpc_prudente)

- `core/mpc_prudente/media_profile.py` — tablas VBR reales + `MediaFaithfulLadder` +
  `resolve_media_descriptor_id` (Phase6 id → descriptor).
- `core/mpc_prudente/dataset.py` — dataset fiel (single + `build_mpc_prudente_multimedia_dataset`).
- `core/mpc_prudente/training.py` (MLP) + `temporal_model.py` (GRU+ensemble) +
  `temporal_training.py` (entrena ensemble) — predictores.
- `core/mpc_prudente/planner.py` — planner CVaR (riesgo) con tamaños reales.
- `core/mpc_prudente/bundle.py` (MLP) + `temporal_bundle.py` (ensemble + dispatcher
  `load_prudent_runtime_bundle`) — bundles runtime.
- `core/mpc_prudente/evaluation.py` — diagnóstico closed-loop offline interno.
- `core/controller/mpc_prudente_runtime.py` — controllers runtime v1 + v2
  (`MpcPrudenteRuntimeController`, `MpcPrudenteTemporalRuntimeController`).
- Registry: `mpc_prudente_v1`, `mpc_prudente_v2`.
- Phase 6: `core/phase6/analysis.py` (métricas cola/catastróficas/stalls + plots
  `qoe_robustez_peor_caso`, `stalls_por_controller`), `catalog.py` (preset
  `comparativa` y `tfg_final`), runner inyecta media por sesión.
- Tablas VBR commiteadas: `media_profiles/segment_sizes/*.json` (8 perfiles).
- Tests: `tests/test_mpc_prudente_*`, `test_phase6_*`. (489 OK al cerrar.)

## 5. Artefactos externos (fuera de Git, en ~/TFG)

- Dataset multimedia: `~/TFG/datasets_normalizados/mpc_prudente/throughput_quantile_full_v1_multimedia`
- Modelos: `~/TFG/modelos/mpc_prudente/temporal_predictor/full_multimedia` (ensemble)
  y `.../runtime_bundle_v1` (MLP), `.../temporal_runtime_bundle_v1` (temporal).
- Paquetes Phase 6: `~/TFG/runs_trazas/phase6/...` (el final: `20260624_182747_tfg_final`).

## 6. Comandos clave (Daniel ejecuta; Claude prepara/commitea desde Windows)

- WSL dataset multivídeo: `bash scripts/run_mpc_prudente_multimedia_dataset_wsl.sh`
- WSL train temporal: `bash scripts/run_mpc_prudente_temporal_training_wsl.sh`
- WSL export bundle temporal: `bash scripts/run_mpc_prudente_temporal_bundle_wsl.sh` (luego mover tarball a Ubuntu)
- Ubuntu Phase 6 final: GUI preset `tfg_final` + 6 controllers, o
  `python3 scripts/run_phase6_validacion_comparativa.py --config config/phase6.local.json --preset tfg_final`
- Sync: WSL/Ubuntu `git pull`; Windows (Claude) commitea con rutas explícitas.

## 7. Pendiente / opciones

- **Memoria** (lo principal que queda): redactar con este resultado + ablaciones +
  resultados negativos + validez metodológica.
- Opcional (si hay tiempo): doc "validez metodológica" formal; afinar la cola
  extrema de v2 en Blender 60fps; alinear objetivo interno de robust_mpc con la
  QoE de eval (rigor máximo, invalida runs previos).

## 8. Cómo trabajar (recordatorio)

Caveman siempre pero entendible. Claude (Windows) desarrolla/commitea/pushea con
rutas explícitas; Daniel ejecuta en WSL (entrena) / Ubuntu cliente (Phase 6) y pega
resultados. Artefactos pesados fuera de Git. No tocar player/runtime/eval sin
contrato+tests. No claims sin gates de Phase 6.
