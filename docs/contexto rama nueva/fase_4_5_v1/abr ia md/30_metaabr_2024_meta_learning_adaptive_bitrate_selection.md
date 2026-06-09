# MetaABR: A Meta-Learning Approach on Adaptative Bitrate Selection for Video Streaming

## 0. Ficha de archivo

- Archivo fuente: `MetaABR_A_Meta-Learning_Approach_on_Adaptative_Bitrate_Selection_for_Video_Streaming.pdf`
- Paginas detectadas: 16
- SHA256 PDF: `27f3f5fa539f621c51b2b9e7fd56425b7f92400976e45a677d8c48cf44b2e0cf`
- Texto crudo auxiliar: `raw_text/30_metaabr_2024_meta_learning_adaptive_bitrate_selection.txt`
- Texto layout auxiliar: `raw_text_layout/30_metaabr_2024_meta_learning_adaptive_bitrate_selection_layout.txt`
- Fecha de generacion: 2026-06-09T12:33:34

## 1. Uso previsto para Fase 4-5 v1

Fuente para meta-learning ABR y adaptacion a condiciones/personalizacion QoE. Relevante por generalizacion, task split, emulacion y testbed; principalmente aporta criterios de robustez y limites de train/test ingenuo.

> Nota de fidelidad: este Markdown es una extraccion tecnica densa para Codex. No es un resumen narrativo ni sustituye al PDF. Para formulas, tablas y figuras criticas, revisar siempre el PDF original.

---

## 2. Identificacion textual de primeras paginas

```text
2422
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024
MetaABR: A Meta-Learning Approach on
Adaptative Bitrate Selection for Video Streaming
Wenzhong Li
, Member, IEEE, Xiang Li, Yeting Xu, Yi Yang, and Sanglu Lu
, Member, IEEE
Abstract—Video streaming is one of the most popular Internet
applications that makes up a large amount of Internet trafﬁc. A
fundamental mechanism in video streaming is adaptive bitrate
(ABR) selection which decides the proper compression level for
each chunk of a video to optimize the users’ quality of experience
(QoE). The existing ABR algorithms require signiﬁcant tuning and
do not generalize to diverse network conditions and personalized
QoE objectives. In this article, we propose a novel framework
for meta-learning based ABR design and discuss challenges of
deploying learning based ABR mechanism in real-world video
streaming systems. We utilize the proposed framework to design
MetaABR, a novel adaptive bitrate selection algorithm based on
meta-reinforcement learning to maximize users’ QoE. By jointly
training multiple learning tasks with a shared meta-critic, it can
provide transferrable meta-knowledge to supervise bitrate selec-
tion across tasks, and can be applied to efﬁciently learn a new
task in unseen environment with only a few trials. We imple-
ment MetaABR on an emulation platform which connects to the
Linux network protocol stack through virtual network interfaces.
Extensive experiments based on real-world traces and wireless
testbed show that MetaABR achieves the best comprehensive QoE
compared with the state-of-the-art ABR algorithms in a variety of
network environments.
Index Terms—Bitrate adaptation, meta-learning, reinforcement
learning, video streaming.
I. INTRODUCTION
R
ECENT years have witnessed a rapid growth of Internet
video streaming applications. Video on demand (VoD) ser-
vices have stimulated a revolution in video content consumption
by providing audiences a platform to watch whatever they want
anytime. According to the report,1 the global video streaming
market size was valued at USD 70.59 billion in 2022, and is
expected to expand at a compound annual growth rate (CAGR)
Manuscriptreceived7May2022;revised26February2023;accepted7March
2023. Date of publication 21 March 2023; date of current version 5 February
2024. This work was partially supported by the Natural Science Foundation of
Jiangsu Province Project “Research on Frontier Basic Theory and Method of
Security Defense for Power Systems with High-dimensional Uncertain Factors”
under Grant BK20222003, in part by the National Natural Science Foundation of
China Grants 61972196, 61832008, and 61832005, in part by the Collaborative
Innovation Center of Novel Software Technology and Industrialization, and the
Sino-German Institutes of Social Computing. Recommended for acceptance by
G. Xylomenos. (Corresponding author: Wenzhong Li.)
The authors are with the State Key Laboratory for Novel Software
Technology, Nanjing University, Nanjing, Jiangsu 210093, China (e-mail:
lwz@nju.edu.cn;
mf1933051@smail.nju.edu.cn;
mf20330097@smail.nju.
edu.cn; 171860540@smail.nju.edu.cn; sanglu@nju.edu.cn).
Digital Object Identiﬁer 10.1109/TMC.2023.3260086
1https://www.grandviewresearch.com/industry-analysis/video-streaming-
market
of 21.3% from 2022 to 2030. The study from Ericsson2 reported
that video streaming currently stands out as the most signiﬁcant
trafﬁc type consumed by smartphone users, and it is projected to
account for 74 percent of Internet trafﬁc by the end of 2024. The
fundamental design of a media streaming system pays increasing
attention to guarantee the users’ Quality of Experience (QoE).
It was showed [1] that users started to abandon a video if it took
more than 2 seconds to start up, with each incremental delay of
1 s resulting in a 5.8% increase in the abandonment rate, and
a moderate amount of interruptions can decrease the average
play time of a viewer by a signiﬁcant amount. Therefore, it is
important for content providers to provide high-quality ﬂuent
video streaming service to their users.
Dynamic Adaptive Streaming over HTTP (DASH) [2] is
the predominant form of video delivery in Internet. In DASH
systems, videos are stored on servers as multiple chunks, each
of which is encoded at several discrete bitrates, where a higher
bitrate implies a higher quality and a longer download time.
Adaptive bitrate (ABR) selection is the fundamental logic in
video streaming that runs on the client-side video players and
dynamically choose a bitrate for each video chunk to optimize
users’ QoE. Selecting the right bitrate in dynamic network is
challenging due to the variability of network conditions and the
trade-off of conﬂicting video QoE requirements [3], [4], [5].
Conventional ABR algorithms adopted a model-based ap-
proach that used mathematical models to describe network
conditions and made bitrate decisions based on the estimation
of network throughput [6], [7], [8], [9], [10] and playback
buffer occupancy [11], [12]. For example, FESTIVE [8] used
the harmonic mean of download speed over recent chunks to
predict the throughput and proposed a stateful bitrate selection
to compensate for the biased interaction between bitrate and
estimated bandwidth. BBA [11] was a buffer-based approach
which selected bitrates based on playback buffer occupation and
estimation of future capacity from past observations. MPC [13]
developed a model predictive control algorithm that combined
both throughput estimates and buffer occupancy information
to select bitrates to maximize QoE over a horizon of several
future chunks. However, model-based ABR algorithms failed
to achieve optimal performance across a broad set of network
conditions and QoE objectives due to their ﬁxed control rules.
In recent years, learning-based ABR algorithms [4], [5],
[14], [15], [16] were proposed to address the issues of bitrate
2https://www.ericsson.com/en/reports-and-papers/mobility-report/articles/
streaming-video
1536-1233 © 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore.  Restrictions apply.
LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING
2423
Fig. 1.
Performance of a pre-trained DRL agent (Pensieve [5] trained on 3G
dataset) testing on different network environments (details are in Section V-C2).
adaptation in varying network conditions. CS2P [4] used a
data-driven approach to learn clusters of similar sessions and
a Hidden-Markov-Model (HMM) based midstream predictor to
model the stateful evolution of throughput. Fugu [16] adopted
a supervised learning approach from the server side to train a
probabilistic predictor of upcoming chunk transmission times
and used the prediction information to improve the control
```

## 3. Metadatos PDF detectados

```json
{
  "format": "PDF 1.4",
  "title": "MetaABR: A Meta-Learning Approach on Adaptative Bitrate Selection for Video Streaming",
  "author": "",
  "subject": "IEEE Transactions on Mobile Computing;2024;23;3;10.1109/TMC.2023.3260086",
  "keywords": "",
  "creator": "LaTeX with hyperref package",
  "producer": "Acrobat Distiller 11.0 (Windows); modified using iText® Core 7.2.4 (AGPL version) ©2000-2022 iText Group NV",
  "creationDate": "D:20240106105415+05'30'",
  "modDate": "D:20240204172635-05'00'",
  "trapped": "",
  "encryption": null
}
```

## 4. Mapa de secciones detectado

- p. 1: I. INTRODUCTION
- p. 3: II. RELATED WORK
- p. 3: A. ABR Schemes for Video Streaming
- p. 4: B. Meta-Learning
- p. 4: III. META-LEARNING BASED BITRATE ADAPTATION
- p. 4: MECHANISM
- p. 4: A. QoE Metrics
- p. 5: NOTATIONS
- p. 5: B. ABR as a Deep Reinforcement Learning Task
- p. 5: C. Solution With a Meta-Learning Framework
- p. 6: IV. TRAINING METHODS
- p. 6: A. Training the Meta-Critic
- p. 7: V. EXPERIMENTS
- p. 7: A. Experiment Setup
- p. 8: THE LAYER PARAMETERS OF METAABR
- p. 9: TABLE III
- p. 9: DATASETS STATISTICS
- p. 9: THE QOE METRICS CONSIDERED IN THE EVALUATION
- p. 9: B. Comparison With Baseline Algorithms
- p. 11: COMPARISON OF AVERAGE BITRATE (MBPS), REBUFFERING TIME (SECOND), VARIATIONS, AND THEIR CORRESPONDING QOE METRICS ON DIFFERENT NETWORK
- p. 11: C. Effectiveness of Meta-Critic Learning
- p. 12: COMPARISON OF QOE METRICS FOR TRANSFERRING A PRE-TRAINED MODEL TO UNSEEN NETWORK ENVIRONMENTS, WHERE METAABR(HYBRID) MEANS A
- p. 12: TABLE VII
- p. 12: MODEL ON 3G DATASET TO MULTIPLE NETWORK ENVIRONMENTS
- p. 13: D. Trade-Off Between QoE Metrics
- p. 13: E. Performance on Multi-Video Scenario
- p. 14: TABLE VIII
- p. 14: F. Performance on Real-World Scenarios
- p. 14: VI. CONCLUSION
- p. 15: REFERENCES

## 5. Figuras, tablas, algoritmos, ecuaciones o teoremas detectados

- p. 2: Fig. 1.
- p. 2: Fig.2.
- p. 2: Fig. 3.
- p. 2: Fig. 3. Assume there are a number of learning tasks that learn
- p. 5: TABLE I
- p. 6: Fig. 4.
- p. 7: Fig. 5.
- p. 8: TABLE II
- p. 9: TABLE III
- p. 9: Fig. 6.
- p. 9: TABLE IV
- p. 9: Table IV. In our experiments, we report the average QoE per
- p. 10: Fig. 7.
- p. 10: Fig. 8.
- p. 10: Fig. 9.
- p. 11: Fig. 10.
- p. 11: TABLE V
- p. 12: TABLE VI
- p. 12: Fig. 11.
- p. 12: Fig. 12.
- p. 12: TABLE VII
- p. 12: Fig. 13.
- p. 13: Fig. 14.
- p. 13: Fig. 15.
- p. 14: Fig. 16.
- p. 14: Fig. 17.
- p. 14: TABLE VIII

## 6. Lineas con posible contenido matematico/formal

Estas lineas NO son LaTeX verificado. Sirven para localizar formulas, objetivos, restricciones o pseudocodigo que hay que verificar en PDF.

- p. 5: `QoEv = μ1QoEv`
- p. 5: `where M = (μ1, μ2, μ3) is a set of non-negative weighting`
- p. 5: `st = (⃗xt, ⃗τt, ⃗nt, bt, ct, lt),`
- p. 5: `can denote the policy by πθ(st, at).`
- p. 5: `where γ ∈(0, 1] is a factor discounting future rewards.`
- p. 6: `t−k = (st−k, at−k, rt−k).`
- p. 7: `φ, ω ←arg min`
- p. 7: `t ) = Qφ(s(i)`
- p. 7: `= Aθ(i)(s(i)`
- p. 7: `θ(i) ←arg max`
- p. 8: `reward discount factor γ = 0.99 by default. The neural network`
- p. 9: `r QoEstd: q(Rn,v) = Rn, M = (1, 4.3, 1). This is the stan-`
- p. 9: `r QoEfluent: q(Rn,v) = Rn, M = (1, 8, 1). This metric`
- p. 9: `r QoEhd: M = (1, 8, 1). This metric favors high deﬁnition`

## 7. Extraccion tecnica por categorias


### 7.1. modelo ia arquitectura algoritmo

Palabras clave usadas: `model, models, neural, architecture, algorithm, policy, agent, actor, critic, actor-critic, DQN, deep Q, Q-learning, PPO, proximal policy, A3C, reinforcement, DRL, deep reinforcement, meta reinforcement, meta-RL, meta learning, MAML, Mamba, state space, SSM, LSTM, policy network, prediction model, Pensieve, SODA, DQNReg, MetaABR, MERINA, Oboe`

**Fragmento 1 - p. 6 - score 10:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2427 Fig. 4. Framework of MetaABR. algorithm [50] for deep reinforcement learning. A3C is a state- of-the-art DRL method that jointly trains a pair of actor-critic deep neural networks for any RL task so that the actor learns to solve the problem, and the critic learns to effectively supervise the actor by approximating its reward. Following the learning to learn method [50], [51], we adapt the A3C method for meta- learning by training a global meta-critic neural network based on cross-task knowledge to supervise multiple actor networks to solve speciﬁc problems. In this way, the shared meta-critic can provide transferable knowledge in training actors to gener- ate ABR policies for different network environments, and the experience of meta-critic can be learned by the actors on new problems with only a few trials to achieve adaptivity and fast convergence.

**Fragmento 2 - p. 6 - score 10:**

Noted that there are many meta-learning meth- ods such as MAML [34], MAESN [52], GrBAL/ReBAL [48], PEARL [53], etc., which we believe are also applicable to the proposed meta-learning framework for adaptive bitrate selec- tion. However, searching for the most efﬁcient meta-learning method for MetaABR is beyond the discussion of this article. The overall framework of MetaABR is illustrated in Fig. 4. It consists of a set of actor networks that learn to solve spe- ciﬁc tasks (e.g., learning an ABR algorithm for a particular network environment such as WiFi and 3G), and a global meta-critic network that learns how to effectively supervise the actors. Actor-critic is a well-known deep reinforcement learning method where an actor is a neural network used to select actions and a critic is another neural network used to learn a value function and update the actor’s policy parameters in a direction of performance improvement [50].

**Fragmento 3 - p. 4 - score 9:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2425 architectures including feedforward and recurrent deep neural networks to learn video adaptation strategies to achieved a good trade-off between policy optimality and convergence speed. Pensieve [5] proposed a Deep Reinforcement Learning (DRL) model that selected bitrates for future video chunks based on observations collected by DASH clients (i.e., throughput es- timation and buffer occupancy) across large video streaming experiments, which provided an expressive and scalable way to incorporate a rich variety of observations into the control policy. To address the issue of low sample efﬁciency of DRL, Comyco [15] trained an ABR policy via imitating expert tra- jectories to avoid redundant exploration.

**Fragmento 4 - p. 2 - score 8:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2423 Fig. 1. Performance of a pre-trained DRL agent (Pensieve [5] trained on 3G dataset) testing on different network environments (details are in Section V-C2). adaptation in varying network conditions. CS2P [4] used a data-driven approach to learn clusters of similar sessions and a Hidden-Markov-Model (HMM) based midstream predictor to model the stateful evolution of throughput. Fugu [16] adopted a supervised learning approach from the server side to train a probabilistic predictor of upcoming chunk transmission times and used the prediction information to improve the control policy of MPC. A few works [5], [14], [15], [17] applied Deep Reinforcement Learning (DRL) to train an agent to generate ABR policy by interacting with the environment.

**Fragmento 5 - p. 8 - score 8:**

3) Baseline Algorithms: We compare MetaABR with three state-of-the-art ABR algorithms: r BBA [11]: a buffer-based approach which selects bitrates based on playback buffer occupation. r RobustMPC [13]: a model predictive control algorithm that combines both throughput estimates and buffer occupancy information to select bitrates. r Pensieve [5]: a state-of-the-art ABR scheme based on deep reinforcement learning. r BayesMPC [58]: an uncertainty-aware robust ABR algo- rithm based on Bayesian neural network (BNN) and model predictive control (MPC). r Comyco [15]: a video quality-aware ABR approach lever- aging imitation learning to accelerate the training process for ABR tasks. Note that we do not compare with other deep learning based ABR algorithms such as Fugu [16], Oboe [23], and Stick [17], since either they are implemented on the server side, or there are lack of open-source code to reproduce their work.

**Fragmento 6 - p. 15 - score 8:**

364, no. 6443, pp. 859–865, 2019. [37] Z. Li, F. Zhou, F. Chen, and H. Li, “Meta-SGD: Learning to learn quickly for few-shot learning,” 2017, arXiv:1707.09835. [38] K. Young, B. Wang, and M. E. Taylor, “Metatrace actor-critic: Online step- size tuning by meta-gradient descent for reinforcement learning control,” 2018, arXiv:1805.04514. [39] N. Mishra, M. Rohaninejad, X. Chen, and P. Abbeel, “A simple neural attentive meta-learner,” 2017, arXiv:1707.03141. [40] Y. Duan, J. Schulman, X. Chen, P. L. Bartlett, I. Sutskever, and P. Abbeel, “RL2: Fast reinforcement learning via slow reinforcement learning,” 2016, arXiv:1611.02779. [41] J.Schulman,F.Wolski,P.Dhariwal,A.Radford,andO.Klimov,“Proximal policy optimization algorithms,” 2017, arXiv:1707.06347.

**Fragmento 7 - p. 2 - score 7:**

They did not rely on pre-programmed models or assumptions about the environment, and gradually learned the best policy for bitrate decisions through observation and experience. For example, Pensieve [5] is a state-of-the-art ABR scheme based on DRL. It represented its control policy as a neural network that mapped raw observations (e.g., throughput samples, playback buffer occupancy, video chunk sizes) to the bitrate decision for the next chunk, which provided an expressive and scalable way to incorporate a rich variety of observations into the ABR policy. Despite the ﬂexibility and effectiveness of the DRL-based ABR algorithms, there remain a number of challenges to de- ploy them in real-world video streaming systems.

**Fragmento 8 - p. 5 - score 7:**

In DRL, the agent uses a deep neural network (DNN) to represent the policy with a number of model parameters θ. Using θ, we can denote the policy by πθ(st, at). Reward: At each time step t, the agent observes some state st, and chooses an action at. After applying the action, the state of the environment transitions to st+1 and the agent receives a reward rt representing a comprehensive QoE metric. With the above formulation, the reinforcement learning task for bitrate adaptation can be described as follows. Reinforcement Learning Task for Bitrate Adaptation: Given a set of observed network states {s1, s2, · · · }, learn a deep neural network model that maps each state to an action (representing the bitrate selection policy): f(st) →at, in order to maximize the long-term expected cumulative discounted reward, i.e., E  ∞  t=0 γtrt  , (6) where γ ∈(0, 1] is a factor discounting future rewards.

**Fragmento 9 - p. 2 - score 6:**

(C1) Long bootstrap time: The DRL-based methods need to collect a large amount of training data by exploring various of actions in different network environments, which typically requires several hours(e.g.,8hoursreportedinPensieve[5])toformapre-trained neural network model. (C2) Lack of knowledge transfer: The existing DRL algorithms are typically task-speciﬁc and trained to work on a speciﬁc network environment independently, which are hard to deal with unseen scenarios. As an example, we adopt the Pensieve [5] algorithm to train a DRL agent on a 3G network, andthenapplytheagentforbitrateselectionondifferentnetwork conditions in Fig. 1. It is shown that the agent performs well on the working environment the same as the training network (see Fig.

**Fragmento 10 - p. 2 - score 6:**

1(a)), whereas it performs poorly on the WiFi and 4G networks, whose QoEs (see Fig. 1(b) and (c)) are close to or lower than that of simple model-based algorithms such as BBA [11] and RobustMPC [13]. (C3) Poor adaptivity: The existing DRL models trained for a client cannot be generalized to other clients even they operate on similar environments. As a result,itishardtotrainageneralizedmodeltocopewithdifferent network types even rich historical datasets are available. For example, we use an augmented hybrid dataset combining 3G, WiFi and 4G network traces to train a DRL model and apply Fig.2. PerformanceofPensieve[5]DRLagentstrainedwithdifferentdatasets, where Hybrid means the dataset combining 3G, WiFi and 4G traces (details are in Section V-C1).

**Fragmento 11 - p. 2 - score 6:**

Besides, because of its support of learning from fewer samples, it thus increases the speed of training pro- cess by limiting the necessary experiments. Finally, by learning multiple tasks, meta-learning can build more generalized models that adapt better to changing conditions. In the proposed framework, each DRL agent observes the network states including the client playback buffer occupancy, past bitrate decisions, and several raw network signals (e.g., throughput measurements), and feeds these values to its local model represented as a neural network. The client chooses a bitrate for the next video chunk based on these metrics, which Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 12 - p. 3 - score 6:**

As shown in Section V-C3, MetaABR trains a DRL agent much faster than regular DRL methods, whose convergence time is about 1/10 of that of Pensieve. Secondly, with the proposed meta-learning method, a DRL agent can be trained to learn transferable knowledge from historical tasks, which gains the ability to be applied in unseen environment. Meta-learning has the advantage of capturing the general knowledge across similar learning tasks in the past to improve the performance of learning new tasks to achieve knowledge transfer. As shown in Sec- tionV-C2,aMeteABRmodelcanbetrainedwiththe3Gnetwork trace and then applied to the WiFi and 4G networks, whose performance is still maintained and is better than the model- based ABR algorithms such as BBA and MPC.

**Fragmento 13 - p. 5 - score 6:**

B. ABR as a Deep Reinforcement Learning Task Adaptive bitrate selection for video streaming can be casted as a deep reinforcement learning (DRL) task: an agent learns by observing the states of the dynamic environment, and produces actions based on a neural network to select the proper bitrate to maximizetheexpectedlong-termQoE.Wediscussthefollowing basic elements of a DRL task. Agent: An agent is an entity in the system responsible for performing learning algorithm and making sequential decisions. In the ABR problem, at each time step, the agent is triggered to choose a bitrate for a chunk to be downloaded. State: A state of the system consists of a number of network performance measurements that are observed by the agent.

**Fragmento 14 - p. 15 - score 6:**

[42] F. Alet, M. F. Schneider, T. Lozano-Perez, and L. P. Kaelbling, “Meta- learning curiosity algorithms,” 2020, arXiv:2003.05325. [43] V. Veeriah et al., “Discovery of useful questions as auxiliary tasks,” 2019, arXiv:1909.04607. [44] Z. Zheng, J. Oh, and S. Singh, “On learning intrinsic rewards for policy gradient methods,” 2018, arXiv:1804.06459. [45] Z. Xu, H. van Hasselt, and D. Silver, “Meta-gradient reinforcement learn- ing,” 2018, arXiv:1805.09801. [46] K. Rakelly, A. Zhou, C. Finn, S. Levine, and D. Quillen, “Efﬁcient off- policy meta-reinforcement learning via probabilistic context variables,” in Proc. Int. Conf. Mach. Learn., 2019, pp. 5331–5340. [47] W. Zhou, Y. Li, Y. Yang, H. Wang, and T. M. Hospedales, “Online meta-critic learning for off-policy actor-critic methods,” 2020, arXiv: 2003.05334.

**Fragmento 15 - p. 2 - score 5:**

Fig. 3. Illustration of meta-critic based bitrate adaptation. it on different network environments in Fig. 2. As illustrated in Figs. 2(a) to (c), the model trained with multiple network traces does not improve adaptivity, and it performs even worse than those trained with a single network dataset. The poor adaptivity with mixture datasets is probably caused by dataset shift [18], [19]: the joint distribution of inputs and outputs differs between training and test stages. In our example, the DRL model trained to ﬁt data on a wide distribution (3G+WiFi+4G) and tested only on a relatively narrow distribution will result in a degradation of performance. In this article, we propose MetaABR, a novel ABR algorithm based on meta-learning to address the above challenges.

**Fragmento 16 - p. 3 - score 5:**

2424 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 results in a QoE metric observed and passed back to the DRL agent as a reward. The states and rewards of the tasks are passed to the meta-critic to train a meta model to supervise the agents to select suitable bitrates to maximize the QoE metric. By jointly training the DRL agents with the meta-critic, the shared meta- critic gains the ability to provide transferrable knowledge among past learning tasks, which can be applied to efﬁciently learn a new target task in unseen environment. Speciﬁcally, the proposec MetaABR can effectively address the above challenges (C1-C3) of video streaming systems. Firstly, MetaABR trains a general meta-model to teach the DRL agents to perform bitrate selection, which enables a new agent to be fastly trained on a target environment (without long bootstrap time).

**Fragmento 17 - p. 3 - score 5:**

The rest of the paper is organized as follows. Section II intro- duces the related works of media streaming bitrate adaptation methods and meta learning algorithms. Section III presents the detailed mechanism of bitrate adaptation based on meta learn- ing. Section IV proposes the training method for the proposed meta-critic and task-speciﬁc actors. Section V evaluates the system performance with extensive experiments. The paper is concluded in Section VI. II. RELATED WORK In this section, we introduce the related works in terms of ABR schemes for video streaming and meta learning. A. ABR Schemes for Video Streaming The ABR schemes for video streaming can be classiﬁed into two categories: the model-based and the learning-based methods.

**Fragmento 18 - p. 4 - score 5:**

Afewrecent works designed meta-RL generalizations for the conventional off-policy RL methods to accelerate the training and testing by replaying buffer samples from meta-training [46], [47]. It had been demonstrated that meta-RL was successfully applied in real-world physical robot [48], imitation learning [49], etc. III. META-LEARNING BASED BITRATE ADAPTATION MECHANISM In this section, we propose a meta-learning based bitrate adap- tation mechanism called MetaABR. We ﬁrst provide quantiﬁed description of QoE metrics, then formulate the ABR problem as a deep reinforcement learning task, which can be solved with a meta-reinforcement learning framework. The key notations used throughout the paper are summarized in Table I.

**Fragmento 19 - p. 5 - score 5:**

C. Solution With a Meta-Learning Framework As discussed in Section I, conventional deep reinforcement learning for ABR selection has the drawbacks of efﬁciency, generalization and robustness. To overcome the performance issues, we propose a novel meta reinforcement learning (MRL) based method called MetaABR for bitrate adaptation in video streaming. In the proposed framework, we apply the A3C Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 20 - p. 6 - score 5:**

When applying the meta- critic to learn a new task, from the perspective of the new task’s actor, it beneﬁts from a pre-trained meta-critic which increases learning speed and decreases required samples. The meta-critic based approach has a number of further bene- ﬁts. (1) It can address DRL tasks (i.e., training agents for differ- ent network environments) within a single framework, where the actors can beneﬁt from the meta-critic’s supervision of what it should do in those unlabelled states (unseen situations). (2) The proposed task-conﬁg and meta-critic networks can capture the correlation among diverse learning tasks from the past, and such history-dependent knowledge can be transferred to the learning of a new task, making the agent more capable of choosing the suitable policy to optimize rewards when being exposed to a new environment.

**Fragmento 21 - p. 7 - score 5:**

φ, ω ←arg min φ,ω M  i=1 (Pφ,ω(s(i) t , a(i) t , z(i) t ))2, Pφ,ω(s(i) t , a(i) t , z(i) t ) = Qφ(s(i) t , a(i) t , C(i) ω,t) −rt −γQφ(s(i) t+1, a(i) t+1, C(i) ω,t+1). (9) In the above equation, Pφ,ω() is the error between the esti- mated reward (the output of the critic network) and the actual reward, and the learning objective is to ﬁnd the optimal model parameters φ and ω that minimize the overall squared error. B. Training the Task-Speciﬁc Actors The actor networks Aθ(i), parameterised by θ(i), are a set of task-speciﬁc neural networks that are used by the agents to generate actions for ABR decision. The neural network structure of the actor networks is similar to that of the conﬁg network. The hidden layer formed by the convolutional layer and the fully connected layer in the actor networks have 128 neurons that apply the softmax function in the output layer.

**Fragmento 22 - p. 10 - score 5:**

Secondly, MetaABR is able to automatically learn suitable ABR policies with a shared meta-critic on Hybrid network environments, whereas the model-based ABR algorithms such as BBA and Robust MPC struggle to optimize for different environments and QoE objectives. Since the model-based al- gorithms employ ﬁxed control laws, they are not ﬂexible for optimizing for multiple QoE objectives with different ABR policies. For example, when network bandwidth is inadequate, the ABR algorithm should build the playback buffer as quickly aspossibleusingthelowestbitrate.Asillustratedbytheresultsin hybrid network, MetaABR is able to learn such a policy without expert involvement, while other algorithms have difﬁculty to optimize such long term strategies.

**Fragmento 23 - p. 11 - score 5:**

As illustrated in Table V, MetaABR(Hybrid) performs close or better than those models personally trained on speciﬁc networks. For example, MetaABR(Hybrid) outperforms MetaABR(WiFi) on the WiFi network, and outperforms MetaABR(4GSyd) on the 4G network, which generally achieves the best perfor- mance on all test datasets. On the other hand, conventional DRL method such as Pensieve has poor adaptivity, e.g., Pen- sieve(Hybrid) clearly performs much worse than Pensieve(3G) and Pensieve(WiFi) on the corresponding datasets. 2) Ability of Knowledge Transfer: We then test the ability of knowledge transfer. Similar to the experiments in Section V-B, we use the Hybrid dataset to pre-train a DRL model, and apply the model to unseen networks (i.e., 4GNY and 5G) to test its performance.

**Fragmento 24 - p. 13 - score 5:**

2434 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 Fig. 14. Performance of MetaABR with different percentages of trainset. Fig. 15. Trade-off between bitrate, rebuffering time and variance. 3) Convergence: We further show the training efﬁciency of MetaABR. Figs. 13(a) and (b) show the loss function and reward of training a Pensieve model, training a MetaABR model from scratch, and training a new task with a pre-trained meta-critic on 3G network. It is shown that MetaABR convergences more faster than that of Pensieve, whose loss approaches 0 after 50 epoches. The reward of MetaABR is signiﬁcantly higher than that of Pensieve, which means it learns a better policy of QoE optimization. It is noticed that learning a new task with MetaABR can converge within 20 epochs, while Pensieve takes about 200 epochs to converge.

**Fragmento 25 - p. 15 - score 5:**

Yang, and T. Ma, “Model-based adversarial meta- reinforcement learning,” in Proc. 34th Int. Conf. Neural Inf. Process. Syst., Red Hook, NY, USA: Curran Associates Inc. 2020, pp. 10161–10173. [23] Z. Akhtar et al., “Oboe: Auto-tuning video abr algorithms to network conditions,” in Proc. Conf. ACM Special Int. Group Data Commun., 2018, pp. 44–58. [24] M. Dasari, K. Kahatapitiya, S. R. Das, A. Balasubramanian, and D. Samaras, “Swift: Adaptive video streaming with layered neural codecs,” Proc. 19th USENIX Symp. Networked Syst. Des. Implementation, Renton, WA, USA: USENIX Association, 2022, pp. 103–118. [25] A. Zhang, C. Wang, B. Han, and F. Qian, “YuZu: Neural-enhanced vol- umetric video streaming,” in Proc. 19th USENIX Symp. Networked Syst.

**Fragmento 26 - p. 16 - score 5:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2437 [49] Y. Duan et al., “One-shot imitation learning,” in Proc. Int. Conf. Neural Inf. Process. Syst., 2017, pp. 1–12. [50] V. Mnih et al., “Asynchronous methods for deep reinforcement learning,” in Proc. 33rd Int. Conf. Int. Conf. Mach. Learn., 2016, pp. 1928–1937. [51] F. Sung, L. Zhang, T. Xiang, T. M. Hospedales, and Y. Yang, “Learning to learn: Meta-critic networks for sample efﬁcient learning,” 2017, arXiv:1706.09529. [52] A. Gupta, R. Mendonca, Y. Liu, P. Abbeel, and S. Levine, “Meta- reinforcement learning of structured exploration strategies,” in Proc. Int. Conf. Neural Inf. Process. Syst., 2018, pp. 1–10. [53] K. Rakelly, A.


### 7.2. estado inputs features observaciones

Palabras clave usadas: `state, states, input, inputs, feature, features, observation, observations, throughput, bandwidth, buffer, download time, download duration, chunk size, segment size, history, past, remaining, last bitrate, network condition, QoE objective, task, environment, session, forecast, prediction, representation`

**Fragmento 1 - p. 1 - score 8:**

Conventional ABR algorithms adopted a model-based ap- proach that used mathematical models to describe network conditions and made bitrate decisions based on the estimation of network throughput [6], [7], [8], [9], [10] and playback buffer occupancy [11], [12]. For example, FESTIVE [8] used the harmonic mean of download speed over recent chunks to predict the throughput and proposed a stateful bitrate selection to compensate for the biased interaction between bitrate and estimated bandwidth. BBA [11] was a buffer-based approach which selected bitrates based on playback buffer occupation and estimation of future capacity from past observations. MPC [13] developed a model predictive control algorithm that combined both throughput estimates and buffer occupancy information to select bitrates to maximize QoE over a horizon of several future chunks.

**Fragmento 2 - p. 3 - score 8:**

2) Learning-Based Methods: Since model-based algorithms failed to achieve optimal performance across a broad set of network conditions and QoE objectives because of their ﬁxed controlrules,thelearning-basedmethods[4],[5],[14],[15],[16] were proposed to learn personalized ABR strategies for various conditions. Based on the observation that video sessions sharing similar key features presented similar initial throughput values and dynamic patterns, the CS2P [4] method used a data-driven approach to learn clusters of similar sessions, and proposed a Hidden-Markov-Model (HMM) based midstream predictor to model the stateful evolution of throughput for bitrate adaptation. D-DASH [14] formulated the DASH video streaming problem within a Deep Q-learning framework, and used mixed learning Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 3 - p. 2 - score 7:**

