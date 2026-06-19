# Decisión — MPC Prudente: generador de dataset de entrenamiento FIEL

| Campo | Valor |
|---|---|
| Fecha | 2026-06-19 |
| Autor | Claude (Claude Code) |
| Rama | `rebuild/phase3-from-phase2` |
| Plan padre | `plan_maestro_controller_ia_claude_20260619.md` |
| Estado | Implementado y validado en Windows con datos reales (perfil smoke). Pendiente: pilot en WSL (Daniel). |

## Qué es

El dataset que aprende el predictor de `mpc_prudente`, generado con **fidelidad al
medio**: los rollouts avanzan el buffer con el **peso real (VBR)** de cada segmento
del MPD (tabla `media_profiles/segment_sizes/<id>.json`), no con CBR.

## Cómo (reutilización, sin duplicar ni romper lo congelado)

- Se reutiliza el generador probado `build_phase45_v3_throughput_quantile_dataset`.
- Se le añade un parámetro **opcional** `ladder_factory` (compatible hacia atrás:
  sin él, comportamiento CBR idéntico). La línea MPC Prudente le pasa una factoría
  que construye un `MediaFaithfulLadder` por ventana.
- `core/mpc_prudente/media_profile.py`: `MediaFaithfulLadder` (tamaños reales,
  cíclico para ventanas largas, offset opcional) compatible con el motor congelado.
- `core/mpc_prudente/dataset.py`: ensambla la factoría + el medio y llama al builder.
- `scripts/generar_dataset_mpc_prudente.py` + `scripts/run_mpc_prudente_pilot_dataset_wsl.sh`.
- El resumen del dataset marca `segment_size_source = "real_vbr_from_server"` y el
  `media_profile_id` real, para distinguirlo del CBR.

## Arquitectura de generalización (importante)

- **Predictor**: agnóstico al medio (predice throughput). Basta entrenarlo con un
  medio representativo (Paseo 10min 30fps 4s) para que el buffer evolucione realista.
- **Planner** (siguiente paso): en runtime usará los tamaños reales del MPD que se
  esté reproduciendo. Por eso el controller generaliza a los 8 perfiles sin
  reentrenar el predictor por cada vídeo.

## Validación hecha

- Tests: 468 OK (incluye dataset fiel end-to-end y compatibilidad del builder v3).
- Smoke real en Windows (manifest curado + trazas reales + descriptor real Paseo):
  `status=PASS segment_size_source=real_vbr_from_server train=720 val=240 leakage=PASS skipped_windows=0`.

## Cómo ejecutar el pilot (Daniel, WSL)

```bash
wsl -d Ubuntu-24.04
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate
bash scripts/run_mpc_prudente_pilot_dataset_wsl.sh
```

Pegar la línea `MPC_PRUDENTE_DATASET status=...`.

## Siguiente paso tras el pilot

Entrenar el predictor de cuantiles sobre este dataset (reutilizando el entrenador
de Neural-MPC) y, en paralelo, diseñar el **planner prudente** (objetivo consciente
del riesgo sobre la cola del throughput) que usará los tamaños reales en runtime.
