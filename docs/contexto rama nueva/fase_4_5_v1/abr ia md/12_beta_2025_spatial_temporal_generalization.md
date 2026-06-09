# BETA: A Novel Spatial-Temporal Learning Method for Enhancing Generalization in Adaptive Video Streaming
**Archivo PDF:** `BETA.pdf`  **Identificador:** `12_beta_2025_spatial_temporal_generalization`  **Páginas:** 15  **SHA256 PDF:** `ccf4060b9f49eafde283bdbf1969736f91d079c9c00cc2c3095886a8984b6c7c`  **Foco para Fase 4-5 v1:** ABR under-generalization; detector for poor-performing network conditions; specialized ABR models; multi-step temporal learning.
> Documento Codex-ready generado para diseño de nuevos modelos/controllers IA ABR. No es una source card corta. Contiene extracción técnica cruda y organizada. El PDF original sigue siendo la fuente de verdad para fórmulas, tablas y figuras si la extracción textual pierde layout.
## 1. Cómo usar este `.md`
- Leer primero secciones 2-5 para ubicar método, señales, datos, evaluación y limitaciones.
- Usar la extracción por categorías como material de diseño/contrato/Codex.
- Para ecuaciones, tablas o figuras críticas, comprobar la página indicada en el PDF original.
- No convertir resultados del paper en promesas directas para DashClientModular4; deben transformarse en hipótesis, guardrails y tests Phase 6.
## 2. Metadatos extraídos
- **format:** PDF 1.4
- **title:** A Novel Spatial-Temporal Learning Method for Enhancing Generalization in Adaptive Video Streaming
- **subject:** IEEE Transactions on Mobile Computing;2025;24;12;10.1109/TMC.2025.3588135
- **creator:** LaTeX with hyperref package
- **producer:** Acrobat Distiller 11.0 (Windows); modified using iText® Core 7.2.4 (AGPL version) ©2000-2022 iText Group NV
- **creationDate:** D:20251024124055+05'30'
- **modDate:** D:20251104172415-05'00'

## 3. Índice de secciones detectadas
- p.1: Abstract—Adaptive video streaming has become a fundamental
- p.1: I. INTRODUCTION
- p.2: II. ABR UNDER-GENERALIZATION
- p.3: TABLE I
- p.3: COMPARISON OF QOE AND STREAMING PERFORMANCE OVER SIX DRL-BASED
- p.3: ABR ALGORITHMS
- p.3: Results Analysis: Table I summarizes the performance of the
- p.4: TABLE II
- p.4: THE PROPORTION OF UNDERPERFORMED STREAMING SESSIONS
- p.4: III. METHODOLOGY
- p.8: IV. PERFORMANCE EVALUATION
- p.8: TABLE III
- p.8: BETA PARAMETERS
- p.8: TABLE IV
- p.8: COMPARISON OF QOE ACROSS SEVEN ABR ALGORITHMS
- p.10: TABLE V
- p.10: COMPARISON OF QOE ACROSS SEVEN DRL METHODS
- p.12: TABLE VI
- p.12: TEMPORAL SENSITIVITY OF THE QOE THRESHOLD
- p.12: TABLE VII
- p.12: SPATIAL SENSITIVITY OF THE QOE THRESHOLD
- p.12: TABLE VIII
- p.12: Q VALUE ESTIMATION METHODS
- p.12: TABLE IX
- p.12: TRAINING UPDATE FREQUENCY
- p.12: TABLE X
- p.12: ACTION NOISE INTRODUCTION
- p.12: TABLE XI
- p.12: ONLINE COMPLEXITY ANALYSIS
- p.13: V. RELATED WORK
- p.13: Discussion: The key limitation of the existing ABR algo-
- p.13: VI. CONCLUSION AND FUTURE WORK
- p.14: ACKNOWLEDGMENT
- p.14: REFERENCES

## 4. Índice de páginas con palabras clave
- p.1: state, action, QoE, buffer, throughput, download, trace, training, PPO, generalization, quality, network condition
- p.2: state, action, reward, QoE, rebuffer, buffer, throughput, bandwidth, download, dataset, trace, training, PPO, A3C, DQN, generalization, quality, network condition
- p.3: action, QoE, rebuffer, buffer, throughput, download, dataset, trace, training, PPO, imitation, quality, visual, network condition
- p.4: state, QoE, download, trace, training, generalization, sensitivity, network condition
- p.5: state, action, reward, QoE, buffer, throughput, download, trace, training, generalization, network condition
- p.6: state, action, QoE, buffer, throughput, download, dataset, trace, training, generalization, network condition
- p.7: state, action, reward, QoE, buffer, throughput, download, trace, training, quality
- p.8: state, action, QoE, download, trace, training, baseline, MPC, Pensieve, generalization, quality, sensitivity
- p.9: action, QoE, rebuffer, buffer, throughput, bandwidth, download, dataset, trace, baseline, MPC, generalization, quality, network condition
- p.10: QoE, rebuffer, buffer, throughput, download, dataset, trace, training, generalization, quality, network condition
- p.11: action, reward, QoE, rebuffer, buffer, download, trace, training, baseline, generalization, sensitivity, network condition
- p.12: action, QoE, buffer, bandwidth, download, training, generalization, sensitivity
- p.13: state, action, QoE, buffer, throughput, bandwidth, download, training, MPC, BOLA, Pensieve, PPO, A3C, DQN, imitation, expert, generalization, quality, network condition
- p.14: QoE, buffer, download, trace, BOLA, Pensieve, PPO, DQN, expert, generalization, quality, visual, network condition
- p.15: state, action, download, visual

## 5. Extracción técnica cruda por categorías

### 5.x Modelo / arquitectura / algoritmo

**[Modelo / arquitectura / algoritmo | extracto 1 | p.1]**

12852 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025 A Novel Spatial-Temporal Learning Method for Enhancing Generalization in Adaptive Video Streaming Guanghui Zhang , Ziming Wang , Huaren Wei, Mengbai Xiao , Hui Yuan , Senior Member, IEEE, Dongxiao Yu , Senior Member, IEEE, and Xiuzhen Cheng , Fellow, IEEE Abstract—Adaptive video streaming has become a fundamental technology for video delivery. With the rise of deep reinforcement learning (DRL), streaming vendors are increasingly adopting DRL- driven adaptive bitrate (ABR) algorithms. In real-world deploy- ments, most ABR approaches are developed with the aim of main- taining good performance across a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditi

**[Modelo / arquitectura / algoritmo | extracto 2 | p.1]**

adaptive bitrate (ABR) algorithms. In real-world deploy- ments, most ABR approaches are developed with the aim of main- taining good performance across a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yielding average QoE gains of 19.4% to 50.9%,andachievingimprovementsofupto244.1%underseverely fluctuating network conditions. Index Terms—Video streaming, mobile network, deep reinforcement learning, quality-of-experience. I. INTRODUCTION I N RECENT years, video streaming has witnessed rapid expansion, emerging as one of the primary applications of the Received 9 December 2024; revised 26 June 2025; accepted 3 July 2025. Date of publication 15 July 2025; date of current version 5 November 2025. This work was supported by the Nati

**[Modelo / arquitectura / algoritmo | extracto 3 | p.1]**

Fellow, IEEE Abstract—Adaptive video streaming has become a fundamental technology for video delivery. With the rise of deep reinforcement learning (DRL), streaming vendors are increasingly adopting DRL- driven adaptive bitrate (ABR) algorithms. In real-world deploy- ments, most ABR approaches are developed with the aim of main- taining good performance across a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yielding average QoE gains of 19.4% to 50.9%,andachievingimprovementsofupto244.1%underseverely fluctuating network conditions. Index Terms—Video streaming, mobile network, deep reinforcement learning, quality-of-experience. I. INTRODUCTION I N RECENT years, video streaming has witnessed rapid expansion, emerging as one of the pr

**[Modelo / arquitectura / algoritmo | extracto 4 | p.1]**

Enhancing Generalization in Adaptive Video Streaming Guanghui Zhang , Ziming Wang , Huaren Wei, Mengbai Xiao , Hui Yuan , Senior Member, IEEE, Dongxiao Yu , Senior Member, IEEE, and Xiuzhen Cheng , Fellow, IEEE Abstract—Adaptive video streaming has become a fundamental technology for video delivery. With the rise of deep reinforcement learning (DRL), streaming vendors are increasingly adopting DRL- driven adaptive bitrate (ABR) algorithms. In real-world deploy- ments, most ABR approaches are developed with the aim of main- taining good performance across a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yielding average QoE gains of 19.4% to 50.9%,andachievingimprovementsofupto244.1%underseverely fluctuating network conditions. Ind

**[Modelo / arquitectura / algoritmo | extracto 5 | p.1]**

ons vary widely [3], [4], [5], [6], [11]. This phenomenon, i.e., the operational range of an ABR algorithm is narrow, leads to a marked decrease in the overall performance. We defined this problem as “ABR Under-Generalization”. The existing ABR algorithms can be generally divided into two major categories: heuristic-based and learning-based. The former [5], [6], [7], [8], [9], [19], [20], [21] rely on pre-programmed ABR model with fixed control rules, which inherently limits their adaptability to generalize the varying network environments. Consequently, the heuristic-based algorithms have gradually lost favor in recent years. In contrast, the learning-based algorithms, particularly those powered by deepreinforcementlearning(DRL)[3],[4],[10],[11],[18],[22], [23], [24], [25], [26], [27], [28], [29], [30], have gained attention. They train neural networks using real network trace data, resulting in ABR models that are more flexible than the heuristic counterparts [10]. 1536-1233 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

**[Modelo / arquitectura / algoritmo | extracto 6 | p.1]**

ACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025 A Novel Spatial-Temporal Learning Method for Enhancing Generalization in Adaptive Video Streaming Guanghui Zhang , Ziming Wang , Huaren Wei, Mengbai Xiao , Hui Yuan , Senior Member, IEEE, Dongxiao Yu , Senior Member, IEEE, and Xiuzhen Cheng , Fellow, IEEE Abstract—Adaptive video streaming has become a fundamental technology for video delivery. With the rise of deep reinforcement learning (DRL), streaming vendors are increasingly adopting DRL- driven adaptive bitrate (ABR) algorithms. In real-world deploy- ments, most ABR approaches are developed with the aim of main- taining good performance across a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yielding average QoE

**[Modelo / arquitectura / algoritmo | extracto 7 | p.1]**

the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yielding average QoE gains of 19.4% to 50.9%,andachievingimprovementsofupto244.1%underseverely fluctuating network conditions. Index Terms—Video streaming, mobile network, deep reinforcement learning, quality-of-experience. I. INTRODUCTION I N RECENT years, video streaming has witnessed rapid expansion, emerging as one of the primary applications of the Received 9 December 2024; revised 26 June 2025; accepted 3 July 2025. Date of publication 15 July 2025; date of current version 5 November 2025. This work was supported by the National Natural Science Foundation of China under Grant 62302268, in part by the Natural Science Foundation of Shandong Province under Grant 2023HWYQ-045 and Grant ZR2023QF060, in part by Qingdao Natural Science Foundation under Grant 23-2-1-127-zyyd-jch, and in part by the Taishan Scholar Project of Shandong Province under Grant tsqn202312051. An earlier version of this paper was presented in part at the IEEE International Conference on Sensing, Communication, and Networking [10.1109/SPCOM50965.2020.9

**[Modelo / arquitectura / algoritmo | extracto 8 | p.1]**

ome a fundamental technology for video delivery. With the rise of deep reinforcement learning (DRL), streaming vendors are increasingly adopting DRL- driven adaptive bitrate (ABR) algorithms. In real-world deploy- ments, most ABR approaches are developed with the aim of main- taining good performance across a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yielding average QoE gains of 19.4% to 50.9%,andachievingimprovementsofupto244.1%underseverely fluctuating network conditions. Index Terms—Video streaming, mobile network, deep reinforcement learning, quality-of-experience. I. INTRODUCTION I N RECENT years, video streaming has witnessed rapid expansion, emerging as one of the primary applications of the Received 9 December 2024; r

**[Modelo / arquitectura / algoritmo | extracto 9 | p.1]**

th the rise of deep reinforcement learning (DRL), streaming vendors are increasingly adopting DRL- driven adaptive bitrate (ABR) algorithms. In real-world deploy- ments, most ABR approaches are developed with the aim of main- taining good performance across a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yielding average QoE gains of 19.4% to 50.9%,andachievingimprovementsofupto244.1%underseverely fluctuating network conditions. Index Terms—Video streaming, mobile network, deep reinforcement learning, quality-of-experience. I. INTRODUCTION I N RECENT years, video streaming has witnessed rapid expansion, emerging as one of the primary applications of the Received 9 December 2024; revised 26 June 2025; accepted 3 July 2025. Date of

**[Modelo / arquitectura / algoritmo | extracto 10 | p.2]**

ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING 12853 However, our measurement study (refer to Section II) reveals that when faced with a wide range of network conditions, even extensively trained DRL-based ABR algorithms can only achieve 43.1% ∼48.9% of the maximum possible QoE, far below the offline optimal 100%. This highlights the problem of ABR Under-Generalization, which contradicts the theoretical expectation that training on large-scale real traces should yield generalizable ABR policies. The root cause appears to lie in the direct application of the generic DRL techniques [12], [13], [14], [15], [16], [17], which fail to capture all the key features required to adapt across different environments. Motivated by this challenge, we proposed BETA, a new DRL-based ABR framework specifically designed to enhance the generalization of video streaming. BETA consists of two core modules: spatial and temporal, which jointly tackle the above-mentioned challenge: Spatial Module: Our measurement study (Section II) shows that none of the ABR algorithms trained

**[Modelo / arquitectura / algoritmo | extracto 11 | p.2]**

otivated by this challenge, we proposed BETA, a new DRL-based ABR framework specifically designed to enhance the generalization of video streaming. BETA consists of two core modules: spatial and temporal, which jointly tackle the above-mentioned challenge: Spatial Module: Our measurement study (Section II) shows that none of the ABR algorithms trained using the conventional DRL approaches [12], [13], [14], [15], [16], [17] consistently maintain high performance across all network conditions. In particular, all the measured algorithms fail in 8.1% to 17.1% of the evaluated traces, significantly degrading the overall results. Additionally, the specific traces where underperformance occurs differ greatly depending on the specific DRL method adopted. To address this issue, BETA incorporates a spatial module. It begins by training a basic ABR model and benchmarks its QoE against the offline optimal performance per streaming ses- sion. This process helps identify the underperforming network conditions, from which the corresponding network features are extracted, and then are used to predict the potential network conditions that might cause poor performance in the future. BETA proceeds to train specialized ABR models specifically tailored to these challenging network conditions. Temporal Module: We observed that the existing DRL- trained ABR algorithms are often short-sighted, focusing only on single-step future planning. This is due to their training approach, where each epoch updates the model based solely on the immediate reward of short-term feedback. This is ill- suited for the video streaming contexts that require consecutive decision-making across all the video segments in eac

**[Modelo / arquitectura / algoritmo | extracto 12 | p.2]**

32] to support reproducibility and future research (Section III). Comprehensive Evaluation: Through extensive evaluations, we show that BETA significantly outperforms the state-of-the- art ABR algorithms. In addition, we investigated the underlying reasons for its effectiveness (Section IV). II. ABR UNDER-GENERALIZATION Existing learning-based ABR algorithms [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30] (will be comprehensively reviewed in Section V) predominantly rely on advanced DRL techniques [12], [13], [14], [15], [16], [17] for policy training. To demonstrate the ABR Under-Generalization problem, we conducted a measurement study evaluating the ABRalgorithms trainedusingsixwidelyadoptedDRLmethods: A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17]. DRL Configuration. The neural network architecture adheres to the established designs from prior literature [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30]. Specifi- cally,themodelinputcomprisesfivecategoriesofenvironmental states: (i) the measured throughput of the past 8 segments, (ii) the download durations of the past 8 segments, (iii) the bitrate of the most recently downloaded segment, (iv) the current buffer occupancy, and (v) the number of remaining segments in the current streaming session. The first two inputs are processed via convolutional neural networks (CNNs) with 128 filters, while the remaining three are fed into fully connected (dense) layers with 128 neurons. Then the outputs are subsequently merged through a dense aggregation layer comprising 256 neurons. The output layer offers the discrete bitrate level, which serves as the decision

**[Modelo / arquitectura / algoritmo | extracto 13 | p.2]**

demonstrates the effectiveness of BETA. Compared to state-of- the-art ABR algorithms, BETA improves average QoE by 19.4% to 50.9%, with gains reaching 244.1% in highly variable network conditions. For the internal QoE metrics, BETA achieves a 7.9% increase in video quality and a 98.3% reduction in rebuffering events. These benefits are attributed to BETA’s flexible bitrate decisions, which not only better match the network dynamics but also fully utilize available network resources. In summary, our contributions are three-fold: Large-Scale Measurement Study: We systematically evalu- ated ABR algorithms trained by six well-known DRL methods, A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17], clearly revealing the impact of the ABR Under- Generalization problem (Section II). Design of BETA: We presented BETA, a DRL-based ABR framework integrating spatial and temporal modules to enhance generalization. The implementation of BETA has been open- sourced on GitHub [32] to support reproducibility and future research (Section III). Comprehensive Evaluation: Through extensive evaluations, we show that BETA significantly outperforms the state-of-the- art ABR algorithms. In addition, we investigated the underlying reasons for its effectiveness (Section IV). II. ABR UNDER-GENERALIZATION Existing learning-based ABR algorithms [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30] (will be comprehensively reviewed in Section V) predominantly rely on advanced DRL techniques [12], [13], [14], [15], [16], [17] for policy training. To demonstrate the ABR Under-Generalization problem, we conducted a measurement study evaluating the ABRalgorithms trainedusings

**[Modelo / arquitectura / algoritmo | extracto 14 | p.2]**

clearly revealing the impact of the ABR Under- Generalization problem (Section II). Design of BETA: We presented BETA, a DRL-based ABR framework integrating spatial and temporal modules to enhance generalization. The implementation of BETA has been open- sourced on GitHub [32] to support reproducibility and future research (Section III). Comprehensive Evaluation: Through extensive evaluations, we show that BETA significantly outperforms the state-of-the- art ABR algorithms. In addition, we investigated the underlying reasons for its effectiveness (Section IV). II. ABR UNDER-GENERALIZATION Existing learning-based ABR algorithms [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30] (will be comprehensively reviewed in Section V) predominantly rely on advanced DRL techniques [12], [13], [14], [15], [16], [17] for policy training. To demonstrate the ABR Under-Generalization problem, we conducted a measurement study evaluating the ABRalgorithms trainedusingsixwidelyadoptedDRLmethods: A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17]. DRL Configuration. The neural network architecture adheres to the established designs from prior literature [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30]. Specifi- cally,themodelinputcomprisesfivecategoriesofenvironmental states: (i) the measured throughput of the past 8 segments, (ii) the download durations of the past 8 segments, (iii) the bitrate of the most recently downloaded segment, (iv) the current buffer occupancy, and (v) the number of remaining segments in the current streaming session. The first two inputs are processed via convolutional neural networks (CNNs) with

**[Modelo / arquitectura / algoritmo | extracto 15 | p.2]**

of ABR Under-Generalization, which contradicts the theoretical expectation that training on large-scale real traces should yield generalizable ABR policies. The root cause appears to lie in the direct application of the generic DRL techniques [12], [13], [14], [15], [16], [17], which fail to capture all the key features required to adapt across different environments. Motivated by this challenge, we proposed BETA, a new DRL-based ABR framework specifically designed to enhance the generalization of video streaming. BETA consists of two core modules: spatial and temporal, which jointly tackle the above-mentioned challenge: Spatial Module: Our measurement study (Section II) shows that none of the ABR algorithms trained using the conventional DRL approaches [12], [13], [14], [15], [16], [17] consistently maintain high performance across all network conditions. In particular, all the measured algorithms fail in 8.1% to 17.1% of the evaluated traces, significantly degrading the overall results. Additionally, the specific traces where underperformance occurs differ greatly depending on the specific DRL method adopted. To address this issue, BETA incorporates a spatial module. It begins by training a basic ABR model and benchmarks its QoE against the offline optimal performance per streaming ses- sion. This process helps identify the underperforming network conditions, from which the corresponding network features are extracted, and then are used to predict the potential network conditions that might cause poor performance in the future. BETA proceeds to train specialized ABR models specifically tailored to these challenging network conditions. Temporal Module: We observed that the exi

**[Modelo / arquitectura / algoritmo | extracto 16 | p.2]**

ced on GitHub [32] to support reproducibility and future research (Section III). Comprehensive Evaluation: Through extensive evaluations, we show that BETA significantly outperforms the state-of-the- art ABR algorithms. In addition, we investigated the underlying reasons for its effectiveness (Section IV). II. ABR UNDER-GENERALIZATION Existing learning-based ABR algorithms [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30] (will be comprehensively reviewed in Section V) predominantly rely on advanced DRL techniques [12], [13], [14], [15], [16], [17] for policy training. To demonstrate the ABR Under-Generalization problem, we conducted a measurement study evaluating the ABRalgorithms trainedusingsixwidelyadoptedDRLmethods: A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17]. DRL Configuration. The neural network architecture adheres to the established designs from prior literature [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30]. Specifi- cally,themodelinputcomprisesfivecategoriesofenvironmental states: (i) the measured throughput of the past 8 segments, (ii) the download durations of the past 8 segments, (iii) the bitrate of the most recently downloaded segment, (iv) the current buffer occupancy, and (v) the number of remaining segments in the current streaming session. The first two inputs are processed via convolutional neural networks (CNNs) with 128 filters, while the remaining three are fed into fully connected (dense) layers with 128 neurons. Then the outputs are subsequently merged through a dense aggregation layer comprising 256 neurons. The output layer offers the discrete bitrate level, which se

### 5.x Estado / inputs / features

**[Estado / inputs / features | extracto 1 | p.1]**

d on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yielding average QoE gains of 19.4% to 50.9%,andachievingimprovementsofupto244.1%underseverely fluctuating network conditions. Index Terms—Video streaming, mobile network, deep reinforcement learning, quality-of-experience. I. INTRODUCTION I N RECENT years, video streaming has witnessed rapid expansion, emerging as one of the primary applications of the Received 9 December 2024; revised 26 June 2025; accepted 3 July 2025. Date of publication 15 July 2025; date of current version 5 November 2025. This work was supported by the National Natural Science Foundation of China under Grant 62302268, in part by the Natural Science Foundation of Shandong Province under Grant 2023HWYQ-045 and Grant ZR2023QF060, in part by Qingdao Natural Science Foundation under Grant 23-2-1-127-zyyd-jch, and in part by the Taishan Schol

**[Estado / inputs / features | extracto 2 | p.1]**

elivery. With the rise of deep reinforcement learning (DRL), streaming vendors are increasingly adopting DRL- driven adaptive bitrate (ABR) algorithms. In real-world deploy- ments, most ABR approaches are developed with the aim of main- taining good performance across a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yielding average QoE gains of 19.4% to 50.9%,andachievingimprovementsofupto244.1%underseverely fluctuating network conditions. Index Terms—Video streaming, mobile network, deep reinforcement learning, quality-of-experience. I. INTRODUCTION I N RECENT years, video streaming has witnessed rapid expansion, emerging as one of the primary applications of the Received 9 December 2024; revised 26 June 2025; accepted 3 July 20

**[Estado / inputs / features | extracto 3 | p.1]**

15 over the past five years and now accounts for over 80% of the Internet traffic [1]. However, the highly variable nature of the mobile networks (primarily caused by unstable radio signals) poses a major obstacle to video streaming. Smooth playback relies on stable and consistent network throughput, which is difficult to main- tain in such dynamic environments. To tackle this issue, the streaming vendors have turned their attention to adaptive bitrate (ABR) algorithms, aiming to alleviate the negative effects of the throughput fluctuations. These ABR algorithms are typically im- plemented under the DASH protocol [2]. Their key component is an adaptive logic, which intelligently adjusts video quality in real time (by selecting appropriate bitrates) based on several streaming metrics such as historical throughput measurements and current buffer status. The objective is to enhance the viewer’s Quality of Experience (QoE). Most ABR algorithms are developed with the intention to perform reliably across the wide network environments of any size and shape, e.g., from 3G networks with peak band- widths of a few Mbps to 5G networks offering mean band- widths of 100+ Mbps. However, real-world experiments con- sistently demonstrate that the existing ABR algorithms, while effective under intended network conditions, suffer significant degradation when the network conditions vary widely [3], [4], [5], [6], [11]. This phenomenon, i.e., the operational range of an ABR algorithm is narrow, leads to a marked decrease in the overall performance. We defined this problem as “ABR Under-Generalization”. The existing ABR algorithms can be generally divided into two major categories: heuristic-based

**[Estado / inputs / features | extracto 4 | p.1]**

engbai Xiao, Dongxiao Yu, and Xiuzhen Cheng are with the School of Computer Science and Technol- ogy, Shandong University, Qingdao 266237, China (e-mail: gh.zhang@sdu. edu.cn; 202235192@mail.sdu.edu.cn; 202315182@mail.sdu.edu.cn; xiaomb@ sdu.edu.cn; dxyu@sdu.edu; xzcheng@sdu.edu.cn). Hui Yuan is with the School of Control Science and Engineering, Shandong University, Jinan 250061, China (e-mail: huiyuan@sdu.edu.cn). Digital Object Identifier 10.1109/TMC.2025.3588135 Internet. As reported by Cisco, global video streaming traffic has surged by a factor of 15 over the past five years and now accounts for over 80% of the Internet traffic [1]. However, the highly variable nature of the mobile networks (primarily caused by unstable radio signals) poses a major obstacle to video streaming. Smooth playback relies on stable and consistent network throughput, which is difficult to main- tain in such dynamic environments. To tackle this issue, the streaming vendors have turned their attention to adaptive bitrate (ABR) algorithms, aiming to alleviate the negative effects of the throughput fluctuations. These ABR algorithms are typically im- plemented under the DASH protocol [2]. Their key component is an adaptive logic, which intelligently adjusts video quality in real time (by selecting appropriate bitrates) based on several streaming metrics such as historical throughput measurements and current buffer status. The objective is to enhance the viewer’s Quality of Experience (QoE). Most ABR algorithms are developed with the intention to perform reliably across the wide network environments of any size and shape, e.g., from 3G networks with peak band- widths of a few Mbps to 5G networks offering

**[Estado / inputs / features | extracto 5 | p.1]**

ize the varying network environments. Consequently, the heuristic-based algorithms have gradually lost favor in recent years. In contrast, the learning-based algorithms, particularly those powered by deepreinforcementlearning(DRL)[3],[4],[10],[11],[18],[22], [23], [24], [25], [26], [27], [28], [29], [30], have gained attention. They train neural networks using real network trace data, resulting in ABR models that are more flexible than the heuristic counterparts [10]. 1536-1233 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

**[Estado / inputs / features | extracto 6 | p.1]**

lier version of this paper was presented in part at the IEEE International Conference on Sensing, Communication, and Networking [10.1109/SPCOM50965.2020.9179507]. Recommended for acceptance by S. Wang. (Corresponding author: Hui Yuan.) Guanghui Zhang, Ziming Wang, Huaren Wei, Mengbai Xiao, Dongxiao Yu, and Xiuzhen Cheng are with the School of Computer Science and Technol- ogy, Shandong University, Qingdao 266237, China (e-mail: gh.zhang@sdu. edu.cn; 202235192@mail.sdu.edu.cn; 202315182@mail.sdu.edu.cn; xiaomb@ sdu.edu.cn; dxyu@sdu.edu; xzcheng@sdu.edu.cn). Hui Yuan is with the School of Control Science and Engineering, Shandong University, Jinan 250061, China (e-mail: huiyuan@sdu.edu.cn). Digital Object Identifier 10.1109/TMC.2025.3588135 Internet. As reported by Cisco, global video streaming traffic has surged by a factor of 15 over the past five years and now accounts for over 80% of the Internet traffic [1]. However, the highly variable nature of the mobile networks (primarily caused by unstable radio signals) poses a major obstacle to video streaming. Smooth playback relies on stable and consistent network throughput, which is difficult to main- tain in such dynamic environments. To tackle this issue, the streaming vendors have turned their attention to adaptive bitrate (ABR) algorithms, aiming to alleviate the negative effects of the throughput fluctuations. These ABR algorithms are typically im- plemented under the DASH protocol [2]. Their key component is an adaptive logic, which intelligently adjusts video quality in real time (by selecting appropriate bitrates) based on several streaming metrics such as historical throughput measurements and current buffer status. Th

**[Estado / inputs / features | extracto 7 | p.1]**

Enhancing Generalization in Adaptive Video Streaming Guanghui Zhang , Ziming Wang , Huaren Wei, Mengbai Xiao , Hui Yuan , Senior Member, IEEE, Dongxiao Yu , Senior Member, IEEE, and Xiuzhen Cheng , Fellow, IEEE Abstract—Adaptive video streaming has become a fundamental technology for video delivery. With the rise of deep reinforcement learning (DRL), streaming vendors are increasingly adopting DRL- driven adaptive bitrate (ABR) algorithms. In real-world deploy- ments, most ABR approaches are developed with the aim of main- taining good performance across a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yielding average QoE gains of 19.4% to 50.9%,andachievingimprovementsofupto244.1%underseverely fluctuating network conditions. Index Terms—V

**[Estado / inputs / features | extracto 8 | p.2]**

