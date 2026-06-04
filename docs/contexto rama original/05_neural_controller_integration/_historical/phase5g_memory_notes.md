# Phase 5G memory notes

These notes are reusable material for the TFG memory. They summarize Phase 5 as integration validation, not comparative evaluation.

## Design chapter

NeuralABR-Lite is integrated as a guarded neural scorer controller. The controller consumes online playback feedback, builds pre-decision runtime features, scores candidate MPD representations, applies an action mask, and passes the selected action through a runtime safety guard before returning an existing ladder rate.

The design separates:

- MPD ladder/rates;
- runtime feature construction;
- model loading;
- inference;
- action-mask safety;
- fallback;
- diagnostic telemetry.

## Implementation chapter

Key implementation elements:

- Safe loader for local-only bundle validation.
- CPU-first PyTorch runtime loading.
- `torch.load(..., map_location="cpu", weights_only=True)`.
- Runtime feature builder using only pre-decision feedback and completed-download history.
- Action mask over current valid `representation_index` values.
- Safety guard that preserves safe actions, downshifts unsafe actions, or requests fallback.
- Classical fallback and emergency lowest valid representation.
- Player telemetry hook that copies diagnostic fields only into existing segment telemetry columns.

## Evaluation chapter

Phase 5 validates integration structure only. It records unit tests, structural smokes, readiness checks, and diagnostic artifact inspection. It does not compare controllers or report QoE superiority.

The final post-hardening real-bundle regression smoke for HEAD `72681b6` is pending user execution in this Phase 5G documentation input.

## Limitations

- No benchmark or comparative claim in Phase 5.
- No claim that `neural_abr_lite` improves QoE.
- Bundle is local-only and remains outside Git.
- Runtime uses CPU PyTorch.
- No online learning.
- No ONNX path.
- No remote model loading.

## Annex material

Useful annex entries:

- validation command list and outcomes;
- focused neural test names;
- readiness strict result;
- static unsafe-loading checks;
- run artifacts kept outside the repository;
- distinction between `segment_telemetry.csv` diagnostic columns and `evaluation_segments.csv` compact evaluation rows.
