# Phase 4F Open Limitations

- Phase 4F is export/inference only.
- NeuralABR-Lite is not registered as a controller and is not integrated into DashClientModular4 runtime.
- No benchmark, ranking, SOTA claim, or real-world validation claim is made.
- Bundle artifacts are local-only and must stay outside the repository.
- OOD diagnostics remain diagnostic-only and must not be tuned on.
- Future Phase 4G must decide whether Phase 5 integration is allowed.
- Future integration must retain a classical safe fallback for invalid, slow, missing, or non-finite neural inference.
- Default pure bundle validation does not scan repository hygiene. Run `scripts/validate_neural_abr_bundle.py --check-repo-hygiene` or the external validation/commit checks when repo artifact hygiene must be blocking.
- Phase 4G is allowed only after the repaired Phase 4F validation passes on both Windows and Ubuntu.
