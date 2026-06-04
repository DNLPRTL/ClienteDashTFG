# Phase 4 remaining roadmap after Phase 4C

## Current point

```text
A0 literature intake: closed
A1 source cards + evidence matrix: closed
A2 method decision: closed
B contracts: closed after validation
C training environment / simulator contract: current
```

## Phase 4C — Training environment / simulator contract

Purpose:

```text
Specify offline replay, traces, teacher labels, sample generation, leakage audit and artifact layout.
```

Exit gate:

```text
Phase 4C docs validated.
No code changed.
No artifacts in repo.
Ready to generate Codex prompt for offline training pipeline only.
```

## Phase 4D — Offline training pipeline implementation

Purpose:

```text
Implement offline neural ABR pipeline outside the client runtime boundary.
```

Allowed future code:

```text
core/neural_abr/ trace/data/model support
scripts/build_neural_abr_dataset.py
scripts/validate_neural_abr_dataset.py
scripts/train_neural_abr.py
scripts/validate_neural_abr_offline.py
```

Not allowed:

```text
client controller registration
player/runtime/media changes
formal benchmark/ranking
legacy dry-runs as training dataset
```

Exit gate:

```text
unit tests pass;
dataset builder smoke pass;
leakage audit pass;
training smoke command exists;
no client integration yet.
```

## Phase 4E — Training smoke + offline validation

Purpose:

```text
Train a small candidate model and decide whether it is academically defensible as an offline candidate.
```

Exit gate for `OFFLINE_CANDIDATE`:

```text
valid actions 100%;
NaN/Inf 0;
no leakage;
no collapse;
beats random/pathological sanity baselines on validation;
latency CPU within budget;
OOD diagnostic reported;
reproducibility pass;
limitations documented.
```

Important:

```text
Phase 4E does not require beating BBA/MPC/robustMPC in a formal benchmark.
If the model loses to classical controllers, the result can still be defensible if explained honestly.
```

## Phase 4F — Export and inference contract

Purpose:

```text
Convert the offline candidate into a safe model bundle for later integration.
```

Required bundle:

```text
model_state.pt or equivalent
model_card.json
feature_schema.json
normalization_stats.json
inference_contract.json
fallback_policy.json
export_manifest.json
```

Exit gate:

```text
model bundle is deterministic;
inference API contract is clear;
action mask is enforced;
fallback behavior is specified;
latency sanity pass;
no training artifacts enter repo.
```

## Phase 4G — Phase 4 closure and go/no-go for Phase 5

Purpose:

```text
Close Phase 4 and decide whether the candidate may be integrated into DashClientModular4.
```

Possible final statuses:

```text
ACCEPTED_FOR_PHASE5_INTEGRATION
DIAGNOSTIC_ONLY_NOT_FOR_INTEGRATION
NEGATIVE_RESULT_DOCUMENTED
```

Only the first status allows Phase 5 client integration.

## Phase 5 — Client integration, only after Phase 4G acceptance

Purpose:

```text
Integrate the accepted model as an experimental controller with fallback and safety gates.
```

Not allowed before Phase 5:

```text
touch controllers/player/runtime/media for neural ABR integration
register IA controller
run formal benchmark/ranking
claim final superiority
```
