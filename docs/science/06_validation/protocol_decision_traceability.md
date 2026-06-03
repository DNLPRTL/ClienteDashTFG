# Protocol Decision Traceability

Status: source-to-decision traceability for Phase 6A0/A1 documentation.

| Source | Decision | Document | Future phase gate |
| --- | --- | --- | --- |
| Puffer/Fugu | Report uncertainty, distributions and sample counts; no winner from fragile differences | `evaluation_evidence_matrix.md`, `phase6a0_no_benchmark_yet.md` | Phase 6A2 statistical comparison plan |
| CausalSim | Primary trace-driven path must state exogenous-trace assumption and leakage gates | `threats_matrix.md`, `phase6a0_open_gaps_for_phase6b.md` | Phase 6B/C eligibility audit |
| SODA | Treat modern non-neural ABR seriously; report switching/smoothness | `evaluation_evidence_matrix.md` | Phase 6A2 metrics schema |
| Into the Wild / ABR-Arena | No global real-world deployment claim from trace-driven results | `threats_matrix.md` | Phase 6A2 threats-to-validity finalization |
| Peroni and Gorinsky | Keep scope to client-side ABR in larger streaming pipeline | `phase6a0_literature_delta_report.md` | Thesis/memory integration |
| Timmerer et al. | Use current HAS/DASH terminology and multidimensional QoE framing | `phase6a0_literature_delta_report.md` | Thesis/memory integration |
| Mahimahi | Keep emulation as secondary/demo, not primary benchmark | `evaluation_evidence_matrix.md` | Ubuntu demo gate, if any |
| Veritas | Do not reuse controller run logs as neutral traces; avoid counterfactual overclaims | `threats_matrix.md` | Phase 6B protocol review |
| Plume | Report dataset/split/tail behavior; avoid mean-only conclusions | `evaluation_evidence_matrix.md` | Phase 6A2 results table/statistics plan |
| SABR / ABRBench | Keep one canonical card; OOD separation, no retraining | `phase6a0_source_triage_decision.md` | Dataset card and license/format gate before ABRBench use |
| CellReplay | Diagnostic/demo labels for cellular replay/emulation | `evaluation_evidence_matrix.md` | Ubuntu evidence package gate |
| HSDPA Norway | First materialization candidate after format/license checks | `dataset_evidence_matrix.md` | Phase 6C dataset materialization gate |
| Ghent 4G/LTE | Hard `logs_all` versus per-mobility deduplication rule | `dataset_evidence_matrix.md` | Phase 6C duplicate/fingerprint audit |
| Raca 4G | Future/OOD 4G candidate | `dataset_evidence_matrix.md` | Access/license/format gate |
| Raca 5G | Future/OOD 5G candidate | `dataset_evidence_matrix.md` | Access/license/format gate |
| Lumos5G | Future/OOD mmWave candidate | `dataset_evidence_matrix.md` | Access/license/format gate |
| Duanmu QoE Index | Keep linear QoE objective; defer perceptual claims | `evaluation_evidence_matrix.md` | Metric artifact gate |
| Barman and Martini | Report QoE influence factors and boundaries | `evaluation_evidence_matrix.md` | Phase 6A2 metrics schema |
| Taraghi et al. | Report bitrate, stalls, switches and startup separately | `evaluation_evidence_matrix.md` | Phase 6A2 results table plan |
| Lancaster | Not authorized until source note/card exists | `dataset_evidence_matrix.md`, `phase6a0_open_gaps_for_phase6b.md` | Source card intake gate |

## Traceability Rule

Future Phase 6 prompts should reference this table before changing protocol, metrics, dataset eligibility or evidence package requirements.
