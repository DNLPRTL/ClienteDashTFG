# Feature availability contract

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Purpose

This contract separates features that are available online from features that may exist only in offline simulation or teacher generation.

A feature is valid for model input only if it is available before the ABR decision is made.

## Availability classes

| Class | Meaning | Can be model input? |
|---|---|---|
| ONLINE_REQUIRED | Always available before decision | yes |
| ONLINE_OPTIONAL | Available only for some stream types or media indexes | yes, with availability flag |
| OFFLINE_TEACHER_ONLY | May be used by an oracle/teacher to produce labels | no |
| DIAGNOSTIC_ONLY | Used in reports and validation diagnostics | no |
| FORBIDDEN | Creates leakage or invalid claims | no |

## ONLINE_REQUIRED features

```text
previous throughput samples
previous download times
buffer_s before decision
last_representation_index
last_bitrate_bps
valid representation ladder
candidate bitrate
candidate representation index
```

## ONLINE_OPTIONAL features

```text
candidate_chunk_size_bytes
chunks_remaining
media_duration
segment_duration
```

Rules:

- They require availability flags.
- They cannot be silently assumed.
- If the client cannot provide them at inference time, the model config must disable them.

## OFFLINE_TEACHER_ONLY features

```text
future throughput samples
future chunk download outcomes
future rebuffer caused by action sequences
oracle rollout return
```

Rules:

- These may be used only to generate diagnostic upper-bound labels or to evaluate a teacher.
- They must never be serialized as model input features.

## DIAGNOSTIC_ONLY features

```text
trace regime label
split name
dataset name
final QoE of a run
controller identity
OOD flag
```

These can be used for analysis and stratified reporting, but not as model inputs.

## FORBIDDEN features

```text
test-set statistics used in training normalization
validation/OOD labels used for hyperparameter selection
future network capacity inferred from the target trace after the decision
legacy dry-run controller outputs used as ground-truth network state
```

## Gate

Any future dataset builder must emit a `feature_availability_report` that maps every generated feature to one of these classes.
