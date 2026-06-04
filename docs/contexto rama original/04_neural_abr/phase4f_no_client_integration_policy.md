# Phase 4F no-client-integration policy

Phase 4F must not integrate NeuralABR-Lite into DashClientModular4 runtime.

Blocked paths:

```text
controllers/
player/
runtime/
media/
main.py
controller registry
```

Allowed scope:

```text
core/neural_abr/export.py
core/neural_abr/inference.py
core/neural_abr/bundle.py
scripts/export_neural_abr_model.py
scripts/validate_neural_abr_bundle.py
scripts/smoke_neural_abr_inference.py
tests/test_neural_abr_bundle.py
tests/test_neural_abr_inference.py
docs/science/04_neural_abr/phase4f_*.md
```

Phase 5 will decide client integration only after Phase 4G accepts the export bundle.
