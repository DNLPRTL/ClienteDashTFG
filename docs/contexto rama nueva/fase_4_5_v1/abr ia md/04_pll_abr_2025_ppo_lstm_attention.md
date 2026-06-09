# Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming
**Archivo PDF:** `075042_1_5.0277381.pdf`
**Identificador:** `04_pll_abr_2025_ppo_lstm_attention`
**Páginas:** 18
**Foco para Fase 4-5 v1:** PPO-based ABR with dual clipping, LSTM/local attention; network dynamics.

> Documento Codex-ready generado para diseño de nuevos modelos/controllers IA ABR. No es una source card corta. Contiene extracción técnica cruda y organizada. El PDF original sigue siendo la fuente de verdad para fórmulas, tablas y figuras si la extracción textual pierde layout.

## 1. Cómo usar este `.md`
- Leer primero las secciones 2-4 para ubicar método, datos y evaluación.
- Usar los extractos crudos por categoría como material base para diseño/contratos/Codex.
- Para ecuaciones, tablas o figuras críticas, comprobar la página indicada en el PDF original.
- No tratar los resultados del paper como promesa directa para DashClientModular4; convertirlos en hipótesis/guardrails y verificar en Phase 6.

## 2. Índice de secciones detectadas
- p.1: J. Acoust. Soc. Am. (June 2021)
- p.1: 09 June 2026 09:26:24
- p.2: 1 School of Software Engineering, Zhengzhou University of Light Industry, Zhengzhou 450003, China
- p.2: ABSTRACT
- p.2: I. INTRODUCTION
- p.2: 09 June 2026 09:26:24
- p.3: 09 June 2026 09:26:24
- p.4: II. BACKGROUND AND RELATED WORK
- p.4: A. Adaptive video streaming and DASH protocol
- p.4: B. Deep reinforcement learning applied to ABR
- p.4: 09 June 2026 09:26:24
- p.5: C. Related work
- p.5: 09 June 2026 09:26:24
- p.6: 09 June 2026 09:26:24
- p.7: III. SYSTEM MODEL
- p.7: A. Description of the problem
- p.7: B. Design of PLL-ABR algorithm
- p.7: 09 June 2026 09:26:24
- p.8: C. Policy update methodology
- p.8: 09 June 2026 09:26:24
- p.9: D. Perception of deep neural network units LSTM-LA
- p.9: 09 June 2026 09:26:24
- p.10: 09 June 2026 09:26:24
- p.11: E. Dynamic adjustment mechanism for nonlinear
- p.11: 09 June 2026 09:26:24
- p.12: IV. EXPERIMENTAL EVALUATION
- p.12: A. Experimental dataset
- p.12: B. Comparative analysis of QoE experimental results
- p.12: 09 June 2026 09:26:24
- p.13: 09 June 2026 09:26:24
- p.14: 09 June 2026 09:26:24
- p.15: C. Generalizability under diverse network conditions
- p.15: 1.2 Mbps to nearly 0.3 Mbps, and the quality gap between before
- p.15: 09 June 2026 09:26:24
- p.16: 09 June 2026 09:26:24
- p.17: V. CONCLUSION
- p.17: 09 June 2026 09:26:24
- p.18: 2022 Conference (Association for Computing Machinery, 2022), pp. 397–413.
- p.18: 09 June 2026 09:26:24

## 3. Índice de páginas con palabras clave
- p.1: energy
- p.2: state, action, QoE, rebuffer, buffer, training
- p.3: state, action, QoE, rebuffer, buffer, throughput, training, baseline, PPO, OOD, generalization
- p.4: QoE, buffer, dataset, training, PPO, latency, OOD, generalization
- p.5: state, action, reward, QoE, buffer, throughput
- p.6: state, action, QoE, buffer, throughput, training, PPO, imitation, latency, generalization
- p.7: state, action, reward, QoE, buffer, training, PPO
- p.8: state, action, reward, QoE, buffer, throughput, training, PPO
- p.9: state, action, reward, throughput, training, PPO, generalization
- p.10: state
- p.11: state, action, training, imitation, OOD
- p.12: state, action, QoE, buffer, throughput, dataset, trace, training, OOD, generalization
- p.13: state, action, QoE, buffer, dataset, training, baseline, PPO, generalization
- p.14: QoE, buffer, training, baseline, PPO, OOD
- p.15: QoE, buffer, throughput, dataset, PPO, OOD, generalization
- p.16: buffer, OOD
- p.17: QoE, buffer, training, PPO, energy, fairness, generalization
- p.18: state, throughput, dataset, trace, imitation

## 4. Extracción técnica cruda por categorías

### 4.x Modelo / arquitectura / algoritmo

**[Modelo / arquitectura / algoritmo | extracto 1 | p.1]**

 View Online  Export Citation RESEARCH ARTICLE | JULY 25 2025 Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming Jianwei Zhang  ; Yang Han ; Zengyu Cai ; Yuan Feng ; Liang Zhu AIP Advances 15, 075042 (2025) https://doi.org/10.1063/5.0277381 Articles You May Be Interested In Semiconductor lasers driven by self-sustained chaotic electronic oscillators and applications to optical chaos cryptography Chaos (July 2012) Optimal design of energy-efficient with traffic uncertainty in wireless body area networks AIP Advances (January 2026) Speech quality estimation with deep lattice networks J. Acoust. Soc. Am. (June 2021) 09 June 2026 09:26:24

**[Modelo / arquitectura / algoritmo | extracto 2 | p.2]**

AIP Advances ARTICLE pubs.aip.org/aip/adv Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming Cite as: AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381 Submitted: 23 April 2025 • Accepted: 7 July 2025 • Published Online: 25 July 2025 Jianwei Zhang,1,a) Yang Han,1 Zengyu Cai,2 Yuan Feng,3 and Liang Zhu2 AFFILIATIONS 1 School of Software Engineering, Zhengzhou University of Light Industry, Zhengzhou 450003, China 2School of Computer Science and Technology, Zhengzhou University of Light Industry, Zhengzhou 450003, China 3School of Electronic Information, Zhengzhou University of Light Industry, Zhengzhou 450003, China a)Author to whom correspondence should be addressed: mailzjw@163.com ABSTRACT Driven by the digital era, video traffic is growing rapidly, and users’ demand for high-quality video experiences is increasing. Adaptive bitrate (ABR) algorithms, as a key technology to optimize the transmission performance of video streams, play an important role in improving the efficiency of communication networks and the quality of experience (QoE). However, existing ABR algorithms rely too much on fixed control rules and simplified environment models, which make it difficult to provide optimal performance under complex and changing physical network environments (e.g., bandwidth fluctuations, delays, and network congestion). To address these challenges, this paper proposes a new ABR algorithm, the deep reinforcement learning enhanced ABR video stream optimization algorithm (PLL-ABR), which adopts proximal policy optimization as a reinforcement learning training framework and combines the dual clipping mechanism and deep neural networks (long short-term memory and local attention mechanism) to improve the training efficiency and

**[Modelo / arquitectura / algoritmo | extracto 3 | p.3]**

AIP Advances ARTICLE pubs.aip.org/aip/adv adjust the bitrate of the video according to the current network conditions and device performance to ensure that the user receives the best viewing experience. In practice, traditional heuristic ABR algorithms mainly include buffer-based5,6 and rate-based algorithms based on network throughput.7 Buffer-based algorithms adjust the bitrate based on monitoring the buffer status to maximize video quality and buffer utilization, but they are not sufficiently responsive to the dynamic network environment, which may lead to QoE degradation or buffer overflow. Rate-based algorithms dynamically adjust the bitrate by predicting the network bandwidth to ensure smooth video transmission, but they ignore the state of the client’s buffer, resulting in unstable performance. The robust MPC algorithm based on control theory integrates the buffer state and the predicted bandwidth to select the best bitrate,8 which improves performance; however, it relies too much on the accuracy of the bandwidth prediction, and once the prediction is inaccurate, performance will be significantly degraded. Recently, researchers have begun to explore more efficient and intelligent ABR algorithms. Among them, the reinforcement learning (RL) technique has become a hot research topic.9 As a machine learning method that interacts with the environment to learn optimal decision policy, reinforcement learning is well suited to be applied in the field of video streaming to improve the performance and stability of ABR algorithms. Past research has focused on traditional reinforcement learning methods, mainly including Q-learning10 and actor-critic.11 For example, Lin et al.12 applied Q-learning to ABR and significantly improved the performance by constructing Q-tables and

**[Modelo / arquitectura / algoritmo | extracto 4 | p.4]**

AIP Advances ARTICLE pubs.aip.org/aip/adv ●An ABR method based on deep reinforcement learning is proposed, which adopts the PPO algorithm with a dual clipping mechanism as the training framework and combines with the LSTM-LA network to capture the long shortterm and local dependencies in the data, which significantly improves the performance of the ABR algorithm. A nonlinear entropy weight dynamic adjustment mechanism is introduced, which further improves the stability and efficiency of strategy optimization by dynamically adjusting the entropy weights and balancing the exploration and utilization, ensuring the high efficiency and flexibility of strategy updating during the training process. ●Experiments have been conducted on a public experimental dataset and compared with existing ABR algorithms. The experimental results show that the method proposed in this paper exhibits significant superiority in terms of overall QoE and the performance of various QoE factors, in addition to its generalization ability in different network environments, which is significantly better than that of other existing algorithms. The rest of the paper is organized as follows. Section II describes the application background of ABR and reviews related work on ABR methods. Section III describes the system model and gives the policy update method. Section IV evaluates the performance of the PLL-ABR method through extensive experimental comparisons. Section V concludes the paper. II. BACKGROUND AND RELATED WORK A. Adaptive video streaming and DASH protocol Adaptive video streaming, as a streaming media delivery technology, can dynamically adjust the bitrate and resolution of the video according to the performance of the user’s device and the current network conditions to ensure that the user rec

**[Modelo / arquitectura / algoritmo | extracto 5 | p.5]**

AIP Advances ARTICLE pubs.aip.org/aip/adv behavioral policy for an intelligent body (agent) during its interaction with the environment. In deep reinforcement learning, an intelligent body optimizes its policy by continuously observing the state of the environment, performing actions, and receiving rewards so that it can make the best decisions when it encounters similar situations in the future. This approach has led to significant breakthroughs in several fields, including network resource management,25 autonomous driving,26 and robot control.27 For example, AlphaGo applied deep reinforcement learning in the game of Go to achieve performance beyond the human level, highlighting the potential and application value of the technology. In addition, deep reinforcement learning also performs well in several network scenarios, such as Software-Defined Networking (SDN), Vehicular Ad hoc NETworks (VANETs), and Wireless Sensor Networks (WSNs),28 demonstrating its great potential in improving network performance and resource utilization efficiency. In DRL, reinforcement learning guides the learning and decision-making processes of intelligence in complex environments by defining decision frameworks and policy-updating algorithms. Deep learning, on the other hand, is used to deal with problems such as function approximation and feature extraction in reinforcement learning to better realize learning and decision-making of intelligence in complex environments. ABR systems dynamically adjust the video bitrate according to network conditions and user requirements to provide the best viewing experience and QoE. Traditional ABR algorithms are usually heuristic rule-based or model-based approaches, which often have difficulty in dealing with complex network environments and video conten

**[Modelo / arquitectura / algoritmo | extracto 6 | p.6]**

AIP Advances ARTICLE pubs.aip.org/aip/adv in variable network environments. Akhtar et al.32 proposed Oboe, an auto-tuning system that pre-calculates the optimal parameters suitable for different network conditions and dynamically adjusts these parameters at runtime based on the current network conditions to automatically optimize existing ABR algorithms. However, when the actual network conditions deviate from the basic assumptions of these ABR algorithms, this approach may exhibit instability. 2. ABR methods based on machine learning To address the shortcomings of traditional heuristics, based on the research of buffer-based and throughput-based adaptive algorithms, researchers have proposed some machine learning-based improvements. Claeys et al.33 proposed an HTTP adaptive streaming client based on adaptive Q-learning, which, unlike traditional heuristics, dynamically learns the optimal behavior corresponding to the current network environment. Chiariotti et al.34 proposed a reinforcement learning-based DASH client logic, which optimally selects the best representation through the Markov Decision Process (MDP) and ensures fast and accurate convergence of the learning through a parallel learning technique. Liu et al.12 combined a k-Nearest Neighbor (KNN) algorithm with a Q-learning algorithm to propose a new KNN-Q learning algorithm for seamless switching bitrate adaptation for video streaming. Mao et al.13 performed bitrate adaptation based on reinforcement learning, using Bayesian optimization to maximize QoE, while training a linear policy to reduce the delay between the video client and the simulated environment. However, the linear approach leads to a degradation of the algorithm’s performance. All of the above-mentioned algorithms are based on Reinforcement Learn

**[Modelo / arquitectura / algoritmo | extracto 7 | p.7]**

AIP Advances ARTICLE pubs.aip.org/aip/adv III. SYSTEM MODEL This section describes the design and implementation of PLL-ABR. The system model fits the actual working mechanism of ABR video streaming in the current internet. We consider a scenario where a video player downloads video files from a server over the internet and plays them back to the user. The video file is divided into consecutive segments, and the server dynamically selects the most suitable segments for transmission based on network conditions and device performance to enhance the viewing experience. During transmission, the available bandwidth fluctuates over time and is affected by network congestion, wireless fading, and other factors. The user’s viewing experience depends not only on the video quality corresponding to the bitrate of the clip but also on playback characteristics such as heavy buffering. The goal of the player is to maximize the utility associated with the viewing experience while flexibly coping with the time-varying and uncertain bandwidth. A. Description of the problem The main goal of ABR is to optimize the user’s quality of the viewing experience to ensure that the user gets the best quality and smoothness when watching video or listening to audio. The QoE function from the literature8 is defined as the reward function in this paper, which is the most commonly used QoE reward function in the field of ABR, which can effectively reflect the user’s perception and expectation of service quality and facilitate experimental comparison with other ABR algorithms. The specific formula is shown in the following equation: QoE = N ∑ n=1 q(Rn) −μ N ∑ n=1 Tn −ρ N ∑ n=1 ∣q(Rn+1) −q(Rn)∣. (1) The QoE factor consists of the following three components: the first one is the video quality: q(Rn) deno

**[Modelo / arquitectura / algoritmo | extracto 8 | p.8]**

AIP Advances ARTICLE pubs.aip.org/aip/adv video streaming bitrate, maximize the user QoE, and effectively cope with complex network environment changes, as we explain the key steps of the algorithm in detail below. Inputs: We designed six parameters as inputs to the neural network, as shown in Eq. (2). By comprehensively analyzing the characteristics of each state’s information, the input parameters are divided into two categories, one for single values and one for continuous values. First, the agent will transmit the information (state si) of each chunk i observed from the environment to the deep neural network, si = (ci, ni, li, ⃗pi, ⃗di, ⃗zi). (2) This includes single-value types: ci denotes the current buffer size, ni denotes the remaining chunks in the video, and li denotes the bitrate of downloading the previous chunk. Considering the singlevalue independent features, we designed to use a fully connected layer to map each input feature to the feature space, which is a simple structure, easy to understand and implement, and usually converges faster during the training process. For continuous value type: ⃗pi denotes the network throughput of the past video chunk download, ⃗di denotes the download time of the past video chunk, and ⃗zi denotes the next video chunk size. Considering that these inputs are characterized by continuity, we adopt LSTM and a local attention mechanism to design the model. This structure can capture long short-term dependencies in the data while capturing local dependencies more effectively, thus improving the model’s ability to understand and utilize the information of the network environment. Policy update: Based on the observation of the input environmental state si, the agent updates the parameters of the policy network using the PPO metho

**[Modelo / arquitectura / algoritmo | extracto 9 | p.9]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 4. Comparison of the effect of PPO and PPO with dual clipping. standard PPO algorithm and the blue partly showing the effect of the improved algorithm. The logic of the PPO algorithm is shown in Algorithm 1, where the policy parameters θ0 and value function parameters ϕ0 are first initialized. k iterations are then performed. In each iteration, the algorithm runs the current policy πk in the given environment, collecting a series of trajectory data Dk. These trajectory data include states, actions, and immediate rewards fed by the environment. Next, based on the collected reward values ˆRt and the current value function Vϕk, the advantage estimate is computed as ˆAt. The algorithm then updates the policy parameters to maximize the PPO objective, which improves the performance of the policy. At the same time, the value function is fitted using mean square error regression to assess the state value more accurately. The whole process is repeated until a predetermined number of iterations is reached. D. Perception of deep neural network units LSTM-LA Traditional reinforcement learning methods have certain disadvantages relative to deep reinforcement learning in terms of feature engineering requirements, generalization capability, training speed, high-dimensional state space processing capability, and continuous action space processing capability.41 These disadvantages limit the performance and application scope of traditional reinforcement learning methods. Especially when dealing with complex and large-scale problems, to cope with this problem, we consider fusing deep neural networks to improve algorithm performance and expect to achieve better results. By observing the inputs of the neural network and comprehensively analyzin

**[Modelo / arquitectura / algoritmo | extracto 10 | p.10]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 5. LSTM-LA neural network unit. dependencies among them, we introduce the LSTM. As a neural network structure specifically designed to process sequence data, the LSTM has memory units and gating mechanisms that can effectively capture and utilize the long short-term dependencies in sequence data. LSTM is a variant of recurrent neural network (RNN) commonly used to process sequence data. Compared to regular RNNs, LSTM is more effective in processing long sequence data because it can capture and utilize long-term dependencies in sequences, avoiding the problems of gradient vanishing and gradient explosion in regular RNNs. The core idea of LSTM networks is to introduce a structure called a “memory cell,” which controls the inputs, outputs, and state updates of the memory cell through a gating mechanism. Inside the memory cell, there is a long-term state called “cell state” Ct, which is used to hold information for a long time. At each time step, the LSTM receives input xt and the hidden state ht−1 from the previous time step, then updates the state of the memory cell based on the current input and the previous hidden state. Specifically, LSTM contains three gate mechanisms: forget gate, input gate, and output gate. The network structure of LSTM is shown in Fig. 6. They are calculated as follows. FIG. 6. LSTM network structure diagram. Forget gate: determines how much of a previous memory state is retained in the current time step. Its calculation formula is shown in the following equation: ft = σ(Wf ⋅[ht−1, xt] + bf ), (7) where σ is the sigmoid function, W f is the weight matrix of the forget gate, and b f is the bias. Input gate: decide how much new information to update to the memory cell. Its calculation formula is shown i

**[Modelo / arquitectura / algoritmo | extracto 11 | p.11]**

AIP Advances ARTICLE pubs.aip.org/aip/adv 2. Capturing local dependencies with local attention There may be complex correlations and dependencies between input data, and these dependencies include not only long and shortterm dependencies but may also manifest as localized dependencies. Although LSTM has a good ability to model long and short-term dependencies, it has some limitations in capturing local correlations. For this reason, this paper introduces the local attention mechanism, which focuses on the information of local regions by assigning different attention weights to different positions of the sequence through a sliding window. The local attention mechanism has the flexibility and variability to adapt to sequence inputs of different lengths and forms, which helps to mine and model local dependencies more effectively. The local attention mechanism effectively reduces computational complexity and enhances local feature extraction by narrowing the attention window and focusing only on local regions of the input sequence. Compared with the O(n2) complexity of global attention, local attention requires only O(w × n) (w is the window size), which significantly improves the computational and storage efficiency in long sequence scenarios, especially suitable for applications with high real-time requirements or memory constraints. In addition, local attention is better at capturing short-time dependencies in the data (e.g., the video stream bitrate decision depends on the characteristics of the first few video blocks) and can flexibly adapt to different needs by dynamically adjusting the window size: a small window captures the fast-changing signals, and a large window captures the long dependencies. The idea is based on the sliding window approach, which calculates th

**[Modelo / arquitectura / algoritmo | extracto 12 | p.12]**

AIP Advances ARTICLE pubs.aip.org/aip/adv dynamically controls the exploration strength of the strategy so as to improve the performance and stability of the video streaming transmission system under complex network conditions. The specific realization process is as follows: Entropy computation: first, the entropy of the current strategy is computed as H. For each strategy, the entropy can be computed by the following equation: H(π) = − n ∑ i=1 π(ai∣si ) log π(ai∣si ), (17) where π(ai∣si) denotes the probability that the intelligent body chooses action ai in state si. The randomness of the current strategy can be measured by this formula. Entropy difference: Calculate the difference ΔH between the current strategy entropy H and the target entropy Htarget. The calculation process is shown in the following equation: ΔH = H −Htarget. (18) The difference reflects the deviation of the entropy of the current strategy from the expected entropy. When ΔH > 0, it indicates that the randomness of the current strategy is higher than expected, at which time the entropy weight can be reduced and the exploration behavior can be decreased; conversely, the entropy weight is increased and exploration is increased. Update of entropy weights: finally, based on this entropy difference, the entropy weights are updated by the learning rate, which is updated as shown in the following equation: λentropy = λentropy −η ⋅tanh (H −Htarget) ⋅γ ⋅T, (19) where γ is the adjustment factor, T is the current number of training rounds, and η is the learning rate. To prevent the entropy weights from becoming too small, λentropy is also boundary-protected, as shown in the following equation: λentropy = max (λentropy, λminimum). (20) Finally, the system updates the strategy parameters in real time based on th

**[Modelo / arquitectura / algoritmo | extracto 13 | p.13]**

AIP Advances ARTICLE pubs.aip.org/aip/adv of RL models by guiding them to be trained in network environments where they do not perform as well as the baseline. 7. NetLLM:47 A model-based approach that efficiently adapts to multiple network tasks by pre-training models to improve performance and generalization. Experimental setup: We randomly select 80% of the samples from the dataset as the training set and the remaining 20% as the test set. In the QoE function, the penalty weight coefficients μ and ρ for re-buffering time and video smoothness are set to 4.3 and 1, respectively. For the Actor network, we pass k = 8 past state information to the network. Among them, the LSTM layer contains 128 neurons, and the fully connected layer uses 128 neurons. The outputs of these layers are then aggregated with the other inputs in the hidden layer, and the softmax function is applied to generate the corresponding action probabilities for the Actor network. The same network structure is used for the Critic network to generate the action values for the Critic network, with the network learning rate configured as 10−4, the optimizer chosen as Adam, the discount factor γ = 0.99, and the target entropy set to 0.1 to ensure that the entropy weights were not less than 0.01. All of these experiments were trained and tested using the deep learning library PyTorch, and our hyperparameters were kept constant throughout the experiments. To ensure the reproducibility of the experimental results, this paper fixes the random seed as 42 during the training process. The training and inference are conducted on a server equipped with NVIDIA GeForce RTX 3090 GPUs and AMD EPYC 7302 Central Processing Unit (CPU), and the software environment consists of Python 3.9 and PyTorch 2.5.1, and the CUDA versio

**[Modelo / arquitectura / algoritmo | extracto 14 | p.14]**

AIP Advances ARTICLE pubs.aip.org/aip/adv TABLE I. Performance comparison of different algorithms. Algorithm Average bitrate (kbps) Average re-buffering time (s) Average bitrate variation (kbps) (between each block) BOLA 1137.309 0.148 254.533 MPC 1127.01 0.101 137.946 Rate-based 947.212 0.122 78.349 Buffer-based 1132.585 0.119 351.978 Pensieve 1074.237 0.093 120.108 Genet 1017.24 0.047 89.556 NetLLM 1005.48 0.041 76.334 PLL-ABR 1107.901 0.088 105.491 QoE function [Eq. (1)] decomposition (for each factor): Bitrate Utility: corresponds to the first part N ∑ n=1 q(Rn) of the QoE function, indicating the currently selected bitrate. Re-buffering Penalty: corresponds to the second part μ N ∑ n=1 Tn of the QoE function, where Tn denotes the re-buffering time and μ is its penalty weight coefficient. Video Smoothness Penalty: corresponds to the third part ρ N ∑ n=1 ∣q(Rn+1) −q(Rn)∣of the QoE function, denoting the amount of bitrate variation between video chunks, and ρ is its penalty weight coefficient. According to the QoE function, we know that QoE is defined as the bitrate utility minus the re-buffering penalty minus the video smoothness penalty. In short, we want the bitrate utility to be as high as possible and the re-buffering and video smoothness penalties to be as low as possible. Figure 9 demonstrates a comparison of the performance of the PLL-ABR with five other representative algorithms in terms of each factor of QoE. As can be seen in Fig. 10, PLL-ABR performs well in the re-buffering penalty and video smoothness penalty modules, with PLL-ABR reducing the re-buffering penalty by 40.59% and 25.58% and reducing the video smoothness penalty by 58.55% and 70.03%, respectively, when compared to the best performers in terms of bitrate utility, BOLA and buffer-based. This

**[Modelo / arquitectura / algoritmo | extracto 15 | p.15]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 10. QoE factors for different dualclip constants. TABLE II. Comparison of PLL-ABR ablation experiments. Method BU RP SP QoE elevate↑(%) PPO + LSTM 1.0786 0.3803 0.0910 52.88 - LA 1.0928 0.3774 0.0975 54.59 - Dual clip 1.0917 0.3826 0.0988 53.38 - NE-weights 1.0960 0.3697 0.1082 54.67 PLL-ABR 1.1079 0.3794 0.1055 55.45 uniformly adopted as the default setting of the double-clipping strategy in the experiments. C. Generalizability under diverse network conditions Considering the diversity of actual network environments, to verify the generalization ability of this paper’s algorithm for different physical network environments (network throughput ranges), the network dataset is further analyzed. Two typical network ranges (poor and good network) are selected for simulation experiments, and the real-time bitrate selections and corresponding buffer sizes of the PLL-ABR algorithm for the two network ranges are given separately. Robust MPC and buffer-based methods are compared, and the results are shown in Fig. 11. Example 1. The first example analyzes an application scenario with poor overall network conditions. It can be observed from Fig. 11(a) that the poorer network environment and objective network fluctuations bring more difficulties to the bitrate selection, especially reflected in robust MPC and buffer-based methods, due to the more inefficient buffer control levels of the two. The network fluctuates greatly when the timestamp is about 50 s and the buffer size drops dramatically, and the bitrate selection drops from 1.2 Mbps to nearly 0.3 Mbps, and the quality gap between before and after the video is too large, which directly affects the result of the QoE function and reduces the user experience. In contrast, by utilizing

**[Modelo / arquitectura / algoritmo | extracto 16 | p.16]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 11. Real-time bitrate selection and buffer occupancy analysis for each algorithm for (a) poor network environments and (b) good network environments. AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381 15, 075042-15 © Author(s) 2025 09 June 2026 09:26:24

### 4.x Estado / inputs / features observables

**[Estado / inputs / features observables | extracto 1 | p.1]**

 View Online  Export Citation RESEARCH ARTICLE | JULY 25 2025 Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming Jianwei Zhang  ; Yang Han ; Zengyu Cai ; Yuan Feng ; Liang Zhu AIP Advances 15, 075042 (2025) https://doi.org/10.1063/5.0277381 Articles You May Be Interested In Semiconductor lasers driven by self-sustained chaotic electronic oscillators and applications to optical chaos cryptography Chaos (July 2012) Optimal design of energy-efficient with traffic uncertainty in wireless body area networks AIP Advances (January 2026) Speech quality estimation with deep lattice networks J. Acoust. Soc. Am. (June 2021) 09 June 2026 09:26:24

**[Estado / inputs / features observables | extracto 2 | p.2]**

AIP Advances ARTICLE pubs.aip.org/aip/adv Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming Cite as: AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381 Submitted: 23 April 2025 • Accepted: 7 July 2025 • Published Online: 25 July 2025 Jianwei Zhang,1,a) Yang Han,1 Zengyu Cai,2 Yuan Feng,3 and Liang Zhu2 AFFILIATIONS 1 School of Software Engineering, Zhengzhou University of Light Industry, Zhengzhou 450003, China 2School of Computer Science and Technology, Zhengzhou University of Light Industry, Zhengzhou 450003, China 3School of Electronic Information, Zhengzhou University of Light Industry, Zhengzhou 450003, China a)Author to whom correspondence should be addressed: mailzjw@163.com ABSTRACT Driven by the digital era, video traffic is growing rapidly, and users’ demand for high-quality video experiences is increasing. Adaptive bitrate (ABR) algorithms, as a key technology to optimize the transmission performance of video streams, play an important role in improving the efficiency of communication networks and the quality of experience (QoE). However, existing ABR algorithms rely too much on fixed control rules and simplified environment models, which make it difficult to provide optimal performance under complex and changing physical network environments (e.g., bandwidth fluctuations, delays, and network congestion). To address these challenges, this paper proposes a new ABR algorithm, the deep reinforcement learning enhanced ABR video stream optimization algorithm (PLL-ABR), which adopts proximal policy optimization as a reinforcement learning training framework and combines the dual clipping mechanism and deep neural networks (long short-term memory and local attention mechanism) to improve the training efficiency and

**[Estado / inputs / features observables | extracto 3 | p.3]**

AIP Advances ARTICLE pubs.aip.org/aip/adv adjust the bitrate of the video according to the current network conditions and device performance to ensure that the user receives the best viewing experience. In practice, traditional heuristic ABR algorithms mainly include buffer-based5,6 and rate-based algorithms based on network throughput.7 Buffer-based algorithms adjust the bitrate based on monitoring the buffer status to maximize video quality and buffer utilization, but they are not sufficiently responsive to the dynamic network environment, which may lead to QoE degradation or buffer overflow. Rate-based algorithms dynamically adjust the bitrate by predicting the network bandwidth to ensure smooth video transmission, but they ignore the state of the client’s buffer, resulting in unstable performance. The robust MPC algorithm based on control theory integrates the buffer state and the predicted bandwidth to select the best bitrate,8 which improves performance; however, it relies too much on the accuracy of the bandwidth prediction, and once the prediction is inaccurate, performance will be significantly degraded. Recently, researchers have begun to explore more efficient and intelligent ABR algorithms. Among them, the reinforcement learning (RL) technique has become a hot research topic.9 As a machine learning method that interacts with the environment to learn optimal decision policy, reinforcement learning is well suited to be applied in the field of video streaming to improve the performance and stability of ABR algorithms. Past research has focused on traditional reinforcement learning methods, mainly including Q-learning10 and actor-critic.11 For example, Lin et al.12 applied Q-learning to ABR and significantly improved the performance by constructing Q-tables and

