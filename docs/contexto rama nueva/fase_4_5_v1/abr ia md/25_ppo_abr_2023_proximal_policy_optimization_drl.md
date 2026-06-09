# PPO-ABR: Proximal Policy Optimization based Deep Reinforcement Learning for Adaptive BitRate streaming

## 0. Ficha de archivo

- Archivo fuente: `PPO-ABR_Proximal_Policy_Optimization_based_Deep_Reinforcement_Learning_for_Adaptive_BitRate_streaming.pdf`
- Paginas detectadas: 6
- SHA256 PDF: `819c3437f69ec88ca20621265224e864549d5890763a6de724127250eefeb24b`
- Texto crudo auxiliar: `raw_text/25_ppo_abr_2023_proximal_policy_optimization_drl.txt`
- Texto layout auxiliar: `raw_text_layout/25_ppo_abr_2023_proximal_policy_optimization_drl_layout.txt`
- Fecha de generacion: 2026-06-09T12:33:28

## 1. Uso previsto para Fase 4-5 v1

Fuente para PPO aplicado a ABR. Relevante para Fase 4-5 v1 como referencia de policy optimization, estado/accion/reward, entrenamiento DRL y comparacion contra A3C/Pensieve/BBA/MPC; no implica adoptar PPO por defecto.

> Nota de fidelidad: este Markdown es una extraccion tecnica densa para Codex. No es un resumen narrativo ni sustituye al PDF. Para formulas, tablas y figuras criticas, revisar siempre el PDF original.

---

## 2. Identificacion textual de primeras paginas

```text
PPO-ABR: Proximal Policy Optimization based Deep
Reinforcement Learning for Adaptive BitRate streaming
Mandan Naresh, Paresh Saxena and Manik Gupta
Dept. of CSIS, BITS Pilani
Hyderabad, India
{p20180420, psaxena, manik}@hyderabad.bits-pilani.ac.in
Abstract—Providing a high Quality of Experience (QoE) for
video streaming in 5G and beyond 5G (B5G) networks is
challenging due to the dynamic nature of the underlying network
conditions. Several Adaptive Bit Rate (ABR) algorithms have
been developed to improve QoE, but most of them are designed
based on fixed rules and unsuitable for a wide range of net-
work conditions. Recently, Deep Reinforcement Learning (DRL)
based Asynchronous Advantage Actor-Critic (A3C) methods have
recently demonstrated promise in their ability to generalise to
diverse network conditions, but they still have limitations. One
specific issue with A3C methods is the lag between each actor’s
behavior policy and central learner’s target policy. Consequently,
suboptimal updates emerge when the behavior and target policies
become out of synchronization. In this paper, we address the
problems faced by vanilla-A3C by integrating the on-policy-
based multi-agent DRL method into the existing video streaming
framework. Specifically, we propose a novel system for ABR gen-
eration - Proximal Policy Optimization-based DRL for Adaptive
Bit Rate streaming (PPO-ABR). Our proposed method improves
the overall video QoE by maximizing sample efficiency using a
clipped probability ratio between the new and the old policies on
multiple epochs of minibatch updates. The experiments on real
network traces demonstrate that PPO-ABR outperforms state-
of-the-art methods for different QoE variants.
Index Terms—Reinforcement learning, video streaming, policy
optimization, adaptive bit rate.
I. INTRODUCTION
Due to the widespread use of the Internet, the volume of
multimedia traffic has increased, including video streaming.
The Cisco annual Internet Report projects that by 2023, 69%
of the world’s population will have access to the Internet, with
Internet video traffic significantly outnumbering other Internet
traffic. In order to ensure seamless video streaming, Dynamic
Adaptive Streaming over HTTP (DASH) [1] uses an adaptive
bit rate (ABR) algorithm to send the video encoded at a
specific bitrate based on the network conditions. Several ABR
algorithms such as RB [2], BB [3], BOLA [4], and Robust-
MPC [5] use network conditions including throughput estima-
tion, playback buffer occupancy or a combination of both for
bitrate estimation with the aim to enhance the QoE for end
users. However, traditional ABR algorithms are designed with
specific network conditions and traffic pattern assumptions. As
a result, they may not perform optimally in networks where
network conditions and traffic patterns are subject to rapid
and unpredictable change. Recently, several data-driven deep
reinforcement learning (DRL) approaches, including Pensieve
[6], A2BR [7], VSiM [8], NANCY [9], AL-FFEA3C [10],
AL-AvgA3C [10], MARL-A3C [11], SAC-ABR [12] and
ALISA [13] are proposed to improve the ABR algorithms.
DRL is a branch of deep learning that deals with how agents
should behave depending on the state of the environment. In
DRL, a policy is created to maximize the expected cumulative
reward. The policy is the mapping function from states of
the environment to actions. Pensieve [6], being one of the
first DRL-based methods for ABR generation, is built upon
the basic vanilla-A3C algorithm, whereas ALISA [13], being
the latest DRL-based ABR method, utilizes soft updates with
an A3C algorithm. Both Pensieve and ALISA update the
ABR control policy based on the current network conditions
and past decisions, and it is able to identify policies that
outperform traditional ABR algorithms.
However, these state-of-the-art DRL-based methods suffer
from two key drawbacks: (i) there is a lag between each
actor’s behavior policy and the central learner’s target policy.
Consequently, suboptimal updates emerge when the behavior
and target policies become out of synchronization, and (ii)
there is a constraint on the divergence between the new and
the old policies. Due to these constraints, these algorithms
may result in imprecise throughput prediction when there are
fluctuations in the network, re-buffering at the client’s device,
and inaccurate bitrate selection impacting the overall QoE
for the end users. To resolve the above issues, we propose
the integration of Proximal Policy Optimization-based DRL
for ABR (PPO-ABR) to use a clipped probability ratio for
constraining the divergence between the new and the old policy
parameters. Our experimental results show that PPO-ABR
improves overall video QoE as compared to other state-of-
the-art methods.
The rest of the paper is organized as follows: Section II
presents the relevant background on reinforcement learning
and on-policy RL methods. Section III presents the design
of the proposed PPO-ABR algorithm. We present the experi-
mental setup and results in Section IV where we include both
training and testing results. Finally, we conclude our work in
Section V.
II. BACKGROUND
RL [14] is a learning process that is adaptive to dynamic
environments, even in cases where there is little or no prior
979-8-3503-3339-8/23/$31.00 ©2023 IEEE
199
2023 International Wireless Communications and Mobile Computing (IWCMC) | 979-8-3503-3339-8/23/$31.00 ©2023 IEEE | DOI: 10.1109/IWCMC58020.2023.10182379
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore.  Restrictions apply.
information. By learning from its mistakes, an agent seeks to
optimize its long-term return in the future. The agent’s inter-
actions with the environment are described using a Markov
decision process (MDP), where at each time step (represented
by t = 0, 1, 2, 3, ...), the agent is situated in a specific state
(st), chooses an action from a set of available actions (at ∈A),
and then receives a reward (rt = R(st, at)) based on its action.
The goal of the agent is to find a policy π(s, a) that maps
states to actions. The state-value function is given by V π
ϕ (s) =
E
"
P∞
k=0 γkrt+k|st = s, πϕ
#
and the action-value function is
given by, Qπ
ϕ(s, a) = E
"
P∞
k=0 γkrt+k|st = s, at = a, πϕ
#
```

## 3. Metadatos PDF detectados

```json
{
  "format": "PDF 1.6",
  "title": "PPO-ABR: Proximal Policy Optimization based Deep Reinforcement Learning for Adaptive BitRate streaming",
  "author": "",
  "subject": "2023 International Wireless Communications and Mobile Computing (IWCMC);2023; ; ;10.1109/IWCMC58020.2023.10182379",
  "keywords": "",
  "creator": "TeX",
  "producer": "pdfTeX-1.40.24; modified using iText® Core 7.2.4 (AGPL version) ©2000-2022 iText Group NV",
  "creationDate": "D:20230713055649-04'00'",
  "modDate": "D:20230719092722-04'00'",
  "trapped": "False",
  "encryption": null
}
```

## 4. Mapa de secciones detectado

- p. 1: I. INTRODUCTION
- p. 1: II. BACKGROUND
- p. 3: III. PROPOSED ON-POLICY ABR METHOD: PPO-ABR
- p. 3: IV. EXPERIMENTAL DETAILS AND RESULTS
- p. 3: A. Datasets
- p. 4: B. Methodologies for Training, Comparative Algorithms, and
- p. 4: HYPERPARAMETERS USED DURING THE TRAINING FOR PENSIEVE,
- p. 4: TRAINING OUTCOMES OF PENSIEVE, SAC-ABR, AND PPO-ABR
- p. 5: C. Training results
- p. 5: D. Testing results
- p. 5: TABLE III
- p. 5: ON THREE DATASETS, THE AVERAGE QOE WAS ATTAINED USING TWO
- p. 5: DIFFERENT QOE METRICS DURING SIMULATION WITH NO PACKET
- p. 6: V. CONCLUSION
- p. 6: ACKNOWLEDGMENT
- p. 6: REFERENCES
- p. 6: 2018 IEEE 26th International Conference on Network Protocols (ICNP),

## 5. Figuras, tablas, algoritmos, ecuaciones o teoremas detectados

- p. 3: Algorithm 1 presents the PPO-ABR algorithm and outlines
- p. 3: Fig. 1. System Model depicting multimedia streaming.
- p. 4: Algorithm 1 PPO-ABR Algorithm
- p. 4: TABLE I
- p. 4: Fig. 2. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was
- p. 4: TABLE II
- p. 5: Fig. 3. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was
- p. 5: Fig. 4. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was
- p. 5: Fig. 5. Performance evaluation of ABR algorithms with QoElin metric when
- p. 5: Fig. 6. Comparing PPO-ABR with current ABR methods by analyzing their
- p. 5: Figure 2 presents the average QoE value achieved by PPO-
- p. 5: TABLE III

## 6. Lineas con posible contenido matematico/formal

Estas lineas NO son LaTeX verificado. Sirven para localizar formulas, objetivos, restricciones o pseudocodigo que hay que verificar en PDF.

- p. 2: `by t = 0, 1, 2, 3, ...), the agent is situated in a specific state`
- p. 2: `(st), chooses an action from a set of available actions (at ∈A),`
- p. 2: `and then receives a reward (rt = R(st, at)) based on its action.`
- p. 2: `The goal of the agent is to find a policy π(s, a) that maps`
- p. 2: `states to actions. The state-value function is given by V π`
- p. 2: `k=0 γkrt+k|st = s, πϕ`
- p. 2: `given by, Qπ`
- p. 2: `ϕ(s, a) = E`
- p. 2: `k=0 γkrt+k|st = s, at = a, πϕ`
- p. 2: `where, γ ∈[0, 1) is a discount factor. The basic on-policy RL`
- p. 2: `∇ϕ log πϕ(at, st)|ϕkAϕ(s, a)`
- p. 2: `where Aϕ(s, a) = Qπ`
- p. 2: `ϕ(s, a) −V π`
- p. 2: `function, ∇ϕ is the policy optimization using a gradient`
- p. 2: `two components: an actor represented by a policy π and a`
- p. 2: `ϕ (st) + γV π`
- p. 2: `ϕ (st+1, ϕ) −V π`
- p. 2: `The gradient operator ∇is used to define the policy and`
- p. 2: `∆ϕ = ϕ + αpδ∇πϕ(st+1, at+1, ϕ)`
- p. 2: `∆θ = θ + αcδ∇V π`
- p. 2: `maximizeϕ V π`
- p. 2: `ϕnew(s) = κ∇V π`
- p. 2: `s ρπϕ(s) P`
- p. 2: `a πϕnew(a|s)Aϕ(s, a)`
- p. 2: `where ρπ(s) presents distribution of state-action pairs, πϕ`
- p. 2: `represents the old policy and πϕnew represents current policy.`
- p. 2: `a πϕnew(a|s)Aϕ(s, a) ≥0 aims to increase the`
- p. 2: `a πϕnew(a|s)Aϕ(s, a) < 0 can`
- p. 2: `maximizeϕ V π`
- p. 2: `ϕnew(s) = κ∇V π`
- p. 2: `ϕ (s) + κEs∼ρπϕ,a∼πϕ`
- p. 2: `subject to DKL(πϕnew||πϕ) ≤λ`
- p. 2: `where r(ϕ) =`
- p. 2: `πϕnew (s,a)`
- p. 2: `tio, DKL(πϕnew||πϕ) = P`
- p. 2: `a πϕnew(s, a) log`
- p. 2: `πϕnew (s,a)`
- p. 2: `DKL(πϕnew||πϕ) ≤λ is used to constrain the divergence`
- p. 2: `limit, λ ∈(0, 1]. We can rewrite equation (6) to maximize`
- p. 2: `maximizeϕ κEs∼ρπϕ,a∼πϕ`
- p. 2: `subject to DKL(πϕnew||πϕ) ≤λ`
- p. 2: `maximizeϕLclip(ϕnew) = κEt`
- p. 2: `subject to DKL(πϕnew||πϕ) ≤λ`
- p. 2: `where ϵ is the hyperparameter for clipping and LCP I(ϕ) =`
- p. 3: `and state input as st = (xt, dt, nt, bt, ct, lt, bwt, det). The first`
- p. 3: `reward at Line 12. The actor-network finds the policy πϕ(.|st),`
- p. 4: `7: for video vi= 1,2,3...., VI do`
- p. 4: `for chunk c=1,2,3...., C do`
- p. 4: `V θ = PK`
- p. 4: `k=1 V (st; θk) for all states st`
- p. 4: `R = V t for non terminal states st`
- p. 4: `Aϕ(s, a) = Qπ`
- p. 4: `ϕ(s, a) −V π`
- p. 4: `r(ϕ) = πϕnew (s,a)`
- p. 4: `if Aϕ(s, a) ≥0 then`
- p. 4: `Update critic parameter θnew = θ + ∂(R−V θ)2`
- p. 4: `probability hyperparameter ϵ = 0.2 determines how much the`
- p. 4: `We use nact = 16 agents for all our experiments. Finally, the`
- p. 4: `this context as follows: (i) QoElin: q(bn) = bn with rebuffer`
- p. 4: `penalty as µ = 4.3 and (ii) QoElog: q(bn) = log(b/bmin)`
- p. 4: `with µ = 2.66.`

## 7. Extraccion tecnica por categorias


### 7.1. modelo ia arquitectura algoritmo

Palabras clave usadas: `model, models, neural, architecture, algorithm, policy, agent, actor, critic, actor-critic, DQN, deep Q, Q-learning, PPO, proximal policy, A3C, reinforcement, DRL, deep reinforcement, meta reinforcement, meta-RL, meta learning, MAML, Mamba, state space, SSM, LSTM, policy network, prediction model, Pensieve, SODA, DQNReg, MetaABR, MERINA, Oboe`

**Fragmento 1 - p. 1 - score 11:**

PPO-ABR: Proximal Policy Optimization based Deep Reinforcement Learning for Adaptive BitRate streaming Mandan Naresh, Paresh Saxena and Manik Gupta Dept. of CSIS, BITS Pilani Hyderabad, India {p20180420, psaxena, manik}@hyderabad.bits-pilani.ac.in Abstract—Providing a high Quality of Experience (QoE) for video streaming in 5G and beyond 5G (B5G) networks is challenging due to the dynamic nature of the underlying network conditions. Several Adaptive Bit Rate (ABR) algorithms have been developed to improve QoE, but most of them are designed based on fixed rules and unsuitable for a wide range of net- work conditions. Recently, Deep Reinforcement Learning (DRL) based Asynchronous Advantage Actor-Critic (A3C) methods have recently demonstrated promise in their ability to generalise to diverse network conditions, but they still have limitations.

**Fragmento 2 - p. 4 - score 8:**

Hyperparameter Description Value Actor-critic algorithms γ Discount factor 0.99 Pensieve, SAC-ABR, PPO-ABR αp Actor network’s learning rate 0.0001 Pensieve, SAC-ABR, PPO-ABR αc Critic network’s learning rate 0.001 Pensieve, SAC-ABR, PPO-ABR η Entropy regularization factor range 6 to 0.01 Pensieve, SAC-ABR, PPO-ABR τ Interpolation factor 0.995 SAC-ABR ϵ clipping parameter 0.2 PPO-ABR R Random seed 42 PPO-ABR nact Total number of agents 16 Pensieve, SAC-ABR, PPO-ABR Fig. 2. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on FCC and Norway traces, and the average values were obtained. the following state-of-the-art DRL-based and non-DRL-based ABR algorithms: SAC-ABR [12], Pensieve [6], BB [3], RB [2], BOLA [4], and Robust-MPC [5].

**Fragmento 3 - p. 1 - score 7:**

DRL is a branch of deep learning that deals with how agents should behave depending on the state of the environment. In DRL, a policy is created to maximize the expected cumulative reward. The policy is the mapping function from states of the environment to actions. Pensieve [6], being one of the first DRL-based methods for ABR generation, is built upon the basic vanilla-A3C algorithm, whereas ALISA [13], being the latest DRL-based ABR method, utilizes soft updates with an A3C algorithm. Both Pensieve and ALISA update the ABR control policy based on the current network conditions and past decisions, and it is able to identify policies that outperform traditional ABR algorithms. However, these state-of-the-art DRL-based methods suffer from two key drawbacks: (i) there is a lag between each actor’s behavior policy and the central learner’s target policy.

**Fragmento 4 - p. 1 - score 7:**

One specific issue with A3C methods is the lag between each actor’s behavior policy and central learner’s target policy. Consequently, suboptimal updates emerge when the behavior and target policies become out of synchronization. In this paper, we address the problems faced by vanilla-A3C by integrating the on-policy- based multi-agent DRL method into the existing video streaming framework. Specifically, we propose a novel system for ABR gen- eration - Proximal Policy Optimization-based DRL for Adaptive Bit Rate streaming (PPO-ABR). Our proposed method improves the overall video QoE by maximizing sample efficiency using a clipped probability ratio between the new and the old policies on multiple epochs of minibatch updates.

**Fragmento 5 - p. 4 - score 7:**

Each OBOE trace stores the bandwidth measurements collected from wired, wireless, and cellular connections, and the throughput range is between 0 and 3 Mbps. B. Methodologies for Training, Comparative Algorithms, and Performance Metrics We train PPO-ABR on the aforementioned datasets for 100,000 iterations, and then we choose the model with the highest average reward. Table I summarizes the hyperpa- rameters utilized for PPO-ABR training. Specifically, clipped probability hyperparameter ϵ = 0.2 determines how much the new policy deviates from the old policy. These values have been selected based on the previous works [6], [21], and [20]. We use nact = 16 agents for all our experiments. Finally, the performance of the proposed PPO-ABR is compared to that of TABLE I HYPERPARAMETERS USED DURING THE TRAINING FOR PENSIEVE, SAC-ABR, AND PPO-ABR.

**Fragmento 6 - p. 1 - score 6:**

Several ABR algorithms such as RB [2], BB [3], BOLA [4], and Robust- MPC [5] use network conditions including throughput estima- tion, playback buffer occupancy or a combination of both for bitrate estimation with the aim to enhance the QoE for end users. However, traditional ABR algorithms are designed with specific network conditions and traffic pattern assumptions. As a result, they may not perform optimally in networks where network conditions and traffic patterns are subject to rapid and unpredictable change. Recently, several data-driven deep reinforcement learning (DRL) approaches, including Pensieve [6], A2BR [7], VSiM [8], NANCY [9], AL-FFEA3C [10], AL-AvgA3C [10], MARL-A3C [11], SAC-ABR [12] and ALISA [13] are proposed to improve the ABR algorithms.

**Fragmento 7 - p. 2 - score 6:**

Furthermore, as an improvement, vanilla-A3C [15] is proposed that uses several copies of the same agent with asynchronous updates. It is more efficient than the actor- critic methods because samples for data can be parallelized using several copies of the same agent resulting in an even smaller training time. In the vanilla-A3C algorithm, the current policy parameters (ϕnew) are updated based on previously collected experience with old policy parameters (ϕ) after every κ steps, i.e., after every κ state-action pairs. The equation below represents the value function update for vanilla-A3C is: maximizeϕ V π ϕnew(s) = κ∇V π ϕ (s) + κ P s ρπϕ(s) P a πϕnew(a|s)Aϕ(s, a) (5) where ρπ(s) presents distribution of state-action pairs, πϕ represents the old policy and πϕnew represents current policy.

**Fragmento 8 - p. 3 - score 6:**

Once the central agent has collected experience from the local agents, it updates its model parameters. Further, the central agent will make the decision to play the chunk with a specified bitrate to the chunk handler. The chunk handler sends the information about the chunk to the buffer and finally, the client will play the chunk n with quality q based on buffer occupancy. In addition to being less sample efficient, the vanilla-A3C also has a high divergence between the target policy of the central learner and every actor’s behavior policy. The subop- timal updates emerge when the behavior and target policies become out of synchronization. To address these issues, PPO- ABR uses a clipped probability ratio to constrain the KL- divergence between the new and the old policy parameters among several epochs instead of a single epoch as in vanilla- A3C.

**Fragmento 9 - p. 3 - score 6:**

Algorithm 1 presents the PPO-ABR algorithm and outlines the critical steps. The input to the algorithm is video samples, including hyperparameter setting for actor and critic networks and state input as st = (xt, dt, nt, bt, ct, lt, bwt, det). The first step is dividing a video file into chunks. Each chunk is played at a specified bitrate using the selection of the action based on the current state and the policy and to store the corresponding reward at Line 12. The actor-network finds the policy πϕ(.|st), and the critic network estimates the state value function. The second step of this algorithm is to compute the advantage function using a current policy at Line 15. The third step is Fig. 1. System Model depicting multimedia streaming.

**Fragmento 10 - p. 3 - score 6:**

Specifically, an ABR algorithm selects the bitrate for each video chunk based on chunk processor input observations, including the number of chunks (ct), chunk size (nt), chunk bitrate (lt), size of the buffer (bt), throughput (xt), and download time (dt). Additionally, the ABR controller takes the network statistics such as bandwidth (bwt) and delay (det) into account. For the state-of-the-art vanilla-A3C, the ABR controller uses multi-agent training with multiple actor and critic neural networks. Each agent is trained in parallel with its own environment based on several state inputs st = (xt, dt, nt, bt, ct, lt, bwt, det). Moreover, each agent is trained and sends the local gradients to the central agent.

**Fragmento 11 - p. 5 - score 6:**

Figure 2 presents the average QoE value achieved by PPO- ABR, SAC-ABR, and Pensieve algorithms at each training epoch. We can observe that SAC-ABR performs poorly at the initial stages of training due to high exploration. Our results show different behavior for each of these algorithms when the number of epochs increases during the training. The PPO-ABR achieves a high QoE value right from the start of the training. Similar improvements are observed with OBOE in Figure 3 and Live traces in Figure 4 as well, where Table II presents the values of QoE obtained using different ABR algorithms. D. Testing results The training models are evaluated using the Mahimahi simulator [24]. We used 250 traces from the Norway test datasets and 205 traces from the FCC test datasets to test the models, as stated in [6].

**Fragmento 12 - p. 6 - score 6:**

Gupta, “Deep reinforcement learning with importance weighted a3c for qoe enhancement in video delivery services,” arXiv preprint arXiv:2304.04527, 2023. [14] R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction. Cambridge, MA, USA: A Bradford Book, 2018. [15] V. Mnih, A. P. Badia, M. Mirza, A. Graves, T. P. Lillicrap, T. Harley, D. Silver, and K. Kavukcuoglu, “Asynchronous methods for deep reinforcement learning,” CoRR, vol. abs/1602.01783, 2016. [16] J. Schulman, S. Levine, P. Moritz, M. I. Jordan, and P. Abbeel, “Trust region policy optimization,” CoRR, vol. abs/1502.05477, 2015. [Online]. Available: http://arxiv.org/abs/1502.05477 [17] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy optimization algorithms,” CoRR, vol.

**Fragmento 13 - p. 6 - score 6:**

1–6. [10] M. Naresh, V. Das, P. Saxena, and M. Gupta, “Deep reinforcement learning based qoe-aware actor-learner architectures for video streaming in iot environments,” Computing, vol. 104, 07 2022. [11] H. Jin, Q. Wang, S. Li, and J. Chen, “Joint qos control and bitrate selec- tion for video streaming based on multi-agent reinforcement learning,” in 2020 IEEE 16th International Conference on Control & Automation (ICCA), 2020, pp. 1360–1365. [12] M. Naresh, N. Gireesh, P. Saxena, and M. Gupta, “Sac-abr: Soft actor- critic based deep reinforcement learning for adaptive bitrate streaming,” in 2022 14th International Conference on COMmunication Systems & NETworkS (COMSNETS), 2022, pp. 353–361. [13] M. Naresh, P. Saxena, and M.

**Fragmento 14 - p. 1 - score 5:**

Consequently, suboptimal updates emerge when the behavior and target policies become out of synchronization, and (ii) there is a constraint on the divergence between the new and the old policies. Due to these constraints, these algorithms may result in imprecise throughput prediction when there are fluctuations in the network, re-buffering at the client’s device, and inaccurate bitrate selection impacting the overall QoE for the end users. To resolve the above issues, we propose the integration of Proximal Policy Optimization-based DRL for ABR (PPO-ABR) to use a clipped probability ratio for constraining the divergence between the new and the old policy parameters. Our experimental results show that PPO-ABR improves overall video QoE as compared to other state-of- the-art methods.

**Fragmento 15 - p. 3 - score 5:**

The PPO-ABR trains multiple agents in parallel, so the multi-agents are trained with their environments for each batch iteration. Moreover, the actor and critic parameters are updated using PPO-clip for each batch iteration. The value function parameters are updated after multiple epochs instead of a single epoch. Further, the central agent collects the mini-batch samples and updates the gradient to the next batch iterations. Overall, PPO-ABR results in a stable update and provides the bit rate to encode the next chunk. IV. EXPERIMENTAL DETAILS AND RESULTS This section will describe the experimental methodology utilised for this study. This will include a description of the datasets used, the training method employed, the algorithms used for comparison, and the performance metrics used to assess their efficacy.

**Fragmento 16 - p. 3 - score 5:**

to compute the policy divergence between the new and the old policies using an important sampling ratio (r(ϕ)) at Line 17. The fourth step is to update the actor parameters at Line 18 using PPO-clip where 1 + ϵ occurs when the advantage estimation is positive else 1 −ϵ is used from Lines 19 to 23. The PPO-clip imposes the penalty on the r(ϕ) ratio in both cases. The fourth step is to update the critic parameter (θnew) at Line 24. The output to the algorithm is the actor-network that makes the decision to play the chunk by chunk with a specified bitrate at Line 29, the critic network evaluates the state-value of the policy with PPO-clip for maximizing rewards at Line 30 and the actor and critic parameters are updated based on the actor and the critic loss functions at Line 31.

**Fragmento 17 - p. 4 - score 5:**

Algorithm 1 PPO-ABR Algorithm 1: Input: video samples, hyperparameters; 2: Parameters: 3: Video vi; choose a video file as a input 4: Chunk c; select the bitrate for future chunks from video file 5: Initialize the batch size B, clipping parameter ϵ 6: Initialize weight parameters: θ, ϕ 7: for video vi= 1,2,3...., VI do 8: Observe initial state st; 9: for chunk c=1,2,3...., C do 10: V θ = PK k=1 V (st; θk) for all states st 11: R ←0 for terminal state sterminal 12: R = V t for non terminal states st 13: for each batch iteration do 14: Compute advantage function on B 15: Aϕ(s, a) = Qπ ϕ(s, a) −V π ϕ (s) 16: Compute the importance sampling weight 17: r(ϕ) = πϕnew (s,a) πϕ(s,a) using policy parameters 18: Update actor parameter by PPO- clip: maximizeϕLclip(ϕnew) = κEt " min LCP I(ϕ), clip(r(ϕ) , 1 −ϵ, 1 + ϵ)Aϕ(s, a) !# 19: if Aϕ(s, a) ≥0 then 20: clip(r(ϕ), 1 + ϵ)Aϕ(s, a) 21: else 22: clip(r(ϕ), 1 −ϵ)Aϕ(s, a) 23: end if 24: Update critic parameter θnew = θ + ∂(R−V θ)2 ∂θ 25: end for 26: end for 27: end for 28: Output: 29: Actor network makes the decision to play the chunk by chunk with a specified bitrate 30: Critic network evaluates the state-value of the policy with PPO-clip for maximizing rewards 31: Update actor and critic parameters θ, ϕ 500 video streaming sessions.

**Fragmento 18 - p. 6 - score 5:**

