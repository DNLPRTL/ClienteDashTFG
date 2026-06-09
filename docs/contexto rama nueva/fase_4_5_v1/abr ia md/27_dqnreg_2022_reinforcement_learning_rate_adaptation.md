# Reinforcement Learning-Based Rate Adaptation in Dynamic Video Streaming / DQNReg

## 0. Ficha de archivo

- Archivo fuente: `v1_covered.pdf`
- Paginas detectadas: 14
- SHA256 PDF: `586132e10610cf8f9a529456625042bfd9805080b5c30f32f55b95697e557ff4`
- Texto crudo auxiliar: `raw_text/27_dqnreg_2022_reinforcement_learning_rate_adaptation.txt`
- Texto layout auxiliar: `raw_text_layout/27_dqnreg_2022_reinforcement_learning_rate_adaptation_layout.txt`
- Fecha de generacion: 2026-06-09T12:33:31

## 1. Uso previsto para Fase 4-5 v1

Fuente para DQN/deep Q-learning aplicado a DASH con reward QoE segment-wise y evaluacion trace-based en WLAN/5G. Relevante como baseline/familia RL directa y para entender estado/accion/reward en modelos simples.

> Nota de fidelidad: este Markdown es una extraccion tecnica densa para Codex. No es un resumen narrativo ni sustituye al PDF. Para formulas, tablas y figuras criticas, revisar siempre el PDF original.

---

## 2. Identificacion textual de primeras paginas

```text
Reinforcement Learning-Based Rate Adaptation in
Dynamic Video Streaming
Nada A. Hafez
American University of Sharjah
Mohamed S. Hassan
American University of Sharjah
Taha Landolsi  (  tlandolsi@aus.edu )
American University of Sharjah https://orcid.org/0000-0001-8479-9056
Research Article
Keywords: Bitrate Adaptation, DASH, Deep Q-learning, Optimization, Reinforcement Learning, Video
Streaming
Posted Date: August 22nd, 2022
DOI: https://doi.org/10.21203/rs.3.rs-1616726/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.
Read Full License
Springer LATEX template
Reinforcement Learning-Based Rate Adaptation in Dynamic
Video Streaming
N. A. Hafez, M. S. Hassan and T. Landolsi
American University of Sharjah, Sharjah, UAE.
*Corresponding author(s). E-mail(s): tlandolsi@aus.edu;
Contributing authors: g00039071@aus.edu; mshassan@aus.edu;
Abstract
Video streaming stands out as the most signiﬁcant trafﬁc type consumed by mobile devices. This increased
demand has been a major driver for research on bitrate adaptation algorithms. Bitrate adaptation ensures high
user-perceived quality, which, in turn, correlates with higher proﬁts for content providers and delivery sys-
tems. Dynamic adaptive streaming over HTTP (DASH) is a widely adopted video streaming standard utilized
by service providers to provide competitive quality of experience (QoE). It is capable of providing seamless
streaming via uncertain network conditions by switching across different video qualities and their correspond-
ing video segment bitrates. The complexity of the video streaming environment makes it a good candidate
for different learning-based approaches. Accordingly, this paper proposes a reinforcement-learning (RL) deep
Q-network called DQNReg, that enhances the classical deep Q-learning method. A segment-wise QoE-based
reward function is formulated so that the learning strategy can converge towards maximizing the QoE out-
come. The proposed RL-based adaptation approach is evaluated using trace-based simulation for both wireless
local area network channels and 5G mobile channels. The performance of this RL-based method is compared
to three methods: A heuristic method, a model-based method, and a classical learning-based method. The com-
parison shows that the RL-based method converges faster while achieving a high QoE score. In addition, it
reduces the re-buffering duration while maintaining higher video quality and relatively lower quality variations.
Keywords: Bitrate Adaptation, DASH, Deep Q-learning, Optimization, Reinforcement Learning, Video Streaming
1 Introduction
With the constant updates to the wireless LAN
(WLAN) standards and the gradual roll out of 5G
mobile networks, wireless technology is expected to
deliver high multi-Gbps peak data rates, ultra-low
latency, increased reliability and decreased network
management complexity [1]. Enhanced mobile broad-
band with more uniform data rates and increased efﬁ-
ciency empower new and improved user experiences.
At the moment, video streaming stands out as the most
signiﬁcant trafﬁc type consumed by mobile devices
accounting for an average of 60% of total trafﬁc.
This percentage is anticipated to increase to 74% by
the end of 2024. Consumer behavior is shifting from
low-deﬁnition (360p) and standard-deﬁnition formats
(480p) to high-deﬁnition video (720p and 1080p)
as network capabilities improve. In addition, viewer
behavior is expected to change more dramatically as
5G services are made available [2]. The quality of
experience (QoE) perceived by the users is affected
by several factors like video quality, quality switch-
ing and re-buffering duration [3] which are inﬂuenced
by video streaming strategies which typically rely on
adaptive bitrate (ABR) techniques for video streaming
to enhance video delivery and customer satisfaction.
1
```

## 3. Metadatos PDF detectados

```json
{
  "format": "PDF 1.7",
  "title": "",
  "author": "85",
  "subject": "",
  "keywords": "",
  "creator": "Chromium",
  "producer": "GPL Ghostscript 9.52",
  "creationDate": "D:20220822184643Z00'00'",
  "modDate": "D:20220822184643Z00'00'",
  "trapped": "",
  "encryption": null
}
```

## 4. Mapa de secciones detectado

- p. 2: 1 Introduction
- p. 3: 2 Literature review of existing
- p. 3: 2.1 Traditional Adaptation Bitrate
- p. 4: 2.2 RL-Based Adaptation
- p. 5: 3 Methodology
- p. 5: 3.1 Video Streaming Model
- p. 5: 3.2 DQNReg algorithm
- p. 6: 3.3 Reward Function
- p. 6: 3.4 Rate Adaptation with DQNReg
- p. 7: 4 Implementation and Simulation
- p. 7: 4.1 Implementation and Training
- p. 7: 4.2 Video Streaming Environment
- p. 8: 4.3 Simulation Setup
- p. 8: 4.4 Video Parameters
- p. 8: 4.5 Network Traces
- p. 8: 4.5.1 WLAN Channel Environment
- p. 8: 4.5.2 Mobile Channel Environment
- p. 8: 4.6 Comparison to Benchmarks
- p. 8: 4.7 Simulation Results
- p. 9: 5 Performance Evaluation and
- p. 9: 5.1 Evaluation Metrics
- p. 10: 5.2 Performance Comparison
- p. 11: 5.3 Analysis and Discussion
- p. 12: 6 Conclusions
- p. 13: P. Frossard, Online learning adaptation strategy
- p. 13: A. Zanella, D-DASH: A deep Q-learning frame-

## 5. Figuras, tablas, algoritmos, ecuaciones o teoremas detectados

- p. 6: Fig. 1 Proposed RL-based rate adaptation scheme using a DQNReg network.
- p. 7: Fig. 2 Training convergence of DQNReg vs. DQN methods.
- p. 7: Figure 2, the average QoE reward on the training set
- p. 9: Fig. 3 Buffer occupancy for: a) RB, b) HB, c) DQN, and d)
- p. 10: Fig. 4 Quality level for: a) RB, b) HB, c) DQN, and d) DQNReg
- p. 10: Figure 7 illustrates the average QoE for all four sim-
- p. 10: Fig. 5 Buffer occupancy for: a) RB, b) HB, c) DQN, and d)
- p. 11: Fig. 6 Quality level for: a) RB, b) HB, c) DQN, and d) DQNReg
- p. 11: Fig. 7 Average QoE for RB, HB, DQN, and DQNReg methods.
- p. 11: Fig. 8 Rebuffering instances for RB, HB, DQN, and DQNReg
- p. 11: Fig. 9 Rebuffering lengths for RB, HB, DQN, and DQNReg meth-
- p. 11: Fig. 10 Inter-starvation lengths for RB, HB, DQN, and DQNReg
- p. 11: Figure 11. DQNReg keeps the quality stable with a
- p. 12: Fig. 11 QL switching instances for RB, HB, DQN, and DQNReg

## 6. Lineas con posible contenido matematico/formal

Estas lineas NO son LaTeX verificado. Sirven para localizar formulas, objetivos, restricciones o pseudocodigo que hay que verificar en PDF.

- p. 5: `then, for a constant bitrate (CBR) case, Li = TsRv`
- p. 5: `max]. If the average network through-`
- p. 5: `i+1 = T B`
- p. 5: `Yt = rt + γ max`
- p. 5: `δ = Q(st, at) −Yt,`
- p. 6: `LReg = αQ(st, at) + δ2,`
- p. 6: `Here, LReg is the DQNReg loss function, Q(st, at) is`
- p. 6: `QoE = Rv`
- p. 6: `si = (Rv`
- p. 7: `The action selected depends on the policy π, which`
- p. 7: `probability distribution over actions. π(si, ai) is the`
- p. 7: `πθ = arg max`
- p. 7: `Q(si, a).`
- p. 7: `here is α = 0.1, the discount factor is γ = 0.99,`
- p. 8: `max = 60s which is common in a`

## 7. Extraccion tecnica por categorias


### 7.1. modelo ia arquitectura algoritmo

Palabras clave usadas: `model, models, neural, architecture, algorithm, policy, agent, actor, critic, actor-critic, DQN, deep Q, Q-learning, PPO, proximal policy, A3C, reinforcement, DRL, deep reinforcement, meta reinforcement, meta-RL, meta learning, MAML, Mamba, state space, SSM, LSTM, policy network, prediction model, Pensieve, SODA, DQNReg, MetaABR, MERINA, Oboe`

**Fragmento 1 - p. 5 - score 7:**

They established chunk-wise subjective QoE model and utilize it as the reward function in reinforcement learning so that the strategy can converge toward the direction of maximizing the subjective QoE score. In our paper work, we use a reinforcement-based deep Q-learning method, called DQNReg [23], to provide a ﬁne video adaptation through the experi- ence acquired from exploring the network conditions. The objective of the proposed method is to enhance the QoE performance under dynamic network condi- tions, and achieve a fast convergence while maintain- ing higher average rewards than other learning-based methods. 3 Methodology In this section, the video streaming model is presented. The DQNReg algorithm and its reward function are introduced.

**Fragmento 2 - p. 12 - score 7:**

Considering the intricate web- based video delivery ecosystem and its various bot- tlenecks, adaptive bitrate algorithms become essential to content providers to optimize video quality. This thesis proposed utilizing DQNReg, a reinforcement learning based technique that enhances the classical deep Q-learning method approach for video adapta- tion. A segment-wise QoE-based reward function is established so that the learning strategy can converge towards maximizing the QoE outcome. DQNReg have been thoroughly evaluated using trace-based simula- tion for ﬁxed and mobile networks. The DQNReg- based method outperforms classical DQN algorithm and other traditional adaptation approaches. Future research can integrate the initial start-up delay and the impact of latency onto the learning-based method, so that the learned policy can be improved with respect to the QoE.

**Fragmento 3 - p. 7 - score 6:**

Once the obser- vation states are collected by the agent, the Q-value table or the weights in the network are updated until the policy converges. Certain hyper-parameters were set similar to [16, 21, 22]. The weight factor used here is α = 0.1, the discount factor is γ = 0.99, the learning rate is 10−5 and the exploration adopted was the ǫ-greedy to explore many states and have a maintain a trade-off between exploration and exploita- tion. The training algorithm takes the bitrate selection for a video segment as a step, it then takes the step experience and stores it into the experience buffer. In Figure 2, the average QoE reward on the training set is plotted against the number of training episodes for both DQNReg and DQN.

**Fragmento 4 - p. 2 - score 5:**

It is capable of providing seamless streaming via uncertain network conditions by switching across different video qualities and their correspond- ing video segment bitrates. The complexity of the video streaming environment makes it a good candidate for different learning-based approaches. Accordingly, this paper proposes a reinforcement-learning (RL) deep Q-network called DQNReg, that enhances the classical deep Q-learning method. A segment-wise QoE-based reward function is formulated so that the learning strategy can converge towards maximizing the QoE out- come. The proposed RL-based adaptation approach is evaluated using trace-based simulation for both wireless local area network channels and 5G mobile channels.

**Fragmento 5 - p. 5 - score 5:**

The buffer size is depleted as the video is played and is replenished as segments are downloaded. Rebuffer- ing or starvation events happen when the playback buffer of the client has been depleted and the consecu- tive video segment does not arrive before its scheduled playback time. If the buffer occupancy is T B i before the i-th segment is downloaded, then it will become just after it is downloaded: T B i+1 = T B i −Li Rn i + Ts. (1) Therefore, if sufﬁcient buffer content is maintained before loading, i.e. if T B i > Li/Rn i , then rebuffering or starvation events will not take place. 3.2 DQNReg algorithm Many enhancements for the classic deep Q-learning techniques have been proposed. One such a technique is the DQNReg [23].

**Fragmento 6 - p. 6 - score 5:**

Springer LATEX template 5 Adaptation Algorithm Video Player 1 7 6 5 4 3 2 8 9 Server 1 7 6 5 4 3 2 8 9 QL1 1 7 6 5 4 3 2 8 9 QL2 1 7 6 5 4 3 2 8 9 QL3 Segment S7-QL3 Video sequence with 3 quality levels Received Video Segments New HTTP Requests Past segment params.: 1. Network throughput,   2. Segment bit rate,   3. Buffer occupancy,   QL1 QL2 QL3 HTTP GET S1-QL1, … , S3-QL1 1 2 3 HTTP GET S4-QL2, … , S6-QL2 4 5 6 HTTP GET S7-QL3, … , S9-QL3 7 8 9 Quality Selection HTTP Responses 1 4 7         DQNReg network with reward function: action RL agent Wireless Network (WLAN or 5G) Fig. 1 Proposed RL-based rate adaptation scheme using a DQNReg network. LReg = αQ(st, at) + δ2, (4) where Yt is the target Q-value at the time step t, rt is the instantaneous reward, at is the instantaneous action output by the agent to the environment, γ is a discount factor, δ is the DQN loss function, and st and st+1 are the states at t and t + 1, respectively.

**Fragmento 7 - p. 6 - score 5:**

A reward function that represents these factors is introduced to issue policies that maximize the QoE perceived by the users. The reward function is deﬁned as follows [3, 16]: QoE = Rv i −µDB −∥Rv i+1 −Rv i ∥, (5) where Rv i is the bitrate of the i-th video segment, DB is the rebuffering duration experienced when the play- out buffer level, when a segment is downloaded, is lower than the needed segment download time. The rebuffering duration is given by: DB = Rv i Rn i Ts −T B i . (6) The parameter µ is a penalty coefﬁcient for the experi- enced rebuffering event. Finally, the term ∥Rv i+1−Rv i ∥ reﬂects the quality variation between two consecutive segments. 3.4 Rate Adaptation with DQNReg The DQNReg algorithm is implemented as follows: Once the segment is downloaded, the RL agent receives the state inputs at segment i, si = (Rv i−1, Rn i , T B i , T D i , NR), (7)

**Fragmento 8 - p. 6 - score 5:**

Here, LReg is the DQNReg loss function, Q(st, at) is the Q-value penalty, α is a weight factor, and δ2 is the squared error. Classical DQN algorithms tend to overestimate the Q-value, which might be a potential problem [23]. It shows that the learned constraints starts early in the training. To address this issue and avoid overes- timation, the weighted penalty is added to DQNReg loss function as shown in equation (4). Consider- ing the characteristics of the DASH rate adaptation, DQNReg is expected to enable the trained agent to obtain improved QoE performance gain. The QoE- based reward function is explained in the following section. 3.3 Reward Function The QoE is impacted by the video quality of the viewed segment, the frequency of quality switching and the experienced re-buffering events.

**Fragmento 9 - p. 7 - score 5:**

The DQNReg simulation results are contrasted with other benchmark approaches. 0 100 200 300 400 500 600 700 800 900 1000 Episode Number 0.7 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5 1.6 Average QoE DQNReg DQN Fig. 2 Training convergence of DQNReg vs. DQN methods. 4.1 Implementation and Training algorithm The neural network architecture, similar to [16] and [22], is composed of 1D convolution layer com- posed of 128 ﬁlters. The output of these layers is then aggregated with other inputs in a hidden layer, that uses 128 neurons, to apply the rectiﬁed linear unit (ReLU) activation function.The number of neu- rons in the output layer is equal to the adaptive bitrate set, which we have denoted as NR. The training is performed on a sequence extracted from the Big Buck Bunny video (available for download from the Blender.org site [24], for example).

**Fragmento 10 - p. 7 - score 5:**

By regularly observing the environment, the agent gathers tuples containing the previous state, the new state, the action to be undertaken, and the reward to be given to the learner. The temporal-difference technique is then applied to perform gradient descent [22]. This allows the value network to estimate the real state-action value function with adequate accuracy. 4 Implementation and Simulation This section showcases the implementation of the pro- posed DQNReg-based adaptation approach with the simulation setup, the video parameters, and network traces. It is noteworthy to indicate that the neural net- work architecture is not a priority of this paper, hence a default network architecture was adopted for the simu- lation.

**Fragmento 11 - p. 2 - score 4:**

The performance of this RL-based method is compared to three methods: A heuristic method, a model-based method, and a classical learning-based method. The com- parison shows that the RL-based method converges faster while achieving a high QoE score. In addition, it reduces the re-buffering duration while maintaining higher video quality and relatively lower quality variations. Keywords: Bitrate Adaptation, DASH, Deep Q-learning, Optimization, Reinforcement Learning, Video Streaming 1 Introduction With the constant updates to the wireless LAN (WLAN) standards and the gradual roll out of 5G mobile networks, wireless technology is expected to deliver high multi-Gbps peak data rates, ultra-low latency, increased reliability and decreased network management complexity [1].

**Fragmento 12 - p. 3 - score 4:**

Every agent memorizes the conse- quences of his actions and avoids them if they resulted in low revenues in the past. With respect to the rate adaptation problem, the environment for RL includes the network throughput, the available video qualities of the video segments, and the video client playback buffer occupancy. In this paper, a RL-based deep Q-learning is pro- posed to achieve ﬁne video adaptation through the experience acquired from exploring the network envi- ronment. The objective is to achieve a fast conver- gence for the RL-based algorithm while enhancing the QoE performance under wireless local area net- works as well as 5G network conditions. The rest of this paper is organized as follows: Section II provides an overview of related work.

**Fragmento 13 - p. 4 - score 4:**

The scheme trains the classiﬁ- cation model using a dataset. The classiﬁer is then used to predict the current request or any future video request. RL allows an agent to discover the right action to take, within a particular context, based on feed- back from its environment. To do this, an adaptation module interacts with its environment by sensing fac- tors that are expected to inﬂuence its decision. For example, in [16], a system that generates ABR algo- rithms using RL is introduced. This system trains a neural network model that selects bitrates for future video segments based on observations collected by client video players. This system does not rely on pre-programmed models or assumptions about the environment.

**Fragmento 14 - p. 5 - score 4:**

Finally, the DQNReg-based rate adapta- tion technique is detailed. 3.1 Video Streaming Model In this paper, a video sequence is modeled as a set of Ns consecutive segments. Each segment lasts for Ts seconds, and is encoded at the bitrate Rv. The client video player requests a segment at bitrate Rv i for the i-th segment. The selected bitrate Rv i is mapped to different quality levels {Q1, Q2, . . . , QN} based on the client device speciﬁcations and the available video content. In general, The higher the bitrate used in encoding, the higher the video quality delivered to the viewer. Suppose that Qj is the quality level requested for the i-th segment, and let its corresponding bitrate be Rv i . If Li be the size of the i-th segment in bits then, for a constant bitrate (CBR) case, Li = TsRv i .

**Fragmento 15 - p. 5 - score 4:**

It builds on the classical DQN algorithm by adding a weighted penalty to the normal squared Bellman error. The authors in [23] proposed evolution strategies by exploring the space of compu- tational graphs which calculates the loss function for an RL agent. They highlighted that DQNReg shows an improved performance over DQN in environments that have not been experienced during training. Their analysis showed that DQNReg outperforms DQN as well other well-known variants such as the double DQN (DDQN). DQNReg is typically characterized with the following set of equations [23]: Yt = rt + γ max a Qtarg(st+1, a), (2) δ = Q(st, at) −Yt, (3)

**Fragmento 16 - p. 8 - score 4:**

The buffer status is not considered during the quality selection decision. The HB approach is a hybrid adaptation algorithm that combines both the traditional RB and the QoE-based optimization adap- tation approach [29]. The HB approach maximizes the average video quality and minimizes the rebuffering duration while maintaining the quality variation to a certain threshold. Finally, the proposed DQNReg is compared to the classical DQN algorithm. 4.7 Simulation Results The DQNReg model is evaluated on the testing datasets, both ﬁxed and mobile. The trained DQNReg

**Fragmento 17 - p. 1 - score 3:**

Reinforcement Learning-Based Rate Adaptation in Dynamic Video Streaming Nada A. Hafez American University of Sharjah Mohamed S. Hassan American University of Sharjah Taha Landolsi (  tlandolsi@aus.edu ) American University of Sharjah https://orcid.org/0000-0001-8479-9056 Research Article Keywords: Bitrate Adaptation, DASH, Deep Q-learning, Optimization, Reinforcement Learning, Video Streaming Posted Date: August 22nd, 2022 DOI: https://doi.org/10.21203/rs.3.rs-1616726/v1 License:   This work is licensed under a Creative Commons Attribution 4.0 International License. Read Full License

**Fragmento 18 - p. 3 - score 3:**

For instance, the persistent bandwidth ﬂuctuations in the mobile network impose a challenge on ABR meth- ods [1]. In such a dynamic environment a ﬂexible ABR strategy is needed so as to intelligently adjust and maintain a good performance. In this paper, we demonstrate that an ABR strategy based on a machine learning (ML) technique, called reinforcement learning (RL), provides an intelligent and effective solution to the dynamic rate adaptation problem. In RL, an agent learns about the dynamic environment through trial-and-error interactions. The agent takes an action and receives a reward from the environment. The objective of an agent is to maxi- mize the discounted cumulative rewards by learning the optimal actions and then gradually converging to the optimal policy.

**Fragmento 19 - p. 4 - score 3:**

Instead, it learns to make ABR decisions solely through observations of the resulting perfor- mance of past decisions. In [17], the authors incorporated an RL method with the addition of Q-Learning. The action is set as the segment request with a particular bitrate and the reward is deﬁned as the QoE approximation. The study maximizes the QoE through adjusting the adap- tation behavior as per the existing network conditions. Another learning based approach propose to combine the nearest neighbor (KNN) with Q-learning algo- rithm [18]. In this bitrate adaptive scenario, the KNN- Q learning can achieve higher QoE and faster conver- gence speed than the Q-learning algorithm alone. Authors in [19] introduce a system that trains the policy via imitating expert trajectories given by the instant solver.

**Fragmento 20 - p. 5 - score 3:**

Springer LATEX template strategy for DASH clients based on an MDP optimiza- tion was proposed in [20]. The authors introduced a penalty function into the reward function to penalize the system for re-buffering events as well as moving away from a safe buffer level. Authors in [21] presented a framework, called D-DASH, that combines deep learning and reinforce- ment learning techniques to optimize the QoE of DASH. They combined feed-forward and recurrent deep neural networks with advanced strategies. The numerical results are obtained on real and simulated channels. Besides yielding a considerably higher QoE, the D-DASH framework exhibits fast convergence rate. Recently, the authors in [22] used enhanced deep Q-learning for DASH video applications, and proposed a QoE-oriented rate adaptation framework based on enhanced deep Q-learning.

**Fragmento 21 - p. 7 - score 3:**

π(si, ai) is the probability that action ai is taken in si. Practically, there are intractably several si, ai pairs, to overcome this a neural network is utilized to represent the pol- icy with manageable number of parameters θ, usually referred to as policy parameters. The advantage of neural networks is that they can deal with raw signals and do not need to have hand-crafted features. In value-based RL, the agent along side the neu- ral network is expected to extract important features from the state, provide accurate estimation of the state- action value and ﬁnally derive the optimal policy. For a well-trained value network the optimal policy is derived as follows: πθ = arg max a Q(si, a). (8) The learning process of the agent is the training pro- cess of the state-action value network.

**Fragmento 22 - p. 8 - score 3:**

The dataset contains client-side cellular performance indicators such as throughput information and other channel and context-related metrics. These metrics are gen- erated from a network monitoring application called G-NetTrack Pro [27]. 4.6 Comparison to Benchmarks The proposed approach is compared to three bench- marks in the literature: The heuristic rate-based (RB) approach, the model optimization hybrid-based (HB) approach, and the classical DQN learning-based approach. The RB approach selects the highest bitrate that is smaller than the predicted throughput regard- less of the previously selected bitrates. This is referred to as a stateless adaptation algorithm [28]. The adap- tation method is a quality level selector based on the predicted adaptation network throughput which is estimated through a moving average window of N steps.

**Fragmento 23 - p. 9 - score 3:**

3 Buffer occupancy for: a) RB, b) HB, c) DQN, and d) DQNReg methods in a WLAN environment. reward function is computed and normalized. High Average QoE reﬂect, high average video quality, low re-buffering duration and fewer quality switch- ing times. 2. Rebuffering times: Measures the number of instances when the buffer occupancy is zero. 3. Rebuffering duration: Measures the total rebuffering time over the entire video playback duration. 4. Inter-starvation length: Measures the time duration that separates successive rebuffering instants [31]. 5. Quality switching times: Counts the number of times the algorithm switches across different qual- ity levels. This reﬂects the number of times the user-perceived quality changes across the entire video playback.

**Fragmento 24 - p. 9 - score 3:**