**[Estado / inputs / features observables | extracto 4 | p.4]**

AIP Advances ARTICLE pubs.aip.org/aip/adv ●An ABR method based on deep reinforcement learning is proposed, which adopts the PPO algorithm with a dual clipping mechanism as the training framework and combines with the LSTM-LA network to capture the long shortterm and local dependencies in the data, which significantly improves the performance of the ABR algorithm. A nonlinear entropy weight dynamic adjustment mechanism is introduced, which further improves the stability and efficiency of strategy optimization by dynamically adjusting the entropy weights and balancing the exploration and utilization, ensuring the high efficiency and flexibility of strategy updating during the training process. ●Experiments have been conducted on a public experimental dataset and compared with existing ABR algorithms. The experimental results show that the method proposed in this paper exhibits significant superiority in terms of overall QoE and the performance of various QoE factors, in addition to its generalization ability in different network environments, which is significantly better than that of other existing algorithms. The rest of the paper is organized as follows. Section II describes the application background of ABR and reviews related work on ABR methods. Section III describes the system model and gives the policy update method. Section IV evaluates the performance of the PLL-ABR method through extensive experimental comparisons. Section V concludes the paper. II. BACKGROUND AND RELATED WORK A. Adaptive video streaming and DASH protocol Adaptive video streaming, as a streaming media delivery technology, can dynamically adjust the bitrate and resolution of the video according to the performance of the user’s device and the current network conditions to ensure that the user rec

**[Estado / inputs / features observables | extracto 5 | p.5]**

AIP Advances ARTICLE pubs.aip.org/aip/adv behavioral policy for an intelligent body (agent) during its interaction with the environment. In deep reinforcement learning, an intelligent body optimizes its policy by continuously observing the state of the environment, performing actions, and receiving rewards so that it can make the best decisions when it encounters similar situations in the future. This approach has led to significant breakthroughs in several fields, including network resource management,25 autonomous driving,26 and robot control.27 For example, AlphaGo applied deep reinforcement learning in the game of Go to achieve performance beyond the human level, highlighting the potential and application value of the technology. In addition, deep reinforcement learning also performs well in several network scenarios, such as Software-Defined Networking (SDN), Vehicular Ad hoc NETworks (VANETs), and Wireless Sensor Networks (WSNs),28 demonstrating its great potential in improving network performance and resource utilization efficiency. In DRL, reinforcement learning guides the learning and decision-making processes of intelligence in complex environments by defining decision frameworks and policy-updating algorithms. Deep learning, on the other hand, is used to deal with problems such as function approximation and feature extraction in reinforcement learning to better realize learning and decision-making of intelligence in complex environments. ABR systems dynamically adjust the video bitrate according to network conditions and user requirements to provide the best viewing experience and QoE. Traditional ABR algorithms are usually heuristic rule-based or model-based approaches, which often have difficulty in dealing with complex network environments and video conten

**[Estado / inputs / features observables | extracto 6 | p.6]**

AIP Advances ARTICLE pubs.aip.org/aip/adv in variable network environments. Akhtar et al.32 proposed Oboe, an auto-tuning system that pre-calculates the optimal parameters suitable for different network conditions and dynamically adjusts these parameters at runtime based on the current network conditions to automatically optimize existing ABR algorithms. However, when the actual network conditions deviate from the basic assumptions of these ABR algorithms, this approach may exhibit instability. 2. ABR methods based on machine learning To address the shortcomings of traditional heuristics, based on the research of buffer-based and throughput-based adaptive algorithms, researchers have proposed some machine learning-based improvements. Claeys et al.33 proposed an HTTP adaptive streaming client based on adaptive Q-learning, which, unlike traditional heuristics, dynamically learns the optimal behavior corresponding to the current network environment. Chiariotti et al.34 proposed a reinforcement learning-based DASH client logic, which optimally selects the best representation through the Markov Decision Process (MDP) and ensures fast and accurate convergence of the learning through a parallel learning technique. Liu et al.12 combined a k-Nearest Neighbor (KNN) algorithm with a Q-learning algorithm to propose a new KNN-Q learning algorithm for seamless switching bitrate adaptation for video streaming. Mao et al.13 performed bitrate adaptation based on reinforcement learning, using Bayesian optimization to maximize QoE, while training a linear policy to reduce the delay between the video client and the simulated environment. However, the linear approach leads to a degradation of the algorithm’s performance. All of the above-mentioned algorithms are based on Reinforcement Learn

**[Estado / inputs / features observables | extracto 7 | p.7]**

AIP Advances ARTICLE pubs.aip.org/aip/adv III. SYSTEM MODEL This section describes the design and implementation of PLL-ABR. The system model fits the actual working mechanism of ABR video streaming in the current internet. We consider a scenario where a video player downloads video files from a server over the internet and plays them back to the user. The video file is divided into consecutive segments, and the server dynamically selects the most suitable segments for transmission based on network conditions and device performance to enhance the viewing experience. During transmission, the available bandwidth fluctuates over time and is affected by network congestion, wireless fading, and other factors. The user’s viewing experience depends not only on the video quality corresponding to the bitrate of the clip but also on playback characteristics such as heavy buffering. The goal of the player is to maximize the utility associated with the viewing experience while flexibly coping with the time-varying and uncertain bandwidth. A. Description of the problem The main goal of ABR is to optimize the user’s quality of the viewing experience to ensure that the user gets the best quality and smoothness when watching video or listening to audio. The QoE function from the literature8 is defined as the reward function in this paper, which is the most commonly used QoE reward function in the field of ABR, which can effectively reflect the user’s perception and expectation of service quality and facilitate experimental comparison with other ABR algorithms. The specific formula is shown in the following equation: QoE = N ∑ n=1 q(Rn) −μ N ∑ n=1 Tn −ρ N ∑ n=1 ∣q(Rn+1) −q(Rn)∣. (1) The QoE factor consists of the following three components: the first one is the video quality: q(Rn) deno

**[Estado / inputs / features observables | extracto 8 | p.8]**

AIP Advances ARTICLE pubs.aip.org/aip/adv video streaming bitrate, maximize the user QoE, and effectively cope with complex network environment changes, as we explain the key steps of the algorithm in detail below. Inputs: We designed six parameters as inputs to the neural network, as shown in Eq. (2). By comprehensively analyzing the characteristics of each state’s information, the input parameters are divided into two categories, one for single values and one for continuous values. First, the agent will transmit the information (state si) of each chunk i observed from the environment to the deep neural network, si = (ci, ni, li, ⃗pi, ⃗di, ⃗zi). (2) This includes single-value types: ci denotes the current buffer size, ni denotes the remaining chunks in the video, and li denotes the bitrate of downloading the previous chunk. Considering the singlevalue independent features, we designed to use a fully connected layer to map each input feature to the feature space, which is a simple structure, easy to understand and implement, and usually converges faster during the training process. For continuous value type: ⃗pi denotes the network throughput of the past video chunk download, ⃗di denotes the download time of the past video chunk, and ⃗zi denotes the next video chunk size. Considering that these inputs are characterized by continuity, we adopt LSTM and a local attention mechanism to design the model. This structure can capture long short-term dependencies in the data while capturing local dependencies more effectively, thus improving the model’s ability to understand and utilize the information of the network environment. Policy update: Based on the observation of the input environmental state si, the agent updates the parameters of the policy network using the PPO metho

**[Estado / inputs / features observables | extracto 9 | p.9]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 4. Comparison of the effect of PPO and PPO with dual clipping. standard PPO algorithm and the blue partly showing the effect of the improved algorithm. The logic of the PPO algorithm is shown in Algorithm 1, where the policy parameters θ0 and value function parameters ϕ0 are first initialized. k iterations are then performed. In each iteration, the algorithm runs the current policy πk in the given environment, collecting a series of trajectory data Dk. These trajectory data include states, actions, and immediate rewards fed by the environment. Next, based on the collected reward values ˆRt and the current value function Vϕk, the advantage estimate is computed as ˆAt. The algorithm then updates the policy parameters to maximize the PPO objective, which improves the performance of the policy. At the same time, the value function is fitted using mean square error regression to assess the state value more accurately. The whole process is repeated until a predetermined number of iterations is reached. D. Perception of deep neural network units LSTM-LA Traditional reinforcement learning methods have certain disadvantages relative to deep reinforcement learning in terms of feature engineering requirements, generalization capability, training speed, high-dimensional state space processing capability, and continuous action space processing capability.41 These disadvantages limit the performance and application scope of traditional reinforcement learning methods. Especially when dealing with complex and large-scale problems, to cope with this problem, we consider fusing deep neural networks to improve algorithm performance and expect to achieve better results. By observing the inputs of the neural network and comprehensively analyzin

**[Estado / inputs / features observables | extracto 10 | p.10]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 5. LSTM-LA neural network unit. dependencies among them, we introduce the LSTM. As a neural network structure specifically designed to process sequence data, the LSTM has memory units and gating mechanisms that can effectively capture and utilize the long short-term dependencies in sequence data. LSTM is a variant of recurrent neural network (RNN) commonly used to process sequence data. Compared to regular RNNs, LSTM is more effective in processing long sequence data because it can capture and utilize long-term dependencies in sequences, avoiding the problems of gradient vanishing and gradient explosion in regular RNNs. The core idea of LSTM networks is to introduce a structure called a “memory cell,” which controls the inputs, outputs, and state updates of the memory cell through a gating mechanism. Inside the memory cell, there is a long-term state called “cell state” Ct, which is used to hold information for a long time. At each time step, the LSTM receives input xt and the hidden state ht−1 from the previous time step, then updates the state of the memory cell based on the current input and the previous hidden state. Specifically, LSTM contains three gate mechanisms: forget gate, input gate, and output gate. The network structure of LSTM is shown in Fig. 6. They are calculated as follows. FIG. 6. LSTM network structure diagram. Forget gate: determines how much of a previous memory state is retained in the current time step. Its calculation formula is shown in the following equation: ft = σ(Wf ⋅[ht−1, xt] + bf ), (7) where σ is the sigmoid function, W f is the weight matrix of the forget gate, and b f is the bias. Input gate: decide how much new information to update to the memory cell. Its calculation formula is shown i

**[Estado / inputs / features observables | extracto 11 | p.11]**

AIP Advances ARTICLE pubs.aip.org/aip/adv 2. Capturing local dependencies with local attention There may be complex correlations and dependencies between input data, and these dependencies include not only long and shortterm dependencies but may also manifest as localized dependencies. Although LSTM has a good ability to model long and short-term dependencies, it has some limitations in capturing local correlations. For this reason, this paper introduces the local attention mechanism, which focuses on the information of local regions by assigning different attention weights to different positions of the sequence through a sliding window. The local attention mechanism has the flexibility and variability to adapt to sequence inputs of different lengths and forms, which helps to mine and model local dependencies more effectively. The local attention mechanism effectively reduces computational complexity and enhances local feature extraction by narrowing the attention window and focusing only on local regions of the input sequence. Compared with the O(n2) complexity of global attention, local attention requires only O(w × n) (w is the window size), which significantly improves the computational and storage efficiency in long sequence scenarios, especially suitable for applications with high real-time requirements or memory constraints. In addition, local attention is better at capturing short-time dependencies in the data (e.g., the video stream bitrate decision depends on the characteristics of the first few video blocks) and can flexibly adapt to different needs by dynamically adjusting the window size: a small window captures the fast-changing signals, and a large window captures the long dependencies. The idea is based on the sliding window approach, which calculates th

**[Estado / inputs / features observables | extracto 12 | p.12]**

AIP Advances ARTICLE pubs.aip.org/aip/adv dynamically controls the exploration strength of the strategy so as to improve the performance and stability of the video streaming transmission system under complex network conditions. The specific realization process is as follows: Entropy computation: first, the entropy of the current strategy is computed as H. For each strategy, the entropy can be computed by the following equation: H(π) = − n ∑ i=1 π(ai∣si ) log π(ai∣si ), (17) where π(ai∣si) denotes the probability that the intelligent body chooses action ai in state si. The randomness of the current strategy can be measured by this formula. Entropy difference: Calculate the difference ΔH between the current strategy entropy H and the target entropy Htarget. The calculation process is shown in the following equation: ΔH = H −Htarget. (18) The difference reflects the deviation of the entropy of the current strategy from the expected entropy. When ΔH > 0, it indicates that the randomness of the current strategy is higher than expected, at which time the entropy weight can be reduced and the exploration behavior can be decreased; conversely, the entropy weight is increased and exploration is increased. Update of entropy weights: finally, based on this entropy difference, the entropy weights are updated by the learning rate, which is updated as shown in the following equation: λentropy = λentropy −η ⋅tanh (H −Htarget) ⋅γ ⋅T, (19) where γ is the adjustment factor, T is the current number of training rounds, and η is the learning rate. To prevent the entropy weights from becoming too small, λentropy is also boundary-protected, as shown in the following equation: λentropy = max (λentropy, λminimum). (20) Finally, the system updates the strategy parameters in real time based on th

**[Estado / inputs / features observables | extracto 13 | p.13]**

AIP Advances ARTICLE pubs.aip.org/aip/adv of RL models by guiding them to be trained in network environments where they do not perform as well as the baseline. 7. NetLLM:47 A model-based approach that efficiently adapts to multiple network tasks by pre-training models to improve performance and generalization. Experimental setup: We randomly select 80% of the samples from the dataset as the training set and the remaining 20% as the test set. In the QoE function, the penalty weight coefficients μ and ρ for re-buffering time and video smoothness are set to 4.3 and 1, respectively. For the Actor network, we pass k = 8 past state information to the network. Among them, the LSTM layer contains 128 neurons, and the fully connected layer uses 128 neurons. The outputs of these layers are then aggregated with the other inputs in the hidden layer, and the softmax function is applied to generate the corresponding action probabilities for the Actor network. The same network structure is used for the Critic network to generate the action values for the Critic network, with the network learning rate configured as 10−4, the optimizer chosen as Adam, the discount factor γ = 0.99, and the target entropy set to 0.1 to ensure that the entropy weights were not less than 0.01. All of these experiments were trained and tested using the deep learning library PyTorch, and our hyperparameters were kept constant throughout the experiments. To ensure the reproducibility of the experimental results, this paper fixes the random seed as 42 during the training process. The training and inference are conducted on a server equipped with NVIDIA GeForce RTX 3090 GPUs and AMD EPYC 7302 Central Processing Unit (CPU), and the software environment consists of Python 3.9 and PyTorch 2.5.1, and the CUDA versio

**[Estado / inputs / features observables | extracto 14 | p.14]**

AIP Advances ARTICLE pubs.aip.org/aip/adv TABLE I. Performance comparison of different algorithms. Algorithm Average bitrate (kbps) Average re-buffering time (s) Average bitrate variation (kbps) (between each block) BOLA 1137.309 0.148 254.533 MPC 1127.01 0.101 137.946 Rate-based 947.212 0.122 78.349 Buffer-based 1132.585 0.119 351.978 Pensieve 1074.237 0.093 120.108 Genet 1017.24 0.047 89.556 NetLLM 1005.48 0.041 76.334 PLL-ABR 1107.901 0.088 105.491 QoE function [Eq. (1)] decomposition (for each factor): Bitrate Utility: corresponds to the first part N ∑ n=1 q(Rn) of the QoE function, indicating the currently selected bitrate. Re-buffering Penalty: corresponds to the second part μ N ∑ n=1 Tn of the QoE function, where Tn denotes the re-buffering time and μ is its penalty weight coefficient. Video Smoothness Penalty: corresponds to the third part ρ N ∑ n=1 ∣q(Rn+1) −q(Rn)∣of the QoE function, denoting the amount of bitrate variation between video chunks, and ρ is its penalty weight coefficient. According to the QoE function, we know that QoE is defined as the bitrate utility minus the re-buffering penalty minus the video smoothness penalty. In short, we want the bitrate utility to be as high as possible and the re-buffering and video smoothness penalties to be as low as possible. Figure 9 demonstrates a comparison of the performance of the PLL-ABR with five other representative algorithms in terms of each factor of QoE. As can be seen in Fig. 10, PLL-ABR performs well in the re-buffering penalty and video smoothness penalty modules, with PLL-ABR reducing the re-buffering penalty by 40.59% and 25.58% and reducing the video smoothness penalty by 58.55% and 70.03%, respectively, when compared to the best performers in terms of bitrate utility, BOLA and buffer-based. This

**[Estado / inputs / features observables | extracto 15 | p.15]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 10. QoE factors for different dualclip constants. TABLE II. Comparison of PLL-ABR ablation experiments. Method BU RP SP QoE elevate↑(%) PPO + LSTM 1.0786 0.3803 0.0910 52.88 - LA 1.0928 0.3774 0.0975 54.59 - Dual clip 1.0917 0.3826 0.0988 53.38 - NE-weights 1.0960 0.3697 0.1082 54.67 PLL-ABR 1.1079 0.3794 0.1055 55.45 uniformly adopted as the default setting of the double-clipping strategy in the experiments. C. Generalizability under diverse network conditions Considering the diversity of actual network environments, to verify the generalization ability of this paper’s algorithm for different physical network environments (network throughput ranges), the network dataset is further analyzed. Two typical network ranges (poor and good network) are selected for simulation experiments, and the real-time bitrate selections and corresponding buffer sizes of the PLL-ABR algorithm for the two network ranges are given separately. Robust MPC and buffer-based methods are compared, and the results are shown in Fig. 11. Example 1. The first example analyzes an application scenario with poor overall network conditions. It can be observed from Fig. 11(a) that the poorer network environment and objective network fluctuations bring more difficulties to the bitrate selection, especially reflected in robust MPC and buffer-based methods, due to the more inefficient buffer control levels of the two. The network fluctuates greatly when the timestamp is about 50 s and the buffer size drops dramatically, and the bitrate selection drops from 1.2 Mbps to nearly 0.3 Mbps, and the quality gap between before and after the video is too large, which directly affects the result of the QoE function and reduces the user experience. In contrast, by utilizing

**[Estado / inputs / features observables | extracto 16 | p.16]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 11. Real-time bitrate selection and buffer occupancy analysis for each algorithm for (a) poor network environments and (b) good network environments. AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381 15, 075042-15 © Author(s) 2025 09 June 2026 09:26:24

### 4.x Acción / decisión ABR

**[Acción / decisión ABR | extracto 1 | p.1]**

 View Online  Export Citation RESEARCH ARTICLE | JULY 25 2025 Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming Jianwei Zhang  ; Yang Han ; Zengyu Cai ; Yuan Feng ; Liang Zhu AIP Advances 15, 075042 (2025) https://doi.org/10.1063/5.0277381 Articles You May Be Interested In Semiconductor lasers driven by self-sustained chaotic electronic oscillators and applications to optical chaos cryptography Chaos (July 2012) Optimal design of energy-efficient with traffic uncertainty in wireless body area networks AIP Advances (January 2026) Speech quality estimation with deep lattice networks J. Acoust. Soc. Am. (June 2021) 09 June 2026 09:26:24

**[Acción / decisión ABR | extracto 2 | p.2]**

AIP Advances ARTICLE pubs.aip.org/aip/adv Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming Cite as: AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381 Submitted: 23 April 2025 • Accepted: 7 July 2025 • Published Online: 25 July 2025 Jianwei Zhang,1,a) Yang Han,1 Zengyu Cai,2 Yuan Feng,3 and Liang Zhu2 AFFILIATIONS 1 School of Software Engineering, Zhengzhou University of Light Industry, Zhengzhou 450003, China 2School of Computer Science and Technology, Zhengzhou University of Light Industry, Zhengzhou 450003, China 3School of Electronic Information, Zhengzhou University of Light Industry, Zhengzhou 450003, China a)Author to whom correspondence should be addressed: mailzjw@163.com ABSTRACT Driven by the digital era, video traffic is growing rapidly, and users’ demand for high-quality video experiences is increasing. Adaptive bitrate (ABR) algorithms, as a key technology to optimize the transmission performance of video streams, play an important role in improving the efficiency of communication networks and the quality of experience (QoE). However, existing ABR algorithms rely too much on fixed control rules and simplified environment models, which make it difficult to provide optimal performance under complex and changing physical network environments (e.g., bandwidth fluctuations, delays, and network congestion). To address these challenges, this paper proposes a new ABR algorithm, the deep reinforcement learning enhanced ABR video stream optimization algorithm (PLL-ABR), which adopts proximal policy optimization as a reinforcement learning training framework and combines the dual clipping mechanism and deep neural networks (long short-term memory and local attention mechanism) to improve the training efficiency and

**[Acción / decisión ABR | extracto 3 | p.3]**

AIP Advances ARTICLE pubs.aip.org/aip/adv adjust the bitrate of the video according to the current network conditions and device performance to ensure that the user receives the best viewing experience. In practice, traditional heuristic ABR algorithms mainly include buffer-based5,6 and rate-based algorithms based on network throughput.7 Buffer-based algorithms adjust the bitrate based on monitoring the buffer status to maximize video quality and buffer utilization, but they are not sufficiently responsive to the dynamic network environment, which may lead to QoE degradation or buffer overflow. Rate-based algorithms dynamically adjust the bitrate by predicting the network bandwidth to ensure smooth video transmission, but they ignore the state of the client’s buffer, resulting in unstable performance. The robust MPC algorithm based on control theory integrates the buffer state and the predicted bandwidth to select the best bitrate,8 which improves performance; however, it relies too much on the accuracy of the bandwidth prediction, and once the prediction is inaccurate, performance will be significantly degraded. Recently, researchers have begun to explore more efficient and intelligent ABR algorithms. Among them, the reinforcement learning (RL) technique has become a hot research topic.9 As a machine learning method that interacts with the environment to learn optimal decision policy, reinforcement learning is well suited to be applied in the field of video streaming to improve the performance and stability of ABR algorithms. Past research has focused on traditional reinforcement learning methods, mainly including Q-learning10 and actor-critic.11 For example, Lin et al.12 applied Q-learning to ABR and significantly improved the performance by constructing Q-tables and

**[Acción / decisión ABR | extracto 4 | p.4]**

AIP Advances ARTICLE pubs.aip.org/aip/adv ●An ABR method based on deep reinforcement learning is proposed, which adopts the PPO algorithm with a dual clipping mechanism as the training framework and combines with the LSTM-LA network to capture the long shortterm and local dependencies in the data, which significantly improves the performance of the ABR algorithm. A nonlinear entropy weight dynamic adjustment mechanism is introduced, which further improves the stability and efficiency of strategy optimization by dynamically adjusting the entropy weights and balancing the exploration and utilization, ensuring the high efficiency and flexibility of strategy updating during the training process. ●Experiments have been conducted on a public experimental dataset and compared with existing ABR algorithms. The experimental results show that the method proposed in this paper exhibits significant superiority in terms of overall QoE and the performance of various QoE factors, in addition to its generalization ability in different network environments, which is significantly better than that of other existing algorithms. The rest of the paper is organized as follows. Section II describes the application background of ABR and reviews related work on ABR methods. Section III describes the system model and gives the policy update method. Section IV evaluates the performance of the PLL-ABR method through extensive experimental comparisons. Section V concludes the paper. II. BACKGROUND AND RELATED WORK A. Adaptive video streaming and DASH protocol Adaptive video streaming, as a streaming media delivery technology, can dynamically adjust the bitrate and resolution of the video according to the performance of the user’s device and the current network conditions to ensure that the user rec

**[Acción / decisión ABR | extracto 5 | p.5]**

AIP Advances ARTICLE pubs.aip.org/aip/adv behavioral policy for an intelligent body (agent) during its interaction with the environment. In deep reinforcement learning, an intelligent body optimizes its policy by continuously observing the state of the environment, performing actions, and receiving rewards so that it can make the best decisions when it encounters similar situations in the future. This approach has led to significant breakthroughs in several fields, including network resource management,25 autonomous driving,26 and robot control.27 For example, AlphaGo applied deep reinforcement learning in the game of Go to achieve performance beyond the human level, highlighting the potential and application value of the technology. In addition, deep reinforcement learning also performs well in several network scenarios, such as Software-Defined Networking (SDN), Vehicular Ad hoc NETworks (VANETs), and Wireless Sensor Networks (WSNs),28 demonstrating its great potential in improving network performance and resource utilization efficiency. In DRL, reinforcement learning guides the learning and decision-making processes of intelligence in complex environments by defining decision frameworks and policy-updating algorithms. Deep learning, on the other hand, is used to deal with problems such as function approximation and feature extraction in reinforcement learning to better realize learning and decision-making of intelligence in complex environments. ABR systems dynamically adjust the video bitrate according to network conditions and user requirements to provide the best viewing experience and QoE. Traditional ABR algorithms are usually heuristic rule-based or model-based approaches, which often have difficulty in dealing with complex network environments and video conten

**[Acción / decisión ABR | extracto 6 | p.6]**

AIP Advances ARTICLE pubs.aip.org/aip/adv in variable network environments. Akhtar et al.32 proposed Oboe, an auto-tuning system that pre-calculates the optimal parameters suitable for different network conditions and dynamically adjusts these parameters at runtime based on the current network conditions to automatically optimize existing ABR algorithms. However, when the actual network conditions deviate from the basic assumptions of these ABR algorithms, this approach may exhibit instability. 2. ABR methods based on machine learning To address the shortcomings of traditional heuristics, based on the research of buffer-based and throughput-based adaptive algorithms, researchers have proposed some machine learning-based improvements. Claeys et al.33 proposed an HTTP adaptive streaming client based on adaptive Q-learning, which, unlike traditional heuristics, dynamically learns the optimal behavior corresponding to the current network environment. Chiariotti et al.34 proposed a reinforcement learning-based DASH client logic, which optimally selects the best representation through the Markov Decision Process (MDP) and ensures fast and accurate convergence of the learning through a parallel learning technique. Liu et al.12 combined a k-Nearest Neighbor (KNN) algorithm with a Q-learning algorithm to propose a new KNN-Q learning algorithm for seamless switching bitrate adaptation for video streaming. Mao et al.13 performed bitrate adaptation based on reinforcement learning, using Bayesian optimization to maximize QoE, while training a linear policy to reduce the delay between the video client and the simulated environment. However, the linear approach leads to a degradation of the algorithm’s performance. All of the above-mentioned algorithms are based on Reinforcement Learn

**[Acción / decisión ABR | extracto 7 | p.7]**

AIP Advances ARTICLE pubs.aip.org/aip/adv III. SYSTEM MODEL This section describes the design and implementation of PLL-ABR. The system model fits the actual working mechanism of ABR video streaming in the current internet. We consider a scenario where a video player downloads video files from a server over the internet and plays them back to the user. The video file is divided into consecutive segments, and the server dynamically selects the most suitable segments for transmission based on network conditions and device performance to enhance the viewing experience. During transmission, the available bandwidth fluctuates over time and is affected by network congestion, wireless fading, and other factors. The user’s viewing experience depends not only on the video quality corresponding to the bitrate of the clip but also on playback characteristics such as heavy buffering. The goal of the player is to maximize the utility associated with the viewing experience while flexibly coping with the time-varying and uncertain bandwidth. A. Description of the problem The main goal of ABR is to optimize the user’s quality of the viewing experience to ensure that the user gets the best quality and smoothness when watching video or listening to audio. The QoE function from the literature8 is defined as the reward function in this paper, which is the most commonly used QoE reward function in the field of ABR, which can effectively reflect the user’s perception and expectation of service quality and facilitate experimental comparison with other ABR algorithms. The specific formula is shown in the following equation: QoE = N ∑ n=1 q(Rn) −μ N ∑ n=1 Tn −ρ N ∑ n=1 ∣q(Rn+1) −q(Rn)∣. (1) The QoE factor consists of the following three components: the first one is the video quality: q(Rn) deno

**[Acción / decisión ABR | extracto 8 | p.8]**

AIP Advances ARTICLE pubs.aip.org/aip/adv video streaming bitrate, maximize the user QoE, and effectively cope with complex network environment changes, as we explain the key steps of the algorithm in detail below. Inputs: We designed six parameters as inputs to the neural network, as shown in Eq. (2). By comprehensively analyzing the characteristics of each state’s information, the input parameters are divided into two categories, one for single values and one for continuous values. First, the agent will transmit the information (state si) of each chunk i observed from the environment to the deep neural network, si = (ci, ni, li, ⃗pi, ⃗di, ⃗zi). (2) This includes single-value types: ci denotes the current buffer size, ni denotes the remaining chunks in the video, and li denotes the bitrate of downloading the previous chunk. Considering the singlevalue independent features, we designed to use a fully connected layer to map each input feature to the feature space, which is a simple structure, easy to understand and implement, and usually converges faster during the training process. For continuous value type: ⃗pi denotes the network throughput of the past video chunk download, ⃗di denotes the download time of the past video chunk, and ⃗zi denotes the next video chunk size. Considering that these inputs are characterized by continuity, we adopt LSTM and a local attention mechanism to design the model. This structure can capture long short-term dependencies in the data while capturing local dependencies more effectively, thus improving the model’s ability to understand and utilize the information of the network environment. Policy update: Based on the observation of the input environmental state si, the agent updates the parameters of the policy network using the PPO metho

**[Acción / decisión ABR | extracto 9 | p.9]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 4. Comparison of the effect of PPO and PPO with dual clipping. standard PPO algorithm and the blue partly showing the effect of the improved algorithm. The logic of the PPO algorithm is shown in Algorithm 1, where the policy parameters θ0 and value function parameters ϕ0 are first initialized. k iterations are then performed. In each iteration, the algorithm runs the current policy πk in the given environment, collecting a series of trajectory data Dk. These trajectory data include states, actions, and immediate rewards fed by the environment. Next, based on the collected reward values ˆRt and the current value function Vϕk, the advantage estimate is computed as ˆAt. The algorithm then updates the policy parameters to maximize the PPO objective, which improves the performance of the policy. At the same time, the value function is fitted using mean square error regression to assess the state value more accurately. The whole process is repeated until a predetermined number of iterations is reached. D. Perception of deep neural network units LSTM-LA Traditional reinforcement learning methods have certain disadvantages relative to deep reinforcement learning in terms of feature engineering requirements, generalization capability, training speed, high-dimensional state space processing capability, and continuous action space processing capability.41 These disadvantages limit the performance and application scope of traditional reinforcement learning methods. Especially when dealing with complex and large-scale problems, to cope with this problem, we consider fusing deep neural networks to improve algorithm performance and expect to achieve better results. By observing the inputs of the neural network and comprehensively analyzin

