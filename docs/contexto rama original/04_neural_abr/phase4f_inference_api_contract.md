# Phase 4F inference API contract

The inference contract is offline-only in Phase 4F.

Input:

- online-observable context features from Phase 4B/4C;
- candidate representation features for each valid MPD representation;
- action mask indicating valid representation indices;
- normalization statistics fitted on train only.

Output:

- score per candidate representation;
- selected `representation_index` after applying action mask;
- optional diagnostic fields: latency_ms, fallback_used, invalid_input_reason.

Hard rules:

- no bitrate outside the MPD ladder;
- no future information;
- no test/OOD tuning;
- no benchmark/ranking;
- no client runtime integration;
- inference must be CPU-first and deterministic in eval mode.

Fallback policy:

If the bundle is missing, invalid, too slow, returns NaN/Inf, has schema mismatch or fails action masking, the future Phase 5 controller must fallback to a classical safe controller. Phase 4F only documents and validates this behavior offline.
