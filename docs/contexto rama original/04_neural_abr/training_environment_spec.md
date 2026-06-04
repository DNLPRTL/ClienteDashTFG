# Training environment specification

## Goal

Define a deterministic offline environment for generating supervised training samples for NeuralABR-Lite without using the production player runtime as a training loop.

The environment exists to answer one question:

```text
Given a trace, a representation ladder, current buffer state, recent observations, and a candidate representation, what context/candidate features and teacher action should be produced without leakage?
```

## Environment type

```text
type: offline trace-driven replay environment
purpose: dataset generation and sanity validation
not purpose: benchmark, final ranking, real-world claim
```

## Inputs

```text
trace_manifest.json
trace files
content ladder description
segment/chunk size table when available
teacher policy configuration
reward version qoe_linear_v1 / reward_n
split manifest
normalization manifest
seed manifest
```

## Outputs

```text
sample_manifest.json
samples_train.*
samples_validation.*
samples_ood_diagnostic.*
teacher_label_report.json
leakage_audit_report.json
normalization_stats.json
sanity_validation_report.json
```

The exact binary/table format will be chosen in Phase 4D, but Phase 4C requires that every output have a manifest and that generated artifacts stay outside the repository.

## Environment loop, conceptual

For each trace and each video/session configuration:

```text
initialize buffer state
initialize history windows with safe defaults
for each segment index t:
    observe only information available before selecting segment t
    build context_features
    enumerate valid candidate representations from the ladder
    build candidate_features for each representation
    compute action_mask
    run teacher policy using allowed teacher inputs
    store supervised label and metadata
    simulate/download chosen representation for transition
    update buffer, throughput history, download history, last action, rebuffer history
```

## Determinism

The environment must be deterministic for a fixed manifest and seed. Re-running the same manifest must produce the same sample count, trace split, normalization stats, labels and sanity metrics within documented tolerance.

## No benchmark boundary

Phase 4 environment outputs are training/validation artifacts. They must not be presented as final benchmark results, final ranking, or formal comparison against all controllers.
