# MamBRA: Session-Level Bandwidth Prediction for Adaptive Video Streaming using Selective State Space Models

## 0. Ficha de archivo

- Archivo fuente: `v1_covered_4254418a-5dc6-4da1-be54-5ccdcf966b39.pdf`
- Paginas detectadas: 26
- SHA256 PDF: `bf9974fc1178d7d08d838c41cb713fe8b79cecb28236d457a62d82b5246130d1`
- Texto crudo auxiliar: `raw_text/28_mambra_2026_session_bandwidth_prediction_ssm_mamba.txt`
- Texto layout auxiliar: `raw_text_layout/28_mambra_2026_session_bandwidth_prediction_ssm_mamba_layout.txt`
- Fecha de generacion: 2026-06-09T12:33:32

## 1. Uso previsto para Fase 4-5 v1

Fuente 2026 para prediccion de bandwidth con SSM/Mamba. Relevante para Fase 4-5 v1 como candidato de predictor auxiliar/risk-aware throughput forecasting; no es necesariamente controller ABR completo.

> Nota de fidelidad: este Markdown es una extraccion tecnica densa para Codex. No es un resumen narrativo ni sustituye al PDF. Para formulas, tablas y figuras criticas, revisar siempre el PDF original.

---

## 2. Identificacion textual de primeras paginas

```text
MamBRA: Session-Level Bandwidth Prediction for
Adaptive Video Streaming using Selective State
Space Models
Jamal Hussein
University of Sulaymaniyah
Aree Mohammed
University of Sulaymaniyah
Miran Abdullah
University of Sulaymaniyah
Research Article
Keywords: SSM-Mamba, bitrate adaptation, video streaming, network bandwidth, QoE
Posted Date: May 12th, 2026
DOI: https://doi.org/10.21203/rs.3.rs-9024915/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.
Read Full License
Additional Declarations: No competing interests reported.
MamBRA: Session-Level Bandwidth Prediction for Adaptive
Video Streaming using Selective State Space Models
Jamal A. Hussein
, Aree A. Mohammed, and Miran T. Abdullah
Department of Computer, College of Science,
University of Sulaimani, KRG, Iraq
{jamal.ali, aree.ali, miran.abdullah}@univsul.edu.iq
March 6, 2026
Corresponding author:
Jamal A. Hussein
Email:
jamal.ali@univsul.edu.iq
Abstract
Live streaming is the real-time transmission of video content to an audience as it
is simultaneously recorded. This technology is frequently utilized for applications such
as covering live events and facilitating video calls. By dynamically modifying the video
quality to match network conditions and device capabilities, adaptive video streaming
provides improved Quality of Experience (QoE). However, as user demands for high
quality and low latency increase, using eﬃcient video streaming systems is getting
harder. In addition to taxing network resources, the increase in video traﬃc is lower-
ing video quality. Deep and transformer learning algorithms use data-driven methods
to optimize video delivery, enhance QoE, and lessen network congestion in order to
overcome these obstacles. Mamba utilizes the eﬃcient linear complexity of selective
state space model (SSM) mechanism to process data sequences more eﬀectively. This
paper proposes an adaptive video streaming framework (MamBRA) based on Mamba for
session-level bandwidth prediction. The model is trained in a supervised time-series
manner on disjoint user sessions to prevent information leakage and preserve temporal
structure. During inference, it leverages the linear state-space formulation of Mamba
to eﬃciently generate stable bandwidth predictions within each session. Experimen-
tal results demonstrate reduced prediction error, improved accuracy, and enhanced
temporal stability. The model achieves an overall inference accuracy of 93.94%, with
session-level accuracy reaching as high as 97.32%. Furthermore, the predicted band-
width achieves more consistent QoE scores compared to the PPO-based approach used
in Pensieve.
Keywords: SSM-Mamba, bitrate adaptation, video streaming, network bandwidth, QoE.
1
```

## 3. Metadatos PDF detectados

```json
{
  "format": "PDF 1.7",
  "title": "",
  "author": "",
  "subject": "",
  "keywords": "",
  "creator": "LaTeX with hyperref",
  "producer": "GPL Ghostscript 10.06.0",
  "creationDate": "D:20260512084543Z00'00'",
  "modDate": "D:20260512084543Z00'00'",
  "trapped": "",
  "encryption": null
}
```

## 4. Mapa de secciones detectado

- p. 7: T. Huang
- p. 7: D. Yang
- p. 7: J. Zhang
- p. 16: RMSE, NRMSE

## 5. Figuras, tablas, algoritmos, ecuaciones o teoremas detectados

- p. 5: Figure 1: The overall architecture and processing pipeline of MamBRA
- p. 7: Table 1: Enhancement of QoE through the evolution of adaptation algorithms
- p. 11: Table 2: Segment downloads, stream switching, network, and buﬀering behavior of the
- p. 12: Figure 2 illustrates the distribution of rows and sessions across the diﬀerent classes
- p. 12: Figure 2: Distribution of sessions and rows among categorical features
- p. 13: Figure 3: Dataset preparation (clean-up, normalization, sequencing and splitting)
- p. 14: Figure 4: Training and validation process of MamBRA model
- p. 16: Figure 5: Inference process of MamBRA for one session of the test data
- p. 17: Figure 6 illustrates the Huber loss and accuracy for the training and validation.
- p. 17: Figure 6: Huber loss versus accuracy
- p. 18: Figure 7 presents a performance breakdown of a model across four features: deviceOS,
- p. 19: Figure 7:
- p. 20: Figure 8:
- p. 20: Figure 9b illustrates and compares the Mean QoE scores across the four diﬀerent device
- p. 21: Figure 9: (a) CDF probability versus QoE for MamBRA and Pensieve-PPO, (b) average QoE
- p. 21: Table 3: Performance comparison summary between MamBRA and Pensieve-PPO

## 6. Lineas con posible contenido matematico/formal

Estas lineas NO son LaTeX verificado. Sirven para localizar formulas, objetivos, restricciones o pseudocodigo que hay que verificar en PDF.

- p. 10: `Let xt ∈RD denote the input at time step t, and let ht ∈RN denote the latent state.`
- p. 10: `ht = ¯Atht−1 + ¯Btxt,`
- p. 10: `yt = Ctht,`
- p. 10: `where ¯At ∈RN×N, ¯Bt ∈RN×D, and Ct ∈RD×N are input-dependent parameters.`
- p. 10: `diagonal state matrix A ∈RN×N (Gu, Goel, et al. 2022). Given a per-token step size`
- p. 10: `∆t > 0, the discretization is`
- p. 10: `¯At = exp(∆tA),`
- p. 10: `¯Bt = A−1 (exp(∆tA) −I) Bt,`
- p. 10: `where I ∈RN×N is the identity matrix.`
- p. 10: `Bt = sB(xt),`
- p. 10: `Ct = sC(xt),`
- p. 10: `∆t = softplus(θ + s∆(xt)).`
- p. 10: `Here, sB(·), sC(·), and s∆(·) are learned linear projections. This design enables adaptive`
- p. 11: `ˆf = min(60, max(−30, f))`
- p. 11: `bufferForwardSecs = max(0, ˆf)`
- p. 11: `bufferDeficitSecs = max(0, −ˆf)`
- p. 13: `(window=20)`
- p. 13: `t=1, training and validation samples are constructed using a window`
- p. 13: `Xt = [xt−19, xt−18, . . . , xt] ,`
- p. 16: `(window=20)`
- p. 16: `during which the ﬁrst W timesteps (with W = 20, matching the training window length)`
- p. 16: `Formally, for each timestep t ≥W, the model updates its internal state using the`
- p. 16: `t ) = fSSM(x(s)`
- p. 18: `NRMSE=0.064.`
- p. 20: `Sessions = 265`
- p. 20: `Sessions = 71`
- p. 20: `Sessions = 45`
- p. 20: `Sessions = 24`
- p. 20: `Accuracy ≈92.763`
- p. 20: `Accuracy ≈92.169`
- p. 20: `Accuracy ≈96.620`
- p. 20: `Accuracy ≈85.794`
- p. 20: `MOS = 1 + 4 ·`
- p. 20: `QoE = (MOS −1) · 4`
- p. 24: `openreview.net/forum?id=tEYskw1VY2.`

## 7. Extraccion tecnica por categorias


### 7.1. modelo ia arquitectura algoritmo

Palabras clave usadas: `model, models, neural, architecture, algorithm, policy, agent, actor, critic, actor-critic, DQN, deep Q, Q-learning, PPO, proximal policy, A3C, reinforcement, DRL, deep reinforcement, meta reinforcement, meta-RL, meta learning, MAML, Mamba, state space, SSM, LSTM, policy network, prediction model, Pensieve, SODA, DQNReg, MetaABR, MERINA, Oboe`

**Fragmento 1 - p. 6 - score 10:**

Conventional Adaptive Bitrate (ABR) algorithms mostly ignore user-speciﬁc content preferences in favor of optimizing network-level metrics like bitrate stability and rebuﬀering avoidance. Sengupta et al. 2018 introduced HotDASH, a hotspot-aware video streaming framework based on an actor-critic neural network and a cascaded deep reinforcement learning architecture, to overcome this limitation. Their technique allows the reinforce- ment learning agent to opportunistically prefetch video segments that suit user preferences while also optimizing bitrate selection. HotDASH dramatically increases user satisfaction and streaming eﬃciency by integrating preference awareness into the adaptation strategy.

**Fragmento 2 - p. 9 - score 9:**

While real-time transcoding takes care of edge storage constraints, the DDPG agent dynamically chooses the best streaming sources; edge, macro, or cloud and matching bitrates. In 5G- enabled multi-tier video streaming, simulations demonstrate that this strategy outperforms conventional network-driven and hybrid edge-cloud techniques by improving QoE, lowering bitrate errors, and minimizing transcoding violations. J. Zhang et al. 2025 suggest Predictive LSTM Local Attention ABR (PLL-ABR), an Adaptive Bitrate (ABR) algorithm based on Deep Reinforcement Learning (DRL) that makes use of the Proximal Policy Optimization (PPO) framework enhanced with dual clipping, Long Short-Term Memory (LSTM) networks, and local attention mechanisms.

**Fragmento 3 - p. 7 - score 7:**

Table 1: Enhancement of QoE through the evolution of adaptation algorithms Investigation Adaptation Algorithm Key Contributions QoE Improvements Mao et al. 2017 Pensieve – RL Neural network selects bitrate based on past streaming states +12–25% average QoE Sengupta et al. 2018 HotDASH – Actor–Critic & Cascaded DRL Incorporates user preferences and prefetching strategies +14.31% bitrate, +16.2% QoE T. Huang et al. 2019 Comyco – Imitation Learning Trains on expert trajectories to reduce exploration overhead +7.5–16.79% perceptual QoE Dinaki et al. 2021 BiLSTM–CNN Hybrid Proactive QoE prediction beyond traditional QoS metrics Lowest MAE and RMSE Wei et al. 2022 QuDASH – Quantum ABR Solves QUBO formulation for optimal bitrate selection Highest QoE in 68.2% of scenarios Xu et al.

**Fragmento 4 - p. 1 - score 5:**

MamBRA: Session-Level Bandwidth Prediction for Adaptive Video Streaming using Selective State Space Models Jamal Hussein University of Sulaymaniyah Aree Mohammed University of Sulaymaniyah Miran Abdullah University of Sulaymaniyah Research Article Keywords: SSM-Mamba, bitrate adaptation, video streaming, network bandwidth, QoE Posted Date: May 12th, 2026 DOI: https://doi.org/10.21203/rs.3.rs-9024915/v1 License:   This work is licensed under a Creative Commons Attribution 4.0 International License. Read Full License Additional Declarations: No competing interests reported.

**Fragmento 5 - p. 2 - score 5:**

However, as user demands for high quality and low latency increase, using eﬃcient video streaming systems is getting harder. In addition to taxing network resources, the increase in video traﬃc is lower- ing video quality. Deep and transformer learning algorithms use data-driven methods to optimize video delivery, enhance QoE, and lessen network congestion in order to overcome these obstacles. Mamba utilizes the eﬃcient linear complexity of selective state space model (SSM) mechanism to process data sequences more eﬀectively. This paper proposes an adaptive video streaming framework (MamBRA) based on Mamba for session-level bandwidth prediction. The model is trained in a supervised time-series manner on disjoint user sessions to prevent information leakage and preserve temporal structure.

**Fragmento 6 - p. 2 - score 5:**

During inference, it leverages the linear state-space formulation of Mamba to eﬃciently generate stable bandwidth predictions within each session. Experimen- tal results demonstrate reduced prediction error, improved accuracy, and enhanced temporal stability. The model achieves an overall inference accuracy of 93.94%, with session-level accuracy reaching as high as 97.32%. Furthermore, the predicted band- width achieves more consistent QoE scores compared to the PPO-based approach used in Pensieve. Keywords: SSM-Mamba, bitrate adaptation, video streaming, network bandwidth, QoE. 1

**Fragmento 7 - p. 4 - score 5:**

This approach seeks to improve energy usage without sacriﬁcing the user experience (Tien et al. 2025; X. Yang et al. 2024). 1.2 Machine Learning–Based Sequence Modeling for Bitrate Adaptation Machine learning–based approaches have been extensively adopted for bitrate adaptation in video streaming, with sequence modeling architectures such as Transformers and recurrent neural networks (RNNs) playing a particularly prominent role (Mao et al. 2017). Recently, Mamba (selective structured state-space sequence architecture) has emerged as a powerful alternative to Transformer-based models (Gu and Dao 2024). Unlike self- attention mechanisms whose computational complexity grows quadratically with sequence length, Mamba leverages selective state-space modeling to achieve linear-time complexity, enabling scalable processing of very long sequences while maintaining competitive repre- sentational capacity.

**Fragmento 8 - p. 6 - score 5:**

The rest of the paper is organized as follows: Section 2 gives a review of the bitrate adaptation for live streaming using optimization techniques, while Section 3 describes the detailed structure of the Mamba framework and the SSM. Section 4 describes the dataset used to build the proposed model. Section 5 presents the proposed MamBRA model in detail. In Section 6, QoE is computed using the bandwidth values predicted by MamBRA, followed by a comparative evaluation against Pensieve-PPO. Finally, Section 7 identiﬁes upcoming trends and gaps in the literature and makes recommendations for further research. 2 Related Work Early studies on adaptive video streaming addressed the shortcomings of traditional rate- and buﬀer-based ABR methods under dynamic network conditions.

**Fragmento 9 - p. 8 - score 5:**

2023. The authors suggested a customized federated learning ABR algorithm that applies a tailoring phase and aggregates knowledge from clients’ local models without exchanging raw data. In addition to improvements from context factors and personalization, experiments on 3G, 4G, and WiFi traces showed the highest overall QoE, the lowest rebuﬀering, and smoothness penalties, with an improvement of about 10% above local models, showing substantial adaptation. RL-based ABR algorithms are inadequate for optimizing QoE, especially during initial buﬀering and playback, according to D. Yang et al. 2023. They suggested a subepisodic DRL method that separated video sessions into formal playback (FP) and initial buﬀer- ing (IB) with distinct replay and optimization memories, all of which were connected by a reward mechanism based on QoE.

**Fragmento 10 - p. 10 - score 5:**

• Mobile device energy and computation costs are frequently disregarded. 3 Mamba Framework Mamba introduces input-dependent selectivity into state space models (SSMs), enabling content-aware sequence modeling with linear time complexity (Gu and Dao 2024). Rather than relying on attention (Vaswani et al. 2017), Mamba performs selective state transitions using structured SSMs. Let xt ∈RD denote the input at time step t, and let ht ∈RN denote the latent state. Mamba models the sequence using the discrete-time recurrence ht = ¯Atht−1 + ¯Btxt, yt = Ctht, where ¯At ∈RN×N, ¯Bt ∈RN×D, and Ct ∈RD×N are input-dependent parameters. The discrete parameters are derived from an underlying continuous-time system with diagonal state matrix A ∈RN×N (Gu, Goel, et al.

**Fragmento 11 - p. 15 - score 5:**

• Categorical Features: These are passed through an Embedding layer, which converts discrete categories into continuous vectors. • Numeric Features: These are passed after normalization (Figure 3) to be com- bined with the embeddings. • Concatenation: Both feature types are merged into a single representation before entering the main model block. 2. Core Model Architecture The dotted box contains the primary neural network components that constitute the MamBRA model: • Input Projection: A linear layer that maps the concatenated features into the model’s hidden dimension. • Mamba Block (Sequence Scan): This is the heart of the model. Unlike standard Transformers, Mamba uses a selective SSM to process sequences eﬃciently, which is particularly good at capturing long-range dependencies.

**Fragmento 12 - p. 21 - score 5:**

Additionally, the bandwidth predicted by MamBRA yields more reliable QoE ratings in comparison to the PPO-based approach used in Pensieve. According to the ﬁndings of this study, several directions for future research are high- lighted, as follows: • Integrating the predictive strengths of MamBRA with end-to-end ABR agent models 20

**Fragmento 13 - p. 24 - score 5:**

“Mamba: Linear-Time Sequence Modeling with Selec- tive State Spaces”. In: First Conference on Language Modeling. url: https : / / openreview.net/forum?id=tEYskw1VY2. Patro, Badri Narayana and Vijay Srinivas Agneeswaran (2025). “Mamba-360: Survey of State Space Models as Transformer Alternative for Long Sequence Modelling: Methods, Applications, and Challenges”. In: Engineering Applications of Artiﬁcial Intelligence 159, p. 111279. issn: 0952-1976. doi: 10.1016/j.engappai.2025.111279. Somvanshi, Shriyank et al. (2025). “From S4 to Mamba: A Comprehensive Survey on Structured State Space Models”. In: arXiv preprint. Survey tracing evolution of SSMs from S4 through Mamba and related variants. url: https://arxiv.org/abs/ 2503.18970.

**Fragmento 14 - p. 24 - score 5:**

Zhang, Guozhen et al. (2024). “VFIMamba: Video Frame Interpolation With State Space Models”. In: Proceedings of the 38th International Conference on Neural Information Processing Systems (NIPS ’24). Vol. 37. Red Hook, NY, USA: Curran Associates Inc., pp. 107225–107248. doi: 10.52202/079017-3405. Liu, Xiao et al. (2026). “Vision Mamba: A Comprehensive Survey and Taxonomy”. In: IEEE Transactions on Neural Networks and Learning Systems 37.2, pp. 505–525. doi: 10.1109/TNNLS.2025.3610435. Zhang, Hanwei et al. (2024). “A Survey on Visual Mamba”. In: Applied Sciences 14.13, p. 5683. doi: 10.3390/app14135683. 23

**Fragmento 15 - p. 25 - score 5:**

Wei, B. et al. (2022). “QuDASH: Quantum-inspired Rate Adaptation Approach for DASH Video Streaming”. In: IEEE Access 11, pp. 118462–118473. doi: 10.1109/ACCESS. 2023.3326326. Xu, Yeting et al. (2023). “FedABR: A Personalized Federated Reinforcement Learning Ap- proach for Adaptive Video Streaming”. In: 2023 IFIP Networking Conference (IFIP Networking). IEEE, pp. 1–9. doi: 10 . 23919 / IFIPNetworking57963 . 2023 . 10186404. Yang, D. et al. (2023). “QoE-Aware Adaptive Bitrate Algorithm Based on Subepisodic Deep Reinforcement Learning for DASH”. In: Proceedings of the 2023 15th Interna- tional Conference on Machine Learning and Computing, pp. 103–108. doi: 10.1145/ 3587716.3587733. Darwich, M. and M. Bayoumi (2024). “Video Quality Adaptation Using CNN and RNN Models for Cost-eﬀective and Scalable Video Streaming Services”.

**Fragmento 16 - p. 25 - score 5:**

Teixeira, Thiago, Bo Zhang, and Yuriy Reznik (2021). “Adaptive Streaming Playback Statistics Dataset”. In: Proceedings of the 12th ACM Multimedia Systems Conference, pp. 248–254. doi: 10.1145/3458305.3478444. Ran, Dezhi et al. (2020). “Preference-aware Dynamic Bitrate Adaptation for Mobile Short- form Video Feed Streaming”. In: IEEE Access 8, pp. 220083–220094. doi: 10.1109/ ACCESS.2020.3042619. Artioli, Emanuele, Farzad Tashtarian, and Christian Timmerer (2024). “DIGITWISE: Dig- ital Twin-based Modeling of Adaptive Video Streaming Engagement”. In: Proceedings of the 15th ACM Multimedia Systems Conference, pp. 78–88. doi: 10.1145/3625468. 3647613. godka (2025). Pensieve-PPO: The simplest implementation of Pensieve via state-of-the- art RL algorithms (PPO, DQN, SAC).

**Fragmento 17 - p. 26 - score 5:**

(2025). “Deep reinforcement learning enhanced optimization algo- rithm for adaptive bitrate video streaming”. In: AIP Advances 15.7, p. 075042. doi: 10.1063/5.0277381. Vaswani, Ashish et al. (2017). “Attention is All you Need”. In: Advances in Neural Informa- tion Processing Systems. Vol. 30. Curran Associates, Inc. url: https://proceedings. neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa- Abstract.html. Gu, Albert, Karan Goel, and Christopher Ré (2022). “Eﬃciently Modeling Long Sequences with Structured State Spaces”. In: International Conference on Learning Representa- tions (ICLR). arXiv: 2111.00396 [cs.LG]. Balachandran, Athula et al. (2013). “Developing a Predictive Model of Quality of Experi- ence for Internet Video”.

**Fragmento 18 - p. 4 - score 4:**

of video data contributes to congestion, elevated costs, and high energy usage (George et al. 2025), among other issues, developing video traﬃc optimization methods is critically important. Furthermore, delivering high video quality and a positive QoE remains a core objective in video streaming. Since algorithms rely on QoE feedback to adjust streaming quality, the ﬁeld heavily invests in research aimed at creating reliable and accurate QoE models (Jia et al. 2025). Another challenge is the energy consumption, which is a main concern across a live video streaming pipeline. Conventional machine and deep learning models oﬀer a solution to these problems by enabling energy-aware video encoding and quality adaptation.

**Fragmento 19 - p. 5 - score 4:**

3. Eﬃcient inference via linear state-space modeling: The inference procedure leverages the linear state-space formulation of Mamba to generate stable and computationally eﬃcient bandwidth predictions within each session, improving temporal smoothness and robustness. 4. QoE-oriented performance validation: Beyond prediction accuracy and error re- duction, the framework demonstrates more consistent QoE outcomes compared to Pensieve-PPO, highlighting its practical advantage for adaptive bitrate streaming. Architectural overview of the proposed MamBRA framework is shown in Figure 1. User session data are utilized for model training and validation, followed by an inference stage that performs adaptive bandwidth selection.

**Fragmento 20 - p. 6 - score 4:**

Therefore, a variety of optimization strategies were then investigated by researchers in an eﬀort to enhance bitrate adaptability. The goal of these strategies was to balance playback stability, re- buﬀering reduction, and video quality in order to improve QoE. Table 1 demonstrates the recent research on optimization algorithms that investigated to enhance QoE. Below a brief description of each algorithm is provided. Mao et al. 2017 discussed the drawbacks of conventional ABR algorithms in dynamic network scenarios. They presented Pensieve, a system based on reinforcement learning that trains a neural network to choose bitrate based on past streaming results. Evalua- tions revealed that it outperformed rate-based, buﬀer-based, and MPC schemes, improving average QoE by 12% to 25% and exhibiting strong performance in previously untested net- work circumstances.

**Fragmento 21 - p. 7 - score 4:**

2025 Adversarial Inverse RL (AIRL) Generalizes to unseen network conditions +4.3–9.4% video quality, –0.054–6.2% stall Naseh et al. 2025 DRL with DDPG Edge-DASH Joint user–server bitrate allocation Higher QoE, fewer bitrate errors J. Zhang et al. 2025 PLL-ABR – DRL with PPO, LSTM & Attention Improves bitrate stability and prediction accuracy ∼28.5% QoE gain requirements, and an average QoE that is 7.5%–16.79% higher than previous methods. In 2020, researchers began addressing the gap in proactive video QoE prediction be- yond traditional QoS metrics. Dinaki et al. 2021 addressed the problem of proactively predicting video QoE beyond QoS metrics and delayed client measurements. A BiLSTM- CNN hybrid model was suggested, in which CNN recovers local patterns from multivariate time series and BiLSTM captures temporal dependencies.

**Fragmento 22 - p. 9 - score 4:**

Robust ABR in heterogeneous networks was discussed by Ling et al. 2025. In order to learn reward functions independent of policies and allow for ﬂexible adaptation to diﬀerent QoE targets and unseen networks, they devised an adversarial inverse reinforcement learn- ing (AIRL) system that makes use of expert demonstrations. Experiments demonstrated a 4.3%–9.4% improvement in video quality and a 0.054%–6.2% reduction in stall time, demonstrating strong adaptation and excellent use of expert knowledge. In multi-tier Edge-DASH networks, a Deep Reinforcement Learning (DRL) framework utilizing Deep Deterministic Policy Gradient (DDPG) has been developed by Naseh et al. 2025 for joint User-to-Server Allocation (USA) and Bitrate Allocation (BrA).

**Fragmento 23 - p. 9 - score 4:**

By increasing bitrate decision accuracy and stability, this method raises QoE. Experimental results show a QoE gain of about 28.5% across bandwidth usage, rebuﬀering, and playback smoothness parameters when compared to numerous state-of-the-art ABR algorithms. The review identiﬁes various research challenges and gaps in adaptive bitrate optimiza- tion for live streaming as follows: • Most techniques handle live streaming like VoD; live-speciﬁc latency restrictions are rarely addressed. • Many studies rely on synthetic or VoD traces due to the lack of realistic live-network datasets. • ML/DRL ABR models often show weak generalization to unseen network conditions. • Insuﬃcient analysis of failure modes and safety of learning-based ABR.

**Fragmento 24 - p. 14 - score 4:**

Session-level windowing further ensures that temporal dependencies are learned strictly within coherent playback contexts, improving both mod- eling ﬁdelity and evaluation validity. 5.2 MamBRA Training and Validation Pipelines The diagram shown in Figure 4 illustrates the architecture and training workﬂow of a machine learning model utilizing a Mamba Block (a State Space Model architecture). The ﬂow is divided into two main paths: the training pipeline (solid lines) and the validation pipeline (dashed lines). Numeric features Categorical features Train data Concatenate Categorical Embeddings (per feature) Numeric features Categorical features Validation data Input Projection Linear Mamba Block (Sequence Scan) RMSNorm Linear Head Prediction (Last Time Step) Huber Loss AdamW Backprop gradients enabled Huber Loss MSE Loss no gradients Core MamBRA train validation shared Figure 4: Training and validation process of MamBRA model 1.

**Fragmento 25 - p. 17 - score 4:**

First, the results of the training are presented in Subsection 6.1. Next, the model’s inference tests are detailed in Subsec- tion 6.2. Finally, the decision-making behavior of MamBRA is compared against the baseline method Pensieve-PPO under a ﬂuctuating network trace using QoE evaluation metric (Subsection 6.3). 6.1 Model Training Results For a sequence-prediction model like MamBRA, and by tracking the Huber loss, the gap between what MamBRA predicted and what the network actually delivered is measured. Figure 6 illustrates the Huber loss and accuracy for the training and validation. Figure 6: Huber loss versus accuracy To provide a comprehensive view of MamBRA model’s performance, we highlight the following analysis: 16

**Fragmento 26 - p. 25 - score 4:**

https://github.com/godka/Pensieve- PPO. GitHub repository (accessed 2026-03-01). Sengupta, S. et al. (2018). “HotDASH: Hotspot Aware Adaptive Video Streaming Using Deep Reinforcement Learning”. In: 2018 IEEE 26th International Conference on Net- work Protocols (ICNP). Cambridge, UK, pp. 165–175. doi: 10.1109/ICNP.2018. 000. Huang, T. et al. (Oct. 2019). “Comyco: Quality-aware Adaptive Video Streaming via Imi- tation Learning”. In: Proceedings of the 27th ACM International Conference on Multi- media, pp. 429–437. doi: 10.1145/3343031.3351014. Dinaki, H.E. et al. (2021). “Forecasting Video QoE with Deep Learning from Multivariate Time-series”. In: IEEE Open Journal of Signal Processing 2, pp. 512–521. doi: 10. 1109/OJSP.2021.3099065.


### 7.2. estado inputs features observaciones

Palabras clave usadas: `state, states, input, inputs, feature, features, observation, observations, throughput, bandwidth, buffer, download time, download duration, chunk size, segment size, history, past, remaining, last bitrate, network condition, QoE objective, task, environment, session, forecast, prediction, representation`

**Fragmento 1 - p. 13 - score 9:**

tures and embedding categorical features. At inference time, the model operates in a fully online and stateful manner, processing observations sequentially without windowing. After a brief 20-timestep warm-up to initialize the SSM state, the model produces per-timestep bandwidth predictions, with the state reset only at session boundaries. 5.1 Feature Preprocessing and Session-Aware Sliding-Window Segmentation The dataset consists of both numeric (throughput and buﬀer occupancy) and categorical (device indicators) features, and is organized into disjoint user sessions, each correspond- ing to a continuous playback episode. All preprocessing and windowing operations are performed at the session level to prevent information leakage across sessions.

**Fragmento 2 - p. 16 - score 9:**

5.3 Inference Procedure At inference time, MamBRA is applied in an online, sequential manner to generate bandwidth predictions within each user session. In contrast to training, where ﬁxed-length sliding windows are used to construct supervised samples, inference does not rely on windowing or stride-based segmentation. Figure 5 illustrates the inference procedure of MamBRA. Test data (one session) Numeric features (-bandwidthMBPS) Categorical features bandwidthMBPS Scaler (Standard) Encoders Preprocesser Warm-up phase (window=20) MamBRA Prediction Inverse-scaler (Standard) predicted bandwidth Huber, MSE, RMSE, NRMSE Accuracy CDF Anlaysis →MOS →QoE Figure 5: Inference process of MamBRA for one session of the test data For a given session s of length Ts with a sequence of preprocessed input features x(s) t Ts t=1, the model processes observations one timestep at a time, updating its internal recurrent state at each step.

**Fragmento 3 - p. 14 - score 6:**

Session-level windowing further ensures that temporal dependencies are learned strictly within coherent playback contexts, improving both mod- eling ﬁdelity and evaluation validity. 5.2 MamBRA Training and Validation Pipelines The diagram shown in Figure 4 illustrates the architecture and training workﬂow of a machine learning model utilizing a Mamba Block (a State Space Model architecture). The ﬂow is divided into two main paths: the training pipeline (solid lines) and the validation pipeline (dashed lines). Numeric features Categorical features Train data Concatenate Categorical Embeddings (per feature) Numeric features Categorical features Validation data Input Projection Linear Mamba Block (Sequence Scan) RMSNorm Linear Head Prediction (Last Time Step) Huber Loss AdamW Backprop gradients enabled Huber Loss MSE Loss no gradients Core MamBRA train validation shared Figure 4: Training and validation process of MamBRA model 1.

**Fragmento 4 - p. 16 - score 6:**

The SSM maintains a hidden state that summarizes past information and evolves according to the learned state transition dynamics. This enables the model to incorporate arbitrarily long temporal context without explicitly storing past inputs. To ensure a well-initialized internal state, inference begins with a warm-up phase, during which the ﬁrst W timesteps (with W = 20, matching the training window length) are fed sequentially into the model without using the corresponding outputs for evaluation or decision-making. After this warm-up, the model generates a bandwidth prediction at every subsequent timestep. Formally, for each timestep t ≥W, the model updates its internal state using the current input x(s) t and produces a prediction ˆy(s) t+1 for the next-step bandwidth: (ˆy(s) t+1, h(s) t ) = fSSM(x(s) t , h(s) t−1), where h(s) t denotes the SSM hidden state at timestep t.

**Fragmento 5 - p. 17 - score 6:**

cisions are made continuously as new network observations arrive. Importantly, the SSM state is reset only at session boundaries, ensuring that temporal dependencies are learned and applied strictly within individual playback sessions. In summary, inference is performed in a fully online and stateful manner, leveraging the recurrent dynamics of Mamba to integrate historical context eﬃciently. The warm-up phase aligns the internal state with recent session dynamics, while step-by-step process- ing enables continuous, low-latency bandwidth prediction suitable for real-time adaptive bitrate control. 6 Results and Discussion In this section, various tests are presented that demonstrate the performance of the pro- posed MamBRA model in terms of loss, accuracy, and QoE.

**Fragmento 6 - p. 2 - score 5:**

MamBRA: Session-Level Bandwidth Prediction for Adaptive Video Streaming using Selective State Space Models Jamal A. Hussein , Aree A. Mohammed, and Miran T. Abdullah Department of Computer, College of Science, University of Sulaimani, KRG, Iraq {jamal.ali, aree.ali, miran.abdullah}@univsul.edu.iq March 6, 2026 Corresponding author: Jamal A. Hussein Email: jamal.ali@univsul.edu.iq Abstract Live streaming is the real-time transmission of video content to an audience as it is simultaneously recorded. This technology is frequently utilized for applications such as covering live events and facilitating video calls. By dynamically modifying the video quality to match network conditions and device capabilities, adaptive video streaming provides improved Quality of Experience (QoE).

**Fragmento 7 - p. 4 - score 5:**

1.3 Research Contributions In this research, we propose MamBRA; an adaptive video streaming framework based on the Mamba architecture for accurate session-level bandwidth prediction. The model is developed and evaluated on a comprehensive dataset comprising diverse numerical and categorical features (Teixeira et al. 2021). User perception of streaming quality is inher- ently subjective; viewers exhibit diverse sensitivities to video artifacts and network-induced 3

**Fragmento 8 - p. 8 - score 5:**

ABR performance and QoE are negatively impacted by erroneous network predictions, which Woo et al. 2024 addressed. They suggested a buﬀer-based ABR algorithm com- bined with a Gated Recurrent Unit (GRU)-based network bandwidth prediction model, which forecasts throughput and playback metrics by utilizing GRU’s temporal dependency modelling. The method, which was tested in train, bus, and pedestrian situations, elim- inated rebuﬀering, minimized quality switches, and oﬀered up to 40% greater MOS than conventional ABR schemes especially in extremely changeable network conditions. In situations with multiple clients, where traditional ABR is unable to guarantee sta- bility and fairness, Kang et al. 2024 concentrated on adaptive streaming.

**Fragmento 9 - p. 11 - score 5:**

Session-level features include sessionID and sequenceID, where sessionID groups events belonging to the same user session and sequenceID denotes the temporal order of events within a session. Following established outlier detection practices in multimedia crowdsourcing [Chen et al., 2014], extreme positive and negative values of bufferForwardSecs were observed due to player state transitions and logging artifacts. To preserve physical interpretability, this signal was clipped to a bounded range [−30, 60] seconds and decomposed into buﬀer oc- cupancy (bufferForwardSecs) and buﬀer deﬁcit (bufferDeficitSecs) components, as deﬁned by the equations below. ˆf = min(60, max(−30, f)) bufferForwardSecs = max(0, ˆf) bufferDeficitSecs = max(0, −ˆf) 10

**Fragmento 10 - p. 13 - score 5:**

Numeric features are standardized using z-score normalization (standard scaling), where the mean and standard deviation are computed from the training split and subsequently applied to validation data. Categorical features are transformed using feature-wise label encoding, mapping each categorical value to an integer index. These encoded categorical features are then used as inputs to learned embedding layers within the model. The dataset is divided into training, validation, and testing sets using a 70%/10%/20% split. The detailed procedures for preprocessing, normalization, windowing, and data partitioning are illustrated in Figure 3. clean-up and split Original data Test data Numeric features Categorical features Train-Validation data Scaler Encoders Preprocesser group by sessionID generate sequences per session group (window=20) split to train and validation Validation data Train data 100% 80% 20% 70% 10% Figure 3: Dataset preparation (clean-up, normalization, sequencing and splitting) The dataset is ﬁrst partitioned into disjoint user sessions, where each session corre- sponds to a continuous playback episode.

**Fragmento 11 - p. 14 - score 5:**

and the corresponding prediction target is the next-step bandwidth value yt+1. Using a stride of 1 generates a prediction target at every valid timestep within each session, resulting in maximally overlapping windows and dense supervision. This approach ensures that the model is trained to make bandwidth predictions at all decision points encountered during a session, closely aligning the training procedure with the online ABR setting, where bitrate adaptation decisions are made continuously throughout playback. The choice of a window length of 20 timesteps captures short-term temporal depen- dencies within a session, such as recent throughput ﬂuctuations and transient network conditions, while avoiding unnecessary long-range context that may span multiple, po- tentially heterogeneous sessions.

**Fragmento 12 - p. 1 - score 4:**

MamBRA: Session-Level Bandwidth Prediction for Adaptive Video Streaming using Selective State Space Models Jamal Hussein University of Sulaymaniyah Aree Mohammed University of Sulaymaniyah Miran Abdullah University of Sulaymaniyah Research Article Keywords: SSM-Mamba, bitrate adaptation, video streaming, network bandwidth, QoE Posted Date: May 12th, 2026 DOI: https://doi.org/10.21203/rs.3.rs-9024915/v1 License:   This work is licensed under a Creative Commons Attribution 4.0 International License. Read Full License Additional Declarations: No competing interests reported.

**Fragmento 13 - p. 2 - score 4:**

However, as user demands for high quality and low latency increase, using eﬃcient video streaming systems is getting harder. In addition to taxing network resources, the increase in video traﬃc is lower- ing video quality. Deep and transformer learning algorithms use data-driven methods to optimize video delivery, enhance QoE, and lessen network congestion in order to overcome these obstacles. Mamba utilizes the eﬃcient linear complexity of selective state space model (SSM) mechanism to process data sequences more eﬀectively. This paper proposes an adaptive video streaming framework (MamBRA) based on Mamba for session-level bandwidth prediction. The model is trained in a supervised time-series manner on disjoint user sessions to prevent information leakage and preserve temporal structure.

**Fragmento 14 - p. 2 - score 4:**

During inference, it leverages the linear state-space formulation of Mamba to eﬃciently generate stable bandwidth predictions within each session. Experimen- tal results demonstrate reduced prediction error, improved accuracy, and enhanced temporal stability. The model achieves an overall inference accuracy of 93.94%, with session-level accuracy reaching as high as 97.32%. Furthermore, the predicted band- width achieves more consistent QoE scores compared to the PPO-based approach used in Pensieve. Keywords: SSM-Mamba, bitrate adaptation, video streaming, network bandwidth, QoE. 1

**Fragmento 15 - p. 3 - score 4:**

2020). When network bandwidth variations are small, ABR algorithms can operate eﬀectively because they use network bandwidth history to anticipate future network bandwidth (Akhtar et al. 2018; Pham et al. 2020). However, the QoE of video streaming frequently deteriorates in settings where network bandwidth ﬂuctuates frequently, like wireless networks, due to imprecise forecasts of future network capacity (Woo et al. 2024). In order to improve QoE in multimedia streaming, numerous studies have been car- ried out(Seufert et al. 2015; Timmerer et al. 2017). These studies have concentrated on adaptive bitrate algorithms, network optimization, predictive QoE modeling, and intelli- gent management systems to minimize buﬀering, latency, and degradation of video quality, particularly in dynamic wireless network environment.

