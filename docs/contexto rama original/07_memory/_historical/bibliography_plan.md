# Bibliography Plan

## Core Entries

| key | source |
| --- | --- |
| `stockhammer2011dash` | Dynamic Adaptive Streaming over HTTP: Standards and Design Principles |
| `iso23009_1_2022` | ISO/IEC 23009-1:2022 |
| `bentaleb2019survey` | A Survey on Bitrate Adaptation Schemes for Streaming Media Over HTTP |
| `timmerer2025hasReview` | HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges |
| `peroni2025pipelineSurvey` | An End-to-End Pipeline Perspective on Video Streaming in Best-Effort Networks |
| `ameigeiras2012youtubeTraffic` | Analysis and modelling of YouTube traffic |
| `ramosMunoz2014mobileYoutube` | Characteristics of mobile YouTube traffic |
| `liu2011rateAdaptation` | Rate Adaptation for Adaptive HTTP Streaming |
| `huang2014bba` | A Buffer-Based Approach to Rate Adaptation |
| `spiteri2020bola` | BOLA: Near-Optimal Bitrate Adaptation for Online Videos |
| `yin2015mpc` | A Control-Theoretic Approach for Dynamic Adaptive Video Streaming over HTTP |
| `mao2017pensieve` | Neural Adaptive Video Streaming with Pensieve |
| `spiteri2019dashjs` | From Theory to Practice: Improving Bitrate Adaptation in the DASH Reference Player |
| `chen2024soda` | SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming |
| `netravali2015mahimahi` | Mahimahi: Accurate Record-and-Replay for HTTP |
| `riiser2013commutePath` | Commute Path Bandwidth Traces from 3G Networks: Analysis and Applications |
| `yan2020puffer` | Learning in situ: a randomized experiment in video streaming |
| `alomar2023causalsim` | CausalSim: A Causal Framework for Unbiased Trace-Driven Simulation |
| `bothra2023veritas` | Veritas: Answering Causal Queries from Video Streaming Traces |
| `wei2019traceBasedEmulation` | Evaluation of Throughput Prediction for Adaptive Bitrate Control Using Trace-Based Emulation |
| `hoffman2025intoTheWildABR` | Into the Wild: Real-World Testing for ML-Based ABR |
| `fccMeasuringBroadbandAmerica` | FCC Measuring Broadband America |
| `linuxTcNetemManual` | Linux tc-netem manual |
| `vanDerHooft2016ghent4g` | 4G/LTE Bandwidth Logs, Ghent, Belgium |
| `raca2018beyondThroughput4g` | Beyond Throughput: a 4G LTE Dataset with Channel and Context Metrics |
| `raca2020beyondThroughput5g` | Beyond Throughput, the next Generation: a 5G Dataset with Channel and Context Metrics |
| `narayanan2020lumos5g` | Lumos5G: Mapping and Predicting Commercial mmWave 5G Throughput |
| `lancasterAbrThroughputTraces` | Lancaster ABR-Throughput-Traces |
| `pufferDataArchive` | Puffer data archive / puffer-statistics |

## Phase 3.5A1 QoE/Reward Tracking

| key | source | status |
| --- | --- | --- |
| `seufert2015hasQoeSurvey` | A Survey on Quality of Experience of HTTP Adaptive Streaming | add for QoE influence factors |
| `yin2015mpc` | A Control-Theoretic Approach for Dynamic Adaptive Video Streaming over HTTP | already core; update use for QoE objective |
| `mao2017pensieve` | Neural Adaptive Video Streaming with Pensieve | already core; update use for reward/QoE candidates |
| `spiteri2020bola` | BOLA: Near-Optimal Bitrate Adaptation for Online Videos | already core; update use for log/concave utility |
| `chen2024soda` | SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming | already core; update use for smoothness evidence |
| `peroni2024qoePitfalls` | Quality of Experience in Video Streaming: Status Quo, Pitfalls, and Guidelines | add for methodology cautions |
| `zhou2022adaptiveStreamingQualityAssessment` | A brief survey on adaptive video streaming quality assessment | add for perceptual/quality-assessment context |
| `netflixVmaf` | VMAF official Netflix repository reference | add as official technical source if cited |
| `timmerer2025hasReview` | HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges | already core; update use for modern HAS context |
| `peroni2025pipelineSurvey` | An End-to-End Pipeline Perspective on Video Streaming in Best-Effort Networks | already core; update use for pipeline/QoE context |
| `zuo2022ruyiPreferenceQoe` | Adaptive Bitrate with User-level QoE Preference for Video Streaming | add for user-preference weight variability |
| `alsader2025qoeDriven6g` | QoE-Driven Adaptive Video Streaming: Architectures, Techniques, and Future Research Challenges Toward 6G Networks | add for future-work context |

