# Method-to-contract traceability

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Purpose

This document maps the Phase 4A evidence to Phase 4B contracts.

| Evidence source group | Contract consequence |
|---|---|
| Pensieve | state/action/reward formulation must be explicit |
| Comyco | imitation learning is feasible and sample-efficient |
| SABR | behavior cloning before RL fine-tuning is a modern route; PPO remains optional |
| ABRL/Facebook | candidate scoring over valid bitrates is preferable to fixed bitrate outputs |
| Oboe | network regimes matter; split and validation must be regime-aware |
| Plume/Gelato | trace skew must be addressed by balancing/diagnostics |
| Puffer/Fugu | ML does not automatically beat simple ABR; predictor+policy remains backup |
| CausalSim | biased trace replay and legacy dry-runs are blocked |
| Into the Wild | no global real-world claims from local trace-driven validation |
| MetaABR/MERINA/A2BR/EAStream/BETA/ANT | OOD/generalization is a required diagnostic axis |
| SODA | non-IA ABR may be strong; smoothness and deployability matter |
| AIRL | reward learning is interesting but not selected because Phase 3.5 closed reward_n |
| Fortuna/NMoEABR | offline/meta/MoE methods are frontier context, not CPU-first base |

## Contract stack

```text
method decision
  -> state representation
  -> action mask / candidate scoring
  -> reward usage
  -> teacher policy
  -> trace split
  -> leakage gates
  -> CPU-first hardware policy
  -> future validation sanity
```

## Phase 4B decision

Every later implementation step must trace back to one or more of these contracts.