**[Acción / decisión ABR | extracto 10 | p.11]**

AIP Advances ARTICLE pubs.aip.org/aip/adv 2. Capturing local dependencies with local attention There may be complex correlations and dependencies between input data, and these dependencies include not only long and shortterm dependencies but may also manifest as localized dependencies. Although LSTM has a good ability to model long and short-term dependencies, it has some limitations in capturing local correlations. For this reason, this paper introduces the local attention mechanism, which focuses on the information of local regions by assigning different attention weights to different positions of the sequence through a sliding window. The local attention mechanism has the flexibility and variability to adapt to sequence inputs of different lengths and forms, which helps to mine and model local dependencies more effectively. The local attention mechanism effectively reduces computational complexity and enhances local feature extraction by narrowing the attention window and focusing only on local regions of the input sequence. Compared with the O(n2) complexity of global attention, local attention requires only O(w × n) (w is the window size), which significantly improves the computational and storage efficiency in long sequence scenarios, especially suitable for applications with high real-time requirements or memory constraints. In addition, local attention is better at capturing short-time dependencies in the data (e.g., the video stream bitrate decision depends on the characteristics of the first few video blocks) and can flexibly adapt to different needs by dynamically adjusting the window size: a small window captures the fast-changing signals, and a large window captures the long dependencies. The idea is based on the sliding window approach, which calculates th

**[Acción / decisión ABR | extracto 11 | p.12]**

AIP Advances ARTICLE pubs.aip.org/aip/adv dynamically controls the exploration strength of the strategy so as to improve the performance and stability of the video streaming transmission system under complex network conditions. The specific realization process is as follows: Entropy computation: first, the entropy of the current strategy is computed as H. For each strategy, the entropy can be computed by the following equation: H(π) = − n ∑ i=1 π(ai∣si ) log π(ai∣si ), (17) where π(ai∣si) denotes the probability that the intelligent body chooses action ai in state si. The randomness of the current strategy can be measured by this formula. Entropy difference: Calculate the difference ΔH between the current strategy entropy H and the target entropy Htarget. The calculation process is shown in the following equation: ΔH = H −Htarget. (18) The difference reflects the deviation of the entropy of the current strategy from the expected entropy. When ΔH > 0, it indicates that the randomness of the current strategy is higher than expected, at which time the entropy weight can be reduced and the exploration behavior can be decreased; conversely, the entropy weight is increased and exploration is increased. Update of entropy weights: finally, based on this entropy difference, the entropy weights are updated by the learning rate, which is updated as shown in the following equation: λentropy = λentropy −η ⋅tanh (H −Htarget) ⋅γ ⋅T, (19) where γ is the adjustment factor, T is the current number of training rounds, and η is the learning rate. To prevent the entropy weights from becoming too small, λentropy is also boundary-protected, as shown in the following equation: λentropy = max (λentropy, λminimum). (20) Finally, the system updates the strategy parameters in real time based on th

**[Acción / decisión ABR | extracto 12 | p.13]**

AIP Advances ARTICLE pubs.aip.org/aip/adv of RL models by guiding them to be trained in network environments where they do not perform as well as the baseline. 7. NetLLM:47 A model-based approach that efficiently adapts to multiple network tasks by pre-training models to improve performance and generalization. Experimental setup: We randomly select 80% of the samples from the dataset as the training set and the remaining 20% as the test set. In the QoE function, the penalty weight coefficients μ and ρ for re-buffering time and video smoothness are set to 4.3 and 1, respectively. For the Actor network, we pass k = 8 past state information to the network. Among them, the LSTM layer contains 128 neurons, and the fully connected layer uses 128 neurons. The outputs of these layers are then aggregated with the other inputs in the hidden layer, and the softmax function is applied to generate the corresponding action probabilities for the Actor network. The same network structure is used for the Critic network to generate the action values for the Critic network, with the network learning rate configured as 10−4, the optimizer chosen as Adam, the discount factor γ = 0.99, and the target entropy set to 0.1 to ensure that the entropy weights were not less than 0.01. All of these experiments were trained and tested using the deep learning library PyTorch, and our hyperparameters were kept constant throughout the experiments. To ensure the reproducibility of the experimental results, this paper fixes the random seed as 42 during the training process. The training and inference are conducted on a server equipped with NVIDIA GeForce RTX 3090 GPUs and AMD EPYC 7302 Central Processing Unit (CPU), and the software environment consists of Python 3.9 and PyTorch 2.5.1, and the CUDA versio

**[Acción / decisión ABR | extracto 13 | p.14]**

AIP Advances ARTICLE pubs.aip.org/aip/adv TABLE I. Performance comparison of different algorithms. Algorithm Average bitrate (kbps) Average re-buffering time (s) Average bitrate variation (kbps) (between each block) BOLA 1137.309 0.148 254.533 MPC 1127.01 0.101 137.946 Rate-based 947.212 0.122 78.349 Buffer-based 1132.585 0.119 351.978 Pensieve 1074.237 0.093 120.108 Genet 1017.24 0.047 89.556 NetLLM 1005.48 0.041 76.334 PLL-ABR 1107.901 0.088 105.491 QoE function [Eq. (1)] decomposition (for each factor): Bitrate Utility: corresponds to the first part N ∑ n=1 q(Rn) of the QoE function, indicating the currently selected bitrate. Re-buffering Penalty: corresponds to the second part μ N ∑ n=1 Tn of the QoE function, where Tn denotes the re-buffering time and μ is its penalty weight coefficient. Video Smoothness Penalty: corresponds to the third part ρ N ∑ n=1 ∣q(Rn+1) −q(Rn)∣of the QoE function, denoting the amount of bitrate variation between video chunks, and ρ is its penalty weight coefficient. According to the QoE function, we know that QoE is defined as the bitrate utility minus the re-buffering penalty minus the video smoothness penalty. In short, we want the bitrate utility to be as high as possible and the re-buffering and video smoothness penalties to be as low as possible. Figure 9 demonstrates a comparison of the performance of the PLL-ABR with five other representative algorithms in terms of each factor of QoE. As can be seen in Fig. 10, PLL-ABR performs well in the re-buffering penalty and video smoothness penalty modules, with PLL-ABR reducing the re-buffering penalty by 40.59% and 25.58% and reducing the video smoothness penalty by 58.55% and 70.03%, respectively, when compared to the best performers in terms of bitrate utility, BOLA and buffer-based. This

**[Acción / decisión ABR | extracto 14 | p.15]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 10. QoE factors for different dualclip constants. TABLE II. Comparison of PLL-ABR ablation experiments. Method BU RP SP QoE elevate↑(%) PPO + LSTM 1.0786 0.3803 0.0910 52.88 - LA 1.0928 0.3774 0.0975 54.59 - Dual clip 1.0917 0.3826 0.0988 53.38 - NE-weights 1.0960 0.3697 0.1082 54.67 PLL-ABR 1.1079 0.3794 0.1055 55.45 uniformly adopted as the default setting of the double-clipping strategy in the experiments. C. Generalizability under diverse network conditions Considering the diversity of actual network environments, to verify the generalization ability of this paper’s algorithm for different physical network environments (network throughput ranges), the network dataset is further analyzed. Two typical network ranges (poor and good network) are selected for simulation experiments, and the real-time bitrate selections and corresponding buffer sizes of the PLL-ABR algorithm for the two network ranges are given separately. Robust MPC and buffer-based methods are compared, and the results are shown in Fig. 11. Example 1. The first example analyzes an application scenario with poor overall network conditions. It can be observed from Fig. 11(a) that the poorer network environment and objective network fluctuations bring more difficulties to the bitrate selection, especially reflected in robust MPC and buffer-based methods, due to the more inefficient buffer control levels of the two. The network fluctuates greatly when the timestamp is about 50 s and the buffer size drops dramatically, and the bitrate selection drops from 1.2 Mbps to nearly 0.3 Mbps, and the quality gap between before and after the video is too large, which directly affects the result of the QoE function and reduces the user experience. In contrast, by utilizing

**[Acción / decisión ABR | extracto 15 | p.16]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 11. Real-time bitrate selection and buffer occupancy analysis for each algorithm for (a) poor network environments and (b) good network environments. AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381 15, 075042-15 © Author(s) 2025 09 June 2026 09:26:24

### 4.x Reward / QoE / función objetivo

**[Reward / QoE / función objetivo | extracto 1 | p.1]**

 View Online  Export Citation RESEARCH ARTICLE | JULY 25 2025 Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming Jianwei Zhang  ; Yang Han ; Zengyu Cai ; Yuan Feng ; Liang Zhu AIP Advances 15, 075042 (2025) https://doi.org/10.1063/5.0277381 Articles You May Be Interested In Semiconductor lasers driven by self-sustained chaotic electronic oscillators and applications to optical chaos cryptography Chaos (July 2012) Optimal design of energy-efficient with traffic uncertainty in wireless body area networks AIP Advances (January 2026) Speech quality estimation with deep lattice networks J. Acoust. Soc. Am. (June 2021) 09 June 2026 09:26:24

**[Reward / QoE / función objetivo | extracto 2 | p.2]**

AIP Advances ARTICLE pubs.aip.org/aip/adv Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming Cite as: AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381 Submitted: 23 April 2025 • Accepted: 7 July 2025 • Published Online: 25 July 2025 Jianwei Zhang,1,a) Yang Han,1 Zengyu Cai,2 Yuan Feng,3 and Liang Zhu2 AFFILIATIONS 1 School of Software Engineering, Zhengzhou University of Light Industry, Zhengzhou 450003, China 2School of Computer Science and Technology, Zhengzhou University of Light Industry, Zhengzhou 450003, China 3School of Electronic Information, Zhengzhou University of Light Industry, Zhengzhou 450003, China a)Author to whom correspondence should be addressed: mailzjw@163.com ABSTRACT Driven by the digital era, video traffic is growing rapidly, and users’ demand for high-quality video experiences is increasing. Adaptive bitrate (ABR) algorithms, as a key technology to optimize the transmission performance of video streams, play an important role in improving the efficiency of communication networks and the quality of experience (QoE). However, existing ABR algorithms rely too much on fixed control rules and simplified environment models, which make it difficult to provide optimal performance under complex and changing physical network environments (e.g., bandwidth fluctuations, delays, and network congestion). To address these challenges, this paper proposes a new ABR algorithm, the deep reinforcement learning enhanced ABR video stream optimization algorithm (PLL-ABR), which adopts proximal policy optimization as a reinforcement learning training framework and combines the dual clipping mechanism and deep neural networks (long short-term memory and local attention mechanism) to improve the training efficiency and

**[Reward / QoE / función objetivo | extracto 3 | p.3]**

AIP Advances ARTICLE pubs.aip.org/aip/adv adjust the bitrate of the video according to the current network conditions and device performance to ensure that the user receives the best viewing experience. In practice, traditional heuristic ABR algorithms mainly include buffer-based5,6 and rate-based algorithms based on network throughput.7 Buffer-based algorithms adjust the bitrate based on monitoring the buffer status to maximize video quality and buffer utilization, but they are not sufficiently responsive to the dynamic network environment, which may lead to QoE degradation or buffer overflow. Rate-based algorithms dynamically adjust the bitrate by predicting the network bandwidth to ensure smooth video transmission, but they ignore the state of the client’s buffer, resulting in unstable performance. The robust MPC algorithm based on control theory integrates the buffer state and the predicted bandwidth to select the best bitrate,8 which improves performance; however, it relies too much on the accuracy of the bandwidth prediction, and once the prediction is inaccurate, performance will be significantly degraded. Recently, researchers have begun to explore more efficient and intelligent ABR algorithms. Among them, the reinforcement learning (RL) technique has become a hot research topic.9 As a machine learning method that interacts with the environment to learn optimal decision policy, reinforcement learning is well suited to be applied in the field of video streaming to improve the performance and stability of ABR algorithms. Past research has focused on traditional reinforcement learning methods, mainly including Q-learning10 and actor-critic.11 For example, Lin et al.12 applied Q-learning to ABR and significantly improved the performance by constructing Q-tables and

**[Reward / QoE / función objetivo | extracto 4 | p.4]**

AIP Advances ARTICLE pubs.aip.org/aip/adv ●An ABR method based on deep reinforcement learning is proposed, which adopts the PPO algorithm with a dual clipping mechanism as the training framework and combines with the LSTM-LA network to capture the long shortterm and local dependencies in the data, which significantly improves the performance of the ABR algorithm. A nonlinear entropy weight dynamic adjustment mechanism is introduced, which further improves the stability and efficiency of strategy optimization by dynamically adjusting the entropy weights and balancing the exploration and utilization, ensuring the high efficiency and flexibility of strategy updating during the training process. ●Experiments have been conducted on a public experimental dataset and compared with existing ABR algorithms. The experimental results show that the method proposed in this paper exhibits significant superiority in terms of overall QoE and the performance of various QoE factors, in addition to its generalization ability in different network environments, which is significantly better than that of other existing algorithms. The rest of the paper is organized as follows. Section II describes the application background of ABR and reviews related work on ABR methods. Section III describes the system model and gives the policy update method. Section IV evaluates the performance of the PLL-ABR method through extensive experimental comparisons. Section V concludes the paper. II. BACKGROUND AND RELATED WORK A. Adaptive video streaming and DASH protocol Adaptive video streaming, as a streaming media delivery technology, can dynamically adjust the bitrate and resolution of the video according to the performance of the user’s device and the current network conditions to ensure that the user rec

**[Reward / QoE / función objetivo | extracto 5 | p.5]**

AIP Advances ARTICLE pubs.aip.org/aip/adv behavioral policy for an intelligent body (agent) during its interaction with the environment. In deep reinforcement learning, an intelligent body optimizes its policy by continuously observing the state of the environment, performing actions, and receiving rewards so that it can make the best decisions when it encounters similar situations in the future. This approach has led to significant breakthroughs in several fields, including network resource management,25 autonomous driving,26 and robot control.27 For example, AlphaGo applied deep reinforcement learning in the game of Go to achieve performance beyond the human level, highlighting the potential and application value of the technology. In addition, deep reinforcement learning also performs well in several network scenarios, such as Software-Defined Networking (SDN), Vehicular Ad hoc NETworks (VANETs), and Wireless Sensor Networks (WSNs),28 demonstrating its great potential in improving network performance and resource utilization efficiency. In DRL, reinforcement learning guides the learning and decision-making processes of intelligence in complex environments by defining decision frameworks and policy-updating algorithms. Deep learning, on the other hand, is used to deal with problems such as function approximation and feature extraction in reinforcement learning to better realize learning and decision-making of intelligence in complex environments. ABR systems dynamically adjust the video bitrate according to network conditions and user requirements to provide the best viewing experience and QoE. Traditional ABR algorithms are usually heuristic rule-based or model-based approaches, which often have difficulty in dealing with complex network environments and video conten

**[Reward / QoE / función objetivo | extracto 6 | p.6]**

AIP Advances ARTICLE pubs.aip.org/aip/adv in variable network environments. Akhtar et al.32 proposed Oboe, an auto-tuning system that pre-calculates the optimal parameters suitable for different network conditions and dynamically adjusts these parameters at runtime based on the current network conditions to automatically optimize existing ABR algorithms. However, when the actual network conditions deviate from the basic assumptions of these ABR algorithms, this approach may exhibit instability. 2. ABR methods based on machine learning To address the shortcomings of traditional heuristics, based on the research of buffer-based and throughput-based adaptive algorithms, researchers have proposed some machine learning-based improvements. Claeys et al.33 proposed an HTTP adaptive streaming client based on adaptive Q-learning, which, unlike traditional heuristics, dynamically learns the optimal behavior corresponding to the current network environment. Chiariotti et al.34 proposed a reinforcement learning-based DASH client logic, which optimally selects the best representation through the Markov Decision Process (MDP) and ensures fast and accurate convergence of the learning through a parallel learning technique. Liu et al.12 combined a k-Nearest Neighbor (KNN) algorithm with a Q-learning algorithm to propose a new KNN-Q learning algorithm for seamless switching bitrate adaptation for video streaming. Mao et al.13 performed bitrate adaptation based on reinforcement learning, using Bayesian optimization to maximize QoE, while training a linear policy to reduce the delay between the video client and the simulated environment. However, the linear approach leads to a degradation of the algorithm’s performance. All of the above-mentioned algorithms are based on Reinforcement Learn

**[Reward / QoE / función objetivo | extracto 7 | p.7]**

AIP Advances ARTICLE pubs.aip.org/aip/adv III. SYSTEM MODEL This section describes the design and implementation of PLL-ABR. The system model fits the actual working mechanism of ABR video streaming in the current internet. We consider a scenario where a video player downloads video files from a server over the internet and plays them back to the user. The video file is divided into consecutive segments, and the server dynamically selects the most suitable segments for transmission based on network conditions and device performance to enhance the viewing experience. During transmission, the available bandwidth fluctuates over time and is affected by network congestion, wireless fading, and other factors. The user’s viewing experience depends not only on the video quality corresponding to the bitrate of the clip but also on playback characteristics such as heavy buffering. The goal of the player is to maximize the utility associated with the viewing experience while flexibly coping with the time-varying and uncertain bandwidth. A. Description of the problem The main goal of ABR is to optimize the user’s quality of the viewing experience to ensure that the user gets the best quality and smoothness when watching video or listening to audio. The QoE function from the literature8 is defined as the reward function in this paper, which is the most commonly used QoE reward function in the field of ABR, which can effectively reflect the user’s perception and expectation of service quality and facilitate experimental comparison with other ABR algorithms. The specific formula is shown in the following equation: QoE = N ∑ n=1 q(Rn) −μ N ∑ n=1 Tn −ρ N ∑ n=1 ∣q(Rn+1) −q(Rn)∣. (1) The QoE factor consists of the following three components: the first one is the video quality: q(Rn) deno

**[Reward / QoE / función objetivo | extracto 8 | p.8]**

AIP Advances ARTICLE pubs.aip.org/aip/adv video streaming bitrate, maximize the user QoE, and effectively cope with complex network environment changes, as we explain the key steps of the algorithm in detail below. Inputs: We designed six parameters as inputs to the neural network, as shown in Eq. (2). By comprehensively analyzing the characteristics of each state’s information, the input parameters are divided into two categories, one for single values and one for continuous values. First, the agent will transmit the information (state si) of each chunk i observed from the environment to the deep neural network, si = (ci, ni, li, ⃗pi, ⃗di, ⃗zi). (2) This includes single-value types: ci denotes the current buffer size, ni denotes the remaining chunks in the video, and li denotes the bitrate of downloading the previous chunk. Considering the singlevalue independent features, we designed to use a fully connected layer to map each input feature to the feature space, which is a simple structure, easy to understand and implement, and usually converges faster during the training process. For continuous value type: ⃗pi denotes the network throughput of the past video chunk download, ⃗di denotes the download time of the past video chunk, and ⃗zi denotes the next video chunk size. Considering that these inputs are characterized by continuity, we adopt LSTM and a local attention mechanism to design the model. This structure can capture long short-term dependencies in the data while capturing local dependencies more effectively, thus improving the model’s ability to understand and utilize the information of the network environment. Policy update: Based on the observation of the input environmental state si, the agent updates the parameters of the policy network using the PPO metho

**[Reward / QoE / función objetivo | extracto 9 | p.9]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 4. Comparison of the effect of PPO and PPO with dual clipping. standard PPO algorithm and the blue partly showing the effect of the improved algorithm. The logic of the PPO algorithm is shown in Algorithm 1, where the policy parameters θ0 and value function parameters ϕ0 are first initialized. k iterations are then performed. In each iteration, the algorithm runs the current policy πk in the given environment, collecting a series of trajectory data Dk. These trajectory data include states, actions, and immediate rewards fed by the environment. Next, based on the collected reward values ˆRt and the current value function Vϕk, the advantage estimate is computed as ˆAt. The algorithm then updates the policy parameters to maximize the PPO objective, which improves the performance of the policy. At the same time, the value function is fitted using mean square error regression to assess the state value more accurately. The whole process is repeated until a predetermined number of iterations is reached. D. Perception of deep neural network units LSTM-LA Traditional reinforcement learning methods have certain disadvantages relative to deep reinforcement learning in terms of feature engineering requirements, generalization capability, training speed, high-dimensional state space processing capability, and continuous action space processing capability.41 These disadvantages limit the performance and application scope of traditional reinforcement learning methods. Especially when dealing with complex and large-scale problems, to cope with this problem, we consider fusing deep neural networks to improve algorithm performance and expect to achieve better results. By observing the inputs of the neural network and comprehensively analyzin

**[Reward / QoE / función objetivo | extracto 10 | p.12]**

AIP Advances ARTICLE pubs.aip.org/aip/adv dynamically controls the exploration strength of the strategy so as to improve the performance and stability of the video streaming transmission system under complex network conditions. The specific realization process is as follows: Entropy computation: first, the entropy of the current strategy is computed as H. For each strategy, the entropy can be computed by the following equation: H(π) = − n ∑ i=1 π(ai∣si ) log π(ai∣si ), (17) where π(ai∣si) denotes the probability that the intelligent body chooses action ai in state si. The randomness of the current strategy can be measured by this formula. Entropy difference: Calculate the difference ΔH between the current strategy entropy H and the target entropy Htarget. The calculation process is shown in the following equation: ΔH = H −Htarget. (18) The difference reflects the deviation of the entropy of the current strategy from the expected entropy. When ΔH > 0, it indicates that the randomness of the current strategy is higher than expected, at which time the entropy weight can be reduced and the exploration behavior can be decreased; conversely, the entropy weight is increased and exploration is increased. Update of entropy weights: finally, based on this entropy difference, the entropy weights are updated by the learning rate, which is updated as shown in the following equation: λentropy = λentropy −η ⋅tanh (H −Htarget) ⋅γ ⋅T, (19) where γ is the adjustment factor, T is the current number of training rounds, and η is the learning rate. To prevent the entropy weights from becoming too small, λentropy is also boundary-protected, as shown in the following equation: λentropy = max (λentropy, λminimum). (20) Finally, the system updates the strategy parameters in real time based on th

**[Reward / QoE / función objetivo | extracto 11 | p.13]**

AIP Advances ARTICLE pubs.aip.org/aip/adv of RL models by guiding them to be trained in network environments where they do not perform as well as the baseline. 7. NetLLM:47 A model-based approach that efficiently adapts to multiple network tasks by pre-training models to improve performance and generalization. Experimental setup: We randomly select 80% of the samples from the dataset as the training set and the remaining 20% as the test set. In the QoE function, the penalty weight coefficients μ and ρ for re-buffering time and video smoothness are set to 4.3 and 1, respectively. For the Actor network, we pass k = 8 past state information to the network. Among them, the LSTM layer contains 128 neurons, and the fully connected layer uses 128 neurons. The outputs of these layers are then aggregated with the other inputs in the hidden layer, and the softmax function is applied to generate the corresponding action probabilities for the Actor network. The same network structure is used for the Critic network to generate the action values for the Critic network, with the network learning rate configured as 10−4, the optimizer chosen as Adam, the discount factor γ = 0.99, and the target entropy set to 0.1 to ensure that the entropy weights were not less than 0.01. All of these experiments were trained and tested using the deep learning library PyTorch, and our hyperparameters were kept constant throughout the experiments. To ensure the reproducibility of the experimental results, this paper fixes the random seed as 42 during the training process. The training and inference are conducted on a server equipped with NVIDIA GeForce RTX 3090 GPUs and AMD EPYC 7302 Central Processing Unit (CPU), and the software environment consists of Python 3.9 and PyTorch 2.5.1, and the CUDA versio

**[Reward / QoE / función objetivo | extracto 12 | p.14]**

AIP Advances ARTICLE pubs.aip.org/aip/adv TABLE I. Performance comparison of different algorithms. Algorithm Average bitrate (kbps) Average re-buffering time (s) Average bitrate variation (kbps) (between each block) BOLA 1137.309 0.148 254.533 MPC 1127.01 0.101 137.946 Rate-based 947.212 0.122 78.349 Buffer-based 1132.585 0.119 351.978 Pensieve 1074.237 0.093 120.108 Genet 1017.24 0.047 89.556 NetLLM 1005.48 0.041 76.334 PLL-ABR 1107.901 0.088 105.491 QoE function [Eq. (1)] decomposition (for each factor): Bitrate Utility: corresponds to the first part N ∑ n=1 q(Rn) of the QoE function, indicating the currently selected bitrate. Re-buffering Penalty: corresponds to the second part μ N ∑ n=1 Tn of the QoE function, where Tn denotes the re-buffering time and μ is its penalty weight coefficient. Video Smoothness Penalty: corresponds to the third part ρ N ∑ n=1 ∣q(Rn+1) −q(Rn)∣of the QoE function, denoting the amount of bitrate variation between video chunks, and ρ is its penalty weight coefficient. According to the QoE function, we know that QoE is defined as the bitrate utility minus the re-buffering penalty minus the video smoothness penalty. In short, we want the bitrate utility to be as high as possible and the re-buffering and video smoothness penalties to be as low as possible. Figure 9 demonstrates a comparison of the performance of the PLL-ABR with five other representative algorithms in terms of each factor of QoE. As can be seen in Fig. 10, PLL-ABR performs well in the re-buffering penalty and video smoothness penalty modules, with PLL-ABR reducing the re-buffering penalty by 40.59% and 25.58% and reducing the video smoothness penalty by 58.55% and 70.03%, respectively, when compared to the best performers in terms of bitrate utility, BOLA and buffer-based. This

**[Reward / QoE / función objetivo | extracto 13 | p.15]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 10. QoE factors for different dualclip constants. TABLE II. Comparison of PLL-ABR ablation experiments. Method BU RP SP QoE elevate↑(%) PPO + LSTM 1.0786 0.3803 0.0910 52.88 - LA 1.0928 0.3774 0.0975 54.59 - Dual clip 1.0917 0.3826 0.0988 53.38 - NE-weights 1.0960 0.3697 0.1082 54.67 PLL-ABR 1.1079 0.3794 0.1055 55.45 uniformly adopted as the default setting of the double-clipping strategy in the experiments. C. Generalizability under diverse network conditions Considering the diversity of actual network environments, to verify the generalization ability of this paper’s algorithm for different physical network environments (network throughput ranges), the network dataset is further analyzed. Two typical network ranges (poor and good network) are selected for simulation experiments, and the real-time bitrate selections and corresponding buffer sizes of the PLL-ABR algorithm for the two network ranges are given separately. Robust MPC and buffer-based methods are compared, and the results are shown in Fig. 11. Example 1. The first example analyzes an application scenario with poor overall network conditions. It can be observed from Fig. 11(a) that the poorer network environment and objective network fluctuations bring more difficulties to the bitrate selection, especially reflected in robust MPC and buffer-based methods, due to the more inefficient buffer control levels of the two. The network fluctuates greatly when the timestamp is about 50 s and the buffer size drops dramatically, and the bitrate selection drops from 1.2 Mbps to nearly 0.3 Mbps, and the quality gap between before and after the video is too large, which directly affects the result of the QoE function and reduces the user experience. In contrast, by utilizing

### 4.x Entrenamiento / learning procedure

**[Entrenamiento / learning procedure | extracto 1 | p.1]**

 View Online  Export Citation RESEARCH ARTICLE | JULY 25 2025 Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming Jianwei Zhang  ; Yang Han ; Zengyu Cai ; Yuan Feng ; Liang Zhu AIP Advances 15, 075042 (2025) https://doi.org/10.1063/5.0277381 Articles You May Be Interested In Semiconductor lasers driven by self-sustained chaotic electronic oscillators and applications to optical chaos cryptography Chaos (July 2012) Optimal design of energy-efficient with traffic uncertainty in wireless body area networks AIP Advances (January 2026) Speech quality estimation with deep lattice networks J. Acoust. Soc. Am. (June 2021) 09 June 2026 09:26:24

**[Entrenamiento / learning procedure | extracto 2 | p.2]**

AIP Advances ARTICLE pubs.aip.org/aip/adv Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming Cite as: AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381 Submitted: 23 April 2025 • Accepted: 7 July 2025 • Published Online: 25 July 2025 Jianwei Zhang,1,a) Yang Han,1 Zengyu Cai,2 Yuan Feng,3 and Liang Zhu2 AFFILIATIONS 1 School of Software Engineering, Zhengzhou University of Light Industry, Zhengzhou 450003, China 2School of Computer Science and Technology, Zhengzhou University of Light Industry, Zhengzhou 450003, China 3School of Electronic Information, Zhengzhou University of Light Industry, Zhengzhou 450003, China a)Author to whom correspondence should be addressed: mailzjw@163.com ABSTRACT Driven by the digital era, video traffic is growing rapidly, and users’ demand for high-quality video experiences is increasing. Adaptive bitrate (ABR) algorithms, as a key technology to optimize the transmission performance of video streams, play an important role in improving the efficiency of communication networks and the quality of experience (QoE). However, existing ABR algorithms rely too much on fixed control rules and simplified environment models, which make it difficult to provide optimal performance under complex and changing physical network environments (e.g., bandwidth fluctuations, delays, and network congestion). To address these challenges, this paper proposes a new ABR algorithm, the deep reinforcement learning enhanced ABR video stream optimization algorithm (PLL-ABR), which adopts proximal policy optimization as a reinforcement learning training framework and combines the dual clipping mechanism and deep neural networks (long short-term memory and local attention mechanism) to improve the training efficiency and

**[Entrenamiento / learning procedure | extracto 3 | p.3]**

AIP Advances ARTICLE pubs.aip.org/aip/adv adjust the bitrate of the video according to the current network conditions and device performance to ensure that the user receives the best viewing experience. In practice, traditional heuristic ABR algorithms mainly include buffer-based5,6 and rate-based algorithms based on network throughput.7 Buffer-based algorithms adjust the bitrate based on monitoring the buffer status to maximize video quality and buffer utilization, but they are not sufficiently responsive to the dynamic network environment, which may lead to QoE degradation or buffer overflow. Rate-based algorithms dynamically adjust the bitrate by predicting the network bandwidth to ensure smooth video transmission, but they ignore the state of the client’s buffer, resulting in unstable performance. The robust MPC algorithm based on control theory integrates the buffer state and the predicted bandwidth to select the best bitrate,8 which improves performance; however, it relies too much on the accuracy of the bandwidth prediction, and once the prediction is inaccurate, performance will be significantly degraded. Recently, researchers have begun to explore more efficient and intelligent ABR algorithms. Among them, the reinforcement learning (RL) technique has become a hot research topic.9 As a machine learning method that interacts with the environment to learn optimal decision policy, reinforcement learning is well suited to be applied in the field of video streaming to improve the performance and stability of ABR algorithms. Past research has focused on traditional reinforcement learning methods, mainly including Q-learning10 and actor-critic.11 For example, Lin et al.12 applied Q-learning to ABR and significantly improved the performance by constructing Q-tables and

