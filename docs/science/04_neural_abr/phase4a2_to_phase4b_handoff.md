# Phase 4A2 to Phase 4B handoff

## Current flow position

```text
search
  -> PDFs
  -> source_cards
  -> evidence_matrix
  -> method_decision      <-- CLOSING
  -> specs                <-- NEXT: Phase 4B
  -> Codex
```

## Selected method for Phase 4B specs

```text
NeuralABR-Lite Candidate Scorer
```

## Phase 4B must produce

```text
docs/science/04_neural_abr/state_representation.md
docs/science/04_neural_abr/action_space_decision.md
docs/science/04_neural_abr/reward_usage_contract.md
docs/science/04_neural_abr/teacher_policy_contract.md
docs/science/04_neural_abr/training_data_contract.md
docs/science/04_neural_abr/trace_split_contract.md
docs/science/04_neural_abr/leakage_prevention_for_ia.md
docs/science/04_neural_abr/fallback_policy_preintegration.md
docs/science/04_neural_abr/artifact_policy_for_training.md
docs/science/04_neural_abr/phase4b_contracts_report.md
```

## Phase 4B questions

1. What exact context features are available online?
2. Which candidate features are available without future leakage?
3. What is the final action mask?
4. Which teacher policy generates labels?
5. What traces/datasets are allowed for train/validation/OOD?
6. What trace regimes define balanced sampling?
7. What reward version is used for teacher selection and validation?
8. What artifacts are local-only and never committed?
9. What acceptance tests must exist before Codex implementation?

## Still blocked after A2

```text
implementation
training
dataset generation
Codex implementation prompt
benchmark
ranking
controller integration
```

## Phase 4B expected stance

Phase 4B should be strict.
Any feature that is not observable at decision time must be rejected as model input.
Any dataset that cannot be separated into train/validation/OOD without leakage must be rejected.
Any teacher that uses future information must keep that information only inside label generation, never in model inputs.
