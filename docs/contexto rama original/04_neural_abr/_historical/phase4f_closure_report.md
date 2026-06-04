# Phase 4F Closure Report

Decision: `PHASE4F_R1_REPAIR_PENDING_CROSS_PLATFORM_CONFIRMATION`

Phase 4F export/inference passed on the real Windows bundle, but Ubuntu exposed a validation-gate classification bug in the temporary unit fixture path. The R1 repair separates correctness gates from environmental/repo hygiene gates.

- Phase 4F scope: export/inference only.
- Client integration: `false`.
- Controller registered: `false`.
- Benchmark/ranking: `false`.
- SOTA or real-world claim: `false`.
- Bundle artifacts local-only outside repo: `true`.
- Default repo hygiene in pure bundle validation: `NOT_CHECKED`.
- Explicit repo hygiene flag: `--check-repo-hygiene`.

Phase 4G is allowed only after the repaired Phase 4F tests and readiness checks pass on both Windows and Ubuntu.