**[Entrenamiento / learning procedure | extracto 4 | p.4]**

AIP Advances ARTICLE pubs.aip.org/aip/adv ●An ABR method based on deep reinforcement learning is proposed, which adopts the PPO algorithm with a dual clipping mechanism as the training framework and combines with the LSTM-LA network to capture the long shortterm and local dependencies in the data, which significantly improves the performance of the ABR algorithm. A nonlinear entropy weight dynamic adjustment mechanism is introduced, which further improves the stability and efficiency of strategy optimization by dynamically adjusting the entropy weights and balancing the exploration and utilization, ensuring the high efficiency and flexibility of strategy updating during the training process. ●Experiments have been conducted on a public experimental dataset and compared with existing ABR algorithms. The experimental results show that the method proposed in this paper exhibits significant superiority in terms of overall QoE and the performance of various QoE factors, in addition to its generalization ability in different network environments, which is significantly better than that of other existing algorithms. The rest of the paper is organized as follows. Section II describes the application background of ABR and reviews related work on ABR methods. Section III describes the system model and gives the policy update method. Section IV evaluates the performance of the PLL-ABR method through extensive experimental comparisons. Section V concludes the paper. II. BACKGROUND AND RELATED WORK A. Adaptive video streaming and DASH protocol Adaptive video streaming, as a streaming media delivery technology, can dynamically adjust the bitrate and resolution of the video according to the performance of the user’s device and the current network conditions to ensure that the user rec

**[Entrenamiento / learning procedure | extracto 5 | p.5]**

AIP Advances ARTICLE pubs.aip.org/aip/adv behavioral policy for an intelligent body (agent) during its interaction with the environment. In deep reinforcement learning, an intelligent body optimizes its policy by continuously observing the state of the environment, performing actions, and receiving rewards so that it can make the best decisions when it encounters similar situations in the future. This approach has led to significant breakthroughs in several fields, including network resource management,25 autonomous driving,26 and robot control.27 For example, AlphaGo applied deep reinforcement learning in the game of Go to achieve performance beyond the human level, highlighting the potential and application value of the technology. In addition, deep reinforcement learning also performs well in several network scenarios, such as Software-Defined Networking (SDN), Vehicular Ad hoc NETworks (VANETs), and Wireless Sensor Networks (WSNs),28 demonstrating its great potential in improving network performance and resource utilization efficiency. In DRL, reinforcement learning guides the learning and decision-making processes of intelligence in complex environments by defining decision frameworks and policy-updating algorithms. Deep learning, on the other hand, is used to deal with problems such as function approximation and feature extraction in reinforcement learning to better realize learning and decision-making of intelligence in complex environments. ABR systems dynamically adjust the video bitrate according to network conditions and user requirements to provide the best viewing experience and QoE. Traditional ABR algorithms are usually heuristic rule-based or model-based approaches, which often have difficulty in dealing with complex network environments and video conten

**[Entrenamiento / learning procedure | extracto 6 | p.6]**

AIP Advances ARTICLE pubs.aip.org/aip/adv in variable network environments. Akhtar et al.32 proposed Oboe, an auto-tuning system that pre-calculates the optimal parameters suitable for different network conditions and dynamically adjusts these parameters at runtime based on the current network conditions to automatically optimize existing ABR algorithms. However, when the actual network conditions deviate from the basic assumptions of these ABR algorithms, this approach may exhibit instability. 2. ABR methods based on machine learning To address the shortcomings of traditional heuristics, based on the research of buffer-based and throughput-based adaptive algorithms, researchers have proposed some machine learning-based improvements. Claeys et al.33 proposed an HTTP adaptive streaming client based on adaptive Q-learning, which, unlike traditional heuristics, dynamically learns the optimal behavior corresponding to the current network environment. Chiariotti et al.34 proposed a reinforcement learning-based DASH client logic, which optimally selects the best representation through the Markov Decision Process (MDP) and ensures fast and accurate convergence of the learning through a parallel learning technique. Liu et al.12 combined a k-Nearest Neighbor (KNN) algorithm with a Q-learning algorithm to propose a new KNN-Q learning algorithm for seamless switching bitrate adaptation for video streaming. Mao et al.13 performed bitrate adaptation based on reinforcement learning, using Bayesian optimization to maximize QoE, while training a linear policy to reduce the delay between the video client and the simulated environment. However, the linear approach leads to a degradation of the algorithm’s performance. All of the above-mentioned algorithms are based on Reinforcement Learn

**[Entrenamiento / learning procedure | extracto 7 | p.7]**

AIP Advances ARTICLE pubs.aip.org/aip/adv III. SYSTEM MODEL This section describes the design and implementation of PLL-ABR. The system model fits the actual working mechanism of ABR video streaming in the current internet. We consider a scenario where a video player downloads video files from a server over the internet and plays them back to the user. The video file is divided into consecutive segments, and the server dynamically selects the most suitable segments for transmission based on network conditions and device performance to enhance the viewing experience. During transmission, the available bandwidth fluctuates over time and is affected by network congestion, wireless fading, and other factors. The user’s viewing experience depends not only on the video quality corresponding to the bitrate of the clip but also on playback characteristics such as heavy buffering. The goal of the player is to maximize the utility associated with the viewing experience while flexibly coping with the time-varying and uncertain bandwidth. A. Description of the problem The main goal of ABR is to optimize the user’s quality of the viewing experience to ensure that the user gets the best quality and smoothness when watching video or listening to audio. The QoE function from the literature8 is defined as the reward function in this paper, which is the most commonly used QoE reward function in the field of ABR, which can effectively reflect the user’s perception and expectation of service quality and facilitate experimental comparison with other ABR algorithms. The specific formula is shown in the following equation: QoE = N ∑ n=1 q(Rn) −μ N ∑ n=1 Tn −ρ N ∑ n=1 ∣q(Rn+1) −q(Rn)∣. (1) The QoE factor consists of the following three components: the first one is the video quality: q(Rn) deno

**[Entrenamiento / learning procedure | extracto 8 | p.8]**

AIP Advances ARTICLE pubs.aip.org/aip/adv video streaming bitrate, maximize the user QoE, and effectively cope with complex network environment changes, as we explain the key steps of the algorithm in detail below. Inputs: We designed six parameters as inputs to the neural network, as shown in Eq. (2). By comprehensively analyzing the characteristics of each state’s information, the input parameters are divided into two categories, one for single values and one for continuous values. First, the agent will transmit the information (state si) of each chunk i observed from the environment to the deep neural network, si = (ci, ni, li, ⃗pi, ⃗di, ⃗zi). (2) This includes single-value types: ci denotes the current buffer size, ni denotes the remaining chunks in the video, and li denotes the bitrate of downloading the previous chunk. Considering the singlevalue independent features, we designed to use a fully connected layer to map each input feature to the feature space, which is a simple structure, easy to understand and implement, and usually converges faster during the training process. For continuous value type: ⃗pi denotes the network throughput of the past video chunk download, ⃗di denotes the download time of the past video chunk, and ⃗zi denotes the next video chunk size. Considering that these inputs are characterized by continuity, we adopt LSTM and a local attention mechanism to design the model. This structure can capture long short-term dependencies in the data while capturing local dependencies more effectively, thus improving the model’s ability to understand and utilize the information of the network environment. Policy update: Based on the observation of the input environmental state si, the agent updates the parameters of the policy network using the PPO metho

**[Entrenamiento / learning procedure | extracto 9 | p.9]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 4. Comparison of the effect of PPO and PPO with dual clipping. standard PPO algorithm and the blue partly showing the effect of the improved algorithm. The logic of the PPO algorithm is shown in Algorithm 1, where the policy parameters θ0 and value function parameters ϕ0 are first initialized. k iterations are then performed. In each iteration, the algorithm runs the current policy πk in the given environment, collecting a series of trajectory data Dk. These trajectory data include states, actions, and immediate rewards fed by the environment. Next, based on the collected reward values ˆRt and the current value function Vϕk, the advantage estimate is computed as ˆAt. The algorithm then updates the policy parameters to maximize the PPO objective, which improves the performance of the policy. At the same time, the value function is fitted using mean square error regression to assess the state value more accurately. The whole process is repeated until a predetermined number of iterations is reached. D. Perception of deep neural network units LSTM-LA Traditional reinforcement learning methods have certain disadvantages relative to deep reinforcement learning in terms of feature engineering requirements, generalization capability, training speed, high-dimensional state space processing capability, and continuous action space processing capability.41 These disadvantages limit the performance and application scope of traditional reinforcement learning methods. Especially when dealing with complex and large-scale problems, to cope with this problem, we consider fusing deep neural networks to improve algorithm performance and expect to achieve better results. By observing the inputs of the neural network and comprehensively analyzin

**[Entrenamiento / learning procedure | extracto 10 | p.10]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 5. LSTM-LA neural network unit. dependencies among them, we introduce the LSTM. As a neural network structure specifically designed to process sequence data, the LSTM has memory units and gating mechanisms that can effectively capture and utilize the long short-term dependencies in sequence data. LSTM is a variant of recurrent neural network (RNN) commonly used to process sequence data. Compared to regular RNNs, LSTM is more effective in processing long sequence data because it can capture and utilize long-term dependencies in sequences, avoiding the problems of gradient vanishing and gradient explosion in regular RNNs. The core idea of LSTM networks is to introduce a structure called a “memory cell,” which controls the inputs, outputs, and state updates of the memory cell through a gating mechanism. Inside the memory cell, there is a long-term state called “cell state” Ct, which is used to hold information for a long time. At each time step, the LSTM receives input xt and the hidden state ht−1 from the previous time step, then updates the state of the memory cell based on the current input and the previous hidden state. Specifically, LSTM contains three gate mechanisms: forget gate, input gate, and output gate. The network structure of LSTM is shown in Fig. 6. They are calculated as follows. FIG. 6. LSTM network structure diagram. Forget gate: determines how much of a previous memory state is retained in the current time step. Its calculation formula is shown in the following equation: ft = σ(Wf ⋅[ht−1, xt] + bf ), (7) where σ is the sigmoid function, W f is the weight matrix of the forget gate, and b f is the bias. Input gate: decide how much new information to update to the memory cell. Its calculation formula is shown i

**[Entrenamiento / learning procedure | extracto 11 | p.11]**

AIP Advances ARTICLE pubs.aip.org/aip/adv 2. Capturing local dependencies with local attention There may be complex correlations and dependencies between input data, and these dependencies include not only long and shortterm dependencies but may also manifest as localized dependencies. Although LSTM has a good ability to model long and short-term dependencies, it has some limitations in capturing local correlations. For this reason, this paper introduces the local attention mechanism, which focuses on the information of local regions by assigning different attention weights to different positions of the sequence through a sliding window. The local attention mechanism has the flexibility and variability to adapt to sequence inputs of different lengths and forms, which helps to mine and model local dependencies more effectively. The local attention mechanism effectively reduces computational complexity and enhances local feature extraction by narrowing the attention window and focusing only on local regions of the input sequence. Compared with the O(n2) complexity of global attention, local attention requires only O(w × n) (w is the window size), which significantly improves the computational and storage efficiency in long sequence scenarios, especially suitable for applications with high real-time requirements or memory constraints. In addition, local attention is better at capturing short-time dependencies in the data (e.g., the video stream bitrate decision depends on the characteristics of the first few video blocks) and can flexibly adapt to different needs by dynamically adjusting the window size: a small window captures the fast-changing signals, and a large window captures the long dependencies. The idea is based on the sliding window approach, which calculates th

**[Entrenamiento / learning procedure | extracto 12 | p.12]**

AIP Advances ARTICLE pubs.aip.org/aip/adv dynamically controls the exploration strength of the strategy so as to improve the performance and stability of the video streaming transmission system under complex network conditions. The specific realization process is as follows: Entropy computation: first, the entropy of the current strategy is computed as H. For each strategy, the entropy can be computed by the following equation: H(π) = − n ∑ i=1 π(ai∣si ) log π(ai∣si ), (17) where π(ai∣si) denotes the probability that the intelligent body chooses action ai in state si. The randomness of the current strategy can be measured by this formula. Entropy difference: Calculate the difference ΔH between the current strategy entropy H and the target entropy Htarget. The calculation process is shown in the following equation: ΔH = H −Htarget. (18) The difference reflects the deviation of the entropy of the current strategy from the expected entropy. When ΔH > 0, it indicates that the randomness of the current strategy is higher than expected, at which time the entropy weight can be reduced and the exploration behavior can be decreased; conversely, the entropy weight is increased and exploration is increased. Update of entropy weights: finally, based on this entropy difference, the entropy weights are updated by the learning rate, which is updated as shown in the following equation: λentropy = λentropy −η ⋅tanh (H −Htarget) ⋅γ ⋅T, (19) where γ is the adjustment factor, T is the current number of training rounds, and η is the learning rate. To prevent the entropy weights from becoming too small, λentropy is also boundary-protected, as shown in the following equation: λentropy = max (λentropy, λminimum). (20) Finally, the system updates the strategy parameters in real time based on th

**[Entrenamiento / learning procedure | extracto 13 | p.13]**

AIP Advances ARTICLE pubs.aip.org/aip/adv of RL models by guiding them to be trained in network environments where they do not perform as well as the baseline. 7. NetLLM:47 A model-based approach that efficiently adapts to multiple network tasks by pre-training models to improve performance and generalization. Experimental setup: We randomly select 80% of the samples from the dataset as the training set and the remaining 20% as the test set. In the QoE function, the penalty weight coefficients μ and ρ for re-buffering time and video smoothness are set to 4.3 and 1, respectively. For the Actor network, we pass k = 8 past state information to the network. Among them, the LSTM layer contains 128 neurons, and the fully connected layer uses 128 neurons. The outputs of these layers are then aggregated with the other inputs in the hidden layer, and the softmax function is applied to generate the corresponding action probabilities for the Actor network. The same network structure is used for the Critic network to generate the action values for the Critic network, with the network learning rate configured as 10−4, the optimizer chosen as Adam, the discount factor γ = 0.99, and the target entropy set to 0.1 to ensure that the entropy weights were not less than 0.01. All of these experiments were trained and tested using the deep learning library PyTorch, and our hyperparameters were kept constant throughout the experiments. To ensure the reproducibility of the experimental results, this paper fixes the random seed as 42 during the training process. The training and inference are conducted on a server equipped with NVIDIA GeForce RTX 3090 GPUs and AMD EPYC 7302 Central Processing Unit (CPU), and the software environment consists of Python 3.9 and PyTorch 2.5.1, and the CUDA versio

**[Entrenamiento / learning procedure | extracto 14 | p.14]**

AIP Advances ARTICLE pubs.aip.org/aip/adv TABLE I. Performance comparison of different algorithms. Algorithm Average bitrate (kbps) Average re-buffering time (s) Average bitrate variation (kbps) (between each block) BOLA 1137.309 0.148 254.533 MPC 1127.01 0.101 137.946 Rate-based 947.212 0.122 78.349 Buffer-based 1132.585 0.119 351.978 Pensieve 1074.237 0.093 120.108 Genet 1017.24 0.047 89.556 NetLLM 1005.48 0.041 76.334 PLL-ABR 1107.901 0.088 105.491 QoE function [Eq. (1)] decomposition (for each factor): Bitrate Utility: corresponds to the first part N ∑ n=1 q(Rn) of the QoE function, indicating the currently selected bitrate. Re-buffering Penalty: corresponds to the second part μ N ∑ n=1 Tn of the QoE function, where Tn denotes the re-buffering time and μ is its penalty weight coefficient. Video Smoothness Penalty: corresponds to the third part ρ N ∑ n=1 ∣q(Rn+1) −q(Rn)∣of the QoE function, denoting the amount of bitrate variation between video chunks, and ρ is its penalty weight coefficient. According to the QoE function, we know that QoE is defined as the bitrate utility minus the re-buffering penalty minus the video smoothness penalty. In short, we want the bitrate utility to be as high as possible and the re-buffering and video smoothness penalties to be as low as possible. Figure 9 demonstrates a comparison of the performance of the PLL-ABR with five other representative algorithms in terms of each factor of QoE. As can be seen in Fig. 10, PLL-ABR performs well in the re-buffering penalty and video smoothness penalty modules, with PLL-ABR reducing the re-buffering penalty by 40.59% and 25.58% and reducing the video smoothness penalty by 58.55% and 70.03%, respectively, when compared to the best performers in terms of bitrate utility, BOLA and buffer-based. This

**[Entrenamiento / learning procedure | extracto 15 | p.15]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 10. QoE factors for different dualclip constants. TABLE II. Comparison of PLL-ABR ablation experiments. Method BU RP SP QoE elevate↑(%) PPO + LSTM 1.0786 0.3803 0.0910 52.88 - LA 1.0928 0.3774 0.0975 54.59 - Dual clip 1.0917 0.3826 0.0988 53.38 - NE-weights 1.0960 0.3697 0.1082 54.67 PLL-ABR 1.1079 0.3794 0.1055 55.45 uniformly adopted as the default setting of the double-clipping strategy in the experiments. C. Generalizability under diverse network conditions Considering the diversity of actual network environments, to verify the generalization ability of this paper’s algorithm for different physical network environments (network throughput ranges), the network dataset is further analyzed. Two typical network ranges (poor and good network) are selected for simulation experiments, and the real-time bitrate selections and corresponding buffer sizes of the PLL-ABR algorithm for the two network ranges are given separately. Robust MPC and buffer-based methods are compared, and the results are shown in Fig. 11. Example 1. The first example analyzes an application scenario with poor overall network conditions. It can be observed from Fig. 11(a) that the poorer network environment and objective network fluctuations bring more difficulties to the bitrate selection, especially reflected in robust MPC and buffer-based methods, due to the more inefficient buffer control levels of the two. The network fluctuates greatly when the timestamp is about 50 s and the buffer size drops dramatically, and the bitrate selection drops from 1.2 Mbps to nearly 0.3 Mbps, and the quality gap between before and after the video is too large, which directly affects the result of the QoE function and reduces the user experience. In contrast, by utilizing

### 4.x Datos / trazas / datasets / contenidos

**[Datos / trazas / datasets / contenidos | extracto 1 | p.1]**

 View Online  Export Citation RESEARCH ARTICLE | JULY 25 2025 Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming Jianwei Zhang  ; Yang Han ; Zengyu Cai ; Yuan Feng ; Liang Zhu AIP Advances 15, 075042 (2025) https://doi.org/10.1063/5.0277381 Articles You May Be Interested In Semiconductor lasers driven by self-sustained chaotic electronic oscillators and applications to optical chaos cryptography Chaos (July 2012) Optimal design of energy-efficient with traffic uncertainty in wireless body area networks AIP Advances (January 2026) Speech quality estimation with deep lattice networks J. Acoust. Soc. Am. (June 2021) 09 June 2026 09:26:24

**[Datos / trazas / datasets / contenidos | extracto 2 | p.2]**

AIP Advances ARTICLE pubs.aip.org/aip/adv Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming Cite as: AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381 Submitted: 23 April 2025 • Accepted: 7 July 2025 • Published Online: 25 July 2025 Jianwei Zhang,1,a) Yang Han,1 Zengyu Cai,2 Yuan Feng,3 and Liang Zhu2 AFFILIATIONS 1 School of Software Engineering, Zhengzhou University of Light Industry, Zhengzhou 450003, China 2School of Computer Science and Technology, Zhengzhou University of Light Industry, Zhengzhou 450003, China 3School of Electronic Information, Zhengzhou University of Light Industry, Zhengzhou 450003, China a)Author to whom correspondence should be addressed: mailzjw@163.com ABSTRACT Driven by the digital era, video traffic is growing rapidly, and users’ demand for high-quality video experiences is increasing. Adaptive bitrate (ABR) algorithms, as a key technology to optimize the transmission performance of video streams, play an important role in improving the efficiency of communication networks and the quality of experience (QoE). However, existing ABR algorithms rely too much on fixed control rules and simplified environment models, which make it difficult to provide optimal performance under complex and changing physical network environments (e.g., bandwidth fluctuations, delays, and network congestion). To address these challenges, this paper proposes a new ABR algorithm, the deep reinforcement learning enhanced ABR video stream optimization algorithm (PLL-ABR), which adopts proximal policy optimization as a reinforcement learning training framework and combines the dual clipping mechanism and deep neural networks (long short-term memory and local attention mechanism) to improve the training efficiency and

**[Datos / trazas / datasets / contenidos | extracto 3 | p.3]**

AIP Advances ARTICLE pubs.aip.org/aip/adv adjust the bitrate of the video according to the current network conditions and device performance to ensure that the user receives the best viewing experience. In practice, traditional heuristic ABR algorithms mainly include buffer-based5,6 and rate-based algorithms based on network throughput.7 Buffer-based algorithms adjust the bitrate based on monitoring the buffer status to maximize video quality and buffer utilization, but they are not sufficiently responsive to the dynamic network environment, which may lead to QoE degradation or buffer overflow. Rate-based algorithms dynamically adjust the bitrate by predicting the network bandwidth to ensure smooth video transmission, but they ignore the state of the client’s buffer, resulting in unstable performance. The robust MPC algorithm based on control theory integrates the buffer state and the predicted bandwidth to select the best bitrate,8 which improves performance; however, it relies too much on the accuracy of the bandwidth prediction, and once the prediction is inaccurate, performance will be significantly degraded. Recently, researchers have begun to explore more efficient and intelligent ABR algorithms. Among them, the reinforcement learning (RL) technique has become a hot research topic.9 As a machine learning method that interacts with the environment to learn optimal decision policy, reinforcement learning is well suited to be applied in the field of video streaming to improve the performance and stability of ABR algorithms. Past research has focused on traditional reinforcement learning methods, mainly including Q-learning10 and actor-critic.11 For example, Lin et al.12 applied Q-learning to ABR and significantly improved the performance by constructing Q-tables and

**[Datos / trazas / datasets / contenidos | extracto 4 | p.4]**

AIP Advances ARTICLE pubs.aip.org/aip/adv ●An ABR method based on deep reinforcement learning is proposed, which adopts the PPO algorithm with a dual clipping mechanism as the training framework and combines with the LSTM-LA network to capture the long shortterm and local dependencies in the data, which significantly improves the performance of the ABR algorithm. A nonlinear entropy weight dynamic adjustment mechanism is introduced, which further improves the stability and efficiency of strategy optimization by dynamically adjusting the entropy weights and balancing the exploration and utilization, ensuring the high efficiency and flexibility of strategy updating during the training process. ●Experiments have been conducted on a public experimental dataset and compared with existing ABR algorithms. The experimental results show that the method proposed in this paper exhibits significant superiority in terms of overall QoE and the performance of various QoE factors, in addition to its generalization ability in different network environments, which is significantly better than that of other existing algorithms. The rest of the paper is organized as follows. Section II describes the application background of ABR and reviews related work on ABR methods. Section III describes the system model and gives the policy update method. Section IV evaluates the performance of the PLL-ABR method through extensive experimental comparisons. Section V concludes the paper. II. BACKGROUND AND RELATED WORK A. Adaptive video streaming and DASH protocol Adaptive video streaming, as a streaming media delivery technology, can dynamically adjust the bitrate and resolution of the video according to the performance of the user’s device and the current network conditions to ensure that the user rec

**[Datos / trazas / datasets / contenidos | extracto 5 | p.5]**

AIP Advances ARTICLE pubs.aip.org/aip/adv behavioral policy for an intelligent body (agent) during its interaction with the environment. In deep reinforcement learning, an intelligent body optimizes its policy by continuously observing the state of the environment, performing actions, and receiving rewards so that it can make the best decisions when it encounters similar situations in the future. This approach has led to significant breakthroughs in several fields, including network resource management,25 autonomous driving,26 and robot control.27 For example, AlphaGo applied deep reinforcement learning in the game of Go to achieve performance beyond the human level, highlighting the potential and application value of the technology. In addition, deep reinforcement learning also performs well in several network scenarios, such as Software-Defined Networking (SDN), Vehicular Ad hoc NETworks (VANETs), and Wireless Sensor Networks (WSNs),28 demonstrating its great potential in improving network performance and resource utilization efficiency. In DRL, reinforcement learning guides the learning and decision-making processes of intelligence in complex environments by defining decision frameworks and policy-updating algorithms. Deep learning, on the other hand, is used to deal with problems such as function approximation and feature extraction in reinforcement learning to better realize learning and decision-making of intelligence in complex environments. ABR systems dynamically adjust the video bitrate according to network conditions and user requirements to provide the best viewing experience and QoE. Traditional ABR algorithms are usually heuristic rule-based or model-based approaches, which often have difficulty in dealing with complex network environments and video conten

**[Datos / trazas / datasets / contenidos | extracto 6 | p.6]**

AIP Advances ARTICLE pubs.aip.org/aip/adv in variable network environments. Akhtar et al.32 proposed Oboe, an auto-tuning system that pre-calculates the optimal parameters suitable for different network conditions and dynamically adjusts these parameters at runtime based on the current network conditions to automatically optimize existing ABR algorithms. However, when the actual network conditions deviate from the basic assumptions of these ABR algorithms, this approach may exhibit instability. 2. ABR methods based on machine learning To address the shortcomings of traditional heuristics, based on the research of buffer-based and throughput-based adaptive algorithms, researchers have proposed some machine learning-based improvements. Claeys et al.33 proposed an HTTP adaptive streaming client based on adaptive Q-learning, which, unlike traditional heuristics, dynamically learns the optimal behavior corresponding to the current network environment. Chiariotti et al.34 proposed a reinforcement learning-based DASH client logic, which optimally selects the best representation through the Markov Decision Process (MDP) and ensures fast and accurate convergence of the learning through a parallel learning technique. Liu et al.12 combined a k-Nearest Neighbor (KNN) algorithm with a Q-learning algorithm to propose a new KNN-Q learning algorithm for seamless switching bitrate adaptation for video streaming. Mao et al.13 performed bitrate adaptation based on reinforcement learning, using Bayesian optimization to maximize QoE, while training a linear policy to reduce the delay between the video client and the simulated environment. However, the linear approach leads to a degradation of the algorithm’s performance. All of the above-mentioned algorithms are based on Reinforcement Learn

**[Datos / trazas / datasets / contenidos | extracto 7 | p.7]**

AIP Advances ARTICLE pubs.aip.org/aip/adv III. SYSTEM MODEL This section describes the design and implementation of PLL-ABR. The system model fits the actual working mechanism of ABR video streaming in the current internet. We consider a scenario where a video player downloads video files from a server over the internet and plays them back to the user. The video file is divided into consecutive segments, and the server dynamically selects the most suitable segments for transmission based on network conditions and device performance to enhance the viewing experience. During transmission, the available bandwidth fluctuates over time and is affected by network congestion, wireless fading, and other factors. The user’s viewing experience depends not only on the video quality corresponding to the bitrate of the clip but also on playback characteristics such as heavy buffering. The goal of the player is to maximize the utility associated with the viewing experience while flexibly coping with the time-varying and uncertain bandwidth. A. Description of the problem The main goal of ABR is to optimize the user’s quality of the viewing experience to ensure that the user gets the best quality and smoothness when watching video or listening to audio. The QoE function from the literature8 is defined as the reward function in this paper, which is the most commonly used QoE reward function in the field of ABR, which can effectively reflect the user’s perception and expectation of service quality and facilitate experimental comparison with other ABR algorithms. The specific formula is shown in the following equation: QoE = N ∑ n=1 q(Rn) −μ N ∑ n=1 Tn −ρ N ∑ n=1 ∣q(Rn+1) −q(Rn)∣. (1) The QoE factor consists of the following three components: the first one is the video quality: q(Rn) deno

**[Datos / trazas / datasets / contenidos | extracto 8 | p.8]**

AIP Advances ARTICLE pubs.aip.org/aip/adv video streaming bitrate, maximize the user QoE, and effectively cope with complex network environment changes, as we explain the key steps of the algorithm in detail below. Inputs: We designed six parameters as inputs to the neural network, as shown in Eq. (2). By comprehensively analyzing the characteristics of each state’s information, the input parameters are divided into two categories, one for single values and one for continuous values. First, the agent will transmit the information (state si) of each chunk i observed from the environment to the deep neural network, si = (ci, ni, li, ⃗pi, ⃗di, ⃗zi). (2) This includes single-value types: ci denotes the current buffer size, ni denotes the remaining chunks in the video, and li denotes the bitrate of downloading the previous chunk. Considering the singlevalue independent features, we designed to use a fully connected layer to map each input feature to the feature space, which is a simple structure, easy to understand and implement, and usually converges faster during the training process. For continuous value type: ⃗pi denotes the network throughput of the past video chunk download, ⃗di denotes the download time of the past video chunk, and ⃗zi denotes the next video chunk size. Considering that these inputs are characterized by continuity, we adopt LSTM and a local attention mechanism to design the model. This structure can capture long short-term dependencies in the data while capturing local dependencies more effectively, thus improving the model’s ability to understand and utilize the information of the network environment. Policy update: Based on the observation of the input environmental state si, the agent updates the parameters of the policy network using the PPO metho

**[Datos / trazas / datasets / contenidos | extracto 9 | p.9]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 4. Comparison of the effect of PPO and PPO with dual clipping. standard PPO algorithm and the blue partly showing the effect of the improved algorithm. The logic of the PPO algorithm is shown in Algorithm 1, where the policy parameters θ0 and value function parameters ϕ0 are first initialized. k iterations are then performed. In each iteration, the algorithm runs the current policy πk in the given environment, collecting a series of trajectory data Dk. These trajectory data include states, actions, and immediate rewards fed by the environment. Next, based on the collected reward values ˆRt and the current value function Vϕk, the advantage estimate is computed as ˆAt. The algorithm then updates the policy parameters to maximize the PPO objective, which improves the performance of the policy. At the same time, the value function is fitted using mean square error regression to assess the state value more accurately. The whole process is repeated until a predetermined number of iterations is reached. D. Perception of deep neural network units LSTM-LA Traditional reinforcement learning methods have certain disadvantages relative to deep reinforcement learning in terms of feature engineering requirements, generalization capability, training speed, high-dimensional state space processing capability, and continuous action space processing capability.41 These disadvantages limit the performance and application scope of traditional reinforcement learning methods. Especially when dealing with complex and large-scale problems, to cope with this problem, we consider fusing deep neural networks to improve algorithm performance and expect to achieve better results. By observing the inputs of the neural network and comprehensively analyzin

