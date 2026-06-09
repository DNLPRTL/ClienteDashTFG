# HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance
**Archivo PDF:** `1-s2.0-S1084804523000231-main.pdf`  
**Identificador:** `07_edge_rl_adaptive_streaming_2023`  
**Páginas:** 12  
**Foco para Fase 4-5 v1:** RL with edge computing assistance; multiple clients; QoE fairness; VMAF/video characteristics.

> Documento Codex-ready generado para diseño de nuevos modelos/controllers IA ABR. No es una source card corta. Contiene extracción técnica cruda y organizada. El PDF original sigue siendo la fuente de verdad para fórmulas, tablas y figuras si la extracción textual pierde layout.

## 1. Cómo usar este `.md`
- Leer primero las secciones 2-4 para ubicar método, datos y evaluación.
- Usar los extractos crudos por categoría como material base para diseño/contratos/Codex.
- Para ecuaciones, tablas o figuras críticas, comprobar la página indicada en el PDF original.
- No tratar los resultados del paper como promesa directa para DashClientModular4; convertirlos en hipótesis/guardrails y verificar en Phase 6.

## 2. Índice de secciones detectadas
- p.2: M. Kim and K. Chung
- p.3: M. Kim and K. Chung
- p.4: M. Kim and K. Chung
- p.5: M. Kim and K. Chung
- p.6: M. Kim and K. Chung
- p.6: 4237 Kbps
- p.6: 3709 Kbps
- p.6: 3602 Kbps
- p.6: 4089 Kbps
- p.6: 2660 Kbps
- p.7: M. Kim and K. Chung
- p.8: M. Kim and K. Chung
- p.9: M. Kim and K. Chung
- p.10: M. Kim and K. Chung
- p.11: M. Kim and K. Chung
- p.12: M. Kim and K. Chung

## 3. Índice de páginas con palabras clave
- p.1: QoE, buffer, PPO, fairness
- p.2: QoE, throughput, dataset, trace, PPO, latency, VMAF, fairness
- p.3: state, action, reward, QoE, buffer, throughput, dataset, training, imitation, fairness
- p.4: state, action, reward, QoE, buffer, throughput, training, VMAF, fairness
- p.5: state, action, reward, QoE, trace, training, baseline, fairness, OOD
- p.6: state, action, reward, QoE, dataset, trace, training, PPO, VMAF, fairness
- p.7: state, action, reward, baseline, VMAF
- p.8: state, action, reward, QoE, dataset, trace, training, VMAF, fairness, OOD
- p.9: state, reward, QoE, buffer, VMAF, fairness
- p.10: QoE, buffer, throughput, imitation, VMAF, fairness
- p.11: state, QoE, buffer, throughput, dataset, PPO, imitation, fairness
- p.12: QoE, buffer, dataset, trace, training, PPO, fairness, OOD

## 4. Extracción técnica cruda por categorías

### 4.x Modelo / arquitectura / algoritmo

**[Modelo / arquitectura / algoritmo | extracto 1 | p.1]**

Journal of Network and Computer Applications 213 (2023) 103604 Available online 17 February 2023 1084-8045/© 2023 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance Minsu Kim, Kwangsue Chung ∗ Department of Electronics and Communications Engineering, Kwangwoon University, Seoul, 01897, South Korea A R T I C L E I N F O Keywords: Adaptive streaming Reinforcement learning Edge computing Quality of Experience A B S T R A C T As the number of users and the types of videos viewed increase, seamless video streaming services are becoming more important. Adaptive streaming aims to achieve high Quality of Experience (QoE) in time-varying network conditions. However, the existing schemes lack considerations for quality adaptation to improve QoE under dynamic network environments and multi-client competition. In this paper, we propose an HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance. The proposed scheme uses reinforcement learning to generate robust adaptation policy for changes in the network conditions. Edge computing plays a role of managing multiple clients based on information about the network and client. The proposed scheme considers subjective quality, multiple videos, and learning variances to advance the adaptation policy. By balancing between individual QoE and QoE fairness, the proposed scheme enables multiple clients to utilize the bandwidth as much as required. Experimental results show that the proposed scheme has better performance for individual QoE and QoE fairness than the existing schemes. 1. Introduction 

**[Modelo / arquitectura / algoritmo | extracto 2 | p.2]**

Journal of Network and Computer Applications 213 (2023) 103604 2 M. Kim and K. Chung Fig. 1. Behavioral structure of HTTP adaptive streaming. Fig. 2. VMAF scores according to bitrates of the BBB video. • We adopt edge computing to support adaptive streaming of multiple clients sharing the same network. • We utilize reinforcement learning to generate a robust adaptation policy for dynamic network environments. • We consider subjective quality, various video characteristics, and learning variances to improve the adaptation policy. • We perform extensive experiments by using the network trace datasets based on real environments and the videos with different characteristics. The remainder of this paper is organized as follows. HTTP adaptive streaming, QoE, edge computing, and reinforcement learning are described in Section 2. The proposed scheme is presented in Section 3. In Section 4, the proposed scheme is compared with existing schemes through simulation-based experiments. Finally, the paper is concluded in Section 5. 2. Related work The process of quality adaptation performed via HTTP adaptive streaming is shown in Fig. 1. The server stores a video in the form of segments with multiple bitrates and a fixed playback length. The client executes the algorithms for quality adaptation and requests a segment from the server. When video streaming starts, the client receives a Media Presentation Description (MPD) file from the server, which includes segment information such as the encoding bitrate and position. The client predicts network conditions based on the measured segment throughput. The quality of the next segment is determined as the bitrate that maximizes QoE under the estimated network conditions (Sobhani et al., 2017; Tian and Liu, 2015). In HTTP adaptive streaming,

**[Modelo / arquitectura / algoritmo | extracto 3 | p.3]**

Journal of Network and Computer Applications 213 (2023) 103604 3 M. Kim and K. Chung bitrate selection algorithm determines the bitrate satisfying each condition of the optimization problem as the quality of the next segment. If all conditions are not satisfied, the algorithm chooses the maximum sustainable bitrate based on the segment throughput and playback buffer level. However, when the network conditions change abruptly, the greedy-based bitrate selection algorithm suffers from QoE degradation. This kind of algorithm explores all cases to solve the optimization problem, leading to low adaptability for dynamic network environments. Edge Computing Assisted Adaptation Scheme with Machine Learning (ECAS-ML) performs intelligent quality adaptation based on edge capability and machine learning (Aguilar-Armijo et al., 2022). To achieve high QoE, the ECAS-ML scheme focuses on managing the tradeoff among bitrate, quality variations, and playback interruptions. The machine learning techniques are utilized to analyze the network conditions and predict the best parameters for heuristic algorithms. However, the ECAS-ML scheme still relies on heuristic algorithms for quality adaptation itself. Tuning the parameters has the limitations to improve overall QoE under dynamic network environments. Unlike the existing schemes, the proposed scheme in this study uses reinforcement learning rather than heuristic algorithms. The adaptation policy of the proposed scheme considers the impact of quality adaptation at each client on overall QoE. This leads to high adaptability for time-varying network conditions and variability in videos, maximizing individual QoE and QoE fairness. Reinforcement learning corrects behavior through trial and error to maximize the cumulative reward in sequential

**[Modelo / arquitectura / algoritmo | extracto 4 | p.4]**

Journal of Network and Computer Applications 213 (2023) 103604 4 M. Kim and K. Chung Fig. 4. Overview of the input data used for multiple linear regression. of the requested quality by segments, degree of quality variations, and playback interruption time. 𝑄𝑜𝐸𝑖= 𝜖𝑄(𝑏𝑖) −𝛿|𝑄(𝑏𝑖) −𝑄(𝑏𝑖−1)| −𝜌𝑇(𝑏𝑖) (1) Where 𝑄𝑜𝐸𝑖is the individual QoE for the 𝑖th segment, and 𝑄(𝑏𝑖) means the function that indicates the relationship between the bitrate 𝑏𝑖and the quality perceived by the client. 𝑇(𝑏𝑖) is the playback interruption time that occurs after the client receives the 𝑖th segment. 𝜖, 𝛿, 𝜌are the weight parameters to combine the requested quality, quality variations, and playback interruption time. The proposed scheme defines 𝑄(𝑏𝑖) as the VMAF score for the bitrate 𝑏𝑖to consider the correlation between bitrate and quality. The Waterloo SQoE-III database is used to determine the values of the weight parameters (Duanmu et al., 2018). The information about bitrate changes due to quality adaptation, the quality perceived by the client, and the VMAF scores by bitrates exist in the Waterloo SQoEIII database. The proposed scheme performs multiple linear regression. Fig. 4 shows the input data to learn the regression model. The proposed scheme uses 80% of the total videos as the training set and the remaining 20% as the testing set. Data division and learning are iterated 1,000 times to reduce the bias occurred when the amount of training data is small. The trained regression model obtains a prediction accuracy of 79.23% for the Waterloo SQoE-III database. The values of the weight parameters are set to 0.41, 0.3, and 6.03, respectively. The proposed scheme aims to maximize the individual QoE and QoE fairness for multiple clients. The target reward of the neural network model is calculated by l

**[Modelo / arquitectura / algoritmo | extracto 5 | p.5]**

Journal of Network and Computer Applications 213 (2023) 103604 5 M. Kim and K. Chung Fig. 5. Structure of the neural network model used in the proposed scheme. 𝜃denotes the parameters of the neural network model, 𝑡is the time step for the episode experienced by the agent, and 𝑟𝑡is the target reward at the time step 𝑡. The proposed scheme treats the time step and the segment index as the same value. 𝜋𝜃(𝑠, 𝑎) means the probability that the agent selects the action 𝑎at the state 𝑠by the policy 𝜋𝜃. 𝐴𝑑𝑣𝜋𝜃(𝑠, 𝑎) is the advantage function that determines the direction of policy improvement. The policy gradient method predicts changes in the expected cumulative discounted reward through the execution trajectories of the current policy. The agent improves the policy to increase the selection probability of the action that maximizes the expected cumulative discounted reward. After the episode ends, the neural network model aggregates the state, the action, the reward, and the policy gradient calculated. The actor network updates its parameters by considering the advantage function and the entropy for the policy. 𝜃𝐴←𝜃𝐴+ 𝛼 𝑃 ∑ 𝑡=1 ▿𝜃𝐴ln { 𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) } 𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) +𝛽▿𝜃𝐴𝐻 { 𝜋𝜃𝐴(∙|𝑠𝑡) } (6) Where 𝜃𝐴denotes the parameters of the actor network, and 𝛼is the learning rate for the actor network. 𝑠𝑡and 𝑎𝑡are the state and the action at the time step 𝑡, respectively. 𝑃means the length of the episode. 𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) is calculated as changes in the expected cumulative discounted reward due to the action determined by the current policy 𝜋𝜃𝐴and the specific action. 𝐻{𝜋𝜃𝐴(∙|𝑠𝑡)} is used to generate a good policy by sufficiently exploring the action space. The proposed scheme defines the entropy for the policy based on the selection probability of all bitrate levels. 𝛽is the entropy weight, wh

**[Modelo / arquitectura / algoritmo | extracto 6 | p.6]**

Journal of Network and Computer Applications 213 (2023) 103604 6 M. Kim and K. Chung Table 1 Configuration of the dataset to support multiple videos. Name Types and characteristics Source bitrate Encoding bitrate BigBuckBunny (BBB) - Animation - High motion 4237 Kbps 300, 800, 1400, 2200, 3000, 3900 Kbps CostaRica (CR) - Nature - Low motion 3709 Kbps 200, 700, 1200, 2000, 2600, 3500 Kbps CSGO (CG) - Game - Average motion 3602 Kbps 500, 950, 1600, 2300, 2800, 3400 Kbps Ski (SK) - Sports - High motion 4089 Kbps 350, 600, 1100, 1800, 2550, 3250 Kbps TearsOfSteel (TOS) - Movie - Low motion 2660 Kbps 400, 550, 1050, 1500, 1950, 2400 Kbps The simulator informs the agent about the state, the action, and the immediate reward for the received segment. Using this segment-level simulator, the proposed scheme learns the neural network model within a short time. The trained neural network model is deployed on the edge server for quality adaptation of multiple clients. In the proposed scheme, the actor network of the central agent is placed on the edge server. When video streaming starts, the edge server creates the same number of instances for the actor network as the number of clients connected. The edge server detects the segment request of the client and extracts QoE-related information. The extracted information is then delivered to the actor network. The output of the instance is the bitrate maximizing individual QoE and QoE fairness at the current state. The edge server modifies the quality information of the segment request according to the output of the instance. The edge server transmits the modified segment request to the server. Upon receiving the segment request, the server transmits the segment corresponding to the requested quality to the client. 3.4. Supporting of mul

**[Modelo / arquitectura / algoritmo | extracto 7 | p.7]**

Journal of Network and Computer Applications 213 (2023) 103604 7 M. Kim and K. Chung Fig. 8. VMAF scores according to segment index for multiple videos. Fig. 9. Immediate reward by episodes of the Pensieve scheme. Pensieve scheme, we performed experiments to measure the changes in the immediate reward according to the episodes. The setup of the Pensieve scheme is used to learn the neural network model (Mao et al., 2017). Fig. 9 shows how the immediate reward of the Pensieve scheme changes by episodes. The measurement results confirmed that the immediate reward fluctuates abruptly for each episode. In the Pensieve scheme, the actor network depends on the expected cumulative discounted reward predicted by the critic network for policy improvement. The learning method using the state-dependent baseline is difficult to distinguish which one affects the reward between the current policy and external factors (Mao et al., 2018). The critic network updates the parameters of the neural network model to reduce the prediction error as the episode proceeds. The direction of policy improvement is wrongly determined by the prediction error at the beginning of learning. To reduce the learning variances due to the error in the statedependent baseline, the proposed scheme uses the input-dependent baseline. The multi-critic network and baseline smoothing can be used to calculate the input-dependent baseline. The multi-critic network includes multiple critic networks that experience different episodes. Each critic network calculates a state-dependent baseline for the current policy of the actor network. The actor network updates its parameters in parallel according to the state-dependent baseline calculated. The multi-critic network approach converges fast to the optimal policy. However, 

**[Modelo / arquitectura / algoritmo | extracto 8 | p.8]**

Journal of Network and Computer Applications 213 (2023) 103604 8 M. Kim and K. Chung Table 3 Setup for the variables used in multi-agent training. Notation Meaning Value 𝑀 Number of multiple inputs 8 𝐿 Number of bitrate levels 6 𝛾 Discounting factor 0.99 𝛼 Learning rate of actor network 0.0001 𝛼′ Learning rate of critic network 0.001 𝛽 Entropy weight 5 to 1 (80,000 episodes) 𝑁𝑟 Number of episode iterations 10 𝑁𝑎 Number of training agents 20 the episodes. The proposed scheme quickly generates the policy that maximizes individual QoE and QoE fairness through input-dependent learning. 3.6. Advantages compared with the existing schemes The proposed scheme uses reinforcement learning based on edge computing assistance. To generate the optimal adaptation policy for multiple clients, the target reward is formulated as a combination of individual QoE and QoE fairness. The QoE of each client, the QoE deviations among multiple clients, and the relationship between bitrate and quality are considered in the target reward. The proposed scheme adopts multi-agent training method to learn the neural network model. Therefore, the adaptation policy is able to determine the next video quality by recognizing multi-client competition under time-varying network conditions. In addition to collecting information about network and client, the edge server handles the neural network model to perform intelligent quality adaptation. The proposed scheme applies the concept of multiple videos and input-dependent learning to adaptation policy generation. This helps the adaptation policy to achieve high QoE in real environments. Consequently, the proposed scheme maximizes the streaming performance for multiple clients. 4. Performance evaluation In this section, we compare the proposed scheme with exist

**[Modelo / arquitectura / algoritmo | extracto 9 | p.9]**

Journal of Network and Computer Applications 213 (2023) 103604 9 M. Kim and K. Chung Table 5 Summary of the performance for the QoE components (BBB). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.78 0.10 0.44 Pensieve (Mao et al., 2017) 2.90 0.10 0.28 QFDVS (Altamimi and Shirmohammadi, 2020) 2.48 0.11 0.40 Proposed 2.90 0.09 0.03 playback interruptions. 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) = 1 𝑃 { 𝜖 𝑃 ∑ 𝑖=1 𝑄(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑄.𝑈 −𝛿 𝑃−1 ∑ 𝑖=1 |𝑄(𝑏𝑖+1) −𝑄(𝑏𝑖)| ⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟ 𝑆.𝑃 −𝜌 𝑃 ∑ 𝑖=1 𝑇(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑅.𝑃 } (12) Where 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) is the average QoE for all segments in the episode experienced by the 𝑘th client. 𝑄.𝑈is the quality utility aggregated for the episode. 𝑆.𝑃is the smoothness penalty calculated by using the magnitude of quality variations. 𝑅.𝑃is the re-buffering penalty determined by the playback interruption time. To evaluate the performance, we measure the average of the overall QoE for the number of clients. By improving QoE fairness, the client can utilize the bandwidth as much as needed to maximize individual QoE (Hoßfeld et al., 2016). We calculate the QoE fairness by using Jain’s Fairness Index (JFI) (Sediq et al., 2013). 𝐽(𝑄𝑜𝐸𝑖) = {∑𝑁𝑎 𝑘=1 𝑄𝑜𝐸𝑖(𝑘)}2 𝑁𝑎 ∑𝑁𝑎 𝑘=1{𝑄𝑜𝐸𝑖(𝑘)}2 (13) Where 𝐽(𝑄𝑜𝐸𝑖) is the QoE fairness for the 𝑖th segment of all clients, and 𝑄𝑜𝐸𝑖(𝑘) is the individual QoE obtained after the 𝑘th client receives the 𝑖th segment. The QoE fairness has a value within 0 and 1. The value close to 1 means that the QoE deviation among multiple clients is low. To evaluate the performance, we measure the average of the QoE fairness for the segments. 4.3. Results for a single video When receiving the BBB video, multiple clients should maintain high quality to maximize individual QoE. The unnecessary quality variations and

**[Modelo / arquitectura / algoritmo | extracto 10 | p.10]**

Journal of Network and Computer Applications 213 (2023) 103604 10 M. Kim and K. Chung Fig. 11. Overall QoE and QoE fairness according to the number of clients (CR). Table 7 Summary of the performance for the QoE components (TOS). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.86 0.08 0.38 Pensieve (Mao et al., 2017) 3.06 0.09 0.33 QFDVS (Altamimi and Shirmohammadi, 2020) 2.55 0.10 0.13 Proposed 3.08 0.07 0.09 number of clients increases by the aggressive adaptation policy. The QFDVS scheme generates the naive adaptation policy, so the overall QoE and the QoE fairness are low. The proposed scheme generates the conservative adaptation policy. This adaptation policy makes the client to utilize the bandwidth as much as needed, leading to the improvements of individual QoE and QoE fairness. Table 6 shows summary of the performance for the QoE components according to various schemes. The ECAA scheme has high smoothness penalty due to quality adaptation based on segment throughput. The aggressive adaptation policy of the Pensieve scheme leads to high quality utility. The QFDVS scheme has low smoothness penalty, but the re-buffering penalty increases by the conservative adaptation policy. The proposed scheme increases the quality slowly and stays long at high quality, resulting in low smoothness penalty and re-buffering penalty. The variations in VMAF scores decrease at high quality, so the differences in VMAF scores for each quality are small, even for the same segment. When receiving the TOS video, multiple clients should improve individual QoE by maintaining high quality for a long time and changing the quality gradually. Moreover, the adaptation policy should select the quality by considering situations that multiple clients oc

### 4.x Estado / inputs / features observables

**[Estado / inputs / features observables | extracto 1 | p.1]**

Journal of Network and Computer Applications 213 (2023) 103604 Available online 17 February 2023 1084-8045/© 2023 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance Minsu Kim, Kwangsue Chung ∗ Department of Electronics and Communications Engineering, Kwangwoon University, Seoul, 01897, South Korea A R T I C L E I N F O Keywords: Adaptive streaming Reinforcement learning Edge computing Quality of Experience A B S T R A C T As the number of users and the types of videos viewed increase, seamless video streaming services are becoming more important. Adaptive streaming aims to achieve high Quality of Experience (QoE) in time-varying network conditions. However, the existing schemes lack considerations for quality adaptation to improve QoE under dynamic network environments and multi-client competition. In this paper, we propose an HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance. The proposed scheme uses reinforcement learning to generate robust adaptation policy for changes in the network conditions. Edge computing plays a role of managing multiple clients based on information about the network and client. The proposed scheme considers subjective quality, multiple videos, and learning variances to advance the adaptation policy. By balancing between individual QoE and QoE fairness, the proposed scheme enables multiple clients to utilize the bandwidth as much as required. Experimental results show that the proposed scheme has better performance for individual QoE and QoE fairness than the existing schemes. 1. Introduction 

**[Estado / inputs / features observables | extracto 2 | p.2]**

Journal of Network and Computer Applications 213 (2023) 103604 2 M. Kim and K. Chung Fig. 1. Behavioral structure of HTTP adaptive streaming. Fig. 2. VMAF scores according to bitrates of the BBB video. • We adopt edge computing to support adaptive streaming of multiple clients sharing the same network. • We utilize reinforcement learning to generate a robust adaptation policy for dynamic network environments. • We consider subjective quality, various video characteristics, and learning variances to improve the adaptation policy. • We perform extensive experiments by using the network trace datasets based on real environments and the videos with different characteristics. The remainder of this paper is organized as follows. HTTP adaptive streaming, QoE, edge computing, and reinforcement learning are described in Section 2. The proposed scheme is presented in Section 3. In Section 4, the proposed scheme is compared with existing schemes through simulation-based experiments. Finally, the paper is concluded in Section 5. 2. Related work The process of quality adaptation performed via HTTP adaptive streaming is shown in Fig. 1. The server stores a video in the form of segments with multiple bitrates and a fixed playback length. The client executes the algorithms for quality adaptation and requests a segment from the server. When video streaming starts, the client receives a Media Presentation Description (MPD) file from the server, which includes segment information such as the encoding bitrate and position. The client predicts network conditions based on the measured segment throughput. The quality of the next segment is determined as the bitrate that maximizes QoE under the estimated network conditions (Sobhani et al., 2017; Tian and Liu, 2015). In HTTP adaptive streaming,

**[Estado / inputs / features observables | extracto 3 | p.3]**

Journal of Network and Computer Applications 213 (2023) 103604 3 M. Kim and K. Chung bitrate selection algorithm determines the bitrate satisfying each condition of the optimization problem as the quality of the next segment. If all conditions are not satisfied, the algorithm chooses the maximum sustainable bitrate based on the segment throughput and playback buffer level. However, when the network conditions change abruptly, the greedy-based bitrate selection algorithm suffers from QoE degradation. This kind of algorithm explores all cases to solve the optimization problem, leading to low adaptability for dynamic network environments. Edge Computing Assisted Adaptation Scheme with Machine Learning (ECAS-ML) performs intelligent quality adaptation based on edge capability and machine learning (Aguilar-Armijo et al., 2022). To achieve high QoE, the ECAS-ML scheme focuses on managing the tradeoff among bitrate, quality variations, and playback interruptions. The machine learning techniques are utilized to analyze the network conditions and predict the best parameters for heuristic algorithms. However, the ECAS-ML scheme still relies on heuristic algorithms for quality adaptation itself. Tuning the parameters has the limitations to improve overall QoE under dynamic network environments. Unlike the existing schemes, the proposed scheme in this study uses reinforcement learning rather than heuristic algorithms. The adaptation policy of the proposed scheme considers the impact of quality adaptation at each client on overall QoE. This leads to high adaptability for time-varying network conditions and variability in videos, maximizing individual QoE and QoE fairness. Reinforcement learning corrects behavior through trial and error to maximize the cumulative reward in sequential

**[Estado / inputs / features observables | extracto 4 | p.4]**

Journal of Network and Computer Applications 213 (2023) 103604 4 M. Kim and K. Chung Fig. 4. Overview of the input data used for multiple linear regression. of the requested quality by segments, degree of quality variations, and playback interruption time. 𝑄𝑜𝐸𝑖= 𝜖𝑄(𝑏𝑖) −𝛿|𝑄(𝑏𝑖) −𝑄(𝑏𝑖−1)| −𝜌𝑇(𝑏𝑖) (1) Where 𝑄𝑜𝐸𝑖is the individual QoE for the 𝑖th segment, and 𝑄(𝑏𝑖) means the function that indicates the relationship between the bitrate 𝑏𝑖and the quality perceived by the client. 𝑇(𝑏𝑖) is the playback interruption time that occurs after the client receives the 𝑖th segment. 𝜖, 𝛿, 𝜌are the weight parameters to combine the requested quality, quality variations, and playback interruption time. The proposed scheme defines 𝑄(𝑏𝑖) as the VMAF score for the bitrate 𝑏𝑖to consider the correlation between bitrate and quality. The Waterloo SQoE-III database is used to determine the values of the weight parameters (Duanmu et al., 2018). The information about bitrate changes due to quality adaptation, the quality perceived by the client, and the VMAF scores by bitrates exist in the Waterloo SQoEIII database. The proposed scheme performs multiple linear regression. Fig. 4 shows the input data to learn the regression model. The proposed scheme uses 80% of the total videos as the training set and the remaining 20% as the testing set. Data division and learning are iterated 1,000 times to reduce the bias occurred when the amount of training data is small. The trained regression model obtains a prediction accuracy of 79.23% for the Waterloo SQoE-III database. The values of the weight parameters are set to 0.41, 0.3, and 6.03, respectively. The proposed scheme aims to maximize the individual QoE and QoE fairness for multiple clients. The target reward of the neural network model is calculated by l

**[Estado / inputs / features observables | extracto 5 | p.5]**

Journal of Network and Computer Applications 213 (2023) 103604 5 M. Kim and K. Chung Fig. 5. Structure of the neural network model used in the proposed scheme. 𝜃denotes the parameters of the neural network model, 𝑡is the time step for the episode experienced by the agent, and 𝑟𝑡is the target reward at the time step 𝑡. The proposed scheme treats the time step and the segment index as the same value. 𝜋𝜃(𝑠, 𝑎) means the probability that the agent selects the action 𝑎at the state 𝑠by the policy 𝜋𝜃. 𝐴𝑑𝑣𝜋𝜃(𝑠, 𝑎) is the advantage function that determines the direction of policy improvement. The policy gradient method predicts changes in the expected cumulative discounted reward through the execution trajectories of the current policy. The agent improves the policy to increase the selection probability of the action that maximizes the expected cumulative discounted reward. After the episode ends, the neural network model aggregates the state, the action, the reward, and the policy gradient calculated. The actor network updates its parameters by considering the advantage function and the entropy for the policy. 𝜃𝐴←𝜃𝐴+ 𝛼 𝑃 ∑ 𝑡=1 ▿𝜃𝐴ln { 𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) } 𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) +𝛽▿𝜃𝐴𝐻 { 𝜋𝜃𝐴(∙|𝑠𝑡) } (6) Where 𝜃𝐴denotes the parameters of the actor network, and 𝛼is the learning rate for the actor network. 𝑠𝑡and 𝑎𝑡are the state and the action at the time step 𝑡, respectively. 𝑃means the length of the episode. 𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) is calculated as changes in the expected cumulative discounted reward due to the action determined by the current policy 𝜋𝜃𝐴and the specific action. 𝐻{𝜋𝜃𝐴(∙|𝑠𝑡)} is used to generate a good policy by sufficiently exploring the action space. The proposed scheme defines the entropy for the policy based on the selection probability of all bitrate levels. 𝛽is the entropy weight, wh

