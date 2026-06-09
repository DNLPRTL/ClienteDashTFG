# A2BR: Learning Tailored Adaptive Bitrate Algorithms to Heterogeneous Network Conditions
**Archivo PDF:** `A2BR.pdf`  **Identificador:** `09_a2br_2022_meta_rl_domain_priors`  **Páginas:** 19  **SHA256 PDF:** `93ec68c16c45abb61d8defbed05e1c82bb236ce038df4a9c5c94356c36edd83a`  **Foco para Fase 4-5 v1:** Meta-RL ABR; domain-specific priors; IMDP framing; online adaptation to heterogeneous network conditions.
> Documento Codex-ready generado para diseño de nuevos modelos/controllers IA ABR. No es una source card corta. Contiene extracción técnica cruda y organizada. El PDF original sigue siendo la fuente de verdad para fórmulas, tablas y figuras si la extracción textual pierde layout.
## 1. Cómo usar este `.md`
- Leer primero secciones 2-5 para ubicar método, señales, datos, evaluación y limitaciones.
- Usar la extracción por categorías como material de diseño/contrato/Codex.
- Para ecuaciones, tablas o figuras críticas, comprobar la página indicada en el PDF original.
- No convertir resultados del paper en promesas directas para DashClientModular4; deben transformarse en hipótesis, guardrails y tests Phase 6.
## 2. Metadatos extraídos
- **format:** PDF 1.4
- **title:** Learning Tailored Adaptive Bitrate Algorithms to Heterogeneous Network Conditions: A Domain-Specific Priors and Meta-Reinforcement Learning Approach
- **subject:** IEEE Journal on Selected Areas in Communications;2022;40;8;10.1109/JSAC.2022.3180804
- **creator:** Aspose Ltd.
- **producer:** Aspose.Pdf for .NET 8.3.0; modified using iText® 7.1.1 ©2000-2018 iText Group NV (AGPL-version)
- **creationDate:** D:20220701190110+05'30'
- **modDate:** D:20220714152637-04'00'

## 3. Índice de secciones detectadas
- p.1: Abstract—Internet adaptive video streaming is a typical form
- p.1: results also illustrate the superiority of A2BR in adapting to the
- p.1: I. INTRODUCTION
- p.2: II. BACKGROUND AND MOTIVATION
- p.3: methods [11], [23]. Unfortunately, such one-fits-all schemes,
- p.3: TABLE I
- p.3: COMPARISON RESULTS ON DIFFERENT ABRS OVER 3G-CAR AND
- p.4: III. METHODS
- p.5: IV. A2BR OVERVIEW
- p.8: method, shown in Eq. 15. The key principle of the mask is to
- p.8: V. EVALUATION
- p.9: TABLE II
- p.9: RESULTS OF EXPERIMENT IN DIFFERENT VEHICLES, SUMMARIZED IN VMAF [22] AND STALL TIME
- p.10: results in Table II, where the video quality is measured as
- p.10: method to help prior ABR algorithms for fitting different
- p.13: TABLE III
- p.13: evaluation phase, we record the detailed playback behavior
- p.15: VI. ABLATION STUDIES
- p.15: results of training A2BR in 100-shot are shown in Figure 14.
- p.16: TABLE IV
- p.16: A2BR WITH DIFFERENT ROLLOUT M
- p.16: VII. RELATED WORK
- p.17: method adapt to the QoE diversity. Zuo et al. [85] propose
- p.17: VIII. CONCLUSION AND FUTURE WORK
- p.17: ACKNOWLEDGMENT
- p.17: REFERENCES
- p.17: Methodology.
- p.19: TRANSACTIONS ON CIRCUITS AND SYSTEMS FOR VIDEO TECHNOLOGY,

## 4. Índice de páginas con palabras clave
- p.1: state, QoE, stall, bandwidth, download, trace, PPO, imitation, inference, quality, network condition
- p.2: state, QoE, stall, buffer, bandwidth, download, dataset, trace, training, Pensieve, imitation, quality, network condition
- p.3: state, action, reward, QoE, rebuffer, buffer, throughput, bandwidth, download, chunk, quality, VMAF, visual, network condition
- p.4: state, action, reward, QoE, stall, buffer, throughput, download, chunk, training, MPC, BOLA, quality, network condition
- p.5: state, reward, QoE, stall, download, trace, training, generalization, fallback, network condition
- p.6: state, action, reward, buffer, throughput, download, chunk, PPO, inference, quality
- p.7: state, reward, throughput, download, training, baseline, PPO, fallback, network condition
- p.8: state, action, reward, QoE, rebuffer, stall, buffer, throughput, bandwidth, download, chunk, training, PPO, generalization, safety, fallback, network condition
- p.9: state, QoE, rebuffer, stall, buffer, throughput, download, chunk, dataset, trace, training, baseline, MPC, BOLA, Pensieve, A3C, quality, VMAF, network condition
- p.10: state, QoE, rebuffer, stall, buffer, throughput, bandwidth, download, chunk, dataset, trace, training, baseline, MPC, BOLA, Pensieve, imitation, risk, quality, VMAF, regime, network condition
- p.11: state, action, QoE, stall, buffer, throughput, bandwidth, download, chunk, dataset, training, baseline, MPC, BOLA, Pensieve, generalization, network condition
- p.12: state, reward, QoE, stall, buffer, throughput, bandwidth, download, dataset, trace, baseline, MPC, BOLA, Pensieve, network condition
- p.13: QoE, rebuffer, stall, buffer, download, chunk, trace, baseline, Pensieve, quality, visual, network condition
- p.14: state, reward, QoE, throughput, download, chunk, dataset, trace, training, baseline, MPC, Pensieve, sensitivity, network condition
- p.15: action, QoE, throughput, bandwidth, download, chunk, dataset, trace, training, baseline, MPC, Pensieve, generalization, risk, SSIM, network condition
- p.16: state, reward, QoE, rebuffer, buffer, throughput, bandwidth, download, chunk, training, MPC, BBA, BOLA, Pensieve, PPO, A3C, imitation, latency, inference, quality, network condition
- p.17: QoE, buffer, throughput, bandwidth, download, chunk, trace, training, BOLA, Pensieve, PPO, imitation, latency, quality, VMAF, visual, network condition
- p.18: action, QoE, bandwidth, download, dataset, trace, training, MPC, BBA, BOLA, Pensieve, PPO, latency, inference
- p.19: action, QoE, throughput, bandwidth, download, chunk, PPO, latency, quality, network condition

## 5. Extracción técnica cruda por categorías

### 5.x Modelo / arquitectura / algoritmo

**[Modelo / arquitectura / algoritmo | extracto 1 | p.1]**

IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 2485 Learning Tailored Adaptive Bitrate Algorithms to Heterogeneous Network Conditions: A Domain-Specific Priors and Meta-Reinforcement Learning Approach Tianchi Huang , Student Member, IEEE, Chao Zhou, Rui-Xiao Zhang , Student Member, IEEE, Chenglei Wu, and Lifeng Sun , Member, IEEE Abstract—Internet adaptive video streaming is a typical form of video delivery that leverages adaptive bitrate (ABR) algorithms to provide video services with high quality of experience (QoE) for various users in diverse and unique network conditions. Such heterogeneous network environments, which can be viewed as exogenous input processes, often lead to the unstable perfor- mance of ABR algorithms. Unfortunately, learning-based ABR algorithm which generated by state-of-the-art reinforcement learning (RL) technologies achieves good average performance but fails to perform well in all kinds of network condit

**[Modelo / arquitectura / algoritmo | extracto 2 | p.1]**

al form of video delivery that leverages adaptive bitrate (ABR) algorithms to provide video services with high quality of experience (QoE) for various users in diverse and unique network conditions. Such heterogeneous network environments, which can be viewed as exogenous input processes, often lead to the unstable perfor- mance of ABR algorithms. Unfortunately, learning-based ABR algorithm which generated by state-of-the-art reinforcement learning (RL) technologies achieves good average performance but fails to perform well in all kinds of network conditions. In this work, considering the video playback process as the Input-driven Markov Decision Process (IMDP), we propose A2BR (Adaptation of ABR), a novel meta-RL ABR approach. A2BR is mainly composed of an online stage and an offline stage. It leverages meta-RL to learn an initial meta-policy with various network conditions at the offline stage and makes decisions in personalized network conditions at the online stage. At the same time, we continually optimize the meta-policy to the tailor- made ABR policy for varying the current network environment within few shots. Moreover, in order to improve the learning Manuscript received 15 December 2021; revised 15 March 2022; accepted 23 April 2022. Date of publication 15 June 2022; date of current version 18 July 2022. This work was supported in part by the National Key Research and Development Program of China under Grant 2018YFB1003703, in part by NSFC under Grant 61936011, in part by the Beijing Key Laboratory of Networked Multimedia, and in part by the Kuaishou-Tsinghua Joint Project under Grant 20192000456. (Corresponding authors: Lifeng Sun; Chao Zhou.) Tianchi Huang is with

**[Modelo / arquitectura / algoritmo | extracto 3 | p.1]**

rate Algorithms to Heterogeneous Network Conditions: A Domain-Specific Priors and Meta-Reinforcement Learning Approach Tianchi Huang , Student Member, IEEE, Chao Zhou, Rui-Xiao Zhang , Student Member, IEEE, Chenglei Wu, and Lifeng Sun , Member, IEEE Abstract—Internet adaptive video streaming is a typical form of video delivery that leverages adaptive bitrate (ABR) algorithms to provide video services with high quality of experience (QoE) for various users in diverse and unique network conditions. Such heterogeneous network environments, which can be viewed as exogenous input processes, often lead to the unstable perfor- mance of ABR algorithms. Unfortunately, learning-based ABR algorithm which generated by state-of-the-art reinforcement learning (RL) technologies achieves good average performance but fails to perform well in all kinds of network conditions. In this work, considering the video playback process as the Input-driven Markov Decision Process (IMDP), we propose A2BR (Adaptation of ABR), a novel meta-RL ABR approach. A2BR is mainly composed of an online stage and an offline stage. It leverages meta-RL to learn an initial meta-policy with various network conditions at the offline stage and makes decisions in personalized network conditions at the online stage. At the same time, we continually optimize the meta-policy to the tailor- made ABR policy for varying the current network environment within few shots. Moreover, in order to improve the learning Manuscript received 15 December 2021; revised 15 March 2022; accepted 23 April 2022. Date of publication 15 June 2022; date of current version 18 July 2022. This work was supported in part by the National Key Research and De

**[Modelo / arquitectura / algoritmo | extracto 4 | p.1]**

e predominant Internet appli- cation, which is up almost 75% all traffic [1], [2]. Espe- cially, adaptive video streaming, such as HLS (HTTP Live Streaming) [3] and DASH [4] has already been the popular form of video delivery [5]. Adaptive bitrate (ABR) algorithms enable Internet adaptive video streaming services to achieve high video quality while avoiding uninterrupted stall event [5] (§II-A). Revisiting the recent success of ABR algorithms, heuristics often make decisions based on network or player sta- tus [6]–[8]. However, those schemes require a proper setting of configuration parameters [9], [10] for fitting different network distributions. By contrast, learning-based schemes employ several learning technologies, such as reinforcement learning [11], [12], supervised learning [2], [13] and imitation learn- ing [14], [15] to train a neural network (NN) w.r.t the given network traffic distributions, and make a zero-shot inference for unseen networks. In short, existing ABR algorithms, either heuristics or learning-based schemes, seldom configure or tune their parameters automatically and rapidly for varying the current network traffic distribution. However, in the adaptive video streaming scenario, the system dynamics are uncertain and the future state cannot be accurately predicted. To prove this view, we focus on inves- tigating the impact of ABR algorithms on the distribution of heterogeneous network traffics, where the distribution is usu- ally summarized by bandwidth traces experienced by different 0733-8716 © 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more

**[Modelo / arquitectura / algoritmo | extracto 5 | p.1]**

Key Laboratory of Pervasive Computing, Ministry of Education, Tsinghua University, Beijing 100084, China (e-mail: sunlf@tsinghua.edu.cn). Color versions of one or more figures in this article are available at https://doi.org/10.1109/JSAC.2022.3180804. Digital Object Identifier 10.1109/JSAC.2022.3180804 efficiency, we fully utilize domain knowledge for implementing a virtual player to replay the previously experienced network. Using trace-driven experiments on various scenarios including different vehicles, users, network types, and heterogeneous user- preferences, we show that A2BR outperforming recent ABR approaches with rapidly adapting to the personalized QoE metrics and specific network conditions. Testbed experimental results also illustrate the superiority of A2BR in adapting to the unseen environments. Index Terms—Streaming media, reinforcement learning (RL), adaptive control. I. INTRODUCTION D UE to the rapid development of network services, video streaming now stands for the predominant Internet appli- cation, which is up almost 75% all traffic [1], [2]. Espe- cially, adaptive video streaming, such as HLS (HTTP Live Streaming) [3] and DASH [4] has already been the popular form of video delivery [5]. Adaptive bitrate (ABR) algorithms enable Internet adaptive video streaming services to achieve high video quality while avoiding uninterrupted stall event [5] (§II-A). Revisiting the recent success of ABR algorithms, heuristics often make decisions based on network or player sta- tus [6]–[8]. However, those schemes require a proper setting of configuration parameters [9], [10] for fitting different network distributions. By contrast, learning-based schemes employ several learning

**[Modelo / arquitectura / algoritmo | extracto 6 | p.1]**

AL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 2485 Learning Tailored Adaptive Bitrate Algorithms to Heterogeneous Network Conditions: A Domain-Specific Priors and Meta-Reinforcement Learning Approach Tianchi Huang , Student Member, IEEE, Chao Zhou, Rui-Xiao Zhang , Student Member, IEEE, Chenglei Wu, and Lifeng Sun , Member, IEEE Abstract—Internet adaptive video streaming is a typical form of video delivery that leverages adaptive bitrate (ABR) algorithms to provide video services with high quality of experience (QoE) for various users in diverse and unique network conditions. Such heterogeneous network environments, which can be viewed as exogenous input processes, often lead to the unstable perfor- mance of ABR algorithms. Unfortunately, learning-based ABR algorithm which generated by state-of-the-art reinforcement learning (RL) technologies achieves good average performance but fails to perform well in all kinds of network conditions. In this work, considering the video playback process as the Input-driven Markov Decision Process (IMDP), we propose A2BR (Adaptation of ABR), a novel meta-RL ABR approach. A2BR is mainly composed of an online stage and an offline stage. It leverages meta-RL to learn an initial meta-policy with various network conditions at the offline stage and makes decisions in personalized network conditions at the online stage. At the same time, we continually optimize the meta-policy to the tailor- made ABR policy for varying the current network environment within few shots. Moreover, in order to improve the learning Manuscript received 15 December 2021; revised 15 March 2022; accepted 23 April 2022. Date of publication 15 June 2022; dat

**[Modelo / arquitectura / algoritmo | extracto 7 | p.1]**

i-Xiao Zhang , Student Member, IEEE, Chenglei Wu, and Lifeng Sun , Member, IEEE Abstract—Internet adaptive video streaming is a typical form of video delivery that leverages adaptive bitrate (ABR) algorithms to provide video services with high quality of experience (QoE) for various users in diverse and unique network conditions. Such heterogeneous network environments, which can be viewed as exogenous input processes, often lead to the unstable perfor- mance of ABR algorithms. Unfortunately, learning-based ABR algorithm which generated by state-of-the-art reinforcement learning (RL) technologies achieves good average performance but fails to perform well in all kinds of network conditions. In this work, considering the video playback process as the Input-driven Markov Decision Process (IMDP), we propose A2BR (Adaptation of ABR), a novel meta-RL ABR approach. A2BR is mainly composed of an online stage and an offline stage. It leverages meta-RL to learn an initial meta-policy with various network conditions at the offline stage and makes decisions in personalized network conditions at the online stage. At the same time, we continually optimize the meta-policy to the tailor- made ABR policy for varying the current network environment within few shots. Moreover, in order to improve the learning Manuscript received 15 December 2021; revised 15 March 2022; accepted 23 April 2022. Date of publication 15 June 2022; date of current version 18 July 2022. This work was supported in part by the National Key Research and Development Program of China under Grant 2018YFB1003703, in part by NSFC under Grant 61936011, in part by the Beijing Key Laboratory of Networked Multimedia, and in part

**[Modelo / arquitectura / algoritmo | extracto 8 | p.2]**

2486 IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 users at any time, in any place, and especially, under any network conditions. Through the analysis of the impact on the network distributions of different users, vehicles, and network types, we empirically find that nowadays’ Internet network conditions are not only diverse but also unique (§II-B). For example, the heterogeneity of network conditions for each user is inevitable, since both subjective and objective user behavior have an important impact on the network traffic distribution. Nevertheless, existing ABR algorithms, either heuristics or learning-based, fail to adapt to such heterogeneous bandwidth conditions that are significantly different from the offline training (or tuning) network dataset [16]. Motivated by these facts, we model the ABR playback process as Input-driven Markov Decision Process (IMDP), which can express an implicit heterogeneous network envi- ronment in an explicit manner (§III-A). We theoretically illustrate that vanilla RL technologies can only generalize a strategy that can perform well on average rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on th

**[Modelo / arquitectura / algoritmo | extracto 9 | p.2]**

ctive and objective user behavior have an important impact on the network traffic distribution. Nevertheless, existing ABR algorithms, either heuristics or learning-based, fail to adapt to such heterogeneous bandwidth conditions that are significantly different from the offline training (or tuning) network dataset [16]. Motivated by these facts, we model the ABR playback process as Input-driven Markov Decision Process (IMDP), which can express an implicit heterogeneous network envi- ronment in an explicit manner (§III-A). We theoretically illustrate that vanilla RL technologies can only generalize a strategy that can perform well on average rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel neural meta-RL ABR system that enables fast adaptation to the specific network conditions (§III-B). A2BR is composed of the offline stage and online stage (§IV). At the offline stage, A2BR trains a meta-model with various real and synthetic network conditions for learning parameter initialization meta-policy, where the policy can provide rapid adaptation for varying heterogeneous networks. To achieve this goal, we implement the training process based on the state-of-the-art gradient-free meta-learning technology [18] and utilize maximum entropy RL methodologies to achieve better exploration (§IV-B). Moreover, at the online stage, t

**[Modelo / arquitectura / algoritmo | extracto 10 | p.2]**

is the first meta-learning with domain knowledge approach for adaptive streaming. • Results on different types of network conditions illustrate that the generated tailor-made ABR policies can well adapt to heterogeneous networks with relatively few-shot. II. BACKGROUND AND MOTIVATION Our research is started with a fundamental quest: How will the recent ABRs perform in various network traffic environ- ments?. To answer this question, first, we briefly introduce the key principle of adaptive video streaming and adaptive bitrate (ABR) algorithms. We then use empirical measure- ments to elucidate the key limitations of prior solutions. A. Adaptive Video Streaming The adaptive bitrate method (ABR) is an algorithm that dynamically selects video bitrates via network conditions and the client’s buffer occupancy. The traditional video stream- ing architecture is shown in Figure 1. The system consists of a video player client with a constrained buffer length and an HTTP-Server or Content Delivery Network (CDN). Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.

**[Modelo / arquitectura / algoritmo | extracto 11 | p.2]**

c distribution. Nevertheless, existing ABR algorithms, either heuristics or learning-based, fail to adapt to such heterogeneous bandwidth conditions that are significantly different from the offline training (or tuning) network dataset [16]. Motivated by these facts, we model the ABR playback process as Input-driven Markov Decision Process (IMDP), which can express an implicit heterogeneous network envi- ronment in an explicit manner (§III-A). We theoretically illustrate that vanilla RL technologies can only generalize a strategy that can perform well on average rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel neural meta-RL ABR system that enables fast adaptation to the specific network conditions (§III-B). A2BR is composed of the offline stage and online stage (§IV). At the offline stage, A2BR trains a meta-model with various real and synthetic network conditions for learning parameter initialization meta-policy, where the policy can provide rapid adaptation for varying heterogeneous networks. To achieve this goal, we implement the training process based on the state-of-the-art gradient-free meta-learning technology [18] and utilize maximum entropy RL methodologies to achieve better exploration (§IV-B). Moreover, at the online stage, the video player, placed on the user side, receives the trained meta-model and pic

**[Modelo / arquitectura / algoritmo | extracto 12 | p.2]**

ny place, and especially, under any network conditions. Through the analysis of the impact on the network distributions of different users, vehicles, and network types, we empirically find that nowadays’ Internet network conditions are not only diverse but also unique (§II-B). For example, the heterogeneity of network conditions for each user is inevitable, since both subjective and objective user behavior have an important impact on the network traffic distribution. Nevertheless, existing ABR algorithms, either heuristics or learning-based, fail to adapt to such heterogeneous bandwidth conditions that are significantly different from the offline training (or tuning) network dataset [16]. Motivated by these facts, we model the ABR playback process as Input-driven Markov Decision Process (IMDP), which can express an implicit heterogeneous network envi- ronment in an explicit manner (§III-A). We theoretically illustrate that vanilla RL technologies can only generalize a strategy that can perform well on average rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel neural meta-RL ABR system that enables fast adaptation to the specific network conditions (§III-B). A2BR is composed of the offline stage and online stage (§IV). At the offline stage, A2BR trains a meta-model with various real and synthetic network conditions for l

**[Modelo / arquitectura / algoritmo | extracto 13 | p.2]**

h conditions that are significantly different from the offline training (or tuning) network dataset [16]. Motivated by these facts, we model the ABR playback process as Input-driven Markov Decision Process (IMDP), which can express an implicit heterogeneous network envi- ronment in an explicit manner (§III-A). We theoretically illustrate that vanilla RL technologies can only generalize a strategy that can perform well on average rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel neural meta-RL ABR system that enables fast adaptation to the specific network conditions (§III-B). A2BR is composed of the offline stage and online stage (§IV). At the offline stage, A2BR trains a meta-model with various real and synthetic network conditions for learning parameter initialization meta-policy, where the policy can provide rapid adaptation for varying heterogeneous networks. To achieve this goal, we implement the training process based on the state-of-the-art gradient-free meta-learning technology [18] and utilize maximum entropy RL methodologies to achieve better exploration (§IV-B). Moreover, at the online stage, the video player, placed on the user side, receives the trained meta-model and picks the bitrates w.r.t the meta-policy and the current specific network status. Upon finishing the video session, the meta-policy is cont

**[Modelo / arquitectura / algoritmo | extracto 14 | p.2]**

k envi- ronment in an explicit manner (§III-A). We theoretically illustrate that vanilla RL technologies can only generalize a strategy that can perform well on average rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel neural meta-RL ABR system that enables fast adaptation to the specific network conditions (§III-B). A2BR is composed of the offline stage and online stage (§IV). At the offline stage, A2BR trains a meta-model with various real and synthetic network conditions for learning parameter initialization meta-policy, where the policy can provide rapid adaptation for varying heterogeneous networks. To achieve this goal, we implement the training process based on the state-of-the-art gradient-free meta-learning technology [18] and utilize maximum entropy RL methodologies to achieve better exploration (§IV-B). Moreover, at the online stage, the video player, placed on the user side, receives the trained meta-model and picks the bitrates w.r.t the meta-policy and the current specific network status. Upon finishing the video session, the meta-policy is continually updated to the tailor-made policy with the collected trajectories. For improving the learning efficiency, the trajec- tories are collected not only from the real world but also from the “virtual world.” Specifically, the virtual world is motivated by domain

**[Modelo / arquitectura / algoritmo | extracto 15 | p.2]**

tions that are significantly different from the offline training (or tuning) network dataset [16]. Motivated by these facts, we model the ABR playback process as Input-driven Markov Decision Process (IMDP), which can express an implicit heterogeneous network envi- ronment in an explicit manner (§III-A). We theoretically illustrate that vanilla RL technologies can only generalize a strategy that can perform well on average rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel neural meta-RL ABR system that enables fast adaptation to the specific network conditions (§III-B). A2BR is composed of the offline stage and online stage (§IV). At the offline stage, A2BR trains a meta-model with various real and synthetic network conditions for learning parameter initialization meta-policy, where the policy can provide rapid adaptation for varying heterogeneous networks. To achieve this goal, we implement the training process based on the state-of-the-art gradient-free meta-learning technology [18] and utilize maximum entropy RL methodologies to achieve better exploration (§IV-B). Moreover, at the online stage, the video player, placed on the user side, receives the trained meta-model and picks the bitrates w.r.t the meta-policy and the current specific network status. Upon finishing the video session, the meta-policy is continual

**[Modelo / arquitectura / algoritmo | extracto 16 | p.3]**

HUANG et al.: LEARNING TAILORED ABR ALGORITHMS TO HETEROGENEOUS NETWORK CONDITIONS 2487 Fig. 2. Visualizing personalized networks from the real-world [2], [20], [21]. The video player client decodes and renders video frames from the playback buffer. Once the streaming service starts, the client fetches the video chunk from the HTTP Server or CDN orderly by an ABR algorithm. The ABR algorithm, implemented on the client-side, determines the next chunk and next chunk video quality via throughput estimation and current buffer utilization. After finishing the session, several metrics, such as total bitrate, total re-buffering time, and total bitrate change will be summarized as a QoE metric to evaluate the performance. Thus, how to achieve high QoE scores for adaptive video streaming has become a major challenge for ABR algorithms. Existing ABR algorithms are generally composed of heuris

### 5.x Estado / inputs / features

**[Estado / inputs / features | extracto 1 | p.1]**

IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 2485 Learning Tailored Adaptive Bitrate Algorithms to Heterogeneous Network Conditions: A Domain-Specific Priors and Meta-Reinforcement Learning Approach Tianchi Huang , Student Member, IEEE, Chao Zhou, Rui-Xiao Zhang , Student Member, IEEE, Chenglei Wu, and Lifeng Sun , Member, IEEE Abstract—Internet adaptive video streaming is a typical form of video delivery that leverages adaptive bitrate (ABR) algorithms to provide video services with high quality of experience (QoE) for various users in diverse and unique network conditions. Such heterogeneous network environments, which can be viewed as exogenous input processes, often lead to the unstable perfor- mance of ABR algorithms. Unfortunately, learning-based ABR algorithm which generated by state-of-the-art reinforcement learning (RL) technologies achieves good average performance but fails to perform well in all kinds of network conditions. In this work, considering the video playback process as the Input-driven Markov Decision Process (IMDP), we propose A2BR (Adaptation of ABR), a novel meta-RL ABR approach. A2BR is mainly composed of an online stage and an offline stage. It leverages meta-RL to learn an initial meta-policy with various network conditions at the offline stage and makes decisions in personalized network conditions at the online stage. At the same time, we continually optimize the meta-policy to the tailor- made ABR policy for varying the current network environment within few shots. Moreover, in order to improve the learning Manuscript received 15 December 2021; revised 15 March 2022; accepted 23 April 2022. Dat

**[Estado / inputs / features | extracto 2 | p.1]**

d Meta-Reinforcement Learning Approach Tianchi Huang , Student Member, IEEE, Chao Zhou, Rui-Xiao Zhang , Student Member, IEEE, Chenglei Wu, and Lifeng Sun , Member, IEEE Abstract—Internet adaptive video streaming is a typical form of video delivery that leverages adaptive bitrate (ABR) algorithms to provide video services with high quality of experience (QoE) for various users in diverse and unique network conditions. Such heterogeneous network environments, which can be viewed as exogenous input processes, often lead to the unstable perfor- mance of ABR algorithms. Unfortunately, learning-based ABR algorithm which generated by state-of-the-art reinforcement learning (RL) technologies achieves good average performance but fails to perform well in all kinds of network conditions. In this work, considering the video playback process as the Input-driven Markov Decision Process (IMDP), we propose A2BR (Adaptation of ABR), a novel meta-RL ABR approach. A2BR is mainly composed of an online stage and an offline stage. It leverages meta-RL to learn an initial meta-policy with various network conditions at the offline stage and makes decisions in personalized network conditions at the online stage. At the same time, we continually optimize the meta-policy to the tailor- made ABR policy for varying the current network environment within few shots. Moreover, in order to improve the learning Manuscript received 15 December 2021; revised 15 March 2022; accepted 23 April 2022. Date of publication 15 June 2022; date of current version 18 July 2022. This work was supported in part by the National Key Research and Development Program of China under Grant 2018YFB1003703, in part by NSFC under G

**[Estado / inputs / features | extracto 3 | p.1]**

distributions. By contrast, learning-based schemes employ several learning technologies, such as reinforcement learning [11], [12], supervised learning [2], [13] and imitation learn- ing [14], [15] to train a neural network (NN) w.r.t the given network traffic distributions, and make a zero-shot inference for unseen networks. In short, existing ABR algorithms, either heuristics or learning-based schemes, seldom configure or tune their parameters automatically and rapidly for varying the current network traffic distribution. However, in the adaptive video streaming scenario, the system dynamics are uncertain and the future state cannot be accurately predicted. To prove this view, we focus on inves- tigating the impact of ABR algorithms on the distribution of heterogeneous network traffics, where the distribution is usu- ally summarized by bandwidth traces experienced by different 0733-8716 © 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.

**[Estado / inputs / features | extracto 4 | p.1]**

ro-shot inference for unseen networks. In short, existing ABR algorithms, either heuristics or learning-based schemes, seldom configure or tune their parameters automatically and rapidly for varying the current network traffic distribution. However, in the adaptive video streaming scenario, the system dynamics are uncertain and the future state cannot be accurately predicted. To prove this view, we focus on inves- tigating the impact of ABR algorithms on the distribution of heterogeneous network traffics, where the distribution is usu- ally summarized by bandwidth traces experienced by different 0733-8716 © 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.

**[Estado / inputs / features | extracto 5 | p.1]**

recent success of ABR algorithms, heuristics often make decisions based on network or player sta- tus [6]–[8]. However, those schemes require a proper setting of configuration parameters [9], [10] for fitting different network distributions. By contrast, learning-based schemes employ several learning technologies, such as reinforcement learning [11], [12], supervised learning [2], [13] and imitation learn- ing [14], [15] to train a neural network (NN) w.r.t the given network traffic distributions, and make a zero-shot inference for unseen networks. In short, existing ABR algorithms, either heuristics or learning-based schemes, seldom configure or tune their parameters automatically and rapidly for varying the current network traffic distribution. However, in the adaptive video streaming scenario, the system dynamics are uncertain and the future state cannot be accurately predicted. To prove this view, we focus on inves- tigating the impact of ABR algorithms on the distribution of heterogeneous network traffics, where the distribution is usu- ally summarized by bandwidth traces experienced by different 0733-8716 © 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.

**[Estado / inputs / features | extracto 6 | p.1]**

rate Algorithms to Heterogeneous Network Conditions: A Domain-Specific Priors and Meta-Reinforcement Learning Approach Tianchi Huang , Student Member, IEEE, Chao Zhou, Rui-Xiao Zhang , Student Member, IEEE, Chenglei Wu, and Lifeng Sun , Member, IEEE Abstract—Internet adaptive video streaming is a typical form of video delivery that leverages adaptive bitrate (ABR) algorithms to provide video services with high quality of experience (QoE) for various users in diverse and unique network conditions. Such heterogeneous network environments, which can be viewed as exogenous input processes, often lead to the unstable perfor- mance of ABR algorithms. Unfortunately, learning-based ABR algorithm which generated by state-of-the-art reinforcement learning (RL) technologies achieves good average performance but fails to perform well in all kinds of network conditions. In this work, considering the video playback process as the Input-driven Markov Decision Process (IMDP), we propose A2BR (Adaptation of ABR), a novel meta-RL ABR approach. A2BR is mainly composed of an online stage and an offline stage. It leverages meta-RL to learn an initial meta-policy with various network conditions at the offline stage and makes decisions in personalized network conditions at the online stage. At the same time, we continually optimize the meta-policy to the tailor- made ABR policy for varying the current network environment within few shots. Moreover, in order to improve the learning Manuscript received 15 December 2021; revised 15 March 2022; accepted 23 April 2022. Date of publication 15 June 2022; date of current version 18 July 2022. This work was supported in part by the National Key Research and Development

**[Estado / inputs / features | extracto 7 | p.2]**

dition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel neural meta-RL ABR system that enables fast adaptation to the specific network conditions (§III-B). A2BR is composed of the offline stage and online stage (§IV). At the offline stage, A2BR trains a meta-model with various real and synthetic network conditions for learning parameter initialization meta-policy, where the policy can provide rapid adaptation for varying heterogeneous networks. To achieve this goal, we implement the training process based on the state-of-the-art gradient-free meta-learning technology [18] and utilize maximum entropy RL methodologies to achieve better exploration (§IV-B). Moreover, at the online stage, the video player, placed on the user side, receives the trained meta-model and picks the bitrates w.r.t the meta-policy and the current specific network status. Upon finishing the video session, the meta-policy is continually updated to the tailor-made policy with the collected trajectories. For improving the learning efficiency, the trajec- tories are collected not only from the real world but also from the “virtual world.” Specifically, the virtual world is motivated by domain principles and constructed by a faithful virtual player and experienced network environments. In addition, we also employ the domain knowledge that uses heuristics to enable safe online RL. Subse

**[Estado / inputs / features | extracto 8 | p.2]**

ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 users at any time, in any place, and especially, under any network conditions. Through the analysis of the impact on the network distributions of different users, vehicles, and network types, we empirically find that nowadays’ Internet network conditions are not only diverse but also unique (§II-B). For example, the heterogeneity of network conditions for each user is inevitable, since both subjective and objective user behavior have an important impact on the network traffic distribution. Nevertheless, existing ABR algorithms, either heuristics or learning-based, fail to adapt to such heterogeneous bandwidth conditions that are significantly different from the offline training (or tuning) network dataset [16]. Motivated by these facts, we model the ABR playback process as Input-driven Markov Decision Process (IMDP), which can express an implicit heterogeneous network envi- ronment in an explicit manner (§III-A). We theoretically illustrate that vanilla RL technologies can only generalize a strategy that can perform well on average rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel neural meta-RL ABR system that enables fast adaptation to the specific network conditions (§III-B). A2BR is composed of the offline stage and online stage (§IV). At the offli

**[Estado / inputs / features | extracto 9 | p.2]**

ific network conditions. • We implement A2BR, which is the first meta-learning with domain knowledge approach for adaptive streaming. • Results on different types of network conditions illustrate that the generated tailor-made ABR policies can well adapt to heterogeneous networks with relatively few-shot. II. BACKGROUND AND MOTIVATION Our research is started with a fundamental quest: How will the recent ABRs perform in various network traffic environ- ments?. To answer this question, first, we briefly introduce the key principle of adaptive video streaming and adaptive bitrate (ABR) algorithms. We then use empirical measure- ments to elucidate the key limitations of prior solutions. A. Adaptive Video Streaming The adaptive bitrate method (ABR) is an algorithm that dynamically selects video bitrates via network conditions and the client’s buffer occupancy. The traditional video stream- ing architecture is shown in Figure 1. The system consists of a video player client with a constrained buffer length and an HTTP-Server or Content Delivery Network (CDN). Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.