**[Datos / trazas / datasets / contenidos | extracto 10 | p.11]**

AIP Advances ARTICLE pubs.aip.org/aip/adv 2. Capturing local dependencies with local attention There may be complex correlations and dependencies between input data, and these dependencies include not only long and shortterm dependencies but may also manifest as localized dependencies. Although LSTM has a good ability to model long and short-term dependencies, it has some limitations in capturing local correlations. For this reason, this paper introduces the local attention mechanism, which focuses on the information of local regions by assigning different attention weights to different positions of the sequence through a sliding window. The local attention mechanism has the flexibility and variability to adapt to sequence inputs of different lengths and forms, which helps to mine and model local dependencies more effectively. The local attention mechanism effectively reduces computational complexity and enhances local feature extraction by narrowing the attention window and focusing only on local regions of the input sequence. Compared with the O(n2) complexity of global attention, local attention requires only O(w × n) (w is the window size), which significantly improves the computational and storage efficiency in long sequence scenarios, especially suitable for applications with high real-time requirements or memory constraints. In addition, local attention is better at capturing short-time dependencies in the data (e.g., the video stream bitrate decision depends on the characteristics of the first few video blocks) and can flexibly adapt to different needs by dynamically adjusting the window size: a small window captures the fast-changing signals, and a large window captures the long dependencies. The idea is based on the sliding window approach, which calculates th

**[Datos / trazas / datasets / contenidos | extracto 11 | p.12]**

AIP Advances ARTICLE pubs.aip.org/aip/adv dynamically controls the exploration strength of the strategy so as to improve the performance and stability of the video streaming transmission system under complex network conditions. The specific realization process is as follows: Entropy computation: first, the entropy of the current strategy is computed as H. For each strategy, the entropy can be computed by the following equation: H(π) = − n ∑ i=1 π(ai∣si ) log π(ai∣si ), (17) where π(ai∣si) denotes the probability that the intelligent body chooses action ai in state si. The randomness of the current strategy can be measured by this formula. Entropy difference: Calculate the difference ΔH between the current strategy entropy H and the target entropy Htarget. The calculation process is shown in the following equation: ΔH = H −Htarget. (18) The difference reflects the deviation of the entropy of the current strategy from the expected entropy. When ΔH > 0, it indicates that the randomness of the current strategy is higher than expected, at which time the entropy weight can be reduced and the exploration behavior can be decreased; conversely, the entropy weight is increased and exploration is increased. Update of entropy weights: finally, based on this entropy difference, the entropy weights are updated by the learning rate, which is updated as shown in the following equation: λentropy = λentropy −η ⋅tanh (H −Htarget) ⋅γ ⋅T, (19) where γ is the adjustment factor, T is the current number of training rounds, and η is the learning rate. To prevent the entropy weights from becoming too small, λentropy is also boundary-protected, as shown in the following equation: λentropy = max (λentropy, λminimum). (20) Finally, the system updates the strategy parameters in real time based on th

**[Datos / trazas / datasets / contenidos | extracto 12 | p.13]**

AIP Advances ARTICLE pubs.aip.org/aip/adv of RL models by guiding them to be trained in network environments where they do not perform as well as the baseline. 7. NetLLM:47 A model-based approach that efficiently adapts to multiple network tasks by pre-training models to improve performance and generalization. Experimental setup: We randomly select 80% of the samples from the dataset as the training set and the remaining 20% as the test set. In the QoE function, the penalty weight coefficients μ and ρ for re-buffering time and video smoothness are set to 4.3 and 1, respectively. For the Actor network, we pass k = 8 past state information to the network. Among them, the LSTM layer contains 128 neurons, and the fully connected layer uses 128 neurons. The outputs of these layers are then aggregated with the other inputs in the hidden layer, and the softmax function is applied to generate the corresponding action probabilities for the Actor network. The same network structure is used for the Critic network to generate the action values for the Critic network, with the network learning rate configured as 10−4, the optimizer chosen as Adam, the discount factor γ = 0.99, and the target entropy set to 0.1 to ensure that the entropy weights were not less than 0.01. All of these experiments were trained and tested using the deep learning library PyTorch, and our hyperparameters were kept constant throughout the experiments. To ensure the reproducibility of the experimental results, this paper fixes the random seed as 42 during the training process. The training and inference are conducted on a server equipped with NVIDIA GeForce RTX 3090 GPUs and AMD EPYC 7302 Central Processing Unit (CPU), and the software environment consists of Python 3.9 and PyTorch 2.5.1, and the CUDA versio

**[Datos / trazas / datasets / contenidos | extracto 13 | p.14]**

AIP Advances ARTICLE pubs.aip.org/aip/adv TABLE I. Performance comparison of different algorithms. Algorithm Average bitrate (kbps) Average re-buffering time (s) Average bitrate variation (kbps) (between each block) BOLA 1137.309 0.148 254.533 MPC 1127.01 0.101 137.946 Rate-based 947.212 0.122 78.349 Buffer-based 1132.585 0.119 351.978 Pensieve 1074.237 0.093 120.108 Genet 1017.24 0.047 89.556 NetLLM 1005.48 0.041 76.334 PLL-ABR 1107.901 0.088 105.491 QoE function [Eq. (1)] decomposition (for each factor): Bitrate Utility: corresponds to the first part N ∑ n=1 q(Rn) of the QoE function, indicating the currently selected bitrate. Re-buffering Penalty: corresponds to the second part μ N ∑ n=1 Tn of the QoE function, where Tn denotes the re-buffering time and μ is its penalty weight coefficient. Video Smoothness Penalty: corresponds to the third part ρ N ∑ n=1 ∣q(Rn+1) −q(Rn)∣of the QoE function, denoting the amount of bitrate variation between video chunks, and ρ is its penalty weight coefficient. According to the QoE function, we know that QoE is defined as the bitrate utility minus the re-buffering penalty minus the video smoothness penalty. In short, we want the bitrate utility to be as high as possible and the re-buffering and video smoothness penalties to be as low as possible. Figure 9 demonstrates a comparison of the performance of the PLL-ABR with five other representative algorithms in terms of each factor of QoE. As can be seen in Fig. 10, PLL-ABR performs well in the re-buffering penalty and video smoothness penalty modules, with PLL-ABR reducing the re-buffering penalty by 40.59% and 25.58% and reducing the video smoothness penalty by 58.55% and 70.03%, respectively, when compared to the best performers in terms of bitrate utility, BOLA and buffer-based. This

**[Datos / trazas / datasets / contenidos | extracto 14 | p.15]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 10. QoE factors for different dualclip constants. TABLE II. Comparison of PLL-ABR ablation experiments. Method BU RP SP QoE elevate↑(%) PPO + LSTM 1.0786 0.3803 0.0910 52.88 - LA 1.0928 0.3774 0.0975 54.59 - Dual clip 1.0917 0.3826 0.0988 53.38 - NE-weights 1.0960 0.3697 0.1082 54.67 PLL-ABR 1.1079 0.3794 0.1055 55.45 uniformly adopted as the default setting of the double-clipping strategy in the experiments. C. Generalizability under diverse network conditions Considering the diversity of actual network environments, to verify the generalization ability of this paper’s algorithm for different physical network environments (network throughput ranges), the network dataset is further analyzed. Two typical network ranges (poor and good network) are selected for simulation experiments, and the real-time bitrate selections and corresponding buffer sizes of the PLL-ABR algorithm for the two network ranges are given separately. Robust MPC and buffer-based methods are compared, and the results are shown in Fig. 11. Example 1. The first example analyzes an application scenario with poor overall network conditions. It can be observed from Fig. 11(a) that the poorer network environment and objective network fluctuations bring more difficulties to the bitrate selection, especially reflected in robust MPC and buffer-based methods, due to the more inefficient buffer control levels of the two. The network fluctuates greatly when the timestamp is about 50 s and the buffer size drops dramatically, and the bitrate selection drops from 1.2 Mbps to nearly 0.3 Mbps, and the quality gap between before and after the video is too large, which directly affects the result of the QoE function and reduces the user experience. In contrast, by utilizing

### 4.x Evaluación / baselines / experimentos

**[Evaluación / baselines / experimentos | extracto 1 | p.2]**

AIP Advances ARTICLE pubs.aip.org/aip/adv Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming Cite as: AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381 Submitted: 23 April 2025 • Accepted: 7 July 2025 • Published Online: 25 July 2025 Jianwei Zhang,1,a) Yang Han,1 Zengyu Cai,2 Yuan Feng,3 and Liang Zhu2 AFFILIATIONS 1 School of Software Engineering, Zhengzhou University of Light Industry, Zhengzhou 450003, China 2School of Computer Science and Technology, Zhengzhou University of Light Industry, Zhengzhou 450003, China 3School of Electronic Information, Zhengzhou University of Light Industry, Zhengzhou 450003, China a)Author to whom correspondence should be addressed: mailzjw@163.com ABSTRACT Driven by the digital era, video traffic is growing rapidly, and users’ demand for high-quality video experiences is increasing. Adaptive bitrate (ABR) algorithms, as a key technology to optimize the transmission performance of video streams, play an important role in improving the efficiency of communication networks and the quality of experience (QoE). However, existing ABR algorithms rely too much on fixed control rules and simplified environment models, which make it difficult to provide optimal performance under complex and changing physical network environments (e.g., bandwidth fluctuations, delays, and network congestion). To address these challenges, this paper proposes a new ABR algorithm, the deep reinforcement learning enhanced ABR video stream optimization algorithm (PLL-ABR), which adopts proximal policy optimization as a reinforcement learning training framework and combines the dual clipping mechanism and deep neural networks (long short-term memory and local attention mechanism) to improve the training efficiency and

**[Evaluación / baselines / experimentos | extracto 2 | p.3]**

AIP Advances ARTICLE pubs.aip.org/aip/adv adjust the bitrate of the video according to the current network conditions and device performance to ensure that the user receives the best viewing experience. In practice, traditional heuristic ABR algorithms mainly include buffer-based5,6 and rate-based algorithms based on network throughput.7 Buffer-based algorithms adjust the bitrate based on monitoring the buffer status to maximize video quality and buffer utilization, but they are not sufficiently responsive to the dynamic network environment, which may lead to QoE degradation or buffer overflow. Rate-based algorithms dynamically adjust the bitrate by predicting the network bandwidth to ensure smooth video transmission, but they ignore the state of the client’s buffer, resulting in unstable performance. The robust MPC algorithm based on control theory integrates the buffer state and the predicted bandwidth to select the best bitrate,8 which improves performance; however, it relies too much on the accuracy of the bandwidth prediction, and once the prediction is inaccurate, performance will be significantly degraded. Recently, researchers have begun to explore more efficient and intelligent ABR algorithms. Among them, the reinforcement learning (RL) technique has become a hot research topic.9 As a machine learning method that interacts with the environment to learn optimal decision policy, reinforcement learning is well suited to be applied in the field of video streaming to improve the performance and stability of ABR algorithms. Past research has focused on traditional reinforcement learning methods, mainly including Q-learning10 and actor-critic.11 For example, Lin et al.12 applied Q-learning to ABR and significantly improved the performance by constructing Q-tables and

**[Evaluación / baselines / experimentos | extracto 3 | p.4]**

AIP Advances ARTICLE pubs.aip.org/aip/adv ●An ABR method based on deep reinforcement learning is proposed, which adopts the PPO algorithm with a dual clipping mechanism as the training framework and combines with the LSTM-LA network to capture the long shortterm and local dependencies in the data, which significantly improves the performance of the ABR algorithm. A nonlinear entropy weight dynamic adjustment mechanism is introduced, which further improves the stability and efficiency of strategy optimization by dynamically adjusting the entropy weights and balancing the exploration and utilization, ensuring the high efficiency and flexibility of strategy updating during the training process. ●Experiments have been conducted on a public experimental dataset and compared with existing ABR algorithms. The experimental results show that the method proposed in this paper exhibits significant superiority in terms of overall QoE and the performance of various QoE factors, in addition to its generalization ability in different network environments, which is significantly better than that of other existing algorithms. The rest of the paper is organized as follows. Section II describes the application background of ABR and reviews related work on ABR methods. Section III describes the system model and gives the policy update method. Section IV evaluates the performance of the PLL-ABR method through extensive experimental comparisons. Section V concludes the paper. II. BACKGROUND AND RELATED WORK A. Adaptive video streaming and DASH protocol Adaptive video streaming, as a streaming media delivery technology, can dynamically adjust the bitrate and resolution of the video according to the performance of the user’s device and the current network conditions to ensure that the user rec

**[Evaluación / baselines / experimentos | extracto 4 | p.5]**

AIP Advances ARTICLE pubs.aip.org/aip/adv behavioral policy for an intelligent body (agent) during its interaction with the environment. In deep reinforcement learning, an intelligent body optimizes its policy by continuously observing the state of the environment, performing actions, and receiving rewards so that it can make the best decisions when it encounters similar situations in the future. This approach has led to significant breakthroughs in several fields, including network resource management,25 autonomous driving,26 and robot control.27 For example, AlphaGo applied deep reinforcement learning in the game of Go to achieve performance beyond the human level, highlighting the potential and application value of the technology. In addition, deep reinforcement learning also performs well in several network scenarios, such as Software-Defined Networking (SDN), Vehicular Ad hoc NETworks (VANETs), and Wireless Sensor Networks (WSNs),28 demonstrating its great potential in improving network performance and resource utilization efficiency. In DRL, reinforcement learning guides the learning and decision-making processes of intelligence in complex environments by defining decision frameworks and policy-updating algorithms. Deep learning, on the other hand, is used to deal with problems such as function approximation and feature extraction in reinforcement learning to better realize learning and decision-making of intelligence in complex environments. ABR systems dynamically adjust the video bitrate according to network conditions and user requirements to provide the best viewing experience and QoE. Traditional ABR algorithms are usually heuristic rule-based or model-based approaches, which often have difficulty in dealing with complex network environments and video conten

**[Evaluación / baselines / experimentos | extracto 5 | p.6]**

AIP Advances ARTICLE pubs.aip.org/aip/adv in variable network environments. Akhtar et al.32 proposed Oboe, an auto-tuning system that pre-calculates the optimal parameters suitable for different network conditions and dynamically adjusts these parameters at runtime based on the current network conditions to automatically optimize existing ABR algorithms. However, when the actual network conditions deviate from the basic assumptions of these ABR algorithms, this approach may exhibit instability. 2. ABR methods based on machine learning To address the shortcomings of traditional heuristics, based on the research of buffer-based and throughput-based adaptive algorithms, researchers have proposed some machine learning-based improvements. Claeys et al.33 proposed an HTTP adaptive streaming client based on adaptive Q-learning, which, unlike traditional heuristics, dynamically learns the optimal behavior corresponding to the current network environment. Chiariotti et al.34 proposed a reinforcement learning-based DASH client logic, which optimally selects the best representation through the Markov Decision Process (MDP) and ensures fast and accurate convergence of the learning through a parallel learning technique. Liu et al.12 combined a k-Nearest Neighbor (KNN) algorithm with a Q-learning algorithm to propose a new KNN-Q learning algorithm for seamless switching bitrate adaptation for video streaming. Mao et al.13 performed bitrate adaptation based on reinforcement learning, using Bayesian optimization to maximize QoE, while training a linear policy to reduce the delay between the video client and the simulated environment. However, the linear approach leads to a degradation of the algorithm’s performance. All of the above-mentioned algorithms are based on Reinforcement Learn

**[Evaluación / baselines / experimentos | extracto 6 | p.7]**

AIP Advances ARTICLE pubs.aip.org/aip/adv III. SYSTEM MODEL This section describes the design and implementation of PLL-ABR. The system model fits the actual working mechanism of ABR video streaming in the current internet. We consider a scenario where a video player downloads video files from a server over the internet and plays them back to the user. The video file is divided into consecutive segments, and the server dynamically selects the most suitable segments for transmission based on network conditions and device performance to enhance the viewing experience. During transmission, the available bandwidth fluctuates over time and is affected by network congestion, wireless fading, and other factors. The user’s viewing experience depends not only on the video quality corresponding to the bitrate of the clip but also on playback characteristics such as heavy buffering. The goal of the player is to maximize the utility associated with the viewing experience while flexibly coping with the time-varying and uncertain bandwidth. A. Description of the problem The main goal of ABR is to optimize the user’s quality of the viewing experience to ensure that the user gets the best quality and smoothness when watching video or listening to audio. The QoE function from the literature8 is defined as the reward function in this paper, which is the most commonly used QoE reward function in the field of ABR, which can effectively reflect the user’s perception and expectation of service quality and facilitate experimental comparison with other ABR algorithms. The specific formula is shown in the following equation: QoE = N ∑ n=1 q(Rn) −μ N ∑ n=1 Tn −ρ N ∑ n=1 ∣q(Rn+1) −q(Rn)∣. (1) The QoE factor consists of the following three components: the first one is the video quality: q(Rn) deno

**[Evaluación / baselines / experimentos | extracto 7 | p.8]**

AIP Advances ARTICLE pubs.aip.org/aip/adv video streaming bitrate, maximize the user QoE, and effectively cope with complex network environment changes, as we explain the key steps of the algorithm in detail below. Inputs: We designed six parameters as inputs to the neural network, as shown in Eq. (2). By comprehensively analyzing the characteristics of each state’s information, the input parameters are divided into two categories, one for single values and one for continuous values. First, the agent will transmit the information (state si) of each chunk i observed from the environment to the deep neural network, si = (ci, ni, li, ⃗pi, ⃗di, ⃗zi). (2) This includes single-value types: ci denotes the current buffer size, ni denotes the remaining chunks in the video, and li denotes the bitrate of downloading the previous chunk. Considering the singlevalue independent features, we designed to use a fully connected layer to map each input feature to the feature space, which is a simple structure, easy to understand and implement, and usually converges faster during the training process. For continuous value type: ⃗pi denotes the network throughput of the past video chunk download, ⃗di denotes the download time of the past video chunk, and ⃗zi denotes the next video chunk size. Considering that these inputs are characterized by continuity, we adopt LSTM and a local attention mechanism to design the model. This structure can capture long short-term dependencies in the data while capturing local dependencies more effectively, thus improving the model’s ability to understand and utilize the information of the network environment. Policy update: Based on the observation of the input environmental state si, the agent updates the parameters of the policy network using the PPO metho

**[Evaluación / baselines / experimentos | extracto 8 | p.9]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 4. Comparison of the effect of PPO and PPO with dual clipping. standard PPO algorithm and the blue partly showing the effect of the improved algorithm. The logic of the PPO algorithm is shown in Algorithm 1, where the policy parameters θ0 and value function parameters ϕ0 are first initialized. k iterations are then performed. In each iteration, the algorithm runs the current policy πk in the given environment, collecting a series of trajectory data Dk. These trajectory data include states, actions, and immediate rewards fed by the environment. Next, based on the collected reward values ˆRt and the current value function Vϕk, the advantage estimate is computed as ˆAt. The algorithm then updates the policy parameters to maximize the PPO objective, which improves the performance of the policy. At the same time, the value function is fitted using mean square error regression to assess the state value more accurately. The whole process is repeated until a predetermined number of iterations is reached. D. Perception of deep neural network units LSTM-LA Traditional reinforcement learning methods have certain disadvantages relative to deep reinforcement learning in terms of feature engineering requirements, generalization capability, training speed, high-dimensional state space processing capability, and continuous action space processing capability.41 These disadvantages limit the performance and application scope of traditional reinforcement learning methods. Especially when dealing with complex and large-scale problems, to cope with this problem, we consider fusing deep neural networks to improve algorithm performance and expect to achieve better results. By observing the inputs of the neural network and comprehensively analyzin

**[Evaluación / baselines / experimentos | extracto 9 | p.10]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 5. LSTM-LA neural network unit. dependencies among them, we introduce the LSTM. As a neural network structure specifically designed to process sequence data, the LSTM has memory units and gating mechanisms that can effectively capture and utilize the long short-term dependencies in sequence data. LSTM is a variant of recurrent neural network (RNN) commonly used to process sequence data. Compared to regular RNNs, LSTM is more effective in processing long sequence data because it can capture and utilize long-term dependencies in sequences, avoiding the problems of gradient vanishing and gradient explosion in regular RNNs. The core idea of LSTM networks is to introduce a structure called a “memory cell,” which controls the inputs, outputs, and state updates of the memory cell through a gating mechanism. Inside the memory cell, there is a long-term state called “cell state” Ct, which is used to hold information for a long time. At each time step, the LSTM receives input xt and the hidden state ht−1 from the previous time step, then updates the state of the memory cell based on the current input and the previous hidden state. Specifically, LSTM contains three gate mechanisms: forget gate, input gate, and output gate. The network structure of LSTM is shown in Fig. 6. They are calculated as follows. FIG. 6. LSTM network structure diagram. Forget gate: determines how much of a previous memory state is retained in the current time step. Its calculation formula is shown in the following equation: ft = σ(Wf ⋅[ht−1, xt] + bf ), (7) where σ is the sigmoid function, W f is the weight matrix of the forget gate, and b f is the bias. Input gate: decide how much new information to update to the memory cell. Its calculation formula is shown i

**[Evaluación / baselines / experimentos | extracto 10 | p.11]**

AIP Advances ARTICLE pubs.aip.org/aip/adv 2. Capturing local dependencies with local attention There may be complex correlations and dependencies between input data, and these dependencies include not only long and shortterm dependencies but may also manifest as localized dependencies. Although LSTM has a good ability to model long and short-term dependencies, it has some limitations in capturing local correlations. For this reason, this paper introduces the local attention mechanism, which focuses on the information of local regions by assigning different attention weights to different positions of the sequence through a sliding window. The local attention mechanism has the flexibility and variability to adapt to sequence inputs of different lengths and forms, which helps to mine and model local dependencies more effectively. The local attention mechanism effectively reduces computational complexity and enhances local feature extraction by narrowing the attention window and focusing only on local regions of the input sequence. Compared with the O(n2) complexity of global attention, local attention requires only O(w × n) (w is the window size), which significantly improves the computational and storage efficiency in long sequence scenarios, especially suitable for applications with high real-time requirements or memory constraints. In addition, local attention is better at capturing short-time dependencies in the data (e.g., the video stream bitrate decision depends on the characteristics of the first few video blocks) and can flexibly adapt to different needs by dynamically adjusting the window size: a small window captures the fast-changing signals, and a large window captures the long dependencies. The idea is based on the sliding window approach, which calculates th

**[Evaluación / baselines / experimentos | extracto 11 | p.12]**

AIP Advances ARTICLE pubs.aip.org/aip/adv dynamically controls the exploration strength of the strategy so as to improve the performance and stability of the video streaming transmission system under complex network conditions. The specific realization process is as follows: Entropy computation: first, the entropy of the current strategy is computed as H. For each strategy, the entropy can be computed by the following equation: H(π) = − n ∑ i=1 π(ai∣si ) log π(ai∣si ), (17) where π(ai∣si) denotes the probability that the intelligent body chooses action ai in state si. The randomness of the current strategy can be measured by this formula. Entropy difference: Calculate the difference ΔH between the current strategy entropy H and the target entropy Htarget. The calculation process is shown in the following equation: ΔH = H −Htarget. (18) The difference reflects the deviation of the entropy of the current strategy from the expected entropy. When ΔH > 0, it indicates that the randomness of the current strategy is higher than expected, at which time the entropy weight can be reduced and the exploration behavior can be decreased; conversely, the entropy weight is increased and exploration is increased. Update of entropy weights: finally, based on this entropy difference, the entropy weights are updated by the learning rate, which is updated as shown in the following equation: λentropy = λentropy −η ⋅tanh (H −Htarget) ⋅γ ⋅T, (19) where γ is the adjustment factor, T is the current number of training rounds, and η is the learning rate. To prevent the entropy weights from becoming too small, λentropy is also boundary-protected, as shown in the following equation: λentropy = max (λentropy, λminimum). (20) Finally, the system updates the strategy parameters in real time based on th

**[Evaluación / baselines / experimentos | extracto 12 | p.13]**

AIP Advances ARTICLE pubs.aip.org/aip/adv of RL models by guiding them to be trained in network environments where they do not perform as well as the baseline. 7. NetLLM:47 A model-based approach that efficiently adapts to multiple network tasks by pre-training models to improve performance and generalization. Experimental setup: We randomly select 80% of the samples from the dataset as the training set and the remaining 20% as the test set. In the QoE function, the penalty weight coefficients μ and ρ for re-buffering time and video smoothness are set to 4.3 and 1, respectively. For the Actor network, we pass k = 8 past state information to the network. Among them, the LSTM layer contains 128 neurons, and the fully connected layer uses 128 neurons. The outputs of these layers are then aggregated with the other inputs in the hidden layer, and the softmax function is applied to generate the corresponding action probabilities for the Actor network. The same network structure is used for the Critic network to generate the action values for the Critic network, with the network learning rate configured as 10−4, the optimizer chosen as Adam, the discount factor γ = 0.99, and the target entropy set to 0.1 to ensure that the entropy weights were not less than 0.01. All of these experiments were trained and tested using the deep learning library PyTorch, and our hyperparameters were kept constant throughout the experiments. To ensure the reproducibility of the experimental results, this paper fixes the random seed as 42 during the training process. The training and inference are conducted on a server equipped with NVIDIA GeForce RTX 3090 GPUs and AMD EPYC 7302 Central Processing Unit (CPU), and the software environment consists of Python 3.9 and PyTorch 2.5.1, and the CUDA versio

**[Evaluación / baselines / experimentos | extracto 13 | p.14]**

AIP Advances ARTICLE pubs.aip.org/aip/adv TABLE I. Performance comparison of different algorithms. Algorithm Average bitrate (kbps) Average re-buffering time (s) Average bitrate variation (kbps) (between each block) BOLA 1137.309 0.148 254.533 MPC 1127.01 0.101 137.946 Rate-based 947.212 0.122 78.349 Buffer-based 1132.585 0.119 351.978 Pensieve 1074.237 0.093 120.108 Genet 1017.24 0.047 89.556 NetLLM 1005.48 0.041 76.334 PLL-ABR 1107.901 0.088 105.491 QoE function [Eq. (1)] decomposition (for each factor): Bitrate Utility: corresponds to the first part N ∑ n=1 q(Rn) of the QoE function, indicating the currently selected bitrate. Re-buffering Penalty: corresponds to the second part μ N ∑ n=1 Tn of the QoE function, where Tn denotes the re-buffering time and μ is its penalty weight coefficient. Video Smoothness Penalty: corresponds to the third part ρ N ∑ n=1 ∣q(Rn+1) −q(Rn)∣of the QoE function, denoting the amount of bitrate variation between video chunks, and ρ is its penalty weight coefficient. According to the QoE function, we know that QoE is defined as the bitrate utility minus the re-buffering penalty minus the video smoothness penalty. In short, we want the bitrate utility to be as high as possible and the re-buffering and video smoothness penalties to be as low as possible. Figure 9 demonstrates a comparison of the performance of the PLL-ABR with five other representative algorithms in terms of each factor of QoE. As can be seen in Fig. 10, PLL-ABR performs well in the re-buffering penalty and video smoothness penalty modules, with PLL-ABR reducing the re-buffering penalty by 40.59% and 25.58% and reducing the video smoothness penalty by 58.55% and 70.03%, respectively, when compared to the best performers in terms of bitrate utility, BOLA and buffer-based. This

**[Evaluación / baselines / experimentos | extracto 14 | p.15]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 10. QoE factors for different dualclip constants. TABLE II. Comparison of PLL-ABR ablation experiments. Method BU RP SP QoE elevate↑(%) PPO + LSTM 1.0786 0.3803 0.0910 52.88 - LA 1.0928 0.3774 0.0975 54.59 - Dual clip 1.0917 0.3826 0.0988 53.38 - NE-weights 1.0960 0.3697 0.1082 54.67 PLL-ABR 1.1079 0.3794 0.1055 55.45 uniformly adopted as the default setting of the double-clipping strategy in the experiments. C. Generalizability under diverse network conditions Considering the diversity of actual network environments, to verify the generalization ability of this paper’s algorithm for different physical network environments (network throughput ranges), the network dataset is further analyzed. Two typical network ranges (poor and good network) are selected for simulation experiments, and the real-time bitrate selections and corresponding buffer sizes of the PLL-ABR algorithm for the two network ranges are given separately. Robust MPC and buffer-based methods are compared, and the results are shown in Fig. 11. Example 1. The first example analyzes an application scenario with poor overall network conditions. It can be observed from Fig. 11(a) that the poorer network environment and objective network fluctuations bring more difficulties to the bitrate selection, especially reflected in robust MPC and buffer-based methods, due to the more inefficient buffer control levels of the two. The network fluctuates greatly when the timestamp is about 50 s and the buffer size drops dramatically, and the bitrate selection drops from 1.2 Mbps to nearly 0.3 Mbps, and the quality gap between before and after the video is too large, which directly affects the result of the QoE function and reduces the user experience. In contrast, by utilizing

### 4.x Limitaciones / riesgos / aplicabilidad

**[Limitaciones / riesgos / aplicabilidad | extracto 1 | p.3]**

AIP Advances ARTICLE pubs.aip.org/aip/adv adjust the bitrate of the video according to the current network conditions and device performance to ensure that the user receives the best viewing experience. In practice, traditional heuristic ABR algorithms mainly include buffer-based5,6 and rate-based algorithms based on network throughput.7 Buffer-based algorithms adjust the bitrate based on monitoring the buffer status to maximize video quality and buffer utilization, but they are not sufficiently responsive to the dynamic network environment, which may lead to QoE degradation or buffer overflow. Rate-based algorithms dynamically adjust the bitrate by predicting the network bandwidth to ensure smooth video transmission, but they ignore the state of the client’s buffer, resulting in unstable performance. The robust MPC algorithm based on control theory integrates the buffer state and the predicted bandwidth to select the best bitrate,8 which improves performance; however, it relies too much on the accuracy of the bandwidth prediction, and once the prediction is inaccurate, performance will be significantly degraded. Recently, researchers have begun to explore more efficient and intelligent ABR algorithms. Among them, the reinforcement learning (RL) technique has become a hot research topic.9 As a machine learning method that interacts with the environment to learn optimal decision policy, reinforcement learning is well suited to be applied in the field of video streaming to improve the performance and stability of ABR algorithms. Past research has focused on traditional reinforcement learning methods, mainly including Q-learning10 and actor-critic.11 For example, Lin et al.12 applied Q-learning to ABR and significantly improved the performance by constructing Q-tables and

