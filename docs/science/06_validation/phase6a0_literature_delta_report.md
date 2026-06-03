# Phase 6A0 Literature Delta Report

Status: documentation-only consolidation from Phase 6A0 intake waves.

## Delta From Phase 6P/P2

Phase 6P and Phase 6P2 closed workspace hygiene, documentation re-cohesion and evidence-integrity preparation. Phase 6A0 now opens the validation documentation path and adds a literature-based protocol scaffold.

This delta does not add benchmark outputs. It adds protocol evidence.

## Methodology Delta

| Source | Delta added |
| --- | --- |
| Puffer/Fugu | Benchmark reporting must include uncertainty, distributions and sample counts, not only means. |
| CausalSim | Trace-driven evaluation requires an explicit exogenous-trace assumption and leakage blocking. |
| SODA | Modern non-neural ABR remains strong context; AI is not automatically superior. |
| Into the Wild / ABR-Arena | Trace-driven results do not imply global real-world deployment performance. |
| Peroni and Gorinsky | The TFG scope is client-side HAS/DASH ABR inside a larger streaming pipeline. |
| Timmerer et al. | QoE and HAS terminology are aligned with current survey literature. |

## Guardrail Delta

| Source | Delta added |
| --- | --- |
| Mahimahi | Emulation can be useful for Ubuntu demos, but is secondary to Python trace-driven evaluation. |
| Veritas | Logs produced under one controller cannot be treated as neutral counterfactual evidence for another. |
| Plume | Trace skew and tail traces require per-dataset/per-split reporting and percentiles. |
| SABR | Learning-based ABR needs OOD separation; ABRBench remains deferred until checked. |
| CellReplay | Cellular replay/emulation can be workload-sensitive; demos must be labeled diagnostic. |

## Dataset Delta

- HSDPA Norway and Ghent are first materialization candidates.
- Ghent has a hard duplicate rule: use `logs_all` or per-mobility folders, not both, unless deduplicated by checksum/fingerprint before split.
- Raca 4G, Raca 5G and Lumos5G are future OOD candidates subject to access, license and format checks.
- Lancaster remains a Phase 6C gap because the current wave pack did not include a source card/source note for it.

## QoE Delta

- `qoe_linear_v1` remains the primary formula.
- `qoe_linear_mean` is the future primary session metric for Phase 6 result summaries.
- `qoe_log_v1` remains a sensitivity metric.
- Startup remains report-only unless measured homogeneously.
- VMAF/P.1203/MOS-style claims are deferred until the needed artifacts exist.
- QoE reporting must include components such as bitrate, rebuffering, switching, gates and exclusions.

## Non-Delta

This block does not:

- change controller code;
- change training or model artifacts;
- change `qoe_linear_v1` or `reward_n`;
- run benchmarks;
- create plots;
- create rankings;
- declare a winner;
- claim `neural_abr_lite` QoE improvement.
