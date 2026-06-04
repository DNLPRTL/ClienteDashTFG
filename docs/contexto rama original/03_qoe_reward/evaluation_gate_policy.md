# Phase 3.5A2 Evaluation Gate Policy

Status: closed_phase3_5a2_documentation_contract.

PHASE_3_5A2_GATES: use_for_eval diagnostic_only do_not_use_for_eval
PHASE_3_5A2_FAILURE_POLICY: gates_not_numeric_punishment

Evaluation gates classify whether rows or sessions are comparable. Gates are not numeric penalties and must not be hidden inside QoE scores.

## Gate Fields

| field | level | meaning |
| --- | --- | --- |
| `row_eval_gate` | segment-level row | whether an individual telemetry row can contribute to metric calculation |
| `session_eval_gate` | run/session | whether the session summary can be used for later evaluation or aggregation |

The session gate dominates the row gate: if the session is not comparable, its rows must not be promoted into benchmark-level aggregates even if some rows look valid.

## Gate Values

| gate | meaning | allowed use |
| --- | --- | --- |
| `use_for_eval` | artifact satisfies the documented contract for its phase | eligible for later evaluation once benchmark protocol exists |
| `diagnostic_only` | artifact is useful for debugging or explanation but not comparable | may be inspected, not aggregated as benchmark evidence |
| `do_not_use_for_eval` | artifact is invalid, legacy, incomplete or outside scope | must not be used for evaluation comparisons |

## Gate Reasons

| reason | typical gate | meaning |
| --- | --- | --- |
| `missing_required_column` | `do_not_use_for_eval` | a required telemetry, formula or schema column is absent |
| `qoe_formula_not_defined` | `do_not_use_for_eval` | artifact predates or omits the formula version contract |
| `legacy_dry_run` | `do_not_use_for_eval` | run was produced before the A2 evaluable contract |
| `incomplete_session` | `do_not_use_for_eval` or `diagnostic_only` | session did not finish expected segments |
| `trace_split_not_allowed` | `do_not_use_for_eval` | trace split is outside the allowed evaluation split |
| `controller_not_in_scope` | `do_not_use_for_eval` | controller is not part of the later declared evaluation scope |
| `runtime_error` | `do_not_use_for_eval` | execution failed or artifact is partial because of runtime error |
| `non_deterministic_run` | `diagnostic_only` or `do_not_use_for_eval` | run cannot be reproduced under the declared contract |
| `generated_before_phase_3_5a` | `do_not_use_for_eval` | artifact was generated before the QoE evidence scaffold |
| `generated_before_phase_3_5a2` | `do_not_use_for_eval` | artifact was generated before the final A2 formula/gate contract |
| `startup_not_measured_homogeneously` | `diagnostic_only` | startup can be reported but not used as a penalty |
| `vmaf_artifacts_missing` | `diagnostic_only` | perceptual metric cannot be computed reproducibly |

## Policy Rules

- Gates avoid contaminated rankings by keeping incomplete, legacy and non-comparable artifacts out of later aggregates.
- Gates are not numeric punishment. A failed run is not converted into an arbitrary low QoE value in A2.
- Dry-runs generated before A2 are not promoted automatically.
- If an artifact is regenerated later, it must record `qoe_formula_version`, `eval_phase`, `outputs_are_benchmark_results`, `session_eval_gate` and the relevant reason fields.
- Startup and VMAF limitations should be explicit reasons, not silent omissions.

## Dry-Run Boundary

Controlled dry-runs from earlier phases remain useful diagnostics. They are not formal benchmark results and should be `do_not_use_for_eval` unless regenerated under the later A2/C contract and the future benchmark protocol.