They did not rely on pre-programmed models or assumptions about the environment, and gradually learned the best policy for bitrate decisions through observation and experience. For example, Pensieve [5] is a state-of-the-art ABR scheme based on DRL. It represented its control policy as a neural network that mapped raw observations (e.g., throughput samples, playback buffer occupancy, video chunk sizes) to the bitrate decision for the next chunk, which provided an expressive and scalable way to incorporate a rich variety of observations into the ABR policy. Despite the ﬂexibility and effectiveness of the DRL-based ABR algorithms, there remain a number of challenges to de- ploy them in real-world video streaming systems.

**Fragmento 4 - p. 5 - score 7:**

At time step t, the state used as input to the DRL agent is denoted by st = (⃗xt, ⃗τt, ⃗nt, bt, ct, lt), (5) where ⃗xt is the network throughput measurements for the past k video chunks; ⃗τt is the download time of the past k video chunks, which represents the time interval of the throughput measurements; ⃗nt is a vector of m available sizes for the next video chunk; bt is the current buffer level; ct is the number of chunks remaining in the video; and lt is the bitrate at which the last chunk was downloaded. Action: Upon observing a state st, the agent needs to take an action at to determine the downloading bitrate for the next video chunk. A video website typically encodes a video with different bitrate levels such as 240p, 480p, and 1080p, and the agent selects bitrate based on a policy learned by the model.

**Fragmento 5 - p. 2 - score 6:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2423 Fig. 1. Performance of a pre-trained DRL agent (Pensieve [5] trained on 3G dataset) testing on different network environments (details are in Section V-C2). adaptation in varying network conditions. CS2P [4] used a data-driven approach to learn clusters of similar sessions and a Hidden-Markov-Model (HMM) based midstream predictor to model the stateful evolution of throughput. Fugu [16] adopted a supervised learning approach from the server side to train a probabilistic predictor of upcoming chunk transmission times and used the prediction information to improve the control policy of MPC. A few works [5], [14], [15], [17] applied Deep Reinforcement Learning (DRL) to train an agent to generate ABR policy by interacting with the environment.

**Fragmento 6 - p. 2 - score 6:**

Besides, because of its support of learning from fewer samples, it thus increases the speed of training pro- cess by limiting the necessary experiments. Finally, by learning multiple tasks, meta-learning can build more generalized models that adapt better to changing conditions. In the proposed framework, each DRL agent observes the network states including the client playback buffer occupancy, past bitrate decisions, and several raw network signals (e.g., throughput measurements), and feeds these values to its local model represented as a neural network. The client chooses a bitrate for the next video chunk based on these metrics, which Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 7 - p. 6 - score 6:**

When applying the meta- critic to learn a new task, from the perspective of the new task’s actor, it beneﬁts from a pre-trained meta-critic which increases learning speed and decreases required samples. The meta-critic based approach has a number of further bene- ﬁts. (1) It can address DRL tasks (i.e., training agents for differ- ent network environments) within a single framework, where the actors can beneﬁt from the meta-critic’s supervision of what it should do in those unlabelled states (unseen situations). (2) The proposed task-conﬁg and meta-critic networks can capture the correlation among diverse learning tasks from the past, and such history-dependent knowledge can be transferred to the learning of a new task, making the agent more capable of choosing the suitable policy to optimize rewards when being exposed to a new environment.

**Fragmento 8 - p. 6 - score 6:**

To achieve this, the meta-critic is further divided into a task-conﬁg network and a critic network as shown in Fig. 4. The task-conﬁg network takes the past trails of a RL task represented by a trajectory of the state, action, and reward as input to learn historical experience, and it outputs a task-actor embedding z which represents the task-speciﬁc features. The critic network uses the current (state, action) and the task-actor embedding z from the task-conﬁg network as input to approximate the reward for a RL task, where z serves as the meta-knowledge to decide how to criticise the current actor on the speciﬁc task. The training details are given in Section IV. By jointly training the meta-critic with multiple actors, the meta-critic gains the ability to correctly criticise a new task based on the provided task-conﬁg network.

**Fragmento 9 - p. 3 - score 5:**

2424 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 results in a QoE metric observed and passed back to the DRL agent as a reward. The states and rewards of the tasks are passed to the meta-critic to train a meta model to supervise the agents to select suitable bitrates to maximize the QoE metric. By jointly training the DRL agents with the meta-critic, the shared meta- critic gains the ability to provide transferrable knowledge among past learning tasks, which can be applied to efﬁciently learn a new target task in unseen environment. Speciﬁcally, the proposec MetaABR can effectively address the above challenges (C1-C3) of video streaming systems. Firstly, MetaABR trains a general meta-model to teach the DRL agents to perform bitrate selection, which enables a new agent to be fastly trained on a target environment (without long bootstrap time).

**Fragmento 10 - p. 6 - score 5:**

The input layer is a concatenation of a fully-connected (FC) layer (to deal with numerical values) and a one-dimensional convolutional neural network (1D-CNN) layer (to deal with vec- tors). It follows by a fully-connected (FC) layer and a recurrent neural network (RNN) layer to produce a task-actor embedding z, which encodes the task-dependent features for meta-learning. Speciﬁcally, we model the task-actor encoder as a Long-Short Term Memory (LSTM) [56] whose input is a trajectory of past k trials each represented by a triplet Lt t−k = (st−k, at−k, rt−k). (7) Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 11 - p. 3 - score 4:**

1) Model-Based Methods: Model-based methods estab- lished mathematical models to describe network conditions and make ABR decisions based on the estimation of available network bandwidth and playback buffer occupancy. The Probe AND Adapt (PANDA) [6] method estimated the bottleneck bandwidth and tried to eliminate the ON-OFF steady state issue aswellasreducebitrateoscillationswhenmultipleclientsshared the same bottleneck link. The piStream [7] method was a video adaptation framework for DASH clients in LTE networks that enabled clients to estimate the available bandwidth based on a resource monitor module that acted as a physical-layer daemon. FESTIVE [8] contained a bandwidth estimator module, a bitrate selection and update method that tried to avoid unfairness of stateless bitrate selection by making the player stateful, and a randomized scheduler that incorporated the buffer size to sched- ule the download of the next segment.

**Fragmento 12 - p. 3 - score 4:**

However, throughput can vary widely over time and result in poor ABR performance. Therefore, BBA [11] adopted a buffer-based approach which picked a bitrate based on playback buffer occupation. However, it suffered from QoE degradation during long-term bandwidth ﬂuctuations. BOLA [12] was also a buffer-based algorithm, whichturnedtheABRproblemintoautility-maximizationprob- lemandsolveditbytheLyapunovfunction.MPC[13]developed a control-theoretic framework that allowed the understanding and exploration of the trade-offs between bandwidth-based and buffer-based adaptation algorithms under different network bandwidth variations. Oboe [23] auto-tuned the parameters of model-based ABR algorithms for different network conditions to improve the ABR’s performance.

**Fragmento 13 - p. 4 - score 4:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2425 architectures including feedforward and recurrent deep neural networks to learn video adaptation strategies to achieved a good trade-off between policy optimality and convergence speed. Pensieve [5] proposed a Deep Reinforcement Learning (DRL) model that selected bitrates for future video chunks based on observations collected by DASH clients (i.e., throughput es- timation and buffer occupancy) across large video streaming experiments, which provided an expressive and scalable way to incorporate a rich variety of observations into the control policy. To address the issue of low sample efﬁciency of DRL, Comyco [15] trained an ABR policy via imitating expert tra- jectories to avoid redundant exploration.

**Fragmento 14 - p. 5 - score 4:**

In DRL, the agent uses a deep neural network (DNN) to represent the policy with a number of model parameters θ. Using θ, we can denote the policy by πθ(st, at). Reward: At each time step t, the agent observes some state st, and chooses an action at. After applying the action, the state of the environment transitions to st+1 and the agent receives a reward rt representing a comprehensive QoE metric. With the above formulation, the reinforcement learning task for bitrate adaptation can be described as follows. Reinforcement Learning Task for Bitrate Adaptation: Given a set of observed network states {s1, s2, · · · }, learn a deep neural network model that maps each state to an action (representing the bitrate selection policy): f(st) →at, in order to maximize the long-term expected cumulative discounted reward, i.e., E  ∞  t=0 γtrt  , (6) where γ ∈(0, 1] is a factor discounting future rewards.

**Fragmento 15 - p. 5 - score 4:**

B. ABR as a Deep Reinforcement Learning Task Adaptive bitrate selection for video streaming can be casted as a deep reinforcement learning (DRL) task: an agent learns by observing the states of the dynamic environment, and produces actions based on a neural network to select the proper bitrate to maximizetheexpectedlong-termQoE.Wediscussthefollowing basic elements of a DRL task. Agent: An agent is an entity in the system responsible for performing learning algorithm and making sequential decisions. In the ABR problem, at each time step, the agent is triggered to choose a bitrate for a chunk to be downloaded. State: A state of the system consists of a number of network performance measurements that are observed by the agent.

**Fragmento 16 - p. 6 - score 4:**

IV. TRAINING METHODS In this section, we introduce the methods of training the meta- critic and the task-speciﬁc actors in detail. A. Training the Meta-Critic In the proposed framework, we want to train a single meta- critic that can criticise any actor to perform any task. This requires two generalisations (task and actor conditioning) com- pared to conventional critic networks that criticise a speciﬁc actor for a speciﬁc task. The structure of the meta-critic is illus- trated in Fig. 5, which consists of two subnetworks: a task-conﬁg network and a critic network. The task-conﬁg network Cω, parameterised by ω, has a three- layer neural network structure. It takes the past k trails of (state, action, reward) triplets as input to learn task-speciﬁc experience.

**Fragmento 17 - p. 7 - score 4:**

2428 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 Fig. 5. Structure of Meta-Critic. The output of the task-conﬁg network is a task-actor embed- ding zt that represents the task-dependent features, where zt = Cω  Lt t−k, Lt t−k+1, . . . , Lt t−1  . (8) The rational of using the proposed task-actor embedding as meta-knowledge to train a meta model are explained as follows. On the one hand, it encodes a sequence of state-action pairs (the choiceofactiondependsontheactor’sparameters),whichcanbe usedbythecritictocharacterizetheactor’spolicyitistocriticise. On the other hand, it encodes the observed rewards of each action, which enables the critic to capture the characterization of the task that the actor is solving.

**Fragmento 18 - p. 7 - score 4:**

The critic network Qφ, parameterised by φ, has similar structure as that of the task-conﬁg network, which is used to approximate the reward for reinforcement learning tasks. Apart from the state st and action at, it further takes the task-actor embedding z as input to learn an action-value function. We use Qφ(s(i) t , a(i) t , z(i) t ) to describe the expected return reward after actor i taking action a(i) t in state s(i) t with a task-actor embedding z(i) t . The meta-critic is shared across all tasks and actors, which is trained to help actors to ﬁnd strategies that are more suitable for the environment. Assuming there are M learning tasks, the update rules for the meta-critic model parameters are as follows.

**Fragmento 19 - p. 8 - score 4:**

3) Baseline Algorithms: We compare MetaABR with three state-of-the-art ABR algorithms: r BBA [11]: a buffer-based approach which selects bitrates based on playback buffer occupation. r RobustMPC [13]: a model predictive control algorithm that combines both throughput estimates and buffer occupancy information to select bitrates. r Pensieve [5]: a state-of-the-art ABR scheme based on deep reinforcement learning. r BayesMPC [58]: an uncertainty-aware robust ABR algo- rithm based on Bayesian neural network (BNN) and model predictive control (MPC). r Comyco [15]: a video quality-aware ABR approach lever- aging imitation learning to accelerate the training process for ABR tasks. Note that we do not compare with other deep learning based ABR algorithms such as Fugu [16], Oboe [23], and Stick [17], since either they are implemented on the server side, or there are lack of open-source code to reproduce their work.

**Fragmento 20 - p. 10 - score 4:**

Secondly, MetaABR is able to automatically learn suitable ABR policies with a shared meta-critic on Hybrid network environments, whereas the model-based ABR algorithms such as BBA and Robust MPC struggle to optimize for different environments and QoE objectives. Since the model-based al- gorithms employ ﬁxed control laws, they are not ﬂexible for optimizing for multiple QoE objectives with different ABR policies. For example, when network bandwidth is inadequate, the ABR algorithm should build the playback buffer as quickly aspossibleusingthelowestbitrate.Asillustratedbytheresultsin hybrid network, MetaABR is able to learn such a policy without expert involvement, while other algorithms have difﬁculty to optimize such long term strategies.

**Fragmento 21 - p. 2 - score 3:**

Fig. 3. Illustration of meta-critic based bitrate adaptation. it on different network environments in Fig. 2. As illustrated in Figs. 2(a) to (c), the model trained with multiple network traces does not improve adaptivity, and it performs even worse than those trained with a single network dataset. The poor adaptivity with mixture datasets is probably caused by dataset shift [18], [19]: the joint distribution of inputs and outputs differs between training and test stages. In our example, the DRL model trained to ﬁt data on a wide distribution (3G+WiFi+4G) and tested only on a relatively narrow distribution will result in a degradation of performance. In this article, we propose MetaABR, a novel ABR algorithm based on meta-learning to address the above challenges.

**Fragmento 22 - p. 2 - score 3:**

(C1) Long bootstrap time: The DRL-based methods need to collect a large amount of training data by exploring various of actions in different network environments, which typically requires several hours(e.g.,8hoursreportedinPensieve[5])toformapre-trained neural network model. (C2) Lack of knowledge transfer: The existing DRL algorithms are typically task-speciﬁc and trained to work on a speciﬁc network environment independently, which are hard to deal with unseen scenarios. As an example, we adopt the Pensieve [5] algorithm to train a DRL agent on a 3G network, andthenapplytheagentforbitrateselectionondifferentnetwork conditions in Fig. 1. It is shown that the agent performs well on the working environment the same as the training network (see Fig.

**Fragmento 23 - p. 2 - score 3:**

Meta- learning is a learning approach that uses the experience and meta-data from the past learning tasks to adapt quickly to new tasks. The basic idea of the proposed MetaABR is illustrated in Fig. 3. Assume there are a number of learning tasks that learn ABR policies on different network environments (e.g., WiFi, 4G and Ethernet). Unlike conventional DRL methods that train the tasks separatively, the meta-learning approach trains all the tasks jointly with a shared meta-critic module. The beneﬁts of training multiple tasks with a meta-learning approach are threefold [20], [21], [22]. Firstly, it can learn task-level meta experiences that help algorithms better adapt to new tasks with optimization of hyper parameters.

**Fragmento 24 - p. 3 - score 3:**

r We utilize the proposed framework to design MetaABR, a novel adaptive bitrate selection algorithm based on meta- learning to maximize users’ QoE. By jointly training mul- tiple learning tasks with a shared meta-critic, it has the ability to provide transferrable knowledge to supervise bitrate selection, and can be applied to efﬁciently learn a new task in unseen environment with much fewer data samples and trainng epoches. r We implement the proposed MetaABR based on an emula- tionplatformwhichconnectstotheLinuxnetworkprotocol stack through a virtual network interface to send real data packets for evaluation. Extensive experiments based on real-world traces show that MetaABR achieves the best comprehensive QoE compared with the state-of-the-art ABR algorithms in a variety of network environments.

**Fragmento 25 - p. 3 - score 3:**

As shown in Section V-C3, MetaABR trains a DRL agent much faster than regular DRL methods, whose convergence time is about 1/10 of that of Pensieve. Secondly, with the proposed meta-learning method, a DRL agent can be trained to learn transferable knowledge from historical tasks, which gains the ability to be applied in unseen environment. Meta-learning has the advantage of capturing the general knowledge across similar learning tasks in the past to improve the performance of learning new tasks to achieve knowledge transfer. As shown in Sec- tionV-C2,aMeteABRmodelcanbetrainedwiththe3Gnetwork trace and then applied to the WiFi and 4G networks, whose performance is still maintained and is better than the model- based ABR algorithms such as BBA and MPC.

**Fragmento 26 - p. 4 - score 3:**

Several meta-representations had been explored in RL including learning the initial conditions [34], [35], hyperparameters [36], step directions [37], and step sizes [38], which enabled meta learning to train a neural network with fewer environmental interactions [39], [40]. In addition to conventional RL that explored environment based on sampling random actions or hand-crafted heuris- tics [41], several meta-RL studies treated exploration strategy or curiosity function as meta-knowledge, and modeled their acquisition as a meta-learning problem to improve sample ef- ﬁciency [42]. A large number of meta-RL studies considered single-task setting, where loss, reward, and hyperparameters were took as meta-knowledge to train together with the base pol- icytoimproveasinglelearningtask[43], [44], [45].


### 7.3. accion decision abr salida

Palabras clave usadas: `action, actions, bitrate, bit rate, quality level, representation, decision, decisions, select, selection, adaptation, output, score, guidance, recommend, priority, policy output, controller, rate adaptation, quality`

**Fragmento 1 - p. 5 - score 7:**

B. ABR as a Deep Reinforcement Learning Task Adaptive bitrate selection for video streaming can be casted as a deep reinforcement learning (DRL) task: an agent learns by observing the states of the dynamic environment, and produces actions based on a neural network to select the proper bitrate to maximizetheexpectedlong-termQoE.Wediscussthefollowing basic elements of a DRL task. Agent: An agent is an entity in the system responsible for performing learning algorithm and making sequential decisions. In the ABR problem, at each time step, the agent is triggered to choose a bitrate for a chunk to be downloaded. State: A state of the system consists of a number of network performance measurements that are observed by the agent.

**Fragmento 2 - p. 1 - score 6:**

Conventional ABR algorithms adopted a model-based ap- proach that used mathematical models to describe network conditions and made bitrate decisions based on the estimation of network throughput [6], [7], [8], [9], [10] and playback buffer occupancy [11], [12]. For example, FESTIVE [8] used the harmonic mean of download speed over recent chunks to predict the throughput and proposed a stateful bitrate selection to compensate for the biased interaction between bitrate and estimated bandwidth. BBA [11] was a buffer-based approach which selected bitrates based on playback buffer occupation and estimation of future capacity from past observations. MPC [13] developed a model predictive control algorithm that combined both throughput estimates and buffer occupancy information to select bitrates to maximize QoE over a horizon of several future chunks.

**Fragmento 3 - p. 1 - score 6:**

2422 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 MetaABR: A Meta-Learning Approach on Adaptative Bitrate Selection for Video Streaming Wenzhong Li , Member, IEEE, Xiang Li, Yeting Xu, Yi Yang, and Sanglu Lu , Member, IEEE Abstract—Video streaming is one of the most popular Internet applications that makes up a large amount of Internet trafﬁc. A fundamental mechanism in video streaming is adaptive bitrate (ABR) selection which decides the proper compression level for each chunk of a video to optimize the users’ quality of experience (QoE). The existing ABR algorithms require signiﬁcant tuning and do not generalize to diverse network conditions and personalized QoE objectives.

**Fragmento 4 - p. 3 - score 6:**

1) Model-Based Methods: Model-based methods estab- lished mathematical models to describe network conditions and make ABR decisions based on the estimation of available network bandwidth and playback buffer occupancy. The Probe AND Adapt (PANDA) [6] method estimated the bottleneck bandwidth and tried to eliminate the ON-OFF steady state issue aswellasreducebitrateoscillationswhenmultipleclientsshared the same bottleneck link. The piStream [7] method was a video adaptation framework for DASH clients in LTE networks that enabled clients to estimate the available bandwidth based on a resource monitor module that acted as a physical-layer daemon. FESTIVE [8] contained a bandwidth estimator module, a bitrate selection and update method that tried to avoid unfairness of stateless bitrate selection by making the player stateful, and a randomized scheduler that incorporated the buffer size to sched- ule the download of the next segment.

**Fragmento 5 - p. 5 - score 6:**

In DRL, the agent uses a deep neural network (DNN) to represent the policy with a number of model parameters θ. Using θ, we can denote the policy by πθ(st, at). Reward: At each time step t, the agent observes some state st, and chooses an action at. After applying the action, the state of the environment transitions to st+1 and the agent receives a reward rt representing a comprehensive QoE metric. With the above formulation, the reinforcement learning task for bitrate adaptation can be described as follows. Reinforcement Learning Task for Bitrate Adaptation: Given a set of observed network states {s1, s2, · · · }, learn a deep neural network model that maps each state to an action (representing the bitrate selection policy): f(st) →at, in order to maximize the long-term expected cumulative discounted reward, i.e., E  ∞  t=0 γtrt  , (6) where γ ∈(0, 1] is a factor discounting future rewards.

**Fragmento 6 - p. 15 - score 6:**

2436 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 based ABR design. Based on the proposed framework, we proposed MetaABR, a novel adaptive bitrate selection algorithm based on meta-critic to maximize users’ QoE. MetaABR jointly trained multiple learning tasks with a shared meta-critic, and it could provide transferrable knowledge to supervise bitrate se- lection across tasks. Extensive experiments based on real-world traces and testbed showed that MetaABR achieved the best QoE compared with the state-of-the-arts. REFERENCES [1] S. Krishnan and R. Sitaraman, “Video stream quality impacts viewer be- havior: Inferring causality using quasi-experimental designs,” IEEE/ACM Trans. Netw., vol.

**Fragmento 7 - p. 2 - score 5:**

(C1) Long bootstrap time: The DRL-based methods need to collect a large amount of training data by exploring various of actions in different network environments, which typically requires several hours(e.g.,8hoursreportedinPensieve[5])toformapre-trained neural network model. (C2) Lack of knowledge transfer: The existing DRL algorithms are typically task-speciﬁc and trained to work on a speciﬁc network environment independently, which are hard to deal with unseen scenarios. As an example, we adopt the Pensieve [5] algorithm to train a DRL agent on a 3G network, andthenapplytheagentforbitrateselectionondifferentnetwork conditions in Fig. 1. It is shown that the agent performs well on the working environment the same as the training network (see Fig.

**Fragmento 8 - p. 3 - score 5:**

2424 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 results in a QoE metric observed and passed back to the DRL agent as a reward. The states and rewards of the tasks are passed to the meta-critic to train a meta model to supervise the agents to select suitable bitrates to maximize the QoE metric. By jointly training the DRL agents with the meta-critic, the shared meta- critic gains the ability to provide transferrable knowledge among past learning tasks, which can be applied to efﬁciently learn a new target task in unseen environment. Speciﬁcally, the proposec MetaABR can effectively address the above challenges (C1-C3) of video streaming systems. Firstly, MetaABR trains a general meta-model to teach the DRL agents to perform bitrate selection, which enables a new agent to be fastly trained on a target environment (without long bootstrap time).

**Fragmento 9 - p. 5 - score 5:**

2426 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 TABLE I NOTATIONS quality, minimizing rebuffering time, and maintaining video quality smoothness (i.e., avoiding constant bitrate ﬂuctuations). For a satisfactory user-perceived QoE, ABR algorithm needs to optimize several conﬂicting goals. For example, increasing the bitrate may lead to longer rebuffering time. There exists signiﬁcant variance in user preferences for video streaming QoE. To formulate the problem, we adopt the quantiﬁcation of QoE metrics as introduced in [13]. Speciﬁcally, users tend to prefer great average quality per chunk for high-deﬁnition content, which can be calculated on the mean of n-th chunk of video v by: QoEv hd = N  n=1 q(Rn,v), (1) where Rn,v is the bitrate of chunk n of video v, and q(·) is a non-decreasing function which maps the selected bitrate to the video quality perceived by user.

**Fragmento 10 - p. 5 - score 5:**

C. Solution With a Meta-Learning Framework As discussed in Section I, conventional deep reinforcement learning for ABR selection has the drawbacks of efﬁciency, generalization and robustness. To overcome the performance issues, we propose a novel meta reinforcement learning (MRL) based method called MetaABR for bitrate adaptation in video streaming. In the proposed framework, we apply the A3C Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 11 - p. 15 - score 5:**

21, pp. 2001–2014, Dec. 2013. [2] T. Stockhammer, “Dynamic adaptive streaming over HTTP: Standards and design principles,” in Proc. 2nd Annu. ACM Conf. Multimedia Syst., 2011, pp. 133–144. [3] T.-Y. Huang, N. Handigol, B. Heller, N. McKeown, and R. Johari, “Con- fused, timid, and unstable: Picking a video streaming rate is hard,” in Proc. Internet Meas. Conf., 2012, pp. 225–238. [4] Y. Sun et al., “CS2P: Improving video bitrate selection and adaptation with data-driven throughput prediction,” in Proc. ACM SIGCOMM Conf., 2016, pp. 272–285. [5] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video streaming with pensieve,” in Proc. Conf. ACM Special Int. Group Data Commun., 2017, pp. 197–210. [6] Z. Li et al., “Probe and adapt: Rate adaptation for HTTP video streaming at scale,” IEEE J.

**Fragmento 12 - p. 1 - score 4:**

Therefore, it is important for content providers to provide high-quality ﬂuent video streaming service to their users. Dynamic Adaptive Streaming over HTTP (DASH) [2] is the predominant form of video delivery in Internet. In DASH systems, videos are stored on servers as multiple chunks, each of which is encoded at several discrete bitrates, where a higher bitrate implies a higher quality and a longer download time. Adaptive bitrate (ABR) selection is the fundamental logic in video streaming that runs on the client-side video players and dynamically choose a bitrate for each video chunk to optimize users’ QoE. Selecting the right bitrate in dynamic network is challenging due to the variability of network conditions and the trade-off of conﬂicting video QoE requirements [3], [4], [5].

**Fragmento 13 - p. 2 - score 4:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2423 Fig. 1. Performance of a pre-trained DRL agent (Pensieve [5] trained on 3G dataset) testing on different network environments (details are in Section V-C2). adaptation in varying network conditions. CS2P [4] used a data-driven approach to learn clusters of similar sessions and a Hidden-Markov-Model (HMM) based midstream predictor to model the stateful evolution of throughput. Fugu [16] adopted a supervised learning approach from the server side to train a probabilistic predictor of upcoming chunk transmission times and used the prediction information to improve the control policy of MPC. A few works [5], [14], [15], [17] applied Deep Reinforcement Learning (DRL) to train an agent to generate ABR policy by interacting with the environment.

**Fragmento 14 - p. 2 - score 4:**

Fig. 3. Illustration of meta-critic based bitrate adaptation. it on different network environments in Fig. 2. As illustrated in Figs. 2(a) to (c), the model trained with multiple network traces does not improve adaptivity, and it performs even worse than those trained with a single network dataset. The poor adaptivity with mixture datasets is probably caused by dataset shift [18], [19]: the joint distribution of inputs and outputs differs between training and test stages. In our example, the DRL model trained to ﬁt data on a wide distribution (3G+WiFi+4G) and tested only on a relatively narrow distribution will result in a degradation of performance. In this article, we propose MetaABR, a novel ABR algorithm based on meta-learning to address the above challenges.

**Fragmento 15 - p. 4 - score 4:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2425 architectures including feedforward and recurrent deep neural networks to learn video adaptation strategies to achieved a good trade-off between policy optimality and convergence speed. Pensieve [5] proposed a Deep Reinforcement Learning (DRL) model that selected bitrates for future video chunks based on observations collected by DASH clients (i.e., throughput es- timation and buffer occupancy) across large video streaming experiments, which provided an expressive and scalable way to incorporate a rich variety of observations into the control policy. To address the issue of low sample efﬁciency of DRL, Comyco [15] trained an ABR policy via imitating expert tra- jectories to avoid redundant exploration.

**Fragmento 16 - p. 6 - score 4:**

Noted that there are many meta-learning meth- ods such as MAML [34], MAESN [52], GrBAL/ReBAL [48], PEARL [53], etc., which we believe are also applicable to the proposed meta-learning framework for adaptive bitrate selec- tion. However, searching for the most efﬁcient meta-learning method for MetaABR is beyond the discussion of this article. The overall framework of MetaABR is illustrated in Fig. 4. It consists of a set of actor networks that learn to solve spe- ciﬁc tasks (e.g., learning an ABR algorithm for a particular network environment such as WiFi and 3G), and a global meta-critic network that learns how to effectively supervise the actors. Actor-critic is a well-known deep reinforcement learning method where an actor is a neural network used to select actions and a critic is another neural network used to learn a value function and update the actor’s policy parameters in a direction of performance improvement [50].

**Fragmento 17 - p. 7 - score 4:**

φ, ω ←arg min φ,ω M  i=1 (Pφ,ω(s(i) t , a(i) t , z(i) t ))2, Pφ,ω(s(i) t , a(i) t , z(i) t ) = Qφ(s(i) t , a(i) t , C(i) ω,t) −rt −γQφ(s(i) t+1, a(i) t+1, C(i) ω,t+1). (9) In the above equation, Pφ,ω() is the error between the esti- mated reward (the output of the critic network) and the actual reward, and the learning objective is to ﬁnd the optimal model parameters φ and ω that minimize the overall squared error. B. Training the Task-Speciﬁc Actors The actor networks Aθ(i), parameterised by θ(i), are a set of task-speciﬁc neural networks that are used by the agents to generate actions for ABR decision. The neural network structure of the actor networks is similar to that of the conﬁg network. The hidden layer formed by the convolutional layer and the fully connected layer in the actor networks have 128 neurons that apply the softmax function in the output layer.

**Fragmento 18 - p. 8 - score 4:**

4) Video Parameters: We have modiﬁed dash.js3 to sup- port MetaABR and the above baseline ABR algorithms. For MetaABR, Pensieve, and RobustMPC, we conﬁgure dash.js to obtain the bitrate selection decision from an ABR process that implements the corresponding algorithm. The DASH player is conﬁgured to have a playback buffer capacity of 60 seconds. Our evaluation used the “Envivio-Dash3” video of the DASH-246 JavaScript reference client. In addition, the video is divided into 48 blocks with a total length of 193 seconds. This video is encoded by the H.264/MPEG-4 codec at bitrates in 300, 750, 1200,1850,2850,4300kbps(whichcorrespondstovideomodes in 240p, 360p, 480p, 720p, 1080p, 1440p). Therefore, each block represents approximately 4 seconds of video playback.

**Fragmento 19 - p. 1 - score 3:**

Extensive experiments based on real-world traces and wireless testbed show that MetaABR achieves the best comprehensive QoE compared with the state-of-the-art ABR algorithms in a variety of network environments. Index Terms—Bitrate adaptation, meta-learning, reinforcement learning, video streaming. I. INTRODUCTION R ECENT years have witnessed a rapid growth of Internet video streaming applications. Video on demand (VoD) ser- vices have stimulated a revolution in video content consumption by providing audiences a platform to watch whatever they want anytime. According to the report,1 the global video streaming market size was valued at USD 70.59 billion in 2022, and is expected to expand at a compound annual growth rate (CAGR) Manuscriptreceived7May2022;revised26February2023;accepted7March 2023.

**Fragmento 20 - p. 1 - score 3:**

In this article, we propose a novel framework for meta-learning based ABR design and discuss challenges of deploying learning based ABR mechanism in real-world video streaming systems. We utilize the proposed framework to design MetaABR, a novel adaptive bitrate selection algorithm based on meta-reinforcement learning to maximize users’ QoE. By jointly training multiple learning tasks with a shared meta-critic, it can provide transferrable meta-knowledge to supervise bitrate selec- tion across tasks, and can be applied to efﬁciently learn a new task in unseen environment with only a few trials. We imple- ment MetaABR on an emulation platform which connects to the Linux network protocol stack through virtual network interfaces.

**Fragmento 21 - p. 2 - score 3:**

They did not rely on pre-programmed models or assumptions about the environment, and gradually learned the best policy for bitrate decisions through observation and experience. For example, Pensieve [5] is a state-of-the-art ABR scheme based on DRL. It represented its control policy as a neural network that mapped raw observations (e.g., throughput samples, playback buffer occupancy, video chunk sizes) to the bitrate decision for the next chunk, which provided an expressive and scalable way to incorporate a rich variety of observations into the ABR policy. Despite the ﬂexibility and effectiveness of the DRL-based ABR algorithms, there remain a number of challenges to de- ploy them in real-world video streaming systems.

**Fragmento 22 - p. 2 - score 3:**

Besides, because of its support of learning from fewer samples, it thus increases the speed of training pro- cess by limiting the necessary experiments. Finally, by learning multiple tasks, meta-learning can build more generalized models that adapt better to changing conditions. In the proposed framework, each DRL agent observes the network states including the client playback buffer occupancy, past bitrate decisions, and several raw network signals (e.g., throughput measurements), and feeds these values to its local model represented as a neural network. The client chooses a bitrate for the next video chunk based on these metrics, which Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 23 - p. 3 - score 3:**

2) Learning-Based Methods: Since model-based algorithms failed to achieve optimal performance across a broad set of network conditions and QoE objectives because of their ﬁxed controlrules,thelearning-basedmethods[4],[5],[14],[15],[16] were proposed to learn personalized ABR strategies for various conditions. Based on the observation that video sessions sharing similar key features presented similar initial throughput values and dynamic patterns, the CS2P [4] method used a data-driven approach to learn clusters of similar sessions, and proposed a Hidden-Markov-Model (HMM) based midstream predictor to model the stateful evolution of throughput for bitrate adaptation. D-DASH [14] formulated the DASH video streaming problem within a Deep Q-learning framework, and used mixed learning Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 24 - p. 3 - score 3:**