penalties. Similarly, BB likewise has a significant smoothness penalty. The PPO-ABR delivers a higher average bit rate and, in comparison, lower smoothness and rebuffering penalties. The PPO-ABR achieves an average QoE higher than the other ABR algorithms due to the combined effects of these individual components. The average QoE values attained by the ABR algorithms when evaluated on the network emulated with no packet losses are then shown in Table III for various QoE metrics. V. CONCLUSION We have shown in this study the advantages of adopt- ing on-policy DRL-based PPO-ABR to increase QoE for video streaming. Our suggested method specifically overcomes the limitations currently faced by state-of-the-art DRL-based methods and consistently achieves higher average QoE than SAC-ABR and Pensieve, respectively, by up to 13.52% and 27.42%, and even higher QoE when compared to other con- ventional fixed-rule-based ABR algorithms.

**Fragmento 19 - p. 1 - score 4:**

The experiments on real network traces demonstrate that PPO-ABR outperforms state- of-the-art methods for different QoE variants. Index Terms—Reinforcement learning, video streaming, policy optimization, adaptive bit rate. I. INTRODUCTION Due to the widespread use of the Internet, the volume of multimedia traffic has increased, including video streaming. The Cisco annual Internet Report projects that by 2023, 69% of the world’s population will have access to the Internet, with Internet video traffic significantly outnumbering other Internet traffic. In order to ensure seamless video streaming, Dynamic Adaptive Streaming over HTTP (DASH) [1] uses an adaptive bit rate (ABR) algorithm to send the video encoded at a specific bitrate based on the network conditions.

**Fragmento 20 - p. 1 - score 4:**

The rest of the paper is organized as follows: Section II presents the relevant background on reinforcement learning and on-policy RL methods. Section III presents the design of the proposed PPO-ABR algorithm. We present the experi- mental setup and results in Section IV where we include both training and testing results. Finally, we conclude our work in Section V. II. BACKGROUND RL [14] is a learning process that is adaptive to dynamic environments, even in cases where there is little or no prior 979-8-3503-3339-8/23/$31.00 ©2023 IEEE 199 2023 International Wireless Communications and Mobile Computing (IWCMC) | 979-8-3503-3339-8/23/$31.00 ©2023 IEEE | DOI: 10.1109/IWCMC58020.2023.10182379 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 21 - p. 2 - score 4:**

These methods have two components: an actor represented by a policy π and a critic represented by an estimate of the action-value function. Neural network function approximators are typically used to represent both of them. With parameters θ, the critic estimates the current policy’s value function. The main goal of this method is to reduce the variance using single-step state-value estimates. The single-step state-value estimates are derived using a temporal difference (δ), and it is given by: δ = V π ϕ (st) + γV π ϕ (st+1, ϕ) −V π ϕ (st, ϕ) (2) The gradient operator ∇is used to define the policy and critic updates with regard to its parameters ϕ and θ, respec- tively: ∆ϕ = ϕ + αpδ∇πϕ(st+1, at+1, ϕ) (3) ∆θ = θ + αcδ∇V π ϕ (st, θ) (4) where αp and αc are the actor and critic learning rates, respectively.

**Fragmento 22 - p. 2 - score 4:**

The basic on-policy RL method is a vanilla policy gradient method [15] where policy parameters are updated after the calculation of the total reward at the end of the episode instead of a single-step. The policy gradient is given by, ∇ϕk = T X t=0 ∇ϕ log πϕ(at, st)|ϕkAϕ(s, a) (1) where Aϕ(s, a) = Qπ ϕ(s, a) −V π ϕ (s) is the advantage function, ∇ϕ is the policy optimization using a gradient operator, T is the number of steps in the episode and ϕk is the current policy parameters. However, the vanilla policy gradient suffers from high variance and high training time due to value estimates being calculated at the end of the episodes instead of every time step. To address these issues, actor-critic methods [15] are proposed.

**Fragmento 23 - p. 3 - score 4:**

represents a modification of the TRPO surrogate objective using a clipped probability ratio ϵ, which ensures that the r(ϕ) remains within the range [1−ϵ, 1+ϵ]. The PPO maximization considers the minimum of the clipped and unclipped objectives resulting in a smaller divergence between the new and the old policy parameters. III. PROPOSED ON-POLICY ABR METHOD: PPO-ABR In this paper, we focus on the HTTP-based video distri- bution system, as shown in Figure 1 that utilize the DASH framework for multimedia streaming. In such systems, the videos are stored on the server in separate chunks, where each chunk is encoded with a specific bitrate. The client then requests each chunk with the appropriate bitrate from the server using an ABR algorithm, where the ABR algorithm generates the bit rate based on factors such as the available network conditions and the capabilities of the client device.

**Fragmento 24 - p. 4 - score 4:**

There also exist other QoE metric formulations, for example in [7] and [8], that can also be used for the performance evaluation. In this work, we focus only on the QoE metric defined in Equation 9. TABLE II TRAINING OUTCOMES OF PENSIEVE, SAC-ABR, AND PPO-ABR CONCERNING THE QoElin AND QoElog METRICS ACROSS MULTIPLE DATASETS. RL algorithm FCC Norway Traces OBOE Traces Live traces QoElin QoElog QoElin QoElog QoElin QoElog PPO-ABR 45.48 45.40 45.79 46.36 44.84 45.89 SAC-ABR 42.60 45.20 41.33 43.88 41.70 43.46 Pensieve 37.45 37.84 37.05 36.30 37.20 37.59 202 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 25 - p. 5 - score 4:**

At a bit rate of 12 Mbps and a latency of 30 ms throughout the testing phase, we assessed how well each ABR algorithm performed. Figure 5 displays the average total reward obtained by various ABR algorithms with the QoElin metric for each trace when the network is simulated during testing with no packet loss. According to our findings, the PPO-ABR algorithms have a higher average QoE of 46.61 than other ABR algorithms. TABLE III ON THREE DATASETS, THE AVERAGE QOE WAS ATTAINED USING TWO DIFFERENT QOE METRICS DURING SIMULATION WITH NO PACKET LOSSES. ABR algorithm FCC and Norway traces OBOE traces Live traces QoElin QoElog QoElin QoElog QoElin QoElog PPO-ABR 46.61 44.93 45.09 46.25 46.91 45.68 SAC-ABR 42.77 43.68 39.72 45.41 42.59 43.90 Pensieve 39.63 35.26 37.96 37.01 39.12 41.68 BB 12.03 12.78 14.08 20 13.81 20.26 RB 35.62 36.45 36.22 37.31 37.45 37.35 BOLA 34.26 35.30 35.04 37.09 35.82 36.05 Robust-MPC 39.93 40.44 40.18 38.29 40.59 38.99 In Figure 6, we compare various ABR algorithms using the average playback bitrate, rebuffering penalty, and smoothness penalty for the QoElin metric under emulation with no packet losses during testing in order to understand and illustrate the better performance of the PPO-ABR.

**Fragmento 26 - p. 5 - score 4:**

It takes approximately eight hours to generate the training model for every algorithm with each dataset. Table II summarizes the QoE metrics obtained during training for the three datasets. The findings indicate that across all three datasets and for both QoElin and QoElog metrics, PPO-ABR consistently outperforms SAC-ABR and Pensieve, achieving higher QoE metrics. Fig. 5. Performance evaluation of ABR algorithms with QoElin metric when tested on the model trained with FCC and Norway traces while the network is emulated with no packet loss. Fig. 6. Comparing PPO-ABR with current ABR methods by analyzing their performance on the individual elements for QoElin metric with no packet loss under emulation (Equation 9).


### 7.2. estado inputs features observaciones

Palabras clave usadas: `state, states, input, inputs, feature, features, observation, observations, throughput, bandwidth, buffer, download time, download duration, chunk size, segment size, history, past, remaining, last bitrate, network condition, QoE objective, task, environment, session, forecast, prediction, representation`

**Fragmento 1 - p. 3 - score 11:**

Specifically, an ABR algorithm selects the bitrate for each video chunk based on chunk processor input observations, including the number of chunks (ct), chunk size (nt), chunk bitrate (lt), size of the buffer (bt), throughput (xt), and download time (dt). Additionally, the ABR controller takes the network statistics such as bandwidth (bwt) and delay (det) into account. For the state-of-the-art vanilla-A3C, the ABR controller uses multi-agent training with multiple actor and critic neural networks. Each agent is trained in parallel with its own environment based on several state inputs st = (xt, dt, nt, bt, ct, lt, bwt, det). Moreover, each agent is trained and sends the local gradients to the central agent.

**Fragmento 2 - p. 1 - score 5:**

DRL is a branch of deep learning that deals with how agents should behave depending on the state of the environment. In DRL, a policy is created to maximize the expected cumulative reward. The policy is the mapping function from states of the environment to actions. Pensieve [6], being one of the first DRL-based methods for ABR generation, is built upon the basic vanilla-A3C algorithm, whereas ALISA [13], being the latest DRL-based ABR method, utilizes soft updates with an A3C algorithm. Both Pensieve and ALISA update the ABR control policy based on the current network conditions and past decisions, and it is able to identify policies that outperform traditional ABR algorithms. However, these state-of-the-art DRL-based methods suffer from two key drawbacks: (i) there is a lag between each actor’s behavior policy and the central learner’s target policy.

**Fragmento 3 - p. 1 - score 4:**

Consequently, suboptimal updates emerge when the behavior and target policies become out of synchronization, and (ii) there is a constraint on the divergence between the new and the old policies. Due to these constraints, these algorithms may result in imprecise throughput prediction when there are fluctuations in the network, re-buffering at the client’s device, and inaccurate bitrate selection impacting the overall QoE for the end users. To resolve the above issues, we propose the integration of Proximal Policy Optimization-based DRL for ABR (PPO-ABR) to use a clipped probability ratio for constraining the divergence between the new and the old policy parameters. Our experimental results show that PPO-ABR improves overall video QoE as compared to other state-of- the-art methods.

**Fragmento 4 - p. 4 - score 4:**

Algorithm 1 PPO-ABR Algorithm 1: Input: video samples, hyperparameters; 2: Parameters: 3: Video vi; choose a video file as a input 4: Chunk c; select the bitrate for future chunks from video file 5: Initialize the batch size B, clipping parameter ϵ 6: Initialize weight parameters: θ, ϕ 7: for video vi= 1,2,3...., VI do 8: Observe initial state st; 9: for chunk c=1,2,3...., C do 10: V θ = PK k=1 V (st; θk) for all states st 11: R ←0 for terminal state sterminal 12: R = V t for non terminal states st 13: for each batch iteration do 14: Compute advantage function on B 15: Aϕ(s, a) = Qπ ϕ(s, a) −V π ϕ (s) 16: Compute the importance sampling weight 17: r(ϕ) = πϕnew (s,a) πϕ(s,a) using policy parameters 18: Update actor parameter by PPO- clip: maximizeϕLclip(ϕnew) = κEt " min LCP I(ϕ), clip(r(ϕ) , 1 −ϵ, 1 + ϵ)Aϕ(s, a) !# 19: if Aϕ(s, a) ≥0 then 20: clip(r(ϕ), 1 + ϵ)Aϕ(s, a) 21: else 22: clip(r(ϕ), 1 −ϵ)Aϕ(s, a) 23: end if 24: Update critic parameter θnew = θ + ∂(R−V θ)2 ∂θ 25: end for 26: end for 27: end for 28: Output: 29: Actor network makes the decision to play the chunk by chunk with a specified bitrate 30: Critic network evaluates the state-value of the policy with PPO-clip for maximizing rewards 31: Update actor and critic parameters θ, ϕ 500 video streaming sessions.

**Fragmento 5 - p. 1 - score 3:**

Several ABR algorithms such as RB [2], BB [3], BOLA [4], and Robust- MPC [5] use network conditions including throughput estima- tion, playback buffer occupancy or a combination of both for bitrate estimation with the aim to enhance the QoE for end users. However, traditional ABR algorithms are designed with specific network conditions and traffic pattern assumptions. As a result, they may not perform optimally in networks where network conditions and traffic patterns are subject to rapid and unpredictable change. Recently, several data-driven deep reinforcement learning (DRL) approaches, including Pensieve [6], A2BR [7], VSiM [8], NANCY [9], AL-FFEA3C [10], AL-AvgA3C [10], MARL-A3C [11], SAC-ABR [12] and ALISA [13] are proposed to improve the ABR algorithms.

**Fragmento 6 - p. 2 - score 3:**

information. By learning from its mistakes, an agent seeks to optimize its long-term return in the future. The agent’s inter- actions with the environment are described using a Markov decision process (MDP), where at each time step (represented by t = 0, 1, 2, 3, ...), the agent is situated in a specific state (st), chooses an action from a set of available actions (at ∈A), and then receives a reward (rt = R(st, at)) based on its action. The goal of the agent is to find a policy π(s, a) that maps states to actions. The state-value function is given by V π ϕ (s) = E " P∞ k=0 γkrt+k|st = s, πϕ # and the action-value function is given by, Qπ ϕ(s, a) = E " P∞ k=0 γkrt+k|st = s, at = a, πϕ # where, γ ∈[0, 1) is a discount factor.

**Fragmento 7 - p. 6 - score 3:**

Future studies will examine PPO-ABR for edge-driven video distribution services and evaluate it using various QoE metric versions. ACKNOWLEDGMENT This work has been supported by TCS foundation under the TCS research scholar program, 2019-2023, India. REFERENCES [1] “ISO/IEC 23009-1:2014: Dynamic adaptive streaming over HTTP(DASH) – Part 1: Media presentation description and segment formats,” May 2014. [2] Y. Sun, X. Yin, J. Jiang, V. Sekar, F. Lin, N. Wang, T. Liu, and B. Sinopoli, “Cs2p: Improving video bitrate selection and adaptation with data-driven throughput prediction,” Proceedings of the 2016 ACM SIGCOMM Conference, 2016. [3] T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Watson, “A buffer-based approach to rate adaptation: Evidence from a large video streaming service,” in Proceedings of the 2014 ACM Conference on SIGCOMM, ser.

**Fragmento 8 - p. 1 - score 2:**

The experiments on real network traces demonstrate that PPO-ABR outperforms state- of-the-art methods for different QoE variants. Index Terms—Reinforcement learning, video streaming, policy optimization, adaptive bit rate. I. INTRODUCTION Due to the widespread use of the Internet, the volume of multimedia traffic has increased, including video streaming. The Cisco annual Internet Report projects that by 2023, 69% of the world’s population will have access to the Internet, with Internet video traffic significantly outnumbering other Internet traffic. In order to ensure seamless video streaming, Dynamic Adaptive Streaming over HTTP (DASH) [1] uses an adaptive bit rate (ABR) algorithm to send the video encoded at a specific bitrate based on the network conditions.

**Fragmento 9 - p. 3 - score 2:**

Algorithm 1 presents the PPO-ABR algorithm and outlines the critical steps. The input to the algorithm is video samples, including hyperparameter setting for actor and critic networks and state input as st = (xt, dt, nt, bt, ct, lt, bwt, det). The first step is dividing a video file into chunks. Each chunk is played at a specified bitrate using the selection of the action based on the current state and the policy and to store the corresponding reward at Line 12. The actor-network finds the policy πϕ(.|st), and the critic network estimates the state value function. The second step of this algorithm is to compute the advantage function using a current policy at Line 15. The third step is Fig. 1. System Model depicting multimedia streaming.

**Fragmento 10 - p. 4 - score 2:**

Each OBOE trace stores the bandwidth measurements collected from wired, wireless, and cellular connections, and the throughput range is between 0 and 3 Mbps. B. Methodologies for Training, Comparative Algorithms, and Performance Metrics We train PPO-ABR on the aforementioned datasets for 100,000 iterations, and then we choose the model with the highest average reward. Table I summarizes the hyperpa- rameters utilized for PPO-ABR training. Specifically, clipped probability hyperparameter ϵ = 0.2 determines how much the new policy deviates from the old policy. These values have been selected based on the previous works [6], [21], and [20]. We use nact = 16 agents for all our experiments. Finally, the performance of the proposed PPO-ABR is compared to that of TABLE I HYPERPARAMETERS USED DURING THE TRAINING FOR PENSIEVE, SAC-ABR, AND PPO-ABR.

**Fragmento 11 - p. 6 - score 2:**

penalties. Similarly, BB likewise has a significant smoothness penalty. The PPO-ABR delivers a higher average bit rate and, in comparison, lower smoothness and rebuffering penalties. The PPO-ABR achieves an average QoE higher than the other ABR algorithms due to the combined effects of these individual components. The average QoE values attained by the ABR algorithms when evaluated on the network emulated with no packet losses are then shown in Table III for various QoE metrics. V. CONCLUSION We have shown in this study the advantages of adopt- ing on-policy DRL-based PPO-ABR to increase QoE for video streaming. Our suggested method specifically overcomes the limitations currently faced by state-of-the-art DRL-based methods and consistently achieves higher average QoE than SAC-ABR and Pensieve, respectively, by up to 13.52% and 27.42%, and even higher QoE when compared to other con- ventional fixed-rule-based ABR algorithms.

**Fragmento 12 - p. 6 - score 2:**

SIGCOMM ’17. New York, NY, USA: Association for Computing Machinery, 2017, p. 197–210. [7] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, and L. Sun, “Learning tailored adaptive bitrate algorithms to heterogeneous network conditions: A domain-specific priors and meta-reinforcement learning approach,” IEEE Journal on Selected Areas in Communications, vol. 40, no. 8, pp. 2485– 2503, 2022. [8] Y. Yuan, W. Wang, Y. Wang, S. S. Adhatarao, B. Ren, K. Zheng, and X. Fu, “Vsim: Improving qoe fairness for video streaming in mobile environments,” in IEEE INFOCOM 2022 - IEEE Conference on Computer Communications, 2022, pp. 1309–1318. [9] P. Saxena, M. Naresh, M. Gupta, A. Achanta, S. Kota, and S. Gupta, “Nancy: Neural adaptive network coding methodology for video dis- tribution over wireless networks,” in GLOBECOM 2020 - 2020 IEEE Global Communications Conference, 2020, pp.

**Fragmento 13 - p. 6 - score 2:**

[21] Z. Akhtar, Y. S. Nam, R. Govindan, S. Rao, J. Chen, E. Katz-Bassett, B. Ribeiro, J. Zhan, and H. Zhang, “Oboe: Auto-tuning video abr algorithms to network conditions,” in Proceedings of the 2018 Con- ference of the ACM Special Interest Group on Data Communication, ser. SIGCOMM ’18. New York, NY, USA: Association for Computing Machinery, 2018, p. 44–58. [22] S. Sengupta, N. Ganguly, S. Chakraborty, and P. De, “Hotdash: Hotspot aware adaptive video streaming using deep reinforcement learning,” 2018 IEEE 26th International Conference on Network Protocols (ICNP), pp. 165–175, 2018. [23] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, “Stick: A harmonious fusion of buffer-based and learning-based approach for adaptive streaming,” in IEEE INFOCOM 2020-IEEE Conference on Computer Communications.

**Fragmento 14 - p. 1 - score 1:**

PPO-ABR: Proximal Policy Optimization based Deep Reinforcement Learning for Adaptive BitRate streaming Mandan Naresh, Paresh Saxena and Manik Gupta Dept. of CSIS, BITS Pilani Hyderabad, India {p20180420, psaxena, manik}@hyderabad.bits-pilani.ac.in Abstract—Providing a high Quality of Experience (QoE) for video streaming in 5G and beyond 5G (B5G) networks is challenging due to the dynamic nature of the underlying network conditions. Several Adaptive Bit Rate (ABR) algorithms have been developed to improve QoE, but most of them are designed based on fixed rules and unsuitable for a wide range of net- work conditions. Recently, Deep Reinforcement Learning (DRL) based Asynchronous Advantage Actor-Critic (A3C) methods have recently demonstrated promise in their ability to generalise to diverse network conditions, but they still have limitations.

**Fragmento 15 - p. 1 - score 1:**

The rest of the paper is organized as follows: Section II presents the relevant background on reinforcement learning and on-policy RL methods. Section III presents the design of the proposed PPO-ABR algorithm. We present the experi- mental setup and results in Section IV where we include both training and testing results. Finally, we conclude our work in Section V. II. BACKGROUND RL [14] is a learning process that is adaptive to dynamic environments, even in cases where there is little or no prior 979-8-3503-3339-8/23/$31.00 ©2023 IEEE 199 2023 International Wireless Communications and Mobile Computing (IWCMC) | 979-8-3503-3339-8/23/$31.00 ©2023 IEEE | DOI: 10.1109/IWCMC58020.2023.10182379 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 16 - p. 2 - score 1:**

These methods have two components: an actor represented by a policy π and a critic represented by an estimate of the action-value function. Neural network function approximators are typically used to represent both of them. With parameters θ, the critic estimates the current policy’s value function. The main goal of this method is to reduce the variance using single-step state-value estimates. The single-step state-value estimates are derived using a temporal difference (δ), and it is given by: δ = V π ϕ (st) + γV π ϕ (st+1, ϕ) −V π ϕ (st, ϕ) (2) The gradient operator ∇is used to define the policy and critic updates with regard to its parameters ϕ and θ, respec- tively: ∆ϕ = ϕ + αpδ∇πϕ(st+1, at+1, ϕ) (3) ∆θ = θ + αcδ∇V π ϕ (st, θ) (4) where αp and αc are the actor and critic learning rates, respectively.

**Fragmento 17 - p. 2 - score 1:**

Furthermore, as an improvement, vanilla-A3C [15] is proposed that uses several copies of the same agent with asynchronous updates. It is more efficient than the actor- critic methods because samples for data can be parallelized using several copies of the same agent resulting in an even smaller training time. In the vanilla-A3C algorithm, the current policy parameters (ϕnew) are updated based on previously collected experience with old policy parameters (ϕ) after every κ steps, i.e., after every κ state-action pairs. The equation below represents the value function update for vanilla-A3C is: maximizeϕ V π ϕnew(s) = κ∇V π ϕ (s) + κ P s ρπϕ(s) P a πϕnew(a|s)Aϕ(s, a) (5) where ρπ(s) presents distribution of state-action pairs, πϕ represents the old policy and πϕnew represents current policy.

**Fragmento 18 - p. 3 - score 1:**

represents a modification of the TRPO surrogate objective using a clipped probability ratio ϵ, which ensures that the r(ϕ) remains within the range [1−ϵ, 1+ϵ]. The PPO maximization considers the minimum of the clipped and unclipped objectives resulting in a smaller divergence between the new and the old policy parameters. III. PROPOSED ON-POLICY ABR METHOD: PPO-ABR In this paper, we focus on the HTTP-based video distri- bution system, as shown in Figure 1 that utilize the DASH framework for multimedia streaming. In such systems, the videos are stored on the server in separate chunks, where each chunk is encoded with a specific bitrate. The client then requests each chunk with the appropriate bitrate from the server using an ABR algorithm, where the ABR algorithm generates the bit rate based on factors such as the available network conditions and the capabilities of the client device.

**Fragmento 19 - p. 3 - score 1:**

Once the central agent has collected experience from the local agents, it updates its model parameters. Further, the central agent will make the decision to play the chunk with a specified bitrate to the chunk handler. The chunk handler sends the information about the chunk to the buffer and finally, the client will play the chunk n with quality q based on buffer occupancy. In addition to being less sample efficient, the vanilla-A3C also has a high divergence between the target policy of the central learner and every actor’s behavior policy. The subop- timal updates emerge when the behavior and target policies become out of synchronization. To address these issues, PPO- ABR uses a clipped probability ratio to constrain the KL- divergence between the new and the old policy parameters among several epochs instead of a single epoch as in vanilla- A3C.

**Fragmento 20 - p. 3 - score 1:**

A. Datasets We utilised multiple datasets FCC [18], Norway [19], LIVE [20], OBOE [21] for our experimentation, including both broadband and mobile datasets. First, we utilised the FCC [18] and Norway datasets [19], which include fixed broad- band technologies and Telenor’s 3G/HSDPA mobile wireless network. We utilized 59 and 68 traces from FCC and Norway throughput traces, respectively for our experiments. The range of throughput for both datasets is 0 to 6 Mbps. Secondly, we used live video streaming datasets [20], which consists of data from wireless networks such as WiFi and 4G. The throughput range of these traces is between 0.2 Mbps and 4 Mbps, and 100 traces are utilised in our experiments. Lastly, we utilised OBOE dataset [21], which include 428 traces from 201 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 21 - p. 3 - score 1:**

The PPO-ABR trains multiple agents in parallel, so the multi-agents are trained with their environments for each batch iteration. Moreover, the actor and critic parameters are updated using PPO-clip for each batch iteration. The value function parameters are updated after multiple epochs instead of a single epoch. Further, the central agent collects the mini-batch samples and updates the gradient to the next batch iterations. Overall, PPO-ABR results in a stable update and provides the bit rate to encode the next chunk. IV. EXPERIMENTAL DETAILS AND RESULTS This section will describe the experimental methodology utilised for this study. This will include a description of the datasets used, the training method employed, the algorithms used for comparison, and the performance metrics used to assess their efficacy.

**Fragmento 22 - p. 3 - score 1:**

to compute the policy divergence between the new and the old policies using an important sampling ratio (r(ϕ)) at Line 17. The fourth step is to update the actor parameters at Line 18 using PPO-clip where 1 + ϵ occurs when the advantage estimation is positive else 1 −ϵ is used from Lines 19 to 23. The PPO-clip imposes the penalty on the r(ϕ) ratio in both cases. The fourth step is to update the critic parameter (θnew) at Line 24. The output to the algorithm is the actor-network that makes the decision to play the chunk by chunk with a specified bitrate at Line 29, the critic network evaluates the state-value of the policy with PPO-clip for maximizing rewards at Line 30 and the actor and critic parameters are updated based on the actor and the critic loss functions at Line 31.

**Fragmento 23 - p. 4 - score 1:**

Hyperparameter Description Value Actor-critic algorithms γ Discount factor 0.99 Pensieve, SAC-ABR, PPO-ABR αp Actor network’s learning rate 0.0001 Pensieve, SAC-ABR, PPO-ABR αc Critic network’s learning rate 0.001 Pensieve, SAC-ABR, PPO-ABR η Entropy regularization factor range 6 to 0.01 Pensieve, SAC-ABR, PPO-ABR τ Interpolation factor 0.995 SAC-ABR ϵ clipping parameter 0.2 PPO-ABR R Random seed 42 PPO-ABR nact Total number of agents 16 Pensieve, SAC-ABR, PPO-ABR Fig. 2. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on FCC and Norway traces, and the average values were obtained. the following state-of-the-art DRL-based and non-DRL-based ABR algorithms: SAC-ABR [12], Pensieve [6], BB [3], RB [2], BOLA [4], and Robust-MPC [5].

**Fragmento 24 - p. 4 - score 1:**

We compare the performance of all ABR algorithms using QoE [12] as a metric. The QoE is expressed as: QoE = N X n=1 q(bn) −µ N X n=1 Tn − N−1 X n=1 |q(bn+1) −q(bn)| (9) The QoE is composed of three elements: (i) the total bit rates of all video chunks, (ii) the penalty incurred by re-buffering, and (iii) the video’s smoothness, which is assessed by calcu- lating the difference in bit rates used to encode consecutive chunks. Various versions of the QoE metric are examined in this context as follows: (i) QoElin: q(bn) = bn with rebuffer penalty as µ = 4.3 and (ii) QoElog: q(bn) = log(b/bmin) with µ = 2.66. Note that we have utilized the above QoE metric formula- tion since it is commonly used in several other works including Robust-MPC [5], [6], [21], [22], [23] and [12].

**Fragmento 25 - p. 5 - score 1:**

At a bit rate of 12 Mbps and a latency of 30 ms throughout the testing phase, we assessed how well each ABR algorithm performed. Figure 5 displays the average total reward obtained by various ABR algorithms with the QoElin metric for each trace when the network is simulated during testing with no packet loss. According to our findings, the PPO-ABR algorithms have a higher average QoE of 46.61 than other ABR algorithms. TABLE III ON THREE DATASETS, THE AVERAGE QOE WAS ATTAINED USING TWO DIFFERENT QOE METRICS DURING SIMULATION WITH NO PACKET LOSSES. ABR algorithm FCC and Norway traces OBOE traces Live traces QoElin QoElog QoElin QoElog QoElin QoElog PPO-ABR 46.61 44.93 45.09 46.25 46.91 45.68 SAC-ABR 42.77 43.68 39.72 45.41 42.59 43.90 Pensieve 39.63 35.26 37.96 37.01 39.12 41.68 BB 12.03 12.78 14.08 20 13.81 20.26 RB 35.62 36.45 36.22 37.31 37.45 37.35 BOLA 34.26 35.30 35.04 37.09 35.82 36.05 Robust-MPC 39.93 40.44 40.18 38.29 40.59 38.99 In Figure 6, we compare various ABR algorithms using the average playback bitrate, rebuffering penalty, and smoothness penalty for the QoElin metric under emulation with no packet losses during testing in order to understand and illustrate the better performance of the PPO-ABR.

**Fragmento 26 - p. 5 - score 1:**