Springer LATEX template agent is employed to pick the rate of the video segment to be downloaded. Once the bitrate is selected, the bitrate is mapped to one of four quality levels to better illustrate the quality changes. The performance of the DQNReg agent for each channel environment type is illustrated. The DQNReg performance is compared to the benchmark approaches. Figures 3–6 illustrate the buffer occupancy and quality levels in both ﬁxed and mobile environments for DQNReg compared to the RB, HB, and DQN benchmark approaches. It is clear that both HB and DQN perform better than RB. Although RB maintains a relatively low number of quality jumps in differ- ent environments, it greatly suffers from rebuffering events.

**Fragmento 25 - p. 10 - score 3:**

5 Buffer occupancy for: a) RB, b) HB, c) DQN, and d) DQNReg methods in a 5G mobile environment. average rebuffering times. Finally, DQNReg achieved the lowest average number of rebuffering times with variance similar to that of DQN. The overall rebuffering duration experienced dur- ing the video playback for all algorithms in all sim- ulated network environments is observed in ﬁgure 9. Again, the RB method has the longest rebuffering duration with a small variance. The HB and DQN methods achieved similar average rebuffering dura- tion of about 10 seconds. Finally, DQNReg achieved the lowest average rebuffering duration of about 7 seconds. The average inter-starvation length for all algo- rithms in all simulated network environments is illus- trated in Figure 10.

**Fragmento 26 - p. 11 - score 3:**

Springer LATEX template 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level a) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level b) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level c) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level d) Fig. 6 Quality level for: a) RB, b) HB, c) DQN, and d) DQNReg methods in a 5G mobile environment. Fig. 7 Average QoE for RB, HB, DQN, and DQNReg methods. place successively with short video playback time in between. The HB and DQNReg approaches have com- parable average inter-starvation lengths while DQN has the highest median value of about 100 seconds and is negatively skewed. The overall number of quality switch times expe- rienced during the video playback for all algorithms Fig.


### 7.2. estado inputs features observaciones

Palabras clave usadas: `state, states, input, inputs, feature, features, observation, observations, throughput, bandwidth, buffer, download time, download duration, chunk size, segment size, history, past, remaining, last bitrate, network condition, QoE objective, task, environment, session, forecast, prediction, representation`

**Fragmento 1 - p. 8 - score 7:**

Springer LATEX template 7 the video playback during the download, the playback buffer is drained by the current segment download time. In case the playback buffer is fully occupied, 500ms delay is applied before fetching the other seg- ment. After each segment download, various state observations such as buffer occupancy and current segment bitrate are passed to the learning agent. The learning agent then tries to maximize the reward QoE value, which is impacted by the varying network con- ditions. To design a network that faithfully emulates real conditions, throughput from a corpus of real net- work traces were used. The traces are used to shape the agent’s experience and help it predict the environment dynamics such as the anticipated network through- put.

**Fragmento 2 - p. 6 - score 6:**

Springer LATEX template 5 Adaptation Algorithm Video Player 1 7 6 5 4 3 2 8 9 Server 1 7 6 5 4 3 2 8 9 QL1 1 7 6 5 4 3 2 8 9 QL2 1 7 6 5 4 3 2 8 9 QL3 Segment S7-QL3 Video sequence with 3 quality levels Received Video Segments New HTTP Requests Past segment params.: 1. Network throughput,   2. Segment bit rate,   3. Buffer occupancy,   QL1 QL2 QL3 HTTP GET S1-QL1, … , S3-QL1 1 2 3 HTTP GET S4-QL2, … , S6-QL2 4 5 6 HTTP GET S7-QL3, … , S9-QL3 7 8 9 Quality Selection HTTP Responses 1 4 7         DQNReg network with reward function: action RL agent Wireless Network (WLAN or 5G) Fig. 1 Proposed RL-based rate adaptation scheme using a DQNReg network. LReg = αQ(st, at) + δ2, (4) where Yt is the target Q-value at the time step t, rt is the instantaneous reward, at is the instantaneous action output by the agent to the environment, γ is a discount factor, δ is the DQN loss function, and st and st+1 are the states at t and t + 1, respectively.

**Fragmento 3 - p. 7 - score 6:**

Springer LATEX template where Rv i−1 is the bitrate at which the last video seg- ment was downloaded, Rn i is the network throughput measurement, T B i is the current buffer level, T D i is the download time of the past video segment and NR is the available bitrate for the next video segment. The learning agent observes the state si from the environ- ment then takes an action ai which is selecting the bitrate for the upcoming video segment. In turn, the agent receives the corresponding reward. It is to be noted that the state transition in the environment is also impacted by the action taken. The action selected depends on the policy π, which is deﬁned as the mapping of the action to state or the probability distribution over actions.

**Fragmento 4 - p. 3 - score 5:**

Every agent memorizes the conse- quences of his actions and avoids them if they resulted in low revenues in the past. With respect to the rate adaptation problem, the environment for RL includes the network throughput, the available video qualities of the video segments, and the video client playback buffer occupancy. In this paper, a RL-based deep Q-learning is pro- posed to achieve ﬁne video adaptation through the experience acquired from exploring the network envi- ronment. The objective is to achieve a fast conver- gence for the RL-based algorithm while enhancing the QoE performance under wireless local area net- works as well as 5G network conditions. The rest of this paper is organized as follows: Section II provides an overview of related work.

**Fragmento 5 - p. 6 - score 5:**

A reward function that represents these factors is introduced to issue policies that maximize the QoE perceived by the users. The reward function is deﬁned as follows [3, 16]: QoE = Rv i −µDB −∥Rv i+1 −Rv i ∥, (5) where Rv i is the bitrate of the i-th video segment, DB is the rebuffering duration experienced when the play- out buffer level, when a segment is downloaded, is lower than the needed segment download time. The rebuffering duration is given by: DB = Rv i Rn i Ts −T B i . (6) The parameter µ is a penalty coefﬁcient for the experi- enced rebuffering event. Finally, the term ∥Rv i+1−Rv i ∥ reﬂects the quality variation between two consecutive segments. 3.4 Rate Adaptation with DQNReg The DQNReg algorithm is implemented as follows: Once the segment is downloaded, the RL agent receives the state inputs at segment i, si = (Rv i−1, Rn i , T B i , T D i , NR), (7)

**Fragmento 6 - p. 4 - score 4:**

A buffer-based adaptation approach that does not rely on throughput prediction methods is presented in [12]. The algorithm solves optimization problem based on the buffer length reservation. It downloads the lowest bitrate and tries to maintain the buffer occu- pancy within a certain threshold. Another adaptation logic based on optimization techniques is presented in [13] which introduces a novel probing based net- work measurement technique to advance the video quality selection. It also presents a QoE-aware DASH system, called QDASH, with mixed-integer linear pro- gramming. The authors in [14] used an optimization mechanism with two objective functions: The ﬁrst function maximizes the overall average QoE among DASH clients, while the second function minimizes the negative impact of temporal video quality changes; that is the up and down switching between different representation during playback.

**Fragmento 7 - p. 4 - score 4:**

Instead, it learns to make ABR decisions solely through observations of the resulting perfor- mance of past decisions. In [17], the authors incorporated an RL method with the addition of Q-Learning. The action is set as the segment request with a particular bitrate and the reward is deﬁned as the QoE approximation. The study maximizes the QoE through adjusting the adap- tation behavior as per the existing network conditions. Another learning based approach propose to combine the nearest neighbor (KNN) with Q-learning algo- rithm [18]. In this bitrate adaptive scenario, the KNN- Q learning can achieve higher QoE and faster conver- gence speed than the Q-learning algorithm alone. Authors in [19] introduce a system that trains the policy via imitating expert trajectories given by the instant solver.

**Fragmento 8 - p. 4 - score 4:**

Springer LATEX template 3 underﬂows are reduced. Nonetheless, the main draw- back of the heuristic based techniques is that they cannot be generalized since they are deterministically customized to particular network conditions. Control theory is used to model dynamical sys- tems that are stable and accurate. The work in [3] introduces a model predictive control approach which optimizes the QoE function by selecting bitrates based on throughput approximation. It predicts throughput of upcoming segments downloads based on existing samples of recently downloaded segments. The work in [10] proposes an adaptation logic based on feed- back control. The quality adaptation controller takes a buffer as an input and returns the video rate of the segment to be downloaded.

**Fragmento 9 - p. 4 - score 4:**

A proportional-integral controller outputs a video rate that matches the esti- mated available and ensures the buffer is maintained at the target level. Optimization-based approaches are widely used for bitrate adaptation in DASH. Essentially, the opti- mization problem is solved based on the prediction of buffer dynamics and network throughput. How- ever, stochastic segment size shifts the buffer occu- pancy from the estimated value. In order to get rid of this effect and improve the prediction accuracy for buffer occupancy [11] propose an algorithm based on Markov decision process (MDP) with segment size information so that only the network capacity vari- ation need to be considered in the decision-making process.

**Fragmento 10 - p. 7 - score 4:**

It is clear that DQNReg con- verges faster and achieves higher average QoE value. 4.2 Video Streaming Environment The video streaming environment consists of a set of videos encoded at different rates. An internal repre- sentation of the client’s playback buffer is maintained. A download time is assigned based on the segment’s bitrate and available network throughput. To represent

**Fragmento 11 - p. 3 - score 3:**

On the other hand, in the ML-based case the video playback system learns to adapt to the network environment even under unfore- seen conditions. Typically, network QoS parameters and video playback buffer information are used in these methods. 2.1 Traditional Adaptation Bitrate Techniques Heuristic-based techniques can be categorized into two types [4]. The ﬁrst type comprises a set of throughput-based techniques, in which a video client relies on observed network throughput to make a decision about the bitrates of future requested seg- ments [7]. The second type comprises a set of buffer- based techniques which utilize the available playback buffer space to determine the quality of the future requested segments [8].

**Fragmento 12 - p. 3 - score 3:**

Typically the video ﬁle is divided into short segments (1-10 seconds long) and encoded at several quality levels (QL). DASH enables seamless switch- ing between quality levels for each segment based on the streaming client local information about cer- tain network quality of service (QoS) parameters, such as the network throughput and delay, the video client playback buffer occupancy and the video server workload. Most ABR methods are based on heuristic algo- rithms, which can be categorized into throughput- based or buffer-based approaches [4]. The heuristic techniques rely on customized, hard-coded algorithms for bitrate selection, which may result in a poor per- formance under different network environments.

**Fragmento 13 - p. 3 - score 3:**

Springer LATEX template Dynamic adaptive streaming over HTTP (DASH) technology utilizes HTTP as its application layer pro- tocol along with TCP as its transport layer proto- col. DASH allows the bitrate and consequently the quality of the video to adjust according to the avail- able resources in the underlying network. Relevant resources are typically the network throughput and the availability of the playback buffer [3]. The client initiates a streaming session with the server and gets the desired video’s manifest ﬁle. The media presenta- tion description (MPD) provides required information such as uniform resource locators (URL), bitrates, resolutions, sizes, and availability of the video seg- ments.

**Fragmento 14 - p. 4 - score 3:**

2.2 RL-Based Adaptation Existing classic ABR algorithms mostly rely on ﬁxed heuristics that have been ﬁne tuned according to ﬁxed assumptions about deployment environments. Not only that, but each of these approaches have been designed to optimize for a speciﬁc QoE metric. Consequently, if the assumptions are breached, these ABR algorithms fail to generalize and perform poorly. To overcome these issues, learning-based adaptation approaches are explored. With machine learning tech- niques a client can learn to adapt its video quality to the changing context without the need for any human intervention. Authors in [15] use a decision-tree based random forest classiﬁcation to map network related features onto the video rate.

**Fragmento 15 - p. 4 - score 3:**

The scheme trains the classiﬁ- cation model using a dataset. The classiﬁer is then used to predict the current request or any future video request. RL allows an agent to discover the right action to take, within a particular context, based on feed- back from its environment. To do this, an adaptation module interacts with its environment by sensing fac- tors that are expected to inﬂuence its decision. For example, in [16], a system that generates ABR algo- rithms using RL is introduced. This system trains a neural network model that selects bitrates for future video segments based on observations collected by client video players. This system does not rely on pre-programmed models or assumptions about the environment.

**Fragmento 16 - p. 7 - score 3:**

π(si, ai) is the probability that action ai is taken in si. Practically, there are intractably several si, ai pairs, to overcome this a neural network is utilized to represent the pol- icy with manageable number of parameters θ, usually referred to as policy parameters. The advantage of neural networks is that they can deal with raw signals and do not need to have hand-crafted features. In value-based RL, the agent along side the neu- ral network is expected to extract important features from the state, provide accurate estimation of the state- action value and ﬁnally derive the optimal policy. For a well-trained value network the optimal policy is derived as follows: πθ = arg max a Q(si, a). (8) The learning process of the agent is the training pro- cess of the state-action value network.

**Fragmento 17 - p. 7 - score 3:**

Once the obser- vation states are collected by the agent, the Q-value table or the weights in the network are updated until the policy converges. Certain hyper-parameters were set similar to [16, 21, 22]. The weight factor used here is α = 0.1, the discount factor is γ = 0.99, the learning rate is 10−5 and the exploration adopted was the ǫ-greedy to explore many states and have a maintain a trade-off between exploration and exploita- tion. The training algorithm takes the bitrate selection for a video segment as a step, it then takes the step experience and stores it into the experience buffer. In Figure 2, the average QoE reward on the training set is plotted against the number of training episodes for both DQNReg and DQN.

**Fragmento 18 - p. 8 - score 3:**

It is necessary to note that the quality of the dataset impacts the performance of the learning agent. These traces allow the agent to experience throughput variations in real networks. 4.3 Simulation Setup A simulation testbed based on the video streaming environment is implemented in SimEvent discrete- event simulator in MATLAB. The testbed simulates the video player buffer dynamics during the process of receiving and playing back video segments based on a bitrate range and network proﬁles. To train the agent a corpus of network traces is created through con- catenating different excerpts of the network datasets, which will be detailed in the section below. The size of the buffer is set T B max = 60s which is common in a DASH video player.

**Fragmento 19 - p. 9 - score 3:**

5 Performance Evaluation and Discussion After performing extensive simulations in different network environments, the performance of the sim- ulated approaches is analyzed and evaluated. The evaluation metrics used are explained then the DQN- Reg adaptation approach is evaluated and compared to the aforementioned benchmark approaches. 5.1 Evaluation Metrics The proposed method’s performance is evaluated using the following metrics: 1. Average QoE: The QoE objective is a sum of weighted objectives that have varying orders of magnitudes. To make fair comparisons it is impor- tant to transform the objective functions in a way that they all have comparable orders of magni- tude [30]. The average QoE, calculated through the 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) a) 260 280 300 320 340 360 380 400 420 440 460 Time (s) 0 20 40 60 Buffer Length (s) b) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) c) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) d) Fig.

**Fragmento 20 - p. 10 - score 3:**

The RB method, however, showed the lowest average score but with a larger variance compared to the other methods. The number of rebuffering instances for all algo- rithms in all simulated network environments is shown in Figure 8. The RB method has the highest number of starvation instances with smallest variance, this means that rebuffering instances will occur with rate-based regardless of the network condition. This is owed to the fact that the RB method ignores the playback buffer occupancy and considers the network through- put only. The HB and DQN methods achieved similar 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) a) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) b) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) c) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) d) Fig.

**Fragmento 21 - p. 12 - score 3:**

By analyzing the various indicators, it is noted that when using the DQNReg approach, the number of rebuffering times, the rebuffering duration and the quality switching times are suppressed to the lowest, while the quality switching times and inter-starvation lengths are maintained at a level comparable to other methods. Under various mobility patterns of real-time network, the average QoE performance of DQNReg is still superior to other methods. This indicates that the trained DQNReg learning agent has strong gen- eralization ability and can ﬂexibly adapt to various network conditions, so that the video service quality can match the network communication quality as well as possible. 6 Conclusions With increased user expectations and demands for uninterrupted viewing and top video quality, stud- ies concluded that users will leave video sessions if the quality is not adequate, harming the revenues of content providers.

**Fragmento 22 - p. 2 - score 2:**

It is capable of providing seamless streaming via uncertain network conditions by switching across different video qualities and their correspond- ing video segment bitrates. The complexity of the video streaming environment makes it a good candidate for different learning-based approaches. Accordingly, this paper proposes a reinforcement-learning (RL) deep Q-network called DQNReg, that enhances the classical deep Q-learning method. A segment-wise QoE-based reward function is formulated so that the learning strategy can converge towards maximizing the QoE out- come. The proposed RL-based adaptation approach is evaluated using trace-based simulation for both wireless local area network channels and 5G mobile channels.

**Fragmento 23 - p. 3 - score 2:**

For instance, the persistent bandwidth ﬂuctuations in the mobile network impose a challenge on ABR meth- ods [1]. In such a dynamic environment a ﬂexible ABR strategy is needed so as to intelligently adjust and maintain a good performance. In this paper, we demonstrate that an ABR strategy based on a machine learning (ML) technique, called reinforcement learning (RL), provides an intelligent and effective solution to the dynamic rate adaptation problem. In RL, an agent learns about the dynamic environment through trial-and-error interactions. The agent takes an action and receives a reward from the environment. The objective of an agent is to maxi- mize the discounted cumulative rewards by learning the optimal actions and then gradually converging to the optimal policy.

**Fragmento 24 - p. 4 - score 2:**

The system attempts to pick the seg- ment with higher perceptual video qualities rather than video bitrates by constructing a neural network archi- tecture, video datasets and QoE metrics with video quality features. Another online learning adaptation

**Fragmento 25 - p. 5 - score 2:**

This relationship does not hold for the variable bitrate (VBR) case, however. The video client application requests segments, waits for the underlying network to deliver them, and then downloads them into a buffer whose instanta- neous temporal occupancy is denoted as T B i . This parameter is measured in seconds, and in a typical setting, may contain tens of seconds worth of video segments. In this paper, we assume that it ranges in the interval [0, T B max]. If the average network through- put be Rn i during the downloading of the i-th segment, then the needed download time will be Li/Rn i . Since Li depends on the segment quality, therefore the download time depends on the segment bitrate Rv i .

**Fragmento 26 - p. 7 - score 2:**

The DQNReg simulation results are contrasted with other benchmark approaches. 0 100 200 300 400 500 600 700 800 900 1000 Episode Number 0.7 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5 1.6 Average QoE DQNReg DQN Fig. 2 Training convergence of DQNReg vs. DQN methods. 4.1 Implementation and Training algorithm The neural network architecture, similar to [16] and [22], is composed of 1D convolution layer com- posed of 128 ﬁlters. The output of these layers is then aggregated with other inputs in a hidden layer, that uses 128 neurons, to apply the rectiﬁed linear unit (ReLU) activation function.The number of neu- rons in the output layer is equal to the adaptive bitrate set, which we have denoted as NR. The training is performed on a sequence extracted from the Big Buck Bunny video (available for download from the Blender.org site [24], for example).


### 7.3. accion decision abr salida

Palabras clave usadas: `action, actions, bitrate, bit rate, quality level, representation, decision, decisions, select, selection, adaptation, output, score, guidance, recommend, priority, policy output, controller, rate adaptation, quality`

**Fragmento 1 - p. 6 - score 9:**

Springer LATEX template 5 Adaptation Algorithm Video Player 1 7 6 5 4 3 2 8 9 Server 1 7 6 5 4 3 2 8 9 QL1 1 7 6 5 4 3 2 8 9 QL2 1 7 6 5 4 3 2 8 9 QL3 Segment S7-QL3 Video sequence with 3 quality levels Received Video Segments New HTTP Requests Past segment params.: 1. Network throughput,   2. Segment bit rate,   3. Buffer occupancy,   QL1 QL2 QL3 HTTP GET S1-QL1, … , S3-QL1 1 2 3 HTTP GET S4-QL2, … , S6-QL2 4 5 6 HTTP GET S7-QL3, … , S9-QL3 7 8 9 Quality Selection HTTP Responses 1 4 7         DQNReg network with reward function: action RL agent Wireless Network (WLAN or 5G) Fig. 1 Proposed RL-based rate adaptation scheme using a DQNReg network. LReg = αQ(st, at) + δ2, (4) where Yt is the target Q-value at the time step t, rt is the instantaneous reward, at is the instantaneous action output by the agent to the environment, γ is a discount factor, δ is the DQN loss function, and st and st+1 are the states at t and t + 1, respectively.

**Fragmento 2 - p. 4 - score 6:**

A buffer-based adaptation approach that does not rely on throughput prediction methods is presented in [12]. The algorithm solves optimization problem based on the buffer length reservation. It downloads the lowest bitrate and tries to maintain the buffer occu- pancy within a certain threshold. Another adaptation logic based on optimization techniques is presented in [13] which introduces a novel probing based net- work measurement technique to advance the video quality selection. It also presents a QoE-aware DASH system, called QDASH, with mixed-integer linear pro- gramming. The authors in [14] used an optimization mechanism with two objective functions: The ﬁrst function maximizes the overall average QoE among DASH clients, while the second function minimizes the negative impact of temporal video quality changes; that is the up and down switching between different representation during playback.

**Fragmento 3 - p. 4 - score 6:**

A proportional-integral controller outputs a video rate that matches the esti- mated available and ensures the buffer is maintained at the target level. Optimization-based approaches are widely used for bitrate adaptation in DASH. Essentially, the opti- mization problem is solved based on the prediction of buffer dynamics and network throughput. How- ever, stochastic segment size shifts the buffer occu- pancy from the estimated value. In order to get rid of this effect and improve the prediction accuracy for buffer occupancy [11] propose an algorithm based on Markov decision process (MDP) with segment size information so that only the network capacity vari- ation need to be considered in the decision-making process.

**Fragmento 4 - p. 12 - score 6:**

Wei, and S. Kwong, Spatial and temporal consistency-aware dynamic adaptive streaming for 360-degree videos, IEEE Journal of Selected Topics in Signal Processing, vol.14, no. 1, pp. 177-193, Jan. 2020. [6] H. Yuan, X. Hu, J. Hou, X. Wei, and S. Kwong, An ensemble rate adaptation framework for dynamic adaptive streaming over HTTP, IEEE Transactions on Broadcasting, vol. 66, no. 2, pp. 251-263, Jun. 2020. [7] A. Bentaleb, B. Taani, A. C. Begen, C. Timmerer, and R. Zimmermann, A survey on bitrate adap- tation schemes for streaming media over HTTP,

**Fragmento 5 - p. 13 - score 6:**

3, pp. 523–534, Sept 2017. [15] Y.-L. Chien, K. C.-J. Lin, and M.-S. Chen, Machine learning based rate adaptation with elas- tic feature selection for HTTP-based streaming, ICME, IEEE Computer Society, 2015, pp. 1–6. [16] H. Mao, R. Netravali, and M. Alizadeh, Neu- ral adaptive video streaming with Pensieve, ACM Conference on SIGCOMM, 2017. [17] M. Claeys, S. Latr´e, J. Famaey, T. Wu, W. Van Leekwijck, and F. De Turck, Design of a Q-learning-based client quality selection algo- rithm for HTTP adaptive video streaming, Pro- ceedings of Adaptive and Learning Agents Work- shop, 2013, pp. 30–37. [18] H. Lin, Z. Shen, H. Zhou, X. Liu, L. Zhang, G. Xiao, and Z. Cheng, KNN-Q learning algo- rithm of bitrate adaptation for video streaming over HTTP, 2020 Information Communication Technologies Conference (ICTC), 2020, pp.

**Fragmento 6 - p. 2 - score 5:**

The performance of this RL-based method is compared to three methods: A heuristic method, a model-based method, and a classical learning-based method. The com- parison shows that the RL-based method converges faster while achieving a high QoE score. In addition, it reduces the re-buffering duration while maintaining higher video quality and relatively lower quality variations. Keywords: Bitrate Adaptation, DASH, Deep Q-learning, Optimization, Reinforcement Learning, Video Streaming 1 Introduction With the constant updates to the wireless LAN (WLAN) standards and the gradual roll out of 5G mobile networks, wireless technology is expected to deliver high multi-Gbps peak data rates, ultra-low latency, increased reliability and decreased network management complexity [1].

**Fragmento 7 - p. 3 - score 5:**

Typically the video ﬁle is divided into short segments (1-10 seconds long) and encoded at several quality levels (QL). DASH enables seamless switch- ing between quality levels for each segment based on the streaming client local information about cer- tain network quality of service (QoS) parameters, such as the network throughput and delay, the video client playback buffer occupancy and the video server workload. Most ABR methods are based on heuristic algo- rithms, which can be categorized into throughput- based or buffer-based approaches [4]. The heuristic techniques rely on customized, hard-coded algorithms for bitrate selection, which may result in a poor per- formance under different network environments.

**Fragmento 8 - p. 4 - score 5:**

Springer LATEX template 3 underﬂows are reduced. Nonetheless, the main draw- back of the heuristic based techniques is that they cannot be generalized since they are deterministically customized to particular network conditions. Control theory is used to model dynamical sys- tems that are stable and accurate. The work in [3] introduces a model predictive control approach which optimizes the QoE function by selecting bitrates based on throughput approximation. It predicts throughput of upcoming segments downloads based on existing samples of recently downloaded segments. The work in [10] proposes an adaptation logic based on feed- back control. The quality adaptation controller takes a buffer as an input and returns the video rate of the segment to be downloaded.

**Fragmento 9 - p. 4 - score 5:**

The scheme trains the classiﬁ- cation model using a dataset. The classiﬁer is then used to predict the current request or any future video request. RL allows an agent to discover the right action to take, within a particular context, based on feed- back from its environment. To do this, an adaptation module interacts with its environment by sensing fac- tors that are expected to inﬂuence its decision. For example, in [16], a system that generates ABR algo- rithms using RL is introduced. This system trains a neural network model that selects bitrates for future video segments based on observations collected by client video players. This system does not rely on pre-programmed models or assumptions about the environment.

**Fragmento 10 - p. 8 - score 5:**

