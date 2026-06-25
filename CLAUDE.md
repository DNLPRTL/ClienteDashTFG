# CLAUDE.md — guía de trabajo con Claude Code

Este archivo lo carga Claude Code en cada sesión. Es el puente para que, aunque
se llene el contexto o se abra una sesión nueva, Claude retome el proyecto sin
perder rigor. Convive con `AGENTS.md` (guía de Codex): **ambos agentes comparten
los mismos documentos canónicos** para no divergir.

## 0. Cómo trabajar conmigo (Daniel ⇄ Claude)

- **Idioma y estilo:** responder siempre en español y en modo *caveman* (denso,
  sin relleno), pero **explicado para que Daniel lo entienda entero**, aunque se
  recorte. Si algo es delicado (riesgo, comando destructivo, orden de pasos),
  salir de caveman y explicar claro.
- **Contrato operativo (igual que con Codex):**
  - Claude (Windows) desarrolla, escribe scripts/docs/tests, valida rápido,
    commitea y pushea con rutas explícitas (nunca `git add .`).
  - Daniel ejecuta en **WSL2** los entrenamientos pesados y en **Ubuntu cliente**
    las validaciones Phase 6. Pega resultados/logs. Se decide el siguiente paso.
  - Comandos a Daniel: **cortos**. Preferir `git pull` + `bash scripts/<x>.sh`.
    Nada de heredocs largos ni listas de flags manuales: versionar un script.
- **Sincronización por GitHub (siempre dar estos comandos al cerrar un cambio):**
  - WSL2 entrenamiento:
    ```bash
    wsl -d Ubuntu-24.04
    cd ~/TFG/DashClientModular4
    git pull
    source ~/venvs/rocm721/bin/activate
    ```
  - Ubuntu cliente validación:
    ```bash
    cd ~/TFG/DashClientModular4
    git pull
    ```
- **Sincronía con Codex:** cada cambio relevante se acompaña de un `.md` de
  contexto/decisión commiteado junto al código (estilo `decision_*.md`), para que
  si Daniel trabaja con Codex y hace `git pull`, sepa exactamente qué se hizo.

## 1. Lectura obligatoria en cada sesión (autoridad canónica)

Antes de proponer cambios técnicos, leer/recordar:

```text
docs/contexto rama nueva/fase_4_5_v1/HANDOFF_mpc_prudente_estado_completo_20260624.md  <- LÉEME 1º (estado completo + resultado final)
AGENTS.md
docs/arquitectura y procedimientos estandar tfg dash/arquitectura_y_procedimientos_estandar_tfg_dash.md
docs/arquitectura y procedimientos estandar tfg dash/TFG_PLAN_GENERICO.md
docs/contexto rama nueva/fase_4_5_v1/proceso_desarrollo_ia_abr.md
docs/contexto rama nueva/fase_4_5_v1/plan_maestro_controller_ia_claude_20260619.md
docs/contexto_para_ia/CONTEXTO_ABSOLUTO_DASHCLIENTMODULAR4_20260615.md
```

Contexto secundario cuando haga falta: `docs/contexto rama nueva/`,
`docs/contexto rama original/`, `docs/todos los estudios pdf convertidos a md/`.

Regla: **no implementar desde PDFs brutos** si existe source card / spec /
decisión / doc operativo.

## 2. Cuatro entornos (no es una sola máquina)

| Entorno | Rol | Ruta |
|---|---|---|
| Windows físico | desarrollo, tests rápidos, commits, push | `C:\Users\danie\Documents\TFG\DashClientModular4` |
| WSL2 Ubuntu ROCm | entrenamiento IA pesado (GPU AMD RX 7800 XT) | `~/TFG/DashClientModular4`, venv `~/venvs/rocm721` |
| Ubuntu cliente | validación real, Phase 6, evidencia | `~/TFG/DashClientModular4` |
| Ubuntu servidor | sirve MPD/segmentos/inits por HTTP | `192.168.1.132:/var/www/html/dash` |

Si Windows y Ubuntu cliente discrepan, **manda Ubuntu cliente**. Artefactos
pesados (datasets, modelos, bundles, runs, logs, segmentos, PDFs) **fuera de Git**,
bajo `~/TFG/...` (Linux) o `C:\Users\danie\Documents\TFG\...`.

## 3. Datos canónicos (no confundir red con medio)

- **Red (emulación) — corpus original:** manifest curado
  `~/TFG/manifests_trazas/phase3/final/phase3_trace_manifest_curated.json`
  (`trace_count=6768`, sintéticas `1024`; eval ≈ 1025 trazas, FCC domina). Es un
  **corpus externo curado** (FCC, Norway, Oboe, Roma, UCC, Lumos5G, Puffer, etc.
  + sintéticas controladas), NO capturas propias. Eval NO se toca para entrenar.
- **Medio (contenido DASH) — perfil real:** MPD `Paseo_Almunecar_10min_30fps_simple_4s.mpd`,
  **6 niveles** `300/750/1200/1850/2850/4300 kbps`, **151 segmentos de 4 s**, VBR.
- Los datasets de entrenamiento IA son **derivados** del manifest, viven en
  `~/TFG/datasets_normalizados/...` y `~/TFG/modelos/...`.

## 4. Contratos congelados (no romper)

- QoE/reward: `reward_n = bitrate_mbps - 4.3*rebuffer_s - smoothness_mbps`;
  métrica primaria `qoe_linear_mean`. `qoe_log_v1` secundaria. `startup_delay_s`
  report-only. VMAF deferred.
- Sin claims de mejora/ranking/ganador fuera de Phase 6 con gates superados.
- No tocar `player.py`, runtime, media engine, controllers ni evaluación sin
  contrato explícito + tests.
- Splits por `leakage_group`, nunca por filas. El controller nunca ve
  `trace_id/dataset_id/split/leakage_group/futuro throughput`.
- Validación mínima Windows: `python -m unittest discover` y
  `python scripts/check_client_readiness.py --strict`.

## 5. Estado y línea activa (resumen; detalle en el PLAN ACTIVO)

- Rama: `rebuild/phase3-from-phase2`. Cliente terminado y ABR-neutral.
- Baselines clásicos cerrados: `rate_based, bba, bola, mpc, robust_mpc`.
- IA previa: `NeuralABR-Lite` (Phase 4/5). Líneas Neural-MPC v1/v2 ya probadas en
  Phase 6 diagnostico/rapido (15/06): técnicamente válidas pero **v2 NO mejora**
  (más agresiva, más rebuffer; peor QoE que v1 y que `robust_mpc`).
- Líneas abandonadas: SPBC/SPC, Q_H scorer (se conservan como **resultados
  negativos** para la memoria).
- **Línea activa: MPC Neuronal Prudente (`mpc_prudente_v1` MLP, `mpc_prudente_v2`
  temporal ensemble).** Predictor neuronal de cuantiles (supervisado) + planner MPC
  prudente (CVaR) con tamaños VBR reales. PARTE TÉCNICA TERMINADA.
- **Resultado final (Phase 6 `tfg_final`, 360 sesiones, 6 controllers, 4 vídeos):**
  v2 temporal = QoE media más alta (2.013), empatado estadísticamente con robust_mpc
  (sign_p=0.54) y con menos rebuffering (stalls 0.29 vs 0.44, >5s 12% vs 23%); v2 > v1.
  Todo en `HANDOFF_mpc_prudente_estado_completo_20260624.md`. PENDIENTE: la memoria.
