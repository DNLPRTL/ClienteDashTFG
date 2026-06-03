# Phase 4C next steps

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Next block after Phase 4B

```text
Phase 4C — training environment / simulator contract
```

## Documents to generate in Phase 4C

```text
training_environment_spec.md
simulator_vs_client_boundary.md
trace_format_spec.md
trace_conversion_spec.md
teacher_replay_spec.md
sample_generation_spec.md
normalization_fit_spec.md
split_manifest_spec.md
artifact_layout_phase4c.md
offline_validation_protocol.md
phase4c_acceptance_gates.md
phase4c_to_phase4d_handoff.md
```

## First Phase 4C question

Before implementation, decide which trace sources are allowed and how they will be represented locally.

The likely local-only roots are:

```text
C:\Users\danie\Documents\TFG\_datasets\phase4_AI
C:\Users\danie\Documents\TFG\_runs\phase4_AI
C:\Users\danie\Documents\TFG\_models\phase4_AI
```

## Reminder

Phase 4C still does not mean Codex implementation. It is the final spec layer before implementation prompts.
