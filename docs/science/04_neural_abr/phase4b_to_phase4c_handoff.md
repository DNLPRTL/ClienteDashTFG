# Phase 4B to Phase 4C handoff

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Handoff summary

Phase 4B has converted the method decision into contracts. Phase 4C must now define the offline training/simulation environment without touching the player/runtime/controller integration.

## Phase 4C must specify

```text
training environment boundary
trace representation format
teacher replay procedure
sample generation procedure
normalization fitting procedure
split manifest generation
artifact layout outside repo
training smoke acceptance plan
validation report schema
```

## Phase 4C must not do

```text
no model training yet, unless later explicitly included as a smoke spec
no controller integration
no player/runtime/media changes
no benchmark/ranking
no use of dry-runs legacy
```

## Inputs from Phase 4B

```text
state_representation.md
action_space_decision.md
reward_usage_contract.md
training_data_contract.md
trace_split_contract.md
teacher_policy_contract.md
leakage_prevention_for_ia.md
hardware_cpu_first_contract.md
```

## Output expected from Phase 4C

A complete training environment specification that is ready to become a Codex implementation prompt only after review.
