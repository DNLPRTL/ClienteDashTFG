# Source card: survey_learning_has2025

## Bibliographic data

- Title: A Review of Learning-Based Methods for Adaptive Video Streaming over HTTP
- Authors: Hala Amer, Mohamed S. Hassan, Mahmoud H. Ismail
- Year: accepted/published context 2025
- Venue: IEEE Access author version / accepted publication
- DOI / stable URL: citation info in PDF indicates DOI 10.1109/ACCESS.2025.3582850
- Local PDF: Surveys de 2025.pdf
- Code URL: not applicable
- Dataset URL: not applicable

## Method family

- Family: survey of learning-based methods for HTTP adaptive video streaming.
- Client-side / server-side / hybrid: covers multiple positions in the streaming pipeline.
- Learning type: reviews ML/DL/RL and related learning-based methods.
- Relation to ABR: gives taxonomy and context for adaptive encoding, bandwidth optimization and quality adaptation.

## State / action / reward

### State

Not a controller. It describes common HAS/DASH decision inputs such as channel quality, client buffer fullness, device capabilities, content characteristics and historical data.

### Action

Not a controller. For ABR papers covered by the survey, the action is generally selecting a quality/bitrate representation for each segment.

### Reward / QoE

Not a specific reward. The survey frames QoE as uninterrupted, high-quality playback while considering video quality, network conditions, bandwidth limitations and device constraints.

## Model and training

- Architecture: not applicable.
- Training method: not applicable.
- Expert / teacher: not applicable.
- Online interaction: not applicable.
- Offline data: not applicable.
- Fine-tuning: not applicable.
- Compute requirements: not applicable.

## Data and evaluation

- Datasets / traces: survey references many works and categories.
- Train split: not applicable.
- Validation split: not applicable.
- Test split: not applicable.
- OOD split: not applicable.
- Baselines: not a single evaluation.
- Evaluation type: literature review.
- Real-world evidence: secondary, through cited works.

## Relevance to DashClientModular4

### What this source justifies

- DASH/HAS leaves adaptation logic open; therefore a custom ABR controller is a valid research target.
- Learning-based ABR is one branch among many, not the only answer.
- A memory chapter can classify ML approaches across encoding, bandwidth optimization and quality adaptation.
- The TFG can situate NeuralABR-Lite as a lightweight learning-based quality adaptation method.

### What this source does NOT justify

- It does not justify any particular algorithm by itself.
- It does not replace primary papers such as Pensieve, Comyco, Puffer, ABRL, SODA or CausalSim.
- It does not justify large models or heavy dependencies.
- It does not justify claims stronger than the primary sources.

### Risks for this TFG

- Leakage risk: low.
- Future-information risk: low.
- Reward hacking risk: low.
- Overfitting risk: low.
- Hardware risk: low.
- Dependency risk: low.

## Decision impact

- Method score: 2/3 as taxonomy, 0/3 as implementation source.
- Feasibility score: 3/3 for memory support.
- Defense strength: 2/3.
- Implementation consequence: use this as state-of-the-art framing, not as method selection evidence.

## Memory / thesis usage

- Chapter: Estado del arte.
- Figure/table candidate: taxonomy of learning-based HAS methods.
- Defense point: the implementation is deliberately scoped to client-side ABR quality adaptation.