**[Limitaciones / riesgos / aplicabilidad | extracto 2 | p.4]**

AIP Advances ARTICLE pubs.aip.org/aip/adv ●An ABR method based on deep reinforcement learning is proposed, which adopts the PPO algorithm with a dual clipping mechanism as the training framework and combines with the LSTM-LA network to capture the long shortterm and local dependencies in the data, which significantly improves the performance of the ABR algorithm. A nonlinear entropy weight dynamic adjustment mechanism is introduced, which further improves the stability and efficiency of strategy optimization by dynamically adjusting the entropy weights and balancing the exploration and utilization, ensuring the high efficiency and flexibility of strategy updating during the training process. ●Experiments have been conducted on a public experimental dataset and compared with existing ABR algorithms. The experimental results show that the method proposed in this paper exhibits significant superiority in terms of overall QoE and the performance of various QoE factors, in addition to its generalization ability in different network environments, which is significantly better than that of other existing algorithms. The rest of the paper is organized as follows. Section II describes the application background of ABR and reviews related work on ABR methods. Section III describes the system model and gives the policy update method. Section IV evaluates the performance of the PLL-ABR method through extensive experimental comparisons. Section V concludes the paper. II. BACKGROUND AND RELATED WORK A. Adaptive video streaming and DASH protocol Adaptive video streaming, as a streaming media delivery technology, can dynamically adjust the bitrate and resolution of the video according to the performance of the user’s device and the current network conditions to ensure that the user rec

**[Limitaciones / riesgos / aplicabilidad | extracto 3 | p.5]**

AIP Advances ARTICLE pubs.aip.org/aip/adv behavioral policy for an intelligent body (agent) during its interaction with the environment. In deep reinforcement learning, an intelligent body optimizes its policy by continuously observing the state of the environment, performing actions, and receiving rewards so that it can make the best decisions when it encounters similar situations in the future. This approach has led to significant breakthroughs in several fields, including network resource management,25 autonomous driving,26 and robot control.27 For example, AlphaGo applied deep reinforcement learning in the game of Go to achieve performance beyond the human level, highlighting the potential and application value of the technology. In addition, deep reinforcement learning also performs well in several network scenarios, such as Software-Defined Networking (SDN), Vehicular Ad hoc NETworks (VANETs), and Wireless Sensor Networks (WSNs),28 demonstrating its great potential in improving network performance and resource utilization efficiency. In DRL, reinforcement learning guides the learning and decision-making processes of intelligence in complex environments by defining decision frameworks and policy-updating algorithms. Deep learning, on the other hand, is used to deal with problems such as function approximation and feature extraction in reinforcement learning to better realize learning and decision-making of intelligence in complex environments. ABR systems dynamically adjust the video bitrate according to network conditions and user requirements to provide the best viewing experience and QoE. Traditional ABR algorithms are usually heuristic rule-based or model-based approaches, which often have difficulty in dealing with complex network environments and video conten

**[Limitaciones / riesgos / aplicabilidad | extracto 4 | p.6]**

AIP Advances ARTICLE pubs.aip.org/aip/adv in variable network environments. Akhtar et al.32 proposed Oboe, an auto-tuning system that pre-calculates the optimal parameters suitable for different network conditions and dynamically adjusts these parameters at runtime based on the current network conditions to automatically optimize existing ABR algorithms. However, when the actual network conditions deviate from the basic assumptions of these ABR algorithms, this approach may exhibit instability. 2. ABR methods based on machine learning To address the shortcomings of traditional heuristics, based on the research of buffer-based and throughput-based adaptive algorithms, researchers have proposed some machine learning-based improvements. Claeys et al.33 proposed an HTTP adaptive streaming client based on adaptive Q-learning, which, unlike traditional heuristics, dynamically learns the optimal behavior corresponding to the current network environment. Chiariotti et al.34 proposed a reinforcement learning-based DASH client logic, which optimally selects the best representation through the Markov Decision Process (MDP) and ensures fast and accurate convergence of the learning through a parallel learning technique. Liu et al.12 combined a k-Nearest Neighbor (KNN) algorithm with a Q-learning algorithm to propose a new KNN-Q learning algorithm for seamless switching bitrate adaptation for video streaming. Mao et al.13 performed bitrate adaptation based on reinforcement learning, using Bayesian optimization to maximize QoE, while training a linear policy to reduce the delay between the video client and the simulated environment. However, the linear approach leads to a degradation of the algorithm’s performance. All of the above-mentioned algorithms are based on Reinforcement Learn

**[Limitaciones / riesgos / aplicabilidad | extracto 5 | p.9]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 4. Comparison of the effect of PPO and PPO with dual clipping. standard PPO algorithm and the blue partly showing the effect of the improved algorithm. The logic of the PPO algorithm is shown in Algorithm 1, where the policy parameters θ0 and value function parameters ϕ0 are first initialized. k iterations are then performed. In each iteration, the algorithm runs the current policy πk in the given environment, collecting a series of trajectory data Dk. These trajectory data include states, actions, and immediate rewards fed by the environment. Next, based on the collected reward values ˆRt and the current value function Vϕk, the advantage estimate is computed as ˆAt. The algorithm then updates the policy parameters to maximize the PPO objective, which improves the performance of the policy. At the same time, the value function is fitted using mean square error regression to assess the state value more accurately. The whole process is repeated until a predetermined number of iterations is reached. D. Perception of deep neural network units LSTM-LA Traditional reinforcement learning methods have certain disadvantages relative to deep reinforcement learning in terms of feature engineering requirements, generalization capability, training speed, high-dimensional state space processing capability, and continuous action space processing capability.41 These disadvantages limit the performance and application scope of traditional reinforcement learning methods. Especially when dealing with complex and large-scale problems, to cope with this problem, we consider fusing deep neural networks to improve algorithm performance and expect to achieve better results. By observing the inputs of the neural network and comprehensively analyzin

**[Limitaciones / riesgos / aplicabilidad | extracto 6 | p.11]**

AIP Advances ARTICLE pubs.aip.org/aip/adv 2. Capturing local dependencies with local attention There may be complex correlations and dependencies between input data, and these dependencies include not only long and shortterm dependencies but may also manifest as localized dependencies. Although LSTM has a good ability to model long and short-term dependencies, it has some limitations in capturing local correlations. For this reason, this paper introduces the local attention mechanism, which focuses on the information of local regions by assigning different attention weights to different positions of the sequence through a sliding window. The local attention mechanism has the flexibility and variability to adapt to sequence inputs of different lengths and forms, which helps to mine and model local dependencies more effectively. The local attention mechanism effectively reduces computational complexity and enhances local feature extraction by narrowing the attention window and focusing only on local regions of the input sequence. Compared with the O(n2) complexity of global attention, local attention requires only O(w × n) (w is the window size), which significantly improves the computational and storage efficiency in long sequence scenarios, especially suitable for applications with high real-time requirements or memory constraints. In addition, local attention is better at capturing short-time dependencies in the data (e.g., the video stream bitrate decision depends on the characteristics of the first few video blocks) and can flexibly adapt to different needs by dynamically adjusting the window size: a small window captures the fast-changing signals, and a large window captures the long dependencies. The idea is based on the sliding window approach, which calculates th

**[Limitaciones / riesgos / aplicabilidad | extracto 7 | p.12]**

AIP Advances ARTICLE pubs.aip.org/aip/adv dynamically controls the exploration strength of the strategy so as to improve the performance and stability of the video streaming transmission system under complex network conditions. The specific realization process is as follows: Entropy computation: first, the entropy of the current strategy is computed as H. For each strategy, the entropy can be computed by the following equation: H(π) = − n ∑ i=1 π(ai∣si ) log π(ai∣si ), (17) where π(ai∣si) denotes the probability that the intelligent body chooses action ai in state si. The randomness of the current strategy can be measured by this formula. Entropy difference: Calculate the difference ΔH between the current strategy entropy H and the target entropy Htarget. The calculation process is shown in the following equation: ΔH = H −Htarget. (18) The difference reflects the deviation of the entropy of the current strategy from the expected entropy. When ΔH > 0, it indicates that the randomness of the current strategy is higher than expected, at which time the entropy weight can be reduced and the exploration behavior can be decreased; conversely, the entropy weight is increased and exploration is increased. Update of entropy weights: finally, based on this entropy difference, the entropy weights are updated by the learning rate, which is updated as shown in the following equation: λentropy = λentropy −η ⋅tanh (H −Htarget) ⋅γ ⋅T, (19) where γ is the adjustment factor, T is the current number of training rounds, and η is the learning rate. To prevent the entropy weights from becoming too small, λentropy is also boundary-protected, as shown in the following equation: λentropy = max (λentropy, λminimum). (20) Finally, the system updates the strategy parameters in real time based on th

**[Limitaciones / riesgos / aplicabilidad | extracto 8 | p.13]**

AIP Advances ARTICLE pubs.aip.org/aip/adv of RL models by guiding them to be trained in network environments where they do not perform as well as the baseline. 7. NetLLM:47 A model-based approach that efficiently adapts to multiple network tasks by pre-training models to improve performance and generalization. Experimental setup: We randomly select 80% of the samples from the dataset as the training set and the remaining 20% as the test set. In the QoE function, the penalty weight coefficients μ and ρ for re-buffering time and video smoothness are set to 4.3 and 1, respectively. For the Actor network, we pass k = 8 past state information to the network. Among them, the LSTM layer contains 128 neurons, and the fully connected layer uses 128 neurons. The outputs of these layers are then aggregated with the other inputs in the hidden layer, and the softmax function is applied to generate the corresponding action probabilities for the Actor network. The same network structure is used for the Critic network to generate the action values for the Critic network, with the network learning rate configured as 10−4, the optimizer chosen as Adam, the discount factor γ = 0.99, and the target entropy set to 0.1 to ensure that the entropy weights were not less than 0.01. All of these experiments were trained and tested using the deep learning library PyTorch, and our hyperparameters were kept constant throughout the experiments. To ensure the reproducibility of the experimental results, this paper fixes the random seed as 42 during the training process. The training and inference are conducted on a server equipped with NVIDIA GeForce RTX 3090 GPUs and AMD EPYC 7302 Central Processing Unit (CPU), and the software environment consists of Python 3.9 and PyTorch 2.5.1, and the CUDA versio

**[Limitaciones / riesgos / aplicabilidad | extracto 9 | p.14]**

AIP Advances ARTICLE pubs.aip.org/aip/adv TABLE I. Performance comparison of different algorithms. Algorithm Average bitrate (kbps) Average re-buffering time (s) Average bitrate variation (kbps) (between each block) BOLA 1137.309 0.148 254.533 MPC 1127.01 0.101 137.946 Rate-based 947.212 0.122 78.349 Buffer-based 1132.585 0.119 351.978 Pensieve 1074.237 0.093 120.108 Genet 1017.24 0.047 89.556 NetLLM 1005.48 0.041 76.334 PLL-ABR 1107.901 0.088 105.491 QoE function [Eq. (1)] decomposition (for each factor): Bitrate Utility: corresponds to the first part N ∑ n=1 q(Rn) of the QoE function, indicating the currently selected bitrate. Re-buffering Penalty: corresponds to the second part μ N ∑ n=1 Tn of the QoE function, where Tn denotes the re-buffering time and μ is its penalty weight coefficient. Video Smoothness Penalty: corresponds to the third part ρ N ∑ n=1 ∣q(Rn+1) −q(Rn)∣of the QoE function, denoting the amount of bitrate variation between video chunks, and ρ is its penalty weight coefficient. According to the QoE function, we know that QoE is defined as the bitrate utility minus the re-buffering penalty minus the video smoothness penalty. In short, we want the bitrate utility to be as high as possible and the re-buffering and video smoothness penalties to be as low as possible. Figure 9 demonstrates a comparison of the performance of the PLL-ABR with five other representative algorithms in terms of each factor of QoE. As can be seen in Fig. 10, PLL-ABR performs well in the re-buffering penalty and video smoothness penalty modules, with PLL-ABR reducing the re-buffering penalty by 40.59% and 25.58% and reducing the video smoothness penalty by 58.55% and 70.03%, respectively, when compared to the best performers in terms of bitrate utility, BOLA and buffer-based. This

**[Limitaciones / riesgos / aplicabilidad | extracto 10 | p.15]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 10. QoE factors for different dualclip constants. TABLE II. Comparison of PLL-ABR ablation experiments. Method BU RP SP QoE elevate↑(%) PPO + LSTM 1.0786 0.3803 0.0910 52.88 - LA 1.0928 0.3774 0.0975 54.59 - Dual clip 1.0917 0.3826 0.0988 53.38 - NE-weights 1.0960 0.3697 0.1082 54.67 PLL-ABR 1.1079 0.3794 0.1055 55.45 uniformly adopted as the default setting of the double-clipping strategy in the experiments. C. Generalizability under diverse network conditions Considering the diversity of actual network environments, to verify the generalization ability of this paper’s algorithm for different physical network environments (network throughput ranges), the network dataset is further analyzed. Two typical network ranges (poor and good network) are selected for simulation experiments, and the real-time bitrate selections and corresponding buffer sizes of the PLL-ABR algorithm for the two network ranges are given separately. Robust MPC and buffer-based methods are compared, and the results are shown in Fig. 11. Example 1. The first example analyzes an application scenario with poor overall network conditions. It can be observed from Fig. 11(a) that the poorer network environment and objective network fluctuations bring more difficulties to the bitrate selection, especially reflected in robust MPC and buffer-based methods, due to the more inefficient buffer control levels of the two. The network fluctuates greatly when the timestamp is about 50 s and the buffer size drops dramatically, and the bitrate selection drops from 1.2 Mbps to nearly 0.3 Mbps, and the quality gap between before and after the video is too large, which directly affects the result of the QoE function and reduces the user experience. In contrast, by utilizing

**[Limitaciones / riesgos / aplicabilidad | extracto 11 | p.16]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 11. Real-time bitrate selection and buffer occupancy analysis for each algorithm for (a) poor network environments and (b) good network environments. AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381 15, 075042-15 © Author(s) 2025 09 June 2026 09:26:24

## 5. Figuras, tablas, algoritmos y ecuaciones detectadas por texto

**[elemento detectado 1 | p.1]**

 View Online  Export Citation RESEARCH ARTICLE | JULY 25 2025 Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming Jianwei Zhang  ; Yang Han ; Zengyu Cai ; Yuan Feng ; Liang Zhu AIP Advances 15, 075042 (2025) https://doi.org/10.1063/5.0277381 Articles You May Be Interested In Semiconductor lasers driven by self-sustained chaotic electronic oscillators and applications to optical chaos cryptography Chaos (July 2012) Optimal design of energy-efficient with traffic uncertainty in wireless body area networks AIP Advances (January 2026) Speech quality estimation with deep lattice networks J. Acoust. Soc. Am. (June 2021) 09 June 2026 09:26:24

**[elemento detectado 2 | p.2]**

AIP Advances ARTICLE pubs.aip.org/aip/adv Deep reinforcement learning enhanced optimization algorithm for adaptive bitrate video streaming Cite as: AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381 Submitted: 23 April 2025 • Accepted: 7 July 2025 • Published Online: 25 July 2025 Jianwei Zhang,1,a) Yang Han,1 Zengyu Cai,2 Yuan Feng,3 and Liang Zhu2 AFFILIATIONS 1 School of Software Engineering, Zhengzhou University of Light Industry, Zhengzhou 450003, China 2School of Computer Science and Technology, Zhengzhou University of Light Industry, Zhengzhou 450003, China 3School of Electronic Information, Zhengzhou University of Light Industry, Zhengzhou 450003, China a)Author to whom correspondence should be addressed: mailzjw@163.com ABSTRACT Driven by the digital era, video traffic is growing rapidly, and users’ demand for high-quality video experiences is increasing. Adaptive bitrate (ABR) algorithms, as a key technology to optimize the transmission performance of video streams, play an important role in improving the efficiency of communication networks and the quality of experience (QoE). However, existing ABR algorithms rely too much on fixed control rules and simplified environment models, which make it difficult to provide optimal performance under complex and changing physical network environments (e.g., bandwidth fluctuations, delays, and network congestion). To address

**[elemento detectado 3 | p.3]**

AIP Advances ARTICLE pubs.aip.org/aip/adv adjust the bitrate of the video according to the current network conditions and device performance to ensure that the user receives the best viewing experience. In practice, traditional heuristic ABR algorithms mainly include buffer-based5,6 and rate-based algorithms based on network throughput.7 Buffer-based algorithms adjust the bitrate based on monitoring the buffer status to maximize video quality and buffer utilization, but they are not sufficiently responsive to the dynamic network environment, which may lead to QoE degradation or buffer overflow. Rate-based algorithms dynamically adjust the bitrate by predicting the network bandwidth to ensure smooth video transmission, but they ignore the state of the client’s buffer, resulting in unstable performance. The robust MPC algorithm based on control theory integrates the buffer state and the predicted bandwidth to select the best bitrate,8 which improves performance; however, it relies too much on the accuracy of the bandwidth prediction, and once the prediction is inaccurate, performance will be significantly degraded. Recently, researchers have begun to explore more efficient and intelligent ABR algorithms. Among them, the reinforcement learning (RL) technique has become a hot research topic.9 As a machine learning method that interacts with the environment to learn optimal decision

**[elemento detectado 4 | p.4]**

AIP Advances ARTICLE pubs.aip.org/aip/adv ●An ABR method based on deep reinforcement learning is proposed, which adopts the PPO algorithm with a dual clipping mechanism as the training framework and combines with the LSTM-LA network to capture the long shortterm and local dependencies in the data, which significantly improves the performance of the ABR algorithm. A nonlinear entropy weight dynamic adjustment mechanism is introduced, which further improves the stability and efficiency of strategy optimization by dynamically adjusting the entropy weights and balancing the exploration and utilization, ensuring the high efficiency and flexibility of strategy updating during the training process. ●Experiments have been conducted on a public experimental dataset and compared with existing ABR algorithms. The experimental results show that the method proposed in this paper exhibits significant superiority in terms of overall QoE and the performance of various QoE factors, in addition to its generalization ability in different network environments, which is significantly better than that of other existing algorithms. The rest of the paper is organized as follows. Section II describes the application background of ABR and reviews related work on ABR methods. Section III describes the system model and gives the policy update method. Section IV evaluates the performance of the PLL-ABR met

**[elemento detectado 5 | p.5]**

AIP Advances ARTICLE pubs.aip.org/aip/adv behavioral policy for an intelligent body (agent) during its interaction with the environment. In deep reinforcement learning, an intelligent body optimizes its policy by continuously observing the state of the environment, performing actions, and receiving rewards so that it can make the best decisions when it encounters similar situations in the future. This approach has led to significant breakthroughs in several fields, including network resource management,25 autonomous driving,26 and robot control.27 For example, AlphaGo applied deep reinforcement learning in the game of Go to achieve performance beyond the human level, highlighting the potential and application value of the technology. In addition, deep reinforcement learning also performs well in several network scenarios, such as Software-Defined Networking (SDN), Vehicular Ad hoc NETworks (VANETs), and Wireless Sensor Networks (WSNs),28 demonstrating its great potential in improving network performance and resource utilization efficiency. In DRL, reinforcement learning guides the learning and decision-making processes of intelligence in complex environments by defining decision frameworks and policy-updating algorithms. Deep learning, on the other hand, is used to deal with problems such as function approximation and feature extraction in reinforcement learning to better reali

**[elemento detectado 6 | p.6]**

AIP Advances ARTICLE pubs.aip.org/aip/adv in variable network environments. Akhtar et al.32 proposed Oboe, an auto-tuning system that pre-calculates the optimal parameters suitable for different network conditions and dynamically adjusts these parameters at runtime based on the current network conditions to automatically optimize existing ABR algorithms. However, when the actual network conditions deviate from the basic assumptions of these ABR algorithms, this approach may exhibit instability. 2. ABR methods based on machine learning To address the shortcomings of traditional heuristics, based on the research of buffer-based and throughput-based adaptive algorithms, researchers have proposed some machine learning-based improvements. Claeys et al.33 proposed an HTTP adaptive streaming client based on adaptive Q-learning, which, unlike traditional heuristics, dynamically learns the optimal behavior corresponding to the current network environment. Chiariotti et al.34 proposed a reinforcement learning-based DASH client logic, which optimally selects the best representation through the Markov Decision Process (MDP) and ensures fast and accurate convergence of the learning through a parallel learning technique. Liu et al.12 combined a k-Nearest Neighbor (KNN) algorithm with a Q-learning algorithm to propose a new KNN-Q learning algorithm for seamless switching bitrate adaptation fo

**[elemento detectado 7 | p.7]**

AIP Advances ARTICLE pubs.aip.org/aip/adv III. SYSTEM MODEL This section describes the design and implementation of PLL-ABR. The system model fits the actual working mechanism of ABR video streaming in the current internet. We consider a scenario where a video player downloads video files from a server over the internet and plays them back to the user. The video file is divided into consecutive segments, and the server dynamically selects the most suitable segments for transmission based on network conditions and device performance to enhance the viewing experience. During transmission, the available bandwidth fluctuates over time and is affected by network congestion, wireless fading, and other factors. The user’s viewing experience depends not only on the video quality corresponding to the bitrate of the clip but also on playback characteristics such as heavy buffering. The goal of the player is to maximize the utility associated with the viewing experience while flexibly coping with the time-varying and uncertain bandwidth. A. Description of the problem The main goal of ABR is to optimize the user’s quality of the viewing experience to ensure that the user gets the best quality and smoothness when watching video or listening to audio. The QoE function from the literature8 is defined as the reward function in this paper, which is the most commonly used QoE reward function in

**[elemento detectado 8 | p.8]**

AIP Advances ARTICLE pubs.aip.org/aip/adv video streaming bitrate, maximize the user QoE, and effectively cope with complex network environment changes, as we explain the key steps of the algorithm in detail below. Inputs: We designed six parameters as inputs to the neural network, as shown in Eq. (2). By comprehensively analyzing the characteristics of each state’s information, the input parameters are divided into two categories, one for single values and one for continuous values. First, the agent will transmit the information (state si) of each chunk i observed from the environment to the deep neural network, si = (ci, ni, li, ⃗pi, ⃗di, ⃗zi). (2) This includes single-value types: ci denotes the current buffer size, ni denotes the remaining chunks in the video, and li denotes the bitrate of downloading the previous chunk. Considering the singlevalue independent features, we designed to use a fully connected layer to map each input feature to the feature space, which is a simple structure, easy to understand and implement, and usually converges faster during the training process. For continuous value type: ⃗pi denotes the network throughput of the past video chunk download, ⃗di denotes the download time of the past video chunk, and ⃗zi denotes the next video chunk size. Considering that these inputs are characterized by continuity, we adopt LSTM and a local attention mechanis

**[elemento detectado 9 | p.9]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 4. Comparison of the effect of PPO and PPO with dual clipping. standard PPO algorithm and the blue partly showing the effect of the improved algorithm. The logic of the PPO algorithm is shown in Algorithm 1, where the policy parameters θ0 and value function parameters ϕ0 are first initialized. k iterations are then performed. In each iteration, the algorithm runs the current policy πk in the given environment, collecting a series of trajectory data Dk. These trajectory data include states, actions, and immediate rewards fed by the environment. Next, based on the collected reward values ˆRt and the current value function Vϕk, the advantage estimate is computed as ˆAt. The algorithm then updates the policy parameters to maximize the PPO objective, which improves the performance of the policy. At the same time, the value function is fitted using mean square error regression to assess the state value more accurately. The whole process is repeated until a predetermined number of iterations is reached. D. Perception of deep neural network units LSTM-LA Traditional reinforcement learning methods have certain disadvantages relative to deep reinforcement learning in terms of feature engineering requirements, generalization capability, training speed, high-dimensional state space processing capability, and continuous action space processing

**[elemento detectado 10 | p.10]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 5. LSTM-LA neural network unit. dependencies among them, we introduce the LSTM. As a neural network structure specifically designed to process sequence data, the LSTM has memory units and gating mechanisms that can effectively capture and utilize the long short-term dependencies in sequence data. LSTM is a variant of recurrent neural network (RNN) commonly used to process sequence data. Compared to regular RNNs, LSTM is more effective in processing long sequence data because it can capture and utilize long-term dependencies in sequences, avoiding the problems of gradient vanishing and gradient explosion in regular RNNs. The core idea of LSTM networks is to introduce a structure called a “memory cell,” which controls the inputs, outputs, and state updates of the memory cell through a gating mechanism. Inside the memory cell, there is a long-term state called “cell state” Ct, which is used to hold information for a long time. At each time step, the LSTM receives input xt and the hidden state ht−1 from the previous time step, then updates the state of the memory cell based on the current input and the previous hidden state. Specifically, LSTM contains three gate mechanisms: forget gate, input gate, and output gate. The network structure of LSTM is shown in Fig. 6. They are calculated as follows. FIG. 6. LSTM network structure diagram.

**[elemento detectado 11 | p.11]**

AIP Advances ARTICLE pubs.aip.org/aip/adv 2. Capturing local dependencies with local attention There may be complex correlations and dependencies between input data, and these dependencies include not only long and shortterm dependencies but may also manifest as localized dependencies. Although LSTM has a good ability to model long and short-term dependencies, it has some limitations in capturing local correlations. For this reason, this paper introduces the local attention mechanism, which focuses on the information of local regions by assigning different attention weights to different positions of the sequence through a sliding window. The local attention mechanism has the flexibility and variability to adapt to sequence inputs of different lengths and forms, which helps to mine and model local dependencies more effectively. The local attention mechanism effectively reduces computational complexity and enhances local feature extraction by narrowing the attention window and focusing only on local regions of the input sequence. Compared with the O(n2) complexity of global attention, local attention requires only O(w × n) (w is the window size), which significantly improves the computational and storage efficiency in long sequence scenarios, especially suitable for applications with high real-time requirements or memory constraints. In addition, local attention is better at capt

**[elemento detectado 12 | p.12]**

AIP Advances ARTICLE pubs.aip.org/aip/adv dynamically controls the exploration strength of the strategy so as to improve the performance and stability of the video streaming transmission system under complex network conditions. The specific realization process is as follows: Entropy computation: first, the entropy of the current strategy is computed as H. For each strategy, the entropy can be computed by the following equation: H(π) = − n ∑ i=1 π(ai∣si ) log π(ai∣si ), (17) where π(ai∣si) denotes the probability that the intelligent body chooses action ai in state si. The randomness of the current strategy can be measured by this formula. Entropy difference: Calculate the difference ΔH between the current strategy entropy H and the target entropy Htarget. The calculation process is shown in the following equation: ΔH = H −Htarget. (18) The difference reflects the deviation of the entropy of the current strategy from the expected entropy. When ΔH > 0, it indicates that the randomness of the current strategy is higher than expected, at which time the entropy weight can be reduced and the exploration behavior can be decreased; conversely, the entropy weight is increased and exploration is increased. Update of entropy weights: finally, based on this entropy difference, the entropy weights are updated by the learning rate, which is updated as shown in the following equation: λentrop

**[elemento detectado 13 | p.13]**

AIP Advances ARTICLE pubs.aip.org/aip/adv of RL models by guiding them to be trained in network environments where they do not perform as well as the baseline. 7. NetLLM:47 A model-based approach that efficiently adapts to multiple network tasks by pre-training models to improve performance and generalization. Experimental setup: We randomly select 80% of the samples from the dataset as the training set and the remaining 20% as the test set. In the QoE function, the penalty weight coefficients μ and ρ for re-buffering time and video smoothness are set to 4.3 and 1, respectively. For the Actor network, we pass k = 8 past state information to the network. Among them, the LSTM layer contains 128 neurons, and the fully connected layer uses 128 neurons. The outputs of these layers are then aggregated with the other inputs in the hidden layer, and the softmax function is applied to generate the corresponding action probabilities for the Actor network. The same network structure is used for the Critic network to generate the action values for the Critic network, with the network learning rate configured as 10−4, the optimizer chosen as Adam, the discount factor γ = 0.99, and the target entropy set to 0.1 to ensure that the entropy weights were not less than 0.01. All of these experiments were trained and tested using the deep learning library PyTorch, and our hyperparameters were kept

**[elemento detectado 14 | p.14]**

AIP Advances ARTICLE pubs.aip.org/aip/adv TABLE I. Performance comparison of different algorithms. Algorithm Average bitrate (kbps) Average re-buffering time (s) Average bitrate variation (kbps) (between each block) BOLA 1137.309 0.148 254.533 MPC 1127.01 0.101 137.946 Rate-based 947.212 0.122 78.349 Buffer-based 1132.585 0.119 351.978 Pensieve 1074.237 0.093 120.108 Genet 1017.24 0.047 89.556 NetLLM 1005.48 0.041 76.334 PLL-ABR 1107.901 0.088 105.491 QoE function [Eq. (1)] decomposition (for each factor): Bitrate Utility: corresponds to the first part N ∑ n=1 q(Rn) of the QoE function, indicating the currently selected bitrate. Re-buffering Penalty: corresponds to the second part μ N ∑ n=1 Tn of the QoE function, where Tn denotes the re-buffering time and μ is its penalty weight coefficient. Video Smoothness Penalty: corresponds to the third part ρ N ∑ n=1 ∣q(Rn+1) −q(Rn)∣of the QoE function, denoting the amount of bitrate variation between video chunks, and ρ is its penalty weight coefficient. According to the QoE function, we know that QoE is defined as the bitrate utility minus the re-buffering penalty minus the video smoothness penalty. In short, we want the bitrate utility to be as high as possible and the re-buffering and video smoothness penalties to be as low as possible. Figure 9 demonstrates a comparison of the performance of the PLL-ABR with five other representativ

