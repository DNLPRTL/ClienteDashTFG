# Phase 6A0 No Benchmark Yet

Status: binding non-results boundary for this documentation block.

## Explicit Statement

No benchmark has been executed in Phase 6A0.

This directory contains protocol evidence only. It does not contain performance evidence.

## Forbidden Interpretations

- No final ranking exists.
- No controller winner exists.
- No plot or result table from real runs exists.
- No `neural_abr_lite` QoE improvement claim exists.
- No Phase 6A0 document authorizes retraining NeuralABR-Lite.
- No Phase 6A0 document changes `qoe_linear_v1` or `reward_n`.

## Smoke And Dry-Run Boundary

Smoke is not benchmark.

Dry-run legacy is not benchmark.

Readiness checks, unit tests, structural smokes, documentation checks and legacy dry-run machinery can prove that code paths are importable or structurally consistent. They do not prove comparative QoE, do not rank controllers and do not establish a winner.

## Evidence Boundary

Generated docs are protocol evidence only. They support future decisions about:

- eligible traces;
- dataset cards;
- leakage gates;
- QoE reporting;
- evidence package contents;
- threats to validity.

They are not:

- benchmark artifacts;
- run logs;
- plots;
- rankings;
- claims of improvement;
- final evaluation tables.

## Future Authorization Requirement

Any future Phase 6 benchmark must first have a finalized protocol, eligible trace manifest, gates, command plan, evidence package contract and no-overlap audit. Until then, `docs/science/06_validation/` is documentation/protocol intake only.
