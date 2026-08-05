# Revisión final técnica (ojos frescos) — línea mpc_prudente + paquete tfg_final

| Campo | Valor |
|---|---|
| Fecha | 2026-08-05 |
| Autor | Claude (revisión), Daniel (decisión) |
| Alcance | `core/mpc_prudente/`, `core/controller/mpc_prudente_runtime.py`, `core/phase6/`, runner, paquete `20260624_182747_tfg_final` |
| Veredicto | **El paquete final es VÁLIDO. Ningún hallazgo lo invalida. No hace falta re-ejecutar.** |

## 1. Qué se verificó (y salió bien)

- **Recomputación independiente de QoE**: se reconstruyó `qoe_linear_mean` de una sesión
  (s00024, v2 + blender 60fps) desde `segment_telemetry.csv` crudo con la fórmula congelada
  (`bitrate_mbps − 4.3·rebuffer − smoothness`): coincide exacto con `session_summary.csv` (0.7655).
- **Paquete internamente consistente**: 360/360 sesiones completed y evaluables; agregados solo
  con las 288 reales (48/controller); 8 gates OK; verificación automática OK; cifras del
  HANDOFF = cifras del paquete (QoE 2.0134, stalls 0.29 vs 0.44, >5s 12% vs 23%, sign_p 0.5413).
- **Auditoría neural**: 1740/1740 filas auditadas POR CADA propio (v1 y v2), 0 fallback,
  0 diagnostic_only, inferencia presente en todas las filas.
- **Multi-vídeo sin sesgo confirmado en evidencia**: los client_configs del paquete inyectan
  `media_profile_id` del vídeo activo a los mpc_prudente (p. ej. sesión v2+blender60 recibe
  `blender_10min_60fps_4s`). El planner usó los tamaños VBR reales del vídeo que reproducía.
- **Sin fuga**: 15 ventanas todas de `split=eval`; el contrato de features
  (`build_context_features` + `reject_forbidden_model_inputs`) no expone trace_id/split/futuro.
- **Matemática del planner correcta**: cuantiles re-monotonizados, CVaR = media de los
  peores ceil(α·K) escenarios, simulación de buffer estándar, recompensa = fórmula QoE congelada.
- **Suite**: 489 tests OK en Windows; `check_client_readiness.py --strict` 104 OK / 0 FAIL.

## 2. Hallazgos (ninguno invalida; por severidad)

### A. [MEDIO — narrativa] En tfg_final el CVaR corrió con `risk_alpha=0.75` FIJO, no adaptativo por buffer
- El config del cliente pasó `risk_alpha: 0.75` explícito a v1 y v2 → `risk_alpha_override`
  activo → la regla `buffer_risk_alpha` (menos buffer → alpha menor) NO se usó en Phase 6.
  Sí está documentado en `runbook_mpc_prudente_runtime_y_phase6_20260623.md`, así que no hay
  mentira, pero el docstring de `planner.py` vende la regla adaptativa como parte del diseño.
- Con α=0.75 y 4 cuantiles, el objetivo real que corrió es: **media de los 3 escenarios más
  pesimistas (q10, q25, q50), descartando q75**. Eso es lo que la memoria debe describir.
- `buffer_risk_alpha` + constantes RISK_* quedan como código no ejercitado en el resultado
  final (solo en diagnósticos offline). Riesgo de pregunta de tribunal. Opciones: (a) memoria
  lo cuenta como "regla disponible, evaluada offline, fijada a 0.75 para el experimento final";
  (b) en la fase de naturalización se simplifica. Decidir en Fase 2.

### B. [MEDIO — matices estadísticos que la memoria debe respetar]
Conteos win/loss/tie por escenario pareado (48 reales):
- **v2 vs robust_mpc: W10 / L14 / T24.** El empate (p=0.54) y la media más alta son ciertos,
  pero v2 NO gana a robust "por ventanas" (pierde 14 de las 24 no empatadas). La ventaja de
  v2 es agregada: evita más catástrofes (colas de rebuffer). Redactar así, nunca "gana en la
  mayoría de escenarios".
