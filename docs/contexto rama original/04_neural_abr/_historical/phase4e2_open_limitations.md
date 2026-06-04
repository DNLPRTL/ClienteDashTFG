# Phase 4E.2 Open Limitations

- Phase 4E.2 is offline diagnostic work only.
- No formal benchmark, ranking, SOTA claim, or real-world claim is made.
- OOD traces are diagnostic-only and must not be tuned on.
- NeuralABR-Lite is not integrated into the client.
- Robustness still depends on corpus breadth, leakage checks, and future Phase 4F export/inference contracts.
- R2 repaired a cross-platform unit-test issue: environmental repo hygiene gates are not treated as pure-assessor hard failures unless explicitly checked or supplied.
- Phase 4F remains paused until Ubuntu validation passes after the R2 repair.
- dataset family hsdpa_norway_mmsys2013 is below 5% of trace count
- regime bucket low_variable is below 5% of trace count
- regime bucket very_high_variable is below 5% of trace count