**[Estado / inputs / features | extracto 10 | p.2]**

2486 IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 users at any time, in any place, and especially, under any network conditions. Through the analysis of the impact on the network distributions of different users, vehicles, and network types, we empirically find that nowadays’ Internet network conditions are not only diverse but also unique (§II-B). For example, the heterogeneity of network conditions for each user is inevitable, since both subjective and objective user behavior have an important impact on the network traffic distribution. Nevertheless, existing ABR algorithms, either heuristics or learning-based, fail to adapt to such heterogeneous bandwidth conditions that are significantly different from the offline training (or tuning) network dataset [16]. Motivated by these facts, we model the ABR playback process as Input-driven Markov Decision Process (IMDP), which can express an implicit heterogeneous network envi- ronment in an explicit manner (§III-A). We theoretically illustrate that vanilla RL technologies can only generalize a strategy that can perform well on average rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel n

**[Estado / inputs / features | extracto 11 | p.2]**

s with relatively few-shot. II. BACKGROUND AND MOTIVATION Our research is started with a fundamental quest: How will the recent ABRs perform in various network traffic environ- ments?. To answer this question, first, we briefly introduce the key principle of adaptive video streaming and adaptive bitrate (ABR) algorithms. We then use empirical measure- ments to elucidate the key limitations of prior solutions. A. Adaptive Video Streaming The adaptive bitrate method (ABR) is an algorithm that dynamically selects video bitrates via network conditions and the client’s buffer occupancy. The traditional video stream- ing architecture is shown in Figure 1. The system consists of a video player client with a constrained buffer length and an HTTP-Server or Content Delivery Network (CDN). Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.

**[Estado / inputs / features | extracto 12 | p.2]**

nowadays’ Internet network conditions are not only diverse but also unique (§II-B). For example, the heterogeneity of network conditions for each user is inevitable, since both subjective and objective user behavior have an important impact on the network traffic distribution. Nevertheless, existing ABR algorithms, either heuristics or learning-based, fail to adapt to such heterogeneous bandwidth conditions that are significantly different from the offline training (or tuning) network dataset [16]. Motivated by these facts, we model the ABR playback process as Input-driven Markov Decision Process (IMDP), which can express an implicit heterogeneous network envi- ronment in an explicit manner (§III-A). We theoretically illustrate that vanilla RL technologies can only generalize a strategy that can perform well on average rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel neural meta-RL ABR system that enables fast adaptation to the specific network conditions (§III-B). A2BR is composed of the offline stage and online stage (§IV). At the offline stage, A2BR trains a meta-model with various real and synthetic network conditions for learning parameter initialization meta-policy, where the policy can provide rapid adaptation for varying heterogeneous networks. To achieve this goal, we implement the training process based on the state-

**[Estado / inputs / features | extracto 13 | p.3]**

red [13], buffer occupancy [7] or predefined models [8]. By con- trast, learning-based ABRs model the process as the Markov decision process (MDP): at each step t, the video client, often namely agent in RL framework, take a proper action at (i.e., select a proper bitrate) w.r.t current system status st. The agent then downloads the chunk and computes a reward rt for measuring the current quality-of-experience (QoE) of the past action. The process will terminate if the agent finishes playing the video session. In the end, we aim to generalize a policy π to maximize the QoE of the entire session. The accumulated QoE objective function is defined as Eq. 1 ([8], [11]), where Rn represents the each chunk’s video bitrate, Tn reflects the rebuffering time for each chunk n, q(Rn) means the quality metric such as video bitrate [8] and VMAF [22] (state-of-the-art quality assessment), μ and ρ are the weight of rebuffering and smoothness penalty, respectively. QoE = N  n=1 q(Rn) −μ N  n=1 Tn −ρ N−1  n=1 |q(Rn+1) −q(Rn)| (1) B. Different Types of Network Conditions Recently, several learning-based schemes have been made to train an NN policy from the clean slate via various RL methods [11], [23]. Unfortunately, such one-fits-all schemes, including heuristics and learning-based can hardly always perform well in today’s network traffics due to the diversity of real-world network conditions [2]. We show the personalized network environments from two perspectives. TABLE I COMPARISON RESULTS ON DIFFERENT ABRS OVER 3G-CAR AND 3G-BUS NETWORKS, WHERE A2BR IS FINE-TUNED IN 20-SHOT 1) Sorted by Users: First, we measure a portion of data from the Puffer project [2] and demonstrate the users’ pers

**[Estado / inputs / features | extracto 14 | p.3]**

VER 3G-CAR AND 3G-BUS NETWORKS, WHERE A2BR IS FINE-TUNED IN 20-SHOT 1) Sorted by Users: First, we measure a portion of data from the Puffer project [2] and demonstrate the users’ personalized network status on June 2, 2021, in Figure 2(a). The left figure illustrates the correlations between throughput and round- trip-time (RTT) of each user. As shown, in the real world, the average bandwidth is particularly varied, ranging from 0.1 to 100 Mbps. The lower bandwidth leads to larger RTT. The network environment of each user is different. Someone can watch the videos with high bandwidth and low RTT, while the others live in the low bandwidth and high RTT scenario. The right figure plots the fine-grained cumulative distribution function (CDF) of throughput and RTT of the users with top-8 viewing hours on that day. We can find the tailor-made features for personalized network conditions: some of the users have very constant throughput (e.g., user C and user F), while most of the users’ bandwidth is unstable and doesn’t cover all network conditions. 2) Sorted by Scenarios: Next, Figure 2(b) shows another personalized network condition that is categorized by network types, which covers 3G, 4G, and 5G networks. Testing results on the bus, car, and metro environments show that different vehicle speeds lead to very different 3G bandwidth distri- butions. For instance, we can see the throughput measured from the metro achieves the lowest average and fluctuation value among the candidates. While we observe the highest bandwidth with high fluctuation in the 3G-car scenario. Mean- while, in addition to the various network specifics on 4G and 5G, the network distributions are always influenced

**[Estado / inputs / features | extracto 15 | p.3]**

HUANG et al.: LEARNING TAILORED ABR ALGORITHMS TO HETEROGENEOUS NETWORK CONDITIONS 2487 Fig. 2. Visualizing personalized networks from the real-world [2], [20], [21]. The video player client decodes and renders video frames from the playback buffer. Once the streaming service starts, the client fetches the video chunk from the HTTP Server or CDN orderly by an ABR algorithm. The ABR algorithm, implemented on the client-side, determines the next chunk and next chunk video quality via throughput estimation and current buffer utilization. After finishing the session, several metrics, such as total bitrate, total re-buffering time, and total bitrate change will be summarized as a QoE metric to evaluate the performance. Thus, how to achieve high QoE scores for adaptive video streaming has become a major challenge for ABR algorithms. Existing ABR algorithms are generally composed of heuris- tics and learning-based. Heuristics make decisions from fea- tures with domain knowledge, e.g., throughput measured [13], buffer occupancy [7] or predefined models [8]. By con- trast, learning-based AB

**[Estado / inputs / features | extracto 16 | p.3]**

-world [2], [20], [21]. The video player client decodes and renders video frames from the playback buffer. Once the streaming service starts, the client fetches the video chunk from the HTTP Server or CDN orderly by an ABR algorithm. The ABR algorithm, implemented on the client-side, determines the next chunk and next chunk video quality via throughput estimation and current buffer utilization. After finishing the session, several metrics, such as total bitrate, total re-buffering time, and total bitrate change will be summarized as a QoE metric to evaluate the performance. Thus, how to achieve high QoE scores for adaptive video streaming has become a major challenge for ABR algorithms. Existing ABR algorithms are generally composed of heuris- tics and learning-based. Heuristics make decisions from fea- tures with domain knowledge, e.g., throughput measured [13], buffer occupancy [7] or predefined models [8]. By con- trast, learning-based ABRs model the process as the Markov decision process (MDP): at each step t, the video client, often namely agent in RL framework, take a proper action at (i.e., select a proper bitrate) w.r.t current system status st. The agent then downloads the chunk and computes a reward rt for measuring the current quality-of-experience (QoE) of the past action. The process will terminate if the agent finishes playing the video session. In the end, we aim to generalize a policy π to maximize the QoE of the entire session. The accumulated QoE objective function is defined as Eq. 1 ([8], [11]), where Rn represents the each chunk’s video bitrate, Tn reflects the rebuffering time for each chunk n, q(Rn) means the quality metric such as video bitrate [8] and VMAF

### 5.x Acción / decisión ABR

**[Acción / decisión ABR | extracto 1 | p.1]**

IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 2485 Learning Tailored Adaptive Bitrate Algorithms to Heterogeneous Network Conditions: A Domain-Specific Priors and Meta-Reinforcement Learning Approach Tianchi Huang , Student Member, IEEE, Chao Zhou, Rui-Xiao Zhang , Student Member, IEEE, Chenglei Wu, and Lifeng Sun , Member, IEEE Abstract—Internet adaptive video streaming is a typical form of video delivery that leverages adaptive bitrate (ABR) algorithms to provide video services with high quality of experience (QoE) for various users in diverse and unique network conditions. Such heterogeneous network environments, which can be viewed as exogenous input processes, often lead to the unstable perfor- mance of ABR algorithms. Unfortunately, learning-based ABR algorithm which generated by state-of-the-art reinforcement learning (RL) technologies achieves good average performance but fails to perform well in all kinds of netw

**[Acción / decisión ABR | extracto 2 | p.1]**

Learning Approach Tianchi Huang , Student Member, IEEE, Chao Zhou, Rui-Xiao Zhang , Student Member, IEEE, Chenglei Wu, and Lifeng Sun , Member, IEEE Abstract—Internet adaptive video streaming is a typical form of video delivery that leverages adaptive bitrate (ABR) algorithms to provide video services with high quality of experience (QoE) for various users in diverse and unique network conditions. Such heterogeneous network environments, which can be viewed as exogenous input processes, often lead to the unstable perfor- mance of ABR algorithms. Unfortunately, learning-based ABR algorithm which generated by state-of-the-art reinforcement learning (RL) technologies achieves good average performance but fails to perform well in all kinds of network conditions. In this work, considering the video playback process as the Input-driven Markov Decision Process (IMDP), we propose A2BR (Adaptation of ABR), a novel meta-RL ABR approach. A2BR is mainly composed of an online stage and an offline stage. It leverages meta-RL to learn an initial meta-policy with various network conditions at the offline stage and makes decisions in personalized network conditions at the online stage. At the same time, we continually optimize the meta-policy to the tailor- made ABR policy for varying the current network environment within few shots. Moreover, in order to improve the learning Manuscript received 15 December 2021; revised 15 March 2022; accepted 23 April 2022. Date of publication 15 June 2022; date of current version 18 July 2022. This work was supported in part by the National Key Research and Development Program of China under Grant 2018YFB1003703, in part by NSFC under Grant 61936011, in part

**[Acción / decisión ABR | extracto 3 | p.1]**

Member, IEEE, Chao Zhou, Rui-Xiao Zhang , Student Member, IEEE, Chenglei Wu, and Lifeng Sun , Member, IEEE Abstract—Internet adaptive video streaming is a typical form of video delivery that leverages adaptive bitrate (ABR) algorithms to provide video services with high quality of experience (QoE) for various users in diverse and unique network conditions. Such heterogeneous network environments, which can be viewed as exogenous input processes, often lead to the unstable perfor- mance of ABR algorithms. Unfortunately, learning-based ABR algorithm which generated by state-of-the-art reinforcement learning (RL) technologies achieves good average performance but fails to perform well in all kinds of network conditions. In this work, considering the video playback process as the Input-driven Markov Decision Process (IMDP), we propose A2BR (Adaptation of ABR), a novel meta-RL ABR approach. A2BR is mainly composed of an online stage and an offline stage. It leverages meta-RL to learn an initial meta-policy with various network conditions at the offline stage and makes decisions in personalized network conditions at the online stage. At the same time, we continually optimize the meta-policy to the tailor- made ABR policy for varying the current network environment within few shots. Moreover, in order to improve the learning Manuscript received 15 December 2021; revised 15 March 2022; accepted 23 April 2022. Date of publication 15 June 2022; date of current version 18 July 2022. This work was supported in part by the National Key Research and Development Program of China under Grant 2018YFB1003703, in part by NSFC under Grant 61936011, in part by the Beijing Key Laboratory of Networked M

**[Acción / decisión ABR | extracto 4 | p.2]**

such heterogeneous bandwidth conditions that are significantly different from the offline training (or tuning) network dataset [16]. Motivated by these facts, we model the ABR playback process as Input-driven Markov Decision Process (IMDP), which can express an implicit heterogeneous network envi- ronment in an explicit manner (§III-A). We theoretically illustrate that vanilla RL technologies can only generalize a strategy that can perform well on average rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel neural meta-RL ABR system that enables fast adaptation to the specific network conditions (§III-B). A2BR is composed of the offline stage and online stage (§IV). At the offline stage, A2BR trains a meta-model with various real and synthetic network conditions for learning parameter initialization meta-policy, where the policy can provide rapid adaptation for varying heterogeneous networks. To achieve this goal, we implement the training process based on the state-of-the-art gradient-free meta-learning technology [18] and utilize maximum entropy RL methodologies to achieve better exploration (§IV-B). Moreover, at the online stage, the video player, placed on the user side, receives the trained meta-model and picks the bitrates w.r.t the meta-policy and the current specific network status. Upon finishing the video sessi

**[Acción / decisión ABR | extracto 5 | p.2]**

N COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 users at any time, in any place, and especially, under any network conditions. Through the analysis of the impact on the network distributions of different users, vehicles, and network types, we empirically find that nowadays’ Internet network conditions are not only diverse but also unique (§II-B). For example, the heterogeneity of network conditions for each user is inevitable, since both subjective and objective user behavior have an important impact on the network traffic distribution. Nevertheless, existing ABR algorithms, either heuristics or learning-based, fail to adapt to such heterogeneous bandwidth conditions that are significantly different from the offline training (or tuning) network dataset [16]. Motivated by these facts, we model the ABR playback process as Input-driven Markov Decision Process (IMDP), which can express an implicit heterogeneous network envi- ronment in an explicit manner (§III-A). We theoretically illustrate that vanilla RL technologies can only generalize a strategy that can perform well on average rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel neural meta-RL ABR system that enables fast adaptation to the specific network conditions (§III-B). A2BR is composed of the offline stage and online stage (§IV). At the offline stage, A2BR trains a

**[Acción / decisión ABR | extracto 6 | p.2]**

2486 IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 users at any time, in any place, and especially, under any network conditions. Through the analysis of the impact on the network distributions of different users, vehicles, and network types, we empirically find that nowadays’ Internet network conditions are not only diverse but also unique (§II-B). For example, the heterogeneity of network conditions for each user is inevitable, since both subjective and objective user behavior have an important impact on the network traffic distribution. Nevertheless, existing ABR algorithms, either heuristics or learning-based, fail to adapt to such heterogeneous bandwidth conditions that are significantly different from the offline training (or tuning) network dataset [16]. Motivated by these facts, we model the ABR playback process as Input-driv

**[Acción / decisión ABR | extracto 7 | p.2]**

t from the offline training (or tuning) network dataset [16]. Motivated by these facts, we model the ABR playback process as Input-driven Markov Decision Process (IMDP), which can express an implicit heterogeneous network envi- ronment in an explicit manner (§III-A). We theoretically illustrate that vanilla RL technologies can only generalize a strategy that can perform well on average rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel neural meta-RL ABR system that enables fast adaptation to the specific network conditions (§III-B). A2BR is composed of the offline stage and online stage (§IV). At the offline stage, A2BR trains a meta-model with various real and synthetic network conditions for learning parameter initialization meta-policy, where the policy can provide rapid adaptation for varying heterogeneous networks. To achieve this goal, we implement the training process based on the state-of-the-art gradient-free meta-learning technology [18] and utilize maximum entropy RL methodologies to achieve better exploration (§IV-B). Moreover, at the online stage, the video player, placed on the user side, receives the trained meta-model and picks the bitrates w.r.t the meta-policy and the current specific network status. Upon finishing the video session, the meta-policy is continually updated to the tailor-made policy with t

**[Acción / decisión ABR | extracto 8 | p.3]**

thm, implemented on the client-side, determines the next chunk and next chunk video quality via throughput estimation and current buffer utilization. After finishing the session, several metrics, such as total bitrate, total re-buffering time, and total bitrate change will be summarized as a QoE metric to evaluate the performance. Thus, how to achieve high QoE scores for adaptive video streaming has become a major challenge for ABR algorithms. Existing ABR algorithms are generally composed of heuris- tics and learning-based. Heuristics make decisions from fea- tures with domain knowledge, e.g., throughput measured [13], buffer occupancy [7] or predefined models [8]. By con- trast, learning-based ABRs model the process as the Markov decision process (MDP): at each step t, the video client, often namely agent in RL framework, take a proper action at (i.e., select a proper bitrate) w.r.t current system status st. The agent then downloads the chunk and computes a reward rt for measuring the current quality-of-experience (QoE) of the past action. The process will terminate if the agent finishes playing the video session. In the end, we aim to generalize a policy π to maximize the QoE of the entire session. The accumulated QoE objective function is defined as Eq. 1 ([8], [11]), where Rn represents the each chunk’s video bitrate, Tn reflects the rebuffering time for each chunk n, q(Rn) means the quality metric such as video bitrate [8] and VMAF [22] (state-of-the-art quality assessment), μ and ρ are the weight of rebuffering and smoothness penalty, respectively. QoE = N  n=1 q(Rn) −μ N  n=1 Tn −ρ N−1  n=1 |q(Rn+1) −q(Rn)| (1) B. Different Types of Network Conditions Recently, sever

**[Acción / decisión ABR | extracto 9 | p.3]**

HUANG et al.: LEARNING TAILORED ABR ALGORITHMS TO HETEROGENEOUS NETWORK CONDITIONS 2487 Fig. 2. Visualizing personalized networks from the real-world [2], [20], [21]. The video player client decodes and renders video frames from the playback buffer. Once the streaming service starts, the client fetches the video chunk from the HTTP Server or CDN orderly by an ABR algorithm. The ABR algorithm, implemented on the client-side, determines the next chunk and next chunk video quality via throughput estimation and current buffer utilization. After finishing the session, several metrics, such as total bitrate, total re-buffering time, and total bitrate change will be summarized as a QoE metric to evaluate the performance. Thus, how to achieve high QoE scores for adaptive video streaming has become a major challenge for ABR algorithms. Existing ABR algorithms are generally composed of heuris- tics and learning-based. Heuristics make decisions from fea- tures with domain knowledge, e.g., throughput measured [13], buffer occupancy [7] or predefined models [8]. By con- trast, learning-based ABRs model the process as the Markov decision process (MDP): at each step t, the video client, often namely agent in RL framework, take a proper action at (i.e., select a proper bitrate) w.r.t current system status st. The agent then downloads the chunk and computes a reward rt for measuring the current quality-of-experience (QoE) of the past action. The proce

**[Acción / decisión ABR | extracto 10 | p.3]**

Fig. 2. Visualizing personalized networks from the real-world [2], [20], [21]. The video player client decodes and renders video frames from the playback buffer. Once the streaming service starts, the client fetches the video chunk from the HTTP Server or CDN orderly by an ABR algorithm. The ABR algorithm, implemented on the client-side, determines the next chunk and next chunk video quality via throughput estimation and current buffer utilization. After finishing the session, several metrics, such as total bitrate, total re-buffering time, and total bitrate change will be summarized as a QoE metric to evaluate the performance. Thus, how to achieve high QoE scores for adaptive video streaming has become a major challenge for ABR algorithms. Existing ABR algorithms are generally composed of heuris- tics and learning-based. Heuristics make decisions from fea- tures with domain knowledge, e.g., throughput measured [13], buffer occupancy [7] or predefined models [8]. By con- trast, learning-based ABRs model the process as the Markov decision process (MDP): at each step t, the video client, often namely agent in RL framework, take a proper action at (i.e., select a proper bitrate) w.r.t current system status st. The agent then downloads the chunk and computes a reward rt for measuring the current quality-of-experience (QoE) of the past action. The process will terminate if the agent finishes playing the video session. In the end, we aim to generalize a policy π to maximize the QoE of the entire session. The accumulated QoE objective function is defined as Eq. 1 ([8], [11]), where Rn represents the each chunk’s video bitrate, Tn reflects the rebuffering time for each chunk n, q(Rn) mea

**[Acción / decisión ABR | extracto 11 | p.3]**

on the client-side, determines the next chunk and next chunk video quality via throughput estimation and current buffer utilization. After finishing the session, several metrics, such as total bitrate, total re-buffering time, and total bitrate change will be summarized as a QoE metric to evaluate the performance. Thus, how to achieve high QoE scores for adaptive video streaming has become a major challenge for ABR algorithms. Existing ABR algorithms are generally composed of heuris- tics and learning-based. Heuristics make decisions from fea- tures with domain knowledge, e.g., throughput measured [13], buffer occupancy [7] or predefined models [8]. By con- trast, learning-based ABRs model the process as the Markov decision process (MDP): at each step t, the video client, often namely agent in RL framework, take a proper action at (i.e., select a proper bitrate) w.r.t current system status st. The agent then downloads the chunk and computes a reward rt for measuring the current quality-of-experience (QoE) of the past action. The process will terminate if the agent finishes playing the video session. In the end, we aim to generalize a policy π to maximize the QoE of the entire session. The accumulated QoE objective function is defined as Eq. 1 ([8], [11]), where Rn represents the each chunk’s video bitrate, Tn reflects the rebuffering time for each chunk n, q(Rn) means the quality metric such as video bitrate [8] and VMAF [22] (state-of-the-art quality assessment), μ and ρ are the weight of rebuffering and smoothness penalty, respectively. QoE = N  n=1 q(Rn) −μ N  n=1 Tn −ρ N−1  n=1 |q(Rn+1) −q(Rn)| (1) B. Different Types of Network Conditions Recently, several learning-based

**[Acción / decisión ABR | extracto 12 | p.3]**

ized network condition that is categorized by network types, which covers 3G, 4G, and 5G networks. Testing results on the bus, car, and metro environments show that different vehicle speeds lead to very different 3G bandwidth distri- butions. For instance, we can see the throughput measured from the metro achieves the lowest average and fluctuation value among the candidates. While we observe the highest bandwidth with high fluctuation in the 3G-car scenario. Mean- while, in addition to the various network specifics on 4G and 5G, the network distributions are always influenced by user behaviors: the network on walking and driving also have their particularity. Hence, the domain gap, which represents the relationship between network traffic distributions across different network types and users, has brought great challenges to recent rate adaptation algorithms. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.

**[Acción / decisión ABR | extracto 13 | p.4]**

nces for all users since the diversity of users’ network conditions. III. METHODS In this section, we start with modeling the tailored ABR process as an Input-driven Markov Decision Process (IMDP). Next, we explain why we have to construct a two-stage process rather than a vanilla one-stage approach. Finally, we briefly introduce meta-agnostic meta-learning and how to leverage domain knowledge. A. Input-Driven MDP Motivated by the observation above, we place the ABR problem in the discrete-time input-driven Markov decision process (MDP) [25], [26]. In detail, we consider the vanilla adaptive video streaming process: at each step t, the video client, often namely agent in RL framework, select a proper bitrate w.r.t current system status. The agent then downloads the chunk and computes an instant score for measuring the quality of the past action. The process continues until the agent finished playing the video session. Definition 1: An input-driven MDP M is defined by a 4-tuple M = (S, A, Z, R), in which S ⊆Rn is a set of n-dimensional states observed (e.g., past throughput mea- sured, buffer occupancy, past bitrate selected, etc.), A ⊆Rm is a set of m-dimensional actions, representing the bitrate candidates of next video chunks, Z = {z0, z1, . . . }, ⊆Rk is a set of k-dimensional input process, as S × A →R denotes the intermediate reward for each bitrate selection operation on the given state. Commonly, the input process in the ABR problem is often denoted as a set of exogenous variables. For example, the personalized network traffic distribution for each user, network status in various network types, tailored QoE preference, etc. Notably, zt is a general process, which is inde

**[Acción / decisión ABR | extracto 14 | p.4]**

2488 IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 Fig. 3. The key principle of our method. We consider learning a good parameter initialization (θ), which can fast adapt to personalized networks. 3) ABR Performance: How do existing one-fits-all ABR algorithms perform in such diverse but unique network con- ditions? Table I shows the average bitrate and stall ratio of existing ABR algorithms (§V-A4) over different mobility types (car and bus) [20]. We show that the irregular networks greatly disturb the stability of the learning-based algorithm, since the difference between the network traffic distributions of the training set and the testing set. Moreover, heuristics like BOLA and RobustMPC (RMPC here) often perform well in one scenario but fail in the other, e.g., BOLA gains a low average bitrate and RobustMPC performs with a high stall ratio. Results indicate that the domain gap among het- erogeneous network scenarios (e.g. Figure 2(b)) leads to the unstable performance of both heuristics and learning-based approaches [16], [24]. One of the feasible ways is to enable the policy to quickly adapt to the current network condition with few trials. As shown, our proposed method A2BR o

**[Acción / decisión ABR | extracto 15 | p.4]**

m well in one scenario but fail in the other, e.g., BOLA gains a low average bitrate and RobustMPC performs with a high stall ratio. Results indicate that the domain gap among het- erogeneous network scenarios (e.g. Figure 2(b)) leads to the unstable performance of both heuristics and learning-based approaches [16], [24]. One of the feasible ways is to enable the policy to quickly adapt to the current network condition with few trials. As shown, our proposed method A2BR outperforms existing techniques on video bitrate and stall ratio after being trained in 20-shot. In summary, we argue that off-the-shelf “one-fits-all” ABR algorithms fail to provide acceptable performances for all users since the diversity of users’ network conditions. III. METHODS In this section, we start with modeling the tailored ABR process as an Input-driven Markov Decision Process (IMDP). Next, we explain why we have to construct a two-stage process rather than a vanilla one-stage approach. Finally, we briefly introduce meta-agnostic meta-learning and how to leverage domain knowledge. A. Input-Driven MDP Motivated by the observation above, we place the ABR problem in the discrete-time input-driven Markov decision process (MDP) [25], [26]. In detail, we consider the vanilla adaptive video streaming process: at each step t, the video client, often namely agent in RL framework, select a proper bitrate w.r.t current system status. The agent then downloads the chunk and computes an instant score for measuring the quality of the past action. The process continues until the agent finished playing the video session. Definition 1: An input-driven MDP M is defined by a 4-tuple M = (S, A, Z, R), in which S ⊆Rn is a s

**[Acción / decisión ABR | extracto 16 | p.4]**

te and stall ratio after being trained in 20-shot. In summary, we argue that off-the-shelf “one-fits-all” ABR algorithms fail to provide acceptable performances for all users since the diversity of users’ network conditions. III. METHODS In this section, we start with modeling the tailored ABR process as an Input-driven Markov Decision Process (IMDP). Next, we explain why we have to construct a two-stage process rather than a vanilla one-stage approach. Finally, we briefly introduce meta-agnostic meta-learning and how to leverage domain knowledge. A. Input-Driven MDP Motivated by the observation above, we place the ABR problem in the discrete-time input-driven Markov decision process (MDP) [25], [26]. In detail, we consider the vanilla adaptive video streaming process: at each step t, the video client, often namely agent in RL framework, select a proper bitrate w.r.t current system status. The agent then downloads the chunk and computes an instant score for measuring the quality of the past action. The process continues until the agent finished playing the video session. Definition 1: An input-driven MDP M is defined by a 4-tuple M = (S, A, Z, R), in which S ⊆Rn is a set of n-dimensional states observed (e.g., past throughput mea- sured, buffer occupancy, past bitrate selected, etc.), A ⊆Rm is a set of m-dimensional actions, representing the bitrate candidates of next video chunks, Z = {z0, z1, . . . }, ⊆Rk is a set of k-dimensional input process, as S × A →R denotes the intermediate reward for each bitrate selection operation on the given state. Commonly, the input process in the ABR problem is often denoted as a set of exogenous variables. For example, the personalized networ

### 5.x Reward / QoE / objetivo

**[Reward / QoE / objetivo | extracto 1 | p.1]**

IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 2485 Learning Tailored Adaptive Bitrate Algorithms to Heterogeneous Network Conditions: A Domain-Specific Priors and Meta-Reinforcement Learning Approach Tianchi Huang , Student Member, IEEE, Chao Zhou, Rui-Xiao Zhang , Student Member, IEEE, Chenglei Wu, and Lifeng Sun , Member, IEEE Abstract—Internet adaptive video streaming is a typical form of video delivery that leverages adaptive bitrate (ABR) algorithms to provide video services with high quality of experience (QoE) for various users in diverse and unique network conditions. Such heterogeneous network environments, which can be viewed as exogenous input processes, often lead to the unstable perfor- mance of ABR algorithms. Unfortunately, learning-based ABR algorithm which generated by state-of-the-art reinforcement learning (RL) technologies achieves good average performance but fails to perform well in all kinds of network conditions. In this work, considering the video playback process as the Input-driven Markov Decision Process (IMDP), we propose A2BR (Adaptation of ABR), a novel meta-RL ABR approach. A2BR is mainly composed of an online stage and an offline stage. It leverages meta-RL to learn an initial meta-policy with various network conditions at the offline stage and makes decisions in personalized network conditions at the online stage. A

**[Reward / QoE / objetivo | extracto 2 | p.1]**

twork types, and heterogeneous user- preferences, we show that A2BR outperforming recent ABR approaches with rapidly adapting to the personalized QoE metrics and specific network conditions. Testbed experimental results also illustrate the superiority of A2BR in adapting to the unseen environments. Index Terms—Streaming media, reinforcement learning (RL), adaptive control. I. INTRODUCTION D UE to the rapid development of network services, video streaming now stands for the predominant Internet appli- cation, which is up almost 75% all traffic [1], [2]. Espe- cially, adaptive video streaming, such as HLS (HTTP Live Streaming) [3] and DASH [4] has already been the popular form of video delivery [5]. Adaptive bitrate (ABR) algorithms enable Internet adaptive video streaming services to achieve high video quality while avoiding uninterrupted stall event [5] (§II-A). Revisiting the recent success of ABR algorithms, heuristics often make decisions based on network or player sta- tus [6]–[8]. However, those schemes require a proper setting of configuration parameters [9], [10] for fitting different network distributions. By contrast, learning-based schemes employ several learning technologies, such as reinforcement learning [11], [12], supervised learning [2], [13] and imitation learn- ing [14], [15] to train a neural network (NN) w.r.t the given network traffic distributions, and make a zero-shot inference for unseen networks. In short, existing ABR algorithms, either heuristics or learning-based schemes, seldom configure or tune their parameters automatically and rapidly for varying the current network traffic distribution. However, in the adaptive video streaming scenario, the sys

**[Reward / QoE / objetivo | extracto 3 | p.2]**

fic network status. Upon finishing the video session, the meta-policy is continually updated to the tailor-made policy with the collected trajectories. For improving the learning efficiency, the trajec- tories are collected not only from the real world but also from the “virtual world.” Specifically, the virtual world is motivated by domain principles and constructed by a faithful virtual player and experienced network environments. In addition, we also employ the domain knowledge that uses heuristics to enable safe online RL. Subsequently, the meta-policy will be continually optimized within 20-shot, i.e., watch 20 videos at the online stage (§IV-C). In the rest of the paper, we conduct several experiments to evaluate A2BR with existing ABR approaches (§V). The case studies contain different types of heterogeneous network conditions and QoE objectives, including differ- ent vehicles, users’ personalized networks, 4G/5G networks, and varying user preferences for QoE metrics. Using trace- driven simulation and real-world evaluation on various videos, we show: Fig. 1. The typical ABR system overview. The ABR algorithm is usually placed on the client-side. 1) A2BR improves the video quality by up to 12.6% while reducing the stall time by 69.3% to 2.8× compared with previously proposed approaches. 2) In the user-personalized network, A2BR outperforms recent heuristics and learning-based ABRs, with improvements on average QoE of 12%-23%; 3) A2BR maintains high bitrates with low video stall in both 4G and 5G networks, whereas the learning-based approach Pensieve diverges. At the same time, A2BR either matches or exceeds the performance of existing schemes on IT-T Rec P.1203 QoE me

**[Reward / QoE / objetivo | extracto 4 | p.2]**

2486 IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 users at any time, in any place, and especially, under any network conditions. Through the analysis of the impact on the network distributions of different users, vehicles, and network types, we empirically find that nowadays’ Internet network conditions are not only diverse but also unique (§II-B). For example, the heterogeneity of network conditions for each user is inevitable, since both subjective and objective user behavior have an important impact on the network traffic distribution. Nevertheless, existing ABR algorithms, either heuristics or learning-based, fail to adapt to such heterogeneous bandwidth conditions that are significantly different from the offline training (or tuning) network dataset [16]. Motivated by these facts, we model the ABR playback process as Input-driven Markov Decision Process (IMDP), which can express an implicit heterogeneous network envi- ronment in an explicit manner (§III-A). We theoretically illustrate that vanilla RL technologies can only generalize a strategy that can perform well on average rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL metho

**[Reward / QoE / objetivo | extracto 5 | p.2]**

player and experienced network environments. In addition, we also employ the domain knowledge that uses heuristics to enable safe online RL. Subsequently, the meta-policy will be continually optimized within 20-shot, i.e., watch 20 videos at the online stage (§IV-C). In the rest of the paper, we conduct several experiments to evaluate A2BR with existing ABR approaches (§V). The case studies contain different types of heterogeneous network conditions and QoE objectives, including differ- ent vehicles, users’ personalized networks, 4G/5G networks, and varying user preferences for QoE metrics. Using trace- driven simulation and real-world evaluation on various videos, we show: Fig. 1. The typical ABR system overview. The ABR algorithm is usually placed on the client-side. 1) A2BR improves the video quality by up to 12.6% while reducing the stall time by 69.3% to 2.8× compared with previously proposed approaches. 2) In the user-personalized network, A2BR outperforms recent heuristics and learning-based ABRs, with improvements on average QoE of 12%-23%; 3) A2BR maintains high bitrates with low video stall in both 4G and 5G networks, whereas the learning-based approach Pensieve diverges. At the same time, A2BR either matches or exceeds the performance of existing schemes on IT-T Rec P.1203 QoE metric [19]. The average QoE is 10% higher than the closest ABR approach Fugu [2]. 4) A2BR with minor modification can hold QoE metrics with different user preferences, further providing 5% improve- ments on QoE at the online stage. 5) We prove that A2BR still performs well on both emulation and real-world testbed. Ablution studies show that the online stage further improves the average QoE b

**[Reward / QoE / objetivo | extracto 6 | p.3]**