r We utilize the proposed framework to design MetaABR, a novel adaptive bitrate selection algorithm based on meta- learning to maximize users’ QoE. By jointly training mul- tiple learning tasks with a shared meta-critic, it has the ability to provide transferrable knowledge to supervise bitrate selection, and can be applied to efﬁciently learn a new task in unseen environment with much fewer data samples and trainng epoches. r We implement the proposed MetaABR based on an emula- tionplatformwhichconnectstotheLinuxnetworkprotocol stack through a virtual network interface to send real data packets for evaluation. Extensive experiments based on real-world traces show that MetaABR achieves the best comprehensive QoE compared with the state-of-the-art ABR algorithms in a variety of network environments.

**Fragmento 25 - p. 3 - score 3:**

Thirdly, since the meta-model is typically trained with multiple datasets from different network environments, the historical experiences can be learned by the meta-model, which can be used to supervise the training of a general agent to adapt to various environments. As shown in Section V-C1, the DRL model of MeteABR trained with a combined dataset (3G+WiFi+4G traces) clearly beats the other DRL models trained with a single dataset. The contribution of our work are summarized as follows. r We formulate a novel framework for meta-learning based adaptive bitrate selection design. We discuss the challenges of deploying DRL-based ABR mechanism in real-world video streaming systems, which are not trivial to address within conventional DRL formalism.

**Fragmento 26 - p. 3 - score 3:**

The rest of the paper is organized as follows. Section II intro- duces the related works of media streaming bitrate adaptation methods and meta learning algorithms. Section III presents the detailed mechanism of bitrate adaptation based on meta learn- ing. Section IV proposes the training method for the proposed meta-critic and task-speciﬁc actors. Section V evaluates the system performance with extensive experiments. The paper is concluded in Section VI. II. RELATED WORK In this section, we introduce the related works in terms of ABR schemes for video streaming and meta learning. A. ABR Schemes for Video Streaming The ABR schemes for video streaming can be classiﬁed into two categories: the model-based and the learning-based methods.


### 7.4. reward qoe objetivo loss

Palabras clave usadas: `reward, QoE, quality of experience, utility, objective, loss, rebuffer, stall, stalling, smoothness, switching, quality variation, bitrate smoothness, video quality, penalty, consistent, consistency, risk, tail, latency`

**Fragmento 1 - p. 5 - score 6:**

Meanwhile, we need to ensure a ﬂuent playback and minimize the rebuffering time of every chunk, which is computed by: QoEv reb = N  n=1 Tn,v, (2) where Tn,v is the rebuffering time that results from downloading chunk n at bitrate Rn,v. Besides, the streaming strategy should reduce sudden and fre- quent quality variations, which may impose negative experience for users. Variation of video quality is calculated by: QoEv var = N−1  n=1 |q(Rn+1,v) −q(Rn, v)|, (3) which penalizes changes in video quality to favor smoothness. Overall objective: The overall objective in a comprehensive QoE metric is a weighted sum of the three metrics on video v, which is deﬁned as QoEv = μ1QoEv hd −μ2QoEv reb −μ3QoEv var, (4) where M = (μ1, μ2, μ3) is a set of non-negative weighting parameters corresponding to users’ preference on the video quality, rebuffering time, and variation, respectively.

**Fragmento 2 - p. 5 - score 4:**

2426 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 TABLE I NOTATIONS quality, minimizing rebuffering time, and maintaining video quality smoothness (i.e., avoiding constant bitrate ﬂuctuations). For a satisfactory user-perceived QoE, ABR algorithm needs to optimize several conﬂicting goals. For example, increasing the bitrate may lead to longer rebuffering time. There exists signiﬁcant variance in user preferences for video streaming QoE. To formulate the problem, we adopt the quantiﬁcation of QoE metrics as introduced in [13]. Speciﬁcally, users tend to prefer great average quality per chunk for high-deﬁnition content, which can be calculated on the mean of n-th chunk of video v by: QoEv hd = N  n=1 q(Rn,v), (1) where Rn,v is the bitrate of chunk n of video v, and q(·) is a non-decreasing function which maps the selected bitrate to the video quality perceived by user.

**Fragmento 3 - p. 9 - score 4:**

r QoEstd: q(Rn,v) = Rn, M = (1, 4.3, 1). This is the stan- dard QoE metric that had been widely used in the state-of- the-art ABR systems such as MPC [64] and Pensieve [5]. r QoEfluent: q(Rn,v) = Rn, M = (1, 8, 1). This metric emphasizes the ﬂuency of the video. It uses a much higher penalty on rebuffering time to calculate the reward, which intends to provide more ﬂuent video streaming service to the user. r QoEhd: M = (1, 8, 1). This metric favors high deﬁnition (HD) video. It adopts a q(Rn,v) mapping that assigns qual- ity scores according to the bitrates as illustrated in Table IV, where HD bitrates have signiﬁcantly higher quality score than that of non-HD bitrates. The exact values of q(Rn,v) for the QoE are provided in Table IV.

**Fragmento 4 - p. 13 - score 4:**

2434 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 Fig. 14. Performance of MetaABR with different percentages of trainset. Fig. 15. Trade-off between bitrate, rebuffering time and variance. 3) Convergence: We further show the training efﬁciency of MetaABR. Figs. 13(a) and (b) show the loss function and reward of training a Pensieve model, training a MetaABR model from scratch, and training a new task with a pre-trained meta-critic on 3G network. It is shown that MetaABR convergences more faster than that of Pensieve, whose loss approaches 0 after 50 epoches. The reward of MetaABR is signiﬁcantly higher than that of Pensieve, which means it learns a better policy of QoE optimization. It is noticed that learning a new task with MetaABR can converge within 20 epochs, while Pensieve takes about 200 epochs to converge.

**Fragmento 5 - p. 1 - score 3:**

2422 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 MetaABR: A Meta-Learning Approach on Adaptative Bitrate Selection for Video Streaming Wenzhong Li , Member, IEEE, Xiang Li, Yeting Xu, Yi Yang, and Sanglu Lu , Member, IEEE Abstract—Video streaming is one of the most popular Internet applications that makes up a large amount of Internet trafﬁc. A fundamental mechanism in video streaming is adaptive bitrate (ABR) selection which decides the proper compression level for each chunk of a video to optimize the users’ quality of experience (QoE). The existing ABR algorithms require signiﬁcant tuning and do not generalize to diverse network conditions and personalized QoE objectives.

**Fragmento 6 - p. 1 - score 2:**

edu.cn; 171860540@smail.nju.edu.cn; sanglu@nju.edu.cn). Digital Object Identiﬁer 10.1109/TMC.2023.3260086 1https://www.grandviewresearch.com/industry-analysis/video-streaming- market of 21.3% from 2022 to 2030. The study from Ericsson2 reported that video streaming currently stands out as the most signiﬁcant trafﬁc type consumed by smartphone users, and it is projected to account for 74 percent of Internet trafﬁc by the end of 2024. The fundamental design of a media streaming system pays increasing attention to guarantee the users’ Quality of Experience (QoE). It was showed [1] that users started to abandon a video if it took more than 2 seconds to start up, with each incremental delay of 1 s resulting in a 5.8% increase in the abandonment rate, and a moderate amount of interruptions can decrease the average play time of a viewer by a signiﬁcant amount.

**Fragmento 7 - p. 1 - score 2:**

However, model-based ABR algorithms failed to achieve optimal performance across a broad set of network conditions and QoE objectives due to their ﬁxed control rules. In recent years, learning-based ABR algorithms [4], [5], [14], [15], [16] were proposed to address the issues of bitrate 2https://www.ericsson.com/en/reports-and-papers/mobility-report/articles/ streaming-video 1536-1233 © 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 8 - p. 2 - score 2:**

1(a)), whereas it performs poorly on the WiFi and 4G networks, whose QoEs (see Fig. 1(b) and (c)) are close to or lower than that of simple model-based algorithms such as BBA [11] and RobustMPC [13]. (C3) Poor adaptivity: The existing DRL models trained for a client cannot be generalized to other clients even they operate on similar environments. As a result,itishardtotrainageneralizedmodeltocopewithdifferent network types even rich historical datasets are available. For example, we use an augmented hybrid dataset combining 3G, WiFi and 4G network traces to train a DRL model and apply Fig.2. PerformanceofPensieve[5]DRLagentstrainedwithdifferentdatasets, where Hybrid means the dataset combining 3G, WiFi and 4G traces (details are in Section V-C1).

**Fragmento 9 - p. 3 - score 2:**

2424 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 results in a QoE metric observed and passed back to the DRL agent as a reward. The states and rewards of the tasks are passed to the meta-critic to train a meta model to supervise the agents to select suitable bitrates to maximize the QoE metric. By jointly training the DRL agents with the meta-critic, the shared meta- critic gains the ability to provide transferrable knowledge among past learning tasks, which can be applied to efﬁciently learn a new target task in unseen environment. Speciﬁcally, the proposec MetaABR can effectively address the above challenges (C1-C3) of video streaming systems. Firstly, MetaABR trains a general meta-model to teach the DRL agents to perform bitrate selection, which enables a new agent to be fastly trained on a target environment (without long bootstrap time).

**Fragmento 10 - p. 3 - score 2:**

2) Learning-Based Methods: Since model-based algorithms failed to achieve optimal performance across a broad set of network conditions and QoE objectives because of their ﬁxed controlrules,thelearning-basedmethods[4],[5],[14],[15],[16] were proposed to learn personalized ABR strategies for various conditions. Based on the observation that video sessions sharing similar key features presented similar initial throughput values and dynamic patterns, the CS2P [4] method used a data-driven approach to learn clusters of similar sessions, and proposed a Hidden-Markov-Model (HMM) based midstream predictor to model the stateful evolution of throughput for bitrate adaptation. D-DASH [14] formulated the DASH video streaming problem within a Deep Q-learning framework, and used mixed learning Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 11 - p. 3 - score 2:**

However, throughput can vary widely over time and result in poor ABR performance. Therefore, BBA [11] adopted a buffer-based approach which picked a bitrate based on playback buffer occupation. However, it suffered from QoE degradation during long-term bandwidth ﬂuctuations. BOLA [12] was also a buffer-based algorithm, whichturnedtheABRproblemintoautility-maximizationprob- lemandsolveditbytheLyapunovfunction.MPC[13]developed a control-theoretic framework that allowed the understanding and exploration of the trade-offs between bandwidth-based and buffer-based adaptation algorithms under different network bandwidth variations. Oboe [23] auto-tuned the parameters of model-based ABR algorithms for different network conditions to improve the ABR’s performance.

**Fragmento 12 - p. 4 - score 2:**

Several meta-representations had been explored in RL including learning the initial conditions [34], [35], hyperparameters [36], step directions [37], and step sizes [38], which enabled meta learning to train a neural network with fewer environmental interactions [39], [40]. In addition to conventional RL that explored environment based on sampling random actions or hand-crafted heuris- tics [41], several meta-RL studies treated exploration strategy or curiosity function as meta-knowledge, and modeled their acquisition as a meta-learning problem to improve sample ef- ﬁciency [42]. A large number of meta-RL studies considered single-task setting, where loss, reward, and hyperparameters were took as meta-knowledge to train together with the base pol- icytoimproveasinglelearningtask[43], [44], [45].

**Fragmento 13 - p. 4 - score 2:**

The details are introduced as follows. A. QoE Metrics Toimproveusers’experience,mediastreamingserviceshould consider a variety of QoE goals such as maximizing video Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 14 - p. 5 - score 2:**

In DRL, the agent uses a deep neural network (DNN) to represent the policy with a number of model parameters θ. Using θ, we can denote the policy by πθ(st, at). Reward: At each time step t, the agent observes some state st, and chooses an action at. After applying the action, the state of the environment transitions to st+1 and the agent receives a reward rt representing a comprehensive QoE metric. With the above formulation, the reinforcement learning task for bitrate adaptation can be described as follows. Reinforcement Learning Task for Bitrate Adaptation: Given a set of observed network states {s1, s2, · · · }, learn a deep neural network model that maps each state to an action (representing the bitrate selection policy): f(st) →at, in order to maximize the long-term expected cumulative discounted reward, i.e., E  ∞  t=0 γtrt  , (6) where γ ∈(0, 1] is a factor discounting future rewards.

**Fragmento 15 - p. 6 - score 2:**

To achieve this, the meta-critic is further divided into a task-conﬁg network and a critic network as shown in Fig. 4. The task-conﬁg network takes the past trails of a RL task represented by a trajectory of the state, action, and reward as input to learn historical experience, and it outputs a task-actor embedding z which represents the task-speciﬁc features. The critic network uses the current (state, action) and the task-actor embedding z from the task-conﬁg network as input to approximate the reward for a RL task, where z serves as the meta-knowledge to decide how to criticise the current actor on the speciﬁc task. The training details are given in Section IV. By jointly training the meta-critic with multiple actors, the meta-critic gains the ability to correctly criticise a new task based on the provided task-conﬁg network.

**Fragmento 16 - p. 6 - score 2:**

IV. TRAINING METHODS In this section, we introduce the methods of training the meta- critic and the task-speciﬁc actors in detail. A. Training the Meta-Critic In the proposed framework, we want to train a single meta- critic that can criticise any actor to perform any task. This requires two generalisations (task and actor conditioning) com- pared to conventional critic networks that criticise a speciﬁc actor for a speciﬁc task. The structure of the meta-critic is illus- trated in Fig. 5, which consists of two subnetworks: a task-conﬁg network and a critic network. The task-conﬁg network Cω, parameterised by ω, has a three- layer neural network structure. It takes the past k trails of (state, action, reward) triplets as input to learn task-speciﬁc experience.

**Fragmento 17 - p. 7 - score 2:**

φ, ω ←arg min φ,ω M  i=1 (Pφ,ω(s(i) t , a(i) t , z(i) t ))2, Pφ,ω(s(i) t , a(i) t , z(i) t ) = Qφ(s(i) t , a(i) t , C(i) ω,t) −rt −γQφ(s(i) t+1, a(i) t+1, C(i) ω,t+1). (9) In the above equation, Pφ,ω() is the error between the esti- mated reward (the output of the critic network) and the actual reward, and the learning objective is to ﬁnd the optimal model parameters φ and ω that minimize the overall squared error. B. Training the Task-Speciﬁc Actors The actor networks Aθ(i), parameterised by θ(i), are a set of task-speciﬁc neural networks that are used by the agents to generate actions for ABR decision. The neural network structure of the actor networks is similar to that of the conﬁg network. The hidden layer formed by the convolutional layer and the fully connected layer in the actor networks have 128 neurons that apply the softmax function in the output layer.

**Fragmento 18 - p. 7 - score 2:**

The actor network takes the state s(i) t as input, then outputs an action a(i) t , i.e., a(i) t = Aθ(i)(s(i) t ). After applying each ac- tion, the agent observes a reward for that chunk. The goal of each learning agent is to maximize the expected cumulative (discounted) reward that it receives from the network environ- ment in terms of a speciﬁc QoE metric. In other words, the actor network intends to maximize the discounted future reward Qφ(s(i) t , a(i) t , z(i) t ) that is the estimated value from the output of the meta-critic network. Therefore, the optimizer alternately updates the actor network with: θ(i) ←arg max θ(i) Qφ  s(i) t , Aθ(i)(s(i) t ), z(i) t  . (10) Intheaboveequation,multipleactorsaretrainedjointlytoﬁnd their optimal model parameters θ(i) to maximize the estimated reward based on the output of the meta-critic.

**Fragmento 19 - p. 7 - score 2:**

(3) How is the trade-off between different conﬂicting QoE metrics? We ﬁnd that MetaABR achieves a better trade-off between increasing bitrate and reducing rebuffering time and variation, which is more closer to the ideal situation compared to the baselines. A. Experiment Setup 1) Implementation: In our implementation of the MetaABR scheme, the task-conﬁg network Cω, the critic network Qφ, and the actor network Aθ are three-layer fully-connected neural networks that use rectiﬁed linear unit (ReLU) as the activa- tion function of each neuron. We train the neural networks on TensorFlow 1.13.1 using RMSPropOptimizer with learning rate 0.01 (Cω), 0.0001 (Qφ), and 0.001 (Aθ) accordingly. The Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 20 - p. 10 - score 2:**

Secondly, MetaABR is able to automatically learn suitable ABR policies with a shared meta-critic on Hybrid network environments, whereas the model-based ABR algorithms such as BBA and Robust MPC struggle to optimize for different environments and QoE objectives. Since the model-based al- gorithms employ ﬁxed control laws, they are not ﬂexible for optimizing for multiple QoE objectives with different ABR policies. For example, when network bandwidth is inadequate, the ABR algorithm should build the playback buffer as quickly aspossibleusingthelowestbitrate.Asillustratedbytheresultsin hybrid network, MetaABR is able to learn such a policy without expert involvement, while other algorithms have difﬁculty to optimize such long term strategies.

**Fragmento 21 - p. 11 - score 2:**

2432 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 Fig. 10. CDF of QoE metrics (Hybrid network). TABLE V COMPARISON OF AVERAGE BITRATE (MBPS), REBUFFERING TIME (SECOND), VARIATIONS, AND THEIR CORRESPONDING QOE METRICS ON DIFFERENT NETWORK ENVIRONMENTS, WHERE METAABR(HYBRID) MEANS A METAABR MODEL TRAINED WITH THE Hybrid DATASET, AND SO ARE THE REST C. Effectiveness of Meta-Critic Learning 1) Adaptivity: The major advantage of MetaABR is its adap- tivity on different network traces, which enables a machine learning ABR algorithm to learn once and be applied to any- where. With the proposed meta-learning method we can train a general model MetaABR(Hybrid) based on the Hybrid dataset and then apply it to the other networks without modiﬁcation.

**Fragmento 22 - p. 13 - score 2:**

4) Performance With Small Samples: Fig. 14 shows the re- sults of MetaABR with different percentages of training sam- ples. It is shown that even using only 10% of the total train dataset, MetaABR still has comparable performance with Pen- sieve with full dataset. D. Trade-Off Between QoE Metrics We study the trade-off between different conﬂicting QoE met- rics, and the normalized results are shown in Fig. 15. It is shown that RobustMPC achieves higher bitrate with larger rebuffering time and variation. Pensieve and BBA have modest bitrate and rebuffering time/variation. Compared to the other algorithms, MetaABR achieves the best trade-off between different QoE metrics, which is much more closer to the ideal situation.

**Fragmento 23 - p. 14 - score 2:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2435 Fig. 16. CDF of QoE metrics of multi-video scenario testing on WiFi network. Fig. 17. CDF of QoEstd metrics under real-world network scenarios. TABLE VIII COMPARISON OF AVERAGE BITRATE (MBPS), REBUFFERING TIME (SECOND), VARIATIONS, AND QoEstd METRIC ON REAL-WORLD SCENARIOS on a variety of QoE metrics, and signiﬁcant performance im- provement is found in the QoEfluent metric. The results suggest that MetaABR can be adapted to the multiple video streaming scenarios with diverse QoE properties. F. Performance on Real-World Scenarios Apartfromtrace-drivenexperiments,wedeploythecompared algorithms in a wireless network testbed to test the performance under real-world scenarios.

**Fragmento 24 - p. 1 - score 1:**

Conventional ABR algorithms adopted a model-based ap- proach that used mathematical models to describe network conditions and made bitrate decisions based on the estimation of network throughput [6], [7], [8], [9], [10] and playback buffer occupancy [11], [12]. For example, FESTIVE [8] used the harmonic mean of download speed over recent chunks to predict the throughput and proposed a stateful bitrate selection to compensate for the biased interaction between bitrate and estimated bandwidth. BBA [11] was a buffer-based approach which selected bitrates based on playback buffer occupation and estimation of future capacity from past observations. MPC [13] developed a model predictive control algorithm that combined both throughput estimates and buffer occupancy information to select bitrates to maximize QoE over a horizon of several future chunks.

**Fragmento 25 - p. 1 - score 1:**

Extensive experiments based on real-world traces and wireless testbed show that MetaABR achieves the best comprehensive QoE compared with the state-of-the-art ABR algorithms in a variety of network environments. Index Terms—Bitrate adaptation, meta-learning, reinforcement learning, video streaming. I. INTRODUCTION R ECENT years have witnessed a rapid growth of Internet video streaming applications. Video on demand (VoD) ser- vices have stimulated a revolution in video content consumption by providing audiences a platform to watch whatever they want anytime. According to the report,1 the global video streaming market size was valued at USD 70.59 billion in 2022, and is expected to expand at a compound annual growth rate (CAGR) Manuscriptreceived7May2022;revised26February2023;accepted7March 2023.

**Fragmento 26 - p. 1 - score 1:**

Therefore, it is important for content providers to provide high-quality ﬂuent video streaming service to their users. Dynamic Adaptive Streaming over HTTP (DASH) [2] is the predominant form of video delivery in Internet. In DASH systems, videos are stored on servers as multiple chunks, each of which is encoded at several discrete bitrates, where a higher bitrate implies a higher quality and a longer download time. Adaptive bitrate (ABR) selection is the fundamental logic in video streaming that runs on the client-side video players and dynamically choose a bitrate for each video chunk to optimize users’ QoE. Selecting the right bitrate in dynamic network is challenging due to the variability of network conditions and the trade-off of conﬂicting video QoE requirements [3], [4], [5].


### 7.5. entrenamiento optimizacion pipeline

Palabras clave usadas: `training, train, trained, episode, epoch, optimizer, learning rate, loss function, minibatch, clipped, probability ratio, experience, simulation, simulator, emulation, testbed, fine-tuning, pretrain, learning task, meta-training, adaptation, oracle, auto-tuning, offline, online`

**Fragmento 1 - p. 4 - score 5:**

Afewrecent works designed meta-RL generalizations for the conventional off-policy RL methods to accelerate the training and testing by replaying buffer samples from meta-training [46], [47]. It had been demonstrated that meta-RL was successfully applied in real-world physical robot [48], imitation learning [49], etc. III. META-LEARNING BASED BITRATE ADAPTATION MECHANISM In this section, we propose a meta-learning based bitrate adap- tation mechanism called MetaABR. We ﬁrst provide quantiﬁed description of QoE metrics, then formulate the ABR problem as a deep reinforcement learning task, which can be solved with a meta-reinforcement learning framework. The key notations used throughout the paper are summarized in Table I.

**Fragmento 2 - p. 13 - score 5:**

2434 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 Fig. 14. Performance of MetaABR with different percentages of trainset. Fig. 15. Trade-off between bitrate, rebuffering time and variance. 3) Convergence: We further show the training efﬁciency of MetaABR. Figs. 13(a) and (b) show the loss function and reward of training a Pensieve model, training a MetaABR model from scratch, and training a new task with a pre-trained meta-critic on 3G network. It is shown that MetaABR convergences more faster than that of Pensieve, whose loss approaches 0 after 50 epoches. The reward of MetaABR is signiﬁcantly higher than that of Pensieve, which means it learns a better policy of QoE optimization. It is noticed that learning a new task with MetaABR can converge within 20 epochs, while Pensieve takes about 200 epochs to converge.

**Fragmento 3 - p. 1 - score 4:**

In this article, we propose a novel framework for meta-learning based ABR design and discuss challenges of deploying learning based ABR mechanism in real-world video streaming systems. We utilize the proposed framework to design MetaABR, a novel adaptive bitrate selection algorithm based on meta-reinforcement learning to maximize users’ QoE. By jointly training multiple learning tasks with a shared meta-critic, it can provide transferrable meta-knowledge to supervise bitrate selec- tion across tasks, and can be applied to efﬁciently learn a new task in unseen environment with only a few trials. We imple- ment MetaABR on an emulation platform which connects to the Linux network protocol stack through virtual network interfaces.

**Fragmento 4 - p. 2 - score 4:**

Fig. 3. Illustration of meta-critic based bitrate adaptation. it on different network environments in Fig. 2. As illustrated in Figs. 2(a) to (c), the model trained with multiple network traces does not improve adaptivity, and it performs even worse than those trained with a single network dataset. The poor adaptivity with mixture datasets is probably caused by dataset shift [18], [19]: the joint distribution of inputs and outputs differs between training and test stages. In our example, the DRL model trained to ﬁt data on a wide distribution (3G+WiFi+4G) and tested only on a relatively narrow distribution will result in a degradation of performance. In this article, we propose MetaABR, a novel ABR algorithm based on meta-learning to address the above challenges.

**Fragmento 5 - p. 2 - score 4:**

Meta- learning is a learning approach that uses the experience and meta-data from the past learning tasks to adapt quickly to new tasks. The basic idea of the proposed MetaABR is illustrated in Fig. 3. Assume there are a number of learning tasks that learn ABR policies on different network environments (e.g., WiFi, 4G and Ethernet). Unlike conventional DRL methods that train the tasks separatively, the meta-learning approach trains all the tasks jointly with a shared meta-critic module. The beneﬁts of training multiple tasks with a meta-learning approach are threefold [20], [21], [22]. Firstly, it can learn task-level meta experiences that help algorithms better adapt to new tasks with optimization of hyper parameters.

**Fragmento 6 - p. 3 - score 4:**

2424 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 results in a QoE metric observed and passed back to the DRL agent as a reward. The states and rewards of the tasks are passed to the meta-critic to train a meta model to supervise the agents to select suitable bitrates to maximize the QoE metric. By jointly training the DRL agents with the meta-critic, the shared meta- critic gains the ability to provide transferrable knowledge among past learning tasks, which can be applied to efﬁciently learn a new target task in unseen environment. Speciﬁcally, the proposec MetaABR can effectively address the above challenges (C1-C3) of video streaming systems. Firstly, MetaABR trains a general meta-model to teach the DRL agents to perform bitrate selection, which enables a new agent to be fastly trained on a target environment (without long bootstrap time).

**Fragmento 7 - p. 3 - score 4:**

r We utilize the proposed framework to design MetaABR, a novel adaptive bitrate selection algorithm based on meta- learning to maximize users’ QoE. By jointly training mul- tiple learning tasks with a shared meta-critic, it has the ability to provide transferrable knowledge to supervise bitrate selection, and can be applied to efﬁciently learn a new task in unseen environment with much fewer data samples and trainng epoches. r We implement the proposed MetaABR based on an emula- tionplatformwhichconnectstotheLinuxnetworkprotocol stack through a virtual network interface to send real data packets for evaluation. Extensive experiments based on real-world traces show that MetaABR achieves the best comprehensive QoE compared with the state-of-the-art ABR algorithms in a variety of network environments.

**Fragmento 8 - p. 3 - score 4:**

Thirdly, since the meta-model is typically trained with multiple datasets from different network environments, the historical experiences can be learned by the meta-model, which can be used to supervise the training of a general agent to adapt to various environments. As shown in Section V-C1, the DRL model of MeteABR trained with a combined dataset (3G+WiFi+4G traces) clearly beats the other DRL models trained with a single dataset. The contribution of our work are summarized as follows. r We formulate a novel framework for meta-learning based adaptive bitrate selection design. We discuss the challenges of deploying DRL-based ABR mechanism in real-world video streaming systems, which are not trivial to address within conventional DRL formalism.

**Fragmento 9 - p. 6 - score 4:**

When applying the meta- critic to learn a new task, from the perspective of the new task’s actor, it beneﬁts from a pre-trained meta-critic which increases learning speed and decreases required samples. The meta-critic based approach has a number of further bene- ﬁts. (1) It can address DRL tasks (i.e., training agents for differ- ent network environments) within a single framework, where the actors can beneﬁt from the meta-critic’s supervision of what it should do in those unlabelled states (unseen situations). (2) The proposed task-conﬁg and meta-critic networks can capture the correlation among diverse learning tasks from the past, and such history-dependent knowledge can be transferred to the learning of a new task, making the agent more capable of choosing the suitable policy to optimize rewards when being exposed to a new environment.

**Fragmento 10 - p. 6 - score 4:**

Unlike conventional actor- critic networks [54], [55] that train a pair of actor-critic for each learning task individually, the proposed framework trains a shared meta-critic to provide transferrable knowledge among actors, which allows the actors to be trained with only a few trials in adapting to a new task. For example, by considering a set of tasks each learns an ABR policy in a particular environment such as Ethernet or WiFi networks, we can train a task-independent meta-critic from them, and apply the meta-critic to efﬁciently learn an actor for a new target task such as a new ABR policy for 3G networks. To apply the idea of meta-learning on solving the problem, we need to explicitly condition the meta-critic on a task, so that at any moment it knows what actor it is training and what task the actor should be trained to solve.

**Fragmento 11 - p. 11 - score 4:**

The results are shown in Table VI, Figs. 11 and 12. Clearly MetaABR(Hybrid) achieves the best QoEs in most cases, and it beats the personally trained method Comyco on most QoE metrics, thanks to its power of knowledge transfer from other learning tasks. Pensieve(Hybrid) performs close to or worse than the model-based methods such as BBA and RobustMPC, which shows poor ability of knowledge transfer without meta-learning. To test whether the training knowledge from single dataset is transferable to multiple datasets, we train both MetaABR and Pensieve on the 3G dataset, and then apply the pre-trained model to the rest networks. The results are shown in Table VII. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 12 - p. 15 - score 4:**

2436 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 based ABR design. Based on the proposed framework, we proposed MetaABR, a novel adaptive bitrate selection algorithm based on meta-critic to maximize users’ QoE. MetaABR jointly trained multiple learning tasks with a shared meta-critic, and it could provide transferrable knowledge to supervise bitrate se- lection across tasks. Extensive experiments based on real-world traces and testbed showed that MetaABR achieved the best QoE compared with the state-of-the-arts. REFERENCES [1] S. Krishnan and R. Sitaraman, “Video stream quality impacts viewer be- havior: Inferring causality using quasi-experimental designs,” IEEE/ACM Trans. Netw., vol.

**Fragmento 13 - p. 2 - score 3:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2423 Fig. 1. Performance of a pre-trained DRL agent (Pensieve [5] trained on 3G dataset) testing on different network environments (details are in Section V-C2). adaptation in varying network conditions. CS2P [4] used a data-driven approach to learn clusters of similar sessions and a Hidden-Markov-Model (HMM) based midstream predictor to model the stateful evolution of throughput. Fugu [16] adopted a supervised learning approach from the server side to train a probabilistic predictor of upcoming chunk transmission times and used the prediction information to improve the control policy of MPC. A few works [5], [14], [15], [17] applied Deep Reinforcement Learning (DRL) to train an agent to generate ABR policy by interacting with the environment.

**Fragmento 14 - p. 2 - score 3:**

