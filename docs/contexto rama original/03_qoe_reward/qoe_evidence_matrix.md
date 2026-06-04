# Phase 3.5A2 QoE Evidence Matrix

Status: interpreted_phase3_5a2. This matrix records how A1 evidence affected the A2 contract.

## Matrix

| source | source role | quality utility | rebuffering/stalling | switching/smoothness | startup delay | perceptual/VMAF | training reward vs evaluation metric | units/weights | practical for DashClientModular4 | A2 decision impact |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| QOE-M01 Seufert 2015 | HAS QoE survey | Video quality/adaptation is an influence factor | Stalling is unexpected and severe | Adaptation/quality variability affects QoE | Initial delay is separate and normally less severe than stalling | Indirect subjective QoE context | Methodology/context, not reward | No universal weights | Strong for term justification | Supports stalling/rebuffering as core and startup as report-only influence factor |
| QOE-M02 Yin 2015 MPC | Classical ABR QoE objective | Explicit `sum q(R_k)` | Explicit rebuffer penalty | Explicit quality-variation penalty | Explicit startup term | No VMAF-specific model | Controller objective can inform evaluation candidate if role-labeled | `lambda`, `mu`, `mu_s` non-negative | Strong candidate formula evidence | Supports `qoe_linear_v1` structure; startup remains report-only in A2 |
| QOE-M03 Mao 2017 Pensieve | Neural ABR reward/QoE evaluation | Linear/log/HD quality utilities | `mu * sum T_n` | absolute quality-change penalty | Not in quoted reward core | No VMAF-specific model | Training reward and average QoE per chunk must be role-labeled | `mu=4.3` linear, `mu=2.66` log, `mu=8` HD | Strong formula evidence | Supports `qoe_linear_v1` with `4.3` and `qoe_log_v1` sensitivity with `2.66` |
| QOE-M04 Spiteri 2020 BOLA | Utility-based ABR | Utility maximization; example `ln(S_m/S_1)` | Rebuffer avoidance via utility/buffer trade-off | Switching mitigation possible but not central | Not central | No VMAF-specific model | Controller objective, not universal evaluation metric | `V`, `gamma`, utility `v_m` | Strong for log/concave utility | Supports `qoe_log_v1` as sensitivity and diminishing-returns discussion |
| QOE-M05 Chen 2024 SODA | Modern smoothness/QoE source | High video quality component | Rebuffer minimized through buffer-cost framing | Bitrate switching is a key term | Not central | No direct VMAF dependency | Controller objective, not direct current metric | `beta`, `gamma`, `omega_n`, time factors | Strong for smoothness evidence | Supports not omitting smoothness from `qoe_linear_v1` |
| QOE-M06 Peroni 2024 | QoE methodology and pitfalls | Influence factor with subjective/contextual limits | Measurable influence factor | Measurable influence factor | Valid only if measured and validated | Objective models require caution | Distinguish test conducting, model building and model using | No weights prescribed | Strong methodology guardrail | Justifies transparent classical formula and avoiding ad hoc QoE/overclaiming |
| QOE-M07 Zhou 2022 | Adaptive streaming quality assessment survey | QoS, signal fidelity and hybrid models | HAS needs playback-issue terms | Adaptive quality changes matter | Initial buffering is a playback issue | Strong VQA/perceptual context | Evaluation/modeling context, not reward | Metric-specific units | Useful for perceptual discussion | Supports VMAF/perceptual as relevant but artifact-dependent/deferred |
| QOE-M08 Netflix VMAF | Official VMAF technical source | VMAF can score perceptual quality | Does not model stalling | Switching would need per-segment score deltas | No | Official VMAF/libvmaf tooling | Technical tool, not ABR reward | VMAF/model parameters | Practical only with reference/distorted artifacts | Supports VMAF deferment unless reproducible artifacts exist |
| QOE-R01 Timmerer 2025 | Modern HAS review/context | HAS QoE and ABR context | HAS QoE context | ABR adaptation context | Contextual | VMAF-aware/energy-aware directions | State of the art, not formula source | No A2 weights | Chapter 2/future work | Context only; does not alter `qoe_linear_v1` decision |
| QOE-R02 Peroni/Gorinsky 2025 | End-to-end pipeline survey/tutorial | QoE models map measurable factors to experience | Stall duration is measurable influence factor | Contextual | Contextual | Contextual | Model-using context, not reward | No A2 weights | Scope boundary | Supports measurable-factor framing without expanding to full CDN/ingestion pipeline |
| QOE-R03 Zuo 2022 Ruyi | User-preference QoE source | VMAF/quality vector term | Rebuffer vector term | Smoothness/switch vector term | Not central | VMAF in preference vector | Preference-aware objective, not current reward | User weights `w_i`; VMAF [0,100] | Weight variability evidence | Supports fixed A2 weights as reproducible choice, not universal truth; VMAF deferred |
| QOE-R04 Alsader 2025 | QoE-driven streaming survey/future context | Broad QoE-driven taxonomy | Broad QoE-driven taxonomy | Broad QoE-driven taxonomy | Contextual | Contextual | Context/future work, not local reward | No local weights | Future-work framing | Context only; does not pull A2 toward 6G, slicing, XR or IA/RL |

## A2 Interpretation Summary

- Pensieve/MPC support `qoe_linear_v1`.
- BOLA supports `qoe_log_v1` as sensitivity.
- Seufert/Yin support startup as an influence factor, but A2 leaves it report-only.
- Zhou/Netflix/Ruyi support VMAF/perceptual relevance, but A2 keeps it artifact-dependent and deferred.
- Peroni 2024 justifies avoiding ad hoc QoE and overclaiming.
- SODA supports not omitting smoothness.

## Reading Rule

Use `qoe_selection.md`, `reward_definition.md`, `secondary_metrics.md`, `metric_formula_catalog.md`, `evaluation_gate_policy.md` and `benchmark_result_schema.md` as the A2 contract. This matrix is the evidence interpretation behind those documents.
