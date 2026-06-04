# Source card: sabr2025_bc_rl_finetuning

## Bibliographic data

- Title: SABR: A Stable Adaptive Bitrate Framework Using Behavior Cloning Pretraining and Reinforcement Learning Fine-Tuning
- Authors: Pengcheng Luo, Yunyang Zhao, Bowen Zhang, Genke Yang, Boon-Hee Soong, Chau Yuen
- Year: 2025/2026 frontier source in the uploaded PDF set
- Venue: uploaded PDF does not expose a final venue/DOI in the parsed first page
- DOI / stable URL: not visible in uploaded PDF text
- Code URL: https://github.com/luopeng69131/SABR
- Dataset URL: https://github.com/luopeng69131/ABRBench
- Local PDF: local-only, not committed: `C:\Users\danie\Documents\TFG\_literature\phase4_AI\03_wave3_frontier_surveillance\pdfs\SABR.pdf`

## Method family

- Family: behavior cloning / supervised pretraining + reinforcement learning fine-tuning.
- Learning type: BC/pretraining followed by PPO fine-tuning.
- Main contribution: stable ABR learning over wide trace distributions using ABRBench-3G and ABRBench-4G+, including dedicated OOD test sets.
- Client-side / server-side / hybrid: ABR policy model for bitrate selection; implementation/evaluation is trace-driven simulator-based.

## State / action / reward

### State

The paper states that its MDP state/action/reward/state transition are consistent with Pensieve. In implementation, Pensieve/Comyco-like 6-by-8 inputs are flattened into a 48-dimensional vector.

Expected practical interpretation for this TFG:

- recent throughput history;
- recent download-time history;
- next chunk sizes when available through the video manifest/artifact contract;
- current playback buffer;
- last selected bitrate / representation;
- chunks remaining for VoD;
- no hidden future not available online.

### Action

- Discrete bitrate/representation choice.
- ABRBench-3G ladder: `{300, 750, 1200, 1850, 2850, 4300}` kbps.
- ABRBench-4G+ ladder: `{1000, 2500, 5000, 8000, 16000, 40000}` kbps.
- For DashClientModular4, this must be converted to `representation_index` within the current MPD ladder.

### Reward / QoE

The paper uses a QoE objective of the form:

```text
sum quality
- smoothness penalty
- rebuffering penalty
```

It uses bitrate as the quality mapping and different rebuffering penalty coefficients for ABRBench-3G and ABRBench-4G+.

For this TFG, reward must remain `qoe_linear_v1 / reward_n` from Phase 3.5 unless a new version is explicitly created.

## Model and training

- BC/pretraining is implemented in PyTorch.
- RL fine-tuning uses PPO from Stable-Baselines3.
- Parallel sample collection uses 4 vectorized environments.
- Actor network in the uploaded PDF: `[48, tanh, 64, tanh, 64, 6]`.
- Critic network: `[48, tanh, 64, tanh, 64, 1]`.
- PPO fine-tuning parameters in the uploaded PDF include 244 iterations, 10 epochs/update, 512 rollout steps/environment, batch size 64, learning rate `3e-4`, clipping `0.2`, discount `0.99`, and GAE `0.95`.

## Data and evaluation

- Datasets / traces:
  - ABRBench-3G: training 1828 traces; test sets include FCC-16, FCC-18, Oboe, Puffer-21, Puffer-22; OOD set includes HSR.
  - ABRBench-4G+: training 262 traces; test sets include Lumos 4G, Lumos 5G, Solis Wi-Fi; OOD sets include Ghent and Lab.
- Baselines:
  - BB, BOLA, RobustMPC, QUETRA, Pensieve, Comyco, NetLLM.
- Evaluation:
  - trace-driven simulator;
  - learning methods trained multiple times and averaged;
  - average-rank comparison across trace sets.

## Relevance to DashClientModular4

### What this source justifies

- The final TFG method can use behavior cloning / imitation learning as a serious recent direction, not merely as a simplification.
- Optional small PPO fine-tuning can be considered only after behavior cloning works, but must not be the base by inertia.
- OOD test sets are central to a credible neural ABR evaluation.
- A very small MLP policy is academically acceptable.

### What this source does NOT justify

- It does not justify launching PPO before closing state/action/reward and dataset contracts.
- It does not justify using the project's old dry-runs as training data.
- It does not justify claiming real-world deployment.
- It does not force Stable-Baselines3 as a dependency for the TFG.

### Risks for this TFG

- PPO fine-tuning can be high-variance and may reward-hack.
- ABRBench ladders may not match the local MPD ladder.
- Trace-driven results do not imply real-world superiority.
- SB3/vector-env dependencies are optional and should not become a Phase 4 gate.

## Decision impact

- Strongly supports: NeuralABR-Lite as behavior-cloned candidate scorer.
- Supports as optional extension: BC pretraining + tiny PPO fine-tune.
- Blocks: PPO-first approach.
- Implementation consequence:
  - start with supervised imitation;
  - keep a small MLP;
  - reserve RL fine-tuning only as a non-blocking extension after A2/B/C specs.

## Memory / thesis usage

- State of the art: modern BC + RL ABR.
- Method decision: why PPO is not selected as base.
- Evaluation: benchmark/OOD design inspiration.
- Defense point: a recent paper itself uses BC before PPO, so the TFG's CPU-first behavior-cloning route is scientifically aligned.
