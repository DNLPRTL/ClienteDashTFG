# Source card: survey_pipeline2025

## Bibliographic data

- Title: An End-to-End Pipeline Perspective on Video Streaming in Best-Effort Networks: A Survey and Tutorial
- Authors: Leonardo Peroni, Sergey Gorinsky
- Year: 2025
- Venue: ACM Computing Surveys, Vol. 57, No. 12, Article 322
- DOI / stable URL: https://doi.org/10.1145/3742472
- Local PDF: Surveys de 2025 2.pdf
- Code URL: not applicable
- Dataset URL: not applicable

## Method family

- Family: end-to-end video streaming survey/tutorial.
- Client-side / server-side / hybrid: covers the whole pipeline; ABR is at the distribution stage.
- Learning type: reviews intuition-based, theory-based and ML-based designs; includes RL, IL, SL and UL categories.
- Relation to ABR: positions ABR inside the HAS distribution pipeline with CDN support and QoE modeling.

## State / action / reward

### State

Not a controller. The survey contextualizes ABR decisions using client/network/content context in the distribution stage.

### Action

Not a controller. ABR action is generally representation/bitrate selection in HAS.

### Reward / QoE

Not a single reward. The survey includes QoE modeling and pipeline-wide trade-offs.

## Model and training

- Architecture: not applicable.
- Training method: not applicable.
- Expert / teacher: not applicable.
- Online interaction: not applicable.
- Offline data: not applicable.
- Fine-tuning: not applicable.
- Compute requirements: not applicable.

## Data and evaluation

- Datasets / traces: not a single experimental dataset; reviews over 200 papers.
- Train split: not applicable.
- Validation split: not applicable.
- Test split: not applicable.
- OOD split: not applicable.
- Baselines: not applicable.
- Evaluation type: survey/tutorial.
- Real-world evidence: secondary, through reviewed platform practices.

## Relevance to DashClientModular4

### What this source justifies

- It gives the best memory-level frame for the end-to-end video streaming pipeline.
- It helps explain why the project focuses on one non-normative component: client-side ABR logic.
- It gives a modern taxonomy: intuition, theory and ML; with ML subdivided into RL, IL, SL and UL.
- It supports figures/tables connecting DashClientModular4 to ingestion, processing and distribution.

### What this source does NOT justify

- It does not pick the ABR IA method.
- It does not justify copying any large system.
- It does not replace primary method papers.
- It does not justify benchmark/ranking in Phase 4.

### Risks for this TFG

- Leakage risk: low.
- Future-information risk: low.
- Reward hacking risk: low.
- Overfitting risk: low.
- Hardware risk: low.
- Dependency risk: low.

## Decision impact

- Method score: 2/3 for taxonomy and thesis framing.
- Feasibility score: 3/3 for memory and defense.
- Defense strength: 3/3.
- Implementation consequence: include a pipeline boundary diagram showing that Phase 4 modifies only ABR policy logic.

## Memory / thesis usage

- Chapter: Estado del arte; Diseño general del sistema.
- Figure/table candidate: end-to-end HAS pipeline and position of ABR controller.
- Defense point: the project is scoped to a well-defined part of the pipeline, not a whole streaming platform.