**[Estado / inputs / features observables | extracto 6 | p.6]**

Journal of Network and Computer Applications 213 (2023) 103604 6 M. Kim and K. Chung Table 1 Configuration of the dataset to support multiple videos. Name Types and characteristics Source bitrate Encoding bitrate BigBuckBunny (BBB) - Animation - High motion 4237 Kbps 300, 800, 1400, 2200, 3000, 3900 Kbps CostaRica (CR) - Nature - Low motion 3709 Kbps 200, 700, 1200, 2000, 2600, 3500 Kbps CSGO (CG) - Game - Average motion 3602 Kbps 500, 950, 1600, 2300, 2800, 3400 Kbps Ski (SK) - Sports - High motion 4089 Kbps 350, 600, 1100, 1800, 2550, 3250 Kbps TearsOfSteel (TOS) - Movie - Low motion 2660 Kbps 400, 550, 1050, 1500, 1950, 2400 Kbps The simulator informs the agent about the state, the action, and the immediate reward for the received segment. Using this segment-level simulator, the proposed scheme learns the neural network model within a short time. The trained neural network model is deployed on the edge server for quality adaptation of multiple clients. In the proposed scheme, the actor network of the central agent is placed on the edge server. When video streaming starts, the edge server creates the same number of instances for the actor network as the number of clients connected. The edge server detects the segment request of the client and extracts QoE-related information. The extracted information is then delivered to the actor network. The output of the instance is the bitrate maximizing individual QoE and QoE fairness at the current state. The edge server modifies the quality information of the segment request according to the output of the instance. The edge server transmits the modified segment request to the server. Upon receiving the segment request, the server transmits the segment corresponding to the requested quality to the client. 3.4. Supporting of mul

**[Estado / inputs / features observables | extracto 7 | p.7]**

Journal of Network and Computer Applications 213 (2023) 103604 7 M. Kim and K. Chung Fig. 8. VMAF scores according to segment index for multiple videos. Fig. 9. Immediate reward by episodes of the Pensieve scheme. Pensieve scheme, we performed experiments to measure the changes in the immediate reward according to the episodes. The setup of the Pensieve scheme is used to learn the neural network model (Mao et al., 2017). Fig. 9 shows how the immediate reward of the Pensieve scheme changes by episodes. The measurement results confirmed that the immediate reward fluctuates abruptly for each episode. In the Pensieve scheme, the actor network depends on the expected cumulative discounted reward predicted by the critic network for policy improvement. The learning method using the state-dependent baseline is difficult to distinguish which one affects the reward between the current policy and external factors (Mao et al., 2018). The critic network updates the parameters of the neural network model to reduce the prediction error as the episode proceeds. The direction of policy improvement is wrongly determined by the prediction error at the beginning of learning. To reduce the learning variances due to the error in the statedependent baseline, the proposed scheme uses the input-dependent baseline. The multi-critic network and baseline smoothing can be used to calculate the input-dependent baseline. The multi-critic network includes multiple critic networks that experience different episodes. Each critic network calculates a state-dependent baseline for the current policy of the actor network. The actor network updates its parameters in parallel according to the state-dependent baseline calculated. The multi-critic network approach converges fast to the optimal policy. However, 

**[Estado / inputs / features observables | extracto 8 | p.8]**

Journal of Network and Computer Applications 213 (2023) 103604 8 M. Kim and K. Chung Table 3 Setup for the variables used in multi-agent training. Notation Meaning Value 𝑀 Number of multiple inputs 8 𝐿 Number of bitrate levels 6 𝛾 Discounting factor 0.99 𝛼 Learning rate of actor network 0.0001 𝛼′ Learning rate of critic network 0.001 𝛽 Entropy weight 5 to 1 (80,000 episodes) 𝑁𝑟 Number of episode iterations 10 𝑁𝑎 Number of training agents 20 the episodes. The proposed scheme quickly generates the policy that maximizes individual QoE and QoE fairness through input-dependent learning. 3.6. Advantages compared with the existing schemes The proposed scheme uses reinforcement learning based on edge computing assistance. To generate the optimal adaptation policy for multiple clients, the target reward is formulated as a combination of individual QoE and QoE fairness. The QoE of each client, the QoE deviations among multiple clients, and the relationship between bitrate and quality are considered in the target reward. The proposed scheme adopts multi-agent training method to learn the neural network model. Therefore, the adaptation policy is able to determine the next video quality by recognizing multi-client competition under time-varying network conditions. In addition to collecting information about network and client, the edge server handles the neural network model to perform intelligent quality adaptation. The proposed scheme applies the concept of multiple videos and input-dependent learning to adaptation policy generation. This helps the adaptation policy to achieve high QoE in real environments. Consequently, the proposed scheme maximizes the streaming performance for multiple clients. 4. Performance evaluation In this section, we compare the proposed scheme with exist

**[Estado / inputs / features observables | extracto 9 | p.9]**

Journal of Network and Computer Applications 213 (2023) 103604 9 M. Kim and K. Chung Table 5 Summary of the performance for the QoE components (BBB). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.78 0.10 0.44 Pensieve (Mao et al., 2017) 2.90 0.10 0.28 QFDVS (Altamimi and Shirmohammadi, 2020) 2.48 0.11 0.40 Proposed 2.90 0.09 0.03 playback interruptions. 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) = 1 𝑃 { 𝜖 𝑃 ∑ 𝑖=1 𝑄(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑄.𝑈 −𝛿 𝑃−1 ∑ 𝑖=1 |𝑄(𝑏𝑖+1) −𝑄(𝑏𝑖)| ⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟ 𝑆.𝑃 −𝜌 𝑃 ∑ 𝑖=1 𝑇(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑅.𝑃 } (12) Where 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) is the average QoE for all segments in the episode experienced by the 𝑘th client. 𝑄.𝑈is the quality utility aggregated for the episode. 𝑆.𝑃is the smoothness penalty calculated by using the magnitude of quality variations. 𝑅.𝑃is the re-buffering penalty determined by the playback interruption time. To evaluate the performance, we measure the average of the overall QoE for the number of clients. By improving QoE fairness, the client can utilize the bandwidth as much as needed to maximize individual QoE (Hoßfeld et al., 2016). We calculate the QoE fairness by using Jain’s Fairness Index (JFI) (Sediq et al., 2013). 𝐽(𝑄𝑜𝐸𝑖) = {∑𝑁𝑎 𝑘=1 𝑄𝑜𝐸𝑖(𝑘)}2 𝑁𝑎 ∑𝑁𝑎 𝑘=1{𝑄𝑜𝐸𝑖(𝑘)}2 (13) Where 𝐽(𝑄𝑜𝐸𝑖) is the QoE fairness for the 𝑖th segment of all clients, and 𝑄𝑜𝐸𝑖(𝑘) is the individual QoE obtained after the 𝑘th client receives the 𝑖th segment. The QoE fairness has a value within 0 and 1. The value close to 1 means that the QoE deviation among multiple clients is low. To evaluate the performance, we measure the average of the QoE fairness for the segments. 4.3. Results for a single video When receiving the BBB video, multiple clients should maintain high quality to maximize individual QoE. The unnecessary quality variations and

**[Estado / inputs / features observables | extracto 10 | p.10]**

Journal of Network and Computer Applications 213 (2023) 103604 10 M. Kim and K. Chung Fig. 11. Overall QoE and QoE fairness according to the number of clients (CR). Table 7 Summary of the performance for the QoE components (TOS). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.86 0.08 0.38 Pensieve (Mao et al., 2017) 3.06 0.09 0.33 QFDVS (Altamimi and Shirmohammadi, 2020) 2.55 0.10 0.13 Proposed 3.08 0.07 0.09 number of clients increases by the aggressive adaptation policy. The QFDVS scheme generates the naive adaptation policy, so the overall QoE and the QoE fairness are low. The proposed scheme generates the conservative adaptation policy. This adaptation policy makes the client to utilize the bandwidth as much as needed, leading to the improvements of individual QoE and QoE fairness. Table 6 shows summary of the performance for the QoE components according to various schemes. The ECAA scheme has high smoothness penalty due to quality adaptation based on segment throughput. The aggressive adaptation policy of the Pensieve scheme leads to high quality utility. The QFDVS scheme has low smoothness penalty, but the re-buffering penalty increases by the conservative adaptation policy. The proposed scheme increases the quality slowly and stays long at high quality, resulting in low smoothness penalty and re-buffering penalty. The variations in VMAF scores decrease at high quality, so the differences in VMAF scores for each quality are small, even for the same segment. When receiving the TOS video, multiple clients should improve individual QoE by maintaining high quality for a long time and changing the quality gradually. Moreover, the adaptation policy should select the quality by considering situations that multiple clients oc

### 4.x Acción / decisión ABR

**[Acción / decisión ABR | extracto 1 | p.1]**

Journal of Network and Computer Applications 213 (2023) 103604 Available online 17 February 2023 1084-8045/© 2023 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance Minsu Kim, Kwangsue Chung ∗ Department of Electronics and Communications Engineering, Kwangwoon University, Seoul, 01897, South Korea A R T I C L E I N F O Keywords: Adaptive streaming Reinforcement learning Edge computing Quality of Experience A B S T R A C T As the number of users and the types of videos viewed increase, seamless video streaming services are becoming more important. Adaptive streaming aims to achieve high Quality of Experience (QoE) in time-varying network conditions. However, the existing schemes lack considerations for quality adaptation to improve QoE under dynamic network environments and multi-client competition. In this paper, we propose an HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance. The proposed scheme uses reinforcement learning to generate robust adaptation policy for changes in the network conditions. Edge computing plays a role of managing multiple clients based on information about the network and client. The proposed scheme considers subjective quality, multiple videos, and learning variances to advance the adaptation policy. By balancing between individual QoE and QoE fairness, the proposed scheme enables multiple clients to utilize the bandwidth as much as required. Experimental results show that the proposed scheme has better performance for individual QoE and QoE fairness than the existing schemes. 1. Introduction 

**[Acción / decisión ABR | extracto 2 | p.2]**

Journal of Network and Computer Applications 213 (2023) 103604 2 M. Kim and K. Chung Fig. 1. Behavioral structure of HTTP adaptive streaming. Fig. 2. VMAF scores according to bitrates of the BBB video. • We adopt edge computing to support adaptive streaming of multiple clients sharing the same network. • We utilize reinforcement learning to generate a robust adaptation policy for dynamic network environments. • We consider subjective quality, various video characteristics, and learning variances to improve the adaptation policy. • We perform extensive experiments by using the network trace datasets based on real environments and the videos with different characteristics. The remainder of this paper is organized as follows. HTTP adaptive streaming, QoE, edge computing, and reinforcement learning are described in Section 2. The proposed scheme is presented in Section 3. In Section 4, the proposed scheme is compared with existing schemes through simulation-based experiments. Finally, the paper is concluded in Section 5. 2. Related work The process of quality adaptation performed via HTTP adaptive streaming is shown in Fig. 1. The server stores a video in the form of segments with multiple bitrates and a fixed playback length. The client executes the algorithms for quality adaptation and requests a segment from the server. When video streaming starts, the client receives a Media Presentation Description (MPD) file from the server, which includes segment information such as the encoding bitrate and position. The client predicts network conditions based on the measured segment throughput. The quality of the next segment is determined as the bitrate that maximizes QoE under the estimated network conditions (Sobhani et al., 2017; Tian and Liu, 2015). In HTTP adaptive streaming,

**[Acción / decisión ABR | extracto 3 | p.3]**

Journal of Network and Computer Applications 213 (2023) 103604 3 M. Kim and K. Chung bitrate selection algorithm determines the bitrate satisfying each condition of the optimization problem as the quality of the next segment. If all conditions are not satisfied, the algorithm chooses the maximum sustainable bitrate based on the segment throughput and playback buffer level. However, when the network conditions change abruptly, the greedy-based bitrate selection algorithm suffers from QoE degradation. This kind of algorithm explores all cases to solve the optimization problem, leading to low adaptability for dynamic network environments. Edge Computing Assisted Adaptation Scheme with Machine Learning (ECAS-ML) performs intelligent quality adaptation based on edge capability and machine learning (Aguilar-Armijo et al., 2022). To achieve high QoE, the ECAS-ML scheme focuses on managing the tradeoff among bitrate, quality variations, and playback interruptions. The machine learning techniques are utilized to analyze the network conditions and predict the best parameters for heuristic algorithms. However, the ECAS-ML scheme still relies on heuristic algorithms for quality adaptation itself. Tuning the parameters has the limitations to improve overall QoE under dynamic network environments. Unlike the existing schemes, the proposed scheme in this study uses reinforcement learning rather than heuristic algorithms. The adaptation policy of the proposed scheme considers the impact of quality adaptation at each client on overall QoE. This leads to high adaptability for time-varying network conditions and variability in videos, maximizing individual QoE and QoE fairness. Reinforcement learning corrects behavior through trial and error to maximize the cumulative reward in sequential

**[Acción / decisión ABR | extracto 4 | p.4]**

Journal of Network and Computer Applications 213 (2023) 103604 4 M. Kim and K. Chung Fig. 4. Overview of the input data used for multiple linear regression. of the requested quality by segments, degree of quality variations, and playback interruption time. 𝑄𝑜𝐸𝑖= 𝜖𝑄(𝑏𝑖) −𝛿|𝑄(𝑏𝑖) −𝑄(𝑏𝑖−1)| −𝜌𝑇(𝑏𝑖) (1) Where 𝑄𝑜𝐸𝑖is the individual QoE for the 𝑖th segment, and 𝑄(𝑏𝑖) means the function that indicates the relationship between the bitrate 𝑏𝑖and the quality perceived by the client. 𝑇(𝑏𝑖) is the playback interruption time that occurs after the client receives the 𝑖th segment. 𝜖, 𝛿, 𝜌are the weight parameters to combine the requested quality, quality variations, and playback interruption time. The proposed scheme defines 𝑄(𝑏𝑖) as the VMAF score for the bitrate 𝑏𝑖to consider the correlation between bitrate and quality. The Waterloo SQoE-III database is used to determine the values of the weight parameters (Duanmu et al., 2018). The information about bitrate changes due to quality adaptation, the quality perceived by the client, and the VMAF scores by bitrates exist in the Waterloo SQoEIII database. The proposed scheme performs multiple linear regression. Fig. 4 shows the input data to learn the regression model. The proposed scheme uses 80% of the total videos as the training set and the remaining 20% as the testing set. Data division and learning are iterated 1,000 times to reduce the bias occurred when the amount of training data is small. The trained regression model obtains a prediction accuracy of 79.23% for the Waterloo SQoE-III database. The values of the weight parameters are set to 0.41, 0.3, and 6.03, respectively. The proposed scheme aims to maximize the individual QoE and QoE fairness for multiple clients. The target reward of the neural network model is calculated by l

**[Acción / decisión ABR | extracto 5 | p.5]**

Journal of Network and Computer Applications 213 (2023) 103604 5 M. Kim and K. Chung Fig. 5. Structure of the neural network model used in the proposed scheme. 𝜃denotes the parameters of the neural network model, 𝑡is the time step for the episode experienced by the agent, and 𝑟𝑡is the target reward at the time step 𝑡. The proposed scheme treats the time step and the segment index as the same value. 𝜋𝜃(𝑠, 𝑎) means the probability that the agent selects the action 𝑎at the state 𝑠by the policy 𝜋𝜃. 𝐴𝑑𝑣𝜋𝜃(𝑠, 𝑎) is the advantage function that determines the direction of policy improvement. The policy gradient method predicts changes in the expected cumulative discounted reward through the execution trajectories of the current policy. The agent improves the policy to increase the selection probability of the action that maximizes the expected cumulative discounted reward. After the episode ends, the neural network model aggregates the state, the action, the reward, and the policy gradient calculated. The actor network updates its parameters by considering the advantage function and the entropy for the policy. 𝜃𝐴←𝜃𝐴+ 𝛼 𝑃 ∑ 𝑡=1 ▿𝜃𝐴ln { 𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) } 𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) +𝛽▿𝜃𝐴𝐻 { 𝜋𝜃𝐴(∙|𝑠𝑡) } (6) Where 𝜃𝐴denotes the parameters of the actor network, and 𝛼is the learning rate for the actor network. 𝑠𝑡and 𝑎𝑡are the state and the action at the time step 𝑡, respectively. 𝑃means the length of the episode. 𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) is calculated as changes in the expected cumulative discounted reward due to the action determined by the current policy 𝜋𝜃𝐴and the specific action. 𝐻{𝜋𝜃𝐴(∙|𝑠𝑡)} is used to generate a good policy by sufficiently exploring the action space. The proposed scheme defines the entropy for the policy based on the selection probability of all bitrate levels. 𝛽is the entropy weight, wh

**[Acción / decisión ABR | extracto 6 | p.6]**

Journal of Network and Computer Applications 213 (2023) 103604 6 M. Kim and K. Chung Table 1 Configuration of the dataset to support multiple videos. Name Types and characteristics Source bitrate Encoding bitrate BigBuckBunny (BBB) - Animation - High motion 4237 Kbps 300, 800, 1400, 2200, 3000, 3900 Kbps CostaRica (CR) - Nature - Low motion 3709 Kbps 200, 700, 1200, 2000, 2600, 3500 Kbps CSGO (CG) - Game - Average motion 3602 Kbps 500, 950, 1600, 2300, 2800, 3400 Kbps Ski (SK) - Sports - High motion 4089 Kbps 350, 600, 1100, 1800, 2550, 3250 Kbps TearsOfSteel (TOS) - Movie - Low motion 2660 Kbps 400, 550, 1050, 1500, 1950, 2400 Kbps The simulator informs the agent about the state, the action, and the immediate reward for the received segment. Using this segment-level simulator, the proposed scheme learns the neural network model within a short time. The trained neural network model is deployed on the edge server for quality adaptation of multiple clients. In the proposed scheme, the actor network of the central agent is placed on the edge server. When video streaming starts, the edge server creates the same number of instances for the actor network as the number of clients connected. The edge server detects the segment request of the client and extracts QoE-related information. The extracted information is then delivered to the actor network. The output of the instance is the bitrate maximizing individual QoE and QoE fairness at the current state. The edge server modifies the quality information of the segment request according to the output of the instance. The edge server transmits the modified segment request to the server. Upon receiving the segment request, the server transmits the segment corresponding to the requested quality to the client. 3.4. Supporting of mul

**[Acción / decisión ABR | extracto 7 | p.7]**

Journal of Network and Computer Applications 213 (2023) 103604 7 M. Kim and K. Chung Fig. 8. VMAF scores according to segment index for multiple videos. Fig. 9. Immediate reward by episodes of the Pensieve scheme. Pensieve scheme, we performed experiments to measure the changes in the immediate reward according to the episodes. The setup of the Pensieve scheme is used to learn the neural network model (Mao et al., 2017). Fig. 9 shows how the immediate reward of the Pensieve scheme changes by episodes. The measurement results confirmed that the immediate reward fluctuates abruptly for each episode. In the Pensieve scheme, the actor network depends on the expected cumulative discounted reward predicted by the critic network for policy improvement. The learning method using the state-dependent baseline is difficult to distinguish which one affects the reward between the current policy and external factors (Mao et al., 2018). The critic network updates the parameters of the neural network model to reduce the prediction error as the episode proceeds. The direction of policy improvement is wrongly determined by the prediction error at the beginning of learning. To reduce the learning variances due to the error in the statedependent baseline, the proposed scheme uses the input-dependent baseline. The multi-critic network and baseline smoothing can be used to calculate the input-dependent baseline. The multi-critic network includes multiple critic networks that experience different episodes. Each critic network calculates a state-dependent baseline for the current policy of the actor network. The actor network updates its parameters in parallel according to the state-dependent baseline calculated. The multi-critic network approach converges fast to the optimal policy. However, 

**[Acción / decisión ABR | extracto 8 | p.8]**

Journal of Network and Computer Applications 213 (2023) 103604 8 M. Kim and K. Chung Table 3 Setup for the variables used in multi-agent training. Notation Meaning Value 𝑀 Number of multiple inputs 8 𝐿 Number of bitrate levels 6 𝛾 Discounting factor 0.99 𝛼 Learning rate of actor network 0.0001 𝛼′ Learning rate of critic network 0.001 𝛽 Entropy weight 5 to 1 (80,000 episodes) 𝑁𝑟 Number of episode iterations 10 𝑁𝑎 Number of training agents 20 the episodes. The proposed scheme quickly generates the policy that maximizes individual QoE and QoE fairness through input-dependent learning. 3.6. Advantages compared with the existing schemes The proposed scheme uses reinforcement learning based on edge computing assistance. To generate the optimal adaptation policy for multiple clients, the target reward is formulated as a combination of individual QoE and QoE fairness. The QoE of each client, the QoE deviations among multiple clients, and the relationship between bitrate and quality are considered in the target reward. The proposed scheme adopts multi-agent training method to learn the neural network model. Therefore, the adaptation policy is able to determine the next video quality by recognizing multi-client competition under time-varying network conditions. In addition to collecting information about network and client, the edge server handles the neural network model to perform intelligent quality adaptation. The proposed scheme applies the concept of multiple videos and input-dependent learning to adaptation policy generation. This helps the adaptation policy to achieve high QoE in real environments. Consequently, the proposed scheme maximizes the streaming performance for multiple clients. 4. Performance evaluation In this section, we compare the proposed scheme with exist

**[Acción / decisión ABR | extracto 9 | p.9]**