rrent buffer utilization. After finishing the session, several metrics, such as total bitrate, total re-buffering time, and total bitrate change will be summarized as a QoE metric to evaluate the performance. Thus, how to achieve high QoE scores for adaptive video streaming has become a major challenge for ABR algorithms. Existing ABR algorithms are generally composed of heuris- tics and learning-based. Heuristics make decisions from fea- tures with domain knowledge, e.g., throughput measured [13], buffer occupancy [7] or predefined models [8]. By con- trast, learning-based ABRs model the process as the Markov decision process (MDP): at each step t, the video client, often namely agent in RL framework, take a proper action at (i.e., select a proper bitrate) w.r.t current system status st. The agent then downloads the chunk and computes a reward rt for measuring the current quality-of-experience (QoE) of the past action. The process will terminate if the agent finishes playing the video session. In the end, we aim to generalize a policy π to maximize the QoE of the entire session. The accumulated QoE objective function is defined as Eq. 1 ([8], [11]), where Rn represents the each chunk’s video bitrate, Tn reflects the rebuffering time for each chunk n, q(Rn) means the quality metric such as video bitrate [8] and VMAF [22] (state-of-the-art quality assessment), μ and ρ are the weight of rebuffering and smoothness penalty, respectively. QoE = N  n=1 q(Rn) −μ N  n=1 Tn −ρ N−1  n=1 |q(Rn+1) −q(Rn)| (1) B. Different Types of Network Conditions Recently, several learning-based schemes have been made to train an NN policy from the clean slate via various RL methods [11], [23]. Unfor

**[Reward / QoE / objetivo | extracto 7 | p.3]**

HUANG et al.: LEARNING TAILORED ABR ALGORITHMS TO HETEROGENEOUS NETWORK CONDITIONS 2487 Fig. 2. Visualizing personalized networks from the real-world [2], [20], [21]. The video player client decodes and renders video frames from the playback buffer. Once the streaming service starts, the client fetches the video chunk from the HTTP Server or CDN orderly by an ABR algorithm. The ABR algorithm, implemented on the client-side, determines the next chunk and next chunk video quality via throughput estimation and current buffer utilization. After finishing the session, several metrics, such as total bitrate, total re-buffering time, and total bitrate change will be summarized as a QoE metric to evaluate the performance. Thus, how to achieve high QoE scores for adaptive video streaming has become a major challenge for ABR algorithms. Existing ABR algorithms are generally composed of heuris- tics and learning-based. Heuristics make decisions from fea- tures with domain knowledge, e.g., throughput measured [13], buffer occupancy [7] or predefined models [8]. By con- trast, learning-based ABRs model the process as the Markov decision process (MDP): at each step t, the video client, often namely agent in RL framework, take a proper action at (i.e., select a proper bitrate) w.r.t current system status st. The agent then downloads the chunk and computes a reward rt for measuring the current quality-of-experience (QoE) of the past action. The process will terminate if the agent finishes playing the video session. In the end,

**[Reward / QoE / objetivo | extracto 8 | p.3]**

reaming has become a major challenge for ABR algorithms. Existing ABR algorithms are generally composed of heuris- tics and learning-based. Heuristics make decisions from fea- tures with domain knowledge, e.g., throughput measured [13], buffer occupancy [7] or predefined models [8]. By con- trast, learning-based ABRs model the process as the Markov decision process (MDP): at each step t, the video client, often namely agent in RL framework, take a proper action at (i.e., select a proper bitrate) w.r.t current system status st. The agent then downloads the chunk and computes a reward rt for measuring the current quality-of-experience (QoE) of the past action. The process will terminate if the agent finishes playing the video session. In the end, we aim to generalize a policy π to maximize the QoE of the entire session. The accumulated QoE objective function is defined as Eq. 1 ([8], [11]), where Rn represents the each chunk’s video bitrate, Tn reflects the rebuffering time for each chunk n, q(Rn) means the quality metric such as video bitrate [8] and VMAF [22] (state-of-the-art quality assessment), μ and ρ are the weight of rebuffering and smoothness penalty, respectively. QoE = N  n=1 q(Rn) −μ N  n=1 Tn −ρ N−1  n=1 |q(Rn+1) −q(Rn)| (1) B. Different Types of Network Conditions Recently, several learning-based schemes have been made to train an NN policy from the clean slate via various RL methods [11], [23]. Unfortunately, such one-fits-all schemes, including heuristics and learning-based can hardly always perform well in today’s network traffics due to the diversity of real-world network conditions [2]. We show the personalized network environments from two perspectives. TABLE

**[Reward / QoE / objetivo | extracto 9 | p.3]**

and learning-based. Heuristics make decisions from fea- tures with domain knowledge, e.g., throughput measured [13], buffer occupancy [7] or predefined models [8]. By con- trast, learning-based ABRs model the process as the Markov decision process (MDP): at each step t, the video client, often namely agent in RL framework, take a proper action at (i.e., select a proper bitrate) w.r.t current system status st. The agent then downloads the chunk and computes a reward rt for measuring the current quality-of-experience (QoE) of the past action. The process will terminate if the agent finishes playing the video session. In the end, we aim to generalize a policy π to maximize the QoE of the entire session. The accumulated QoE objective function is defined as Eq. 1 ([8], [11]), where Rn represents the each chunk’s video bitrate, Tn reflects the rebuffering time for each chunk n, q(Rn) means the quality metric such as video bitrate [8] and VMAF [22] (state-of-the-art quality assessment), μ and ρ are the weight of rebuffering and smoothness penalty, respectively. QoE = N  n=1 q(Rn) −μ N  n=1 Tn −ρ N−1  n=1 |q(Rn+1) −q(Rn)| (1) B. Different Types of Network Conditions Recently, several learning-based schemes have been made to train an NN policy from the clean slate via various RL methods [11], [23]. Unfortunately, such one-fits-all schemes, including heuristics and learning-based can hardly always perform well in today’s network traffics due to the diversity of real-world network conditions [2]. We show the personalized network environments from two perspectives. TABLE I COMPARISON RESULTS ON DIFFERENT ABRS OVER 3G-CAR AND 3G-BUS NETWORKS, WHERE A2BR IS FINE-TUNED IN 20-SHOT 1) Sorted b

**[Reward / QoE / objetivo | extracto 10 | p.3]**

-based ABRs model the process as the Markov decision process (MDP): at each step t, the video client, often namely agent in RL framework, take a proper action at (i.e., select a proper bitrate) w.r.t current system status st. The agent then downloads the chunk and computes a reward rt for measuring the current quality-of-experience (QoE) of the past action. The process will terminate if the agent finishes playing the video session. In the end, we aim to generalize a policy π to maximize the QoE of the entire session. The accumulated QoE objective function is defined as Eq. 1 ([8], [11]), where Rn represents the each chunk’s video bitrate, Tn reflects the rebuffering time for each chunk n, q(Rn) means the quality metric such as video bitrate [8] and VMAF [22] (state-of-the-art quality assessment), μ and ρ are the weight of rebuffering and smoothness penalty, respectively. QoE = N  n=1 q(Rn) −μ N  n=1 Tn −ρ N−1  n=1 |q(Rn+1) −q(Rn)| (1) B. Different Types of Network Conditions Recently, several learning-based schemes have been made to train an NN policy from the clean slate via various RL methods [11], [23]. Unfortunately, such one-fits-all schemes, including heuristics and learning-based can hardly always perform well in today’s network traffics due to the diversity of real-world network conditions [2]. We show the personalized network environments from two perspectives. TABLE I COMPARISON RESULTS ON DIFFERENT ABRS OVER 3G-CAR AND 3G-BUS NETWORKS, WHERE A2BR IS FINE-TUNED IN 20-SHOT 1) Sorted by Users: First, we measure a portion of data from the Puffer project [2] and demonstrate the users’ personalized network status on June 2, 2021, in Figure 2(a). The left figure illustra

**[Reward / QoE / objetivo | extracto 11 | p.3]**

ghput measured [13], buffer occupancy [7] or predefined models [8]. By con- trast, learning-based ABRs model the process as the Markov decision process (MDP): at each step t, the video client, often namely agent in RL framework, take a proper action at (i.e., select a proper bitrate) w.r.t current system status st. The agent then downloads the chunk and computes a reward rt for measuring the current quality-of-experience (QoE) of the past action. The process will terminate if the agent finishes playing the video session. In the end, we aim to generalize a policy π to maximize the QoE of the entire session. The accumulated QoE objective function is defined as Eq. 1 ([8], [11]), where Rn represents the each chunk’s video bitrate, Tn reflects the rebuffering time for each chunk n, q(Rn) means the quality metric such as video bitrate [8] and VMAF [22] (state-of-the-art quality assessment), μ and ρ are the weight of rebuffering and smoothness penalty, respectively. QoE = N  n=1 q(Rn) −μ N  n=1 Tn −ρ N−1  n=1 |q(Rn+1) −q(Rn)| (1) B. Different Types of Network Conditions Recently, several learning-based schemes have been made to train an NN policy from the clean slate via various RL methods [11], [23]. Unfortunately, such one-fits-all schemes, including heuristics and learning-based can hardly always perform well in today’s network traffics due to the diversity of real-world network conditions [2]. We show the personalized network environments from two perspectives. TABLE I COMPARISON RESULTS ON DIFFERENT ABRS OVER 3G-CAR AND 3G-BUS NETWORKS, WHERE A2BR IS FINE-TUNED IN 20-SHOT 1) Sorted by Users: First, we measure a portion of data from the Puffer project [2] and demonstrate the

**[Reward / QoE / objetivo | extracto 12 | p.4]**

ut-driven Markov decision process (MDP) [25], [26]. In detail, we consider the vanilla adaptive video streaming process: at each step t, the video client, often namely agent in RL framework, select a proper bitrate w.r.t current system status. The agent then downloads the chunk and computes an instant score for measuring the quality of the past action. The process continues until the agent finished playing the video session. Definition 1: An input-driven MDP M is defined by a 4-tuple M = (S, A, Z, R), in which S ⊆Rn is a set of n-dimensional states observed (e.g., past throughput mea- sured, buffer occupancy, past bitrate selected, etc.), A ⊆Rm is a set of m-dimensional actions, representing the bitrate candidates of next video chunks, Z = {z0, z1, . . . }, ⊆Rk is a set of k-dimensional input process, as S × A →R denotes the intermediate reward for each bitrate selection operation on the given state. Commonly, the input process in the ABR problem is often denoted as a set of exogenous variables. For example, the personalized network traffic distribution for each user, network status in various network types, tailored QoE preference, etc. Notably, zt is a general process, which is independent for the state st and action at. In other words, the at depends on st only, with no relationship to zt – this is the key dif- ference between input-driven MDPs and Partially Observable MDPs [27]. The reward function for ABR algorithms is often defined to achieve high quality of experience (QoE). Definition 2: For an input-driven MDPs, the stochastic transition dynamics are given by Ta(s′; s, z) = Pr(st+1 = s′; st = s, at = a, zt = z), (2) representing a state-transition probability of next s

**[Reward / QoE / objetivo | extracto 13 | p.4]**

mputes an instant score for measuring the quality of the past action. The process continues until the agent finished playing the video session. Definition 1: An input-driven MDP M is defined by a 4-tuple M = (S, A, Z, R), in which S ⊆Rn is a set of n-dimensional states observed (e.g., past throughput mea- sured, buffer occupancy, past bitrate selected, etc.), A ⊆Rm is a set of m-dimensional actions, representing the bitrate candidates of next video chunks, Z = {z0, z1, . . . }, ⊆Rk is a set of k-dimensional input process, as S × A →R denotes the intermediate reward for each bitrate selection operation on the given state. Commonly, the input process in the ABR problem is often denoted as a set of exogenous variables. For example, the personalized network traffic distribution for each user, network status in various network types, tailored QoE preference, etc. Notably, zt is a general process, which is independent for the state st and action at. In other words, the at depends on st only, with no relationship to zt – this is the key dif- ference between input-driven MDPs and Partially Observable MDPs [27]. The reward function for ABR algorithms is often defined to achieve high quality of experience (QoE). Definition 2: For an input-driven MDPs, the stochastic transition dynamics are given by Ta(s′; s, z) = Pr(st+1 = s′; st = s, at = a, zt = z), (2) representing a state-transition probability of next state st+1 with the given any state st, action at, and current personalized networks zt. Definition 3: Followed by the definition of input-driven MDP, the Q-value of a given state-action pair can be defined as Q(s, a, z) =  s′∈S Ta(s′; s, z) (r(s, z, a) + γV (s′, z′)) (3) Here V (s

**[Reward / QoE / objetivo | extracto 14 | p.4]**

e selected, etc.), A ⊆Rm is a set of m-dimensional actions, representing the bitrate candidates of next video chunks, Z = {z0, z1, . . . }, ⊆Rk is a set of k-dimensional input process, as S × A →R denotes the intermediate reward for each bitrate selection operation on the given state. Commonly, the input process in the ABR problem is often denoted as a set of exogenous variables. For example, the personalized network traffic distribution for each user, network status in various network types, tailored QoE preference, etc. Notably, zt is a general process, which is independent for the state st and action at. In other words, the at depends on st only, with no relationship to zt – this is the key dif- ference between input-driven MDPs and Partially Observable MDPs [27]. The reward function for ABR algorithms is often defined to achieve high quality of experience (QoE). Definition 2: For an input-driven MDPs, the stochastic transition dynamics are given by Ta(s′; s, z) = Pr(st+1 = s′; st = s, at = a, zt = z), (2) representing a state-transition probability of next state st+1 with the given any state st, action at, and current personalized networks zt. Definition 3: Followed by the definition of input-driven MDP, the Q-value of a given state-action pair can be defined as Q(s, a, z) =  s′∈S Ta(s′; s, z) (r(s, z, a) + γV (s′, z′)) (3) Here V (s′, z′) is the value function for state s′, γ is the discounted factor ∈[0, 1). When γ < 1, there exists an optimal policy π∗(s, z): π∗(s, z) = arg max a∈A  s′∈S Ta(s′, z′; s, z) ×  r(s, z, a) + γ max a′∈A Q(s′, a′, z′)  (4) Here we consider two agents with the same policy π, while they work in the IMDPs with different input processes Z1 and Z2. When observ

**[Reward / QoE / objetivo | extracto 15 | p.4]**

2488 IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 Fig. 3. The key principle of our method. We consider learning a good parameter initialization (θ), which can fast adapt to personalized networks. 3) ABR Performance: How do existing one-fits-all ABR algorithms perform in such diverse but unique network con- ditions? Table I shows the average bitrate and stall ratio of existing ABR algorithms (§V-A4) over different mobility types (car and bus) [20]. We show that the irregular networks greatly disturb the stability of the learning-based algorithm, since the difference between the network traffic distributions of the training set and the testing set. Moreover, heuristics like BOLA and RobustMPC (RMPC here) often perform well in one scenario but fail in the other, e.g., BOLA gains a low average bitrate and RobustMPC performs with a high stall ratio. Results indicate that the domain gap among het- erogeneous network scenarios (e.g. Figure 2(b)) leads to the unstable performance of both heuristics and learning-based approaches [16], [24]. One of the feasible ways is to enable the policy to quickly adapt to the current network condition with few trials. As shown, our proposed method A2BR outperforms

**[Reward / QoE / objetivo | extracto 16 | p.4]**

ition of input-driven MDP, the Q-value of a given state-action pair can be defined as Q(s, a, z) =  s′∈S Ta(s′; s, z) (r(s, z, a) + γV (s′, z′)) (3) Here V (s′, z′) is the value function for state s′, γ is the discounted factor ∈[0, 1). When γ < 1, there exists an optimal policy π∗(s, z): π∗(s, z) = arg max a∈A  s′∈S Ta(s′, z′; s, z) ×  r(s, z, a) + γ max a′∈A Q(s′, a′, z′)  (4) Here we consider two agents with the same policy π, while they work in the IMDPs with different input processes Z1 and Z2. When observing the same state s, the following agents would determine the same action a. Thus, the difference between the Q values of two agents will be equal only if Z1 equals Z2. For solving Eq. 4, we can employ various reinforcement learning (RL) strategies if Z is known before the process starts. However, in practice, the agent cannot perceptualize its personalized network traffic before transmitting video streams. Assuming that the input process Z is “agnostic” for the agent, we find that vanilla RL method can only learn the optimal policy ˆπ∗which is relevant to Q(s′, a′) instead of Q(s′, a′, z′): max a′∈A Q(s′, a′) = Ez′∼T max a′∈A[Q(s′, a′, z′)]. (5) There exists the variance reduction between the two cases, which eventually results in the sub-optimal policy [26]. Hence, we have a challenge here: considering that the input process can hardly be explicitly observed, how to learn a tailor-made ABR algorithm for heterogeneous network conditions? Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.

### 5.x Entrenamiento / optimización

**[Entrenamiento / optimización | extracto 1 | p.1]**

s for the predominant Internet appli- cation, which is up almost 75% all traffic [1], [2]. Espe- cially, adaptive video streaming, such as HLS (HTTP Live Streaming) [3] and DASH [4] has already been the popular form of video delivery [5]. Adaptive bitrate (ABR) algorithms enable Internet adaptive video streaming services to achieve high video quality while avoiding uninterrupted stall event [5] (§II-A). Revisiting the recent success of ABR algorithms, heuristics often make decisions based on network or player sta- tus [6]–[8]. However, those schemes require a proper setting of configuration parameters [9], [10] for fitting different network distributions. By contrast, learning-based schemes employ several learning technologies, such as reinforcement learning [11], [12], supervised learning [2], [13] and imitation learn- ing [14], [15] to train a neural network (NN) w.r.t the given network traffic distributions, and make a zero-shot inference for unseen networks. In short, existing ABR algorithms, either heuristics or learning-based schemes, seldom configure or tune their parameters automatically and rapidly for varying the current network traffic distribution. However, in the adaptive video streaming scenario, the system dynamics are uncertain and the future state cannot be accurately predicted. To prove this view, we focus on inves- tigating the impact of ABR algorithms on the distribution of heterogeneous network traffics, where the distribution is usu- ally summarized by bandwidth traces experienced by different 0733-8716 © 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html

**[Entrenamiento / optimización | extracto 2 | p.1]**

services, video streaming now stands for the predominant Internet appli- cation, which is up almost 75% all traffic [1], [2]. Espe- cially, adaptive video streaming, such as HLS (HTTP Live Streaming) [3] and DASH [4] has already been the popular form of video delivery [5]. Adaptive bitrate (ABR) algorithms enable Internet adaptive video streaming services to achieve high video quality while avoiding uninterrupted stall event [5] (§II-A). Revisiting the recent success of ABR algorithms, heuristics often make decisions based on network or player sta- tus [6]–[8]. However, those schemes require a proper setting of configuration parameters [9], [10] for fitting different network distributions. By contrast, learning-based schemes employ several learning technologies, such as reinforcement learning [11], [12], supervised learning [2], [13] and imitation learn- ing [14], [15] to train a neural network (NN) w.r.t the given network traffic distributions, and make a zero-shot inference for unseen networks. In short, existing ABR algorithms, either heuristics or learning-based schemes, seldom configure or tune their parameters automatically and rapidly for varying the current network traffic distribution. However, in the adaptive video streaming scenario, the system dynamics are uncertain and the future state cannot be accurately predicted. To prove this view, we focus on inves- tigating the impact of ABR algorithms on the distribution of heterogeneous network traffics, where the distribution is usu- ally summarized by bandwidth traces experienced by different 0733-8716 © 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org

**[Entrenamiento / optimización | extracto 3 | p.1]**

e but fails to perform well in all kinds of network conditions. In this work, considering the video playback process as the Input-driven Markov Decision Process (IMDP), we propose A2BR (Adaptation of ABR), a novel meta-RL ABR approach. A2BR is mainly composed of an online stage and an offline stage. It leverages meta-RL to learn an initial meta-policy with various network conditions at the offline stage and makes decisions in personalized network conditions at the online stage. At the same time, we continually optimize the meta-policy to the tailor- made ABR policy for varying the current network environment within few shots. Moreover, in order to improve the learning Manuscript received 15 December 2021; revised 15 March 2022; accepted 23 April 2022. Date of publication 15 June 2022; date of current version 18 July 2022. This work was supported in part by the National Key Research and Development Program of China under Grant 2018YFB1003703, in part by NSFC under Grant 61936011, in part by the Beijing Key Laboratory of Networked Multimedia, and in part by the Kuaishou-Tsinghua Joint Project under Grant 20192000456. (Corresponding authors: Lifeng Sun; Chao Zhou.) Tianchi Huang is with the Beijing Key Laboratory of Networked Multime- dia, Department of Computer Science and Technology, Tsinghua University, Beijing 100084, China (e-mail: htc19@mails.tsinghua.edu.cn). Chao Zhou is with Beijing Kuaishou Technology Company Ltd., Beijing 100085, China (e-mail: zhouchao@kuaishou.com). Rui-Xiao Zhang and Chenglei Wu are with the Beijing National Research Center for Information Science and Technology (BNRist), Department of Computer Science and Technology, Tsinghua Univer- sity, Beijin

**[Entrenamiento / optimización | extracto 4 | p.2]**

2486 IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 users at any time, in any place, and especially, under any network conditions. Through the analysis of the impact on the network distributions of different users, vehicles, and network types, we empirically find that nowadays’ Internet network conditions are not only diverse but also unique (§II-B). For example, the heterogeneity of network conditions for each user is inevitable, since both subjective and objective user behavior have an important impact on the network traffic distribution. Nevertheless, existing ABR algorithms, either heuristics or learning-based, fail to adapt to such heterogeneous bandwidth conditions that are significantly different from the offline training (or tuning) network dataset [16]. Motivated by these facts, we model the ABR playback process as Input-driven Markov Decision Process (IMDP), which can express an implicit heterogeneous network envi- ronment in an explicit manner (§III-A). We theoretically illustrate that vanilla RL technologies can only generalize a strategy that can perform well on average rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel neural meta-RL ABR system that enables fast adaptation to the specif

**[Entrenamiento / optimización | extracto 5 | p.2]**

rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel neural meta-RL ABR system that enables fast adaptation to the specific network conditions (§III-B). A2BR is composed of the offline stage and online stage (§IV). At the offline stage, A2BR trains a meta-model with various real and synthetic network conditions for learning parameter initialization meta-policy, where the policy can provide rapid adaptation for varying heterogeneous networks. To achieve this goal, we implement the training process based on the state-of-the-art gradient-free meta-learning technology [18] and utilize maximum entropy RL methodologies to achieve better exploration (§IV-B). Moreover, at the online stage, the video player, placed on the user side, receives the trained meta-model and picks the bitrates w.r.t the meta-policy and the current specific network status. Upon finishing the video session, the meta-policy is continually updated to the tailor-made policy with the collected trajectories. For improving the learning efficiency, the trajec- tories are collected not only from the real world but also from the “virtual world.” Specifically, the virtual world is motivated by domain principles and constructed by a faithful virtual player and experienced network environments. In addition, we also employ the domain knowledge that uses heuristics to e

**[Entrenamiento / optimización | extracto 6 | p.2]**

ough in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel neural meta-RL ABR system that enables fast adaptation to the specific network conditions (§III-B). A2BR is composed of the offline stage and online stage (§IV). At the offline stage, A2BR trains a meta-model with various real and synthetic network conditions for learning parameter initialization meta-policy, where the policy can provide rapid adaptation for varying heterogeneous networks. To achieve this goal, we implement the training process based on the state-of-the-art gradient-free meta-learning technology [18] and utilize maximum entropy RL methodologies to achieve better exploration (§IV-B). Moreover, at the online stage, the video player, placed on the user side, receives the trained meta-model and picks the bitrates w.r.t the meta-policy and the current specific network status. Upon finishing the video session, the meta-policy is continually updated to the tailor-made policy with the collected trajectories. For improving the learning efficiency, the trajec- tories are collected not only from the real world but also from the “virtual world.” Specifically, the virtual world is motivated by domain principles and constructed by a faithful virtual player and experienced network environments. In addition, we also employ the domain knowledge that uses heuristics to enable safe online RL. Subsequently, the meta-po

**[Entrenamiento / optimización | extracto 7 | p.2]**

ot. The contributions of this work are summarized as follows: • We empirically analyze today’s heterogeneous network traf- fics and propose a two-stage meta-learning scheme for varying specific network conditions. • We implement A2BR, which is the first meta-learning with domain knowledge approach for adaptive streaming. • Results on different types of network conditions illustrate that the generated tailor-made ABR policies can well adapt to heterogeneous networks with relatively few-shot. II. BACKGROUND AND MOTIVATION Our research is started with a fundamental quest: How will the recent ABRs perform in various network traffic environ- ments?. To answer this question, first, we briefly introduce the key principle of adaptive video streaming and adaptive bitrate (ABR) algorithms. We then use empirical measure- ments to elucidate the key limitations of prior solutions. A. Adaptive Video Streaming The adaptive bitrate method (ABR) is an algorithm that dynamically selects video bitrates via network conditions and the client’s buffer occupancy. The traditional video stream- ing architecture is shown in Figure 1. The system consists of a video player client with a constrained buffer length and an HTTP-Server or Content Delivery Network (CDN). Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.

**[Entrenamiento / optimización | extracto 8 | p.3]**

rrent system status st. The agent then downloads the chunk and computes a reward rt for measuring the current quality-of-experience (QoE) of the past action. The process will terminate if the agent finishes playing the video session. In the end, we aim to generalize a policy π to maximize the QoE of the entire session. The accumulated QoE objective function is defined as Eq. 1 ([8], [11]), where Rn represents the each chunk’s video bitrate, Tn reflects the rebuffering time for each chunk n, q(Rn) means the quality metric such as video bitrate [8] and VMAF [22] (state-of-the-art quality assessment), μ and ρ are the weight of rebuffering and smoothness penalty, respectively. QoE = N  n=1 q(Rn) −μ N  n=1 Tn −ρ N−1  n=1 |q(Rn+1) −q(Rn)| (1) B. Different Types of Network Conditions Recently, several learning-based schemes have been made to train an NN policy from the clean slate via various RL methods [11], [23]. Unfortunately, such one-fits-all schemes, including heuristics and learning-based can hardly always perform well in today’s network traffics due to the diversity of real-world network conditions [2]. We show the personalized network environments from two perspectives. TABLE I COMPARISON RESULTS ON DIFFERENT ABRS OVER 3G-CAR AND 3G-BUS NETWORKS, WHERE A2BR IS FINE-TUNED IN 20-SHOT 1) Sorted by Users: First, we measure a portion of data from the Puffer project [2] and demonstrate the users’ personalized network status on June 2, 2021, in Figure 2(a). The left figure illustrates the correlations between throughput and round- trip-time (RTT) of each user. As shown, in the real world, the average bandwidth is particularly varied, ranging from 0.1 to 100 Mbps. The lower bandw

**[Entrenamiento / optimización | extracto 9 | p.3]**

bitrate, Tn reflects the rebuffering time for each chunk n, q(Rn) means the quality metric such as video bitrate [8] and VMAF [22] (state-of-the-art quality assessment), μ and ρ are the weight of rebuffering and smoothness penalty, respectively. QoE = N  n=1 q(Rn) −μ N  n=1 Tn −ρ N−1  n=1 |q(Rn+1) −q(Rn)| (1) B. Different Types of Network Conditions Recently, several learning-based schemes have been made to train an NN policy from the clean slate via various RL methods [11], [23]. Unfortunately, such one-fits-all schemes, including heuristics and learning-based can hardly always perform well in today’s network traffics due to the diversity of real-world network conditions [2]. We show the personalized network environments from two perspectives. TABLE I COMPARISON RESULTS ON DIFFERENT ABRS OVER 3G-CAR AND 3G-BUS NETWORKS, WHERE A2BR IS FINE-TUNED IN 20-SHOT 1) Sorted by Users: First, we measure a portion of data from the Puffer project [2] and demonstrate the users’ personalized network status on June 2, 2021, in Figure 2(a). The left figure illustrates the correlations between throughput and round- trip-time (RTT) of each user. As shown, in the real world, the average bandwidth is particularly varied, ranging from 0.1 to 100 Mbps. The lower bandwidth leads to larger RTT. The network environment of each user is different. Someone can watch the videos with high bandwidth and low RTT, while the others live in the low bandwidth and high RTT scenario. The right figure plots the fine-grained cumulative distribution function (CDF) of throughput and RTT of the users with top-8 viewing hours on that day. We can find the tailor-made features for personalized network conditions: some of t

**[Entrenamiento / optimización | extracto 10 | p.3]**

sonalized network conditions: some of the users have very constant throughput (e.g., user C and user F), while most of the users’ bandwidth is unstable and doesn’t cover all network conditions. 2) Sorted by Scenarios: Next, Figure 2(b) shows another personalized network condition that is categorized by network types, which covers 3G, 4G, and 5G networks. Testing results on the bus, car, and metro environments show that different vehicle speeds lead to very different 3G bandwidth distri- butions. For instance, we can see the throughput measured from the metro achieves the lowest average and fluctuation value among the candidates. While we observe the highest bandwidth with high fluctuation in the 3G-car scenario. Mean- while, in addition to the various network specifics on 4G and 5G, the network distributions are always influenced by user behaviors: the network on walking and driving also have their particularity. Hence, the domain gap, which represents the relationship between network traffic distributions across different network types and users, has brought great challenges to recent rate adaptation algorithms. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.

**[Entrenamiento / optimización | extracto 11 | p.4]**

2488 IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 Fig. 3. The key principle of our method. We consider learning a good parameter initialization (θ), which can fast adapt to personalized networks. 3) ABR Performance: How do existing one-fits-all ABR algorithms perform in such diverse but unique network con- ditions? Table I shows the average bitrate and stall ratio of existing ABR algorithms (§V-A4) over different mobility types (car and bus) [20]. We show that the irregular networks greatly disturb the stability of the learning-based algorithm, since the difference between the network traffic distributions of the training set and the testing set. Moreover, heuristics like BOLA and RobustMPC (RMPC here) often perform well in one scenario but fail in the other, e.g., BOLA gains a low average bitrate and RobustMPC performs with a high stall ratio. Results indicate that the domain gap among het- erogeneous network scenarios (e.g. Figure 2(b)) leads to the unstable performance of both heuristics and learning-based approaches [16], [24]. One of the feasible ways is to enable the policy to quickly adapt to the current network condition with few trials. As shown, our proposed method A2BR outperforms existing techniques on video bitrate and stall ratio after being trained in 20-shot. In summary, we argue that off-the-shelf “one-fits-all” ABR algorithms fail to provide acceptable performances for all users since the diversity of users’ network conditions. III. M

**[Entrenamiento / optimización | extracto 12 | p.5]**

HUANG et al.: LEARNING TAILORED ABR ALGORITHMS TO HETEROGENEOUS NETWORK CONDITIONS 2489 Fig. 4. The system overview of A2BR. A2BR mainly consists of two stages, the offline stage and the online stage. B. Meta-RL With Domain Knowledge With the rapid progress of on-device machine learning in both academia [28] and industry [29], training NNs on users’ devices has already been a practical way of learning the tailor-made ABR policy from a clean slate in situ. Neverthe- less, recent model-free RL technologies lack sample efficiency, which requires high convergence time on each client [2]. For example, a single agent requires at least 640,000 steps, spanning over 2 years, to converge in the real world. Most users would leave the platform before the algorithm has been completely trained [11]. In this paper, we consider a two-stage approach, which is composed of offline stage and online stage. Technically, at the offline stage, we attempt to train the meta policy via the traces collected by different network conditions, aiming at improving the average performance for all networks. At the online stage, we continually optimize the meta policy to fast “identify” the unique inp

**[Entrenamiento / optimización | extracto 13 | p.5]**

to the trajectories collected from both the real-world and the virtual player, while the real-world samples often account for a small part of them. IV. A2BR OVERVIEW We propose A2BR (Adaption of Adaptive BitRate), a novel neural ABR system that can quickly adapt the personalized network conditions via meta-RL and domain knowledge. The system workflow is shown in Figure 4. A2BR consists of offline meta stage and online adaptation stage. At the offline stage, we train a meta-model using MAML with various network environments to learn a good parameter initialization for achieving both acceptable “mean” performance and fast adaptation. At the online stage, the agents continually tune the meta-model with the help of domain knowledge for rapidly varying the personalized network condition, i.e., generating a tailor-made ABR algorithm. A. Basic Training Algorithm In this section, we introduce the NN architecture for each model in A2BR. First, we describe the NN’s inputs, outputs, and architecture. Then, we explain the basic training method- ology of A2BR. 1) NN Model Overview: The NN architecture is shown in Figure 5. Here we denote the parameters of the meta actor model as δπ and the meta critic model as δv. What’s more, we refer to the combination of the meta actor model and critic model as the meta actor-critic model. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.

**[Entrenamiento / optimización | extracto 14 | p.5]**

0]. Treating the task as the user’s person- alized network environment, we find that model agnostic meta learning (MAML) [18] is quite suitable in personalized ABR scenarios where the network traces on each user are quite limited. More comparison of existing meta-learning methods is discussed in §VI-A. Specifically, MAML consists of an inner loop and an outer loop. For every cycle of the outer loop update, a specific task will be sampled from a distribution of tasks. and trains the parameter weights that determine the agent’s behavior. In the inner loop, the agent interacts with the sampled environment and optimizes for maximizing the accumulated reward, i.e., QoE (Eq. 1). Let δ denote the parameter weights, inner/outer loop learn- ing rate are represented as α/β, and policy improvement function L, for a distribution of task T , the meta-optimization process can be presented as Eq. 6. δ ←δ −β∇θ  T⟩∼p(T ) LT⟩(fθ −α∇θLT⟩(fθ)) (6) D. Leveraging Domain Knowledge For tackling the second challenge, apart from the gains from MAML, we attempt to adopt the domain principle and knowledge of adaptive video streaming to accelerate the learning efficiency on the online stage. On the one hand, given a complete network trace, recent research has revealed that the ABR process can be precisely emulated by an ABR virtual player [10], [31]. Thus, based on the domain principles of the ABR framework, we implement a faithful ABR simulator to virtual rollout the trajectories, aiming to help improve data effi- ciency and generalization ability. On the other hand, we treat the domain knowledge of state-of-the-art heuristics [8] as the fallback policy which can help identify if the meta policy takes the syst

**[Entrenamiento / optimización | extracto 15 | p.5]**

r fast-learning? ii) How to efficiently learn tailor-made ABR algorithms online? C. Model Agnostic Meta-Learning for the first challenge, we present a method based on meta- learning, which provides an alternative paradigm to improve the learning algorithm itself and gains experience over multiple learning episodes [30]. Treating the task as the user’s person- alized network environment, we find that model agnostic meta learning (MAML) [18] is quite suitable in personalized ABR scenarios where the network traces on each user are quite limited. More comparison of existing meta-learning methods is discussed in §VI-A. Specifically, MAML consists of an inner loop and an outer loop. For every cycle of the outer loop update, a specific task will be sampled from a distribution of tasks. and trains the parameter weights that determine the agent’s behavior. In the inner loop, the agent interacts with the sampled environment and optimizes for maximizing the accumulated reward, i.e., QoE (Eq. 1). Let δ denote the parameter weights, inner/outer loop learn- ing rate are represented as α/β, and policy improvement function L, for a distribution of task T , the meta-optimization process can be presented as Eq. 6. δ ←δ −β∇θ  T⟩∼p(T ) LT⟩(fθ −α∇θLT⟩(fθ)) (6) D. Leveraging Domain Knowledge For tackling the second challenge, apart from the gains from MAML, we attempt to adopt the domain principle and knowledge of adaptive video streaming to accelerate the learning efficiency on the online stage. On the one hand, given a complete network trace, recent research has revealed that the ABR process can be precisely emulated by an ABR virtual player [10], [31]. Thus, based on the domain principles of the A

