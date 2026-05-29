# Phase 4G final limitations

Phase 4 closes with a valid offline NeuralABR-Lite candidate and exportable bundle, but these limitations remain:

1. No formal QoE benchmark has been run.
2. No final ranking against BBA, BOLA, MPC, robust_mpc or classical controllers has been produced.
3. OOD results are diagnostic-only.
4. The HSDPA Norway dataset family is underrepresented in the expanded corpus.
5. The model imitates `robust_mpc`; it is not proven to outperform the teacher.
6. The bundle is not integrated into DashClientModular4 runtime.
7. No real-world deployment claim is made.
8. No SOTA claim is made.
9. The future controller must enforce action mask and fallback at runtime.
10. The future controller must not use any feature unavailable before the next segment request.
11. Future Phase 6 evaluation must be separated from training and tuning artifacts.
12. PyTorch model loading must remain local/trusted; `weights_only=True` hardening should be retained if compatible.

These limitations are acceptable because Phase 4's objective was not final comparative evaluation. Its objective was to produce a scientifically justified, CPU-first, reproducible, offline learned ABR candidate and an exportable inference bundle.