Journal of Network and Computer Applications 213 (2023) 103604 9 M. Kim and K. Chung Table 5 Summary of the performance for the QoE components (BBB). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.78 0.10 0.44 Pensieve (Mao et al., 2017) 2.90 0.10 0.28 QFDVS (Altamimi and Shirmohammadi, 2020) 2.48 0.11 0.40 Proposed 2.90 0.09 0.03 playback interruptions. 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) = 1 𝑃 { 𝜖 𝑃 ∑ 𝑖=1 𝑄(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑄.𝑈 −𝛿 𝑃−1 ∑ 𝑖=1 |𝑄(𝑏𝑖+1) −𝑄(𝑏𝑖)| ⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟ 𝑆.𝑃 −𝜌 𝑃 ∑ 𝑖=1 𝑇(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑅.𝑃 } (12) Where 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) is the average QoE for all segments in the episode experienced by the 𝑘th client. 𝑄.𝑈is the quality utility aggregated for the episode. 𝑆.𝑃is the smoothness penalty calculated by using the magnitude of quality variations. 𝑅.𝑃is the re-buffering penalty determined by the playback interruption time. To evaluate the performance, we measure the average of the overall QoE for the number of clients. By improving QoE fairness, the client can utilize the bandwidth as much as needed to maximize individual QoE (Hoßfeld et al., 2016). We calculate the QoE fairness by using Jain’s Fairness Index (JFI) (Sediq et al., 2013). 𝐽(𝑄𝑜𝐸𝑖) = {∑𝑁𝑎 𝑘=1 𝑄𝑜𝐸𝑖(𝑘)}2 𝑁𝑎 ∑𝑁𝑎 𝑘=1{𝑄𝑜𝐸𝑖(𝑘)}2 (13) Where 𝐽(𝑄𝑜𝐸𝑖) is the QoE fairness for the 𝑖th segment of all clients, and 𝑄𝑜𝐸𝑖(𝑘) is the individual QoE obtained after the 𝑘th client receives the 𝑖th segment. The QoE fairness has a value within 0 and 1. The value close to 1 means that the QoE deviation among multiple clients is low. To evaluate the performance, we measure the average of the QoE fairness for the segments. 4.3. Results for a single video When receiving the BBB video, multiple clients should maintain high quality to maximize individual QoE. The unnecessary quality variations and

**[Acción / decisión ABR | extracto 10 | p.10]**

Journal of Network and Computer Applications 213 (2023) 103604 10 M. Kim and K. Chung Fig. 11. Overall QoE and QoE fairness according to the number of clients (CR). Table 7 Summary of the performance for the QoE components (TOS). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.86 0.08 0.38 Pensieve (Mao et al., 2017) 3.06 0.09 0.33 QFDVS (Altamimi and Shirmohammadi, 2020) 2.55 0.10 0.13 Proposed 3.08 0.07 0.09 number of clients increases by the aggressive adaptation policy. The QFDVS scheme generates the naive adaptation policy, so the overall QoE and the QoE fairness are low. The proposed scheme generates the conservative adaptation policy. This adaptation policy makes the client to utilize the bandwidth as much as needed, leading to the improvements of individual QoE and QoE fairness. Table 6 shows summary of the performance for the QoE components according to various schemes. The ECAA scheme has high smoothness penalty due to quality adaptation based on segment throughput. The aggressive adaptation policy of the Pensieve scheme leads to high quality utility. The QFDVS scheme has low smoothness penalty, but the re-buffering penalty increases by the conservative adaptation policy. The proposed scheme increases the quality slowly and stays long at high quality, resulting in low smoothness penalty and re-buffering penalty. The variations in VMAF scores decrease at high quality, so the differences in VMAF scores for each quality are small, even for the same segment. When receiving the TOS video, multiple clients should improve individual QoE by maintaining high quality for a long time and changing the quality gradually. Moreover, the adaptation policy should select the quality by considering situations that multiple clients oc

### 4.x Reward / QoE / función objetivo

**[Reward / QoE / función objetivo | extracto 1 | p.1]**

Journal of Network and Computer Applications 213 (2023) 103604 Available online 17 February 2023 1084-8045/© 2023 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance Minsu Kim, Kwangsue Chung ∗ Department of Electronics and Communications Engineering, Kwangwoon University, Seoul, 01897, South Korea A R T I C L E I N F O Keywords: Adaptive streaming Reinforcement learning Edge computing Quality of Experience A B S T R A C T As the number of users and the types of videos viewed increase, seamless video streaming services are becoming more important. Adaptive streaming aims to achieve high Quality of Experience (QoE) in time-varying network conditions. However, the existing schemes lack considerations for quality adaptation to improve QoE under dynamic network environments and multi-client competition. In this paper, we propose an HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance. The proposed scheme uses reinforcement learning to generate robust adaptation policy for changes in the network conditions. Edge computing plays a role of managing multiple clients based on information about the network and client. The proposed scheme considers subjective quality, multiple videos, and learning variances to advance the adaptation policy. By balancing between individual QoE and QoE fairness, the proposed scheme enables multiple clients to utilize the bandwidth as much as required. Experimental results show that the proposed scheme has better performance for individual QoE and QoE fairness than the existing schemes. 1. Introduction 

**[Reward / QoE / función objetivo | extracto 2 | p.2]**

Journal of Network and Computer Applications 213 (2023) 103604 2 M. Kim and K. Chung Fig. 1. Behavioral structure of HTTP adaptive streaming. Fig. 2. VMAF scores according to bitrates of the BBB video. • We adopt edge computing to support adaptive streaming of multiple clients sharing the same network. • We utilize reinforcement learning to generate a robust adaptation policy for dynamic network environments. • We consider subjective quality, various video characteristics, and learning variances to improve the adaptation policy. • We perform extensive experiments by using the network trace datasets based on real environments and the videos with different characteristics. The remainder of this paper is organized as follows. HTTP adaptive streaming, QoE, edge computing, and reinforcement learning are described in Section 2. The proposed scheme is presented in Section 3. In Section 4, the proposed scheme is compared with existing schemes through simulation-based experiments. Finally, the paper is concluded in Section 5. 2. Related work The process of quality adaptation performed via HTTP adaptive streaming is shown in Fig. 1. The server stores a video in the form of segments with multiple bitrates and a fixed playback length. The client executes the algorithms for quality adaptation and requests a segment from the server. When video streaming starts, the client receives a Media Presentation Description (MPD) file from the server, which includes segment information such as the encoding bitrate and position. The client predicts network conditions based on the measured segment throughput. The quality of the next segment is determined as the bitrate that maximizes QoE under the estimated network conditions (Sobhani et al., 2017; Tian and Liu, 2015). In HTTP adaptive streaming,

**[Reward / QoE / función objetivo | extracto 3 | p.3]**

Journal of Network and Computer Applications 213 (2023) 103604 3 M. Kim and K. Chung bitrate selection algorithm determines the bitrate satisfying each condition of the optimization problem as the quality of the next segment. If all conditions are not satisfied, the algorithm chooses the maximum sustainable bitrate based on the segment throughput and playback buffer level. However, when the network conditions change abruptly, the greedy-based bitrate selection algorithm suffers from QoE degradation. This kind of algorithm explores all cases to solve the optimization problem, leading to low adaptability for dynamic network environments. Edge Computing Assisted Adaptation Scheme with Machine Learning (ECAS-ML) performs intelligent quality adaptation based on edge capability and machine learning (Aguilar-Armijo et al., 2022). To achieve high QoE, the ECAS-ML scheme focuses on managing the tradeoff among bitrate, quality variations, and playback interruptions. The machine learning techniques are utilized to analyze the network conditions and predict the best parameters for heuristic algorithms. However, the ECAS-ML scheme still relies on heuristic algorithms for quality adaptation itself. Tuning the parameters has the limitations to improve overall QoE under dynamic network environments. Unlike the existing schemes, the proposed scheme in this study uses reinforcement learning rather than heuristic algorithms. The adaptation policy of the proposed scheme considers the impact of quality adaptation at each client on overall QoE. This leads to high adaptability for time-varying network conditions and variability in videos, maximizing individual QoE and QoE fairness. Reinforcement learning corrects behavior through trial and error to maximize the cumulative reward in sequential

**[Reward / QoE / función objetivo | extracto 4 | p.4]**

Journal of Network and Computer Applications 213 (2023) 103604 4 M. Kim and K. Chung Fig. 4. Overview of the input data used for multiple linear regression. of the requested quality by segments, degree of quality variations, and playback interruption time. 𝑄𝑜𝐸𝑖= 𝜖𝑄(𝑏𝑖) −𝛿|𝑄(𝑏𝑖) −𝑄(𝑏𝑖−1)| −𝜌𝑇(𝑏𝑖) (1) Where 𝑄𝑜𝐸𝑖is the individual QoE for the 𝑖th segment, and 𝑄(𝑏𝑖) means the function that indicates the relationship between the bitrate 𝑏𝑖and the quality perceived by the client. 𝑇(𝑏𝑖) is the playback interruption time that occurs after the client receives the 𝑖th segment. 𝜖, 𝛿, 𝜌are the weight parameters to combine the requested quality, quality variations, and playback interruption time. The proposed scheme defines 𝑄(𝑏𝑖) as the VMAF score for the bitrate 𝑏𝑖to consider the correlation between bitrate and quality. The Waterloo SQoE-III database is used to determine the values of the weight parameters (Duanmu et al., 2018). The information about bitrate changes due to quality adaptation, the quality perceived by the client, and the VMAF scores by bitrates exist in the Waterloo SQoEIII database. The proposed scheme performs multiple linear regression. Fig. 4 shows the input data to learn the regression model. The proposed scheme uses 80% of the total videos as the training set and the remaining 20% as the testing set. Data division and learning are iterated 1,000 times to reduce the bias occurred when the amount of training data is small. The trained regression model obtains a prediction accuracy of 79.23% for the Waterloo SQoE-III database. The values of the weight parameters are set to 0.41, 0.3, and 6.03, respectively. The proposed scheme aims to maximize the individual QoE and QoE fairness for multiple clients. The target reward of the neural network model is calculated by l

**[Reward / QoE / función objetivo | extracto 5 | p.5]**

Journal of Network and Computer Applications 213 (2023) 103604 5 M. Kim and K. Chung Fig. 5. Structure of the neural network model used in the proposed scheme. 𝜃denotes the parameters of the neural network model, 𝑡is the time step for the episode experienced by the agent, and 𝑟𝑡is the target reward at the time step 𝑡. The proposed scheme treats the time step and the segment index as the same value. 𝜋𝜃(𝑠, 𝑎) means the probability that the agent selects the action 𝑎at the state 𝑠by the policy 𝜋𝜃. 𝐴𝑑𝑣𝜋𝜃(𝑠, 𝑎) is the advantage function that determines the direction of policy improvement. The policy gradient method predicts changes in the expected cumulative discounted reward through the execution trajectories of the current policy. The agent improves the policy to increase the selection probability of the action that maximizes the expected cumulative discounted reward. After the episode ends, the neural network model aggregates the state, the action, the reward, and the policy gradient calculated. The actor network updates its parameters by considering the advantage function and the entropy for the policy. 𝜃𝐴←𝜃𝐴+ 𝛼 𝑃 ∑ 𝑡=1 ▿𝜃𝐴ln { 𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) } 𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) +𝛽▿𝜃𝐴𝐻 { 𝜋𝜃𝐴(∙|𝑠𝑡) } (6) Where 𝜃𝐴denotes the parameters of the actor network, and 𝛼is the learning rate for the actor network. 𝑠𝑡and 𝑎𝑡are the state and the action at the time step 𝑡, respectively. 𝑃means the length of the episode. 𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) is calculated as changes in the expected cumulative discounted reward due to the action determined by the current policy 𝜋𝜃𝐴and the specific action. 𝐻{𝜋𝜃𝐴(∙|𝑠𝑡)} is used to generate a good policy by sufficiently exploring the action space. The proposed scheme defines the entropy for the policy based on the selection probability of all bitrate levels. 𝛽is the entropy weight, wh

**[Reward / QoE / función objetivo | extracto 6 | p.6]**

Journal of Network and Computer Applications 213 (2023) 103604 6 M. Kim and K. Chung Table 1 Configuration of the dataset to support multiple videos. Name Types and characteristics Source bitrate Encoding bitrate BigBuckBunny (BBB) - Animation - High motion 4237 Kbps 300, 800, 1400, 2200, 3000, 3900 Kbps CostaRica (CR) - Nature - Low motion 3709 Kbps 200, 700, 1200, 2000, 2600, 3500 Kbps CSGO (CG) - Game - Average motion 3602 Kbps 500, 950, 1600, 2300, 2800, 3400 Kbps Ski (SK) - Sports - High motion 4089 Kbps 350, 600, 1100, 1800, 2550, 3250 Kbps TearsOfSteel (TOS) - Movie - Low motion 2660 Kbps 400, 550, 1050, 1500, 1950, 2400 Kbps The simulator informs the agent about the state, the action, and the immediate reward for the received segment. Using this segment-level simulator, the proposed scheme learns the neural network model within a short time. The trained neural network model is deployed on the edge server for quality adaptation of multiple clients. In the proposed scheme, the actor network of the central agent is placed on the edge server. When video streaming starts, the edge server creates the same number of instances for the actor network as the number of clients connected. The edge server detects the segment request of the client and extracts QoE-related information. The extracted information is then delivered to the actor network. The output of the instance is the bitrate maximizing individual QoE and QoE fairness at the current state. The edge server modifies the quality information of the segment request according to the output of the instance. The edge server transmits the modified segment request to the server. Upon receiving the segment request, the server transmits the segment corresponding to the requested quality to the client. 3.4. Supporting of mul

**[Reward / QoE / función objetivo | extracto 7 | p.7]**

Journal of Network and Computer Applications 213 (2023) 103604 7 M. Kim and K. Chung Fig. 8. VMAF scores according to segment index for multiple videos. Fig. 9. Immediate reward by episodes of the Pensieve scheme. Pensieve scheme, we performed experiments to measure the changes in the immediate reward according to the episodes. The setup of the Pensieve scheme is used to learn the neural network model (Mao et al., 2017). Fig. 9 shows how the immediate reward of the Pensieve scheme changes by episodes. The measurement results confirmed that the immediate reward fluctuates abruptly for each episode. In the Pensieve scheme, the actor network depends on the expected cumulative discounted reward predicted by the critic network for policy improvement. The learning method using the state-dependent baseline is difficult to distinguish which one affects the reward between the current policy and external factors (Mao et al., 2018). The critic network updates the parameters of the neural network model to reduce the prediction error as the episode proceeds. The direction of policy improvement is wrongly determined by the prediction error at the beginning of learning. To reduce the learning variances due to the error in the statedependent baseline, the proposed scheme uses the input-dependent baseline. The multi-critic network and baseline smoothing can be used to calculate the input-dependent baseline. The multi-critic network includes multiple critic networks that experience different episodes. Each critic network calculates a state-dependent baseline for the current policy of the actor network. The actor network updates its parameters in parallel according to the state-dependent baseline calculated. The multi-critic network approach converges fast to the optimal policy. However, 

**[Reward / QoE / función objetivo | extracto 8 | p.8]**

Journal of Network and Computer Applications 213 (2023) 103604 8 M. Kim and K. Chung Table 3 Setup for the variables used in multi-agent training. Notation Meaning Value 𝑀 Number of multiple inputs 8 𝐿 Number of bitrate levels 6 𝛾 Discounting factor 0.99 𝛼 Learning rate of actor network 0.0001 𝛼′ Learning rate of critic network 0.001 𝛽 Entropy weight 5 to 1 (80,000 episodes) 𝑁𝑟 Number of episode iterations 10 𝑁𝑎 Number of training agents 20 the episodes. The proposed scheme quickly generates the policy that maximizes individual QoE and QoE fairness through input-dependent learning. 3.6. Advantages compared with the existing schemes The proposed scheme uses reinforcement learning based on edge computing assistance. To generate the optimal adaptation policy for multiple clients, the target reward is formulated as a combination of individual QoE and QoE fairness. The QoE of each client, the QoE deviations among multiple clients, and the relationship between bitrate and quality are considered in the target reward. The proposed scheme adopts multi-agent training method to learn the neural network model. Therefore, the adaptation policy is able to determine the next video quality by recognizing multi-client competition under time-varying network conditions. In addition to collecting information about network and client, the edge server handles the neural network model to perform intelligent quality adaptation. The proposed scheme applies the concept of multiple videos and input-dependent learning to adaptation policy generation. This helps the adaptation policy to achieve high QoE in real environments. Consequently, the proposed scheme maximizes the streaming performance for multiple clients. 4. Performance evaluation In this section, we compare the proposed scheme with exist

**[Reward / QoE / función objetivo | extracto 9 | p.9]**

Journal of Network and Computer Applications 213 (2023) 103604 9 M. Kim and K. Chung Table 5 Summary of the performance for the QoE components (BBB). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.78 0.10 0.44 Pensieve (Mao et al., 2017) 2.90 0.10 0.28 QFDVS (Altamimi and Shirmohammadi, 2020) 2.48 0.11 0.40 Proposed 2.90 0.09 0.03 playback interruptions. 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) = 1 𝑃 { 𝜖 𝑃 ∑ 𝑖=1 𝑄(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑄.𝑈 −𝛿 𝑃−1 ∑ 𝑖=1 |𝑄(𝑏𝑖+1) −𝑄(𝑏𝑖)| ⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟ 𝑆.𝑃 −𝜌 𝑃 ∑ 𝑖=1 𝑇(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑅.𝑃 } (12) Where 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) is the average QoE for all segments in the episode experienced by the 𝑘th client. 𝑄.𝑈is the quality utility aggregated for the episode. 𝑆.𝑃is the smoothness penalty calculated by using the magnitude of quality variations. 𝑅.𝑃is the re-buffering penalty determined by the playback interruption time. To evaluate the performance, we measure the average of the overall QoE for the number of clients. By improving QoE fairness, the client can utilize the bandwidth as much as needed to maximize individual QoE (Hoßfeld et al., 2016). We calculate the QoE fairness by using Jain’s Fairness Index (JFI) (Sediq et al., 2013). 𝐽(𝑄𝑜𝐸𝑖) = {∑𝑁𝑎 𝑘=1 𝑄𝑜𝐸𝑖(𝑘)}2 𝑁𝑎 ∑𝑁𝑎 𝑘=1{𝑄𝑜𝐸𝑖(𝑘)}2 (13) Where 𝐽(𝑄𝑜𝐸𝑖) is the QoE fairness for the 𝑖th segment of all clients, and 𝑄𝑜𝐸𝑖(𝑘) is the individual QoE obtained after the 𝑘th client receives the 𝑖th segment. The QoE fairness has a value within 0 and 1. The value close to 1 means that the QoE deviation among multiple clients is low. To evaluate the performance, we measure the average of the QoE fairness for the segments. 4.3. Results for a single video When receiving the BBB video, multiple clients should maintain high quality to maximize individual QoE. The unnecessary quality variations and

**[Reward / QoE / función objetivo | extracto 10 | p.10]**

Journal of Network and Computer Applications 213 (2023) 103604 10 M. Kim and K. Chung Fig. 11. Overall QoE and QoE fairness according to the number of clients (CR). Table 7 Summary of the performance for the QoE components (TOS). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.86 0.08 0.38 Pensieve (Mao et al., 2017) 3.06 0.09 0.33 QFDVS (Altamimi and Shirmohammadi, 2020) 2.55 0.10 0.13 Proposed 3.08 0.07 0.09 number of clients increases by the aggressive adaptation policy. The QFDVS scheme generates the naive adaptation policy, so the overall QoE and the QoE fairness are low. The proposed scheme generates the conservative adaptation policy. This adaptation policy makes the client to utilize the bandwidth as much as needed, leading to the improvements of individual QoE and QoE fairness. Table 6 shows summary of the performance for the QoE components according to various schemes. The ECAA scheme has high smoothness penalty due to quality adaptation based on segment throughput. The aggressive adaptation policy of the Pensieve scheme leads to high quality utility. The QFDVS scheme has low smoothness penalty, but the re-buffering penalty increases by the conservative adaptation policy. The proposed scheme increases the quality slowly and stays long at high quality, resulting in low smoothness penalty and re-buffering penalty. The variations in VMAF scores decrease at high quality, so the differences in VMAF scores for each quality are small, even for the same segment. When receiving the TOS video, multiple clients should improve individual QoE by maintaining high quality for a long time and changing the quality gradually. Moreover, the adaptation policy should select the quality by considering situations that multiple clients oc

### 4.x Entrenamiento / learning procedure

**[Entrenamiento / learning procedure | extracto 1 | p.1]**

Journal of Network and Computer Applications 213 (2023) 103604 Available online 17 February 2023 1084-8045/© 2023 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance Minsu Kim, Kwangsue Chung ∗ Department of Electronics and Communications Engineering, Kwangwoon University, Seoul, 01897, South Korea A R T I C L E I N F O Keywords: Adaptive streaming Reinforcement learning Edge computing Quality of Experience A B S T R A C T As the number of users and the types of videos viewed increase, seamless video streaming services are becoming more important. Adaptive streaming aims to achieve high Quality of Experience (QoE) in time-varying network conditions. However, the existing schemes lack considerations for quality adaptation to improve QoE under dynamic network environments and multi-client competition. In this paper, we propose an HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance. The proposed scheme uses reinforcement learning to generate robust adaptation policy for changes in the network conditions. Edge computing plays a role of managing multiple clients based on information about the network and client. The proposed scheme considers subjective quality, multiple videos, and learning variances to advance the adaptation policy. By balancing between individual QoE and QoE fairness, the proposed scheme enables multiple clients to utilize the bandwidth as much as required. Experimental results show that the proposed scheme has better performance for individual QoE and QoE fairness than the existing schemes. 1. Introduction 

**[Entrenamiento / learning procedure | extracto 2 | p.2]**

Journal of Network and Computer Applications 213 (2023) 103604 2 M. Kim and K. Chung Fig. 1. Behavioral structure of HTTP adaptive streaming. Fig. 2. VMAF scores according to bitrates of the BBB video. • We adopt edge computing to support adaptive streaming of multiple clients sharing the same network. • We utilize reinforcement learning to generate a robust adaptation policy for dynamic network environments. • We consider subjective quality, various video characteristics, and learning variances to improve the adaptation policy. • We perform extensive experiments by using the network trace datasets based on real environments and the videos with different characteristics. The remainder of this paper is organized as follows. HTTP adaptive streaming, QoE, edge computing, and reinforcement learning are described in Section 2. The proposed scheme is presented in Section 3. In Section 4, the proposed scheme is compared with existing schemes through simulation-based experiments. Finally, the paper is concluded in Section 5. 2. Related work The process of quality adaptation performed via HTTP adaptive streaming is shown in Fig. 1. The server stores a video in the form of segments with multiple bitrates and a fixed playback length. The client executes the algorithms for quality adaptation and requests a segment from the server. When video streaming starts, the client receives a Media Presentation Description (MPD) file from the server, which includes segment information such as the encoding bitrate and position. The client predicts network conditions based on the measured segment throughput. The quality of the next segment is determined as the bitrate that maximizes QoE under the estimated network conditions (Sobhani et al., 2017; Tian and Liu, 2015). In HTTP adaptive streaming,

**[Entrenamiento / learning procedure | extracto 3 | p.3]**

Journal of Network and Computer Applications 213 (2023) 103604 3 M. Kim and K. Chung bitrate selection algorithm determines the bitrate satisfying each condition of the optimization problem as the quality of the next segment. If all conditions are not satisfied, the algorithm chooses the maximum sustainable bitrate based on the segment throughput and playback buffer level. However, when the network conditions change abruptly, the greedy-based bitrate selection algorithm suffers from QoE degradation. This kind of algorithm explores all cases to solve the optimization problem, leading to low adaptability for dynamic network environments. Edge Computing Assisted Adaptation Scheme with Machine Learning (ECAS-ML) performs intelligent quality adaptation based on edge capability and machine learning (Aguilar-Armijo et al., 2022). To achieve high QoE, the ECAS-ML scheme focuses on managing the tradeoff among bitrate, quality variations, and playback interruptions. The machine learning techniques are utilized to analyze the network conditions and predict the best parameters for heuristic algorithms. However, the ECAS-ML scheme still relies on heuristic algorithms for quality adaptation itself. Tuning the parameters has the limitations to improve overall QoE under dynamic network environments. Unlike the existing schemes, the proposed scheme in this study uses reinforcement learning rather than heuristic algorithms. The adaptation policy of the proposed scheme considers the impact of quality adaptation at each client on overall QoE. This leads to high adaptability for time-varying network conditions and variability in videos, maximizing individual QoE and QoE fairness. Reinforcement learning corrects behavior through trial and error to maximize the cumulative reward in sequential

**[Entrenamiento / learning procedure | extracto 4 | p.4]**

Journal of Network and Computer Applications 213 (2023) 103604 4 M. Kim and K. Chung Fig. 4. Overview of the input data used for multiple linear regression. of the requested quality by segments, degree of quality variations, and playback interruption time. 𝑄𝑜𝐸𝑖= 𝜖𝑄(𝑏𝑖) −𝛿|𝑄(𝑏𝑖) −𝑄(𝑏𝑖−1)| −𝜌𝑇(𝑏𝑖) (1) Where 𝑄𝑜𝐸𝑖is the individual QoE for the 𝑖th segment, and 𝑄(𝑏𝑖) means the function that indicates the relationship between the bitrate 𝑏𝑖and the quality perceived by the client. 𝑇(𝑏𝑖) is the playback interruption time that occurs after the client receives the 𝑖th segment. 𝜖, 𝛿, 𝜌are the weight parameters to combine the requested quality, quality variations, and playback interruption time. The proposed scheme defines 𝑄(𝑏𝑖) as the VMAF score for the bitrate 𝑏𝑖to consider the correlation between bitrate and quality. The Waterloo SQoE-III database is used to determine the values of the weight parameters (Duanmu et al., 2018). The information about bitrate changes due to quality adaptation, the quality perceived by the client, and the VMAF scores by bitrates exist in the Waterloo SQoEIII database. The proposed scheme performs multiple linear regression. Fig. 4 shows the input data to learn the regression model. The proposed scheme uses 80% of the total videos as the training set and the remaining 20% as the testing set. Data division and learning are iterated 1,000 times to reduce the bias occurred when the amount of training data is small. The trained regression model obtains a prediction accuracy of 79.23% for the Waterloo SQoE-III database. The values of the weight parameters are set to 0.41, 0.3, and 6.03, respectively. The proposed scheme aims to maximize the individual QoE and QoE fairness for multiple clients. The target reward of the neural network model is calculated by l

**[Entrenamiento / learning procedure | extracto 5 | p.5]**

Journal of Network and Computer Applications 213 (2023) 103604 5 M. Kim and K. Chung Fig. 5. Structure of the neural network model used in the proposed scheme. 𝜃denotes the parameters of the neural network model, 𝑡is the time step for the episode experienced by the agent, and 𝑟𝑡is the target reward at the time step 𝑡. The proposed scheme treats the time step and the segment index as the same value. 𝜋𝜃(𝑠, 𝑎) means the probability that the agent selects the action 𝑎at the state 𝑠by the policy 𝜋𝜃. 𝐴𝑑𝑣𝜋𝜃(𝑠, 𝑎) is the advantage function that determines the direction of policy improvement. The policy gradient method predicts changes in the expected cumulative discounted reward through the execution trajectories of the current policy. The agent improves the policy to increase the selection probability of the action that maximizes the expected cumulative discounted reward. After the episode ends, the neural network model aggregates the state, the action, the reward, and the policy gradient calculated. The actor network updates its parameters by considering the advantage function and the entropy for the policy. 𝜃𝐴←𝜃𝐴+ 𝛼 𝑃 ∑ 𝑡=1 ▿𝜃𝐴ln { 𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) } 𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) +𝛽▿𝜃𝐴𝐻 { 𝜋𝜃𝐴(∙|𝑠𝑡) } (6) Where 𝜃𝐴denotes the parameters of the actor network, and 𝛼is the learning rate for the actor network. 𝑠𝑡and 𝑎𝑡are the state and the action at the time step 𝑡, respectively. 𝑃means the length of the episode. 𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) is calculated as changes in the expected cumulative discounted reward due to the action determined by the current policy 𝜋𝜃𝐴and the specific action. 𝐻{𝜋𝜃𝐴(∙|𝑠𝑡)} is used to generate a good policy by sufficiently exploring the action space. The proposed scheme defines the entropy for the policy based on the selection probability of all bitrate levels. 𝛽is the entropy weight, wh