ch the corresponding network features are extracted, and then are used to predict the potential network conditions that might cause poor performance in the future. BETA proceeds to train specialized ABR models specifically tailored to these challenging network conditions. Temporal Module: We observed that the existing DRL- trained ABR algorithms are often short-sighted, focusing only on single-step future planning. This is due to their training approach, where each epoch updates the model based solely on the immediate reward of short-term feedback. This is ill- suited for the video streaming contexts that require consecutive decision-making across all the video segments in each streaming session. BETA addresses this issue with a temporal module. BETA samples multi-segment decision sequences during training, each consisting of a series of state-action-reward tuples. For each sequence, a discounted actual reward encompassing all the seg- ments is calculated, along with an expected reward based on the initial and final states of each sequence. Both of the rewards are then used to update the neuron weights by minimizing the gap between them. This approach enables the trained ABR model to make far-sighted decisions, thereby ensuring more stable QoE. Extensive evaluation using large-scale network trace datasets demonstrates the effectiveness of BETA. Compared to state-of- the-art ABR algorithms, BETA improves average QoE by 19.4% to 50.9%, with gains reaching 244.1% in highly variable network conditions. For the internal QoE metrics, BETA achieves a 7.9% increase in video quality and a 98.3% reduction in rebuffering events. These benefits are attributed to BETA’s flexible bitrate de

**[Estado / inputs / features | extracto 9 | p.2]**

e-of-the- art ABR algorithms. In addition, we investigated the underlying reasons for its effectiveness (Section IV). II. ABR UNDER-GENERALIZATION Existing learning-based ABR algorithms [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30] (will be comprehensively reviewed in Section V) predominantly rely on advanced DRL techniques [12], [13], [14], [15], [16], [17] for policy training. To demonstrate the ABR Under-Generalization problem, we conducted a measurement study evaluating the ABRalgorithms trainedusingsixwidelyadoptedDRLmethods: A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17]. DRL Configuration. The neural network architecture adheres to the established designs from prior literature [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30]. Specifi- cally,themodelinputcomprisesfivecategoriesofenvironmental states: (i) the measured throughput of the past 8 segments, (ii) the download durations of the past 8 segments, (iii) the bitrate of the most recently downloaded segment, (iv) the current buffer occupancy, and (v) the number of remaining segments in the current streaming session. The first two inputs are processed via convolutional neural networks (CNNs) with 128 filters, while the remaining three are fed into fully connected (dense) layers with 128 neurons. Then the outputs are subsequently merged through a dense aggregation layer comprising 256 neurons. The output layer offers the discrete bitrate level, which serves as the decision action. All the six DRL methods are trained using the Adam optimizer, with training hyperparameters (e.g., learning rate, batch size, experience replay buffer) individu

**[Estado / inputs / features | extracto 10 | p.2]**

ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING 12853 However, our measurement study (refer to Section II) reveals that when faced with a wide range of network conditions, even extensively trained DRL-based ABR algorithms can only achieve 43.1% ∼48.9% of the maximum possible QoE, far below the offline optimal 100%. This highlights the problem of ABR Under-Generalization, which contradicts the theoretical expectation that training on large-scale real traces should yield generalizable ABR policies. The root cause appears to lie in the direct application of the generic DRL techniques [12], [13], [14], [15], [16], [17], which fail to capture all the key features required to adapt across different environments. Motivated by this challenge, we proposed BETA, a new DRL-based ABR framework specifically designed to enhance the generalization of video streaming. BETA consists of two core modules: spatial and temporal, which jointly tackle the above-mentioned challenge: Spatial Module: Our measurement study (Section II) shows that none of the ABR algorithms trained using the conventional DRL approaches [12], [13], [14], [15], [16], [17] consistently maintain high performance across all network conditions. In particular, all the measured algorithms fail in 8.1% to 17.1% of the evaluated traces, significantly degrading the overall results. Additionally, the specific traces where underperformance occurs differ greatly depending on the specific DRL method adopted. To address this issue, BETA incorporates

**[Estado / inputs / features | extracto 11 | p.2]**

ment decision sequences during training, each consisting of a series of state-action-reward tuples. For each sequence, a discounted actual reward encompassing all the seg- ments is calculated, along with an expected reward based on the initial and final states of each sequence. Both of the rewards are then used to update the neuron weights by minimizing the gap between them. This approach enables the trained ABR model to make far-sighted decisions, thereby ensuring more stable QoE. Extensive evaluation using large-scale network trace datasets demonstrates the effectiveness of BETA. Compared to state-of- the-art ABR algorithms, BETA improves average QoE by 19.4% to 50.9%, with gains reaching 244.1% in highly variable network conditions. For the internal QoE metrics, BETA achieves a 7.9% increase in video quality and a 98.3% reduction in rebuffering events. These benefits are attributed to BETA’s flexible bitrate decisions, which not only better match the network dynamics but also fully utilize available network resources. In summary, our contributions are three-fold: Large-Scale Measurement Study: We systematically evalu- ated ABR algorithms trained by six well-known DRL methods, A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17], clearly revealing the impact of the ABR Under- Generalization problem (Section II). Design of BETA: We presented BETA, a DRL-based ABR framework integrating spatial and temporal modules to enhance generalization. The implementation of BETA has been open- sourced on GitHub [32] to support reproducibility and future research (Section III). Comprehensive Evaluation: Through extensive evaluations, we show that BETA significantly outperforms th

**[Estado / inputs / features | extracto 12 | p.2]**

ying reasons for its effectiveness (Section IV). II. ABR UNDER-GENERALIZATION Existing learning-based ABR algorithms [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30] (will be comprehensively reviewed in Section V) predominantly rely on advanced DRL techniques [12], [13], [14], [15], [16], [17] for policy training. To demonstrate the ABR Under-Generalization problem, we conducted a measurement study evaluating the ABRalgorithms trainedusingsixwidelyadoptedDRLmethods: A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17]. DRL Configuration. The neural network architecture adheres to the established designs from prior literature [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30]. Specifi- cally,themodelinputcomprisesfivecategoriesofenvironmental states: (i) the measured throughput of the past 8 segments, (ii) the download durations of the past 8 segments, (iii) the bitrate of the most recently downloaded segment, (iv) the current buffer occupancy, and (v) the number of remaining segments in the current streaming session. The first two inputs are processed via convolutional neural networks (CNNs) with 128 filters, while the remaining three are fed into fully connected (dense) layers with 128 neurons. Then the outputs are subsequently merged through a dense aggregation layer comprising 256 neurons. The output layer offers the discrete bitrate level, which serves as the decision action. All the six DRL methods are trained using the Adam optimizer, with training hyperparameters (e.g., learning rate, batch size, experience replay buffer) individually tuned. Streaming Environment: To emulate the realistic streaming envi

**[Estado / inputs / features | extracto 13 | p.2]**

. The output layer offers the discrete bitrate level, which serves as the decision action. All the six DRL methods are trained using the Adam optimizer, with training hyperparameters (e.g., learning rate, batch size, experience replay buffer) individually tuned. Streaming Environment: To emulate the realistic streaming environment, we built an open-source ABR emulator [32] based on the previous work by Mao et al. [10], applying custom modi- fications to accommodate our experimental setup. For example, each streaming session emulates the playback of a 192-second video, partitioned into 48 segments of 4 seconds each. Every segment is encoded into eight bitrate levels: {0.2, 0.8, 2.2, 5.0, 10.0, 18.0, 32.0, 50.0} Mbps, reflecting a wide range of encoding options. The network condition is emulated using TCP throughput traces, with an average bandwidth of 17.66 Mbps and a peak Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

**[Estado / inputs / features | extracto 14 | p.2]**

IV). II. ABR UNDER-GENERALIZATION Existing learning-based ABR algorithms [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30] (will be comprehensively reviewed in Section V) predominantly rely on advanced DRL techniques [12], [13], [14], [15], [16], [17] for policy training. To demonstrate the ABR Under-Generalization problem, we conducted a measurement study evaluating the ABRalgorithms trainedusingsixwidelyadoptedDRLmethods: A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17]. DRL Configuration. The neural network architecture adheres to the established designs from prior literature [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30]. Specifi- cally,themodelinputcomprisesfivecategoriesofenvironmental states: (i) the measured throughput of the past 8 segments, (ii) the download durations of the past 8 segments, (iii) the bitrate of the most recently downloaded segment, (iv) the current buffer occupancy, and (v) the number of remaining segments in the current streaming session. The first two inputs are processed via convolutional neural networks (CNNs) with 128 filters, while the remaining three are fed into fully connected (dense) layers with 128 neurons. Then the outputs are subsequently merged through a dense aggregation layer comprising 256 neurons. The output layer offers the discrete bitrate level, which serves as the decision action. All the six DRL methods are trained using the Adam optimizer, with training hyperparameters (e.g., learning rate, batch size, experience replay buffer) individually tuned. Streaming Environment: To emulate the realistic streaming environment, we built an open-source ABR emula

**[Estado / inputs / features | extracto 15 | p.2]**

ts effectiveness (Section IV). II. ABR UNDER-GENERALIZATION Existing learning-based ABR algorithms [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30] (will be comprehensively reviewed in Section V) predominantly rely on advanced DRL techniques [12], [13], [14], [15], [16], [17] for policy training. To demonstrate the ABR Under-Generalization problem, we conducted a measurement study evaluating the ABRalgorithms trainedusingsixwidelyadoptedDRLmethods: A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17]. DRL Configuration. The neural network architecture adheres to the established designs from prior literature [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30]. Specifi- cally,themodelinputcomprisesfivecategoriesofenvironmental states: (i) the measured throughput of the past 8 segments, (ii) the download durations of the past 8 segments, (iii) the bitrate of the most recently downloaded segment, (iv) the current buffer occupancy, and (v) the number of remaining segments in the current streaming session. The first two inputs are processed via convolutional neural networks (CNNs) with 128 filters, while the remaining three are fed into fully connected (dense) layers with 128 neurons. Then the outputs are subsequently merged through a dense aggregation layer comprising 256 neurons. The output layer offers the discrete bitrate level, which serves as the decision action. All the six DRL methods are trained using the Adam optimizer, with training hyperparameters (e.g., learning rate, batch size, experience replay buffer) individually tuned. Streaming Environment: To emulate the realistic streaming environment, we

**[Estado / inputs / features | extracto 16 | p.2]**

the ABR algorithms trained using the conventional DRL approaches [12], [13], [14], [15], [16], [17] consistently maintain high performance across all network conditions. In particular, all the measured algorithms fail in 8.1% to 17.1% of the evaluated traces, significantly degrading the overall results. Additionally, the specific traces where underperformance occurs differ greatly depending on the specific DRL method adopted. To address this issue, BETA incorporates a spatial module. It begins by training a basic ABR model and benchmarks its QoE against the offline optimal performance per streaming ses- sion. This process helps identify the underperforming network conditions, from which the corresponding network features are extracted, and then are used to predict the potential network conditions that might cause poor performance in the future. BETA proceeds to train specialized ABR models specifically tailored to these challenging network conditions. Temporal Module: We observed that the existing DRL- trained ABR algorithms are often short-sighted, focusing only on single-step future planning. This is due to their training approach, where each epoch updates the model based solely on the immediate reward of short-term feedback. This is ill- suited for the video streaming contexts that require consecutive decision-making across all the video segments in each streaming session. BETA addresses this issue with a temporal module. BETA samples multi-segment decision sequences during training, each consisting of a series of state-action-reward tuples. For each sequence, a discounted actual reward encompassing all the seg- ments is calculated, along with an expected reward based on th

### 5.x Acción / decisión ABR

**[Acción / decisión ABR | extracto 1 | p.1]**

12852 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025 A Novel Spatial-Temporal Learning Method for Enhancing Generalization in Adaptive Video Streaming Guanghui Zhang , Ziming Wang , Huaren Wei, Mengbai Xiao , Hui Yuan , Senior Member, IEEE, Dongxiao Yu , Senior Member, IEEE, and Xiuzhen Cheng , Fellow, IEEE Abstract—Adaptive video streaming has become a fundamental technology for video delivery. With the rise of deep reinforcement learning (DRL), streaming vendors are increasingly adopting DRL- driven adaptive bitrate (ABR) algorithms. In real-world deploy- ments, most ABR approaches are developed with the aim of main- taining good performance across a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-ba

**[Acción / decisión ABR | extracto 2 | p.1]**

ang@sdu. edu.cn; 202235192@mail.sdu.edu.cn; 202315182@mail.sdu.edu.cn; xiaomb@ sdu.edu.cn; dxyu@sdu.edu; xzcheng@sdu.edu.cn). Hui Yuan is with the School of Control Science and Engineering, Shandong University, Jinan 250061, China (e-mail: huiyuan@sdu.edu.cn). Digital Object Identifier 10.1109/TMC.2025.3588135 Internet. As reported by Cisco, global video streaming traffic has surged by a factor of 15 over the past five years and now accounts for over 80% of the Internet traffic [1]. However, the highly variable nature of the mobile networks (primarily caused by unstable radio signals) poses a major obstacle to video streaming. Smooth playback relies on stable and consistent network throughput, which is difficult to main- tain in such dynamic environments. To tackle this issue, the streaming vendors have turned their attention to adaptive bitrate (ABR) algorithms, aiming to alleviate the negative effects of the throughput fluctuations. These ABR algorithms are typically im- plemented under the DASH protocol [2]. Their key component is an adaptive logic, which intelligently adjusts video quality in real time (by selecting appropriate bitrates) based on several streaming metrics such as historical throughput measurements and current buffer status. The objective is to enhance the viewer’s Quality of Experience (QoE). Most ABR algorithms are developed with the intention to perform reliably across the wide network environments of any size and shape, e.g., from 3G networks with peak band- widths of a few Mbps to 5G networks offering mean band- widths of 100+ Mbps. However, real-world experiments con- sistently demonstrate that the existing ABR algorithms, while effective under intended

**[Acción / decisión ABR | extracto 3 | p.1]**

of main- taining good performance across a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yielding average QoE gains of 19.4% to 50.9%,andachievingimprovementsofupto244.1%underseverely fluctuating network conditions. Index Terms—Video streaming, mobile network, deep reinforcement learning, quality-of-experience. I. INTRODUCTION I N RECENT years, video streaming has witnessed rapid expansion, emerging as one of the primary applications of the Received 9 December 2024; revised 26 June 2025; accepted 3 July 2025. Date of publication 15 July 2025; date of current version 5 November 2025. This work was supported by the National Natural Science Foundation of China under Grant 62302268, in part by the Natural Science Foundation of Shando

**[Acción / decisión ABR | extracto 4 | p.1]**

entifier 10.1109/TMC.2025.3588135 Internet. As reported by Cisco, global video streaming traffic has surged by a factor of 15 over the past five years and now accounts for over 80% of the Internet traffic [1]. However, the highly variable nature of the mobile networks (primarily caused by unstable radio signals) poses a major obstacle to video streaming. Smooth playback relies on stable and consistent network throughput, which is difficult to main- tain in such dynamic environments. To tackle this issue, the streaming vendors have turned their attention to adaptive bitrate (ABR) algorithms, aiming to alleviate the negative effects of the throughput fluctuations. These ABR algorithms are typically im- plemented under the DASH protocol [2]. Their key component is an adaptive logic, which intelligently adjusts video quality in real time (by selecting appropriate bitrates) based on several streaming metrics such as historical throughput measurements and current buffer status. The objective is to enhance the viewer’s Quality of Experience (QoE). Most ABR algorithms are developed with the intention to perform reliably across the wide network environments of any size and shape, e.g., from 3G networks with peak band- widths of a few Mbps to 5G networks offering mean band- widths of 100+ Mbps. However, real-world experiments con- sistently demonstrate that the existing ABR algorithms, while effective under intended network conditions, suffer significant degradation when the network conditions vary widely [3], [4], [5], [6], [11]. This phenomenon, i.e., the operational range of an ABR algorithm is narrow, leads to a marked decrease in the overall performance. We defined this problem as “

**[Acción / decisión ABR | extracto 5 | p.2]**

corresponding network features are extracted, and then are used to predict the potential network conditions that might cause poor performance in the future. BETA proceeds to train specialized ABR models specifically tailored to these challenging network conditions. Temporal Module: We observed that the existing DRL- trained ABR algorithms are often short-sighted, focusing only on single-step future planning. This is due to their training approach, where each epoch updates the model based solely on the immediate reward of short-term feedback. This is ill- suited for the video streaming contexts that require consecutive decision-making across all the video segments in each streaming session. BETA addresses this issue with a temporal module. BETA samples multi-segment decision sequences during training, each consisting of a series of state-action-reward tuples. For each sequence, a discounted actual reward encompassing all the seg- ments is calculated, along with an expected reward based on the initial and final states of each sequence. Both of the rewards are then used to update the neuron weights by minimizing the gap between them. This approach enables the trained ABR model to make far-sighted decisions, thereby ensuring more stable QoE. Extensive evaluation using large-scale network trace datasets demonstrates the effectiveness of BETA. Compared to state-of- the-art ABR algorithms, BETA improves average QoE by 19.4% to 50.9%, with gains reaching 244.1% in highly variable network conditions. For the internal QoE metrics, BETA achieves a 7.9% increase in video quality and a 98.3% reduction in rebuffering events. These benefits are attributed to BETA’s flexible bitrate decisions

**[Acción / decisión ABR | extracto 6 | p.2]**

s of state-action-reward tuples. For each sequence, a discounted actual reward encompassing all the seg- ments is calculated, along with an expected reward based on the initial and final states of each sequence. Both of the rewards are then used to update the neuron weights by minimizing the gap between them. This approach enables the trained ABR model to make far-sighted decisions, thereby ensuring more stable QoE. Extensive evaluation using large-scale network trace datasets demonstrates the effectiveness of BETA. Compared to state-of- the-art ABR algorithms, BETA improves average QoE by 19.4% to 50.9%, with gains reaching 244.1% in highly variable network conditions. For the internal QoE metrics, BETA achieves a 7.9% increase in video quality and a 98.3% reduction in rebuffering events. These benefits are attributed to BETA’s flexible bitrate decisions, which not only better match the network dynamics but also fully utilize available network resources. In summary, our contributions are three-fold: Large-Scale Measurement Study: We systematically evalu- ated ABR algorithms trained by six well-known DRL methods, A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17], clearly revealing the impact of the ABR Under- Generalization problem (Section II). Design of BETA: We presented BETA, a DRL-based ABR framework integrating spatial and temporal modules to enhance generalization. The implementation of BETA has been open- sourced on GitHub [32] to support reproducibility and future research (Section III). Comprehensive Evaluation: Through extensive evaluations, we show that BETA significantly outperforms the state-of-the- art ABR algorithms. In addition, we investigated the

**[Acción / decisión ABR | extracto 7 | p.2]**

tial module. It begins by training a basic ABR model and benchmarks its QoE against the offline optimal performance per streaming ses- sion. This process helps identify the underperforming network conditions, from which the corresponding network features are extracted, and then are used to predict the potential network conditions that might cause poor performance in the future. BETA proceeds to train specialized ABR models specifically tailored to these challenging network conditions. Temporal Module: We observed that the existing DRL- trained ABR algorithms are often short-sighted, focusing only on single-step future planning. This is due to their training approach, where each epoch updates the model based solely on the immediate reward of short-term feedback. This is ill- suited for the video streaming contexts that require consecutive decision-making across all the video segments in each streaming session. BETA addresses this issue with a temporal module. BETA samples multi-segment decision sequences during training, each consisting of a series of state-action-reward tuples. For each sequence, a discounted actual reward encompassing all the seg- ments is calculated, along with an expected reward based on the initial and final states of each sequence. Both of the rewards are then used to update the neuron weights by minimizing the gap between them. This approach enables the trained ABR model to make far-sighted decisions, thereby ensuring more stable QoE. Extensive evaluation using large-scale network trace datasets demonstrates the effectiveness of BETA. Compared to state-of- the-art ABR algorithms, BETA improves average QoE by 19.4% to 50.9%, with gains reaching 244.1% in hig

**[Acción / decisión ABR | extracto 8 | p.3]**

12854 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025 TABLE I COMPARISON OF QOE AND STREAMING PERFORMANCE OVER SIX DRL-BASED ABR ALGORITHMS value of up to 131.44 Mbps. These traces were collected from real-world cellular networks, including 3G, 4G, 5G, and Wi- Fi, over a continuous 77-day period. The data collection was conducted across four types of geographic locations: subways, campuses, shopping malls, and homes. The complete dataset has been made publicly available on GitHub [36]. In this evaluation, 80% of the data is used for model training, and the remaining 20% is reserved for online testing. Both the training and testing sets comprehensively cover the three network types, the four geographic locations, and all the time periods in one day. For the streaming performance metric, we adopted an existing QoE function proposed by Mao e

**[Acción / decisión ABR | extracto 9 | p.3]**

ollection was conducted across four types of geographic locations: subways, campuses, shopping malls, and homes. The complete dataset has been made publicly available on GitHub [36]. In this evaluation, 80% of the data is used for model training, and the remaining 20% is reserved for online testing. Both the training and testing sets comprehensively cover the three network types, the four geographic locations, and all the time periods in one day. For the streaming performance metric, we adopted an existing QoE function proposed by Mao et al. [10]: QoE = N−1  t=0 F(bt) −σ × N−1  t=0 θt − N−2  t=0 |F(bt+1) −F(bt)| (1) where the first term of Eq. (1) denotes the video quality utility, and the last two denote the penalties for playback rebuffering (coefficient σ = 50) and video quality variation respectively. Specifically, bt is the video bitrate of segment t, θt is the rebuffering duration in downloading segment t, F(.) denotes the mapping from bitrate to video quality where we adopted linear mapping F(bt) = bt [10] in this evaluation. Results Analysis: Table I summarizes the performance of the six DRL-based ABR algorithms. QoE is reported using two representations: the absolute QoE score (denoted as A-QoE) and the normalized QoE score (denoted as N-QoE). The normalized score is obtained by dividing the absolute score by the offline optimal. The optimal QoE serves as the theoretical upper bound, which is computed based on dynamic programming, using an omniscient policy with perfect foresight of future network throughput (more details are referred to Spiteri et al. [8], and the implementation is available in [31]). In addition to the QoE, we further evaluated the three core metri

**[Acción / decisión ABR | extracto 10 | p.3]**

and testing sets comprehensively cover the three network types, the four geographic locations, and all the time periods in one day. For the streaming performance metric, we adopted an existing QoE function proposed by Mao et al. [10]: QoE = N−1  t=0 F(bt) −σ × N−1  t=0 θt − N−2  t=0 |F(bt+1) −F(bt)| (1) where the first term of Eq. (1) denotes the video quality utility, and the last two denote the penalties for playback rebuffering (coefficient σ = 50) and video quality variation respectively. Specifically, bt is the video bitrate of segment t, θt is the rebuffering duration in downloading segment t, F(.) denotes the mapping from bitrate to video quality where we adopted linear mapping F(bt) = bt [10] in this evaluation. Results Analysis: Table I summarizes the performance of the six DRL-based ABR algorithms. QoE is reported using two representations: the absolute QoE score (denoted as A-QoE) and the normalized QoE score (denoted as N-QoE). The normalized score is obtained by dividing the absolute score by the offline optimal. The optimal QoE serves as the theoretical upper bound, which is computed based on dynamic programming, using an omniscient policy with perfect foresight of future network throughput (more details are referred to Spiteri et al. [8], and the implementation is available in [31]). In addition to the QoE, we further evaluated the three core metrics that contribute to QoE: the average video bitrate, total rebuffering duration, and video quality variation. See their definitions in Eq. (1). These metrics collectively characterize the tradeoffs each algorithm makes in adaptive streaming scenarios. From Table I, two key observations can be made regarding the QoE perform

**[Acción / decisión ABR | extracto 11 | p.3]**

hereas the SAC-based model performs the worst, with an A-QoE of only305.9.Second,thenormalizedQoE(N-QoE)revealsthatall the six methods attain only suboptimal performance, achieving merely 43.1% to 48.9% of the offline optimal QoE. This is significantly lower than the theoretical upper bound of 100%. While the offline optimal, derived under the assumption of perfect foresight of future throughput, is unattainable in real- world settings due to the inherent unpredictability of network dynamics, the pronounced QoE gap highlights the substantial room for performance improvement. In Table I, the best-performing DRL method under each metric is highlighted in bold. To gain deeper insights into these top-performing models, we further analyzed their per-session performance. Specifically, since TD3 achieves the highest nor- malized QoE (48.9%), we selected two representative streaming sessions and visualized their performance in Fig. 1(a) and (b). In Sample 1 (Fig. 1(a)), TD3 exhibits effective bitrate adaptation, resulting in a high QoE score of 1405.9, which is close to the offline optimal of 1574.0. By contrast, in Sample 2 (Fig. 1(b)), TD3 fails to adapt appropriately to dynamic network conditions, leading to a significant rebuffering event. Specifically, at the 30th segment, the available throughput drops sharply, yet the selected bitrate remains high, rapidly depleting the playback buffer and causing an 8.9-second rebuffering event. This results inaseverelydegradedQoEof–31.1,farbelowthecorresponding offline optimal of 685.0. Although TD3 achieves the highest overall QoE, it performs suboptimally in terms of rebuffering duration and quality varia- tion, as shown in Table I. In contr

**[Acción / decisión ABR | extracto 12 | p.3]**

causing an 8.9-second rebuffering event. This results inaseverelydegradedQoEof–31.1,farbelowthecorresponding offline optimal of 685.0. Although TD3 achieves the highest overall QoE, it performs suboptimally in terms of rebuffering duration and quality varia- tion, as shown in Table I. In contrast, PPO yields the best results for these two metrics. To this end, we applied PPO to the same two streaming sessions (i.e., Sample 1 and Sample 2) and visual- ized the streaming performance in Fig. 1(c) and (d), respectively. Interestingly, PPO exhibits a markedly different adaptation be- havior compared to TD3. In Sample 1, PPO achieves a QoE of 577.3, which is significantly lower than both the offline optimal (1574.0) and the result achieved by TD3 (1405.9). This underperformance is primarily due to its conservative bitrate selection, i.e., PPO chooses bitrates substantially below the available throughput, leading to inefficient utilization of network resources. Conversely, in Sample 2, PPO achieves a QoE of 327.2, which, although still below the offline optimal (685.0), is markedly superior to that of TD3 (–31.1). This improvement is largely attributable to PPO’s effective avoidance of playback rebuffering events, as the rebuffering duration approaches zero. From the above results, several important insights emerge. While the DRL-based ABR algorithms can perform adequately under their intended network conditions, the effectiveness de- grades considerably in others. This limitation stems from their Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

**[Acción / decisión ABR | extracto 13 | p.3]**

performance, achieving merely 43.1% to 48.9% of the offline optimal QoE. This is significantly lower than the theoretical upper bound of 100%. While the offline optimal, derived under the assumption of perfect foresight of future throughput, is unattainable in real- world settings due to the inherent unpredictability of network dynamics, the pronounced QoE gap highlights the substantial room for performance improvement. In Table I, the best-performing DRL method under each metric is highlighted in bold. To gain deeper insights into these top-performing models, we further analyzed their per-session performance. Specifically, since TD3 achieves the highest nor- malized QoE (48.9%), we selected two representative streaming sessions and visualized their performance in Fig. 1(a) and (b). In Sample 1 (Fig. 1(a)), TD3 exhibits effective bitrate adaptation, resulting in a high QoE score of 1405.9, which is close to the offline optimal of 1574.0. By contrast, in Sample 2 (Fig. 1(b)), TD3 fails to adapt appropriately to dynamic network conditions, leading to a significant rebuffering event. Specifically, at the 30th segment, the available throughput drops sharply, yet the selected bitrate remains high, rapidly depleting the playback buffer and causing an 8.9-second rebuffering event. This results inaseverelydegradedQoEof–31.1,farbelowthecorresponding offline optimal of 685.0. Although TD3 achieves the highest overall QoE, it performs suboptimally in terms of rebuffering duration and quality varia- tion, as shown in Table I. In contrast, PPO yields the best results for these two metrics. To this end, we applied PPO to the same two streaming sessions (i.e., Sample 1 and Sample 2) and visual- i

**[Acción / decisión ABR | extracto 14 | p.4]**

the Spatial Module. Specifically, BETA initially invokes the Temporal Module to train a base ABR model, which is then evaluated across all training network traces by comparing the achieved QoE with the corresponding offline optimum. Based on this evaluation, the training traces are partitioned into two subsets: one where the ABR model performs adequately, and the other where it fails to generalize well. From these labeled traces, BETA extracts in- ternal network features to train a classifier that predicts whether a given network trace is likely to result in underperformance. This classifier enables BETA to dynamically distinguish between “normal” and “difficult” traces in real-time. Accordingly, two complementary ABR models are trained for each trace subset by invoking the Temporal Module, and during online stream- ing, BETA dynamically selects the appropriate logic to better Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

**[Acción / decisión ABR | extracto 15 | p.5]**

12856 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025 Fig. 2. The whole structure of BETA with the spatial module and the temporal module. accommodate the diverse network conditions. The details are elaborated in Section III-B. Temporal Module: Existing DRL-based ABR algorithms [12], [13], [14], [15], [16], [17] often exhibit short-sightedness. This is problematic in adaptive video streaming, where QoE is influenced by temporal continuity and cumulative effects of the ABR decisions over multiple segments. To overcome this issue, BETA introduces the Temporal Module. During training, BETA records a state–action–reward tuple for each segment and stores them in an experience buffer, maintaining a history of decision sequences. From this buffer, it samples tuple sequences where each consists of n consecutive segments. For each sequence, a disc

**[Acción / decisión ABR | extracto 16 | p.5]**

