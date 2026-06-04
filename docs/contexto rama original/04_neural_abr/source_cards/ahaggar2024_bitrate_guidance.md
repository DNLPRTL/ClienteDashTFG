# Source card: ahaggar2024_bitrate_guidance

## Bibliographic data

- Title: Bitrate Adaptation and Guidance With Meta Reinforcement Learning
- Authors: Abdelhak Bentaleb, May Lim, Mehmet N. Akcay, Ali C. Begen, Roger Zimmermann
- Year: 2024
- Venue: IEEE Transactions on Mobile Computing, Vol. 23, No. 11
- DOI / stable URL: https://doi.org/10.1109/TMC.2024.3376560
- Local PDF: Bitrate Adaptation and Guidance With Meta Reinforcement Learning.pdf
- Code URL: paper references Ahaggar bitrate guidance repository, but it is not adopted as a dependency for this TFG.
- Dataset URL: not used as implementation dependency.

## Method family

- Family: server-side bitrate guidance with meta-RL.
- Client-side / server-side / hybrid: hybrid; server-side model guides client-side heuristic ABR.
- Learning type: multi-agent A2C, clipped DPPO, Adam, MAML-style meta-RL.
- Relation to ABR: the model does not fully replace the client controller; it provides quality-aware bitrate guidance.

## State / action / reward

### State

Ahaggar uses network conditions, client status, device resolution and streamed content as model inputs. It leverages CMCD/CMSD metadata exchange and models the problem as a POMDP with belief states over histories of observations/actions.

### Action

The model provides bitrate guidance, selecting the minimum bitrate among available options above which the next higher bitrate improves perceptual quality only insignificantly for the specific device resolution.

### Reward / QoE

The objective is quality-aware and resolution-aware. The paper uses VMAF as a full-reference perceptual quality metric and optimizes user experience while reducing bandwidth consumption.

## Model and training

- Architecture: server-side neural model for multiple clients/agents.
- Training method: offline meta-training and online meta-testing/inference; A2C with clipped DPPO and MAML-style meta-RL.
- Expert / teacher: none.
- Online interaction: yes, in the sense of guidance adaptation/inference.
- Offline data: heterogeneous network environments.
- Fine-tuning: fast adaptation to unseen environments with a small number of shots.
- Compute requirements: intentionally placed server-side to exploit server compute and keep clients lightweight.

## Data and evaluation

- Datasets / traces: real-world trace-driven experiments across multiple clients, varied network conditions and device resolutions.
- Train split: meta-training over heterogeneous environments.
- Validation split: not directly reusable for this TFG.
- Test split: unseen/mixed environments.
- OOD split: unseen network/device conditions.
- Baselines: client-side heuristic and competing ABR/guidance schemes.
- Evaluation type: real-world trace-driven experiments on an open-source system.
- Real-world evidence: trace-driven, heterogeneous multi-client evaluation; not a local DashClientModular4 deployment.

## Relevance to DashClientModular4

### What this source justifies

- The IA component can be a guidance/advisor layer, not necessarily a full replacement of classical ABR.
- A lightweight client plus heavier server-side logic is a valid design pattern, although this TFG will remain client-local unless later specs say otherwise.
- Device/content/context features are valuable, but only if observable and available without leakage.
- VMAF is academically relevant but remains deferred in this TFG because Phase 3.5 explicitly deferred VMAF.

### What this source does NOT justify

- It does not justify implementing server-side CMCD/CMSD guidance now.
- It does not justify requiring VMAF in Phase 4.
- It does not justify DPPO/MAML as mandatory.
- It does not justify heavy dependencies such as Ray/RLlib/TensorFlow-style stacks in a CPU-first Windows project.

### Risks for this TFG

- Leakage risk: medium if server/client metadata is assumed available without contract.
- Future-information risk: medium if content quality metrics are used in runtime features.
- Reward hacking risk: medium for meta-RL.
- Overfitting risk: medium/high.
- Hardware risk: high for cloning; low for adopting the guidance concept.
- Dependency risk: high for direct implementation.

## Decision impact

- Method score: 3/3 for guidance/fallback concept; 1/3 for direct implementation.
- Feasibility score: 3/3 if used conceptually, 0/3 if cloned.
- Defense strength: 3/3.
- Implementation consequence: NeuralABR-Lite may be specified as a recommendation/guidance layer with a safety wrapper.

## Memory / thesis usage

- Chapter: Estado del arte; Arquitectura IA híbrida; Limitaciones.
- Figure/table candidate: "policy replacement vs guidance" comparison.
- Defense point: the thesis deliberately chooses a small client-side/guidance-compatible model instead of a server-side meta-RL system.