**[Entrenamiento / learning procedure | extracto 6 | p.6]**

Journal of Network and Computer Applications 213 (2023) 103604 6 M. Kim and K. Chung Table 1 Configuration of the dataset to support multiple videos. Name Types and characteristics Source bitrate Encoding bitrate BigBuckBunny (BBB) - Animation - High motion 4237 Kbps 300, 800, 1400, 2200, 3000, 3900 Kbps CostaRica (CR) - Nature - Low motion 3709 Kbps 200, 700, 1200, 2000, 2600, 3500 Kbps CSGO (CG) - Game - Average motion 3602 Kbps 500, 950, 1600, 2300, 2800, 3400 Kbps Ski (SK) - Sports - High motion 4089 Kbps 350, 600, 1100, 1800, 2550, 3250 Kbps TearsOfSteel (TOS) - Movie - Low motion 2660 Kbps 400, 550, 1050, 1500, 1950, 2400 Kbps The simulator informs the agent about the state, the action, and the immediate reward for the received segment. Using this segment-level simulator, the proposed scheme learns the neural network model within a short time. The trained neural network model is deployed on the edge server for quality adaptation of multiple clients. In the proposed scheme, the actor network of the central agent is placed on the edge server. When video streaming starts, the edge server creates the same number of instances for the actor network as the number of clients connected. The edge server detects the segment request of the client and extracts QoE-related information. The extracted information is then delivered to the actor network. The output of the instance is the bitrate maximizing individual QoE and QoE fairness at the current state. The edge server modifies the quality information of the segment request according to the output of the instance. The edge server transmits the modified segment request to the server. Upon receiving the segment request, the server transmits the segment corresponding to the requested quality to the client. 3.4. Supporting of mul

**[Entrenamiento / learning procedure | extracto 7 | p.8]**

Journal of Network and Computer Applications 213 (2023) 103604 8 M. Kim and K. Chung Table 3 Setup for the variables used in multi-agent training. Notation Meaning Value 𝑀 Number of multiple inputs 8 𝐿 Number of bitrate levels 6 𝛾 Discounting factor 0.99 𝛼 Learning rate of actor network 0.0001 𝛼′ Learning rate of critic network 0.001 𝛽 Entropy weight 5 to 1 (80,000 episodes) 𝑁𝑟 Number of episode iterations 10 𝑁𝑎 Number of training agents 20 the episodes. The proposed scheme quickly generates the policy that maximizes individual QoE and QoE fairness through input-dependent learning. 3.6. Advantages compared with the existing schemes The proposed scheme uses reinforcement learning based on edge computing assistance. To generate the optimal adaptation policy for multiple clients, the target reward is formulated as a combination of individual QoE and QoE fairness. The QoE of each client, the QoE deviations among multiple clients, and the relationship between bitrate and quality are considered in the target reward. The proposed scheme adopts multi-agent training method to learn the neural network model. Therefore, the adaptation policy is able to determine the next video quality by recognizing multi-client competition under time-varying network conditions. In addition to collecting information about network and client, the edge server handles the neural network model to perform intelligent quality adaptation. The proposed scheme applies the concept of multiple videos and input-dependent learning to adaptation policy generation. This helps the adaptation policy to achieve high QoE in real environments. Consequently, the proposed scheme maximizes the streaming performance for multiple clients. 4. Performance evaluation In this section, we compare the proposed scheme with exist

**[Entrenamiento / learning procedure | extracto 8 | p.9]**

Journal of Network and Computer Applications 213 (2023) 103604 9 M. Kim and K. Chung Table 5 Summary of the performance for the QoE components (BBB). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.78 0.10 0.44 Pensieve (Mao et al., 2017) 2.90 0.10 0.28 QFDVS (Altamimi and Shirmohammadi, 2020) 2.48 0.11 0.40 Proposed 2.90 0.09 0.03 playback interruptions. 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) = 1 𝑃 { 𝜖 𝑃 ∑ 𝑖=1 𝑄(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑄.𝑈 −𝛿 𝑃−1 ∑ 𝑖=1 |𝑄(𝑏𝑖+1) −𝑄(𝑏𝑖)| ⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟ 𝑆.𝑃 −𝜌 𝑃 ∑ 𝑖=1 𝑇(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑅.𝑃 } (12) Where 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) is the average QoE for all segments in the episode experienced by the 𝑘th client. 𝑄.𝑈is the quality utility aggregated for the episode. 𝑆.𝑃is the smoothness penalty calculated by using the magnitude of quality variations. 𝑅.𝑃is the re-buffering penalty determined by the playback interruption time. To evaluate the performance, we measure the average of the overall QoE for the number of clients. By improving QoE fairness, the client can utilize the bandwidth as much as needed to maximize individual QoE (Hoßfeld et al., 2016). We calculate the QoE fairness by using Jain’s Fairness Index (JFI) (Sediq et al., 2013). 𝐽(𝑄𝑜𝐸𝑖) = {∑𝑁𝑎 𝑘=1 𝑄𝑜𝐸𝑖(𝑘)}2 𝑁𝑎 ∑𝑁𝑎 𝑘=1{𝑄𝑜𝐸𝑖(𝑘)}2 (13) Where 𝐽(𝑄𝑜𝐸𝑖) is the QoE fairness for the 𝑖th segment of all clients, and 𝑄𝑜𝐸𝑖(𝑘) is the individual QoE obtained after the 𝑘th client receives the 𝑖th segment. The QoE fairness has a value within 0 and 1. The value close to 1 means that the QoE deviation among multiple clients is low. To evaluate the performance, we measure the average of the QoE fairness for the segments. 4.3. Results for a single video When receiving the BBB video, multiple clients should maintain high quality to maximize individual QoE. The unnecessary quality variations and

**[Entrenamiento / learning procedure | extracto 9 | p.10]**

Journal of Network and Computer Applications 213 (2023) 103604 10 M. Kim and K. Chung Fig. 11. Overall QoE and QoE fairness according to the number of clients (CR). Table 7 Summary of the performance for the QoE components (TOS). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.86 0.08 0.38 Pensieve (Mao et al., 2017) 3.06 0.09 0.33 QFDVS (Altamimi and Shirmohammadi, 2020) 2.55 0.10 0.13 Proposed 3.08 0.07 0.09 number of clients increases by the aggressive adaptation policy. The QFDVS scheme generates the naive adaptation policy, so the overall QoE and the QoE fairness are low. The proposed scheme generates the conservative adaptation policy. This adaptation policy makes the client to utilize the bandwidth as much as needed, leading to the improvements of individual QoE and QoE fairness. Table 6 shows summary of the performance for the QoE components according to various schemes. The ECAA scheme has high smoothness penalty due to quality adaptation based on segment throughput. The aggressive adaptation policy of the Pensieve scheme leads to high quality utility. The QFDVS scheme has low smoothness penalty, but the re-buffering penalty increases by the conservative adaptation policy. The proposed scheme increases the quality slowly and stays long at high quality, resulting in low smoothness penalty and re-buffering penalty. The variations in VMAF scores decrease at high quality, so the differences in VMAF scores for each quality are small, even for the same segment. When receiving the TOS video, multiple clients should improve individual QoE by maintaining high quality for a long time and changing the quality gradually. Moreover, the adaptation policy should select the quality by considering situations that multiple clients oc

### 4.x Datos / trazas / datasets / contenidos

**[Datos / trazas / datasets / contenidos | extracto 1 | p.1]**

Journal of Network and Computer Applications 213 (2023) 103604 Available online 17 February 2023 1084-8045/© 2023 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance Minsu Kim, Kwangsue Chung ∗ Department of Electronics and Communications Engineering, Kwangwoon University, Seoul, 01897, South Korea A R T I C L E I N F O Keywords: Adaptive streaming Reinforcement learning Edge computing Quality of Experience A B S T R A C T As the number of users and the types of videos viewed increase, seamless video streaming services are becoming more important. Adaptive streaming aims to achieve high Quality of Experience (QoE) in time-varying network conditions. However, the existing schemes lack considerations for quality adaptation to improve QoE under dynamic network environments and multi-client competition. In this paper, we propose an HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance. The proposed scheme uses reinforcement learning to generate robust adaptation policy for changes in the network conditions. Edge computing plays a role of managing multiple clients based on information about the network and client. The proposed scheme considers subjective quality, multiple videos, and learning variances to advance the adaptation policy. By balancing between individual QoE and QoE fairness, the proposed scheme enables multiple clients to utilize the bandwidth as much as required. Experimental results show that the proposed scheme has better performance for individual QoE and QoE fairness than the existing schemes. 1. Introduction 

**[Datos / trazas / datasets / contenidos | extracto 2 | p.2]**

Journal of Network and Computer Applications 213 (2023) 103604 2 M. Kim and K. Chung Fig. 1. Behavioral structure of HTTP adaptive streaming. Fig. 2. VMAF scores according to bitrates of the BBB video. • We adopt edge computing to support adaptive streaming of multiple clients sharing the same network. • We utilize reinforcement learning to generate a robust adaptation policy for dynamic network environments. • We consider subjective quality, various video characteristics, and learning variances to improve the adaptation policy. • We perform extensive experiments by using the network trace datasets based on real environments and the videos with different characteristics. The remainder of this paper is organized as follows. HTTP adaptive streaming, QoE, edge computing, and reinforcement learning are described in Section 2. The proposed scheme is presented in Section 3. In Section 4, the proposed scheme is compared with existing schemes through simulation-based experiments. Finally, the paper is concluded in Section 5. 2. Related work The process of quality adaptation performed via HTTP adaptive streaming is shown in Fig. 1. The server stores a video in the form of segments with multiple bitrates and a fixed playback length. The client executes the algorithms for quality adaptation and requests a segment from the server. When video streaming starts, the client receives a Media Presentation Description (MPD) file from the server, which includes segment information such as the encoding bitrate and position. The client predicts network conditions based on the measured segment throughput. The quality of the next segment is determined as the bitrate that maximizes QoE under the estimated network conditions (Sobhani et al., 2017; Tian and Liu, 2015). In HTTP adaptive streaming,

**[Datos / trazas / datasets / contenidos | extracto 3 | p.3]**

Journal of Network and Computer Applications 213 (2023) 103604 3 M. Kim and K. Chung bitrate selection algorithm determines the bitrate satisfying each condition of the optimization problem as the quality of the next segment. If all conditions are not satisfied, the algorithm chooses the maximum sustainable bitrate based on the segment throughput and playback buffer level. However, when the network conditions change abruptly, the greedy-based bitrate selection algorithm suffers from QoE degradation. This kind of algorithm explores all cases to solve the optimization problem, leading to low adaptability for dynamic network environments. Edge Computing Assisted Adaptation Scheme with Machine Learning (ECAS-ML) performs intelligent quality adaptation based on edge capability and machine learning (Aguilar-Armijo et al., 2022). To achieve high QoE, the ECAS-ML scheme focuses on managing the tradeoff among bitrate, quality variations, and playback interruptions. The machine learning techniques are utilized to analyze the network conditions and predict the best parameters for heuristic algorithms. However, the ECAS-ML scheme still relies on heuristic algorithms for quality adaptation itself. Tuning the parameters has the limitations to improve overall QoE under dynamic network environments. Unlike the existing schemes, the proposed scheme in this study uses reinforcement learning rather than heuristic algorithms. The adaptation policy of the proposed scheme considers the impact of quality adaptation at each client on overall QoE. This leads to high adaptability for time-varying network conditions and variability in videos, maximizing individual QoE and QoE fairness. Reinforcement learning corrects behavior through trial and error to maximize the cumulative reward in sequential

**[Datos / trazas / datasets / contenidos | extracto 4 | p.4]**

Journal of Network and Computer Applications 213 (2023) 103604 4 M. Kim and K. Chung Fig. 4. Overview of the input data used for multiple linear regression. of the requested quality by segments, degree of quality variations, and playback interruption time. 𝑄𝑜𝐸𝑖= 𝜖𝑄(𝑏𝑖) −𝛿|𝑄(𝑏𝑖) −𝑄(𝑏𝑖−1)| −𝜌𝑇(𝑏𝑖) (1) Where 𝑄𝑜𝐸𝑖is the individual QoE for the 𝑖th segment, and 𝑄(𝑏𝑖) means the function that indicates the relationship between the bitrate 𝑏𝑖and the quality perceived by the client. 𝑇(𝑏𝑖) is the playback interruption time that occurs after the client receives the 𝑖th segment. 𝜖, 𝛿, 𝜌are the weight parameters to combine the requested quality, quality variations, and playback interruption time. The proposed scheme defines 𝑄(𝑏𝑖) as the VMAF score for the bitrate 𝑏𝑖to consider the correlation between bitrate and quality. The Waterloo SQoE-III database is used to determine the values of the weight parameters (Duanmu et al., 2018). The information about bitrate changes due to quality adaptation, the quality perceived by the client, and the VMAF scores by bitrates exist in the Waterloo SQoEIII database. The proposed scheme performs multiple linear regression. Fig. 4 shows the input data to learn the regression model. The proposed scheme uses 80% of the total videos as the training set and the remaining 20% as the testing set. Data division and learning are iterated 1,000 times to reduce the bias occurred when the amount of training data is small. The trained regression model obtains a prediction accuracy of 79.23% for the Waterloo SQoE-III database. The values of the weight parameters are set to 0.41, 0.3, and 6.03, respectively. The proposed scheme aims to maximize the individual QoE and QoE fairness for multiple clients. The target reward of the neural network model is calculated by l

**[Datos / trazas / datasets / contenidos | extracto 5 | p.5]**

Journal of Network and Computer Applications 213 (2023) 103604 5 M. Kim and K. Chung Fig. 5. Structure of the neural network model used in the proposed scheme. 𝜃denotes the parameters of the neural network model, 𝑡is the time step for the episode experienced by the agent, and 𝑟𝑡is the target reward at the time step 𝑡. The proposed scheme treats the time step and the segment index as the same value. 𝜋𝜃(𝑠, 𝑎) means the probability that the agent selects the action 𝑎at the state 𝑠by the policy 𝜋𝜃. 𝐴𝑑𝑣𝜋𝜃(𝑠, 𝑎) is the advantage function that determines the direction of policy improvement. The policy gradient method predicts changes in the expected cumulative discounted reward through the execution trajectories of the current policy. The agent improves the policy to increase the selection probability of the action that maximizes the expected cumulative discounted reward. After the episode ends, the neural network model aggregates the state, the action, the reward, and the policy gradient calculated. The actor network updates its parameters by considering the advantage function and the entropy for the policy. 𝜃𝐴←𝜃𝐴+ 𝛼 𝑃 ∑ 𝑡=1 ▿𝜃𝐴ln { 𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) } 𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) +𝛽▿𝜃𝐴𝐻 { 𝜋𝜃𝐴(∙|𝑠𝑡) } (6) Where 𝜃𝐴denotes the parameters of the actor network, and 𝛼is the learning rate for the actor network. 𝑠𝑡and 𝑎𝑡are the state and the action at the time step 𝑡, respectively. 𝑃means the length of the episode. 𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) is calculated as changes in the expected cumulative discounted reward due to the action determined by the current policy 𝜋𝜃𝐴and the specific action. 𝐻{𝜋𝜃𝐴(∙|𝑠𝑡)} is used to generate a good policy by sufficiently exploring the action space. The proposed scheme defines the entropy for the policy based on the selection probability of all bitrate levels. 𝛽is the entropy weight, wh

**[Datos / trazas / datasets / contenidos | extracto 6 | p.6]**

Journal of Network and Computer Applications 213 (2023) 103604 6 M. Kim and K. Chung Table 1 Configuration of the dataset to support multiple videos. Name Types and characteristics Source bitrate Encoding bitrate BigBuckBunny (BBB) - Animation - High motion 4237 Kbps 300, 800, 1400, 2200, 3000, 3900 Kbps CostaRica (CR) - Nature - Low motion 3709 Kbps 200, 700, 1200, 2000, 2600, 3500 Kbps CSGO (CG) - Game - Average motion 3602 Kbps 500, 950, 1600, 2300, 2800, 3400 Kbps Ski (SK) - Sports - High motion 4089 Kbps 350, 600, 1100, 1800, 2550, 3250 Kbps TearsOfSteel (TOS) - Movie - Low motion 2660 Kbps 400, 550, 1050, 1500, 1950, 2400 Kbps The simulator informs the agent about the state, the action, and the immediate reward for the received segment. Using this segment-level simulator, the proposed scheme learns the neural network model within a short time. The trained neural network model is deployed on the edge server for quality adaptation of multiple clients. In the proposed scheme, the actor network of the central agent is placed on the edge server. When video streaming starts, the edge server creates the same number of instances for the actor network as the number of clients connected. The edge server detects the segment request of the client and extracts QoE-related information. The extracted information is then delivered to the actor network. The output of the instance is the bitrate maximizing individual QoE and QoE fairness at the current state. The edge server modifies the quality information of the segment request according to the output of the instance. The edge server transmits the modified segment request to the server. Upon receiving the segment request, the server transmits the segment corresponding to the requested quality to the client. 3.4. Supporting of mul

**[Datos / trazas / datasets / contenidos | extracto 7 | p.7]**

Journal of Network and Computer Applications 213 (2023) 103604 7 M. Kim and K. Chung Fig. 8. VMAF scores according to segment index for multiple videos. Fig. 9. Immediate reward by episodes of the Pensieve scheme. Pensieve scheme, we performed experiments to measure the changes in the immediate reward according to the episodes. The setup of the Pensieve scheme is used to learn the neural network model (Mao et al., 2017). Fig. 9 shows how the immediate reward of the Pensieve scheme changes by episodes. The measurement results confirmed that the immediate reward fluctuates abruptly for each episode. In the Pensieve scheme, the actor network depends on the expected cumulative discounted reward predicted by the critic network for policy improvement. The learning method using the state-dependent baseline is difficult to distinguish which one affects the reward between the current policy and external factors (Mao et al., 2018). The critic network updates the parameters of the neural network model to reduce the prediction error as the episode proceeds. The direction of policy improvement is wrongly determined by the prediction error at the beginning of learning. To reduce the learning variances due to the error in the statedependent baseline, the proposed scheme uses the input-dependent baseline. The multi-critic network and baseline smoothing can be used to calculate the input-dependent baseline. The multi-critic network includes multiple critic networks that experience different episodes. Each critic network calculates a state-dependent baseline for the current policy of the actor network. The actor network updates its parameters in parallel according to the state-dependent baseline calculated. The multi-critic network approach converges fast to the optimal policy. However, 

**[Datos / trazas / datasets / contenidos | extracto 8 | p.8]**

Journal of Network and Computer Applications 213 (2023) 103604 8 M. Kim and K. Chung Table 3 Setup for the variables used in multi-agent training. Notation Meaning Value 𝑀 Number of multiple inputs 8 𝐿 Number of bitrate levels 6 𝛾 Discounting factor 0.99 𝛼 Learning rate of actor network 0.0001 𝛼′ Learning rate of critic network 0.001 𝛽 Entropy weight 5 to 1 (80,000 episodes) 𝑁𝑟 Number of episode iterations 10 𝑁𝑎 Number of training agents 20 the episodes. The proposed scheme quickly generates the policy that maximizes individual QoE and QoE fairness through input-dependent learning. 3.6. Advantages compared with the existing schemes The proposed scheme uses reinforcement learning based on edge computing assistance. To generate the optimal adaptation policy for multiple clients, the target reward is formulated as a combination of individual QoE and QoE fairness. The QoE of each client, the QoE deviations among multiple clients, and the relationship between bitrate and quality are considered in the target reward. The proposed scheme adopts multi-agent training method to learn the neural network model. Therefore, the adaptation policy is able to determine the next video quality by recognizing multi-client competition under time-varying network conditions. In addition to collecting information about network and client, the edge server handles the neural network model to perform intelligent quality adaptation. The proposed scheme applies the concept of multiple videos and input-dependent learning to adaptation policy generation. This helps the adaptation policy to achieve high QoE in real environments. Consequently, the proposed scheme maximizes the streaming performance for multiple clients. 4. Performance evaluation In this section, we compare the proposed scheme with exist

**[Datos / trazas / datasets / contenidos | extracto 9 | p.9]**

