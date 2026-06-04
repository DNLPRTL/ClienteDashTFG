# Phase 5F fault injection plan

## Boundary

All Phase 5F fault injection is diagnostic-only structural hardening. It is not a benchmark, not controller ranking, and not Phase 6 validation.

Temporary synthetic bundles may be created only inside test temp directories. No model artifacts, CSVs, logs, run outputs, datasets, zips, PDFs, or media files may be committed.

## Bundle faults

Expected behavior: controller creation and `calcControlAction()` do not raise; neural path fails closed; classical fallback or emergency lowest valid representation is selected; `neural_fallback_reason` is stable and populated.

- Missing `bundle_dir`.
- Non-existent `bundle_dir`.
- Missing `bundle_manifest.json`.
- Corrupted `bundle_manifest.json`.
- Missing `model_card.json`.
- Malformed `model_card.json`.
- Missing `feature_schema.json`.
- Wrong feature schema version.
- Missing `normalization_stats.json`.
- Missing `model_state.pt`.
- Manifest/file hash mismatch.
- Model architecture/config mismatch.

## Torch/load faults

Expected behavior: runtime stays CPU-local and safe-load-only; there is no unsafe retry; fallback reason is stable.

- `torch` unavailable.
- `torch.load(..., map_location="cpu", weights_only=True)` raises `TypeError`.
- `torch.load(..., map_location="cpu", weights_only=True)` raises `RuntimeError`.
- Static runtime code contains no `weights_only=False`, `torch.hub`, URL loading, `urlopen`, or `requests` model-loading path.

## Feature faults

Expected behavior: feature construction fails closed or clamps according to the runtime contract; no future or forbidden fields enter model features.

- Missing `rates`.
- Empty `rates`.
- Zero, negative, non-finite, or non-numeric rates.
- `max_level < 0`.
- `max_level` beyond the ladder.
- Missing `level`.
- Out-of-bounds `level`.
- Missing or non-numeric `queued_time`.
- Zero `last_download_time`.
- Missing `last_fragment_size`.
- Missing `fragment_duration`.
- Single representation ladder.
- Forbidden model-input fields.

## Mask/action faults

Expected behavior: invalid action masks and scorer actions do not execute unsafe neural actions.

- All-false mask.
- Selected action outside the mask.
- Selected action outside the ladder.
- Action-mask valid count remains recorded.
- `neural_invalid_action_detected` is set when the scorer selects an invalid action.

## Safety faults

Expected behavior: safe raw actions pass, unsafe raw actions downshift, missing safety signals fall back, and non-finite estimated download times do not execute.

- Safe raw action.
- Unsafe raw action with feasible lower action.
- Unsafe raw action with no feasible lower action.
- Missing throughput or buffer signals.
- Non-finite estimated download time.

## Fallback faults

Expected behavior: classical fallback errors do not escape and the controller executes the lowest valid representation as an emergency path.

- Preferred fallback controller raises.
- Every fallback controller raises.
- Fallback target quantizes outside the valid mask.

## Telemetry faults

Expected behavior: diagnostics are present only in `segment_telemetry.csv`, never in `evaluation_segments.csv`, and values are CSV-safe.

- Required `feedback_neural_*` header fields missing.
- Hook raises or returns non-dict telemetry.
- Unknown fallback reason text.
- Embedded newline in diagnostic string.
- Existing non-neural controller without telemetry hook.
- Benchmark/ranking/improvement fields accidentally added.