- **24/48 empates EXACTOS v2=robust**: ventanas fáciles donde ambos saturan la escalera sin
  stalls y toman decisiones idénticas. Explica el n efectivo del sign test (24) y es un buen
  argumento: la diferencia se juega solo en ventanas difíciles.
- **v2 vs v1: W18 / L9 / T21, Δmedia +0.079, CI95 bootstrap [+0.020, +0.168] (excluye 0),
  sign_p=0.12.** El claim "v2 mejora a v1" SÍ se sostiene por el CI pareado del bootstrap,
  aunque el sign test no llegue a significativo. Citar el CI, no solo las medias.
- **rate_based vs robust: media +0.026 pero W12 / L36, sign_p=0.0007** → robust gana a
  rate_based en 3 de cada 4 ventanas; la media de rate_based solo es mayor porque evita
  catástrofes. El HANDOFF lista "+0.026" sin este matiz; la memoria no debe presentar a
  rate_based como "empatado con robust" sin decirlo.
- **v2 vs rate_based: W38 / L10, sign_p=0.0001** (media +0.035, CI incluye 0). Claim positivo
  disponible: v2 gana a rate_based en la gran mayoría de ventanas de forma significativa
  (aunque la magnitud media no sea distinguible de 0).

### C. [BAJO] Dos ventanas reales comparten `leakage_group` (`ghent_4g_lte:bus`: real_008 y real_009)
No es fuga train→eval (ambas en eval; el split protege el entrenamiento). Solo reduce un poco
la independencia entre 2 de los 48 escenarios. Mencionable como limitación menor, o ignorar.

### D. [BAJO — arreglo seguro] `core/phase6/catalog.py` sin defaults para `mpc_prudente_v2`
`DEFAULT_CONTROLLER_ALIASES`/`HUMAN_NAMES` no incluyen `mpc_prudente_v2` (y mapean v1 a
`propio_mpc_prudente`, no al `propio_mpc_prudente_v1` usado). Los nombres del tfg_final
salieron del config local de Ubuntu. Si alguien re-ejecuta sin ese config, los alias cambian.
Arreglo cosmético seguro (solo presentación; no toca resultados).

### E. [BAJO — cosmético] Diagnostics iniciales de v2 con key de v1
`MpcPrudenteTemporalRuntimeController.__init__` crea los diagnostics base antes de sobrescribir
`controller_key`; se corrige en la primera decisión. Cero efecto en telemetría de sesión.

### F. [BAJO — endurecimiento opcional] `_ensure_faithful_ladder` solo valida el NÚMERO de
representaciones vs el cliente, no los valores de bitrate de la escalera. En la práctica ambas
son [300..4300] verificadas. Se puede añadir comparación de bitrates (arreglo seguro).

### G. [BAJO — cosmético] Gate `all_members_finite_loss` (temporal_training) exige además
`val_pinball < 10.0`, pero el threshold reportado dice solo "finite". Renombrar o reflejar.

### H. [NOTA defensa] Latencia de decisión de los propios ≈ 190 ms de media (p95 ≈ 250–285 ms):
el planner enumera 6^5=7776 secuencias en Python puro. Muy por debajo del segmento de 4 s y
reportado en `overhead_decision`. Respuesta preparada: no se optimizó porque no era cuello.

### I. [NOTA defensa] CVaR sobre 4 cuantiles equiponderados: (0.10,0.25,0.50,0.75) no son
escenarios equiprobables; tratarlos igual sesga hacia la cola inferior. Es una aproximación
discreta CONSERVADORA, coherente con el diseño prudente. Tenerlo articulado para el tribunal.

## 3. Decisiones pendientes (Daniel)
1. Hallazgo A: ¿memoria cuenta la regla adaptativa como "disponible pero fijada a 0.75", o se
   simplifica el código en la naturalización? (Ninguna opción exige re-ejecutar.)
2. Arreglos seguros D/F/G: aplicarlos en la pasada de naturalización (Fase 2), con tests.
3. Matices B: incorporarlos tal cual a la redacción de resultados de la memoria.

## 4. Flags
`benchmark_performed=true (Phase 6 tfg_final, gates OK)` — este doc no cambia claims;
los claims autorizados siguen siendo los del HANDOFF con los matices del punto 2.B.