**[Entrenamiento / optimización | extracto 16 | p.5]**

icy via the traces collected by different network conditions, aiming at improving the average performance for all networks. At the online stage, we continually optimize the meta policy to fast “identify” the unique input process for adapting to the personalized networks. To achieve this, we encounter two new challenges based on the specific features of ABR tasks: i) how to obtain a good parameter initialization for fast-learning? ii) How to efficiently learn tailor-made ABR algorithms online? C. Model Agnostic Meta-Learning for the first challenge, we present a method based on meta- learning, which provides an alternative paradigm to improve the learning algorithm itself and gains experience over multiple learning episodes [30]. Treating the task as the user’s person- alized network environment, we find that model agnostic meta learning (MAML) [18] is quite suitable in personalized ABR scenarios where the network traces on each user are quite limited. More comparison of existing meta-learning methods is discussed in §VI-A. Specifically, MAML consists of an inner loop and an outer loop. For every cycle of the outer loop update, a specific task will be sampled from a distribution of tasks. and trains the parameter weights that determine the agent’s behavior. In the inner loop, the agent interacts with the sampled environment and optimizes for maximizing the accumulated reward, i.e., QoE (Eq. 1). Let δ denote the parameter weights, inner/outer loop learn- ing rate are represented as α/β, and policy improvement function L, for a distribution of task T , the meta-optimization process can be presented as Eq. 6. δ ←δ −β∇θ  T⟩∼p(T ) LT⟩(fθ −α∇θLT⟩(fθ)) (6) D. Leveraging Domain Knowl

### 5.x Datos / trazas / datasets

**[Datos / trazas / datasets | extracto 1 | p.1]**

singhua.edu.cn; wucl18@mails.tsinghua.edu.cn). Lifeng Sun is with the Beijing Key Laboratory of Networked Multimedia, Department of Computer Science and Technology, Tsinghua University, Beijing 100084, China, also with the Beijing National Research Center for Information Science and Technology (BNRist), Department of Computer Science and Technology, Tsinghua University, Beijing 100084, China, and also with the Key Laboratory of Pervasive Computing, Ministry of Education, Tsinghua University, Beijing 100084, China (e-mail: sunlf@tsinghua.edu.cn). Color versions of one or more figures in this article are available at https://doi.org/10.1109/JSAC.2022.3180804. Digital Object Identifier 10.1109/JSAC.2022.3180804 efficiency, we fully utilize domain knowledge for implementing a virtual player to replay the previously experienced network. Using trace-driven experiments on various scenarios including different vehicles, users, network types, and heterogeneous user- preferences, we show that A2BR outperforming recent ABR approaches with rapidly adapting to the personalized QoE metrics and specific network conditions. Testbed experimental results also illustrate the superiority of A2BR in adapting to the unseen environments. Index Terms—Streaming media, reinforcement learning (RL), adaptive control. I. INTRODUCTION D UE to the rapid development of network services, video streaming now stands for the predominant Internet appli- cation, which is up almost 75% all traffic [1], [2]. Espe- cially, adaptive video streaming, such as HLS (HTTP Live Streaming) [3] and DASH [4] has already been the popular form of video delivery [5]. Adaptive bitrate (ABR) algorithms enable Internet adaptive vide

**[Datos / trazas / datasets | extracto 2 | p.1]**

ons. By contrast, learning-based schemes employ several learning technologies, such as reinforcement learning [11], [12], supervised learning [2], [13] and imitation learn- ing [14], [15] to train a neural network (NN) w.r.t the given network traffic distributions, and make a zero-shot inference for unseen networks. In short, existing ABR algorithms, either heuristics or learning-based schemes, seldom configure or tune their parameters automatically and rapidly for varying the current network traffic distribution. However, in the adaptive video streaming scenario, the system dynamics are uncertain and the future state cannot be accurately predicted. To prove this view, we focus on inves- tigating the impact of ABR algorithms on the distribution of heterogeneous network traffics, where the distribution is usu- ally summarized by bandwidth traces experienced by different 0733-8716 © 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.

**[Datos / trazas / datasets | extracto 3 | p.1]**

IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 2485 Learning Tailored Adaptive Bitrate Algorithms to Heterogeneous Network Conditions: A Domain-Specific Priors and Meta-Reinforcement Learning Approach Tianchi Huang , Student Member, IEEE, Chao Zhou, Rui-Xiao Zhang , Student Member, IEEE, Chenglei Wu, and Lifeng Sun , Member, IEEE Abstract—Internet adaptive video streaming is a typical form of video delivery that leverages adaptive bitrate (ABR) algorithms to provide video services with high quality of experience (QoE) for various users in diverse and unique network conditions. Such heterogeneous network environments, which can be viewed as exogenous input processes, often lead to the unstable perfor- mance of ABR algorithms. Unfortunately, learning-based ABR algorithm which generated by state-of-the-art reinforcement learning (RL) technologies achieves good average performance but fails to perform well in all kinds of network conditions. In this work, considering the video playback process as the Input-driven Markov Decision Process (IMDP), we propose A2BR (Adaptation of ABR), a novel meta-RL ABR approach. A2BR is mainly composed of an online stage and an offline stage. It leverages meta-RL to l

**[Datos / trazas / datasets | extracto 4 | p.2]**

2486 IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 users at any time, in any place, and especially, under any network conditions. Through the analysis of the impact on the network distributions of different users, vehicles, and network types, we empirically find that nowadays’ Internet network conditions are not only diverse but also unique (§II-B). For example, the heterogeneity of network conditions for each user is inevitable, since both subjective and objective user behavior have an important impact on the network traffic distribution. Nevertheless, existing ABR algorithms, either heuristics or learning-based, fail to adapt to such heterogeneous bandwidth conditions that are significantly different from the offline training (or tuning) network dataset [16]. Motivated by these facts, we model the ABR playback process as Input-driven Markov Decision Process (IMDP), which can express an implicit heterogeneous network envi- ronment in an explicit manner (§III-A). We theoretically illustrate that vanilla RL technologies can only generalize a strategy that can perform well on average rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel neural meta-RL ABR system that enables fast adaptation to the specific network conditions (§III-B).

**[Datos / trazas / datasets | extracto 5 | p.2]**

ries. For improving the learning efficiency, the trajec- tories are collected not only from the real world but also from the “virtual world.” Specifically, the virtual world is motivated by domain principles and constructed by a faithful virtual player and experienced network environments. In addition, we also employ the domain knowledge that uses heuristics to enable safe online RL. Subsequently, the meta-policy will be continually optimized within 20-shot, i.e., watch 20 videos at the online stage (§IV-C). In the rest of the paper, we conduct several experiments to evaluate A2BR with existing ABR approaches (§V). The case studies contain different types of heterogeneous network conditions and QoE objectives, including differ- ent vehicles, users’ personalized networks, 4G/5G networks, and varying user preferences for QoE metrics. Using trace- driven simulation and real-world evaluation on various videos, we show: Fig. 1. The typical ABR system overview. The ABR algorithm is usually placed on the client-side. 1) A2BR improves the video quality by up to 12.6% while reducing the stall time by 69.3% to 2.8× compared with previously proposed approaches. 2) In the user-personalized network, A2BR outperforms recent heuristics and learning-based ABRs, with improvements on average QoE of 12%-23%; 3) A2BR maintains high bitrates with low video stall in both 4G and 5G networks, whereas the learning-based approach Pensieve diverges. At the same time, A2BR either matches or exceeds the performance of existing schemes on IT-T Rec P.1203 QoE metric [19]. The average QoE is 10% higher than the closest ABR approach Fugu [2]. 4) A2BR with minor modification can hold QoE metrics with different

**[Datos / trazas / datasets | extracto 6 | p.2]**

nually updated to the tailor-made policy with the collected trajectories. For improving the learning efficiency, the trajec- tories are collected not only from the real world but also from the “virtual world.” Specifically, the virtual world is motivated by domain principles and constructed by a faithful virtual player and experienced network environments. In addition, we also employ the domain knowledge that uses heuristics to enable safe online RL. Subsequently, the meta-policy will be continually optimized within 20-shot, i.e., watch 20 videos at the online stage (§IV-C). In the rest of the paper, we conduct several experiments to evaluate A2BR with existing ABR approaches (§V). The case studies contain different types of heterogeneous network conditions and QoE objectives, including differ- ent vehicles, users’ personalized networks, 4G/5G networks, and varying user preferences for QoE metrics. Using trace- driven simulation and real-world evaluation on various videos, we show: Fig. 1. The typical ABR system overview. The ABR algorithm is usually placed on the client-side. 1) A2BR improves the video quality by up to 12.6% while reducing the stall time by 69.3% to 2.8× compared with previously proposed approaches. 2) In the user-personalized network, A2BR outperforms recent heuristics and learning-based ABRs, with improvements on average QoE of 12%-23%; 3) A2BR maintains high bitrates with low video stall in both 4G and 5G networks, whereas the learning-based approach Pensieve diverges. At the same time, A2BR either matches or exceeds the performance of existing schemes on IT-T Rec P.1203 QoE metric [19]. The average QoE is 10% higher than the closest ABR approach Fugu [

**[Datos / trazas / datasets | extracto 7 | p.2]**

lly updated to the tailor-made policy with the collected trajectories. For improving the learning efficiency, the trajec- tories are collected not only from the real world but also from the “virtual world.” Specifically, the virtual world is motivated by domain principles and constructed by a faithful virtual player and experienced network environments. In addition, we also employ the domain knowledge that uses heuristics to enable safe online RL. Subsequently, the meta-policy will be continually optimized within 20-shot, i.e., watch 20 videos at the online stage (§IV-C). In the rest of the paper, we conduct several experiments to evaluate A2BR with existing ABR approaches (§V). The case studies contain different types of heterogeneous network conditions and QoE objectives, including differ- ent vehicles, users’ personalized networks, 4G/5G networks, and varying user preferences for QoE metrics. Using trace- driven simulation and real-world evaluation on various videos, we show: Fig. 1. The typical ABR system overview. The ABR algorithm is usually placed on the client-side. 1) A2BR improves the video quality by up to 12.6% while reducing the stall time by 69.3% to 2.8× compared with previously proposed approaches. 2) In the user-personalized network, A2BR outperforms recent heuristics and learning-based ABRs, with improvements on average QoE of 12%-23%; 3) A2BR maintains high bitrates with low video stall in both 4G and 5G networks, whereas the learning-based approach Pensieve diverges. At the same time, A2BR either matches or exceeds the performance of existing schemes on IT-T Rec P.1203 QoE metric [19]. The average QoE is 10% higher than the closest ABR approach Fugu [2].

**[Datos / trazas / datasets | extracto 8 | p.2]**

ee RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption of Adaptive Bitrate Algorithm), a novel neural meta-RL ABR system that enables fast adaptation to the specific network conditions (§III-B). A2BR is composed of the offline stage and online stage (§IV). At the offline stage, A2BR trains a meta-model with various real and synthetic network conditions for learning parameter initialization meta-policy, where the policy can provide rapid adaptation for varying heterogeneous networks. To achieve this goal, we implement the training process based on the state-of-the-art gradient-free meta-learning technology [18] and utilize maximum entropy RL methodologies to achieve better exploration (§IV-B). Moreover, at the online stage, the video player, placed on the user side, receives the trained meta-model and picks the bitrates w.r.t the meta-policy and the current specific network status. Upon finishing the video session, the meta-policy is continually updated to the tailor-made policy with the collected trajectories. For improving the learning efficiency, the trajec- tories are collected not only from the real world but also from the “virtual world.” Specifically, the virtual world is motivated by domain principles and constructed by a faithful virtual player and experienced network environments. In addition, we also employ the domain knowledge that uses heuristics to enable safe online RL. Subsequently, the meta-policy will be continually optimized within 20-shot, i.e., watch 20 videos at the online stage (§IV-C). In the rest of the paper, we conduct several experiments t

**[Datos / trazas / datasets | extracto 9 | p.3]**

n, in the real world, the average bandwidth is particularly varied, ranging from 0.1 to 100 Mbps. The lower bandwidth leads to larger RTT. The network environment of each user is different. Someone can watch the videos with high bandwidth and low RTT, while the others live in the low bandwidth and high RTT scenario. The right figure plots the fine-grained cumulative distribution function (CDF) of throughput and RTT of the users with top-8 viewing hours on that day. We can find the tailor-made features for personalized network conditions: some of the users have very constant throughput (e.g., user C and user F), while most of the users’ bandwidth is unstable and doesn’t cover all network conditions. 2) Sorted by Scenarios: Next, Figure 2(b) shows another personalized network condition that is categorized by network types, which covers 3G, 4G, and 5G networks. Testing results on the bus, car, and metro environments show that different vehicle speeds lead to very different 3G bandwidth distri- butions. For instance, we can see the throughput measured from the metro achieves the lowest average and fluctuation value among the candidates. While we observe the highest bandwidth with high fluctuation in the 3G-car scenario. Mean- while, in addition to the various network specifics on 4G and 5G, the network distributions are always influenced by user behaviors: the network on walking and driving also have their particularity. Hence, the domain gap, which represents the relationship between network traffic distributions across different network types and users, has brought great challenges to recent rate adaptation algorithms. Authorized licensed use limited to: UNIVERSIDAD DE GRANAD

**[Datos / trazas / datasets | extracto 10 | p.3]**

here Rn represents the each chunk’s video bitrate, Tn reflects the rebuffering time for each chunk n, q(Rn) means the quality metric such as video bitrate [8] and VMAF [22] (state-of-the-art quality assessment), μ and ρ are the weight of rebuffering and smoothness penalty, respectively. QoE = N  n=1 q(Rn) −μ N  n=1 Tn −ρ N−1  n=1 |q(Rn+1) −q(Rn)| (1) B. Different Types of Network Conditions Recently, several learning-based schemes have been made to train an NN policy from the clean slate via various RL methods [11], [23]. Unfortunately, such one-fits-all schemes, including heuristics and learning-based can hardly always perform well in today’s network traffics due to the diversity of real-world network conditions [2]. We show the personalized network environments from two perspectives. TABLE I COMPARISON RESULTS ON DIFFERENT ABRS OVER 3G-CAR AND 3G-BUS NETWORKS, WHERE A2BR IS FINE-TUNED IN 20-SHOT 1) Sorted by Users: First, we measure a portion of data from the Puffer project [2] and demonstrate the users’ personalized network status on June 2, 2021, in Figure 2(a). The left figure illustrates the correlations between throughput and round- trip-time (RTT) of each user. As shown, in the real world, the average bandwidth is particularly varied, ranging from 0.1 to 100 Mbps. The lower bandwidth leads to larger RTT. The network environment of each user is different. Someone can watch the videos with high bandwidth and low RTT, while the others live in the low bandwidth and high RTT scenario. The right figure plots the fine-grained cumulative distribution function (CDF) of throughput and RTT of the users with top-8 viewing hours on that day. We can find the tailor-made featur

**[Datos / trazas / datasets | extracto 11 | p.3]**

e real world, the average bandwidth is particularly varied, ranging from 0.1 to 100 Mbps. The lower bandwidth leads to larger RTT. The network environment of each user is different. Someone can watch the videos with high bandwidth and low RTT, while the others live in the low bandwidth and high RTT scenario. The right figure plots the fine-grained cumulative distribution function (CDF) of throughput and RTT of the users with top-8 viewing hours on that day. We can find the tailor-made features for personalized network conditions: some of the users have very constant throughput (e.g., user C and user F), while most of the users’ bandwidth is unstable and doesn’t cover all network conditions. 2) Sorted by Scenarios: Next, Figure 2(b) shows another personalized network condition that is categorized by network types, which covers 3G, 4G, and 5G networks. Testing results on the bus, car, and metro environments show that different vehicle speeds lead to very different 3G bandwidth distri- butions. For instance, we can see the throughput measured from the metro achieves the lowest average and fluctuation value among the candidates. While we observe the highest bandwidth with high fluctuation in the 3G-car scenario. Mean- while, in addition to the various network specifics on 4G and 5G, the network distributions are always influenced by user behaviors: the network on walking and driving also have their particularity. Hence, the domain gap, which represents the relationship between network traffic distributions across different network types and users, has brought great challenges to recent rate adaptation algorithms. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downl

**[Datos / trazas / datasets | extracto 12 | p.3]**

HUANG et al.: LEARNING TAILORED ABR ALGORITHMS TO HETEROGENEOUS NETWORK CONDITIONS 2487 Fig. 2. Visualizing personalized networks from the real-world [2], [20], [21]. The video player client decodes and renders video frames from the playback buffer. Once the streaming service starts, the client fetches the video chunk from the HTTP Server or CDN orderly by an ABR algorithm. The ABR algorithm, implemented on the client-side, determines the next chunk and next chunk video quality via throughput estimation and current buffer utilization. After finishing the session, several metrics, such as total bitrate, total re-buffering time, and total bitrate change will be summarized as a QoE metric to evaluate the performance. Thus, how to achieve high QoE scores for adaptive video streaming has become a major challenge for ABR algorithms. Existing ABR algorithms are generally composed of heuris- tics and learning-based. Heuristics make decisions from fea- tures with domain knowledge, e.g., throughput measured [13], buffer

**[Datos / trazas / datasets | extracto 13 | p.4]**

lgorithms (§V-A4) over different mobility types (car and bus) [20]. We show that the irregular networks greatly disturb the stability of the learning-based algorithm, since the difference between the network traffic distributions of the training set and the testing set. Moreover, heuristics like BOLA and RobustMPC (RMPC here) often perform well in one scenario but fail in the other, e.g., BOLA gains a low average bitrate and RobustMPC performs with a high stall ratio. Results indicate that the domain gap among het- erogeneous network scenarios (e.g. Figure 2(b)) leads to the unstable performance of both heuristics and learning-based approaches [16], [24]. One of the feasible ways is to enable the policy to quickly adapt to the current network condition with few trials. As shown, our proposed method A2BR outperforms existing techniques on video bitrate and stall ratio after being trained in 20-shot. In summary, we argue that off-the-shelf “one-fits-all” ABR algorithms fail to provide acceptable performances for all users since the diversity of users’ network conditions. III. METHODS In this section, we start with modeling the tailored ABR process as an Input-driven Markov Decision Process (IMDP). Next, we explain why we have to construct a two-stage process rather than a vanilla one-stage approach. Finally, we briefly introduce meta-agnostic meta-learning and how to leverage domain knowledge. A. Input-Driven MDP Motivated by the observation above, we place the ABR problem in the discrete-time input-driven Markov decision process (MDP) [25], [26]. In detail, we consider the vanilla adaptive video streaming process: at each step t, the video client, often namely agent in RL frame

**[Datos / trazas / datasets | extracto 14 | p.5]**

R mainly consists of two stages, the offline stage and the online stage. B. Meta-RL With Domain Knowledge With the rapid progress of on-device machine learning in both academia [28] and industry [29], training NNs on users’ devices has already been a practical way of learning the tailor-made ABR policy from a clean slate in situ. Neverthe- less, recent model-free RL technologies lack sample efficiency, which requires high convergence time on each client [2]. For example, a single agent requires at least 640,000 steps, spanning over 2 years, to converge in the real world. Most users would leave the platform before the algorithm has been completely trained [11]. In this paper, we consider a two-stage approach, which is composed of offline stage and online stage. Technically, at the offline stage, we attempt to train the meta policy via the traces collected by different network conditions, aiming at improving the average performance for all networks. At the online stage, we continually optimize the meta policy to fast “identify” the unique input process for adapting to the personalized networks. To achieve this, we encounter two new challenges based on the specific features of ABR tasks: i) how to obtain a good parameter initialization for fast-learning? ii) How to efficiently learn tailor-made ABR algorithms online? C. Model Agnostic Meta-Learning for the first challenge, we present a method based on meta- learning, which provides an alternative paradigm to improve the learning algorithm itself and gains experience over multiple learning episodes [30]. Treating the task as the user’s person- alized network environment, we find that model agnostic meta learning (MAML) [18] is qui

**[Datos / trazas / datasets | extracto 15 | p.5]**

ving the average performance for all networks. At the online stage, we continually optimize the meta policy to fast “identify” the unique input process for adapting to the personalized networks. To achieve this, we encounter two new challenges based on the specific features of ABR tasks: i) how to obtain a good parameter initialization for fast-learning? ii) How to efficiently learn tailor-made ABR algorithms online? C. Model Agnostic Meta-Learning for the first challenge, we present a method based on meta- learning, which provides an alternative paradigm to improve the learning algorithm itself and gains experience over multiple learning episodes [30]. Treating the task as the user’s person- alized network environment, we find that model agnostic meta learning (MAML) [18] is quite suitable in personalized ABR scenarios where the network traces on each user are quite limited. More comparison of existing meta-learning methods is discussed in §VI-A. Specifically, MAML consists of an inner loop and an outer loop. For every cycle of the outer loop update, a specific task will be sampled from a distribution of tasks. and trains the parameter weights that determine the agent’s behavior. In the inner loop, the agent interacts with the sampled environment and optimizes for maximizing the accumulated reward, i.e., QoE (Eq. 1). Let δ denote the parameter weights, inner/outer loop learn- ing rate are represented as α/β, and policy improvement function L, for a distribution of task T , the meta-optimization process can be presented as Eq. 6. δ ←δ −β∇θ  T⟩∼p(T ) LT⟩(fθ −α∇θLT⟩(fθ)) (6) D. Leveraging Domain Knowledge For tackling the second challenge, apart from the gains from MAML, we atte

**[Datos / trazas / datasets | extracto 16 | p.5]**

atform before the algorithm has been completely trained [11]. In this paper, we consider a two-stage approach, which is composed of offline stage and online stage. Technically, at the offline stage, we attempt to train the meta policy via the traces collected by different network conditions, aiming at improving the average performance for all networks. At the online stage, we continually optimize the meta policy to fast “identify” the unique input process for adapting to the personalized networks. To achieve this, we encounter two new challenges based on the specific features of ABR tasks: i) how to obtain a good parameter initialization for fast-learning? ii) How to efficiently learn tailor-made ABR algorithms online? C. Model Agnostic Meta-Learning for the first challenge, we present a method based on meta- learning, which provides an alternative paradigm to improve the learning algorithm itself and gains experience over multiple learning episodes [30]. Treating the task as the user’s person- alized network environment, we find that model agnostic meta learning (MAML) [18] is quite suitable in personalized ABR scenarios where the network traces on each user are quite limited. More comparison of existing meta-learning methods is discussed in §VI-A. Specifically, MAML consists of an inner loop and an outer loop. For every cycle of the outer loop update, a specific task will be sampled from a distribution of tasks. and trains the parameter weights that determine the agent’s behavior. In the inner loop, the agent interacts with the sampled environment and optimizes for maximizing the accumulated reward, i.e., QoE (Eq. 1). Let δ denote the parameter weights, inner/outer loop le

### 5.x Evaluación / baselines / experimentos

**[Evaluación / baselines / experimentos | extracto 1 | p.1]**

n; wucl18@mails.tsinghua.edu.cn). Lifeng Sun is with the Beijing Key Laboratory of Networked Multimedia, Department of Computer Science and Technology, Tsinghua University, Beijing 100084, China, also with the Beijing National Research Center for Information Science and Technology (BNRist), Department of Computer Science and Technology, Tsinghua University, Beijing 100084, China, and also with the Key Laboratory of Pervasive Computing, Ministry of Education, Tsinghua University, Beijing 100084, China (e-mail: sunlf@tsinghua.edu.cn). Color versions of one or more figures in this article are available at https://doi.org/10.1109/JSAC.2022.3180804. Digital Object Identifier 10.1109/JSAC.2022.3180804 efficiency, we fully utilize domain knowledge for implementing a virtual player to replay the previously experienced network. Using trace-driven experiments on various scenarios including different vehicles, users, network types, and heterogeneous user- preferences, we show that A2BR outperforming recent ABR approaches with rapidly adapting to the personalized QoE metrics and specific network conditions. Testbed experimental results also illustrate the superiority of A2BR in adapting to the unseen environments. Index Terms—Streaming media, reinforcement learning (RL), adaptive control. I. INTRODUCTION D UE to the rapid development of network services, video streaming now stands for the predominant Internet appli- cation, which is up almost 75% all traffic [1], [2]. Espe- cially, adaptive video streaming, such as HLS (HTTP Live Streaming) [3] and DASH [4] has already been the popular form of video delivery [5]. Adaptive bitrate (ABR) algorithms enable Internet adaptive video streaming servic

**[Evaluación / baselines / experimentos | extracto 2 | p.1]**

NRist), Department of Computer Science and Technology, Tsinghua University, Beijing 100084, China, and also with the Key Laboratory of Pervasive Computing, Ministry of Education, Tsinghua University, Beijing 100084, China (e-mail: sunlf@tsinghua.edu.cn). Color versions of one or more figures in this article are available at https://doi.org/10.1109/JSAC.2022.3180804. Digital Object Identifier 10.1109/JSAC.2022.3180804 efficiency, we fully utilize domain knowledge for implementing a virtual player to replay the previously experienced network. Using trace-driven experiments on various scenarios including different vehicles, users, network types, and heterogeneous user- preferences, we show that A2BR outperforming recent ABR approaches with rapidly adapting to the personalized QoE metrics and specific network conditions. Testbed experimental results also illustrate the superiority of A2BR in adapting to the unseen environments. Index Terms—Streaming media, reinforcement learning (RL), adaptive control. I. INTRODUCTION D UE to the rapid development of network services, video streaming now stands for the predominant Internet appli- cation, which is up almost 75% all traffic [1], [2]. Espe- cially, adaptive video streaming, such as HLS (HTTP Live Streaming) [3] and DASH [4] has already been the popular form of video delivery [5]. Adaptive bitrate (ABR) algorithms enable Internet adaptive video streaming services to achieve high video quality while avoiding uninterrupted stall event [5] (§II-A). Revisiting the recent success of ABR algorithms, heuristics often make decisions based on network or player sta- tus [6]–[8]. However, those schemes require a proper setting of configuration pa

**[Evaluación / baselines / experimentos | extracto 3 | p.1]**

NO. 8, AUGUST 2022 2485 Learning Tailored Adaptive Bitrate Algorithms to Heterogeneous Network Conditions: A Domain-Specific Priors and Meta-Reinforcement Learning Approach Tianchi Huang , Student Member, IEEE, Chao Zhou, Rui-Xiao Zhang , Student Member, IEEE, Chenglei Wu, and Lifeng Sun , Member, IEEE Abstract—Internet adaptive video streaming is a typical form of video delivery that leverages adaptive bitrate (ABR) algorithms to provide video services with high quality of experience (QoE) for various users in diverse and unique network conditions. Such heterogeneous network environments, which can be viewed as exogenous input processes, often lead to the unstable perfor- mance of ABR algorithms. Unfortunately, learning-based ABR algorithm which generated by state-of-the-art reinforcement learning (RL) technologies achieves good average performance but fails to perform well in all kinds of network conditions. In this work, considering the video playback process as the Input-driven Markov Decision Process (IMDP), we propose A2BR (Adaptation of ABR), a novel meta-RL ABR approach. A2BR is mainly composed of an online stage and an offline stage. It leverages meta-RL to learn an initial meta-policy with various network conditions at the offline stage and makes decisions in personalized network conditions at the online stage. At the same time, we continually optimize the meta-policy to the tailor- made ABR policy for varying the current network environment within few shots. Moreover, in order to improve the learning Manuscript received 15 December 2021; revised 15 March 2022; accepted 23 April 2022. Date of publication 15 June 2022; date of current version 18 July 2022. This work was sup

**[Evaluación / baselines / experimentos | extracto 4 | p.1]**

singhua.edu.cn; wucl18@mails.tsinghua.edu.cn). Lifeng Sun is with the Beijing Key Laboratory of Networked Multimedia, Department of Computer Science and Technology, Tsinghua University, Beijing 100084, China, also with the Beijing National Research Center for Information Science and Technology (BNRist), Department of Computer Science and Technology, Tsinghua University, Beijing 100084, China, and also with the Key Laboratory of Pervasive Computing, Ministry of Education, Tsinghua University, Beijing 100084, China (e-mail: sunlf@tsinghua.edu.cn). Color versions of one or more figures in this article are available at https://doi.org/10.1109/JSAC.2022.3180804. Digital Object Identifier 10.1109/JSAC.2022.3180804 efficiency, we fully utilize domain knowledge for implementing a virtual player to replay the previously experienced network. Using trace-driven experiments on various scenarios including different vehicles, users, network types, and heterogeneous user- preferences, we show that A2BR outperforming recent ABR approaches with rapidly adapting to the personalized QoE metrics and specific network conditions. Testbed experimental results also illustrate the superiority of A2BR in adapting to the unseen environments. Index Terms—Streaming media, reinforcement learning (RL), adaptive control. I. INTRODUCTION D UE to the rapid development of network services, video streaming now stands for the predominant Internet appli- cation, which is up almost 75% all traffic [1], [2]. Espe- cially, adaptive video streaming, such as HLS (HTTP Live Streaming) [3] and DASH [4] has already been the popular form of video delivery [5]. Adaptive bitrate (ABR) algorithms enable Internet adaptive video strea

**[Evaluación / baselines / experimentos | extracto 5 | p.2]**

ncy, the trajec- tories are collected not only from the real world but also from the “virtual world.” Specifically, the virtual world is motivated by domain principles and constructed by a faithful virtual player and experienced network environments. In addition, we also employ the domain knowledge that uses heuristics to enable safe online RL. Subsequently, the meta-policy will be continually optimized within 20-shot, i.e., watch 20 videos at the online stage (§IV-C). In the rest of the paper, we conduct several experiments to evaluate A2BR with existing ABR approaches (§V). The case studies contain different types of heterogeneous network conditions and QoE objectives, including differ- ent vehicles, users’ personalized networks, 4G/5G networks, and varying user preferences for QoE metrics. Using trace- driven simulation and real-world evaluation on various videos, we show: Fig. 1. The typical ABR system overview. The ABR algorithm is usually placed on the client-side. 1) A2BR improves the video quality by up to 12.6% while reducing the stall time by 69.3% to 2.8× compared with previously proposed approaches. 2) In the user-personalized network, A2BR outperforms recent heuristics and learning-based ABRs, with improvements on average QoE of 12%-23%; 3) A2BR maintains high bitrates with low video stall in both 4G and 5G networks, whereas the learning-based approach Pensieve diverges. At the same time, A2BR either matches or exceeds the performance of existing schemes on IT-T Rec P.1203 QoE metric [19]. The average QoE is 10% higher than the closest ABR approach Fugu [2]. 4) A2BR with minor modification can hold QoE metrics with different user preferences, further providing 5% impro

**[Evaluación / baselines / experimentos | extracto 6 | p.2]**

ge, the video player, placed on the user side, receives the trained meta-model and picks the bitrates w.r.t the meta-policy and the current specific network status. Upon finishing the video session, the meta-policy is continually updated to the tailor-made policy with the collected trajectories. For improving the learning efficiency, the trajec- tories are collected not only from the real world but also from the “virtual world.” Specifically, the virtual world is motivated by domain principles and constructed by a faithful virtual player and experienced network environments. In addition, we also employ the domain knowledge that uses heuristics to enable safe online RL. Subsequently, the meta-policy will be continually optimized within 20-shot, i.e., watch 20 videos at the online stage (§IV-C). In the rest of the paper, we conduct several experiments to evaluate A2BR with existing ABR approaches (§V). The case studies contain different types of heterogeneous network conditions and QoE objectives, including differ- ent vehicles, users’ personalized networks, 4G/5G networks, and varying user preferences for QoE metrics. Using trace- driven simulation and real-world evaluation on various videos, we show: Fig. 1. The typical ABR system overview. The ABR algorithm is usually placed on the client-side. 1) A2BR improves the video quality by up to 12.6% while reducing the stall time by 69.3% to 2.8× compared with previously proposed approaches. 2) In the user-personalized network, A2BR outperforms recent heuristics and learning-based ABRs, with improvements on average QoE of 12%-23%; 3) A2BR maintains high bitrates with low video stall in both 4G and 5G networks, whereas the learning-based

**[Evaluación / baselines / experimentos | extracto 7 | p.2]**

ork environments. In addition, we also employ the domain knowledge that uses heuristics to enable safe online RL. Subsequently, the meta-policy will be continually optimized within 20-shot, i.e., watch 20 videos at the online stage (§IV-C). In the rest of the paper, we conduct several experiments to evaluate A2BR with existing ABR approaches (§V). The case studies contain different types of heterogeneous network conditions and QoE objectives, including differ- ent vehicles, users’ personalized networks, 4G/5G networks, and varying user preferences for QoE metrics. Using trace- driven simulation and real-world evaluation on various videos, we show: Fig. 1. The typical ABR system overview. The ABR algorithm is usually placed on the client-side. 1) A2BR improves the video quality by up to 12.6% while reducing the stall time by 69.3% to 2.8× compared with previously proposed approaches. 2) In the user-personalized network, A2BR outperforms recent heuristics and learning-based ABRs, with improvements on average QoE of 12%-23%; 3) A2BR maintains high bitrates with low video stall in both 4G and 5G networks, whereas the learning-based approach Pensieve diverges. At the same time, A2BR either matches or exceeds the performance of existing schemes on IT-T Rec P.1203 QoE metric [19]. The average QoE is 10% higher than the closest ABR approach Fugu [2]. 4) A2BR with minor modification can hold QoE metrics with different user preferences, further providing 5% improve- ments on QoE at the online stage. 5) We prove that A2BR still performs well on both emulation and real-world testbed. Ablution studies show that the online stage further improves the average QoE by 6% after learning in specifi

**[Evaluación / baselines / experimentos | extracto 8 | p.2]**

e of existing schemes on IT-T Rec P.1203 QoE metric [19]. The average QoE is 10% higher than the closest ABR approach Fugu [2]. 4) A2BR with minor modification can hold QoE metrics with different user preferences, further providing 5% improve- ments on QoE at the online stage. 5) We prove that A2BR still performs well on both emulation and real-world testbed. Ablution studies show that the online stage further improves the average QoE by 6% after learning in specific network conditions within 10-shot, and 8% after 50-shot. The contributions of this work are summarized as follows: • We empirically analyze today’s heterogeneous network traf- fics and propose a two-stage meta-learning scheme for varying specific network conditions. • We implement A2BR, which is the first meta-learning with domain knowledge approach for adaptive streaming. • Results on different types of network conditions illustrate that the generated tailor-made ABR policies can well adapt to heterogeneous networks with relatively few-shot. II. BACKGROUND AND MOTIVATION Our research is started with a fundamental quest: How will the recent ABRs perform in various network traffic environ- ments?. To answer this question, first, we briefly introduce the key principle of adaptive video streaming and adaptive bitrate (ABR) algorithms. We then use empirical measure- ments to elucidate the key limitations of prior solutions. A. Adaptive Video Streaming The adaptive bitrate method (ABR) is an algorithm that dynamically selects video bitrates via network conditions and the client’s buffer occupancy. The traditional video stream- ing architecture is shown in Figure 1. The system consists of a video player client with a con