Journal of Network and Computer Applications 213 (2023) 103604 9 M. Kim and K. Chung Table 5 Summary of the performance for the QoE components (BBB). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.78 0.10 0.44 Pensieve (Mao et al., 2017) 2.90 0.10 0.28 QFDVS (Altamimi and Shirmohammadi, 2020) 2.48 0.11 0.40 Proposed 2.90 0.09 0.03 playback interruptions. 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) = 1 𝑃 { 𝜖 𝑃 ∑ 𝑖=1 𝑄(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑄.𝑈 −𝛿 𝑃−1 ∑ 𝑖=1 |𝑄(𝑏𝑖+1) −𝑄(𝑏𝑖)| ⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟ 𝑆.𝑃 −𝜌 𝑃 ∑ 𝑖=1 𝑇(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑅.𝑃 } (12) Where 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) is the average QoE for all segments in the episode experienced by the 𝑘th client. 𝑄.𝑈is the quality utility aggregated for the episode. 𝑆.𝑃is the smoothness penalty calculated by using the magnitude of quality variations. 𝑅.𝑃is the re-buffering penalty determined by the playback interruption time. To evaluate the performance, we measure the average of the overall QoE for the number of clients. By improving QoE fairness, the client can utilize the bandwidth as much as needed to maximize individual QoE (Hoßfeld et al., 2016). We calculate the QoE fairness by using Jain’s Fairness Index (JFI) (Sediq et al., 2013). 𝐽(𝑄𝑜𝐸𝑖) = {∑𝑁𝑎 𝑘=1 𝑄𝑜𝐸𝑖(𝑘)}2 𝑁𝑎 ∑𝑁𝑎 𝑘=1{𝑄𝑜𝐸𝑖(𝑘)}2 (13) Where 𝐽(𝑄𝑜𝐸𝑖) is the QoE fairness for the 𝑖th segment of all clients, and 𝑄𝑜𝐸𝑖(𝑘) is the individual QoE obtained after the 𝑘th client receives the 𝑖th segment. The QoE fairness has a value within 0 and 1. The value close to 1 means that the QoE deviation among multiple clients is low. To evaluate the performance, we measure the average of the QoE fairness for the segments. 4.3. Results for a single video When receiving the BBB video, multiple clients should maintain high quality to maximize individual QoE. The unnecessary quality variations and

**[Datos / trazas / datasets / contenidos | extracto 10 | p.10]**

Journal of Network and Computer Applications 213 (2023) 103604 10 M. Kim and K. Chung Fig. 11. Overall QoE and QoE fairness according to the number of clients (CR). Table 7 Summary of the performance for the QoE components (TOS). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.86 0.08 0.38 Pensieve (Mao et al., 2017) 3.06 0.09 0.33 QFDVS (Altamimi and Shirmohammadi, 2020) 2.55 0.10 0.13 Proposed 3.08 0.07 0.09 number of clients increases by the aggressive adaptation policy. The QFDVS scheme generates the naive adaptation policy, so the overall QoE and the QoE fairness are low. The proposed scheme generates the conservative adaptation policy. This adaptation policy makes the client to utilize the bandwidth as much as needed, leading to the improvements of individual QoE and QoE fairness. Table 6 shows summary of the performance for the QoE components according to various schemes. The ECAA scheme has high smoothness penalty due to quality adaptation based on segment throughput. The aggressive adaptation policy of the Pensieve scheme leads to high quality utility. The QFDVS scheme has low smoothness penalty, but the re-buffering penalty increases by the conservative adaptation policy. The proposed scheme increases the quality slowly and stays long at high quality, resulting in low smoothness penalty and re-buffering penalty. The variations in VMAF scores decrease at high quality, so the differences in VMAF scores for each quality are small, even for the same segment. When receiving the TOS video, multiple clients should improve individual QoE by maintaining high quality for a long time and changing the quality gradually. Moreover, the adaptation policy should select the quality by considering situations that multiple clients oc

### 4.x Evaluación / baselines / experimentos

**[Evaluación / baselines / experimentos | extracto 1 | p.1]**

Journal of Network and Computer Applications 213 (2023) 103604 Available online 17 February 2023 1084-8045/© 2023 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance Minsu Kim, Kwangsue Chung ∗ Department of Electronics and Communications Engineering, Kwangwoon University, Seoul, 01897, South Korea A R T I C L E I N F O Keywords: Adaptive streaming Reinforcement learning Edge computing Quality of Experience A B S T R A C T As the number of users and the types of videos viewed increase, seamless video streaming services are becoming more important. Adaptive streaming aims to achieve high Quality of Experience (QoE) in time-varying network conditions. However, the existing schemes lack considerations for quality adaptation to improve QoE under dynamic network environments and multi-client competition. In this paper, we propose an HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance. The proposed scheme uses reinforcement learning to generate robust adaptation policy for changes in the network conditions. Edge computing plays a role of managing multiple clients based on information about the network and client. The proposed scheme considers subjective quality, multiple videos, and learning variances to advance the adaptation policy. By balancing between individual QoE and QoE fairness, the proposed scheme enables multiple clients to utilize the bandwidth as much as required. Experimental results show that the proposed scheme has better performance for individual QoE and QoE fairness than the existing schemes. 1. Introduction 

**[Evaluación / baselines / experimentos | extracto 2 | p.2]**

Journal of Network and Computer Applications 213 (2023) 103604 2 M. Kim and K. Chung Fig. 1. Behavioral structure of HTTP adaptive streaming. Fig. 2. VMAF scores according to bitrates of the BBB video. • We adopt edge computing to support adaptive streaming of multiple clients sharing the same network. • We utilize reinforcement learning to generate a robust adaptation policy for dynamic network environments. • We consider subjective quality, various video characteristics, and learning variances to improve the adaptation policy. • We perform extensive experiments by using the network trace datasets based on real environments and the videos with different characteristics. The remainder of this paper is organized as follows. HTTP adaptive streaming, QoE, edge computing, and reinforcement learning are described in Section 2. The proposed scheme is presented in Section 3. In Section 4, the proposed scheme is compared with existing schemes through simulation-based experiments. Finally, the paper is concluded in Section 5. 2. Related work The process of quality adaptation performed via HTTP adaptive streaming is shown in Fig. 1. The server stores a video in the form of segments with multiple bitrates and a fixed playback length. The client executes the algorithms for quality adaptation and requests a segment from the server. When video streaming starts, the client receives a Media Presentation Description (MPD) file from the server, which includes segment information such as the encoding bitrate and position. The client predicts network conditions based on the measured segment throughput. The quality of the next segment is determined as the bitrate that maximizes QoE under the estimated network conditions (Sobhani et al., 2017; Tian and Liu, 2015). In HTTP adaptive streaming,

**[Evaluación / baselines / experimentos | extracto 3 | p.3]**

Journal of Network and Computer Applications 213 (2023) 103604 3 M. Kim and K. Chung bitrate selection algorithm determines the bitrate satisfying each condition of the optimization problem as the quality of the next segment. If all conditions are not satisfied, the algorithm chooses the maximum sustainable bitrate based on the segment throughput and playback buffer level. However, when the network conditions change abruptly, the greedy-based bitrate selection algorithm suffers from QoE degradation. This kind of algorithm explores all cases to solve the optimization problem, leading to low adaptability for dynamic network environments. Edge Computing Assisted Adaptation Scheme with Machine Learning (ECAS-ML) performs intelligent quality adaptation based on edge capability and machine learning (Aguilar-Armijo et al., 2022). To achieve high QoE, the ECAS-ML scheme focuses on managing the tradeoff among bitrate, quality variations, and playback interruptions. The machine learning techniques are utilized to analyze the network conditions and predict the best parameters for heuristic algorithms. However, the ECAS-ML scheme still relies on heuristic algorithms for quality adaptation itself. Tuning the parameters has the limitations to improve overall QoE under dynamic network environments. Unlike the existing schemes, the proposed scheme in this study uses reinforcement learning rather than heuristic algorithms. The adaptation policy of the proposed scheme considers the impact of quality adaptation at each client on overall QoE. This leads to high adaptability for time-varying network conditions and variability in videos, maximizing individual QoE and QoE fairness. Reinforcement learning corrects behavior through trial and error to maximize the cumulative reward in sequential

**[Evaluación / baselines / experimentos | extracto 4 | p.4]**

Journal of Network and Computer Applications 213 (2023) 103604 4 M. Kim and K. Chung Fig. 4. Overview of the input data used for multiple linear regression. of the requested quality by segments, degree of quality variations, and playback interruption time. 𝑄𝑜𝐸𝑖= 𝜖𝑄(𝑏𝑖) −𝛿|𝑄(𝑏𝑖) −𝑄(𝑏𝑖−1)| −𝜌𝑇(𝑏𝑖) (1) Where 𝑄𝑜𝐸𝑖is the individual QoE for the 𝑖th segment, and 𝑄(𝑏𝑖) means the function that indicates the relationship between the bitrate 𝑏𝑖and the quality perceived by the client. 𝑇(𝑏𝑖) is the playback interruption time that occurs after the client receives the 𝑖th segment. 𝜖, 𝛿, 𝜌are the weight parameters to combine the requested quality, quality variations, and playback interruption time. The proposed scheme defines 𝑄(𝑏𝑖) as the VMAF score for the bitrate 𝑏𝑖to consider the correlation between bitrate and quality. The Waterloo SQoE-III database is used to determine the values of the weight parameters (Duanmu et al., 2018). The information about bitrate changes due to quality adaptation, the quality perceived by the client, and the VMAF scores by bitrates exist in the Waterloo SQoEIII database. The proposed scheme performs multiple linear regression. Fig. 4 shows the input data to learn the regression model. The proposed scheme uses 80% of the total videos as the training set and the remaining 20% as the testing set. Data division and learning are iterated 1,000 times to reduce the bias occurred when the amount of training data is small. The trained regression model obtains a prediction accuracy of 79.23% for the Waterloo SQoE-III database. The values of the weight parameters are set to 0.41, 0.3, and 6.03, respectively. The proposed scheme aims to maximize the individual QoE and QoE fairness for multiple clients. The target reward of the neural network model is calculated by l

**[Evaluación / baselines / experimentos | extracto 5 | p.5]**

Journal of Network and Computer Applications 213 (2023) 103604 5 M. Kim and K. Chung Fig. 5. Structure of the neural network model used in the proposed scheme. 𝜃denotes the parameters of the neural network model, 𝑡is the time step for the episode experienced by the agent, and 𝑟𝑡is the target reward at the time step 𝑡. The proposed scheme treats the time step and the segment index as the same value. 𝜋𝜃(𝑠, 𝑎) means the probability that the agent selects the action 𝑎at the state 𝑠by the policy 𝜋𝜃. 𝐴𝑑𝑣𝜋𝜃(𝑠, 𝑎) is the advantage function that determines the direction of policy improvement. The policy gradient method predicts changes in the expected cumulative discounted reward through the execution trajectories of the current policy. The agent improves the policy to increase the selection probability of the action that maximizes the expected cumulative discounted reward. After the episode ends, the neural network model aggregates the state, the action, the reward, and the policy gradient calculated. The actor network updates its parameters by considering the advantage function and the entropy for the policy. 𝜃𝐴←𝜃𝐴+ 𝛼 𝑃 ∑ 𝑡=1 ▿𝜃𝐴ln { 𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) } 𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) +𝛽▿𝜃𝐴𝐻 { 𝜋𝜃𝐴(∙|𝑠𝑡) } (6) Where 𝜃𝐴denotes the parameters of the actor network, and 𝛼is the learning rate for the actor network. 𝑠𝑡and 𝑎𝑡are the state and the action at the time step 𝑡, respectively. 𝑃means the length of the episode. 𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) is calculated as changes in the expected cumulative discounted reward due to the action determined by the current policy 𝜋𝜃𝐴and the specific action. 𝐻{𝜋𝜃𝐴(∙|𝑠𝑡)} is used to generate a good policy by sufficiently exploring the action space. The proposed scheme defines the entropy for the policy based on the selection probability of all bitrate levels. 𝛽is the entropy weight, wh

**[Evaluación / baselines / experimentos | extracto 6 | p.6]**

Journal of Network and Computer Applications 213 (2023) 103604 6 M. Kim and K. Chung Table 1 Configuration of the dataset to support multiple videos. Name Types and characteristics Source bitrate Encoding bitrate BigBuckBunny (BBB) - Animation - High motion 4237 Kbps 300, 800, 1400, 2200, 3000, 3900 Kbps CostaRica (CR) - Nature - Low motion 3709 Kbps 200, 700, 1200, 2000, 2600, 3500 Kbps CSGO (CG) - Game - Average motion 3602 Kbps 500, 950, 1600, 2300, 2800, 3400 Kbps Ski (SK) - Sports - High motion 4089 Kbps 350, 600, 1100, 1800, 2550, 3250 Kbps TearsOfSteel (TOS) - Movie - Low motion 2660 Kbps 400, 550, 1050, 1500, 1950, 2400 Kbps The simulator informs the agent about the state, the action, and the immediate reward for the received segment. Using this segment-level simulator, the proposed scheme learns the neural network model within a short time. The trained neural network model is deployed on the edge server for quality adaptation of multiple clients. In the proposed scheme, the actor network of the central agent is placed on the edge server. When video streaming starts, the edge server creates the same number of instances for the actor network as the number of clients connected. The edge server detects the segment request of the client and extracts QoE-related information. The extracted information is then delivered to the actor network. The output of the instance is the bitrate maximizing individual QoE and QoE fairness at the current state. The edge server modifies the quality information of the segment request according to the output of the instance. The edge server transmits the modified segment request to the server. Upon receiving the segment request, the server transmits the segment corresponding to the requested quality to the client. 3.4. Supporting of mul

**[Evaluación / baselines / experimentos | extracto 7 | p.7]**

Journal of Network and Computer Applications 213 (2023) 103604 7 M. Kim and K. Chung Fig. 8. VMAF scores according to segment index for multiple videos. Fig. 9. Immediate reward by episodes of the Pensieve scheme. Pensieve scheme, we performed experiments to measure the changes in the immediate reward according to the episodes. The setup of the Pensieve scheme is used to learn the neural network model (Mao et al., 2017). Fig. 9 shows how the immediate reward of the Pensieve scheme changes by episodes. The measurement results confirmed that the immediate reward fluctuates abruptly for each episode. In the Pensieve scheme, the actor network depends on the expected cumulative discounted reward predicted by the critic network for policy improvement. The learning method using the state-dependent baseline is difficult to distinguish which one affects the reward between the current policy and external factors (Mao et al., 2018). The critic network updates the parameters of the neural network model to reduce the prediction error as the episode proceeds. The direction of policy improvement is wrongly determined by the prediction error at the beginning of learning. To reduce the learning variances due to the error in the statedependent baseline, the proposed scheme uses the input-dependent baseline. The multi-critic network and baseline smoothing can be used to calculate the input-dependent baseline. The multi-critic network includes multiple critic networks that experience different episodes. Each critic network calculates a state-dependent baseline for the current policy of the actor network. The actor network updates its parameters in parallel according to the state-dependent baseline calculated. The multi-critic network approach converges fast to the optimal policy. However, 

**[Evaluación / baselines / experimentos | extracto 8 | p.8]**

Journal of Network and Computer Applications 213 (2023) 103604 8 M. Kim and K. Chung Table 3 Setup for the variables used in multi-agent training. Notation Meaning Value 𝑀 Number of multiple inputs 8 𝐿 Number of bitrate levels 6 𝛾 Discounting factor 0.99 𝛼 Learning rate of actor network 0.0001 𝛼′ Learning rate of critic network 0.001 𝛽 Entropy weight 5 to 1 (80,000 episodes) 𝑁𝑟 Number of episode iterations 10 𝑁𝑎 Number of training agents 20 the episodes. The proposed scheme quickly generates the policy that maximizes individual QoE and QoE fairness through input-dependent learning. 3.6. Advantages compared with the existing schemes The proposed scheme uses reinforcement learning based on edge computing assistance. To generate the optimal adaptation policy for multiple clients, the target reward is formulated as a combination of individual QoE and QoE fairness. The QoE of each client, the QoE deviations among multiple clients, and the relationship between bitrate and quality are considered in the target reward. The proposed scheme adopts multi-agent training method to learn the neural network model. Therefore, the adaptation policy is able to determine the next video quality by recognizing multi-client competition under time-varying network conditions. In addition to collecting information about network and client, the edge server handles the neural network model to perform intelligent quality adaptation. The proposed scheme applies the concept of multiple videos and input-dependent learning to adaptation policy generation. This helps the adaptation policy to achieve high QoE in real environments. Consequently, the proposed scheme maximizes the streaming performance for multiple clients. 4. Performance evaluation In this section, we compare the proposed scheme with exist

**[Evaluación / baselines / experimentos | extracto 9 | p.9]**

Journal of Network and Computer Applications 213 (2023) 103604 9 M. Kim and K. Chung Table 5 Summary of the performance for the QoE components (BBB). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.78 0.10 0.44 Pensieve (Mao et al., 2017) 2.90 0.10 0.28 QFDVS (Altamimi and Shirmohammadi, 2020) 2.48 0.11 0.40 Proposed 2.90 0.09 0.03 playback interruptions. 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) = 1 𝑃 { 𝜖 𝑃 ∑ 𝑖=1 𝑄(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑄.𝑈 −𝛿 𝑃−1 ∑ 𝑖=1 |𝑄(𝑏𝑖+1) −𝑄(𝑏𝑖)| ⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟ 𝑆.𝑃 −𝜌 𝑃 ∑ 𝑖=1 𝑇(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑅.𝑃 } (12) Where 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) is the average QoE for all segments in the episode experienced by the 𝑘th client. 𝑄.𝑈is the quality utility aggregated for the episode. 𝑆.𝑃is the smoothness penalty calculated by using the magnitude of quality variations. 𝑅.𝑃is the re-buffering penalty determined by the playback interruption time. To evaluate the performance, we measure the average of the overall QoE for the number of clients. By improving QoE fairness, the client can utilize the bandwidth as much as needed to maximize individual QoE (Hoßfeld et al., 2016). We calculate the QoE fairness by using Jain’s Fairness Index (JFI) (Sediq et al., 2013). 𝐽(𝑄𝑜𝐸𝑖) = {∑𝑁𝑎 𝑘=1 𝑄𝑜𝐸𝑖(𝑘)}2 𝑁𝑎 ∑𝑁𝑎 𝑘=1{𝑄𝑜𝐸𝑖(𝑘)}2 (13) Where 𝐽(𝑄𝑜𝐸𝑖) is the QoE fairness for the 𝑖th segment of all clients, and 𝑄𝑜𝐸𝑖(𝑘) is the individual QoE obtained after the 𝑘th client receives the 𝑖th segment. The QoE fairness has a value within 0 and 1. The value close to 1 means that the QoE deviation among multiple clients is low. To evaluate the performance, we measure the average of the QoE fairness for the segments. 4.3. Results for a single video When receiving the BBB video, multiple clients should maintain high quality to maximize individual QoE. The unnecessary quality variations and

**[Evaluación / baselines / experimentos | extracto 10 | p.10]**

Journal of Network and Computer Applications 213 (2023) 103604 10 M. Kim and K. Chung Fig. 11. Overall QoE and QoE fairness according to the number of clients (CR). Table 7 Summary of the performance for the QoE components (TOS). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.86 0.08 0.38 Pensieve (Mao et al., 2017) 3.06 0.09 0.33 QFDVS (Altamimi and Shirmohammadi, 2020) 2.55 0.10 0.13 Proposed 3.08 0.07 0.09 number of clients increases by the aggressive adaptation policy. The QFDVS scheme generates the naive adaptation policy, so the overall QoE and the QoE fairness are low. The proposed scheme generates the conservative adaptation policy. This adaptation policy makes the client to utilize the bandwidth as much as needed, leading to the improvements of individual QoE and QoE fairness. Table 6 shows summary of the performance for the QoE components according to various schemes. The ECAA scheme has high smoothness penalty due to quality adaptation based on segment throughput. The aggressive adaptation policy of the Pensieve scheme leads to high quality utility. The QFDVS scheme has low smoothness penalty, but the re-buffering penalty increases by the conservative adaptation policy. The proposed scheme increases the quality slowly and stays long at high quality, resulting in low smoothness penalty and re-buffering penalty. The variations in VMAF scores decrease at high quality, so the differences in VMAF scores for each quality are small, even for the same segment. When receiving the TOS video, multiple clients should improve individual QoE by maintaining high quality for a long time and changing the quality gradually. Moreover, the adaptation policy should select the quality by considering situations that multiple clients oc

### 4.x Limitaciones / riesgos / aplicabilidad

**[Limitaciones / riesgos / aplicabilidad | extracto 1 | p.1]**

Journal of Network and Computer Applications 213 (2023) 103604 Available online 17 February 2023 1084-8045/© 2023 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance Minsu Kim, Kwangsue Chung ∗ Department of Electronics and Communications Engineering, Kwangwoon University, Seoul, 01897, South Korea A R T I C L E I N F O Keywords: Adaptive streaming Reinforcement learning Edge computing Quality of Experience A B S T R A C T As the number of users and the types of videos viewed increase, seamless video streaming services are becoming more important. Adaptive streaming aims to achieve high Quality of Experience (QoE) in time-varying network conditions. However, the existing schemes lack considerations for quality adaptation to improve QoE under dynamic network environments and multi-client competition. In this paper, we propose an HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance. The proposed scheme uses reinforcement learning to generate robust adaptation policy for changes in the network conditions. Edge computing plays a role of managing multiple clients based on information about the network and client. The proposed scheme considers subjective quality, multiple videos, and learning variances to advance the adaptation policy. By balancing between individual QoE and QoE fairness, the proposed scheme enables multiple clients to utilize the bandwidth as much as required. Experimental results show that the proposed scheme has better performance for individual QoE and QoE fairness than the existing schemes. 1. Introduction 

**[Limitaciones / riesgos / aplicabilidad | extracto 2 | p.2]**

Journal of Network and Computer Applications 213 (2023) 103604 2 M. Kim and K. Chung Fig. 1. Behavioral structure of HTTP adaptive streaming. Fig. 2. VMAF scores according to bitrates of the BBB video. • We adopt edge computing to support adaptive streaming of multiple clients sharing the same network. • We utilize reinforcement learning to generate a robust adaptation policy for dynamic network environments. • We consider subjective quality, various video characteristics, and learning variances to improve the adaptation policy. • We perform extensive experiments by using the network trace datasets based on real environments and the videos with different characteristics. The remainder of this paper is organized as follows. HTTP adaptive streaming, QoE, edge computing, and reinforcement learning are described in Section 2. The proposed scheme is presented in Section 3. In Section 4, the proposed scheme is compared with existing schemes through simulation-based experiments. Finally, the paper is concluded in Section 5. 2. Related work The process of quality adaptation performed via HTTP adaptive streaming is shown in Fig. 1. The server stores a video in the form of segments with multiple bitrates and a fixed playback length. The client executes the algorithms for quality adaptation and requests a segment from the server. When video streaming starts, the client receives a Media Presentation Description (MPD) file from the server, which includes segment information such as the encoding bitrate and position. The client predicts network conditions based on the measured segment throughput. The quality of the next segment is determined as the bitrate that maximizes QoE under the estimated network conditions (Sobhani et al., 2017; Tian and Liu, 2015). In HTTP adaptive streaming,

**[Limitaciones / riesgos / aplicabilidad | extracto 3 | p.3]**

Journal of Network and Computer Applications 213 (2023) 103604 3 M. Kim and K. Chung bitrate selection algorithm determines the bitrate satisfying each condition of the optimization problem as the quality of the next segment. If all conditions are not satisfied, the algorithm chooses the maximum sustainable bitrate based on the segment throughput and playback buffer level. However, when the network conditions change abruptly, the greedy-based bitrate selection algorithm suffers from QoE degradation. This kind of algorithm explores all cases to solve the optimization problem, leading to low adaptability for dynamic network environments. Edge Computing Assisted Adaptation Scheme with Machine Learning (ECAS-ML) performs intelligent quality adaptation based on edge capability and machine learning (Aguilar-Armijo et al., 2022). To achieve high QoE, the ECAS-ML scheme focuses on managing the tradeoff among bitrate, quality variations, and playback interruptions. The machine learning techniques are utilized to analyze the network conditions and predict the best parameters for heuristic algorithms. However, the ECAS-ML scheme still relies on heuristic algorithms for quality adaptation itself. Tuning the parameters has the limitations to improve overall QoE under dynamic network environments. Unlike the existing schemes, the proposed scheme in this study uses reinforcement learning rather than heuristic algorithms. The adaptation policy of the proposed scheme considers the impact of quality adaptation at each client on overall QoE. This leads to high adaptability for time-varying network conditions and variability in videos, maximizing individual QoE and QoE fairness. Reinforcement learning corrects behavior through trial and error to maximize the cumulative reward in sequential

**[Limitaciones / riesgos / aplicabilidad | extracto 4 | p.4]**

Journal of Network and Computer Applications 213 (2023) 103604 4 M. Kim and K. Chung Fig. 4. Overview of the input data used for multiple linear regression. of the requested quality by segments, degree of quality variations, and playback interruption time. 𝑄𝑜𝐸𝑖= 𝜖𝑄(𝑏𝑖) −𝛿|𝑄(𝑏𝑖) −𝑄(𝑏𝑖−1)| −𝜌𝑇(𝑏𝑖) (1) Where 𝑄𝑜𝐸𝑖is the individual QoE for the 𝑖th segment, and 𝑄(𝑏𝑖) means the function that indicates the relationship between the bitrate 𝑏𝑖and the quality perceived by the client. 𝑇(𝑏𝑖) is the playback interruption time that occurs after the client receives the 𝑖th segment. 𝜖, 𝛿, 𝜌are the weight parameters to combine the requested quality, quality variations, and playback interruption time. The proposed scheme defines 𝑄(𝑏𝑖) as the VMAF score for the bitrate 𝑏𝑖to consider the correlation between bitrate and quality. The Waterloo SQoE-III database is used to determine the values of the weight parameters (Duanmu et al., 2018). The information about bitrate changes due to quality adaptation, the quality perceived by the client, and the VMAF scores by bitrates exist in the Waterloo SQoEIII database. The proposed scheme performs multiple linear regression. Fig. 4 shows the input data to learn the regression model. The proposed scheme uses 80% of the total videos as the training set and the remaining 20% as the testing set. Data division and learning are iterated 1,000 times to reduce the bias occurred when the amount of training data is small. The trained regression model obtains a prediction accuracy of 79.23% for the Waterloo SQoE-III database. The values of the weight parameters are set to 0.41, 0.3, and 6.03, respectively. The proposed scheme aims to maximize the individual QoE and QoE fairness for multiple clients. The target reward of the neural network model is calculated by l

**[Limitaciones / riesgos / aplicabilidad | extracto 5 | p.5]**

Journal of Network and Computer Applications 213 (2023) 103604 5 M. Kim and K. Chung Fig. 5. Structure of the neural network model used in the proposed scheme. 𝜃denotes the parameters of the neural network model, 𝑡is the time step for the episode experienced by the agent, and 𝑟𝑡is the target reward at the time step 𝑡. The proposed scheme treats the time step and the segment index as the same value. 𝜋𝜃(𝑠, 𝑎) means the probability that the agent selects the action 𝑎at the state 𝑠by the policy 𝜋𝜃. 𝐴𝑑𝑣𝜋𝜃(𝑠, 𝑎) is the advantage function that determines the direction of policy improvement. The policy gradient method predicts changes in the expected cumulative discounted reward through the execution trajectories of the current policy. The agent improves the policy to increase the selection probability of the action that maximizes the expected cumulative discounted reward. After the episode ends, the neural network model aggregates the state, the action, the reward, and the policy gradient calculated. The actor network updates its parameters by considering the advantage function and the entropy for the policy. 𝜃𝐴←𝜃𝐴+ 𝛼 𝑃 ∑ 𝑡=1 ▿𝜃𝐴ln { 𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) } 𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) +𝛽▿𝜃𝐴𝐻 { 𝜋𝜃𝐴(∙|𝑠𝑡) } (6) Where 𝜃𝐴denotes the parameters of the actor network, and 𝛼is the learning rate for the actor network. 𝑠𝑡and 𝑎𝑡are the state and the action at the time step 𝑡, respectively. 𝑃means the length of the episode. 𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) is calculated as changes in the expected cumulative discounted reward due to the action determined by the current policy 𝜋𝜃𝐴and the specific action. 𝐻{𝜋𝜃𝐴(∙|𝑠𝑡)} is used to generate a good policy by sufficiently exploring the action space. The proposed scheme defines the entropy for the policy based on the selection probability of all bitrate levels. 𝛽is the entropy weight, wh