(C1) Long bootstrap time: The DRL-based methods need to collect a large amount of training data by exploring various of actions in different network environments, which typically requires several hours(e.g.,8hoursreportedinPensieve[5])toformapre-trained neural network model. (C2) Lack of knowledge transfer: The existing DRL algorithms are typically task-speciﬁc and trained to work on a speciﬁc network environment independently, which are hard to deal with unseen scenarios. As an example, we adopt the Pensieve [5] algorithm to train a DRL agent on a 3G network, andthenapplytheagentforbitrateselectionondifferentnetwork conditions in Fig. 1. It is shown that the agent performs well on the working environment the same as the training network (see Fig.

**Fragmento 15 - p. 3 - score 3:**

As shown in Section V-C3, MetaABR trains a DRL agent much faster than regular DRL methods, whose convergence time is about 1/10 of that of Pensieve. Secondly, with the proposed meta-learning method, a DRL agent can be trained to learn transferable knowledge from historical tasks, which gains the ability to be applied in unseen environment. Meta-learning has the advantage of capturing the general knowledge across similar learning tasks in the past to improve the performance of learning new tasks to achieve knowledge transfer. As shown in Sec- tionV-C2,aMeteABRmodelcanbetrainedwiththe3Gnetwork trace and then applied to the WiFi and 4G networks, whose performance is still maintained and is better than the model- based ABR algorithms such as BBA and MPC.

**Fragmento 16 - p. 3 - score 3:**

The rest of the paper is organized as follows. Section II intro- duces the related works of media streaming bitrate adaptation methods and meta learning algorithms. Section III presents the detailed mechanism of bitrate adaptation based on meta learn- ing. Section IV proposes the training method for the proposed meta-critic and task-speciﬁc actors. Section V evaluates the system performance with extensive experiments. The paper is concluded in Section VI. II. RELATED WORK In this section, we introduce the related works in terms of ABR schemes for video streaming and meta learning. A. ABR Schemes for Video Streaming The ABR schemes for video streaming can be classiﬁed into two categories: the model-based and the learning-based methods.

**Fragmento 17 - p. 4 - score 3:**

Optimization of video streaming dilivery were also studied in the aspects of routing path assignment [29] and inter-session multiplexing congestion control [30]. Different from the existing learning based methods, the pro- posed MetaABR method introduces a novel meta-learning ap- proach with neural-enhanced bitrate selection particularly object to improve the generalization, robustness, and training efﬁciency of the deep learning based ABR methods. To the best of our knowledge, MetaABR is the ﬁrst to incorporate meta-critic into the design of ABR mechanism for video streaming. B. Meta-Learning Meta-learning, also known as learning to learn, is a machine learning method that intends to learn the general knowledge across similar learning tasks to improve its performance in new tasks based on a few examples [20], [21].

**Fragmento 18 - p. 4 - score 3:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2425 architectures including feedforward and recurrent deep neural networks to learn video adaptation strategies to achieved a good trade-off between policy optimality and convergence speed. Pensieve [5] proposed a Deep Reinforcement Learning (DRL) model that selected bitrates for future video chunks based on observations collected by DASH clients (i.e., throughput es- timation and buffer occupancy) across large video streaming experiments, which provided an expressive and scalable way to incorporate a rich variety of observations into the control policy. To address the issue of low sample efﬁciency of DRL, Comyco [15] trained an ABR policy via imitating expert tra- jectories to avoid redundant exploration.

**Fragmento 19 - p. 6 - score 3:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2427 Fig. 4. Framework of MetaABR. algorithm [50] for deep reinforcement learning. A3C is a state- of-the-art DRL method that jointly trains a pair of actor-critic deep neural networks for any RL task so that the actor learns to solve the problem, and the critic learns to effectively supervise the actor by approximating its reward. Following the learning to learn method [50], [51], we adapt the A3C method for meta- learning by training a global meta-critic neural network based on cross-task knowledge to supervise multiple actor networks to solve speciﬁc problems. In this way, the shared meta-critic can provide transferable knowledge in training actors to gener- ate ABR policies for different network environments, and the experience of meta-critic can be learned by the actors on new problems with only a few trials to achieve adaptivity and fast convergence.

**Fragmento 20 - p. 6 - score 3:**

To achieve this, the meta-critic is further divided into a task-conﬁg network and a critic network as shown in Fig. 4. The task-conﬁg network takes the past trails of a RL task represented by a trajectory of the state, action, and reward as input to learn historical experience, and it outputs a task-actor embedding z which represents the task-speciﬁc features. The critic network uses the current (state, action) and the task-actor embedding z from the task-conﬁg network as input to approximate the reward for a RL task, where z serves as the meta-knowledge to decide how to criticise the current actor on the speciﬁc task. The training details are given in Section IV. By jointly training the meta-critic with multiple actors, the meta-critic gains the ability to correctly criticise a new task based on the provided task-conﬁg network.

**Fragmento 21 - p. 6 - score 3:**

IV. TRAINING METHODS In this section, we introduce the methods of training the meta- critic and the task-speciﬁc actors in detail. A. Training the Meta-Critic In the proposed framework, we want to train a single meta- critic that can criticise any actor to perform any task. This requires two generalisations (task and actor conditioning) com- pared to conventional critic networks that criticise a speciﬁc actor for a speciﬁc task. The structure of the meta-critic is illus- trated in Fig. 5, which consists of two subnetworks: a task-conﬁg network and a critic network. The task-conﬁg network Cω, parameterised by ω, has a three- layer neural network structure. It takes the past k trails of (state, action, reward) triplets as input to learn task-speciﬁc experience.

**Fragmento 22 - p. 7 - score 3:**

The actor network takes the state s(i) t as input, then outputs an action a(i) t , i.e., a(i) t = Aθ(i)(s(i) t ). After applying each ac- tion, the agent observes a reward for that chunk. The goal of each learning agent is to maximize the expected cumulative (discounted) reward that it receives from the network environ- ment in terms of a speciﬁc QoE metric. In other words, the actor network intends to maximize the discounted future reward Qφ(s(i) t , a(i) t , z(i) t ) that is the estimated value from the output of the meta-critic network. Therefore, the optimizer alternately updates the actor network with: θ(i) ←arg max θ(i) Qφ  s(i) t , Aθ(i)(s(i) t ), z(i) t  . (10) Intheaboveequation,multipleactorsaretrainedjointlytoﬁnd their optimal model parameters θ(i) to maximize the estimated reward based on the output of the meta-critic.

**Fragmento 23 - p. 7 - score 3:**

V. EXPERIMENTS In this section, we conduct extensive experiments to evaluate the performance of MetaABR. Our experiments cover a broad set of network conditions and QoE metrics. We mainly focus on answering the following questions. (1) How does MetaABR compare to the state-of-the-art ABR algorithms in terms of video QoE? We ﬁnd that, in all of the consideredscenarios,MetaABRisabletorivaloroutperformthe best existing scheme, with average QoE improvements ranging from 3%-15%. (2) Does the MetaABR method perform more efﬁciently than other reinforcement learning methods? Through the experiment, we ﬁnd that MetaABR can achieve comparable performance with other reinforcement learning methods with much fewer samples and training epochs, and it performs the best even being transferred to a different network environment.

**Fragmento 24 - p. 7 - score 3:**

(3) How is the trade-off between different conﬂicting QoE metrics? We ﬁnd that MetaABR achieves a better trade-off between increasing bitrate and reducing rebuffering time and variation, which is more closer to the ideal situation compared to the baselines. A. Experiment Setup 1) Implementation: In our implementation of the MetaABR scheme, the task-conﬁg network Cω, the critic network Qφ, and the actor network Aθ are three-layer fully-connected neural networks that use rectiﬁed linear unit (ReLU) as the activa- tion function of each neuron. We train the neural networks on TensorFlow 1.13.1 using RMSPropOptimizer with learning rate 0.01 (Cω), 0.0001 (Qφ), and 0.001 (Aθ) accordingly. The Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 25 - p. 7 - score 3:**

The critic network Qφ, parameterised by φ, has similar structure as that of the task-conﬁg network, which is used to approximate the reward for reinforcement learning tasks. Apart from the state st and action at, it further takes the task-actor embedding z as input to learn an action-value function. We use Qφ(s(i) t , a(i) t , z(i) t ) to describe the expected return reward after actor i taking action a(i) t in state s(i) t with a task-actor embedding z(i) t . The meta-critic is shared across all tasks and actors, which is trained to help actors to ﬁnd strategies that are more suitable for the environment. Assuming there are M learning tasks, the update rules for the meta-critic model parameters are as follows.

**Fragmento 26 - p. 9 - score 3:**

MetaABR trained from hy- brid trace signiﬁcantly outperforms the other algorithms, which achieves the best QoE on almost all network conditions. This shows the power of meta-learning: it can learn experiences from different network conditions to improve performance and be adaptable to different scenarios. For QoEstd, a widely con- sidered metric in the literature [5], [64], the average QoE for MetaABR is 5% higher than that of Pensieve on 3G networks, and 3% ∼15% higher in other networks. The gaps between MetaABR and other methods are also found in QoEfluent and QoEhd. It is noticed that the CDFs in 4GSyd show stair-like shapes in Fig. 9, and the reason is explained as follows. Since the 4GSyd trace has very stable throughput, where over 95% Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.


### 7.6. datos trazas datasets origen

Palabras clave usadas: `dataset, datasets, trace, traces, network trace, bandwidth trace, real-world, FCC, HSDPA, Norway, LTE, 4G, 5G, WiFi, WLAN, Mahimahi, emulation, testbed, Puffer, data, sessions, users, video, chunk, streaming server`

**Fragmento 1 - p. 8 - score 10:**

In 3https://github.com/Dash-Industry-Forum/dash.js/, Akamai, 2020. our settings, the client video player is Google Chrome (version 85) and chromedriver (version 85.0.4183.38). The video server is Apache (version 2.4.7). We use Mahimahi [57] to emulate network environments from the network traces between the client and the server with 80 ms RTT. 5) Datasets and Network Traces: To evaluate the ABR algo- rithms on realistic network conditions, we created a corpus of network traces using several real-world network communication datasets. r 3 G [59]: This dataset was collected from popular commute routes in and around Oslo (Norway). It includes throughput measurements of real-world adaptive HTTP streaming per- formed over 3G networks using mobile devices traveling with different types of public transportation (metro, tram, train, bus and ferry).

**Fragmento 2 - p. 3 - score 9:**

Thirdly, since the meta-model is typically trained with multiple datasets from different network environments, the historical experiences can be learned by the meta-model, which can be used to supervise the training of a general agent to adapt to various environments. As shown in Section V-C1, the DRL model of MeteABR trained with a combined dataset (3G+WiFi+4G traces) clearly beats the other DRL models trained with a single dataset. The contribution of our work are summarized as follows. r We formulate a novel framework for meta-learning based adaptive bitrate selection design. We discuss the challenges of deploying DRL-based ABR mechanism in real-world video streaming systems, which are not trivial to address within conventional DRL formalism.

**Fragmento 3 - p. 8 - score 9:**

It was generated from two mobility pat- terns (static and car) across two application patterns (video streaming and ﬁle download). It consists of two parts: the ﬁrst is a production dataset collected from real-world and the second is synthetic data generated from a large-scale multi-cell 5G/mmwave ns-3 platform. We selected the data generated from the Amazon Prime and Netﬂix streaming services in the experiments, and the throughput of the 5G network is in the range of 3 ∼202.5 Mbps. The basic information of the datasets are listed in Table III. The statistical characteristics of the datasets are shown in Fig. 6. According to the ﬁgure, both 3G and WiFi traces have small throughput and low variations.

**Fragmento 4 - p. 9 - score 9:**

For the WiFi dataset, we generated 1000 traces (each with 320 sec- onds) by concatenating randomly selected traces from the “Web browsing” category in the Aug 2016 collection. For the Hybrid scenario, we simply combined the throughput traces generated from the 3G, WiFi, and 4GSyd datasets together to form the dataset. We reformatted the generated throughput traces to ﬁt the Mahimahi [57] emulation platform, so that the same trace can be replayed to test different ABR algorithms. We randomly partition the generated traces into train and test datasets, where 80% of data are used for training machine learning models and 20% are used for testing all compared algorithms by default. Among the train set, 20% of data are used to form a validation set for hyperperameter tuning.

**Fragmento 5 - p. 2 - score 8:**

Fig. 3. Illustration of meta-critic based bitrate adaptation. it on different network environments in Fig. 2. As illustrated in Figs. 2(a) to (c), the model trained with multiple network traces does not improve adaptivity, and it performs even worse than those trained with a single network dataset. The poor adaptivity with mixture datasets is probably caused by dataset shift [18], [19]: the joint distribution of inputs and outputs differs between training and test stages. In our example, the DRL model trained to ﬁt data on a wide distribution (3G+WiFi+4G) and tested only on a relatively narrow distribution will result in a degradation of performance. In this article, we propose MetaABR, a novel ABR algorithm based on meta-learning to address the above challenges.

**Fragmento 6 - p. 2 - score 8:**

1(a)), whereas it performs poorly on the WiFi and 4G networks, whose QoEs (see Fig. 1(b) and (c)) are close to or lower than that of simple model-based algorithms such as BBA [11] and RobustMPC [13]. (C3) Poor adaptivity: The existing DRL models trained for a client cannot be generalized to other clients even they operate on similar environments. As a result,itishardtotrainageneralizedmodeltocopewithdifferent network types even rich historical datasets are available. For example, we use an augmented hybrid dataset combining 3G, WiFi and 4G network traces to train a DRL model and apply Fig.2. PerformanceofPensieve[5]DRLagentstrainedwithdifferentdatasets, where Hybrid means the dataset combining 3G, WiFi and 4G traces (details are in Section V-C1).

**Fragmento 7 - p. 9 - score 8:**

Since the traces of the 4GNY and 5G datasets are much smaller than that of the other datasets, we only used them for testing the adaptivity and knowledge transfer of the DRL algorithms. That is, we trained the DRL models using other datasets, and then tested the pre-trained models on the 4GNY and 5G datasets to show their performance on unseen network environments. Following similar principle, we generated 200 throughput traces each with a duration of 320 seconds by using TABLE IV THE QOE METRICS CONSIDERED IN THE EVALUATION a sliding window across the 4GNY and 5G network traces to form the test sets. 6) QoE Metrics: Similar to the literature, we consider three QoE metrics with different choices of the combination of q(Rn,v) and M.

**Fragmento 8 - p. 8 - score 7:**

The throughput of the network is between 0.1 ∼1 Mbps. r WiFi [5]: This dataset is from the work [5], which is tai- lored from a broadband dataset provided by the FCC [60]. Since the original dataset contains large amount broadband data log over one year, the authors in [5] selected the “Web browsing” category in the Aug 2016 collection and only keeps traces whose average throughput is less than 6 Mbps to avoid trivial ABR solutions. r 4GSyd [61]: This dataset was collected from SpeedTest measurements conducted in Sydney on 4G networks under vehicular driving conditions. In the dataset, throughput measurements samples were collected within 72 trips in different day and night times to consider On and Off peak hours of trafﬁc.

**Fragmento 9 - p. 9 - score 7:**

In our experiments, we report the average QoE per chunk, i.e., the total QoE metric divided by the number of chunks in the video. B. Comparison With Baseline Algorithms In this section, we compare the performance of MetaABR with the baseline algorithms with different network traces. The Cumulative Distribution Functions (CDFs) of the algo- rithms on different QoE metrics are illustrated in Figs. 7, 8, 9, and 10, and the average results are shown in Table V. We make the following discussions on the results. Firstly, MetaABR either matches or exceeds the performance of the state-of-the-art ABR algorithms on each QoE metric and network considered. According to Table V, MetaABR trained from individual network trace (e.g., 3G, WiFi, and 4GSyd) performs very close to Pensieve.

**Fragmento 10 - p. 9 - score 7:**

2430 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 TABLE III DATASETS STATISTICS Fig. 6. Characteristics of datasets. standard deviation is less than 0.5. The reason is that 4GSyd was collectedwiththeTestSpeedAPPwhichformsstablethroughput testing from different locations. The 4GNY and 5 G datasets are more diverse, whose throughput spread from a wide range with larger deviations. For each of the above dataset, we follow the method proposed in Pensieve [5] to generate traces for reinforcement learning and to test the ABR algorithms. For the 3G and 4GSyd datasets, we generated 1000 throughput traces each with a duration of 320 seconds by using a sliding window across the network traces.

**Fragmento 11 - p. 16 - score 7:**

Netravali et al., “Mahimahi: Accurate record-and-replay for HTTP,” in Proc. USENIX Annu. Tech. Conf., 2015, pp. 417–429. [58] N. Kan, C. Li, C. Yang, W. Dai, J. Zou, and H. Xiong, “Uncertainty-aware robust adaptive video streaming with bayesian neural network and model predictive control,” in Proc. 31st ACM Workshop Netw. Operating Syst. Support Digit. Audio Video, 2021, pp. 17–24. [59] H. Riiser, P. Vigmostad, C. Griwodz, and P. Halvorsen, “Commute path bandwidth traces from 3G networks: Analysis and applications,” in Proc. 4th ACM Multimedia Syst. Conf., 2013, pp. 114–118. [60] “Raw data - measuring broadband America2016,” 2021. [Online]. Available: https://www.fcc.gov/reports-research/reports/measuring- broadband-america/raw-data-measuring-broadband-america-2016 [61] A.

**Fragmento 12 - p. 10 - score 6:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2431 Fig. 7. CDF of QoE metrics (3G network). Fig. 8. CDF of QoE metrics (WiFi network). Fig. 9. CDF of QoE metrics (4Gsyd network). throughput are concentrated on 8-9 Mbps with standard de- viation less than 0.5 as shown in Fig. 6, it is easy to form a trivial solution for bitrate selection. That is, it can use full (near-constant) bandwidth to satisfy the QoE in a high level for the vast majority of ABR cases. Therefore, machine learning methods did not show signiﬁcant performance improvement compared to model-based methods in the 4GSyd datasets, and most algorithms achieve high QoEs with more than 95% of cases concentrating on a high level.

**Fragmento 13 - p. 11 - score 6:**

As illustrated in Table V, MetaABR(Hybrid) performs close or better than those models personally trained on speciﬁc networks. For example, MetaABR(Hybrid) outperforms MetaABR(WiFi) on the WiFi network, and outperforms MetaABR(4GSyd) on the 4G network, which generally achieves the best perfor- mance on all test datasets. On the other hand, conventional DRL method such as Pensieve has poor adaptivity, e.g., Pen- sieve(Hybrid) clearly performs much worse than Pensieve(3G) and Pensieve(WiFi) on the corresponding datasets. 2) Ability of Knowledge Transfer: We then test the ability of knowledge transfer. Similar to the experiments in Section V-B, we use the Hybrid dataset to pre-train a DRL model, and apply the model to unseen networks (i.e., 4GNY and 5G) to test its performance.

**Fragmento 14 - p. 13 - score 6:**

E. Performance on Multi-Video Scenario In this experiment, we test the pre-trained DRL models on a multi-video scenario to evaluate their ability to generalize across multiple video streaming properties. We generate the trace of multiple video streaming scenario as follows. We generate 1000 synthetic video traces with diverse bitrates, chunk sizes, and video duration. The value of bitrate is randomly chosen from {200, 300, 450, 750, 1200, 1850, 2850, 4300, 6000, 8000} Kbps. The chunk size of each video is a mean size multiplying a Gaussian distribution N(1, 0.1). The duration of each video is a random chunk number in the range [20,100]. We apply the DRL model trained with Hybrid dataset on the multi-video scenario, and the experimental results are illustrated in Fig.

**Fragmento 15 - p. 15 - score 6:**

2436 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 based ABR design. Based on the proposed framework, we proposed MetaABR, a novel adaptive bitrate selection algorithm based on meta-critic to maximize users’ QoE. MetaABR jointly trained multiple learning tasks with a shared meta-critic, and it could provide transferrable knowledge to supervise bitrate se- lection across tasks. Extensive experiments based on real-world traces and testbed showed that MetaABR achieved the best QoE compared with the state-of-the-arts. REFERENCES [1] S. Krishnan and R. Sitaraman, “Video stream quality impacts viewer be- havior: Inferring causality using quasi-experimental designs,” IEEE/ACM Trans. Netw., vol.

**Fragmento 16 - p. 16 - score 6:**

Bokani, M. Hassan, S. S. Kanhere, J. Yao, and G. Zhong, “Comprehen- sive mobile bandwidth traces from vehicular networks,” in Proc. 7th Int. Conf. Multimedia Syst., 2016, pp. 1–6. [62] L. Mei et al., “Realtime mobile bandwidth prediction using LSTM neural network and bayesian fusion,” Comput. Netw., vol. 182, 2020, Art. no. 107515. [63] D. Raca, D. Leahy, C.J. Sreenan, and J. J. Quinlan, “Beyond throughput, the next generation: A 5G dataset with channel and context metrics,” in Proc. 11th ACM Multimedia Syst. Conf., 2020, pp. 303–308. [64] P. Wawrzynski, “Control policy with autocorrelated noise in reinforcement learning for robotics,” Int. J. Mach. Learn. Comput., vol. 5, no. 2, 2015, Art. no. 91. Wenzhong Li (Member, IEEE) received the BS and PhD degrees in computer science from Nanjing Uni- versity, China.

**Fragmento 17 - p. 1 - score 5:**

Extensive experiments based on real-world traces and wireless testbed show that MetaABR achieves the best comprehensive QoE compared with the state-of-the-art ABR algorithms in a variety of network environments. Index Terms—Bitrate adaptation, meta-learning, reinforcement learning, video streaming. I. INTRODUCTION R ECENT years have witnessed a rapid growth of Internet video streaming applications. Video on demand (VoD) ser- vices have stimulated a revolution in video content consumption by providing audiences a platform to watch whatever they want anytime. According to the report,1 the global video streaming market size was valued at USD 70.59 billion in 2022, and is expected to expand at a compound annual growth rate (CAGR) Manuscriptreceived7May2022;revised26February2023;accepted7March 2023.

**Fragmento 18 - p. 2 - score 5:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2423 Fig. 1. Performance of a pre-trained DRL agent (Pensieve [5] trained on 3G dataset) testing on different network environments (details are in Section V-C2). adaptation in varying network conditions. CS2P [4] used a data-driven approach to learn clusters of similar sessions and a Hidden-Markov-Model (HMM) based midstream predictor to model the stateful evolution of throughput. Fugu [16] adopted a supervised learning approach from the server side to train a probabilistic predictor of upcoming chunk transmission times and used the prediction information to improve the control policy of MPC. A few works [5], [14], [15], [17] applied Deep Reinforcement Learning (DRL) to train an agent to generate ABR policy by interacting with the environment.

**Fragmento 19 - p. 3 - score 5:**

r We utilize the proposed framework to design MetaABR, a novel adaptive bitrate selection algorithm based on meta- learning to maximize users’ QoE. By jointly training mul- tiple learning tasks with a shared meta-critic, it has the ability to provide transferrable knowledge to supervise bitrate selection, and can be applied to efﬁciently learn a new task in unseen environment with much fewer data samples and trainng epoches. r We implement the proposed MetaABR based on an emula- tionplatformwhichconnectstotheLinuxnetworkprotocol stack through a virtual network interface to send real data packets for evaluation. Extensive experiments based on real-world traces show that MetaABR achieves the best comprehensive QoE compared with the state-of-the-art ABR algorithms in a variety of network environments.

**Fragmento 20 - p. 8 - score 5:**

The throughput of the 4G network ranges from 5 ∼10 Mbps. r Hybrid (3G + WiFi + 4GSyd): We combine the data sampes of the above 3G, WiFi, and 4GSyd datasets to generateahybriddataset.Itsimulatesthereal-lifescenarios where three networks are dynamically switching due to the mobility of smartphones. The performance in this dataset can well reﬂect the generalization ability of the ABR method. r 4GNY [62]: This dataset was collected on New York City MTA bus and subway. The data was recorded with a mobile phone running iPerf to log TCP throughput every 1000 milliseconds. The throughput of the network environment is between 1 ∼108 Mbps. r 5 G [63]: This dataset was collected from a major Irish mobile operator.

**Fragmento 21 - p. 11 - score 5:**

2432 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 Fig. 10. CDF of QoE metrics (Hybrid network). TABLE V COMPARISON OF AVERAGE BITRATE (MBPS), REBUFFERING TIME (SECOND), VARIATIONS, AND THEIR CORRESPONDING QOE METRICS ON DIFFERENT NETWORK ENVIRONMENTS, WHERE METAABR(HYBRID) MEANS A METAABR MODEL TRAINED WITH THE Hybrid DATASET, AND SO ARE THE REST C. Effectiveness of Meta-Critic Learning 1) Adaptivity: The major advantage of MetaABR is its adap- tivity on different network traces, which enables a machine learning ABR algorithm to learn once and be applied to any- where. With the proposed meta-learning method we can train a general model MetaABR(Hybrid) based on the Hybrid dataset and then apply it to the other networks without modiﬁcation.

**Fragmento 22 - p. 12 - score 5:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2433 TABLE VI COMPARISON OF QOE METRICS FOR TRANSFERRING A PRE-TRAINED MODEL TO UNSEEN NETWORK ENVIRONMENTS, WHERE METAABR(HYBRID) MEANS A METAABR MODEL TRAINED WITH THE Hybrid DATASET, AND SO ARE THE REST Fig. 11. CDF of QoE metrics (Train set: Hybrid; Test set: 4GNY ). Fig. 12. CDF of QoE metrics (Train set: Hybrid; Test set: 5G). TABLE VII COMPARISON OF QoEstd METRIC FOR TRANSFERRING A PRE-TRAINED MODEL ON 3G DATASET TO MULTIPLE NETWORK ENVIRONMENTS According to the table, both MetaABR and Pensieve perform well in 3G network (where train and test environment are the same). After applying to other networks, Pensieve performs worse than the model-based approaches BBA and RobustMPC, Fig.

**Fragmento 23 - p. 14 - score 5:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2435 Fig. 16. CDF of QoE metrics of multi-video scenario testing on WiFi network. Fig. 17. CDF of QoEstd metrics under real-world network scenarios. TABLE VIII COMPARISON OF AVERAGE BITRATE (MBPS), REBUFFERING TIME (SECOND), VARIATIONS, AND QoEstd METRIC ON REAL-WORLD SCENARIOS on a variety of QoE metrics, and signiﬁcant performance im- provement is found in the QoEfluent metric. The results suggest that MetaABR can be adapted to the multiple video streaming scenarios with diverse QoE properties. F. Performance on Real-World Scenarios Apartfromtrace-drivenexperiments,wedeploythecompared algorithms in a wireless network testbed to test the performance under real-world scenarios.

**Fragmento 24 - p. 1 - score 4:**

In this article, we propose a novel framework for meta-learning based ABR design and discuss challenges of deploying learning based ABR mechanism in real-world video streaming systems. We utilize the proposed framework to design MetaABR, a novel adaptive bitrate selection algorithm based on meta-reinforcement learning to maximize users’ QoE. By jointly training multiple learning tasks with a shared meta-critic, it can provide transferrable meta-knowledge to supervise bitrate selec- tion across tasks, and can be applied to efﬁciently learn a new task in unseen environment with only a few trials. We imple- ment MetaABR on an emulation platform which connects to the Linux network protocol stack through virtual network interfaces.

**Fragmento 25 - p. 3 - score 4:**

As shown in Section V-C3, MetaABR trains a DRL agent much faster than regular DRL methods, whose convergence time is about 1/10 of that of Pensieve. Secondly, with the proposed meta-learning method, a DRL agent can be trained to learn transferable knowledge from historical tasks, which gains the ability to be applied in unseen environment. Meta-learning has the advantage of capturing the general knowledge across similar learning tasks in the past to improve the performance of learning new tasks to achieve knowledge transfer. As shown in Sec- tionV-C2,aMeteABRmodelcanbetrainedwiththe3Gnetwork trace and then applied to the WiFi and 4G networks, whose performance is still maintained and is better than the model- based ABR algorithms such as BBA and MPC.

**Fragmento 26 - p. 4 - score 4:**

Stick [17] fused the DRL method and traditional buffer-based method to output the buffer-bound, which was used to control the buffer-based approach for maximizing the QoE metrics. Fugu [16] argued that in real-world setting, it was difﬁcult for sophisticated or machine-learned control schemes to outperform a simple buffer- basedcontrolscheme,notwithstandinggoodperformanceinnet- work emulators or simulators. It used supervised learning with data from real deployment environment to train a probabilistic predictor of upcoming chunk transmission times to improve a classical control policy. Recently, learning-based methods were extended to the emerging 3D video streaming applications and video conferencing systems [24], [25], [26], [27], [28].


### 7.7. evaluacion baselines experimentos

Palabras clave usadas: `evaluation, experiment, experiments, baseline, baselines, compare, comparison, Pensieve, BBA, BOLA, MPC, RobustMPC, FastMPC, A3C, PPO, DQN, SODA, Oboe, MetaABR, results, outperform, ablation, scenario, test`

**Fragmento 1 - p. 8 - score 8:**

3) Baseline Algorithms: We compare MetaABR with three state-of-the-art ABR algorithms: r BBA [11]: a buffer-based approach which selects bitrates based on playback buffer occupation. r RobustMPC [13]: a model predictive control algorithm that combines both throughput estimates and buffer occupancy information to select bitrates. r Pensieve [5]: a state-of-the-art ABR scheme based on deep reinforcement learning. r BayesMPC [58]: an uncertainty-aware robust ABR algo- rithm based on Bayesian neural network (BNN) and model predictive control (MPC). r Comyco [15]: a video quality-aware ABR approach lever- aging imitation learning to accelerate the training process for ABR tasks. Note that we do not compare with other deep learning based ABR algorithms such as Fugu [16], Oboe [23], and Stick [17], since either they are implemented on the server side, or there are lack of open-source code to reproduce their work.

**Fragmento 2 - p. 9 - score 8:**

In our experiments, we report the average QoE per chunk, i.e., the total QoE metric divided by the number of chunks in the video. B. Comparison With Baseline Algorithms In this section, we compare the performance of MetaABR with the baseline algorithms with different network traces. The Cumulative Distribution Functions (CDFs) of the algo- rithms on different QoE metrics are illustrated in Figs. 7, 8, 9, and 10, and the average results are shown in Table V. We make the following discussions on the results. Firstly, MetaABR either matches or exceeds the performance of the state-of-the-art ABR algorithms on each QoE metric and network considered. According to Table V, MetaABR trained from individual network trace (e.g., 3G, WiFi, and 4GSyd) performs very close to Pensieve.

**Fragmento 3 - p. 14 - score 8:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2435 Fig. 16. CDF of QoE metrics of multi-video scenario testing on WiFi network. Fig. 17. CDF of QoEstd metrics under real-world network scenarios. TABLE VIII COMPARISON OF AVERAGE BITRATE (MBPS), REBUFFERING TIME (SECOND), VARIATIONS, AND QoEstd METRIC ON REAL-WORLD SCENARIOS on a variety of QoE metrics, and signiﬁcant performance im- provement is found in the QoEfluent metric. The results suggest that MetaABR can be adapted to the multiple video streaming scenarios with diverse QoE properties. F. Performance on Real-World Scenarios Apartfromtrace-drivenexperiments,wedeploythecompared algorithms in a wireless network testbed to test the performance under real-world scenarios.

**Fragmento 4 - p. 11 - score 7:**

The results are shown in Table VI, Figs. 11 and 12. Clearly MetaABR(Hybrid) achieves the best QoEs in most cases, and it beats the personally trained method Comyco on most QoE metrics, thanks to its power of knowledge transfer from other learning tasks. Pensieve(Hybrid) performs close to or worse than the model-based methods such as BBA and RobustMPC, which shows poor ability of knowledge transfer without meta-learning. To test whether the training knowledge from single dataset is transferable to multiple datasets, we train both MetaABR and Pensieve on the 3G dataset, and then apply the pre-trained model to the rest networks. The results are shown in Table VII. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 5 - p. 12 - score 7:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2433 TABLE VI COMPARISON OF QOE METRICS FOR TRANSFERRING A PRE-TRAINED MODEL TO UNSEEN NETWORK ENVIRONMENTS, WHERE METAABR(HYBRID) MEANS A METAABR MODEL TRAINED WITH THE Hybrid DATASET, AND SO ARE THE REST Fig. 11. CDF of QoE metrics (Train set: Hybrid; Test set: 4GNY ). Fig. 12. CDF of QoE metrics (Train set: Hybrid; Test set: 5G). TABLE VII COMPARISON OF QoEstd METRIC FOR TRANSFERRING A PRE-TRAINED MODEL ON 3G DATASET TO MULTIPLE NETWORK ENVIRONMENTS According to the table, both MetaABR and Pensieve perform well in 3G network (where train and test environment are the same). After applying to other networks, Pensieve performs worse than the model-based approaches BBA and RobustMPC, Fig.

**Fragmento 6 - p. 13 - score 7:**

4) Performance With Small Samples: Fig. 14 shows the re- sults of MetaABR with different percentages of training sam- ples. It is shown that even using only 10% of the total train dataset, MetaABR still has comparable performance with Pen- sieve with full dataset. D. Trade-Off Between QoE Metrics We study the trade-off between different conﬂicting QoE met- rics, and the normalized results are shown in Fig. 15. It is shown that RobustMPC achieves higher bitrate with larger rebuffering time and variation. Pensieve and BBA have modest bitrate and rebuffering time/variation. Compared to the other algorithms, MetaABR achieves the best trade-off between different QoE metrics, which is much more closer to the ideal situation.

**Fragmento 7 - p. 14 - score 7:**

(3) School Bus: the client is connected to a 4G network and it is placed on a school bus with constant movement. The CDF of QoE of different ABR algorithms under different scenarios is compared in Fig. 17, and the average QoE metrics are illustrated in Table VIII. Due to page limit, we only show the QoEstd metric for comparison. According to Fig. 17, the CDF curve of MetaABR is lower than that of other algorithms in three scenarios, which means MetaABR is concentrating on the region of higher QoEstd. According to Table VIII, in the dormitory scenario, MetaABR improves the QoE performance by 4.2% compared to Pensieve and 57.4% higher than that of RobustMPC.Similarly,signiﬁcantQoEimprovementisfoundin the library and the school bus scenarios.

**Fragmento 8 - p. 7 - score 6:**

V. EXPERIMENTS In this section, we conduct extensive experiments to evaluate the performance of MetaABR. Our experiments cover a broad set of network conditions and QoE metrics. We mainly focus on answering the following questions. (1) How does MetaABR compare to the state-of-the-art ABR algorithms in terms of video QoE? We ﬁnd that, in all of the consideredscenarios,MetaABRisabletorivaloroutperformthe best existing scheme, with average QoE improvements ranging from 3%-15%. (2) Does the MetaABR method perform more efﬁciently than other reinforcement learning methods? Through the experiment, we ﬁnd that MetaABR can achieve comparable performance with other reinforcement learning methods with much fewer samples and training epochs, and it performs the best even being transferred to a different network environment.

**Fragmento 9 - p. 8 - score 6:**

4) Video Parameters: We have modiﬁed dash.js3 to sup- port MetaABR and the above baseline ABR algorithms. For MetaABR, Pensieve, and RobustMPC, we conﬁgure dash.js to obtain the bitrate selection decision from an ABR process that implements the corresponding algorithm. The DASH player is conﬁgured to have a playback buffer capacity of 60 seconds. Our evaluation used the “Envivio-Dash3” video of the DASH-246 JavaScript reference client. In addition, the video is divided into 48 blocks with a total length of 193 seconds. This video is encoded by the H.264/MPEG-4 codec at bitrates in 300, 750, 1200,1850,2850,4300kbps(whichcorrespondstovideomodes in 240p, 360p, 480p, 720p, 1080p, 1440p). Therefore, each block represents approximately 4 seconds of video playback.

**Fragmento 10 - p. 11 - score 6:**

As illustrated in Table V, MetaABR(Hybrid) performs close or better than those models personally trained on speciﬁc networks. For example, MetaABR(Hybrid) outperforms MetaABR(WiFi) on the WiFi network, and outperforms MetaABR(4GSyd) on the 4G network, which generally achieves the best perfor- mance on all test datasets. On the other hand, conventional DRL method such as Pensieve has poor adaptivity, e.g., Pen- sieve(Hybrid) clearly performs much worse than Pensieve(3G) and Pensieve(WiFi) on the corresponding datasets. 2) Ability of Knowledge Transfer: We then test the ability of knowledge transfer. Similar to the experiments in Section V-B, we use the Hybrid dataset to pre-train a DRL model, and apply the model to unseen networks (i.e., 4GNY and 5G) to test its performance.

**Fragmento 11 - p. 1 - score 5:**

Extensive experiments based on real-world traces and wireless testbed show that MetaABR achieves the best comprehensive QoE compared with the state-of-the-art ABR algorithms in a variety of network environments. Index Terms—Bitrate adaptation, meta-learning, reinforcement learning, video streaming. I. INTRODUCTION R ECENT years have witnessed a rapid growth of Internet video streaming applications. Video on demand (VoD) ser- vices have stimulated a revolution in video content consumption by providing audiences a platform to watch whatever they want anytime. According to the report,1 the global video streaming market size was valued at USD 70.59 billion in 2022, and is expected to expand at a compound annual growth rate (CAGR) Manuscriptreceived7May2022;revised26February2023;accepted7March 2023.

