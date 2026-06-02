# Phase 5B Codex implementation readiness gate

## Gate

Implementation is allowed only after these docs are reviewed.

## Checklist

- [ ] Source cards exist.
- [ ] Evidence matrix exists.
- [ ] Runtime feature availability matrix exists.
- [ ] Safety/fallback matrix exists.
- [ ] Model loading matrix exists.
- [ ] Telemetry contamination matrix exists.
- [ ] Integration method decision exists.
- [ ] All Phase 5B contracts exist.
- [ ] All Phase 5C implementation specs exist.
- [ ] Phase 5D Codex implementation prompt exists.
- [ ] Offline/runtime boundary explicitly blocks `weights_only=False` runtime loading.
- [ ] Telemetry hook decision is reviewed.
- [ ] No code touched.
- [ ] Tests still pass.
- [ ] Readiness strict passes.
- [ ] Ubuntu validation is done.

## Candidate future implementation files

The following files are candidates only. They are not to be created in this documentation block:

```text
core/controller/neural_abr_lite.py
core/controller/neural_abr_runtime_features.py
core/controller/neural_abr_safety.py
core/controller/neural_abr_loader.py
core/controller/neural_abr_diagnostics.py
tests/test_neural_abr_controller.py
tests/test_neural_abr_runtime_features.py
tests/test_neural_abr_safety_fallback.py
tests/test_neural_abr_model_loading_runtime.py
tests/test_neural_abr_registry.py
tests/test_neural_abr_fake_smoke.py
```

## Future implementation conditions

A future Codex implementation prompt must explicitly preserve:

- BaseController-compatible API;
- local-only bundle;
- safe CPU `state_dict` loading;
- mandatory action mask;
- safety guard;
- classical fallback;
- diagnostic-only telemetry;
- no benchmark/ranking.