**[Limitaciones / riesgos / aplicabilidad | extracto 6 | p.6]**

Journal of Network and Computer Applications 213 (2023) 103604 6 M. Kim and K. Chung Table 1 Configuration of the dataset to support multiple videos. Name Types and characteristics Source bitrate Encoding bitrate BigBuckBunny (BBB) - Animation - High motion 4237 Kbps 300, 800, 1400, 2200, 3000, 3900 Kbps CostaRica (CR) - Nature - Low motion 3709 Kbps 200, 700, 1200, 2000, 2600, 3500 Kbps CSGO (CG) - Game - Average motion 3602 Kbps 500, 950, 1600, 2300, 2800, 3400 Kbps Ski (SK) - Sports - High motion 4089 Kbps 350, 600, 1100, 1800, 2550, 3250 Kbps TearsOfSteel (TOS) - Movie - Low motion 2660 Kbps 400, 550, 1050, 1500, 1950, 2400 Kbps The simulator informs the agent about the state, the action, and the immediate reward for the received segment. Using this segment-level simulator, the proposed scheme learns the neural network model within a short time. The trained neural network model is deployed on the edge server for quality adaptation of multiple clients. In the proposed scheme, the actor network of the central agent is placed on the edge server. When video streaming starts, the edge server creates the same number of instances for the actor network as the number of clients connected. The edge server detects the segment request of the client and extracts QoE-related information. The extracted information is then delivered to the actor network. The output of the instance is the bitrate maximizing individual QoE and QoE fairness at the current state. The edge server modifies the quality information of the segment request according to the output of the instance. The edge server transmits the modified segment request to the server. Upon receiving the segment request, the server transmits the segment corresponding to the requested quality to the client. 3.4. Supporting of mul

**[Limitaciones / riesgos / aplicabilidad | extracto 7 | p.7]**

Journal of Network and Computer Applications 213 (2023) 103604 7 M. Kim and K. Chung Fig. 8. VMAF scores according to segment index for multiple videos. Fig. 9. Immediate reward by episodes of the Pensieve scheme. Pensieve scheme, we performed experiments to measure the changes in the immediate reward according to the episodes. The setup of the Pensieve scheme is used to learn the neural network model (Mao et al., 2017). Fig. 9 shows how the immediate reward of the Pensieve scheme changes by episodes. The measurement results confirmed that the immediate reward fluctuates abruptly for each episode. In the Pensieve scheme, the actor network depends on the expected cumulative discounted reward predicted by the critic network for policy improvement. The learning method using the state-dependent baseline is difficult to distinguish which one affects the reward between the current policy and external factors (Mao et al., 2018). The critic network updates the parameters of the neural network model to reduce the prediction error as the episode proceeds. The direction of policy improvement is wrongly determined by the prediction error at the beginning of learning. To reduce the learning variances due to the error in the statedependent baseline, the proposed scheme uses the input-dependent baseline. The multi-critic network and baseline smoothing can be used to calculate the input-dependent baseline. The multi-critic network includes multiple critic networks that experience different episodes. Each critic network calculates a state-dependent baseline for the current policy of the actor network. The actor network updates its parameters in parallel according to the state-dependent baseline calculated. The multi-critic network approach converges fast to the optimal policy. However, 

**[Limitaciones / riesgos / aplicabilidad | extracto 8 | p.8]**

Journal of Network and Computer Applications 213 (2023) 103604 8 M. Kim and K. Chung Table 3 Setup for the variables used in multi-agent training. Notation Meaning Value 𝑀 Number of multiple inputs 8 𝐿 Number of bitrate levels 6 𝛾 Discounting factor 0.99 𝛼 Learning rate of actor network 0.0001 𝛼′ Learning rate of critic network 0.001 𝛽 Entropy weight 5 to 1 (80,000 episodes) 𝑁𝑟 Number of episode iterations 10 𝑁𝑎 Number of training agents 20 the episodes. The proposed scheme quickly generates the policy that maximizes individual QoE and QoE fairness through input-dependent learning. 3.6. Advantages compared with the existing schemes The proposed scheme uses reinforcement learning based on edge computing assistance. To generate the optimal adaptation policy for multiple clients, the target reward is formulated as a combination of individual QoE and QoE fairness. The QoE of each client, the QoE deviations among multiple clients, and the relationship between bitrate and quality are considered in the target reward. The proposed scheme adopts multi-agent training method to learn the neural network model. Therefore, the adaptation policy is able to determine the next video quality by recognizing multi-client competition under time-varying network conditions. In addition to collecting information about network and client, the edge server handles the neural network model to perform intelligent quality adaptation. The proposed scheme applies the concept of multiple videos and input-dependent learning to adaptation policy generation. This helps the adaptation policy to achieve high QoE in real environments. Consequently, the proposed scheme maximizes the streaming performance for multiple clients. 4. Performance evaluation In this section, we compare the proposed scheme with exist

**[Limitaciones / riesgos / aplicabilidad | extracto 9 | p.9]**

Journal of Network and Computer Applications 213 (2023) 103604 9 M. Kim and K. Chung Table 5 Summary of the performance for the QoE components (BBB). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.78 0.10 0.44 Pensieve (Mao et al., 2017) 2.90 0.10 0.28 QFDVS (Altamimi and Shirmohammadi, 2020) 2.48 0.11 0.40 Proposed 2.90 0.09 0.03 playback interruptions. 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) = 1 𝑃 { 𝜖 𝑃 ∑ 𝑖=1 𝑄(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑄.𝑈 −𝛿 𝑃−1 ∑ 𝑖=1 |𝑄(𝑏𝑖+1) −𝑄(𝑏𝑖)| ⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟ 𝑆.𝑃 −𝜌 𝑃 ∑ 𝑖=1 𝑇(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑅.𝑃 } (12) Where 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) is the average QoE for all segments in the episode experienced by the 𝑘th client. 𝑄.𝑈is the quality utility aggregated for the episode. 𝑆.𝑃is the smoothness penalty calculated by using the magnitude of quality variations. 𝑅.𝑃is the re-buffering penalty determined by the playback interruption time. To evaluate the performance, we measure the average of the overall QoE for the number of clients. By improving QoE fairness, the client can utilize the bandwidth as much as needed to maximize individual QoE (Hoßfeld et al., 2016). We calculate the QoE fairness by using Jain’s Fairness Index (JFI) (Sediq et al., 2013). 𝐽(𝑄𝑜𝐸𝑖) = {∑𝑁𝑎 𝑘=1 𝑄𝑜𝐸𝑖(𝑘)}2 𝑁𝑎 ∑𝑁𝑎 𝑘=1{𝑄𝑜𝐸𝑖(𝑘)}2 (13) Where 𝐽(𝑄𝑜𝐸𝑖) is the QoE fairness for the 𝑖th segment of all clients, and 𝑄𝑜𝐸𝑖(𝑘) is the individual QoE obtained after the 𝑘th client receives the 𝑖th segment. The QoE fairness has a value within 0 and 1. The value close to 1 means that the QoE deviation among multiple clients is low. To evaluate the performance, we measure the average of the QoE fairness for the segments. 4.3. Results for a single video When receiving the BBB video, multiple clients should maintain high quality to maximize individual QoE. The unnecessary quality variations and

**[Limitaciones / riesgos / aplicabilidad | extracto 10 | p.10]**

Journal of Network and Computer Applications 213 (2023) 103604 10 M. Kim and K. Chung Fig. 11. Overall QoE and QoE fairness according to the number of clients (CR). Table 7 Summary of the performance for the QoE components (TOS). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.86 0.08 0.38 Pensieve (Mao et al., 2017) 3.06 0.09 0.33 QFDVS (Altamimi and Shirmohammadi, 2020) 2.55 0.10 0.13 Proposed 3.08 0.07 0.09 number of clients increases by the aggressive adaptation policy. The QFDVS scheme generates the naive adaptation policy, so the overall QoE and the QoE fairness are low. The proposed scheme generates the conservative adaptation policy. This adaptation policy makes the client to utilize the bandwidth as much as needed, leading to the improvements of individual QoE and QoE fairness. Table 6 shows summary of the performance for the QoE components according to various schemes. The ECAA scheme has high smoothness penalty due to quality adaptation based on segment throughput. The aggressive adaptation policy of the Pensieve scheme leads to high quality utility. The QFDVS scheme has low smoothness penalty, but the re-buffering penalty increases by the conservative adaptation policy. The proposed scheme increases the quality slowly and stays long at high quality, resulting in low smoothness penalty and re-buffering penalty. The variations in VMAF scores decrease at high quality, so the differences in VMAF scores for each quality are small, even for the same segment. When receiving the TOS video, multiple clients should improve individual QoE by maintaining high quality for a long time and changing the quality gradually. Moreover, the adaptation policy should select the quality by considering situations that multiple clients oc

## 5. Figuras, tablas, algoritmos y ecuaciones detectadas por texto

**[elemento detectado 1 | p.1]**

Journal of Network and Computer Applications 213 (2023) 103604 Available online 17 February 2023 1084-8045/© 2023 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Journal of Network and Computer Applications journal homepage: www.elsevier.com/locate/jnca HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance Minsu Kim, Kwangsue Chung ∗ Department of Electronics and Communications Engineering, Kwangwoon University, Seoul, 01897, South Korea A R T I C L E I N F O Keywords: Adaptive streaming Reinforcement learning Edge computing Quality of Experience A B S T R A C T As the number of users and the types of videos viewed increase, seamless video streaming services are becoming more important. Adaptive streaming aims to achieve high Quality of Experience (QoE) in time-varying network conditions. However, the existing schemes lack considerations for quality adaptation to improve QoE under dynamic network environments and multi-client competition. In this paper, we propose an HTTP adaptive streaming scheme based on reinforcement learning with edge computing assistance. The proposed scheme uses reinforcement learning to generate robust adaptation policy for changes in the network conditions. Edge computing plays a role of managing multiple clients based on information about the network and client. The proposed scheme co

**[elemento detectado 2 | p.2]**

Journal of Network and Computer Applications 213 (2023) 103604 2 M. Kim and K. Chung Fig. 1. Behavioral structure of HTTP adaptive streaming. Fig. 2. VMAF scores according to bitrates of the BBB video. • We adopt edge computing to support adaptive streaming of multiple clients sharing the same network. • We utilize reinforcement learning to generate a robust adaptation policy for dynamic network environments. • We consider subjective quality, various video characteristics, and learning variances to improve the adaptation policy. • We perform extensive experiments by using the network trace datasets based on real environments and the videos with different characteristics. The remainder of this paper is organized as follows. HTTP adaptive streaming, QoE, edge computing, and reinforcement learning are described in Section 2. The proposed scheme is presented in Section 3. In Section 4, the proposed scheme is compared with existing schemes through simulation-based experiments. Finally, the paper is concluded in Section 5. 2. Related work The process of quality adaptation performed via HTTP adaptive streaming is shown in Fig. 1. The server stores a video in the form of segments with multiple bitrates and a fixed playback length. The client executes the algorithms for quality adaptation and requests a segment from the server. When video streaming starts, the client receives a Media Pr

**[elemento detectado 3 | p.3]**

Journal of Network and Computer Applications 213 (2023) 103604 3 M. Kim and K. Chung bitrate selection algorithm determines the bitrate satisfying each condition of the optimization problem as the quality of the next segment. If all conditions are not satisfied, the algorithm chooses the maximum sustainable bitrate based on the segment throughput and playback buffer level. However, when the network conditions change abruptly, the greedy-based bitrate selection algorithm suffers from QoE degradation. This kind of algorithm explores all cases to solve the optimization problem, leading to low adaptability for dynamic network environments. Edge Computing Assisted Adaptation Scheme with Machine Learning (ECAS-ML) performs intelligent quality adaptation based on edge capability and machine learning (Aguilar-Armijo et al., 2022). To achieve high QoE, the ECAS-ML scheme focuses on managing the tradeoff among bitrate, quality variations, and playback interruptions. The machine learning techniques are utilized to analyze the network conditions and predict the best parameters for heuristic algorithms. However, the ECAS-ML scheme still relies on heuristic algorithms for quality adaptation itself. Tuning the parameters has the limitations to improve overall QoE under dynamic network environments. Unlike the existing schemes, the proposed scheme in this study uses reinforcement learning rath

**[elemento detectado 4 | p.4]**

Journal of Network and Computer Applications 213 (2023) 103604 4 M. Kim and K. Chung Fig. 4. Overview of the input data used for multiple linear regression. of the requested quality by segments, degree of quality variations, and playback interruption time. 𝑄𝑜𝐸𝑖= 𝜖𝑄(𝑏𝑖) −𝛿|𝑄(𝑏𝑖) −𝑄(𝑏𝑖−1)| −𝜌𝑇(𝑏𝑖) (1) Where 𝑄𝑜𝐸𝑖is the individual QoE for the 𝑖th segment, and 𝑄(𝑏𝑖) means the function that indicates the relationship between the bitrate 𝑏𝑖and the quality perceived by the client. 𝑇(𝑏𝑖) is the playback interruption time that occurs after the client receives the 𝑖th segment. 𝜖, 𝛿, 𝜌are the weight parameters to combine the requested quality, quality variations, and playback interruption time. The proposed scheme defines 𝑄(𝑏𝑖) as the VMAF score for the bitrate 𝑏𝑖to consider the correlation between bitrate and quality. The Waterloo SQoE-III database is used to determine the values of the weight parameters (Duanmu et al., 2018). The information about bitrate changes due to quality adaptation, the quality perceived by the client, and the VMAF scores by bitrates exist in the Waterloo SQoEIII database. The proposed scheme performs multiple linear regression. Fig. 4 shows the input data to learn the regression model. The proposed scheme uses 80% of the total videos as the training set and the remaining 20% as the testing set. Data division and learning are iterated 1,000 times to reduce the bia

**[elemento detectado 5 | p.5]**

Journal of Network and Computer Applications 213 (2023) 103604 5 M. Kim and K. Chung Fig. 5. Structure of the neural network model used in the proposed scheme. 𝜃denotes the parameters of the neural network model, 𝑡is the time step for the episode experienced by the agent, and 𝑟𝑡is the target reward at the time step 𝑡. The proposed scheme treats the time step and the segment index as the same value. 𝜋𝜃(𝑠, 𝑎) means the probability that the agent selects the action 𝑎at the state 𝑠by the policy 𝜋𝜃. 𝐴𝑑𝑣𝜋𝜃(𝑠, 𝑎) is the advantage function that determines the direction of policy improvement. The policy gradient method predicts changes in the expected cumulative discounted reward through the execution trajectories of the current policy. The agent improves the policy to increase the selection probability of the action that maximizes the expected cumulative discounted reward. After the episode ends, the neural network model aggregates the state, the action, the reward, and the policy gradient calculated. The actor network updates its parameters by considering the advantage function and the entropy for the policy. 𝜃𝐴←𝜃𝐴+ 𝛼 𝑃 ∑ 𝑡=1 ▿𝜃𝐴ln { 𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) } 𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) +𝛽▿𝜃𝐴𝐻 { 𝜋𝜃𝐴(∙|𝑠𝑡) } (6) Where 𝜃𝐴denotes the parameters of the actor network, and 𝛼is the learning rate for the actor network. 𝑠𝑡and 𝑎𝑡are the state and the action at the time step 𝑡, respectively. 𝑃means the length of the epi

**[elemento detectado 6 | p.6]**

Journal of Network and Computer Applications 213 (2023) 103604 6 M. Kim and K. Chung Table 1 Configuration of the dataset to support multiple videos. Name Types and characteristics Source bitrate Encoding bitrate BigBuckBunny (BBB) - Animation - High motion 4237 Kbps 300, 800, 1400, 2200, 3000, 3900 Kbps CostaRica (CR) - Nature - Low motion 3709 Kbps 200, 700, 1200, 2000, 2600, 3500 Kbps CSGO (CG) - Game - Average motion 3602 Kbps 500, 950, 1600, 2300, 2800, 3400 Kbps Ski (SK) - Sports - High motion 4089 Kbps 350, 600, 1100, 1800, 2550, 3250 Kbps TearsOfSteel (TOS) - Movie - Low motion 2660 Kbps 400, 550, 1050, 1500, 1950, 2400 Kbps The simulator informs the agent about the state, the action, and the immediate reward for the received segment. Using this segment-level simulator, the proposed scheme learns the neural network model within a short time. The trained neural network model is deployed on the edge server for quality adaptation of multiple clients. In the proposed scheme, the actor network of the central agent is placed on the edge server. When video streaming starts, the edge server creates the same number of instances for the actor network as the number of clients connected. The edge server detects the segment request of the client and extracts QoE-related information. The extracted information is then delivered to the actor network. The output of the instance is the b

**[elemento detectado 7 | p.7]**

Journal of Network and Computer Applications 213 (2023) 103604 7 M. Kim and K. Chung Fig. 8. VMAF scores according to segment index for multiple videos. Fig. 9. Immediate reward by episodes of the Pensieve scheme. Pensieve scheme, we performed experiments to measure the changes in the immediate reward according to the episodes. The setup of the Pensieve scheme is used to learn the neural network model (Mao et al., 2017). Fig. 9 shows how the immediate reward of the Pensieve scheme changes by episodes. The measurement results confirmed that the immediate reward fluctuates abruptly for each episode. In the Pensieve scheme, the actor network depends on the expected cumulative discounted reward predicted by the critic network for policy improvement. The learning method using the state-dependent baseline is difficult to distinguish which one affects the reward between the current policy and external factors (Mao et al., 2018). The critic network updates the parameters of the neural network model to reduce the prediction error as the episode proceeds. The direction of policy improvement is wrongly determined by the prediction error at the beginning of learning. To reduce the learning variances due to the error in the statedependent baseline, the proposed scheme uses the input-dependent baseline. The multi-critic network and baseline smoothing can be used to calculate the input-depend

**[elemento detectado 8 | p.8]**

Journal of Network and Computer Applications 213 (2023) 103604 8 M. Kim and K. Chung Table 3 Setup for the variables used in multi-agent training. Notation Meaning Value 𝑀 Number of multiple inputs 8 𝐿 Number of bitrate levels 6 𝛾 Discounting factor 0.99 𝛼 Learning rate of actor network 0.0001 𝛼′ Learning rate of critic network 0.001 𝛽 Entropy weight 5 to 1 (80,000 episodes) 𝑁𝑟 Number of episode iterations 10 𝑁𝑎 Number of training agents 20 the episodes. The proposed scheme quickly generates the policy that maximizes individual QoE and QoE fairness through input-dependent learning. 3.6. Advantages compared with the existing schemes The proposed scheme uses reinforcement learning based on edge computing assistance. To generate the optimal adaptation policy for multiple clients, the target reward is formulated as a combination of individual QoE and QoE fairness. The QoE of each client, the QoE deviations among multiple clients, and the relationship between bitrate and quality are considered in the target reward. The proposed scheme adopts multi-agent training method to learn the neural network model. Therefore, the adaptation policy is able to determine the next video quality by recognizing multi-client competition under time-varying network conditions. In addition to collecting information about network and client, the edge server handles the neural network model to perform inte

**[elemento detectado 9 | p.9]**

Journal of Network and Computer Applications 213 (2023) 103604 9 M. Kim and K. Chung Table 5 Summary of the performance for the QoE components (BBB). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.78 0.10 0.44 Pensieve (Mao et al., 2017) 2.90 0.10 0.28 QFDVS (Altamimi and Shirmohammadi, 2020) 2.48 0.11 0.40 Proposed 2.90 0.09 0.03 playback interruptions. 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) = 1 𝑃 { 𝜖 𝑃 ∑ 𝑖=1 𝑄(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑄.𝑈 −𝛿 𝑃−1 ∑ 𝑖=1 |𝑄(𝑏𝑖+1) −𝑄(𝑏𝑖)| ⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟ 𝑆.𝑃 −𝜌 𝑃 ∑ 𝑖=1 𝑇(𝑏𝑖) ⏟⏞⏞⏞⏟⏞⏞⏞⏟ 𝑅.𝑃 } (12) Where 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) is the average QoE for all segments in the episode experienced by the 𝑘th client. 𝑄.𝑈is the quality utility aggregated for the episode. 𝑆.𝑃is the smoothness penalty calculated by using the magnitude of quality variations. 𝑅.𝑃is the re-buffering penalty determined by the playback interruption time. To evaluate the performance, we measure the average of the overall QoE for the number of clients. By improving QoE fairness, the client can utilize the bandwidth as much as needed to maximize individual QoE (Hoßfeld et al., 2016). We calculate the QoE fairness by using Jain’s Fairness Index (JFI) (Sediq et al., 2013). 𝐽(𝑄𝑜𝐸𝑖) = {∑𝑁𝑎 𝑘=1 𝑄𝑜𝐸𝑖(𝑘)}2 𝑁𝑎 ∑𝑁𝑎 𝑘=1{𝑄𝑜𝐸𝑖(𝑘)}2 (13) Where 𝐽(𝑄𝑜𝐸𝑖) is the QoE fairness for the 𝑖th segment of all clients, and 𝑄𝑜𝐸𝑖(𝑘) is the individual QoE obtained after the 𝑘th client receives the 𝑖th

**[elemento detectado 10 | p.10]**

Journal of Network and Computer Applications 213 (2023) 103604 10 M. Kim and K. Chung Fig. 11. Overall QoE and QoE fairness according to the number of clients (CR). Table 7 Summary of the performance for the QoE components (TOS). Schemes Quality utility Smoothness penalty Re-buffering penalty ECAA (Mehrabi et al., 2018) 2.86 0.08 0.38 Pensieve (Mao et al., 2017) 3.06 0.09 0.33 QFDVS (Altamimi and Shirmohammadi, 2020) 2.55 0.10 0.13 Proposed 3.08 0.07 0.09 number of clients increases by the aggressive adaptation policy. The QFDVS scheme generates the naive adaptation policy, so the overall QoE and the QoE fairness are low. The proposed scheme generates the conservative adaptation policy. This adaptation policy makes the client to utilize the bandwidth as much as needed, leading to the improvements of individual QoE and QoE fairness. Table 6 shows summary of the performance for the QoE components according to various schemes. The ECAA scheme has high smoothness penalty due to quality adaptation based on segment throughput. The aggressive adaptation policy of the Pensieve scheme leads to high quality utility. The QFDVS scheme has low smoothness penalty, but the re-buffering penalty increases by the conservative adaptation policy. The proposed scheme increases the quality slowly and stays long at high quality, resulting in low smoothness penalty and re-buffering penalty. The variat

## 6. Texto crudo extraído del cuerpo principal por página

> Esta sección conserva el texto extraído página a página hasta referencias/bibliografía cuando se detecta. Se incluye para no perder detalles de método, entrenamiento, datos o evaluación. Puede tener problemas de orden de columnas o fórmulas por naturaleza del PDF.

### Página 1

