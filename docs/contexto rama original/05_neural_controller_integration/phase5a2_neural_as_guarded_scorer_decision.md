# Phase 5A2 neural as guarded scorer decision

## Selected architecture

The future controller will be a BaseController-compatible wrapper around the Phase 4 Candidate Scorer. It remains advisory/scoring until a safety guard accepts the action.

Expected future structure:

1. Controller receives feedback through the existing controller API.
2. Bundle loading happens lazily or during controller initialization.
3. Any load failure disables neural and uses fallback.
4. Runtime feature builder maps feedback into context and candidate features.
5. Bundle `feature_schema.json` is checked against the runtime builder version.
6. `normalization_stats.json` is applied from train-only stats.
7. The scorer returns one score per candidate representation.
8. Masked argmax selects `raw_action`.
9. Safety guard validates `raw_action`.
10. The controller maps the executed representation index to `feedback["rates"][index]`.
11. The controller returns/selects that existing rate in bytes per second.
12. Diagnostic telemetry records raw index, executed index, rates, inference time, safety intervention and fallback reason.

## Fail-closed behavior

The future wrapper must fail closed:

- missing bundle -> fallback;
- invalid schema -> fallback;
- load error -> fallback;
- missing required features -> fallback;
- invalid mask -> fallback;
- unsafe raw action -> safe downshift or fallback;
- runtime exception -> fallback.

## Documentation status

This is still documentation. No `core/controller/neural_abr_lite.py`, registry entry, player integration, config activation or test implementation is created in this block.
