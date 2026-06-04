# Phase 5C offline/runtime boundary spec

## Boundary

Phase 4 code produced an offline/export bundle and offline inference smoke. Phase 5D runtime code will integrate the accepted bundle into the client controller API. These are different trust and data contexts.

## Runtime may reuse stable primitives

Phase 5D may reuse:

- `core/neural_abr/model.py` model class;
- `core/neural_abr/normalization.py` train-only normalizer;
- `core/neural_abr/bundle.py` metadata and sha256 validation helpers;
- `core/neural_abr/features.py` flattening and forbidden-key checks;
- `core/neural_abr/action_mask.py` action mask validation.

## Runtime must not reuse unsafe or development-only behavior

Phase 5D must not reuse:

- `torch.load(..., weights_only=False)`;
- plain `torch.load(path, map_location="cpu")` compatibility fallback;
- offline validation samples;
- dataset split labels;
- trace ids;
- source dataset names;
- teacher actions or teacher rewards;
- training reports as model inputs;
- benchmark outputs as model inputs;
- dry-run legacy labels.

## Fail-closed rule

Runtime must fail closed to fallback for:

- missing bundle;
- invalid manifest;
- hash mismatch;
- schema mismatch;
- unsupported safe PyTorch loading;
- model load failure;
- feature build failure;
- invalid action mask;
- non-finite score;
- unsafe selected action;
- inference timeout;
- runtime exception.

All telemetry is diagnostic-only and not benchmark evidence.