**[Evaluación / baselines / experimentos | extracto 9 | p.2]**

fferent types of heterogeneous network conditions and QoE objectives, including differ- ent vehicles, users’ personalized networks, 4G/5G networks, and varying user preferences for QoE metrics. Using trace- driven simulation and real-world evaluation on various videos, we show: Fig. 1. The typical ABR system overview. The ABR algorithm is usually placed on the client-side. 1) A2BR improves the video quality by up to 12.6% while reducing the stall time by 69.3% to 2.8× compared with previously proposed approaches. 2) In the user-personalized network, A2BR outperforms recent heuristics and learning-based ABRs, with improvements on average QoE of 12%-23%; 3) A2BR maintains high bitrates with low video stall in both 4G and 5G networks, whereas the learning-based approach Pensieve diverges. At the same time, A2BR either matches or exceeds the performance of existing schemes on IT-T Rec P.1203 QoE metric [19]. The average QoE is 10% higher than the closest ABR approach Fugu [2]. 4) A2BR with minor modification can hold QoE metrics with different user preferences, further providing 5% improve- ments on QoE at the online stage. 5) We prove that A2BR still performs well on both emulation and real-world testbed. Ablution studies show that the online stage further improves the average QoE by 6% after learning in specific network conditions within 10-shot, and 8% after 50-shot. The contributions of this work are summarized as follows: • We empirically analyze today’s heterogeneous network traf- fics and propose a two-stage meta-learning scheme for varying specific network conditions. • We implement A2BR, which is the first meta-learning with domain knowledge approach for adaptive streaming. • R

**[Evaluación / baselines / experimentos | extracto 10 | p.2]**

is usually placed on the client-side. 1) A2BR improves the video quality by up to 12.6% while reducing the stall time by 69.3% to 2.8× compared with previously proposed approaches. 2) In the user-personalized network, A2BR outperforms recent heuristics and learning-based ABRs, with improvements on average QoE of 12%-23%; 3) A2BR maintains high bitrates with low video stall in both 4G and 5G networks, whereas the learning-based approach Pensieve diverges. At the same time, A2BR either matches or exceeds the performance of existing schemes on IT-T Rec P.1203 QoE metric [19]. The average QoE is 10% higher than the closest ABR approach Fugu [2]. 4) A2BR with minor modification can hold QoE metrics with different user preferences, further providing 5% improve- ments on QoE at the online stage. 5) We prove that A2BR still performs well on both emulation and real-world testbed. Ablution studies show that the online stage further improves the average QoE by 6% after learning in specific network conditions within 10-shot, and 8% after 50-shot. The contributions of this work are summarized as follows: • We empirically analyze today’s heterogeneous network traf- fics and propose a two-stage meta-learning scheme for varying specific network conditions. • We implement A2BR, which is the first meta-learning with domain knowledge approach for adaptive streaming. • Results on different types of network conditions illustrate that the generated tailor-made ABR policies can well adapt to heterogeneous networks with relatively few-shot. II. BACKGROUND AND MOTIVATION Our research is started with a fundamental quest: How will the recent ABRs perform in various network traffic environ- ments?. To answer

**[Evaluación / baselines / experimentos | extracto 11 | p.2]**

fline stage, A2BR trains a meta-model with various real and synthetic network conditions for learning parameter initialization meta-policy, where the policy can provide rapid adaptation for varying heterogeneous networks. To achieve this goal, we implement the training process based on the state-of-the-art gradient-free meta-learning technology [18] and utilize maximum entropy RL methodologies to achieve better exploration (§IV-B). Moreover, at the online stage, the video player, placed on the user side, receives the trained meta-model and picks the bitrates w.r.t the meta-policy and the current specific network status. Upon finishing the video session, the meta-policy is continually updated to the tailor-made policy with the collected trajectories. For improving the learning efficiency, the trajec- tories are collected not only from the real world but also from the “virtual world.” Specifically, the virtual world is motivated by domain principles and constructed by a faithful virtual player and experienced network environments. In addition, we also employ the domain knowledge that uses heuristics to enable safe online RL. Subsequently, the meta-policy will be continually optimized within 20-shot, i.e., watch 20 videos at the online stage (§IV-C). In the rest of the paper, we conduct several experiments to evaluate A2BR with existing ABR approaches (§V). The case studies contain different types of heterogeneous network conditions and QoE objectives, including differ- ent vehicles, users’ personalized networks, 4G/5G networks, and varying user preferences for QoE metrics. Using trace- driven simulation and real-world evaluation on various videos, we show: Fig. 1. The typical ABR sys

**[Evaluación / baselines / experimentos | extracto 12 | p.2]**

uate A2BR with existing ABR approaches (§V). The case studies contain different types of heterogeneous network conditions and QoE objectives, including differ- ent vehicles, users’ personalized networks, 4G/5G networks, and varying user preferences for QoE metrics. Using trace- driven simulation and real-world evaluation on various videos, we show: Fig. 1. The typical ABR system overview. The ABR algorithm is usually placed on the client-side. 1) A2BR improves the video quality by up to 12.6% while reducing the stall time by 69.3% to 2.8× compared with previously proposed approaches. 2) In the user-personalized network, A2BR outperforms recent heuristics and learning-based ABRs, with improvements on average QoE of 12%-23%; 3) A2BR maintains high bitrates with low video stall in both 4G and 5G networks, whereas the learning-based approach Pensieve diverges. At the same time, A2BR either matches or exceeds the performance of existing schemes on IT-T Rec P.1203 QoE metric [19]. The average QoE is 10% higher than the closest ABR approach Fugu [2]. 4) A2BR with minor modification can hold QoE metrics with different user preferences, further providing 5% improve- ments on QoE at the online stage. 5) We prove that A2BR still performs well on both emulation and real-world testbed. Ablution studies show that the online stage further improves the average QoE by 6% after learning in specific network conditions within 10-shot, and 8% after 50-shot. The contributions of this work are summarized as follows: • We empirically analyze today’s heterogeneous network traf- fics and propose a two-stage meta-learning scheme for varying specific network conditions. • We implement A2BR, which is the fir

**[Evaluación / baselines / experimentos | extracto 13 | p.3]**

unction is defined as Eq. 1 ([8], [11]), where Rn represents the each chunk’s video bitrate, Tn reflects the rebuffering time for each chunk n, q(Rn) means the quality metric such as video bitrate [8] and VMAF [22] (state-of-the-art quality assessment), μ and ρ are the weight of rebuffering and smoothness penalty, respectively. QoE = N  n=1 q(Rn) −μ N  n=1 Tn −ρ N−1  n=1 |q(Rn+1) −q(Rn)| (1) B. Different Types of Network Conditions Recently, several learning-based schemes have been made to train an NN policy from the clean slate via various RL methods [11], [23]. Unfortunately, such one-fits-all schemes, including heuristics and learning-based can hardly always perform well in today’s network traffics due to the diversity of real-world network conditions [2]. We show the personalized network environments from two perspectives. TABLE I COMPARISON RESULTS ON DIFFERENT ABRS OVER 3G-CAR AND 3G-BUS NETWORKS, WHERE A2BR IS FINE-TUNED IN 20-SHOT 1) Sorted by Users: First, we measure a portion of data from the Puffer project [2] and demonstrate the users’ personalized network status on June 2, 2021, in Figure 2(a). The left figure illustrates the correlations between throughput and round- trip-time (RTT) of each user. As shown, in the real world, the average bandwidth is particularly varied, ranging from 0.1 to 100 Mbps. The lower bandwidth leads to larger RTT. The network environment of each user is different. Someone can watch the videos with high bandwidth and low RTT, while the others live in the low bandwidth and high RTT scenario. The right figure plots the fine-grained cumulative distribution function (CDF) of throughput and RTT of the users with top-8 viewing hours on that day.

**[Evaluación / baselines / experimentos | extracto 14 | p.3]**

defined as Eq. 1 ([8], [11]), where Rn represents the each chunk’s video bitrate, Tn reflects the rebuffering time for each chunk n, q(Rn) means the quality metric such as video bitrate [8] and VMAF [22] (state-of-the-art quality assessment), μ and ρ are the weight of rebuffering and smoothness penalty, respectively. QoE = N  n=1 q(Rn) −μ N  n=1 Tn −ρ N−1  n=1 |q(Rn+1) −q(Rn)| (1) B. Different Types of Network Conditions Recently, several learning-based schemes have been made to train an NN policy from the clean slate via various RL methods [11], [23]. Unfortunately, such one-fits-all schemes, including heuristics and learning-based can hardly always perform well in today’s network traffics due to the diversity of real-world network conditions [2]. We show the personalized network environments from two perspectives. TABLE I COMPARISON RESULTS ON DIFFERENT ABRS OVER 3G-CAR AND 3G-BUS NETWORKS, WHERE A2BR IS FINE-TUNED IN 20-SHOT 1) Sorted by Users: First, we measure a portion of data from the Puffer project [2] and demonstrate the users’ personalized network status on June 2, 2021, in Figure 2(a). The left figure illustrates the correlations between throughput and round- trip-time (RTT) of each user. As shown, in the real world, the average bandwidth is particularly varied, ranging from 0.1 to 100 Mbps. The lower bandwidth leads to larger RTT. The network environment of each user is different. Someone can watch the videos with high bandwidth and low RTT, while the others live in the low bandwidth and high RTT scenario. The right figure plots the fine-grained cumulative distribution function (CDF) of throughput and RTT of the users with top-8 viewing hours on that day. We can

**[Evaluación / baselines / experimentos | extracto 15 | p.3]**

HUANG et al.: LEARNING TAILORED ABR ALGORITHMS TO HETEROGENEOUS NETWORK CONDITIONS 2487 Fig. 2. Visualizing personalized networks from the real-world [2], [20], [21]. The video player client decodes and renders video frames from the playback buffer. Once the streaming service starts, the client fetches the video chunk from the HTTP Server or CDN orderly by an ABR algorithm. The ABR algorithm, implemented on the client-side, determines the next chunk and next chunk video quality via throughput estimation and current buffer utilization. After finishing the session, several metrics, such as total bitrate, total re-buffering time, and total bitrate change will be summarized as a QoE metric to evaluate the performance. Thus, how to achieve high QoE scores for adaptive video streaming has become a major challenge for ABR algorithms. Existing ABR algorithms are generally composed of heuris- tics and learning-based. Heuristics make decisions from fea- tures with domain knowledge, e.g., throughput measured [13], buffer occupancy [7] or predefined models [8]. By con- trast, learning-based ABRs model the process as the Markov decision process (MDP): at each step t, the video client, often namely agent in RL framework, take a proper action at (i.e., select a proper bitrate) w.r.t current system status st. The agent then downloads the chunk and computes a reward rt for measuring the current quality-of-experience (QoE) of the past action. The process will terminate if the agent finishes playing the video session. In the end, we aim to generalize a policy π to

**[Evaluación / baselines / experimentos | extracto 16 | p.3]**

end, we aim to generalize a policy π to maximize the QoE of the entire session. The accumulated QoE objective function is defined as Eq. 1 ([8], [11]), where Rn represents the each chunk’s video bitrate, Tn reflects the rebuffering time for each chunk n, q(Rn) means the quality metric such as video bitrate [8] and VMAF [22] (state-of-the-art quality assessment), μ and ρ are the weight of rebuffering and smoothness penalty, respectively. QoE = N  n=1 q(Rn) −μ N  n=1 Tn −ρ N−1  n=1 |q(Rn+1) −q(Rn)| (1) B. Different Types of Network Conditions Recently, several learning-based schemes have been made to train an NN policy from the clean slate via various RL methods [11], [23]. Unfortunately, such one-fits-all schemes, including heuristics and learning-based can hardly always perform well in today’s network traffics due to the diversity of real-world network conditions [2]. We show the personalized network environments from two perspectives. TABLE I COMPARISON RESULTS ON DIFFERENT ABRS OVER 3G-CAR AND 3G-BUS NETWORKS, WHERE A2BR IS FINE-TUNED IN 20-SHOT 1) Sorted by Users: First, we measure a portion of data from the Puffer project [2] and demonstrate the users’ personalized network status on June 2, 2021, in Figure 2(a). The left figure illustrates the correlations between throughput and round- trip-time (RTT) of each user. As shown, in the real world, the average bandwidth is particularly varied, ranging from 0.1 to 100 Mbps. The lower bandwidth leads to larger RTT. The network environment of each user is different. Someone can watch the videos with high bandwidth and low RTT, while the others live in the low bandwidth and high RTT scenario. The right figure plots the fine-grained

### 5.x Limitaciones / riesgos / implementación

**[Limitaciones / riesgos / implementación | extracto 1 | p.1]**

cially, adaptive video streaming, such as HLS (HTTP Live Streaming) [3] and DASH [4] has already been the popular form of video delivery [5]. Adaptive bitrate (ABR) algorithms enable Internet adaptive video streaming services to achieve high video quality while avoiding uninterrupted stall event [5] (§II-A). Revisiting the recent success of ABR algorithms, heuristics often make decisions based on network or player sta- tus [6]–[8]. However, those schemes require a proper setting of configuration parameters [9], [10] for fitting different network distributions. By contrast, learning-based schemes employ several learning technologies, such as reinforcement learning [11], [12], supervised learning [2], [13] and imitation learn- ing [14], [15] to train a neural network (NN) w.r.t the given network traffic distributions, and make a zero-shot inference for unseen networks. In short, existing ABR algorithms, either heuristics or learning-based schemes, seldom configure or tune their parameters automatically and rapidly for varying the current network traffic distribution. However, in the adaptive video streaming scenario, the system dynamics are uncertain and the future state cannot be accurately predicted. To prove this view, we focus on inves- tigating the impact of ABR algorithms on the distribution of heterogeneous network traffics, where the distribution is usu- ally summarized by bandwidth traces experienced by different 0733-8716 © 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May

**[Limitaciones / riesgos / implementación | extracto 2 | p.1]**

22 2485 Learning Tailored Adaptive Bitrate Algorithms to Heterogeneous Network Conditions: A Domain-Specific Priors and Meta-Reinforcement Learning Approach Tianchi Huang , Student Member, IEEE, Chao Zhou, Rui-Xiao Zhang , Student Member, IEEE, Chenglei Wu, and Lifeng Sun , Member, IEEE Abstract—Internet adaptive video streaming is a typical form of video delivery that leverages adaptive bitrate (ABR) algorithms to provide video services with high quality of experience (QoE) for various users in diverse and unique network conditions. Such heterogeneous network environments, which can be viewed as exogenous input processes, often lead to the unstable perfor- mance of ABR algorithms. Unfortunately, learning-based ABR algorithm which generated by state-of-the-art reinforcement learning (RL) technologies achieves good average performance but fails to perform well in all kinds of network conditions. In this work, considering the video playback process as the Input-driven Markov Decision Process (IMDP), we propose A2BR (Adaptation of ABR), a novel meta-RL ABR approach. A2BR is mainly composed of an online stage and an offline stage. It leverages meta-RL to learn an initial meta-policy with various network conditions at the offline stage and makes decisions in personalized network conditions at the online stage. At the same time, we continually optimize the meta-policy to the tailor- made ABR policy for varying the current network environment within few shots. Moreover, in order to improve the learning Manuscript received 15 December 2021; revised 15 March 2022; accepted 23 April 2022. Date of publication 15 June 2022; date of current version 18 July 2022. This work was supported in

**[Limitaciones / riesgos / implementación | extracto 3 | p.2]**

hot. The contributions of this work are summarized as follows: • We empirically analyze today’s heterogeneous network traf- fics and propose a two-stage meta-learning scheme for varying specific network conditions. • We implement A2BR, which is the first meta-learning with domain knowledge approach for adaptive streaming. • Results on different types of network conditions illustrate that the generated tailor-made ABR policies can well adapt to heterogeneous networks with relatively few-shot. II. BACKGROUND AND MOTIVATION Our research is started with a fundamental quest: How will the recent ABRs perform in various network traffic environ- ments?. To answer this question, first, we briefly introduce the key principle of adaptive video streaming and adaptive bitrate (ABR) algorithms. We then use empirical measure- ments to elucidate the key limitations of prior solutions. A. Adaptive Video Streaming The adaptive bitrate method (ABR) is an algorithm that dynamically selects video bitrates via network conditions and the client’s buffer occupancy. The traditional video stream- ing architecture is shown in Figure 1. The system consists of a video player client with a constrained buffer length and an HTTP-Server or Content Delivery Network (CDN). Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.

**[Limitaciones / riesgos / implementación | extracto 4 | p.2]**

2486 IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 users at any time, in any place, and especially, under any network conditions. Through the analysis of the impact on the network distributions of different users, vehicles, and network types, we empirically find that nowadays’ Internet network conditions are not only diverse but also unique (§II-B). For example, the heterogeneity of network conditions for each user is inevitable, since both subjective and objective user behavior have an important impact on the network traffic distribution. Nevertheless, existing ABR algorithms, either heuristics or learning-based, fail to adapt to such heterogeneous bandwidth conditions that are significantly different from the offline training (or tuning) network dataset [16]. Motivated by these facts, we model the ABR playback process as Input-driven Markov Decision Process (IMDP), which can express an implicit heterogeneous network envi- ronment in an explicit manner (§III-A). We theoretically illustrate that vanilla RL technologies can only generalize a strategy that can perform well on average rather than every network condition. While through in-depth analysis, we find that the most intuitive solution, i.e., reinforced tailored policies in situ [2], is also impractical since off- the-shelf model-free RL methods [17] heavily lack sample efficiency, which cannot train a policy within an acceptable time. Hence, based on the theory of IMDP, we propose A2BR (Adaption

**[Limitaciones / riesgos / implementación | extracto 5 | p.3]**

HUANG et al.: LEARNING TAILORED ABR ALGORITHMS TO HETEROGENEOUS NETWORK CONDITIONS 2487 Fig. 2. Visualizing personalized networks from the real-world [2], [20], [21]. The video player client decodes and renders video frames from the playback buffer. Once the streaming service starts, the client fetches the video chunk from the HTTP Server or CDN orderly by an ABR algorithm. The ABR algorithm, implemented on the client-side, determines the next chunk and next chunk video quality via throughput estimation and current buffer utilization. After finishing the session, several metrics, such as total bitrate, total re-buffering time, and total bitrate change will be summarized as a QoE metric to evaluate the performance. Thus, how to achieve high QoE scores for adaptive video streaming has become a major challenge for ABR algorithms. Existing ABR algorithms are generally composed of heuris- tics and learning-based. Heuristics make decisions from fea- tures with domain knowledge, e.g., throughput measured [13], buffer occupancy [7] or predefined models [8]. By con- trast, learning-based ABRs model the process as the Markov decision process (MDP): at each step t, the video client, often namely agent in RL framework, take a proper action at (i.e., select a proper bitrate) w.r.t current system status st. The agent then downloads the chunk and computes a reward rt for measuring the current quality-of-experience (QoE) of the past action. The process will terminate if the agent finishes playing the video session. In the end, we aim to generalize a policy π to maximize the QoE of the entire session. The accumulated QoE objective function is defined as Eq.

**[Limitaciones / riesgos / implementación | extracto 6 | p.4]**

2488 IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 Fig. 3. The key principle of our method. We consider learning a good parameter initialization (θ), which can fast adapt to personalized networks. 3) ABR Performance: How do existing one-fits-all ABR algorithms perform in such diverse but unique network con- ditions? Table I shows the average bitrate and stall ratio of existing ABR algorithms (§V-A4) over different mobility types (car and bus) [20]. We show that the irregular networks greatly disturb the stability of the learning-based algorithm, since the difference between the network traffic distributions of the training set and the testing set. Moreover, heuristics like BOLA and RobustMPC (RMPC here) often perform well in one scenario but fail in the other, e.g., BOLA gains a low average bitrate and RobustMPC performs with a high stall ratio. Results indicate that the domain gap among het- erogeneous network scenarios (e.g. Figure 2(b)) leads to the unstable performance of both heuristics and learning-based approaches [16], [24]. One of the feasible ways is to enable the policy to quickly adapt to the current network condition with few trials. As shown, our proposed method A2BR outperforms existing techniques on video bitrate and stall ratio after being trained in 20-shot. In summary, we argue that off-the-shelf “one-fits-all” ABR algorithms fail to provide acceptable performances for all users since the diversity of users’ network conditions. III. METHODS In this section, we start with modeling the tailored ABR proces

**[Limitaciones / riesgos / implementación | extracto 7 | p.4]**

y of the learning-based algorithm, since the difference between the network traffic distributions of the training set and the testing set. Moreover, heuristics like BOLA and RobustMPC (RMPC here) often perform well in one scenario but fail in the other, e.g., BOLA gains a low average bitrate and RobustMPC performs with a high stall ratio. Results indicate that the domain gap among het- erogeneous network scenarios (e.g. Figure 2(b)) leads to the unstable performance of both heuristics and learning-based approaches [16], [24]. One of the feasible ways is to enable the policy to quickly adapt to the current network condition with few trials. As shown, our proposed method A2BR outperforms existing techniques on video bitrate and stall ratio after being trained in 20-shot. In summary, we argue that off-the-shelf “one-fits-all” ABR algorithms fail to provide acceptable performances for all users since the diversity of users’ network conditions. III. METHODS In this section, we start with modeling the tailored ABR process as an Input-driven Markov Decision Process (IMDP). Next, we explain why we have to construct a two-stage process rather than a vanilla one-stage approach. Finally, we briefly introduce meta-agnostic meta-learning and how to leverage domain knowledge. A. Input-Driven MDP Motivated by the observation above, we place the ABR problem in the discrete-time input-driven Markov decision process (MDP) [25], [26]. In detail, we consider the vanilla adaptive video streaming process: at each step t, the video client, often namely agent in RL framework, select a proper bitrate w.r.t current system status. The agent then downloads the chunk and computes an instant score for mea

**[Limitaciones / riesgos / implementación | extracto 8 | p.4]**

e IMDPs with different input processes Z1 and Z2. When observing the same state s, the following agents would determine the same action a. Thus, the difference between the Q values of two agents will be equal only if Z1 equals Z2. For solving Eq. 4, we can employ various reinforcement learning (RL) strategies if Z is known before the process starts. However, in practice, the agent cannot perceptualize its personalized network traffic before transmitting video streams. Assuming that the input process Z is “agnostic” for the agent, we find that vanilla RL method can only learn the optimal policy ˆπ∗which is relevant to Q(s′, a′) instead of Q(s′, a′, z′): max a′∈A Q(s′, a′) = Ez′∼T max a′∈A[Q(s′, a′, z′)]. (5) There exists the variance reduction between the two cases, which eventually results in the sub-optimal policy [26]. Hence, we have a challenge here: considering that the input process can hardly be explicitly observed, how to learn a tailor-made ABR algorithm for heterogeneous network conditions? Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.

**[Limitaciones / riesgos / implementación | extracto 9 | p.5]**

Eq. 1). Let δ denote the parameter weights, inner/outer loop learn- ing rate are represented as α/β, and policy improvement function L, for a distribution of task T , the meta-optimization process can be presented as Eq. 6. δ ←δ −β∇θ  T⟩∼p(T ) LT⟩(fθ −α∇θLT⟩(fθ)) (6) D. Leveraging Domain Knowledge For tackling the second challenge, apart from the gains from MAML, we attempt to adopt the domain principle and knowledge of adaptive video streaming to accelerate the learning efficiency on the online stage. On the one hand, given a complete network trace, recent research has revealed that the ABR process can be precisely emulated by an ABR virtual player [10], [31]. Thus, based on the domain principles of the ABR framework, we implement a faithful ABR simulator to virtual rollout the trajectories, aiming to help improve data effi- ciency and generalization ability. On the other hand, we treat the domain knowledge of state-of-the-art heuristics [8] as the fallback policy which can help identify if the meta policy takes the system into the unexpected status (e.g., interrupt stall event). Putting them together, during the online stage, the agents continually optimize the meta policy according to the trajectories collected from both the real-world and the virtual player, while the real-world samples often account for a small part of them. IV. A2BR OVERVIEW We propose A2BR (Adaption of Adaptive BitRate), a novel neural ABR system that can quickly adapt the personalized network conditions via meta-RL and domain knowledge. The system workflow is shown in Figure 4. A2BR consists of offline meta stage and online adaptation stage. At the offline stage, we train a meta-model using MAML with various n

**[Limitaciones / riesgos / implementación | extracto 10 | p.5]**

olicy from a clean slate in situ. Neverthe- less, recent model-free RL technologies lack sample efficiency, which requires high convergence time on each client [2]. For example, a single agent requires at least 640,000 steps, spanning over 2 years, to converge in the real world. Most users would leave the platform before the algorithm has been completely trained [11]. In this paper, we consider a two-stage approach, which is composed of offline stage and online stage. Technically, at the offline stage, we attempt to train the meta policy via the traces collected by different network conditions, aiming at improving the average performance for all networks. At the online stage, we continually optimize the meta policy to fast “identify” the unique input process for adapting to the personalized networks. To achieve this, we encounter two new challenges based on the specific features of ABR tasks: i) how to obtain a good parameter initialization for fast-learning? ii) How to efficiently learn tailor-made ABR algorithms online? C. Model Agnostic Meta-Learning for the first challenge, we present a method based on meta- learning, which provides an alternative paradigm to improve the learning algorithm itself and gains experience over multiple learning episodes [30]. Treating the task as the user’s person- alized network environment, we find that model agnostic meta learning (MAML) [18] is quite suitable in personalized ABR scenarios where the network traces on each user are quite limited. More comparison of existing meta-learning methods is discussed in §VI-A. Specifically, MAML consists of an inner loop and an outer loop. For every cycle of the outer loop update, a specific task will be

**[Limitaciones / riesgos / implementación | extracto 11 | p.6]**

2490 IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022 Fig. 5. A2BR’s NN architecture overview. A2BR consists of an actor network and a critic network. a) Inputs: As mentioned before, A2BR is allowed to continually learn the system dynamics at the online stage, which motivates us to consider the computational overhead during the inference phase. In other words, A2BR’s input should be carefully designed by avoiding trivial features. In the beginning, we train a teacher network with all possible features as the input (e.g., past bitrate, buffer throughput, download time, response time, bitrate map, chunk map, chunk remaining). Next, we use light weighted machine learning model, i.e., decision tree, to imitate the NN’s policy and prune the most trivial features [32]. Finally, our state representation is listed as follows. For each video chunk t, the agent takes 5 metrics, totally 17 critic features, as the state st. The state contains past video quality qt, current buffer occupancy bt, past k chunk’s throughput measured, i.e., Ct, past k chunk’s download time, i.e., Dt, and past k chunk’s response time: i.e., Pt. Hence, the state st can be written as {qt

**[Limitaciones / riesgos / implementación | extracto 12 | p.6]**

lly-connected layers to extract features. In detail, we first use three Conv1D layers with feature number = 64, and kernel size = 1 to extract features from throughput, download time, and response time. Meanwhile, we adopt two fully-connected layers with feature number = 64 to up-sample the features of past video quality and buffer occupancy. Then we use a concatenate layer to concentrate all the features and take a fully connected layer with 64 neurons to down-sample the features. Finally, we take an n-dim vector with Softmax activation function to represent the actor network’s output and use a single scalar to represent the critic network’s output. 2) Maximum Entropy PPO: As mentioned before, the basic idea of DRL is to improve the policy via improving the probabilities of the high-reward-samples and avoiding the pos- sibilities of the failure-samples from the sampled trajectories. In other words, the improved policy π at state st is required to pick the action at which produced the best-accumulated reward Rt, i.e., at = argmaxa Et[Rt(st, zt, a)]. Due to the setting of meta-learning (§III-B), A2BR often requires more exploration at the offline stage, while less exploration but more exploitation at the online stage. To that end, inspired by the recent maximum entropy policies [34], we present ME-PPO (Maximum Entropy Proxy Policy Opti- mization) to train the NN. See in Eq. 7, the improved policy πθ at state st is required to pick the optimal action a∗ t which produced the best accumulated reward Rt =  t γt(rt + λHπθ(st)), in which Hπθ(st) is the entropy of the current policy (Eq. 8), λ is the entropy weight which encourage explo- ration feedback. It is strongly correlated to

**[Limitaciones / riesgos / implementación | extracto 13 | p.7]**

nd f(δ). 20: Add D′ to D. 21: end for 22: Update meta-model δ with D. 23: end for The central agent finally merges the gradients via workers’ loss functions and the outer loop’s learning rate β. In addition, we make the training phase of the online stage more practical from different perspectives. 1) Meta-Learned Value Network: First, we adopt fresh trajectories to adapt the meta value network before updating the meta policy network. Such settings allow the frame- work to estimate the advantage function precisely and avoid introducing extra bias caused by exogenous inputs to the baseline [26]. 2) Policy Gradient for the Outer Loop: Next, we focus on policy gradient methods [37] for expressing the loss function of the outer loop to accelerate the training process, since there’s no obvious distinction in the overall performance between the complex ME-PPO loss and the vanilla policy gradient loss in the outer loop. In turn, we keep using ME-PPO in the inner loop due to its advantages compared with the policy gradient method (Eq. 14). LP G = −Et ∇θ log πθ(at; st) ˆ At (14) 3) Training With First-Order MAML: Finally, we simplify the MAML process to the First-Order MAML, which com- putes the meta-objective derivative at the post-update para- meters directly [38]. In brief, first-Order MAML ignores the second derivative part and doesn’t have to use all the inner gradients for updating. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.

**[Limitaciones / riesgos / implementación | extracto 14 | p.8]**

e player safely rollouts the trajectory D w.r.t the hybrid policy. Upon finishing the session, we “restore” the current network Env from D and put it into the envi- ronment collector DEnv. Then we randomly sample M net- work environments from the collector and use the virtual player to roll out another set of trajectories D′. Finally, the learner employs ME-PPO for meta policy training accord- ing to D and D′. We discuss the best learning epoch for A2BR in §VI-B. V. EVALUATION In this section, we evaluate A2BR in several personalized network environments, including user-personalized, 3G, 4G, and 5G networks, where the average bandwidth of which are gradually increased, ranging from 3 Mbps to 110 Mbps. Furthermore, we enhance A2BR to support varying the QoE of user preferences. Finally, we conduct a real-world experiment to understand the generalization of A2BR. A. Methodology 1) Implementation: The A2BR’s gym-like environment and the virtual player are written by Python 3.6. At the same time, we adopt TFLearn 1.5.0 [45] to build the A2BR’s NN and TensorFlow 2.4.0 [46] to implement the training workflow. We set inner loop’s learning rate α = 10−4, outer loop’s learning rate β = 10−3, virtual player rollout M = 20. Meanwhile, we use Adam [47] to optimize the model. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.

**[Limitaciones / riesgos / implementación | extracto 15 | p.8]**

arns from clean slates). Hence, we leverage domain principles and knowledge, such as vir- tual environment replay and safe exploration for online RL, to further improve the learning efficiency in the online stage. More specifically, the online training process is mainly composed of a learner, an environment collector, and a fallback policy. The pseudocode in Alg. 2 depicts the overall algorithm. When the video session starts, the video player receives the trained meta model δπ from the training server. Then the player makes the ABR decision with the combination of the meta policy and the fallback policy. Such a hybrid decision enables the player always to play on the “safety” track. Fallback Policy Design: The pre-trained meta-model learns parameter-initialization for varying different network condi- tions, while it hardly guarantees the robustness of our system at the online stage. The meta-model is required to be continually trained at the online stage, as unsafe bitrate decisions may still happen due to action explorations or unexpected changes in the network environment. Hence, we have to design a proper fallback policy to avoid unnecessary stalling events caused by exploration. However, revisiting the recent safe and robust online RL approach [39]–[43], we find that none of the schemes can satisfy our requirements. For example, reward shaping-based approaches such as OnRL [41] and Deep- OR [40] integrate an instinct reward signal as a switching penalty into the reward function. While in our case, the reward functions of the offline stage and the online stage must be con- sistent, otherwise, the critic network has to be retrained w.r.t the changed reward function. Such inac

**[Limitaciones / riesgos / implementación | extracto 16 | p.8]**

exploration for online RL, to further improve the learning efficiency in the online stage. More specifically, the online training process is mainly composed of a learner, an environment collector, and a fallback policy. The pseudocode in Alg. 2 depicts the overall algorithm. When the video session starts, the video player receives the trained meta model δπ from the training server. Then the player makes the ABR decision with the combination of the meta policy and the fallback policy. Such a hybrid decision enables the player always to play on the “safety” track. Fallback Policy Design: The pre-trained meta-model learns parameter-initialization for varying different network condi- tions, while it hardly guarantees the robustness of our system at the online stage. The meta-model is required to be continually trained at the online stage, as unsafe bitrate decisions may still happen due to action explorations or unexpected changes in the network environment. Hence, we have to design a proper fallback policy to avoid unnecessary stalling events caused by exploration. However, revisiting the recent safe and robust online RL approach [39]–[43], we find that none of the schemes can satisfy our requirements. For example, reward shaping-based approaches such as OnRL [41] and Deep- OR [40] integrate an instinct reward signal as a switching penalty into the reward function. While in our case, the reward functions of the offline stage and the online stage must be con- sistent, otherwise, the critic network has to be retrained w.r.t the changed reward function. Such inaccurate value estima- tions will eventually break the fast learning. Meanwhile, other vanilla mask-based approaches (e.g., D

## 6. Figuras / tablas / algoritmos / ecuaciones detectados por texto
- p.2: Fig. 1.
- p.2: Figure 1. The system consists
- p.3: Fig. 2.
- p.3: Eq. 1 ([8], [11]), where Rn represents the each chunk’s video
- p.3: Figure 2(a). The left figure
- p.3: Figure 2(b) shows another
- p.4: Fig. 3.
- p.4: Figure 2(b)) leads to the
- p.4: Eq. 4, we can employ various reinforcement
- p.5: Fig. 4.
- p.5: Eq. 1).
- p.5: Eq. 6.
- p.5: Figure 4. A2BR consists of
- p.5: Figure 5. Here we denote the parameters of the meta actor
- p.6: Fig. 5. A2BR’s NN architecture overview. A2BR consists of an actor network
- p.6: Figure 5, the A2BR’s NN architecture
- p.6: Eq. 7, the improved policy
- p.6: Eq. 8), λ is the entropy weight which encourage explo-
- p.6: Eq. 10,
- p.7: Algorithm 1 Meta-Learning for the Offline Stage
- p.7: Eq. 12.
- p.7: Eq.13). We set Htarget = 0.1 as suggested by related
- p.7: Alg. 1). In the inner loop phase, for each
- p.7: Algorithm 2 Learning Tailor-Made ABRs for the Online Stage
- p.7: Eq 16).
- p.7: Eq. 15.
- p.7: Eq. 14).
- p.8: Alg. 2 depicts the overall algorithm.
- p.8: Eq. 15. The key principle of the mask is to
- p.8: Eq. 16, the heuristic-based method is motivated
- p.9: Fig. 6.
- p.9: Figure 6. We can see that estimating throughput
- p.10: Eq. 17). In this experiment, we set
- p.10: Eq. 1), which is consistent with
- p.10: Figure 7, in which the user id represents
- p.11: Fig. 7.
- p.11: Fig. 8.
- p.11: Figure 7 we can see
- p.11: Figure 8(a) shows the QoE break-
- p.11: Fig. 9.
- p.11: Figure 8(b), we can see a significant benefit
- p.11: Figure 9 shows two bad cases of A2BR.
- p.11: Figure 9(a)) indicates that A2BR doesn’t reach the
- p.11: Figure 7, the ABR algorithm only needs to take
- p.12: Fig. 10.
- p.12: Figure 9(b))
- p.12: Eq. 1) might hardly map the actual QoE for
- p.12: Figure 10 reports the comparison results of existing ABRs,
- p.12: Figure 10(a) demonstrates
- p.12: Figure 10(b) and 10(c) show that A2BR increases the bitrate
- p.12: Figure 10(d) shows a significant performance
- p.12: Figure 10(f) and Figure 10(e), we find the same conclu-
- p.13: Fig. 11.
- p.14: Fig. 12.
- p.14: Figure 11(a). The first change
- p.14: Figure 11 provides a
- p.14: Figure 12(a) shows the per-
- p.15: Figure 12(b). Notably, this scenario is a typical
- p.15: Figure 12(c) and find that Pensieve still
- p.15: Figure 13. A2BR trains faster
- p.15: Fig. 13.
- p.15: Fig. 14.
- p.15: Figure 14.
- p.16: Fig. 15.
- p.16: Figure 15 demonstrates

