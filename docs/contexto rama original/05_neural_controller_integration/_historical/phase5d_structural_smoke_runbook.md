# Phase 5D structural smoke runbook

## Boundary

Phase 5D fake smoke is diagnostic-only structural integration. It checks that the guarded controller can load or fail closed, choose only current ladder rates, write diagnostic telemetry, and finish with the fake engine.

It is not a benchmark, not a ranking, not a baseline comparison, and not a real playback validation.

## Unit tests

Run the focused tests:

```text
python -m unittest tests.test_neural_abr_registry
python -m unittest tests.test_neural_abr_model_loading_runtime
python -m unittest tests.test_neural_abr_runtime_features
python -m unittest tests.test_neural_abr_safety_fallback
python -m unittest tests.test_neural_abr_controller
python -m unittest tests.test_neural_abr_player_telemetry_hook
python -m unittest tests.test_neural_abr_fake_smoke
```

Then run:

```text
python -m unittest discover
python scripts/check_client_readiness.py --strict
```

## Local bundle configuration

Keep the Phase 4F bundle outside the repository. The directory must contain:

```text
bundle_manifest.json
model_card.json
feature_schema.json
normalization_stats.json
ladder_schema.json
inference_contract.json
fallback_policy.json
model_state.pt
```

Example config fragment:

```yaml
controller:
  name: "neural_abr_lite"
  params:
    bundle_dir: "/absolute/path/outside/repo/neural_abr_lite_bundle"
    enabled: true
    fallback_controller: "robust_mpc"
    diagnostic_telemetry: true
    fail_closed: true
```

Do not put the bundle, `.pt` files, logs, CSVs, or run outputs in Git.

## Fake-engine structural smoke

Use a local MPD and fake media engine:

```text
python main.py --config path\to\client.neural_abr_lite.fake.yaml
```

The config should use:

```yaml
media_engine:
  name: "fake"
controller:
  name: "neural_abr_lite"
playback:
  headless: true
analysis:
  enabled: false
```

## Inspect outputs

After the smoke, inspect the run directory:

- `run_manifest.json`: status should be `completed`, controller name should be `neural_abr_lite`.
- `config.resolved.json`: confirms the resolved local bundle path and fake engine config.
- `environment.json`: records environment diagnostics.
- `segment_telemetry.csv`: may include `feedback_neural_*` diagnostic columns.
- `evaluation_segments.csv`: must not include neural diagnostic columns.

There should be no legacy `dataset.csv` or `dataset_training.csv`.

## Later phases

Real GStreamer playback belongs to Phase 5E structural integration smoke.

Formal comparative validation, trace selection, metrics, statistical handling, and any controller ranking belong to Phase 6.
