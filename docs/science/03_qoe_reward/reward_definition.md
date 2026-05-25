# Phase 3.5A2 Reward Definition

Status: closed_phase3_5a2_documentation_contract.

PHASE_3_5A2_REWARD_VERSION: qoe_linear_v1
PHASE_3_5A2_REWARD_SCOPE: future_ia_candidate_only
PHASE_3_5A2_NON_GOAL: no_ia_training_in_phase_3_5a2

## Formula Version

The documented reward formula version is `qoe_linear_v1`.

This reward is a future IA candidate only. Phase 3.5A2 does not train IA, select an IA algorithm, create a learning loop or implement reward code.

## Segment Reward

For segment `n`:

```text
q_n = bitrate_kbps_n / 1000.0
smoothness_n = 0.0 if n == 1 else abs(q_n - q_(n-1))
reward_n = q_n - 4.3 * rebuffer_s_n - smoothness_n
```

| term | unit | role |
| --- | --- | --- |
| `bitrate_kbps_n` | kbps | segment bitrate input |
| `q_n` | Mbps utility | positive quality utility |
| `rebuffer_s_n` | seconds | playback interruption penalty input |
| `smoothness_n` | Mbps utility delta | adjacent quality-change penalty input |
| `reward_n` | QoE utility units | segment-level reward candidate |

## Session QoE

For `N` evaluable segments:

```text
qoe_linear_sum = sum(reward_n)
qoe_linear_mean = qoe_linear_sum / N
```

`qoe_linear_mean` is the primary future session metric. `qoe_linear_sum` is an auxiliary accumulated score.

## Evaluation Metric vs Training Reward Candidate

| role | meaning in A2 | status |
| --- | --- | --- |
| evaluation metric | run/session summary score for later comparable artifacts | `qoe_linear_mean` selected as primary future session metric |
| training reward candidate | per-segment scalar that a later IA phase could use | `reward_n` documented as future candidate only |
| controller objective | internal objective used by a specific controller | not changed by A2 |

The same formula family can inform both evaluation and future reward design, but the roles must remain explicit. A2 closes the documentation semantics, not a training setup.

## Phase 4 Compatibility

The segment-level reward is compatible with a future Phase 4 because it is local, scalar, telemetry-derived and defined per segment. This compatibility does not open Phase 4 in A2 and does not select PPO, actor-critic, offline RL or any other IA method.

## Non-Goals

- No IA/training in this block.
- No reward implementation in this block.
- No runner integration in this block.
- No benchmark or ranked controller comparison in this block.
