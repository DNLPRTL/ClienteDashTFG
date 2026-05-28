# Phase 4C environment acceptance tests

## Phase 4C documentation acceptance

Phase 4C is accepted when the following documents exist and are artifact-clean:

```text
phase4c_training_environment_report.md
training_environment_spec.md
simulator_vs_client_boundary.md
trace_format_contract.md
trace_conversion_contract.md
trace_manifest_contract.md
network_regime_contract.md
content_ladder_contract.md
replay_engine_contract.md
teacher_replay_environment_contract.md
sample_generation_contract.md
dataset_builder_contract.md
normalization_pipeline_contract.md
simulator_determinism_contract.md
leakage_audit_protocol.md
offline_validation_protocol.md
synthetic_sanity_trace_contract.md
phase4c_artifact_layout.md
defendibility_acceptance_gates.md
implementation_go_no_go_policy.md
phase4_remaining_roadmap.md
phase4c_to_phase4d_handoff.md
```

## Future Phase 4D implementation acceptance

Phase 4D may only implement offline pipeline components if Phase 4C validates.

Implementation acceptance will require tests for:

```text
trace schema parsing
unit conversion
deterministic replay
action mask construction
feature availability audit
teacher label generation
sample manifest generation
normalization train-only
artifact location outside repo
```

## Future Phase 4E model acceptance

Phase 4E is where a trained model can become an `OFFLINE_CANDIDATE`.

Required future checks:

```text
valid actions = 100%
NaN/Inf scores = 0
invalid labels = 0
leakage audit = PASS
non-collapse = PASS
CPU latency = PASS
validation sanity baseline = PASS
OOD diagnostic report = PRESENT
reproducibility rerun = PASS
```
