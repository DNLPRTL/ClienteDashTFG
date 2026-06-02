# Phase 5F scope and gate

## Scope

Phase 5F is fallback/error/telemetry hardening for the guarded `neural_abr_lite` controller integration.

Starting HEAD for this block:

```text
929bab4 docs(neural-abr): close Phase 5E structural smoke validation
```

This block stresses controlled failure cases and hardens fail-closed behavior. It does not improve QoE, compare controllers, rank controllers, retrain a model, add a benchmark, or create Phase 6 validation tooling.

## In scope

- Runtime model-loading safety.
- Temporary synthetic bundle fault injection.
- Runtime feature and action-mask hardening.
- Safety guard and fallback-controller failure behavior.
- Inference output failure handling.
- Diagnostic-only telemetry stability.
- Documentation of expected fallback behavior.

## Out of scope

- Benchmark scripts.
- Controller comparison or ranking.
- Training pipeline changes.
- Retraining or model selection.
- Model artifact, dataset, media, CSV, log, zip, PDF, or run-output commits.
- Default activation of `neural_abr_lite`.
- Neural diagnostic fields in `evaluation_segments.csv`.

## Closure criteria

Phase 5F may close only when:

- hardening tests pass;
- fail-closed behavior is verified for loader, feature, action, safety, inference, fallback, and telemetry faults;
- diagnostic telemetry remains stable and CSV-safe;
- no generated artifacts or model files are committed;
- `python -m unittest discover` passes;
- `python scripts\check_client_readiness.py --strict` passes;
- Ubuntu validation is completed and recorded.

Until Ubuntu validation is recorded, local hardening can be considered ready for Ubuntu confirmation but not a full cross-platform closure.
