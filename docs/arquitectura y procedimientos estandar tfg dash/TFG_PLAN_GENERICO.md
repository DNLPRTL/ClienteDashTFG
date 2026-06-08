# Plan generico del TFG

_Paquete imprescindible para trasladar DashClientModular4 a otro proyecto o a otra IA sin cargar toda la documentacion historica._

## 1. Identidad del proyecto

- Proyecto: DashClientModular4.
- Tema: ABR con IA para streaming MPEG-DASH.
- Objetivo general: construir un cliente DASH modular, implementar baselines ABR clasicos, integrar un controlador IA propio y preparar una evaluacion comparativa defendible.
- Estado consolidado al generar este paquete: Phase 1 a Phase 5 cerradas; la Fase de Verificacion del cliente y los controllers clasicos esta cerrada en Ubuntu. La fase activa pasa a Phase 6 planning. No hay benchmark final autorizado todavia.

## 2. Resultado esperado del TFG

El TFG debe terminar con:

1. Un cliente DASH Python modular, reproducible y ABR-neutral.
2. Baselines ABR clasicos implementados y testeados bajo un contrato comun.
3. Un controlador IA propio integrado como controller normal del cliente.
4. Un protocolo de evaluacion reproducible con trazas, media profile, QoE y estadistica.
5. Comparacion formal solo cuando Phase 6 autorice benchmark.
6. Memoria academica alineada con la estructura del profesor, la plantilla LaTeX oficial y la normativa UGR/ETSIIT.

## 3. Fases del trabajo

### Phase 1 - Client hardening

Estado: cerrada.

Objetivo: convertir el cliente DASH en una base tecnica estable. La fase deja config YAML, run layout reproducible, outputs canonicos, fake engine, GStreamer como integracion/demo, controller contract, benchmark neutrality y readiness gate.

No significa: benchmark, ranking, QoE final, baselines academicos o IA.

### Phase 2 - Baselines ABR

Estado: cerrada.

Objetivo: transformar literatura ABR en controllers reales y trazables. Incluye sanity controllers, rate_based, BBA, BOLA, MPC y RobustMPC, con paper cards, specs, mappings, acceptance tests y cierre estructural.

No significa: comparacion formal ni ganador.

### Phase 3 - Traces y replay

Estado: cerrada.

Objetivo: definir trazas, normalizacion, manifests, split policy, replay trace-driven y limites de leakage.

No significa: benchmark final ni claims de generalizacion.

### Phase 3.5 - QoE y reward

Estado: cerrada.

Objetivo: congelar qoe_linear_v1, reward_n, metricas secundarias, gates de evaluacion y politicas de no ranking.

No significa: resultados comparativos, plots o winner.

### Phase 4 - NeuralABR-Lite offline

Estado: cerrada.

Objetivo: construir NeuralABR-Lite Candidate Scorer como modelo pequeno, CPU-first, entrenado por imitation learning con robust_mpc como teacher y exportado como bundle local-only.

No significa: controller integrado ni claim de mejora.

### Phase 5 - Integracion del controller IA

Estado: cerrada.

Objetivo: integrar `neural_abr_lite` como guarded neural scorer controller con action mask, safety guard, fallback, carga segura de bundle, inferencia CPU y telemetria diagnostica.

No significa: que la IA gane, ranking, benchmark, SOTA o validacion real-world.

### Fase de Verificacion - Cliente y controllers clasicos

Estado: cerrada en Ubuntu.

Objetivo: demostrar que el cliente reproduce contenido DASH, genera artifacts
canonicos, no contamina pruebas futuras y usa controllers clasicos coherentes
con sus specs locales.

No significa: benchmark, ranking, ganador, comparacion QoE ni afirmacion de
mejora.

### Phase 6 - Validacion comparativa formal

Estado: pipeline implementado para ejecucion en Ubuntu cliente; benchmark solo se autoriza por gates del paquete generado.

Objetivo actual: ejecutar comparacion formal con protocolo congelado, red controlada por trazas, QoE `qoe_linear_v1`, estadistica emparejada y paquete de evidencia externo. La seleccion formal compacta timestamps de traza a tiempo continuo, evalua 30 segmentos de media de 4 s y usa una ventana de replay de red con margen para rebuffering.

No significa: ganador automatico ni afirmacion de mejora QoE; `rapido` no autoriza ranking y `equilibrado`/`extendido` solo lo autorizan si pasan todos los gates.

