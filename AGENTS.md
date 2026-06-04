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
Phase 3 Rebuild - traces, normalization and splits
```

Phase 1 y Phase 2 se consideran cerradas. Phase 3 se esta rehaciendo desde el
cierre real de Phase 2 por errores detectados en configuracion de trazas, trace
replay, seleccion de datasets y dependencias posteriores. No hay benchmark,
training IA, ranking, ganador ni afirmacion de mejora de QoE autorizados.

## Documentos obligatorios por ejecucion

Antes de hacer cambios relevantes, leer siempre:

```text
docs/arquitectura y procedimientos estandar tfg dash/arquitectura_y_procedimientos_estandar_tfg_dash.md
docs/arquitectura y procedimientos estandar tfg dash/TFG_PLAN_GENERICO.md
```

Usar tambien como contexto secundario, cuando haga falta:

```text
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
6. Ubuntu servidor solo sirve MPD, segmentos e inicializaciones DASH; no define
   la red experimental.
7. No tocar `player.py`, runtime, media engine, controladores ni evaluacion sin
   contrato explicito y tests.
8. No mezclar contenido DASH, trazas de red, resultados, entrenamiento y
   benchmark.
9. No llamar benchmark a smoke tests, dry-runs, conversiones ni auditorias.
10. No declarar mejora de QoE, ranking, ganador ni generalizacion antes de una
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
