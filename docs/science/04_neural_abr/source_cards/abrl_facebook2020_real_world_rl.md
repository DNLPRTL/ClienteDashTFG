# Source card: abrl_facebook2020_real_world_rl

## Bibliographic data

- Title: Real-world Video Adaptation with Reinforcement Learning
- Authors: Hongzi Mao, Shannon Chen, Drew Dimmery, Shaun Singh, Drew Blaisdell, Yuandong Tian, Mohammad Alizadeh, Eytan Bakshy
- Year: 2019/2020 context, ICML RL4RealLife workshop paper
- Venue: Reinforcement Learning for Real Life Workshop, ICML
- DOI / stable URL: workshop paper; stable source from uploaded PDF
- Local PDF: Real-world Video Adaptation with Reinforcement Learning.pdf
- Code URL: not used as an implementation dependency for this TFG
- Dataset URL: not used as an implementation dependency for this TFG

## Method family

- Family: Reinforcement learning for production ABR.
- Client-side / server-side / hybrid: client-side player policy deployed inside Facebook web video platform.
- Learning type: policy gradient RL with custom variance reduction and constrained Bayesian optimization for reward shaping.
- Relation to ABR: direct ABR bitrate selection, but with a production-specific architecture and safety translation layer.

## State / action / reward

### State

The paper defines the RL state for each chunk as:

```text
s_t = (x_t, o_t, n_t_vector)
```

where:

- `x_t`: bandwidth prediction for the next chunk;
- `o_t`: current buffer occupancy;
- `n_t_vector`: vector of file sizes for the next video chunk, one entry per available bitrate.

### Action

The action is the next bitrate / encoding choice. The paper’s key design is that the number of available encodings can vary by video. Instead of a fixed output head, the policy network is copied with shared weights for every bitrate candidate and outputs a priority score `q_i` for each candidate. A softmax over the priority values gives a probability distribution over all valid bitrates.

### Reward / QoE

The reward is a weighted combination of selected bitrate, stall duration and stall count:

```text
r_t = positive bitrate term - stall duration penalty + stall count term
```

The paper explicitly notes that the reward weights cannot simply be predetermined because the goal is multidimensional: higher bitrate, lower stall time and lower stall count. It therefore uses constrained Bayesian optimization for reward shaping.

## Model and training

- Architecture: shared candidate-scoring neural network copied over available bitrate encodings, followed by softmax.
- Training method: policy gradient RL, variance reduction, simulator trained from production-collected traces.
- Expert / teacher: none; RL learns from simulated rollouts.
- Online interaction: production deployment after offline/simulated training and policy translation.
- Offline data: large production video traces.
- Fine-tuning: not adopted as a requirement for this TFG.
- Compute requirements: production-scale training and deployment context; not a CPU-first undergraduate implementation target.

## Data and evaluation

- Datasets / traces: traces from Facebook’s production web video platform.
- Train split: production traces used for simulator training; exact TFG-compatible split not directly reusable.
- Validation split: production methodology, not reusable directly.
- Test split: one-week worldwide deployment.
- OOD split: not formalized as a TFG-style OOD split.
- Baselines: carefully tuned human-engineered production ABR algorithm.
- Evaluation type: simulation plus real production deployment.
- Real-world evidence: week-long worldwide deployment with more than 30 million video streaming sessions; reported gains are modest but real: at least 1.6% video quality improvement and 0.4% stall improvement.

## Relevance to DashClientModular4

### What this source justifies

- Candidate-scoring over available representations is the strongest architectural clue for NeuralABR-Lite.
- A neural ABR should never output an arbitrary bitrate outside the available ladder.
- A small shared scorer can support ladders with different numbers of representations.
- RL needs more than an off-the-shelf algorithm: variance reduction, reward shaping, safety and interpretability matter.
- Modest real-world gains are still academically valuable; no SOTA claim is needed.

### What this source does NOT justify

- It does not justify implementing production-scale RL in this TFG.
- It does not justify using PPO/A3C by inertia.
- It does not justify changing the already closed `qoe_linear_v1` reward without versioning.
- It does not justify making real-world deployment claims from local trace-driven validation.

### Risks for this TFG

- Leakage risk: medium if production trace assumptions are copied without causal analysis.
- Future-information risk: medium if next-chunk sizes are used without proving they are available in DashClientModular4.
- Reward hacking risk: high for direct RL; mitigated by using imitation learning first.
- Overfitting risk: high if trained on narrow traces.
- Hardware risk: high for production RL; low for adopting only the candidate-scoring architecture.
- Dependency risk: medium/high if copying the original training setup; low if translating the architecture to PyTorch CPU later.

## Decision impact

- Method score: 3/3 for candidate-scoring design.
- Feasibility score: 2/3 if used as architecture only; 0/3 if cloned as production RL.
- Defense strength: 3/3.
- Implementation consequence: NeuralABR-Lite should prefer a shared candidate scorer over a fixed softmax head.

## Memory / thesis usage

- Chapter: Estado del arte; Diseño del controlador IA; Amenazas a la validez.
- Figure/table candidate: candidate-scoring architecture for variable MPD ladders.
- Defense point: production RL gains required custom engineering and were modest, so the TFG chooses a smaller reproducible subset.
