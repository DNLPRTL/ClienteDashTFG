# Simulator vs client boundary

## Boundary statement

The Phase 4 training environment is not the DashClientModular4 player. It is an offline, trace-driven environment used to produce training samples and sanity validation for a future neural ABR candidate.

## Why the boundary exists

The boundary prevents:

- training from runtime/player logs without a data contract;
- contaminating the client with experimental learning code;
- confusing training validation with benchmark evaluation;
- using smoke scenarios as datasets;
- leaking future information from a trace replay into model features.

## Allowed in Phase 4C

```text
Markdown contracts
pseudocode
artifact layout
acceptance gates
future module names
```

## Not allowed in Phase 4C

```text
core/neural_abr/ implementation
scripts/build_neural_abr_dataset.py
scripts/train_neural_abr.py
controller IA
player integration
runtime integration
benchmark execution
training execution
model checkpoints
```

## Future code boundary

When Phase 4D begins, implementation may create an offline pipeline such as:

```text
core/neural_abr/
  trace_schema.py
  replay_env.py
  teacher_policy.py
  feature_builder.py
  dataset_builder.py
  normalizer.py
  sanity_validation.py

scripts/
  build_neural_abr_dataset.py
  validate_neural_abr_dataset.py
```

This future code must not register a client controller and must not alter existing controllers/player/runtime/media.

## Client integration boundary

Client integration is not Phase 4C and not Phase 4D. A neural controller may only be integrated in a later Phase 5 after Phase 4G explicitly marks the candidate as `ACCEPTED_FOR_PHASE5_INTEGRATION`.
