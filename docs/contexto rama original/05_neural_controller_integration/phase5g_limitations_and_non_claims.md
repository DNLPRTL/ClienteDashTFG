# Phase 5G limitations and non-claims

## Explicit non-claims

Phase 5 does not include:

- formal controller comparison;
- benchmark execution;
- controller ranking;
- a claim that `neural_abr_lite` is better than any baseline;
- QoE improvement claim;
- real-world generalization claim;
- retraining;
- online learning;
- model selection by benchmark result.

## Smoke limitations

The fake-engine smoke is structural integration validation only. It verifies that the controller can run through the client path, select rates from the ladder, and keep telemetry boundaries intact.

The Ubuntu/GStreamer smoke is structural/demo validation only. It is not benchmark-grade evidence.

## Bundle limitations

The runtime bundle remains a local artifact outside Git. The repository does not contain the real bundle, model checkpoint, datasets, run outputs, media, or generated smoke artifacts.

## Runtime limitations

The integrated controller uses CPU-first PyTorch inference. It does not add ONNX runtime support, online learning, retraining, or remote model loading.

## Evaluation boundary

Runtime integration is ready subject to the pending final post-hardening smoke record. Formal evaluation is not part of Phase 5.

## Phase 5G pending item

Final post-hardening real-bundle regression smoke for HEAD `72681b6` is recorded as:

```text
PENDING_USER_EXECUTION
```
