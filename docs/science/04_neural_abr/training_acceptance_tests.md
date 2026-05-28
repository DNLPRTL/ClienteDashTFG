# Training acceptance tests contract

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Purpose

This document defines the future acceptance tests that must exist before training can be considered reliable.

## Dataset acceptance gates

A future dataset build must pass:

```text
trace source manifest exists
split manifest exists
train/validation/OOD trace ids are disjoint
no dry-runs legacy source appears
feature availability report exists
normalization fit split is train-only
teacher labels are valid actions
no forbidden features appear in model input schema
```

## Model acceptance gates

A future model training run must pass:

```text
training seed recorded
model config recorded
dataset schema version recorded
normalization version recorded
loss curve recorded
validation sanity report recorded
all selected actions valid
CPU inference latency recorded
artifact paths outside repo
```

## Behavioral gates

A future candidate model must be reviewed for:

```text
min/max/fixed collapse
excessive switching
rebuffer spikes
teacher disagreement
OOD degradation
reward hacking
```

## Failure policy

Failing a gate does not necessarily invalidate the thesis. It invalidates claims of successful controller behavior until the limitation is documented or the issue is fixed.

## Phase 4B decision

These tests are required in future implementation specs. They are not implemented in Phase 4B.
