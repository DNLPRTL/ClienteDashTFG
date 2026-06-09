# ALVS: Adaptive Live Video Streaming using deep reinforcement learning
**Archivo PDF:** `1-s2.0-S1084804522001035-main.pdf`
**Identificador:** `06_alvs_2022_live_video_drl`
**Páginas:** 9
**Foco para Fase 4-5 v1:** Live streaming DRL jointly selecting playback speed and video quality.

> Documento Codex-ready generado para diseño de nuevos modelos/controllers IA ABR. No es una source card corta. Contiene extracción técnica cruda y organizada. El PDF original sigue siendo la fuente de verdad para fórmulas, tablas y figuras si la extracción textual pierde layout.

## 1. Cómo usar este `.md`
- Leer primero las secciones 2-4 para ubicar método, datos y evaluación.
- Usar los extractos crudos por categoría como material base para diseño/contratos/Codex.
- Para ecuaciones, tablas o figuras críticas, comprobar la página indicada en el PDF original.
- No tratar los resultados del paper como promesa directa para DashClientModular4; convertirlos en hipótesis/guardrails y verificar en Phase 6.

## 2. Índice de secciones detectadas
- No se detectó índice fiable por extracción textual.

## 3. Índice de páginas con palabras clave
- p.1: state, action, reward, QoE, buffer, trace, training, latency
- p.2: state, action, QoE, buffer, throughput, trace, training, latency
- p.3: action, QoE, buffer, training, PPO, latency, fairness
- p.4: state, action, reward, QoE, buffer, throughput, training, latency
- p.5: state, action, reward, QoE, buffer, throughput, trace, training, PPO, latency, OOD
- p.6: state, reward, QoE, trace, training, baseline, latency
- p.7: QoE, latency
- p.8: state, action, reward, QoE, trace, training, imitation, latency
- p.9: trace, latency

## 4. Extracción técnica cruda por categorías

### 4.x Modelo / arquitectura / algoritmo

**[Modelo / arquitectura / algoritmo | extracto 1 | p.1]**

Journal of Network and Computer Applications 205 (2022) 103451 Available online 17 June 2022 1084-8045/© 2022 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca ALVS: Adaptive Live Video Streaming using deep reinforcement learning Ihsan Mert Ozcelik ∗, Cem Ersoy Bogazici University, Istanbul, Turkey A R T I C L E I N F O Keywords: Adaptive playback speed Deep reinforcement learning Live streaming media and video quality A B S T R A C T Achieving a high Quality of Experience (QoE) in live event streaming is a challenging problem given a low-latency requirement and time-varying network conditions. Adaptive video bitrate and adaptive playback speed techniques are two separate control knobs to address this challenge. In this paper, we consider these two control parameters in a joint optimization problem and present a deep reinforcement learning (DRL) framework to maximize QoE for live streaming without any assumption about the environment or fixed rulebased heuristics. With the proposed DRL framework, our approach (ALVS) constructs the inference model to make a joint decision of adaptive playback speed and video quality level for the next video segment. Simulation results through real network traces show that ALVS outperforms both state-of-the-art DRL-based and rule-based algorithms in terms of QoE without sacrificing live latency and skipping any content. 1. Introduction Live event streaming is growing in popularity as over-the-top (OTT) service providers are procuring broadcasting rights of worldwide premium sports events like English Premier League, ATP Tour Tennis, Major League Baseball, American National Football League with 5G infrastructure rolling ou

**[Modelo / arquitectura / algoritmo | extracto 2 | p.2]**

Journal of Network and Computer Applications 205 (2022) 103451 2 I.M. Ozcelik and C. Ersoy receives the action taken by the actor and the state space observations to estimate the maximum future award (i.e., the action value). As the value estimator, the critic network is later used to evaluate the action to accelerate to train the actor network; (3) we implement a playback simulator to emulate the adaptive playback speed and video quality selection in live events over DASH. We leverage this simulator in the training process to experience 8 h playback in only 10 s using real 4G traces in one epoch; (4) we perform extensive experiments to confront ALVS with both state-of-the-art DRL-based and rule-based solutions. The remaining parts of the paper are organized as follows. Section 2 surveys the related work by underlining the open issues in the literature and our novelty compared to the literature. Section 3 explains the system model and the formulation of the optimization problem. Section 4 elaborates our proposed RL framework. Section 5 presents an extensive performance evaluation and comparative analysis, followed by the conclusion and future work in Section 6. 2. Related work There is a large group of existing work on reducing end-to-end delay in HTTP live streaming, while aiming to achieve a high QoE. El Essaili et al. (2018) presented a prototype with 33 ms fragments using the chunked transfer to reduce latency without taking into account optimal video bitrate selection and measuring the overall QoE. Van Der Hooft et al. (2018) introduced a new low-latency approach for live streaming based on HTTP/2’s push feature and super-short segments. It reduces end-to-end latency within the range of eight to ten seconds. In contrast, it brings about longer video freeze times co

**[Modelo / arquitectura / algoritmo | extracto 3 | p.3]**