**Fragmento 16 - p. 5 - score 4:**

From a QoE per- spective, the predicted bandwidth yields more consistent QoE scores than those obtained using the PPO-based strategy implemented in Pensieve (Mao et al. 2017; godka 2025), highlighting the eﬀectiveness of the proposed framework for adaptive bitrate streaming optimization. The main contributions of the proposed approach can be summarized as follows: 1. Novel dataset structuring at the session level: The dataset is reorganized into fully disjoint user sessions with heterogeneous numerical and categorical features, enabling realistic temporal modeling while explicitly preventing cross-session information leak- age. 2. Session-aware supervised training strategy: A time-series learning framework is de- signed where training is strictly performed at the session level, preserving sequential dependencies and ensuring fair generalization across independent user trajectories.

**Fragmento 17 - p. 5 - score 4:**

3. Eﬃcient inference via linear state-space modeling: The inference procedure leverages the linear state-space formulation of Mamba to generate stable and computationally eﬃcient bandwidth predictions within each session, improving temporal smoothness and robustness. 4. QoE-oriented performance validation: Beyond prediction accuracy and error re- duction, the framework demonstrates more consistent QoE outcomes compared to Pensieve-PPO, highlighting its practical advantage for adaptive bitrate streaming. Architectural overview of the proposed MamBRA framework is shown in Figure 1. User session data are utilized for model training and validation, followed by an inference stage that performs adaptive bandwidth selection.

**Fragmento 18 - p. 5 - score 4:**

impairments (Ran et al. 2020; Artioli et al. 2024). Therefore, the dataset is organized into multiple disjoint user sessions. To prevent information leakage and preserve temporal con- sistency, a supervised time-series learning strategy is employed, where training is conducted strictly at the session level. During inference, the proposed approach exploits the linear state-space formulation of Mamba to eﬃciently generate bandwidth predictions within each individual user session, enabling scalable and stable sequential modeling. Experimental re- sults demonstrate signiﬁcant error reduction and improved predictive accuracy. Moreover, the predicted bandwidth trajectories exhibit enhanced temporal stability.

**Fragmento 19 - p. 7 - score 4:**

Table 1: Enhancement of QoE through the evolution of adaptation algorithms Investigation Adaptation Algorithm Key Contributions QoE Improvements Mao et al. 2017 Pensieve – RL Neural network selects bitrate based on past streaming states +12–25% average QoE Sengupta et al. 2018 HotDASH – Actor–Critic & Cascaded DRL Incorporates user preferences and prefetching strategies +14.31% bitrate, +16.2% QoE T. Huang et al. 2019 Comyco – Imitation Learning Trains on expert trajectories to reduce exploration overhead +7.5–16.79% perceptual QoE Dinaki et al. 2021 BiLSTM–CNN Hybrid Proactive QoE prediction beyond traditional QoS metrics Lowest MAE and RMSE Wei et al. 2022 QuDASH – Quantum ABR Solves QUBO formulation for optimal bitrate selection Highest QoE in 68.2% of scenarios Xu et al.

**Fragmento 20 - p. 11 - score 4:**

The selected features are grouped into several categories, including session-level, network-level, and client-level attributes. The dataset consists of numerous client ses- sions recorded as streaming events at 4-second intervals, providing playback statistics and related metrics corresponding to the aforementioned categories, as summarized in Table 2. Table 2: Segment downloads, stream switching, network, and buﬀering behavior of the dataset (Teixeira et al. 2021). Type Category Feature Description Numeric Session sessionID The player’s session number. sequenceID A number associated with each video segment (event) within a session. Time videoSecs Seconds viewed between the last two segments. bufferForwardSecs Seconds of video buﬀered but not viewed yet.

**Fragmento 21 - p. 11 - score 4:**

bufferDeficitSecs Seconds of video playback missing due to stalling. rebufferingSecs Seconds buﬀered between the last two segments. rebufferingCount Times buﬀering occurs between the last two seg- ments. Network bytesTransferred Bytes transferred since the start of the session. bandwidthMBPS Network bandwidth. Categorical Client deviceType {desktop, tv, tablet, mobile, . . . } deviceOS {windows, android, other, ios, web_os, . . . } browser {chrome, other, ﬁrefox, edge, . . . } player {web, app} playerDim 110 dimensions (width×height). The feature playerDim is obtained by merging two numeric columns in the original dataset, resulting in 110 distinct player dimension categories. The segment duration is ﬁxed at four seconds across all sessions.

**Fragmento 22 - p. 15 - score 4:**

• Categorical Features: These are passed through an Embedding layer, which converts discrete categories into continuous vectors. • Numeric Features: These are passed after normalization (Figure 3) to be com- bined with the embeddings. • Concatenation: Both feature types are merged into a single representation before entering the main model block. 2. Core Model Architecture The dotted box contains the primary neural network components that constitute the MamBRA model: • Input Projection: A linear layer that maps the concatenated features into the model’s hidden dimension. • Mamba Block (Sequence Scan): This is the heart of the model. Unlike standard Transformers, Mamba uses a selective SSM to process sequences eﬃciently, which is particularly good at capturing long-range dependencies.

**Fragmento 23 - p. 21 - score 4:**

Inconsistent. While it reaches high scores, many sessions experience low QoE (as low as 0.0–0.4). 7 Conclusion and Future Work This study developed MamBRA model, a new bitrate adaptation framework for video stream- ing that employs Mamba for accurate session-level bandwidth prediction. The streaming dataset are recognized by fully disconnected user sessions and the model implements a su- pervised time-series learning technique that ensures temporal consistency while explicitly limiting cross-session information leaking. The conducted test demonstrates that MamBRA has remarkably reduces prediction errors (Huber and MSE) and improves temporal sta- bility of predicted bandwidths. A signiﬁcant ﬁnding of this research work is that Mamba’s linear state-space model allows for eﬃcient and stable computation, which makes it very appropriate for real-time use.

**Fragmento 24 - p. 5 - score 3:**

The resulting decisions are assessed using quantitative performance metrics, including loss, prediction accuracy, and QoE. Dataset User Session Sequences MamBRA Model Training & Validation Inference Stage Adaptive Bandwidth Selection Performance Evaluation Loss | Accuracy | QoE Figure 1: The overall architecture and processing pipeline of MamBRA 4

**Fragmento 25 - p. 7 - score 3:**

2023 Federated Learning ABR Client-speciﬁc models without raw data exchange ∼10% QoE gain, reduced rebuﬀering D. Yang et al. 2023 Subepisodic DRL Separate buﬀering and playback memories for control stability Smoother bitrate, fewer stalls Darwich et al. 2024 CNN–RNN Hybrid Frame-level bitrate estimation for ﬁne-grained adaptation +16.6% QoE, +37.1% bitrate, –87.5% rebuﬀering Woo et al. 2024 GRU-Based Bandwidth & Buﬀer ABR Throughput prediction with minimized bitrate switching Up to +40% MOS Kang et al. 2024 RL Edge-Assisted ABR Multi-client edge-assisted adaptive streaming Improved fairness and QoE Wang et al. 2024 Adversarial Information Bottleneck + Imitation Learning Robust QoE modeling with reduced overﬁtting +7.3% QoE, +30% ranking Ling et al.

**Fragmento 26 - p. 9 - score 3:**

By increasing bitrate decision accuracy and stability, this method raises QoE. Experimental results show a QoE gain of about 28.5% across bandwidth usage, rebuﬀering, and playback smoothness parameters when compared to numerous state-of-the-art ABR algorithms. The review identiﬁes various research challenges and gaps in adaptive bitrate optimiza- tion for live streaming as follows: • Most techniques handle live streaming like VoD; live-speciﬁc latency restrictions are rarely addressed. • Many studies rely on synthetic or VoD traces due to the lack of realistic live-network datasets. • ML/DRL ABR models often show weak generalization to unseen network conditions. • Insuﬃcient analysis of failure modes and safety of learning-based ABR.


### 7.3. accion decision abr salida

Palabras clave usadas: `action, actions, bitrate, bit rate, quality level, representation, decision, decisions, select, selection, adaptation, output, score, guidance, recommend, priority, policy output, controller, rate adaptation, quality`

**Fragmento 1 - p. 6 - score 5:**

Conventional Adaptive Bitrate (ABR) algorithms mostly ignore user-speciﬁc content preferences in favor of optimizing network-level metrics like bitrate stability and rebuﬀering avoidance. Sengupta et al. 2018 introduced HotDASH, a hotspot-aware video streaming framework based on an actor-critic neural network and a cascaded deep reinforcement learning architecture, to overcome this limitation. Their technique allows the reinforce- ment learning agent to opportunistically prefetch video segments that suit user preferences while also optimizing bitrate selection. HotDASH dramatically increases user satisfaction and streaming eﬃciency by integrating preference awareness into the adaptation strategy.

**Fragmento 2 - p. 8 - score 5:**

In order to maximize user QoE, Wei et al. 2022 pointed out that traditional adaptive bitrate (ABR) techniques frequently struggle to optimize bitrate selection and minimize rebuﬀering at the same time. As a quantum-inspired ABR control method, QuDASH was presented to get around these restrictions. To ﬁnd the best bitrates, it uses a Digital Annealer to solve a Quadratic Unconstrained Binary Optimization (QUBO) problem that models buﬀer conditions, bitrate ﬂuctuations, and video quality. Based on actual network traces, simulation results show that QuDASH outperforms current ABR techniques, at- taining the highest QoE in 68.2% of scenarios, conﬁrming its eﬃcacy in improving user experience. ABR adaptation under various networks and numerous QoE objectives was the main focus of the research conducted by Xu et al.

**Fragmento 3 - p. 14 - score 5:**

and the corresponding prediction target is the next-step bandwidth value yt+1. Using a stride of 1 generates a prediction target at every valid timestep within each session, resulting in maximally overlapping windows and dense supervision. This approach ensures that the model is trained to make bandwidth predictions at all decision points encountered during a session, closely aligning the training procedure with the online ABR setting, where bitrate adaptation decisions are made continuously throughout playback. The choice of a window length of 20 timesteps captures short-term temporal depen- dencies within a session, such as recent throughput ﬂuctuations and transient network conditions, while avoiding unnecessary long-range context that may span multiple, po- tentially heterogeneous sessions.

**Fragmento 4 - p. 22 - score 5:**

that can enhance bitrate selection in real-time. • Exploring the deployment of MamBRA in edge computing frameworks could further boost performance in multi-client scenario’s, minimizing latency and improving re- source allocation fairness. • Incorporating more sophisticated perceptual video quality metrics into the training objective may enhance the model’s performance to better match user satisfaction. • Testing and evaluating the proposed framework using various, modern network traces (e.g., 5G and Starlink) will guarantee its robustness to the growing of modern internet traﬃc. 8 Declarations Funding The authors received no ﬁnancial support for the research, authorship, and/or publication of this article.

**Fragmento 5 - p. 1 - score 4:**

MamBRA: Session-Level Bandwidth Prediction for Adaptive Video Streaming using Selective State Space Models Jamal Hussein University of Sulaymaniyah Aree Mohammed University of Sulaymaniyah Miran Abdullah University of Sulaymaniyah Research Article Keywords: SSM-Mamba, bitrate adaptation, video streaming, network bandwidth, QoE Posted Date: May 12th, 2026 DOI: https://doi.org/10.21203/rs.3.rs-9024915/v1 License:   This work is licensed under a Creative Commons Attribution 4.0 International License. Read Full License Additional Declarations: No competing interests reported.

**Fragmento 6 - p. 2 - score 4:**

During inference, it leverages the linear state-space formulation of Mamba to eﬃciently generate stable bandwidth predictions within each session. Experimen- tal results demonstrate reduced prediction error, improved accuracy, and enhanced temporal stability. The model achieves an overall inference accuracy of 93.94%, with session-level accuracy reaching as high as 97.32%. Furthermore, the predicted band- width achieves more consistent QoE scores compared to the PPO-based approach used in Pensieve. Keywords: SSM-Mamba, bitrate adaptation, video streaming, network bandwidth, QoE. 1

**Fragmento 7 - p. 3 - score 4:**

2017; Apple Inc. 2024), and MPEG’s Dynamic Adaptive Streaming over HTTP (MPEG-DASH)(DASH Industry Forum 2024) have solidiﬁed HAS as the global norm. However, live streaming remains challenging as providers must balance low latency, high visual quality, and network eﬃciency (Yin et al. 2015; T.-Y. Huang et al. 2014). These com- peting demands under ﬂuctuating bandwidth have sparked ongoing research into bitrate adaptation and buﬀer management. Ultimately, the need to minimize rebuﬀering while maintaining stability continues to drive innovation in streaming algorithms and system design. 1.1 Challenges in Adaptive Bitrate (ABR) Streaming Streaming services use adaptive bitrate (ABR) algorithms to manage network bandwidth ﬂuctuations for better QoE (Spiteri et al.

**Fragmento 8 - p. 4 - score 4:**

This approach seeks to improve energy usage without sacriﬁcing the user experience (Tien et al. 2025; X. Yang et al. 2024). 1.2 Machine Learning–Based Sequence Modeling for Bitrate Adaptation Machine learning–based approaches have been extensively adopted for bitrate adaptation in video streaming, with sequence modeling architectures such as Transformers and recurrent neural networks (RNNs) playing a particularly prominent role (Mao et al. 2017). Recently, Mamba (selective structured state-space sequence architecture) has emerged as a powerful alternative to Transformer-based models (Gu and Dao 2024). Unlike self- attention mechanisms whose computational complexity grows quadratically with sequence length, Mamba leverages selective state-space modeling to achieve linear-time complexity, enabling scalable processing of very long sequences while maintaining competitive repre- sentational capacity.

**Fragmento 9 - p. 5 - score 4:**

The resulting decisions are assessed using quantitative performance metrics, including loss, prediction accuracy, and QoE. Dataset User Session Sequences MamBRA Model Training & Validation Inference Stage Adaptive Bandwidth Selection Performance Evaluation Loss | Accuracy | QoE Figure 1: The overall architecture and processing pipeline of MamBRA 4

**Fragmento 10 - p. 6 - score 4:**

The rest of the paper is organized as follows: Section 2 gives a review of the bitrate adaptation for live streaming using optimization techniques, while Section 3 describes the detailed structure of the Mamba framework and the SSM. Section 4 describes the dataset used to build the proposed model. Section 5 presents the proposed MamBRA model in detail. In Section 6, QoE is computed using the bandwidth values predicted by MamBRA, followed by a comparative evaluation against Pensieve-PPO. Finally, Section 7 identiﬁes upcoming trends and gaps in the literature and makes recommendations for further research. 2 Related Work Early studies on adaptive video streaming addressed the shortcomings of traditional rate- and buﬀer-based ABR methods under dynamic network conditions.

**Fragmento 11 - p. 7 - score 4:**

Table 1: Enhancement of QoE through the evolution of adaptation algorithms Investigation Adaptation Algorithm Key Contributions QoE Improvements Mao et al. 2017 Pensieve – RL Neural network selects bitrate based on past streaming states +12–25% average QoE Sengupta et al. 2018 HotDASH – Actor–Critic & Cascaded DRL Incorporates user preferences and prefetching strategies +14.31% bitrate, +16.2% QoE T. Huang et al. 2019 Comyco – Imitation Learning Trains on expert trajectories to reduce exploration overhead +7.5–16.79% perceptual QoE Dinaki et al. 2021 BiLSTM–CNN Hybrid Proactive QoE prediction beyond traditional QoS metrics Lowest MAE and RMSE Wei et al. 2022 QuDASH – Quantum ABR Solves QUBO formulation for optimal bitrate selection Highest QoE in 68.2% of scenarios Xu et al.

**Fragmento 12 - p. 21 - score 4:**

Inconsistent. While it reaches high scores, many sessions experience low QoE (as low as 0.0–0.4). 7 Conclusion and Future Work This study developed MamBRA model, a new bitrate adaptation framework for video stream- ing that employs Mamba for accurate session-level bandwidth prediction. The streaming dataset are recognized by fully disconnected user sessions and the model implements a su- pervised time-series learning technique that ensures temporal consistency while explicitly limiting cross-session information leaking. The conducted test demonstrates that MamBRA has remarkably reduces prediction errors (Huber and MSE) and improves temporal sta- bility of predicted bandwidths. A signiﬁcant ﬁnding of this research work is that Mamba’s linear state-space model allows for eﬃcient and stable computation, which makes it very appropriate for real-time use.

**Fragmento 13 - p. 23 - score 4:**

In: IEEE/ACM Transactions on Networking 28.4, pp. 1698–1711. doi: 10.1109/TNET.2020.2996964. Akhtar, Zahaib et al. (2018). “Oboe: Auto-tuning Video ABR Algorithms to Network Conditions”. In: Proceedings of the 2018 Conference of the ACM Special Interest Group on Data Communication, pp. 44–58. doi: 10.1145/3230543.3230558. Pham, Stefan et al. (2020). “Evaluation of shared resource allocation using SAND for ABR streaming”. In: ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM) 16.2s, pp. 1–18. doi: 10.1145/3388926. Woo, J. et al. (2024). “Improving the Quality of Experience of Video Streaming Through a Buﬀer-Based Adaptive Bitrate Algorithm and Gated Recurrent Unit-Based Network Bandwidth Prediction”.

**Fragmento 14 - p. 25 - score 4:**

Wei, B. et al. (2022). “QuDASH: Quantum-inspired Rate Adaptation Approach for DASH Video Streaming”. In: IEEE Access 11, pp. 118462–118473. doi: 10.1109/ACCESS. 2023.3326326. Xu, Yeting et al. (2023). “FedABR: A Personalized Federated Reinforcement Learning Ap- proach for Adaptive Video Streaming”. In: 2023 IFIP Networking Conference (IFIP Networking). IEEE, pp. 1–9. doi: 10 . 23919 / IFIPNetworking57963 . 2023 . 10186404. Yang, D. et al. (2023). “QoE-Aware Adaptive Bitrate Algorithm Based on Subepisodic Deep Reinforcement Learning for DASH”. In: Proceedings of the 2023 15th Interna- tional Conference on Machine Learning and Computing, pp. 103–108. doi: 10.1145/ 3587716.3587733. Darwich, M. and M. Bayoumi (2024). “Video Quality Adaptation Using CNN and RNN Models for Cost-eﬀective and Scalable Video Streaming Services”.

**Fragmento 15 - p. 5 - score 3:**

3. Eﬃcient inference via linear state-space modeling: The inference procedure leverages the linear state-space formulation of Mamba to generate stable and computationally eﬃcient bandwidth predictions within each session, improving temporal smoothness and robustness. 4. QoE-oriented performance validation: Beyond prediction accuracy and error re- duction, the framework demonstrates more consistent QoE outcomes compared to Pensieve-PPO, highlighting its practical advantage for adaptive bitrate streaming. Architectural overview of the proposed MamBRA framework is shown in Figure 1. User session data are utilized for model training and validation, followed by an inference stage that performs adaptive bandwidth selection.

**Fragmento 16 - p. 6 - score 3:**

According to experimental assessments, the suggested system outperforms traditional ABR techniques in terms of average delivered bitrate by 14.31% and improves QoE by 16.2%. Key drawbacks of learning-based Adaptive Bit Rate (ABR) streaming were discussed by T. Huang et al. 2019, including low sample eﬃciency and inadequate perceptual video quality consideration. They presented Comyco, a video quality-aware ABR method that uses imitation learning and trains its neural network on expert trajectories produced by an instant solver. This approach maximizes the use of gathered data and reduces unnec- essary exploration. Comyco improves the overall QoE by choosing video chunks based on perceptual quality rather than just bitrate.

**Fragmento 17 - p. 9 - score 3:**

Robust ABR in heterogeneous networks was discussed by Ling et al. 2025. In order to learn reward functions independent of policies and allow for ﬂexible adaptation to diﬀerent QoE targets and unseen networks, they devised an adversarial inverse reinforcement learn- ing (AIRL) system that makes use of expert demonstrations. Experiments demonstrated a 4.3%–9.4% improvement in video quality and a 0.054%–6.2% reduction in stall time, demonstrating strong adaptation and excellent use of expert knowledge. In multi-tier Edge-DASH networks, a Deep Reinforcement Learning (DRL) framework utilizing Deep Deterministic Policy Gradient (DDPG) has been developed by Naseh et al. 2025 for joint User-to-Server Allocation (USA) and Bitrate Allocation (BrA).

**Fragmento 18 - p. 16 - score 3:**

This inference strategy yields dense, per-timestep predictions throughout the session and closely reﬂects the online ABR deployment scenario, in which bitrate adaptation de- 15

**Fragmento 19 - p. 19 - score 3:**

6.3 QoE Results The proposed MamBRA model is evaluated using MOS values to predict the QoE scores. These scores are normalized and cumulative scores are then calculated (CDF). Figure 9a illustrates CDF analysis of QoE scores, comparing two diﬀerent systems: MamBRA and Pensieve-PPO. • MOS: A numerical measure of the human-perceived quality. It typically ranges from 1 (Bad) to 5 (Excellent). • QoE: The subjective “satisfaction” of the user. It is aﬀected by buﬀering, video clarity, and how long it takes for the video to start. The mathematical formulas are as follows: 18

**Fragmento 20 - p. 23 - score 3:**

23, 2025. url: https: //developer.apple.com/streaming/. DASH Industry Forum (2024). MPEG-DASH (Dynamic Adaptive Streaming over HTTP). Accessed: Apr. 23, 2025. url: https://dashif.org/. Yin, Xiaoqi et al. (2015). “A Control-theoretic Approach for Dynamic Adaptive Video Streaming over HTTP”. In: Proceedings of the 2015 ACM conference on special interest group on data communication, pp. 325–338. doi: 10.1145/2785956.2787486. Huang, Te-Yuan et al. (2014). “A Buﬀer-based Approach to Rate Adaptation: Evidence from a Large Video Streaming Service”. In: Proceedings of the 2014 ACM conference on SIGCOMM, pp. 187–198. doi: 10.1145/2619239.2626296. Spiteri, K., R. Urgaonkar, and R. K. Sitaraman (2020). “BOLA: Near-optimal Bitrate Adaptation for Online Videos”.

**Fragmento 21 - p. 24 - score 3:**

“QoE-Energy Consumption Optimiza- tion for End-User Devices in Adaptive Bitrate Video Streaming Using the Lagrange Multiplier Method”. In: EAI Endorsed Transactions on Industrial Networks and Intel- ligent Systems 12.3. doi: 10.4108/eetinis.v12i3.8587. Yang, Xiang et al. (Apr. 2024). “PICO: Pipeline Inference Framework for Versatile CNNs on Diverse Mobile Devices”. In: IEEE Transactions on Mobile Computing 23.4, pp. 2712– 2730. doi: 10.1109/TMC.2023.3265111. Mao, Hongzi, Ravi Netravali, and Mohammad Alizadeh (2017). “Neural Adaptive Video Streaming with Pensieve”. In: Proceedings of the ACM Special Interest Group on Data Communication, pp. 197–210. doi: 10.1145/3098822.3098823. Gu, Albert and Tri Dao (2024).

**Fragmento 22 - p. 25 - score 3:**

Teixeira, Thiago, Bo Zhang, and Yuriy Reznik (2021). “Adaptive Streaming Playback Statistics Dataset”. In: Proceedings of the 12th ACM Multimedia Systems Conference, pp. 248–254. doi: 10.1145/3458305.3478444. Ran, Dezhi et al. (2020). “Preference-aware Dynamic Bitrate Adaptation for Mobile Short- form Video Feed Streaming”. In: IEEE Access 8, pp. 220083–220094. doi: 10.1109/ ACCESS.2020.3042619. Artioli, Emanuele, Farzad Tashtarian, and Christian Timmerer (2024). “DIGITWISE: Dig- ital Twin-based Modeling of Adaptive Video Streaming Engagement”. In: Proceedings of the 15th ACM Multimedia Systems Conference, pp. 78–88. doi: 10.1145/3625468. 3647613. godka (2025). Pensieve-PPO: The simplest implementation of Pensieve via state-of-the- art RL algorithms (PPO, DQN, SAC).

**Fragmento 23 - p. 26 - score 3:**