**Fragmento 12 - p. 3 - score 5:**

r We utilize the proposed framework to design MetaABR, a novel adaptive bitrate selection algorithm based on meta- learning to maximize users’ QoE. By jointly training mul- tiple learning tasks with a shared meta-critic, it has the ability to provide transferrable knowledge to supervise bitrate selection, and can be applied to efﬁciently learn a new task in unseen environment with much fewer data samples and trainng epoches. r We implement the proposed MetaABR based on an emula- tionplatformwhichconnectstotheLinuxnetworkprotocol stack through a virtual network interface to send real data packets for evaluation. Extensive experiments based on real-world traces show that MetaABR achieves the best comprehensive QoE compared with the state-of-the-art ABR algorithms in a variety of network environments.

**Fragmento 13 - p. 7 - score 5:**

(3) How is the trade-off between different conﬂicting QoE metrics? We ﬁnd that MetaABR achieves a better trade-off between increasing bitrate and reducing rebuffering time and variation, which is more closer to the ideal situation compared to the baselines. A. Experiment Setup 1) Implementation: In our implementation of the MetaABR scheme, the task-conﬁg network Cω, the critic network Qφ, and the actor network Aθ are three-layer fully-connected neural networks that use rectiﬁed linear unit (ReLU) as the activa- tion function of each neuron. We train the neural networks on TensorFlow 1.13.1 using RMSPropOptimizer with learning rate 0.01 (Cω), 0.0001 (Qφ), and 0.001 (Aθ) accordingly. The Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 14 - p. 8 - score 5:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2429 TABLE II THE LAYER PARAMETERS OF METAABR reward discount factor γ = 0.99 by default. The neural network structure of MetaABR is illustrated in Table II. 2) Evaluation Platform: The experiments are conducted on a PC server (CPU: Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20 GHz; Memory: 32 GB DDR4 2400Mhz*4; OS: 64-bit Ubuntu 16.04). We implement the proposed MetaABR frame- work based on the Mahimahi [57] emulation platform, which is connected to the Linux network protocol stack through a virtual network interface and sends real data packets. Mahimahi can be used to record trafﬁc from HTTP-based applications and replay it under emulated network conditions, which is ideal for fair comparison of different ABR algorithms for video streaming.

**Fragmento 15 - p. 15 - score 5:**

2436 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 based ABR design. Based on the proposed framework, we proposed MetaABR, a novel adaptive bitrate selection algorithm based on meta-critic to maximize users’ QoE. MetaABR jointly trained multiple learning tasks with a shared meta-critic, and it could provide transferrable knowledge to supervise bitrate se- lection across tasks. Extensive experiments based on real-world traces and testbed showed that MetaABR achieved the best QoE compared with the state-of-the-arts. REFERENCES [1] S. Krishnan and R. Sitaraman, “Video stream quality impacts viewer be- havior: Inferring causality using quasi-experimental designs,” IEEE/ACM Trans. Netw., vol.

**Fragmento 16 - p. 2 - score 4:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2423 Fig. 1. Performance of a pre-trained DRL agent (Pensieve [5] trained on 3G dataset) testing on different network environments (details are in Section V-C2). adaptation in varying network conditions. CS2P [4] used a data-driven approach to learn clusters of similar sessions and a Hidden-Markov-Model (HMM) based midstream predictor to model the stateful evolution of throughput. Fugu [16] adopted a supervised learning approach from the server side to train a probabilistic predictor of upcoming chunk transmission times and used the prediction information to improve the control policy of MPC. A few works [5], [14], [15], [17] applied Deep Reinforcement Learning (DRL) to train an agent to generate ABR policy by interacting with the environment.

**Fragmento 17 - p. 2 - score 4:**

1(a)), whereas it performs poorly on the WiFi and 4G networks, whose QoEs (see Fig. 1(b) and (c)) are close to or lower than that of simple model-based algorithms such as BBA [11] and RobustMPC [13]. (C3) Poor adaptivity: The existing DRL models trained for a client cannot be generalized to other clients even they operate on similar environments. As a result,itishardtotrainageneralizedmodeltocopewithdifferent network types even rich historical datasets are available. For example, we use an augmented hybrid dataset combining 3G, WiFi and 4G network traces to train a DRL model and apply Fig.2. PerformanceofPensieve[5]DRLagentstrainedwithdifferentdatasets, where Hybrid means the dataset combining 3G, WiFi and 4G traces (details are in Section V-C1).

**Fragmento 18 - p. 3 - score 4:**

However, throughput can vary widely over time and result in poor ABR performance. Therefore, BBA [11] adopted a buffer-based approach which picked a bitrate based on playback buffer occupation. However, it suffered from QoE degradation during long-term bandwidth ﬂuctuations. BOLA [12] was also a buffer-based algorithm, whichturnedtheABRproblemintoautility-maximizationprob- lemandsolveditbytheLyapunovfunction.MPC[13]developed a control-theoretic framework that allowed the understanding and exploration of the trade-offs between bandwidth-based and buffer-based adaptation algorithms under different network bandwidth variations. Oboe [23] auto-tuned the parameters of model-based ABR algorithms for different network conditions to improve the ABR’s performance.

**Fragmento 19 - p. 3 - score 4:**

As shown in Section V-C3, MetaABR trains a DRL agent much faster than regular DRL methods, whose convergence time is about 1/10 of that of Pensieve. Secondly, with the proposed meta-learning method, a DRL agent can be trained to learn transferable knowledge from historical tasks, which gains the ability to be applied in unseen environment. Meta-learning has the advantage of capturing the general knowledge across similar learning tasks in the past to improve the performance of learning new tasks to achieve knowledge transfer. As shown in Sec- tionV-C2,aMeteABRmodelcanbetrainedwiththe3Gnetwork trace and then applied to the WiFi and 4G networks, whose performance is still maintained and is better than the model- based ABR algorithms such as BBA and MPC.

**Fragmento 20 - p. 4 - score 4:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2425 architectures including feedforward and recurrent deep neural networks to learn video adaptation strategies to achieved a good trade-off between policy optimality and convergence speed. Pensieve [5] proposed a Deep Reinforcement Learning (DRL) model that selected bitrates for future video chunks based on observations collected by DASH clients (i.e., throughput es- timation and buffer occupancy) across large video streaming experiments, which provided an expressive and scalable way to incorporate a rich variety of observations into the control policy. To address the issue of low sample efﬁciency of DRL, Comyco [15] trained an ABR policy via imitating expert tra- jectories to avoid redundant exploration.

**Fragmento 21 - p. 9 - score 4:**

MetaABR trained from hy- brid trace signiﬁcantly outperforms the other algorithms, which achieves the best QoE on almost all network conditions. This shows the power of meta-learning: it can learn experiences from different network conditions to improve performance and be adaptable to different scenarios. For QoEstd, a widely con- sidered metric in the literature [5], [64], the average QoE for MetaABR is 5% higher than that of Pensieve on 3G networks, and 3% ∼15% higher in other networks. The gaps between MetaABR and other methods are also found in QoEfluent and QoEhd. It is noticed that the CDFs in 4GSyd show stair-like shapes in Fig. 9, and the reason is explained as follows. Since the 4GSyd trace has very stable throughput, where over 95% Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 22 - p. 10 - score 4:**

Secondly, MetaABR is able to automatically learn suitable ABR policies with a shared meta-critic on Hybrid network environments, whereas the model-based ABR algorithms such as BBA and Robust MPC struggle to optimize for different environments and QoE objectives. Since the model-based al- gorithms employ ﬁxed control laws, they are not ﬂexible for optimizing for multiple QoE objectives with different ABR policies. For example, when network bandwidth is inadequate, the ABR algorithm should build the playback buffer as quickly aspossibleusingthelowestbitrate.Asillustratedbytheresultsin hybrid network, MetaABR is able to learn such a policy without expert involvement, while other algorithms have difﬁculty to optimize such long term strategies.

**Fragmento 23 - p. 13 - score 4:**

E. Performance on Multi-Video Scenario In this experiment, we test the pre-trained DRL models on a multi-video scenario to evaluate their ability to generalize across multiple video streaming properties. We generate the trace of multiple video streaming scenario as follows. We generate 1000 synthetic video traces with diverse bitrates, chunk sizes, and video duration. The value of bitrate is randomly chosen from {200, 300, 450, 750, 1200, 1850, 2850, 4300, 6000, 8000} Kbps. The chunk size of each video is a mean size multiplying a Gaussian distribution N(1, 0.1). The duration of each video is a random chunk number in the range [20,100]. We apply the DRL model trained with Hybrid dataset on the multi-video scenario, and the experimental results are illustrated in Fig.

**Fragmento 24 - p. 2 - score 3:**

Besides, because of its support of learning from fewer samples, it thus increases the speed of training pro- cess by limiting the necessary experiments. Finally, by learning multiple tasks, meta-learning can build more generalized models that adapt better to changing conditions. In the proposed framework, each DRL agent observes the network states including the client playback buffer occupancy, past bitrate decisions, and several raw network signals (e.g., throughput measurements), and feeds these values to its local model represented as a neural network. The client chooses a bitrate for the next video chunk based on these metrics, which Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 25 - p. 9 - score 3:**

For the WiFi dataset, we generated 1000 traces (each with 320 sec- onds) by concatenating randomly selected traces from the “Web browsing” category in the Aug 2016 collection. For the Hybrid scenario, we simply combined the throughput traces generated from the 3G, WiFi, and 4GSyd datasets together to form the dataset. We reformatted the generated throughput traces to ﬁt the Mahimahi [57] emulation platform, so that the same trace can be replayed to test different ABR algorithms. We randomly partition the generated traces into train and test datasets, where 80% of data are used for training machine learning models and 20% are used for testing all compared algorithms by default. Among the train set, 20% of data are used to form a validation set for hyperperameter tuning.

**Fragmento 26 - p. 13 - score 3:**

16. As shown in the ﬁgure, MetaABR still outperforms the baseline algorithms Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore. Restrictions apply.


### 7.8. resultados numericos metricas

Palabras clave usadas: `improvement, improve, gain, reduce, reduction, %, QoE gain, higher, lower, average, median, percentile, stall time, latency, overhead, accuracy, significant, p95, p99, score, ratio, duration`

**Fragmento 1 - p. 14 - score 6:**

(3) School Bus: the client is connected to a 4G network and it is placed on a school bus with constant movement. The CDF of QoE of different ABR algorithms under different scenarios is compared in Fig. 17, and the average QoE metrics are illustrated in Table VIII. Due to page limit, we only show the QoEstd metric for comparison. According to Fig. 17, the CDF curve of MetaABR is lower than that of other algorithms in three scenarios, which means MetaABR is concentrating on the region of higher QoEstd. According to Table VIII, in the dormitory scenario, MetaABR improves the QoE performance by 4.2% compared to Pensieve and 57.4% higher than that of RobustMPC.Similarly,signiﬁcantQoEimprovementisfoundin the library and the school bus scenarios.

**Fragmento 2 - p. 4 - score 4:**

Meta-learning helps to achieve higher model accuracy, because of its optimization of learning algorithms such as optimization of hyper parameters to achieve the best results. It also helps to learn algorithms better adapt to changing conditions by training multiple tasks to build more generalized models. At the architecture level, meta-learning is usually conceptualized as involving two learn- ing systems: a lower-level system that learns relatively quickly and is mainly responsible for adapting to new task; A slower upper-level system that can work across multiple tasks to adjust and improve lower-level systems with an objective of general- ization performance. Inside and outside the deep learning community, various methods have been explored to achieve the basic meta-learning setting [21].

**Fragmento 3 - p. 7 - score 4:**

V. EXPERIMENTS In this section, we conduct extensive experiments to evaluate the performance of MetaABR. Our experiments cover a broad set of network conditions and QoE metrics. We mainly focus on answering the following questions. (1) How does MetaABR compare to the state-of-the-art ABR algorithms in terms of video QoE? We ﬁnd that, in all of the consideredscenarios,MetaABRisabletorivaloroutperformthe best existing scheme, with average QoE improvements ranging from 3%-15%. (2) Does the MetaABR method perform more efﬁciently than other reinforcement learning methods? Through the experiment, we ﬁnd that MetaABR can achieve comparable performance with other reinforcement learning methods with much fewer samples and training epochs, and it performs the best even being transferred to a different network environment.

**Fragmento 4 - p. 9 - score 4:**

MetaABR trained from hy- brid trace signiﬁcantly outperforms the other algorithms, which achieves the best QoE on almost all network conditions. This shows the power of meta-learning: it can learn experiences from different network conditions to improve performance and be adaptable to different scenarios. For QoEstd, a widely con- sidered metric in the literature [5], [64], the average QoE for MetaABR is 5% higher than that of Pensieve on 3G networks, and 3% ∼15% higher in other networks. The gaps between MetaABR and other methods are also found in QoEfluent and QoEhd. It is noticed that the CDFs in 4GSyd show stair-like shapes in Fig. 9, and the reason is explained as follows. Since the 4GSyd trace has very stable throughput, where over 95% Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 5 - p. 10 - score 3:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2431 Fig. 7. CDF of QoE metrics (3G network). Fig. 8. CDF of QoE metrics (WiFi network). Fig. 9. CDF of QoE metrics (4Gsyd network). throughput are concentrated on 8-9 Mbps with standard de- viation less than 0.5 as shown in Fig. 6, it is easy to form a trivial solution for bitrate selection. That is, it can use full (near-constant) bandwidth to satisfy the QoE in a high level for the vast majority of ABR cases. Therefore, machine learning methods did not show signiﬁcant performance improvement compared to model-based methods in the 4GSyd datasets, and most algorithms achieve high QoEs with more than 95% of cases concentrating on a high level.

**Fragmento 6 - p. 1 - score 2:**

edu.cn; 171860540@smail.nju.edu.cn; sanglu@nju.edu.cn). Digital Object Identiﬁer 10.1109/TMC.2023.3260086 1https://www.grandviewresearch.com/industry-analysis/video-streaming- market of 21.3% from 2022 to 2030. The study from Ericsson2 reported that video streaming currently stands out as the most signiﬁcant trafﬁc type consumed by smartphone users, and it is projected to account for 74 percent of Internet trafﬁc by the end of 2024. The fundamental design of a media streaming system pays increasing attention to guarantee the users’ Quality of Experience (QoE). It was showed [1] that users started to abandon a video if it took more than 2 seconds to start up, with each incremental delay of 1 s resulting in a 5.8% increase in the abandonment rate, and a moderate amount of interruptions can decrease the average play time of a viewer by a signiﬁcant amount.

**Fragmento 7 - p. 2 - score 2:**

Fig. 3. Illustration of meta-critic based bitrate adaptation. it on different network environments in Fig. 2. As illustrated in Figs. 2(a) to (c), the model trained with multiple network traces does not improve adaptivity, and it performs even worse than those trained with a single network dataset. The poor adaptivity with mixture datasets is probably caused by dataset shift [18], [19]: the joint distribution of inputs and outputs differs between training and test stages. In our example, the DRL model trained to ﬁt data on a wide distribution (3G+WiFi+4G) and tested only on a relatively narrow distribution will result in a degradation of performance. In this article, we propose MetaABR, a novel ABR algorithm based on meta-learning to address the above challenges.

**Fragmento 8 - p. 3 - score 2:**

However, throughput can vary widely over time and result in poor ABR performance. Therefore, BBA [11] adopted a buffer-based approach which picked a bitrate based on playback buffer occupation. However, it suffered from QoE degradation during long-term bandwidth ﬂuctuations. BOLA [12] was also a buffer-based algorithm, whichturnedtheABRproblemintoautility-maximizationprob- lemandsolveditbytheLyapunovfunction.MPC[13]developed a control-theoretic framework that allowed the understanding and exploration of the trade-offs between bandwidth-based and buffer-based adaptation algorithms under different network bandwidth variations. Oboe [23] auto-tuned the parameters of model-based ABR algorithms for different network conditions to improve the ABR’s performance.

**Fragmento 9 - p. 3 - score 2:**

As shown in Section V-C3, MetaABR trains a DRL agent much faster than regular DRL methods, whose convergence time is about 1/10 of that of Pensieve. Secondly, with the proposed meta-learning method, a DRL agent can be trained to learn transferable knowledge from historical tasks, which gains the ability to be applied in unseen environment. Meta-learning has the advantage of capturing the general knowledge across similar learning tasks in the past to improve the performance of learning new tasks to achieve knowledge transfer. As shown in Sec- tionV-C2,aMeteABRmodelcanbetrainedwiththe3Gnetwork trace and then applied to the WiFi and 4G networks, whose performance is still maintained and is better than the model- based ABR algorithms such as BBA and MPC.

**Fragmento 10 - p. 4 - score 2:**

Several meta-representations had been explored in RL including learning the initial conditions [34], [35], hyperparameters [36], step directions [37], and step sizes [38], which enabled meta learning to train a neural network with fewer environmental interactions [39], [40]. In addition to conventional RL that explored environment based on sampling random actions or hand-crafted heuris- tics [41], several meta-RL studies treated exploration strategy or curiosity function as meta-knowledge, and modeled their acquisition as a meta-learning problem to improve sample ef- ﬁciency [42]. A large number of meta-RL studies considered single-task setting, where loss, reward, and hyperparameters were took as meta-knowledge to train together with the base pol- icytoimproveasinglelearningtask[43], [44], [45].

**Fragmento 11 - p. 6 - score 2:**

Noted that there are many meta-learning meth- ods such as MAML [34], MAESN [52], GrBAL/ReBAL [48], PEARL [53], etc., which we believe are also applicable to the proposed meta-learning framework for adaptive bitrate selec- tion. However, searching for the most efﬁcient meta-learning method for MetaABR is beyond the discussion of this article. The overall framework of MetaABR is illustrated in Fig. 4. It consists of a set of actor networks that learn to solve spe- ciﬁc tasks (e.g., learning an ABR algorithm for a particular network environment such as WiFi and 3G), and a global meta-critic network that learns how to effectively supervise the actors. Actor-critic is a well-known deep reinforcement learning method where an actor is a neural network used to select actions and a critic is another neural network used to learn a value function and update the actor’s policy parameters in a direction of performance improvement [50].

**Fragmento 12 - p. 9 - score 2:**

r QoEstd: q(Rn,v) = Rn, M = (1, 4.3, 1). This is the stan- dard QoE metric that had been widely used in the state-of- the-art ABR systems such as MPC [64] and Pensieve [5]. r QoEfluent: q(Rn,v) = Rn, M = (1, 8, 1). This metric emphasizes the ﬂuency of the video. It uses a much higher penalty on rebuffering time to calculate the reward, which intends to provide more ﬂuent video streaming service to the user. r QoEhd: M = (1, 8, 1). This metric favors high deﬁnition (HD) video. It adopts a q(Rn,v) mapping that assigns qual- ity scores according to the bitrates as illustrated in Table IV, where HD bitrates have signiﬁcantly higher quality score than that of non-HD bitrates. The exact values of q(Rn,v) for the QoE are provided in Table IV.

**Fragmento 13 - p. 9 - score 2:**

Since the traces of the 4GNY and 5G datasets are much smaller than that of the other datasets, we only used them for testing the adaptivity and knowledge transfer of the DRL algorithms. That is, we trained the DRL models using other datasets, and then tested the pre-trained models on the 4GNY and 5G datasets to show their performance on unseen network environments. Following similar principle, we generated 200 throughput traces each with a duration of 320 seconds by using TABLE IV THE QOE METRICS CONSIDERED IN THE EVALUATION a sliding window across the 4GNY and 5G network traces to form the test sets. 6) QoE Metrics: Similar to the literature, we consider three QoE metrics with different choices of the combination of q(Rn,v) and M.

**Fragmento 14 - p. 9 - score 2:**

2430 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 TABLE III DATASETS STATISTICS Fig. 6. Characteristics of datasets. standard deviation is less than 0.5. The reason is that 4GSyd was collectedwiththeTestSpeedAPPwhichformsstablethroughput testing from different locations. The 4GNY and 5 G datasets are more diverse, whose throughput spread from a wide range with larger deviations. For each of the above dataset, we follow the method proposed in Pensieve [5] to generate traces for reinforcement learning and to test the ABR algorithms. For the 3G and 4GSyd datasets, we generated 1000 throughput traces each with a duration of 320 seconds by using a sliding window across the network traces.

**Fragmento 15 - p. 13 - score 2:**

E. Performance on Multi-Video Scenario In this experiment, we test the pre-trained DRL models on a multi-video scenario to evaluate their ability to generalize across multiple video streaming properties. We generate the trace of multiple video streaming scenario as follows. We generate 1000 synthetic video traces with diverse bitrates, chunk sizes, and video duration. The value of bitrate is randomly chosen from {200, 300, 450, 750, 1200, 1850, 2850, 4300, 6000, 8000} Kbps. The chunk size of each video is a mean size multiplying a Gaussian distribution N(1, 0.1). The duration of each video is a random chunk number in the range [20,100]. We apply the DRL model trained with Hybrid dataset on the multi-video scenario, and the experimental results are illustrated in Fig.

**Fragmento 16 - p. 13 - score 2:**

4) Performance With Small Samples: Fig. 14 shows the re- sults of MetaABR with different percentages of training sam- ples. It is shown that even using only 10% of the total train dataset, MetaABR still has comparable performance with Pen- sieve with full dataset. D. Trade-Off Between QoE Metrics We study the trade-off between different conﬂicting QoE met- rics, and the normalized results are shown in Fig. 15. It is shown that RobustMPC achieves higher bitrate with larger rebuffering time and variation. Pensieve and BBA have modest bitrate and rebuffering time/variation. Compared to the other algorithms, MetaABR achieves the best trade-off between different QoE metrics, which is much more closer to the ideal situation.

**Fragmento 17 - p. 1 - score 1:**

Therefore, it is important for content providers to provide high-quality ﬂuent video streaming service to their users. Dynamic Adaptive Streaming over HTTP (DASH) [2] is the predominant form of video delivery in Internet. In DASH systems, videos are stored on servers as multiple chunks, each of which is encoded at several discrete bitrates, where a higher bitrate implies a higher quality and a longer download time. Adaptive bitrate (ABR) selection is the fundamental logic in video streaming that runs on the client-side video players and dynamically choose a bitrate for each video chunk to optimize users’ QoE. Selecting the right bitrate in dynamic network is challenging due to the variability of network conditions and the trade-off of conﬂicting video QoE requirements [3], [4], [5].

**Fragmento 18 - p. 2 - score 1:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2423 Fig. 1. Performance of a pre-trained DRL agent (Pensieve [5] trained on 3G dataset) testing on different network environments (details are in Section V-C2). adaptation in varying network conditions. CS2P [4] used a data-driven approach to learn clusters of similar sessions and a Hidden-Markov-Model (HMM) based midstream predictor to model the stateful evolution of throughput. Fugu [16] adopted a supervised learning approach from the server side to train a probabilistic predictor of upcoming chunk transmission times and used the prediction information to improve the control policy of MPC. A few works [5], [14], [15], [17] applied Deep Reinforcement Learning (DRL) to train an agent to generate ABR policy by interacting with the environment.

**Fragmento 19 - p. 2 - score 1:**

1(a)), whereas it performs poorly on the WiFi and 4G networks, whose QoEs (see Fig. 1(b) and (c)) are close to or lower than that of simple model-based algorithms such as BBA [11] and RobustMPC [13]. (C3) Poor adaptivity: The existing DRL models trained for a client cannot be generalized to other clients even they operate on similar environments. As a result,itishardtotrainageneralizedmodeltocopewithdifferent network types even rich historical datasets are available. For example, we use an augmented hybrid dataset combining 3G, WiFi and 4G network traces to train a DRL model and apply Fig.2. PerformanceofPensieve[5]DRLagentstrainedwithdifferentdatasets, where Hybrid means the dataset combining 3G, WiFi and 4G traces (details are in Section V-C1).

**Fragmento 20 - p. 3 - score 1:**

1) Model-Based Methods: Model-based methods estab- lished mathematical models to describe network conditions and make ABR decisions based on the estimation of available network bandwidth and playback buffer occupancy. The Probe AND Adapt (PANDA) [6] method estimated the bottleneck bandwidth and tried to eliminate the ON-OFF steady state issue aswellasreducebitrateoscillationswhenmultipleclientsshared the same bottleneck link. The piStream [7] method was a video adaptation framework for DASH clients in LTE networks that enabled clients to estimate the available bandwidth based on a resource monitor module that acted as a physical-layer daemon. FESTIVE [8] contained a bandwidth estimator module, a bitrate selection and update method that tried to avoid unfairness of stateless bitrate selection by making the player stateful, and a randomized scheduler that incorporated the buffer size to sched- ule the download of the next segment.

**Fragmento 21 - p. 3 - score 1:**

2424 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 results in a QoE metric observed and passed back to the DRL agent as a reward. The states and rewards of the tasks are passed to the meta-critic to train a meta model to supervise the agents to select suitable bitrates to maximize the QoE metric. By jointly training the DRL agents with the meta-critic, the shared meta- critic gains the ability to provide transferrable knowledge among past learning tasks, which can be applied to efﬁciently learn a new target task in unseen environment. Speciﬁcally, the proposec MetaABR can effectively address the above challenges (C1-C3) of video streaming systems. Firstly, MetaABR trains a general meta-model to teach the DRL agents to perform bitrate selection, which enables a new agent to be fastly trained on a target environment (without long bootstrap time).

**Fragmento 22 - p. 4 - score 1:**

Optimization of video streaming dilivery were also studied in the aspects of routing path assignment [29] and inter-session multiplexing congestion control [30]. Different from the existing learning based methods, the pro- posed MetaABR method introduces a novel meta-learning ap- proach with neural-enhanced bitrate selection particularly object to improve the generalization, robustness, and training efﬁciency of the deep learning based ABR methods. To the best of our knowledge, MetaABR is the ﬁrst to incorporate meta-critic into the design of ABR mechanism for video streaming. B. Meta-Learning Meta-learning, also known as learning to learn, is a machine learning method that intends to learn the general knowledge across similar learning tasks to improve its performance in new tasks based on a few examples [20], [21].

**Fragmento 23 - p. 4 - score 1:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2425 architectures including feedforward and recurrent deep neural networks to learn video adaptation strategies to achieved a good trade-off between policy optimality and convergence speed. Pensieve [5] proposed a Deep Reinforcement Learning (DRL) model that selected bitrates for future video chunks based on observations collected by DASH clients (i.e., throughput es- timation and buffer occupancy) across large video streaming experiments, which provided an expressive and scalable way to incorporate a rich variety of observations into the control policy. To address the issue of low sample efﬁciency of DRL, Comyco [15] trained an ABR policy via imitating expert tra- jectories to avoid redundant exploration.

**Fragmento 24 - p. 4 - score 1:**

Stick [17] fused the DRL method and traditional buffer-based method to output the buffer-bound, which was used to control the buffer-based approach for maximizing the QoE metrics. Fugu [16] argued that in real-world setting, it was difﬁcult for sophisticated or machine-learned control schemes to outperform a simple buffer- basedcontrolscheme,notwithstandinggoodperformanceinnet- work emulators or simulators. It used supervised learning with data from real deployment environment to train a probabilistic predictor of upcoming chunk transmission times to improve a classical control policy. Recently, learning-based methods were extended to the emerging 3D video streaming applications and video conferencing systems [24], [25], [26], [27], [28].

**Fragmento 25 - p. 4 - score 1:**

An important method was introduced by Hochreiter et al. which used standard backpropagation to train recurrent neural networks for a series of related tasks [31]. The basic process of learning each new task in Hochreiter method is completely within the dynamic range of the recurrent network, which was suitable for the structure of the task family trained across the network [32]. Reinforcement Learning (RL) learned control policies through interacting with an environment, which enabled an agent to obtain high reward in achieving a sequential action task within an environment. However, RL typically suffered from extreme sample inefﬁciency due to sparse rewards, the need of exploration, and high-variance optimization algorithms [33].

**Fragmento 26 - p. 4 - score 1:**

The details are introduced as follows. A. QoE Metrics Toimproveusers’experience,mediastreamingserviceshould consider a variety of QoE goals such as maximizing video Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore. Restrictions apply.


### 7.9. limitaciones riesgos coste

Palabras clave usadas: `limitation, limitations, future work, challenge, challenges, overhead, complexity, compute, GPU, CPU, deployment, real-world, generalization, out-of-distribution, OOD, unstable, fail, bias, sensitive, prediction error, horizon, scalability`

**Fragmento 1 - p. 1 - score 3:**

In this article, we propose a novel framework for meta-learning based ABR design and discuss challenges of deploying learning based ABR mechanism in real-world video streaming systems. We utilize the proposed framework to design MetaABR, a novel adaptive bitrate selection algorithm based on meta-reinforcement learning to maximize users’ QoE. By jointly training multiple learning tasks with a shared meta-critic, it can provide transferrable meta-knowledge to supervise bitrate selec- tion across tasks, and can be applied to efﬁciently learn a new task in unseen environment with only a few trials. We imple- ment MetaABR on an emulation platform which connects to the Linux network protocol stack through virtual network interfaces.

**Fragmento 2 - p. 2 - score 3:**

They did not rely on pre-programmed models or assumptions about the environment, and gradually learned the best policy for bitrate decisions through observation and experience. For example, Pensieve [5] is a state-of-the-art ABR scheme based on DRL. It represented its control policy as a neural network that mapped raw observations (e.g., throughput samples, playback buffer occupancy, video chunk sizes) to the bitrate decision for the next chunk, which provided an expressive and scalable way to incorporate a rich variety of observations into the ABR policy. Despite the ﬂexibility and effectiveness of the DRL-based ABR algorithms, there remain a number of challenges to de- ploy them in real-world video streaming systems.

**Fragmento 3 - p. 3 - score 3:**

Thirdly, since the meta-model is typically trained with multiple datasets from different network environments, the historical experiences can be learned by the meta-model, which can be used to supervise the training of a general agent to adapt to various environments. As shown in Section V-C1, the DRL model of MeteABR trained with a combined dataset (3G+WiFi+4G traces) clearly beats the other DRL models trained with a single dataset. The contribution of our work are summarized as follows. r We formulate a novel framework for meta-learning based adaptive bitrate selection design. We discuss the challenges of deploying DRL-based ABR mechanism in real-world video streaming systems, which are not trivial to address within conventional DRL formalism.

**Fragmento 4 - p. 4 - score 3:**

Stick [17] fused the DRL method and traditional buffer-based method to output the buffer-bound, which was used to control the buffer-based approach for maximizing the QoE metrics. Fugu [16] argued that in real-world setting, it was difﬁcult for sophisticated or machine-learned control schemes to outperform a simple buffer- basedcontrolscheme,notwithstandinggoodperformanceinnet- work emulators or simulators. It used supervised learning with data from real deployment environment to train a probabilistic predictor of upcoming chunk transmission times to improve a classical control policy. Recently, learning-based methods were extended to the emerging 3D video streaming applications and video conferencing systems [24], [25], [26], [27], [28].

**Fragmento 5 - p. 14 - score 3:**

In summary, MetaABR achieves the highest QoE in all three real-world scenarios, and its rebufﬁng time and variations are much lower than that of the baseline algorithms. VI. CONCLUSION In this article, we addressed the challenges of deploying learning based ABR mechanism in real-world video streaming systems, and proposed a novel framework for meta-learning Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 6 - p. 1 - score 2:**

Conventional ABR algorithms adopted a model-based ap- proach that used mathematical models to describe network conditions and made bitrate decisions based on the estimation of network throughput [6], [7], [8], [9], [10] and playback buffer occupancy [11], [12]. For example, FESTIVE [8] used the harmonic mean of download speed over recent chunks to predict the throughput and proposed a stateful bitrate selection to compensate for the biased interaction between bitrate and estimated bandwidth. BBA [11] was a buffer-based approach which selected bitrates based on playback buffer occupation and estimation of future capacity from past observations. MPC [13] developed a model predictive control algorithm that combined both throughput estimates and buffer occupancy information to select bitrates to maximize QoE over a horizon of several future chunks.

**Fragmento 7 - p. 2 - score 2:**

Fig. 3. Illustration of meta-critic based bitrate adaptation. it on different network environments in Fig. 2. As illustrated in Figs. 2(a) to (c), the model trained with multiple network traces does not improve adaptivity, and it performs even worse than those trained with a single network dataset. The poor adaptivity with mixture datasets is probably caused by dataset shift [18], [19]: the joint distribution of inputs and outputs differs between training and test stages. In our example, the DRL model trained to ﬁt data on a wide distribution (3G+WiFi+4G) and tested only on a relatively narrow distribution will result in a degradation of performance. In this article, we propose MetaABR, a novel ABR algorithm based on meta-learning to address the above challenges.

**Fragmento 8 - p. 3 - score 2:**

2424 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 results in a QoE metric observed and passed back to the DRL agent as a reward. The states and rewards of the tasks are passed to the meta-critic to train a meta model to supervise the agents to select suitable bitrates to maximize the QoE metric. By jointly training the DRL agents with the meta-critic, the shared meta- critic gains the ability to provide transferrable knowledge among past learning tasks, which can be applied to efﬁciently learn a new target task in unseen environment. Speciﬁcally, the proposec MetaABR can effectively address the above challenges (C1-C3) of video streaming systems. Firstly, MetaABR trains a general meta-model to teach the DRL agents to perform bitrate selection, which enables a new agent to be fastly trained on a target environment (without long bootstrap time).

**Fragmento 9 - p. 4 - score 2:**

Afewrecent works designed meta-RL generalizations for the conventional off-policy RL methods to accelerate the training and testing by replaying buffer samples from meta-training [46], [47]. It had been demonstrated that meta-RL was successfully applied in real-world physical robot [48], imitation learning [49], etc. III. META-LEARNING BASED BITRATE ADAPTATION MECHANISM In this section, we propose a meta-learning based bitrate adap- tation mechanism called MetaABR. We ﬁrst provide quantiﬁed description of QoE metrics, then formulate the ABR problem as a deep reinforcement learning task, which can be solved with a meta-reinforcement learning framework. The key notations used throughout the paper are summarized in Table I.

