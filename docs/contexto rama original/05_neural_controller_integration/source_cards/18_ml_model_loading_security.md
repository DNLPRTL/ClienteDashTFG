# Source card 18: ML model loading security

## Title

On the (In)Security of Loading Machine Learning Models.

## Authors

Not recorded in the provided Phase 5 distillation.

## Year

2025/2026 technical/security source.

## Venue/type

Security research / technical reference for model loading risk.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

The source warns that model loading can execute unsafe behavior when arbitrary pickle loading is allowed.

## Runtime integration pattern

Separate trusted architecture code from local weight tensors. Avoid full-object model loading from untrusted artifacts.

## Runtime inputs

Local model artifact path and trusted repo architecture code.

## Runtime action/output

Loaded `state_dict` or fail-closed fallback. No ABR action is produced by this source.

## Safety/fallback/action mask

Unsafe or unsupported loading must disable neural and fallback. This is part of runtime safety.

## Latency/compute/deployment assumptions

Security is prioritized over convenience. Prototype-only shortcuts are not allowed in runtime.

## What transfers to DashClientModular4

- Local-only bundle.
- Architecture from trusted repo code.
- No untrusted artifacts.
- No `weights_only=False`.
- Fail closed if safe loading is unavailable.

## What must not be copied

- Exploit details.
- Any pattern that relies on arbitrary pickle execution.

## Phase 5 docs affected

- `phase5a1_model_loading_matrix.md`
- `phase5b_model_loading_security_contract.md`
- `phase5b_error_handling_contract.md`

## Memory/defense usage

Use this source to defend the bundle loading threat model.

## Final decision

Transfer the safe loading threat model. Reject full pickle model loading.
