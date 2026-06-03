# Evaluation Evidence Matrix

Status: protocol-evidence matrix only. No benchmark result is recorded here.

## Source To Protocol Decisions

| Source | Trace-driven evaluation | Claims discipline | Distributions/percentiles | OOD separation | Secondary emulation/demo | VM bridge not benchmark | QoE/reporting boundary | MOS/VMAF boundary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Puffer/Fugu | Supports controlled comparison, but highlights real-world complexity | No winner on small/uncertain differences | Report medians, percentiles, sample counts | Indirect: avoid overgeneralization | Not primary | Not a benchmark path | Report QoE components, not only mean | No perceptual claim transferred |
| CausalSim | Requires exogenous-trace assumption | No causal overclaim | Report uncertainty where possible | Prevent leakage and contaminated splits | Not primary | Not a benchmark path | Gates must separate evaluable/diagnostic rows | No MOS/VMAF claim |
| SODA | Context for ABR evaluation beyond simple heuristics | AI not automatically superior | Report switching/smoothness distributions | Contextual only | Not primary | Not a benchmark path | Include switching as secondary metric | No perceptual claim transferred |
| Into the Wild / ABR-Arena | Trace-driven is controlled, not global real-world | No global deployment claim | Report region/domain limits when applicable | Separate TFG OOD from real-world deployment | Optional future context | VM/content path is demo only | State sim-to-real limits | No MOS/VMAF claim |
| Peroni and Gorinsky | Positions client-side ABR in pipeline | Avoid scope overclaim | Not statistical source | Scope only | Not primary | VM server not CDN benchmark | QoE is part of pipeline scope | No perceptual claim transferred |
| Timmerer et al. | Supports HAS/DASH evaluation context | Avoid broad HAS claims outside client ABR | Not statistical source | Scope only | Not primary | VM server is media/content support | QoE is multidimensional | No perceptual claim transferred |
| Mahimahi | Not primary; emulation is secondary | Emulation output cannot be final ranking alone | Not primary | Not OOD source | Secondary validation/demo only | Do not use VM bridge as benchmark network | Diagnostic labels required | No MOS/VMAF claim |
| Veritas | Warns against run logs as exogenous traces | No counterfactual production claim | Use uncertainty/caution | Prevent contamination by controller-dependent traces | Not primary | Not a benchmark path | Gates separate protocol evidence from claims | No MOS/VMAF claim |
| Plume | Trace distribution must be characterized | Avoid mean-only conclusions | Percentiles/CDF-style summaries needed | Tail/OOD traces must not be hidden | Not primary | Not a benchmark path | Component summaries by dataset/split | No MOS/VMAF claim |
| SABR / ABRBench | Supports train/test/OOD discipline | Preprint used with caution | Use OOD summaries separately | Dedicated OOD required | Not primary | Not a benchmark path | No retraining/tuning on OOD | No MOS/VMAF claim |
| CellReplay | Emulation is not primary trace-driven path | Reproducibility is not perfect fidelity | Not primary | Cellular limits documented | Secondary diagnostic/demo only | VM bridge not benchmark network | Diagnostic labels required | No MOS/VMAF claim |
| HSDPA Norway | Candidate trace family after checks | Legacy domain must be stated | Report by dataset family | Split after checksum/fingerprint audit | Not relevant | Not a benchmark network path | Normalized trace evidence only | No MOS/VMAF claim |
| Ghent 4G/LTE | Candidate trace family after duplicate guardrail | Duplicate/leakage risk must be stated | Report by mobility if used | Split only after deduplication | Not relevant | Not a benchmark network path | Normalized trace evidence only | No MOS/VMAF claim |
| Raca 4G | Future OOD candidate | Modern 4G claims only if materialized | Report mobility/domain components | OOD/test candidate | Not relevant | Not a benchmark network path | Throughput primary, KPIs metadata | No MOS/VMAF claim |
| Raca 5G | Future OOD candidate | 5G claims only if materialized | Report 5G separately | OOD candidate | Not relevant | Not a benchmark network path | Separate production/synthetic | No MOS/VMAF claim |
| Lumos5G | Future OOD candidate | mmWave claims only if materialized | Percentiles important for variability | OOD candidate | Not relevant | Not a benchmark network path | No prediction features as controller input | No MOS/VMAF claim |
| Duanmu QoE Index | Not trace source | No subjective QoE overclaim | Report QoE components | Not OOD source | Not primary | Not a benchmark path | `qoe_linear_v1` objective only | Deferred without artifacts |
| Barman and Martini | Not trace source | No MOS claim from linear QoE | Component reporting | Not OOD source | Not primary | Not a benchmark path | Influence factors: included/report-only/deferred | Deferred without artifacts |
| Taraghi et al. | Not trace source | Objective vs subjective gap stated | Component distributions useful | Not OOD source | Not primary | Not a benchmark path | Bitrate, stalls, switches, startup report-only | Deferred without artifacts |

## Current Binding Decisions

- Python trace-driven evaluation remains the primary path.
- VM bridge networking is not a benchmark path.
- Emulation/demo artifacts must be labeled secondary or diagnostic.
- Future result summaries must include gates/exclusions.
- No MOS, VMAF or perceptual QoE claim is allowed without the required artifacts and a documented metric decision.
