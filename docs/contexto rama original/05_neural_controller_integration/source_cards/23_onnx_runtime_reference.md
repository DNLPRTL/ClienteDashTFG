﻿# Source card 23: ONNX Runtime reference

## Title

ONNX Runtime Python API.

## Authors

ONNX Runtime maintainers.

## Year

2026 documentation context.

## Venue/type

Technical reference only / deferred future option.

## Phase 5 triage

TECHNICAL_REFERENCE_ONLY / DEFERRED.

## Why this source matters for integration

ONNX Runtime is a possible future inference backend, but it is not required for Phase 5.

## Runtime integration pattern

An `InferenceSession` loads an ONNX or ORT model and `session.run` computes predictions with configured providers such as `CPUExecutionProvider`.

## Runtime inputs

ONNX/ORT model file and input tensors.

## Runtime action/output

Model prediction outputs from an inference session.

## Safety/fallback/action mask

A future ONNX loader would still need schema validation, local-only loading, finite output checks, action mask and fallback.

## Latency/compute/deployment assumptions

CPU inference is possible, but adding ONNX now would add conversion and dependency contracts.

## What transfers to DashClientModular4

- ONNX may be a future migration option.
- CPU provider can be considered later.

## What must not be copied

- Making ONNX a Phase 5 dependency.
- Adding `.onnx` artifacts to Git.

## Phase 5 docs affected

- `phase5a1_model_loading_matrix.md`
- `phase5a2_rejected_alternatives.md`
- `_historical/phase5_remaining_roadmap.md`

## Memory/defense usage

Use as future-work material for possible inference backend migration.

## Final decision

Defer ONNX. Phase 5 uses local PyTorch state_dict loading.