Figure 2 presents the average QoE value achieved by PPO- ABR, SAC-ABR, and Pensieve algorithms at each training epoch. We can observe that SAC-ABR performs poorly at the initial stages of training due to high exploration. Our results show different behavior for each of these algorithms when the number of epochs increases during the training. The PPO-ABR achieves a high QoE value right from the start of the training. Similar improvements are observed with OBOE in Figure 3 and Live traces in Figure 4 as well, where Table II presents the values of QoE obtained using different ABR algorithms. D. Testing results The training models are evaluated using the Mahimahi simulator [24]. We used 250 traces from the Norway test datasets and 205 traces from the FCC test datasets to test the models, as stated in [6].


### 7.3. accion decision abr salida

Palabras clave usadas: `action, actions, bitrate, bit rate, quality level, representation, decision, decisions, select, selection, adaptation, output, score, guidance, recommend, priority, policy output, controller, rate adaptation, quality`

**Fragmento 1 - p. 6 - score 5:**

Future studies will examine PPO-ABR for edge-driven video distribution services and evaluate it using various QoE metric versions. ACKNOWLEDGMENT This work has been supported by TCS foundation under the TCS research scholar program, 2019-2023, India. REFERENCES [1] “ISO/IEC 23009-1:2014: Dynamic adaptive streaming over HTTP(DASH) – Part 1: Media presentation description and segment formats,” May 2014. [2] Y. Sun, X. Yin, J. Jiang, V. Sekar, F. Lin, N. Wang, T. Liu, and B. Sinopoli, “Cs2p: Improving video bitrate selection and adaptation with data-driven throughput prediction,” Proceedings of the 2016 ACM SIGCOMM Conference, 2016. [3] T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Watson, “A buffer-based approach to rate adaptation: Evidence from a large video streaming service,” in Proceedings of the 2014 ACM Conference on SIGCOMM, ser.

**Fragmento 2 - p. 1 - score 4:**

DRL is a branch of deep learning that deals with how agents should behave depending on the state of the environment. In DRL, a policy is created to maximize the expected cumulative reward. The policy is the mapping function from states of the environment to actions. Pensieve [6], being one of the first DRL-based methods for ABR generation, is built upon the basic vanilla-A3C algorithm, whereas ALISA [13], being the latest DRL-based ABR method, utilizes soft updates with an A3C algorithm. Both Pensieve and ALISA update the ABR control policy based on the current network conditions and past decisions, and it is able to identify policies that outperform traditional ABR algorithms. However, these state-of-the-art DRL-based methods suffer from two key drawbacks: (i) there is a lag between each actor’s behavior policy and the central learner’s target policy.

**Fragmento 3 - p. 3 - score 4:**

Algorithm 1 presents the PPO-ABR algorithm and outlines the critical steps. The input to the algorithm is video samples, including hyperparameter setting for actor and critic networks and state input as st = (xt, dt, nt, bt, ct, lt, bwt, det). The first step is dividing a video file into chunks. Each chunk is played at a specified bitrate using the selection of the action based on the current state and the policy and to store the corresponding reward at Line 12. The actor-network finds the policy πϕ(.|st), and the critic network estimates the state value function. The second step of this algorithm is to compute the advantage function using a current policy at Line 15. The third step is Fig. 1. System Model depicting multimedia streaming.

**Fragmento 4 - p. 4 - score 4:**

Algorithm 1 PPO-ABR Algorithm 1: Input: video samples, hyperparameters; 2: Parameters: 3: Video vi; choose a video file as a input 4: Chunk c; select the bitrate for future chunks from video file 5: Initialize the batch size B, clipping parameter ϵ 6: Initialize weight parameters: θ, ϕ 7: for video vi= 1,2,3...., VI do 8: Observe initial state st; 9: for chunk c=1,2,3...., C do 10: V θ = PK k=1 V (st; θk) for all states st 11: R ←0 for terminal state sterminal 12: R = V t for non terminal states st 13: for each batch iteration do 14: Compute advantage function on B 15: Aϕ(s, a) = Qπ ϕ(s, a) −V π ϕ (s) 16: Compute the importance sampling weight 17: r(ϕ) = πϕnew (s,a) πϕ(s,a) using policy parameters 18: Update actor parameter by PPO- clip: maximizeϕLclip(ϕnew) = κEt " min LCP I(ϕ), clip(r(ϕ) , 1 −ϵ, 1 + ϵ)Aϕ(s, a) !# 19: if Aϕ(s, a) ≥0 then 20: clip(r(ϕ), 1 + ϵ)Aϕ(s, a) 21: else 22: clip(r(ϕ), 1 −ϵ)Aϕ(s, a) 23: end if 24: Update critic parameter θnew = θ + ∂(R−V θ)2 ∂θ 25: end for 26: end for 27: end for 28: Output: 29: Actor network makes the decision to play the chunk by chunk with a specified bitrate 30: Critic network evaluates the state-value of the policy with PPO-clip for maximizing rewards 31: Update actor and critic parameters θ, ϕ 500 video streaming sessions.

**Fragmento 5 - p. 1 - score 3:**

PPO-ABR: Proximal Policy Optimization based Deep Reinforcement Learning for Adaptive BitRate streaming Mandan Naresh, Paresh Saxena and Manik Gupta Dept. of CSIS, BITS Pilani Hyderabad, India {p20180420, psaxena, manik}@hyderabad.bits-pilani.ac.in Abstract—Providing a high Quality of Experience (QoE) for video streaming in 5G and beyond 5G (B5G) networks is challenging due to the dynamic nature of the underlying network conditions. Several Adaptive Bit Rate (ABR) algorithms have been developed to improve QoE, but most of them are designed based on fixed rules and unsuitable for a wide range of net- work conditions. Recently, Deep Reinforcement Learning (DRL) based Asynchronous Advantage Actor-Critic (A3C) methods have recently demonstrated promise in their ability to generalise to diverse network conditions, but they still have limitations.

**Fragmento 6 - p. 1 - score 3:**

Consequently, suboptimal updates emerge when the behavior and target policies become out of synchronization, and (ii) there is a constraint on the divergence between the new and the old policies. Due to these constraints, these algorithms may result in imprecise throughput prediction when there are fluctuations in the network, re-buffering at the client’s device, and inaccurate bitrate selection impacting the overall QoE for the end users. To resolve the above issues, we propose the integration of Proximal Policy Optimization-based DRL for ABR (PPO-ABR) to use a clipped probability ratio for constraining the divergence between the new and the old policy parameters. Our experimental results show that PPO-ABR improves overall video QoE as compared to other state-of- the-art methods.

**Fragmento 7 - p. 2 - score 3:**

information. By learning from its mistakes, an agent seeks to optimize its long-term return in the future. The agent’s inter- actions with the environment are described using a Markov decision process (MDP), where at each time step (represented by t = 0, 1, 2, 3, ...), the agent is situated in a specific state (st), chooses an action from a set of available actions (at ∈A), and then receives a reward (rt = R(st, at)) based on its action. The goal of the agent is to find a policy π(s, a) that maps states to actions. The state-value function is given by V π ϕ (s) = E " P∞ k=0 γkrt+k|st = s, πϕ # and the action-value function is given by, Qπ ϕ(s, a) = E " P∞ k=0 γkrt+k|st = s, at = a, πϕ # where, γ ∈[0, 1) is a discount factor.

**Fragmento 8 - p. 3 - score 3:**

Once the central agent has collected experience from the local agents, it updates its model parameters. Further, the central agent will make the decision to play the chunk with a specified bitrate to the chunk handler. The chunk handler sends the information about the chunk to the buffer and finally, the client will play the chunk n with quality q based on buffer occupancy. In addition to being less sample efficient, the vanilla-A3C also has a high divergence between the target policy of the central learner and every actor’s behavior policy. The subop- timal updates emerge when the behavior and target policies become out of synchronization. To address these issues, PPO- ABR uses a clipped probability ratio to constrain the KL- divergence between the new and the old policy parameters among several epochs instead of a single epoch as in vanilla- A3C.

**Fragmento 9 - p. 3 - score 3:**

to compute the policy divergence between the new and the old policies using an important sampling ratio (r(ϕ)) at Line 17. The fourth step is to update the actor parameters at Line 18 using PPO-clip where 1 + ϵ occurs when the advantage estimation is positive else 1 −ϵ is used from Lines 19 to 23. The PPO-clip imposes the penalty on the r(ϕ) ratio in both cases. The fourth step is to update the critic parameter (θnew) at Line 24. The output to the algorithm is the actor-network that makes the decision to play the chunk by chunk with a specified bitrate at Line 29, the critic network evaluates the state-value of the policy with PPO-clip for maximizing rewards at Line 30 and the actor and critic parameters are updated based on the actor and the critic loss functions at Line 31.

**Fragmento 10 - p. 3 - score 3:**

Specifically, an ABR algorithm selects the bitrate for each video chunk based on chunk processor input observations, including the number of chunks (ct), chunk size (nt), chunk bitrate (lt), size of the buffer (bt), throughput (xt), and download time (dt). Additionally, the ABR controller takes the network statistics such as bandwidth (bwt) and delay (det) into account. For the state-of-the-art vanilla-A3C, the ABR controller uses multi-agent training with multiple actor and critic neural networks. Each agent is trained in parallel with its own environment based on several state inputs st = (xt, dt, nt, bt, ct, lt, bwt, det). Moreover, each agent is trained and sends the local gradients to the central agent.

**Fragmento 11 - p. 1 - score 2:**

The experiments on real network traces demonstrate that PPO-ABR outperforms state- of-the-art methods for different QoE variants. Index Terms—Reinforcement learning, video streaming, policy optimization, adaptive bit rate. I. INTRODUCTION Due to the widespread use of the Internet, the volume of multimedia traffic has increased, including video streaming. The Cisco annual Internet Report projects that by 2023, 69% of the world’s population will have access to the Internet, with Internet video traffic significantly outnumbering other Internet traffic. In order to ensure seamless video streaming, Dynamic Adaptive Streaming over HTTP (DASH) [1] uses an adaptive bit rate (ABR) algorithm to send the video encoded at a specific bitrate based on the network conditions.

**Fragmento 12 - p. 3 - score 2:**

represents a modification of the TRPO surrogate objective using a clipped probability ratio ϵ, which ensures that the r(ϕ) remains within the range [1−ϵ, 1+ϵ]. The PPO maximization considers the minimum of the clipped and unclipped objectives resulting in a smaller divergence between the new and the old policy parameters. III. PROPOSED ON-POLICY ABR METHOD: PPO-ABR In this paper, we focus on the HTTP-based video distri- bution system, as shown in Figure 1 that utilize the DASH framework for multimedia streaming. In such systems, the videos are stored on the server in separate chunks, where each chunk is encoded with a specific bitrate. The client then requests each chunk with the appropriate bitrate from the server using an ABR algorithm, where the ABR algorithm generates the bit rate based on factors such as the available network conditions and the capabilities of the client device.

**Fragmento 13 - p. 5 - score 2:**

At a bit rate of 12 Mbps and a latency of 30 ms throughout the testing phase, we assessed how well each ABR algorithm performed. Figure 5 displays the average total reward obtained by various ABR algorithms with the QoElin metric for each trace when the network is simulated during testing with no packet loss. According to our findings, the PPO-ABR algorithms have a higher average QoE of 46.61 than other ABR algorithms. TABLE III ON THREE DATASETS, THE AVERAGE QOE WAS ATTAINED USING TWO DIFFERENT QOE METRICS DURING SIMULATION WITH NO PACKET LOSSES. ABR algorithm FCC and Norway traces OBOE traces Live traces QoElin QoElog QoElin QoElog QoElin QoElog PPO-ABR 46.61 44.93 45.09 46.25 46.91 45.68 SAC-ABR 42.77 43.68 39.72 45.41 42.59 43.90 Pensieve 39.63 35.26 37.96 37.01 39.12 41.68 BB 12.03 12.78 14.08 20 13.81 20.26 RB 35.62 36.45 36.22 37.31 37.45 37.35 BOLA 34.26 35.30 35.04 37.09 35.82 36.05 Robust-MPC 39.93 40.44 40.18 38.29 40.59 38.99 In Figure 6, we compare various ABR algorithms using the average playback bitrate, rebuffering penalty, and smoothness penalty for the QoElin metric under emulation with no packet losses during testing in order to understand and illustrate the better performance of the PPO-ABR.

**Fragmento 14 - p. 6 - score 2:**

SIGCOMM ’17. New York, NY, USA: Association for Computing Machinery, 2017, p. 197–210. [7] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, and L. Sun, “Learning tailored adaptive bitrate algorithms to heterogeneous network conditions: A domain-specific priors and meta-reinforcement learning approach,” IEEE Journal on Selected Areas in Communications, vol. 40, no. 8, pp. 2485– 2503, 2022. [8] Y. Yuan, W. Wang, Y. Wang, S. S. Adhatarao, B. Ren, K. Zheng, and X. Fu, “Vsim: Improving qoe fairness for video streaming in mobile environments,” in IEEE INFOCOM 2022 - IEEE Conference on Computer Communications, 2022, pp. 1309–1318. [9] P. Saxena, M. Naresh, M. Gupta, A. Achanta, S. Kota, and S. Gupta, “Nancy: Neural adaptive network coding methodology for video dis- tribution over wireless networks,” in GLOBECOM 2020 - 2020 IEEE Global Communications Conference, 2020, pp.

**Fragmento 15 - p. 6 - score 2:**

SIGCOMM ’14. New York, NY, USA: Association for Computing Machinery, 2014, p. 187–198. [4] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “Bola: Near-optimal bi- trate adaptation for online videos,” in IEEE INFOCOM 2016 - The 35th Annual IEEE International Conference on Computer Communications, 2016, pp. 1–9. [5] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic approach for dynamic adaptive video streaming over http,” in Proceed- ings of the 2015 ACM Conference on Special Interest Group on Data Communication, ser. SIGCOMM ’15. New York, NY, USA: Association for Computing Machinery, 2015, p. 325–338. [6] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video stream- ing with pensieve,” in Proceedings of the Conference of the ACM Special Interest Group on Data Communication, ser.

**Fragmento 16 - p. 1 - score 1:**

Several ABR algorithms such as RB [2], BB [3], BOLA [4], and Robust- MPC [5] use network conditions including throughput estima- tion, playback buffer occupancy or a combination of both for bitrate estimation with the aim to enhance the QoE for end users. However, traditional ABR algorithms are designed with specific network conditions and traffic pattern assumptions. As a result, they may not perform optimally in networks where network conditions and traffic patterns are subject to rapid and unpredictable change. Recently, several data-driven deep reinforcement learning (DRL) approaches, including Pensieve [6], A2BR [7], VSiM [8], NANCY [9], AL-FFEA3C [10], AL-AvgA3C [10], MARL-A3C [11], SAC-ABR [12] and ALISA [13] are proposed to improve the ABR algorithms.

**Fragmento 17 - p. 1 - score 1:**

One specific issue with A3C methods is the lag between each actor’s behavior policy and central learner’s target policy. Consequently, suboptimal updates emerge when the behavior and target policies become out of synchronization. In this paper, we address the problems faced by vanilla-A3C by integrating the on-policy- based multi-agent DRL method into the existing video streaming framework. Specifically, we propose a novel system for ABR gen- eration - Proximal Policy Optimization-based DRL for Adaptive Bit Rate streaming (PPO-ABR). Our proposed method improves the overall video QoE by maximizing sample efficiency using a clipped probability ratio between the new and the old policies on multiple epochs of minibatch updates.

**Fragmento 18 - p. 2 - score 1:**

These methods have two components: an actor represented by a policy π and a critic represented by an estimate of the action-value function. Neural network function approximators are typically used to represent both of them. With parameters θ, the critic estimates the current policy’s value function. The main goal of this method is to reduce the variance using single-step state-value estimates. The single-step state-value estimates are derived using a temporal difference (δ), and it is given by: δ = V π ϕ (st) + γV π ϕ (st+1, ϕ) −V π ϕ (st, ϕ) (2) The gradient operator ∇is used to define the policy and critic updates with regard to its parameters ϕ and θ, respec- tively: ∆ϕ = ϕ + αpδ∇πϕ(st+1, at+1, ϕ) (3) ∆θ = θ + αcδ∇V π ϕ (st, θ) (4) where αp and αc are the actor and critic learning rates, respectively.

**Fragmento 19 - p. 2 - score 1:**

Furthermore, as an improvement, vanilla-A3C [15] is proposed that uses several copies of the same agent with asynchronous updates. It is more efficient than the actor- critic methods because samples for data can be parallelized using several copies of the same agent resulting in an even smaller training time. In the vanilla-A3C algorithm, the current policy parameters (ϕnew) are updated based on previously collected experience with old policy parameters (ϕ) after every κ steps, i.e., after every κ state-action pairs. The equation below represents the value function update for vanilla-A3C is: maximizeϕ V π ϕnew(s) = κ∇V π ϕ (s) + κ P s ρπϕ(s) P a πϕnew(a|s)Aϕ(s, a) (5) where ρπ(s) presents distribution of state-action pairs, πϕ represents the old policy and πϕnew represents current policy.

**Fragmento 20 - p. 3 - score 1:**

The PPO-ABR trains multiple agents in parallel, so the multi-agents are trained with their environments for each batch iteration. Moreover, the actor and critic parameters are updated using PPO-clip for each batch iteration. The value function parameters are updated after multiple epochs instead of a single epoch. Further, the central agent collects the mini-batch samples and updates the gradient to the next batch iterations. Overall, PPO-ABR results in a stable update and provides the bit rate to encode the next chunk. IV. EXPERIMENTAL DETAILS AND RESULTS This section will describe the experimental methodology utilised for this study. This will include a description of the datasets used, the training method employed, the algorithms used for comparison, and the performance metrics used to assess their efficacy.

**Fragmento 21 - p. 4 - score 1:**

Each OBOE trace stores the bandwidth measurements collected from wired, wireless, and cellular connections, and the throughput range is between 0 and 3 Mbps. B. Methodologies for Training, Comparative Algorithms, and Performance Metrics We train PPO-ABR on the aforementioned datasets for 100,000 iterations, and then we choose the model with the highest average reward. Table I summarizes the hyperpa- rameters utilized for PPO-ABR training. Specifically, clipped probability hyperparameter ϵ = 0.2 determines how much the new policy deviates from the old policy. These values have been selected based on the previous works [6], [21], and [20]. We use nact = 16 agents for all our experiments. Finally, the performance of the proposed PPO-ABR is compared to that of TABLE I HYPERPARAMETERS USED DURING THE TRAINING FOR PENSIEVE, SAC-ABR, AND PPO-ABR.

**Fragmento 22 - p. 4 - score 1:**

We compare the performance of all ABR algorithms using QoE [12] as a metric. The QoE is expressed as: QoE = N X n=1 q(bn) −µ N X n=1 Tn − N−1 X n=1 |q(bn+1) −q(bn)| (9) The QoE is composed of three elements: (i) the total bit rates of all video chunks, (ii) the penalty incurred by re-buffering, and (iii) the video’s smoothness, which is assessed by calcu- lating the difference in bit rates used to encode consecutive chunks. Various versions of the QoE metric are examined in this context as follows: (i) QoElin: q(bn) = bn with rebuffer penalty as µ = 4.3 and (ii) QoElog: q(bn) = log(b/bmin) with µ = 2.66. Note that we have utilized the above QoE metric formula- tion since it is commonly used in several other works including Robust-MPC [5], [6], [21], [22], [23] and [12].

**Fragmento 23 - p. 5 - score 1:**

Our findings indicate that, with the exception of BOLA and RB, most ABR al- gorithms attain greater bitrates. Several of these algorithms experience rebuffering penalties due to the higher bitrate choice, with BB and SAC-ABR having the biggest rebuffering 203 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 24 - p. 6 - score 1:**

penalties. Similarly, BB likewise has a significant smoothness penalty. The PPO-ABR delivers a higher average bit rate and, in comparison, lower smoothness and rebuffering penalties. The PPO-ABR achieves an average QoE higher than the other ABR algorithms due to the combined effects of these individual components. The average QoE values attained by the ABR algorithms when evaluated on the network emulated with no packet losses are then shown in Table III for various QoE metrics. V. CONCLUSION We have shown in this study the advantages of adopt- ing on-policy DRL-based PPO-ABR to increase QoE for video streaming. Our suggested method specifically overcomes the limitations currently faced by state-of-the-art DRL-based methods and consistently achieves higher average QoE than SAC-ABR and Pensieve, respectively, by up to 13.52% and 27.42%, and even higher QoE when compared to other con- ventional fixed-rule-based ABR algorithms.

**Fragmento 25 - p. 6 - score 1:**

1–6. [10] M. Naresh, V. Das, P. Saxena, and M. Gupta, “Deep reinforcement learning based qoe-aware actor-learner architectures for video streaming in iot environments,” Computing, vol. 104, 07 2022. [11] H. Jin, Q. Wang, S. Li, and J. Chen, “Joint qos control and bitrate selec- tion for video streaming based on multi-agent reinforcement learning,” in 2020 IEEE 16th International Conference on Control & Automation (ICCA), 2020, pp. 1360–1365. [12] M. Naresh, N. Gireesh, P. Saxena, and M. Gupta, “Sac-abr: Soft actor- critic based deep reinforcement learning for adaptive bitrate streaming,” in 2022 14th International Conference on COMmunication Systems & NETworkS (COMSNETS), 2022, pp. 353–361. [13] M. Naresh, P. Saxena, and M.


### 7.4. reward qoe objetivo loss

Palabras clave usadas: `reward, QoE, quality of experience, utility, objective, loss, rebuffer, stall, stalling, smoothness, switching, quality variation, bitrate smoothness, video quality, penalty, consistent, consistency, risk, tail, latency`

**Fragmento 1 - p. 5 - score 7:**

At a bit rate of 12 Mbps and a latency of 30 ms throughout the testing phase, we assessed how well each ABR algorithm performed. Figure 5 displays the average total reward obtained by various ABR algorithms with the QoElin metric for each trace when the network is simulated during testing with no packet loss. According to our findings, the PPO-ABR algorithms have a higher average QoE of 46.61 than other ABR algorithms. TABLE III ON THREE DATASETS, THE AVERAGE QOE WAS ATTAINED USING TWO DIFFERENT QOE METRICS DURING SIMULATION WITH NO PACKET LOSSES. ABR algorithm FCC and Norway traces OBOE traces Live traces QoElin QoElog QoElin QoElog QoElin QoElog PPO-ABR 46.61 44.93 45.09 46.25 46.91 45.68 SAC-ABR 42.77 43.68 39.72 45.41 42.59 43.90 Pensieve 39.63 35.26 37.96 37.01 39.12 41.68 BB 12.03 12.78 14.08 20 13.81 20.26 RB 35.62 36.45 36.22 37.31 37.45 37.35 BOLA 34.26 35.30 35.04 37.09 35.82 36.05 Robust-MPC 39.93 40.44 40.18 38.29 40.59 38.99 In Figure 6, we compare various ABR algorithms using the average playback bitrate, rebuffering penalty, and smoothness penalty for the QoElin metric under emulation with no packet losses during testing in order to understand and illustrate the better performance of the PPO-ABR.

**Fragmento 2 - p. 6 - score 6:**

penalties. Similarly, BB likewise has a significant smoothness penalty. The PPO-ABR delivers a higher average bit rate and, in comparison, lower smoothness and rebuffering penalties. The PPO-ABR achieves an average QoE higher than the other ABR algorithms due to the combined effects of these individual components. The average QoE values attained by the ABR algorithms when evaluated on the network emulated with no packet losses are then shown in Table III for various QoE metrics. V. CONCLUSION We have shown in this study the advantages of adopt- ing on-policy DRL-based PPO-ABR to increase QoE for video streaming. Our suggested method specifically overcomes the limitations currently faced by state-of-the-art DRL-based methods and consistently achieves higher average QoE than SAC-ABR and Pensieve, respectively, by up to 13.52% and 27.42%, and even higher QoE when compared to other con- ventional fixed-rule-based ABR algorithms.

**Fragmento 3 - p. 4 - score 4:**

We compare the performance of all ABR algorithms using QoE [12] as a metric. The QoE is expressed as: QoE = N X n=1 q(bn) −µ N X n=1 Tn − N−1 X n=1 |q(bn+1) −q(bn)| (9) The QoE is composed of three elements: (i) the total bit rates of all video chunks, (ii) the penalty incurred by re-buffering, and (iii) the video’s smoothness, which is assessed by calcu- lating the difference in bit rates used to encode consecutive chunks. Various versions of the QoE metric are examined in this context as follows: (i) QoElin: q(bn) = bn with rebuffer penalty as µ = 4.3 and (ii) QoElog: q(bn) = log(b/bmin) with µ = 2.66. Note that we have utilized the above QoE metric formula- tion since it is commonly used in several other works including Robust-MPC [5], [6], [21], [22], [23] and [12].

**Fragmento 4 - p. 3 - score 3:**

to compute the policy divergence between the new and the old policies using an important sampling ratio (r(ϕ)) at Line 17. The fourth step is to update the actor parameters at Line 18 using PPO-clip where 1 + ϵ occurs when the advantage estimation is positive else 1 −ϵ is used from Lines 19 to 23. The PPO-clip imposes the penalty on the r(ϕ) ratio in both cases. The fourth step is to update the critic parameter (θnew) at Line 24. The output to the algorithm is the actor-network that makes the decision to play the chunk by chunk with a specified bitrate at Line 29, the critic network evaluates the state-value of the policy with PPO-clip for maximizing rewards at Line 30 and the actor and critic parameters are updated based on the actor and the critic loss functions at Line 31.

**Fragmento 5 - p. 5 - score 3:**

It takes approximately eight hours to generate the training model for every algorithm with each dataset. Table II summarizes the QoE metrics obtained during training for the three datasets. The findings indicate that across all three datasets and for both QoElin and QoElog metrics, PPO-ABR consistently outperforms SAC-ABR and Pensieve, achieving higher QoE metrics. Fig. 5. Performance evaluation of ABR algorithms with QoElin metric when tested on the model trained with FCC and Norway traces while the network is emulated with no packet loss. Fig. 6. Comparing PPO-ABR with current ABR methods by analyzing their performance on the individual elements for QoElin metric with no packet loss under emulation (Equation 9).

**Fragmento 6 - p. 1 - score 2:**

PPO-ABR: Proximal Policy Optimization based Deep Reinforcement Learning for Adaptive BitRate streaming Mandan Naresh, Paresh Saxena and Manik Gupta Dept. of CSIS, BITS Pilani Hyderabad, India {p20180420, psaxena, manik}@hyderabad.bits-pilani.ac.in Abstract—Providing a high Quality of Experience (QoE) for video streaming in 5G and beyond 5G (B5G) networks is challenging due to the dynamic nature of the underlying network conditions. Several Adaptive Bit Rate (ABR) algorithms have been developed to improve QoE, but most of them are designed based on fixed rules and unsuitable for a wide range of net- work conditions. Recently, Deep Reinforcement Learning (DRL) based Asynchronous Advantage Actor-Critic (A3C) methods have recently demonstrated promise in their ability to generalise to diverse network conditions, but they still have limitations.

**Fragmento 7 - p. 6 - score 2:**

SIGCOMM ’17. New York, NY, USA: Association for Computing Machinery, 2017, p. 197–210. [7] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, and L. Sun, “Learning tailored adaptive bitrate algorithms to heterogeneous network conditions: A domain-specific priors and meta-reinforcement learning approach,” IEEE Journal on Selected Areas in Communications, vol. 40, no. 8, pp. 2485– 2503, 2022. [8] Y. Yuan, W. Wang, Y. Wang, S. S. Adhatarao, B. Ren, K. Zheng, and X. Fu, “Vsim: Improving qoe fairness for video streaming in mobile environments,” in IEEE INFOCOM 2022 - IEEE Conference on Computer Communications, 2022, pp. 1309–1318. [9] P. Saxena, M. Naresh, M. Gupta, A. Achanta, S. Kota, and S. Gupta, “Nancy: Neural adaptive network coding methodology for video dis- tribution over wireless networks,” in GLOBECOM 2020 - 2020 IEEE Global Communications Conference, 2020, pp.

**Fragmento 8 - p. 1 - score 1:**

DRL is a branch of deep learning that deals with how agents should behave depending on the state of the environment. In DRL, a policy is created to maximize the expected cumulative reward. The policy is the mapping function from states of the environment to actions. Pensieve [6], being one of the first DRL-based methods for ABR generation, is built upon the basic vanilla-A3C algorithm, whereas ALISA [13], being the latest DRL-based ABR method, utilizes soft updates with an A3C algorithm. Both Pensieve and ALISA update the ABR control policy based on the current network conditions and past decisions, and it is able to identify policies that outperform traditional ABR algorithms. However, these state-of-the-art DRL-based methods suffer from two key drawbacks: (i) there is a lag between each actor’s behavior policy and the central learner’s target policy.

**Fragmento 9 - p. 1 - score 1:**

