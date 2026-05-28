# Why not PPO-first

Status: **PPO-first rejected as Phase 4 base**

## Decision

Do not select PPO/A2C/A3C-first as the base Phase 4 method.

## Reasons

1. **High training variance.** RL policies can be unstable, sensitive to reward weights and hard to reproduce.
2. **Reward hacking risk.** Directly optimizing `reward_n` can produce pathological behavior unless many sanity checks exist.
3. **CPU-first constraint.** Long RL training loops are not aligned with the current hardware/software stack.
4. **Dependency risk.** Modern PPO often introduces Stable-Baselines3/Gymnasium/RLlib-like dependencies; older papers use obsolete TensorFlow/Ray stacks.
5. **Defense risk.** It is harder to explain a PPO policy failure than a supervised imitation policy failure.
6. **Literature risk.** The recent evidence points to pretraining/behavior cloning first, with RL fine-tuning only as optional extension.

## What is still allowed

PPO may remain as:

```text
optional tiny fine-tune after behavior cloning
```

Only if:

- the BC model is stable;
- the training environment is specified;
- reward hacking gates exist;
- CPU-first reproducibility is acceptable;
- it is not needed for the thesis core.

## What is not allowed

```text
No PPO by inertia.
No PPO before state/action/reward/data contracts.
No PPO as the first IA deliverable.
No PPO benchmark/ranking in Phase 4.
```