atic in adaptive video streaming, where QoE is influenced by temporal continuity and cumulative effects of the ABR decisions over multiple segments. To overcome this issue, BETA introduces the Temporal Module. During training, BETA records a state–action–reward tuple for each segment and stores them in an experience buffer, maintaining a history of decision sequences. From this buffer, it samples tuple sequences where each consists of n consecutive segments. For each sequence, a discounted actual reward encompassing all the segments is cal- culated, along with an expected reward based on the initial and final states of each sequence. These two rewards are integrated into the training, where the neural network weights are adjusted to minimize the discrepancy between the two. Through this approach, the training ABR model learns to optimize decisions across temporally extended horizons, thereby improving QoE consistency across entire streaming sessions. The details are provided in Section III-C. B. Spatial Module The structure of the Spatial Module is illustrated in Fig. 2-left. It operates in three sequential phases: offline classifier training, offline multi-model training, and online differential streaming. The three phases are encapsulated in Algorithm 1 as three distinct functions: lines 4∼17, lines 18∼29, and lines 30∼38, respectively. The main execution flow (lines 1∼3) invokes these functions in sequence. In the following, we elaborate on each phase in detail. Offline Classifier Training: The primary objective of the Spatial Module is to enhance the generalization capability of ABR algorithms, namely, to ensure robust performance across a wide spectrum of network conditions.

### 5.x Reward / QoE / objetivo

**[Reward / QoE / objetivo | extracto 1 | p.1]**

poral Learning Method for Enhancing Generalization in Adaptive Video Streaming Guanghui Zhang , Ziming Wang , Huaren Wei, Mengbai Xiao , Hui Yuan , Senior Member, IEEE, Dongxiao Yu , Senior Member, IEEE, and Xiuzhen Cheng , Fellow, IEEE Abstract—Adaptive video streaming has become a fundamental technology for video delivery. With the rise of deep reinforcement learning (DRL), streaming vendors are increasingly adopting DRL- driven adaptive bitrate (ABR) algorithms. In real-world deploy- ments, most ABR approaches are developed with the aim of main- taining good performance across a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yielding average QoE gains of 19.4% to 50.9%,andachievingimprovementsofupto244.1%underseverely fluct

**[Reward / QoE / objetivo | extracto 2 | p.1]**

0% of the Internet traffic [1]. However, the highly variable nature of the mobile networks (primarily caused by unstable radio signals) poses a major obstacle to video streaming. Smooth playback relies on stable and consistent network throughput, which is difficult to main- tain in such dynamic environments. To tackle this issue, the streaming vendors have turned their attention to adaptive bitrate (ABR) algorithms, aiming to alleviate the negative effects of the throughput fluctuations. These ABR algorithms are typically im- plemented under the DASH protocol [2]. Their key component is an adaptive logic, which intelligently adjusts video quality in real time (by selecting appropriate bitrates) based on several streaming metrics such as historical throughput measurements and current buffer status. The objective is to enhance the viewer’s Quality of Experience (QoE). Most ABR algorithms are developed with the intention to perform reliably across the wide network environments of any size and shape, e.g., from 3G networks with peak band- widths of a few Mbps to 5G networks offering mean band- widths of 100+ Mbps. However, real-world experiments con- sistently demonstrate that the existing ABR algorithms, while effective under intended network conditions, suffer significant degradation when the network conditions vary widely [3], [4], [5], [6], [11]. This phenomenon, i.e., the operational range of an ABR algorithm is narrow, leads to a marked decrease in the overall performance. We defined this problem as “ABR Under-Generalization”. The existing ABR algorithms can be generally divided into two major categories: heuristic-based and learning-based. The former [5], [6], [7], [8], [9], [19], [20], [2

**[Reward / QoE / objetivo | extracto 3 | p.1]**

ive years and now accounts for over 80% of the Internet traffic [1]. However, the highly variable nature of the mobile networks (primarily caused by unstable radio signals) poses a major obstacle to video streaming. Smooth playback relies on stable and consistent network throughput, which is difficult to main- tain in such dynamic environments. To tackle this issue, the streaming vendors have turned their attention to adaptive bitrate (ABR) algorithms, aiming to alleviate the negative effects of the throughput fluctuations. These ABR algorithms are typically im- plemented under the DASH protocol [2]. Their key component is an adaptive logic, which intelligently adjusts video quality in real time (by selecting appropriate bitrates) based on several streaming metrics such as historical throughput measurements and current buffer status. The objective is to enhance the viewer’s Quality of Experience (QoE). Most ABR algorithms are developed with the intention to perform reliably across the wide network environments of any size and shape, e.g., from 3G networks with peak band- widths of a few Mbps to 5G networks offering mean band- widths of 100+ Mbps. However, real-world experiments con- sistently demonstrate that the existing ABR algorithms, while effective under intended network conditions, suffer significant degradation when the network conditions vary widely [3], [4], [5], [6], [11]. This phenomenon, i.e., the operational range of an ABR algorithm is narrow, leads to a marked decrease in the overall performance. We defined this problem as “ABR Under-Generalization”. The existing ABR algorithms can be generally divided into two major categories: heuristic-based and learning-based. T

**[Reward / QoE / objetivo | extracto 4 | p.1]**

r: Hui Yuan.) Guanghui Zhang, Ziming Wang, Huaren Wei, Mengbai Xiao, Dongxiao Yu, and Xiuzhen Cheng are with the School of Computer Science and Technol- ogy, Shandong University, Qingdao 266237, China (e-mail: gh.zhang@sdu. edu.cn; 202235192@mail.sdu.edu.cn; 202315182@mail.sdu.edu.cn; xiaomb@ sdu.edu.cn; dxyu@sdu.edu; xzcheng@sdu.edu.cn). Hui Yuan is with the School of Control Science and Engineering, Shandong University, Jinan 250061, China (e-mail: huiyuan@sdu.edu.cn). Digital Object Identifier 10.1109/TMC.2025.3588135 Internet. As reported by Cisco, global video streaming traffic has surged by a factor of 15 over the past five years and now accounts for over 80% of the Internet traffic [1]. However, the highly variable nature of the mobile networks (primarily caused by unstable radio signals) poses a major obstacle to video streaming. Smooth playback relies on stable and consistent network throughput, which is difficult to main- tain in such dynamic environments. To tackle this issue, the streaming vendors have turned their attention to adaptive bitrate (ABR) algorithms, aiming to alleviate the negative effects of the throughput fluctuations. These ABR algorithms are typically im- plemented under the DASH protocol [2]. Their key component is an adaptive logic, which intelligently adjusts video quality in real time (by selecting appropriate bitrates) based on several streaming metrics such as historical throughput measurements and current buffer status. The objective is to enhance the viewer’s Quality of Experience (QoE). Most ABR algorithms are developed with the intention to perform reliably across the wide network environments of any size and shape, e.g., from 3G networks

**[Reward / QoE / objetivo | extracto 5 | p.2]**

s differ greatly depending on the specific DRL method adopted. To address this issue, BETA incorporates a spatial module. It begins by training a basic ABR model and benchmarks its QoE against the offline optimal performance per streaming ses- sion. This process helps identify the underperforming network conditions, from which the corresponding network features are extracted, and then are used to predict the potential network conditions that might cause poor performance in the future. BETA proceeds to train specialized ABR models specifically tailored to these challenging network conditions. Temporal Module: We observed that the existing DRL- trained ABR algorithms are often short-sighted, focusing only on single-step future planning. This is due to their training approach, where each epoch updates the model based solely on the immediate reward of short-term feedback. This is ill- suited for the video streaming contexts that require consecutive decision-making across all the video segments in each streaming session. BETA addresses this issue with a temporal module. BETA samples multi-segment decision sequences during training, each consisting of a series of state-action-reward tuples. For each sequence, a discounted actual reward encompassing all the seg- ments is calculated, along with an expected reward based on the initial and final states of each sequence. Both of the rewards are then used to update the neuron weights by minimizing the gap between them. This approach enables the trained ABR model to make far-sighted decisions, thereby ensuring more stable QoE. Extensive evaluation using large-scale network trace datasets demonstrates the effectiveness of BETA. Compared to s

**[Reward / QoE / objetivo | extracto 6 | p.2]**

ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING 12853 However, our measurement study (refer to Section II) reveals that when faced with a wide range of network conditions, even extensively trained DRL-based ABR algorithms can only achieve 43.1% ∼48.9% of the maximum possible QoE, far below the offline optimal 100%. This highlights the problem of ABR Under-Generalization, which contradicts the theoretical expectation that training on large-scale real traces should yield generalizable ABR policies. The root cause appears to lie in the direct application of the generic DRL techniques [12], [13], [14], [15], [16], [17], which fail to capture all the key features required to adapt across different environments. Motivated by this challenge, we proposed BETA, a new DRL-based ABR framework specifically designed to enhance the generalization of video streaming. BETA consists of two core modules: spatial and temporal, which jointly tackle the above-mentioned challenge: Spatial Module: Our measurement study (Section II) shows that none of the ABR algorithms trained using the conventional DRL approaches [12], [13], [14], [1

**[Reward / QoE / objetivo | extracto 7 | p.2]**

egment decision sequences during training, each consisting of a series of state-action-reward tuples. For each sequence, a discounted actual reward encompassing all the seg- ments is calculated, along with an expected reward based on the initial and final states of each sequence. Both of the rewards are then used to update the neuron weights by minimizing the gap between them. This approach enables the trained ABR model to make far-sighted decisions, thereby ensuring more stable QoE. Extensive evaluation using large-scale network trace datasets demonstrates the effectiveness of BETA. Compared to state-of- the-art ABR algorithms, BETA improves average QoE by 19.4% to 50.9%, with gains reaching 244.1% in highly variable network conditions. For the internal QoE metrics, BETA achieves a 7.9% increase in video quality and a 98.3% reduction in rebuffering events. These benefits are attributed to BETA’s flexible bitrate decisions, which not only better match the network dynamics but also fully utilize available network resources. In summary, our contributions are three-fold: Large-Scale Measurement Study: We systematically evalu- ated ABR algorithms trained by six well-known DRL methods, A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17], clearly revealing the impact of the ABR Under- Generalization problem (Section II). Design of BETA: We presented BETA, a DRL-based ABR framework integrating spatial and temporal modules to enhance generalization. The implementation of BETA has been open- sourced on GitHub [32] to support reproducibility and future research (Section III). Comprehensive Evaluation: Through extensive evaluations, we show that BETA significantly outperforms th

**[Reward / QoE / objetivo | extracto 8 | p.3]**

12854 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025 TABLE I COMPARISON OF QOE AND STREAMING PERFORMANCE OVER SIX DRL-BASED ABR ALGORITHMS value of up to 131.44 Mbps. These traces were collected from real-world cellular networks, including 3G, 4G, 5G, and Wi- Fi, over a continuous 77-day period. The data collection was conducted across four types of geographic locations: subways, campuses, shopping malls, and homes. The complete dataset has been made publicly available on GitHub [36]. In this evaluation, 80% of the data is used for model training, and the remaining 20% is reserved for online testing. Both the training and testing sets comprehensively cover the three network types, the four geographic locations, and all the time periods in one day. For the streaming performance metric, we adopted an existing QoE function proposed by Mao et al. [10]: QoE = N−1  t=0 F(bt) −σ × N−1  t=0 θt − N−2  t=0 |F(bt+1) −F(bt)

**[Reward / QoE / objetivo | extracto 9 | p.3]**

ue of up to 131.44 Mbps. These traces were collected from real-world cellular networks, including 3G, 4G, 5G, and Wi- Fi, over a continuous 77-day period. The data collection was conducted across four types of geographic locations: subways, campuses, shopping malls, and homes. The complete dataset has been made publicly available on GitHub [36]. In this evaluation, 80% of the data is used for model training, and the remaining 20% is reserved for online testing. Both the training and testing sets comprehensively cover the three network types, the four geographic locations, and all the time periods in one day. For the streaming performance metric, we adopted an existing QoE function proposed by Mao et al. [10]: QoE = N−1  t=0 F(bt) −σ × N−1  t=0 θt − N−2  t=0 |F(bt+1) −F(bt)| (1) where the first term of Eq. (1) denotes the video quality utility, and the last two denote the penalties for playback rebuffering (coefficient σ = 50) and video quality variation respectively. Specifically, bt is the video bitrate of segment t, θt is the rebuffering duration in downloading segment t, F(.) denotes the mapping from bitrate to video quality where we adopted linear mapping F(bt) = bt [10] in this evaluation. Results Analysis: Table I summarizes the performance of the six DRL-based ABR algorithms. QoE is reported using two representations: the absolute QoE score (denoted as A-QoE) and the normalized QoE score (denoted as N-QoE). The normalized score is obtained by dividing the absolute score by the offline optimal. The optimal QoE serves as the theoretical upper bound, which is computed based on dynamic programming, using an omniscient policy with perfect foresight of future network through

**[Reward / QoE / objetivo | extracto 10 | p.3]**

al-world cellular networks, including 3G, 4G, 5G, and Wi- Fi, over a continuous 77-day period. The data collection was conducted across four types of geographic locations: subways, campuses, shopping malls, and homes. The complete dataset has been made publicly available on GitHub [36]. In this evaluation, 80% of the data is used for model training, and the remaining 20% is reserved for online testing. Both the training and testing sets comprehensively cover the three network types, the four geographic locations, and all the time periods in one day. For the streaming performance metric, we adopted an existing QoE function proposed by Mao et al. [10]: QoE = N−1  t=0 F(bt) −σ × N−1  t=0 θt − N−2  t=0 |F(bt+1) −F(bt)| (1) where the first term of Eq. (1) denotes the video quality utility, and the last two denote the penalties for playback rebuffering (coefficient σ = 50) and video quality variation respectively. Specifically, bt is the video bitrate of segment t, θt is the rebuffering duration in downloading segment t, F(.) denotes the mapping from bitrate to video quality where we adopted linear mapping F(bt) = bt [10] in this evaluation. Results Analysis: Table I summarizes the performance of the six DRL-based ABR algorithms. QoE is reported using two representations: the absolute QoE score (denoted as A-QoE) and the normalized QoE score (denoted as N-QoE). The normalized score is obtained by dividing the absolute score by the offline optimal. The optimal QoE serves as the theoretical upper bound, which is computed based on dynamic programming, using an omniscient policy with perfect foresight of future network throughput (more details are referred to Spiteri et al. [8], and the

**[Reward / QoE / objetivo | extracto 11 | p.4]**

ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING 12855 Fig. 1. Per-session streaming performance (the x-axis – segment index, with the width of each segment scaled by its playback time). TABLE II THE PROPORTION OF UNDERPERFORMED STREAMING SESSIONS lack of generalization capability across diverse network condi- tions (i.e., the problem “ABR Under-Generalization” described in Section I). To further quantify this problem, we introduce a metric that captures the proportion of streaming sessions in which a DRL-based ABR method yields QoE significantly below the offline optimal. Specifically, we define this proportion as follows: ε = |{κj |oj −rj > δ, j = 0, 1, . . . , J −1}| J (2) where rj is the achieved QoE of session j, oj is the corresponding optimum, δ is the QoE gap (δ is set to 700. Note that this setting is to reflect the large gap between the actual QoE and the offline optimal. A sensitivity analysis is performed in Section IV-E), symbol |. | calculates the element number of the set, J is the total session number (denominator), and ε is the output proportion. Table II presents the results of the under-performing propor- tion across all six DRL-based ABR algorithms. The observed values are non-negligible, ranging from 8.1% to 17.1%. Given the pre-defined QoE gap δ = 700, such a high proportion of poorly performing sessions substantially degrades the overall QoE.

**[Reward / QoE / objetivo | extracto 12 | p.5]**

12856 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025 Fig. 2. The whole structure of BETA with the spatial module and the temporal module. accommodate the diverse network conditions. The details are elaborated in Section III-B. Temporal Module: Existing DRL-based ABR algorithms [12], [13], [14], [15], [16], [17] often exhibit short-sightedness. This is problematic in adaptive video streaming, where QoE is influenced by temporal continuity and cumulative effects of the ABR decisions over multiple segments. To overcome this issue, BETA introduces the Temporal Module. During training, BETA records a state–action–reward tuple for each segment and stores them in an experience buffer, maintaining a history of decision sequences. From this buffer, it samples tuple sequences where each consists of n consecutive segments. For each sequence, a discounted actual reward encompassing all the segments is cal- culated, along with an expected reward based on the initial and final states of each sequence. These two rewards are integrated into the training, where the neural network weights are adjusted to minimize the discrepancy between the two. Through this approach, the training ABR model learns to optimize decisions across temporally extended horizons, thereby improving QoE consistency across entire streaming sessions. The details are provided in Section III-C. B. Spatial Module The structure of the Spatial Module is illustrated in Fig. 2-left. It operates in thr

**[Reward / QoE / objetivo | extracto 13 | p.5]**

oral continuity and cumulative effects of the ABR decisions over multiple segments. To overcome this issue, BETA introduces the Temporal Module. During training, BETA records a state–action–reward tuple for each segment and stores them in an experience buffer, maintaining a history of decision sequences. From this buffer, it samples tuple sequences where each consists of n consecutive segments. For each sequence, a discounted actual reward encompassing all the segments is cal- culated, along with an expected reward based on the initial and final states of each sequence. These two rewards are integrated into the training, where the neural network weights are adjusted to minimize the discrepancy between the two. Through this approach, the training ABR model learns to optimize decisions across temporally extended horizons, thereby improving QoE consistency across entire streaming sessions. The details are provided in Section III-C. B. Spatial Module The structure of the Spatial Module is illustrated in Fig. 2-left. It operates in three sequential phases: offline classifier training, offline multi-model training, and online differential streaming. The three phases are encapsulated in Algorithm 1 as three distinct functions: lines 4∼17, lines 18∼29, and lines 30∼38, respectively. The main execution flow (lines 1∼3) invokes these functions in sequence. In the following, we elaborate on each phase in detail. Offline Classifier Training: The primary objective of the Spatial Module is to enhance the generalization capability of ABR algorithms, namely, to ensure robust performance across a wide spectrum of network conditions. Achieving this requires targeting the improvements of the n

**[Reward / QoE / objetivo | extracto 14 | p.5]**

he training, where the neural network weights are adjusted to minimize the discrepancy between the two. Through this approach, the training ABR model learns to optimize decisions across temporally extended horizons, thereby improving QoE consistency across entire streaming sessions. The details are provided in Section III-C. B. Spatial Module The structure of the Spatial Module is illustrated in Fig. 2-left. It operates in three sequential phases: offline classifier training, offline multi-model training, and online differential streaming. The three phases are encapsulated in Algorithm 1 as three distinct functions: lines 4∼17, lines 18∼29, and lines 30∼38, respectively. The main execution flow (lines 1∼3) invokes these functions in sequence. In the following, we elaborate on each phase in detail. Offline Classifier Training: The primary objective of the Spatial Module is to enhance the generalization capability of ABR algorithms, namely, to ensure robust performance across a wide spectrum of network conditions. Achieving this requires targeting the improvements of the network condition where the ABR model exhibits degraded performance. To this end, this phase focuses on identifying such problematic conditions. However, a key challenge arises: even if these conditions are well identified during offline training, the trained models may not work well at runtime, as the future network conditions of an ongoing streaming session are not known a priori. To tackle the challenge, in this work, a binary classifier is trained for the identification of network conditions. At the start, BETA trains a basic ABR model via the temporal module (will be introduced in Section III-C), and tests the

**[Reward / QoE / objetivo | extracto 15 | p.6]**

ach with 128 filters, to extract temporal patterns. The remaining three scalar states are Algorithm 1: Spatial Module. Input: Training throughput trace of all streaming sessions j: Λ={κj | ࢘j} # Step 1: Input - training trace data Λ; Output - trained classifier C and basic ABR model Mbasic. 1: C, Mbasic = Offline_Classifier_Training (Λ) # Step 2: Input - classifier C, training trace Λ, basic ABR model Mbasic; Output – two trained ABR models, i.e., ML1, ML2. 2 : ML1, ML2 = Offline_MultiModel_Training (C, Λ, Mbasic) # Step 3: Input - classifier C, and trained ABR models ML1, ML2. 3: Online_Differential_Streaming (C, ML1, ML2) 4: Function Offline_Classifier_Training (Λ={κj | ࢘j}) 5: Train ABR model Mbasic with Λ via temporal module 6: Λnormal = Ø, Λunder = Ø 7: for trace κj in streaming session j=1 to J do 8: Test Mbasic with κj, and obtain QoE rj 9: Compute optimal QoE under κj, denoted by oj 10: if oj – rj > δ then 11: Λunder ←κj 12: else 13: Λnormal ←κj 14: end if 15: end for 16: Supervised learning to train binary classifier C via {Λnormal, Λunder} 17: return C 18: Function Offline_MultiModel_Training (C, Λ={κj | ࢘j}, Mbasic) 19: Λ’normal = Ø, Λ’under = Ø 20: for trace κj in streaming session j=1 to J do 21: if C(κj) == L1 then 22: ΛL1 ←κj 23: else 24: ΛL2 ←κj 25: end if 26: end for 27: Train ABR model ML1 (upon Mbasic) with trace set ΛL1 via temporal module 28: Train ABR model ML2 (upon Mbasic) with trace set ΛL2 via temporal module 29: return ML1, ML2 30: Function Online_Differential_Streaming (C, ML1, ML2) 31: while a new streaming session starts do 32: Obtain the online captured throughput trace, denoted by κ 33: if C(κ) == L1 then 34: Apply ABR model ML1 to the current

**[Reward / QoE / objetivo | extracto 16 | p.7]**

12858 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025 Algorithm 2: Temporal Module. Initialize: critic-networks Qθ1 and Qθ2 (neuron weight θ1, θ2); actor-network πφ (neuron weight φ), target networks Qθ1_tar, Qθ2_tar, and πφ_tar (neuron weight θ1_tar, θ2_tar, φ_tar) Input: throughput trace data of all streaming sessions j: {κj | ࢘j} Output: trained actor-network πφ 1: for each streaming session j do 2: for segment t = 1 to T do 3: Observe state st and decide action at: at = πφ(st) 4: Map at to bitrate bt and download segment t with throughput trace κj 5: Observe reward rt (i.e., QoE), and new state st+1 6: Store tuple (st, at, rt, st+1) in an experience buffer Π 7: Sample a mini-batch Ω from Π, including a batch of tuple sequences, each with n consecutive tuples: Ω ←⟨(st′+i, at′+i, rt′+i, st′+1+i)⟩i=0,1,...,n−1 8: Qtar = Compute_Target_Q (Ω, n) 9: Update critics Qθ1, Qθ2 by minimizing the loss function: minθ1/2[Qθ1/2(st′, at′) −Qtar]2 10: if (t mod σ) == 0 then 11: Update actor πφ by maximizing the Q value: maxφQθ1[st′, πφ(st′)] 12: Softly update target networks: φ_tar = τ×φ_tar + (1-τ)×φ θ1_tar = τ×θ1_tar + (1-τ)×θ1 θ2_tar = τ×θ2_tar + (1-τ)×θ2 13: end if 14: end for 15: end for 16: return trained actor network πφ 17: Function Compute_Target_Q (Ω, n) 18: Initialize cumulative reward: R = 0 19: for (st’+i, at’+i, rt’+i, st’+1+i) in Ω and i = 0 to n-1 do 20: Update R with reward rt’+i and discount facto

### 5.x Entrenamiento / optimización

**[Entrenamiento / optimización | extracto 1 | p.1]**

12852 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025 A Novel Spatial-Temporal Learning Method for Enhancing Generalization in Adaptive Video Streaming Guanghui Zhang , Ziming Wang , Huaren Wei, Mengbai Xiao , Hui Yuan , Senior Member, IEEE, Dongxiao Yu , Senior Member, IEEE, and Xiuzhen Cheng , Fellow, IEEE Abstract—Adaptive video streaming has become a fundamental technology for video delivery. With the rise of deep reinforcement learning (DRL), streaming vendors are increasingly adopting DRL- driven adaptive bitrate (ABR) algorithms. In real-world deploy- ments, most ABR approaches are developed with the aim of main- taining good performance across a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms

**[Entrenamiento / optimización | extracto 2 | p.1]**

mance across a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yielding average QoE gains of 19.4% to 50.9%,andachievingimprovementsofupto244.1%underseverely fluctuating network conditions. Index Terms—Video streaming, mobile network, deep reinforcement learning, quality-of-experience. I. INTRODUCTION I N RECENT years, video streaming has witnessed rapid expansion, emerging as one of the primary applications of the Received 9 December 2024; revised 26 June 2025; accepted 3 July 2025. Date of publication 15 July 2025; date of current version 5 November 2025. This work was supported by the National Natural Science Foundation of China under Grant 62302268, in part by the Natural Science Foundation of Shandong Province under Grant 2023H

**[Entrenamiento / optimización | extracto 3 | p.1]**

oss a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yielding average QoE gains of 19.4% to 50.9%,andachievingimprovementsofupto244.1%underseverely fluctuating network conditions. Index Terms—Video streaming, mobile network, deep reinforcement learning, quality-of-experience. I. INTRODUCTION I N RECENT years, video streaming has witnessed rapid expansion, emerging as one of the primary applications of the Received 9 December 2024; revised 26 June 2025; accepted 3 July 2025. Date of publication 15 July 2025; date of current version 5 November 2025. This work was supported by the National Natural Science Foundation of China under Grant 62302268, in part by the Natural Science Foundation of Shandong Province under Grant 2023HWYQ-04

**[Entrenamiento / optimización | extracto 4 | p.1]**

ecialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yielding average QoE gains of 19.4% to 50.9%,andachievingimprovementsofupto244.1%underseverely fluctuating network conditions. Index Terms—Video streaming, mobile network, deep reinforcement learning, quality-of-experience. I. INTRODUCTION I N RECENT years, video streaming has witnessed rapid expansion, emerging as one of the primary applications of the Received 9 December 2024; revised 26 June 2025; accepted 3 July 2025. Date of publication 15 July 2025; date of current version 5 November 2025. This work was supported by the National Natural Science Foundation of China under Grant 62302268, in part by the Natural Science Foundation of Shandong Province under Grant 2023HWYQ-045 and Grant ZR2023QF060, in part by Qingdao Natural Science Foundation under Grant 23-2-1-127-zyyd-jch, and in part by the Taishan Scholar Project of Shandong Province under Grant tsqn202312051. An earlier version of this paper was presented in part at the IEEE International Conference on Sensing, Communication, and Networking [10.1109/SPCOM50965.2020.9179507]. Recommended for acceptance by S. Wang. (Corresponding author: Hui Yuan.) Guanghui Zhang, Ziming Wang, Huaren Wei, Mengbai Xiao, Dongxiao Yu, and Xiuzhen Cheng are with the School of Computer Science and Technol- ogy, Shandong University, Qingdao 266237, China (e-mail: gh.zhang@sdu. edu.cn; 202235192@mail.sdu.edu.cn; 202

**[Entrenamiento / optimización | extracto 5 | p.2]**

ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING 12853 However, our measurement study (refer to Section II) reveals that when faced with a wide range of network conditions, even extensively trained DRL-based ABR algorithms can only achieve 43.1% ∼48.9% of the maximum possible QoE, far below the offline optimal 100%. This highlights the problem of ABR Under-Generalization, which contradicts the theoretical expectation that training on large-scale real traces should yield generalizable ABR policies. The root cause appears to lie in the direct application of the generic DRL techniques [12], [13], [14], [15], [16], [17], which fail to capture all the key features required to adapt across different environments. Motivated by this challenge, we proposed BETA, a new DRL-based ABR framework specifically designed to enhance the generalization of video streaming. BETA consists of two core modules: spatial and temporal, which jointly tackle the above-mentioned challenge: Spatial Module: Our measurement study (Section II) shows that none of

**[Entrenamiento / optimización | extracto 6 | p.2]**

erent environments. Motivated by this challenge, we proposed BETA, a new DRL-based ABR framework specifically designed to enhance the generalization of video streaming. BETA consists of two core modules: spatial and temporal, which jointly tackle the above-mentioned challenge: Spatial Module: Our measurement study (Section II) shows that none of the ABR algorithms trained using the conventional DRL approaches [12], [13], [14], [15], [16], [17] consistently maintain high performance across all network conditions. In particular, all the measured algorithms fail in 8.1% to 17.1% of the evaluated traces, significantly degrading the overall results. Additionally, the specific traces where underperformance occurs differ greatly depending on the specific DRL method adopted. To address this issue, BETA incorporates a spatial module. It begins by training a basic ABR model and benchmarks its QoE against the offline optimal performance per streaming ses- sion. This process helps identify the underperforming network conditions, from which the corresponding network features are extracted, and then are used to predict the potential network conditions that might cause poor performance in the future. BETA proceeds to train specialized ABR models specifically tailored to these challenging network conditions. Temporal Module: We observed that the existing DRL- trained ABR algorithms are often short-sighted, focusing only on single-step future planning. This is due to their training approach, where each epoch updates the model based solely on the immediate reward of short-term feedback. This is ill- suited for the video streaming contexts that require consecutive decision-making across all the vid

**[Entrenamiento / optimización | extracto 7 | p.2]**

3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30]. Specifi- cally,themodelinputcomprisesfivecategoriesofenvironmental states: (i) the measured throughput of the past 8 segments, (ii) the download durations of the past 8 segments, (iii) the bitrate of the most recently downloaded segment, (iv) the current buffer occupancy, and (v) the number of remaining segments in the current streaming session. The first two inputs are processed via convolutional neural networks (CNNs) with 128 filters, while the remaining three are fed into fully connected (dense) layers with 128 neurons. Then the outputs are subsequently merged through a dense aggregation layer comprising 256 neurons. The output layer offers the discrete bitrate level, which serves as the decision action. All the six DRL methods are trained using the Adam optimizer, with training hyperparameters (e.g., learning rate, batch size, experience replay buffer) individually tuned. Streaming Environment: To emulate the realistic streaming environment, we built an open-source ABR emulator [32] based on the previous work by Mao et al. [10], applying custom modi- fications to accommodate our experimental setup. For example, each streaming session emulates the playback of a 192-second video, partitioned into 48 segments of 4 seconds each. Every segment is encoded into eight bitrate levels: {0.2, 0.8, 2.2, 5.0, 10.0, 18.0, 32.0, 50.0} Mbps, reflecting a wide range of encoding options. The network condition is emulated using TCP throughput traces, with an average bandwidth of 17.66 Mbps and a peak Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplo

**[Entrenamiento / optimización | extracto 8 | p.2]**

ally, the specific traces where underperformance occurs differ greatly depending on the specific DRL method adopted. To address this issue, BETA incorporates a spatial module. It begins by training a basic ABR model and benchmarks its QoE against the offline optimal performance per streaming ses- sion. This process helps identify the underperforming network conditions, from which the corresponding network features are extracted, and then are used to predict the potential network conditions that might cause poor performance in the future. BETA proceeds to train specialized ABR models specifically tailored to these challenging network conditions. Temporal Module: We observed that the existing DRL- trained ABR algorithms are often short-sighted, focusing only on single-step future planning. This is due to their training approach, where each epoch updates the model based solely on the immediate reward of short-term feedback. This is ill- suited for the video streaming contexts that require consecutive decision-making across all the video segments in each streaming session. BETA addresses this issue with a temporal module. BETA samples multi-segment decision sequences during training, each consisting of a series of state-action-reward tuples. For each sequence, a discounted actual reward encompassing all the seg- ments is calculated, along with an expected reward based on the initial and final states of each sequence. Both of the rewards are then used to update the neuron weights by minimizing the gap between them. This approach enables the trained ABR model to make far-sighted decisions, thereby ensuring more stable QoE. Extensive evaluation using large-scale network trace dataset

**[Entrenamiento / optimización | extracto 9 | p.2]**

[28], [29], [30]. Specifi- cally,themodelinputcomprisesfivecategoriesofenvironmental states: (i) the measured throughput of the past 8 segments, (ii) the download durations of the past 8 segments, (iii) the bitrate of the most recently downloaded segment, (iv) the current buffer occupancy, and (v) the number of remaining segments in the current streaming session. The first two inputs are processed via convolutional neural networks (CNNs) with 128 filters, while the remaining three are fed into fully connected (dense) layers with 128 neurons. Then the outputs are subsequently merged through a dense aggregation layer comprising 256 neurons. The output layer offers the discrete bitrate level, which serves as the decision action. All the six DRL methods are trained using the Adam optimizer, with training hyperparameters (e.g., learning rate, batch size, experience replay buffer) individually tuned. Streaming Environment: To emulate the realistic streaming environment, we built an open-source ABR emulator [32] based on the previous work by Mao et al. [10], applying custom modi- fications to accommodate our experimental setup. For example, each streaming session emulates the playback of a 192-second video, partitioned into 48 segments of 4 seconds each. Every segment is encoded into eight bitrate levels: {0.2, 0.8, 2.2, 5.0, 10.0, 18.0, 32.0, 50.0} Mbps, reflecting a wide range of encoding options. The network condition is emulated using TCP throughput traces, with an average bandwidth of 17.66 Mbps and a peak Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

**[Entrenamiento / optimización | extracto 10 | p.2]**

e gap between them. This approach enables the trained ABR model to make far-sighted decisions, thereby ensuring more stable QoE. Extensive evaluation using large-scale network trace datasets demonstrates the effectiveness of BETA. Compared to state-of- the-art ABR algorithms, BETA improves average QoE by 19.4% to 50.9%, with gains reaching 244.1% in highly variable network conditions. For the internal QoE metrics, BETA achieves a 7.9% increase in video quality and a 98.3% reduction in rebuffering events. These benefits are attributed to BETA’s flexible bitrate decisions, which not only better match the network dynamics but also fully utilize available network resources. In summary, our contributions are three-fold: Large-Scale Measurement Study: We systematically evalu- ated ABR algorithms trained by six well-known DRL methods, A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17], clearly revealing the impact of the ABR Under- Generalization problem (Section II). Design of BETA: We presented BETA, a DRL-based ABR framework integrating spatial and temporal modules to enhance generalization. The implementation of BETA has been open- sourced on GitHub [32] to support reproducibility and future research (Section III). Comprehensive Evaluation: Through extensive evaluations, we show that BETA significantly outperforms the state-of-the- art ABR algorithms. In addition, we investigated the underlying reasons for its effectiveness (Section IV). II. ABR UNDER-GENERALIZATION Existing learning-based ABR algorithms [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30] (will be comprehensively reviewed in Section V) predominantly rely on advanced DRL

