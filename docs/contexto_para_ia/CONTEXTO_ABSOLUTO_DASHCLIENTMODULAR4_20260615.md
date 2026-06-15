# Contexto absoluto tecnico - DashClientModular4

| Campo | Valor |
|---|---|
| Proyecto | `DashClientModular4` |
| Ruta Windows | `C:\Users\danie\Documents\TFG\DashClientModular4` |
| Raiz TFG Windows | `C:\Users\danie\Documents\TFG` |
| Fecha de generacion | `2026-06-15T15:56:53+02:00` |
| Rama activa esperada | `rebuild/phase3-from-phase2` |
| HEAD observado | `caa8b7a69a6c3d2fceb2c17cd2d544f962ba6a76` |
| Entregable IA | `C:\Users\danie\Documents\TFG\DashClientModular4\docs\contexto_para_ia\CONTEXTO_ABSOLUTO_DASHCLIENTMODULAR4_20260615.md` |
| Entregable humano | `C:\Users\danie\Documents\TFG\DashClientModular4\output\pdf\CONTEXTO_ABSOLUTO_DASHCLIENTMODULAR4_20260615.pdf` |

## Proposito exacto

Este documento consolida el estado tecnico y operativo materializado en el repositorio y en las carpetas hermanas visibles de `C:\Users\danie\Documents\TFG`. Esta pensado para que otra IA pueda continuar el proyecto sin depender de memoria conversacional no versionada.

El documento contiene hechos, contratos, rutas, fases, reglas, arquitectura, estado actual, catalogos de fuentes y piezas de codigo. No contiene recomendaciones nuevas, ranking, conclusiones subjetivas ni afirmaciones de mejora de QoE no autorizadas.

## Alcance verificable

- Incluye documentos y chats que estan materializados como archivos Markdown dentro del repo, especialmente `docs/contexto del orquestador el chat web/CONTEXTO_MAESTRO_WEB_TFG.md`.
- Incluye inventario automatico del codigo, scripts, tests, docs y carpetas externas visibles.
- No afirma haber leido conversaciones que no existan como archivo accesible en el filesystem.
- No copia datasets, modelos, trazas, bundles, zips, PDFs ni media al repositorio.

## Fuentes inspeccionadas

| Fuente | Conteo | Observacion |
|---|---:|---|
| Archivos versionados detectados por `git ls-files` | 1081 | Inventario de repo limpio sin `.git` |
| Markdown versionados | 761 | Docs, source cards, decisiones, runbooks y corpus convertido |
| Modulos Python inventariados | 274 | `core`, `scripts`, `tests`, entrypoints y utilidades |
| Scripts/runbooks en `scripts/` | 103 | Python y shell versionados |
| Tests Python | 75 | `unittest`/tests estructurales |
| Directorios externos bajo raiz TFG | 846 | Inventario de carpetas hermanas y paquetes generados |

Documentos obligatorios leidos y usados como autoridad inicial:

```text
docs/arquitectura y procedimientos estandar tfg dash/arquitectura_y_procedimientos_estandar_tfg_dash.md
docs/arquitectura y procedimientos estandar tfg dash/TFG_PLAN_GENERICO.md
docs/contexto rama nueva/fase_4_5_v1/proceso_desarrollo_ia_abr.md
```

Contexto secundario usado cuando aplica:

```text
docs/contexto rama nueva/
docs/contexto rama original/
docs/contexto del orquestador el chat web/
docs/todos los estudios pdf convertidos a md/
```

## Estado actual de rama y continuidad

Estado Git observado al generar este documento:

```text
## rebuild/phase3-from-phase2...origin/rebuild/phase3-from-phase2
?? docs/contexto_para_ia/
?? output/
?? scripts/generate_contexto_absoluto.py
```

Ramas observadas:

```text
archive/current-before-phase3-rebuild                133f24ca4f34b9c3f546c3bb16c10884dcc7f623 feat(validation): add Phase 6 MPD media profile freeze
  main                                                 133f24ca4f34b9c3f546c3bb16c10884dcc7f623 [ahead 1] feat(validation): add Phase 6 MPD media profile freeze
* rebuild/phase3-from-phase2                           caa8b7a69a6c3d2fceb2c17cd2d544f962ba6a76 feat(phase45): add closed-loop spbc spc dataset
  remotes/origin/archive/current-before-phase3-rebuild 133f24ca4f34b9c3f546c3bb16c10884dcc7f623 feat(validation): add Phase 6 MPD media profile freeze
  remotes/origin/main                                  099ce7e054ed580a89b8a79d692d0fb9c74e163d fix(validation): harden Phase 6C live materialization
  remotes/origin/rebuild/phase3-from-phase2            caa8b7a69a6c3d2fceb2c17cd2d544f962ba6a76 feat(phase45): add closed-loop spbc spc dataset
```

Lectura tecnica del estado:

- La rama activa es `rebuild/phase3-from-phase2`.
- La rama `archive/current-before-phase3-rebuild` existe como referencia historica protegida del estado anterior a la reconstruccion desde Phase 2.
- `main` aparece como referencia historica/otra rama, no como rama activa de trabajo de este hilo.
- El ultimo commit observado en la rama activa es `feat(phase45): add closed-loop spbc spc dataset`.
- La fase activa declarada por `AGENTS.md` es `Phase 6 implementation ready - validacion comparativa formal`.
- Fase 4-5 v1 queda abierta como iteracion nueva e independiente para controllers IA nuevos; no sustituye las Phase 4/5 cerradas.

Log reciente de la rama activa:

```text
* caa8b7a (HEAD -> rebuild/phase3-from-phase2, origin/rebuild/phase3-from-phase2) feat(phase45): add closed-loop spbc spc dataset
* 2492c38 Add phase45 v3 neural MPC v2 bundle flow
* eae24ad Prepare phase45 v3 neural MPC full v2 training
* 414e582 docs(phase45): define IA ABR development process
* 502e0f7 feat(phase45): integrate neural mpc runtime controller
* 788c6dc docs(phase45): add neural mpc ubuntu bundle validation
* fa00e2f feat(phase45): export neural mpc experimental bundle
* fee2307 docs(phase45): prepare neural mpc experimental candidate
* ae2d5ad fix(phase45): monotonicize neural mpc checkpoint quantiles
* 7afeb26 chore(phase45): add neural mpc expanded diagnostic runbook
* 2d83d0e docs(phase45): record neural mpc diagnostic pass
* 7ad7748 tune(phase45): make neural mpc medium-buffer planning safer
* d4b0d4f feat(phase45): add neural throughput calibrated mpc
* fd5dc90 docs(phase45): make QH scorer blockage report self-contained
* 7f1af61 feat(phase45): add softer hard-negative qh scorer
* f2c2f02 feat(phase45): add hard-negative QH scorer profile
* d5d637e docs(phase45): update QH scorer blockage report
* ddd3d8a chore(phase45): add QH scorer error analysis
* 94f75b2 feat(phase45): add temporal GRU QH scorer profile
* d9510cb chore(phase45): require GPU for adv regret runbook
* 4c5a217 feat(phase45): add advantage regret QH scorer profile
* c3396fd docs(phase45): document QH scorer pilot blockage
* e8d07b6 chore(phase45): add QH scorer pilot rank WSL runbook
* c81911a feat(phase45): add regret-aware QH scorer profile
* 8d93e61 chore(phase45): add QH scorer pilot plus profile
* bb99174 fix(phase45): mask infeasible QH scorer targets
* 9974467 chore(phase45): loosen QH scorer smoke quality gate
* 84c2c85 feat(phase45): train v3 QH scorer
* 7ba3909 fix(phase45): keep v3 audit imports lightweight
* 589b283 chore(phase45): summarize v3 QH dataset audits
* 449ce89 feat(phase45): generate v3 closed-loop QH dataset
* cd5e537 chore(phase45): clarify collapse audit missing results path
* 174268f feat(phase45): add v3 closed-loop oracle and collapse audit
* 84547bf feat(phase45): integrate SPBC v2 ABR controller
* 9cb757d docs(phase45): document SPBC ABR model evidence
* c7d9736 feat(phase45-v1): add safe advantage SPBC probe
* b465cd6 feat(phase45-v1): add safe PPO SPBC pilot
* 42528e4 feat(phase45-v1): add SPC critic copilot training
* 376d8b7 chore(phase45-v1): show residual safe-rank epoch diagnostics
* 13be6b0 feat(phase45-v1): add residual safe-rank SPBC pilot
* 3b96047 chore(phase45-v1): add hybrid veto threshold sweep
* 144499b chore(phase45-v1): keep hybrid runner output compact
* 61b6ceb feat(phase45-v1): add spbc spc hybrid offline validation
* d9c34e6 docs(phase45-v1): reset spc as calibrated critic
* 1a9ffb5 feat(phase45-v1): add safe rank loss for spc reward risk
* 73bd7f3 chore(phase45-v1): prepare spc reward risk dagger2 pilot
* c3ee4d2 docs(phase45-v1): record anchor safe rank full result
* 2967c93 chore(phase45-v1): script anchor safe rank full run
* ab40de1 chore(phase45-v1): add anchor safe rank wsl runner
* d41b86b feat(phase45-v1): add safe rank loss for spbc dpo
* 9700c68 chore(phase45-v1): add safe margin seed checks
* 44bde57 feat(phase45-v1): add safe margin dpo training losses
* fed1eb4 feat(phase45-v1): gate dagger checkpoint selection
* 244010a feat(phase45-v1): support warm v2 dagger training
* 21e0bcc feat(phase45-v1): add dagger2 on-policy dataset builder
* 93ff968 feat(phase45-v1): add reward risk scorer training
* 32a8132 feat(phase45-v1): add utility risk spbc v2 training
* 8204cfc feat(phase45-v1): add utility-aware spbc v2 training
* 9b57d3a feat(phase45-v1): add spbc v2 dpo training
* f59db3f feat(phase45-v1): add preference on-policy v2 dataset
* 933ad70 feat(phase45-v1): add spbc spc offline validation
* f2268f3 feat(phase45-v1): add spbc abr offline training
* e9b113b feat(phase45-v1): show spc training progress
* 8481c3a feat(phase45-v1): add spc abr offline training
* 6c9a9a6 feat(phase45-v1): add spc spbc dataset generator
* b0319d1 docs(phase4-5-v1): decide new abr ai candidates
* 4e0d236 docs(phase4-5-v1): complete paper corpus
* e9b3f9d docs(phase4-5-v1): reset corpus and add wsl gpu context
* 713fd2f docs(phase4-5-v1): add detailed paper technical matrix
* 73d6f48 docs(phase4-5-v1): clarify greenfield controller direction
* b3c2911 docs(phase4-5-v1): audit abr ai paper corpus
* b8ddadd fix(phase6): tolerate non-utf8 child logs
* ec1cc60 fix(phase6): audit neural inference in own controllers
* a5b4d02 feat(phase6): add diagnostic preset and package audit
* f631784 fix(phase6): harden trace replay validation
* a0f8502 feat(phase6): implement comparative validation pipeline
* d045c42 docs(verification): close client verification and hand off phase6
* 1a52a43 feat(verification): add classic controller verification phase
* 6fb9d44 docs(neural-abr): close phase5 ubuntu smoke
* d5a407d feat(neural-abr): integrate two guarded controllers
* 0d6e2de docs(neural-abr): close phase4 and hand off phase5
* 8e08d4e feat(neural-abr): train robust model from real controller
* c2915c4 feat(neural-abr): add phase4 hybrid teacher model path
* f5da074 feat(neural-abr): export phase4 inference bundle
* b5ccc36 feat(neural-abr): add phase4 candidate training gate
* 4e6a419 feat(neural-abr): add phase4 offline training data pipeline
* e199c8c feat(neural-abr): add phase4a training trace sampler
* 7cfbeb4 feat(trace): add synthetic controlled network traces
* 09b4c54 feat(qoe): rebuild Phase 3.5 QoE reward methodology
* ebc405c feat(trace): add Phase 3 quality audit
* cc568b3 feat(trace): close Phase 3 trace corpus
* c46a381 feat(trace): rebuild Phase 3 trace pipeline
* 7f4686f docs(rebuild): refresh Phase 3 rebuild context
* 792c6e8 docs(rebuild): record Phase 3 rebuild start point
* 28f9741 docs(science): formally close Phase 2 baseline work
* db5f8c8 docs(science): close Phase 2.3 baseline implementation audit
* 504f48f feat(controller): add RobustMPC ABR baseline
* a36be16 feat(controller): add MPC ABR baseline
* 1819aa3 feat(controller): add BOLA ABR baseline
* 2120c5f feat(controller): add BBA ABR baseline
* cf5e583 feat(controller): add rate based ABR baseline
* 19fe1ed feat(controller): add sanity rate controllers
* ac082df docs(science): add Phase 2 controller academic validation gate
* 7a2dac7 docs(science): add Phase 2 ABR baseline operational specs
* 6e0886e docs(science): add Phase 2 PDF-grounded source evidence
* c12ba5a docs(science): scaffold Phase 2 ABR baseline literature docs
* 00d4f8b (tag: phase1-client-readiness) Certify client readiness for Phase 1 closure
* 8334adb Document Phase 1 acceptance and metric provenance
* 6f36888 Harden GStreamer integration path
* 21631a6 Clean up academic run artifacts
* 8ae0d57 Add benchmark neutrality contract
* 52a9da4 Start runtime player responsibility split
* 4a807a4 Add deterministic test controllers
* f0ff8bd Document controller decision contract
* ec94bf1 Stabilize dataset telemetry schema
* 23005e1 Add minimal fake-engine smoke tests
* 4d9fa47 Add reproducible run layout
* 54901b8 Add environment dependency checks
* 8ff2134 Fix Python 3.8 compatibility in controller registry
* 40566b0 Add config-driven client runner
```

Controllers registrados en `core/controller/registry.py`:

| Key | Label | Factory |
|---|---|---|
| `min_rate` | Min rate (sanity/control) | `MinRateController` |
| `fixed_rate` | Fixed rate or level (sanity/control) | `FixedRateController` |
| `max_rate` | Max rate (sanity/control) | `MaxRateController` |
| `rate_based` | Rate-based throughput baseline | `RateBasedController` |
| `bba` | BBA buffer-based baseline | `BbaController` |
| `bola` | BOLA-basic utility/buffer baseline | `BolaController` |
| `mpc` | MPC hybrid planning baseline | `MpcController` |
| `robust_mpc` | RobustMPC conservative planning baseline | `RobustMpcController` |
| `neural_abr_lite_robust_mpc` | NeuralABR-Lite guarded controller (robust_mpc teacher) | `NeuralAbrLiteRobustMpcController` |
| `neural_abr_lite_teacher_hibrido` | NeuralABR-Lite guarded controller (teacher_hibrido) | `NeuralAbrLiteTeacherHibridoController` |
| `spbc_abr_v2_dpo_anchor_safe_rank` | SPBC ABR v2 DPO guarded controller (anchor safe-rank) | `SpbcAbrV2DpoAnchorSafeRankController` |
| `phase45_v3_neural_throughput_calibrated_mpc_v1` | Phase45 v3 Neural Throughput-Calibrated MPC | `Phase45V3NeuralMpcController` |
| `phase45_v3_neural_throughput_calibrated_mpc_v2` | Phase45 v3 Neural Throughput-Calibrated MPC v2 | `Phase45V3NeuralMpcV2Controller` |
| `fixed_quality` | Fixed quality (test/debug) | `FixedQualityController` |
| `scripted_quality` | Scripted quality (test/debug) | `ScriptedQualityController` |
| `max_quality` | Max quality (legacy/debug/stress) | `MaxQualityController` |

Interpretacion de registry:

- Sanity/control: `min_rate`, `fixed_rate`, `max_rate`, `fixed_quality`, `scripted_quality`, `max_quality`.
- Baselines academicos clasicos: `rate_based`, `bba`, `bola`, `mpc`, `robust_mpc`.
- IA historica Phase 4/5: `neural_abr_lite_robust_mpc`, `neural_abr_lite_teacher_hibrido`.
- IA experimental SPBC v2: `spbc_abr_v2_dpo_anchor_safe_rank`.
- IA viva Neural-MPC: `phase45_v3_neural_throughput_calibrated_mpc_v1` y `phase45_v3_neural_throughput_calibrated_mpc_v2`.

## Modelo de trabajo Codex-Daniel

Contrato operativo permanente:

```text
Codex prepara, implementa, valida rapido, commitea/pushea cuando cierre cambios.
Daniel ejecuta en Ubuntu cliente o WSL2 los entrenamientos/evaluaciones largos.
Daniel pega resultados, logs o resumenes.
Se discute el resultado y se decide el siguiente paso documentado.
```

Responsabilidades:

| Actor/entorno | Responsabilidad | No debe hacer |
|---|---|---|
| Codex en Windows | Desarrollo, scripts, docs, tests, commits, push, runbooks cortos | Pedir bloques largos manuales, improvisar ciencia sin spec |
| Daniel en Ubuntu cliente | `git pull`, lanzar validaciones Phase 6, devolver resultados | Editar codigo manualmente como flujo normal |
| Daniel en WSL2 ROCm | Lanzar entrenamientos IA pesados con scripts versionados | Usar `/mnt/c/...` como raiz principal de entrenamiento |
| Ubuntu servidor | Servir MPD, segmentos e inicializaciones DASH por HTTP | Definir la red experimental o el benchmark |

Forma de dar comandos a Daniel:

- Comandos cortos.
- Preferencia por `git pull` y `bash scripts/<script>.sh`.
- Sin heredocs largos, bucles extensos ni listas de flags manuales.
- Si una ejecucion larga se repite, se versiona un script en `scripts/`.
- Windows y Ubuntu cliente se conectan por GitHub, no copiando codigo a mano.

Cierre normal de un bloque en Windows:

```powershell
git status --short --branch
git diff --check
python -m unittest discover
python scripts/check_client_readiness.py --strict
git add <rutas explicitas>
git commit -m "mensaje claro"
git push
```

Sin embargo, artefactos pesados o generados no se commitean: datasets, trazas normalizadas, manifests finales generados, runs, logs, modelos, bundles, zips, PDFs, videos, segmentos DASH y paquetes de evidencia.

## Arquitectura de entornos

La arquitectura operativa no trata el proyecto como una unica maquina. Hay cuatro entornos con responsabilidades separadas.

| Entorno | Ruta/estado | Papel |
|---|---|---|
| Windows fisico | `C:\Users\danie\Documents\TFG\DashClientModular4` | Desarrollo, tests rapidos, docs, commits, push |
| WSL2 Ubuntu ROCm | `~/TFG/DashClientModular4`, venv `~/venvs/rocm721` | Entrenamiento IA pesado y generacion de artefactos externos |
| Ubuntu cliente | `~/TFG/DashClientModular4` | Validacion real, Phase 6, paquetes de evidencia |
| Ubuntu servidor | `/var/www/html/dash` | Servir MPD/segmentos/inits por HTTP |

Estado WSL2/ROCm observado y documentado:

```text
Distribucion: Ubuntu-24.04 en WSL2
Ubuntu observado: Ubuntu 24.04.4 LTS
Venv GPU: ~/venvs/rocm721
Torch observado: 2.9.1+rocm7.2.1
GPU observada: AMD Radeon RX 7800 XT
torch.cuda.is_available(): True
```

Comprobacion WSL2 recomendada:

```bash
wsl -d Ubuntu-24.04
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate
python3 -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

Regla de rutas WSL2:

- Datasets, checkpoints, modelos, logs y runs de entrenamiento deben vivir bajo rutas Linux dentro de `~/TFG`.
- `/mnt/c/Users/danie/Documents/TFG/...` puede usarse para consultas puntuales, no como workspace principal de entrenamiento pesado.

Servidor DASH observado/documentado:

```text
Base Ubuntu servidor: /var/www/html/dash
URL ejemplo: http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd
Comprobacion aceptada: HTTP/1.1 200 OK
```

## Estructura del repositorio y carpetas hermanas

Top-level versionado detectado por `git ls-files`:

| Carpeta/archivo | Archivos versionados |
|---|---:|
| `.gitignore` | 1 |
| `AGENTS.md` | 1 |
| `README.md` | 1 |
| `analysis_metrics.py` | 1 |
| `config` | 3 |
| `core` | 129 |
| `docs` | 763 |
| `main.py` | 1 |
| `player.py` | 1 |
| `progress_bar.py` | 1 |
| `requirements-analysis.txt` | 1 |
| `requirements.txt` | 1 |
| `scripts` | 102 |
| `tests` | 75 |

Carpetas principales del repo:

| Ruta | Papel tecnico |
|---|---|
| `core/` | Codigo de cliente, controllers, trace replay, QoE, Phase 6 y entrenamiento IA |
| `scripts/` | Runbooks ejecutables, generadores, entrenadores, validadores, empaquetadores |
| `tests/` | Tests unitarios/estructurales/contratos |
| `docs/` | Contexto cientifico, decisiones, source cards, runbooks, cierres y memoria |
| `config/` | Configs ejemplo de cliente y Phase 6 |
| `output/pdf/` | PDFs generados localmente; no se deben commitear |

Carpetas hermanas externas detectadas bajo la raiz TFG:

| Nombre | Directorios | Archivos | Ultima modificacion |
|---|---:|---:|---|
| `20260608_160906_rapido` | 148 | 592 | `2026-06-08T18:38:36` |
| `20260608_193615_equilibrado` | 168 | 645 | `2026-06-09T06:58:36` |
| `20260611_193501_diagnostico` | 20 | 80 | `2026-06-11T19:49:00` |
| `20260611_202406_rapido` | 48 | 192 | `2026-06-11T21:09:57` |
| `20260615_110912_diagnostico` | 32 | 128 | `2026-06-15T11:17:59` |
| `20260615_112752_rapido` | 88 | 352 | `2026-06-15T13:03:19` |
| `20260615_141628_diagnostico` | 20 | 80 | `2026-06-15T14:27:33` |
| `abr ia pdf` | 1 | 32 | `2026-06-09T12:39:49` |
| `auditorias_trazas` | 3 | 35 | `2026-06-09T12:58:07` |
| `DashClientModular4` | 85 | 1092 | `2026-06-15T15:55:23` |
| `dataset en bruto` | 105 | 1309 | `2026-06-04T17:51:29` |
| `datasets_normalizados` | 26 | 7007 | `2026-06-08T11:48:35` |
| `manifests_trazas` | 36 | 8028 | `2026-06-08T11:48:49` |
| `modelos` | 5 | 30 | `2026-06-08T11:48:23` |
| `runs_trazas` | 45 | 89 | `2026-06-08T14:34:13` |

Rutas externas canonicas activas:

```text
C:\Users\danie\Documents\TFG\dataset en bruto
C:\Users\danie\Documents\TFG\datasets_normalizados
C:\Users\danie\Documents\TFG\manifests_trazas
C:\Users\danie\Documents\TFG\runs_trazas
C:\Users\danie\Documents\TFG\auditorias_trazas
C:\Users\danie\Documents\TFG\modelos
```

Artefactos externos relevantes fijados por instrucciones:

```text
C:\Users\danie\Documents\TFG\manifests_trazas\phase3\final\phase3_trace_manifest_curated.json
C:\Users\danie\Documents\TFG\runs_trazas\phase3_5\smoke
```

Archivos externos clave encontrados por nombre/patron:

| Ruta relativa a TFG | Tamano bytes | Ultima modificacion |
|---|---:|---|
| `20260608_160906_rapido\00_protocolo\client_configs\s00001_base_rate_based_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1.yaml` | 1451 | `2026-06-08T16:09:06` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00002_base_bba_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1.yaml` | 1437 | `2026-06-08T16:11:09` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00003_base_bola_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1.yaml` | 1439 | `2026-06-08T16:13:13` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00004_base_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1.yaml` | 1437 | `2026-06-08T16:15:17` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00005_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1.yaml` | 1451 | `2026-06-08T16:17:20` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00006_propio_rmp_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1.yaml` | 1712 | `2026-06-08T16:19:24` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00007_propio_th_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1.yaml` | 1732 | `2026-06-08T16:21:43` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00008_base_rate_based_paseo_10min_30fps_4s_real_002_3c716a0f31_r1.yaml` | 1453 | `2026-06-08T16:23:49` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00009_base_bba_paseo_10min_30fps_4s_real_002_3c716a0f31_r1.yaml` | 1439 | `2026-06-08T16:25:51` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00010_base_bola_paseo_10min_30fps_4s_real_002_3c716a0f31_r1.yaml` | 1441 | `2026-06-08T16:27:53` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00011_base_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1.yaml` | 1439 | `2026-06-08T16:29:56` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00012_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1.yaml` | 1453 | `2026-06-08T16:31:58` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00013_propio_rmp_paseo_10min_30fps_4s_real_002_3c716a0f31_r1.yaml` | 1714 | `2026-06-08T16:34:00` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00014_propio_th_paseo_10min_30fps_4s_real_002_3c716a0f31_r1.yaml` | 1734 | `2026-06-08T16:36:03` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00015_base_rate_based_paseo_10min_30fps_4s_real_003_9da918eb99_r1.yaml` | 1454 | `2026-06-08T16:38:05` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00016_base_bba_paseo_10min_30fps_4s_real_003_9da918eb99_r1.yaml` | 1440 | `2026-06-08T16:40:07` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00017_base_bola_paseo_10min_30fps_4s_real_003_9da918eb99_r1.yaml` | 1442 | `2026-06-08T16:42:10` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00018_base_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1.yaml` | 1440 | `2026-06-08T16:44:12` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00019_base_robust_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1.yaml` | 1454 | `2026-06-08T16:46:14` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00020_propio_rmp_paseo_10min_30fps_4s_real_003_9da918eb99_r1.yaml` | 1715 | `2026-06-08T16:48:17` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00021_propio_th_paseo_10min_30fps_4s_real_003_9da918eb99_r1.yaml` | 1735 | `2026-06-08T16:50:19` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00022_base_rate_based_paseo_10min_30fps_4s_real_004_8a94b2b843_r1.yaml` | 1453 | `2026-06-08T16:52:21` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00023_base_bba_paseo_10min_30fps_4s_real_004_8a94b2b843_r1.yaml` | 1439 | `2026-06-08T16:54:25` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00024_base_bola_paseo_10min_30fps_4s_real_004_8a94b2b843_r1.yaml` | 1441 | `2026-06-08T16:56:28` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00025_base_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1.yaml` | 1439 | `2026-06-08T16:58:31` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00026_base_robust_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1.yaml` | 1453 | `2026-06-08T17:00:34` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00027_propio_rmp_paseo_10min_30fps_4s_real_004_8a94b2b843_r1.yaml` | 1714 | `2026-06-08T17:02:37` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00028_propio_th_paseo_10min_30fps_4s_real_004_8a94b2b843_r1.yaml` | 1734 | `2026-06-08T17:04:50` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00029_base_rate_based_paseo_10min_30fps_4s_real_005_00d8be5b10_r1.yaml` | 1453 | `2026-06-08T17:06:54` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00030_base_bba_paseo_10min_30fps_4s_real_005_00d8be5b10_r1.yaml` | 1439 | `2026-06-08T17:08:56` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00031_base_bola_paseo_10min_30fps_4s_real_005_00d8be5b10_r1.yaml` | 1441 | `2026-06-08T17:10:59` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00032_base_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1.yaml` | 1439 | `2026-06-08T17:13:01` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00033_base_robust_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1.yaml` | 1453 | `2026-06-08T17:15:15` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00034_propio_rmp_paseo_10min_30fps_4s_real_005_00d8be5b10_r1.yaml` | 1714 | `2026-06-08T17:17:24` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00035_propio_th_paseo_10min_30fps_4s_real_005_00d8be5b10_r1.yaml` | 1734 | `2026-06-08T17:19:33` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00036_base_rate_based_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1.yaml` | 1451 | `2026-06-08T17:21:47` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00037_base_bba_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1.yaml` | 1437 | `2026-06-08T17:23:50` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00038_base_bola_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1.yaml` | 1439 | `2026-06-08T17:26:00` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00039_base_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1.yaml` | 1437 | `2026-06-08T17:28:23` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00040_base_robust_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1.yaml` | 1451 | `2026-06-08T17:30:54` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00041_propio_rmp_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1.yaml` | 1712 | `2026-06-08T17:33:02` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00042_propio_th_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1.yaml` | 1732 | `2026-06-08T17:35:33` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00043_base_rate_based_paseo_10min_30fps_4s_real_007_8775c96d2f_r1.yaml` | 1454 | `2026-06-08T17:38:07` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00044_base_bba_paseo_10min_30fps_4s_real_007_8775c96d2f_r1.yaml` | 1440 | `2026-06-08T17:40:09` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00045_base_bola_paseo_10min_30fps_4s_real_007_8775c96d2f_r1.yaml` | 1442 | `2026-06-08T17:42:12` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00046_base_mpc_paseo_10min_30fps_4s_real_007_8775c96d2f_r1.yaml` | 1440 | `2026-06-08T17:44:14` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00047_base_robust_mpc_paseo_10min_30fps_4s_real_007_8775c96d2f_r1.yaml` | 1454 | `2026-06-08T17:46:16` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00048_propio_rmp_paseo_10min_30fps_4s_real_007_8775c96d2f_r1.yaml` | 1715 | `2026-06-08T17:48:18` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00049_propio_th_paseo_10min_30fps_4s_real_007_8775c96d2f_r1.yaml` | 1735 | `2026-06-08T17:50:20` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00050_base_rate_based_paseo_10min_30fps_4s_real_008_52feb47a90_r1.yaml` | 1405 | `2026-06-08T17:52:23` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00051_base_bba_paseo_10min_30fps_4s_real_008_52feb47a90_r1.yaml` | 1391 | `2026-06-08T17:54:25` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00052_base_bola_paseo_10min_30fps_4s_real_008_52feb47a90_r1.yaml` | 1393 | `2026-06-08T17:56:27` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00053_base_mpc_paseo_10min_30fps_4s_real_008_52feb47a90_r1.yaml` | 1391 | `2026-06-08T17:58:29` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00054_base_robust_mpc_paseo_10min_30fps_4s_real_008_52feb47a90_r1.yaml` | 1405 | `2026-06-08T18:00:31` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00055_propio_rmp_paseo_10min_30fps_4s_real_008_52feb47a90_r1.yaml` | 1666 | `2026-06-08T18:02:33` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00056_propio_th_paseo_10min_30fps_4s_real_008_52feb47a90_r1.yaml` | 1686 | `2026-06-08T18:04:36` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00057_base_rate_based_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1.yaml` | 1485 | `2026-06-08T18:06:38` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00058_base_bba_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1.yaml` | 1471 | `2026-06-08T18:08:43` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00059_base_bola_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1.yaml` | 1473 | `2026-06-08T18:10:47` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00060_base_mpc_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1.yaml` | 1471 | `2026-06-08T18:13:32` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00061_base_robust_mpc_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1.yaml` | 1485 | `2026-06-08T18:15:37` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00062_propio_rmp_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1.yaml` | 1746 | `2026-06-08T18:17:42` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00063_propio_th_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1.yaml` | 1766 | `2026-06-08T18:20:24` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00064_base_rate_based_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1.yaml` | 1500 | `2026-06-08T18:22:33` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00065_base_bba_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1.yaml` | 1486 | `2026-06-08T18:24:35` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00066_base_bola_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1.yaml` | 1488 | `2026-06-08T18:26:38` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00067_base_mpc_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1.yaml` | 1486 | `2026-06-08T18:28:40` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00068_base_robust_mpc_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1.yaml` | 1500 | `2026-06-08T18:30:43` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00069_propio_rmp_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1.yaml` | 1761 | `2026-06-08T18:32:45` |
| `20260608_160906_rapido\00_protocolo\client_configs\s00070_propio_th_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1.yaml` | 1781 | `2026-06-08T18:34:47` |
| `20260608_160906_rapido\00_protocolo\controllers.csv` | 273 | `2026-06-08T16:09:06` |
| `20260608_160906_rapido\00_protocolo\media_profiles.csv` | 258 | `2026-06-08T16:09:06` |
| `20260608_160906_rapido\00_protocolo\protocolo_validacion.json` | 11495 | `2026-06-08T16:09:06` |
| `20260608_160906_rapido\00_protocolo\session_plan.csv` | 84760 | `2026-06-08T16:09:06` |
| `20260608_160906_rapido\00_protocolo\session_plan.json` | 133438 | `2026-06-08T16:09:06` |
| `20260608_160906_rapido\00_protocolo\trace_windows.csv` | 5268 | `2026-06-08T16:09:06` |
| `20260608_160906_rapido\01_ejecucion\runs\s00001_base_rate_based_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_160907\config.resolved.json` | 1511 | `2026-06-08T16:09:07` |
| `20260608_160906_rapido\01_ejecucion\runs\s00001_base_rate_based_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_160907\environment.json` | 1298 | `2026-06-08T16:09:07` |
| `20260608_160906_rapido\01_ejecucion\runs\s00001_base_rate_based_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_160907\evaluation_segments.csv` | 1628 | `2026-06-08T16:10:34` |
| `20260608_160906_rapido\01_ejecucion\runs\s00001_base_rate_based_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_160907\run_manifest.json` | 3098 | `2026-06-08T16:11:09` |
| `20260608_160906_rapido\01_ejecucion\runs\s00001_base_rate_based_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_160907\segment_telemetry.csv` | 16118 | `2026-06-08T16:11:09` |
| `20260608_160906_rapido\01_ejecucion\runs\s00002_base_bba_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161110\config.resolved.json` | 1497 | `2026-06-08T16:11:10` |
| `20260608_160906_rapido\01_ejecucion\runs\s00002_base_bba_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161110\environment.json` | 1298 | `2026-06-08T16:11:10` |
| `20260608_160906_rapido\01_ejecucion\runs\s00002_base_bba_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161110\evaluation_segments.csv` | 1614 | `2026-06-08T16:13:04` |
| `20260608_160906_rapido\01_ejecucion\runs\s00002_base_bba_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161110\run_manifest.json` | 3063 | `2026-06-08T16:13:13` |
| `20260608_160906_rapido\01_ejecucion\runs\s00002_base_bba_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161110\segment_telemetry.csv` | 16018 | `2026-06-08T16:13:13` |
| `20260608_160906_rapido\01_ejecucion\runs\s00003_base_bola_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161314\config.resolved.json` | 1499 | `2026-06-08T16:13:14` |
| `20260608_160906_rapido\01_ejecucion\runs\s00003_base_bola_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161314\environment.json` | 1298 | `2026-06-08T16:13:14` |
| `20260608_160906_rapido\01_ejecucion\runs\s00003_base_bola_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161314\evaluation_segments.csv` | 1623 | `2026-06-08T16:14:58` |
| `20260608_160906_rapido\01_ejecucion\runs\s00003_base_bola_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161314\run_manifest.json` | 3068 | `2026-06-08T16:15:16` |
| `20260608_160906_rapido\01_ejecucion\runs\s00003_base_bola_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161314\segment_telemetry.csv` | 15999 | `2026-06-08T16:15:16` |
| `20260608_160906_rapido\01_ejecucion\runs\s00004_base_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161517\config.resolved.json` | 1497 | `2026-06-08T16:15:17` |
| `20260608_160906_rapido\01_ejecucion\runs\s00004_base_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161517\environment.json` | 1298 | `2026-06-08T16:15:17` |
| `20260608_160906_rapido\01_ejecucion\runs\s00004_base_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161517\evaluation_segments.csv` | 1620 | `2026-06-08T16:17:13` |
| `20260608_160906_rapido\01_ejecucion\runs\s00004_base_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161517\run_manifest.json` | 3063 | `2026-06-08T16:17:20` |
| `20260608_160906_rapido\01_ejecucion\runs\s00004_base_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161517\segment_telemetry.csv` | 15949 | `2026-06-08T16:17:20` |
| `20260608_160906_rapido\01_ejecucion\runs\s00005_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161721\config.resolved.json` | 1511 | `2026-06-08T16:17:21` |
| `20260608_160906_rapido\01_ejecucion\runs\s00005_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161721\environment.json` | 1298 | `2026-06-08T16:17:21` |
| `20260608_160906_rapido\01_ejecucion\runs\s00005_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161721\evaluation_segments.csv` | 1618 | `2026-06-08T16:19:14` |
| `20260608_160906_rapido\01_ejecucion\runs\s00005_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161721\run_manifest.json` | 3098 | `2026-06-08T16:19:23` |
| `20260608_160906_rapido\01_ejecucion\runs\s00005_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161721\segment_telemetry.csv` | 16096 | `2026-06-08T16:19:23` |
| `20260608_160906_rapido\01_ejecucion\runs\s00006_propio_rmp_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161924\config.resolved.json` | 1768 | `2026-06-08T16:19:24` |
| `20260608_160906_rapido\01_ejecucion\runs\s00006_propio_rmp_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161924\environment.json` | 1298 | `2026-06-08T16:19:24` |
| `20260608_160906_rapido\01_ejecucion\runs\s00006_propio_rmp_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161924\evaluation_segments.csv` | 1625 | `2026-06-08T16:21:36` |
| `20260608_160906_rapido\01_ejecucion\runs\s00006_propio_rmp_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161924\run_manifest.json` | 3340 | `2026-06-08T16:21:43` |
| `20260608_160906_rapido\01_ejecucion\runs\s00006_propio_rmp_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161924\segment_telemetry.csv` | 23881 | `2026-06-08T16:21:43` |
| `20260608_160906_rapido\01_ejecucion\runs\s00007_propio_th_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_162144\config.resolved.json` | 1788 | `2026-06-08T16:21:44` |
| `20260608_160906_rapido\01_ejecucion\runs\s00007_propio_th_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_162144\environment.json` | 1298 | `2026-06-08T16:21:44` |
| `20260608_160906_rapido\01_ejecucion\runs\s00007_propio_th_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_162144\evaluation_segments.csv` | 1618 | `2026-06-08T16:23:42` |
| `20260608_160906_rapido\01_ejecucion\runs\s00007_propio_th_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_162144\run_manifest.json` | 3357 | `2026-06-08T16:23:49` |
| `20260608_160906_rapido\01_ejecucion\runs\s00007_propio_th_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_162144\segment_telemetry.csv` | 24725 | `2026-06-08T16:23:49` |
| `20260608_160906_rapido\01_ejecucion\runs\s00008_base_rate_based_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162350\config.resolved.json` | 1513 | `2026-06-08T16:23:50` |
| `20260608_160906_rapido\01_ejecucion\runs\s00008_base_rate_based_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162350\environment.json` | 1298 | `2026-06-08T16:23:50` |
| `20260608_160906_rapido\01_ejecucion\runs\s00008_base_rate_based_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162350\evaluation_segments.csv` | 1662 | `2026-06-08T16:24:49` |
| `20260608_160906_rapido\01_ejecucion\runs\s00008_base_rate_based_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162350\run_manifest.json` | 3100 | `2026-06-08T16:25:51` |
| `20260608_160906_rapido\01_ejecucion\runs\s00008_base_rate_based_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162350\segment_telemetry.csv` | 16227 | `2026-06-08T16:25:51` |
| `20260608_160906_rapido\01_ejecucion\runs\s00009_base_bba_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162552\config.resolved.json` | 1499 | `2026-06-08T16:25:52` |
| `20260608_160906_rapido\01_ejecucion\runs\s00009_base_bba_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162552\environment.json` | 1298 | `2026-06-08T16:25:52` |
| `20260608_160906_rapido\01_ejecucion\runs\s00009_base_bba_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162552\evaluation_segments.csv` | 1663 | `2026-06-08T16:26:51` |
| `20260608_160906_rapido\01_ejecucion\runs\s00009_base_bba_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162552\run_manifest.json` | 3065 | `2026-06-08T16:27:53` |
| `20260608_160906_rapido\01_ejecucion\runs\s00009_base_bba_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162552\segment_telemetry.csv` | 16013 | `2026-06-08T16:27:53` |
| `20260608_160906_rapido\01_ejecucion\runs\s00010_base_bola_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162754\config.resolved.json` | 1501 | `2026-06-08T16:27:54` |
| `20260608_160906_rapido\01_ejecucion\runs\s00010_base_bola_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162754\environment.json` | 1298 | `2026-06-08T16:27:54` |
| `20260608_160906_rapido\01_ejecucion\runs\s00010_base_bola_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162754\evaluation_segments.csv` | 1660 | `2026-06-08T16:28:54` |
| `20260608_160906_rapido\01_ejecucion\runs\s00010_base_bola_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162754\run_manifest.json` | 3070 | `2026-06-08T16:29:56` |
| `20260608_160906_rapido\01_ejecucion\runs\s00010_base_bola_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162754\segment_telemetry.csv` | 16028 | `2026-06-08T16:29:56` |
| `20260608_160906_rapido\01_ejecucion\runs\s00011_base_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162956\config.resolved.json` | 1499 | `2026-06-08T16:29:56` |
| `20260608_160906_rapido\01_ejecucion\runs\s00011_base_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162956\environment.json` | 1298 | `2026-06-08T16:29:56` |
| `20260608_160906_rapido\01_ejecucion\runs\s00011_base_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162956\evaluation_segments.csv` | 1663 | `2026-06-08T16:30:56` |
| `20260608_160906_rapido\01_ejecucion\runs\s00011_base_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162956\run_manifest.json` | 3065 | `2026-06-08T16:31:58` |
| `20260608_160906_rapido\01_ejecucion\runs\s00011_base_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162956\segment_telemetry.csv` | 16063 | `2026-06-08T16:31:58` |
| `20260608_160906_rapido\01_ejecucion\runs\s00012_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163159\config.resolved.json` | 1513 | `2026-06-08T16:31:59` |
| `20260608_160906_rapido\01_ejecucion\runs\s00012_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163159\environment.json` | 1298 | `2026-06-08T16:31:59` |
| `20260608_160906_rapido\01_ejecucion\runs\s00012_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163159\evaluation_segments.csv` | 1664 | `2026-06-08T16:32:58` |
| `20260608_160906_rapido\01_ejecucion\runs\s00012_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163159\run_manifest.json` | 3100 | `2026-06-08T16:34:00` |
| `20260608_160906_rapido\01_ejecucion\runs\s00012_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163159\segment_telemetry.csv` | 16277 | `2026-06-08T16:34:00` |
| `20260608_160906_rapido\01_ejecucion\runs\s00013_propio_rmp_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163401\config.resolved.json` | 1770 | `2026-06-08T16:34:01` |
| `20260608_160906_rapido\01_ejecucion\runs\s00013_propio_rmp_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163401\environment.json` | 1298 | `2026-06-08T16:34:01` |
| `20260608_160906_rapido\01_ejecucion\runs\s00013_propio_rmp_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163401\evaluation_segments.csv` | 1662 | `2026-06-08T16:35:00` |
| `20260608_160906_rapido\01_ejecucion\runs\s00013_propio_rmp_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163401\run_manifest.json` | 3342 | `2026-06-08T16:36:02` |
| `20260608_160906_rapido\01_ejecucion\runs\s00013_propio_rmp_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163401\segment_telemetry.csv` | 23924 | `2026-06-08T16:36:02` |
| `20260608_160906_rapido\01_ejecucion\runs\s00014_propio_th_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163603\config.resolved.json` | 1790 | `2026-06-08T16:36:03` |
| `20260608_160906_rapido\01_ejecucion\runs\s00014_propio_th_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163603\environment.json` | 1298 | `2026-06-08T16:36:03` |
| `20260608_160906_rapido\01_ejecucion\runs\s00014_propio_th_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163603\evaluation_segments.csv` | 1649 | `2026-06-08T16:37:02` |
| `20260608_160906_rapido\01_ejecucion\runs\s00014_propio_th_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163603\run_manifest.json` | 3359 | `2026-06-08T16:38:05` |
| `20260608_160906_rapido\01_ejecucion\runs\s00014_propio_th_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163603\segment_telemetry.csv` | 24897 | `2026-06-08T16:38:05` |
| `20260608_160906_rapido\01_ejecucion\runs\s00015_base_rate_based_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_163806\config.resolved.json` | 1514 | `2026-06-08T16:38:06` |
| `20260608_160906_rapido\01_ejecucion\runs\s00015_base_rate_based_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_163806\environment.json` | 1298 | `2026-06-08T16:38:06` |
| `20260608_160906_rapido\01_ejecucion\runs\s00015_base_rate_based_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_163806\evaluation_segments.csv` | 1661 | `2026-06-08T16:39:05` |
| `20260608_160906_rapido\01_ejecucion\runs\s00015_base_rate_based_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_163806\run_manifest.json` | 3101 | `2026-06-08T16:40:07` |
| `20260608_160906_rapido\01_ejecucion\runs\s00015_base_rate_based_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_163806\segment_telemetry.csv` | 16284 | `2026-06-08T16:40:07` |
| `20260608_160906_rapido\01_ejecucion\runs\s00016_base_bba_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164008\config.resolved.json` | 1500 | `2026-06-08T16:40:08` |
| `20260608_160906_rapido\01_ejecucion\runs\s00016_base_bba_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164008\environment.json` | 1298 | `2026-06-08T16:40:08` |
| `20260608_160906_rapido\01_ejecucion\runs\s00016_base_bba_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164008\evaluation_segments.csv` | 1662 | `2026-06-08T16:41:07` |
| `20260608_160906_rapido\01_ejecucion\runs\s00016_base_bba_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164008\run_manifest.json` | 3066 | `2026-06-08T16:42:09` |
| `20260608_160906_rapido\01_ejecucion\runs\s00016_base_bba_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164008\segment_telemetry.csv` | 16071 | `2026-06-08T16:42:09` |
| `20260608_160906_rapido\01_ejecucion\runs\s00017_base_bola_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164210\config.resolved.json` | 1502 | `2026-06-08T16:42:10` |
| `20260608_160906_rapido\01_ejecucion\runs\s00017_base_bola_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164210\environment.json` | 1298 | `2026-06-08T16:42:10` |
| `20260608_160906_rapido\01_ejecucion\runs\s00017_base_bola_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164210\evaluation_segments.csv` | 1651 | `2026-06-08T16:43:09` |
| `20260608_160906_rapido\01_ejecucion\runs\s00017_base_bola_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164210\run_manifest.json` | 3071 | `2026-06-08T16:44:12` |
| `20260608_160906_rapido\01_ejecucion\runs\s00017_base_bola_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164210\segment_telemetry.csv` | 15901 | `2026-06-08T16:44:12` |
| `20260608_160906_rapido\01_ejecucion\runs\s00018_base_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164413\config.resolved.json` | 1500 | `2026-06-08T16:44:13` |
| `20260608_160906_rapido\01_ejecucion\runs\s00018_base_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164413\environment.json` | 1298 | `2026-06-08T16:44:13` |
| `20260608_160906_rapido\01_ejecucion\runs\s00018_base_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164413\evaluation_segments.csv` | 1662 | `2026-06-08T16:45:12` |
| `20260608_160906_rapido\01_ejecucion\runs\s00018_base_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164413\run_manifest.json` | 3066 | `2026-06-08T16:46:14` |
| `20260608_160906_rapido\01_ejecucion\runs\s00018_base_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164413\segment_telemetry.csv` | 16053 | `2026-06-08T16:46:14` |
| `20260608_160906_rapido\01_ejecucion\runs\s00019_base_robust_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164615\config.resolved.json` | 1514 | `2026-06-08T16:46:15` |
| `20260608_160906_rapido\01_ejecucion\runs\s00019_base_robust_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164615\environment.json` | 1298 | `2026-06-08T16:46:15` |
| `20260608_160906_rapido\01_ejecucion\runs\s00019_base_robust_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164615\evaluation_segments.csv` | 1663 | `2026-06-08T16:47:14` |
| `20260608_160906_rapido\01_ejecucion\runs\s00019_base_robust_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164615\run_manifest.json` | 3101 | `2026-06-08T16:48:16` |
| `20260608_160906_rapido\01_ejecucion\runs\s00019_base_robust_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164615\segment_telemetry.csv` | 16301 | `2026-06-08T16:48:16` |
| `20260608_160906_rapido\01_ejecucion\runs\s00020_propio_rmp_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164817\config.resolved.json` | 1771 | `2026-06-08T16:48:17` |
| `20260608_160906_rapido\01_ejecucion\runs\s00020_propio_rmp_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164817\environment.json` | 1298 | `2026-06-08T16:48:17` |
| `20260608_160906_rapido\01_ejecucion\runs\s00020_propio_rmp_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164817\evaluation_segments.csv` | 1663 | `2026-06-08T16:49:16` |
| `20260608_160906_rapido\01_ejecucion\runs\s00020_propio_rmp_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164817\run_manifest.json` | 3343 | `2026-06-08T16:50:19` |
| `20260608_160906_rapido\01_ejecucion\runs\s00020_propio_rmp_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164817\segment_telemetry.csv` | 23941 | `2026-06-08T16:50:19` |
| `20260608_160906_rapido\01_ejecucion\runs\s00021_propio_th_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_165020\config.resolved.json` | 1791 | `2026-06-08T16:50:20` |
| `20260608_160906_rapido\01_ejecucion\runs\s00021_propio_th_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_165020\environment.json` | 1298 | `2026-06-08T16:50:20` |
| `20260608_160906_rapido\01_ejecucion\runs\s00021_propio_th_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_165020\evaluation_segments.csv` | 1654 | `2026-06-08T16:51:18` |
| `20260608_160906_rapido\01_ejecucion\runs\s00021_propio_th_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_165020\run_manifest.json` | 3360 | `2026-06-08T16:52:21` |
| `20260608_160906_rapido\01_ejecucion\runs\s00021_propio_th_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_165020\segment_telemetry.csv` | 24907 | `2026-06-08T16:52:21` |
| `20260608_160906_rapido\01_ejecucion\runs\s00022_base_rate_based_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165222\config.resolved.json` | 1513 | `2026-06-08T16:52:22` |
| `20260608_160906_rapido\01_ejecucion\runs\s00022_base_rate_based_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165222\environment.json` | 1298 | `2026-06-08T16:52:22` |
| `20260608_160906_rapido\01_ejecucion\runs\s00022_base_rate_based_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165222\evaluation_segments.csv` | 1626 | `2026-06-08T16:53:34` |
| `20260608_160906_rapido\01_ejecucion\runs\s00022_base_rate_based_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165222\run_manifest.json` | 3100 | `2026-06-08T16:54:25` |
| `20260608_160906_rapido\01_ejecucion\runs\s00022_base_rate_based_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165222\segment_telemetry.csv` | 16066 | `2026-06-08T16:54:25` |
| `20260608_160906_rapido\01_ejecucion\runs\s00023_base_bba_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165425\config.resolved.json` | 1499 | `2026-06-08T16:54:25` |
| `20260608_160906_rapido\01_ejecucion\runs\s00023_base_bba_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165425\environment.json` | 1298 | `2026-06-08T16:54:25` |
| `20260608_160906_rapido\01_ejecucion\runs\s00023_base_bba_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165425\evaluation_segments.csv` | 1624 | `2026-06-08T16:56:18` |
| `20260608_160906_rapido\01_ejecucion\runs\s00023_base_bba_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165425\run_manifest.json` | 3065 | `2026-06-08T16:56:28` |
| `20260608_160906_rapido\01_ejecucion\runs\s00023_base_bba_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165425\segment_telemetry.csv` | 15875 | `2026-06-08T16:56:28` |
| `20260608_160906_rapido\01_ejecucion\runs\s00024_base_bola_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165629\config.resolved.json` | 1501 | `2026-06-08T16:56:29` |
| `20260608_160906_rapido\01_ejecucion\runs\s00024_base_bola_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165629\environment.json` | 1298 | `2026-06-08T16:56:29` |
| `20260608_160906_rapido\01_ejecucion\runs\s00024_base_bola_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165629\evaluation_segments.csv` | 1622 | `2026-06-08T16:58:08` |
| `20260608_160906_rapido\01_ejecucion\runs\s00024_base_bola_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165629\run_manifest.json` | 3070 | `2026-06-08T16:58:31` |
| `20260608_160906_rapido\01_ejecucion\runs\s00024_base_bola_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165629\segment_telemetry.csv` | 15928 | `2026-06-08T16:58:31` |
| `20260608_160906_rapido\01_ejecucion\runs\s00025_base_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165832\config.resolved.json` | 1499 | `2026-06-08T16:58:32` |
| `20260608_160906_rapido\01_ejecucion\runs\s00025_base_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165832\environment.json` | 1298 | `2026-06-08T16:58:32` |
| `20260608_160906_rapido\01_ejecucion\runs\s00025_base_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165832\evaluation_segments.csv` | 1623 | `2026-06-08T17:00:29` |
| `20260608_160906_rapido\01_ejecucion\runs\s00025_base_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165832\run_manifest.json` | 3065 | `2026-06-08T17:00:34` |
| `20260608_160906_rapido\01_ejecucion\runs\s00025_base_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165832\segment_telemetry.csv` | 15684 | `2026-06-08T17:00:34` |
| `20260608_160906_rapido\01_ejecucion\runs\s00026_base_robust_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170035\config.resolved.json` | 1513 | `2026-06-08T17:00:35` |
| `20260608_160906_rapido\01_ejecucion\runs\s00026_base_robust_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170035\environment.json` | 1298 | `2026-06-08T17:00:35` |
| `20260608_160906_rapido\01_ejecucion\runs\s00026_base_robust_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170035\evaluation_segments.csv` | 1627 | `2026-06-08T17:02:28` |
| `20260608_160906_rapido\01_ejecucion\runs\s00026_base_robust_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170035\run_manifest.json` | 3100 | `2026-06-08T17:02:37` |
| `20260608_160906_rapido\01_ejecucion\runs\s00026_base_robust_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170035\segment_telemetry.csv` | 15878 | `2026-06-08T17:02:37` |
| `20260608_160906_rapido\01_ejecucion\runs\s00027_propio_rmp_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170238\config.resolved.json` | 1770 | `2026-06-08T17:02:38` |
| `20260608_160906_rapido\01_ejecucion\runs\s00027_propio_rmp_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170238\environment.json` | 1298 | `2026-06-08T17:02:38` |
| `20260608_160906_rapido\01_ejecucion\runs\s00027_propio_rmp_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170238\evaluation_segments.csv` | 1623 | `2026-06-08T17:04:44` |
| `20260608_160906_rapido\01_ejecucion\runs\s00027_propio_rmp_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170238\run_manifest.json` | 3342 | `2026-06-08T17:04:50` |
| `20260608_160906_rapido\01_ejecucion\runs\s00027_propio_rmp_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170238\segment_telemetry.csv` | 23779 | `2026-06-08T17:04:50` |
| `20260608_160906_rapido\01_ejecucion\runs\s00028_propio_th_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170451\config.resolved.json` | 1790 | `2026-06-08T17:04:51` |
| `20260608_160906_rapido\01_ejecucion\runs\s00028_propio_th_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170451\environment.json` | 1298 | `2026-06-08T17:04:51` |
| `20260608_160906_rapido\01_ejecucion\runs\s00028_propio_th_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170451\evaluation_segments.csv` | 1623 | `2026-06-08T17:06:42` |
| `20260608_160906_rapido\01_ejecucion\runs\s00028_propio_th_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170451\run_manifest.json` | 3359 | `2026-06-08T17:06:54` |
| `20260608_160906_rapido\01_ejecucion\runs\s00028_propio_th_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170451\segment_telemetry.csv` | 24641 | `2026-06-08T17:06:54` |
| `20260608_160906_rapido\01_ejecucion\runs\s00029_base_rate_based_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_170654\config.resolved.json` | 1513 | `2026-06-08T17:06:54` |
| `20260608_160906_rapido\01_ejecucion\runs\s00029_base_rate_based_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_170654\environment.json` | 1298 | `2026-06-08T17:06:54` |
| `20260608_160906_rapido\01_ejecucion\runs\s00029_base_rate_based_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_170654\evaluation_segments.csv` | 1637 | `2026-06-08T17:08:15` |
| `20260608_160906_rapido\01_ejecucion\runs\s00029_base_rate_based_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_170654\run_manifest.json` | 3100 | `2026-06-08T17:08:56` |
| `20260608_160906_rapido\01_ejecucion\runs\s00029_base_rate_based_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_170654\segment_telemetry.csv` | 16196 | `2026-06-08T17:08:56` |
| `20260608_160906_rapido\01_ejecucion\runs\s00030_base_bba_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_170857\config.resolved.json` | 1499 | `2026-06-08T17:08:57` |
| `20260608_160906_rapido\01_ejecucion\runs\s00030_base_bba_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_170857\environment.json` | 1298 | `2026-06-08T17:08:57` |
| `20260608_160906_rapido\01_ejecucion\runs\s00030_base_bba_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_170857\evaluation_segments.csv` | 1641 | `2026-06-08T17:10:44` |
| `20260608_160906_rapido\01_ejecucion\runs\s00030_base_bba_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_170857\run_manifest.json` | 3065 | `2026-06-08T17:10:59` |
| `20260608_160906_rapido\01_ejecucion\runs\s00030_base_bba_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_170857\segment_telemetry.csv` | 15958 | `2026-06-08T17:10:59` |
| `20260608_160906_rapido\01_ejecucion\runs\s00031_base_bola_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171100\config.resolved.json` | 1501 | `2026-06-08T17:11:00` |
| `20260608_160906_rapido\01_ejecucion\runs\s00031_base_bola_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171100\environment.json` | 1298 | `2026-06-08T17:11:00` |
| `20260608_160906_rapido\01_ejecucion\runs\s00031_base_bola_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171100\evaluation_segments.csv` | 1640 | `2026-06-08T17:12:22` |
| `20260608_160906_rapido\01_ejecucion\runs\s00031_base_bola_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171100\run_manifest.json` | 3070 | `2026-06-08T17:13:01` |
| `20260608_160906_rapido\01_ejecucion\runs\s00031_base_bola_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171100\segment_telemetry.csv` | 15880 | `2026-06-08T17:13:01` |
| `20260608_160906_rapido\01_ejecucion\runs\s00032_base_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171302\config.resolved.json` | 1499 | `2026-06-08T17:13:02` |
| `20260608_160906_rapido\01_ejecucion\runs\s00032_base_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171302\environment.json` | 1298 | `2026-06-08T17:13:02` |
| `20260608_160906_rapido\01_ejecucion\runs\s00032_base_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171302\evaluation_segments.csv` | 1642 | `2026-06-08T17:15:00` |
| `20260608_160906_rapido\01_ejecucion\runs\s00032_base_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171302\run_manifest.json` | 3065 | `2026-06-08T17:15:14` |
| `20260608_160906_rapido\01_ejecucion\runs\s00032_base_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171302\segment_telemetry.csv` | 15972 | `2026-06-08T17:15:14` |
| `20260608_160906_rapido\01_ejecucion\runs\s00033_base_robust_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171515\config.resolved.json` | 1513 | `2026-06-08T17:15:15` |
| `20260608_160906_rapido\01_ejecucion\runs\s00033_base_robust_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171515\environment.json` | 1298 | `2026-06-08T17:15:15` |
| `20260608_160906_rapido\01_ejecucion\runs\s00033_base_robust_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171515\evaluation_segments.csv` | 1641 | `2026-06-08T17:17:07` |
| `20260608_160906_rapido\01_ejecucion\runs\s00033_base_robust_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171515\run_manifest.json` | 3100 | `2026-06-08T17:17:24` |
| `20260608_160906_rapido\01_ejecucion\runs\s00033_base_robust_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171515\segment_telemetry.csv` | 16222 | `2026-06-08T17:17:24` |
| `20260608_160906_rapido\01_ejecucion\runs\s00034_propio_rmp_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171725\config.resolved.json` | 1770 | `2026-06-08T17:17:25` |
| `20260608_160906_rapido\01_ejecucion\runs\s00034_propio_rmp_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171725\environment.json` | 1298 | `2026-06-08T17:17:25` |
| `20260608_160906_rapido\01_ejecucion\runs\s00034_propio_rmp_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171725\evaluation_segments.csv` | 1640 | `2026-06-08T17:19:17` |
| `20260608_160906_rapido\01_ejecucion\runs\s00034_propio_rmp_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171725\run_manifest.json` | 3342 | `2026-06-08T17:19:33` |
| `20260608_160906_rapido\01_ejecucion\runs\s00034_propio_rmp_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171725\segment_telemetry.csv` | 23826 | `2026-06-08T17:19:33` |
| `20260608_160906_rapido\01_ejecucion\runs\s00035_propio_th_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171934\config.resolved.json` | 1790 | `2026-06-08T17:19:34` |
| `20260608_160906_rapido\01_ejecucion\runs\s00035_propio_th_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171934\environment.json` | 1298 | `2026-06-08T17:19:34` |
| `20260608_160906_rapido\01_ejecucion\runs\s00035_propio_th_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171934\evaluation_segments.csv` | 1645 | `2026-06-08T17:21:32` |
| `20260608_160906_rapido\01_ejecucion\runs\s00035_propio_th_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171934\run_manifest.json` | 3359 | `2026-06-08T17:21:47` |
| `20260608_160906_rapido\01_ejecucion\runs\s00035_propio_th_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171934\segment_telemetry.csv` | 24849 | `2026-06-08T17:21:47` |
| `20260608_160906_rapido\01_ejecucion\runs\s00036_base_rate_based_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172148\config.resolved.json` | 1511 | `2026-06-08T17:21:48` |
| `20260608_160906_rapido\01_ejecucion\runs\s00036_base_rate_based_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172148\environment.json` | 1298 | `2026-06-08T17:21:48` |
| `20260608_160906_rapido\01_ejecucion\runs\s00036_base_rate_based_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172148\evaluation_segments.csv` | 1626 | `2026-06-08T17:23:18` |
| `20260608_160906_rapido\01_ejecucion\runs\s00036_base_rate_based_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172148\run_manifest.json` | 3098 | `2026-06-08T17:23:49` |
| `20260608_160906_rapido\01_ejecucion\runs\s00036_base_rate_based_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172148\segment_telemetry.csv` | 15965 | `2026-06-08T17:23:49` |
| `20260608_160906_rapido\01_ejecucion\runs\s00037_base_bba_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172350\config.resolved.json` | 1497 | `2026-06-08T17:23:50` |
| `20260608_160906_rapido\01_ejecucion\runs\s00037_base_bba_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172350\environment.json` | 1298 | `2026-06-08T17:23:50` |
| `20260608_160906_rapido\01_ejecucion\runs\s00037_base_bba_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172350\evaluation_segments.csv` | 1633 | `2026-06-08T17:25:54` |
| `20260608_160906_rapido\01_ejecucion\runs\s00037_base_bba_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172350\run_manifest.json` | 3063 | `2026-06-08T17:26:00` |
| `20260608_160906_rapido\01_ejecucion\runs\s00037_base_bba_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172350\segment_telemetry.csv` | 15744 | `2026-06-08T17:26:00` |
| `20260608_160906_rapido\01_ejecucion\runs\s00038_base_bola_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172601\config.resolved.json` | 1499 | `2026-06-08T17:26:01` |
| `20260608_160906_rapido\01_ejecucion\runs\s00038_base_bola_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172601\environment.json` | 1298 | `2026-06-08T17:26:01` |
| `20260608_160906_rapido\01_ejecucion\runs\s00038_base_bola_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172601\evaluation_segments.csv` | 1620 | `2026-06-08T17:28:19` |
| `20260608_160906_rapido\01_ejecucion\runs\s00038_base_bola_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172601\run_manifest.json` | 3068 | `2026-06-08T17:28:23` |
| `20260608_160906_rapido\01_ejecucion\runs\s00038_base_bola_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172601\segment_telemetry.csv` | 15946 | `2026-06-08T17:28:23` |
| `20260608_160906_rapido\01_ejecucion\runs\s00039_base_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172824\config.resolved.json` | 1497 | `2026-06-08T17:28:24` |
| `20260608_160906_rapido\01_ejecucion\runs\s00039_base_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172824\environment.json` | 1298 | `2026-06-08T17:28:24` |
| `20260608_160906_rapido\01_ejecucion\runs\s00039_base_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172824\evaluation_segments.csv` | 1627 | `2026-06-08T17:30:44` |
| `20260608_160906_rapido\01_ejecucion\runs\s00039_base_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172824\run_manifest.json` | 3063 | `2026-06-08T17:30:54` |
| `20260608_160906_rapido\01_ejecucion\runs\s00039_base_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172824\segment_telemetry.csv` | 15775 | `2026-06-08T17:30:54` |
| `20260608_160906_rapido\01_ejecucion\runs\s00040_base_robust_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173055\config.resolved.json` | 1511 | `2026-06-08T17:30:55` |
| `20260608_160906_rapido\01_ejecucion\runs\s00040_base_robust_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173055\environment.json` | 1298 | `2026-06-08T17:30:55` |
| `20260608_160906_rapido\01_ejecucion\runs\s00040_base_robust_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173055\evaluation_segments.csv` | 1626 | `2026-06-08T17:32:46` |
| `20260608_160906_rapido\01_ejecucion\runs\s00040_base_robust_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173055\run_manifest.json` | 3098 | `2026-06-08T17:33:02` |
| `20260608_160906_rapido\01_ejecucion\runs\s00040_base_robust_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173055\segment_telemetry.csv` | 15970 | `2026-06-08T17:33:02` |
| `20260608_160906_rapido\01_ejecucion\runs\s00041_propio_rmp_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173302\config.resolved.json` | 1768 | `2026-06-08T17:33:02` |
| `20260608_160906_rapido\01_ejecucion\runs\s00041_propio_rmp_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173302\environment.json` | 1298 | `2026-06-08T17:33:02` |
| `20260608_160906_rapido\01_ejecucion\runs\s00041_propio_rmp_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173302\evaluation_segments.csv` | 1624 | `2026-06-08T17:35:24` |
| `20260608_160906_rapido\01_ejecucion\runs\s00041_propio_rmp_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173302\run_manifest.json` | 3340 | `2026-06-08T17:35:33` |
| `20260608_160906_rapido\01_ejecucion\runs\s00041_propio_rmp_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173302\segment_telemetry.csv` | 23677 | `2026-06-08T17:35:33` |
| `20260608_160906_rapido\01_ejecucion\runs\s00042_propio_th_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173533\config.resolved.json` | 1788 | `2026-06-08T17:35:33` |
| `20260608_160906_rapido\01_ejecucion\runs\s00042_propio_th_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173533\environment.json` | 1298 | `2026-06-08T17:35:34` |
| `20260608_160906_rapido\01_ejecucion\runs\s00042_propio_th_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173533\evaluation_segments.csv` | 1628 | `2026-06-08T17:38:00` |
| `20260608_160906_rapido\01_ejecucion\runs\s00042_propio_th_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173533\run_manifest.json` | 3357 | `2026-06-08T17:38:07` |
| `20260608_160906_rapido\01_ejecucion\runs\s00042_propio_th_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173533\segment_telemetry.csv` | 24683 | `2026-06-08T17:38:07` |
| `20260608_160906_rapido\01_ejecucion\runs\s00043_base_rate_based_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_173808\config.resolved.json` | 1514 | `2026-06-08T17:38:08` |
| `20260608_160906_rapido\01_ejecucion\runs\s00043_base_rate_based_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_173808\environment.json` | 1298 | `2026-06-08T17:38:08` |
| `20260608_160906_rapido\01_ejecucion\runs\s00043_base_rate_based_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_173808\evaluation_segments.csv` | 1722 | `2026-06-08T17:39:05` |
| `20260608_160906_rapido\01_ejecucion\runs\s00043_base_rate_based_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_173808\run_manifest.json` | 3101 | `2026-06-08T17:40:09` |
| `20260608_160906_rapido\01_ejecucion\runs\s00043_base_rate_based_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_173808\segment_telemetry.csv` | 16416 | `2026-06-08T17:40:09` |
| `20260608_160906_rapido\01_ejecucion\runs\s00044_base_bba_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_174010\config.resolved.json` | 1500 | `2026-06-08T17:40:10` |
| `20260608_160906_rapido\01_ejecucion\runs\s00044_base_bba_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_174010\environment.json` | 1298 | `2026-06-08T17:40:10` |
| `20260608_160906_rapido\01_ejecucion\runs\s00044_base_bba_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_174010\evaluation_segments.csv` | 1721 | `2026-06-08T17:41:07` |
| `20260608_160906_rapido\01_ejecucion\runs\s00044_base_bba_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_174010\run_manifest.json` | 3066 | `2026-06-08T17:42:11` |
| `20260608_160906_rapido\01_ejecucion\runs\s00044_base_bba_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_174010\segment_telemetry.csv` | 16215 | `2026-06-08T17:42:11` |
| `20260608_160906_rapido\01_ejecucion\runs\s00045_base_bola_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_174212\config.resolved.json` | 1502 | `2026-06-08T17:42:12` |
| `20260608_160906_rapido\01_ejecucion\runs\s00045_base_bola_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_174212\environment.json` | 1298 | `2026-06-08T17:42:12` |
| `20260608_160906_rapido\01_ejecucion\runs\s00045_base_bola_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_174212\evaluation_segments.csv` | 1717 | `2026-06-08T17:43:10` |
| `20260608_160906_rapido\01_ejecucion\runs\s00045_base_bola_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_174212\run_manifest.json` | 3071 | `2026-06-08T17:44:14` |
| `(catalogo truncado en PDF/MD principal)` | 18032 | archivos clave adicionales omitidos de esta tabla |

Nota de no contaminacion: el inventario externo documenta existencia y rutas. No mueve ni copia artefactos al repo.

## Historia formal por fases

### Phase 1 - Client hardening

Estado: cerrada.

Objetivo: convertir el cliente DASH en una base tecnica estable, modular, reproducible y ABR-neutral.

Resultados cerrados:

- Config YAML y runner controlado.
- Layout reproducible de runs.
- Outputs canonicos: `run_manifest.json`, `config.resolved.json`, `environment.json`, `run.log`, `segment_telemetry.csv`, `evaluation_segments.csv`.
- Eliminacion de outputs legacy `dataset.csv` y `dataset_training.csv` como artefactos canonicos.
- Fake media engine como camino controlado.
- GStreamer como integracion/demo, no evidencia equivalente de benchmark.
- Controller contract y feedback runtime.
- Benchmark neutrality contract.
- Readiness gate con `scripts/check_client_readiness.py --strict`.

No significa: benchmark, ranking, QoE final, baselines academicos o IA.

### Phase 2 - Baselines ABR clasicos

Estado: cerrada.

Controllers implementados:

```text
min_rate
fixed_rate
max_rate
rate_based
bba
bola
mpc
robust_mpc
```

Proceso usado:

```text
paper/source -> paper_card/source_evidence -> implementation_spec -> controller_api_mapping -> acceptance_tests -> codigo -> tests -> docs
```

Papel de cada baseline:

- `rate_based`: seleccion por throughput medido y factor de seguridad.
- `bba`: decision por ocupacion de buffer con reservoir/cushion.
- `bola`: utilidad/buffer, BOLA-basic, sin DYNAMIC ni FAST SWITCHING.
- `mpc`: enumeracion de secuencias con prediccion de throughput y reward interno.
- `robust_mpc`: MPC conservador con error historico y fallback seguro.

No significa: comparacion formal, ganador ni QoE final.

### Phase 3 Rebuild - Trazas y replay

Estado: cerrada en Windows con corpus externo, auditoria de calidad, replay tecnico y manifest curado recomendado.

Unidad canonica:

```text
throughput_kbps
```

Schema normalizado:

```csv
timestamp_s,duration_s,throughput_kbps
```

Separacion obligatoria:

- Las muestras que ve el replay no contienen `trace_id`, `dataset_id`, `source_id`, `split`, `group_id`, `leakage_group`, etiqueta OOD ni futuro throughput como input del controller.
- Los splits `train`, `test` y `eval` se hacen por `leakage_group`/grupo semantico, no por filas.
- FCC, Puffer y GAViST quedan marcados por semantica para no tratarlos sin control como trazas directas de ancho de banda disponible.

Manifest curado activo:

```text
C:\Users\danie\Documents\TFG\manifests_trazas\phase3\final\phase3_trace_manifest_curated.json
```

### Addendum sintetico Phase 3

Contrato sintetico:

```text
dataset_id=synthetic_controlled_network
semantics=synthetic_available_bandwidth
generator_id=phase3_synthetic_controlled_network_v1
trace_count=6768
synthetic_trace_count=1024
synthetic_split_counts=train:720,test:152,eval:152
```

Regla: resultados sinteticos futuros se reportan separados de trazas reales y no autorizan generalizacion real-world.

### Phase 3.5 Rebuild - QoE, reward y gates

Estado: cerrada en Windows con contrato `qoe_linear_v1`, calculadora QoE pura, postprocesador QoE, gates y smokes sinteticos controlados.

Formula cerrada:

```text
qoe_formula_version=qoe_linear_v1
reward_n = bitrate_mbps - 4.3 * rebuffer_s - smoothness_mbps
primary_session_metric=qoe_linear_mean
```

Detalles:

- `qoe_log_v1` es metrica secundaria de sensibilidad.
- `startup_delay_s` es report-only.
- VMAF queda deferred/artifact-dependent.
- Gates validos: `use_for_eval`, `diagnostic_only`, `do_not_use_for_eval`.
- Smokes QoE son sinteticos y no consumen trazas reales.

Flags requeridos para smokes QoE:

```text
outputs_are_benchmark_results=false
benchmark_performed=false
ranking_performed=false
no_final_ranking=true
ia_training_performed=false
```

### Phase 4 Rebuild - NeuralABR-Lite offline

Estado: cerrada en Ubuntu con dos bundles offline `NeuralABR-Lite`: uno entrenado con `robust_mpc` real y otro con `teacher_hibrido`.

Metodo:

- Candidate scorer pequeno, CPU-first.
- Entrenamiento por imitation learning/behavior cloning.
- Salida como score por representacion candidata.
- Action mask, normalization train-only y contrato de bundle.
- Artefactos pesados fuera de Git.

No hay benchmark, ranking, ganador ni afirmacion autorizada de mejora QoE.

### Phase 5 - Integracion de IA historica

Estado: cerrada en Ubuntu con dos controllers IA integrados.

Controllers:

```text
neural_abr_lite_robust_mpc
neural_abr_lite_teacher_hibrido
```

Contrato de runtime:

- Carga de bundle local-only fuera del repo.
- Inferencia CPU.
- Verificacion de hashes cuando esta configurada.
- Action mask.
- Safety guard.
- Fallback a `robust_mpc`.
- Telemetria neural diagnostica en `segment_telemetry.csv`.
- `evaluation_segments.csv` queda limpio de columnas IA.

No significa que la IA gane, ni benchmark, ni ranking, ni mejora QoE.

### Fase de Verificacion del Cliente y Controllers Clasicos

Estado: cerrada en Ubuntu con informe externo aceptado.

Evidencia reportada:

```text
python scripts/check_client_readiness.py --strict -> 88 OK / 0 WARN / 0 FAIL
curl -I http://192.168.1.132/dash/.../Paseo_Almunecar_1min_30fps_simple_4s.mpd -> HTTP/1.1 200 OK
python scripts/verificar_cliente_y_controllers_clasicos.py --mpd-url ... -> Status: accepted
```

Demuestra funcionamiento estructural contra servidor DASH y ausencia de contaminacion en runs clasicos. No demuestra ranking ni mejora de ningun controller.

### Phase 6 - Validacion comparativa formal

Estado: pipeline reproducible implementado para ejecucion en Ubuntu cliente. La fase formal solo autoriza comparacion si pasan gates del paquete.

Objetivo:

- Congelar protocolo, controllers, MPDs/media profiles, trazas, QoE, seeds, gates y estadistica.
- Ejecutar sesiones trace-driven en Ubuntu cliente con engine `fake` para reproducibilidad.
- Generar paquete de evidencia externo con protocolo, ejecucion, resultados, graficas e informe.

Presets relevantes:

- `diagnostico`: 6 segmentos por sesion, verifica maquinaria completa, no ranking.
- `rapido`: amplia cobertura, sigue sin ser benchmark final ni ranking.
- `equilibrado`/`extendido`: solo autorizan ranking si pasan todos los gates y verificacion automatica.

## Desarrollo IA ABR actual

### Fase 4-5 v1 como iteracion nueva

Fase 4-5 v1 queda abierta como iteracion nueva e independiente. No sustituye a Phase 4 ni Phase 5 cerradas y no hereda automaticamente decisiones de `NeuralABR-Lite`.

Corpus canonico:

```text
docs/contexto rama nueva/fase_4_5_v1/abr ia md/
```

Proceso obligatorio:

```text
decision documentada
-> dataset pilot
-> auditoria dataset pilot
-> entrenamiento pilot 1 seed
-> resumen y analisis de errores
-> pilot multi-seed
-> diagnostico closed-loop offline
-> bundle experimental externo
-> smoke/runtime load
-> Phase 6 diagnostico en Ubuntu cliente
-> Phase 6 rapido si procede
-> iteracion controlada
-> full dataset/full training solo si la evidencia lo justifica
```

Criterios permanentes de no avance:

- No avanzar si `best_epoch=0` por fallback.
- No avanzar si pasa copiando referencia sin aprendizaje real.
- No avanzar si rompe gates anti-colapso.
- No avanzar si produce acciones invalidas.
- No avanzar si requiere relajar gates.
- No avanzar si usa artefactos fuera de rutas Linux en WSL.
- No avanzar si necesita comandos manuales largos no versionados.

### Decision inicial Fase 4-5 v1

Candidatos definidos el 2026-06-09:

| Candidato | Tipo | Estado |
|---|---|---|
| `spc_abr_v1` | Predictor neural de throughput/capacidad + planner ABR determinista risk-aware | Prioridad inicial |
| `spbc_abr_v1` | Policy neural con predictor auxiliar, behavior cloning desde `oracle_qoe_beam_v1` | Segundo candidato |
| `spbc_ppo_abr_v1` | Fine-tuning RL de `spbc_abr_v1` | Condicionado a gates |

Opciones descartadas como primer controller: DQN puro, A3C/Pensieve clonado, meta-RL completo, Mamba/SSM como dependencia inicial, energia, edge, multiusuario, live playback speed, short-video MARL y VMAF.

### SPBC historico y SPBC v2

Hecho documentado: el SPBC historico fracaso como controller runtime por desalineacion entre dinamica offline y dinamica del cliente final.

Sintomas de colapso reportados para SPBC v2 en Phase 6 rapido:

```text
controller=propio_spbc_v2_anchor
status=FAIL
collapse_detected=True
high_capacity_action0_rate=0.6623376623376623
max_consecutive_action0_after_startup=26
fallback_row_count=5
fallback_reasons={"inference_timeout": 5}
qoe_delta_vs_baseline_mean=-1.7679512342365435
mean_measured_throughput_kbps=100153.01954068724
median_selected_bitrate_kbps=300.0
```

Diagnostico factual asociado: entrenamiento antiguo con `max_buffer_s=20.0` frente a cliente/Phase 6 con `max_buffer_s=60.0`.

### Phase45 v3 Q_H scorer bloqueado

Linea: `phase45_v3_qh_scorer`.

Objetivo: scorer neural que recibe estado ABR visible por controller y candidatos de bitrate, y ordena acciones segun targets `Q_H(s,a)` generados en entorno cerrado.

Mejor intento documentado:

```text
run=qh_scorer_pilot_adv_regret_dataset_pilot_seed450924_v1
status=REVIEW
top1_accuracy=0.788844
mean_regret_q_h=0.395739
gate_mean_regret_q_h<=0.35 FAIL
high_capacity_predicted_action0_rate=0.002946 PASS
```

Intentos que no avanzaron el gate principal:

```text
pilot_adv_regret_v1 mean_regret_q_h=0.395739
pilot_adv_regret_gru_v1 mean_regret_q_h=0.442516
hardneg_v1 mean_regret_q_h=0.401737
hardneg_v2 mean_regret_q_h=0.417399
```

Lectura aceptada: no era solo un problema de loss. El target `Q_H(s,a)` usa futuro como target-only; estados visibles similares pueden tener targets distintos por futuro inmediato no observable. El scorer queda como experimento negativo, diagnostico y posible ablation, no como via principal.

### Linea viva - Neural Throughput-Calibrated MPC

Controller candidato:

```text
phase45_v3_neural_throughput_calibrated_mpc_v1
predictor neuronal de cuantiles de throughput futuro
+ planner MPC explicito sobre qoe_linear_v1
```

Contrato tecnico:

- La red no elige bitrate directamente.
- La red predice log-ratios de throughput futuro respecto a una base robusta.
- El planner MPC auditable elige accion.
- `future throughput` se usa solo como target de entrenamiento, nunca como input.
- `eval` queda excluido de entrenamiento.

Targets:

```text
base_tp = harmonic_mean(throughput_history_bps)
target_log_ratio_h = log((future_tp_h + eps) / (base_tp + eps))
horizon=5
quantiles=0.10,0.25,0.50,0.75
```

Loss:

```text
loss = pinball + crossing_penalty + temporal_smoothness_penalty
```

Regla de cuantiles por buffer:

```text
buffer < 4s         -> q10
4s <= buffer < 12s  -> q25
12s <= buffer <20s  -> blend(q25,q50)
buffer >=20s        -> q50
```

Reward usado por MPC:

```text
reward = bitrate_mbps - 4.3 * rebuffer_s - smoothness_mbps
```

Gates diagnosticos:

- `high_capacity_action0_rate <= 0.05`.
- `high_capacity_mean_bitrate_ratio_vs_robust_mpc >= 0.70`.
- `fallback_rate == 0`.
- `invalid_action_count == 0`.
- Rebuffer en bucket `2_5_mbps` no debe explotar frente a `robust_mpc`.
- QoE media no debe ser catastroficamente peor que `robust_mpc`.

Piloto inicial: tras calibracion de planner paso de `bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean=+1.3203728087318694 s` a `+0.08001783155587106 s`, con `status=PASS` en 32 sesiones/8 ventanas.

Diagnostico ampliado: 3 seeds x 32 ventanas, todas `PASS`, sin fallback, sin acciones invalidas y sin colapso high-capacity a accion 0.

Bundle v1:

```text
~/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1
schema_id=phase45_v3_neural_mpc_experimental_bundle_v1
runtime_controller_integrated=false al definir bundle
phase6_formal_evaluation_performed=false
```

Runtime v1: integrado como controller guarded con bundle externo, fallback `robust_mpc`, `weights_only=True` en runtime, telemetria neural diagnostica y hash validation.

### Neural-MPC v2 full

Motivo de v2: `20260615_112752_rapido` mostro integracion runtime limpia pero una debilidad localizada en ventana real media-variable con rebuffer alto frente a Robust MPC.

Perfil v2:

```text
dataset_dir=~/TFG/datasets_normalizados/phase45_v3/throughput_quantile_full_v1_neural_mpc_v2
model_root=~/TFG/modelos/phase45_v3/throughput_quantile_predictor/full_v1_neural_mpc_v2
run_root=~/TFG/runs_phase45_v3/neural_mpc_full_v1_v2
seeds=452001,452002,452003
train_window_count=4096
validation_window_count=1024
qh_horizon_segments=5
qh_beam_width=24
max_windows_per_trace=4
```

Lectura de full training v2:

- Tres seeds con training `PASS` y evaluacion closed-loop offline `PASS`.
- `fallback=0`, acciones invalidas `0`, sin accion 0 en alta capacidad.
- Seed `452001` activa warning `paired_rebuffer_spike_vs_robust_mpc` con peor delta `+5.409446542610964 s`.
- Seeds `452002` y `452003` no activan warnings.
- Seed canonica aprobada para bundle v2: `452003`.
- Controller key v2: `phase45_v3_neural_throughput_calibrated_mpc_v2`.

Flags siguen siendo diagnosticos:

```text
benchmark_performed=false
ranking_performed=false
no_final_ranking=true
qoe_claims_authorized=false
```

Secuencia correcta definida para v2:

```text
exportar bundle v2 en WSL
-> empaquetar y mover a Ubuntu cliente
-> validar bundle v2
-> smoke runtime controller v2
-> Phase 6 diagnostico con v1 y v2
-> Phase 6 rapido con v1 y v2 si pasa
-> solo despues decidir si equilibrado tiene sentido
```

### Nueva linea paralela - Closed-loop SPBC/SPC v1

Decision: abrir `phase45_v3_closedloop_spbc_spc_v1` como linea paralela sin tocar Neural-MPC.

Filosofia:

```text
SPBC-v3 = policy neural candidata
SPC-v3  = critic predictivo por accion
hybrid  = SPBC propone + SPC audita/veta/reordena localmente
```

Primer paso autorizado:

```text
disenar e implementar generador de dataset pilot closedloop_spbc_spc_v1
```

Ruta dataset propuesta:

```text
~/TFG/datasets_normalizados/phase45_v3/closedloop_spbc_spc_pilot_v1
```

No autorizado todavia: entrenamiento, bundle, controller runtime, Phase 6, ranking ni claim de QoE.

## Phase 6 - Protocolo, metricas y paquete de evidencia

Phase 6 se ejecuta con `scripts/run_phase6_validacion_comparativa.py`.

Config base:

```text
schema_version=phase6_config_v1
manifest_path=/home/daniel/TFG/manifests_trazas/phase3/final/phase3_trace_manifest_curated.json
output_root=/home/daniel/TFG/runs_trazas/phase6/validacion_comparativa
repo_root=/home/daniel/TFG/DashClientModular4
engine=fake
seed=606
decision_interval_s=4.0
window_duration_s=300.0
compact_timestamps=true
max_media_segments=30
max_buffer_seconds=60.0
initial_quality=0
initial_controller_decision=false
```

Seleccion de trazas:

- Solo `split=eval`.
- `usable_for_eval` no debe ser `false`.
- Duracion >= ventana requerida.
- Sinteticas identificadas por `dataset_id=synthetic_controlled_network` o `semantics=synthetic_available_bandwidth`.
- Trazas reales formales deben superar suelo de throughput medio y maximo configurado.
- Seleccion balanceada por `dataset_id`, `semantics`, `network_condition` y `difficulty_bucket`.

Buckets de dificultad:

```text
mean < 1500 kbps -> baja_capacidad
1500 <= mean < 5000 -> media_capacidad o media_capacidad_variable
5000 <= mean < 20000 -> alta_capacidad o alta_capacidad_variable
mean >= 20000 -> muy_alta_capacidad
variabilidad = (max-min)/mean; variable si >= 1.5
```

Package structure:

```text
<package_root>/
  00_protocolo/
    protocolo_validacion.json
    session_plan.json
    session_plan.csv
    trace_windows.csv
    controllers.csv
    media_profiles.csv
    client_configs/
  01_ejecucion/
    runs/
    command_logs/
  02_resultados/
    raw_chunks.csv
    session_summary.csv
    aggregates_by_controller.json
    statistics.json
    resultados_para_validar.json
    resultados_para_validar.md
  03_graficas/
    plot_manifest.json
  04_informe/
    informe_comparativo.md
    conclusiones_tecnicas.md
    manifest_paquete_evidencia.json
```

Metricas agregadas por controller:

- `qoe_linear_mean` y `qoe_linear_sum`.
- `avg_quality_mbps`.
- `total_rebuffer_s_mean`.
- `rebuffer_ratio_mean`.
- `smoothness_penalty_mean`.
- `decision_latency_ms_mean`.
- Percentiles y conteos segun analisis.
- Auditoria neural en controllers propios: inference rows, fallback rows, diagnostic rows, hash ok, feature ok y latency.

Estadistica:

- Deltas emparejados por controller.
- Intervalos `ci95_low/high`.
- `sign_test_p_value`.
- Ranking solo si `benchmark_authorized` y `ranking_authorized` pasan gates.

Gates de paquete:

- Artefactos requeridos presentes.
- Sessions completadas y evaluables.
- Sin artefactos legacy.
- Controllers propios con auditoria neural correcta cuando son evaluables.
- Preset con capacidad de benchmark/ranking solo en condiciones permitidas.

Config local para comparar Neural-MPC v1/v2:

```text
config/phase6.neural_mpc_v1_v2.local.example.json
controllers=[rate_based, bola, robust_mpc, phase45_v3_neural_throughput_calibrated_mpc_v1, phase45_v3_neural_throughput_calibrated_mpc_v2]
output_root=/home/daniel/TFG/runs_trazas/phase6/validacion_comparativa_neural_mpc_v1_v2
preset=diagnostico por defecto en el ejemplo
```

## Corpus cientifico y documental

Regla metodologica permanente: no implementar directamente desde PDFs brutos si existen source cards, specs, decisiones canonicas o documentos operativos.

Flujo PDF/fuente -> Codex:

```text
PDF/fuente
-> paper_card.md o source_card.md
-> decision_matrix.md
-> implementation_spec.md
-> controller_api_mapping.md
-> acceptance_tests.md
-> prompt autosuficiente para Codex
-> implementacion
-> tests
-> validacion
-> cierre documental
```

### Corpus operativo Fase 4-5 v1 - ABR IA

Documentos detectados en `docs/contexto rama nueva/fase_4_5_v1/abr ia md/`: 32.

| # | Documento | Primer heading |
|---:|---|---|
| 1 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\01_comyco_2019_imitation_learning.md` | Comyco: Quality-Aware Adaptive Video Streaming via Imitation Learning |
| 2 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\02_puffer_fugu_2020_learning_in_situ.md` | Learning in situ: a randomized experiment in video streaming |
| 3 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\03_sabr_2025_bc_rl_finetuning.md` | SABR: A Stable Adaptive Bitrate Framework Using Behavior Cloning Pretraining and Reinforcement Learning Fine-Tuning |
| 4 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\04_pll_abr_2025_ppo_lstm_attention.md` | Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming |
| 5 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\05_greenabr_2022_energy_aware_drl.md` | GreenABR: Energy-Aware Adaptive Bitrate Streaming with Deep Reinforcement Learning |
| 6 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\06_alvs_2022_live_video_drl.md` | ALVS: Adaptive Live Video Streaming using deep reinforcement learning |
| 7 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\07_edge_rl_adaptive_streaming_2023.md` | HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance |
| 8 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\08_pca_gwo_bp_mpeg_dash_ai_bitrate_selection.md` | Bit rate selection technology of image processing based on artificial intelligence in MPEG-DASH adaptive streaming media |
| 9 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\09_a2br_2022_meta_rl_domain_priors.md` | A2BR: Learning Tailored Adaptive Bitrate Algorithms to Heterogeneous Network Conditions |
| 10 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\10_ant_2024_network_dynamics_dedicated_models.md` | ANT: Learning Accurate Network Dynamics for Enhanced Adaptive Video Streaming |
| 11 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\11_souane_2023_drl_dash.md` | Deep Reinforcement Learning-Based Approach for Video Streaming: Dynamic Adaptive Video Streaming over HTTP |
| 12 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\12_beta_2025_spatial_temporal_generalization.md` | BETA: A Novel Spatial-Temporal Learning Method for Enhancing Generalization in Adaptive Video Streaming |
| 13 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\13_visual_sensitivity_aware_drl_abr.md` | A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning |
| 14 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\14_incendio_sabr_marl_expert_guidance.md` | Incendio: Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance |
| 15 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\15_http_adaptive_streaming_review_2025.md` | HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges |
| 16 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\16_learning_based_methods_has_review_2025.md` | A Review of Learning-Based Methods for Adaptive Video Streaming Over HTTP |
| 17 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\17_bpa_bandwidth_prediction_drl_abr.md` | Enhancing Adaptive Video Streaming through Bandwidth Prediction with Deep Reinforcement Learning |
| 18 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\18_fortuna_2025_offline_meta_rl_diverse_networks.md` | Fortuna - Optimizing Adaptive Video Streaming: Offline Reinforcement Learning and Meta-Learning in Diverse Networks |
| 19 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\19_gelato_plume_2024_trace_skew_neural_abr.md` | Gelato / Plume - Practically High Performant Neural Adaptive Video Streaming |
| 20 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\20_kaken_20k14740_fair_high_qoe_multiuser_abr_report.md` | KAKEN 20K14740 - Adaptive bitrate control strategy for ensuring high-QoE and fair video streaming in multi-user networks |
| 21 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\21_a2br_learning_tailored_abr_domain_priors_meta_rl.md` | Learning Tailored Adaptive Bitrate Algorithms to Heterogeneous Network Conditions - A2BR |
| 22 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\22_ahaggar_bitrate_guidance_meta_rl_cmcd_cmsd.md` | Bitrate Adaptation and Guidance With Meta Reinforcement Learning - Ahaggar |
| 23 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\23_causalsim_2023_unbiased_trace_driven_simulation.md` | CausalSim - A Causal Framework for Unbiased Trace-Driven Simulation |
| 24 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\24_eastream_2026_environment_aware_abr_meta_rl_vae.md` | EAStream - Environment-Aware Adaptive Bitrate Algorithm for Reliable Video Streaming Services |
| 25 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\25_ppo_abr_2023_proximal_policy_optimization_drl.md` | PPO-ABR: Proximal Policy Optimization based Deep Reinforcement Learning for Adaptive BitRate streaming |
| 26 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\26_soda_2024_consistent_high_quality_non_neural_abr.md` | SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming |
| 27 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\27_dqnreg_2022_reinforcement_learning_rate_adaptation.md` | Reinforcement Learning-Based Rate Adaptation in Dynamic Video Streaming / DQNReg |
| 28 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\28_mambra_2026_session_bandwidth_prediction_ssm_mamba.md` | MamBRA: Session-Level Bandwidth Prediction for Adaptive Video Streaming using Selective State Space Models |
| 29 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\29_merina_2022_meta_rl_generalization_neural_abr.md` | MERINA: Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning |
| 30 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\30_metaabr_2024_meta_learning_adaptive_bitrate_selection.md` | MetaABR: A Meta-Learning Approach on Adaptative Bitrate Selection for Video Streaming |
| 31 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\31_oboe_2018_auto_tuning_abr_network_conditions.md` | Oboe: Auto-tuning Video ABR Algorithms to Network Conditions |
| 32 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\32_pensieve_2017_neural_adaptive_video_streaming.md` | Pensieve: Neural Adaptive Video Streaming |

Sintesis de decisiones extraidas de `decision_tecnica_modelos_v1.md`:

- Comyco y SABR aportan imitation learning, experto offline, DAgger/rollouts y BC antes de PPO.
- Puffer/Fugu, BPA y MamBRA apoyan predictor de throughput + decision ABR segura.
- A2BR, ANT, BETA, Oboe, Gelato/Plume, MERINA, MetaABR y EAStream apoyan balance por regimen, evaluacion por buckets y posible especializacion posterior.
- SODA, Oboe, Puffer/Fugu y CausalSim actuan como guardrails de deployability, consistencia y sesgo de simulacion.
- Energia, edge, multiusuario, live playback speed, short video MARL y VMAF quedan fuera del contrato Phase 6 actual.

### Estudios PDF convertidos a Markdown

Documentos detectados en `docs/todos los estudios pdf convertidos a md/`: 63.

| Documento | Primer heading |
|---|---|
| `docs\todos los estudios pdf convertidos a md\01_2015_seufert_qoe_http_adaptive_streaming_survey.md` | 01_2015_seufert_qoe_http_adaptive_streaming_survey |
| `docs\todos los estudios pdf convertidos a md\06_2024_peroni_qoe_status_quo_pitfalls_guidelines.md` | 06_2024_peroni_qoe_status_quo_pitfalls_guidelines |
| `docs\todos los estudios pdf convertidos a md\11_2022_zuo_ruyi_user_level_qoe_preference.md` | 11_2022_zuo_ruyi_user_level_qoe_preference |
| `docs\todos los estudios pdf convertidos a md\12_2025_alsader_qoe_driven_adaptive_video_streaming_6g_survey.md` | 12_2025_alsader_qoe_driven_adaptive_video_streaming_6g_survey |
| `docs\todos los estudios pdf convertidos a md\2011_liu_rate_adaptation_adaptive_http_streaming.md` | 2011_liu_rate_adaptation_adaptive_http_streaming |
| `docs\todos los estudios pdf convertidos a md\2011_stockhammer_dash_standards_design_principles.md` | 2011_stockhammer_dash_standards_design_principles |
| `docs\todos los estudios pdf convertidos a md\2012_ameigeiras_youtube_traffic_analysis_modelling.md` | 2012_ameigeiras_youtube_traffic_analysis_modelling |
| `docs\todos los estudios pdf convertidos a md\2013_riiser_commute_path_bandwidth_traces_3g_networks.md` | 2013_riiser_commute_path_bandwidth_traces_3g_networks |
| `docs\todos los estudios pdf convertidos a md\2014_huang_bba_buffer_based_rate_adaptation.md` | 2014_huang_bba_buffer_based_rate_adaptation |
| `docs\todos los estudios pdf convertidos a md\2014_ramos_munoz_mobile_youtube_traffic_characteristics.md` | 2014_ramos_munoz_mobile_youtube_traffic_characteristics |
| `docs\todos los estudios pdf convertidos a md\2015_netravali_mahimahi_record_replay_http.md` | 2015_netravali_mahimahi_record_replay_http |
| `docs\todos los estudios pdf convertidos a md\2015_yin_mpc_control_theoretic_abr_http.md` | 2015_yin_mpc_control_theoretic_abr_http |
| `docs\todos los estudios pdf convertidos a md\2016_van_der_hooft_http2_hevc_video_over_4g_lte.md` | 2016_van_der_hooft_http2_hevc_video_over_4g_lte |
| `docs\todos los estudios pdf convertidos a md\2018_raca_4g_lte_dataset_channel_context_metrics.md` | 2018_raca_4g_lte_dataset_channel_context_metrics |
| `docs\todos los estudios pdf convertidos a md\2019_bentaleb_abr_survey_http_streaming.md` | 2019_bentaleb_abr_survey_http_streaming |
| `docs\todos los estudios pdf convertidos a md\2019_spiteri_dash_reference_player_bola_dynamic.md` | 2019_spiteri_dash_reference_player_bola_dynamic |
| `docs\todos los estudios pdf convertidos a md\2019_wei_trace_based_emulation_throughput_prediction_abr.md` | 2019_wei_trace_based_emulation_throughput_prediction_abr |
| `docs\todos los estudios pdf convertidos a md\2020_narayanan_lumos5g_imc.md` | 2020_narayanan_lumos5g_imc |
| `docs\todos los estudios pdf convertidos a md\2020_raca_5g_dataset_channel_context_metrics_mmsys.md` | 2020_raca_5g_dataset_channel_context_metrics_mmsys |
| `docs\todos los estudios pdf convertidos a md\2020_spiteri_bola_near_optimal_bitrate_adaptation_ton.md` | 2020_spiteri_bola_near_optimal_bitrate_adaptation_ton |
| `docs\todos los estudios pdf convertidos a md\2020_yan_puffer_learning_in_situ_nsdi.md` | 2020_yan_puffer_learning_in_situ_nsdi |
| `docs\todos los estudios pdf convertidos a md\2022_iso_iec_23009_1_dash_reference.md` | 2022_iso_iec_23009_1_dash_reference |
| `docs\todos los estudios pdf convertidos a md\2023_bothra_veritas_causal_queries_video_streaming_traces.md` | 2023_bothra_veritas_causal_queries_video_streaming_traces |
| `docs\todos los estudios pdf convertidos a md\2025_hoffman_into_the_wild_ml_based_abr.md` | 2025_hoffman_into_the_wild_ml_based_abr |
| `docs\todos los estudios pdf convertidos a md\2025_peroni_gorinsky_video_streaming_best_effort_pipeline_survey.md` | 2025_peroni_gorinsky_video_streaming_best_effort_pipeline_survey |
| `docs\todos los estudios pdf convertidos a md\A quality-of-experience database for adaptive video streaming.md` | ofstallingpersegment, |
| `docs\todos los estudios pdf convertidos a md\A review of learning-based methods for adaptive video streaming over HTTP.md` | A review of learning-based methods for adaptive video streaming over HTTP |
| `docs\todos los estudios pdf convertidos a md\A2BR.md` | A2BR |
| `docs\todos los estudios pdf convertidos a md\AIRL.md` | AIRL |
| `docs\todos los estudios pdf convertidos a md\ANT.md` | ANT |
| `docs\todos los estudios pdf convertidos a md\BETA.md` | Step1:Input-trainingtracedataΛ;Output-trainedclassifierC |
| `docs\todos los estudios pdf convertidos a md\Beyond Throughput The Next Generation A 5G Dataset with Channel and Context Metrics.md` | Beyond Throughput The Next Generation A 5G Dataset with Channel and Context Metrics |
| `docs\todos los estudios pdf convertidos a md\Beyond Throughput a 4G LTE Dataset with Channel and Context Metrics.md` | Beyond Throughput a 4G LTE Dataset with Channel and Context Metrics |
| `docs\todos los estudios pdf convertidos a md\Bitrate Adaptation and Guidance With Meta Reinforcement Learning.md` | Bitrate Adaptation and Guidance With Meta Reinforcement Learning |
| `docs\todos los estudios pdf convertidos a md\Buffer awareness neural adaptive video streaming for avoiding extra buffer consumption.md` | randomize bitrate ladders: 100-7000kbps |
| `docs\todos los estudios pdf convertidos a md\CausalSim.md` | CausalSim |
| `docs\todos los estudios pdf convertidos a md\CellReplay.md` | CellReplay |
| `docs\todos los estudios pdf convertidos a md\Comyco.md` | Comyco |
| `docs\todos los estudios pdf convertidos a md\EAStream.md` | EAStream |
| `docs\todos los estudios pdf convertidos a md\Fortuna.md` | Fortuna |
| `docs\todos los estudios pdf convertidos a md\Gelato.md` | Gelato |
| `docs\todos los estudios pdf convertidos a md\HTTP Adaptive Streaming A Review on Current Advances and Future Challenges.md` | HTTP Adaptive Streaming A Review on Current Advances and Future Challenges |
| `docs\todos los estudios pdf convertidos a md\Hybrid Adaptive Bitrate for Video Streaming.md` | Fallback point identifier |
| `docs\todos los estudios pdf convertidos a md\MERINA.md` | MERINA |
| `docs\todos los estudios pdf convertidos a md\Mahimahi.md` | Mahimahi |
| `docs\todos los estudios pdf convertidos a md\MetaABR.md` | MetaABR |
| `docs\todos los estudios pdf convertidos a md\NMoEABR.md` | NMoEABR |
| `docs\todos los estudios pdf convertidos a md\ONNX Runtime Python API.md` | X is numpy array on cpu |
| `docs\todos los estudios pdf convertidos a md\Oboe.md` | Oboe |
| `docs\todos los estudios pdf convertidos a md\On the (In) Security of Loading Machine Learning Models.md` | On the (In) Security of Loading Machine Learning Models |
| `docs\todos los estudios pdf convertidos a md\Pensieve.md` | Pensieve |
| `docs\todos los estudios pdf convertidos a md\Plume.md` | Plume |
| `docs\todos los estudios pdf convertidos a md\PyTorch 2.12 documentation.md` | Load all tensors onto the CPU |
| `docs\todos los estudios pdf convertidos a md\QoE modeling for HTTP adaptive video streaming.md` | QoE modeling for HTTP adaptive video streaming |
| `docs\todos los estudios pdf convertidos a md\Real-world Video Adaptation with Reinforcement Learning.md` | Real-world Video Adaptation with Reinforcement Learning |
| `docs\todos los estudios pdf convertidos a md\SABR.md` | SABR |
| `docs\todos los estudios pdf convertidos a md\SODA.md` | SODA |
| `docs\todos los estudios pdf convertidos a md\SafeSABR.md` | SafeSABR |
| `docs\todos los estudios pdf convertidos a md\Surveys de 2025.md` | Surveys de 2025 |
| `docs\todos los estudios pdf convertidos a md\Uncertainty-aware robust adaptive video streaming with bayesian neural network and model predictive control.md` | Uncertainty-aware robust adaptive video streaming with bayesian neural network and model predictive control |
| `docs\todos los estudios pdf convertidos a md\Understanding quality of experience of heuristic-based HTTP adaptive bitrate algorithms.md` | Understanding quality of experience of heuristic-based HTTP adaptive bitrate algorithms |
| `docs\todos los estudios pdf convertidos a md\Veritas.md` | Veritas |
| `docs\todos los estudios pdf convertidos a md\Zhou.md` | Zhou |

### Source cards y paper cards versionadas

Tarjetas detectadas por nombre (`source_cards`, `paper_cards`, `paper_card`, `source_evidence`): 79.

| Documento | Primer heading |
|---|---|
| `docs\contexto rama original\01_baselines\bba\paper_card.md` | Paper Card: BBA Baseline |
| `docs\contexto rama original\01_baselines\bba\source_evidence.md` | Source evidence â€” BBA |
| `docs\contexto rama original\01_baselines\bola\paper_card.md` | Paper Card: BOLA Baseline |
| `docs\contexto rama original\01_baselines\bola\source_evidence.md` | Source evidence â€” BOLA |
| `docs\contexto rama original\01_baselines\mpc\paper_card.md` | Paper Card: MPC Baseline |
| `docs\contexto rama original\01_baselines\mpc\source_evidence.md` | Source evidence â€” MPC |
| `docs\contexto rama original\01_baselines\optional_methods\soda\source_evidence.md` | Source evidence â€” SODA optional candidate |
| `docs\contexto rama original\01_baselines\rate_based\paper_card.md` | Paper Card: Rate-Based Baseline |
| `docs\contexto rama original\01_baselines\rate_based\source_evidence.md` | Source evidence â€” rate_based |
| `docs\contexto rama original\01_baselines\robust_mpc\paper_card.md` | Paper Card: RobustMPC Baseline |
| `docs\contexto rama original\01_baselines\robust_mpc\source_evidence.md` | Source evidence â€” RobustMPC |
| `docs\contexto rama original\03_qoe_reward\source_cards\alsader2025_qoe_driven_streaming_6g.md` | Source card - alsader2025 |
| `docs\contexto rama original\03_qoe_reward\source_cards\chen2024_soda_smoothness_qoe.md` | Source card - chen2024 |
| `docs\contexto rama original\03_qoe_reward\source_cards\mao2017_pensieve_qoe_reward.md` | Source card - mao2017 |
| `docs\contexto rama original\03_qoe_reward\source_cards\netflix_vmaf_perceptual_quality.md` | Source card - netflixVmaf |
| `docs\contexto rama original\03_qoe_reward\source_cards\peroni2024_qoe_pitfalls_guidelines.md` | Source card - peroni2024 |
| `docs\contexto rama original\03_qoe_reward\source_cards\peroni2025_pipeline_qoe_context.md` | Source card - peroni2025 |
| `docs\contexto rama original\03_qoe_reward\source_cards\seufert2015_has_qoe_survey.md` | Source card - seufert2015 |
| `docs\contexto rama original\03_qoe_reward\source_cards\spiteri2020_bola_utility_qoe.md` | Source card - spiteri2020 |
| `docs\contexto rama original\03_qoe_reward\source_cards\timmerer2025_has_review_qoe_context.md` | Source card - timmerer2025 |
| `docs\contexto rama original\03_qoe_reward\source_cards\yin2015_mpc_qoe_objective.md` | Source card - yin2015 |
| `docs\contexto rama original\03_qoe_reward\source_cards\zhou2022_adaptive_streaming_quality_assessment.md` | Source card - zhou2022 |
| `docs\contexto rama original\03_qoe_reward\source_cards\zuo2022_ruyi_user_preference_qoe.md` | Source card - zuo2022 |
| `docs\contexto rama original\04_neural_abr\source_cards\a2br2022_meta_rl.md` | Source card: a2br2022_meta_rl |
| `docs\contexto rama original\04_neural_abr\source_cards\ababR_search_note.md` | Source note: ababR_search_note |
| `docs\contexto rama original\04_neural_abr\source_cards\abrl_facebook2020_real_world_rl.md` | Source card: abrl_facebook2020_real_world_rl |
| `docs\contexto rama original\04_neural_abr\source_cards\ahaggar2024_bitrate_guidance.md` | Source card: ahaggar2024_bitrate_guidance |
| `docs\contexto rama original\04_neural_abr\source_cards\airl2025_inverse_rl.md` | Source card: airl2025_inverse_rl |
| `docs\contexto rama original\04_neural_abr\source_cards\ant2024_network_dynamics.md` | Source card: ant2024_network_dynamics |
| `docs\contexto rama original\04_neural_abr\source_cards\beta2025_spatial_temporal_generalization.md` | Source card: beta2025_spatial_temporal_generalization |
| `docs\contexto rama original\04_neural_abr\source_cards\causalsim2023_unbiased_trace_simulation.md` | Source card: causalsim2023_unbiased_trace_simulation |
| `docs\contexto rama original\04_neural_abr\source_cards\comyco2020_lifelong_imitation_learning.md` | Source card: comyco2020_lifelong_imitation_learning |
| `docs\contexto rama original\04_neural_abr\source_cards\eastream2026_environment_aware.md` | Source card: eastream2026_environment_aware |
| `docs\contexto rama original\04_neural_abr\source_cards\fortuna2025_offline_meta_rl.md` | Source card: fortuna2025_offline_meta_rl |
| `docs\contexto rama original\04_neural_abr\source_cards\http_adaptive_streaming_review2025.md` | Source card: http_adaptive_streaming_review2025 |
| `docs\contexto rama original\04_neural_abr\source_cards\into_the_wild2025_real_world_testing.md` | Source card: into_the_wild2025_real_world_testing |
| `docs\contexto rama original\04_neural_abr\source_cards\merina2022_meta_rl_generalization.md` | Source card: merina2022_meta_rl_generalization |
| `docs\contexto rama original\04_neural_abr\source_cards\metaabr2024_meta_learning.md` | Source card: metaabr2024_meta_learning |
| `docs\contexto rama original\04_neural_abr\source_cards\nmoeabr2026_mixture_of_experts.md` | Source card: nmoeabr2026_mixture_of_experts |
| `docs\contexto rama original\04_neural_abr\source_cards\oboe2018_autotuning_abr.md` | Source card: oboe2018_autotuning_abr |
| `docs\contexto rama original\04_neural_abr\source_cards\pensieve2017_neural_abr.md` | Source card: pensieve2017_neural_abr |
| `docs\contexto rama original\04_neural_abr\source_cards\plume_gelato2024_trace_skew.md` | Source card: plume_gelato2024_trace_skew |
| `docs\contexto rama original\04_neural_abr\source_cards\ppo_abr_search_note.md` | Source note: ppo_abr_search_note |
| `docs\contexto rama original\04_neural_abr\source_cards\puffer_fugu2020_learning_in_situ.md` | Source card: puffer_fugu2020_learning_in_situ |
| `docs\contexto rama original\04_neural_abr\source_cards\sabr2025_bc_rl_finetuning.md` | Source card: sabr2025_bc_rl_finetuning |
| `docs\contexto rama original\04_neural_abr\source_cards\soda2024_smoothness_controller.md` | Source card: soda2024_smoothness_controller |
| `docs\contexto rama original\04_neural_abr\source_cards\survey_learning_has2025.md` | Source card: survey_learning_has2025 |
| `docs\contexto rama original\04_neural_abr\source_cards\survey_pipeline2025.md` | Source card: survey_pipeline2025 |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\01_safesabr_runtime_safety_auditor.md` | Source card 01: SafeSABR runtime safety auditor |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\02_deepbuffer_action_mask_variable_ladder.md` | Source card 02: DeepBuffer action mask and variable ladder |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\03_a2br_domain_priors_fallback.md` | Source card 03: A2BR domain priors and fallback |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\04_abrl_facebook_candidate_scoring_deployment.md` | Source card 04: ABRL Facebook candidate scoring deployment |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\05_ahaggar_bitrate_guidance_hybrid_boundary.md` | Title |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\06_puffer_fugu_ml_predictor_mpc.md` | Source card 06: Puffer/Fugu ML predictor plus MPC |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\07_hybrid_abr_decision_level_fallback.md` | Source card 07: Hybrid ABR decision-level fallback |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\08_bayesmpc_uncertainty_predictor_mpc.md` | Source card 08: BayesMPC uncertainty predictor plus MPC |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\09_causalsim_trace_bias_contamination.md` | Source card 09: CausalSim trace bias and contamination |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\10_into_the_wild_real_world_testing_gap.md` | Title |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\11_comyco_lifelong_imitation_learning.md` | Title |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\12_oboe_runtime_network_state_autotuning.md` | Title |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\13_soda_deployable_smoothness_controller.md` | Title |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\14_sabr_bc_pretraining_rl_finetuning.md` | Title |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\15_beta_under_generalization.md` | Title |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\16_ant_network_dynamics_detection.md` | Title |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\17_gelato_plume_trace_skew_real_world.md` | Title |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\18_ml_model_loading_security.md` | Source card 18: ML model loading security |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\19_has_review_2025_background.md` | Title |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\20_learning_based_has_review_2025_background.md` | Title |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\21_metaabr_meta_learning_background.md` | Title |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\22_pytorch_model_loading_reference.md` | Source card 22: PyTorch model loading reference |
| `docs\contexto rama original\05_neural_controller_integration\source_cards\23_onnx_runtime_reference.md` | Title |
| `docs\contexto rama original\0_field_map\dash_source_evidence.md` | Source evidence â€” DASH, HAS and field map |
| `docs\contexto rama original\0_field_map\local_streaming_source_evidence.md` | Source evidence â€” local UGR streaming-related work |
| `docs\contexto rama original\0_field_map\paper_cards\ameigeiras_2012_youtube_traffic.md` | Source Card: Ameigeiras et al. 2012 YouTube Traffic |
| `docs\contexto rama original\0_field_map\paper_cards\bentaleb_2019_abr_survey.md` | Source Card: Bentaleb et al. 2019 ABR Survey |
| `docs\contexto rama original\0_field_map\paper_cards\peroni_2025_streaming_pipeline_survey.md` | Source Card: Peroni and Gorinsky 2025 Pipeline Survey |
| `docs\contexto rama original\0_field_map\paper_cards\ramos_munoz_2014_mobile_youtube_traffic.md` | Source Card: Ramos-Munoz et al. 2014 Mobile YouTube Traffic |
| `docs\contexto rama original\0_field_map\paper_cards\stockhammer_2011_dash.md` | Source Card: Stockhammer 2011 DASH |
| `docs\contexto rama original\0_field_map\paper_cards\timmerer_2025_has_review.md` | Source Card: Timmerer et al. 2025 HAS Review |

## Arquitectura de codigo

Separacion tecnica obligatoria mantenida por el proyecto:

- parser MPD;
- descarga de segmentos;
- buffer;
- motor de reproduccion;
- control ABR;
- logging;
- evaluacion;
- trace replay;
- normalizacion de datasets;
- documentacion cientifica;
- workspaces externos.

Mapa funcional:

| Area | Archivos | Papel |
|---|---:|---|
| `core/parser` | 4 | Parser MPD y contratos de representaciones |
| `core/downloader.py` | 0 | Descarga HTTP/fragmentos |
| `core/media_engine` | 4 | Engine fake/GStreamer |
| `core/controller` | 21 | Controllers clasicos, IA, registry y safety |
| `core/trace_replay` | 24 | Schema, manifest, converters, network model |
| `core/evaluation` | 3 | QoE y artefactos de evaluacion |
| `core/neural_abr` | 23 | NeuralABR-Lite training/inference/bundles |
| `core/phase45_v1` | 18 | SPBC/SPC v1/v2 dataset/training/offline validation |
| `core/phase45_v3` | 16 | Entorno cerrado, QH scorer, Neural-MPC, bundle, validation |
| `core/phase6` | 6 | Config, catalog, seleccion, analisis, verificacion Phase 6 |

Entrypoints principales:

| Archivo | Papel |
|---|---|
| `main.py` | Runner principal cliente DASH con config |
| `player.py` | Loop de reproduccion/runtime; tocar solo con contrato y tests |
| `analysis_metrics.py` | Utilidades historicas/metricas de analisis |
| `progress_bar.py` | Presentacion/progreso, no autoridad experimental |

Controllers actuales:

| Key | Factory | Papel |
|---|---|---|
| `min_rate` | `MinRateController` | control tecnico/debug |
| `fixed_rate` | `FixedRateController` | control tecnico/debug |
| `max_rate` | `MaxRateController` | control tecnico/debug |
| `rate_based` | `RateBasedController` | baseline ABR clasico |
| `bba` | `BbaController` | baseline ABR clasico |
| `bola` | `BolaController` | baseline ABR clasico |
| `mpc` | `MpcController` | baseline ABR clasico |
| `robust_mpc` | `RobustMpcController` | baseline ABR clasico |
| `neural_abr_lite_robust_mpc` | `NeuralAbrLiteRobustMpcController` | IA historica Phase 4/5 |
| `neural_abr_lite_teacher_hibrido` | `NeuralAbrLiteTeacherHibridoController` | IA historica Phase 4/5 |
| `spbc_abr_v2_dpo_anchor_safe_rank` | `SpbcAbrV2DpoAnchorSafeRankController` | IA experimental SPBC |
| `phase45_v3_neural_throughput_calibrated_mpc_v1` | `Phase45V3NeuralMpcController` | IA Neural-MPC Phase45 v3 |
| `phase45_v3_neural_throughput_calibrated_mpc_v2` | `Phase45V3NeuralMpcV2Controller` | IA Neural-MPC Phase45 v3 |
| `fixed_quality` | `FixedQualityController` | control tecnico/debug |
| `scripted_quality` | `ScriptedQualityController` | control tecnico/debug |
| `max_quality` | `MaxQualityController` | control tecnico/debug |

Inventario AST resumido de modulos Python por area:

### `core/__init__.py`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\__init__.py` |  |  |  |

### `core/benchmark_contract.py`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\benchmark_contract.py` |  | `normalize_segment_index`, `classify_segment_phase`, `should_use_segment_for_eval`, `classify_stall_event`, `should_use_stall_for_eval` | `PHASE_INIT`, `PHASE_STARTUP`, `PHASE_WARMUP`, `PHASE_STEADY_STATE`, `PHASE_DRAIN`, `PHASE_TERMINAL`, `PHASE_ERROR`, `SEGMENT_PHASES` (+6) |

### `core/client_config.py`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\client_config.py` | `ConfigError`, `MediaEngineConfig`, `ControllerConfig`, `PlaybackConfig`, `DownloaderConfig`, `NetworkReplayConfig`, `OutputConfig`, `LoggingConfig` (+2) | `load_client_config`, `validate_config_for_run`, `_select_config_path`, `_load_yaml_file`, `_parse_simple_yaml`, `_parse_scalar`, `_deep_merge`, `_mapping`, `_as_str`, `_as_optional_str` (+6) | `REPO_ROOT`, `DEFAULT_EXAMPLE_CONFIG`, `DEFAULT_LOCAL_CONFIG` |

### `core/controller`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\controller\__init__.py` |  |  |  |
| `core\controller\base.py` | `BaseController` |  |  |
| `core\controller\bba.py` | `BbaController` | `_available_rates_Bps`, `_clamp_level`, `_finish`, `_non_negative_float`, `_positive_float`, `_finite_float`, `_to_int` | `DEFAULT_RESERVOIR_S`, `DEFAULT_CUSHION_S` |
| `core\controller\bola.py` | `BolaController` | `_available_rates_Bps`, `_utilities_log_rate_ratio`, `_candidate_segment_sizes_B`, `_normalize_segment_sizes_B`, `_rate_to_bytes_per_second`, `_size_to_bytes`, `_clamp_level`, `_finish`, `_positive_float`, `_optional_non_negative_float` (+6) | `DEFAULT_BOLA_V`, `DEFAULT_BOLA_GAMMA`, `DEFAULT_MIN_SEGMENT_DURATION_S`, `DEFAULT_UTILITY_MODE`, `DEFAULT_SIZE_MODE`, `DEFAULT_ALL_NEGATIVE_POLICY` |
| `core\controller\contract.py` |  | `missing_feedback_keys`, `validate_feedback_keys`, `validate_rates`, `quantize_rate_to_level` | `CONTROLLER_CONTRACT_VERSION`, `CONTROLLER_API_STATUS`, `REQUIRED_FEEDBACK_KEYS`, `CURRENT_FEEDBACK_KEYS`, `FEEDBACK_UNITS`, `TARGET_RATE_UNIT`, `QUALITY_LEVEL_UNIT`, `LEGACY_FEEDBACK_KEYS` (+2) |
| `core\controller\fixed_quality.py` | `FixedQualityController` | `_clamp_level`, `_to_int` |  |
| `core\controller\max_quality_controller.py` | `MaxQualityController` |  |  |
| `core\controller\mpc.py` | `MpcController` | `_simulate_sequence`, `_available_rates_Bps`, `_configured_throughput_history_Bps`, `_measured_throughput_sample_Bps`, `_harmonic_mean_Bps`, `_qualities_log_rate_ratio`, `_candidate_segment_sizes_B`, `_normalize_segment_sizes_B`, `_rate_to_bytes_per_second`, `_size_to_bytes` (+13) | `DEFAULT_HORIZON`, `DEFAULT_THROUGHPUT_HISTORY_WINDOW`, `DEFAULT_REBUFFER_PENALTY`, `DEFAULT_SWITCH_PENALTY`, `DEFAULT_STARTUP_LEVEL`, `DEFAULT_MAX_ENUMERATED_SEQUENCES`, `DEFAULT_MIN_VALID_THROUGHPUT_BPS`, `DEFAULT_MIN_SEGMENT_DURATION_S` (+2) |
| `core\controller\neural_abr_diagnostics.py` | `NeuralAbrDiagnostics` | `stable_reason`, `augment_feedback_with_neural_diagnostics` | `NEURAL_DIAGNOSTIC_KEYS`, `STABLE_FALLBACK_REASONS` |
| `core\controller\neural_abr_lite.py` | `NeuralAbrLiteController`, `NeuralAbrLiteRobustMpcController`, `NeuralAbrLiteTeacherHibridoController` | `_create_classical_fallback`, `_apply_load_error_diagnostics`, `_set_raw_action_diagnostics`, `_runtime_inference_reason`, `_lowest_rate_from_payload`, `_fallback_payload`, `_basic_rates_and_mask`, `_basic_rates`, `_positive_float`, `_finite_float` (+2) | `DEFAULT_FALLBACK_CONTROLLER`, `DEFAULT_MAX_INFERENCE_LATENCY_MS` |
| `core\controller\neural_abr_loader.py` | `NeuralAbrRuntimeBundleError`, `NeuralAbrRuntimeBundle` | `load_neural_abr_runtime_bundle`, `_validate_bundle`, `_load_feature_schema`, `_torch_load_weights_only`, `_assert_candidate_indices_are_positions`, `_finite_scores`, `_select_position` |  |
| `core\controller\neural_abr_runtime_features.py` | `RuntimeFeatureError`, `RuntimeFeaturePayload`, `NeuralAbrRuntimeFeatureBuilder` | `_candidate_features`, `_chunks_remaining`, `_left_pad`, `_finite_number`, `_int_or_none`, `_clamp` |  |
| `core\controller\neural_abr_safety.py` | `NeuralAbrSafetyError` | `safe_action_to_rate`, `lowest_valid_action` |  |
| `core\controller\phase45_v3_neural_mpc.py` | `Phase45V3NeuralMpcRuntimeError`, `Phase45V3NeuralMpcRuntimeBundle`, `Phase45V3NeuralMpcController`, `Phase45V3NeuralMpcV2Controller` | `_validate_bundle`, `_torch_load_weights_only`, `_ladder_from_payload`, `_state_from_payload`, `_positive_history`, `_lowest_valid_rate`, `_rates_from_feedback`, `_apply_load_error_diagnostics`, `_positive_float`, `_positive_int` (+2) | `DEFAULT_NEURAL_MPC_BUNDLE_DIR`, `DEFAULT_NEURAL_MPC_V2_BUNDLE_DIR`, `DEFAULT_FALLBACK_CONTROLLER` |
| `core\controller\rate_based.py` | `RateBasedController` | `_available_rates_Bps`, `_measured_throughput_Bps`, `_history_throughput_Bps`, `_rate_to_bytes_per_second`, `_floor_rate_to_level`, `_current_level`, `_clamp_level`, `_finish`, `_bounded_float`, `_non_negative_float` (+3) | `DEFAULT_SAFETY_FACTOR`, `DEFAULT_EWMA_ALPHA`, `DEFAULT_CRITICAL_BUFFER_S`, `DEFAULT_STARTUP_LEVEL`, `DEFAULT_MAX_UPSHIFT_LEVELS` |
| `core\controller\registry.py` | `ControllerSpec` | `available_controllers`, `create_controller` | `CONTROLLER_REGISTRY` |
| `core\controller\robust_mpc.py` | `RobustMpcController` | `_configured_prediction_error_history`, `_prediction_errors_from_history_pairs`, `_configured_rate_history_Bps`, `_prediction_error_ratio`, `_unit_interval_float`, `_first_not_none` | `DEFAULT_PREDICTION_ERROR_WINDOW`, `DEFAULT_STARTUP_SAFETY_FACTOR`, `DEFAULT_EPSILON_THROUGHPUT_BPS` |
| `core\controller\sanity_rate.py` | `MinRateController`, `MaxRateController`, `FixedRateController` | `_available_rates`, `_normalize_rates`, `_floor_rate_to_level`, `_clamp_level`, `_target_rate_to_bytes_per_second`, `_finish`, `_first_not_none`, `_to_int` |  |
| `core\controller\scripted_quality.py` | `ScriptedQualityController` | `_normalize_levels`, `_clamp_level`, `_to_int`, `_to_non_negative_int` |  |
| `core\controller\spbc_abr_v2_dpo.py` | `SpbcAbrV2DpoAnchorSafeRankController` |  |  |
| `core\controller\spbc_abr_v2_dpo_loader.py` | `SpbcV2DpoRuntimeBundle` | `load_spbc_v2_dpo_runtime_bundle`, `_validate_bundle`, `_load_feature_schema`, `_load_normalization`, `_build_feature_rows`, `_normalize_vector`, `_normalize_matrix`, `_tensor_row`, `_torch_load_weights_only`, `_assert_candidate_indices_are_positions` (+6) |  |

### `core/dataset_schema.py`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\dataset_schema.py` |  | `feedback_column_name`, `feedback_column_names`, `build_segment_telemetry_header`, `build_default_segment_telemetry_header`, `build_evaluation_segments_header`, `validate_unique_columns`, `validate_row_length` | `SEGMENT_TELEMETRY_SCHEMA_VERSION`, `EVALUATION_SEGMENTS_SCHEMA_VERSION`, `SEGMENT_TELEMETRY_ROW_COLUMNS`, `SEGMENT_TELEMETRY_SEGMENT_COLUMNS`, `SEGMENT_TELEMETRY_DERIVED_COLUMNS`, `SEGMENT_TELEMETRY_STALL_COLUMNS`, `EVALUATION_SEGMENTS_COLUMNS`, `DEFAULT_SEGMENT_TELEMETRY_FEEDBACK_KEYS` (+7) |

### `core/downloader.py`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\downloader.py` | `SegmentDownloader` |  |  |

### `core/evaluation`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\evaluation\__init__.py` |  |  |  |
| `core\evaluation\artifacts.py` | `QoEArtifactError`, `QoEArtifactComputationResult` | `load_segment_qoe_inputs_from_csv`, `compute_qoe_summary_from_segments_csv`, `compute_qoe_artifacts_from_dry_run`, `_require_file`, `_read_json_object`, `_write_json`, `_require_columns`, `_resolve_expected_segment_count`, `_derive_gate_reasons`, `_row_gate_values` (+3) | `DRY_RUN_SEGMENTS_FILENAME`, `DRY_RUN_SUMMARY_FILENAME`, `DRY_RUN_MANIFEST_FILENAME`, `QOE_SEGMENT_REWARDS_FILENAME`, `QOE_RUN_SUMMARY_FILENAME`, `QOE_ARTIFACT_MANIFEST_FILENAME`, `REQUIRED_QOE_SEGMENT_COLUMNS`, `GATE_USE_FOR_EVAL` (+2) |
| `core\evaluation\qoe.py` | `SegmentQoEInput`, `QoEWeights`, `QoEResult` | `compute_linear_qoe`, `compute_log_qoe`, `_validated_segments`, `_validated_weights`, `_require_finite_positive`, `_require_finite_non_negative`, `_require_finite`, `_adjacent_deltas`, `_build_result` | `LINEAR_QOE_VERSION`, `LOG_QOE_VERSION`, `DEFAULT_LINEAR_REBUFFER_WEIGHT`, `DEFAULT_LOG_REBUFFER_WEIGHT`, `DEFAULT_SMOOTHNESS_WEIGHT` |

### `core/media_engine`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\media_engine\__init__.py` |  |  |  |
| `core\media_engine\base.py` | `BaseMediaEngine` |  |  |
| `core\media_engine\fake.py` | `FakeMediaEngine` |  |  |
| `core\media_engine\gst_media_engine.py` | `GstMediaEngine` | `gstreamer_unavailable_message`, `_format_exception` | `_LOG_LEVEL` |

### `core/neural_abr`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\neural_abr\__init__.py` |  |  |  |
| `core\neural_abr\action_mask.py` | `ActionMaskError` | `build_action_mask`, `validate_action_mask`, `assert_action_valid`, `lowest_valid_action` |  |
| `core\neural_abr\artifacts.py` | `NeuralAbrArtifactError` | `resolve_path`, `ensure_outside_repo`, `prepare_output_dir`, `ensure_existing_dir`, `write_json`, `read_json`, `write_jsonl`, `read_jsonl` | `REPO_ROOT` |
| `core\neural_abr\bundle.py` | `BundleError` | `prepare_bundle_output_dir`, `resolve_bundle_dir`, `sha256_file`, `bundle_file_record`, `write_phase4_bundle_manifest`, `validate_phase4_bundle_dir`, `require_bundle_files` | `REQUIRED_BUNDLE_FILES`, `HASHED_BUNDLE_FILES` |
| `core\neural_abr\bundle_validation.py` | `BundleValidationError` | `validate_phase4_inference_bundle`, `_gate`, `_p95` |  |
| `core\neural_abr\candidate_readiness.py` | `CandidateReadinessError` | `assess_phase4_candidate_model`, `_gate`, `_mapping`, `_float_eq`, `_float_at_least`, `_all_finite`, `_prediction_warnings`, `_sha256_file` |  |
| `core\neural_abr\constants.py` |  |  | `PHASE4_TRAINING_DATA_SCHEMA_ID`, `PHASE4_FEATURE_SCHEMA_ID`, `PHASE4_LABEL_SCHEMA_ID`, `PHASE4_NORMALIZATION_SCHEMA_ID`, `PHASE4_LEAKAGE_AUDIT_SCHEMA_ID`, `PHASE4_TRAINING_SMOKE_SCHEMA_ID`, `PHASE4_MODEL_CONFIG_SCHEMA_ID`, `PHASE4_FORMAL_TRAINING_SCHEMA_ID` (+47) |
| `core\neural_abr\content_ladder.py` | `ContentLadderError`, `Representation`, `ContentLadder` | `default_training_ladder`, `_validate_ladder` |  |
| `core\neural_abr\export_bundle.py` | `BundleExportError` | `export_phase4_inference_bundle`, `_validate_export_inputs`, `_build_ladder_schema`, `_build_model_card`, `_build_inference_contract`, `_build_fallback_policy`, `_utc_now` |  |
| `core\neural_abr\features.py` | `FeatureError` | `build_context_features`, `build_candidate_features`, `flatten_context_features`, `flatten_candidate_features`, `build_feature_schema`, `audit_feature_payload`, `reject_forbidden_model_inputs`, `_left_pad`, `_numeric_sequence`, `_finite_number` |  |
| `core\neural_abr\hybrid_teacher.py` | `ClassicTeacherDecision`, `HybridTeacherSampleDraft`, `ClassicTeacherTrajectory`, `HybridTeacherWindowSelection`, `HybridTeacherError`, `ClassicControllerTeacher` | `select_hybrid_teacher_for_window`, `build_hybrid_label_for_draft`, `qoe_linear_reward_for_replay_step`, `hybrid_selection_audit`, `_simulate_teacher_trajectory`, `_build_controller`, `_feedback_from_state`, `_action_from_target_rate`, `_trajectory_sort_key` |  |
| `core\neural_abr\hybrid_training_data.py` |  | `build_phase4_hybrid_teacher_data_from_plan`, `build_phase4_hybrid_teacher_data_from_plan_file`, `validate_phase4_hybrid_teacher_data_dir`, `_samples_for_hybrid_window`, `_hybrid_sample_metadata`, `_build_hybrid_summary`, `_build_hybrid_leakage_audit`, `_build_hybrid_teacher_audit`, `_validate_plan_for_hybrid_build`, `_limited_windows` | `HYBRID_TEACHER_AUDIT_FILENAME` |
| `core\neural_abr\inference.py` | `InferenceError`, `NeuralAbrLiteInferenceBundle` | `load_phase4_inference_bundle`, `run_phase4_inference_smoke`, `_torch_load_cpu`, `_mapping`, `_sequence`, `_candidate_sequence`, `_assert_candidate_indices_are_positions`, `_finite_scores`, `_select_position`, `_scores_are_finite` (+2) |  |
| `core\neural_abr\model.py` | `ModelError`, `NeuralAbrLiteCandidateScorer` | `masked_cross_entropy`, `predict_actions` |  |
| `core\neural_abr\model_training.py` | `CandidateModelTrainingError` | `train_phase4_candidate_model`, `load_phase4_candidate_model`, `_validate_optional_sample_limit`, `_sha256_file`, `_torch_load_cpu` |  |
| `core\neural_abr\normalization.py` | `NormalizationError`, `NormalizationStats`, `FeatureNormalizer` |  |  |
| `core\neural_abr\replay_environment.py` | `ReplayState`, `ReplayStepResult`, `ReplayEnvironmentError`, `TraceReplayEnvironment` | `_append_context_value` |  |
| `core\neural_abr\sample_schema.py` | `SampleSchemaError` | `build_label_schema`, `validate_sample`, `_mapping`, `_sequence` |  |
| `core\neural_abr\trace_sampling.py` | `Phase4TraceSamplingError`, `Phase4SamplingConfig`, `_SelectionCounters` | `build_phase4_training_trace_artifacts`, `write_phase4_training_trace_artifacts`, `validate_phase4_training_trace_plan`, `load_phase4_training_trace_plan`, `_validated_phase3_traces`, `_build_trace_windows`, `_trace_allowed_for_role`, `_window_count_for_trace`, `_window_record`, `_select_balanced_windows` (+25) | `PHASE4A_PHASE`, `TRACE_WINDOW_INDEX_SCHEMA_ID`, `TRAINING_TRACE_PLAN_SCHEMA_ID`, `SAMPLING_AUDIT_SCHEMA_ID`, `TRACE_WINDOW_INDEX_FILENAME`, `TRAINING_TRACE_PLAN_FILENAME`, `SAMPLING_AUDIT_FILENAME`, `DEFAULT_SEED` (+1) |
| `core\neural_abr\training_data.py` | `TrainingDataBuildError` | `build_phase4_training_data_from_plan`, `build_phase4_training_data_from_plan_file`, `load_trace_window`, `_samples_for_window`, `_sample_metadata`, `_build_summary`, `_build_leakage_audit`, `_validate_plan_for_data_build`, `_limited_windows` |  |
| `core\neural_abr\training_data_validation.py` | `TrainingDataValidationError` | `validate_phase4_training_data_dir` |  |
| `core\neural_abr\training_runtime.py` | `TrainingRuntimeError` | `set_training_determinism`, `batch_to_tensors`, `evaluate_candidate_scorer` |  |
| `core\neural_abr\training_smoke.py` | `TrainingSmokeError` | `run_phase4_training_smoke` |  |

### `core/output_artifacts.py`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\output_artifacts.py` |  |  | `RUN_MANIFEST_FILENAME`, `RESOLVED_CONFIG_FILENAME`, `ENVIRONMENT_FILENAME`, `RUN_LOG_FILENAME`, `SEGMENT_TELEMETRY_FILENAME`, `EVALUATION_SEGMENTS_FILENAME`, `RUN_MANIFEST_KEY`, `RESOLVED_CONFIG_KEY` (+6) |

### `core/parser`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\parser\__init__.py` |  |  |  |
| `core\parser\base.py` | `ParserBase` |  |  |
| `core\parser\dash.py` | `DashParser` |  |  |
| `core\parser\test_parser.py` |  | `main` |  |

### `core/phase45_v1`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\phase45_v1\__init__.py` |  |  |  |
| `core\phase45_v1\constants.py` |  | `no_benchmark_policy` | `PHASE45_V1_PHASE`, `DATASET_SCHEMA_ID`, `SAMPLE_SCHEMA_ID`, `SAMPLING_PLAN_SCHEMA_ID`, `SAMPLING_AUDIT_SCHEMA_ID`, `FEATURE_SCHEMA_ID`, `TARGET_SCHEMA_ID`, `LEAKAGE_AUDIT_SCHEMA_ID` (+42) |
| `core\phase45_v1\dataset.py` | `Phase45DatasetBuildError` | `build_phase45_v1_dataset`, `load_trace_window`, `_samples_for_window`, `_build_spc_targets`, `_build_audit`, `_future_throughput_stats`, `_weighted_future_values`, `_weighted_quantile`, `_sample_metadata`, `_build_summary` (+4) |  |
| `core\phase45_v1\normalization.py` | `NumericStats` | `build_train_only_normalization`, `_collect_model_input_values`, `_collect_mapping_values`, `_add_numeric`, `_numeric_stats` |  |
| `core\phase45_v1\offline_validation.py` | `Phase45OfflineValidationError`, `OfflineValidationProfile`, `GuardDecision`, `OfflineExample`, `LoadedSpbcRuntime`, `LoadedSpcRuntime`, `_VariantMetricTotals`, `_GuardMetricTotals` | `profile_by_name`, `validate_spbc_spc_offline`, `load_spbc_runtime`, `load_spc_runtime`, `apply_spc_guard`, `load_offline_examples`, `resolve_torch_device`, `_build_observation`, `_build_comparison`, `_build_offline_gate` (+18) | `OFFLINE_VALIDATION_PROFILES` |
| `core\phase45_v1\oracle.py` | `Phase45OracleError`, `OracleConfig`, `OracleDecision`, `_BeamNode` | `select_oracle_action`, `simulate_step_from_state`, `linear_reward_for_state`, `oracle_policy_card`, `_beam_sort_key`, `_fallback_decision`, `_append_context_value` |  |
| `core\phase45_v1\paths.py` | `Phase45PathError`, `PathRewriteRule` | `parse_rewrite_rule`, `parse_rewrite_rules`, `default_trace_path_rewrites`, `resolve_external_trace_path` |  |
| `core\phase45_v1\preference_dataset_v2.py` | `Phase45V2DatasetBuildError`, `Phase45V2DatasetValidationError`, `LoadedRolloutPolicy` | `build_phase45_v2_dataset`, `validate_phase45_v2_dataset_dir`, `validate_v2_sample`, `_samples_for_window`, `_build_per_action_outcomes`, `_build_preference_pairs`, `_best_immediate_action`, `_load_optional_spbc_runtime`, `_load_optional_v2_dpo_runtime`, `_select_policy_action` (+22) | `PHASE45_V2_PHASE`, `V2_DATASET_SCHEMA_ID`, `V2_DAGGER2_DATASET_SCHEMA_ID`, `V2_SAMPLE_SCHEMA_ID`, `V2_TARGET_SCHEMA_ID`, `V2_LEAKAGE_AUDIT_SCHEMA_ID`, `V2_PREFERENCE_AUDIT_SCHEMA_ID`, `SUPPORTED_V2_DATASET_SCHEMA_IDS` (+22) |
| `core\phase45_v1\profiles.py` | `Phase45ProfileError`, `DatasetProfile` | `profile_by_name` | `PROFILES` |
| `core\phase45_v1\sample_schema.py` | `Phase45SampleSchemaError` | `build_model_input_schema`, `build_target_schema`, `validate_sample`, `reject_forbidden_model_inputs`, `_validate_model_inputs`, `_require_mapping`, `_finite` |  |
| `core\phase45_v1\sampling.py` | `Phase45SamplingError`, `SamplingConfig`, `_SelectionCounters` | `build_sampling_artifacts`, `validate_sampling_plan`, `_validated_phase3_traces`, `_build_candidate_windows`, `_select_windows`, `_quota_rejection_reason`, `_window_record`, `throughput_bucket`, `variability_bucket`, `_selection_group_key` (+20) |  |
| `core\phase45_v1\spbc_spc_v2_hybrid_validation.py` | `SpbcSpcV2HybridValidationProfile`, `SpbcSpcV2HybridValidationError`, `_ModeAccumulator` | `hybrid_profile_by_name`, `validate_spbc_spc_v2_hybrid_offline`, `_evaluate_hybrid_modes`, `_spc_model_and_normalization`, `_select_veto_only`, `_select_topk_rerank`, `_is_safe_action`, `_observation_for_action`, `_is_useful_intervention`, `_hybrid_gate` (+10) | `SPBC_SPC_V2_HYBRID_VALIDATION_REPORT_FILENAME`, `SPBC_SPC_V2_HYBRID_VALIDATION_PROFILES` |
| `core\phase45_v1\spbc_training.py` | `SpbcTrainingError`, `SpbcTrainingProfile`, `SpbcExample`, `SpbcNormalizationStats`, `SpbcAbrV1Policy`, `_LossTotals`, `_PolicyMetricTotals` | `profile_by_name`, `train_spbc_abr_v1`, `load_spbc_examples`, `fit_spbc_normalization`, `examples_to_tensors`, `compute_class_weighting`, `evaluate_spbc_model`, `resolve_torch_device`, `set_training_seed`, `_run_epoch` (+20) | `SEQUENCE_FEATURES`, `SCALAR_FEATURES`, `CANDIDATE_FEATURES`, `SPBC_TRAINING_PROFILES` |
| `core\phase45_v1\spbc_v2_dpo_bundle.py` | `SpbcV2DpoBundleError` | `export_spbc_v2_dpo_inference_bundle`, `validate_spbc_v2_dpo_bundle_dir`, `write_spbc_v2_dpo_bundle_manifest`, `build_spbc_v2_dpo_feature_schema`, `build_spbc_v2_dpo_ladder_schema`, `build_spbc_v2_dpo_model_card`, `build_spbc_v2_dpo_inference_contract`, `build_spbc_v2_dpo_fallback_policy`, `sha256_file`, `bundle_file_record` (+10) | `SPBC_V2_DPO_CONTROLLER_KEY`, `SPBC_V2_DPO_CONTROLLER_ALIAS`, `SPBC_V2_DPO_CONTROLLER_DISPLAY_NAME`, `SPBC_V2_DPO_BUNDLE_SCHEMA_ID`, `SPBC_V2_DPO_BUNDLE_MANIFEST_FILENAME`, `SPBC_V2_DPO_BUNDLE_MODEL_FILENAME`, `SPBC_V2_DPO_BUNDLE_MODEL_CONFIG_FILENAME`, `SPBC_V2_DPO_BUNDLE_NORMALIZATION_FILENAME` (+8) |
| `core\phase45_v1\spbc_v2_dpo_training.py` | `SpbcV2DpoTrainingError`, `SpbcV2DpoTrainingProfile`, `PreferencePair`, `SpbcV2DpoExample`, `SpbcV2DpoNormalizationStats`, `SpbcAbrV2DpoPolicy`, `_LossTotals`, `_PolicyMetricTotals` | `profile_by_name`, `train_spbc_abr_v2_dpo`, `load_spbc_v2_dpo_examples`, `fit_spbc_v2_dpo_normalization`, `examples_to_tensors`, `evaluate_spbc_v2_dpo_model`, `resolve_torch_device`, `set_training_seed`, `_run_epoch`, `_loss_components` (+60) | `SPBC_V2_DPO_MODEL_KEY`, `SPBC_V2_DPO_MODEL_CONFIG_SCHEMA_ID`, `SPBC_V2_DPO_TRAINING_REPORT_SCHEMA_ID`, `SPBC_V2_DPO_CHECKPOINT_SCHEMA_ID`, `SPBC_V2_DPO_MODEL_FILENAME`, `SPBC_V2_DPO_MODEL_CONFIG_FILENAME`, `SPBC_V2_DPO_NORMALIZATION_FILENAME`, `SPBC_V2_DPO_TRAINING_REPORT_FILENAME` (+11) |
| `core\phase45_v1\spc_training.py` | `SpcTrainingError`, `SpcTrainingProfile`, `SpcExample`, `SpcNormalizationStats`, `SpcAbrV1Predictor`, `_MetricTotals` | `profile_by_name`, `train_spc_abr_v1`, `load_spc_examples`, `fit_spc_normalization`, `examples_to_tensors`, `evaluate_spc_model`, `resolve_torch_device`, `set_training_seed`, `_run_epoch`, `_emit_progress` (+24) | `SEQUENCE_FEATURES`, `SCALAR_FEATURES`, `CANDIDATE_FEATURES`, `QUANTILE_KEYS`, `QUANTILE_VALUES`, `SPC_TRAINING_PROFILES` |
| `core\phase45_v1\spc_v2_reward_risk_training.py` | `SpcV2RewardRiskTrainingError`, `SpcV2RewardRiskTrainingProfile`, `SpcV2RewardRiskNormalizationStats`, `SpcAbrV2RewardRiskScorer`, `_LossTotals`, `_PredictionMetricTotals`, `_ScorerMetricTotals` | `profile_by_name`, `train_spc_abr_v2_reward_risk`, `fit_spc_v2_reward_risk_normalization`, `evaluate_spc_v2_reward_risk_model`, `resolve_torch_device`, `set_training_seed`, `_load_examples_for_scorer`, `_run_epoch`, `_loss_components`, `_masked_weighted_cross_entropy` (+24) | `SPC_V2_REWARD_RISK_MODEL_KEY`, `SPC_V2_REWARD_RISK_MODEL_CONFIG_SCHEMA_ID`, `SPC_V2_REWARD_RISK_TRAINING_REPORT_SCHEMA_ID`, `SPC_V2_REWARD_RISK_CHECKPOINT_SCHEMA_ID`, `SPC_V2_REWARD_RISK_MODEL_FILENAME`, `SPC_V2_REWARD_RISK_MODEL_CONFIG_FILENAME`, `SPC_V2_REWARD_RISK_NORMALIZATION_FILENAME`, `SPC_V2_REWARD_RISK_TRAINING_REPORT_FILENAME` (+5) |
| `core\phase45_v1\validation.py` | `Phase45DatasetValidationError` | `validate_phase45_v1_dataset_dir`, `_assert_no_benchmark` |  |

### `core/phase45_v3`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\phase45_v3\__init__.py` |  | `__getattr__` |  |
| `core\phase45_v3\abr_closed_loop_env.py` | `AbrClosedLoopEnvError`, `AbrClosedLoopState`, `AbrClosedLoopStep`, `AbrClosedLoopEnv` | `default_phase45_v3_ladder`, `initial_closed_loop_state`, `simulate_closed_loop_step`, `linear_transition_reward`, `runtime_feedback_from_state`, `_append_history`, `_finite_positive` | `PHASE45_V3_DEFAULT_MAX_BUFFER_S`, `PHASE45_V3_DEFAULT_SEGMENT_DURATION_S` |
| `core\phase45_v3\closedloop_spbc_spc_dataset.py` | `Phase45V3ClosedLoopSpbcSpcDatasetError` | `build_phase45_v3_closedloop_spbc_spc_dataset`, `validate_phase45_v3_closedloop_spbc_spc_dataset_dir`, `summarize_phase45_v3_closedloop_spbc_spc_dataset`, `load_phase3_manifest`, `build_default_phase45_v3_closedloop_spbc_spc_trace_path_rewrites`, `resolve_phase45_v3_closedloop_spbc_spc_trace_path`, `_transform_qh_sample`, `_build_augmented_action_value`, `_build_spbc_spc_summary`, `_build_spbc_spc_leakage_audit` (+17) | `SPBC_SPC_DATASET_SCHEMA_ID`, `SPBC_SPC_SAMPLE_SCHEMA_ID`, `SPBC_POLICY_TARGET_ID`, `SPC_CRITIC_TARGET_ID`, `SPBC_SPC_FEATURE_SCHEMA_ID`, `SPBC_SPC_TARGET_SCHEMA_ID`, `SPBC_SPC_LEAKAGE_AUDIT_SCHEMA_ID`, `SPBC_SPC_TARGET_AUDIT_SCHEMA_ID` (+19) |
| `core\phase45_v3\constants.py` |  | `no_benchmark_policy` | `PHASE45_V3_PHASE`, `DATASET_SCHEMA_ID`, `SAMPLE_SCHEMA_ID`, `FEATURE_SCHEMA_ID`, `TARGET_SCHEMA_ID`, `LEAKAGE_AUDIT_SCHEMA_ID`, `NORMALIZATION_SCHEMA_ID`, `QH_AUDIT_SCHEMA_ID` (+23) |
| `core\phase45_v3\dataset.py` | `Phase45V3DatasetBuildError` | `build_phase45_v3_qh_dataset`, `load_phase3_manifest`, `build_default_phase45_v3_trace_path_rewrites`, `resolve_phase45_v3_trace_path`, `_samples_for_window_rollout`, `_validate_sample`, `_build_summary`, `_build_leakage_audit`, `_build_qh_audit`, `_build_feature_schema` (+15) |  |
| `core\phase45_v3\neural_mpc_bundle.py` | `Phase45V3NeuralMpcBundleError` | `export_phase45_v3_neural_mpc_experimental_bundle`, `collect_neural_mpc_candidate_readiness`, `validate_phase45_v3_neural_mpc_bundle_dir`, `write_neural_mpc_bundle_manifest`, `build_neural_mpc_model_card`, `build_neural_mpc_inference_contract`, `build_neural_mpc_fallback_policy`, `sha256_file`, `bundle_file_record`, `_canonical_seed_record` (+7) | `NEURAL_MPC_BUNDLE_SCHEMA_ID`, `NEURAL_MPC_BUNDLE_REPORT_SCHEMA_ID`, `NEURAL_MPC_BUNDLE_MANIFEST_FILENAME`, `NEURAL_MPC_BUNDLE_MODEL_FILENAME`, `NEURAL_MPC_BUNDLE_MODEL_CONFIG_FILENAME`, `NEURAL_MPC_BUNDLE_NORMALIZATION_FILENAME`, `NEURAL_MPC_BUNDLE_MODEL_CARD_FILENAME`, `NEURAL_MPC_BUNDLE_INFERENCE_CONTRACT_FILENAME` (+4) |
| `core\phase45_v3\neural_mpc_controller.py` | `Phase45V3NeuralMpcError`, `NeuralMpcDecision`, `NeuralThroughputCalibratedMpcController`, `TorchThroughputQuantilePredictor` | `plan_neural_mpc_action`, `select_throughput_plan_for_buffer`, `_score_sequence`, `_validate_prediction`, `_valid_actions`, `_nearest_quantile_index`, `_monotonicize_quantile_row`, `_normalize_vector`, `_resolve_device` | `NEURAL_MPC_CONTROLLER_KEY`, `NEURAL_MPC_V2_CONTROLLER_KEY`, `NEURAL_MPC_CONTROLLER_KEYS`, `DEFAULT_NEURAL_MPC_HORIZON`, `DEFAULT_NEURAL_MPC_QUANTILES`, `DEFAULT_REBUFFER_WEIGHT`, `DEFAULT_SWITCH_WEIGHT`, `NEURAL_MPC_Q10_BUFFER_MAX_S` (+2) |
| `core\phase45_v3\neural_mpc_evaluation.py` | `Phase45V3NeuralMpcEvaluationError` | `evaluate_phase45_v3_neural_mpc_closed_loop`, `_run_session`, `_make_controller`, `_feedback_for_classic`, `_build_metrics`, `_paired_metrics`, `_evaluate_gates`, `_high_capacity_rows`, `_high_capacity_action0_rate`, `_high_capacity_bitrates` (+7) | `NEURAL_MPC_CLOSED_LOOP_REPORT_SCHEMA_ID`, `NEURAL_MPC_CLOSED_LOOP_REPORT_FILENAME` |
| `core\phase45_v3\neural_mpc_training.py` | `Phase45V3NeuralMpcTrainingError`, `ThroughputQuantileTrainingProfile`, `ThroughputQuantileNormalization` | `throughput_quantile_training_profile_by_name`, `train_phase45_v3_throughput_quantile_predictor`, `load_throughput_quantile_examples`, `fit_throughput_quantile_normalization`, `throughput_quantile_examples_to_tensors`, `evaluate_throughput_quantile_predictor`, `_sample_to_arrays`, `_evaluate_training_gates`, `_nearest_quantile_index`, `_resolve_device` (+5) | `THROUGHPUT_QUANTILE_CHECKPOINT_SCHEMA_ID`, `THROUGHPUT_QUANTILE_TRAINING_REPORT_SCHEMA_ID`, `THROUGHPUT_QUANTILE_NORMALIZATION_SCHEMA_ID`, `THROUGHPUT_QUANTILE_MODEL_FILENAME`, `THROUGHPUT_QUANTILE_MODEL_CONFIG_FILENAME`, `THROUGHPUT_QUANTILE_NORMALIZATION_FILENAME`, `THROUGHPUT_QUANTILE_TRAINING_REPORT_FILENAME`, `THROUGHPUT_QUANTILE_TRAINING_PROFILES` |
| `core\phase45_v3\policy_collapse_audit.py` | `PolicyCollapseAuditError`, `PolicyCollapseAuditConfig` | `audit_phase6_policy_collapse`, `write_audit_json`, `_evaluate_gates`, `_resolve_result_file`, `_read_csv`, `_rows_by_session`, `_is_high_capacity_safe_row`, `_is_action0`, `_action_values`, `_time_to_reach_by_session` (+9) | `PHASE45_V3_POLICY_COLLAPSE_AUDIT_SCHEMA_ID` |
| `core\phase45_v3\profiles.py` | `Phase45V3ProfileError`, `Phase45V3DatasetProfile` | `profile_by_name` | `PROFILES` |
| `core\phase45_v3\qh_oracle.py` | `Phase45V3QhOracleError`, `QhOracleConfig`, `QhActionValue`, `QhOracleDecision`, `_BeamNode` | `evaluate_qh_actions`, `qh_oracle_card`, `_evaluate_forced_first_action`, `_best_tail_beam`, `_step_with_network`, `_action_value_sort_key`, `_beam_sort_key`, `_infeasible_action`, `_finite_json_number` | `PHASE45_V3_QH_ORACLE_ID` |
| `core\phase45_v3\qh_scorer_training.py` | `Phase45V3QhScorerTrainingError`, `QhScorerTrainingProfile`, `QhScorerNormalization`, `Phase45V3QhScorer`, `Phase45V3TemporalGruQhScorer` | `training_profile_by_name`, `train_phase45_v3_qh_scorer`, `load_qh_scorer_examples`, `fit_qh_scorer_normalization`, `examples_to_tensors`, `_build_qh_scorer_model`, `evaluate_qh_scorer`, `_loss_for_batch`, `_denormalize_q_values`, `_pairwise_qh_rank_loss` (+36) | `PHASE45_V3_QH_SCORER_MODEL_KEY`, `QH_SCORER_MODEL_CONFIG_SCHEMA_ID`, `QH_SCORER_TRAINING_REPORT_SCHEMA_ID`, `QH_SCORER_CHECKPOINT_SCHEMA_ID`, `QH_SCORER_MODEL_FILENAME`, `QH_SCORER_MODEL_CONFIG_FILENAME`, `QH_SCORER_NORMALIZATION_FILENAME`, `QH_SCORER_TRAINING_REPORT_FILENAME` (+1) |
| `core\phase45_v3\throughput_quantile_dataset.py` | `Phase45V3ThroughputQuantileDatasetError` | `build_phase45_v3_throughput_quantile_dataset`, `validate_phase45_v3_throughput_quantile_dataset_dir`, `_samples_for_window_rollout`, `_build_target`, `harmonic_mean_bps`, `_future_weighted_mean_bps`, `_weighted_future_values`, `_select_rollout_action`, `_floor_bitrate_to_action`, `_validate_sample` (+9) | `THROUGHPUT_QUANTILE_DATASET_SCHEMA_ID`, `THROUGHPUT_QUANTILE_SAMPLE_SCHEMA_ID`, `THROUGHPUT_QUANTILE_TARGET_ID`, `THROUGHPUT_QUANTILE_LEAKAGE_AUDIT_SCHEMA_ID`, `THROUGHPUT_QUANTILE_TARGET_SCHEMA_ID`, `THROUGHPUT_QUANTILE_TRAINING_DATA_FILENAME`, `THROUGHPUT_QUANTILE_VALIDATION_DATA_FILENAME`, `THROUGHPUT_QUANTILE_SUMMARY_FILENAME` (+15) |
| `core\phase45_v3\throughput_quantile_model.py` | `Phase45V3ThroughputQuantileModelError`, `ThroughputQuantilePredictor` | `pinball_quantile_loss`, `quantile_crossing_penalty`, `temporal_smoothness_penalty`, `throughput_quantile_loss`, `_validate_prediction_target` | `PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY`, `THROUGHPUT_QUANTILE_MODEL_CONFIG_SCHEMA_ID` |
| `core\phase45_v3\validation.py` | `Phase45V3ValidationError` | `validate_phase45_v3_dataset_dir`, `_sample_errors`, `_validation_result` |  |

### `core/phase6`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\phase6\__init__.py` |  |  | `PHASE6_SCHEMA_VERSION` |
| `core\phase6\analysis.py` |  | `analyze_phase6_run`, `summarize_session`, `aggregate_summaries`, `paired_statistics`, `evaluate_gates`, `build_ranking`, `generate_phase6_plots`, `render_validation_markdown`, `render_comparative_report`, `render_technical_conclusions` (+42) | `REFERENCE_CONTROLLER_ALIAS`, `PROPIOS_PREFIXES`, `PLOT_MANIFEST_FILENAME` |
| `core\phase6\catalog.py` |  | `preset_spec`, `media_profiles_for_preset`, `discover_comparable_controllers`, `controller_params`, `_safe_alias`, `_mapping`, `_list_or_empty`, `_list_or_none` | `DEFAULT_CONTROLLER_EXCLUDE`, `DEFAULT_CONTROLLER_ALIASES`, `DEFAULT_CONTROLLER_HUMAN_NAMES`, `MEDIA_PROFILES`, `PRESET_SPECS`, `PRESET_NAMES` |
| `core\phase6\config.py` |  | `load_phase6_config`, `write_phase6_example_config`, `_select_path`, `_load_mapping_file`, `_deep_merge` | `REPO_ROOT`, `DEFAULT_PHASE6_EXAMPLE_CONFIG`, `DEFAULT_PHASE6_LOCAL_CONFIG`, `DEFAULT_PHASE6_CONFIG` |
| `core\phase6\selection.py` |  | `load_trace_manifest`, `select_trace_windows`, `is_synthetic_trace`, `_passes_formal_throughput_floor`, `_balanced_pick`, `difficulty_bucket`, `_balance_key`, `_window_start_for_trace`, `_path_rewrites`, `_rewrite_path` (+4) | `SYNTHETIC_DATASET_ID`, `SYNTHETIC_SEMANTICS` |
| `core\phase6\verification.py` |  | `verify_phase6_package`, `render_phase6_verification_markdown`, `_verify_plots`, `_resolved_plot_path`, `_append_verification_to_validation_markdown`, `_check`, `_failure_reasons`, `_failure_summary`, `_plot_problem_summary`, `_synthetic_reported` (+6) | `REQUIRED_DIRS`, `REQUIRED_RESULT_FILES` |

### `core/run_context.py`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\run_context.py` | `RunContext` | `create_run_context`, `build_run_manifest`, `build_environment_snapshot`, `git_metadata`, `_create_unique_run_dir`, `_artifact_filename`, `_write_json`, `_python_info`, `_platform_info`, `_module_versions` (+9) | `SCHEMA_VERSION`, `REPO_ROOT`, `RUNTIME_MODULES`, `ANALYSIS_MODULES`, `GST_TOOLS` |

### `core/runtime_feedback.py`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\runtime_feedback.py` |  | `build_controller_feedback` |  |

### `core/trace_replay`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\trace_replay\__init__.py` |  |  |  |
| `core\trace_replay\controlled_downloader.py` | `TraceControlledDownloader` | `compact_loaded_trace_timeline`, `clip_loaded_trace_window`, `_clip_sample`, `_safe_callback` |  |
| `core\trace_replay\converters\__init__.py` |  |  |  |
| `core\trace_replay\converters\base.py` | `ConversionResult`, `BaseTraceConverter` |  |  |
| `core\trace_replay\converters\common.py` |  | `slugify`, `stable_id`, `sha256_file`, `path_text`, `find_first_file`, `iter_files_under_hint`, `parse_float`, `parse_datetime`, `median_positive_delta`, `rows_from_timestamps_and_throughput` (+2) |  |
| `core\trace_replay\converters\fcc_mba.py` | `FccMbaConverter` |  |  |
| `core\trace_replay\converters\gavist5g.py` | `Gavist5GConverter` |  |  |
| `core\trace_replay\converters\interval_logs.py` | `_IntervalLogConverter`, `NorwayHsdpaConverter`, `Ghent4GLteConverter` |  |  |
| `core\trace_replay\converters\lumos5g.py` | `Lumos5GConverter` |  |  |
| `core\trace_replay\converters\nyu_mets.py` | `NyuMetsConverter` |  |  |
| `core\trace_replay\converters\oboe.py` | `OboeConverter` |  |  |
| `core\trace_replay\converters\puffer.py` | `PufferSamplingPolicy`, `PufferConverter` | `_positive_int` |  |
| `core\trace_replay\converters\registry.py` |  | `available_converters`, `converter_by_id` | `CONVERTER_CLASSES` |
| `core\trace_replay\converters\roma.py` | `RomaActiveThroughputConverter` |  |  |
| `core\trace_replay\converters\ucc.py` | `_UccDlBitrateConverter`, `Ucc4GBeyondThroughputConverter`, `Ucc5GBeyondThroughputConverter` |  |  |
| `core\trace_replay\inventory.py` | `RawFileInventory` | `sha256_file`, `dataset_id_for_path`, `parser_hint_for_file`, `detect_columns`, `iter_raw_files`, `build_raw_dataset_inventory`, `write_raw_dataset_inventory` | `DATASET_FOLDER_HINTS` |
| `core\trace_replay\loader.py` | `TraceLoadError`, `TraceSample`, `LoadedTrace` | `_sample_from_row`, `load_normalized_trace_rows`, `load_normalized_trace_csv` |  |
| `core\trace_replay\manifest_validation.py` | `Phase3ManifestValidationError` | `validate_phase3_trace_manifest_data`, `validate_phase3_trace_manifest_file`, `_require_fields`, `_assert_close`, `_verify_source_hash` | `REQUIRED_MANIFEST_FIELDS`, `REQUIRED_TRACE_FIELDS` |
| `core\trace_replay\network_model.py` | `TraceReplayError`, `SegmentDownloadResult`, `TraceDrivenNetworkModel` | `_validate_segment_size_bytes`, `_validate_start_time_s`, `_throughput_kbps_to_bytes_per_second`, `_measured_kbps` | `END_POLICY_FAIL`, `END_POLICY_LOOP` |
| `core\trace_replay\quality.py` | `TraceQualityPolicy`, `TraceQualityAssessment` | `assess_trace_quality`, `compute_zero_fraction`, `build_quality_audit`, `build_curated_manifest`, `_counter_dict`, `_network_condition` | `DEFAULT_MIN_SAMPLES`, `DEFAULT_MIN_DURATION_S`, `DEFAULT_MOSTLY_ZERO_THRESHOLD`, `DEFAULT_EXTREME_THROUGHPUT_KBPS` |
| `core\trace_replay\schema.py` | `NormalizedTraceStats` | `has_required_columns`, `row_projection` | `NORMALIZED_TRACE_SCHEMA_ID`, `REQUIRED_COLUMNS` |
| `core\trace_replay\splits.py` |  | `stable_group_sort_key`, `_split_group_names`, `assign_splits_by_leakage_group`, `assign_stratified_splits_by_semantics`, `split_counts`, `group_counts`, `semantics_counts`, `mark_duplicates`, `build_phase3_trace_manifest` | `SPLIT_NAMES`, `DEFAULT_SPLIT_SEED`, `DEFAULT_SPLIT_STRATEGY` |
| `core\trace_replay\synthetic.py` | `SyntheticTraceSourceSpec` | `scenario_ids`, `generate_synthetic_trace_rows`, `generate_synthetic_trace_set`, `merge_synthetic_entries_into_manifest`, `_scenario_values`, `_markovian_mobile_values`, `_choose_state`, `_assign_scenario_splits`, `_counter_dict`, `_split_counts_by_scenario` (+4) | `SYNTHETIC_DATASET_ID`, `SYNTHETIC_GENERATOR_ID`, `SYNTHETIC_SEMANTICS`, `SYNTHETIC_INTENDED_USE`, `DEFAULT_SYNTHETIC_SEED`, `DEFAULT_SYNTHETIC_TRACE_DURATION_S`, `DEFAULT_SYNTHETIC_SAMPLE_DURATION_S`, `DEFAULT_SYNTHETIC_COUNT_PER_SCENARIO` (+1) |
| `core\trace_replay\validation.py` | `TraceValidationError` | `_as_float`, `validate_normalized_trace_rows`, `validate_normalized_trace_csv` |  |

### `core/utils`

| Archivo | Clases | Funciones | Constantes top-level |
|---|---|---|---|
| `core\utils\__init__.py` |  |  |  |
| `core\utils\logging.py` |  |  |  |

## Comandos y runbooks operativos

Validacion minima Windows segun aplique:

```powershell
git status --short --branch
git diff --check
python -m unittest discover
python scripts/check_client_readiness.py --strict
```

Sincronizacion Ubuntu cliente:

```bash
cd ~/TFG/DashClientModular4
git pull
```

Sincronizacion WSL2/ROCm:

```bash
wsl -d Ubuntu-24.04
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate
python3 -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

Phase 6 comparativa:

```bash
cd ~/TFG/DashClientModular4
git pull
python scripts/run_phase6_validacion_comparativa.py --preset diagnostico
python scripts/verificar_paquete_phase6.py --package-root <paquete>
```

Phase45 Neural-MPC v1/v2 config local recomendada:

```bash
cp config/phase6.neural_mpc_v1_v2.local.example.json config/phase6.local.yaml
python scripts/run_phase6_validacion_comparativa.py --config config/phase6.local.yaml --preset diagnostico
```

Runbooks WSL/Ubuntu relevantes detectados por nombre:

```text
scripts/run_phase45_v3_neural_mpc_pilot_wsl.sh
scripts/run_phase45_v3_neural_mpc_expanded_diagnostic_wsl.sh
scripts/generate_phase45_v3_neural_mpc_full_dataset_v2_wsl.sh
scripts/run_phase45_v3_neural_mpc_full_training_v2_wsl.sh
scripts/export_phase45_v3_neural_mpc_experimental_bundle_wsl.sh
scripts/export_phase45_v3_neural_mpc_experimental_bundle_v2_wsl.sh
scripts/package_phase45_v3_neural_mpc_experimental_bundle_transfer_wsl.sh
scripts/package_phase45_v3_neural_mpc_experimental_bundle_v2_transfer_wsl.sh
scripts/validate_phase45_v3_neural_mpc_experimental_bundle_ubuntu_cliente.sh
scripts/smoke_phase45_v3_neural_mpc_runtime_controller_ubuntu_cliente.sh
scripts/smoke_phase45_v3_neural_mpc_runtime_controller_v2_ubuntu_cliente.sh
```

## Paquetes Phase 6 externos detectados

Estos paquetes estan fuera del repo bajo la raiz TFG. Se documentan como evidencia de ejecuciones existentes, no como benchmark automaticamente autorizado.

| Paquete | Preset | Sesiones | Controllers | Benchmark autorizado | Ranking autorizado | Resultado MD |
|---|---|---:|---:|---|---|---|
| `20260608_160906_rapido` | `rapido` | 70 | 7 | `False` | `False` | `/home/daniel/TFG/runs_trazas/phase6/validacion_comparativa/20260608_160906_rapido/02_resultados/resultados_para_validar.md` |
| `20260608_193615_equilibrado` | `equilibrado` | 392 | 7 | `False` | `False` | `` |
| `20260611_193501_diagnostico` | `diagnostico` | 6 | 2 | `False` | `False` | `/home/daniel/TFG/runs_trazas/phase6/validacion_comparativa/20260611_193501_diagnostico/02_resultados/resultados_para_validar.md` |
| `20260611_202406_rapido` | `rapido` | 20 | 2 | `False` | `False` | `/home/daniel/TFG/runs_trazas/phase6/validacion_comparativa/20260611_202406_rapido/02_resultados/resultados_para_validar.md` |
| `20260615_110912_diagnostico` | `diagnostico` | 12 | 4 | `False` | `False` | `/home/daniel/TFG/runs_trazas/phase6/validacion_comparativa/20260615_110912_diagnostico/02_resultados/resultados_para_validar.md` |
| `20260615_112752_rapido` | `rapido` | 40 | 4 | `False` | `False` | `/home/daniel/TFG/runs_trazas/phase6/validacion_comparativa/20260615_112752_rapido/02_resultados/resultados_para_validar.md` |
| `20260615_141628_diagnostico` | `diagnostico` | 6 | 2 | `False` | `False` | `/home/daniel/TFG/runs_trazas/phase6/validacion_comparativa/20260615_141628_diagnostico/02_resultados/resultados_para_validar.md` |

## Catalogos exhaustivos

### Catalogo Markdown versionado

| # | Ruta | Bytes | Primer heading | Status/flags detectados |
|---:|---|---:|---|---|
| 1 | `docs\arquitectura y procedimientos estandar tfg dash\TFG_PLAN_GENERICO.md` | 10363 | Plan generico del TFG | Estado: cerrada.; Estado: cerrada.; Estado: cerrada. |
| 2 | `docs\arquitectura y procedimientos estandar tfg dash\arquitectura_y_procedimientos_estandar_tfg_dash.md` | 163491 | Arquitectura operativa y procedimientos estándar del TFG DASH/ABR |  |
| 3 | `docs\contexto del orquestador el chat web\CONTEXTO_MAESTRO_WEB_TFG.md` | 33378 | Contexto maestro normalizado — DashClientModular4 |  |
| 4 | `docs\contexto rama nueva\02_traces_replay\README.md` | 1360 | Phase 3 Rebuild - Traces y replay | Status: closed_on_windows_pending_ubuntu_validation. |
| 5 | `docs\contexto rama nueva\02_traces_replay\synthetic_controlled_traces.md` | 2929 | Synthetic controlled traces addendum | Status: phase3_addendum_synthetic_controlled_traces. |
| 6 | `docs\contexto rama nueva\03_qoe_reward\README.md` | 1384 | Phase 3.5 Rebuild - QoE, reward y gates | Status: closed_phase3_5_rebuild_after_validation. |
| 7 | `docs\contexto rama nueva\03_qoe_reward\evaluation_gate_policy.md` | 903 | Evaluation gate policy | Status: closed_phase3_5_rebuild_contract.; benchmark_performed=false; ranking_performed=false |
| 8 | `docs\contexto rama nueva\03_qoe_reward\no_ranking_policy.md` | 485 | No-ranking policy | Status: closed_phase3_5_rebuild_contract. |
| 9 | `docs\contexto rama nueva\03_qoe_reward\phase3_5_closure_report.md` | 1039 | Phase 3.5 Rebuild closure report | Status: closed_phase3_5_rebuild_on_windows.; ranking_performed=false; benchmark_performed=false |
| 10 | `docs\contexto rama nueva\03_qoe_reward\phase3_5_final_artifact_index.md` | 550 | Phase 3.5 artifact index | Status: closed_phase3_5_rebuild_contract. |
| 11 | `docs\contexto rama nueva\03_qoe_reward\phase3_5_results_boundary.md` | 629 | Phase 3.5 results boundary | Status: closed_phase3_5_rebuild_contract. |
| 12 | `docs\contexto rama nueva\03_qoe_reward\phase3_5_transition_to_phase4.md` | 713 | Transition to Phase 4 | Status: ready_for_phase4_planning_after_phase3_5_validation. |
| 13 | `docs\contexto rama nueva\03_qoe_reward\qoe_artifact_computation_spec.md` | 850 | QoE artifact computation spec | Status: implemented_phase3_5_rebuild.; benchmark_performed=false; ranking_performed=false |
| 14 | `docs\contexto rama nueva\03_qoe_reward\qoe_selection.md` | 786 | QoE selection | Status: closed_phase3_5_rebuild_contract. |
| 15 | `docs\contexto rama nueva\03_qoe_reward\reward_definition.md` | 903 | Reward definition | Status: closed_phase3_5_rebuild_contract. |
| 16 | `docs\contexto rama nueva\03_qoe_reward\secondary_metrics.md` | 637 | Secondary metrics | Status: closed_phase3_5_rebuild_contract. |
| 17 | `docs\contexto rama nueva\04_neural_abr\README.md` | 1943 | Phase 4 Rebuild - NeuralABR offline | Status: phase4g_closed_ready_for_phase5. |
| 18 | `docs\contexto rama nueva\04_neural_abr\phase4a_plan_de_trazas_para_entrenamiento.md` | 3830 | Phase 4A - Plan de trazas para entrenamiento | Status: implemented_on_windows_pending_ubuntu_validation.; status=PASS; benchmark_performed=false |
| 19 | `docs\contexto rama nueva\04_neural_abr\phase4bcd_datos_y_prueba_rapida_offline.md` | 3141 | Phase 4B/C/D - Datos offline y prueba rapida | Status: robust_mpc_controller_real_rebuild_in_progress.; status=PASS; benchmark_performed=false |
| 20 | `docs\contexto rama nueva\04_neural_abr\phase4e_entrenamiento_modelo_candidato.md` | 3454 | Phase 4E - Entrenamiento del modelo candidato | Status: robust_mpc_controller_real_rebuild_in_progress.; status=PASS; benchmark_performed=false |
| 21 | `docs\contexto rama nueva\04_neural_abr\phase4f_export_bundle_inferencia.md` | 2653 | Phase 4F - Export del bundle de inferencia | Status: implemented_on_windows_pending_ubuntu_validation.; status=PASS; ranking_performed=false |
| 22 | `docs\contexto rama nueva\04_neural_abr\phase4g_cierre_modelos_offline.md` | 5244 | Phase 4G - Cierre de NeuralABR-Lite offline | Status: closed_on_ubuntu. |
| 23 | `docs\contexto rama nueva\04_neural_abr\phase4h_teacher_hibrido_sin_vmaf.md` | 3170 | Phase 4H - Teacher hibrido sin VMAF |  |
| 24 | `docs\contexto rama nueva\04_neural_abr\phase5_contexto_nuevo_hilo_integracion_dos_modelos.md` | 5906 | Phase 5 - Contexto para nuevo hilo |  |
| 25 | `docs\contexto rama nueva\05_neural_controller\README.md` | 1721 | Phase 5 - Integracion de dos controllers NeuralABR-Lite | Status: closed_on_ubuntu. |
| 26 | `docs\contexto rama nueva\05_neural_controller\phase5_cierre_windows.md` | 2107 | Phase 5 - Cierre | Status: closed_on_ubuntu.; status=completed |
| 27 | `docs\contexto rama nueva\05_neural_controller\phase5_contracto_integracion_dos_controllers.md` | 1538 | Phase 5 - Contrato de integracion de dos controllers |  |
| 28 | `docs\contexto rama nueva\05_neural_controller\phase5_fallback_y_telemetria.md` | 1564 | Phase 5 - Fallback y telemetria |  |
| 29 | `docs\contexto rama nueva\05_neural_controller\phase5_feature_mapping_runtime.md` | 1951 | Phase 5 - Feature mapping runtime |  |
| 30 | `docs\contexto rama nueva\05_neural_controller\phase5_tests_y_runbook_ubuntu.md` | 2682 | Phase 5 - Tests y runbook Ubuntu |  |
| 31 | `docs\contexto rama nueva\06_validation\README.md` | 4729 | Phase 6 - Validacion Comparativa Formal | Status: implementation_ready_for_ubuntu_execution. |
| 32 | `docs\contexto rama nueva\06_validation\contexto_inicio_phase6.md` | 2844 | Contexto de Inicio para Phase 6 | Status: handoff_ready. |
| 33 | `docs\contexto rama nueva\07_memoria_defensa\README.md` | 247 | Phase 7 futura - Memoria y defensa | Status: reference_placeholder. |
| 34 | `docs\contexto rama nueva\README.md` | 1545 | Contexto rama nueva |  |
| 35 | `docs\contexto rama nueva\fase_4_5_v1\README.md` | 8688 | Fase 4-5 v1 - Iteracion nueva IA ABR |  |
| 36 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\01_comyco_2019_imitation_learning.md` | 174509 | Comyco: Quality-Aware Adaptive Video Streaming via Imitation Learning |  |
| 37 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\02_puffer_fugu_2020_learning_in_situ.md` | 236366 | Learning in situ: a randomized experiment in video streaming |  |
| 38 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\03_sabr_2025_bc_rl_finetuning.md` | 106429 | SABR: A Stable Adaptive Bitrate Framework Using Behavior Cloning Pretraining and Reinforcement Learning Fine-Tuning |  |
| 39 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\04_pll_abr_2025_ppo_lstm_attention.md` | 299572 | Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming |  |
| 40 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\05_greenabr_2022_energy_aware_drl.md` | 252896 | GreenABR: Energy-Aware Adaptive Bitrate Streaming with Deep Reinforcement Learning |  |
| 41 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\06_alvs_2022_live_video_drl.md` | 146777 | ALVS: Adaptive Live Video Streaming using deep reinforcement learning |  |
| 42 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\07_edge_rl_adaptive_streaming_2023.md` | 230513 | HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance |  |
| 43 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\08_pca_gwo_bp_mpeg_dash_ai_bitrate_selection.md` | 148843 | Bit rate selection technology of image processing based on artificial intelligence in MPEG-DASH adaptive streaming media |  |
| 44 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\09_a2br_2022_meta_rl_domain_priors.md` | 330334 | A2BR: Learning Tailored Adaptive Bitrate Algorithms to Heterogeneous Network Conditions |  |
| 45 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\10_ant_2024_network_dynamics_dedicated_models.md` | 304509 | ANT: Learning Accurate Network Dynamics for Enhanced Adaptive Video Streaming |  |
| 46 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\11_souane_2023_drl_dash.md` | 291160 | Deep Reinforcement Learning-Based Approach for Video Streaming: Dynamic Adaptive Video Streaming over HTTP |  |
| 47 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\12_beta_2025_spatial_temporal_generalization.md` | 298687 | BETA: A Novel Spatial-Temporal Learning Method for Enhancing Generalization in Adaptive Video Streaming |  |
| 48 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\13_visual_sensitivity_aware_drl_abr.md` | 296246 | A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning |  |
| 49 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\14_incendio_sabr_marl_expert_guidance.md` | 266061 | Incendio: Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance |  |
| 50 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\15_http_adaptive_streaming_review_2025.md` | 332441 | HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges |  |
| 51 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\16_learning_based_methods_has_review_2025.md` | 402707 | A Review of Learning-Based Methods for Adaptive Video Streaming Over HTTP |  |
| 52 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\17_bpa_bandwidth_prediction_drl_abr.md` | 8828922 | Enhancing Adaptive Video Streaming through Bandwidth Prediction with Deep Reinforcement Learning |  |
| 53 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\18_fortuna_2025_offline_meta_rl_diverse_networks.md` | 273436 | Fortuna - Optimizing Adaptive Video Streaming: Offline Reinforcement Learning and Meta-Learning in Diverse Networks |  |
| 54 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\19_gelato_plume_2024_trace_skew_neural_abr.md` | 283858 | Gelato / Plume - Practically High Performant Neural Adaptive Video Streaming |  |
| 55 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\20_kaken_20k14740_fair_high_qoe_multiuser_abr_report.md` | 167972 | KAKEN 20K14740 - Adaptive bitrate control strategy for ensuring high-QoE and fair video streaming in multi-user networks |  |
| 56 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\21_a2br_learning_tailored_abr_domain_priors_meta_rl.md` | 316850 | Learning Tailored Adaptive Bitrate Algorithms to Heterogeneous Network Conditions - A2BR |  |
| 57 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\22_ahaggar_bitrate_guidance_meta_rl_cmcd_cmsd.md` | 286194 | Bitrate Adaptation and Guidance With Meta Reinforcement Learning - Ahaggar |  |
| 58 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\23_causalsim_2023_unbiased_trace_driven_simulation.md` | 341353 | CausalSim - A Causal Framework for Unbiased Trace-Driven Simulation |  |
| 59 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\24_eastream_2026_environment_aware_abr_meta_rl_vae.md` | 278943 | EAStream - Environment-Aware Adaptive Bitrate Algorithm for Reliable Video Streaming Services |  |
| 60 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\25_ppo_abr_2023_proximal_policy_optimization_drl.md` | 244495 | PPO-ABR: Proximal Policy Optimization based Deep Reinforcement Learning for Adaptive BitRate streaming |  |
| 61 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\26_soda_2024_consistent_high_quality_non_neural_abr.md` | 423014 | SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming |  |
| 62 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\27_dqnreg_2022_reinforcement_learning_rate_adaptation.md` | 237855 | Reinforcement Learning-Based Rate Adaptation in Dynamic Video Streaming / DQNReg |  |
| 63 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\28_mambra_2026_session_bandwidth_prediction_ssm_mamba.md` | 277020 | MamBRA: Session-Level Bandwidth Prediction for Adaptive Video Streaming using Selective State Space Models |  |
| 64 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\29_merina_2022_meta_rl_generalization_neural_abr.md` | 341923 | MERINA: Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning |  |
| 65 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\30_metaabr_2024_meta_learning_adaptive_bitrate_selection.md` | 307461 | MetaABR: A Meta-Learning Approach on Adaptative Bitrate Selection for Video Streaming |  |
| 66 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\31_oboe_2018_auto_tuning_abr_network_conditions.md` | 304454 | Oboe: Auto-tuning Video ABR Algorithms to Network Conditions |  |
| 67 | `docs\contexto rama nueva\fase_4_5_v1\abr ia md\32_pensieve_2017_neural_adaptive_video_streaming.md` | 322181 | Pensieve: Neural Adaptive Video Streaming |  |
| 68 | `docs\contexto rama nueva\fase_4_5_v1\bloqueos\bloqueo_phase45_v3_qh_scorer_pilot_20260612.md` | 37132 | Informe objetivo de bloqueo para ayuda externa - Phase45 v3 Q_H scorer pilot | status=FAIL; status=PASS; status=PASS |
| 69 | `docs\contexto rama nueva\fase_4_5_v1\decision_phase45_v2_spbc_dpo_7b2.md` | 1747 | Decision tecnica 7B.2 - spbc_abr_v2_dpo utility/risk-aware |  |
| 70 | `docs\contexto rama nueva\fase_4_5_v1\decision_phase45_v2_spbc_dpo_7b3.md` | 2161 | Decision tecnica 7B.3 - spbc_abr_v2_dpo utility/risk multitask |  |
| 71 | `docs\contexto rama nueva\fase_4_5_v1\decision_phase45_v2_spbc_dpo_7b4_dagger2.md` | 5643 | Decision tecnica 7B.4 - DAgger-2 para spbc_abr_v2_dpo | benchmark_performed=false; ranking_performed=false; benchmark_performed=false |
| 72 | `docs\contexto rama nueva\fase_4_5_v1\decision_phase45_v2_spbc_ppo_safe_7f.md` | 3526 | Decision tecnica 7F - PPO seguro offline para SPBC |  |
| 73 | `docs\contexto rama nueva\fase_4_5_v1\decision_phase45_v2_spbc_residual_safe_rank_7d.md` | 3372 | Decision tecnica 7D - piloto SPBC residual safe-rank | benchmark_performed=false; ranking_performed=false |
| 74 | `docs\contexto rama nueva\fase_4_5_v1\decision_phase45_v2_spbc_safe_advantage_7g.md` | 2634 | Decision tecnica 7G - Safe Advantage probe para SPBC |  |
| 75 | `docs\contexto rama nueva\fase_4_5_v1\decision_phase45_v2_spc_critic_copilot_7e.md` | 3486 | Decision tecnica 7E - SPC critic/copilot calibrado |  |
| 76 | `docs\contexto rama nueva\fase_4_5_v1\decision_phase45_v2_spc_reward_risk_7c.md` | 9405 | Decision - Bloque 7C spc_abr_v2_reward_risk |  |
| 77 | `docs\contexto rama nueva\fase_4_5_v1\decision_phase45_v3_closedloop_spbc_spc_v1_20260615.md` | 5753 | Decision Phase45 v3 Closed-loop SPBC/SPC v1 - 2026-06-15 |  |
| 78 | `docs\contexto rama nueva\fase_4_5_v1\decision_phase45_v3_neural_mpc_expanded_diagnostic_20260615.md` | 12165 | Decision Phase45 v3 Neural-MPC Expanded Diagnostic - 2026-06-15 | benchmark_performed=false; ranking_performed=false; qoe_claims_authorized=false |
| 79 | `docs\contexto rama nueva\fase_4_5_v1\decision_phase45_v3_neural_mpc_experimental_candidate_20260615.md` | 5487 | Decision Phase45 v3 Neural-MPC Experimental Candidate - 2026-06-15 | benchmark_performed=false; ranking_performed=false; qoe_claims_authorized=false |
| 80 | `docs\contexto rama nueva\fase_4_5_v1\decision_phase45_v3_neural_mpc_full_v2_after_rapid_20260615.md` | 3001 | Decision Phase45 v3 Neural-MPC full v2 tras preset rapido | benchmark_performed=false; ranking_performed=false; qoe_claims_authorized=false |
| 81 | `docs\contexto rama nueva\fase_4_5_v1\decision_phase45_v3_neural_mpc_v2_bundle_after_full_training_20260615.md` | 2585 | Decision Phase45 v3 Neural-MPC v2 tras full training | benchmark_performed=false; ranking_performed=false; qoe_claims_authorized=false |
| 82 | `docs\contexto rama nueva\fase_4_5_v1\decision_phase45_v3_neural_throughput_calibrated_mpc_v1_20260612.md` | 7333 | Decision Phase45 v3 Neural Throughput-Calibrated MPC v1 - 2026-06-12 | status=PASS |
| 83 | `docs\contexto rama nueva\fase_4_5_v1\decision_phase45_v3_qh_scorer_hardneg_20260612.md` | 1768 | Decision Phase45 v3 - Q_H scorer hard-negative pilot | Estado: decision operativa para un experimento trainer-only. No es benchmark, no; status=REVIEW |
| 84 | `docs\contexto rama nueva\fase_4_5_v1\decision_phase45_v3_qh_scorer_hardneg_v2_20260612.md` | 2361 | Decision Phase45 v3 QH scorer hard-negative v2 - 2026-06-12 |  |
| 85 | `docs\contexto rama nueva\fase_4_5_v1\decision_tecnica_modelos_v1.md` | 15110 | Fase 4-5 v1 - Decision tecnica de modelos/controllers IA | Status: decision_inicial_lista_para_specs. |
| 86 | `docs\contexto rama nueva\fase_4_5_v1\informe_modelo_ia_abr_spbc_estado_y_caminos.md` | 40138 | Informe de estado para construir el controller IA ABR | status=PASS; Estado: no hay SPC aceptado que deba integrarse ya como copilot. La idea sigue; status=PASS |
| 87 | `docs\contexto rama nueva\fase_4_5_v1\proceso_desarrollo_ia_abr.md` | 7858 | Proceso estandar de desarrollo IA ABR - Fase 4-5 v1 | Estado: guia operativa obligatoria para nuevas lineas IA ABR.; benchmark_performed=false; ranking_performed=false |
| 88 | `docs\contexto rama nueva\fase_4_5_v1\runbook_phase45_v1_dataset_wsl.md` | 3072 | Runbook Phase 4-5 v1 - Dataset derivado SPC/SPBC en WSL2 |  |
| 89 | `docs\contexto rama nueva\fase_4_5_v1\runbook_phase45_v1_spc_training_wsl.md` | 2431 | Runbook Phase 4-5 v1 - Entrenamiento `spc_abr_v1` |  |
| 90 | `docs\contexto rama nueva\fase_4_5_v1\runbook_phase45_v2_dagger2_dataset_wsl.md` | 15972 | Runbook Phase 4-5 v2 - Dataset DAgger-2 para 7B |  |
| 91 | `docs\contexto rama nueva\fase_4_5_v1\runbook_phase45_v2_dataset_wsl.md` | 3425 | Runbook Phase 4-5 v2 - Dataset enriquecido preference/on-policy |  |
| 92 | `docs\contexto rama nueva\fase_4_5_v1\runbook_phase45_v2_spbc_controller_phase6.md` | 3990 | Runbook SPBC v2 DPO controller en Phase 6 |  |
| 93 | `docs\contexto rama nueva\fase_4_5_v1\runbook_phase45_v2_spbc_dpo_training_wsl.md` | 7019 | Runbook Phase 4-5 v2 - Entrenamiento spbc_abr_v2_dpo |  |
| 94 | `docs\contexto rama nueva\fase_4_5_v1\runbook_phase45_v2_spc_reward_risk_wsl.md` | 10169 | Runbook Phase 4-5 v2 - Entrenamiento spc_abr_v2_reward_risk |  |
| 95 | `docs\contexto rama nueva\fase_4_5_v1\runbook_phase45_v3_closedloop_spbc_spc_dataset_20260615.md` | 3318 | Runbook Phase45 v3 closed-loop SPBC/SPC dataset - 2026-06-15 | status=PASS |
| 96 | `docs\contexto rama nueva\fase_4_5_v1\runbook_phase45_v3_neural_mpc_bundle_ubuntu_cliente_20260615.md` | 3555 | Runbook Phase45 v3 Neural-MPC Bundle en Ubuntu Cliente - 2026-06-15 | status=PASS; benchmark_performed=false; ranking_performed=false |
| 97 | `docs\contexto rama nueva\fase_4_5_v1\runbook_phase45_v3_neural_mpc_runtime_controller_20260615.md` | 2793 | Runbook Phase45 v3 Neural-MPC Runtime Controller - 2026-06-15 | status=PASS; benchmark_performed=false; ranking_performed=false |
| 98 | `docs\contexto rama nueva\fase_4_5_v1\wsl_rocm_gpu_context.md` | 3496 | WSL2 ROCm GPU context |  |
| 99 | `docs\contexto rama nueva\fase_verificacion_cliente_y_controllers_clasicos\README.md` | 2019 | Fase de Verificacion del Cliente y Controllers Clasicos | Status: closed_on_ubuntu. |
| 100 | `docs\contexto rama nueva\fase_verificacion_cliente_y_controllers_clasicos\como_saber_que_el_cliente_funciona.md` | 1372 | Como Saber Que El Cliente Funciona |  |
| 101 | `docs\contexto rama nueva\fase_verificacion_cliente_y_controllers_clasicos\como_saber_que_no_contamina_las_pruebas.md` | 1220 | Como Saber Que No Contamina Las Pruebas |  |
| 102 | `docs\contexto rama nueva\fase_verificacion_cliente_y_controllers_clasicos\contrato_de_verificacion.md` | 1439 | Contrato de Verificacion |  |
| 103 | `docs\contexto rama nueva\fase_verificacion_cliente_y_controllers_clasicos\guia_ubuntu_paso_a_paso.md` | 1723 | Guia Ubuntu Paso A Paso | Status: accepted; Status: accepted_local_only |
| 104 | `docs\contexto rama nueva\fase_verificacion_cliente_y_controllers_clasicos\informe_final_verificacion.md` | 1705 | Informe Final de Verificacion | Status: closed_on_ubuntu. |
| 105 | `docs\contexto rama nueva\fase_verificacion_cliente_y_controllers_clasicos\verificacion_de_controllers_clasicos.md` | 2120 | Verificacion de Controllers Clasicos |  |
| 106 | `docs\contexto rama original\01_baselines\README.md` | 2521 | Baseline Selection |  |
| 107 | `docs\contexto rama original\01_baselines\_handoffs\README.md` | 374 | Handoffs And Prompts |  |
| 108 | `docs\contexto rama original\01_baselines\_handoffs\phase2_transition_to_phase3.md` | 2147 | Phase 2 To Phase 3 Transition |  |
| 109 | `docs\contexto rama original\01_baselines\_historical\README.md` | 635 | Historical Documents |  |
| 110 | `docs\contexto rama original\01_baselines\_historical\baseline_implementation_plan.md` | 7536 | Baseline Implementation Plan |  |
| 111 | `docs\contexto rama original\01_baselines\_historical\baseline_limitations.md` | 1867 | Baseline Limitations |  |
| 112 | `docs\contexto rama original\01_baselines\_historical\baseline_registry_audit.md` | 3443 | Baseline Registry Audit |  |
| 113 | `docs\contexto rama original\01_baselines\_historical\baseline_smoke_summary.md` | 2558 | Baseline Smoke Summary |  |
| 114 | `docs\contexto rama original\01_baselines\_historical\baseline_testing_summary.md` | 3232 | Baseline Testing Summary |  |
| 115 | `docs\contexto rama original\01_baselines\_historical\phase2_open_limitations_and_deferred_work.md` | 2594 | Phase 2 Open Limitations And Deferred Work |  |
| 116 | `docs\contexto rama original\01_baselines\_historical\phase2_test_validation_summary.md` | 4379 | Phase 2 Test Validation Summary |  |
| 117 | `docs\contexto rama original\01_baselines\_templates\README.md` | 479 | Templates |  |
| 118 | `docs\contexto rama original\01_baselines\_templates\acceptance_tests_template.md` | 864 | Acceptance Tests Template |  |
| 119 | `docs\contexto rama original\01_baselines\_templates\controller_api_mapping_template.md` | 992 | Controller API Mapping Template |  |
| 120 | `docs\contexto rama original\01_baselines\_templates\implementation_spec_template.md` | 1258 | Implementation Spec Template |  |
| 121 | `docs\contexto rama original\01_baselines\_templates\notes_for_memory_template.md` | 673 | Notes For Memory Template |  |
| 122 | `docs\contexto rama original\01_baselines\_templates\paper_intake_template.md` | 1012 | Paper Intake Template |  |
| 123 | `docs\contexto rama original\01_baselines\baseline_acceptance_matrix.md` | 6442 | Protocol Binding |  |
| 124 | `docs\contexto rama original\01_baselines\baseline_implementation_summary.md` | 4210 | Baseline Implementation Summary |  |
| 125 | `docs\contexto rama original\01_baselines\baseline_memory_traceability_matrix.md` | 8293 | Baseline Memory Traceability Matrix |  |
| 126 | `docs\contexto rama original\01_baselines\baseline_phase2_3_closure_report.md` | 4017 | Starting Point |  |
| 127 | `docs\contexto rama original\01_baselines\baseline_result_interpretation_policy.md` | 2321 | Baseline Result Interpretation Policy |  |
| 128 | `docs\contexto rama original\01_baselines\baseline_selection_matrix.md` | 6126 | Baseline Selection Matrix |  |
| 129 | `docs\contexto rama original\01_baselines\baseline_signal_matrix.md` | 4870 | Baseline Signal Matrix |  |
| 130 | `docs\contexto rama original\01_baselines\bba\acceptance_tests.md` | 4458 | bba Acceptance Tests | Status: implemented in `tests/test_bba_controller.py` during Phase 2.3.3. |
| 131 | `docs\contexto rama original\01_baselines\bba\controller_api_mapping.md` | 3896 | bba Controller API Mapping |  |
| 132 | `docs\contexto rama original\01_baselines\bba\implementation_spec.md` | 5128 | bba Implementation Spec |  |
| 133 | `docs\contexto rama original\01_baselines\bba\notes_for_memory.md` | 4097 | bba Notes For Memory |  |
| 134 | `docs\contexto rama original\01_baselines\bba\paper_card.md` | 1487 | Paper Card: BBA Baseline |  |
| 135 | `docs\contexto rama original\01_baselines\bba\source_evidence.md` | 7370 | Source evidence â€” BBA | Status: evidence layer only. Not an implementation spec and not runtime code. |
| 136 | `docs\contexto rama original\01_baselines\bola\acceptance_tests.md` | 4461 | bola Acceptance Tests |  |
| 137 | `docs\contexto rama original\01_baselines\bola\controller_api_mapping.md` | 4293 | bola Controller API Mapping |  |
| 138 | `docs\contexto rama original\01_baselines\bola\dashjs_practical_evidence.md` | 6258 | Practical source evidence â€” BOLA, BOLA-E, DYNAMIC, FAST SWITCHING and dash.js | Status: practical evidence layer only. Not an implementation spec and not runtime code. |
| 139 | `docs\contexto rama original\01_baselines\bola\dashjs_source_card.md` | 1785 | Source Card: dash.js Practical BOLA Source |  |
| 140 | `docs\contexto rama original\01_baselines\bola\implementation_spec.md` | 7382 | bola Implementation Spec |  |
| 141 | `docs\contexto rama original\01_baselines\bola\notes_for_memory.md` | 3726 | bola Notes For Memory |  |
| 142 | `docs\contexto rama original\01_baselines\bola\paper_card.md` | 1530 | Paper Card: BOLA Baseline |  |
| 143 | `docs\contexto rama original\01_baselines\bola\source_evidence.md` | 7919 | Source evidence â€” BOLA | Status: evidence layer only. Not an implementation spec and not runtime code. |
| 144 | `docs\contexto rama original\01_baselines\controller_academic_validation_protocol.md` | 3942 | Controller Academic Validation Protocol |  |
| 145 | `docs\contexto rama original\01_baselines\controller_code_review_checklist.md` | 2862 | Controller Code Review Checklist |  |
| 146 | `docs\contexto rama original\01_baselines\controller_implementation_readiness_gate.md` | 3386 | Controller Implementation Readiness Gate |  |
| 147 | `docs\contexto rama original\01_baselines\controller_traceability_matrix.md` | 4408 | Traceability Rule |  |
| 148 | `docs\contexto rama original\01_baselines\controller_unit_test_protocol.md` | 3595 | Controller Unit Test Protocol |  |
| 149 | `docs\contexto rama original\01_baselines\discarded_candidates.md` | 1385 | Discarded Or Deferred Candidates |  |
| 150 | `docs\contexto rama original\01_baselines\fake_smoke_validation_protocol.md` | 3225 | Fake Smoke Validation Protocol |  |
| 151 | `docs\contexto rama original\01_baselines\metric_validity_for_baselines.md` | 3251 | Metric Validity For Baselines |  |
| 152 | `docs\contexto rama original\01_baselines\mpc\acceptance_tests.md` | 5095 | mpc Acceptance Tests |  |
| 153 | `docs\contexto rama original\01_baselines\mpc\controller_api_mapping.md` | 4869 | mpc Controller API Mapping |  |
| 154 | `docs\contexto rama original\01_baselines\mpc\implementation_spec.md` | 9197 | mpc Implementation Spec |  |
| 155 | `docs\contexto rama original\01_baselines\mpc\notes_for_memory.md` | 3575 | mpc Notes For Memory |  |
| 156 | `docs\contexto rama original\01_baselines\mpc\paper_card.md` | 1533 | Paper Card: MPC Baseline |  |
| 157 | `docs\contexto rama original\01_baselines\mpc\source_evidence.md` | 8092 | Source evidence â€” MPC | Status: evidence layer only. Not an implementation spec and not runtime code. |
| 158 | `docs\contexto rama original\01_baselines\optional_candidates.md` | 1812 | Optional Candidates |  |
| 159 | `docs\contexto rama original\01_baselines\optional_methods\festive\candidate_card.md` | 1292 | Candidate Card: FESTIVE |  |
| 160 | `docs\contexto rama original\01_baselines\optional_methods\lumos\candidate_card.md` | 1202 | Candidate Card: Lumos |  |
| 161 | `docs\contexto rama original\01_baselines\optional_methods\oboe\candidate_card.md` | 1220 | Candidate Card: Oboe |  |
| 162 | `docs\contexto rama original\01_baselines\optional_methods\other_candidates.md` | 516 | Other Candidates |  |
| 163 | `docs\contexto rama original\01_baselines\optional_methods\panda\candidate_card.md` | 1210 | Candidate Card: PANDA |  |
| 164 | `docs\contexto rama original\01_baselines\optional_methods\rbc\candidate_card.md` | 864 | Candidate Card: RBC |  |
| 165 | `docs\contexto rama original\01_baselines\optional_methods\soda\candidate_card.md` | 1439 | Candidate Card: SODA |  |
| 166 | `docs\contexto rama original\01_baselines\optional_methods\soda\source_evidence.md` | 4101 | Source evidence â€” SODA optional candidate | Status: optional candidate evidence only. Not an implementation spec and not runtime code. |
| 167 | `docs\contexto rama original\01_baselines\optional_methods\wish\candidate_card.md` | 1295 | Candidate Card: WISH |  |
| 168 | `docs\contexto rama original\01_baselines\phase2_academic_validity_statement.md` | 2912 | Phase 2 Academic Validity Statement |  |
| 169 | `docs\contexto rama original\01_baselines\phase2_baseline_closure.md` | 7261 | Closure Verdict |  |
| 170 | `docs\contexto rama original\01_baselines\phase2_controller_inventory.md` | 4752 | Phase 2 Controller Inventory |  |
| 171 | `docs\contexto rama original\01_baselines\rate_based\acceptance_tests.md` | 4669 | rate_based Acceptance Tests | Status: implemented in `tests/test_rate_based_controller.py` during Phase 2.3.2. |
| 172 | `docs\contexto rama original\01_baselines\rate_based\controller_api_mapping.md` | 3944 | rate_based Controller API Mapping |  |
| 173 | `docs\contexto rama original\01_baselines\rate_based\implementation_spec.md` | 6763 | rate_based Implementation Spec |  |
| 174 | `docs\contexto rama original\01_baselines\rate_based\notes_for_memory.md` | 4570 | rate_based Notes For Memory |  |
| 175 | `docs\contexto rama original\01_baselines\rate_based\paper_card.md` | 1581 | Paper Card: Rate-Based Baseline |  |
| 176 | `docs\contexto rama original\01_baselines\rate_based\source_evidence.md` | 9184 | Source evidence â€” rate_based | Status: evidence layer only. Not an implementation spec and not runtime code. |
| 177 | `docs\contexto rama original\01_baselines\robust_mpc\acceptance_tests.md` | 5669 | robust_mpc Acceptance Tests |  |
| 178 | `docs\contexto rama original\01_baselines\robust_mpc\controller_api_mapping.md` | 5307 | robust_mpc Controller API Mapping |  |
| 179 | `docs\contexto rama original\01_baselines\robust_mpc\implementation_spec.md` | 9802 | robust_mpc Implementation Spec |  |
| 180 | `docs\contexto rama original\01_baselines\robust_mpc\notes_for_memory.md` | 3594 | robust_mpc Notes For Memory |  |
| 181 | `docs\contexto rama original\01_baselines\robust_mpc\paper_card.md` | 1701 | Paper Card: RobustMPC Baseline |  |
| 182 | `docs\contexto rama original\01_baselines\robust_mpc\pensieve_source_artifact_card.md` | 1878 | Source Artifact Card: Pensieve and RobustMPC |  |
| 183 | `docs\contexto rama original\01_baselines\robust_mpc\source_evidence.md` | 7083 | Source evidence â€” RobustMPC | Status: evidence layer only. Not an implementation spec and not runtime code. |
| 184 | `docs\contexto rama original\01_baselines\sanity_controllers\acceptance_tests.md` | 1498 | Sanity Controllers Acceptance Tests |  |
| 185 | `docs\contexto rama original\01_baselines\sanity_controllers\fixed_rate_spec.md` | 1831 | Fixed-Rate Sanity Controller Spec |  |
| 186 | `docs\contexto rama original\01_baselines\sanity_controllers\max_rate_spec.md` | 965 | Max-Rate Sanity Controller Spec |  |
| 187 | `docs\contexto rama original\01_baselines\sanity_controllers\min_rate_spec.md` | 914 | Min-Rate Sanity Controller Spec |  |
| 188 | `docs\contexto rama original\01_baselines\sanity_controllers\notes_for_memory.md` | 1070 | Sanity Controllers Notes For Memory |  |
| 189 | `docs\contexto rama original\01_baselines\source_inventory.md` | 3390 | Baseline Source Inventory |  |
| 190 | `docs\contexto rama original\02_traces_replay\README.md` | 12797 | Phase 3 Trace Replay Methodology |  |
| 191 | `docs\contexto rama original\02_traces_replay\_historical\README.md` | 1042 | Historical Documents |  |
| 192 | `docs\contexto rama original\02_traces_replay\_historical\dataset_download_plan.md` | 2837 | Dataset Download Plan |  |
| 193 | `docs\contexto rama original\02_traces_replay\_historical\phase3_2b_closure_report.md` | 1941 | Phase 3.2B Closure Report |  |
| 194 | `docs\contexto rama original\02_traces_replay\_historical\phase3_2c_closure_report.md` | 1475 | Phase 3.2C Closure Report |  |
| 195 | `docs\contexto rama original\02_traces_replay\_historical\phase3_2c_dataset_audit_summary.md` | 2962 | Phase 3.2C Dataset Audit Summary |  |
| 196 | `docs\contexto rama original\02_traces_replay\_historical\phase3_3a_closure_report.md` | 1346 | Phase 3.3A Closure Report |  |
| 197 | `docs\contexto rama original\02_traces_replay\_historical\phase3_3b_closure_report.md` | 2218 | Files Created Or Modified |  |
| 198 | `docs\contexto rama original\02_traces_replay\_historical\phase3_4a_closure_report.md` | 2415 | Phase 3.4A Closure Report |  |
| 199 | `docs\contexto rama original\02_traces_replay\_historical\phase3_4a_local_conversion_smoke_runbook.md` | 3393 | Phase 3.4A Local Conversion Smoke Runbook |  |
| 200 | `docs\contexto rama original\02_traces_replay\_historical\phase3_4b_closure_report.md` | 1525 | Phase 3.4B Closure Report |  |
| 201 | `docs\contexto rama original\02_traces_replay\_historical\phase3_4b_local_model_smoke_runbook.md` | 1477 | Phase 3.4B Local Model Smoke Runbook |  |
| 202 | `docs\contexto rama original\02_traces_replay\_historical\phase3_4c_closure_report.md` | 2229 | Phase 3.4C Closure Report |  |
| 203 | `docs\contexto rama original\02_traces_replay\_historical\phase3_4c_local_dry_run_smoke_runbook.md` | 1981 | Phase 3.4C Local Dry-Run Smoke Runbook |  |
| 204 | `docs\contexto rama original\02_traces_replay\_historical\phase3_4d_closure_report.md` | 3657 | Phase 3.4D Closure Report |  |
| 205 | `docs\contexto rama original\02_traces_replay\_historical\phase3_4d_mahimahi_runbook.md` | 2495 | Phase 3.4D Mahimahi Runbook |  |
| 206 | `docs\contexto rama original\02_traces_replay\_historical\phase3_4d_tc_netem_runbook.md` | 2083 | Phase 3.4D tc/netem Runbook |  |
| 207 | `docs\contexto rama original\02_traces_replay\_historical\phase3_memory_notes.md` | 6786 | Phase 3 Memory Notes |  |
| 208 | `docs\contexto rama original\02_traces_replay\_historical\replay_runner_requirements.md` | 6733 | Replay Runner Requirements |  |
| 209 | `docs\contexto rama original\02_traces_replay\_historical\synthetic_trace_test_plan.md` | 5506 | Synthetic Trace Test Plan |  |
| 210 | `docs\contexto rama original\02_traces_replay\_historical\trace_conversion_plan.md` | 5358 | Trace Conversion Plan |  |
| 211 | `docs\contexto rama original\02_traces_replay\_templates\README.md` | 372 | Templates |  |
| 212 | `docs\contexto rama original\02_traces_replay\_templates\method_card_template.md` | 1636 | Method Card Template |  |
| 213 | `docs\contexto rama original\02_traces_replay\_templates\trace_dataset_card_template.md` | 1729 | Trace Dataset Card Template |  |
| 214 | `docs\contexto rama original\02_traces_replay\common_trace_schema.md` | 5065 | Common Trace Schema |  |
| 215 | `docs\contexto rama original\02_traces_replay\evaluation_network_scenarios.md` | 1999 | Evaluation Network Scenarios |  |
| 216 | `docs\contexto rama original\02_traces_replay\generalization_protocol.md` | 5030 | Generalization Protocol |  |
| 217 | `docs\contexto rama original\02_traces_replay\leakage_prevention_policy.md` | 5846 | Leakage Prevention Policy |  |
| 218 | `docs\contexto rama original\02_traces_replay\mahimahi_or_alternatives.md` | 3442 | Mahimahi Or Alternatives |  |
| 219 | `docs\contexto rama original\02_traces_replay\method_cards\causalsim_trace_driven_bias.md` | 3169 | Method card — CausalSim and trace-driven simulation bias |  |
| 220 | `docs\contexto rama original\02_traces_replay\method_cards\into_the_wild_abrarena_real_world_testing.md` | 2173 | Method card — Into the Wild / ABR-Arena |  |
| 221 | `docs\contexto rama original\02_traces_replay\method_cards\mahimahi_record_replay_http.md` | 4409 | Method card — Mahimahi record-and-replay for HTTP |  |
| 222 | `docs\contexto rama original\02_traces_replay\method_cards\pensieve_trace_driven_evaluation.md` | 3114 | Method card — Pensieve trace-driven evaluation methodology |  |
| 223 | `docs\contexto rama original\02_traces_replay\method_cards\puffer_learning_in_situ.md` | 3185 | Method card — Puffer/Fugu learning in situ |  |
| 224 | `docs\contexto rama original\02_traces_replay\method_cards\tc_netem_network_emulation.md` | 2636 | Method card — Linux tc/netem network emulation |  |
| 225 | `docs\contexto rama original\02_traces_replay\method_cards\veritas_causal_queries_video_streaming_traces.md` | 2498 | Method card — Veritas causal queries from video streaming traces |  |
| 226 | `docs\contexto rama original\02_traces_replay\method_cards\wei2019_trace_based_emulation_for_abr.md` | 2814 | Method card — Wei et al. trace-based emulation for ABR throughput prediction |  |
| 227 | `docs\contexto rama original\02_traces_replay\phase3_2c_local_dataset_acquisition.md` | 4422 | Phase 3.2C Local Dataset Acquisition | Status: raw local candidate only. Not normalized, not split, not benchmark material.; Status: raw local candidate only. Not normalized, not split, not benchmark material.; Status: raw local candidate only. Not normalized, not split, not benchmark material. |
| 228 | `docs\contexto rama original\02_traces_replay\phase3_3a_synthetic_trace_schema_validation.md` | 3020 | Phase 3.3A Synthetic Trace Schema Validation |  |
| 229 | `docs\contexto rama original\02_traces_replay\phase3_3b_trace_loader.md` | 3466 | Phase 3.3B TraceLoader For Normalized Schema V1 |  |
| 230 | `docs\contexto rama original\02_traces_replay\phase3_4a_dataset_converters.md` | 5264 | Phase 3.4A Dataset Converters |  |
| 231 | `docs\contexto rama original\02_traces_replay\phase3_4b_fake_replay_adapter.md` | 1385 | Phase 3.4B Fake Replay Adapter Boundary |  |
| 232 | `docs\contexto rama original\02_traces_replay\phase3_4b_trace_driven_network_model.md` | 2732 | Phase 3.4B Trace-Driven Network Model |  |
| 233 | `docs\contexto rama original\02_traces_replay\phase3_4c_controlled_dry_runs.md` | 2860 | Phase 3.4C Controlled Trace Dry-Runs |  |
| 234 | `docs\contexto rama original\02_traces_replay\phase3_4c_controller_adapter.md` | 2298 | Phase 3.4C Controller Adapter Boundary |  |
| 235 | `docs\contexto rama original\02_traces_replay\phase3_4d_environment_probe_policy.md` | 1673 | Phase 3.4D Environment Probe Policy |  |
| 236 | `docs\contexto rama original\02_traces_replay\phase3_4d_mahimahi_tc_decision.md` | 4649 | Phase 3.4D Mahimahi/tc Decision |  |
| 237 | `docs\contexto rama original\02_traces_replay\phase3_4d_validation_boundaries.md` | 2217 | Phase 3.4D Validation Boundaries |  |
| 238 | `docs\contexto rama original\02_traces_replay\replay_emulation_decision.md` | 4926 | Replay Emulation Decision |  |
| 239 | `docs\contexto rama original\02_traces_replay\run_artifact_expectations.md` | 4921 | Future Artifact Types |  |
| 240 | `docs\contexto rama original\02_traces_replay\search_protocol.md` | 3958 | Search Protocol |  |
| 241 | `docs\contexto rama original\02_traces_replay\source_inventory.md` | 9925 | Trace Replay Source Inventory |  |
| 242 | `docs\contexto rama original\02_traces_replay\source_triage_decision.md` | 6352 | Phase 3.2A source triage decision |  |
| 243 | `docs\contexto rama original\02_traces_replay\trace_dataset_cards\fcc_measuring_broadband_america_reference.md` | 2589 | Trace dataset card — FCC Measuring Broadband America reference |  |
| 244 | `docs\contexto rama original\02_traces_replay\trace_dataset_cards\ghent_4g_lte_bandwidth_logs.md` | 3198 | Trace dataset card — Ghent 4G/LTE Bandwidth Logs |  |
| 245 | `docs\contexto rama original\02_traces_replay\trace_dataset_cards\hsdpa_norway_mmsys2013.md` | 3573 | Trace dataset card — Norway HSDPA / MMSys 2013 |  |
| 246 | `docs\contexto rama original\02_traces_replay\trace_dataset_cards\lancaster_abr_throughput_traces.md` | 2948 | Trace dataset card — Lancaster ABR-Throughput-Traces |  |
| 247 | `docs\contexto rama original\02_traces_replay\trace_dataset_cards\lumos5g_mmwave_throughput.md` | 3468 | Trace dataset card — Lumos5G mmWave throughput |  |
| 248 | `docs\contexto rama original\02_traces_replay\trace_dataset_cards\puffer_data_archive_metadata.md` | 2782 | Trace dataset card — Puffer data archive metadata |  |
| 249 | `docs\contexto rama original\02_traces_replay\trace_dataset_cards\raca_4g_lte_channel_context.md` | 3231 | Trace dataset card — Raca et al. 4G LTE channel/context dataset |  |
| 250 | `docs\contexto rama original\02_traces_replay\trace_dataset_cards\raca_5g_channel_context.md` | 3172 | Trace dataset card — Raca et al. 5G channel/context dataset |  |
| 251 | `docs\contexto rama original\02_traces_replay\trace_dataset_matrix.md` | 11802 | Trace Dataset Matrix |  |
| 252 | `docs\contexto rama original\02_traces_replay\trace_dataset_selection.md` | 6246 | Trace Dataset Selection |  |
| 253 | `docs\contexto rama original\02_traces_replay\trace_directory_layout.md` | 3018 | Trace Directory Layout |  |
| 254 | `docs\contexto rama original\02_traces_replay\trace_manifest_schema.md` | 5452 | Trace Manifest Schema |  |
| 255 | `docs\contexto rama original\02_traces_replay\trace_schema_acceptance_tests.md` | 3707 | Trace Schema Acceptance Tests |  |
| 256 | `docs\contexto rama original\02_traces_replay\trace_schema_risks_and_open_decisions.md` | 7540 | Trace Schema Risks And Open Decisions |  |
| 257 | `docs\contexto rama original\02_traces_replay\trace_source_to_internal_mapping.md` | 7336 | Trace Source To Internal Mapping |  |
| 258 | `docs\contexto rama original\02_traces_replay\trace_split_manifest_policy.md` | 2599 | Trace Split Manifest Policy |  |
| 259 | `docs\contexto rama original\02_traces_replay\trace_units_and_normalization.md` | 3375 | Trace Units And Normalization |  |
| 260 | `docs\contexto rama original\02_traces_replay\train_validation_test_ood_policy.md` | 4940 | Train Validation Test OOD Policy |  |
| 261 | `docs\contexto rama original\03_qoe_reward\README.md` | 5642 | Phase 3.5 - QoE, reward and final metric semantics |  |
| 262 | `docs\contexto rama original\03_qoe_reward\_handoffs\README.md` | 458 | Handoffs And Prompts |  |
| 263 | `docs\contexto rama original\03_qoe_reward\_handoffs\phase3_5_to_phase4_context_prompt.md` | 1568 | Phase 3.5 To Phase 4 Context Prompt |  |
| 264 | `docs\contexto rama original\03_qoe_reward\_handoffs\phase3_5_to_phase4_master_handoff.md` | 2693 | Phase 3.5 To Phase 4 Master Handoff |  |
| 265 | `docs\contexto rama original\03_qoe_reward\_handoffs\phase3_5_transition_to_phase4.md` | 1528 | Phase 3.5 Transition To Phase 4 |  |
| 266 | `docs\contexto rama original\03_qoe_reward\_historical\README.md` | 809 | Historical Documents |  |
| 267 | `docs\contexto rama original\03_qoe_reward\_historical\controlled_qoe_smoke_runbook.md` | 3202 | Controlled QoE Smoke Runbook | ranking_performed=false; benchmark_performed=false |
| 268 | `docs\contexto rama original\03_qoe_reward\_historical\phase3_5_closure_report.md` | 3810 | Phase 3.5 Closure Report |  |
| 269 | `docs\contexto rama original\03_qoe_reward\_historical\phase3_5_defense_talking_points.md` | 2609 | Phase 3.5 Defense Talking Points |  |
| 270 | `docs\contexto rama original\03_qoe_reward\_historical\phase3_5_open_limitations.md` | 1232 | Phase 3.5 Open Limitations |  |
| 271 | `docs\contexto rama original\03_qoe_reward\_historical\phase3_5_validation_summary.md` | 1265 | Phase 3.5 Validation Summary |  |
| 272 | `docs\contexto rama original\03_qoe_reward\_historical\phase3_5a0_intake_report.md` | 3249 | Phase 3.5A0 Intake Report |  |
| 273 | `docs\contexto rama original\03_qoe_reward\_historical\phase3_5a1_source_card_distillation_report.md` | 4173 | Phase 3.5A1 Source-Card Distillation Report | Status: completed documentation block. |
| 274 | `docs\contexto rama original\03_qoe_reward\_historical\phase3_5a2_qoe_reward_decision_report.md` | 2759 | Phase 3.5A2 QoE/Reward Decision Report | Status: completed documentation block. |
| 275 | `docs\contexto rama original\03_qoe_reward\_historical\phase3_5b_qoe_calculator_report.md` | 2030 | Initial Repository State | Status: completed_phase3_5b_pure_calculator. |
| 276 | `docs\contexto rama original\03_qoe_reward\_historical\phase3_5c_qoe_artifact_report.md` | 2570 | Initial Repository State | Status: completed_phase3_5c_artifact_post_processor. |
| 277 | `docs\contexto rama original\03_qoe_reward\_historical\phase3_5d_controlled_smoke_report.md` | 2849 | Initial HEAD |  |
| 278 | `docs\contexto rama original\03_qoe_reward\_templates\README.md` | 337 | Templates |  |
| 279 | `docs\contexto rama original\03_qoe_reward\_templates\source_card_template.md` | 1537 | Source card â€” TEMPLATE | Status: template |
| 280 | `docs\contexto rama original\03_qoe_reward\benchmark_result_schema.md` | 3955 | Phase 3.5A2 Benchmark Result Schema Boundary | Status: closed_phase3_5a2_documentation_contract. |
| 281 | `docs\contexto rama original\03_qoe_reward\dry_run_to_qoe_mapping.md` | 2529 | Phase 3.5C Dry-Run To QoE Mapping | Status: implemented_phase3_5c_mapping. |
| 282 | `docs\contexto rama original\03_qoe_reward\evaluation_gate_policy.md` | 3553 | Phase 3.5A2 Evaluation Gate Policy | Status: closed_phase3_5a2_documentation_contract. |
| 283 | `docs\contexto rama original\03_qoe_reward\metric_formula_catalog.md` | 3298 | Phase 3.5A2 Metric Formula Catalog | Status: closed_phase3_5a2_documentation_contract. |
| 284 | `docs\contexto rama original\03_qoe_reward\no_ranking_policy.md` | 1024 | No-Ranking Policy For Phase 3.5D |  |
| 285 | `docs\contexto rama original\03_qoe_reward\phase3_5_final_artifact_index.md` | 2528 | 1. Evidence Docs |  |
| 286 | `docs\contexto rama original\03_qoe_reward\phase3_5_results_boundary.md` | 1257 | Phase 3.5 Results Boundary |  |
| 287 | `docs\contexto rama original\03_qoe_reward\qoe_artifact_computation_spec.md` | 1621 | Scope | Status: implemented_phase3_5c_isolated_post_processor. |
| 288 | `docs\contexto rama original\03_qoe_reward\qoe_calculator_acceptance_tests.md` | 1725 | Phase 3.5B QoE Calculator Acceptance Tests | Status: implemented_phase3_5b_synthetic_tests. |
| 289 | `docs\contexto rama original\03_qoe_reward\qoe_calculator_implementation_spec.md` | 2165 | Phase 3.5B QoE Calculator Implementation Spec | Status: implemented_phase3_5b_pure_calculator. |
| 290 | `docs\contexto rama original\03_qoe_reward\qoe_evidence_matrix.md` | 5826 | Phase 3.5A2 QoE Evidence Matrix | Status: interpreted_phase3_5a2. This matrix records how A1 evidence affected the A2 contract. |
| 291 | `docs\contexto rama original\03_qoe_reward\qoe_formula_candidates.md` | 2311 | QoE Formula Candidates | Status: resolved_phase3_5a2. |
| 292 | `docs\contexto rama original\03_qoe_reward\qoe_selection.md` | 4890 | Phase 3.5A2 QoE Selection | Status: closed_phase3_5a2_documentation_contract. |
| 293 | `docs\contexto rama original\03_qoe_reward\qoe_summary_schema.md` | 1441 | Phase 3.5C QoE Summary Schema | Status: implemented_phase3_5c_artifact_schema. |
| 294 | `docs\contexto rama original\03_qoe_reward\qoe_terms_crosswalk.md` | 2372 | QoE Terms Crosswalk | Status: closed_phase3_5a2_terms. |
| 295 | `docs\contexto rama original\03_qoe_reward\reward_definition.md` | 2364 | Phase 3.5A2 Reward Definition | Status: closed_phase3_5a2_documentation_contract. |
| 296 | `docs\contexto rama original\03_qoe_reward\run_summary_schema.md` | 2510 | Phase 3.5C Run Summary Schema | Status: implemented_phase3_5c_schema. |
| 297 | `docs\contexto rama original\03_qoe_reward\search_protocol.md` | 1298 | Phase 3.5A0 Search Protocol |  |
| 298 | `docs\contexto rama original\03_qoe_reward\secondary_metrics.md` | 3392 | Phase 3.5A2 Secondary Metrics | Status: closed_phase3_5a2_documentation_contract. |
| 299 | `docs\contexto rama original\03_qoe_reward\source_cards\alsader2025_qoe_driven_streaming_6g.md` | 4031 | Source card - alsader2025 | Status: distilled_phase3_5a1 |
| 300 | `docs\contexto rama original\03_qoe_reward\source_cards\chen2024_soda_smoothness_qoe.md` | 4664 | Source card - chen2024 | Status: distilled_phase3_5a1 |
| 301 | `docs\contexto rama original\03_qoe_reward\source_cards\mao2017_pensieve_qoe_reward.md` | 4627 | Source card - mao2017 | Status: distilled_phase3_5a1 |
| 302 | `docs\contexto rama original\03_qoe_reward\source_cards\netflix_vmaf_perceptual_quality.md` | 4372 | Source card - netflixVmaf | Status: distilled_phase3_5a1 |
| 303 | `docs\contexto rama original\03_qoe_reward\source_cards\peroni2024_qoe_pitfalls_guidelines.md` | 4288 | Source card - peroni2024 | Status: distilled_phase3_5a1 |
| 304 | `docs\contexto rama original\03_qoe_reward\source_cards\peroni2025_pipeline_qoe_context.md` | 4175 | Source card - peroni2025 | Status: distilled_phase3_5a1 |
| 305 | `docs\contexto rama original\03_qoe_reward\source_cards\seufert2015_has_qoe_survey.md` | 4726 | Source card - seufert2015 | Status: distilled_phase3_5a1 |
| 306 | `docs\contexto rama original\03_qoe_reward\source_cards\spiteri2020_bola_utility_qoe.md` | 4591 | Source card - spiteri2020 | Status: distilled_phase3_5a1 |
| 307 | `docs\contexto rama original\03_qoe_reward\source_cards\timmerer2025_has_review_qoe_context.md` | 3982 | Source card - timmerer2025 | Status: distilled_phase3_5a1 |
| 308 | `docs\contexto rama original\03_qoe_reward\source_cards\yin2015_mpc_qoe_objective.md` | 4376 | Source card - yin2015 | Status: distilled_phase3_5a1 |
| 309 | `docs\contexto rama original\03_qoe_reward\source_cards\zhou2022_adaptive_streaming_quality_assessment.md` | 4705 | Source card - zhou2022 | Status: distilled_phase3_5a1 |
| 310 | `docs\contexto rama original\03_qoe_reward\source_cards\zuo2022_ruyi_user_preference_qoe.md` | 4151 | Source card - zuo2022 | Status: distilled_phase3_5a1 |
| 311 | `docs\contexto rama original\03_qoe_reward\source_inventory.md` | 3769 | Phase 3.5A1 Source Inventory |  |
| 312 | `docs\contexto rama original\03_qoe_reward\source_triage_decision.md` | 3414 | Phase 3.5A1 Source Triage Decision |  |
| 313 | `docs\contexto rama original\04_neural_abr\README.md` | 960 | Phase 4 — IA/RL ABR |  |
| 314 | `docs\contexto rama original\04_neural_abr\_handoffs\README.md` | 1076 | Handoffs And Prompts |  |
| 315 | `docs\contexto rama original\04_neural_abr\_handoffs\package1_next_steps.md` | 754 | Package 1 next steps |  |
| 316 | `docs\contexto rama original\04_neural_abr\_handoffs\package2_next_steps.md` | 1128 | Package 2 next steps |  |
| 317 | `docs\contexto rama original\04_neural_abr\_handoffs\package3_next_steps.md` | 1229 | Package 3 next steps |  |
| 318 | `docs\contexto rama original\04_neural_abr\_handoffs\phase4_to_phase5_handoff.md` | 1314 | Phase 4 to Phase 5 handoff |  |
| 319 | `docs\contexto rama original\04_neural_abr\_handoffs\phase4a1_to_phase4a2_handoff.md` | 1436 | Phase 4A1 to Phase 4A2 handoff |  |
| 320 | `docs\contexto rama original\04_neural_abr\_handoffs\phase4a2_to_phase4b_handoff.md` | 1935 | Current flow position |  |
| 321 | `docs\contexto rama original\04_neural_abr\_handoffs\phase4b_next_steps.md` | 2012 | Next steps — Phase 4B contracts |  |
| 322 | `docs\contexto rama original\04_neural_abr\_handoffs\phase4b_to_phase4c_handoff.md` | 1342 | Phase 4B to Phase 4C handoff | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 323 | `docs\contexto rama original\04_neural_abr\_handoffs\phase4c_next_steps.md` | 1127 | Phase 4C next steps | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 324 | `docs\contexto rama original\04_neural_abr\_handoffs\phase4c_to_phase4d_handoff.md` | 1380 | Phase 4C to Phase 4D handoff |  |
| 325 | `docs\contexto rama original\04_neural_abr\_handoffs\phase4d_codex_prompt_offline_pipeline.md` | 9487 | NON-NEGOTIABLE CONTEXT |  |
| 326 | `docs\contexto rama original\04_neural_abr\_handoffs\phase4d_next_steps.md` | 808 | Phase 4D next steps |  |
| 327 | `docs\contexto rama original\04_neural_abr\_handoffs\phase4d_to_phase4e_handoff.md` | 601 | Phase 4D to Phase 4E handoff |  |
| 328 | `docs\contexto rama original\04_neural_abr\_handoffs\phase4e1_codex_prompt_external_trace_dataset.md` | 7033 | Objective |  |
| 329 | `docs\contexto rama original\04_neural_abr\_handoffs\phase4e2_codex_prompt_expanded_corpus_candidate_readiness.md` | 16237 | 0. Current phase |  |
| 330 | `docs\contexto rama original\04_neural_abr\_handoffs\phase4e_codex_prompt_training_smoke_offline_validation.md` | 4731 | Phase state |  |
| 331 | `docs\contexto rama original\04_neural_abr\_handoffs\phase4e_next_steps.md` | 510 | Phase 4E next steps |  |
| 332 | `docs\contexto rama original\04_neural_abr\_handoffs\phase4e_to_phase4f_handoff.md` | 463 | Phase 4E to Phase 4F handoff |  |
| 333 | `docs\contexto rama original\04_neural_abr\_handoffs\phase4f_next_steps.md` | 373 | Phase 4F next steps |  |
| 334 | `docs\contexto rama original\04_neural_abr\_handoffs\phase4f_to_phase4g_handoff.md` | 428 | Phase 4F to Phase 4G Handoff |  |
| 335 | `docs\contexto rama original\04_neural_abr\_handoffs\phase5_context_prompt.md` | 1964 | Phase 5 context prompt |  |
| 336 | `docs\contexto rama original\04_neural_abr\_historical\README.md` | 2970 | Historical Documents |  |
| 337 | `docs\contexto rama original\04_neural_abr\_historical\neural_abr_lite_module_plan.md` | 1305 | NeuralABR-Lite module plan |  |
| 338 | `docs\contexto rama original\04_neural_abr\_historical\notes_for_memory.md` | 1371 | Phase 4 notes for memory |  |
| 339 | `docs\contexto rama original\04_neural_abr\_historical\phase4_remaining_roadmap.md` | 3184 | Phase 4 remaining roadmap after Phase 4C |  |
| 340 | `docs\contexto rama original\04_neural_abr\_historical\phase4a0_literature_intake_report.md` | 564 | phase4a0_literature_intake_report | Status: ready for closure after three PDF waves. |
| 341 | `docs\contexto rama original\04_neural_abr\_historical\phase4a1_closure_report.md` | 1544 | Phase 4A1 closure report |  |
| 342 | `docs\contexto rama original\04_neural_abr\_historical\phase4a1_package1_report.md` | 1648 | Phase 4A1 Package 1 report — core-decision source cards |  |
| 343 | `docs\contexto rama original\04_neural_abr\_historical\phase4a1_package2_report.md` | 2771 | Phase 4A1 Package 2 report — Generalization, deployment and surveys |  |
| 344 | `docs\contexto rama original\04_neural_abr\_historical\phase4a1_package3_report.md` | 1828 | Phase 4A1 Package 3 report |  |
| 345 | `docs\contexto rama original\04_neural_abr\_historical\phase4a1_source_card_report.md` | 280 | phase4a1_source_card_report | Status: draft scaffold. |
| 346 | `docs\contexto rama original\04_neural_abr\_historical\phase4a2_closure_report.md` | 1332 | Phase 4A2 closure report | Status: **ready to close after validation** |
| 347 | `docs\contexto rama original\04_neural_abr\_historical\phase4a2_method_decision_report.md` | 4619 | Phase 4A2 — Method decision report | Status: **closed as method decision, pending Phase 4B contracts** |
| 348 | `docs\contexto rama original\04_neural_abr\_historical\phase4a2_notes_for_memory.md` | 1602 | Phase 4A2 notes for memory and defense |  |
| 349 | `docs\contexto rama original\04_neural_abr\_historical\phase4b_closure_report.md` | 1297 | Phase 4B closure report | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 350 | `docs\contexto rama original\04_neural_abr\_historical\phase4b_contracts_report.md` | 2886 | Phase 4B contracts report | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 351 | `docs\contexto rama original\04_neural_abr\_historical\phase4b_notes_for_memory.md` | 1582 | Phase 4B notes for memory | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 352 | `docs\contexto rama original\04_neural_abr\_historical\phase4c_closure_report.md` | 830 | Phase 4C closure report | Status: ready to close after applying this package and passing validation. |
| 353 | `docs\contexto rama original\04_neural_abr\_historical\phase4c_notes_for_memory.md` | 945 | Phase 4C notes for memory |  |
| 354 | `docs\contexto rama original\04_neural_abr\_historical\phase4c_training_environment_report.md` | 2132 | Phase 4C — Training environment / simulator contract report | Status: draft package generated after Phase 4B validation. |
| 355 | `docs\contexto rama original\04_neural_abr\_historical\phase4d_defense_talking_points.md` | 1639 | Phase 4D defense talking points |  |
| 356 | `docs\contexto rama original\04_neural_abr\_historical\phase4d_implementation_report.md` | 4682 | Phase 4D implementation report | Status: PASS for offline pipeline implementation smoke. |
| 357 | `docs\contexto rama original\04_neural_abr\_historical\phase4d_offline_pipeline_specs_report.md` | 2025 | Phase 4D — offline training pipeline implementation specs report |  |
| 358 | `docs\contexto rama original\04_neural_abr\_historical\phase4d_open_limitations.md` | 1420 | Phase 4D open limitations |  |
| 359 | `docs\contexto rama original\04_neural_abr\_historical\phase4d_test_report.md` | 2450 | Phase 4D test report | Status: PASS for Phase 4D offline pipeline smoke. |
| 360 | `docs\contexto rama original\04_neural_abr\_historical\phase4e1_closure_report.md` | 1452 | Phase 4E.1 closure report |  |
| 361 | `docs\contexto rama original\04_neural_abr\_historical\phase4e1_dataset_manifest_summary.md` | 2827 | Phase 4E.1 dataset manifest summary |  |
| 362 | `docs\contexto rama original\04_neural_abr\_historical\phase4e1_defense_talking_points.md` | 1537 | Phase 4E.1 defense talking points |  |
| 363 | `docs\contexto rama original\04_neural_abr\_historical\phase4e1_external_trace_smoke_report.md` | 3815 | Phase 4E.1 external trace smoke report |  |
| 364 | `docs\contexto rama original\04_neural_abr\_historical\phase4e1_external_trace_split_plan.md` | 1476 | Phase 4E.1 External Trace Split Plan |  |
| 365 | `docs\contexto rama original\04_neural_abr\_historical\phase4e1_external_trace_validation_report.md` | 2275 | Phase 4E.1 external trace validation report |  |
| 366 | `docs\contexto rama original\04_neural_abr\_historical\phase4e1_open_limitations.md` | 1312 | Phase 4E.1 open limitations |  |
| 367 | `docs\contexto rama original\04_neural_abr\_historical\phase4e1_trace_data_intake_report.md` | 4065 | Phase 4E.1 Trace Data Intake Report |  |
| 368 | `docs\contexto rama original\04_neural_abr\_historical\phase4e1_validation_commands_ubuntu.md` | 608 | Phase 4E.1 Ubuntu Validation Commands |  |
| 369 | `docs\contexto rama original\04_neural_abr\_historical\phase4e1_windows_commands.md` | 2771 | Apply package |  |
| 370 | `docs\contexto rama original\04_neural_abr\_historical\phase4e2_candidate_readiness_report.md` | 2343 | Phase 4E.2 Candidate Readiness Report |  |
| 371 | `docs\contexto rama original\04_neural_abr\_historical\phase4e2_closure_report.md` | 1046 | Phase 4E.2 Closure Report |  |
| 372 | `docs\contexto rama original\04_neural_abr\_historical\phase4e2_defense_material_requirements.md` | 661 | Phase 4E.2 defense material requirements |  |
| 373 | `docs\contexto rama original\04_neural_abr\_historical\phase4e2_expanded_corpus_plan.md` | 1110 | Phase 4E.2 — Expanded external corpus plan |  |
| 374 | `docs\contexto rama original\04_neural_abr\_historical\phase4e2_open_limitations.md` | 810 | Phase 4E.2 Open Limitations |  |
| 375 | `docs\contexto rama original\04_neural_abr\_historical\phase4e2_repair_report.md` | 2606 | Phase 4E.2 Repair Report |  |
| 376 | `docs\contexto rama original\04_neural_abr\_historical\phase4e2_trace_corpus_requirements.md` | 680 | Phase 4E.2 trace corpus requirements |  |
| 377 | `docs\contexto rama original\04_neural_abr\_historical\phase4e2_training_runbook_plain_language.md` | 838 | Phase 4E.2 training runbook, plain language |  |
| 378 | `docs\contexto rama original\04_neural_abr\_historical\phase4e2_validation_commands_ubuntu.md` | 490 | Phase 4E.2 Ubuntu validation |  |
| 379 | `docs\contexto rama original\04_neural_abr\_historical\phase4e2_validation_report.md` | 661 | Phase 4E.2 Validation Report |  |
| 380 | `docs\contexto rama original\04_neural_abr\_historical\phase4e2_windows_commands.md` | 1813 | Phase 4E.2 Windows commands |  |
| 381 | `docs\contexto rama original\04_neural_abr\_historical\phase4e_artifact_manifest.md` | 2022 | Phase 4E artifact manifest |  |
| 382 | `docs\contexto rama original\04_neural_abr\_historical\phase4e_closure_report.md` | 1516 | Phase 4E closure report |  |
| 383 | `docs\contexto rama original\04_neural_abr\_historical\phase4e_defense_material_requirements.md` | 811 | Phase 4E — Defense material requirements |  |
| 384 | `docs\contexto rama original\04_neural_abr\_historical\phase4e_defense_talking_points.md` | 1664 | Phase 4E defense talking points |  |
| 385 | `docs\contexto rama original\04_neural_abr\_historical\phase4e_model_card_draft.md` | 2364 | Phase 4E model card draft |  |
| 386 | `docs\contexto rama original\04_neural_abr\_historical\phase4e_model_selection_notes.md` | 1512 | Phase 4E model selection notes |  |
| 387 | `docs\contexto rama original\04_neural_abr\_historical\phase4e_offline_validation_report.md` | 2434 | Phase 4E offline validation report |  |
| 388 | `docs\contexto rama original\04_neural_abr\_historical\phase4e_open_limitations.md` | 1445 | Phase 4E open limitations |  |
| 389 | `docs\contexto rama original\04_neural_abr\_historical\phase4e_trace_usage_plan.md` | 1140 | Phase 4E — Trace usage plan |  |
| 390 | `docs\contexto rama original\04_neural_abr\_historical\phase4e_training_commands_windows.md` | 2579 | Phase 4E — Windows command runbook |  |
| 391 | `docs\contexto rama original\04_neural_abr\_historical\phase4e_training_runbook_plain_language.md` | 2335 | Phase 4E — Plain-language training runbook |  |
| 392 | `docs\contexto rama original\04_neural_abr\_historical\phase4e_training_smoke_plan.md` | 1773 | Phase 4E — Training smoke + offline validation plan |  |
| 393 | `docs\contexto rama original\04_neural_abr\_historical\phase4e_training_smoke_report.md` | 4060 | Phase 4E training smoke report |  |
| 394 | `docs\contexto rama original\04_neural_abr\_historical\phase4e_validation_commands_ubuntu.md` | 642 | Phase 4E — Ubuntu validation commands |  |
| 395 | `docs\contexto rama original\04_neural_abr\_historical\phase4f_bundle_validation_report.md` | 2075 | Phase 4F Bundle Validation Report |  |
| 396 | `docs\contexto rama original\04_neural_abr\_historical\phase4f_closure_report.md` | 790 | Phase 4F Closure Report |  |
| 397 | `docs\contexto rama original\04_neural_abr\_historical\phase4f_defense_talking_points.md` | 1537 | Phase 4F Defense Talking Points |  |
| 398 | `docs\contexto rama original\04_neural_abr\_historical\phase4f_export_report.md` | 679 | Phase 4F Export Report |  |
| 399 | `docs\contexto rama original\04_neural_abr\_historical\phase4f_export_validation_plan.md` | 664 | Phase 4F export validation plan |  |
| 400 | `docs\contexto rama original\04_neural_abr\_historical\phase4f_inference_latency_report.md` | 446 | Phase 4F Inference Latency Report |  |
| 401 | `docs\contexto rama original\04_neural_abr\_historical\phase4f_inference_smoke_report.md` | 379 | Phase 4F Inference Smoke Report |  |
| 402 | `docs\contexto rama original\04_neural_abr\_historical\phase4f_memory_defense_requirements.md` | 734 | Phase 4F memory and defense requirements |  |
| 403 | `docs\contexto rama original\04_neural_abr\_historical\phase4f_open_limitations.md` | 906 | Phase 4F Open Limitations |  |
| 404 | `docs\contexto rama original\04_neural_abr\_historical\phase4f_repair_report.md` | 1433 | Phase 4F-R1 Repair Report |  |
| 405 | `docs\contexto rama original\04_neural_abr\_historical\phase4g_final_limitations.md` | 1237 | Phase 4G final limitations |  |
| 406 | `docs\contexto rama original\04_neural_abr\_historical\phase4g_memory_defense_summary.md` | 2560 | Phase 4G memory and defense summary |  |
| 407 | `docs\contexto rama original\04_neural_abr\_historical\phase5a0_literature_delta_plan.md` | 4027 | Phase 5A0 literature delta plan |  |
| 408 | `docs\contexto rama original\04_neural_abr\_templates\README.md` | 540 | Templates |  |
| 409 | `docs\contexto rama original\04_neural_abr\_templates\phase4d_closure_report_template.md` | 445 | Phase 4D closure report template |  |
| 410 | `docs\contexto rama original\04_neural_abr\_templates\phase4e_model_card_template.md` | 645 | Phase 4E model card draft |  |
| 411 | `docs\contexto rama original\04_neural_abr\_templates\phase4e_offline_validation_report_template.md` | 615 | Phase 4E offline validation report template |  |
| 412 | `docs\contexto rama original\04_neural_abr\_templates\phase4e_training_report_template.md` | 835 | Phase 4E training smoke report |  |
| 413 | `docs\contexto rama original\04_neural_abr\_templates\phase4f_closure_report_template.md` | 613 | Phase 4F closure report template |  |
| 414 | `docs\contexto rama original\04_neural_abr\_templates\source_card_template.md` | 1088 | Bibliographic data |  |
| 415 | `docs\contexto rama original\04_neural_abr\action_space_decision.md` | 1422 | Action space decision | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 416 | `docs\contexto rama original\04_neural_abr\artifact_policy_phase4b.md` | 1418 | Phase 4B artifact policy | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 417 | `docs\contexto rama original\04_neural_abr\candidate_representation_scoring_contract.md` | 2282 | Candidate representation scoring contract | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 418 | `docs\contexto rama original\04_neural_abr\cli_and_artifact_contract_phase4d.md` | 962 | CLI and artifact contract for Phase 4D |  |
| 419 | `docs\contexto rama original\04_neural_abr\content_ladder_contract.md` | 1181 | Content ladder and segment table contract |  |
| 420 | `docs\contexto rama original\04_neural_abr\content_ladder_implementation_spec.md` | 995 | Content ladder implementation spec |  |
| 421 | `docs\contexto rama original\04_neural_abr\dataset_builder_contract.md` | 1185 | Dataset builder contract |  |
| 422 | `docs\contexto rama original\04_neural_abr\dataset_builder_implementation_spec.md` | 1242 | Dataset builder implementation spec |  |
| 423 | `docs\contexto rama original\04_neural_abr\dataset_schema_contract.md` | 2057 | Dataset schema contract | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 424 | `docs\contexto rama original\04_neural_abr\defendibility_acceptance_gates.md` | 2740 | Defendibility and acceptance gates |  |
| 425 | `docs\contexto rama original\04_neural_abr\environment_acceptance_tests.md` | 1614 | Phase 4C environment acceptance tests |  |
| 426 | `docs\contexto rama original\04_neural_abr\fallback_policy_preintegration.md` | 1621 | Fallback policy pre-integration contract | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 427 | `docs\contexto rama original\04_neural_abr\feature_availability_contract.md` | 2419 | Feature availability contract | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 428 | `docs\contexto rama original\04_neural_abr\feature_builder_implementation_spec.md` | 1004 | Feature builder implementation spec |  |
| 429 | `docs\contexto rama original\04_neural_abr\fugu_lite_backup_comparator_decision.md` | 1361 | Backup/comparator decision: Fugu-lite predictor + policy | Status: **retained as backup/comparator, not selected as primary** |
| 430 | `docs\contexto rama original\04_neural_abr\hardware_cpu_first_contract.md` | 1409 | Hardware CPU-first contract | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 431 | `docs\contexto rama original\04_neural_abr\implementation_go_no_go_policy.md` | 1519 | Implementation go/no-go policy |  |
| 432 | `docs\contexto rama original\04_neural_abr\leakage_audit_protocol.md` | 1009 | Leakage audit protocol |  |
| 433 | `docs\contexto rama original\04_neural_abr\leakage_prevention_for_ia.md` | 2103 | Leakage prevention for IA | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 434 | `docs\contexto rama original\04_neural_abr\memory_defense_traceability_phase4d.md` | 1053 | Required implementation docs after Codex |  |
| 435 | `docs\contexto rama original\04_neural_abr\method_acceptance_gates.md` | 1478 | Phase 4A2 method acceptance gates |  |
| 436 | `docs\contexto rama original\04_neural_abr\method_decision_record.md` | 3544 | Method decision record — NeuralABR-Lite Candidate Scorer | Status: **Accepted for specification** |
| 437 | `docs\contexto rama original\04_neural_abr\method_feasibility_matrix.md` | 1648 | Phase 4 method feasibility matrix |  |
| 438 | `docs\contexto rama original\04_neural_abr\method_to_contract_traceability.md` | 1771 | Method-to-contract traceability | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 439 | `docs\contexto rama original\04_neural_abr\model_training_implementation_spec.md` | 1078 | Model and training implementation spec |  |
| 440 | `docs\contexto rama original\04_neural_abr\network_regime_contract.md` | 1307 | Network regime contract |  |
| 441 | `docs\contexto rama original\04_neural_abr\neural_abr_design_intent.md` | 3402 | NeuralABR-Lite design intent |  |
| 442 | `docs\contexto rama original\04_neural_abr\neural_abr_lite_candidate_scorer_decision.md` | 2409 | Decision: NeuralABR-Lite Candidate Scorer | Status: **selected as primary Phase 4 method** |
| 443 | `docs\contexto rama original\04_neural_abr\neural_evidence_matrix.md` | 4833 | Neural ABR evidence matrix | Status: final A1 matrix after Package 1 + Package 2 + Package 3 |
| 444 | `docs\contexto rama original\04_neural_abr\neural_method_selection.md` | 2511 | Neural method selection | Status: **selected method family for Phase 4B specs** |
| 445 | `docs\contexto rama original\04_neural_abr\neural_methods_crosswalk.md` | 2208 | Neural methods crosswalk |  |
| 446 | `docs\contexto rama original\04_neural_abr\normalization_contract.md` | 1901 | Normalization contract | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 447 | `docs\contexto rama original\04_neural_abr\normalization_implementation_spec.md` | 512 | Normalization implementation spec |  |
| 448 | `docs\contexto rama original\04_neural_abr\normalization_pipeline_contract.md` | 917 | Normalization pipeline contract |  |
| 449 | `docs\contexto rama original\04_neural_abr\offline_pipeline_architecture_spec.md` | 1488 | Offline pipeline architecture spec |  |
| 450 | `docs\contexto rama original\04_neural_abr\offline_validation_protocol.md` | 1492 | Offline validation protocol |  |
| 451 | `docs\contexto rama original\04_neural_abr\phase4c_artifact_layout.md` | 1213 | Phase 4C artifact layout |  |
| 452 | `docs\contexto rama original\04_neural_abr\phase4d_artifact_policy.md` | 611 | Phase 4D artifact policy |  |
| 453 | `docs\contexto rama original\04_neural_abr\phase4d_code_traceability_matrix.md` | 5913 | Phase 4D code traceability matrix |  |
| 454 | `docs\contexto rama original\04_neural_abr\phase4d_coderun_logging_protocol.md` | 562 | Phase 4D Codex/code-run logging protocol |  |
| 455 | `docs\contexto rama original\04_neural_abr\phase4d_go_no_go_gates.md` | 870 | Phase 4D go/no-go gates |  |
| 456 | `docs\contexto rama original\04_neural_abr\phase4e1_acceptance_gates.md` | 1485 | Phase 4E.1 Acceptance Gates |  |
| 457 | `docs\contexto rama original\04_neural_abr\phase4e1_external_trace_model_card.md` | 2778 | Phase 4E.1 external trace model card |  |
| 458 | `docs\contexto rama original\04_neural_abr\phase4e1_no_phase4f_yet.md` | 769 | Phase 4E.1 No Phase 4F Yet |  |
| 459 | `docs\contexto rama original\04_neural_abr\phase4e1_phase3_trace_reuse_decision.md` | 2747 | Phase 4E.1 Phase 3 Trace Reuse Decision |  |
| 460 | `docs\contexto rama original\04_neural_abr\phase4e1_qoe_reward_context_reconciliation.md` | 1366 | Phase 4E.1 QoE/Reward Context Reconciliation |  |
| 461 | `docs\contexto rama original\04_neural_abr\phase4e1_to_phase4f_gate.md` | 927 | Phase 4E.1 to Phase 4F Gate |  |
| 462 | `docs\contexto rama original\04_neural_abr\phase4e2_candidate_readiness_gate.md` | 1489 | Phase 4E.2 candidate-readiness gate |  |
| 463 | `docs\contexto rama original\04_neural_abr\phase4e2_model_card.md` | 796 | Phase 4E.2 Model Card |  |
| 464 | `docs\contexto rama original\04_neural_abr\phase4e2_no_phase4f_yet.md` | 343 | Phase 4F remains blocked before Phase 4E.2 gate |  |
| 465 | `docs\contexto rama original\04_neural_abr\phase4e2_to_phase4f_gate.md` | 506 | Phase 4E.2 to Phase 4F gate |  |
| 466 | `docs\contexto rama original\04_neural_abr\phase4e_model_acceptance_gates.md` | 1212 | Phase 4E — Model acceptance gates |  |
| 467 | `docs\contexto rama original\04_neural_abr\phase4e_no_benchmark_policy.md` | 535 | Phase 4E — No-benchmark policy |  |
| 468 | `docs\contexto rama original\04_neural_abr\phase4f_bundle_contract.md` | 1148 | Phase 4F bundle contract |  |
| 469 | `docs\contexto rama original\04_neural_abr\phase4f_export_inference_contract_report.md` | 753 | Phase 4F — export/inference contract report | Status: scaffold for Phase 4F. |
| 470 | `docs\contexto rama original\04_neural_abr\phase4f_go_no_go_gates.md` | 842 | Phase 4F go/no-go gates |  |
| 471 | `docs\contexto rama original\04_neural_abr\phase4f_inference_api_contract.md` | 998 | Phase 4F inference API contract |  |
| 472 | `docs\contexto rama original\04_neural_abr\phase4f_latency_and_determinism_contract.md` | 541 | Phase 4F latency and determinism contract |  |
| 473 | `docs\contexto rama original\04_neural_abr\phase4f_model_card.md` | 670 | Phase 4F Model Card |  |
| 474 | `docs\contexto rama original\04_neural_abr\phase4f_no_client_integration_policy.md` | 629 | Phase 4F no-client-integration policy |  |
| 475 | `docs\contexto rama original\04_neural_abr\phase4g_bundle_acceptance_record.md` | 1396 | Phase 4G bundle acceptance record |  |
| 476 | `docs\contexto rama original\04_neural_abr\phase4g_closure_report.md` | 4089 | Phase 4G closure report — NeuralABR-Lite | Status: **CLOSED pending repository application/validation**. |
| 477 | `docs\contexto rama original\04_neural_abr\phase4g_go_no_go_decision.md` | 1657 | Phase 4G go/no-go decision |  |
| 478 | `docs\contexto rama original\04_neural_abr\phase4g_phase5_integration_gate.md` | 1104 | Phase 4G Phase 5 integration gate |  |
| 479 | `docs\contexto rama original\04_neural_abr\replay_engine_contract.md` | 1515 | Replay engine contract |  |
| 480 | `docs\contexto rama original\04_neural_abr\replay_environment_implementation_spec.md` | 1121 | Replay environment implementation spec |  |
| 481 | `docs\contexto rama original\04_neural_abr\reward_usage_contract.md` | 1927 | Reward usage contract | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 482 | `docs\contexto rama original\04_neural_abr\risk_register.md` | 1868 | Phase 4 neural ABR risk register |  |
| 483 | `docs\contexto rama original\04_neural_abr\sample_generation_contract.md` | 1483 | Supervised sample generation contract |  |
| 484 | `docs\contexto rama original\04_neural_abr\simulator_determinism_contract.md` | 843 | Simulator determinism contract |  |
| 485 | `docs\contexto rama original\04_neural_abr\simulator_vs_client_boundary.md` | 1660 | Simulator vs client boundary |  |
| 486 | `docs\contexto rama original\04_neural_abr\source_cards\a2br2022_meta_rl.md` | 4967 | Source card: a2br2022_meta_rl |  |
| 487 | `docs\contexto rama original\04_neural_abr\source_cards\ababR_search_note.md` | 864 | Source note: ababR_search_note |  |
| 488 | `docs\contexto rama original\04_neural_abr\source_cards\abrl_facebook2020_real_world_rl.md` | 5754 | Source card: abrl_facebook2020_real_world_rl |  |
| 489 | `docs\contexto rama original\04_neural_abr\source_cards\ahaggar2024_bitrate_guidance.md` | 4776 | Source card: ahaggar2024_bitrate_guidance |  |
| 490 | `docs\contexto rama original\04_neural_abr\source_cards\airl2025_inverse_rl.md` | 3535 | Source card: airl2025_inverse_rl |  |
| 491 | `docs\contexto rama original\04_neural_abr\source_cards\ant2024_network_dynamics.md` | 3298 | Source card: ant2024_network_dynamics |  |
| 492 | `docs\contexto rama original\04_neural_abr\source_cards\beta2025_spatial_temporal_generalization.md` | 3862 | Source card: beta2025_spatial_temporal_generalization |  |
| 493 | `docs\contexto rama original\04_neural_abr\source_cards\causalsim2023_unbiased_trace_simulation.md` | 4632 | Source card: causalsim2023_unbiased_trace_simulation |  |
| 494 | `docs\contexto rama original\04_neural_abr\source_cards\comyco2020_lifelong_imitation_learning.md` | 5976 | Source card: comyco2020_lifelong_imitation_learning |  |
| 495 | `docs\contexto rama original\04_neural_abr\source_cards\eastream2026_environment_aware.md` | 3841 | Source card: eastream2026_environment_aware |  |
| 496 | `docs\contexto rama original\04_neural_abr\source_cards\fortuna2025_offline_meta_rl.md` | 4346 | Source card: fortuna2025_offline_meta_rl |  |
| 497 | `docs\contexto rama original\04_neural_abr\source_cards\http_adaptive_streaming_review2025.md` | 1871 | Source card: http_adaptive_streaming_review2025 |  |
| 498 | `docs\contexto rama original\04_neural_abr\source_cards\into_the_wild2025_real_world_testing.md` | 3738 | Source card: into_the_wild2025_real_world_testing |  |
| 499 | `docs\contexto rama original\04_neural_abr\source_cards\merina2022_meta_rl_generalization.md` | 5083 | Source card: merina2022_meta_rl_generalization |  |
| 500 | `docs\contexto rama original\04_neural_abr\source_cards\metaabr2024_meta_learning.md` | 4535 | Source card: metaabr2024_meta_learning |  |
| 501 | `docs\contexto rama original\04_neural_abr\source_cards\nmoeabr2026_mixture_of_experts.md` | 3182 | Source card: nmoeabr2026_mixture_of_experts |  |
| 502 | `docs\contexto rama original\04_neural_abr\source_cards\oboe2018_autotuning_abr.md` | 4757 | Source card: oboe2018_autotuning_abr |  |
| 503 | `docs\contexto rama original\04_neural_abr\source_cards\pensieve2017_neural_abr.md` | 5909 | Source card: pensieve2017_neural_abr |  |
| 504 | `docs\contexto rama original\04_neural_abr\source_cards\plume_gelato2024_trace_skew.md` | 5213 | Source card: plume_gelato2024_trace_skew |  |
| 505 | `docs\contexto rama original\04_neural_abr\source_cards\ppo_abr_search_note.md` | 727 | Source note: ppo_abr_search_note |  |
| 506 | `docs\contexto rama original\04_neural_abr\source_cards\puffer_fugu2020_learning_in_situ.md` | 5573 | Source card: puffer_fugu2020_learning_in_situ |  |
| 507 | `docs\contexto rama original\04_neural_abr\source_cards\sabr2025_bc_rl_finetuning.md` | 5129 | Source card: sabr2025_bc_rl_finetuning |  |
| 508 | `docs\contexto rama original\04_neural_abr\source_cards\soda2024_smoothness_controller.md` | 4525 | Source card: soda2024_smoothness_controller |  |
| 509 | `docs\contexto rama original\04_neural_abr\source_cards\survey_learning_has2025.md` | 3459 | Source card: survey_learning_has2025 |  |
| 510 | `docs\contexto rama original\04_neural_abr\source_cards\survey_pipeline2025.md` | 3220 | Source card: survey_pipeline2025 |  |
| 511 | `docs\contexto rama original\04_neural_abr\source_inventory.md` | 919 | Wave 1 — Core decision |  |
| 512 | `docs\contexto rama original\04_neural_abr\state_representation.md` | 4670 | State representation contract | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 513 | `docs\contexto rama original\04_neural_abr\synthetic_sanity_trace_contract.md` | 905 | Synthetic sanity trace contract |  |
| 514 | `docs\contexto rama original\04_neural_abr\teacher_policy_contract.md` | 2326 | Teacher policy contract | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 515 | `docs\contexto rama original\04_neural_abr\teacher_policy_implementation_spec.md` | 1041 | Teacher policy implementation spec |  |
| 516 | `docs\contexto rama original\04_neural_abr\teacher_replay_environment_contract.md` | 1414 | Teacher replay environment contract |  |
| 517 | `docs\contexto rama original\04_neural_abr\tests_acceptance_phase4d.md` | 1459 | Phase 4D tests and acceptance |  |
| 518 | `docs\contexto rama original\04_neural_abr\trace_conversion_contract.md` | 1424 | Trace conversion contract |  |
| 519 | `docs\contexto rama original\04_neural_abr\trace_format_contract.md` | 1689 | Trace format contract |  |
| 520 | `docs\contexto rama original\04_neural_abr\trace_manifest_contract.md` | 1321 | Trace manifest contract |  |
| 521 | `docs\contexto rama original\04_neural_abr\trace_schema_implementation_spec.md` | 1139 | Trace schema implementation spec |  |
| 522 | `docs\contexto rama original\04_neural_abr\trace_split_contract.md` | 2052 | Trace split contract | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 523 | `docs\contexto rama original\04_neural_abr\training_acceptance_tests.md` | 1546 | Training acceptance tests contract | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 524 | `docs\contexto rama original\04_neural_abr\training_data_contract.md` | 2538 | Training data contract | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 525 | `docs\contexto rama original\04_neural_abr\training_environment_spec.md` | 2412 | Training environment specification |  |
| 526 | `docs\contexto rama original\04_neural_abr\validation_sanity_contract.md` | 1727 | Validation sanity contract | Status: repo-ready contract draft generated after Phase 4A0/A1/A2. |
| 527 | `docs\contexto rama original\04_neural_abr\why_not_large_models_moe_transformers.md` | 979 | Why not large models, MoE or transformer-like ABR as base | Status: **large neural ABR rejected as Phase 4 base** |
| 528 | `docs\contexto rama original\04_neural_abr\why_not_meta_rl_full.md` | 1143 | Why not full meta-RL as base | Status: **full meta-RL rejected as Phase 4 base** |
| 529 | `docs\contexto rama original\04_neural_abr\why_not_offline_rl_full.md` | 1125 | Why not full offline RL as base | Status: **full offline RL rejected as Phase 4 base** |
| 530 | `docs\contexto rama original\04_neural_abr\why_not_ppo_first.md` | 1383 | Why not PPO-first | Status: **PPO-first rejected as Phase 4 base** |
| 531 | `docs\contexto rama original\04_neural_abr\why_not_reward_learning.md` | 943 | Why not reward learning / AIRL as base | Status: **reward learning rejected as Phase 4 base** |
| 532 | `docs\contexto rama original\05_neural_controller_integration\README.md` | 4085 | Phase 5 NeuralABR-Lite controller integration |  |
| 533 | `docs\contexto rama original\05_neural_controller_integration\_handoffs\README.md` | 416 | Handoffs And Prompts |  |
| 534 | `docs\contexto rama original\05_neural_controller_integration\_handoffs\phase5c_phase5d_codex_prompt.md` | 7170 | Phase 5D Codex implementation prompt |  |
| 535 | `docs\contexto rama original\05_neural_controller_integration\_handoffs\phase5g_closed_phase_handoff_stub.md` | 2282 | Current validated HEAD | Status: PASS. |
| 536 | `docs\contexto rama original\05_neural_controller_integration\_historical\README.md` | 995 | Historical Documents |  |
| 537 | `docs\contexto rama original\05_neural_controller_integration\_historical\notes_for_memory.md` | 1516 | Notes for memory |  |
| 538 | `docs\contexto rama original\05_neural_controller_integration\_historical\phase5_remaining_roadmap.md` | 1925 | Phase 5C: implementation prompt/spec finalization | Status: closed.; Status: closed.; Status: closed. |
| 539 | `docs\contexto rama original\05_neural_controller_integration\_historical\phase5a0_closure_report.md` | 921 | Phase 5A0 closure report |  |
| 540 | `docs\contexto rama original\05_neural_controller_integration\_historical\phase5a0_literature_delta_report.md` | 3231 | Phase 5A0 literature delta report |  |
| 541 | `docs\contexto rama original\05_neural_controller_integration\_historical\phase5c_closure_report.md` | 1620 | Phase 5C closure report |  |
| 542 | `docs\contexto rama original\05_neural_controller_integration\_historical\phase5c_file_change_plan.md` | 1574 | Phase 5C file change plan for Phase 5D |  |
| 543 | `docs\contexto rama original\05_neural_controller_integration\_historical\phase5c_test_plan_phase5d.md` | 1786 | Phase 5C test plan for Phase 5D |  |
| 544 | `docs\contexto rama original\05_neural_controller_integration\_historical\phase5d_structural_smoke_runbook.md` | 2601 | Phase 5D structural smoke runbook |  |
| 545 | `docs\contexto rama original\05_neural_controller_integration\_historical\phase5e_real_bundle_smoke_runbook.md` | 5149 | Phase 5E real bundle smoke runbook |  |
| 546 | `docs\contexto rama original\05_neural_controller_integration\_historical\phase5e_structural_smoke_plan.md` | 3177 | Phase 5E structural smoke plan |  |
| 547 | `docs\contexto rama original\05_neural_controller_integration\_historical\phase5e_ubuntu_gstreamer_smoke_runbook.md` | 3498 | Phase 5E Ubuntu GStreamer structural smoke runbook |  |
| 548 | `docs\contexto rama original\05_neural_controller_integration\_historical\phase5f_fault_injection_plan.md` | 3466 | Phase 5F fault injection plan |  |
| 549 | `docs\contexto rama original\05_neural_controller_integration\_historical\phase5f_hardening_report.md` | 5364 | Phase 5F hardening report |  |
| 550 | `docs\contexto rama original\05_neural_controller_integration\_historical\phase5g_controller_status_summary.md` | 1861 | Phase 5G controller status summary |  |
| 551 | `docs\contexto rama original\05_neural_controller_integration\_historical\phase5g_memory_notes.md` | 2234 | Phase 5G memory notes |  |
| 552 | `docs\contexto rama original\05_neural_controller_integration\_historical\phase5g_safety_fallback_closure.md` | 2573 | Phase 5G safety and fallback closure |  |
| 553 | `docs\contexto rama original\05_neural_controller_integration\_historical\phase5g_telemetry_artifact_closure.md` | 1593 | Phase 5G telemetry and artifact closure |  |
| 554 | `docs\contexto rama original\05_neural_controller_integration\phase5a0_no_implementation_yet.md` | 883 | Phase 5A0 no implementation yet |  |
| 555 | `docs\contexto rama original\05_neural_controller_integration\phase5a0_search_protocol.md` | 1976 | Phase 5A0 search protocol |  |
| 556 | `docs\contexto rama original\05_neural_controller_integration\phase5a0_source_inventory.md` | 5167 | Phase 5A0 source inventory |  |
| 557 | `docs\contexto rama original\05_neural_controller_integration\phase5a0_source_triage_decision.md` | 3786 | Phase 5A0 source triage decision |  |
| 558 | `docs\contexto rama original\05_neural_controller_integration\phase5a1_integration_evidence_matrix.md` | 6170 | Phase 5A1 integration evidence matrix |  |
| 559 | `docs\contexto rama original\05_neural_controller_integration\phase5a1_model_loading_matrix.md` | 1331 | Phase 5A1 model loading matrix |  |
| 560 | `docs\contexto rama original\05_neural_controller_integration\phase5a1_runtime_feature_availability_matrix.md` | 2369 | Phase 5A1 runtime feature availability matrix |  |
| 561 | `docs\contexto rama original\05_neural_controller_integration\phase5a1_safety_fallback_matrix.md` | 1916 | Phase 5A1 safety fallback matrix |  |
| 562 | `docs\contexto rama original\05_neural_controller_integration\phase5a1_source_card_index.md` | 3045 | Phase 5A1 source card index |  |
| 563 | `docs\contexto rama original\05_neural_controller_integration\phase5a1_telemetry_contamination_matrix.md` | 1883 | Phase 5A1 telemetry contamination matrix |  |
| 564 | `docs\contexto rama original\05_neural_controller_integration\phase5a2_integration_method_decision.md` | 1282 | Phase 5A2 integration method decision |  |
| 565 | `docs\contexto rama original\05_neural_controller_integration\phase5a2_neural_as_guarded_scorer_decision.md` | 1624 | Phase 5A2 neural as guarded scorer decision |  |
| 566 | `docs\contexto rama original\05_neural_controller_integration\phase5a2_rejected_alternatives.md` | 1609 | Phase 5A2 rejected alternatives |  |
| 567 | `docs\contexto rama original\05_neural_controller_integration\phase5b_acceptance_tests.md` | 1260 | Phase 5B acceptance tests |  |
| 568 | `docs\contexto rama original\05_neural_controller_integration\phase5b_action_mask_contract.md` | 1140 | Phase 5B action mask contract |  |
| 569 | `docs\contexto rama original\05_neural_controller_integration\phase5b_artifact_policy.md` | 616 | Phase 5B artifact policy |  |
| 570 | `docs\contexto rama original\05_neural_controller_integration\phase5b_bundle_loading_contract.md` | 1072 | Phase 5B bundle loading contract |  |
| 571 | `docs\contexto rama original\05_neural_controller_integration\phase5b_codex_implementation_readiness_gate.md` | 1669 | Phase 5B Codex implementation readiness gate |  |
| 572 | `docs\contexto rama original\05_neural_controller_integration\phase5b_controller_integration_contract.md` | 1470 | Phase 5B controller integration contract |  |
| 573 | `docs\contexto rama original\05_neural_controller_integration\phase5b_cpu_inference_contract.md` | 1000 | Phase 5B CPU inference contract |  |
| 574 | `docs\contexto rama original\05_neural_controller_integration\phase5b_error_handling_contract.md` | 1803 | Phase 5B error handling contract |  |
| 575 | `docs\contexto rama original\05_neural_controller_integration\phase5b_fallback_policy_contract.md` | 1254 | Phase 5B fallback policy contract |  |
| 576 | `docs\contexto rama original\05_neural_controller_integration\phase5b_model_loading_security_contract.md` | 1168 | Phase 5B model loading security contract |  |
| 577 | `docs\contexto rama original\05_neural_controller_integration\phase5b_no_benchmark_policy.md` | 805 | Phase 5B no benchmark policy |  |
| 578 | `docs\contexto rama original\05_neural_controller_integration\phase5b_runtime_feature_builder_contract.md` | 1862 | Phase 5B runtime feature builder contract |  |
| 579 | `docs\contexto rama original\05_neural_controller_integration\phase5b_safety_guard_contract.md` | 1380 | Phase 5B safety guard contract |  |
| 580 | `docs\contexto rama original\05_neural_controller_integration\phase5b_telemetry_contract.md` | 1020 | Phase 5B telemetry contract |  |
| 581 | `docs\contexto rama original\05_neural_controller_integration\phase5c_action_mask_safety_fallback_spec.md` | 2279 | Phase 5C action mask, safety and fallback spec |  |
| 582 | `docs\contexto rama original\05_neural_controller_integration\phase5c_bundle_runtime_spec.md` | 1705 | Phase 5C bundle runtime spec |  |
| 583 | `docs\contexto rama original\05_neural_controller_integration\phase5c_controller_api_mapping.md` | 2026 | Phase 5C controller API mapping |  |
| 584 | `docs\contexto rama original\05_neural_controller_integration\phase5c_current_code_mapping.md` | 4506 | Phase 5C current code mapping |  |
| 585 | `docs\contexto rama original\05_neural_controller_integration\phase5c_offline_runtime_boundary_spec.md` | 1454 | Phase 5C offline/runtime boundary spec |  |
| 586 | `docs\contexto rama original\05_neural_controller_integration\phase5c_runtime_feature_spec.md` | 2824 | Phase 5C runtime feature spec |  |
| 587 | `docs\contexto rama original\05_neural_controller_integration\phase5c_scope_and_gate.md` | 1419 | Phase 5C scope and gate |  |
| 588 | `docs\contexto rama original\05_neural_controller_integration\phase5c_telemetry_hook_decision.md` | 2620 | Phase 5C telemetry hook decision |  |
| 589 | `docs\contexto rama original\05_neural_controller_integration\phase5d_implementation_report.md` | 3930 | Scope |  |
| 590 | `docs\contexto rama original\05_neural_controller_integration\phase5e_artifact_inspection_checklist.md` | 9332 | Phase 5E artifact inspection checklist |  |
| 591 | `docs\contexto rama original\05_neural_controller_integration\phase5e_closure_report.md` | 5780 | Status |  |
| 592 | `docs\contexto rama original\05_neural_controller_integration\phase5e_scope_and_gate.md` | 1999 | Scope |  |
| 593 | `docs\contexto rama original\05_neural_controller_integration\phase5f_closure_report.md` | 3367 | Phase 5F closure report |  |
| 594 | `docs\contexto rama original\05_neural_controller_integration\phase5f_error_fallback_matrix.md` | 7364 | Phase 5F error fallback matrix |  |
| 595 | `docs\contexto rama original\05_neural_controller_integration\phase5f_scope_and_gate.md` | 1694 | Phase 5F scope and gate |  |
| 596 | `docs\contexto rama original\05_neural_controller_integration\phase5f_telemetry_hardening_matrix.md` | 3053 | Phase 5F telemetry hardening matrix |  |
| 597 | `docs\contexto rama original\05_neural_controller_integration\phase5g_final_integration_closure_report.md` | 5525 | Decision | Status: PASS. |
| 598 | `docs\contexto rama original\05_neural_controller_integration\phase5g_limitations_and_non_claims.md` | 1372 | Phase 5G limitations and non-claims |  |
| 599 | `docs\contexto rama original\05_neural_controller_integration\phase5g_repository_release_checklist.md` | 1093 | Checklist |  |
| 600 | `docs\contexto rama original\05_neural_controller_integration\phase5g_scope_and_gate.md` | 1387 | Scope |  |
| 601 | `docs\contexto rama original\05_neural_controller_integration\phase5g_validation_register.md` | 4652 | Register | Status: PASS. |
| 602 | `docs\contexto rama original\05_neural_controller_integration\source_cards\01_safesabr_runtime_safety_auditor.md` | 2248 | Source card 01: SafeSABR runtime safety auditor |  |
| 603 | `docs\contexto rama original\05_neural_controller_integration\source_cards\02_deepbuffer_action_mask_variable_ladder.md` | 2014 | Source card 02: DeepBuffer action mask and variable ladder |  |
| 604 | `docs\contexto rama original\05_neural_controller_integration\source_cards\03_a2br_domain_priors_fallback.md` | 2039 | Source card 03: A2BR domain priors and fallback |  |
| 605 | `docs\contexto rama original\05_neural_controller_integration\source_cards\04_abrl_facebook_candidate_scoring_deployment.md` | 2184 | Source card 04: ABRL Facebook candidate scoring deployment |  |
| 606 | `docs\contexto rama original\05_neural_controller_integration\source_cards\05_ahaggar_bitrate_guidance_hybrid_boundary.md` | 1956 | Title |  |
| 607 | `docs\contexto rama original\05_neural_controller_integration\source_cards\06_puffer_fugu_ml_predictor_mpc.md` | 1992 | Source card 06: Puffer/Fugu ML predictor plus MPC |  |
| 608 | `docs\contexto rama original\05_neural_controller_integration\source_cards\07_hybrid_abr_decision_level_fallback.md` | 1880 | Source card 07: Hybrid ABR decision-level fallback |  |
| 609 | `docs\contexto rama original\05_neural_controller_integration\source_cards\08_bayesmpc_uncertainty_predictor_mpc.md` | 1733 | Source card 08: BayesMPC uncertainty predictor plus MPC |  |
| 610 | `docs\contexto rama original\05_neural_controller_integration\source_cards\09_causalsim_trace_bias_contamination.md` | 1751 | Source card 09: CausalSim trace bias and contamination |  |
| 611 | `docs\contexto rama original\05_neural_controller_integration\source_cards\10_into_the_wild_real_world_testing_gap.md` | 1649 | Title |  |
| 612 | `docs\contexto rama original\05_neural_controller_integration\source_cards\11_comyco_lifelong_imitation_learning.md` | 1888 | Title |  |
| 613 | `docs\contexto rama original\05_neural_controller_integration\source_cards\12_oboe_runtime_network_state_autotuning.md` | 1876 | Title |  |
| 614 | `docs\contexto rama original\05_neural_controller_integration\source_cards\13_soda_deployable_smoothness_controller.md` | 1805 | Title |  |
| 615 | `docs\contexto rama original\05_neural_controller_integration\source_cards\14_sabr_bc_pretraining_rl_finetuning.md` | 1872 | Title |  |
| 616 | `docs\contexto rama original\05_neural_controller_integration\source_cards\15_beta_under_generalization.md` | 1696 | Title |  |
| 617 | `docs\contexto rama original\05_neural_controller_integration\source_cards\16_ant_network_dynamics_detection.md` | 1605 | Title |  |
| 618 | `docs\contexto rama original\05_neural_controller_integration\source_cards\17_gelato_plume_trace_skew_real_world.md` | 1662 | Title |  |
| 619 | `docs\contexto rama original\05_neural_controller_integration\source_cards\18_ml_model_loading_security.md` | 1754 | Source card 18: ML model loading security |  |
| 620 | `docs\contexto rama original\05_neural_controller_integration\source_cards\19_has_review_2025_background.md` | 1585 | Title |  |
| 621 | `docs\contexto rama original\05_neural_controller_integration\source_cards\20_learning_based_has_review_2025_background.md` | 1531 | Title |  |
| 622 | `docs\contexto rama original\05_neural_controller_integration\source_cards\21_metaabr_meta_learning_background.md` | 1520 | Title |  |
| 623 | `docs\contexto rama original\05_neural_controller_integration\source_cards\22_pytorch_model_loading_reference.md` | 1558 | Source card 22: PyTorch model loading reference |  |
| 624 | `docs\contexto rama original\05_neural_controller_integration\source_cards\23_onnx_runtime_reference.md` | 1575 | Title |  |
| 625 | `docs\contexto rama original\07_memory\README.md` | 836 | Thesis Memory |  |
| 626 | `docs\contexto rama original\07_memory\_historical\README.md` | 919 | Historical Documents |  |
| 627 | `docs\contexto rama original\07_memory\_historical\bibliography_plan.md` | 7756 | Bibliography Plan |  |
| 628 | `docs\contexto rama original\07_memory\_historical\chapter_05_baseline_implementation_notes.md` | 3962 | Chapter 05 Baseline Implementation Notes |  |
| 629 | `docs\contexto rama original\07_memory\_historical\chapter_06_evaluation_methodology_notes.md` | 11499 | Chapter 06 Evaluation Methodology Notes |  |
| 630 | `docs\contexto rama original\07_memory\_historical\defense_and_submission_requirements.md` | 837 | Defense And Submission Requirements |  |
| 631 | `docs\contexto rama original\07_memory\_historical\figures_plan.md` | 6269 | Figures Plan |  |
| 632 | `docs\contexto rama original\07_memory\_historical\gantt_and_costs_plan.md` | 1069 | Gantt And Costs Plan |  |
| 633 | `docs\contexto rama original\07_memory\_historical\memory_build_runbook.md` | 652 | Memory Build Runbook |  |
| 634 | `docs\contexto rama original\07_memory\_historical\official_normative_requirements.md` | 808 | Official And Normative Requirements |  |
| 635 | `docs\contexto rama original\07_memory\_historical\phase2_defense_talking_points.md` | 2914 | Phase 2 Defense Talking Points |  |
| 636 | `docs\contexto rama original\07_memory\_historical\phase2_memory_integration_plan.md` | 2910 | Phase 2 Memory Integration Plan |  |
| 637 | `docs\contexto rama original\07_memory\_historical\phase2_tables_and_figures_final_plan.md` | 2547 | Phase 2 Tables And Figures Final Plan |  |
| 638 | `docs\contexto rama original\07_memory\_historical\phase3_defense_talking_points.md` | 7976 | Phase 3 Defense Talking Points |  |
| 639 | `docs\contexto rama original\07_memory\_historical\phase3_figures_tables_plan.md` | 6840 | Phase 3 Figures Tables Plan |  |
| 640 | `docs\contexto rama original\07_memory\_historical\python_development_narrative_plan.md` | 2354 | Python Development Narrative Plan |  |
| 641 | `docs\contexto rama original\07_memory\_historical\tables_plan.md` | 8897 | Tables Plan |  |
| 642 | `docs\contexto rama original\07_memory\_templates\README.md` | 343 | Templates |  |
| 643 | `docs\contexto rama original\07_memory\_templates\latex_template_integration.md` | 849 | LaTeX Template Integration |  |
| 644 | `docs\contexto rama original\07_memory\chapter_06_pre_evaluation_boundary.md` | 2392 | Chapter 06 Pre-Evaluation Boundary |  |
| 645 | `docs\contexto rama original\07_memory\code_understanding_and_defense_checklist.md` | 5888 | Code Understanding And Defense Checklist |  |
| 646 | `docs\contexto rama original\07_memory\figures_tables_register.md` | 8598 | Figures And Tables Register |  |
| 647 | `docs\contexto rama original\07_memory\implementation_chapter_traceability.md` | 5669 | Implementation Chapter Traceability |  |
| 648 | `docs\contexto rama original\07_memory\memory_structure_professor.md` | 1167 | Memory Structure For Professor Review |  |
| 649 | `docs\contexto rama original\07_memory\originality_and_citation_policy.md` | 1232 | Originality And Citation Policy |  |
| 650 | `docs\contexto rama original\07_memory\portada_prefacio_metadata.md` | 694 | Portada And Preface Metadata |  |
| 651 | `docs\contexto rama original\07_memory\rubric_alignment.md` | 1055 | Rubric Alignment |  |
| 652 | `docs\contexto rama original\07_memory\style_and_format_rules.md` | 809 | Style And Format Rules |  |
| 653 | `docs\contexto rama original\0_desarrollo_del_cliente\audit.md` | 27814 | ABR Benchmarking Client Skeleton Audit |  |
| 654 | `docs\contexto rama original\0_desarrollo_del_cliente\baseline_entry_contract.md` | 12061 | Contrato de entrada para futuros baselines ABR |  |
| 655 | `docs\contexto rama original\0_desarrollo_del_cliente\client_architecture_audit.md` | 6523 | Auditoria de arquitectura del cliente |  |
| 656 | `docs\contexto rama original\0_desarrollo_del_cliente\client_readiness_report.md` | 6765 | Informe de readiness del cliente |  |
| 657 | `docs\contexto rama original\0_desarrollo_del_cliente\hardening_step_10_benchmark_neutrality.md` | 2907 | Hardening Step 10: Benchmark Neutrality Contract |  |
| 658 | `docs\contexto rama original\0_desarrollo_del_cliente\hardening_step_11_output_hygiene_legacy_cleanup.md` | 2024 | Hardening Step 11: Output Hygiene And Legacy Cleanup |  |
| 659 | `docs\contexto rama original\0_desarrollo_del_cliente\hardening_step_12_gstreamer_integration.md` | 1789 | Hardening Step 12: GStreamer Integration |  |
| 660 | `docs\contexto rama original\0_desarrollo_del_cliente\hardening_step_14_client_readiness.md` | 2968 | Hardening Step 14: Client Readiness Certification |  |
| 661 | `docs\contexto rama original\0_desarrollo_del_cliente\hardening_step_1_importability.md` | 1212 | Hardening Step 1: Importability |  |
| 662 | `docs\contexto rama original\0_desarrollo_del_cliente\hardening_step_2_config_runner.md` | 2879 | Hardening Step 2: Config Runner |  |
| 663 | `docs\contexto rama original\0_desarrollo_del_cliente\hardening_step_3_dependencies_environment.md` | 2842 | Hardening Step 3: Dependencies And Environment |  |
| 664 | `docs\contexto rama original\0_desarrollo_del_cliente\hardening_step_4_run_layout.md` | 2428 | Hardening Step 4: Reproducible Run Layout |  |
| 665 | `docs\contexto rama original\0_desarrollo_del_cliente\hardening_step_5_smoke_tests.md` | 2973 | Hardening Step 5: Minimal Smoke Tests |  |
| 666 | `docs\contexto rama original\0_desarrollo_del_cliente\hardening_step_6_dataset_schema.md` | 2146 | Hardening Step 6: Dataset Telemetry Schema Contract |  |
| 667 | `docs\contexto rama original\0_desarrollo_del_cliente\hardening_step_7_controller_contract.md` | 3195 | Hardening Step 7: Controller API / ABR Decision Contract |  |
| 668 | `docs\contexto rama original\0_desarrollo_del_cliente\hardening_step_8_deterministic_test_controllers.md` | 2555 | Hardening Step 8: Deterministic Test Controllers |  |
| 669 | `docs\contexto rama original\0_desarrollo_del_cliente\hardening_step_9_runtime_player_split.md` | 2324 | Hardening Step 9: Runtime / Player Responsibility Split |  |
| 670 | `docs\contexto rama original\0_desarrollo_del_cliente\metric_catalog.md` | 10060 | Catalogo de metricas y senales |  |
| 671 | `docs\contexto rama original\0_desarrollo_del_cliente\output_artifact_contract.md` | 4131 | Output Artifact Contract |  |
| 672 | `docs\contexto rama original\0_desarrollo_del_cliente\phase1_acceptance.md` | 7269 | Phase 1 Acceptance |  |
| 673 | `docs\contexto rama original\0_desarrollo_del_cliente\phase1_status.md` | 13887 | Phase 1 Status - Client Hardening |  |
| 674 | `docs\contexto rama original\0_desarrollo_del_cliente\phase2_baseline_closure.md` | 806 | Phase 2 Baseline Closure |  |
| 675 | `docs\contexto rama original\0_desarrollo_del_cliente\runtime_console_output_contract.md` | 3066 | Runtime Console Output Contract |  |
| 676 | `docs\contexto rama original\0_desarrollo_del_cliente\target.md` | 358 | target |  |
| 677 | `docs\contexto rama original\0_desarrollo_del_cliente\telemetry_column_provenance.md` | 18482 | Telemetry Column Provenance |  |
| 678 | `docs\contexto rama original\0_desarrollo_del_cliente\telemetry_metric_audit.md` | 8538 | Telemetry Metric Audit |  |
| 679 | `docs\contexto rama original\0_field_map\README.md` | 788 | Field Map |  |
| 680 | `docs\contexto rama original\0_field_map\dash_source_evidence.md` | 4932 | Source evidence â€” DASH, HAS and field map | Status: field-map evidence only. Not runtime code. |
| 681 | `docs\contexto rama original\0_field_map\dash_standard_reference.md` | 1652 | DASH Standard Reference |  |
| 682 | `docs\contexto rama original\0_field_map\local_streaming_related_work.md` | 1263 | Local Streaming Related Work |  |
| 683 | `docs\contexto rama original\0_field_map\local_streaming_source_evidence.md` | 4565 | Source evidence â€” local UGR streaming-related work | Status: local related work evidence only. Not baseline evidence and not runtime code. |
| 684 | `docs\contexto rama original\0_field_map\paper_cards\ameigeiras_2012_youtube_traffic.md` | 1220 | Source Card: Ameigeiras et al. 2012 YouTube Traffic |  |
| 685 | `docs\contexto rama original\0_field_map\paper_cards\bentaleb_2019_abr_survey.md` | 1303 | Source Card: Bentaleb et al. 2019 ABR Survey |  |
| 686 | `docs\contexto rama original\0_field_map\paper_cards\peroni_2025_streaming_pipeline_survey.md` | 1365 | Source Card: Peroni and Gorinsky 2025 Pipeline Survey |  |
| 687 | `docs\contexto rama original\0_field_map\paper_cards\ramos_munoz_2014_mobile_youtube_traffic.md` | 1212 | Source Card: Ramos-Munoz et al. 2014 Mobile YouTube Traffic |  |
| 688 | `docs\contexto rama original\0_field_map\paper_cards\stockhammer_2011_dash.md` | 1136 | Source Card: Stockhammer 2011 DASH |  |
| 689 | `docs\contexto rama original\0_field_map\paper_cards\timmerer_2025_has_review.md` | 1320 | Source Card: Timmerer et al. 2025 HAS Review |  |
| 690 | `docs\contexto rama original\0_field_map\research_questions.md` | 1577 | Research Questions |  |
| 691 | `docs\contexto rama original\0_field_map\scope_decision.md` | 1964 | Scope Decision |  |
| 692 | `docs\contexto rama original\0_field_map\source_inventory.md` | 3277 | Source Inventory |  |
| 693 | `docs\contexto rama original\0_field_map\state_of_the_art_map.md` | 2444 | State of the Art Map |  |
| 694 | `docs\contexto rama original\0_field_map\thesis_positioning.md` | 1865 | Thesis Positioning |  |
| 695 | `docs\rebuild\phase3_rebuild_closure_report.md` | 3585 | Phase 3 Rebuild Closure Report | status=PASS |
| 696 | `docs\rebuild\phase3_rebuild_start_report.md` | 4168 | Phase 3 rebuild start report |  |
| 697 | `docs\rebuild\phase3_rebuild_trace_pipeline.md` | 2978 | Phase 3 Rebuild Trace Pipeline |  |
| 698 | `docs\rebuild\phase3_trace_quality_audit_report.md` | 2922 | Phase 3 Trace Quality Audit Report | status=PASS |
| 699 | `docs\todos los estudios pdf convertidos a md\01_2015_seufert_qoe_http_adaptive_streaming_survey.md` | 172860 | 01_2015_seufert_qoe_http_adaptive_streaming_survey |  |
| 700 | `docs\todos los estudios pdf convertidos a md\06_2024_peroni_qoe_status_quo_pitfalls_guidelines.md` | 91791 | 06_2024_peroni_qoe_status_quo_pitfalls_guidelines |  |
| 701 | `docs\todos los estudios pdf convertidos a md\11_2022_zuo_ruyi_user_level_qoe_preference.md` | 89663 | 11_2022_zuo_ruyi_user_level_qoe_preference |  |
| 702 | `docs\todos los estudios pdf convertidos a md\12_2025_alsader_qoe_driven_adaptive_video_streaming_6g_survey.md` | 235832 | 12_2025_alsader_qoe_driven_adaptive_video_streaming_6g_survey |  |
| 703 | `docs\todos los estudios pdf convertidos a md\2011_liu_rate_adaptation_adaptive_http_streaming.md` | 40203 | 2011_liu_rate_adaptation_adaptive_http_streaming |  |
| 704 | `docs\todos los estudios pdf convertidos a md\2011_stockhammer_dash_standards_design_principles.md` | 17023 | 2011_stockhammer_dash_standards_design_principles |  |
| 705 | `docs\todos los estudios pdf convertidos a md\2012_ameigeiras_youtube_traffic_analysis_modelling.md` | 109851 | 2012_ameigeiras_youtube_traffic_analysis_modelling |  |
| 706 | `docs\todos los estudios pdf convertidos a md\2013_riiser_commute_path_bandwidth_traces_3g_networks.md` | 46649 | 2013_riiser_commute_path_bandwidth_traces_3g_networks |  |
| 707 | `docs\todos los estudios pdf convertidos a md\2014_huang_bba_buffer_based_rate_adaptation.md` | 143065 | 2014_huang_bba_buffer_based_rate_adaptation |  |
| 708 | `docs\todos los estudios pdf convertidos a md\2014_ramos_munoz_mobile_youtube_traffic_characteristics.md` | 49246 | 2014_ramos_munoz_mobile_youtube_traffic_characteristics |  |
| 709 | `docs\todos los estudios pdf convertidos a md\2015_netravali_mahimahi_record_replay_http.md` | 95125 | 2015_netravali_mahimahi_record_replay_http |  |
| 710 | `docs\todos los estudios pdf convertidos a md\2015_yin_mpc_control_theoretic_abr_http.md` | 144322 | 2015_yin_mpc_control_theoretic_abr_http |  |
| 711 | `docs\todos los estudios pdf convertidos a md\2016_van_der_hooft_http2_hevc_video_over_4g_lte.md` | 42509 | 2016_van_der_hooft_http2_hevc_video_over_4g_lte |  |
| 712 | `docs\todos los estudios pdf convertidos a md\2018_raca_4g_lte_dataset_channel_context_metrics.md` | 38408 | 2018_raca_4g_lte_dataset_channel_context_metrics |  |
| 713 | `docs\todos los estudios pdf convertidos a md\2019_bentaleb_abr_survey_http_streaming.md` | 194658 | 2019_bentaleb_abr_survey_http_streaming |  |
| 714 | `docs\todos los estudios pdf convertidos a md\2019_spiteri_dash_reference_player_bola_dynamic.md` | 84667 | 2019_spiteri_dash_reference_player_bola_dynamic |  |
| 715 | `docs\todos los estudios pdf convertidos a md\2019_wei_trace_based_emulation_throughput_prediction_abr.md` | 71215 | 2019_wei_trace_based_emulation_throughput_prediction_abr |  |
| 716 | `docs\todos los estudios pdf convertidos a md\2020_narayanan_lumos5g_imc.md` | 128011 | 2020_narayanan_lumos5g_imc |  |
| 717 | `docs\todos los estudios pdf convertidos a md\2020_raca_5g_dataset_channel_context_metrics_mmsys.md` | 34830 | 2020_raca_5g_dataset_channel_context_metrics_mmsys |  |
| 718 | `docs\todos los estudios pdf convertidos a md\2020_spiteri_bola_near_optimal_bitrate_adaptation_ton.md` | 98678 | 2020_spiteri_bola_near_optimal_bitrate_adaptation_ton |  |
| 719 | `docs\todos los estudios pdf convertidos a md\2020_yan_puffer_learning_in_situ_nsdi.md` | 95272 | 2020_yan_puffer_learning_in_situ_nsdi |  |
| 720 | `docs\todos los estudios pdf convertidos a md\2022_iso_iec_23009_1_dash_reference.md` | 1030305 | 2022_iso_iec_23009_1_dash_reference |  |
| 721 | `docs\todos los estudios pdf convertidos a md\2023_bothra_veritas_causal_queries_video_streaming_traces.md` | 105273 | 2023_bothra_veritas_causal_queries_video_streaming_traces |  |
| 722 | `docs\todos los estudios pdf convertidos a md\2025_hoffman_into_the_wild_ml_based_abr.md` | 28022 | 2025_hoffman_into_the_wild_ml_based_abr |  |
| 723 | `docs\todos los estudios pdf convertidos a md\2025_peroni_gorinsky_video_streaming_best_effort_pipeline_survey.md` | 167386 | 2025_peroni_gorinsky_video_streaming_best_effort_pipeline_survey |  |
| 724 | `docs\todos los estudios pdf convertidos a md\A quality-of-experience database for adaptive video streaming.md` | 85137 | ofstallingpersegment, |  |
| 725 | `docs\todos los estudios pdf convertidos a md\A review of learning-based methods for adaptive video streaming over HTTP.md` | 241730 | A review of learning-based methods for adaptive video streaming over HTTP |  |
| 726 | `docs\todos los estudios pdf convertidos a md\A2BR.md` | 133269 | A2BR |  |
| 727 | `docs\todos los estudios pdf convertidos a md\AIRL.md` | 86925 | AIRL |  |
| 728 | `docs\todos los estudios pdf convertidos a md\ANT.md` | 98891 | ANT |  |
| 729 | `docs\todos los estudios pdf convertidos a md\BETA.md` | 100235 | Step1:Input-trainingtracedataΛ;Output-trainedclassifierC |  |
| 730 | `docs\todos los estudios pdf convertidos a md\Beyond Throughput The Next Generation A 5G Dataset with Channel and Context Metrics.md` | 34830 | Beyond Throughput The Next Generation A 5G Dataset with Channel and Context Metrics |  |
| 731 | `docs\todos los estudios pdf convertidos a md\Beyond Throughput a 4G LTE Dataset with Channel and Context Metrics.md` | 38408 | Beyond Throughput a 4G LTE Dataset with Channel and Context Metrics |  |
| 732 | `docs\todos los estudios pdf convertidos a md\Bitrate Adaptation and Guidance With Meta Reinforcement Learning.md` | 124699 | Bitrate Adaptation and Guidance With Meta Reinforcement Learning |  |
| 733 | `docs\todos los estudios pdf convertidos a md\Buffer awareness neural adaptive video streaming for avoiding extra buffer consumption.md` | 77996 | randomize bitrate ladders: 100-7000kbps |  |
| 734 | `docs\todos los estudios pdf convertidos a md\CausalSim.md` | 218543 | CausalSim |  |
| 735 | `docs\todos los estudios pdf convertidos a md\CellReplay.md` | 150335 | CellReplay |  |
| 736 | `docs\todos los estudios pdf convertidos a md\Comyco.md` | 133952 | Comyco |  |
| 737 | `docs\todos los estudios pdf convertidos a md\EAStream.md` | 105673 | EAStream |  |
| 738 | `docs\todos los estudios pdf convertidos a md\Fortuna.md` | 86496 | Fortuna |  |
| 739 | `docs\todos los estudios pdf convertidos a md\Gelato.md` | 78850 | Gelato |  |
| 740 | `docs\todos los estudios pdf convertidos a md\HTTP Adaptive Streaming A Review on Current Advances and Future Challenges.md` | 118313 | HTTP Adaptive Streaming A Review on Current Advances and Future Challenges |  |
| 741 | `docs\todos los estudios pdf convertidos a md\Hybrid Adaptive Bitrate for Video Streaming.md` | 47076 | Fallback point identifier |  |
| 742 | `docs\todos los estudios pdf convertidos a md\MERINA.md` | 93128 | MERINA |  |
| 743 | `docs\todos los estudios pdf convertidos a md\Mahimahi.md` | 95125 | Mahimahi |  |
| 744 | `docs\todos los estudios pdf convertidos a md\MetaABR.md` | 85621 | MetaABR |  |
| 745 | `docs\todos los estudios pdf convertidos a md\NMoEABR.md` | 109120 | NMoEABR |  |
| 746 | `docs\todos los estudios pdf convertidos a md\ONNX Runtime Python API.md` | 42528 | X is numpy array on cpu |  |
| 747 | `docs\todos los estudios pdf convertidos a md\Oboe.md` | 90707 | Oboe |  |
| 748 | `docs\todos los estudios pdf convertidos a md\On the (In) Security of Loading Machine Learning Models.md` | 162973 | On the (In) Security of Loading Machine Learning Models |  |
| 749 | `docs\todos los estudios pdf convertidos a md\Pensieve.md` | 102508 | Pensieve |  |
| 750 | `docs\todos los estudios pdf convertidos a md\Plume.md` | 83415 | Plume |  |
| 751 | `docs\todos los estudios pdf convertidos a md\PyTorch 2.12 documentation.md` | 7324 | Load all tensors onto the CPU |  |
| 752 | `docs\todos los estudios pdf convertidos a md\QoE modeling for HTTP adaptive video streaming.md` | 190534 | QoE modeling for HTTP adaptive video streaming |  |
| 753 | `docs\todos los estudios pdf convertidos a md\Real-world Video Adaptation with Reinforcement Learning.md` | 77065 | Real-world Video Adaptation with Reinforcement Learning |  |
| 754 | `docs\todos los estudios pdf convertidos a md\SABR.md` | 50486 | SABR |  |
| 755 | `docs\todos los estudios pdf convertidos a md\SODA.md` | 236965 | SODA |  |
| 756 | `docs\todos los estudios pdf convertidos a md\SafeSABR.md` | 93615 | SafeSABR |  |
| 757 | `docs\todos los estudios pdf convertidos a md\Surveys de 2025.md` | 247987 | Surveys de 2025 |  |
| 758 | `docs\todos los estudios pdf convertidos a md\Uncertainty-aware robust adaptive video streaming with bayesian neural network and model predictive control.md` | 53634 | Uncertainty-aware robust adaptive video streaming with bayesian neural network and model predictive control |  |
| 759 | `docs\todos los estudios pdf convertidos a md\Understanding quality of experience of heuristic-based HTTP adaptive bitrate algorithms.md` | 55203 | Understanding quality of experience of heuristic-based HTTP adaptive bitrate algorithms |  |
| 760 | `docs\todos los estudios pdf convertidos a md\Veritas.md` | 131008 | Veritas |  |
| 761 | `docs\todos los estudios pdf convertidos a md\Zhou.md` | 42374 | Zhou |  |

### Catalogo Python versionado

| # | Ruta | Bytes | Clases | Funciones | Parse error |
|---:|---|---:|---|---|---|
| 1 | `analysis_metrics.py` | 17360 |  | `_coerce_types`, `_estimate_startup_delay`, `_count_switches_series`, `_quality_switches`, `_playback_time`, `_total_bytes`, `_mean_throughput_bps`, `load_and_summarize`, `_save_bar`, `plot_summary_tables`, `plot_timelines`, `_minmax_norm` (+2) |  |
| 2 | `core\__init__.py` | 0 |  |  |  |
| 3 | `core\benchmark_contract.py` | 2684 |  | `normalize_segment_index`, `classify_segment_phase`, `should_use_segment_for_eval`, `classify_stall_event`, `should_use_stall_for_eval` |  |
| 4 | `core\client_config.py` | 18655 | `ConfigError`, `MediaEngineConfig`, `ControllerConfig`, `PlaybackConfig`, `DownloaderConfig`, `NetworkReplayConfig`, `OutputConfig`, `LoggingConfig`, `AnalysisConfig`, `ClientConfig` | `load_client_config`, `validate_config_for_run`, `_select_config_path`, `_load_yaml_file`, `_parse_simple_yaml`, `_parse_scalar`, `_deep_merge`, `_mapping`, `_as_str`, `_as_optional_str`, `_output_filename`, `_as_bool` (+4) |  |
| 5 | `core\controller\__init__.py` | 0 |  |  |  |
| 6 | `core\controller\base.py` | 3193 | `BaseController` |  |  |
| 7 | `core\controller\bba.py` | 4182 | `BbaController` | `_available_rates_Bps`, `_clamp_level`, `_finish`, `_non_negative_float`, `_positive_float`, `_finite_float`, `_to_int` |  |
| 8 | `core\controller\bola.py` | 12933 | `BolaController` | `_available_rates_Bps`, `_utilities_log_rate_ratio`, `_candidate_segment_sizes_B`, `_normalize_segment_sizes_B`, `_rate_to_bytes_per_second`, `_size_to_bytes`, `_clamp_level`, `_finish`, `_positive_float`, `_optional_non_negative_float`, `_finite_float`, `_to_int` (+4) |  |
| 9 | `core\controller\contract.py` | 5100 |  | `missing_feedback_keys`, `validate_feedback_keys`, `validate_rates`, `quantize_rate_to_level` |  |
| 10 | `core\controller\fixed_quality.py` | 1329 | `FixedQualityController` | `_clamp_level`, `_to_int` |  |
| 11 | `core\controller\max_quality_controller.py` | 5358 | `MaxQualityController` |  |  |
| 12 | `core\controller\mpc.py` | 21311 | `MpcController` | `_simulate_sequence`, `_available_rates_Bps`, `_configured_throughput_history_Bps`, `_measured_throughput_sample_Bps`, `_harmonic_mean_Bps`, `_qualities_log_rate_ratio`, `_candidate_segment_sizes_B`, `_normalize_segment_sizes_B`, `_rate_to_bytes_per_second`, `_size_to_bytes`, `_remaining_segments`, `_current_level` (+11) |  |
| 13 | `core\controller\neural_abr_diagnostics.py` | 4747 | `NeuralAbrDiagnostics` | `stable_reason`, `augment_feedback_with_neural_diagnostics` |  |
| 14 | `core\controller\neural_abr_lite.py` | 15203 | `NeuralAbrLiteController`, `NeuralAbrLiteRobustMpcController`, `NeuralAbrLiteTeacherHibridoController` | `_create_classical_fallback`, `_apply_load_error_diagnostics`, `_set_raw_action_diagnostics`, `_runtime_inference_reason`, `_lowest_rate_from_payload`, `_fallback_payload`, `_basic_rates_and_mask`, `_basic_rates`, `_positive_float`, `_finite_float`, `_int_or_default`, `_as_bool` |  |
| 15 | `core\controller\neural_abr_loader.py` | 10429 | `NeuralAbrRuntimeBundleError`, `NeuralAbrRuntimeBundle` | `load_neural_abr_runtime_bundle`, `_validate_bundle`, `_load_feature_schema`, `_torch_load_weights_only`, `_assert_candidate_indices_are_positions`, `_finite_scores`, `_select_position` |  |
| 16 | `core\controller\neural_abr_runtime_features.py` | 11036 | `RuntimeFeatureError`, `RuntimeFeaturePayload`, `NeuralAbrRuntimeFeatureBuilder` | `_candidate_features`, `_chunks_remaining`, `_left_pad`, `_finite_number`, `_int_or_none`, `_clamp` |  |
| 17 | `core\controller\neural_abr_safety.py` | 1523 | `NeuralAbrSafetyError` | `safe_action_to_rate`, `lowest_valid_action` |  |
| 18 | `core\controller\phase45_v3_neural_mpc.py` | 20958 | `Phase45V3NeuralMpcRuntimeError`, `Phase45V3NeuralMpcRuntimeBundle`, `Phase45V3NeuralMpcController`, `Phase45V3NeuralMpcV2Controller` | `_validate_bundle`, `_torch_load_weights_only`, `_ladder_from_payload`, `_state_from_payload`, `_positive_history`, `_lowest_valid_rate`, `_rates_from_feedback`, `_apply_load_error_diagnostics`, `_positive_float`, `_positive_int`, `_finite_float`, `_as_bool` |  |
| 19 | `core\controller\rate_based.py` | 12481 | `RateBasedController` | `_available_rates_Bps`, `_measured_throughput_Bps`, `_history_throughput_Bps`, `_rate_to_bytes_per_second`, `_floor_rate_to_level`, `_current_level`, `_clamp_level`, `_finish`, `_bounded_float`, `_non_negative_float`, `_finite_float`, `_to_int` (+1) |  |
| 20 | `core\controller\registry.py` | 4255 | `ControllerSpec` | `available_controllers`, `create_controller` |  |
| 21 | `core\controller\robust_mpc.py` | 17833 | `RobustMpcController` | `_configured_prediction_error_history`, `_prediction_errors_from_history_pairs`, `_configured_rate_history_Bps`, `_prediction_error_ratio`, `_unit_interval_float`, `_first_not_none` |  |
| 22 | `core\controller\sanity_rate.py` | 4475 | `MinRateController`, `MaxRateController`, `FixedRateController` | `_available_rates`, `_normalize_rates`, `_floor_rate_to_level`, `_clamp_level`, `_target_rate_to_bytes_per_second`, `_finish`, `_first_not_none`, `_to_int` |  |
| 23 | `core\controller\scripted_quality.py` | 2377 | `ScriptedQualityController` | `_normalize_levels`, `_clamp_level`, `_to_int`, `_to_non_negative_int` |  |
| 24 | `core\controller\spbc_abr_v2_dpo.py` | 1514 | `SpbcAbrV2DpoAnchorSafeRankController` |  |  |
| 25 | `core\controller\spbc_abr_v2_dpo_loader.py` | 15392 | `SpbcV2DpoRuntimeBundle` | `load_spbc_v2_dpo_runtime_bundle`, `_validate_bundle`, `_load_feature_schema`, `_load_normalization`, `_build_feature_rows`, `_normalize_vector`, `_normalize_matrix`, `_tensor_row`, `_torch_load_weights_only`, `_assert_candidate_indices_are_positions`, `_finite_scores`, `_select_position` (+4) |  |
| 26 | `core\dataset_schema.py` | 3743 |  | `feedback_column_name`, `feedback_column_names`, `build_segment_telemetry_header`, `build_default_segment_telemetry_header`, `build_evaluation_segments_header`, `validate_unique_columns`, `validate_row_length` |  |
| 27 | `core\downloader.py` | 5736 | `SegmentDownloader` |  |  |
| 28 | `core\evaluation\__init__.py` | 755 |  |  |  |
| 29 | `core\evaluation\artifacts.py` | 13411 | `QoEArtifactError`, `QoEArtifactComputationResult` | `load_segment_qoe_inputs_from_csv`, `compute_qoe_summary_from_segments_csv`, `compute_qoe_artifacts_from_dry_run`, `_require_file`, `_read_json_object`, `_write_json`, `_require_columns`, `_resolve_expected_segment_count`, `_derive_gate_reasons`, `_row_gate_values`, `_append_unique`, `_qoe_result_to_summary` (+1) |  |
| 30 | `core\evaluation\qoe.py` | 7696 | `SegmentQoEInput`, `QoEWeights`, `QoEResult` | `compute_linear_qoe`, `compute_log_qoe`, `_validated_segments`, `_validated_weights`, `_require_finite_positive`, `_require_finite_non_negative`, `_require_finite`, `_adjacent_deltas`, `_build_result` |  |
| 31 | `core\media_engine\__init__.py` | 0 |  |  |  |
| 32 | `core\media_engine\base.py` | 1859 | `BaseMediaEngine` |  |  |
| 33 | `core\media_engine\fake.py` | 9296 | `FakeMediaEngine` |  |  |
| 34 | `core\media_engine\gst_media_engine.py` | 25838 | `GstMediaEngine` | `gstreamer_unavailable_message`, `_format_exception` |  |
| 35 | `core\neural_abr\__init__.py` | 232 |  |  |  |
| 36 | `core\neural_abr\action_mask.py` | 1813 | `ActionMaskError` | `build_action_mask`, `validate_action_mask`, `assert_action_valid`, `lowest_valid_action` |  |
| 37 | `core\neural_abr\artifacts.py` | 3070 | `NeuralAbrArtifactError` | `resolve_path`, `ensure_outside_repo`, `prepare_output_dir`, `ensure_existing_dir`, `write_json`, `read_json`, `write_jsonl`, `read_jsonl` |  |
| 38 | `core\neural_abr\bundle.py` | 5746 | `BundleError` | `prepare_bundle_output_dir`, `resolve_bundle_dir`, `sha256_file`, `bundle_file_record`, `write_phase4_bundle_manifest`, `validate_phase4_bundle_dir`, `require_bundle_files` |  |
| 39 | `core\neural_abr\bundle_validation.py` | 5572 | `BundleValidationError` | `validate_phase4_inference_bundle`, `_gate`, `_p95` |  |
| 40 | `core\neural_abr\candidate_readiness.py` | 12677 | `CandidateReadinessError` | `assess_phase4_candidate_model`, `_gate`, `_mapping`, `_float_eq`, `_float_at_least`, `_all_finite`, `_prediction_warnings`, `_sha256_file` |  |
| 41 | `core\neural_abr\constants.py` | 4932 |  |  |  |
| 42 | `core\neural_abr\content_ladder.py` | 4800 | `ContentLadderError`, `Representation`, `ContentLadder` | `default_training_ladder`, `_validate_ladder` |  |
| 43 | `core\neural_abr\export_bundle.py` | 10954 | `BundleExportError` | `export_phase4_inference_bundle`, `_validate_export_inputs`, `_build_ladder_schema`, `_build_model_card`, `_build_inference_contract`, `_build_fallback_policy`, `_utc_now` |  |
| 44 | `core\neural_abr\features.py` | 6257 | `FeatureError` | `build_context_features`, `build_candidate_features`, `flatten_context_features`, `flatten_candidate_features`, `build_feature_schema`, `audit_feature_payload`, `reject_forbidden_model_inputs`, `_left_pad`, `_numeric_sequence`, `_finite_number` |  |
| 45 | `core\neural_abr\hybrid_teacher.py` | 12217 | `ClassicTeacherDecision`, `HybridTeacherSampleDraft`, `ClassicTeacherTrajectory`, `HybridTeacherWindowSelection`, `HybridTeacherError`, `ClassicControllerTeacher` | `select_hybrid_teacher_for_window`, `build_hybrid_label_for_draft`, `qoe_linear_reward_for_replay_step`, `hybrid_selection_audit`, `_simulate_teacher_trajectory`, `_build_controller`, `_feedback_from_state`, `_action_from_target_rate`, `_trajectory_sort_key` |  |
| 46 | `core\neural_abr\hybrid_training_data.py` | 17635 |  | `build_phase4_hybrid_teacher_data_from_plan`, `build_phase4_hybrid_teacher_data_from_plan_file`, `validate_phase4_hybrid_teacher_data_dir`, `_samples_for_hybrid_window`, `_hybrid_sample_metadata`, `_build_hybrid_summary`, `_build_hybrid_leakage_audit`, `_build_hybrid_teacher_audit`, `_validate_plan_for_hybrid_build`, `_limited_windows` |  |
| 47 | `core\neural_abr\inference.py` | 12387 | `InferenceError`, `NeuralAbrLiteInferenceBundle` | `load_phase4_inference_bundle`, `run_phase4_inference_smoke`, `_torch_load_cpu`, `_mapping`, `_sequence`, `_candidate_sequence`, `_assert_candidate_indices_are_positions`, `_finite_scores`, `_select_position`, `_scores_are_finite`, `_latency_summary`, `_percentile` |  |
| 48 | `core\neural_abr\model.py` | 4230 | `ModelError`, `NeuralAbrLiteCandidateScorer` | `masked_cross_entropy`, `predict_actions` |  |
| 49 | `core\neural_abr\model_training.py` | 10884 | `CandidateModelTrainingError` | `train_phase4_candidate_model`, `load_phase4_candidate_model`, `_validate_optional_sample_limit`, `_sha256_file`, `_torch_load_cpu` |  |
| 50 | `core\neural_abr\normalization.py` | 5591 | `NormalizationError`, `NormalizationStats`, `FeatureNormalizer` |  |  |
| 51 | `core\neural_abr\replay_environment.py` | 4616 | `ReplayState`, `ReplayStepResult`, `ReplayEnvironmentError`, `TraceReplayEnvironment` | `_append_context_value` |  |
| 52 | `core\neural_abr\sample_schema.py` | 4636 | `SampleSchemaError` | `build_label_schema`, `validate_sample`, `_mapping`, `_sequence` |  |
| 53 | `core\neural_abr\trace_sampling.py` | 33618 | `Phase4TraceSamplingError`, `Phase4SamplingConfig`, `_SelectionCounters` | `build_phase4_training_trace_artifacts`, `write_phase4_training_trace_artifacts`, `validate_phase4_training_trace_plan`, `load_phase4_training_trace_plan`, `_validated_phase3_traces`, `_build_trace_windows`, `_trace_allowed_for_role`, `_window_count_for_trace`, `_window_record`, `_select_balanced_windows`, `_quota_rejection_reason`, `_quota_limit` (+23) |  |
| 54 | `core\neural_abr\training_data.py` | 14055 | `TrainingDataBuildError` | `build_phase4_training_data_from_plan`, `build_phase4_training_data_from_plan_file`, `load_trace_window`, `_samples_for_window`, `_sample_metadata`, `_build_summary`, `_build_leakage_audit`, `_validate_plan_for_data_build`, `_limited_windows` |  |
| 55 | `core\neural_abr\training_data_validation.py` | 3666 | `TrainingDataValidationError` | `validate_phase4_training_data_dir` |  |
| 56 | `core\neural_abr\training_runtime.py` | 3960 | `TrainingRuntimeError` | `set_training_determinism`, `batch_to_tensors`, `evaluate_candidate_scorer` |  |
| 57 | `core\neural_abr\training_smoke.py` | 4170 | `TrainingSmokeError` | `run_phase4_training_smoke` |  |
| 58 | `core\output_artifacts.py` | 782 |  |  |  |
| 59 | `core\parser\__init__.py` | 0 |  |  |  |
| 60 | `core\parser\base.py` | 2677 | `ParserBase` |  |  |
| 61 | `core\parser\dash.py` | 17359 | `DashParser` |  |  |
| 62 | `core\parser\test_parser.py` | 2370 |  | `main` |  |
| 63 | `core\phase45_v1\__init__.py` | 1340 |  |  |  |
| 64 | `core\phase45_v1\constants.py` | 4423 |  | `no_benchmark_policy` |  |
| 65 | `core\phase45_v1\dataset.py` | 26826 | `Phase45DatasetBuildError` | `build_phase45_v1_dataset`, `load_trace_window`, `_samples_for_window`, `_build_spc_targets`, `_build_audit`, `_future_throughput_stats`, `_weighted_future_values`, `_weighted_quantile`, `_sample_metadata`, `_build_summary`, `_build_leakage_audit`, `_build_oracle_audit` (+2) |  |
| 66 | `core\phase45_v1\normalization.py` | 3322 | `NumericStats` | `build_train_only_normalization`, `_collect_model_input_values`, `_collect_mapping_values`, `_add_numeric`, `_numeric_stats` |  |
| 67 | `core\phase45_v1\offline_validation.py` | 40470 | `Phase45OfflineValidationError`, `OfflineValidationProfile`, `GuardDecision`, `OfflineExample`, `LoadedSpbcRuntime`, `LoadedSpcRuntime`, `_VariantMetricTotals`, `_GuardMetricTotals` | `profile_by_name`, `validate_spbc_spc_offline`, `load_spbc_runtime`, `load_spc_runtime`, `apply_spc_guard`, `load_offline_examples`, `resolve_torch_device`, `_build_observation`, `_build_comparison`, `_build_offline_gate`, `_recommend_next_step`, `_low_buckets_not_worse` (+16) |  |
| 68 | `core\phase45_v1\oracle.py` | 10036 | `Phase45OracleError`, `OracleConfig`, `OracleDecision`, `_BeamNode` | `select_oracle_action`, `simulate_step_from_state`, `linear_reward_for_state`, `oracle_policy_card`, `_beam_sort_key`, `_fallback_decision`, `_append_context_value` |  |
| 69 | `core\phase45_v1\paths.py` | 2525 | `Phase45PathError`, `PathRewriteRule` | `parse_rewrite_rule`, `parse_rewrite_rules`, `default_trace_path_rewrites`, `resolve_external_trace_path` |  |
| 70 | `core\phase45_v1\preference_dataset_v2.py` | 56132 | `Phase45V2DatasetBuildError`, `Phase45V2DatasetValidationError`, `LoadedRolloutPolicy` | `build_phase45_v2_dataset`, `validate_phase45_v2_dataset_dir`, `validate_v2_sample`, `_samples_for_window`, `_build_per_action_outcomes`, `_build_preference_pairs`, `_best_immediate_action`, `_load_optional_spbc_runtime`, `_load_optional_v2_dpo_runtime`, `_select_policy_action`, `_build_feature_schema`, `_build_target_schema` (+20) |  |
| 71 | `core\phase45_v1\profiles.py` | 2769 | `Phase45ProfileError`, `DatasetProfile` | `profile_by_name` |  |
| 72 | `core\phase45_v1\sample_schema.py` | 6737 | `Phase45SampleSchemaError` | `build_model_input_schema`, `build_target_schema`, `validate_sample`, `reject_forbidden_model_inputs`, `_validate_model_inputs`, `_require_mapping`, `_finite` |  |
| 73 | `core\phase45_v1\sampling.py` | 28966 | `Phase45SamplingError`, `SamplingConfig`, `_SelectionCounters` | `build_sampling_artifacts`, `validate_sampling_plan`, `_validated_phase3_traces`, `_build_candidate_windows`, `_select_windows`, `_quota_rejection_reason`, `_window_record`, `throughput_bucket`, `variability_bucket`, `_selection_group_key`, `_selection_weight_for_key`, `_trace_allowed_for_role` (+18) |  |
| 74 | `core\phase45_v1\spbc_spc_v2_hybrid_validation.py` | 35545 | `SpbcSpcV2HybridValidationProfile`, `SpbcSpcV2HybridValidationError`, `_ModeAccumulator` | `hybrid_profile_by_name`, `validate_spbc_spc_v2_hybrid_offline`, `_evaluate_hybrid_modes`, `_spc_model_and_normalization`, `_select_veto_only`, `_select_topk_rerank`, `_is_safe_action`, `_observation_for_action`, `_is_useful_intervention`, `_hybrid_gate`, `_mode_delta`, `_critical_delta` (+8) |  |
| 75 | `core\phase45_v1\spbc_training.py` | 47424 | `SpbcTrainingError`, `SpbcTrainingProfile`, `SpbcExample`, `SpbcNormalizationStats`, `SpbcAbrV1Policy`, `_LossTotals`, `_PolicyMetricTotals` | `profile_by_name`, `train_spbc_abr_v1`, `load_spbc_examples`, `fit_spbc_normalization`, `examples_to_tensors`, `compute_class_weighting`, `evaluate_spbc_model`, `resolve_torch_device`, `set_training_seed`, `_run_epoch`, `_loss_components`, `_masked_weighted_cross_entropy` (+18) |  |
| 76 | `core\phase45_v1\spbc_v2_dpo_bundle.py` | 20963 | `SpbcV2DpoBundleError` | `export_spbc_v2_dpo_inference_bundle`, `validate_spbc_v2_dpo_bundle_dir`, `write_spbc_v2_dpo_bundle_manifest`, `build_spbc_v2_dpo_feature_schema`, `build_spbc_v2_dpo_ladder_schema`, `build_spbc_v2_dpo_model_card`, `build_spbc_v2_dpo_inference_contract`, `build_spbc_v2_dpo_fallback_policy`, `sha256_file`, `bundle_file_record`, `_validate_training_checkpoint`, `_validate_normalization` (+8) |  |
| 77 | `core\phase45_v1\spbc_v2_dpo_training.py` | 145714 | `SpbcV2DpoTrainingError`, `SpbcV2DpoTrainingProfile`, `PreferencePair`, `SpbcV2DpoExample`, `SpbcV2DpoNormalizationStats`, `SpbcAbrV2DpoPolicy`, `_LossTotals`, `_PolicyMetricTotals` | `profile_by_name`, `train_spbc_abr_v2_dpo`, `load_spbc_v2_dpo_examples`, `fit_spbc_v2_dpo_normalization`, `examples_to_tensors`, `evaluate_spbc_v2_dpo_model`, `resolve_torch_device`, `set_training_seed`, `_run_epoch`, `_loss_components`, `_masked_weighted_cross_entropy`, `_dpo_loss` (+58) |  |
| 78 | `core\phase45_v1\spc_training.py` | 42818 | `SpcTrainingError`, `SpcTrainingProfile`, `SpcExample`, `SpcNormalizationStats`, `SpcAbrV1Predictor`, `_MetricTotals` | `profile_by_name`, `train_spc_abr_v1`, `load_spc_examples`, `fit_spc_normalization`, `examples_to_tensors`, `evaluate_spc_model`, `resolve_torch_device`, `set_training_seed`, `_run_epoch`, `_emit_progress`, `_progress_batch_interval`, `_loss_components` (+22) |  |
| 79 | `core\phase45_v1\spc_v2_reward_risk_training.py` | 68229 | `SpcV2RewardRiskTrainingError`, `SpcV2RewardRiskTrainingProfile`, `SpcV2RewardRiskNormalizationStats`, `SpcAbrV2RewardRiskScorer`, `_LossTotals`, `_PredictionMetricTotals`, `_ScorerMetricTotals` | `profile_by_name`, `train_spc_abr_v2_reward_risk`, `fit_spc_v2_reward_risk_normalization`, `evaluate_spc_v2_reward_risk_model`, `resolve_torch_device`, `set_training_seed`, `_load_examples_for_scorer`, `_run_epoch`, `_loss_components`, `_masked_weighted_cross_entropy`, `_pairwise_score_loss`, `_masked_weighted_smooth_l1` (+22) |  |
| 80 | `core\phase45_v1\validation.py` | 4953 | `Phase45DatasetValidationError` | `validate_phase45_v1_dataset_dir`, `_assert_no_benchmark` |  |
| 81 | `core\phase45_v3\__init__.py` | 2077 |  | `__getattr__` |  |
| 82 | `core\phase45_v3\abr_closed_loop_env.py` | 10238 | `AbrClosedLoopEnvError`, `AbrClosedLoopState`, `AbrClosedLoopStep`, `AbrClosedLoopEnv` | `default_phase45_v3_ladder`, `initial_closed_loop_state`, `simulate_closed_loop_step`, `linear_transition_reward`, `runtime_feedback_from_state`, `_append_history`, `_finite_positive` |  |
| 83 | `core\phase45_v3\closedloop_spbc_spc_dataset.py` | 41428 | `Phase45V3ClosedLoopSpbcSpcDatasetError` | `build_phase45_v3_closedloop_spbc_spc_dataset`, `validate_phase45_v3_closedloop_spbc_spc_dataset_dir`, `summarize_phase45_v3_closedloop_spbc_spc_dataset`, `load_phase3_manifest`, `build_default_phase45_v3_closedloop_spbc_spc_trace_path_rewrites`, `resolve_phase45_v3_closedloop_spbc_spc_trace_path`, `_transform_qh_sample`, `_build_augmented_action_value`, `_build_spbc_spc_summary`, `_build_spbc_spc_leakage_audit`, `_build_spbc_spc_target_audit`, `_build_spbc_spc_feature_schema` (+15) |  |
| 84 | `core\phase45_v3\constants.py` | 2486 |  | `no_benchmark_policy` |  |
| 85 | `core\phase45_v3\dataset.py` | 30105 | `Phase45V3DatasetBuildError` | `build_phase45_v3_qh_dataset`, `load_phase3_manifest`, `build_default_phase45_v3_trace_path_rewrites`, `resolve_phase45_v3_trace_path`, `_samples_for_window_rollout`, `_validate_sample`, `_build_summary`, `_build_leakage_audit`, `_build_qh_audit`, `_build_feature_schema`, `_build_target_schema`, `_sample_metadata` (+13) |  |
| 86 | `core\phase45_v3\neural_mpc_bundle.py` | 23894 | `Phase45V3NeuralMpcBundleError` | `export_phase45_v3_neural_mpc_experimental_bundle`, `collect_neural_mpc_candidate_readiness`, `validate_phase45_v3_neural_mpc_bundle_dir`, `write_neural_mpc_bundle_manifest`, `build_neural_mpc_model_card`, `build_neural_mpc_inference_contract`, `build_neural_mpc_fallback_policy`, `sha256_file`, `bundle_file_record`, `_canonical_seed_record`, `_failed_gates`, `_mapping` (+5) |  |
| 87 | `core\phase45_v3\neural_mpc_controller.py` | 14037 | `Phase45V3NeuralMpcError`, `NeuralMpcDecision`, `NeuralThroughputCalibratedMpcController`, `TorchThroughputQuantilePredictor` | `plan_neural_mpc_action`, `select_throughput_plan_for_buffer`, `_score_sequence`, `_validate_prediction`, `_valid_actions`, `_nearest_quantile_index`, `_monotonicize_quantile_row`, `_normalize_vector`, `_resolve_device` |  |
| 88 | `core\phase45_v3\neural_mpc_evaluation.py` | 21526 | `Phase45V3NeuralMpcEvaluationError` | `evaluate_phase45_v3_neural_mpc_closed_loop`, `_run_session`, `_make_controller`, `_feedback_for_classic`, `_build_metrics`, `_paired_metrics`, `_evaluate_gates`, `_high_capacity_rows`, `_high_capacity_action0_rate`, `_high_capacity_bitrates`, `_is_high_capacity_row`, `_normalize_controller_name` (+5) |  |
| 89 | `core\phase45_v3\neural_mpc_training.py` | 18731 | `Phase45V3NeuralMpcTrainingError`, `ThroughputQuantileTrainingProfile`, `ThroughputQuantileNormalization` | `throughput_quantile_training_profile_by_name`, `train_phase45_v3_throughput_quantile_predictor`, `load_throughput_quantile_examples`, `fit_throughput_quantile_normalization`, `throughput_quantile_examples_to_tensors`, `evaluate_throughput_quantile_predictor`, `_sample_to_arrays`, `_evaluate_training_gates`, `_nearest_quantile_index`, `_resolve_device`, `_seed_everything`, `_mean_std_rows` (+3) |  |
| 90 | `core\phase45_v3\policy_collapse_audit.py` | 15334 | `PolicyCollapseAuditError`, `PolicyCollapseAuditConfig` | `audit_phase6_policy_collapse`, `write_audit_json`, `_evaluate_gates`, `_resolve_result_file`, `_read_csv`, `_rows_by_session`, `_is_high_capacity_safe_row`, `_is_action0`, `_action_values`, `_time_to_reach_by_session`, `_max_consecutive_action0`, `_paired_summary_deltas` (+7) |  |
| 91 | `core\phase45_v3\profiles.py` | 3061 | `Phase45V3ProfileError`, `Phase45V3DatasetProfile` | `profile_by_name` |  |
| 92 | `core\phase45_v3\qh_oracle.py` | 11257 | `Phase45V3QhOracleError`, `QhOracleConfig`, `QhActionValue`, `QhOracleDecision`, `_BeamNode` | `evaluate_qh_actions`, `qh_oracle_card`, `_evaluate_forced_first_action`, `_best_tail_beam`, `_step_with_network`, `_action_value_sort_key`, `_beam_sort_key`, `_infeasible_action`, `_finite_json_number` |  |
| 93 | `core\phase45_v3\qh_scorer_training.py` | 60496 | `Phase45V3QhScorerTrainingError`, `QhScorerTrainingProfile`, `QhScorerNormalization`, `Phase45V3QhScorer`, `Phase45V3TemporalGruQhScorer` | `training_profile_by_name`, `train_phase45_v3_qh_scorer`, `load_qh_scorer_examples`, `fit_qh_scorer_normalization`, `examples_to_tensors`, `_build_qh_scorer_model`, `evaluate_qh_scorer`, `_loss_for_batch`, `_denormalize_q_values`, `_pairwise_qh_rank_loss`, `_soft_q_kl_loss`, `_soft_q_target_probs` (+34) |  |
| 94 | `core\phase45_v3\throughput_quantile_dataset.py` | 30225 | `Phase45V3ThroughputQuantileDatasetError` | `build_phase45_v3_throughput_quantile_dataset`, `validate_phase45_v3_throughput_quantile_dataset_dir`, `_samples_for_window_rollout`, `_build_target`, `harmonic_mean_bps`, `_future_weighted_mean_bps`, `_weighted_future_values`, `_select_rollout_action`, `_floor_bitrate_to_action`, `_validate_sample`, `_sample_errors`, `_build_leakage_audit` (+7) |  |
| 95 | `core\phase45_v3\throughput_quantile_model.py` | 5667 | `Phase45V3ThroughputQuantileModelError`, `ThroughputQuantilePredictor` | `pinball_quantile_loss`, `quantile_crossing_penalty`, `temporal_smoothness_penalty`, `throughput_quantile_loss`, `_validate_prediction_target` |  |
| 96 | `core\phase45_v3\validation.py` | 5892 | `Phase45V3ValidationError` | `validate_phase45_v3_dataset_dir`, `_sample_errors`, `_validation_result` |  |
| 97 | `core\phase6\__init__.py` | 101 |  |  |  |
| 98 | `core\phase6\analysis.py` | 58155 |  | `analyze_phase6_run`, `summarize_session`, `aggregate_summaries`, `paired_statistics`, `evaluate_gates`, `build_ranking`, `generate_phase6_plots`, `render_validation_markdown`, `render_comparative_report`, `render_technical_conclusions`, `bootstrap_ci`, `sign_test_exact` (+40) |  |
| 99 | `core\phase6\catalog.py` | 8451 |  | `preset_spec`, `media_profiles_for_preset`, `discover_comparable_controllers`, `controller_params`, `_safe_alias`, `_mapping`, `_list_or_empty`, `_list_or_none` |  |
| 100 | `core\phase6\config.py` | 5590 |  | `load_phase6_config`, `write_phase6_example_config`, `_select_path`, `_load_mapping_file`, `_deep_merge` |  |
| 101 | `core\phase6\selection.py` | 9317 |  | `load_trace_manifest`, `select_trace_windows`, `is_synthetic_trace`, `_passes_formal_throughput_floor`, `_balanced_pick`, `difficulty_bucket`, `_balance_key`, `_window_start_for_trace`, `_path_rewrites`, `_rewrite_path`, `_stable_token`, `_stable_int` (+2) |  |
| 102 | `core\phase6\verification.py` | 10719 |  | `verify_phase6_package`, `render_phase6_verification_markdown`, `_verify_plots`, `_resolved_plot_path`, `_append_verification_to_validation_markdown`, `_check`, `_failure_reasons`, `_failure_summary`, `_plot_problem_summary`, `_synthetic_reported`, `_legacy_artifact_paths`, `_read_json` (+4) |  |
| 103 | `core\run_context.py` | 12114 | `RunContext` | `create_run_context`, `build_run_manifest`, `build_environment_snapshot`, `git_metadata`, `_create_unique_run_dir`, `_artifact_filename`, `_write_json`, `_python_info`, `_platform_info`, `_module_versions`, `_module_availability`, `_module_status` (+7) |  |
| 104 | `core\runtime_feedback.py` | 1696 |  | `build_controller_feedback` |  |
| 105 | `core\trace_replay\__init__.py` | 666 |  |  |  |
| 106 | `core\trace_replay\controlled_downloader.py` | 8786 | `TraceControlledDownloader` | `compact_loaded_trace_timeline`, `clip_loaded_trace_window`, `_clip_sample`, `_safe_callback` |  |
| 107 | `core\trace_replay\converters\__init__.py` | 143 |  |  |  |
| 108 | `core\trace_replay\converters\base.py` | 4353 | `ConversionResult`, `BaseTraceConverter` |  |  |
| 109 | `core\trace_replay\converters\common.py` | 5400 |  | `slugify`, `stable_id`, `sha256_file`, `path_text`, `find_first_file`, `iter_files_under_hint`, `parse_float`, `parse_datetime`, `median_positive_delta`, `rows_from_timestamps_and_throughput`, `sequential_rows`, `write_normalized_csv` |  |
| 110 | `core\trace_replay\converters\fcc_mba.py` | 4493 | `FccMbaConverter` |  |  |
| 111 | `core\trace_replay\converters\gavist5g.py` | 2394 | `Gavist5GConverter` |  |  |
| 112 | `core\trace_replay\converters\interval_logs.py` | 2788 | `_IntervalLogConverter`, `NorwayHsdpaConverter`, `Ghent4GLteConverter` |  |  |
| 113 | `core\trace_replay\converters\lumos5g.py` | 3821 | `Lumos5GConverter` |  |  |
| 114 | `core\trace_replay\converters\nyu_mets.py` | 1284 | `NyuMetsConverter` |  |  |
| 115 | `core\trace_replay\converters\oboe.py` | 1429 | `OboeConverter` |  |  |
| 116 | `core\trace_replay\converters\puffer.py` | 9980 | `PufferSamplingPolicy`, `PufferConverter` | `_positive_int` |  |
| 117 | `core\trace_replay\converters\registry.py` | 1496 |  | `available_converters`, `converter_by_id` |  |
| 118 | `core\trace_replay\converters\roma.py` | 5306 | `RomaActiveThroughputConverter` |  |  |
| 119 | `core\trace_replay\converters\ucc.py` | 1871 | `_UccDlBitrateConverter`, `Ucc4GBeyondThroughputConverter`, `Ucc5GBeyondThroughputConverter` |  |  |
| 120 | `core\trace_replay\inventory.py` | 5396 | `RawFileInventory` | `sha256_file`, `dataset_id_for_path`, `parser_hint_for_file`, `detect_columns`, `iter_raw_files`, `build_raw_dataset_inventory`, `write_raw_dataset_inventory` |  |
| 121 | `core\trace_replay\loader.py` | 2861 | `TraceLoadError`, `TraceSample`, `LoadedTrace` | `_sample_from_row`, `load_normalized_trace_rows`, `load_normalized_trace_csv` |  |
| 122 | `core\trace_replay\manifest_validation.py` | 7771 | `Phase3ManifestValidationError` | `validate_phase3_trace_manifest_data`, `validate_phase3_trace_manifest_file`, `_require_fields`, `_assert_close`, `_verify_source_hash` |  |
| 123 | `core\trace_replay\network_model.py` | 7896 | `TraceReplayError`, `SegmentDownloadResult`, `TraceDrivenNetworkModel` | `_validate_segment_size_bytes`, `_validate_start_time_s`, `_throughput_kbps_to_bytes_per_second`, `_measured_kbps` |  |
| 124 | `core\trace_replay\quality.py` | 8300 | `TraceQualityPolicy`, `TraceQualityAssessment` | `assess_trace_quality`, `compute_zero_fraction`, `build_quality_audit`, `build_curated_manifest`, `_counter_dict`, `_network_condition` |  |
| 125 | `core\trace_replay\schema.py` | 820 | `NormalizedTraceStats` | `has_required_columns`, `row_projection` |  |
| 126 | `core\trace_replay\splits.py` | 6600 |  | `stable_group_sort_key`, `_split_group_names`, `assign_splits_by_leakage_group`, `assign_stratified_splits_by_semantics`, `split_counts`, `group_counts`, `semantics_counts`, `mark_duplicates`, `build_phase3_trace_manifest` |  |
| 127 | `core\trace_replay\synthetic.py` | 16962 | `SyntheticTraceSourceSpec` | `scenario_ids`, `generate_synthetic_trace_rows`, `generate_synthetic_trace_set`, `merge_synthetic_entries_into_manifest`, `_scenario_values`, `_markovian_mobile_values`, `_choose_state`, `_assign_scenario_splits`, `_counter_dict`, `_split_counts_by_scenario`, `_scenario_rng`, `_validate_generation_inputs` (+2) |  |
| 128 | `core\trace_replay\validation.py` | 3681 | `TraceValidationError` | `_as_float`, `validate_normalized_trace_rows`, `validate_normalized_trace_csv` |  |
| 129 | `core\utils\__init__.py` | 0 |  |  |  |
| 130 | `core\utils\logging.py` | 0 |  |  |  |
| 131 | `main.py` | 11201 |  | `main`, `run_client`, `_configure_logging`, `_create_media_engine`, `_create_downloader`, `_apply_runtime_config`, `_run_with_progress_window`, `_estimate_total_duration`, `_run_legacy_analysis`, `_prompt_for_manual_config` |  |
| 132 | `player.py` | 41978 | `Player` | `_safe_div` |  |
| 133 | `progress_bar.py` | 8485 | `ProgressBarWindow` |  |  |
| 134 | `scripts\analyze_phase45_v3_qh_scorer_errors.py` | 13250 |  | `main`, `analyze_qh_scorer_errors`, `_resolve_model_path`, `_profile_from_checkpoint`, `_normalization_from_checkpoint`, `_summary`, `_summaries_by`, `_count_by`, `_confusion`, `_metadata_value`, `_float_or_none`, `_bucket_buffer` (+6) |  |
| 135 | `scripts\analyze_phase6_results.py` | 1406 |  | `main` |  |
| 136 | `scripts\audit_phase3_raw_datasets.py` | 1695 |  | `main` |  |
| 137 | `scripts\audit_phase3_trace_quality.py` | 3225 |  | `main` |  |
| 138 | `scripts\audit_phase6_policy_collapse.py` | 3057 |  | `main` |  |
| 139 | `scripts\build_phase3_trace_manifest.py` | 2481 |  | `main` |  |
| 140 | `scripts\build_phase45_v1_dataset.py` | 4055 |  | `main`, `_parse_representation_kbps` |  |
| 141 | `scripts\build_phase45_v2_dagger2_dataset.py` | 6103 |  | `main`, `_parse_representation_kbps` |  |
| 142 | `scripts\build_phase45_v2_dataset.py` | 4705 |  | `main`, `_parse_representation_kbps` |  |
| 143 | `scripts\build_phase4_datos_entrenamiento.py` | 2582 |  | `main`, `_parse_representation_kbps` |  |
| 144 | `scripts\build_phase4_datos_teacher_hibrido.py` | 1673 |  | `main` |  |
| 145 | `scripts\build_phase4_training_trace_plan.py` | 4282 |  | `main` |  |
| 146 | `scripts\check_client_readiness.py` | 19303 | `Result` | `main`, `run_checks`, `check_required_docs`, `check_required_imports`, `check_artifact_constants`, `check_legacy_artifact_boundaries`, `check_telemetry_provenance`, `check_benchmark_neutrality`, `check_controller_baseline_entry`, `check_runtime_console_contract`, `check_gstreamer_boundary`, `check_phase3_rebuild_boundary` (+6) |  |
| 147 | `scripts\check_environment.py` | 8836 | `CheckResult` | `main`, `run_profile`, `check_dev_profile`, `check_analysis_profile`, `check_gst_profile`, `_check_python_version`, `_check_modules`, `_check_project_imports`, `_check_gst_tools`, `_import_gst`, `_gst_skip_result`, `_expand_profiles` (+4) |  |
| 148 | `scripts\compute_qoe_from_dry_run.py` | 1494 |  | `main` |  |
| 149 | `scripts\convert_phase3_traces.py` | 4783 |  | `main` |  |
| 150 | `scripts\entrenar_phase4_modelo_candidato.py` | 2576 |  | `main`, `_parse_hidden_sizes` |  |
| 151 | `scripts\entrenar_phase4_modelo_teacher_hibrido.py` | 2922 |  | `main`, `_parse_hidden_sizes` |  |
| 152 | `scripts\evaluate_phase45_v3_neural_mpc_closedloop.py` | 3232 |  | `main`, `_parse_csv` |  |
| 153 | `scripts\export_phase45_v2_spbc_dpo_bundle.py` | 1938 |  | `main` |  |
| 154 | `scripts\export_phase45_v3_neural_mpc_experimental_bundle.py` | 2307 |  | `main`, `_parse_seeds` |  |
| 155 | `scripts\exportar_phase4_bundle_inferencia.py` | 1519 |  | `main` |  |
| 156 | `scripts\exportar_phase4_bundle_teacher_hibrido.py` | 1562 |  | `main` |  |
| 157 | `scripts\generate_contexto_absoluto.py` | 72769 | `MarkdownInfo`, `PythonInfo` | `main`, `build_markdown`, `add_title`, `add_scope_and_sources`, `add_current_state`, `add_operating_model`, `add_environment_architecture`, `add_repository_and_external_layout`, `add_phase_history`, `add_ai_controller_history`, `add_phase6_method`, `add_scientific_corpus` (+28) |  |
| 158 | `scripts\generate_phase3_synthetic_traces.py` | 5084 |  | `main`, `_preserve_snapshot` |  |
| 159 | `scripts\generate_phase45_v3_closedloop_spbc_spc_dataset.py` | 4472 |  | `main`, `_parse_representation_kbps` |  |
| 160 | `scripts\generate_phase45_v3_qh_dataset.py` | 4342 |  | `main`, `_parse_representation_kbps` |  |
| 161 | `scripts\generate_phase45_v3_throughput_quantile_dataset.py` | 4555 |  | `main`, `_parse_ints`, `_parse_floats` |  |
| 162 | `scripts\package_phase3_ubuntu_artifacts.py` | 6957 |  | `main`, `_copy_payload`, `_rewrite_paths`, `_validate_payload_manifests`, `_localize_paths`, `_write_zip`, `_find_windows_path_offenders`, `_assert_under_tfg` |  |
| 163 | `scripts\phase6_gui.py` | 18343 | `Phase6Gui` | `build_phase6_command`, `build_analysis_command`, `build_classic_controlled_command`, `write_gui_override_config`, `_mapping`, `_optional_int`, `parse_phase6_progress_line`, `_format_duration`, `main` |  |
| 164 | `scripts\probar_phase4_inferencia_bundle.py` | 1498 |  | `main` |  |
| 165 | `scripts\revisar_phase4_modelo_candidato.py` | 1962 |  | `main` |  |
| 166 | `scripts\revisar_phase4_modelo_teacher_hibrido.py` | 2466 |  | `main` |  |
| 167 | `scripts\run_phase3_trace_closure.py` | 10486 |  | `main`, `_external_roots`, `_clean_derived_roots`, `_convert_all`, `_run_replay_smoke`, `_try_semantics_replay` |  |
| 168 | `scripts\run_phase4_prueba_rapida_entrenamiento.py` | 1656 |  | `main` |  |
| 169 | `scripts\run_phase6_validacion_comparativa.py` | 24660 |  | `main`, `run_phase6`, `build_phase6_protocol_and_plan`, `build_session`, `write_protocol_package`, `run_session`, `_decode_subprocess_output`, `build_client_config`, `create_package_root`, `resolve_package_root`, `load_existing_protocol_package`, `apply_preset_overrides` (+8) |  |
| 170 | `scripts\run_phase6_verificacion_clasica_controlada.py` | 8827 |  | `main`, `run_controlled_smoke`, `build_client_config`, `render_report`, `_mapping` |  |
| 171 | `scripts\run_qoe_smoke_scenarios.py` | 8103 |  | `main`, `run_qoe_smoke_scenarios`, `_scenarios`, `_write_dry_run_like_artifacts`, `_scenario_passed`, `_assert_clean_target` |  |
| 172 | `scripts\smoke_phase45_v3_neural_mpc_runtime_controller.py` | 3689 |  | `main`, `_smoke_feedback` |  |
| 173 | `scripts\summarize_phase45_v2_anchor_safe_rank.py` | 1441 |  | `main` |  |
| 174 | `scripts\summarize_phase45_v2_anchor_safe_rank_full.py` | 1758 |  | `main` |  |
| 175 | `scripts\summarize_phase45_v2_spbc_ppo_safe_pilot.py` | 8622 |  | `main`, `_report_paths`, `_print_report`, `_print_epoch_diagnostics`, `_failed_checks_text`, `_mapping`, `_value` |  |
| 176 | `scripts\summarize_phase45_v2_spbc_residual_safe_rank_pilot.py` | 4828 |  | `main`, `_print_epoch_diagnostics`, `_failed_checks`, `_value` |  |
| 177 | `scripts\summarize_phase45_v2_spbc_spc_hybrid_offline.py` | 3726 |  | `main`, `_short_delta`, `_focus`, `_spbc2` |  |
| 178 | `scripts\summarize_phase45_v2_spbc_spc_hybrid_veto_sweep.py` | 3274 |  | `main`, `_short_delta` |  |
| 179 | `scripts\summarize_phase45_v2_spc_critic_copilot.py` | 4786 |  | `main`, `_short_delta`, `_value` |  |
| 180 | `scripts\summarize_phase45_v2_spc_reward_risk_dagger2_pilot.py` | 3901 |  | `main`, `_metric_delta` |  |
| 181 | `scripts\summarize_phase45_v3_closedloop_spbc_spc_dataset.py` | 2191 |  | `main`, `_print_compact` |  |
| 182 | `scripts\summarize_phase45_v3_qh_dataset.py` | 3921 |  | `main`, `summarize_phase45_v3_qh_dataset`, `_print_compact` |  |
| 183 | `scripts\train_phase45_v1_spbc_abr.py` | 6495 |  | `main`, `_make_progress_printer`, `_format_seconds` |  |
| 184 | `scripts\train_phase45_v1_spc_abr.py` | 6481 |  | `main`, `_make_progress_printer`, `_format_seconds` |  |
| 185 | `scripts\train_phase45_v2_spbc_dpo.py` | 17210 |  | `main`, `_profile_with_overrides`, `_make_progress_printer`, `_format_seconds` |  |
| 186 | `scripts\train_phase45_v2_spc_reward_risk.py` | 12211 |  | `main`, `_profile_with_overrides`, `_make_progress_printer`, `_format_seconds` |  |
| 187 | `scripts\train_phase45_v3_qh_scorer.py` | 9133 |  | `main`, `_profile_with_overrides`, `_parse_hidden_sizes`, `_print_compact` |  |
| 188 | `scripts\train_phase45_v3_throughput_quantile_predictor.py` | 4910 |  | `main`, `_profile_with_overrides`, `_parse_ints`, `_parse_floats`, `_print_compact` |  |
| 189 | `scripts\validar_phase4_bundle_inferencia.py` | 1736 |  | `main` |  |
| 190 | `scripts\validar_phase4_bundle_teacher_hibrido.py` | 1737 |  | `main` |  |
| 191 | `scripts\validate_phase3_trace_manifest.py` | 1360 |  | `main` |  |
| 192 | `scripts\validate_phase45_v1_spbc_spc_offline.py` | 5154 |  | `main`, `_make_progress_printer`, `_format_seconds` |  |
| 193 | `scripts\validate_phase45_v2_spbc_dpo_bundle.py` | 3499 |  | `main`, `_smoke_feedback` |  |
| 194 | `scripts\validate_phase45_v2_spbc_spc_hybrid_offline.py` | 7012 |  | `main`, `_checkpoint_parent_name`, `_make_progress_printer`, `_format_seconds` |  |
| 195 | `scripts\validate_phase45_v3_neural_mpc_experimental_bundle.py` | 1835 |  | `main` |  |
| 196 | `scripts\validate_phase4_datos_entrenamiento.py` | 958 |  | `main` |  |
| 197 | `scripts\validate_phase4_datos_teacher_hibrido.py` | 984 |  | `main` |  |
| 198 | `scripts\verificar_cliente_y_controllers_clasicos.py` | 37351 | `VerificationResult` | `main`, `default_output_root`, `normalize_controller_list`, `run_theory_probe`, `probe_feedback`, `validate_probe_expectation`, `run_server_smoke`, `build_client_config_yaml`, `audit_run_directory`, `validate_policy_decisions`, `build_summary`, `render_report` (+15) |  |
| 199 | `scripts\verificar_paquete_phase6.py` | 1210 |  | `main` |  |
| 200 | `tests\__init__.py` | 0 |  |  |  |
| 201 | `tests\neural_abr_bundle_utils.py` | 4532 |  | `build_minimal_phase4_bundle`, `minimal_feedback` |  |
| 202 | `tests\spbc_v2_dpo_bundle_utils.py` | 5526 |  | `build_minimal_spbc_v2_dpo_bundle`, `minimal_spbc_feedback`, `_normalization` |  |
| 203 | `tests\test_baseline_entry_contract.py` | 2798 | `BaselineEntryContractTest` |  |  |
| 204 | `tests\test_baseline_registry_audit.py` | 4257 | `BaselineRegistryAuditTest` |  |  |
| 205 | `tests\test_bba_controller.py` | 10597 | `BbaRegistryTest`, `BbaContractTest`, `BbaDecisionTest`, `BbaForbiddenSignalTest` | `feedback`, `_without_key` |  |
| 206 | `tests\test_benchmark_contract.py` | 3961 | `BenchmarkContractTest` |  |  |
| 207 | `tests\test_bola_controller.py` | 13880 | `BolaRegistryTest`, `BolaContractTest`, `BolaDecisionTest`, `BolaForbiddenSignalTest` | `feedback`, `_without_key` |  |
| 208 | `tests\test_client_readiness_check.py` | 837 | `ClientReadinessCheckTest` |  |  |
| 209 | `tests\test_config.py` | 10998 | `ConfigLoadingTest`, `ControllerConfigLookupTest` |  |  |
| 210 | `tests\test_controller_contract.py` | 5830 | `ControllerContractTest` | `complete_feedback` |  |
| 211 | `tests\test_dataset_schema.py` | 3259 | `SegmentTelemetrySchemaTest` |  |  |
| 212 | `tests\test_deterministic_controllers.py` | 6058 | `FixedQualityControllerTest`, `ScriptedQualityControllerTest`, `DeterministicControllerRegistryTest` | `feedback` |  |
| 213 | `tests\test_environment_check.py` | 2742 | `EnvironmentCheckTest` |  |  |
| 214 | `tests\test_fake_client_smoke.py` | 11261 | `FakeSegmentDownloader`, `FakeClientSmokeTest` | `reset_logging` |  |
| 215 | `tests\test_gst_media_engine.py` | 8454 | `FakePad`, `FakeElement`, `FakeBus`, `FakePipeline`, `FakeGst`, `FakeGLib`, `FakeErrorMessage`, `GstMediaEngineContractTest` |  |  |
| 216 | `tests\test_imports.py` | 1585 | `ImportSmokeTest` |  |  |
| 217 | `tests\test_mpc_controller.py` | 18621 | `MpcRegistryTest`, `MpcContractTest`, `MpcDecisionTest`, `MpcCombinatorialSafetyTest`, `MpcForbiddenSignalTest` | `feedback` |  |
| 218 | `tests\test_neural_abr_controller.py` | 4476 | `NeuralAbrControllerTest` |  |  |
| 219 | `tests\test_neural_abr_loader.py` | 4101 | `NeuralAbrLoaderTest` |  |  |
| 220 | `tests\test_neural_abr_player_smoke.py` | 7911 | `FakeSegmentDownloader`, `NeuralAbrPlayerSmokeTest` | `_tiny_mpd`, `_reset_logging` |  |
| 221 | `tests\test_neural_abr_registry.py` | 1707 | `NeuralAbrRegistryTest` |  |  |
| 222 | `tests\test_neural_abr_runtime_features.py` | 3088 | `NeuralAbrRuntimeFeatureTest` |  |  |
| 223 | `tests\test_output_artifacts.py` | 1407 | `OutputArtifactsTest` |  |  |
| 224 | `tests\test_phase1_acceptance_docs.py` | 3789 | `Phase1AcceptanceDocsTest` | `read_doc` |  |
| 225 | `tests\test_phase3_inventory_and_splits.py` | 4209 | `Phase3InventoryAndSplitsTest` |  |  |
| 226 | `tests\test_phase3_manifest_validation.py` | 4992 | `Phase3ManifestValidationTest` |  |  |
| 227 | `tests\test_phase3_network_model.py` | 3197 | `Phase3NetworkModelTest` |  |  |
| 228 | `tests\test_phase3_synthetic_traces.py` | 9152 | `Phase3SyntheticTracesTest` |  |  |
| 229 | `tests\test_phase3_trace_converters.py` | 9301 | `Phase3TraceConvertersTest` | `read_normalized` |  |
| 230 | `tests\test_phase3_trace_quality.py` | 5333 | `Phase3TraceQualityTest` |  |  |
| 231 | `tests\test_phase3_trace_schema.py` | 3189 | `Phase3TraceSchemaTest` |  |  |
| 232 | `tests\test_phase45_v1_dataset.py` | 9679 | `Phase45V1DatasetTest` | `build_manifest_without_files`, `build_manifest_with_trace_files`, `manifest_from_traces`, `trace_record` |  |
| 233 | `tests\test_phase45_v1_offline_validation.py` | 8677 | `Phase45V1OfflineValidationTest` | `build_unit_dataset`, `build_spbc_checkpoint`, `build_spc_checkpoint`, `read_first_jsonl` |  |
| 234 | `tests\test_phase45_v1_spbc_training.py` | 7470 | `Phase45V1SpbcTrainingTest` | `build_unit_dataset` |  |
| 235 | `tests\test_phase45_v1_spc_training.py` | 5854 | `Phase45V1SpcTrainingTest` | `build_unit_dataset` |  |
| 236 | `tests\test_phase45_v2_preference_dataset.py` | 14340 | `Phase45V2PreferenceDatasetTest` | `unit_profile`, `write_stub_spbc_checkpoint`, `write_stub_spbc_v2_dpo_checkpoint`, `build_manifest_with_trace_files` |  |
| 237 | `tests\test_phase45_v2_spbc_dpo_training.py` | 38383 | `Phase45V2SpbcDpoTrainingTest` | `build_unit_v2_dataset` |  |
| 238 | `tests\test_phase45_v2_spbc_spc_hybrid_validation.py` | 5454 | `Phase45V2SpbcSpcHybridValidationTest` | `_write_stub_spbc_v2_checkpoint`, `_write_stub_spc_v2_checkpoint`, `_save_checkpoint` |  |
| 239 | `tests\test_phase45_v2_spc_reward_risk_training.py` | 14565 | `Phase45V2SpcRewardRiskTrainingTest` |  |  |
| 240 | `tests\test_phase45_v3_anti_collapse_gate.py` | 4610 | `Phase45V3AntiCollapseGateTest` | `_write_phase6_package`, `_write_csv` |  |
| 241 | `tests\test_phase45_v3_closed_loop_env_step.py` | 1207 | `Phase45V3ClosedLoopEnvStepTest` |  |  |
| 242 | `tests\test_phase45_v3_closedloop_spbc_spc_dataset.py` | 4970 | `Phase45V3ClosedLoopSpbcSpcDatasetTest` |  |  |
| 243 | `tests\test_phase45_v3_dataset.py` | 9180 | `Phase45V3DatasetTest` |  |  |
| 244 | `tests\test_phase45_v3_neural_mpc_bundle.py` | 8451 | `Phase45V3NeuralMpcBundleTests` |  |  |
| 245 | `tests\test_phase45_v3_neural_mpc_no_collapse.py` | 1743 | `Phase45V3NeuralMpcNoCollapseTest` |  |  |
| 246 | `tests\test_phase45_v3_neural_mpc_planner.py` | 3374 | `Phase45V3NeuralMpcPlannerTest` |  |  |
| 247 | `tests\test_phase45_v3_neural_mpc_runtime_controller.py` | 6885 | `Phase45V3NeuralMpcRuntimeControllerTests` |  |  |
| 248 | `tests\test_phase45_v3_neural_mpc_v2_controller.py` | 1026 | `Phase45V3NeuralMpcV2ControllerTest` |  |  |
| 249 | `tests\test_phase45_v3_qh_oracle.py` | 2626 | `Phase45V3QhOracleTest` | `_constant_network_model`, `_value_by_action` |  |
| 250 | `tests\test_phase45_v3_qh_scorer_losses.py` | 8158 | `Phase45V3QhScorerLossesTest` |  |  |
| 251 | `tests\test_phase45_v3_qoe_parity.py` | 1106 | `Phase45V3QoEParityTest` |  |  |
| 252 | `tests\test_phase45_v3_state_builder_parity.py` | 1499 | `Phase45V3StateBuilderParityTest` |  |  |
| 253 | `tests\test_phase45_v3_throughput_quantile_dataset.py` | 3310 | `Phase45V3ThroughputQuantileDatasetTest` |  |  |
| 254 | `tests\test_phase45_v3_throughput_quantile_loss.py` | 1464 | `Phase45V3ThroughputQuantileLossTest` |  |  |
| 255 | `tests\test_phase45_v3_throughput_quantile_training_profile.py` | 809 | `Phase45V3ThroughputQuantileTrainingProfileTest` |  |  |
| 256 | `tests\test_phase4_bundle_inferencia.py` | 5104 | `Phase4BundleInferenciaTest` | `_build_ready_candidate` |  |
| 257 | `tests\test_phase4_datos_entrenamiento.py` | 8280 | `Phase4DatosEntrenamientoTest` | `build_manifest_with_trace_files`, `write_trace_record` |  |
| 258 | `tests\test_phase4_modelo_candidato.py` | 3817 | `Phase4ModeloCandidatoTest` |  |  |
| 259 | `tests\test_phase4_teacher_hibrido.py` | 6596 | `Phase4TeacherHibridoTest` | `_build_small_plan` |  |
| 260 | `tests\test_phase4_training_trace_plan.py` | 8241 | `Phase4TrainingTracePlanTest` | `build_manifest`, `trace_record` |  |
| 261 | `tests\test_phase6_pipeline.py` | 33891 | `Phase6SelectionTest`, `TraceControlledDownloaderTest`, `Phase6AnalysisTest`, `Phase6RunnerAndGuiTest`, `FakeBaseDownloader` | `_trace`, `_session`, `_write_run`, `_read_csv`, `_as_float` |  |
| 262 | `tests\test_player_fragment_flow.py` | 10669 | `RecordingFakeMediaEngine`, `RecordingDownloader`, `PlayerFragmentFlowTest` | `reset_logging`, `_single_run_dir`, `_mpd_text`, `_client_config` |  |
| 263 | `tests\test_qoe_artifacts.py` | 6875 | `QoEArtifactsTest` |  |  |
| 264 | `tests\test_qoe_metrics.py` | 3371 | `QoEMetricsTest` |  |  |
| 265 | `tests\test_qoe_smoke_scenarios.py` | 1738 | `QoESmokeScenariosTest` |  |  |
| 266 | `tests\test_rate_based_controller.py` | 10295 | `RateBasedRegistryTest`, `RateBasedContractTest`, `RateBasedDecisionTest`, `RateBasedTransitionTest`, `RateBasedForbiddenSignalTest` | `feedback` |  |
| 267 | `tests\test_robust_mpc_controller.py` | 17462 | `RobustMpcRegistryTest`, `RobustMpcContractTest`, `RobustMpcCorrectionTest`, `RobustMpcCompatibilityTest`, `RobustMpcForbiddenSignalTest` | `feedback` |  |
| 268 | `tests\test_run_context.py` | 5563 | `RunContextTest` |  |  |
| 269 | `tests\test_runtime_feedback.py` | 4213 | `_FakeMediaEngine`, `_FakeDownloader`, `_FakeController`, `RuntimeFeedbackTest` |  |  |
| 270 | `tests\test_runtime_output_contract_docs.py` | 1758 | `RuntimeOutputContractDocsTest` |  |  |
| 271 | `tests\test_sanity_rate_controllers.py` | 10836 | `SanityControllerRegistryTest`, `SanityControllerContractTest`, `MinRateControllerTest`, `MaxRateControllerTest`, `FixedRateControllerTest`, `FixedRateUnitConversionTest` | `feedback` |  |
| 272 | `tests\test_spbc_v2_dpo_controller.py` | 7936 | `SpbcV2DpoControllerTest` | `_training_normalization` |  |
| 273 | `tests\test_telemetry_column_provenance_docs.py` | 2818 | `TelemetryColumnProvenanceDocsTest` |  |  |
| 274 | `tests\test_verificacion_cliente_controllers_clasicos.py` | 6132 | `VerificacionTheoryProbeTest`, `VerificacionRunAuditTest` | `build_fake_run` |  |

### Catalogo scripts

| # | Ruta | Tipo | Bytes |
|---:|---|---|---:|
| 1 | `scripts\analyze_phase45_v3_qh_scorer_errors.py` | `.py` | 13250 |
| 2 | `scripts\analyze_phase6_results.py` | `.py` | 1406 |
| 3 | `scripts\audit_phase3_raw_datasets.py` | `.py` | 1695 |
| 4 | `scripts\audit_phase3_trace_quality.py` | `.py` | 3225 |
| 5 | `scripts\audit_phase6_policy_collapse.py` | `.py` | 3057 |
| 6 | `scripts\build_phase3_trace_manifest.py` | `.py` | 2481 |
| 7 | `scripts\build_phase45_v1_dataset.py` | `.py` | 4055 |
| 8 | `scripts\build_phase45_v2_dagger2_dataset.py` | `.py` | 6103 |
| 9 | `scripts\build_phase45_v2_dataset.py` | `.py` | 4705 |
| 10 | `scripts\build_phase4_datos_entrenamiento.py` | `.py` | 2582 |
| 11 | `scripts\build_phase4_datos_teacher_hibrido.py` | `.py` | 1673 |
| 12 | `scripts\build_phase4_training_trace_plan.py` | `.py` | 4282 |
| 13 | `scripts\check_client_readiness.py` | `.py` | 19303 |
| 14 | `scripts\check_environment.py` | `.py` | 8836 |
| 15 | `scripts\compute_qoe_from_dry_run.py` | `.py` | 1494 |
| 16 | `scripts\convert_phase3_traces.py` | `.py` | 4783 |
| 17 | `scripts\entrenar_phase4_modelo_candidato.py` | `.py` | 2576 |
| 18 | `scripts\entrenar_phase4_modelo_teacher_hibrido.py` | `.py` | 2922 |
| 19 | `scripts\evaluate_phase45_v3_neural_mpc_closedloop.py` | `.py` | 3232 |
| 20 | `scripts\export_phase45_v2_spbc_dpo_bundle.py` | `.py` | 1938 |
| 21 | `scripts\export_phase45_v3_neural_mpc_experimental_bundle.py` | `.py` | 2307 |
| 22 | `scripts\export_phase45_v3_neural_mpc_experimental_bundle_v2_wsl.sh` | `.sh` | 1508 |
| 23 | `scripts\export_phase45_v3_neural_mpc_experimental_bundle_wsl.sh` | `.sh` | 1316 |
| 24 | `scripts\exportar_phase4_bundle_inferencia.py` | `.py` | 1519 |
| 25 | `scripts\exportar_phase4_bundle_teacher_hibrido.py` | `.py` | 1562 |
| 26 | `scripts\generate_contexto_absoluto.py` | `.py` | 72769 |
| 27 | `scripts\generate_phase3_synthetic_traces.py` | `.py` | 5084 |
| 28 | `scripts\generate_phase45_v3_closedloop_spbc_spc_dataset.py` | `.py` | 4472 |
| 29 | `scripts\generate_phase45_v3_closedloop_spbc_spc_full_dataset_wsl.sh` | `.sh` | 709 |
| 30 | `scripts\generate_phase45_v3_closedloop_spbc_spc_pilot_dataset_wsl.sh` | `.sh` | 707 |
| 31 | `scripts\generate_phase45_v3_neural_mpc_full_dataset_v2_wsl.sh` | `.sh` | 767 |
| 32 | `scripts\generate_phase45_v3_qh_dataset.py` | `.py` | 4342 |
| 33 | `scripts\generate_phase45_v3_throughput_quantile_dataset.py` | `.py` | 4555 |
| 34 | `scripts\package_phase3_ubuntu_artifacts.py` | `.py` | 6957 |
| 35 | `scripts\package_phase45_v3_neural_mpc_experimental_bundle_transfer_wsl.sh` | `.sh` | 1897 |
| 36 | `scripts\package_phase45_v3_neural_mpc_experimental_bundle_v2_transfer_wsl.sh` | `.sh` | 450 |
| 37 | `scripts\phase6_gui.py` | `.py` | 18343 |
| 38 | `scripts\print_phase45_v3_neural_mpc_expanded_diagnostic_summary_wsl.sh` | `.sh` | 7012 |
| 39 | `scripts\print_phase45_v3_neural_mpc_experimental_bundle_summary_ubuntu_cliente.sh` | `.sh` | 140 |
| 40 | `scripts\print_phase45_v3_neural_mpc_experimental_bundle_summary_wsl.sh` | `.sh` | 3279 |
| 41 | `scripts\print_phase45_v3_neural_mpc_experimental_bundle_v2_summary_wsl.sh` | `.sh` | 285 |
| 42 | `scripts\print_phase45_v3_neural_mpc_experimental_candidate_readiness_wsl.sh` | `.sh` | 4395 |
| 43 | `scripts\print_phase45_v3_neural_mpc_full_dataset_v2_summary_wsl.sh` | `.sh` | 3894 |
| 44 | `scripts\print_phase45_v3_neural_mpc_full_training_v2_summary_wsl.sh` | `.sh` | 7296 |
| 45 | `scripts\probar_phase4_inferencia_bundle.py` | `.py` | 1498 |
| 46 | `scripts\revisar_phase4_modelo_candidato.py` | `.py` | 1962 |
| 47 | `scripts\revisar_phase4_modelo_teacher_hibrido.py` | `.py` | 2466 |
| 48 | `scripts\run_phase3_trace_closure.py` | `.py` | 10486 |
| 49 | `scripts\run_phase45_v2_anchor_safe_rank_full_wsl.sh` | `.sh` | 1782 |
| 50 | `scripts\run_phase45_v2_anchor_safe_rank_wsl.sh` | `.sh` | 2020 |
| 51 | `scripts\run_phase45_v2_spbc_ppo_safe_pilot_wsl.sh` | `.sh` | 2643 |
| 52 | `scripts\run_phase45_v2_spbc_residual_safe_rank_pilot_wsl.sh` | `.sh` | 2248 |
| 53 | `scripts\run_phase45_v2_spbc_safe_advantage_probe_wsl.sh` | `.sh` | 2991 |
| 54 | `scripts\run_phase45_v2_spbc_spc_hybrid_offline_wsl.sh` | `.sh` | 1353 |
| 55 | `scripts\run_phase45_v2_spbc_spc_hybrid_veto_sweep_wsl.sh` | `.sh` | 1577 |
| 56 | `scripts\run_phase45_v2_spc_critic_copilot_wsl.sh` | `.sh` | 2323 |
| 57 | `scripts\run_phase45_v2_spc_reward_risk_dagger2_pilot_wsl.sh` | `.sh` | 1854 |
| 58 | `scripts\run_phase45_v2_spc_reward_risk_dagger2_safe_rank_pilot_wsl.sh` | `.sh` | 1980 |
| 59 | `scripts\run_phase45_v3_neural_mpc_expanded_diagnostic_wsl.sh` | `.sh` | 2344 |
| 60 | `scripts\run_phase45_v3_neural_mpc_full_training_v2_wsl.sh` | `.sh` | 2060 |
| 61 | `scripts\run_phase45_v3_neural_mpc_pilot_wsl.sh` | `.sh` | 1346 |
| 62 | `scripts\run_phase45_v3_qh_scorer_pilot_adv_regret_gru_wsl.sh` | `.sh` | 919 |
| 63 | `scripts\run_phase45_v3_qh_scorer_pilot_adv_regret_hardneg_v2_wsl.sh` | `.sh` | 941 |
| 64 | `scripts\run_phase45_v3_qh_scorer_pilot_adv_regret_hardneg_wsl.sh` | `.sh` | 935 |
| 65 | `scripts\run_phase45_v3_qh_scorer_pilot_adv_regret_wsl.sh` | `.sh` | 915 |
| 66 | `scripts\run_phase45_v3_qh_scorer_pilot_rank_wsl.sh` | `.sh` | 561 |
| 67 | `scripts\run_phase4_prueba_rapida_entrenamiento.py` | `.py` | 1656 |
| 68 | `scripts\run_phase6_validacion_comparativa.py` | `.py` | 24660 |
| 69 | `scripts\run_phase6_verificacion_clasica_controlada.py` | `.py` | 8827 |
| 70 | `scripts\run_qoe_smoke_scenarios.py` | `.py` | 8103 |
| 71 | `scripts\smoke_phase45_v3_neural_mpc_runtime_controller.py` | `.py` | 3689 |
| 72 | `scripts\smoke_phase45_v3_neural_mpc_runtime_controller_ubuntu_cliente.sh` | `.sh` | 669 |
| 73 | `scripts\smoke_phase45_v3_neural_mpc_runtime_controller_v2_ubuntu_cliente.sh` | `.sh` | 375 |
| 74 | `scripts\summarize_phase45_v2_anchor_safe_rank.py` | `.py` | 1441 |
| 75 | `scripts\summarize_phase45_v2_anchor_safe_rank_full.py` | `.py` | 1758 |
| 76 | `scripts\summarize_phase45_v2_spbc_ppo_safe_pilot.py` | `.py` | 8622 |
| 77 | `scripts\summarize_phase45_v2_spbc_residual_safe_rank_pilot.py` | `.py` | 4828 |
| 78 | `scripts\summarize_phase45_v2_spbc_spc_hybrid_offline.py` | `.py` | 3726 |
| 79 | `scripts\summarize_phase45_v2_spbc_spc_hybrid_veto_sweep.py` | `.py` | 3274 |
| 80 | `scripts\summarize_phase45_v2_spc_critic_copilot.py` | `.py` | 4786 |
| 81 | `scripts\summarize_phase45_v2_spc_reward_risk_dagger2_pilot.py` | `.py` | 3901 |
| 82 | `scripts\summarize_phase45_v3_closedloop_spbc_spc_dataset.py` | `.py` | 2191 |
| 83 | `scripts\summarize_phase45_v3_qh_dataset.py` | `.py` | 3921 |
| 84 | `scripts\train_phase45_v1_spbc_abr.py` | `.py` | 6495 |
| 85 | `scripts\train_phase45_v1_spc_abr.py` | `.py` | 6481 |
| 86 | `scripts\train_phase45_v2_spbc_dpo.py` | `.py` | 17210 |
| 87 | `scripts\train_phase45_v2_spc_reward_risk.py` | `.py` | 12211 |
| 88 | `scripts\train_phase45_v3_qh_scorer.py` | `.py` | 9133 |
| 89 | `scripts\train_phase45_v3_throughput_quantile_predictor.py` | `.py` | 4910 |
| 90 | `scripts\unpack_phase45_v3_neural_mpc_experimental_bundle_ubuntu_cliente.sh` | `.sh` | 908 |
| 91 | `scripts\unpack_phase45_v3_neural_mpc_experimental_bundle_v2_ubuntu_cliente.sh` | `.sh` | 479 |
| 92 | `scripts\validar_phase4_bundle_inferencia.py` | `.py` | 1736 |
| 93 | `scripts\validar_phase4_bundle_teacher_hibrido.py` | `.py` | 1737 |
| 94 | `scripts\validate_phase3_trace_manifest.py` | `.py` | 1360 |
| 95 | `scripts\validate_phase45_v1_spbc_spc_offline.py` | `.py` | 5154 |
| 96 | `scripts\validate_phase45_v2_spbc_dpo_bundle.py` | `.py` | 3499 |
| 97 | `scripts\validate_phase45_v2_spbc_spc_hybrid_offline.py` | `.py` | 7012 |
| 98 | `scripts\validate_phase45_v3_neural_mpc_experimental_bundle.py` | `.py` | 1835 |
| 99 | `scripts\validate_phase45_v3_neural_mpc_experimental_bundle_ubuntu_cliente.sh` | `.sh` | 595 |
| 100 | `scripts\validate_phase4_datos_entrenamiento.py` | `.py` | 958 |
| 101 | `scripts\validate_phase4_datos_teacher_hibrido.py` | `.py` | 984 |
| 102 | `scripts\verificar_cliente_y_controllers_clasicos.py` | `.py` | 37351 |
| 103 | `scripts\verificar_paquete_phase6.py` | `.py` | 1210 |

### Catalogo tests

| # | Ruta | Bytes |
|---:|---|---:|
| 1 | `tests\__init__.py` | 0 |
| 2 | `tests\neural_abr_bundle_utils.py` | 4532 |
| 3 | `tests\spbc_v2_dpo_bundle_utils.py` | 5526 |
| 4 | `tests\test_baseline_entry_contract.py` | 2798 |
| 5 | `tests\test_baseline_registry_audit.py` | 4257 |
| 6 | `tests\test_bba_controller.py` | 10597 |
| 7 | `tests\test_benchmark_contract.py` | 3961 |
| 8 | `tests\test_bola_controller.py` | 13880 |
| 9 | `tests\test_client_readiness_check.py` | 837 |
| 10 | `tests\test_config.py` | 10998 |
| 11 | `tests\test_controller_contract.py` | 5830 |
| 12 | `tests\test_dataset_schema.py` | 3259 |
| 13 | `tests\test_deterministic_controllers.py` | 6058 |
| 14 | `tests\test_environment_check.py` | 2742 |
| 15 | `tests\test_fake_client_smoke.py` | 11261 |
| 16 | `tests\test_gst_media_engine.py` | 8454 |
| 17 | `tests\test_imports.py` | 1585 |
| 18 | `tests\test_mpc_controller.py` | 18621 |
| 19 | `tests\test_neural_abr_controller.py` | 4476 |
| 20 | `tests\test_neural_abr_loader.py` | 4101 |
| 21 | `tests\test_neural_abr_player_smoke.py` | 7911 |
| 22 | `tests\test_neural_abr_registry.py` | 1707 |
| 23 | `tests\test_neural_abr_runtime_features.py` | 3088 |
| 24 | `tests\test_output_artifacts.py` | 1407 |
| 25 | `tests\test_phase1_acceptance_docs.py` | 3789 |
| 26 | `tests\test_phase3_inventory_and_splits.py` | 4209 |
| 27 | `tests\test_phase3_manifest_validation.py` | 4992 |
| 28 | `tests\test_phase3_network_model.py` | 3197 |
| 29 | `tests\test_phase3_synthetic_traces.py` | 9152 |
| 30 | `tests\test_phase3_trace_converters.py` | 9301 |
| 31 | `tests\test_phase3_trace_quality.py` | 5333 |
| 32 | `tests\test_phase3_trace_schema.py` | 3189 |
| 33 | `tests\test_phase45_v1_dataset.py` | 9679 |
| 34 | `tests\test_phase45_v1_offline_validation.py` | 8677 |
| 35 | `tests\test_phase45_v1_spbc_training.py` | 7470 |
| 36 | `tests\test_phase45_v1_spc_training.py` | 5854 |
| 37 | `tests\test_phase45_v2_preference_dataset.py` | 14340 |
| 38 | `tests\test_phase45_v2_spbc_dpo_training.py` | 38383 |
| 39 | `tests\test_phase45_v2_spbc_spc_hybrid_validation.py` | 5454 |
| 40 | `tests\test_phase45_v2_spc_reward_risk_training.py` | 14565 |
| 41 | `tests\test_phase45_v3_anti_collapse_gate.py` | 4610 |
| 42 | `tests\test_phase45_v3_closed_loop_env_step.py` | 1207 |
| 43 | `tests\test_phase45_v3_closedloop_spbc_spc_dataset.py` | 4970 |
| 44 | `tests\test_phase45_v3_dataset.py` | 9180 |
| 45 | `tests\test_phase45_v3_neural_mpc_bundle.py` | 8451 |
| 46 | `tests\test_phase45_v3_neural_mpc_no_collapse.py` | 1743 |
| 47 | `tests\test_phase45_v3_neural_mpc_planner.py` | 3374 |
| 48 | `tests\test_phase45_v3_neural_mpc_runtime_controller.py` | 6885 |
| 49 | `tests\test_phase45_v3_neural_mpc_v2_controller.py` | 1026 |
| 50 | `tests\test_phase45_v3_qh_oracle.py` | 2626 |
| 51 | `tests\test_phase45_v3_qh_scorer_losses.py` | 8158 |
| 52 | `tests\test_phase45_v3_qoe_parity.py` | 1106 |
| 53 | `tests\test_phase45_v3_state_builder_parity.py` | 1499 |
| 54 | `tests\test_phase45_v3_throughput_quantile_dataset.py` | 3310 |
| 55 | `tests\test_phase45_v3_throughput_quantile_loss.py` | 1464 |
| 56 | `tests\test_phase45_v3_throughput_quantile_training_profile.py` | 809 |
| 57 | `tests\test_phase4_bundle_inferencia.py` | 5104 |
| 58 | `tests\test_phase4_datos_entrenamiento.py` | 8280 |
| 59 | `tests\test_phase4_modelo_candidato.py` | 3817 |
| 60 | `tests\test_phase4_teacher_hibrido.py` | 6596 |
| 61 | `tests\test_phase4_training_trace_plan.py` | 8241 |
| 62 | `tests\test_phase6_pipeline.py` | 33891 |
| 63 | `tests\test_player_fragment_flow.py` | 10669 |
| 64 | `tests\test_qoe_artifacts.py` | 6875 |
| 65 | `tests\test_qoe_metrics.py` | 3371 |
| 66 | `tests\test_qoe_smoke_scenarios.py` | 1738 |
| 67 | `tests\test_rate_based_controller.py` | 10295 |
| 68 | `tests\test_robust_mpc_controller.py` | 17462 |
| 69 | `tests\test_run_context.py` | 5563 |
| 70 | `tests\test_runtime_feedback.py` | 4213 |
| 71 | `tests\test_runtime_output_contract_docs.py` | 1758 |
| 72 | `tests\test_sanity_rate_controllers.py` | 10836 |
| 73 | `tests\test_spbc_v2_dpo_controller.py` | 7936 |
| 74 | `tests\test_telemetry_column_provenance_docs.py` | 2818 |
| 75 | `tests\test_verificacion_cliente_controllers_clasicos.py` | 6132 |

### Catalogo de directorios externos bajo raiz TFG

| # | Profundidad | Ruta relativa | Directorios hijos | Archivos hijos |
|---:|---:|---|---:|---:|
| 1 | 0 | `.` | 15 | 0 |
| 2 | 1 | `20260608_160906_rapido` | 5 | 0 |
| 3 | 1 | `20260608_193615_equilibrado` | 5 | 0 |
| 4 | 1 | `20260611_193501_diagnostico` | 5 | 0 |
| 5 | 1 | `20260611_202406_rapido` | 5 | 0 |
| 6 | 1 | `20260615_110912_diagnostico` | 5 | 0 |
| 7 | 1 | `20260615_112752_rapido` | 5 | 0 |
| 8 | 1 | `20260615_141628_diagnostico` | 5 | 0 |
| 9 | 1 | `abr ia pdf` | 1 | 0 |
| 10 | 1 | `auditorias_trazas` | 2 | 0 |
| 11 | 1 | `DashClientModular4` | 9 | 9 |
| 12 | 1 | `dataset en bruto` | 9 | 1 |
| 13 | 1 | `datasets_normalizados` | 2 | 0 |
| 14 | 1 | `manifests_trazas` | 2 | 0 |
| 15 | 1 | `modelos` | 1 | 0 |
| 16 | 1 | `runs_trazas` | 6 | 0 |
| 17 | 2 | `20260608_160906_rapido\00_protocolo` | 1 | 6 |
| 18 | 2 | `20260608_160906_rapido\01_ejecucion` | 2 | 0 |
| 19 | 2 | `20260608_160906_rapido\02_resultados` | 0 | 8 |
| 20 | 2 | `20260608_160906_rapido\03_graficas` | 0 | 15 |
| 21 | 2 | `20260608_160906_rapido\04_informe` | 0 | 3 |
| 22 | 2 | `20260608_193615_equilibrado\00_protocolo` | 1 | 6 |
| 23 | 2 | `20260608_193615_equilibrado\01_ejecucion` | 2 | 0 |
| 24 | 2 | `20260608_193615_equilibrado\02_resultados` | 0 | 0 |
| 25 | 2 | `20260608_193615_equilibrado\03_graficas` | 0 | 0 |
| 26 | 2 | `20260608_193615_equilibrado\04_informe` | 0 | 0 |
| 27 | 2 | `20260611_193501_diagnostico\00_protocolo` | 1 | 6 |
| 28 | 2 | `20260611_193501_diagnostico\01_ejecucion` | 2 | 0 |
| 29 | 2 | `20260611_193501_diagnostico\02_resultados` | 0 | 8 |
| 30 | 2 | `20260611_193501_diagnostico\03_graficas` | 0 | 15 |
| 31 | 2 | `20260611_193501_diagnostico\04_informe` | 0 | 3 |
| 32 | 2 | `20260611_202406_rapido\00_protocolo` | 1 | 6 |
| 33 | 2 | `20260611_202406_rapido\01_ejecucion` | 2 | 0 |
| 34 | 2 | `20260611_202406_rapido\02_resultados` | 0 | 8 |
| 35 | 2 | `20260611_202406_rapido\03_graficas` | 0 | 15 |
| 36 | 2 | `20260611_202406_rapido\04_informe` | 0 | 3 |
| 37 | 2 | `20260615_110912_diagnostico\00_protocolo` | 1 | 6 |
| 38 | 2 | `20260615_110912_diagnostico\01_ejecucion` | 2 | 0 |
| 39 | 2 | `20260615_110912_diagnostico\02_resultados` | 0 | 8 |
| 40 | 2 | `20260615_110912_diagnostico\03_graficas` | 0 | 15 |
| 41 | 2 | `20260615_110912_diagnostico\04_informe` | 0 | 3 |
| 42 | 2 | `20260615_112752_rapido\00_protocolo` | 1 | 6 |
| 43 | 2 | `20260615_112752_rapido\01_ejecucion` | 2 | 0 |
| 44 | 2 | `20260615_112752_rapido\02_resultados` | 0 | 8 |
| 45 | 2 | `20260615_112752_rapido\03_graficas` | 0 | 15 |
| 46 | 2 | `20260615_112752_rapido\04_informe` | 0 | 3 |
| 47 | 2 | `20260615_141628_diagnostico\00_protocolo` | 1 | 6 |
| 48 | 2 | `20260615_141628_diagnostico\01_ejecucion` | 2 | 0 |
| 49 | 2 | `20260615_141628_diagnostico\02_resultados` | 0 | 8 |
| 50 | 2 | `20260615_141628_diagnostico\03_graficas` | 0 | 15 |
| 51 | 2 | `20260615_141628_diagnostico\04_informe` | 0 | 3 |
| 52 | 2 | `abr ia pdf\abr ia pdf` | 0 | 32 |
| 53 | 2 | `auditorias_trazas\phase3` | 1 | 0 |
| 54 | 2 | `auditorias_trazas\phase4_5_v1_pdf_text_tmp` | 0 | 32 |
| 55 | 2 | `DashClientModular4\.idea` | 1 | 6 |
| 56 | 2 | `DashClientModular4\analysis_output` | 0 | 0 |
| 57 | 2 | `DashClientModular4\config` | 0 | 4 |
| 58 | 2 | `DashClientModular4\core` | 10 | 8 |
| 59 | 2 | `DashClientModular4\docs` | 7 | 0 |
| 60 | 2 | `DashClientModular4\logs` | 0 | 0 |
| 61 | 2 | `DashClientModular4\output` | 1 | 0 |
| 62 | 2 | `DashClientModular4\scripts` | 3 | 103 |
| 63 | 2 | `DashClientModular4\tests` | 0 | 75 |
| 64 | 2 | `dataset en bruto\BelgiumGhent 4G UGentIDLab LTE traces` | 0 | 40 |
| 65 | 2 | `dataset en bruto\beyond_throughput_4g_lte` | 5 | 0 |
| 66 | 2 | `dataset en bruto\FCC Measuring Broadband America` | 1 | 0 |
| 67 | 2 | `dataset en bruto\GAViST5G (Gaming and Video Streaming Traffic for 5G)` | 2 | 0 |
| 68 | 2 | `dataset en bruto\Large Scale Dataset of 4G NB-IoT and 5G Non-Standalone Network Measurements` | 0 | 5 |
| 69 | 2 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS` | 4 | 0 |
| 70 | 2 | `dataset en bruto\Norway HSDPA (UMass trace archive)` | 11 | 0 |
| 71 | 2 | `dataset en bruto\oboe` | 1 | 0 |
| 72 | 2 | `dataset en bruto\Puffer` | 0 | 4 |
| 73 | 2 | `datasets_normalizados\phase3` | 1 | 0 |
| 74 | 2 | `datasets_normalizados\phase4` | 2 | 0 |
| 75 | 2 | `manifests_trazas\phase3` | 1 | 0 |
| 76 | 2 | `manifests_trazas\phase4` | 2 | 0 |
| 77 | 2 | `modelos\phase4` | 4 | 0 |
| 78 | 2 | `runs_trazas\fase_verificacion_cliente_y_controllers_clasicos` | 3 | 2 |
| 79 | 2 | `runs_trazas\phase3` | 1 | 0 |
| 80 | 2 | `runs_trazas\phase3_5` | 1 | 0 |
| 81 | 2 | `runs_trazas\phase4` | 3 | 0 |
| 82 | 2 | `runs_trazas\phase5` | 3 | 0 |
| 83 | 2 | `runs_trazas\phase6` | 1 | 0 |
| 84 | 3 | `20260608_160906_rapido\00_protocolo\client_configs` | 0 | 70 |
| 85 | 3 | `20260608_160906_rapido\01_ejecucion\command_logs` | 0 | 70 |
| 86 | 3 | `20260608_160906_rapido\01_ejecucion\runs` | 70 | 0 |
| 87 | 3 | `20260608_193615_equilibrado\00_protocolo\client_configs` | 0 | 80 |
| 88 | 3 | `20260608_193615_equilibrado\01_ejecucion\command_logs` | 0 | 79 |
| 89 | 3 | `20260608_193615_equilibrado\01_ejecucion\runs` | 80 | 0 |
| 90 | 3 | `20260611_193501_diagnostico\00_protocolo\client_configs` | 0 | 6 |
| 91 | 3 | `20260611_193501_diagnostico\01_ejecucion\command_logs` | 0 | 6 |
| 92 | 3 | `20260611_193501_diagnostico\01_ejecucion\runs` | 6 | 0 |
| 93 | 3 | `20260611_202406_rapido\00_protocolo\client_configs` | 0 | 20 |
| 94 | 3 | `20260611_202406_rapido\01_ejecucion\command_logs` | 0 | 20 |
| 95 | 3 | `20260611_202406_rapido\01_ejecucion\runs` | 20 | 0 |
| 96 | 3 | `20260615_110912_diagnostico\00_protocolo\client_configs` | 0 | 12 |
| 97 | 3 | `20260615_110912_diagnostico\01_ejecucion\command_logs` | 0 | 12 |
| 98 | 3 | `20260615_110912_diagnostico\01_ejecucion\runs` | 12 | 0 |
| 99 | 3 | `20260615_112752_rapido\00_protocolo\client_configs` | 0 | 40 |
| 100 | 3 | `20260615_112752_rapido\01_ejecucion\command_logs` | 0 | 40 |
| 101 | 3 | `20260615_112752_rapido\01_ejecucion\runs` | 40 | 0 |
| 102 | 3 | `20260615_141628_diagnostico\00_protocolo\client_configs` | 0 | 6 |
| 103 | 3 | `20260615_141628_diagnostico\01_ejecucion\command_logs` | 0 | 6 |
| 104 | 3 | `20260615_141628_diagnostico\01_ejecucion\runs` | 6 | 0 |
| 105 | 3 | `auditorias_trazas\phase3\final` | 0 | 3 |
| 106 | 3 | `DashClientModular4\.idea\inspectionProfiles` | 0 | 1 |
| 107 | 3 | `DashClientModular4\core\controller` | 0 | 21 |
| 108 | 3 | `DashClientModular4\core\evaluation` | 0 | 3 |
| 109 | 3 | `DashClientModular4\core\media_engine` | 0 | 4 |
| 110 | 3 | `DashClientModular4\core\neural_abr` | 0 | 23 |
| 111 | 3 | `DashClientModular4\core\parser` | 0 | 4 |
| 112 | 3 | `DashClientModular4\core\phase45_v1` | 0 | 18 |
| 113 | 3 | `DashClientModular4\core\phase45_v3` | 0 | 16 |
| 114 | 3 | `DashClientModular4\core\phase6` | 0 | 6 |
| 115 | 3 | `DashClientModular4\core\trace_replay` | 1 | 11 |
| 116 | 3 | `DashClientModular4\core\utils` | 0 | 2 |
| 117 | 3 | `DashClientModular4\docs\arquitectura y procedimientos estandar tfg dash` | 0 | 2 |
| 118 | 3 | `DashClientModular4\docs\contexto del orquestador el chat web` | 0 | 1 |
| 119 | 3 | `DashClientModular4\docs\contexto rama nueva` | 8 | 1 |
| 120 | 3 | `DashClientModular4\docs\contexto rama original` | 8 | 0 |
| 121 | 3 | `DashClientModular4\docs\contexto_para_ia` | 0 | 1 |
| 122 | 3 | `DashClientModular4\docs\rebuild` | 0 | 4 |
| 123 | 3 | `DashClientModular4\docs\todos los estudios pdf convertidos a md` | 0 | 63 |
| 124 | 3 | `DashClientModular4\output\pdf` | 0 | 1 |
| 125 | 3 | `DashClientModular4\scripts\eval` | 0 | 0 |
| 126 | 3 | `DashClientModular4\scripts\setup` | 0 | 0 |
| 127 | 3 | `DashClientModular4\scripts\smoke` | 0 | 0 |
| 128 | 3 | `dataset en bruto\beyond_throughput_4g_lte\bus` | 0 | 16 |
| 129 | 3 | `dataset en bruto\beyond_throughput_4g_lte\car` | 0 | 53 |
| 130 | 3 | `dataset en bruto\beyond_throughput_4g_lte\pedestrian` | 0 | 31 |
| 131 | 3 | `dataset en bruto\beyond_throughput_4g_lte\static` | 0 | 15 |
| 132 | 3 | `dataset en bruto\beyond_throughput_4g_lte\train` | 0 | 20 |
| 133 | 3 | `dataset en bruto\FCC Measuring Broadband America\data-raw-2023-feb` | 1 | 0 |
| 134 | 3 | `dataset en bruto\GAViST5G (Gaming and Video Streaming Traffic for 5G)\Global` | 2 | 0 |
| 135 | 3 | `dataset en bruto\GAViST5G (Gaming and Video Streaming Traffic for 5G)\Local` | 2 | 0 |
| 136 | 3 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\Lumos5G-v1.0` | 0 | 3 |
| 137 | 3 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS` | 3 | 0 |
| 138 | 3 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 4G LTE Beyond Throughput 4G LTE` | 2 | 0 |
| 139 | 3 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation` | 1 | 0 |
| 140 | 3 | `dataset en bruto\Norway HSDPA (UMass trace archive)\bus.ljansbakken-oslo` | 0 | 17 |
| 141 | 3 | `dataset en bruto\Norway HSDPA (UMass trace archive)\car.aarnes-elverum` | 0 | 1 |
| 142 | 3 | `dataset en bruto\Norway HSDPA (UMass trace archive)\car.oslo-grimstad` | 0 | 1 |
| 143 | 3 | `dataset en bruto\Norway HSDPA (UMass trace archive)\car.snaroya-smestad` | 0 | 5 |
| 144 | 3 | `dataset en bruto\Norway HSDPA (UMass trace archive)\ferry.nesoddtangen-oslo` | 0 | 16 |
| 145 | 3 | `dataset en bruto\Norway HSDPA (UMass trace archive)\metro.kalbakken-jernbanetorget` | 0 | 17 |
| 146 | 3 | `dataset en bruto\Norway HSDPA (UMass trace archive)\train.oslo-vestby` | 0 | 2 |
| 147 | 3 | `dataset en bruto\Norway HSDPA (UMass trace archive)\train.vestby-oslo` | 0 | 3 |
| 148 | 3 | `dataset en bruto\Norway HSDPA (UMass trace archive)\tram.jernbanetorget-ljabru` | 0 | 8 |
| 149 | 3 | `dataset en bruto\Norway HSDPA (UMass trace archive)\tram.jernbanetorget-universitetssykehuset` | 0 | 1 |
| 150 | 3 | `dataset en bruto\Norway HSDPA (UMass trace archive)\tram.ljabru-jernbanetorget` | 0 | 15 |
| 151 | 3 | `dataset en bruto\oboe\traces` | 0 | 428 |
| 152 | 3 | `datasets_normalizados\phase3\final` | 1 | 0 |
| 153 | 3 | `datasets_normalizados\phase4\phase4B_datos_para_entrenamiento` | 0 | 7 |
| 154 | 3 | `datasets_normalizados\phase4\phase4H_datos_teacher_hibrido_sin_vmaf` | 0 | 8 |
| 155 | 3 | `manifests_trazas\phase3\final` | 2 | 6 |
| 156 | 3 | `manifests_trazas\phase4\phase4A_plan_de_trazas_para_entrenamiento` | 0 | 3 |
| 157 | 3 | `manifests_trazas\phase4\phase4A_training_corpus_sampler` | 0 | 3 |
| 158 | 3 | `modelos\phase4\phase4E_modelo_candidato_neural_abr_lite` | 0 | 5 |
| 159 | 3 | `modelos\phase4\phase4F_bundle_para_inferencia_neural_abr_lite` | 0 | 10 |
| 160 | 3 | `modelos\phase4\phase4H_bundle_para_inferencia_teacher_hibrido_neural_abr_lite` | 0 | 10 |
| 161 | 3 | `modelos\phase4\phase4H_modelo_teacher_hibrido_neural_abr_lite` | 0 | 5 |
| 162 | 3 | `runs_trazas\fase_verificacion_cliente_y_controllers_clasicos\command_logs` | 0 | 5 |
| 163 | 3 | `runs_trazas\fase_verificacion_cliente_y_controllers_clasicos\configs` | 0 | 5 |
| 164 | 3 | `runs_trazas\fase_verificacion_cliente_y_controllers_clasicos\runs` | 1 | 0 |
| 165 | 3 | `runs_trazas\phase3\final` | 0 | 1 |
| 166 | 3 | `runs_trazas\phase3_5\smoke` | 1 | 1 |
| 167 | 3 | `runs_trazas\phase4\phase4D_prueba_rapida_entrenamiento` | 0 | 1 |
| 168 | 3 | `runs_trazas\phase4\phase4F_validacion_bundle_inferencia` | 0 | 3 |
| 169 | 3 | `runs_trazas\phase4\phase4H_validacion_bundle_teacher_hibrido` | 0 | 3 |
| 170 | 3 | `runs_trazas\phase5\configs` | 0 | 2 |
| 171 | 3 | `runs_trazas\phase5\smoke_neural_robust_mpc` | 1 | 0 |
| 172 | 3 | `runs_trazas\phase5\smoke_neural_teacher_hibrido` | 1 | 0 |
| 173 | 3 | `runs_trazas\phase6\tmp_dryrun_fix` | 1 | 0 |
| 174 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00001_base_rate_based_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 175 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00002_base_bba_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 176 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00003_base_bola_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 177 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00004_base_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 178 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00005_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 179 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00006_propio_rmp_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 180 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00007_propio_th_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 181 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00008_base_rate_based_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 182 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00009_base_bba_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 183 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00010_base_bola_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 184 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00011_base_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 185 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00012_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 186 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00013_propio_rmp_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 187 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00014_propio_th_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 188 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00015_base_rate_based_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 189 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00016_base_bba_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 190 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00017_base_bola_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 191 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00018_base_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 192 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00019_base_robust_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 193 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00020_propio_rmp_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 194 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00021_propio_th_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 195 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00022_base_rate_based_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 196 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00023_base_bba_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 197 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00024_base_bola_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 198 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00025_base_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 199 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00026_base_robust_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 200 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00027_propio_rmp_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 201 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00028_propio_th_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 202 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00029_base_rate_based_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 203 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00030_base_bba_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 204 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00031_base_bola_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 205 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00032_base_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 206 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00033_base_robust_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 207 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00034_propio_rmp_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 208 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00035_propio_th_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 209 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00036_base_rate_based_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 210 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00037_base_bba_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 211 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00038_base_bola_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 212 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00039_base_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 213 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00040_base_robust_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 214 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00041_propio_rmp_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 215 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00042_propio_th_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 216 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00043_base_rate_based_paseo_10min_30fps_4s_real_007_8775c96d2f_r1` | 1 | 0 |
| 217 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00044_base_bba_paseo_10min_30fps_4s_real_007_8775c96d2f_r1` | 1 | 0 |
| 218 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00045_base_bola_paseo_10min_30fps_4s_real_007_8775c96d2f_r1` | 1 | 0 |
| 219 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00046_base_mpc_paseo_10min_30fps_4s_real_007_8775c96d2f_r1` | 1 | 0 |
| 220 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00047_base_robust_mpc_paseo_10min_30fps_4s_real_007_8775c96d2f_r1` | 1 | 0 |
| 221 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00048_propio_rmp_paseo_10min_30fps_4s_real_007_8775c96d2f_r1` | 1 | 0 |
| 222 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00049_propio_th_paseo_10min_30fps_4s_real_007_8775c96d2f_r1` | 1 | 0 |
| 223 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00050_base_rate_based_paseo_10min_30fps_4s_real_008_52feb47a90_r1` | 1 | 0 |
| 224 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00051_base_bba_paseo_10min_30fps_4s_real_008_52feb47a90_r1` | 1 | 0 |
| 225 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00052_base_bola_paseo_10min_30fps_4s_real_008_52feb47a90_r1` | 1 | 0 |
| 226 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00053_base_mpc_paseo_10min_30fps_4s_real_008_52feb47a90_r1` | 1 | 0 |
| 227 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00054_base_robust_mpc_paseo_10min_30fps_4s_real_008_52feb47a90_r1` | 1 | 0 |
| 228 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00055_propio_rmp_paseo_10min_30fps_4s_real_008_52feb47a90_r1` | 1 | 0 |
| 229 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00056_propio_th_paseo_10min_30fps_4s_real_008_52feb47a90_r1` | 1 | 0 |
| 230 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00057_base_rate_based_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 231 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00058_base_bba_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 232 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00059_base_bola_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 233 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00060_base_mpc_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 234 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00061_base_robust_mpc_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 235 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00062_propio_rmp_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 236 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00063_propio_th_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 237 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00064_base_rate_based_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1` | 1 | 0 |
| 238 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00065_base_bba_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1` | 1 | 0 |
| 239 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00066_base_bola_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1` | 1 | 0 |
| 240 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00067_base_mpc_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1` | 1 | 0 |
| 241 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00068_base_robust_mpc_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1` | 1 | 0 |
| 242 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00069_propio_rmp_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1` | 1 | 0 |
| 243 | 4 | `20260608_160906_rapido\01_ejecucion\runs\s00070_propio_th_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1` | 1 | 0 |
| 244 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00001_base_rate_based_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 245 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00002_base_bba_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 246 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00003_base_bola_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 247 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00004_base_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 248 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00005_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 249 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00006_propio_rmp_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 250 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00007_propio_th_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 251 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00008_base_rate_based_blender_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 252 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00009_base_bba_blender_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 253 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00010_base_bola_blender_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 254 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00011_base_mpc_blender_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 255 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00012_base_robust_mpc_blender_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 256 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00013_propio_rmp_blender_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 257 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00014_propio_th_blender_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 258 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00015_base_rate_based_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 259 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00016_base_bba_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 260 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00017_base_bola_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 261 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00018_base_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 262 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00019_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 263 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00020_propio_rmp_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 264 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00021_propio_th_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 265 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00022_base_rate_based_blender_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 266 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00023_base_bba_blender_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 267 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00024_base_bola_blender_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 268 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00025_base_mpc_blender_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 269 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00026_base_robust_mpc_blender_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 270 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00027_propio_rmp_blender_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 271 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00028_propio_th_blender_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 272 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00029_base_rate_based_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 273 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00030_base_bba_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 274 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00031_base_bola_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 275 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00032_base_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 276 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00033_base_robust_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 277 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00034_propio_rmp_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 278 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00035_propio_th_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 279 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00036_base_rate_based_blender_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 280 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00037_base_bba_blender_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 281 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00038_base_bola_blender_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 282 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00039_base_mpc_blender_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 283 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00040_base_robust_mpc_blender_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 284 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00041_propio_rmp_blender_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 285 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00042_propio_th_blender_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 286 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00043_base_rate_based_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 287 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00044_base_bba_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 288 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00045_base_bola_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 289 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00046_base_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 290 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00047_base_robust_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 291 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00048_propio_rmp_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 292 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00049_propio_th_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 293 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00050_base_rate_based_blender_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 294 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00051_base_bba_blender_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 295 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00052_base_bola_blender_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 296 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00053_base_mpc_blender_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 297 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00054_base_robust_mpc_blender_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 298 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00055_propio_rmp_blender_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 299 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00056_propio_th_blender_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 300 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00057_base_rate_based_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 301 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00058_base_bba_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 302 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00059_base_bola_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 303 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00060_base_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 304 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00061_base_robust_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 305 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00062_propio_rmp_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 306 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00063_propio_th_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 307 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00064_base_rate_based_blender_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 308 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00065_base_bba_blender_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 309 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00066_base_bola_blender_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 310 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00067_base_mpc_blender_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 311 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00068_base_robust_mpc_blender_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 312 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00069_propio_rmp_blender_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 313 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00070_propio_th_blender_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 314 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00071_base_rate_based_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 315 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00072_base_bba_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 316 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00073_base_bola_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 317 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00074_base_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 318 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00075_base_robust_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 319 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00076_propio_rmp_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 320 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00077_propio_th_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 321 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00078_base_rate_based_blender_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 322 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00079_base_bba_blender_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 323 | 4 | `20260608_193615_equilibrado\01_ejecucion\runs\s00080_base_bola_blender_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 324 | 4 | `20260611_193501_diagnostico\01_ejecucion\runs\s00001_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 325 | 4 | `20260611_193501_diagnostico\01_ejecucion\runs\s00002_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 326 | 4 | `20260611_193501_diagnostico\01_ejecucion\runs\s00003_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 327 | 4 | `20260611_193501_diagnostico\01_ejecucion\runs\s00004_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 328 | 4 | `20260611_193501_diagnostico\01_ejecucion\runs\s00005_base_robust_mpc_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 329 | 4 | `20260611_193501_diagnostico\01_ejecucion\runs\s00006_propio_spbc_v2_anchor_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 330 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00001_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 331 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00002_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 332 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00003_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 333 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00004_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 334 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00005_base_robust_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 335 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00006_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 336 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00007_base_robust_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 337 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00008_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 338 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00009_base_robust_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 339 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00010_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 340 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00011_base_robust_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 341 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00012_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 342 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00013_base_robust_mpc_paseo_10min_30fps_4s_real_007_8775c96d2f_r1` | 1 | 0 |
| 343 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00014_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_007_8775c96d2f_r1` | 1 | 0 |
| 344 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00015_base_robust_mpc_paseo_10min_30fps_4s_real_008_52feb47a90_r1` | 1 | 0 |
| 345 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00016_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_008_52feb47a90_r1` | 1 | 0 |
| 346 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00017_base_robust_mpc_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 347 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00018_propio_spbc_v2_anchor_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 348 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00019_base_robust_mpc_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1` | 1 | 0 |
| 349 | 4 | `20260611_202406_rapido\01_ejecucion\runs\s00020_propio_spbc_v2_anchor_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1` | 1 | 0 |
| 350 | 4 | `20260615_110912_diagnostico\01_ejecucion\runs\s00001_base_rate_based_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 351 | 4 | `20260615_110912_diagnostico\01_ejecucion\runs\s00002_base_bola_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 352 | 4 | `20260615_110912_diagnostico\01_ejecucion\runs\s00003_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 353 | 4 | `20260615_110912_diagnostico\01_ejecucion\runs\s00004_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 354 | 4 | `20260615_110912_diagnostico\01_ejecucion\runs\s00005_base_rate_based_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 355 | 4 | `20260615_110912_diagnostico\01_ejecucion\runs\s00006_base_bola_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 356 | 4 | `20260615_110912_diagnostico\01_ejecucion\runs\s00007_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 357 | 4 | `20260615_110912_diagnostico\01_ejecucion\runs\s00008_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 358 | 4 | `20260615_110912_diagnostico\01_ejecucion\runs\s00009_base_rate_based_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 359 | 4 | `20260615_110912_diagnostico\01_ejecucion\runs\s00010_base_bola_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 360 | 4 | `20260615_110912_diagnostico\01_ejecucion\runs\s00011_base_robust_mpc_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 361 | 4 | `20260615_110912_diagnostico\01_ejecucion\runs\s00012_propio_neural_mpc_v1_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 362 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00001_base_rate_based_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 363 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00002_base_bola_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 364 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00003_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 365 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00004_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 366 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00005_base_rate_based_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 367 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00006_base_bola_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 368 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00007_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 369 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00008_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 370 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00009_base_rate_based_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 371 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00010_base_bola_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 372 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00011_base_robust_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 373 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00012_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_003_9da918eb99_r1` | 1 | 0 |
| 374 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00013_base_rate_based_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 375 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00014_base_bola_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 376 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00015_base_robust_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 377 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00016_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_004_8a94b2b843_r1` | 1 | 0 |
| 378 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00017_base_rate_based_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 379 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00018_base_bola_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 380 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00019_base_robust_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 381 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00020_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_005_00d8be5b10_r1` | 1 | 0 |
| 382 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00021_base_rate_based_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 383 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00022_base_bola_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 384 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00023_base_robust_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 385 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00024_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1` | 1 | 0 |
| 386 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00025_base_rate_based_paseo_10min_30fps_4s_real_007_8775c96d2f_r1` | 1 | 0 |
| 387 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00026_base_bola_paseo_10min_30fps_4s_real_007_8775c96d2f_r1` | 1 | 0 |
| 388 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00027_base_robust_mpc_paseo_10min_30fps_4s_real_007_8775c96d2f_r1` | 1 | 0 |
| 389 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00028_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_007_8775c96d2f_r1` | 1 | 0 |
| 390 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00029_base_rate_based_paseo_10min_30fps_4s_real_008_52feb47a90_r1` | 1 | 0 |
| 391 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00030_base_bola_paseo_10min_30fps_4s_real_008_52feb47a90_r1` | 1 | 0 |
| 392 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00031_base_robust_mpc_paseo_10min_30fps_4s_real_008_52feb47a90_r1` | 1 | 0 |
| 393 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00032_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_008_52feb47a90_r1` | 1 | 0 |
| 394 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00033_base_rate_based_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 395 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00034_base_bola_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 396 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00035_base_robust_mpc_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 397 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00036_propio_neural_mpc_v1_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 398 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00037_base_rate_based_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1` | 1 | 0 |
| 399 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00038_base_bola_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1` | 1 | 0 |
| 400 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00039_base_robust_mpc_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1` | 1 | 0 |
| 401 | 4 | `20260615_112752_rapido\01_ejecucion\runs\s00040_propio_neural_mpc_v1_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1` | 1 | 0 |
| 402 | 4 | `20260615_141628_diagnostico\01_ejecucion\runs\s00001_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 403 | 4 | `20260615_141628_diagnostico\01_ejecucion\runs\s00002_propio_neural_mpc_v2_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1` | 1 | 0 |
| 404 | 4 | `20260615_141628_diagnostico\01_ejecucion\runs\s00003_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 405 | 4 | `20260615_141628_diagnostico\01_ejecucion\runs\s00004_propio_neural_mpc_v2_paseo_10min_30fps_4s_real_002_3c716a0f31_r1` | 1 | 0 |
| 406 | 4 | `20260615_141628_diagnostico\01_ejecucion\runs\s00005_propio_neural_mpc_v1_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 407 | 4 | `20260615_141628_diagnostico\01_ejecucion\runs\s00006_propio_neural_mpc_v2_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1` | 1 | 0 |
| 408 | 4 | `DashClientModular4\core\trace_replay\converters` | 0 | 13 |
| 409 | 4 | `DashClientModular4\docs\contexto rama nueva\02_traces_replay` | 0 | 2 |
| 410 | 4 | `DashClientModular4\docs\contexto rama nueva\03_qoe_reward` | 0 | 11 |
| 411 | 4 | `DashClientModular4\docs\contexto rama nueva\04_neural_abr` | 0 | 8 |
| 412 | 4 | `DashClientModular4\docs\contexto rama nueva\05_neural_controller` | 0 | 6 |
| 413 | 4 | `DashClientModular4\docs\contexto rama nueva\06_validation` | 0 | 2 |
| 414 | 4 | `DashClientModular4\docs\contexto rama nueva\07_memoria_defensa` | 0 | 1 |
| 415 | 4 | `DashClientModular4\docs\contexto rama nueva\fase_4_5_v1` | 2 | 31 |
| 416 | 4 | `DashClientModular4\docs\contexto rama nueva\fase_verificacion_cliente_y_controllers_clasicos` | 0 | 7 |
| 417 | 4 | `DashClientModular4\docs\contexto rama original\01_baselines` | 10 | 21 |
| 418 | 4 | `DashClientModular4\docs\contexto rama original\02_traces_replay` | 4 | 32 |
| 419 | 4 | `DashClientModular4\docs\contexto rama original\03_qoe_reward` | 4 | 22 |
| 420 | 4 | `DashClientModular4\docs\contexto rama original\04_neural_abr` | 4 | 93 |
| 421 | 4 | `DashClientModular4\docs\contexto rama original\05_neural_controller_integration` | 3 | 49 |
| 422 | 4 | `DashClientModular4\docs\contexto rama original\07_memory` | 2 | 10 |
| 423 | 4 | `DashClientModular4\docs\contexto rama original\0_desarrollo_del_cliente` | 0 | 26 |
| 424 | 4 | `DashClientModular4\docs\contexto rama original\0_field_map` | 1 | 10 |
| 425 | 4 | `dataset en bruto\FCC Measuring Broadband America\data-raw-2023-feb\202302` | 0 | 19 |
| 426 | 4 | `dataset en bruto\GAViST5G (Gaming and Video Streaming Traffic for 5G)\Global\Online Gaming` | 3 | 0 |
| 427 | 4 | `dataset en bruto\GAViST5G (Gaming and Video Streaming Traffic for 5G)\Global\Video Streaming` | 0 | 14 |
| 428 | 4 | `dataset en bruto\GAViST5G (Gaming and Video Streaming Traffic for 5G)\Local\Online Gaming` | 3 | 0 |
| 429 | 4 | `dataset en bruto\GAViST5G (Gaming and Video Streaming Traffic for 5G)\Local\Video Streaming` | 4 | 0 |
| 430 | 4 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset` | 2 | 0 |
| 431 | 4 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Multivariate_Dataset` | 1 | 0 |
| 432 | 4 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Sample_Traces` | 0 | 8 |
| 433 | 4 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 4G LTE Beyond Throughput 4G LTE\LTE_Dataset` | 1 | 0 |
| 434 | 4 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 4G LTE Beyond Throughput 4G LTE\ns3_dataset` | 1 | 0 |
| 435 | 4 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset` | 3 | 1 |
| 436 | 4 | `datasets_normalizados\phase3\final\schema_v1` | 12 | 0 |
| 437 | 4 | `manifests_trazas\phase3\final\synthetic_sources` | 1 | 0 |
| 438 | 4 | `manifests_trazas\phase3\final\traces` | 12 | 0 |
| 439 | 4 | `runs_trazas\fase_verificacion_cliente_y_controllers_clasicos\runs\server_smoke` | 5 | 0 |
| 440 | 4 | `runs_trazas\phase3_5\smoke\scenarios` | 4 | 0 |
| 441 | 4 | `runs_trazas\phase5\smoke_neural_robust_mpc\run_20260605_143034` | 0 | 6 |
| 442 | 4 | `runs_trazas\phase5\smoke_neural_teacher_hibrido\run_20260605_143136` | 0 | 6 |
| 443 | 4 | `runs_trazas\phase6\tmp_dryrun_fix\20260608_143413_rapido` | 0 | 0 |
| 444 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00001_base_rate_based_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_160907` | 0 | 6 |
| 445 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00002_base_bba_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161110` | 0 | 6 |
| 446 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00003_base_bola_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161314` | 0 | 6 |
| 447 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00004_base_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161517` | 0 | 6 |
| 448 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00005_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161721` | 0 | 6 |
| 449 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00006_propio_rmp_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_161924` | 0 | 6 |
| 450 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00007_propio_th_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_162144` | 0 | 6 |
| 451 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00008_base_rate_based_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162350` | 0 | 6 |
| 452 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00009_base_bba_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162552` | 0 | 6 |
| 453 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00010_base_bola_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162754` | 0 | 6 |
| 454 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00011_base_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_162956` | 0 | 6 |
| 455 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00012_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163159` | 0 | 6 |
| 456 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00013_propio_rmp_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163401` | 0 | 6 |
| 457 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00014_propio_th_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_163603` | 0 | 6 |
| 458 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00015_base_rate_based_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_163806` | 0 | 6 |
| 459 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00016_base_bba_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164008` | 0 | 6 |
| 460 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00017_base_bola_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164210` | 0 | 6 |
| 461 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00018_base_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164413` | 0 | 6 |
| 462 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00019_base_robust_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164615` | 0 | 6 |
| 463 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00020_propio_rmp_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_164817` | 0 | 6 |
| 464 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00021_propio_th_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_165020` | 0 | 6 |
| 465 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00022_base_rate_based_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165222` | 0 | 6 |
| 466 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00023_base_bba_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165425` | 0 | 6 |
| 467 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00024_base_bola_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165629` | 0 | 6 |
| 468 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00025_base_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_165832` | 0 | 6 |
| 469 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00026_base_robust_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170035` | 0 | 6 |
| 470 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00027_propio_rmp_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170238` | 0 | 6 |
| 471 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00028_propio_th_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_170451` | 0 | 6 |
| 472 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00029_base_rate_based_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_170654` | 0 | 6 |
| 473 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00030_base_bba_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_170857` | 0 | 6 |
| 474 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00031_base_bola_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171100` | 0 | 6 |
| 475 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00032_base_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171302` | 0 | 6 |
| 476 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00033_base_robust_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171515` | 0 | 6 |
| 477 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00034_propio_rmp_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171725` | 0 | 6 |
| 478 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00035_propio_th_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_171934` | 0 | 6 |
| 479 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00036_base_rate_based_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172148` | 0 | 6 |
| 480 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00037_base_bba_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172350` | 0 | 6 |
| 481 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00038_base_bola_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172601` | 0 | 6 |
| 482 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00039_base_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_172824` | 0 | 6 |
| 483 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00040_base_robust_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173055` | 0 | 6 |
| 484 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00041_propio_rmp_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173302` | 0 | 6 |
| 485 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00042_propio_th_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_173533` | 0 | 6 |
| 486 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00043_base_rate_based_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_173808` | 0 | 6 |
| 487 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00044_base_bba_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_174010` | 0 | 6 |
| 488 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00045_base_bola_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_174212` | 0 | 6 |
| 489 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00046_base_mpc_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_174415` | 0 | 6 |
| 490 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00047_base_robust_mpc_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_174617` | 0 | 6 |
| 491 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00048_propio_rmp_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_174819` | 0 | 6 |
| 492 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00049_propio_th_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260608_175021` | 0 | 6 |
| 493 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00050_base_rate_based_paseo_10min_30fps_4s_real_008_52feb47a90_r1\run_20260608_175223` | 0 | 6 |
| 494 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00051_base_bba_paseo_10min_30fps_4s_real_008_52feb47a90_r1\run_20260608_175425` | 0 | 6 |
| 495 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00052_base_bola_paseo_10min_30fps_4s_real_008_52feb47a90_r1\run_20260608_175628` | 0 | 6 |
| 496 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00053_base_mpc_paseo_10min_30fps_4s_real_008_52feb47a90_r1\run_20260608_175830` | 0 | 6 |
| 497 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00054_base_robust_mpc_paseo_10min_30fps_4s_real_008_52feb47a90_r1\run_20260608_180032` | 0 | 6 |
| 498 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00055_propio_rmp_paseo_10min_30fps_4s_real_008_52feb47a90_r1\run_20260608_180234` | 0 | 6 |
| 499 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00056_propio_th_paseo_10min_30fps_4s_real_008_52feb47a90_r1\run_20260608_180436` | 0 | 6 |
| 500 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00057_base_rate_based_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260608_180639` | 0 | 6 |
| 501 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00058_base_bba_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260608_180843` | 0 | 6 |
| 502 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00059_base_bola_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260608_181048` | 0 | 6 |
| 503 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00060_base_mpc_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260608_181333` | 0 | 6 |
| 504 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00061_base_robust_mpc_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260608_181538` | 0 | 6 |
| 505 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00062_propio_rmp_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260608_181742` | 0 | 6 |
| 506 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00063_propio_th_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260608_182025` | 0 | 6 |
| 507 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00064_base_rate_based_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1\run_20260608_182234` | 0 | 6 |
| 508 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00065_base_bba_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1\run_20260608_182436` | 0 | 6 |
| 509 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00066_base_bola_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1\run_20260608_182638` | 0 | 6 |
| 510 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00067_base_mpc_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1\run_20260608_182841` | 0 | 6 |
| 511 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00068_base_robust_mpc_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1\run_20260608_183043` | 0 | 6 |
| 512 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00069_propio_rmp_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1\run_20260608_183246` | 0 | 6 |
| 513 | 5 | `20260608_160906_rapido\01_ejecucion\runs\s00070_propio_th_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1\run_20260608_183448` | 0 | 6 |
| 514 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00001_base_rate_based_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_193616` | 0 | 6 |
| 515 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00002_base_bba_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_193819` | 0 | 6 |
| 516 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00003_base_bola_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_194023` | 0 | 6 |
| 517 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00004_base_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_194226` | 0 | 6 |
| 518 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00005_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_194430` | 0 | 6 |
| 519 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00006_propio_rmp_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_194633` | 0 | 6 |
| 520 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00007_propio_th_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_194853` | 0 | 6 |
| 521 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00008_base_rate_based_blender_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_195058` | 0 | 6 |
| 522 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00009_base_bba_blender_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_195301` | 0 | 6 |
| 523 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00010_base_bola_blender_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_195503` | 0 | 6 |
| 524 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00011_base_mpc_blender_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_195706` | 0 | 6 |
| 525 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00012_base_robust_mpc_blender_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_195909` | 0 | 6 |
| 526 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00013_propio_rmp_blender_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_200112` | 0 | 6 |
| 527 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00014_propio_th_blender_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260608_200330` | 0 | 6 |
| 528 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00015_base_rate_based_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_200534` | 0 | 6 |
| 529 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00016_base_bba_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_200736` | 0 | 6 |
| 530 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00017_base_bola_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_200938` | 0 | 6 |
| 531 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00018_base_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_201140` | 0 | 6 |
| 532 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00019_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_201343` | 0 | 6 |
| 533 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00020_propio_rmp_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_201545` | 0 | 6 |
| 534 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00021_propio_th_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_201747` | 0 | 6 |
| 535 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00022_base_rate_based_blender_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_201949` | 0 | 6 |
| 536 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00023_base_bba_blender_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_202152` | 0 | 6 |
| 537 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00024_base_bola_blender_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_202354` | 0 | 6 |
| 538 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00025_base_mpc_blender_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_202556` | 0 | 6 |
| 539 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00026_base_robust_mpc_blender_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_202758` | 0 | 6 |
| 540 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00027_propio_rmp_blender_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_203001` | 0 | 6 |
| 541 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00028_propio_th_blender_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260608_203203` | 0 | 6 |
| 542 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00029_base_rate_based_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_203405` | 0 | 6 |
| 543 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00030_base_bba_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_203608` | 0 | 6 |
| 544 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00031_base_bola_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_203810` | 0 | 6 |
| 545 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00032_base_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_204012` | 0 | 6 |
| 546 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00033_base_robust_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_204214` | 0 | 6 |
| 547 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00034_propio_rmp_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_204417` | 0 | 6 |
| 548 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00035_propio_th_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_204619` | 0 | 6 |
| 549 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00036_base_rate_based_blender_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_204822` | 0 | 6 |
| 550 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00037_base_bba_blender_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_205024` | 0 | 6 |
| 551 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00038_base_bola_blender_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_205226` | 0 | 6 |
| 552 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00039_base_mpc_blender_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_205429` | 0 | 6 |
| 553 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00040_base_robust_mpc_blender_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_205631` | 0 | 6 |
| 554 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00041_propio_rmp_blender_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_205833` | 0 | 6 |
| 555 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00042_propio_th_blender_10min_30fps_4s_real_003_9da918eb99_r1\run_20260608_210035` | 0 | 6 |
| 556 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00043_base_rate_based_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_210238` | 0 | 6 |
| 557 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00044_base_bba_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_210441` | 0 | 6 |
| 558 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00045_base_bola_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_210644` | 0 | 6 |
| 559 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00046_base_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_210847` | 0 | 6 |
| 560 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00047_base_robust_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_211051` | 0 | 6 |
| 561 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00048_propio_rmp_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_211254` | 0 | 6 |
| 562 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00049_propio_th_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_211507` | 0 | 6 |
| 563 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00050_base_rate_based_blender_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_211710` | 0 | 6 |
| 564 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00051_base_bba_blender_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_211913` | 0 | 6 |
| 565 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00052_base_bola_blender_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_212116` | 0 | 6 |
| 566 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00053_base_mpc_blender_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_212318` | 0 | 6 |
| 567 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00054_base_robust_mpc_blender_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_212521` | 0 | 6 |
| 568 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00055_propio_rmp_blender_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_212724` | 0 | 6 |
| 569 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00056_propio_th_blender_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260608_212936` | 0 | 6 |
| 570 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00057_base_rate_based_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_213139` | 0 | 6 |
| 571 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00058_base_bba_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_213341` | 0 | 6 |
| 572 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00059_base_bola_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_213544` | 0 | 6 |
| 573 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00060_base_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_213746` | 0 | 6 |
| 574 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00061_base_robust_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_214001` | 0 | 6 |
| 575 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00062_propio_rmp_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_214211` | 0 | 6 |
| 576 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00063_propio_th_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_214420` | 0 | 6 |
| 577 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00064_base_rate_based_blender_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_214633` | 0 | 6 |
| 578 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00065_base_bba_blender_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_214836` | 0 | 6 |
| 579 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00066_base_bola_blender_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_215038` | 0 | 6 |
| 580 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00067_base_mpc_blender_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_215241` | 0 | 6 |
| 581 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00068_base_robust_mpc_blender_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_215454` | 0 | 6 |
| 582 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00069_propio_rmp_blender_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_215703` | 0 | 6 |
| 583 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00070_propio_th_blender_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260608_215911` | 0 | 6 |
| 584 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00071_base_rate_based_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_220126` | 0 | 6 |
| 585 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00072_base_bba_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_220329` | 0 | 6 |
| 586 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00073_base_bola_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_220539` | 0 | 6 |
| 587 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00074_base_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_220803` | 0 | 6 |
| 588 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00075_base_robust_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_221034` | 0 | 6 |
| 589 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00076_propio_rmp_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_221241` | 0 | 6 |
| 590 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00077_propio_th_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_221513` | 0 | 6 |
| 591 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00078_base_rate_based_blender_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_221747` | 0 | 6 |
| 592 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00079_base_bba_blender_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_221950` | 0 | 6 |
| 593 | 5 | `20260608_193615_equilibrado\01_ejecucion\runs\s00080_base_bola_blender_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260608_222153` | 0 | 6 |
| 594 | 5 | `20260611_193501_diagnostico\01_ejecucion\runs\s00001_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260611_193502` | 0 | 6 |
| 595 | 5 | `20260611_193501_diagnostico\01_ejecucion\runs\s00002_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260611_193530` | 0 | 6 |
| 596 | 5 | `20260611_193501_diagnostico\01_ejecucion\runs\s00003_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260611_193557` | 0 | 6 |
| 597 | 5 | `20260611_193501_diagnostico\01_ejecucion\runs\s00004_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260611_193623` | 0 | 6 |
| 598 | 5 | `20260611_193501_diagnostico\01_ejecucion\runs\s00005_base_robust_mpc_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260611_193649` | 0 | 6 |
| 599 | 5 | `20260611_193501_diagnostico\01_ejecucion\runs\s00006_propio_spbc_v2_anchor_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260611_193718` | 0 | 6 |
| 600 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00001_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260611_202407` | 0 | 6 |
| 601 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00002_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260611_202610` | 0 | 6 |
| 602 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00003_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260611_202814` | 0 | 6 |
| 603 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00004_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260611_203016` | 0 | 6 |
| 604 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00005_base_robust_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260611_203218` | 0 | 6 |
| 605 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00006_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260611_203420` | 0 | 6 |
| 606 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00007_base_robust_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260611_203623` | 0 | 6 |
| 607 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00008_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260611_203826` | 0 | 6 |
| 608 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00009_base_robust_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260611_204029` | 0 | 6 |
| 609 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00010_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260611_204238` | 0 | 6 |
| 610 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00011_base_robust_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260611_204441` | 0 | 6 |
| 611 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00012_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260611_204648` | 0 | 6 |
| 612 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00013_base_robust_mpc_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260611_204854` | 0 | 6 |
| 613 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00014_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260611_205056` | 0 | 6 |
| 614 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00015_base_robust_mpc_paseo_10min_30fps_4s_real_008_52feb47a90_r1\run_20260611_205258` | 0 | 6 |
| 615 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00016_propio_spbc_v2_anchor_paseo_10min_30fps_4s_real_008_52feb47a90_r1\run_20260611_205500` | 0 | 6 |
| 616 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00017_base_robust_mpc_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260611_205702` | 0 | 6 |
| 617 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00018_propio_spbc_v2_anchor_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260611_205907` | 0 | 6 |
| 618 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00019_base_robust_mpc_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1\run_20260611_210112` | 0 | 6 |
| 619 | 5 | `20260611_202406_rapido\01_ejecucion\runs\s00020_propio_spbc_v2_anchor_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1\run_20260611_210314` | 0 | 6 |
| 620 | 5 | `20260615_110912_diagnostico\01_ejecucion\runs\s00001_base_rate_based_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260615_110913` | 0 | 6 |
| 621 | 5 | `20260615_110912_diagnostico\01_ejecucion\runs\s00002_base_bola_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260615_110940` | 0 | 6 |
| 622 | 5 | `20260615_110912_diagnostico\01_ejecucion\runs\s00003_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260615_111007` | 0 | 6 |
| 623 | 5 | `20260615_110912_diagnostico\01_ejecucion\runs\s00004_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260615_111035` | 0 | 6 |
| 624 | 5 | `20260615_110912_diagnostico\01_ejecucion\runs\s00005_base_rate_based_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260615_111102` | 0 | 6 |
| 625 | 5 | `20260615_110912_diagnostico\01_ejecucion\runs\s00006_base_bola_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260615_111128` | 0 | 6 |
| 626 | 5 | `20260615_110912_diagnostico\01_ejecucion\runs\s00007_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260615_111154` | 0 | 6 |
| 627 | 5 | `20260615_110912_diagnostico\01_ejecucion\runs\s00008_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260615_111220` | 0 | 6 |
| 628 | 5 | `20260615_110912_diagnostico\01_ejecucion\runs\s00009_base_rate_based_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260615_111246` | 0 | 6 |
| 629 | 5 | `20260615_110912_diagnostico\01_ejecucion\runs\s00010_base_bola_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260615_111315` | 0 | 6 |
| 630 | 5 | `20260615_110912_diagnostico\01_ejecucion\runs\s00011_base_robust_mpc_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260615_111351` | 0 | 6 |
| 631 | 5 | `20260615_110912_diagnostico\01_ejecucion\runs\s00012_propio_neural_mpc_v1_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260615_111420` | 0 | 6 |
| 632 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00001_base_rate_based_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260615_112753` | 0 | 6 |
| 633 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00002_base_bola_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260615_112956` | 0 | 6 |
| 634 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00003_base_robust_mpc_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260615_113159` | 0 | 6 |
| 635 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00004_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260615_113403` | 0 | 6 |
| 636 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00005_base_rate_based_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260615_113606` | 0 | 6 |
| 637 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00006_base_bola_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260615_113810` | 0 | 6 |
| 638 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00007_base_robust_mpc_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260615_114013` | 0 | 6 |
| 639 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00008_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260615_114215` | 0 | 6 |
| 640 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00009_base_rate_based_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260615_114417` | 0 | 6 |
| 641 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00010_base_bola_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260615_114620` | 0 | 6 |
| 642 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00011_base_robust_mpc_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260615_114822` | 0 | 6 |
| 643 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00012_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_003_9da918eb99_r1\run_20260615_115024` | 0 | 6 |
| 644 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00013_base_rate_based_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260615_115227` | 0 | 6 |
| 645 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00014_base_bola_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260615_115430` | 0 | 6 |
| 646 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00015_base_robust_mpc_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260615_115633` | 0 | 6 |
| 647 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00016_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_004_8a94b2b843_r1\run_20260615_115836` | 0 | 6 |
| 648 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00017_base_rate_based_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260615_120039` | 0 | 6 |
| 649 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00018_base_bola_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260615_120242` | 0 | 6 |
| 650 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00019_base_robust_mpc_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260615_120444` | 0 | 6 |
| 651 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00020_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_005_00d8be5b10_r1\run_20260615_120654` | 0 | 6 |
| 652 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00021_base_rate_based_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260615_120900` | 0 | 6 |
| 653 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00022_base_bola_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260615_121103` | 0 | 6 |
| 654 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00023_base_robust_mpc_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260615_121327` | 0 | 6 |
| 655 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00024_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_006_d2d8a29c20_r1\run_20260615_121535` | 0 | 6 |
| 656 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00025_base_rate_based_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260615_121754` | 0 | 6 |
| 657 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00026_base_bola_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260615_121956` | 0 | 6 |
| 658 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00027_base_robust_mpc_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260615_122158` | 0 | 6 |
| 659 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00028_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_007_8775c96d2f_r1\run_20260615_122400` | 0 | 6 |
| 660 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00029_base_rate_based_paseo_10min_30fps_4s_real_008_52feb47a90_r1\run_20260615_122602` | 0 | 6 |
| 661 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00030_base_bola_paseo_10min_30fps_4s_real_008_52feb47a90_r1\run_20260615_122804` | 0 | 6 |
| 662 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00031_base_robust_mpc_paseo_10min_30fps_4s_real_008_52feb47a90_r1\run_20260615_123007` | 0 | 6 |
| 663 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00032_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_008_52feb47a90_r1\run_20260615_123209` | 0 | 6 |
| 664 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00033_base_rate_based_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260615_123411` | 0 | 6 |
| 665 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00034_base_bola_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260615_123616` | 0 | 6 |
| 666 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00035_base_robust_mpc_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260615_123913` | 0 | 6 |
| 667 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00036_propio_neural_mpc_v1_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260615_124118` | 0 | 6 |
| 668 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00037_base_rate_based_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1\run_20260615_124322` | 0 | 6 |
| 669 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00038_base_bola_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1\run_20260615_124525` | 0 | 6 |
| 670 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00039_base_robust_mpc_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1\run_20260615_124727` | 0 | 6 |
| 671 | 5 | `20260615_112752_rapido\01_ejecucion\runs\s00040_propio_neural_mpc_v1_paseo_10min_30fps_4s_synthetic_002_d934ff24c4_r1\run_20260615_124929` | 0 | 6 |
| 672 | 5 | `20260615_141628_diagnostico\01_ejecucion\runs\s00001_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260615_141629` | 0 | 6 |
| 673 | 5 | `20260615_141628_diagnostico\01_ejecucion\runs\s00002_propio_neural_mpc_v2_paseo_10min_30fps_4s_real_001_81e4eea3a8_r1\run_20260615_141656` | 0 | 6 |
| 674 | 5 | `20260615_141628_diagnostico\01_ejecucion\runs\s00003_propio_neural_mpc_v1_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260615_141724` | 0 | 6 |
| 675 | 5 | `20260615_141628_diagnostico\01_ejecucion\runs\s00004_propio_neural_mpc_v2_paseo_10min_30fps_4s_real_002_3c716a0f31_r1\run_20260615_141750` | 0 | 6 |
| 676 | 5 | `20260615_141628_diagnostico\01_ejecucion\runs\s00005_propio_neural_mpc_v1_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260615_141816` | 0 | 6 |
| 677 | 5 | `20260615_141628_diagnostico\01_ejecucion\runs\s00006_propio_neural_mpc_v2_paseo_10min_30fps_4s_synthetic_001_4089a97df3_r1\run_20260615_141844` | 0 | 6 |
| 678 | 5 | `DashClientModular4\docs\contexto rama nueva\fase_4_5_v1\abr ia md` | 0 | 32 |
| 679 | 5 | `DashClientModular4\docs\contexto rama nueva\fase_4_5_v1\bloqueos` | 0 | 1 |
| 680 | 5 | `DashClientModular4\docs\contexto rama original\01_baselines\_handoffs` | 0 | 2 |
| 681 | 5 | `DashClientModular4\docs\contexto rama original\01_baselines\_historical` | 0 | 8 |
| 682 | 5 | `DashClientModular4\docs\contexto rama original\01_baselines\_templates` | 0 | 6 |
| 683 | 5 | `DashClientModular4\docs\contexto rama original\01_baselines\bba` | 0 | 6 |
| 684 | 5 | `DashClientModular4\docs\contexto rama original\01_baselines\bola` | 0 | 8 |
| 685 | 5 | `DashClientModular4\docs\contexto rama original\01_baselines\mpc` | 0 | 6 |
| 686 | 5 | `DashClientModular4\docs\contexto rama original\01_baselines\optional_methods` | 7 | 1 |
| 687 | 5 | `DashClientModular4\docs\contexto rama original\01_baselines\rate_based` | 0 | 6 |
| 688 | 5 | `DashClientModular4\docs\contexto rama original\01_baselines\robust_mpc` | 0 | 7 |
| 689 | 5 | `DashClientModular4\docs\contexto rama original\01_baselines\sanity_controllers` | 0 | 5 |
| 690 | 5 | `DashClientModular4\docs\contexto rama original\02_traces_replay\_historical` | 0 | 20 |
| 691 | 5 | `DashClientModular4\docs\contexto rama original\02_traces_replay\_templates` | 0 | 3 |
| 692 | 5 | `DashClientModular4\docs\contexto rama original\02_traces_replay\method_cards` | 0 | 9 |
| 693 | 5 | `DashClientModular4\docs\contexto rama original\02_traces_replay\trace_dataset_cards` | 0 | 9 |
| 694 | 5 | `DashClientModular4\docs\contexto rama original\03_qoe_reward\_handoffs` | 0 | 4 |
| 695 | 5 | `DashClientModular4\docs\contexto rama original\03_qoe_reward\_historical` | 0 | 12 |
| 696 | 5 | `DashClientModular4\docs\contexto rama original\03_qoe_reward\_templates` | 0 | 2 |
| 697 | 5 | `DashClientModular4\docs\contexto rama original\03_qoe_reward\source_cards` | 0 | 12 |
| 698 | 5 | `DashClientModular4\docs\contexto rama original\04_neural_abr\_handoffs` | 0 | 22 |
| 699 | 5 | `DashClientModular4\docs\contexto rama original\04_neural_abr\_historical` | 0 | 72 |
| 700 | 5 | `DashClientModular4\docs\contexto rama original\04_neural_abr\_templates` | 0 | 7 |
| 701 | 5 | `DashClientModular4\docs\contexto rama original\04_neural_abr\source_cards` | 0 | 25 |
| 702 | 5 | `DashClientModular4\docs\contexto rama original\05_neural_controller_integration\_handoffs` | 0 | 3 |
| 703 | 5 | `DashClientModular4\docs\contexto rama original\05_neural_controller_integration\_historical` | 0 | 18 |
| 704 | 5 | `DashClientModular4\docs\contexto rama original\05_neural_controller_integration\source_cards` | 0 | 23 |
| 705 | 5 | `DashClientModular4\docs\contexto rama original\07_memory\_historical` | 0 | 16 |
| 706 | 5 | `DashClientModular4\docs\contexto rama original\07_memory\_templates` | 0 | 2 |
| 707 | 5 | `DashClientModular4\docs\contexto rama original\0_field_map\paper_cards` | 0 | 6 |
| 708 | 5 | `dataset en bruto\GAViST5G (Gaming and Video Streaming Traffic for 5G)\Global\Online Gaming\LOL` | 0 | 11 |
| 709 | 5 | `dataset en bruto\GAViST5G (Gaming and Video Streaming Traffic for 5G)\Global\Online Gaming\TFT` | 0 | 6 |
| 710 | 5 | `dataset en bruto\GAViST5G (Gaming and Video Streaming Traffic for 5G)\Global\Online Gaming\VAL` | 0 | 8 |
| 711 | 5 | `dataset en bruto\GAViST5G (Gaming and Video Streaming Traffic for 5G)\Local\Online Gaming\LOL` | 0 | 9 |
| 712 | 5 | `dataset en bruto\GAViST5G (Gaming and Video Streaming Traffic for 5G)\Local\Online Gaming\TFT` | 0 | 8 |
| 713 | 5 | `dataset en bruto\GAViST5G (Gaming and Video Streaming Traffic for 5G)\Local\Online Gaming\VAL` | 0 | 4 |
| 714 | 5 | `dataset en bruto\GAViST5G (Gaming and Video Streaming Traffic for 5G)\Local\Video Streaming\Crave` | 0 | 10 |
| 715 | 5 | `dataset en bruto\GAViST5G (Gaming and Video Streaming Traffic for 5G)\Local\Video Streaming\Netflix` | 0 | 12 |
| 716 | 5 | `dataset en bruto\GAViST5G (Gaming and Video Streaming Traffic for 5G)\Local\Video Streaming\PrimeVideo` | 0 | 11 |
| 717 | 5 | `dataset en bruto\GAViST5G (Gaming and Video Streaming Traffic for 5G)\Local\Video Streaming\YouTube` | 0 | 29 |
| 718 | 5 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_1` | 1 | 0 |
| 719 | 5 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_2` | 6 | 0 |
| 720 | 5 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Multivariate_Dataset\dataset` | 5 | 0 |
| 721 | 5 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 4G LTE Beyond Throughput 4G LTE\LTE_Dataset\Dataset` | 5 | 0 |
| 722 | 5 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 4G LTE Beyond Throughput 4G LTE\ns3_dataset\sampling_interval` | 2 | 0 |
| 723 | 5 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset\Amazon_Prime` | 2 | 0 |
| 724 | 5 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset\Download` | 2 | 1 |
| 725 | 5 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset\Netflix` | 2 | 0 |
| 726 | 5 | `datasets_normalizados\phase3\final\schema_v1\fcc_measuring_broadband_america` | 0 | 4302 |
| 727 | 5 | `datasets_normalizados\phase3\final\schema_v1\gavist5g` | 0 | 122 |
| 728 | 5 | `datasets_normalizados\phase3\final\schema_v1\ghent_4g_lte` | 0 | 40 |
| 729 | 5 | `datasets_normalizados\phase3\final\schema_v1\lumos5g` | 0 | 118 |
| 730 | 5 | `datasets_normalizados\phase3\final\schema_v1\norway_hsdpa_umass` | 0 | 86 |
| 731 | 5 | `datasets_normalizados\phase3\final\schema_v1\nyu_mets` | 0 | 38 |
| 732 | 5 | `datasets_normalizados\phase3\final\schema_v1\oboe` | 0 | 428 |
| 733 | 5 | `datasets_normalizados\phase3\final\schema_v1\puffer_stanford` | 0 | 94 |
| 734 | 5 | `datasets_normalizados\phase3\final\schema_v1\roma_4g_nbiot_5g_nsa` | 0 | 522 |
| 735 | 5 | `datasets_normalizados\phase3\final\schema_v1\synthetic_controlled_network` | 8 | 0 |
| 736 | 5 | `datasets_normalizados\phase3\final\schema_v1\ucc_4g_lte_beyond_throughput` | 0 | 135 |
| 737 | 5 | `datasets_normalizados\phase3\final\schema_v1\ucc_5g_beyond_throughput` | 0 | 83 |
| 738 | 5 | `manifests_trazas\phase3\final\synthetic_sources\synthetic_controlled_network` | 8 | 0 |
| 739 | 5 | `manifests_trazas\phase3\final\traces\fcc_measuring_broadband_america` | 0 | 4302 |
| 740 | 5 | `manifests_trazas\phase3\final\traces\gavist5g` | 0 | 122 |
| 741 | 5 | `manifests_trazas\phase3\final\traces\ghent_4g_lte` | 0 | 40 |
| 742 | 5 | `manifests_trazas\phase3\final\traces\lumos5g` | 0 | 118 |
| 743 | 5 | `manifests_trazas\phase3\final\traces\norway_hsdpa_umass` | 0 | 86 |
| 744 | 5 | `manifests_trazas\phase3\final\traces\nyu_mets` | 0 | 38 |
| 745 | 5 | `manifests_trazas\phase3\final\traces\oboe` | 0 | 428 |
| 746 | 5 | `manifests_trazas\phase3\final\traces\puffer_stanford` | 0 | 94 |
| 747 | 5 | `manifests_trazas\phase3\final\traces\roma_4g_nbiot_5g_nsa` | 0 | 522 |
| 748 | 5 | `manifests_trazas\phase3\final\traces\synthetic_controlled_network` | 8 | 0 |
| 749 | 5 | `manifests_trazas\phase3\final\traces\ucc_4g_lte_beyond_throughput` | 0 | 135 |
| 750 | 5 | `manifests_trazas\phase3\final\traces\ucc_5g_beyond_throughput` | 0 | 83 |
| 751 | 5 | `runs_trazas\fase_verificacion_cliente_y_controllers_clasicos\runs\server_smoke\bba` | 1 | 0 |
| 752 | 5 | `runs_trazas\fase_verificacion_cliente_y_controllers_clasicos\runs\server_smoke\bola` | 1 | 0 |
| 753 | 5 | `runs_trazas\fase_verificacion_cliente_y_controllers_clasicos\runs\server_smoke\mpc` | 1 | 0 |
| 754 | 5 | `runs_trazas\fase_verificacion_cliente_y_controllers_clasicos\runs\server_smoke\rate_based` | 1 | 0 |
| 755 | 5 | `runs_trazas\fase_verificacion_cliente_y_controllers_clasicos\runs\server_smoke\robust_mpc` | 1 | 0 |
| 756 | 5 | `runs_trazas\phase3_5\smoke\scenarios\complete_use_for_eval` | 2 | 0 |
| 757 | 5 | `runs_trazas\phase3_5\smoke\scenarios\incomplete_session` | 2 | 0 |
| 758 | 5 | `runs_trazas\phase3_5\smoke\scenarios\legacy_do_not_use_for_eval` | 2 | 0 |
| 759 | 5 | `runs_trazas\phase3_5\smoke\scenarios\source_claims_benchmark` | 2 | 0 |
| 760 | 6 | `DashClientModular4\docs\contexto rama original\01_baselines\optional_methods\festive` | 0 | 1 |
| 761 | 6 | `DashClientModular4\docs\contexto rama original\01_baselines\optional_methods\lumos` | 0 | 1 |
| 762 | 6 | `DashClientModular4\docs\contexto rama original\01_baselines\optional_methods\oboe` | 0 | 1 |
| 763 | 6 | `DashClientModular4\docs\contexto rama original\01_baselines\optional_methods\panda` | 0 | 1 |
| 764 | 6 | `DashClientModular4\docs\contexto rama original\01_baselines\optional_methods\rbc` | 0 | 1 |
| 765 | 6 | `DashClientModular4\docs\contexto rama original\01_baselines\optional_methods\soda` | 0 | 2 |
| 766 | 6 | `DashClientModular4\docs\contexto rama original\01_baselines\optional_methods\wish` | 0 | 1 |
| 767 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_1\Dataset` | 10 | 0 |
| 768 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_2\7Train` | 0 | 2 |
| 769 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_2\Bus_NYU_Campus` | 0 | 1 |
| 770 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_2\BusBrooklyn` | 0 | 2 |
| 771 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_2\Car` | 0 | 2 |
| 772 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_2\LIRR` | 0 | 2 |
| 773 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_2\QTrain` | 0 | 1 |
| 774 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Multivariate_Dataset\dataset\BB16` | 0 | 1 |
| 775 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Multivariate_Dataset\dataset\BB61` | 0 | 1 |
| 776 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Multivariate_Dataset\dataset\BB62` | 0 | 1 |
| 777 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Multivariate_Dataset\dataset\MM15` | 0 | 1 |
| 778 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Multivariate_Dataset\dataset\TT7` | 0 | 1 |
| 779 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 4G LTE Beyond Throughput 4G LTE\LTE_Dataset\Dataset\bus` | 0 | 16 |
| 780 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 4G LTE Beyond Throughput 4G LTE\LTE_Dataset\Dataset\car` | 0 | 53 |
| 781 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 4G LTE Beyond Throughput 4G LTE\LTE_Dataset\Dataset\pedestrian` | 0 | 31 |
| 782 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 4G LTE Beyond Throughput 4G LTE\LTE_Dataset\Dataset\static` | 0 | 15 |
| 783 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 4G LTE Beyond Throughput 4G LTE\LTE_Dataset\Dataset\train` | 0 | 20 |
| 784 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 4G LTE Beyond Throughput 4G LTE\ns3_dataset\sampling_interval\1s` | 0 | 100 |
| 785 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 4G LTE Beyond Throughput 4G LTE\ns3_dataset\sampling_interval\250ms` | 0 | 100 |
| 786 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset\Amazon_Prime\Driving` | 2 | 0 |
| 787 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset\Amazon_Prime\Static` | 2 | 0 |
| 788 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset\Download\Driving` | 0 | 16 |
| 789 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset\Download\Static` | 0 | 5 |
| 790 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset\Netflix\Driving` | 2 | 0 |
| 791 | 6 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset\Netflix\Static` | 2 | 0 |
| 792 | 6 | `datasets_normalizados\phase3\final\schema_v1\synthetic_controlled_network\synthetic_high_jitter` | 0 | 128 |
| 793 | 6 | `datasets_normalizados\phase3\final\schema_v1\synthetic_controlled_network\synthetic_mobile_variable` | 0 | 128 |
| 794 | 6 | `datasets_normalizados\phase3\final\schema_v1\synthetic_controlled_network\synthetic_perfect_high` | 0 | 128 |
| 795 | 6 | `datasets_normalizados\phase3\final\schema_v1\synthetic_controlled_network\synthetic_periodic_oscillation` | 0 | 128 |
| 796 | 6 | `datasets_normalizados\phase3\final\schema_v1\synthetic_controlled_network\synthetic_stable_low` | 0 | 128 |
| 797 | 6 | `datasets_normalizados\phase3\final\schema_v1\synthetic_controlled_network\synthetic_stall_trap` | 0 | 128 |
| 798 | 6 | `datasets_normalizados\phase3\final\schema_v1\synthetic_controlled_network\synthetic_sudden_drop` | 0 | 128 |
| 799 | 6 | `datasets_normalizados\phase3\final\schema_v1\synthetic_controlled_network\synthetic_sudden_recovery` | 0 | 128 |
| 800 | 6 | `manifests_trazas\phase3\final\synthetic_sources\synthetic_controlled_network\synthetic_high_jitter` | 0 | 128 |
| 801 | 6 | `manifests_trazas\phase3\final\synthetic_sources\synthetic_controlled_network\synthetic_mobile_variable` | 0 | 128 |
| 802 | 6 | `manifests_trazas\phase3\final\synthetic_sources\synthetic_controlled_network\synthetic_perfect_high` | 0 | 128 |
| 803 | 6 | `manifests_trazas\phase3\final\synthetic_sources\synthetic_controlled_network\synthetic_periodic_oscillation` | 0 | 128 |
| 804 | 6 | `manifests_trazas\phase3\final\synthetic_sources\synthetic_controlled_network\synthetic_stable_low` | 0 | 128 |
| 805 | 6 | `manifests_trazas\phase3\final\synthetic_sources\synthetic_controlled_network\synthetic_stall_trap` | 0 | 128 |
| 806 | 6 | `manifests_trazas\phase3\final\synthetic_sources\synthetic_controlled_network\synthetic_sudden_drop` | 0 | 128 |
| 807 | 6 | `manifests_trazas\phase3\final\synthetic_sources\synthetic_controlled_network\synthetic_sudden_recovery` | 0 | 128 |
| 808 | 6 | `manifests_trazas\phase3\final\traces\synthetic_controlled_network\synthetic_high_jitter` | 0 | 128 |
| 809 | 6 | `manifests_trazas\phase3\final\traces\synthetic_controlled_network\synthetic_mobile_variable` | 0 | 128 |
| 810 | 6 | `manifests_trazas\phase3\final\traces\synthetic_controlled_network\synthetic_perfect_high` | 0 | 128 |
| 811 | 6 | `manifests_trazas\phase3\final\traces\synthetic_controlled_network\synthetic_periodic_oscillation` | 0 | 128 |
| 812 | 6 | `manifests_trazas\phase3\final\traces\synthetic_controlled_network\synthetic_stable_low` | 0 | 128 |
| 813 | 6 | `manifests_trazas\phase3\final\traces\synthetic_controlled_network\synthetic_stall_trap` | 0 | 128 |
| 814 | 6 | `manifests_trazas\phase3\final\traces\synthetic_controlled_network\synthetic_sudden_drop` | 0 | 128 |
| 815 | 6 | `manifests_trazas\phase3\final\traces\synthetic_controlled_network\synthetic_sudden_recovery` | 0 | 128 |
| 816 | 6 | `runs_trazas\fase_verificacion_cliente_y_controllers_clasicos\runs\server_smoke\bba\run_20260608_102118` | 0 | 6 |
| 817 | 6 | `runs_trazas\fase_verificacion_cliente_y_controllers_clasicos\runs\server_smoke\bola\run_20260608_102220` | 0 | 6 |
| 818 | 6 | `runs_trazas\fase_verificacion_cliente_y_controllers_clasicos\runs\server_smoke\mpc\run_20260608_102322` | 0 | 6 |
| 819 | 6 | `runs_trazas\fase_verificacion_cliente_y_controllers_clasicos\runs\server_smoke\rate_based\run_20260608_102016` | 0 | 6 |
| 820 | 6 | `runs_trazas\fase_verificacion_cliente_y_controllers_clasicos\runs\server_smoke\robust_mpc\run_20260608_102424` | 0 | 6 |
| 821 | 6 | `runs_trazas\phase3_5\smoke\scenarios\complete_use_for_eval\dry_run` | 0 | 3 |
| 822 | 6 | `runs_trazas\phase3_5\smoke\scenarios\complete_use_for_eval\qoe` | 0 | 3 |
| 823 | 6 | `runs_trazas\phase3_5\smoke\scenarios\incomplete_session\dry_run` | 0 | 3 |
| 824 | 6 | `runs_trazas\phase3_5\smoke\scenarios\incomplete_session\qoe` | 0 | 3 |
| 825 | 6 | `runs_trazas\phase3_5\smoke\scenarios\legacy_do_not_use_for_eval\dry_run` | 0 | 3 |
| 826 | 6 | `runs_trazas\phase3_5\smoke\scenarios\legacy_do_not_use_for_eval\qoe` | 0 | 3 |
| 827 | 6 | `runs_trazas\phase3_5\smoke\scenarios\source_claims_benchmark\dry_run` | 0 | 3 |
| 828 | 6 | `runs_trazas\phase3_5\smoke\scenarios\source_claims_benchmark\qoe` | 0 | 3 |
| 829 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_1\Dataset\Bus_B57` | 0 | 2 |
| 830 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_1\Dataset\Bus_B62` | 0 | 2 |
| 831 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_1\Dataset\Bus_M15` | 0 | 2 |
| 832 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_1\Dataset\Bus_NYU_Campus` | 0 | 1 |
| 833 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_1\Dataset\Car` | 0 | 2 |
| 834 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_1\Dataset\Ferry` | 0 | 5 |
| 835 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_1\Dataset\LIRR` | 0 | 2 |
| 836 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_1\Dataset\Subway_7Train` | 0 | 2 |
| 837 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_1\Dataset\Subway_D_Train` | 0 | 2 |
| 838 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\NYU-METS\Dataset\Dataset_1\Dataset\Subway_Q_Train` | 0 | 3 |
| 839 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset\Amazon_Prime\Driving\animated-AdventureTime` | 0 | 7 |
| 840 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset\Amazon_Prime\Driving\Season3-TheExpanse` | 0 | 14 |
| 841 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset\Amazon_Prime\Static\animated-Ninjago` | 0 | 3 |
| 842 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset\Amazon_Prime\Static\Season3-TheExpanse` | 0 | 5 |
| 843 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset\Netflix\Driving\animated-RickandMorty` | 0 | 9 |
| 844 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset\Netflix\Driving\Season3-StrangerThings` | 0 | 14 |
| 845 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset\Netflix\Static\animated-RickandMorty` | 0 | 4 |
| 846 | 7 | `dataset en bruto\Lumos5G, UCC 4G LTE, UCC 5G, NYU‑METS\UCC 5G Beyond Throughput, The Next Generation\5G-production-dataset\Netflix\Static\Season3-StrangerThings` | 0 | 6 |

## Punto exacto de continuacion

Estado operativo al generar este documento:

- Rama: `rebuild/phase3-from-phase2`.
- Fase activa global: Phase 6 implementation ready - validacion comparativa formal.
- Fase IA nueva activa: Fase 4-5 v1/v3, con Neural-MPC v1/v2 y linea paralela closed-loop SPBC/SPC v1.
- No hay autorizacion general para benchmark/ranking/ganador fuera de Phase 6 con gates superados.
- Cualquier modelo IA nuevo debe seguir el embudo documentado en `proceso_desarrollo_ia_abr.md`.
- `phase45_v3_neural_throughput_calibrated_mpc_v1` no debe tocarse por abrir lineas paralelas.
- `phase45_v3_closedloop_spbc_spc_v1` acaba de autorizar dataset pilot/generador, no entrenamiento ni runtime.

Checklist que debe aplicar una IA externa antes de actuar:

1. Leer `AGENTS.md`.
2. Leer los tres documentos obligatorios.
3. Verificar `git status --short --branch`.
4. Identificar si la tarea afecta a runtime/player/controller/evaluacion.
5. No tocar `player.py`, runtime, media engine, controllers ni evaluacion sin contrato explicito y tests.
6. No usar PDFs brutos si existe `.md` operativo.
7. No llamar benchmark a smoke, dry-run, entrenamiento offline ni diagnostico.
8. Mantener datasets/modelos/runs fuera de Git.
9. Dar a Daniel comandos cortos versionados.
10. Si una linea se bloquea mas de dos ejecuciones sin avance de paso, generar informe objetivo autosuficiente de bloqueo.

Formula final que rige comparacion formal:

```text
reward_n = bitrate_mbps - 4.3 * rebuffer_s - smoothness_mbps
primary_session_metric = qoe_linear_mean
```

Frase metodologica valida:

> El proyecto busca un controller IA ABR propio defendible, integrado como controller normal del cliente, evaluado solo mediante protocolo Phase 6 reproducible con trazas, media profile, QoE y gates congelados.
