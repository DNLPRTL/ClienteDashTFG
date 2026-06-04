# Network regime contract

## Purpose

Define how Phase 4 groups traces by network regime for balanced training and diagnostic validation.

## Motivation

The literature intake showed that ABR performance depends strongly on network regime. Oboe, Plume/Gelato, MetaABR, ANT and BETA all point to distribution shift, trace skew and under-generalization as major threats.

## Regime features

Computed from train traces only for fitting thresholds or clustering:

```text
mean throughput
median throughput
p05 throughput
p95 throughput
coefficient of variation
mean absolute throughput change
stall-risk proxy
bitrate-ceiling proxy
duration_s
```

## Initial human-readable buckets

```text
slow_stable
slow_variable
medium_stable
medium_variable
fast_stable
fast_variable
unknown_or_short
```

These labels are not model targets. They are used for balancing, diagnostics, tables and OOD design.

## No leakage rule

Regime labels may be used to build splits and diagnostic reports. They must not be fed as model features unless Phase 4B/4C explicitly marks them computable online at decision time.

## OOD design

At least one OOD diagnostic mode must be planned:

```text
held-out source dataset
held-out regime bucket
synthetic stress traces
```

OOD diagnostics are not used for hyperparameter tuning.
