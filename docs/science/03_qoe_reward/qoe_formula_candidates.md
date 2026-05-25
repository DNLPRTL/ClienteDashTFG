# QoE Formula Candidates

Status: candidates only. No final formula is closed in Phase 3.5A1.

## Candidate families

| candidate | evidence base | formula sketch | expected role | A1 status |
| --- | --- | --- | --- | --- |
| qoe_linear_candidate | Pensieve, MPC | `sum q(R_n) - rebuffer_penalty * sum rebuffer_s - smoothness_penalty * sum abs(q(R_n) - q(R_{n-1}))`, with `q(R)=R` or bitrate utility | likely practical for current segment-level telemetry | evidence supports consideration in A2 |
| qoe_log_candidate | Pensieve, BOLA, MPC | same additive structure, with `q(R)=log(R/R_min)` or a BOLA-like concave utility such as `ln(S_m/S_1)` | sensitivity candidate for diminishing returns from higher bitrate | evidence supports consideration in A2 |
| qoe_perceptual_candidate | Zhou 2022, Netflix VMAF, Ruyi | replace or augment bitrate utility with per-segment VMAF/perceptual utility, then combine with rebuffering and smoothness | scientifically attractive but artifact-dependent | likely secondary/deferred unless reference/distorted artifacts exist |
| startup_penalty_candidate | Seufert 2015, Yin 2015 | add `- startup_penalty * startup_delay_s` or report startup separately | report-only or optional penalty candidate | should be considered in A2 if measured homogeneously |
| failure_gate_candidate | Peroni 2024 methodology plus local artifact policy need | use `use_for_eval`, `diagnostic_only` and `do_not_use_for_eval` gates instead of numeric punishment for incomplete/non-comparable runs | gate policy candidate for run comparability | pending final evaluation_gate_policy in A2 |

## qoe_linear_candidate

- Based on Pensieve/MPC additive QoE/reward evidence.
- Uses `q(R)=R` or another bitrate-derived quality utility already available from current telemetry.
- Includes rebuffering and smoothness penalties.
- Likely practical for current DashClientModular4 trace-driven telemetry because bitrate, selected representation and rebuffer-like timing are closer to the existing data path than perceptual artifacts.
- Pending final A2 decision.

## qoe_log_candidate

- Based on Pensieve log-QoE and BOLA utility evidence.
- Uses `q(R)=log(R/R_min)` or another concave utility to represent diminishing returns.
- Useful for sensitivity analysis or an alternative candidate if linear bitrate over-rewards very high representations.
- Pending final A2 decision.

## qoe_perceptual_candidate

- Based on VMAF/perceptual-quality evidence from quality-assessment sources and Ruyi-style preference vectors.
- Requires per-segment perceptual artifacts, a reference/distorted comparison pipeline or another documented perceptual-quality source.
- Not suitable as primary in the current pipeline unless the missing artifacts and reproducibility contract exist.
- Likely secondary/deferred unless measured.

## startup_penalty_candidate

- Justified by Seufert as an HAS QoE influence factor and by Yin/MPC as an explicit term.
- Measurement quality matters: startup delay should not be mixed into the main score if only some runs measure it comparably.
- Should be considered in A2 as an optional penalty or report-only component.

## failure_gate_candidate

- Incomplete sessions, runtime errors and non-comparable runs should be separated by gates.
- A gate avoids hiding failed or partial runs inside an arbitrary numeric penalty.
- Pending final `evaluation_gate_policy.md` in A2.

## Non-decision

This file must not be used as implementation input until Phase 3.5A2 closes `qoe_selection.md`, `reward_definition.md`, `secondary_metrics.md`, `metric_formula_catalog.md`, `benchmark_result_schema.md` and `evaluation_gate_policy.md`.