The dataset contains client-side cellular performance indicators such as throughput information and other channel and context-related metrics. These metrics are gen- erated from a network monitoring application called G-NetTrack Pro [27]. 4.6 Comparison to Benchmarks The proposed approach is compared to three bench- marks in the literature: The heuristic rate-based (RB) approach, the model optimization hybrid-based (HB) approach, and the classical DQN learning-based approach. The RB approach selects the highest bitrate that is smaller than the predicted throughput regard- less of the previously selected bitrates. This is referred to as a stateless adaptation algorithm [28]. The adap- tation method is a quality level selector based on the predicted adaptation network throughput which is estimated through a moving average window of N steps.

**Fragmento 11 - p. 8 - score 5:**

The buffer status is not considered during the quality selection decision. The HB approach is a hybrid adaptation algorithm that combines both the traditional RB and the QoE-based optimization adap- tation approach [29]. The HB approach maximizes the average video quality and minimizes the rebuffering duration while maintaining the quality variation to a certain threshold. Finally, the proposed DQNReg is compared to the classical DQN algorithm. 4.7 Simulation Results The DQNReg model is evaluated on the testing datasets, both ﬁxed and mobile. The trained DQNReg

**Fragmento 12 - p. 13 - score 5:**

302– 306. [19] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, Comyco: Quality-aware adaptive video streaming via imitation learning, Proceed- ings of the 27th ACM International Conference on Multimedia, 2019, p. 429–437. [20] F. Chiariotti, S. D’Aronco, L. Toni, and P. Frossard, Online learning adaptation strategy for DASH clients, Proceedings of the 7th Interna- tional Conference on Multimedia Systems, 2016. [21] M. Gadaleta, F. Chiariotti, M. Rossi, and A. Zanella, D-DASH: A deep Q-learning frame- work for DASH video streaming, IEEE Trans- actions on Cognitive Communications and Net- working, vol. 3, no. 4, pp. 703–718, 2017. [22] J. Liu, X. Tao, and J. Lu, QoE-Oriented Rate Adaptation for DASH With Enhanced Deep Q- Learning, IEEE Access, vol.

**Fragmento 13 - p. 14 - score 5:**

Arora, Introduction to Optimum Design. Aca- demic Press, 2017. [31] H. Mukhtar, M. Hassan, and T. Landolsi, An occupancy-based and channel-aware multi-level adaptive scheme for video communications over wireless channels, EURASIP Journal on Wireless Communications and Networking, vol. 2011, 12 2011. [32] B. Wang, X. Luo, P. Hu, and F. Ren, Improving optimization-based rate adaptation in DASH sys- tem, 2017 26th International Conference on Com- puter Communication and Networks (ICCCN), 2017, pp. 1–9. [33] N. Bouten, S. Latr´e, J. Famaey, W. Van Leekwi- jck, and F. De Turck, In-network quality optimiza- tion for adaptive video streaming services, IEEE Transactions on Multimedia, vol. 16, no. 8, pp. 2281–2293, 2014.

**Fragmento 14 - p. 2 - score 4:**

Springer LATEX template Reinforcement Learning-Based Rate Adaptation in Dynamic Video Streaming N. A. Hafez, M. S. Hassan and T. Landolsi American University of Sharjah, Sharjah, UAE. *Corresponding author(s). E-mail(s): tlandolsi@aus.edu; Contributing authors: g00039071@aus.edu; mshassan@aus.edu; Abstract Video streaming stands out as the most signiﬁcant trafﬁc type consumed by mobile devices. This increased demand has been a major driver for research on bitrate adaptation algorithms. Bitrate adaptation ensures high user-perceived quality, which, in turn, correlates with higher proﬁts for content providers and delivery sys- tems. Dynamic adaptive streaming over HTTP (DASH) is a widely adopted video streaming standard utilized by service providers to provide competitive quality of experience (QoE).

**Fragmento 15 - p. 3 - score 4:**

For instance, the persistent bandwidth ﬂuctuations in the mobile network impose a challenge on ABR meth- ods [1]. In such a dynamic environment a ﬂexible ABR strategy is needed so as to intelligently adjust and maintain a good performance. In this paper, we demonstrate that an ABR strategy based on a machine learning (ML) technique, called reinforcement learning (RL), provides an intelligent and effective solution to the dynamic rate adaptation problem. In RL, an agent learns about the dynamic environment through trial-and-error interactions. The agent takes an action and receives a reward from the environment. The objective of an agent is to maxi- mize the discounted cumulative rewards by learning the optimal actions and then gradually converging to the optimal policy.

**Fragmento 16 - p. 3 - score 4:**

Every agent memorizes the conse- quences of his actions and avoids them if they resulted in low revenues in the past. With respect to the rate adaptation problem, the environment for RL includes the network throughput, the available video qualities of the video segments, and the video client playback buffer occupancy. In this paper, a RL-based deep Q-learning is pro- posed to achieve ﬁne video adaptation through the experience acquired from exploring the network envi- ronment. The objective is to achieve a fast conver- gence for the RL-based algorithm while enhancing the QoE performance under wireless local area net- works as well as 5G network conditions. The rest of this paper is organized as follows: Section II provides an overview of related work.

**Fragmento 17 - p. 3 - score 4:**

On the other hand, in the ML-based case the video playback system learns to adapt to the network environment even under unfore- seen conditions. Typically, network QoS parameters and video playback buffer information are used in these methods. 2.1 Traditional Adaptation Bitrate Techniques Heuristic-based techniques can be categorized into two types [4]. The ﬁrst type comprises a set of throughput-based techniques, in which a video client relies on observed network throughput to make a decision about the bitrates of future requested seg- ments [7]. The second type comprises a set of buffer- based techniques which utilize the available playback buffer space to determine the quality of the future requested segments [8].

**Fragmento 18 - p. 4 - score 4:**

Instead, it learns to make ABR decisions solely through observations of the resulting perfor- mance of past decisions. In [17], the authors incorporated an RL method with the addition of Q-Learning. The action is set as the segment request with a particular bitrate and the reward is deﬁned as the QoE approximation. The study maximizes the QoE through adjusting the adap- tation behavior as per the existing network conditions. Another learning based approach propose to combine the nearest neighbor (KNN) with Q-learning algo- rithm [18]. In this bitrate adaptive scenario, the KNN- Q learning can achieve higher QoE and faster conver- gence speed than the Q-learning algorithm alone. Authors in [19] introduce a system that trains the policy via imitating expert trajectories given by the instant solver.

**Fragmento 19 - p. 5 - score 4:**

Finally, the DQNReg-based rate adapta- tion technique is detailed. 3.1 Video Streaming Model In this paper, a video sequence is modeled as a set of Ns consecutive segments. Each segment lasts for Ts seconds, and is encoded at the bitrate Rv. The client video player requests a segment at bitrate Rv i for the i-th segment. The selected bitrate Rv i is mapped to different quality levels {Q1, Q2, . . . , QN} based on the client device speciﬁcations and the available video content. In general, The higher the bitrate used in encoding, the higher the video quality delivered to the viewer. Suppose that Qj is the quality level requested for the i-th segment, and let its corresponding bitrate be Rv i . If Li be the size of the i-th segment in bits then, for a constant bitrate (CBR) case, Li = TsRv i .

**Fragmento 20 - p. 6 - score 4:**

A reward function that represents these factors is introduced to issue policies that maximize the QoE perceived by the users. The reward function is deﬁned as follows [3, 16]: QoE = Rv i −µDB −∥Rv i+1 −Rv i ∥, (5) where Rv i is the bitrate of the i-th video segment, DB is the rebuffering duration experienced when the play- out buffer level, when a segment is downloaded, is lower than the needed segment download time. The rebuffering duration is given by: DB = Rv i Rn i Ts −T B i . (6) The parameter µ is a penalty coefﬁcient for the experi- enced rebuffering event. Finally, the term ∥Rv i+1−Rv i ∥ reﬂects the quality variation between two consecutive segments. 3.4 Rate Adaptation with DQNReg The DQNReg algorithm is implemented as follows: Once the segment is downloaded, the RL agent receives the state inputs at segment i, si = (Rv i−1, Rn i , T B i , T D i , NR), (7)

**Fragmento 21 - p. 7 - score 4:**

Springer LATEX template where Rv i−1 is the bitrate at which the last video seg- ment was downloaded, Rn i is the network throughput measurement, T B i is the current buffer level, T D i is the download time of the past video segment and NR is the available bitrate for the next video segment. The learning agent observes the state si from the environ- ment then takes an action ai which is selecting the bitrate for the upcoming video segment. In turn, the agent receives the corresponding reward. It is to be noted that the state transition in the environment is also impacted by the action taken. The action selected depends on the policy π, which is deﬁned as the mapping of the action to state or the probability distribution over actions.

**Fragmento 22 - p. 8 - score 4:**

The segment-wise QoE reward is estimated after each bitrate selection. 4.4 Video Parameters In the simulation, the video used is Big Buck Bunny, which is a simple animation short clip of 10 minutes and 34 seconds duration under the Peach open movie project. The video content consists of animated char- acters with a non intricate background [25]. The video in the dataset is encoded by the H.264/MPEG-4 codec to thirteen different representation rates, ranging from 235 kbps to 40 Mbps. The 4-second segment group is selected from the full DASH proﬁle. 4.5 Network Traces The proposed approach is examined using realistic network environment conditions. Real network traces are used from a ﬁxed WLAN [26] network and a mobile 5G network [1].

**Fragmento 23 - p. 9 - score 4:**

Springer LATEX template agent is employed to pick the rate of the video segment to be downloaded. Once the bitrate is selected, the bitrate is mapped to one of four quality levels to better illustrate the quality changes. The performance of the DQNReg agent for each channel environment type is illustrated. The DQNReg performance is compared to the benchmark approaches. Figures 3–6 illustrate the buffer occupancy and quality levels in both ﬁxed and mobile environments for DQNReg compared to the RB, HB, and DQN benchmark approaches. It is clear that both HB and DQN perform better than RB. Although RB maintains a relatively low number of quality jumps in differ- ent environments, it greatly suffers from rebuffering events.

**Fragmento 24 - p. 13 - score 4:**

Hu, and F. Ren, Improving optimization-based rate adaptation in DASH sys- tem, 2017 26th International Conference on Com- puter Communication and Networks (ICCCN), 2017, pp. 1–9. [12] T.-Y. Huang, R. Johari, N. McKeown, M. Trun- nell, and M. Watson, A buffer-based approach to rate adaptation: Evidence from a large video streaming service, SIGCOMM Comput. Com- mun. Rev., vol. 44, no. 4, p. 187–198, Aug. 2014. [13] R. K. P. Mok, X. Luo, E. W. W. Chan, and R. K. C. Chang, QDASH: A QoE-aware DASH System, Proceedings of the 3rd Multimedia Sys- tems Conference, 2012, p. 11–22. [14] L. Yu, T. Tillo, and J. Xiao, QoE-Driven Dynamic Adaptive Video Streaming Strategy With Future Information, IEEE Transactions on Broadcasting, vol. 63, no.

**Fragmento 25 - p. 14 - score 4:**

Springer LATEX template 13 [26] WLAN Throughput Project, Available: [online]: https://data.world/engrasifkhan/wlan- throughput/workspacef. [27] G-NetTrack Pro user manual. Available [online]: https://gyokovsolutions.com/manual-g-nettrack [28] J. Jiang, V. Sekar, and H. Zhang, Improving fairness, efﬁciency, and stability in HTTP-based adaptive video streaming with festive, IEEE/ACM Transactions on Networking, vol. 22, no. 01, pp. 326–340, jan. 2014. [29] N. A. Hafez, M. S. Hassan, T. Landolsi, Reformed QoE Based Approach in Bitrate- Adaptation for Dynamic Adaptive Streaming Sys- tems, To appear in the International Journal of Interdisciplinary Telecommunications and Net- working, Volume 14, Issue 1, 2022. [30] J.

**Fragmento 26 - p. 1 - score 3:**

Reinforcement Learning-Based Rate Adaptation in Dynamic Video Streaming Nada A. Hafez American University of Sharjah Mohamed S. Hassan American University of Sharjah Taha Landolsi (  tlandolsi@aus.edu ) American University of Sharjah https://orcid.org/0000-0001-8479-9056 Research Article Keywords: Bitrate Adaptation, DASH, Deep Q-learning, Optimization, Reinforcement Learning, Video Streaming Posted Date: August 22nd, 2022 DOI: https://doi.org/10.21203/rs.3.rs-1616726/v1 License:   This work is licensed under a Creative Commons Attribution 4.0 International License. Read Full License


### 7.4. reward qoe objetivo loss

Palabras clave usadas: `reward, QoE, quality of experience, utility, objective, loss, rebuffer, stall, stalling, smoothness, switching, quality variation, bitrate smoothness, video quality, penalty, consistent, consistency, risk, tail, latency`

**Fragmento 1 - p. 6 - score 6:**

Here, LReg is the DQNReg loss function, Q(st, at) is the Q-value penalty, α is a weight factor, and δ2 is the squared error. Classical DQN algorithms tend to overestimate the Q-value, which might be a potential problem [23]. It shows that the learned constraints starts early in the training. To address this issue and avoid overes- timation, the weighted penalty is added to DQNReg loss function as shown in equation (4). Consider- ing the characteristics of the DASH rate adaptation, DQNReg is expected to enable the trained agent to obtain improved QoE performance gain. The QoE- based reward function is explained in the following section. 3.3 Reward Function The QoE is impacted by the video quality of the viewed segment, the frequency of quality switching and the experienced re-buffering events.

**Fragmento 2 - p. 6 - score 5:**

A reward function that represents these factors is introduced to issue policies that maximize the QoE perceived by the users. The reward function is deﬁned as follows [3, 16]: QoE = Rv i −µDB −∥Rv i+1 −Rv i ∥, (5) where Rv i is the bitrate of the i-th video segment, DB is the rebuffering duration experienced when the play- out buffer level, when a segment is downloaded, is lower than the needed segment download time. The rebuffering duration is given by: DB = Rv i Rn i Ts −T B i . (6) The parameter µ is a penalty coefﬁcient for the experi- enced rebuffering event. Finally, the term ∥Rv i+1−Rv i ∥ reﬂects the quality variation between two consecutive segments. 3.4 Rate Adaptation with DQNReg The DQNReg algorithm is implemented as follows: Once the segment is downloaded, the RL agent receives the state inputs at segment i, si = (Rv i−1, Rn i , T B i , T D i , NR), (7)

**Fragmento 3 - p. 9 - score 5:**

3 Buffer occupancy for: a) RB, b) HB, c) DQN, and d) DQNReg methods in a WLAN environment. reward function is computed and normalized. High Average QoE reﬂect, high average video quality, low re-buffering duration and fewer quality switch- ing times. 2. Rebuffering times: Measures the number of instances when the buffer occupancy is zero. 3. Rebuffering duration: Measures the total rebuffering time over the entire video playback duration. 4. Inter-starvation length: Measures the time duration that separates successive rebuffering instants [31]. 5. Quality switching times: Counts the number of times the algorithm switches across different qual- ity levels. This reﬂects the number of times the user-perceived quality changes across the entire video playback.

**Fragmento 4 - p. 2 - score 4:**

The performance of this RL-based method is compared to three methods: A heuristic method, a model-based method, and a classical learning-based method. The com- parison shows that the RL-based method converges faster while achieving a high QoE score. In addition, it reduces the re-buffering duration while maintaining higher video quality and relatively lower quality variations. Keywords: Bitrate Adaptation, DASH, Deep Q-learning, Optimization, Reinforcement Learning, Video Streaming 1 Introduction With the constant updates to the wireless LAN (WLAN) standards and the gradual roll out of 5G mobile networks, wireless technology is expected to deliver high multi-Gbps peak data rates, ultra-low latency, increased reliability and decreased network management complexity [1].

**Fragmento 5 - p. 4 - score 4:**

A buffer-based adaptation approach that does not rely on throughput prediction methods is presented in [12]. The algorithm solves optimization problem based on the buffer length reservation. It downloads the lowest bitrate and tries to maintain the buffer occu- pancy within a certain threshold. Another adaptation logic based on optimization techniques is presented in [13] which introduces a novel probing based net- work measurement technique to advance the video quality selection. It also presents a QoE-aware DASH system, called QDASH, with mixed-integer linear pro- gramming. The authors in [14] used an optimization mechanism with two objective functions: The ﬁrst function maximizes the overall average QoE among DASH clients, while the second function minimizes the negative impact of temporal video quality changes; that is the up and down switching between different representation during playback.

**Fragmento 6 - p. 8 - score 4:**

The buffer status is not considered during the quality selection decision. The HB approach is a hybrid adaptation algorithm that combines both the traditional RB and the QoE-based optimization adap- tation approach [29]. The HB approach maximizes the average video quality and minimizes the rebuffering duration while maintaining the quality variation to a certain threshold. Finally, the proposed DQNReg is compared to the classical DQN algorithm. 4.7 Simulation Results The DQNReg model is evaluated on the testing datasets, both ﬁxed and mobile. The trained DQNReg

**Fragmento 7 - p. 12 - score 4:**

By analyzing the various indicators, it is noted that when using the DQNReg approach, the number of rebuffering times, the rebuffering duration and the quality switching times are suppressed to the lowest, while the quality switching times and inter-starvation lengths are maintained at a level comparable to other methods. Under various mobility patterns of real-time network, the average QoE performance of DQNReg is still superior to other methods. This indicates that the trained DQNReg learning agent has strong gen- eralization ability and can ﬂexibly adapt to various network conditions, so that the video service quality can match the network communication quality as well as possible. 6 Conclusions With increased user expectations and demands for uninterrupted viewing and top video quality, stud- ies concluded that users will leave video sessions if the quality is not adequate, harming the revenues of content providers.

**Fragmento 8 - p. 12 - score 4:**

Considering the intricate web- based video delivery ecosystem and its various bot- tlenecks, adaptive bitrate algorithms become essential to content providers to optimize video quality. This thesis proposed utilizing DQNReg, a reinforcement learning based technique that enhances the classical deep Q-learning method approach for video adapta- tion. A segment-wise QoE-based reward function is established so that the learning strategy can converge towards maximizing the QoE outcome. DQNReg have been thoroughly evaluated using trace-based simula- tion for ﬁxed and mobile networks. The DQNReg- based method outperforms classical DQN algorithm and other traditional adaptation approaches. Future research can integrate the initial start-up delay and the impact of latency onto the learning-based method, so that the learned policy can be improved with respect to the QoE.

**Fragmento 9 - p. 2 - score 3:**

Enhanced mobile broad- band with more uniform data rates and increased efﬁ- ciency empower new and improved user experiences. At the moment, video streaming stands out as the most signiﬁcant trafﬁc type consumed by mobile devices accounting for an average of 60% of total trafﬁc. This percentage is anticipated to increase to 74% by the end of 2024. Consumer behavior is shifting from low-deﬁnition (360p) and standard-deﬁnition formats (480p) to high-deﬁnition video (720p and 1080p) as network capabilities improve. In addition, viewer behavior is expected to change more dramatically as 5G services are made available [2]. The quality of experience (QoE) perceived by the users is affected by several factors like video quality, quality switch- ing and re-buffering duration [3] which are inﬂuenced by video streaming strategies which typically rely on adaptive bitrate (ABR) techniques for video streaming to enhance video delivery and customer satisfaction.

**Fragmento 10 - p. 2 - score 3:**

It is capable of providing seamless streaming via uncertain network conditions by switching across different video qualities and their correspond- ing video segment bitrates. The complexity of the video streaming environment makes it a good candidate for different learning-based approaches. Accordingly, this paper proposes a reinforcement-learning (RL) deep Q-network called DQNReg, that enhances the classical deep Q-learning method. A segment-wise QoE-based reward function is formulated so that the learning strategy can converge towards maximizing the QoE out- come. The proposed RL-based adaptation approach is evaluated using trace-based simulation for both wireless local area network channels and 5G mobile channels.

**Fragmento 11 - p. 5 - score 3:**

Springer LATEX template strategy for DASH clients based on an MDP optimiza- tion was proposed in [20]. The authors introduced a penalty function into the reward function to penalize the system for re-buffering events as well as moving away from a safe buffer level. Authors in [21] presented a framework, called D-DASH, that combines deep learning and reinforce- ment learning techniques to optimize the QoE of DASH. They combined feed-forward and recurrent deep neural networks with advanced strategies. The numerical results are obtained on real and simulated channels. Besides yielding a considerably higher QoE, the D-DASH framework exhibits fast convergence rate. Recently, the authors in [22] used enhanced deep Q-learning for DASH video applications, and proposed a QoE-oriented rate adaptation framework based on enhanced deep Q-learning.

**Fragmento 12 - p. 5 - score 3:**

They established chunk-wise subjective QoE model and utilize it as the reward function in reinforcement learning so that the strategy can converge toward the direction of maximizing the subjective QoE score. In our paper work, we use a reinforcement-based deep Q-learning method, called DQNReg [23], to provide a ﬁne video adaptation through the experi- ence acquired from exploring the network conditions. The objective of the proposed method is to enhance the QoE performance under dynamic network condi- tions, and achieve a fast convergence while maintain- ing higher average rewards than other learning-based methods. 3 Methodology In this section, the video streaming model is presented. The DQNReg algorithm and its reward function are introduced.

**Fragmento 13 - p. 9 - score 3:**

It is evident that RB does not manage the buffer occupancy well which would greatly impact its performance. It is noted that, with DQNReg both the buffer starvation instances (which cause rebuffer- ing events) and the frequency of quality switching are signiﬁcantly reduced compared to all other meth- ods. DQNReg outperforms other approaches in the two simulated environments as it does not suffer from rebuffering events in the ﬁxed environment, while maintains relatively frequency of quality vari- ations. Furthermore, DQNReg reduces the starvation instances in the mobile environment. Although DQN shows a relatively low number of rebuffering events, it struggles with quality variations, which is noticeably reduced in DQNReg.

**Fragmento 14 - p. 2 - score 2:**

Springer LATEX template Reinforcement Learning-Based Rate Adaptation in Dynamic Video Streaming N. A. Hafez, M. S. Hassan and T. Landolsi American University of Sharjah, Sharjah, UAE. *Corresponding author(s). E-mail(s): tlandolsi@aus.edu; Contributing authors: g00039071@aus.edu; mshassan@aus.edu; Abstract Video streaming stands out as the most signiﬁcant trafﬁc type consumed by mobile devices. This increased demand has been a major driver for research on bitrate adaptation algorithms. Bitrate adaptation ensures high user-perceived quality, which, in turn, correlates with higher proﬁts for content providers and delivery sys- tems. Dynamic adaptive streaming over HTTP (DASH) is a widely adopted video streaming standard utilized by service providers to provide competitive quality of experience (QoE).

**Fragmento 15 - p. 3 - score 2:**

For instance, the persistent bandwidth ﬂuctuations in the mobile network impose a challenge on ABR meth- ods [1]. In such a dynamic environment a ﬂexible ABR strategy is needed so as to intelligently adjust and maintain a good performance. In this paper, we demonstrate that an ABR strategy based on a machine learning (ML) technique, called reinforcement learning (RL), provides an intelligent and effective solution to the dynamic rate adaptation problem. In RL, an agent learns about the dynamic environment through trial-and-error interactions. The agent takes an action and receives a reward from the environment. The objective of an agent is to maxi- mize the discounted cumulative rewards by learning the optimal actions and then gradually converging to the optimal policy.

**Fragmento 16 - p. 3 - score 2:**

Every agent memorizes the conse- quences of his actions and avoids them if they resulted in low revenues in the past. With respect to the rate adaptation problem, the environment for RL includes the network throughput, the available video qualities of the video segments, and the video client playback buffer occupancy. In this paper, a RL-based deep Q-learning is pro- posed to achieve ﬁne video adaptation through the experience acquired from exploring the network envi- ronment. The objective is to achieve a fast conver- gence for the RL-based algorithm while enhancing the QoE performance under wireless local area net- works as well as 5G network conditions. The rest of this paper is organized as follows: Section II provides an overview of related work.

**Fragmento 17 - p. 3 - score 2:**

Authors in [9] presented a pre- diction model to accurately approximate the trend of buffer level variation in the client side. The quality switching in the adaptation is reduced based on the approximation. It can be concluded from the results that a steady video quality is achieved when buffer

**Fragmento 18 - p. 4 - score 2:**

Instead, it learns to make ABR decisions solely through observations of the resulting perfor- mance of past decisions. In [17], the authors incorporated an RL method with the addition of Q-Learning. The action is set as the segment request with a particular bitrate and the reward is deﬁned as the QoE approximation. The study maximizes the QoE through adjusting the adap- tation behavior as per the existing network conditions. Another learning based approach propose to combine the nearest neighbor (KNN) with Q-learning algo- rithm [18]. In this bitrate adaptive scenario, the KNN- Q learning can achieve higher QoE and faster conver- gence speed than the Q-learning algorithm alone. Authors in [19] introduce a system that trains the policy via imitating expert trajectories given by the instant solver.

**Fragmento 19 - p. 4 - score 2:**

2.2 RL-Based Adaptation Existing classic ABR algorithms mostly rely on ﬁxed heuristics that have been ﬁne tuned according to ﬁxed assumptions about deployment environments. Not only that, but each of these approaches have been designed to optimize for a speciﬁc QoE metric. Consequently, if the assumptions are breached, these ABR algorithms fail to generalize and perform poorly. To overcome these issues, learning-based adaptation approaches are explored. With machine learning tech- niques a client can learn to adapt its video quality to the changing context without the need for any human intervention. Authors in [15] use a decision-tree based random forest classiﬁcation to map network related features onto the video rate.

**Fragmento 20 - p. 4 - score 2:**

The system attempts to pick the seg- ment with higher perceptual video qualities rather than video bitrates by constructing a neural network archi- tecture, video datasets and QoE metrics with video quality features. Another online learning adaptation

**Fragmento 21 - p. 5 - score 2:**