### Phase 7 - Memoria y defensa

Estado: referencia activa.

Objetivo: redactar y defender el TFG usando el material tecnico de fases, la estructura del profesor, la plantilla LaTeX oficial y la normativa UGR/ETSIIT.

## 4. Metodologia permanente

La regla central es investigacion just-in-time por fase:

1. Definir la pregunta tecnica.
2. Buscar solo las fuentes necesarias.
3. Analizar PDFs o papers relevantes.
4. Convertir cada fuente en `.md` operativo.
5. Convertir decisiones cientificas en specs implementables.
6. Codex implementa desde `.md`, no desde PDFs brutos.
7. Validar con tests, runbooks, readiness checks y revision.
8. Cerrar bloque y documentar limites.

Codex no debe decidir ciencia desde cero. Codex ejecuta cuando existen contratos, specs y acceptance tests.

## 5. Flujo PDF -> MD -> Codex

Flujo recomendado para cada paper o fuente:

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

Contenido minimo de una `paper_card.md`:

- titulo, autores, ano, venue y DOI/URL si existe;
- problema que resuelve;
- algoritmo o metodologia;
- variables, unidades, datasets y metricas;
- que aporta al TFG;
- que no aporta;
- decision practica derivada;
- uso previsto en memoria.

Contenido minimo de una `implementation_spec.md`:

- entradas necesarias desde el cliente;
- salida esperada;
- pseudocodigo, formulas y parametros;
- unidades;
- edge cases;
- simplificaciones aceptadas y prohibidas;
- logging/telemetry;
- criterios de aceptacion;
- riesgos.

## 6. Reglas permanentes

- No llamar benchmark a smoke tests.
- No llamar training dataset a CSVs runtime.
- No usar dry-runs legacy como training data.
- No mezclar fake engine y GStreamer como evidencias equivalentes.
- No commitear datasets, logs, CSVs generados, zips, modelos, bundles, PDFs, media ni artefactos externos.
- No usar `git add .`.
- No tocar player/runtime/media sin contrato y tests.
- No permitir que un controller vea `trace_id`, `dataset_id`, split, OOD label o futuro throughput.
- No declarar que `neural_abr_lite` mejora QoE hasta una evaluacion formal autorizada.
- No producir rankings, plots o winner antes de Phase 6E o fase equivalente explicitamente autorizada.

## 7. Validaciones base

Para bloques documentales:

```powershell
git status --short --branch
git diff --check
python -m unittest discover
python scripts/check_client_readiness.py --strict
```

Para bloques de controller:

```powershell
git status --short --branch
git diff --check
python -m unittest discover
python scripts/check_client_readiness.py --strict
```

Ademas, revisar manifest, CSVs, telemetria y que no aparezcan artefactos legacy como `dataset.csv` o `dataset_training.csv`.

Para bloques de validacion:

- validar manifests;
- validar leakage guards;
- validar readiness;
- mantener datasets y reportes fuera de Git;
- no ejecutar benchmark si `benchmark_authorized=false`.

## 8. Memoria y defensa

La memoria debe seguir la estructura indicada por el profesor:

1. Introduccion.
2. Antecedentes y estado del arte.
3. Planificacion y costes.
4. Diseno.
5. Implementacion.
6. Evaluacion.
7. Conclusiones y trabajo futuro.
8. Bibliografia.
9. Anexos.

Reglas de estilo:

- estilo impersonal;
- frases cortas;
- cada capitulo abre con contexto y cierra con resumen;
- toda figura y tabla debe estar numerada, descrita y referenciada;
- las citas deben ser trazables;
- la plantilla LaTeX oficial UGR/ETSIIT y la convocatoria vigente prevalecen sobre cualquier plan interno.

## 9. Material imprescindible que acompana este plan

Para trasladar el proyecto a otra IA, usar este paquete minimo:

- `TFG_PLAN_GENERICO.md`: este plan.
- `TFG_CONTEXTO_DESARROLLO_NORMALIZADO.md`: historia y estado real reconciliado.
- `06_validation_super.md`: fase activa/preparatoria actual.
- `07_memory_thesis_super.md`: memoria y defensa.
- `99_roadmap_runbooks_super.md`: indices, runbooks y roadmap operativo.

Los super documentos eliminados del paquete minimo no se consideran perdidos: son sintetizados por el contexto normalizado y siguen existiendo en la documentacion original fuera de `_super`.
