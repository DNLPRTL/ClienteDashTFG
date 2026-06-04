# Phase 5B bundle loading contract

## Purpose

The future controller loads a Phase 4F NeuralABR-Lite bundle from a local directory configured outside the repository.

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

## Validation

The loader must validate:

- manifest schema;
- required file presence;
- sha256 hashes;
- model family;
- teacher;
- action space;
- feature schema version;
- normalization schema version;
- ladder schema version;
- inference contract version;
- fallback policy version.

Expected values include:

- model family: `NeuralABR-Lite Candidate Scorer`;
- teacher: `robust_mpc` unless explicitly documented otherwise;
- action space: `representation_index`;
- training method: behavior cloning / imitation learning.

## Failure behavior

Missing or invalid bundle means:

```text
neural disabled + fallback
```

No remote bundle loading is allowed. Bundle artifacts remain outside the repository.