Finally, the DQNReg-based rate adapta- tion technique is detailed. 3.1 Video Streaming Model In this paper, a video sequence is modeled as a set of Ns consecutive segments. Each segment lasts for Ts seconds, and is encoded at the bitrate Rv. The client video player requests a segment at bitrate Rv i for the i-th segment. The selected bitrate Rv i is mapped to different quality levels {Q1, Q2, . . . , QN} based on the client device speciﬁcations and the available video content. In general, The higher the bitrate used in encoding, the higher the video quality delivered to the viewer. Suppose that Qj is the quality level requested for the i-th segment, and let its corresponding bitrate be Rv i . If Li be the size of the i-th segment in bits then, for a constant bitrate (CBR) case, Li = TsRv i .

**Fragmento 22 - p. 5 - score 2:**

It builds on the classical DQN algorithm by adding a weighted penalty to the normal squared Bellman error. The authors in [23] proposed evolution strategies by exploring the space of compu- tational graphs which calculates the loss function for an RL agent. They highlighted that DQNReg shows an improved performance over DQN in environments that have not been experienced during training. Their analysis showed that DQNReg outperforms DQN as well other well-known variants such as the double DQN (DDQN). DQNReg is typically characterized with the following set of equations [23]: Yt = rt + γ max a Qtarg(st+1, a), (2) δ = Q(st, at) −Yt, (3)

**Fragmento 23 - p. 6 - score 2:**

Springer LATEX template 5 Adaptation Algorithm Video Player 1 7 6 5 4 3 2 8 9 Server 1 7 6 5 4 3 2 8 9 QL1 1 7 6 5 4 3 2 8 9 QL2 1 7 6 5 4 3 2 8 9 QL3 Segment S7-QL3 Video sequence with 3 quality levels Received Video Segments New HTTP Requests Past segment params.: 1. Network throughput,   2. Segment bit rate,   3. Buffer occupancy,   QL1 QL2 QL3 HTTP GET S1-QL1, … , S3-QL1 1 2 3 HTTP GET S4-QL2, … , S6-QL2 4 5 6 HTTP GET S7-QL3, … , S9-QL3 7 8 9 Quality Selection HTTP Responses 1 4 7         DQNReg network with reward function: action RL agent Wireless Network (WLAN or 5G) Fig. 1 Proposed RL-based rate adaptation scheme using a DQNReg network. LReg = αQ(st, at) + δ2, (4) where Yt is the target Q-value at the time step t, rt is the instantaneous reward, at is the instantaneous action output by the agent to the environment, γ is a discount factor, δ is the DQN loss function, and st and st+1 are the states at t and t + 1, respectively.

**Fragmento 24 - p. 7 - score 2:**

Once the obser- vation states are collected by the agent, the Q-value table or the weights in the network are updated until the policy converges. Certain hyper-parameters were set similar to [16, 21, 22]. The weight factor used here is α = 0.1, the discount factor is γ = 0.99, the learning rate is 10−5 and the exploration adopted was the ǫ-greedy to explore many states and have a maintain a trade-off between exploration and exploita- tion. The training algorithm takes the bitrate selection for a video segment as a step, it then takes the step experience and stores it into the experience buffer. In Figure 2, the average QoE reward on the training set is plotted against the number of training episodes for both DQNReg and DQN.

**Fragmento 25 - p. 8 - score 2:**

Springer LATEX template 7 the video playback during the download, the playback buffer is drained by the current segment download time. In case the playback buffer is fully occupied, 500ms delay is applied before fetching the other seg- ment. After each segment download, various state observations such as buffer occupancy and current segment bitrate are passed to the learning agent. The learning agent then tries to maximize the reward QoE value, which is impacted by the varying network con- ditions. To design a network that faithfully emulates real conditions, throughput from a corpus of real net- work traces were used. The traces are used to shape the agent’s experience and help it predict the environment dynamics such as the anticipated network through- put.

**Fragmento 26 - p. 8 - score 2:**

The segment-wise QoE reward is estimated after each bitrate selection. 4.4 Video Parameters In the simulation, the video used is Big Buck Bunny, which is a simple animation short clip of 10 minutes and 34 seconds duration under the Peach open movie project. The video content consists of animated char- acters with a non intricate background [25]. The video in the dataset is encoded by the H.264/MPEG-4 codec to thirteen different representation rates, ranging from 235 kbps to 40 Mbps. The 4-second segment group is selected from the full DASH proﬁle. 4.5 Network Traces The proposed approach is examined using realistic network environment conditions. Real network traces are used from a ﬁxed WLAN [26] network and a mobile 5G network [1].


### 7.5. entrenamiento optimizacion pipeline

Palabras clave usadas: `training, train, trained, episode, epoch, optimizer, learning rate, loss function, minibatch, clipped, probability ratio, experience, simulation, simulator, emulation, testbed, fine-tuning, pretrain, learning task, meta-training, adaptation, oracle, auto-tuning, offline, online`

**Fragmento 1 - p. 6 - score 6:**

Here, LReg is the DQNReg loss function, Q(st, at) is the Q-value penalty, α is a weight factor, and δ2 is the squared error. Classical DQN algorithms tend to overestimate the Q-value, which might be a potential problem [23]. It shows that the learned constraints starts early in the training. To address this issue and avoid overes- timation, the weighted penalty is added to DQNReg loss function as shown in equation (4). Consider- ing the characteristics of the DASH rate adaptation, DQNReg is expected to enable the trained agent to obtain improved QoE performance gain. The QoE- based reward function is explained in the following section. 3.3 Reward Function The QoE is impacted by the video quality of the viewed segment, the frequency of quality switching and the experienced re-buffering events.

**Fragmento 2 - p. 7 - score 5:**

Once the obser- vation states are collected by the agent, the Q-value table or the weights in the network are updated until the policy converges. Certain hyper-parameters were set similar to [16, 21, 22]. The weight factor used here is α = 0.1, the discount factor is γ = 0.99, the learning rate is 10−5 and the exploration adopted was the ǫ-greedy to explore many states and have a maintain a trade-off between exploration and exploita- tion. The training algorithm takes the bitrate selection for a video segment as a step, it then takes the step experience and stores it into the experience buffer. In Figure 2, the average QoE reward on the training set is plotted against the number of training episodes for both DQNReg and DQN.

**Fragmento 3 - p. 8 - score 5:**

It is necessary to note that the quality of the dataset impacts the performance of the learning agent. These traces allow the agent to experience throughput variations in real networks. 4.3 Simulation Setup A simulation testbed based on the video streaming environment is implemented in SimEvent discrete- event simulator in MATLAB. The testbed simulates the video player buffer dynamics during the process of receiving and playing back video segments based on a bitrate range and network proﬁles. To train the agent a corpus of network traces is created through con- catenating different excerpts of the network datasets, which will be detailed in the section below. The size of the buffer is set T B max = 60s which is common in a DASH video player.

**Fragmento 4 - p. 5 - score 4:**

It builds on the classical DQN algorithm by adding a weighted penalty to the normal squared Bellman error. The authors in [23] proposed evolution strategies by exploring the space of compu- tational graphs which calculates the loss function for an RL agent. They highlighted that DQNReg shows an improved performance over DQN in environments that have not been experienced during training. Their analysis showed that DQNReg outperforms DQN as well other well-known variants such as the double DQN (DDQN). DQNReg is typically characterized with the following set of equations [23]: Yt = rt + γ max a Qtarg(st+1, a), (2) δ = Q(st, at) −Yt, (3)

**Fragmento 5 - p. 7 - score 4:**

The DQNReg simulation results are contrasted with other benchmark approaches. 0 100 200 300 400 500 600 700 800 900 1000 Episode Number 0.7 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5 1.6 Average QoE DQNReg DQN Fig. 2 Training convergence of DQNReg vs. DQN methods. 4.1 Implementation and Training algorithm The neural network architecture, similar to [16] and [22], is composed of 1D convolution layer com- posed of 128 ﬁlters. The output of these layers is then aggregated with other inputs in a hidden layer, that uses 128 neurons, to apply the rectiﬁed linear unit (ReLU) activation function.The number of neu- rons in the output layer is equal to the adaptive bitrate set, which we have denoted as NR. The training is performed on a sequence extracted from the Big Buck Bunny video (available for download from the Blender.org site [24], for example).

**Fragmento 6 - p. 8 - score 4:**

The buffer status is not considered during the quality selection decision. The HB approach is a hybrid adaptation algorithm that combines both the traditional RB and the QoE-based optimization adap- tation approach [29]. The HB approach maximizes the average video quality and minimizes the rebuffering duration while maintaining the quality variation to a certain threshold. Finally, the proposed DQNReg is compared to the classical DQN algorithm. 4.7 Simulation Results The DQNReg model is evaluated on the testing datasets, both ﬁxed and mobile. The trained DQNReg

**Fragmento 7 - p. 7 - score 3:**

π(si, ai) is the probability that action ai is taken in si. Practically, there are intractably several si, ai pairs, to overcome this a neural network is utilized to represent the pol- icy with manageable number of parameters θ, usually referred to as policy parameters. The advantage of neural networks is that they can deal with raw signals and do not need to have hand-crafted features. In value-based RL, the agent along side the neu- ral network is expected to extract important features from the state, provide accurate estimation of the state- action value and ﬁnally derive the optimal policy. For a well-trained value network the optimal policy is derived as follows: πθ = arg max a Q(si, a). (8) The learning process of the agent is the training pro- cess of the state-action value network.

**Fragmento 8 - p. 2 - score 2:**

Springer LATEX template Reinforcement Learning-Based Rate Adaptation in Dynamic Video Streaming N. A. Hafez, M. S. Hassan and T. Landolsi American University of Sharjah, Sharjah, UAE. *Corresponding author(s). E-mail(s): tlandolsi@aus.edu; Contributing authors: g00039071@aus.edu; mshassan@aus.edu; Abstract Video streaming stands out as the most signiﬁcant trafﬁc type consumed by mobile devices. This increased demand has been a major driver for research on bitrate adaptation algorithms. Bitrate adaptation ensures high user-perceived quality, which, in turn, correlates with higher proﬁts for content providers and delivery sys- tems. Dynamic adaptive streaming over HTTP (DASH) is a widely adopted video streaming standard utilized by service providers to provide competitive quality of experience (QoE).

**Fragmento 9 - p. 2 - score 2:**

It is capable of providing seamless streaming via uncertain network conditions by switching across different video qualities and their correspond- ing video segment bitrates. The complexity of the video streaming environment makes it a good candidate for different learning-based approaches. Accordingly, this paper proposes a reinforcement-learning (RL) deep Q-network called DQNReg, that enhances the classical deep Q-learning method. A segment-wise QoE-based reward function is formulated so that the learning strategy can converge towards maximizing the QoE out- come. The proposed RL-based adaptation approach is evaluated using trace-based simulation for both wireless local area network channels and 5G mobile channels.

**Fragmento 10 - p. 3 - score 2:**

Section III describes the methodology. Section IV details the implementation and the simulation setup. Section V is dedicated to the performance evaluation of the proposed approach and section VI gives the conclusions of this study. 2 Literature review of existing solutions Adaptation methods and algorithms are still under- going extensive research work regardless of the pub- lic adoption [4–6]. This is owed to the contin- uously updated internet video delivery ecosystem. This section illustrates the various classic adaptation approaches. The existing approaches are classiﬁed into two main categories; Traditional adaptation tech- niques and ML-based adaptation methods. In the tra- ditional adaptation case, the solutions are customized for predetermined scenarios.

**Fragmento 11 - p. 3 - score 2:**

Every agent memorizes the conse- quences of his actions and avoids them if they resulted in low revenues in the past. With respect to the rate adaptation problem, the environment for RL includes the network throughput, the available video qualities of the video segments, and the video client playback buffer occupancy. In this paper, a RL-based deep Q-learning is pro- posed to achieve ﬁne video adaptation through the experience acquired from exploring the network envi- ronment. The objective is to achieve a fast conver- gence for the RL-based algorithm while enhancing the QoE performance under wireless local area net- works as well as 5G network conditions. The rest of this paper is organized as follows: Section II provides an overview of related work.

**Fragmento 12 - p. 4 - score 2:**

The scheme trains the classiﬁ- cation model using a dataset. The classiﬁer is then used to predict the current request or any future video request. RL allows an agent to discover the right action to take, within a particular context, based on feed- back from its environment. To do this, an adaptation module interacts with its environment by sensing fac- tors that are expected to inﬂuence its decision. For example, in [16], a system that generates ABR algo- rithms using RL is introduced. This system trains a neural network model that selects bitrates for future video segments based on observations collected by client video players. This system does not rely on pre-programmed models or assumptions about the environment.

**Fragmento 13 - p. 4 - score 2:**

The system attempts to pick the seg- ment with higher perceptual video qualities rather than video bitrates by constructing a neural network archi- tecture, video datasets and QoE metrics with video quality features. Another online learning adaptation

**Fragmento 14 - p. 6 - score 2:**

Springer LATEX template 5 Adaptation Algorithm Video Player 1 7 6 5 4 3 2 8 9 Server 1 7 6 5 4 3 2 8 9 QL1 1 7 6 5 4 3 2 8 9 QL2 1 7 6 5 4 3 2 8 9 QL3 Segment S7-QL3 Video sequence with 3 quality levels Received Video Segments New HTTP Requests Past segment params.: 1. Network throughput,   2. Segment bit rate,   3. Buffer occupancy,   QL1 QL2 QL3 HTTP GET S1-QL1, … , S3-QL1 1 2 3 HTTP GET S4-QL2, … , S6-QL2 4 5 6 HTTP GET S7-QL3, … , S9-QL3 7 8 9 Quality Selection HTTP Responses 1 4 7         DQNReg network with reward function: action RL agent Wireless Network (WLAN or 5G) Fig. 1 Proposed RL-based rate adaptation scheme using a DQNReg network. LReg = αQ(st, at) + δ2, (4) where Yt is the target Q-value at the time step t, rt is the instantaneous reward, at is the instantaneous action output by the agent to the environment, γ is a discount factor, δ is the DQN loss function, and st and st+1 are the states at t and t + 1, respectively.

**Fragmento 15 - p. 6 - score 2:**

A reward function that represents these factors is introduced to issue policies that maximize the QoE perceived by the users. The reward function is deﬁned as follows [3, 16]: QoE = Rv i −µDB −∥Rv i+1 −Rv i ∥, (5) where Rv i is the bitrate of the i-th video segment, DB is the rebuffering duration experienced when the play- out buffer level, when a segment is downloaded, is lower than the needed segment download time. The rebuffering duration is given by: DB = Rv i Rn i Ts −T B i . (6) The parameter µ is a penalty coefﬁcient for the experi- enced rebuffering event. Finally, the term ∥Rv i+1−Rv i ∥ reﬂects the quality variation between two consecutive segments. 3.4 Rate Adaptation with DQNReg The DQNReg algorithm is implemented as follows: Once the segment is downloaded, the RL agent receives the state inputs at segment i, si = (Rv i−1, Rn i , T B i , T D i , NR), (7)

**Fragmento 16 - p. 7 - score 2:**

By regularly observing the environment, the agent gathers tuples containing the previous state, the new state, the action to be undertaken, and the reward to be given to the learner. The temporal-difference technique is then applied to perform gradient descent [22]. This allows the value network to estimate the real state-action value function with adequate accuracy. 4 Implementation and Simulation This section showcases the implementation of the pro- posed DQNReg-based adaptation approach with the simulation setup, the video parameters, and network traces. It is noteworthy to indicate that the neural net- work architecture is not a priority of this paper, hence a default network architecture was adopted for the simu- lation.

**Fragmento 17 - p. 9 - score 2:**

5 Performance Evaluation and Discussion After performing extensive simulations in different network environments, the performance of the sim- ulated approaches is analyzed and evaluated. The evaluation metrics used are explained then the DQN- Reg adaptation approach is evaluated and compared to the aforementioned benchmark approaches. 5.1 Evaluation Metrics The proposed method’s performance is evaluated using the following metrics: 1. Average QoE: The QoE objective is a sum of weighted objectives that have varying orders of magnitudes. To make fair comparisons it is impor- tant to transform the objective functions in a way that they all have comparable orders of magni- tude [30]. The average QoE, calculated through the 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) a) 260 280 300 320 340 360 380 400 420 440 460 Time (s) 0 20 40 60 Buffer Length (s) b) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) c) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) d) Fig.

**Fragmento 18 - p. 12 - score 2:**

By analyzing the various indicators, it is noted that when using the DQNReg approach, the number of rebuffering times, the rebuffering duration and the quality switching times are suppressed to the lowest, while the quality switching times and inter-starvation lengths are maintained at a level comparable to other methods. Under various mobility patterns of real-time network, the average QoE performance of DQNReg is still superior to other methods. This indicates that the trained DQNReg learning agent has strong gen- eralization ability and can ﬂexibly adapt to various network conditions, so that the video service quality can match the network communication quality as well as possible. 6 Conclusions With increased user expectations and demands for uninterrupted viewing and top video quality, stud- ies concluded that users will leave video sessions if the quality is not adequate, harming the revenues of content providers.

**Fragmento 19 - p. 13 - score 2:**

302– 306. [19] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, Comyco: Quality-aware adaptive video streaming via imitation learning, Proceed- ings of the 27th ACM International Conference on Multimedia, 2019, p. 429–437. [20] F. Chiariotti, S. D’Aronco, L. Toni, and P. Frossard, Online learning adaptation strategy for DASH clients, Proceedings of the 7th Interna- tional Conference on Multimedia Systems, 2016. [21] M. Gadaleta, F. Chiariotti, M. Rossi, and A. Zanella, D-DASH: A deep Q-learning frame- work for DASH video streaming, IEEE Trans- actions on Cognitive Communications and Net- working, vol. 3, no. 4, pp. 703–718, 2017. [22] J. Liu, X. Tao, and J. Lu, QoE-Oriented Rate Adaptation for DASH With Enhanced Deep Q- Learning, IEEE Access, vol.

**Fragmento 20 - p. 14 - score 2:**

Springer LATEX template 13 [26] WLAN Throughput Project, Available: [online]: https://data.world/engrasifkhan/wlan- throughput/workspacef. [27] G-NetTrack Pro user manual. Available [online]: https://gyokovsolutions.com/manual-g-nettrack [28] J. Jiang, V. Sekar, and H. Zhang, Improving fairness, efﬁciency, and stability in HTTP-based adaptive video streaming with festive, IEEE/ACM Transactions on Networking, vol. 22, no. 01, pp. 326–340, jan. 2014. [29] N. A. Hafez, M. S. Hassan, T. Landolsi, Reformed QoE Based Approach in Bitrate- Adaptation for Dynamic Adaptive Streaming Sys- tems, To appear in the International Journal of Interdisciplinary Telecommunications and Net- working, Volume 14, Issue 1, 2022. [30] J.

**Fragmento 21 - p. 1 - score 1:**

Reinforcement Learning-Based Rate Adaptation in Dynamic Video Streaming Nada A. Hafez American University of Sharjah Mohamed S. Hassan American University of Sharjah Taha Landolsi (  tlandolsi@aus.edu ) American University of Sharjah https://orcid.org/0000-0001-8479-9056 Research Article Keywords: Bitrate Adaptation, DASH, Deep Q-learning, Optimization, Reinforcement Learning, Video Streaming Posted Date: August 22nd, 2022 DOI: https://doi.org/10.21203/rs.3.rs-1616726/v1 License:   This work is licensed under a Creative Commons Attribution 4.0 International License. Read Full License

**Fragmento 22 - p. 2 - score 1:**

Enhanced mobile broad- band with more uniform data rates and increased efﬁ- ciency empower new and improved user experiences. At the moment, video streaming stands out as the most signiﬁcant trafﬁc type consumed by mobile devices accounting for an average of 60% of total trafﬁc. This percentage is anticipated to increase to 74% by the end of 2024. Consumer behavior is shifting from low-deﬁnition (360p) and standard-deﬁnition formats (480p) to high-deﬁnition video (720p and 1080p) as network capabilities improve. In addition, viewer behavior is expected to change more dramatically as 5G services are made available [2]. The quality of experience (QoE) perceived by the users is affected by several factors like video quality, quality switch- ing and re-buffering duration [3] which are inﬂuenced by video streaming strategies which typically rely on adaptive bitrate (ABR) techniques for video streaming to enhance video delivery and customer satisfaction.

**Fragmento 23 - p. 2 - score 1:**

The performance of this RL-based method is compared to three methods: A heuristic method, a model-based method, and a classical learning-based method. The com- parison shows that the RL-based method converges faster while achieving a high QoE score. In addition, it reduces the re-buffering duration while maintaining higher video quality and relatively lower quality variations. Keywords: Bitrate Adaptation, DASH, Deep Q-learning, Optimization, Reinforcement Learning, Video Streaming 1 Introduction With the constant updates to the wireless LAN (WLAN) standards and the gradual roll out of 5G mobile networks, wireless technology is expected to deliver high multi-Gbps peak data rates, ultra-low latency, increased reliability and decreased network management complexity [1].

**Fragmento 24 - p. 3 - score 1:**

For instance, the persistent bandwidth ﬂuctuations in the mobile network impose a challenge on ABR meth- ods [1]. In such a dynamic environment a ﬂexible ABR strategy is needed so as to intelligently adjust and maintain a good performance. In this paper, we demonstrate that an ABR strategy based on a machine learning (ML) technique, called reinforcement learning (RL), provides an intelligent and effective solution to the dynamic rate adaptation problem. In RL, an agent learns about the dynamic environment through trial-and-error interactions. The agent takes an action and receives a reward from the environment. The objective of an agent is to maxi- mize the discounted cumulative rewards by learning the optimal actions and then gradually converging to the optimal policy.

**Fragmento 25 - p. 3 - score 1:**

On the other hand, in the ML-based case the video playback system learns to adapt to the network environment even under unfore- seen conditions. Typically, network QoS parameters and video playback buffer information are used in these methods. 2.1 Traditional Adaptation Bitrate Techniques Heuristic-based techniques can be categorized into two types [4]. The ﬁrst type comprises a set of throughput-based techniques, in which a video client relies on observed network throughput to make a decision about the bitrates of future requested seg- ments [7]. The second type comprises a set of buffer- based techniques which utilize the available playback buffer space to determine the quality of the future requested segments [8].

**Fragmento 26 - p. 3 - score 1:**

Authors in [9] presented a pre- diction model to accurately approximate the trend of buffer level variation in the client side. The quality switching in the adaptation is reduced based on the approximation. It can be concluded from the results that a steady video quality is achieved when buffer


### 7.6. datos trazas datasets origen

Palabras clave usadas: `dataset, datasets, trace, traces, network trace, bandwidth trace, real-world, FCC, HSDPA, Norway, LTE, 4G, 5G, WiFi, WLAN, Mahimahi, emulation, testbed, Puffer, data, sessions, users, video, chunk, streaming server`

**Fragmento 1 - p. 8 - score 8:**

It is necessary to note that the quality of the dataset impacts the performance of the learning agent. These traces allow the agent to experience throughput variations in real networks. 4.3 Simulation Setup A simulation testbed based on the video streaming environment is implemented in SimEvent discrete- event simulator in MATLAB. The testbed simulates the video player buffer dynamics during the process of receiving and playing back video segments based on a bitrate range and network proﬁles. To train the agent a corpus of network traces is created through con- catenating different excerpts of the network datasets, which will be detailed in the section below. The size of the buffer is set T B max = 60s which is common in a DASH video player.

**Fragmento 2 - p. 8 - score 8:**

The segment-wise QoE reward is estimated after each bitrate selection. 4.4 Video Parameters In the simulation, the video used is Big Buck Bunny, which is a simple animation short clip of 10 minutes and 34 seconds duration under the Peach open movie project. The video content consists of animated char- acters with a non intricate background [25]. The video in the dataset is encoded by the H.264/MPEG-4 codec to thirteen different representation rates, ranging from 235 kbps to 40 Mbps. The 4-second segment group is selected from the full DASH proﬁle. 4.5 Network Traces The proposed approach is examined using realistic network environment conditions. Real network traces are used from a ﬁxed WLAN [26] network and a mobile 5G network [1].

**Fragmento 3 - p. 8 - score 6:**

It is important to note the difference in the offered throughput and the mobility pattern in the two networks as it affects the quality and the performance of the approaches. 4.5.1 WLAN Channel Environment The average WLAN network throughput trace is obtained from [26] and used in the deployed algo- rithm. The throughput is limited to less than 2 Mbps. The dataset contains client-side cellular key perfor- mance indicators such as throughput information and other context related metrics. 4.5.2 Mobile Channel Environment The 5G network trace is taken from a publicly avail- able dataset which was collected from a mobile oper- ator [1]. The dataset is created from a static and a driving vehicle mobility patterns, where the net- work throughput reaches up to 200 Mbps.

**Fragmento 4 - p. 2 - score 4:**

Enhanced mobile broad- band with more uniform data rates and increased efﬁ- ciency empower new and improved user experiences. At the moment, video streaming stands out as the most signiﬁcant trafﬁc type consumed by mobile devices accounting for an average of 60% of total trafﬁc. This percentage is anticipated to increase to 74% by the end of 2024. Consumer behavior is shifting from low-deﬁnition (360p) and standard-deﬁnition formats (480p) to high-deﬁnition video (720p and 1080p) as network capabilities improve. In addition, viewer behavior is expected to change more dramatically as 5G services are made available [2]. The quality of experience (QoE) perceived by the users is affected by several factors like video quality, quality switch- ing and re-buffering duration [3] which are inﬂuenced by video streaming strategies which typically rely on adaptive bitrate (ABR) techniques for video streaming to enhance video delivery and customer satisfaction.

**Fragmento 5 - p. 2 - score 4:**

The performance of this RL-based method is compared to three methods: A heuristic method, a model-based method, and a classical learning-based method. The com- parison shows that the RL-based method converges faster while achieving a high QoE score. In addition, it reduces the re-buffering duration while maintaining higher video quality and relatively lower quality variations. Keywords: Bitrate Adaptation, DASH, Deep Q-learning, Optimization, Reinforcement Learning, Video Streaming 1 Introduction With the constant updates to the wireless LAN (WLAN) standards and the gradual roll out of 5G mobile networks, wireless technology is expected to deliver high multi-Gbps peak data rates, ultra-low latency, increased reliability and decreased network management complexity [1].

