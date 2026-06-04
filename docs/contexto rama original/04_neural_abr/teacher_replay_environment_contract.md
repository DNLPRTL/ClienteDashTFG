# Teacher replay environment contract

## Purpose

Define how teacher labels are generated for behavior cloning without contaminating model features.

## Teachers

```text
T0 primary: robust_mpc_policy_replay
T1 secondary/comparator: mpc_policy_replay
T2 diagnostic upper bound: bounded_oracle_teacher
```

## Teacher label

The supervised label is:

```text
teacher_representation_index
```

Optional label metadata:

```text
teacher_score_by_candidate
teacher_reward_estimate
teacher_name
teacher_config_hash
teacher_confidence_proxy
```

Teacher metadata must not become a model input.

## Teacher information boundary

A teacher may use more planning information than the deployed model if and only if:

```text
1. the extra information is used only to produce labels;
2. the extra information is recorded in teacher metadata;
3. no extra information is copied into model features;
4. the source card / contract marks the risk;
5. the leakage audit can detect violations.
```

## Oracle policy

The bounded oracle is diagnostic only by default. It may provide an upper-bound label distribution or sanity comparison, but it is not the base teacher unless Phase 4A2/B is explicitly reopened.

## Teacher split rule

Teachers may generate labels only for traces assigned to the corresponding split. A model trained on train labels must not see validation/OOD labels during fitting or hyperparameter selection.
