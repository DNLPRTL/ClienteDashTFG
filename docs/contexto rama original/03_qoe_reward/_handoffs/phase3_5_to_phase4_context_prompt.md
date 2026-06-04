# Phase 3.5 To Phase 4 Context Prompt

Use this prompt to start the next chat after the Phase 3.5E commit.

## Prompt

Act as implementation-science agent for the TFG DashClientModular4 -- ABR with IA for DASH streaming.

Repository: `DashClientModular4`

Branch: `main`

Expected HEAD after Phase 3.5E: `TO_BE_FILLED_AFTER_COMMIT`

Final Phase 3.5 status:

- QoE/reward scientific evidence is distilled.
- Primary QoE formula is `qoe_linear_v1`.
- Primary future session metric is `qoe_linear_mean`.
- Future IA reward candidate is `reward_n` from `qoe_linear_v1`.
- Sensitivity metric is `qoe_log_v1`.
- Startup is report-only.
- VMAF is deferred and artifact-dependent.
- Gates are documented and implemented around artifacts.
- Pure QoE calculator, post-processor and controlled smoke scenarios exist.

Not closed:

- no formal benchmark;
- no controller ranking;
- no IA/RL training;
- no algorithm selected;
- no generated training artifacts in Git.

Next phase:

- Phase 4 -- IA/RL ABR.
- Recommended first block: Phase 4A0 -- IA/RL ABR literature intake and algorithm triage.

Rules:

- Do not program IA before source papers are carded.
- Do not train without state/action/reward and training-data specs.
- Do not benchmark or rank controllers yet.
- Use source cards and evidence docs.
- Do not commit generated datasets, logs, CSVs, model checkpoints or media.

## Validation markers

- PHASE_3_5_TO_PHASE_4_CONTEXT_PROMPT: ready
- NEXT_PHASE: Phase 4 IA/RL ABR
- FIRST_BLOCK: Phase 4A0 literature intake and algorithm triage
- TO_BE_FILLED_AFTER_COMMIT