**Fragmento 6 - p. 4 - score 4:**

The system attempts to pick the seg- ment with higher perceptual video qualities rather than video bitrates by constructing a neural network archi- tecture, video datasets and QoE metrics with video quality features. Another online learning adaptation

**Fragmento 7 - p. 7 - score 4:**

By regularly observing the environment, the agent gathers tuples containing the previous state, the new state, the action to be undertaken, and the reward to be given to the learner. The temporal-difference technique is then applied to perform gradient descent [22]. This allows the value network to estimate the real state-action value function with adequate accuracy. 4 Implementation and Simulation This section showcases the implementation of the pro- posed DQNReg-based adaptation approach with the simulation setup, the video parameters, and network traces. It is noteworthy to indicate that the neural net- work architecture is not a priority of this paper, hence a default network architecture was adopted for the simu- lation.

**Fragmento 8 - p. 8 - score 4:**

The buffer status is not considered during the quality selection decision. The HB approach is a hybrid adaptation algorithm that combines both the traditional RB and the QoE-based optimization adap- tation approach [29]. The HB approach maximizes the average video quality and minimizes the rebuffering duration while maintaining the quality variation to a certain threshold. Finally, the proposed DQNReg is compared to the classical DQN algorithm. 4.7 Simulation Results The DQNReg model is evaluated on the testing datasets, both ﬁxed and mobile. The trained DQNReg

**Fragmento 9 - p. 12 - score 4:**

References [1] D. Raca, D. Leahy, C. J. Sreenan, and J. J. Quin- lan, Beyond Throughput, the Next Generation: A 5G Dataset with Channel and Context Met- rics, Proceedings of the 11th ACM Multimedia Systems Conference, 2020, p. 303–308. [2] Ericsson 2018 mobility report. Available [online]: www.ericsson.com [3] X. Yin, A. Jindal, A. Sekar, and B. Sinopoli, A control-theoretic approach for dynamic adaptive video streaming over HTTP, ACM Conference on SIGCOMM, 2015. [4] M. J. Khan, S. Harous, and A. Bentaleb, Client- driven adaptive bitrate techniques for media streaming over HTTP: Initial ﬁndings, 2020 IEEE International Conference on Electro Information Technology (EIT), 2020, pp. 053–059. [5] H. Yuan, S. Zhao, J. Hou, X.

**Fragmento 10 - p. 13 - score 4:**

7, pp. 8454–8469, 2019. [23] J. D. Co-Reyes, Y. Miao, D. Peng, E. Real, Q. V. Le, S. Levine, H. Lee, and A. Faust, Evolving reinforcement learning algorithms, International Conference on Learning Representations, 2021. [24] Big Buck Bunny video. Available [online]: download.blender.org/demo/movies/BBB. [25] J. J. Quinlan and C. J. Sreenan, Multi-proﬁle ultra high deﬁnition (UHD) AVC and HEVC 4k DASH datasets, Proceedings of the 9th ACM Multimedia Systems Conference, 2018, p. 375–380.

**Fragmento 11 - p. 2 - score 3:**

It is capable of providing seamless streaming via uncertain network conditions by switching across different video qualities and their correspond- ing video segment bitrates. The complexity of the video streaming environment makes it a good candidate for different learning-based approaches. Accordingly, this paper proposes a reinforcement-learning (RL) deep Q-network called DQNReg, that enhances the classical deep Q-learning method. A segment-wise QoE-based reward function is formulated so that the learning strategy can converge towards maximizing the QoE out- come. The proposed RL-based adaptation approach is evaluated using trace-based simulation for both wireless local area network channels and 5G mobile channels.

**Fragmento 12 - p. 3 - score 3:**

Every agent memorizes the conse- quences of his actions and avoids them if they resulted in low revenues in the past. With respect to the rate adaptation problem, the environment for RL includes the network throughput, the available video qualities of the video segments, and the video client playback buffer occupancy. In this paper, a RL-based deep Q-learning is pro- posed to achieve ﬁne video adaptation through the experience acquired from exploring the network envi- ronment. The objective is to achieve a fast conver- gence for the RL-based algorithm while enhancing the QoE performance under wireless local area net- works as well as 5G network conditions. The rest of this paper is organized as follows: Section II provides an overview of related work.

**Fragmento 13 - p. 4 - score 3:**

The scheme trains the classiﬁ- cation model using a dataset. The classiﬁer is then used to predict the current request or any future video request. RL allows an agent to discover the right action to take, within a particular context, based on feed- back from its environment. To do this, an adaptation module interacts with its environment by sensing fac- tors that are expected to inﬂuence its decision. For example, in [16], a system that generates ABR algo- rithms using RL is introduced. This system trains a neural network model that selects bitrates for future video segments based on observations collected by client video players. This system does not rely on pre-programmed models or assumptions about the environment.

**Fragmento 14 - p. 6 - score 3:**

Springer LATEX template 5 Adaptation Algorithm Video Player 1 7 6 5 4 3 2 8 9 Server 1 7 6 5 4 3 2 8 9 QL1 1 7 6 5 4 3 2 8 9 QL2 1 7 6 5 4 3 2 8 9 QL3 Segment S7-QL3 Video sequence with 3 quality levels Received Video Segments New HTTP Requests Past segment params.: 1. Network throughput,   2. Segment bit rate,   3. Buffer occupancy,   QL1 QL2 QL3 HTTP GET S1-QL1, … , S3-QL1 1 2 3 HTTP GET S4-QL2, … , S6-QL2 4 5 6 HTTP GET S7-QL3, … , S9-QL3 7 8 9 Quality Selection HTTP Responses 1 4 7         DQNReg network with reward function: action RL agent Wireless Network (WLAN or 5G) Fig. 1 Proposed RL-based rate adaptation scheme using a DQNReg network. LReg = αQ(st, at) + δ2, (4) where Yt is the target Q-value at the time step t, rt is the instantaneous reward, at is the instantaneous action output by the agent to the environment, γ is a discount factor, δ is the DQN loss function, and st and st+1 are the states at t and t + 1, respectively.

**Fragmento 15 - p. 8 - score 3:**

Springer LATEX template 7 the video playback during the download, the playback buffer is drained by the current segment download time. In case the playback buffer is fully occupied, 500ms delay is applied before fetching the other seg- ment. After each segment download, various state observations such as buffer occupancy and current segment bitrate are passed to the learning agent. The learning agent then tries to maximize the reward QoE value, which is impacted by the varying network con- ditions. To design a network that faithfully emulates real conditions, throughput from a corpus of real net- work traces were used. The traces are used to shape the agent’s experience and help it predict the environment dynamics such as the anticipated network through- put.

**Fragmento 16 - p. 12 - score 3:**

By analyzing the various indicators, it is noted that when using the DQNReg approach, the number of rebuffering times, the rebuffering duration and the quality switching times are suppressed to the lowest, while the quality switching times and inter-starvation lengths are maintained at a level comparable to other methods. Under various mobility patterns of real-time network, the average QoE performance of DQNReg is still superior to other methods. This indicates that the trained DQNReg learning agent has strong gen- eralization ability and can ﬂexibly adapt to various network conditions, so that the video service quality can match the network communication quality as well as possible. 6 Conclusions With increased user expectations and demands for uninterrupted viewing and top video quality, stud- ies concluded that users will leave video sessions if the quality is not adequate, harming the revenues of content providers.

**Fragmento 17 - p. 14 - score 3:**

Springer LATEX template 13 [26] WLAN Throughput Project, Available: [online]: https://data.world/engrasifkhan/wlan- throughput/workspacef. [27] G-NetTrack Pro user manual. Available [online]: https://gyokovsolutions.com/manual-g-nettrack [28] J. Jiang, V. Sekar, and H. Zhang, Improving fairness, efﬁciency, and stability in HTTP-based adaptive video streaming with festive, IEEE/ACM Transactions on Networking, vol. 22, no. 01, pp. 326–340, jan. 2014. [29] N. A. Hafez, M. S. Hassan, T. Landolsi, Reformed QoE Based Approach in Bitrate- Adaptation for Dynamic Adaptive Streaming Sys- tems, To appear in the International Journal of Interdisciplinary Telecommunications and Net- working, Volume 14, Issue 1, 2022. [30] J.

**Fragmento 18 - p. 5 - score 2:**

They established chunk-wise subjective QoE model and utilize it as the reward function in reinforcement learning so that the strategy can converge toward the direction of maximizing the subjective QoE score. In our paper work, we use a reinforcement-based deep Q-learning method, called DQNReg [23], to provide a ﬁne video adaptation through the experi- ence acquired from exploring the network conditions. The objective of the proposed method is to enhance the QoE performance under dynamic network condi- tions, and achieve a fast convergence while maintain- ing higher average rewards than other learning-based methods. 3 Methodology In this section, the video streaming model is presented. The DQNReg algorithm and its reward function are introduced.

**Fragmento 19 - p. 6 - score 2:**

A reward function that represents these factors is introduced to issue policies that maximize the QoE perceived by the users. The reward function is deﬁned as follows [3, 16]: QoE = Rv i −µDB −∥Rv i+1 −Rv i ∥, (5) where Rv i is the bitrate of the i-th video segment, DB is the rebuffering duration experienced when the play- out buffer level, when a segment is downloaded, is lower than the needed segment download time. The rebuffering duration is given by: DB = Rv i Rn i Ts −T B i . (6) The parameter µ is a penalty coefﬁcient for the experi- enced rebuffering event. Finally, the term ∥Rv i+1−Rv i ∥ reﬂects the quality variation between two consecutive segments. 3.4 Rate Adaptation with DQNReg The DQNReg algorithm is implemented as follows: Once the segment is downloaded, the RL agent receives the state inputs at segment i, si = (Rv i−1, Rn i , T B i , T D i , NR), (7)

**Fragmento 20 - p. 7 - score 2:**

The DQNReg simulation results are contrasted with other benchmark approaches. 0 100 200 300 400 500 600 700 800 900 1000 Episode Number 0.7 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5 1.6 Average QoE DQNReg DQN Fig. 2 Training convergence of DQNReg vs. DQN methods. 4.1 Implementation and Training algorithm The neural network architecture, similar to [16] and [22], is composed of 1D convolution layer com- posed of 128 ﬁlters. The output of these layers is then aggregated with other inputs in a hidden layer, that uses 128 neurons, to apply the rectiﬁed linear unit (ReLU) activation function.The number of neu- rons in the output layer is equal to the adaptive bitrate set, which we have denoted as NR. The training is performed on a sequence extracted from the Big Buck Bunny video (available for download from the Blender.org site [24], for example).

**Fragmento 21 - p. 8 - score 2:**

The dataset contains client-side cellular performance indicators such as throughput information and other channel and context-related metrics. These metrics are gen- erated from a network monitoring application called G-NetTrack Pro [27]. 4.6 Comparison to Benchmarks The proposed approach is compared to three bench- marks in the literature: The heuristic rate-based (RB) approach, the model optimization hybrid-based (HB) approach, and the classical DQN learning-based approach. The RB approach selects the highest bitrate that is smaller than the predicted throughput regard- less of the previously selected bitrates. This is referred to as a stateless adaptation algorithm [28]. The adap- tation method is a quality level selector based on the predicted adaptation network throughput which is estimated through a moving average window of N steps.

**Fragmento 22 - p. 9 - score 2:**

3 Buffer occupancy for: a) RB, b) HB, c) DQN, and d) DQNReg methods in a WLAN environment. reward function is computed and normalized. High Average QoE reﬂect, high average video quality, low re-buffering duration and fewer quality switch- ing times. 2. Rebuffering times: Measures the number of instances when the buffer occupancy is zero. 3. Rebuffering duration: Measures the total rebuffering time over the entire video playback duration. 4. Inter-starvation length: Measures the time duration that separates successive rebuffering instants [31]. 5. Quality switching times: Counts the number of times the algorithm switches across different qual- ity levels. This reﬂects the number of times the user-perceived quality changes across the entire video playback.

**Fragmento 23 - p. 10 - score 2:**

5 Buffer occupancy for: a) RB, b) HB, c) DQN, and d) DQNReg methods in a 5G mobile environment. average rebuffering times. Finally, DQNReg achieved the lowest average number of rebuffering times with variance similar to that of DQN. The overall rebuffering duration experienced dur- ing the video playback for all algorithms in all sim- ulated network environments is observed in ﬁgure 9. Again, the RB method has the longest rebuffering duration with a small variance. The HB and DQN methods achieved similar average rebuffering dura- tion of about 10 seconds. Finally, DQNReg achieved the lowest average rebuffering duration of about 7 seconds. The average inter-starvation length for all algo- rithms in all simulated network environments is illus- trated in Figure 10.

**Fragmento 24 - p. 11 - score 2:**

Springer LATEX template 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level a) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level b) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level c) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level d) Fig. 6 Quality level for: a) RB, b) HB, c) DQN, and d) DQNReg methods in a 5G mobile environment. Fig. 7 Average QoE for RB, HB, DQN, and DQNReg methods. place successively with short video playback time in between. The HB and DQNReg approaches have com- parable average inter-starvation lengths while DQN has the highest median value of about 100 seconds and is negatively skewed. The overall number of quality switch times expe- rienced during the video playback for all algorithms Fig.

**Fragmento 25 - p. 12 - score 2:**

Considering the intricate web- based video delivery ecosystem and its various bot- tlenecks, adaptive bitrate algorithms become essential to content providers to optimize video quality. This thesis proposed utilizing DQNReg, a reinforcement learning based technique that enhances the classical deep Q-learning method approach for video adapta- tion. A segment-wise QoE-based reward function is established so that the learning strategy can converge towards maximizing the QoE outcome. DQNReg have been thoroughly evaluated using trace-based simula- tion for ﬁxed and mobile networks. The DQNReg- based method outperforms classical DQN algorithm and other traditional adaptation approaches. Future research can integrate the initial start-up delay and the impact of latency onto the learning-based method, so that the learned policy can be improved with respect to the QoE.

**Fragmento 26 - p. 1 - score 1:**

Reinforcement Learning-Based Rate Adaptation in Dynamic Video Streaming Nada A. Hafez American University of Sharjah Mohamed S. Hassan American University of Sharjah Taha Landolsi (  tlandolsi@aus.edu ) American University of Sharjah https://orcid.org/0000-0001-8479-9056 Research Article Keywords: Bitrate Adaptation, DASH, Deep Q-learning, Optimization, Reinforcement Learning, Video Streaming Posted Date: August 22nd, 2022 DOI: https://doi.org/10.21203/rs.3.rs-1616726/v1 License:   This work is licensed under a Creative Commons Attribution 4.0 International License. Read Full License


### 7.7. evaluacion baselines experimentos

Palabras clave usadas: `evaluation, experiment, experiments, baseline, baselines, compare, comparison, Pensieve, BBA, BOLA, MPC, RobustMPC, FastMPC, A3C, PPO, DQN, SODA, Oboe, MetaABR, results, outperform, ablation, scenario, test`

**Fragmento 1 - p. 8 - score 4:**

The buffer status is not considered during the quality selection decision. The HB approach is a hybrid adaptation algorithm that combines both the traditional RB and the QoE-based optimization adap- tation approach [29]. The HB approach maximizes the average video quality and minimizes the rebuffering duration while maintaining the quality variation to a certain threshold. Finally, the proposed DQNReg is compared to the classical DQN algorithm. 4.7 Simulation Results The DQNReg model is evaluated on the testing datasets, both ﬁxed and mobile. The trained DQNReg

**Fragmento 2 - p. 9 - score 4:**

5 Performance Evaluation and Discussion After performing extensive simulations in different network environments, the performance of the sim- ulated approaches is analyzed and evaluated. The evaluation metrics used are explained then the DQN- Reg adaptation approach is evaluated and compared to the aforementioned benchmark approaches. 5.1 Evaluation Metrics The proposed method’s performance is evaluated using the following metrics: 1. Average QoE: The QoE objective is a sum of weighted objectives that have varying orders of magnitudes. To make fair comparisons it is impor- tant to transform the objective functions in a way that they all have comparable orders of magni- tude [30]. The average QoE, calculated through the 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) a) 260 280 300 320 340 360 380 400 420 440 460 Time (s) 0 20 40 60 Buffer Length (s) b) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) c) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) d) Fig.

**Fragmento 3 - p. 8 - score 3:**

The dataset contains client-side cellular performance indicators such as throughput information and other channel and context-related metrics. These metrics are gen- erated from a network monitoring application called G-NetTrack Pro [27]. 4.6 Comparison to Benchmarks The proposed approach is compared to three bench- marks in the literature: The heuristic rate-based (RB) approach, the model optimization hybrid-based (HB) approach, and the classical DQN learning-based approach. The RB approach selects the highest bitrate that is smaller than the predicted throughput regard- less of the previously selected bitrates. This is referred to as a stateless adaptation algorithm [28]. The adap- tation method is a quality level selector based on the predicted adaptation network throughput which is estimated through a moving average window of N steps.

**Fragmento 4 - p. 9 - score 3:**

It is evident that RB does not manage the buffer occupancy well which would greatly impact its performance. It is noted that, with DQNReg both the buffer starvation instances (which cause rebuffer- ing events) and the frequency of quality switching are signiﬁcantly reduced compared to all other meth- ods. DQNReg outperforms other approaches in the two simulated environments as it does not suffer from rebuffering events in the ﬁxed environment, while maintains relatively frequency of quality vari- ations. Furthermore, DQNReg reduces the starvation instances in the mobile environment. Although DQN shows a relatively low number of rebuffering events, it struggles with quality variations, which is noticeably reduced in DQNReg.

**Fragmento 5 - p. 3 - score 2:**

Section III describes the methodology. Section IV details the implementation and the simulation setup. Section V is dedicated to the performance evaluation of the proposed approach and section VI gives the conclusions of this study. 2 Literature review of existing solutions Adaptation methods and algorithms are still under- going extensive research work regardless of the pub- lic adoption [4–6]. This is owed to the contin- uously updated internet video delivery ecosystem. This section illustrates the various classic adaptation approaches. The existing approaches are classiﬁed into two main categories; Traditional adaptation tech- niques and ML-based adaptation methods. In the tra- ditional adaptation case, the solutions are customized for predetermined scenarios.

**Fragmento 6 - p. 5 - score 2:**

Finally, the DQNReg-based rate adapta- tion technique is detailed. 3.1 Video Streaming Model In this paper, a video sequence is modeled as a set of Ns consecutive segments. Each segment lasts for Ts seconds, and is encoded at the bitrate Rv. The client video player requests a segment at bitrate Rv i for the i-th segment. The selected bitrate Rv i is mapped to different quality levels {Q1, Q2, . . . , QN} based on the client device speciﬁcations and the available video content. In general, The higher the bitrate used in encoding, the higher the video quality delivered to the viewer. Suppose that Qj is the quality level requested for the i-th segment, and let its corresponding bitrate be Rv i . If Li be the size of the i-th segment in bits then, for a constant bitrate (CBR) case, Li = TsRv i .

**Fragmento 7 - p. 5 - score 2:**

It builds on the classical DQN algorithm by adding a weighted penalty to the normal squared Bellman error. The authors in [23] proposed evolution strategies by exploring the space of compu- tational graphs which calculates the loss function for an RL agent. They highlighted that DQNReg shows an improved performance over DQN in environments that have not been experienced during training. Their analysis showed that DQNReg outperforms DQN as well other well-known variants such as the double DQN (DDQN). DQNReg is typically characterized with the following set of equations [23]: Yt = rt + γ max a Qtarg(st+1, a), (2) δ = Q(st, at) −Yt, (3)

**Fragmento 8 - p. 7 - score 2:**

The DQNReg simulation results are contrasted with other benchmark approaches. 0 100 200 300 400 500 600 700 800 900 1000 Episode Number 0.7 0.8 0.9 1 1.1 1.2 1.3 1.4 1.5 1.6 Average QoE DQNReg DQN Fig. 2 Training convergence of DQNReg vs. DQN methods. 4.1 Implementation and Training algorithm The neural network architecture, similar to [16] and [22], is composed of 1D convolution layer com- posed of 128 ﬁlters. The output of these layers is then aggregated with other inputs in a hidden layer, that uses 128 neurons, to apply the rectiﬁed linear unit (ReLU) activation function.The number of neu- rons in the output layer is equal to the adaptive bitrate set, which we have denoted as NR. The training is performed on a sequence extracted from the Big Buck Bunny video (available for download from the Blender.org site [24], for example).

**Fragmento 9 - p. 9 - score 2:**

Springer LATEX template agent is employed to pick the rate of the video segment to be downloaded. Once the bitrate is selected, the bitrate is mapped to one of four quality levels to better illustrate the quality changes. The performance of the DQNReg agent for each channel environment type is illustrated. The DQNReg performance is compared to the benchmark approaches. Figures 3–6 illustrate the buffer occupancy and quality levels in both ﬁxed and mobile environments for DQNReg compared to the RB, HB, and DQN benchmark approaches. It is clear that both HB and DQN perform better than RB. Although RB maintains a relatively low number of quality jumps in differ- ent environments, it greatly suffers from rebuffering events.

**Fragmento 10 - p. 10 - score 2:**

The RB method, however, showed the lowest average score but with a larger variance compared to the other methods. The number of rebuffering instances for all algo- rithms in all simulated network environments is shown in Figure 8. The RB method has the highest number of starvation instances with smallest variance, this means that rebuffering instances will occur with rate-based regardless of the network condition. This is owed to the fact that the RB method ignores the playback buffer occupancy and considers the network through- put only. The HB and DQN methods achieved similar 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) a) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) b) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) c) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) d) Fig.

**Fragmento 11 - p. 10 - score 2:**

Springer LATEX template 9 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level a) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level b) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level c) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level d) Fig. 4 Quality level for: a) RB, b) HB, c) DQN, and d) DQNReg methods in a WLAN environment. 5.2 Performance Comparison Figure 7 illustrates the average QoE for all four sim- ulated approaches across all simulated network envi- ronments. The DQNReg method achieved the highest score in comparison to the other methods. The HB method average score is comparable to that of the DQN one, but has a relatively larger variance.

**Fragmento 12 - p. 12 - score 2:**

Considering the intricate web- based video delivery ecosystem and its various bot- tlenecks, adaptive bitrate algorithms become essential to content providers to optimize video quality. This thesis proposed utilizing DQNReg, a reinforcement learning based technique that enhances the classical deep Q-learning method approach for video adapta- tion. A segment-wise QoE-based reward function is established so that the learning strategy can converge towards maximizing the QoE outcome. DQNReg have been thoroughly evaluated using trace-based simula- tion for ﬁxed and mobile networks. The DQNReg- based method outperforms classical DQN algorithm and other traditional adaptation approaches. Future research can integrate the initial start-up delay and the impact of latency onto the learning-based method, so that the learned policy can be improved with respect to the QoE.

**Fragmento 13 - p. 2 - score 1:**

The performance of this RL-based method is compared to three methods: A heuristic method, a model-based method, and a classical learning-based method. The com- parison shows that the RL-based method converges faster while achieving a high QoE score. In addition, it reduces the re-buffering duration while maintaining higher video quality and relatively lower quality variations. Keywords: Bitrate Adaptation, DASH, Deep Q-learning, Optimization, Reinforcement Learning, Video Streaming 1 Introduction With the constant updates to the wireless LAN (WLAN) standards and the gradual roll out of 5G mobile networks, wireless technology is expected to deliver high multi-Gbps peak data rates, ultra-low latency, increased reliability and decreased network management complexity [1].

**Fragmento 14 - p. 2 - score 1:**

It is capable of providing seamless streaming via uncertain network conditions by switching across different video qualities and their correspond- ing video segment bitrates. The complexity of the video streaming environment makes it a good candidate for different learning-based approaches. Accordingly, this paper proposes a reinforcement-learning (RL) deep Q-network called DQNReg, that enhances the classical deep Q-learning method. A segment-wise QoE-based reward function is formulated so that the learning strategy can converge towards maximizing the QoE out- come. The proposed RL-based adaptation approach is evaluated using trace-based simulation for both wireless local area network channels and 5G mobile channels.

**Fragmento 15 - p. 3 - score 1:**

Authors in [9] presented a pre- diction model to accurately approximate the trend of buffer level variation in the client side. The quality switching in the adaptation is reduced based on the approximation. It can be concluded from the results that a steady video quality is achieved when buffer

**Fragmento 16 - p. 4 - score 1:**

Instead, it learns to make ABR decisions solely through observations of the resulting perfor- mance of past decisions. In [17], the authors incorporated an RL method with the addition of Q-Learning. The action is set as the segment request with a particular bitrate and the reward is deﬁned as the QoE approximation. The study maximizes the QoE through adjusting the adap- tation behavior as per the existing network conditions. Another learning based approach propose to combine the nearest neighbor (KNN) with Q-learning algo- rithm [18]. In this bitrate adaptive scenario, the KNN- Q learning can achieve higher QoE and faster conver- gence speed than the Q-learning algorithm alone. Authors in [19] introduce a system that trains the policy via imitating expert trajectories given by the instant solver.

**Fragmento 17 - p. 5 - score 1:**

Springer LATEX template strategy for DASH clients based on an MDP optimiza- tion was proposed in [20]. The authors introduced a penalty function into the reward function to penalize the system for re-buffering events as well as moving away from a safe buffer level. Authors in [21] presented a framework, called D-DASH, that combines deep learning and reinforce- ment learning techniques to optimize the QoE of DASH. They combined feed-forward and recurrent deep neural networks with advanced strategies. The numerical results are obtained on real and simulated channels. Besides yielding a considerably higher QoE, the D-DASH framework exhibits fast convergence rate. Recently, the authors in [22] used enhanced deep Q-learning for DASH video applications, and proposed a QoE-oriented rate adaptation framework based on enhanced deep Q-learning.