## Phase 3.5A2 QoE/Reward Use

| decision area | bibliography support |
| --- | --- |
| `qoe_linear_v1` primary formula | `yin2015mpc`, `mao2017pensieve`, with `chen2024soda` supporting smoothness |
| `qoe_log_v1` sensitivity | `mao2017pensieve`, `spiteri2020bola` |
| startup report-only | `seufert2015hasQoeSurvey`, `yin2015mpc` |
| VMAF/perceptual deferred | `zhou2022adaptiveStreamingQualityAssessment`, `netflixVmaf`, `zuo2022ruyiPreferenceQoe` |
| fixed-weight limitation | `peroni2024qoePitfalls`, `zuo2022ruyiPreferenceQoe` |
| gate policy and overclaiming boundary | `peroni2024qoePitfalls`, `peroni2025pipelineSurvey` |
| state-of-the-art and future work | `timmerer2025hasReview`, `alsader2025qoeDriven6g` |

## Phase 3.5E Chapter 6 Support

The Phase 3.5 QoE sources support Chapter 6 methodology rather than benchmark claims:

- `seufert2015hasQoeSurvey` supports stalling, startup and adaptation as influence factors.
- `yin2015mpc` and `mao2017pensieve` support the multi-term `qoe_linear_v1` structure.
- `spiteri2020bola` and `mao2017pensieve` support `qoe_log_v1` as sensitivity.
- `chen2024soda` supports the decision not to omit smoothness/switching.
- `peroni2024qoePitfalls` supports avoiding ad hoc QoE models and overclaiming.
- `zhou2022adaptiveStreamingQualityAssessment`, `netflixVmaf` and `zuo2022ruyiPreferenceQoe` support VMAF/perceptual quality as relevant but artifact-dependent.
- `timmerer2025hasReview`, `peroni2025pipelineSurvey` and `alsader2025qoeDriven6g` support modern context and future-work positioning.

## Later Work

- Verify final BibTeX entries against publisher pages before thesis submission.
- Keep DOI URLs where available.
- Do not include bibliography entries for papers not cited in the final text.
- Use Phase 2 closure docs to decide which optional/deferred methods deserve final bibliography entries. SODA and Pensieve are useful if discussed as future work or historical IA/RL context; RBC should not receive a final entry until its source identity is locked.
- Use Phase 3 source cards to decide which trace/replay entries are cited in Chapter 6. Dataset candidates should not become final bibliography entries unless they are actually used or discussed.
- CausalSim, Veritas, Wei 2019 and Into the Wild/ABR-Arena are Phase 3.2A methodology or threats-to-validity references, not implementation authorizations.
- Phase 3.2B adds no new bibliography sources. It defines local schema, manifest, storage and conversion planning documents derived from the Phase 3.2A source cards.
- Phase 3.2C adds no new bibliography sources. It records local acquisition/audit status for already-carded datasets.
- Phase 3.3A adds no new bibliography sources. It is a local implementation and validation gate for the already-defined normalized trace schema.
- Phase 3.3B adds no new bibliography sources. It is a local loader implementation for already-normalized traces.
- Phase 3.4C adds no new bibliography sources. It is a local controlled dry-run harness and adapter boundary over the already-documented trace/replay methodology.
- Phase 3.4D adds no new bibliography sources. It reuses the existing Mahimahi and Linux `tc-netem` references only to document optional runbook boundaries.
- Phase 3.5E adds no new bibliography sources. It consolidates the QoE/reward sources as Chapter 6 methodology support and Phase 4 context.
