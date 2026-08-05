# Fase 2 — Naturalización del código de la línea mpc_prudente + apropiación

| Campo | Valor |
|---|---|
| Fecha | 2026-08-05 |
| Alcance | `core/mpc_prudente/`, `core/controller/mpc_prudente_runtime.py`, `core/phase6/catalog.py`, `docs/defensa/` |
| Regla | Solo mejora genuina. Cero cambios de comportamiento en runtime. Sin tocar player/runtime/eval congelados ni el historial de git. |
| Validación | `python -m unittest discover` → 489 OK; `check_client_readiness.py --strict` → 104 OK / 0 FAIL |

## Qué se cambió (y por qué NO altera resultados)

1. **Docstrings de módulo acortados** (media_profile, dataset, planner, training,
   temporal_model, temporal_training, bundle, temporal_bundle, evaluation,
   mpc_prudente_runtime): de "nota de diseño kilométrica" a resumen breve en
   español. Solo comentarios; cero código.
2. **planner.py — docstring honesto sobre `risk_alpha`** (hallazgo A de la
   revisión): deja claro que la regla adaptativa por buffer se usó solo en
   diagnósticos offline y que Phase 6 corrió con α=0.75 fijo.
3. **Deduplicación en bundles** (hallazgo de sobre-ingeniería): la verificación
   de tamaños/sha256 del manifiesto estaba copiada en `bundle.py` y
   `temporal_bundle.py` → helper común `verify_manifest_file_records`. La
   conversión log-ratio→bps (clip [0.15, 4.0] + sort) estaba copiada en los dos
   `predict()` → helper común `log_ratio_rows_to_bps`. Misma lógica, un solo sitio.
4. **Arreglo E (cosmético):** `MpcPrudenteTemporalRuntimeController` regenera sus
   diagnostics iniciales tras fijar `controller_key`, para que nunca exista un
   estado con key de v1. Sin efecto en telemetría de sesiones (se regeneraba en
   la primera decisión).
5. **Arreglo F (endurecimiento):** `_ensure_faithful_ladder` ahora compara también
   los VALORES de bitrate del perfil contra la escalera del cliente (antes solo el
   número de niveles). Si difieren → fallback auditado. En los datos reales
   coinciden siempre (misma fuente MPD), así que no cambia ninguna decisión.
6. **Arreglo G (cosmético):** el gate `all_members_finite_loss` de
   temporal_training declara su umbral real ("finita y < 10.0" en vez de "finite").
7. **Arreglo D:** `core/phase6/catalog.py` añade defaults de alias/nombre para
   `mpc_prudente_v2` y alinea los de v1 con los usados en `tfg_final`
   (`propio_mpc_prudente_v1/v2`). Solo presentación; el paquete final usó estos
   mismos nombres vía config local.
8. **Estilo:** eliminados los `;` de líneas múltiples en `temporal_training._load_examples`.

## Qué NO se tocó a propósito

- `core/phase6/analysis.py`, `selection.py`, `verification.py`, runner: producen
  la evidencia ya generada; cualquier retoque ahí crea riesgo de discrepancia
  código↔paquete sin beneficio.
- `buffer_risk_alpha` y constantes RISK_*: se mantienen (las usan los
  diagnósticos offline y los tests; y son la respuesta a la pregunta "¿trabajo
  futuro?"). El docstring ya cuenta la verdad.
- Ningún nombre público: los tests importan la API completa y siguen en verde.

## Material nuevo en docs/defensa/

- `material_reproducibilidad.md` — inventario EXACTO de la parte técnica: qué
  ficheros del repo + qué artefactos externos + qué contenido DASH hay que mover
  para repetir el experimento en otro PC, y qué es redundante.
- `apropiacion_codigo_mpc_prudente.md` — módulo a módulo: qué hace, por qué, y el
  flujo end-to-end para contarlo de memoria.
- `preguntas_tribunal_respuestas.md` — 25 preguntas probables con respuesta.
