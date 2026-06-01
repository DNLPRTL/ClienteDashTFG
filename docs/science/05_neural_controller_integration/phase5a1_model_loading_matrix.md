# Phase 5A1 model loading matrix

| Option | Benefits | Risks | Phase 5 decision |
|---|---|---|---|
| PyTorch `state_dict` local-only | Matches Phase 4 bundle, CPU-first, can use trusted repo architecture, supports `weights_only=True` | Requires PyTorch availability and schema checks | ACCEPTED for Phase 5 |
| Full pickle model | Convenient for prototypes | Arbitrary pickle loading risk, architecture embedded in untrusted artifact, hard to audit | REJECTED |
| ONNX Runtime | Portable future inference option, CPU provider available | Adds dependency and conversion contract not needed now | DEFERRED |

## Required Phase 5 loading constraints

- Load only from a local bundle directory configured in a future implementation.
- Keep the bundle outside the repository.
- Validate manifest schema and sha256 hashes.
- Validate model family, teacher, action space, feature schema and normalization schema.
- Instantiate architecture from trusted local repo code.
- Load weights with:

```python
torch.load(path, map_location="cpu", weights_only=True)
```

- Do not load remote URLs.
- Do not use `torch.hub`.
- Do not use `weights_only=False` in runtime.
- If the installed PyTorch version does not support safe loading, fail closed and fallback unless a future, explicitly documented dev-only compatibility mode is approved.