## 7. Líneas con posible contenido matemático/formal
- p.1: `cation, which is up almost 75% all traffic [1], [2]. Espe-`
- p.1: `Streaming) [3] and DASH [4] has already been the popular`
- p.1: `form of video delivery [5]. Adaptive bitrate (ABR) algorithms`
- p.1: `high video quality while avoiding uninterrupted stall event [5]`
- p.1: `tus [6]–[8]. However, those schemes require a proper setting of`
- p.1: `configuration parameters [9], [10] for fitting different network`
- p.1: `[11], [12], supervised learning [2], [13] and imitation learn-`
- p.1: `ing [14], [15] to train a neural network (NN) w.r.t the given`
- p.2: `training (or tuning) network dataset [16].`
- p.2: `tailored policies in situ [2], is also impractical since off-`
- p.2: `the-shelf model-free RL methods [17] heavily lack sample`
- p.2: `meta-learning technology [18] and utilize maximum entropy`
- p.2: `Rec P.1203 QoE metric [19]. The average QoE is 10%`
- p.2: `higher than the closest ABR approach Fugu [2].`
- p.3: `Visualizing personalized networks from the real-world [2], [20], [21].`
- p.3: `tures with domain knowledge, e.g., throughput measured [13],`
- p.3: `buffer occupancy [7] or predefined models [8]. By con-`
- p.3: `Eq. 1 ([8], [11]), where Rn represents the each chunk’s video`
- p.3: `q(Rn) means the quality metric such as video bitrate [8] and`
- p.3: `VMAF [22] (state-of-the-art quality assessment), μ and ρ are`
- p.3: `methods [11], [23]. Unfortunately, such one-fits-all schemes,`
- p.3: `real-world network conditions [2]. We show the personalized`
- p.3: `the Puffer project [2] and demonstrate the users’ personalized`
- p.4: `types (car and bus) [20]. We show that the irregular networks`
- p.4: `approaches [16], [24]. One of the feasible ways is to enable the`
- p.4: `process (MDP) [25], [26]. In detail, we consider the vanilla`
- p.4: `candidates of next video chunks, Z = {z0, z1, . . . }, ⊆Rk is`
- p.4: `MDPs [27]. The reward function for ABR algorithms is often`
- p.4: `Ta(s′; s, z) = Pr(st+1 = s′; st = s, at = a, zt = z),`
- p.4: `discounted factor ∈[0, 1).`
- p.4: `When γ < 1, there exists an optimal policy π∗(s, z):`
- p.4: `π∗(s, z) = arg max`
- p.4: `For solving Eq. 4, we can employ various reinforcement`
- p.4: `a′∈A Q(s′, a′) = Ez′∼T max`
- p.4: `a′∈A[Q(s′, a′, z′)].`
- p.4: `which eventually results in the sub-optimal policy [26]. Hence,`
- p.5: `both academia [28] and industry [29], training NNs on users’`
- p.5: `which requires high convergence time on each client [2].`
- p.5: `completely trained [11].`
- p.5: `learning episodes [30]. Treating the task as the user’s person-`
- p.5: `learning (MAML) [18] is quite suitable in personalized ABR`
- p.5: `accumulated reward, i.e., QoE (Eq. 1).`
- p.5: `process can be presented as Eq. 6.`
- p.5: `δ ←δ −β∇θ`
- p.5: `LT⟩(fθ −α∇θLT⟩(fθ))`
- p.5: `player [10], [31]. Thus, based on the domain principles of the`
- p.5: `the domain knowledge of state-of-the-art heuristics [8] as the`
- p.5: `model as δπ and the meta critic model as δv. What’s more,`
- p.6: `the most trivial features [32]. Finally, our state representation`
- p.6: `the state st can be written as {qt, bt, Ct, Dt, Pt}. We set`
- p.6: `environments [33].`
- p.6: `with feature number = 64, and kernel size = 1 to extract`
- p.6: `reward Rt, i.e., at = argmaxa Et[Rt(st, zt, a)].`
- p.6: `end, inspired by the recent maximum entropy policies [34],`
- p.6: `mization) to train the NN. See in Eq. 7, the improved policy`
- p.6: `πθ at state st is required to pick the optimal action a∗`
- p.6: `λHπθ(st)), in which Hπθ(st) is the entropy of the current`
- p.6: `policy (Eq. 8), λ is the entropy weight which encourage explo-`
- p.6: `γt(rt + λHπθ(st))]`
- p.6: `Hπθ(st) = −`
- p.6: `πθ(ai; st) log πθ(ai; st).`
- p.6: `Optimization (Dual-PPO) [35]. Briefly, the Dual-clip PPO`
- p.6: `as Eq. 10,`
- p.6: ` πθ(at|st)`
- p.6: `πθold(at|st)(δ) ˆAt,`
- p.6: ` πθ(at|st)`
- p.6: `πθold(at|st)(δ), 1 − , 1 +`
- p.6: `ˆEt[max(LPPO, c ˆAt)]`
- p.6: `ˆEt[LPPO]`
- p.6: `ˆAt = rt + γ[V πθ(st+1) + λHπθ(st+1)] −V πθ(st).`
- p.6: `gradient. We set = 0.2, c = 3 as consistent with the original`
- p.6: `paper [35].`
- p.7: `1: randomly initialize ψ, δπ, and δv`
- p.7: `i ←δ −α∇θLME−P P O`
- p.7: `Update δ with ˆD = {D′`
- p.7: `i|i = 1,· · · , K} using policy`
- p.7: `δ ←δ −β∇θ`
- p.7: `2 ˆEt [At]2 .`
- p.7: `We summarize the loss function LME−P P O in Eq. 12.`
- p.7: `∇LME−P P O = −∇θLME-Policy(πθ, ˆAt) + ∇θvLValue.`

## 8. Texto crudo completo por página

> Mantener este bloque para Codex si necesita comprobar contexto literal. Puede contener errores de orden por columnas del PDF. Para fórmulas exactas o tablas complejas, usar PDF original.


### Página 1

```text
IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022
2485
Learning Tailored Adaptive Bitrate Algorithms to
Heterogeneous Network Conditions:
A Domain-Specific Priors and
Meta-Reinforcement
Learning Approach
Tianchi Huang
, Student Member, IEEE, Chao Zhou, Rui-Xiao Zhang
, Student Member, IEEE,
Chenglei Wu, and Lifeng Sun
, Member, IEEE
Abstract—Internet adaptive video streaming is a typical form
of video delivery that leverages adaptive bitrate (ABR) algorithms
to provide video services with high quality of experience (QoE)
for various users in diverse and unique network conditions. Such
heterogeneous network environments, which can be viewed as
exogenous input processes, often lead to the unstable perfor-
mance of ABR algorithms. Unfortunately, learning-based ABR
algorithm which generated by state-of-the-art reinforcement
learning (RL) technologies achieves good average performance
but fails to perform well in all kinds of network conditions.
In this work, considering the video playback process as the
Input-driven Markov Decision Process (IMDP), we propose
A2BR (Adaptation of ABR), a novel meta-RL ABR approach.
A2BR is mainly composed of an online stage and an offline stage.
It leverages meta-RL to learn an initial meta-policy with various
network conditions at the offline stage and makes decisions
in personalized network conditions at the online stage. At the
same time, we continually optimize the meta-policy to the tailor-
made ABR policy for varying the current network environment
within few shots. Moreover, in order to improve the learning
Manuscript received 15 December 2021; revised 15 March 2022; accepted
23 April 2022. Date of publication 15 June 2022; date of current version
18 July 2022. This work was supported in part by the National Key Research
and Development Program of China under Grant 2018YFB1003703, in part
by NSFC under Grant 61936011, in part by the Beijing Key Laboratory of
Networked Multimedia, and in part by the Kuaishou-Tsinghua Joint Project
under Grant 20192000456. (Corresponding authors: Lifeng Sun; Chao Zhou.)
Tianchi Huang is with the Beijing Key Laboratory of Networked Multime-
dia, Department of Computer Science and Technology, Tsinghua University,
Beijing 100084, China (e-mail: htc19@mails.tsinghua.edu.cn).
Chao Zhou is with Beijing Kuaishou Technology Company Ltd., Beijing
100085, China (e-mail: zhouchao@kuaishou.com).
Rui-Xiao
Zhang
and
Chenglei
Wu are
with
the
Beijing
National
Research
Center
for
Information
Science
and
Technology
(BNRist),
Department
of
Computer
Science
and
Technology,
Tsinghua
Univer-
sity,
Beijing
100084,
China
(e-mail:
zhangrx17@mails.tsinghua.edu.cn;
wucl18@mails.tsinghua.edu.cn).
Lifeng Sun is with the Beijing Key Laboratory of Networked Multimedia,
Department of Computer Science and Technology, Tsinghua University,
Beijing 100084, China, also with the Beijing National Research Center for
Information Science and Technology (BNRist), Department of Computer
Science and Technology, Tsinghua University, Beijing 100084, China, and
also with the Key Laboratory of Pervasive Computing, Ministry of Education,
Tsinghua University, Beijing 100084, China (e-mail: sunlf@tsinghua.edu.cn).
Color versions of one or more figures in this article are available at
https://doi.org/10.1109/JSAC.2022.3180804.
Digital Object Identifier 10.1109/JSAC.2022.3180804
efficiency, we fully utilize domain knowledge for implementing
a virtual player to replay the previously experienced network.
Using trace-driven experiments on various scenarios including
different vehicles, users, network types, and heterogeneous user-
preferences, we show that A2BR outperforming recent ABR
approaches with rapidly adapting to the personalized QoE
metrics and specific network conditions. Testbed experimental
results also illustrate the superiority of A2BR in adapting to the
unseen environments.
Index Terms—Streaming media, reinforcement learning (RL),
adaptive control.
I. INTRODUCTION
D
UE to the rapid development of network services, video
streaming now stands for the predominant Internet appli-
cation, which is up almost 75% all traffic [1], [2]. Espe-
cially, adaptive video streaming, such as HLS (HTTP Live
Streaming) [3] and DASH [4] has already been the popular
form of video delivery [5]. Adaptive bitrate (ABR) algorithms
enable Internet adaptive video streaming services to achieve
high video quality while avoiding uninterrupted stall event [5]
(§II-A). Revisiting the recent success of ABR algorithms,
heuristics often make decisions based on network or player sta-
tus [6]–[8]. However, those schemes require a proper setting of
configuration parameters [9], [10] for fitting different network
distributions. By contrast, learning-based schemes employ
several learning technologies, such as reinforcement learning
[11], [12], supervised learning [2], [13] and imitation learn-
ing [14], [15] to train a neural network (NN) w.r.t the given
network traffic distributions, and make a zero-shot inference
for unseen networks. In short, existing ABR algorithms, either
heuristics or learning-based schemes, seldom configure or tune
their parameters automatically and rapidly for varying the
current network traffic distribution.
However, in the adaptive video streaming scenario, the
system dynamics are uncertain and the future state cannot be
accurately predicted. To prove this view, we focus on inves-
tigating the impact of ABR algorithms on the distribution of
heterogeneous network traffics, where the distribution is usu-
ally summarized by bandwidth traces experienced by different
0733-8716 © 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 2

```text
2486
IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022
users at any time, in any place, and especially, under any
network conditions. Through the analysis of the impact on the
network distributions of different users, vehicles, and network
types, we empirically find that nowadays’ Internet network
conditions are not only diverse but also unique (§II-B). For
example, the heterogeneity of network conditions for each user
is inevitable, since both subjective and objective user behavior
have an important impact on the network traffic distribution.
Nevertheless, existing ABR algorithms, either heuristics or
learning-based, fail to adapt to such heterogeneous bandwidth
conditions that are significantly different from the offline
training (or tuning) network dataset [16].
Motivated by these facts, we model the ABR playback
process as Input-driven Markov Decision Process (IMDP),
which can express an implicit heterogeneous network envi-
ronment in an explicit manner (§III-A). We theoretically
illustrate that vanilla RL technologies can only generalize
a strategy that can perform well on average rather than
every network condition. While through in-depth analysis,
we find that the most intuitive solution, i.e., reinforced
tailored policies in situ [2], is also impractical since off-
the-shelf model-free RL methods [17] heavily lack sample
efficiency, which cannot train a policy within an acceptable
time.
Hence, based on the theory of IMDP, we propose A2BR
(Adaption of Adaptive Bitrate Algorithm), a novel neural
meta-RL ABR system that enables fast adaptation to the
specific network conditions (§III-B). A2BR is composed of the
offline stage and online stage (§IV). At the offline stage, A2BR
trains a meta-model with various real and synthetic network
conditions for learning parameter initialization meta-policy,
where the policy can provide rapid adaptation for varying
heterogeneous networks. To achieve this goal, we implement
the training process based on the state-of-the-art gradient-free
meta-learning technology [18] and utilize maximum entropy
RL methodologies to achieve better exploration (§IV-B).
Moreover, at the online stage, the video player, placed on
the user side, receives the trained meta-model and picks the
bitrates w.r.t the meta-policy and the current specific network
status. Upon finishing the video session, the meta-policy is
continually updated to the tailor-made policy with the collected
trajectories. For improving the learning efficiency, the trajec-
tories are collected not only from the real world but also from
the “virtual world.” Specifically, the virtual world is motivated
by domain principles and constructed by a faithful virtual
player and experienced network environments. In addition,
we also employ the domain knowledge that uses heuristics
to enable safe online RL. Subsequently, the meta-policy will
be continually optimized within 20-shot, i.e., watch 20 videos
at the online stage (§IV-C).
In the rest of the paper, we conduct several experiments
to evaluate A2BR with existing ABR approaches (§V).
The case studies contain different types of heterogeneous
network conditions and QoE objectives, including differ-
ent vehicles, users’ personalized networks, 4G/5G networks,
and varying user preferences for QoE metrics. Using trace-
driven simulation and real-world evaluation on various videos,
we show:
Fig. 1.
The typical ABR system overview. The ABR algorithm is usually
placed on the client-side.
1) A2BR improves the video quality by up to 12.6% while
reducing the stall time by 69.3% to 2.8× compared with
previously proposed approaches.
2) In the user-personalized network, A2BR outperforms recent
heuristics and learning-based ABRs, with improvements on
average QoE of 12%-23%;
3) A2BR maintains high bitrates with low video stall in both
4G and 5G networks, whereas the learning-based approach
Pensieve diverges. At the same time, A2BR either matches
or exceeds the performance of existing schemes on IT-T
Rec P.1203 QoE metric [19]. The average QoE is 10%
higher than the closest ABR approach Fugu [2].
4) A2BR with minor modification can hold QoE metrics with
different user preferences, further providing 5% improve-
ments on QoE at the online stage.
5) We prove that A2BR still performs well on both emulation
and real-world testbed. Ablution studies show that the
online stage further improves the average QoE by 6% after
learning in specific network conditions within 10-shot, and
8% after 50-shot.
The contributions of this work are summarized as follows:
• We empirically analyze today’s heterogeneous network traf-
fics and propose a two-stage meta-learning scheme for
varying specific network conditions.
• We implement A2BR, which is the first meta-learning with
domain knowledge approach for adaptive streaming.
• Results on different types of network conditions illustrate
that the generated tailor-made ABR policies can well adapt
to heterogeneous networks with relatively few-shot.
II. BACKGROUND AND MOTIVATION
Our research is started with a fundamental quest: How will
the recent ABRs perform in various network traffic environ-
ments?. To answer this question, first, we briefly introduce
the key principle of adaptive video streaming and adaptive
bitrate (ABR) algorithms. We then use empirical measure-
ments to elucidate the key limitations of prior solutions.
A. Adaptive Video Streaming
The adaptive bitrate method (ABR) is an algorithm that
dynamically selects video bitrates via network conditions and
the client’s buffer occupancy. The traditional video stream-
ing architecture is shown in Figure 1. The system consists
of a video player client with a constrained buffer length
and an HTTP-Server or Content Delivery Network (CDN).
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 3

```text
HUANG et al.: LEARNING TAILORED ABR ALGORITHMS TO HETEROGENEOUS NETWORK CONDITIONS
2487
Fig. 2.
Visualizing personalized networks from the real-world [2], [20], [21].
The video player client decodes and renders video frames
from the playback buffer. Once the streaming service starts,
the client fetches the video chunk from the HTTP Server or
CDN orderly by an ABR algorithm. The ABR algorithm,
implemented on the client-side, determines the next chunk
and next chunk video quality via throughput estimation and
current buffer utilization. After finishing the session, several
metrics, such as total bitrate, total re-buffering time, and total
bitrate change will be summarized as a QoE metric to evaluate
the performance. Thus, how to achieve high QoE scores for
adaptive video streaming has become a major challenge for
ABR algorithms.
Existing ABR algorithms are generally composed of heuris-
tics and learning-based. Heuristics make decisions from fea-
tures with domain knowledge, e.g., throughput measured [13],
buffer occupancy [7] or predefined models [8]. By con-
trast, learning-based ABRs model the process as the Markov
decision process (MDP): at each step t, the video client,
often namely agent in RL framework, take a proper action
at (i.e., select a proper bitrate) w.r.t current system status st.
The agent then downloads the chunk and computes a reward rt
for measuring the current quality-of-experience (QoE) of the
past action. The process will terminate if the agent finishes
playing the video session. In the end, we aim to generalize a
policy π to maximize the QoE of the entire session.
The accumulated QoE objective function is defined as
Eq. 1 ([8], [11]), where Rn represents the each chunk’s video
bitrate, Tn reflects the rebuffering time for each chunk n,
q(Rn) means the quality metric such as video bitrate [8] and
VMAF [22] (state-of-the-art quality assessment), μ and ρ are
the weight of rebuffering and smoothness penalty, respectively.
QoE =
N

n=1
q(Rn) −μ
N

n=1
Tn −ρ
N−1

n=1
|q(Rn+1) −q(Rn)|
(1)
B. Different Types of Network Conditions
Recently, several learning-based schemes have been made
to train an NN policy from the clean slate via various RL
methods [11], [23]. Unfortunately, such one-fits-all schemes,
including heuristics and learning-based can hardly always
perform well in today’s network traffics due to the diversity of
real-world network conditions [2]. We show the personalized
network environments from two perspectives.
TABLE I
COMPARISON RESULTS ON DIFFERENT ABRS OVER 3G-CAR AND
3G-BUS NETWORKS, WHERE A2BR IS FINE-TUNED IN 20-SHOT
1) Sorted by Users: First, we measure a portion of data from
the Puffer project [2] and demonstrate the users’ personalized
network status on June 2, 2021, in Figure 2(a). The left figure
illustrates the correlations between throughput and round-
trip-time (RTT) of each user. As shown, in the real world,
the average bandwidth is particularly varied, ranging from
0.1 to 100 Mbps. The lower bandwidth leads to larger RTT.
The network environment of each user is different. Someone
can watch the videos with high bandwidth and low RTT, while
the others live in the low bandwidth and high RTT scenario.
The right figure plots the fine-grained cumulative distribution
function (CDF) of throughput and RTT of the users with top-8
viewing hours on that day. We can find the tailor-made features
for personalized network conditions: some of the users have
very constant throughput (e.g., user C and user F), while
most of the users’ bandwidth is unstable and doesn’t cover
all network conditions.
2) Sorted by Scenarios: Next, Figure 2(b) shows another
personalized network condition that is categorized by network
types, which covers 3G, 4G, and 5G networks. Testing results
on the bus, car, and metro environments show that different
vehicle speeds lead to very different 3G bandwidth distri-
butions. For instance, we can see the throughput measured
from the metro achieves the lowest average and fluctuation
value among the candidates. While we observe the highest
bandwidth with high fluctuation in the 3G-car scenario. Mean-
while, in addition to the various network specifics on 4G
and 5G, the network distributions are always influenced by
user behaviors: the network on walking and driving also have
their particularity. Hence, the domain gap, which represents
the relationship between network traffic distributions across
different network types and users, has brought great challenges
to recent rate adaptation algorithms.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 4

```text
2488
IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022
Fig. 3.
The key principle of our method. We consider learning a good
parameter initialization (θ), which can fast adapt to personalized networks.
3) ABR Performance:
How do existing one-fits-all ABR
algorithms perform in such diverse but unique network con-
ditions? Table I shows the average bitrate and stall ratio
of existing ABR algorithms (§V-A4) over different mobility
types (car and bus) [20]. We show that the irregular networks
greatly disturb the stability of the learning-based algorithm,
since the difference between the network traffic distributions
of the training set and the testing set. Moreover, heuristics
like BOLA and RobustMPC (RMPC here) often perform well
in one scenario but fail in the other, e.g., BOLA gains a
low average bitrate and RobustMPC performs with a high
stall ratio. Results indicate that the domain gap among het-
erogeneous network scenarios (e.g. Figure 2(b)) leads to the
unstable performance of both heuristics and learning-based
approaches [16], [24]. One of the feasible ways is to enable the
policy to quickly adapt to the current network condition with
few trials. As shown, our proposed method A2BR outperforms
existing techniques on video bitrate and stall ratio after being
trained in 20-shot.
In summary, we argue that off-the-shelf “one-fits-all” ABR
algorithms fail to provide acceptable performances for all users
since the diversity of users’ network conditions.
III. METHODS
In this section, we start with modeling the tailored ABR
process as an Input-driven Markov Decision Process (IMDP).
Next, we explain why we have to construct a two-stage process
rather than a vanilla one-stage approach. Finally, we briefly
introduce meta-agnostic meta-learning and how to leverage
domain knowledge.
A. Input-Driven MDP
Motivated by the observation above, we place the ABR
problem in the discrete-time input-driven Markov decision
process (MDP) [25], [26]. In detail, we consider the vanilla
adaptive video streaming process: at each step t, the video
client, often namely agent in RL framework, select a proper
bitrate w.r.t current system status. The agent then downloads
the chunk and computes an instant score for measuring the
quality of the past action. The process continues until the agent
finished playing the video session.
Definition 1:
An input-driven MDP M is defined by a
4-tuple M = (S, A, Z, R), in which S ⊆Rn is a set of
n-dimensional states observed (e.g., past throughput mea-
sured, buffer occupancy, past bitrate selected, etc.), A ⊆Rm
is a set of m-dimensional actions, representing the bitrate
candidates of next video chunks, Z = {z0, z1, . . . }, ⊆Rk is
a set of k-dimensional input process, as S × A →R denotes
the intermediate reward for each bitrate selection operation
on the given state.
Commonly, the input process in the ABR problem is often
denoted as a set of exogenous variables. For example, the
personalized network traffic distribution for each user, network
status in various network types, tailored QoE preference, etc.
Notably, zt is a general process, which is independent for
the state st and action at. In other words, the at depends
on st only, with no relationship to zt – this is the key dif-
ference between input-driven MDPs and Partially Observable
MDPs [27]. The reward function for ABR algorithms is often
defined to achieve high quality of experience (QoE).
Definition 2:
For an input-driven MDPs, the stochastic
transition dynamics are given by
Ta(s′; s, z) = Pr(st+1 = s′; st = s, at = a, zt = z),
(2)
representing a state-transition probability of next state st+1
with the given any state st, action at, and current personalized
networks zt.
Definition 3: Followed by the definition of input-driven
MDP, the Q-value of a given state-action pair can be defined
as
Q(s, a, z) =

s′∈S
Ta(s′; s, z) (r(s, z, a) + γV (s′, z′))
(3)
Here V (s′, z′) is the value function for state s′, γ is the
discounted factor ∈[0, 1).
When γ < 1, there exists an optimal policy π∗(s, z):
π∗(s, z) = arg max
a∈A

s′∈S
Ta(s′, z′; s, z)
×

r(s, z, a) + γ max
a′∈A Q(s′, a′, z′)

(4)
Here we consider two agents with the same policy π, while
they work in the IMDPs with different input processes Z1
and Z2. When observing the same state s, the following
agents would determine the same action a. Thus, the difference
between the Q values of two agents will be equal only if Z1
equals Z2.
For solving Eq. 4, we can employ various reinforcement
learning (RL) strategies if Z is known before the process
starts. However, in practice, the agent cannot perceptualize its
personalized network traffic before transmitting video streams.
Assuming that the input process Z is “agnostic” for the agent,
we find that vanilla RL method can only learn the optimal
policy ˆπ∗which is relevant to Q(s′, a′) instead of Q(s′, a′, z′):
max
a′∈A Q(s′, a′) = Ez′∼T max
a′∈A[Q(s′, a′, z′)].
(5)
There exists the variance reduction between the two cases,
which eventually results in the sub-optimal policy [26]. Hence,
we have a challenge here: considering that the input process
can hardly be explicitly observed, how to learn a tailor-made
ABR algorithm for heterogeneous network conditions?
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 5

```text
HUANG et al.: LEARNING TAILORED ABR ALGORITHMS TO HETEROGENEOUS NETWORK CONDITIONS
2489
Fig. 4.
The system overview of A2BR. A2BR mainly consists of two stages, the offline stage and the online stage.
B. Meta-RL With Domain Knowledge
With the rapid progress of on-device machine learning in
both academia [28] and industry [29], training NNs on users’
devices has already been a practical way of learning the
tailor-made ABR policy from a clean slate in situ. Neverthe-
less, recent model-free RL technologies lack sample efficiency,
which requires high convergence time on each client [2].
For example, a single agent requires at least 640,000 steps,
spanning over 2 years, to converge in the real world. Most
users would leave the platform before the algorithm has been
completely trained [11].
In this paper, we consider a two-stage approach, which is
composed of offline stage and online stage. Technically, at the
offline stage, we attempt to train the meta policy via the traces
collected by different network conditions, aiming at improving
the average performance for all networks. At the online stage,
we continually optimize the meta policy to fast “identify”
the unique input process for adapting to the personalized
networks. To achieve this, we encounter two new challenges
based on the specific features of ABR tasks: i) how to obtain
a good parameter initialization for fast-learning? ii) How to
efficiently learn tailor-made ABR algorithms online?
C. Model Agnostic Meta-Learning
for the first challenge, we present a method based on meta-
learning, which provides an alternative paradigm to improve
the learning algorithm itself and gains experience over multiple
learning episodes [30]. Treating the task as the user’s person-
alized network environment, we find that model agnostic meta
learning (MAML) [18] is quite suitable in personalized ABR
scenarios where the network traces on each user are quite
limited. More comparison of existing meta-learning methods is
discussed in §VI-A. Specifically, MAML consists of an inner
loop and an outer loop. For every cycle of the outer loop
update, a specific task will be sampled from a distribution
of tasks. and trains the parameter weights that determine the
agent’s behavior. In the inner loop, the agent interacts with
the sampled environment and optimizes for maximizing the
accumulated reward, i.e., QoE (Eq. 1).
Let δ denote the parameter weights, inner/outer loop learn-
ing rate are represented as α/β, and policy improvement
function L, for a distribution of task T , the meta-optimization
process can be presented as Eq. 6.
δ ←δ −β∇θ

T⟩∼p(T )
LT⟩(fθ −α∇θLT⟩(fθ))
(6)
D. Leveraging Domain Knowledge
For tackling the second challenge, apart from the gains
from MAML, we attempt to adopt the domain principle
and knowledge of adaptive video streaming to accelerate the
learning efficiency on the online stage. On the one hand, given
a complete network trace, recent research has revealed that the
ABR process can be precisely emulated by an ABR virtual
player [10], [31]. Thus, based on the domain principles of the
ABR framework, we implement a faithful ABR simulator to
virtual rollout the trajectories, aiming to help improve data effi-
ciency and generalization ability. On the other hand, we treat
the domain knowledge of state-of-the-art heuristics [8] as the
fallback policy which can help identify if the meta policy
takes the system into the unexpected status (e.g., interrupt
stall event). Putting them together, during the online stage, the
agents continually optimize the meta policy according to the
trajectories collected from both the real-world and the virtual
player, while the real-world samples often account for a small
part of them.
IV. A2BR OVERVIEW
We propose A2BR (Adaption of Adaptive BitRate), a novel
neural ABR system that can quickly adapt the personalized
network conditions via meta-RL and domain knowledge. The
system workflow is shown in Figure 4. A2BR consists of
offline meta stage and online adaptation stage. At the offline
stage, we train a meta-model using MAML with various
network environments to learn a good parameter initialization
for achieving both acceptable “mean” performance and fast
adaptation. At the online stage, the agents continually tune
the meta-model with the help of domain knowledge for rapidly
varying the personalized network condition, i.e., generating a
tailor-made ABR algorithm.
A. Basic Training Algorithm
In this section, we introduce the NN architecture for each
model in A2BR. First, we describe the NN’s inputs, outputs,
and architecture. Then, we explain the basic training method-
ology of A2BR.
1) NN Model Overview: The NN architecture is shown in
Figure 5. Here we denote the parameters of the meta actor
model as δπ and the meta critic model as δv. What’s more,
we refer to the combination of the meta actor model and critic
model as the meta actor-critic model.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 6

```text
2490
IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022
Fig. 5. A2BR’s NN architecture overview. A2BR consists of an actor network
and a critic network.
a) Inputs:
As mentioned before, A2BR is allowed to
continually learn the system dynamics at the online stage,
which motivates us to consider the computational overhead
during the inference phase. In other words, A2BR’s input
should be carefully designed by avoiding trivial features.
In the beginning, we train a teacher network with all possible
features as the input (e.g., past bitrate, buffer throughput,
download time, response time, bitrate map, chunk map, chunk
remaining). Next, we use light weighted machine learning
model, i.e., decision tree, to imitate the NN’s policy and prune
the most trivial features [32]. Finally, our state representation
is listed as follows.
For each video chunk t, the agent takes 5 metrics, totally
17 critic features, as the state st. The state contains past
video quality qt, current buffer occupancy bt, past k chunk’s
throughput measured, i.e., Ct, past k chunk’s download time,
i.e., Dt, and past k chunk’s response time: i.e., Pt. Hence,
the state st can be written as {qt, bt, Ct, Dt, Pt}. We set
past k as 5 for further reducing the state size due to the
light-weighted requirements. Moreover, instead of feeding the
exact values of gathered statistics to the agent, we also use
normalized statistics. The state normalization method enables
the agent to generalize the strategy better in unseen network
environments [33].
b) Outputs:
The A2BR’s actor model uses a discrete
action space, i.e., an n-dim vector, which indicates the proba-
bility of the bitrate level being selected under the current state.
The A2BR’s critic model outputs a single scalar, representing
the estimated value for the current state.
NN architecture A2BR uses a neural network (NN) to
take an action for the given state. For each video chunk, the
agent mainly takes the past five values as a sequence for
representing the current state, including past video quality,
buffer occupancy, throughput, download time, and response
time. As shown in Figure 5, the A2BR’s NN architecture
uses several Conv-1D layers and fully-connected layers to
extract features. In detail, we first use three Conv1D layers
with feature number = 64, and kernel size = 1 to extract
features from throughput, download time, and response time.
Meanwhile, we adopt two fully-connected layers with feature
number = 64 to up-sample the features of past video quality
and buffer occupancy. Then we use a concatenate layer to
concentrate all the features and take a fully connected layer
with 64 neurons to down-sample the features. Finally, we take
an n-dim vector with Softmax activation function to represent
the actor network’s output and use a single scalar to represent
the critic network’s output.
2) Maximum Entropy PPO: As mentioned before, the basic
idea of DRL is to improve the policy via improving the
probabilities of the high-reward-samples and avoiding the pos-
sibilities of the failure-samples from the sampled trajectories.
In other words, the improved policy π at state st is required
to pick the action at which produced the best-accumulated
reward Rt, i.e., at = argmaxa Et[Rt(st, zt, a)].
Due to the setting of meta-learning (§III-B), A2BR often
requires more exploration at the offline stage, while less
exploration but more exploitation at the online stage. To that
end, inspired by the recent maximum entropy policies [34],
we present ME-PPO (Maximum Entropy Proxy Policy Opti-
mization) to train the NN. See in Eq. 7, the improved policy
πθ at state st is required to pick the optimal action a∗
t which
produced the best accumulated reward Rt = 
t γt(rt +
λHπθ(st)), in which Hπθ(st) is the entropy of the current
policy (Eq. 8), λ is the entropy weight which encourage explo-
ration feedback. It is strongly correlated to the unpredictability
of the actions which an agent takes in a given policy. The
greater the entropy, the more random the actions that an agent
performs, and vice versa.
a∗
t = arg max
a
ˆEt[

t
γt(rt + λHπθ(st))]
(7)
Hπθ(st) = −

i∈A
πθ(ai; st) log πθ(ai; st).
(8)
ME-PPO is incrementally implemented based on state-
of-the-art on-policy DRL algorithm Dual-clip Proxy Policy
Optimization (Dual-PPO) [35]. Briefly, the Dual-clip PPO
algorithm adopts a double-clip method to restrict the step size
of the policy iteration and update the NN by minimizing the
following clipped surrogate objective.
The loss function of the A2BR’s actor network is computed
as Eq. 10,
LPPO = min
 πθ(at|st)
πθold(at|st)(δ) ˆAt,
clip
 πθ(at|st)
πθold(at|st)(δ), 1 − , 1 +
 ˆAt

.
(9)
LME-Policy =

