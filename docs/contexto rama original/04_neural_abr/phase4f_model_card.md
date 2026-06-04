# Phase 4F Model Card

Model: NeuralABR-Lite Candidate Scorer.

This is a local-only export/inference bundle for Phase 4F. It is not integrated into the DASH client and no neural controller is registered.

- Training method: `behavior_cloning` / `imitation_learning`
- Teacher: `robust_mpc`
- Action: `representation_index`
- Reward context: `qoe_linear_v1 / reward_n`
- Device: `cpu`
- Trace count: `210`
- Validation valid action rate: `1.0`
- OOD diagnostic valid action rate: `1.0`
- Epochs: `20`
- Batch size: `32`

No benchmark/ranking, SOTA, or real-world validation claim is made. Phase 4G will decide whether Phase 5 integration is allowed.