**Fragmento 10 - p. 1 - score 1:**

Extensive experiments based on real-world traces and wireless testbed show that MetaABR achieves the best comprehensive QoE compared with the state-of-the-art ABR algorithms in a variety of network environments. Index Terms—Bitrate adaptation, meta-learning, reinforcement learning, video streaming. I. INTRODUCTION R ECENT years have witnessed a rapid growth of Internet video streaming applications. Video on demand (VoD) ser- vices have stimulated a revolution in video content consumption by providing audiences a platform to watch whatever they want anytime. According to the report,1 the global video streaming market size was valued at USD 70.59 billion in 2022, and is expected to expand at a compound annual growth rate (CAGR) Manuscriptreceived7May2022;revised26February2023;accepted7March 2023.

**Fragmento 11 - p. 1 - score 1:**

However, model-based ABR algorithms failed to achieve optimal performance across a broad set of network conditions and QoE objectives due to their ﬁxed control rules. In recent years, learning-based ABR algorithms [4], [5], [14], [15], [16] were proposed to address the issues of bitrate 2https://www.ericsson.com/en/reports-and-papers/mobility-report/articles/ streaming-video 1536-1233 © 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 12 - p. 3 - score 1:**

2) Learning-Based Methods: Since model-based algorithms failed to achieve optimal performance across a broad set of network conditions and QoE objectives because of their ﬁxed controlrules,thelearning-basedmethods[4],[5],[14],[15],[16] were proposed to learn personalized ABR strategies for various conditions. Based on the observation that video sessions sharing similar key features presented similar initial throughput values and dynamic patterns, the CS2P [4] method used a data-driven approach to learn clusters of similar sessions, and proposed a Hidden-Markov-Model (HMM) based midstream predictor to model the stateful evolution of throughput for bitrate adaptation. D-DASH [14] formulated the DASH video streaming problem within a Deep Q-learning framework, and used mixed learning Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 13 - p. 3 - score 1:**

r We utilize the proposed framework to design MetaABR, a novel adaptive bitrate selection algorithm based on meta- learning to maximize users’ QoE. By jointly training mul- tiple learning tasks with a shared meta-critic, it has the ability to provide transferrable knowledge to supervise bitrate selection, and can be applied to efﬁciently learn a new task in unseen environment with much fewer data samples and trainng epoches. r We implement the proposed MetaABR based on an emula- tionplatformwhichconnectstotheLinuxnetworkprotocol stack through a virtual network interface to send real data packets for evaluation. Extensive experiments based on real-world traces show that MetaABR achieves the best comprehensive QoE compared with the state-of-the-art ABR algorithms in a variety of network environments.

**Fragmento 14 - p. 4 - score 1:**

Optimization of video streaming dilivery were also studied in the aspects of routing path assignment [29] and inter-session multiplexing congestion control [30]. Different from the existing learning based methods, the pro- posed MetaABR method introduces a novel meta-learning ap- proach with neural-enhanced bitrate selection particularly object to improve the generalization, robustness, and training efﬁciency of the deep learning based ABR methods. To the best of our knowledge, MetaABR is the ﬁrst to incorporate meta-critic into the design of ABR mechanism for video streaming. B. Meta-Learning Meta-learning, also known as learning to learn, is a machine learning method that intends to learn the general knowledge across similar learning tasks to improve its performance in new tasks based on a few examples [20], [21].

**Fragmento 15 - p. 4 - score 1:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2425 architectures including feedforward and recurrent deep neural networks to learn video adaptation strategies to achieved a good trade-off between policy optimality and convergence speed. Pensieve [5] proposed a Deep Reinforcement Learning (DRL) model that selected bitrates for future video chunks based on observations collected by DASH clients (i.e., throughput es- timation and buffer occupancy) across large video streaming experiments, which provided an expressive and scalable way to incorporate a rich variety of observations into the control policy. To address the issue of low sample efﬁciency of DRL, Comyco [15] trained an ABR policy via imitating expert tra- jectories to avoid redundant exploration.

**Fragmento 16 - p. 5 - score 1:**

Meanwhile, we need to ensure a ﬂuent playback and minimize the rebuffering time of every chunk, which is computed by: QoEv reb = N  n=1 Tn,v, (2) where Tn,v is the rebuffering time that results from downloading chunk n at bitrate Rn,v. Besides, the streaming strategy should reduce sudden and fre- quent quality variations, which may impose negative experience for users. Variation of video quality is calculated by: QoEv var = N−1  n=1 |q(Rn+1,v) −q(Rn, v)|, (3) which penalizes changes in video quality to favor smoothness. Overall objective: The overall objective in a comprehensive QoE metric is a weighted sum of the three metrics on video v, which is deﬁned as QoEv = μ1QoEv hd −μ2QoEv reb −μ3QoEv var, (4) where M = (μ1, μ2, μ3) is a set of non-negative weighting parameters corresponding to users’ preference on the video quality, rebuffering time, and variation, respectively.

**Fragmento 17 - p. 5 - score 1:**

C. Solution With a Meta-Learning Framework As discussed in Section I, conventional deep reinforcement learning for ABR selection has the drawbacks of efﬁciency, generalization and robustness. To overcome the performance issues, we propose a novel meta reinforcement learning (MRL) based method called MetaABR for bitrate adaptation in video streaming. In the proposed framework, we apply the A3C Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 18 - p. 8 - score 1:**

In 3https://github.com/Dash-Industry-Forum/dash.js/, Akamai, 2020. our settings, the client video player is Google Chrome (version 85) and chromedriver (version 85.0.4183.38). The video server is Apache (version 2.4.7). We use Mahimahi [57] to emulate network environments from the network traces between the client and the server with 80 ms RTT. 5) Datasets and Network Traces: To evaluate the ABR algo- rithms on realistic network conditions, we created a corpus of network traces using several real-world network communication datasets. r 3 G [59]: This dataset was collected from popular commute routes in and around Oslo (Norway). It includes throughput measurements of real-world adaptive HTTP streaming per- formed over 3G networks using mobile devices traveling with different types of public transportation (metro, tram, train, bus and ferry).

**Fragmento 19 - p. 8 - score 1:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2429 TABLE II THE LAYER PARAMETERS OF METAABR reward discount factor γ = 0.99 by default. The neural network structure of MetaABR is illustrated in Table II. 2) Evaluation Platform: The experiments are conducted on a PC server (CPU: Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20 GHz; Memory: 32 GB DDR4 2400Mhz*4; OS: 64-bit Ubuntu 16.04). We implement the proposed MetaABR frame- work based on the Mahimahi [57] emulation platform, which is connected to the Linux network protocol stack through a virtual network interface and sends real data packets. Mahimahi can be used to record trafﬁc from HTTP-based applications and replay it under emulated network conditions, which is ideal for fair comparison of different ABR algorithms for video streaming.

**Fragmento 20 - p. 8 - score 1:**

The throughput of the 4G network ranges from 5 ∼10 Mbps. r Hybrid (3G + WiFi + 4GSyd): We combine the data sampes of the above 3G, WiFi, and 4GSyd datasets to generateahybriddataset.Itsimulatesthereal-lifescenarios where three networks are dynamically switching due to the mobility of smartphones. The performance in this dataset can well reﬂect the generalization ability of the ABR method. r 4GNY [62]: This dataset was collected on New York City MTA bus and subway. The data was recorded with a mobile phone running iPerf to log TCP throughput every 1000 milliseconds. The throughput of the network environment is between 1 ∼108 Mbps. r 5 G [63]: This dataset was collected from a major Irish mobile operator.

**Fragmento 21 - p. 8 - score 1:**

It was generated from two mobility pat- terns (static and car) across two application patterns (video streaming and ﬁle download). It consists of two parts: the ﬁrst is a production dataset collected from real-world and the second is synthetic data generated from a large-scale multi-cell 5G/mmwave ns-3 platform. We selected the data generated from the Amazon Prime and Netﬂix streaming services in the experiments, and the throughput of the 5G network is in the range of 3 ∼202.5 Mbps. The basic information of the datasets are listed in Table III. The statistical characteristics of the datasets are shown in Fig. 6. According to the ﬁgure, both 3G and WiFi traces have small throughput and low variations.

**Fragmento 22 - p. 14 - score 1:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2435 Fig. 16. CDF of QoE metrics of multi-video scenario testing on WiFi network. Fig. 17. CDF of QoEstd metrics under real-world network scenarios. TABLE VIII COMPARISON OF AVERAGE BITRATE (MBPS), REBUFFERING TIME (SECOND), VARIATIONS, AND QoEstd METRIC ON REAL-WORLD SCENARIOS on a variety of QoE metrics, and signiﬁcant performance im- provement is found in the QoEfluent metric. The results suggest that MetaABR can be adapted to the multiple video streaming scenarios with diverse QoE properties. F. Performance on Real-World Scenarios Apartfromtrace-drivenexperiments,wedeploythecompared algorithms in a wireless network testbed to test the performance under real-world scenarios.

**Fragmento 23 - p. 14 - score 1:**

We use a laptop (lenovo savior y7000, windows 10) as client, and it connects to a HUAWEI P20 (Harmony 2.0.0) smartphone which is used as a proxy to establish Wi-Fi or 4G connections. The laptop uses a Chrome browser to access video-on-demand service from a media server (Intel(R) Xeon(R) CPU E5-2630v4@2.20 GHz; 32 GB DDR4 2400 Mhz*4; 64-bit Ubuntu 16.04), and the ABR algorithms are implemented in dash.js that is used by the player for adaptive bitrate selection. We conduct experiments based on three real- world scenarios. (1) Dormitory: the client is almost static in a university dormitory and it connects to a small WiFi network. (2) Library: the client is connected to a library WiFi network with many users around and occasional movement.

**Fragmento 24 - p. 15 - score 1:**

21, pp. 2001–2014, Dec. 2013. [2] T. Stockhammer, “Dynamic adaptive streaming over HTTP: Standards and design principles,” in Proc. 2nd Annu. ACM Conf. Multimedia Syst., 2011, pp. 133–144. [3] T.-Y. Huang, N. Handigol, B. Heller, N. McKeown, and R. Johari, “Con- fused, timid, and unstable: Picking a video streaming rate is hard,” in Proc. Internet Meas. Conf., 2012, pp. 225–238. [4] Y. Sun et al., “CS2P: Improving video bitrate selection and adaptation with data-driven throughput prediction,” in Proc. ACM SIGCOMM Conf., 2016, pp. 272–285. [5] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video streaming with pensieve,” in Proc. Conf. ACM Special Int. Group Data Commun., 2017, pp. 197–210. [6] Z. Li et al., “Probe and adapt: Rate adaptation for HTTP video streaming at scale,” IEEE J.

**Fragmento 25 - p. 15 - score 1:**

2436 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 based ABR design. Based on the proposed framework, we proposed MetaABR, a novel adaptive bitrate selection algorithm based on meta-critic to maximize users’ QoE. MetaABR jointly trained multiple learning tasks with a shared meta-critic, and it could provide transferrable knowledge to supervise bitrate se- lection across tasks. Extensive experiments based on real-world traces and testbed showed that MetaABR achieved the best QoE compared with the state-of-the-arts. REFERENCES [1] S. Krishnan and R. Sitaraman, “Video stream quality impacts viewer be- havior: Inferring causality using quasi-experimental designs,” IEEE/ACM Trans. Netw., vol.

**Fragmento 26 - p. 15 - score 1:**

[48] A. Nagabandi et al., “Learning to adapt in dynamic, real-world environ- ments through meta-reinforcement learning,” 2018, arXiv:1803.11347. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore. Restrictions apply.


### 7.10. ideas fase45 v1 controller defendible

Palabras clave usadas: `risk, safe, safety, robust, conservative, fallback, uncertainty, capacity, lower bound, tail, severe, low buffer, volatile, variable, fluctuation, drop, zero, consistent, smoothness, auto-tuning, regime, cluster, guidance, hybrid, generalization, environment-aware, prediction, selector`

**Fragmento 1 - p. 2 - score 3:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2423 Fig. 1. Performance of a pre-trained DRL agent (Pensieve [5] trained on 3G dataset) testing on different network environments (details are in Section V-C2). adaptation in varying network conditions. CS2P [4] used a data-driven approach to learn clusters of similar sessions and a Hidden-Markov-Model (HMM) based midstream predictor to model the stateful evolution of throughput. Fugu [16] adopted a supervised learning approach from the server side to train a probabilistic predictor of upcoming chunk transmission times and used the prediction information to improve the control policy of MPC. A few works [5], [14], [15], [17] applied Deep Reinforcement Learning (DRL) to train an agent to generate ABR policy by interacting with the environment.

**Fragmento 2 - p. 2 - score 3:**

1(a)), whereas it performs poorly on the WiFi and 4G networks, whose QoEs (see Fig. 1(b) and (c)) are close to or lower than that of simple model-based algorithms such as BBA [11] and RobustMPC [13]. (C3) Poor adaptivity: The existing DRL models trained for a client cannot be generalized to other clients even they operate on similar environments. As a result,itishardtotrainageneralizedmodeltocopewithdifferent network types even rich historical datasets are available. For example, we use an augmented hybrid dataset combining 3G, WiFi and 4G network traces to train a DRL model and apply Fig.2. PerformanceofPensieve[5]DRLagentstrainedwithdifferentdatasets, where Hybrid means the dataset combining 3G, WiFi and 4G traces (details are in Section V-C1).

**Fragmento 3 - p. 4 - score 2:**

Optimization of video streaming dilivery were also studied in the aspects of routing path assignment [29] and inter-session multiplexing congestion control [30]. Different from the existing learning based methods, the pro- posed MetaABR method introduces a novel meta-learning ap- proach with neural-enhanced bitrate selection particularly object to improve the generalization, robustness, and training efﬁciency of the deep learning based ABR methods. To the best of our knowledge, MetaABR is the ﬁrst to incorporate meta-critic into the design of ABR mechanism for video streaming. B. Meta-Learning Meta-learning, also known as learning to learn, is a machine learning method that intends to learn the general knowledge across similar learning tasks to improve its performance in new tasks based on a few examples [20], [21].

**Fragmento 4 - p. 5 - score 2:**

C. Solution With a Meta-Learning Framework As discussed in Section I, conventional deep reinforcement learning for ABR selection has the drawbacks of efﬁciency, generalization and robustness. To overcome the performance issues, we propose a novel meta reinforcement learning (MRL) based method called MetaABR for bitrate adaptation in video streaming. In the proposed framework, we apply the A3C Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 5 - p. 8 - score 2:**

3) Baseline Algorithms: We compare MetaABR with three state-of-the-art ABR algorithms: r BBA [11]: a buffer-based approach which selects bitrates based on playback buffer occupation. r RobustMPC [13]: a model predictive control algorithm that combines both throughput estimates and buffer occupancy information to select bitrates. r Pensieve [5]: a state-of-the-art ABR scheme based on deep reinforcement learning. r BayesMPC [58]: an uncertainty-aware robust ABR algo- rithm based on Bayesian neural network (BNN) and model predictive control (MPC). r Comyco [15]: a video quality-aware ABR approach lever- aging imitation learning to accelerate the training process for ABR tasks. Note that we do not compare with other deep learning based ABR algorithms such as Fugu [16], Oboe [23], and Stick [17], since either they are implemented on the server side, or there are lack of open-source code to reproduce their work.

**Fragmento 6 - p. 8 - score 2:**

4) Video Parameters: We have modiﬁed dash.js3 to sup- port MetaABR and the above baseline ABR algorithms. For MetaABR, Pensieve, and RobustMPC, we conﬁgure dash.js to obtain the bitrate selection decision from an ABR process that implements the corresponding algorithm. The DASH player is conﬁgured to have a playback buffer capacity of 60 seconds. Our evaluation used the “Envivio-Dash3” video of the DASH-246 JavaScript reference client. In addition, the video is divided into 48 blocks with a total length of 193 seconds. This video is encoded by the H.264/MPEG-4 codec at bitrates in 300, 750, 1200,1850,2850,4300kbps(whichcorrespondstovideomodes in 240p, 360p, 480p, 720p, 1080p, 1440p). Therefore, each block represents approximately 4 seconds of video playback.

**Fragmento 7 - p. 8 - score 2:**

The throughput of the 4G network ranges from 5 ∼10 Mbps. r Hybrid (3G + WiFi + 4GSyd): We combine the data sampes of the above 3G, WiFi, and 4GSyd datasets to generateahybriddataset.Itsimulatesthereal-lifescenarios where three networks are dynamically switching due to the mobility of smartphones. The performance in this dataset can well reﬂect the generalization ability of the ABR method. r 4GNY [62]: This dataset was collected on New York City MTA bus and subway. The data was recorded with a mobile phone running iPerf to log TCP throughput every 1000 milliseconds. The throughput of the network environment is between 1 ∼108 Mbps. r 5 G [63]: This dataset was collected from a major Irish mobile operator.

**Fragmento 8 - p. 10 - score 2:**

Secondly, MetaABR is able to automatically learn suitable ABR policies with a shared meta-critic on Hybrid network environments, whereas the model-based ABR algorithms such as BBA and Robust MPC struggle to optimize for different environments and QoE objectives. Since the model-based al- gorithms employ ﬁxed control laws, they are not ﬂexible for optimizing for multiple QoE objectives with different ABR policies. For example, when network bandwidth is inadequate, the ABR algorithm should build the playback buffer as quickly aspossibleusingthelowestbitrate.Asillustratedbytheresultsin hybrid network, MetaABR is able to learn such a policy without expert involvement, while other algorithms have difﬁculty to optimize such long term strategies.

**Fragmento 9 - p. 11 - score 2:**

The results are shown in Table VI, Figs. 11 and 12. Clearly MetaABR(Hybrid) achieves the best QoEs in most cases, and it beats the personally trained method Comyco on most QoE metrics, thanks to its power of knowledge transfer from other learning tasks. Pensieve(Hybrid) performs close to or worse than the model-based methods such as BBA and RobustMPC, which shows poor ability of knowledge transfer without meta-learning. To test whether the training knowledge from single dataset is transferable to multiple datasets, we train both MetaABR and Pensieve on the 3G dataset, and then apply the pre-trained model to the rest networks. The results are shown in Table VII. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 10 - p. 12 - score 2:**

LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING 2433 TABLE VI COMPARISON OF QOE METRICS FOR TRANSFERRING A PRE-TRAINED MODEL TO UNSEEN NETWORK ENVIRONMENTS, WHERE METAABR(HYBRID) MEANS A METAABR MODEL TRAINED WITH THE Hybrid DATASET, AND SO ARE THE REST Fig. 11. CDF of QoE metrics (Train set: Hybrid; Test set: 4GNY ). Fig. 12. CDF of QoE metrics (Train set: Hybrid; Test set: 5G). TABLE VII COMPARISON OF QoEstd METRIC FOR TRANSFERRING A PRE-TRAINED MODEL ON 3G DATASET TO MULTIPLE NETWORK ENVIRONMENTS According to the table, both MetaABR and Pensieve perform well in 3G network (where train and test environment are the same). After applying to other networks, Pensieve performs worse than the model-based approaches BBA and RobustMPC, Fig.

**Fragmento 11 - p. 16 - score 2:**

Netravali et al., “Mahimahi: Accurate record-and-replay for HTTP,” in Proc. USENIX Annu. Tech. Conf., 2015, pp. 417–429. [58] N. Kan, C. Li, C. Yang, W. Dai, J. Zou, and H. Xiong, “Uncertainty-aware robust adaptive video streaming with bayesian neural network and model predictive control,” in Proc. 31st ACM Workshop Netw. Operating Syst. Support Digit. Audio Video, 2021, pp. 17–24. [59] H. Riiser, P. Vigmostad, C. Griwodz, and P. Halvorsen, “Commute path bandwidth traces from 3G networks: Analysis and applications,” in Proc. 4th ACM Multimedia Syst. Conf., 2013, pp. 114–118. [60] “Raw data - measuring broadband America2016,” 2021. [Online]. Available: https://www.fcc.gov/reports-research/reports/measuring- broadband-america/raw-data-measuring-broadband-america-2016 [61] A.

**Fragmento 12 - p. 1 - score 1:**

Conventional ABR algorithms adopted a model-based ap- proach that used mathematical models to describe network conditions and made bitrate decisions based on the estimation of network throughput [6], [7], [8], [9], [10] and playback buffer occupancy [11], [12]. For example, FESTIVE [8] used the harmonic mean of download speed over recent chunks to predict the throughput and proposed a stateful bitrate selection to compensate for the biased interaction between bitrate and estimated bandwidth. BBA [11] was a buffer-based approach which selected bitrates based on playback buffer occupation and estimation of future capacity from past observations. MPC [13] developed a model predictive control algorithm that combined both throughput estimates and buffer occupancy information to select bitrates to maximize QoE over a horizon of several future chunks.

**Fragmento 13 - p. 3 - score 1:**

2) Learning-Based Methods: Since model-based algorithms failed to achieve optimal performance across a broad set of network conditions and QoE objectives because of their ﬁxed controlrules,thelearning-basedmethods[4],[5],[14],[15],[16] were proposed to learn personalized ABR strategies for various conditions. Based on the observation that video sessions sharing similar key features presented similar initial throughput values and dynamic patterns, the CS2P [4] method used a data-driven approach to learn clusters of similar sessions, and proposed a Hidden-Markov-Model (HMM) based midstream predictor to model the stateful evolution of throughput for bitrate adaptation. D-DASH [14] formulated the DASH video streaming problem within a Deep Q-learning framework, and used mixed learning Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 14 - p. 3 - score 1:**

The rest of the paper is organized as follows. Section II intro- duces the related works of media streaming bitrate adaptation methods and meta learning algorithms. Section III presents the detailed mechanism of bitrate adaptation based on meta learn- ing. Section IV proposes the training method for the proposed meta-critic and task-speciﬁc actors. Section V evaluates the system performance with extensive experiments. The paper is concluded in Section VI. II. RELATED WORK In this section, we introduce the related works in terms of ABR schemes for video streaming and meta learning. A. ABR Schemes for Video Streaming The ABR schemes for video streaming can be classiﬁed into two categories: the model-based and the learning-based methods.

**Fragmento 15 - p. 4 - score 1:**

Swift [24] adopted a layered encoder that learns to compress a video frame into layered codes and proposed an ABR protocol based on detecting available bandwidth and client-side capacity. YuZu [25] adopted a neural-enhanced method for intra- and inter-frame optimizations using 3D super resolution to increase the visual quality of volumetric video streaming. Vues [26] was an edge-assisted transcoding system that transcoded a volu- metric video frame into multiple 2D views using lightweight machine learning models and adaptively selected the view that optimized the QoE for mobile clients. GSO-Simulcast [27] was a multi-party video-conferencing system where a media server globally coordinated the publishing and subscribing to decide the resolution and bitrate of video streams for each participant.

**Fragmento 16 - p. 4 - score 1:**

Afewrecent works designed meta-RL generalizations for the conventional off-policy RL methods to accelerate the training and testing by replaying buffer samples from meta-training [46], [47]. It had been demonstrated that meta-RL was successfully applied in real-world physical robot [48], imitation learning [49], etc. III. META-LEARNING BASED BITRATE ADAPTATION MECHANISM In this section, we propose a meta-learning based bitrate adap- tation mechanism called MetaABR. We ﬁrst provide quantiﬁed description of QoE metrics, then formulate the ABR problem as a deep reinforcement learning task, which can be solved with a meta-reinforcement learning framework. The key notations used throughout the paper are summarized in Table I.

**Fragmento 17 - p. 4 - score 1:**

The details are introduced as follows. A. QoE Metrics Toimproveusers’experience,mediastreamingserviceshould consider a variety of QoE goals such as maximizing video Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 18 - p. 5 - score 1:**

2426 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 TABLE I NOTATIONS quality, minimizing rebuffering time, and maintaining video quality smoothness (i.e., avoiding constant bitrate ﬂuctuations). For a satisfactory user-perceived QoE, ABR algorithm needs to optimize several conﬂicting goals. For example, increasing the bitrate may lead to longer rebuffering time. There exists signiﬁcant variance in user preferences for video streaming QoE. To formulate the problem, we adopt the quantiﬁcation of QoE metrics as introduced in [13]. Speciﬁcally, users tend to prefer great average quality per chunk for high-deﬁnition content, which can be calculated on the mean of n-th chunk of video v by: QoEv hd = N  n=1 q(Rn,v), (1) where Rn,v is the bitrate of chunk n of video v, and q(·) is a non-decreasing function which maps the selected bitrate to the video quality perceived by user.

**Fragmento 19 - p. 5 - score 1:**

Meanwhile, we need to ensure a ﬂuent playback and minimize the rebuffering time of every chunk, which is computed by: QoEv reb = N  n=1 Tn,v, (2) where Tn,v is the rebuffering time that results from downloading chunk n at bitrate Rn,v. Besides, the streaming strategy should reduce sudden and fre- quent quality variations, which may impose negative experience for users. Variation of video quality is calculated by: QoEv var = N−1  n=1 |q(Rn+1,v) −q(Rn, v)|, (3) which penalizes changes in video quality to favor smoothness. Overall objective: The overall objective in a comprehensive QoE metric is a weighted sum of the three metrics on video v, which is deﬁned as QoEv = μ1QoEv hd −μ2QoEv reb −μ3QoEv var, (4) where M = (μ1, μ2, μ3) is a set of non-negative weighting parameters corresponding to users’ preference on the video quality, rebuffering time, and variation, respectively.

**Fragmento 20 - p. 6 - score 1:**

To achieve this, the meta-critic is further divided into a task-conﬁg network and a critic network as shown in Fig. 4. The task-conﬁg network takes the past trails of a RL task represented by a trajectory of the state, action, and reward as input to learn historical experience, and it outputs a task-actor embedding z which represents the task-speciﬁc features. The critic network uses the current (state, action) and the task-actor embedding z from the task-conﬁg network as input to approximate the reward for a RL task, where z serves as the meta-knowledge to decide how to criticise the current actor on the speciﬁc task. The training details are given in Section IV. By jointly training the meta-critic with multiple actors, the meta-critic gains the ability to correctly criticise a new task based on the provided task-conﬁg network.

**Fragmento 21 - p. 6 - score 1:**

IV. TRAINING METHODS In this section, we introduce the methods of training the meta- critic and the task-speciﬁc actors in detail. A. Training the Meta-Critic In the proposed framework, we want to train a single meta- critic that can criticise any actor to perform any task. This requires two generalisations (task and actor conditioning) com- pared to conventional critic networks that criticise a speciﬁc actor for a speciﬁc task. The structure of the meta-critic is illus- trated in Fig. 5, which consists of two subnetworks: a task-conﬁg network and a critic network. The task-conﬁg network Cω, parameterised by ω, has a three- layer neural network structure. It takes the past k trails of (state, action, reward) triplets as input to learn task-speciﬁc experience.

**Fragmento 22 - p. 9 - score 1:**

For the WiFi dataset, we generated 1000 traces (each with 320 sec- onds) by concatenating randomly selected traces from the “Web browsing” category in the Aug 2016 collection. For the Hybrid scenario, we simply combined the throughput traces generated from the 3G, WiFi, and 4GSyd datasets together to form the dataset. We reformatted the generated throughput traces to ﬁt the Mahimahi [57] emulation platform, so that the same trace can be replayed to test different ABR algorithms. We randomly partition the generated traces into train and test datasets, where 80% of data are used for training machine learning models and 20% are used for testing all compared algorithms by default. Among the train set, 20% of data are used to form a validation set for hyperperameter tuning.

**Fragmento 23 - p. 11 - score 1:**

As illustrated in Table V, MetaABR(Hybrid) performs close or better than those models personally trained on speciﬁc networks. For example, MetaABR(Hybrid) outperforms MetaABR(WiFi) on the WiFi network, and outperforms MetaABR(4GSyd) on the 4G network, which generally achieves the best perfor- mance on all test datasets. On the other hand, conventional DRL method such as Pensieve has poor adaptivity, e.g., Pen- sieve(Hybrid) clearly performs much worse than Pensieve(3G) and Pensieve(WiFi) on the corresponding datasets. 2) Ability of Knowledge Transfer: We then test the ability of knowledge transfer. Similar to the experiments in Section V-B, we use the Hybrid dataset to pre-train a DRL model, and apply the model to unseen networks (i.e., 4GNY and 5G) to test its performance.

**Fragmento 24 - p. 11 - score 1:**

2432 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024 Fig. 10. CDF of QoE metrics (Hybrid network). TABLE V COMPARISON OF AVERAGE BITRATE (MBPS), REBUFFERING TIME (SECOND), VARIATIONS, AND THEIR CORRESPONDING QOE METRICS ON DIFFERENT NETWORK ENVIRONMENTS, WHERE METAABR(HYBRID) MEANS A METAABR MODEL TRAINED WITH THE Hybrid DATASET, AND SO ARE THE REST C. Effectiveness of Meta-Critic Learning 1) Adaptivity: The major advantage of MetaABR is its adap- tivity on different network traces, which enables a machine learning ABR algorithm to learn once and be applied to any- where. With the proposed meta-learning method we can train a general model MetaABR(Hybrid) based on the Hybrid dataset and then apply it to the other networks without modiﬁcation.

**Fragmento 25 - p. 13 - score 1:**

E. Performance on Multi-Video Scenario In this experiment, we test the pre-trained DRL models on a multi-video scenario to evaluate their ability to generalize across multiple video streaming properties. We generate the trace of multiple video streaming scenario as follows. We generate 1000 synthetic video traces with diverse bitrates, chunk sizes, and video duration. The value of bitrate is randomly chosen from {200, 300, 450, 750, 1200, 1850, 2850, 4300, 6000, 8000} Kbps. The chunk size of each video is a mean size multiplying a Gaussian distribution N(1, 0.1). The duration of each video is a random chunk number in the range [20,100]. We apply the DRL model trained with Hybrid dataset on the multi-video scenario, and the experimental results are illustrated in Fig.

**Fragmento 26 - p. 13 - score 1:**

