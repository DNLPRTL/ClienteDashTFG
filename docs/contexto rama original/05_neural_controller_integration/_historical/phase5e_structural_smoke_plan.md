# Phase 5E structural smoke plan

## Boundary

Phase 5E validates structure only. It checks that `neural_abr_lite` can be selected through the existing config/CLI path, fails closed when needed, writes diagnostic telemetry to `segment_telemetry.csv`, and keeps `evaluation_segments.csv` free of neural diagnostic fields.

None of the checks below are Phase 6 benchmark, ranking, winner selection, or improvement evidence.

## Level 1: unit and integration tests with temporary bundle

Purpose:

- Confirm registry import and controller construction.
- Confirm no-bundle fallback behavior.
- Confirm safe runtime loading uses local CPU `weights_only=True` behavior.
- Confirm feature builder, action mask, safety guard, fallback, diagnostics, and player telemetry hook behavior.
- Confirm fake-engine client run with a synthetic temporary bundle produces canonical artifacts and deletes temporary outputs when the test ends.

Commands:

```text
python -m unittest tests.test_neural_abr_registry
python -m unittest tests.test_neural_abr_model_loading_runtime
python -m unittest tests.test_neural_abr_runtime_features
python -m unittest tests.test_neural_abr_safety_fallback
python -m unittest tests.test_neural_abr_controller
python -m unittest tests.test_neural_abr_fake_smoke
python -m unittest tests.test_neural_abr_player_telemetry_hook
```

Interpretation:

- Pass means the Phase 5D implementation is still structurally coherent.
- Fail means Phase 5E must stop and the failure must be handled as implementation hardening, not benchmark analysis.

## Level 2: fake-engine smoke with real local Phase 4F bundle

Purpose:

- Exercise `main.py --config` with `controller.name: neural_abr_lite`.
- Load a real local Phase 4F bundle outside the repository.
- Run the fake media engine against a local or VM-served MPD.
- Inspect `run_manifest.json`, `config.resolved.json`, `environment.json`, `run.log`, `segment_telemetry.csv`, and `evaluation_segments.csv`.

Inputs:

- A real Phase 4F bundle path supplied by the user.
- A small local or VM-served DASH MPD.
- An output root outside the repository.

Interpretation:

- Pass means the real-bundle client run path is structurally usable.
- Fallback can still be an acceptable structural result when diagnostics show expected fail-closed behavior.
- This level does not compare controllers or score quality.

## Level 3: optional Ubuntu GStreamer structural smoke

Purpose:

- Check that the same controller/config path can be used with `media_engine.name: gst` on an Ubuntu environment with GStreamer.
- Use headless/fakesink mode where supported.
- Confirm canonical artifacts and diagnostic telemetry are still produced.

Interpretation:

- This is integration/demo validation only.
- Network bridge behavior, GStreamer timing, decoder behavior, and fakesink operation are not benchmark-grade evidence.

## Global gates

All levels must preserve:

- No controller comparison.
- No ranking, winner, p-value, improvement percentage, or SOTA claim.
- No retraining.
- No model or media artifacts in Git.
- No generated run directory committed.
- `evaluation_segments.csv` remains uncontaminated by neural diagnostic fields.