**[elemento detectado 15 | p.15]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 10. QoE factors for different dualclip constants. TABLE II. Comparison of PLL-ABR ablation experiments. Method BU RP SP QoE elevate↑(%) PPO + LSTM 1.0786 0.3803 0.0910 52.88 - LA 1.0928 0.3774 0.0975 54.59 - Dual clip 1.0917 0.3826 0.0988 53.38 - NE-weights 1.0960 0.3697 0.1082 54.67 PLL-ABR 1.1079 0.3794 0.1055 55.45 uniformly adopted as the default setting of the double-clipping strategy in the experiments. C. Generalizability under diverse network conditions Considering the diversity of actual network environments, to verify the generalization ability of this paper’s algorithm for different physical network environments (network throughput ranges), the network dataset is further analyzed. Two typical network ranges (poor and good network) are selected for simulation experiments, and the real-time bitrate selections and corresponding buffer sizes of the PLL-ABR algorithm for the two network ranges are given separately. Robust MPC and buffer-based methods are compared, and the results are shown in Fig. 11. Example 1. The first example analyzes an application scenario with poor overall network conditions. It can be observed from Fig. 11(a) that the poorer network environment and objective network fluctuations bring more difficulties to the bitrate selection, especially reflected in robust MPC and buffer-based methods, due to the mo

**[elemento detectado 16 | p.16]**

AIP Advances ARTICLE pubs.aip.org/aip/adv FIG. 11. Real-time bitrate selection and buffer occupancy analysis for each algorithm for (a) poor network environments and (b) good network environments. AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381 15, 075042-15 © Author(s) 2025 09 June 2026 09:26:24

## 6. Texto crudo extraído del cuerpo principal por página

> Esta sección conserva el texto extraído página a página hasta referencias/bibliografía cuando se detecta. Se incluye para no perder detalles de método, entrenamiento, datos o evaluación. Puede tener problemas de orden de columnas o fórmulas por naturaleza del PDF.

### Página 1


View
Online 
Export
Citation
RESEARCH ARTICLE |  JULY 25 2025
Deep reinforcement learning enhanced optimization
algorithm for adaptive bitrate video streaming
Jianwei Zhang 
 ; Yang Han
 ; Zengyu Cai
 ; Yuan Feng
 ; Liang Zhu
AIP Advances 15, 075042 (2025)
https://doi.org/10.1063/5.0277381
Articles You May Be Interested In
Semiconductor lasers driven by self-sustained chaotic electronic oscillators and applications to optical
chaos cryptography
Chaos (July 2012)
Optimal design of energy-efficient with traffic uncertainty in wireless body area networks
AIP Advances (January 2026)
Speech quality estimation with deep lattice networks
J. Acoust. Soc. Am. (June 2021)
 09 June 2026 09:26:24

### Página 2

