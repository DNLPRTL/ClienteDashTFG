# Source card 15: BETA under-generalization

## Title

A Novel Spatial-Temporal Learning Method for Enhancing Generalization in Adaptive Video Streaming.

## Authors

Guanghui Zhang, Ziming Wang, Huaren Wei, Mengbai Xiao, Hui Yuan, Dongxiao Yu, Xiuzhen Cheng.

## Year

2025.

## Venue/type

IEEE Transactions on Mobile Computing; research source.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

BETA identifies ABR under-generalization: DRL models can underperform across diverse network conditions.

## Runtime integration pattern

BETA detects problematic conditions, trains specialized models and switches models at runtime.

## Runtime inputs

Real-time network conditions and model-selection signals. Phase 5 does not implement the detector.

## Runtime action/output

Specialized model selection and ABR action.

## Safety/fallback/action mask

The source supports an OOD/generalization risk register, not a Phase 5 action mask.

## Latency/compute/deployment assumptions

Runtime model switching adds complexity and is deferred.

## What transfers to DashClientModular4

- Record OOD/generalization risk.
- Do not claim generalization from Phase 5 smoke.
- Keep telemetry rich enough for later diagnosis.

## What must not be copied

- Detector.
- Specialized model ensemble.
- Runtime model switching.

## Phase 5 docs affected

- `phase5a1_telemetry_contamination_matrix.md`
- `phase5a2_rejected_alternatives.md`
- `_historical/notes_for_memory.md`

## Memory/defense usage

Use this source to explain why Phase 5 does not claim robust generalization.

## Final decision

Transfer under-generalization risk. Defer multi-model switching.