Wang, S., J. Lin, and F. Ye (Dec. 2024). “Imitation Learning for Adaptive Video Streaming with Future Adversarial Information Bottleneck Principle”. In: IEEE Transactions on Mobile Computing 23.12, pp. 13670–13683. doi: 10.1109/TMC.2024.3437455. Ling, Y. and Y. Qin (2025). “Learning Robust Adaptive Bitrate Algorithms with Adversar- ial Inverse Reinforcement Learning”. In: Chinese Journal of Electronics 34.4, pp. 1309– 1320. doi: 10.23919/cje.2024.00.202. Naseh, D., A. Bozorgchenani, and D. Tarchi (2025). “Deep Reinforcement Learning for Edge-DASH-based Dynamic Video Streaming”. In: 2025 IEEE Wireless Communica- tions and Networking Conference (WCNC), pp. 1–6. doi: 10.1109/WCNC61545. 2025.10978132. Zhang, Jianwei et al.

**Fragmento 24 - p. 2 - score 2:**

However, as user demands for high quality and low latency increase, using eﬃcient video streaming systems is getting harder. In addition to taxing network resources, the increase in video traﬃc is lower- ing video quality. Deep and transformer learning algorithms use data-driven methods to optimize video delivery, enhance QoE, and lessen network congestion in order to overcome these obstacles. Mamba utilizes the eﬃcient linear complexity of selective state space model (SSM) mechanism to process data sequences more eﬀectively. This paper proposes an adaptive video streaming framework (MamBRA) based on Mamba for session-level bandwidth prediction. The model is trained in a supervised time-series manner on disjoint user sessions to prevent information leakage and preserve temporal structure.

**Fragmento 25 - p. 2 - score 2:**

MamBRA: Session-Level Bandwidth Prediction for Adaptive Video Streaming using Selective State Space Models Jamal A. Hussein , Aree A. Mohammed, and Miran T. Abdullah Department of Computer, College of Science, University of Sulaimani, KRG, Iraq {jamal.ali, aree.ali, miran.abdullah}@univsul.edu.iq March 6, 2026 Corresponding author: Jamal A. Hussein Email: jamal.ali@univsul.edu.iq Abstract Live streaming is the real-time transmission of video content to an audience as it is simultaneously recorded. This technology is frequently utilized for applications such as covering live events and facilitating video calls. By dynamically modifying the video quality to match network conditions and device capabilities, adaptive video streaming provides improved Quality of Experience (QoE).

**Fragmento 26 - p. 3 - score 2:**

2020). When network bandwidth variations are small, ABR algorithms can operate eﬀectively because they use network bandwidth history to anticipate future network bandwidth (Akhtar et al. 2018; Pham et al. 2020). However, the QoE of video streaming frequently deteriorates in settings where network bandwidth ﬂuctuates frequently, like wireless networks, due to imprecise forecasts of future network capacity (Woo et al. 2024). In order to improve QoE in multimedia streaming, numerous studies have been car- ried out(Seufert et al. 2015; Timmerer et al. 2017). These studies have concentrated on adaptive bitrate algorithms, network optimization, predictive QoE modeling, and intelli- gent management systems to minimize buﬀering, latency, and degradation of video quality, particularly in dynamic wireless network environment.


### 7.4. reward qoe objetivo loss

Palabras clave usadas: `reward, QoE, quality of experience, utility, objective, loss, rebuffer, stall, stalling, smoothness, switching, quality variation, bitrate smoothness, video quality, penalty, consistent, consistency, risk, tail, latency`

**Fragmento 1 - p. 8 - score 4:**

2023. The authors suggested a customized federated learning ABR algorithm that applies a tailoring phase and aggregates knowledge from clients’ local models without exchanging raw data. In addition to improvements from context factors and personalization, experiments on 3G, 4G, and WiFi traces showed the highest overall QoE, the lowest rebuﬀering, and smoothness penalties, with an improvement of about 10% above local models, showing substantial adaptation. RL-based ABR algorithms are inadequate for optimizing QoE, especially during initial buﬀering and playback, according to D. Yang et al. 2023. They suggested a subepisodic DRL method that separated video sessions into formal playback (FP) and initial buﬀer- ing (IB) with distinct replay and optimization memories, all of which were connected by a reward mechanism based on QoE.

**Fragmento 2 - p. 9 - score 4:**

Robust ABR in heterogeneous networks was discussed by Ling et al. 2025. In order to learn reward functions independent of policies and allow for ﬂexible adaptation to diﬀerent QoE targets and unseen networks, they devised an adversarial inverse reinforcement learn- ing (AIRL) system that makes use of expert demonstrations. Experiments demonstrated a 4.3%–9.4% improvement in video quality and a 0.054%–6.2% reduction in stall time, demonstrating strong adaptation and excellent use of expert knowledge. In multi-tier Edge-DASH networks, a Deep Reinforcement Learning (DRL) framework utilizing Deep Deterministic Policy Gradient (DDPG) has been developed by Naseh et al. 2025 for joint User-to-Server Allocation (USA) and Bitrate Allocation (BrA).

**Fragmento 3 - p. 2 - score 3:**

However, as user demands for high quality and low latency increase, using eﬃcient video streaming systems is getting harder. In addition to taxing network resources, the increase in video traﬃc is lower- ing video quality. Deep and transformer learning algorithms use data-driven methods to optimize video delivery, enhance QoE, and lessen network congestion in order to overcome these obstacles. Mamba utilizes the eﬃcient linear complexity of selective state space model (SSM) mechanism to process data sequences more eﬀectively. This paper proposes an adaptive video streaming framework (MamBRA) based on Mamba for session-level bandwidth prediction. The model is trained in a supervised time-series manner on disjoint user sessions to prevent information leakage and preserve temporal structure.

**Fragmento 4 - p. 2 - score 3:**

MamBRA: Session-Level Bandwidth Prediction for Adaptive Video Streaming using Selective State Space Models Jamal A. Hussein , Aree A. Mohammed, and Miran T. Abdullah Department of Computer, College of Science, University of Sulaimani, KRG, Iraq {jamal.ali, aree.ali, miran.abdullah}@univsul.edu.iq March 6, 2026 Corresponding author: Jamal A. Hussein Email: jamal.ali@univsul.edu.iq Abstract Live streaming is the real-time transmission of video content to an audience as it is simultaneously recorded. This technology is frequently utilized for applications such as covering live events and facilitating video calls. By dynamically modifying the video quality to match network conditions and device capabilities, adaptive video streaming provides improved Quality of Experience (QoE).

**Fragmento 5 - p. 3 - score 3:**

2020). When network bandwidth variations are small, ABR algorithms can operate eﬀectively because they use network bandwidth history to anticipate future network bandwidth (Akhtar et al. 2018; Pham et al. 2020). However, the QoE of video streaming frequently deteriorates in settings where network bandwidth ﬂuctuates frequently, like wireless networks, due to imprecise forecasts of future network capacity (Woo et al. 2024). In order to improve QoE in multimedia streaming, numerous studies have been car- ried out(Seufert et al. 2015; Timmerer et al. 2017). These studies have concentrated on adaptive bitrate algorithms, network optimization, predictive QoE modeling, and intelli- gent management systems to minimize buﬀering, latency, and degradation of video quality, particularly in dynamic wireless network environment.

**Fragmento 6 - p. 4 - score 3:**

of video data contributes to congestion, elevated costs, and high energy usage (George et al. 2025), among other issues, developing video traﬃc optimization methods is critically important. Furthermore, delivering high video quality and a positive QoE remains a core objective in video streaming. Since algorithms rely on QoE feedback to adjust streaming quality, the ﬁeld heavily invests in research aimed at creating reliable and accurate QoE models (Jia et al. 2025). Another challenge is the energy consumption, which is a main concern across a live video streaming pipeline. Conventional machine and deep learning models oﬀer a solution to these problems by enabling energy-aware video encoding and quality adaptation.

**Fragmento 7 - p. 5 - score 3:**

3. Eﬃcient inference via linear state-space modeling: The inference procedure leverages the linear state-space formulation of Mamba to generate stable and computationally eﬃcient bandwidth predictions within each session, improving temporal smoothness and robustness. 4. QoE-oriented performance validation: Beyond prediction accuracy and error re- duction, the framework demonstrates more consistent QoE outcomes compared to Pensieve-PPO, highlighting its practical advantage for adaptive bitrate streaming. Architectural overview of the proposed MamBRA framework is shown in Figure 1. User session data are utilized for model training and validation, followed by an inference stage that performs adaptive bandwidth selection.

**Fragmento 8 - p. 7 - score 3:**

2025 Adversarial Inverse RL (AIRL) Generalizes to unseen network conditions +4.3–9.4% video quality, –0.054–6.2% stall Naseh et al. 2025 DRL with DDPG Edge-DASH Joint user–server bitrate allocation Higher QoE, fewer bitrate errors J. Zhang et al. 2025 PLL-ABR – DRL with PPO, LSTM & Attention Improves bitrate stability and prediction accuracy ∼28.5% QoE gain requirements, and an average QoE that is 7.5%–16.79% higher than previous methods. In 2020, researchers began addressing the gap in proactive video QoE prediction be- yond traditional QoS metrics. Dinaki et al. 2021 addressed the problem of proactively predicting video QoE beyond QoS metrics and delayed client measurements. A BiLSTM- CNN hybrid model was suggested, in which CNN recovers local patterns from multivariate time series and BiLSTM captures temporal dependencies.

**Fragmento 9 - p. 7 - score 3:**

2023 Federated Learning ABR Client-speciﬁc models without raw data exchange ∼10% QoE gain, reduced rebuﬀering D. Yang et al. 2023 Subepisodic DRL Separate buﬀering and playback memories for control stability Smoother bitrate, fewer stalls Darwich et al. 2024 CNN–RNN Hybrid Frame-level bitrate estimation for ﬁne-grained adaptation +16.6% QoE, +37.1% bitrate, –87.5% rebuﬀering Woo et al. 2024 GRU-Based Bandwidth & Buﬀer ABR Throughput prediction with minimized bitrate switching Up to +40% MOS Kang et al. 2024 RL Edge-Assisted ABR Multi-client edge-assisted adaptive streaming Improved fairness and QoE Wang et al. 2024 Adversarial Information Bottleneck + Imitation Learning Robust QoE modeling with reduced overﬁtting +7.3% QoE, +30% ranking Ling et al.

**Fragmento 10 - p. 8 - score 3:**

In order to maximize user QoE, Wei et al. 2022 pointed out that traditional adaptive bitrate (ABR) techniques frequently struggle to optimize bitrate selection and minimize rebuﬀering at the same time. As a quantum-inspired ABR control method, QuDASH was presented to get around these restrictions. To ﬁnd the best bitrates, it uses a Digital Annealer to solve a Quadratic Unconstrained Binary Optimization (QUBO) problem that models buﬀer conditions, bitrate ﬂuctuations, and video quality. Based on actual network traces, simulation results show that QuDASH outperforms current ABR techniques, at- taining the highest QoE in 68.2% of scenarios, conﬁrming its eﬃcacy in improving user experience. ABR adaptation under various networks and numerous QoE objectives was the main focus of the research conducted by Xu et al.

**Fragmento 11 - p. 9 - score 3:**

By increasing bitrate decision accuracy and stability, this method raises QoE. Experimental results show a QoE gain of about 28.5% across bandwidth usage, rebuﬀering, and playback smoothness parameters when compared to numerous state-of-the-art ABR algorithms. The review identiﬁes various research challenges and gaps in adaptive bitrate optimiza- tion for live streaming as follows: • Most techniques handle live streaming like VoD; live-speciﬁc latency restrictions are rarely addressed. • Many studies rely on synthetic or VoD traces due to the lack of realistic live-network datasets. • ML/DRL ABR models often show weak generalization to unseen network conditions. • Insuﬃcient analysis of failure modes and safety of learning-based ABR.

**Fragmento 12 - p. 11 - score 3:**

bufferDeficitSecs Seconds of video playback missing due to stalling. rebufferingSecs Seconds buﬀered between the last two segments. rebufferingCount Times buﬀering occurs between the last two seg- ments. Network bytesTransferred Bytes transferred since the start of the session. bandwidthMBPS Network bandwidth. Categorical Client deviceType {desktop, tv, tablet, mobile, . . . } deviceOS {windows, android, other, ios, web_os, . . . } browser {chrome, other, ﬁrefox, edge, . . . } player {web, app} playerDim 110 dimensions (width×height). The feature playerDim is obtained by merging two numeric columns in the original dataset, resulting in 110 distinct player dimension categories. The segment duration is ﬁxed at four seconds across all sessions.

**Fragmento 13 - p. 12 - score 3:**