Consequently, suboptimal updates emerge when the behavior and target policies become out of synchronization, and (ii) there is a constraint on the divergence between the new and the old policies. Due to these constraints, these algorithms may result in imprecise throughput prediction when there are fluctuations in the network, re-buffering at the client’s device, and inaccurate bitrate selection impacting the overall QoE for the end users. To resolve the above issues, we propose the integration of Proximal Policy Optimization-based DRL for ABR (PPO-ABR) to use a clipped probability ratio for constraining the divergence between the new and the old policy parameters. Our experimental results show that PPO-ABR improves overall video QoE as compared to other state-of- the-art methods.

**Fragmento 10 - p. 1 - score 1:**

The experiments on real network traces demonstrate that PPO-ABR outperforms state- of-the-art methods for different QoE variants. Index Terms—Reinforcement learning, video streaming, policy optimization, adaptive bit rate. I. INTRODUCTION Due to the widespread use of the Internet, the volume of multimedia traffic has increased, including video streaming. The Cisco annual Internet Report projects that by 2023, 69% of the world’s population will have access to the Internet, with Internet video traffic significantly outnumbering other Internet traffic. In order to ensure seamless video streaming, Dynamic Adaptive Streaming over HTTP (DASH) [1] uses an adaptive bit rate (ABR) algorithm to send the video encoded at a specific bitrate based on the network conditions.

**Fragmento 11 - p. 1 - score 1:**

Several ABR algorithms such as RB [2], BB [3], BOLA [4], and Robust- MPC [5] use network conditions including throughput estima- tion, playback buffer occupancy or a combination of both for bitrate estimation with the aim to enhance the QoE for end users. However, traditional ABR algorithms are designed with specific network conditions and traffic pattern assumptions. As a result, they may not perform optimally in networks where network conditions and traffic patterns are subject to rapid and unpredictable change. Recently, several data-driven deep reinforcement learning (DRL) approaches, including Pensieve [6], A2BR [7], VSiM [8], NANCY [9], AL-FFEA3C [10], AL-AvgA3C [10], MARL-A3C [11], SAC-ABR [12] and ALISA [13] are proposed to improve the ABR algorithms.

**Fragmento 12 - p. 1 - score 1:**

One specific issue with A3C methods is the lag between each actor’s behavior policy and central learner’s target policy. Consequently, suboptimal updates emerge when the behavior and target policies become out of synchronization. In this paper, we address the problems faced by vanilla-A3C by integrating the on-policy- based multi-agent DRL method into the existing video streaming framework. Specifically, we propose a novel system for ABR gen- eration - Proximal Policy Optimization-based DRL for Adaptive Bit Rate streaming (PPO-ABR). Our proposed method improves the overall video QoE by maximizing sample efficiency using a clipped probability ratio between the new and the old policies on multiple epochs of minibatch updates.

**Fragmento 13 - p. 2 - score 1:**

We can rewrite equation (6) to maximize only the second part, also known as the surrogate advantage objective, as follows: maximizeϕ κEs∼ρπϕ,a∼πϕ " r(ϕ) Aϕ(s, a) # subject to DKL(πϕnew||πϕ) ≤λ (7) Although TRPO provides constraints on the divergence between the new and the old policies, it can still lead to instability in policy updates. To address this issue, the on- policy PPO algorithm [17] is proposed that uses a clipped probability ratio to constrain the divergence between the old and the new policy parameters. The objective function in PPO is derived from Equation (7), and the maximization problem is given as: maximizeϕLclip(ϕnew) = κEt " min LCP I(ϕ), clip(r(ϕ) , 1 −ϵ, 1 + ϵ)Aϕ(s, a) !# subject to DKL(πϕnew||πϕ) ≤λ (8) where ϵ is the hyperparameter for clipping and LCP I(ϕ) = κEt " r(ϕ) Aϕ(s, a) # where CPI refers to a conservative policy iteration.

**Fragmento 14 - p. 2 - score 1:**

information. By learning from its mistakes, an agent seeks to optimize its long-term return in the future. The agent’s inter- actions with the environment are described using a Markov decision process (MDP), where at each time step (represented by t = 0, 1, 2, 3, ...), the agent is situated in a specific state (st), chooses an action from a set of available actions (at ∈A), and then receives a reward (rt = R(st, at)) based on its action. The goal of the agent is to find a policy π(s, a) that maps states to actions. The state-value function is given by V π ϕ (s) = E " P∞ k=0 γkrt+k|st = s, πϕ # and the action-value function is given by, Qπ ϕ(s, a) = E " P∞ k=0 γkrt+k|st = s, at = a, πϕ # where, γ ∈[0, 1) is a discount factor.

**Fragmento 15 - p. 2 - score 1:**

The basic on-policy RL method is a vanilla policy gradient method [15] where policy parameters are updated after the calculation of the total reward at the end of the episode instead of a single-step. The policy gradient is given by, ∇ϕk = T X t=0 ∇ϕ log πϕ(at, st)|ϕkAϕ(s, a) (1) where Aϕ(s, a) = Qπ ϕ(s, a) −V π ϕ (s) is the advantage function, ∇ϕ is the policy optimization using a gradient operator, T is the number of steps in the episode and ϕk is the current policy parameters. However, the vanilla policy gradient suffers from high variance and high training time due to value estimates being calculated at the end of the episodes instead of every time step. To address these issues, actor-critic methods [15] are proposed.

**Fragmento 16 - p. 2 - score 1:**

From Equation (8), the first term represents the TRPO unclipped surrogate objective, and the second term 200 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 17 - p. 3 - score 1:**

represents a modification of the TRPO surrogate objective using a clipped probability ratio ϵ, which ensures that the r(ϕ) remains within the range [1−ϵ, 1+ϵ]. The PPO maximization considers the minimum of the clipped and unclipped objectives resulting in a smaller divergence between the new and the old policy parameters. III. PROPOSED ON-POLICY ABR METHOD: PPO-ABR In this paper, we focus on the HTTP-based video distri- bution system, as shown in Figure 1 that utilize the DASH framework for multimedia streaming. In such systems, the videos are stored on the server in separate chunks, where each chunk is encoded with a specific bitrate. The client then requests each chunk with the appropriate bitrate from the server using an ABR algorithm, where the ABR algorithm generates the bit rate based on factors such as the available network conditions and the capabilities of the client device.

**Fragmento 18 - p. 3 - score 1:**

The PPO-ABR trains multiple agents in parallel, so the multi-agents are trained with their environments for each batch iteration. Moreover, the actor and critic parameters are updated using PPO-clip for each batch iteration. The value function parameters are updated after multiple epochs instead of a single epoch. Further, the central agent collects the mini-batch samples and updates the gradient to the next batch iterations. Overall, PPO-ABR results in a stable update and provides the bit rate to encode the next chunk. IV. EXPERIMENTAL DETAILS AND RESULTS This section will describe the experimental methodology utilised for this study. This will include a description of the datasets used, the training method employed, the algorithms used for comparison, and the performance metrics used to assess their efficacy.

**Fragmento 19 - p. 3 - score 1:**

Algorithm 1 presents the PPO-ABR algorithm and outlines the critical steps. The input to the algorithm is video samples, including hyperparameter setting for actor and critic networks and state input as st = (xt, dt, nt, bt, ct, lt, bwt, det). The first step is dividing a video file into chunks. Each chunk is played at a specified bitrate using the selection of the action based on the current state and the policy and to store the corresponding reward at Line 12. The actor-network finds the policy πϕ(.|st), and the critic network estimates the state value function. The second step of this algorithm is to compute the advantage function using a current policy at Line 15. The third step is Fig. 1. System Model depicting multimedia streaming.

**Fragmento 20 - p. 4 - score 1:**

Algorithm 1 PPO-ABR Algorithm 1: Input: video samples, hyperparameters; 2: Parameters: 3: Video vi; choose a video file as a input 4: Chunk c; select the bitrate for future chunks from video file 5: Initialize the batch size B, clipping parameter ϵ 6: Initialize weight parameters: θ, ϕ 7: for video vi= 1,2,3...., VI do 8: Observe initial state st; 9: for chunk c=1,2,3...., C do 10: V θ = PK k=1 V (st; θk) for all states st 11: R ←0 for terminal state sterminal 12: R = V t for non terminal states st 13: for each batch iteration do 14: Compute advantage function on B 15: Aϕ(s, a) = Qπ ϕ(s, a) −V π ϕ (s) 16: Compute the importance sampling weight 17: r(ϕ) = πϕnew (s,a) πϕ(s,a) using policy parameters 18: Update actor parameter by PPO- clip: maximizeϕLclip(ϕnew) = κEt " min LCP I(ϕ), clip(r(ϕ) , 1 −ϵ, 1 + ϵ)Aϕ(s, a) !# 19: if Aϕ(s, a) ≥0 then 20: clip(r(ϕ), 1 + ϵ)Aϕ(s, a) 21: else 22: clip(r(ϕ), 1 −ϵ)Aϕ(s, a) 23: end if 24: Update critic parameter θnew = θ + ∂(R−V θ)2 ∂θ 25: end for 26: end for 27: end for 28: Output: 29: Actor network makes the decision to play the chunk by chunk with a specified bitrate 30: Critic network evaluates the state-value of the policy with PPO-clip for maximizing rewards 31: Update actor and critic parameters θ, ϕ 500 video streaming sessions.

**Fragmento 21 - p. 4 - score 1:**

Each OBOE trace stores the bandwidth measurements collected from wired, wireless, and cellular connections, and the throughput range is between 0 and 3 Mbps. B. Methodologies for Training, Comparative Algorithms, and Performance Metrics We train PPO-ABR on the aforementioned datasets for 100,000 iterations, and then we choose the model with the highest average reward. Table I summarizes the hyperpa- rameters utilized for PPO-ABR training. Specifically, clipped probability hyperparameter ϵ = 0.2 determines how much the new policy deviates from the old policy. These values have been selected based on the previous works [6], [21], and [20]. We use nact = 16 agents for all our experiments. Finally, the performance of the proposed PPO-ABR is compared to that of TABLE I HYPERPARAMETERS USED DURING THE TRAINING FOR PENSIEVE, SAC-ABR, AND PPO-ABR.

**Fragmento 22 - p. 4 - score 1:**

Hyperparameter Description Value Actor-critic algorithms γ Discount factor 0.99 Pensieve, SAC-ABR, PPO-ABR αp Actor network’s learning rate 0.0001 Pensieve, SAC-ABR, PPO-ABR αc Critic network’s learning rate 0.001 Pensieve, SAC-ABR, PPO-ABR η Entropy regularization factor range 6 to 0.01 Pensieve, SAC-ABR, PPO-ABR τ Interpolation factor 0.995 SAC-ABR ϵ clipping parameter 0.2 PPO-ABR R Random seed 42 PPO-ABR nact Total number of agents 16 Pensieve, SAC-ABR, PPO-ABR Fig. 2. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on FCC and Norway traces, and the average values were obtained. the following state-of-the-art DRL-based and non-DRL-based ABR algorithms: SAC-ABR [12], Pensieve [6], BB [3], RB [2], BOLA [4], and Robust-MPC [5].

**Fragmento 23 - p. 4 - score 1:**

There also exist other QoE metric formulations, for example in [7] and [8], that can also be used for the performance evaluation. In this work, we focus only on the QoE metric defined in Equation 9. TABLE II TRAINING OUTCOMES OF PENSIEVE, SAC-ABR, AND PPO-ABR CONCERNING THE QoElin AND QoElog METRICS ACROSS MULTIPLE DATASETS. RL algorithm FCC Norway Traces OBOE Traces Live traces QoElin QoElog QoElin QoElog QoElin QoElog PPO-ABR 45.48 45.40 45.79 46.36 44.84 45.89 SAC-ABR 42.60 45.20 41.33 43.88 41.70 43.46 Pensieve 37.45 37.84 37.05 36.30 37.20 37.59 202 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 24 - p. 5 - score 1:**

Figure 2 presents the average QoE value achieved by PPO- ABR, SAC-ABR, and Pensieve algorithms at each training epoch. We can observe that SAC-ABR performs poorly at the initial stages of training due to high exploration. Our results show different behavior for each of these algorithms when the number of epochs increases during the training. The PPO-ABR achieves a high QoE value right from the start of the training. Similar improvements are observed with OBOE in Figure 3 and Live traces in Figure 4 as well, where Table II presents the values of QoE obtained using different ABR algorithms. D. Testing results The training models are evaluated using the Mahimahi simulator [24]. We used 250 traces from the Norway test datasets and 205 traces from the FCC test datasets to test the models, as stated in [6].

**Fragmento 25 - p. 5 - score 1:**

Fig. 3. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on OBOE traces, and the average values were obtained. Fig. 4. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on Live traces, and the average values were obtained. C. Training results We trained PPO-ABR, SAC-ABR, and Pensieve using the three datasets mentioned in the preceding section. Further- more, in order to maximize entropy, we utilized an entropy regularization ranging from 6 to 0.01 for a better exploration- exploitation tradeoff, i.e., initially, an entropy value of six is used for a few iterations, and then it is gradually decreased to 0.01.

**Fragmento 26 - p. 5 - score 1:**

Our findings indicate that, with the exception of BOLA and RB, most ABR al- gorithms attain greater bitrates. Several of these algorithms experience rebuffering penalties due to the higher bitrate choice, with BB and SAC-ABR having the biggest rebuffering 203 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore. Restrictions apply.


### 7.5. entrenamiento optimizacion pipeline

Palabras clave usadas: `training, train, trained, episode, epoch, optimizer, learning rate, loss function, minibatch, clipped, probability ratio, experience, simulation, simulator, emulation, testbed, fine-tuning, pretrain, learning task, meta-training, adaptation, oracle, auto-tuning, offline, online`

**Fragmento 1 - p. 3 - score 5:**

Once the central agent has collected experience from the local agents, it updates its model parameters. Further, the central agent will make the decision to play the chunk with a specified bitrate to the chunk handler. The chunk handler sends the information about the chunk to the buffer and finally, the client will play the chunk n with quality q based on buffer occupancy. In addition to being less sample efficient, the vanilla-A3C also has a high divergence between the target policy of the central learner and every actor’s behavior policy. The subop- timal updates emerge when the behavior and target policies become out of synchronization. To address these issues, PPO- ABR uses a clipped probability ratio to constrain the KL- divergence between the new and the old policy parameters among several epochs instead of a single epoch as in vanilla- A3C.

**Fragmento 2 - p. 1 - score 4:**

Consequently, suboptimal updates emerge when the behavior and target policies become out of synchronization, and (ii) there is a constraint on the divergence between the new and the old policies. Due to these constraints, these algorithms may result in imprecise throughput prediction when there are fluctuations in the network, re-buffering at the client’s device, and inaccurate bitrate selection impacting the overall QoE for the end users. To resolve the above issues, we propose the integration of Proximal Policy Optimization-based DRL for ABR (PPO-ABR) to use a clipped probability ratio for constraining the divergence between the new and the old policy parameters. Our experimental results show that PPO-ABR improves overall video QoE as compared to other state-of- the-art methods.

**Fragmento 3 - p. 1 - score 4:**

One specific issue with A3C methods is the lag between each actor’s behavior policy and central learner’s target policy. Consequently, suboptimal updates emerge when the behavior and target policies become out of synchronization. In this paper, we address the problems faced by vanilla-A3C by integrating the on-policy- based multi-agent DRL method into the existing video streaming framework. Specifically, we propose a novel system for ABR gen- eration - Proximal Policy Optimization-based DRL for Adaptive Bit Rate streaming (PPO-ABR). Our proposed method improves the overall video QoE by maximizing sample efficiency using a clipped probability ratio between the new and the old policies on multiple epochs of minibatch updates.

**Fragmento 4 - p. 3 - score 4:**

The PPO-ABR trains multiple agents in parallel, so the multi-agents are trained with their environments for each batch iteration. Moreover, the actor and critic parameters are updated using PPO-clip for each batch iteration. The value function parameters are updated after multiple epochs instead of a single epoch. Further, the central agent collects the mini-batch samples and updates the gradient to the next batch iterations. Overall, PPO-ABR results in a stable update and provides the bit rate to encode the next chunk. IV. EXPERIMENTAL DETAILS AND RESULTS This section will describe the experimental methodology utilised for this study. This will include a description of the datasets used, the training method employed, the algorithms used for comparison, and the performance metrics used to assess their efficacy.

**Fragmento 5 - p. 4 - score 4:**

Hyperparameter Description Value Actor-critic algorithms γ Discount factor 0.99 Pensieve, SAC-ABR, PPO-ABR αp Actor network’s learning rate 0.0001 Pensieve, SAC-ABR, PPO-ABR αc Critic network’s learning rate 0.001 Pensieve, SAC-ABR, PPO-ABR η Entropy regularization factor range 6 to 0.01 Pensieve, SAC-ABR, PPO-ABR τ Interpolation factor 0.995 SAC-ABR ϵ clipping parameter 0.2 PPO-ABR R Random seed 42 PPO-ABR nact Total number of agents 16 Pensieve, SAC-ABR, PPO-ABR Fig. 2. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on FCC and Norway traces, and the average values were obtained. the following state-of-the-art DRL-based and non-DRL-based ABR algorithms: SAC-ABR [12], Pensieve [6], BB [3], RB [2], BOLA [4], and Robust-MPC [5].

**Fragmento 6 - p. 5 - score 4:**

Figure 2 presents the average QoE value achieved by PPO- ABR, SAC-ABR, and Pensieve algorithms at each training epoch. We can observe that SAC-ABR performs poorly at the initial stages of training due to high exploration. Our results show different behavior for each of these algorithms when the number of epochs increases during the training. The PPO-ABR achieves a high QoE value right from the start of the training. Similar improvements are observed with OBOE in Figure 3 and Live traces in Figure 4 as well, where Table II presents the values of QoE obtained using different ABR algorithms. D. Testing results The training models are evaluated using the Mahimahi simulator [24]. We used 250 traces from the Norway test datasets and 205 traces from the FCC test datasets to test the models, as stated in [6].

**Fragmento 7 - p. 5 - score 4:**

Fig. 3. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on OBOE traces, and the average values were obtained. Fig. 4. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on Live traces, and the average values were obtained. C. Training results We trained PPO-ABR, SAC-ABR, and Pensieve using the three datasets mentioned in the preceding section. Further- more, in order to maximize entropy, we utilized an entropy regularization ranging from 6 to 0.01 for a better exploration- exploitation tradeoff, i.e., initially, an entropy value of six is used for a few iterations, and then it is gradually decreased to 0.01.

**Fragmento 8 - p. 5 - score 4:**

It takes approximately eight hours to generate the training model for every algorithm with each dataset. Table II summarizes the QoE metrics obtained during training for the three datasets. The findings indicate that across all three datasets and for both QoElin and QoElog metrics, PPO-ABR consistently outperforms SAC-ABR and Pensieve, achieving higher QoE metrics. Fig. 5. Performance evaluation of ABR algorithms with QoElin metric when tested on the model trained with FCC and Norway traces while the network is emulated with no packet loss. Fig. 6. Comparing PPO-ABR with current ABR methods by analyzing their performance on the individual elements for QoElin metric with no packet loss under emulation (Equation 9).

**Fragmento 9 - p. 2 - score 3:**

We can rewrite equation (6) to maximize only the second part, also known as the surrogate advantage objective, as follows: maximizeϕ κEs∼ρπϕ,a∼πϕ " r(ϕ) Aϕ(s, a) # subject to DKL(πϕnew||πϕ) ≤λ (7) Although TRPO provides constraints on the divergence between the new and the old policies, it can still lead to instability in policy updates. To address this issue, the on- policy PPO algorithm [17] is proposed that uses a clipped probability ratio to constrain the divergence between the old and the new policy parameters. The objective function in PPO is derived from Equation (7), and the maximization problem is given as: maximizeϕLclip(ϕnew) = κEt " min LCP I(ϕ), clip(r(ϕ) , 1 −ϵ, 1 + ϵ)Aϕ(s, a) !# subject to DKL(πϕnew||πϕ) ≤λ (8) where ϵ is the hyperparameter for clipping and LCP I(ϕ) = κEt " r(ϕ) Aϕ(s, a) # where CPI refers to a conservative policy iteration.

**Fragmento 10 - p. 2 - score 3:**

Furthermore, as an improvement, vanilla-A3C [15] is proposed that uses several copies of the same agent with asynchronous updates. It is more efficient than the actor- critic methods because samples for data can be parallelized using several copies of the same agent resulting in an even smaller training time. In the vanilla-A3C algorithm, the current policy parameters (ϕnew) are updated based on previously collected experience with old policy parameters (ϕ) after every κ steps, i.e., after every κ state-action pairs. The equation below represents the value function update for vanilla-A3C is: maximizeϕ V π ϕnew(s) = κ∇V π ϕ (s) + κ P s ρπϕ(s) P a πϕnew(a|s)Aϕ(s, a) (5) where ρπ(s) presents distribution of state-action pairs, πϕ represents the old policy and πϕnew represents current policy.

**Fragmento 11 - p. 2 - score 3:**

The basic on-policy RL method is a vanilla policy gradient method [15] where policy parameters are updated after the calculation of the total reward at the end of the episode instead of a single-step. The policy gradient is given by, ∇ϕk = T X t=0 ∇ϕ log πϕ(at, st)|ϕkAϕ(s, a) (1) where Aϕ(s, a) = Qπ ϕ(s, a) −V π ϕ (s) is the advantage function, ∇ϕ is the policy optimization using a gradient operator, T is the number of steps in the episode and ϕk is the current policy parameters. However, the vanilla policy gradient suffers from high variance and high training time due to value estimates being calculated at the end of the episodes instead of every time step. To address these issues, actor-critic methods [15] are proposed.

**Fragmento 12 - p. 3 - score 3:**

Specifically, an ABR algorithm selects the bitrate for each video chunk based on chunk processor input observations, including the number of chunks (ct), chunk size (nt), chunk bitrate (lt), size of the buffer (bt), throughput (xt), and download time (dt). Additionally, the ABR controller takes the network statistics such as bandwidth (bwt) and delay (det) into account. For the state-of-the-art vanilla-A3C, the ABR controller uses multi-agent training with multiple actor and critic neural networks. Each agent is trained in parallel with its own environment based on several state inputs st = (xt, dt, nt, bt, ct, lt, bwt, det). Moreover, each agent is trained and sends the local gradients to the central agent.

**Fragmento 13 - p. 4 - score 3:**

Each OBOE trace stores the bandwidth measurements collected from wired, wireless, and cellular connections, and the throughput range is between 0 and 3 Mbps. B. Methodologies for Training, Comparative Algorithms, and Performance Metrics We train PPO-ABR on the aforementioned datasets for 100,000 iterations, and then we choose the model with the highest average reward. Table I summarizes the hyperpa- rameters utilized for PPO-ABR training. Specifically, clipped probability hyperparameter ϵ = 0.2 determines how much the new policy deviates from the old policy. These values have been selected based on the previous works [6], [21], and [20]. We use nact = 16 agents for all our experiments. Finally, the performance of the proposed PPO-ABR is compared to that of TABLE I HYPERPARAMETERS USED DURING THE TRAINING FOR PENSIEVE, SAC-ABR, AND PPO-ABR.

**Fragmento 14 - p. 1 - score 2:**

The rest of the paper is organized as follows: Section II presents the relevant background on reinforcement learning and on-policy RL methods. Section III presents the design of the proposed PPO-ABR algorithm. We present the experi- mental setup and results in Section IV where we include both training and testing results. Finally, we conclude our work in Section V. II. BACKGROUND RL [14] is a learning process that is adaptive to dynamic environments, even in cases where there is little or no prior 979-8-3503-3339-8/23/$31.00 ©2023 IEEE 199 2023 International Wireless Communications and Mobile Computing (IWCMC) | 979-8-3503-3339-8/23/$31.00 ©2023 IEEE | DOI: 10.1109/IWCMC58020.2023.10182379 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 15 - p. 3 - score 2:**

represents a modification of the TRPO surrogate objective using a clipped probability ratio ϵ, which ensures that the r(ϕ) remains within the range [1−ϵ, 1+ϵ]. The PPO maximization considers the minimum of the clipped and unclipped objectives resulting in a smaller divergence between the new and the old policy parameters. III. PROPOSED ON-POLICY ABR METHOD: PPO-ABR In this paper, we focus on the HTTP-based video distri- bution system, as shown in Figure 1 that utilize the DASH framework for multimedia streaming. In such systems, the videos are stored on the server in separate chunks, where each chunk is encoded with a specific bitrate. The client then requests each chunk with the appropriate bitrate from the server using an ABR algorithm, where the ABR algorithm generates the bit rate based on factors such as the available network conditions and the capabilities of the client device.

**Fragmento 16 - p. 4 - score 2:**

There also exist other QoE metric formulations, for example in [7] and [8], that can also be used for the performance evaluation. In this work, we focus only on the QoE metric defined in Equation 9. TABLE II TRAINING OUTCOMES OF PENSIEVE, SAC-ABR, AND PPO-ABR CONCERNING THE QoElin AND QoElog METRICS ACROSS MULTIPLE DATASETS. RL algorithm FCC Norway Traces OBOE Traces Live traces QoElin QoElog QoElin QoElog QoElin QoElog PPO-ABR 45.48 45.40 45.79 46.36 44.84 45.89 SAC-ABR 42.60 45.20 41.33 43.88 41.70 43.46 Pensieve 37.45 37.84 37.05 36.30 37.20 37.59 202 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 17 - p. 5 - score 2:**

At a bit rate of 12 Mbps and a latency of 30 ms throughout the testing phase, we assessed how well each ABR algorithm performed. Figure 5 displays the average total reward obtained by various ABR algorithms with the QoElin metric for each trace when the network is simulated during testing with no packet loss. According to our findings, the PPO-ABR algorithms have a higher average QoE of 46.61 than other ABR algorithms. TABLE III ON THREE DATASETS, THE AVERAGE QOE WAS ATTAINED USING TWO DIFFERENT QOE METRICS DURING SIMULATION WITH NO PACKET LOSSES. ABR algorithm FCC and Norway traces OBOE traces Live traces QoElin QoElog QoElin QoElog QoElin QoElog PPO-ABR 46.61 44.93 45.09 46.25 46.91 45.68 SAC-ABR 42.77 43.68 39.72 45.41 42.59 43.90 Pensieve 39.63 35.26 37.96 37.01 39.12 41.68 BB 12.03 12.78 14.08 20 13.81 20.26 RB 35.62 36.45 36.22 37.31 37.45 37.35 BOLA 34.26 35.30 35.04 37.09 35.82 36.05 Robust-MPC 39.93 40.44 40.18 38.29 40.59 38.99 In Figure 6, we compare various ABR algorithms using the average playback bitrate, rebuffering penalty, and smoothness penalty for the QoElin metric under emulation with no packet losses during testing in order to understand and illustrate the better performance of the PPO-ABR.

**Fragmento 18 - p. 6 - score 2:**

SIGCOMM ’14. New York, NY, USA: Association for Computing Machinery, 2014, p. 187–198. [4] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “Bola: Near-optimal bi- trate adaptation for online videos,” in IEEE INFOCOM 2016 - The 35th Annual IEEE International Conference on Computer Communications, 2016, pp. 1–9. [5] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic approach for dynamic adaptive video streaming over http,” in Proceed- ings of the 2015 ACM Conference on Special Interest Group on Data Communication, ser. SIGCOMM ’15. New York, NY, USA: Association for Computing Machinery, 2015, p. 325–338. [6] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video stream- ing with pensieve,” in Proceedings of the Conference of the ACM Special Interest Group on Data Communication, ser.

**Fragmento 19 - p. 1 - score 1:**

PPO-ABR: Proximal Policy Optimization based Deep Reinforcement Learning for Adaptive BitRate streaming Mandan Naresh, Paresh Saxena and Manik Gupta Dept. of CSIS, BITS Pilani Hyderabad, India {p20180420, psaxena, manik}@hyderabad.bits-pilani.ac.in Abstract—Providing a high Quality of Experience (QoE) for video streaming in 5G and beyond 5G (B5G) networks is challenging due to the dynamic nature of the underlying network conditions. Several Adaptive Bit Rate (ABR) algorithms have been developed to improve QoE, but most of them are designed based on fixed rules and unsuitable for a wide range of net- work conditions. Recently, Deep Reinforcement Learning (DRL) based Asynchronous Advantage Actor-Critic (A3C) methods have recently demonstrated promise in their ability to generalise to diverse network conditions, but they still have limitations.

**Fragmento 20 - p. 2 - score 1:**

Note that P a πϕnew(a|s)Aϕ(s, a) ≥0 aims to increase the value function, however, P a πϕnew(a|s)Aϕ(s, a) < 0 can result in a decrease in the value function and in a increase of divergence between the old and the new policies. To alleviate this issue, the on-policy trust region policy optimization (TRPO) [16] proposes Kullback–Leibler (KL) di- vergence constraint to update the value function. The equation (5) is rewritten with KL divergence constraint as follows: maximizeϕ V π ϕnew(s) = κ∇V π ϕ (s) + κEs∼ρπϕ,a∼πϕ " r(ϕ) Aϕ(s, a) # subject to DKL(πϕnew||πϕ) ≤λ (6) where r(ϕ) = πϕnew (s,a) πϕ(s,a) is the importance sampling ra- tio, DKL(πϕnew||πϕ) = P a πϕnew(s, a) log πϕnew (s,a) πϕ(s,a) ! and DKL(πϕnew||πϕ) ≤λ is used to constrain the divergence between the new and old policies with λ as a KL-divergence limit, λ ∈(0, 1].

