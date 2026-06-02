# Phase 5C action mask, safety and fallback spec

## Action mask

Phase 5D must build an action mask for the current feedback ladder:

- length = `len(feedback["rates"])`;
- valid index range = `0..feedback["max_level"]`;
- rates beyond `max_level` are invalid;
- invalid rates or non-positive rates are invalid;
- all invalid -> fallback.

The mask must be validated before inference. Selected actions must be validated after inference.

## Inference rule

- CPU model scores candidate representations.
- Invalid candidates must not be actionable.
- Selection considers only valid mask positions.
- `raw_action` must be finite and valid.
- NaN/Inf score -> fallback.
- selected masked action -> fallback.

## Safety guard

The safety guard runs after `raw_action`:

- preserve `raw_action` if safe;
- if unsafe, downshift to the highest lower feasible action;
- if no feasible action exists, use emergency lowest valid representation or fallback chain;
- record `neural_safety_intervened`.

## Initial feasibility rule

When measured throughput and fragment duration are available:

```text
conservative_throughput_Bps = conservative factor or recent minimum throughput
candidate_size_bytes = explicit size if known, otherwise rate_Bps * fragment_duration_s
estimated_download_time = candidate_size_bytes / conservative_throughput_Bps
safe if estimated_download_time <= max(buffer_s - safety_margin_s, fragment_duration_s)
```

If required signals are absent, use fallback rather than guessing.

## Fallback chain

Preferred order:

```text
1. robust_mpc
2. mpc
3. rate_based
4. bba
5. min_rate
6. lowest valid representation
```

If a named fallback controller cannot be constructed or cannot return a valid ladder rate, continue to the next fallback. The lowest valid representation is the final emergency.

## Fallback reasons

Phase 5D must enumerate fallback reasons:

```text
BUNDLE_MISSING
MANIFEST_INVALID
HASH_MISMATCH
SCHEMA_MISMATCH
MODEL_LOAD_FAILED
PYTORCH_UNAVAILABLE
SAFE_LOAD_UNSUPPORTED
FEATURE_BUILD_FAILED
REQUIRED_FEATURE_MISSING
ACTION_MASK_INVALID
ALL_ACTIONS_INVALID
NON_FINITE_SCORE
SELECTED_ACTION_MASKED
SAFETY_REJECTED
INFERENCE_TIMEOUT
RUNTIME_EXCEPTION
FALLBACK_CONTROLLER_UNAVAILABLE
```

Fallback is diagnostic-only and not benchmark evidence.