where f is the original forward buﬀer seconds. This distinction is essential for improving model training and QoE analysis, as values outside the range [−30, 60] represent non-QoE behavior, which do not reﬂect perceptual video quality and should be excluded from learning and evaluation (Balachandran et al. 2013; Seufert et al. 2015; Yin et al. 2015; Mao et al. 2017). Applying this range preserves stall severity and buﬀer safety characteristics while eliminating unrealistic magnitudes, without discarding any rows. Extreme negative values typically arise from session resets, timestamp wraparounds, backward jumps in playback position, and cumulative subtraction bugs (Miller 2016; Allard et al. 2020). In contrast, extreme positive values are usually caused by paused playback, background tab buﬀering, seek-ahead artifacts, and segment prefetching during stalls (Almquist et al.

**Fragmento 14 - p. 17 - score 3:**

cisions are made continuously as new network observations arrive. Importantly, the SSM state is reset only at session boundaries, ensuring that temporal dependencies are learned and applied strictly within individual playback sessions. In summary, inference is performed in a fully online and stateful manner, leveraging the recurrent dynamics of Mamba to integrate historical context eﬃciently. The warm-up phase aligns the internal state with recent session dynamics, while step-by-step process- ing enables continuous, low-latency bandwidth prediction suitable for real-time adaptive bitrate control. 6 Results and Discussion In this section, various tests are presented that demonstrate the performance of the pro- posed MamBRA model in terms of loss, accuracy, and QoE.

**Fragmento 15 - p. 17 - score 3:**

First, the results of the training are presented in Subsection 6.1. Next, the model’s inference tests are detailed in Subsec- tion 6.2. Finally, the decision-making behavior of MamBRA is compared against the baseline method Pensieve-PPO under a ﬂuctuating network trace using QoE evaluation metric (Subsection 6.3). 6.1 Model Training Results For a sequence-prediction model like MamBRA, and by tracking the Huber loss, the gap between what MamBRA predicted and what the network actually delivered is measured. Figure 6 illustrates the Huber loss and accuracy for the training and validation. Figure 6: Huber loss versus accuracy To provide a comprehensive view of MamBRA model’s performance, we highlight the following analysis: 16

**Fragmento 16 - p. 21 - score 3:**

Inconsistent. While it reaches high scores, many sessions experience low QoE (as low as 0.0–0.4). 7 Conclusion and Future Work This study developed MamBRA model, a new bitrate adaptation framework for video stream- ing that employs Mamba for accurate session-level bandwidth prediction. The streaming dataset are recognized by fully disconnected user sessions and the model implements a su- pervised time-series learning technique that ensures temporal consistency while explicitly limiting cross-session information leaking. The conducted test demonstrates that MamBRA has remarkably reduces prediction errors (Huber and MSE) and improves temporal sta- bility of predicted bandwidths. A signiﬁcant ﬁnding of this research work is that Mamba’s linear state-space model allows for eﬃcient and stable computation, which makes it very appropriate for real-time use.

**Fragmento 17 - p. 22 - score 3:**

that can enhance bitrate selection in real-time. • Exploring the deployment of MamBRA in edge computing frameworks could further boost performance in multi-client scenario’s, minimizing latency and improving re- source allocation fairness. • Incorporating more sophisticated perceptual video quality metrics into the training objective may enhance the model’s performance to better match user satisfaction. • Testing and evaluating the proposed framework using various, modern network traces (e.g., 5G and Starlink) will guarantee its robustness to the growing of modern internet traﬃc. 8 Declarations Funding The authors received no ﬁnancial support for the research, authorship, and/or publication of this article.

**Fragmento 18 - p. 2 - score 2:**

During inference, it leverages the linear state-space formulation of Mamba to eﬃciently generate stable bandwidth predictions within each session. Experimen- tal results demonstrate reduced prediction error, improved accuracy, and enhanced temporal stability. The model achieves an overall inference accuracy of 93.94%, with session-level accuracy reaching as high as 97.32%. Furthermore, the predicted band- width achieves more consistent QoE scores compared to the PPO-based approach used in Pensieve. Keywords: SSM-Mamba, bitrate adaptation, video streaming, network bandwidth, QoE. 1

**Fragmento 19 - p. 3 - score 2:**

1 Introduction Internet video traﬃc has surged over the past two decades, accounting for over 65% of all web traﬃc (Sandvine 2023). This growth, fueled by video-on-demand and live streaming, strains network infrastructure and complicates the delivery of a consistent Quality of Expe- rience (QoE). To address these challenges, the industry has adopted HTTP-based adaptive streaming (HAS) as the standard delivery method (Abdullah et al. 2017). HAS divides video into segments at various bitrates, enabling clients to adjust quality dynamically based on network conditions while utilizing existing HTTP infrastructure for scalability and compatibility. Major standards like Microsoft’s Smooth Streaming (MSS) (Microsoft 2008; Stockhammer 2011), Apple’s HTTP Live Streaming (HLS) (Pantos et al.

**Fragmento 20 - p. 3 - score 2:**

2017; Apple Inc. 2024), and MPEG’s Dynamic Adaptive Streaming over HTTP (MPEG-DASH)(DASH Industry Forum 2024) have solidiﬁed HAS as the global norm. However, live streaming remains challenging as providers must balance low latency, high visual quality, and network eﬃciency (Yin et al. 2015; T.-Y. Huang et al. 2014). These com- peting demands under ﬂuctuating bandwidth have sparked ongoing research into bitrate adaptation and buﬀer management. Ultimately, the need to minimize rebuﬀering while maintaining stability continues to drive innovation in streaming algorithms and system design. 1.1 Challenges in Adaptive Bitrate (ABR) Streaming Streaming services use adaptive bitrate (ABR) algorithms to manage network bandwidth ﬂuctuations for better QoE (Spiteri et al.

**Fragmento 21 - p. 3 - score 2:**

Taha, Ali, et al. 2021 introduced an automated model to accurately evaluate and predict QoE for adaptive video streaming over wireless networks by utilizing objective performance metrics. Therefore, a QoE-aware adap- tive management system is proposed in order to reduce buﬀering and quality degradation by dynamically optimizing HD video streaming over wireless network environments (Taha, Canovas, et al. 2021). The beneﬁts of adaptive video streaming—better quality and user experience—come at the cost of high bandwidth consumption and excessive video traﬃc. Since this volume 2

**Fragmento 22 - p. 5 - score 2:**

From a QoE per- spective, the predicted bandwidth yields more consistent QoE scores than those obtained using the PPO-based strategy implemented in Pensieve (Mao et al. 2017; godka 2025), highlighting the eﬀectiveness of the proposed framework for adaptive bitrate streaming optimization. The main contributions of the proposed approach can be summarized as follows: 1. Novel dataset structuring at the session level: The dataset is reorganized into fully disjoint user sessions with heterogeneous numerical and categorical features, enabling realistic temporal modeling while explicitly preventing cross-session information leak- age. 2. Session-aware supervised training strategy: A time-series learning framework is de- signed where training is strictly performed at the session level, preserving sequential dependencies and ensuring fair generalization across independent user trajectories.

**Fragmento 23 - p. 5 - score 2:**

The resulting decisions are assessed using quantitative performance metrics, including loss, prediction accuracy, and QoE. Dataset User Session Sequences MamBRA Model Training & Validation Inference Stage Adaptive Bandwidth Selection Performance Evaluation Loss | Accuracy | QoE Figure 1: The overall architecture and processing pipeline of MamBRA 4

**Fragmento 24 - p. 6 - score 2:**

Therefore, a variety of optimization strategies were then investigated by researchers in an eﬀort to enhance bitrate adaptability. The goal of these strategies was to balance playback stability, re- buﬀering reduction, and video quality in order to improve QoE. Table 1 demonstrates the recent research on optimization algorithms that investigated to enhance QoE. Below a brief description of each algorithm is provided. Mao et al. 2017 discussed the drawbacks of conventional ABR algorithms in dynamic network scenarios. They presented Pensieve, a system based on reinforcement learning that trains a neural network to choose bitrate based on past streaming results. Evalua- tions revealed that it outperformed rate-based, buﬀer-based, and MPC schemes, improving average QoE by 12% to 25% and exhibiting strong performance in previously untested net- work circumstances.

**Fragmento 25 - p. 6 - score 2:**

The rest of the paper is organized as follows: Section 2 gives a review of the bitrate adaptation for live streaming using optimization techniques, while Section 3 describes the detailed structure of the Mamba framework and the SSM. Section 4 describes the dataset used to build the proposed model. Section 5 presents the proposed MamBRA model in detail. In Section 6, QoE is computed using the bandwidth values predicted by MamBRA, followed by a comparative evaluation against Pensieve-PPO. Finally, Section 7 identiﬁes upcoming trends and gaps in the literature and makes recommendations for further research. 2 Related Work Early studies on adaptive video streaming addressed the shortcomings of traditional rate- and buﬀer-based ABR methods under dynamic network conditions.

**Fragmento 26 - p. 6 - score 2:**

According to experimental assessments, the suggested system outperforms traditional ABR techniques in terms of average delivered bitrate by 14.31% and improves QoE by 16.2%. Key drawbacks of learning-based Adaptive Bit Rate (ABR) streaming were discussed by T. Huang et al. 2019, including low sample eﬃciency and inadequate perceptual video quality consideration. They presented Comyco, a video quality-aware ABR method that uses imitation learning and trains its neural network on expert trajectories produced by an instant solver. This approach maximizes the use of gathered data and reduces unnec- essary exploration. Comyco improves the overall QoE by choosing video chunks based on perceptual quality rather than just bitrate.


### 7.5. entrenamiento optimizacion pipeline

Palabras clave usadas: `training, train, trained, episode, epoch, optimizer, learning rate, loss function, minibatch, clipped, probability ratio, experience, simulation, simulator, emulation, testbed, fine-tuning, pretrain, learning task, meta-training, adaptation, oracle, auto-tuning, offline, online`

**Fragmento 1 - p. 8 - score 5:**

In order to maximize user QoE, Wei et al. 2022 pointed out that traditional adaptive bitrate (ABR) techniques frequently struggle to optimize bitrate selection and minimize rebuﬀering at the same time. As a quantum-inspired ABR control method, QuDASH was presented to get around these restrictions. To ﬁnd the best bitrates, it uses a Digital Annealer to solve a Quadratic Unconstrained Binary Optimization (QUBO) problem that models buﬀer conditions, bitrate ﬂuctuations, and video quality. Based on actual network traces, simulation results show that QuDASH outperforms current ABR techniques, at- taining the highest QoE in 68.2% of scenarios, conﬁrming its eﬃcacy in improving user experience. ABR adaptation under various networks and numerous QoE objectives was the main focus of the research conducted by Xu et al.

**Fragmento 2 - p. 14 - score 5:**

and the corresponding prediction target is the next-step bandwidth value yt+1. Using a stride of 1 generates a prediction target at every valid timestep within each session, resulting in maximally overlapping windows and dense supervision. This approach ensures that the model is trained to make bandwidth predictions at all decision points encountered during a session, closely aligning the training procedure with the online ABR setting, where bitrate adaptation decisions are made continuously throughout playback. The choice of a window length of 20 timesteps captures short-term temporal depen- dencies within a session, such as recent throughput ﬂuctuations and transient network conditions, while avoiding unnecessary long-range context that may span multiple, po- tentially heterogeneous sessions.

**Fragmento 3 - p. 15 - score 4:**

• RMSNorm and Linear Head: The output of the Mamba block is normalized using Root Mean Square Layer Normalization and then passed through a ﬁnal linear layer to project it to the target output size. • Prediction (Last Time Step): The model extracts the prediction from the ﬁnal time step to make its assessment. 3. Loss Functions and Optimization The diagram distinguishes how the model is evaluated during diﬀerent phases: Phase Gradient Status Loss Functions Used Optimizer Train Enabled Huber Loss AdamW Backprop Validation Disabled Huber Loss & MSE Loss N/A • Huber Loss: Used as the primary training objective. It is often preferred over MSE (Mean Squared Error) because it is less sensitive to outliers in the data.

**Fragmento 4 - p. 18 - score 4:**

6.2 Inference Tests Unlike the training phase, where the model adjusts its weights based on a loss function (like Huber loss), the inference test focuses on how the model actually acts in a real-world simulation. Over all dataset sessions used during inference, the model attains a mean squared error (MSE) of 3669.33, a root mean squared error (RMSE) of 60.58, a normalized RMSE (NRMSE, computed by normalizing the MSE over the range Max–Min) of 0.06, and an overall accuracy of 93.94%. The remainder of this subsection provides a detailed examination of these performance metrics at the individual session level. 6.2.1 Loss Figure 7 presents a performance breakdown of a model across four features: deviceOS, deviceType, browser, and player.

**Fragmento 5 - p. 13 - score 3:**

Numeric features are standardized using z-score normalization (standard scaling), where the mean and standard deviation are computed from the training split and subsequently applied to validation data. Categorical features are transformed using feature-wise label encoding, mapping each categorical value to an integer index. These encoded categorical features are then used as inputs to learned embedding layers within the model. The dataset is divided into training, validation, and testing sets using a 70%/10%/20% split. The detailed procedures for preprocessing, normalization, windowing, and data partitioning are illustrated in Figure 3. clean-up and split Original data Test data Numeric features Categorical features Train-Validation data Scaler Encoders Preprocesser group by sessionID generate sequences per session group (window=20) split to train and validation Validation data Train data 100% 80% 20% 70% 10% Figure 3: Dataset preparation (clean-up, normalization, sequencing and splitting) The dataset is ﬁrst partitioned into disjoint user sessions, where each session corre- sponds to a continuous playback episode.

**Fragmento 6 - p. 15 - score 3:**

• AdamW: The optimizer used to update the model weights based on the calcu- lated gradients during the training phase. Essentially, the model takes a mix of categorical and numerical data, embeds them, processes them through a Mamba sequential architecture, and uses Huber loss to guide the AdamW optimizer during training. During validation, it checks performance using both Huber and MSE losses to ensure the model generalizes well without updating the weights. 14

**Fragmento 7 - p. 16 - score 3:**

5.3 Inference Procedure At inference time, MamBRA is applied in an online, sequential manner to generate bandwidth predictions within each user session. In contrast to training, where ﬁxed-length sliding windows are used to construct supervised samples, inference does not rely on windowing or stride-based segmentation. Figure 5 illustrates the inference procedure of MamBRA. Test data (one session) Numeric features (-bandwidthMBPS) Categorical features bandwidthMBPS Scaler (Standard) Encoders Preprocesser Warm-up phase (window=20) MamBRA Prediction Inverse-scaler (Standard) predicted bandwidth Huber, MSE, RMSE, NRMSE Accuracy CDF Anlaysis →MOS →QoE Figure 5: Inference process of MamBRA for one session of the test data For a given session s of length Ts with a sequence of preprocessed input features x(s) t Ts t=1, the model processes observations one timestep at a time, updating its internal recurrent state at each step.

**Fragmento 8 - p. 18 - score 3:**

• Correlation between “Loss and Accuracy”: From Figure 6 we can see that when Huber loss drops quickly in the ﬁrst 20 epochs accuracy goes up sharply. This shows that when Huber loss goes down accuracy goes up meaning that the model is eﬀectively optimizing its internal weights to minimize prediction errors. • Learning stability: The training accuracy, shown as a solid line keeps going up and until it reaches 93%. At that point the validation’s accuracy, represented by a red dashed line levels oﬀat, around 88%. This high validation accuracy shows that the Mamba state-space architecture is successfully capturing the complex temporal dependencies of the network traces. • Generalization Gap: The model appears to generalize well to unseen, unexplored network conditions, as indicated by the narrow diﬀerence between the training and validation accuracy curves.

**Fragmento 9 - p. 2 - score 2:**

However, as user demands for high quality and low latency increase, using eﬃcient video streaming systems is getting harder. In addition to taxing network resources, the increase in video traﬃc is lower- ing video quality. Deep and transformer learning algorithms use data-driven methods to optimize video delivery, enhance QoE, and lessen network congestion in order to overcome these obstacles. Mamba utilizes the eﬃcient linear complexity of selective state space model (SSM) mechanism to process data sequences more eﬀectively. This paper proposes an adaptive video streaming framework (MamBRA) based on Mamba for session-level bandwidth prediction. The model is trained in a supervised time-series manner on disjoint user sessions to prevent information leakage and preserve temporal structure.

**Fragmento 10 - p. 4 - score 2:**

This approach seeks to improve energy usage without sacriﬁcing the user experience (Tien et al. 2025; X. Yang et al. 2024). 1.2 Machine Learning–Based Sequence Modeling for Bitrate Adaptation Machine learning–based approaches have been extensively adopted for bitrate adaptation in video streaming, with sequence modeling architectures such as Transformers and recurrent neural networks (RNNs) playing a particularly prominent role (Mao et al. 2017). Recently, Mamba (selective structured state-space sequence architecture) has emerged as a powerful alternative to Transformer-based models (Gu and Dao 2024). Unlike self- attention mechanisms whose computational complexity grows quadratically with sequence length, Mamba leverages selective state-space modeling to achieve linear-time complexity, enabling scalable processing of very long sequences while maintaining competitive repre- sentational capacity.

**Fragmento 11 - p. 4 - score 2:**

Its design integrates continuous-time state-space formulations with data-dependent parameterization, allowing eﬃcient parallel training and fast autoregressive inference. Due to these properties, Mamba demonstrates strong long-range dependency modeling and improved memory eﬃciency compared to traditional Transformers (Patro et al. 2025; Somvanshi et al. 2025). Recent studies have successfully extended Mamba to multiple domains (including vision, video understanding, and multimodal learning) highlighting its adaptability and robustness across tasks that require long-context modeling (G. Zhang et al. 2024; Liu et al. 2026; H. Zhang et al. 2024). These characteristics make Mamba particularly attractive for sequential decision-making and time-series applications such as adaptive video streaming, where eﬃcient long-horizon modeling and low inference latency are critical.

**Fragmento 12 - p. 5 - score 2:**

From a QoE per- spective, the predicted bandwidth yields more consistent QoE scores than those obtained using the PPO-based strategy implemented in Pensieve (Mao et al. 2017; godka 2025), highlighting the eﬀectiveness of the proposed framework for adaptive bitrate streaming optimization. The main contributions of the proposed approach can be summarized as follows: 1. Novel dataset structuring at the session level: The dataset is reorganized into fully disjoint user sessions with heterogeneous numerical and categorical features, enabling realistic temporal modeling while explicitly preventing cross-session information leak- age. 2. Session-aware supervised training strategy: A time-series learning framework is de- signed where training is strictly performed at the session level, preserving sequential dependencies and ensuring fair generalization across independent user trajectories.

**Fragmento 13 - p. 5 - score 2:**

3. Eﬃcient inference via linear state-space modeling: The inference procedure leverages the linear state-space formulation of Mamba to generate stable and computationally eﬃcient bandwidth predictions within each session, improving temporal smoothness and robustness. 4. QoE-oriented performance validation: Beyond prediction accuracy and error re- duction, the framework demonstrates more consistent QoE outcomes compared to Pensieve-PPO, highlighting its practical advantage for adaptive bitrate streaming. Architectural overview of the proposed MamBRA framework is shown in Figure 1. User session data are utilized for model training and validation, followed by an inference stage that performs adaptive bandwidth selection.

**Fragmento 14 - p. 5 - score 2:**

impairments (Ran et al. 2020; Artioli et al. 2024). Therefore, the dataset is organized into multiple disjoint user sessions. To prevent information leakage and preserve temporal con- sistency, a supervised time-series learning strategy is employed, where training is conducted strictly at the session level. During inference, the proposed approach exploits the linear state-space formulation of Mamba to eﬃciently generate bandwidth predictions within each individual user session, enabling scalable and stable sequential modeling. Experimental re- sults demonstrate signiﬁcant error reduction and improved predictive accuracy. Moreover, the predicted bandwidth trajectories exhibit enhanced temporal stability.

**Fragmento 15 - p. 5 - score 2:**

The resulting decisions are assessed using quantitative performance metrics, including loss, prediction accuracy, and QoE. Dataset User Session Sequences MamBRA Model Training & Validation Inference Stage Adaptive Bandwidth Selection Performance Evaluation Loss | Accuracy | QoE Figure 1: The overall architecture and processing pipeline of MamBRA 4

**Fragmento 16 - p. 6 - score 2:**

This results in faster training, fewer sample 5

**Fragmento 17 - p. 7 - score 2:**

Table 1: Enhancement of QoE through the evolution of adaptation algorithms Investigation Adaptation Algorithm Key Contributions QoE Improvements Mao et al. 2017 Pensieve – RL Neural network selects bitrate based on past streaming states +12–25% average QoE Sengupta et al. 2018 HotDASH – Actor–Critic & Cascaded DRL Incorporates user preferences and prefetching strategies +14.31% bitrate, +16.2% QoE T. Huang et al. 2019 Comyco – Imitation Learning Trains on expert trajectories to reduce exploration overhead +7.5–16.79% perceptual QoE Dinaki et al. 2021 BiLSTM–CNN Hybrid Proactive QoE prediction beyond traditional QoS metrics Lowest MAE and RMSE Wei et al. 2022 QuDASH – Quantum ABR Solves QUBO formulation for optimal bitrate selection Highest QoE in 68.2% of scenarios Xu et al.

**Fragmento 18 - p. 9 - score 2:**

While real-time transcoding takes care of edge storage constraints, the DDPG agent dynamically chooses the best streaming sources; edge, macro, or cloud and matching bitrates. In 5G- enabled multi-tier video streaming, simulations demonstrate that this strategy outperforms conventional network-driven and hybrid edge-cloud techniques by improving QoE, lowering bitrate errors, and minimizing transcoding violations. J. Zhang et al. 2025 suggest Predictive LSTM Local Attention ABR (PLL-ABR), an Adaptive Bitrate (ABR) algorithm based on Deep Reinforcement Learning (DRL) that makes use of the Proximal Policy Optimization (PPO) framework enhanced with dual clipping, Long Short-Term Memory (LSTM) networks, and local attention mechanisms.

**Fragmento 19 - p. 10 - score 2:**

4 Dataset Description and Preparation For modeling the proposed system, we utilized the comprehensive statistical dataset intro- duced by Teixeira et al. 2021. Fourteen features were selected and adapted for use during both the training and inference phases of our model. A total of approximately 1.4 million records, distributed across 1,966 user sessions, were extracted and preprocessed for this study. 9

**Fragmento 20 - p. 12 - score 2:**

2018; Xie et al. 2024). Figure 2 illustrates the distribution of rows and sessions across the diﬀerent classes within the four categorical features deviceType, deviceOS, browser and player. The length of each bar indicates the number of rows associated with a given feature, while the numbers displayed on the bars denote the corresponding number of sessions. The majority of user sessions were conducted via the Chrome web browser on desktop comput- ers running the Windows operating system. Mobile phones and TV devices running the Android operating system accounted for the second and third highest number of sessions, respectively. Figure 2: Distribution of sessions and rows among categorical features 5 Training and Inference Procedures of the MamBRA Model We train the proposed MamBRA using session-aware sliding windows of 20 timesteps with stride 1, applied independently within each user session after standardizing numeric fea- 11

**Fragmento 21 - p. 12 - score 2:**

where f is the original forward buﬀer seconds. This distinction is essential for improving model training and QoE analysis, as values outside the range [−30, 60] represent non-QoE behavior, which do not reﬂect perceptual video quality and should be excluded from learning and evaluation (Balachandran et al. 2013; Seufert et al. 2015; Yin et al. 2015; Mao et al. 2017). Applying this range preserves stall severity and buﬀer safety characteristics while eliminating unrealistic magnitudes, without discarding any rows. Extreme negative values typically arise from session resets, timestamp wraparounds, backward jumps in playback position, and cumulative subtraction bugs (Miller 2016; Allard et al. 2020). In contrast, extreme positive values are usually caused by paused playback, background tab buﬀering, seek-ahead artifacts, and segment prefetching during stalls (Almquist et al.

**Fragmento 22 - p. 13 - score 2:**

tures and embedding categorical features. At inference time, the model operates in a fully online and stateful manner, processing observations sequentially without windowing. After a brief 20-timestep warm-up to initialize the SSM state, the model produces per-timestep bandwidth predictions, with the state reset only at session boundaries. 5.1 Feature Preprocessing and Session-Aware Sliding-Window Segmentation The dataset consists of both numeric (throughput and buﬀer occupancy) and categorical (device indicators) features, and is organized into disjoint user sessions, each correspond- ing to a continuous playback episode. All preprocessing and windowing operations are performed at the session level to prevent information leakage across sessions.

**Fragmento 23 - p. 13 - score 2:**

Sliding-window segmentation is performed inde- pendently within each session to prevent information leakage across session boundaries. For a given session s of length Ts consisting of a sequence of network and playback feature vectors {xt}Ts t=1, training and validation samples are constructed using a window size of 20 timesteps and a stride of 1. At each timestep t, the model input is deﬁned as Xt = [xt−19, xt−18, . . . , xt] , 12

**Fragmento 24 - p. 14 - score 2:**

Session-level windowing further ensures that temporal dependencies are learned strictly within coherent playback contexts, improving both mod- eling ﬁdelity and evaluation validity. 5.2 MamBRA Training and Validation Pipelines The diagram shown in Figure 4 illustrates the architecture and training workﬂow of a machine learning model utilizing a Mamba Block (a State Space Model architecture). The ﬂow is divided into two main paths: the training pipeline (solid lines) and the validation pipeline (dashed lines). Numeric features Categorical features Train data Concatenate Categorical Embeddings (per feature) Numeric features Categorical features Validation data Input Projection Linear Mamba Block (Sequence Scan) RMSNorm Linear Head Prediction (Last Time Step) Huber Loss AdamW Backprop gradients enabled Huber Loss MSE Loss no gradients Core MamBRA train validation shared Figure 4: Training and validation process of MamBRA model 1.

**Fragmento 25 - p. 14 - score 2:**

Data Input and Preprocessing The model handles two types of data from both the training and validation sets: 13

**Fragmento 26 - p. 16 - score 2:**

The SSM maintains a hidden state that summarizes past information and evolves according to the learned state transition dynamics. This enables the model to incorporate arbitrarily long temporal context without explicitly storing past inputs. To ensure a well-initialized internal state, inference begins with a warm-up phase, during which the ﬁrst W timesteps (with W = 20, matching the training window length) are fed sequentially into the model without using the corresponding outputs for evaluation or decision-making. After this warm-up, the model generates a bandwidth prediction at every subsequent timestep. Formally, for each timestep t ≥W, the model updates its internal state using the current input x(s) t and produces a prediction ˆy(s) t+1 for the next-step bandwidth: (ˆy(s) t+1, h(s) t ) = fSSM(x(s) t , h(s) t−1), where h(s) t denotes the SSM hidden state at timestep t.


### 7.6. datos trazas datasets origen

Palabras clave usadas: `dataset, datasets, trace, traces, network trace, bandwidth trace, real-world, FCC, HSDPA, Norway, LTE, 4G, 5G, WiFi, WLAN, Mahimahi, emulation, testbed, Puffer, data, sessions, users, video, chunk, streaming server`

**Fragmento 1 - p. 8 - score 7:**

2023. The authors suggested a customized federated learning ABR algorithm that applies a tailoring phase and aggregates knowledge from clients’ local models without exchanging raw data. In addition to improvements from context factors and personalization, experiments on 3G, 4G, and WiFi traces showed the highest overall QoE, the lowest rebuﬀering, and smoothness penalties, with an improvement of about 10% above local models, showing substantial adaptation. RL-based ABR algorithms are inadequate for optimizing QoE, especially during initial buﬀering and playback, according to D. Yang et al. 2023. They suggested a subepisodic DRL method that separated video sessions into formal playback (FP) and initial buﬀer- ing (IB) with distinct replay and optimization memories, all of which were connected by a reward mechanism based on QoE.

**Fragmento 2 - p. 9 - score 5:**

By increasing bitrate decision accuracy and stability, this method raises QoE. Experimental results show a QoE gain of about 28.5% across bandwidth usage, rebuﬀering, and playback smoothness parameters when compared to numerous state-of-the-art ABR algorithms. The review identiﬁes various research challenges and gaps in adaptive bitrate optimiza- tion for live streaming as follows: • Most techniques handle live streaming like VoD; live-speciﬁc latency restrictions are rarely addressed. • Many studies rely on synthetic or VoD traces due to the lack of realistic live-network datasets. • ML/DRL ABR models often show weak generalization to unseen network conditions. • Insuﬃcient analysis of failure modes and safety of learning-based ABR.

**Fragmento 3 - p. 22 - score 5:**

that can enhance bitrate selection in real-time. • Exploring the deployment of MamBRA in edge computing frameworks could further boost performance in multi-client scenario’s, minimizing latency and improving re- source allocation fairness. • Incorporating more sophisticated perceptual video quality metrics into the training objective may enhance the model’s performance to better match user satisfaction. • Testing and evaluating the proposed framework using various, modern network traces (e.g., 5G and Starlink) will guarantee its robustness to the growing of modern internet traﬃc. 8 Declarations Funding The authors received no ﬁnancial support for the research, authorship, and/or publication of this article.

**Fragmento 4 - p. 8 - score 4:**

Based on enhanced HE-EMDQN frameworks, this technique allowed for smoother, more eﬃcient bitrate adaption, decreased inter-phase in- terference, and increased sample eﬃciency. Better initial buﬀering performance, faster convergence, fewer rebuﬀering events, and improved QoE were observed in experimental ﬁndings on both synthetic and actual network traces compared to conventional RL and episodic DRL approaches. Optimizing video quality in dynamic networks while reducing bandwidth and playback interruptions was studied by Darwich et al. 2024. With RNN estimating the ideal bitrate per frame and CNN extracting information from video frames, they suggested a hybrid CNN-RNN architecture. By reducing rebuﬀering by 87.5%, improving QoE by 16.6%, and increasing average bitrate by 37.1%, experimental results demonstrated improved user experience and smoother playing compared to current ABR techniques.

**Fragmento 5 - p. 8 - score 4:**

In order to maximize user QoE, Wei et al. 2022 pointed out that traditional adaptive bitrate (ABR) techniques frequently struggle to optimize bitrate selection and minimize rebuﬀering at the same time. As a quantum-inspired ABR control method, QuDASH was presented to get around these restrictions. To ﬁnd the best bitrates, it uses a Digital Annealer to solve a Quadratic Unconstrained Binary Optimization (QUBO) problem that models buﬀer conditions, bitrate ﬂuctuations, and video quality. Based on actual network traces, simulation results show that QuDASH outperforms current ABR techniques, at- taining the highest QoE in 68.2% of scenarios, conﬁrming its eﬃcacy in improving user experience. ABR adaptation under various networks and numerous QoE objectives was the main focus of the research conducted by Xu et al.

**Fragmento 6 - p. 11 - score 4:**

bufferDeficitSecs Seconds of video playback missing due to stalling. rebufferingSecs Seconds buﬀered between the last two segments. rebufferingCount Times buﬀering occurs between the last two seg- ments. Network bytesTransferred Bytes transferred since the start of the session. bandwidthMBPS Network bandwidth. Categorical Client deviceType {desktop, tv, tablet, mobile, . . . } deviceOS {windows, android, other, ios, web_os, . . . } browser {chrome, other, ﬁrefox, edge, . . . } player {web, app} playerDim 110 dimensions (width×height). The feature playerDim is obtained by merging two numeric columns in the original dataset, resulting in 110 distinct player dimension categories. The segment duration is ﬁxed at four seconds across all sessions.

**Fragmento 7 - p. 18 - score 4:**

6.2 Inference Tests Unlike the training phase, where the model adjusts its weights based on a loss function (like Huber loss), the inference test focuses on how the model actually acts in a real-world simulation. Over all dataset sessions used during inference, the model attains a mean squared error (MSE) of 3669.33, a root mean squared error (RMSE) of 60.58, a normalized RMSE (NRMSE, computed by normalizing the MSE over the range Max–Min) of 0.06, and an overall accuracy of 93.94%. The remainder of this subsection provides a detailed examination of these performance metrics at the individual session level. 6.2.1 Loss Figure 7 presents a performance breakdown of a model across four features: deviceOS, deviceType, browser, and player.

**Fragmento 8 - p. 21 - score 4:**

Inconsistent. While it reaches high scores, many sessions experience low QoE (as low as 0.0–0.4). 7 Conclusion and Future Work This study developed MamBRA model, a new bitrate adaptation framework for video stream- ing that employs Mamba for accurate session-level bandwidth prediction. The streaming dataset are recognized by fully disconnected user sessions and the model implements a su- pervised time-series learning technique that ensures temporal consistency while explicitly limiting cross-session information leaking. The conducted test demonstrates that MamBRA has remarkably reduces prediction errors (Huber and MSE) and improves temporal sta- bility of predicted bandwidths. A signiﬁcant ﬁnding of this research work is that Mamba’s linear state-space model allows for eﬃcient and stable computation, which makes it very appropriate for real-time use.

**Fragmento 9 - p. 2 - score 3:**

However, as user demands for high quality and low latency increase, using eﬃcient video streaming systems is getting harder. In addition to taxing network resources, the increase in video traﬃc is lower- ing video quality. Deep and transformer learning algorithms use data-driven methods to optimize video delivery, enhance QoE, and lessen network congestion in order to overcome these obstacles. Mamba utilizes the eﬃcient linear complexity of selective state space model (SSM) mechanism to process data sequences more eﬀectively. This paper proposes an adaptive video streaming framework (MamBRA) based on Mamba for session-level bandwidth prediction. The model is trained in a supervised time-series manner on disjoint user sessions to prevent information leakage and preserve temporal structure.

**Fragmento 10 - p. 4 - score 3:**

1.3 Research Contributions In this research, we propose MamBRA; an adaptive video streaming framework based on the Mamba architecture for accurate session-level bandwidth prediction. The model is developed and evaluated on a comprehensive dataset comprising diverse numerical and categorical features (Teixeira et al. 2021). User perception of streaming quality is inher- ently subjective; viewers exhibit diverse sensitivities to video artifacts and network-induced 3

**Fragmento 11 - p. 5 - score 3:**

From a QoE per- spective, the predicted bandwidth yields more consistent QoE scores than those obtained using the PPO-based strategy implemented in Pensieve (Mao et al. 2017; godka 2025), highlighting the eﬀectiveness of the proposed framework for adaptive bitrate streaming optimization. The main contributions of the proposed approach can be summarized as follows: 1. Novel dataset structuring at the session level: The dataset is reorganized into fully disjoint user sessions with heterogeneous numerical and categorical features, enabling realistic temporal modeling while explicitly preventing cross-session information leak- age. 2. Session-aware supervised training strategy: A time-series learning framework is de- signed where training is strictly performed at the session level, preserving sequential dependencies and ensuring fair generalization across independent user trajectories.

**Fragmento 12 - p. 5 - score 3:**

impairments (Ran et al. 2020; Artioli et al. 2024). Therefore, the dataset is organized into multiple disjoint user sessions. To prevent information leakage and preserve temporal con- sistency, a supervised time-series learning strategy is employed, where training is conducted strictly at the session level. During inference, the proposed approach exploits the linear state-space formulation of Mamba to eﬃciently generate bandwidth predictions within each individual user session, enabling scalable and stable sequential modeling. Experimental re- sults demonstrate signiﬁcant error reduction and improved predictive accuracy. Moreover, the predicted bandwidth trajectories exhibit enhanced temporal stability.

**Fragmento 13 - p. 6 - score 3:**

The rest of the paper is organized as follows: Section 2 gives a review of the bitrate adaptation for live streaming using optimization techniques, while Section 3 describes the detailed structure of the Mamba framework and the SSM. Section 4 describes the dataset used to build the proposed model. Section 5 presents the proposed MamBRA model in detail. In Section 6, QoE is computed using the bandwidth values predicted by MamBRA, followed by a comparative evaluation against Pensieve-PPO. Finally, Section 7 identiﬁes upcoming trends and gaps in the literature and makes recommendations for further research. 2 Related Work Early studies on adaptive video streaming addressed the shortcomings of traditional rate- and buﬀer-based ABR methods under dynamic network conditions.

**Fragmento 14 - p. 6 - score 3:**

According to experimental assessments, the suggested system outperforms traditional ABR techniques in terms of average delivered bitrate by 14.31% and improves QoE by 16.2%. Key drawbacks of learning-based Adaptive Bit Rate (ABR) streaming were discussed by T. Huang et al. 2019, including low sample eﬃciency and inadequate perceptual video quality consideration. They presented Comyco, a video quality-aware ABR method that uses imitation learning and trains its neural network on expert trajectories produced by an instant solver. This approach maximizes the use of gathered data and reduces unnec- essary exploration. Comyco improves the overall QoE by choosing video chunks based on perceptual quality rather than just bitrate.

**Fragmento 15 - p. 10 - score 3:**

4 Dataset Description and Preparation For modeling the proposed system, we utilized the comprehensive statistical dataset intro- duced by Teixeira et al. 2021. Fourteen features were selected and adapted for use during both the training and inference phases of our model. A total of approximately 1.4 million records, distributed across 1,966 user sessions, were extracted and preprocessed for this study. 9

**Fragmento 16 - p. 11 - score 3:**

The selected features are grouped into several categories, including session-level, network-level, and client-level attributes. The dataset consists of numerous client ses- sions recorded as streaming events at 4-second intervals, providing playback statistics and related metrics corresponding to the aforementioned categories, as summarized in Table 2. Table 2: Segment downloads, stream switching, network, and buﬀering behavior of the dataset (Teixeira et al. 2021). Type Category Feature Description Numeric Session sessionID The player’s session number. sequenceID A number associated with each video segment (event) within a session. Time videoSecs Seconds viewed between the last two segments. bufferForwardSecs Seconds of video buﬀered but not viewed yet.

**Fragmento 17 - p. 13 - score 3:**

Numeric features are standardized using z-score normalization (standard scaling), where the mean and standard deviation are computed from the training split and subsequently applied to validation data. Categorical features are transformed using feature-wise label encoding, mapping each categorical value to an integer index. These encoded categorical features are then used as inputs to learned embedding layers within the model. The dataset is divided into training, validation, and testing sets using a 70%/10%/20% split. The detailed procedures for preprocessing, normalization, windowing, and data partitioning are illustrated in Figure 3. clean-up and split Original data Test data Numeric features Categorical features Train-Validation data Scaler Encoders Preprocesser group by sessionID generate sequences per session group (window=20) split to train and validation Validation data Train data 100% 80% 20% 70% 10% Figure 3: Dataset preparation (clean-up, normalization, sequencing and splitting) The dataset is ﬁrst partitioned into disjoint user sessions, where each session corre- sponds to a continuous playback episode.

**Fragmento 18 - p. 13 - score 3:**

tures and embedding categorical features. At inference time, the model operates in a fully online and stateful manner, processing observations sequentially without windowing. After a brief 20-timestep warm-up to initialize the SSM state, the model produces per-timestep bandwidth predictions, with the state reset only at session boundaries. 5.1 Feature Preprocessing and Session-Aware Sliding-Window Segmentation The dataset consists of both numeric (throughput and buﬀer occupancy) and categorical (device indicators) features, and is organized into disjoint user sessions, each correspond- ing to a continuous playback episode. All preprocessing and windowing operations are performed at the session level to prevent information leakage across sessions.

**Fragmento 19 - p. 18 - score 3:**

• Correlation between “Loss and Accuracy”: From Figure 6 we can see that when Huber loss drops quickly in the ﬁrst 20 epochs accuracy goes up sharply. This shows that when Huber loss goes down accuracy goes up meaning that the model is eﬀectively optimizing its internal weights to minimize prediction errors. • Learning stability: The training accuracy, shown as a solid line keeps going up and until it reaches 93%. At that point the validation’s accuracy, represented by a red dashed line levels oﬀat, around 88%. This high validation accuracy shows that the Mamba state-space architecture is successfully capturing the complex temporal dependencies of the network traces. • Generalization Gap: The model appears to generalize well to unseen, unexplored network conditions, as indicated by the narrow diﬀerence between the training and validation accuracy curves.

**Fragmento 20 - p. 20 - score 3:**

Desktop TV Mobile Tablet Sessions = 265 Sessions = 71 Sessions = 45 Sessions = 24 Accuracy ≈92.763 Accuracy ≈92.169 Accuracy ≈96.620 Accuracy ≈85.794 Figure 8: Comparison between measured bandwidth (bandwidthMBPS) and model- predicted bandwidth (predictedMBPS) across device types. MOS = 1 + 4 · log10 (bps + 1) −log10 (minbps + 1) log10 (maxbps + 1) −log10 (minbps + 1) QoE = (MOS −1) · 4 where bps is the predicted network’s bandwidth that MamBRA model calculated. Figure 9b illustrates and compares the Mean QoE scores across the four diﬀerent device types tv, desktop, mobile, and tablet. The data suggests that larger-screen devices (desktops and TVs) generally provide a higher QoE than portable devices (tablets and mobiles) in this speciﬁc dataset.

**Fragmento 21 - p. 25 - score 3:**

Teixeira, Thiago, Bo Zhang, and Yuriy Reznik (2021). “Adaptive Streaming Playback Statistics Dataset”. In: Proceedings of the 12th ACM Multimedia Systems Conference, pp. 248–254. doi: 10.1145/3458305.3478444. Ran, Dezhi et al. (2020). “Preference-aware Dynamic Bitrate Adaptation for Mobile Short- form Video Feed Streaming”. In: IEEE Access 8, pp. 220083–220094. doi: 10.1109/ ACCESS.2020.3042619. Artioli, Emanuele, Farzad Tashtarian, and Christian Timmerer (2024). “DIGITWISE: Dig- ital Twin-based Modeling of Adaptive Video Streaming Engagement”. In: Proceedings of the 15th ACM Multimedia Systems Conference, pp. 78–88. doi: 10.1145/3625468. 3647613. godka (2025). Pensieve-PPO: The simplest implementation of Pensieve via state-of-the- art RL algorithms (PPO, DQN, SAC).

**Fragmento 22 - p. 4 - score 2:**

This approach seeks to improve energy usage without sacriﬁcing the user experience (Tien et al. 2025; X. Yang et al. 2024). 1.2 Machine Learning–Based Sequence Modeling for Bitrate Adaptation Machine learning–based approaches have been extensively adopted for bitrate adaptation in video streaming, with sequence modeling architectures such as Transformers and recurrent neural networks (RNNs) playing a particularly prominent role (Mao et al. 2017). Recently, Mamba (selective structured state-space sequence architecture) has emerged as a powerful alternative to Transformer-based models (Gu and Dao 2024). Unlike self- attention mechanisms whose computational complexity grows quadratically with sequence length, Mamba leverages selective state-space modeling to achieve linear-time complexity, enabling scalable processing of very long sequences while maintaining competitive repre- sentational capacity.

**Fragmento 23 - p. 4 - score 2:**

Its design integrates continuous-time state-space formulations with data-dependent parameterization, allowing eﬃcient parallel training and fast autoregressive inference. Due to these properties, Mamba demonstrates strong long-range dependency modeling and improved memory eﬃciency compared to traditional Transformers (Patro et al. 2025; Somvanshi et al. 2025). Recent studies have successfully extended Mamba to multiple domains (including vision, video understanding, and multimodal learning) highlighting its adaptability and robustness across tasks that require long-context modeling (G. Zhang et al. 2024; Liu et al. 2026; H. Zhang et al. 2024). These characteristics make Mamba particularly attractive for sequential decision-making and time-series applications such as adaptive video streaming, where eﬃcient long-horizon modeling and low inference latency are critical.

**Fragmento 24 - p. 4 - score 2:**

of video data contributes to congestion, elevated costs, and high energy usage (George et al. 2025), among other issues, developing video traﬃc optimization methods is critically important. Furthermore, delivering high video quality and a positive QoE remains a core objective in video streaming. Since algorithms rely on QoE feedback to adjust streaming quality, the ﬁeld heavily invests in research aimed at creating reliable and accurate QoE models (Jia et al. 2025). Another challenge is the energy consumption, which is a main concern across a live video streaming pipeline. Conventional machine and deep learning models oﬀer a solution to these problems by enabling energy-aware video encoding and quality adaptation.

**Fragmento 25 - p. 5 - score 2:**

The resulting decisions are assessed using quantitative performance metrics, including loss, prediction accuracy, and QoE. Dataset User Session Sequences MamBRA Model Training & Validation Inference Stage Adaptive Bandwidth Selection Performance Evaluation Loss | Accuracy | QoE Figure 1: The overall architecture and processing pipeline of MamBRA 4

**Fragmento 26 - p. 9 - score 2:**

While real-time transcoding takes care of edge storage constraints, the DDPG agent dynamically chooses the best streaming sources; edge, macro, or cloud and matching bitrates. In 5G- enabled multi-tier video streaming, simulations demonstrate that this strategy outperforms conventional network-driven and hybrid edge-cloud techniques by improving QoE, lowering bitrate errors, and minimizing transcoding violations. J. Zhang et al. 2025 suggest Predictive LSTM Local Attention ABR (PLL-ABR), an Adaptive Bitrate (ABR) algorithm based on Deep Reinforcement Learning (DRL) that makes use of the Proximal Policy Optimization (PPO) framework enhanced with dual clipping, Long Short-Term Memory (LSTM) networks, and local attention mechanisms.


### 7.7. evaluacion baselines experimentos

Palabras clave usadas: `evaluation, experiment, experiments, baseline, baselines, compare, comparison, Pensieve, BBA, BOLA, MPC, RobustMPC, FastMPC, A3C, PPO, DQN, SODA, Oboe, MetaABR, results, outperform, ablation, scenario, test`

**Fragmento 1 - p. 17 - score 7:**

First, the results of the training are presented in Subsection 6.1. Next, the model’s inference tests are detailed in Subsec- tion 6.2. Finally, the decision-making behavior of MamBRA is compared against the baseline method Pensieve-PPO under a ﬂuctuating network trace using QoE evaluation metric (Subsection 6.3). 6.1 Model Training Results For a sequence-prediction model like MamBRA, and by tracking the Huber loss, the gap between what MamBRA predicted and what the network actually delivered is measured. Figure 6 illustrates the Huber loss and accuracy for the training and validation. Figure 6: Huber loss versus accuracy To provide a comprehensive view of MamBRA model’s performance, we highlight the following analysis: 16

**Fragmento 2 - p. 6 - score 6:**

Therefore, a variety of optimization strategies were then investigated by researchers in an eﬀort to enhance bitrate adaptability. The goal of these strategies was to balance playback stability, re- buﬀering reduction, and video quality in order to improve QoE. Table 1 demonstrates the recent research on optimization algorithms that investigated to enhance QoE. Below a brief description of each algorithm is provided. Mao et al. 2017 discussed the drawbacks of conventional ABR algorithms in dynamic network scenarios. They presented Pensieve, a system based on reinforcement learning that trains a neural network to choose bitrate based on past streaming results. Evalua- tions revealed that it outperformed rate-based, buﬀer-based, and MPC schemes, improving average QoE by 12% to 25% and exhibiting strong performance in previously untested net- work circumstances.

**Fragmento 3 - p. 2 - score 4:**

During inference, it leverages the linear state-space formulation of Mamba to eﬃciently generate stable bandwidth predictions within each session. Experimen- tal results demonstrate reduced prediction error, improved accuracy, and enhanced temporal stability. The model achieves an overall inference accuracy of 93.94%, with session-level accuracy reaching as high as 97.32%. Furthermore, the predicted band- width achieves more consistent QoE scores compared to the PPO-based approach used in Pensieve. Keywords: SSM-Mamba, bitrate adaptation, video streaming, network bandwidth, QoE. 1

**Fragmento 4 - p. 8 - score 4:**

Based on enhanced HE-EMDQN frameworks, this technique allowed for smoother, more eﬃcient bitrate adaption, decreased inter-phase in- terference, and increased sample eﬃciency. Better initial buﬀering performance, faster convergence, fewer rebuﬀering events, and improved QoE were observed in experimental ﬁndings on both synthetic and actual network traces compared to conventional RL and episodic DRL approaches. Optimizing video quality in dynamic networks while reducing bandwidth and playback interruptions was studied by Darwich et al. 2024. With RNN estimating the ideal bitrate per frame and CNN extracting information from video frames, they suggested a hybrid CNN-RNN architecture. By reducing rebuﬀering by 87.5%, improving QoE by 16.6%, and increasing average bitrate by 37.1%, experimental results demonstrated improved user experience and smoother playing compared to current ABR techniques.

**Fragmento 5 - p. 5 - score 3:**

3. Eﬃcient inference via linear state-space modeling: The inference procedure leverages the linear state-space formulation of Mamba to generate stable and computationally eﬃcient bandwidth predictions within each session, improving temporal smoothness and robustness. 4. QoE-oriented performance validation: Beyond prediction accuracy and error re- duction, the framework demonstrates more consistent QoE outcomes compared to Pensieve-PPO, highlighting its practical advantage for adaptive bitrate streaming. Architectural overview of the proposed MamBRA framework is shown in Figure 1. User session data are utilized for model training and validation, followed by an inference stage that performs adaptive bandwidth selection.

**Fragmento 6 - p. 6 - score 3:**

The rest of the paper is organized as follows: Section 2 gives a review of the bitrate adaptation for live streaming using optimization techniques, while Section 3 describes the detailed structure of the Mamba framework and the SSM. Section 4 describes the dataset used to build the proposed model. Section 5 presents the proposed MamBRA model in detail. In Section 6, QoE is computed using the bandwidth values predicted by MamBRA, followed by a comparative evaluation against Pensieve-PPO. Finally, Section 7 identiﬁes upcoming trends and gaps in the literature and makes recommendations for further research. 2 Related Work Early studies on adaptive video streaming addressed the shortcomings of traditional rate- and buﬀer-based ABR methods under dynamic network conditions.

**Fragmento 7 - p. 8 - score 3:**

In order to maximize user QoE, Wei et al. 2022 pointed out that traditional adaptive bitrate (ABR) techniques frequently struggle to optimize bitrate selection and minimize rebuﬀering at the same time. As a quantum-inspired ABR control method, QuDASH was presented to get around these restrictions. To ﬁnd the best bitrates, it uses a Digital Annealer to solve a Quadratic Unconstrained Binary Optimization (QUBO) problem that models buﬀer conditions, bitrate ﬂuctuations, and video quality. Based on actual network traces, simulation results show that QuDASH outperforms current ABR techniques, at- taining the highest QoE in 68.2% of scenarios, conﬁrming its eﬃcacy in improving user experience. ABR adaptation under various networks and numerous QoE objectives was the main focus of the research conducted by Xu et al.

**Fragmento 8 - p. 9 - score 3:**

By increasing bitrate decision accuracy and stability, this method raises QoE. Experimental results show a QoE gain of about 28.5% across bandwidth usage, rebuﬀering, and playback smoothness parameters when compared to numerous state-of-the-art ABR algorithms. The review identiﬁes various research challenges and gaps in adaptive bitrate optimiza- tion for live streaming as follows: • Most techniques handle live streaming like VoD; live-speciﬁc latency restrictions are rarely addressed. • Many studies rely on synthetic or VoD traces due to the lack of realistic live-network datasets. • ML/DRL ABR models often show weak generalization to unseen network conditions. • Insuﬃcient analysis of failure modes and safety of learning-based ABR.

**Fragmento 9 - p. 19 - score 3:**

deviceType DeviceOS browser player Figure 7: Comparison between measured bandwidth (bandwidthMBPS) and model- predicted bandwidth (predictedMBPS) across device types. 6.2.2 Accuracy Additional experiments were conducted at the video-session level. For instance, when considering sessions on mobile devices, the model achieves an overall average accuracy of approximately 96.62% across 45 sessions. Figure 8 presents a set of time-series plots that as- sess the bandwidth prediction performance across all device types by comparing the actual bandwidth with the model’s predicted values. Overall, the model demonstrates smoother and more stable (i.e., more “conﬁdent”) predictions, particularly in longer sessions.

**Fragmento 10 - p. 19 - score 3:**

6.3 QoE Results The proposed MamBRA model is evaluated using MOS values to predict the QoE scores. These scores are normalized and cumulative scores are then calculated (CDF). Figure 9a illustrates CDF analysis of QoE scores, comparing two diﬀerent systems: MamBRA and Pensieve-PPO. • MOS: A numerical measure of the human-perceived quality. It typically ranges from 1 (Bad) to 5 (Excellent). • QoE: The subjective “satisfaction” of the user. It is aﬀected by buﬀering, video clarity, and how long it takes for the video to start. The mathematical formulas are as follows: 18

**Fragmento 11 - p. 21 - score 3:**

(a) CDF-QoE for MamBRA and Pensieve-PPO (b) Average QoE for each device type Figure 9: (a) CDF probability versus QoE for MamBRA and Pensieve-PPO, (b) average QoE for deviceType feature values (desktop, tv, mobile, and tablet) Table 3: Performance comparison summary between MamBRA and Pensieve-PPO Model/Metric Behavior Performance Summary Actual Bandwidth Smooth, steep curve starting around 0.7. Excellent. Nearly all sessions achieve a QoE score above 0.7, with a median around 0.82. Predicted (MamBRA) Even further right than the actual scores. Optimistic. The model predicts even higher QoE (median 0.9) than what is actually achieved. Pensieve-PPO A ”staircase” step function spread across the x-axis.

**Fragmento 12 - p. 21 - score 3:**

Additionally, the bandwidth predicted by MamBRA yields more reliable QoE ratings in comparison to the PPO-based approach used in Pensieve. According to the ﬁndings of this study, several directions for future research are high- lighted, as follows: • Integrating the predictive strengths of MamBRA with end-to-end ABR agent models 20

**Fragmento 13 - p. 22 - score 3:**

that can enhance bitrate selection in real-time. • Exploring the deployment of MamBRA in edge computing frameworks could further boost performance in multi-client scenario’s, minimizing latency and improving re- source allocation fairness. • Incorporating more sophisticated perceptual video quality metrics into the training objective may enhance the model’s performance to better match user satisfaction. • Testing and evaluating the proposed framework using various, modern network traces (e.g., 5G and Starlink) will guarantee its robustness to the growing of modern internet traﬃc. 8 Declarations Funding The authors received no ﬁnancial support for the research, authorship, and/or publication of this article.

**Fragmento 14 - p. 25 - score 3:**

Teixeira, Thiago, Bo Zhang, and Yuriy Reznik (2021). “Adaptive Streaming Playback Statistics Dataset”. In: Proceedings of the 12th ACM Multimedia Systems Conference, pp. 248–254. doi: 10.1145/3458305.3478444. Ran, Dezhi et al. (2020). “Preference-aware Dynamic Bitrate Adaptation for Mobile Short- form Video Feed Streaming”. In: IEEE Access 8, pp. 220083–220094. doi: 10.1109/ ACCESS.2020.3042619. Artioli, Emanuele, Farzad Tashtarian, and Christian Timmerer (2024). “DIGITWISE: Dig- ital Twin-based Modeling of Adaptive Video Streaming Engagement”. In: Proceedings of the 15th ACM Multimedia Systems Conference, pp. 78–88. doi: 10.1145/3625468. 3647613. godka (2025). Pensieve-PPO: The simplest implementation of Pensieve via state-of-the- art RL algorithms (PPO, DQN, SAC).

**Fragmento 15 - p. 5 - score 2:**

From a QoE per- spective, the predicted bandwidth yields more consistent QoE scores than those obtained using the PPO-based strategy implemented in Pensieve (Mao et al. 2017; godka 2025), highlighting the eﬀectiveness of the proposed framework for adaptive bitrate streaming optimization. The main contributions of the proposed approach can be summarized as follows: 1. Novel dataset structuring at the session level: The dataset is reorganized into fully disjoint user sessions with heterogeneous numerical and categorical features, enabling realistic temporal modeling while explicitly preventing cross-session information leak- age. 2. Session-aware supervised training strategy: A time-series learning framework is de- signed where training is strictly performed at the session level, preserving sequential dependencies and ensuring fair generalization across independent user trajectories.

**Fragmento 16 - p. 6 - score 2:**

According to experimental assessments, the suggested system outperforms traditional ABR techniques in terms of average delivered bitrate by 14.31% and improves QoE by 16.2%. Key drawbacks of learning-based Adaptive Bit Rate (ABR) streaming were discussed by T. Huang et al. 2019, including low sample eﬃciency and inadequate perceptual video quality consideration. They presented Comyco, a video quality-aware ABR method that uses imitation learning and trains its neural network on expert trajectories produced by an instant solver. This approach maximizes the use of gathered data and reduces unnec- essary exploration. Comyco improves the overall QoE by choosing video chunks based on perceptual quality rather than just bitrate.

**Fragmento 17 - p. 7 - score 2:**

Table 1: Enhancement of QoE through the evolution of adaptation algorithms Investigation Adaptation Algorithm Key Contributions QoE Improvements Mao et al. 2017 Pensieve – RL Neural network selects bitrate based on past streaming states +12–25% average QoE Sengupta et al. 2018 HotDASH – Actor–Critic & Cascaded DRL Incorporates user preferences and prefetching strategies +14.31% bitrate, +16.2% QoE T. Huang et al. 2019 Comyco – Imitation Learning Trains on expert trajectories to reduce exploration overhead +7.5–16.79% perceptual QoE Dinaki et al. 2021 BiLSTM–CNN Hybrid Proactive QoE prediction beyond traditional QoS metrics Lowest MAE and RMSE Wei et al. 2022 QuDASH – Quantum ABR Solves QUBO formulation for optimal bitrate selection Highest QoE in 68.2% of scenarios Xu et al.

**Fragmento 18 - p. 8 - score 2:**

2023. The authors suggested a customized federated learning ABR algorithm that applies a tailoring phase and aggregates knowledge from clients’ local models without exchanging raw data. In addition to improvements from context factors and personalization, experiments on 3G, 4G, and WiFi traces showed the highest overall QoE, the lowest rebuﬀering, and smoothness penalties, with an improvement of about 10% above local models, showing substantial adaptation. RL-based ABR algorithms are inadequate for optimizing QoE, especially during initial buﬀering and playback, according to D. Yang et al. 2023. They suggested a subepisodic DRL method that separated video sessions into formal playback (FP) and initial buﬀer- ing (IB) with distinct replay and optimization memories, all of which were connected by a reward mechanism based on QoE.

**Fragmento 19 - p. 9 - score 2:**

Robust ABR in heterogeneous networks was discussed by Ling et al. 2025. In order to learn reward functions independent of policies and allow for ﬂexible adaptation to diﬀerent QoE targets and unseen networks, they devised an adversarial inverse reinforcement learn- ing (AIRL) system that makes use of expert demonstrations. Experiments demonstrated a 4.3%–9.4% improvement in video quality and a 0.054%–6.2% reduction in stall time, demonstrating strong adaptation and excellent use of expert knowledge. In multi-tier Edge-DASH networks, a Deep Reinforcement Learning (DRL) framework utilizing Deep Deterministic Policy Gradient (DDPG) has been developed by Naseh et al. 2025 for joint User-to-Server Allocation (USA) and Bitrate Allocation (BrA).

**Fragmento 20 - p. 9 - score 2:**

While real-time transcoding takes care of edge storage constraints, the DDPG agent dynamically chooses the best streaming sources; edge, macro, or cloud and matching bitrates. In 5G- enabled multi-tier video streaming, simulations demonstrate that this strategy outperforms conventional network-driven and hybrid edge-cloud techniques by improving QoE, lowering bitrate errors, and minimizing transcoding violations. J. Zhang et al. 2025 suggest Predictive LSTM Local Attention ABR (PLL-ABR), an Adaptive Bitrate (ABR) algorithm based on Deep Reinforcement Learning (DRL) that makes use of the Proximal Policy Optimization (PPO) framework enhanced with dual clipping, Long Short-Term Memory (LSTM) networks, and local attention mechanisms.

**Fragmento 21 - p. 17 - score 2:**

cisions are made continuously as new network observations arrive. Importantly, the SSM state is reset only at session boundaries, ensuring that temporal dependencies are learned and applied strictly within individual playback sessions. In summary, inference is performed in a fully online and stateful manner, leveraging the recurrent dynamics of Mamba to integrate historical context eﬃciently. The warm-up phase aligns the internal state with recent session dynamics, while step-by-step process- ing enables continuous, low-latency bandwidth prediction suitable for real-time adaptive bitrate control. 6 Results and Discussion In this section, various tests are presented that demonstrate the performance of the pro- posed MamBRA model in terms of loss, accuracy, and QoE.

**Fragmento 22 - p. 20 - score 2:**

Desktop TV Mobile Tablet Sessions = 265 Sessions = 71 Sessions = 45 Sessions = 24 Accuracy ≈92.763 Accuracy ≈92.169 Accuracy ≈96.620 Accuracy ≈85.794 Figure 8: Comparison between measured bandwidth (bandwidthMBPS) and model- predicted bandwidth (predictedMBPS) across device types. MOS = 1 + 4 · log10 (bps + 1) −log10 (minbps + 1) log10 (maxbps + 1) −log10 (minbps + 1) QoE = (MOS −1) · 4 where bps is the predicted network’s bandwidth that MamBRA model calculated. Figure 9b illustrates and compares the Mean QoE scores across the four diﬀerent device types tv, desktop, mobile, and tablet. The data suggests that larger-screen devices (desktops and TVs) generally provide a higher QoE than portable devices (tablets and mobiles) in this speciﬁc dataset.

**Fragmento 23 - p. 20 - score 2:**

Several technical factors contribute to the lower scores seen for mobile devices, such as network volatility, hardware constraints, and mobility factors. Table 3 summarizes the performance of MamBRA and Pensieve-PPO. 19

**Fragmento 24 - p. 23 - score 2:**

In: IEEE/ACM Transactions on Networking 28.4, pp. 1698–1711. doi: 10.1109/TNET.2020.2996964. Akhtar, Zahaib et al. (2018). “Oboe: Auto-tuning Video ABR Algorithms to Network Conditions”. In: Proceedings of the 2018 Conference of the ACM Special Interest Group on Data Communication, pp. 44–58. doi: 10.1145/3230543.3230558. Pham, Stefan et al. (2020). “Evaluation of shared resource allocation using SAND for ABR streaming”. In: ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM) 16.2s, pp. 1–18. doi: 10.1145/3388926. Woo, J. et al. (2024). “Improving the Quality of Experience of Video Streaming Through a Buﬀer-Based Adaptive Bitrate Algorithm and Gated Recurrent Unit-Based Network Bandwidth Prediction”.

**Fragmento 25 - p. 25 - score 2:**

https://github.com/godka/Pensieve- PPO. GitHub repository (accessed 2026-03-01). Sengupta, S. et al. (2018). “HotDASH: Hotspot Aware Adaptive Video Streaming Using Deep Reinforcement Learning”. In: 2018 IEEE 26th International Conference on Net- work Protocols (ICNP). Cambridge, UK, pp. 165–175. doi: 10.1109/ICNP.2018. 000. Huang, T. et al. (Oct. 2019). “Comyco: Quality-aware Adaptive Video Streaming via Imi- tation Learning”. In: Proceedings of the 27th ACM International Conference on Multi- media, pp. 429–437. doi: 10.1145/3343031.3351014. Dinaki, H.E. et al. (2021). “Forecasting Video QoE with Deep Learning from Multivariate Time-series”. In: IEEE Open Journal of Signal Processing 2, pp. 512–521. doi: 10. 1109/OJSP.2021.3099065.

**Fragmento 26 - p. 4 - score 1:**

Its design integrates continuous-time state-space formulations with data-dependent parameterization, allowing eﬃcient parallel training and fast autoregressive inference. Due to these properties, Mamba demonstrates strong long-range dependency modeling and improved memory eﬃciency compared to traditional Transformers (Patro et al. 2025; Somvanshi et al. 2025). Recent studies have successfully extended Mamba to multiple domains (including vision, video understanding, and multimodal learning) highlighting its adaptability and robustness across tasks that require long-context modeling (G. Zhang et al. 2024; Liu et al. 2026; H. Zhang et al. 2024). These characteristics make Mamba particularly attractive for sequential decision-making and time-series applications such as adaptive video streaming, where eﬃcient long-horizon modeling and low inference latency are critical.


### 7.8. resultados numericos metricas

Palabras clave usadas: `improvement, improve, gain, reduce, reduction, %, QoE gain, higher, lower, average, median, percentile, stall time, latency, overhead, accuracy, significant, p95, p99, score, ratio, duration`

**Fragmento 1 - p. 7 - score 7:**

2025 Adversarial Inverse RL (AIRL) Generalizes to unseen network conditions +4.3–9.4% video quality, –0.054–6.2% stall Naseh et al. 2025 DRL with DDPG Edge-DASH Joint user–server bitrate allocation Higher QoE, fewer bitrate errors J. Zhang et al. 2025 PLL-ABR – DRL with PPO, LSTM & Attention Improves bitrate stability and prediction accuracy ∼28.5% QoE gain requirements, and an average QoE that is 7.5%–16.79% higher than previous methods. In 2020, researchers began addressing the gap in proactive video QoE prediction be- yond traditional QoS metrics. Dinaki et al. 2021 addressed the problem of proactively predicting video QoE beyond QoS metrics and delayed client measurements. A BiLSTM- CNN hybrid model was suggested, in which CNN recovers local patterns from multivariate time series and BiLSTM captures temporal dependencies.

**Fragmento 2 - p. 7 - score 7:**

Table 1: Enhancement of QoE through the evolution of adaptation algorithms Investigation Adaptation Algorithm Key Contributions QoE Improvements Mao et al. 2017 Pensieve – RL Neural network selects bitrate based on past streaming states +12–25% average QoE Sengupta et al. 2018 HotDASH – Actor–Critic & Cascaded DRL Incorporates user preferences and prefetching strategies +14.31% bitrate, +16.2% QoE T. Huang et al. 2019 Comyco – Imitation Learning Trains on expert trajectories to reduce exploration overhead +7.5–16.79% perceptual QoE Dinaki et al. 2021 BiLSTM–CNN Hybrid Proactive QoE prediction beyond traditional QoS metrics Lowest MAE and RMSE Wei et al. 2022 QuDASH – Quantum ABR Solves QUBO formulation for optimal bitrate selection Highest QoE in 68.2% of scenarios Xu et al.

**Fragmento 3 - p. 9 - score 6:**

Robust ABR in heterogeneous networks was discussed by Ling et al. 2025. In order to learn reward functions independent of policies and allow for ﬂexible adaptation to diﬀerent QoE targets and unseen networks, they devised an adversarial inverse reinforcement learn- ing (AIRL) system that makes use of expert demonstrations. Experiments demonstrated a 4.3%–9.4% improvement in video quality and a 0.054%–6.2% reduction in stall time, demonstrating strong adaptation and excellent use of expert knowledge. In multi-tier Edge-DASH networks, a Deep Reinforcement Learning (DRL) framework utilizing Deep Deterministic Policy Gradient (DDPG) has been developed by Naseh et al. 2025 for joint User-to-Server Allocation (USA) and Bitrate Allocation (BrA).

**Fragmento 4 - p. 9 - score 6:**

they suggested RL-based HTTP adaptive streaming with edge collaboration, which dy- namically redistributes clients to edge networks. In multi-client streaming scenarios, sim- ulations showed gains in user fairness, total QoE, and individual QoE, proving the eﬃcacy of edge-assisted RL techniques. The focus of Wang et al. 2024 was on overﬁtting and instability in RL-based ABR algorithms. An adversarial information bottleneck and imitation learning are combined in their suggested system, which learns from oﬄine optimum expert policies. Simulations showed enhanced robustness, generalization, and session-level consistency, with an average QoE increase of 7.3% and a ranking performance improvement of 30.01%.

**Fragmento 5 - p. 2 - score 5:**

During inference, it leverages the linear state-space formulation of Mamba to eﬃciently generate stable bandwidth predictions within each session. Experimen- tal results demonstrate reduced prediction error, improved accuracy, and enhanced temporal stability. The model achieves an overall inference accuracy of 93.94%, with session-level accuracy reaching as high as 97.32%. Furthermore, the predicted band- width achieves more consistent QoE scores compared to the PPO-based approach used in Pensieve. Keywords: SSM-Mamba, bitrate adaptation, video streaming, network bandwidth, QoE. 1

**Fragmento 6 - p. 6 - score 5:**

According to experimental assessments, the suggested system outperforms traditional ABR techniques in terms of average delivered bitrate by 14.31% and improves QoE by 16.2%. Key drawbacks of learning-based Adaptive Bit Rate (ABR) streaming were discussed by T. Huang et al. 2019, including low sample eﬃciency and inadequate perceptual video quality consideration. They presented Comyco, a video quality-aware ABR method that uses imitation learning and trains its neural network on expert trajectories produced by an instant solver. This approach maximizes the use of gathered data and reduces unnec- essary exploration. Comyco improves the overall QoE by choosing video chunks based on perceptual quality rather than just bitrate.

**Fragmento 7 - p. 7 - score 5:**

2023 Federated Learning ABR Client-speciﬁc models without raw data exchange ∼10% QoE gain, reduced rebuﬀering D. Yang et al. 2023 Subepisodic DRL Separate buﬀering and playback memories for control stability Smoother bitrate, fewer stalls Darwich et al. 2024 CNN–RNN Hybrid Frame-level bitrate estimation for ﬁne-grained adaptation +16.6% QoE, +37.1% bitrate, –87.5% rebuﬀering Woo et al. 2024 GRU-Based Bandwidth & Buﬀer ABR Throughput prediction with minimized bitrate switching Up to +40% MOS Kang et al. 2024 RL Edge-Assisted ABR Multi-client edge-assisted adaptive streaming Improved fairness and QoE Wang et al. 2024 Adversarial Information Bottleneck + Imitation Learning Robust QoE modeling with reduced overﬁtting +7.3% QoE, +30% ranking Ling et al.

**Fragmento 8 - p. 9 - score 5:**

By increasing bitrate decision accuracy and stability, this method raises QoE. Experimental results show a QoE gain of about 28.5% across bandwidth usage, rebuﬀering, and playback smoothness parameters when compared to numerous state-of-the-art ABR algorithms. The review identiﬁes various research challenges and gaps in adaptive bitrate optimiza- tion for live streaming as follows: • Most techniques handle live streaming like VoD; live-speciﬁc latency restrictions are rarely addressed. • Many studies rely on synthetic or VoD traces due to the lack of realistic live-network datasets. • ML/DRL ABR models often show weak generalization to unseen network conditions. • Insuﬃcient analysis of failure modes and safety of learning-based ABR.

**Fragmento 9 - p. 18 - score 5:**

It uses two distinct visualizations to compare raw error magnitudes against relative accuracy. The heatmap displays three error metrics: MSE, RMSE, and NRMSE. For deviceOS, Android is the top performer in terms of error reduction, boasting the lowest MSE (100) and a very low NRMSE (0.032) with the high accuracy rate (96.77%). While for deviceType, Mobile is clearly the “cleanest” category for the model and leads the pack, nearing 100% accuracy. This correlates perfectly with the low error values as shown in the heatmap. What is related to the web browsers, the model performs very consistently across diﬀerent browsers. Finally, the web player displays slightly higher ac- curacy (approx. 94-95%) compared to the app player (approx.

**Fragmento 10 - p. 6 - score 4:**

Therefore, a variety of optimization strategies were then investigated by researchers in an eﬀort to enhance bitrate adaptability. The goal of these strategies was to balance playback stability, re- buﬀering reduction, and video quality in order to improve QoE. Table 1 demonstrates the recent research on optimization algorithms that investigated to enhance QoE. Below a brief description of each algorithm is provided. Mao et al. 2017 discussed the drawbacks of conventional ABR algorithms in dynamic network scenarios. They presented Pensieve, a system based on reinforcement learning that trains a neural network to choose bitrate based on past streaming results. Evalua- tions revealed that it outperformed rate-based, buﬀer-based, and MPC schemes, improving average QoE by 12% to 25% and exhibiting strong performance in previously untested net- work circumstances.

**Fragmento 11 - p. 21 - score 4:**

(a) CDF-QoE for MamBRA and Pensieve-PPO (b) Average QoE for each device type Figure 9: (a) CDF probability versus QoE for MamBRA and Pensieve-PPO, (b) average QoE for deviceType feature values (desktop, tv, mobile, and tablet) Table 3: Performance comparison summary between MamBRA and Pensieve-PPO Model/Metric Behavior Performance Summary Actual Bandwidth Smooth, steep curve starting around 0.7. Excellent. Nearly all sessions achieve a QoE score above 0.7, with a median around 0.82. Predicted (MamBRA) Even further right than the actual scores. Optimistic. The model predicts even higher QoE (median 0.9) than what is actually achieved. Pensieve-PPO A ”staircase” step function spread across the x-axis.

**Fragmento 12 - p. 5 - score 3:**

impairments (Ran et al. 2020; Artioli et al. 2024). Therefore, the dataset is organized into multiple disjoint user sessions. To prevent information leakage and preserve temporal con- sistency, a supervised time-series learning strategy is employed, where training is conducted strictly at the session level. During inference, the proposed approach exploits the linear state-space formulation of Mamba to eﬃciently generate bandwidth predictions within each individual user session, enabling scalable and stable sequential modeling. Experimental re- sults demonstrate signiﬁcant error reduction and improved predictive accuracy. Moreover, the predicted bandwidth trajectories exhibit enhanced temporal stability.

**Fragmento 13 - p. 7 - score 3:**

Evaluations against LSTM, BiLSTM, SVM, and MLP revealed the lowest MAE and RMSE, indicating superior QoE prediction accuracy and allowing for proactive management to stop deterioration of the user experience. 6

**Fragmento 14 - p. 8 - score 3:**

Based on enhanced HE-EMDQN frameworks, this technique allowed for smoother, more eﬃcient bitrate adaption, decreased inter-phase in- terference, and increased sample eﬃciency. Better initial buﬀering performance, faster convergence, fewer rebuﬀering events, and improved QoE were observed in experimental ﬁndings on both synthetic and actual network traces compared to conventional RL and episodic DRL approaches. Optimizing video quality in dynamic networks while reducing bandwidth and playback interruptions was studied by Darwich et al. 2024. With RNN estimating the ideal bitrate per frame and CNN extracting information from video frames, they suggested a hybrid CNN-RNN architecture. By reducing rebuﬀering by 87.5%, improving QoE by 16.6%, and increasing average bitrate by 37.1%, experimental results demonstrated improved user experience and smoother playing compared to current ABR techniques.

**Fragmento 15 - p. 8 - score 3:**

2023. The authors suggested a customized federated learning ABR algorithm that applies a tailoring phase and aggregates knowledge from clients’ local models without exchanging raw data. In addition to improvements from context factors and personalization, experiments on 3G, 4G, and WiFi traces showed the highest overall QoE, the lowest rebuﬀering, and smoothness penalties, with an improvement of about 10% above local models, showing substantial adaptation. RL-based ABR algorithms are inadequate for optimizing QoE, especially during initial buﬀering and playback, according to D. Yang et al. 2023. They suggested a subepisodic DRL method that separated video sessions into formal playback (FP) and initial buﬀer- ing (IB) with distinct replay and optimization memories, all of which were connected by a reward mechanism based on QoE.

**Fragmento 16 - p. 13 - score 3:**

Numeric features are standardized using z-score normalization (standard scaling), where the mean and standard deviation are computed from the training split and subsequently applied to validation data. Categorical features are transformed using feature-wise label encoding, mapping each categorical value to an integer index. These encoded categorical features are then used as inputs to learned embedding layers within the model. The dataset is divided into training, validation, and testing sets using a 70%/10%/20% split. The detailed procedures for preprocessing, normalization, windowing, and data partitioning are illustrated in Figure 3. clean-up and split Original data Test data Numeric features Categorical features Train-Validation data Scaler Encoders Preprocesser group by sessionID generate sequences per session group (window=20) split to train and validation Validation data Train data 100% 80% 20% 70% 10% Figure 3: Dataset preparation (clean-up, normalization, sequencing and splitting) The dataset is ﬁrst partitioned into disjoint user sessions, where each session corre- sponds to a continuous playback episode.

**Fragmento 17 - p. 19 - score 3:**

deviceType DeviceOS browser player Figure 7: Comparison between measured bandwidth (bandwidthMBPS) and model- predicted bandwidth (predictedMBPS) across device types. 6.2.2 Accuracy Additional experiments were conducted at the video-session level. For instance, when considering sessions on mobile devices, the model achieves an overall average accuracy of approximately 96.62% across 45 sessions. Figure 8 presents a set of time-series plots that as- sess the bandwidth prediction performance across all device types by comparing the actual bandwidth with the model’s predicted values. Overall, the model demonstrates smoother and more stable (i.e., more “conﬁdent”) predictions, particularly in longer sessions.

**Fragmento 18 - p. 20 - score 3:**

Desktop TV Mobile Tablet Sessions = 265 Sessions = 71 Sessions = 45 Sessions = 24 Accuracy ≈92.763 Accuracy ≈92.169 Accuracy ≈96.620 Accuracy ≈85.794 Figure 8: Comparison between measured bandwidth (bandwidthMBPS) and model- predicted bandwidth (predictedMBPS) across device types. MOS = 1 + 4 · log10 (bps + 1) −log10 (minbps + 1) log10 (maxbps + 1) −log10 (minbps + 1) QoE = (MOS −1) · 4 where bps is the predicted network’s bandwidth that MamBRA model calculated. Figure 9b illustrates and compares the Mean QoE scores across the four diﬀerent device types tv, desktop, mobile, and tablet. The data suggests that larger-screen devices (desktops and TVs) generally provide a higher QoE than portable devices (tablets and mobiles) in this speciﬁc dataset.

**Fragmento 19 - p. 21 - score 3:**

Inconsistent. While it reaches high scores, many sessions experience low QoE (as low as 0.0–0.4). 7 Conclusion and Future Work This study developed MamBRA model, a new bitrate adaptation framework for video stream- ing that employs Mamba for accurate session-level bandwidth prediction. The streaming dataset are recognized by fully disconnected user sessions and the model implements a su- pervised time-series learning technique that ensures temporal consistency while explicitly limiting cross-session information leaking. The conducted test demonstrates that MamBRA has remarkably reduces prediction errors (Huber and MSE) and improves temporal sta- bility of predicted bandwidths. A signiﬁcant ﬁnding of this research work is that Mamba’s linear state-space model allows for eﬃcient and stable computation, which makes it very appropriate for real-time use.

**Fragmento 20 - p. 2 - score 2:**

However, as user demands for high quality and low latency increase, using eﬃcient video streaming systems is getting harder. In addition to taxing network resources, the increase in video traﬃc is lower- ing video quality. Deep and transformer learning algorithms use data-driven methods to optimize video delivery, enhance QoE, and lessen network congestion in order to overcome these obstacles. Mamba utilizes the eﬃcient linear complexity of selective state space model (SSM) mechanism to process data sequences more eﬀectively. This paper proposes an adaptive video streaming framework (MamBRA) based on Mamba for session-level bandwidth prediction. The model is trained in a supervised time-series manner on disjoint user sessions to prevent information leakage and preserve temporal structure.

**Fragmento 21 - p. 3 - score 2:**

2020). When network bandwidth variations are small, ABR algorithms can operate eﬀectively because they use network bandwidth history to anticipate future network bandwidth (Akhtar et al. 2018; Pham et al. 2020). However, the QoE of video streaming frequently deteriorates in settings where network bandwidth ﬂuctuates frequently, like wireless networks, due to imprecise forecasts of future network capacity (Woo et al. 2024). In order to improve QoE in multimedia streaming, numerous studies have been car- ried out(Seufert et al. 2015; Timmerer et al. 2017). These studies have concentrated on adaptive bitrate algorithms, network optimization, predictive QoE modeling, and intelli- gent management systems to minimize buﬀering, latency, and degradation of video quality, particularly in dynamic wireless network environment.

**Fragmento 22 - p. 4 - score 2:**

Its design integrates continuous-time state-space formulations with data-dependent parameterization, allowing eﬃcient parallel training and fast autoregressive inference. Due to these properties, Mamba demonstrates strong long-range dependency modeling and improved memory eﬃciency compared to traditional Transformers (Patro et al. 2025; Somvanshi et al. 2025). Recent studies have successfully extended Mamba to multiple domains (including vision, video understanding, and multimodal learning) highlighting its adaptability and robustness across tasks that require long-context modeling (G. Zhang et al. 2024; Liu et al. 2026; H. Zhang et al. 2024). These characteristics make Mamba particularly attractive for sequential decision-making and time-series applications such as adaptive video streaming, where eﬃcient long-horizon modeling and low inference latency are critical.

**Fragmento 23 - p. 11 - score 2:**

bufferDeficitSecs Seconds of video playback missing due to stalling. rebufferingSecs Seconds buﬀered between the last two segments. rebufferingCount Times buﬀering occurs between the last two seg- ments. Network bytesTransferred Bytes transferred since the start of the session. bandwidthMBPS Network bandwidth. Categorical Client deviceType {desktop, tv, tablet, mobile, . . . } deviceOS {windows, android, other, ios, web_os, . . . } browser {chrome, other, ﬁrefox, edge, . . . } player {web, app} playerDim 110 dimensions (width×height). The feature playerDim is obtained by merging two numeric columns in the original dataset, resulting in 110 distinct player dimension categories. The segment duration is ﬁxed at four seconds across all sessions.

**Fragmento 24 - p. 17 - score 2:**

cisions are made continuously as new network observations arrive. Importantly, the SSM state is reset only at session boundaries, ensuring that temporal dependencies are learned and applied strictly within individual playback sessions. In summary, inference is performed in a fully online and stateful manner, leveraging the recurrent dynamics of Mamba to integrate historical context eﬃciently. The warm-up phase aligns the internal state with recent session dynamics, while step-by-step process- ing enables continuous, low-latency bandwidth prediction suitable for real-time adaptive bitrate control. 6 Results and Discussion In this section, various tests are presented that demonstrate the performance of the pro- posed MamBRA model in terms of loss, accuracy, and QoE.

**Fragmento 25 - p. 17 - score 2:**

First, the results of the training are presented in Subsection 6.1. Next, the model’s inference tests are detailed in Subsec- tion 6.2. Finally, the decision-making behavior of MamBRA is compared against the baseline method Pensieve-PPO under a ﬂuctuating network trace using QoE evaluation metric (Subsection 6.3). 6.1 Model Training Results For a sequence-prediction model like MamBRA, and by tracking the Huber loss, the gap between what MamBRA predicted and what the network actually delivered is measured. Figure 6 illustrates the Huber loss and accuracy for the training and validation. Figure 6: Huber loss versus accuracy To provide a comprehensive view of MamBRA model’s performance, we highlight the following analysis: 16

**Fragmento 26 - p. 18 - score 2:**

• Correlation between “Loss and Accuracy”: From Figure 6 we can see that when Huber loss drops quickly in the ﬁrst 20 epochs accuracy goes up sharply. This shows that when Huber loss goes down accuracy goes up meaning that the model is eﬀectively optimizing its internal weights to minimize prediction errors. • Learning stability: The training accuracy, shown as a solid line keeps going up and until it reaches 93%. At that point the validation’s accuracy, represented by a red dashed line levels oﬀat, around 88%. This high validation accuracy shows that the Mamba state-space architecture is successfully capturing the complex temporal dependencies of the network traces. • Generalization Gap: The model appears to generalize well to unseen, unexplored network conditions, as indicated by the narrow diﬀerence between the training and validation accuracy curves.


### 7.9. limitaciones riesgos coste

Palabras clave usadas: `limitation, limitations, future work, challenge, challenges, overhead, complexity, compute, GPU, CPU, deployment, real-world, generalization, out-of-distribution, OOD, unstable, fail, bias, sensitive, prediction error, horizon, scalability`

**Fragmento 1 - p. 9 - score 4:**

By increasing bitrate decision accuracy and stability, this method raises QoE. Experimental results show a QoE gain of about 28.5% across bandwidth usage, rebuﬀering, and playback smoothness parameters when compared to numerous state-of-the-art ABR algorithms. The review identiﬁes various research challenges and gaps in adaptive bitrate optimiza- tion for live streaming as follows: • Most techniques handle live streaming like VoD; live-speciﬁc latency restrictions are rarely addressed. • Many studies rely on synthetic or VoD traces due to the lack of realistic live-network datasets. • ML/DRL ABR models often show weak generalization to unseen network conditions. • Insuﬃcient analysis of failure modes and safety of learning-based ABR.

**Fragmento 2 - p. 3 - score 3:**

1 Introduction Internet video traﬃc has surged over the past two decades, accounting for over 65% of all web traﬃc (Sandvine 2023). This growth, fueled by video-on-demand and live streaming, strains network infrastructure and complicates the delivery of a consistent Quality of Expe- rience (QoE). To address these challenges, the industry has adopted HTTP-based adaptive streaming (HAS) as the standard delivery method (Abdullah et al. 2017). HAS divides video into segments at various bitrates, enabling clients to adjust quality dynamically based on network conditions while utilizing existing HTTP infrastructure for scalability and compatibility. Major standards like Microsoft’s Smooth Streaming (MSS) (Microsoft 2008; Stockhammer 2011), Apple’s HTTP Live Streaming (HLS) (Pantos et al.

**Fragmento 3 - p. 3 - score 2:**

2017; Apple Inc. 2024), and MPEG’s Dynamic Adaptive Streaming over HTTP (MPEG-DASH)(DASH Industry Forum 2024) have solidiﬁed HAS as the global norm. However, live streaming remains challenging as providers must balance low latency, high visual quality, and network eﬃciency (Yin et al. 2015; T.-Y. Huang et al. 2014). These com- peting demands under ﬂuctuating bandwidth have sparked ongoing research into bitrate adaptation and buﬀer management. Ultimately, the need to minimize rebuﬀering while maintaining stability continues to drive innovation in streaming algorithms and system design. 1.1 Challenges in Adaptive Bitrate (ABR) Streaming Streaming services use adaptive bitrate (ABR) algorithms to manage network bandwidth ﬂuctuations for better QoE (Spiteri et al.

**Fragmento 4 - p. 18 - score 2:**

• Correlation between “Loss and Accuracy”: From Figure 6 we can see that when Huber loss drops quickly in the ﬁrst 20 epochs accuracy goes up sharply. This shows that when Huber loss goes down accuracy goes up meaning that the model is eﬀectively optimizing its internal weights to minimize prediction errors. • Learning stability: The training accuracy, shown as a solid line keeps going up and until it reaches 93%. At that point the validation’s accuracy, represented by a red dashed line levels oﬀat, around 88%. This high validation accuracy shows that the Mamba state-space architecture is successfully capturing the complex temporal dependencies of the network traces. • Generalization Gap: The model appears to generalize well to unseen, unexplored network conditions, as indicated by the narrow diﬀerence between the training and validation accuracy curves.

**Fragmento 5 - p. 18 - score 2:**

6.2 Inference Tests Unlike the training phase, where the model adjusts its weights based on a loss function (like Huber loss), the inference test focuses on how the model actually acts in a real-world simulation. Over all dataset sessions used during inference, the model attains a mean squared error (MSE) of 3669.33, a root mean squared error (RMSE) of 60.58, a normalized RMSE (NRMSE, computed by normalizing the MSE over the range Max–Min) of 0.06, and an overall accuracy of 93.94%. The remainder of this subsection provides a detailed examination of these performance metrics at the individual session level. 6.2.1 Loss Figure 7 presents a performance breakdown of a model across four features: deviceOS, deviceType, browser, and player.

**Fragmento 6 - p. 21 - score 2:**

Inconsistent. While it reaches high scores, many sessions experience low QoE (as low as 0.0–0.4). 7 Conclusion and Future Work This study developed MamBRA model, a new bitrate adaptation framework for video stream- ing that employs Mamba for accurate session-level bandwidth prediction. The streaming dataset are recognized by fully disconnected user sessions and the model implements a su- pervised time-series learning technique that ensures temporal consistency while explicitly limiting cross-session information leaking. The conducted test demonstrates that MamBRA has remarkably reduces prediction errors (Huber and MSE) and improves temporal sta- bility of predicted bandwidths. A signiﬁcant ﬁnding of this research work is that Mamba’s linear state-space model allows for eﬃcient and stable computation, which makes it very appropriate for real-time use.

**Fragmento 7 - p. 22 - score 2:**

Author Contributions The authors’ contributions are as follows: • Jamal A. Hussein: wrote Section 3, prepared the dataset (Section 4), designed and implemented the proposed system (Section 5) and conducted the inference experi- ments and corresponding results (Figures 7 and 8). • Aree A. Mohammad: computed the QoE metrics based on the results generated from the system implementation and prepared the ﬁgures presented in Subsections 6.1 and 6.3. Aree initially wrote the Conclusion and Future Work section (Section 7). • Miran T. Abdullah: prepared the Related Work section (Section 2). • Aree and Jamal collaborated in preparing the inference results subsection (Subsec- tion 6.2). • The Introduction section (Section 1) was jointly written by all authors.

**Fragmento 8 - p. 24 - score 2:**

“Mamba: Linear-Time Sequence Modeling with Selec- tive State Spaces”. In: First Conference on Language Modeling. url: https : / / openreview.net/forum?id=tEYskw1VY2. Patro, Badri Narayana and Vijay Srinivas Agneeswaran (2025). “Mamba-360: Survey of State Space Models as Transformer Alternative for Long Sequence Modelling: Methods, Applications, and Challenges”. In: Engineering Applications of Artiﬁcial Intelligence 159, p. 111279. issn: 0952-1976. doi: 10.1016/j.engappai.2025.111279. Somvanshi, Shriyank et al. (2025). “From S4 to Mamba: A Comprehensive Survey on Structured State Space Models”. In: arXiv preprint. Survey tracing evolution of SSMs from S4 through Mamba and related variants. url: https://arxiv.org/abs/ 2503.18970.

**Fragmento 9 - p. 2 - score 1:**

However, as user demands for high quality and low latency increase, using eﬃcient video streaming systems is getting harder. In addition to taxing network resources, the increase in video traﬃc is lower- ing video quality. Deep and transformer learning algorithms use data-driven methods to optimize video delivery, enhance QoE, and lessen network congestion in order to overcome these obstacles. Mamba utilizes the eﬃcient linear complexity of selective state space model (SSM) mechanism to process data sequences more eﬀectively. This paper proposes an adaptive video streaming framework (MamBRA) based on Mamba for session-level bandwidth prediction. The model is trained in a supervised time-series manner on disjoint user sessions to prevent information leakage and preserve temporal structure.

**Fragmento 10 - p. 2 - score 1:**

MamBRA: Session-Level Bandwidth Prediction for Adaptive Video Streaming using Selective State Space Models Jamal A. Hussein , Aree A. Mohammed, and Miran T. Abdullah Department of Computer, College of Science, University of Sulaimani, KRG, Iraq {jamal.ali, aree.ali, miran.abdullah}@univsul.edu.iq March 6, 2026 Corresponding author: Jamal A. Hussein Email: jamal.ali@univsul.edu.iq Abstract Live streaming is the real-time transmission of video content to an audience as it is simultaneously recorded. This technology is frequently utilized for applications such as covering live events and facilitating video calls. By dynamically modifying the video quality to match network conditions and device capabilities, adaptive video streaming provides improved Quality of Experience (QoE).

**Fragmento 11 - p. 2 - score 1:**

During inference, it leverages the linear state-space formulation of Mamba to eﬃciently generate stable bandwidth predictions within each session. Experimen- tal results demonstrate reduced prediction error, improved accuracy, and enhanced temporal stability. The model achieves an overall inference accuracy of 93.94%, with session-level accuracy reaching as high as 97.32%. Furthermore, the predicted band- width achieves more consistent QoE scores compared to the PPO-based approach used in Pensieve. Keywords: SSM-Mamba, bitrate adaptation, video streaming, network bandwidth, QoE. 1

**Fragmento 12 - p. 4 - score 1:**

This approach seeks to improve energy usage without sacriﬁcing the user experience (Tien et al. 2025; X. Yang et al. 2024). 1.2 Machine Learning–Based Sequence Modeling for Bitrate Adaptation Machine learning–based approaches have been extensively adopted for bitrate adaptation in video streaming, with sequence modeling architectures such as Transformers and recurrent neural networks (RNNs) playing a particularly prominent role (Mao et al. 2017). Recently, Mamba (selective structured state-space sequence architecture) has emerged as a powerful alternative to Transformer-based models (Gu and Dao 2024). Unlike self- attention mechanisms whose computational complexity grows quadratically with sequence length, Mamba leverages selective state-space modeling to achieve linear-time complexity, enabling scalable processing of very long sequences while maintaining competitive repre- sentational capacity.

**Fragmento 13 - p. 4 - score 1:**

Its design integrates continuous-time state-space formulations with data-dependent parameterization, allowing eﬃcient parallel training and fast autoregressive inference. Due to these properties, Mamba demonstrates strong long-range dependency modeling and improved memory eﬃciency compared to traditional Transformers (Patro et al. 2025; Somvanshi et al. 2025). Recent studies have successfully extended Mamba to multiple domains (including vision, video understanding, and multimodal learning) highlighting its adaptability and robustness across tasks that require long-context modeling (G. Zhang et al. 2024; Liu et al. 2026; H. Zhang et al. 2024). These characteristics make Mamba particularly attractive for sequential decision-making and time-series applications such as adaptive video streaming, where eﬃcient long-horizon modeling and low inference latency are critical.

**Fragmento 14 - p. 4 - score 1:**

of video data contributes to congestion, elevated costs, and high energy usage (George et al. 2025), among other issues, developing video traﬃc optimization methods is critically important. Furthermore, delivering high video quality and a positive QoE remains a core objective in video streaming. Since algorithms rely on QoE feedback to adjust streaming quality, the ﬁeld heavily invests in research aimed at creating reliable and accurate QoE models (Jia et al. 2025). Another challenge is the energy consumption, which is a main concern across a live video streaming pipeline. Conventional machine and deep learning models oﬀer a solution to these problems by enabling energy-aware video encoding and quality adaptation.

**Fragmento 15 - p. 5 - score 1:**

From a QoE per- spective, the predicted bandwidth yields more consistent QoE scores than those obtained using the PPO-based strategy implemented in Pensieve (Mao et al. 2017; godka 2025), highlighting the eﬀectiveness of the proposed framework for adaptive bitrate streaming optimization. The main contributions of the proposed approach can be summarized as follows: 1. Novel dataset structuring at the session level: The dataset is reorganized into fully disjoint user sessions with heterogeneous numerical and categorical features, enabling realistic temporal modeling while explicitly preventing cross-session information leak- age. 2. Session-aware supervised training strategy: A time-series learning framework is de- signed where training is strictly performed at the session level, preserving sequential dependencies and ensuring fair generalization across independent user trajectories.

**Fragmento 16 - p. 6 - score 1:**

The rest of the paper is organized as follows: Section 2 gives a review of the bitrate adaptation for live streaming using optimization techniques, while Section 3 describes the detailed structure of the Mamba framework and the SSM. Section 4 describes the dataset used to build the proposed model. Section 5 presents the proposed MamBRA model in detail. In Section 6, QoE is computed using the bandwidth values predicted by MamBRA, followed by a comparative evaluation against Pensieve-PPO. Finally, Section 7 identiﬁes upcoming trends and gaps in the literature and makes recommendations for further research. 2 Related Work Early studies on adaptive video streaming addressed the shortcomings of traditional rate- and buﬀer-based ABR methods under dynamic network conditions.

**Fragmento 17 - p. 6 - score 1:**

Conventional Adaptive Bitrate (ABR) algorithms mostly ignore user-speciﬁc content preferences in favor of optimizing network-level metrics like bitrate stability and rebuﬀering avoidance. Sengupta et al. 2018 introduced HotDASH, a hotspot-aware video streaming framework based on an actor-critic neural network and a cascaded deep reinforcement learning architecture, to overcome this limitation. Their technique allows the reinforce- ment learning agent to opportunistically prefetch video segments that suit user preferences while also optimizing bitrate selection. HotDASH dramatically increases user satisfaction and streaming eﬃciency by integrating preference awareness into the adaptation strategy.

**Fragmento 18 - p. 7 - score 1:**

Table 1: Enhancement of QoE through the evolution of adaptation algorithms Investigation Adaptation Algorithm Key Contributions QoE Improvements Mao et al. 2017 Pensieve – RL Neural network selects bitrate based on past streaming states +12–25% average QoE Sengupta et al. 2018 HotDASH – Actor–Critic & Cascaded DRL Incorporates user preferences and prefetching strategies +14.31% bitrate, +16.2% QoE T. Huang et al. 2019 Comyco – Imitation Learning Trains on expert trajectories to reduce exploration overhead +7.5–16.79% perceptual QoE Dinaki et al. 2021 BiLSTM–CNN Hybrid Proactive QoE prediction beyond traditional QoS metrics Lowest MAE and RMSE Wei et al. 2022 QuDASH – Quantum ABR Solves QUBO formulation for optimal bitrate selection Highest QoE in 68.2% of scenarios Xu et al.

**Fragmento 19 - p. 9 - score 1:**

they suggested RL-based HTTP adaptive streaming with edge collaboration, which dy- namically redistributes clients to edge networks. In multi-client streaming scenarios, sim- ulations showed gains in user fairness, total QoE, and individual QoE, proving the eﬃcacy of edge-assisted RL techniques. The focus of Wang et al. 2024 was on overﬁtting and instability in RL-based ABR algorithms. An adversarial information bottleneck and imitation learning are combined in their suggested system, which learns from oﬄine optimum expert policies. Simulations showed enhanced robustness, generalization, and session-level consistency, with an average QoE increase of 7.3% and a ranking performance improvement of 30.01%.

**Fragmento 20 - p. 10 - score 1:**

• Mobile device energy and computation costs are frequently disregarded. 3 Mamba Framework Mamba introduces input-dependent selectivity into state space models (SSMs), enabling content-aware sequence modeling with linear time complexity (Gu and Dao 2024). Rather than relying on attention (Vaswani et al. 2017), Mamba performs selective state transitions using structured SSMs. Let xt ∈RD denote the input at time step t, and let ht ∈RN denote the latent state. Mamba models the sequence using the discrete-time recurrence ht = ¯Atht−1 + ¯Btxt, yt = Ctht, where ¯At ∈RN×N, ¯Bt ∈RN×D, and Ct ∈RD×N are input-dependent parameters. The discrete parameters are derived from an underlying continuous-time system with diagonal state matrix A ∈RN×N (Gu, Goel, et al.

**Fragmento 21 - p. 10 - score 1:**

2022). Given a per-token step size ∆t > 0, the discretization is ¯At = exp(∆tA), ¯Bt = A−1 (exp(∆tA) −I) Bt, where I ∈RN×N is the identity matrix. Selectivity is introduced by making the parameters functions of the input: Bt = sB(xt), Ct = sC(xt), ∆t = softplus(θ + s∆(xt)). Here, sB(·), sC(·), and s∆(·) are learned linear projections. This design enables adaptive state updates, memory retention, and readout at each time step. Because the parameters vary across time steps, convolution-based acceleration used in time-invariant SSMs is no longer applicable. Mamba instead employs a hardware-aware parallel scan (preﬁx-sum) algorithm to evaluate the recurrence eﬃciently, achieving linear time complexity and logarithmic parallel depth.

**Fragmento 22 - p. 13 - score 1:**

Numeric features are standardized using z-score normalization (standard scaling), where the mean and standard deviation are computed from the training split and subsequently applied to validation data. Categorical features are transformed using feature-wise label encoding, mapping each categorical value to an integer index. These encoded categorical features are then used as inputs to learned embedding layers within the model. The dataset is divided into training, validation, and testing sets using a 70%/10%/20% split. The detailed procedures for preprocessing, normalization, windowing, and data partitioning are illustrated in Figure 3. clean-up and split Original data Test data Numeric features Categorical features Train-Validation data Scaler Encoders Preprocesser group by sessionID generate sequences per session group (window=20) split to train and validation Validation data Train data 100% 80% 20% 70% 10% Figure 3: Dataset preparation (clean-up, normalization, sequencing and splitting) The dataset is ﬁrst partitioned into disjoint user sessions, where each session corre- sponds to a continuous playback episode.

**Fragmento 23 - p. 15 - score 1:**

• Categorical Features: These are passed through an Embedding layer, which converts discrete categories into continuous vectors. • Numeric Features: These are passed after normalization (Figure 3) to be com- bined with the embeddings. • Concatenation: Both feature types are merged into a single representation before entering the main model block. 2. Core Model Architecture The dotted box contains the primary neural network components that constitute the MamBRA model: • Input Projection: A linear layer that maps the concatenated features into the model’s hidden dimension. • Mamba Block (Sequence Scan): This is the heart of the model. Unlike standard Transformers, Mamba uses a selective SSM to process sequences eﬃciently, which is particularly good at capturing long-range dependencies.

**Fragmento 24 - p. 15 - score 1:**

• RMSNorm and Linear Head: The output of the Mamba block is normalized using Root Mean Square Layer Normalization and then passed through a ﬁnal linear layer to project it to the target output size. • Prediction (Last Time Step): The model extracts the prediction from the ﬁnal time step to make its assessment. 3. Loss Functions and Optimization The diagram distinguishes how the model is evaluated during diﬀerent phases: Phase Gradient Status Loss Functions Used Optimizer Train Enabled Huber Loss AdamW Backprop Validation Disabled Huber Loss & MSE Loss N/A • Huber Loss: Used as the primary training objective. It is often preferred over MSE (Mean Squared Error) because it is less sensitive to outliers in the data.

**Fragmento 25 - p. 16 - score 1:**

This inference strategy yields dense, per-timestep predictions throughout the session and closely reﬂects the online ABR deployment scenario, in which bitrate adaptation de- 15

**Fragmento 26 - p. 22 - score 1:**

that can enhance bitrate selection in real-time. • Exploring the deployment of MamBRA in edge computing frameworks could further boost performance in multi-client scenario’s, minimizing latency and improving re- source allocation fairness. • Incorporating more sophisticated perceptual video quality metrics into the training objective may enhance the model’s performance to better match user satisfaction. • Testing and evaluating the proposed framework using various, modern network traces (e.g., 5G and Starlink) will guarantee its robustness to the growing of modern internet traﬃc. 8 Declarations Funding The authors received no ﬁnancial support for the research, authorship, and/or publication of this article.


### 7.10. ideas fase45 v1 controller defendible

Palabras clave usadas: `risk, safe, safety, robust, conservative, fallback, uncertainty, capacity, lower bound, tail, severe, low buffer, volatile, variable, fluctuation, drop, zero, consistent, smoothness, auto-tuning, regime, cluster, guidance, hybrid, generalization, environment-aware, prediction, selector`

**Fragmento 1 - p. 5 - score 4:**

3. Eﬃcient inference via linear state-space modeling: The inference procedure leverages the linear state-space formulation of Mamba to generate stable and computationally eﬃcient bandwidth predictions within each session, improving temporal smoothness and robustness. 4. QoE-oriented performance validation: Beyond prediction accuracy and error re- duction, the framework demonstrates more consistent QoE outcomes compared to Pensieve-PPO, highlighting its practical advantage for adaptive bitrate streaming. Architectural overview of the proposed MamBRA framework is shown in Figure 1. User session data are utilized for model training and validation, followed by an inference stage that performs adaptive bandwidth selection.

**Fragmento 2 - p. 9 - score 4:**

By increasing bitrate decision accuracy and stability, this method raises QoE. Experimental results show a QoE gain of about 28.5% across bandwidth usage, rebuﬀering, and playback smoothness parameters when compared to numerous state-of-the-art ABR algorithms. The review identiﬁes various research challenges and gaps in adaptive bitrate optimiza- tion for live streaming as follows: • Most techniques handle live streaming like VoD; live-speciﬁc latency restrictions are rarely addressed. • Many studies rely on synthetic or VoD traces due to the lack of realistic live-network datasets. • ML/DRL ABR models often show weak generalization to unseen network conditions. • Insuﬃcient analysis of failure modes and safety of learning-based ABR.

**Fragmento 3 - p. 7 - score 3:**

2023 Federated Learning ABR Client-speciﬁc models without raw data exchange ∼10% QoE gain, reduced rebuﬀering D. Yang et al. 2023 Subepisodic DRL Separate buﬀering and playback memories for control stability Smoother bitrate, fewer stalls Darwich et al. 2024 CNN–RNN Hybrid Frame-level bitrate estimation for ﬁne-grained adaptation +16.6% QoE, +37.1% bitrate, –87.5% rebuﬀering Woo et al. 2024 GRU-Based Bandwidth & Buﬀer ABR Throughput prediction with minimized bitrate switching Up to +40% MOS Kang et al. 2024 RL Edge-Assisted ABR Multi-client edge-assisted adaptive streaming Improved fairness and QoE Wang et al. 2024 Adversarial Information Bottleneck + Imitation Learning Robust QoE modeling with reduced overﬁtting +7.3% QoE, +30% ranking Ling et al.

**Fragmento 4 - p. 18 - score 3:**

• Correlation between “Loss and Accuracy”: From Figure 6 we can see that when Huber loss drops quickly in the ﬁrst 20 epochs accuracy goes up sharply. This shows that when Huber loss goes down accuracy goes up meaning that the model is eﬀectively optimizing its internal weights to minimize prediction errors. • Learning stability: The training accuracy, shown as a solid line keeps going up and until it reaches 93%. At that point the validation’s accuracy, represented by a red dashed line levels oﬀat, around 88%. This high validation accuracy shows that the Mamba state-space architecture is successfully capturing the complex temporal dependencies of the network traces. • Generalization Gap: The model appears to generalize well to unseen, unexplored network conditions, as indicated by the narrow diﬀerence between the training and validation accuracy curves.

**Fragmento 5 - p. 2 - score 2:**

During inference, it leverages the linear state-space formulation of Mamba to eﬃciently generate stable bandwidth predictions within each session. Experimen- tal results demonstrate reduced prediction error, improved accuracy, and enhanced temporal stability. The model achieves an overall inference accuracy of 93.94%, with session-level accuracy reaching as high as 97.32%. Furthermore, the predicted band- width achieves more consistent QoE scores compared to the PPO-based approach used in Pensieve. Keywords: SSM-Mamba, bitrate adaptation, video streaming, network bandwidth, QoE. 1

**Fragmento 6 - p. 5 - score 2:**

From a QoE per- spective, the predicted bandwidth yields more consistent QoE scores than those obtained using the PPO-based strategy implemented in Pensieve (Mao et al. 2017; godka 2025), highlighting the eﬀectiveness of the proposed framework for adaptive bitrate streaming optimization. The main contributions of the proposed approach can be summarized as follows: 1. Novel dataset structuring at the session level: The dataset is reorganized into fully disjoint user sessions with heterogeneous numerical and categorical features, enabling realistic temporal modeling while explicitly preventing cross-session information leak- age. 2. Session-aware supervised training strategy: A time-series learning framework is de- signed where training is strictly performed at the session level, preserving sequential dependencies and ensuring fair generalization across independent user trajectories.

**Fragmento 7 - p. 7 - score 2:**

2025 Adversarial Inverse RL (AIRL) Generalizes to unseen network conditions +4.3–9.4% video quality, –0.054–6.2% stall Naseh et al. 2025 DRL with DDPG Edge-DASH Joint user–server bitrate allocation Higher QoE, fewer bitrate errors J. Zhang et al. 2025 PLL-ABR – DRL with PPO, LSTM & Attention Improves bitrate stability and prediction accuracy ∼28.5% QoE gain requirements, and an average QoE that is 7.5%–16.79% higher than previous methods. In 2020, researchers began addressing the gap in proactive video QoE prediction be- yond traditional QoS metrics. Dinaki et al. 2021 addressed the problem of proactively predicting video QoE beyond QoS metrics and delayed client measurements. A BiLSTM- CNN hybrid model was suggested, in which CNN recovers local patterns from multivariate time series and BiLSTM captures temporal dependencies.

**Fragmento 8 - p. 7 - score 2:**

Table 1: Enhancement of QoE through the evolution of adaptation algorithms Investigation Adaptation Algorithm Key Contributions QoE Improvements Mao et al. 2017 Pensieve – RL Neural network selects bitrate based on past streaming states +12–25% average QoE Sengupta et al. 2018 HotDASH – Actor–Critic & Cascaded DRL Incorporates user preferences and prefetching strategies +14.31% bitrate, +16.2% QoE T. Huang et al. 2019 Comyco – Imitation Learning Trains on expert trajectories to reduce exploration overhead +7.5–16.79% perceptual QoE Dinaki et al. 2021 BiLSTM–CNN Hybrid Proactive QoE prediction beyond traditional QoS metrics Lowest MAE and RMSE Wei et al. 2022 QuDASH – Quantum ABR Solves QUBO formulation for optimal bitrate selection Highest QoE in 68.2% of scenarios Xu et al.

**Fragmento 9 - p. 8 - score 2:**

2023. The authors suggested a customized federated learning ABR algorithm that applies a tailoring phase and aggregates knowledge from clients’ local models without exchanging raw data. In addition to improvements from context factors and personalization, experiments on 3G, 4G, and WiFi traces showed the highest overall QoE, the lowest rebuﬀering, and smoothness penalties, with an improvement of about 10% above local models, showing substantial adaptation. RL-based ABR algorithms are inadequate for optimizing QoE, especially during initial buﬀering and playback, according to D. Yang et al. 2023. They suggested a subepisodic DRL method that separated video sessions into formal playback (FP) and initial buﬀer- ing (IB) with distinct replay and optimization memories, all of which were connected by a reward mechanism based on QoE.

**Fragmento 10 - p. 9 - score 2:**

they suggested RL-based HTTP adaptive streaming with edge collaboration, which dy- namically redistributes clients to edge networks. In multi-client streaming scenarios, sim- ulations showed gains in user fairness, total QoE, and individual QoE, proving the eﬃcacy of edge-assisted RL techniques. The focus of Wang et al. 2024 was on overﬁtting and instability in RL-based ABR algorithms. An adversarial information bottleneck and imitation learning are combined in their suggested system, which learns from oﬄine optimum expert policies. Simulations showed enhanced robustness, generalization, and session-level consistency, with an average QoE increase of 7.3% and a ranking performance improvement of 30.01%.

**Fragmento 11 - p. 12 - score 2:**

where f is the original forward buﬀer seconds. This distinction is essential for improving model training and QoE analysis, as values outside the range [−30, 60] represent non-QoE behavior, which do not reﬂect perceptual video quality and should be excluded from learning and evaluation (Balachandran et al. 2013; Seufert et al. 2015; Yin et al. 2015; Mao et al. 2017). Applying this range preserves stall severity and buﬀer safety characteristics while eliminating unrealistic magnitudes, without discarding any rows. Extreme negative values typically arise from session resets, timestamp wraparounds, backward jumps in playback position, and cumulative subtraction bugs (Miller 2016; Allard et al. 2020). In contrast, extreme positive values are usually caused by paused playback, background tab buﬀering, seek-ahead artifacts, and segment prefetching during stalls (Almquist et al.

**Fragmento 12 - p. 17 - score 2:**

First, the results of the training are presented in Subsection 6.1. Next, the model’s inference tests are detailed in Subsec- tion 6.2. Finally, the decision-making behavior of MamBRA is compared against the baseline method Pensieve-PPO under a ﬂuctuating network trace using QoE evaluation metric (Subsection 6.3). 6.1 Model Training Results For a sequence-prediction model like MamBRA, and by tracking the Huber loss, the gap between what MamBRA predicted and what the network actually delivered is measured. Figure 6 illustrates the Huber loss and accuracy for the training and validation. Figure 6: Huber loss versus accuracy To provide a comprehensive view of MamBRA model’s performance, we highlight the following analysis: 16

**Fragmento 13 - p. 21 - score 2:**

Inconsistent. While it reaches high scores, many sessions experience low QoE (as low as 0.0–0.4). 7 Conclusion and Future Work This study developed MamBRA model, a new bitrate adaptation framework for video stream- ing that employs Mamba for accurate session-level bandwidth prediction. The streaming dataset are recognized by fully disconnected user sessions and the model implements a su- pervised time-series learning technique that ensures temporal consistency while explicitly limiting cross-session information leaking. The conducted test demonstrates that MamBRA has remarkably reduces prediction errors (Huber and MSE) and improves temporal sta- bility of predicted bandwidths. A signiﬁcant ﬁnding of this research work is that Mamba’s linear state-space model allows for eﬃcient and stable computation, which makes it very appropriate for real-time use.

**Fragmento 14 - p. 23 - score 2:**

In: IEEE/ACM Transactions on Networking 28.4, pp. 1698–1711. doi: 10.1109/TNET.2020.2996964. Akhtar, Zahaib et al. (2018). “Oboe: Auto-tuning Video ABR Algorithms to Network Conditions”. In: Proceedings of the 2018 Conference of the ACM Special Interest Group on Data Communication, pp. 44–58. doi: 10.1145/3230543.3230558. Pham, Stefan et al. (2020). “Evaluation of shared resource allocation using SAND for ABR streaming”. In: ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM) 16.2s, pp. 1–18. doi: 10.1145/3388926. Woo, J. et al. (2024). “Improving the Quality of Experience of Video Streaming Through a Buﬀer-Based Adaptive Bitrate Algorithm and Gated Recurrent Unit-Based Network Bandwidth Prediction”.

**Fragmento 15 - p. 1 - score 1:**

MamBRA: Session-Level Bandwidth Prediction for Adaptive Video Streaming using Selective State Space Models Jamal Hussein University of Sulaymaniyah Aree Mohammed University of Sulaymaniyah Miran Abdullah University of Sulaymaniyah Research Article Keywords: SSM-Mamba, bitrate adaptation, video streaming, network bandwidth, QoE Posted Date: May 12th, 2026 DOI: https://doi.org/10.21203/rs.3.rs-9024915/v1 License:   This work is licensed under a Creative Commons Attribution 4.0 International License. Read Full License Additional Declarations: No competing interests reported.

**Fragmento 16 - p. 2 - score 1:**

However, as user demands for high quality and low latency increase, using eﬃcient video streaming systems is getting harder. In addition to taxing network resources, the increase in video traﬃc is lower- ing video quality. Deep and transformer learning algorithms use data-driven methods to optimize video delivery, enhance QoE, and lessen network congestion in order to overcome these obstacles. Mamba utilizes the eﬃcient linear complexity of selective state space model (SSM) mechanism to process data sequences more eﬀectively. This paper proposes an adaptive video streaming framework (MamBRA) based on Mamba for session-level bandwidth prediction. The model is trained in a supervised time-series manner on disjoint user sessions to prevent information leakage and preserve temporal structure.

**Fragmento 17 - p. 2 - score 1:**

MamBRA: Session-Level Bandwidth Prediction for Adaptive Video Streaming using Selective State Space Models Jamal A. Hussein , Aree A. Mohammed, and Miran T. Abdullah Department of Computer, College of Science, University of Sulaimani, KRG, Iraq {jamal.ali, aree.ali, miran.abdullah}@univsul.edu.iq March 6, 2026 Corresponding author: Jamal A. Hussein Email: jamal.ali@univsul.edu.iq Abstract Live streaming is the real-time transmission of video content to an audience as it is simultaneously recorded. This technology is frequently utilized for applications such as covering live events and facilitating video calls. By dynamically modifying the video quality to match network conditions and device capabilities, adaptive video streaming provides improved Quality of Experience (QoE).

**Fragmento 18 - p. 3 - score 1:**

2020). When network bandwidth variations are small, ABR algorithms can operate eﬀectively because they use network bandwidth history to anticipate future network bandwidth (Akhtar et al. 2018; Pham et al. 2020). However, the QoE of video streaming frequently deteriorates in settings where network bandwidth ﬂuctuates frequently, like wireless networks, due to imprecise forecasts of future network capacity (Woo et al. 2024). In order to improve QoE in multimedia streaming, numerous studies have been car- ried out(Seufert et al. 2015; Timmerer et al. 2017). These studies have concentrated on adaptive bitrate algorithms, network optimization, predictive QoE modeling, and intelli- gent management systems to minimize buﬀering, latency, and degradation of video quality, particularly in dynamic wireless network environment.

**Fragmento 19 - p. 3 - score 1:**

1 Introduction Internet video traﬃc has surged over the past two decades, accounting for over 65% of all web traﬃc (Sandvine 2023). This growth, fueled by video-on-demand and live streaming, strains network infrastructure and complicates the delivery of a consistent Quality of Expe- rience (QoE). To address these challenges, the industry has adopted HTTP-based adaptive streaming (HAS) as the standard delivery method (Abdullah et al. 2017). HAS divides video into segments at various bitrates, enabling clients to adjust quality dynamically based on network conditions while utilizing existing HTTP infrastructure for scalability and compatibility. Major standards like Microsoft’s Smooth Streaming (MSS) (Microsoft 2008; Stockhammer 2011), Apple’s HTTP Live Streaming (HLS) (Pantos et al.

**Fragmento 20 - p. 4 - score 1:**

This approach seeks to improve energy usage without sacriﬁcing the user experience (Tien et al. 2025; X. Yang et al. 2024). 1.2 Machine Learning–Based Sequence Modeling for Bitrate Adaptation Machine learning–based approaches have been extensively adopted for bitrate adaptation in video streaming, with sequence modeling architectures such as Transformers and recurrent neural networks (RNNs) playing a particularly prominent role (Mao et al. 2017). Recently, Mamba (selective structured state-space sequence architecture) has emerged as a powerful alternative to Transformer-based models (Gu and Dao 2024). Unlike self- attention mechanisms whose computational complexity grows quadratically with sequence length, Mamba leverages selective state-space modeling to achieve linear-time complexity, enabling scalable processing of very long sequences while maintaining competitive repre- sentational capacity.

**Fragmento 21 - p. 4 - score 1:**

Its design integrates continuous-time state-space formulations with data-dependent parameterization, allowing eﬃcient parallel training and fast autoregressive inference. Due to these properties, Mamba demonstrates strong long-range dependency modeling and improved memory eﬃciency compared to traditional Transformers (Patro et al. 2025; Somvanshi et al. 2025). Recent studies have successfully extended Mamba to multiple domains (including vision, video understanding, and multimodal learning) highlighting its adaptability and robustness across tasks that require long-context modeling (G. Zhang et al. 2024; Liu et al. 2026; H. Zhang et al. 2024). These characteristics make Mamba particularly attractive for sequential decision-making and time-series applications such as adaptive video streaming, where eﬃcient long-horizon modeling and low inference latency are critical.

**Fragmento 22 - p. 4 - score 1:**

1.3 Research Contributions In this research, we propose MamBRA; an adaptive video streaming framework based on the Mamba architecture for accurate session-level bandwidth prediction. The model is developed and evaluated on a comprehensive dataset comprising diverse numerical and categorical features (Teixeira et al. 2021). User perception of streaming quality is inher- ently subjective; viewers exhibit diverse sensitivities to video artifacts and network-induced 3

**Fragmento 23 - p. 5 - score 1:**

impairments (Ran et al. 2020; Artioli et al. 2024). Therefore, the dataset is organized into multiple disjoint user sessions. To prevent information leakage and preserve temporal con- sistency, a supervised time-series learning strategy is employed, where training is conducted strictly at the session level. During inference, the proposed approach exploits the linear state-space formulation of Mamba to eﬃciently generate bandwidth predictions within each individual user session, enabling scalable and stable sequential modeling. Experimental re- sults demonstrate signiﬁcant error reduction and improved predictive accuracy. Moreover, the predicted bandwidth trajectories exhibit enhanced temporal stability.

**Fragmento 24 - p. 5 - score 1:**

The resulting decisions are assessed using quantitative performance metrics, including loss, prediction accuracy, and QoE. Dataset User Session Sequences MamBRA Model Training & Validation Inference Stage Adaptive Bandwidth Selection Performance Evaluation Loss | Accuracy | QoE Figure 1: The overall architecture and processing pipeline of MamBRA 4

**Fragmento 25 - p. 6 - score 1:**

The rest of the paper is organized as follows: Section 2 gives a review of the bitrate adaptation for live streaming using optimization techniques, while Section 3 describes the detailed structure of the Mamba framework and the SSM. Section 4 describes the dataset used to build the proposed model. Section 5 presents the proposed MamBRA model in detail. In Section 6, QoE is computed using the bandwidth values predicted by MamBRA, followed by a comparative evaluation against Pensieve-PPO. Finally, Section 7 identiﬁes upcoming trends and gaps in the literature and makes recommendations for further research. 2 Related Work Early studies on adaptive video streaming addressed the shortcomings of traditional rate- and buﬀer-based ABR methods under dynamic network conditions.

**Fragmento 26 - p. 7 - score 1:**

Evaluations against LSTM, BiLSTM, SVM, and MLP revealed the lowest MAE and RMSE, indicating superior QoE prediction accuracy and allowing for proactive management to stop deterioration of the user experience. 6


## 8. Checklist crudo para Codex / diseno Fase 4-5 v1

- [ ] Extraer exactamente que modelo/algoritmo propone.
- [ ] Extraer features/estado disponibles online y descartar future leakage.
- [ ] Extraer accion/salida y si coincide con representation_index o necesita adaptacion.
- [ ] Extraer reward/QoE/loss y relacion con qoe_linear_v1/rebuffer/smoothness.
- [ ] Extraer datasets/traces/splits y si son comparables a nuestras trazas curadas.
- [ ] Extraer baselines y escenarios donde falla/mejora.
- [ ] Extraer limitaciones y requisitos hardware/dependencias.
- [ ] Decidir si aporta a: nuevo modelo, teacher mejorado, predictor, selector, safety layer, risk-aware guard o solo contexto.


## 9. Texto crudo por pagina

Incluye texto extraido por pagina. Puede contener artefactos de dos columnas, encabezados, pies, referencias o formulas degradadas. Consultar `raw_text_layout/` para extraccion layout completa.


### Pagina 1
```text
MamBRA: Session-Level Bandwidth Prediction for
Adaptive Video Streaming using Selective State
Space Models
Jamal Hussein 
University of Sulaymaniyah
Aree Mohammed 
University of Sulaymaniyah
Miran Abdullah 
University of Sulaymaniyah
Research Article
Keywords: SSM-Mamba, bitrate adaptation, video streaming, network bandwidth, QoE
Posted Date: May 12th, 2026
DOI: https://doi.org/10.21203/rs.3.rs-9024915/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Additional Declarations: No competing interests reported.
```


### Pagina 2
```text
MamBRA: Session-Level Bandwidth Prediction for Adaptive
Video Streaming using Selective State Space Models
Jamal A. Hussein
, Aree A. Mohammed, and Miran T. Abdullah
Department of Computer, College of Science,
University of Sulaimani, KRG, Iraq
{jamal.ali, aree.ali, miran.abdullah}@univsul.edu.iq
March 6, 2026
Corresponding author:
Jamal A. Hussein
Email:
jamal.ali@univsul.edu.iq
Abstract
Live streaming is the real-time transmission of video content to an audience as it
is simultaneously recorded. This technology is frequently utilized for applications such
as covering live events and facilitating video calls. By dynamically modifying the video
quality to match network conditions and device capabilities, adaptive video streaming
provides improved Quality of Experience (QoE). However, as user demands for high
quality and low latency increase, using eﬃcient video streaming systems is getting
harder. In addition to taxing network resources, the increase in video traﬃc is lower-
ing video quality. Deep and transformer learning algorithms use data-driven methods
to optimize video delivery, enhance QoE, and lessen network congestion in order to
overcome these obstacles. Mamba utilizes the eﬃcient linear complexity of selective
state space model (SSM) mechanism to process data sequences more eﬀectively. This
paper proposes an adaptive video streaming framework (MamBRA) based on Mamba for
session-level bandwidth prediction. The model is trained in a supervised time-series
manner on disjoint user sessions to prevent information leakage and preserve temporal
structure. During inference, it leverages the linear state-space formulation of Mamba
to eﬃciently generate stable bandwidth predictions within each session. Experimen-
tal results demonstrate reduced prediction error, improved accuracy, and enhanced
temporal stability. The model achieves an overall inference accuracy of 93.94%, with
session-level accuracy reaching as high as 97.32%. Furthermore, the predicted band-
width achieves more consistent QoE scores compared to the PPO-based approach used
in Pensieve.
Keywords: SSM-Mamba, bitrate adaptation, video streaming, network bandwidth, QoE.
1
```


### Pagina 3
```text
1
Introduction
Internet video traﬃc has surged over the past two decades, accounting for over 65% of all
web traﬃc (Sandvine 2023). This growth, fueled by video-on-demand and live streaming,
strains network infrastructure and complicates the delivery of a consistent Quality of Expe-
rience (QoE). To address these challenges, the industry has adopted HTTP-based adaptive
streaming (HAS) as the standard delivery method (Abdullah et al. 2017). HAS divides
video into segments at various bitrates, enabling clients to adjust quality dynamically
based on network conditions while utilizing existing HTTP infrastructure for scalability
and compatibility. Major standards like Microsoft’s Smooth Streaming (MSS) (Microsoft
2008; Stockhammer 2011), Apple’s HTTP Live Streaming (HLS) (Pantos et al. 2017; Apple
Inc. 2024), and MPEG’s Dynamic Adaptive Streaming over HTTP (MPEG-DASH)(DASH
Industry Forum 2024) have solidiﬁed HAS as the global norm.
However, live streaming remains challenging as providers must balance low latency, high
visual quality, and network eﬃciency (Yin et al. 2015; T.-Y. Huang et al. 2014). These com-
peting demands under ﬂuctuating bandwidth have sparked ongoing research into bitrate
adaptation and buﬀer management. Ultimately, the need to minimize rebuﬀering while
maintaining stability continues to drive innovation in streaming algorithms and system
design.
1.1
Challenges in Adaptive Bitrate (ABR) Streaming
Streaming services use adaptive bitrate (ABR) algorithms to manage network bandwidth
ﬂuctuations for better QoE (Spiteri et al. 2020). When network bandwidth variations are
small, ABR algorithms can operate eﬀectively because they use network bandwidth history
to anticipate future network bandwidth (Akhtar et al. 2018; Pham et al. 2020). However,
the QoE of video streaming frequently deteriorates in settings where network bandwidth
ﬂuctuates frequently, like wireless networks, due to imprecise forecasts of future network
capacity (Woo et al. 2024).
In order to improve QoE in multimedia streaming, numerous studies have been car-
ried out(Seufert et al. 2015; Timmerer et al. 2017). These studies have concentrated on
adaptive bitrate algorithms, network optimization, predictive QoE modeling, and intelli-
gent management systems to minimize buﬀering, latency, and degradation of video quality,
particularly in dynamic wireless network environment. Taha, Ali, et al. 2021 introduced an
automated model to accurately evaluate and predict QoE for adaptive video streaming over
wireless networks by utilizing objective performance metrics. Therefore, a QoE-aware adap-
tive management system is proposed in order to reduce buﬀering and quality degradation
by dynamically optimizing HD video streaming over wireless network environments (Taha,
Canovas, et al. 2021).
The beneﬁts of adaptive video streaming—better quality and user experience—come
at the cost of high bandwidth consumption and excessive video traﬃc. Since this volume
2
```


### Pagina 4
```text
of video data contributes to congestion, elevated costs, and high energy usage (George
et al. 2025), among other issues, developing video traﬃc optimization methods is critically
important. Furthermore, delivering high video quality and a positive QoE remains a core
objective in video streaming. Since algorithms rely on QoE feedback to adjust streaming
quality, the ﬁeld heavily invests in research aimed at creating reliable and accurate QoE
models (Jia et al. 2025). Another challenge is the energy consumption, which is a main
concern across a live video streaming pipeline. Conventional machine and deep learning
models oﬀer a solution to these problems by enabling energy-aware video encoding and
quality adaptation. This approach seeks to improve energy usage without sacriﬁcing the
user experience (Tien et al. 2025; X. Yang et al. 2024).
1.2
Machine Learning–Based Sequence Modeling for Bitrate Adaptation
Machine learning–based approaches have been extensively adopted for bitrate adaptation in
video streaming, with sequence modeling architectures such as Transformers and recurrent
neural networks (RNNs) playing a particularly prominent role (Mao et al. 2017).
Recently, Mamba (selective structured state-space sequence architecture) has emerged
as a powerful alternative to Transformer-based models (Gu and Dao 2024). Unlike self-
attention mechanisms whose computational complexity grows quadratically with sequence
length, Mamba leverages selective state-space modeling to achieve linear-time complexity,
enabling scalable processing of very long sequences while maintaining competitive repre-
sentational capacity. Its design integrates continuous-time state-space formulations with
data-dependent parameterization, allowing eﬃcient parallel training and fast autoregressive
inference.
Due to these properties, Mamba demonstrates strong long-range dependency modeling
and improved memory eﬃciency compared to traditional Transformers (Patro et al. 2025;
Somvanshi et al. 2025).
Recent studies have successfully extended Mamba to multiple
domains (including vision, video understanding, and multimodal learning) highlighting its
adaptability and robustness across tasks that require long-context modeling (G. Zhang
et al. 2024; Liu et al. 2026; H. Zhang et al. 2024). These characteristics make Mamba
particularly attractive for sequential decision-making and time-series applications such as
adaptive video streaming, where eﬃcient long-horizon modeling and low inference latency
are critical.
1.3
Research Contributions
In this research, we propose MamBRA; an adaptive video streaming framework based on
the Mamba architecture for accurate session-level bandwidth prediction.
The model is
developed and evaluated on a comprehensive dataset comprising diverse numerical and
categorical features (Teixeira et al. 2021). User perception of streaming quality is inher-
ently subjective; viewers exhibit diverse sensitivities to video artifacts and network-induced
3
```


### Pagina 5
```text
impairments (Ran et al. 2020; Artioli et al. 2024). Therefore, the dataset is organized into
multiple disjoint user sessions. To prevent information leakage and preserve temporal con-
sistency, a supervised time-series learning strategy is employed, where training is conducted
strictly at the session level. During inference, the proposed approach exploits the linear
state-space formulation of Mamba to eﬃciently generate bandwidth predictions within each
individual user session, enabling scalable and stable sequential modeling. Experimental re-
sults demonstrate signiﬁcant error reduction and improved predictive accuracy. Moreover,
the predicted bandwidth trajectories exhibit enhanced temporal stability. From a QoE per-
spective, the predicted bandwidth yields more consistent QoE scores than those obtained
using the PPO-based strategy implemented in Pensieve (Mao et al. 2017; godka 2025),
highlighting the eﬀectiveness of the proposed framework for adaptive bitrate streaming
optimization. The main contributions of the proposed approach can be summarized as
follows:
1. Novel dataset structuring at the session level: The dataset is reorganized into fully
disjoint user sessions with heterogeneous numerical and categorical features, enabling
realistic temporal modeling while explicitly preventing cross-session information leak-
age.
2. Session-aware supervised training strategy: A time-series learning framework is de-
signed where training is strictly performed at the session level, preserving sequential
dependencies and ensuring fair generalization across independent user trajectories.
3. Eﬃcient inference via linear state-space modeling: The inference procedure leverages
the linear state-space formulation of Mamba to generate stable and computationally
eﬃcient bandwidth predictions within each session, improving temporal smoothness
and robustness.
4. QoE-oriented performance validation:
Beyond prediction accuracy and error re-
duction, the framework demonstrates more consistent QoE outcomes compared to
Pensieve-PPO, highlighting its practical advantage for adaptive bitrate streaming.
Architectural overview of the proposed MamBRA framework is shown in Figure 1. User
session data are utilized for model training and validation, followed by an inference stage
that performs adaptive bandwidth selection. The resulting decisions are assessed using
quantitative performance metrics, including loss, prediction accuracy, and QoE.
Dataset
User Session
Sequences
MamBRA Model
Training & Validation
Inference Stage
Adaptive Bandwidth
Selection
Performance Evaluation
Loss | Accuracy | QoE
Figure 1: The overall architecture and processing pipeline of MamBRA
4
```


### Pagina 6
```text
The rest of the paper is organized as follows: Section 2 gives a review of the bitrate
adaptation for live streaming using optimization techniques, while Section 3 describes the
detailed structure of the Mamba framework and the SSM. Section 4 describes the dataset
used to build the proposed model. Section 5 presents the proposed MamBRA model in detail.
In Section 6, QoE is computed using the bandwidth values predicted by MamBRA, followed
by a comparative evaluation against Pensieve-PPO. Finally, Section 7 identiﬁes upcoming
trends and gaps in the literature and makes recommendations for further research.
2
Related Work
Early studies on adaptive video streaming addressed the shortcomings of traditional rate-
and buﬀer-based ABR methods under dynamic network conditions. Therefore, a variety
of optimization strategies were then investigated by researchers in an eﬀort to enhance
bitrate adaptability. The goal of these strategies was to balance playback stability, re-
buﬀering reduction, and video quality in order to improve QoE. Table 1 demonstrates the
recent research on optimization algorithms that investigated to enhance QoE. Below a brief
description of each algorithm is provided.
Mao et al. 2017 discussed the drawbacks of conventional ABR algorithms in dynamic
network scenarios. They presented Pensieve, a system based on reinforcement learning
that trains a neural network to choose bitrate based on past streaming results. Evalua-
tions revealed that it outperformed rate-based, buﬀer-based, and MPC schemes, improving
average QoE by 12% to 25% and exhibiting strong performance in previously untested net-
work circumstances.
Conventional Adaptive Bitrate (ABR) algorithms mostly ignore user-speciﬁc content
preferences in favor of optimizing network-level metrics like bitrate stability and rebuﬀering
avoidance. Sengupta et al. 2018 introduced HotDASH, a hotspot-aware video streaming
framework based on an actor-critic neural network and a cascaded deep reinforcement
learning architecture, to overcome this limitation. Their technique allows the reinforce-
ment learning agent to opportunistically prefetch video segments that suit user preferences
while also optimizing bitrate selection. HotDASH dramatically increases user satisfaction
and streaming eﬃciency by integrating preference awareness into the adaptation strategy.
According to experimental assessments, the suggested system outperforms traditional ABR
techniques in terms of average delivered bitrate by 14.31% and improves QoE by 16.2%.
Key drawbacks of learning-based Adaptive Bit Rate (ABR) streaming were discussed
by T. Huang et al. 2019, including low sample eﬃciency and inadequate perceptual video
quality consideration. They presented Comyco, a video quality-aware ABR method that
uses imitation learning and trains its neural network on expert trajectories produced by
an instant solver. This approach maximizes the use of gathered data and reduces unnec-
essary exploration. Comyco improves the overall QoE by choosing video chunks based on
perceptual quality rather than just bitrate. This results in faster training, fewer sample
5
```


### Pagina 7
```text
Table 1: Enhancement of QoE through the evolution of adaptation algorithms
Investigation
Adaptation Algorithm
Key Contributions
QoE Improvements
Mao et al.
2017
Pensieve – RL
Neural network selects bitrate
based on past streaming states
+12–25% average QoE
Sengupta
et al. 2018
HotDASH – Actor–Critic
& Cascaded DRL
Incorporates user preferences and
prefetching strategies
+14.31% bitrate, +16.2%
QoE
T. Huang
et al. 2019
Comyco – Imitation
Learning
Trains on expert trajectories to
reduce exploration overhead
+7.5–16.79% perceptual
QoE
Dinaki et al.
2021
BiLSTM–CNN Hybrid
Proactive QoE prediction beyond
traditional QoS metrics
Lowest MAE and RMSE
Wei et al.
2022
QuDASH – Quantum ABR
Solves QUBO formulation for
optimal bitrate selection
Highest QoE in 68.2% of
scenarios
Xu et al.
2023
Federated Learning ABR
Client-speciﬁc models without
raw data exchange
∼10% QoE gain, reduced
rebuﬀering
D. Yang
et al. 2023
Subepisodic DRL
Separate buﬀering and playback
memories for control stability
Smoother bitrate, fewer
stalls
Darwich
et al. 2024
CNN–RNN Hybrid
Frame-level bitrate estimation for
ﬁne-grained adaptation
+16.6% QoE, +37.1%
bitrate, –87.5% rebuﬀering
Woo et al.
2024
GRU-Based Bandwidth &
Buﬀer ABR
Throughput prediction with
minimized bitrate switching
Up to +40% MOS
Kang et al.
2024
RL Edge-Assisted ABR
Multi-client edge-assisted
adaptive streaming
Improved fairness and QoE
Wang et al.
2024
Adversarial Information
Bottleneck + Imitation
Learning
Robust QoE modeling with
reduced overﬁtting
+7.3% QoE, +30% ranking
Ling et al.
2025
Adversarial Inverse RL
(AIRL)
Generalizes to unseen network
conditions
+4.3–9.4% video quality,
–0.054–6.2% stall
Naseh et al.
2025
DRL with DDPG
Edge-DASH
Joint user–server bitrate
allocation
Higher QoE, fewer bitrate
errors
J. Zhang
et al. 2025
PLL-ABR – DRL with
PPO, LSTM & Attention
Improves bitrate stability and
prediction accuracy
∼28.5% QoE gain
requirements, and an average QoE that is 7.5%–16.79% higher than previous methods.
In 2020, researchers began addressing the gap in proactive video QoE prediction be-
yond traditional QoS metrics. Dinaki et al. 2021 addressed the problem of proactively
predicting video QoE beyond QoS metrics and delayed client measurements. A BiLSTM-
CNN hybrid model was suggested, in which CNN recovers local patterns from multivariate
time series and BiLSTM captures temporal dependencies.
Evaluations against LSTM,
BiLSTM, SVM, and MLP revealed the lowest MAE and RMSE, indicating superior QoE
prediction accuracy and allowing for proactive management to stop deterioration of the
user experience.
6
```


### Pagina 8
```text
In order to maximize user QoE, Wei et al. 2022 pointed out that traditional adaptive
bitrate (ABR) techniques frequently struggle to optimize bitrate selection and minimize
rebuﬀering at the same time. As a quantum-inspired ABR control method, QuDASH was
presented to get around these restrictions.
To ﬁnd the best bitrates, it uses a Digital
Annealer to solve a Quadratic Unconstrained Binary Optimization (QUBO) problem that
models buﬀer conditions, bitrate ﬂuctuations, and video quality. Based on actual network
traces, simulation results show that QuDASH outperforms current ABR techniques, at-
taining the highest QoE in 68.2% of scenarios, conﬁrming its eﬃcacy in improving user
experience.
ABR adaptation under various networks and numerous QoE objectives was the main
focus of the research conducted by Xu et al. 2023. The authors suggested a customized
federated learning ABR algorithm that applies a tailoring phase and aggregates knowledge
from clients’ local models without exchanging raw data. In addition to improvements from
context factors and personalization, experiments on 3G, 4G, and WiFi traces showed the
highest overall QoE, the lowest rebuﬀering, and smoothness penalties, with an improvement
of about 10% above local models, showing substantial adaptation.
RL-based ABR algorithms are inadequate for optimizing QoE, especially during initial
buﬀering and playback, according to D. Yang et al. 2023. They suggested a subepisodic
DRL method that separated video sessions into formal playback (FP) and initial buﬀer-
ing (IB) with distinct replay and optimization memories, all of which were connected by
a reward mechanism based on QoE. Based on enhanced HE-EMDQN frameworks, this
technique allowed for smoother, more eﬃcient bitrate adaption, decreased inter-phase in-
terference, and increased sample eﬃciency.
Better initial buﬀering performance, faster
convergence, fewer rebuﬀering events, and improved QoE were observed in experimental
ﬁndings on both synthetic and actual network traces compared to conventional RL and
episodic DRL approaches.
Optimizing video quality in dynamic networks while reducing bandwidth and playback
interruptions was studied by Darwich et al. 2024. With RNN estimating the ideal bitrate
per frame and CNN extracting information from video frames, they suggested a hybrid
CNN-RNN architecture.
By reducing rebuﬀering by 87.5%, improving QoE by 16.6%,
and increasing average bitrate by 37.1%, experimental results demonstrated improved user
experience and smoother playing compared to current ABR techniques.
ABR performance and QoE are negatively impacted by erroneous network predictions,
which Woo et al. 2024 addressed. They suggested a buﬀer-based ABR algorithm com-
bined with a Gated Recurrent Unit (GRU)-based network bandwidth prediction model,
which forecasts throughput and playback metrics by utilizing GRU’s temporal dependency
modelling. The method, which was tested in train, bus, and pedestrian situations, elim-
inated rebuﬀering, minimized quality switches, and oﬀered up to 40% greater MOS than
conventional ABR schemes especially in extremely changeable network conditions.
In situations with multiple clients, where traditional ABR is unable to guarantee sta-
bility and fairness, Kang et al. 2024 concentrated on adaptive streaming. For best results,
7
```


### Pagina 9
```text
they suggested RL-based HTTP adaptive streaming with edge collaboration, which dy-
namically redistributes clients to edge networks. In multi-client streaming scenarios, sim-
ulations showed gains in user fairness, total QoE, and individual QoE, proving the eﬃcacy
of edge-assisted RL techniques.
The focus of Wang et al. 2024 was on overﬁtting and instability in RL-based ABR
algorithms. An adversarial information bottleneck and imitation learning are combined
in their suggested system, which learns from oﬄine optimum expert policies. Simulations
showed enhanced robustness, generalization, and session-level consistency, with an average
QoE increase of 7.3% and a ranking performance improvement of 30.01%.
Robust ABR in heterogeneous networks was discussed by Ling et al. 2025. In order to
learn reward functions independent of policies and allow for ﬂexible adaptation to diﬀerent
QoE targets and unseen networks, they devised an adversarial inverse reinforcement learn-
ing (AIRL) system that makes use of expert demonstrations. Experiments demonstrated
a 4.3%–9.4% improvement in video quality and a 0.054%–6.2% reduction in stall time,
demonstrating strong adaptation and excellent use of expert knowledge.
In multi-tier Edge-DASH networks, a Deep Reinforcement Learning (DRL) framework
utilizing Deep Deterministic Policy Gradient (DDPG) has been developed by Naseh et
al. 2025 for joint User-to-Server Allocation (USA) and Bitrate Allocation (BrA). While
real-time transcoding takes care of edge storage constraints, the DDPG agent dynamically
chooses the best streaming sources; edge, macro, or cloud and matching bitrates. In 5G-
enabled multi-tier video streaming, simulations demonstrate that this strategy outperforms
conventional network-driven and hybrid edge-cloud techniques by improving QoE, lowering
bitrate errors, and minimizing transcoding violations.
J. Zhang et al. 2025 suggest Predictive LSTM Local Attention ABR (PLL-ABR), an
Adaptive Bitrate (ABR) algorithm based on Deep Reinforcement Learning (DRL) that
makes use of the Proximal Policy Optimization (PPO) framework enhanced with dual
clipping, Long Short-Term Memory (LSTM) networks, and local attention mechanisms. By
increasing bitrate decision accuracy and stability, this method raises QoE. Experimental
results show a QoE gain of about 28.5% across bandwidth usage, rebuﬀering, and playback
smoothness parameters when compared to numerous state-of-the-art ABR algorithms.
The review identiﬁes various research challenges and gaps in adaptive bitrate optimiza-
tion for live streaming as follows:
• Most techniques handle live streaming like VoD; live-speciﬁc latency restrictions are
rarely addressed.
• Many studies rely on synthetic or VoD traces due to the lack of realistic live-network
datasets.
• ML/DRL ABR models often show weak generalization to unseen network conditions.
• Insuﬃcient analysis of failure modes and safety of learning-based ABR.
8
```


### Pagina 10
```text
• Mobile device energy and computation costs are frequently disregarded.
3
Mamba Framework
Mamba introduces input-dependent selectivity into state space models (SSMs), enabling
content-aware sequence modeling with linear time complexity (Gu and Dao 2024). Rather
than relying on attention (Vaswani et al. 2017), Mamba performs selective state transitions
using structured SSMs.
Let xt ∈RD denote the input at time step t, and let ht ∈RN denote the latent state.
Mamba models the sequence using the discrete-time recurrence
ht = ¯Atht−1 + ¯Btxt,
yt = Ctht,
where ¯At ∈RN×N, ¯Bt ∈RN×D, and Ct ∈RD×N are input-dependent parameters.
The discrete parameters are derived from an underlying continuous-time system with
diagonal state matrix A ∈RN×N (Gu, Goel, et al. 2022). Given a per-token step size
∆t > 0, the discretization is
¯At = exp(∆tA),
¯Bt = A−1 (exp(∆tA) −I) Bt,
where I ∈RN×N is the identity matrix.
Selectivity is introduced by making the parameters functions of the input:
Bt = sB(xt),
Ct = sC(xt),
∆t = softplus(θ + s∆(xt)).
Here, sB(·), sC(·), and s∆(·) are learned linear projections. This design enables adaptive
state updates, memory retention, and readout at each time step.
Because the parameters vary across time steps, convolution-based acceleration used in
time-invariant SSMs is no longer applicable.
Mamba instead employs a hardware-aware
parallel scan (preﬁx-sum) algorithm to evaluate the recurrence eﬃciently, achieving linear
time complexity and logarithmic parallel depth.
4
Dataset Description and Preparation
For modeling the proposed system, we utilized the comprehensive statistical dataset intro-
duced by Teixeira et al. 2021. Fourteen features were selected and adapted for use during
both the training and inference phases of our model. A total of approximately 1.4 million
records, distributed across 1,966 user sessions, were extracted and preprocessed for this
study.
9
```


### Pagina 11
```text
The selected features are grouped into several categories, including session-level,
network-level, and client-level attributes.
The dataset consists of numerous client ses-
sions recorded as streaming events at 4-second intervals, providing playback statistics and
related metrics corresponding to the aforementioned categories, as summarized in Table 2.
Table 2: Segment downloads, stream switching, network, and buﬀering behavior of the
dataset (Teixeira et al. 2021).
Type
Category
Feature
Description
Numeric
Session
sessionID
The player’s session number.
sequenceID
A number associated with each video segment
(event) within a session.
Time
videoSecs
Seconds viewed between the last two segments.
bufferForwardSecs
Seconds of video buﬀered but not viewed yet.
bufferDeficitSecs
Seconds of video playback missing due to stalling.
rebufferingSecs
Seconds buﬀered between the last two segments.
rebufferingCount
Times buﬀering occurs between the last two seg-
ments.
Network
bytesTransferred
Bytes transferred since the start of the session.
bandwidthMBPS
Network bandwidth.
Categorical
Client
deviceType
{desktop, tv, tablet, mobile, . . . }
deviceOS
{windows, android, other, ios, web_os, . . . }
browser
{chrome, other, ﬁrefox, edge, . . . }
player
{web, app}
playerDim
110 dimensions (width×height).
The feature playerDim is obtained by merging two numeric columns in the original
dataset, resulting in 110 distinct player dimension categories. The segment duration is
ﬁxed at four seconds across all sessions. Session-level features include sessionID and
sequenceID, where sessionID groups events belonging to the same user session and
sequenceID denotes the temporal order of events within a session.
Following established outlier detection practices in multimedia crowdsourcing [Chen et
al., 2014], extreme positive and negative values of bufferForwardSecs were observed
due to player state transitions and logging artifacts. To preserve physical interpretability,
this signal was clipped to a bounded range [−30, 60] seconds and decomposed into buﬀer oc-
cupancy (bufferForwardSecs) and buﬀer deﬁcit (bufferDeficitSecs) components,
as deﬁned by the equations below.
ˆf = min(60, max(−30, f))
bufferForwardSecs = max(0, ˆf)
bufferDeficitSecs = max(0, −ˆf)
10
```


### Pagina 12
```text
where f is the original forward buﬀer seconds.
This distinction is essential for improving model training and QoE analysis, as values
outside the range [−30, 60] represent non-QoE behavior, which do not reﬂect perceptual
video quality and should be excluded from learning and evaluation (Balachandran et al.
2013; Seufert et al. 2015; Yin et al. 2015; Mao et al. 2017). Applying this range preserves
stall severity and buﬀer safety characteristics while eliminating unrealistic magnitudes,
without discarding any rows. Extreme negative values typically arise from session resets,
timestamp wraparounds, backward jumps in playback position, and cumulative subtraction
bugs (Miller 2016; Allard et al. 2020). In contrast, extreme positive values are usually
caused by paused playback, background tab buﬀering, seek-ahead artifacts, and segment
prefetching during stalls (Almquist et al. 2018; Xie et al. 2024).
Figure 2 illustrates the distribution of rows and sessions across the diﬀerent classes
within the four categorical features deviceType, deviceOS, browser and player.
The length of each bar indicates the number of rows associated with a given feature, while
the numbers displayed on the bars denote the corresponding number of sessions.
The
majority of user sessions were conducted via the Chrome web browser on desktop comput-
ers running the Windows operating system. Mobile phones and TV devices running the
Android operating system accounted for the second and third highest number of sessions,
respectively.
Figure 2: Distribution of sessions and rows among categorical features
5
Training and Inference Procedures of the MamBRA Model
We train the proposed MamBRA using session-aware sliding windows of 20 timesteps with
stride 1, applied independently within each user session after standardizing numeric fea-
11
```


### Pagina 13
```text
tures and embedding categorical features. At inference time, the model operates in a fully
online and stateful manner, processing observations sequentially without windowing. After
a brief 20-timestep warm-up to initialize the SSM state, the model produces per-timestep
bandwidth predictions, with the state reset only at session boundaries.
5.1
Feature Preprocessing and Session-Aware Sliding-Window Segmentation
The dataset consists of both numeric (throughput and buﬀer occupancy) and categorical
(device indicators) features, and is organized into disjoint user sessions, each correspond-
ing to a continuous playback episode. All preprocessing and windowing operations are
performed at the session level to prevent information leakage across sessions.
Numeric features are standardized using z-score normalization (standard scaling), where
the mean and standard deviation are computed from the training split and subsequently
applied to validation data. Categorical features are transformed using feature-wise label
encoding, mapping each categorical value to an integer index. These encoded categorical
features are then used as inputs to learned embedding layers within the model. The dataset
is divided into training, validation, and testing sets using a 70%/10%/20% split.
The
detailed procedures for preprocessing, normalization, windowing, and data partitioning
are illustrated in Figure 3.
clean-up
and split
Original data
Test data
Numeric features
Categorical features
Train-Validation data
Scaler
Encoders
Preprocesser
group by
sessionID
generate sequences
per session group
(window=20)
split to train
and validation
Validation data
Train data
100%
80%
20%
70%
10%
Figure 3: Dataset preparation (clean-up, normalization, sequencing and splitting)
The dataset is ﬁrst partitioned into disjoint user sessions, where each session corre-
sponds to a continuous playback episode. Sliding-window segmentation is performed inde-
pendently within each session to prevent information leakage across session boundaries.
For a given session s of length Ts consisting of a sequence of network and playback
feature vectors {xt}Ts
t=1, training and validation samples are constructed using a window
size of 20 timesteps and a stride of 1. At each timestep t, the model input is deﬁned as
Xt = [xt−19, xt−18, . . . , xt] ,
12
```


### Pagina 14
```text
and the corresponding prediction target is the next-step bandwidth value yt+1.
Using a stride of 1 generates a prediction target at every valid timestep within each
session, resulting in maximally overlapping windows and dense supervision. This approach
ensures that the model is trained to make bandwidth predictions at all decision points
encountered during a session, closely aligning the training procedure with the online ABR
setting, where bitrate adaptation decisions are made continuously throughout playback.
The choice of a window length of 20 timesteps captures short-term temporal depen-
dencies within a session, such as recent throughput ﬂuctuations and transient network
conditions, while avoiding unnecessary long-range context that may span multiple, po-
tentially heterogeneous sessions. Session-level windowing further ensures that temporal
dependencies are learned strictly within coherent playback contexts, improving both mod-
eling ﬁdelity and evaluation validity.
5.2
MamBRA Training and Validation Pipelines
The diagram shown in Figure 4 illustrates the architecture and training workﬂow of a
machine learning model utilizing a Mamba Block (a State Space Model architecture). The
ﬂow is divided into two main paths: the training pipeline (solid lines) and the validation
pipeline (dashed lines).
Numeric features
Categorical features
Train data
Concatenate
Categorical
Embeddings
(per feature)
Numeric features
Categorical features
Validation data
Input Projection
Linear
Mamba Block
(Sequence Scan)
RMSNorm
Linear Head
Prediction
(Last Time Step)
Huber Loss
AdamW
Backprop
gradients enabled
Huber Loss
MSE Loss
no gradients
Core MamBRA
train
validation
shared
Figure 4: Training and validation process of MamBRA model
1. Data Input and Preprocessing
The model handles two types of data from both the training and validation sets:
13
```


### Pagina 15
```text
• Categorical Features: These are passed through an Embedding layer, which
converts discrete categories into continuous vectors.
• Numeric Features: These are passed after normalization (Figure 3) to be com-
bined with the embeddings.
• Concatenation: Both feature types are merged into a single representation before
entering the main model block.
2. Core Model Architecture
The dotted box contains the primary neural network components that constitute the
MamBRA model:
• Input Projection: A linear layer that maps the concatenated features into the
model’s hidden dimension.
• Mamba Block (Sequence Scan): This is the heart of the model. Unlike standard
Transformers, Mamba uses a selective SSM to process sequences eﬃciently, which
is particularly good at capturing long-range dependencies.
• RMSNorm and Linear Head: The output of the Mamba block is normalized
using Root Mean Square Layer Normalization and then passed through a ﬁnal
linear layer to project it to the target output size.
• Prediction (Last Time Step): The model extracts the prediction from the ﬁnal
time step to make its assessment.
3. Loss Functions and Optimization
The diagram distinguishes how the model is evaluated during diﬀerent phases:
Phase
Gradient Status
Loss Functions Used
Optimizer
Train
Enabled
Huber Loss
AdamW Backprop
Validation
Disabled
Huber Loss & MSE Loss
N/A
• Huber Loss: Used as the primary training objective. It is often preferred over
MSE (Mean Squared Error) because it is less sensitive to outliers in the data.
• AdamW: The optimizer used to update the model weights based on the calcu-
lated gradients during the training phase.
Essentially, the model takes a mix of categorical and numerical data, embeds them,
processes them through a Mamba sequential architecture, and uses Huber loss to guide the
AdamW optimizer during training. During validation, it checks performance using both
Huber and MSE losses to ensure the model generalizes well without updating the weights.
14
```


### Pagina 16
```text
5.3
Inference Procedure
At inference time, MamBRA is applied in an online, sequential manner to generate bandwidth
predictions within each user session. In contrast to training, where ﬁxed-length sliding
windows are used to construct supervised samples, inference does not rely on windowing
or stride-based segmentation. Figure 5 illustrates the inference procedure of MamBRA.
Test data
(one session)
Numeric features
(-bandwidthMBPS)
Categorical features
bandwidthMBPS
Scaler
(Standard)
Encoders
Preprocesser
Warm-up phase
(window=20)
MamBRA
Prediction
Inverse-scaler
(Standard)
predicted
bandwidth
Huber, MSE,
RMSE, NRMSE
Accuracy
CDF Anlaysis
→MOS
→QoE
Figure 5: Inference process of MamBRA for one session of the test data
For a given session s of length Ts with a sequence of preprocessed input features x(s)
t
Ts
t=1,
the model processes observations one timestep at a time, updating its internal recurrent
state at each step. The SSM maintains a hidden state that summarizes past information
and evolves according to the learned state transition dynamics. This enables the model to
incorporate arbitrarily long temporal context without explicitly storing past inputs.
To ensure a well-initialized internal state, inference begins with a warm-up phase,
during which the ﬁrst W timesteps (with W = 20, matching the training window length)
are fed sequentially into the model without using the corresponding outputs for evaluation
or decision-making. After this warm-up, the model generates a bandwidth prediction at
every subsequent timestep.
Formally, for each timestep t ≥W, the model updates its internal state using the
current input x(s)
t
and produces a prediction ˆy(s)
t+1 for the next-step bandwidth:
(ˆy(s)
t+1, h(s)
t ) = fSSM(x(s)
t , h(s)
t−1),
where h(s)
t
denotes the SSM hidden state at timestep t.
This inference strategy yields dense, per-timestep predictions throughout the session
and closely reﬂects the online ABR deployment scenario, in which bitrate adaptation de-
15
```


### Pagina 17
```text
cisions are made continuously as new network observations arrive. Importantly, the SSM
state is reset only at session boundaries, ensuring that temporal dependencies are learned
and applied strictly within individual playback sessions.
In summary, inference is performed in a fully online and stateful manner, leveraging
the recurrent dynamics of Mamba to integrate historical context eﬃciently. The warm-up
phase aligns the internal state with recent session dynamics, while step-by-step process-
ing enables continuous, low-latency bandwidth prediction suitable for real-time adaptive
bitrate control.
6
Results and Discussion
In this section, various tests are presented that demonstrate the performance of the pro-
posed MamBRA model in terms of loss, accuracy, and QoE. First, the results of the training
are presented in Subsection 6.1. Next, the model’s inference tests are detailed in Subsec-
tion 6.2. Finally, the decision-making behavior of MamBRA is compared against the baseline
method Pensieve-PPO under a ﬂuctuating network trace using QoE evaluation metric
(Subsection 6.3).
6.1
Model Training Results
For a sequence-prediction model like MamBRA, and by tracking the Huber loss, the gap
between what MamBRA predicted and what the network actually delivered is measured.
Figure 6 illustrates the Huber loss and accuracy for the training and validation.
Figure 6: Huber loss versus accuracy
To provide a comprehensive view of MamBRA model’s performance, we highlight the
following analysis:
16
```


### Pagina 18
```text
• Correlation between “Loss and Accuracy”: From Figure 6 we can see that when Huber
loss drops quickly in the ﬁrst 20 epochs accuracy goes up sharply. This shows that
when Huber loss goes down accuracy goes up meaning that the model is eﬀectively
optimizing its internal weights to minimize prediction errors.
• Learning stability: The training accuracy, shown as a solid line keeps going up and
until it reaches 93%. At that point the validation’s accuracy, represented by a red
dashed line levels oﬀat, around 88%.
This high validation accuracy shows that
the Mamba state-space architecture is successfully capturing the complex temporal
dependencies of the network traces.
• Generalization Gap: The model appears to generalize well to unseen, unexplored
network conditions, as indicated by the narrow diﬀerence between the training and
validation accuracy curves.
6.2
Inference Tests
Unlike the training phase, where the model adjusts its weights based on a loss function
(like Huber loss), the inference test focuses on how the model actually acts in a real-world
simulation.
Over all dataset sessions used during inference, the model attains a mean
squared error (MSE) of 3669.33, a root mean squared error (RMSE) of 60.58, a normalized
RMSE (NRMSE, computed by normalizing the MSE over the range Max–Min) of 0.06,
and an overall accuracy of 93.94%. The remainder of this subsection provides a detailed
examination of these performance metrics at the individual session level.
6.2.1
Loss
Figure 7 presents a performance breakdown of a model across four features: deviceOS,
deviceType, browser, and player. It uses two distinct visualizations to compare raw
error magnitudes against relative accuracy.
The heatmap displays three error metrics:
MSE, RMSE, and NRMSE.
For deviceOS, Android is the top performer in terms of error reduction, boasting the
lowest MSE (100) and a very low NRMSE (0.032) with the high accuracy rate (96.77%).
While for deviceType, Mobile is clearly the “cleanest” category for the model and leads
the pack, nearing 100% accuracy. This correlates perfectly with the low error values as
shown in the heatmap. What is related to the web browsers, the model performs very
consistently across diﬀerent browsers. Finally, the web player displays slightly higher ac-
curacy (approx. 94-95%) compared to the app player (approx. 91-92%) with a minimum
NRMSE=0.064.
17
```


### Pagina 19
```text
deviceType
DeviceOS
browser
player
Figure 7:
Comparison between measured bandwidth (bandwidthMBPS) and model-
predicted bandwidth (predictedMBPS) across device types.
6.2.2
Accuracy
Additional experiments were conducted at the video-session level.
For instance, when
considering sessions on mobile devices, the model achieves an overall average accuracy of
approximately 96.62% across 45 sessions. Figure 8 presents a set of time-series plots that as-
sess the bandwidth prediction performance across all device types by comparing the actual
bandwidth with the model’s predicted values. Overall, the model demonstrates smoother
and more stable (i.e., more “conﬁdent”) predictions, particularly in longer sessions.
6.3
QoE Results
The proposed MamBRA model is evaluated using MOS values to predict the QoE scores.
These scores are normalized and cumulative scores are then calculated (CDF). Figure 9a
illustrates CDF analysis of QoE scores, comparing two diﬀerent systems: MamBRA and
Pensieve-PPO.
• MOS: A numerical measure of the human-perceived quality.
It typically ranges
from 1 (Bad) to 5 (Excellent).
• QoE: The subjective “satisfaction” of the user.
It is aﬀected by buﬀering, video
clarity, and how long it takes for the video to start.
The mathematical formulas are as follows:
18
```


### Pagina 20
```text
Desktop
TV
Mobile
Tablet
Sessions = 265
Sessions = 71
Sessions = 45
Sessions = 24
Accuracy ≈92.763
Accuracy ≈92.169
Accuracy ≈96.620
Accuracy ≈85.794
Figure 8:
Comparison between measured bandwidth (bandwidthMBPS) and model-
predicted bandwidth (predictedMBPS) across device types.
MOS = 1 + 4 ·
log10 (bps + 1) −log10 (minbps + 1)
log10 (maxbps + 1) −log10 (minbps + 1)
QoE = (MOS −1) · 4
where bps is the predicted network’s bandwidth that MamBRA model calculated.
Figure 9b illustrates and compares the Mean QoE scores across the four diﬀerent device
types tv, desktop, mobile, and tablet. The data suggests that larger-screen devices (desktops
and TVs) generally provide a higher QoE than portable devices (tablets and mobiles) in this
speciﬁc dataset. Several technical factors contribute to the lower scores seen for mobile
devices, such as network volatility, hardware constraints, and mobility factors. Table 3
summarizes the performance of MamBRA and Pensieve-PPO.
19
```


### Pagina 21
```text
(a) CDF-QoE for MamBRA and Pensieve-PPO
(b) Average QoE for each device type
Figure 9: (a) CDF probability versus QoE for MamBRA and Pensieve-PPO, (b) average QoE
for deviceType feature values (desktop, tv, mobile, and tablet)
Table 3: Performance comparison summary between MamBRA and Pensieve-PPO
Model/Metric
Behavior
Performance Summary
Actual Bandwidth
Smooth, steep curve starting
around 0.7.
Excellent. Nearly all sessions achieve a QoE
score above 0.7, with a median around 0.82.
Predicted (MamBRA)
Even further right than the
actual scores.
Optimistic. The model predicts even higher QoE
(median 0.9) than what is actually achieved.
Pensieve-PPO
A ”staircase” step function
spread across the x-axis.
Inconsistent. While it reaches high scores, many
sessions experience low QoE (as low as 0.0–0.4).
7
Conclusion and Future Work
This study developed MamBRA model, a new bitrate adaptation framework for video stream-
ing that employs Mamba for accurate session-level bandwidth prediction. The streaming
dataset are recognized by fully disconnected user sessions and the model implements a su-
pervised time-series learning technique that ensures temporal consistency while explicitly
limiting cross-session information leaking. The conducted test demonstrates that MamBRA
has remarkably reduces prediction errors (Huber and MSE) and improves temporal sta-
bility of predicted bandwidths. A signiﬁcant ﬁnding of this research work is that Mamba’s
linear state-space model allows for eﬃcient and stable computation, which makes it very
appropriate for real-time use.
Additionally, the bandwidth predicted by MamBRA yields
more reliable QoE ratings in comparison to the PPO-based approach used in Pensieve.
According to the ﬁndings of this study, several directions for future research are high-
lighted, as follows:
• Integrating the predictive strengths of MamBRA with end-to-end ABR agent models
20
```


### Pagina 22
```text
that can enhance bitrate selection in real-time.
• Exploring the deployment of MamBRA in edge computing frameworks could further
boost performance in multi-client scenario’s, minimizing latency and improving re-
source allocation fairness.
• Incorporating more sophisticated perceptual video quality metrics into the training
objective may enhance the model’s performance to better match user satisfaction.
• Testing and evaluating the proposed framework using various, modern network traces
(e.g., 5G and Starlink) will guarantee its robustness to the growing of modern internet
traﬃc.
8
Declarations
Funding
The authors received no ﬁnancial support for the research, authorship, and/or
publication of this article.
Author Contributions
The authors’ contributions are as follows:
• Jamal A. Hussein: wrote Section 3, prepared the dataset (Section 4), designed and
implemented the proposed system (Section 5) and conducted the inference experi-
ments and corresponding results (Figures 7 and 8).
• Aree A. Mohammad: computed the QoE metrics based on the results generated from
the system implementation and prepared the ﬁgures presented in Subsections 6.1
and 6.3. Aree initially wrote the Conclusion and Future Work section (Section 7).
• Miran T. Abdullah: prepared the Related Work section (Section 2).
• Aree and Jamal collaborated in preparing the inference results subsection (Subsec-
tion 6.2).
• The Introduction section (Section 1) was jointly written by all authors.
• All authors reviewed and approved the results and conclusions presented in this study,
and approved the ﬁnal version of the manuscript.
References
Sandvine (2023). 2023 Global Internet Phenomena Report. Tech. rep. url: https://
www.sandvine.com/global-internet-phenomena-report-2024.
21
```


### Pagina 23
```text
Abdullah, M. T. A. et al. (2017). “Survey of Transportation of Adaptive Multimedia
Streaming Service in Internet”. In: Network Protocols and Algorithms 9.1–2, pp. 85–
125. doi: 10.5296/npa.v9i1-2.12412.
Microsoft (2008). IIS Smooth Streaming Technical Overview. https://learn.microsoft.
com. Microsoft Developer Network (MSDN).
Stockhammer, Thomas (2011). “Dynamic Adaptive Streaming over HTTP –: Standards
and Design Principles”. In: Proceedings of the second annual ACM conference on Mul-
timedia systems, pp. 133–144. doi: 10.1145/1943552.1943572.
Pantos, Roger and William May (2017). HTTP Live Streaming. RFC 8216. IETF. url:
https://www.rfc-editor.org/rfc/rfc8216.
Apple Inc. (2024). HTTP Live Streaming (HLS). Accessed: Apr. 23, 2025. url: https:
//developer.apple.com/streaming/.
DASH Industry Forum (2024). MPEG-DASH (Dynamic Adaptive Streaming over HTTP).
Accessed: Apr. 23, 2025. url: https://dashif.org/.
Yin, Xiaoqi et al. (2015). “A Control-theoretic Approach for Dynamic Adaptive Video
Streaming over HTTP”. In: Proceedings of the 2015 ACM conference on special interest
group on data communication, pp. 325–338. doi: 10.1145/2785956.2787486.
Huang, Te-Yuan et al. (2014). “A Buﬀer-based Approach to Rate Adaptation: Evidence
from a Large Video Streaming Service”. In: Proceedings of the 2014 ACM conference
on SIGCOMM, pp. 187–198. doi: 10.1145/2619239.2626296.
Spiteri, K., R. Urgaonkar, and R. K. Sitaraman (2020). “BOLA: Near-optimal Bitrate
Adaptation for Online Videos”. In: IEEE/ACM Transactions on Networking 28.4,
pp. 1698–1711. doi: 10.1109/TNET.2020.2996964.
Akhtar, Zahaib et al. (2018). “Oboe: Auto-tuning Video ABR Algorithms to Network
Conditions”. In: Proceedings of the 2018 Conference of the ACM Special Interest Group
on Data Communication, pp. 44–58. doi: 10.1145/3230543.3230558.
Pham, Stefan et al. (2020). “Evaluation of shared resource allocation using SAND for ABR
streaming”. In: ACM Transactions on Multimedia Computing, Communications, and
Applications (TOMM) 16.2s, pp. 1–18. doi: 10.1145/3388926.
Woo, J. et al. (2024). “Improving the Quality of Experience of Video Streaming Through
a Buﬀer-Based Adaptive Bitrate Algorithm and Gated Recurrent Unit-Based Network
Bandwidth Prediction”. In: Appl. Sci. 14.22, p. 10490. doi: 10.3390/app142210490.
Seufert, Michael et al. (2015). “A Survey on Quality of Experience of HTTP Adaptive
Streaming”. In: IEEE Communications Surveys & Tutorials 17.1, pp. 469–492. doi:
10.1109/COMST.2014.2360940.
Timmerer, Christian, Miska Müller, and Stefan Lederer (2017). “Adaptive Streaming of
Multimedia Content: A Survey”. In: IEEE Communications Surveys & Tutorials 19.1,
pp. 1–27. doi: 10.1006/rtim.2001.0224.
Taha, Miran, Aree Ali, et al. (2021). “An Automated Model for the Assessment of QoE of
Adaptive Video Streaming over Wireless Networks”. In: Multimedia Tools and Appli-
cations 80.17, pp. 26833–26854. doi: 10.1007/s11042-021-10934-9.
22
```


### Pagina 24
```text
Taha, Miran, Alejandro Canovas, et al. (2021). “A QoE Adaptive Management System
for High Deﬁnition Video Streaming over Wireless Networks”. In: Telecommunication
Systems 77.1, pp. 63–81. doi: 10.1007/s11235-020-00741-2.
George, S. A. and V. Joseph (2025). “Optimizing QoE of Real-Time Video Using Band-
width Sharing”. In: IEEE Access 13, pp. 50953–50966. doi: 10.1109/ACCESS.2025.
3552944.
Jia, Lianchen et al. (2025). “Towards User-level QoE: Large-scale Practice in Personalized
Optimization of Adaptive Video Streaming”. In: Proceedings of the ACM SIGCOMM
2025 Conference (SIGCOMM ’25). New York, NY, USA: Association for Computing
Machinery, pp. 1154–1166. doi: 10.1145/3718958.3750526.
Tien, Vu Huu and Thao Nguyen Thi Huong (2025). “QoE-Energy Consumption Optimiza-
tion for End-User Devices in Adaptive Bitrate Video Streaming Using the Lagrange
Multiplier Method”. In: EAI Endorsed Transactions on Industrial Networks and Intel-
ligent Systems 12.3. doi: 10.4108/eetinis.v12i3.8587.
Yang, Xiang et al. (Apr. 2024). “PICO: Pipeline Inference Framework for Versatile CNNs on
Diverse Mobile Devices”. In: IEEE Transactions on Mobile Computing 23.4, pp. 2712–
2730. doi: 10.1109/TMC.2023.3265111.
Mao, Hongzi, Ravi Netravali, and Mohammad Alizadeh (2017). “Neural Adaptive Video
Streaming with Pensieve”. In: Proceedings of the ACM Special Interest Group on Data
Communication, pp. 197–210. doi: 10.1145/3098822.3098823.
Gu, Albert and Tri Dao (2024). “Mamba: Linear-Time Sequence Modeling with Selec-
tive State Spaces”. In: First Conference on Language Modeling. url: https : / /
openreview.net/forum?id=tEYskw1VY2.
Patro, Badri Narayana and Vijay Srinivas Agneeswaran (2025). “Mamba-360: Survey of
State Space Models as Transformer Alternative for Long Sequence Modelling: Methods,
Applications, and Challenges”. In: Engineering Applications of Artiﬁcial Intelligence
159, p. 111279. issn: 0952-1976. doi: 10.1016/j.engappai.2025.111279.
Somvanshi, Shriyank et al. (2025). “From S4 to Mamba: A Comprehensive Survey on
Structured State Space Models”. In: arXiv preprint. Survey tracing evolution of SSMs
from S4 through Mamba and related variants. url: https://arxiv.org/abs/
2503.18970.
Zhang, Guozhen et al. (2024). “VFIMamba: Video Frame Interpolation With State Space
Models”. In: Proceedings of the 38th International Conference on Neural Information
Processing Systems (NIPS ’24). Vol. 37. Red Hook, NY, USA: Curran Associates Inc.,
pp. 107225–107248. doi: 10.52202/079017-3405.
Liu, Xiao et al. (2026). “Vision Mamba: A Comprehensive Survey and Taxonomy”. In:
IEEE Transactions on Neural Networks and Learning Systems 37.2, pp. 505–525. doi:
10.1109/TNNLS.2025.3610435.
Zhang, Hanwei et al. (2024). “A Survey on Visual Mamba”. In: Applied Sciences 14.13,
p. 5683. doi: 10.3390/app14135683.
23
```


### Pagina 25
```text
Teixeira, Thiago, Bo Zhang, and Yuriy Reznik (2021). “Adaptive Streaming Playback
Statistics Dataset”. In: Proceedings of the 12th ACM Multimedia Systems Conference,
pp. 248–254. doi: 10.1145/3458305.3478444.
Ran, Dezhi et al. (2020). “Preference-aware Dynamic Bitrate Adaptation for Mobile Short-
form Video Feed Streaming”. In: IEEE Access 8, pp. 220083–220094. doi: 10.1109/
ACCESS.2020.3042619.
Artioli, Emanuele, Farzad Tashtarian, and Christian Timmerer (2024). “DIGITWISE: Dig-
ital Twin-based Modeling of Adaptive Video Streaming Engagement”. In: Proceedings of
the 15th ACM Multimedia Systems Conference, pp. 78–88. doi: 10.1145/3625468.
3647613.
godka (2025). Pensieve-PPO: The simplest implementation of Pensieve via state-of-the-
art RL algorithms (PPO, DQN, SAC). https://github.com/godka/Pensieve-
PPO. GitHub repository (accessed 2026-03-01).
Sengupta, S. et al. (2018). “HotDASH: Hotspot Aware Adaptive Video Streaming Using
Deep Reinforcement Learning”. In: 2018 IEEE 26th International Conference on Net-
work Protocols (ICNP). Cambridge, UK, pp. 165–175. doi: 10.1109/ICNP.2018.
000.
Huang, T. et al. (Oct. 2019). “Comyco: Quality-aware Adaptive Video Streaming via Imi-
tation Learning”. In: Proceedings of the 27th ACM International Conference on Multi-
media, pp. 429–437. doi: 10.1145/3343031.3351014.
Dinaki, H.E. et al. (2021). “Forecasting Video QoE with Deep Learning from Multivariate
Time-series”. In: IEEE Open Journal of Signal Processing 2, pp. 512–521. doi: 10.
1109/OJSP.2021.3099065.
Wei, B. et al. (2022). “QuDASH: Quantum-inspired Rate Adaptation Approach for DASH
Video Streaming”. In: IEEE Access 11, pp. 118462–118473. doi: 10.1109/ACCESS.
2023.3326326.
Xu, Yeting et al. (2023). “FedABR: A Personalized Federated Reinforcement Learning Ap-
proach for Adaptive Video Streaming”. In: 2023 IFIP Networking Conference (IFIP
Networking). IEEE, pp. 1–9. doi: 10 . 23919 / IFIPNetworking57963 . 2023 .
10186404.
Yang, D. et al. (2023). “QoE-Aware Adaptive Bitrate Algorithm Based on Subepisodic
Deep Reinforcement Learning for DASH”. In: Proceedings of the 2023 15th Interna-
tional Conference on Machine Learning and Computing, pp. 103–108. doi: 10.1145/
3587716.3587733.
Darwich, M. and M. Bayoumi (2024). “Video Quality Adaptation Using CNN and RNN
Models for Cost-eﬀective and Scalable Video Streaming Services”. In: Cluster Comput-
ing 27.5, pp. 6355–6375. doi: 10.1007/s10586-024-04315-8.
Kang, J. and K. Chung (2024). “RL-based HTTP Adaptive Streaming with Edge Collabo-
ration in Multi-client Environment”. In: Journal of Network and Computer Applications
223, p. 103833. doi: 10.1016/j.jnca.2024.103833.
24
```


### Pagina 26
```text
Wang, S., J. Lin, and F. Ye (Dec. 2024). “Imitation Learning for Adaptive Video Streaming
with Future Adversarial Information Bottleneck Principle”. In: IEEE Transactions on
Mobile Computing 23.12, pp. 13670–13683. doi: 10.1109/TMC.2024.3437455.
Ling, Y. and Y. Qin (2025). “Learning Robust Adaptive Bitrate Algorithms with Adversar-
ial Inverse Reinforcement Learning”. In: Chinese Journal of Electronics 34.4, pp. 1309–
1320. doi: 10.23919/cje.2024.00.202.
Naseh, D., A. Bozorgchenani, and D. Tarchi (2025). “Deep Reinforcement Learning for
Edge-DASH-based Dynamic Video Streaming”. In: 2025 IEEE Wireless Communica-
tions and Networking Conference (WCNC), pp. 1–6. doi: 10.1109/WCNC61545.
2025.10978132.
Zhang, Jianwei et al. (2025). “Deep reinforcement learning enhanced optimization algo-
rithm for adaptive bitrate video streaming”. In: AIP Advances 15.7, p. 075042. doi:
10.1063/5.0277381.
Vaswani, Ashish et al. (2017). “Attention is All you Need”. In: Advances in Neural Informa-
tion Processing Systems. Vol. 30. Curran Associates, Inc. url: https://proceedings.
neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-
Abstract.html.
Gu, Albert, Karan Goel, and Christopher Ré (2022). “Eﬃciently Modeling Long Sequences
with Structured State Spaces”. In: International Conference on Learning Representa-
tions (ICLR). arXiv: 2111.00396 [cs.LG].
Balachandran, Athula et al. (2013). “Developing a Predictive Model of Quality of Experi-
ence for Internet Video”. In: ACM SIGCOMM Computer Communication Review 43.4,
pp. 339–350. doi: 10.1145/2534169.2486025.
Miller, Konstantin (2016). Adaptation Algorithms for HTTP-based Video Streaming. Tech-
nische Universitaet Berlin (Germany). doi: 10.14279/depositonce-5586.
Allard, Josh, Andrew Roskuski, and Mark Claypool (2020). “Measuring and Modeling the
Impact of Buﬀering and Interrupts on Streaming Video Quality of Experience”. In:
Proceedings of the 18th international conference on advances in mobile computing &
multimedia, pp. 153–160. doi: 10.1145/3428690.3429173.
Almquist, Mathias et al. (2018). “The Prefetch Aggressiveness Tradeoﬀin 360 Video
Streaming”. In: Proceedings of the 9th ACM Multimedia Systems Conference, pp. 258–
269. doi: 10.1145/3204949.3204970.
Xie, Yuhong et al. (2024). “Short Video Preloading via Domain Knowledge Assisted Deep
Reinforcement Learning”. In: Digital Communications and Networks 10.6, pp. 1826–
1836. doi: 10.1016/j.dcan.2024.01.006.
25
```