**[Entrenamiento / optimización | extracto 11 | p.2]**

imizing the gap between them. This approach enables the trained ABR model to make far-sighted decisions, thereby ensuring more stable QoE. Extensive evaluation using large-scale network trace datasets demonstrates the effectiveness of BETA. Compared to state-of- the-art ABR algorithms, BETA improves average QoE by 19.4% to 50.9%, with gains reaching 244.1% in highly variable network conditions. For the internal QoE metrics, BETA achieves a 7.9% increase in video quality and a 98.3% reduction in rebuffering events. These benefits are attributed to BETA’s flexible bitrate decisions, which not only better match the network dynamics but also fully utilize available network resources. In summary, our contributions are three-fold: Large-Scale Measurement Study: We systematically evalu- ated ABR algorithms trained by six well-known DRL methods, A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17], clearly revealing the impact of the ABR Under- Generalization problem (Section II). Design of BETA: We presented BETA, a DRL-based ABR framework integrating spatial and temporal modules to enhance generalization. The implementation of BETA has been open- sourced on GitHub [32] to support reproducibility and future research (Section III). Comprehensive Evaluation: Through extensive evaluations, we show that BETA significantly outperforms the state-of-the- art ABR algorithms. In addition, we investigated the underlying reasons for its effectiveness (Section IV). II. ABR UNDER-GENERALIZATION Existing learning-based ABR algorithms [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30] (will be comprehensively reviewed in Section V) predominantly rely on ad

**[Entrenamiento / optimización | extracto 12 | p.2]**

ch enables the trained ABR model to make far-sighted decisions, thereby ensuring more stable QoE. Extensive evaluation using large-scale network trace datasets demonstrates the effectiveness of BETA. Compared to state-of- the-art ABR algorithms, BETA improves average QoE by 19.4% to 50.9%, with gains reaching 244.1% in highly variable network conditions. For the internal QoE metrics, BETA achieves a 7.9% increase in video quality and a 98.3% reduction in rebuffering events. These benefits are attributed to BETA’s flexible bitrate decisions, which not only better match the network dynamics but also fully utilize available network resources. In summary, our contributions are three-fold: Large-Scale Measurement Study: We systematically evalu- ated ABR algorithms trained by six well-known DRL methods, A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17], clearly revealing the impact of the ABR Under- Generalization problem (Section II). Design of BETA: We presented BETA, a DRL-based ABR framework integrating spatial and temporal modules to enhance generalization. The implementation of BETA has been open- sourced on GitHub [32] to support reproducibility and future research (Section III). Comprehensive Evaluation: Through extensive evaluations, we show that BETA significantly outperforms the state-of-the- art ABR algorithms. In addition, we investigated the underlying reasons for its effectiveness (Section IV). II. ABR UNDER-GENERALIZATION Existing learning-based ABR algorithms [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30] (will be comprehensively reviewed in Section V) predominantly rely on advanced DRL techniques [12], [13], [14], [

**[Entrenamiento / optimización | extracto 13 | p.2]**

[30]. Specifi- cally,themodelinputcomprisesfivecategoriesofenvironmental states: (i) the measured throughput of the past 8 segments, (ii) the download durations of the past 8 segments, (iii) the bitrate of the most recently downloaded segment, (iv) the current buffer occupancy, and (v) the number of remaining segments in the current streaming session. The first two inputs are processed via convolutional neural networks (CNNs) with 128 filters, while the remaining three are fed into fully connected (dense) layers with 128 neurons. Then the outputs are subsequently merged through a dense aggregation layer comprising 256 neurons. The output layer offers the discrete bitrate level, which serves as the decision action. All the six DRL methods are trained using the Adam optimizer, with training hyperparameters (e.g., learning rate, batch size, experience replay buffer) individually tuned. Streaming Environment: To emulate the realistic streaming environment, we built an open-source ABR emulator [32] based on the previous work by Mao et al. [10], applying custom modi- fications to accommodate our experimental setup. For example, each streaming session emulates the playback of a 192-second video, partitioned into 48 segments of 4 seconds each. Every segment is encoded into eight bitrate levels: {0.2, 0.8, 2.2, 5.0, 10.0, 18.0, 32.0, 50.0} Mbps, reflecting a wide range of encoding options. The network condition is emulated using TCP throughput traces, with an average bandwidth of 17.66 Mbps and a peak Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

**[Entrenamiento / optimización | extracto 14 | p.3]**

12854 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025 TABLE I COMPARISON OF QOE AND STREAMING PERFORMANCE OVER SIX DRL-BASED ABR ALGORITHMS value of up to 131.44 Mbps. These traces were collected from real-world cellular networks, including 3G, 4G, 5G, and Wi- Fi, over a continuous 77-day period. The data collection was conducted across four types of geographic locations: subways, campuses, shopping malls, and homes. The complete dataset has been made publicly available on GitHub [36]. In this evaluation, 80% of the data is used for model training, and the remaining 20% is reserved for online testing. Both the training and testing sets comprehensively cover the three network types, the four geographic locations, and all the time periods in one day. For the streaming performance metric, we adopted an existing QoE function proposed by Mao et al. [10]: QoE = N−1  t=0 F(bt) −σ × N−1  t=0 θt − N−2  t=0 |F(bt+1) −F(bt)| (1) where the first term of Eq. (1) denotes the video quality utility, and the last two denote the penalties for playback rebuffering (coefficient σ = 50) and video quality variation respectively. Specifically, bt is the video bitrate of segment t, θt is the rebuffering duration in downloading segment t, F(.) denotes the mapping from bitrate to video quality where we adopted linear mapping F(bt) = bt [10] in this evaluation. Results Analysis: Table I summarizes the

**[Entrenamiento / optimización | extracto 15 | p.3]**

oE of 577.3, which is significantly lower than both the offline optimal (1574.0) and the result achieved by TD3 (1405.9). This underperformance is primarily due to its conservative bitrate selection, i.e., PPO chooses bitrates substantially below the available throughput, leading to inefficient utilization of network resources. Conversely, in Sample 2, PPO achieves a QoE of 327.2, which, although still below the offline optimal (685.0), is markedly superior to that of TD3 (–31.1). This improvement is largely attributable to PPO’s effective avoidance of playback rebuffering events, as the rebuffering duration approaches zero. From the above results, several important insights emerge. While the DRL-based ABR algorithms can perform adequately under their intended network conditions, the effectiveness de- grades considerably in others. This limitation stems from their Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

**[Entrenamiento / optimización | extracto 16 | p.3]**

o representative streaming sessions and visualized their performance in Fig. 1(a) and (b). In Sample 1 (Fig. 1(a)), TD3 exhibits effective bitrate adaptation, resulting in a high QoE score of 1405.9, which is close to the offline optimal of 1574.0. By contrast, in Sample 2 (Fig. 1(b)), TD3 fails to adapt appropriately to dynamic network conditions, leading to a significant rebuffering event. Specifically, at the 30th segment, the available throughput drops sharply, yet the selected bitrate remains high, rapidly depleting the playback buffer and causing an 8.9-second rebuffering event. This results inaseverelydegradedQoEof–31.1,farbelowthecorresponding offline optimal of 685.0. Although TD3 achieves the highest overall QoE, it performs suboptimally in terms of rebuffering duration and quality varia- tion, as shown in Table I. In contrast, PPO yields the best results for these two metrics. To this end, we applied PPO to the same two streaming sessions (i.e., Sample 1 and Sample 2) and visual- ized the streaming performance in Fig. 1(c) and (d), respectively. Interestingly, PPO exhibits a markedly different adaptation be- havior compared to TD3. In Sample 1, PPO achieves a QoE of 577.3, which is significantly lower than both the offline optimal (1574.0) and the result achieved by TD3 (1405.9). This underperformance is primarily due to its conservative bitrate selection, i.e., PPO chooses bitrates substantially below the available throughput, leading to inefficient utilization of network resources. Conversely, in Sample 2, PPO achieves a QoE of 327.2, which, although still below the offline optimal (685.0), is markedly superior to that of TD3 (–31.1). This improvement is largely

### 5.x Datos / trazas / datasets

**[Datos / trazas / datasets | extracto 1 | p.1]**

12852 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025 A Novel Spatial-Temporal Learning Method for Enhancing Generalization in Adaptive Video Streaming Guanghui Zhang , Ziming Wang , Huaren Wei, Mengbai Xiao , Hui Yuan , Senior Member, IEEE, Dongxiao Yu , Senior Member, IEEE, and Xiuzhen Cheng , Fellow, IEEE Abstract—Adaptive video streaming has become a fundamental technology for video delivery. With the rise of deep reinforcement learning (DRL), streaming vendors are increasingly adopting DRL- driven adaptive bitrate (ABR) algorithms. In real-world deploy- ments, most ABR approaches are developed with the aim of main- taining good performance across a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yield

**[Datos / trazas / datasets | extracto 2 | p.1]**

ming. Smooth playback relies on stable and consistent network throughput, which is difficult to main- tain in such dynamic environments. To tackle this issue, the streaming vendors have turned their attention to adaptive bitrate (ABR) algorithms, aiming to alleviate the negative effects of the throughput fluctuations. These ABR algorithms are typically im- plemented under the DASH protocol [2]. Their key component is an adaptive logic, which intelligently adjusts video quality in real time (by selecting appropriate bitrates) based on several streaming metrics such as historical throughput measurements and current buffer status. The objective is to enhance the viewer’s Quality of Experience (QoE). Most ABR algorithms are developed with the intention to perform reliably across the wide network environments of any size and shape, e.g., from 3G networks with peak band- widths of a few Mbps to 5G networks offering mean band- widths of 100+ Mbps. However, real-world experiments con- sistently demonstrate that the existing ABR algorithms, while effective under intended network conditions, suffer significant degradation when the network conditions vary widely [3], [4], [5], [6], [11]. This phenomenon, i.e., the operational range of an ABR algorithm is narrow, leads to a marked decrease in the overall performance. We defined this problem as “ABR Under-Generalization”. The existing ABR algorithms can be generally divided into two major categories: heuristic-based and learning-based. The former [5], [6], [7], [8], [9], [19], [20], [21] rely on pre-programmed ABR model with fixed control rules, which inherently limits their adaptability to generalize the varying network environments. C

**[Datos / trazas / datasets | extracto 3 | p.1]**

t network throughput, which is difficult to main- tain in such dynamic environments. To tackle this issue, the streaming vendors have turned their attention to adaptive bitrate (ABR) algorithms, aiming to alleviate the negative effects of the throughput fluctuations. These ABR algorithms are typically im- plemented under the DASH protocol [2]. Their key component is an adaptive logic, which intelligently adjusts video quality in real time (by selecting appropriate bitrates) based on several streaming metrics such as historical throughput measurements and current buffer status. The objective is to enhance the viewer’s Quality of Experience (QoE). Most ABR algorithms are developed with the intention to perform reliably across the wide network environments of any size and shape, e.g., from 3G networks with peak band- widths of a few Mbps to 5G networks offering mean band- widths of 100+ Mbps. However, real-world experiments con- sistently demonstrate that the existing ABR algorithms, while effective under intended network conditions, suffer significant degradation when the network conditions vary widely [3], [4], [5], [6], [11]. This phenomenon, i.e., the operational range of an ABR algorithm is narrow, leads to a marked decrease in the overall performance. We defined this problem as “ABR Under-Generalization”. The existing ABR algorithms can be generally divided into two major categories: heuristic-based and learning-based. The former [5], [6], [7], [8], [9], [19], [20], [21] rely on pre-programmed ABR model with fixed control rules, which inherently limits their adaptability to generalize the varying network environments. Consequently, the heuristic-based algorithms have gra

**[Datos / trazas / datasets | extracto 4 | p.1]**

ns, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yielding average QoE gains of 19.4% to 50.9%,andachievingimprovementsofupto244.1%underseverely fluctuating network conditions. Index Terms—Video streaming, mobile network, deep reinforcement learning, quality-of-experience. I. INTRODUCTION I N RECENT years, video streaming has witnessed rapid expansion, emerging as one of the primary applications of the Received 9 December 2024; revised 26 June 2025; accepted 3 July 2025. Date of publication 15 July 2025; date of current version 5 November 2025. This work was supported by the National Natural Science Foundation of China under Grant 62302268, in part by the Natural Science Foundation of Shandong Province under Grant 2023HWYQ-045 and Grant ZR2023QF060, in part by Qingdao Natural Science Foundation under Grant 23-2-1-127-zyyd-jch, and in part by the Taishan Scholar Project of Shandong Province under Grant tsqn202312051. An earlier version of this paper was presented in part at the IEEE International Conference on Sensing, Communicat

**[Datos / trazas / datasets | extracto 5 | p.2]**

h epoch updates the model based solely on the immediate reward of short-term feedback. This is ill- suited for the video streaming contexts that require consecutive decision-making across all the video segments in each streaming session. BETA addresses this issue with a temporal module. BETA samples multi-segment decision sequences during training, each consisting of a series of state-action-reward tuples. For each sequence, a discounted actual reward encompassing all the seg- ments is calculated, along with an expected reward based on the initial and final states of each sequence. Both of the rewards are then used to update the neuron weights by minimizing the gap between them. This approach enables the trained ABR model to make far-sighted decisions, thereby ensuring more stable QoE. Extensive evaluation using large-scale network trace datasets demonstrates the effectiveness of BETA. Compared to state-of- the-art ABR algorithms, BETA improves average QoE by 19.4% to 50.9%, with gains reaching 244.1% in highly variable network conditions. For the internal QoE metrics, BETA achieves a 7.9% increase in video quality and a 98.3% reduction in rebuffering events. These benefits are attributed to BETA’s flexible bitrate decisions, which not only better match the network dynamics but also fully utilize available network resources. In summary, our contributions are three-fold: Large-Scale Measurement Study: We systematically evalu- ated ABR algorithms trained by six well-known DRL methods, A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17], clearly revealing the impact of the ABR Under- Generalization problem (Section II). Design of BETA: We presented BETA, a DRL-based ABR

**[Datos / trazas / datasets | extracto 6 | p.2]**

ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING 12853 However, our measurement study (refer to Section II) reveals that when faced with a wide range of network conditions, even extensively trained DRL-based ABR algorithms can only achieve 43.1% ∼48.9% of the maximum possible QoE, far below the offline optimal 100%. This highlights the problem of ABR Under-Generalization, which contradicts the theoretical expectation that training on large-scale real traces should yield generalizable ABR policies. The root cause appears to lie in the direct application of the generic DRL techniques [12], [13], [14], [15], [16], [17], which fail to capture all the key features required to adapt across different environments. Motivated by this challenge, we proposed BETA, a new DRL-based ABR framework specifically designed to enhance the generalization of video streaming. BETA consists of two core modules: spatial and temporal, which jointly tackle the above-mentioned challenge: Spatial Module: Our measurement study (Section II) shows that none of the ABR algorithms trained using the conventional DRL approaches [12], [13], [14], [15], [16], [17] consistently maintain high performance across all network conditions. In particular, all the measured algorithms fail in 8.1% to 17.1% of the evaluated traces, signi

**[Datos / trazas / datasets | extracto 7 | p.2]**

le real traces should yield generalizable ABR policies. The root cause appears to lie in the direct application of the generic DRL techniques [12], [13], [14], [15], [16], [17], which fail to capture all the key features required to adapt across different environments. Motivated by this challenge, we proposed BETA, a new DRL-based ABR framework specifically designed to enhance the generalization of video streaming. BETA consists of two core modules: spatial and temporal, which jointly tackle the above-mentioned challenge: Spatial Module: Our measurement study (Section II) shows that none of the ABR algorithms trained using the conventional DRL approaches [12], [13], [14], [15], [16], [17] consistently maintain high performance across all network conditions. In particular, all the measured algorithms fail in 8.1% to 17.1% of the evaluated traces, significantly degrading the overall results. Additionally, the specific traces where underperformance occurs differ greatly depending on the specific DRL method adopted. To address this issue, BETA incorporates a spatial module. It begins by training a basic ABR model and benchmarks its QoE against the offline optimal performance per streaming ses- sion. This process helps identify the underperforming network conditions, from which the corresponding network features are extracted, and then are used to predict the potential network conditions that might cause poor performance in the future. BETA proceeds to train specialized ABR models specifically tailored to these challenging network conditions. Temporal Module: We observed that the existing DRL- trained ABR algorithms are often short-sighted, focusing only on single-step future planni

**[Datos / trazas / datasets | extracto 8 | p.2]**

ing. To demonstrate the ABR Under-Generalization problem, we conducted a measurement study evaluating the ABRalgorithms trainedusingsixwidelyadoptedDRLmethods: A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17]. DRL Configuration. The neural network architecture adheres to the established designs from prior literature [3], [4], [10], [11], [18], [22], [23], [24], [25], [26], [27], [28], [29], [30]. Specifi- cally,themodelinputcomprisesfivecategoriesofenvironmental states: (i) the measured throughput of the past 8 segments, (ii) the download durations of the past 8 segments, (iii) the bitrate of the most recently downloaded segment, (iv) the current buffer occupancy, and (v) the number of remaining segments in the current streaming session. The first two inputs are processed via convolutional neural networks (CNNs) with 128 filters, while the remaining three are fed into fully connected (dense) layers with 128 neurons. Then the outputs are subsequently merged through a dense aggregation layer comprising 256 neurons. The output layer offers the discrete bitrate level, which serves as the decision action. All the six DRL methods are trained using the Adam optimizer, with training hyperparameters (e.g., learning rate, batch size, experience replay buffer) individually tuned. Streaming Environment: To emulate the realistic streaming environment, we built an open-source ABR emulator [32] based on the previous work by Mao et al. [10], applying custom modi- fications to accommodate our experimental setup. For example, each streaming session emulates the playback of a 192-second video, partitioned into 48 segments of 4 seconds each. Every segment is encoded into eight bi

**[Datos / trazas / datasets | extracto 9 | p.2]**

ANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING 12853 However, our measurement study (refer to Section II) reveals that when faced with a wide range of network conditions, even extensively trained DRL-based ABR algorithms can only achieve 43.1% ∼48.9% of the maximum possible QoE, far below the offline optimal 100%. This highlights the problem of ABR Under-Generalization, which contradicts the theoretical expectation that training on large-scale real traces should yield generalizable ABR policies. The root cause appears to lie in the direct application of the generic DRL techniques [12], [13], [14], [15], [16], [17], which fail to capture all the key features required to adapt across different environments. Motivated by this challenge, we proposed BETA, a new DRL-based ABR framework specifically designed to enhance the generalization of video streaming. BETA consists of two core modules: spatial and temporal, which jointly tackle the above-mentioned challenge: Spatial Module: Our measurement study (Section II) shows that none of the ABR algorithms trained using the conventional DRL approaches [12], [13], [14], [15], [16], [17] consistently maintain high performance across all network conditions. In particular, all the measured algorithms fail in 8.1% to 17.1% of the evaluated traces, significantly degrading the overall results. Additionally, the specific traces where underperformance occurs differ greatly depending on the specific DRL method adopted. To address this issue, BETA incorporates a spatial module. It begins by training a basic ABR model and benchmarks its QoE against the offline optimal performance per streaming ses- sion. This process helps identify the underperfo

**[Datos / trazas / datasets | extracto 10 | p.3]**

12854 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025 TABLE I COMPARISON OF QOE AND STREAMING PERFORMANCE OVER SIX DRL-BASED ABR ALGORITHMS value of up to 131.44 Mbps. These traces were collected from real-world cellular networks, including 3G, 4G, 5G, and Wi- Fi, over a continuous 77-day period. The data collection was conducted across four types of geographic locations: subways, campuses, shopping malls, and homes. The complete dataset has been made publicly available on GitHub [36]. In this evaluation, 80% of the data is used for model training, and the remaining 20% is reserved for online testing. Both the training and testing sets comprehensively cover the three network types, the four geographic locations, and all the time periods in one day. For the streaming performance metric, we adopted an existing QoE function proposed by Mao et al. [10]: QoE = N−1  t=0 F(bt) −σ × N−1  t=0 θt − N−2  t=0 |F(bt+1) −F(bt)| (1) where the first term of Eq. (1) denotes the video quality utility, and the last two denote the penalties for playback rebuffering (coefficient σ = 50) and video quality variation respectively. Specifically, bt is the video bitrate of segment t, θt is the rebuffering duration in downloading segment t, F(.) denotes the mapping from bitrate to video quality

**[Datos / trazas / datasets | extracto 11 | p.3]**

ALGORITHMS value of up to 131.44 Mbps. These traces were collected from real-world cellular networks, including 3G, 4G, 5G, and Wi- Fi, over a continuous 77-day period. The data collection was conducted across four types of geographic locations: subways, campuses, shopping malls, and homes. The complete dataset has been made publicly available on GitHub [36]. In this evaluation, 80% of the data is used for model training, and the remaining 20% is reserved for online testing. Both the training and testing sets comprehensively cover the three network types, the four geographic locations, and all the time periods in one day. For the streaming performance metric, we adopted an existing QoE function proposed by Mao et al. [10]: QoE = N−1  t=0 F(bt) −σ × N−1  t=0 θt − N−2  t=0 |F(bt+1) −F(bt)| (1) where the first term of Eq. (1) denotes the video quality utility, and the last two denote the penalties for playback rebuffering (coefficient σ = 50) and video quality variation respectively. Specifically, bt is the video bitrate of segment t, θt is the rebuffering duration in downloading segment t, F(.) denotes the mapping from bitrate to video quality where we adopted linear mapping F(bt) = bt [10] in this evaluation. Results Analysis: Table I summarizes the performance of the six DRL-based ABR algorithms. QoE is reported using two representations: the absolute QoE score (denoted as A-QoE) and the normalized QoE score (denoted as N-QoE). The normalized score is obtained by dividing the absolute score by the offline optimal. The optimal QoE serves as the theoretical upper bound, which is computed based on dynamic programming, using an omniscient policy with perfect foresight of future

**[Datos / trazas / datasets | extracto 12 | p.4]**

optimum, δ is the QoE gap (δ is set to 700. Note that this setting is to reflect the large gap between the actual QoE and the offline optimal. A sensitivity analysis is performed in Section IV-E), symbol |. | calculates the element number of the set, J is the total session number (denominator), and ε is the output proportion. Table II presents the results of the under-performing propor- tion across all six DRL-based ABR algorithms. The observed values are non-negligible, ranging from 8.1% to 17.1%. Given the pre-defined QoE gap δ = 700, such a high proportion of poorly performing sessions substantially degrades the overall QoE. We hypothesize that this suboptimality stems from the direct application of conventional DRL methods [12], [13], [14], [15], [16], [17] to the ABR task. Despite extensive training on large-scale real-world network traces, these DRL methods fail to fully capture the critical features necessary for robust perfor- mance across diverse network environments. This problem is particularly problematic in practice, where streaming services must operate across a wide spectrum of network conditions, ranging from low-capacity 3G networks to high-speed 5G envi- ronments. Without addressing the generalization deficiency, the performance of the DRL-based ABR algorithms will inevitably be constrained by their limited adaptability, ultimately becoming a bottleneck in real-world deployment scenarios. III. METHODOLOGY Building upon the insights derived in Section II, we proposed BETA, a new DRL-based framework designed to address the ABR Under-Generalization problem. The overall description of BETA is presented in Section III-A, followed by the details of its two key modu

**[Datos / trazas / datasets | extracto 13 | p.4]**

followed by the details of its two key modules in Sections III-B and Section III-C, respectively. A. BETA Overall Fig. 2 plots the overall architecture of BETA, which comprises twoprimarymodules:SpatialandTemporal.TheSpatialModule serves as the master routine, while the Temporal Module is a sub-routine that is periodically invoked by the Spatial Module. Spatial Module: As shown in the measurement study in Section II, ABR algorithms trained with the state-of-the-art DRL methods [12], [13], [14], [15], [16], [17] only achieve 43.1% to 48.9% of the optimal QoE, primarily due to the severe underperformance in 8.1% to 17.1% of the streaming sessions. To address this issue, BETA introduces the Spatial Module. Specifically, BETA initially invokes the Temporal Module to train a base ABR model, which is then evaluated across all training network traces by comparing the achieved QoE with the corresponding offline optimum. Based on this evaluation, the training traces are partitioned into two subsets: one where the ABR model performs adequately, and the other where it fails to generalize well. From these labeled traces, BETA extracts in- ternal network features to train a classifier that predicts whether a given network trace is likely to result in underperformance. This classifier enables BETA to dynamically distinguish between “normal” and “difficult” traces in real-time. Accordingly, two complementary ABR models are trained for each trace subset by invoking the Temporal Module, and during online stream- ing, BETA dynamically selects the appropriate logic to better Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Re

**[Datos / trazas / datasets | extracto 14 | p.4]**

he output proportion. Table II presents the results of the under-performing propor- tion across all six DRL-based ABR algorithms. The observed values are non-negligible, ranging from 8.1% to 17.1%. Given the pre-defined QoE gap δ = 700, such a high proportion of poorly performing sessions substantially degrades the overall QoE. We hypothesize that this suboptimality stems from the direct application of conventional DRL methods [12], [13], [14], [15], [16], [17] to the ABR task. Despite extensive training on large-scale real-world network traces, these DRL methods fail to fully capture the critical features necessary for robust perfor- mance across diverse network environments. This problem is particularly problematic in practice, where streaming services must operate across a wide spectrum of network conditions, ranging from low-capacity 3G networks to high-speed 5G envi- ronments. Without addressing the generalization deficiency, the performance of the DRL-based ABR algorithms will inevitably be constrained by their limited adaptability, ultimately becoming a bottleneck in real-world deployment scenarios. III. METHODOLOGY Building upon the insights derived in Section II, we proposed BETA, a new DRL-based framework designed to address the ABR Under-Generalization problem. The overall description of BETA is presented in Section III-A, followed by the details of its two key modules in Sections III-B and Section III-C, respectively. A. BETA Overall Fig. 2 plots the overall architecture of BETA, which comprises twoprimarymodules:SpatialandTemporal.TheSpatialModule serves as the master routine, while the Temporal Module is a sub-routine that is periodically invoked by the Spatia