**Fragmento 21 - p. 2 - score 1:**

These methods have two components: an actor represented by a policy π and a critic represented by an estimate of the action-value function. Neural network function approximators are typically used to represent both of them. With parameters θ, the critic estimates the current policy’s value function. The main goal of this method is to reduce the variance using single-step state-value estimates. The single-step state-value estimates are derived using a temporal difference (δ), and it is given by: δ = V π ϕ (st) + γV π ϕ (st+1, ϕ) −V π ϕ (st, ϕ) (2) The gradient operator ∇is used to define the policy and critic updates with regard to its parameters ϕ and θ, respec- tively: ∆ϕ = ϕ + αpδ∇πϕ(st+1, at+1, ϕ) (3) ∆θ = θ + αcδ∇V π ϕ (st, θ) (4) where αp and αc are the actor and critic learning rates, respectively.

**Fragmento 22 - p. 2 - score 1:**

From Equation (8), the first term represents the TRPO unclipped surrogate objective, and the second term 200 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 23 - p. 3 - score 1:**

to compute the policy divergence between the new and the old policies using an important sampling ratio (r(ϕ)) at Line 17. The fourth step is to update the actor parameters at Line 18 using PPO-clip where 1 + ϵ occurs when the advantage estimation is positive else 1 −ϵ is used from Lines 19 to 23. The PPO-clip imposes the penalty on the r(ϕ) ratio in both cases. The fourth step is to update the critic parameter (θnew) at Line 24. The output to the algorithm is the actor-network that makes the decision to play the chunk by chunk with a specified bitrate at Line 29, the critic network evaluates the state-value of the policy with PPO-clip for maximizing rewards at Line 30 and the actor and critic parameters are updated based on the actor and the critic loss functions at Line 31.

**Fragmento 24 - p. 5 - score 1:**

Our findings indicate that, with the exception of BOLA and RB, most ABR al- gorithms attain greater bitrates. Several of these algorithms experience rebuffering penalties due to the higher bitrate choice, with BB and SAC-ABR having the biggest rebuffering 203 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 25 - p. 6 - score 1:**

Future studies will examine PPO-ABR for edge-driven video distribution services and evaluate it using various QoE metric versions. ACKNOWLEDGMENT This work has been supported by TCS foundation under the TCS research scholar program, 2019-2023, India. REFERENCES [1] “ISO/IEC 23009-1:2014: Dynamic adaptive streaming over HTTP(DASH) – Part 1: Media presentation description and segment formats,” May 2014. [2] Y. Sun, X. Yin, J. Jiang, V. Sekar, F. Lin, N. Wang, T. Liu, and B. Sinopoli, “Cs2p: Improving video bitrate selection and adaptation with data-driven throughput prediction,” Proceedings of the 2016 ACM SIGCOMM Conference, 2016. [3] T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Watson, “A buffer-based approach to rate adaptation: Evidence from a large video streaming service,” in Proceedings of the 2014 ACM Conference on SIGCOMM, ser.

**Fragmento 26 - p. 6 - score 1:**

[21] Z. Akhtar, Y. S. Nam, R. Govindan, S. Rao, J. Chen, E. Katz-Bassett, B. Ribeiro, J. Zhan, and H. Zhang, “Oboe: Auto-tuning video abr algorithms to network conditions,” in Proceedings of the 2018 Con- ference of the ACM Special Interest Group on Data Communication, ser. SIGCOMM ’18. New York, NY, USA: Association for Computing Machinery, 2018, p. 44–58. [22] S. Sengupta, N. Ganguly, S. Chakraborty, and P. De, “Hotdash: Hotspot aware adaptive video streaming using deep reinforcement learning,” 2018 IEEE 26th International Conference on Network Protocols (ICNP), pp. 165–175, 2018. [23] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, “Stick: A harmonious fusion of buffer-based and learning-based approach for adaptive streaming,” in IEEE INFOCOM 2020-IEEE Conference on Computer Communications.


### 7.6. datos trazas datasets origen

Palabras clave usadas: `dataset, datasets, trace, traces, network trace, bandwidth trace, real-world, FCC, HSDPA, Norway, LTE, 4G, 5G, WiFi, WLAN, Mahimahi, emulation, testbed, Puffer, data, sessions, users, video, chunk, streaming server`

**Fragmento 1 - p. 3 - score 11:**

A. Datasets We utilised multiple datasets FCC [18], Norway [19], LIVE [20], OBOE [21] for our experimentation, including both broadband and mobile datasets. First, we utilised the FCC [18] and Norway datasets [19], which include fixed broad- band technologies and Telenor’s 3G/HSDPA mobile wireless network. We utilized 59 and 68 traces from FCC and Norway throughput traces, respectively for our experiments. The range of throughput for both datasets is 0 to 6 Mbps. Secondly, we used live video streaming datasets [20], which consists of data from wireless networks such as WiFi and 4G. The throughput range of these traces is between 0.2 Mbps and 4 Mbps, and 100 traces are utilised in our experiments. Lastly, we utilised OBOE dataset [21], which include 428 traces from 201 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 2 - p. 5 - score 8:**

At a bit rate of 12 Mbps and a latency of 30 ms throughout the testing phase, we assessed how well each ABR algorithm performed. Figure 5 displays the average total reward obtained by various ABR algorithms with the QoElin metric for each trace when the network is simulated during testing with no packet loss. According to our findings, the PPO-ABR algorithms have a higher average QoE of 46.61 than other ABR algorithms. TABLE III ON THREE DATASETS, THE AVERAGE QOE WAS ATTAINED USING TWO DIFFERENT QOE METRICS DURING SIMULATION WITH NO PACKET LOSSES. ABR algorithm FCC and Norway traces OBOE traces Live traces QoElin QoElog QoElin QoElog QoElin QoElog PPO-ABR 46.61 44.93 45.09 46.25 46.91 45.68 SAC-ABR 42.77 43.68 39.72 45.41 42.59 43.90 Pensieve 39.63 35.26 37.96 37.01 39.12 41.68 BB 12.03 12.78 14.08 20 13.81 20.26 RB 35.62 36.45 36.22 37.31 37.45 37.35 BOLA 34.26 35.30 35.04 37.09 35.82 36.05 Robust-MPC 39.93 40.44 40.18 38.29 40.59 38.99 In Figure 6, we compare various ABR algorithms using the average playback bitrate, rebuffering penalty, and smoothness penalty for the QoElin metric under emulation with no packet losses during testing in order to understand and illustrate the better performance of the PPO-ABR.

**Fragmento 3 - p. 5 - score 8:**

Figure 2 presents the average QoE value achieved by PPO- ABR, SAC-ABR, and Pensieve algorithms at each training epoch. We can observe that SAC-ABR performs poorly at the initial stages of training due to high exploration. Our results show different behavior for each of these algorithms when the number of epochs increases during the training. The PPO-ABR achieves a high QoE value right from the start of the training. Similar improvements are observed with OBOE in Figure 3 and Live traces in Figure 4 as well, where Table II presents the values of QoE obtained using different ABR algorithms. D. Testing results The training models are evaluated using the Mahimahi simulator [24]. We used 250 traces from the Norway test datasets and 205 traces from the FCC test datasets to test the models, as stated in [6].

**Fragmento 4 - p. 5 - score 8:**

It takes approximately eight hours to generate the training model for every algorithm with each dataset. Table II summarizes the QoE metrics obtained during training for the three datasets. The findings indicate that across all three datasets and for both QoElin and QoElog metrics, PPO-ABR consistently outperforms SAC-ABR and Pensieve, achieving higher QoE metrics. Fig. 5. Performance evaluation of ABR algorithms with QoElin metric when tested on the model trained with FCC and Norway traces while the network is emulated with no packet loss. Fig. 6. Comparing PPO-ABR with current ABR methods by analyzing their performance on the individual elements for QoElin metric with no packet loss under emulation (Equation 9).

**Fragmento 5 - p. 4 - score 7:**

There also exist other QoE metric formulations, for example in [7] and [8], that can also be used for the performance evaluation. In this work, we focus only on the QoE metric defined in Equation 9. TABLE II TRAINING OUTCOMES OF PENSIEVE, SAC-ABR, AND PPO-ABR CONCERNING THE QoElin AND QoElog METRICS ACROSS MULTIPLE DATASETS. RL algorithm FCC Norway Traces OBOE Traces Live traces QoElin QoElog QoElin QoElog QoElin QoElog PPO-ABR 45.48 45.40 45.79 46.36 44.84 45.89 SAC-ABR 42.60 45.20 41.33 43.88 41.70 43.46 Pensieve 37.45 37.84 37.05 36.30 37.20 37.59 202 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 6 - p. 6 - score 6:**

abs/1707.06347, 2017. [Online]. Available: http://arxiv.org/abs/1707.06347 [18] Federal Communications Commission. (2016) Federal communications commission. 2016. raw data - measuring broadband america. [Online]. Available: https://www.fcc.gov/reports-research/reports/ measuring- broadband- america/raw- data- measuring- broadband- america- 2016 [19] H. Riiser, P. Vigmostad, C. Griwodz, and P. Halvorsen, “Commute path bandwidth traces from 3g networks: Analysis and applications,” ser. MMSys ’13. New York, NY, USA: Association for Computing Machinery, 2013, p. 114–118. [20] G. Yi, “The acm multimedia 2019 live video streaming grand challenge,” The ACM Multimedia 2019 Live Video Streaming Grand Challenge, October 21–25, 2019, Nice, France.

**Fragmento 7 - p. 5 - score 5:**

Fig. 3. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on OBOE traces, and the average values were obtained. Fig. 4. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on Live traces, and the average values were obtained. C. Training results We trained PPO-ABR, SAC-ABR, and Pensieve using the three datasets mentioned in the preceding section. Further- more, in order to maximize entropy, we utilized an entropy regularization ranging from 6 to 0.01 for a better exploration- exploitation tradeoff, i.e., initially, an entropy value of six is used for a few iterations, and then it is gradually decreased to 0.01.

**Fragmento 8 - p. 1 - score 4:**

The experiments on real network traces demonstrate that PPO-ABR outperforms state- of-the-art methods for different QoE variants. Index Terms—Reinforcement learning, video streaming, policy optimization, adaptive bit rate. I. INTRODUCTION Due to the widespread use of the Internet, the volume of multimedia traffic has increased, including video streaming. The Cisco annual Internet Report projects that by 2023, 69% of the world’s population will have access to the Internet, with Internet video traffic significantly outnumbering other Internet traffic. In order to ensure seamless video streaming, Dynamic Adaptive Streaming over HTTP (DASH) [1] uses an adaptive bit rate (ABR) algorithm to send the video encoded at a specific bitrate based on the network conditions.

**Fragmento 9 - p. 3 - score 4:**

The PPO-ABR trains multiple agents in parallel, so the multi-agents are trained with their environments for each batch iteration. Moreover, the actor and critic parameters are updated using PPO-clip for each batch iteration. The value function parameters are updated after multiple epochs instead of a single epoch. Further, the central agent collects the mini-batch samples and updates the gradient to the next batch iterations. Overall, PPO-ABR results in a stable update and provides the bit rate to encode the next chunk. IV. EXPERIMENTAL DETAILS AND RESULTS This section will describe the experimental methodology utilised for this study. This will include a description of the datasets used, the training method employed, the algorithms used for comparison, and the performance metrics used to assess their efficacy.

**Fragmento 10 - p. 4 - score 4:**

Each OBOE trace stores the bandwidth measurements collected from wired, wireless, and cellular connections, and the throughput range is between 0 and 3 Mbps. B. Methodologies for Training, Comparative Algorithms, and Performance Metrics We train PPO-ABR on the aforementioned datasets for 100,000 iterations, and then we choose the model with the highest average reward. Table I summarizes the hyperpa- rameters utilized for PPO-ABR training. Specifically, clipped probability hyperparameter ϵ = 0.2 determines how much the new policy deviates from the old policy. These values have been selected based on the previous works [6], [21], and [20]. We use nact = 16 agents for all our experiments. Finally, the performance of the proposed PPO-ABR is compared to that of TABLE I HYPERPARAMETERS USED DURING THE TRAINING FOR PENSIEVE, SAC-ABR, AND PPO-ABR.

**Fragmento 11 - p. 4 - score 4:**

Hyperparameter Description Value Actor-critic algorithms γ Discount factor 0.99 Pensieve, SAC-ABR, PPO-ABR αp Actor network’s learning rate 0.0001 Pensieve, SAC-ABR, PPO-ABR αc Critic network’s learning rate 0.001 Pensieve, SAC-ABR, PPO-ABR η Entropy regularization factor range 6 to 0.01 Pensieve, SAC-ABR, PPO-ABR τ Interpolation factor 0.995 SAC-ABR ϵ clipping parameter 0.2 PPO-ABR R Random seed 42 PPO-ABR nact Total number of agents 16 Pensieve, SAC-ABR, PPO-ABR Fig. 2. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on FCC and Norway traces, and the average values were obtained. the following state-of-the-art DRL-based and non-DRL-based ABR algorithms: SAC-ABR [12], Pensieve [6], BB [3], RB [2], BOLA [4], and Robust-MPC [5].

**Fragmento 12 - p. 4 - score 3:**

Algorithm 1 PPO-ABR Algorithm 1: Input: video samples, hyperparameters; 2: Parameters: 3: Video vi; choose a video file as a input 4: Chunk c; select the bitrate for future chunks from video file 5: Initialize the batch size B, clipping parameter ϵ 6: Initialize weight parameters: θ, ϕ 7: for video vi= 1,2,3...., VI do 8: Observe initial state st; 9: for chunk c=1,2,3...., C do 10: V θ = PK k=1 V (st; θk) for all states st 11: R ←0 for terminal state sterminal 12: R = V t for non terminal states st 13: for each batch iteration do 14: Compute advantage function on B 15: Aϕ(s, a) = Qπ ϕ(s, a) −V π ϕ (s) 16: Compute the importance sampling weight 17: r(ϕ) = πϕnew (s,a) πϕ(s,a) using policy parameters 18: Update actor parameter by PPO- clip: maximizeϕLclip(ϕnew) = κEt " min LCP I(ϕ), clip(r(ϕ) , 1 −ϵ, 1 + ϵ)Aϕ(s, a) !# 19: if Aϕ(s, a) ≥0 then 20: clip(r(ϕ), 1 + ϵ)Aϕ(s, a) 21: else 22: clip(r(ϕ), 1 −ϵ)Aϕ(s, a) 23: end if 24: Update critic parameter θnew = θ + ∂(R−V θ)2 ∂θ 25: end for 26: end for 27: end for 28: Output: 29: Actor network makes the decision to play the chunk by chunk with a specified bitrate 30: Critic network evaluates the state-value of the policy with PPO-clip for maximizing rewards 31: Update actor and critic parameters θ, ϕ 500 video streaming sessions.

**Fragmento 13 - p. 1 - score 2:**

PPO-ABR: Proximal Policy Optimization based Deep Reinforcement Learning for Adaptive BitRate streaming Mandan Naresh, Paresh Saxena and Manik Gupta Dept. of CSIS, BITS Pilani Hyderabad, India {p20180420, psaxena, manik}@hyderabad.bits-pilani.ac.in Abstract—Providing a high Quality of Experience (QoE) for video streaming in 5G and beyond 5G (B5G) networks is challenging due to the dynamic nature of the underlying network conditions. Several Adaptive Bit Rate (ABR) algorithms have been developed to improve QoE, but most of them are designed based on fixed rules and unsuitable for a wide range of net- work conditions. Recently, Deep Reinforcement Learning (DRL) based Asynchronous Advantage Actor-Critic (A3C) methods have recently demonstrated promise in their ability to generalise to diverse network conditions, but they still have limitations.

**Fragmento 14 - p. 1 - score 2:**

Consequently, suboptimal updates emerge when the behavior and target policies become out of synchronization, and (ii) there is a constraint on the divergence between the new and the old policies. Due to these constraints, these algorithms may result in imprecise throughput prediction when there are fluctuations in the network, re-buffering at the client’s device, and inaccurate bitrate selection impacting the overall QoE for the end users. To resolve the above issues, we propose the integration of Proximal Policy Optimization-based DRL for ABR (PPO-ABR) to use a clipped probability ratio for constraining the divergence between the new and the old policy parameters. Our experimental results show that PPO-ABR improves overall video QoE as compared to other state-of- the-art methods.

**Fragmento 15 - p. 1 - score 2:**

Several ABR algorithms such as RB [2], BB [3], BOLA [4], and Robust- MPC [5] use network conditions including throughput estima- tion, playback buffer occupancy or a combination of both for bitrate estimation with the aim to enhance the QoE for end users. However, traditional ABR algorithms are designed with specific network conditions and traffic pattern assumptions. As a result, they may not perform optimally in networks where network conditions and traffic patterns are subject to rapid and unpredictable change. Recently, several data-driven deep reinforcement learning (DRL) approaches, including Pensieve [6], A2BR [7], VSiM [8], NANCY [9], AL-FFEA3C [10], AL-AvgA3C [10], MARL-A3C [11], SAC-ABR [12] and ALISA [13] are proposed to improve the ABR algorithms.

**Fragmento 16 - p. 3 - score 2:**

represents a modification of the TRPO surrogate objective using a clipped probability ratio ϵ, which ensures that the r(ϕ) remains within the range [1−ϵ, 1+ϵ]. The PPO maximization considers the minimum of the clipped and unclipped objectives resulting in a smaller divergence between the new and the old policy parameters. III. PROPOSED ON-POLICY ABR METHOD: PPO-ABR In this paper, we focus on the HTTP-based video distri- bution system, as shown in Figure 1 that utilize the DASH framework for multimedia streaming. In such systems, the videos are stored on the server in separate chunks, where each chunk is encoded with a specific bitrate. The client then requests each chunk with the appropriate bitrate from the server using an ABR algorithm, where the ABR algorithm generates the bit rate based on factors such as the available network conditions and the capabilities of the client device.

**Fragmento 17 - p. 3 - score 2:**

Algorithm 1 presents the PPO-ABR algorithm and outlines the critical steps. The input to the algorithm is video samples, including hyperparameter setting for actor and critic networks and state input as st = (xt, dt, nt, bt, ct, lt, bwt, det). The first step is dividing a video file into chunks. Each chunk is played at a specified bitrate using the selection of the action based on the current state and the policy and to store the corresponding reward at Line 12. The actor-network finds the policy πϕ(.|st), and the critic network estimates the state value function. The second step of this algorithm is to compute the advantage function using a current policy at Line 15. The third step is Fig. 1. System Model depicting multimedia streaming.

**Fragmento 18 - p. 3 - score 2:**

Specifically, an ABR algorithm selects the bitrate for each video chunk based on chunk processor input observations, including the number of chunks (ct), chunk size (nt), chunk bitrate (lt), size of the buffer (bt), throughput (xt), and download time (dt). Additionally, the ABR controller takes the network statistics such as bandwidth (bwt) and delay (det) into account. For the state-of-the-art vanilla-A3C, the ABR controller uses multi-agent training with multiple actor and critic neural networks. Each agent is trained in parallel with its own environment based on several state inputs st = (xt, dt, nt, bt, ct, lt, bwt, det). Moreover, each agent is trained and sends the local gradients to the central agent.

**Fragmento 19 - p. 4 - score 2:**

We compare the performance of all ABR algorithms using QoE [12] as a metric. The QoE is expressed as: QoE = N X n=1 q(bn) −µ N X n=1 Tn − N−1 X n=1 |q(bn+1) −q(bn)| (9) The QoE is composed of three elements: (i) the total bit rates of all video chunks, (ii) the penalty incurred by re-buffering, and (iii) the video’s smoothness, which is assessed by calcu- lating the difference in bit rates used to encode consecutive chunks. Various versions of the QoE metric are examined in this context as follows: (i) QoElin: q(bn) = bn with rebuffer penalty as µ = 4.3 and (ii) QoElog: q(bn) = log(b/bmin) with µ = 2.66. Note that we have utilized the above QoE metric formula- tion since it is commonly used in several other works including Robust-MPC [5], [6], [21], [22], [23] and [12].

**Fragmento 20 - p. 6 - score 2:**

Future studies will examine PPO-ABR for edge-driven video distribution services and evaluate it using various QoE metric versions. ACKNOWLEDGMENT This work has been supported by TCS foundation under the TCS research scholar program, 2019-2023, India. REFERENCES [1] “ISO/IEC 23009-1:2014: Dynamic adaptive streaming over HTTP(DASH) – Part 1: Media presentation description and segment formats,” May 2014. [2] Y. Sun, X. Yin, J. Jiang, V. Sekar, F. Lin, N. Wang, T. Liu, and B. Sinopoli, “Cs2p: Improving video bitrate selection and adaptation with data-driven throughput prediction,” Proceedings of the 2016 ACM SIGCOMM Conference, 2016. [3] T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Watson, “A buffer-based approach to rate adaptation: Evidence from a large video streaming service,” in Proceedings of the 2014 ACM Conference on SIGCOMM, ser.

**Fragmento 21 - p. 6 - score 2:**

[21] Z. Akhtar, Y. S. Nam, R. Govindan, S. Rao, J. Chen, E. Katz-Bassett, B. Ribeiro, J. Zhan, and H. Zhang, “Oboe: Auto-tuning video abr algorithms to network conditions,” in Proceedings of the 2018 Con- ference of the ACM Special Interest Group on Data Communication, ser. SIGCOMM ’18. New York, NY, USA: Association for Computing Machinery, 2018, p. 44–58. [22] S. Sengupta, N. Ganguly, S. Chakraborty, and P. De, “Hotdash: Hotspot aware adaptive video streaming using deep reinforcement learning,” 2018 IEEE 26th International Conference on Network Protocols (ICNP), pp. 165–175, 2018. [23] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, “Stick: A harmonious fusion of buffer-based and learning-based approach for adaptive streaming,” in IEEE INFOCOM 2020-IEEE Conference on Computer Communications.

**Fragmento 22 - p. 6 - score 2:**

SIGCOMM ’14. New York, NY, USA: Association for Computing Machinery, 2014, p. 187–198. [4] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “Bola: Near-optimal bi- trate adaptation for online videos,” in IEEE INFOCOM 2016 - The 35th Annual IEEE International Conference on Computer Communications, 2016, pp. 1–9. [5] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic approach for dynamic adaptive video streaming over http,” in Proceed- ings of the 2015 ACM Conference on Special Interest Group on Data Communication, ser. SIGCOMM ’15. New York, NY, USA: Association for Computing Machinery, 2015, p. 325–338. [6] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video stream- ing with pensieve,” in Proceedings of the Conference of the ACM Special Interest Group on Data Communication, ser.

**Fragmento 23 - p. 1 - score 1:**

One specific issue with A3C methods is the lag between each actor’s behavior policy and central learner’s target policy. Consequently, suboptimal updates emerge when the behavior and target policies become out of synchronization. In this paper, we address the problems faced by vanilla-A3C by integrating the on-policy- based multi-agent DRL method into the existing video streaming framework. Specifically, we propose a novel system for ABR gen- eration - Proximal Policy Optimization-based DRL for Adaptive Bit Rate streaming (PPO-ABR). Our proposed method improves the overall video QoE by maximizing sample efficiency using a clipped probability ratio between the new and the old policies on multiple epochs of minibatch updates.

**Fragmento 24 - p. 2 - score 1:**

Furthermore, as an improvement, vanilla-A3C [15] is proposed that uses several copies of the same agent with asynchronous updates. It is more efficient than the actor- critic methods because samples for data can be parallelized using several copies of the same agent resulting in an even smaller training time. In the vanilla-A3C algorithm, the current policy parameters (ϕnew) are updated based on previously collected experience with old policy parameters (ϕ) after every κ steps, i.e., after every κ state-action pairs. The equation below represents the value function update for vanilla-A3C is: maximizeϕ V π ϕnew(s) = κ∇V π ϕ (s) + κ P s ρπϕ(s) P a πϕnew(a|s)Aϕ(s, a) (5) where ρπ(s) presents distribution of state-action pairs, πϕ represents the old policy and πϕnew represents current policy.

**Fragmento 25 - p. 3 - score 1:**

Once the central agent has collected experience from the local agents, it updates its model parameters. Further, the central agent will make the decision to play the chunk with a specified bitrate to the chunk handler. The chunk handler sends the information about the chunk to the buffer and finally, the client will play the chunk n with quality q based on buffer occupancy. In addition to being less sample efficient, the vanilla-A3C also has a high divergence between the target policy of the central learner and every actor’s behavior policy. The subop- timal updates emerge when the behavior and target policies become out of synchronization. To address these issues, PPO- ABR uses a clipped probability ratio to constrain the KL- divergence between the new and the old policy parameters among several epochs instead of a single epoch as in vanilla- A3C.

**Fragmento 26 - p. 3 - score 1:**

to compute the policy divergence between the new and the old policies using an important sampling ratio (r(ϕ)) at Line 17. The fourth step is to update the actor parameters at Line 18 using PPO-clip where 1 + ϵ occurs when the advantage estimation is positive else 1 −ϵ is used from Lines 19 to 23. The PPO-clip imposes the penalty on the r(ϕ) ratio in both cases. The fourth step is to update the critic parameter (θnew) at Line 24. The output to the algorithm is the actor-network that makes the decision to play the chunk by chunk with a specified bitrate at Line 29, the critic network evaluates the state-value of the policy with PPO-clip for maximizing rewards at Line 30 and the actor and critic parameters are updated based on the actor and the critic loss functions at Line 31.


### 7.7. evaluacion baselines experimentos

Palabras clave usadas: `evaluation, experiment, experiments, baseline, baselines, compare, comparison, Pensieve, BBA, BOLA, MPC, RobustMPC, FastMPC, A3C, PPO, DQN, SODA, Oboe, MetaABR, results, outperform, ablation, scenario, test`

**Fragmento 1 - p. 5 - score 7:**

At a bit rate of 12 Mbps and a latency of 30 ms throughout the testing phase, we assessed how well each ABR algorithm performed. Figure 5 displays the average total reward obtained by various ABR algorithms with the QoElin metric for each trace when the network is simulated during testing with no packet loss. According to our findings, the PPO-ABR algorithms have a higher average QoE of 46.61 than other ABR algorithms. TABLE III ON THREE DATASETS, THE AVERAGE QOE WAS ATTAINED USING TWO DIFFERENT QOE METRICS DURING SIMULATION WITH NO PACKET LOSSES. ABR algorithm FCC and Norway traces OBOE traces Live traces QoElin QoElog QoElin QoElog QoElin QoElog PPO-ABR 46.61 44.93 45.09 46.25 46.91 45.68 SAC-ABR 42.77 43.68 39.72 45.41 42.59 43.90 Pensieve 39.63 35.26 37.96 37.01 39.12 41.68 BB 12.03 12.78 14.08 20 13.81 20.26 RB 35.62 36.45 36.22 37.31 37.45 37.35 BOLA 34.26 35.30 35.04 37.09 35.82 36.05 Robust-MPC 39.93 40.44 40.18 38.29 40.59 38.99 In Figure 6, we compare various ABR algorithms using the average playback bitrate, rebuffering penalty, and smoothness penalty for the QoElin metric under emulation with no packet losses during testing in order to understand and illustrate the better performance of the PPO-ABR.

**Fragmento 2 - p. 4 - score 6:**

Each OBOE trace stores the bandwidth measurements collected from wired, wireless, and cellular connections, and the throughput range is between 0 and 3 Mbps. B. Methodologies for Training, Comparative Algorithms, and Performance Metrics We train PPO-ABR on the aforementioned datasets for 100,000 iterations, and then we choose the model with the highest average reward. Table I summarizes the hyperpa- rameters utilized for PPO-ABR training. Specifically, clipped probability hyperparameter ϵ = 0.2 determines how much the new policy deviates from the old policy. These values have been selected based on the previous works [6], [21], and [20]. We use nact = 16 agents for all our experiments. Finally, the performance of the proposed PPO-ABR is compared to that of TABLE I HYPERPARAMETERS USED DURING THE TRAINING FOR PENSIEVE, SAC-ABR, AND PPO-ABR.

**Fragmento 3 - p. 5 - score 5:**

Figure 2 presents the average QoE value achieved by PPO- ABR, SAC-ABR, and Pensieve algorithms at each training epoch. We can observe that SAC-ABR performs poorly at the initial stages of training due to high exploration. Our results show different behavior for each of these algorithms when the number of epochs increases during the training. The PPO-ABR achieves a high QoE value right from the start of the training. Similar improvements are observed with OBOE in Figure 3 and Live traces in Figure 4 as well, where Table II presents the values of QoE obtained using different ABR algorithms. D. Testing results The training models are evaluated using the Mahimahi simulator [24]. We used 250 traces from the Norway test datasets and 205 traces from the FCC test datasets to test the models, as stated in [6].