ˆEt[max(LPPO, c ˆAt)]
ˆAt < 0
ˆEt[LPPO]
ˆAt ≥0
(10)
where ˆAt is the advantage function:
ˆAt = rt + γ[V πθ(st+1) + λHπθ(st+1)] −V πθ(st).
(11)
Here and c are hyper-parameters that control how to clip the
gradient. We set = 0.2, c = 3 as consistent with the original
paper [35].
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 7

```text
HUANG et al.: LEARNING TAILORED ABR ALGORITHMS TO HETEROGENEOUS NETWORK CONDITIONS
2491
Algorithm 1 Meta-Learning for the Offline Stage
Require: p(Env): distribution over heterogeneous networks.
Require: α, β: learning rate for inner-loop and outer-loop.
1: randomly initialize ψ, δπ, and δv
2: while not done do
3:
Sample user’s network environments Envi ∼p(Env)
4:
// Train the NN in parallel, agent number K
5:
for Envi in K do
6:
// Inner Loop Phase
7:
Rollout M trajectories D in Envi using fθ.
8:
Meta-update using using ME-PPO:
δ′
i ←δ −α∇θLME−P P O
Envi
(fθ, D).
9:
// Outer Loop Phase
10:
Sample trajectory D′
i using fθ′
i in Envi.
11:
end for
12:
// Outer Loop Update
13:
Update δ with ˆD = {D′
i|i = 1,· · · , K} using policy
gradient:
δ ←δ −β∇θ

Envi∼p(Env) LP G
Envi(fθ′
i, D′
i).
14: end while
The A2BR’s critic network Vθp is updated via minimizing
the error of the advantage function ˆAt: LValue = 1
2 ˆEt [At]2 .
We summarize the loss function LME−P P O in Eq. 12.
∇LME−P P O = −∇θLME-Policy(πθ, ˆAt) + ∇θvLValue.
(12)
Meanwhile, considering that on-policy RL is sensitive to
the entropy weight and it usually requires careful tuning [10],
we autonomously adjust the entropy weight λ for minimizing
the gap between the current entropy and the target entropy
Htarget (Eq.13). We set Htarget = 0.1 as suggested by related
work [36]. α is the learning rate of the actor-network.
λ ←λ −α [Hπθ(st) −Htarget] .
(13)
We summarize all hyper-parameters of ME-PPO as follows:
i) entropy weight λ, ii )PPO clip factor , iii) Dual-clip PPO
clip factor c, iv) target entropy Htarget, and v) learning rate
α, β. It’s important that most parameters (i.e. , c, α, β) are
configured as the default settings of the original paper [17],
[35], [36]. The only special parameter is the entropy weight
λ. It is dynamically being tuned by Htarget and α during
training.
B. Meta-Learned Policies for Offline Stage
Inspired by vanilla MAML methods, the offline training
phase can be categorized into the inner loop phase and
outer loop phase (Alg. 1). In the inner loop phase, for each
epoch, the worker i first randomly picks a specific network
condition as the environment from the network status pool,
and samples N trajectories in that environment according to
the current policy πθ. Then the meta-model is optimized by
the collected trajectories with the ME-PPO method. Here we
treat the learned meta-model as δ′
i. In the outer loop phase,
the worker i continually rollouts several trajectories from the
randomized selected environments with the meta-policy f(δ′
i),
and computes gradients for δ with the trajectory. Subsequently,
each worker sends the computed gradients to the central agent.
Algorithm 2 Learning Tailor-Made ABRs for the Online Stage
Require: δ: The trained meta-model in the offline stage.
Require: DEnv: the collection of network environments
experienced.
1: DEnv = {}.
2: for video session do
3:
// rollout policy with the “real” player.
4:
t ←0; D = {}.
5:
while not done do
6:
Get ABR state st.
7:
Get π w.r.t st and δ: πθ(st).
8:
Predict future throughput: ˆct.
9:
Generate mask m with the fallback policy (Eq 16).
10:
Pick ˆat according to Eq. 15.
11:
Calculate instant reward rt.
12:
Add {st, ˆat, rt} to D.
13:
t ←t + 1
14:
end while
15:
Estimate environment experienced Env from D in hind-
sight; Add Env to DEnv.
16:
// rollout policy from virtual environment.
17:
for M Rollouts do
18:
Uniformly sample condition Env′ from DEnv.
19:
Rollout trajectories D′ using Env′ and f(δ).
20:
Add D′ to D.
21:
end for
22:
Update meta-model δ with D.
23: end for
The central agent finally merges the gradients via workers’
loss functions and the outer loop’s learning rate β. In addition,
we make the training phase of the online stage more practical
from different perspectives.
1) Meta-Learned Value Network: First, we adopt fresh
trajectories to adapt the meta value network before updating
the meta policy network. Such settings allow the frame-
work to estimate the advantage function precisely and avoid
introducing extra bias caused by exogenous inputs to the
baseline [26].
2) Policy Gradient for the Outer Loop: Next, we focus on
policy gradient methods [37] for expressing the loss function
of the outer loop to accelerate the training process, since
there’s no obvious distinction in the overall performance
between the complex ME-PPO loss and the vanilla policy
gradient loss in the outer loop. In turn, we keep using ME-PPO
in the inner loop due to its advantages compared with the
policy gradient method (Eq. 14).
LP G = −Et


∇θ log πθ(at; st) ˆ
At


(14)
3) Training With First-Order MAML: Finally, we simplify
the MAML process to the First-Order MAML, which com-
putes the meta-objective derivative at the post-update para-
meters directly [38]. In brief, first-Order MAML ignores the
second derivative part and doesn’t have to use all the inner
gradients for updating.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 8

```text
2492
IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022
C. Learning Tailor-Made ABRs for Online Stage
Recall that we attempt to learn a tailor-made ABR algorithm
for varying current heterogeneous networks within few-shot
learning at the online stage. As much as MAML enables
the meta models (i.e., NN) to learn quickly for varying
the current users’ network condition, it still takes at least
2,000 times on watching videos to complete the adapta-
tion to the current network (even it’s 320× faster than
the prior approach that learns from clean slates). Hence,
we leverage domain principles and knowledge, such as vir-
tual environment replay and safe exploration for online RL,
to further improve the learning efficiency in the online
stage.
More specifically, the online training process is mainly
composed of a learner, an environment collector, and a fallback
policy. The pseudocode in Alg. 2 depicts the overall algorithm.
When the video session starts, the video player receives
the trained meta model δπ from the training server. Then
the player makes the ABR decision with the combination
of the meta policy and the fallback policy. Such a hybrid
decision enables the player always to play on the “safety”
track.
Fallback Policy Design: The pre-trained meta-model learns
parameter-initialization for varying different network condi-
tions, while it hardly guarantees the robustness of our system at
the online stage. The meta-model is required to be continually
trained at the online stage, as unsafe bitrate decisions may
still happen due to action explorations or unexpected changes
in the network environment. Hence, we have to design a
proper fallback policy to avoid unnecessary stalling events
caused by exploration. However, revisiting the recent safe and
robust online RL approach [39]–[43], we find that none of the
schemes can satisfy our requirements. For example, reward
shaping-based approaches such as OnRL [41] and Deep-
OR [40] integrate an instinct reward signal as a switching
penalty into the reward function. While in our case, the reward
functions of the offline stage and the online stage must be con-
sistent, otherwise, the critic network has to be retrained w.r.t
the changed reward function. Such inaccurate value estima-
tions will eventually break the fast learning. Meanwhile, other
vanilla mask-based approaches (e.g., Decima [42]) block the
unsafely or invalid actions by applying action masking [44].
Nevertheless, the mask values are often determined by the
exogenous inputs, e.g., global DAG information ([42]), which
is not included in the state space. Hence, the tailor-made ABR
policy cannot be successfully learned without changing the
state representation.
To this end, we propose a fallback policy that only relies on
the metrics in the current state representation, that is, it doesn’t
require any additional modification to the reward function.
The fallback policy is a hybrid scheme that combines the
original NN’s actor outputs and the mask of a heuristic-based
method, shown in Eq. 15. The key principle of the mask is to
“filter” out all the bitrate actions that might incur rebuffering
events, instead of directly making bitrate selection policies.
As listed in Eq. 16, the heuristic-based method is motivated
by HYB [10] that simply picks the maximum bitrate without
occurring stall events. In detail, at chunk t, the hybrid action
ˆat for the given state st becomes
ˆat ∼{
miewi

j mjewj |∀i = [1, . . . , j]}
(15)
mi =

1
ˆctbt −RiL > 0
0 otherwise,
(16)
where for the i-th mask of the total bitrate levels (aka.,
actions) j, mi indicates a mask, presented by a {0, 1}
vector, that controls whether the action ai are safe or not.
ˆct is the predicted network capacity. Here ˆct is calculated
by the average value of past throughput measured, i.e., ˆct =
 Ct/  (Dt + Pt). Note that it can be measured by any
prediction method, such as EWMA and harmonic mean. bt
is the current buffer occupancy of the player. Each chunk
has the same video time of L seconds. Thus, RiL means the
average chunk size for the i −th bitrate-level. w represents
the final NN output with no activation functions. The mask
values can be easily computed from the state input. As a result,
we can still use the original training techniques to update the
NN since the back-propagation of the gradient of the NN still
holds.
We evaluate the proportion of using the original meta-policy
and fallback policy. Results show that the fallback policy only
accounts for about 1%-4% of the overall decision-making in
different network scenarios (not shown). It makes sense since
the fallback policy will be enabled only if the meta-policy picks
the bitrate that might occur during the stall event. In other
words, the fallback policy is the lower bound of A2BR.
Most of the decisions are still determined by the meta-policy
model.
Consequently, the player safely rollouts the trajectory D
w.r.t the hybrid policy. Upon finishing the session, we “restore”
the current network Env from D and put it into the envi-
ronment collector DEnv. Then we randomly sample M net-
work environments from the collector and use the virtual
player to roll out another set of trajectories D′. Finally, the
learner employs ME-PPO for meta policy training accord-
ing to D and D′. We discuss the best learning epoch
for A2BR in §VI-B.
V. EVALUATION
In this section, we evaluate A2BR in several personalized
network environments, including user-personalized, 3G, 4G,
and 5G networks, where the average bandwidth of which
are gradually increased, ranging from 3 Mbps to 110 Mbps.
Furthermore, we enhance A2BR to support varying the QoE of
user preferences. Finally, we conduct a real-world experiment
to understand the generalization of A2BR.
A. Methodology
1) Implementation: The A2BR’s gym-like environment and
the virtual player are written by Python 3.6. At the same time,
we adopt TFLearn 1.5.0 [45] to build the A2BR’s NN and
TensorFlow 2.4.0 [46] to implement the training workflow.
We set inner loop’s learning rate α = 10−4, outer loop’s
learning rate β = 10−3, virtual player rollout M = 20.
Meanwhile, we use Adam [47] to optimize the model.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 9

```text
HUANG et al.: LEARNING TAILORED ABR ALGORITHMS TO HETEROGENEOUS NETWORK CONDITIONS
2493
TABLE II
RESULTS OF EXPERIMENT IN DIFFERENT VEHICLES, SUMMARIZED IN VMAF [22] AND STALL TIME
Fig. 6.
Our virtual player focus on the RTT dynamics (right side), which
leads to better simulation results.
2) Testbed: We build a trace-driven “gym”-like [48] simula-
tor to train and validate A2BR w.r.t various network datasets
and video sets. The simulator is pragmatically implemented
based on various state-of-the-art ABR virtual simulators
[14], [49]. Moreover, we integrate round trip time (RTT) into
the simulator for improving the accurateness of throughput
measurement.
3) Simulator Fidelity: Now we show the strength of our
proposed virtual player. Previous studies demonstrate that
the used congestion control algorithm can impact the per-
formance of ABR algorithms due to the cross-layer effects,
as one of the better solutions is to faithfully measure the
round-trip propagation time at each time [50]. At the same
time, round trip time (RTT) is also observable, since the
video client can estimate the current RTT via estimating
time-to-first-byte (TTFB) or response time [4]. To that end,
we apply the RTT dynamic module to the simulator for
enhancing the throughput prediction. We conduct 4 real-
world experiments to prove the effectiveness of our simulator.
Specifically, we propose a Round-Robin ABR algorithm that
picks the bitrate orderly and uses the algorithm to collect
the information for each chunk, such as download chunk
size, download time, and current RTT. After finishing the
video session, we compute the throughout for each bitrate
using RTT or not using RTT respectively. Note that we finish
the experiment in stationary network environments, in which
their network capacity does not change rapidly. Results are
illustrated in Figure 6. We can see that estimating throughput
with RTT performs much better than that not using the
RTT metric.
4) ABR Baselines: We select several representational ABR
algorithms, which include heuristics and learning-based.
All the baselines are retrained or tuned for fitting each
experiment.
• BOLA [51]: a popular buffer-based heuristic that turns
the ABR problem into a utility maximization problem and
solves it by using the Lyapunov function.
• RobustMPC [8]: the state-of-the-art heuristics which con-
sider both the buffer occupancy and throughput predictions
and maximize the QoE by solving an optimization problem.
BOLA and RobustMPC are still top-2 methods that are
widely deployed in industries [4], [31].
• Fugu [2]: an ABR algorithm that leverages deep neural
network (DNN) to estimate download time for each chunk,
and uses model predictive control (MPC) to make decisions
according to the estimated values. We retrain the DTP model
of Fugu with partial information since it requires some TCP
metrics which is not fully logged in the dataset.
• Pensieve [11]: an RL-based algorithm which takes the
former network status as states and optimizes itself with
various network conditions using A3C method [52]. In this
work, we retrained Pensieve with our videos, datasets, and
QoE metrics.
B. Case Study: Different Vehicles
First, we evaluate A2BR and existing ABR algorithms in
the personalized network scenarios which consider the various
type of vehicles, including the car, bus, ferry, and metro.
1) Network and Video Settings:
For the training set,
we adopt a Markovian model where each state represented
an average throughput in the range of 0.1-6Mbps [11]. For
each epoch, we randomly sample trajectories with different
initial parameters and take them as the virtual personalized
scenario. In the online stage, we use HSDPA [20], a well-
known 3G/HSDPA to continually train the meta-model. The
network scenarios are naturally categorized into bus, car, ferry,
and metro. Meanwhile, we use EnvivioDash3 to evaluate
existing algorithms, where the video chunks are encoded as
{0.3, 0.75, 1.2, 1.8, 2.8, 4.3} Mbps [4]. Besides that, we opti-
mize A2BR with the quality-aware QoE metric QoEv, which
is constructed by video quality, rebuffering time, positive and
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 10

```text
2494
IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022
negative smoothness [14] (Eq. 17). In this experiment, we set
the maximum buffer size = 60 seconds.
QoEv = αv
N

n=1
q(Rn) −βv
N

n=1
Tn
+ γv
N−1

n=1
[q(Rn+1) −q(Rn)]+
−δv
N−1

n=1
[q(Rn+1) −q(Rn)]−
(17)
Here αv, βv, γv, δv are the parameters to describe their
aggressiveness. Followed by the original paper [14], we set
αv = 0.8469, βv = 28.7959, γv = 0.2979, δv = 1.0610.
Furthermore, for the sake of fairness, we also comparing the
A2BR with additional ABR approaches:
• Oboe [10], an auto-tuning mechanism that detects changes
in network conditions and adjusts ABR’s hyper-parameters
according to the configured map. Since the official imple-
mentation of Oboe is not publicly available, we have tried
our best to reproduce Oboe. For more detail please refer
to [53].
• Comyco [14], a quality-aware ABR scheme that leverages
imitation learning to improve the policy. We adopt the
pre-trained model provided by the authors.
2) A2BR vs. Existing Algorithms: We list the comparison
results in Table II, where the video quality is measured as
VMAF [22]. Here we can see that A2BR gains the highest
VMAF score while guaranteeing the lowest stall time in Car
and Bus scenarios. In particular, A2BR improves the average
VMAF by up to 12.6% and reduces the average stall time
by 78.8% compared with RobustMPC. A2BR also performs
better than Pensieve with the average VMAF of up to 12.6%
and the stall time of up to 69.3%. Furthermore, we observe that
although A2BR doesn’t achieve the best performance on both
VMAF metric and stall time in the Ferry and Metro network
scenario. Here we make a deeper analysis as follows:
1 Our first observation is A2BR reaches the lowest stall
time among all candidates and its VMAF comes only last
followed by BOLA. However, BOLA performs 1.1 ×−2.8×
higher stall time than that of A2BR, which is surely a con-
siderable price. In particular, BOLA often occurs rebuffering
events (i.e. 5.68% in terms of the stall ratio) under the Ferry
scenario. With further analysis, we observe that the network
throughput of the Ferry scenario is highly variable. Traditional
model-based approaches RobustMPC estimates the throughput
cautiously, requesting chunks at median-level bitrates with
keeping a medium-sized playback buffer. While BOLA mainly
takes current buffer size as inputs, failing to perceive heavy
ramp-down or ramp-up on the throughput. Hence, BOLA
strongly prefers HD videos but occurs a high stall ratio in
the Ferry scenario. In contrast, A2BR attempts to reduce
the rebuffering time rather than picking chunks with higher
bitrates. Comparing the performance of A2BR and Pensieve,
we can see that A2BR maintains the behaviors on average
quality but further decreases 1.69% on relative time stalled.
2 Second, comparing A2BR with Fugu in 4 scenarios,
we observe that, although Fugu leverages accurate prediction
to exceed RobustMPC, Fugu also underperforms A2BR in
low-speed vehicles, such as the car and bus. In such sce-
narios, accurate throughput prediction hardly influences QoE.
While Fugu almost matches the performance of A2BR on
both VMAF and stall ratio, which indicates the strength of
throughput prediction.
3 Finally, Oboe and Comyco show similar behavior over
all considered scenarios, i.e., gaining higher video quality but
slightly increasing the risk of rebuffering. The average time
stalled for A2BR is 62% lower than Comyco and 65% lower
than RobustMPC on the car scenario. One of the reasons
is that these schemes heavily depend on shortening the gap
between the network distributions of the training set and the
test environment. Same conclusions have also been observed
in the results of Pensieve. A2BR employs the online learning
phase to “understand” and vary current network conditions,
which eventually yield better performance.
C. Case Study: User-Personalized Networks
Next, we compare the performance of A2BR with baselines
in the user-personalized network conditions.
1) Network and Video Settings: We use the Puffer net-
work dataset [2], which includes 580,708 real-world wired
network environments collected from 28089 unique users.
We randomly sample 1000 unique users from the dataset
as the user-personalized network dataset. Each user contains
at least 30 unique network traces and each trace lasts over
300 seconds. We split the dataset into two groups, where
80% of the dataset for training and 20% of the dataset
for testing. Considering the wide range of users’ network
bandwidth, we use a 4K DASH dataset provided by Quinlan
and Sreenan [54] as the video description. The videos are
encoded at 13 bitrate levels, ranging from 0.235Mbps to
40Mbps (i.e., 40Mbps, 25Mbps, 15Mbps, 4.3Mbps, 3.85Mbps,
3Mbps, 2.35Mbps, 1.75Mbps, 1.05Mbps, 750Kbps, 560Kbps,
375Kbps, 235Kbps). We set μ = 40, ρ = 1 to balance the
conflicting goals in QoE (Eq. 1), which is consistent with
the maximum bitrate of the video. In this part, we set the
maximum buffer size as 40 seconds.
2) A2BR for Different Users: To better understand the
A2BR’s performance on each user, we report the detailed QoE
breakdown of ABR algorithms over top-9 user-personalized
network conditions in Figure 7, in which the user id represents
the user logged in the Puffer dataset. As shown, BOLA per-
forms well in fast-network scenarios with a small bandwidth
jitter, such as user No. 897 and 3805. Especially in user
No. 3805, BOLA even achieves the same performance com-
pared with A2BR. While it fails to work well in slow-network
scenarios, e.g., user No. 1871. One of the underlying reasons
is that existing heuristics, including BOLA and RobustMPC,
require proper parameter settings to vary different network
conditions. Although Oboe [10] considers using an auto-tuning
method to help prior ABR algorithms for fitting different
throughput regimes, it lacks fast adaptation ability. Specifi-
cally, Oboe adopts the offline mapping method to generate
tailor-made ABR strategies for each network state. However,
considering that computing the best parameter configuration
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 11

```text
HUANG et al.: LEARNING TAILORED ABR ALGORITHMS TO HETEROGENEOUS NETWORK CONDITIONS
2495
Fig. 7.
Comparison results of user-personalized network conditions. In detail, we select top-8 users among 1000 unique users from the Puffer network
dataset. Results are plotted with the CDF of QoE metrics.
Fig. 8.
Comparing the performance of A2BR with existing ABR
approaches in the user-personalized network conditions. (Primary experi-
ment: 650 stream-hours, Slow-network users: 117 stream-hours.)
for one network state takes about 12 seconds on a single
core, computing a user-personalized network condition will
take approximately 3 hours to explore with 1 core [10]. Thus,
it’s quite impractical to online map the best parameter for
each user. The same conclusions are also observed in lifelong
learning-based ABRs such as Comyco [24] and Fugu [2].
Comyco requires an hour to retrain the global policy as Fugu
lasts a day to refresh the model. Especially, both Comyco
and Fugu are interested in providing good video delivery QoE
for all users instead of on average. In Figure 7 we can see
that Pensieve does perform well across all considered network
scenarios while it seldom performs the best performance
among all baselines. In contrast, A2BR rivals or outperforms
other ABR schemes for most users in 20-shot.
3) A2BR vs. Baselines: Figure 8(a) shows the QoE break-
down of A2BR and recent baselines. The results are evaluated
on 650 stream-hours of network data. The performance gain in
QoE between A2BR and existing heuristic baselines is approx-
imately 51% (BOLA) and 21% (RobustMPC). As expected,
we also find that A2BR also outperforms recent learning-
based approaches, with the improvements on QoE of 12%
on Pensieve and 21% compared with Fugu. It makes sense
since existing ABRs didn’t consider the input process, while
such schemes will eventually fail if the current personalized
network behaves differently from the fixed training network
set. What’s more, we report the breakdown results performing
Fig. 9.
Demonstrating bad cases of A2BR. A2BR perform even worse than
before if continually trained over such network conditions.
on the slow network users, where the users have an average
throughput of less than 10Mbps. Such typical low-bandwidth
scenarios are quite challenging for ABR algorithms [5].
As shown in Figure 8(b), we can see a significant benefit
from using meta-RL for fast adaptation. Especially, the gap
between A2BR and Pensieve widens to 51% for average QoE.
One of the reasons is A2BR pays more attention to avoiding
stall time (0.26% vs. 0.49%), which is 1× lower than that
of Pensieve. Another possible reason is that, for most network
conditions in the Puffer dataset, the ABR algorithm can blindly
pick the chunk with the highest bitrate if the current mea-
sured throughput is significantly sufficient for downloading
all bitrate levels [2]. Hence, recent RL technologies lack
sufficient generalization abilities to handle such a “large”
action space, i.e., 13 bitrate levels, which is 2× larger than the
original version [11] A2BR can solve this issue via learning
environments in situ.
4) Deep Dive: Upon analyzing the advantage of A2BR,
we investigate the lower bound of the proposed scheme,
i.e., in which scenario that A2BR performs worse than
we expected? Figure 9 shows two bad cases of A2BR.
Case A (Figure 9(a)) indicates that A2BR doesn’t reach the
best QoE among all ABR algorithms. Similar to user No.
897 in Figure 7, the ABR algorithm only needs to take
the current buffer as the input to control such networks,
since its network throughput is highly variable, which has
negative impacts on QoE. A2BR cannot learn such a complex
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 12

```text
2496
IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022
Fig. 10.
Comparison of average normalized bitrate and stall ratio in 4G and 5G. Error bars show 95% confidence intervals.
logic in rather few-shot. Moreover, Case B (Figure 9(b))
shows a good network condition, as most ABRs achieve
maximum QoE. A2BR keeps exploring environments during
the online phase, which may lead to the fair but not the best
performance.
D. Case Study: 4G and 5G
In this part, we set up an experiment to understand how
A2BR performs in different wireless networks such as 4G and
5G, and how about walking or driving in those networks.
1) Network and Video Settings: We take the Lumos5G
dataset [21], containing 121 5G and 175 4G throughput
traces, collected at 1-second granularity. As suggested by [56],
we formally categorize the network conditions into 4 types,
i.e., 4G with walking, 4G with driving, 5G with walking as
well as 5G with driving. Considering the wide range of 5G’s
bandwidth, we use a 4K video encoded as {20, 40, 60, 80, 110,
160}Mbps [57]. Motivated by the prior study [56], we also
modify the QoE metric μ = 160, ρ = 1, where μ is often
set as the maximum number of bitrate levels of the 4K video.
Here we configure the maximum buffer occupancy as 60 sec-
onds. Same as §V-B, we take Comyco [14] as the baseline.
Note that Comyco is retrained with the aforementioned QoE
objective. Besides, considering that the general linear-based
reward function (Eq. 1) might hardly map the actual QoE for
4K videos [23], [56], we leverage a more realistic QoE model,
i.e., ITU-T Rec. P.1203 [55] for evaluating the performance.
2) Bitrate-Stall Analysis: We summarize the experimen-
tal results according to the relationship of stall time and
normalized bitrate, in which the normalized bitrate is com-
puted as
Rk
160. Notably, results show that our proposed
BOLA performs much better than the results of the previous
work [56] (2% vs. 5% on stall ratio). Due to the minor
incorrect settings in terms of the experimental setup,1 we have
re-evaluated BOLA with tuned parameters to achieve the best
average performance across all network traces.
Figure 10 reports the comparison results of existing ABRs,
including heuristics and learning-based schemes. Recall that
A2BR is only tuned for 20-shot. We see that A2BR can
provide outstanding performance in terms of high video bitrate
and low stall ratio. Specifically, Figure 10(a) demonstrates
that A2BR outperforms heuristics on the average bitrate of
2.9%-6% and average stall reduction of 42%-70%. One of
the underlying reasons is that the bitrate ladder provided by
the 4K video is not adequate for 4G networks. Commonly,
the average bandwidth of 4G networks is lower than 40Mbps,
while most bitrate levels are larger than the average bandwidth.
To this end, how to construct a proper bitrate ladder for
different network conditions is an interesting topic but out
of scope here [58]. We will jointly consider the bitrate ladder
construction and ABR implementation in future work.
Figure 10(b) and 10(c) show that A2BR increases the bitrate
by 2%-5% and heavily reduces the stall ratio by 6%-23% com-
pared with state-of-the-art ABR Fugu [2] in the 4G scenario.
Furthermore, Figure 10(d) shows a significant performance
gap between the recent ABR scheme and A2BR, since recent
work suffers from either low video bitrate (e.g., BOLA and
RobustMPC) or high stall ratio (e.g. Pensieve and Comyco).
From Figure 10(f) and Figure 10(e), we find the same conclu-
sion of prior work [56]: NN-based ABR scheme such as Pen-
sieve and Comyco fails to maintain the high performance in
5G network scenario because they often suffer from very high
stall ratio. In contrast, the aforementioned situation has been
rectified by A2BR: it shows a significant decrease (i.e., 69%
and 80% on average) of video stall in driving and walking
1See details in https://github.com/SIGCOMM21-5G/artifact/issues/8
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 13

```text
HUANG et al.: LEARNING TAILORED ABR ALGORITHMS TO HETEROGENEOUS NETWORK CONDITIONS
2497
TABLE III
QOE PERFORMANCE COMPARISON OF DIFFERENT ABR ALGORITHMS. RESULTS ARE CALCULATED BY ITU-P.1203 [55]
Fig. 11.
Comparing A2BR with existing QoE-driven ABR algorithms on HSDPA and FCC networks traces. Results are normalized against the performance
of Pensieve. The error bars show std from the average. We consider three types of QoE metrics that described in §V-E2.
scenario compared to Pensieve, as the average bitrate of it only
performs 2%-4% lower than that of Pensieve. Such decreases
are indeed acceptable because each algorithm performs with
the normalized bitrate of at least 0.9 in 5G scenarios.
3) ITU-T Rec P.1203 QoE Analysis: In addition, we cal-
culate an estimated MOS for each video session via ITU-T
P.1203 QoE model [55]. As suggested by previous work [59],
we use mode 0, which fully considers 6 metrics, such as
selected bitrate, video codec, video resolution, frame rate,
starting time of stall events, and stall duration. During the
evaluation phase, we record the detailed playback behavior
for each chunk and ABR algorithm. Then we feed the play-
back logs to ITU-T P.1203 Standalone Implementation2 and
obtain the final MOS scores. To better understand the quality
from different perspectives, we take 3 MOS scores, involving
i) O.23, indicating perceptual stalling indication; ii) O.35,
meaning visual coding quality score for the entire session;
iii) O.46, representing media session quality score, aka. final
QoE score. All the MOS scores are computed as a single score
on a 1-5 quality scale. The comprehensive instruction of ITU-T
P.1203 can be found in [19].
Table III reports the detailed comparison results of A2BR
and existing ABR algorithms over 4G and 5G network
conditions, where the values are depicted as avg. ± std..
There are three key takeaways from these results. First,
we find that A2BR either rivals or surpasses the performance
of the best existing ABR algorithm on each MOS score
and network considered. Especially, in comparison to the
2https://github.com/itu-p1203/itu-p1203
closest competitive scheme Fugu, A2BR provides 10.0% (4G:
25.93%, 5G: 0.53%) on average O.46 score (i.e., overall QoE
score). In our opinion, A2BR obtains its outstanding perfor-
mance since it pays more attention to avoiding stalls, as it
improves 23.3%-72.4% on average O.23 score (i.e., overall
stall score) compared with baselines.
Second, A2BR not only reaches the best average perfor-
mance but also attains the lowest variance with an average
O.46 score compared to existing ABR schemes. Here the key
reason is that A2BR prefers smooth rate adaptation rather than
requesting chunks with the highest bitrate level (e.g. Pensieve).
Particularly, Comyco reaches second place in terms of QoE
variation (1.04), but it only ranks fourth on average QoE (2.43)
among 6 candidates. Compared to the best scheme A2BR,
Comyco should focus on reducing the stall ratio in 5G network
conditions. A strawman solution is to set the rebuffering
penalty as a larger value, e.g., μ = 320. However, the increased
rebuffering penalty also leads to the more conservative bitrate
selection strategy on the 4G network. Thus, the better solution
for Comyco is to follow A2BR, i.e., learning policies with
different network conditions separately (§III-B).
Finally, to our surprise, we observe that Pensieve performs
poorly on O.46 score, even though it stands for the worst
scheme among all ABR schemes. This is because Pensieve
obtains the lowest score on O.23 (i.e., stall). Such results
indicate that the distribution shift effect is positively mislead-
ing the algorithm to local optima [60]. A2BR performs well
over all networks considered since it can continually learn the
strategy to vary current network environments.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 14

```text
2498
IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022
Fig. 12.
Performance of A2BR and recent ABRs in Dash.js. Results are reported as normalized QoE (QoE/QoEmax).
E. Case Study: Varying User Preference
Previous experiments assume that the QoE of a user is
roughly even with the others [2], [8], [11], [14]. Based on
the assumption, traditional ABRs are optimized toward a fixed
QoE model, and these approaches will perform poorly if the
QoE metric is changed [12]. However, recent studies argue
that QoE preferences vary with users because each user has
their viewing interests. Hence, the ABR algorithm should be
optimized by considering QoE diversity. In this part, we try to
answer: can A2BR also tame the complexity of various QoE
preferences in relatively few-shot?
1) Enhancement for Multiple QoE Preferences: We con-
sider two enhancements to the training algorithm which enable
A2BR to better understand QoE preferences. The detailed
modification is described in Figure 11(a). The first change
is that we incorporate QoE parameters μ, ρ into the state
representation. During training, for each session, we ran-
domly reset the parameters and obtain the reward score
according to the selected parameters. Second, we apply a
fully-connected layer with 64 neurons to the A2BR’s NN
for extracting the high-dimensional features from the QoE
parameters.
2) Experimental Settings: At the offline stage, we train
A2BR via Pensieve training dataset [62]. At the online stage,
we continually train the meta-policy over the traces which
are randomly selected from the HSDPA and FCC datasets.
Training time lasts 20-shot. In light of MPC’s evaluation
settings [8], we compare the performance of ABR algorithms
under 3 sets of QoE weights: i) “Default” (μ = 4.3, λ = 1),
ii) “Conservative” (μ = 8.6, λ = 1), and iii) ”Stable” (μ =
4.3, λ = 4.3). In this experiment, RobustMPC is optimized
by the actual QoE preference. We adopt Pensieve as the
pre-trained model that trained with the default QoE set.
3) Effectiveness Analysis of A2BR: Figure 11 provides a
summary to illustrate the average normalized QoE that each
scheme achieves on HSDPA and FCC datasets. As expected,
A2BR efficiently learns the individual QoE requirements and
outperforms ABR approaches: it rapidly obtains 5.1% QoE
gains over HSDPA and 5.0% QoE gains over FCC com-
pared with A2BR-meta (i.e., the initial meta-policy of A2BR)
in 20-shot. Moreover, another observation is that heuristics
like RobustMPC fails to handle all QoE preference settings.
Especially in the “Stable” QoE set, RobustMPC never picks
the chunk with the highest bitrate during the entire session.
We reason that RobustMPC solves a QoE maximization prob-
lem over a horizon of only 5 future chunks. While due to the
large penalty from switching bitrates (i.e., 4.3), the best trajec-
tory that MPC planned seldom contains any bitrate changes.
Widen the prediction horizon can not perfectly solve the
problem for MPC since its sensitivity to throughput prediction
errors and the length of the optimization horizon [8], [11].
It proves that there’s still plenty of room for improvement
by developing outstanding planning/decision strategies for
heuristics. One of the possible ways is to joint deep learning
and model-based planning method for accurate decision [63].
In addition, we can see that Pensieve performs poorly except
for the default QoE set (μ = 4.3, ρ = 1.0) because it is trained
via a fixed QoE objective. Thus, Pensieve can not adjust itself
to various objectives such as the “Conservative” and “Stable”
sets.
F. Real-World Deployment
We establish a full-system implementation to evaluate
A2BR and other ABR approaches on Dash.js [4]. Specifically,
the system consists of a video client, a video server, and an
A2BR decision server. For each chunk, the video client reports
all the features like a state to the A2BR decision server. The
decision server then sends the bitrate level back to the client.
The client requests the chunk from the video server with the
bitrate level suggested by the decision server. When the session
ends, the decision server starts to restore the network traces
from previously collected states, then it virtually rolls out
several trajectories using a virtual player, and updating the NN
according to the “real” and “fake” trajectories (see §IV-C). The
network condition is configured by Mahimahi [61] with the
randomly selected traces from HSDPA dataset [20]. We adopt
TCP-BBR [64] as the basic TCP congestion control algorithm
and repeatedly replay the videos named EnvivioDash3 [4]
with all the evaluated ABR algorithms over all considered
network conditions. We report the average “learning curve”
of A2BR for each video session. Figure 12(a) shows the per-
formance of A2BR and existing ABR schemes (i.e., Pensieve
and RobustMPC) in the emulation environment, we see that
A2BR (i.e., meta policy) performs worse than Pensieve and
RobustMPC at the beginning of the online stage. After playing
the video 8 times, A2BR suddenly learns the better policy
that matches the behavior of baselines. After that, we see that
A2BR incrementally improves itself to achieve the best results
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 15