**[Datos / trazas / datasets | extracto 15 | p.4]**

e II presents the results of the under-performing propor- tion across all six DRL-based ABR algorithms. The observed values are non-negligible, ranging from 8.1% to 17.1%. Given the pre-defined QoE gap δ = 700, such a high proportion of poorly performing sessions substantially degrades the overall QoE. We hypothesize that this suboptimality stems from the direct application of conventional DRL methods [12], [13], [14], [15], [16], [17] to the ABR task. Despite extensive training on large-scale real-world network traces, these DRL methods fail to fully capture the critical features necessary for robust perfor- mance across diverse network environments. This problem is particularly problematic in practice, where streaming services must operate across a wide spectrum of network conditions, ranging from low-capacity 3G networks to high-speed 5G envi- ronments. Without addressing the generalization deficiency, the performance of the DRL-based ABR algorithms will inevitably be constrained by their limited adaptability, ultimately becoming a bottleneck in real-world deployment scenarios. III. METHODOLOGY Building upon the insights derived in Section II, we proposed BETA, a new DRL-based framework designed to address the ABR Under-Generalization problem. The overall description of BETA is presented in Section III-A, followed by the details of its two key modules in Sections III-B and Section III-C, respectively. A. BETA Overall Fig. 2 plots the overall architecture of BETA, which comprises twoprimarymodules:SpatialandTemporal.TheSpatialModule serves as the master routine, while the Temporal Module is a sub-routine that is periodically invoked by the Spatial Module. Spatial Module:

**[Datos / trazas / datasets | extracto 16 | p.4]**

ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING 12855 Fig. 1. Per-session streaming performance (the x-axis – segment index, with the width of each segment scaled by its playback time). TABLE II THE PROPORTION OF UNDERPERFORMED STREAMING SESSIONS lack of generalization capability across diverse network condi- tions (i.e., the problem “ABR Under-Generalization” described in Section I). To further quantify this problem, we introduce a metric that captures the proportion of streaming sessions in which a DRL-based ABR method yields QoE significantly below the offline optimal. Specifically, we define this proportion as follows: ε = |{κj |oj −rj > δ, j = 0, 1, . . . , J −1}| J (2) where rj is the achieved QoE of session j, oj is the corresponding optimum, δ is the QoE gap (δ is set to 700. Note that this setting is to reflect the large gap between the actual QoE and the offline op

### 5.x Evaluación / baselines / experimentos

**[Evaluación / baselines / experimentos | extracto 1 | p.1]**

l find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each training epoch, enabling the trained model to account for long-term environmental dynamics. Comprehensive evaluations show that BETA outperforms state-of- the-art ABR algorithms, yielding average QoE gains of 19.4% to 50.9%,andachievingimprovementsofupto244.1%underseverely fluctuating network conditions. Index Terms—Video streaming, mobile network, deep reinforcement learning, quality-of-experience. I. INTRODUCTION I N RECENT years, video streaming has witnessed rapid expansion, emerging as one of the primary applications of the Received 9 December 2024; revised 26 June 2025; accepted 3 July 2025. Date of publication 15 July 2025; date of current version 5 November 2025. This work was supported by the National Natural Science Foundation of China under Grant 62302268, in part by the Natural Science Foundation of Shandong Province under Grant 2023HWYQ-045 and Grant ZR2023QF060, in part by Qingdao Natural Science Foundation under Grant 23-2-1-127-zyyd-jch

**[Evaluación / baselines / experimentos | extracto 2 | p.1]**

vironments. To tackle this issue, the streaming vendors have turned their attention to adaptive bitrate (ABR) algorithms, aiming to alleviate the negative effects of the throughput fluctuations. These ABR algorithms are typically im- plemented under the DASH protocol [2]. Their key component is an adaptive logic, which intelligently adjusts video quality in real time (by selecting appropriate bitrates) based on several streaming metrics such as historical throughput measurements and current buffer status. The objective is to enhance the viewer’s Quality of Experience (QoE). Most ABR algorithms are developed with the intention to perform reliably across the wide network environments of any size and shape, e.g., from 3G networks with peak band- widths of a few Mbps to 5G networks offering mean band- widths of 100+ Mbps. However, real-world experiments con- sistently demonstrate that the existing ABR algorithms, while effective under intended network conditions, suffer significant degradation when the network conditions vary widely [3], [4], [5], [6], [11]. This phenomenon, i.e., the operational range of an ABR algorithm is narrow, leads to a marked decrease in the overall performance. We defined this problem as “ABR Under-Generalization”. The existing ABR algorithms can be generally divided into two major categories: heuristic-based and learning-based. The former [5], [6], [7], [8], [9], [19], [20], [21] rely on pre-programmed ABR model with fixed control rules, which inherently limits their adaptability to generalize the varying network environments. Consequently, the heuristic-based algorithms have gradually lost favor in recent years. In contrast, the learning-based algorithms, pa

**[Evaluación / baselines / experimentos | extracto 3 | p.1]**

phenomenon, i.e., the operational range of an ABR algorithm is narrow, leads to a marked decrease in the overall performance. We defined this problem as “ABR Under-Generalization”. The existing ABR algorithms can be generally divided into two major categories: heuristic-based and learning-based. The former [5], [6], [7], [8], [9], [19], [20], [21] rely on pre-programmed ABR model with fixed control rules, which inherently limits their adaptability to generalize the varying network environments. Consequently, the heuristic-based algorithms have gradually lost favor in recent years. In contrast, the learning-based algorithms, particularly those powered by deepreinforcementlearning(DRL)[3],[4],[10],[11],[18],[22], [23], [24], [25], [26], [27], [28], [29], [30], have gained attention. They train neural networks using real network trace data, resulting in ABR models that are more flexible than the heuristic counterparts [10]. 1536-1233 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

**[Evaluación / baselines / experimentos | extracto 4 | p.1]**

12852 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025 A Novel Spatial-Temporal Learning Method for Enhancing Generalization in Adaptive Video Streaming Guanghui Zhang , Ziming Wang , Huaren Wei, Mengbai Xiao , Hui Yuan , Senior Member, IEEE, Dongxiao Yu , Senior Member, IEEE, and Xiuzhen Cheng , Fellow, IEEE Abstract—Adaptive video streaming has become a fundamental technology for video delivery. With the rise of deep reinforcement learning (DRL), streaming vendors are increasingly adopting DRL- driven adaptive bitrate (ABR) algorithms. In real-world deploy- ments, most ABR approaches are developed with the aim of main- taining good performance across a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, which falls significantly short of the 100% op- timum. We termed this problem as “ABR Under-Generalization”. To overcome this problem, we introduce BETA – a novel DRL- based ABR framework that incorporates both spatial and temporal learning mechanisms: 1) Spatially, BETA features a detector that flags the network conditions likely to cause poor performance, then trains specialized ABR models tailored for those conditions and 2) Temporally, BETA enhances its learning by incorporating multi-step decision experiences at each train

**[Evaluación / baselines / experimentos | extracto 5 | p.1]**

dynamic environments. To tackle this issue, the streaming vendors have turned their attention to adaptive bitrate (ABR) algorithms, aiming to alleviate the negative effects of the throughput fluctuations. These ABR algorithms are typically im- plemented under the DASH protocol [2]. Their key component is an adaptive logic, which intelligently adjusts video quality in real time (by selecting appropriate bitrates) based on several streaming metrics such as historical throughput measurements and current buffer status. The objective is to enhance the viewer’s Quality of Experience (QoE). Most ABR algorithms are developed with the intention to perform reliably across the wide network environments of any size and shape, e.g., from 3G networks with peak band- widths of a few Mbps to 5G networks offering mean band- widths of 100+ Mbps. However, real-world experiments con- sistently demonstrate that the existing ABR algorithms, while effective under intended network conditions, suffer significant degradation when the network conditions vary widely [3], [4], [5], [6], [11]. This phenomenon, i.e., the operational range of an ABR algorithm is narrow, leads to a marked decrease in the overall performance. We defined this problem as “ABR Under-Generalization”. The existing ABR algorithms can be generally divided into two major categories: heuristic-based and learning-based. The former [5], [6], [7], [8], [9], [19], [20], [21] rely on pre-programmed ABR model with fixed control rules, which inherently limits their adaptability to generalize the varying network environments. Consequently, the heuristic-based algorithms have gradually lost favor in recent years. In contrast, the learning-based alg

**[Evaluación / baselines / experimentos | extracto 6 | p.2]**

s due to their training approach, where each epoch updates the model based solely on the immediate reward of short-term feedback. This is ill- suited for the video streaming contexts that require consecutive decision-making across all the video segments in each streaming session. BETA addresses this issue with a temporal module. BETA samples multi-segment decision sequences during training, each consisting of a series of state-action-reward tuples. For each sequence, a discounted actual reward encompassing all the seg- ments is calculated, along with an expected reward based on the initial and final states of each sequence. Both of the rewards are then used to update the neuron weights by minimizing the gap between them. This approach enables the trained ABR model to make far-sighted decisions, thereby ensuring more stable QoE. Extensive evaluation using large-scale network trace datasets demonstrates the effectiveness of BETA. Compared to state-of- the-art ABR algorithms, BETA improves average QoE by 19.4% to 50.9%, with gains reaching 244.1% in highly variable network conditions. For the internal QoE metrics, BETA achieves a 7.9% increase in video quality and a 98.3% reduction in rebuffering events. These benefits are attributed to BETA’s flexible bitrate decisions, which not only better match the network dynamics but also fully utilize available network resources. In summary, our contributions are three-fold: Large-Scale Measurement Study: We systematically evalu- ated ABR algorithms trained by six well-known DRL methods, A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17], clearly revealing the impact of the ABR Under- Generalization problem (Section II). Design of

**[Evaluación / baselines / experimentos | extracto 7 | p.2]**

ent buffer occupancy, and (v) the number of remaining segments in the current streaming session. The first two inputs are processed via convolutional neural networks (CNNs) with 128 filters, while the remaining three are fed into fully connected (dense) layers with 128 neurons. Then the outputs are subsequently merged through a dense aggregation layer comprising 256 neurons. The output layer offers the discrete bitrate level, which serves as the decision action. All the six DRL methods are trained using the Adam optimizer, with training hyperparameters (e.g., learning rate, batch size, experience replay buffer) individually tuned. Streaming Environment: To emulate the realistic streaming environment, we built an open-source ABR emulator [32] based on the previous work by Mao et al. [10], applying custom modi- fications to accommodate our experimental setup. For example, each streaming session emulates the playback of a 192-second video, partitioned into 48 segments of 4 seconds each. Every segment is encoded into eight bitrate levels: {0.2, 0.8, 2.2, 5.0, 10.0, 18.0, 32.0, 50.0} Mbps, reflecting a wide range of encoding options. The network condition is emulated using TCP throughput traces, with an average bandwidth of 17.66 Mbps and a peak Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

**[Evaluación / baselines / experimentos | extracto 8 | p.2]**

ediate reward of short-term feedback. This is ill- suited for the video streaming contexts that require consecutive decision-making across all the video segments in each streaming session. BETA addresses this issue with a temporal module. BETA samples multi-segment decision sequences during training, each consisting of a series of state-action-reward tuples. For each sequence, a discounted actual reward encompassing all the seg- ments is calculated, along with an expected reward based on the initial and final states of each sequence. Both of the rewards are then used to update the neuron weights by minimizing the gap between them. This approach enables the trained ABR model to make far-sighted decisions, thereby ensuring more stable QoE. Extensive evaluation using large-scale network trace datasets demonstrates the effectiveness of BETA. Compared to state-of- the-art ABR algorithms, BETA improves average QoE by 19.4% to 50.9%, with gains reaching 244.1% in highly variable network conditions. For the internal QoE metrics, BETA achieves a 7.9% increase in video quality and a 98.3% reduction in rebuffering events. These benefits are attributed to BETA’s flexible bitrate decisions, which not only better match the network dynamics but also fully utilize available network resources. In summary, our contributions are three-fold: Large-Scale Measurement Study: We systematically evalu- ated ABR algorithms trained by six well-known DRL methods, A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and SAC [17], clearly revealing the impact of the ABR Under- Generalization problem (Section II). Design of BETA: We presented BETA, a DRL-based ABR framework integrating spatial and temporal modul

**[Evaluación / baselines / experimentos | extracto 9 | p.2]**

R policies. The root cause appears to lie in the direct application of the generic DRL techniques [12], [13], [14], [15], [16], [17], which fail to capture all the key features required to adapt across different environments. Motivated by this challenge, we proposed BETA, a new DRL-based ABR framework specifically designed to enhance the generalization of video streaming. BETA consists of two core modules: spatial and temporal, which jointly tackle the above-mentioned challenge: Spatial Module: Our measurement study (Section II) shows that none of the ABR algorithms trained using the conventional DRL approaches [12], [13], [14], [15], [16], [17] consistently maintain high performance across all network conditions. In particular, all the measured algorithms fail in 8.1% to 17.1% of the evaluated traces, significantly degrading the overall results. Additionally, the specific traces where underperformance occurs differ greatly depending on the specific DRL method adopted. To address this issue, BETA incorporates a spatial module. It begins by training a basic ABR model and benchmarks its QoE against the offline optimal performance per streaming ses- sion. This process helps identify the underperforming network conditions, from which the corresponding network features are extracted, and then are used to predict the potential network conditions that might cause poor performance in the future. BETA proceeds to train specialized ABR models specifically tailored to these challenging network conditions. Temporal Module: We observed that the existing DRL- trained ABR algorithms are often short-sighted, focusing only on single-step future planning. This is due to their training approach,

**[Evaluación / baselines / experimentos | extracto 10 | p.2]**

highlights the problem of ABR Under-Generalization, which contradicts the theoretical expectation that training on large-scale real traces should yield generalizable ABR policies. The root cause appears to lie in the direct application of the generic DRL techniques [12], [13], [14], [15], [16], [17], which fail to capture all the key features required to adapt across different environments. Motivated by this challenge, we proposed BETA, a new DRL-based ABR framework specifically designed to enhance the generalization of video streaming. BETA consists of two core modules: spatial and temporal, which jointly tackle the above-mentioned challenge: Spatial Module: Our measurement study (Section II) shows that none of the ABR algorithms trained using the conventional DRL approaches [12], [13], [14], [15], [16], [17] consistently maintain high performance across all network conditions. In particular, all the measured algorithms fail in 8.1% to 17.1% of the evaluated traces, significantly degrading the overall results. Additionally, the specific traces where underperformance occurs differ greatly depending on the specific DRL method adopted. To address this issue, BETA incorporates a spatial module. It begins by training a basic ABR model and benchmarks its QoE against the offline optimal performance per streaming ses- sion. This process helps identify the underperforming network conditions, from which the corresponding network features are extracted, and then are used to predict the potential network conditions that might cause poor performance in the future. BETA proceeds to train specialized ABR models specifically tailored to these challenging network conditions. Temporal Module: We ob

**[Evaluación / baselines / experimentos | extracto 11 | p.3]**

12854 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025 TABLE I COMPARISON OF QOE AND STREAMING PERFORMANCE OVER SIX DRL-BASED ABR ALGORITHMS value of up to 131.44 Mbps. These traces were collected from real-world cellular networks, including 3G, 4G, 5G, and Wi- Fi, over a continuous 77-day period. The data collection was conducted across four types of geographic locations: subways, campuses, shopping malls, and homes. The complete dataset has been made publicly available on GitHub [36]. In this evaluation, 80% of the data is used for model training, and the remaining 20% is reserved for online testing. Both the training and testing sets comprehensively cover the three network types, the four geographic locations, and all the time periods in one day. For the streaming performance metric, we adopted an existing QoE function proposed by Mao et al. [10]: QoE = N−1  t=0 F(bt) −σ × N−1  t=0 θt − N−2  t=0 |F(bt+1) −F(bt)| (1) where the first term of Eq. (1) denotes the video quality utility, and the last two denote the penalties for playback rebuffering (coefficient σ = 50) and video quality variation respectively. Specifically, bt is the video bitrate of segment t, θt is the rebuffering duration in downloading segment t, F(.) denotes the mapping from bitrate to video quality where we adopted linear mapping F(bt) = bt [10] in this evaluation.

**[Evaluación / baselines / experimentos | extracto 12 | p.3]**

ls to adapt appropriately to dynamic network conditions, leading to a significant rebuffering event. Specifically, at the 30th segment, the available throughput drops sharply, yet the selected bitrate remains high, rapidly depleting the playback buffer and causing an 8.9-second rebuffering event. This results inaseverelydegradedQoEof–31.1,farbelowthecorresponding offline optimal of 685.0. Although TD3 achieves the highest overall QoE, it performs suboptimally in terms of rebuffering duration and quality varia- tion, as shown in Table I. In contrast, PPO yields the best results for these two metrics. To this end, we applied PPO to the same two streaming sessions (i.e., Sample 1 and Sample 2) and visual- ized the streaming performance in Fig. 1(c) and (d), respectively. Interestingly, PPO exhibits a markedly different adaptation be- havior compared to TD3. In Sample 1, PPO achieves a QoE of 577.3, which is significantly lower than both the offline optimal (1574.0) and the result achieved by TD3 (1405.9). This underperformance is primarily due to its conservative bitrate selection, i.e., PPO chooses bitrates substantially below the available throughput, leading to inefficient utilization of network resources. Conversely, in Sample 2, PPO achieves a QoE of 327.2, which, although still below the offline optimal (685.0), is markedly superior to that of TD3 (–31.1). This improvement is largely attributable to PPO’s effective avoidance of playback rebuffering events, as the rebuffering duration approaches zero. From the above results, several important insights emerge. While the DRL-based ABR algorithms can perform adequately under their intended network conditions, the effectiveness de

**[Evaluación / baselines / experimentos | extracto 13 | p.3]**

80% of the data is used for model training, and the remaining 20% is reserved for online testing. Both the training and testing sets comprehensively cover the three network types, the four geographic locations, and all the time periods in one day. For the streaming performance metric, we adopted an existing QoE function proposed by Mao et al. [10]: QoE = N−1  t=0 F(bt) −σ × N−1  t=0 θt − N−2  t=0 |F(bt+1) −F(bt)| (1) where the first term of Eq. (1) denotes the video quality utility, and the last two denote the penalties for playback rebuffering (coefficient σ = 50) and video quality variation respectively. Specifically, bt is the video bitrate of segment t, θt is the rebuffering duration in downloading segment t, F(.) denotes the mapping from bitrate to video quality where we adopted linear mapping F(bt) = bt [10] in this evaluation. Results Analysis: Table I summarizes the performance of the six DRL-based ABR algorithms. QoE is reported using two representations: the absolute QoE score (denoted as A-QoE) and the normalized QoE score (denoted as N-QoE). The normalized score is obtained by dividing the absolute score by the offline optimal. The optimal QoE serves as the theoretical upper bound, which is computed based on dynamic programming, using an omniscient policy with perfect foresight of future network throughput (more details are referred to Spiteri et al. [8], and the implementation is available in [31]). In addition to the QoE, we further evaluated the three core metrics that contribute to QoE: the average video bitrate, total rebuffering duration, and video quality variation. See their definitions in Eq. (1). These metrics collectively characterize the tradeoffs ea

**[Evaluación / baselines / experimentos | extracto 14 | p.3]**

ng, and the remaining 20% is reserved for online testing. Both the training and testing sets comprehensively cover the three network types, the four geographic locations, and all the time periods in one day. For the streaming performance metric, we adopted an existing QoE function proposed by Mao et al. [10]: QoE = N−1  t=0 F(bt) −σ × N−1  t=0 θt − N−2  t=0 |F(bt+1) −F(bt)| (1) where the first term of Eq. (1) denotes the video quality utility, and the last two denote the penalties for playback rebuffering (coefficient σ = 50) and video quality variation respectively. Specifically, bt is the video bitrate of segment t, θt is the rebuffering duration in downloading segment t, F(.) denotes the mapping from bitrate to video quality where we adopted linear mapping F(bt) = bt [10] in this evaluation. Results Analysis: Table I summarizes the performance of the six DRL-based ABR algorithms. QoE is reported using two representations: the absolute QoE score (denoted as A-QoE) and the normalized QoE score (denoted as N-QoE). The normalized score is obtained by dividing the absolute score by the offline optimal. The optimal QoE serves as the theoretical upper bound, which is computed based on dynamic programming, using an omniscient policy with perfect foresight of future network throughput (more details are referred to Spiteri et al. [8], and the implementation is available in [31]). In addition to the QoE, we further evaluated the three core metrics that contribute to QoE: the average video bitrate, total rebuffering duration, and video quality variation. See their definitions in Eq. (1). These metrics collectively characterize the tradeoffs each algorithm makes in adaptive streaming scena

**[Evaluación / baselines / experimentos | extracto 15 | p.4]**

tively. A. BETA Overall Fig. 2 plots the overall architecture of BETA, which comprises twoprimarymodules:SpatialandTemporal.TheSpatialModule serves as the master routine, while the Temporal Module is a sub-routine that is periodically invoked by the Spatial Module. Spatial Module: As shown in the measurement study in Section II, ABR algorithms trained with the state-of-the-art DRL methods [12], [13], [14], [15], [16], [17] only achieve 43.1% to 48.9% of the optimal QoE, primarily due to the severe underperformance in 8.1% to 17.1% of the streaming sessions. To address this issue, BETA introduces the Spatial Module. Specifically, BETA initially invokes the Temporal Module to train a base ABR model, which is then evaluated across all training network traces by comparing the achieved QoE with the corresponding offline optimum. Based on this evaluation, the training traces are partitioned into two subsets: one where the ABR model performs adequately, and the other where it fails to generalize well. From these labeled traces, BETA extracts in- ternal network features to train a classifier that predicts whether a given network trace is likely to result in underperformance. This classifier enables BETA to dynamically distinguish between “normal” and “difficult” traces in real-time. Accordingly, two complementary ABR models are trained for each trace subset by invoking the Temporal Module, and during online stream- ing, BETA dynamically selects the appropriate logic to better Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

**[Evaluación / baselines / experimentos | extracto 16 | p.4]**

of generalization capability across diverse network condi- tions (i.e., the problem “ABR Under-Generalization” described in Section I). To further quantify this problem, we introduce a metric that captures the proportion of streaming sessions in which a DRL-based ABR method yields QoE significantly below the offline optimal. Specifically, we define this proportion as follows: ε = |{κj |oj −rj > δ, j = 0, 1, . . . , J −1}| J (2) where rj is the achieved QoE of session j, oj is the corresponding optimum, δ is the QoE gap (δ is set to 700. Note that this setting is to reflect the large gap between the actual QoE and the offline optimal. A sensitivity analysis is performed in Section IV-E), symbol |. | calculates the element number of the set, J is the total session number (denominator), and ε is the output proportion. Table II presents the results of the under-performing propor- tion across all six DRL-based ABR algorithms. The observed values are non-negligible, ranging from 8.1% to 17.1%. Given the pre-defined QoE gap δ = 700, such a high proportion of poorly performing sessions substantially degrades the overall QoE. We hypothesize that this suboptimality stems from the direct application of conventional DRL methods [12], [13], [14], [15], [16], [17] to the ABR task. Despite extensive training on large-scale real-world network traces, these DRL methods fail to fully capture the critical features necessary for robust perfor- mance across diverse network environments. This problem is particularly problematic in practice, where streaming services must operate across a wide spectrum of network conditions, ranging from low-capacity 3G networks to high-speed 5G envi- ronments. Witho

### 5.x Limitaciones / riesgos / implementación

**[Limitaciones / riesgos / implementación | extracto 1 | p.1]**

12852 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025 A Novel Spatial-Temporal Learning Method for Enhancing Generalization in Adaptive Video Streaming Guanghui Zhang , Ziming Wang , Huaren Wei, Mengbai Xiao , Hui Yuan , Senior Member, IEEE, Dongxiao Yu , Senior Member, IEEE, and Xiuzhen Cheng , Fellow, IEEE Abstract—Adaptive video streaming has become a fundamental technology for video delivery. With the rise of deep reinforcement learning (DRL), streaming vendors are increasingly adopting DRL- driven adaptive bitrate (ABR) algorithms. In real-world deploy- ments, most ABR approaches are developed with the aim of main- taining good performance across a wide variety of network environ- ments. However, contrary to this expectation, our empirical find- ings show that even when trained on extensive real-world network trace data, these DRL-based ABR algorithms achieve only 43.1% to 48.9% of Quality-of-Experience (QoE) under highly diverse network conditions, whic

**[Limitaciones / riesgos / implementación | extracto 2 | p.2]**

ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING 12853 However, our measurement study (refer to Section II) reveals that when faced with a wide range of network conditions, even extensively trained DRL-based ABR algorithms can only achieve 43.1% ∼48.9% of the maximum possible QoE, far below the offline optimal 100%. This highlights the problem of ABR Under-Generalization, which contradicts the theoretical expectation that training on large-scale real traces should yield generalizable ABR policies. The root cause appears to lie in the direct application of the generic DRL techniques [12], [13], [14], [15], [16], [17], which fail to capture all the key features required to adapt across different environments. Motivated by this challenge, we proposed BETA, a new DRL-based ABR framework specifically designed to enhance the generalization of video streaming. BETA

**[Limitaciones / riesgos / implementación | extracto 3 | p.2]**

expectation that training on large-scale real traces should yield generalizable ABR policies. The root cause appears to lie in the direct application of the generic DRL techniques [12], [13], [14], [15], [16], [17], which fail to capture all the key features required to adapt across different environments. Motivated by this challenge, we proposed BETA, a new DRL-based ABR framework specifically designed to enhance the generalization of video streaming. BETA consists of two core modules: spatial and temporal, which jointly tackle the above-mentioned challenge: Spatial Module: Our measurement study (Section II) shows that none of the ABR algorithms trained using the conventional DRL approaches [12], [13], [14], [15], [16], [17] consistently maintain high performance across all network conditions. In particular, all the measured algorithms fail in 8.1% to 17.1% of the evaluated traces, significantly degrading the overall results. Additionally, the specific traces where underperformance occurs differ greatly depending on the specific DRL method adopted. To address this issue, BETA incorporates a spatial module. It begins by training a basic ABR model and benchmarks its QoE against the offline optimal performance per streaming ses- sion. This process helps identify the underperforming network conditions, from which the corresponding network features are extracted, and then are used to predict the potential network conditions that might cause poor performance in the future. BETA proceeds to train specialized ABR models specifically tailored to these challenging network conditions. Temporal Module: We observed that the existing DRL- trained ABR algorithms are often short-sighted, f

**[Limitaciones / riesgos / implementación | extracto 4 | p.2]**

s that when faced with a wide range of network conditions, even extensively trained DRL-based ABR algorithms can only achieve 43.1% ∼48.9% of the maximum possible QoE, far below the offline optimal 100%. This highlights the problem of ABR Under-Generalization, which contradicts the theoretical expectation that training on large-scale real traces should yield generalizable ABR policies. The root cause appears to lie in the direct application of the generic DRL techniques [12], [13], [14], [15], [16], [17], which fail to capture all the key features required to adapt across different environments. Motivated by this challenge, we proposed BETA, a new DRL-based ABR framework specifically designed to enhance the generalization of video streaming. BETA consists of two core modules: spatial and temporal, which jointly tackle the above-mentioned challenge: Spatial Module: Our measurement study (Section II) shows that none of the ABR algorithms trained using the conventional DRL approaches [12], [13], [14], [15], [16], [17] consistently maintain high performance across all network conditions. In particular, all the measured algorithms fail in 8.1% to 17.1% of the evaluated traces, significantly degrading the overall results. Additionally, the specific traces where underperformance occurs differ greatly depending on the specific DRL method adopted. To address this issue, BETA incorporates a spatial module. It begins by training a basic ABR model and benchmarks its QoE against the offline optimal performance per streaming ses- sion. This process helps identify the underperforming network conditions, from which the corresponding network features are extracted, and then are used to predict the

**[Limitaciones / riesgos / implementación | extracto 5 | p.3]**

QoE of 577.3, which is significantly lower than both the offline optimal (1574.0) and the result achieved by TD3 (1405.9). This underperformance is primarily due to its conservative bitrate selection, i.e., PPO chooses bitrates substantially below the available throughput, leading to inefficient utilization of network resources. Conversely, in Sample 2, PPO achieves a QoE of 327.2, which, although still below the offline optimal (685.0), is markedly superior to that of TD3 (–31.1). This improvement is largely attributable to PPO’s effective avoidance of playback rebuffering events, as the rebuffering duration approaches zero. From the above results, several important insights emerge. While the DRL-based ABR algorithms can perform adequately under their intended network conditions, the effectiveness de- grades considerably in others. This limitation stems from their Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

**[Limitaciones / riesgos / implementación | extracto 6 | p.3]**

hile the offline optimal, derived under the assumption of perfect foresight of future throughput, is unattainable in real- world settings due to the inherent unpredictability of network dynamics, the pronounced QoE gap highlights the substantial room for performance improvement. In Table I, the best-performing DRL method under each metric is highlighted in bold. To gain deeper insights into these top-performing models, we further analyzed their per-session performance. Specifically, since TD3 achieves the highest nor- malized QoE (48.9%), we selected two representative streaming sessions and visualized their performance in Fig. 1(a) and (b). In Sample 1 (Fig. 1(a)), TD3 exhibits effective bitrate adaptation, resulting in a high QoE score of 1405.9, which is close to the offline optimal of 1574.0. By contrast, in Sample 2 (Fig. 1(b)), TD3 fails to adapt appropriately to dynamic network conditions, leading to a significant rebuffering event. Specifically, at the 30th segment, the available throughput drops sharply, yet the selected bitrate remains high, rapidly depleting the playback buffer and causing an 8.9-second rebuffering event. This results inaseverelydegradedQoEof–31.1,farbelowthecorresponding offline optimal of 685.0. Although TD3 achieves the highest overall QoE, it performs suboptimally in terms of rebuffering duration and quality varia- tion, as shown in Table I. In contrast, PPO yields the best results for these two metrics. To this end, we applied PPO to the same two streaming sessions (i.e., Sample 1 and Sample 2) and visual- ized the streaming performance in Fig. 1(c) and (d), respectively. Interestingly, PPO exhibits a markedly different adaptation be- havior c

