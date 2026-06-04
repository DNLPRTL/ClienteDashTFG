# Phase 4F export validation plan

Required validation sequence:

1. Locate Phase 4E.2 source artifacts outside the repo.
2. Export the model bundle to a local-only models folder.
3. Validate bundle schema and hashes.
4. Load the bundle on CPU.
5. Run sample inference on validation/OOD samples.
6. Check action mask correctness.
7. Measure latency.
8. Generate model card, export report, validation report and defense notes.
9. Run full unit tests and readiness.
10. Confirm no controller/player/runtime/media changes.

Decision outcomes:

```text
PHASE4F_EXPORT_BUNDLE_READY_FOR_PHASE4G
PHASE4F_EXPORT_PASS_NOT_READY_FOR_PHASE4G
PHASE4F_BLOCKED_NEEDS_FIX
```
