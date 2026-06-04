# Phase 4E.1 QoE/Reward Context Reconciliation

Phase 3.5 QoE/reward material inspected from the uploaded `03_qoe_reward.zip`:

- Primary formula: `qoe_linear_v1`.
- Primary session metric: `qoe_linear_mean`.
- Segment reward candidate for IA: `reward_n = q_n - 4.3 * rebuffer_s_n - smoothness_n`.
- `q_n = bitrate_kbps_n / 1000.0`.
- `smoothness_n = 0.0` for the first segment, otherwise the absolute Mbps utility delta.
- Startup remains report-only.
- VMAF remains deferred.
- Evaluation gates remain `use_for_eval`, `diagnostic_only`, and `do_not_use_for_eval`.
- Dry-runs and smokes are not formal benchmarks and are not training datasets.

## Consequence for external-trace smoke

Phase 4E.1 must keep these roles separate:

| concept | allowed role in Phase 4E.1 |
|---|---|
| `reward_n` | label/teacher objective context or offline sanity metric |
| `qoe_linear_mean` | diagnostic summary only, not ranking |
| `qoe_log_v1` | sensitivity note only |
| startup | report-only |
| VMAF | deferred |
| gates | required for artifact interpretation |

## Critical boundary

An external-trace smoke can show that the offline model trains and behaves sanely on external trace data. It cannot claim final QoE superiority.

## Markers

- QOE_FORMULA_VERSION: qoe_linear_v1
- TRAINING_REWARD_CANDIDATE: reward_n
- PHASE4E1_BENCHMARK: false
- PHASE4E1_RANKING: false
