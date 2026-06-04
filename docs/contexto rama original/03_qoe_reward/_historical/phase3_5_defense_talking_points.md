# Phase 3.5 Defense Talking Points

## Why Scientific Search Came First

- QoE is not a single universal number; it depends on influence factors, weights and context.
- Phase 3.5 therefore distilled HAS QoE surveys, MPC/Pensieve/BOLA/SODA formulas, VMAF context and QoE methodology cautions before choosing a project metric.
- This makes the final formula a documented engineering decision, not an ad hoc score.

## Why qoe_linear_v1 Is Primary

- It follows the common ABR QoE core: quality utility, rebuffering penalty and smoothness penalty.
- It is compatible with the current telemetry: segment bitrate and rebuffer time.
- It is transparent, reproducible and easy to test.
- It avoids pretending to estimate subjective MOS without validation.

## Why qoe_log_v1 Is Sensitivity

- Log utility is supported by Pensieve variants and BOLA-style diminishing returns.
- It is useful for sensitivity analysis.
- It is not the primary metric because the linear formula is the simplest current telemetry-compatible baseline for Phase 3.5.

## Why VMAF Is Deferred

- VMAF is scientifically relevant for perceptual quality.
- It requires reproducible reference/distorted video artifacts per segment.
- The current pipeline does not generate those artifacts, so VMAF remains deferred and artifact-dependent.

## Why Startup Is Report-Only

- Startup delay is a known QoE influence factor.
- It is kept out of `qoe_linear_v1` until homogeneous measurement is guaranteed.
- If activated later, it should require a new formula version.

## Why Gates Instead Of Numeric Punishment

- Incomplete, legacy or non-comparable artifacts should not be mixed into rankings through arbitrary penalties.
- Gates make the evaluation boundary explicit: `use_for_eval`, `diagnostic_only`, `do_not_use_for_eval`.

## Why Smoke Is Not Benchmark

- Phase 3.5D uses synthetic controlled inputs.
- It validates artifact flow and gates, not real controller performance.
- It does not aggregate results, rank controllers or name winners.

## Why There Is No Ranking Yet

- Ranking requires a formal benchmark protocol, trace splits, aggregation policy and result interpretation policy.
- Phase 3.5 prepares the metric and artifact contract only.

## Why Phase 4 Can Start With A New Gate

- Phase 4 can reuse `reward_n` from `qoe_linear_v1` as a reward candidate.
- Phase 4 must still perform IA/RL literature triage, algorithm selection docs and state/action/reward specs before implementation.

## Validation markers

- PHASE_3_5_DEFENSE_POINTS: ready
- qoe_linear_v1
- smoke not benchmark
- no ranking
- no IA training in Phase 3.5