Journal of Network and Computer Applications 213 (2023) 103604
Available online 17 February 2023
1084-8045/© 2023 Elsevier Ltd. All rights reserved.
Contents lists available at ScienceDirect
Journal of Network and Computer Applications
journal homepage: www.elsevier.com/locate/jnca
HTTP adaptive streaming scheme based on reinforcement learning with edge
computing assistance
Minsu Kim, Kwangsue Chung ∗
Department of Electronics and Communications Engineering, Kwangwoon University, Seoul, 01897, South Korea
A R T I C L E
I N F O
Keywords:
Adaptive streaming
Reinforcement learning
Edge computing
Quality of Experience
A B S T R A C T
As the number of users and the types of videos viewed increase, seamless video streaming services are becoming
more important. Adaptive streaming aims to achieve high Quality of Experience (QoE) in time-varying network
conditions. However, the existing schemes lack considerations for quality adaptation to improve QoE under
dynamic network environments and multi-client competition. In this paper, we propose an HTTP adaptive
streaming scheme based on reinforcement learning with edge computing assistance. The proposed scheme
uses reinforcement learning to generate robust adaptation policy for changes in the network conditions. Edge
computing plays a role of managing multiple clients based on information about the network and client.
The proposed scheme considers subjective quality, multiple videos, and learning variances to advance the
adaptation policy. By balancing between individual QoE and QoE fairness, the proposed scheme enables
multiple clients to utilize the bandwidth as much as required. Experimental results show that the proposed
scheme has better performance for individual QoE and QoE fairness than the existing schemes.
1. Introduction
With the advent of various Over-The-Top (OTT) platforms and
mobile devices, the demand for video streaming services is increasing (Cisco, 2020). Accordingly, HTTP adaptive streaming is attracting
attention as a technology for seamless video streaming. The key objective of HTTP adaptive streaming is to improve Quality of Experience
(QoE) (Kua et al., 2017; Petrangeli et al., 2018). Existing schemes using
HTTP adaptive streaming perform quality adaptation by considering
the available network bandwidth, playback buffer level, and content
characteristics (Liu et al., 2011; Le et al., 2013; Juluri et al., 2015; Mok
et al., 2012; Beben et al., 2016).
Multiple clients share a network with limited bandwidth during
video streaming. The available network bandwidth varies rapidly over
time, and each client watches different videos. Therefore, bandwidth
competition among multiple clients occurs. Existing schemes using
HTTP adaptive streaming do not consider bandwidth competition and
depend on heuristic algorithms (Akhshabi et al., 2012; Chen et al.,
2013). Furthermore, bitrate fairness, rather than QoE fairness, is considered in quality adaptation for multiple clients (Jiang et al., 2018).
These approaches hinder the client from using as much bandwidth as
required; hence, individual QoE is degraded.
The QoE is determined by using various factors that have conflicting
goals. Quality adaptation based on QoE influencing factors is required
to enable seamless video streaming (Bae et al., 2015; Jiang et al., 2012).
∗Corresponding author.
E-mail addresses: mskim@cclab.kw.ac.kr (M. Kim), kchung@kw.ac.kr (K. Chung).
The characteristics of subjective quality are not considered in HTTP
adaptive streaming. Subjective quality is not proportional to bitrate
because video type and scene changes also affect the quality perceived
by the client (Qin et al., 2019). If subjective quality is not considered,
the client selects a high bitrate as the quality, even if the QoE gain
is low. This causes bandwidth waste, resulting in the degradation of
individual QoE.
To optimize the performance of video streaming services, quality
adaptation should be intelligent and robust to changes in network conditions. Moreover, individual QoE and QoE fairness should be improved
by considering subjective quality to avoid wastage of available network
bandwidth by the client.
In this paper, we propose an HTTP adaptive streaming scheme
based on reinforcement learning with edge computing assistance. The
proposed scheme applies edge computing to HTTP adaptive streaming,
which makes it easy to access the channel status and support quality adaptation with minor modifications. The proposed scheme uses
reinforcement learning based on a neural network model to generate
an adaptation policy. The neural network model takes QoE-related
information as the input. Maximizing individual QoE and QoE fairness
is set as the objective of the adaptation policy. To generalize the neural
network model, the proposed scheme considers videos with different
characteristics and learning variances occurred in policy improvement.
The major contributions of the proposed scheme are listed below.
https://doi.org/10.1016/j.jnca.2023.103604
Received 26 August 2022; Received in revised form 24 January 2023; Accepted 14 February 2023

### Página 2

Journal of Network and Computer Applications 213 (2023) 103604
2
M. Kim and K. Chung
Fig. 1. Behavioral structure of HTTP adaptive streaming.
Fig. 2. VMAF scores according to bitrates of the BBB video.
• We adopt edge computing to support adaptive streaming of multiple clients sharing the same network.
• We utilize reinforcement learning to generate a robust adaptation
policy for dynamic network environments.
• We consider subjective quality, various video characteristics, and
learning variances to improve the adaptation policy.
• We perform extensive experiments by using the network trace
datasets based on real environments and the videos with different
characteristics.
The remainder of this paper is organized as follows. HTTP adaptive
streaming, QoE, edge computing, and reinforcement learning are described in Section 2. The proposed scheme is presented in Section 3.
In Section 4, the proposed scheme is compared with existing schemes
through simulation-based experiments. Finally, the paper is concluded
in Section 5.
2. Related work
The process of quality adaptation performed via HTTP adaptive
streaming is shown in Fig. 1. The server stores a video in the form of
segments with multiple bitrates and a fixed playback length. The client
executes the algorithms for quality adaptation and requests a segment
from the server. When video streaming starts, the client receives a
Media Presentation Description (MPD) file from the server, which
includes segment information such as the encoding bitrate and position.
The client predicts network conditions based on the measured segment
throughput. The quality of the next segment is determined as the bitrate
that maximizes QoE under the estimated network conditions (Sobhani
et al., 2017; Tian and Liu, 2015).
In HTTP adaptive streaming, QoE is quantified by a combination
of the requested quality for a segment, amount of quality variations,
and playback interruption time. Although the method of using objective factors is simple, it is difficult to accurately measure the quality
perceived by the client. Previous studies have shown that bitrate has a
nonlinear relationship with subjective quality (Li et al., 2016). Video
Multimethod Assessment Fusion (VMAF) is a metric that reflects the
correlation between bitrate and quality for various videos with different
characteristics (Bampis et al., 2021). The VMAF scores for a video
are extracted through frame information aggregation and machine
learning. Because the VMAF score is determined for each frame, it can
be easily applied to the quality adaptation process of HTTP adaptive
streaming. Fig. 2 shows the VMAF scores based on the bitrates of the
Big Buck Bunny (BBB) video. The amount of increasing the VMAF
score becomes small when the bitrate becomes high. Determining the
quality of the segment as high bitrate may result in the bandwidth of
multiple clients being wasted, causing network congestion and degradation of the overall QoE. The VMAF score should be used in quality
adaptation such that the client does not waste the available network
bandwidth (Huang et al., 2018).
Processing real-time data in a cloud degrades the efficiency and scalability of services owing to a long delay. Edge computing improves the
response time and saves the available network bandwidth by processing
data in the vicinity of where data are generated (Abbas et al., 2017). In
addition, edge computing can be applied to HTTP adaptive streaming to
enable efficient bandwidth utilization and reduce unnecessary latency
in video delivery (Bilal and Erbad, 2017). HTTP adaptive streaming
using edge computing requires making minor modifications to server
and client, unlike the method that moves adaptation intelligence to
network elements. The edge server has higher computational power
and larger storage space than the client, hence it is suitable for quality
adaptation based on learning with neural network model.
The Prius scheme performs quality adaptation on the edge server for
multiple clients in a mobile network (Yan et al., 2016). It formulates the
optimization problem for multiple clients by considering the available
resources of the mobile network, the QoE continuum, and several
constraints related to the network and client. This scheme aims to
achieve the same QoE continuum value for multiple clients with limited
bandwidth. Thanks to the capability of edge computing, the Prius
scheme outperforms existing schemes that determine the quality at the
client end. However, it depends on heuristic algorithms, leading to QoE
degradation when the network conditions change abruptly. The method
of achieving the same QoE continuum value prevents multiple clients
from utilizing the bandwidth as much as required to improve their QoE.
Edge Computing Assisted Adaptive streaming (ECAA) supports quality
adaptation for multiple clients at an edge server (Mehrabi et al., 2018).
The ECAA scheme aims to maximize the individual QoE and bitrate
fairness. The optimization problem for multiple clients is formulated
by considering the average quality, quality variations, playback interruptions, and bitrate fairness. The ECAA scheme uses a greedy-based
bitrate selection algorithm to solve the optimization problem. The

### Página 3

Journal of Network and Computer Applications 213 (2023) 103604
3
M. Kim and K. Chung
bitrate selection algorithm determines the bitrate satisfying each condition of the optimization problem as the quality of the next segment.
If all conditions are not satisfied, the algorithm chooses the maximum
sustainable bitrate based on the segment throughput and playback
buffer level. However, when the network conditions change abruptly,
the greedy-based bitrate selection algorithm suffers from QoE degradation. This kind of algorithm explores all cases to solve the optimization
problem, leading to low adaptability for dynamic network environments. Edge Computing Assisted Adaptation Scheme with Machine
Learning (ECAS-ML) performs intelligent quality adaptation based on
edge capability and machine learning (Aguilar-Armijo et al., 2022).
To achieve high QoE, the ECAS-ML scheme focuses on managing the
tradeoff among bitrate, quality variations, and playback interruptions.
The machine learning techniques are utilized to analyze the network
conditions and predict the best parameters for heuristic algorithms.
However, the ECAS-ML scheme still relies on heuristic algorithms for
quality adaptation itself. Tuning the parameters has the limitations to
improve overall QoE under dynamic network environments. Unlike the
existing schemes, the proposed scheme in this study uses reinforcement
learning rather than heuristic algorithms. The adaptation policy of the
proposed scheme considers the impact of quality adaptation at each
client on overall QoE. This leads to high adaptability for time-varying
network conditions and variability in videos, maximizing individual
QoE and QoE fairness.
Reinforcement learning corrects behavior through trial and error to
maximize the cumulative reward in sequential decision-making problems (Luong et al., 2019; Arulkumaran et al., 2017). The optimization
problem of reinforcement learning is expressed by using the Markov
Decision Process (MDP), which consists of an agent, an environment,
a state, an action, and a reward. The agent obtains information about
the reward and next state from the environment. The next action is
selected according to the current policy. The state is defined as the
information provided by the environment and the elements required
to construct the reward. The action is determined by the policy, and
the agent explores the action space in various ways. The reward is
the result of the action selected by the agent. To improve the policy,
the agent maximizes the total future reward to be accumulated by
the policy from the current state. Since quality adaptation is a type
of sequential decision-making problem, it can be converted into the
form of an MDP (Martín et al., 2016). Parameter tuning for changes in
network conditions is not required if reinforcement learning is applied
to HTTP adaptive streaming.
Pensieve is an HTTP adaptive streaming scheme that uses reinforcement learning to solve QoE degradation problems due to the limitations
of heuristic algorithms (Mao et al., 2017). The Pensieve scheme uses the
individual QoE as the reward, and the adaptation policy is generated
by the neural network model. The Pensieve scheme trains the neural
network model with datasets for various network environments and includes the neural network model based on actor–critic approach (Mnih
et al., 2016). The Pensieve scheme uses the information required for
quality adaptation and the influencing factors for individual QoE as
the state. The action is defined as the bitrate selection for the next
segment to be requested. The adaptation policy of the Pensieve scheme
does not consider multi-client competition. This causes severe network
congestion so that the overall QoE of multiple clients is degraded. For
intelligent quality adaptation of multiple clients, QoE-Fair DASH Video
Streaming (QFDVS) uses reinforcement learning and defines the reward
by considering QoE fairness (Altamimi and Shirmohammadi, 2020).
The server performs quality adaptation and stores the trained neural
network model. The QFDVS scheme adopts the actor–critic approach
for the neural network model to generate the policy that determines
the adaptation period and maximum sustainable bitrate. The adaptation
period refers to the time it takes for the client to request the next
segment from the previous segment. The client periodically reports
the bitrate of the segment received and the packet loss ratio of the
network to the server. The adaptation policy of the QFDVS scheme
Fig. 3. Quality adaptation based on reinforcement learning using the neural network
model.
aims to maximize QoE fairness by limiting the bandwidth available to
clients. The QFDVS scheme focuses on improving QoE fairness rather
than individual QoE, resulting in the degradation of overall QoE. The
performance of the QFDVS scheme is degraded in dynamic network
environments. This is because the QFDVS scheme considers a low
number of QoE-related information when generating the adaptation
policy. Reinforcement Learning-Based QoE-Oriented Dynamic Adaptive
Streaming Framework (RLQDAS) aims to maximize the QoE of multiple
clients (Wei et al., 2021). To this end, the inherent fluctuations in network conditions and videos are considered. The optimization problem
is formulated by jointly considering video quality and buffer status.
However, the RLQDAS scheme focuses on guaranteeing applicationlevel fairness based on QoS factors. This approach hinders multiple
clients to utilize the bandwidth as much as needed to improve their
QoE. Unlike the existing schemes, the proposed scheme in this study
considers both individual QoE and QoE fairness. The edge computing
assistance helps the adaptation policy to balance between individual
QoE and QoE fairness. The proposed scheme improves the training
method for the neural network model to reduce learning variances.
Through the advanced training method, the adaptation policy has
better performance under the complicated networks, a large number
of clients, and various videos.
3. Proposed scheme
The basic assumptions for the proposed HTTP adaptive streaming
scheme based on reinforcement learning with edge computing assistance are as follows. The available network bandwidth is affected by the
channel status and bandwidth competition. Multiple clients use devices
with the same resolution. The client modifies the HTTP header of the
segment request to provide the QoE-related information to the server.
The delay caused by the modification of the segment request is ignored.
3.1. Problem definition
The neural network model trained by reinforcement learning plays
a key role in the quality adaptation process of the proposed scheme.
Therefore, it is necessary to concretize the method of applying reinforcement learning to HTTP adaptive streaming. Fig. 3 shows the
structure of the quality adaptation performed by the proposed scheme.
An Adaptive Bit Rate (ABR) agent is represented by the neural network
model. The agent utilizes QoE-related information as the state and determines the quality of the next segment based on the action. According
to the selected action, the agent obtains the reward and the next state
from the environment.
In reinforcement learning, the agent uses the reward for policy
improvement. To generate an optimal policy, the reward should be
related to the state and the optimization goal of the agent. The proposed scheme defines the immediate reward as a linear combination

### Página 4

Journal of Network and Computer Applications 213 (2023) 103604
4
M. Kim and K. Chung
Fig. 4. Overview of the input data used for multiple linear regression.
of the requested quality by segments, degree of quality variations, and
playback interruption time.
𝑄𝑜𝐸𝑖= 𝜖𝑄(𝑏𝑖) −𝛿|𝑄(𝑏𝑖) −𝑄(𝑏𝑖−1)| −𝜌𝑇(𝑏𝑖)
(1)
Where 𝑄𝑜𝐸𝑖is the individual QoE for the 𝑖th segment, and 𝑄(𝑏𝑖) means
the function that indicates the relationship between the bitrate 𝑏𝑖and
the quality perceived by the client. 𝑇(𝑏𝑖) is the playback interruption
time that occurs after the client receives the 𝑖th segment. 𝜖, 𝛿, 𝜌are the
weight parameters to combine the requested quality, quality variations,
and playback interruption time. The proposed scheme defines 𝑄(𝑏𝑖) as
the VMAF score for the bitrate 𝑏𝑖to consider the correlation between
bitrate and quality.
The Waterloo SQoE-III database is used to determine the values of
the weight parameters (Duanmu et al., 2018). The information about
bitrate changes due to quality adaptation, the quality perceived by the
client, and the VMAF scores by bitrates exist in the Waterloo SQoEIII database. The proposed scheme performs multiple linear regression.
Fig. 4 shows the input data to learn the regression model. The proposed
scheme uses 80% of the total videos as the training set and the remaining 20% as the testing set. Data division and learning are iterated 1,000
times to reduce the bias occurred when the amount of training data is
small. The trained regression model obtains a prediction accuracy of
79.23% for the Waterloo SQoE-III database. The values of the weight
parameters are set to 0.41, 0.3, and 6.03, respectively.
The proposed scheme aims to maximize the individual QoE and QoE
fairness for multiple clients. The target reward of the neural network
model is calculated by linearly combining the individual QoE and QoE
deviation among multiple clients.
𝑟𝑖(𝑘) = 𝑄𝑜𝐸𝑖−𝜇
|𝑄𝑜𝐸𝑖−𝑄𝑜𝐸𝑖,𝑎𝑣𝑔(𝑘)|
𝑄𝑜𝐸𝑚𝑎𝑥−𝑄𝑜𝐸𝑚𝑖𝑛
, ∀𝑘= 1, 2, … , 𝑁𝑐
(2)
Where 𝑟𝑖(𝑘) means the target reward for the 𝑖th segment requested
by the 𝑘th client. 𝑄𝑜𝐸𝑖,𝑎𝑣𝑔(𝑘) is the average QoE of multiple clients,
except that for the 𝑘th client. 𝑄𝑜𝐸𝑚𝑎𝑥and 𝑄𝑜𝐸𝑚𝑖𝑛are the maximum and
minimum values of individual QoE for multiple clients, respectively. 𝜇
is the weight parameter of the target reward, and its value is set to the
minimum value of the individual QoE for multiple clients. 𝑁𝑐denotes
the number of clients connected to the edge server. The target reward
is used to update the parameters of the neural network model after the
episode ends.
At the beginning of learning, individual QoE is low because the
adaptation policy has not yet been sufficiently improved. In this case,
the impact of QoE deviation among multiple clients on the target
reward becomes large. The neural network model generates the adaptation policy that conservatively increases the bitrate to reduce the
QoE deviation. The impact of individual QoE on the target reward
increases because the QoE fairness is improved by the conservative
adaptation policy after the agent has experienced several episodes.
To improve the individual QoE, the neural network model generates
the adaptation policy that selects the bitrate maximizing the average
quality and minimizing quality variations and playback interruptions.
The proposed scheme improves the adaptation policy according to
individual QoE and QoE deviation among multiple clients.
The state is the information generated by the interactions between
the agent and the environment. If the state space is too small, information loss occurs during the training of the neural network model. If
the state space is unnecessarily large, the learning complexity increases,
and it takes a long time to converge to the optimal policy. The proposed
scheme defines the state space by considering the influencing factors of
quality adaptation for multiple clients.
𝑆𝑖= {⃖⃖⃗
𝑥𝑖(𝑀), ⃖⃖⃗
𝑑𝑖(𝑀), ⃖⃖⃗𝑧𝑖(𝐿), 𝑜𝑖, 𝑏𝑖, ⃖⃖⃗
𝑓𝑖(𝐿), 𝑐𝑖}
(3)
Where 𝑆𝑖is the state space for the 𝑖th segment. ⃖⃖⃗
𝑥𝑖(𝑀) and ⃖⃖⃗
𝑑𝑖(𝑀) are
the throughput and the download time from the past 𝑀th segment
to the 𝑖th segment, respectively. ⃖⃖⃗𝑧𝑖(𝐿) denotes the next segment sizes
for all bitrate levels, and 𝐿is the number of bitrate levels. 𝑜𝑖is the
playback buffer level changed after the client receives the 𝑖th segment.
To generate the adaptation policy considering subjective quality, the
proposed scheme uses factors related to the VMAF score as the state.
⃖⃖⃗
𝑓𝑖(𝐿) and 𝑐𝑖denote next VMAF scores for all bitrate levels and the
VMAF score for the 𝑖th segment.
The action constitutes the policy along with the state, and the
agent obtains the next state and the reward by the selected action.
The proposed scheme defines the action space by considering that the
client determines the bitrate of the next segment to perform quality
adaptation.
𝑊𝑖= {𝜔1, 𝜔2, … , 𝜔𝐿}
(4)
Where 𝑊𝑖is the action space for the 𝑖th segment, and 𝜔𝑙is the bitrate
corresponding to the level 𝑙. To simplify the scope of the problem,
the proposed scheme assumes that the number of bitrate levels is
fixed. Moreover, the proposed scheme sets the playback length of
the segment and the number of segments to fixed values. The agent
should sufficiently explore the action space to improve the learning
performance. In the proposed scheme, the agent randomly selects the
next action while experiencing the episodes. To verify the validity
of the adaptation policy, the agent determines the bitrate with the
highest selection probability as the next action while the trained neural
network model is being tested.
3.2. Neural network model
The proposed scheme represents complex policy by using the neural
network model. The actor–critic approach is utilized for the neural
network model. Fig. 5 shows the actor network and the critic network
to generate the adaptation policy. For making the neural network
model simple, the proposed scheme uses Fully Connected (FC) and
1D-Convolutional Neural Network (CNN) layers. The FC layers extract
features from a single input, whereas the 1D-CNN layers extract features from multiple inputs. The output layer calculates the selection
probability for each bitrate and the value for the current state.
Except for the output layer, the actor network and the critic network
have the same architecture of layers. The actor network learns the
policy that determines the next action for the current state. The critic
network predicts the cumulative discounted reward for the current
state. The actor network determines the direction of policy improvement by considering the cumulative discounted reward predicted by
the critic network.
The proposed scheme updates the parameters of the neural network
model by using the policy gradient method (Grondman et al., 2012).
Maximizing the expected cumulative discounted reward of the agent is
formulated as the optimization problem based on the policy gradient.
▿𝜃𝐸𝜋𝜃
[ ∞
∑
𝑡=1
𝛾𝑡−1𝑟𝑡
]
= 𝐸𝜋𝜃
[▿𝜃ln{𝜋𝜃(𝑠, 𝑎)}𝐴𝑑𝑣𝜋𝜃(𝑠, 𝑎)]
(5)

### Página 5

Journal of Network and Computer Applications 213 (2023) 103604
5
M. Kim and K. Chung
Fig. 5. Structure of the neural network model used in the proposed scheme.
𝜃denotes the parameters of the neural network model, 𝑡is the
time step for the episode experienced by the agent, and 𝑟𝑡is the target
reward at the time step 𝑡. The proposed scheme treats the time step
and the segment index as the same value. 𝜋𝜃(𝑠, 𝑎) means the probability
that the agent selects the action 𝑎at the state 𝑠by the policy 𝜋𝜃.
𝐴𝑑𝑣𝜋𝜃(𝑠, 𝑎) is the advantage function that determines the direction
of policy improvement. The policy gradient method predicts changes
in the expected cumulative discounted reward through the execution
trajectories of the current policy. The agent improves the policy to
increase the selection probability of the action that maximizes the
expected cumulative discounted reward.
After the episode ends, the neural network model aggregates the
state, the action, the reward, and the policy gradient calculated. The
actor network updates its parameters by considering the advantage
function and the entropy for the policy.
𝜃𝐴←𝜃𝐴+ 𝛼
𝑃
∑
𝑡=1
▿𝜃𝐴ln
{
𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡)
}
𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡)
+𝛽▿𝜃𝐴𝐻
{
𝜋𝜃𝐴(∙|𝑠𝑡)
}
(6)
Where 𝜃𝐴denotes the parameters of the actor network, and 𝛼is the
learning rate for the actor network. 𝑠𝑡and 𝑎𝑡are the state and the action
at the time step 𝑡, respectively. 𝑃means the length of the episode.
𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) is calculated as changes in the expected cumulative discounted reward due to the action determined by the current policy
𝜋𝜃𝐴and the specific action. 𝐻{𝜋𝜃𝐴(∙|𝑠𝑡)} is used to generate a good
policy by sufficiently exploring the action space. The proposed scheme
defines the entropy for the policy based on the selection probability of
all bitrate levels. 𝛽is the entropy weight, which is set to a large value at
the beginning of learning and decreases according to episode progress.
The critic network calculates the baseline of the advantage function.
The parameters of the critic network are updated to reduce the prediction loss in the expected cumulative discounted reward for the current
state. The prediction loss is represented in the form of squared error.
𝜃𝑣←𝜃𝑣−𝛼′
𝑃
∑
𝑡=1
▿𝜃𝑣
{𝑟𝑡+ 𝛾𝑉𝜋𝜃𝐴(𝑠𝑡+1; 𝜃𝑣) −𝑉𝜋𝜃𝐴(𝑠𝑡; 𝜃𝑣)}2
(7)
Where 𝜃𝑣denotes the parameters of the critic network, and 𝛼′ is
the learning rate for the critic network. 𝑉𝜋𝜃𝐴means the cumulative
discounted reward for the policy 𝜋𝜃𝐴at the state 𝑠𝑡, which is predicted
by the critic network. At the beginning of learning, the prediction loss
is large due to the insufficient policy improvement. The prediction loss
decreases as the agent continuously improves the policy.
The advantage function for the action 𝑎𝑡at the state 𝑠𝑡is calculated
as the difference between the baseline determined by the critic network
and the expected cumulative discounted reward at the time step 𝑡.
𝐴𝑑𝑣𝜋𝜃𝐴(𝑠𝑡, 𝑎𝑡) =
𝑃
∑
𝑡′=𝑡
𝛾(𝑡′−1)𝑟𝑡′ −𝑛𝑡
(8)
Fig. 6. Conceptual diagram of multi-agent training method.
Where 𝑛𝑡means the baseline used to calculate the advantage function at
the time step 𝑡. The value of the baseline is the same as the cumulative
discounted reward that the critic network predicts for the policy 𝜋𝜃𝐴of
the actor network at the state 𝑠𝑡.
3.3. Multi-agent training
In video streaming services, multiple clients experience different
network conditions according to the channel status and video characteristics. The proposed scheme aims to maximize individual QoE and
QoE fairness when multiple clients compete for the limited bandwidth
of the network. Therefore, a training method that causes multiple
agents to experience episodes independently and aggregates the immediate reward to calculate the target reward is required. Fig. 6 shows
how multi-agent training is performed to learn the neural network
model in the proposed scheme. The forward agent and the central agent
share the updated parameters of the neural network model and the
learning information.
Each agent has the neural network model that consists of the actor
network and the critic network, described in Section 3.2. 𝑁𝑎is the
number of forward agents that participate in multi-agent training.
The forward agent experiences the episode and transfers the collected
information to the central agent. The episode is represented in the form
of network traces. To simplify the problem scope, the proposed scheme
assumes that the bandwidth of the network traces is changed by the
channel status and multi-client competition. The length of the episode
is fixed to the number of segments, and the forward agent simulates
video streaming based on the bandwidth of the network traces. The
immediate reward in the forward agent means the individual QoE of
each client. The central agent calculates the target reward by aggregating the individual QoE. The actor network and the critic network in
the central agent update the parameters of the neural network model by
using the policy gradient for the target reward. The updated parameters
are copied to the actor network and the critic network in forward
agents. Through this process, the forward agent recognizes multi-client
competition.
Although training the neural network model in real environments
is ideal, this approach has the disadvantage of waiting for the agent
to receive all the segments. The proposed scheme trains the neural
network model offline by using the simulator that operates bitrate selection dynamics for the segments. The simulator measures the segment
download time based on the bandwidth of the network trace and the bitrate of the segment. Moreover, the simulator judges whether the client
experiences playback interruptions according to the measurement results. If the playback interruptions occur, then the segment request is
stopped and tried again after a certain amount of time has elapsed.