AIP Advances
ARTICLE
pubs.aip.org/aip/adv
Deep reinforcement learning enhanced
optimization algorithm for adaptive bitrate
video streaming
Cite as: AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381
Submitted: 23 April 2025 • Accepted: 7 July 2025 •
Published Online: 25 July 2025
Jianwei Zhang,1,a)
Yang Han,1
Zengyu Cai,2
Yuan Feng,3
and Liang Zhu2
AFFILIATIONS
1 School of Software Engineering, Zhengzhou University of Light Industry, Zhengzhou 450003, China
2School of Computer Science and Technology, Zhengzhou University of Light Industry, Zhengzhou 450003, China
3School of Electronic Information, Zhengzhou University of Light Industry, Zhengzhou 450003, China
a)Author to whom correspondence should be addressed: mailzjw@163.com
ABSTRACT
Driven by the digital era, video traffic is growing rapidly, and users’ demand for high-quality video experiences is increasing. Adaptive bitrate
(ABR) algorithms, as a key technology to optimize the transmission performance of video streams, play an important role in improving the
efficiency of communication networks and the quality of experience (QoE). However, existing ABR algorithms rely too much on fixed control rules and simplified environment models, which make it difficult to provide optimal performance under complex and changing physical
network environments (e.g., bandwidth fluctuations, delays, and network congestion). To address these challenges, this paper proposes a new
ABR algorithm, the deep reinforcement learning enhanced ABR video stream optimization algorithm (PLL-ABR), which adopts proximal
policy optimization as a reinforcement learning training framework and combines the dual clipping mechanism and deep neural networks
(long short-term memory and local attention mechanism) to improve the training efficiency and policy parameter optimization capability. In
addition, this paper also introduces a nonlinear entropy weight dynamic adjustment mechanism to balance exploration and utilization and
enhance the stability of strategy optimization. By training the neural network model through reinforcement learning, PLL-ABR can dynamically select the future video block bitrate based on the physical state of the client video player and network environment information. Through
comparison experiments with seven representative ABR algorithms, the method shows significant superiority under different physical network conditions and QoE factors (bitrate utilization, rebuffering penalty, and video smoothness penalty), with an average QoE improvement
of 28.50%.
© 2025 Author(s). All article content, except where otherwise noted, is licensed under a Creative Commons Attribution-NonCommercialNoDerivs 4.0 International (CC BY-NC-ND) license (https://creativecommons.org/licenses/by-nc-nd/4.0/). https://doi.org/10.1063/5.0277381
I. INTRODUCTION
With the rapid development of internet and mobile communication technologies, video streaming has become an integral part of
network applications.1 Users can watch video content anytime and
anywhere through a variety of devices, enjoying a convenient way
of entertainment and information access. Sandvine, in the “Global
Internet Phenomenon Report,”2 stated that in the global Internet
traffic, video accounted for 65% of the total traffic, and video traffic will continue to increase in the future, which also puts forward
a higher demand for high-quality video experience. However, the
popularity of video streaming also brings many challenges. During
video streaming transmission, poor or fluctuating network conditions and inappropriate bitrate selection may lead to problems such
as video lagging and picture quality degradation, which seriously
affects the user’s Quality of Experience (QoE).3 This situation not
only reduces user satisfaction but also directly affects the commercial
revenue and market competitiveness of content providers.4 Therefore, in the case of network bandwidth fluctuations and significant
differences in device performance, how to ensure that users continue
to receive a high-quality video viewing experience has become an
urgent problem to be solved.
In video streaming, Adaptive Bitrate (ABR) is an effective way
to solve these problems, and the ABR algorithm can dynamically
AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381
15, 075042-1
© Author(s) 2025
 09 June 2026 09:26:24

### Página 3

AIP Advances
ARTICLE
pubs.aip.org/aip/adv
adjust the bitrate of the video according to the current network
conditions and device performance to ensure that the user receives
the best viewing experience. In practice, traditional heuristic ABR
algorithms mainly include buffer-based5,6 and rate-based algorithms
based on network throughput.7 Buffer-based algorithms adjust the
bitrate based on monitoring the buffer status to maximize video
quality and buffer utilization, but they are not sufficiently responsive
to the dynamic network environment, which may lead to QoE degradation or buffer overflow. Rate-based algorithms dynamically adjust
the bitrate by predicting the network bandwidth to ensure smooth
video transmission, but they ignore the state of the client’s buffer,
resulting in unstable performance. The robust MPC algorithm based
on control theory integrates the buffer state and the predicted
bandwidth to select the best bitrate,8 which improves performance;
however, it relies too much on the accuracy of the bandwidth prediction, and once the prediction is inaccurate, performance will be
significantly degraded.
Recently, researchers have begun to explore more efficient
and intelligent ABR algorithms. Among them, the reinforcement
learning (RL) technique has become a hot research topic.9 As a
machine learning method that interacts with the environment to
learn optimal decision policy, reinforcement learning is well suited
to be applied in the field of video streaming to improve the performance and stability of ABR algorithms. Past research has focused
on traditional reinforcement learning methods, mainly including
Q-learning10 and actor-critic.11 For example, Lin et al.12 applied
Q-learning to ABR and significantly improved the performance by
constructing Q-tables and iteratively updating them; however, since
Q-learning consumes a large amount of spatiotemporal resources
in calculating and storing the Q-function tables, it must make a
trade-off between the spatiotemporal complexity and the QoE performance, thus limiting the efficiency. Mao et al.13 constructed a
reinforcement learning ABR approach that uses Bayesian methods14 to optimize QoE and trains a linear policy to reduce the delay
between the video client and the simulated environment; however,
the linear approach leads to a degradation of the algorithm’s performance. Later, Deep Reinforcement Learning (DRL) was proposed
to solve the ABR problem.15 DRL combines deep learning models
and reinforcement learning methods and can learn complex features and laws from large amounts of data and learn better policy
by interacting with the environment, which significantly improves
the performance and adaptability of ABR algorithms. Pensieve was
the first one to apply DRL to practical ABR and has become the
current benchmark of ABR algorithms for DRL,16 which uses the
Asynchronous Advantage Actor-Critic (A3C)17 method combined
with Deep Neural Networks (DNNs) to select the video bitrate based
on the network environment information but still suffers from the
problems of unstable training, inefficient samples, and not being able
to request the optimal bitrate. Lekharu et al.18 used LSTM to optimize the original 1DCNN structure to learn more accurate timing
features to optimize the QoE, but there is the problem of insufficient learning of the baseline function, which leads to lower training
efficiency. At present, the DRL algorithm still has a lot of room for
improvement.
Aiming at the shortcomings of current DRL algorithms in the
field in terms of sample efficiency, stability, and generalization ability, this paper proposes a deep reinforcement learning-enhanced
adaptive bitrate video stream optimization algorithm (PLL-ABR). It
is able to dynamically select the bitrate of future video blocks based
on the client video player state and network environment information and does not rely on a priori knowledge or fixed rules but
dynamically adjusts the ABR strategy based on the past decision
results. Specifically, it utilizes the policy optimization capability of
the reinforcement learning algorithm PPO (proximal policy optimization)19 to improve the training efficiency by optimizing the
sample utilization and reducing the dependence on a large amount
of training data. At the same time, to address the problem of gradient selection bias that occurs when the advantage function of the
PPO algorithm is negative (i.e., the larger the absolute value of the
gradient, the more likely it is to be selected), it adopts a dual clipping
mechanism (Dual Clipping) is optimized to ensure that the policy
update is more stable, reduce the risk of policy crash during the policy update process, and improve the convergence and stability of the
policy. In view of the complexity of the network state and other parameters, this paper combines the Long Short-Term Memory (LSTM)
network to capture the long- and short-term dependencies in the
bitrate decision and uses the Local Attention (LA) mechanism to
focus on the local dependency information in the bitrate decision by
means of a sliding window to ensure that the algorithm can make
a bitrate decision quickly and accurately even when the network
condition changes dynamically. In addition, this paper introduces
a nonlinear entropy weight dynamic adjustment mechanism, which
balances the exploration and utilization by dynamically adjusting the
entropy weights, effectively enhancing the strategy exploration and
convergence during the training process so that PLL-ABR maintains
good stability and efficiency in the process of continuous optimization. Through extensive experimental verification, PLL-ABR shows
significant superiority under different network conditions and QoE
factors (bitrate utilization, rebuffering penalty, and video smoothness penalty), with the average QoE improved by 28.50% compared
to several of the most representative algorithms currently available.
These experimental results show that the method proposed in this
paper has great potential to improve video transmission quality and
user experience.
The main contributions are summarized as follows:
●In the DRL system, we adopt the proximal policy optimization (PPO) algorithm for policy updates, which significantly
improves the performance of the ABR algorithm. Considering the problem of gradient deviation of PPO when the
advantage function is negative, this paper adopts a dual
clipping mechanism for optimization for ABR applications.
This approach effectively reduces the risk of crashing during the policy update process and further improves the
training stability and optimization performance of the ABR
algorithm.
●Considering the ABR application scenario, this paper combines the diversity of state parameters such as network
throughput and buffer to design a more suitable data
type personalized deep neural network (LSTM-LA), which
improves the feature extraction and learning ability for different types of data. By optimizing the network training
strategy, it can better fit the value function and strategy
function in DRL, thus achieving better strategy learning.
AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381
15, 075042-2
© Author(s) 2025
 09 June 2026 09:26:24

### Página 4

AIP Advances
ARTICLE
pubs.aip.org/aip/adv
●An ABR method based on deep reinforcement learning is
proposed, which adopts the PPO algorithm with a dual clipping mechanism as the training framework and combines
with the LSTM-LA network to capture the long shortterm and local dependencies in the data, which significantly
improves the performance of the ABR algorithm. A nonlinear entropy weight dynamic adjustment mechanism is
introduced, which further improves the stability and efficiency of strategy optimization by dynamically adjusting the
entropy weights and balancing the exploration and utilization, ensuring the high efficiency and flexibility of strategy
updating during the training process.
●Experiments have been conducted on a public experimental dataset and compared with existing ABR algorithms.
The experimental results show that the method proposed in
this paper exhibits significant superiority in terms of overall QoE and the performance of various QoE factors, in
addition to its generalization ability in different network
environments, which is significantly better than that of other
existing algorithms.
The rest of the paper is organized as follows. Section II describes
the application background of ABR and reviews related work on
ABR methods. Section III describes the system model and gives
the policy update method. Section IV evaluates the performance of
the PLL-ABR method through extensive experimental comparisons.
Section V concludes the paper.
II. BACKGROUND AND RELATED WORK
A. Adaptive video streaming and DASH protocol
Adaptive video streaming, as a streaming media delivery technology, can dynamically adjust the bitrate and resolution of the
video according to the performance of the user’s device and the
current network conditions to ensure that the user receives the best
viewing experience in different network environments.20 In adaptive video streaming, the video content is usually split into multiple
segments with different bitrates and stored on the server side with
different bitrates and resolutions. The player constantly monitors
network conditions, such as bandwidth and latency, and dynamically selects the bitrate of downloaded segments based on these
conditions: high bitrate segments are selected when the network
conditions are good, and low bitrate segments are selected when the
network conditions are poor. At the same time, the player maintains
a buffer to balance the impact of network fluctuations on the viewing
experience. This approach ensures smoothness and quality of video
playback, even under fluctuating network conditions.
Dynamic Adaptive Streaming over HTTP (DASH) is a protocol
that implements adaptive video streaming as the main form of video
delivery at present21 and has been widely used in various applications and video content providers such as YouTube22 and Netflix.23
It uses HTTP as the transport protocol, as shown in Fig. 1, where
the video server divides the video content media file into small segments of different qualities and resolutions and generates a Media
Presentation Description (MPD) file that describes the characteristics and availability of these segments. This file provides clients
with paths and parameters that can be used to deliver and stream
video media content, directing the client to a Content Distribution
Network (CDN).24 Utilizing the ABR algorithm, the DASH player
dynamically selects the most appropriate clips for delivery based
on the network conditions and performance of the user’s device
to provide a better viewing experience and achieve adaptive video
streaming.
B. Deep reinforcement learning applied to ABR
Deep reinforcement learning combines deep learning and
reinforcement learning to solve the problem of learning optimal
FIG. 1. DASH system optimizes video
streaming.
AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381
15, 075042-3
© Author(s) 2025
 09 June 2026 09:26:24

### Página 5

AIP Advances
ARTICLE
pubs.aip.org/aip/adv
behavioral policy for an intelligent body (agent) during its interaction with the environment. In deep reinforcement learning, an
intelligent body optimizes its policy by continuously observing the
state of the environment, performing actions, and receiving rewards
so that it can make the best decisions when it encounters similar situations in the future. This approach has led to significant
breakthroughs in several fields, including network resource management,25 autonomous driving,26 and robot control.27 For example, AlphaGo applied deep reinforcement learning in the game of
Go to achieve performance beyond the human level, highlighting
the potential and application value of the technology. In addition,
deep reinforcement learning also performs well in several network
scenarios, such as Software-Defined Networking (SDN), Vehicular Ad hoc NETworks (VANETs), and Wireless Sensor Networks
(WSNs),28 demonstrating its great potential in improving network
performance and resource utilization efficiency.
In DRL, reinforcement learning guides the learning and
decision-making processes of intelligence in complex environments
by defining decision frameworks and policy-updating algorithms.
Deep learning, on the other hand, is used to deal with problems
such as function approximation and feature extraction in reinforcement learning to better realize learning and decision-making of
intelligence in complex environments.
ABR systems dynamically adjust the video bitrate according
to network conditions and user requirements to provide the best
viewing experience and QoE. Traditional ABR algorithms are usually heuristic rule-based or model-based approaches, which often
have difficulty in dealing with complex network environments and
video content. In contrast, deep reinforcement learning can improve
the user viewing experience and QoE by learning to map from
the environment state to the optimal action, automatically discovering the relationship between complex network features and
video content, and optimizing the decisions of ABR in continuous
interaction.
The application of deep reinforcement learning in the ABR system is shown in Fig. 2, demonstrating its position and role in the
whole system architecture. Deep reinforcement learning can effectively cope with dynamically changing network environments and
video content by modeling the environment, formulating decisionmaking policy, and optimizing in real-time, thus improving the
performance and adaptability of the ABR system. This approach
not only enhances the user viewing experience but also provides
FIG. 2. Deep reinforcement learning applied to the ABR system architecture
diagram.
video content providers and platforms with more efficient means of
resource management and transmission optimization.
C. Related work
In recent years, with the rapidly growing demand for video
streaming, ABR algorithms have received extensive attention and
research in improving QoE. ABR algorithms optimize the smoothness and quality of video playback by dynamically adjusting the
bitrate of the video stream to adapt to changing network conditions and device performance. Some of the work related to the ABR
algorithm is given below.
1. ABR methods based on traditional heuristics
Earlier ABR algorithms were mainly based on the current network bandwidth estimation to select the video bitrate. Liu et al.29
proposed a rate adaptation algorithm for adaptive HTTP streams,
based on the smoothed HTTP throughput measured by the Segment Fetch Time (SFT) to detect bandwidth changes, and realized
dynamic switching of encoded content with different bitrates, so
that the impact of TCP congestion control and persistent bandwidth changes on HTTP streams can be effectively dealt with. The
PANDA algorithm applies the “probe and adapt” principle to the
design of throughput prediction and video bitrate adaptation,30
which effectively reduces the instability of video bitrate selection
and reduces the risk of buffer underruns. CS2P designed a better throughput prediction system utilizing a data-driven approach
to learning, which significantly improved the prediction accuracy
by improving the median accuracy by 40% and 50% on the initial
and midstream throughput prediction errors, respectively.31 As the
demand for user experience increases, ABR algorithms that focus
more on buffer state have emerged. Huang et al.5 propose an algorithm that monitors and optimizes the client buffer state to reduce
re-buffering events and improve video playback coherence. Spiteri
et al.6 propose an inline control algorithm for modern video players that introduces the Lyapunov optimization theory to adjust the
video bitrate by predicting and optimizing the buffer occupancy to
maximize the quality of user experience. The above-mentioned two
classes of methods have the disadvantage of incomplete considerations in making bitrate decisions; rate-based class algorithms have
advantages in instantaneous bandwidth measurement but are susceptible to transient network fluctuations, leading to unstable bitrate
selection. While buffer-based class algorithms improve the stability
of video playback by focusing on the buffer state, they have shortcomings in the initial stage and when the network conditions are
changing rapidly and may consume cache resources significantly
when the network plummets, with the risk of interrupting the video
playback. Robust MPC introduces a model prediction in control theory by combining the throughput and buffer size control method to
predict the future network bandwidth and buffer state to select the
optimal video bitrate.8 At the same time, it abandons the approach
of describing QoE as a fixed concept and defines a linear function
that can describe the user’s QoE as the optimization objective of the
algorithm. However, this method is too dependent on the predicted
throughput and is very sensitive to parameter settings, requiring
careful tuning of each parameter according to different network
conditions, making it difficult to demonstrate optimal performance
AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381
15, 075042-4
© Author(s) 2025
 09 June 2026 09:26:24

### Página 6

AIP Advances
ARTICLE
pubs.aip.org/aip/adv
in variable network environments. Akhtar et al.32 proposed Oboe,
an auto-tuning system that pre-calculates the optimal parameters
suitable for different network conditions and dynamically adjusts
these parameters at runtime based on the current network conditions to automatically optimize existing ABR algorithms. However, when the actual network conditions deviate from the basic
assumptions of these ABR algorithms, this approach may exhibit
instability.
2. ABR methods based on machine learning
To address the shortcomings of traditional heuristics, based on
the research of buffer-based and throughput-based adaptive algorithms, researchers have proposed some machine learning-based
improvements. Claeys et al.33 proposed an HTTP adaptive streaming client based on adaptive Q-learning, which, unlike traditional
heuristics, dynamically learns the optimal behavior corresponding
to the current network environment. Chiariotti et al.34 proposed a
reinforcement learning-based DASH client logic, which optimally
selects the best representation through the Markov Decision Process
(MDP) and ensures fast and accurate convergence of the learning through a parallel learning technique. Liu et al.12 combined a
k-Nearest Neighbor (KNN) algorithm with a Q-learning algorithm
to propose a new KNN-Q learning algorithm for seamless switching bitrate adaptation for video streaming. Mao et al.13 performed
bitrate adaptation based on reinforcement learning, using Bayesian
optimization to maximize QoE, while training a linear policy to
reduce the delay between the video client and the simulated environment. However, the linear approach leads to a degradation of
the algorithm’s performance. All of the above-mentioned algorithms
are based on Reinforcement Learning (RL), which optimizes QoE
performance through a data-driven approach that does not rely
on pre-designed models or environment assumptions and gradually learns the optimal bitrate adaptive policy, which significantly
outperforms traditional heuristics. However, these RL-based ABR
algorithms suffer from the dimensionality catastrophe and slow convergence, making it difficult to maintain efficient performance with
large state and action spaces.
Recently, with the development of deep learning technology
in various fields, some researchers have combined deep learning
with reinforcement learning and achieved remarkable results. For
example, Google’s DeepMind team used deep reinforcement learning technology to develop AlphaGo and became the first artificial
intelligence (AI) program to defeat the human Go world champion,35 marking a major breakthrough of AI in the field of complex
strategies. Later, some researchers proposed Deep Reinforcement
Learning (DRL)-based ABR methods, and Pensieve was the first to
propose an ABR method using DRL as the current benchmark of
DRL-based ABR methods,16 which performs ABR by training neural network models and is able to learn optimal bitrate selection
strategies by simulating different network environments and user
behaviors, with a strong adaptive capability and intelligence level.
D-DASH is an approach to ABR using deep Q-learning,36 which
evaluates different learning architectures, including feed-forward
and recurrent deep neural networks, and incorporates high-level
strategies for performance evaluation. However, this method has
shortcomings, such as unstable training and the inability to request
the optimal bitrate.
To overcome these limitations, researchers have improved
the model structure and QoE functions from different perspectives. LASH introduced a Pensieve-based augmentation network to
improve the performance by better modeling the sequence data.18
Long and Sun37 proposed a DRL-based panoramic video streaming
scheme, which redefines the QoE, including the black area ratio, and
jointly optimizes the bitrate and redundancy rate. These approaches
show superior performance in task-specific scenarios but typically
require complex model tuning and do not generalize well across
environments.
Recent efforts have turned to training strategy optimization
to improve generalization and learning efficiency. Xia et al.46 proposed a training framework based on course learning that gradually
guides RL models to learn in “difficult” network environments. This
approach improves performance by comparing the performance of
RL models and rule-based algorithms in different environments
and dynamically selecting the training environment. Vo et al.38
introduced federated learning into DRL-based ABR, which supports
cross-device training without centralized transmission of the raw
state data and significantly improves the model’s adaptability in
multiple environments. Current DRL-based ABR methods are still
deficient in sampling efficiency, stability, and generalization ability,
and there is still a lot of room for improvement. Future research will
focus on the following three aspects:
●Aiming at the shortcomings of low sample efficiency and
poor stability of deep reinforcement learning methods, more
suitable policy optimization algorithms need to be designed
to improve the efficiency and stability of the algorithms.
●For ABR application scenarios, it is necessary to design a
more suitable Deep Neural Network (DNN) structure and
optimize the network training policy to better fit the value
function and the policy function in the DRL to achieve better
policy learning.
●Network variability has an important impact on the performance of ABR algorithms, and it is necessary to solve
the problems of bandwidth fluctuation and latency variation
that may be caused by different network environments to
satisfy the user’s demand for high-quality video.
Aiming at the above-mentioned three aspects, this paper proposes a deep reinforcement learning-based ABR method, which
exploits the policy optimization capability of PPO, reduces the
dependence on a large amount of training data by optimizing sample utilization, and improves training efficiency. At the same time,
the dual clipping mechanism is used to ensure the stability of the
policy update and reduce the risk of policy collapse, which further
improves the convergence and stability of the policy. In addition,
the combination of LSTM and the local attention captures the long
short-term dependence and local dependence of the network state
and other information, respectively, which improves the strategy
learning efficiency of the optimization algorithm and effectively
improves the performance and effect of ABR. Through extensive
experimental validation, PLL-ABR shows obvious superiority under
various network conditions, including QoE factors such as bitrate
utility, re-buffering penalty, and video smoothness penalty. Compared with the current mainstream algorithms, the average QoE is
improved by 28.50%, which significantly improves the QoE of video
transmission.
AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381
15, 075042-5
© Author(s) 2025
 09 June 2026 09:26:24

### Página 7

AIP Advances
ARTICLE
pubs.aip.org/aip/adv
III. SYSTEM MODEL
This section describes the design and implementation of
PLL-ABR. The system model fits the actual working mechanism of
ABR video streaming in the current internet. We consider a scenario where a video player downloads video files from a server
over the internet and plays them back to the user. The video file
is divided into consecutive segments, and the server dynamically
selects the most suitable segments for transmission based on network conditions and device performance to enhance the viewing
experience. During transmission, the available bandwidth fluctuates
over time and is affected by network congestion, wireless fading, and
other factors. The user’s viewing experience depends not only on
the video quality corresponding to the bitrate of the clip but also
on playback characteristics such as heavy buffering. The goal of the
player is to maximize the utility associated with the viewing experience while flexibly coping with the time-varying and uncertain
bandwidth.
A. Description of the problem
The main goal of ABR is to optimize the user’s quality of the
viewing experience to ensure that the user gets the best quality and
smoothness when watching video or listening to audio.
The QoE function from the literature8 is defined as the reward
function in this paper, which is the most commonly used QoE
reward function in the field of ABR, which can effectively reflect
the user’s perception and expectation of service quality and facilitate
experimental comparison with other ABR algorithms. The specific
formula is shown in the following equation:
QoE =
N
∑
n=1
q(Rn) −μ
N
∑
n=1
Tn −ρ
N
∑
n=1
∣q(Rn+1) −q(Rn)∣.
(1)
The QoE factor consists of the following three components: the
first one is the video quality: q(Rn) denotes the n-th bitrate mapping to the user-perceived quality; the second one is the re-buffering
time: Tn denotes the re-buffering time incurred when selecting the
bitrate Rn to download the video chunks; and the third one is the
video smoothness: ∣q(Rn+1) −q(Rn)∣denotes the difference in the
bitrate between the two chunks in terms of the perceived change in
video quality. Here, μ and ρ denote the penalty weight coefficients
for re-buffering time and video smoothness, respectively.
B. Design of PLL-ABR algorithm
PLL-ABR is a learning method in which the agent interacts with
the environment to maximize cumulative rewards. It first needs to
interact with the video streaming environment to obtain the current
network state and video playback information, such as bandwidth
and delay. Then, a policy network is used to select the optimal bitrate
based on this state information. To describe our algorithm, we draw
the algorithm framework diagram, as shown in Fig. 3. The PLL-ABR
method uses PPO as a reinforcement learning framework and at the
same time integrates deep neural networks for optimizing the ABR
algorithm. Among them, the policy network, often called the Actor
network, is responsible for outputting the probability distribution
of actions based on the current environment state, while the value
network, referred to as the Critic network, evaluates the value of the
state and helps the Actor network better select actions.
The overall implementation process of the algorithm is as follows: input the environment state parameter si and initialize the
parameters of the policy network and the value network. For each
training round, the environment state and player environment state
are initialized first. When the round is not finished, the algorithm
obtains the current network state and video playback information
from the player environment and merges them with the environment state s. Subsequently, the policy network Actor selects the
optimal bitrate action ai based on the current state, calculates the
probability distribution π(ai, si) and state value v = V(si) for each
action, and then executes the action and observes the reward R and
the new state s′
i. Next, the player’s environment state is updated, and
empirical data are recorded. Using this experience data, the algorithm computes the advantage function A(si, ai) for each experience
and updates the parameters of the policy network and the value
network. This process is repeated until all training rounds are completed. The optimization policy can adaptively select the optimal
FIG. 3. PLL-ABR algorithmic framework.
AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381
15, 075042-6
© Author(s) 2025
 09 June 2026 09:26:24

### Página 8

AIP Advances
ARTICLE
pubs.aip.org/aip/adv
video streaming bitrate, maximize the user QoE, and effectively cope
with complex network environment changes, as we explain the key
steps of the algorithm in detail below.
Inputs: We designed six parameters as inputs to the neural
network, as shown in Eq. (2). By comprehensively analyzing the
characteristics of each state’s information, the input parameters are
divided into two categories, one for single values and one for continuous values. First, the agent will transmit the information (state si)
of each chunk i observed from the environment to the deep neural
network,
si = (ci, ni, li, ⃗pi, ⃗di, ⃗zi).
(2)
This includes single-value types: ci denotes the current buffer
size, ni denotes the remaining chunks in the video, and li denotes the
bitrate of downloading the previous chunk. Considering the singlevalue independent features, we designed to use a fully connected
layer to map each input feature to the feature space, which is a simple
structure, easy to understand and implement, and usually converges
faster during the training process.
For continuous value type: ⃗pi denotes the network throughput
of the past video chunk download, ⃗di denotes the download time
of the past video chunk, and ⃗zi denotes the next video chunk size.
Considering that these inputs are characterized by continuity, we
adopt LSTM and a local attention mechanism to design the model.
This structure can capture long short-term dependencies in the data
while capturing local dependencies more effectively, thus improving
the model’s ability to understand and utilize the information of the
network environment.
Policy update: Based on the observation of the input environmental state si, the agent updates the parameters of the policy
network using the PPO method.
Policy: In the PLL-ABR system, after receiving the state information si, the agent will make the corresponding action ai according
to the defined policy π : π(si, ai) →[0, 1], where the policy π is the
probability of the action ai that may be taken under the state si. Considering the diversity of the parameters of (si, ai), the designed deep
neural network can help to adjust and optimize the parameters of
the policy; we denote it as θ, i.e., πθ(si, ai).
Training: Our policy optimization method is based on the
results of policy evaluation (the probability π or value v of choosing
different actions ai in different states si), and the PPO algorithm is
used to update the parameters of the policy network so that the policy can obtain higher rewards in future environment interactions.
We describe the policy optimization method in detail in Sec. III C,
where the optimization method conforms to Eq. (3).
Reward: The main goal of the agent is to optimize the cumulative reward (QoE). After the agent observes the state si from
the environment and makes the corresponding action ai, the environment will return to the agent the reward value. The reward
value formula conforms to Eq. (1), which means that the weighted
value of the three parts—video quality, re-buffering time, and video
smoothness—is optimal.
Output: The output of the policy network (Actor) is a vector, where each element represents the probability πθ of selecting
the corresponding action (bitrate selected by the video chunk). After
obtaining the output of the policy network, the system will select a
specific action (bitrate) based on the probability distribution of the
output and apply it to the video playback process. The output of the
value network (Critic) is an estimate vϕ of the value of the action
in the current state, i.e., the expected reward for taking a certain
action given the current state. This value estimation helps the policy
network (Actor) to better select actions to maximize the long-term
cumulative reward.
C. Policy update methodology
Proximal Policy Optimization (PPO) is a policy optimization
algorithm for solving reinforcement learning problems, aiming to
cope with the problems of low sample utilization and unstable training in traditional policy gradient methods. PPO is based on the
actor-critic architecture, which ensures the stability and efficiency
of training by controlling the magnitude of the policy update during the training process and the objective function of the policy
update with appropriate clipping to ensure the stability and efficiency of training. This method improves the training efficiency
while ensuring its convergence and effectively solves the problems of
low sample utilization and unstable training in the traditional policy
gradient method. Compared with traditional reinforcement learning algorithms such as Q-learning and SARSA,39 the PPO algorithm
significantly improves the stability and efficiency of the training
process.
The PPO update policy is shown in the following equation:
θk+1 = arg max
θ
E
s,a∼πθk
[L(s, a, θk, θ)].
(3)
The gradient ascent method is used to maximize the objective,
where L is defined as shown in the following equation:
L(s, a, θk, θ) = min (r(θ) ˆA, clip(r(θ), 1 −ε, 1 + ε) ˆA),
(4)
where πθ denotes the policy with parameter θ, r(θ) is the correction
factor, as shown in Eq. (5), ˆA is the advantage function Aπθk (s, a),
θ is the parameter of the policy at iteration k, and ε is a small
hyperparameter,
r(θ) = πθ(a∣s)
πθk(a∣s).
(5)
The traditional PPO algorithm, in order to limit the update step
size, sets an “upper limit,” over which the algorithm will be clipped.
However, when the advantage function A is negative, this clipping
strategy may lead to the situation that the larger the absolute value
of the gradient, the more the gradient will be selected, which violates
the original intention of limiting the gradient update amplitude and
leads to unstable training or performance degradation. In order to
solve this problem, in this paper, for the ABR, a dual clipping mechanism40 is used to improve the PPO for better learning of the ABR
algorithm, whose L is defined as shown in the following equation:
L(s, a, θk, θ) = max (min (r(θ) ˆA, clip(r(θ), 1 −ε, 1 + ε) ˆA), c ˆA). (6)
It does another negative lower limit clipping on top of the
original clipping, which effectively solves the problem when the
advantage function is negative and further improves the stability and
performance of the training through the dual clipping mechanism,
where c > 1 is used to limit the lower limit of the clipping, as shown
in Fig. 4, with the black line segment partly showing the effect of the
AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381
15, 075042-7
© Author(s) 2025
 09 June 2026 09:26:24

### Página 9

AIP Advances
ARTICLE
pubs.aip.org/aip/adv
FIG. 4. Comparison of the effect of PPO and PPO with dual clipping.
standard PPO algorithm and the blue partly showing the effect of the
improved algorithm.
The logic of the PPO algorithm is shown in Algorithm 1, where
the policy parameters θ0 and value function parameters ϕ0 are first
initialized. k iterations are then performed. In each iteration, the
algorithm runs the current policy πk in the given environment, collecting a series of trajectory data Dk. These trajectory data include
states, actions, and immediate rewards fed by the environment.
Next, based on the collected reward values ˆRt and the current value
function Vϕk, the advantage estimate is computed as ˆAt. The algorithm then updates the policy parameters to maximize the PPO
objective, which improves the performance of the policy. At the
same time, the value function is fitted using mean square error
regression to assess the state value more accurately. The whole
process is repeated until a predetermined number of iterations is
reached.
D. Perception of deep neural network units LSTM-LA
Traditional reinforcement learning methods have certain disadvantages relative to deep reinforcement learning in terms of
feature engineering requirements, generalization capability, training
speed, high-dimensional state space processing capability, and continuous action space processing capability.41 These disadvantages
limit the performance and application scope of traditional reinforcement learning methods. Especially when dealing with complex and
large-scale problems, to cope with this problem, we consider fusing
deep neural networks to improve algorithm performance and expect
to achieve better results.
By observing the inputs of the neural network and comprehensively analyzing their respective properties, we use a more complex
deep neural network for the continuous values (⃗pi, ⃗di, ⃗zi), which are
input parameters with sequential properties and contain historical
information about the download of consecutive chunks of video in
the video streaming system. To better capture the relationships and
dependencies between their data points, we design to use a combination of the LSTM and the local attention mechanism; the LSTM-LA
unit is shown in Fig. 5.
1. Capturing long short-term dependencies
with LSTM
Considering that past network throughput, download time, and
next video chunk size have an impact on current and future video
chunk downloads, and that there may be complex long short-term
ALGORITHM 1. PPO algorithm with double clipping applied to ABR.
Input: initial policy parameters θ0; initial value function parameters ϕ0;
the set of iteration indices K = {0, 1, . . . , n}, where k ∈K denotes
the current iteration step; the trajectory data Dk = {sk, ak, πk, vk, rk}
include states, action, action probability, value function estimation,
and immediate reward resulting from interaction with the environment.
Output: optimized policy parameters θ∗; optimized value function
Parameters ϕ∗; records of rewards and losses during training
and updated policies πθ
∗.
1
foreach k ∈K do
2
Collect the set of trajectories Dk by running policy
πk = π(θk) in the environment.
3
Calculate the value of collected rewards ˆR.
4
Calculate the advantage estimate ˆA based
on the current value function Vϕk.
5
Update the policy by maximizing the objective:
6
θk+1 = arg max
θ
1
∣Dk∣T ∑
τ ∈Dk
T
∑
t=0
max (min (rt(θ) ˆAt, clip(rt(θ), 1 −ε, 1 + ε) ˆAt), c ˆAt)
7
Fitting the value function by regression on mean-square error:
8
ϕk+1 = arg min
ϕ
1
∣Dk∣T ∑
τ ∈Dk
T
∑
t=0
(Vϕ(st) −ˆR t)2
9
end for
AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381
15, 075042-8
© Author(s) 2025
 09 June 2026 09:26:24

### Página 10

AIP Advances
ARTICLE
pubs.aip.org/aip/adv
FIG. 5. LSTM-LA neural network unit.
dependencies among them, we introduce the LSTM. As a neural network structure specifically designed to process sequence data, the
LSTM has memory units and gating mechanisms that can effectively
capture and utilize the long short-term dependencies in sequence
data.
LSTM is a variant of recurrent neural network (RNN) commonly used to process sequence data. Compared to regular RNNs,
LSTM is more effective in processing long sequence data because it
can capture and utilize long-term dependencies in sequences, avoiding the problems of gradient vanishing and gradient explosion in
regular RNNs.
The core idea of LSTM networks is to introduce a structure
called a “memory cell,” which controls the inputs, outputs, and state
updates of the memory cell through a gating mechanism. Inside the
memory cell, there is a long-term state called “cell state” Ct, which
is used to hold information for a long time. At each time step, the
LSTM receives input xt and the hidden state ht−1 from the previous
time step, then updates the state of the memory cell based on the
current input and the previous hidden state.
Specifically, LSTM contains three gate mechanisms: forget gate,
input gate, and output gate. The network structure of LSTM is
shown in Fig. 6. They are calculated as follows.
FIG. 6. LSTM network structure diagram.
Forget gate: determines how much of a previous memory state
is retained in the current time step. Its calculation formula is shown
in the following equation:
ft = σ(Wf ⋅[ht−1, xt] + bf ),
(7)
where σ is the sigmoid function, W f is the weight matrix of the
forget gate, and b f is the bias.
Input gate: decide how much new information to update to
the memory cell. Its calculation formula is shown in the following
equation:
it = σ(Wi ⋅[ht−1, xt] + bi).
(8)
The calculation process for updating the memory cell is shown
in the following equation:
˜Ct = tanh (WC ⋅[ht−1, xt] + bC).
(9)
Output gate: Determines how much information is output from
the memory cell to the hidden state. The formula for this is shown
in the following equation:
ot = σ(Wo ⋅[ht−1, xt] + bo).
(10)
The final hidden state ht and the state Ct of the memory cell are
calculated by the following equations:
ht = ot ⊙tan h(Ct),
(11)
Ct = ft ⊙Ct−1 + it ⊙˜Ct,
(12)
where ⊙denotes element-by-element multiplication. These gating
mechanisms allow the LSTM to selectively forget past information,
accept new information and update the state, and maintain important information in the sequence for a long period of time, thus
effectively handling long short-term dependencies.
AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381
15, 075042-9
© Author(s) 2025
 09 June 2026 09:26:24

### Página 11

AIP Advances
ARTICLE
pubs.aip.org/aip/adv
2. Capturing local dependencies with local attention
There may be complex correlations and dependencies between
input data, and these dependencies include not only long and shortterm dependencies but may also manifest as localized dependencies.
Although LSTM has a good ability to model long and short-term
dependencies, it has some limitations in capturing local correlations. For this reason, this paper introduces the local attention
mechanism, which focuses on the information of local regions by
assigning different attention weights to different positions of the
sequence through a sliding window. The local attention mechanism
has the flexibility and variability to adapt to sequence inputs of
different lengths and forms, which helps to mine and model local
dependencies more effectively.
The local attention mechanism effectively reduces computational complexity and enhances local feature extraction by narrowing the attention window and focusing only on local regions of
the input sequence. Compared with the O(n2) complexity of global
attention, local attention requires only O(w × n) (w is the window
size), which significantly improves the computational and storage
efficiency in long sequence scenarios, especially suitable for applications with high real-time requirements or memory constraints.
In addition, local attention is better at capturing short-time dependencies in the data (e.g., the video stream bitrate decision depends
on the characteristics of the first few video blocks) and can flexibly
adapt to different needs by dynamically adjusting the window size:
a small window captures the fast-changing signals, and a large window captures the long dependencies. The idea is based on the sliding
window approach, which calculates the role relationships between
local window elements only at position i. The model learns these
local dependencies and uses this information to calculate the weight
of each element and subsequently performs a weighted summation
of the elements within the window to finally obtain a representation of the entire sequence. The use of a local attention mechanism
can effectively capture the local features of the sequence and can
effectively reduce the computational complexity.
Given a sequence x = (x1, x2, . . . , xn), the local attention mechanism differs from global attention in that only the relationship
between that position and other positions within its local window is
computed, rather than the relative relationship to all positions in the
global sequence, and the local attention mechanism is formulated as
follows.
The inputs are mapped into queries, keys, and values by linear
transformations as shown in the following equation:
Q = XWq, K = XWk, V = XWv,
(13)
where Wq, Wk, Wv are the learnable weight matrices, and Q, K, V are
the query, key, and value representations, respectively.
For each position i, its attentional weight with respect to position j within the local window is calculated and softmax normalized
as shown in the following equation:
LocalAttentionij = softmax(QiKT
j
√
dk
),
(14)
where Qi is the query vector for position i, Ki is the key vector for
position j, and dk is the dimension of the key vector.
The definition of a localized window is shown in the following
equation:
windowi = [max (0, i −w
2 ), . . . , min (n, i + w
2 )],
(15)
where w is the size of the local window and n is the length of the
sequence.
The context vector for position i is obtained by weighted
summation as shown in the following equation:
contexti =
∑
j ∈windowi
LocalAttentionijVj,
(16)
where Vj is the value vector for position j. The output for each
position is a weighted summation based on that position and the
positions within its localized window.
Output representation: finally, the weighted representation
obtained from the weighted summation is used as an output
representation for subsequent tasks.
By effectively integrating these two information capturing
mechanisms, the model’s ability to process sequences can be
improved. LSTM uses the gating mechanism to effectively capture
long and short-term dependencies in long sequences, but due to the
attenuation of the information transfer when LSTM performs long
sequence processing, it can result in insufficient sensitivity to information for the model training. The localized attention mechanism,
on the other hand, allows the model to have adapted attention in the
local region of the sequence, that is, to allocate attention dynamically
in the local region and is not limited to the neighboring positions
of the current node, so as to effectively capture the information in
that local region. By combining the two, the memory mechanism of
LSTM can be used to deal with the long- and short-term dependencies between sequences, and the sliding window of local attention
can be used to flexibly adapt and weigh the information at different locations in the sequence, which can ensure the efficient transfer
of information to long sequences while also taking into account the
effective capture of local information. As a result, this combination
strategy can better adapt to sequence data of different lengths and
forms and shows more powerful performance in various sequence
tasks for bitrate adaptive tasks.
E. Dynamic adjustment mechanism for nonlinear
entropy weights
Entropy regularization is an important technique used in
reinforcement learning to balance exploration and exploitation by
introducing entropy terms in strategy optimization to enhance
the exploration of strategies and prevent falling into local optima.
Higher entropy values help explore new strategies, while lower
entropy values promote stable decision-making based on experience. However, traditional reinforcement learning methods usually
use fixed entropy weights, which are difficult to adapt to dynamic
network environments such as bandwidth fluctuations and delay
jitter and easily lead to unstable strategies or performance degradation. For this reason, this paper introduces a nonlinear entropy
weight dynamic adjustment mechanism, which adaptively adjusts
the entropy weight according to the real-time network state and
AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381
15, 075042-10
© Author(s) 2025
 09 June 2026 09:26:24

### Página 12

AIP Advances
ARTICLE
pubs.aip.org/aip/adv
dynamically controls the exploration strength of the strategy so as to
improve the performance and stability of the video streaming transmission system under complex network conditions. The specific
realization process is as follows:
Entropy computation: first, the entropy of the current strategy
is computed as H. For each strategy, the entropy can be computed
by the following equation:
H(π) = −
n
∑
i=1
π(ai∣si ) log π(ai∣si ),
(17)
where π(ai∣si) denotes the probability that the intelligent body
chooses action ai in state si. The randomness of the current strategy
can be measured by this formula.
Entropy difference: Calculate the difference ΔH between the
current strategy entropy H and the target entropy Htarget. The
calculation process is shown in the following equation:
ΔH = H −Htarget.
(18)
The difference reflects the deviation of the entropy of the current strategy from the expected entropy. When ΔH > 0, it indicates
that the randomness of the current strategy is higher than expected,
at which time the entropy weight can be reduced and the exploration behavior can be decreased; conversely, the entropy weight is
increased and exploration is increased.
Update of entropy weights: finally, based on this entropy difference, the entropy weights are updated by the learning rate, which is
updated as shown in the following equation:
λentropy = λentropy −η ⋅tanh (H −Htarget) ⋅γ ⋅T,
(19)
where γ is the adjustment factor, T is the current number of training
rounds, and η is the learning rate. To prevent the entropy weights
from becoming too small, λentropy is also boundary-protected, as
shown in the following equation:
λentropy = max (λentropy, λminimum).
(20)
Finally, the system updates the strategy parameters in real
time based on the optimization results and adjusts the exploration
effort according to the network state changes to balance the exploration and exploitation. It should be emphasized that increasing
the explorability does not mean directly choosing a higher bitrate,
but rather it means preventing the system from converging to a
certain fixed strategy too early in an uncertain environment, such
as choosing a low bitrate or a certain fixed network behavior too
early. Therefore, the increase in entropy is intended to help the
system discover more appropriate coping strategies by enhancing
explorability.
IV. EXPERIMENTAL EVALUATION
In this section, we describe the experimental setup, dataset
selection, and experimental results. The experiments are divided
into three parts: first, the overall performance of the PLL-ABR algorithm is evaluated and compared with seven representative ABR
algorithms; second, the QoE function is disassembled to analyze
the algorithm’s performance on three factors, namely, bitrate utility, re-buffering penalty, and video smoothness penalty; and finally,
the algorithm is tested for its performance and generalization ability under different network conditions (including poor and good
network environments).
A. Experimental dataset
To ensure that ABR policies under real network conditions
are specified, our experimental data are divided into two parts: the
network trajectory dataset and the video sources.
Network trajectory datasets contain two broadband datasets,
Federal Communications Commission (FCC)42 and High Speed
Downlink Packages Access (HSDPA),43 which are derived from
data generated by users while watching videos on mobile devices in
scenarios such as trains, buses, and trolleys, etc. The FCC dataset
is maintained by the U.S. Federal Communications Commission
(FCC), which covers information related to various broadband
Internet Service Providers (ISPs) in the U.S. It contains more than 1
× 106 network throughput data at 5-s granularity, from which 1000
traces were selected. The HSDPA dataset is bandwidth tracking data
collected in Norway, which provides real-world measurements at 1s granularity over 30 min, and traces with the same specifications
as those of the FCC dataset were selected. Meanwhile, the average
throughput in the dataset is limited to a range of 0.2 to 6 Mbps in
order to optimize the ABR model and avoid falling into a situation
where the maximum bitrate is always selected.
Video sources: as a benchmark video for evaluating the ABR
strategy, we chose the reference video “/EnvivioDash3” from the
DASH player.44 This video uses the H.264/MPEG-4 codec and is
encoded at six different bitrates {300, 750, 1200, 1850, 2850, 4300}
kbps. The video contains a total of 48 video chunks, each of which is
∼4 s long.
B. Comparative analysis of QoE experimental results
After configuring the network trajectory dataset and the video
dataset, we experimentally evaluated the designed PLL-ABR algorithm and compared it with the following seven most representative
ABR algorithms under the same conditions:
1.
Buffer-based:5 A buffer-based approach that optimizes video
transmission by monitoring the client’s buffer.
2.
Rate-based:7 A network throughput-based approach that
dynamically adjusts the bitrate of the video stream based on
the predicted network throughput.
3.
Robust MPC:8 A model predictive control-based optimization
method for video streaming transmission combines network
state and buffer filling to optimize video transmission.
4.
Buffer Occupancy based Lyapunov Algorithm (BOLA):6 A
buffer-based algorithm for ABR selection, designed using Lyapunov optimization, is the default ABR algorithm for the
dash.js45 player.
5.
Pensieve:16 An A3C-based video streaming delivery optimization method that dynamically adjusts the bitrate and quality
of videos by learning the user’s viewing behavior and network
conditions.
6.
Genet:46 A training framework based on course learning
that improves the generalization ability and performance
AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381
15, 075042-11
© Author(s) 2025
 09 June 2026 09:26:24

### Página 13

AIP Advances
ARTICLE
pubs.aip.org/aip/adv
of RL models by guiding them to be trained in network
environments where they do not perform as well as the
baseline.
7.
NetLLM:47 A model-based approach that efficiently adapts
to multiple network tasks by pre-training models to improve
performance and generalization.
Experimental setup: We randomly select 80% of the samples
from the dataset as the training set and the remaining 20% as the test
set. In the QoE function, the penalty weight coefficients μ and ρ for
re-buffering time and video smoothness are set to 4.3 and 1, respectively. For the Actor network, we pass k = 8 past state information
to the network. Among them, the LSTM layer contains 128 neurons,
and the fully connected layer uses 128 neurons. The outputs of these
layers are then aggregated with the other inputs in the hidden layer,
and the softmax function is applied to generate the corresponding
action probabilities for the Actor network. The same network structure is used for the Critic network to generate the action values for
the Critic network, with the network learning rate configured as
10−4, the optimizer chosen as Adam, the discount factor γ = 0.99, and
the target entropy set to 0.1 to ensure that the entropy weights were
not less than 0.01. All of these experiments were trained and tested
using the deep learning library PyTorch, and our hyperparameters
were kept constant throughout the experiments.
To ensure the reproducibility of the experimental results, this
paper fixes the random seed as 42 during the training process. The
training and inference are conducted on a server equipped with
NVIDIA GeForce RTX 3090 GPUs and AMD EPYC 7302 Central
Processing Unit (CPU), and the software environment consists of
Python 3.9 and PyTorch 2.5.1, and the CUDA version is 12.4. The
training process uses 16 parallel environments for sampling, and a
single training cycle takes about 600 ms. The model was saved every
300 training cycles to maintain training stability.
1. Overall QoE performance comparison
We plotted the comparison of the average QoE values of
the eight ABR algorithms to better demonstrate the experimental
results. As shown in Fig. 7, the performance of PLL-ABR designed
by us under the same conditions outperforms the other seven most
FIG. 7. Average QoE values of PLL-ABR vs existing ABR algorithms.
FIG. 8. Comparison of average QoE value CDF of PLL-ABR with existing ABR
algorithms.
representative ABR algorithms at present, and compared with these
algorithms, the average QoE of PLL-ABR is improved by 28.50%
overall, and Fig. 8 shows the algorithm’s average on each network
trajectory in a Cumulative Distribution Function (CDF) distribution of QoE. Combining the two comparison graphs, we find that
PLL-ABR not only excels in overall performance but also significantly outperforms other ABR algorithms in generalization ability
over multiple network trajectories.
The reason for this significant difference is that most of the
existing algorithms use fixed control policies and lack the ability to adapt dynamically to fluctuations in network conditions.
Although Pensieve is also based on the RL approach, compared with
PLL-ABR, the design of the optimization algorithm lacks pertinence
and is difficult to handle environmental changes and sample deviations stably. In contrast, PLL-ABR integrates multiple dynamic
variables such as buffer states and network conditions and utilizes
a more efficient PPO optimization algorithm and the learning capability of deep neural networks (LSTM-LA), combined with real-time
user QoE feedback for dynamic optimization.
Therefore, in the experimental comparison, the PLL-ABR algorithm shows significant advantages in terms of average QoE, generalization performance, and stability, and has higher dynamic
optimization capability, which is suitable for video transmission
optimization scenarios under various network conditions.
2. QoE performance comparison by factors
In comparative experiments of ABR algorithms, the core of our
concern is often the overall effect of QoE (Quality of Experience),
which has been compared in previous analyses. After disassembling
and analyzing the QoE function [Eq. (1)] and conducting several
comparison experiments, we found that analyzing the components
of the QoE function (performance of each factor) separately helps to
better understand the performance of the algorithms. Table I shows
the performance comparison of different algorithms.
AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381
15, 075042-12
© Author(s) 2025
 09 June 2026 09:26:24

### Página 14

AIP Advances
ARTICLE
pubs.aip.org/aip/adv
TABLE I. Performance comparison of different algorithms.
Algorithm
Average
bitrate
(kbps)
Average
re-buffering
time (s)
Average bitrate
variation (kbps)
(between
each block)
BOLA
1137.309
0.148
254.533
MPC
1127.01
0.101
137.946
Rate-based
947.212
0.122
78.349
Buffer-based
1132.585
0.119
351.978
Pensieve
1074.237
0.093
120.108
Genet
1017.24
0.047
89.556
NetLLM
1005.48
0.041
76.334
PLL-ABR
1107.901
0.088
105.491
QoE function [Eq. (1)] decomposition (for each factor):
Bitrate Utility: corresponds to the first part
N
∑
n=1
q(Rn) of the
QoE function, indicating the currently selected bitrate.
Re-buffering Penalty: corresponds to the second part μ
N
∑
n=1
Tn
of the QoE function, where Tn denotes the re-buffering time and
μ is its penalty weight coefficient.
Video Smoothness Penalty: corresponds to the third part
ρ
N
∑
n=1
∣q(Rn+1) −q(Rn)∣of the QoE function, denoting the amount
of bitrate variation between video chunks, and ρ is its penalty weight
coefficient.
According to the QoE function, we know that QoE is defined
as the bitrate utility minus the re-buffering penalty minus the video
smoothness penalty. In short, we want the bitrate utility to be as high
as possible and the re-buffering and video smoothness penalties to
be as low as possible. Figure 9 demonstrates a comparison of the
performance of the PLL-ABR with five other representative algorithms in terms of each factor of QoE.
As can be seen in Fig. 10, PLL-ABR performs well in the
re-buffering penalty and video smoothness penalty modules, with
PLL-ABR reducing the re-buffering penalty by 40.59% and 25.58%
and reducing the video smoothness penalty by 58.55% and 70.03%,
respectively, when compared to the best performers in terms of
bitrate utility, BOLA and buffer-based. This clear performance
advantage demonstrates the excellence of PLL-ABR in balancing the
comprehensive performance of the three key factors to achieve the
most optimal QoE. This comprehensive performance optimization
helps to avoid over-optimizing the performance of a single factor
at the expense of the others, which in turn ensures the stability and
robustness of the algorithm.
To thoroughly assess the contribution of each enhancement
component in the PLL-ABR architecture, we conducted a full ablation study. As shown in Table II, we evaluated the performance of
the model by disabling each individual component (dual clipping,
local attention, and nonlinear entropy weights) while keeping the
others active. Furthermore, we added a baseline version that disables
all enhancements (i.e., PPO + LSTM).
The results show that each component contributes positively to
the overall QoE, with the full PLL-ABR model performing the best.
It is worth noting that removing either the dual clipping or localized attention mechanisms leads to a more substantial performance
degradation, suggesting that they have a greater impact.
Meanwhile, in order to evaluate the effect of the dual-clip constant c on the model performance, this paper designs sensitivity
experiments by setting c = 2,3,4 and training and testing the model
under the same training configuration. Figure 10 illustrates the performance of each evaluation factor of QoE under different c values.
The experimental results show that when c = 3, the model exhibits
a more balanced performance on each factor, indicating that the
parameter realizes a good trade-off between the policy update constraint and the learning efficiency. Therefore, in this paper, c = 3 is
FIG. 9. QoE performance comparison by
factors.
AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381
15, 075042-13
© Author(s) 2025
 09 June 2026 09:26:24

### Página 15

AIP Advances
ARTICLE
pubs.aip.org/aip/adv
FIG. 10. QoE factors for different dualclip constants.
TABLE II. Comparison of PLL-ABR ablation experiments.
Method
BU
RP
SP
QoE elevate↑(%)
PPO + LSTM
1.0786
0.3803
0.0910
52.88
- LA
1.0928
0.3774
0.0975
54.59
- Dual clip
1.0917
0.3826
0.0988
53.38
- NE-weights
1.0960
0.3697
0.1082
54.67
PLL-ABR
1.1079
0.3794
0.1055
55.45
uniformly adopted as the default setting of the double-clipping
strategy in the experiments.
C. Generalizability under diverse network conditions
Considering the diversity of actual network environments, to
verify the generalization ability of this paper’s algorithm for different physical network environments (network throughput ranges),
the network dataset is further analyzed. Two typical network ranges
(poor and good network) are selected for simulation experiments,
and the real-time bitrate selections and corresponding buffer sizes
of the PLL-ABR algorithm for the two network ranges are given separately. Robust MPC and buffer-based methods are compared, and
the results are shown in Fig. 11.
Example 1. The first example analyzes an application scenario
with poor overall network conditions. It can be observed from
Fig. 11(a) that the poorer network environment and objective network fluctuations bring more difficulties to the bitrate selection,
especially reflected in robust MPC and buffer-based methods, due
to the more inefficient buffer control levels of the two. The network fluctuates greatly when the timestamp is about 50 s and the
buffer size drops dramatically, and the bitrate selection drops from
1.2 Mbps to nearly 0.3 Mbps, and the quality gap between before
and after the video is too large, which directly affects the result of
the QoE function and reduces the user experience. In contrast, by
utilizing the learning capability of PLL-ABR, the bitrate selection is
almost not negatively affected in the same time period, and it is still
able to stably increase to a higher level and maintain it for nearly
100 seconds in the following, which significantly improves the
quality of user experience when watching videos.
Example 2. Under good network conditions, PLL-ABR also
significantly outperforms robust MPC and buffer-based methods.
Looking closely at the real-time buffer-size situation in the example, it can be clearly found that PLL-ABR tends to rapidly increase
the buffer size to a high level, and, therefore, tends to be more
conservative in the selection of the video bitrate at the beginning
stage, which It shows a trend of steady increase, and when the buffer
level is high enough, PLL-ABR increases the bitrate significantly and
ensures high quality delivery for a longer period of time, as can be
seen in Fig. 11(b), the buffer size reaches a higher level when the
timestamp is around 100 s, and the algorithm ensures the subsequent stable and high-quality delivery despite the large drop in the
network condition in the following 10 s or so until the end, on the
contrary, robust MPC and buffer-based tend to ignore the control
of buffer level in the starting phase and rapidly increase the bitrate
selection level, which may lead to subsequent dramatic fluctuations
in the bitrate selection level and difficulty in maintaining persistent
high-quality bitrates, and reduce the algorithm performance.
In both examples, we have combined the cases of poor and
good network conditions. Observing the comparison graphs in the
bitrate selection section, we can find that the PLL-ABR algorithm
has a more stable bitrate selection compared to the other two algorithms, indicating its better performance in video smoothness. At
the same time, due to its ability to utilize the buffer size and real-time
bandwidth situation more effectively, PLL-ABR can maintain a high
bitrate level for a longer period of time, which significantly improves
the quality of the user’s viewing experience. These experimental
results not only verify the superiority of the PLL-ABR algorithm
in different network environments with higher dynamic optimization and generalization capabilities but also highlight its potential
AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381
15, 075042-14
© Author(s) 2025
 09 June 2026 09:26:24

### Página 16

AIP Advances
ARTICLE
pubs.aip.org/aip/adv
FIG. 11. Real-time bitrate selection and
buffer occupancy analysis for each algorithm for (a) poor network environments
and (b) good network environments.
AIP Advances 15, 075042 (2025); doi: 10.1063/5.0277381
15, 075042-15
© Author(s) 2025
 09 June 2026 09:26:24

## 7. Referencias/bibliografía
Referencias detectadas desde la página 17. No se expanden completas aquí para no contaminar la lectura de método; consultar PDF original o raw text si hace falta.