**Fragmento 4 - p. 5 - score 5:**

It takes approximately eight hours to generate the training model for every algorithm with each dataset. Table II summarizes the QoE metrics obtained during training for the three datasets. The findings indicate that across all three datasets and for both QoElin and QoElog metrics, PPO-ABR consistently outperforms SAC-ABR and Pensieve, achieving higher QoE metrics. Fig. 5. Performance evaluation of ABR algorithms with QoElin metric when tested on the model trained with FCC and Norway traces while the network is emulated with no packet loss. Fig. 6. Comparing PPO-ABR with current ABR methods by analyzing their performance on the individual elements for QoElin metric with no packet loss under emulation (Equation 9).

**Fragmento 5 - p. 1 - score 4:**

DRL is a branch of deep learning that deals with how agents should behave depending on the state of the environment. In DRL, a policy is created to maximize the expected cumulative reward. The policy is the mapping function from states of the environment to actions. Pensieve [6], being one of the first DRL-based methods for ABR generation, is built upon the basic vanilla-A3C algorithm, whereas ALISA [13], being the latest DRL-based ABR method, utilizes soft updates with an A3C algorithm. Both Pensieve and ALISA update the ABR control policy based on the current network conditions and past decisions, and it is able to identify policies that outperform traditional ABR algorithms. However, these state-of-the-art DRL-based methods suffer from two key drawbacks: (i) there is a lag between each actor’s behavior policy and the central learner’s target policy.

**Fragmento 6 - p. 1 - score 4:**

Consequently, suboptimal updates emerge when the behavior and target policies become out of synchronization, and (ii) there is a constraint on the divergence between the new and the old policies. Due to these constraints, these algorithms may result in imprecise throughput prediction when there are fluctuations in the network, re-buffering at the client’s device, and inaccurate bitrate selection impacting the overall QoE for the end users. To resolve the above issues, we propose the integration of Proximal Policy Optimization-based DRL for ABR (PPO-ABR) to use a clipped probability ratio for constraining the divergence between the new and the old policy parameters. Our experimental results show that PPO-ABR improves overall video QoE as compared to other state-of- the-art methods.

**Fragmento 7 - p. 1 - score 4:**

The experiments on real network traces demonstrate that PPO-ABR outperforms state- of-the-art methods for different QoE variants. Index Terms—Reinforcement learning, video streaming, policy optimization, adaptive bit rate. I. INTRODUCTION Due to the widespread use of the Internet, the volume of multimedia traffic has increased, including video streaming. The Cisco annual Internet Report projects that by 2023, 69% of the world’s population will have access to the Internet, with Internet video traffic significantly outnumbering other Internet traffic. In order to ensure seamless video streaming, Dynamic Adaptive Streaming over HTTP (DASH) [1] uses an adaptive bit rate (ABR) algorithm to send the video encoded at a specific bitrate based on the network conditions.

**Fragmento 8 - p. 1 - score 4:**

Several ABR algorithms such as RB [2], BB [3], BOLA [4], and Robust- MPC [5] use network conditions including throughput estima- tion, playback buffer occupancy or a combination of both for bitrate estimation with the aim to enhance the QoE for end users. However, traditional ABR algorithms are designed with specific network conditions and traffic pattern assumptions. As a result, they may not perform optimally in networks where network conditions and traffic patterns are subject to rapid and unpredictable change. Recently, several data-driven deep reinforcement learning (DRL) approaches, including Pensieve [6], A2BR [7], VSiM [8], NANCY [9], AL-FFEA3C [10], AL-AvgA3C [10], MARL-A3C [11], SAC-ABR [12] and ALISA [13] are proposed to improve the ABR algorithms.

**Fragmento 9 - p. 3 - score 4:**

The PPO-ABR trains multiple agents in parallel, so the multi-agents are trained with their environments for each batch iteration. Moreover, the actor and critic parameters are updated using PPO-clip for each batch iteration. The value function parameters are updated after multiple epochs instead of a single epoch. Further, the central agent collects the mini-batch samples and updates the gradient to the next batch iterations. Overall, PPO-ABR results in a stable update and provides the bit rate to encode the next chunk. IV. EXPERIMENTAL DETAILS AND RESULTS This section will describe the experimental methodology utilised for this study. This will include a description of the datasets used, the training method employed, the algorithms used for comparison, and the performance metrics used to assess their efficacy.

**Fragmento 10 - p. 4 - score 4:**

Hyperparameter Description Value Actor-critic algorithms γ Discount factor 0.99 Pensieve, SAC-ABR, PPO-ABR αp Actor network’s learning rate 0.0001 Pensieve, SAC-ABR, PPO-ABR αc Critic network’s learning rate 0.001 Pensieve, SAC-ABR, PPO-ABR η Entropy regularization factor range 6 to 0.01 Pensieve, SAC-ABR, PPO-ABR τ Interpolation factor 0.995 SAC-ABR ϵ clipping parameter 0.2 PPO-ABR R Random seed 42 PPO-ABR nact Total number of agents 16 Pensieve, SAC-ABR, PPO-ABR Fig. 2. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on FCC and Norway traces, and the average values were obtained. the following state-of-the-art DRL-based and non-DRL-based ABR algorithms: SAC-ABR [12], Pensieve [6], BB [3], RB [2], BOLA [4], and Robust-MPC [5].

**Fragmento 11 - p. 4 - score 4:**

There also exist other QoE metric formulations, for example in [7] and [8], that can also be used for the performance evaluation. In this work, we focus only on the QoE metric defined in Equation 9. TABLE II TRAINING OUTCOMES OF PENSIEVE, SAC-ABR, AND PPO-ABR CONCERNING THE QoElin AND QoElog METRICS ACROSS MULTIPLE DATASETS. RL algorithm FCC Norway Traces OBOE Traces Live traces QoElin QoElog QoElin QoElog QoElin QoElog PPO-ABR 45.48 45.40 45.79 46.36 44.84 45.89 SAC-ABR 42.60 45.20 41.33 43.88 41.70 43.46 Pensieve 37.45 37.84 37.05 36.30 37.20 37.59 202 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 12 - p. 5 - score 4:**

Fig. 3. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on OBOE traces, and the average values were obtained. Fig. 4. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on Live traces, and the average values were obtained. C. Training results We trained PPO-ABR, SAC-ABR, and Pensieve using the three datasets mentioned in the preceding section. Further- more, in order to maximize entropy, we utilized an entropy regularization ranging from 6 to 0.01 for a better exploration- exploitation tradeoff, i.e., initially, an entropy value of six is used for a few iterations, and then it is gradually decreased to 0.01.

**Fragmento 13 - p. 6 - score 4:**

penalties. Similarly, BB likewise has a significant smoothness penalty. The PPO-ABR delivers a higher average bit rate and, in comparison, lower smoothness and rebuffering penalties. The PPO-ABR achieves an average QoE higher than the other ABR algorithms due to the combined effects of these individual components. The average QoE values attained by the ABR algorithms when evaluated on the network emulated with no packet losses are then shown in Table III for various QoE metrics. V. CONCLUSION We have shown in this study the advantages of adopt- ing on-policy DRL-based PPO-ABR to increase QoE for video streaming. Our suggested method specifically overcomes the limitations currently faced by state-of-the-art DRL-based methods and consistently achieves higher average QoE than SAC-ABR and Pensieve, respectively, by up to 13.52% and 27.42%, and even higher QoE when compared to other con- ventional fixed-rule-based ABR algorithms.

**Fragmento 14 - p. 1 - score 3:**

The rest of the paper is organized as follows: Section II presents the relevant background on reinforcement learning and on-policy RL methods. Section III presents the design of the proposed PPO-ABR algorithm. We present the experi- mental setup and results in Section IV where we include both training and testing results. Finally, we conclude our work in Section V. II. BACKGROUND RL [14] is a learning process that is adaptive to dynamic environments, even in cases where there is little or no prior 979-8-3503-3339-8/23/$31.00 ©2023 IEEE 199 2023 International Wireless Communications and Mobile Computing (IWCMC) | 979-8-3503-3339-8/23/$31.00 ©2023 IEEE | DOI: 10.1109/IWCMC58020.2023.10182379 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 15 - p. 3 - score 3:**

A. Datasets We utilised multiple datasets FCC [18], Norway [19], LIVE [20], OBOE [21] for our experimentation, including both broadband and mobile datasets. First, we utilised the FCC [18] and Norway datasets [19], which include fixed broad- band technologies and Telenor’s 3G/HSDPA mobile wireless network. We utilized 59 and 68 traces from FCC and Norway throughput traces, respectively for our experiments. The range of throughput for both datasets is 0 to 6 Mbps. Secondly, we used live video streaming datasets [20], which consists of data from wireless networks such as WiFi and 4G. The throughput range of these traces is between 0.2 Mbps and 4 Mbps, and 100 traces are utilised in our experiments. Lastly, we utilised OBOE dataset [21], which include 428 traces from 201 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 16 - p. 1 - score 2:**

PPO-ABR: Proximal Policy Optimization based Deep Reinforcement Learning for Adaptive BitRate streaming Mandan Naresh, Paresh Saxena and Manik Gupta Dept. of CSIS, BITS Pilani Hyderabad, India {p20180420, psaxena, manik}@hyderabad.bits-pilani.ac.in Abstract—Providing a high Quality of Experience (QoE) for video streaming in 5G and beyond 5G (B5G) networks is challenging due to the dynamic nature of the underlying network conditions. Several Adaptive Bit Rate (ABR) algorithms have been developed to improve QoE, but most of them are designed based on fixed rules and unsuitable for a wide range of net- work conditions. Recently, Deep Reinforcement Learning (DRL) based Asynchronous Advantage Actor-Critic (A3C) methods have recently demonstrated promise in their ability to generalise to diverse network conditions, but they still have limitations.

**Fragmento 17 - p. 1 - score 2:**

One specific issue with A3C methods is the lag between each actor’s behavior policy and central learner’s target policy. Consequently, suboptimal updates emerge when the behavior and target policies become out of synchronization. In this paper, we address the problems faced by vanilla-A3C by integrating the on-policy- based multi-agent DRL method into the existing video streaming framework. Specifically, we propose a novel system for ABR gen- eration - Proximal Policy Optimization-based DRL for Adaptive Bit Rate streaming (PPO-ABR). Our proposed method improves the overall video QoE by maximizing sample efficiency using a clipped probability ratio between the new and the old policies on multiple epochs of minibatch updates.

**Fragmento 18 - p. 3 - score 2:**

Once the central agent has collected experience from the local agents, it updates its model parameters. Further, the central agent will make the decision to play the chunk with a specified bitrate to the chunk handler. The chunk handler sends the information about the chunk to the buffer and finally, the client will play the chunk n with quality q based on buffer occupancy. In addition to being less sample efficient, the vanilla-A3C also has a high divergence between the target policy of the central learner and every actor’s behavior policy. The subop- timal updates emerge when the behavior and target policies become out of synchronization. To address these issues, PPO- ABR uses a clipped probability ratio to constrain the KL- divergence between the new and the old policy parameters among several epochs instead of a single epoch as in vanilla- A3C.

**Fragmento 19 - p. 4 - score 2:**

We compare the performance of all ABR algorithms using QoE [12] as a metric. The QoE is expressed as: QoE = N X n=1 q(bn) −µ N X n=1 Tn − N−1 X n=1 |q(bn+1) −q(bn)| (9) The QoE is composed of three elements: (i) the total bit rates of all video chunks, (ii) the penalty incurred by re-buffering, and (iii) the video’s smoothness, which is assessed by calcu- lating the difference in bit rates used to encode consecutive chunks. Various versions of the QoE metric are examined in this context as follows: (i) QoElin: q(bn) = bn with rebuffer penalty as µ = 4.3 and (ii) QoElog: q(bn) = log(b/bmin) with µ = 2.66. Note that we have utilized the above QoE metric formula- tion since it is commonly used in several other works including Robust-MPC [5], [6], [21], [22], [23] and [12].

**Fragmento 20 - p. 6 - score 2:**

SIGCOMM ’14. New York, NY, USA: Association for Computing Machinery, 2014, p. 187–198. [4] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “Bola: Near-optimal bi- trate adaptation for online videos,” in IEEE INFOCOM 2016 - The 35th Annual IEEE International Conference on Computer Communications, 2016, pp. 1–9. [5] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic approach for dynamic adaptive video streaming over http,” in Proceed- ings of the 2015 ACM Conference on Special Interest Group on Data Communication, ser. SIGCOMM ’15. New York, NY, USA: Association for Computing Machinery, 2015, p. 325–338. [6] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video stream- ing with pensieve,” in Proceedings of the Conference of the ACM Special Interest Group on Data Communication, ser.

**Fragmento 21 - p. 2 - score 1:**

We can rewrite equation (6) to maximize only the second part, also known as the surrogate advantage objective, as follows: maximizeϕ κEs∼ρπϕ,a∼πϕ " r(ϕ) Aϕ(s, a) # subject to DKL(πϕnew||πϕ) ≤λ (7) Although TRPO provides constraints on the divergence between the new and the old policies, it can still lead to instability in policy updates. To address this issue, the on- policy PPO algorithm [17] is proposed that uses a clipped probability ratio to constrain the divergence between the old and the new policy parameters. The objective function in PPO is derived from Equation (7), and the maximization problem is given as: maximizeϕLclip(ϕnew) = κEt " min LCP I(ϕ), clip(r(ϕ) , 1 −ϵ, 1 + ϵ)Aϕ(s, a) !# subject to DKL(πϕnew||πϕ) ≤λ (8) where ϵ is the hyperparameter for clipping and LCP I(ϕ) = κEt " r(ϕ) Aϕ(s, a) # where CPI refers to a conservative policy iteration.

**Fragmento 22 - p. 2 - score 1:**

Furthermore, as an improvement, vanilla-A3C [15] is proposed that uses several copies of the same agent with asynchronous updates. It is more efficient than the actor- critic methods because samples for data can be parallelized using several copies of the same agent resulting in an even smaller training time. In the vanilla-A3C algorithm, the current policy parameters (ϕnew) are updated based on previously collected experience with old policy parameters (ϕ) after every κ steps, i.e., after every κ state-action pairs. The equation below represents the value function update for vanilla-A3C is: maximizeϕ V π ϕnew(s) = κ∇V π ϕ (s) + κ P s ρπϕ(s) P a πϕnew(a|s)Aϕ(s, a) (5) where ρπ(s) presents distribution of state-action pairs, πϕ represents the old policy and πϕnew represents current policy.

**Fragmento 23 - p. 3 - score 1:**

represents a modification of the TRPO surrogate objective using a clipped probability ratio ϵ, which ensures that the r(ϕ) remains within the range [1−ϵ, 1+ϵ]. The PPO maximization considers the minimum of the clipped and unclipped objectives resulting in a smaller divergence between the new and the old policy parameters. III. PROPOSED ON-POLICY ABR METHOD: PPO-ABR In this paper, we focus on the HTTP-based video distri- bution system, as shown in Figure 1 that utilize the DASH framework for multimedia streaming. In such systems, the videos are stored on the server in separate chunks, where each chunk is encoded with a specific bitrate. The client then requests each chunk with the appropriate bitrate from the server using an ABR algorithm, where the ABR algorithm generates the bit rate based on factors such as the available network conditions and the capabilities of the client device.

**Fragmento 24 - p. 3 - score 1:**

to compute the policy divergence between the new and the old policies using an important sampling ratio (r(ϕ)) at Line 17. The fourth step is to update the actor parameters at Line 18 using PPO-clip where 1 + ϵ occurs when the advantage estimation is positive else 1 −ϵ is used from Lines 19 to 23. The PPO-clip imposes the penalty on the r(ϕ) ratio in both cases. The fourth step is to update the critic parameter (θnew) at Line 24. The output to the algorithm is the actor-network that makes the decision to play the chunk by chunk with a specified bitrate at Line 29, the critic network evaluates the state-value of the policy with PPO-clip for maximizing rewards at Line 30 and the actor and critic parameters are updated based on the actor and the critic loss functions at Line 31.

**Fragmento 25 - p. 3 - score 1:**

Algorithm 1 presents the PPO-ABR algorithm and outlines the critical steps. The input to the algorithm is video samples, including hyperparameter setting for actor and critic networks and state input as st = (xt, dt, nt, bt, ct, lt, bwt, det). The first step is dividing a video file into chunks. Each chunk is played at a specified bitrate using the selection of the action based on the current state and the policy and to store the corresponding reward at Line 12. The actor-network finds the policy πϕ(.|st), and the critic network estimates the state value function. The second step of this algorithm is to compute the advantage function using a current policy at Line 15. The third step is Fig. 1. System Model depicting multimedia streaming.

**Fragmento 26 - p. 3 - score 1:**

Specifically, an ABR algorithm selects the bitrate for each video chunk based on chunk processor input observations, including the number of chunks (ct), chunk size (nt), chunk bitrate (lt), size of the buffer (bt), throughput (xt), and download time (dt). Additionally, the ABR controller takes the network statistics such as bandwidth (bwt) and delay (det) into account. For the state-of-the-art vanilla-A3C, the ABR controller uses multi-agent training with multiple actor and critic neural networks. Each agent is trained in parallel with its own environment based on several state inputs st = (xt, dt, nt, bt, ct, lt, bwt, det). Moreover, each agent is trained and sends the local gradients to the central agent.


### 7.8. resultados numericos metricas

Palabras clave usadas: `improvement, improve, gain, reduce, reduction, %, QoE gain, higher, lower, average, median, percentile, stall time, latency, overhead, accuracy, significant, p95, p99, score, ratio, duration`

**Fragmento 1 - p. 6 - score 5:**

penalties. Similarly, BB likewise has a significant smoothness penalty. The PPO-ABR delivers a higher average bit rate and, in comparison, lower smoothness and rebuffering penalties. The PPO-ABR achieves an average QoE higher than the other ABR algorithms due to the combined effects of these individual components. The average QoE values attained by the ABR algorithms when evaluated on the network emulated with no packet losses are then shown in Table III for various QoE metrics. V. CONCLUSION We have shown in this study the advantages of adopt- ing on-policy DRL-based PPO-ABR to increase QoE for video streaming. Our suggested method specifically overcomes the limitations currently faced by state-of-the-art DRL-based methods and consistently achieves higher average QoE than SAC-ABR and Pensieve, respectively, by up to 13.52% and 27.42%, and even higher QoE when compared to other con- ventional fixed-rule-based ABR algorithms.

**Fragmento 2 - p. 5 - score 4:**

Figure 2 presents the average QoE value achieved by PPO- ABR, SAC-ABR, and Pensieve algorithms at each training epoch. We can observe that SAC-ABR performs poorly at the initial stages of training due to high exploration. Our results show different behavior for each of these algorithms when the number of epochs increases during the training. The PPO-ABR achieves a high QoE value right from the start of the training. Similar improvements are observed with OBOE in Figure 3 and Live traces in Figure 4 as well, where Table II presents the values of QoE obtained using different ABR algorithms. D. Testing results The training models are evaluated using the Mahimahi simulator [24]. We used 250 traces from the Norway test datasets and 205 traces from the FCC test datasets to test the models, as stated in [6].

**Fragmento 3 - p. 5 - score 3:**

At a bit rate of 12 Mbps and a latency of 30 ms throughout the testing phase, we assessed how well each ABR algorithm performed. Figure 5 displays the average total reward obtained by various ABR algorithms with the QoElin metric for each trace when the network is simulated during testing with no packet loss. According to our findings, the PPO-ABR algorithms have a higher average QoE of 46.61 than other ABR algorithms. TABLE III ON THREE DATASETS, THE AVERAGE QOE WAS ATTAINED USING TWO DIFFERENT QOE METRICS DURING SIMULATION WITH NO PACKET LOSSES. ABR algorithm FCC and Norway traces OBOE traces Live traces QoElin QoElog QoElin QoElog QoElin QoElog PPO-ABR 46.61 44.93 45.09 46.25 46.91 45.68 SAC-ABR 42.77 43.68 39.72 45.41 42.59 43.90 Pensieve 39.63 35.26 37.96 37.01 39.12 41.68 BB 12.03 12.78 14.08 20 13.81 20.26 RB 35.62 36.45 36.22 37.31 37.45 37.35 BOLA 34.26 35.30 35.04 37.09 35.82 36.05 Robust-MPC 39.93 40.44 40.18 38.29 40.59 38.99 In Figure 6, we compare various ABR algorithms using the average playback bitrate, rebuffering penalty, and smoothness penalty for the QoElin metric under emulation with no packet losses during testing in order to understand and illustrate the better performance of the PPO-ABR.

**Fragmento 4 - p. 1 - score 2:**

Consequently, suboptimal updates emerge when the behavior and target policies become out of synchronization, and (ii) there is a constraint on the divergence between the new and the old policies. Due to these constraints, these algorithms may result in imprecise throughput prediction when there are fluctuations in the network, re-buffering at the client’s device, and inaccurate bitrate selection impacting the overall QoE for the end users. To resolve the above issues, we propose the integration of Proximal Policy Optimization-based DRL for ABR (PPO-ABR) to use a clipped probability ratio for constraining the divergence between the new and the old policy parameters. Our experimental results show that PPO-ABR improves overall video QoE as compared to other state-of- the-art methods.

**Fragmento 5 - p. 1 - score 2:**

The experiments on real network traces demonstrate that PPO-ABR outperforms state- of-the-art methods for different QoE variants. Index Terms—Reinforcement learning, video streaming, policy optimization, adaptive bit rate. I. INTRODUCTION Due to the widespread use of the Internet, the volume of multimedia traffic has increased, including video streaming. The Cisco annual Internet Report projects that by 2023, 69% of the world’s population will have access to the Internet, with Internet video traffic significantly outnumbering other Internet traffic. In order to ensure seamless video streaming, Dynamic Adaptive Streaming over HTTP (DASH) [1] uses an adaptive bit rate (ABR) algorithm to send the video encoded at a specific bitrate based on the network conditions.

**Fragmento 6 - p. 1 - score 2:**

One specific issue with A3C methods is the lag between each actor’s behavior policy and central learner’s target policy. Consequently, suboptimal updates emerge when the behavior and target policies become out of synchronization. In this paper, we address the problems faced by vanilla-A3C by integrating the on-policy- based multi-agent DRL method into the existing video streaming framework. Specifically, we propose a novel system for ABR gen- eration - Proximal Policy Optimization-based DRL for Adaptive Bit Rate streaming (PPO-ABR). Our proposed method improves the overall video QoE by maximizing sample efficiency using a clipped probability ratio between the new and the old policies on multiple epochs of minibatch updates.

**Fragmento 7 - p. 2 - score 2:**

Furthermore, as an improvement, vanilla-A3C [15] is proposed that uses several copies of the same agent with asynchronous updates. It is more efficient than the actor- critic methods because samples for data can be parallelized using several copies of the same agent resulting in an even smaller training time. In the vanilla-A3C algorithm, the current policy parameters (ϕnew) are updated based on previously collected experience with old policy parameters (ϕ) after every κ steps, i.e., after every κ state-action pairs. The equation below represents the value function update for vanilla-A3C is: maximizeϕ V π ϕnew(s) = κ∇V π ϕ (s) + κ P s ρπϕ(s) P a πϕnew(a|s)Aϕ(s, a) (5) where ρπ(s) presents distribution of state-action pairs, πϕ represents the old policy and πϕnew represents current policy.

**Fragmento 8 - p. 4 - score 2:**

Each OBOE trace stores the bandwidth measurements collected from wired, wireless, and cellular connections, and the throughput range is between 0 and 3 Mbps. B. Methodologies for Training, Comparative Algorithms, and Performance Metrics We train PPO-ABR on the aforementioned datasets for 100,000 iterations, and then we choose the model with the highest average reward. Table I summarizes the hyperpa- rameters utilized for PPO-ABR training. Specifically, clipped probability hyperparameter ϵ = 0.2 determines how much the new policy deviates from the old policy. These values have been selected based on the previous works [6], [21], and [20]. We use nact = 16 agents for all our experiments. Finally, the performance of the proposed PPO-ABR is compared to that of TABLE I HYPERPARAMETERS USED DURING THE TRAINING FOR PENSIEVE, SAC-ABR, AND PPO-ABR.

**Fragmento 9 - p. 5 - score 2:**

Fig. 3. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on OBOE traces, and the average values were obtained. Fig. 4. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on Live traces, and the average values were obtained. C. Training results We trained PPO-ABR, SAC-ABR, and Pensieve using the three datasets mentioned in the preceding section. Further- more, in order to maximize entropy, we utilized an entropy regularization ranging from 6 to 0.01 for a better exploration- exploitation tradeoff, i.e., initially, an entropy value of six is used for a few iterations, and then it is gradually decreased to 0.01.

**Fragmento 10 - p. 1 - score 1:**

DRL is a branch of deep learning that deals with how agents should behave depending on the state of the environment. In DRL, a policy is created to maximize the expected cumulative reward. The policy is the mapping function from states of the environment to actions. Pensieve [6], being one of the first DRL-based methods for ABR generation, is built upon the basic vanilla-A3C algorithm, whereas ALISA [13], being the latest DRL-based ABR method, utilizes soft updates with an A3C algorithm. Both Pensieve and ALISA update the ABR control policy based on the current network conditions and past decisions, and it is able to identify policies that outperform traditional ABR algorithms. However, these state-of-the-art DRL-based methods suffer from two key drawbacks: (i) there is a lag between each actor’s behavior policy and the central learner’s target policy.

**Fragmento 11 - p. 1 - score 1:**

PPO-ABR: Proximal Policy Optimization based Deep Reinforcement Learning for Adaptive BitRate streaming Mandan Naresh, Paresh Saxena and Manik Gupta Dept. of CSIS, BITS Pilani Hyderabad, India {p20180420, psaxena, manik}@hyderabad.bits-pilani.ac.in Abstract—Providing a high Quality of Experience (QoE) for video streaming in 5G and beyond 5G (B5G) networks is challenging due to the dynamic nature of the underlying network conditions. Several Adaptive Bit Rate (ABR) algorithms have been developed to improve QoE, but most of them are designed based on fixed rules and unsuitable for a wide range of net- work conditions. Recently, Deep Reinforcement Learning (DRL) based Asynchronous Advantage Actor-Critic (A3C) methods have recently demonstrated promise in their ability to generalise to diverse network conditions, but they still have limitations.

**Fragmento 12 - p. 1 - score 1:**

Several ABR algorithms such as RB [2], BB [3], BOLA [4], and Robust- MPC [5] use network conditions including throughput estima- tion, playback buffer occupancy or a combination of both for bitrate estimation with the aim to enhance the QoE for end users. However, traditional ABR algorithms are designed with specific network conditions and traffic pattern assumptions. As a result, they may not perform optimally in networks where network conditions and traffic patterns are subject to rapid and unpredictable change. Recently, several data-driven deep reinforcement learning (DRL) approaches, including Pensieve [6], A2BR [7], VSiM [8], NANCY [9], AL-FFEA3C [10], AL-AvgA3C [10], MARL-A3C [11], SAC-ABR [12] and ALISA [13] are proposed to improve the ABR algorithms.

**Fragmento 13 - p. 2 - score 1:**

We can rewrite equation (6) to maximize only the second part, also known as the surrogate advantage objective, as follows: maximizeϕ κEs∼ρπϕ,a∼πϕ " r(ϕ) Aϕ(s, a) # subject to DKL(πϕnew||πϕ) ≤λ (7) Although TRPO provides constraints on the divergence between the new and the old policies, it can still lead to instability in policy updates. To address this issue, the on- policy PPO algorithm [17] is proposed that uses a clipped probability ratio to constrain the divergence between the old and the new policy parameters. The objective function in PPO is derived from Equation (7), and the maximization problem is given as: maximizeϕLclip(ϕnew) = κEt " min LCP I(ϕ), clip(r(ϕ) , 1 −ϵ, 1 + ϵ)Aϕ(s, a) !# subject to DKL(πϕnew||πϕ) ≤λ (8) where ϵ is the hyperparameter for clipping and LCP I(ϕ) = κEt " r(ϕ) Aϕ(s, a) # where CPI refers to a conservative policy iteration.

**Fragmento 14 - p. 2 - score 1:**

These methods have two components: an actor represented by a policy π and a critic represented by an estimate of the action-value function. Neural network function approximators are typically used to represent both of them. With parameters θ, the critic estimates the current policy’s value function. The main goal of this method is to reduce the variance using single-step state-value estimates. The single-step state-value estimates are derived using a temporal difference (δ), and it is given by: δ = V π ϕ (st) + γV π ϕ (st+1, ϕ) −V π ϕ (st, ϕ) (2) The gradient operator ∇is used to define the policy and critic updates with regard to its parameters ϕ and θ, respec- tively: ∆ϕ = ϕ + αpδ∇πϕ(st+1, at+1, ϕ) (3) ∆θ = θ + αcδ∇V π ϕ (st, θ) (4) where αp and αc are the actor and critic learning rates, respectively.