4) Performance With Small Samples: Fig. 14 shows the re- sults of MetaABR with different percentages of training sam- ples. It is shown that even using only 10% of the total train dataset, MetaABR still has comparable performance with Pen- sieve with full dataset. D. Trade-Off Between QoE Metrics We study the trade-off between different conﬂicting QoE met- rics, and the normalized results are shown in Fig. 15. It is shown that RobustMPC achieves higher bitrate with larger rebuffering time and variation. Pensieve and BBA have modest bitrate and rebuffering time/variation. Compared to the other algorithms, MetaABR achieves the best trade-off between different QoE metrics, which is much more closer to the ideal situation.


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
2422
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024
MetaABR: A Meta-Learning Approach on
Adaptative Bitrate Selection for Video Streaming
Wenzhong Li
, Member, IEEE, Xiang Li, Yeting Xu, Yi Yang, and Sanglu Lu
, Member, IEEE
Abstract—Video streaming is one of the most popular Internet
applications that makes up a large amount of Internet trafﬁc. A
fundamental mechanism in video streaming is adaptive bitrate
(ABR) selection which decides the proper compression level for
each chunk of a video to optimize the users’ quality of experience
(QoE). The existing ABR algorithms require signiﬁcant tuning and
do not generalize to diverse network conditions and personalized
QoE objectives. In this article, we propose a novel framework
for meta-learning based ABR design and discuss challenges of
deploying learning based ABR mechanism in real-world video
streaming systems. We utilize the proposed framework to design
MetaABR, a novel adaptive bitrate selection algorithm based on
meta-reinforcement learning to maximize users’ QoE. By jointly
training multiple learning tasks with a shared meta-critic, it can
provide transferrable meta-knowledge to supervise bitrate selec-
tion across tasks, and can be applied to efﬁciently learn a new
task in unseen environment with only a few trials. We imple-
ment MetaABR on an emulation platform which connects to the
Linux network protocol stack through virtual network interfaces.
Extensive experiments based on real-world traces and wireless
testbed show that MetaABR achieves the best comprehensive QoE
compared with the state-of-the-art ABR algorithms in a variety of
network environments.
Index Terms—Bitrate adaptation, meta-learning, reinforcement
learning, video streaming.
I. INTRODUCTION
R
ECENT years have witnessed a rapid growth of Internet
video streaming applications. Video on demand (VoD) ser-
vices have stimulated a revolution in video content consumption
by providing audiences a platform to watch whatever they want
anytime. According to the report,1 the global video streaming
market size was valued at USD 70.59 billion in 2022, and is
expected to expand at a compound annual growth rate (CAGR)
Manuscriptreceived7May2022;revised26February2023;accepted7March
2023. Date of publication 21 March 2023; date of current version 5 February
2024. This work was partially supported by the Natural Science Foundation of
Jiangsu Province Project “Research on Frontier Basic Theory and Method of
Security Defense for Power Systems with High-dimensional Uncertain Factors”
under Grant BK20222003, in part by the National Natural Science Foundation of
China Grants 61972196, 61832008, and 61832005, in part by the Collaborative
Innovation Center of Novel Software Technology and Industrialization, and the
Sino-German Institutes of Social Computing. Recommended for acceptance by
G. Xylomenos. (Corresponding author: Wenzhong Li.)
The authors are with the State Key Laboratory for Novel Software
Technology, Nanjing University, Nanjing, Jiangsu 210093, China (e-mail:
lwz@nju.edu.cn;
mf1933051@smail.nju.edu.cn;
mf20330097@smail.nju.
edu.cn; 171860540@smail.nju.edu.cn; sanglu@nju.edu.cn).
Digital Object Identiﬁer 10.1109/TMC.2023.3260086
1https://www.grandviewresearch.com/industry-analysis/video-streaming-
market
of 21.3% from 2022 to 2030. The study from Ericsson2 reported
that video streaming currently stands out as the most signiﬁcant
trafﬁc type consumed by smartphone users, and it is projected to
account for 74 percent of Internet trafﬁc by the end of 2024. The
fundamental design of a media streaming system pays increasing
attention to guarantee the users’ Quality of Experience (QoE).
It was showed [1] that users started to abandon a video if it took
more than 2 seconds to start up, with each incremental delay of
1 s resulting in a 5.8% increase in the abandonment rate, and
a moderate amount of interruptions can decrease the average
play time of a viewer by a signiﬁcant amount. Therefore, it is
important for content providers to provide high-quality ﬂuent
video streaming service to their users.
Dynamic Adaptive Streaming over HTTP (DASH) [2] is
the predominant form of video delivery in Internet. In DASH
systems, videos are stored on servers as multiple chunks, each
of which is encoded at several discrete bitrates, where a higher
bitrate implies a higher quality and a longer download time.
Adaptive bitrate (ABR) selection is the fundamental logic in
video streaming that runs on the client-side video players and
dynamically choose a bitrate for each video chunk to optimize
users’ QoE. Selecting the right bitrate in dynamic network is
challenging due to the variability of network conditions and the
trade-off of conﬂicting video QoE requirements [3], [4], [5].
Conventional ABR algorithms adopted a model-based ap-
proach that used mathematical models to describe network
conditions and made bitrate decisions based on the estimation
of network throughput [6], [7], [8], [9], [10] and playback
buffer occupancy [11], [12]. For example, FESTIVE [8] used
the harmonic mean of download speed over recent chunks to
predict the throughput and proposed a stateful bitrate selection
to compensate for the biased interaction between bitrate and
estimated bandwidth. BBA [11] was a buffer-based approach
which selected bitrates based on playback buffer occupation and
estimation of future capacity from past observations. MPC [13]
developed a model predictive control algorithm that combined
both throughput estimates and buffer occupancy information
to select bitrates to maximize QoE over a horizon of several
future chunks. However, model-based ABR algorithms failed
to achieve optimal performance across a broad set of network
conditions and QoE objectives due to their ﬁxed control rules.
In recent years, learning-based ABR algorithms [4], [5],
[14], [15], [16] were proposed to address the issues of bitrate
2https://www.ericsson.com/en/reports-and-papers/mobility-report/articles/
streaming-video
1536-1233 © 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 2
```text
LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING
2423
Fig. 1.
Performance of a pre-trained DRL agent (Pensieve [5] trained on 3G
dataset) testing on different network environments (details are in Section V-C2).
adaptation in varying network conditions. CS2P [4] used a
data-driven approach to learn clusters of similar sessions and
a Hidden-Markov-Model (HMM) based midstream predictor to
model the stateful evolution of throughput. Fugu [16] adopted
a supervised learning approach from the server side to train a
probabilistic predictor of upcoming chunk transmission times
and used the prediction information to improve the control
policy of MPC. A few works [5], [14], [15], [17] applied Deep
Reinforcement Learning (DRL) to train an agent to generate
ABR policy by interacting with the environment. They did
not rely on pre-programmed models or assumptions about the
environment, and gradually learned the best policy for bitrate
decisions through observation and experience. For example,
Pensieve [5] is a state-of-the-art ABR scheme based on DRL. It
represented its control policy as a neural network that mapped
raw observations (e.g., throughput samples, playback buffer
occupancy, video chunk sizes) to the bitrate decision for the
next chunk, which provided an expressive and scalable way to
incorporate a rich variety of observations into the ABR policy.
Despite the ﬂexibility and effectiveness of the DRL-based
ABR algorithms, there remain a number of challenges to de-
ploy them in real-world video streaming systems. (C1) Long
bootstrap time: The DRL-based methods need to collect a large
amount of training data by exploring various of actions in
different network environments, which typically requires several
hours(e.g.,8hoursreportedinPensieve[5])toformapre-trained
neural network model. (C2) Lack of knowledge transfer: The
existing DRL algorithms are typically task-speciﬁc and trained
to work on a speciﬁc network environment independently, which
are hard to deal with unseen scenarios. As an example, we adopt
the Pensieve [5] algorithm to train a DRL agent on a 3G network,
andthenapplytheagentforbitrateselectionondifferentnetwork
conditions in Fig. 1. It is shown that the agent performs well
on the working environment the same as the training network
(see Fig. 1(a)), whereas it performs poorly on the WiFi and
4G networks, whose QoEs (see Fig. 1(b) and (c)) are close
to or lower than that of simple model-based algorithms such
as BBA [11] and RobustMPC [13]. (C3) Poor adaptivity: The
existing DRL models trained for a client cannot be generalized
to other clients even they operate on similar environments. As a
result,itishardtotrainageneralizedmodeltocopewithdifferent
network types even rich historical datasets are available. For
example, we use an augmented hybrid dataset combining 3G,
WiFi and 4G network traces to train a DRL model and apply
Fig.2.
PerformanceofPensieve[5]DRLagentstrainedwithdifferentdatasets,
where Hybrid means the dataset combining 3G, WiFi and 4G traces (details are
in Section V-C1).
Fig. 3.
Illustration of meta-critic based bitrate adaptation.
it on different network environments in Fig. 2. As illustrated in
Figs. 2(a) to (c), the model trained with multiple network traces
does not improve adaptivity, and it performs even worse than
those trained with a single network dataset. The poor adaptivity
with mixture datasets is probably caused by dataset shift [18],
[19]: the joint distribution of inputs and outputs differs between
training and test stages. In our example, the DRL model trained
to ﬁt data on a wide distribution (3G+WiFi+4G) and tested only
on a relatively narrow distribution will result in a degradation of
performance.
In this article, we propose MetaABR, a novel ABR algorithm
based on meta-learning to address the above challenges. Meta-
learning is a learning approach that uses the experience and
meta-data from the past learning tasks to adapt quickly to new
tasks. The basic idea of the proposed MetaABR is illustrated in
Fig. 3. Assume there are a number of learning tasks that learn
ABR policies on different network environments (e.g., WiFi, 4G
and Ethernet). Unlike conventional DRL methods that train the
tasks separatively, the meta-learning approach trains all the tasks
jointly with a shared meta-critic module. The beneﬁts of training
multiple tasks with a meta-learning approach are threefold [20],
[21], [22]. Firstly, it can learn task-level meta experiences that
help algorithms better adapt to new tasks with optimization of
hyper parameters. Besides, because of its support of learning
from fewer samples, it thus increases the speed of training pro-
cess by limiting the necessary experiments. Finally, by learning
multiple tasks, meta-learning can build more generalized models
that adapt better to changing conditions.
In the proposed framework, each DRL agent observes the
network states including the client playback buffer occupancy,
past bitrate decisions, and several raw network signals (e.g.,
throughput measurements), and feeds these values to its local
model represented as a neural network. The client chooses a
bitrate for the next video chunk based on these metrics, which
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 3
```text
2424
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024
results in a QoE metric observed and passed back to the DRL
agent as a reward. The states and rewards of the tasks are passed
to the meta-critic to train a meta model to supervise the agents to
select suitable bitrates to maximize the QoE metric. By jointly
training the DRL agents with the meta-critic, the shared meta-
critic gains the ability to provide transferrable knowledge among
past learning tasks, which can be applied to efﬁciently learn a
new target task in unseen environment.
Speciﬁcally, the proposec MetaABR can effectively address
the above challenges (C1-C3) of video streaming systems.
Firstly, MetaABR trains a general meta-model to teach the DRL
agents to perform bitrate selection, which enables a new agent to
be fastly trained on a target environment (without long bootstrap
time). As shown in Section V-C3, MetaABR trains a DRL agent
much faster than regular DRL methods, whose convergence time
is about 1/10 of that of Pensieve. Secondly, with the proposed
meta-learning method, a DRL agent can be trained to learn
transferable knowledge from historical tasks, which gains the
ability to be applied in unseen environment. Meta-learning has
the advantage of capturing the general knowledge across similar
learning tasks in the past to improve the performance of learning
new tasks to achieve knowledge transfer. As shown in Sec-
tionV-C2,aMeteABRmodelcanbetrainedwiththe3Gnetwork
trace and then applied to the WiFi and 4G networks, whose
performance is still maintained and is better than the model-
based ABR algorithms such as BBA and MPC. Thirdly, since
the meta-model is typically trained with multiple datasets from
different network environments, the historical experiences can
be learned by the meta-model, which can be used to supervise
the training of a general agent to adapt to various environments.
As shown in Section V-C1, the DRL model of MeteABR trained
with a combined dataset (3G+WiFi+4G traces) clearly beats the
other DRL models trained with a single dataset.
The contribution of our work are summarized as follows.
r We formulate a novel framework for meta-learning based
adaptive bitrate selection design. We discuss the challenges
of deploying DRL-based ABR mechanism in real-world
video streaming systems, which are not trivial to address
within conventional DRL formalism.
r We utilize the proposed framework to design MetaABR, a
novel adaptive bitrate selection algorithm based on meta-
learning to maximize users’ QoE. By jointly training mul-
tiple learning tasks with a shared meta-critic, it has the
ability to provide transferrable knowledge to supervise
bitrate selection, and can be applied to efﬁciently learn
a new task in unseen environment with much fewer data
samples and trainng epoches.
r We implement the proposed MetaABR based on an emula-
tionplatformwhichconnectstotheLinuxnetworkprotocol
stack through a virtual network interface to send real data
packets for evaluation. Extensive experiments based on
real-world traces show that MetaABR achieves the best
comprehensive QoE compared with the state-of-the-art
ABR algorithms in a variety of network environments.
The rest of the paper is organized as follows. Section II intro-
duces the related works of media streaming bitrate adaptation
methods and meta learning algorithms. Section III presents the
detailed mechanism of bitrate adaptation based on meta learn-
ing. Section IV proposes the training method for the proposed
meta-critic and task-speciﬁc actors. Section V evaluates the
system performance with extensive experiments. The paper is
concluded in Section VI.
II. RELATED WORK
In this section, we introduce the related works in terms of
ABR schemes for video streaming and meta learning.
A. ABR Schemes for Video Streaming
The ABR schemes for video streaming can be classiﬁed
into two categories: the model-based and the learning-based
methods.
1) Model-Based Methods: Model-based methods estab-
lished mathematical models to describe network conditions
and make ABR decisions based on the estimation of available
network bandwidth and playback buffer occupancy. The Probe
AND Adapt (PANDA) [6] method estimated the bottleneck
bandwidth and tried to eliminate the ON-OFF steady state issue
aswellasreducebitrateoscillationswhenmultipleclientsshared
the same bottleneck link. The piStream [7] method was a video
adaptation framework for DASH clients in LTE networks that
enabled clients to estimate the available bandwidth based on a
resource monitor module that acted as a physical-layer daemon.
FESTIVE [8] contained a bandwidth estimator module, a bitrate
selection and update method that tried to avoid unfairness of
stateless bitrate selection by making the player stateful, and a
randomized scheduler that incorporated the buffer size to sched-
ule the download of the next segment. However, throughput can
vary widely over time and result in poor ABR performance.
Therefore, BBA [11] adopted a buffer-based approach which
picked a bitrate based on playback buffer occupation. However,
it suffered from QoE degradation during long-term bandwidth
ﬂuctuations. BOLA [12] was also a buffer-based algorithm,
whichturnedtheABRproblemintoautility-maximizationprob-
lemandsolveditbytheLyapunovfunction.MPC[13]developed
a control-theoretic framework that allowed the understanding
and exploration of the trade-offs between bandwidth-based
and buffer-based adaptation algorithms under different network
bandwidth variations. Oboe [23] auto-tuned the parameters of
model-based ABR algorithms for different network conditions
to improve the ABR’s performance.
2) Learning-Based Methods: Since model-based algorithms
failed to achieve optimal performance across a broad set of
network conditions and QoE objectives because of their ﬁxed
controlrules,thelearning-basedmethods[4],[5],[14],[15],[16]
were proposed to learn personalized ABR strategies for various
conditions. Based on the observation that video sessions sharing
similar key features presented similar initial throughput values
and dynamic patterns, the CS2P [4] method used a data-driven
approach to learn clusters of similar sessions, and proposed a
Hidden-Markov-Model (HMM) based midstream predictor to
model the stateful evolution of throughput for bitrate adaptation.
D-DASH [14] formulated the DASH video streaming problem
within a Deep Q-learning framework, and used mixed learning
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 4
```text
LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING
2425
architectures including feedforward and recurrent deep neural
networks to learn video adaptation strategies to achieved a good
trade-off between policy optimality and convergence speed.
Pensieve [5] proposed a Deep Reinforcement Learning (DRL)
model that selected bitrates for future video chunks based on
observations collected by DASH clients (i.e., throughput es-
timation and buffer occupancy) across large video streaming
experiments, which provided an expressive and scalable way
to incorporate a rich variety of observations into the control
policy. To address the issue of low sample efﬁciency of DRL,
Comyco [15] trained an ABR policy via imitating expert tra-
jectories to avoid redundant exploration. Stick [17] fused the
DRL method and traditional buffer-based method to output
the buffer-bound, which was used to control the buffer-based
approach for maximizing the QoE metrics. Fugu [16] argued
that in real-world setting, it was difﬁcult for sophisticated or
machine-learned control schemes to outperform a simple buffer-
basedcontrolscheme,notwithstandinggoodperformanceinnet-
work emulators or simulators. It used supervised learning with
data from real deployment environment to train a probabilistic
predictor of upcoming chunk transmission times to improve
a classical control policy. Recently, learning-based methods
were extended to the emerging 3D video streaming applications
and video conferencing systems [24], [25], [26], [27], [28].
Swift [24] adopted a layered encoder that learns to compress
a video frame into layered codes and proposed an ABR protocol
based on detecting available bandwidth and client-side capacity.
YuZu [25] adopted a neural-enhanced method for intra- and
inter-frame optimizations using 3D super resolution to increase
the visual quality of volumetric video streaming. Vues [26] was
an edge-assisted transcoding system that transcoded a volu-
metric video frame into multiple 2D views using lightweight
machine learning models and adaptively selected the view that
optimized the QoE for mobile clients. GSO-Simulcast [27] was
a multi-party video-conferencing system where a media server
globally coordinated the publishing and subscribing to decide
the resolution and bitrate of video streams for each participant.
Optimization of video streaming dilivery were also studied in
the aspects of routing path assignment [29] and inter-session
multiplexing congestion control [30].
Different from the existing learning based methods, the pro-
posed MetaABR method introduces a novel meta-learning ap-
proach with neural-enhanced bitrate selection particularly object
to improve the generalization, robustness, and training efﬁciency
of the deep learning based ABR methods. To the best of our
knowledge, MetaABR is the ﬁrst to incorporate meta-critic into
the design of ABR mechanism for video streaming.
B. Meta-Learning
Meta-learning, also known as learning to learn, is a machine
learning method that intends to learn the general knowledge
across similar learning tasks to improve its performance in new
tasks based on a few examples [20], [21]. Meta-learning helps
to achieve higher model accuracy, because of its optimization of
learning algorithms such as optimization of hyper parameters
to achieve the best results. It also helps to learn algorithms
better adapt to changing conditions by training multiple tasks
to build more generalized models. At the architecture level,
meta-learning is usually conceptualized as involving two learn-
ing systems: a lower-level system that learns relatively quickly
and is mainly responsible for adapting to new task; A slower
upper-level system that can work across multiple tasks to adjust
and improve lower-level systems with an objective of general-
ization performance.
Inside and outside the deep learning community, various
methods have been explored to achieve the basic meta-learning
setting [21]. An important method was introduced by Hochreiter
et al. which used standard backpropagation to train recurrent
neural networks for a series of related tasks [31]. The basic
process of learning each new task in Hochreiter method is
completely within the dynamic range of the recurrent network,
which was suitable for the structure of the task family trained
across the network [32].
Reinforcement Learning (RL) learned control policies
through interacting with an environment, which enabled an
agent to obtain high reward in achieving a sequential action task
within an environment. However, RL typically suffered from
extreme sample inefﬁciency due to sparse rewards, the need
of exploration, and high-variance optimization algorithms [33].
Several meta-representations had been explored in RL including
learning the initial conditions [34], [35], hyperparameters [36],
step directions [37], and step sizes [38], which enabled meta
learning to train a neural network with fewer environmental
interactions [39], [40].
In addition to conventional RL that explored environment
based on sampling random actions or hand-crafted heuris-
tics [41], several meta-RL studies treated exploration strategy
or curiosity function as meta-knowledge, and modeled their
acquisition as a meta-learning problem to improve sample ef-
ﬁciency [42]. A large number of meta-RL studies considered
single-task setting, where loss, reward, and hyperparameters
were took as meta-knowledge to train together with the base pol-
icytoimproveasinglelearningtask[43], [44], [45]. Afewrecent
works designed meta-RL generalizations for the conventional
off-policy RL methods to accelerate the training and testing by
replaying buffer samples from meta-training [46], [47]. It had
been demonstrated that meta-RL was successfully applied in
real-world physical robot [48], imitation learning [49], etc.
III. META-LEARNING BASED BITRATE ADAPTATION
MECHANISM
In this section, we propose a meta-learning based bitrate adap-
tation mechanism called MetaABR. We ﬁrst provide quantiﬁed
description of QoE metrics, then formulate the ABR problem as
a deep reinforcement learning task, which can be solved with a
meta-reinforcement learning framework. The key notations used
throughout the paper are summarized in Table I. The details are
introduced as follows.
A. QoE Metrics
Toimproveusers’experience,mediastreamingserviceshould
consider a variety of QoE goals such as maximizing video
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 5
```text
2426
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024
TABLE I
NOTATIONS
quality, minimizing rebuffering time, and maintaining video
quality smoothness (i.e., avoiding constant bitrate ﬂuctuations).
For a satisfactory user-perceived QoE, ABR algorithm needs
to optimize several conﬂicting goals. For example, increasing
the bitrate may lead to longer rebuffering time. There exists
signiﬁcant variance in user preferences for video streaming QoE.
To formulate the problem, we adopt the quantiﬁcation of QoE
metrics as introduced in [13].
Speciﬁcally, users tend to prefer great average quality per
chunk for high-deﬁnition content, which can be calculated on
the mean of n-th chunk of video v by:
QoEv
hd =
N

n=1
q(Rn,v),
(1)
where Rn,v is the bitrate of chunk n of video v, and q(·) is a
non-decreasing function which maps the selected bitrate to the
video quality perceived by user.
Meanwhile, we need to ensure a ﬂuent playback and minimize
the rebuffering time of every chunk, which is computed by:
QoEv
reb =
N

n=1
Tn,v,
(2)
where Tn,v is the rebuffering time that results from downloading
chunk n at bitrate Rn,v.
Besides, the streaming strategy should reduce sudden and fre-
quent quality variations, which may impose negative experience
for users. Variation of video quality is calculated by:
QoEv
var =
N−1

n=1
|q(Rn+1,v) −q(Rn, v)|,
(3)
which penalizes changes in video quality to favor smoothness.
Overall objective: The overall objective in a comprehensive
QoE metric is a weighted sum of the three metrics on video v,
which is deﬁned as
QoEv = μ1QoEv
hd −μ2QoEv
reb −μ3QoEv
var,
(4)
where M = (μ1, μ2, μ3) is a set of non-negative weighting
parameters corresponding to users’ preference on the video
quality, rebuffering time, and variation, respectively.
B. ABR as a Deep Reinforcement Learning Task
Adaptive bitrate selection for video streaming can be casted
as a deep reinforcement learning (DRL) task: an agent learns by
observing the states of the dynamic environment, and produces
actions based on a neural network to select the proper bitrate to
maximizetheexpectedlong-termQoE.Wediscussthefollowing
basic elements of a DRL task.
Agent: An agent is an entity in the system responsible for
performing learning algorithm and making sequential decisions.
In the ABR problem, at each time step, the agent is triggered to
choose a bitrate for a chunk to be downloaded.
State: A state of the system consists of a number of network
performance measurements that are observed by the agent. At
time step t, the state used as input to the DRL agent is denoted
by
st = (⃗xt, ⃗τt, ⃗nt, bt, ct, lt),
(5)
where ⃗xt is the network throughput measurements for the past
k video chunks; ⃗τt is the download time of the past k video
chunks, which represents the time interval of the throughput
measurements; ⃗nt is a vector of m available sizes for the next
video chunk; bt is the current buffer level; ct is the number of
chunks remaining in the video; and lt is the bitrate at which the
last chunk was downloaded.
Action: Upon observing a state st, the agent needs to take
an action at to determine the downloading bitrate for the next
video chunk. A video website typically encodes a video with
different bitrate levels such as 240p, 480p, and 1080p, and the
agent selects bitrate based on a policy learned by the model. In
DRL, the agent uses a deep neural network (DNN) to represent
the policy with a number of model parameters θ. Using θ, we
can denote the policy by πθ(st, at).
Reward: At each time step t, the agent observes some state
st, and chooses an action at. After applying the action, the state
of the environment transitions to st+1 and the agent receives a
reward rt representing a comprehensive QoE metric.
With the above formulation, the reinforcement learning task
for bitrate adaptation can be described as follows.
Reinforcement Learning Task for Bitrate Adaptation: Given a
set of observed network states {s1, s2, · · · }, learn a deep neural
network model that maps each state to an action (representing
the bitrate selection policy): f(st) →at, in order to maximize
the long-term expected cumulative discounted reward, i.e.,
E
 ∞

t=0
γtrt

,
(6)
where γ ∈(0, 1] is a factor discounting future rewards.
C. Solution With a Meta-Learning Framework
As discussed in Section I, conventional deep reinforcement
learning for ABR selection has the drawbacks of efﬁciency,
generalization and robustness. To overcome the performance
issues, we propose a novel meta reinforcement learning (MRL)
based method called MetaABR for bitrate adaptation in video
streaming. In the proposed framework, we apply the A3C
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 6
```text
LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING
2427
Fig. 4.
Framework of MetaABR.
algorithm [50] for deep reinforcement learning. A3C is a state-
of-the-art DRL method that jointly trains a pair of actor-critic
deep neural networks for any RL task so that the actor learns to
solve the problem, and the critic learns to effectively supervise
the actor by approximating its reward. Following the learning
to learn method [50], [51], we adapt the A3C method for meta-
learning by training a global meta-critic neural network based
on cross-task knowledge to supervise multiple actor networks
to solve speciﬁc problems. In this way, the shared meta-critic
can provide transferable knowledge in training actors to gener-
ate ABR policies for different network environments, and the
experience of meta-critic can be learned by the actors on new
problems with only a few trials to achieve adaptivity and fast
convergence. Noted that there are many meta-learning meth-
ods such as MAML [34], MAESN [52], GrBAL/ReBAL [48],
PEARL [53], etc., which we believe are also applicable to the
proposed meta-learning framework for adaptive bitrate selec-
tion. However, searching for the most efﬁcient meta-learning
method for MetaABR is beyond the discussion of this article.
The overall framework of MetaABR is illustrated in Fig. 4.
It consists of a set of actor networks that learn to solve spe-
ciﬁc tasks (e.g., learning an ABR algorithm for a particular
network environment such as WiFi and 3G), and a global
meta-critic network that learns how to effectively supervise the
actors. Actor-critic is a well-known deep reinforcement learning
method where an actor is a neural network used to select actions
and a critic is another neural network used to learn a value
function and update the actor’s policy parameters in a direction
of performance improvement [50]. Unlike conventional actor-
critic networks [54], [55] that train a pair of actor-critic for
each learning task individually, the proposed framework trains
a shared meta-critic to provide transferrable knowledge among
actors, which allows the actors to be trained with only a few trials
in adapting to a new task. For example, by considering a set of
tasks each learns an ABR policy in a particular environment such
as Ethernet or WiFi networks, we can train a task-independent
meta-critic from them, and apply the meta-critic to efﬁciently
learn an actor for a new target task such as a new ABR policy
for 3G networks.
To apply the idea of meta-learning on solving the problem,
we need to explicitly condition the meta-critic on a task, so
that at any moment it knows what actor it is training and what
task the actor should be trained to solve. To achieve this, the
meta-critic is further divided into a task-conﬁg network and a
critic network as shown in Fig. 4. The task-conﬁg network takes
the past trails of a RL task represented by a trajectory of the
state, action, and reward as input to learn historical experience,
and it outputs a task-actor embedding z which represents the
task-speciﬁc features. The critic network uses the current (state,
action) and the task-actor embedding z from the task-conﬁg
network as input to approximate the reward for a RL task, where
z serves as the meta-knowledge to decide how to criticise the
current actor on the speciﬁc task. The training details are given
in Section IV.
By jointly training the meta-critic with multiple actors, the
meta-critic gains the ability to correctly criticise a new task based
on the provided task-conﬁg network. When applying the meta-
critic to learn a new task, from the perspective of the new task’s
actor, it beneﬁts from a pre-trained meta-critic which increases
learning speed and decreases required samples.
The meta-critic based approach has a number of further bene-
ﬁts. (1) It can address DRL tasks (i.e., training agents for differ-
ent network environments) within a single framework, where the
actors can beneﬁt from the meta-critic’s supervision of what it
should do in those unlabelled states (unseen situations). (2) The
proposed task-conﬁg and meta-critic networks can capture the
correlation among diverse learning tasks from the past, and such
history-dependent knowledge can be transferred to the learning
of a new task, making the agent more capable of choosing the
suitable policy to optimize rewards when being exposed to a new
environment.
IV. TRAINING METHODS
In this section, we introduce the methods of training the meta-
critic and the task-speciﬁc actors in detail.
A. Training the Meta-Critic
In the proposed framework, we want to train a single meta-
critic that can criticise any actor to perform any task. This
requires two generalisations (task and actor conditioning) com-
pared to conventional critic networks that criticise a speciﬁc
actor for a speciﬁc task. The structure of the meta-critic is illus-
trated in Fig. 5, which consists of two subnetworks: a task-conﬁg
network and a critic network.
The task-conﬁg network Cω, parameterised by ω, has a three-
layer neural network structure. It takes the past k trails of (state,
action, reward) triplets as input to learn task-speciﬁc experience.
The input layer is a concatenation of a fully-connected (FC)
layer (to deal with numerical values) and a one-dimensional
convolutional neural network (1D-CNN) layer (to deal with vec-
tors). It follows by a fully-connected (FC) layer and a recurrent
neural network (RNN) layer to produce a task-actor embedding
z, which encodes the task-dependent features for meta-learning.
Speciﬁcally, we model the task-actor encoder as a Long-Short
Term Memory (LSTM) [56] whose input is a trajectory of past
k trials each represented by a triplet
Lt
t−k = (st−k, at−k, rt−k).
(7)
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 7
```text
2428
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024
Fig. 5.
Structure of Meta-Critic.
The output of the task-conﬁg network is a task-actor embed-
ding zt that represents the task-dependent features, where
zt = Cω

Lt
t−k, Lt
t−k+1, . . . , Lt
t−1

.
(8)
The rational of using the proposed task-actor embedding as
meta-knowledge to train a meta model are explained as follows.
On the one hand, it encodes a sequence of state-action pairs (the
choiceofactiondependsontheactor’sparameters),whichcanbe
usedbythecritictocharacterizetheactor’spolicyitistocriticise.
On the other hand, it encodes the observed rewards of each
action, which enables the critic to capture the characterization
of the task that the actor is solving.
The critic network Qφ, parameterised by φ, has similar
structure as that of the task-conﬁg network, which is used to
approximate the reward for reinforcement learning tasks. Apart
from the state st and action at, it further takes the task-actor
embedding z as input to learn an action-value function. We use
Qφ(s(i)
t , a(i)
t , z(i)
t ) to describe the expected return reward after
actor i taking action a(i)
t
in state s(i)
t
with a task-actor embedding
z(i)
t .
The meta-critic is shared across all tasks and actors, which
is trained to help actors to ﬁnd strategies that are more suitable
for the environment. Assuming there are M learning tasks, the
update rules for the meta-critic model parameters are as follows.
φ, ω ←arg min
φ,ω
M

i=1
(Pφ,ω(s(i)
t , a(i)
t , z(i)
t ))2,
Pφ,ω(s(i)
t , a(i)
t , z(i)
t ) = Qφ(s(i)
t , a(i)
t , C(i)
ω,t) −rt
−γQφ(s(i)
t+1, a(i)
t+1, C(i)
ω,t+1).
(9)
In the above equation, Pφ,ω() is the error between the esti-
mated reward (the output of the critic network) and the actual
reward, and the learning objective is to ﬁnd the optimal model
parameters φ and ω that minimize the overall squared error.
B. Training the Task-Speciﬁc Actors
The actor networks Aθ(i), parameterised by θ(i), are a set
of task-speciﬁc neural networks that are used by the agents to
generate actions for ABR decision. The neural network structure
of the actor networks is similar to that of the conﬁg network. The
hidden layer formed by the convolutional layer and the fully
connected layer in the actor networks have 128 neurons that
apply the softmax function in the output layer.
The actor network takes the state s(i)
t
as input, then outputs
an action a(i)
t , i.e., a(i)
t
= Aθ(i)(s(i)
t ). After applying each ac-
tion, the agent observes a reward for that chunk. The goal of
each learning agent is to maximize the expected cumulative
(discounted) reward that it receives from the network environ-
ment in terms of a speciﬁc QoE metric. In other words, the
actor network intends to maximize the discounted future reward
Qφ(s(i)
t , a(i)
t , z(i)
t ) that is the estimated value from the output
of the meta-critic network. Therefore, the optimizer alternately
updates the actor network with:
θ(i) ←arg max
θ(i)
Qφ

s(i)
t , Aθ(i)(s(i)
t ), z(i)
t

