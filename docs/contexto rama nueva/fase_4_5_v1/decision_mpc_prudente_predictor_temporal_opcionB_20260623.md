# Decisión — Opción B: predictor temporal (GRU) + ensemble profundo

| Campo | Valor |
|---|---|
| Fecha | 2026-06-23 |
| Autor | Claude (Claude Code) |
| Rama | `rebuild/phase3-from-phase2` |
| Estado | Código listo y probado en Windows (smoke real OK). Pendiente: dataset full + entrenamiento full en GPU (Daniel). |

## Por qué B (la evidencia lo pide)

El `comparativa` formal mostró: prudente **empata** a robust_mpc, más suave, gana en
`real_005` (variable), pero PIERDE en ventanas duras (`real_011`, `real_012`). El
diagnóstico: en `real_012` el predictor MLP se pasó de **optimista** → ni la
prudencia salvó. **El cuello de botella es el predictor, no el planner.**

## El mejor predictor para este caso

`core/mpc_prudente/temporal_model.py` + `temporal_training.py`:

1. **GRU** que LEE la secuencia de red (no un vector aplanado) → capta tendencias.
2. **Cuantiles monótonos por construcción** (base + incrementos softplus
   acumulados): imposible que se crucen. Sin penalización ni postproceso.
3. **Ensemble profundo** (M modelos con semillas distintas). Su **discrepancia**
   mide la incertidumbre epistémica; el combinador **ensancha la cola inferior**
   proporcional a esa discrepancia → en ventanas raras/OOD (donde el MLP se pasaba
   de optimista) el controller se vuelve más prudente SOLO. Es el arreglo directo
   de `real_012`. (Deep ensembles = estado del arte en incertidumbre calibrada;
   BayesMPC es la versión bayesiana.)

Reutiliza el dataset fiel (mismo contexto de 5 pasos + targets) y la loss pinball.
Auditoría de calibración con la predicción de ensemble.

## Validación en Windows (smoke real, 2 miembros, 8 épocas)

Pipeline end-to-end OK (entrena, ensembla, calibra, guarda). Calibración aún floja
con 2/8 (`max_cov_err=0.11`); el full (5 miembros, 80 épocas) la afina. 485 tests OK.

## Pipeline (Daniel ejecuta paso a paso)

### 1. (WSL) Dataset FULL fiel
```bash
wsl -d Ubuntu-24.04
cd ~/TFG/DashClientModular4 && git pull
source ~/venvs/rocm721/bin/activate
bash scripts/run_mpc_prudente_full_dataset_wsl.sh
```
→ `MPC_PRUDENTE_DATASET status=PASS`

### 2. (WSL GPU) Entrenar el predictor temporal ensemble (full)
```bash
bash scripts/run_mpc_prudente_temporal_training_wsl.sh
```
→ pega `MPC_PRUDENTE_TEMPORAL status=...` (miramos coverage, max_cov_err, epistemic).

### 3. Si la calibración convence → bundle + controller temporal + Phase 6 `comparativa`
(Lo preparo cuando me pases el resultado del entrenamiento.)

## Qué esperar / criterio

- Buena calibración (`max_cov_err <= 0.08`), miembros con loss finita.
- `epistemic` > 0 (los miembros discrepan → hay incertidumbre que explotar).
- El objetivo: que en ventanas duras la cola se ensanche y el planner evite el
  stall que perdió `real_012`. Se verá en Phase 6.
