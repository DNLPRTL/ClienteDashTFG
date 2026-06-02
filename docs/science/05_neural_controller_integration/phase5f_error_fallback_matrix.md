# Phase 5F error fallback matrix

All entries are diagnostic-only. Benchmark relevance is none unless the field is explicitly described as structural diagnostic telemetry.

| Fault | Expected fallback_reason | Expected selected action/rate behavior | Expected telemetry fields | Test name | Benchmark relevance |
| --- | --- | --- | --- | --- | --- |
| Valid temporary bundle | `success_neural` | Selected rate is from current ladder. | `neural_bundle_loaded=1`, `neural_diagnostic_only=1` | `test_valid_temp_bundle_loads_and_stays_diagnostic` | diagnostic only |
| Missing `bundle_dir` | `missing_bundle_dir` | Classical fallback selects a current ladder rate. | `neural_fallback_used=1`, `neural_bundle_loaded=0` | `test_missing_or_nonexistent_bundle_dir_fails_closed` | none |
| Non-existent `bundle_dir` | `missing_bundle_dir` | Classical fallback selects a current ladder rate. | `neural_fallback_used=1`, `neural_bundle_configured=1` | `test_missing_or_nonexistent_bundle_dir_fails_closed` | none |
| Missing required bundle file | `bundle_schema_invalid` | Classical fallback selects a current ladder rate. | `neural_bundle_loaded=0`, `neural_fallback_used=1` | `test_missing_required_bundle_files_fail_closed` | none |
| Corrupted bundle manifest | `bundle_schema_invalid` | Classical fallback selects a current ladder rate. | `neural_bundle_schema_ok=0`, `neural_fallback_used=1` | `test_corrupted_bundle_manifest_fails_closed` | none |
| Malformed JSON metadata | `bundle_schema_invalid` | Classical fallback selects a current ladder rate. | `neural_bundle_loaded=0`, `neural_fallback_used=1` | `test_malformed_json_metadata_fails_closed` | none |
| Wrong feature schema version | `bundle_schema_invalid` | Classical fallback selects a current ladder rate. | `neural_feature_schema_ok=0`, `neural_fallback_used=1` | `test_wrong_feature_schema_version_fails_closed` | none |
| Hash mismatch | `bundle_hash_invalid` | Classical fallback selects a current ladder rate. | `neural_bundle_hash_ok=0`, `neural_fallback_used=1` | `test_hash_mismatch_fails_closed` | none |
| Architecture/config mismatch | `bundle_schema_invalid` | Classical fallback selects a current ladder rate. | `neural_bundle_loaded=0`, `neural_fallback_used=1` | `test_architecture_mismatch_fails_closed` | none |
| `torch.load` `TypeError` for `weights_only` | `safe_torch_load_unavailable` | Classical fallback selects a current ladder rate; no unsafe retry. | `neural_fallback_used=1`, `neural_bundle_loaded=0` | `test_torch_load_type_error_falls_back_without_unsafe_retry` | none |
| `torch.load` runtime error | `bundle_load_failed` | Classical fallback selects a current ladder rate. | `neural_fallback_used=1`, `neural_bundle_loaded=0` | `test_torch_load_runtime_error_falls_back_without_crash` | none |
| Missing `rates` | `missing_required_feature` | No valid ladder is trusted; selected rate is `0.0`. | `neural_fallback_used=1`, `neural_action_mask_valid_count=0` | `test_missing_and_empty_rates_fail_closed` | none |
| Empty `rates` | `all_actions_invalid` | No valid ladder is trusted; selected rate is `0.0`. | `neural_fallback_used=1`, `neural_action_mask_valid_count=0` | `test_missing_and_empty_rates_fail_closed` | none |
| Invalid rate entries | `action_mask_invalid` | Invalid candidates are masked; controller fails closed instead of executing them. | `neural_fallback_used=1` | `test_invalid_rates_are_masked_for_action_mask_and_fail_closed_in_controller` | none |
| `max_level < 0` | `all_actions_invalid` | No action executes from an all-false mask. | `neural_fallback_used=1`, valid count `0` | `test_max_level_edges_are_safe` | none |
| `max_level` beyond ladder | `success_neural` or later fallback reason | Mask clamps to ladder length. | Valid count equals ladder length. | `test_max_level_edges_are_safe` | diagnostic only |
| Missing `level` | `missing_required_feature` | Classical fallback selects a current ladder rate. | `neural_feature_vector_ok=0`, missing feature recorded. | `test_level_missing_falls_back_and_out_of_bounds_level_clamps_in_features` | none |
| Out-of-bounds `level` | `success_neural` or later fallback reason | Feature builder clamps last representation index to ladder bounds. | Model feature remains finite. | `test_level_missing_falls_back_and_out_of_bounds_level_clamps_in_features` | diagnostic only |
| Missing/non-numeric `queued_time` | `missing_required_feature` | Classical fallback selects a current ladder rate. | `neural_feature_vector_ok=0` | `test_queued_time_missing_or_non_numeric_falls_back` | none |
| Zero `last_download_time` | `success_neural` or later fallback reason | Throughput sample is ignored; no division by zero. | Feature vectors stay finite. | `test_download_sample_missing_or_zero_is_ignored_without_division_by_zero` | diagnostic only |
| Missing `last_fragment_size` | `success_neural` or later fallback reason | Throughput sample is ignored; no future data is used. | Feature vectors stay finite. | `test_download_sample_missing_or_zero_is_ignored_without_division_by_zero` | diagnostic only |
| Missing `fragment_duration` | `missing_required_feature` | Classical fallback selects a current ladder rate. | `neural_feature_vector_ok=0` | `test_missing_fragment_duration_falls_back` | none |
| Single representation | `single_representation` | The only representation is selected. | `neural_safe_action=0`, valid count `1` | `test_single_representation_selects_only_representation` | diagnostic only |
| Forbidden model-input field | `feature_build_failed` | Feature builder rejects payload before inference. | No forbidden field reaches model features. | `test_forbidden_model_input_fields_are_rejected` | none |
| Selected action outside ladder | `selected_masked_action` | Classical fallback selects a current ladder rate. | `neural_invalid_action_detected=1` | `test_selected_action_outside_ladder_falls_back` | none |
| Empty or mismatched scores | `inference_failed` | Classical fallback selects a current ladder rate. | `neural_fallback_used=1` | `test_empty_or_mismatched_scores_fall_back` | none |
| Inference exception | `inference_failed` | Classical fallback selects a current ladder rate. | `neural_fallback_used=1` | `test_inference_exception_and_timeout_fall_back` | none |
| Inference timeout | `inference_timeout` | Classical fallback selects a current ladder rate. | `neural_inference_ms` recorded, fallback used. | `test_inference_exception_and_timeout_fall_back` | diagnostic only |
| Non-finite safety estimate | `safety_guard_rejected` | Safety requests fallback instead of executing the raw action. | `neural_safety_intervened=1` when surfaced through controller. | `test_non_finite_safety_estimate_requests_fallback` | none |
| Fallback controller failure | `fallback_controller_failed` | Lowest valid representation is executed. | `neural_safe_action=0`, fallback used. | `test_fallback_controller_failure_executes_lowest_valid_representation` | none |
| Unknown fallback reason text | `inference_failed` | Classical fallback selects a current ladder rate. | Stable reason label, no exception text/newline. | `test_unknown_fallback_reason_is_sanitized_to_stable_label` | none |
| Neural telemetry hook exception | unchanged/non-neural path | Player update continues without crash. | Existing columns only. | `test_hook_exceptions_do_not_crash_player_update` | none |
