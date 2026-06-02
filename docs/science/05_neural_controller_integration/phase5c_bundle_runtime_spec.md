# Phase 5C bundle runtime spec

## Bundle source

Runtime bundle path comes from future controller params:

```text
controller.params.bundle_dir
```

The bundle must be local-only and outside the repository.

## Required files

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

## Required validation

Before model load, Phase 5D must validate:

- manifest `schema_version`;
- required file presence;
- sha256 hashes;
- `model_family`;
- `training_method`;
- `teacher`;
- `action_space`;
- feature schema version and names;
- normalization schema version and train-only fit;
- model config dimensions;
- model config family/type;
- inference contract compatibility;
- fallback policy compatibility.

Expected metadata:

```text
model_family = NeuralABR-Lite Candidate Scorer
training_method = behavior_cloning
teacher = robust_mpc
action_space = representation_index
```

## Safe load

Runtime must instantiate architecture from trusted local code and load the local state dict with:

```python
torch.load(model_state_path, map_location="cpu", weights_only=True)
```

If `TypeError` occurs because `weights_only` is unsupported, runtime must fail closed and fallback.

## Forbidden loading behavior

Runtime must not use:

- `weights_only=False`;
- plain `torch.load(path, map_location="cpu")` fallback;
- `torch.hub`;
- remote URLs;
- automatic downloads;
- arbitrary pickle model objects.

## Missing or invalid bundle

Missing or invalid bundle means:

```text
neural disabled
fallback used
neural_fallback_reason recorded
```

The diagnostic record is not benchmark output.
