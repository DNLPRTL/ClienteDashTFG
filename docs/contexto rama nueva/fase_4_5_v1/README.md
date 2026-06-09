# Fase 4-5 v1 - Nueva iteracion IA ABR

Status: paper_audit_started.

Esta fase no sustituye a las Phase 4 y Phase 5 cerradas. Es una iteracion
nueva para disenar controllers IA mas defendibles, empaquetables como bundles
reproducibles e integrables como controllers normales de Phase 6.

## Objetivo

Crear uno o varios controllers propios que reduzcan rebuffering y agresividad en
redes bajas o variables, manteniendo calidad razonable en redes medias y altas.

El resultado buscado no es declarar un ganador antes de Phase 6, sino producir
controllers con:

- comportamiento explicable por escenario;
- inferencia real auditada;
- fallback 0 en diagnostico y rapido;
- separacion limpia entre entrenamiento, bundle, controller y evaluacion;
- comparacion posterior contra clasicos y controllers propios previos.

## Guardrails

- No cerrar Phase 6 durante esta iteracion.
- No declarar mejora QoE, ranking ni ganador desde smokes, diagnosticos o
  presets no autorizados.
- No mezclar trazas sinteticas con conclusiones principales sobre redes reales.
- No commitear PDFs, modelos, bundles, runs, CSVs generados ni paquetes de
  evidencia.
- El controller no puede ver `trace_id`, `dataset_id`, `split`,
  `leakage_group`, etiquetas OOD, throughput futuro ni QoE futuro en runtime.

## Corpus inicial

Los PDFs viven fuera del repo:

```text
C:\Users\danie\Documents\TFG\abr ia pdf\abr ia pdf
```

La auditoria operativa versionable vive aqui:

```text
docs/contexto rama nueva/fase_4_5_v1/paper_audits/
```

## Documentos de esta fase

- `paper_audits/00_indice_corpus.md`: inventario PDF por PDF.
- `paper_audits/*.md`: ficha operativa por PDF.
- `decision_modelos_v1.md`: sintesis critica y planes de controller.

## Siguiente ciclo previsto

1. Auditar corpus ABR/IA.
2. Analizar fallos chunk a chunk de los controllers propios actuales en Phase 6.
3. Congelar plan Fase 4-5 v1.
4. Construir dataset offline sin leakage.
5. Entrenar o construir modelos candidatos.
6. Exportar bundles reproducibles.
7. Integrar controllers plug-and-play.
8. Ejecutar Phase 6 diagnostico y rapido en Ubuntu cliente.
