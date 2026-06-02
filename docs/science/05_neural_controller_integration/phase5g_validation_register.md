# Phase 5G validation register

## Register

| Block | Commit | Validation commands | Test count | Readiness result | Ubuntu result | Artifacts/smoke result | Acceptance decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Phase 5A0/A1/A2/B evidence and contracts | `8c9ca3b` | `python -m unittest discover`; `python scripts\check_client_readiness.py --strict` | 405 tests | PASS | Not applicable to documentation contracts | Documentation-only evidence/contracts; no runtime smoke | Accepted for Phase 5C specification |
| Phase 5C implementation specs | `0374f7b` | `python -m unittest discover`; `python scripts\check_client_readiness.py --strict` | 405 tests | PASS | Not applicable to documentation specs | Documentation-only specs; no runtime smoke | Accepted for Phase 5D implementation |
| Phase 5D guarded controller implementation | `9bf35f6` | Focused neural tests; `python -m unittest discover`; `python scripts\check_client_readiness.py --strict` | 441 tests | PASS | Not required for implementation commit | Synthetic temporary-bundle fake smoke covered by tests; no artifacts committed | Accepted for Phase 5E structural smoke |
| Phase 5E structural smoke preparation/closure | `2f17dd7` / `929bab4` | Focused neural tests; `python -m unittest discover`; `python scripts\check_client_readiness.py --strict` | 441 tests | PASS - 78 OK / 0 WARN / 0 FAIL | PASS for user-reported Ubuntu fake-engine smokes; later PASS for optional Ubuntu/GStreamer structural/demo smoke | No-bundle fake-engine PASS; real-bundle fake-engine PASS; `segment_telemetry.csv` diagnostic fields present; `evaluation_segments.csv` uncontaminated | `ACCEPTED_FOR_PHASE5F` |
| Phase 5F fallback/error/telemetry hardening | `72681b6` | `git diff --check`; py_compile neural runtime files; focused neural tests; new hardening tests; `python -m unittest discover`; `python scripts\check_client_readiness.py --strict`; static unsafe-loading checks | 471 tests | PASS - 78 OK / 0 WARN / 0 FAIL | Phase 5F final Ubuntu confirmation was required by the local gate; final post-hardening regression smoke not provided in Phase 5G input | Hardening tests PASS; static checks show no `weights_only=False`, no `torch.hub`, no URL/request model loading; no artifacts committed | Accepted locally for Phase 5G documentation closure, final smoke passed record |
| Phase 5G final documentation closure | Current docs-only closure | `git status --short --branch`; `git diff --name-only`; `git diff --check`; `python -m unittest discover`; `python scripts\check_client_readiness.py --strict` | 471 tests | PASS - 78 OK / 0 WARN / 0 FAIL | Final post-hardening real-bundle regression smoke: `PASS_RECORDED_AFTER_USER_EXECUTION` | Documentation-only closure; changed files limited to allowed Phase 5G docs, README, and roadmap; no code/tests/config/scripts/artifacts changed | `ACCEPTED_AS_INTEGRATED_GUARDED_CONTROLLER` |

## Notes

- All smoke evidence is structural integration evidence only.
- Phase 5 contains no benchmark, ranking, improvement claim, retraining, or controller comparison.
- Run outputs and real bundle artifacts remain outside Git.


## Final post-hardening real-bundle regression smoke — recorded after Codex closure

Status: PASS.

Executed on Ubuntu after Phase 5F hardening and after the Phase 5G docs-only closure commit was created.

Repository state:
- HEAD: e510ec7 docs(neural-abr): close Phase 5 controller integration
- Branch: main
- Remote state: main...origin/main

Run:
- RUN_DIR_PHASE5G: /home/daniel/TFG/_runs/phase5g_closure_regression/real_bundle_fake_20260602_091533/run_20260602_091534
- media_engine: fake
- controller: neural_abr_lite
- bundle: Phase 4F local-only bundle outside the repository

Artifact inspection:
- run_manifest.json: OK
- config.resolved.json: OK
- environment.json: OK
- run.log: OK
- segment_telemetry.csv: OK
- evaluation_segments.csv: OK
- legacy dataset.csv: absent
- legacy dataset_training.csv: absent

Neural telemetry:
- segment_telemetry.csv contains feedback_neural_* diagnostic columns.
- evaluation_segments.csv contains no neural diagnostic columns.
- feedback_neural_bundle_loaded values include: 1
- feedback_neural_fallback_used values include: 0
- feedback_neural_fallback_reason values include: success_neural
- feedback_neural_diagnostic_only values include: 1
- raw_action and safe_action were present and valid.
- inference_ms was recorded.

Decision:
Phase 5 is accepted as integrated guarded controller.

Boundary:
This smoke is structural integration validation only. It is not benchmark, not ranking, not a QoE improvement claim, and not a real-world generalization claim.
