# Verificacion de Controllers Clasicos

Esta fase no reescribe la teoria desde PDFs brutos. Usa la documentacion local
ya cerrada en Phase 2 y la conecta con ejecuciones reales del cliente.

## `rate_based`

- Idea: selecciona la mayor representacion por debajo de un throughput medido y
  protegido por safety factor.
- Codigo: `core/controller/rate_based.py`.
- Tests: `tests/test_rate_based_controller.py`.
- Spec: `docs/contexto rama original/01_baselines/rate_based/implementation_spec.md`.
- Probe: comprueba throughput, safety factor y subida conservadora.

## `bba`

- Idea: usa el buffer como senal principal mediante reservoir y cushion.
- Codigo: `core/controller/bba.py`.
- Tests: `tests/test_bba_controller.py`.
- Spec: `docs/contexto rama original/01_baselines/bba/implementation_spec.md`.
- Probe: situa el buffer dentro del cushion y espera una calidad intermedia.

## `bola`

- Idea: calcula una puntuacion BOLA-basic por representacion.
- Codigo: `core/controller/bola.py`.
- Tests: `tests/test_bola_controller.py`.
- Spec: `docs/contexto rama original/01_baselines/bola/implementation_spec.md`.
- Probe: comprueba que el nivel elegido coincide con el mejor score.

## `mpc`

- Idea: enumera secuencias, simula buffer y devuelve la primera accion de la
  mejor secuencia.
- Codigo: `core/controller/mpc.py`.
- Tests: `tests/test_mpc_controller.py`.
- Spec: `docs/contexto rama original/01_baselines/mpc/implementation_spec.md`.
- Probe: comprueba prediccion armonica, horizonte y objetivo interno.

## `robust_mpc`

- Idea: usa MPC con prediccion conservadora corregida por error reciente.
- Codigo: `core/controller/robust_mpc.py`.
- Tests: `tests/test_robust_mpc_controller.py`.
- Spec: `docs/contexto rama original/01_baselines/robust_mpc/implementation_spec.md`.
- Probe: comprueba que la prediccion robusta no supera la prediccion base y que
  no usa IA/RL.

## Lectura correcta de la evidencia

Si un controller elige calidad alta en una red local rapida, eso no significa
que gane. Solo significa que, con las senales observadas en ese run, devolvio
una accion valida y coherente con su regla.

