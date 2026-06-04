# Reward usage contract

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Reward decision

The reward/QoE objective for Phase 4 IA work is inherited from Phase 3.5:

```text
qoe_linear_v1
reward_n
```

This reward is the only default optimization target for teacher selection, label generation diagnostics, and offline validation in Phase 4.

## Allowed uses

`qoe_linear_v1 / reward_n` may be used for:

```text
teacher trajectory scoring
teacher action comparison
training-label metadata
validation sanity reports
OOD diagnostic reports
method analysis
```

## Not allowed

The reward must not be changed silently.

Forbidden without a new versioned methodology document:

```text
changing rebuffer penalty
changing switching penalty
adding startup to optimized reward if startup remains report-only
switching to qoe_log_v1 as default
adding VMAF as default reward
normalizing reward with validation/test/OOD statistics
optimizing a hidden proxy while reporting reward_n
```

## Diagnostic-only metrics

The following remain diagnostic/report-only unless separately promoted by a new phase decision:

```text
qoe_log_v1 sensitivity
startup metrics
VMAF / perceptual metrics
real-world QoE claims
```

## Reward hacking gates

A future training run must fail sanity review if it achieves high reward by:

```text
collapsing to min_rate in all cases
collapsing to max_rate in all cases
causing excessive switching
using invalid actions
exploiting startup report-only status
exploiting unavailable future information
optimizing validation/OOD after seeing their outcomes
```

## Phase 4B decision

Reward is closed as `qoe_linear_v1 / reward_n`. Reward learning, inverse RL, AIRL-style learned reward, and new QoE definitions are explicitly not selected for the base implementation.
