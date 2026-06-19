# Decisión — MPC Prudente: diagnóstico estratificado y over-conservadurismo

| Campo | Valor |
|---|---|
| Fecha | 2026-06-19 |
| Autor | Claude (Claude Code) |
| Rama | `rebuild/phase3-from-phase2` |
| Estado | Diagnóstico corregido y analizado. Decisión pendiente: afinar riesgo vs aceptar e ir a Phase 6. |

## Qué pasó (y por qué el primer diagnóstico engañaba)

El diagnóstico de 32 ventanas dio `qoe=-52`, `rebuffer=12026 s`, con prudente y
robust **idénticos**. No era bug del controller: el corpus de validación incluye
trazas **impracticables** (medias de 6–160 kbps) y con **outages** (throughput→0)
donde ningún ABR puede evitar rebuffer. Esas pocas trazas ahogaban la señal.

Corrección (como Phase 6): se añadió **suelo de servibilidad** (media ≥ 600 kbps)
y **estratificación por bucket de capacidad/variabilidad** a
`core/mpc_prudente/evaluation.py`.

## Resultado honesto (27 ventanas servibles)

| controller | QoE | rebuffer(s) | bitrate(kbps) |
|---|---:|---:|---:|
| robust_mpc | 2.056 | 22.6 | 2309 |
| neural_mpc viejo | 2.026 | 28.3 | 2325 |
| mpc_prudente | 2.007 | 22.6 | 2238 |
| bola | 1.445 | 33.6 | 1752 |

Delta prudente vs robust por capacidad: `1_2mbps −0.001`, `2_5mbps −0.069`,
`5_20mbps −0.097`, `gt_20mbps −0.100`. Rebuffer delta = 0.000 en todos.

## Lectura sin adornos

- **Seguro**: prudente iguala el rebuffer de robust_mpc (22.6, el mejor) y MEJORA
  el del neural_mpc viejo (28.3). 0 fallback, 0 invalid.
- **Pero no gana**: QoE −0.05 vs robust_mpc, por **over-conservadurismo en ALTA
  capacidad** (el déficit crece con la capacidad: hasta −0.10 en >20 Mbps). Ahí no
  hay riesgo y aun así no sube al máximo bitrate, dejando QoE sobre la mesa.
- Causa: el objetivo CVaR pondera los escenarios malos (q10/q25) **incluso cuando
  el buffer está lleno y la capacidad sobra**, así que planifica por debajo de
  robust_mpc (que usa una sola estimación de throughput).
- En estas trazas de validación no hay un caso `real_006` (over-agresión que
  cause stall), así que la prudencia no tiene rebuffer que ahorrar; solo cuesta
  bitrate. Su ventaja debería verse en trazas más duras (eval/Phase 6).

## Decisión propuesta

**Una iteración de afinado del riesgo** (barata, sin reentrenar el predictor):
hacer que la aversión al riesgo sea **dependiente de la capacidad/seguridad** —
neutral u optimista cuando el buffer está alto Y el suelo predictivo es alto
(empujar bitrate), manteniendo la prudencia solo cuando la cola predictiva avisa
de riesgo real. Objetivo: recuperar la QoE de alta capacidad sin perder la
seguridad de rebuffer. Luego re-diagnosticar.

Alternativa: aceptar (prudente es seguro y competitivo, −0.05 vs robust con
rebuffer igual) e ir a Phase 6 sobre eval, donde puede aparecer el régimen duro.

Recomendación: afinar primero (1 iteración), porque el déficit está localizado y
es claramente corregible; mejora el resultado defendible.
