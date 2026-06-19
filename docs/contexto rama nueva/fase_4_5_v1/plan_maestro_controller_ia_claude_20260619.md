# Plan maestro — Controller IA ABR defendible (línea nueva `phase45_v4`)

| Campo | Valor |
|---|---|
| Autor | Claude (Claude Code, desktop) |
| Fecha | 2026-06-19 |
| Rama | `rebuild/phase3-from-phase2` |
| Estado | Propuesta de arranque. Documentación + decisión. Sin código de controller todavía. |
| Sustituye a | Continuación a ciegas de Neural-MPC v2 y de las líneas SPBC/SPC y Q_H scorer |
| Reglas | Hereda todos los contratos de `AGENTS.md` y `CLAUDE.md` (QoE congelada, no benchmark sin gates, no tocar runtime/player/eval sin contrato+tests) |

Este documento es autosuficiente: una IA externa (o Codex tras `git pull`) debe
poder entender el plan sin este chat.

---

## 1. Objetivo real (sin autoengaños)

Construir **un** controller ABR con IA que sea **digno de tribunal de TFG de
Teleco**: que demuestre que el autor sabe de IA, está al día del ABR/DASH actual,
aplica técnicas con criterio, y obtiene algo **interesante, seguro, interpretable
y justificado en evidencia**.

No es objetivo "ganar a todos los baselines en todo" ni "romper el paradigma del
streaming". El objetivo es: bajo el protocolo riguroso Phase 6, un controller IA
propio **seguro, interpretable y competitivo (no peor que `robust_mpc` dentro de
intervalo de confianza, mejor en algún régimen)**, con el **rigor metodológico**
como aportación principal.

Plazo: ~2 semanas para la parte técnica (cliente ya hecho + controller IA
defendible + evaluación Phase 6). La memoria escrita va después.

---

## 2. Diagnóstico honesto de lo anterior (qué falló y por qué)

Evidencia del último paquete `20260615_143801_rapido` (preset rápido, 50 sesiones,
gates técnicos OK, 0 fallback, inferencia auditada):

| Controller | QoE lineal media | Rebuffer medio (s) |
|---|---:|---:|
| `robust_mpc` | **2.330** | 1.487 |
| `rate_based` | 2.227 | 0.000 |
| Neural-MPC **v1** | 2.179 | 2.502 |
| Neural-MPC **v2** | 1.935 | 3.988 |
| `bola` | 1.478 | 3.481 |

Caso que rompe (ventana `real_006_d2d8a29c20`, `media_capacidad_variable`):

| Controller | QoE | Rebuffer (s) |
|---|---:|---:|
| `rate_based` | 0.545 | 0.000 |
| `robust_mpc` | -0.151 | 4.771 |
| Neural v1 | -1.835 | 16.285 |
| Neural v2 | -2.761 | **21.750** |

Hechos:

1. **"Más datos" no arregló nada.** v2 se entrenó con dataset full; v1 era pilot.
   v2 quedó **más agresiva justo donde no debía** (elige 4300 kbps en capacidad
   media variable y se come rebuffers enormes). Más entrenamiento empeoró el QoE.
2. **El bug viejo de buffer ya estaba corregido** (`max_buffer_s=60.0` en
   `core/phase45_v3/abr_closed_loop_env.py`). No es eso.
3. **Sigue vivo un desajuste entrenamiento↔cliente en el MEDIO:** el entorno de
   entrenamiento y el planner usan **CBR** (`tamaño = bitrate × duración`):
   - `core/neural_abr/content_ladder.py:66` → `segment_size_bytes = bitrate_bps * segment_duration_s / 8`, con `segment_size_source = "bitrate_times_duration_bytes"`.
   - `core/phase45_v3/neural_mpc_controller.py` → planner con `segment_size_bits = bitrate_bps * segment_duration_s`.
   Pero el cliente real reproduce MPDs **VBR**: el segmento N pesa distinto cada
   vez (ej. Paseo 4300 kbps: total 306.91 MiB ≈ media nominal, pero por segmento
   varía). En ventanas de capacidad variable, ese error de estimación se suma a la
   varianza de red y produce el rebuffer catastrófico.
4. **Líneas muertas, bien diagnosticadas:** SPBC/SPC (colapso por desajuste
   offline↔cliente; filosofía de policy directa abandonada) y Q_H scorer (su
   target usa futuro inmediato no observable → estados visibles iguales con
   target distinto → no aprendible). **Se conservan como resultados negativos.**

### Tesis nueva (la aportación que defenderemos)

