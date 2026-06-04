# Source card 04: ABRL Facebook candidate scoring deployment

## Title

Real-world Video Adaptation with Reinforcement Learning.

## Authors

Hongzi Mao, Shannon Chen, Drew Dimmery, Shaun Singh, Drew Blaisdell, Yuandong Tian, Mohammad Alizadeh, Eytan Bakshy.

## Year

2019/2020 context.

## Venue/type

Reinforcement Learning for Real Life Workshop, ICML; production-oriented research source.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

The source supports per-representation scoring because production videos can have arbitrary bitrate encodings. A fixed neural output head is a poor fit for arbitrary ladders.

## Runtime integration pattern

The policy produces one priority value per bitrate encoding. Deployment required additional safety and interpretability work.

## Runtime inputs

The source uses playback and encoding information such as buffer, prediction and candidate chunk/encoding data. DashClientModular4 must use only inputs available before the decision.

## Runtime action/output

Priority/score per valid encoding, then selection over available encodings.

## Safety/fallback/action mask

The key transfer is candidate-specific scoring over valid encodings. Safety and interpretability remain necessary before deployment.

## Latency/compute/deployment assumptions

The original production environment is not copied. Phase 5 keeps a small CPU-first scorer and modest claims.

## What transfers to DashClientModular4

- Score each candidate representation.
- Do not assume a fixed output head.
- Keep output tied to current MPD ladder.
- Keep claims modest and diagnostic-only.

## What must not be copied

- Full RL training framework.
- Constrained Bayesian reward shaping.
- Production improvement claims.

## Phase 5 docs affected

- `phase5a2_integration_method_decision.md`
- `phase5b_controller_integration_contract.md`
- `phase5b_action_mask_contract.md`

## Memory/defense usage

Use this source to defend the Candidate Scorer architecture and to explain why no Phase 5 ranking is claimed.

## Final decision

Transfer per-candidate scoring and production humility. Do not copy the production RL system.
