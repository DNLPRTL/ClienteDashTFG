# Phase 3.5 Transition To Phase 4

Phase 3.5 enables Phase 4 to start from a documented reward and artifact boundary, but it does not authorize IA/RL implementation by itself.

## Enabled For Phase 4

- `reward_n` from `qoe_linear_v1` as a candidate reward.
- Pure QoE calculator for `qoe_linear_v1` and `qoe_log_v1`.
- Isolated QoE artifact post-processor.
- Evaluation gates: `use_for_eval`, `diagnostic_only`, `do_not_use_for_eval`.
- No-ranking and no-benchmark policy.
- Controlled smoke validation of the artifact path.

## Not Enabled

- No formal benchmark.
- No controller ranking.
- No training over real datasets without a new IA/RL spec.
- No PPO, actor-critic, offline RL or other algorithm selection without paper search and decision docs.
- No legacy dry-run artifacts as training data.
- No generated training artifacts in Git.

## Phase 4 Entry Conditions

Phase 4 should start only after:

- a new IA/RL ABR scientific search;
- IA/RL source cards;
- state/action/reward specification;
- training/evaluation split specification;
- reproducibility plan;
- safety and overclaiming boundary;
- acceptance tests;
- artifact storage policy that keeps generated training artifacts outside Git.

## Suggested First Subphase

Phase 4A0 -- IA/RL ABR literature intake and algorithm triage.

## Validation markers

- PHASE_3_5_TO_PHASE_4_GATE: open_after_closure
- PHASE_4_FIRST_BLOCK: literature_intake_algorithm_triage
- reward_candidate=qoe_linear_v1
- no IA training before Phase 4 specs
- no benchmark promotion
