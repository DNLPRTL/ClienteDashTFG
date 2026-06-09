# AGENTS.md

Guia permanente de trabajo para `DashClientModular4`.

## Estado actual

El proyecto esta en la rama:

```text
rebuild/phase3-from-phase2
```

El trabajo anterior de fases 3, 3.5, 4, 5 y 6 esta protegido como referencia
historica en:

```text
archive/current-before-phase3-rebuild
```

La fase activa es:

```text
Phase 6 implementation ready - validacion comparativa formal
```

Phase 1 y Phase 2 se consideran cerradas. Phase 3 Rebuild esta cerrada en
Windows con corpus externo, auditoria de calidad, replay tecnico y manifest
curado recomendado para preparacion de entrenamiento/evaluacion. Phase 3.5
Rebuild esta cerrada en Windows con contrato `qoe_linear_v1`, calculadora QoE
pura, postprocesador QoE, gates y smokes sinteticos controlados. Phase 4 Rebuild
esta cerrada en Ubuntu con dos bundles offline `NeuralABR-Lite`: uno entrenado
con `robust_mpc` real y otro con `teacher_hibrido`. No hay benchmark, ranking,
ganador ni afirmacion de mejora de QoE autorizados.
Phase 5 esta cerrada en Ubuntu con dos controllers IA integrados.
La Fase de Verificacion del Cliente y Controllers Clasicos esta cerrada en
Ubuntu con informe externo aceptado. Phase 6 dispone de pipeline reproducible
para ejecutar evaluacion formal en Ubuntu cliente sin reutilizar smokes como
benchmark.

Fase 4-5 v1 queda abierta como iteracion nueva e independiente para crear
controllers IA nuevos. No sustituye a las Phase 4 y Phase 5 cerradas, y no debe
heredar automaticamente decisiones de `NeuralABR-Lite`. El punto de partida
canonico es el corpus `.md` creado desde cero en:

```text
docs/contexto rama nueva/fase_4_5_v1/abr ia md/
```

Antes de decidir modelo, entrenamiento, dataset derivado o controller para
Fase 4-5 v1, leer ese corpus operativo y documentar la decision nueva.

## Documentos obligatorios por ejecucion

Antes de hacer cambios relevantes, leer siempre:

```text
docs/arquitectura y procedimientos estandar tfg dash/arquitectura_y_procedimientos_estandar_tfg_dash.md
docs/arquitectura y procedimientos estandar tfg dash/TFG_PLAN_GENERICO.md
```

Usar tambien como contexto secundario, cuando haga falta:

```text
docs/contexto rama nueva/
docs/contexto rama original/
docs/contexto del orquestador el chat web/
docs/todos los estudios pdf convertidos a md/
```

No implementar directamente desde PDFs brutos si existen source cards, specs,
decisiones canonicas o documentos operativos.

## Rutas externas actuales

Los datos pesados y derivados viven fuera del repositorio, bajo:

```text
C:\Users\danie\Documents\TFG
```

Rutas activas:

```text
C:\Users\danie\Documents\TFG\dataset en bruto
C:\Users\danie\Documents\TFG\datasets_normalizados
C:\Users\danie\Documents\TFG\manifests_trazas
C:\Users\danie\Documents\TFG\runs_trazas
C:\Users\danie\Documents\TFG\auditorias_trazas
C:\Users\danie\Documents\TFG\modelos
```

Entorno WSL2/ROCm disponible para entrenamiento IA pesado:

```text
Distribucion: Ubuntu-24.04 en WSL2
Venv GPU: ~/venvs/rocm721
Torch observado: 2.9.1+rocm7.2.1
GPU observada: AMD Radeon RX 7800 XT
Repo recomendado dentro de WSL: ~/TFG/DashClientModular4
Raiz pesada recomendada dentro de WSL: ~/TFG
```

En WSL2, no usar `/mnt/c/Users/danie/Documents/TFG/...` como ruta principal de
entrenamiento ni de ficheros grandes. Puede servir para consultas puntuales,
pero datasets, checkpoints, modelos, logs y runs de entrenamiento deben vivir
bajo rutas Linux dentro de `~/TFG`.

Artifacts externos relevantes:

```text
C:\Users\danie\Documents\TFG\manifests_trazas\phase3\final\phase3_trace_manifest_curated.json
C:\Users\danie\Documents\TFG\runs_trazas\phase3_5\smoke
```

No commitear datasets, trazas normalizadas, manifests finales generados, runs,
logs, modelos, bundles, zips, PDFs, videos, segmentos DASH ni otros artifacts
pesados/generados.

## Reglas permanentes

1. Mantener el cliente limpio, modular y testeable.
2. Usar staging explicito por ruta. No usar `git add .`.
3. Todo cambio importante debe tener commit propio.
4. Windows desarrolla, testea rapido, commitea y pushea; Ubuntu cliente ejecuta
   las validaciones relevantes.
