# Next steps — Phase 4B contracts

Phase 4B starts after Phase 4A2 is applied and validated.

## Step 1 — State representation

Create `../state_representation.md`.

It must decide:

```text
k throughput history size
k download-time history size
buffer normalization
last representation encoding
switch/rebuffer history
chunks remaining usage
whether candidate chunk size is allowed
which features are online-observable
```

## Step 2 — Action space

Create `../action_space_decision.md`.

It must decide:

```text
action = representation_index
candidate mask
invalid-action fallback
variable ladder handling
mapping from model score to selected representation
```

## Step 3 — Reward contract

Create `../reward_usage_contract.md`.

It must decide:

```text
reward_n usage
qoe_linear_v1 usage
qoe_linear_mean usage
qoe_log_v1 diagnostic-only role
startup report-only role
VMAF deferred role
```

## Step 4 — Teacher policy contract

Create `../teacher_policy_contract.md`.

It must compare:

```text
MPC teacher
robust_mpc teacher
oracle-limited teacher
consensus teacher
```

## Step 5 — Training data contract

Create `../training_data_contract.md` and `../trace_split_contract.md`.

They must decide:

```text
allowed trace sources
forbidden trace sources
train/validation/OOD split
regime clustering
seeds
no dry-runs legacy
no smoke scenarios
```

## Step 6 — Leakage prevention

Create `../leakage_prevention_for_ia.md`.

It must define hard blockers:

```text
future throughput not in model inputs
future chunk sizes only if truly available via MPD/media metadata
teacher future allowed only for labels
validation/OOD never used for training or hyperparameter tuning
legacy dry-runs forbidden as training data
```

## Step 7 — Artifact policy

Create `artifact_policy_for_training.md`.

It must define:

```text
PDFs outside repo
datasets outside repo
models/checkpoints outside repo
logs outside repo
CSV experiment artifacts outside repo
only repo-ready markdown/specs committed
```