.
(10)
Intheaboveequation,multipleactorsaretrainedjointlytoﬁnd
their optimal model parameters θ(i) to maximize the estimated
reward based on the output of the meta-critic.
V. EXPERIMENTS
In this section, we conduct extensive experiments to evaluate
the performance of MetaABR. Our experiments cover a broad
set of network conditions and QoE metrics. We mainly focus on
answering the following questions.
(1) How does MetaABR compare to the state-of-the-art ABR
algorithms in terms of video QoE? We ﬁnd that, in all of the
consideredscenarios,MetaABRisabletorivaloroutperformthe
best existing scheme, with average QoE improvements ranging
from 3%-15%.
(2) Does the MetaABR method perform more efﬁciently than
other reinforcement learning methods? Through the experiment,
we ﬁnd that MetaABR can achieve comparable performance
with other reinforcement learning methods with much fewer
samples and training epochs, and it performs the best even being
transferred to a different network environment.
(3) How is the trade-off between different conﬂicting QoE
metrics? We ﬁnd that MetaABR achieves a better trade-off
between increasing bitrate and reducing rebuffering time and
variation, which is more closer to the ideal situation compared
to the baselines.
A. Experiment Setup
1) Implementation: In our implementation of the MetaABR
scheme, the task-conﬁg network Cω, the critic network Qφ,
and the actor network Aθ are three-layer fully-connected neural
networks that use rectiﬁed linear unit (ReLU) as the activa-
tion function of each neuron. We train the neural networks
on TensorFlow 1.13.1 using RMSPropOptimizer with learning
rate 0.01 (Cω), 0.0001 (Qφ), and 0.001 (Aθ) accordingly. The
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 8
```text
LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING
2429
TABLE II
THE LAYER PARAMETERS OF METAABR
reward discount factor γ = 0.99 by default. The neural network
structure of MetaABR is illustrated in Table II.
2) Evaluation Platform: The experiments are conducted on
a PC server (CPU: Intel(R) Xeon(R) CPU E5-2630 v4 @
2.20 GHz; Memory: 32 GB DDR4 2400Mhz*4; OS: 64-bit
Ubuntu 16.04). We implement the proposed MetaABR frame-
work based on the Mahimahi [57] emulation platform, which is
connected to the Linux network protocol stack through a virtual
network interface and sends real data packets. Mahimahi can be
used to record trafﬁc from HTTP-based applications and replay
it under emulated network conditions, which is ideal for fair
comparison of different ABR algorithms for video streaming.
3) Baseline Algorithms: We compare MetaABR with three
state-of-the-art ABR algorithms:
r BBA [11]: a buffer-based approach which selects bitrates
based on playback buffer occupation.
r RobustMPC [13]: a model predictive control algorithm that
combines both throughput estimates and buffer occupancy
information to select bitrates.
r Pensieve [5]: a state-of-the-art ABR scheme based on deep
reinforcement learning.
r BayesMPC [58]: an uncertainty-aware robust ABR algo-
rithm based on Bayesian neural network (BNN) and model
predictive control (MPC).
r Comyco [15]: a video quality-aware ABR approach lever-
aging imitation learning to accelerate the training process
for ABR tasks.
Note that we do not compare with other deep learning based
ABR algorithms such as Fugu [16], Oboe [23], and Stick [17],
since either they are implemented on the server side, or there are
lack of open-source code to reproduce their work.
4) Video Parameters: We have modiﬁed dash.js3 to sup-
port MetaABR and the above baseline ABR algorithms. For
MetaABR, Pensieve, and RobustMPC, we conﬁgure dash.js to
obtain the bitrate selection decision from an ABR process that
implements the corresponding algorithm. The DASH player is
conﬁgured to have a playback buffer capacity of 60 seconds. Our
evaluation used the “Envivio-Dash3” video of the DASH-246
JavaScript reference client. In addition, the video is divided
into 48 blocks with a total length of 193 seconds. This video
is encoded by the H.264/MPEG-4 codec at bitrates in 300, 750,
1200,1850,2850,4300kbps(whichcorrespondstovideomodes
in 240p, 360p, 480p, 720p, 1080p, 1440p). Therefore, each
block represents approximately 4 seconds of video playback. In
3https://github.com/Dash-Industry-Forum/dash.js/, Akamai, 2020.
our settings, the client video player is Google Chrome (version
85) and chromedriver (version 85.0.4183.38). The video server
is Apache (version 2.4.7). We use Mahimahi [57] to emulate
network environments from the network traces between the
client and the server with 80 ms RTT.
5) Datasets and Network Traces: To evaluate the ABR algo-
rithms on realistic network conditions, we created a corpus of
network traces using several real-world network communication
datasets.
r 3 G [59]: This dataset was collected from popular commute
routes in and around Oslo (Norway). It includes throughput
measurements of real-world adaptive HTTP streaming per-
formed over 3G networks using mobile devices traveling
with different types of public transportation (metro, tram,
train, bus and ferry). The throughput of the network is
between 0.1 ∼1 Mbps.
r WiFi [5]: This dataset is from the work [5], which is tai-
lored from a broadband dataset provided by the FCC [60].
Since the original dataset contains large amount broadband
data log over one year, the authors in [5] selected the “Web
browsing” category in the Aug 2016 collection and only
keeps traces whose average throughput is less than 6 Mbps
to avoid trivial ABR solutions.
r 4GSyd [61]: This dataset was collected from SpeedTest
measurements conducted in Sydney on 4G networks under
vehicular driving conditions. In the dataset, throughput
measurements samples were collected within 72 trips in
different day and night times to consider On and Off peak
hours of trafﬁc. The throughput of the 4G network ranges
from 5 ∼10 Mbps.
r Hybrid (3G + WiFi + 4GSyd): We combine the data
sampes of the above 3G, WiFi, and 4GSyd datasets to
generateahybriddataset.Itsimulatesthereal-lifescenarios
where three networks are dynamically switching due to the
mobility of smartphones. The performance in this dataset
can well reﬂect the generalization ability of the ABR
method.
r 4GNY [62]: This dataset was collected on New York City
MTA bus and subway. The data was recorded with a mobile
phone running iPerf to log TCP throughput every 1000
milliseconds. The throughput of the network environment
is between 1 ∼108 Mbps.
r 5 G [63]: This dataset was collected from a major Irish
mobile operator. It was generated from two mobility pat-
terns (static and car) across two application patterns (video
streaming and ﬁle download). It consists of two parts: the
ﬁrst is a production dataset collected from real-world and
the second is synthetic data generated from a large-scale
multi-cell 5G/mmwave ns-3 platform. We selected the data
generated from the Amazon Prime and Netﬂix streaming
services in the experiments, and the throughput of the 5G
network is in the range of 3 ∼202.5 Mbps.
The basic information of the datasets are listed in Table III.
The statistical characteristics of the datasets are shown in Fig. 6.
According to the ﬁgure, both 3G and WiFi traces have small
throughput and low variations. It is observed that over 95%
throughput of 4GSyd are concentrated on 8-9 Mbps, and the
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 9
```text
2430
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024
TABLE III
DATASETS STATISTICS
Fig. 6.
Characteristics of datasets.
standard deviation is less than 0.5. The reason is that 4GSyd was
collectedwiththeTestSpeedAPPwhichformsstablethroughput
testing from different locations. The 4GNY and 5 G datasets are
more diverse, whose throughput spread from a wide range with
larger deviations.
For each of the above dataset, we follow the method proposed
in Pensieve [5] to generate traces for reinforcement learning and
to test the ABR algorithms. For the 3G and 4GSyd datasets, we
generated 1000 throughput traces each with a duration of 320
seconds by using a sliding window across the network traces. For
the WiFi dataset, we generated 1000 traces (each with 320 sec-
onds) by concatenating randomly selected traces from the “Web
browsing” category in the Aug 2016 collection. For the Hybrid
scenario, we simply combined the throughput traces generated
from the 3G, WiFi, and 4GSyd datasets together to form the
dataset. We reformatted the generated throughput traces to ﬁt
the Mahimahi [57] emulation platform, so that the same trace
can be replayed to test different ABR algorithms. We randomly
partition the generated traces into train and test datasets, where
80% of data are used for training machine learning models and
20% are used for testing all compared algorithms by default.
Among the train set, 20% of data are used to form a validation
set for hyperperameter tuning.
Since the traces of the 4GNY and 5G datasets are much
smaller than that of the other datasets, we only used them
for testing the adaptivity and knowledge transfer of the DRL
algorithms. That is, we trained the DRL models using other
datasets, and then tested the pre-trained models on the 4GNY
and 5G datasets to show their performance on unseen network
environments. Following similar principle, we generated 200
throughput traces each with a duration of 320 seconds by using
TABLE IV
THE QOE METRICS CONSIDERED IN THE EVALUATION
a sliding window across the 4GNY and 5G network traces to
form the test sets.
6) QoE Metrics: Similar to the literature, we consider three
QoE metrics with different choices of the combination of
q(Rn,v) and M.
r QoEstd: q(Rn,v) = Rn, M = (1, 4.3, 1). This is the stan-
dard QoE metric that had been widely used in the state-of-
the-art ABR systems such as MPC [64] and Pensieve [5].
r QoEfluent: q(Rn,v) = Rn, M = (1, 8, 1). This metric
emphasizes the ﬂuency of the video. It uses a much higher
penalty on rebuffering time to calculate the reward, which
intends to provide more ﬂuent video streaming service to
the user.
r QoEhd: M = (1, 8, 1). This metric favors high deﬁnition
(HD) video. It adopts a q(Rn,v) mapping that assigns qual-
ity scores according to the bitrates as illustrated in Table IV,
where HD bitrates have signiﬁcantly higher quality score
than that of non-HD bitrates.
The exact values of q(Rn,v) for the QoE are provided in
Table IV. In our experiments, we report the average QoE per
chunk, i.e., the total QoE metric divided by the number of chunks
in the video.
B. Comparison With Baseline Algorithms
In this section, we compare the performance of MetaABR
with the baseline algorithms with different network traces.
The Cumulative Distribution Functions (CDFs) of the algo-
rithms on different QoE metrics are illustrated in Figs. 7, 8, 9,
and 10, and the average results are shown in Table V. We make
the following discussions on the results.
Firstly, MetaABR either matches or exceeds the performance
of the state-of-the-art ABR algorithms on each QoE metric and
network considered. According to Table V, MetaABR trained
from individual network trace (e.g., 3G, WiFi, and 4GSyd)
performs very close to Pensieve. MetaABR trained from hy-
brid trace signiﬁcantly outperforms the other algorithms, which
achieves the best QoE on almost all network conditions. This
shows the power of meta-learning: it can learn experiences from
different network conditions to improve performance and be
adaptable to different scenarios. For QoEstd, a widely con-
sidered metric in the literature [5], [64], the average QoE for
MetaABR is 5% higher than that of Pensieve on 3G networks,
and 3% ∼15% higher in other networks. The gaps between
MetaABR and other methods are also found in QoEfluent and
QoEhd. It is noticed that the CDFs in 4GSyd show stair-like
shapes in Fig. 9, and the reason is explained as follows. Since
the 4GSyd trace has very stable throughput, where over 95%
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 10
```text
LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING
2431
Fig. 7.
CDF of QoE metrics (3G network).
Fig. 8.
CDF of QoE metrics (WiFi network).
Fig. 9.
CDF of QoE metrics (4Gsyd network).
throughput are concentrated on 8-9 Mbps with standard de-
viation less than 0.5 as shown in Fig. 6, it is easy to form
a trivial solution for bitrate selection. That is, it can use full
(near-constant) bandwidth to satisfy the QoE in a high level for
the vast majority of ABR cases. Therefore, machine learning
methods did not show signiﬁcant performance improvement
compared to model-based methods in the 4GSyd datasets, and
most algorithms achieve high QoEs with more than 95% of cases
concentrating on a high level.
Secondly, MetaABR is able to automatically learn suitable
ABR policies with a shared meta-critic on Hybrid network
environments, whereas the model-based ABR algorithms such
as BBA and Robust MPC struggle to optimize for different
environments and QoE objectives. Since the model-based al-
gorithms employ ﬁxed control laws, they are not ﬂexible for
optimizing for multiple QoE objectives with different ABR
policies. For example, when network bandwidth is inadequate,
the ABR algorithm should build the playback buffer as quickly
aspossibleusingthelowestbitrate.Asillustratedbytheresultsin
hybrid network, MetaABR is able to learn such a policy without
expert involvement, while other algorithms have difﬁculty to
optimize such long term strategies.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 11
```text
2432
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024
Fig. 10.
CDF of QoE metrics (Hybrid network).
TABLE V
COMPARISON OF AVERAGE BITRATE (MBPS), REBUFFERING TIME (SECOND), VARIATIONS, AND THEIR CORRESPONDING QOE METRICS ON DIFFERENT NETWORK
ENVIRONMENTS, WHERE METAABR(HYBRID) MEANS A METAABR MODEL TRAINED WITH THE Hybrid DATASET, AND SO ARE THE REST
C. Effectiveness of Meta-Critic Learning
1) Adaptivity: The major advantage of MetaABR is its adap-
tivity on different network traces, which enables a machine
learning ABR algorithm to learn once and be applied to any-
where. With the proposed meta-learning method we can train a
general model MetaABR(Hybrid) based on the Hybrid dataset
and then apply it to the other networks without modiﬁcation.
As illustrated in Table V, MetaABR(Hybrid) performs close or
better than those models personally trained on speciﬁc networks.
For example, MetaABR(Hybrid) outperforms MetaABR(WiFi)
on the WiFi network, and outperforms MetaABR(4GSyd) on
the 4G network, which generally achieves the best perfor-
mance on all test datasets. On the other hand, conventional
DRL method such as Pensieve has poor adaptivity, e.g., Pen-
sieve(Hybrid) clearly performs much worse than Pensieve(3G)
and Pensieve(WiFi) on the corresponding datasets.
2) Ability of Knowledge Transfer: We then test the ability of
knowledge transfer. Similar to the experiments in Section V-B,
we use the Hybrid dataset to pre-train a DRL model, and apply
the model to unseen networks (i.e., 4GNY and 5G) to test its
performance. The results are shown in Table VI, Figs. 11 and
12. Clearly MetaABR(Hybrid) achieves the best QoEs in most
cases, and it beats the personally trained method Comyco on
most QoE metrics, thanks to its power of knowledge transfer
from other learning tasks. Pensieve(Hybrid) performs close to
or worse than the model-based methods such as BBA and
RobustMPC, which shows poor ability of knowledge transfer
without meta-learning.
To test whether the training knowledge from single dataset
is transferable to multiple datasets, we train both MetaABR
and Pensieve on the 3G dataset, and then apply the pre-trained
model to the rest networks. The results are shown in Table VII.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 12
```text
LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING
2433
TABLE VI
COMPARISON OF QOE METRICS FOR TRANSFERRING A PRE-TRAINED MODEL TO UNSEEN NETWORK ENVIRONMENTS, WHERE METAABR(HYBRID) MEANS A
METAABR MODEL TRAINED WITH THE Hybrid DATASET, AND SO ARE THE REST
Fig. 11.
CDF of QoE metrics (Train set: Hybrid; Test set: 4GNY ).
Fig. 12.
CDF of QoE metrics (Train set: Hybrid; Test set: 5G).
TABLE VII
COMPARISON OF QoEstd METRIC FOR TRANSFERRING A PRE-TRAINED
MODEL ON 3G DATASET TO MULTIPLE NETWORK ENVIRONMENTS
According to the table, both MetaABR and Pensieve perform
well in 3G network (where train and test environment are the
same). After applying to other networks, Pensieve performs
worse than the model-based approaches BBA and RobustMPC,
Fig. 13.
Convergence of MetaABR.
but MetaABR still performs the best among all scenarios. This
veriﬁes the power of meta-learning in knowledge transfer.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 13
```text
2434
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024
Fig. 14.
Performance of MetaABR with different percentages of trainset.
Fig. 15.
Trade-off between bitrate, rebuffering time and variance.
3) Convergence: We further show the training efﬁciency of
MetaABR. Figs. 13(a) and (b) show the loss function and reward
of training a Pensieve model, training a MetaABR model from
scratch, and training a new task with a pre-trained meta-critic
on 3G network. It is shown that MetaABR convergences more
faster than that of Pensieve, whose loss approaches 0 after
50 epoches. The reward of MetaABR is signiﬁcantly higher
than that of Pensieve, which means it learns a better policy of
QoE optimization. It is noticed that learning a new task with
MetaABR can converge within 20 epochs, while Pensieve takes
about 200 epochs to converge.
4) Performance With Small Samples: Fig. 14 shows the re-
sults of MetaABR with different percentages of training sam-
ples. It is shown that even using only 10% of the total train
dataset, MetaABR still has comparable performance with Pen-
sieve with full dataset.
D. Trade-Off Between QoE Metrics
We study the trade-off between different conﬂicting QoE met-
rics, and the normalized results are shown in Fig. 15. It is shown
that RobustMPC achieves higher bitrate with larger rebuffering
time and variation. Pensieve and BBA have modest bitrate and
rebuffering time/variation. Compared to the other algorithms,
MetaABR achieves the best trade-off between different QoE
metrics, which is much more closer to the ideal situation.
E. Performance on Multi-Video Scenario
In this experiment, we test the pre-trained DRL models on a
multi-video scenario to evaluate their ability to generalize across
multiple video streaming properties. We generate the trace of
multiple video streaming scenario as follows. We generate 1000
synthetic video traces with diverse bitrates, chunk sizes, and
video duration. The value of bitrate is randomly chosen from
{200, 300, 450, 750, 1200, 1850, 2850, 4300, 6000, 8000}
Kbps. The chunk size of each video is a mean size multiplying a
Gaussian distribution N(1, 0.1). The duration of each video is a
random chunk number in the range [20,100]. We apply the DRL
model trained with Hybrid dataset on the multi-video scenario,
and the experimental results are illustrated in Fig. 16. As shown
in the ﬁgure, MetaABR still outperforms the baseline algorithms
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 14
```text
LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING
2435
Fig. 16.
CDF of QoE metrics of multi-video scenario testing on WiFi network.
Fig. 17.
CDF of QoEstd metrics under real-world network scenarios.
TABLE VIII
COMPARISON OF AVERAGE BITRATE (MBPS), REBUFFERING TIME (SECOND), VARIATIONS, AND QoEstd METRIC ON REAL-WORLD SCENARIOS
on a variety of QoE metrics, and signiﬁcant performance im-
provement is found in the QoEfluent metric. The results suggest
that MetaABR can be adapted to the multiple video streaming
scenarios with diverse QoE properties.
F. Performance on Real-World Scenarios
Apartfromtrace-drivenexperiments,wedeploythecompared
algorithms in a wireless network testbed to test the performance
under real-world scenarios. We use a laptop (lenovo savior
y7000, windows 10) as client, and it connects to a HUAWEI
P20 (Harmony 2.0.0) smartphone which is used as a proxy to
establish Wi-Fi or 4G connections. The laptop uses a Chrome
browser to access video-on-demand service from a media server
(Intel(R) Xeon(R) CPU E5-2630v4@2.20 GHz; 32 GB DDR4
2400 Mhz*4; 64-bit Ubuntu 16.04), and the ABR algorithms are
implemented in dash.js that is used by the player for adaptive
bitrate selection. We conduct experiments based on three real-
world scenarios. (1) Dormitory: the client is almost static in a
university dormitory and it connects to a small WiFi network.
(2) Library: the client is connected to a library WiFi network
with many users around and occasional movement. (3) School
Bus: the client is connected to a 4G network and it is placed on
a school bus with constant movement.
The CDF of QoE of different ABR algorithms under different
scenarios is compared in Fig. 17, and the average QoE metrics
are illustrated in Table VIII. Due to page limit, we only show
the QoEstd metric for comparison. According to Fig. 17, the
CDF curve of MetaABR is lower than that of other algorithms
in three scenarios, which means MetaABR is concentrating on
the region of higher QoEstd. According to Table VIII, in the
dormitory scenario, MetaABR improves the QoE performance
by 4.2% compared to Pensieve and 57.4% higher than that of
RobustMPC.Similarly,signiﬁcantQoEimprovementisfoundin
the library and the school bus scenarios. In summary, MetaABR
achieves the highest QoE in all three real-world scenarios, and
its rebufﬁng time and variations are much lower than that of the
baseline algorithms.
VI. CONCLUSION
In this article, we addressed the challenges of deploying
learning based ABR mechanism in real-world video streaming
systems, and proposed a novel framework for meta-learning
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 15
```text
2436
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 3, MARCH 2024
based ABR design. Based on the proposed framework, we
proposed MetaABR, a novel adaptive bitrate selection algorithm
based on meta-critic to maximize users’ QoE. MetaABR jointly
trained multiple learning tasks with a shared meta-critic, and it
could provide transferrable knowledge to supervise bitrate se-
lection across tasks. Extensive experiments based on real-world
traces and testbed showed that MetaABR achieved the best QoE
compared with the state-of-the-arts.
REFERENCES
[1] S. Krishnan and R. Sitaraman, “Video stream quality impacts viewer be-
havior: Inferring causality using quasi-experimental designs,” IEEE/ACM
Trans. Netw., vol. 21, pp. 2001–2014, Dec. 2013.
[2] T. Stockhammer, “Dynamic adaptive streaming over HTTP: Standards and
design principles,” in Proc. 2nd Annu. ACM Conf. Multimedia Syst., 2011,
pp. 133–144.
[3] T.-Y. Huang, N. Handigol, B. Heller, N. McKeown, and R. Johari, “Con-
fused, timid, and unstable: Picking a video streaming rate is hard,” in Proc.
Internet Meas. Conf., 2012, pp. 225–238.
[4] Y. Sun et al., “CS2P: Improving video bitrate selection and adaptation
with data-driven throughput prediction,” in Proc. ACM SIGCOMM Conf.,
2016, pp. 272–285.
[5] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video streaming
with pensieve,” in Proc. Conf. ACM Special Int. Group Data Commun.,
2017, pp. 197–210.
[6] Z. Li et al., “Probe and adapt: Rate adaptation for HTTP video streaming at
scale,” IEEE J. Sel. Areas Commun., vol. 32, no. 4, pp. 719–733, Apr. 2014.
[7] X. Xie, X. Zhang, S. Kumar, and L. E. Li, “piStream: Physical layer
informed adaptive video streaming over LTE,” in Proc. 21st Annu. Int.
Conf. Mobile Comput. Netw., 2015, pp. 413–425.
[8] J. Jiang, V. Sekar, and H. Zhang, “Improving fairness, efﬁciency, and
stability in HTTP-based adaptive video streaming with festive,” in Proc.
8th Int. Conf. Emerg. Netw. Experiments Technol., 2012, pp. 97–108.
[9] C. Yue, R. Jin, K. Suh, Y. Qin, B. Wang, and W. Wei, “Linkforecast:
Cellular link bandwidth prediction in LTE networks,” IEEE Trans. Mobile
Comput., vol. 17, no. 7, pp. 1582–1594, Jul. 2018.
[10] L. Mei et al., “Realtime mobile bandwidth prediction using LSTM neu-
ral network,” in Passive and Active Measurement, D. Choffnes and M.
Barcellos Eds., Cham, Switzerland: Springer, 2019, pp. 34–47.
[11] T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Watson, “A
buffer-based approach to rate adaptation: Evidence from a large video
streaming service,” in Proc. ACM Conf. SIGCOMM, 2014, pp. 187–198.
[12] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal
bitrate adaptation for online videos,” IEEE/ACM Trans. Netw., vol. 28,
no. 4, pp. 1698–1711, Aug. 2020.
[13] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic approach
for dynamic adaptive video streaming over HTTP,” in Proc. ACM Conf.
Special Int. Group Data Commun., 2015, pp. 325–338.
[14] M. Gadaleta, F. Chiariotti, M. Rossi, and A. Zanella, “D-DASH: A deep
q-learning framework for dash video streaming,” IEEE Trans. Cogn.
Commun. Netw., vol. 3, no. 4, pp. 703–718, Dec. 2017.
[15] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, “Comyco:
Quality-aware adaptive video streaming via imitation learning,” in Proc.
27th ACM Int. Conf. Multimedia, 2019, pp. 429–437.
[16] F. Y. Yan et al., “Learning in situ: A randomized experiment in video
streaming,” in Proc. 17th USENIX Symp. Networked Syst. Des. Implemen-
tation, 2020, pp. 495–511.
[17] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, “Stick: A har-
monious fusion of buffer-based and learning-based approach for adaptive
streaming,” in Proc. IEEE Conf. Comput. Commun., 2020, pp. 1967–1976.
[18] J. Quionero-Candela, M. Sugiyama, A. Schwaighofer, and N. D.
Lawrence, Dataset Shift in Machine Learning. Cambridge, MA, USA:
MIT Press, 2009.
[19] R. Taori, A. Dave, V. Shankar, N. Carlini, B. Recht, and L. Schmidt, “Mea-
suring robustness to natural distribution shifts in image classiﬁcation,” in
Advances in Neural Information Processing Systems, H. Larochelle, M.
Ranzato, R. Hadsell, M. Balcan, and H. Lin, Eds., vol. 33. Red Hook, NY,
USA: Curran Associates, Inc., 2020, pp. 18 583–18 599.
[20] J. Schmidhuber, J. Zhao, and M. A. Wiering, “Technical report IDSIA,”
Tech. Rep., vol. 69–96, pp. 1–23, 1996. [Online]. Available: https://dspace.
library.uu.nl/handle/1874/25022
[21] S. Thrun and L. Pratt, “Learning to learn: Introduction and overview,” in
Learning to Learn. Berlin, Germany: Springer, 1998, pp. 3–17.
[22] Z. Lin, G. Thomas, G. Yang, and T. Ma, “Model-based adversarial meta-
reinforcement learning,” in Proc. 34th Int. Conf. Neural Inf. Process. Syst.,
Red Hook, NY, USA: Curran Associates Inc. 2020, pp. 10161–10173.
[23] Z. Akhtar et al., “Oboe: Auto-tuning video abr algorithms to network
conditions,” in Proc. Conf. ACM Special Int. Group Data Commun., 2018,
pp. 44–58.
[24] M. Dasari, K. Kahatapitiya, S. R. Das, A. Balasubramanian, and D.
Samaras, “Swift: Adaptive video streaming with layered neural codecs,”
Proc. 19th USENIX Symp. Networked Syst. Des. Implementation, Renton,
WA, USA: USENIX Association, 2022, pp. 103–118.
[25] A. Zhang, C. Wang, B. Han, and F. Qian, “YuZu: Neural-enhanced vol-
umetric video streaming,” in Proc. 19th USENIX Symp. Networked Syst.
Des. Implementation, Renton, WA, USA: USENIX Association, 2022,
pp. 137–154.
[26] Y. Liu, B. Han, F. Qian, A. Narayanan, and Z.-L. Zhang, “Vues: Practical
mobile volumetric video streaming through multiview transcoding,” in
Proc. 28th Annu. Int. Conf. Mobile Comput. Netw., New York, NY, USA:
Association for Computing Machinery, 2022, pp. 514–527.
[27] X. Lin et al., “GSO-simulcast: Global stream orchestration in simulcast
video conferencing systems,” in Proc. ACM SIGCOMM Conf., New York,
NY, USA: Association for Computing Machinery, 2022, pp. 826–839.
[28] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, and L. Sun, “Learning tai-
lored adaptive bitrate algorithms to heterogeneous network conditions: A
domain-speciﬁc priors and meta-reinforcement learning approach,” IEEE
J. Sel. Areas Commun., vol. 40, no. 8, pp. 2485–2503, Aug. 2022.
[29] J. Li et al., “LiveNet: A low-latency video transport network for large-scale
live streaming,” in Proc. ACM SIGCOMM Conf., New York, NY, USA:
Association for Computing Machinery, 2022, pp. 812–825.
[30] B. Wu, T. Li, C. Luo, C. Ouyang, X. Du, and F. Wang, “AutoPlex:
Inter-session multiplexing congestion control for large-scale live video
services,” in Proc. ACM SIGCOMM Workshop Netw.-Application Integra-
tion, New York, NY, USA: Association for Computing Machinery, 2022,
pp. 1–6.
[31] S. Hochreiter, A. S. Younger, and P. R. Conwell, “Learning to learn using
gradient descent,” in Proc. Int. Conf. Artif. Neural Netw., 2001, pp. 87–94.
[32] D. V. Prokhorov, L. Feldkarnp, and I. Y. Tyukin, “Adaptive behavior with
ﬁxed weights in RNN: An overview,” in Proc. IEEE Int. Joint Conf. Neural
Netw., 2002, pp. 2018–2022.
[33] R. J. Williams, “Simple statistical gradient-following algorithms for
connectionist reinforcement learning,” Mach. Learn., vol. 8, no. 3/4,
pp. 229–256, 1992.
[34] C. Finn, P. Abbeel, and S. Levine, “Model-agnostic meta-learning for fast
adaptation of deep networks,” in Proc. Int. Conf. Mach. Learn., 2017,
pp. 1126–1135.
[35] C. Fernando et al., “Meta-learning by the baldwin effect,” in Proc. Genet.
Evol. Computation Conf. Companion, 2018, pp. 1313–1320.
[36] M. Jaderberg et al., “Human-level performance in 3D multiplayer
games with population-based reinforcement learning,” Science, vol. 364,
no. 6443, pp. 859–865, 2019.
[37] Z. Li, F. Zhou, F. Chen, and H. Li, “Meta-SGD: Learning to learn quickly
for few-shot learning,” 2017, arXiv:1707.09835.
[38] K. Young, B. Wang, and M. E. Taylor, “Metatrace actor-critic: Online step-
size tuning by meta-gradient descent for reinforcement learning control,”
2018, arXiv:1805.04514.
[39] N. Mishra, M. Rohaninejad, X. Chen, and P. Abbeel, “A simple neural
attentive meta-learner,” 2017, arXiv:1707.03141.
[40] Y. Duan, J. Schulman, X. Chen, P. L. Bartlett, I. Sutskever, and P. Abbeel,
“RL2: Fast reinforcement learning via slow reinforcement learning,”
2016, arXiv:1611.02779.
[41] J.Schulman,F.Wolski,P.Dhariwal,A.Radford,andO.Klimov,“Proximal
policy optimization algorithms,” 2017, arXiv:1707.06347.
[42] F. Alet, M. F. Schneider, T. Lozano-Perez, and L. P. Kaelbling, “Meta-
learning curiosity algorithms,” 2020, arXiv:2003.05325.
[43] V. Veeriah et al., “Discovery of useful questions as auxiliary tasks,”
2019, arXiv:1909.04607.
[44] Z. Zheng, J. Oh, and S. Singh, “On learning intrinsic rewards for policy
gradient methods,” 2018, arXiv:1804.06459.
[45] Z. Xu, H. van Hasselt, and D. Silver, “Meta-gradient reinforcement learn-
ing,” 2018, arXiv:1805.09801.
[46] K. Rakelly, A. Zhou, C. Finn, S. Levine, and D. Quillen, “Efﬁcient off-
policy meta-reinforcement learning via probabilistic context variables,” in
Proc. Int. Conf. Mach. Learn., 2019, pp. 5331–5340.
[47] W. Zhou, Y. Li, Y. Yang, H. Wang, and T. M. Hospedales, “Online
meta-critic learning for off-policy actor-critic methods,” 2020, arXiv:
2003.05334.
[48] A. Nagabandi et al., “Learning to adapt in dynamic, real-world environ-
ments through meta-reinforcement learning,” 2018, arXiv:1803.11347.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 16
```text
LI et al.: METAABR: A META-LEARNING APPROACH ON ADAPTATIVE BITRATE SELECTION FOR VIDEO STREAMING
2437
[49] Y. Duan et al., “One-shot imitation learning,” in Proc. Int. Conf. Neural
Inf. Process. Syst., 2017, pp. 1–12.
[50] V. Mnih et al., “Asynchronous methods for deep reinforcement learning,”
in Proc. 33rd Int. Conf. Int. Conf. Mach. Learn., 2016, pp. 1928–1937.
[51] F. Sung, L. Zhang, T. Xiang, T. M. Hospedales, and Y. Yang,
“Learning to learn: Meta-critic networks for sample efﬁcient learning,”
2017, arXiv:1706.09529.
[52] A. Gupta, R. Mendonca, Y. Liu, P. Abbeel, and S. Levine, “Meta-
reinforcement learning of structured exploration strategies,” in Proc. Int.
Conf. Neural Inf. Process. Syst., 2018, pp. 1–10.
[53] K. Rakelly, A. Zhou, D. Quillen, C. Finn, and S. Levine, “Efﬁcient off-
policy meta-reinforcement learning via probabilistic context variables,”,
2019, arXiv:1903.08254.
[54] A. G. Barto, R. S. Sutton, and C. W. Anderson, “Neuronlike adaptive
elements that can solve difﬁcult learning control problems,” IEEE Trans.
Systems, Man, Cybern., vol. 13, no. 5, pp. 834–846, Sep./Oct. 1983.
[55] I. Grondman, L. Busoniu, G. A. Lopes, and R. Babuska, “A survey of actor-
critic reinforcement learning: Standard and natural policy gradients,” IEEE
Trans. Systems, Man, Cybern. C Appl. Rev., vol. 42, no. 6, pp. 1291–1307,
Nov. 2012.
[56] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” Neural
Computation, vol. 9, no. 8, pp. 1735–1780, 1997.
[57] R. Netravali et al., “Mahimahi: Accurate record-and-replay for HTTP,” in
Proc. USENIX Annu. Tech. Conf., 2015, pp. 417–429.
[58] N. Kan, C. Li, C. Yang, W. Dai, J. Zou, and H. Xiong, “Uncertainty-aware
robust adaptive video streaming with bayesian neural network and model
predictive control,” in Proc. 31st ACM Workshop Netw. Operating Syst.
Support Digit. Audio Video, 2021, pp. 17–24.
[59] H. Riiser, P. Vigmostad, C. Griwodz, and P. Halvorsen, “Commute path
bandwidth traces from 3G networks: Analysis and applications,” in Proc.
4th ACM Multimedia Syst. Conf., 2013, pp. 114–118.
[60] “Raw data - measuring broadband America2016,” 2021. [Online].
Available:
https://www.fcc.gov/reports-research/reports/measuring-
broadband-america/raw-data-measuring-broadband-america-2016
[61] A. Bokani, M. Hassan, S. S. Kanhere, J. Yao, and G. Zhong, “Comprehen-
sive mobile bandwidth traces from vehicular networks,” in Proc. 7th Int.
Conf. Multimedia Syst., 2016, pp. 1–6.
[62] L. Mei et al., “Realtime mobile bandwidth prediction using LSTM
neural network and bayesian fusion,” Comput. Netw., vol. 182, 2020,
Art. no. 107515.
[63] D. Raca, D. Leahy, C.J. Sreenan, and J. J. Quinlan, “Beyond throughput,
the next generation: A 5G dataset with channel and context metrics,” in
Proc. 11th ACM Multimedia Syst. Conf., 2020, pp. 303–308.
[64] P. Wawrzynski, “Control policy with autocorrelated noise in reinforcement
learning for robotics,” Int. J. Mach. Learn. Comput., vol. 5, no. 2, 2015,
Art. no. 91.
Wenzhong Li (Member, IEEE) received the BS and
PhD degrees in computer science from Nanjing Uni-
versity, China. He was an Alexander von Humboldt
Scholar fellow with the University of Goettingen,
Germany. He is now a full professor with the Depart-
ment of Computer Science, Nanjing University. His
research interests include distributed computing, data
mining, mobile cloud computing, wireless networks,
pervasive computing, and social networks. He has
published more than 100 peer-review papers at inter-
national conferences and journals, which include IN-
FOCOM,UBICOMP,IJCAI,ACMMultimedia,ICDCS,IEEECommunications
Magazine, IEEE/ACM Transactions on Networking (ToN), IEEE Journal on
Selected Areas in Communications (JSAC), IEEE Transactions on Parallel and
Distributed Systems (TPDS), IEEE Transactions on Wireless Communications
(TWC), etc. He served as Program co-chair of MobiArch 2013 and Registration
Chair of ICNP 2013. He was the TPC member of several international con-
ferences and the reviewer of many journals. He is the principle investigator of
three fundings from NSFC, and the co-principle investigator of a China-Europe
international research staff exchange program. He is a member of ACM, and
China Computer Federation (CCF). He was also the winner of the Best Paper
Award of ICC 2009 and APNet 2018.
Xiang Li received the BS degree in computer science
from the Harbin Institute of Technology, China. He
is currently working toward the master’s degree with
the Department of Computer Science, Nanjing Uni-
versity. He has published several peer-review papers
at international conferences and journals including
IEEE Journal on Selected Areas in Communications
(JSAC). His research interests include media stream-
ing, network congestion control, and deep learning.
Yeting Xu received the BS degree in computer sci-
ence from Central South University, China. She is
currently working toward the master’s degree with the
Department of Computer Science, Nanjing Univer-
sity. Her research interests include media streaming,
network congestion control, and deep reinforcement
learning.
Yi Yang received the BS degree in computer science
fromNanjingUniversity,China.Heiscurrentlywork-
ing toward the PhD degree with the Department of
Computer Science, Nanjing University. His research
interests include network congestion control, rein-
forcement learning, and edge computing.
Sanglu Lu (Member, IEEE) received the BS, MS,
and PhD degrees in computer science from Nanjing
University, in 1992, 1995, and 1997, respectively.
She is currently a professor with the Department of
Computer Science and Technology and the deputy
director of State Key Laboratory for Novel Software
Technology.Herresearchinterestsincludedistributed
computing, pervasive computing, and wireless net-
works. She has published more than 100 papers in
referred journals and conferences in the above areas.
She is a member ACM.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 10:17:05 UTC from IEEE Xplore.  Restrictions apply.
```
