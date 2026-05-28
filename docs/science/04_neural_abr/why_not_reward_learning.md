# Why not reward learning / AIRL as base

Status: **reward learning rejected as Phase 4 base**

## Decision

Do not select AIRL/inverse reinforcement learning/reward learning as the primary method.

## Reasons

Phase 3.5 already closed the QoE/reward methodology:

```text
qoe_linear_v1
qoe_linear_mean
reward_n candidate for IA
qoe_log_v1 sensitivity
startup report-only
VMAF deferred
```

Learning a new reward in Phase 4 would reopen a closed methodology and create unnecessary instability.
It would also make reward hacking harder to diagnose.

## What is retained

AIRL-style sources are still useful for:

- demonstration learning context;
- action masks;
- expert trajectory framing;
- discussion of why learned rewards are out of scope.

## Implementation consequence

The future model trains against teacher actions and evaluates with the fixed Phase 3.5 reward/QoE definitions.
No learned reward is introduced as the base method.
