# Source card: into_the_wild2025_real_world_testing

## Bibliographic data

- Title: Into the Wild: Real-World Testing for ML-Based ABR
- Authors: Benjamin Hoffman, Alexander Dietmüller, Ayush Mishra, Laurent Vanbever
- Year: 2025
- Venue: PACMI 2025
- DOI / stable URL: https://doi.org/10.1145/3766882.3767186
- Local PDF: into the wild.pdf
- Code URL: ABR-Arena is announced as community infrastructure; not adopted as dependency in this TFG.
- Dataset URL: not used as implementation dependency.

## Method family

- Family: real-world testing / sim-to-real / evaluation methodology.
- Client-side / server-side / hybrid: evaluation platform for ABR algorithms.
- Learning type: not a new policy; evaluates ML-based ABR generalization.
- Relation to ABR: warns that ML-based ABR can perform well in simulation or one platform but fail in broader Internet conditions.

## State / action / reward

### State

Not applicable as a controller. The paper focuses on testing contexts and geographical/network diversity.

### Action

Not applicable as a controller. ABR-Arena evaluates ABR algorithm behavior across regions.

### Reward / QoE

QoE metrics depend on tested ABR algorithms; the paper’s role is methodological.

## Model and training

- Architecture: testing infrastructure, not a model architecture.
- Training method: not applicable.
- Expert / teacher: not applicable.
- Online interaction: real Internet testing across global regions.
- Offline data: not a training source for this TFG.
- Fine-tuning: not applicable.
- Compute requirements: platform/deployment infrastructure, not a CPU-first local model.

## Data and evaluation

- Datasets / traces: global real-world testing environments.
- Train split: not applicable.
- Validation split: not applicable.
- Test split: distributed real-world tests.
- OOD split: geographical and deployment diversity is the central issue.
- Baselines: ML-based ABR methods trained/tested on narrower platforms such as Puffer.
- Evaluation type: real-world testing methodology.
- Real-world evidence: shows that testing in a single real-world environment can still generalize poorly due to geographical diversity, survivorship bias and platform coverage limitations.

## Relevance to DashClientModular4

### What this source justifies

- Phase 4 must not claim global real-world validity.
- "Tested on real traces" is not equivalent to "validated on the Internet".
- OOD and region/regime diversity must be explicit in the evidence matrix and memory.
- Even Puffer-like evaluation has limitations.

### What this source does NOT justify

- It does not require building ABR-Arena.
- It does not require cloud deployment.
- It does not justify delaying the TFG until real-world global testing exists.
- It does not justify rejecting IA; it just constrains claims.

### Risks for this TFG

- Leakage risk: low directly; high relevance to validity.
- Future-information risk: low.
- Reward hacking risk: medium if synthetic success is overclaimed.
- Overfitting risk: high if validation context is narrow.
- Hardware risk: low for methodology; high for cloning global platform.
- Dependency risk: low.

## Decision impact

- Method score: 3/3 for threat-to-validity control.
- Feasibility score: 3/3 as documentation constraint; 0/3 as implementation target.
- Defense strength: 3/3.
- Implementation consequence: all Phase 4 evaluation statements must say "trace-driven controlled validation", not "real-world proof".

## Memory / thesis usage

- Chapter: Evaluación; Amenazas a la validez; Conclusiones.
- Figure/table candidate: sim -> trace-driven -> Puffer-like -> global real-world validity ladder.
- Defense point: the TFG is intentionally conservative about real-world claims.
