# Phase 5A1 safety fallback matrix

## Source mapping

| Source | Safety/fallback lesson | Phase 5 transfer |
|---|---|---|
| SafeSABR | Check `raw_action`, execute `safe_action`, downshift on unsafe action, lowest if none feasible | Implement later a post-inference safety guard and intervention telemetry |
| Hybrid ABR | Decision-level fallback to rule-based/RobustMPC when neural decision is not preferred | Enumerate fallback reasons and keep final authority outside the neural score |
| A2BR | Domain knowledge and heuristics improve online safety | Classical fallback is a safety prior; no online adaptation in Phase 5 |
| Ahaggar | Client keeps lightweight heuristic while ML provides guidance | Neural scorer is advisory/scoring, not a single point of failure |
| BayesMPC | Conservative lower-bound estimates can feed robust decisions | Safety guard may later use conservative throughput estimates |
| Fugu | Learned component is bounded by MPC | Keep neural bounded by classical logic |
| DeepBuffer | Invalid actions are masked before selection | All invalid candidates are filtered before argmax |

## Fallback triggers

The future controller must fallback or disable neural on:

- bundle missing;
- manifest invalid;
- hash mismatch;
- schema mismatch;
- `model_state.pt` load failure;
- PyTorch unavailable;
- unsupported `torch.load` safe mode;
- feature build failure;
- missing required feature;
- action mask invalid;
- all actions invalid;
- NaN/Inf score;
- selected action masked out;
- safety guard rejects `raw_action`;
- inference timeout;
- runtime exception.

## Fallback chain

Preferred fallback order:

```text
1. robust_mpc if available
2. mpc or rate_based if robust_mpc is unavailable
3. bba or min_rate as conservative emergency
4. lowest valid representation as final emergency
```

Fallback must be visible in telemetry. Fallback is diagnostic-only and not benchmark evidence.