### Página 6

Journal of Network and Computer Applications 213 (2023) 103604
6
M. Kim and K. Chung
Table 1
Configuration of the dataset to support multiple videos.
Name
Types and
characteristics
Source
bitrate
Encoding
bitrate
BigBuckBunny
(BBB)
- Animation
- High motion
4237 Kbps
300, 800, 1400, 2200,
3000, 3900 Kbps
CostaRica
(CR)
- Nature
- Low motion
3709 Kbps
200, 700, 1200, 2000,
2600, 3500 Kbps
CSGO
(CG)
- Game
- Average motion
3602 Kbps
500, 950, 1600, 2300,
2800, 3400 Kbps
Ski
(SK)
- Sports
- High motion
4089 Kbps
350, 600, 1100, 1800,
2550, 3250 Kbps
TearsOfSteel
(TOS)
- Movie
- Low motion
2660 Kbps
400, 550, 1050, 1500,
1950, 2400 Kbps
The simulator informs the agent about the state, the action, and the
immediate reward for the received segment. Using this segment-level
simulator, the proposed scheme learns the neural network model within
a short time.
The trained neural network model is deployed on the edge server for
quality adaptation of multiple clients. In the proposed scheme, the actor
network of the central agent is placed on the edge server. When video
streaming starts, the edge server creates the same number of instances
for the actor network as the number of clients connected. The edge
server detects the segment request of the client and extracts QoE-related
information. The extracted information is then delivered to the actor
network. The output of the instance is the bitrate maximizing individual
QoE and QoE fairness at the current state. The edge server modifies the
quality information of the segment request according to the output of
the instance. The edge server transmits the modified segment request
to the server. Upon receiving the segment request, the server transmits
the segment corresponding to the requested quality to the client.
3.4. Supporting of multiple videos
In video streaming services, videos viewed by the client have various characteristics in terms of data size and scene changes. To generalize the adaptation policy, it is necessary to consider that the size of
segments and VMAF scores are different for each client. The proposed
scheme extends the learning method to reflect situations that multiple agents stream different videos during training the neural network
model. Table 1 shows the dataset to support multiple videos with different characteristics. The proposed scheme extracts the VMAF scores
for the segments based on videos with source resolution of 1080p.
The proposed scheme determines the encoding bitrates of multiple
videos by considering Dynamic Adaptive Streaming over HTTP (DASH)
standard dataset (Lederer et al., 2012). The average VMAF scores and
the VMAF score for each segment are extracted for multiple videos
to utilize in learning the neural network model. Fig. 7 shows the
extraction results of the average VMAF scores by bitrates for each
video. The BBB video has a high average VMAF score because the
source bitrate and the encoding bitrate are high. The distortion and
data loss by scene changes in the BBB video are small due to the
characteristics of animation genre. The CR video is composed of natural
landscapes with mostly still objects. In addition, the average VMAF
score is low because distortion occurs due to abrupt scene changes
when different backgrounds appear in the video. The CG and SK videos
have high average VMAF scores since there is less distortion by the
continuous appearance of moving objects. The TOS video has a high
average VMAF score because objects and backgrounds in its scenes are
expressed clearly due to the characteristics of movie genre. Fig. 8 shows
the VMAF scores for the segments of each video in the dataset. The
videos in the dataset consist of 48 segments with playback length of
4 s, and video qualities from 144p to 1080p correspond to the encoding
bitrates. Thanks to less distortion and loss of data within scenes, the
Fig. 7. Changes in average VMAF scores for multiple videos.
VMAF scores of the BBB video show small fluctuations at high quality.
The subjective quality changes abruptly according to bitrates at low
quality, leading to large fluctuations in VMAF scores. However, the
VMAF scores of the BBB video are still high compared with other
videos. In the CR video, scene distortion occurs frequently over time,
so the VMAF score for each segment fluctuates greatly. Moreover, since
the CR video is mainly composed of static scenes, the VMAF scores of
the CR video are low compared with other videos even at high quality.
The fluctuations in the VMAF score for each segment are small in the
CG video because objects with average motion appear continuously,
and similar scenes are repeated over time. In the SK video, the objects
move quickly within the scenes, but the background hardly changes.
Therefore, the fluctuations in the VMAF score for each segment are
small at high quality. Although the TOS video has a low encoding
bitrate, there are small fluctuations in the VMAF score for each segment
at high quality because it generates less distortion in the scenes. For
the 144p quality of the CG and SK videos, it is difficult to express the
complex situations of game genre and fast movements in sports due to
low bitrates. As a result, most of the VMAF scores for the 144p quality
of the CG and SK videos have a value of 0.
The proposed scheme supports multiple videos when determining
network traces and videos to be used in multi-agent training. For each
episode, the agent randomly selects a video from the dataset. The
selected video is not changed during the simulations to learn the neural
network model. The target reward is calculated by considering the
segment sizes and VMAF scores of the video selected differently for
each agent.
3.5. Input-dependent learning
The agent randomly determines the next action to improve the
policy. However, this method increases the learning variances because
outliers occur frequently in the reward (Nair et al., 2018). Using the

### Página 7

Journal of Network and Computer Applications 213 (2023) 103604
7
M. Kim and K. Chung
Fig. 8. VMAF scores according to segment index for multiple videos.
Fig. 9. Immediate reward by episodes of the Pensieve scheme.
Pensieve scheme, we performed experiments to measure the changes
in the immediate reward according to the episodes. The setup of the
Pensieve scheme is used to learn the neural network model (Mao et al.,
2017). Fig. 9 shows how the immediate reward of the Pensieve scheme
changes by episodes. The measurement results confirmed that the
immediate reward fluctuates abruptly for each episode. In the Pensieve
scheme, the actor network depends on the expected cumulative discounted reward predicted by the critic network for policy improvement.
The learning method using the state-dependent baseline is difficult to
distinguish which one affects the reward between the current policy
and external factors (Mao et al., 2018). The critic network updates
the parameters of the neural network model to reduce the prediction
error as the episode proceeds. The direction of policy improvement
is wrongly determined by the prediction error at the beginning of
learning.
To reduce the learning variances due to the error in the statedependent baseline, the proposed scheme uses the input-dependent
baseline. The multi-critic network and baseline smoothing can be used
to calculate the input-dependent baseline. The multi-critic network includes multiple critic networks that experience different episodes. Each
critic network calculates a state-dependent baseline for the current
policy of the actor network. The actor network updates its parameters
in parallel according to the state-dependent baseline calculated. The
multi-critic network approach converges fast to the optimal policy.
However, the burden of learning increases because multiple critic
networks are required for a single actor network. Baseline smoothing
aggregates the expected cumulative discounted reward obtained from
the episodes iterated. The agent randomly selects the next action for
each time step of the episode. Therefore, as the agent repeats the
Table 2
Mean and standard deviation of the immediate reward by the episodes
according to baseline type.
Metrics
State-dependent
Input-dependent
Mean
63.75
68.29 (+7.12%)
Standard deviation
16.96
15.26 (−11.14%)
same episode, it reduces the learning variances. The baseline smoothing
approach has the advantages of simple implementation and a low
burden of learning.
The proposed scheme uses baseline smoothing for input-dependent
learning. Through simulations, the agent can easily repeat the episode
for a video with a fixed number of segments.
𝑛(𝑚)
𝑡
=
𝑃𝑚
∑
𝑖′=1
𝛾(𝑖′−1)𝑟(𝑚)
𝑖′
(9)
Where 𝑛(𝑚)
𝑡
means the value of the baseline calculated by the iteration
results of the 𝑚th episode for the time step 𝑡. 𝑃𝑚is the length of the
𝑚th episode, and 𝑟(𝑚)
𝑖′
is the target reward for the 𝑖′th segment in the
𝑚th episode. In parameter update of the neural network model, the
proposed scheme considers the information of the first one among the
episodes iterated. When the advantage function is calculated, the time
steps for the expected cumulative discounted reward and the baseline
are set to the time step of the first episode.
To determine the baseline of the advantage function, the proposed
scheme calculates the average of the baseline 𝑛𝑡,𝑎𝑣𝑔according to the
episode iterations for the time step 𝑡.
𝑛𝑡,𝑎𝑣𝑔= 1
𝑁𝑟
𝑁𝑟
∑
𝑚=1
𝑛(𝑚)
𝑡
(10)
Where 𝑁𝑟is the number of iterations for the same episode. The proposed scheme considers the average of the baseline according to the
episode iterations at the previous time step in calculating the value of
the baseline for the time step 𝑡.
𝑛𝑡= 1
𝑡
𝑡∑
𝑗=1
𝑛𝑗,𝑎𝑣𝑔
(11)
The baseline is determined according to the target reward obtained
by the current policy. The policy improvement is accelerated as learning proceeds. In addition, the baseline is designed to minimize the
prediction error caused by an imperfect policy, so it is robust to the
learning variances.
We performed experiments that measure the mean and standard
deviation of the immediate reward of the agent to validate the inputdependent learning. Table 2 shows the results of quantitative comparisons for the mean and standard deviation of the immediate reward by

### Página 8

Journal of Network and Computer Applications 213 (2023) 103604
8
M. Kim and K. Chung
Table 3
Setup for the variables used in multi-agent training.
Notation
Meaning
Value
𝑀
Number of multiple inputs
8
𝐿
Number of bitrate levels
6
𝛾
Discounting factor
0.99
𝛼
Learning rate of actor network
0.0001
𝛼′
Learning rate of critic network
0.001
𝛽
Entropy weight
5 to 1
(80,000 episodes)
𝑁𝑟
Number of episode iterations
10
𝑁𝑎
Number of training agents
20
the episodes. The proposed scheme quickly generates the policy that
maximizes individual QoE and QoE fairness through input-dependent
learning.
3.6. Advantages compared with the existing schemes
The proposed scheme uses reinforcement learning based on edge
computing assistance. To generate the optimal adaptation policy for
multiple clients, the target reward is formulated as a combination of
individual QoE and QoE fairness. The QoE of each client, the QoE
deviations among multiple clients, and the relationship between bitrate
and quality are considered in the target reward. The proposed scheme
adopts multi-agent training method to learn the neural network model.
Therefore, the adaptation policy is able to determine the next video
quality by recognizing multi-client competition under time-varying network conditions. In addition to collecting information about network
and client, the edge server handles the neural network model to perform intelligent quality adaptation. The proposed scheme applies the
concept of multiple videos and input-dependent learning to adaptation
policy generation. This helps the adaptation policy to achieve high QoE
in real environments. Consequently, the proposed scheme maximizes
the streaming performance for multiple clients.
4. Performance evaluation
In this section, we compare the proposed scheme with existing
schemes through simulation-based experiments. ECAA, Pensieve, and
QFDVS are used as the existing schemes for performance comparisons. First, we evaluate whether the adaptation policy of the proposed
scheme improves individual QoE and QoE fairness. Next, the impact of
the QoE components on the performance is analyzed. We set evaluation
scenarios for a single video and multiple videos. The individual QoE
and the QoE fairness are measured by changing the number of clients
in each scenario.
4.1. Experimental setup
We utilize TensorFlow and TFLearn library to implement the neural
network model (Google, 2022). The 1D-CNN neurons in the input layer
have 128 filters. The size of each filter is 4, and the stride is 1. The
number of linear neurons in the input layer is the same as the number
of filters for each 1D-CNN neuron. The number of linear neurons in
the output layer of the actor network is the same as the number of
bitrate levels. The critic network has one linear neuron in the output
layer. Rectified Linear Unit (ReLu) is used as the activation function
for the input and hidden layers (Nair and Hinton, 2010). Softmax
is used as the activation function for the output layer of the actor
network (Goodman, 2001). Table 3 shows the variables required to
perform multi-agent training in the proposed scheme. The values for
the discounting factor, learning rates for the actor network and the
critic network, and the number of episode iterations are determined
via preliminary experiments.
Table 4
Mean and standard deviation for the bandwidth of the network traces
in the datasets.
Metrics
Norway
FCC
Belgium
Mean
(Mbps)
1.38
1.92
2.96
Standard deviation
(Mbps)
0.61
1.47
1.26
The number of multiple inputs affects the capability of the neural
network model to identify changes in network conditions. We set the
number of multiple inputs by referring to the experiments performed in
the Pensieve scheme (Mao et al., 2017). The discounting factor reflects
the uncertainty of the next time steps at the current state. The entropy
weight controls the degree of exploration in the agent for the action
space. The number of training agents is equal to the maximum number
of clients used in the experiments.
Using the Norway 3G/HSDPA, FCC Broadband, and Belgium 4G/LTE
datasets, we generated network traces for learning the neural network
model (Riiser et al., 2013; FCC, 2018; Van Der Hooft et al., 2016).
The Norway 3G/HSDPA dataset records the measurement results for
the bandwidth when video streaming is performed during 30 min
in mobile devices. The FCC Broadband dataset contains more than
1 million network traces. Each network trace records the changes
in the bandwidth over 2,100 s by the period of 5 s. The Belgium
4G/LTE dataset records the measurement results for the bandwidth
when mobile devices receive large files through the LTE network. The
new network trace is generated by randomly selecting and combining
the bandwidth from the network trace of each dataset. This trace
records the changes in the bandwidth over 300 s, and the number of
network traces is 6,000. To improve learning efficiency, the proposed
scheme uses the network traces with the minimum bandwidth greater
than 0.2 Mbps and the maximum bandwidth less than 6 Mbps. 80%
of the network traces is randomly used in training the agent, and the
remaining 20% is used in testing the trained neural network model.
Table 4 shows the characteristics of the datasets according to mean
and standard deviation of bandwidth. The Belgium 4G/LTE dataset
has a higher bandwidth of the network traces than other datasets. We
adjusted the bandwidth of the network traces on the Belgium 4G/LTE
dataset.
In the evaluation scenario for a single video, we use the BBB,
CR, and TOS videos. In the evaluation scenario for multiple videos,
all videos in the datasets are used. Unless otherwise noted, the experimental results are the average values for a total of 10 runs. We
changed some settings of the existing schemes for fair comparisons. The
Pensieve scheme trains the neural network model with the same video
and network traces as the proposed scheme and uses the individual
QoE defined in the proposed scheme. The QFDVS scheme utilizes the
same video, network traces, and QoE model as the proposed scheme.
The existing schemes add information related to the VMAF scores to
the state. Moreover, the variables used in multi-agent training of the
proposed scheme are applied to the existing schemes.
4.2. Evaluation metrics
The performance of video streaming services is affected by individual QoE and QoE deviation among multiple clients. To evaluate
the performance of the proposed scheme and the existing schemes,
the metrics for overall QoE and QoE fairness are defined. The overall
QoE means the average of the individual QoE obtained by the client
after video streaming ends. Therefore, we calculate the overall QoE for
each episode by considering the average quality, quality variations, and

### Página 9

Journal of Network and Computer Applications 213 (2023) 103604
9
M. Kim and K. Chung
Table 5
Summary of the performance for the QoE components (BBB).
Schemes
Quality
utility
Smoothness
penalty
Re-buffering
penalty
ECAA (Mehrabi et al., 2018)
2.78
0.10
0.44
Pensieve (Mao et al., 2017)
2.90
0.10
0.28
QFDVS (Altamimi and
Shirmohammadi, 2020)
2.48
0.11
0.40
Proposed
2.90
0.09
0.03
playback interruptions.
𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) = 1
𝑃
{
𝜖
𝑃
∑
𝑖=1
𝑄(𝑏𝑖)
⏟⏞⏞⏞⏟⏞⏞⏞⏟
𝑄.𝑈
−𝛿
𝑃−1
∑
𝑖=1
|𝑄(𝑏𝑖+1) −𝑄(𝑏𝑖)|
⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟
𝑆.𝑃
−𝜌
𝑃
∑
𝑖=1
𝑇(𝑏𝑖)
⏟⏞⏞⏞⏟⏞⏞⏞⏟
𝑅.𝑃
}
(12)
Where 𝑄𝑜𝐸𝑇𝑜𝑡𝑎𝑙(𝑘) is the average QoE for all segments in the episode
experienced by the 𝑘th client. 𝑄.𝑈is the quality utility aggregated for
the episode. 𝑆.𝑃is the smoothness penalty calculated by using the magnitude of quality variations. 𝑅.𝑃is the re-buffering penalty determined
by the playback interruption time. To evaluate the performance, we
measure the average of the overall QoE for the number of clients.
By improving QoE fairness, the client can utilize the bandwidth as
much as needed to maximize individual QoE (Hoßfeld et al., 2016). We
calculate the QoE fairness by using Jain’s Fairness Index (JFI) (Sediq
et al., 2013).
𝐽(𝑄𝑜𝐸𝑖) =
{∑𝑁𝑎
𝑘=1 𝑄𝑜𝐸𝑖(𝑘)}2
𝑁𝑎
∑𝑁𝑎
𝑘=1{𝑄𝑜𝐸𝑖(𝑘)}2
(13)
Where 𝐽(𝑄𝑜𝐸𝑖) is the QoE fairness for the 𝑖th segment of all clients,
and 𝑄𝑜𝐸𝑖(𝑘) is the individual QoE obtained after the 𝑘th client receives
the 𝑖th segment. The QoE fairness has a value within 0 and 1. The
value close to 1 means that the QoE deviation among multiple clients is
low. To evaluate the performance, we measure the average of the QoE
fairness for the segments.
4.3. Results for a single video
When receiving the BBB video, multiple clients should maintain
high quality to maximize individual QoE. The unnecessary quality
variations and the QoE deviation among multiple clients should be minimized by considering the changes in VMAF scores. Fig. 10 shows the
measurement results of overall QoE and QoE fairness for the BBB video
according to the number of clients. We presented the measurement
results with normalization by the largest value.
The ECAA scheme mostly selects a high bitrate for multiple clients.
This behavior leads to high overall QoE and improves QoE fairness.
Thanks to the capability of reinforcement learning, the Pensieve scheme
has better performance than other schemes in terms of overall QoE, except for the proposed scheme. The Pensieve scheme iterates aggressive
and conservative adaptation behaviors, which help it in achieving a
certain level of QoE fairness. The QFDVS scheme has the state space
with small size, leading to low complexity of adaptation policy. As a
result, the QFDVS scheme has the lowest overall QoE and QoE fairness.
The proposed scheme uses the target reward based on individual QoE
and QoE fairness. The target reward is designed to minimize QoE
deviation among multiple clients and maximize bandwidth utilization
of each client. For the cases of changing the number of clients, the
proposed scheme outperforms the existing schemes. Table 5 shows
summary of the performance for the QoE components according to
various schemes. We calculated the results as the average by the
Fig. 10. Overall QoE and QoE fairness according to the number of clients (BBB).
Table 6
Summary of the performance for the QoE components (CR).
Schemes
Quality
utility
Smoothness
penalty
Re-buffering
penalty
ECAA (Mehrabi et al., 2018)
1.76
0.47
0.14
Pensieve (Mao et al., 2017)
1.91
0.46
0.08
QFDVS (Altamimi and
Shirmohammadi, 2020)
1.74
0.45
0.25
Proposed
1.89
0.45
0.04
numbers of clients and segments. The ECAA scheme suffers from high
re-buffering penalty due to the aggressive adaptation behavior at the
beginning of video streaming. The Pensieve scheme has high quality
utility since the adaptation policy aims to maximize individual QoE.
The QFDVS scheme generates the conservative adaptation policy due
to the reward focusing on QoE fairness, leading to low quality utility.
The proposed scheme considers individual QoE and QoE fairness when
generating the adaptation policy. Therefore, the proposed scheme has
better performance for the QoE components than other schemes.
In the CR video, the average VMAF scores for the segments are low,
and the variations in the VMAF scores are high. When receiving the CR
video, multiple clients should improve individual QoE and QoE fairness
by considering the high variability in network conditions and videos.
Moreover, the quality variations and playback interruptions should be
minimized by promptly reacting to the changes in the individual QoE
of each client. Fig. 11 shows the measurement results of overall QoE
and QoE fairness for the CR video according to the number of clients.
In the ECAA scheme, multiple clients select the quality with the
same bitrate regardless of the changes in the VMAF scores, leading to
high QoE fairness. The Pensieve scheme reacts promptly to the changes
in the individual QoE. However, the QoE fairness is degraded as the

### Página 10

Journal of Network and Computer Applications 213 (2023) 103604
10
M. Kim and K. Chung
Fig. 11. Overall QoE and QoE fairness according to the number of clients (CR).
Table 7
Summary of the performance for the QoE components (TOS).
Schemes
Quality
utility
Smoothness
penalty
Re-buffering
penalty
ECAA (Mehrabi et al., 2018)
2.86
0.08
0.38
Pensieve (Mao et al., 2017)
3.06
0.09
0.33
QFDVS (Altamimi and
Shirmohammadi, 2020)
2.55
0.10
0.13
Proposed
3.08
0.07
0.09
number of clients increases by the aggressive adaptation policy. The
QFDVS scheme generates the naive adaptation policy, so the overall
QoE and the QoE fairness are low. The proposed scheme generates
the conservative adaptation policy. This adaptation policy makes the
client to utilize the bandwidth as much as needed, leading to the
improvements of individual QoE and QoE fairness. Table 6 shows
summary of the performance for the QoE components according to
various schemes. The ECAA scheme has high smoothness penalty due
to quality adaptation based on segment throughput. The aggressive
adaptation policy of the Pensieve scheme leads to high quality utility.
The QFDVS scheme has low smoothness penalty, but the re-buffering
penalty increases by the conservative adaptation policy. The proposed
scheme increases the quality slowly and stays long at high quality,
resulting in low smoothness penalty and re-buffering penalty.
The variations in VMAF scores decrease at high quality, so the
differences in VMAF scores for each quality are small, even for the
same segment. When receiving the TOS video, multiple clients should
improve individual QoE by maintaining high quality for a long time and
changing the quality gradually. Moreover, the adaptation policy should
select the quality by considering situations that multiple clients occupy
Fig. 12. Overall QoE and QoE fairness according to the number of clients (TOS).
much bandwidth at the same time. Fig. 12 shows the measurement
results of overall QoE and QoE fairness for the TOS video according
to the number of clients.
The overall QoE of the ECAA scheme is degraded even for the case of
low variability in videos due to the limitations of heuristic algorithms.
The Pensieve scheme does not consider QoE fairness in quality adaptation. This behavior causes the bandwidth waste of multiple clients,
leading to the degradation of the overall QoE and the QoE fairness. The
QFDVS scheme achieves high overall QoE compared with the ECAA
scheme when the number of clients is large. The proposed scheme
changes the quality by considering QoE deviation among multiple
clients. Both the overall QoE and the QoE fairness are improved in
the proposed scheme because the quality adaptation controls the client
not to utilize more bandwidth than necessary when maximizing the
individual QoE. Table 7 shows summary of the performance for the
QoE components according to various schemes. The ECAA scheme uses
the quality change threshold based on segment throughput and the
bitrate fairness threshold with a fixed value, leading to high smoothness
penalty. The Pensieve scheme performs quality adaptation aggressively,
even if the variability in videos is low. Therefore, the smoothness
penalty and the re-buffering penalty are high. The QFDVS scheme
suffers from low quality utility due to the adaptation policy that limits
the bandwidth utilization of multiple clients to be low. The proposed
scheme maximizes the individual QoE while making multiple clients to
utilize the bandwidth sufficiently, leading to better performance than
other schemes.
4.4. Results for multiple videos
The characteristics of videos affect changes in the VMAF scores and
segment sizes. In video streaming services, multiple clients share the

## 7. Referencias/bibliografía
Referencias detectadas desde la página 11. No se expanden completas aquí para no contaminar la lectura de método; consultar PDF original o raw text si hace falta.