**Fragmento 18 - p. 5 - score 1:**

They established chunk-wise subjective QoE model and utilize it as the reward function in reinforcement learning so that the strategy can converge toward the direction of maximizing the subjective QoE score. In our paper work, we use a reinforcement-based deep Q-learning method, called DQNReg [23], to provide a ﬁne video adaptation through the experi- ence acquired from exploring the network conditions. The objective of the proposed method is to enhance the QoE performance under dynamic network condi- tions, and achieve a fast convergence while maintain- ing higher average rewards than other learning-based methods. 3 Methodology In this section, the video streaming model is presented. The DQNReg algorithm and its reward function are introduced.

**Fragmento 19 - p. 5 - score 1:**

The buffer size is depleted as the video is played and is replenished as segments are downloaded. Rebuffer- ing or starvation events happen when the playback buffer of the client has been depleted and the consecu- tive video segment does not arrive before its scheduled playback time. If the buffer occupancy is T B i before the i-th segment is downloaded, then it will become just after it is downloaded: T B i+1 = T B i −Li Rn i + Ts. (1) Therefore, if sufﬁcient buffer content is maintained before loading, i.e. if T B i > Li/Rn i , then rebuffering or starvation events will not take place. 3.2 DQNReg algorithm Many enhancements for the classic deep Q-learning techniques have been proposed. One such a technique is the DQNReg [23].

**Fragmento 20 - p. 6 - score 1:**

Springer LATEX template 5 Adaptation Algorithm Video Player 1 7 6 5 4 3 2 8 9 Server 1 7 6 5 4 3 2 8 9 QL1 1 7 6 5 4 3 2 8 9 QL2 1 7 6 5 4 3 2 8 9 QL3 Segment S7-QL3 Video sequence with 3 quality levels Received Video Segments New HTTP Requests Past segment params.: 1. Network throughput,   2. Segment bit rate,   3. Buffer occupancy,   QL1 QL2 QL3 HTTP GET S1-QL1, … , S3-QL1 1 2 3 HTTP GET S4-QL2, … , S6-QL2 4 5 6 HTTP GET S7-QL3, … , S9-QL3 7 8 9 Quality Selection HTTP Responses 1 4 7         DQNReg network with reward function: action RL agent Wireless Network (WLAN or 5G) Fig. 1 Proposed RL-based rate adaptation scheme using a DQNReg network. LReg = αQ(st, at) + δ2, (4) where Yt is the target Q-value at the time step t, rt is the instantaneous reward, at is the instantaneous action output by the agent to the environment, γ is a discount factor, δ is the DQN loss function, and st and st+1 are the states at t and t + 1, respectively.

**Fragmento 21 - p. 6 - score 1:**

A reward function that represents these factors is introduced to issue policies that maximize the QoE perceived by the users. The reward function is deﬁned as follows [3, 16]: QoE = Rv i −µDB −∥Rv i+1 −Rv i ∥, (5) where Rv i is the bitrate of the i-th video segment, DB is the rebuffering duration experienced when the play- out buffer level, when a segment is downloaded, is lower than the needed segment download time. The rebuffering duration is given by: DB = Rv i Rn i Ts −T B i . (6) The parameter µ is a penalty coefﬁcient for the experi- enced rebuffering event. Finally, the term ∥Rv i+1−Rv i ∥ reﬂects the quality variation between two consecutive segments. 3.4 Rate Adaptation with DQNReg The DQNReg algorithm is implemented as follows: Once the segment is downloaded, the RL agent receives the state inputs at segment i, si = (Rv i−1, Rn i , T B i , T D i , NR), (7)

**Fragmento 22 - p. 6 - score 1:**

Here, LReg is the DQNReg loss function, Q(st, at) is the Q-value penalty, α is a weight factor, and δ2 is the squared error. Classical DQN algorithms tend to overestimate the Q-value, which might be a potential problem [23]. It shows that the learned constraints starts early in the training. To address this issue and avoid overes- timation, the weighted penalty is added to DQNReg loss function as shown in equation (4). Consider- ing the characteristics of the DASH rate adaptation, DQNReg is expected to enable the trained agent to obtain improved QoE performance gain. The QoE- based reward function is explained in the following section. 3.3 Reward Function The QoE is impacted by the video quality of the viewed segment, the frequency of quality switching and the experienced re-buffering events.

**Fragmento 23 - p. 7 - score 1:**

By regularly observing the environment, the agent gathers tuples containing the previous state, the new state, the action to be undertaken, and the reward to be given to the learner. The temporal-difference technique is then applied to perform gradient descent [22]. This allows the value network to estimate the real state-action value function with adequate accuracy. 4 Implementation and Simulation This section showcases the implementation of the pro- posed DQNReg-based adaptation approach with the simulation setup, the video parameters, and network traces. It is noteworthy to indicate that the neural net- work architecture is not a priority of this paper, hence a default network architecture was adopted for the simu- lation.

**Fragmento 24 - p. 7 - score 1:**

Once the obser- vation states are collected by the agent, the Q-value table or the weights in the network are updated until the policy converges. Certain hyper-parameters were set similar to [16, 21, 22]. The weight factor used here is α = 0.1, the discount factor is γ = 0.99, the learning rate is 10−5 and the exploration adopted was the ǫ-greedy to explore many states and have a maintain a trade-off between exploration and exploita- tion. The training algorithm takes the bitrate selection for a video segment as a step, it then takes the step experience and stores it into the experience buffer. In Figure 2, the average QoE reward on the training set is plotted against the number of training episodes for both DQNReg and DQN.

**Fragmento 25 - p. 7 - score 1:**

It is clear that DQNReg con- verges faster and achieves higher average QoE value. 4.2 Video Streaming Environment The video streaming environment consists of a set of videos encoded at different rates. An internal repre- sentation of the client’s playback buffer is maintained. A download time is assigned based on the segment’s bitrate and available network throughput. To represent

**Fragmento 26 - p. 8 - score 1:**

It is necessary to note that the quality of the dataset impacts the performance of the learning agent. These traces allow the agent to experience throughput variations in real networks. 4.3 Simulation Setup A simulation testbed based on the video streaming environment is implemented in SimEvent discrete- event simulator in MATLAB. The testbed simulates the video player buffer dynamics during the process of receiving and playing back video segments based on a bitrate range and network proﬁles. To train the agent a corpus of network traces is created through con- catenating different excerpts of the network datasets, which will be detailed in the section below. The size of the buffer is set T B max = 60s which is common in a DASH video player.


### 7.8. resultados numericos metricas

Palabras clave usadas: `improvement, improve, gain, reduce, reduction, %, QoE gain, higher, lower, average, median, percentile, stall time, latency, overhead, accuracy, significant, p95, p99, score, ratio, duration`

**Fragmento 1 - p. 2 - score 7:**

The performance of this RL-based method is compared to three methods: A heuristic method, a model-based method, and a classical learning-based method. The com- parison shows that the RL-based method converges faster while achieving a high QoE score. In addition, it reduces the re-buffering duration while maintaining higher video quality and relatively lower quality variations. Keywords: Bitrate Adaptation, DASH, Deep Q-learning, Optimization, Reinforcement Learning, Video Streaming 1 Introduction With the constant updates to the wireless LAN (WLAN) standards and the gradual roll out of 5G mobile networks, wireless technology is expected to deliver high multi-Gbps peak data rates, ultra-low latency, increased reliability and decreased network management complexity [1].

**Fragmento 2 - p. 2 - score 5:**

Enhanced mobile broad- band with more uniform data rates and increased efﬁ- ciency empower new and improved user experiences. At the moment, video streaming stands out as the most signiﬁcant trafﬁc type consumed by mobile devices accounting for an average of 60% of total trafﬁc. This percentage is anticipated to increase to 74% by the end of 2024. Consumer behavior is shifting from low-deﬁnition (360p) and standard-deﬁnition formats (480p) to high-deﬁnition video (720p and 1080p) as network capabilities improve. In addition, viewer behavior is expected to change more dramatically as 5G services are made available [2]. The quality of experience (QoE) perceived by the users is affected by several factors like video quality, quality switch- ing and re-buffering duration [3] which are inﬂuenced by video streaming strategies which typically rely on adaptive bitrate (ABR) techniques for video streaming to enhance video delivery and customer satisfaction.

**Fragmento 3 - p. 10 - score 4:**

5 Buffer occupancy for: a) RB, b) HB, c) DQN, and d) DQNReg methods in a 5G mobile environment. average rebuffering times. Finally, DQNReg achieved the lowest average number of rebuffering times with variance similar to that of DQN. The overall rebuffering duration experienced dur- ing the video playback for all algorithms in all sim- ulated network environments is observed in ﬁgure 9. Again, the RB method has the longest rebuffering duration with a small variance. The HB and DQN methods achieved similar average rebuffering dura- tion of about 10 seconds. Finally, DQNReg achieved the lowest average rebuffering duration of about 7 seconds. The average inter-starvation length for all algo- rithms in all simulated network environments is illus- trated in Figure 10.

**Fragmento 4 - p. 12 - score 4:**

Springer LATEX template 11 Fig. 11 QL switching instances for RB, HB, DQN, and DQNReg methods. a low complexity algorithm and yields fewer qual- ity switching instances. However, it suffers more frequent rebuffering instances, longer rebuffering durations, and shorter inter-starvation lengths. As for the HB approach, it has lower quality switching times but some how experiences a higher number of rebuffering instances. Its performance is comparable to other methods with respect to rebuffering durations and inter-starvation lengths. On the other hand, DQN performs well with respect to number of rebuffering times and has a quite large inter-starvation length. It how ever has a high variance in the quality switching times, which may indicate its inability to generalize well under different environments.

**Fragmento 5 - p. 5 - score 3:**

They established chunk-wise subjective QoE model and utilize it as the reward function in reinforcement learning so that the strategy can converge toward the direction of maximizing the subjective QoE score. In our paper work, we use a reinforcement-based deep Q-learning method, called DQNReg [23], to provide a ﬁne video adaptation through the experi- ence acquired from exploring the network conditions. The objective of the proposed method is to enhance the QoE performance under dynamic network condi- tions, and achieve a fast convergence while maintain- ing higher average rewards than other learning-based methods. 3 Methodology In this section, the video streaming model is presented. The DQNReg algorithm and its reward function are introduced.

**Fragmento 6 - p. 6 - score 3:**

A reward function that represents these factors is introduced to issue policies that maximize the QoE perceived by the users. The reward function is deﬁned as follows [3, 16]: QoE = Rv i −µDB −∥Rv i+1 −Rv i ∥, (5) where Rv i is the bitrate of the i-th video segment, DB is the rebuffering duration experienced when the play- out buffer level, when a segment is downloaded, is lower than the needed segment download time. The rebuffering duration is given by: DB = Rv i Rn i Ts −T B i . (6) The parameter µ is a penalty coefﬁcient for the experi- enced rebuffering event. Finally, the term ∥Rv i+1−Rv i ∥ reﬂects the quality variation between two consecutive segments. 3.4 Rate Adaptation with DQNReg The DQNReg algorithm is implemented as follows: Once the segment is downloaded, the RL agent receives the state inputs at segment i, si = (Rv i−1, Rn i , T B i , T D i , NR), (7)

**Fragmento 7 - p. 7 - score 3:**

Once the obser- vation states are collected by the agent, the Q-value table or the weights in the network are updated until the policy converges. Certain hyper-parameters were set similar to [16, 21, 22]. The weight factor used here is α = 0.1, the discount factor is γ = 0.99, the learning rate is 10−5 and the exploration adopted was the ǫ-greedy to explore many states and have a maintain a trade-off between exploration and exploita- tion. The training algorithm takes the bitrate selection for a video segment as a step, it then takes the step experience and stores it into the experience buffer. In Figure 2, the average QoE reward on the training set is plotted against the number of training episodes for both DQNReg and DQN.

**Fragmento 8 - p. 8 - score 3:**

The buffer status is not considered during the quality selection decision. The HB approach is a hybrid adaptation algorithm that combines both the traditional RB and the QoE-based optimization adap- tation approach [29]. The HB approach maximizes the average video quality and minimizes the rebuffering duration while maintaining the quality variation to a certain threshold. Finally, the proposed DQNReg is compared to the classical DQN algorithm. 4.7 Simulation Results The DQNReg model is evaluated on the testing datasets, both ﬁxed and mobile. The trained DQNReg

**Fragmento 9 - p. 9 - score 3:**

3 Buffer occupancy for: a) RB, b) HB, c) DQN, and d) DQNReg methods in a WLAN environment. reward function is computed and normalized. High Average QoE reﬂect, high average video quality, low re-buffering duration and fewer quality switch- ing times. 2. Rebuffering times: Measures the number of instances when the buffer occupancy is zero. 3. Rebuffering duration: Measures the total rebuffering time over the entire video playback duration. 4. Inter-starvation length: Measures the time duration that separates successive rebuffering instants [31]. 5. Quality switching times: Counts the number of times the algorithm switches across different qual- ity levels. This reﬂects the number of times the user-perceived quality changes across the entire video playback.

**Fragmento 10 - p. 10 - score 3:**

Again, the RB method has the lowest performing method with respect to rebuffer- ing. The RB method has the lowest inter-starvation duration, meaning that rebuffering events will take

**Fragmento 11 - p. 12 - score 3:**

By analyzing the various indicators, it is noted that when using the DQNReg approach, the number of rebuffering times, the rebuffering duration and the quality switching times are suppressed to the lowest, while the quality switching times and inter-starvation lengths are maintained at a level comparable to other methods. Under various mobility patterns of real-time network, the average QoE performance of DQNReg is still superior to other methods. This indicates that the trained DQNReg learning agent has strong gen- eralization ability and can ﬂexibly adapt to various network conditions, so that the video service quality can match the network communication quality as well as possible. 6 Conclusions With increased user expectations and demands for uninterrupted viewing and top video quality, stud- ies concluded that users will leave video sessions if the quality is not adequate, harming the revenues of content providers.

**Fragmento 12 - p. 4 - score 2:**

A proportional-integral controller outputs a video rate that matches the esti- mated available and ensures the buffer is maintained at the target level. Optimization-based approaches are widely used for bitrate adaptation in DASH. Essentially, the opti- mization problem is solved based on the prediction of buffer dynamics and network throughput. How- ever, stochastic segment size shifts the buffer occu- pancy from the estimated value. In order to get rid of this effect and improve the prediction accuracy for buffer occupancy [11] propose an algorithm based on Markov decision process (MDP) with segment size information so that only the network capacity vari- ation need to be considered in the decision-making process.

**Fragmento 13 - p. 6 - score 2:**

Here, LReg is the DQNReg loss function, Q(st, at) is the Q-value penalty, α is a weight factor, and δ2 is the squared error. Classical DQN algorithms tend to overestimate the Q-value, which might be a potential problem [23]. It shows that the learned constraints starts early in the training. To address this issue and avoid overes- timation, the weighted penalty is added to DQNReg loss function as shown in equation (4). Consider- ing the characteristics of the DASH rate adaptation, DQNReg is expected to enable the trained agent to obtain improved QoE performance gain. The QoE- based reward function is explained in the following section. 3.3 Reward Function The QoE is impacted by the video quality of the viewed segment, the frequency of quality switching and the experienced re-buffering events.

**Fragmento 14 - p. 7 - score 2:**

It is clear that DQNReg con- verges faster and achieves higher average QoE value. 4.2 Video Streaming Environment The video streaming environment consists of a set of videos encoded at different rates. An internal repre- sentation of the client’s playback buffer is maintained. A download time is assigned based on the segment’s bitrate and available network throughput. To represent

**Fragmento 15 - p. 8 - score 2:**

The segment-wise QoE reward is estimated after each bitrate selection. 4.4 Video Parameters In the simulation, the video used is Big Buck Bunny, which is a simple animation short clip of 10 minutes and 34 seconds duration under the Peach open movie project. The video content consists of animated char- acters with a non intricate background [25]. The video in the dataset is encoded by the H.264/MPEG-4 codec to thirteen different representation rates, ranging from 235 kbps to 40 Mbps. The 4-second segment group is selected from the full DASH proﬁle. 4.5 Network Traces The proposed approach is examined using realistic network environment conditions. Real network traces are used from a ﬁxed WLAN [26] network and a mobile 5G network [1].

**Fragmento 16 - p. 10 - score 2:**

The RB method, however, showed the lowest average score but with a larger variance compared to the other methods. The number of rebuffering instances for all algo- rithms in all simulated network environments is shown in Figure 8. The RB method has the highest number of starvation instances with smallest variance, this means that rebuffering instances will occur with rate-based regardless of the network condition. This is owed to the fact that the RB method ignores the playback buffer occupancy and considers the network through- put only. The HB and DQN methods achieved similar 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) a) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) b) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) c) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 0 20 40 60 Buffer Length (s) d) Fig.

**Fragmento 17 - p. 10 - score 2:**

Springer LATEX template 9 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level a) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level b) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level c) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level d) Fig. 4 Quality level for: a) RB, b) HB, c) DQN, and d) DQNReg methods in a WLAN environment. 5.2 Performance Comparison Figure 7 illustrates the average QoE for all four sim- ulated approaches across all simulated network envi- ronments. The DQNReg method achieved the highest score in comparison to the other methods. The HB method average score is comparable to that of the DQN one, but has a relatively larger variance.

**Fragmento 18 - p. 11 - score 2:**

Springer LATEX template 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level a) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level b) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level c) 0 50 100 150 200 250 300 350 400 450 500 Time (s) 1 2 3 4 Quality Level d) Fig. 6 Quality level for: a) RB, b) HB, c) DQN, and d) DQNReg methods in a 5G mobile environment. Fig. 7 Average QoE for RB, HB, DQN, and DQNReg methods. place successively with short video playback time in between. The HB and DQNReg approaches have com- parable average inter-starvation lengths while DQN has the highest median value of about 100 seconds and is negatively skewed. The overall number of quality switch times expe- rienced during the video playback for all algorithms Fig.

**Fragmento 19 - p. 12 - score 2:**

Considering the intricate web- based video delivery ecosystem and its various bot- tlenecks, adaptive bitrate algorithms become essential to content providers to optimize video quality. This thesis proposed utilizing DQNReg, a reinforcement learning based technique that enhances the classical deep Q-learning method approach for video adapta- tion. A segment-wise QoE-based reward function is established so that the learning strategy can converge towards maximizing the QoE outcome. DQNReg have been thoroughly evaluated using trace-based simula- tion for ﬁxed and mobile networks. The DQNReg- based method outperforms classical DQN algorithm and other traditional adaptation approaches. Future research can integrate the initial start-up delay and the impact of latency onto the learning-based method, so that the learned policy can be improved with respect to the QoE.

**Fragmento 20 - p. 2 - score 1:**

Springer LATEX template Reinforcement Learning-Based Rate Adaptation in Dynamic Video Streaming N. A. Hafez, M. S. Hassan and T. Landolsi American University of Sharjah, Sharjah, UAE. *Corresponding author(s). E-mail(s): tlandolsi@aus.edu; Contributing authors: g00039071@aus.edu; mshassan@aus.edu; Abstract Video streaming stands out as the most signiﬁcant trafﬁc type consumed by mobile devices. This increased demand has been a major driver for research on bitrate adaptation algorithms. Bitrate adaptation ensures high user-perceived quality, which, in turn, correlates with higher proﬁts for content providers and delivery sys- tems. Dynamic adaptive streaming over HTTP (DASH) is a widely adopted video streaming standard utilized by service providers to provide competitive quality of experience (QoE).

**Fragmento 21 - p. 3 - score 1:**

Authors in [9] presented a pre- diction model to accurately approximate the trend of buffer level variation in the client side. The quality switching in the adaptation is reduced based on the approximation. It can be concluded from the results that a steady video quality is achieved when buffer

**Fragmento 22 - p. 4 - score 1:**

A buffer-based adaptation approach that does not rely on throughput prediction methods is presented in [12]. The algorithm solves optimization problem based on the buffer length reservation. It downloads the lowest bitrate and tries to maintain the buffer occu- pancy within a certain threshold. Another adaptation logic based on optimization techniques is presented in [13] which introduces a novel probing based net- work measurement technique to advance the video quality selection. It also presents a QoE-aware DASH system, called QDASH, with mixed-integer linear pro- gramming. The authors in [14] used an optimization mechanism with two objective functions: The ﬁrst function maximizes the overall average QoE among DASH clients, while the second function minimizes the negative impact of temporal video quality changes; that is the up and down switching between different representation during playback.

**Fragmento 23 - p. 4 - score 1:**

Instead, it learns to make ABR decisions solely through observations of the resulting perfor- mance of past decisions. In [17], the authors incorporated an RL method with the addition of Q-Learning. The action is set as the segment request with a particular bitrate and the reward is deﬁned as the QoE approximation. The study maximizes the QoE through adjusting the adap- tation behavior as per the existing network conditions. Another learning based approach propose to combine the nearest neighbor (KNN) with Q-learning algo- rithm [18]. In this bitrate adaptive scenario, the KNN- Q learning can achieve higher QoE and faster conver- gence speed than the Q-learning algorithm alone. Authors in [19] introduce a system that trains the policy via imitating expert trajectories given by the instant solver.

**Fragmento 24 - p. 4 - score 1:**

Springer LATEX template 3 underﬂows are reduced. Nonetheless, the main draw- back of the heuristic based techniques is that they cannot be generalized since they are deterministically customized to particular network conditions. Control theory is used to model dynamical sys- tems that are stable and accurate. The work in [3] introduces a model predictive control approach which optimizes the QoE function by selecting bitrates based on throughput approximation. It predicts throughput of upcoming segments downloads based on existing samples of recently downloaded segments. The work in [10] proposes an adaptation logic based on feed- back control. The quality adaptation controller takes a buffer as an input and returns the video rate of the segment to be downloaded.

**Fragmento 25 - p. 4 - score 1:**

The system attempts to pick the seg- ment with higher perceptual video qualities rather than video bitrates by constructing a neural network archi- tecture, video datasets and QoE metrics with video quality features. Another online learning adaptation

**Fragmento 26 - p. 5 - score 1:**

Springer LATEX template strategy for DASH clients based on an MDP optimiza- tion was proposed in [20]. The authors introduced a penalty function into the reward function to penalize the system for re-buffering events as well as moving away from a safe buffer level. Authors in [21] presented a framework, called D-DASH, that combines deep learning and reinforce- ment learning techniques to optimize the QoE of DASH. They combined feed-forward and recurrent deep neural networks with advanced strategies. The numerical results are obtained on real and simulated channels. Besides yielding a considerably higher QoE, the D-DASH framework exhibits fast convergence rate. Recently, the authors in [22] used enhanced deep Q-learning for DASH video applications, and proposed a QoE-oriented rate adaptation framework based on enhanced deep Q-learning.


### 7.9. limitaciones riesgos coste

Palabras clave usadas: `limitation, limitations, future work, challenge, challenges, overhead, complexity, compute, GPU, CPU, deployment, real-world, generalization, out-of-distribution, OOD, unstable, fail, bias, sensitive, prediction error, horizon, scalability`

**Fragmento 1 - p. 2 - score 2:**

It is capable of providing seamless streaming via uncertain network conditions by switching across different video qualities and their correspond- ing video segment bitrates. The complexity of the video streaming environment makes it a good candidate for different learning-based approaches. Accordingly, this paper proposes a reinforcement-learning (RL) deep Q-network called DQNReg, that enhances the classical deep Q-learning method. A segment-wise QoE-based reward function is formulated so that the learning strategy can converge towards maximizing the QoE out- come. The proposed RL-based adaptation approach is evaluated using trace-based simulation for both wireless local area network channels and 5G mobile channels.

**Fragmento 2 - p. 3 - score 2:**

For instance, the persistent bandwidth ﬂuctuations in the mobile network impose a challenge on ABR meth- ods [1]. In such a dynamic environment a ﬂexible ABR strategy is needed so as to intelligently adjust and maintain a good performance. In this paper, we demonstrate that an ABR strategy based on a machine learning (ML) technique, called reinforcement learning (RL), provides an intelligent and effective solution to the dynamic rate adaptation problem. In RL, an agent learns about the dynamic environment through trial-and-error interactions. The agent takes an action and receives a reward from the environment. The objective of an agent is to maxi- mize the discounted cumulative rewards by learning the optimal actions and then gradually converging to the optimal policy.

**Fragmento 3 - p. 4 - score 2:**

2.2 RL-Based Adaptation Existing classic ABR algorithms mostly rely on ﬁxed heuristics that have been ﬁne tuned according to ﬁxed assumptions about deployment environments. Not only that, but each of these approaches have been designed to optimize for a speciﬁc QoE metric. Consequently, if the assumptions are breached, these ABR algorithms fail to generalize and perform poorly. To overcome these issues, learning-based adaptation approaches are explored. With machine learning tech- niques a client can learn to adapt its video quality to the changing context without the need for any human intervention. Authors in [15] use a decision-tree based random forest classiﬁcation to map network related features onto the video rate.

**Fragmento 4 - p. 2 - score 1:**

The performance of this RL-based method is compared to three methods: A heuristic method, a model-based method, and a classical learning-based method. The com- parison shows that the RL-based method converges faster while achieving a high QoE score. In addition, it reduces the re-buffering duration while maintaining higher video quality and relatively lower quality variations. Keywords: Bitrate Adaptation, DASH, Deep Q-learning, Optimization, Reinforcement Learning, Video Streaming 1 Introduction With the constant updates to the wireless LAN (WLAN) standards and the gradual roll out of 5G mobile networks, wireless technology is expected to deliver high multi-Gbps peak data rates, ultra-low latency, increased reliability and decreased network management complexity [1].

**Fragmento 5 - p. 9 - score 1:**

