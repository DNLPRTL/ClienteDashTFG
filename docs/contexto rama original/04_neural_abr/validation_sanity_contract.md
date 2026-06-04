# Validation sanity contract

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Purpose

Phase 4 validation is not a formal benchmark. It is a sanity and methodology gate.

## Required future sanity checks

A future trained model must satisfy:

```text
all selected actions are valid representation_index values
no invalid action mask violations
no NaN/Inf scores
model does not collapse trivially to min_rate
model does not collapse trivially to max_rate
model does not copy a fixed_rate pattern unless the teacher/data justify it
validation loss/reward diagnostics are reported honestly
OOD diagnostic is reported separately from validation
inference latency is measured on CPU
```

## Collapse checks

A model is suspicious if:

```text
>95% of actions are the same representation across diverse validation traces
switching is extreme without QoE benefit
rebuffer is reduced only by permanent lowest-bitrate behavior
quality is high only by inducing unacceptable rebuffering
```

Thresholds may be refined in Phase 4C/4D, but collapse detection is mandatory.

## No ranking

Phase 4 validation must not produce a final controller ranking.

Allowed:

```text
sanity comparison against teacher
sanity comparison against random/minimal baseline
diagnostic comparison against existing controllers with explicit no-ranking label
```

Forbidden:

```text
claiming final benchmark winner
ranking controllers for thesis conclusions
using Phase 4 validation as Phase 6 benchmark
```

## Phase 4B decision

Validation is sanity-only until a later benchmark phase defines formal evaluation.
