# Phase 5G controller status summary

## Controller identity

- Controller key: `neural_abr_lite`.
- Role: guarded neural scorer controller.
- Model source: Phase 4 NeuralABR-Lite Candidate Scorer.
- Action space: `representation_index`.
- Controller return unit: bytes per second from the current MPD ladder.

## Bundle status

The bundle is optional and local-only. A valid real bundle must live outside the repository and contain the Phase 4F runtime files, including `model_state.pt`, metadata JSON files, normalization stats, and manifest hashes.

No model bundle is committed to Git.

## No-bundle behavior

When no bundle is configured, controller creation does not crash. Runtime decisions fail closed through the fallback path and return a valid current ladder rate when a valid ladder is available.

## Real-bundle behavior

When a valid local bundle is configured, the controller loads the bundle, validates metadata and hashes, constructs runtime features, builds an action mask, performs CPU inference, applies the safety guard, and returns a safe ladder rate.

If any part of loading, feature construction, inference, action selection, safety, or fallback fails, the controller fails closed.

## Safety and fallback

The controller uses:

- mandatory action mask;
- runtime safety guard;
- classical fallback controller path;
- emergency lowest valid representation path.

## Telemetry

Neural telemetry is diagnostic-only. `segment_telemetry.csv` may contain `feedback_neural_*` fields. `evaluation_segments.csv` must not contain neural diagnostic fields.

## Configuration status

The repository includes a disabled/commented example for `neural_abr_lite`. Default controller behavior was not changed.

## Benchmark status

No benchmark, ranking, comparison, improvement claim, retraining, or real-world superiority claim is part of Phase 5.
