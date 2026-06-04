# Source card 22: PyTorch model loading reference

## Title

PyTorch 2.12 model loading documentation.

## Authors

PyTorch maintainers.

## Year

2026 documentation context.

## Venue/type

Technical reference only.

## Phase 5 triage

TECHNICAL_REFERENCE_ONLY.

## Why this source matters for integration

The PyTorch documentation defines the safe CPU loading pattern needed for local `state_dict` inference.

## Runtime integration pattern

Use trusted architecture code from the repository and load tensor weights from the local bundle.

## Runtime inputs

Local `model_state.pt` path.

## Runtime action/output

Loaded tensors/state_dict or fail-closed fallback.

## Safety/fallback/action mask

Safe loading is a prerequisite before any action mask or inference. If loading is unsupported or fails, fallback must run.

## Latency/compute/deployment assumptions

The loader must force CPU with `map_location="cpu"` and avoid GPU requirements.

## What transfers to DashClientModular4

Required future runtime pattern:

```python
torch.load(path, map_location="cpu", weights_only=True)
```

## What must not be copied

- Loading untrusted data.
- Full-object pickle loading.
- `weights_only=False` at runtime.

## Phase 5 docs affected

- `phase5a1_model_loading_matrix.md`
- `phase5b_model_loading_security_contract.md`
- `phase5b_cpu_inference_contract.md`

## Memory/defense usage

Use this reference to defend local-only safe loading in the implementation chapter.

## Final decision

Use as a technical reference for PyTorch state_dict loading.