3 Buffer occupancy for: a) RB, b) HB, c) DQN, and d) DQNReg methods in a WLAN environment. reward function is computed and normalized. High Average QoE reﬂect, high average video quality, low re-buffering duration and fewer quality switch- ing times. 2. Rebuffering times: Measures the number of instances when the buffer occupancy is zero. 3. Rebuffering duration: Measures the total rebuffering time over the entire video playback duration. 4. Inter-starvation length: Measures the time duration that separates successive rebuffering instants [31]. 5. Quality switching times: Counts the number of times the algorithm switches across different qual- ity levels. This reﬂects the number of times the user-perceived quality changes across the entire video playback.

**Fragmento 6 - p. 12 - score 1:**

Springer LATEX template 11 Fig. 11 QL switching instances for RB, HB, DQN, and DQNReg methods. a low complexity algorithm and yields fewer qual- ity switching instances. However, it suffers more frequent rebuffering instances, longer rebuffering durations, and shorter inter-starvation lengths. As for the HB approach, it has lower quality switching times but some how experiences a higher number of rebuffering instances. Its performance is comparable to other methods with respect to rebuffering durations and inter-starvation lengths. On the other hand, DQN performs well with respect to number of rebuffering times and has a quite large inter-starvation length. It how ever has a high variance in the quality switching times, which may indicate its inability to generalize well under different environments.

**Fragmento 7 - p. 13 - score 1:**

3, pp. 523–534, Sept 2017. [15] Y.-L. Chien, K. C.-J. Lin, and M.-S. Chen, Machine learning based rate adaptation with elas- tic feature selection for HTTP-based streaming, ICME, IEEE Computer Society, 2015, pp. 1–6. [16] H. Mao, R. Netravali, and M. Alizadeh, Neu- ral adaptive video streaming with Pensieve, ACM Conference on SIGCOMM, 2017. [17] M. Claeys, S. Latr´e, J. Famaey, T. Wu, W. Van Leekwijck, and F. De Turck, Design of a Q-learning-based client quality selection algo- rithm for HTTP adaptive video streaming, Pro- ceedings of Adaptive and Learning Agents Work- shop, 2013, pp. 30–37. [18] H. Lin, Z. Shen, H. Zhou, X. Liu, L. Zhang, G. Xiao, and Z. Cheng, KNN-Q learning algo- rithm of bitrate adaptation for video streaming over HTTP, 2020 Information Communication Technologies Conference (ICTC), 2020, pp.


### 7.10. ideas fase45 v1 controller defendible

Palabras clave usadas: `risk, safe, safety, robust, conservative, fallback, uncertainty, capacity, lower bound, tail, severe, low buffer, volatile, variable, fluctuation, drop, zero, consistent, smoothness, auto-tuning, regime, cluster, guidance, hybrid, generalization, environment-aware, prediction, selector`

**Fragmento 1 - p. 4 - score 2:**

A proportional-integral controller outputs a video rate that matches the esti- mated available and ensures the buffer is maintained at the target level. Optimization-based approaches are widely used for bitrate adaptation in DASH. Essentially, the opti- mization problem is solved based on the prediction of buffer dynamics and network throughput. How- ever, stochastic segment size shifts the buffer occu- pancy from the estimated value. In order to get rid of this effect and improve the prediction accuracy for buffer occupancy [11] propose an algorithm based on Markov decision process (MDP) with segment size information so that only the network capacity vari- ation need to be considered in the decision-making process.

**Fragmento 2 - p. 8 - score 2:**

The dataset contains client-side cellular performance indicators such as throughput information and other channel and context-related metrics. These metrics are gen- erated from a network monitoring application called G-NetTrack Pro [27]. 4.6 Comparison to Benchmarks The proposed approach is compared to three bench- marks in the literature: The heuristic rate-based (RB) approach, the model optimization hybrid-based (HB) approach, and the classical DQN learning-based approach. The RB approach selects the highest bitrate that is smaller than the predicted throughput regard- less of the previously selected bitrates. This is referred to as a stateless adaptation algorithm [28]. The adap- tation method is a quality level selector based on the predicted adaptation network throughput which is estimated through a moving average window of N steps.

**Fragmento 3 - p. 3 - score 1:**

Section III describes the methodology. Section IV details the implementation and the simulation setup. Section V is dedicated to the performance evaluation of the proposed approach and section VI gives the conclusions of this study. 2 Literature review of existing solutions Adaptation methods and algorithms are still under- going extensive research work regardless of the pub- lic adoption [4–6]. This is owed to the contin- uously updated internet video delivery ecosystem. This section illustrates the various classic adaptation approaches. The existing approaches are classiﬁed into two main categories; Traditional adaptation tech- niques and ML-based adaptation methods. In the tra- ditional adaptation case, the solutions are customized for predetermined scenarios.

**Fragmento 4 - p. 4 - score 1:**

A buffer-based adaptation approach that does not rely on throughput prediction methods is presented in [12]. The algorithm solves optimization problem based on the buffer length reservation. It downloads the lowest bitrate and tries to maintain the buffer occu- pancy within a certain threshold. Another adaptation logic based on optimization techniques is presented in [13] which introduces a novel probing based net- work measurement technique to advance the video quality selection. It also presents a QoE-aware DASH system, called QDASH, with mixed-integer linear pro- gramming. The authors in [14] used an optimization mechanism with two objective functions: The ﬁrst function maximizes the overall average QoE among DASH clients, while the second function minimizes the negative impact of temporal video quality changes; that is the up and down switching between different representation during playback.

**Fragmento 5 - p. 5 - score 1:**

Springer LATEX template strategy for DASH clients based on an MDP optimiza- tion was proposed in [20]. The authors introduced a penalty function into the reward function to penalize the system for re-buffering events as well as moving away from a safe buffer level. Authors in [21] presented a framework, called D-DASH, that combines deep learning and reinforce- ment learning techniques to optimize the QoE of DASH. They combined feed-forward and recurrent deep neural networks with advanced strategies. The numerical results are obtained on real and simulated channels. Besides yielding a considerably higher QoE, the D-DASH framework exhibits fast convergence rate. Recently, the authors in [22] used enhanced deep Q-learning for DASH video applications, and proposed a QoE-oriented rate adaptation framework based on enhanced deep Q-learning.

**Fragmento 6 - p. 5 - score 1:**

Finally, the DQNReg-based rate adapta- tion technique is detailed. 3.1 Video Streaming Model In this paper, a video sequence is modeled as a set of Ns consecutive segments. Each segment lasts for Ts seconds, and is encoded at the bitrate Rv. The client video player requests a segment at bitrate Rv i for the i-th segment. The selected bitrate Rv i is mapped to different quality levels {Q1, Q2, . . . , QN} based on the client device speciﬁcations and the available video content. In general, The higher the bitrate used in encoding, the higher the video quality delivered to the viewer. Suppose that Qj is the quality level requested for the i-th segment, and let its corresponding bitrate be Rv i . If Li be the size of the i-th segment in bits then, for a constant bitrate (CBR) case, Li = TsRv i .

**Fragmento 7 - p. 5 - score 1:**

This relationship does not hold for the variable bitrate (VBR) case, however. The video client application requests segments, waits for the underlying network to deliver them, and then downloads them into a buffer whose instanta- neous temporal occupancy is denoted as T B i . This parameter is measured in seconds, and in a typical setting, may contain tens of seconds worth of video segments. In this paper, we assume that it ranges in the interval [0, T B max]. If the average network through- put be Rn i during the downloading of the i-th segment, then the needed download time will be Li/Rn i . Since Li depends on the segment quality, therefore the download time depends on the segment bitrate Rv i .

**Fragmento 8 - p. 8 - score 1:**

It is necessary to note that the quality of the dataset impacts the performance of the learning agent. These traces allow the agent to experience throughput variations in real networks. 4.3 Simulation Setup A simulation testbed based on the video streaming environment is implemented in SimEvent discrete- event simulator in MATLAB. The testbed simulates the video player buffer dynamics during the process of receiving and playing back video segments based on a bitrate range and network proﬁles. To train the agent a corpus of network traces is created through con- catenating different excerpts of the network datasets, which will be detailed in the section below. The size of the buffer is set T B max = 60s which is common in a DASH video player.

**Fragmento 9 - p. 8 - score 1:**

The buffer status is not considered during the quality selection decision. The HB approach is a hybrid adaptation algorithm that combines both the traditional RB and the QoE-based optimization adap- tation approach [29]. The HB approach maximizes the average video quality and minimizes the rebuffering duration while maintaining the quality variation to a certain threshold. Finally, the proposed DQNReg is compared to the classical DQN algorithm. 4.7 Simulation Results The DQNReg model is evaluated on the testing datasets, both ﬁxed and mobile. The trained DQNReg

**Fragmento 10 - p. 9 - score 1:**

3 Buffer occupancy for: a) RB, b) HB, c) DQN, and d) DQNReg methods in a WLAN environment. reward function is computed and normalized. High Average QoE reﬂect, high average video quality, low re-buffering duration and fewer quality switch- ing times. 2. Rebuffering times: Measures the number of instances when the buffer occupancy is zero. 3. Rebuffering duration: Measures the total rebuffering time over the entire video playback duration. 4. Inter-starvation length: Measures the time duration that separates successive rebuffering instants [31]. 5. Quality switching times: Counts the number of times the algorithm switches across different qual- ity levels. This reﬂects the number of times the user-perceived quality changes across the entire video playback.


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
Reinforcement Learning-Based Rate Adaptation in
Dynamic Video Streaming
Nada A. Hafez 
American University of Sharjah
Mohamed S. Hassan 
American University of Sharjah
Taha Landolsi  (  tlandolsi@aus.edu )
American University of Sharjah https://orcid.org/0000-0001-8479-9056
Research Article
Keywords: Bitrate Adaptation, DASH, Deep Q-learning, Optimization, Reinforcement Learning, Video
Streaming
Posted Date: August 22nd, 2022
DOI: https://doi.org/10.21203/rs.3.rs-1616726/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
```


### Pagina 2
```text
Springer LATEX template
Reinforcement Learning-Based Rate Adaptation in Dynamic
Video Streaming
N. A. Hafez, M. S. Hassan and T. Landolsi
American University of Sharjah, Sharjah, UAE.
*Corresponding author(s). E-mail(s): tlandolsi@aus.edu;
Contributing authors: g00039071@aus.edu; mshassan@aus.edu;
Abstract
Video streaming stands out as the most signiﬁcant trafﬁc type consumed by mobile devices. This increased
demand has been a major driver for research on bitrate adaptation algorithms. Bitrate adaptation ensures high
user-perceived quality, which, in turn, correlates with higher proﬁts for content providers and delivery sys-
tems. Dynamic adaptive streaming over HTTP (DASH) is a widely adopted video streaming standard utilized
by service providers to provide competitive quality of experience (QoE). It is capable of providing seamless
streaming via uncertain network conditions by switching across different video qualities and their correspond-
ing video segment bitrates. The complexity of the video streaming environment makes it a good candidate
for different learning-based approaches. Accordingly, this paper proposes a reinforcement-learning (RL) deep
Q-network called DQNReg, that enhances the classical deep Q-learning method. A segment-wise QoE-based
reward function is formulated so that the learning strategy can converge towards maximizing the QoE out-
come. The proposed RL-based adaptation approach is evaluated using trace-based simulation for both wireless
local area network channels and 5G mobile channels. The performance of this RL-based method is compared
to three methods: A heuristic method, a model-based method, and a classical learning-based method. The com-
parison shows that the RL-based method converges faster while achieving a high QoE score. In addition, it
reduces the re-buffering duration while maintaining higher video quality and relatively lower quality variations.
Keywords: Bitrate Adaptation, DASH, Deep Q-learning, Optimization, Reinforcement Learning, Video Streaming
1 Introduction
With the constant updates to the wireless LAN
(WLAN) standards and the gradual roll out of 5G
mobile networks, wireless technology is expected to
deliver high multi-Gbps peak data rates, ultra-low
latency, increased reliability and decreased network
management complexity [1]. Enhanced mobile broad-
band with more uniform data rates and increased efﬁ-
ciency empower new and improved user experiences.
At the moment, video streaming stands out as the most
signiﬁcant trafﬁc type consumed by mobile devices
accounting for an average of 60% of total trafﬁc.
This percentage is anticipated to increase to 74% by
the end of 2024. Consumer behavior is shifting from
low-deﬁnition (360p) and standard-deﬁnition formats
(480p) to high-deﬁnition video (720p and 1080p)
as network capabilities improve. In addition, viewer
behavior is expected to change more dramatically as
5G services are made available [2]. The quality of
experience (QoE) perceived by the users is affected
by several factors like video quality, quality switch-
ing and re-buffering duration [3] which are inﬂuenced
by video streaming strategies which typically rely on
adaptive bitrate (ABR) techniques for video streaming
to enhance video delivery and customer satisfaction.
1
```


### Pagina 3
```text
Springer LATEX template
Dynamic adaptive streaming over HTTP (DASH)
technology utilizes HTTP as its application layer pro-
tocol along with TCP as its transport layer proto-
col. DASH allows the bitrate and consequently the
quality of the video to adjust according to the avail-
able resources in the underlying network. Relevant
resources are typically the network throughput and
the availability of the playback buffer [3]. The client
initiates a streaming session with the server and gets
the desired video’s manifest ﬁle. The media presenta-
tion description (MPD) provides required information
such as uniform resource locators (URL), bitrates,
resolutions, sizes, and availability of the video seg-
ments. Typically the video ﬁle is divided into short
segments (1-10 seconds long) and encoded at several
quality levels (QL). DASH enables seamless switch-
ing between quality levels for each segment based
on the streaming client local information about cer-
tain network quality of service (QoS) parameters,
such as the network throughput and delay, the video
client playback buffer occupancy and the video server
workload.
Most ABR methods are based on heuristic algo-
rithms, which can be categorized into throughput-
based or buffer-based approaches [4]. The heuristic
techniques rely on customized, hard-coded algorithms
for bitrate selection, which may result in a poor per-
formance under different network environments. For
instance, the persistent bandwidth ﬂuctuations in the
mobile network impose a challenge on ABR meth-
ods [1]. In such a dynamic environment a ﬂexible
ABR strategy is needed so as to intelligently adjust
and maintain a good performance.
In this paper, we demonstrate that an ABR strategy
based on a machine learning (ML) technique, called
reinforcement learning (RL), provides an intelligent
and effective solution to the dynamic rate adaptation
problem. In RL, an agent learns about the dynamic
environment through trial-and-error interactions. The
agent takes an action and receives a reward from the
environment. The objective of an agent is to maxi-
mize the discounted cumulative rewards by learning
the optimal actions and then gradually converging to
the optimal policy. Every agent memorizes the conse-
quences of his actions and avoids them if they resulted
in low revenues in the past. With respect to the rate
adaptation problem, the environment for RL includes
the network throughput, the available video qualities
of the video segments, and the video client playback
buffer occupancy.
In this paper, a RL-based deep Q-learning is pro-
posed to achieve ﬁne video adaptation through the
experience acquired from exploring the network envi-
ronment. The objective is to achieve a fast conver-
gence for the RL-based algorithm while enhancing
the QoE performance under wireless local area net-
works as well as 5G network conditions. The rest of
this paper is organized as follows: Section II provides
an overview of related work. Section III describes the
methodology. Section IV details the implementation
and the simulation setup. Section V is dedicated to the
performance evaluation of the proposed approach and
section VI gives the conclusions of this study.
2 Literature review of existing
solutions
Adaptation methods and algorithms are still under-
going extensive research work regardless of the pub-
lic adoption [4–6]. This is owed to the contin-
uously updated internet video delivery ecosystem.
This section illustrates the various classic adaptation
approaches. The existing approaches are classiﬁed
into two main categories; Traditional adaptation tech-
niques and ML-based adaptation methods. In the tra-
ditional adaptation case, the solutions are customized
for predetermined scenarios. On the other hand, in the
ML-based case the video playback system learns to
adapt to the network environment even under unfore-
seen conditions. Typically, network QoS parameters
and video playback buffer information are used in
these methods.
2.1 Traditional Adaptation Bitrate
Techniques
Heuristic-based techniques can be categorized into
two types [4]. The ﬁrst type comprises a set of
throughput-based techniques, in which a video client
relies on observed network throughput to make a
decision about the bitrates of future requested seg-
ments [7]. The second type comprises a set of buffer-
based techniques which utilize the available playback
buffer space to determine the quality of the future
requested segments [8]. Authors in [9] presented a pre-
diction model to accurately approximate the trend of
buffer level variation in the client side. The quality
switching in the adaptation is reduced based on the
approximation. It can be concluded from the results
that a steady video quality is achieved when buffer
```


### Pagina 4
```text
Springer LATEX template
3
underﬂows are reduced. Nonetheless, the main draw-
back of the heuristic based techniques is that they
cannot be generalized since they are deterministically
customized to particular network conditions.
Control theory is used to model dynamical sys-
tems that are stable and accurate. The work in [3]
introduces a model predictive control approach which
optimizes the QoE function by selecting bitrates based
on throughput approximation. It predicts throughput
of upcoming segments downloads based on existing
samples of recently downloaded segments. The work
in [10] proposes an adaptation logic based on feed-
back control. The quality adaptation controller takes
a buffer as an input and returns the video rate of the
segment to be downloaded. A proportional-integral
controller outputs a video rate that matches the esti-
mated available and ensures the buffer is maintained
at the target level.
Optimization-based approaches are widely used
for bitrate adaptation in DASH. Essentially, the opti-
mization problem is solved based on the prediction
of buffer dynamics and network throughput. How-
ever, stochastic segment size shifts the buffer occu-
pancy from the estimated value. In order to get rid
of this effect and improve the prediction accuracy for
buffer occupancy [11] propose an algorithm based on
Markov decision process (MDP) with segment size
information so that only the network capacity vari-
ation need to be considered in the decision-making
process.
A buffer-based adaptation approach that does not
rely on throughput prediction methods is presented
in [12]. The algorithm solves optimization problem
based on the buffer length reservation. It downloads
the lowest bitrate and tries to maintain the buffer occu-
pancy within a certain threshold. Another adaptation
logic based on optimization techniques is presented
in [13] which introduces a novel probing based net-
work measurement technique to advance the video
quality selection. It also presents a QoE-aware DASH
system, called QDASH, with mixed-integer linear pro-
gramming. The authors in [14] used an optimization
mechanism with two objective functions: The ﬁrst
function maximizes the overall average QoE among
DASH clients, while the second function minimizes
the negative impact of temporal video quality changes;
that is the up and down switching between different
representation during playback.
2.2 RL-Based Adaptation
Existing classic ABR algorithms mostly rely on ﬁxed
heuristics that have been ﬁne tuned according to
ﬁxed assumptions about deployment environments.
Not only that, but each of these approaches have
been designed to optimize for a speciﬁc QoE metric.
Consequently, if the assumptions are breached, these
ABR algorithms fail to generalize and perform poorly.
To overcome these issues, learning-based adaptation
approaches are explored. With machine learning tech-
niques a client can learn to adapt its video quality to
the changing context without the need for any human
intervention.
Authors in [15] use a decision-tree based random
forest classiﬁcation to map network related features
onto the video rate. The scheme trains the classiﬁ-
cation model using a dataset. The classiﬁer is then
used to predict the current request or any future video
request. RL allows an agent to discover the right action
to take, within a particular context, based on feed-
back from its environment. To do this, an adaptation
module interacts with its environment by sensing fac-
tors that are expected to inﬂuence its decision. For
example, in [16], a system that generates ABR algo-
rithms using RL is introduced. This system trains a
neural network model that selects bitrates for future
video segments based on observations collected by
client video players. This system does not rely on
pre-programmed models or assumptions about the
environment. Instead, it learns to make ABR decisions
solely through observations of the resulting perfor-
mance of past decisions.
In [17], the authors incorporated an RL method
with the addition of Q-Learning. The action is set
as the segment request with a particular bitrate and
the reward is deﬁned as the QoE approximation. The
study maximizes the QoE through adjusting the adap-
tation behavior as per the existing network conditions.
Another learning based approach propose to combine
the nearest neighbor (KNN) with Q-learning algo-
rithm [18]. In this bitrate adaptive scenario, the KNN-
Q learning can achieve higher QoE and faster conver-
gence speed than the Q-learning algorithm alone.
Authors in [19] introduce a system that trains the
policy via imitating expert trajectories given by the
instant solver. The system attempts to pick the seg-
ment with higher perceptual video qualities rather than
video bitrates by constructing a neural network archi-
tecture, video datasets and QoE metrics with video
quality features. Another online learning adaptation
```


### Pagina 5
```text
Springer LATEX template
strategy for DASH clients based on an MDP optimiza-
tion was proposed in [20]. The authors introduced a
penalty function into the reward function to penalize
the system for re-buffering events as well as moving
away from a safe buffer level.
Authors in [21] presented a framework, called
D-DASH, that combines deep learning and reinforce-
ment learning techniques to optimize the QoE of
DASH. They combined feed-forward and recurrent
deep neural networks with advanced strategies. The
numerical results are obtained on real and simulated
channels. Besides yielding a considerably higher QoE,
the D-DASH framework exhibits fast convergence
rate. Recently, the authors in [22] used enhanced
deep Q-learning for DASH video applications, and
proposed a QoE-oriented rate adaptation framework
based on enhanced deep Q-learning. They established
chunk-wise subjective QoE model and utilize it as
the reward function in reinforcement learning so that
the strategy can converge toward the direction of
maximizing the subjective QoE score.
In our paper work, we use a reinforcement-based
deep Q-learning method, called DQNReg [23], to
provide a ﬁne video adaptation through the experi-
ence acquired from exploring the network conditions.
The objective of the proposed method is to enhance
the QoE performance under dynamic network condi-
tions, and achieve a fast convergence while maintain-
ing higher average rewards than other learning-based
methods.
3 Methodology
In this section, the video streaming model is presented.
The DQNReg algorithm and its reward function are
introduced. Finally, the DQNReg-based rate adapta-
tion technique is detailed.
3.1 Video Streaming Model
In this paper, a video sequence is modeled as a set of
Ns consecutive segments. Each segment lasts for Ts
seconds, and is encoded at the bitrate Rv. The client
video player requests a segment at bitrate Rv
i for the
i-th segment. The selected bitrate Rv
i is mapped to
different quality levels {Q1, Q2, . . . , QN} based on
the client device speciﬁcations and the available video
content. In general, The higher the bitrate used in
encoding, the higher the video quality delivered to the
viewer. Suppose that Qj is the quality level requested
for the i-th segment, and let its corresponding bitrate
be Rv
i . If Li be the size of the i-th segment in bits
then, for a constant bitrate (CBR) case, Li = TsRv
i .
This relationship does not hold for the variable bitrate
(VBR) case, however.
The video client application requests segments,
waits for the underlying network to deliver them, and
then downloads them into a buffer whose instanta-
neous temporal occupancy is denoted as T B
i . This
parameter is measured in seconds, and in a typical
setting, may contain tens of seconds worth of video
segments. In this paper, we assume that it ranges in
the interval [0, T B
max]. If the average network through-
put be Rn
i during the downloading of the i-th segment,
then the needed download time will be Li/Rn
i . Since
Li depends on the segment quality, therefore the
download time depends on the segment bitrate Rv
i .
The buffer size is depleted as the video is played and
is replenished as segments are downloaded. Rebuffer-
ing or starvation events happen when the playback
buffer of the client has been depleted and the consecu-
tive video segment does not arrive before its scheduled
playback time. If the buffer occupancy is T B
i
before
the i-th segment is downloaded, then it will become
just after it is downloaded:
T B
i+1 = T B
i −Li
Rn
i
+ Ts.
(1)
Therefore, if sufﬁcient buffer content is maintained
before loading, i.e. if T B
i
> Li/Rn
i , then rebuffering
or starvation events will not take place.
3.2 DQNReg algorithm
Many enhancements for the classic deep Q-learning
techniques have been proposed. One such a technique
is the DQNReg [23]. It builds on the classical DQN
algorithm by adding a weighted penalty to the normal
squared Bellman error. The authors in [23] proposed
evolution strategies by exploring the space of compu-
tational graphs which calculates the loss function for
an RL agent. They highlighted that DQNReg shows
an improved performance over DQN in environments
that have not been experienced during training. Their
analysis showed that DQNReg outperforms DQN as
well other well-known variants such as the double
DQN (DDQN). DQNReg is typically characterized
with the following set of equations [23]:
Yt = rt + γ max
a
Qtarg(st+1, a),
(2)
δ = Q(st, at) −Yt,
(3)
```


### Pagina 6
```text
Springer LATEX template
5
Adaptation 
Algorithm
Video 
Player
1
7
6
5
4
3
2
8
9
Server
1
7
6
5
4
3
2
8
9
QL1
1
7
6
5
4
3
2
8
9
QL2
1
7
6
5
4
3
2
8
9
QL3
Segment S7-QL3
Video sequence with 3 quality levels
Received Video Segments
New
HTTP
Requests
Past segment params.:
1. Network throughput, 

2. Segment bit rate, 

3. Buffer occupancy, 

QL1
QL2
QL3
HTTP GET S1-QL1, … , S3-QL1
1
2
3
HTTP GET S4-QL2, … , S6-QL2
4
5
6
HTTP GET S7-QL3, … , S9-QL3
7
8
9
Quality
Selection
HTTP
Responses
1
4
7
	 

    

 

