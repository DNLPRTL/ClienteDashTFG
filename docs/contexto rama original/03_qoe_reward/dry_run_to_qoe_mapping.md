# Phase 3.5C Dry-Run To QoE Mapping

Status: implemented_phase3_5c_mapping.

PHASE_3_5C_MAPPING: trace_dry_run_segments_to_qoe_inputs

## Source Artifact

The post-processor reads one existing `trace_dry_run_segments.csv` file from a single dry-run artifact directory. It also expects the paired `trace_dry_run_summary.json` and `trace_dry_run_manifest.json` files for provenance.

## Required Columns

| source column | purpose |
| --- | --- |
| `segment_index` | numeric ordering key; duplicate values are rejected |
| `representation_bitrate_kbps` | mapped to QoE bitrate input |
| `rebuffer_s` | mapped to QoE rebuffer input |
| `controller_name` | must be single-valued within the file |
| `trace_id` | must be single-valued within the file |
| `row_eval_gate` | source row gate used to determine session comparability |
| `outputs_are_benchmark_results` | source benchmark flag; output remains false |
| `final_qoe_reward_defined` | source legacy/pre-A2 signal |
| `no_final_ranking` | source ranking boundary; output remains true |

## Formula Mapping

| dry-run field | QoE input |
| --- | --- |
| `representation_bitrate_kbps` | `SegmentQoEInput.bitrate_kbps` |
| `rebuffer_s` | `SegmentQoEInput.rebuffer_s` |

Rows are sorted numerically by `segment_index` before QoE calculation. If the source order was not already sorted, the run summary records that fact.

## Preserved Optional Columns

If present, the segment reward CSV preserves:

- `phase`
- `phase_label`
- `schema_version`
- `segment_duration_s`
- `buffer_before_s`
- `buffer_after_s`
- `download_duration_s`
- `measured_throughput_kbps`

## Gate Propagation

- If all source rows have `row_eval_gate=use_for_eval`, source flags are consistent, and the expected/completed segment counts match, the session can receive `use_for_eval`.
- If any source row is not `use_for_eval`, the QoE artifacts are still computed but `session_eval_gate=do_not_use_for_eval`.
- Phase 3.4C dry-runs with `row_eval_gate=do_not_use_for_eval` receive `legacy_dry_run` and `generated_before_phase_3_5a2` reasons.
- Source `outputs_are_benchmark_results=true` never promotes the output; it forces a non-evaluable gate and the QoE output still records `outputs_are_benchmark_results=false`.
- `no_final_ranking` is preserved as `true` in the QoE outputs.

## Legacy Boundary

Dry-runs generated before the A2/A2.1/C contract are not automatically promoted. Phase 3.5C may compute diagnostic QoE numbers from them, but it does not convert them into benchmark or ranking evidence.
