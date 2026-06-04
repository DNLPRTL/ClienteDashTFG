# Phase 5B model loading security contract

## Purpose

The future model loader must avoid unsafe machine-learning model loading behavior.

## Required rules

- Only load from a local bundle.
- No remote URL.
- No `torch.hub`.
- No arbitrary pickle.
- No `weights_only=False` in runtime.
- Instantiate architecture from trusted local repo code.
- Validate sha256 before model loading.
- Validate schema versions before inference.
- Load `state_dict` with safe CPU loading:

```python
torch.load(path, map_location="cpu", weights_only=True)
```

## PyTorch compatibility

If the installed PyTorch version does not support safe loading, runtime must fail closed and fallback. A future dev-only compatibility mode would require explicit documentation and must not be enabled by default.

## ONNX status

ONNX Runtime is deferred. It may be considered later as a migration option, but Phase 5 does not require ONNX and does not add `.onnx` artifacts to Git.

## Threat model

The bundle is trusted only if it is local, hash-validated, schema-validated and produced by the documented Phase 4 export pipeline. Architecture code is trusted only from the local repository.
