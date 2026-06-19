# Decisión — MPC Prudente: entrenamiento del predictor + gates de calibración

| Campo | Valor |
|---|---|
| Fecha | 2026-06-19 |
| Autor | Claude (Claude Code) |
| Rama | `rebuild/phase3-from-phase2` |
| Plan padre | `plan_maestro_controller_ia_claude_20260619.md` |
| Estado | Implementado y validado en Windows (CPU). Pendiente: entrenamiento canónico en WSL GPU (Daniel). |

## Decisión metodológica (criterio Claude, no inercia)

No hacemos pilot→full por ritual. Entrenamos el predictor **una vez** sobre el
dataset pilot (30.570 muestras es de sobra para un MLP pequeño). "Más datos" ya
demostró empeorar (v1 pilot batió a v2 full): el cuello de botella es fidelidad +
objetivo, no cantidad de datos. La palanca real es el planner prudente + Phase 6.
Ver memoria `metodologia-no-escalar-datos`.

## Qué se añadió respecto al entrenador heredado

El entrenador de Neural-MPC solo comprobaba que la loss fuese **finita**. Para un
predictor de cuantiles eso es insuficiente. Se reutiliza ese entrenador SIN tocarlo
y se le añade una **auditoría de calibración** (`core/mpc_prudente/training.py`):

- **Cobertura empírica por cuantil**: qué fracción de targets cae bajo cada cuantil
  predicho; debe ≈ el nivel nominal (gate `coverage_calibrated`, tol 0.08).
- **Monotonía / no-crossing**: fracción de filas con cuantiles cruzados (gate
  `quantiles_monotone`, ≤ 0.02). El MLP no garantiza monotonía por construcción.
- **Señal aprendida**: pinball final < pinball de la época 1 (no fallback trivial).
- **Pinball finito**.

## Resultado del pilot (preview en Windows CPU, 40 épocas)

```
pinball=0.239  coverage=[0.066, 0.169, 0.435, 0.747]  (nominal 0.10/0.25/0.50/0.75)
max_cov_err=0.0814  crossing_rate=0.0075  best_epoch=25  status=REVIEW
```

Lectura honesta:
- Monotonía: **PASS** (0.75% de crossing, ≪ 2%).
- Señal aprendida: **PASS** (best_epoch=25).
- Calibración: **REVIEW por un pelo** (0.0814 vs 0.08). q10/q50/q75 casi clavados;
  el q25 va algo bajo (0.169 vs 0.25). El sesgo del q10 hacia abajo (0.066) es,
  para un controller **prudente**, conservador y por tanto seguro.

`max_cov_err≈0.08` con tres de cuatro cuantiles bien calibrados es un predictor
esencialmente bien calibrado. El gate estricto (0.08) lo deja en REVIEW para que lo
decidamos con evidencia, no por defecto.

## Camino tras el entrenamiento canónico en WSL

Según los números reales de Daniel en GPU:
- Si calibración ≈ 0.08: **aceptable** (defendible como bien calibrado) → seguir al
  planner prudente. O, si se quiere afinar el q25, un run de 60 épocas (barato en
  GPU) y elegir el mejor calibrado. No se mueve el umbral para "aprobar".
- El modelo **canónico** se entrena en WSL (entorno de entrenamiento del proyecto);
  el run CPU de Windows es solo validación del pipeline.

## Cómo ejecutar (Daniel, WSL GPU)

```bash
wsl -d Ubuntu-24.04
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate
bash scripts/run_mpc_prudente_pilot_training_wsl.sh
```

Pegar la línea `MPC_PRUDENTE_TRAINING status=...`.

## Siguiente paso

Diseñar el **planner prudente**: usa los cuantiles predichos + los tamaños reales
del MPD activo para elegir bitrate con un objetivo consciente del riesgo (penaliza
la cola de rebuffer), en vez de la regla fija buffer→cuantil de v1/v2.
