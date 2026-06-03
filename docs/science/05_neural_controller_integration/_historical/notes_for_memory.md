# Notes for memory

## Design chapter

Phase 5 supports a design chapter centered on a guarded neural scorer:

- NeuralABR-Lite scores candidate representations.
- The action mask prevents invalid MPD representations.
- A runtime safety guard checks the raw neural action.
- Classical fallback remains mandatory.
- Bundle loading is local-only and fail-closed.

## Implementation chapter

The future implementation chapter can describe:

- a BaseController-compatible wrapper;
- a runtime feature builder from `setPlayerFeedback` data;
- train-only normalization from the bundle;
- PyTorch CPU inference with `model.eval()` and `torch.no_grad()`;
- safe local `state_dict` loading;
- diagnostic telemetry for raw action, safe action and fallback.

## Evaluation chapter

Phase 5 draws a hard line between diagnostic smoke and benchmark:

- structural smoke checks integration only;
- fallback and telemetry checks are diagnostic-only;
- no ranking or improvement claim is allowed;
- formal comparison belongs to Phase 6.

## Limitations

Phase 5 explicitly does not claim:

- real-world validation;
- controller superiority;
- online learning;
- ONNX deployment;
- server-side guidance;
- generalization to unseen networks.

## Future work

Future work may investigate:

- ONNX Runtime migration;
- SODA-style low-compute controller ideas;
- BayesMPC-style uncertainty integration;
- CMCD/CMSD guidance;
- online retraining or lifelong learning;
- multi-model switching;
- real-world testing beyond local traces.
