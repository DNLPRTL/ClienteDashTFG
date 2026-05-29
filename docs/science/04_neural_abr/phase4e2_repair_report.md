# Phase 4E.2 Repair Report

Phase 4E.2 follows Phase 4E.1 because the earlier work only proved external trace ingestion on a small smoke corpus. The repair keeps the scope offline and diagnostic while making the expanded corpus usable for candidate-readiness assessment.

## R2 cross-platform repair

After commit `316e37f`, the Windows expanded run passed and produced a Phase 4E.2 candidate-ready diagnostic result. Ubuntu validation then failed in `tests.test_neural_abr_candidate_readiness` because the pure candidate-readiness assessor treated `no_forbidden_repo_artifacts` as a hard correctness gate and scanned the real repository during unit tests.

The R2 repair separates gates into three categories:

- hard correctness gates: invalid actions, invalid labels, NaN/Inf, split leakage, broken dataset validation, broken offline validation, non-CPU execution, or broken train-only normalization;
- candidate-readiness gates: trace count, dataset-family count, regime-bucket count, model-card presence, and limitations-doc presence;
- environmental or external gates: repository artifact scans and protected-path git scans.

If only candidate-readiness gates fail, the decision is `PHASE4E2_EXPANDED_CORPUS_PASS_NOT_CANDIDATE` and the CLI exits 0. Environmental gates are `UNKNOWN` unless explicitly supplied or explicitly checked, and only explicit failures can block.

Phase 4F remains blocked until Ubuntu validation passes after this R2 repair.

The repair addressed two blockers: unsupported `phase4e2_regime_balanced_trace_v1` split policy during dataset build, and a missing candidate-readiness assessor CLI.

The split loader now accepts Phase 4E.1 and Phase 4E.2 policies. Phase 4E.2 assignment is trace-level, leakage-group clean, deterministic with seed, and uses dataset/regime strata when metadata is available.

The assessor CLI accepts the required `--dataset-dir`, `--run-dir`, `--validation-dir`, `--output-dir`, and `--phase phase4e2` arguments. Normal PASS_NOT_CANDIDATE outcomes exit with code 0, while correctness blockers exit with code 1.

Candidate-readiness is assessed from dataset manifests, leakage checks, train-only normalization, CPU training metadata, offline validation metrics, prediction-vs-teacher distributions, repo artifact hygiene, and required memory/limitations docs.

This is still not a benchmark or ranking because it does not compare against the classical controllers in a formal evaluation matrix and does not make deployment or real-world claims.

Decision after latest assessment: `PHASE4E2_EXPANDED_CORPUS_CANDIDATE_READY_FOR_PHASE4F`