**Fragmento 15 - p. 3 - score 1:**

represents a modification of the TRPO surrogate objective using a clipped probability ratio ϵ, which ensures that the r(ϕ) remains within the range [1−ϵ, 1+ϵ]. The PPO maximization considers the minimum of the clipped and unclipped objectives resulting in a smaller divergence between the new and the old policy parameters. III. PROPOSED ON-POLICY ABR METHOD: PPO-ABR In this paper, we focus on the HTTP-based video distri- bution system, as shown in Figure 1 that utilize the DASH framework for multimedia streaming. In such systems, the videos are stored on the server in separate chunks, where each chunk is encoded with a specific bitrate. The client then requests each chunk with the appropriate bitrate from the server using an ABR algorithm, where the ABR algorithm generates the bit rate based on factors such as the available network conditions and the capabilities of the client device.

**Fragmento 16 - p. 3 - score 1:**

Once the central agent has collected experience from the local agents, it updates its model parameters. Further, the central agent will make the decision to play the chunk with a specified bitrate to the chunk handler. The chunk handler sends the information about the chunk to the buffer and finally, the client will play the chunk n with quality q based on buffer occupancy. In addition to being less sample efficient, the vanilla-A3C also has a high divergence between the target policy of the central learner and every actor’s behavior policy. The subop- timal updates emerge when the behavior and target policies become out of synchronization. To address these issues, PPO- ABR uses a clipped probability ratio to constrain the KL- divergence between the new and the old policy parameters among several epochs instead of a single epoch as in vanilla- A3C.

**Fragmento 17 - p. 3 - score 1:**

The PPO-ABR trains multiple agents in parallel, so the multi-agents are trained with their environments for each batch iteration. Moreover, the actor and critic parameters are updated using PPO-clip for each batch iteration. The value function parameters are updated after multiple epochs instead of a single epoch. Further, the central agent collects the mini-batch samples and updates the gradient to the next batch iterations. Overall, PPO-ABR results in a stable update and provides the bit rate to encode the next chunk. IV. EXPERIMENTAL DETAILS AND RESULTS This section will describe the experimental methodology utilised for this study. This will include a description of the datasets used, the training method employed, the algorithms used for comparison, and the performance metrics used to assess their efficacy.

**Fragmento 18 - p. 3 - score 1:**

to compute the policy divergence between the new and the old policies using an important sampling ratio (r(ϕ)) at Line 17. The fourth step is to update the actor parameters at Line 18 using PPO-clip where 1 + ϵ occurs when the advantage estimation is positive else 1 −ϵ is used from Lines 19 to 23. The PPO-clip imposes the penalty on the r(ϕ) ratio in both cases. The fourth step is to update the critic parameter (θnew) at Line 24. The output to the algorithm is the actor-network that makes the decision to play the chunk by chunk with a specified bitrate at Line 29, the critic network evaluates the state-value of the policy with PPO-clip for maximizing rewards at Line 30 and the actor and critic parameters are updated based on the actor and the critic loss functions at Line 31.

**Fragmento 19 - p. 4 - score 1:**

Algorithm 1 PPO-ABR Algorithm 1: Input: video samples, hyperparameters; 2: Parameters: 3: Video vi; choose a video file as a input 4: Chunk c; select the bitrate for future chunks from video file 5: Initialize the batch size B, clipping parameter ϵ 6: Initialize weight parameters: θ, ϕ 7: for video vi= 1,2,3...., VI do 8: Observe initial state st; 9: for chunk c=1,2,3...., C do 10: V θ = PK k=1 V (st; θk) for all states st 11: R ←0 for terminal state sterminal 12: R = V t for non terminal states st 13: for each batch iteration do 14: Compute advantage function on B 15: Aϕ(s, a) = Qπ ϕ(s, a) −V π ϕ (s) 16: Compute the importance sampling weight 17: r(ϕ) = πϕnew (s,a) πϕ(s,a) using policy parameters 18: Update actor parameter by PPO- clip: maximizeϕLclip(ϕnew) = κEt " min LCP I(ϕ), clip(r(ϕ) , 1 −ϵ, 1 + ϵ)Aϕ(s, a) !# 19: if Aϕ(s, a) ≥0 then 20: clip(r(ϕ), 1 + ϵ)Aϕ(s, a) 21: else 22: clip(r(ϕ), 1 −ϵ)Aϕ(s, a) 23: end if 24: Update critic parameter θnew = θ + ∂(R−V θ)2 ∂θ 25: end for 26: end for 27: end for 28: Output: 29: Actor network makes the decision to play the chunk by chunk with a specified bitrate 30: Critic network evaluates the state-value of the policy with PPO-clip for maximizing rewards 31: Update actor and critic parameters θ, ϕ 500 video streaming sessions.

**Fragmento 20 - p. 4 - score 1:**

Hyperparameter Description Value Actor-critic algorithms γ Discount factor 0.99 Pensieve, SAC-ABR, PPO-ABR αp Actor network’s learning rate 0.0001 Pensieve, SAC-ABR, PPO-ABR αc Critic network’s learning rate 0.001 Pensieve, SAC-ABR, PPO-ABR η Entropy regularization factor range 6 to 0.01 Pensieve, SAC-ABR, PPO-ABR τ Interpolation factor 0.995 SAC-ABR ϵ clipping parameter 0.2 PPO-ABR R Random seed 42 PPO-ABR nact Total number of agents 16 Pensieve, SAC-ABR, PPO-ABR Fig. 2. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on FCC and Norway traces, and the average values were obtained. the following state-of-the-art DRL-based and non-DRL-based ABR algorithms: SAC-ABR [12], Pensieve [6], BB [3], RB [2], BOLA [4], and Robust-MPC [5].

**Fragmento 21 - p. 5 - score 1:**

It takes approximately eight hours to generate the training model for every algorithm with each dataset. Table II summarizes the QoE metrics obtained during training for the three datasets. The findings indicate that across all three datasets and for both QoElin and QoElog metrics, PPO-ABR consistently outperforms SAC-ABR and Pensieve, achieving higher QoE metrics. Fig. 5. Performance evaluation of ABR algorithms with QoElin metric when tested on the model trained with FCC and Norway traces while the network is emulated with no packet loss. Fig. 6. Comparing PPO-ABR with current ABR methods by analyzing their performance on the individual elements for QoElin metric with no packet loss under emulation (Equation 9).

**Fragmento 22 - p. 5 - score 1:**

Our findings indicate that, with the exception of BOLA and RB, most ABR al- gorithms attain greater bitrates. Several of these algorithms experience rebuffering penalties due to the higher bitrate choice, with BB and SAC-ABR having the biggest rebuffering 203 Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore. Restrictions apply.


### 7.9. limitaciones riesgos coste

Palabras clave usadas: `limitation, limitations, future work, challenge, challenges, overhead, complexity, compute, GPU, CPU, deployment, real-world, generalization, out-of-distribution, OOD, unstable, fail, bias, sensitive, prediction error, horizon, scalability`

**Fragmento 1 - p. 1 - score 2:**

PPO-ABR: Proximal Policy Optimization based Deep Reinforcement Learning for Adaptive BitRate streaming Mandan Naresh, Paresh Saxena and Manik Gupta Dept. of CSIS, BITS Pilani Hyderabad, India {p20180420, psaxena, manik}@hyderabad.bits-pilani.ac.in Abstract—Providing a high Quality of Experience (QoE) for video streaming in 5G and beyond 5G (B5G) networks is challenging due to the dynamic nature of the underlying network conditions. Several Adaptive Bit Rate (ABR) algorithms have been developed to improve QoE, but most of them are designed based on fixed rules and unsuitable for a wide range of net- work conditions. Recently, Deep Reinforcement Learning (DRL) based Asynchronous Advantage Actor-Critic (A3C) methods have recently demonstrated promise in their ability to generalise to diverse network conditions, but they still have limitations.

**Fragmento 2 - p. 6 - score 2:**

penalties. Similarly, BB likewise has a significant smoothness penalty. The PPO-ABR delivers a higher average bit rate and, in comparison, lower smoothness and rebuffering penalties. The PPO-ABR achieves an average QoE higher than the other ABR algorithms due to the combined effects of these individual components. The average QoE values attained by the ABR algorithms when evaluated on the network emulated with no packet losses are then shown in Table III for various QoE metrics. V. CONCLUSION We have shown in this study the advantages of adopt- ing on-policy DRL-based PPO-ABR to increase QoE for video streaming. Our suggested method specifically overcomes the limitations currently faced by state-of-the-art DRL-based methods and consistently achieves higher average QoE than SAC-ABR and Pensieve, respectively, by up to 13.52% and 27.42%, and even higher QoE when compared to other con- ventional fixed-rule-based ABR algorithms.

**Fragmento 3 - p. 3 - score 1:**

to compute the policy divergence between the new and the old policies using an important sampling ratio (r(ϕ)) at Line 17. The fourth step is to update the actor parameters at Line 18 using PPO-clip where 1 + ϵ occurs when the advantage estimation is positive else 1 −ϵ is used from Lines 19 to 23. The PPO-clip imposes the penalty on the r(ϕ) ratio in both cases. The fourth step is to update the critic parameter (θnew) at Line 24. The output to the algorithm is the actor-network that makes the decision to play the chunk by chunk with a specified bitrate at Line 29, the critic network evaluates the state-value of the policy with PPO-clip for maximizing rewards at Line 30 and the actor and critic parameters are updated based on the actor and the critic loss functions at Line 31.

**Fragmento 4 - p. 3 - score 1:**

Algorithm 1 presents the PPO-ABR algorithm and outlines the critical steps. The input to the algorithm is video samples, including hyperparameter setting for actor and critic networks and state input as st = (xt, dt, nt, bt, ct, lt, bwt, det). The first step is dividing a video file into chunks. Each chunk is played at a specified bitrate using the selection of the action based on the current state and the policy and to store the corresponding reward at Line 12. The actor-network finds the policy πϕ(.|st), and the critic network estimates the state value function. The second step of this algorithm is to compute the advantage function using a current policy at Line 15. The third step is Fig. 1. System Model depicting multimedia streaming.

**Fragmento 5 - p. 4 - score 1:**

Algorithm 1 PPO-ABR Algorithm 1: Input: video samples, hyperparameters; 2: Parameters: 3: Video vi; choose a video file as a input 4: Chunk c; select the bitrate for future chunks from video file 5: Initialize the batch size B, clipping parameter ϵ 6: Initialize weight parameters: θ, ϕ 7: for video vi= 1,2,3...., VI do 8: Observe initial state st; 9: for chunk c=1,2,3...., C do 10: V θ = PK k=1 V (st; θk) for all states st 11: R ←0 for terminal state sterminal 12: R = V t for non terminal states st 13: for each batch iteration do 14: Compute advantage function on B 15: Aϕ(s, a) = Qπ ϕ(s, a) −V π ϕ (s) 16: Compute the importance sampling weight 17: r(ϕ) = πϕnew (s,a) πϕ(s,a) using policy parameters 18: Update actor parameter by PPO- clip: maximizeϕLclip(ϕnew) = κEt " min LCP I(ϕ), clip(r(ϕ) , 1 −ϵ, 1 + ϵ)Aϕ(s, a) !# 19: if Aϕ(s, a) ≥0 then 20: clip(r(ϕ), 1 + ϵ)Aϕ(s, a) 21: else 22: clip(r(ϕ), 1 −ϵ)Aϕ(s, a) 23: end if 24: Update critic parameter θnew = θ + ∂(R−V θ)2 ∂θ 25: end for 26: end for 27: end for 28: Output: 29: Actor network makes the decision to play the chunk by chunk with a specified bitrate 30: Critic network evaluates the state-value of the policy with PPO-clip for maximizing rewards 31: Update actor and critic parameters θ, ϕ 500 video streaming sessions.

**Fragmento 6 - p. 6 - score 1:**

SIGCOMM ’17. New York, NY, USA: Association for Computing Machinery, 2017, p. 197–210. [7] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, and L. Sun, “Learning tailored adaptive bitrate algorithms to heterogeneous network conditions: A domain-specific priors and meta-reinforcement learning approach,” IEEE Journal on Selected Areas in Communications, vol. 40, no. 8, pp. 2485– 2503, 2022. [8] Y. Yuan, W. Wang, Y. Wang, S. S. Adhatarao, B. Ren, K. Zheng, and X. Fu, “Vsim: Improving qoe fairness for video streaming in mobile environments,” in IEEE INFOCOM 2022 - IEEE Conference on Computer Communications, 2022, pp. 1309–1318. [9] P. Saxena, M. Naresh, M. Gupta, A. Achanta, S. Kota, and S. Gupta, “Nancy: Neural adaptive network coding methodology for video dis- tribution over wireless networks,” in GLOBECOM 2020 - 2020 IEEE Global Communications Conference, 2020, pp.

**Fragmento 7 - p. 6 - score 1:**

[21] Z. Akhtar, Y. S. Nam, R. Govindan, S. Rao, J. Chen, E. Katz-Bassett, B. Ribeiro, J. Zhan, and H. Zhang, “Oboe: Auto-tuning video abr algorithms to network conditions,” in Proceedings of the 2018 Con- ference of the ACM Special Interest Group on Data Communication, ser. SIGCOMM ’18. New York, NY, USA: Association for Computing Machinery, 2018, p. 44–58. [22] S. Sengupta, N. Ganguly, S. Chakraborty, and P. De, “Hotdash: Hotspot aware adaptive video streaming using deep reinforcement learning,” 2018 IEEE 26th International Conference on Network Protocols (ICNP), pp. 165–175, 2018. [23] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, “Stick: A harmonious fusion of buffer-based and learning-based approach for adaptive streaming,” in IEEE INFOCOM 2020-IEEE Conference on Computer Communications.

**Fragmento 8 - p. 6 - score 1:**

SIGCOMM ’14. New York, NY, USA: Association for Computing Machinery, 2014, p. 187–198. [4] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “Bola: Near-optimal bi- trate adaptation for online videos,” in IEEE INFOCOM 2016 - The 35th Annual IEEE International Conference on Computer Communications, 2016, pp. 1–9. [5] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic approach for dynamic adaptive video streaming over http,” in Proceed- ings of the 2015 ACM Conference on Special Interest Group on Data Communication, ser. SIGCOMM ’15. New York, NY, USA: Association for Computing Machinery, 2015, p. 325–338. [6] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video stream- ing with pensieve,” in Proceedings of the Conference of the ACM Special Interest Group on Data Communication, ser.

**Fragmento 9 - p. 6 - score 1:**

abs/1707.06347, 2017. [Online]. Available: http://arxiv.org/abs/1707.06347 [18] Federal Communications Commission. (2016) Federal communications commission. 2016. raw data - measuring broadband america. [Online]. Available: https://www.fcc.gov/reports-research/reports/ measuring- broadband- america/raw- data- measuring- broadband- america- 2016 [19] H. Riiser, P. Vigmostad, C. Griwodz, and P. Halvorsen, “Commute path bandwidth traces from 3g networks: Analysis and applications,” ser. MMSys ’13. New York, NY, USA: Association for Computing Machinery, 2013, p. 114–118. [20] G. Yi, “The acm multimedia 2019 live video streaming grand challenge,” The ACM Multimedia 2019 Live Video Streaming Grand Challenge, October 21–25, 2019, Nice, France.


### 7.10. ideas fase45 v1 controller defendible

Palabras clave usadas: `risk, safe, safety, robust, conservative, fallback, uncertainty, capacity, lower bound, tail, severe, low buffer, volatile, variable, fluctuation, drop, zero, consistent, smoothness, auto-tuning, regime, cluster, guidance, hybrid, generalization, environment-aware, prediction, selector`

**Fragmento 1 - p. 1 - score 2:**

Consequently, suboptimal updates emerge when the behavior and target policies become out of synchronization, and (ii) there is a constraint on the divergence between the new and the old policies. Due to these constraints, these algorithms may result in imprecise throughput prediction when there are fluctuations in the network, re-buffering at the client’s device, and inaccurate bitrate selection impacting the overall QoE for the end users. To resolve the above issues, we propose the integration of Proximal Policy Optimization-based DRL for ABR (PPO-ABR) to use a clipped probability ratio for constraining the divergence between the new and the old policy parameters. Our experimental results show that PPO-ABR improves overall video QoE as compared to other state-of- the-art methods.

**Fragmento 2 - p. 4 - score 2:**

We compare the performance of all ABR algorithms using QoE [12] as a metric. The QoE is expressed as: QoE = N X n=1 q(bn) −µ N X n=1 Tn − N−1 X n=1 |q(bn+1) −q(bn)| (9) The QoE is composed of three elements: (i) the total bit rates of all video chunks, (ii) the penalty incurred by re-buffering, and (iii) the video’s smoothness, which is assessed by calcu- lating the difference in bit rates used to encode consecutive chunks. Various versions of the QoE metric are examined in this context as follows: (i) QoElin: q(bn) = bn with rebuffer penalty as µ = 4.3 and (ii) QoElog: q(bn) = log(b/bmin) with µ = 2.66. Note that we have utilized the above QoE metric formula- tion since it is commonly used in several other works including Robust-MPC [5], [6], [21], [22], [23] and [12].

**Fragmento 3 - p. 5 - score 2:**

At a bit rate of 12 Mbps and a latency of 30 ms throughout the testing phase, we assessed how well each ABR algorithm performed. Figure 5 displays the average total reward obtained by various ABR algorithms with the QoElin metric for each trace when the network is simulated during testing with no packet loss. According to our findings, the PPO-ABR algorithms have a higher average QoE of 46.61 than other ABR algorithms. TABLE III ON THREE DATASETS, THE AVERAGE QOE WAS ATTAINED USING TWO DIFFERENT QOE METRICS DURING SIMULATION WITH NO PACKET LOSSES. ABR algorithm FCC and Norway traces OBOE traces Live traces QoElin QoElog QoElin QoElog QoElin QoElog PPO-ABR 46.61 44.93 45.09 46.25 46.91 45.68 SAC-ABR 42.77 43.68 39.72 45.41 42.59 43.90 Pensieve 39.63 35.26 37.96 37.01 39.12 41.68 BB 12.03 12.78 14.08 20 13.81 20.26 RB 35.62 36.45 36.22 37.31 37.45 37.35 BOLA 34.26 35.30 35.04 37.09 35.82 36.05 Robust-MPC 39.93 40.44 40.18 38.29 40.59 38.99 In Figure 6, we compare various ABR algorithms using the average playback bitrate, rebuffering penalty, and smoothness penalty for the QoElin metric under emulation with no packet losses during testing in order to understand and illustrate the better performance of the PPO-ABR.

**Fragmento 4 - p. 6 - score 2:**

penalties. Similarly, BB likewise has a significant smoothness penalty. The PPO-ABR delivers a higher average bit rate and, in comparison, lower smoothness and rebuffering penalties. The PPO-ABR achieves an average QoE higher than the other ABR algorithms due to the combined effects of these individual components. The average QoE values attained by the ABR algorithms when evaluated on the network emulated with no packet losses are then shown in Table III for various QoE metrics. V. CONCLUSION We have shown in this study the advantages of adopt- ing on-policy DRL-based PPO-ABR to increase QoE for video streaming. Our suggested method specifically overcomes the limitations currently faced by state-of-the-art DRL-based methods and consistently achieves higher average QoE than SAC-ABR and Pensieve, respectively, by up to 13.52% and 27.42%, and even higher QoE when compared to other con- ventional fixed-rule-based ABR algorithms.

**Fragmento 5 - p. 1 - score 1:**

Several ABR algorithms such as RB [2], BB [3], BOLA [4], and Robust- MPC [5] use network conditions including throughput estima- tion, playback buffer occupancy or a combination of both for bitrate estimation with the aim to enhance the QoE for end users. However, traditional ABR algorithms are designed with specific network conditions and traffic pattern assumptions. As a result, they may not perform optimally in networks where network conditions and traffic patterns are subject to rapid and unpredictable change. Recently, several data-driven deep reinforcement learning (DRL) approaches, including Pensieve [6], A2BR [7], VSiM [8], NANCY [9], AL-FFEA3C [10], AL-AvgA3C [10], MARL-A3C [11], SAC-ABR [12] and ALISA [13] are proposed to improve the ABR algorithms.

**Fragmento 6 - p. 2 - score 1:**

We can rewrite equation (6) to maximize only the second part, also known as the surrogate advantage objective, as follows: maximizeϕ κEs∼ρπϕ,a∼πϕ " r(ϕ) Aϕ(s, a) # subject to DKL(πϕnew||πϕ) ≤λ (7) Although TRPO provides constraints on the divergence between the new and the old policies, it can still lead to instability in policy updates. To address this issue, the on- policy PPO algorithm [17] is proposed that uses a clipped probability ratio to constrain the divergence between the old and the new policy parameters. The objective function in PPO is derived from Equation (7), and the maximization problem is given as: maximizeϕLclip(ϕnew) = κEt " min LCP I(ϕ), clip(r(ϕ) , 1 −ϵ, 1 + ϵ)Aϕ(s, a) !# subject to DKL(πϕnew||πϕ) ≤λ (8) where ϵ is the hyperparameter for clipping and LCP I(ϕ) = κEt " r(ϕ) Aϕ(s, a) # where CPI refers to a conservative policy iteration.

**Fragmento 7 - p. 3 - score 1:**

The PPO-ABR trains multiple agents in parallel, so the multi-agents are trained with their environments for each batch iteration. Moreover, the actor and critic parameters are updated using PPO-clip for each batch iteration. The value function parameters are updated after multiple epochs instead of a single epoch. Further, the central agent collects the mini-batch samples and updates the gradient to the next batch iterations. Overall, PPO-ABR results in a stable update and provides the bit rate to encode the next chunk. IV. EXPERIMENTAL DETAILS AND RESULTS This section will describe the experimental methodology utilised for this study. This will include a description of the datasets used, the training method employed, the algorithms used for comparison, and the performance metrics used to assess their efficacy.

**Fragmento 8 - p. 4 - score 1:**

Hyperparameter Description Value Actor-critic algorithms γ Discount factor 0.99 Pensieve, SAC-ABR, PPO-ABR αp Actor network’s learning rate 0.0001 Pensieve, SAC-ABR, PPO-ABR αc Critic network’s learning rate 0.001 Pensieve, SAC-ABR, PPO-ABR η Entropy regularization factor range 6 to 0.01 Pensieve, SAC-ABR, PPO-ABR τ Interpolation factor 0.995 SAC-ABR ϵ clipping parameter 0.2 PPO-ABR R Random seed 42 PPO-ABR nact Total number of agents 16 Pensieve, SAC-ABR, PPO-ABR Fig. 2. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was measured during training over 100,000 epochs for the QoElin metric on FCC and Norway traces, and the average values were obtained. the following state-of-the-art DRL-based and non-DRL-based ABR algorithms: SAC-ABR [12], Pensieve [6], BB [3], RB [2], BOLA [4], and Robust-MPC [5].

**Fragmento 9 - p. 5 - score 1:**

It takes approximately eight hours to generate the training model for every algorithm with each dataset. Table II summarizes the QoE metrics obtained during training for the three datasets. The findings indicate that across all three datasets and for both QoElin and QoElog metrics, PPO-ABR consistently outperforms SAC-ABR and Pensieve, achieving higher QoE metrics. Fig. 5. Performance evaluation of ABR algorithms with QoElin metric when tested on the model trained with FCC and Norway traces while the network is emulated with no packet loss. Fig. 6. Comparing PPO-ABR with current ABR methods by analyzing their performance on the individual elements for QoElin metric with no packet loss under emulation (Equation 9).

**Fragmento 10 - p. 6 - score 1:**

SIGCOMM ’17. New York, NY, USA: Association for Computing Machinery, 2017, p. 197–210. [7] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, and L. Sun, “Learning tailored adaptive bitrate algorithms to heterogeneous network conditions: A domain-specific priors and meta-reinforcement learning approach,” IEEE Journal on Selected Areas in Communications, vol. 40, no. 8, pp. 2485– 2503, 2022. [8] Y. Yuan, W. Wang, Y. Wang, S. S. Adhatarao, B. Ren, K. Zheng, and X. Fu, “Vsim: Improving qoe fairness for video streaming in mobile environments,” in IEEE INFOCOM 2022 - IEEE Conference on Computer Communications, 2022, pp. 1309–1318. [9] P. Saxena, M. Naresh, M. Gupta, A. Achanta, S. Kota, and S. Gupta, “Nancy: Neural adaptive network coding methodology for video dis- tribution over wireless networks,” in GLOBECOM 2020 - 2020 IEEE Global Communications Conference, 2020, pp.

**Fragmento 11 - p. 6 - score 1:**

Future studies will examine PPO-ABR for edge-driven video distribution services and evaluate it using various QoE metric versions. ACKNOWLEDGMENT This work has been supported by TCS foundation under the TCS research scholar program, 2019-2023, India. REFERENCES [1] “ISO/IEC 23009-1:2014: Dynamic adaptive streaming over HTTP(DASH) – Part 1: Media presentation description and segment formats,” May 2014. [2] Y. Sun, X. Yin, J. Jiang, V. Sekar, F. Lin, N. Wang, T. Liu, and B. Sinopoli, “Cs2p: Improving video bitrate selection and adaptation with data-driven throughput prediction,” Proceedings of the 2016 ACM SIGCOMM Conference, 2016. [3] T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Watson, “A buffer-based approach to rate adaptation: Evidence from a large video streaming service,” in Proceedings of the 2014 ACM Conference on SIGCOMM, ser.

**Fragmento 12 - p. 6 - score 1:**