5. GitHub es el puente limpio entre Windows y Ubuntu cliente.
6. WSL2 Ubuntu con ROCm entrena IA pesada cuando haga falta, pero no sustituye
   la validacion formal de Ubuntu cliente.
7. Ubuntu servidor solo sirve MPD, segmentos e inicializaciones DASH; no define
   la red experimental.
8. No tocar `player.py`, runtime, media engine, controladores ni evaluacion sin
   contrato explicito y tests.
9. No mezclar contenido DASH, trazas de red, resultados, entrenamiento y
   benchmark.
10. No llamar benchmark a smoke tests, dry-runs, conversiones ni auditorias.
11. No declarar mejora de QoE, ranking, ganador ni generalizacion antes de una
    fase de evaluacion formal autorizada.

## Phase 3 Rebuild guardrails

La unidad canonica de throughput normalizado es:

```text
throughput_kbps
```

El schema de traza normalizada de Phase 3 es:

```csv
timestamp_s,duration_s,throughput_kbps
```

Los metadatos de trazas, splits y auditoria se guardan separados de las muestras
que vera el replay. Un controller no debe ver:

```text
trace_id
dataset_id
source_id
split
group_id
leakage_group
OOD label
futuro throughput
```

Los splits `train`, `test` y `eval` deben hacerse por `leakage_group`/grupo
semantico, nunca por filas.

FCC, Puffer y GAViST pueden procesarse, pero sus semanticas deben quedar
marcadas de forma explicita para no tratarlas sin control como equivalentes a
trazas directas de ancho de banda disponible.

## Phase 3.5 Rebuild guardrails

La formula QoE/reward cerrada para esta rama es:

```text
qoe_formula_version=qoe_linear_v1
reward_n = bitrate_mbps - 4.3 * rebuffer_s - smoothness_mbps
primary_session_metric=qoe_linear_mean
```

`qoe_log_v1` queda como metrica secundaria de sensibilidad. `startup_delay_s`
queda report-only. VMAF queda deferred/artifact-dependent.

Los gates validos son:

```text
use_for_eval
diagnostic_only
do_not_use_for_eval
```

Los smokes de QoE son sinteticos y no consumen trazas reales. Sus salidas deben
mantener:

```text
outputs_are_benchmark_results=false
benchmark_performed=false
ranking_performed=false
no_final_ranking=true
ia_training_performed=false
```

Phase 4 ya cerro el contrato de sampler/corpus y el entrenamiento offline. Phase
5 integro los bundles como controllers sin convertir smokes en benchmark. La
Fase de Verificacion comprobo cliente y controllers clasicos sin benchmark,
ranking, ganador ni afirmacion de mejora. Phase 6 debe ser la primera fase que
autorice evaluacion comparativa formal, si antes congela protocolo, trazas,
media profile, QoE y gates.

## Synthetic controlled trace guardrails

El addendum sintetico de Phase 3 usa:

```text
dataset_id=synthetic_controlled_network
semantics=synthetic_available_bandwidth
generator_id=phase3_synthetic_controlled_network_v1
```

Las trazas sinteticas pueden aparecer en `train`, `test` y `eval`, pero cualquier
resultado futuro debe reportarse separado de trazas reales. No usar resultados
sinteticos para afirmar generalizacion real-world. Phase 4 debe limitar su cuota
en el sampler para evitar que dominen el aprendizaje.

El manifest curado actualizado con sinteticas queda en:

```text
C:\Users\danie\Documents\TFG\manifests_trazas\phase3\final\phase3_trace_manifest_curated.json
```

Conteo esperado tras el addendum:

```text
trace_count=6768
synthetic_trace_count=1024
synthetic_split_counts=train:720,test:152,eval:152
```

## Separacion tecnica

Mantener separados:

- parser MPD
- descarga de segmentos
- buffer
- motor de reproduccion
- control ABR
- logging
- evaluacion
- trace replay
- normalizacion de datasets
- documentacion cientifica
- workspaces externos

## Validacion minima esperada

En Windows, segun aplique:

```powershell
git status --short --branch
git diff --check
python -m unittest discover
python scripts/check_client_readiness.py --strict
```

En Ubuntu cliente, Daniel sincronizara con:

```bash
cd ~/TFG/DashClientModular4
git pull
```

Despues ejecutara el smoke/runbook indicado para la fase. Si Windows y Ubuntu
cliente discrepan, manda Ubuntu cliente.

En WSL2 para entrenamiento IA con GPU, Daniel sincronizara o clonara el repo en
`~/TFG/DashClientModular4`, activara `~/venvs/rocm721` y comprobara PyTorch:

```bash
wsl -d Ubuntu-24.04
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate
python3 -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

La salida esperada para el entorno GPU actual es `True` y `AMD Radeon RX 7800 XT`
o nombre equivalente de la GPU AMD expuesta por ROCm.
