# Phase 3.5A1 Source-Card Distillation Report

Status: completed documentation block.

## Initial repository state

- Expected initial HEAD: `0a43675`
- Expected initial commit: `docs(science): scaffold Phase 3.5 QoE evidence intake`
- Branch: `main`
- Scope: Markdown-only scientific documentation under `docs/science`.

## Source cards filled

- `../source_cards/seufert2015_has_qoe_survey.md`
- `../source_cards/yin2015_mpc_qoe_objective.md`
- `../source_cards/mao2017_pensieve_qoe_reward.md`
- `../source_cards/spiteri2020_bola_utility_qoe.md`
- `../source_cards/chen2024_soda_smoothness_qoe.md`
- `../source_cards/peroni2024_qoe_pitfalls_guidelines.md`
- `../source_cards/zhou2022_adaptive_streaming_quality_assessment.md`
- `../source_cards/netflix_vmaf_perceptual_quality.md`
- `../source_cards/timmerer2025_has_review_qoe_context.md`
- `../source_cards/peroni2025_pipeline_qoe_context.md`
- `../source_cards/zuo2022_ruyi_user_preference_qoe.md`
- `../source_cards/alsader2025_qoe_driven_streaming_6g.md`

## Matrix and crosswalk updates

- `../qoe_evidence_matrix.md` now compares all 12 sources across quality utility, rebuffering/stalling, smoothness, startup, perceptual/VMAF, latency/live-specific factors, reward/evaluation role, units/weights and practical implications.
- `../qoe_terms_crosswalk.md` now normalizes local terms against paper terms: `quality_utility`, `rebuffering`, `smoothness`, `startup_delay`, `perceptual_quality`, `training_reward`, `evaluation_metric`, `evaluation_gate` and `failure_handling`.
- `../qoe_formula_candidates.md` now lists candidate families only: linear, log, perceptual, startup penalty and failure gate.
- `../source_inventory.md` and `../source_triage_decision.md` now record A1 distillation status.

## Scientific synthesis

- Common core: the strongest ABR/QoE sources converge on quality utility, rebuffering/stalling and smoothness/switching.
- Startup is relevant, but its inclusion depends on homogeneous measurement. It should be considered in A2 and may remain report-only if the telemetry contract is uneven.
- VMAF and perceptual quality are relevant, but artifact-dependent. They are likely secondary/deferred unless per-segment perceptual artifacts and reference/distorted video requirements are satisfied.
- User preference weights vary, so any fixed weights in this TFG should be framed as a reproducible engineering choice, not a universal user truth.
- Methodology sources warn against ad hoc QoE models without validation. A transparent classical candidate is better supported than inventing a new subjective model.

## Candidates passed to Phase 3.5A2

- `qoe_linear_candidate`: Pensieve/MPC additive quality minus rebuffering and smoothness penalties.
- `qoe_log_candidate`: Pensieve/BOLA concave quality utility with the same penalty family.
- `qoe_perceptual_candidate`: VMAF/perceptual utility, likely secondary/deferred unless artifacts exist.
- `startup_penalty_candidate`: optional or report-only startup term if measured homogeneously.
- `failure_gate_candidate`: explicit gates for incomplete/non-comparable artifacts rather than hidden numeric punishment.

## What remains for A2

- `../qoe_selection.md`
- `../reward_definition.md`
- `../secondary_metrics.md`
- `../metric_formula_catalog.md`
- `../benchmark_result_schema.md`
- `../evaluation_gate_policy.md`

## Non-goals respected

- No code was implemented.
- No `core/evaluation` package was created.
- No controller, player, runtime, media-engine or trace-runner files were modified.
- No CSVs, logs, zips, PDFs, media or generated artifacts were added.
- No IA/RL training or algorithm selection was opened.
- No ranked controller comparison was produced.
- No formal benchmark claim was made.
- No final QoE/reward formula was closed.

## Memory-doc updates

All requested memory docs existed and were updated minimally:

- `docs/science/07_memory/_historical/chapter_06_evaluation_methodology_notes.md`
- `docs/science/07_memory/_historical/tables_plan.md`
- `docs/science/07_memory/_historical/figures_plan.md`
- `docs/science/07_memory/figures_tables_register.md`
- `docs/science/07_memory/_historical/bibliography_plan.md`

