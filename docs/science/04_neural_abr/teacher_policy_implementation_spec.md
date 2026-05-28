# Teacher policy implementation spec

## Primary teacher

```text
robust_mpc_policy_replay
```

Implementation may wrap the existing `robust_mpc` controller through the existing public feedback contract, or implement an equivalent deterministic teacher replay adapter if the wrapper is cleaner.

## Secondary teacher

```text
mpc_policy_replay
```

Used for comparison/diagnostics, not as the default label source unless explicitly configured.

## Diagnostic-only upper bound

```text
bounded_oracle_teacher
```

The oracle may inspect future network information only to compute an upper-bound diagnostic label. It must not be the default teacher and must never leak future values into model features.

## Teacher output

```json
{
  "teacher_name": "robust_mpc",
  "teacher_action": 2,
  "teacher_reason": "robust_mpc_sequence_selection",
  "teacher_reward_n": 0.42,
  "diagnostic_only": false
}
```

## Gate

Every teacher action must satisfy:

```text
0 <= teacher_action < representation_count
action_mask[teacher_action] == true
```
