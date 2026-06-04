# Phase 4F go/no-go gates

Phase 4F can close as ready for Phase 4G only if all gates pass:

- bundle created outside repo;
- required files present;
- manifest hashes valid;
- bundle loads on CPU;
- feature schema matches Phase 4B/4C contracts;
- normalization stats are present and train-only;
- action mask enforced;
- 100% valid actions in sample inference;
- no NaN/Inf scores;
- deterministic eval inference;
- p95 latency <= 10 ms per decision;
- full unit tests pass;
- readiness passes;
- no forbidden artifacts in repo;
- no controller/player/runtime/media changes;
- memory/defense docs present.

If any hard gate fails: `PHASE4F_BLOCKED_NEEDS_FIX`.

If basic export works but candidate is not safe enough for Phase 4G: `PHASE4F_EXPORT_PASS_NOT_READY_FOR_PHASE4G`.

If all gates pass: `PHASE4F_EXPORT_BUNDLE_READY_FOR_PHASE4G`.
