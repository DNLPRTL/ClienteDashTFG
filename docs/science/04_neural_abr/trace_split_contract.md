# Trace split contract

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Split unit

The split unit is the trace, not the segment and not the generated sample.

Forbidden:

```text
segment-level random split from the same trace into train and validation
generated samples from the same trace appearing in both train and validation
same trace appearing in train and OOD diagnostic
```

## Required split groups

Phase 4 uses:

```text
train
validation
ood_diagnostic
```

There is no formal benchmark ranking split in Phase 4.

## Recommended initial proportions

For a sufficiently large trace corpus:

```text
train: 70%
validation: 15%
ood_diagnostic: 15%
```

If one dataset is clearly out-of-domain, it should be held as `ood_diagnostic` rather than mixed randomly.

## Regime-aware split

Trace regimes must be computed at trace level using simple descriptive features, for example:

```text
median throughput
p05 throughput
p95 throughput
coefficient of variation
mean absolute throughput change
stall-risk proxy
```

Regime buckets may include:

```text
slow_stable
slow_variable
medium_stable
medium_variable
fast_stable
fast_variable
```

The exact thresholds are deferred to Phase 4C/4D, but the split must be regime-aware.

## OOD diagnostic rules

OOD diagnostics are used to detect failure modes, not to tune the model.

Forbidden:

```text
selecting hyperparameters by maximizing OOD performance
rerunning many model variants until OOD looks good
using OOD results as benchmark ranking
```

Allowed:

```text
reporting OOD failures honestly
using OOD to document limitations
using OOD to motivate future work
```

## Seed policy

Every split must record:

```text
split_seed
split_algorithm
trace_ids per split
regime labels per trace
source dataset per trace
creation timestamp
```

## Phase 4B decision

Trace-level disjoint split and OOD diagnostic are mandatory gates before any training.