Journal of Network and Computer Applications 205 (2022) 103451 3 I.M. Ozcelik and C. Ersoy Table 1 Comparative table of highlighted studies. Study Goal Approach Action space (Output) Gap for live video streaming Mao et al. (2017) Learning video bitrate adaptation to maximize per-client QoE given changing environment DRL (A2C via a NN) Discreet video bitrates Does not consider live latency Mao et al. (2020) Evaluating Pensieve (Mao et al., 2017) via real-life deployment of millions of video-on-demand sessions DRL (A2C via a NN) Discreet Video Bitrates Does not consider live latency Bentaleb et al. (2018) Maximizing QoE fairness across video sessions Value-based RL Discreet Video Bitrates Does not consider live latency Claeys et al. (2014) Learning video bitrate adaptation to maximize per-client QoE given changing environment Value-based RL Discreet Video Bitrates Does not consider live latency Cui et al. (2021) Learning video bitrate and buffer thresholds to maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Video Bitrates) x (2 Target Buffer Levels to choose playback speeds) Not choose playback speed explicitly. Instead, it uses hand-crafted buffer thresholds as a proxy to choose fast or slow playback speed, which cannot be generalized. Wang et al. (2019) Maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Video Bitrates) x (2 Target Buffer Levels to choose playback speeds) x (Latency Limit to skip frames) The same behavior with TcLiVi Cui et al. (2021) as it also skips content to catch up with the live event. Hong et al. (2019) Maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Discreet Video Bitrates) x (2 Target Buffer Levels

**[Modelo / arquitectura / algoritmo | extracto 4 | p.4]**

Journal of Network and Computer Applications 205 (2022) 103451 4 I.M. Ozcelik and C. Ersoy Fig. 1, while the content is being encoded at the OTT backend side. Our objective during this real-time process is to maximize QoE subject to the live latency target by choosing the played video quality level and playback speed for each video fragment. As the contributors to QoE during a live event streaming process are the played video quality, video quality fluctuations, video freezes, and end-to-end latency between capturing and rendering the event moment, we define QoE model as the weighed sum of these four sub-objectives. This objective can be mathematically expressed as the following: max 𝑝𝑡,𝑞𝑡 𝑇∑ 𝑡=0 𝑄𝑜𝐸𝑡, (1) where 𝑄𝑜𝐸𝑡= (𝑐0 ∗𝑞𝑡 (2) −𝑐1 ∗𝑚𝑎𝑥(0, ((𝑏𝑢𝑓𝑓𝑒𝑟𝑡+ 𝐹𝐷) 𝑝𝑡 ) −(𝐹𝐷∗ 𝑞𝑡 𝐵𝑊𝑡 )) (3) −𝑐2 ∗(|𝑞𝑡−𝑞𝑡−1|) −𝑐3 ∗𝑙𝑖𝑣𝑒_𝑑𝑒𝑙𝑎𝑦𝑡) (4) s.t. 𝑝𝑡∈{0.9, 1, 1.1}, 𝑞𝑡∈{available video bitrates}, (5) 𝑏𝑢𝑓𝑓𝑒𝑟𝑡< 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡, (6) where 𝑝𝑡, 𝑞𝑡, 𝑏𝑢𝑓𝑓𝑒𝑟𝑡, and 𝐵𝑊𝑡represent the playback speed, the played video quality level, the remaining video duration in the playout buffer, and the measured available throughput at time step 𝑡, respectively. 𝑐0,1,2,3 are the coefficients to set the impact of each sub-objective on the overall QoE in Eq. (4). 𝐹𝐷is the fragment duration as a static value during 𝑇-second live streaming. 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡is the target live latency as a kind of service-level agreement value assigned by the OTT application provider. Constraint (5) limits the range of the available playback speed and video quality values, while Constraint (6) makes sure players can only buffer content shorter than the target live latency. The inference module in Fig. 1 outputs the adaptive video quality 𝑞𝑡and playback speed 𝑝𝑡given an input set of observations (e.g., the past bandwidth measurements, the remaining

**[Modelo / arquitectura / algoritmo | extracto 5 | p.5]**

Journal of Network and Computer Applications 205 (2022) 103451 5 I.M. Ozcelik and C. Ersoy a limited number of adjustable policy parameters represented as 𝜃. First, using the policy gradient theorem (Xu et al., 2021), we train the policy for the optimal 𝜃parameters to maximize the expected future reward expressed in Eq. (7). Then, we follow the gradient ∇𝜃𝐽(𝜃) of the expected cumulative reward with respect to the policy parameters in Eq. (9). ∇𝜃𝐽(𝜃) = ∇𝜃E𝜋𝜃 [𝐺𝑡 ] = E𝜋𝜃 [∇𝜃log 𝜋𝜃(𝑠, 𝑎)𝐴𝜋𝜃(𝑠, 𝑎) + 𝛽∇𝜃𝐻(𝜋𝜃(𝑠))] , where 𝐴𝜋𝜃(𝑠, 𝑎) = 𝑄𝜋𝜃(𝑠, 𝑎) −𝑉𝜋𝜃(𝑠). (9) Note that 𝑉(𝑠) is the expected future reward before any action is taken in state 𝑠, whereas 𝑄(𝑠, 𝑎), the Q-value, is the expected reward in state 𝑠after action 𝑎is performed. 𝐴𝜋𝜃(𝑠, 𝑎), the difference between them, is an indicator of how bad or good is a particular action given a particular state. It is also called the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value. Inspired by Pensieve (Mao et al., 2017), we also use an entropy component 𝐻(⋅) with the exploration factor 𝛽in Eq. (9) to trade off exploitation against exploration to obtain better policies as a standard approach in RL. During the training process, the policy parameters of the actor network are updated in each step in the direction of the gradient as in Eq. (10). 𝜃←𝜃+ 𝛼∇𝜃𝐽(𝜃), where 𝛼is the learning rate. (10) The learning agent empirically calculates the Q-value in our simulated environment after performing a sampled action of playback speed and video quality in the actor network output. As Eq. (10) needs the estimation of the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value that depends on 𝑉(𝑠), we use the critic network to approximate 𝑉(𝑠). To train the critic network, we use a multi-step Temporal Difference (TD) learning by getting inspired by Cui et al. (2021). So, the critic network gets the action taken by the actor ne

**[Modelo / arquitectura / algoritmo | extracto 6 | p.6]**

Journal of Network and Computer Applications 205 (2022) 103451 6 I.M. Ozcelik and C. Ersoy Fig. 3. Training convergence to optimal policy parameters. Table 3 Comparison of all five approaches in terms of QoE and live latency. 5-min live sessions 20-min live sessions Avg. Total Reward (QoE) Avg. Live Latency (s) Avg. Total Reward (QoE) Avg. Live Latency (s) ALVS 35.8 ± 5.6 6.7 ± 0.2 154.9 ± 12.7 6.3 ± 0.1 TCLiVi 22.7 ± 5.4 5.5 ± 0.2 93.1 ± 12.3 6.1 ± 0.1 Pensieve 21.0 ± 4.3 6.9 ± 2.1 81.5 ± 32.3 7.8 ± 1.0 DASH.js 29.2 ± 9.4 5.9 ± 0.2 119.4 ± 26.2 6.1 ± 0.1 Baseline 30.1 ± 9.4 11.3 ± 0.4 132.3 ± 32.8 13.9 ± 0.3 Fig. 4. QoE improvement progress over validation set during training. the others despite a higher live latency due to the fixed adaptive playback speed because the QoE formula favors more on the video quality compared to the live delay. As similar to 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒, 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒 suffers from higher live latency because of the fixed playback speed. As 𝐷𝐴𝑆𝐻.𝑗𝑠uses an adaptive playback speed on top of 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒to catch up to the live event, it achieves a lower live latency. 𝑇𝐶𝐿𝑖𝑉𝑖follows the live events more closely at the expense of 40% less QoE than our approach because it is more conservative in video quality selection. As the total event duration increases, our approach also catches up with the live latency achieved by 𝑇𝐶𝐿𝑖𝑉𝑖. In the same manner, as the live event duration gets longer, the approaches with the fixed playback speed, 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒and 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒, manifest higher live latency because longer events have a higher risk of video stalls and the approaches with the fixed playback speed do not have any mechanism to re-catch up with the live event moment. Among the other three approaches with the adaptive playback speed, which are our approach, 𝑇𝐶𝐿𝑖𝑉𝑖, and 𝐷𝐴𝑆𝐻.𝑗𝑠, our approach

**[Modelo / arquitectura / algoritmo | extracto 7 | p.7]**

Journal of Network and Computer Applications 205 (2022) 103451 7 I.M. Ozcelik and C. Ersoy Fig. 5. QoE scores of all the approaches over 15 5-min and 20-min live sessions. Fig. 6. Live latency changes over time. catching up with the live event time despite network fluctuations and video stalls. Second, our approach elaborated in Section 4.2 can adapt to highly varying network conditions without requiring any handcrafted threshold or heuristic. The same policy achieves low-latency

### 4.x Estado / inputs / features observables

**[Estado / inputs / features observables | extracto 1 | p.1]**

Journal of Network and Computer Applications 205 (2022) 103451 Available online 17 June 2022 1084-8045/© 2022 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca ALVS: Adaptive Live Video Streaming using deep reinforcement learning Ihsan Mert Ozcelik ∗, Cem Ersoy Bogazici University, Istanbul, Turkey A R T I C L E I N F O Keywords: Adaptive playback speed Deep reinforcement learning Live streaming media and video quality A B S T R A C T Achieving a high Quality of Experience (QoE) in live event streaming is a challenging problem given a low-latency requirement and time-varying network conditions. Adaptive video bitrate and adaptive playback speed techniques are two separate control knobs to address this challenge. In this paper, we consider these two control parameters in a joint optimization problem and present a deep reinforcement learning (DRL) framework to maximize QoE for live streaming without any assumption about the environment or fixed rulebased heuristics. With the proposed DRL framework, our approach (ALVS) constructs the inference model to make a joint decision of adaptive playback speed and video quality level for the next video segment. Simulation results through real network traces show that ALVS outperforms both state-of-the-art DRL-based and rule-based algorithms in terms of QoE without sacrificing live latency and skipping any content. 1. Introduction Live event streaming is growing in popularity as over-the-top (OTT) service providers are procuring broadcasting rights of worldwide premium sports events like English Premier League, ATP Tour Tennis, Major League Baseball, American National Football League with 5G infrastructure rolling ou

**[Estado / inputs / features observables | extracto 2 | p.2]**

Journal of Network and Computer Applications 205 (2022) 103451 2 I.M. Ozcelik and C. Ersoy receives the action taken by the actor and the state space observations to estimate the maximum future award (i.e., the action value). As the value estimator, the critic network is later used to evaluate the action to accelerate to train the actor network; (3) we implement a playback simulator to emulate the adaptive playback speed and video quality selection in live events over DASH. We leverage this simulator in the training process to experience 8 h playback in only 10 s using real 4G traces in one epoch; (4) we perform extensive experiments to confront ALVS with both state-of-the-art DRL-based and rule-based solutions. The remaining parts of the paper are organized as follows. Section 2 surveys the related work by underlining the open issues in the literature and our novelty compared to the literature. Section 3 explains the system model and the formulation of the optimization problem. Section 4 elaborates our proposed RL framework. Section 5 presents an extensive performance evaluation and comparative analysis, followed by the conclusion and future work in Section 6. 2. Related work There is a large group of existing work on reducing end-to-end delay in HTTP live streaming, while aiming to achieve a high QoE. El Essaili et al. (2018) presented a prototype with 33 ms fragments using the chunked transfer to reduce latency without taking into account optimal video bitrate selection and measuring the overall QoE. Van Der Hooft et al. (2018) introduced a new low-latency approach for live streaming based on HTTP/2’s push feature and super-short segments. It reduces end-to-end latency within the range of eight to ten seconds. In contrast, it brings about longer video freeze times co

**[Estado / inputs / features observables | extracto 3 | p.3]**

Journal of Network and Computer Applications 205 (2022) 103451 3 I.M. Ozcelik and C. Ersoy Table 1 Comparative table of highlighted studies. Study Goal Approach Action space (Output) Gap for live video streaming Mao et al. (2017) Learning video bitrate adaptation to maximize per-client QoE given changing environment DRL (A2C via a NN) Discreet video bitrates Does not consider live latency Mao et al. (2020) Evaluating Pensieve (Mao et al., 2017) via real-life deployment of millions of video-on-demand sessions DRL (A2C via a NN) Discreet Video Bitrates Does not consider live latency Bentaleb et al. (2018) Maximizing QoE fairness across video sessions Value-based RL Discreet Video Bitrates Does not consider live latency Claeys et al. (2014) Learning video bitrate adaptation to maximize per-client QoE given changing environment Value-based RL Discreet Video Bitrates Does not consider live latency Cui et al. (2021) Learning video bitrate and buffer thresholds to maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Video Bitrates) x (2 Target Buffer Levels to choose playback speeds) Not choose playback speed explicitly. Instead, it uses hand-crafted buffer thresholds as a proxy to choose fast or slow playback speed, which cannot be generalized. Wang et al. (2019) Maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Video Bitrates) x (2 Target Buffer Levels to choose playback speeds) x (Latency Limit to skip frames) The same behavior with TcLiVi Cui et al. (2021) as it also skips content to catch up with the live event. Hong et al. (2019) Maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Discreet Video Bitrates) x (2 Target Buffer Levels

**[Estado / inputs / features observables | extracto 4 | p.4]**

Journal of Network and Computer Applications 205 (2022) 103451 4 I.M. Ozcelik and C. Ersoy Fig. 1, while the content is being encoded at the OTT backend side. Our objective during this real-time process is to maximize QoE subject to the live latency target by choosing the played video quality level and playback speed for each video fragment. As the contributors to QoE during a live event streaming process are the played video quality, video quality fluctuations, video freezes, and end-to-end latency between capturing and rendering the event moment, we define QoE model as the weighed sum of these four sub-objectives. This objective can be mathematically expressed as the following: max 𝑝𝑡,𝑞𝑡 𝑇∑ 𝑡=0 𝑄𝑜𝐸𝑡, (1) where 𝑄𝑜𝐸𝑡= (𝑐0 ∗𝑞𝑡 (2) −𝑐1 ∗𝑚𝑎𝑥(0, ((𝑏𝑢𝑓𝑓𝑒𝑟𝑡+ 𝐹𝐷) 𝑝𝑡 ) −(𝐹𝐷∗ 𝑞𝑡 𝐵𝑊𝑡 )) (3) −𝑐2 ∗(|𝑞𝑡−𝑞𝑡−1|) −𝑐3 ∗𝑙𝑖𝑣𝑒_𝑑𝑒𝑙𝑎𝑦𝑡) (4) s.t. 𝑝𝑡∈{0.9, 1, 1.1}, 𝑞𝑡∈{available video bitrates}, (5) 𝑏𝑢𝑓𝑓𝑒𝑟𝑡< 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡, (6) where 𝑝𝑡, 𝑞𝑡, 𝑏𝑢𝑓𝑓𝑒𝑟𝑡, and 𝐵𝑊𝑡represent the playback speed, the played video quality level, the remaining video duration in the playout buffer, and the measured available throughput at time step 𝑡, respectively. 𝑐0,1,2,3 are the coefficients to set the impact of each sub-objective on the overall QoE in Eq. (4). 𝐹𝐷is the fragment duration as a static value during 𝑇-second live streaming. 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡is the target live latency as a kind of service-level agreement value assigned by the OTT application provider. Constraint (5) limits the range of the available playback speed and video quality values, while Constraint (6) makes sure players can only buffer content shorter than the target live latency. The inference module in Fig. 1 outputs the adaptive video quality 𝑞𝑡and playback speed 𝑝𝑡given an input set of observations (e.g., the past bandwidth measurements, the remaining

**[Estado / inputs / features observables | extracto 5 | p.5]**

Journal of Network and Computer Applications 205 (2022) 103451 5 I.M. Ozcelik and C. Ersoy a limited number of adjustable policy parameters represented as 𝜃. First, using the policy gradient theorem (Xu et al., 2021), we train the policy for the optimal 𝜃parameters to maximize the expected future reward expressed in Eq. (7). Then, we follow the gradient ∇𝜃𝐽(𝜃) of the expected cumulative reward with respect to the policy parameters in Eq. (9). ∇𝜃𝐽(𝜃) = ∇𝜃E𝜋𝜃 [𝐺𝑡 ] = E𝜋𝜃 [∇𝜃log 𝜋𝜃(𝑠, 𝑎)𝐴𝜋𝜃(𝑠, 𝑎) + 𝛽∇𝜃𝐻(𝜋𝜃(𝑠))] , where 𝐴𝜋𝜃(𝑠, 𝑎) = 𝑄𝜋𝜃(𝑠, 𝑎) −𝑉𝜋𝜃(𝑠). (9) Note that 𝑉(𝑠) is the expected future reward before any action is taken in state 𝑠, whereas 𝑄(𝑠, 𝑎), the Q-value, is the expected reward in state 𝑠after action 𝑎is performed. 𝐴𝜋𝜃(𝑠, 𝑎), the difference between them, is an indicator of how bad or good is a particular action given a particular state. It is also called the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value. Inspired by Pensieve (Mao et al., 2017), we also use an entropy component 𝐻(⋅) with the exploration factor 𝛽in Eq. (9) to trade off exploitation against exploration to obtain better policies as a standard approach in RL. During the training process, the policy parameters of the actor network are updated in each step in the direction of the gradient as in Eq. (10). 𝜃←𝜃+ 𝛼∇𝜃𝐽(𝜃), where 𝛼is the learning rate. (10) The learning agent empirically calculates the Q-value in our simulated environment after performing a sampled action of playback speed and video quality in the actor network output. As Eq. (10) needs the estimation of the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value that depends on 𝑉(𝑠), we use the critic network to approximate 𝑉(𝑠). To train the critic network, we use a multi-step Temporal Difference (TD) learning by getting inspired by Cui et al. (2021). So, the critic network gets the action taken by the actor ne

**[Estado / inputs / features observables | extracto 6 | p.6]**

Journal of Network and Computer Applications 205 (2022) 103451 6 I.M. Ozcelik and C. Ersoy Fig. 3. Training convergence to optimal policy parameters. Table 3 Comparison of all five approaches in terms of QoE and live latency. 5-min live sessions 20-min live sessions Avg. Total Reward (QoE) Avg. Live Latency (s) Avg. Total Reward (QoE) Avg. Live Latency (s) ALVS 35.8 ± 5.6 6.7 ± 0.2 154.9 ± 12.7 6.3 ± 0.1 TCLiVi 22.7 ± 5.4 5.5 ± 0.2 93.1 ± 12.3 6.1 ± 0.1 Pensieve 21.0 ± 4.3 6.9 ± 2.1 81.5 ± 32.3 7.8 ± 1.0 DASH.js 29.2 ± 9.4 5.9 ± 0.2 119.4 ± 26.2 6.1 ± 0.1 Baseline 30.1 ± 9.4 11.3 ± 0.4 132.3 ± 32.8 13.9 ± 0.3 Fig. 4. QoE improvement progress over validation set during training. the others despite a higher live latency due to the fixed adaptive playback speed because the QoE formula favors more on the video quality compared to the live delay. As similar to 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒, 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒 suffers from higher live latency because of the fixed playback speed. As 𝐷𝐴𝑆𝐻.𝑗𝑠uses an adaptive playback speed on top of 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒to catch up to the live event, it achieves a lower live latency. 𝑇𝐶𝐿𝑖𝑉𝑖follows the live events more closely at the expense of 40% less QoE than our approach because it is more conservative in video quality selection. As the total event duration increases, our approach also catches up with the live latency achieved by 𝑇𝐶𝐿𝑖𝑉𝑖. In the same manner, as the live event duration gets longer, the approaches with the fixed playback speed, 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒and 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒, manifest higher live latency because longer events have a higher risk of video stalls and the approaches with the fixed playback speed do not have any mechanism to re-catch up with the live event moment. Among the other three approaches with the adaptive playback speed, which are our approach, 𝑇𝐶𝐿𝑖𝑉𝑖, and 𝐷𝐴𝑆𝐻.𝑗𝑠, our approach

**[Estado / inputs / features observables | extracto 7 | p.7]**

Journal of Network and Computer Applications 205 (2022) 103451 7 I.M. Ozcelik and C. Ersoy Fig. 5. QoE scores of all the approaches over 15 5-min and 20-min live sessions. Fig. 6. Live latency changes over time. catching up with the live event time despite network fluctuations and video stalls. Second, our approach elaborated in Section 4.2 can adapt to highly varying network conditions without requiring any handcrafted threshold or heuristic. The same policy achieves low-latency

### 4.x Acción / decisión ABR

**[Acción / decisión ABR | extracto 1 | p.1]**

Journal of Network and Computer Applications 205 (2022) 103451 Available online 17 June 2022 1084-8045/© 2022 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca ALVS: Adaptive Live Video Streaming using deep reinforcement learning Ihsan Mert Ozcelik ∗, Cem Ersoy Bogazici University, Istanbul, Turkey A R T I C L E I N F O Keywords: Adaptive playback speed Deep reinforcement learning Live streaming media and video quality A B S T R A C T Achieving a high Quality of Experience (QoE) in live event streaming is a challenging problem given a low-latency requirement and time-varying network conditions. Adaptive video bitrate and adaptive playback speed techniques are two separate control knobs to address this challenge. In this paper, we consider these two control parameters in a joint optimization problem and present a deep reinforcement learning (DRL) framework to maximize QoE for live streaming without any assumption about the environment or fixed rulebased heuristics. With the proposed DRL framework, our approach (ALVS) constructs the inference model to make a joint decision of adaptive playback speed and video quality level for the next video segment. Simulation results through real network traces show that ALVS outperforms both state-of-the-art DRL-based and rule-based algorithms in terms of QoE without sacrificing live latency and skipping any content. 1. Introduction Live event streaming is growing in popularity as over-the-top (OTT) service providers are procuring broadcasting rights of worldwide premium sports events like English Premier League, ATP Tour Tennis, Major League Baseball, American National Football League with 5G infrastructure rolling ou

**[Acción / decisión ABR | extracto 2 | p.2]**

Journal of Network and Computer Applications 205 (2022) 103451 2 I.M. Ozcelik and C. Ersoy receives the action taken by the actor and the state space observations to estimate the maximum future award (i.e., the action value). As the value estimator, the critic network is later used to evaluate the action to accelerate to train the actor network; (3) we implement a playback simulator to emulate the adaptive playback speed and video quality selection in live events over DASH. We leverage this simulator in the training process to experience 8 h playback in only 10 s using real 4G traces in one epoch; (4) we perform extensive experiments to confront ALVS with both state-of-the-art DRL-based and rule-based solutions. The remaining parts of the paper are organized as follows. Section 2 surveys the related work by underlining the open issues in the literature and our novelty compared to the literature. Section 3 explains the system model and the formulation of the optimization problem. Section 4 elaborates our proposed RL framework. Section 5 presents an extensive performance evaluation and comparative analysis, followed by the conclusion and future work in Section 6. 2. Related work There is a large group of existing work on reducing end-to-end delay in HTTP live streaming, while aiming to achieve a high QoE. El Essaili et al. (2018) presented a prototype with 33 ms fragments using the chunked transfer to reduce latency without taking into account optimal video bitrate selection and measuring the overall QoE. Van Der Hooft et al. (2018) introduced a new low-latency approach for live streaming based on HTTP/2’s push feature and super-short segments. It reduces end-to-end latency within the range of eight to ten seconds. In contrast, it brings about longer video freeze times co

**[Acción / decisión ABR | extracto 3 | p.3]**

Journal of Network and Computer Applications 205 (2022) 103451 3 I.M. Ozcelik and C. Ersoy Table 1 Comparative table of highlighted studies. Study Goal Approach Action space (Output) Gap for live video streaming Mao et al. (2017) Learning video bitrate adaptation to maximize per-client QoE given changing environment DRL (A2C via a NN) Discreet video bitrates Does not consider live latency Mao et al. (2020) Evaluating Pensieve (Mao et al., 2017) via real-life deployment of millions of video-on-demand sessions DRL (A2C via a NN) Discreet Video Bitrates Does not consider live latency Bentaleb et al. (2018) Maximizing QoE fairness across video sessions Value-based RL Discreet Video Bitrates Does not consider live latency Claeys et al. (2014) Learning video bitrate adaptation to maximize per-client QoE given changing environment Value-based RL Discreet Video Bitrates Does not consider live latency Cui et al. (2021) Learning video bitrate and buffer thresholds to maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Video Bitrates) x (2 Target Buffer Levels to choose playback speeds) Not choose playback speed explicitly. Instead, it uses hand-crafted buffer thresholds as a proxy to choose fast or slow playback speed, which cannot be generalized. Wang et al. (2019) Maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Video Bitrates) x (2 Target Buffer Levels to choose playback speeds) x (Latency Limit to skip frames) The same behavior with TcLiVi Cui et al. (2021) as it also skips content to catch up with the live event. Hong et al. (2019) Maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Discreet Video Bitrates) x (2 Target Buffer Levels

**[Acción / decisión ABR | extracto 4 | p.4]**

Journal of Network and Computer Applications 205 (2022) 103451 4 I.M. Ozcelik and C. Ersoy Fig. 1, while the content is being encoded at the OTT backend side. Our objective during this real-time process is to maximize QoE subject to the live latency target by choosing the played video quality level and playback speed for each video fragment. As the contributors to QoE during a live event streaming process are the played video quality, video quality fluctuations, video freezes, and end-to-end latency between capturing and rendering the event moment, we define QoE model as the weighed sum of these four sub-objectives. This objective can be mathematically expressed as the following: max 𝑝𝑡,𝑞𝑡 𝑇∑ 𝑡=0 𝑄𝑜𝐸𝑡, (1) where 𝑄𝑜𝐸𝑡= (𝑐0 ∗𝑞𝑡 (2) −𝑐1 ∗𝑚𝑎𝑥(0, ((𝑏𝑢𝑓𝑓𝑒𝑟𝑡+ 𝐹𝐷) 𝑝𝑡 ) −(𝐹𝐷∗ 𝑞𝑡 𝐵𝑊𝑡 )) (3) −𝑐2 ∗(|𝑞𝑡−𝑞𝑡−1|) −𝑐3 ∗𝑙𝑖𝑣𝑒_𝑑𝑒𝑙𝑎𝑦𝑡) (4) s.t. 𝑝𝑡∈{0.9, 1, 1.1}, 𝑞𝑡∈{available video bitrates}, (5) 𝑏𝑢𝑓𝑓𝑒𝑟𝑡< 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡, (6) where 𝑝𝑡, 𝑞𝑡, 𝑏𝑢𝑓𝑓𝑒𝑟𝑡, and 𝐵𝑊𝑡represent the playback speed, the played video quality level, the remaining video duration in the playout buffer, and the measured available throughput at time step 𝑡, respectively. 𝑐0,1,2,3 are the coefficients to set the impact of each sub-objective on the overall QoE in Eq. (4). 𝐹𝐷is the fragment duration as a static value during 𝑇-second live streaming. 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡is the target live latency as a kind of service-level agreement value assigned by the OTT application provider. Constraint (5) limits the range of the available playback speed and video quality values, while Constraint (6) makes sure players can only buffer content shorter than the target live latency. The inference module in Fig. 1 outputs the adaptive video quality 𝑞𝑡and playback speed 𝑝𝑡given an input set of observations (e.g., the past bandwidth measurements, the remaining

**[Acción / decisión ABR | extracto 5 | p.5]**

Journal of Network and Computer Applications 205 (2022) 103451 5 I.M. Ozcelik and C. Ersoy a limited number of adjustable policy parameters represented as 𝜃. First, using the policy gradient theorem (Xu et al., 2021), we train the policy for the optimal 𝜃parameters to maximize the expected future reward expressed in Eq. (7). Then, we follow the gradient ∇𝜃𝐽(𝜃) of the expected cumulative reward with respect to the policy parameters in Eq. (9). ∇𝜃𝐽(𝜃) = ∇𝜃E𝜋𝜃 [𝐺𝑡 ] = E𝜋𝜃 [∇𝜃log 𝜋𝜃(𝑠, 𝑎)𝐴𝜋𝜃(𝑠, 𝑎) + 𝛽∇𝜃𝐻(𝜋𝜃(𝑠))] , where 𝐴𝜋𝜃(𝑠, 𝑎) = 𝑄𝜋𝜃(𝑠, 𝑎) −𝑉𝜋𝜃(𝑠). (9) Note that 𝑉(𝑠) is the expected future reward before any action is taken in state 𝑠, whereas 𝑄(𝑠, 𝑎), the Q-value, is the expected reward in state 𝑠after action 𝑎is performed. 𝐴𝜋𝜃(𝑠, 𝑎), the difference between them, is an indicator of how bad or good is a particular action given a particular state. It is also called the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value. Inspired by Pensieve (Mao et al., 2017), we also use an entropy component 𝐻(⋅) with the exploration factor 𝛽in Eq. (9) to trade off exploitation against exploration to obtain better policies as a standard approach in RL. During the training process, the policy parameters of the actor network are updated in each step in the direction of the gradient as in Eq. (10). 𝜃←𝜃+ 𝛼∇𝜃𝐽(𝜃), where 𝛼is the learning rate. (10) The learning agent empirically calculates the Q-value in our simulated environment after performing a sampled action of playback speed and video quality in the actor network output. As Eq. (10) needs the estimation of the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value that depends on 𝑉(𝑠), we use the critic network to approximate 𝑉(𝑠). To train the critic network, we use a multi-step Temporal Difference (TD) learning by getting inspired by Cui et al. (2021). So, the critic network gets the action taken by the actor ne

**[Acción / decisión ABR | extracto 6 | p.6]**

Journal of Network and Computer Applications 205 (2022) 103451 6 I.M. Ozcelik and C. Ersoy Fig. 3. Training convergence to optimal policy parameters. Table 3 Comparison of all five approaches in terms of QoE and live latency. 5-min live sessions 20-min live sessions Avg. Total Reward (QoE) Avg. Live Latency (s) Avg. Total Reward (QoE) Avg. Live Latency (s) ALVS 35.8 ± 5.6 6.7 ± 0.2 154.9 ± 12.7 6.3 ± 0.1 TCLiVi 22.7 ± 5.4 5.5 ± 0.2 93.1 ± 12.3 6.1 ± 0.1 Pensieve 21.0 ± 4.3 6.9 ± 2.1 81.5 ± 32.3 7.8 ± 1.0 DASH.js 29.2 ± 9.4 5.9 ± 0.2 119.4 ± 26.2 6.1 ± 0.1 Baseline 30.1 ± 9.4 11.3 ± 0.4 132.3 ± 32.8 13.9 ± 0.3 Fig. 4. QoE improvement progress over validation set during training. the others despite a higher live latency due to the fixed adaptive playback speed because the QoE formula favors more on the video quality compared to the live delay. As similar to 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒, 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒 suffers from higher live latency because of the fixed playback speed. As 𝐷𝐴𝑆𝐻.𝑗𝑠uses an adaptive playback speed on top of 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒to catch up to the live event, it achieves a lower live latency. 𝑇𝐶𝐿𝑖𝑉𝑖follows the live events more closely at the expense of 40% less QoE than our approach because it is more conservative in video quality selection. As the total event duration increases, our approach also catches up with the live latency achieved by 𝑇𝐶𝐿𝑖𝑉𝑖. In the same manner, as the live event duration gets longer, the approaches with the fixed playback speed, 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒and 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒, manifest higher live latency because longer events have a higher risk of video stalls and the approaches with the fixed playback speed do not have any mechanism to re-catch up with the live event moment. Among the other three approaches with the adaptive playback speed, which are our approach, 𝑇𝐶𝐿𝑖𝑉𝑖, and 𝐷𝐴𝑆𝐻.𝑗𝑠, our approach

### 4.x Reward / QoE / función objetivo

**[Reward / QoE / función objetivo | extracto 1 | p.1]**

Journal of Network and Computer Applications 205 (2022) 103451 Available online 17 June 2022 1084-8045/© 2022 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca ALVS: Adaptive Live Video Streaming using deep reinforcement learning Ihsan Mert Ozcelik ∗, Cem Ersoy Bogazici University, Istanbul, Turkey A R T I C L E I N F O Keywords: Adaptive playback speed Deep reinforcement learning Live streaming media and video quality A B S T R A C T Achieving a high Quality of Experience (QoE) in live event streaming is a challenging problem given a low-latency requirement and time-varying network conditions. Adaptive video bitrate and adaptive playback speed techniques are two separate control knobs to address this challenge. In this paper, we consider these two control parameters in a joint optimization problem and present a deep reinforcement learning (DRL) framework to maximize QoE for live streaming without any assumption about the environment or fixed rulebased heuristics. With the proposed DRL framework, our approach (ALVS) constructs the inference model to make a joint decision of adaptive playback speed and video quality level for the next video segment. Simulation results through real network traces show that ALVS outperforms both state-of-the-art DRL-based and rule-based algorithms in terms of QoE without sacrificing live latency and skipping any content. 1. Introduction Live event streaming is growing in popularity as over-the-top (OTT) service providers are procuring broadcasting rights of worldwide premium sports events like English Premier League, ATP Tour Tennis, Major League Baseball, American National Football League with 5G infrastructure rolling ou

**[Reward / QoE / función objetivo | extracto 2 | p.2]**

Journal of Network and Computer Applications 205 (2022) 103451 2 I.M. Ozcelik and C. Ersoy receives the action taken by the actor and the state space observations to estimate the maximum future award (i.e., the action value). As the value estimator, the critic network is later used to evaluate the action to accelerate to train the actor network; (3) we implement a playback simulator to emulate the adaptive playback speed and video quality selection in live events over DASH. We leverage this simulator in the training process to experience 8 h playback in only 10 s using real 4G traces in one epoch; (4) we perform extensive experiments to confront ALVS with both state-of-the-art DRL-based and rule-based solutions. The remaining parts of the paper are organized as follows. Section 2 surveys the related work by underlining the open issues in the literature and our novelty compared to the literature. Section 3 explains the system model and the formulation of the optimization problem. Section 4 elaborates our proposed RL framework. Section 5 presents an extensive performance evaluation and comparative analysis, followed by the conclusion and future work in Section 6. 2. Related work There is a large group of existing work on reducing end-to-end delay in HTTP live streaming, while aiming to achieve a high QoE. El Essaili et al. (2018) presented a prototype with 33 ms fragments using the chunked transfer to reduce latency without taking into account optimal video bitrate selection and measuring the overall QoE. Van Der Hooft et al. (2018) introduced a new low-latency approach for live streaming based on HTTP/2’s push feature and super-short segments. It reduces end-to-end latency within the range of eight to ten seconds. In contrast, it brings about longer video freeze times co

**[Reward / QoE / función objetivo | extracto 3 | p.3]**

Journal of Network and Computer Applications 205 (2022) 103451 3 I.M. Ozcelik and C. Ersoy Table 1 Comparative table of highlighted studies. Study Goal Approach Action space (Output) Gap for live video streaming Mao et al. (2017) Learning video bitrate adaptation to maximize per-client QoE given changing environment DRL (A2C via a NN) Discreet video bitrates Does not consider live latency Mao et al. (2020) Evaluating Pensieve (Mao et al., 2017) via real-life deployment of millions of video-on-demand sessions DRL (A2C via a NN) Discreet Video Bitrates Does not consider live latency Bentaleb et al. (2018) Maximizing QoE fairness across video sessions Value-based RL Discreet Video Bitrates Does not consider live latency Claeys et al. (2014) Learning video bitrate adaptation to maximize per-client QoE given changing environment Value-based RL Discreet Video Bitrates Does not consider live latency Cui et al. (2021) Learning video bitrate and buffer thresholds to maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Video Bitrates) x (2 Target Buffer Levels to choose playback speeds) Not choose playback speed explicitly. Instead, it uses hand-crafted buffer thresholds as a proxy to choose fast or slow playback speed, which cannot be generalized. Wang et al. (2019) Maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Video Bitrates) x (2 Target Buffer Levels to choose playback speeds) x (Latency Limit to skip frames) The same behavior with TcLiVi Cui et al. (2021) as it also skips content to catch up with the live event. Hong et al. (2019) Maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Discreet Video Bitrates) x (2 Target Buffer Levels

**[Reward / QoE / función objetivo | extracto 4 | p.4]**

Journal of Network and Computer Applications 205 (2022) 103451 4 I.M. Ozcelik and C. Ersoy Fig. 1, while the content is being encoded at the OTT backend side. Our objective during this real-time process is to maximize QoE subject to the live latency target by choosing the played video quality level and playback speed for each video fragment. As the contributors to QoE during a live event streaming process are the played video quality, video quality fluctuations, video freezes, and end-to-end latency between capturing and rendering the event moment, we define QoE model as the weighed sum of these four sub-objectives. This objective can be mathematically expressed as the following: max 𝑝𝑡,𝑞𝑡 𝑇∑ 𝑡=0 𝑄𝑜𝐸𝑡, (1) where 𝑄𝑜𝐸𝑡= (𝑐0 ∗𝑞𝑡 (2) −𝑐1 ∗𝑚𝑎𝑥(0, ((𝑏𝑢𝑓𝑓𝑒𝑟𝑡+ 𝐹𝐷) 𝑝𝑡 ) −(𝐹𝐷∗ 𝑞𝑡 𝐵𝑊𝑡 )) (3) −𝑐2 ∗(|𝑞𝑡−𝑞𝑡−1|) −𝑐3 ∗𝑙𝑖𝑣𝑒_𝑑𝑒𝑙𝑎𝑦𝑡) (4) s.t. 𝑝𝑡∈{0.9, 1, 1.1}, 𝑞𝑡∈{available video bitrates}, (5) 𝑏𝑢𝑓𝑓𝑒𝑟𝑡< 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡, (6) where 𝑝𝑡, 𝑞𝑡, 𝑏𝑢𝑓𝑓𝑒𝑟𝑡, and 𝐵𝑊𝑡represent the playback speed, the played video quality level, the remaining video duration in the playout buffer, and the measured available throughput at time step 𝑡, respectively. 𝑐0,1,2,3 are the coefficients to set the impact of each sub-objective on the overall QoE in Eq. (4). 𝐹𝐷is the fragment duration as a static value during 𝑇-second live streaming. 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡is the target live latency as a kind of service-level agreement value assigned by the OTT application provider. Constraint (5) limits the range of the available playback speed and video quality values, while Constraint (6) makes sure players can only buffer content shorter than the target live latency. The inference module in Fig. 1 outputs the adaptive video quality 𝑞𝑡and playback speed 𝑝𝑡given an input set of observations (e.g., the past bandwidth measurements, the remaining

**[Reward / QoE / función objetivo | extracto 5 | p.5]**

Journal of Network and Computer Applications 205 (2022) 103451 5 I.M. Ozcelik and C. Ersoy a limited number of adjustable policy parameters represented as 𝜃. First, using the policy gradient theorem (Xu et al., 2021), we train the policy for the optimal 𝜃parameters to maximize the expected future reward expressed in Eq. (7). Then, we follow the gradient ∇𝜃𝐽(𝜃) of the expected cumulative reward with respect to the policy parameters in Eq. (9). ∇𝜃𝐽(𝜃) = ∇𝜃E𝜋𝜃 [𝐺𝑡 ] = E𝜋𝜃 [∇𝜃log 𝜋𝜃(𝑠, 𝑎)𝐴𝜋𝜃(𝑠, 𝑎) + 𝛽∇𝜃𝐻(𝜋𝜃(𝑠))] , where 𝐴𝜋𝜃(𝑠, 𝑎) = 𝑄𝜋𝜃(𝑠, 𝑎) −𝑉𝜋𝜃(𝑠). (9) Note that 𝑉(𝑠) is the expected future reward before any action is taken in state 𝑠, whereas 𝑄(𝑠, 𝑎), the Q-value, is the expected reward in state 𝑠after action 𝑎is performed. 𝐴𝜋𝜃(𝑠, 𝑎), the difference between them, is an indicator of how bad or good is a particular action given a particular state. It is also called the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value. Inspired by Pensieve (Mao et al., 2017), we also use an entropy component 𝐻(⋅) with the exploration factor 𝛽in Eq. (9) to trade off exploitation against exploration to obtain better policies as a standard approach in RL. During the training process, the policy parameters of the actor network are updated in each step in the direction of the gradient as in Eq. (10). 𝜃←𝜃+ 𝛼∇𝜃𝐽(𝜃), where 𝛼is the learning rate. (10) The learning agent empirically calculates the Q-value in our simulated environment after performing a sampled action of playback speed and video quality in the actor network output. As Eq. (10) needs the estimation of the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value that depends on 𝑉(𝑠), we use the critic network to approximate 𝑉(𝑠). To train the critic network, we use a multi-step Temporal Difference (TD) learning by getting inspired by Cui et al. (2021). So, the critic network gets the action taken by the actor ne

**[Reward / QoE / función objetivo | extracto 6 | p.6]**

Journal of Network and Computer Applications 205 (2022) 103451 6 I.M. Ozcelik and C. Ersoy Fig. 3. Training convergence to optimal policy parameters. Table 3 Comparison of all five approaches in terms of QoE and live latency. 5-min live sessions 20-min live sessions Avg. Total Reward (QoE) Avg. Live Latency (s) Avg. Total Reward (QoE) Avg. Live Latency (s) ALVS 35.8 ± 5.6 6.7 ± 0.2 154.9 ± 12.7 6.3 ± 0.1 TCLiVi 22.7 ± 5.4 5.5 ± 0.2 93.1 ± 12.3 6.1 ± 0.1 Pensieve 21.0 ± 4.3 6.9 ± 2.1 81.5 ± 32.3 7.8 ± 1.0 DASH.js 29.2 ± 9.4 5.9 ± 0.2 119.4 ± 26.2 6.1 ± 0.1 Baseline 30.1 ± 9.4 11.3 ± 0.4 132.3 ± 32.8 13.9 ± 0.3 Fig. 4. QoE improvement progress over validation set during training. the others despite a higher live latency due to the fixed adaptive playback speed because the QoE formula favors more on the video quality compared to the live delay. As similar to 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒, 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒 suffers from higher live latency because of the fixed playback speed. As 𝐷𝐴𝑆𝐻.𝑗𝑠uses an adaptive playback speed on top of 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒to catch up to the live event, it achieves a lower live latency. 𝑇𝐶𝐿𝑖𝑉𝑖follows the live events more closely at the expense of 40% less QoE than our approach because it is more conservative in video quality selection. As the total event duration increases, our approach also catches up with the live latency achieved by 𝑇𝐶𝐿𝑖𝑉𝑖. In the same manner, as the live event duration gets longer, the approaches with the fixed playback speed, 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒and 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒, manifest higher live latency because longer events have a higher risk of video stalls and the approaches with the fixed playback speed do not have any mechanism to re-catch up with the live event moment. Among the other three approaches with the adaptive playback speed, which are our approach, 𝑇𝐶𝐿𝑖𝑉𝑖, and 𝐷𝐴𝑆𝐻.𝑗𝑠, our approach

**[Reward / QoE / función objetivo | extracto 7 | p.7]**

Journal of Network and Computer Applications 205 (2022) 103451 7 I.M. Ozcelik and C. Ersoy Fig. 5. QoE scores of all the approaches over 15 5-min and 20-min live sessions. Fig. 6. Live latency changes over time. catching up with the live event time despite network fluctuations and video stalls. Second, our approach elaborated in Section 4.2 can adapt to highly varying network conditions without requiring any handcrafted threshold or heuristic. The same policy achieves low-latency

### 4.x Entrenamiento / learning procedure

**[Entrenamiento / learning procedure | extracto 1 | p.1]**

Journal of Network and Computer Applications 205 (2022) 103451 Available online 17 June 2022 1084-8045/© 2022 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca ALVS: Adaptive Live Video Streaming using deep reinforcement learning Ihsan Mert Ozcelik ∗, Cem Ersoy Bogazici University, Istanbul, Turkey A R T I C L E I N F O Keywords: Adaptive playback speed Deep reinforcement learning Live streaming media and video quality A B S T R A C T Achieving a high Quality of Experience (QoE) in live event streaming is a challenging problem given a low-latency requirement and time-varying network conditions. Adaptive video bitrate and adaptive playback speed techniques are two separate control knobs to address this challenge. In this paper, we consider these two control parameters in a joint optimization problem and present a deep reinforcement learning (DRL) framework to maximize QoE for live streaming without any assumption about the environment or fixed rulebased heuristics. With the proposed DRL framework, our approach (ALVS) constructs the inference model to make a joint decision of adaptive playback speed and video quality level for the next video segment. Simulation results through real network traces show that ALVS outperforms both state-of-the-art DRL-based and rule-based algorithms in terms of QoE without sacrificing live latency and skipping any content. 1. Introduction Live event streaming is growing in popularity as over-the-top (OTT) service providers are procuring broadcasting rights of worldwide premium sports events like English Premier League, ATP Tour Tennis, Major League Baseball, American National Football League with 5G infrastructure rolling ou

**[Entrenamiento / learning procedure | extracto 2 | p.2]**

Journal of Network and Computer Applications 205 (2022) 103451 2 I.M. Ozcelik and C. Ersoy receives the action taken by the actor and the state space observations to estimate the maximum future award (i.e., the action value). As the value estimator, the critic network is later used to evaluate the action to accelerate to train the actor network; (3) we implement a playback simulator to emulate the adaptive playback speed and video quality selection in live events over DASH. We leverage this simulator in the training process to experience 8 h playback in only 10 s using real 4G traces in one epoch; (4) we perform extensive experiments to confront ALVS with both state-of-the-art DRL-based and rule-based solutions. The remaining parts of the paper are organized as follows. Section 2 surveys the related work by underlining the open issues in the literature and our novelty compared to the literature. Section 3 explains the system model and the formulation of the optimization problem. Section 4 elaborates our proposed RL framework. Section 5 presents an extensive performance evaluation and comparative analysis, followed by the conclusion and future work in Section 6. 2. Related work There is a large group of existing work on reducing end-to-end delay in HTTP live streaming, while aiming to achieve a high QoE. El Essaili et al. (2018) presented a prototype with 33 ms fragments using the chunked transfer to reduce latency without taking into account optimal video bitrate selection and measuring the overall QoE. Van Der Hooft et al. (2018) introduced a new low-latency approach for live streaming based on HTTP/2’s push feature and super-short segments. It reduces end-to-end latency within the range of eight to ten seconds. In contrast, it brings about longer video freeze times co

**[Entrenamiento / learning procedure | extracto 3 | p.3]**

Journal of Network and Computer Applications 205 (2022) 103451 3 I.M. Ozcelik and C. Ersoy Table 1 Comparative table of highlighted studies. Study Goal Approach Action space (Output) Gap for live video streaming Mao et al. (2017) Learning video bitrate adaptation to maximize per-client QoE given changing environment DRL (A2C via a NN) Discreet video bitrates Does not consider live latency Mao et al. (2020) Evaluating Pensieve (Mao et al., 2017) via real-life deployment of millions of video-on-demand sessions DRL (A2C via a NN) Discreet Video Bitrates Does not consider live latency Bentaleb et al. (2018) Maximizing QoE fairness across video sessions Value-based RL Discreet Video Bitrates Does not consider live latency Claeys et al. (2014) Learning video bitrate adaptation to maximize per-client QoE given changing environment Value-based RL Discreet Video Bitrates Does not consider live latency Cui et al. (2021) Learning video bitrate and buffer thresholds to maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Video Bitrates) x (2 Target Buffer Levels to choose playback speeds) Not choose playback speed explicitly. Instead, it uses hand-crafted buffer thresholds as a proxy to choose fast or slow playback speed, which cannot be generalized. Wang et al. (2019) Maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Video Bitrates) x (2 Target Buffer Levels to choose playback speeds) x (Latency Limit to skip frames) The same behavior with TcLiVi Cui et al. (2021) as it also skips content to catch up with the live event. Hong et al. (2019) Maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Discreet Video Bitrates) x (2 Target Buffer Levels

**[Entrenamiento / learning procedure | extracto 4 | p.4]**

Journal of Network and Computer Applications 205 (2022) 103451 4 I.M. Ozcelik and C. Ersoy Fig. 1, while the content is being encoded at the OTT backend side. Our objective during this real-time process is to maximize QoE subject to the live latency target by choosing the played video quality level and playback speed for each video fragment. As the contributors to QoE during a live event streaming process are the played video quality, video quality fluctuations, video freezes, and end-to-end latency between capturing and rendering the event moment, we define QoE model as the weighed sum of these four sub-objectives. This objective can be mathematically expressed as the following: max 𝑝𝑡,𝑞𝑡 𝑇∑ 𝑡=0 𝑄𝑜𝐸𝑡, (1) where 𝑄𝑜𝐸𝑡= (𝑐0 ∗𝑞𝑡 (2) −𝑐1 ∗𝑚𝑎𝑥(0, ((𝑏𝑢𝑓𝑓𝑒𝑟𝑡+ 𝐹𝐷) 𝑝𝑡 ) −(𝐹𝐷∗ 𝑞𝑡 𝐵𝑊𝑡 )) (3) −𝑐2 ∗(|𝑞𝑡−𝑞𝑡−1|) −𝑐3 ∗𝑙𝑖𝑣𝑒_𝑑𝑒𝑙𝑎𝑦𝑡) (4) s.t. 𝑝𝑡∈{0.9, 1, 1.1}, 𝑞𝑡∈{available video bitrates}, (5) 𝑏𝑢𝑓𝑓𝑒𝑟𝑡< 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡, (6) where 𝑝𝑡, 𝑞𝑡, 𝑏𝑢𝑓𝑓𝑒𝑟𝑡, and 𝐵𝑊𝑡represent the playback speed, the played video quality level, the remaining video duration in the playout buffer, and the measured available throughput at time step 𝑡, respectively. 𝑐0,1,2,3 are the coefficients to set the impact of each sub-objective on the overall QoE in Eq. (4). 𝐹𝐷is the fragment duration as a static value during 𝑇-second live streaming. 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡is the target live latency as a kind of service-level agreement value assigned by the OTT application provider. Constraint (5) limits the range of the available playback speed and video quality values, while Constraint (6) makes sure players can only buffer content shorter than the target live latency. The inference module in Fig. 1 outputs the adaptive video quality 𝑞𝑡and playback speed 𝑝𝑡given an input set of observations (e.g., the past bandwidth measurements, the remaining

**[Entrenamiento / learning procedure | extracto 5 | p.5]**

Journal of Network and Computer Applications 205 (2022) 103451 5 I.M. Ozcelik and C. Ersoy a limited number of adjustable policy parameters represented as 𝜃. First, using the policy gradient theorem (Xu et al., 2021), we train the policy for the optimal 𝜃parameters to maximize the expected future reward expressed in Eq. (7). Then, we follow the gradient ∇𝜃𝐽(𝜃) of the expected cumulative reward with respect to the policy parameters in Eq. (9). ∇𝜃𝐽(𝜃) = ∇𝜃E𝜋𝜃 [𝐺𝑡 ] = E𝜋𝜃 [∇𝜃log 𝜋𝜃(𝑠, 𝑎)𝐴𝜋𝜃(𝑠, 𝑎) + 𝛽∇𝜃𝐻(𝜋𝜃(𝑠))] , where 𝐴𝜋𝜃(𝑠, 𝑎) = 𝑄𝜋𝜃(𝑠, 𝑎) −𝑉𝜋𝜃(𝑠). (9) Note that 𝑉(𝑠) is the expected future reward before any action is taken in state 𝑠, whereas 𝑄(𝑠, 𝑎), the Q-value, is the expected reward in state 𝑠after action 𝑎is performed. 𝐴𝜋𝜃(𝑠, 𝑎), the difference between them, is an indicator of how bad or good is a particular action given a particular state. It is also called the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value. Inspired by Pensieve (Mao et al., 2017), we also use an entropy component 𝐻(⋅) with the exploration factor 𝛽in Eq. (9) to trade off exploitation against exploration to obtain better policies as a standard approach in RL. During the training process, the policy parameters of the actor network are updated in each step in the direction of the gradient as in Eq. (10). 𝜃←𝜃+ 𝛼∇𝜃𝐽(𝜃), where 𝛼is the learning rate. (10) The learning agent empirically calculates the Q-value in our simulated environment after performing a sampled action of playback speed and video quality in the actor network output. As Eq. (10) needs the estimation of the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value that depends on 𝑉(𝑠), we use the critic network to approximate 𝑉(𝑠). To train the critic network, we use a multi-step Temporal Difference (TD) learning by getting inspired by Cui et al. (2021). So, the critic network gets the action taken by the actor ne

**[Entrenamiento / learning procedure | extracto 6 | p.6]**

Journal of Network and Computer Applications 205 (2022) 103451 6 I.M. Ozcelik and C. Ersoy Fig. 3. Training convergence to optimal policy parameters. Table 3 Comparison of all five approaches in terms of QoE and live latency. 5-min live sessions 20-min live sessions Avg. Total Reward (QoE) Avg. Live Latency (s) Avg. Total Reward (QoE) Avg. Live Latency (s) ALVS 35.8 ± 5.6 6.7 ± 0.2 154.9 ± 12.7 6.3 ± 0.1 TCLiVi 22.7 ± 5.4 5.5 ± 0.2 93.1 ± 12.3 6.1 ± 0.1 Pensieve 21.0 ± 4.3 6.9 ± 2.1 81.5 ± 32.3 7.8 ± 1.0 DASH.js 29.2 ± 9.4 5.9 ± 0.2 119.4 ± 26.2 6.1 ± 0.1 Baseline 30.1 ± 9.4 11.3 ± 0.4 132.3 ± 32.8 13.9 ± 0.3 Fig. 4. QoE improvement progress over validation set during training. the others despite a higher live latency due to the fixed adaptive playback speed because the QoE formula favors more on the video quality compared to the live delay. As similar to 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒, 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒 suffers from higher live latency because of the fixed playback speed. As 𝐷𝐴𝑆𝐻.𝑗𝑠uses an adaptive playback speed on top of 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒to catch up to the live event, it achieves a lower live latency. 𝑇𝐶𝐿𝑖𝑉𝑖follows the live events more closely at the expense of 40% less QoE than our approach because it is more conservative in video quality selection. As the total event duration increases, our approach also catches up with the live latency achieved by 𝑇𝐶𝐿𝑖𝑉𝑖. In the same manner, as the live event duration gets longer, the approaches with the fixed playback speed, 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒and 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒, manifest higher live latency because longer events have a higher risk of video stalls and the approaches with the fixed playback speed do not have any mechanism to re-catch up with the live event moment. Among the other three approaches with the adaptive playback speed, which are our approach, 𝑇𝐶𝐿𝑖𝑉𝑖, and 𝐷𝐴𝑆𝐻.𝑗𝑠, our approach

### 4.x Datos / trazas / datasets / contenidos

**[Datos / trazas / datasets / contenidos | extracto 1 | p.1]**

Journal of Network and Computer Applications 205 (2022) 103451 Available online 17 June 2022 1084-8045/© 2022 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca ALVS: Adaptive Live Video Streaming using deep reinforcement learning Ihsan Mert Ozcelik ∗, Cem Ersoy Bogazici University, Istanbul, Turkey A R T I C L E I N F O Keywords: Adaptive playback speed Deep reinforcement learning Live streaming media and video quality A B S T R A C T Achieving a high Quality of Experience (QoE) in live event streaming is a challenging problem given a low-latency requirement and time-varying network conditions. Adaptive video bitrate and adaptive playback speed techniques are two separate control knobs to address this challenge. In this paper, we consider these two control parameters in a joint optimization problem and present a deep reinforcement learning (DRL) framework to maximize QoE for live streaming without any assumption about the environment or fixed rulebased heuristics. With the proposed DRL framework, our approach (ALVS) constructs the inference model to make a joint decision of adaptive playback speed and video quality level for the next video segment. Simulation results through real network traces show that ALVS outperforms both state-of-the-art DRL-based and rule-based algorithms in terms of QoE without sacrificing live latency and skipping any content. 1. Introduction Live event streaming is growing in popularity as over-the-top (OTT) service providers are procuring broadcasting rights of worldwide premium sports events like English Premier League, ATP Tour Tennis, Major League Baseball, American National Football League with 5G infrastructure rolling ou

**[Datos / trazas / datasets / contenidos | extracto 2 | p.2]**

Journal of Network and Computer Applications 205 (2022) 103451 2 I.M. Ozcelik and C. Ersoy receives the action taken by the actor and the state space observations to estimate the maximum future award (i.e., the action value). As the value estimator, the critic network is later used to evaluate the action to accelerate to train the actor network; (3) we implement a playback simulator to emulate the adaptive playback speed and video quality selection in live events over DASH. We leverage this simulator in the training process to experience 8 h playback in only 10 s using real 4G traces in one epoch; (4) we perform extensive experiments to confront ALVS with both state-of-the-art DRL-based and rule-based solutions. The remaining parts of the paper are organized as follows. Section 2 surveys the related work by underlining the open issues in the literature and our novelty compared to the literature. Section 3 explains the system model and the formulation of the optimization problem. Section 4 elaborates our proposed RL framework. Section 5 presents an extensive performance evaluation and comparative analysis, followed by the conclusion and future work in Section 6. 2. Related work There is a large group of existing work on reducing end-to-end delay in HTTP live streaming, while aiming to achieve a high QoE. El Essaili et al. (2018) presented a prototype with 33 ms fragments using the chunked transfer to reduce latency without taking into account optimal video bitrate selection and measuring the overall QoE. Van Der Hooft et al. (2018) introduced a new low-latency approach for live streaming based on HTTP/2’s push feature and super-short segments. It reduces end-to-end latency within the range of eight to ten seconds. In contrast, it brings about longer video freeze times co

**[Datos / trazas / datasets / contenidos | extracto 3 | p.3]**

Journal of Network and Computer Applications 205 (2022) 103451 3 I.M. Ozcelik and C. Ersoy Table 1 Comparative table of highlighted studies. Study Goal Approach Action space (Output) Gap for live video streaming Mao et al. (2017) Learning video bitrate adaptation to maximize per-client QoE given changing environment DRL (A2C via a NN) Discreet video bitrates Does not consider live latency Mao et al. (2020) Evaluating Pensieve (Mao et al., 2017) via real-life deployment of millions of video-on-demand sessions DRL (A2C via a NN) Discreet Video Bitrates Does not consider live latency Bentaleb et al. (2018) Maximizing QoE fairness across video sessions Value-based RL Discreet Video Bitrates Does not consider live latency Claeys et al. (2014) Learning video bitrate adaptation to maximize per-client QoE given changing environment Value-based RL Discreet Video Bitrates Does not consider live latency Cui et al. (2021) Learning video bitrate and buffer thresholds to maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Video Bitrates) x (2 Target Buffer Levels to choose playback speeds) Not choose playback speed explicitly. Instead, it uses hand-crafted buffer thresholds as a proxy to choose fast or slow playback speed, which cannot be generalized. Wang et al. (2019) Maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Video Bitrates) x (2 Target Buffer Levels to choose playback speeds) x (Latency Limit to skip frames) The same behavior with TcLiVi Cui et al. (2021) as it also skips content to catch up with the live event. Hong et al. (2019) Maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Discreet Video Bitrates) x (2 Target Buffer Levels

**[Datos / trazas / datasets / contenidos | extracto 4 | p.4]**

Journal of Network and Computer Applications 205 (2022) 103451 4 I.M. Ozcelik and C. Ersoy Fig. 1, while the content is being encoded at the OTT backend side. Our objective during this real-time process is to maximize QoE subject to the live latency target by choosing the played video quality level and playback speed for each video fragment. As the contributors to QoE during a live event streaming process are the played video quality, video quality fluctuations, video freezes, and end-to-end latency between capturing and rendering the event moment, we define QoE model as the weighed sum of these four sub-objectives. This objective can be mathematically expressed as the following: max 𝑝𝑡,𝑞𝑡 𝑇∑ 𝑡=0 𝑄𝑜𝐸𝑡, (1) where 𝑄𝑜𝐸𝑡= (𝑐0 ∗𝑞𝑡 (2) −𝑐1 ∗𝑚𝑎𝑥(0, ((𝑏𝑢𝑓𝑓𝑒𝑟𝑡+ 𝐹𝐷) 𝑝𝑡 ) −(𝐹𝐷∗ 𝑞𝑡 𝐵𝑊𝑡 )) (3) −𝑐2 ∗(|𝑞𝑡−𝑞𝑡−1|) −𝑐3 ∗𝑙𝑖𝑣𝑒_𝑑𝑒𝑙𝑎𝑦𝑡) (4) s.t. 𝑝𝑡∈{0.9, 1, 1.1}, 𝑞𝑡∈{available video bitrates}, (5) 𝑏𝑢𝑓𝑓𝑒𝑟𝑡< 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡, (6) where 𝑝𝑡, 𝑞𝑡, 𝑏𝑢𝑓𝑓𝑒𝑟𝑡, and 𝐵𝑊𝑡represent the playback speed, the played video quality level, the remaining video duration in the playout buffer, and the measured available throughput at time step 𝑡, respectively. 𝑐0,1,2,3 are the coefficients to set the impact of each sub-objective on the overall QoE in Eq. (4). 𝐹𝐷is the fragment duration as a static value during 𝑇-second live streaming. 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡is the target live latency as a kind of service-level agreement value assigned by the OTT application provider. Constraint (5) limits the range of the available playback speed and video quality values, while Constraint (6) makes sure players can only buffer content shorter than the target live latency. The inference module in Fig. 1 outputs the adaptive video quality 𝑞𝑡and playback speed 𝑝𝑡given an input set of observations (e.g., the past bandwidth measurements, the remaining

**[Datos / trazas / datasets / contenidos | extracto 5 | p.5]**

Journal of Network and Computer Applications 205 (2022) 103451 5 I.M. Ozcelik and C. Ersoy a limited number of adjustable policy parameters represented as 𝜃. First, using the policy gradient theorem (Xu et al., 2021), we train the policy for the optimal 𝜃parameters to maximize the expected future reward expressed in Eq. (7). Then, we follow the gradient ∇𝜃𝐽(𝜃) of the expected cumulative reward with respect to the policy parameters in Eq. (9). ∇𝜃𝐽(𝜃) = ∇𝜃E𝜋𝜃 [𝐺𝑡 ] = E𝜋𝜃 [∇𝜃log 𝜋𝜃(𝑠, 𝑎)𝐴𝜋𝜃(𝑠, 𝑎) + 𝛽∇𝜃𝐻(𝜋𝜃(𝑠))] , where 𝐴𝜋𝜃(𝑠, 𝑎) = 𝑄𝜋𝜃(𝑠, 𝑎) −𝑉𝜋𝜃(𝑠). (9) Note that 𝑉(𝑠) is the expected future reward before any action is taken in state 𝑠, whereas 𝑄(𝑠, 𝑎), the Q-value, is the expected reward in state 𝑠after action 𝑎is performed. 𝐴𝜋𝜃(𝑠, 𝑎), the difference between them, is an indicator of how bad or good is a particular action given a particular state. It is also called the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value. Inspired by Pensieve (Mao et al., 2017), we also use an entropy component 𝐻(⋅) with the exploration factor 𝛽in Eq. (9) to trade off exploitation against exploration to obtain better policies as a standard approach in RL. During the training process, the policy parameters of the actor network are updated in each step in the direction of the gradient as in Eq. (10). 𝜃←𝜃+ 𝛼∇𝜃𝐽(𝜃), where 𝛼is the learning rate. (10) The learning agent empirically calculates the Q-value in our simulated environment after performing a sampled action of playback speed and video quality in the actor network output. As Eq. (10) needs the estimation of the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value that depends on 𝑉(𝑠), we use the critic network to approximate 𝑉(𝑠). To train the critic network, we use a multi-step Temporal Difference (TD) learning by getting inspired by Cui et al. (2021). So, the critic network gets the action taken by the actor ne

**[Datos / trazas / datasets / contenidos | extracto 6 | p.6]**

Journal of Network and Computer Applications 205 (2022) 103451 6 I.M. Ozcelik and C. Ersoy Fig. 3. Training convergence to optimal policy parameters. Table 3 Comparison of all five approaches in terms of QoE and live latency. 5-min live sessions 20-min live sessions Avg. Total Reward (QoE) Avg. Live Latency (s) Avg. Total Reward (QoE) Avg. Live Latency (s) ALVS 35.8 ± 5.6 6.7 ± 0.2 154.9 ± 12.7 6.3 ± 0.1 TCLiVi 22.7 ± 5.4 5.5 ± 0.2 93.1 ± 12.3 6.1 ± 0.1 Pensieve 21.0 ± 4.3 6.9 ± 2.1 81.5 ± 32.3 7.8 ± 1.0 DASH.js 29.2 ± 9.4 5.9 ± 0.2 119.4 ± 26.2 6.1 ± 0.1 Baseline 30.1 ± 9.4 11.3 ± 0.4 132.3 ± 32.8 13.9 ± 0.3 Fig. 4. QoE improvement progress over validation set during training. the others despite a higher live latency due to the fixed adaptive playback speed because the QoE formula favors more on the video quality compared to the live delay. As similar to 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒, 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒 suffers from higher live latency because of the fixed playback speed. As 𝐷𝐴𝑆𝐻.𝑗𝑠uses an adaptive playback speed on top of 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒to catch up to the live event, it achieves a lower live latency. 𝑇𝐶𝐿𝑖𝑉𝑖follows the live events more closely at the expense of 40% less QoE than our approach because it is more conservative in video quality selection. As the total event duration increases, our approach also catches up with the live latency achieved by 𝑇𝐶𝐿𝑖𝑉𝑖. In the same manner, as the live event duration gets longer, the approaches with the fixed playback speed, 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒and 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒, manifest higher live latency because longer events have a higher risk of video stalls and the approaches with the fixed playback speed do not have any mechanism to re-catch up with the live event moment. Among the other three approaches with the adaptive playback speed, which are our approach, 𝑇𝐶𝐿𝑖𝑉𝑖, and 𝐷𝐴𝑆𝐻.𝑗𝑠, our approach

**[Datos / trazas / datasets / contenidos | extracto 7 | p.7]**

Journal of Network and Computer Applications 205 (2022) 103451 7 I.M. Ozcelik and C. Ersoy Fig. 5. QoE scores of all the approaches over 15 5-min and 20-min live sessions. Fig. 6. Live latency changes over time. catching up with the live event time despite network fluctuations and video stalls. Second, our approach elaborated in Section 4.2 can adapt to highly varying network conditions without requiring any handcrafted threshold or heuristic. The same policy achieves low-latency

### 4.x Evaluación / baselines / experimentos

**[Evaluación / baselines / experimentos | extracto 1 | p.1]**

Journal of Network and Computer Applications 205 (2022) 103451 Available online 17 June 2022 1084-8045/© 2022 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca ALVS: Adaptive Live Video Streaming using deep reinforcement learning Ihsan Mert Ozcelik ∗, Cem Ersoy Bogazici University, Istanbul, Turkey A R T I C L E I N F O Keywords: Adaptive playback speed Deep reinforcement learning Live streaming media and video quality A B S T R A C T Achieving a high Quality of Experience (QoE) in live event streaming is a challenging problem given a low-latency requirement and time-varying network conditions. Adaptive video bitrate and adaptive playback speed techniques are two separate control knobs to address this challenge. In this paper, we consider these two control parameters in a joint optimization problem and present a deep reinforcement learning (DRL) framework to maximize QoE for live streaming without any assumption about the environment or fixed rulebased heuristics. With the proposed DRL framework, our approach (ALVS) constructs the inference model to make a joint decision of adaptive playback speed and video quality level for the next video segment. Simulation results through real network traces show that ALVS outperforms both state-of-the-art DRL-based and rule-based algorithms in terms of QoE without sacrificing live latency and skipping any content. 1. Introduction Live event streaming is growing in popularity as over-the-top (OTT) service providers are procuring broadcasting rights of worldwide premium sports events like English Premier League, ATP Tour Tennis, Major League Baseball, American National Football League with 5G infrastructure rolling ou

**[Evaluación / baselines / experimentos | extracto 2 | p.2]**

Journal of Network and Computer Applications 205 (2022) 103451 2 I.M. Ozcelik and C. Ersoy receives the action taken by the actor and the state space observations to estimate the maximum future award (i.e., the action value). As the value estimator, the critic network is later used to evaluate the action to accelerate to train the actor network; (3) we implement a playback simulator to emulate the adaptive playback speed and video quality selection in live events over DASH. We leverage this simulator in the training process to experience 8 h playback in only 10 s using real 4G traces in one epoch; (4) we perform extensive experiments to confront ALVS with both state-of-the-art DRL-based and rule-based solutions. The remaining parts of the paper are organized as follows. Section 2 surveys the related work by underlining the open issues in the literature and our novelty compared to the literature. Section 3 explains the system model and the formulation of the optimization problem. Section 4 elaborates our proposed RL framework. Section 5 presents an extensive performance evaluation and comparative analysis, followed by the conclusion and future work in Section 6. 2. Related work There is a large group of existing work on reducing end-to-end delay in HTTP live streaming, while aiming to achieve a high QoE. El Essaili et al. (2018) presented a prototype with 33 ms fragments using the chunked transfer to reduce latency without taking into account optimal video bitrate selection and measuring the overall QoE. Van Der Hooft et al. (2018) introduced a new low-latency approach for live streaming based on HTTP/2’s push feature and super-short segments. It reduces end-to-end latency within the range of eight to ten seconds. In contrast, it brings about longer video freeze times co

**[Evaluación / baselines / experimentos | extracto 3 | p.4]**

Journal of Network and Computer Applications 205 (2022) 103451 4 I.M. Ozcelik and C. Ersoy Fig. 1, while the content is being encoded at the OTT backend side. Our objective during this real-time process is to maximize QoE subject to the live latency target by choosing the played video quality level and playback speed for each video fragment. As the contributors to QoE during a live event streaming process are the played video quality, video quality fluctuations, video freezes, and end-to-end latency between capturing and rendering the event moment, we define QoE model as the weighed sum of these four sub-objectives. This objective can be mathematically expressed as the following: max 𝑝𝑡,𝑞𝑡 𝑇∑ 𝑡=0 𝑄𝑜𝐸𝑡, (1) where 𝑄𝑜𝐸𝑡= (𝑐0 ∗𝑞𝑡 (2) −𝑐1 ∗𝑚𝑎𝑥(0, ((𝑏𝑢𝑓𝑓𝑒𝑟𝑡+ 𝐹𝐷) 𝑝𝑡 ) −(𝐹𝐷∗ 𝑞𝑡 𝐵𝑊𝑡 )) (3) −𝑐2 ∗(|𝑞𝑡−𝑞𝑡−1|) −𝑐3 ∗𝑙𝑖𝑣𝑒_𝑑𝑒𝑙𝑎𝑦𝑡) (4) s.t. 𝑝𝑡∈{0.9, 1, 1.1}, 𝑞𝑡∈{available video bitrates}, (5) 𝑏𝑢𝑓𝑓𝑒𝑟𝑡< 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡, (6) where 𝑝𝑡, 𝑞𝑡, 𝑏𝑢𝑓𝑓𝑒𝑟𝑡, and 𝐵𝑊𝑡represent the playback speed, the played video quality level, the remaining video duration in the playout buffer, and the measured available throughput at time step 𝑡, respectively. 𝑐0,1,2,3 are the coefficients to set the impact of each sub-objective on the overall QoE in Eq. (4). 𝐹𝐷is the fragment duration as a static value during 𝑇-second live streaming. 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡is the target live latency as a kind of service-level agreement value assigned by the OTT application provider. Constraint (5) limits the range of the available playback speed and video quality values, while Constraint (6) makes sure players can only buffer content shorter than the target live latency. The inference module in Fig. 1 outputs the adaptive video quality 𝑞𝑡and playback speed 𝑝𝑡given an input set of observations (e.g., the past bandwidth measurements, the remaining

**[Evaluación / baselines / experimentos | extracto 4 | p.5]**

Journal of Network and Computer Applications 205 (2022) 103451 5 I.M. Ozcelik and C. Ersoy a limited number of adjustable policy parameters represented as 𝜃. First, using the policy gradient theorem (Xu et al., 2021), we train the policy for the optimal 𝜃parameters to maximize the expected future reward expressed in Eq. (7). Then, we follow the gradient ∇𝜃𝐽(𝜃) of the expected cumulative reward with respect to the policy parameters in Eq. (9). ∇𝜃𝐽(𝜃) = ∇𝜃E𝜋𝜃 [𝐺𝑡 ] = E𝜋𝜃 [∇𝜃log 𝜋𝜃(𝑠, 𝑎)𝐴𝜋𝜃(𝑠, 𝑎) + 𝛽∇𝜃𝐻(𝜋𝜃(𝑠))] , where 𝐴𝜋𝜃(𝑠, 𝑎) = 𝑄𝜋𝜃(𝑠, 𝑎) −𝑉𝜋𝜃(𝑠). (9) Note that 𝑉(𝑠) is the expected future reward before any action is taken in state 𝑠, whereas 𝑄(𝑠, 𝑎), the Q-value, is the expected reward in state 𝑠after action 𝑎is performed. 𝐴𝜋𝜃(𝑠, 𝑎), the difference between them, is an indicator of how bad or good is a particular action given a particular state. It is also called the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value. Inspired by Pensieve (Mao et al., 2017), we also use an entropy component 𝐻(⋅) with the exploration factor 𝛽in Eq. (9) to trade off exploitation against exploration to obtain better policies as a standard approach in RL. During the training process, the policy parameters of the actor network are updated in each step in the direction of the gradient as in Eq. (10). 𝜃←𝜃+ 𝛼∇𝜃𝐽(𝜃), where 𝛼is the learning rate. (10) The learning agent empirically calculates the Q-value in our simulated environment after performing a sampled action of playback speed and video quality in the actor network output. As Eq. (10) needs the estimation of the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value that depends on 𝑉(𝑠), we use the critic network to approximate 𝑉(𝑠). To train the critic network, we use a multi-step Temporal Difference (TD) learning by getting inspired by Cui et al. (2021). So, the critic network gets the action taken by the actor ne

**[Evaluación / baselines / experimentos | extracto 5 | p.6]**

Journal of Network and Computer Applications 205 (2022) 103451 6 I.M. Ozcelik and C. Ersoy Fig. 3. Training convergence to optimal policy parameters. Table 3 Comparison of all five approaches in terms of QoE and live latency. 5-min live sessions 20-min live sessions Avg. Total Reward (QoE) Avg. Live Latency (s) Avg. Total Reward (QoE) Avg. Live Latency (s) ALVS 35.8 ± 5.6 6.7 ± 0.2 154.9 ± 12.7 6.3 ± 0.1 TCLiVi 22.7 ± 5.4 5.5 ± 0.2 93.1 ± 12.3 6.1 ± 0.1 Pensieve 21.0 ± 4.3 6.9 ± 2.1 81.5 ± 32.3 7.8 ± 1.0 DASH.js 29.2 ± 9.4 5.9 ± 0.2 119.4 ± 26.2 6.1 ± 0.1 Baseline 30.1 ± 9.4 11.3 ± 0.4 132.3 ± 32.8 13.9 ± 0.3 Fig. 4. QoE improvement progress over validation set during training. the others despite a higher live latency due to the fixed adaptive playback speed because the QoE formula favors more on the video quality compared to the live delay. As similar to 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒, 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒 suffers from higher live latency because of the fixed playback speed. As 𝐷𝐴𝑆𝐻.𝑗𝑠uses an adaptive playback speed on top of 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒to catch up to the live event, it achieves a lower live latency. 𝑇𝐶𝐿𝑖𝑉𝑖follows the live events more closely at the expense of 40% less QoE than our approach because it is more conservative in video quality selection. As the total event duration increases, our approach also catches up with the live latency achieved by 𝑇𝐶𝐿𝑖𝑉𝑖. In the same manner, as the live event duration gets longer, the approaches with the fixed playback speed, 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒and 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒, manifest higher live latency because longer events have a higher risk of video stalls and the approaches with the fixed playback speed do not have any mechanism to re-catch up with the live event moment. Among the other three approaches with the adaptive playback speed, which are our approach, 𝑇𝐶𝐿𝑖𝑉𝑖, and 𝐷𝐴𝑆𝐻.𝑗𝑠, our approach

### 4.x Limitaciones / riesgos / aplicabilidad

**[Limitaciones / riesgos / aplicabilidad | extracto 1 | p.1]**

Journal of Network and Computer Applications 205 (2022) 103451 Available online 17 June 2022 1084-8045/© 2022 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca ALVS: Adaptive Live Video Streaming using deep reinforcement learning Ihsan Mert Ozcelik ∗, Cem Ersoy Bogazici University, Istanbul, Turkey A R T I C L E I N F O Keywords: Adaptive playback speed Deep reinforcement learning Live streaming media and video quality A B S T R A C T Achieving a high Quality of Experience (QoE) in live event streaming is a challenging problem given a low-latency requirement and time-varying network conditions. Adaptive video bitrate and adaptive playback speed techniques are two separate control knobs to address this challenge. In this paper, we consider these two control parameters in a joint optimization problem and present a deep reinforcement learning (DRL) framework to maximize QoE for live streaming without any assumption about the environment or fixed rulebased heuristics. With the proposed DRL framework, our approach (ALVS) constructs the inference model to make a joint decision of adaptive playback speed and video quality level for the next video segment. Simulation results through real network traces show that ALVS outperforms both state-of-the-art DRL-based and rule-based algorithms in terms of QoE without sacrificing live latency and skipping any content. 1. Introduction Live event streaming is growing in popularity as over-the-top (OTT) service providers are procuring broadcasting rights of worldwide premium sports events like English Premier League, ATP Tour Tennis, Major League Baseball, American National Football League with 5G infrastructure rolling ou

**[Limitaciones / riesgos / aplicabilidad | extracto 2 | p.2]**

Journal of Network and Computer Applications 205 (2022) 103451 2 I.M. Ozcelik and C. Ersoy receives the action taken by the actor and the state space observations to estimate the maximum future award (i.e., the action value). As the value estimator, the critic network is later used to evaluate the action to accelerate to train the actor network; (3) we implement a playback simulator to emulate the adaptive playback speed and video quality selection in live events over DASH. We leverage this simulator in the training process to experience 8 h playback in only 10 s using real 4G traces in one epoch; (4) we perform extensive experiments to confront ALVS with both state-of-the-art DRL-based and rule-based solutions. The remaining parts of the paper are organized as follows. Section 2 surveys the related work by underlining the open issues in the literature and our novelty compared to the literature. Section 3 explains the system model and the formulation of the optimization problem. Section 4 elaborates our proposed RL framework. Section 5 presents an extensive performance evaluation and comparative analysis, followed by the conclusion and future work in Section 6. 2. Related work There is a large group of existing work on reducing end-to-end delay in HTTP live streaming, while aiming to achieve a high QoE. El Essaili et al. (2018) presented a prototype with 33 ms fragments using the chunked transfer to reduce latency without taking into account optimal video bitrate selection and measuring the overall QoE. Van Der Hooft et al. (2018) introduced a new low-latency approach for live streaming based on HTTP/2’s push feature and super-short segments. It reduces end-to-end latency within the range of eight to ten seconds. In contrast, it brings about longer video freeze times co

**[Limitaciones / riesgos / aplicabilidad | extracto 3 | p.3]**

Journal of Network and Computer Applications 205 (2022) 103451 3 I.M. Ozcelik and C. Ersoy Table 1 Comparative table of highlighted studies. Study Goal Approach Action space (Output) Gap for live video streaming Mao et al. (2017) Learning video bitrate adaptation to maximize per-client QoE given changing environment DRL (A2C via a NN) Discreet video bitrates Does not consider live latency Mao et al. (2020) Evaluating Pensieve (Mao et al., 2017) via real-life deployment of millions of video-on-demand sessions DRL (A2C via a NN) Discreet Video Bitrates Does not consider live latency Bentaleb et al. (2018) Maximizing QoE fairness across video sessions Value-based RL Discreet Video Bitrates Does not consider live latency Claeys et al. (2014) Learning video bitrate adaptation to maximize per-client QoE given changing environment Value-based RL Discreet Video Bitrates Does not consider live latency Cui et al. (2021) Learning video bitrate and buffer thresholds to maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Video Bitrates) x (2 Target Buffer Levels to choose playback speeds) Not choose playback speed explicitly. Instead, it uses hand-crafted buffer thresholds as a proxy to choose fast or slow playback speed, which cannot be generalized. Wang et al. (2019) Maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Video Bitrates) x (2 Target Buffer Levels to choose playback speeds) x (Latency Limit to skip frames) The same behavior with TcLiVi Cui et al. (2021) as it also skips content to catch up with the live event. Hong et al. (2019) Maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Discreet Video Bitrates) x (2 Target Buffer Levels

**[Limitaciones / riesgos / aplicabilidad | extracto 4 | p.4]**

Journal of Network and Computer Applications 205 (2022) 103451 4 I.M. Ozcelik and C. Ersoy Fig. 1, while the content is being encoded at the OTT backend side. Our objective during this real-time process is to maximize QoE subject to the live latency target by choosing the played video quality level and playback speed for each video fragment. As the contributors to QoE during a live event streaming process are the played video quality, video quality fluctuations, video freezes, and end-to-end latency between capturing and rendering the event moment, we define QoE model as the weighed sum of these four sub-objectives. This objective can be mathematically expressed as the following: max 𝑝𝑡,𝑞𝑡 𝑇∑ 𝑡=0 𝑄𝑜𝐸𝑡, (1) where 𝑄𝑜𝐸𝑡= (𝑐0 ∗𝑞𝑡 (2) −𝑐1 ∗𝑚𝑎𝑥(0, ((𝑏𝑢𝑓𝑓𝑒𝑟𝑡+ 𝐹𝐷) 𝑝𝑡 ) −(𝐹𝐷∗ 𝑞𝑡 𝐵𝑊𝑡 )) (3) −𝑐2 ∗(|𝑞𝑡−𝑞𝑡−1|) −𝑐3 ∗𝑙𝑖𝑣𝑒_𝑑𝑒𝑙𝑎𝑦𝑡) (4) s.t. 𝑝𝑡∈{0.9, 1, 1.1}, 𝑞𝑡∈{available video bitrates}, (5) 𝑏𝑢𝑓𝑓𝑒𝑟𝑡< 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡, (6) where 𝑝𝑡, 𝑞𝑡, 𝑏𝑢𝑓𝑓𝑒𝑟𝑡, and 𝐵𝑊𝑡represent the playback speed, the played video quality level, the remaining video duration in the playout buffer, and the measured available throughput at time step 𝑡, respectively. 𝑐0,1,2,3 are the coefficients to set the impact of each sub-objective on the overall QoE in Eq. (4). 𝐹𝐷is the fragment duration as a static value during 𝑇-second live streaming. 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡is the target live latency as a kind of service-level agreement value assigned by the OTT application provider. Constraint (5) limits the range of the available playback speed and video quality values, while Constraint (6) makes sure players can only buffer content shorter than the target live latency. The inference module in Fig. 1 outputs the adaptive video quality 𝑞𝑡and playback speed 𝑝𝑡given an input set of observations (e.g., the past bandwidth measurements, the remaining

**[Limitaciones / riesgos / aplicabilidad | extracto 5 | p.5]**

Journal of Network and Computer Applications 205 (2022) 103451 5 I.M. Ozcelik and C. Ersoy a limited number of adjustable policy parameters represented as 𝜃. First, using the policy gradient theorem (Xu et al., 2021), we train the policy for the optimal 𝜃parameters to maximize the expected future reward expressed in Eq. (7). Then, we follow the gradient ∇𝜃𝐽(𝜃) of the expected cumulative reward with respect to the policy parameters in Eq. (9). ∇𝜃𝐽(𝜃) = ∇𝜃E𝜋𝜃 [𝐺𝑡 ] = E𝜋𝜃 [∇𝜃log 𝜋𝜃(𝑠, 𝑎)𝐴𝜋𝜃(𝑠, 𝑎) + 𝛽∇𝜃𝐻(𝜋𝜃(𝑠))] , where 𝐴𝜋𝜃(𝑠, 𝑎) = 𝑄𝜋𝜃(𝑠, 𝑎) −𝑉𝜋𝜃(𝑠). (9) Note that 𝑉(𝑠) is the expected future reward before any action is taken in state 𝑠, whereas 𝑄(𝑠, 𝑎), the Q-value, is the expected reward in state 𝑠after action 𝑎is performed. 𝐴𝜋𝜃(𝑠, 𝑎), the difference between them, is an indicator of how bad or good is a particular action given a particular state. It is also called the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value. Inspired by Pensieve (Mao et al., 2017), we also use an entropy component 𝐻(⋅) with the exploration factor 𝛽in Eq. (9) to trade off exploitation against exploration to obtain better policies as a standard approach in RL. During the training process, the policy parameters of the actor network are updated in each step in the direction of the gradient as in Eq. (10). 𝜃←𝜃+ 𝛼∇𝜃𝐽(𝜃), where 𝛼is the learning rate. (10) The learning agent empirically calculates the Q-value in our simulated environment after performing a sampled action of playback speed and video quality in the actor network output. As Eq. (10) needs the estimation of the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value that depends on 𝑉(𝑠), we use the critic network to approximate 𝑉(𝑠). To train the critic network, we use a multi-step Temporal Difference (TD) learning by getting inspired by Cui et al. (2021). So, the critic network gets the action taken by the actor ne

**[Limitaciones / riesgos / aplicabilidad | extracto 6 | p.6]**

Journal of Network and Computer Applications 205 (2022) 103451 6 I.M. Ozcelik and C. Ersoy Fig. 3. Training convergence to optimal policy parameters. Table 3 Comparison of all five approaches in terms of QoE and live latency. 5-min live sessions 20-min live sessions Avg. Total Reward (QoE) Avg. Live Latency (s) Avg. Total Reward (QoE) Avg. Live Latency (s) ALVS 35.8 ± 5.6 6.7 ± 0.2 154.9 ± 12.7 6.3 ± 0.1 TCLiVi 22.7 ± 5.4 5.5 ± 0.2 93.1 ± 12.3 6.1 ± 0.1 Pensieve 21.0 ± 4.3 6.9 ± 2.1 81.5 ± 32.3 7.8 ± 1.0 DASH.js 29.2 ± 9.4 5.9 ± 0.2 119.4 ± 26.2 6.1 ± 0.1 Baseline 30.1 ± 9.4 11.3 ± 0.4 132.3 ± 32.8 13.9 ± 0.3 Fig. 4. QoE improvement progress over validation set during training. the others despite a higher live latency due to the fixed adaptive playback speed because the QoE formula favors more on the video quality compared to the live delay. As similar to 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒, 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒 suffers from higher live latency because of the fixed playback speed. As 𝐷𝐴𝑆𝐻.𝑗𝑠uses an adaptive playback speed on top of 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒to catch up to the live event, it achieves a lower live latency. 𝑇𝐶𝐿𝑖𝑉𝑖follows the live events more closely at the expense of 40% less QoE than our approach because it is more conservative in video quality selection. As the total event duration increases, our approach also catches up with the live latency achieved by 𝑇𝐶𝐿𝑖𝑉𝑖. In the same manner, as the live event duration gets longer, the approaches with the fixed playback speed, 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒and 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒, manifest higher live latency because longer events have a higher risk of video stalls and the approaches with the fixed playback speed do not have any mechanism to re-catch up with the live event moment. Among the other three approaches with the adaptive playback speed, which are our approach, 𝑇𝐶𝐿𝑖𝑉𝑖, and 𝐷𝐴𝑆𝐻.𝑗𝑠, our approach

**[Limitaciones / riesgos / aplicabilidad | extracto 7 | p.7]**

Journal of Network and Computer Applications 205 (2022) 103451 7 I.M. Ozcelik and C. Ersoy Fig. 5. QoE scores of all the approaches over 15 5-min and 20-min live sessions. Fig. 6. Live latency changes over time. catching up with the live event time despite network fluctuations and video stalls. Second, our approach elaborated in Section 4.2 can adapt to highly varying network conditions without requiring any handcrafted threshold or heuristic. The same policy achieves low-latency

## 5. Figuras, tablas, algoritmos y ecuaciones detectadas por texto

**[elemento detectado 1 | p.1]**

Journal of Network and Computer Applications 205 (2022) 103451 Available online 17 June 2022 1084-8045/© 2022 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca ALVS: Adaptive Live Video Streaming using deep reinforcement learning Ihsan Mert Ozcelik ∗, Cem Ersoy Bogazici University, Istanbul, Turkey A R T I C L E I N F O Keywords: Adaptive playback speed Deep reinforcement learning Live streaming media and video quality A B S T R A C T Achieving a high Quality of Experience (QoE) in live event streaming is a challenging problem given a low-latency requirement and time-varying network conditions. Adaptive video bitrate and adaptive playback speed techniques are two separate control knobs to address this challenge. In this paper, we consider these two control parameters in a joint optimization problem and present a deep reinforcement learning (DRL) framework to maximize QoE for live streaming without any assumption about the environment or fixed rulebased heuristics. With the proposed DRL framework, our approach (ALVS) constructs the inference model to make a joint decision of adaptive playback speed and video quality level for the next video segment. Simulation results through real network traces show that ALVS outperforms both state-of-the-art DRL-based and rule

**[elemento detectado 2 | p.2]**

Journal of Network and Computer Applications 205 (2022) 103451 2 I.M. Ozcelik and C. Ersoy receives the action taken by the actor and the state space observations to estimate the maximum future award (i.e., the action value). As the value estimator, the critic network is later used to evaluate the action to accelerate to train the actor network; (3) we implement a playback simulator to emulate the adaptive playback speed and video quality selection in live events over DASH. We leverage this simulator in the training process to experience 8 h playback in only 10 s using real 4G traces in one epoch; (4) we perform extensive experiments to confront ALVS with both state-of-the-art DRL-based and rule-based solutions. The remaining parts of the paper are organized as follows. Section 2 surveys the related work by underlining the open issues in the literature and our novelty compared to the literature. Section 3 explains the system model and the formulation of the optimization problem. Section 4 elaborates our proposed RL framework. Section 5 presents an extensive performance evaluation and comparative analysis, followed by the conclusion and future work in Section 6. 2. Related work There is a large group of existing work on reducing end-to-end delay in HTTP live streaming, while aiming to achieve a high QoE. El Essaili et al. (2018) presented a prototype with 33 ms fragments using t

**[elemento detectado 3 | p.3]**

Journal of Network and Computer Applications 205 (2022) 103451 3 I.M. Ozcelik and C. Ersoy Table 1 Comparative table of highlighted studies. Study Goal Approach Action space (Output) Gap for live video streaming Mao et al. (2017) Learning video bitrate adaptation to maximize per-client QoE given changing environment DRL (A2C via a NN) Discreet video bitrates Does not consider live latency Mao et al. (2020) Evaluating Pensieve (Mao et al., 2017) via real-life deployment of millions of video-on-demand sessions DRL (A2C via a NN) Discreet Video Bitrates Does not consider live latency Bentaleb et al. (2018) Maximizing QoE fairness across video sessions Value-based RL Discreet Video Bitrates Does not consider live latency Claeys et al. (2014) Learning video bitrate adaptation to maximize per-client QoE given changing environment Value-based RL Discreet Video Bitrates Does not consider live latency Cui et al. (2021) Learning video bitrate and buffer thresholds to maximize per-client QoE given changing environment during live video streaming DRL (A2C via a NN) (Video Bitrates) x (2 Target Buffer Levels to choose playback speeds) Not choose playback speed explicitly. Instead, it uses hand-crafted buffer thresholds as a proxy to choose fast or slow playback speed, which cannot be generalized. Wang et al. (2019) Maximize per-client QoE given changing environment during live video streami

**[elemento detectado 4 | p.4]**

Journal of Network and Computer Applications 205 (2022) 103451 4 I.M. Ozcelik and C. Ersoy Fig. 1, while the content is being encoded at the OTT backend side. Our objective during this real-time process is to maximize QoE subject to the live latency target by choosing the played video quality level and playback speed for each video fragment. As the contributors to QoE during a live event streaming process are the played video quality, video quality fluctuations, video freezes, and end-to-end latency between capturing and rendering the event moment, we define QoE model as the weighed sum of these four sub-objectives. This objective can be mathematically expressed as the following: max 𝑝𝑡,𝑞𝑡 𝑇∑ 𝑡=0 𝑄𝑜𝐸𝑡, (1) where 𝑄𝑜𝐸𝑡= (𝑐0 ∗𝑞𝑡 (2) −𝑐1 ∗𝑚𝑎𝑥(0, ((𝑏𝑢𝑓𝑓𝑒𝑟𝑡+ 𝐹𝐷) 𝑝𝑡 ) −(𝐹𝐷∗ 𝑞𝑡 𝐵𝑊𝑡 )) (3) −𝑐2 ∗(|𝑞𝑡−𝑞𝑡−1|) −𝑐3 ∗𝑙𝑖𝑣𝑒_𝑑𝑒𝑙𝑎𝑦𝑡) (4) s.t. 𝑝𝑡∈{0.9, 1, 1.1}, 𝑞𝑡∈{available video bitrates}, (5) 𝑏𝑢𝑓𝑓𝑒𝑟𝑡< 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡, (6) where 𝑝𝑡, 𝑞𝑡, 𝑏𝑢𝑓𝑓𝑒𝑟𝑡, and 𝐵𝑊𝑡represent the playback speed, the played video quality level, the remaining video duration in the playout buffer, and the measured available throughput at time step 𝑡, respectively. 𝑐0,1,2,3 are the coefficients to set the impact of each sub-objective on the overall QoE in Eq. (4). 𝐹𝐷is the fragment duration as a static value during 𝑇-second live streaming. 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡is the target live latency as a kind of service-level agreement value assigned by

**[elemento detectado 5 | p.5]**

Journal of Network and Computer Applications 205 (2022) 103451 5 I.M. Ozcelik and C. Ersoy a limited number of adjustable policy parameters represented as 𝜃. First, using the policy gradient theorem (Xu et al., 2021), we train the policy for the optimal 𝜃parameters to maximize the expected future reward expressed in Eq. (7). Then, we follow the gradient ∇𝜃𝐽(𝜃) of the expected cumulative reward with respect to the policy parameters in Eq. (9). ∇𝜃𝐽(𝜃) = ∇𝜃E𝜋𝜃 [𝐺𝑡 ] = E𝜋𝜃 [∇𝜃log 𝜋𝜃(𝑠, 𝑎)𝐴𝜋𝜃(𝑠, 𝑎) + 𝛽∇𝜃𝐻(𝜋𝜃(𝑠))] , where 𝐴𝜋𝜃(𝑠, 𝑎) = 𝑄𝜋𝜃(𝑠, 𝑎) −𝑉𝜋𝜃(𝑠). (9) Note that 𝑉(𝑠) is the expected future reward before any action is taken in state 𝑠, whereas 𝑄(𝑠, 𝑎), the Q-value, is the expected reward in state 𝑠after action 𝑎is performed. 𝐴𝜋𝜃(𝑠, 𝑎), the difference between them, is an indicator of how bad or good is a particular action given a particular state. It is also called the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value. Inspired by Pensieve (Mao et al., 2017), we also use an entropy component 𝐻(⋅) with the exploration factor 𝛽in Eq. (9) to trade off exploitation against exploration to obtain better policies as a standard approach in RL. During the training process, the policy parameters of the actor network are updated in each step in the direction of the gradient as in Eq. (10). 𝜃←𝜃+ 𝛼∇𝜃𝐽(𝜃), where 𝛼is the learning rate. (10) The learning agent empirically calculates the Q-value in our simulated environment after pe

**[elemento detectado 6 | p.6]**

Journal of Network and Computer Applications 205 (2022) 103451 6 I.M. Ozcelik and C. Ersoy Fig. 3. Training convergence to optimal policy parameters. Table 3 Comparison of all five approaches in terms of QoE and live latency. 5-min live sessions 20-min live sessions Avg. Total Reward (QoE) Avg. Live Latency (s) Avg. Total Reward (QoE) Avg. Live Latency (s) ALVS 35.8 ± 5.6 6.7 ± 0.2 154.9 ± 12.7 6.3 ± 0.1 TCLiVi 22.7 ± 5.4 5.5 ± 0.2 93.1 ± 12.3 6.1 ± 0.1 Pensieve 21.0 ± 4.3 6.9 ± 2.1 81.5 ± 32.3 7.8 ± 1.0 DASH.js 29.2 ± 9.4 5.9 ± 0.2 119.4 ± 26.2 6.1 ± 0.1 Baseline 30.1 ± 9.4 11.3 ± 0.4 132.3 ± 32.8 13.9 ± 0.3 Fig. 4. QoE improvement progress over validation set during training. the others despite a higher live latency due to the fixed adaptive playback speed because the QoE formula favors more on the video quality compared to the live delay. As similar to 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒, 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒 suffers from higher live latency because of the fixed playback speed. As 𝐷𝐴𝑆𝐻.𝑗𝑠uses an adaptive playback speed on top of 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒to catch up to the live event, it achieves a lower live latency. 𝑇𝐶𝐿𝑖𝑉𝑖follows the live events more closely at the expense of 40% less QoE than our approach because it is more conservative in video quality selection. As the total event duration increases, our approach also catches up with the live latency achieved by 𝑇𝐶𝐿𝑖𝑉𝑖. In the same manner, as the live event duration gets long

**[elemento detectado 7 | p.7]**

Journal of Network and Computer Applications 205 (2022) 103451 7 I.M. Ozcelik and C. Ersoy Fig. 5. QoE scores of all the approaches over 15 5-min and 20-min live sessions. Fig. 6. Live latency changes over time. catching up with the live event time despite network fluctuations and video stalls. Second, our approach elaborated in Section 4.2 can adapt to highly varying network conditions without requiring any handcrafted threshold or heuristic. The same policy achieves low-latency

## 6. Texto crudo extraído del cuerpo principal por página

> Esta sección conserva el texto extraído página a página hasta referencias/bibliografía cuando se detecta. Se incluye para no perder detalles de método, entrenamiento, datos o evaluación. Puede tener problemas de orden de columnas o fórmulas por naturaleza del PDF.

### Página 1

Journal of Network and Computer Applications 205 (2022) 103451
Available online 17 June 2022
1084-8045/© 2022 Elsevier Ltd. All rights reserved.
Contents lists available at ScienceDirect
Journal of Network and Computer Applications
journal homepage: www.elsevier.com/locate/jnca
ALVS: Adaptive Live Video Streaming using deep reinforcement learning
Ihsan Mert Ozcelik ∗, Cem Ersoy
Bogazici University, Istanbul, Turkey
A R T I C L E
I N F O
Keywords:
Adaptive playback speed
Deep reinforcement learning
Live streaming media and video quality
A B S T R A C T
Achieving a high Quality of Experience (QoE) in live event streaming is a challenging problem given a
low-latency requirement and time-varying network conditions. Adaptive video bitrate and adaptive playback
speed techniques are two separate control knobs to address this challenge. In this paper, we consider these
two control parameters in a joint optimization problem and present a deep reinforcement learning (DRL)
framework to maximize QoE for live streaming without any assumption about the environment or fixed rulebased heuristics. With the proposed DRL framework, our approach (ALVS) constructs the inference model to
make a joint decision of adaptive playback speed and video quality level for the next video segment. Simulation
results through real network traces show that ALVS outperforms both state-of-the-art DRL-based and rule-based
algorithms in terms of QoE without sacrificing live latency and skipping any content.
1. Introduction
Live event streaming is growing in popularity as over-the-top (OTT)
service providers are procuring broadcasting rights of worldwide premium sports events like English Premier League, ATP Tour Tennis,
Major League Baseball, American National Football League with 5G
infrastructure rolling out more and more. At that point, Dynamic
Adaptive Streaming over HTTP (DASH) is the most promising approach
for the rapid deployment of the infrastructure of those live events due
to its existing wide adoption for Video-on-Demand (VoD) use cases.
In DASH, the multiple quality versions of the same content at
different encoding bitrates are kept at the OTT back-end side. Each
version is split into small segments. Segment duration and boundaries
are the same among all versions of the same content. It enables players
to choose the appropriate video quality and switch based on the clientside decision to adapt to the varying network conditions (Mondal and
Chakraborty, 2020).
DASH has been initially designed for VoD to serve previouslystored videos. Hence, legacy DASH players struggle to achieve low
latency and a high QoE simultaneously in live sports events. The live
latency in this context means the time difference from capturing to
rendering a particular moment of the event. The challenge of DASH
players is to catch up terrestrial cable latencies in the broadcast world
characterized by a 5 to 10-s latency (Petrangeli et al., 2018) while
maximizing viewers’ Quality-of-Experience (QoE). They buffer a few
segments to start playback (e.g., three 10-s segments in Apple HLS,
which causes about a 40-s lag between a viewer’s screen and the event).
Any stall during the stream also adds to this delay. Such delays ruin
∗Corresponding author.
E-mail addresses: mert.ozcelik@boun.edu.tr (I.M. Ozcelik), cem.ersoy@boun.edu.tr (C. Ersoy).
the viewer’s QoE with a high risk of the spoiler effect. To mitigate,
adaptive playback speed, in addition to adaptive video bitrates, is used
by relying on the assumption that variations in the playback speed of
10% or less are not perceptually noticeable to viewers (Kalman et al.,
2004). So, the player speeds up or slows down the playback rate within
the range of (0.9, 1.1) to keep itself close to a target latency.
In this paper, we consider adaptive playback speed and video
quality decision as a joint optimization problem. We implement Deep
Reinforcement Learning (DRL) framework to learn video bitrate and
playback speed adaptation strategy to maximize QoE for live video
streaming without any assumption about the environment or fixed rulebased heuristics. We also aim to keep live latency low without skipping
any content. We compare our approach (ALVS) with state-of-the-art
solutions under real 4G traces.
Our main contribution is to perform a joint inference of playback
speed and video bitrate selection after training the system to learn a
strategy to obtain a high QoE with low latency via our DRL framework.
To achieve this, we make the following contributions: (1) we represent
the state space from the key observations of player, the action space
of the available video bitrates and three playback speed levels, and
a reward function in the form of a combined formula of QoE and
live latency; (2) we construct a neural network to provide the best
action for a given state to map the state space to a joint decision of
playback speed and video bitrate levels for the next video segment.
To train the model, we utilize Asynchronous Actor–Critic algorithm
(A3C), a state-of-the-art reinforcement learning (RL) algorithm, by
introducing another neural network called the critic network, which
https://doi.org/10.1016/j.jnca.2022.103451
Received 15 November 2021; Received in revised form 9 May 2022; Accepted 8 June 2022

### Página 2

Journal of Network and Computer Applications 205 (2022) 103451
2
I.M. Ozcelik and C. Ersoy
receives the action taken by the actor and the state space observations
to estimate the maximum future award (i.e., the action value). As the
value estimator, the critic network is later used to evaluate the action
to accelerate to train the actor network; (3) we implement a playback
simulator to emulate the adaptive playback speed and video quality
selection in live events over DASH. We leverage this simulator in the
training process to experience 8 h playback in only 10 s using real 4G
traces in one epoch; (4) we perform extensive experiments to confront
ALVS with both state-of-the-art DRL-based and rule-based solutions.
The remaining parts of the paper are organized as follows. Section 2
surveys the related work by underlining the open issues in the literature and our novelty compared to the literature. Section 3 explains
the system model and the formulation of the optimization problem.
Section 4 elaborates our proposed RL framework. Section 5 presents an
extensive performance evaluation and comparative analysis, followed
by the conclusion and future work in Section 6.
2. Related work
There is a large group of existing work on reducing end-to-end delay
in HTTP live streaming, while aiming to achieve a high QoE.
El Essaili et al. (2018) presented a prototype with 33 ms fragments
using the chunked transfer to reduce latency without taking into account optimal video bitrate selection and measuring the overall QoE.
Van Der Hooft et al. (2018) introduced a new low-latency approach
for live streaming based on HTTP/2’s push feature and super-short
segments. It reduces end-to-end latency within the range of eight to
ten seconds. In contrast, it brings about longer video freeze times compared to the legacy HTTP/1.1 approaches due to encoding overhead
of super-short segments and conventional pull-based ABR deficiencies
in HTTP/2 push-based models. Yahia et al. (2019) described another
HTTP/2-based approach by proposing frame discarding to achieve
low-latency video streaming. Moreover, the intuitive way to reduce
the live latency in the legacy HTTP/1.1 approaches is to shorten the
fragment duration. However, it also causes numerous drawbacks such
as a dramatic increase in the number of HTTP requests and responses,
a few multiples of the relevant round-trip times, diminished visual
quality, and excessive rates of switches between different video quality
levels. To resolve the latency problem of live streaming over DASH at
scale without all those drawbacks and sacrificing QoE of end-users, the
MPEG CMAF packaging through HTTP 1.1 chunked encoding transfer
is introduced. It allows DASH to achieve low latency in live streaming,
as demonstrated in Akamai (2019). A segment in CMAF consists of
multiple small pieces called chunks, i.e., the smallest decodable units.
With the HTTP chunked transfer, it enables to distribute segments by
chunks (e.g., even 100 ms content) while keeping all main advantages
of DASH systems such as quality switching at segment boundaries,
leveraging the caches in content delivery networks (CDNs), only one
request for each segment and firewall friendliness. As illustrated in
Fig. 1, our proposed system model in ALVS also utilizes the MPEG
CMAF packaging through HTTP 1.1 chunked encoding transfer.
The HTTP Chunked Encoded transfer of CMAF segments brings
extra complexities to conventional ABRs. First, the buffered content
duration should be short (e.g., less than a few seconds) to limit the
delay from the actual event to users’ screens. It prevents buffer-based
solutions (e.g., BOLA Spiteri et al., 2016) from achieving a high QoE
due to frequent video quality changes because buffer occupancy bars
to increase or decrease the quality are extremely close to each other.
In other words, legacy buffer-based ABR solutions are not effective in
low-latency live streaming. Second, there are also recent workarounds
for the ABR problems in HTTP 1.1 chunked encoding CMAF packages
through throughput-based adaptive bitrate algorithms and a parallel
playback speed adaptation mechanism. Similarly, DASH.js (Forum,
2017) introduces adaptive playback speed heuristics independent from
the video bitrate selection in their ABR algorithms. On top of DASH.js,
STALLION (Gutterman et al., 2020) benefits from DASH.js for playback
speed adaption as it drives only video bitrate selection to strive for lowlatency live streaming. So, it does not solve a joint decision problem
of playback speed and video quality level. As another example on top
of DASH.js, 𝐿𝑜𝐿(Low-on-Latency) (Lim et al., 2020) also emphasizes
the impact of the encoder-side idle times on the inaccurate throughput
measurement and introduces a novel throughput measurement module
by parsing the chunk payloads to identify chunk boundaries based on
the headers (i.e., 𝑚𝑜𝑜𝑓box) in fragmented MP4 data. It is aimed at
determining the idle periods explicitly using chunk boundary identifications. As a follow-up study, Bentaleb et al. in Bentaleb et al.
(2021) also propose 𝐿𝑜𝐿+ to enable the wide deployment of 𝐿𝑜𝐿
by introducing a novel adaptive playback speed control mechanism
and configurable QoE objectives rather than the singular QoE. Third,
we presented a purely client-based heuristic to measure the available
bandwidth by approximating the idle times at the encoder side and the
active download times of all the chunks limited by only network status
in live streaming over DASH (Ozcelik and Ersoy, 2020).
Machine learning-based frameworks are widely used to enhance
QoE in DASH systems. Petrangeli et al. (2017) present one of the first
machine learning-based approaches by predicting possible video freezes
and prioritizing the delivery of the relevant fragment downloads, while
utilizing active network programming based on the Software-defined
Networking paradigm. There are also numerous studies in the literature
based on DRL-based Adaptive Bitrate (ABR) mechanisms rather than
rule-based heuristics to choose the appropriate video quality level
and update it depending on changing network conditions to maximize
viewers’ QoE. For example, Pensieve (Mao et al., 2017) uses DRL to
select video bitrates to achieve a high QoE in DASH after training a
neural network model with the observations collected by players in
VoD use cases. Inspired by Pensieve, TCLiVi (Cui et al., 2021) uses
the same DRL framework for live streaming to decide the video quality
level and the target buffer level that players aim to maintain as the
minimum content duration required by the player. The buffer level is
used as a proxy in TCLiVi for the slow and fast playback speeds, which
slows down the payback to avoid a video freeze and speeds up the
video player to reduce latency, respectively. CBLC (Hong et al., 2019)
also uses DRL to decide the latency limit to skip content to catch up
to the live edge. However, none of them consider CMAF packaging
over short-duration chunks and directly choose playback speed as the
output of the DRL process. Instead, they select playback speed via
hand-crafted thresholds of the delta between the target buffer and the
current buffer duration. Furthermore, Wang et al. (2019) designed a
new ABR algorithm called 𝐵𝑖𝑡𝐿𝑎𝑡for the Live Video Streaming Grand
Challenge (Yi et al., 2019) in which there exists a frame-level live video
simulator for participants to implement ABR algorithms and benchmark. 𝐵𝑖𝑡𝐿𝑎𝑡benefits from reinforcement learning to provide adaptive
latency limits, control playback rate and skip content to achieve a target
latency. Moreover, Sun et al. in two related works (i.e., Sun et al.
(2021a) and Sun et al. (2021b)) use deep reinforcement learning to
choose the adaptive video bitrate and playback speed in chunk-based
video packaging and streaming over HTTP, while aiming to balance
video quality, playback latency, video freeze and skip. Their approach
skips the content to catch up with the live event in case live latency
is increasing; whereas our proposed approach ALVS guarantees that
all the moments of the live events are rendered without dropping any
content.
In summary, our novelty compared to previous approaches explained above is to perform a joint inference of playback speed and
video bitrate selection for low-latency live streaming. Our contribution
on top of the existing DRL-based approaches summarized in Table 1
is to choose playback speed as the direct output of the DRL process
without using any hand-crafted threshold and skipping any content. In
other words, we address all the gaps of the existing studies highlighted
in Table 1.

### Página 3

Journal of Network and Computer Applications 205 (2022) 103451
3
I.M. Ozcelik and C. Ersoy
Table 1
Comparative table of highlighted studies.
Study
Goal
Approach
Action space (Output)
Gap for live video
streaming
Mao et al.
(2017)
Learning video bitrate adaptation to
maximize per-client QoE given changing
environment
DRL (A2C via a NN)
Discreet video bitrates
Does not consider live
latency
Mao et al.
(2020)
Evaluating Pensieve (Mao et al., 2017)
via real-life deployment of millions of
video-on-demand sessions
DRL (A2C via a NN)
Discreet Video
Bitrates
Does not consider live
latency
Bentaleb
et al. (2018)
Maximizing QoE fairness across video
sessions
Value-based RL
Discreet Video
Bitrates
Does not consider live
latency
Claeys et al.
(2014)
Learning video bitrate adaptation to
maximize per-client QoE given changing
environment
Value-based RL
Discreet Video
Bitrates
Does not consider live
latency
Cui et al.
(2021)
Learning video bitrate and buffer
thresholds to maximize per-client QoE
given changing environment during live
video streaming
DRL (A2C via a NN)
(Video Bitrates) x (2
Target Buffer Levels
to choose playback
speeds)
Not choose playback
speed explicitly. Instead,
it uses hand-crafted
buffer thresholds as a
proxy to choose fast or
slow playback speed,
which cannot be
generalized.
Wang et al.
(2019)
Maximize per-client QoE given changing
environment during live video streaming
DRL (A2C via a NN)
(Video Bitrates) x (2
Target Buffer Levels
to choose playback
speeds) x (Latency
Limit to skip frames)
The same behavior with
TcLiVi Cui et al. (2021)
as it also skips content to
catch up with the live
event.
Hong et al.
(2019)
Maximize per-client QoE given changing
environment during live video streaming
DRL (A2C via a NN)
(Discreet Video
Bitrates) x (2 Target
Buffer Levels to
choose playback
speeds) x (Latency
Limit to skip frames)
The same behavior with
BitLat Wang et al.
(2019).
Sun et al.
(2021a) and
Sun et al.
(2021b)
Choose optimal video bitrate and
playback speed given changing
environment during live video streaming
DRL (Q-Network)
(Discreet Video
Bitrates) x (5
different playback
speeds) x (Whether to
skip content)
It skips content to catch
up with the live event. It
also has a larger action
space, which reduces the
efficiency of exploration
of the optimal policy
during training.
Our work
(ALVS)
Learning video bitrate and playback
speed adaptation jointly to maximize
per-client QoE given changing
environment during live video streaming
DRL (A2C via a NN)
(Discreet Video
Bitrates) x (3 different
playback speeds)
No gap, follows the live
stream continuously.
Fig. 1. The proposed system of DRL-based Adaptive Live Streaming over HTTP Chunked Encoded Transfer of CMAF segments.
3. System model and formulation of the problem
In this study, the considered multimedia delivery system between
DASH clients and servers supports HTTP chunked encoding transfer of
CMAF packages. Chunks are encoded and packaged to different quality
levels at the server-side. The packager output is immediately transferred to the live origin chunk-by-chunk for distribution. So, chunks
can be posted to the network without waiting to encode the whole
segment. Note that the content representation and data flow are fully
compatible with legacy DASH systems as players are informed about
the available video quality levels via the manifest files fetched at the
beginning of each session. At any time, players download only one
quality representation and they can switch the quality level at the
fragment boundaries.
Players can be simultaneously pulling chunks of the CMAF segment
at a specific video quality chosen by the inference module as shown in

### Página 4

Journal of Network and Computer Applications 205 (2022) 103451
4
I.M. Ozcelik and C. Ersoy
Fig. 1, while the content is being encoded at the OTT backend side. Our
objective during this real-time process is to maximize QoE subject to the
live latency target by choosing the played video quality level and playback speed for each video fragment. As the contributors to QoE during a
live event streaming process are the played video quality, video quality
fluctuations, video freezes, and end-to-end latency between capturing
and rendering the event moment, we define QoE model as the weighed
sum of these four sub-objectives. This objective can be mathematically
expressed as the following:
max
𝑝𝑡,𝑞𝑡
𝑇∑
𝑡=0
𝑄𝑜𝐸𝑡,
(1)
where 𝑄𝑜𝐸𝑡= (𝑐0 ∗𝑞𝑡
(2)
−𝑐1 ∗𝑚𝑎𝑥(0, ((𝑏𝑢𝑓𝑓𝑒𝑟𝑡+ 𝐹𝐷)
𝑝𝑡
) −(𝐹𝐷∗
𝑞𝑡
𝐵𝑊𝑡
))
(3)
−𝑐2 ∗(|𝑞𝑡−𝑞𝑡−1|) −𝑐3 ∗𝑙𝑖𝑣𝑒_𝑑𝑒𝑙𝑎𝑦𝑡)
(4)
s.t.
𝑝𝑡∈{0.9, 1, 1.1}, 𝑞𝑡∈{available video bitrates},
(5)
𝑏𝑢𝑓𝑓𝑒𝑟𝑡< 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡,
(6)
where 𝑝𝑡, 𝑞𝑡, 𝑏𝑢𝑓𝑓𝑒𝑟𝑡, and 𝐵𝑊𝑡represent the playback speed, the played
video quality level, the remaining video duration in the playout buffer,
and the measured available throughput at time step 𝑡, respectively.
𝑐0,1,2,3 are the coefficients to set the impact of each sub-objective on the
overall QoE in Eq. (4). 𝐹𝐷is the fragment duration as a static value
during 𝑇-second live streaming. 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡is the target live latency as a
kind of service-level agreement value assigned by the OTT application
provider. Constraint (5) limits the range of the available playback speed
and video quality values, while Constraint (6) makes sure players can
only buffer content shorter than the target live latency.
The inference module in Fig. 1 outputs the adaptive video quality
𝑞𝑡and playback speed 𝑝𝑡given an input set of observations (e.g., the
past bandwidth measurements, the remaining buffer size, the current
live latency, the next available video segment sizes). The decision
mechanism within the inference module relies on a neural network with
the policy parameters. The neural network’s training process and its
design to generate those parameters are elaborated in the proposed RL
framework as discussed in the next section.
4. The proposed RL framework
4.1. RL problem definition
We model the interactions between an agent and the environment
in time-varying network and player conditions as a Markov Decision
Process (MDP) represented by a sequence of states, actions, and rewards.
State 𝑠𝑡at a specific time 𝑡is the observation of the environment
which is enough to determine the next state 𝑠𝑡+1. The action is taken
by the agent to lead to a state transition. In our problem, the agent
is our inference module that controls adaptive playback speed and
video quality. The reward 𝑟𝑡is the immediate feedback signal of the
environment as a result of the 𝑎𝑡at time step 𝑡.
In our RL task, given a MDP we aim to find a policy, i.e., a mapping
from states to actions, that maximizes the expected sum of future
rewards in Eq. (7). The policy function 𝜋∶𝑆↦𝐴chooses the action
𝑎𝑡∈𝐴given the current state 𝑠𝑡∈𝑆, that gains 𝑟𝑡.
𝐺𝑡=
∞
∑
𝑡=0
𝛾𝑡𝑟𝑡,
(7)
where 𝛾∈(0, 1] is the discount factor to trade-off present and future
rewards and 𝑡= 0 is the current time.
Fig. 2. The proposed actor–critic architecture.
We explain our state and action spaces, and reward function as
follows:
State space: We use the playing video bitrate, bandwidth measurement, the download time of the last segment, the remaining buffer size,
the current live latency, the next available video segment sizes, and the
number of the remaining segments until the end of the live events as
the observation signals to determine the next state.
Action space: It includes 𝑁∗𝐾combinations, where 𝑁is the
number of the available video quality levels, and 𝐾is the number of
playback speed levels.
Reward Function: We represent 𝑟𝑡in the form of a combined QoE
expression used by Cui et al. (2021) as in Eq. (8). As in line with
the objective function presented in Eq. (4), it is aimed to balance four
sub-objectives relying on the coefficients of each QoE contributor such
as the played video bitrate, video stall duration, the quality switch
compared to the quality of the previous fragment, and latency between
capturing and rendering the segment of live event.
𝑟𝑡=𝑐0 ∗𝑉𝑄𝑡−𝑐1 ∗𝑠𝑡𝑎𝑙𝑙_𝑑𝑢𝑟𝑎𝑡𝑖𝑜𝑛𝑡
−𝑐2 ∗|𝑉𝑄𝑡−𝑉𝑄𝑡−1| −𝑐3 ∗𝑙𝑖𝑣𝑒_𝑑𝑒𝑙𝑎𝑦𝑡,
(8)
where 𝑉𝑄𝑡is the video bitrate at time step 𝑡.
Environment: The system model of live streaming via DASH in timevarying network conditions in Section 2 serves as the environment of
the proposed RL framework.
4.2. The proposed actor–critic algorithm
As shown Fig. 2, we use an actor–critic architecture. The actor
outputs the policy 𝜋for any state 𝑠, a vector of probabilities of each
action alternative across 𝑁
∗𝐾combinations. As the state space
is at a tremendous scale due to continuous discrete values of input
features, we utilize a neural network to approximate the policy 𝜋𝜃with

### Página 5

Journal of Network and Computer Applications 205 (2022) 103451
5
I.M. Ozcelik and C. Ersoy
a limited number of adjustable policy parameters represented as 𝜃.
First, using the policy gradient theorem (Xu et al., 2021), we train the
policy for the optimal 𝜃parameters to maximize the expected future
reward expressed in Eq. (7). Then, we follow the gradient ∇𝜃𝐽(𝜃) of
the expected cumulative reward with respect to the policy parameters
in Eq. (9).
∇𝜃𝐽(𝜃) = ∇𝜃E𝜋𝜃
[𝐺𝑡
]
= E𝜋𝜃
[∇𝜃log 𝜋𝜃(𝑠, 𝑎)𝐴𝜋𝜃(𝑠, 𝑎) + 𝛽∇𝜃𝐻(𝜋𝜃(𝑠))] ,
where 𝐴𝜋𝜃(𝑠, 𝑎) = 𝑄𝜋𝜃(𝑠, 𝑎) −𝑉𝜋𝜃(𝑠).
(9)
Note that 𝑉(𝑠) is the expected future reward before any action is
taken in state 𝑠, whereas 𝑄(𝑠, 𝑎), the Q-value, is the expected reward
in state 𝑠after action 𝑎is performed. 𝐴𝜋𝜃(𝑠, 𝑎), the difference between
them, is an indicator of how bad or good is a particular action given
a particular state. It is also called the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value. Inspired by
Pensieve (Mao et al., 2017), we also use an entropy component 𝐻(⋅)
with the exploration factor 𝛽in Eq. (9) to trade off exploitation against
exploration to obtain better policies as a standard approach in RL.
During the training process, the policy parameters of the actor network
are updated in each step in the direction of the gradient as in Eq. (10).
𝜃←𝜃+ 𝛼∇𝜃𝐽(𝜃), where 𝛼is the learning rate.
(10)
The learning agent empirically calculates the Q-value in our simulated environment after performing a sampled action of playback speed
and video quality in the actor network output. As Eq. (10) needs the
estimation of the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value that depends on 𝑉(𝑠), we use the
critic network to approximate 𝑉(𝑠). To train the critic network, we
use a multi-step Temporal Difference (TD) learning by getting inspired
by Cui et al. (2021). So, the critic network gets the action taken by the
actor network and estimates 𝑉(𝑠) that is later used to update the policy
parameters depending on the 𝑎𝑑𝑣𝑎𝑛𝑡𝑎𝑔𝑒value.
Once we generate the policy parameters after training two neural
networks, we deploy only the actor network with the policy parameters
to players. In the inference module, we continuously feed the instantaneous state space information to decide the video quality per each
segment and playback speed level over time.
5. Computational experiments
5.1. Experiment setup
We extend 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒’s simulator by adding new features to emulate
adaptive playback speed and the real-time nature of content streaming
in which the player is not allowed to download future content even
if the network capacity and the play-out buffer capacity allow. To
mimic the environment, we use real network traces (Riiser et al., 2013)
collected in Norway from different-type vehicles such as train, tram,
metro, bus, car and ferry. Our test video is encoded to 𝑁= 6 different
quality levels at {300, 750, 1200, 1850, 2850, 4300} kbps, and each
video fragment is four seconds long, while each live event has a total
duration of 20 min. Our player simulator supports 𝐾= 3 playback
speed levels at {0.9, 1, 1.1}. So, in our action space, we have 𝑁∗
𝐾= 18 discrete alternatives for the joint decision of playback speed
and video quality. We set the player buffer limit to one fragment. So,
our target live latency 𝑇𝑙𝑖𝑣𝑒_𝑡𝑎𝑟𝑔𝑒𝑡is 4 s.
5.2. Training details and QoE coefficients
All the hyper-parameters used in training are shown in Table 2. All
of them are kept static during the training process except for 𝛽. We start
with 𝛽= 4 and gradually reduce it to 0.2. We realized that 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒and
𝑇𝑐𝐿𝑖𝑉𝑖used the common hyper-parameter values for the same neural
network backbone. Thus, we did not use any further hyper-parameter
tuning, and continued with their hyper-parameters.
Table 2
Training parameters.
Parameter
Value
𝛼𝑎𝑐𝑡𝑜𝑟(learning rate)
0.001
𝛼𝑐𝑟𝑖𝑡𝑖𝑐(learning rate)
0.0001
𝛽(entropy weight)
4 to 0.2
𝛽𝐸𝑃𝑆(entropy constant)
0.000001
𝛾(discount factor)
0.99
batch size
48
The entire training process took about 200,000 epochs to converge.
Fig. 3 reflects the training convergence through the TD loss and avg.
entropy values over the last 100,000 epochs. In each step, seven
features of the state space explained in Section 3 are forwarded to the
input layer. At the same time, eight past throughput measurements and
the next available video segment sizes are first passed into a standard
1D-CNN. Then, we have a hidden layer of 128 neurons where the
results of the input layer go through a fully connected network with
the activation function of 𝑅𝑒𝐿𝑈. Input and hidden layers have the same
structure in the actor and critic networks, as depicted in Fig. 2, whereas
the output layer differs. We use the softmax function in the output layer
of the actor network that gives the probability distribution over 18
combinations of playback speed and video bitrate. In contrast, the critic
network has a linear neuron in the output layer for the expected future
reward. We use TensorFlow to implement and train these networks. We
use 70% of the network traces for the training data, 15% as a crossvalidation validation set, and keep the rest as an independent test set
for the comparison with the others. We also run a cross-validation on
unseen network traces every 500 epochs during the last 100,000 epochs
of the training process, and archived the mean, median and TP95 of the
reward values (i.e., a proxy for users’ QoE) across those 20 live video
sessions. The cross-validation results are shown in Fig. 4.
In the training process, the coefficients of each QoE contributor in
the reward function in Eq. (4) are chosen as the same with 𝑇𝐶𝐿𝑖𝑉𝑖(Cui
et al., 2021) for a fair comparison using the same units with 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒
and 𝑇𝐶𝐿𝑖𝑉𝑖, while 𝑐0, 𝑐1, 𝑐2, and 𝑐3 are set to 1, 1.5, 0.005, and 0.02
respectively. These can be straightforwardly adapted to reflect the
different QoE preferences, and the training process can be repeated
using the updated reward function and the same parameters in Table 2.
E.g., if reducing live delay is more critical, the penalty factor of the
relevant component (i.e., 𝑐3) can be increased. An extensive study can
be found in Segura-Garcia et al. (2018) to define different reward
functions based on various estimated mean opinion score formulas for
the subjective video quality of experience evaluation.
5.3. Results
5.3.1. Comparative analysis
Our approach (ALVS) is compared to the following state-of-theart algorithms: (1) 𝑇𝐶𝐿𝑖𝑉𝑖uses DRL-based adaptive video bitrate
and target buffer selection that is later used to choose the playback
speed. (2) 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒uses DRL-based adaptive video bitrate with a fixed
playback speed for VoD use case. For a fair comparison, we re-train its
model by replacing the reward function with the same QoE formula
as in Eq. (4) used by TCLiVi and our approach. (3) 𝐷𝐴𝑆𝐻.𝑗𝑠is a
commercial player developed by DASH Industry Forum that supports
low-latency mode with adaptive playback speed. We use a throughputbased ABR version in our comparative analysis. (4) 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒uses a
throughput-based ABR with a fixed playback speed.
We run each approach under the same network traces in 15 5-min
and 20-min live sessions. Table 3 summarizes the QoE scores and live
delays with the mean and 95% confidence interval values over all the
sessions. It clearly shows that our approach outperforms the others in
terms of the total reward in the form of a QoE score without sacrificing
the live latency considerably. 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒gives a better QoE score across

### Página 6

Journal of Network and Computer Applications 205 (2022) 103451
6
I.M. Ozcelik and C. Ersoy
Fig. 3. Training convergence to optimal policy parameters.
Table 3
Comparison of all five approaches in terms of QoE and live latency.
5-min
live sessions
20-min
live sessions
Avg. Total
Reward (QoE)
Avg. Live
Latency (s)
Avg. Total
Reward (QoE)
Avg. Live
Latency (s)
ALVS
35.8 ± 5.6
6.7 ± 0.2
154.9 ± 12.7
6.3 ± 0.1
TCLiVi
22.7 ± 5.4
5.5 ± 0.2
93.1 ± 12.3
6.1 ± 0.1
Pensieve
21.0 ± 4.3
6.9 ± 2.1
81.5 ± 32.3
7.8 ± 1.0
DASH.js
29.2 ± 9.4
5.9 ± 0.2
119.4 ± 26.2
6.1 ± 0.1
Baseline
30.1 ± 9.4
11.3 ± 0.4
132.3 ± 32.8
13.9 ± 0.3
Fig. 4. QoE improvement progress over validation set during training.
the others despite a higher live latency due to the fixed adaptive
playback speed because the QoE formula favors more on the video
quality compared to the live delay. As similar to 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒, 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒
suffers from higher live latency because of the fixed playback speed. As
𝐷𝐴𝑆𝐻.𝑗𝑠uses an adaptive playback speed on top of 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒to catch
up to the live event, it achieves a lower live latency. 𝑇𝐶𝐿𝑖𝑉𝑖follows
the live events more closely at the expense of 40% less QoE than our
approach because it is more conservative in video quality selection.
As the total event duration increases, our approach also catches up
with the live latency achieved by 𝑇𝐶𝐿𝑖𝑉𝑖. In the same manner, as the
live event duration gets longer, the approaches with the fixed playback
speed, 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒and 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒, manifest higher live latency because
longer events have a higher risk of video stalls and the approaches
with the fixed playback speed do not have any mechanism to re-catch
up with the live event moment. Among the other three approaches
with the adaptive playback speed, which are our approach, 𝑇𝐶𝐿𝑖𝑉𝑖,
and 𝐷𝐴𝑆𝐻.𝑗𝑠, our approach is the only mechanism which achieves to
reduce the average live latency as event duration increases from 5 min
to 20 min. It also indicates that our approach, ALVS, is more effective
in longer live events to deliver low-latency live streaming.
Fig. 5 represents the box plots of the QoE scores in all sessions
through their quartiles. As illustrated in Fig. 5, there is a greater variability and outliers in QoE scores of 𝑇𝐶𝐿𝑖𝑉𝑖and 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒compared to
ALVS. It shows that ALVS is also better at adapting to various environment conditions, while we provide a stable QoE in all different network
conditions. Although the top quartile and the maximum QoE score in
𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒over all experiments are highly close to our approach, note
that 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒noticeably sacrifices the live latency as shown in Table 3.
It is because 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒uses a fixed playback speed and consequently
cannot catch up with the live event time after any video stall.
We investigate live latency changes over time in each session. Fig. 6
depicts representative sessions from each trace group to dive deep
into the performance over 20-min sessions. It confirms that our policy
learned how to adapt the playback speed as a catch-up feature to pull
the player back to the target live edge gradually. Note that there is
no sudden live latency drop (i.e., no undefined slope) at any point
on graphs while recovering from high latency values, as the gradual
decreases are always with the same slope due to one static value of
faster playback (i.e., 1.1) in ALVS. It also proves that ALVS does not skip
to the next fragments for the fast recovery of high latency values. So, it
guarantees rendering all key frames from each fragment. Furthermore,
it also highlights the impact of adaptive playback speed in 𝑇𝐶𝐿𝑖𝑉𝑖,
𝐷𝐴𝑆𝐻.𝑗𝑠and our approach. After video stalls, they can recover the
live latency, whereas 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒and 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒get stuck at higher live
latency values. Figs. 6(c) and 6(f) perfectly exemplify this situation in
which 𝐵𝑎𝑠𝑒𝑙𝑖𝑛𝑒and 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒cannot recover the live latency once they
go away because of any video stall.
5.3.2. Efficiency
We analyze the efficiency being added to live video streaming
systems through our proposed DRL framework in two aspects, which
are the maximization of the user experience during live events, and
elimination of manual efforts in defining rule-based heuristics at the
OTT application provider. First, comparative analysis elaborated in
Section 5.3.1 through the QoE scores and live latency values in Table 3
reflects that our approach is more efficient than the state-of-the-art
solutions. It provides a better QoE (up to 68%) than the others, while

### Página 7

Journal of Network and Computer Applications 205 (2022) 103451
7
I.M. Ozcelik and C. Ersoy
Fig. 5. QoE scores of all the approaches over 15 5-min and 20-min live sessions.
Fig. 6. Live latency changes over time.
catching up with the live event time despite network fluctuations and
video stalls. Second, our approach elaborated in Section 4.2 can adapt
to highly varying network conditions without requiring any handcrafted threshold or heuristic. The same policy achieves low-latency

## 7. Referencias/bibliografía
Referencias detectadas desde la página 8. No se expanden completas aquí para no contaminar la lectura de método; consultar PDF original o raw text si hace falta.
