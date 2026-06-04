# Phase 4C to Phase 4D handoff

## Context for Phase 4D

Phase 4D may implement the offline neural ABR pipeline specified in Phase 4C.

## Allowed implementation target

```text
Offline pipeline only.
No client integration.
```

## Candidate future modules

```text
core/neural_abr/__init__.py
core/neural_abr/trace_schema.py
core/neural_abr/trace_loader.py
core/neural_abr/replay_env.py
core/neural_abr/feature_builder.py
core/neural_abr/action_mask.py
core/neural_abr/teacher_policy.py
core/neural_abr/dataset_builder.py
core/neural_abr/normalizer.py
core/neural_abr/model.py
core/neural_abr/sanity_validation.py
```

## Candidate future scripts

```text
scripts/build_neural_abr_dataset.py
scripts/validate_neural_abr_dataset.py
scripts/train_neural_abr.py
scripts/validate_neural_abr_offline.py
```

## Required future tests

```text
tests/test_neural_abr_trace_schema.py
tests/test_neural_abr_action_mask.py
tests/test_neural_abr_feature_builder.py
tests/test_neural_abr_replay_env.py
tests/test_neural_abr_teacher_policy.py
tests/test_neural_abr_dataset_builder.py
tests/test_neural_abr_normalizer.py
tests/test_neural_abr_sanity_validation.py
```

## Codex prompt gate

A Codex implementation prompt is allowed only after Phase 4C validation. It must implement Phase 4D offline pipeline components and must explicitly forbid controller/player/runtime/media integration.