[21] Z. Akhtar, Y. S. Nam, R. Govindan, S. Rao, J. Chen, E. Katz-Bassett, B. Ribeiro, J. Zhan, and H. Zhang, “Oboe: Auto-tuning video abr algorithms to network conditions,” in Proceedings of the 2018 Con- ference of the ACM Special Interest Group on Data Communication, ser. SIGCOMM ’18. New York, NY, USA: Association for Computing Machinery, 2018, p. 44–58. [22] S. Sengupta, N. Ganguly, S. Chakraborty, and P. De, “Hotdash: Hotspot aware adaptive video streaming using deep reinforcement learning,” 2018 IEEE 26th International Conference on Network Protocols (ICNP), pp. 165–175, 2018. [23] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, “Stick: A harmonious fusion of buffer-based and learning-based approach for adaptive streaming,” in IEEE INFOCOM 2020-IEEE Conference on Computer Communications.


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
PPO-ABR: Proximal Policy Optimization based Deep
Reinforcement Learning for Adaptive BitRate streaming
Mandan Naresh, Paresh Saxena and Manik Gupta
Dept. of CSIS, BITS Pilani
Hyderabad, India
{p20180420, psaxena, manik}@hyderabad.bits-pilani.ac.in
Abstract—Providing a high Quality of Experience (QoE) for
video streaming in 5G and beyond 5G (B5G) networks is
challenging due to the dynamic nature of the underlying network
conditions. Several Adaptive Bit Rate (ABR) algorithms have
been developed to improve QoE, but most of them are designed
based on fixed rules and unsuitable for a wide range of net-
work conditions. Recently, Deep Reinforcement Learning (DRL)
based Asynchronous Advantage Actor-Critic (A3C) methods have
recently demonstrated promise in their ability to generalise to
diverse network conditions, but they still have limitations. One
specific issue with A3C methods is the lag between each actor’s
behavior policy and central learner’s target policy. Consequently,
suboptimal updates emerge when the behavior and target policies
become out of synchronization. In this paper, we address the
problems faced by vanilla-A3C by integrating the on-policy-
based multi-agent DRL method into the existing video streaming
framework. Specifically, we propose a novel system for ABR gen-
eration - Proximal Policy Optimization-based DRL for Adaptive
Bit Rate streaming (PPO-ABR). Our proposed method improves
the overall video QoE by maximizing sample efficiency using a
clipped probability ratio between the new and the old policies on
multiple epochs of minibatch updates. The experiments on real
network traces demonstrate that PPO-ABR outperforms state-
of-the-art methods for different QoE variants.
Index Terms—Reinforcement learning, video streaming, policy
optimization, adaptive bit rate.
I. INTRODUCTION
Due to the widespread use of the Internet, the volume of
multimedia traffic has increased, including video streaming.
The Cisco annual Internet Report projects that by 2023, 69%
of the world’s population will have access to the Internet, with
Internet video traffic significantly outnumbering other Internet
traffic. In order to ensure seamless video streaming, Dynamic
Adaptive Streaming over HTTP (DASH) [1] uses an adaptive
bit rate (ABR) algorithm to send the video encoded at a
specific bitrate based on the network conditions. Several ABR
algorithms such as RB [2], BB [3], BOLA [4], and Robust-
MPC [5] use network conditions including throughput estima-
tion, playback buffer occupancy or a combination of both for
bitrate estimation with the aim to enhance the QoE for end
users. However, traditional ABR algorithms are designed with
specific network conditions and traffic pattern assumptions. As
a result, they may not perform optimally in networks where
network conditions and traffic patterns are subject to rapid
and unpredictable change. Recently, several data-driven deep
reinforcement learning (DRL) approaches, including Pensieve
[6], A2BR [7], VSiM [8], NANCY [9], AL-FFEA3C [10],
AL-AvgA3C [10], MARL-A3C [11], SAC-ABR [12] and
ALISA [13] are proposed to improve the ABR algorithms.
DRL is a branch of deep learning that deals with how agents
should behave depending on the state of the environment. In
DRL, a policy is created to maximize the expected cumulative
reward. The policy is the mapping function from states of
the environment to actions. Pensieve [6], being one of the
first DRL-based methods for ABR generation, is built upon
the basic vanilla-A3C algorithm, whereas ALISA [13], being
the latest DRL-based ABR method, utilizes soft updates with
an A3C algorithm. Both Pensieve and ALISA update the
ABR control policy based on the current network conditions
and past decisions, and it is able to identify policies that
outperform traditional ABR algorithms.
However, these state-of-the-art DRL-based methods suffer
from two key drawbacks: (i) there is a lag between each
actor’s behavior policy and the central learner’s target policy.
Consequently, suboptimal updates emerge when the behavior
and target policies become out of synchronization, and (ii)
there is a constraint on the divergence between the new and
the old policies. Due to these constraints, these algorithms
may result in imprecise throughput prediction when there are
fluctuations in the network, re-buffering at the client’s device,
and inaccurate bitrate selection impacting the overall QoE
for the end users. To resolve the above issues, we propose
the integration of Proximal Policy Optimization-based DRL
for ABR (PPO-ABR) to use a clipped probability ratio for
constraining the divergence between the new and the old policy
parameters. Our experimental results show that PPO-ABR
improves overall video QoE as compared to other state-of-
the-art methods.
The rest of the paper is organized as follows: Section II
presents the relevant background on reinforcement learning
and on-policy RL methods. Section III presents the design
of the proposed PPO-ABR algorithm. We present the experi-
mental setup and results in Section IV where we include both
training and testing results. Finally, we conclude our work in
Section V.
II. BACKGROUND
RL [14] is a learning process that is adaptive to dynamic
environments, even in cases where there is little or no prior
979-8-3503-3339-8/23/$31.00 ©2023 IEEE
199
2023 International Wireless Communications and Mobile Computing (IWCMC) | 979-8-3503-3339-8/23/$31.00 ©2023 IEEE | DOI: 10.1109/IWCMC58020.2023.10182379
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 2
```text
information. By learning from its mistakes, an agent seeks to
optimize its long-term return in the future. The agent’s inter-
actions with the environment are described using a Markov
decision process (MDP), where at each time step (represented
by t = 0, 1, 2, 3, ...), the agent is situated in a specific state
(st), chooses an action from a set of available actions (at ∈A),
and then receives a reward (rt = R(st, at)) based on its action.
The goal of the agent is to find a policy π(s, a) that maps
states to actions. The state-value function is given by V π
ϕ (s) =
E
"
P∞
k=0 γkrt+k|st = s, πϕ
#
and the action-value function is
given by, Qπ
ϕ(s, a) = E
"
P∞
k=0 γkrt+k|st = s, at = a, πϕ
#
where, γ ∈[0, 1) is a discount factor. The basic on-policy RL
method is a vanilla policy gradient method [15] where policy
parameters are updated after the calculation of the total reward
at the end of the episode instead of a single-step. The policy
gradient is given by,
∇ϕk =
T
X
t=0
∇ϕ log πϕ(at, st)|ϕkAϕ(s, a)
(1)
where Aϕ(s, a) = Qπ
ϕ(s, a) −V π
ϕ (s) is the advantage
function, ∇ϕ is the policy optimization using a gradient
operator, T is the number of steps in the episode and ϕk
is the current policy parameters. However, the vanilla policy
gradient suffers from high variance and high training time
due to value estimates being calculated at the end of the
episodes instead of every time step. To address these issues,
actor-critic methods [15] are proposed. These methods have
two components: an actor represented by a policy π and a
critic represented by an estimate of the action-value function.
Neural network function approximators are typically used to
represent both of them. With parameters θ, the critic estimates
the current policy’s value function. The main goal of this
method is to reduce the variance using single-step state-value
estimates. The single-step state-value estimates are derived
using a temporal difference (δ), and it is given by:
δ = V π
ϕ (st) + γV π
ϕ (st+1, ϕ) −V π
ϕ (st, ϕ)
(2)
The gradient operator ∇is used to define the policy and
critic updates with regard to its parameters ϕ and θ, respec-
tively:
∆ϕ = ϕ + αpδ∇πϕ(st+1, at+1, ϕ)
(3)
∆θ = θ + αcδ∇V π
ϕ (st, θ)
(4)
where αp and αc are the actor and critic learning rates,
respectively. Furthermore, as an improvement, vanilla-A3C
[15] is proposed that uses several copies of the same agent
with asynchronous updates. It is more efficient than the actor-
critic methods because samples for data can be parallelized
using several copies of the same agent resulting in an even
smaller training time. In the vanilla-A3C algorithm, the current
policy parameters (ϕnew) are updated based on previously
collected experience with old policy parameters (ϕ) after every
κ steps, i.e., after every κ state-action pairs. The equation
below represents the value function update for vanilla-A3C
is:
maximizeϕ V π
ϕnew(s) = κ∇V π
ϕ (s) + κ P
s ρπϕ(s) P
a πϕnew(a|s)Aϕ(s, a)
(5)
where ρπ(s) presents distribution of state-action pairs, πϕ
represents the old policy and πϕnew represents current policy.
Note that P
a πϕnew(a|s)Aϕ(s, a) ≥0 aims to increase the
value function, however, P
a πϕnew(a|s)Aϕ(s, a) < 0 can
result in a decrease in the value function and in a increase
of divergence between the old and the new policies.
To alleviate this issue, the on-policy trust region policy
optimization (TRPO) [16] proposes Kullback–Leibler (KL) di-
vergence constraint to update the value function. The equation
(5) is rewritten with KL divergence constraint as follows:
maximizeϕ V π
ϕnew(s) = κ∇V π
ϕ (s) + κEs∼ρπϕ,a∼πϕ
"
r(ϕ) Aϕ(s, a)
#
subject to DKL(πϕnew||πϕ) ≤λ
(6)
where r(ϕ) =
πϕnew (s,a)
πϕ(s,a)
is the importance sampling ra-
tio, DKL(πϕnew||πϕ) = P
a πϕnew(s, a) log
 
πϕnew (s,a)
πϕ(s,a)
!
and
DKL(πϕnew||πϕ) ≤λ is used to constrain the divergence
between the new and old policies with λ as a KL-divergence
limit, λ ∈(0, 1]. We can rewrite equation (6) to maximize
only the second part, also known as the surrogate advantage
objective, as follows:
maximizeϕ κEs∼ρπϕ,a∼πϕ
"
r(ϕ) Aϕ(s, a)
#
subject to DKL(πϕnew||πϕ) ≤λ
(7)
Although TRPO provides constraints on the divergence
between the new and the old policies, it can still lead to
instability in policy updates. To address this issue, the on-
policy PPO algorithm [17] is proposed that uses a clipped
probability ratio to constrain the divergence between the old
and the new policy parameters. The objective function in PPO
is derived from Equation (7), and the maximization problem
is given as:
maximizeϕLclip(ϕnew) = κEt
"
min
 
LCP I(ϕ), clip(r(ϕ) , 1 −ϵ, 1 + ϵ)Aϕ(s, a)
!#
subject to DKL(πϕnew||πϕ) ≤λ
(8)
where ϵ is the hyperparameter for clipping and LCP I(ϕ) =
κEt
"
r(ϕ) Aϕ(s, a)
#
where CPI refers to a conservative policy
iteration. From Equation (8), the first term represents the
TRPO unclipped surrogate objective, and the second term
200
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 3
```text
represents a modification of the TRPO surrogate objective
using a clipped probability ratio ϵ, which ensures that the r(ϕ)
remains within the range [1−ϵ, 1+ϵ]. The PPO maximization
considers the minimum of the clipped and unclipped objectives
resulting in a smaller divergence between the new and the old
policy parameters.
III. PROPOSED ON-POLICY ABR METHOD: PPO-ABR
In this paper, we focus on the HTTP-based video distri-
bution system, as shown in Figure 1 that utilize the DASH
framework for multimedia streaming. In such systems, the
videos are stored on the server in separate chunks, where
each chunk is encoded with a specific bitrate. The client then
requests each chunk with the appropriate bitrate from the
server using an ABR algorithm, where the ABR algorithm
generates the bit rate based on factors such as the available
network conditions and the capabilities of the client device.
Specifically, an ABR algorithm selects the bitrate for each
video chunk based on chunk processor input observations,
including the number of chunks (ct), chunk size (nt), chunk
bitrate (lt), size of the buffer (bt), throughput (xt), and
download time (dt). Additionally, the ABR controller takes
the network statistics such as bandwidth (bwt) and delay (det)
into account.
For the state-of-the-art vanilla-A3C, the ABR controller
uses multi-agent training with multiple actor and critic
neural networks. Each agent is trained in parallel with
its own environment based on several state inputs st
=
(xt, dt, nt, bt, ct, lt, bwt, det). Moreover, each agent is trained
and sends the local gradients to the central agent. Once the
central agent has collected experience from the local agents,
it updates its model parameters. Further, the central agent will
make the decision to play the chunk with a specified bitrate to
the chunk handler. The chunk handler sends the information
about the chunk to the buffer and finally, the client will play
the chunk n with quality q based on buffer occupancy.
In addition to being less sample efficient, the vanilla-A3C
also has a high divergence between the target policy of the
central learner and every actor’s behavior policy. The subop-
timal updates emerge when the behavior and target policies
become out of synchronization. To address these issues, PPO-
ABR uses a clipped probability ratio to constrain the KL-
divergence between the new and the old policy parameters
among several epochs instead of a single epoch as in vanilla-
A3C.
Algorithm 1 presents the PPO-ABR algorithm and outlines
the critical steps. The input to the algorithm is video samples,
including hyperparameter setting for actor and critic networks
and state input as st = (xt, dt, nt, bt, ct, lt, bwt, det). The first
step is dividing a video file into chunks. Each chunk is played
at a specified bitrate using the selection of the action based on
the current state and the policy and to store the corresponding
reward at Line 12. The actor-network finds the policy πϕ(.|st),
and the critic network estimates the state value function. The
second step of this algorithm is to compute the advantage
function using a current policy at Line 15. The third step is
Fig. 1. System Model depicting multimedia streaming.
to compute the policy divergence between the new and the
old policies using an important sampling ratio (r(ϕ)) at Line
17. The fourth step is to update the actor parameters at Line
18 using PPO-clip where 1 + ϵ occurs when the advantage
estimation is positive else 1 −ϵ is used from Lines 19 to 23.
The PPO-clip imposes the penalty on the r(ϕ) ratio in both
cases. The fourth step is to update the critic parameter (θnew)
at Line 24.
The output to the algorithm is the actor-network that makes
the decision to play the chunk by chunk with a specified bitrate
at Line 29, the critic network evaluates the state-value of the
policy with PPO-clip for maximizing rewards at Line 30 and
the actor and critic parameters are updated based on the actor
and the critic loss functions at Line 31. The PPO-ABR trains
multiple agents in parallel, so the multi-agents are trained with
their environments for each batch iteration. Moreover, the actor
and critic parameters are updated using PPO-clip for each
batch iteration. The value function parameters are updated
after multiple epochs instead of a single epoch. Further, the
central agent collects the mini-batch samples and updates the
gradient to the next batch iterations. Overall, PPO-ABR results
in a stable update and provides the bit rate to encode the next
chunk.
IV. EXPERIMENTAL DETAILS AND RESULTS
This section will describe the experimental methodology
utilised for this study. This will include a description of the
datasets used, the training method employed, the algorithms
used for comparison, and the performance metrics used to
assess their efficacy.
A. Datasets
We utilised multiple datasets FCC [18], Norway [19], LIVE
[20], OBOE [21] for our experimentation, including both
broadband and mobile datasets. First, we utilised the FCC
[18] and Norway datasets [19], which include fixed broad-
band technologies and Telenor’s 3G/HSDPA mobile wireless
network. We utilized 59 and 68 traces from FCC and Norway
throughput traces, respectively for our experiments. The range
of throughput for both datasets is 0 to 6 Mbps. Secondly,
we used live video streaming datasets [20], which consists
of data from wireless networks such as WiFi and 4G. The
throughput range of these traces is between 0.2 Mbps and 4
Mbps, and 100 traces are utilised in our experiments. Lastly,
we utilised OBOE dataset [21], which include 428 traces from
201
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 4
```text
Algorithm 1 PPO-ABR Algorithm
1: Input: video samples, hyperparameters;
2: Parameters:
3: Video vi; choose a video file as a input
4: Chunk c; select the bitrate for future chunks from video
file
5: Initialize the batch size B, clipping parameter ϵ
6: Initialize weight parameters: θ, ϕ
7: for video vi= 1,2,3...., VI do
8:
Observe initial state st;
9:
for chunk c=1,2,3...., C do
10:
V θ = PK
k=1 V (st; θk) for all states st
11:
R ←0 for terminal state sterminal
12:
R = V t for non terminal states st
13:
for each batch iteration do
14:
Compute advantage function on B
15:
Aϕ(s, a) = Qπ
ϕ(s, a) −V π
ϕ (s)
16:
Compute the importance sampling weight
17:
r(ϕ) = πϕnew (s,a)
πϕ(s,a)
using policy parameters
18:
Update
actor
parameter
by
PPO-
clip:
maximizeϕLclip(ϕnew)
=
κEt
"
min
 
LCP I(ϕ), clip(r(ϕ) , 1 −ϵ, 1 + ϵ)Aϕ(s, a)
!#
19:
if Aϕ(s, a) ≥0 then
20:
clip(r(ϕ), 1 + ϵ)Aϕ(s, a)
21:
else
22:
clip(r(ϕ), 1 −ϵ)Aϕ(s, a)
23:
end if
24:
Update critic parameter θnew = θ + ∂(R−V θ)2
∂θ
25:
end for
26:
end for
27: end for
28: Output:
29: Actor network makes the decision to play the chunk by
chunk with a specified bitrate
30: Critic network evaluates the state-value of the policy with
PPO-clip for maximizing rewards
31: Update actor and critic parameters θ, ϕ
500 video streaming sessions. Each OBOE trace stores the
bandwidth measurements collected from wired, wireless, and
cellular connections, and the throughput range is between 0
and 3 Mbps.
B. Methodologies for Training, Comparative Algorithms, and
Performance Metrics
We train PPO-ABR on the aforementioned datasets for
100,000 iterations, and then we choose the model with the
highest average reward. Table I summarizes the hyperpa-
rameters utilized for PPO-ABR training. Specifically, clipped
probability hyperparameter ϵ = 0.2 determines how much the
new policy deviates from the old policy. These values have
been selected based on the previous works [6], [21], and [20].
We use nact = 16 agents for all our experiments. Finally, the
performance of the proposed PPO-ABR is compared to that of
TABLE I
HYPERPARAMETERS USED DURING THE TRAINING FOR PENSIEVE,
SAC-ABR, AND PPO-ABR.
Hyperparameter
Description
Value
Actor-critic algorithms
γ
Discount factor
0.99
Pensieve, SAC-ABR, PPO-ABR
αp
Actor network’s learning rate
0.0001
Pensieve, SAC-ABR, PPO-ABR
αc
Critic network’s learning rate
0.001
Pensieve, SAC-ABR, PPO-ABR
η
Entropy regularization factor range
6 to 0.01
Pensieve, SAC-ABR, PPO-ABR
τ
Interpolation factor
0.995
SAC-ABR
ϵ
clipping parameter
0.2
PPO-ABR
R
Random seed
42
PPO-ABR
nact
Total number of agents
16
Pensieve, SAC-ABR, PPO-ABR
Fig. 2. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was
measured during training over 100,000 epochs for the QoElin metric on FCC
and Norway traces, and the average values were obtained.
the following state-of-the-art DRL-based and non-DRL-based
ABR algorithms: SAC-ABR [12], Pensieve [6], BB [3], RB
[2], BOLA [4], and Robust-MPC [5].
We compare the performance of all ABR algorithms using
QoE [12] as a metric. The QoE is expressed as:
QoE =
N
X
n=1
q(bn) −µ
N
X
n=1
Tn −
N−1
X
n=1
|q(bn+1) −q(bn)| (9)
The QoE is composed of three elements: (i) the total bit rates
of all video chunks, (ii) the penalty incurred by re-buffering,
and (iii) the video’s smoothness, which is assessed by calcu-
lating the difference in bit rates used to encode consecutive
chunks. Various versions of the QoE metric are examined in
this context as follows: (i) QoElin: q(bn) = bn with rebuffer
penalty as µ = 4.3 and (ii) QoElog: q(bn) = log(b/bmin)
with µ = 2.66.
Note that we have utilized the above QoE metric formula-
tion since it is commonly used in several other works including
Robust-MPC [5], [6], [21], [22], [23] and [12]. There also exist
other QoE metric formulations, for example in [7] and [8], that
can also be used for the performance evaluation. In this work,
we focus only on the QoE metric defined in Equation 9.
TABLE II
TRAINING OUTCOMES OF PENSIEVE, SAC-ABR, AND PPO-ABR
CONCERNING THE QoElin AND QoElog METRICS ACROSS MULTIPLE
DATASETS.
RL algorithm
FCC Norway Traces
OBOE Traces
Live traces
QoElin
QoElog
QoElin
QoElog
QoElin
QoElog
PPO-ABR
45.48
45.40
45.79
46.36
44.84
45.89
SAC-ABR
42.60
45.20
41.33
43.88
41.70
43.46
Pensieve
37.45
37.84
37.05
36.30
37.20
37.59
202
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 5
```text
Fig. 3. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was
measured during training over 100,000 epochs for the QoElin metric on
OBOE traces, and the average values were obtained.
Fig. 4. The QoE performance of Pensieve, SAC-ABR, and PPO-ABR was
measured during training over 100,000 epochs for the QoElin metric on Live
traces, and the average values were obtained.
C. Training results
We trained PPO-ABR, SAC-ABR, and Pensieve using the
three datasets mentioned in the preceding section. Further-
more, in order to maximize entropy, we utilized an entropy
regularization ranging from 6 to 0.01 for a better exploration-
exploitation tradeoff, i.e., initially, an entropy value of six is
used for a few iterations, and then it is gradually decreased
to 0.01. It takes approximately eight hours to generate the
training model for every algorithm with each dataset. Table
II summarizes the QoE metrics obtained during training for
the three datasets. The findings indicate that across all three
datasets and for both QoElin and QoElog metrics, PPO-ABR
consistently outperforms SAC-ABR and Pensieve, achieving
higher QoE metrics.
Fig. 5. Performance evaluation of ABR algorithms with QoElin metric when
tested on the model trained with FCC and Norway traces while the network
is emulated with no packet loss.
Fig. 6. Comparing PPO-ABR with current ABR methods by analyzing their
performance on the individual elements for QoElin metric with no packet
loss under emulation (Equation 9).
Figure 2 presents the average QoE value achieved by PPO-
ABR, SAC-ABR, and Pensieve algorithms at each training
epoch. We can observe that SAC-ABR performs poorly at the
initial stages of training due to high exploration. Our results
show different behavior for each of these algorithms when the
number of epochs increases during the training. The PPO-ABR
achieves a high QoE value right from the start of the training.
Similar improvements are observed with OBOE in Figure 3
and Live traces in Figure 4 as well, where Table II presents
the values of QoE obtained using different ABR algorithms.
D. Testing results
The training models are evaluated using the Mahimahi
simulator [24]. We used 250 traces from the Norway test
datasets and 205 traces from the FCC test datasets to test
the models, as stated in [6]. At a bit rate of 12 Mbps and a
latency of 30 ms throughout the testing phase, we assessed
how well each ABR algorithm performed. Figure 5 displays
the average total reward obtained by various ABR algorithms
with the QoElin metric for each trace when the network is
simulated during testing with no packet loss. According to our
findings, the PPO-ABR algorithms have a higher average QoE
of 46.61 than other ABR algorithms.
TABLE III
ON THREE DATASETS, THE AVERAGE QOE WAS ATTAINED USING TWO
DIFFERENT QOE METRICS DURING SIMULATION WITH NO PACKET
LOSSES.
ABR algorithm
FCC and Norway traces
OBOE traces
Live traces
QoElin
QoElog
QoElin
QoElog
QoElin
QoElog
PPO-ABR
46.61
44.93
45.09
46.25
46.91
45.68
SAC-ABR
42.77
43.68
39.72
45.41
42.59
43.90
Pensieve
39.63
35.26
37.96
37.01
39.12
41.68
BB
12.03
12.78
14.08
20
13.81
20.26
RB
35.62
36.45
36.22
37.31
37.45
37.35
BOLA
34.26
35.30
35.04
37.09
35.82
36.05
Robust-MPC
39.93
40.44
40.18
38.29
40.59
38.99
In Figure 6, we compare various ABR algorithms using the
average playback bitrate, rebuffering penalty, and smoothness
penalty for the QoElin metric under emulation with no packet
losses during testing in order to understand and illustrate the
better performance of the PPO-ABR. Our findings indicate
that, with the exception of BOLA and RB, most ABR al-
gorithms attain greater bitrates. Several of these algorithms
experience rebuffering penalties due to the higher bitrate
choice, with BB and SAC-ABR having the biggest rebuffering
203
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 6
```text
penalties. Similarly, BB likewise has a significant smoothness
penalty. The PPO-ABR delivers a higher average bit rate and,
in comparison, lower smoothness and rebuffering penalties.
The PPO-ABR achieves an average QoE higher than the
other ABR algorithms due to the combined effects of these
individual components. The average QoE values attained by
the ABR algorithms when evaluated on the network emulated
with no packet losses are then shown in Table III for various
QoE metrics.
V. CONCLUSION
We have shown in this study the advantages of adopt-
ing on-policy DRL-based PPO-ABR to increase QoE for
video streaming. Our suggested method specifically overcomes
the limitations currently faced by state-of-the-art DRL-based
methods and consistently achieves higher average QoE than
SAC-ABR and Pensieve, respectively, by up to 13.52% and
27.42%, and even higher QoE when compared to other con-
ventional fixed-rule-based ABR algorithms. Future studies will
examine PPO-ABR for edge-driven video distribution services
and evaluate it using various QoE metric versions.
ACKNOWLEDGMENT
This work has been supported by TCS foundation under the
TCS research scholar program, 2019-2023, India.
REFERENCES
[1] “ISO/IEC
23009-1:2014:
Dynamic
adaptive
streaming
over
HTTP(DASH) – Part 1: Media presentation description and segment
formats,” May 2014.
[2] Y. Sun, X. Yin, J. Jiang, V. Sekar, F. Lin, N. Wang, T. Liu, and
B. Sinopoli, “Cs2p: Improving video bitrate selection and adaptation
with data-driven throughput prediction,” Proceedings of the 2016 ACM
SIGCOMM Conference, 2016.
[3] T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Watson, “A
buffer-based approach to rate adaptation: Evidence from a large video
streaming service,” in Proceedings of the 2014 ACM Conference on
SIGCOMM, ser. SIGCOMM ’14.
New York, NY, USA: Association
for Computing Machinery, 2014, p. 187–198.
[4] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “Bola: Near-optimal bi-
trate adaptation for online videos,” in IEEE INFOCOM 2016 - The 35th
Annual IEEE International Conference on Computer Communications,
2016, pp. 1–9.
[5] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic
approach for dynamic adaptive video streaming over http,” in Proceed-
ings of the 2015 ACM Conference on Special Interest Group on Data
Communication, ser. SIGCOMM ’15. New York, NY, USA: Association
for Computing Machinery, 2015, p. 325–338.
[6] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video stream-
ing with pensieve,” in Proceedings of the Conference of the ACM
Special Interest Group on Data Communication, ser. SIGCOMM ’17.
New York, NY, USA: Association for Computing Machinery, 2017, p.
197–210.
[7] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, and L. Sun, “Learning tailored
adaptive bitrate algorithms to heterogeneous network conditions: A
domain-specific priors and meta-reinforcement learning approach,” IEEE
Journal on Selected Areas in Communications, vol. 40, no. 8, pp. 2485–
2503, 2022.
[8] Y. Yuan, W. Wang, Y. Wang, S. S. Adhatarao, B. Ren, K. Zheng,
and X. Fu, “Vsim: Improving qoe fairness for video streaming in
mobile environments,” in IEEE INFOCOM 2022 - IEEE Conference
on Computer Communications, 2022, pp. 1309–1318.
[9] P. Saxena, M. Naresh, M. Gupta, A. Achanta, S. Kota, and S. Gupta,
“Nancy: Neural adaptive network coding methodology for video dis-
tribution over wireless networks,” in GLOBECOM 2020 - 2020 IEEE
Global Communications Conference, 2020, pp. 1–6.
[10] M. Naresh, V. Das, P. Saxena, and M. Gupta, “Deep reinforcement
learning based qoe-aware actor-learner architectures for video streaming
in iot environments,” Computing, vol. 104, 07 2022.
[11] H. Jin, Q. Wang, S. Li, and J. Chen, “Joint qos control and bitrate selec-
tion for video streaming based on multi-agent reinforcement learning,”
in 2020 IEEE 16th International Conference on Control & Automation
(ICCA), 2020, pp. 1360–1365.
[12] M. Naresh, N. Gireesh, P. Saxena, and M. Gupta, “Sac-abr: Soft actor-
critic based deep reinforcement learning for adaptive bitrate streaming,”
in 2022 14th International Conference on COMmunication Systems &
NETworkS (COMSNETS), 2022, pp. 353–361.
[13] M. Naresh, P. Saxena, and M. Gupta, “Deep reinforcement learning
with importance weighted a3c for qoe enhancement in video delivery
services,” arXiv preprint arXiv:2304.04527, 2023.
[14] R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction.
Cambridge, MA, USA: A Bradford Book, 2018.
[15] V. Mnih, A. P. Badia, M. Mirza, A. Graves, T. P. Lillicrap, T. Harley,
D. Silver, and K. Kavukcuoglu, “Asynchronous methods for deep
reinforcement learning,” CoRR, vol. abs/1602.01783, 2016.
[16] J. Schulman, S. Levine, P. Moritz, M. I. Jordan, and P. Abbeel,
“Trust region policy optimization,” CoRR, vol. abs/1502.05477, 2015.
[Online]. Available: http://arxiv.org/abs/1502.05477
[17] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov,
“Proximal policy optimization algorithms,” CoRR, vol. abs/1707.06347,
2017. [Online]. Available: http://arxiv.org/abs/1707.06347
[18] Federal Communications Commission. (2016) Federal communications
commission. 2016. raw data - measuring broadband america. [Online].
Available:
https://www.fcc.gov/reports-research/reports/
measuring-
broadband- america/raw- data- measuring- broadband- america- 2016
[19] H. Riiser, P. Vigmostad, C. Griwodz, and P. Halvorsen, “Commute
path bandwidth traces from 3g networks: Analysis and applications,”
ser. MMSys ’13.
New York, NY, USA: Association for Computing
Machinery, 2013, p. 114–118.
[20] G. Yi, “The acm multimedia 2019 live video streaming grand challenge,”
The ACM Multimedia 2019 Live Video Streaming Grand Challenge,
October 21–25, 2019, Nice, France.
[21] Z. Akhtar, Y. S. Nam, R. Govindan, S. Rao, J. Chen, E. Katz-Bassett,
B. Ribeiro, J. Zhan, and H. Zhang, “Oboe: Auto-tuning video abr
algorithms to network conditions,” in Proceedings of the 2018 Con-
ference of the ACM Special Interest Group on Data Communication,
ser. SIGCOMM ’18.
New York, NY, USA: Association for Computing
Machinery, 2018, p. 44–58.
[22] S. Sengupta, N. Ganguly, S. Chakraborty, and P. De, “Hotdash: Hotspot
aware adaptive video streaming using deep reinforcement learning,”
2018 IEEE 26th International Conference on Network Protocols (ICNP),
pp. 165–175, 2018.
[23] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, “Stick:
A harmonious fusion of buffer-based and learning-based approach for
adaptive streaming,” in IEEE INFOCOM 2020-IEEE Conference on
Computer Communications.
IEEE, 2020, pp. 1967–1976.
[24] R. Netravali, A. Sivaraman, S. Das, A. Goyal, K. Winstein, J. Mickens,
and H. Balakrishnan, “Mahimahi: Accurate record-and-replay for http.”
USA: USENIX Association, 2015.
204
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:46:34 UTC from IEEE Xplore.  Restrictions apply.
```