> **El cuello de botella no era el modelo de IA, sino (a) la falta de fidelidad
> del entorno de entrenamiento/planificación al medio real (VBR del MPD del
> cliente) y (b) la ausencia de un objetivo consciente del riesgo.**

Esto es defendible y actual:
- **Sesgo de simulación / sim-to-real:** CausalSim (NSDI'23), Puffer "Learning in
  situ" (NSDI'20), Gelato/Plume, "Into the wild" (2025) → entrenar/evaluar en
  simuladores no fieles sesga las conclusiones. Nuestra corrección ataca justo eso.
- **Incertidumbre + control:** BayesMPC ("Uncertainty-aware robust ABR with
  Bayesian NN + MPC") y Fugu/Puffer → predictor con incertidumbre + controlador
  explícito > policy neural opaca.
- **Deployability/consistencia:** Oboe, SODA → seguridad y consistencia importan
  tanto como el pico de QoE.

---

## 3. Paradigma elegido (y por qué, frente a alternativas)

**Mantener el paradigma híbrido `predictor neural + planner MPC explícito`**, pero
reconstruirlo bien. No es "seguir con v2": cambian los dos cimientos.

| Opción | Pros | Contras | Veredicto |
|---|---|---|---|
| **Híbrido predictor(incertidumbre)+MPC fiel al medio** | interpretable, seguro, actual (Fugu/BayesMPC), base ya existe y es arreglable, fallback robusto | incremental | **ELEGIDA** |
| RL puro (Pensieve/PPO) | "moderno" | caja negra, difícil defender seguridad, propenso a colapso (ya visto en SPBC), arriesgado en 2 semanas | descartada (sí como mención/ablación) |
| Imitation/BC de oráculo (Comyco/SABR) | simple | ya se hizo (NeuralABR-Lite), mediocre, hereda errores del experto | descartada como vía principal |
| Offline/Meta-RL (Fortuna/MERINA) | generalización | demasiado pesado para 2 semanas, difícil cerrar con rigor | fuera de plazo |

Por qué el híbrido gana para ESTE TFG: interpretable (el tribunal ve *por qué*
decide), seguro (fallback a `robust_mpc`, action mask, sin acciones inválidas),
al día (predictor + control con incertidumbre es lo que recomienda la literatura
de despliegue real), y **arreglable en plazo** porque el 80% ya está construido y
la causa raíz está identificada.

---

## 4. Los tres pilares de la línea `phase45_v4`

### Pilar A — Fidelidad al medio real (lo que pedía Daniel)

Entrenar y planificar en **el mismo medio que reproduce el cliente**: mismo MPD,
mismas 6 representations, mismo tamaño real de fragmento (VBR), mismos 4 s, mismo
buffer 60 s, mismo bucle de decisión.

- **Extraer una tabla real de tamaños de segmento** del servidor:
  `segmento N → bytes` por representación, para `paseo_10min_30fps_4s` (y luego
  `blender_10min_30fps_4s` y variantes 60fps si se usan en presets superiores).
- **Usar esa tabla en DOS sitios**: (1) el simulador closed-loop de entrenamiento
  y generación de dataset; (2) el modelo de tiempo de descarga del planner MPC.
- Resultado: el modelo aprende y planifica con la **física real de descarga**,
  no con una aproximación CBR. Esto ataca directamente `real_005/real_006`.

> Nota: la RED se sigue emulando con el corpus de trazas curado (eso ya es
> correcto y externo). Lo que arreglamos es el MEDIO. Son cosas distintas.

### Pilar B — Planificación consciente del riesgo (incertidumbre)

El predictor ya produce **cuantiles** de throughput futuro (q10/q25/q50/q75). Hoy
el planner usa una regla *a mano* "buffer → qué cuantil usar", que es frágil.

- Sustituir esa regla por un **objetivo de planificación con riesgo a la baja**:
  penalizar explícitamente la cola mala (rebuffer) usando la **distribución
  predictiva completa**, no un único cuantil. Forma concreta a evaluar:
  restricción de probabilidad sobre rebuffer (chance-constraint) o coste tipo
  **CVaR** sobre el peor caso del horizonte, modulado por la **anchura predicha**
  (más incertidumbre → más conservador).
- Esto es lo que hace que en `media_capacidad_variable` el controller **no se
  lance a 4300** cuando la cola predictiva dice que hay riesgo de stall.
- Grounded en BayesMPC: incertidumbre del predictor → robustez del MPC.

### Pilar C — Protocolo riguroso + resultados negativos como aportación

- Evaluación **solo** vía Phase 6 (protocolo, trazas, media profile, QoE, seeds,
  gates congelados). Deltas emparejados, CI95, sign-test. Sin claims sin gates.
- La memoria incluye explícitamente la **ablación**: v1 vs v2 (más datos no
  mejora), SPBC (colapso), Q_H (no aprendible), y el salto al arreglar fidelidad
  + riesgo. Eso es madurez científica y suma nota.

---

## 5. Embudo de desarrollo (sigue `proceso_desarrollo_ia_abr.md`)

```text
0. tabla de tamaños reales del medio (servidor -> JSON)           [Ubuntu cliente]
1. dataset pilot FIEL (red curada + medio VBR real)               [WSL]
2. auditoría del dataset pilot (anti-fuga, anti-colapso, gates)   [WSL]
3. entrenamiento pilot 1 seed                                     [WSL]
4. análisis de errores honesto                                    [Claude]
5. multi-seed si el pilot lo justifica                            [WSL]
6. diagnóstico closed-loop offline (gates, sin fallback)          [WSL]
7. bundle experimental externo                                    [WSL]
8. smoke runtime del controller                                   [Ubuntu cliente]
9. Phase 6 diagnostico (v4 vs robust_mpc/bola/rate_based)         [Ubuntu cliente]
10. Phase 6 rapido si pasa                                        [Ubuntu cliente]
11. decidir full / equilibrado solo si la evidencia lo justifica
```

Criterios permanentes de **no avance** (de `AGENTS.md`): no avanzar si
`best_epoch=0` por fallback, si copia la clase mayoritaria sin aprender, si rompe
gates anti-colapso, si produce acciones inválidas, si exige relajar gates, o si
necesita comandos manuales largos no versionados.

---

## 6. Criterio de éxito para la defensa

Se considera éxito (suficiente para un 10 de TFG, no para publicar en NSDI):

1. `phase45_v4` integrado como controller normal del cliente, **seguro**: 0
   fallback, 0 acciones inválidas, sin colapso high-capacity a acción 0.
2. **Interpretable**: el planner explica cada decisión (predicción + coste).
3. **Competitivo** bajo Phase 6 riguroso: QoE **no peor que `robust_mpc`** dentro
   de CI95, e idealmente mejor en al menos un bucket de dificultad (p. ej. evita
   el desastre de `real_006`).
4. **Aportación metodológica clara**: fidelidad al medio (sim-to-real del VBR) +
   planificación consciente del riesgo, con ablación honesta de los intentos
   previos.

No se promete superar a todos los baselines en todos los buckets.

---

## 7. Qué NO se toca

- `phase45_v3_neural_throughput_calibrated_mpc_v1/v2`: **congelados** como
  evidencia/ablación. No se borran ni se editan.
- `player.py`, runtime, media engine, controllers existentes, evaluación:
  intactos salvo contrato explícito + tests.
- Corpus de trazas de red (manifest curado): se usa tal cual; eval no se toca.
- Datasets/modelos/bundles/runs: fuera de Git, bajo `~/TFG/...`.

---

## 8. Primeros pasos concretos (próxima iteración)

1. **(Claude)** Escribir `scripts/` un extractor de tabla de tamaños reales de
   segmento (`segmento N → bytes` por representación) contra el servidor por HTTP
   (HEAD/Content-Length), salida JSON pequeña como *descriptor de media profile*.
2. **(Daniel, Ubuntu cliente)** `git pull` + `bash scripts/<extractor>.sh` →
   genera la tabla (el servidor solo es accesible desde la VM cliente).
3. **(Claude)** Diseñar el contrato del dataset pilot FIEL que consume esa tabla.
4. Continuar el embudo del punto 5.

---

## 9. Preguntas abiertas para Daniel (no bloquean documentar, sí bloquean código)

1. **Foto "antes":** ¿lanzamos primero **un** Phase 6 diagnostico de v2 tal cual
   para tener el "antes" cuantificado (luce mucho en la memoria), o vamos directos
   a reconstruir fiel? (Recomiendo lo primero: 1 ejecución corta.)
2. **Alcance del medio:** ¿el controller se defenderá solo sobre `Paseo` 30fps 4s,
   o también `Blender` y 60fps? Define cuántas tablas VBR extraer.
3. **Tabla VBR en Git:** la tabla es pequeña (≈ KB). ¿La commiteamos como
   *descriptor de media profile* versionado (cómodo, viaja por git a WSL), o la
   tratamos como artefacto externo y la movemos a mano? (Recomiendo commitearla.)
4. **Nombre de la línea:** ¿`phase45_v4` te vale como id, o prefieres un nombre
   "de marca" para la memoria (p. ej. *MF-RiskMPC*: Media-Faithful Risk-aware MPC)?
