# Phase 5A0 source triage decision

## Categories

- `ACCEPTED_FOR_SOURCE_CARD`: directly affects Phase 5 integration contracts.
- `BACKGROUND_ONLY`: useful for TFG context, not a direct implementation contract.
- `TECHNICAL_REFERENCE_ONLY`: used for API/security constraints, not ABR method evidence.
- `REJECTED_FOR_PHASE5`: not needed for this controller integration block.
- `DEFERRED_TO_PHASE6_OR_FUTURE_WORK`: interesting, but outside Phase 5 implementation readiness.

## Decisions

| Source | Triage | Rationale |
|---|---|---|
| SafeSABR | ACCEPTED_FOR_SOURCE_CARD | Directly supports raw action, safety auditor, lower feasible action and fallback telemetry. |
| DeepBuffer | ACCEPTED_FOR_SOURCE_CARD | Directly supports variable ladders and mandatory action masks. |
| A2BR | ACCEPTED_FOR_SOURCE_CARD | Supports domain priors and classical fallback while rejecting online adaptation for Phase 5. |
| ABRL / Facebook | ACCEPTED_FOR_SOURCE_CARD | Supports score-per-candidate representation and modest deployment claims. |
| Ahaggar | ACCEPTED_FOR_SOURCE_CARD | Supports advisory ML guidance with client heuristic fallback. |
| Puffer/Fugu | ACCEPTED_FOR_SOURCE_CARD | Supports hybrid ML/classical boundaries and not benchmark caution. |
| Hybrid ABR | ACCEPTED_FOR_SOURCE_CARD | Supports decision-level fallback to RobustMPC-style logic. |
| BayesMPC | ACCEPTED_FOR_SOURCE_CARD | Supports conservative feasibility checks under uncertainty. |
| CausalSim | ACCEPTED_FOR_SOURCE_CARD | Directly warns against trace and telemetry contamination. |
| Into the Wild / ABR-Arena | ACCEPTED_FOR_SOURCE_CARD | Directly supports no real-world claims from Phase 5 smoke. |
| Comyco | ACCEPTED_FOR_SOURCE_CARD | Supports imitation learning while deferring lifelong updates. |
| Oboe | ACCEPTED_FOR_SOURCE_CARD | Supports runtime regime diagnostics as future analysis, not Phase 5 tuning. |
| SODA | ACCEPTED_FOR_SOURCE_CARD | Supports CPU and low-compute deployment constraints. |
| SABR | ACCEPTED_FOR_SOURCE_CARD | Supports BC pretraining background and OOD caution; RL fine-tuning deferred. |
| BETA | ACCEPTED_FOR_SOURCE_CARD | Documents under-generalization risk and defers model switching. |
| ANT | ACCEPTED_FOR_SOURCE_CARD | Warns that simple throughput averages are limited; supports richer diagnostics. |
| Gelato/Plume | ACCEPTED_FOR_SOURCE_CARD | Supports trace skew risk and no premature generalization claims. |
| ML model loading security | ACCEPTED_FOR_SOURCE_CARD | Directly shapes the runtime model loading threat model. |
| HAS Review 2025 | BACKGROUND_ONLY | Explains HAS/DASH client-side ABR placement. |
| Learning-Based HAS Review 2025 | BACKGROUND_ONLY | Provides survey context and deployment gap framing. |
| MetaABR | BACKGROUND_ONLY | Supports no meta-learning in Phase 5. |
| PyTorch 2.12 documentation | TECHNICAL_REFERENCE_ONLY | Defines safe CPU loading pattern. |
| ONNX Runtime Python API | TECHNICAL_REFERENCE_ONLY / DEFERRED_TO_PHASE6_OR_FUTURE_WORK | Useful future migration option, not a Phase 5 dependency. |
| eBandit | REJECTED_FOR_PHASE5 | Not needed for guarded Candidate Scorer integration. |
| PivotSketch | REJECTED_FOR_PHASE5 | Not directly relevant to controller API, action mask or fallback contracts. |
| CADENCE | REJECTED_FOR_PHASE5 | Outside current client integration scope. |
| ABUV | REJECTED_FOR_PHASE5 | Does not change Phase 5 integration contracts. |
| Edge-assisted secure streaming | DEFERRED_TO_PHASE6_OR_FUTURE_WORK | Requires system architecture beyond local bundle integration. |
| Cross-layer wireless tuning | DEFERRED_TO_PHASE6_OR_FUTURE_WORK | Requires signals not currently exposed by the client. |
| mmWave/3D streaming | DEFERRED_TO_PHASE6_OR_FUTURE_WORK | Domain extension, not current DASH client integration. |