DQNReg network with reward function:
action
RL agent
Wireless
Network
(WLAN or 5G)
Fig. 1 Proposed RL-based rate adaptation scheme using a DQNReg network.
LReg = αQ(st, at) + δ2,
(4)
where Yt is the target Q-value at the time step t, rt
is the instantaneous reward, at is the instantaneous
action output by the agent to the environment, γ is
a discount factor, δ is the DQN loss function, and st
and st+1 are the states at t and t + 1, respectively.
Here, LReg is the DQNReg loss function, Q(st, at) is
the Q-value penalty, α is a weight factor, and δ2 is the
squared error.
Classical DQN algorithms tend to overestimate the
Q-value, which might be a potential problem [23].
It shows that the learned constraints starts early in
the training. To address this issue and avoid overes-
timation, the weighted penalty is added to DQNReg
loss function as shown in equation (4). Consider-
ing the characteristics of the DASH rate adaptation,
DQNReg is expected to enable the trained agent to
obtain improved QoE performance gain. The QoE-
based reward function is explained in the following
section.
3.3 Reward Function
The QoE is impacted by the video quality of the
viewed segment, the frequency of quality switching
and the experienced re-buffering events. A reward
function that represents these factors is introduced to
issue policies that maximize the QoE perceived by the
users. The reward function is deﬁned as follows [3,
16]:
QoE = Rv
i −µDB −∥Rv
i+1 −Rv
i ∥,
(5)
where Rv
i is the bitrate of the i-th video segment, DB
is the rebuffering duration experienced when the play-
out buffer level, when a segment is downloaded, is
lower than the needed segment download time. The
rebuffering duration is given by:
DB = Rv
i
Rn
i
Ts −T B
i .
(6)
The parameter µ is a penalty coefﬁcient for the experi-
enced rebuffering event. Finally, the term ∥Rv
i+1−Rv
i ∥
reﬂects the quality variation between two consecutive
segments.
3.4 Rate Adaptation with DQNReg
The DQNReg algorithm is implemented as follows:
Once the segment is downloaded, the RL agent
receives the state inputs at segment i,
si = (Rv
i−1, Rn
i , T B
i , T D
i , NR),
(7)
```


### Pagina 7
```text
Springer LATEX template
where Rv
i−1 is the bitrate at which the last video seg-
ment was downloaded, Rn
i is the network throughput
measurement, T B
i is the current buffer level, T D
i is the
download time of the past video segment and NR is
the available bitrate for the next video segment. The
learning agent observes the state si from the environ-
ment then takes an action ai which is selecting the
bitrate for the upcoming video segment. In turn, the
agent receives the corresponding reward. It is to be
noted that the state transition in the environment is
also impacted by the action taken.
The action selected depends on the policy π, which
is deﬁned as the mapping of the action to state or the
probability distribution over actions. π(si, ai) is the
probability that action ai is taken in si. Practically,
there are intractably several si, ai pairs, to overcome
this a neural network is utilized to represent the pol-
icy with manageable number of parameters θ, usually
referred to as policy parameters. The advantage of
neural networks is that they can deal with raw signals
and do not need to have hand-crafted features.
In value-based RL, the agent along side the neu-
ral network is expected to extract important features
from the state, provide accurate estimation of the state-
action value and ﬁnally derive the optimal policy. For
a well-trained value network the optimal policy is
derived as follows:
πθ = arg max
a
Q(si, a).
(8)
The learning process of the agent is the training pro-
cess of the state-action value network. By regularly
observing the environment, the agent gathers tuples
containing the previous state, the new state, the action
to be undertaken, and the reward to be given to
the learner. The temporal-difference technique is then
applied to perform gradient descent [22]. This allows
the value network to estimate the real state-action
value function with adequate accuracy.
4 Implementation and Simulation
This section showcases the implementation of the pro-
posed DQNReg-based adaptation approach with the
simulation setup, the video parameters, and network
traces. It is noteworthy to indicate that the neural net-
work architecture is not a priority of this paper, hence a
default network architecture was adopted for the simu-
lation. The DQNReg simulation results are contrasted
with other benchmark approaches.
0
100
200
300
400
500
600
700
800
900
1000
Episode Number
0.7
0.8
0.9
1
1.1
1.2
1.3
1.4
1.5
1.6
Average QoE 
DQNReg
DQN
Fig. 2 Training convergence of DQNReg vs. DQN methods.
4.1 Implementation and Training
algorithm
The neural network architecture, similar to [16]
and [22], is composed of 1D convolution layer com-
posed of 128 ﬁlters. The output of these layers is
then aggregated with other inputs in a hidden layer,
that uses 128 neurons, to apply the rectiﬁed linear
unit (ReLU) activation function.The number of neu-
rons in the output layer is equal to the adaptive bitrate
set, which we have denoted as NR. The training
is performed on a sequence extracted from the Big
Buck Bunny video (available for download from the
Blender.org site [24], for example). Once the obser-
vation states are collected by the agent, the Q-value
table or the weights in the network are updated until
the policy converges. Certain hyper-parameters were
set similar to [16, 21, 22]. The weight factor used
here is α = 0.1, the discount factor is γ = 0.99,
the learning rate is 10−5 and the exploration adopted
was the ǫ-greedy to explore many states and have a
maintain a trade-off between exploration and exploita-
tion. The training algorithm takes the bitrate selection
for a video segment as a step, it then takes the step
experience and stores it into the experience buffer. In
Figure 2, the average QoE reward on the training set
is plotted against the number of training episodes for
both DQNReg and DQN. It is clear that DQNReg con-
verges faster and achieves higher average QoE value.
4.2 Video Streaming Environment
The video streaming environment consists of a set of
videos encoded at different rates. An internal repre-
sentation of the client’s playback buffer is maintained.
A download time is assigned based on the segment’s
bitrate and available network throughput. To represent
```


### Pagina 8
```text
Springer LATEX template
7
the video playback during the download, the playback
buffer is drained by the current segment download
time. In case the playback buffer is fully occupied,
500ms delay is applied before fetching the other seg-
ment. After each segment download, various state
observations such as buffer occupancy and current
segment bitrate are passed to the learning agent. The
learning agent then tries to maximize the reward QoE
value, which is impacted by the varying network con-
ditions. To design a network that faithfully emulates
real conditions, throughput from a corpus of real net-
work traces were used. The traces are used to shape the
agent’s experience and help it predict the environment
dynamics such as the anticipated network through-
put. It is necessary to note that the quality of the
dataset impacts the performance of the learning agent.
These traces allow the agent to experience throughput
variations in real networks.
4.3 Simulation Setup
A simulation testbed based on the video streaming
environment is implemented in SimEvent discrete-
event simulator in MATLAB. The testbed simulates
the video player buffer dynamics during the process of
receiving and playing back video segments based on a
bitrate range and network proﬁles. To train the agent
a corpus of network traces is created through con-
catenating different excerpts of the network datasets,
which will be detailed in the section below. The size
of the buffer is set T B
max = 60s which is common in a
DASH video player. The segment-wise QoE reward is
estimated after each bitrate selection.
4.4 Video Parameters
In the simulation, the video used is Big Buck Bunny,
which is a simple animation short clip of 10 minutes
and 34 seconds duration under the Peach open movie
project. The video content consists of animated char-
acters with a non intricate background [25]. The video
in the dataset is encoded by the H.264/MPEG-4 codec
to thirteen different representation rates, ranging from
235 kbps to 40 Mbps. The 4-second segment group is
selected from the full DASH proﬁle.
4.5 Network Traces
The proposed approach is examined using realistic
network environment conditions. Real network traces
are used from a ﬁxed WLAN [26] network and a
mobile 5G network [1]. It is important to note the
difference in the offered throughput and the mobility
pattern in the two networks as it affects the quality and
the performance of the approaches.
4.5.1 WLAN Channel Environment
The average WLAN network throughput trace is
obtained from [26] and used in the deployed algo-
rithm. The throughput is limited to less than 2 Mbps.
The dataset contains client-side cellular key perfor-
mance indicators such as throughput information and
other context related metrics.
4.5.2 Mobile Channel Environment
The 5G network trace is taken from a publicly avail-
able dataset which was collected from a mobile oper-
ator [1]. The dataset is created from a static and
a driving vehicle mobility patterns, where the net-
work throughput reaches up to 200 Mbps. The dataset
contains client-side cellular performance indicators
such as throughput information and other channel
and context-related metrics. These metrics are gen-
erated from a network monitoring application called
G-NetTrack Pro [27].
4.6 Comparison to Benchmarks
The proposed approach is compared to three bench-
marks in the literature: The heuristic rate-based
(RB) approach, the model optimization hybrid-based
(HB) approach, and the classical DQN learning-based
approach. The RB approach selects the highest bitrate
that is smaller than the predicted throughput regard-
less of the previously selected bitrates. This is referred
to as a stateless adaptation algorithm [28]. The adap-
tation method is a quality level selector based on
the predicted adaptation network throughput which
is estimated through a moving average window of
N steps. The buffer status is not considered during
the quality selection decision. The HB approach is a
hybrid adaptation algorithm that combines both the
traditional RB and the QoE-based optimization adap-
tation approach [29]. The HB approach maximizes the
average video quality and minimizes the rebuffering
duration while maintaining the quality variation to a
certain threshold. Finally, the proposed DQNReg is
compared to the classical DQN algorithm.
4.7 Simulation Results
The DQNReg model is evaluated on the testing
datasets, both ﬁxed and mobile. The trained DQNReg
```


### Pagina 9
```text
Springer LATEX template
agent is employed to pick the rate of the video segment
to be downloaded. Once the bitrate is selected, the
bitrate is mapped to one of four quality levels to better
illustrate the quality changes. The performance of the
DQNReg agent for each channel environment type is
illustrated. The DQNReg performance is compared to
the benchmark approaches.
Figures 3–6 illustrate the buffer occupancy and
quality levels in both ﬁxed and mobile environments
for DQNReg compared to the RB, HB, and DQN
benchmark approaches. It is clear that both HB and
DQN perform better than RB. Although RB maintains
a relatively low number of quality jumps in differ-
ent environments, it greatly suffers from rebuffering
events. It is evident that RB does not manage the
buffer occupancy well which would greatly impact
its performance. It is noted that, with DQNReg both
the buffer starvation instances (which cause rebuffer-
ing events) and the frequency of quality switching
are signiﬁcantly reduced compared to all other meth-
ods. DQNReg outperforms other approaches in the
two simulated environments as it does not suffer
from rebuffering events in the ﬁxed environment,
while maintains relatively frequency of quality vari-
ations. Furthermore, DQNReg reduces the starvation
instances in the mobile environment. Although DQN
shows a relatively low number of rebuffering events, it
struggles with quality variations, which is noticeably
reduced in DQNReg.
5 Performance Evaluation and
Discussion
After performing extensive simulations in different
network environments, the performance of the sim-
ulated approaches is analyzed and evaluated. The
evaluation metrics used are explained then the DQN-
Reg adaptation approach is evaluated and compared to
the aforementioned benchmark approaches.
5.1 Evaluation Metrics
The proposed method’s performance is evaluated
using the following metrics:
1. Average QoE: The QoE objective is a sum of
weighted objectives that have varying orders of
magnitudes. To make fair comparisons it is impor-
tant to transform the objective functions in a way
that they all have comparable orders of magni-
tude [30]. The average QoE, calculated through the
0
50
100
150
200
250
300
350
400
450
500
Time (s)
0
20
40
60
Buffer Length (s)
a)
260
280
300
320
340
360
380
400
420
440
460
Time (s)
0
20
40
60
Buffer Length (s)
b)
0
50
100
150
200
250
300
350
400
450
500
Time (s)
0
20
40
60
Buffer Length (s)
c)
0
50
100
150
200
250
300
350
400
450
500
Time (s)
0
20
40
60
Buffer Length (s)
d)
Fig. 3 Buffer occupancy for: a) RB, b) HB, c) DQN, and d)
DQNReg methods in a WLAN environment.
reward function is computed and normalized. High
Average QoE reﬂect, high average video quality,
low re-buffering duration and fewer quality switch-
ing times.
2. Rebuffering times: Measures the number of
instances when the buffer occupancy is zero.
3. Rebuffering
duration:
Measures
the
total
rebuffering time over the entire video playback
duration.
4. Inter-starvation
length:
Measures
the
time
duration that separates successive rebuffering
instants [31].
5. Quality switching times: Counts the number of
times the algorithm switches across different qual-
ity levels. This reﬂects the number of times the
user-perceived quality changes across the entire
video playback.
```


### Pagina 10
```text
Springer LATEX template
9
0
50
100
150
200
250
300
350
400
450
500
Time (s)
1
2
3
4
Quality Level
a)
0
50
100
150
200
250
300
350
400
450
500
Time (s)
1
2
3
4
Quality Level
b)
0
50
100
150
200
250
300
350
400
450
500
Time (s)
1
2
3
4
Quality Level
c)
0
50
100
150
200
250
300
350
400
450
500
Time (s)
1
2
3
4
Quality Level
d)
Fig. 4 Quality level for: a) RB, b) HB, c) DQN, and d) DQNReg
methods in a WLAN environment.
5.2 Performance Comparison
Figure 7 illustrates the average QoE for all four sim-
ulated approaches across all simulated network envi-
ronments. The DQNReg method achieved the highest
score in comparison to the other methods. The HB
method average score is comparable to that of the
DQN one, but has a relatively larger variance. The RB
method, however, showed the lowest average score but
with a larger variance compared to the other methods.
The number of rebuffering instances for all algo-
rithms in all simulated network environments is shown
in Figure 8. The RB method has the highest number of
starvation instances with smallest variance, this means
that rebuffering instances will occur with rate-based
regardless of the network condition. This is owed to
the fact that the RB method ignores the playback
buffer occupancy and considers the network through-
put only. The HB and DQN methods achieved similar
0
50
100
150
200
250
300
350
400
450
500
Time (s)
0
20
40
60
Buffer Length (s)
a)
0
50
100
150
200
250
300
350
400
450
500
Time (s)
0
20
40
60
Buffer Length (s)
b)
0
50
100
150
200
250
300
350
400
450
500
Time (s)
0
20
40
60
Buffer Length (s)
c)
0
50
100
150
200
250
300
350
400
450
500
Time (s)
0
20
40
60
Buffer Length (s)
d)
Fig. 5 Buffer occupancy for: a) RB, b) HB, c) DQN, and d)
DQNReg methods in a 5G mobile environment.
average rebuffering times. Finally, DQNReg achieved
the lowest average number of rebuffering times with
variance similar to that of DQN.
The overall rebuffering duration experienced dur-
ing the video playback for all algorithms in all sim-
ulated network environments is observed in ﬁgure 9.
Again, the RB method has the longest rebuffering
duration with a small variance. The HB and DQN
methods achieved similar average rebuffering dura-
tion of about 10 seconds. Finally, DQNReg achieved
the lowest average rebuffering duration of about 7
seconds.
The average inter-starvation length for all algo-
rithms in all simulated network environments is illus-
trated in Figure 10. Again, the RB method has the
lowest performing method with respect to rebuffer-
ing. The RB method has the lowest inter-starvation
duration, meaning that rebuffering events will take
```


### Pagina 11
```text
Springer LATEX template
0
50
100
150
200
250
300
350
400
450
500
Time (s)
1
2
3
4
Quality Level
a)
0
50
100
150
200
250
300
350
400
450
500
Time (s)
1
2
3
4
Quality Level
b)
0
50
100
150
200
250
300
350
400
450
500
Time (s)
1
2
3
4
Quality Level
c)
0
50
100
150
200
250
300
350
400
450
500
Time (s)
1
2
3
4
Quality Level
d)
Fig. 6 Quality level for: a) RB, b) HB, c) DQN, and d) DQNReg
methods in a 5G mobile environment.
Fig. 7 Average QoE for RB, HB, DQN, and DQNReg methods.
place successively with short video playback time in
between. The HB and DQNReg approaches have com-
parable average inter-starvation lengths while DQN
has the highest median value of about 100 seconds and
is negatively skewed.
The overall number of quality switch times expe-
rienced during the video playback for all algorithms
Fig. 8 Rebuffering instances for RB, HB, DQN, and DQNReg
methods.
Fig. 9 Rebuffering lengths for RB, HB, DQN, and DQNReg meth-
ods.
Fig. 10 Inter-starvation lengths for RB, HB, DQN, and DQNReg
methods.
in the simulated network environments is shown in
Figure 11. DQNReg keeps the quality stable with a
low variance and smaller number of quality switching
times. Both RB and HB methods have similar aver-
age for quality switching times. However, HB has a
very high variance and is positively skewed. Simi-
larly, DQN has the highest variance which may mean
that the number of quality switching may greatly vary
across different environments.
5.3 Analysis and Discussion
Comparing
the
various
simulated
adaptation
approaches, the advantage of the RB method is being
```


### Pagina 12
```text
Springer LATEX template
11
Fig. 11 QL switching instances for RB, HB, DQN, and DQNReg
methods.
a low complexity algorithm and yields fewer qual-
ity switching instances. However, it suffers more
frequent rebuffering instances, longer rebuffering
durations, and shorter inter-starvation lengths. As
for the HB approach, it has lower quality switching
times but some how experiences a higher number of
rebuffering instances. Its performance is comparable
to other methods with respect to rebuffering durations
and inter-starvation lengths. On the other hand, DQN
performs well with respect to number of rebuffering
times and has a quite large inter-starvation length. It
how ever has a high variance in the quality switching
times, which may indicate its inability to generalize
well under different environments.
By analyzing the various indicators, it is noted
that when using the DQNReg approach, the number
of rebuffering times, the rebuffering duration and the
quality switching times are suppressed to the lowest,
while the quality switching times and inter-starvation
lengths are maintained at a level comparable to other
methods. Under various mobility patterns of real-time
network, the average QoE performance of DQNReg
is still superior to other methods. This indicates that
the trained DQNReg learning agent has strong gen-
eralization ability and can ﬂexibly adapt to various
network conditions, so that the video service quality
can match the network communication quality as well
as possible.
6 Conclusions
With increased user expectations and demands for
uninterrupted viewing and top video quality, stud-
ies concluded that users will leave video sessions
if the quality is not adequate, harming the revenues
of content providers. Considering the intricate web-
based video delivery ecosystem and its various bot-
tlenecks, adaptive bitrate algorithms become essential
to content providers to optimize video quality. This
thesis proposed utilizing DQNReg, a reinforcement
learning based technique that enhances the classical
deep Q-learning method approach for video adapta-
tion. A segment-wise QoE-based reward function is
established so that the learning strategy can converge
towards maximizing the QoE outcome. DQNReg have
been thoroughly evaluated using trace-based simula-
tion for ﬁxed and mobile networks. The DQNReg-
based method outperforms classical DQN algorithm
and other traditional adaptation approaches. Future
research can integrate the initial start-up delay and the
impact of latency onto the learning-based method, so
that the learned policy can be improved with respect
to the QoE.
References
[1] D. Raca, D. Leahy, C. J. Sreenan, and J. J. Quin-
lan, Beyond Throughput, the Next Generation:
A 5G Dataset with Channel and Context Met-
rics, Proceedings of the 11th ACM Multimedia
Systems Conference, 2020, p. 303–308.
[2] Ericsson 2018 mobility report. Available [online]:
www.ericsson.com
[3] X. Yin, A. Jindal, A. Sekar, and B. Sinopoli, A
control-theoretic approach for dynamic adaptive
video streaming over HTTP, ACM Conference on
SIGCOMM, 2015.
[4] M. J. Khan, S. Harous, and A. Bentaleb, Client-
driven adaptive bitrate techniques for media
streaming over HTTP: Initial ﬁndings, 2020 IEEE
International Conference on Electro Information
Technology (EIT), 2020, pp. 053–059.
[5] H. Yuan, S. Zhao, J. Hou, X. Wei, and S. Kwong,
Spatial and temporal consistency-aware dynamic
adaptive streaming for 360-degree videos, IEEE
Journal of Selected Topics in Signal Processing,
vol.14, no. 1, pp. 177-193, Jan. 2020.
[6] H. Yuan, X. Hu, J. Hou, X. Wei, and S.
Kwong, An ensemble rate adaptation framework
for dynamic adaptive streaming over HTTP, IEEE
Transactions on Broadcasting, vol. 66, no. 2, pp.
251-263, Jun. 2020.
[7] A. Bentaleb, B. Taani, A. C. Begen, C. Timmerer,
and R. Zimmermann, A survey on bitrate adap-
tation schemes for streaming media over HTTP,
```


### Pagina 13
```text
Springer LATEX template
IEEE Communications Surveys Tutorials, vol. 21,
no. 1, pp. 562–585, 2019.
[8] T.-Y. Huang, R. Johari, N. McKeown, M. Trun-
nell, and M. Watson, A buffer-based approach
to rate adaptation: Evidence from a large video
streaming service, Proceedings of the 2014 ACM
Conference on SIGCOMM, 2014, p. 187–198.
[9] Y. Zhou, Y. Duan, J. Sun, and Z. Guo, Towards
simple and smooth rate adaption for VBR video
in DASH, 2014 IEEE Visual Communications and
Image Processing Conference, pp. 9–12, 2014.
[10] L. De Cicco, S. Mascolo, and V. Palmisano,
Feedback control for adaptive live video stream-
ing, Proceedings of the Second Annual ACM
Conference on Multimedia Systems, 2011, p.
145–156.
[11] B. Wang, X. Luo, P. Hu, and F. Ren, Improving
optimization-based rate adaptation in DASH sys-
tem, 2017 26th International Conference on Com-
puter Communication and Networks (ICCCN),
2017, pp. 1–9.
[12] T.-Y. Huang, R. Johari, N. McKeown, M. Trun-
nell, and M. Watson, A buffer-based approach
to rate adaptation: Evidence from a large video
streaming service, SIGCOMM Comput. Com-
mun. Rev., vol. 44, no. 4, p. 187–198, Aug. 2014.
[13] R. K. P. Mok, X. Luo, E. W. W. Chan, and
R. K. C. Chang, QDASH: A QoE-aware DASH
System, Proceedings of the 3rd Multimedia Sys-
tems Conference, 2012, p. 11–22.
[14] L. Yu, T. Tillo, and J. Xiao, QoE-Driven
Dynamic Adaptive Video Streaming Strategy
With Future Information, IEEE Transactions on
Broadcasting, vol. 63, no. 3, pp. 523–534, Sept
2017.
[15] Y.-L. Chien, K. C.-J. Lin, and M.-S. Chen,
Machine learning based rate adaptation with elas-
tic feature selection for HTTP-based streaming,
ICME, IEEE Computer Society, 2015, pp. 1–6.
[16] H. Mao, R. Netravali, and M. Alizadeh, Neu-
ral adaptive video streaming with Pensieve, ACM
Conference on SIGCOMM, 2017.
[17] M.
Claeys,
S.
Latr´e,
J.
Famaey,
T.
Wu,
W. Van Leekwijck, and F. De Turck, Design of
a Q-learning-based client quality selection algo-
rithm for HTTP adaptive video streaming, Pro-
ceedings of Adaptive and Learning Agents Work-
shop, 2013, pp. 30–37.
[18] H. Lin, Z. Shen, H. Zhou, X. Liu, L. Zhang,
G. Xiao, and Z. Cheng, KNN-Q learning algo-
rithm of bitrate adaptation for video streaming
over HTTP, 2020 Information Communication
Technologies Conference (ICTC), 2020, pp. 302–
306.
[19] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao,
and L. Sun, Comyco: Quality-aware adaptive
video streaming via imitation learning, Proceed-
ings of the 27th ACM International Conference on
Multimedia, 2019, p. 429–437.
[20] F.
Chiariotti,
S.
D’Aronco,
L.
Toni,
and
P. Frossard, Online learning adaptation strategy
for DASH clients, Proceedings of the 7th Interna-
tional Conference on Multimedia Systems, 2016.
[21] M. Gadaleta, F. Chiariotti, M. Rossi, and
A. Zanella, D-DASH: A deep Q-learning frame-
work for DASH video streaming, IEEE Trans-
actions on Cognitive Communications and Net-
working, vol. 3, no. 4, pp. 703–718, 2017.
[22] J. Liu, X. Tao, and J. Lu, QoE-Oriented Rate
Adaptation for DASH With Enhanced Deep Q-
Learning, IEEE Access, vol. 7, pp. 8454–8469,
2019.
[23] J. D. Co-Reyes, Y. Miao, D. Peng, E. Real, Q. V.
Le, S. Levine, H. Lee, and A. Faust, Evolving
reinforcement learning algorithms, International
Conference on Learning Representations, 2021.
[24] Big Buck Bunny video. Available [online]:
download.blender.org/demo/movies/BBB.
[25] J. J. Quinlan and C. J. Sreenan, Multi-proﬁle
ultra high deﬁnition (UHD) AVC and HEVC
4k DASH datasets, Proceedings of the 9th
ACM Multimedia Systems Conference, 2018, p.
375–380.
```


### Pagina 14
```text
Springer LATEX template
13
[26] WLAN Throughput Project, Available: [online]:
https://data.world/engrasifkhan/wlan-
throughput/workspacef.
[27] G-NetTrack Pro user manual. Available [online]:
https://gyokovsolutions.com/manual-g-nettrack
[28] J. Jiang, V. Sekar, and H. Zhang, Improving
fairness, efﬁciency, and stability in HTTP-based
adaptive video streaming with festive, IEEE/ACM
Transactions on Networking, vol. 22, no. 01, pp.
326–340, jan. 2014.
[29] N. A. Hafez, M. S. Hassan, T. Landolsi,
Reformed QoE Based Approach in Bitrate-
Adaptation for Dynamic Adaptive Streaming Sys-
tems, To appear in the International Journal of
Interdisciplinary Telecommunications and Net-
working, Volume 14, Issue 1, 2022.
[30] J. Arora, Introduction to Optimum Design. Aca-
demic Press, 2017.
[31] H. Mukhtar, M. Hassan, and T. Landolsi, An
occupancy-based and channel-aware multi-level
adaptive scheme for video communications over
wireless channels, EURASIP Journal on Wireless
Communications and Networking, vol. 2011, 12
2011.
[32] B. Wang, X. Luo, P. Hu, and F. Ren, Improving
optimization-based rate adaptation in DASH sys-
tem, 2017 26th International Conference on Com-
puter Communication and Networks (ICCCN),
2017, pp. 1–9.
[33] N. Bouten, S. Latr´e, J. Famaey, W. Van Leekwi-
jck, and F. De Turck, In-network quality optimiza-
tion for adaptive video streaming services, IEEE
Transactions on Multimedia, vol. 16, no. 8, pp.
2281–2293, 2014.
```