**[Limitaciones / riesgos / implementación | extracto 7 | p.4]**

ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING 12855 Fig. 1. Per-session streaming performance (the x-axis – segment index, with the width of each segment scaled by its playback time). TABLE II THE PROPORTION OF UNDERPERFORMED STREAMING SESSIONS lack of generalization capability across diverse network condi- tions (i.e., the problem “ABR Under-Generalization” described in Section I). To further quantify this problem, we introduce a metric that captures the proportion of streaming sessions in which a DRL-based ABR method yields QoE significantly below the offline optimal. Specifically, we define this proportion as follows: ε = |{κj |oj −rj > δ, j = 0, 1, . . . , J −1}| J (2) where rj is the achieved QoE of session j, oj is the corresponding optimum, δ is the QoE gap (δ is set to 700. Note that this setting is to reflect the large gap between the actual QoE

**[Limitaciones / riesgos / implementación | extracto 8 | p.4]**

large gap between the actual QoE and the offline optimal. A sensitivity analysis is performed in Section IV-E), symbol |. | calculates the element number of the set, J is the total session number (denominator), and ε is the output proportion. Table II presents the results of the under-performing propor- tion across all six DRL-based ABR algorithms. The observed values are non-negligible, ranging from 8.1% to 17.1%. Given the pre-defined QoE gap δ = 700, such a high proportion of poorly performing sessions substantially degrades the overall QoE. We hypothesize that this suboptimality stems from the direct application of conventional DRL methods [12], [13], [14], [15], [16], [17] to the ABR task. Despite extensive training on large-scale real-world network traces, these DRL methods fail to fully capture the critical features necessary for robust perfor- mance across diverse network environments. This problem is particularly problematic in practice, where streaming services must operate across a wide spectrum of network conditions, ranging from low-capacity 3G networks to high-speed 5G envi- ronments. Without addressing the generalization deficiency, the performance of the DRL-based ABR algorithms will inevitably be constrained by their limited adaptability, ultimately becoming a bottleneck in real-world deployment scenarios. III. METHODOLOGY Building upon the insights derived in Section II, we proposed BETA, a new DRL-based framework designed to address the ABR Under-Generalization problem. The overall description of BETA is presented in Section III-A, followed by the details of its two key modules in Sections III-B and Section III-C, respectively. A. BETA Overall Fig. 2 plots t

**[Limitaciones / riesgos / implementación | extracto 9 | p.4]**

(δ is set to 700. Note that this setting is to reflect the large gap between the actual QoE and the offline optimal. A sensitivity analysis is performed in Section IV-E), symbol |. | calculates the element number of the set, J is the total session number (denominator), and ε is the output proportion. Table II presents the results of the under-performing propor- tion across all six DRL-based ABR algorithms. The observed values are non-negligible, ranging from 8.1% to 17.1%. Given the pre-defined QoE gap δ = 700, such a high proportion of poorly performing sessions substantially degrades the overall QoE. We hypothesize that this suboptimality stems from the direct application of conventional DRL methods [12], [13], [14], [15], [16], [17] to the ABR task. Despite extensive training on large-scale real-world network traces, these DRL methods fail to fully capture the critical features necessary for robust perfor- mance across diverse network environments. This problem is particularly problematic in practice, where streaming services must operate across a wide spectrum of network conditions, ranging from low-capacity 3G networks to high-speed 5G envi- ronments. Without addressing the generalization deficiency, the performance of the DRL-based ABR algorithms will inevitably be constrained by their limited adaptability, ultimately becoming a bottleneck in real-world deployment scenarios. III. METHODOLOGY Building upon the insights derived in Section II, we proposed BETA, a new DRL-based framework designed to address the ABR Under-Generalization problem. The overall description of BETA is presented in Section III-A, followed by the details of its two key modules in Sections III-B and

**[Limitaciones / riesgos / implementación | extracto 10 | p.5]**

adjusted to minimize the discrepancy between the two. Through this approach, the training ABR model learns to optimize decisions across temporally extended horizons, thereby improving QoE consistency across entire streaming sessions. The details are provided in Section III-C. B. Spatial Module The structure of the Spatial Module is illustrated in Fig. 2-left. It operates in three sequential phases: offline classifier training, offline multi-model training, and online differential streaming. The three phases are encapsulated in Algorithm 1 as three distinct functions: lines 4∼17, lines 18∼29, and lines 30∼38, respectively. The main execution flow (lines 1∼3) invokes these functions in sequence. In the following, we elaborate on each phase in detail. Offline Classifier Training: The primary objective of the Spatial Module is to enhance the generalization capability of ABR algorithms, namely, to ensure robust performance across a wide spectrum of network conditions. Achieving this requires targeting the improvements of the network condition where the ABR model exhibits degraded performance. To this end, this phase focuses on identifying such problematic conditions. However, a key challenge arises: even if these conditions are well identified during offline training, the trained models may not work well at runtime, as the future network conditions of an ongoing streaming session are not known a priori. To tackle the challenge, in this work, a binary classifier is trained for the identification of network conditions. At the start, BETA trains a basic ABR model via the temporal module (will be introduced in Section III-C), and tests the QoE performance rj under the throughput trace data κj o

**[Limitaciones / riesgos / implementación | extracto 11 | p.5]**

his approach, the training ABR model learns to optimize decisions across temporally extended horizons, thereby improving QoE consistency across entire streaming sessions. The details are provided in Section III-C. B. Spatial Module The structure of the Spatial Module is illustrated in Fig. 2-left. It operates in three sequential phases: offline classifier training, offline multi-model training, and online differential streaming. The three phases are encapsulated in Algorithm 1 as three distinct functions: lines 4∼17, lines 18∼29, and lines 30∼38, respectively. The main execution flow (lines 1∼3) invokes these functions in sequence. In the following, we elaborate on each phase in detail. Offline Classifier Training: The primary objective of the Spatial Module is to enhance the generalization capability of ABR algorithms, namely, to ensure robust performance across a wide spectrum of network conditions. Achieving this requires targeting the improvements of the network condition where the ABR model exhibits degraded performance. To this end, this phase focuses on identifying such problematic conditions. However, a key challenge arises: even if these conditions are well identified during offline training, the trained models may not work well at runtime, as the future network conditions of an ongoing streaming session are not known a priori. To tackle the challenge, in this work, a binary classifier is trained for the identification of network conditions. At the start, BETA trains a basic ABR model via the temporal module (will be introduced in Section III-C), and tests the QoE performance rj under the throughput trace data κj of streaming session j. Then, BETA compares QoE rj to th

**[Limitaciones / riesgos / implementación | extracto 12 | p.5]**

in Fig. 2-left. It operates in three sequential phases: offline classifier training, offline multi-model training, and online differential streaming. The three phases are encapsulated in Algorithm 1 as three distinct functions: lines 4∼17, lines 18∼29, and lines 30∼38, respectively. The main execution flow (lines 1∼3) invokes these functions in sequence. In the following, we elaborate on each phase in detail. Offline Classifier Training: The primary objective of the Spatial Module is to enhance the generalization capability of ABR algorithms, namely, to ensure robust performance across a wide spectrum of network conditions. Achieving this requires targeting the improvements of the network condition where the ABR model exhibits degraded performance. To this end, this phase focuses on identifying such problematic conditions. However, a key challenge arises: even if these conditions are well identified during offline training, the trained models may not work well at runtime, as the future network conditions of an ongoing streaming session are not known a priori. To tackle the challenge, in this work, a binary classifier is trained for the identification of network conditions. At the start, BETA trains a basic ABR model via the temporal module (will be introduced in Section III-C), and tests the QoE performance rj under the throughput trace data κj of streaming session j. Then, BETA compares QoE rj to the offline optimum oj (c.f. Section II for the calculation of the optimal QoE), and uses their gap, i.e., (oj – rj), to classify all the throughput traces into two subsets, namely, Λnormal and Λunder: Λnormal = {κj |oj −rj ≤δ, j = 0, 1, . . . , J −1} (3) Λunder = {κj |oj −rj > δ, j = 0,

**[Limitaciones / riesgos / implementación | extracto 13 | p.6]**

ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING 12857 degradation in the streaming performance. Therefore, the binary classifier must be applied consistently in both the offline and online phases to enable the ABR models to learn how to cope with the classification errors. In this work, we re-defined two new trace datasets ΛL1 and ΛL2, and re-classified the throughput traces. Specifically, normal-performed trace set ΛL1 and under-performed trace set ΛL2 are labeled by L1 and L2, respectively. BETA executes the binary classifier, denoted by function C(.), to categorize the traces of all the streaming sessions, i.e., {κj, j = 01,…, J-1}, into the two sets: ΛL1 = {κj |C (κj) ≡L1, j = 0, 1, . . . , J −1} (5) ΛL2 = {κj |C (κj) ≡L2, j = 0, 1, . . . , J −1} (6) Thereafter,withthetwotracesets,BETAinvokesthetemporal module to train ABR model ML1 and ML2 specifically

**[Limitaciones / riesgos / implementación | extracto 14 | p.6]**

L1 and ML2, are selectively executed by BETA based on the network conditions of each stream- ing session. Specifically, BETA continuously monitors the net- work environment and records the observed video download throughput in the form of trace data during the online phase. At the start of each new streaming session, the most recent trace data is fed into the binary classifier to infer the network condition and determine the corresponding session label. If the classifier predicts L1, indicating a normal network condition, BETA deploys ML1 for that session. Conversely, if the output is L2, suggesting a potentially underperforming or challenging network condition, ML2 is selected instead. This differential execution mechanism enables BETA to dynamically adapt its ABR policy in response to real-time network conditions, thereby enhancing the robustness and consistency across heterogeneous environments. C. Temporal Module The structure of the Temporal Module is illustrated in Fig. 2- right. It is composed of six neural networks in total: an actor network, a target actor network, two critic networks, and two tar- get critic networks, following the architecture proposed in [14]. Among these, only the actor network is responsible for ABR decisions, and the remaining five all serve as training assistants. For the actor-network, the input layer contains five environ- ment states that characterize both the network conditions and the streaming context, including (i) the measured throughput over the past eight segments (represented as a list), (ii) the segment download times over the past eight segments (also as a list), (iii) the bitrate selected for the most recently downloaded segment, (

**[Limitaciones / riesgos / implementación | extracto 15 | p.8]**

ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING 12859 On this basis, the next step is to update the two critic-networks Qθ1 and Qθ2. The objective is to make the Q-value output by the critic-networks close to the target Q value Qtar through tuning the neuron weights θj = 12 of the two critics respectively (line 9). This step is implemented via executing a deterministic policy gradient to minimize the following loss function: minθj Qθj (st′, at′) −Qtar 2, j = 1, 2 (10) where state st’ and action at’ are in the first tuple in the tuple sequence Ω (i.e., index i = 0, see (8)). The actor-network πφ will then be updated by gradient descent based on the newly learned critic-network-1 Qθ1 to maximize its output Q-value (line 11): maxφQθ1 [st′, πφ(st′)] (11) where state st’ is in the first tuple of the tuple sequence Ω. The intuition behind (8) ∼(11) is to give

**[Limitaciones / riesgos / implementación | extracto 16 | p.9]**

g higher bitrates at the expense of slightly increased rebuffering. These results reflect BETA’s ability to adapt its ABR policy flexibly in accordance with the varying objective functions. Among the three QoE functions, only the Linear QoE directly uses bitrate to represent video quality. The Log and HD QoE functions apply nonlinear mappings (see Section IV-A). To better assess the actual video quality across algorithms, we replaced the bitrate values on the x-axis of Fig. 4 with their corresponding quantified video quality scores, and re-plotted the results in Fig. 5. The overall trends remain consistent: BETA achieves the most favorable trade-off between video quality and rebuffering, offering a principled explanation for its superior QoE performance across all evaluation criteria. C. Network Robustness To assess whether the ABR Under-Generalization problem is effectively addressed, we evaluated the network robustness Fig. 5. Comparison of video quality and rebuffering over 7 algorithms. Fig. 6. QoE comparison over three different network conditions. Low (0∼15 Mbps), Medium (15∼25 Mbps), and High (>25 Mbps) are three network trace datasets with different mean throughputs. of each algorithm by comparing their QoE performance under varying network conditions, as shown in Fig. 6. Specifically, the network traces were partitioned into three subsets based on their mean throughput: low (0∼15 Mbps), medium (15∼25 Mbps), and high (>25 Mbps), to reflect different ranges of realistic operating environments. In Fig. 6 (upper left), BETA consistently outperforms all baseline algorithms across the three network conditions. In the mixed network setting, BETA achieves 19.4% to 50.9% higher mean Qo

## 6. Figuras / tablas / algoritmos / ecuaciones detectados por texto
- p.3: Fig. 1(a) and (b). In
- p.3: Fig. 1(a)), TD3 exhibits effective bitrate adaptation,
- p.3: Fig. 1(b)),
- p.3: Fig. 1(c) and (d), respectively.
- p.4: Fig. 1.
- p.4: Fig. 2 plots the overall architecture of BETA, which comprises
- p.5: Fig. 2.
- p.5: Fig. 2-left.
- p.5: Algorithm 1 as three
- p.6: Fig. 2-
- p.6: Algorithm 1: Spatial Module.
- p.7: Algorithm 2: Temporal Module.
- p.7: Algorithm 2. Specifically, in one streaming session, for each
- p.7: Algorithm 2). Then, from Π, BETA will randomly
- p.7: Algorithm 2 (line 17 ∼line 24).
- p.8: Fig. 3 presents the Cumulative
- p.9: Fig. 3.
- p.9: Fig. 4.
- p.9: Fig. 4 compares the average video bitrate and rebuffering du-
- p.9: Fig. 4 with their
- p.9: Fig. 5. The overall trends remain consistent: BETA
- p.9: Fig. 5.
- p.9: Fig. 6.
- p.9: Fig. 6. Specifically, the
- p.9: Fig. 6 (upper left), BETA consistently outperforms all
- p.9: Fig. 6 (lower left). Across
- p.9: Fig. 7(a),
- p.10: Fig. 7.
- p.10: Fig. 8.
- p.10: Fig. 7 (note that due to the similarity of the results,
- p.10: Fig. 7(b) and
- p.10: Fig. 8 presents the evolution of QoE over training
- p.11: Fig. 9.
- p.11: Fig. 9, both variants exhibit
- p.11: Fig. 7(a)). To uncover which module
- p.11: Fig. 7(d). However, it shows a pattern very similar to the full
- p.11: Fig. 7(a)). To this end, we further removed the
- p.11: Fig.7(e),thediffer-
- p.11: Fig. 10-left. We observed that the QoE peaks
- p.11: Fig. 10.
- p.11: Fig.10-middle,itisobservedthatastheQoEthresholdincreases,
- p.11: Fig.10-right,

## 7. Líneas con posible contenido matemático/formal
- p.1: `[10.1109/SPCOM50965.2020.9179507]. Recommended for acceptance by S.`
- p.1: `for over 80% of the Internet traffic [1].`
- p.1: `plemented under the DASH protocol [2]. Their key component`
- p.1: `degradation when the network conditions vary widely [3], [4],`
- p.1: `[5], [6], [11]. This phenomenon, i.e., the operational range of`
- p.1: `The former [5], [6], [7], [8], [9], [19], [20], [21] rely on`
- p.1: `deepreinforcementlearning(DRL)[3],[4],[10],[11],[18],[22],`
- p.1: `[23], [24], [25], [26], [27], [28], [29], [30], have gained attention.`
- p.1: `counterparts [10].`
- p.2: `the direct application of the generic DRL techniques [12], [13],`
- p.2: `[14], [15], [16], [17], which fail to capture all the key features`
- p.2: `DRL approaches [12], [13], [14], [15], [16], [17] consistently`
- p.2: `A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and`
- p.2: `SAC [17], clearly revealing the impact of the ABR Under-`
- p.2: `sourced on GitHub [32] to support reproducibility and future`
- p.2: `Existing learning-based ABR algorithms [3], [4], [10], [11],`
- p.2: `[18], [22], [23], [24], [25], [26], [27], [28], [29], [30] (will be`
- p.2: `advanced DRL techniques [12], [13], [14], [15], [16], [17] for`
- p.2: `SAC [17].`
- p.2: `to the established designs from prior literature [3], [4], [10], [11],`
- p.2: `[18], [22], [23], [24], [25], [26], [27], [28], [29], [30]. Specifi-`
- p.2: `environment, we built an open-source ABR emulator [32] based`
- p.2: `on the previous work by Mao et al. [10], applying custom modi-`
- p.3: `been made publicly available on GitHub [36]. In this evaluation,`
- p.3: `QoE function proposed by Mao et al. [10]:`
- p.3: `where the first term of Eq. (1) denotes the video quality utility,`
- p.3: `(coefficient σ = 50) and video quality variation respectively.`
- p.3: `mapping F(bt) = bt [10] in this evaluation.`
- p.3: `throughput (more details are referred to Spiteri et al. [8], and the`
- p.3: `implementation is available in [31]). In addition to the QoE, we`
- p.3: `quality variation. See their definitions in Eq. (1). These metrics`
- p.4: `ε = |{κj |oj −rj > δ, j = 0, 1, . . . , J −1}|`
- p.4: `optimum, δ is the QoE gap (δ is set to 700. Note that this setting`
- p.4: `the pre-defined QoE gap δ = 700, such a high proportion of`
- p.4: `direct application of conventional DRL methods [12], [13], [14],`
- p.4: `[15], [16], [17] to the ABR task. Despite extensive training on`
- p.4: `DRL methods [12], [13], [14], [15], [16], [17] only achieve`
- p.5: `[12], [13], [14], [15], [16], [17] often exhibit short-sightedness.`
- p.5: `Λnormal = {κj |oj −rj ≤δ, j = 0, 1, . . . , J −1}`
- p.5: `Λunder = {κj |oj −rj > δ, j = 0, 1, . . . , J −1}`
- p.5: `is larger than QoE threshold δ (e.g., = 700) then throughput`
- p.5: `trace sets {Λnormal, Λunder} work as the ground truth during`
- p.6: `traces of all the streaming sessions, i.e., {κj, j = 01,…, J-1},`
- p.6: `ΛL1 = {κj |C (κj) ≡L1, j = 0, 1, . . . , J −1}`
- p.6: `ΛL2 = {κj |C (κj) ≡L2, j = 0, 1, . . . , J −1}`
- p.6: `get critic networks, following the architecture proposed in [14].`
- p.6: `Λ={κj | ࢘j}`
- p.6: `1: C, Mbasic = Offline_Classifier_Training (Λ)`
- p.6: `2 : ML1, ML2 = Offline_MultiModel_Training (C, Λ, Mbasic)`
- p.6: `3: Online_Differential_Streaming (C, ML1, ML2)`
- p.6: `4: Function Offline_Classifier_Training (Λ={κj | ࢘j})`
- p.6: `Λnormal = Ø, Λunder = Ø`
- p.6: `18: Function Offline_MultiModel_Training (C, Λ={κj | ࢘j},`
- p.6: `Λ’normal = Ø, Λ’under = Ø`
- p.6: `if C(κj) == L1 then`
- p.6: `30: Function Online_Differential_Streaming (C, ML1, ML2)`
- p.6: `if C(κ) == L1 then`
- p.7: `Initialize: critic-networks Qθ1 and Qθ2 (neuron weight θ1,`
- p.7: `θ2); actor-network πφ (neuron weight φ), target networks`
- p.7: `Qθ1_tar, Qθ2_tar, and πφ_tar (neuron weight θ1_tar,`
- p.7: `θ2_tar, φ_tar)`
- p.7: `{κj | ࢘j}`
- p.7: `Observe state st and decide action at: at = πφ(st)`
- p.7: `Ω ←⟨(st′+i, at′+i, rt′+i, st′+1+i)⟩i=0,1,...,n−1`
- p.7: `Qtar = Compute_Target_Q (Ω, n)`
- p.7: `Update critics Qθ1, Qθ2 by minimizing the loss`
- p.7: `minθ1/2[Qθ1/2(st′, at′) −Qtar]2`
- p.7: `if (t mod σ) == 0 then`
- p.7: `maxφQθ1[st′, πφ(st′)]`
- p.7: `Softly update target networks: φ_tar = τ×φ_tar +`
- p.7: `(1-τ)×φ θ1_tar = τ×θ1_tar + (1-τ)×θ1`
- p.7: `θ2_tar = τ×θ2_tar + (1-τ)×θ2`
- p.7: `17: Function Compute_Target_Q (Ω, n)`
- p.7: `R = R + βi × rt’+i`
- p.7: `atar = πφ_tar(st’+n) + N(μ,σ2)`
- p.7: `Qtar1 = Qθ1_tar(st’+n, atar), Qtar2 = Qθ2_tar(st’+n,`
- p.7: `min_Q = min(Qtar1, Qtar2)`
- p.7: `return R + βn × min_Q`
- p.7: `{ηh | h = 01,…,H-1} (total H versions), and the output bt is the`
- p.7: `[10], and then the resultant reward rt (quantified by the QoE`

## 8. Texto crudo completo por página

> Mantener este bloque para Codex si necesita comprobar contexto literal. Puede contener errores de orden por columnas del PDF. Para fórmulas exactas o tablas complejas, usar PDF original.


### Página 1

```text
12852
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025
A Novel Spatial-Temporal Learning Method for
Enhancing Generalization in Adaptive
Video Streaming
Guanghui Zhang
, Ziming Wang
, Huaren Wei, Mengbai Xiao
, Hui Yuan
, Senior Member, IEEE,
Dongxiao Yu
, Senior Member, IEEE, and Xiuzhen Cheng
, Fellow, IEEE
Abstract—Adaptive video streaming has become a fundamental
technology for video delivery. With the rise of deep reinforcement
learning (DRL), streaming vendors are increasingly adopting DRL-
driven adaptive bitrate (ABR) algorithms. In real-world deploy-
ments, most ABR approaches are developed with the aim of main-
taining good performance across a wide variety of network environ-
ments. However, contrary to this expectation, our empirical find-
ings show that even when trained on extensive real-world network
trace data, these DRL-based ABR algorithms achieve only 43.1%
to 48.9% of Quality-of-Experience (QoE) under highly diverse
network conditions, which falls significantly short of the 100% op-
timum. We termed this problem as “ABR Under-Generalization”.
To overcome this problem, we introduce BETA – a novel DRL-
based ABR framework that incorporates both spatial and temporal
learning mechanisms: 1) Spatially, BETA features a detector that
flags the network conditions likely to cause poor performance,
then trains specialized ABR models tailored for those conditions
and 2) Temporally, BETA enhances its learning by incorporating
multi-step decision experiences at each training epoch, enabling the
trained model to account for long-term environmental dynamics.
Comprehensive evaluations show that BETA outperforms state-of-
the-art ABR algorithms, yielding average QoE gains of 19.4% to
50.9%,andachievingimprovementsofupto244.1%underseverely
fluctuating network conditions.
Index
Terms—Video
streaming,
mobile
network,
deep
reinforcement learning, quality-of-experience.
I. INTRODUCTION
I
N RECENT years, video streaming has witnessed rapid
expansion, emerging as one of the primary applications of the
Received 9 December 2024; revised 26 June 2025; accepted 3 July 2025.
Date of publication 15 July 2025; date of current version 5 November 2025.
This work was supported by the National Natural Science Foundation of China
under Grant 62302268, in part by the Natural Science Foundation of Shandong
Province under Grant 2023HWYQ-045 and Grant ZR2023QF060, in part by
Qingdao Natural Science Foundation under Grant 23-2-1-127-zyyd-jch, and
in part by the Taishan Scholar Project of Shandong Province under Grant
tsqn202312051. An earlier version of this paper was presented in part at the
IEEE International Conference on Sensing, Communication, and Networking
[10.1109/SPCOM50965.2020.9179507]. Recommended for acceptance by S.
Wang. (Corresponding author: Hui Yuan.)
Guanghui Zhang, Ziming Wang, Huaren Wei, Mengbai Xiao, Dongxiao Yu,
and Xiuzhen Cheng are with the School of Computer Science and Technol-
ogy, Shandong University, Qingdao 266237, China (e-mail: gh.zhang@sdu.
edu.cn; 202235192@mail.sdu.edu.cn; 202315182@mail.sdu.edu.cn; xiaomb@
sdu.edu.cn; dxyu@sdu.edu; xzcheng@sdu.edu.cn).
Hui Yuan is with the School of Control Science and Engineering, Shandong
University, Jinan 250061, China (e-mail: huiyuan@sdu.edu.cn).
Digital Object Identifier 10.1109/TMC.2025.3588135
Internet. As reported by Cisco, global video streaming traffic has
surged by a factor of 15 over the past five years and now accounts
for over 80% of the Internet traffic [1].
However, the highly variable nature of the mobile networks
(primarily caused by unstable radio signals) poses a major
obstacle to video streaming. Smooth playback relies on stable
and consistent network throughput, which is difficult to main-
tain in such dynamic environments. To tackle this issue, the
streaming vendors have turned their attention to adaptive bitrate
(ABR) algorithms, aiming to alleviate the negative effects of the
throughput fluctuations. These ABR algorithms are typically im-
plemented under the DASH protocol [2]. Their key component
is an adaptive logic, which intelligently adjusts video quality
in real time (by selecting appropriate bitrates) based on several
streaming metrics such as historical throughput measurements
and current buffer status. The objective is to enhance the viewer’s
Quality of Experience (QoE).
Most ABR algorithms are developed with the intention to
perform reliably across the wide network environments of
any size and shape, e.g., from 3G networks with peak band-
widths of a few Mbps to 5G networks offering mean band-
widths of 100+ Mbps. However, real-world experiments con-
sistently demonstrate that the existing ABR algorithms, while
effective under intended network conditions, suffer significant
degradation when the network conditions vary widely [3], [4],
[5], [6], [11]. This phenomenon, i.e., the operational range of
an ABR algorithm is narrow, leads to a marked decrease in
the overall performance. We defined this problem as “ABR
Under-Generalization”.
The existing ABR algorithms can be generally divided
into two major categories: heuristic-based and learning-based.
The former [5], [6], [7], [8], [9], [19], [20], [21] rely on
pre-programmed ABR model with fixed control rules, which
inherently limits their adaptability to generalize the varying
network
environments.
Consequently,
the
heuristic-based
algorithms have gradually lost favor in recent years. In contrast,
the learning-based algorithms, particularly those powered by
deepreinforcementlearning(DRL)[3],[4],[10],[11],[18],[22],
[23], [24], [25], [26], [27], [28], [29], [30], have gained attention.
They train neural networks using real network trace data,
resulting in ABR models that are more flexible than the heuristic
counterparts [10].
1536-1233 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence and similar technologies.
Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.
```

### Página 2

