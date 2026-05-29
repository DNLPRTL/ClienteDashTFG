# Phase 4G bundle acceptance record

## Accepted artifact

Accepted artifact family:

```text
NeuralABR-Lite Phase 4F local bundle
```

Expected local root:

```text
C:\Users\danie\Documents\TFG\_models\phase4_AI\neural_abr_lite\phase4F
```

The exact timestamped bundle directory must be preserved locally and referenced in future Phase 5 runbooks.

## Required bundle contents

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

## Acceptance basis

The bundle is accepted because:

- required files are present;
- hashes are validated;
- the model loads on CPU;
- inference applies the action mask;
- selected actions are valid MPD representation indices;
- inference is deterministic in smoke testing;
- no NaN/Inf scores are observed;
- the fallback policy is documented;
- the bundle is outside the repository;
- Windows and Ubuntu validations pass.

## Constraints carried to Phase 5

Phase 5 integration must preserve:

- CPU-first loading/inference;
- bundle schema compatibility;
- strict feature schema checks;
- train-only normalization stats;
- action mask enforcement;
- fallback controller path;
- diagnostic telemetry without benchmark contamination;
- no runtime dependency on local training artifacts;
- no model/checkpoint artifacts committed to Git.
