# Phase 5G safety and fallback closure

## Fail-closed guarantees

`neural_abr_lite` is integrated as a guarded controller. Its neural path is allowed to influence playback only after local bundle validation, runtime feature construction, action-mask validation, inference output validation, and safety-guard validation succeed.

If the guarded path fails, the controller falls back to a classical controller path or emergency lowest valid representation.

## Covered fallback reasons

Phase 5F covered stable fallback reasons including:

- `neural_disabled`
- `missing_bundle_dir`
- `bundle_load_failed`
- `torch_unavailable`
- `safe_torch_load_unavailable`
- `bundle_schema_invalid`
- `bundle_hash_invalid`
- `feature_build_failed`
- `missing_required_feature`
- `action_mask_invalid`
- `all_actions_invalid`
- `inference_failed`
- `inference_timeout`
- `non_finite_scores`
- `selected_masked_action`
- `safety_guard_rejected`
- `fallback_controller_failed`
- `emergency_lowest_representation`
- `single_representation`
- `success_neural`

`fallback_reason` values are sanitized to stable enum-like labels before telemetry output. Unknown exception-like text is normalized to `inference_failed`.

## Phase 5F tests added

- `tests/test_neural_abr_fault_injection.py`
- `tests/test_neural_abr_hardening.py`
- `tests/test_neural_abr_telemetry_hardening.py`

These tests cover bundle/load faults, torch safe-load faults, runtime feature failures, action-mask failures, invalid scorer actions, non-finite and mismatched scorer outputs, inference exceptions, timeout handling, safety guard failure, fallback-controller failure, and telemetry hardening.

## Runtime loading safety

Runtime model loading uses:

```text
torch.load(..., map_location="cpu", weights_only=True)
```

Runtime code never uses `weights_only=False`. Static checks also recorded no `torch.hub` usage and no URL/request model-loading path.

## Inference output safety

Non-finite scores fail closed. Empty or action-mask-length-mismatched scorer outputs fail closed. Selected actions outside the ladder or outside the current action mask fail closed.

## Safety guard safety

The safety guard preserves safe raw actions, downshifts unsafe actions when a feasible lower representation exists, and requests fallback when required safety signals are missing or invalid.

Non-finite estimated download-time values are rejected and converted to fallback rather than executed.

## Boundary

This closure is integration hardening only. It is not benchmark evidence and does not claim controller superiority.