```text
ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING
12853
However, our measurement study (refer to Section II) reveals
that when faced with a wide range of network conditions,
even extensively trained DRL-based ABR algorithms can only
achieve 43.1% ∼48.9% of the maximum possible QoE, far
below the offline optimal 100%. This highlights the problem of
ABR Under-Generalization, which contradicts the theoretical
expectation that training on large-scale real traces should yield
generalizable ABR policies. The root cause appears to lie in
the direct application of the generic DRL techniques [12], [13],
[14], [15], [16], [17], which fail to capture all the key features
required to adapt across different environments.
Motivated by this challenge, we proposed BETA, a new
DRL-based ABR framework specifically designed to enhance
the generalization of video streaming. BETA consists of two
core modules: spatial and temporal, which jointly tackle the
above-mentioned challenge:
Spatial Module: Our measurement study (Section II) shows
that none of the ABR algorithms trained using the conventional
DRL approaches [12], [13], [14], [15], [16], [17] consistently
maintain high performance across all network conditions. In
particular, all the measured algorithms fail in 8.1% to 17.1% of
the evaluated traces, significantly degrading the overall results.
Additionally, the specific traces where underperformance occurs
differ greatly depending on the specific DRL method adopted.
To address this issue, BETA incorporates a spatial module.
It begins by training a basic ABR model and benchmarks its
QoE against the offline optimal performance per streaming ses-
sion. This process helps identify the underperforming network
conditions, from which the corresponding network features are
extracted, and then are used to predict the potential network
conditions that might cause poor performance in the future.
BETA proceeds to train specialized ABR models specifically
tailored to these challenging network conditions.
Temporal Module: We observed that the existing DRL-
trained ABR algorithms are often short-sighted, focusing only
on single-step future planning. This is due to their training
approach, where each epoch updates the model based solely
on the immediate reward of short-term feedback. This is ill-
suited for the video streaming contexts that require consecutive
decision-making across all the video segments in each streaming
session.
BETA addresses this issue with a temporal module. BETA
samples multi-segment decision sequences during training, each
consisting of a series of state-action-reward tuples. For each
sequence, a discounted actual reward encompassing all the seg-
ments is calculated, along with an expected reward based on the
initial and final states of each sequence. Both of the rewards are
then used to update the neuron weights by minimizing the gap
between them. This approach enables the trained ABR model to
make far-sighted decisions, thereby ensuring more stable QoE.
Extensive evaluation using large-scale network trace datasets
demonstrates the effectiveness of BETA. Compared to state-of-
the-art ABR algorithms, BETA improves average QoE by 19.4%
to 50.9%, with gains reaching 244.1% in highly variable network
conditions. For the internal QoE metrics, BETA achieves a 7.9%
increase in video quality and a 98.3% reduction in rebuffering
events. These benefits are attributed to BETA’s flexible bitrate
decisions, which not only better match the network dynamics
but also fully utilize available network resources.
In summary, our contributions are three-fold:
Large-Scale Measurement Study: We systematically evalu-
ated ABR algorithms trained by six well-known DRL methods,
A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and
SAC [17], clearly revealing the impact of the ABR Under-
Generalization problem (Section II).
Design of BETA: We presented BETA, a DRL-based ABR
framework integrating spatial and temporal modules to enhance
generalization. The implementation of BETA has been open-
sourced on GitHub [32] to support reproducibility and future
research (Section III).
Comprehensive Evaluation: Through extensive evaluations,
we show that BETA significantly outperforms the state-of-the-
art ABR algorithms. In addition, we investigated the underlying
reasons for its effectiveness (Section IV).
II. ABR UNDER-GENERALIZATION
Existing learning-based ABR algorithms [3], [4], [10], [11],
[18], [22], [23], [24], [25], [26], [27], [28], [29], [30] (will be
comprehensively reviewed in Section V) predominantly rely on
advanced DRL techniques [12], [13], [14], [15], [16], [17] for
policy training. To demonstrate the ABR Under-Generalization
problem, we conducted a measurement study evaluating the
ABRalgorithms trainedusingsixwidelyadoptedDRLmethods:
A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and
SAC [17].
DRL Configuration. The neural network architecture adheres
to the established designs from prior literature [3], [4], [10], [11],
[18], [22], [23], [24], [25], [26], [27], [28], [29], [30]. Specifi-
cally,themodelinputcomprisesfivecategoriesofenvironmental
states: (i) the measured throughput of the past 8 segments, (ii)
the download durations of the past 8 segments, (iii) the bitrate of
the most recently downloaded segment, (iv) the current buffer
occupancy, and (v) the number of remaining segments in the
current streaming session. The first two inputs are processed via
convolutional neural networks (CNNs) with 128 filters, while
the remaining three are fed into fully connected (dense) layers
with 128 neurons. Then the outputs are subsequently merged
through a dense aggregation layer comprising 256 neurons. The
output layer offers the discrete bitrate level, which serves as the
decision action. All the six DRL methods are trained using the
Adam optimizer, with training hyperparameters (e.g., learning
rate, batch size, experience replay buffer) individually tuned.
Streaming Environment: To emulate the realistic streaming
environment, we built an open-source ABR emulator [32] based
on the previous work by Mao et al. [10], applying custom modi-
fications to accommodate our experimental setup. For example,
each streaming session emulates the playback of a 192-second
video, partitioned into 48 segments of 4 seconds each. Every
segment is encoded into eight bitrate levels: {0.2, 0.8, 2.2, 5.0,
10.0, 18.0, 32.0, 50.0} Mbps, reflecting a wide range of encoding
options.
The network condition is emulated using TCP throughput
traces, with an average bandwidth of 17.66 Mbps and a peak
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.
```

### Página 3

```text
12854
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025
TABLE I
COMPARISON OF QOE AND STREAMING PERFORMANCE OVER SIX DRL-BASED
ABR ALGORITHMS
value of up to 131.44 Mbps. These traces were collected from
real-world cellular networks, including 3G, 4G, 5G, and Wi-
Fi, over a continuous 77-day period. The data collection was
conducted across four types of geographic locations: subways,
campuses, shopping malls, and homes. The complete dataset has
been made publicly available on GitHub [36]. In this evaluation,
80% of the data is used for model training, and the remaining
20% is reserved for online testing. Both the training and testing
sets comprehensively cover the three network types, the four
geographic locations, and all the time periods in one day.
For the streaming performance metric, we adopted an existing
QoE function proposed by Mao et al. [10]:
QoE =
N−1

t=0
F(bt) −σ ×
N−1

t=0
θt −
N−2

t=0
|F(bt+1) −F(bt)|
(1)
where the first term of Eq. (1) denotes the video quality utility,
and the last two denote the penalties for playback rebuffering
(coefficient σ = 50) and video quality variation respectively.
Specifically, bt is the video bitrate of segment t, θt is the
rebuffering duration in downloading segment t, F(.) denotes the
mapping from bitrate to video quality where we adopted linear
mapping F(bt) = bt [10] in this evaluation.
Results Analysis: Table I summarizes the performance of the
six DRL-based ABR algorithms. QoE is reported using two
representations: the absolute QoE score (denoted as A-QoE) and
the normalized QoE score (denoted as N-QoE). The normalized
score is obtained by dividing the absolute score by the offline
optimal. The optimal QoE serves as the theoretical upper bound,
which is computed based on dynamic programming, using
an omniscient policy with perfect foresight of future network
throughput (more details are referred to Spiteri et al. [8], and the
implementation is available in [31]). In addition to the QoE, we
further evaluated the three core metrics that contribute to QoE:
the average video bitrate, total rebuffering duration, and video
quality variation. See their definitions in Eq. (1). These metrics
collectively characterize the tradeoffs each algorithm makes in
adaptive streaming scenarios.
From Table I, two key observations can be made regarding
the QoE performance of different DRL-based ABR algorithms.
First, there exists a substantial performance disparity among
the DRL methods. For example, the TD3-based ABR model
achieves the highest absolute QoE (A-QoE) of 346.7, whereas
the SAC-based model performs the worst, with an A-QoE of
only305.9.Second,thenormalizedQoE(N-QoE)revealsthatall
the six methods attain only suboptimal performance, achieving
merely 43.1% to 48.9% of the offline optimal QoE. This is
significantly lower than the theoretical upper bound of 100%.
While the offline optimal, derived under the assumption of
perfect foresight of future throughput, is unattainable in real-
world settings due to the inherent unpredictability of network
dynamics, the pronounced QoE gap highlights the substantial
room for performance improvement.
In Table I, the best-performing DRL method under each
metric is highlighted in bold. To gain deeper insights into these
top-performing models, we further analyzed their per-session
performance. Specifically, since TD3 achieves the highest nor-
malized QoE (48.9%), we selected two representative streaming
sessions and visualized their performance in Fig. 1(a) and (b). In
Sample 1 (Fig. 1(a)), TD3 exhibits effective bitrate adaptation,
resulting in a high QoE score of 1405.9, which is close to the
offline optimal of 1574.0. By contrast, in Sample 2 (Fig. 1(b)),
TD3 fails to adapt appropriately to dynamic network conditions,
leading to a significant rebuffering event. Specifically, at the
30th segment, the available throughput drops sharply, yet the
selected bitrate remains high, rapidly depleting the playback
buffer and causing an 8.9-second rebuffering event. This results
inaseverelydegradedQoEof–31.1,farbelowthecorresponding
offline optimal of 685.0.
Although TD3 achieves the highest overall QoE, it performs
suboptimally in terms of rebuffering duration and quality varia-
tion, as shown in Table I. In contrast, PPO yields the best results
for these two metrics. To this end, we applied PPO to the same
two streaming sessions (i.e., Sample 1 and Sample 2) and visual-
ized the streaming performance in Fig. 1(c) and (d), respectively.
Interestingly, PPO exhibits a markedly different adaptation be-
havior compared to TD3. In Sample 1, PPO achieves a QoE
of 577.3, which is significantly lower than both the offline
optimal (1574.0) and the result achieved by TD3 (1405.9). This
underperformance is primarily due to its conservative bitrate
selection, i.e., PPO chooses bitrates substantially below the
available throughput, leading to inefficient utilization of network
resources. Conversely, in Sample 2, PPO achieves a QoE of
327.2, which, although still below the offline optimal (685.0),
is markedly superior to that of TD3 (–31.1). This improvement
is largely attributable to PPO’s effective avoidance of playback
rebuffering events, as the rebuffering duration approaches zero.
From the above results, several important insights emerge.
While the DRL-based ABR algorithms can perform adequately
under their intended network conditions, the effectiveness de-
grades considerably in others. This limitation stems from their
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.
```

### Página 4

```text
ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING
12855
Fig. 1.
Per-session streaming performance (the x-axis – segment index, with the width of each segment scaled by its playback time).
TABLE II
THE PROPORTION OF UNDERPERFORMED STREAMING SESSIONS
lack of generalization capability across diverse network condi-
tions (i.e., the problem “ABR Under-Generalization” described
in Section I). To further quantify this problem, we introduce
a metric that captures the proportion of streaming sessions
in which a DRL-based ABR method yields QoE significantly
below the offline optimal. Specifically, we define this proportion
as follows:
ε = |{κj |oj −rj > δ, j = 0, 1, . . . , J −1}|
J
(2)
where rj is the achieved QoE of session j, oj is the corresponding
optimum, δ is the QoE gap (δ is set to 700. Note that this setting
is to reflect the large gap between the actual QoE and the offline
optimal. A sensitivity analysis is performed in Section IV-E),
symbol |. | calculates the element number of the set, J is the total
session number (denominator), and ε is the output proportion.
Table II presents the results of the under-performing propor-
tion across all six DRL-based ABR algorithms. The observed
values are non-negligible, ranging from 8.1% to 17.1%. Given
the pre-defined QoE gap δ = 700, such a high proportion of
poorly performing sessions substantially degrades the overall
QoE. We hypothesize that this suboptimality stems from the
direct application of conventional DRL methods [12], [13], [14],
[15], [16], [17] to the ABR task. Despite extensive training on
large-scale real-world network traces, these DRL methods fail
to fully capture the critical features necessary for robust perfor-
mance across diverse network environments. This problem is
particularly problematic in practice, where streaming services
must operate across a wide spectrum of network conditions,
ranging from low-capacity 3G networks to high-speed 5G envi-
ronments. Without addressing the generalization deficiency, the
performance of the DRL-based ABR algorithms will inevitably
be constrained by their limited adaptability, ultimately becoming
a bottleneck in real-world deployment scenarios.
III. METHODOLOGY
Building upon the insights derived in Section II, we proposed
BETA, a new DRL-based framework designed to address the
ABR Under-Generalization problem. The overall description of
BETA is presented in Section III-A, followed by the details
of its two key modules in Sections III-B and Section III-C,
respectively.
A. BETA Overall
Fig. 2 plots the overall architecture of BETA, which comprises
twoprimarymodules:SpatialandTemporal.TheSpatialModule
serves as the master routine, while the Temporal Module is a
sub-routine that is periodically invoked by the Spatial Module.
Spatial Module: As shown in the measurement study in
Section II, ABR algorithms trained with the state-of-the-art
DRL methods [12], [13], [14], [15], [16], [17] only achieve
43.1% to 48.9% of the optimal QoE, primarily due to the severe
underperformance in 8.1% to 17.1% of the streaming sessions.
To address this issue, BETA introduces the Spatial Module.
Specifically, BETA initially invokes the Temporal Module to
train a base ABR model, which is then evaluated across all
training network traces by comparing the achieved QoE with
the corresponding offline optimum. Based on this evaluation,
the training traces are partitioned into two subsets: one where
the ABR model performs adequately, and the other where it fails
to generalize well. From these labeled traces, BETA extracts in-
ternal network features to train a classifier that predicts whether a
given network trace is likely to result in underperformance. This
classifier enables BETA to dynamically distinguish between
“normal” and “difficult” traces in real-time. Accordingly, two
complementary ABR models are trained for each trace subset
by invoking the Temporal Module, and during online stream-
ing, BETA dynamically selects the appropriate logic to better
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.
```

### Página 5

```text
12856
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025
Fig. 2.
The whole structure of BETA with the spatial module and the temporal module.
accommodate the diverse network conditions. The details are
elaborated in Section III-B.
Temporal Module: Existing DRL-based ABR algorithms
[12], [13], [14], [15], [16], [17] often exhibit short-sightedness.
This is problematic in adaptive video streaming, where QoE is
influenced by temporal continuity and cumulative effects of the
ABR decisions over multiple segments. To overcome this issue,
BETA introduces the Temporal Module. During training, BETA
records a state–action–reward tuple for each segment and stores
them in an experience buffer, maintaining a history of decision
sequences. From this buffer, it samples tuple sequences where
each consists of n consecutive segments. For each sequence, a
discounted actual reward encompassing all the segments is cal-
culated, along with an expected reward based on the initial and
final states of each sequence. These two rewards are integrated
into the training, where the neural network weights are adjusted
to minimize the discrepancy between the two. Through this
approach, the training ABR model learns to optimize decisions
across temporally extended horizons, thereby improving QoE
consistency across entire streaming sessions. The details are
provided in Section III-C.
B. Spatial Module
The structure of the Spatial Module is illustrated in Fig. 2-left.
It operates in three sequential phases: offline classifier training,
offline multi-model training, and online differential streaming.
The three phases are encapsulated in Algorithm 1 as three
distinct functions: lines 4∼17, lines 18∼29, and lines 30∼38,
respectively. The main execution flow (lines 1∼3) invokes these
functions in sequence. In the following, we elaborate on each
phase in detail.
Offline Classifier Training: The primary objective of the
Spatial Module is to enhance the generalization capability of
ABR algorithms, namely, to ensure robust performance across
a wide spectrum of network conditions. Achieving this requires
targeting the improvements of the network condition where
the ABR model exhibits degraded performance. To this end,
this phase focuses on identifying such problematic conditions.
However, a key challenge arises: even if these conditions are
well identified during offline training, the trained models may
not work well at runtime, as the future network conditions of an
ongoing streaming session are not known a priori.
To tackle the challenge, in this work, a binary classifier is
trained for the identification of network conditions. At the start,
BETA trains a basic ABR model via the temporal module (will
be introduced in Section III-C), and tests the QoE performance rj
under the throughput trace data κj of streaming session j. Then,
BETA compares QoE rj to the offline optimum oj (c.f. Section II
for the calculation of the optimal QoE), and uses their gap, i.e.,
(oj – rj), to classify all the throughput traces into two subsets,
namely, Λnormal and Λunder:
Λnormal = {κj |oj −rj ≤δ, j = 0, 1, . . . , J −1}
(3)
Λunder = {κj |oj −rj > δ, j = 0, 1, . . . , J −1}
(4)
The intuition behind the two equations is that, if the QoE gap
is larger than QoE threshold δ (e.g., = 700) then throughput
trace κj will be incorporated into set Λunder that consists of all
under-performed traces. On the contrary, trace κj will be into the
normal-performed set Λnormal. On this basis, BETA will train
a binary classifier via supervised learning where the classifier is
modeled with convolutional neural networks (CNN). The two
trace sets {Λnormal, Λunder} work as the ground truth during
the training.
Offline Multi-model Training: Prior to training the ABR mod-
els, the throughput traces will be re-classified using the binary
classifier. One might question why BETA does not simply rely
on the ground-truth classification obtained via (3) and (4). The
reason is that the binary classifier will be ultimately applied
in the online streaming, but it is inherently imperfect to cope
with the unknown network conditions at runtime, and thus,
the online classification inevitably has errors. If such misclas-
sifications are not exposed to the ABR models during offline
training, the models will lack the necessary robustness to handle
them at runtime. Consequently, this would lead to a significant
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.
```

### Página 6

```text
ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING
12857
degradation in the streaming performance. Therefore, the binary
classifier must be applied consistently in both the offline and
online phases to enable the ABR models to learn how to cope
with the classification errors.
In this work, we re-defined two new trace datasets ΛL1
and ΛL2, and re-classified the throughput traces. Specifically,
normal-performed trace set ΛL1 and under-performed trace set
ΛL2 are labeled by L1 and L2, respectively. BETA executes
the binary classifier, denoted by function C(.), to categorize the
traces of all the streaming sessions, i.e., {κj, j = 01,…, J-1},
into the two sets:
ΛL1 = {κj |C (κj) ≡L1, j = 0, 1, . . . , J −1}
(5)
ΛL2 = {κj |C (κj) ≡L2, j = 0, 1, . . . , J −1}
(6)
Thereafter,withthetwotracesets,BETAinvokesthetemporal
module to train ABR model ML1 and ML2 specifically for each
of the two network classes. These two models can be executed
complementarily at the online phase.
Online Differential Streaming: At runtime, the two trained
ABR models, denoted as ML1 and ML2, are selectively executed
by BETA based on the network conditions of each stream-
ing session. Specifically, BETA continuously monitors the net-
work environment and records the observed video download
throughput in the form of trace data during the online phase.
At the start of each new streaming session, the most recent
trace data is fed into the binary classifier to infer the network
condition and determine the corresponding session label. If the
classifier predicts L1, indicating a normal network condition,
BETA deploys ML1 for that session. Conversely, if the output
is L2, suggesting a potentially underperforming or challenging
network condition, ML2 is selected instead. This differential
execution mechanism enables BETA to dynamically adapt its
ABR policy in response to real-time network conditions, thereby
enhancing the robustness and consistency across heterogeneous
environments.
C. Temporal Module
The structure of the Temporal Module is illustrated in Fig. 2-
right. It is composed of six neural networks in total: an actor
network, a target actor network, two critic networks, and two tar-
get critic networks, following the architecture proposed in [14].
Among these, only the actor network is responsible for ABR
decisions, and the remaining five all serve as training assistants.
For the actor-network, the input layer contains five environ-
ment states that characterize both the network conditions and
the streaming context, including (i) the measured throughput
over the past eight segments (represented as a list), (ii) the
segment download times over the past eight segments (also as a
list), (iii) the bitrate selected for the most recently downloaded
segment, (iv) the current buffer occupancy (in seconds), and (v)
the number of remaining segments yet to be downloaded in the
current streaming session. This input design is consistent with
the DRL settings introduced in Section II.
In the hidden layers, the first two states (among the five) are
individually processed by two CNNs, each with 128 filters, to
extract temporal patterns. The remaining three scalar states are
Algorithm 1: Spatial Module.
Input: Training throughput trace of all streaming sessions j:
Λ={κj | ࢘j}
# Step 1: Input - training trace data Λ; Output - trained classifier C
and basic ABR model Mbasic.
1: C, Mbasic = Offline_Classifier_Training (Λ)
# Step 2: Input - classifier C, training trace Λ, basic ABR model
Mbasic; Output – two trained ABR models, i.e., ML1, ML2.
2 : ML1, ML2 = Offline_MultiModel_Training (C, Λ, Mbasic)
# Step 3: Input - classifier C, and trained ABR models ML1, ML2.
3: Online_Differential_Streaming (C, ML1, ML2)
4: Function Offline_Classifier_Training (Λ={κj | ࢘j})
5:
Train ABR model Mbasic with Λ via temporal module
6:
Λnormal = Ø, Λunder = Ø
7:
for trace κj in streaming session j=1 to J do
8:
Test Mbasic with κj, and obtain QoE rj
9:
Compute optimal QoE under κj, denoted by oj
10:
if oj – rj > δ then
11:
Λunder ←κj
12:
else
13:
Λnormal ←κj
14:
end if
15:
end for
16:
Supervised learning to train binary classifier C via {Λnormal,
Λunder}
17:
return C
18: Function Offline_MultiModel_Training (C, Λ={κj | ࢘j},
Mbasic)
19:
Λ’normal = Ø, Λ’under = Ø
20:
for trace κj in streaming session j=1 to J do
21:
if C(κj) == L1 then
22:
ΛL1 ←κj
23:
else
24:
ΛL2 ←κj
25:
end if
26:
end for
27:
Train ABR model ML1 (upon Mbasic) with trace set ΛL1 via
temporal module
28:
Train ABR model ML2 (upon Mbasic) with trace set ΛL2 via
temporal module
29:
return ML1, ML2
30: Function Online_Differential_Streaming (C, ML1, ML2)
31:
while a new streaming session starts do
32:
Obtain the online captured throughput trace, denoted by κ
33:
if C(κ) == L1 then
34:
Apply ABR model ML1 to the current session
35:
else
36:
Apply ABR model ML2 to the current session
37:
end if
38:
end while
each passed through separate fully connected (dense) layers with
128 neurons. The outputs of all the five are then concatenated
and passed through an additional dense layer consisting of 256
neurons, which serves as the final hidden representation for
action generation.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.
```

### Página 7

```text
12858
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025
Algorithm 2: Temporal Module.
Initialize: critic-networks Qθ1 and Qθ2 (neuron weight θ1,
θ2); actor-network πφ (neuron weight φ), target networks
Qθ1_tar, Qθ2_tar, and πφ_tar (neuron weight θ1_tar,
θ2_tar, φ_tar)
Input: throughput trace data of all streaming sessions j:
{κj | ࢘j}
Output: trained actor-network πφ
1: for each streaming session j do
2:
for segment t = 1 to T do
3:
Observe state st and decide action at: at = πφ(st)
4:
Map at to bitrate bt and download segment t with
throughput trace κj
5:
Observe reward rt (i.e., QoE), and new state st+1
6:
Store tuple (st, at, rt, st+1) in an experience buffer Π
7:
Sample a mini-batch Ω from Π, including a batch of
tuple sequences, each with n consecutive tuples:
Ω ←⟨(st′+i, at′+i, rt′+i, st′+1+i)⟩i=0,1,...,n−1
8:
Qtar = Compute_Target_Q (Ω, n)
9:
Update critics Qθ1, Qθ2 by minimizing the loss
function:
minθ1/2[Qθ1/2(st′, at′) −Qtar]2
10:
if (t mod σ) == 0 then
11:
Update actor πφ by maximizing the Q value:
maxφQθ1[st′, πφ(st′)]
12:
Softly update target networks: φ_tar = τ×φ_tar +
(1-τ)×φ θ1_tar = τ×θ1_tar + (1-τ)×θ1
θ2_tar = τ×θ2_tar + (1-τ)×θ2
13:
end if
14:
end for
15: end for
16: return trained actor network πφ
17: Function Compute_Target_Q (Ω, n)
18:
Initialize cumulative reward: R = 0
19:
for (st’+i, at’+i, rt’+i, st’+1+i) in Ω and i = 0 to n-1
do
20:
Update R with reward rt’+i and discount factor β:
R = R + βi × rt’+i
21:
end for
22:
Calculate target action with the last state st’+n in Ω:
atar = πφ_tar(st’+n) + N(μ,σ2)
23:
Calculate minimum target Q value:
Qtar1 = Qθ1_tar(st’+n, atar), Qtar2 = Qθ2_tar(st’+n,
atar)
min_Q = min(Qtar1, Qtar2)
24:
return R + βn × min_Q
The output layer has only one neuron with the activation
function Tanh. The output action, denoted by at (for segment
t), is continuous-valued, ranging from −1 to +1. To map it to
the encoding bitrate version, we defined a mapping policy:
bt = max

ηh
ηh ≤

η0 + (ηH−1 −η0)(at+1)
2

,
h = 0, . . . , H −1

(7)
where ηh is one encoding bitrate version in the bitrate profile
{ηh | h = 01,…,H-1} (total H versions), and the output bt is the
final bitrate decision for segment t.
The critic network shares a similar structure with the actor
network, but differs in two key aspects: its input and output
layers. On the input side, in addition to the five environment
states (i.e., the input of the actor network), the critic network also
receives the action at output by the actor network (corresponding
to the current state). This additional input allows the critic
network to evaluate the quality of a given state–action pair. On
the output side, unlike the actor network that outputs an action,
the critic network outputs a scalar Q-value (associated with the
input state–action pair), which is used to compute the temporal
difference (TD) error, that in turn guides the update of the
neural network during training. It is worth noting that the target
critic network and target actor network adopt exactly the same
architecture as their respective primary networks (critic and
actor), and are used solely for stabilizing the training process.
Therefore, their structural details are omitted here for brevity.
The running procedure of the temporal module is described
in Algorithm 2. Specifically, in one streaming session, for each
video segment t, the environment state st is fed into the actor-
network to obtain action at which is then mapped to the available
bitrate version according to (7). Under the bitrate decision,
segment t will be streamed in a virtual streaming environment
[10], and then the resultant reward rt (quantified by the QoE
function like (1)) and new state st+1 will be obtained. These
metrics will be formulated into a 4-factor tuple, denoted by (st,
at, rt, st+1,), and stored into an experience buffer Π (c.f. line 1
∼line 6 in Algorithm 2). Then, from Π, BETA will randomly
sample a batch of tuple sequences, denoted by Ω, each consisting
of n consecutive tuples (line 7):
Ω ←

(st′+i, at′+i, rt′+i, st′+1+i)i=0,1,...n−1

(8)
where the tuples are sorted by segment index i = 01,…,n-1.
Each tuple sequence in Ω contains the state-action pairs and the
corresponding rewards of n consecutive segments (steps), which
gives long-term environmental feedback to the bitrate decisions
made by the neural network. These historical experiences will
be further fed back into the training process, offering the neural
network a long-term decision horizon.
To incorporate the experiences into the training, BETA uses
the data in Ω for calculating a target Q value (line 8):
Qtar =

n−1

i=0
βirt′+i


+ βn min (Qtar1, Qtar2)
(9)
where Qtar1 and Qtar2 are the Q-values output by the two target-
critic-networksrespectively,rt’+i istherewards(i.e.,QoE)ofthe
ith segment in Ω (c.f. (8)), β is a discount factor, and n is the total
tuple number. The detailed implementation for calculating target
Q value Qtar is described by the function Compute_Target_Q(.)
in Algorithm 2 (line 17 ∼line 24).
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.
```

### Página 8

```text
ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING
12859
On this basis, the next step is to update the two critic-networks
Qθ1 and Qθ2. The objective is to make the Q-value output by the
critic-networks close to the target Q value Qtar through tuning
the neuron weights θj = 12 of the two critics respectively (line
9). This step is implemented via executing a deterministic policy
gradient to minimize the following loss function:
minθj


Qθj (st′, at′) −Qtar

2, j = 1, 2
(10)
where state st’ and action at’ are in the first tuple in the tuple
sequence Ω (i.e., index i = 0, see (8)). The actor-network πφ will
then be updated by gradient descent based on the newly learned
critic-network-1 Qθ1 to maximize its output Q-value (line 11):
maxφQθ1 [st′, πφ(st′)]
(11)
where state st’ is in the first tuple of the tuple sequence Ω. The
intuition behind (8) ∼(11) is to give the two critic-networks a
longer-termviewsothattheycanmoreaccuratelyassesstheben-
efits derived from the actions made by the current actor-network.
In this way, as the training proceeds, the ABR algorithm, i.e.,
the actor-network, will be gradually offered the ability to make
far-sighted decisions.
At the end of each training epoch, all target networks, in-
cluding the target actor and the two target critic networks,
are updated using an exponential weighted moving average
(EWMA) policy. This soft update mechanism incrementally
incorporates the parameters of the newly updated actor and critic
networks into their corresponding target networks (line 12),
thereby enhancing training stability and mitigating oscillations.
After a sufficient number of training epochs, the learning process
converges, and the final actor network is exported as the trained
ABR decision model, which is subsequently deployed in the
streaming environment to make bitrate adaptation decisions
(line 16).
IV. PERFORMANCE EVALUATION
In this section, we evaluated the performance of BETA and
compared it to the state-of-the-art ABR algorithms. In addition,
we explored the underlying factors that contribute to BETA’s
superiority.
A. Experimental Setup
Baseline: To benchmark the performance of BETA, we imple-
mented six state-of-the-art ABR algorithms. These include: 1)
Two basic algorithms: MPC [7] (heuristic-based), and Pensieve
[10] (DRL-based); 2) Four algorithms that focus on improving
the ABR generalization: PSQA [5] (parameter-tunning), EAS
[3] (ensemble learning), Genet [18] (curriculum learning), and
Merina [4] (meta reinforcement learning). A comprehensive
review of these ABR approaches is shown in Section V.
BETA parameter: The default setting of the hyperparameters
of BETA is summarized in Table III. A sensitivity analysis
examining their impact will be presented in Section IV-E. Ad-
ditionally, the streaming environment settings, including video
segmentation, bitrate ladder, and network trace characteristics,
are described in detail in Section II.
TABLE III
BETA PARAMETERS
TABLE IV
COMPARISON OF QOE ACROSS SEVEN ABR ALGORITHMS
Performance metrics: To evaluate the QoE comprehensively,
the QoE function in Eq. (1) is further extended to three variants
(based on Mao et al. [10]) in terms of the mapping from bitrate
bt (segment t) to video quality F(.):
r QoElin maintains a linear relationship between bitrate and
video quality, i.e., F(bt) = bt. The penalty coefficient σ =
50;
r QoElog maintains a log relationship between bitrate and
video quality, i.e., F(bt) = log(bt/rmin), rmin = 0.2 Mbps.
The penalty coefficient σ = 5.52;
r QoEhd prefers high video quality: if bt<5 Mbps, then
F(bt) = 1.6bt+1; if 5 Mbps<bt<10 Mbps, then F(bt) =
1.6bt+25; if 10 Mbps<bt<50 Mbps, then F(bt) =
1.6bt+50. The penalty coefficient σ = 30.
B. QoE Performance
Table IV summarizes the QoE performance of the seven ABR
algorithms under three different QoE functions, as defined in
Section IV-A. Across all three cases, the proposed BETA con-
sistently outperforms the state-of-the-art baselines, achieving a
14.8% to 37.9% improvement in mean QoE. To further illustrate
the distributional characteristics, Fig. 3 presents the Cumulative
Distribution Function (CDF) of per-session QoE. Compared to
other algorithms, BETA yields a significantly lower proportion
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.
```

### Página 9

