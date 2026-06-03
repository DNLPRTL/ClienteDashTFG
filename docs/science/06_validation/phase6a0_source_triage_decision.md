# Phase 6A0 Source Triage Decision

Status: Phase 6A0/A1 documentation triage.

## Triage Categories

- `ACCEPTED_MANDATORY_METHODOLOGY`: required to shape validation protocol and claims discipline.
- `ACCEPTED_GUARDRAIL_SECONDARY`: required or useful guardrail; does not define primary benchmark.
- `ACCEPTED_DATASET_CARD`: dataset candidate requiring local-only materialization checks.
- `ACCEPTED_QOE_REPORTING`: shapes metric boundaries, reporting and threats.
- `DEFERRED_OPTIONAL`: useful later, but not authorized for Phase 6A0 execution.
- `NOT_USED_FOR_EVALUATION`: explicitly not valid as benchmark evidence now.

## Decisions

| Source/candidate | Triage | Decision |
| --- | --- | --- |
| Puffer/Fugu | ACCEPTED_MANDATORY_METHODOLOGY | Use for uncertainty, distributions and cautious comparison. |
| CausalSim | ACCEPTED_MANDATORY_METHODOLOGY | Use for exogenous-trace assumption, leakage and causal-threat language. |
| SODA | ACCEPTED_MANDATORY_METHODOLOGY | Use as modern non-neural context and switching/smoothness reporting support. |
| Into the Wild / ABR-Arena | ACCEPTED_MANDATORY_METHODOLOGY | Use for sim-to-real and no global deployment claim. |
| Peroni and Gorinsky | ACCEPTED_MANDATORY_METHODOLOGY | Use for pipeline taxonomy and scope control. |
| Timmerer et al. HAS review | ACCEPTED_MANDATORY_METHODOLOGY | Use for HAS/DASH/QoE state-of-the-art framing. |
| Mahimahi | ACCEPTED_GUARDRAIL_SECONDARY | Secondary emulation/demo reference only. |
| Veritas | ACCEPTED_GUARDRAIL_SECONDARY | Causal-query warning and no run-log-as-trace rule. |
| Plume | ACCEPTED_GUARDRAIL_SECONDARY | Trace skew and tail reporting guardrail. |
| SABR / ABRBench | ACCEPTED_GUARDRAIL_SECONDARY | One consolidated card; OOD split discipline only. |
| CellReplay | ACCEPTED_GUARDRAIL_SECONDARY | Cellular replay limitation; diagnostic/demo labels only. |
| HSDPA Norway | ACCEPTED_DATASET_CARD | First materialization candidate after license/format checks. |
| Ghent 4G/LTE | ACCEPTED_DATASET_CARD | First materialization candidate with mandatory duplicate guardrail. |
| Raca 4G | ACCEPTED_DATASET_CARD | Future/OOD 4G candidate after checks. |
| Raca 5G | ACCEPTED_DATASET_CARD | Future/OOD 5G candidate after checks. |
| Lumos5G | ACCEPTED_DATASET_CARD | Future/OOD mmWave 5G candidate after checks. |
| Duanmu Streaming QoE Index | ACCEPTED_QOE_REPORTING | QoE limitation and VMAF/MOS caution. |
| Barman and Martini QoE survey | ACCEPTED_QOE_REPORTING | QoE influence factors and metric-boundary support. |
| Taraghi heuristic ABR QoE | ACCEPTED_QOE_REPORTING | Component reporting and objective/subjective gap support. |
| ABRBench dataset | DEFERRED_OPTIONAL | Needs source/dataset card, access/license/format and leakage audit. |
| VMAF/P.1203/MOS primary claims | DEFERRED_OPTIONAL | Artifact-dependent and not authorized in Phase 6A0. |
| Lancaster | DEFERRED_OPTIONAL | Gap until a source note/card exists. |
| Raw PDFs | NOT_USED_FOR_EVALUATION | Not an implementation input. |
| VM bridge network | NOT_USED_FOR_EVALUATION | Not a benchmark network path. |
| Phase 4E2 diagnostics | NOT_USED_FOR_EVALUATION | Not strong generalization evidence. |

## SABR Consolidation Decision

Wave 2 and wave 3 both contain SABR material. Phase 6A0 keeps one canonical SABR source card:

```text
docs/science/06_validation/source_cards/2025_luo_sabr_abrbench_generalization.md
```

The canonical card records both intake origins and keeps the preprint under caution. No second SABR card is created.