```text
HUANG et al.: LEARNING TAILORED ABR ALGORITHMS TO HETEROGENEOUS NETWORK CONDITIONS
2499
among candidates, i.e., Pensieve: (7.8%↑) and RobustMPC:
(8.5%↑).
Furthermore, we conduct a real-world experiment over two
representative network scenarios, including public WiFi and
wired network. We apply the video client and A2BR server
on the laptop (MacBook Pro, 64GB RAM), and establish a
video server on the AWS. For the first experiment, we connect
a public WiFi and repeatedly play the video 20 times. Results
are shown in Figure 12(b). Notably, this scenario is a typical
network condition over which the basic network “trace” is
dynamically changed rather than fixed during the phase. Dif-
ferent from the results in the emulation tools, we find that
Pensieve’s conservative policy leads to poor generalization
ability: it doesn’t work well on networks dissimilar to the
networks it has trained on [2], [65]. A2BR, trained 20 times,
outperforms other ABR algorithms on average QoE improve-
ments of 9.6% (RobustMPC) and 12.8% (Pensieve), which
yields the effectiveness and generalization capacity.
The second real-world experiment is established over the
wired network, where the average bandwidth is always suffi-
cient for picking the chunk with the highest bitrate. We demon-
strate the results in Figure 12(c) and find that Pensieve still
exhibits the worst behavior because it performs like running on
slow-path networks. By contrast, RobustMPC runs perfectly
well in the high throughput and low variance network condi-
tions. Unfortunately, we can find that A2BR’s performance is
continually enhanced by 5.6% but fails to reach the optimal
score after 20 trials. The reason is similar to the fact that we
have figured out in §V-C4: A2BR is incrementally improved
by encouraging exploration, which might heavily influence the
ABR performance.
VI. ABLATION STUDIES
A. Choice of Meta-Learning Methods
We make a comparison of A2BR with different meta-
learning strategies, such as Pearl [66], Reptile [67] and
FedAvg [68], and the vanilla RL training methodology [11].
Pearl is an off-policy meta-RL algorithm that takes proba-
bilistic embeddings to determine the latent embedding of the
current environment. Considering A2BR is working in the
discrete action spaces (§IV), we use double Q-learning [69] as
the Pearl’s RL training method. In the offline training stage,
the latent embedding is directly estimated by the average and
standard deviation throughput of the entire session. While
in the online stage, the embedding is computed from the
throughput observed of the past five chunks. Reptile is one
of the meta-learning algorithms which repeatedly samples
a task, training on it, and updating the initial parameters
towards the parameters learned on that task. In addition, recent
work reveals that FedAvg and Reptile are quite similar to
each other since FedAvg can be viewed as a special case
of Reptile if the learning rate equals 1 [70], [71]. Hence,
we treat FedAvg as a linear combination of a naive baseline.
We evaluate ABRs on the same validation set every 300 epochs
and report the learning curve in Figure 13. A2BR trains faster
and performs slightly better than others. Comparing A2BR
with Pearl, we find Pearl typically converges quickly because
Fig. 13.
Comparing A2BR with existing meta-RL methods, including Pearl,
Reptile and Fed-Avg.
Fig. 14.
A2BR with different rollout times M.
Pearl works based on a sample-efficient off-policy method.
However, it fails to obtain better final performance compared
with on-policy meta-RL A2BR. What’s more, compared to
Reptile, both the convergence speed and final performance
of A2BR are significantly improved, which indicates the
effectiveness of the offline stage. To sum up, MAML is the
most suitable method among existing meta-RL algorithms for
our work.
B. Choice of Different Rollout M and Learning Epochs
The higher M indicates better sample efficiency since most
trajectories will be sampled from the virtual player and the
environment collector. However, it also brings out the risk
that too many virtual trajectories may be overkill for meta
updating. We compare A2BR with different rollout times M,
which includes {0, 5, 10, 20, 100}, over the Puffer dataset.
Note that A2BR doesn’t use the virtual player for improving
learning efficiency when M = 0. In other words, it reflects the
performance of using MAML solely at the online stage. The
results of training A2BR in 100-shot are shown in Figure 14.
We leave three notes here. First, A2BR reaches the best
performance when M
= 100. However, it takes 5× on
computational overhead but only improves less than 1% on
average QoE compared with M = 20. Thus, we confirm that
M = 20 is a sufficient parameter setting for the online stage.
Second, compared to Pensieve which doesn’t adopt meta-
policy techniques, we see that A2BR (M = 20) consistently
improves the performance by 6% in 10-shot, 7.8% in 20-shot,
but only 8% in 50-shot. Such minor improvements (i.e., 0.2%)
between 20-shot and 50-shot motivates us to continually train
A2BR in 20-shot at the online stage.
Finally, we find that A2BR with M = 0 obtains 3.5%
improvements on average QoE compared to Pensieve in
20-shot. It proves that A2BR can also provide acceptable
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 16

```text
2500
IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022
Fig. 15.
Comparing performance of 1-step MPC and NN-based ABR
algorithm. The results contain CPU, memory consumed, inference time, and
energy cost.
TABLE IV
A2BR WITH DIFFERENT ROLLOUT M
improvements without using a virtual player to replay the
environment experienced. Unfortunately, it only gains 4%
improvements compared with Pensieve in the next 50-shot,
which is indeed a minor improvement compared with using
virtual play technologies.
C. Computational Cost for Online Learning
We follow the calculation method described in [72] and
compute the number of floating point operations (FLOPs) of
A2BR on both inference and backpropagation operation [73]
in Table IV. A2BR with M = 100 takes almost 5× computa-
tional overhead compared with M = 20. Hence, we set M =
20 for balancing the trade-off among the sample efficiency,
model accuracy, and computational cost. Most notably, this
cost is rather small, only 0.86% of the consumption inferred
by the state-of-the-art image recognition model MicroNet [74].
Moreover, we deploy the NN model of A2BR to the
mobile phones to investigate whether A2BR can work well
or not. In detail, we adopt an Android phone named Huawei
P20, with 128GB of internal storage and 4GB of RAM.
We modify Kuaishou’s production video player to support
NN inference via a self-developed NN tool, namely YCNN
(a Tensorflow-Lite [75] like NN API). Figure 15 demonstrates
the performance of two ABR schemes, i.e., 1-step MPC and
NN-based scheme, in which these two schemes have been
performed in the same video and network environment for
at least two hours. The NN-based scheme uses the same
architecture of A2BR, and it only makes inference instead
of continual learning. As shown, we can see the energy
cost of the two schemes is quite similar. Meanwhile, the
NN-based scheme runs slightly higher than 1-step MPC in
terms of CPU utilization and memory consumed. Such minor
costs have negligible impacts on today’s mobile phones [76].
Moreover, the extra-low overhead on inference time proves
that applying sophisticated feature engineering is useful for
both meta-learning and online deployment.
VII. RELATED WORK
In this section, we summarize recent ABR algorithms.
Existing ABR algorithms are generally categorized into three
types: heuristics, learning-based, online-learning based, and
preference-aware ABR approaches.
A. Traditional ABRs
Heuristic-based ABR methods often adopt critical fea-
tures or domain knowledge, such as throughput prediction
(E.g., FESTIVE [6] and PANDA [77]) and buffer occupancy
control (E.g., BBA [7] and BOLA [51]), for choosing the
proper bitrate for the ABR task. However, such approaches
require accurate bandwidth estimation or suffer from long-term
bandwidth fluctuation problems. Then, MPC [8] picks the
next chunks’ bitrate by jointly considering throughput and
buffer occupancy. Nevertheless, MPC is sensitive to its
parameters since it relies on well-understanding different
network conditions. To deal with the aforementioned short-
comings, Oboe [10] is an auto-tuning method to tune the
traditional heuristic methods to achieve better performance
in different network settings. Moreover, in the live streaming
field, MultiLive designs a quality model and proposes a rate
adaptation algorithm for multi-party scenarios [78]. However,
such heuristics will perform unstable if the current network
condition doesn’t meet the presumptions of the fundamental
principle of the proposed ABR algorithm.
B. Learning-Based ABRs
By contrast, learning-based schemes take raw observa-
tions as the input, aiming to train a NN from the clean
slate via various learning methods, such as imitation learn-
ing [14], A3C [11], PPO [23], and ACKTR [79]. For example,
Mao et al. [11] propose Pensieve, which leverages the deep
reinforcement learning (DRL) method to generate a strategy
towards higher reward feedback, in which the reward function
is represented as the simple weighted sum of bitrate, rebuffer-
ing, and smoothness. Bentaleb et al. [59] propose AMP that
encompasses techniques for bandwidth prediction and model
auto-selection, which is specifically designed for low-latency
live steaming with chunked transfer encoding. Stick is a fusion
approach that fuses the learning-based and the conventional
buffer-based approach [12] for not only achieving higher per-
formance but also reducing the computational overhead. More-
over, to make the learning-based ABR scheme more practical,
Meng et al. [80] proposes Pitree to distill the ABR policy into
a decision tree-based model. Meanwhile, Lumos [81] leverages
the regression tree for accurate throughput prediction, leading
to better QoE performance. Such approaches are trained or
optimized in the offline setting, that is, using a fixed network
distribution. Nevertheless, they fail to perform well if the
online network distribution is different from the training set.
C. Online-Learning Based ABRs
Several online-learning-based ABR schemes have been pro-
posed in recent years. OnRL [41] adopts federated learning to
continually update its strategy for real-time communication.
Oboe [10] and Puffer [2] dynamically update the configuration
map or NN model according to current bandwidth capacities
periodically. L2A-LL [82] uses Online Convex Optimiza-
tion (OCO) to make decisions for low-latency live streaming.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 17

```text
HUANG et al.: LEARNING TAILORED ABR ALGORITHMS TO HETEROGENEOUS NETWORK CONDITIONS
2501
However, recent work failed to consider a personalized net-
work environment with the fast adaptation requirement.
D. Preference-Aware ABRs
Elephanta [83] is the first QoE diversity perception approach
for edge clients by adjusting the parameters during the ses-
sion. Elephanta models the video streaming process as a
renewal system, which enables it to adapt to QoE diversity
online. DAVS [84] is an imitation learning-based approach
that considers the user’s viewing preference for making the
method adapt to the QoE diversity. Zuo et al. [85] propose
Ruyi, an off-policy RL-based video streaming system that
incorporates preference awareness into both the QoE model
and the ABR algorithm. Ruyi is optimized by a variant of
the Deep Q-learning algorithm with the experience replay
technique [86]. However, recent schemes lack the ability to
fast adapt to specific QoE preferences.
VIII. CONCLUSION AND FUTURE WORK
We have proposed A2BR, a novel meta-RL ABR approach
to fast adapts the personalized network conditions. We divided
the training process into two stages, aiming to meta-train an
initial model in the offline stage, and continually leveraged
domain knowledge to adapt tailor-made networks within few-
shots in the online stage. Experimental results on several rep-
resentative network scenarios revealed that A2BR can quickly
generate tailor-made policies within 20 shots.
In this work, we only discuss the performance of A2BR in
the VOD (video on demand) scenario, where the maximum
buffer size is often set above 30 seconds. While another
popular streaming scenario is the live streaming scenario,
in which the buffer occupancy is considered as a penalty, often
sized below 3 seconds. Ideally, deploying A2BR in live (or
low latency) streaming scenario is quite challenging, since
i) measuring throughput becomes tough due to the application
limit [87], ii) we should design the decision algorithm by
considering lower playback buffer size [88], [89], and iii) the
lack of a faithful packet-level simulator rather than frame-level
solution [90] for live streaming. We plan to investigate A2BR
in the live streaming scenario in future work.
Furthermore, we also believe that A2BR sheds light on
improving similar input-driven MDP (IMDP) tasks, such
as internet congestion control algorithms [33], schedul-
ing/offloading algorithms [42], [91], and so on. In these tasks,
an exogenous yet stochastic input process often affects the
dynamics of the system as well. For example, for congestion
control algorithms, heuristics like TCP-BBR and TCP-Cubic
can’t always perform well under all considered scenarios. Here
A2BR is a suitable scheme that allows the control strategy to
adapt to the environment faster.
ACKNOWLEDGMENT
The authors thank their colleagues from the Kuaishou
video transport and delivery group, including Dan Yang,
Yangchao Zhao, Yixuan Ban, and Kewei Zhu. They also thank
the anonymous reviewer for the valuable feedback. Special
thanks to their editors Prof. Zhu Han and Lei Liang for useful
suggestions.
REFERENCES
[1] Cisco.
(2017).
Cisco
Visual
Networking
Index:
Forecast
and
Methodology.
[Online].
Available:
https://www.cisco.com/
c/dam/en/us/solutions/collateral/service-provider/visual-networking-
index-vni/complete-white-paper-c11-481360.pdf
[2] F. Y. Yan et al., “Learning in situ: A randomized experiment in video
streaming,” in Proc. 17th USENIX Symp. Netw. Syst. Design Implement.
(NSDI), 2020, pp. 495–511.
[3] (2019). HTTP Live Streaming. [Online]. Available: https://developer.
apple.com/streaming/
[4] DASH. (2019). Dash. [Online]. Available: https://dashif.org/
[5] A. Bentaleb, B. Taani, A. C. Begen, C. Timmerer, and R. Zimmermann,
“A survey on bitrate adaptation schemes for streaming media over
HTTP,” IEEE Commun. Surveys Tuts., vol. 21, no. 1, pp. 562–585,
1st Quart., 2018.
[6] J. Jiang, V. Sekar, and H. Zhang, “Improving fairness, efficiency, and
stability in HTTP-based adaptive video streaming with festive,” TON,
vol. 22, no. 1, pp. 326–340, 2014.
[7] T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Watson,
“A buffer-based approach to rate adaptation: Evidence from a large
video streaming service,” in Proc. ACM Conf. SIGCOMM, Oct. 2014,
vol. 44, no. 4, pp. 187–198.
[8] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic
approach for dynamic adaptive video streaming over HTTP,” in
Proc. ACM Conf. Special Interest Group Data Commun., Aug. 2015,
pp. 325–338.
[9] P. K. Yadav, A. Shafiei, and W. T. Ooi, “QUETRA: A queuing theory
approach to DASH rate adaptation,” in Proc. 25th ACM Int. Conf.
Multimedia, Oct. 2017, pp. 1130–1138.
[10] Z. Akhtar et al., “Oboe: Auto-tuning video ABR algorithms to network
conditions,” in Proc. Conf. ACM Special Interest Group Data Commun.,
Aug. 2018, pp. 44–58.
[11] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video stream-
ing with pensieve,” in Proc. Conf. ACM Special Interest Group Data
Commun., Aug. 2017, pp. 197–210.
[12] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, “Stick:
A harmonious fusion of buffer-based and learning-based approach
for adaptive streaming,” in Proc. IEEE Conf. Comput. Commun.
(INFOCOM), Jul. 2020, pp. 1967–1976.
[13] Y. Sun et al., “CS2P: Improving video bitrate selection and adaptation
with data-driven throughput prediction,” in Proc. ACM SIGCOMM
Conf., Aug. 2016, pp. 272–285.
[14] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, “Comyco:
Quality-aware adaptive video streaming via imitation learning,” in Proc.
27th ACM Int. Conf. Multimedia, Oct. 2019, pp. 429–437.
[15] W. Li, J. Huang, S. Wang, S. Liu, and J. Wang, “DAVS: Dynamic-chunk
quality aware adaptive video streaming using apprenticeship learning,” in
Proc. IEEE Global Commun. Conf. (GLOBECOM), Dec. 2020, pp. 1–6.
[16] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal
bitrate adaptation for online videos,” IEEE/ACM Trans. Netw., vol. 28,
no. 4, pp. 1698–1711, Aug. 2020.
[17] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov,
“Proximal policy optimization algorithms,” 2017, arXiv:1707.06347.
[18] C. Finn, P. Abbeel, and S. Levine, “Model-agnostic meta-learning for
fast adaptation of deep networks,” in Proc. Int. Conf. Mach. Learn.,
2017, pp. 1126–1135.
[19] A. Raake,
M.-N. Garcia,
W. Robitza,
P. List, S. Göring,
and
B. Feiten, “A bitstream-based, scalable video-quality model for HTTP
adaptive streaming: ITU-T P.1203.1,” in Proc. 9th Int. Conf. Qual. Mul-
timedia Exper. (QoMEX), Erfurt, Germany, 2017. [Online]. Available:
http://ieeexplore.ieee.org/document/7965631/
[20] H. Riiser, P. Vigmostad, C. Griwodz, and P. Halvorsen, “Commute path
bandwidth traces from 3G networks: Analysis and applications,” in Proc.
4th ACM Multimedia Syst. Conf., 2013, pp. 114–118.
[21] A. Narayanan et al., “Lumos5G: Mapping and predicting commer-
cial mmWave 5G throughput,” in Proc. ACM Internet Meas. Conf.,
Oct. 2020, pp. 176–193, doi: 10.1145/3419394.3423629.
[22] R. Rassool, “VMAF reproducibility: Validating a perceptual practical
video quality metric,” in Proc. IEEE Int. Symp. Broadband Multimedia
Syst. Broadcast. (BMSB), Jun. 2017, pp. 1–2.
[23] T. Huang, R.-X. Zhang, and L. Sun, “Self-play reinforcement learning
for video transmission,” in Proc. 30th ACM Workshop Netw. Oper. Syst.
Support Digit. Audio Video, Jun. 2020, pp. 7–13.
[24] T. Huang et al., “Quality-aware neural adaptive video streaming with
lifelong imitation learning,” IEEE J. Sel. Areas Commun., vol. 38, no. 10,
pp. 2324–2342, Oct. 2020.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 18

```text
2502
IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, VOL. 40, NO. 8, AUGUST 2022
[25] Y. Zheng et al., “Enabling robust DRL-driven networking systems via
teacher–student learning,” IEEE J. Sel. Areas Commun., vol. 40, no. 1,
pp. 376–392, Jan. 2022.
[26] H. Mao, S. B. Venkatakrishnan, M. Schwarzkopf, and M. Alizadeh,
“Variance reduction for reinforcement learning in input-driven environ-
ments,” 2018, arXiv:1807.02264.
[27] M. T. J. Spaan, “Partially observable Markov decision processes,”
in Reinforcement Learning (Adaptation, Learning, and Optimization),
vol. 12, M. Wiering and M. Van Otterlo, Eds. Berlin, Germany: Springer,
2012, doi: 10.1007/978-3-642-27645-3_12.
[28] Z. Huo, Q. Yang, B. Gu, and L. Carin. Heng Huang, “Faster on-
device training using new federated momentum algorithm,” 2020,
arXiv:2002.02090.
[29] X. Jiang et al., “MNN: A universal and efficient inference engine,” in
Proc. Mach. Learn. Syst. (MLSys), 2020, pp. 1–13.
[30] T. Hospedales, A. Antoniou, P. Micaelli, and A. Storkey, “Meta-learning
in neural networks: A survey,” 2020, arXiv:2004.05439.
[31] T.-Y. Huang, C. Ekanadham, A. J. Berglund, and Z. Li, “Hindsight: Eval-
uate video bitrate adaptation at scale,” in Proc. 10th ACM Multimedia
Syst. Conf., Jun. 2019, pp. 86–97.
[32] Z. Meng, M. Wang, J. Bai, M. Xu, H. Mao, and H. Hu, “Interpreting
deep learning-based networking systems,” in Proc. Annu. Conf. ACM
Special Interest Group Data Commun. Appl., Technol., Archit., Protocols
Comput. Commun., Jul. 2020, pp. 154–171.
[33] S. Abbasloo, C.-Y. Yen, and H. J. Chao, “Classic meets modern:
A pragmatic learning-based congestion control for the Internet,” in Proc.
Annu. Conf. ACM Special Interest Group Data Commun. Appl., Technol.,
Archit., Protocols Comput. Commun., Jul. 2020, pp. 632–647.
[34] J. Schulman, X. Chen, and P. Abbeel, “Equivalence between policy
gradients and soft Q-learning,” 2017, arXiv:1704.06440.
[35] D. Ye et al., “Mastering complex control in MOBA games with deep
reinforcement learning,” 2019, arXiv:1912.09729.
[36] J. Li et al., “Suphx: Mastering Mahjong with deep reinforcement
learning,” 2020, arXiv:2003.13590.
[37] R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction.
Cambridge, MA, USA: MIT Press, 2018.
[38] A. Biswas and S. Agrawal, “First-order meta-learned initialization for
faster adaptation in deep reinforcement learning,” in Proc. NIPS, 2018.
[39] H. Zhang et al., “Loki: Improving long tail performance of learning-
based real-time video adaptation by fusing rule-based models,” in Proc.
27th Annu. Int. Conf. Mobile Comput. Netw., Oct. 2021, pp. 775–788.
[40] C. Liu, M. Xu, Y. Yang, and N. Geng, “DRL-OR: Deep reinforcement
learning-based online routing for multi-type service requirements,” in
Proc. IEEE Conf. Comput. Commun. (INFOCOM), May 2021, pp. 1–10.
[41] H. Zhang et al., “OnRL: Improving mobile video telephony via online
reinforcement learning,” in Proc. 26th Annu. Int. Conf. Mobile Comput.
Netw., Sep. 2020, pp. 1–14.
[42] H. Mao, M. Schwarzkopf, S. B. Venkatakrishnan, Z. Meng, and
M. Alizadeh, “Learning scheduling algorithms for data processing clus-
ters,” in Proc. ACM Special Interest Group Data Commun., Aug. 2019,
pp. 270–288.
[43] H. Mao, M. Schwarzkopf, H. He, and M. Alizadeh, “Towards safe online
reinforcement learning in computer systems,” in Proc. NeurIPS Mach.
Learn. Syst. Workshop, 2019.
[44] S. Huang and S. Ontañón, “A closer look at invalid action masking in
policy gradient algorithms,” 2020, arXiv:2006.14171.
[45] Y. Tang, “TF.Learn: TensorFlow’s high-level module for distributed
machine learning,” 2016, arXiv:1612.04251.
[46] M. Abadi et al., “TensorFlow: A system for large-scale machine
learning,” in Proc. 12th USENIX Symp. Oper. Syst. Design Implement.
(OSDI), vol. 16, 2016, pp. 265–283.
[47] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,”
2014, arXiv:1412.6980.
[48] G. Brockman et al., “OpenAI gym,” 2016, arXiv:1606.01540.
[49] H. Mao et al., “Park: An open platform for learning augmented com-
puter systems,” in Proc. Adv. Neural Inf. Process. Syst. (NIPS), 2019,
pp. 1–13.
[50] P. G. Pereira, A. Schmidt, and T. Herfet, “Cross-layer effects on training
neural algorithms for video streaming,” in Proc. 28th ACM SIGMM
Workshop Netw. Operating Syst. Support Digit. Audio Video, Jun. 2018,
pp. 43–48.
[51] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal
bitrate adaptation for online videos,” in Proc. IEEE 35th Annu. Int. Conf.
Comput. Commun. (INFOCOM), Apr. 2016, pp. 1–9.
[52] V. Mnih et al., “Asynchronous methods for deep reinforcement learning,”
in Proc. Int. Conf. Mach. Learn., 2016, pp. 1928–1937.
[53] T. Huang. (2022). Oboe Reproduce. [Online].
Available:
https://
github.com/godka/oboe-reproduce
[54] J. J. Quinlan and C. J. Sreenan, “Multi-profile ultra high definition
(UHD) AVC and HEVC 4K DASH datasets,” in Proc. 9th ACM
Multimedia Syst. Conf., Jun. 2018, pp. 375–380.
[55] W. Robitza et al., “HTTP adaptive streaming QoE estimation with
ITU-T rec. P. 1203: Open databases and software,” in Proc. 9th ACM
Multimedia Syst. Conf., Jun. 2018, p. 1203.
[56] A. Narayanan et al., “A variegated look at 5G in the wild: Perfor-
mance, power, and QoE implications,” in Proc. ACM SIGCOMM Conf.,
Aug. 2021, pp. 610–625.
[57] The
HDR
Channel.
(2021).
Real
4K
HDR
60fps:
LG
Jazz
HDR
UHD
(Chromecast
Ultra).
[Online].
Available:
https://www.youtube.com/watch?v=mkggXE5e2yk
[58] T. Huang, R.-X. Zhang, and L. Sun, “Deep reinforced bitrate ladders
for adaptive video streaming,” in Proc. 31st ACM Workshop Netw. Oper.
Syst. Support Digit. Audio Video, Jul. 2021, pp. 66–73.
[59] A. Bentaleb, A. C. Begen, S. Harous, and R. Zimmermann, “Data-driven
bandwidth prediction models and automated model selection for low
latency,” IEEE Trans. Multimedia, vol. 23, pp. 2588–2601, 2021.
[60] A. Agarwal, S. M. Kakade, J. D. Lee, and G. Mahajan, “On the theory
of policy gradient methods: Optimality, approximation, and distribution
shift,” J. Mach. Learn. Res., vol. 22, no. 98, pp. 1–76, 2021.
[61] R. Netravali et al., “Mahimahi: Accurate record-and-replay for HTTP,”
in Proc. USENIX Annu. Tech. Conf. (USENIX ATC), 2015, pp. 417–429.
[62] H.
Mao.
(Jul.
2017).
Pensieve-Traces.
[Online].
Available:
https://www.dropbox.com/sh/ss0zs1lc4cklu3u/
AAB-8WC3cHD4PTtYT0E4M19Ja?dl=0
[63] T. Huang and L. Sun, “DeepMPC: A mixture ABR approach via deep
learning and MPC,” in Proc. IEEE Int. Conf. Image Process. (ICIP),
Oct. 2020, pp. 1231–1235.
[64] N. Cardwell, Y. Cheng, C. S. Gunn, S. H. Yeganeh, and V. Jacobson,
“BBR: Congestion-based congestion control,” Queue, vol. 14, no. 5,
p. 50, Oct. 2016.
[65] P. Crews and H. Ayers, “CS 244’18: Recreating and extending Pensieve,”
2018.
[Online].
Available:
https://reproducingnetworkresearch.word
press.com/2018/07/16/cs-244-18-recreating-and-extending-pensieve/
[66] K. Rakelly, A. Zhou, C. Finn, S. Levine, and D. Quillen, “Efficient off-
policy meta-reinforcement learning via probabilistic context variables,”
in Proc. Int. Conf. Mach. Learn. (ICML), 2019, pp. 5331–5340.
[67] A. Nichol, J. Achiam, and J. Schulman, “On first-order meta-learning
algorithms,” 2018, arXiv:1803.02999.
[68] B. McMahan, E. Moore, D. Ramage, S. Hampson, and B. A. Y. Arcas,
“Communication-efficient learning of deep networks from decentralized
data,” in Proc. 20th Int. Conf. Artif. Intell. Statist., 2017, pp. 1273–1282.
[69] H. Van Hasselt, A. Guez, and D. Silver, “Deep reinforcement learning
with double Q-learning,” in Proc. AAAI Conf. Artif. Intell., vol. 30, no. 1,
2016, pp. 1–7.
[70] Y. Jiang, J. Koneˇcn`y, K. Rush, and S. Kannan, “Improving feder-
ated learning personalization via model agnostic meta learning,” 2019,
arXiv:1909.12488.
[71] M. Khodak, M.-F. F. Balcan, and A. S. Talwalkar, “Adaptive gradient-
based meta-learning methods,” in Proc. Adv. Neural Inf. Process. Syst.,
vol. 32, 2019, pp. 1–12.
[72] OpenAI.
(2018).
AI
and
Compute.
[Online].
Available:
https://openai.com/blog/ai-and-compute/
[73] P. Molchanov, S. Tyree, T. Karras, T. Aila, and J. Kautz, “Pruning
convolutional neural networks for resource efficient inference,” 2016,
arXiv:1611.06440.
[74] Y. Li et al., “MicroNet: Towards image recognition with extremely low
FLOPs,” 2020, arXiv:2011.12289.
[75] S. Li, “Tensorflow lite: On-device machine learning framework,”
J. Comput. Res. Develop., vol. 57, no. 9, p. 1839, 2020.
[76] H. Mao et al., “Real-world video adaptation with reinforcement learn-
ing,” 2020, arXiv:2008.12858.
[77] Z. Li et al., “Probe and adapt: Rate adaptation for HTTP video streaming
at scale,” IEEE J. Sel. Areas Commun., vol. 32, no. 4, pp. 719–733,
Apr. 2014.
[78] Z. Wang et al., “MultiLive: Adaptive bitrate control for low-delay multi-
party interactive live streaming,” IEEE/ACM Trans. Netw., vol. 30, no. 2,
pp. 923–938, Apr. 2021.
[79] T. Feng, H. Sun, Q. Qi, J. Wang, and J. Liao, “Vabis: Video adaptation
bitrate system for time-critical live streaming,” IEEE Trans. Multimedia,
vol. 22, no. 11, pp. 2963–2976, Nov. 2019.
[80] Z. Meng et al., “Practically deploying heavyweight adaptive bitrate
algorithms with teacher–student learning,” IEEE/ACM Trans. Netw.,
vol. 29, no. 2, pp. 723–736, Apr. 2021.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```

### Página 19

```text
HUANG et al.: LEARNING TAILORED ABR ALGORITHMS TO HETEROGENEOUS NETWORK CONDITIONS
2503
[81] G. Lv, W. Qinghua, W. Wang, Z. Li, and G. Xie, “Lumos: Towards better
video streaming QOE through accurate throughput prediction,” in Proc.
IEEE Conf. Comput. Commun. (INFOCOM), May 2021, pp. 1–10.
[82] T. Karagkioules, R. Mekuria, D. Griffioen, and A. Wagenaar, “Online
learning for low-latency adaptive streaming,” in Proc. 11th ACM Multi-
media Syst. Conf., May 2020, pp. 315–320.
[83] C. Qiao, J. Wang, and Y. Liu, “Beyond QoE: Diversity adaptation in
video streaming at the edge,” IEEE/ACM Trans. Netw., vol. 29, no. 1,
pp. 289–302, Feb. 2020.
[84] W. Li, J. Huang, S. Wang, C. Wu, S. Liu, and J. Wang, “An apprentice-
ship learning approach for adaptive video streaming based on chunk
quality and user preference,” IEEE Trans. Multimedia, early access,
Feb. 1, 2022, doi: 10.1109/TMM.2022.3147667.
[85] X. Zuo, Y. Jiayu, M. Wang, and Y. Cui, “Adaptive bitrate with user-level
QOE preference for video streaming,” in Proc. IEEE Conf. Comput.
Commun. (INFOCOM), May 2021, pp. 1–10.
[86] V. Mnih et al., “Playing atari with deep reinforcement learning,” 2013,
arXiv:1312.5602.
[87] A. Bentaleb, C. Timmerer, A. C. Begen, and R. Zimmermann, “Per-
formance analysis of ACTE: A bandwidth prediction method for low-
latency chunked streaming,” ACM Trans. Multimedia Comput., Com-
mun., Appl., vol. 16, no. 2s, pp. 1–24, Apr. 2020.
[88] M. Lim, M. N. Akcay, A. Bentaleb, A. C. Begen, and R. Zimmermann,
“When they go high, we go low: Low-latency live streaming in dash.
Js with LoL,” in Proc. 11th ACM Multimedia Syst. Conf., May 2020,
pp. 321–326.
[89] L. Sun, T. Zong, S. Wang, Y. Liu, and Y. Wang, “Tightrope walking in
low-latency live streaming: Optimal joint adaptation of video rate and
playback speed,” in Proc. 12th ACM Multimedia Syst. Conf., Jul. 2021,
pp. 200–213.
[90] G. Yi et al., “The ACM multimedia 2019 live video streaming grand
challenge,” in Proc. 27th ACM Int. Conf. Multimedia, Oct. 2019,
pp. 2622–2626.
[91] R.-X. Zhang et al., “Enhancing the crowdsourced live streaming: A deep
reinforcement learning approach,” in Proc. 29th ACM Workshop Netw.
Oper. Syst. Support Digit. Audio Video (NOSSDAV), 2019, pp. 55–60.
Tianchi Huang (Student Member, IEEE) received
the M.E. degree from the Department of Com-
puter Science and Technology, Guizhou University,
in 2018. He is currently pursuing the Ph.D. degree
with the Department of Computer Science and Tech-
nology, Tsinghua University, advised by Prof. Lifeng
Sun. His research work focuses on the multimedia
network streaming, including transmitting streams,
and edge-assisted content delivery. He received the
Best Student Paper Award from the ACM Mul-
timedia System 2019 Workshop. He has been a
Reviewer of IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY and IEEE
TRANSACTIONS ON MULTIMEDIA.
Chao
Zhou
received
the
Ph.D.
degree
from
the Institute of Computer Science and Technol-
ogy, Peking University, Beijing, China, in 2014.
He has been with Beijing Kuaishou Technology
Company Ltd., as an Algorithm Scientist. Before
joining Kuaishou, he was a Senior Research Engi-
neer with the Media Technology Laboratory, CRI,
Huawei Technologies Company Ltd., Beijing. His
research interests include HTTP video streaming,
joint source-channel coding, and multimedia com-
munications and processing. He received the Best
Paper Award from the IEEE VCIP 2015 and the Best Student Paper
Award from the IEEE VCIP 2012. He has been a Reviewer of IEEE
TRANSACTIONS ON CIRCUITS AND SYSTEMS FOR VIDEO TECHNOLOGY,
IEEE TRANSACTIONS ON MULTIMEDIA, and IEEE TRANSACTIONS ON
WIRELESS COMMUNICATION.
Rui-Xiao Zhang (Student Member, IEEE) received
the B.E. degree from the Department of Electronic
Engineering, Tsinghua University, China, in 2017,
where he is currently pursuing the Ph.D. degree with
the Department of Computer Science and Technol-
ogy. His research interests include content delivery
networks, the optimization of multimedia streaming,
and reinforcement learning. He received the Best
Student Paper Award from the ACM Multimedia
System 2019 Workshop.
Chenglei Wu received the master’s degree from
Tsinghua University, where he is currently pursuing
the Ph.D. degree with the Department of Computer
Science and Technology. His research interests focus
on 360 video streaming, adaptive video streaming,
and routing.
Lifeng Sun (Member, IEEE) received the B.S.
and Ph.D. degrees in system engineering from
the National University of Defense Technology,
Changsha,
Hunan,
China,
in
1995
and
2000,
respectively. He has been join Tsinghua University
since 2001. He is currently a Professor with the
Department of Computer Science and Technology,
Tsinghua University, Beijing. His research interests
include the area of networked multimedia, video
streaming, 3D/multiview video coding, multimedia
cloud computing, and social media.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:21:45 UTC from IEEE Xplore. Restrictions apply.
```
