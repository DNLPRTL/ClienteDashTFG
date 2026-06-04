# Phase 4F Bundle Validation Report

Decision: `PHASE4F_EXPORT_BUNDLE_READY_FOR_PHASE4G`

Phase 4F validates a local-only export/inference bundle. It does not integrate NeuralABR-Lite into DashClientModular4 and does not register a neural controller.

- Bundle dir: `C:\Users\danie\Documents\TFG\_models\phase4_AI\neural_abr_lite\phase4F\bundle_20260529_091652`
- Hard failures: `[]`
- Warnings: `[]`

## Gates

- `deterministic_inference`: `PASS` (1.0)
- `fallback_policy_present`: `PASS` (C:\Users\danie\Documents\TFG\_models\phase4_AI\neural_abr_lite\phase4F\bundle_20260529_091652\fallback_policy.json)
- `feature_schema_present`: `PASS` (C:\Users\danie\Documents\TFG\_models\phase4_AI\neural_abr_lite\phase4F\bundle_20260529_091652\feature_schema.json)
- `inference_contract_present`: `PASS` (C:\Users\danie\Documents\TFG\_models\phase4_AI\neural_abr_lite\phase4F\bundle_20260529_091652\inference_contract.json)
- `ladder_schema_present`: `PASS` (C:\Users\danie\Documents\TFG\_models\phase4_AI\neural_abr_lite\phase4F\bundle_20260529_091652\ladder_schema.json)
- `model_card_present`: `PASS` (C:\Users\danie\Documents\TFG\_models\phase4_AI\neural_abr_lite\phase4F\bundle_20260529_091652\model_card.json)
- `model_loads_on_cpu`: `PASS` (model_state.pt loads with map_location=cpu and eval mode)
- `no_controller_player_runtime_media_main_changes`: `PASS` ([])
- `no_nan_inf_scores`: `PASS` (True)
- `no_repo_artifacts`: `PASS` ([])
- `normalization_stats_present`: `PASS` (C:\Users\danie\Documents\TFG\_models\phase4_AI\neural_abr_lite\phase4F\bundle_20260529_091652\normalization_stats.json)
- `p95_latency_ms`: `PASS` (0.11300016194581985)
- `required_files_present`: `PASS` (all required bundle files are present)
- `sample_inference_valid_action_rate`: `PASS` (1.0)
- `sha256_hashes_match`: `PASS` (all payload hashes match bundle_manifest.json)

No benchmark/ranking, SOTA, or real-world validation claim is made. Bundle artifacts are local-only and outside the repository. Phase 4G will decide whether Phase 5 integration is allowed.
