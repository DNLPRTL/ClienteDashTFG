# Phase 3.5A2 QoE Selection

Status: closed_phase3_5a2_documentation_contract.

PHASE_3_5A2_DECISION: primary_qoe=qoe_linear_v1
PHASE_3_5A2_DECISION: primary_session_metric=qoe_linear_mean
PHASE_3_5A2_DECISION: startup_penalty_weight=0.0
PHASE_3_5A2_DECISION: vmaf_status=deferred_artifact_dependent
PHASE_3_5A2_DECISION: dry_runs_are_not_benchmarks=true

## Primary Decision

The primary QoE formula version for later evaluable run summaries is `qoe_linear_v1`.

The primary session metric is `qoe_linear_mean`.

```text
qoe_formula_version = qoe_linear_v1
primary_session_metric = qoe_linear_mean
```

This decision closes the Phase 3.5 documentation contract only. It does not implement a calculator, modify a runner, execute experiments, produce a ranking or create a formal benchmark.

## Segment Formula

For each segment `n`:

| symbol | definition | unit |
| --- | --- | --- |
| `bitrate_kbps_n` | bitrate of segment `n` | kbps |
| `q_n` | `bitrate_kbps_n / 1000.0` | Mbps utility |
| `rebuffer_s_n` | rebuffering seconds attributed to segment `n` | seconds |
| `smoothness_n` | `0.0` if `n == 1`, else `abs(q_n - q_(n-1))` | Mbps utility delta |
| `reward_n` | `q_n - 4.3 * rebuffer_s_n - smoothness_n` | QoE utility units |

## Session Formula

For a session with `N` evaluable segments:

```text
qoe_linear_sum = sum(reward_n)
qoe_linear_mean = qoe_linear_sum / N
quality_utility_sum = sum(q_n)
rebuffer_penalty = 4.3 * sum(rebuffer_s_n)
smoothness_penalty = sum(smoothness_n)
total_rebuffer_s = sum(rebuffer_s_n)
avg_bitrate_kbps = mean(bitrate_kbps_n)
avg_quality_mbps = mean(q_n)
total_switch_magnitude_kbps = sum(abs(bitrate_kbps_n - bitrate_kbps_(n-1))) for n > 1
quality_switch_count = count(bitrate_kbps_n != bitrate_kbps_(n-1)) for n > 1
```

If `N == 0`, the session is not comparable and must not receive `use_for_eval`.

## Weights

| term | weight | source rationale |
| --- | --- | --- |
| quality utility | `+1.0` | Pensieve/MPC additive quality term; current telemetry supports bitrate-derived utility |
| rebuffering | `-4.3` | Pensieve linear QoE variant; consistent with the selected linear utility scale |
| smoothness | `-1.0` | Pensieve/MPC absolute quality-change penalty |
| startup delay | `0.0` | Seufert/Yin support startup as an influence factor, but A2 keeps it report-only |
| VMAF/perceptual | not included | Zhou/Netflix/Ruyi support relevance, but required artifacts are absent from the current contract |

## Evidence Justification

- Pensieve and MPC support a transparent additive formula with quality utility, rebuffering penalty and smoothness penalty.
- Pensieve provides the `4.3` rebuffering weight for the linear utility candidate.
- SODA supports not omitting smoothness from the evaluation vocabulary.
- Peroni 2024 supports using a transparent classical formula instead of inventing an ad hoc subjective model without validation.
- Ruyi/Zuo shows weights vary by user, so this formula is a reproducible TFG metric choice, not a universal claim about all viewers.

## Why qoe_log_v1 Is Sensitivity

`qoe_log_v1` is retained as a secondary sensitivity metric because Pensieve and BOLA support log/concave utility and diminishing returns. It is not the primary metric because the current pipeline can document a simpler linear Mbps utility directly from `bitrate_kbps_n`, while log utility requires an explicit `min_bitrate_kbps` reference and changes score interpretation.

## Why VMAF Is Deferred

VMAF/perceptual quality is scientifically relevant, but artifact-dependent. It requires reproducible per-segment perceptual artifacts, normally including reference/distorted video inputs or an equivalent documented pipeline. Phase 3.5A2 does not add VMAF as a primary metric and does not calculate VMAF from bitrate-only telemetry.

## Why Startup Is Report-Only

Startup delay is an HAS QoE influence factor, and Yin/MPC includes a startup term. Phase 3.5A2 sets `startup_penalty_weight = 0.0` because startup should not be mixed into `qoe_linear_v1` until the measurement is homogeneous across evaluable sessions. If a startup penalty is activated later, it requires a new formula version.

## Why Failures Use Gates

Incomplete sessions, runtime errors and non-comparable artifacts are handled by `session_eval_gate` and `row_eval_gate`, not by ad hoc numeric punishment. This keeps invalid artifacts visible and avoids contaminating later comparisons.

## Relation To Existing Dry-Runs

Dry-runs generated before the Phase 3.5A2 contract are not formal benchmark evidence. They are `do_not_use_for_eval` unless regenerated under a later controlled contract that records the required fields, formula version, evaluation phase and gates.

## Explicit Warnings

- No hay benchmark formal todavia.
- No hay ranking formal todavia.
- `qoe_linear_v1` is a documentation contract for later implementation, not an already-computed result.
