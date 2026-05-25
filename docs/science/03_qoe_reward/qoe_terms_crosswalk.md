# QoE Terms Crosswalk

Status: closed_phase3_5a2_terms.

This file normalizes paper terminology into the A2 contract. It does not implement code.

| local term | paper terms | A2 closed local field/formula | unit/type | A2 status |
| --- | --- | --- | --- | --- |
| `quality_utility` | bitrate, video quality, quality, utility | `quality_utility_mbps = bitrate_kbps / 1000.0` | Mbps utility | closed for `qoe_linear_v1` |
| `rebuffering` | stalling, freezing, playback interruption, buffer underrun | `rebuffer_s` | seconds | closed for `qoe_linear_v1` |
| `smoothness` | bitrate switching, quality variation, quality change, instability | `abs(delta quality_utility_mbps)` | Mbps utility delta | closed for `qoe_linear_v1` |
| `startup_delay` | initial delay, startup latency, join time | `startup_delay_s` | seconds | report-only; `startup_penalty_weight = 0.0` |
| `perceptual_quality` | VMAF, PSNR, SSIM, MOS proxy, signal fidelity | VMAF/perceptual branch | metric-specific | deferred/artifact-dependent |
| `training_reward` | scalar reward, RL objective, ABR reward | `reward_n` from `qoe_linear_v1` | QoE utility units per segment | future IA candidate only |
| `evaluation_metric` | QoE score, average QoE per chunk, run-level QoE | `qoe_linear_mean` primary, `qoe_linear_sum` auxiliary | QoE utility units | closed as future evaluation summary terms |
| `evaluation_gate` | use_for_eval, diagnostic_only, do_not_use_for_eval | `row_eval_gate`, `session_eval_gate` | categorical | closed as gate policy |
| `failure_handling` | incomplete session, runtime error, failed run, non-comparable run | `session_eval_gate`, `failure_reason` | categorical | gates, not numeric punishment |
| `latency` | live latency, end-to-end delay, glass-to-glass delay | no A2 primary field | seconds if later scoped | deferred |

## A2 Normalization Notes

- The linear primary quality term is `quality_utility_mbps`, not raw kbps.
- `smoothness` is computed on Mbps utility for `qoe_linear_v1`; kbps switch metrics remain secondary diagnostics.
- `startup_delay_s` can be reported, but it is excluded from `qoe_linear_v1`.
- VMAF must not be inferred from bitrate-only telemetry.
- `training_reward` is a future IA candidate only and does not activate training or select an algorithm.
- `row_eval_gate` and `session_eval_gate` control comparability before any future aggregate.
