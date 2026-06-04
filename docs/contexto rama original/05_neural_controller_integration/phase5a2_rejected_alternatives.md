# Phase 5A2 rejected alternatives

| Alternative | Decision | Reason |
|---|---|---|
| Full neural policy | Rejected for Phase 5 | Would make the model the final control owner and increase failure risk. |
| PPO fine-tuning | Rejected for Phase 5 | Phase 4 selected behavior cloning; RL fine-tuning would require new training and validation. |
| Lifelong learning | Deferred | Comyco-style updates need a training/update loop outside this integration block. |
| Meta-RL | Deferred | A2BR/MetaABR-style adaptation is beyond safe client integration. |
| Server guidance | Deferred | Ahaggar-style CMCD/CMSD guidance changes system architecture. |
| ONNX as current dependency | Deferred | PyTorch state_dict already matches Phase 4; ONNX requires a new conversion contract. |
| SODA implementation | Rejected for Phase 5 | SODA is a separate controller design, not the accepted Candidate Scorer integration. |
| BayesMPC implementation | Rejected for Phase 5 | BayesMPC is useful for conservative safety framing, not a new MPC implementation now. |
| BETA/ANT switching | Deferred | Multi-model switching needs model families, detectors and evaluation not present in Phase 5. |
| Gelato/Plume retraining | Deferred | Trace skew mitigation and real-world retraining belong to future evaluation/retraining work. |

## Final note

Rejected and deferred alternatives remain useful for the TFG limitations and future-work chapters. They do not change the Phase 5 decision: guarded neural scorer, action mask, safety guard, classical fallback, CPU-first local inference, diagnostic-only telemetry and no benchmark.
