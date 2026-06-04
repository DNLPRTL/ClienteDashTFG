# Phase 4E.2 candidate-readiness gate

## Hard gates

A model can be considered ready for Phase 4F only if all hard gates pass:

```text
unit tests PASS
readiness PASS
forbidden artifact check PASS
dataset validation PASS
offline validation PASS
no NaN/Inf
no invalid labels
validation valid action rate == 1.0
OOD diagnostic valid action rate == 1.0
trace-level split
no leakage_group overlap
normalizer fitted on train only
no dry-run legacy data
no controller/player/runtime/media changes
CPU-only execution
at least 30 traces
at least 2 dataset families
at least 3 regime buckets or PASS_NOT_CANDIDATE
CPU inference latency p95 <= 10 ms
model card exists
limitations doc exists
```

## Distribution sanity

The prediction distribution must be compared against the teacher distribution. A high class-4 share is not automatically collapse if the teacher also selects class 4 frequently.

Flag possible collapse when:

```text
total variation distance(predicted, teacher) > 0.25
or entropy(predicted) / entropy(teacher) < 0.60
```

unless the report explains why the trace corpus genuinely produces that pattern.

## Decision rules

```text
Any leakage / invalid actions / artifact contamination / readiness failure:
  PHASE4E2_BLOCKED_NEEDS_FIX

All technical gates pass, but corpus is too small/narrow:
  PHASE4E2_EXPANDED_CORPUS_PASS_NOT_CANDIDATE

All hard gates pass, corpus is sufficient, latency passes, docs complete:
  PHASE4E2_EXPANDED_CORPUS_CANDIDATE_READY_FOR_PHASE4F
```
