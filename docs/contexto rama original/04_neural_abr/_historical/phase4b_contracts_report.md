# Phase 4B contracts report

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Position in the Phase 4 flow

Completed before this block:

```text
Phase 4A0 — literature intake and algorithm triage
Phase 4A1 — source cards + evidence matrix
Phase 4A2 — method decision
```

This block closes the design contracts required before any implementation:

```text
state -> action -> reward -> data -> teacher -> split -> leakage gates -> validation sanity
```

Still not allowed in this block:

```text
no IA implementation
no neural controller integration
no training
no Codex implementation prompt
no benchmark
no ranking
no dry-runs legacy as training dataset
no controllers/player/runtime/media changes
```

## Selected method carried from Phase 4A2

```text
NeuralABR-Lite Candidate Scorer
  small CPU-first neural ABR
  trained by behavior cloning / imitation learning
  output = score per valid representation candidate
  action = representation_index inside the MPD ladder
  safety = action mask + classical fallback
  reward/teacher objective = qoe_linear_v1 / reward_n from Phase 3.5
```

The method remains intentionally small and defensible. The model is not a claim of SOTA and is not a claim of real-world deployment performance. It is a trace-driven, CPU-first, reproducible academic controller candidate.

## Why Phase 4B matters

The literature package produced four hard constraints:

1. **Pensieve / SABR / Comyco** justify neural ABR and imitation-based learning, but do not justify copying a large or old stack.
2. **Puffer / Fugu / Into the Wild / CausalSim** block exaggerated claims and naive trace replay.
3. **Oboe / Plume / MetaABR / ANT / BETA / EAStream** require regime-aware splits and OOD diagnostics.
4. **SODA / ABRL / Ahaggar** require deployability, action validity, smoothness awareness and fallback.

Phase 4B turns those constraints into concrete gates.

## Contract files in this block

```text
state_representation.md
feature_availability_contract.md
candidate_representation_scoring_contract.md
action_space_decision.md
reward_usage_contract.md
training_data_contract.md
trace_split_contract.md
teacher_policy_contract.md
dataset_schema_contract.md
normalization_contract.md
leakage_prevention_for_ia.md
hardware_cpu_first_contract.md
fallback_policy_preintegration.md
validation_sanity_contract.md
training_acceptance_tests.md
artifact_policy_phase4b.md
method_to_contract_traceability.md
phase4b_notes_for_memory.md
phase4b_closure_report.md
phase4b_to_phase4c_handoff.md
phase4c_next_steps.md
```

## Closure condition

Phase 4B is closed when all contract documents exist, contain the required gates, validate as artifact-clean, and no code/runtime/controller/player/media path has been touched.
