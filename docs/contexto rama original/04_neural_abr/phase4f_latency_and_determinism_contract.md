# Phase 4F latency and determinism contract

Phase 4F must measure offline inference latency on CPU.

Acceptance target:

- p95 latency <= 10 ms per ABR decision on the user's Windows CPU environment;
- 100% valid actions after action mask;
- repeated inference on the same input returns the same selected representation in eval mode;
- no NaN/Inf in scores;
- bundle load succeeds without GPU/CUDA/DirectML/WSL.

The latency number is not a benchmark against ABR controllers. It is only a safety/feasibility gate for future integration.
