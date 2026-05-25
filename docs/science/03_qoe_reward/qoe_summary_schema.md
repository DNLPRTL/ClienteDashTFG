# Phase 3.5C QoE Summary Schema

Status: implemented_phase3_5c_artifact_schema.

PHASE_3_5C_QOE_SUMMARY_SCHEMA: qoe_artifacts_v1

## Artifact Set

Phase 3.5C writes three QoE artifacts:

- `qoe_segment_rewards.csv`
- `qoe_run_summary.json`
- `qoe_artifact_manifest.json`

Every artifact belongs to `eval_phase=phase3_5c_qoe_artifact_computation`.

## qoe_segment_rewards.csv

Minimum columns:

- `segment_index`
- `trace_id`
- `controller_name`
- `qoe_formula_version`
- `bitrate_kbps`
- `rebuffer_s`
- `quality_utility_mbps`
- `smoothness_penalty`
- `rebuffer_penalty`
- `segment_reward`
- `source_row_eval_gate`
- `row_eval_gate`
- `eval_phase`
- `outputs_are_benchmark_results`
- `no_final_ranking`

Optional dry-run columns are preserved when present.

## qoe_run_summary.json

The run summary records `qoe_linear_v1` metrics, optional `qoe_log_v1` sensitivity metrics and gate status. It is a run-level artifact, not a benchmark aggregate.

## qoe_artifact_manifest.json

The manifest records:

- `artifact_type=qoe_artifact_manifest`
- `eval_phase`
- `outputs_are_benchmark_results=false`
- `no_final_ranking=true`
- `session_eval_gate`
- `gate_reasons`
- generated QoE artifact filenames
- source dry-run artifact filenames

## Non-Claims

- `outputs_are_benchmark_results=false` in Phase 3.5C.
- `no_final_ranking=true` in Phase 3.5C.
- QoE artifacts are not controller rankings.
- QoE artifacts are not formal benchmark outputs.
