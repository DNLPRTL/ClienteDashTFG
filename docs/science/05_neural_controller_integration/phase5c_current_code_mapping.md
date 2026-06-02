# Phase 5C current code mapping

## Mapping table

| Current code | Current role | Phase 5D implication |
|---|---|---|
| `core/controller/base.py` | `BaseController` exposes `setPlayerFeedback`, `calcControlAction`, `setControlAction`, `getControlAction`, `quantizeRate`, `getIdleDuration` and idle handling. | `NeuralAbrLiteController` must subclass or remain compatible with this API and return bytes-per-second rates. |
| `core/controller/contract.py` | Defines current dict-based feedback keys, units, target rates as bytes per second and quality levels as representation indices. | Runtime feature builder must consume this feedback contract and never treat target rates as bits per second. |
| `core/controller/registry.py` | Registry maps controller keys to factory specs. | Phase 5D may register `neural_abr_lite`; Phase 5C must not. |
| `core/controller/rate_based.py` | Baseline fallback returns a valid ladder rate and clamps by `max_level`. | Useful fallback candidate after `robust_mpc` and `mpc`. |
| `core/controller/mpc.py` | MPC baseline uses current rates, throughput history and fragment duration; returns a valid ladder rate. | Useful fallback candidate and source for candidate-size estimation patterns. |
| `core/controller/robust_mpc.py` | Conservative MPC baseline with prediction-error correction. | Preferred fallback controller when neural is disabled or unsafe. |
| `core/neural_abr/bundle.py` | Phase 4F bundle validation helpers, required files, manifest fields and sha256 validation. | Runtime can reuse validation helpers, then add stricter runtime schema/model checks. |
| `core/neural_abr/model.py` | `NeuralAbrLiteCandidateScorer` architecture is available and CPU-first. | Runtime should instantiate this trusted local architecture, then load a local state_dict. |
| `core/neural_abr/normalization.py` | `FeatureNormalizer` and train-only `NormalizationStats` are available. | Runtime may reuse normalization, preserving train-only stats. |
| `core/neural_abr/features.py` | Offline feature schema, flattening and forbidden input checks are available. | Runtime can reuse flattening/checks, but must build online features from controller feedback, not replay state. |
| `core/neural_abr/action_mask.py` | `validate_action_mask`, `assert_action_valid` and `lowest_valid_action` are available. | Runtime should reuse these primitives for mask and selected-action validation. |
| `core/neural_abr/content_ladder.py` | Offline content ladder and size-estimation helpers exist. | Runtime may borrow formulas, but should not require an offline `ContentLadder`. |
| `core/neural_abr/inference.py` | Phase 4 offline inference exists, including validation-sample loading and `_torch_load_cpu`. | Do not blindly reuse for runtime because `_torch_load_cpu` falls back to unsafe `weights_only=False`. Runtime must fail closed instead. |
| `core/client_config.py` | Generic `controller.params` pass through to registry factories. | Phase 5D can receive neural params through existing config parsing without changing config code. |
| `core/dataset_schema.py` | Segment telemetry header is built from initial feedback keys plus fixed policy/stall columns. Evaluation header is static. | Prefer dynamic feedback-key telemetry via `augment_feedback`; modify schema only if static diagnostic columns are approved. |
| `core/runtime_feedback.py` | Builds current ordered controller feedback from player state. | Runtime feature builder should map these keys directly. |
| `player.py` | Calls `controller.augment_feedback` before header and row creation; updates pending rows after `calcControlAction`. | Post-decision neural telemetry may require a minimal optional hook in Phase 5D. |
| `main.py` | Creates controller by registry key and params, then passes it to `Player`. | Phase 5D registry entry should make `neural_abr_lite` config-driven without changing `main.py`. |
| `config/client.example.yaml` | Default controller is a disabled/debug classical controller; params pass through generically. | Phase 5D may add only a disabled documented neural example if approved. |

## Security note

`core/neural_abr/inference.py` is offline Phase 4 code. Its `_torch_load_cpu` tries `weights_only=True`, then plain `torch.load`, then `weights_only=False`. Phase 5D runtime code must not use that unsafe fallback. Runtime loading must call:

```python
torch.load(path, map_location="cpu", weights_only=True)
```

If this is unsupported or fails, runtime must disable neural and fallback.
