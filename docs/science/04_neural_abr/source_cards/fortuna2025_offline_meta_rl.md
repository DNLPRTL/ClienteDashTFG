# Source card: fortuna2025_offline_meta_rl

## Bibliographic data

- Title: Optimizing Adaptive Video Streaming: Offline Reinforcement Learning and Meta-Learning in Diverse Networks
- Authors: Ling Yi, Yongbin Qin, Ruizhang Huang
- Year: 2025
- Venue: IEEE Transactions on Multimedia, Vol. 27, 2025
- DOI / stable URL: `10.1109/TMM.2025.3604930`
- Local PDF: local-only, not committed: `C:\Users\danie\Documents\TFG\_literature\phase4_AI\03_wave3_frontier_surveillance\pdfs\Fortuna.pdf`

## Method family

- Family: offline reinforcement learning + meta-learning + curriculum learning.
- Learning type: actor-critic / meta-RL with offline data and online adaptation.
- Main contribution: address heavy-tailed Internet behavior, diversity, unpredictability and heterogeneous QoE objectives with offline/meta RL and TCP-aware features.

## State / action / reward

### State

The uploaded paper describes a state with seven variables:

- throughput `C_t`;
- chunk download time `d_k(R_k) / C_k`;
- next chunk sizes `R_{n+1}`;
- RTT;
- buffer size `B_t`;
- remaining chunks `N`;
- current/previous chunk bitrate `R_n`.

For DashClientModular4:

- throughput, download time, buffer, chunk size, remaining chunks and last bitrate are plausible;
- RTT/TCP CWND are not currently part of the Phase 3.5 contract and must not be added unless Phase 4B explicitly extends runtime telemetry.

### Action

- Discrete bitrate selection.
- The paper uses output masking so that the actor's probability distribution includes only bitrate levels supported by the current video.

For DashClientModular4:

- action mask maps directly to valid `representation_index` values in the MPD.

### Reward / QoE

- Reward is set according to QoE metric components.
- The paper discusses balancing video quality and rebuffering and later considers TCP/network effects.
- For this TFG, the reward must remain Phase 3.5 `qoe_linear_v1 / reward_n`, not an unversioned new QoE.

## Model and training

- Actor-critic method.
- One hidden layer, 128 convolution kernels and fully connected network for feature extraction.
- Convolution kernel size 4, stride 1.
- Offline phase learns from diverse offline data and expert data.
- Online phase increases streaming-session complexity with curriculum learning.
- Meta-learning optimizes initialization for fast adaptation.
- Includes TCP congestion-control features such as RTT/CWND to account for interactions with network transport.

## Data and evaluation

- Trace-driven and real-world scenarios.
- Generalization reported across 3G, 4G, 5G, WiFi, synthetic networks and different video streams.
- Reports:
  - learning efficiency improvements above 7.5% to 4x;
  - stall-time reductions of 4.6% to 14.2%.

## Relevance to DashClientModular4

### What this source justifies

- Offline RL is relevant in 2025, but it needs representative offline data and careful adaptation logic.
- Heavy-tailed Internet behavior must be explicitly discussed in the memory.
- Action masking is a required safety mechanism.
- TCP/application interactions are a real threat to naive trace replay.

### What this source does NOT justify

- It does not justify offline RL as the TFG base without a valid logged dataset.
- It does not justify collecting training data from dry-runs legacy.
- It does not justify adding RTT/CWND features without instrumentation and state contract.
- It does not justify claiming real-world robustness from trace-driven training.

### Risks for this TFG

- High data requirement.
- High implementation complexity.
- Potential mismatch with CPU-first constraints.
- Potential leakage if expert/offline data are not split correctly.
- TCP features unavailable in current client/runtime.

## Decision impact

- Strongly supports: dataset contract, action masking, caution with offline RL.
- Weakly supports: future extension toward offline/meta RL.
- Blocks: full Fortuna-like implementation as Phase 4 base.
- Implementation consequence:
  - keep offline RL out of the core plan;
  - use this source in `method_feasibility_matrix.md` to justify why the selected method is smaller.

## Memory / thesis usage

- State of the art: offline/meta RL frontier.
- Threats to validity: heavy tails and transport-layer interactions.
- Defense point: excluding offline RL is a reasoned feasibility decision, not lack of ambition.