```text
12860
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025
Fig. 3.
Cumulative Distribution Function (CDF) distributions of per-
streaming-session QoE performance.
Fig. 4.
Comparison of bitrate and rebuffering over 7 ABR algorithms.
of poor-performing sessions (i.e., QoE < 0) and a higher con-
centration of high-performing sessions, which contributes to its
superior mean performance.
Among the comparison algorithms, EAS achieves the most
consistent performance across the three QoE functions, within
83.8% to 84.7% of BETA’s QoE. In contrast, other algorithms
exhibit more variability. For instance, Merina performs poorly
under the Linear QoE (normalized score of 0.661), due to a
high fraction of sessions with substantial rebuffering events, but
performs better under the HD QoE (score of 0.806). Others, such
as PSQA and MPC, show similar trends with Merina.
Fig. 4 compares the average video bitrate and rebuffering du-
ration across all algorithms. The results are particularly insight-
ful. Although BETA achieves the best QoE, its selected bitrate
is not always the highest. Instead, it maintains a consistently low
rebuffering duration, especially under the Linear and Log QoE
functions where rebuffering carries a greater penalty weight.
In contrast, under the HD QoE, which emphasizes high video
quality, BETA adapts by selecting higher bitrates at the expense
of slightly increased rebuffering. These results reflect BETA’s
ability to adapt its ABR policy flexibly in accordance with the
varying objective functions.
Among the three QoE functions, only the Linear QoE directly
uses bitrate to represent video quality. The Log and HD QoE
functions apply nonlinear mappings (see Section IV-A). To
better assess the actual video quality across algorithms, we
replaced the bitrate values on the x-axis of Fig. 4 with their
corresponding quantified video quality scores, and re-plotted
the results in Fig. 5. The overall trends remain consistent: BETA
achieves the most favorable trade-off between video quality and
rebuffering, offering a principled explanation for its superior
QoE performance across all evaluation criteria.
C. Network Robustness
To assess whether the ABR Under-Generalization problem
is effectively addressed, we evaluated the network robustness
Fig. 5.
Comparison of video quality and rebuffering over 7 algorithms.
Fig. 6.
QoE comparison over three different network conditions. Low
(0∼15 Mbps), Medium (15∼25 Mbps), and High (>25 Mbps) are three network
trace datasets with different mean throughputs.
of each algorithm by comparing their QoE performance under
varying network conditions, as shown in Fig. 6. Specifically, the
network traces were partitioned into three subsets based on their
mean throughput: low (0∼15 Mbps), medium (15∼25 Mbps),
and high (>25 Mbps), to reflect different ranges of realistic
operating environments.
In Fig. 6 (upper left), BETA consistently outperforms all
baseline algorithms across the three network conditions. In the
mixed network setting, BETA achieves 19.4% to 50.9% higher
mean QoE. More notably, under the low-throughput condition,
which is characterized by greater variability and constrained
bandwidth, BETA’s advantage is even more pronounced, achiev-
ing up to 244.1% improvement over the weakest baseline and at
least 39.3% over the strongest one. The primary driver behind
this performance gain is BETA’s ability to significantly reduce
rebuffering events, as illustrated in Fig. 6 (lower left). Across
all network subsets, BETA consistently records the shortest re-
bufferingduration,highlightingitsrobustnessinadaptingtoboth
bandwidth-limited and highly fluctuating network conditions.
For a deeper understanding of BETA’s superiority, in Fig. 7(a),
we plotted its buffer dynamics under the three network con-
ditions to see its ABR decision behavior. The differences are
readily apparent across the three cases. For example, at the low
network, it is clear that the buffer level of BETA is higher
than that of the other two cases (i.e., the medium and the
high networks). It intentionally selects the bitrates much lower
than the measured throughput because the network condition is
judged to be poor and high measured throughput is treated as the
exception that is unlikely to last. Thus, maintaining a high buffer
level would effectively prevent the potential rebuffering events
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.
```

### Página 10

```text
ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING
12861
Fig. 7.
Buffer dynamics over three different network conditions. Low (0∼15
Mbps), Medium (15∼25 Mbps), and High (>25 Mbps) are three network trace
datasets with different mean throughputs.
in the future. At the medium network, BETA is more moderate
and balanced. At the high network, the buffer level is much lower
because BETA is more aggressive and even occasionally selects
bitrates higher than the measured throughput. The intuition is
that the low measured throughput at the high network is likely
short-term so keeping high bitrates can prevent unnecessary
QoE degradations. Overall, BETA’s behavior fundamentally
stems from its flexible tuning of ABR adaptation aggressiveness,
which enables it to make not only fine-grained decisions but also
long-sighted planning.
Among these comparison algorithms, some have generaliza-
tion awareness such as PSQA [5], EAS [3], Genet [18], and
Merina [4]. To see their effectiveness, we plotted the buffer
TABLE V
COMPARISON OF QOE ACROSS SEVEN DRL METHODS
Fig. 8.
Comparison of training QoE over seven DRL methods.
dynamics in Fig. 7 (note that due to the similarity of the results,
we only show the results of EAS and Merina in Fig. 7(b) and
(c), respectively). It is observed that both EAS and Merina
perform differently from BETA. For example, the buffer level
of EAS is roughly consistent regardless of whether the network
fluctuates drastically or not in the three network conditions,
which is due to its dynamic ABR aggressiveness adjustment.
While such decisions can effectively reduce rebuffering, the
network resources cannot be fully utilized especially when the
network is high. By contrast, Merine’s ABR is far less flexible.
It has much less buffering in the low network than in the medium
and high networks, so significant rebuffering and underutilized
network resources are inevitably incurred.
D. Training Efficiency
BETA’s model training plays a decisive role in its superior
performance. In Section II, we evaluated the training efficiency
of the existing DRL methods. In this section, we will compare
BETA to the existing ones in terms of QoE, video bitrate, re-
buffering, and quality variations. The results are summarized in
Table V. It is observed that the QoE of BETA is much better than
the existing DRLs by 19.1% ∼25.0%. The major contributor
is the substantial rebuffering reduction, by 37.3% ∼143.1%.
While the bitrate and the quality variation achieved by BETA
are not the best among all these methods, BETA maintains a
more balanced result between the three metrics, offering a better
overall QoE (i.e., the optimization objective of the training).
To further investigate the training behavior of the evaluated
DRL methods, Fig. 8 presents the evolution of QoE over training
epochs(x-axis). Importantly, QoE is evaluated on a validation
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.
```

### Página 11

```text
12862
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025
Fig. 9.
Ablation analysis for temporal and spatial modules of BETA.
trace set, which is completely isolated from the training set
to ensure generalization assessment. From the figure, we ob-
served that although BETA converges more slowly compared
to methods such as DDPG and SAC, it ultimately achieves
substantially higher QoE. In contrast, the baseline DRL methods
exhibit significant instability, particularly TD3 and DDPG, both
of which suffer sharp QoE drops after reaching early peaks,
suggesting possible overfitting or poor generalization.
BETA’s training framework integrates two key modules: the
Temporal Module and the Spatial Module (refer to Section III).
To assess their individual contributions, we performed an ab-
lation study, comparing two reduced versions of BETA against
the full. The first variant, BETA_w/o_Temporal, excludes the
temporal module while retaining the spatial one. The second,
BETA_w/o_Spatial, removes the spatial module but preserves
the temporal logic. As shown in Fig. 9, both variants exhibit
significant degradation in QoE compared to the full version
of BETA. In particular, the removal of either module leads to
a marked increase in rebuffering duration and a reduction in
average bitrate, indicating that both modules are essential to
achieving BETA’s robust performance.
In Section IV-C, we plotted the buffer dynamics to gain insight
into the network robustness of ABR decisions, where BETA
can dynamically adjust the ABR aggressiveness across different
network conditions (see Fig. 7(a)). To uncover which module
of BETA achieves this efficacy, we plot the buffer dynamics
of BETA_w/o_Spatial (i.e., removing the spatial module) in
Fig. 7(d). However, it shows a pattern very similar to the full
version of BETA (Fig. 7(a)). To this end, we further removed the
temporal module from BETA_w/o_Spatial, leaving the rest as
theoriginalTD3[14]toobservetheeffect.InFig.7(e),thediffer-
ences begin to emerge (compared to BETA_w/o_Spatial), with
TD3’s buffer being more consistent across the three networks.
This result clearly demonstrates the efficacy of BETA’s temporal
module, which gives the trained ABR model a long-term view
and more flexibility to make decisions for specific networks.
E. Sensitivity Analysis
In BETA, some key parameters may significantly affect its
performance so we conducted a sensitivity analysis on them.
First, in the temporal module of the training, there is a look
ahead horizon including n consecutive segments to calculate the
expectedreward(c.f.SectionIII-C).ThisiskeytoBETAbecause
it provides a long-sighted view of the training ABR model. To
see its effects on QoE, we tuned the value from 1 to 40 and then
plotted the result in Fig. 10-left. We observed that the QoE peaks
Fig. 10.
Sensitivity analysis on the key parameters of BETA.
at the value of 5 and too small/large a value degrades the result.
This indicates that it is not as intuitive that a longer look ahead
horizon brings better performance.
The second key parameter works in the spatial module of
the training which is a pre-defined QoE threshold (i.e., the
gap between the actual QoE and the offline optimal) for the
classification of the normal-performed and under-performed
network traces (c.f. Section III-B). We tuned its value from 100
to 2000 to see the effect on QoE and classification accuracy. In
Fig.10-middle,itisobservedthatastheQoEthresholdincreases,
the classification accuracy keeps increasing. This is expected
because the larger the threshold, the easier it is to segregate
the two types of traces. However, the QoE shows a different
pattern which peaks at 700. From 700 to 2000 (QoE threshold),
even though the classification accuracy increases, the QoE drops
substantially. The reason is that, at runtime, the classification
inevitably has errors. If this is not shown to the ABR model
during the offline training, then the trained ABR model cannot
get the knowledge to cope with such errors. As a result, the
ABR model takes erroneous behaviors at runtime, degrading
the resultant QoE.
The third parameter is the network trace length which is the
length of the input data for the binary classifier in the spatial
module of the training. We tuned its value from 20 sec to 400
sectoseeitseffectontheclassificationaccuracy.InFig.10-right,
as expected, the QoE increases as the length gets longer because
the classifier is able to obtain more comprehensive knowledge
with more historical traces.
To further validate the robustness of the setting of the QoE
threshold, we partitioned the evaluation network data both tem-
porally and spatially. Notably, the network trace data [36] was
collected from real mobile networks over a span of 77 consec-
utive days. The collection sites encompass a diverse range of
geographic locations, including subways, campuses, shopping
malls, and more.
First, we divided the network data temporally into four groups
based on their collection time: 0:00–6:00, 6:00–12:00, 12:00–
18:00, 18:00–24:00. We then conducted a sensitivity analysis
for the QoE threshold across each of these time-based groups.
The results, presented in Table VI, consistently indicate that a
QoE threshold of 700 achieves the highest QoE performance
across all four cases. Second, to assess the sensitivity spatially,
we further extracted three groups of network data collected
from different geographic locations. The results, presented in
Table VII, show that the QoE threshold of 700 consistently
achieves the highest QoE across all three cases.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.
```

### Página 12

```text
ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING
12863
TABLE VI
TEMPORAL SENSITIVITY OF THE QOE THRESHOLD
TABLE VII
SPATIAL SENSITIVITY OF THE QOE THRESHOLD
TABLE VIII
Q VALUE ESTIMATION METHODS
In conclusion, the QoE threshold keeps stable across the
diverse network environments. This stability stems from the
fact that the QoE threshold quantifies the performance gap
between the actual QoE and the offline optimum within each
video session. Since this gap is a relative measure, it is largely
unaffected by variations in network environments. For example,
in a low-bandwidth environment, both the actual QoE and the of-
fline optimal QoE tend to be lower, whereas in a high-bandwidth
environment, both values are higher. Thus, the relative QoE gap
keeps fairly consistent across the two scenarios. Therefore, there
is no need to fine-tune the QoE threshold for different network
environments.
At last, we test some training parameters. The first is the
Q-value estimation method. We tested two candidate methods:
oneistheQ-valueestimatedbycalculatingtheaverageofthetwo
target values; the other is the smaller of the two target Q-values.
As shown in Table VIII, the former one achieves only 93% of
the performance compared to the latter one. This difference can
be attributed to the fact that taking the smaller of the two target
Q-values helps effectively avoid Q-value overestimation. The
overestimation primarily results from the randomness in the
estimation process, such as the random tuple sampling from
the experience buffer.
The next is the training update frequency, which refers to the
number of epochs between two updates of the actor network.
We tuned it within the range 1 ∼32 to assess its impact on
QoE performance and training speed. As shown in Table IX,
as the epoch number increases, the QoE initially increases and
then decreases, with the peak performance occurring at = 4,
TABLE IX
TRAINING UPDATE FREQUENCY
TABLE X
ACTION NOISE INTRODUCTION
TABLE XI
ONLINE COMPLEXITY ANALYSIS
representing a 6% improvement compared to = 1. Additionally,
the training speed improves as the epoch number increases. This
is expected because when the epoch number between updating
theActorisincreased,thesystemrequiresfewerupdates,leading
to less computational resource consumption.
The third is the Action noise, which is to avoid premature
convergence. To test its impact on QoE, we varied the standard
deviation of the action noise within 0.0 to 2.0, where 0 represents
no action noise. As shown in Table X, the QoE performance is
degraded when the noise is either too small or too large. The
best performance is achieved with a standard deviation of 1.0,
demonstrating that this level of action noise provides the optimal
balance for enhancing QoE.
F. Complexity Analysis
In the last experiment, we evaluated the complexity of the
ABR algorithms. We quantify the complexity with the practical
algorithmic runtime and the average memory occupancy eval-
uated in the online streaming phase. Table XI summarizes the
result where the algorithmic runtime is the accumulation of 100
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.
```

### Página 13

```text
12864
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025
streaming sessions (a total of 19200 sec), and the memory occu-
pancy is the average usage of each second. First, it is observed
that PSQA and MPC have significantly longer runtimes (249.9
sec and 226.5 sec) than others. This is because the ABR decision
of the two requires repeated querying of the hash tables [5],
[7] while all other algorithms adopt neural networks that have
a faster mapping speed. Second, Merina occupies the largest
memory usage (1188.7 MByte) among the all, which is due
to the meta-reinforcement-learning that holds a more complex
neural network structure [4], [34]. Third, in both the algorithmic
runtime and the memory occupancy, the complexity of BETA is
moderate among all the algorithms.
Next, regarding the resource-intensive nature of computing
the offline optimal, we provided a complexity analysis for the
offlinetrainingofBETA(thetrainingincludestheofflineoptimal
computation). The computing server specifications are: CPU –
Intel Xeon Platinum 8375C @ 2.90 GHz; CPU cores – 128;
Motherboard – R0K8F35; Operating system – Ubuntu 22.04
LTS; Memory – 256 GB; GPU – NVIDIA GeForce RTX 4090;
GPU Cores – 2.
The training complexity is summarized as follows:
r DRL training speed – 96 epochs per minute
r Total DRL training time – 2∼2.5 hours
r GPU utilization – 8%
r Memory consumption – 0.45 GB
r Offline optimal computation (using the dynamic program-
ming algorithm with a time granularity of 0.05) – 1 hour
for 1000 epochs
Overall, the offline training of BETA is typically completed
within 4 hours, making the computational overhead manageable
within a standard server environment.
V. RELATED WORK
Over the past decade, adaptive video streaming has undergone
significant advancements under the standardization protocol of
DASH [2], [33]. In this section, we provide a structured review
of the existing ABR research.
Heuristic-based ABR: Heuristic-based algorithms rely on pre-
defined rules. For example, Jiang et al. [6] proposed FESTIVE,
which selects the bitrate based on the harmonic mean of past
throughput. Spiteri et al. [8] developed BOLA, which uses buffer
occupancy and Lyapunov optimization for decision-making. Yin
et al. [7] introduced RobustMPC, which formulates bitrate selec-
tion as a QoE maximization problem. Akhtar et al. [9] proposed
Oboe, which dynamically adjusts RobustMPC’s discount factor
to better adapt to network variability. Zuo et al. [19] designed
Ruyi, which incorporates user preferences into QoE optimiza-
tion. Xu et al. [20] presented Karma, using causal sequence
modeling for adaptive decisions. Chen et al. [21] proposed
SODA, which applies smoothed online convex optimization to
reduce quality fluctuations.
Learning-based ABR: The other branch leverages deep rein-
forcement learning (DRL) to train ABR algorithms. For exam-
ple, Pensieve [10] is one of the earliest DRL-based methods,
using A3C [12] for policy learning. Several follow-up imple-
mentations have explored alternative DRL algorithms, such as
PPO [22], SAC [23], and DQN [24]. More recent advancements
include DeepBuffer [25], a buffer-aware ABR algorithm trained
via DCPPG; Jade [26], which incorporates human feedback
to align decisions with QoE preferences; and Incendio [27],
which uses multi-agent reinforcement learning [37] with expert
guidance. Other notable examples include GreenABR [28], an
energy-efficient ABR model trained via DQN; CAST [29],
which employs self-play DRL to consider video scene complex-
ity; and a data-wastage-aware ABR algorithm by Zhang et al.
[30], trained with A3C to reduce bandwidth inefficiency.
Generalization-Aware ABR Solution: To address the ABR
Under-Generalization problem, several representative solutions
have been proposed in recent years. PSQA [5], developed by
Zhang et al., provides a general framework for tuning internal
ABR parameters for specific network conditions. EAS [3], also
by Zhang et al., constructs an ensemble of ABR models tailored
to different mean throughput levels. Genet [18], proposed by
Xia et al., adopts curriculum learning to dynamically adjust the
training data distribution to improve generalization. In parallel,
meta-reinforcement learning has been explored by Kan et al.
[4] and Bentaleb et al. [11], both of which employ an auxiliary
feature extraction network to enable rapid adaptation of the ABR
policy to diverse networks.
Discussion: The key limitation of the existing ABR algo-
rithms, including both heuristic-based and learning-based ap-
proaches, is that they typically rely on a single ABR model
(e.g., a standalone neural network), as seen in the state-of-the-art
algorithms such as the A3C-based Pensieve [10], the curriculum
learning-basedGenet[18],andthemeta-reinforcementlearning-
based Merina [4]. However, real-world network conditions are
highly complex and characterized by diverse features, some of
which cannot even be quantified. As a result, the solo ABR
model struggles to incorporate all the network features effec-
tively and fails to achieve balanced results in heterogeneous net-
work environments. This is the key cause of the generalization
issue.
Fundamentally, BETA differs from the existing ABR algo-
rithms.Itfirstclassifiesthenetworkdataofallstreamingsessions
into two categories by analyzing the gap between the actual
QoE and the offline optimal QoE of each session. Sessions with
a large QoE gap are labeled as poor-performing, while those
with a small gap are considered normal. BETA then trains two
distinct ABR models for these two categories. At runtime, it
dynamically switches between the two models based on real-
time network conditions. This design provides a practical and
effective solution to the long-standing generalization issue in
ABR decision-making.
VI. CONCLUSION AND FUTURE WORK
This work reveals the ABR Under-Generalization problem
that exists in the state-of-the-art ABR algorithms. To address
this problem, we proposed BETA, a novel DRL-based ABR
framework that incorporates spatial and temporal modules to
enhance generalization across diverse network environments.
Extensive evaluations demonstrate that BETA consistently out-
performs the existing algorithms in terms of QoE, while also
exhibiting strong robustness. This indicates that it effectively
overcomes the generalization problem.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.
```

### Página 14

```text
ZHANG et al.: NOVEL SPATIAL-TEMPORAL LEARNING METHOD FOR ENHANCING GENERALIZATION IN ADAPTIVE VIDEO STREAMING
12865
While BETA focuses on improving generalization with
respect to network conditions, real-world streaming scenar-
ios involve broader challenges, including heterogeneous QoE
preferences, evolving user behaviors, and device diversity. Ad-
dressing these aspects remains a promising direction for future
research.
ACKNOWLEDGMENT
The authors wish to thank the associate editor and the anony-
mous reviewers for their insightful comments in improving this
paper.
REFERENCES
[1] Cisco Visual Networking Index: Global Mobile Data Traffic Forecase
Update, 2017-2022. San Jose, CA, USA: Cisco Inc., Mar. 2020. [Online].
Available:
https://www.cisco.com/c/en/us/solutions/collateral/service-
provider/visual-networking-index-vni/white-paper-c11-741490.html
[2] T. Stockhammer, “Dynamic adaptive streaming over HTTP: Standards
and design principles,” in Proc. ACM Conf. Multimedia System, 2011,
pp. 133–144.
[3] G. Zhang and J. Lee, “Ensemble adaptive streaming – A new paradigm to
generate streaming algorithms via specializations,” IEEE Trans. Mobile
Comput., vol. 19, no. 6, pp. 1346–1358, Jun. 2020.
[4] N. Kan, Y. Jiang, C. Li, W. Dai, J. Zou, and H. Xiong, “Improving
generalization for neural adaptive video streaming via meta reinforcement
learning,” in Proc. ACM Int. Conf. Multimedia, 2022, pp. 3006–3016.
[5] G. Zhang, J. Zhang, Y. Liu, H. Hu, J. Y. B. Lee, and V. Aggarwal,
“Adaptive video streaming with automatic quality-of-experience opti-
mization,” IEEE Trans. Mobile Comput., vol. 22, no. 8, pp. 4456–4470,
Aug. 2023.
[6] J.Jiang,V.Sekar,andH.Zhang,“Improvingfairness,efficiency,andstabil-
ity in HTTP-based adaptive video streaming with FESTIVE,” IEEE/ACM
Trans. Netw., vol. 22, no. 1, pp. 97–108, Feb. 2014.
[7] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A Control-Theoretic Ap-
proach for Dynamic Adaptive Video Streaming over HTTP,” in Proc. ACM
Special Int. Group Data Commun., London, U.K., 2015, pp. 325–338.
[8] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal
bitrate adaptation for online videos,” IEEE/ACM Trans. Netw., vol. 28,
no. 4, pp. 1698–1711, Aug. 2020.
[9] Z. Akhtar, Y. S. Nam, and R. Govindan, “Oboe: Auto-tuning video ABR
algorithms to network condition,” in Proc. ACM Special Int. Group Data
Commun., 2018, pp. 44–58.
[10] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video streaming
with pensieve,” in Proc. ACM Special Int. Group Data Commun., 2017,
pp. 197–210.
[11] A. Bentaleb, M. Lim, M. N. Akcay, A. C. Begen, and R. Zimmermann,
“Meta reinforcement learning for rate adaptation,” in Proc. IEEE Conf.
Comput. Commun., 2023, pp. 1–10.
[12] V. Mnih, A. P. Badia, M. Mirza, and A. Graves, “Asynchronous methods
for deep reinforcement learning,” in Proc. Int. Conf. Mach. Learn., 2016,
pp. 1928–1937.
[13] T. Lillicrap et al., “Continuous control with deep reinforcement learning,”
Sep. 2015, arXiv:1509.02971.
[14] S. Fujimoto, H. Hoof, and D. Meger, “Addressing function approximation
error in actor-critic methods,” in Proc. Int. Conf. Mach. Learn., 2018,
pp. 1587–1596.
[15] V. Mnih et al., “Human-level Control through Deep Reinforcement Learn-
ing,” Nature, vol. 518, no. 7540, pp. 529–533, Feb. 2015.
[16] J.Schulman,F.Wolski,P.Dhariwal,A.Radford,andO.Klimov,“Proximal
Policy optimization algorithms,” 2017, arXiv:1707.06347.
[17] T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine, “Soft actor-critic: Off-
policy maximum entropy deep reinforcement learning with a stochastic
actor,” in Proc. Int. Conf. Mach. Learn., 2018, pp. 1861–1870.
[18] Z. Xia, Y. Zhou, F. Y. Yan, and J. Jiang, “Genet: Automatic curriculum
generation for learning adaptation in networking,” in Proc. ACM Special
Int. Group Data Commun., 2022, pp. 397–413.
[19] X. Zuo, J. Yang, M. Wang, and Y. Cui, “Adaptive bitrate with user-level
QoE preference for video streaming,” in Proc. IEEE Conf. Comput. Com-
mun., 022, pp. 1279–1288.
[20] B. Xu, H. Chen, and Z. Ma, “Karma: Adaptive video streaming via
causal sequence modeling,” in Proc. ACM Int. Conf. Multimedia, 2023,
pp. 1527–1535.
[21] T. Chen et al., “SODA: An adaptive bitrate controller for consistent high
quality video streaming,” in Proc. ACM Special Int. Group Data Commun.,
2024, pp. 1–14.
[22] “PensieveimplementedbyPPO,”2021,[Online].Available:https://github.
com/godka/Pensieve-PPO
[23] “Pensieve implemented by SAC,” 2021, [Online]. Available: https://
github.com/godka/Pensieve-SAC
[24] “Pensieve implemented by DQN,” 2021, [Online]. Available: https://
github.com/godka/Pensieve-PPO/tree/dqn
[25] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, and L. Sun, “Buffer awareness
neural adaptive video streaming for avoiding extra buffer consumption,”
in Proc. IEEE Conf. Comput. Commun., 2023, pp. 1–10.
[26] T. Huang, R. Zhang, C. Wu, and L. Sun, “Optimizing adaptive video
streaming with human feedback,” in Proc. ACM Int. Conf. Multimedia,
2023, pp. 1707–1718.
[27] Y. Li, Q. Zheng, Z. Zhang, H. Chen, and Z. Ma, “Improving ABR
performance for short video streaming using multi-agent reinforcement
learning with expert guidance,” in Proc. Workshop Netw. Operating System
Support Digit. Audio Video, 2023, pp. 58–64.
[28] B. Turkkan et al., “GreenABR+: Generalized energy-aware adaptive
bitrate streaming,” ACM Trans. Multimedia Comput. Commun. Appl.,
vol. 20, 2024, Art. no. 269.
[29] W. Li et al., “Optimizing video streaming in dynamic networks: An
intelligent adaptive bitrate solution considering scene intricacy and data
budget,” IEEE Trans. Mobile Comput., vol. 23, no. 12, pp. 12280–12297,
May 2024.
[30] G. Zhang et al., “DUASVS: A mobile data saving strategy in short-
form video streaming,” IEEE Trans. Serv. Comput., vol. 16, no. 2,
pp. 1066–1078, Mar. 2023.
[31] “Video streaming emulator,” 2017, [Online]. Available: https://github.
com/hongzimao/pensieve
[32] “The source code of BETA,” 2024, [Online]. Available: https://github.
com/ZM-SDUr/BETA/
[33] “dash.js,” 2014, [Online]. Available: https://github.com/Dash-Industry-
Forum/dash.js/wiki
[34] W. Du, L. Geng, J. Liu, Z. Zhao, C. Wang, and J. Huo, “Decoupled
knowledge distillation method based on meta-learning,” High-Confidence
Comput., vol. 4, no. 1, Mar. 2024, Art. no. 100164.
[35] Z. Wang, G. Zhang, M. Xiao, D. Yu, and X. Cheng, “BETA: A novel
learning-based adaptive streaming approach with spatial and temporal
optimization,” in Proc. IEEE Int. Conf. Sens. Commun. Netw., Phoenix,
AZ, USA, 2024, pp. 1–9.
[36] “Network trace data,” 2022, [Online]. Available: https://github.com/
Streaming-code/TraceData/releases/tag/TraceData
[37] H. Liu, “Cooperative multi-agent game based on reinforcement learning,”
High-Confidence Comput., vol. 4, no. 1, Mar. 2024, Art. no. 100205.
Guanghui Zhang received the PhD degree from
the Department of Information Engineering, Chinese
University of Hong Kong, in 2020, and the MS degree
in electronic science and technology from Peking
University, in 2016. He is currently a professor with
the School of Computer Science and Technology,
Shandong University, China. From 2020 to 2022, he
worked as a postdoctoral researcher with the Chinese
University of Hong Kong, and then as a research
assistant professor with the Hong Kong Baptist Uni-
versity. His research interests include broadly lies in
networking systems, multimedia systems, and machine learning.
Ziming Wang is currently working toward the MSc
degree with the School of Computer Science and
Technology, Shandong University, China. His re-
search interests include broadly lies in networking
systems, multimedia systems, and machine learning.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.
```

### Página 15

```text
12866
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 24, NO. 12, DECEMBER 2025
Huaren Wei is currently working toward the MSc
degree with the School of Computer Science and
Technology, Shandong University, China. His re-
search interests include broadly networking systems,
multimedia systems, and machine learning.
Mengbai Xiao received the MS degree in software
engineering from the University of Science and Tech-
nology of China, in 2011, and the PhD degree in com-
putersciencefromGeorgeMasonUniversity,in2018.
HeisaprofessorwiththeSchoolofComputerScience
and Technology, Shandong University, China. He was
a postdoctoral researcher with the HPCS Lab, Ohio
State University. His research interests include mul-
timedia systems, parallel and distributed systems. He
has published papers in prestigious conferences, such
as ACM Multimedia, ACM ICS, IEEE ICDE, IEEE
ICDCS, and IEEE INFOCOM.
Hui Yuan (Senior Member, IEEE) received the BE
and PhD degrees in telecommunication engineer-
ing from Xidian University, Xi’an, China, in 2006
and 2011, respectively. In 2011, he joined Shan-
dong University, Ji’nan, China, as a lecturer (April
2011–December 2014), an associate professor (Jan-
uary 2015-August 2016), and a professor (September
2016). His research interests include 3D visual media
coding and communication.
Dongxiao Yu (Senior Member, IEEE) received the
BS degree in mathematics from Shandong University,
in 2006, and the PhD degree in computer science from
the University of Hong Kong, in 2014. He became
an associate professor with the School of Computer
Science and Technology, Huazhong University of
Science and Technology, in 2016. Currently, he is a
professor with the School of Computer Science and
Technology, Shandong University. His research inter-
ests include wireless networking, distributed comput-
ing, and graph algorithms.
Xiuzhen Cheng (Fellow, IEEE) received the MS and
PhD degrees in computer science from the Univer-
sity of Minnesota – Twin Cities, in 2000 and 2002,
respectively. She was a faculty member with the De-
partment of Computer Science, George Washington
University, from 2002-2020. Currently, she is a pro-
fessor of computer science with Shandong Univer-
sity, Qingdao, China. Her research interests include
focuses on blockchain computing, IOT Security, and
privacy-aware computing.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.
```
