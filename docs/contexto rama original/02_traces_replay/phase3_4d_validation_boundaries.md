# Phase 3.4D Validation Boundaries

This document separates smoke checks, dry-runs, validation, benchmarks and final evaluation for the trace/replay stack.

## Boundary Terms

| term | meaning | Phase 3.4D status |
| --- | --- | --- |
| Smoke | A small check that a path can execute or that an environment capability exists. | Allowed as local documentation/probe concept only. |
| Dry-run | Controlled integration run that exercises existing code without final metrics. | Phase 3.4C Python dry-run exists, but its outputs are not benchmark results. |
| Validation | Additional evidence that a method behaves as intended under a specified setup. | Mahimahi/tc are optional future validation candidates only. |
| Benchmark | Controlled comparison with frozen metrics, splits and interpretation rules. | Not authorized in Phase 3.4D. |
| Final evaluation | Thesis-facing result interpretation with final QoE/reward and ranking rules. | Deferred to Phase 3.5 and later. |

## Current Artifact Status

Phase 3.4C dry-run artifacts are not benchmark results. They are labeled:

- `phase = phase3_4c_dry_run`;
- `outputs_are_benchmark_results = false`;
- `final_qoe_reward_defined = false`;
- `row_eval_gate = do_not_use_for_eval`;
- `no_final_ranking = true`.

Mahimahi and `tc/netem` runbook outputs are not benchmark results in Phase 3.4D. Environment probes are local/audit-only and must remain outside the repository.

## Prohibited Interpretations

Do not claim:

- one controller is better than another;
- Mahimahi/tc outputs are equivalent to Python dry-run outputs;
- dry-run telemetry is final QoE/reward;
- a probe proves external emulator reproducibility;
- Phase 3.4D creates benchmark evidence;
- IA/RL training is now authorized.

## Phase 3.5 Boundary

Final evaluation metrics and QoE/reward close only in Phase 3.5. Controller ranking remains prohibited until the final benchmark protocol defines:

- metric definitions;
- split/freeze policy;
- artifact contract;
- interpretation rules;
- method labels for Python, Mahimahi or `tc/netem`, if any external validation is later used.

IA/RL training remains prohibited until a later phase explicitly authorizes reward, state, action and split controls.
