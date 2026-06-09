# Bitrate Adaptation and Guidance With Meta Reinforcement Learning - Ahaggar

## 0. Identificacion del archivo

- Archivo fuente: `Bitrate_Adaptation_and_Guidance_With_Meta_Reinforcement_Learning.pdf`
- Paginas detectadas: `15`
- SHA256 PDF: `1d96730b63c13a139627db089bffe0a1190a3da93f407293ac204c34ab7a976f`
- Texto crudo auxiliar PyMuPDF: `raw_text/22_ahaggar_bitrate_guidance_meta_rl_cmcd_cmsd.txt`
- Texto crudo auxiliar pdftotext -layout: `raw_text_layout/22_ahaggar_bitrate_guidance_meta_rl_cmcd_cmsd_layout.txt`

## 1. Uso previsto para Fase 4-5 v1

Fuente esencial para integracion/hibridacion: IA como guidance servidor-cliente, CMCD/CMSD, metadatos, device/content/network features y heuristicas del cliente. Muy relevante para pensar controllers propios que combinan modelo + decision segura, no caja negra pura.

## 2. Advertencia de fidelidad

Este archivo NO es un resumen breve. Es una extraccion tecnica densa para que Codex pueda leer el paper sin depender de conversiones Markdown corruptas. El PDF original sigue siendo la fuente de verdad para formulas, tablas, figuras, simbolos y resultados exactos. Cuando una formula, tabla o figura sea decisiva, se debe verificar contra el PDF original.

## 3. Identificacion textual extraida de las primeras paginas

```text
10378
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024
Bitrate Adaptation and Guidance With Meta
Reinforcement Learning
Abdelhak Bentaleb
, Member, IEEE, May Lim
, Mehmet N. Akcay
, Ali C. Begen
, Senior Member, IEEE,
and Roger Zimmermann
, Senior Member, IEEE
Abstract—Adaptive bitrate (ABR) schemes enable streaming
clients to adapt to time-varying network/device conditions for a
stall-free viewing experience. Most ABR schemes use manually
tuned heuristics or learning-based methods. Heuristics are easy to
implement but do not always perform well, whereas learning-based
methods generally perform well but are difﬁcult to deploy on
low-resource devices. To make the most out of both worlds, we
earlier developed Ahaggar, a learning-based scheme executing
on the server side that provides quality-aware bitrate guidance to
streaming clients running their own heuristics. Ahaggar’s novelty
is the meta reinforcement learning approach taking network condi-
tions, clients’ statuses and device resolutions, and streamed content
as input features to perform bitrate guidance. Ahaggar uses the
new Common Media Client/Server Data (CMCD/SD) protocols to
exchange the necessary metadata between the servers and clients.
While Ahaggar was a signiﬁcant step forward, in this study, we
focus on three open areas, namely, (i) exploring the performance of
Ahaggar in a heterogeneous environment including both Ahag-
gar and non-Ahaggar clients with varied network conditions
and device resolutions, and (ii) quantifying the impact of device
resolutions on QoE with Ahaggar. We thoroughly investigate these
areas and report our ﬁndings. We also (iii) discuss the Ahaggar
design choices. Experiments on an open-source system show that
Ahaggar adapts to unseen conditions fast and outperforms its
competitors in several viewer experience metrics.
Index Terms—Adaptive streaming, meta-RL, ABR, CMCD,
CMSD, bitrate guidance, quality awareness.
I. INTRODUCTION
W
ITH the prevalence of HTTP adaptive streaming (HAS),
the design of adaptive bitrate (ABR) logic—the algo-
rithm deciding which segments to download and when (pri-
marily based on the advertised encoding bitrate)—has received
Manuscript received 22 January 2024; accepted 5 March 2024. Date of
publication 12 March 2024; date of current version 3 October 2024. This
work was supported in part by Singapore MoE Academic Research Fund Tier
2 under MOE’s ofﬁcial under Grant T2EP20221-0023, and in part by the
ScientiﬁcandTechnologicalResearchCouncilofTürkiyeunderGrant120C154.
Recommended for acceptance by R. Zhang. (Corresponding author: Abdelhak
Bentaleb.)
Abdelhak Bentaleb is with the Gina Cody School of Engineering and Com-
puter Science, Concordia University, Montreal, QC H3G 1M8, Canada (e-mail:
abdelhak.bentaleb@concordia.ca).
May Lim and Roger Zimmermann are with the School of Computing,
National University of Singapore, Singapore 119077 (e-mail: maylim@comp.
nus.edu.sg; rogerz@comp.nus.edu.sg).
Mehmet N. Akcay and Ali C. Begen are with Ozyegin University,
34794 Istanbul, Türkiye (e-mail: necmettin.akcay@ozu.edu.tr; ali.begen@
ozyegin.edu.tr).
This
article
has
supplementary
downloadable
material
available
at
https://doi.org/10.1109/TMC.2024.3376560, provided by the authors.
Digital Object Identiﬁer 10.1109/TMC.2024.3376560
signiﬁcantresearchattention.ExistingABRschemes[15]canbe
broadly classiﬁed as heuristic or learning-based. ABR schemes
driven by heuristics make decisions based on client-side ob-
servations such as throughput estimation [31], playback buffer
level [47] or a combination of the two [53]. Although these
schemes are easy to implement, they heavily depend on some
conﬁguration parameters, and a poor setting may signiﬁcantly
hinder their efﬁcacy [27]. Hence, learning-based schemes have
become an alternative, beneﬁting from the latest breakthroughs
in machine learning (ML) such as deep reinforcement learning
(DRL), and supervised and imitation learning techniques [5].
Learning-basedschemesattaingoodstrategieswithoutrequiring
any presumptions about the environment.
Nonetheless, learning-based schemes are exposed to two
major limitations. First, their performance heavily depends on
the training data. Network environments can be quite diverse,
and their dynamics change over time. Therefore, future states
are not easy to predict accurately. Most schemes use classical
approaches to train an agent by giving feedback for decisions
while interacting with an environment. Such interaction can be
efﬁcientlyperformedinacontrolledtrace-drivensimulator. Still,
a mismatch may occur when the trained model is deployed in
a live system and encounters an environment not previously
seen [55]. As a result, the scheme may fail to perform proper
rate adaptation. Second, deploying learning-based schemes on
devices with scarce resources is impractical due to high storage
and computational costs. Prior work [55] showed that a learning
model trained on past network scenarios could hardly provide
a comparable performance under new conditions, and hence,
effective and continual model retraining/update was required.
```

## 4. Metadatos PDF detectados

```json
{
  "format": "PDF 1.4",
  "title": "Bitrate Adaptation and Guidance With Meta Reinforcement Learning",
  "author": "",
  "subject": "IEEE Transactions on Mobile Computing;2024;23;11;10.1109/TMC.2024.3376560",
  "keywords": "",
  "creator": "LaTeX with hyperref package",
  "producer": "Acrobat Distiller 11.0 (Windows); modified using iText® Core 7.2.4 (AGPL version) ©2000-2022 iText Group NV",
  "creationDate": "D:20240905114618+05'30'",
  "modDate": "D:20241002162808-04'00'",
  "trapped": "",
  "encryption": null
}
```

## 5. Mapa de secciones detectado

- p. 1: I. INTRODUCTION
- p. 2: II. RELATED WORK
- p. 3: III. Ahaggar BITRATE GUIDANCE
- p. 3: A. Formulation of the Problem
- p. 7: C. Ahaggar Meta-Testing (Online)
- p. 7: IV. Ahaggar DESIGN CHOICES
- p. 8: C. Number of Shots and Learning Episodes
- p. 8: MODEL CONVERGENCE/GENERALIZATION FOR DIFFERENT SOLUTIONS TIME
- p. 8: D. Ahaggar Model Convergence
- p. 9: V. PERFORMANCE EVALUATION
- p. 9: A. Ahaggar Implementation
- p. 9: B. Methodology and Evaluation Setup
- p. 10: TABLE III
- p. 10: AVERAGE RESULTS OF THE QOE AND ITS METRICS FOR DIFFERENT NETWORK TRACES FOR SCENARIO A1
- p. 10: C. Results for Multiple Identical Clients (Scenario A1)
- p. 11: RUNNING ON DEVICES WITH DIFFERENT RESOLUTIONS FOR SCENARIO B1
- p. 11: D. Results for Multiple Mixed-Device Clients (Scenario B1)
- p. 12: AVERAGE RESULTS OF THE QOE AND ITS METRICS FOR DIFFERENT NETWORK TRACES FOR SCENARIO A2
- p. 12: E. Results for Multiple Identical Clients With Shared Network
- p. 13: F. Results for Multiple Mixed-Device Clients With Shared
- p. 13: G. Results for Multiple Mixed-ABR Clients (Scenario C)
- p. 13: RUNNING ON DEVICES WITH DIFFERENT RESOLUTIONS FOR SCENARIO B2
- p. 13: TABLE VII
- p. 13: CLIENTS UNDER DIFFERENT NETWORK TRACES FOR SCENARIO C
- p. 14: VI. CONCLUSION
- p. 14: REFERENCES

## 6. Figuras, tablas, algoritmos y ecuaciones detectadas

- p. 3: Fig. 1.
- p. 4: Fig. 2.
- p. 6: Algorithm 1: Ahaggar DPPO (Central Agent; Chief).
- p. 6: Algorithm 2: Ahaggar DPPO (Workers).
- p. 7: Fig. 3.
- p. 8: Fig. 4.
- p. 8: Fig. 5. We observe that Ahaggar with X = 100 converges
- p. 8: Fig. 5.
- p. 8: TABLE I
- p. 9: TABLE II
- p. 9: Table II.
- p. 10: TABLE III
- p. 10: Table III shows the total QoE and detailed breakdown of each
- p. 11: Fig. 6.
- p. 11: TABLE IV
- p. 12: TABLE V
- p. 12: Fig. 7(a)–(c) where Ahaggar is placed much further ahead
- p. 13: Fig. 7.
- p. 13: TABLE VI
- p. 13: TABLE VII
- p. 3: Fig. 2,
- p. 5: Fig. 1. For each episode, an agent c updates its gradient policy
- p. 6: Fig. 1). Each agent is
- p. 6: Algorithm 1 for the chief and Algorithm 2 for the workers.
- p. 7: Fig. 2), which
- p. 7: Fig. 3. We can see that DPPO achieves the best
- p. 8: Fig. 4. With 3,000 episodes, we observe that MAML out-
- p. 10: Fig. 6 and Table III conﬁrm this. For instance,
- p. 11: Fig. 6). In
- p. 11: Fig. 6(a): 22.28% (44.73%),
- p. 11: Fig. 6(b): 49.49% (37.06%), NYU LTE Fig.
- p. 11: Fig. 6(d): 8.01% (31.10%)]
- p. 12: Fig. 7, we can also see that Ahaggar achieved the
- p. 12: Fig. 7(a): 109.80%
- p. 12: Fig. 7(b): 74.30% (90.16%), NYU
- p. 12: Fig. 7(c): 104.20% (114.14%), Lumous 5G Fig. 7(d):
- p. 12: Fig.7(a):93.58%(95.40%),Belgium
- p. 12: Fig. 7(b): 87.08% (98.74%), NYU LTE Fig. 7(c):
- p. 12: Fig. 7(d): 1.57% (20.96%)],

## 7. Lineas con posible contenido matematico/formal

- p. 1: `resolutions on QoE with Ahaggar. We thoroughly investigate these`
- p. 1: `logic to improve the quality of experience (QoE). Incorporating`
- p. 1: `harmoniously to deliver s better QoE? ❷How to implement`
- p. 2: `Policy Optimization (DPPO) [25] with clip and Adam optimizer`
- p. 2: `for policy updates at each time interval. Considering the changes`
- p. 2: `(MAML) [23] on-policy gradient-based meta-RL approach that`
- p. 2: `embeds policy gradient steps into the meta optimization. This al-`
- p. 2: `is the ﬁrst study using meta-RL to improve QoE for adaptive`
- p. 2: `meta-policy, adjusting the parameter weights that determine the`
- p. 2: `viewer QoE by up to 87.0%, reduces rebuffering duration by up`
- p. 2: `gar QoE enhancement.`
- p. 2: `why we used DPPO and MAML as the policy update`
- p. 2: `shows the existing solutions for QoE optimization. Section III`
- p. 2: `maximizing the viewer QoE. Bentaleb et al. [10] designed AMP`
- p. 2: `for intelligent QoE optimization decisions (e.g., [13]).`
- p. 3: `decision making. These solutions collect QoE metrics from`
- p. 3: `t (π), ∀c ∈[1, . . . , N], ∀t ∈[1, . . . , k]`
- p. 3: `t (π) ≤mtpc`
- p. 3: `t (π) ≤BWtotal`
- p. 3: `Further in this formulation, π is an RL policy that decides the`
- p. 3: `POMDP model consists of 11-tuples POMDP = (S, A, O, R,`
- p. 3: `r S = {S1, . . . , SN} is the set of the ﬁnite and discrete agent`
- p. 3: `agent states as Sc = {sc`
- p. 3: `k}, where k = |Zc| is the`
- p. 3: `r A = {A1, . . . , AN} is the ﬁnite and discrete set of actions`
- p. 3: `actions as Ac = {ac`
- p. 3: `r O = {O1, . . . , ON} is the ﬁnite set of observation states`
- p. 3: `observations is Oc = {oc`
- p. 3: `r R = {R1, . . . , RN} is the set of expected immediate re-`
- p. 3: `agents. For each client c, the set of rewards is Rc =`
- p. 3: `r P = S × S × A →[0, 1] is the state transition probability`
- p. 3: `r U = O × S × A →[0, 1] is the observation probability`
- p. 3: `r Z = {Z1, . . . , ZN} represents the bitrate guidance prob-`
- p. 3: `lem maxπ QoEc`
- p. 3: `t (π) for every agent c. The set of bi-`
- p. 3: `trate guidance tasks for agent c is thus deﬁned as Zc =`
- p. 3: `r C = {1, . . . , N} is the set of N agents, where N is the total`
- p. 4: `At each time t = [1, . . . , k], each agent c does not track the`
- p. 4: `as Hc = {hc`
- p. 4: `t = {(ac`
- p. 4: `the set of histories of N agents as H = {H1, . . . , HN}. Yet, hc`
- p. 4: `t = O(oc`
- p. 4: `t, Bc = {bc`
- p. 4: `k} and B = {B1, . . . , BN} are the set`
- p. 4: `agent c strives to ﬁnd the effective optimal policy πc,⋆to solve`
- p. 4: `accumulated discounted reward (denoted by Gc`
- p. 4: `and Adam optimizer for policy (π) updates at every time in-`
- p. 4: `environments, it uses MAML—the meta-RL policy gradient`
- p. 4: `round-trip time (RTT; ms) and packet loss (%).`
- p. 4: `(ii) input state, action and reward spaces, (iii) NN architecture`
- p. 4: `with policy update and meta-RL approaches, (iv) headless video`
- p. 4: `The Ahaggar uses an A2C NN. Without loss of generality`
- p. 4: `states. The solution of the POMDP is a policy prescribing which`
- p. 4: `t ) while it receives a reward rc`
- p. 4: `c aims to ﬁnd the optimal policy πc,⋆: S →O →B →A that`
- p. 4: `maps states-to-actions and maximizes the reward.`
- p. 4: `t = {mtpc`
- p. 5: `each time epoch t, the Ahaggar policy πc,⋆of agent c maps bc`
- p. 5: `ated probabilities. πc,⋆: bc`
- p. 5: `the value function V c,π(bc`
- p. 5: `convolution with feature number (=64) and kernel size (=1)`
- p. 5: `FC layers with feature number (=64) and a Rectiﬁed Linear`
- p. 5: `▷Reward Function. At each time epoch t, the reward rc`
- p. 5: `so, we adopt a well-know state-of-the-art reward function [11],`
- p. 5: `t = ω1 × qc`
- p. 5: `and ωi are the coefﬁcients of the reward function. Herein,`
- p. 5: `of 20 in VMAF values of two consecutive segments. This QoE`
- p. 5: `that ω1 = 0.077, ω2 = 1.249, ω3 = 2.877, ω4 = 0.049, and`
- p. 5: `ω5 = 1.436 achieve the best trade-off between the ﬁve QoE`
- p. 5: `▷Policy Gradient and Training Algorithm. The essential`
- p. 5: `objective of Ahaggar is to improve the policy via boosting`
- p. 5: `the probabilities of high-reward samples from the collected`
- p. 5: `to the bitrate for the next segment using the improved policy`
- p. 5: `π : πc,⋆`
- p. 5: `accumulated discounted reward that is expressed as`
- p. 5: `t = arg max`
- p. 5: `θ denotes the batch size for updating the gradient policy πc`
- p. 5: `γ ∈[0, 1] is the discount factor, θ is the policy parameter, and`
- p. 5: `in Fig. 1. For each episode, an agent c updates its gradient policy`
- p. 5: `t is maximized with respect to the policy parameters`
- p. 5: `t) ▽log πc`
- p. 5: `where Θ is the total number of episodes, Aπc`
- p. 5: `cumulative reward after deterministically selecting the action ac`
- p. 5: `t, compared with the expected reward for action drawn`
- p. 5: `from policy πc`
- p. 5: `t.Priorwork[54]foundthatAπc`
- p. 5: `of length κ such that Aπc`
- p. 5: `t) = Qπc`
- p. 5: `t) −V πc`
- p. 5: `Temporal Difference (TD) approach given by: Qπc`
- p. 5: `dropouts with probability (p = 0.5) to add a regularization term`
- p. 5: `the entropy E = H(πc`
- p. 5: `decisions. Therefore, the parameter θπc of the actor is updated`
- p. 6: `θπc ←θπc + α`
- p. 6: `t) ▽θ log πc`
- p. 6: `we have to estimate the value function V πc`
- p. 6: `method to compute the loss function and minimize its value.`
- p. 6: `t + γV πc`
- p. 6: `t+1; θvc) −V πc`
- p. 6: `where ¯α is the learning rate for the critic, V πc`
- p. 6: `Finally, we update the policy πθ periodically every κ-steps`
- p. 6: `Adam optimizer. The constraint represents how much the policy`
- p. 6: `(KL) divergence (KL[πc`
- p. 6: `as: θκ+1 = arg maxθ LKLP EN`
- p. 6: `−¯βKL[πc`
- p. 6: `E is the empirical expectation over time steps, ratiot(θ) (=`
- p. 6: `desired changes in the policy per time episode. The scaling term`
- p. 6: `Wait until N gradient parameters for actor (θπ) and`
- p. 6: `Average gradients and update global θπ and θv`
- p. 6: `Update all the workers with global θπ and θv`
- p. 6: `while not done (for every t = [1, . . . , Tπc`
- p. 6: `Run policy πc`
- p. 6: `Estimate discounted expected reward Gc`
- p. 6: `θold ←πc`
- p. 6: `if KL[πc`
- p. 6: `Send gradient actor parameters (θπc) to chief`
- p. 6: `else if KL[πc`
- p. 6: `if the actual change in the policy stays signiﬁcantly below or`
- p. 6: `D = {(bc`
- p. 6: `current policy πc`
- p. 7: `κ of policy gradient updates on the data from an environment`
- p. 7: `κ = θ −α ▽θ LDP P O`
- p. 7: `loss on the environment Evti after κ-step of updates.`
- p. 7: `policy πc`
- p. 7: `loss functions and the outer loop’s learning rate β. Formally, we`
- p. 7: `deﬁne a meta-objective (Lmeta(θ)) as Tπc`
- p. 7: `t=1 LSGD`
- p. 7: `θ = θ −β ▽θ`
- p. 7: `Evti denotes the loss on the environment Evti.`
- p. 7: `In Ahaggar, we used DPPO [25] as a policy update tech-`
- p. 7: `compared to popular vanilla DRL-based policy update tech-`
- p. 7: `(A3C), trust region policy optimization (TRPO), deep deter-`
- p. 7: `ministic policy gradient (DDPG), soft actor-critic (SAC), twin`
- p. 7: `r A3C is an on-policy algorithm that extends actor-critic to`
- p. 7: `r TRPO is an on-policy algorithm that updates policies by`
- p. 7: `r DDPG is an off-policy algorithm that combines DQN and`
- p. 7: `actor-critic algorithms to use deterministic policy gradients`
- p. 7: `for updating the policy via a DL approach.`
- p. 7: `r SAC is an off-policy algorithm that combines stochastic`
- p. 7: `policy optimization and DDPG-style approaches. It incor-`
- p. 7: `r TD3 is an off-policy algorithm that introduces clipped dou-`
- p. 7: `ble Q-learning mode and a delayed policy update strategy`
- p. 7: `other policy update techniques, we prepared 10% as a validation`
- p. 7: `performance with (i) the highest possible N-QoElin (reward;`
- p. 7: `highest reward value with only 3,000 episodes, compared to its`
- p. 7: `function (7) to remove incentives for the new policy to get far`
- p. 7: `from the old policy. Hence, it allows robust policy optimization`
- p. 7: `reward, but it takes more time (6,000 episodes) to converge to`
- p. 7: `the best achievable reward. With this result, we ﬁnd DPPO is the`
- p. 7: `best ﬁt for Ahaggar out of existing policy update techniques.`
- p. 7: `r PEARL uses the SAC policy for meta-training and adapts`
- p. 7: `context variable on which the policy is conditioned.`
- p. 7: `vanilla off-policy RL algorithm.`
- p. 8: `coupled with a new off-policy learning algorithm termed`
- p. 8: `V-trace. V-trace is a general off-policy learning algorithm`
- p. 8: `more stable and robust than other off-policy techniques for`
- p. 8: `It also converges quickly to the best reward, requiring 3,000`
- p. 8: `X = {1, 20, 40, 60, 80, 100}. We used the same validation set`
- p. 8: `Fig. 5. We observe that Ahaggar with X = 100 converges`
- p. 8: `compared to X = 80, X = 60 and X = 40, respectively. One`
- p. 8: `interesting observation is that Ahaggar with X = 40 (40-`
- p. 8: `and meta-testing phases compared to X = 100, X = 80, or`
- p. 8: `X = 60. Therefore, we set X=40 during the meta-training and`
- p. 8: `X = 1 or X = 20, the convergence was very slow (requiring`
- p. 9: `used the mb = l (maximum suggested bitrate) CMSD-Dynamic`
- p. 9: `with our datasets and QoE metrics to ﬁt each experiment.`
- p. 9: `two main QoE models: Linear QoE [50] and ITU P.1203 QoE`
- p. 9: `the QoE, we used a normalized QoElin (N-QoElin) with values`
- p. 9: `QoE (QoE⋆) in each session such that N-QoElin = QoElin /`
- p. 9: `QoE⋆. The ITU P.1203 QoE model in Mode 0 (O.46) takes four`
- p. 9: `in [44]. This model outputs QoE values in the range of one to`
- p. 10: `AVERAGE RESULTS OF THE QOE AND ITS METRICS FOR DIFFERENT NETWORK TRACES FOR SCENARIO A1`
- p. 10: `Table III shows the total QoE and detailed breakdown of each`
- p. 10: `QoE metric for each ABR scheme for various network traces.`
- p. 11: `Avg. QoE itu (O.46) and avg. rebuffering duration ratio in various`
- p. 11: `detail, Ahaggar achieved the highest average QoE with an`
- p. 11: `in terms of the QoE and rebuffering duration. This is because`
- p. 11: `RobustMPC, suffered from low QoE and long RD due to wrong`
- p. 11: `AVERAGE QOE itu (O.46) SCORES AND ITS METRICS PRODUCED BY Ahaggar`
- p. 12: `AVERAGE RESULTS OF THE QOE AND ITS METRICS FOR DIFFERENT NETWORK TRACES FOR SCENARIO A2`
- p. 12: `clients). Table V shows the total QoE and detailed breakdown`
- p. 12: `of each QoE metric for each ABR scheme for various network`
- p. 13: `AVERAGE RESULTS OF QOE itu (O.46) AND VMAF PRODUCED BY DYNAMIC`
- p. 14: `ing QoE of HTTP adaptive streaming using software deﬁned network-`
- p. 14: `“CFA: A practical prediction system for video QoE optimization,”`
- p. 15: `power, and QoE implications,” in Proc. ACM SIGCOMM Conf., 2021,`
- p. 15: `[44] W. Robitza et al., “HTTP adaptive streaming QoE estimation with ITU-T`

## 8. Extraccion tecnica cruda por categorias


### 8.1. modelo algoritmo arquitectura

Palabras clave usadas: `model, algorithm, architecture, framework, policy, neural, network, deep reinforcement, reinforcement learning, DRL, DQN, PPO, A2C, A3C, actor, critic, agent, meta, meta-learning, MAML, offline reinforcement, curriculum, VAE, variational autoencoder, LSTM, BiLSTM, GRU, CNN, predictor, bandwidth prediction, Plume, Gelato, Ahaggar, CausalSim, IMDP, domain-specific prior`

**Fragmento 1 - p. 2 - score 12:**

Ahaggar models bitrate guidance tasks for multiple clients as a partially ob- servable Markov decision process (POMDP) and leverages the latest developments in DRL to dynamically adapt to the varying network conditions. Speciﬁcally, it uses advantage Actor-Critic networks (A2C) for model training and Distributed Proximal Policy Optimization (DPPO) [25] with clip and Adam optimizer for policy updates at each time interval. Considering the changes in the environment, we adopt a Model Agnostic Meta-Learning (MAML) [23] on-policy gradient-based meta-RL approach that embeds policy gradient steps into the meta optimization. This al- lows Ahaggar to update the model parameters to achieve good generalization performance on unseen environments during the inference.

**Fragmento 2 - p. 8 - score 10:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10385 Fig. 4. MAML versus others. r REPTILE works by repeatedly sampling an environment, performing stochastic gradient descent on it, and updating the initial parameters towards the ﬁnal parameters learned on that environment. r ANIL is a simpliﬁed version of MAML that removes the inner-loop updates for all but the head (ﬁnal layer) of a neural network during training and inference. r IMPALA introduces a highly scalable distributed agent coupled with a new off-policy learning algorithm termed V-trace. V-trace is a general off-policy learning algorithm more stable and robust than other off-policy techniques for actor-critic agents.

**Fragmento 3 - p. 7 - score 9:**

With this result, we ﬁnd DPPO is the best ﬁt for Ahaggar out of existing policy update techniques. B. Why MAML? We compare the performance of Ahaggar with MAML against Ahaggar with different well-known meta-RL ap- proaches [26]: PEARL, RL2, REPTILE, ANIL, and IMPALA. r PEARL uses the SAC policy for meta-training and adapts to new environments by performing inference over a latent context variable on which the policy is conditioned. r RL2 tries to structure the RL agent as a recurrent neural network(RNN),whichreceivesobservations,pastrewards, and actions, and retains its state across episodes in a given environment. Particularly, RL2 is encoded inside the weights of an RNN, which are learned slowly through a vanilla off-policy RL algorithm.

**Fragmento 4 - p. 4 - score 8:**

These belief states are a sufﬁcient measure of histories and given a belief state bc t, an agent c strives to ﬁnd the effective optimal policy πc,⋆to solve (1) by ﬁnding the best bitrate for each client that maximizes the accumulated discounted reward (denoted by Gc t and deﬁned in Section III-B). The Ahaggar learning model solves the POMDP problem (1) using a multi-agent A2C [6] NN with clipped DPPO [25] and Adam optimizer for policy (π) updates at every time in- terval. For continual learning and quickly adapting to unseen environments, it uses MAML—the meta-RL policy gradient approach—allowing Ahaggar to learn hyper-parameter ini- tialization and speed up the optimization of the learned model during inference.

**Fragmento 5 - p. 6 - score 8:**

Here, the N agents continually send their parameters θ to a central agent (termed the chief), which aggregates them to generate a single Ahaggar model. For each sequence of parameters θ that it receives, the chief uses the A2C algorithm to compute a gradient based on (5) and (6). Then, the chief updates the A2C networks and pushes out the new model to the agent that sent the parameters. Such an update process can happen synchronously or asynchronously among all agents, but we foundthataveraginggradientsandapplyingthemsynchronously leads to better results in the meta-testing phase. The pseudocode for the DPPO used by Ahaggar is provided in Algorithm 1 for the chief and Algorithm 2 for the workers.

**Fragmento 6 - p. 6 - score 8:**

▷Meta-Learned Policies for Training Algorithm. We adopt the MAML approach, which allows learning model parameters θ via meta-RL, i.e., ﬁnding the model parameters sensitive to changes in the environment, allowing the Ahaggar model to achieve fast adaptation to unseen environments during the inference phase. The training algorithm consists of two loops: (1) Inner Loop. For each episode, each agent c ﬁrst randomly picks a speciﬁc network and content trace as the environment, and sample X ∈D trajectories (also referred to as shots) where D = {(bc 1, ac 1); . . . ; (bc k, ac k)} denotes the set of sampled tra- jectories for inner loop in that environment according to the current policy πc θ.

**Fragmento 7 - p. 7 - score 8:**

r DDPG is an off-policy algorithm that combines DQN and actor-critic algorithms to use deterministic policy gradients for updating the policy via a DL approach. r SAC is an off-policy algorithm that combines stochastic policy optimization and DDPG-style approaches. It incor- porates the clipped double-Q trick and entropy regulariza- tion. r TD3 is an off-policy algorithm that introduces clipped dou- ble Q-learning mode and a delayed policy update strategy to solve the overestimation problem of DDPG. r Random is an algorithm that chooses an action randomly. To compare the performance of Ahaggar with DPPO against other policy update techniques, we prepared 10% as a validation set from the 20% of the testing set comprising network and video content traces.

**Fragmento 8 - p. 2 - score 7:**

3) We explored the design choices of Ahaggar, including why we used DPPO and MAML as the policy update solution and the meta-RL algorithm, respectively. We also examined the effects of the number of shots, the learning episode and the Ahaggar model convergence. The rest of the paper is organized as follows. Section II shows the existing solutions for QoE optimization. Section III describes the Ahaggar solution, followed by its design choices in Section IV. The performance evaluation in Sections V and VI concludes the paper. II. RELATED WORK Client-Driven Heuristic-Based ABR: These schemes use heuristics based on estimated throughput (e.g., PANDA [31]), buffer level (e.g., BOLA [47]), segment size (e.g., SARA [8]), or a combination (e.g., MPCDASH [53]).

**Fragmento 9 - p. 5 - score 7:**

The Ahaggar critic model outputs a single scalar indicating the value function V c,π(bc t) for the current state. ▷NN Architecture. The Ahaggar A2C NN architecture consists of two networks: actor and critic. Each network uses two 1DConv layers and six linear fully-connected (FC) layers to extract the set of features. Each 1DConv layer consists of 3x3 convolution with feature number (=64) and kernel size (=1) to feed the features −−→ LSc t and −−→ QT c t . Other inputs are fed into FC layers with feature number (=64) and a Rectiﬁed Linear Unit (ReLU()) activation function. Then, all input layers are concatenated and ﬁnally fed into an FC layer with 64 neurons and a slope of 0.5 to down-sample the concatenated features.

**Fragmento 10 - p. 6 - score 7:**

In these algorithms, the hyperparameter KLtarget represents the desired changes in the policy per time episode. The scaling term ˜α controls the adjustment of the KL-regularization coefﬁcient Algorithm 1: Ahaggar DPPO (Central Agent; Chief). 1: for Each agent c ∈{1, . . . , N} do 2: while not done do 3: Wait until N gradient parameters for actor (θπ) and critic (θv) are available 4: Average gradients and update global θπ and θv 5: Update all the workers with global θπ and θv 6: end while 7: end for Algorithm 2: Ahaggar DPPO (Workers). 1: for Each agent c ∈{1, . . . , N} do 2: while not done (for every t = [1, . . . , Tπc θ]) do 3: for Each κ ∈{0, . . . , Θ −1} do 4: Run policy πc θκ and collects {bc t, ac t, rc t} 5: Estimate discounted expected reward Gc t 6: Estimate advantages A πc θκ t 7: Store partial trajectory information 8: end for 9: πc θold ←πc θ 10: Compute LKLP EN θκ (θ) using (7) 11: if KL[πc θold|πc θ] > 4KLtarget then 12: Break and continue with next time epoch t + 1 13: end if 14: Compute ▽θLKLP EN θκ 15: Send gradient actor parameters (θπc) to chief 16: Send gradient critic parameters (θvc) to chief 17: Wait until parameters are accepted or dropped 18: Update parameters of worker c 19: if KL[πc θold|πc θ] > ¯βhighKLtarget then 20: ¯β ←˜α¯β 21: else if KL[πc θold|πc θ] < ¯βlowKLtarget then 22: ¯β ←¯β/˜α 23: end if 24: end while 25: end for if the actual change in the policy stays signiﬁcantly below or above the target KL, i.e., it falls outside the interval [¯βlow × KLtarget, ¯βhigh × KLtarget].

**Fragmento 11 - p. 7 - score 7:**

Here, we show the central insight of selecting DPPO compared to popular vanilla DRL-based policy update tech- niques [6], [21] such as asynchronous advantage actor-critic (A3C), trust region policy optimization (TRPO), deep deter- ministic policy gradient (DDPG), soft actor-critic (SAC), twin delayed DDPG (TD3) and Random. r A3C is an on-policy algorithm that extends actor-critic to asynchronous and parallel learning, disturbs the correlation between data, and improves training speed. r TRPO is an on-policy algorithm that updates policies by taking the largest step possible to improve performance Fig. 3. DPPO versus others. while satisfying a KL-Divergence constraint on how close the new and old policies are allowed to be.

**Fragmento 12 - p. 2 - score 6:**

Therefore, our model can converge quickly to the best performance and adapt to new unseen environments with only a small number of (e.g., 40) shots. To our knowledge, this paper is the ﬁrst study using meta-RL to improve QoE for adaptive streaming clients while cleanly separating the responsibilities for the servers and clients and respecting the client-driven nature of HAS. The Ahaggar solution comprises two phases: (i) (ofﬂine) meta-training, where each RL agent trains the Ahaggar meta- model on heterogeneous network environments, and (ii) (online) meta-testing (also called inference), where each agent contin- ually learns the system dynamics and rapidly optimizes the meta-policy, adjusting the parameter weights that determine the agent behavior according to the trajectories collected from both the meta-training and meta-testing.

**Fragmento 13 - p. 3 - score 6:**

Inparticular,weuseacentralizedtraining with decentralized execution (CTDE) paradigm [56] to train the MARL agents. CTDE allows these agents to train decentralized policies with global information during training and to make decisions based on the individually learned policies during inference. We also use MAML [23], the meta-RL algorithm, to adapt to various network environments through parameter learning. The overall workﬂow of Ahaggar is shown in Fig. 2, where the steps are numbered as 1⃝– 8⃝. A. Formulation of the Problem At each segment download time epoch t, Ahaggar performs the bitrate guidance tasks (denoted by Z) by selecting the best bitrate (denoted by lc t) with respect to the current state (denoted by sc t) of each client c.

**Fragmento 14 - p. 5 - score 6:**

DPPO allows Ahaggar to run multi-agents (or workers), where each agent has its own A2C network and data collection. Thus, the gradient calculations are distributed over workers, as shown in Fig. 1. For each episode, an agent c updates its gradient policy such that Gc t is maximized with respect to the policy parameters θ, as follows: ▽¯Gc t = 1 Θ Θ  θ=1 Tπc θ  t=1 A πc θ t (bc t, ac t) ▽log πc θ(ac t, sc t), (4) where Θ is the total number of episodes, Aπc θ(bc t, ac t) is the advantage function that represents the difference in the expected cumulative reward after deterministically selecting the action ac t in state bc t, compared with the expected reward for action drawn from policy πc θ.

**Fragmento 15 - p. 2 - score 5:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10379 bitrate guidance with perceptual quality and device resolution awareness? ❸How to achieve continual learning for the server- side bitrate guidance? We answer the questions above in the context of Ahaggar,1 a meta reinforcement learning (meta-RL)-based solution. Ahag- gar has a server-side learning model that takes network condi- tions, clients’ statuses, device resolutions and streamed content as input features, and then provides quality and resolution-aware bitrate guidance to the streaming clients. Leveraging the server’s vastcomputationalpower,storagecapacityandmemory,Ahag- gar enables model inference for performing bitrate guidance tasks and helps resource-constrained streaming clients run their lightweight heuristic-based ABR schemes.

**Fragmento 16 - p. 4 - score 5:**

To cover a wide range of device resolu- tions, each source video was encoded at {0.24, 0.37, 0.57, 0.75, 1.0, 1.76, 2.36, 3.0, 4.3, 5.7, 8.0, 11, 16.6}Mbps at a resolution of {180, 216, 288, 288, 360, 540, 720, 720, 1080, 1080, 1440, 2160, 2160}p, respectively. Each trace is comprised of video segments with their corresponding encoded bitrates (Mbps), sizes (bytes) and VMAF scores for three device resolutions (phone, HDTV and UHDTV). We performed customized modiﬁcations on the Park simula- tor [34] to fully comply with the Ahaggar design. Speciﬁcally, we revised (i) the problem space using POMDP instead of MDP, (ii) input state, action and reward spaces, (iii) NN architecture with policy update and meta-RL approaches, (iv) headless video client by introducing three device resolutions, and (v) MARL with CTDE and shared environment support.

**Fragmento 17 - p. 4 - score 5:**

B. Ahaggar Meta-Training (Ofﬂine) To train the Ahaggar meta-model, we use Park [34]—a Python-based segment-level simulator that is based on OpenAI and state-of-the-art ABR simulators [46] for RL-based model training. This simulator faithfully emulates a streaming session where the learning agent uses a large corpus of real-world net- work and content traces to explore the streaming environment. ▷Network Traces. We used the Belgium 4G/LTE [51], Nor- way 4G/LTE [43], NYU LTE [36] and Lumous 4G/5G [39] datasets. Each trace entry consists of a throughput value (Mbps), round-trip time (RTT; ms) and packet loss (%). ▷Content Traces. We used the Comyco [27] and Waterloo SQoE-IV [22] datasets.

**Fragmento 18 - p. 5 - score 5:**

These results are similar to [50]. ▷Policy Gradient and Training Algorithm. The essential objective of Ahaggar is to improve the policy via boosting the probabilities of high-reward samples from the collected trajectories and declining the possibilities of failure samples from the bad trajectories. For every time epoch t, each RL agent c of Ahaggar selects the action ac t that corresponds to the bitrate for the next segment using the improved policy π : πc,⋆ θ (bc t, ac t) →[0, 1] at state bc t, which results in the best accumulated discounted reward that is expressed as Gc t = Tπc θ  ¯t=t γ¯t−t × rc t, ac t = arg max a E [Gc t(bc t, a)] , (3) where Gc t is computed from time t to the end of training, Tπc θ denotes the batch size for updating the gradient policy πc θ, γ ∈[0, 1] is the discount factor, θ is the policy parameter, and πc,⋆ θ (bc t, ac t) is the probability that action ac t is taken in state bc t.

**Fragmento 19 - p. 5 - score 5:**

▷Action Space. The action space A is deﬁned as the available bitrate levels (i.e., n-dimensional vector) for a given video. In each time epoch t, the Ahaggar policy πc,⋆of agent c maps bc t to compact discrete action space A and select ac,⋆ t ∈A. ▷Observation Space. We expose a subset of Ahaggar states as the observations, where the agent c observes oc t = {mtpc t, qtc t, blc t, lsc t, dtc t, rsc t, −−→ LSc t , −−→ QT c t } for each time epoch t. ▷Output. The Ahaggar actor model returns 1×n- dimensional vector representing bitrate levels with their associ- ated probabilities. πc,⋆: bc t →ac,⋆ t maps the state bc t to the best action ac,⋆ t based on the state-action probabilities, where ac,⋆ t with the highest probability is selected under the current state.

**Fragmento 20 - p. 5 - score 5:**

The actor and critic use the same structure but with different outputs. For both networks, we use the Softmax activation function (Softmax()) with the L2-norm of networks as the last FC layer, resulting in an output range from 0 to 1. ▷Reward Function. At each time epoch t, the reward rc t of an agent c is calculated after each action ac t is taken to ensure that Ahaggar can learn from past experience. To do so, we adopt a well-know state-of-the-art reward function [11], [27], [35], [50], [53] that linearly combines ﬁve metrics (2): perceptual quality (qc t(lc t)), rebuffering duration (rdc t) and count (rcc t), quality oscillations (qoc t) and switches (qsc t).

**Fragmento 21 - p. 6 - score 5:**

To do so, the critic network uses the standard TD method to compute the loss function and minimize its value. The parameter θvc of the critic network is updated through a stochastic gradient descent (SGD) algorithm using (6). θvc ←θvc −¯α Tθ  t=1 ▽θ(rc t + γV πc θ(bc t+1; θvc) −V πc θ(bc t; θvc))2, (6) where ¯α is the learning rate for the critic, V πc θ(bc t; θvc) and V πc θ(bc t+1, θvc) are the objective assessments for bc t and bc t+1, respectively, from the critic network. Finally, we update the policy πθ periodically every κ-steps using PPO with constrained clipped objective (CCO) and the Adam optimizer. The constraint represents how much the policy is allowed to change, expressed in terms of the Kullback-Leibler (KL) divergence (KL[πc θold|πc θ]).

**Fragmento 22 - p. 6 - score 5:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10383 via a stochastic gradient ascent using (5). θπc ←θπc + α Tθ  t=1 A πc θ t (bc t, ac t) ▽θ log πc θ(ac t, bc t) + β E, (5) where Tθ is the update interval, α is the learning rate and β is the entropy parameter that is set to a large value at the beginning of the training to encourage exploration and decreases over time to emphasize improving rewards. To calculate the advantage A(bc t, ac t) for a given experience, we have to estimate the value function V πc θ(b). This estimation is performed by the critic network that makes an objective assessment for all the states ∀bc t ∈B of an agent c during the training.


### 8.2. estado inputs features

Palabras clave usadas: `state, input, feature, observation, throughput, bandwidth, buffer, download time, chunk size, history, past, remaining, TCP, RTT, CWND, device, resolution, content, CMCD, CMSD, network condition, environment, latent, context, trace features`

**Fragmento 1 - p. 5 - score 9:**

10382 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024 dtc t, rsc t, −−→ LSc t , −−→ QT c t }, comprised of network, content and play- back features of the last downloaded segment. These inputs are measured throughput mtpc t (Kbps), VMAF quality qtc t (0–100), current playback buffer length blc t (second), segment size lsc t (KB), download time dtc t (second), percentage of the remaining segments in the video rsc t (%), vector of m available sizes for the next segment −−→ LSc t (KB) and vector of m available VMAF qualities for the next segment −−→ QT c t (0–100). Instead of feeding the A2C NN the exact values of the input state, we normalize them to enable the agent to generalize the strategy better in an unseen network environment [3].

**Fragmento 2 - p. 1 - score 8:**

To make the most out of both worlds, we earlier developed Ahaggar, a learning-based scheme executing on the server side that provides quality-aware bitrate guidance to streaming clients running their own heuristics. Ahaggar’s novelty is the meta reinforcement learning approach taking network condi- tions, clients’ statuses and device resolutions, and streamed content as input features to perform bitrate guidance. Ahaggar uses the new Common Media Client/Server Data (CMCD/SD) protocols to exchange the necessary metadata between the servers and clients. While Ahaggar was a signiﬁcant step forward, in this study, we focus on three open areas, namely, (i) exploring the performance of Ahaggar in a heterogeneous environment including both Ahag- gar and non-Ahaggar clients with varied network conditions and device resolutions, and (ii) quantifying the impact of device resolutions on QoE with Ahaggar.

**Fragmento 3 - p. 2 - score 7:**

CMCD deﬁnes a set of information collected by a media client and sent along with the HTTP requests to the server running Ahaggar in query arguments or header extensions. CMSD allows the server to 1A highland region in the central Sahara in southern Algeria. convey Ahaggar bitrate guidance decisions to media clients through the HTTP response headers. We evaluate the performance of Ahaggar against several ABR solutions by running real-world trace-driven experiments. These experiments cover multiple clients with heterogeneous network conditions and device resolutions. Experimental re- sults show that Ahaggar delivers consistent quality, improves viewer QoE by up to 87.0%, reduces rebuffering duration by up to 84.4% and reduces bandwidth consumption by up to 62.6%.

**Fragmento 4 - p. 2 - score 6:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10379 bitrate guidance with perceptual quality and device resolution awareness? ❸How to achieve continual learning for the server- side bitrate guidance? We answer the questions above in the context of Ahaggar,1 a meta reinforcement learning (meta-RL)-based solution. Ahag- gar has a server-side learning model that takes network condi- tions, clients’ statuses, device resolutions and streamed content as input features, and then provides quality and resolution-aware bitrate guidance to the streaming clients. Leveraging the server’s vastcomputationalpower,storagecapacityandmemory,Ahag- gar enables model inference for performing bitrate guidance tasks and helps resource-constrained streaming clients run their lightweight heuristic-based ABR schemes.

**Fragmento 5 - p. 2 - score 6:**

We take inputs from the network, clients and streamed content into the Ahaggar neural network (NN) for bitrate guidance. The objective of Ahaggar is to select the minimum bitrate (among the available options) above which the next higher bitrate improves the perceptual quality only insigniﬁcantly at the speciﬁc device resolution. In this study, we use an objective full-reference perceptual video quality metric known as Video Multi-method Assessment Fusion (VMAF) [42]. To ensure healthy cooperation without incurring additional complexities between the clients and servers, Ahaggar adopts the emerging Common Media Client/Server Data standards: CMCD [9], [13], [18] and CMSD [7], [19], [33].

**Fragmento 6 - p. 4 - score 6:**

During the session, the simulator used the traces and each client interaction with the environment as input features to feed into the NN, from which the RL agent, in turn, decided the segment bitrates at every time step. The Ahaggar uses an A2C NN. Without loss of generality and since the agents are independent, we simplify the formu- lation in the context of a single agent. At every time epoch t, the segment-level statistics for each agent are collected and aggregated as the environment input state. Different from MDP, in POMDP, the agent cannot directly observe the complete system state, but the agent makes observations that depend on the state.

**Fragmento 7 - p. 7 - score 6:**

With this result, we ﬁnd DPPO is the best ﬁt for Ahaggar out of existing policy update techniques. B. Why MAML? We compare the performance of Ahaggar with MAML against Ahaggar with different well-known meta-RL ap- proaches [26]: PEARL, RL2, REPTILE, ANIL, and IMPALA. r PEARL uses the SAC policy for meta-training and adapts to new environments by performing inference over a latent context variable on which the policy is conditioned. r RL2 tries to structure the RL agent as a recurrent neural network(RNN),whichreceivesobservations,pastrewards, and actions, and retains its state across episodes in a given environment. Particularly, RL2 is encoded inside the weights of an RNN, which are learned slowly through a vanilla off-policy RL algorithm.

**Fragmento 8 - p. 4 - score 5:**

To cover a wide range of device resolu- tions, each source video was encoded at {0.24, 0.37, 0.57, 0.75, 1.0, 1.76, 2.36, 3.0, 4.3, 5.7, 8.0, 11, 16.6}Mbps at a resolution of {180, 216, 288, 288, 360, 540, 720, 720, 1080, 1080, 1440, 2160, 2160}p, respectively. Each trace is comprised of video segments with their corresponding encoded bitrates (Mbps), sizes (bytes) and VMAF scores for three device resolutions (phone, HDTV and UHDTV). We performed customized modiﬁcations on the Park simula- tor [34] to fully comply with the Ahaggar design. Speciﬁcally, we revised (i) the problem space using POMDP instead of MDP, (ii) input state, action and reward spaces, (iii) NN architecture with policy update and meta-RL approaches, (iv) headless video client by introducing three device resolutions, and (v) MARL with CTDE and shared environment support.

**Fragmento 9 - p. 4 - score 5:**

B. Ahaggar Meta-Training (Ofﬂine) To train the Ahaggar meta-model, we use Park [34]—a Python-based segment-level simulator that is based on OpenAI and state-of-the-art ABR simulators [46] for RL-based model training. This simulator faithfully emulates a streaming session where the learning agent uses a large corpus of real-world net- work and content traces to explore the streaming environment. ▷Network Traces. We used the Belgium 4G/LTE [51], Nor- way 4G/LTE [43], NYU LTE [36] and Lumous 4G/5G [39] datasets. Each trace entry consists of a throughput value (Mbps), round-trip time (RTT; ms) and packet loss (%). ▷Content Traces. We used the Comyco [27] and Waterloo SQoE-IV [22] datasets.

**Fragmento 10 - p. 9 - score 5:**

To simplify the presentation of the QoE, we used a normalized QoElin (N-QoElin) with values between 0 and 1. To achieve that, we used the best achievable QoE (QoE⋆) in each session such that N-QoElin = QoElin / QoE⋆. The ITU P.1203 QoE model in Mode 0 (O.46) takes four metrics as input: bitrate, rebuffering duration, frame rate and content resolution. How to compute the QoEitu is described in [44]. This model outputs QoE values in the range of one to ﬁve (MOS) and we normalized them (N-QoEitu) to [0,1]. In addition, we computed (i) the total downloaded (TD) size (in MB) metric to measure how much bandwidth was consumed during the session, (ii) percentage of the HD (pHD) segments rendered at 720p or higher, and (iii) percentage of the UHD (pUHD) segments rendered at 2160p.

**Fragmento 11 - p. 10 - score 5:**

TD column in Table III). We anticipated these results because Ahaggar makes bitrate guidance decisions based on not only the throughput, buffer level and segment sizes, but also segment quality and device resolution. It also uses MAML for continual learning and fast adaptation to unseen environments. In contrast, other ABR schemes use one or more heuristics or an NN combining these heuristics and they do not necessarily perform well in unseen environments. Fig. 6 and Table III conﬁrm this. For instance, Pensieve achieved the highest average selected bitrate and Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.

**Fragmento 12 - p. 1 - score 4:**

Therefore, future states are not easy to predict accurately. Most schemes use classical approaches to train an agent by giving feedback for decisions while interacting with an environment. Such interaction can be efﬁcientlyperformedinacontrolledtrace-drivensimulator. Still, a mismatch may occur when the trained model is deployed in a live system and encounters an environment not previously seen [55]. As a result, the scheme may fail to perform proper rate adaptation. Second, deploying learning-based schemes on devices with scarce resources is impractical due to high storage and computational costs. Prior work [55] showed that a learning model trained on past network scenarios could hardly provide a comparable performance under new conditions, and hence, effective and continual model retraining/update was required.

**Fragmento 13 - p. 2 - score 4:**

In addition, Ahaggar quickly converges to the best solution during the training process with an improvement of 5.6× in terms of the number of epochs required and 6× speedup on the training time compared to the recent RL-based solutions such as [35], [52]. This paper is an extended version of Ahaggar [14], focusing on three main areas that remain open: 1) We conducted more experimental evaluations to assess the performance of Ahaggar in more challenging scenarios, especially in a heterogeneous environment that includes both Ahaggar and non-Ahaggar clients with different network conditions and device resolutions. 2) We investigated the impact of device resolution on Ahag- gar QoE enhancement.

**Fragmento 14 - p. 3 - score 4:**

Mathematically, the bitrate guidance problem for multiple clients can be formulated as ⎧ ⎪ ⎪ ⎪ ⎪ ⎨ ⎪ ⎪ ⎪ ⎪ ⎩ ﬁnd lc,⋆ t (π), ∀c ∈[1, . . . , N], ∀t ∈[1, . . . , k] arg max π QoEc t (π) s.t. lc,⋆ t (π) ≤mtpc t C.1 N  c=1 lc,⋆ t (π) ≤BWtotal C.2 , (1) where lc,⋆ t is the best bitrate, which is the minimum among the available options above and the next higher bitrate improves the perceptual quality only insigniﬁcantly for the speciﬁc content at the speciﬁc device resolution. Here, we use 1-JND (Just No- ticeable Difference) as the threshold for being signiﬁcant [37]. Further in this formulation, π is an RL policy that decides the bitrate for each client, N is the total number of clients, BWtotal is the total server capacity and mtpc is the measured throughput by client c.

**Fragmento 15 - p. 9 - score 4:**

We (i) added new CMCD parameters (qt, dt, rs, ls, −→ QT, −→ LS) to support Ahaggar design, and (ii) used the mb = l (maximum suggested bitrate) CMSD-Dynamic parameter to convey Ahaggar’s bitrate guidance to each cor- responding client. On the server side, we used TensorFlow.js converter [45] to convert and load a pre-trained meta-model into a JavaScript Web-based application and run inference through TensorFlow.js. On the client side, we implemented a simple heuristic as our ABR scheme, which used Ahaggar bitrate guidance decisions to perform rate adaptation. To simplify input state data collection, we appended the manifest ﬁles by adding four tags: size, phone, hdtv and uhdtv.

**Fragmento 16 - p. 11 - score 4:**

It is worth mentioning that all schemes faced a few rebuffering events in Lumous 5G because sometimes the bandwidth dropped signiﬁcantly and suddenly (caused by the handoffs to 4G). This is a behavior known in 5G networks operating in higher frequencies [39]. To understand how QoEitu (Mode 0) is computed for each session, Table III (the eighth and ninth columns) highlights the scores of its essential metrics (O.23: Rebufﬁng Duration Score and O.46: Overall Score) for different ABR schemes. The score of each metric is given in the MOS range of one to ﬁve. Here, we deduce three important thrusts. First, Ahaggar outperformed the baselines, achieving the best O.23 and O.46 scores for all network traces with an average improvement of 67.55% (heuristic-based: 60.75%, learning-based: 94.75%) TABLE IV AVERAGE QOE itu (O.46) SCORES AND ITS METRICS PRODUCED BY Ahaggar RUNNING ON DEVICES WITH DIFFERENT RESOLUTIONS FOR SCENARIO B1 and 36.86% (heuristic-based: 33.70%, learning-based: 49.49%) across all network traces, respectively.

**Fragmento 17 - p. 13 - score 4:**

Similar to the results in Scenario A1, Dynamic achieved the second-best results in terms of average O.23 and O.46 scores, while Pensieve experienced multiple rebuffering events that led to the lowest average O.23 and O.46 scores, averaged across all network traces. Comparing the ﬁndings between Scenario A1 and this scenario (Scenario A2), we can see that they generally share similar observations as to the performance gains Ahaggar achieves compared to the other ABR schemes, which validates its performance in both client-side and server-side network emulation scenarios. F. Results for Multiple Mixed-Device Clients With Shared Network Trace (Scenario B2) Similar to Scenario B1, we ran two clients with each device resolution (DR) (total of six clients) to evaluate the effective- ness of Ahaggar in adapting to different DRs.

**Fragmento 18 - p. 2 - score 3:**

Client-Driven Learning-Based ABR: These schemes learn from the streaming environment by training an NN using DRL techniques [6], [17]. Mao et al. [35] proposed Pensieve, the ﬁrst learning ABR that used DRL to generate a strategy toward maximizing the viewer QoE. Bentaleb et al. [10] designed AMP that implemented a set of learning-based bandwidth predictors and model auto-selection for HAS. Similarly, Fugu [52] was proposed to leverage the hidden Markov model for accurate throughput prediction. Huang et al. [27] used imitation learning to propose Comyco as ABR for on-demand videos. Server-Driven Solutions: These solutions implement a rate control on the server to control a client’s ABR decisions im- plicitly or explicitly.

**Fragmento 19 - p. 3 - score 3:**

Inparticular,weuseacentralizedtraining with decentralized execution (CTDE) paradigm [56] to train the MARL agents. CTDE allows these agents to train decentralized policies with global information during training and to make decisions based on the individually learned policies during inference. We also use MAML [23], the meta-RL algorithm, to adapt to various network environments through parameter learning. The overall workﬂow of Ahaggar is shown in Fig. 2, where the steps are numbered as 1⃝– 8⃝. A. Formulation of the Problem At each segment download time epoch t, Ahaggar performs the bitrate guidance tasks (denoted by Z) by selecting the best bitrate (denoted by lc t) with respect to the current state (denoted by sc t) of each client c.

**Fragmento 20 - p. 3 - score 3:**

The formulation in (1) is a multi-agent decision problem and aims to ﬁnd the best bitrate lc,⋆ t that maximizes the viewer QoEc t for each client c with respect to C.1–C.2. Here, each client has access only to its local observations, and fully capturing the state of the global environment experienced by all clients is not feasible. Therefore, we cast the problem (1) as a partially observ- able Markov decision process (POMDP), which is characterized by its observation and historical information capabilities. The POMDP model consists of 11-tuples POMDP = (S, A, O, R, P, U, Z, C, N, α, γ), where: r S = {S1, . . . , SN} is the set of the ﬁnite and discrete agent states of N agents.

**Fragmento 21 - p. 4 - score 3:**

The agent uses these observations to form a belief about what state the system is currently in. This is called a belief state and is expressed as a probability distribution over all possible states. The solution of the POMDP is a policy prescribing which action to take in each belief state. Formally, RL agents interact with the environment that deﬁnes state space S, observation space O and belief state space B. At each time epoch t, each RL agent c observes a state oc t ∈O and then receives a belief state bc t ∈B from the environment. Later, it takes an action ac t ∈A (aka lc,⋆ t ) while it receives a reward rc t ∈R. Here, each agent c aims to ﬁnd the optimal policy πc,⋆: S →O →B →A that maps states-to-actions and maximizes the reward.

**Fragmento 22 - p. 4 - score 3:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10381 Fig. 2. Overall bitrate guidance system of Ahaggar. At each time t = [1, . . . , k], each agent c does not track the exact state sc t, but rather it uses the observations oc t for any given task zc t. Therefore, it has to rely on the history of actions and observations, denoted by hc t, to perform the best actions that result in higher rewards. We deﬁne the set of histories of client c as Hc = {hc 1, . . . , hc k} where hc t = {(ac t, oc t); . . . ; (ac 1, oc 1)} and the set of histories of N agents as H = {H1, . . . , HN}. Yet, hc t might exponentially grow with every action taken and every state observed.


### 8.3. accion decision abr

Palabras clave usadas: `action, bitrate, quality level, representation, decision, select, selection, guidance, recommendation, adaptation, cap, mask, quality, download, chunk, rate`

**Fragmento 1 - p. 10 - score 8:**

TD column in Table III). We anticipated these results because Ahaggar makes bitrate guidance decisions based on not only the throughput, buffer level and segment sizes, but also segment quality and device resolution. It also uses MAML for continual learning and fast adaptation to unseen environments. In contrast, other ABR schemes use one or more heuristics or an NN combining these heuristics and they do not necessarily perform well in unseen environments. Fig. 6 and Table III conﬁrm this. For instance, Pensieve achieved the highest average selected bitrate and Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.

**Fragmento 2 - p. 2 - score 6:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10379 bitrate guidance with perceptual quality and device resolution awareness? ❸How to achieve continual learning for the server- side bitrate guidance? We answer the questions above in the context of Ahaggar,1 a meta reinforcement learning (meta-RL)-based solution. Ahag- gar has a server-side learning model that takes network condi- tions, clients’ statuses, device resolutions and streamed content as input features, and then provides quality and resolution-aware bitrate guidance to the streaming clients. Leveraging the server’s vastcomputationalpower,storagecapacityandmemory,Ahag- gar enables model inference for performing bitrate guidance tasks and helps resource-constrained streaming clients run their lightweight heuristic-based ABR schemes.

**Fragmento 3 - p. 3 - score 6:**

Inparticular,weuseacentralizedtraining with decentralized execution (CTDE) paradigm [56] to train the MARL agents. CTDE allows these agents to train decentralized policies with global information during training and to make decisions based on the individually learned policies during inference. We also use MAML [23], the meta-RL algorithm, to adapt to various network environments through parameter learning. The overall workﬂow of Ahaggar is shown in Fig. 2, where the steps are numbered as 1⃝– 8⃝. A. Formulation of the Problem At each segment download time epoch t, Ahaggar performs the bitrate guidance tasks (denoted by Z) by selecting the best bitrate (denoted by lc t) with respect to the current state (denoted by sc t) of each client c.

**Fragmento 4 - p. 3 - score 6:**

For each agent c, we deﬁne the set of agent states as Sc = {sc 1, . . . , sc k}, where k = |Zc| is the total number of bitrate guidance tasks. r A = {A1, . . . , AN} is the ﬁnite and discrete set of actions of N agents. For each agent c, we deﬁne the set of agent actions as Ac = {ac 1, . . . , ac k}, where each action is the selected bitrate lc during a bitrate guidance task. r O = {O1, . . . , ON} is the ﬁnite set of observation states captured by the set of agents. For each client c, the set of observations is Oc = {oc 1, . . . , oc k}. r R = {R1, . . . , RN} is the set of expected immediate re- wards, which depends on states and actions taken by N agents. For each client c, the set of rewards is Rc = {rc 1, .

**Fragmento 5 - p. 1 - score 5:**

10378 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024 Bitrate Adaptation and Guidance With Meta Reinforcement Learning Abdelhak Bentaleb , Member, IEEE, May Lim , Mehmet N. Akcay , Ali C. Begen , Senior Member, IEEE, and Roger Zimmermann , Senior Member, IEEE Abstract—Adaptive bitrate (ABR) schemes enable streaming clients to adapt to time-varying network/device conditions for a stall-free viewing experience. Most ABR schemes use manually tuned heuristics or learning-based methods. Heuristics are easy to implement but do not always perform well, whereas learning-based methods generally perform well but are difﬁcult to deploy on low-resource devices.

**Fragmento 6 - p. 1 - score 5:**

We thoroughly investigate these areas and report our ﬁndings. We also (iii) discuss the Ahaggar design choices. Experiments on an open-source system show that Ahaggar adapts to unseen conditions fast and outperforms its competitors in several viewer experience metrics. Index Terms—Adaptive streaming, meta-RL, ABR, CMCD, CMSD, bitrate guidance, quality awareness. I. INTRODUCTION W ITH the prevalence of HTTP adaptive streaming (HAS), the design of adaptive bitrate (ABR) logic—the algo- rithm deciding which segments to download and when (pri- marily based on the advertised encoding bitrate)—has received Manuscript received 22 January 2024; accepted 5 March 2024.

**Fragmento 7 - p. 2 - score 5:**

CMCD deﬁnes a set of information collected by a media client and sent along with the HTTP requests to the server running Ahaggar in query arguments or header extensions. CMSD allows the server to 1A highland region in the central Sahara in southern Algeria. convey Ahaggar bitrate guidance decisions to media clients through the HTTP response headers. We evaluate the performance of Ahaggar against several ABR solutions by running real-world trace-driven experiments. These experiments cover multiple clients with heterogeneous network conditions and device resolutions. Experimental re- sults show that Ahaggar delivers consistent quality, improves viewer QoE by up to 87.0%, reduces rebuffering duration by up to 84.4% and reduces bandwidth consumption by up to 62.6%.

**Fragmento 8 - p. 2 - score 5:**

We take inputs from the network, clients and streamed content into the Ahaggar neural network (NN) for bitrate guidance. The objective of Ahaggar is to select the minimum bitrate (among the available options) above which the next higher bitrate improves the perceptual quality only insigniﬁcantly at the speciﬁc device resolution. In this study, we use an objective full-reference perceptual video quality metric known as Video Multi-method Assessment Fusion (VMAF) [42]. To ensure healthy cooperation without incurring additional complexities between the clients and servers, Ahaggar adopts the emerging Common Media Client/Server Data standards: CMCD [9], [13], [18] and CMSD [7], [19], [33].

**Fragmento 9 - p. 3 - score 5:**

Mathematically, the bitrate guidance problem for multiple clients can be formulated as ⎧ ⎪ ⎪ ⎪ ⎪ ⎨ ⎪ ⎪ ⎪ ⎪ ⎩ ﬁnd lc,⋆ t (π), ∀c ∈[1, . . . , N], ∀t ∈[1, . . . , k] arg max π QoEc t (π) s.t. lc,⋆ t (π) ≤mtpc t C.1 N  c=1 lc,⋆ t (π) ≤BWtotal C.2 , (1) where lc,⋆ t is the best bitrate, which is the minimum among the available options above and the next higher bitrate improves the perceptual quality only insigniﬁcantly for the speciﬁc content at the speciﬁc device resolution. Here, we use 1-JND (Just No- ticeable Difference) as the threshold for being signiﬁcant [37]. Further in this formulation, π is an RL policy that decides the bitrate for each client, N is the total number of clients, BWtotal is the total server capacity and mtpc is the measured throughput by client c.

**Fragmento 10 - p. 4 - score 5:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10381 Fig. 2. Overall bitrate guidance system of Ahaggar. At each time t = [1, . . . , k], each agent c does not track the exact state sc t, but rather it uses the observations oc t for any given task zc t. Therefore, it has to rely on the history of actions and observations, denoted by hc t, to perform the best actions that result in higher rewards. We deﬁne the set of histories of client c as Hc = {hc 1, . . . , hc k} where hc t = {(ac t, oc t); . . . ; (ac 1, oc 1)} and the set of histories of N agents as H = {H1, . . . , HN}. Yet, hc t might exponentially grow with every action taken and every state observed.

**Fragmento 11 - p. 8 - score 5:**

Similarly, in meta-testing (20% datasets), Ahaggar generalizes well and converges within only 40-shots (e.g., equal to watching 40 video sessions). In contrast, other techniques require more shots to adapt to various environments. For example, ANIL and PEAR require 100-shots and 150- shots, respectively. This is an anticipated result from Ahaggar because of DPPO multi-agent work distribution and MAML fast adaptation capabilities. More notably, during the inference, Ahaggar takes only a few milliseconds to perform the bitrate Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 12 - p. 9 - score 5:**

We (i) added new CMCD parameters (qt, dt, rs, ls, −→ QT, −→ LS) to support Ahaggar design, and (ii) used the mb = l (maximum suggested bitrate) CMSD-Dynamic parameter to convey Ahaggar’s bitrate guidance to each cor- responding client. On the server side, we used TensorFlow.js converter [45] to convert and load a pre-trained meta-model into a JavaScript Web-based application and run inference through TensorFlow.js. On the client side, we implemented a simple heuristic as our ABR scheme, which used Ahaggar bitrate guidance decisions to perform rate adaptation. To simplify input state data collection, we appended the manifest ﬁles by adding four tags: size, phone, hdtv and uhdtv.

**Fragmento 13 - p. 11 - score 5:**

It also achieved higher O.35 (Visual Quality Score, not shown) scores with values ranging between 4.60 and 4.94. These results conﬁrm how well Ahaggar performs to balance the QoEitu metrics. Second, the Belgium 4G/LTE dataset has the lowest bandwidth values in its network traces. Therefore, all ABR schemes achieved the lowest scores in terms of O.23, O.35 and O.46. Nonetheless, since Ahaggar has been designed to adapt quickly to challenging network conditions (thanks to MAML), it was able to obtain the best O.23 (2.37) and O.46 (2.70) scores. Although other baselines achieved a comparable O.35 score (not shown), they faced frequent and long rebuffering events due to their greedy bitrate selection strategy.

**Fragmento 14 - p. 12 - score 5:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10389 TABLE V AVERAGE RESULTS OF THE QOE AND ITS METRICS FOR DIFFERENT NETWORK TRACES FOR SCENARIO A2 Ahaggar picked a higher bitrate on the average for a UHDTV compared to an HDTV and a phone. For instance, it selected 1.5x-2x higher bitrate for UHDTV compared to the phone with almost a 1-JND difference between the VMAF scores for various network traces. This is because devices with a phone-like res- olution can achieve the highest VMAF score (95-98) requiring only half of the bitrate that a UHDTV requires. We note that the VMAF score differences at a similar bitrate level (e.g., phone versus HDTV in NYU LTE) are due to the different per-device VMAF models used to calculate the scores.

**Fragmento 15 - p. 14 - score 5:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10391 Dynamic clients in mixed-ABR environments). We note that Belgium 4G/LTE contains the most challenging traces with the lowest bandwidth range than the other three sets of traces, and under these extreme network conditions, the Dynamic clients were selecting much lower video bitrates that coincided with the levels of bitrate selected by the Ahaggar clients. Hence, in Belgium 4G/LTE, the introduction of Ahaggar clients did not affect the amount of data transmitted over the network which explains the absence of performance gains as seen in the other sets of traces.

**Fragmento 16 - p. 1 - score 4:**

To make the most out of both worlds, we earlier developed Ahaggar, a learning-based scheme executing on the server side that provides quality-aware bitrate guidance to streaming clients running their own heuristics. Ahaggar’s novelty is the meta reinforcement learning approach taking network condi- tions, clients’ statuses and device resolutions, and streamed content as input features to perform bitrate guidance. Ahaggar uses the new Common Media Client/Server Data (CMCD/SD) protocols to exchange the necessary metadata between the servers and clients. While Ahaggar was a signiﬁcant step forward, in this study, we focus on three open areas, namely, (i) exploring the performance of Ahaggar in a heterogeneous environment including both Ahag- gar and non-Ahaggar clients with varied network conditions and device resolutions, and (ii) quantifying the impact of device resolutions on QoE with Ahaggar.

**Fragmento 17 - p. 1 - score 4:**

Lastly, many studies [22], [30] claim that perceptual video quality and device resolution must be considered in the ABR logic to improve the quality of experience (QoE). Incorporating these parameters into a learning model and then continually retraining the model is also infeasible for clients running on low-resource devices. In our prior work (Ahaggar) [14], we have shown that heuristic and learning-based schemes can complement each other and leveraging the advantages of both solutions while avoiding their shortcomings is the key. This brings up the following three questions, which we seek to answer: ❶Can we run a lightweight heuristic-based scheme on the client side and learning-based bitrate guidance on the server side (which is not as constrained as the clients) such that they can cooperate harmoniously to deliver s better QoE?

**Fragmento 18 - p. 1 - score 4:**

Therefore, future states are not easy to predict accurately. Most schemes use classical approaches to train an agent by giving feedback for decisions while interacting with an environment. Such interaction can be efﬁcientlyperformedinacontrolledtrace-drivensimulator. Still, a mismatch may occur when the trained model is deployed in a live system and encounters an environment not previously seen [55]. As a result, the scheme may fail to perform proper rate adaptation. Second, deploying learning-based schemes on devices with scarce resources is impractical due to high storage and computational costs. Prior work [55] showed that a learning model trained on past network scenarios could hardly provide a comparable performance under new conditions, and hence, effective and continual model retraining/update was required.

**Fragmento 19 - p. 2 - score 4:**

Ahaggar models bitrate guidance tasks for multiple clients as a partially ob- servable Markov decision process (POMDP) and leverages the latest developments in DRL to dynamically adapt to the varying network conditions. Speciﬁcally, it uses advantage Actor-Critic networks (A2C) for model training and Distributed Proximal Policy Optimization (DPPO) [25] with clip and Adam optimizer for policy updates at each time interval. Considering the changes in the environment, we adopt a Model Agnostic Meta-Learning (MAML) [23] on-policy gradient-based meta-RL approach that embeds policy gradient steps into the meta optimization. This al- lows Ahaggar to update the model parameters to achieve good generalization performance on unseen environments during the inference.

**Fragmento 20 - p. 2 - score 4:**

Client-Driven Learning-Based ABR: These schemes learn from the streaming environment by training an NN using DRL techniques [6], [17]. Mao et al. [35] proposed Pensieve, the ﬁrst learning ABR that used DRL to generate a strategy toward maximizing the viewer QoE. Bentaleb et al. [10] designed AMP that implemented a set of learning-based bandwidth predictors and model auto-selection for HAS. Similarly, Fugu [52] was proposed to leverage the hidden Markov model for accurate throughput prediction. Huang et al. [27] used imitation learning to propose Comyco as ABR for on-demand videos. Server-Driven Solutions: These solutions implement a rate control on the server to control a client’s ABR decisions im- plicitly or explicitly.

**Fragmento 21 - p. 3 - score 4:**

10380 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024 Fig. 1. MARL of Ahaggar. Network-Driven Solutions: These solutions can be further cat- egorized into: (1) In-network solutions where some works [11], [12] use software-deﬁned networking to assist clients in their ABR decisions, rate allocation [38] or multi-path delivery [16]; (2) Server and network assistance solutions where some pa- pers [40], [49] leverage the SAND standard [1] that enables data collection from various network entities involved in media delivery. These data are then stored on a centralized server for intelligent decisions, e.g., rate allocation; (3) Data-driven solutions that combine SAND with AI capabilities for improved decision making.

**Fragmento 22 - p. 3 - score 4:**

. . , rc k}. r P = S × S × A →[0, 1] is the state transition probability function P(s′|s, a) from the state s to s′ ∈S when action a ∈A is taken. r U = O × S × A →[0, 1] is the observation probability function O(o′|s′, a) of observing o′ ∈O after transitioning to s′ due to a. r Z = {Z1, . . . , ZN} represents the bitrate guidance prob- lem maxπ QoEc t (π) for every agent c. The set of bi- trate guidance tasks for agent c is thus deﬁned as Zc = {zc 1, . . . , zc k}. r C = {1, . . . , N} is the set of N agents, where N is the total number of agents and c ∈[1, . . . , N] is an agent. r α and γ ∈[0, 1] are the learning rate and discount factor, respectively. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.


### 8.4. reward qoe objetivo

Palabras clave usadas: `reward, QoE, quality of experience, utility, objective, loss, rebuffer, stall, stalling, smoothness, switching, quality variation, latency, fairness, bitrate smoothness, video quality, tail, risk, severe`

**Fragmento 1 - p. 1 - score 3:**

Lastly, many studies [22], [30] claim that perceptual video quality and device resolution must be considered in the ABR logic to improve the quality of experience (QoE). Incorporating these parameters into a learning model and then continually retraining the model is also infeasible for clients running on low-resource devices. In our prior work (Ahaggar) [14], we have shown that heuristic and learning-based schemes can complement each other and leveraging the advantages of both solutions while avoiding their shortcomings is the key. This brings up the following three questions, which we seek to answer: ❶Can we run a lightweight heuristic-based scheme on the client side and learning-based bitrate guidance on the server side (which is not as constrained as the clients) such that they can cooperate harmoniously to deliver s better QoE?

**Fragmento 2 - p. 7 - score 3:**

We implemented these techniques in Ahaggar and then ran the experiment with 1,000 agents on the same validation set every 500 episodes and recorded the validation learning curve in Fig. 3. We can see that DPPO achieves the best performance with (i) the highest possible N-QoElin (reward; see Section V-B4) and (ii) trains and converges faster to the highest reward value with only 3,000 episodes, compared to its competitors.DPPOreliesonspecializedclippingintheobjective function (7) to remove incentives for the new policy to get far from the old policy. Hence, it allows robust policy optimization for whole video sessions. Comparing DPPO with TRPO, we observe that TRPO is the runner-up that typically obtains a high reward, but it takes more time (6,000 episodes) to converge to the best achievable reward.

**Fragmento 3 - p. 11 - score 3:**

10388 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024 Fig. 6. Avg. QoE itu (O.46) and avg. rebuffering duration ratio in various network traces for Scenario A1. The bottom (left) edge, mark and top (right) edge indicate the average−std, average and average + std, respectively, with a 95% conﬁdence interval. average pUHD, but it performed poorly in most other metrics. In thesamecontext,BOLAfailedtodelivergoodvideoqualitywith inferior VMAF scores, and RobustMPC suffered from frequent and long rebuffering events. Similarly, Ahaggar achieved the highest average QoEitu and lowest average rebuffering duration (see Fig. 6). In detail, Ahaggar achieved the highest average QoE with an improvement of [Lumous 4G Fig.

**Fragmento 4 - p. 11 - score 3:**

6(a): 22.28% (44.73%), Belgium 4G/LTE Fig. 6(b): 49.49% (37.06%), NYU LTE Fig. 6(c): 55.04% (85.08%), Lumous 5G Fig. 6(d): 8.01% (31.10%)] and lowest average rebuffering duration with a reduction of 62.81% (84.36%) across all network traces, compared to heuristic-based (learning-based) ABR schemes. Compared to Ahaggar, Dynamic achieved the second-best average results in terms of the QoE and rebuffering duration. This is because of the Dynamic design that combines the beneﬁts of BOLA and TH by switching between both in runtime based on the stability of the current buffer level. However, Pensieve, followed by RobustMPC, suffered from low QoE and long RD due to wrong ABR decisions.

**Fragmento 5 - p. 12 - score 3:**

7(a): 109.80% (114.92%), Belgium 4G/LTE Fig. 7(b): 74.30% (90.16%), NYU LTE Fig. 7(c): 104.20% (114.14%), Lumous 5G Fig. 7(d): 10.69% (10.87%)] and lowest average rebuffering duration with areductionof[Lumous4GFig.7(a):93.58%(95.40%),Belgium 4G/LTE Fig. 7(b): 87.08% (98.74%), NYU LTE Fig. 7(c): 95.03% (98.75%), Lumous 5G Fig. 7(d): 1.57% (20.96%)], compared to the heuristic-based (learning-based) ABR schemes. The performance gains are most prominent in Lumous 4G, Belgium 4G/LTE and NYU LTE, which is also evident in Fig. 7(a)–(c) where Ahaggar is placed much further ahead of the other schemes. From the detailed analysis of the QoEitu scores in Table V, we see that Ahaggar achieved the highest average O.23 and O.46 scores for all network traces with an average improvement Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 6 - p. 2 - score 2:**

CMCD deﬁnes a set of information collected by a media client and sent along with the HTTP requests to the server running Ahaggar in query arguments or header extensions. CMSD allows the server to 1A highland region in the central Sahara in southern Algeria. convey Ahaggar bitrate guidance decisions to media clients through the HTTP response headers. We evaluate the performance of Ahaggar against several ABR solutions by running real-world trace-driven experiments. These experiments cover multiple clients with heterogeneous network conditions and device resolutions. Experimental re- sults show that Ahaggar delivers consistent quality, improves viewer QoE by up to 87.0%, reduces rebuffering duration by up to 84.4% and reduces bandwidth consumption by up to 62.6%.

**Fragmento 7 - p. 2 - score 2:**

We take inputs from the network, clients and streamed content into the Ahaggar neural network (NN) for bitrate guidance. The objective of Ahaggar is to select the minimum bitrate (among the available options) above which the next higher bitrate improves the perceptual quality only insigniﬁcantly at the speciﬁc device resolution. In this study, we use an objective full-reference perceptual video quality metric known as Video Multi-method Assessment Fusion (VMAF) [42]. To ensure healthy cooperation without incurring additional complexities between the clients and servers, Ahaggar adopts the emerging Common Media Client/Server Data standards: CMCD [9], [13], [18] and CMSD [7], [19], [33].

**Fragmento 8 - p. 3 - score 2:**

These solutions collect QoE metrics from many streaming sessions at a logically centralized controller that maintains a global view of the real-time network conditions, based on which the controller makes decisions regarding the individual sessions (e.g., [24], [28]). III. Ahaggar BITRATE GUIDANCE Ahaggar serves multiple clients (agents in RL) with a shared environment, distinct rewards and policies, as depicted in Fig. 1. It performs bitrate guidance tasks at every time window and decides the best bitrate for each client. Therefore, we consider a fully cooperative multi-agent RL (MARL) [56] framework with independent learners setting that involves a set of agents sharing thesameenvironment.

**Fragmento 9 - p. 4 - score 2:**

B. Ahaggar Meta-Training (Ofﬂine) To train the Ahaggar meta-model, we use Park [34]—a Python-based segment-level simulator that is based on OpenAI and state-of-the-art ABR simulators [46] for RL-based model training. This simulator faithfully emulates a streaming session where the learning agent uses a large corpus of real-world net- work and content traces to explore the streaming environment. ▷Network Traces. We used the Belgium 4G/LTE [51], Nor- way 4G/LTE [43], NYU LTE [36] and Lumous 4G/5G [39] datasets. Each trace entry consists of a throughput value (Mbps), round-trip time (RTT; ms) and packet loss (%). ▷Content Traces. We used the Comyco [27] and Waterloo SQoE-IV [22] datasets.

**Fragmento 10 - p. 5 - score 2:**

These results are similar to [50]. ▷Policy Gradient and Training Algorithm. The essential objective of Ahaggar is to improve the policy via boosting the probabilities of high-reward samples from the collected trajectories and declining the possibilities of failure samples from the bad trajectories. For every time epoch t, each RL agent c of Ahaggar selects the action ac t that corresponds to the bitrate for the next segment using the improved policy π : πc,⋆ θ (bc t, ac t) →[0, 1] at state bc t, which results in the best accumulated discounted reward that is expressed as Gc t = Tπc θ  ¯t=t γ¯t−t × rc t, ac t = arg max a E [Gc t(bc t, a)] , (3) where Gc t is computed from time t to the end of training, Tπc θ denotes the batch size for updating the gradient policy πc θ, γ ∈[0, 1] is the discount factor, θ is the policy parameter, and πc,⋆ θ (bc t, ac t) is the probability that action ac t is taken in state bc t.

**Fragmento 11 - p. 5 - score 2:**

rc t = ω1 × qc t(lc t) −ω2 × rdc t −ω3 × rcc t −ω4 × qoc t −ω5 × qsc t, (2) where qc t(lc t) maps the selected bitrate to the quality perceived (VMAF) [11], [53], qoc t = |qc t(lc t) −qc t−1(lc t−1)|, qsc t = qoc t/20, and ωi are the coefﬁcients of the reward function. Herein, following prior works [27], [50], we set qsc t as the difference of 20 in VMAF values of two consecutive segments. This QoE model is developed based on linear regression on two datasets: Comyco [27] and Waterloo SQoE-IV [22], where 70% of the data is used for training and 30% for testing. We followed the same setup to tune the coefﬁcients and our results show that ω1 = 0.077, ω2 = 1.249, ω3 = 2.877, ω4 = 0.049, and ω5 = 1.436 achieve the best trade-off between the ﬁve QoE metrics.

**Fragmento 12 - p. 5 - score 2:**

The actor and critic use the same structure but with different outputs. For both networks, we use the Softmax activation function (Softmax()) with the L2-norm of networks as the last FC layer, resulting in an output range from 0 to 1. ▷Reward Function. At each time epoch t, the reward rc t of an agent c is calculated after each action ac t is taken to ensure that Ahaggar can learn from past experience. To do so, we adopt a well-know state-of-the-art reward function [11], [27], [35], [50], [53] that linearly combines ﬁve metrics (2): perceptual quality (qc t(lc t)), rebuffering duration (rdc t) and count (rcc t), quality oscillations (qoc t) and switches (qsc t).

**Fragmento 13 - p. 6 - score 2:**

To do so, the critic network uses the standard TD method to compute the loss function and minimize its value. The parameter θvc of the critic network is updated through a stochastic gradient descent (SGD) algorithm using (6). θvc ←θvc −¯α Tθ  t=1 ▽θ(rc t + γV πc θ(bc t+1; θvc) −V πc θ(bc t; θvc))2, (6) where ¯α is the learning rate for the critic, V πc θ(bc t; θvc) and V πc θ(bc t+1, θvc) are the objective assessments for bc t and bc t+1, respectively, from the critic network. Finally, we update the policy πθ periodically every κ-steps using PPO with constrained clipped objective (CCO) and the Adam optimizer. The constraint represents how much the policy is allowed to change, expressed in terms of the Kullback-Leibler (KL) divergence (KL[πc θold|πc θ]).

**Fragmento 14 - p. 6 - score 2:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10383 via a stochastic gradient ascent using (5). θπc ←θπc + α Tθ  t=1 A πc θ t (bc t, ac t) ▽θ log πc θ(ac t, bc t) + β E, (5) where Tθ is the update interval, α is the learning rate and β is the entropy parameter that is set to a large value at the beginning of the training to encourage exploration and decreases over time to emphasize improving rewards. To calculate the advantage A(bc t, ac t) for a given experience, we have to estimate the value function V πc θ(b). This estimation is performed by the critic network that makes an objective assessment for all the states ∀bc t ∈B of an agent c during the training.

**Fragmento 15 - p. 7 - score 2:**

After that, these agents send the calculated gradients to the chief, which in turn merges them via agents’ loss functions and the outer loop’s learning rate β. Formally, we deﬁne a meta-objective (Lmeta(θ)) as Tπc θ t=1 LSGD Evti (fθiκ). The optimization of L is called the outer-loop update. The resulting update for θ is given by (9). θ = θ −β ▽θ Tπc θ  t=1 LSGD Evti (fθiκ, Di κ), (9) where the update is performed using SGD, β is a learning rate and LSGD Evti denotes the loss on the environment Evti. C. Ahaggar Meta-Testing (Online) The objective of Ahaggar is to learn how to adapt to hetero- geneous network environments during the online phase through continual learning enabled by MAML.

**Fragmento 16 - p. 8 - score 2:**

We run the same experiment outlined in Section IV-A and the meta-validation learning curve for this experiment is shown in Fig. 4. With 3,000 episodes, we observe that MAML out- performs existing meta-RL approaches in terms of N-QoElin with an average improvement of 57.5% (PEARL: 64.4%, RL2: 65.3%, REPTILE: 79.9%, ANIL: 28.7%, IMPALA: 49.11%). It also converges quickly to the best reward, requiring 3,000 episodes, 2x better than the runner-up approach (ANIL), which shows the effectiveness of MAML in the meta-training phase. ANIL generally performs better than RL2, IMPALA, REPTILE and PEARL, as it is an extension of MAML without inner-loop updates.

**Fragmento 17 - p. 9 - score 2:**

To simplify the presentation of the QoE, we used a normalized QoElin (N-QoElin) with values between 0 and 1. To achieve that, we used the best achievable QoE (QoE⋆) in each session such that N-QoElin = QoElin / QoE⋆. The ITU P.1203 QoE model in Mode 0 (O.46) takes four metrics as input: bitrate, rebuffering duration, frame rate and content resolution. How to compute the QoEitu is described in [44]. This model outputs QoE values in the range of one to ﬁve (MOS) and we normalized them (N-QoEitu) to [0,1]. In addition, we computed (i) the total downloaded (TD) size (in MB) metric to measure how much bandwidth was consumed during the session, (ii) percentage of the HD (pHD) segments rendered at 720p or higher, and (iii) percentage of the UHD (pUHD) segments rendered at 2160p.

**Fragmento 18 - p. 9 - score 2:**

4) Performance Metrics: We tested the ABR schemes using two main QoE models: Linear QoE [50] and ITU P.1203 QoE (Mode 0) [44]. For every session, we computed the accumulated QoElin using a linear function as follows: ω1 k  t=1 qc t(lc t)−ω2 k  t=1 rdc t −ω3rcc t −ω4 k  t=2 qoc t −ω5 k  t=2 qsc t, (10) where k t=1 qc t(lc t) is the accumulative perceived perceptual quality, k t=1 rdc t is the total rebuffering duration (RD), rcc t is the total rebuffering count (RC), k t=2 qoc t is the cumulative quality oscillations, k t=2 qsc t is the total number of quality switches, and k is the total number of segments. The coefﬁcients of ω1,2,3,4,5 are given in (2).

**Fragmento 19 - p. 10 - score 2:**

r Scenario C: The six clients contain a mix of ABR schemes: three Dynamic and three Ahaggar clients. This scenario evaluates the impact of introducing Ahaggar clients amongst clients that do not use Ahaggar. Client-side network emulation is used. Details of the network traces used in each scenario are given in supplementary materials (Appendix A), available online. C. Results for Multiple Identical Clients (Scenario A1) For each ABR scheme, we ran multiple UHDTV clients. Table III shows the total QoE and detailed breakdown of each QoE metric for each ABR scheme for various network traces. We provide the average and standard deviation values for six clients and over ﬁve runs in the format of average ± std.

**Fragmento 20 - p. 11 - score 2:**

It is worth mentioning that all schemes faced a few rebuffering events in Lumous 5G because sometimes the bandwidth dropped signiﬁcantly and suddenly (caused by the handoffs to 4G). This is a behavior known in 5G networks operating in higher frequencies [39]. To understand how QoEitu (Mode 0) is computed for each session, Table III (the eighth and ninth columns) highlights the scores of its essential metrics (O.23: Rebufﬁng Duration Score and O.46: Overall Score) for different ABR schemes. The score of each metric is given in the MOS range of one to ﬁve. Here, we deduce three important thrusts. First, Ahaggar outperformed the baselines, achieving the best O.23 and O.46 scores for all network traces with an average improvement of 67.55% (heuristic-based: 60.75%, learning-based: 94.75%) TABLE IV AVERAGE QOE itu (O.46) SCORES AND ITS METRICS PRODUCED BY Ahaggar RUNNING ON DEVICES WITH DIFFERENT RESOLUTIONS FOR SCENARIO B1 and 36.86% (heuristic-based: 33.70%, learning-based: 49.49%) across all network traces, respectively.

**Fragmento 21 - p. 11 - score 2:**

Third, Dynamic was the runner-up, receiving the second-best results in terms of O.23 and O.46. Unexpectedly, Pensieve failed to produce good ABR decisions, leading to multiple rebuffering events that contributed to the lowest O.23 score, which impacted O.46 negatively in most network traces. WealsoconductedacomparisonbetweenQoEitu andQoElin. We ﬁrst normalized both values (Section V-B4) and the com- parison between different ABR schemes for various network traces is listed in the last column of Table III. In each network trace, Ahaggar achieved the highest and most consistent per- formance in terms of N-QoEitu and N-QoElin (only in NYU LTE, TH and Dynamic were slightly better) compared to other ABR schemes.

**Fragmento 22 - p. 11 - score 2:**

It also achieved higher O.35 (Visual Quality Score, not shown) scores with values ranging between 4.60 and 4.94. These results conﬁrm how well Ahaggar performs to balance the QoEitu metrics. Second, the Belgium 4G/LTE dataset has the lowest bandwidth values in its network traces. Therefore, all ABR schemes achieved the lowest scores in terms of O.23, O.35 and O.46. Nonetheless, since Ahaggar has been designed to adapt quickly to challenging network conditions (thanks to MAML), it was able to obtain the best O.23 (2.37) and O.46 (2.70) scores. Although other baselines achieved a comparable O.35 score (not shown), they faced frequent and long rebuffering events due to their greedy bitrate selection strategy.


### 8.5. entrenamiento optimizacion

Palabras clave usadas: `training, train, trained, episode, epoch, optimizer, learning rate, experience replay, fine-tune, fine-tuning, pretrain, pre-training, behavior cloning, imitation, expert, simulation, simulator, offline, online, curriculum, loss function, joint optimization, dataset, sample`

**Fragmento 1 - p. 6 - score 5:**

To do so, the critic network uses the standard TD method to compute the loss function and minimize its value. The parameter θvc of the critic network is updated through a stochastic gradient descent (SGD) algorithm using (6). θvc ←θvc −¯α Tθ  t=1 ▽θ(rc t + γV πc θ(bc t+1; θvc) −V πc θ(bc t; θvc))2, (6) where ¯α is the learning rate for the critic, V πc θ(bc t; θvc) and V πc θ(bc t+1, θvc) are the objective assessments for bc t and bc t+1, respectively, from the critic network. Finally, we update the policy πθ periodically every κ-steps using PPO with constrained clipped objective (CCO) and the Adam optimizer. The constraint represents how much the policy is allowed to change, expressed in terms of the Kullback-Leibler (KL) divergence (KL[πc θold|πc θ]).

**Fragmento 2 - p. 9 - score 5:**

These tags represent the segment sizes and VMAF scores for phone, HDTV and UHDTV, respectively. The VMAF scores were computed using different VMAF models depending on the device resolution. We provide a sample manifest ﬁle in [2]. B. Methodology and Evaluation Setup 1) Video Sample and Parameters: The HTTP server hosted the 4K DASH dataset [41] that was not used in training. We encoded the 636 seconds long Big Buck Bunny (BBB) into four- second segments in FFmpeg using the H.264 codec at 30 fps and in 13 bitrates/resolutions. Further characteristics of BBB are given in supplementary materials (Appendix B), available online. 2) Network Traces: We used network traces with different user mobility (bus, walking, car, train, bicycle, tram, ferry and driving) to throttle the bandwidth between the server and clients.

**Fragmento 3 - p. 1 - score 4:**

Therefore, future states are not easy to predict accurately. Most schemes use classical approaches to train an agent by giving feedback for decisions while interacting with an environment. Such interaction can be efﬁcientlyperformedinacontrolledtrace-drivensimulator. Still, a mismatch may occur when the trained model is deployed in a live system and encounters an environment not previously seen [55]. As a result, the scheme may fail to perform proper rate adaptation. Second, deploying learning-based schemes on devices with scarce resources is impractical due to high storage and computational costs. Prior work [55] showed that a learning model trained on past network scenarios could hardly provide a comparable performance under new conditions, and hence, effective and continual model retraining/update was required.

**Fragmento 4 - p. 4 - score 4:**

B. Ahaggar Meta-Training (Ofﬂine) To train the Ahaggar meta-model, we use Park [34]—a Python-based segment-level simulator that is based on OpenAI and state-of-the-art ABR simulators [46] for RL-based model training. This simulator faithfully emulates a streaming session where the learning agent uses a large corpus of real-world net- work and content traces to explore the streaming environment. ▷Network Traces. We used the Belgium 4G/LTE [51], Nor- way 4G/LTE [43], NYU LTE [36] and Lumous 4G/5G [39] datasets. Each trace entry consists of a throughput value (Mbps), round-trip time (RTT; ms) and packet loss (%). ▷Content Traces. We used the Comyco [27] and Waterloo SQoE-IV [22] datasets.

**Fragmento 5 - p. 5 - score 4:**

These results are similar to [50]. ▷Policy Gradient and Training Algorithm. The essential objective of Ahaggar is to improve the policy via boosting the probabilities of high-reward samples from the collected trajectories and declining the possibilities of failure samples from the bad trajectories. For every time epoch t, each RL agent c of Ahaggar selects the action ac t that corresponds to the bitrate for the next segment using the improved policy π : πc,⋆ θ (bc t, ac t) →[0, 1] at state bc t, which results in the best accumulated discounted reward that is expressed as Gc t = Tπc θ  ¯t=t γ¯t−t × rc t, ac t = arg max a E [Gc t(bc t, a)] , (3) where Gc t is computed from time t to the end of training, Tπc θ denotes the batch size for updating the gradient policy πc θ, γ ∈[0, 1] is the discount factor, θ is the policy parameter, and πc,⋆ θ (bc t, ac t) is the probability that action ac t is taken in state bc t.

**Fragmento 6 - p. 6 - score 4:**

▷Meta-Learned Policies for Training Algorithm. We adopt the MAML approach, which allows learning model parameters θ via meta-RL, i.e., ﬁnding the model parameters sensitive to changes in the environment, allowing the Ahaggar model to achieve fast adaptation to unseen environments during the inference phase. The training algorithm consists of two loops: (1) Inner Loop. For each episode, each agent c ﬁrst randomly picks a speciﬁc network and content trace as the environment, and sample X ∈D trajectories (also referred to as shots) where D = {(bc 1, ac 1); . . . ; (bc k, ac k)} denotes the set of sampled tra- jectories for inner loop in that environment according to the current policy πc θ.

**Fragmento 7 - p. 8 - score 4:**

One interesting observation is that Ahaggar with X = 40 (40- shots) is the best trade-off point, allowing good sampling ef- ﬁciency and convergence to its best generalization performance (highestachievableN-QoElin)muchfaster(comparableto2,500 episodes) within 3,000 episodes, and signiﬁcant reduction in computation cost overhead for both Ahaggar meta-training and meta-testing phases compared to X = 100, X = 80, or X = 60. Therefore, we set X=40 during the meta-training and meta-testing (and meta-validation) phases. More notably, with X = 1 or X = 20, the convergence was very slow (requiring more episodes) compared to X > 20-shots. D. Ahaggar Model Convergence We trained each model on a physical workstation machine with dual 20-core Intel E5-2630 v4 @ 2.20GHz processors, 192 GB memory, and 8 GPUs.

**Fragmento 8 - p. 8 - score 4:**

Table I shows the convergence time, episodes and shots required for a model to generalize and converge to the best solution. We ﬁxed the number of shots to 40 and workers to 1,000 for all meta-RL techniques, including Ahaggar, ANIL, PEARL, and RL2. During the training (80% datasets), Ahaggar is able to converge faster and achieve the best performance with 3,000 episodes (with 2,000 iterations per episode), taking eight hours of training, compared to other solutions. It requires 2x (2x), 4x (3x), 5x (5x), 7x (9x), and 10x (12x) fewer episodes (time) to achieve its best generalization performance compared to ANIL, IMPALA, RL2, Fugu and Pensive, respectively.

**Fragmento 9 - p. 9 - score 4:**

These traces were extracted from the 20% of network datasets for testing (Belgium 4G/LTE [51], NYU LTE [36], Lumous 4G/5G [39]). We randomly extracted six network traces from each dataset where the inter-variation duration between the bandwidth values was ﬁxed to ﬁve seconds. Further char- acteristics of the traces are given in supplementary materials (Appendix A), available online. 3) ABRSchemes: WecomparedAhaggaragainstheuristics such as throughput-based (TH), buffer-based (BOLA) and Dynamic (TH+BOLA) from dash.js [20] and RobustMPC [53] and one learning-based scheme: Pensieve [35]. The heuristic-based schemes were tuned and Pensieve was retrained with our datasets and QoE metrics to ﬁt each experiment.

**Fragmento 10 - p. 9 - score 4:**

Training parameters can impact the performance of Ahag- gar, so we empirically set the parameters as summarized in Table II. 2) Ofﬂine Training: To train the Ahaggar meta-model, we used a customized trace-based segment-level Gym simu- lator based on Park [34]. This simulator was implemented in Python 3.6 to simulate a typical HAS system based on real- world network and content traces. We used TFLearn 1.5.0 [48], RLlib of Ray 1.12.0 [32] and TensorFlow 2.4.0 to implement Ahaggar’s NN architecture and build the training workﬂow. 3) Online Testing: To test Ahaggar, we implemented a CMCD/SD-enabled streaming system [2] with Ahaggar’s bi- trate guidance functions.

**Fragmento 11 - p. 1 - score 3:**

Lastly, many studies [22], [30] claim that perceptual video quality and device resolution must be considered in the ABR logic to improve the quality of experience (QoE). Incorporating these parameters into a learning model and then continually retraining the model is also infeasible for clients running on low-resource devices. In our prior work (Ahaggar) [14], we have shown that heuristic and learning-based schemes can complement each other and leveraging the advantages of both solutions while avoiding their shortcomings is the key. This brings up the following three questions, which we seek to answer: ❶Can we run a lightweight heuristic-based scheme on the client side and learning-based bitrate guidance on the server side (which is not as constrained as the clients) such that they can cooperate harmoniously to deliver s better QoE?

**Fragmento 12 - p. 1 - score 3:**

Although these schemes are easy to implement, they heavily depend on some conﬁguration parameters, and a poor setting may signiﬁcantly hinder their efﬁcacy [27]. Hence, learning-based schemes have become an alternative, beneﬁting from the latest breakthroughs in machine learning (ML) such as deep reinforcement learning (DRL), and supervised and imitation learning techniques [5]. Learning-basedschemesattaingoodstrategieswithoutrequiring any presumptions about the environment. Nonetheless, learning-based schemes are exposed to two major limitations. First, their performance heavily depends on the training data. Network environments can be quite diverse, and their dynamics change over time.

**Fragmento 13 - p. 2 - score 3:**

Therefore, our model can converge quickly to the best performance and adapt to new unseen environments with only a small number of (e.g., 40) shots. To our knowledge, this paper is the ﬁrst study using meta-RL to improve QoE for adaptive streaming clients while cleanly separating the responsibilities for the servers and clients and respecting the client-driven nature of HAS. The Ahaggar solution comprises two phases: (i) (ofﬂine) meta-training, where each RL agent trains the Ahaggar meta- model on heterogeneous network environments, and (ii) (online) meta-testing (also called inference), where each agent contin- ually learns the system dynamics and rapidly optimizes the meta-policy, adjusting the parameter weights that determine the agent behavior according to the trajectories collected from both the meta-training and meta-testing.

**Fragmento 14 - p. 2 - score 3:**

Ahaggar models bitrate guidance tasks for multiple clients as a partially ob- servable Markov decision process (POMDP) and leverages the latest developments in DRL to dynamically adapt to the varying network conditions. Speciﬁcally, it uses advantage Actor-Critic networks (A2C) for model training and Distributed Proximal Policy Optimization (DPPO) [25] with clip and Adam optimizer for policy updates at each time interval. Considering the changes in the environment, we adopt a Model Agnostic Meta-Learning (MAML) [23] on-policy gradient-based meta-RL approach that embeds policy gradient steps into the meta optimization. This al- lows Ahaggar to update the model parameters to achieve good generalization performance on unseen environments during the inference.

**Fragmento 15 - p. 2 - score 3:**

Client-Driven Learning-Based ABR: These schemes learn from the streaming environment by training an NN using DRL techniques [6], [17]. Mao et al. [35] proposed Pensieve, the ﬁrst learning ABR that used DRL to generate a strategy toward maximizing the viewer QoE. Bentaleb et al. [10] designed AMP that implemented a set of learning-based bandwidth predictors and model auto-selection for HAS. Similarly, Fugu [52] was proposed to leverage the hidden Markov model for accurate throughput prediction. Huang et al. [27] used imitation learning to propose Comyco as ABR for on-demand videos. Server-Driven Solutions: These solutions implement a rate control on the server to control a client’s ABR decisions im- plicitly or explicitly.

**Fragmento 16 - p. 2 - score 3:**

In addition, Ahaggar quickly converges to the best solution during the training process with an improvement of 5.6× in terms of the number of epochs required and 6× speedup on the training time compared to the recent RL-based solutions such as [35], [52]. This paper is an extended version of Ahaggar [14], focusing on three main areas that remain open: 1) We conducted more experimental evaluations to assess the performance of Ahaggar in more challenging scenarios, especially in a heterogeneous environment that includes both Ahaggar and non-Ahaggar clients with different network conditions and device resolutions. 2) We investigated the impact of device resolution on Ahag- gar QoE enhancement.

**Fragmento 17 - p. 3 - score 3:**

Inparticular,weuseacentralizedtraining with decentralized execution (CTDE) paradigm [56] to train the MARL agents. CTDE allows these agents to train decentralized policies with global information during training and to make decisions based on the individually learned policies during inference. We also use MAML [23], the meta-RL algorithm, to adapt to various network environments through parameter learning. The overall workﬂow of Ahaggar is shown in Fig. 2, where the steps are numbered as 1⃝– 8⃝. A. Formulation of the Problem At each segment download time epoch t, Ahaggar performs the bitrate guidance tasks (denoted by Z) by selecting the best bitrate (denoted by lc t) with respect to the current state (denoted by sc t) of each client c.

**Fragmento 18 - p. 5 - score 3:**

rc t = ω1 × qc t(lc t) −ω2 × rdc t −ω3 × rcc t −ω4 × qoc t −ω5 × qsc t, (2) where qc t(lc t) maps the selected bitrate to the quality perceived (VMAF) [11], [53], qoc t = |qc t(lc t) −qc t−1(lc t−1)|, qsc t = qoc t/20, and ωi are the coefﬁcients of the reward function. Herein, following prior works [27], [50], we set qsc t as the difference of 20 in VMAF values of two consecutive segments. This QoE model is developed based on linear regression on two datasets: Comyco [27] and Waterloo SQoE-IV [22], where 70% of the data is used for training and 30% for testing. We followed the same setup to tune the coefﬁcients and our results show that ω1 = 0.077, ω2 = 1.249, ω3 = 2.877, ω4 = 0.049, and ω5 = 1.436 achieve the best trade-off between the ﬁve QoE metrics.

**Fragmento 19 - p. 6 - score 3:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10383 via a stochastic gradient ascent using (5). θπc ←θπc + α Tθ  t=1 A πc θ t (bc t, ac t) ▽θ log πc θ(ac t, bc t) + β E, (5) where Tθ is the update interval, α is the learning rate and β is the entropy parameter that is set to a large value at the beginning of the training to encourage exploration and decreases over time to emphasize improving rewards. To calculate the advantage A(bc t, ac t) for a given experience, we have to estimate the value function V πc θ(b). This estimation is performed by the critic network that makes an objective assessment for all the states ∀bc t ∈B of an agent c during the training.

**Fragmento 20 - p. 7 - score 3:**

With this result, we ﬁnd DPPO is the best ﬁt for Ahaggar out of existing policy update techniques. B. Why MAML? We compare the performance of Ahaggar with MAML against Ahaggar with different well-known meta-RL ap- proaches [26]: PEARL, RL2, REPTILE, ANIL, and IMPALA. r PEARL uses the SAC policy for meta-training and adapts to new environments by performing inference over a latent context variable on which the policy is conditioned. r RL2 tries to structure the RL agent as a recurrent neural network(RNN),whichreceivesobservations,pastrewards, and actions, and retains its state across episodes in a given environment. Particularly, RL2 is encoded inside the weights of an RNN, which are learned slowly through a vanilla off-policy RL algorithm.

**Fragmento 21 - p. 7 - score 3:**

After that, these agents send the calculated gradients to the chief, which in turn merges them via agents’ loss functions and the outer loop’s learning rate β. Formally, we deﬁne a meta-objective (Lmeta(θ)) as Tπc θ t=1 LSGD Evti (fθiκ). The optimization of L is called the outer-loop update. The resulting update for θ is given by (9). θ = θ −β ▽θ Tπc θ  t=1 LSGD Evti (fθiκ, Di κ), (9) where the update is performed using SGD, β is a learning rate and LSGD Evti denotes the loss on the environment Evti. C. Ahaggar Meta-Testing (Online) The objective of Ahaggar is to learn how to adapt to hetero- geneous network environments during the online phase through continual learning enabled by MAML.

**Fragmento 22 - p. 8 - score 3:**

However, they all, including ANIL, require more train- ing time and episodes to converge. REPTILE fails to converge and struggles to adapt/generalize to different environments. To sum up, this result suggests the effectiveness of MAML against its baselines. C. Number of Shots and Learning Episodes Although considering more trajectories X (or shots) results in increased improvement in sampling efﬁciency, it generates more computation cost overhead, which can hinder the performance of the trained model and its generalization during inference. A good solution should make a trade-off between sampling efﬁciency, model generalization/convergence and computation cost overhead.


### 8.6. datos trazas datasets

Palabras clave usadas: `dataset, trace, traces, network trace, bandwidth trace, FCC, HSDPA, Norway, LTE, 4G, WiFi, Puffer, Starlink, cellular, synthetic, simulation, testbed, Mahimahi, live streaming, real-world, stream-years, users, sessions, heavy-tailed, CMCD, CMSD`

**Fragmento 1 - p. 4 - score 7:**

B. Ahaggar Meta-Training (Ofﬂine) To train the Ahaggar meta-model, we use Park [34]—a Python-based segment-level simulator that is based on OpenAI and state-of-the-art ABR simulators [46] for RL-based model training. This simulator faithfully emulates a streaming session where the learning agent uses a large corpus of real-world net- work and content traces to explore the streaming environment. ▷Network Traces. We used the Belgium 4G/LTE [51], Nor- way 4G/LTE [43], NYU LTE [36] and Lumous 4G/5G [39] datasets. Each trace entry consists of a throughput value (Mbps), round-trip time (RTT; ms) and packet loss (%). ▷Content Traces. We used the Comyco [27] and Waterloo SQoE-IV [22] datasets.

**Fragmento 2 - p. 9 - score 6:**

These traces were extracted from the 20% of network datasets for testing (Belgium 4G/LTE [51], NYU LTE [36], Lumous 4G/5G [39]). We randomly extracted six network traces from each dataset where the inter-variation duration between the bandwidth values was ﬁxed to ﬁve seconds. Further char- acteristics of the traces are given in supplementary materials (Appendix A), available online. 3) ABRSchemes: WecomparedAhaggaragainstheuristics such as throughput-based (TH), buffer-based (BOLA) and Dynamic (TH+BOLA) from dash.js [20] and RobustMPC [53] and one learning-based scheme: Pensieve [35]. The heuristic-based schemes were tuned and Pensieve was retrained with our datasets and QoE metrics to ﬁt each experiment.

**Fragmento 3 - p. 11 - score 6:**

It also achieved higher O.35 (Visual Quality Score, not shown) scores with values ranging between 4.60 and 4.94. These results conﬁrm how well Ahaggar performs to balance the QoEitu metrics. Second, the Belgium 4G/LTE dataset has the lowest bandwidth values in its network traces. Therefore, all ABR schemes achieved the lowest scores in terms of O.23, O.35 and O.46. Nonetheless, since Ahaggar has been designed to adapt quickly to challenging network conditions (thanks to MAML), it was able to obtain the best O.23 (2.37) and O.46 (2.70) scores. Although other baselines achieved a comparable O.35 score (not shown), they faced frequent and long rebuffering events due to their greedy bitrate selection strategy.

**Fragmento 4 - p. 11 - score 5:**

6(a): 22.28% (44.73%), Belgium 4G/LTE Fig. 6(b): 49.49% (37.06%), NYU LTE Fig. 6(c): 55.04% (85.08%), Lumous 5G Fig. 6(d): 8.01% (31.10%)] and lowest average rebuffering duration with a reduction of 62.81% (84.36%) across all network traces, compared to heuristic-based (learning-based) ABR schemes. Compared to Ahaggar, Dynamic achieved the second-best average results in terms of the QoE and rebuffering duration. This is because of the Dynamic design that combines the beneﬁts of BOLA and TH by switching between both in runtime based on the stability of the current buffer level. However, Pensieve, followed by RobustMPC, suffered from low QoE and long RD due to wrong ABR decisions.

**Fragmento 5 - p. 12 - score 5:**

7(a): 109.80% (114.92%), Belgium 4G/LTE Fig. 7(b): 74.30% (90.16%), NYU LTE Fig. 7(c): 104.20% (114.14%), Lumous 5G Fig. 7(d): 10.69% (10.87%)] and lowest average rebuffering duration with areductionof[Lumous4GFig.7(a):93.58%(95.40%),Belgium 4G/LTE Fig. 7(b): 87.08% (98.74%), NYU LTE Fig. 7(c): 95.03% (98.75%), Lumous 5G Fig. 7(d): 1.57% (20.96%)], compared to the heuristic-based (learning-based) ABR schemes. The performance gains are most prominent in Lumous 4G, Belgium 4G/LTE and NYU LTE, which is also evident in Fig. 7(a)–(c) where Ahaggar is placed much further ahead of the other schemes. From the detailed analysis of the QoEitu scores in Table V, we see that Ahaggar achieved the highest average O.23 and O.46 scores for all network traces with an average improvement Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 6 - p. 13 - score 5:**

The results are presented in Table VI. From the results, we can see that Ahaggar is still able to showcase its DR awareness by selecting the lowest average bitrates for phone, followed by HDTV, and the highest average bitrates for UHDTV across all network traces (except for Belgium 4G/LTE where the average selected bitrate for phone and HDTV are comparable). This validates its DR awareness capabilities in both client-side and server-side network emulation scenarios. G. Results for Multiple Mixed-ABR Clients (Scenario C) In this scenario, we ran Dynamic and Ahaggar clients concurrently (three clients each giving six clients in total) to TABLE VI AVERAGE QOE itu (O.46) SCORES AND ITS METRICS PRODUCED BY Ahaggar RUNNING ON DEVICES WITH DIFFERENT RESOLUTIONS FOR SCENARIO B2 TABLE VII AVERAGE RESULTS OF QOE itu (O.46) AND VMAF PRODUCED BY DYNAMIC CLIENTS WHEN RAN CONCURRENTLY WITH AND WITHOUT Ahaggar CLIENTS UNDER DIFFERENT NETWORK TRACES FOR SCENARIO C study the effect of introducing new Ahaggar clients to a pool of existing non-Ahaggar clients.

**Fragmento 7 - p. 13 - score 5:**

The average QoEitu (O.46) and VMAF results are presented in Table VII. From the results, we can see that Dynamic clients in the mixed-ABR environments that also contain Ahaggar clients performed bet- ter than the Dynamic clients in the Dynamic-only environment for all network traces except Belgium 4G/LTE. Speciﬁcally, the Dynamic clients that ran concurrently with Ahaggar-UHDTV (Ahaggar-HDTV)clientsachievedimprovementsinQoEitu of [Lumous 4G: 12.36% (21.21%), NYU LTE: 6.87% (13.28%), Lumous 5G: 14.15% (13.21%)], while keeping VMAF con- sistent (within 0.19% (0.08%)) across these network traces, when compared against the Dynamic clients in Dynamic-only environment.

**Fragmento 8 - p. 2 - score 4:**

CMCD deﬁnes a set of information collected by a media client and sent along with the HTTP requests to the server running Ahaggar in query arguments or header extensions. CMSD allows the server to 1A highland region in the central Sahara in southern Algeria. convey Ahaggar bitrate guidance decisions to media clients through the HTTP response headers. We evaluate the performance of Ahaggar against several ABR solutions by running real-world trace-driven experiments. These experiments cover multiple clients with heterogeneous network conditions and device resolutions. Experimental re- sults show that Ahaggar delivers consistent quality, improves viewer QoE by up to 87.0%, reduces rebuffering duration by up to 84.4% and reduces bandwidth consumption by up to 62.6%.

**Fragmento 9 - p. 9 - score 4:**

These tags represent the segment sizes and VMAF scores for phone, HDTV and UHDTV, respectively. The VMAF scores were computed using different VMAF models depending on the device resolution. We provide a sample manifest ﬁle in [2]. B. Methodology and Evaluation Setup 1) Video Sample and Parameters: The HTTP server hosted the 4K DASH dataset [41] that was not used in training. We encoded the 636 seconds long Big Buck Bunny (BBB) into four- second segments in FFmpeg using the H.264 codec at 30 fps and in 13 bitrates/resolutions. Further characteristics of BBB are given in supplementary materials (Appendix B), available online. 2) Network Traces: We used network traces with different user mobility (bus, walking, car, train, bicycle, tram, ferry and driving) to throttle the bandwidth between the server and clients.

**Fragmento 10 - p. 10 - score 4:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10387 TABLE III AVERAGE RESULTS OF THE QOE AND ITS METRICS FOR DIFFERENT NETWORK TRACES FOR SCENARIO A1 headless mode enabled using Puppeteer (https://pptr.dev/). The maximum playback buffer level was kept at the default value of 20 seconds. For network emulation, we used tc NetEm (https: //man7.org/linux/man-pages/man8/tc-netem.8.html) to throttle the total bandwidth available to the clients according to the network traces described in Section V-B2. We adopted two types of network emulations: (i) in server-side network emulation, the throttling is done on the server port so that all sessions share a single network trace, and (ii) in client-side network emulation, the throttling is done within each client’s Docker container so that session-speciﬁc network traces are used for each session.

**Fragmento 11 - p. 11 - score 4:**

It is worth mentioning that all schemes faced a few rebuffering events in Lumous 5G because sometimes the bandwidth dropped signiﬁcantly and suddenly (caused by the handoffs to 4G). This is a behavior known in 5G networks operating in higher frequencies [39]. To understand how QoEitu (Mode 0) is computed for each session, Table III (the eighth and ninth columns) highlights the scores of its essential metrics (O.23: Rebufﬁng Duration Score and O.46: Overall Score) for different ABR schemes. The score of each metric is given in the MOS range of one to ﬁve. Here, we deduce three important thrusts. First, Ahaggar outperformed the baselines, achieving the best O.23 and O.46 scores for all network traces with an average improvement of 67.55% (heuristic-based: 60.75%, learning-based: 94.75%) TABLE IV AVERAGE QOE itu (O.46) SCORES AND ITS METRICS PRODUCED BY Ahaggar RUNNING ON DEVICES WITH DIFFERENT RESOLUTIONS FOR SCENARIO B1 and 36.86% (heuristic-based: 33.70%, learning-based: 49.49%) across all network traces, respectively.

**Fragmento 12 - p. 11 - score 4:**

10388 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024 Fig. 6. Avg. QoE itu (O.46) and avg. rebuffering duration ratio in various network traces for Scenario A1. The bottom (left) edge, mark and top (right) edge indicate the average−std, average and average + std, respectively, with a 95% conﬁdence interval. average pUHD, but it performed poorly in most other metrics. In thesamecontext,BOLAfailedtodelivergoodvideoqualitywith inferior VMAF scores, and RobustMPC suffered from frequent and long rebuffering events. Similarly, Ahaggar achieved the highest average QoEitu and lowest average rebuffering duration (see Fig. 6). In detail, Ahaggar achieved the highest average QoE with an improvement of [Lumous 4G Fig.

**Fragmento 13 - p. 11 - score 4:**

Third, Dynamic was the runner-up, receiving the second-best results in terms of O.23 and O.46. Unexpectedly, Pensieve failed to produce good ABR decisions, leading to multiple rebuffering events that contributed to the lowest O.23 score, which impacted O.46 negatively in most network traces. WealsoconductedacomparisonbetweenQoEitu andQoElin. We ﬁrst normalized both values (Section V-B4) and the com- parison between different ABR schemes for various network traces is listed in the last column of Table III. In each network trace, Ahaggar achieved the highest and most consistent per- formance in terms of N-QoEitu and N-QoElin (only in NYU LTE, TH and Dynamic were slightly better) compared to other ABR schemes.

**Fragmento 14 - p. 12 - score 4:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10389 TABLE V AVERAGE RESULTS OF THE QOE AND ITS METRICS FOR DIFFERENT NETWORK TRACES FOR SCENARIO A2 Ahaggar picked a higher bitrate on the average for a UHDTV compared to an HDTV and a phone. For instance, it selected 1.5x-2x higher bitrate for UHDTV compared to the phone with almost a 1-JND difference between the VMAF scores for various network traces. This is because devices with a phone-like res- olution can achieve the highest VMAF score (95-98) requiring only half of the bitrate that a UHDTV requires. We note that the VMAF score differences at a similar bitrate level (e.g., phone versus HDTV in NYU LTE) are due to the different per-device VMAF models used to calculate the scores.

**Fragmento 15 - p. 12 - score 4:**

This leads to large bandwidth savings as indicated by the average TD performance. We also note that Lumous 5G contains the least challenging traces with the highest bandwidth range compared to the other three sets of traces, and hence, its results do not show the same signiﬁcant improvements in the rebufferingperformance(speciﬁcallyinaverageRDandaverage RC) of Ahaggar when compared against the other schemes. From Fig. 7, we can also see that Ahaggar achieved the highest average QoEitu across all network traces and lowest average rebuffering duration in all traces except Lumous 5G. Speciﬁcally, Ahaggar achieved the highest average QoEitu with an improvement of [Lumous 4G Fig.

**Fragmento 16 - p. 14 - score 4:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10391 Dynamic clients in mixed-ABR environments). We note that Belgium 4G/LTE contains the most challenging traces with the lowest bandwidth range than the other three sets of traces, and under these extreme network conditions, the Dynamic clients were selecting much lower video bitrates that coincided with the levels of bitrate selected by the Ahaggar clients. Hence, in Belgium 4G/LTE, the introduction of Ahaggar clients did not affect the amount of data transmitted over the network which explains the absence of performance gains as seen in the other sets of traces.

**Fragmento 17 - p. 9 - score 3:**

10386 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024 TABLE II Ahaggar TRAINING/TESTING PARAMETERS guidance decisions. Another notable observation is that Fugu and Pensieve do not leverage meta-learning techniques. Thus, it takes longer for them to converge. V. PERFORMANCE EVALUATION A. Ahaggar Implementation 1) Choice of Ahaggar Parameters: To train the Ahag- gar model, we used a total of 2000 traces (1500 network and 500 content) from different datasets as described in Sec- tion III-B. We randomized them and then used 80% for training and 20% for testing. With an 80–20 train-test split, we per- formed a 5-fold walk-forward cross-validation on each dataset.

**Fragmento 18 - p. 9 - score 3:**

Training parameters can impact the performance of Ahag- gar, so we empirically set the parameters as summarized in Table II. 2) Ofﬂine Training: To train the Ahaggar meta-model, we used a customized trace-based segment-level Gym simu- lator based on Park [34]. This simulator was implemented in Python 3.6 to simulate a typical HAS system based on real- world network and content traces. We used TFLearn 1.5.0 [48], RLlib of Ray 1.12.0 [32] and TensorFlow 2.4.0 to implement Ahaggar’s NN architecture and build the training workﬂow. 3) Online Testing: To test Ahaggar, we implemented a CMCD/SD-enabled streaming system [2] with Ahaggar’s bi- trate guidance functions.

**Fragmento 19 - p. 10 - score 3:**

In general, Ahaggar gained the best possible performance in terms of RC, RD and TD without sacriﬁcing the VMAF score compared to other baselines in all network traces. Looking at the averages across all the network traces, we see that Ahag- gar reduced average RD by 62.81% (84.36%), average RC by 53.52% (71.18%) and average TD by 53.27% (59.34%), compared to the heuristic-based (learning-based) ABR schemes. In addition, Ahaggar signiﬁcantly reduced the number of times a UHD segment was picked when there was no noticeable VMAF score difference compared to the other best-performing schemes (RobustMPC and Dynamic) across all network traces. Such reduction translates to signiﬁcant bandwidth savings (see the Avg.

**Fragmento 20 - p. 10 - score 3:**

r Scenario C: The six clients contain a mix of ABR schemes: three Dynamic and three Ahaggar clients. This scenario evaluates the impact of introducing Ahaggar clients amongst clients that do not use Ahaggar. Client-side network emulation is used. Details of the network traces used in each scenario are given in supplementary materials (Appendix A), available online. C. Results for Multiple Identical Clients (Scenario A1) For each ABR scheme, we ran multiple UHDTV clients. Table III shows the total QoE and detailed breakdown of each QoE metric for each ABR scheme for various network traces. We provide the average and standard deviation values for six clients and over ﬁve runs in the format of average ± std.

**Fragmento 21 - p. 12 - score 3:**

E. Results for Multiple Identical Clients With Shared Network Trace (Scenario A2) Similar to Scenario A1, we ran six UHDTV clients for each ABR scheme in this scenario. However, in contrast to the client- side network emulation used in Scenario A1, the clients in each ABR scheme here share the same network trace via server-side network emulation, which allows us to evaluate the performance when the network is constrained at the server-end (before the streams propagate to the downstream links that separate the clients). Table V shows the total QoE and detailed breakdown of each QoE metric for each ABR scheme for various network traces. Generally speaking, with the exception of Lumous 5G, Ahaggar achieved the best performance in terms of RC, RD and TD with a much smaller trade-off in VMAF as compared to the other ABR schemes.

**Fragmento 22 - p. 12 - score 3:**

Speciﬁcally, the averages computed across all the network traces show that Ahaggar reduced average RD by 91.10% (97.95%), average RC by 83.85% (91.47%) and average TD by 66.55% (70.90%) compared to the heuristic-based (learning-based) ABR schemes. In contrast, the average VMAF scores only dropped by 4.24% (5.54%) compared to the heuristic-based (learning-based) ABR schemes (or 4.00 (5.12) in absolute values which is less than a 1-JND difference as compared to the other schemes). Moreover, Ahag- gar picked a signiﬁcantly lower percentage of UHD segments, speciﬁcally, a reduction of 41.80% (43.66%) compared to the heuristic-based (learning-based) ABR schemes, while keeping to within 1-JND difference in VMAF scores across all network traces.


### 8.7. evaluacion baselines experimentos

Palabras clave usadas: `evaluation, experiment, baseline, compare, comparison, Pensieve, BBA, BOLA, MPC, RobustMPC, FastMPC, Rate-based, Comyco, Oboe, A2BR, Fugu, Puffer, Ahaggar, Gelato, Plume, results, performance, ablation`

**Fragmento 1 - p. 9 - score 7:**

These traces were extracted from the 20% of network datasets for testing (Belgium 4G/LTE [51], NYU LTE [36], Lumous 4G/5G [39]). We randomly extracted six network traces from each dataset where the inter-variation duration between the bandwidth values was ﬁxed to ﬁve seconds. Further char- acteristics of the traces are given in supplementary materials (Appendix A), available online. 3) ABRSchemes: WecomparedAhaggaragainstheuristics such as throughput-based (TH), buffer-based (BOLA) and Dynamic (TH+BOLA) from dash.js [20] and RobustMPC [53] and one learning-based scheme: Pensieve [35]. The heuristic-based schemes were tuned and Pensieve was retrained with our datasets and QoE metrics to ﬁt each experiment.

**Fragmento 2 - p. 11 - score 7:**

6(a): 22.28% (44.73%), Belgium 4G/LTE Fig. 6(b): 49.49% (37.06%), NYU LTE Fig. 6(c): 55.04% (85.08%), Lumous 5G Fig. 6(d): 8.01% (31.10%)] and lowest average rebuffering duration with a reduction of 62.81% (84.36%) across all network traces, compared to heuristic-based (learning-based) ABR schemes. Compared to Ahaggar, Dynamic achieved the second-best average results in terms of the QoE and rebuffering duration. This is because of the Dynamic design that combines the beneﬁts of BOLA and TH by switching between both in runtime based on the stability of the current buffer level. However, Pensieve, followed by RobustMPC, suffered from low QoE and long RD due to wrong ABR decisions.

**Fragmento 3 - p. 10 - score 6:**

In general, Ahaggar gained the best possible performance in terms of RC, RD and TD without sacriﬁcing the VMAF score compared to other baselines in all network traces. Looking at the averages across all the network traces, we see that Ahag- gar reduced average RD by 62.81% (84.36%), average RC by 53.52% (71.18%) and average TD by 53.27% (59.34%), compared to the heuristic-based (learning-based) ABR schemes. In addition, Ahaggar signiﬁcantly reduced the number of times a UHD segment was picked when there was no noticeable VMAF score difference compared to the other best-performing schemes (RobustMPC and Dynamic) across all network traces. Such reduction translates to signiﬁcant bandwidth savings (see the Avg.

**Fragmento 4 - p. 2 - score 5:**

3) We explored the design choices of Ahaggar, including why we used DPPO and MAML as the policy update solution and the meta-RL algorithm, respectively. We also examined the effects of the number of shots, the learning episode and the Ahaggar model convergence. The rest of the paper is organized as follows. Section II shows the existing solutions for QoE optimization. Section III describes the Ahaggar solution, followed by its design choices in Section IV. The performance evaluation in Sections V and VI concludes the paper. II. RELATED WORK Client-Driven Heuristic-Based ABR: These schemes use heuristics based on estimated throughput (e.g., PANDA [31]), buffer level (e.g., BOLA [47]), segment size (e.g., SARA [8]), or a combination (e.g., MPCDASH [53]).

**Fragmento 5 - p. 2 - score 5:**

In addition, Ahaggar quickly converges to the best solution during the training process with an improvement of 5.6× in terms of the number of epochs required and 6× speedup on the training time compared to the recent RL-based solutions such as [35], [52]. This paper is an extended version of Ahaggar [14], focusing on three main areas that remain open: 1) We conducted more experimental evaluations to assess the performance of Ahaggar in more challenging scenarios, especially in a heterogeneous environment that includes both Ahaggar and non-Ahaggar clients with different network conditions and device resolutions. 2) We investigated the impact of device resolution on Ahag- gar QoE enhancement.

**Fragmento 6 - p. 9 - score 5:**

10386 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024 TABLE II Ahaggar TRAINING/TESTING PARAMETERS guidance decisions. Another notable observation is that Fugu and Pensieve do not leverage meta-learning techniques. Thus, it takes longer for them to converge. V. PERFORMANCE EVALUATION A. Ahaggar Implementation 1) Choice of Ahaggar Parameters: To train the Ahag- gar model, we used a total of 2000 traces (1500 network and 500 content) from different datasets as described in Sec- tion III-B. We randomized them and then used 80% for training and 20% for testing. With an 80–20 train-test split, we per- formed a 5-fold walk-forward cross-validation on each dataset.

**Fragmento 7 - p. 11 - score 5:**

Third, Dynamic was the runner-up, receiving the second-best results in terms of O.23 and O.46. Unexpectedly, Pensieve failed to produce good ABR decisions, leading to multiple rebuffering events that contributed to the lowest O.23 score, which impacted O.46 negatively in most network traces. WealsoconductedacomparisonbetweenQoEitu andQoElin. We ﬁrst normalized both values (Section V-B4) and the com- parison between different ABR schemes for various network traces is listed in the last column of Table III. In each network trace, Ahaggar achieved the highest and most consistent per- formance in terms of N-QoEitu and N-QoElin (only in NYU LTE, TH and Dynamic were slightly better) compared to other ABR schemes.

**Fragmento 8 - p. 13 - score 5:**

Similar to the results in Scenario A1, Dynamic achieved the second-best results in terms of average O.23 and O.46 scores, while Pensieve experienced multiple rebuffering events that led to the lowest average O.23 and O.46 scores, averaged across all network traces. Comparing the ﬁndings between Scenario A1 and this scenario (Scenario A2), we can see that they generally share similar observations as to the performance gains Ahaggar achieves compared to the other ABR schemes, which validates its performance in both client-side and server-side network emulation scenarios. F. Results for Multiple Mixed-Device Clients With Shared Network Trace (Scenario B2) Similar to Scenario B1, we ran two clients with each device resolution (DR) (total of six clients) to evaluate the effective- ness of Ahaggar in adapting to different DRs.

**Fragmento 9 - p. 7 - score 4:**

We implemented these techniques in Ahaggar and then ran the experiment with 1,000 agents on the same validation set every 500 episodes and recorded the validation learning curve in Fig. 3. We can see that DPPO achieves the best performance with (i) the highest possible N-QoElin (reward; see Section V-B4) and (ii) trains and converges faster to the highest reward value with only 3,000 episodes, compared to its competitors.DPPOreliesonspecializedclippingintheobjective function (7) to remove incentives for the new policy to get far from the old policy. Hence, it allows robust policy optimization for whole video sessions. Comparing DPPO with TRPO, we observe that TRPO is the runner-up that typically obtains a high reward, but it takes more time (6,000 episodes) to converge to the best achievable reward.

**Fragmento 10 - p. 8 - score 4:**

Table I shows the convergence time, episodes and shots required for a model to generalize and converge to the best solution. We ﬁxed the number of shots to 40 and workers to 1,000 for all meta-RL techniques, including Ahaggar, ANIL, PEARL, and RL2. During the training (80% datasets), Ahaggar is able to converge faster and achieve the best performance with 3,000 episodes (with 2,000 iterations per episode), taking eight hours of training, compared to other solutions. It requires 2x (2x), 4x (3x), 5x (5x), 7x (9x), and 10x (12x) fewer episodes (time) to achieve its best generalization performance compared to ANIL, IMPALA, RL2, Fugu and Pensive, respectively.

**Fragmento 11 - p. 11 - score 4:**

10388 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024 Fig. 6. Avg. QoE itu (O.46) and avg. rebuffering duration ratio in various network traces for Scenario A1. The bottom (left) edge, mark and top (right) edge indicate the average−std, average and average + std, respectively, with a 95% conﬁdence interval. average pUHD, but it performed poorly in most other metrics. In thesamecontext,BOLAfailedtodelivergoodvideoqualitywith inferior VMAF scores, and RobustMPC suffered from frequent and long rebuffering events. Similarly, Ahaggar achieved the highest average QoEitu and lowest average rebuffering duration (see Fig. 6). In detail, Ahaggar achieved the highest average QoE with an improvement of [Lumous 4G Fig.

**Fragmento 12 - p. 12 - score 4:**

E. Results for Multiple Identical Clients With Shared Network Trace (Scenario A2) Similar to Scenario A1, we ran six UHDTV clients for each ABR scheme in this scenario. However, in contrast to the client- side network emulation used in Scenario A1, the clients in each ABR scheme here share the same network trace via server-side network emulation, which allows us to evaluate the performance when the network is constrained at the server-end (before the streams propagate to the downstream links that separate the clients). Table V shows the total QoE and detailed breakdown of each QoE metric for each ABR scheme for various network traces. Generally speaking, with the exception of Lumous 5G, Ahaggar achieved the best performance in terms of RC, RD and TD with a much smaller trade-off in VMAF as compared to the other ABR schemes.

**Fragmento 13 - p. 12 - score 4:**

This leads to large bandwidth savings as indicated by the average TD performance. We also note that Lumous 5G contains the least challenging traces with the highest bandwidth range compared to the other three sets of traces, and hence, its results do not show the same signiﬁcant improvements in the rebufferingperformance(speciﬁcallyinaverageRDandaverage RC) of Ahaggar when compared against the other schemes. From Fig. 7, we can also see that Ahaggar achieved the highest average QoEitu across all network traces and lowest average rebuffering duration in all traces except Lumous 5G. Speciﬁcally, Ahaggar achieved the highest average QoEitu with an improvement of [Lumous 4G Fig.

**Fragmento 14 - p. 2 - score 3:**

CMCD deﬁnes a set of information collected by a media client and sent along with the HTTP requests to the server running Ahaggar in query arguments or header extensions. CMSD allows the server to 1A highland region in the central Sahara in southern Algeria. convey Ahaggar bitrate guidance decisions to media clients through the HTTP response headers. We evaluate the performance of Ahaggar against several ABR solutions by running real-world trace-driven experiments. These experiments cover multiple clients with heterogeneous network conditions and device resolutions. Experimental re- sults show that Ahaggar delivers consistent quality, improves viewer QoE by up to 87.0%, reduces rebuffering duration by up to 84.4% and reduces bandwidth consumption by up to 62.6%.

**Fragmento 15 - p. 2 - score 3:**

Client-Driven Learning-Based ABR: These schemes learn from the streaming environment by training an NN using DRL techniques [6], [17]. Mao et al. [35] proposed Pensieve, the ﬁrst learning ABR that used DRL to generate a strategy toward maximizing the viewer QoE. Bentaleb et al. [10] designed AMP that implemented a set of learning-based bandwidth predictors and model auto-selection for HAS. Similarly, Fugu [52] was proposed to leverage the hidden Markov model for accurate throughput prediction. Huang et al. [27] used imitation learning to propose Comyco as ABR for on-demand videos. Server-Driven Solutions: These solutions implement a rate control on the server to control a client’s ABR decisions im- plicitly or explicitly.

**Fragmento 16 - p. 7 - score 3:**

r DDPG is an off-policy algorithm that combines DQN and actor-critic algorithms to use deterministic policy gradients for updating the policy via a DL approach. r SAC is an off-policy algorithm that combines stochastic policy optimization and DDPG-style approaches. It incor- porates the clipped double-Q trick and entropy regulariza- tion. r TD3 is an off-policy algorithm that introduces clipped dou- ble Q-learning mode and a delayed policy update strategy to solve the overestimation problem of DDPG. r Random is an algorithm that chooses an action randomly. To compare the performance of Ahaggar with DPPO against other policy update techniques, we prepared 10% as a validation set from the 20% of the testing set comprising network and video content traces.

**Fragmento 17 - p. 7 - score 3:**

With this result, we ﬁnd DPPO is the best ﬁt for Ahaggar out of existing policy update techniques. B. Why MAML? We compare the performance of Ahaggar with MAML against Ahaggar with different well-known meta-RL ap- proaches [26]: PEARL, RL2, REPTILE, ANIL, and IMPALA. r PEARL uses the SAC policy for meta-training and adapts to new environments by performing inference over a latent context variable on which the policy is conditioned. r RL2 tries to structure the RL agent as a recurrent neural network(RNN),whichreceivesobservations,pastrewards, and actions, and retains its state across episodes in a given environment. Particularly, RL2 is encoded inside the weights of an RNN, which are learned slowly through a vanilla off-policy RL algorithm.

**Fragmento 18 - p. 8 - score 3:**

One interesting observation is that Ahaggar with X = 40 (40- shots) is the best trade-off point, allowing good sampling ef- ﬁciency and convergence to its best generalization performance (highestachievableN-QoElin)muchfaster(comparableto2,500 episodes) within 3,000 episodes, and signiﬁcant reduction in computation cost overhead for both Ahaggar meta-training and meta-testing phases compared to X = 100, X = 80, or X = 60. Therefore, we set X=40 during the meta-training and meta-testing (and meta-validation) phases. More notably, with X = 1 or X = 20, the convergence was very slow (requiring more episodes) compared to X > 20-shots. D. Ahaggar Model Convergence We trained each model on a physical workstation machine with dual 20-core Intel E5-2630 v4 @ 2.20GHz processors, 192 GB memory, and 8 GPUs.

**Fragmento 19 - p. 8 - score 3:**

However, they all, including ANIL, require more train- ing time and episodes to converge. REPTILE fails to converge and struggles to adapt/generalize to different environments. To sum up, this result suggests the effectiveness of MAML against its baselines. C. Number of Shots and Learning Episodes Although considering more trajectories X (or shots) results in increased improvement in sampling efﬁciency, it generates more computation cost overhead, which can hinder the performance of the trained model and its generalization during inference. A good solution should make a trade-off between sampling efﬁciency, model generalization/convergence and computation cost overhead.

**Fragmento 20 - p. 8 - score 3:**

To ﬁnd the best value for X that leads to faster convergence and minimizes the computation cost overhead, we ran an experiment for Ahaggar with various shot values X = {1, 20, 40, 60, 80, 100}. We used the same validation set and setup as above Section IV-A. The meta-validation learning curve for Ahaggar with various shot values is highlighted in Fig. 5. We observe that Ahaggar with X = 100 converges to the best N-QoElin with fewer episodes of 2,500. However, it generates 2x, 4x, and 8x more computation cost overhead Fig. 5. Ahaggar convergence. TABLE I MODEL CONVERGENCE/GENERALIZATION FOR DIFFERENT SOLUTIONS TIME compared to X = 80, X = 60 and X = 40, respectively.

**Fragmento 21 - p. 10 - score 3:**

TD column in Table III). We anticipated these results because Ahaggar makes bitrate guidance decisions based on not only the throughput, buffer level and segment sizes, but also segment quality and device resolution. It also uses MAML for continual learning and fast adaptation to unseen environments. In contrast, other ABR schemes use one or more heuristics or an NN combining these heuristics and they do not necessarily perform well in unseen environments. Fig. 6 and Table III conﬁrm this. For instance, Pensieve achieved the highest average selected bitrate and Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.

**Fragmento 22 - p. 11 - score 3:**

It also achieved higher O.35 (Visual Quality Score, not shown) scores with values ranging between 4.60 and 4.94. These results conﬁrm how well Ahaggar performs to balance the QoEitu metrics. Second, the Belgium 4G/LTE dataset has the lowest bandwidth values in its network traces. Therefore, all ABR schemes achieved the lowest scores in terms of O.23, O.35 and O.46. Nonetheless, since Ahaggar has been designed to adapt quickly to challenging network conditions (thanks to MAML), it was able to obtain the best O.23 (2.37) and O.46 (2.70) scores. Although other baselines achieved a comparable O.35 score (not shown), they faced frequent and long rebuffering events due to their greedy bitrate selection strategy.


### 8.8. resultados numericos

Palabras clave usadas: `improve, improvement, outperform, gain, %, QoE gain, higher, lower, average, result, achieve, compared to, reduce, decrease, increase, stall time, stream-years, users, ms, latency`

**Fragmento 1 - p. 12 - score 7:**

7(a): 109.80% (114.92%), Belgium 4G/LTE Fig. 7(b): 74.30% (90.16%), NYU LTE Fig. 7(c): 104.20% (114.14%), Lumous 5G Fig. 7(d): 10.69% (10.87%)] and lowest average rebuffering duration with areductionof[Lumous4GFig.7(a):93.58%(95.40%),Belgium 4G/LTE Fig. 7(b): 87.08% (98.74%), NYU LTE Fig. 7(c): 95.03% (98.75%), Lumous 5G Fig. 7(d): 1.57% (20.96%)], compared to the heuristic-based (learning-based) ABR schemes. The performance gains are most prominent in Lumous 4G, Belgium 4G/LTE and NYU LTE, which is also evident in Fig. 7(a)–(c) where Ahaggar is placed much further ahead of the other schemes. From the detailed analysis of the QoEitu scores in Table V, we see that Ahaggar achieved the highest average O.23 and O.46 scores for all network traces with an average improvement Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 2 - p. 12 - score 7:**

This leads to large bandwidth savings as indicated by the average TD performance. We also note that Lumous 5G contains the least challenging traces with the highest bandwidth range compared to the other three sets of traces, and hence, its results do not show the same signiﬁcant improvements in the rebufferingperformance(speciﬁcallyinaverageRDandaverage RC) of Ahaggar when compared against the other schemes. From Fig. 7, we can also see that Ahaggar achieved the highest average QoEitu across all network traces and lowest average rebuffering duration in all traces except Lumous 5G. Speciﬁcally, Ahaggar achieved the highest average QoEitu with an improvement of [Lumous 4G Fig.

**Fragmento 3 - p. 13 - score 7:**

The average QoEitu (O.46) and VMAF results are presented in Table VII. From the results, we can see that Dynamic clients in the mixed-ABR environments that also contain Ahaggar clients performed bet- ter than the Dynamic clients in the Dynamic-only environment for all network traces except Belgium 4G/LTE. Speciﬁcally, the Dynamic clients that ran concurrently with Ahaggar-UHDTV (Ahaggar-HDTV)clientsachievedimprovementsinQoEitu of [Lumous 4G: 12.36% (21.21%), NYU LTE: 6.87% (13.28%), Lumous 5G: 14.15% (13.21%)], while keeping VMAF con- sistent (within 0.19% (0.08%)) across these network traces, when compared against the Dynamic clients in Dynamic-only environment.

**Fragmento 4 - p. 10 - score 6:**

In general, Ahaggar gained the best possible performance in terms of RC, RD and TD without sacriﬁcing the VMAF score compared to other baselines in all network traces. Looking at the averages across all the network traces, we see that Ahag- gar reduced average RD by 62.81% (84.36%), average RC by 53.52% (71.18%) and average TD by 53.27% (59.34%), compared to the heuristic-based (learning-based) ABR schemes. In addition, Ahaggar signiﬁcantly reduced the number of times a UHD segment was picked when there was no noticeable VMAF score difference compared to the other best-performing schemes (RobustMPC and Dynamic) across all network traces. Such reduction translates to signiﬁcant bandwidth savings (see the Avg.

**Fragmento 5 - p. 11 - score 6:**

It is worth mentioning that all schemes faced a few rebuffering events in Lumous 5G because sometimes the bandwidth dropped signiﬁcantly and suddenly (caused by the handoffs to 4G). This is a behavior known in 5G networks operating in higher frequencies [39]. To understand how QoEitu (Mode 0) is computed for each session, Table III (the eighth and ninth columns) highlights the scores of its essential metrics (O.23: Rebufﬁng Duration Score and O.46: Overall Score) for different ABR schemes. The score of each metric is given in the MOS range of one to ﬁve. Here, we deduce three important thrusts. First, Ahaggar outperformed the baselines, achieving the best O.23 and O.46 scores for all network traces with an average improvement of 67.55% (heuristic-based: 60.75%, learning-based: 94.75%) TABLE IV AVERAGE QOE itu (O.46) SCORES AND ITS METRICS PRODUCED BY Ahaggar RUNNING ON DEVICES WITH DIFFERENT RESOLUTIONS FOR SCENARIO B1 and 36.86% (heuristic-based: 33.70%, learning-based: 49.49%) across all network traces, respectively.

**Fragmento 6 - p. 11 - score 6:**

6(a): 22.28% (44.73%), Belgium 4G/LTE Fig. 6(b): 49.49% (37.06%), NYU LTE Fig. 6(c): 55.04% (85.08%), Lumous 5G Fig. 6(d): 8.01% (31.10%)] and lowest average rebuffering duration with a reduction of 62.81% (84.36%) across all network traces, compared to heuristic-based (learning-based) ABR schemes. Compared to Ahaggar, Dynamic achieved the second-best average results in terms of the QoE and rebuffering duration. This is because of the Dynamic design that combines the beneﬁts of BOLA and TH by switching between both in runtime based on the stability of the current buffer level. However, Pensieve, followed by RobustMPC, suffered from low QoE and long RD due to wrong ABR decisions.

**Fragmento 7 - p. 13 - score 6:**

Similar to the results in Scenario A1, Dynamic achieved the second-best results in terms of average O.23 and O.46 scores, while Pensieve experienced multiple rebuffering events that led to the lowest average O.23 and O.46 scores, averaged across all network traces. Comparing the ﬁndings between Scenario A1 and this scenario (Scenario A2), we can see that they generally share similar observations as to the performance gains Ahaggar achieves compared to the other ABR schemes, which validates its performance in both client-side and server-side network emulation scenarios. F. Results for Multiple Mixed-Device Clients With Shared Network Trace (Scenario B2) Similar to Scenario B1, we ran two clients with each device resolution (DR) (total of six clients) to evaluate the effective- ness of Ahaggar in adapting to different DRs.

**Fragmento 8 - p. 13 - score 6:**

10390 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024 Fig. 7. Avg. QoE itu (O.46) and avg. rebuffering duration ratio in various network traces for Scenario A2. The bottom (left) edge, mark and top (right) edge indicate the average−std, average and average + std, respectively, with a 95% conﬁdence interval. of 126.23% (143.87%) and 66.14% (73.69%) compared to the heuristic-based (learning-based) ABR schemes, respectively. These results again validate that Ahaggar is able to balance the QoEitu metrics well. This observation is also consistent with the N-QoElin results whereby Ahaggar achieved the best or close to the best N-QoElin scores, ranging between 0.97 and 1.00 (with 1.00 being the highest possible score), in all network traces.

**Fragmento 9 - p. 13 - score 6:**

The performance gain in QoEitu is primarily due to the lower rebuffering duration (not shown in Table VII) where the Dynamic clients in mixed-ABR environments achieved re- duction in average rebuffering duration by [Lumous 4G: 20.05% (30.03%), NYU LTE: 14.49% (11.34%), Lumous 5G: 47.95% (51.42%)] when running concurrently with Ahaggar-UHDTV (Ahaggar-HDTV) clients. This validates that the bandwidth savings brought about by Ahaggar clients have positive spill- over effects on other clients sharing the network as well (as shown by the reduced rebuffering duration experienced by the Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.

**Fragmento 10 - p. 2 - score 5:**

CMCD deﬁnes a set of information collected by a media client and sent along with the HTTP requests to the server running Ahaggar in query arguments or header extensions. CMSD allows the server to 1A highland region in the central Sahara in southern Algeria. convey Ahaggar bitrate guidance decisions to media clients through the HTTP response headers. We evaluate the performance of Ahaggar against several ABR solutions by running real-world trace-driven experiments. These experiments cover multiple clients with heterogeneous network conditions and device resolutions. Experimental re- sults show that Ahaggar delivers consistent quality, improves viewer QoE by up to 87.0%, reduces rebuffering duration by up to 84.4% and reduces bandwidth consumption by up to 62.6%.

**Fragmento 11 - p. 8 - score 5:**

However, they all, including ANIL, require more train- ing time and episodes to converge. REPTILE fails to converge and struggles to adapt/generalize to different environments. To sum up, this result suggests the effectiveness of MAML against its baselines. C. Number of Shots and Learning Episodes Although considering more trajectories X (or shots) results in increased improvement in sampling efﬁciency, it generates more computation cost overhead, which can hinder the performance of the trained model and its generalization during inference. A good solution should make a trade-off between sampling efﬁciency, model generalization/convergence and computation cost overhead.

**Fragmento 12 - p. 8 - score 5:**

We run the same experiment outlined in Section IV-A and the meta-validation learning curve for this experiment is shown in Fig. 4. With 3,000 episodes, we observe that MAML out- performs existing meta-RL approaches in terms of N-QoElin with an average improvement of 57.5% (PEARL: 64.4%, RL2: 65.3%, REPTILE: 79.9%, ANIL: 28.7%, IMPALA: 49.11%). It also converges quickly to the best reward, requiring 3,000 episodes, 2x better than the runner-up approach (ANIL), which shows the effectiveness of MAML in the meta-training phase. ANIL generally performs better than RL2, IMPALA, REPTILE and PEARL, as it is an extension of MAML without inner-loop updates.

**Fragmento 13 - p. 11 - score 5:**

10388 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024 Fig. 6. Avg. QoE itu (O.46) and avg. rebuffering duration ratio in various network traces for Scenario A1. The bottom (left) edge, mark and top (right) edge indicate the average−std, average and average + std, respectively, with a 95% conﬁdence interval. average pUHD, but it performed poorly in most other metrics. In thesamecontext,BOLAfailedtodelivergoodvideoqualitywith inferior VMAF scores, and RobustMPC suffered from frequent and long rebuffering events. Similarly, Ahaggar achieved the highest average QoEitu and lowest average rebuffering duration (see Fig. 6). In detail, Ahaggar achieved the highest average QoE with an improvement of [Lumous 4G Fig.

**Fragmento 14 - p. 12 - score 5:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10389 TABLE V AVERAGE RESULTS OF THE QOE AND ITS METRICS FOR DIFFERENT NETWORK TRACES FOR SCENARIO A2 Ahaggar picked a higher bitrate on the average for a UHDTV compared to an HDTV and a phone. For instance, it selected 1.5x-2x higher bitrate for UHDTV compared to the phone with almost a 1-JND difference between the VMAF scores for various network traces. This is because devices with a phone-like res- olution can achieve the highest VMAF score (95-98) requiring only half of the bitrate that a UHDTV requires. We note that the VMAF score differences at a similar bitrate level (e.g., phone versus HDTV in NYU LTE) are due to the different per-device VMAF models used to calculate the scores.

**Fragmento 15 - p. 12 - score 5:**

Speciﬁcally, the averages computed across all the network traces show that Ahaggar reduced average RD by 91.10% (97.95%), average RC by 83.85% (91.47%) and average TD by 66.55% (70.90%) compared to the heuristic-based (learning-based) ABR schemes. In contrast, the average VMAF scores only dropped by 4.24% (5.54%) compared to the heuristic-based (learning-based) ABR schemes (or 4.00 (5.12) in absolute values which is less than a 1-JND difference as compared to the other schemes). Moreover, Ahag- gar picked a signiﬁcantly lower percentage of UHD segments, speciﬁcally, a reduction of 41.80% (43.66%) compared to the heuristic-based (learning-based) ABR schemes, while keeping to within 1-JND difference in VMAF scores across all network traces.

**Fragmento 16 - p. 2 - score 4:**

In addition, Ahaggar quickly converges to the best solution during the training process with an improvement of 5.6× in terms of the number of epochs required and 6× speedup on the training time compared to the recent RL-based solutions such as [35], [52]. This paper is an extended version of Ahaggar [14], focusing on three main areas that remain open: 1) We conducted more experimental evaluations to assess the performance of Ahaggar in more challenging scenarios, especially in a heterogeneous environment that includes both Ahaggar and non-Ahaggar clients with different network conditions and device resolutions. 2) We investigated the impact of device resolution on Ahag- gar QoE enhancement.

**Fragmento 17 - p. 11 - score 4:**

Third, Dynamic was the runner-up, receiving the second-best results in terms of O.23 and O.46. Unexpectedly, Pensieve failed to produce good ABR decisions, leading to multiple rebuffering events that contributed to the lowest O.23 score, which impacted O.46 negatively in most network traces. WealsoconductedacomparisonbetweenQoEitu andQoElin. We ﬁrst normalized both values (Section V-B4) and the com- parison between different ABR schemes for various network traces is listed in the last column of Table III. In each network trace, Ahaggar achieved the highest and most consistent per- formance in terms of N-QoEitu and N-QoElin (only in NYU LTE, TH and Dynamic were slightly better) compared to other ABR schemes.

**Fragmento 18 - p. 11 - score 4:**

It also achieved higher O.35 (Visual Quality Score, not shown) scores with values ranging between 4.60 and 4.94. These results conﬁrm how well Ahaggar performs to balance the QoEitu metrics. Second, the Belgium 4G/LTE dataset has the lowest bandwidth values in its network traces. Therefore, all ABR schemes achieved the lowest scores in terms of O.23, O.35 and O.46. Nonetheless, since Ahaggar has been designed to adapt quickly to challenging network conditions (thanks to MAML), it was able to obtain the best O.23 (2.37) and O.46 (2.70) scores. Although other baselines achieved a comparable O.35 score (not shown), they faced frequent and long rebuffering events due to their greedy bitrate selection strategy.

**Fragmento 19 - p. 12 - score 4:**

E. Results for Multiple Identical Clients With Shared Network Trace (Scenario A2) Similar to Scenario A1, we ran six UHDTV clients for each ABR scheme in this scenario. However, in contrast to the client- side network emulation used in Scenario A1, the clients in each ABR scheme here share the same network trace via server-side network emulation, which allows us to evaluate the performance when the network is constrained at the server-end (before the streams propagate to the downstream links that separate the clients). Table V shows the total QoE and detailed breakdown of each QoE metric for each ABR scheme for various network traces. Generally speaking, with the exception of Lumous 5G, Ahaggar achieved the best performance in terms of RC, RD and TD with a much smaller trade-off in VMAF as compared to the other ABR schemes.

**Fragmento 20 - p. 2 - score 3:**

We take inputs from the network, clients and streamed content into the Ahaggar neural network (NN) for bitrate guidance. The objective of Ahaggar is to select the minimum bitrate (among the available options) above which the next higher bitrate improves the perceptual quality only insigniﬁcantly at the speciﬁc device resolution. In this study, we use an objective full-reference perceptual video quality metric known as Video Multi-method Assessment Fusion (VMAF) [42]. To ensure healthy cooperation without incurring additional complexities between the clients and servers, Ahaggar adopts the emerging Common Media Client/Server Data standards: CMCD [9], [13], [18] and CMSD [7], [19], [33].

**Fragmento 21 - p. 5 - score 3:**

rc t = ω1 × qc t(lc t) −ω2 × rdc t −ω3 × rcc t −ω4 × qoc t −ω5 × qsc t, (2) where qc t(lc t) maps the selected bitrate to the quality perceived (VMAF) [11], [53], qoc t = |qc t(lc t) −qc t−1(lc t−1)|, qsc t = qoc t/20, and ωi are the coefﬁcients of the reward function. Herein, following prior works [27], [50], we set qsc t as the difference of 20 in VMAF values of two consecutive segments. This QoE model is developed based on linear regression on two datasets: Comyco [27] and Waterloo SQoE-IV [22], where 70% of the data is used for training and 30% for testing. We followed the same setup to tune the coefﬁcients and our results show that ω1 = 0.077, ω2 = 1.249, ω3 = 2.877, ω4 = 0.049, and ω5 = 1.436 achieve the best trade-off between the ﬁve QoE metrics.

**Fragmento 22 - p. 7 - score 3:**

r DDPG is an off-policy algorithm that combines DQN and actor-critic algorithms to use deterministic policy gradients for updating the policy via a DL approach. r SAC is an off-policy algorithm that combines stochastic policy optimization and DDPG-style approaches. It incor- porates the clipped double-Q trick and entropy regulariza- tion. r TD3 is an off-policy algorithm that introduces clipped dou- ble Q-learning mode and a delayed policy update strategy to solve the overestimation problem of DDPG. r Random is an algorithm that chooses an action randomly. To compare the performance of Ahaggar with DPPO against other policy update techniques, we prepared 10% as a validation set from the 20% of the testing set comprising network and video content traces.


### 8.9. limitaciones riesgos

Palabras clave usadas: `limitation, future work, challenge, overhead, complexity, generalization, real-world, deployment, cost, computational, unstable, fail, failure, heterogeneous, bias, biased, unbiased, trace-driven, heavy-tailed, unseen, uncertainty, unpredictable, privacy, fairness`

**Fragmento 1 - p. 1 - score 4:**

Therefore, future states are not easy to predict accurately. Most schemes use classical approaches to train an agent by giving feedback for decisions while interacting with an environment. Such interaction can be efﬁcientlyperformedinacontrolledtrace-drivensimulator. Still, a mismatch may occur when the trained model is deployed in a live system and encounters an environment not previously seen [55]. As a result, the scheme may fail to perform proper rate adaptation. Second, deploying learning-based schemes on devices with scarce resources is impractical due to high storage and computational costs. Prior work [55] showed that a learning model trained on past network scenarios could hardly provide a comparable performance under new conditions, and hence, effective and continual model retraining/update was required.

**Fragmento 2 - p. 8 - score 4:**

However, they all, including ANIL, require more train- ing time and episodes to converge. REPTILE fails to converge and struggles to adapt/generalize to different environments. To sum up, this result suggests the effectiveness of MAML against its baselines. C. Number of Shots and Learning Episodes Although considering more trajectories X (or shots) results in increased improvement in sampling efﬁciency, it generates more computation cost overhead, which can hinder the performance of the trained model and its generalization during inference. A good solution should make a trade-off between sampling efﬁciency, model generalization/convergence and computation cost overhead.

**Fragmento 3 - p. 2 - score 3:**

CMCD deﬁnes a set of information collected by a media client and sent along with the HTTP requests to the server running Ahaggar in query arguments or header extensions. CMSD allows the server to 1A highland region in the central Sahara in southern Algeria. convey Ahaggar bitrate guidance decisions to media clients through the HTTP response headers. We evaluate the performance of Ahaggar against several ABR solutions by running real-world trace-driven experiments. These experiments cover multiple clients with heterogeneous network conditions and device resolutions. Experimental re- sults show that Ahaggar delivers consistent quality, improves viewer QoE by up to 87.0%, reduces rebuffering duration by up to 84.4% and reduces bandwidth consumption by up to 62.6%.

**Fragmento 4 - p. 5 - score 3:**

In PPO, the advantage function is calculated as a function of Gc t and baseline basec t that has an impact on the convergenceofGc t.Priorwork[54]foundthatAπc θ didnotgener- alize well. Hence, in DPPO, we revise the advantage function by using a truncated backpropagation through time with a window of length κ such that Aπc θ(bc t, ac t) = Qπc θ(bc t, ac t) −V πc θ(bc t). Qπc θ is calculated by the actor network, which uses the κ-step Temporal Difference (TD) approach given by: Qπc θ(bc t, ac t) = κ=Θ−1 κ=0 γκrc t+κ + γΘV (bc t+Θ). For each episode, the agent c of the actor network aims to maximize Gc t through maximizing Aπc θ, where it samples a trajectory of bitrate decisions and uses the empirically computed advantage as an unbiased estimate of Aπc θ(bc t, ac t).

**Fragmento 5 - p. 8 - score 3:**

One interesting observation is that Ahaggar with X = 40 (40- shots) is the best trade-off point, allowing good sampling ef- ﬁciency and convergence to its best generalization performance (highestachievableN-QoElin)muchfaster(comparableto2,500 episodes) within 3,000 episodes, and signiﬁcant reduction in computation cost overhead for both Ahaggar meta-training and meta-testing phases compared to X = 100, X = 80, or X = 60. Therefore, we set X=40 during the meta-training and meta-testing (and meta-validation) phases. More notably, with X = 1 or X = 20, the convergence was very slow (requiring more episodes) compared to X > 20-shots. D. Ahaggar Model Convergence We trained each model on a physical workstation machine with dual 20-core Intel E5-2630 v4 @ 2.20GHz processors, 192 GB memory, and 8 GPUs.

**Fragmento 6 - p. 8 - score 3:**

To ﬁnd the best value for X that leads to faster convergence and minimizes the computation cost overhead, we ran an experiment for Ahaggar with various shot values X = {1, 20, 40, 60, 80, 100}. We used the same validation set and setup as above Section IV-A. The meta-validation learning curve for Ahaggar with various shot values is highlighted in Fig. 5. We observe that Ahaggar with X = 100 converges to the best N-QoElin with fewer episodes of 2,500. However, it generates 2x, 4x, and 8x more computation cost overhead Fig. 5. Ahaggar convergence. TABLE I MODEL CONVERGENCE/GENERALIZATION FOR DIFFERENT SOLUTIONS TIME compared to X = 80, X = 60 and X = 40, respectively.

**Fragmento 7 - p. 2 - score 2:**

Therefore, our model can converge quickly to the best performance and adapt to new unseen environments with only a small number of (e.g., 40) shots. To our knowledge, this paper is the ﬁrst study using meta-RL to improve QoE for adaptive streaming clients while cleanly separating the responsibilities for the servers and clients and respecting the client-driven nature of HAS. The Ahaggar solution comprises two phases: (i) (ofﬂine) meta-training, where each RL agent trains the Ahaggar meta- model on heterogeneous network environments, and (ii) (online) meta-testing (also called inference), where each agent contin- ually learns the system dynamics and rapidly optimizes the meta-policy, adjusting the parameter weights that determine the agent behavior according to the trajectories collected from both the meta-training and meta-testing.

**Fragmento 8 - p. 2 - score 2:**

Ahaggar models bitrate guidance tasks for multiple clients as a partially ob- servable Markov decision process (POMDP) and leverages the latest developments in DRL to dynamically adapt to the varying network conditions. Speciﬁcally, it uses advantage Actor-Critic networks (A2C) for model training and Distributed Proximal Policy Optimization (DPPO) [25] with clip and Adam optimizer for policy updates at each time interval. Considering the changes in the environment, we adopt a Model Agnostic Meta-Learning (MAML) [23] on-policy gradient-based meta-RL approach that embeds policy gradient steps into the meta optimization. This al- lows Ahaggar to update the model parameters to achieve good generalization performance on unseen environments during the inference.

**Fragmento 9 - p. 5 - score 2:**

These results are similar to [50]. ▷Policy Gradient and Training Algorithm. The essential objective of Ahaggar is to improve the policy via boosting the probabilities of high-reward samples from the collected trajectories and declining the possibilities of failure samples from the bad trajectories. For every time epoch t, each RL agent c of Ahaggar selects the action ac t that corresponds to the bitrate for the next segment using the improved policy π : πc,⋆ θ (bc t, ac t) →[0, 1] at state bc t, which results in the best accumulated discounted reward that is expressed as Gc t = Tπc θ  ¯t=t γ¯t−t × rc t, ac t = arg max a E [Gc t(bc t, a)] , (3) where Gc t is computed from time t to the end of training, Tπc θ denotes the batch size for updating the gradient policy πc θ, γ ∈[0, 1] is the discount factor, θ is the policy parameter, and πc,⋆ θ (bc t, ac t) is the probability that action ac t is taken in state bc t.

**Fragmento 10 - p. 1 - score 1:**

To make the most out of both worlds, we earlier developed Ahaggar, a learning-based scheme executing on the server side that provides quality-aware bitrate guidance to streaming clients running their own heuristics. Ahaggar’s novelty is the meta reinforcement learning approach taking network condi- tions, clients’ statuses and device resolutions, and streamed content as input features to perform bitrate guidance. Ahaggar uses the new Common Media Client/Server Data (CMCD/SD) protocols to exchange the necessary metadata between the servers and clients. While Ahaggar was a signiﬁcant step forward, in this study, we focus on three open areas, namely, (i) exploring the performance of Ahaggar in a heterogeneous environment including both Ahag- gar and non-Ahaggar clients with varied network conditions and device resolutions, and (ii) quantifying the impact of device resolutions on QoE with Ahaggar.

**Fragmento 11 - p. 1 - score 1:**

Although these schemes are easy to implement, they heavily depend on some conﬁguration parameters, and a poor setting may signiﬁcantly hinder their efﬁcacy [27]. Hence, learning-based schemes have become an alternative, beneﬁting from the latest breakthroughs in machine learning (ML) such as deep reinforcement learning (DRL), and supervised and imitation learning techniques [5]. Learning-basedschemesattaingoodstrategieswithoutrequiring any presumptions about the environment. Nonetheless, learning-based schemes are exposed to two major limitations. First, their performance heavily depends on the training data. Network environments can be quite diverse, and their dynamics change over time.

**Fragmento 12 - p. 1 - score 1:**

We thoroughly investigate these areas and report our ﬁndings. We also (iii) discuss the Ahaggar design choices. Experiments on an open-source system show that Ahaggar adapts to unseen conditions fast and outperforms its competitors in several viewer experience metrics. Index Terms—Adaptive streaming, meta-RL, ABR, CMCD, CMSD, bitrate guidance, quality awareness. I. INTRODUCTION W ITH the prevalence of HTTP adaptive streaming (HAS), the design of adaptive bitrate (ABR) logic—the algo- rithm deciding which segments to download and when (pri- marily based on the advertised encoding bitrate)—has received Manuscript received 22 January 2024; accepted 5 March 2024.

**Fragmento 13 - p. 2 - score 1:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10379 bitrate guidance with perceptual quality and device resolution awareness? ❸How to achieve continual learning for the server- side bitrate guidance? We answer the questions above in the context of Ahaggar,1 a meta reinforcement learning (meta-RL)-based solution. Ahag- gar has a server-side learning model that takes network condi- tions, clients’ statuses, device resolutions and streamed content as input features, and then provides quality and resolution-aware bitrate guidance to the streaming clients. Leveraging the server’s vastcomputationalpower,storagecapacityandmemory,Ahag- gar enables model inference for performing bitrate guidance tasks and helps resource-constrained streaming clients run their lightweight heuristic-based ABR schemes.

**Fragmento 14 - p. 2 - score 1:**

In addition, Ahaggar quickly converges to the best solution during the training process with an improvement of 5.6× in terms of the number of epochs required and 6× speedup on the training time compared to the recent RL-based solutions such as [35], [52]. This paper is an extended version of Ahaggar [14], focusing on three main areas that remain open: 1) We conducted more experimental evaluations to assess the performance of Ahaggar in more challenging scenarios, especially in a heterogeneous environment that includes both Ahaggar and non-Ahaggar clients with different network conditions and device resolutions. 2) We investigated the impact of device resolution on Ahag- gar QoE enhancement.

**Fragmento 15 - p. 4 - score 1:**

These belief states are a sufﬁcient measure of histories and given a belief state bc t, an agent c strives to ﬁnd the effective optimal policy πc,⋆to solve (1) by ﬁnding the best bitrate for each client that maximizes the accumulated discounted reward (denoted by Gc t and deﬁned in Section III-B). The Ahaggar learning model solves the POMDP problem (1) using a multi-agent A2C [6] NN with clipped DPPO [25] and Adam optimizer for policy (π) updates at every time in- terval. For continual learning and quickly adapting to unseen environments, it uses MAML—the meta-RL policy gradient approach—allowing Ahaggar to learn hyper-parameter ini- tialization and speed up the optimization of the learned model during inference.

**Fragmento 16 - p. 4 - score 1:**

B. Ahaggar Meta-Training (Ofﬂine) To train the Ahaggar meta-model, we use Park [34]—a Python-based segment-level simulator that is based on OpenAI and state-of-the-art ABR simulators [46] for RL-based model training. This simulator faithfully emulates a streaming session where the learning agent uses a large corpus of real-world net- work and content traces to explore the streaming environment. ▷Network Traces. We used the Belgium 4G/LTE [51], Nor- way 4G/LTE [43], NYU LTE [36] and Lumous 4G/5G [39] datasets. Each trace entry consists of a throughput value (Mbps), round-trip time (RTT; ms) and packet loss (%). ▷Content Traces. We used the Comyco [27] and Waterloo SQoE-IV [22] datasets.

**Fragmento 17 - p. 5 - score 1:**

10382 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024 dtc t, rsc t, −−→ LSc t , −−→ QT c t }, comprised of network, content and play- back features of the last downloaded segment. These inputs are measured throughput mtpc t (Kbps), VMAF quality qtc t (0–100), current playback buffer length blc t (second), segment size lsc t (KB), download time dtc t (second), percentage of the remaining segments in the video rsc t (%), vector of m available sizes for the next segment −−→ LSc t (KB) and vector of m available VMAF qualities for the next segment −−→ QT c t (0–100). Instead of feeding the A2C NN the exact values of the input state, we normalize them to enable the agent to generalize the strategy better in an unseen network environment [3].

**Fragmento 18 - p. 6 - score 1:**

▷Meta-Learned Policies for Training Algorithm. We adopt the MAML approach, which allows learning model parameters θ via meta-RL, i.e., ﬁnding the model parameters sensitive to changes in the environment, allowing the Ahaggar model to achieve fast adaptation to unseen environments during the inference phase. The training algorithm consists of two loops: (1) Inner Loop. For each episode, each agent c ﬁrst randomly picks a speciﬁc network and content trace as the environment, and sample X ∈D trajectories (also referred to as shots) where D = {(bc 1, ac 1); . . . ; (bc k, ac k)} denotes the set of sampled tra- jectories for inner loop in that environment according to the current policy πc θ.

**Fragmento 19 - p. 8 - score 1:**

Table I shows the convergence time, episodes and shots required for a model to generalize and converge to the best solution. We ﬁxed the number of shots to 40 and workers to 1,000 for all meta-RL techniques, including Ahaggar, ANIL, PEARL, and RL2. During the training (80% datasets), Ahaggar is able to converge faster and achieve the best performance with 3,000 episodes (with 2,000 iterations per episode), taking eight hours of training, compared to other solutions. It requires 2x (2x), 4x (3x), 5x (5x), 7x (9x), and 10x (12x) fewer episodes (time) to achieve its best generalization performance compared to ANIL, IMPALA, RL2, Fugu and Pensive, respectively.

**Fragmento 20 - p. 10 - score 1:**

TD column in Table III). We anticipated these results because Ahaggar makes bitrate guidance decisions based on not only the throughput, buffer level and segment sizes, but also segment quality and device resolution. It also uses MAML for continual learning and fast adaptation to unseen environments. In contrast, other ABR schemes use one or more heuristics or an NN combining these heuristics and they do not necessarily perform well in unseen environments. Fig. 6 and Table III conﬁrm this. For instance, Pensieve achieved the highest average selected bitrate and Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.

**Fragmento 21 - p. 11 - score 1:**

10388 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024 Fig. 6. Avg. QoE itu (O.46) and avg. rebuffering duration ratio in various network traces for Scenario A1. The bottom (left) edge, mark and top (right) edge indicate the average−std, average and average + std, respectively, with a 95% conﬁdence interval. average pUHD, but it performed poorly in most other metrics. In thesamecontext,BOLAfailedtodelivergoodvideoqualitywith inferior VMAF scores, and RobustMPC suffered from frequent and long rebuffering events. Similarly, Ahaggar achieved the highest average QoEitu and lowest average rebuffering duration (see Fig. 6). In detail, Ahaggar achieved the highest average QoE with an improvement of [Lumous 4G Fig.

**Fragmento 22 - p. 11 - score 1:**

Third, Dynamic was the runner-up, receiving the second-best results in terms of O.23 and O.46. Unexpectedly, Pensieve failed to produce good ABR decisions, leading to multiple rebuffering events that contributed to the lowest O.23 score, which impacted O.46 negatively in most network traces. WealsoconductedacomparisonbetweenQoEitu andQoElin. We ﬁrst normalized both values (Section V-B4) and the com- parison between different ABR schemes for various network traces is listed in the last column of Table III. In each network trace, Ahaggar achieved the highest and most consistent per- formance in terms of N-QoEitu and N-QoElin (only in NYU LTE, TH and Dynamic were slightly better) compared to other ABR schemes.


### 8.10. ideas phase45 v1 controller

Palabras clave usadas: `safe, safety, risk, risk-aware, risk-calibrated, conservative, fallback, uncertainty, lower bound, buffer, low buffer, variable, fluctuation, tail, severe, rebuffering, stall, guidance, expert, hybrid, meta, environment-aware, trace skew, cluster, prioritize, fairness, multi-user, TCP, BPM, BSM`

**Fragmento 1 - p. 1 - score 3:**

10378 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024 Bitrate Adaptation and Guidance With Meta Reinforcement Learning Abdelhak Bentaleb , Member, IEEE, May Lim , Mehmet N. Akcay , Ali C. Begen , Senior Member, IEEE, and Roger Zimmermann , Senior Member, IEEE Abstract—Adaptive bitrate (ABR) schemes enable streaming clients to adapt to time-varying network/device conditions for a stall-free viewing experience. Most ABR schemes use manually tuned heuristics or learning-based methods. Heuristics are easy to implement but do not always perform well, whereas learning-based methods generally perform well but are difﬁcult to deploy on low-resource devices.

**Fragmento 2 - p. 2 - score 3:**

CMCD deﬁnes a set of information collected by a media client and sent along with the HTTP requests to the server running Ahaggar in query arguments or header extensions. CMSD allows the server to 1A highland region in the central Sahara in southern Algeria. convey Ahaggar bitrate guidance decisions to media clients through the HTTP response headers. We evaluate the performance of Ahaggar against several ABR solutions by running real-world trace-driven experiments. These experiments cover multiple clients with heterogeneous network conditions and device resolutions. Experimental re- sults show that Ahaggar delivers consistent quality, improves viewer QoE by up to 87.0%, reduces rebuffering duration by up to 84.4% and reduces bandwidth consumption by up to 62.6%.

**Fragmento 3 - p. 10 - score 3:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10387 TABLE III AVERAGE RESULTS OF THE QOE AND ITS METRICS FOR DIFFERENT NETWORK TRACES FOR SCENARIO A1 headless mode enabled using Puppeteer (https://pptr.dev/). The maximum playback buffer level was kept at the default value of 20 seconds. For network emulation, we used tc NetEm (https: //man7.org/linux/man-pages/man8/tc-netem.8.html) to throttle the total bandwidth available to the clients according to the network traces described in Section V-B2. We adopted two types of network emulations: (i) in server-side network emulation, the throttling is done on the server port so that all sessions share a single network trace, and (ii) in client-side network emulation, the throttling is done within each client’s Docker container so that session-speciﬁc network traces are used for each session.

**Fragmento 4 - p. 11 - score 3:**

10388 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024 Fig. 6. Avg. QoE itu (O.46) and avg. rebuffering duration ratio in various network traces for Scenario A1. The bottom (left) edge, mark and top (right) edge indicate the average−std, average and average + std, respectively, with a 95% conﬁdence interval. average pUHD, but it performed poorly in most other metrics. In thesamecontext,BOLAfailedtodelivergoodvideoqualitywith inferior VMAF scores, and RobustMPC suffered from frequent and long rebuffering events. Similarly, Ahaggar achieved the highest average QoEitu and lowest average rebuffering duration (see Fig. 6). In detail, Ahaggar achieved the highest average QoE with an improvement of [Lumous 4G Fig.

**Fragmento 5 - p. 12 - score 3:**

7(a): 109.80% (114.92%), Belgium 4G/LTE Fig. 7(b): 74.30% (90.16%), NYU LTE Fig. 7(c): 104.20% (114.14%), Lumous 5G Fig. 7(d): 10.69% (10.87%)] and lowest average rebuffering duration with areductionof[Lumous4GFig.7(a):93.58%(95.40%),Belgium 4G/LTE Fig. 7(b): 87.08% (98.74%), NYU LTE Fig. 7(c): 95.03% (98.75%), Lumous 5G Fig. 7(d): 1.57% (20.96%)], compared to the heuristic-based (learning-based) ABR schemes. The performance gains are most prominent in Lumous 4G, Belgium 4G/LTE and NYU LTE, which is also evident in Fig. 7(a)–(c) where Ahaggar is placed much further ahead of the other schemes. From the detailed analysis of the QoEitu scores in Table V, we see that Ahaggar achieved the highest average O.23 and O.46 scores for all network traces with an average improvement Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 6 - p. 1 - score 2:**

To make the most out of both worlds, we earlier developed Ahaggar, a learning-based scheme executing on the server side that provides quality-aware bitrate guidance to streaming clients running their own heuristics. Ahaggar’s novelty is the meta reinforcement learning approach taking network condi- tions, clients’ statuses and device resolutions, and streamed content as input features to perform bitrate guidance. Ahaggar uses the new Common Media Client/Server Data (CMCD/SD) protocols to exchange the necessary metadata between the servers and clients. While Ahaggar was a signiﬁcant step forward, in this study, we focus on three open areas, namely, (i) exploring the performance of Ahaggar in a heterogeneous environment including both Ahag- gar and non-Ahaggar clients with varied network conditions and device resolutions, and (ii) quantifying the impact of device resolutions on QoE with Ahaggar.

**Fragmento 7 - p. 1 - score 2:**

We thoroughly investigate these areas and report our ﬁndings. We also (iii) discuss the Ahaggar design choices. Experiments on an open-source system show that Ahaggar adapts to unseen conditions fast and outperforms its competitors in several viewer experience metrics. Index Terms—Adaptive streaming, meta-RL, ABR, CMCD, CMSD, bitrate guidance, quality awareness. I. INTRODUCTION W ITH the prevalence of HTTP adaptive streaming (HAS), the design of adaptive bitrate (ABR) logic—the algo- rithm deciding which segments to download and when (pri- marily based on the advertised encoding bitrate)—has received Manuscript received 22 January 2024; accepted 5 March 2024.

**Fragmento 8 - p. 2 - score 2:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10379 bitrate guidance with perceptual quality and device resolution awareness? ❸How to achieve continual learning for the server- side bitrate guidance? We answer the questions above in the context of Ahaggar,1 a meta reinforcement learning (meta-RL)-based solution. Ahag- gar has a server-side learning model that takes network condi- tions, clients’ statuses, device resolutions and streamed content as input features, and then provides quality and resolution-aware bitrate guidance to the streaming clients. Leveraging the server’s vastcomputationalpower,storagecapacityandmemory,Ahag- gar enables model inference for performing bitrate guidance tasks and helps resource-constrained streaming clients run their lightweight heuristic-based ABR schemes.

**Fragmento 9 - p. 2 - score 2:**

Ahaggar models bitrate guidance tasks for multiple clients as a partially ob- servable Markov decision process (POMDP) and leverages the latest developments in DRL to dynamically adapt to the varying network conditions. Speciﬁcally, it uses advantage Actor-Critic networks (A2C) for model training and Distributed Proximal Policy Optimization (DPPO) [25] with clip and Adam optimizer for policy updates at each time interval. Considering the changes in the environment, we adopt a Model Agnostic Meta-Learning (MAML) [23] on-policy gradient-based meta-RL approach that embeds policy gradient steps into the meta optimization. This al- lows Ahaggar to update the model parameters to achieve good generalization performance on unseen environments during the inference.

**Fragmento 10 - p. 2 - score 2:**

3) We explored the design choices of Ahaggar, including why we used DPPO and MAML as the policy update solution and the meta-RL algorithm, respectively. We also examined the effects of the number of shots, the learning episode and the Ahaggar model convergence. The rest of the paper is organized as follows. Section II shows the existing solutions for QoE optimization. Section III describes the Ahaggar solution, followed by its design choices in Section IV. The performance evaluation in Sections V and VI concludes the paper. II. RELATED WORK Client-Driven Heuristic-Based ABR: These schemes use heuristics based on estimated throughput (e.g., PANDA [31]), buffer level (e.g., BOLA [47]), segment size (e.g., SARA [8]), or a combination (e.g., MPCDASH [53]).

**Fragmento 11 - p. 3 - score 2:**

Inparticular,weuseacentralizedtraining with decentralized execution (CTDE) paradigm [56] to train the MARL agents. CTDE allows these agents to train decentralized policies with global information during training and to make decisions based on the individually learned policies during inference. We also use MAML [23], the meta-RL algorithm, to adapt to various network environments through parameter learning. The overall workﬂow of Ahaggar is shown in Fig. 2, where the steps are numbered as 1⃝– 8⃝. A. Formulation of the Problem At each segment download time epoch t, Ahaggar performs the bitrate guidance tasks (denoted by Z) by selecting the best bitrate (denoted by lc t) with respect to the current state (denoted by sc t) of each client c.

**Fragmento 12 - p. 4 - score 2:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10381 Fig. 2. Overall bitrate guidance system of Ahaggar. At each time t = [1, . . . , k], each agent c does not track the exact state sc t, but rather it uses the observations oc t for any given task zc t. Therefore, it has to rely on the history of actions and observations, denoted by hc t, to perform the best actions that result in higher rewards. We deﬁne the set of histories of client c as Hc = {hc 1, . . . , hc k} where hc t = {(ac t, oc t); . . . ; (ac 1, oc 1)} and the set of histories of N agents as H = {H1, . . . , HN}. Yet, hc t might exponentially grow with every action taken and every state observed.

**Fragmento 13 - p. 5 - score 2:**

The actor and critic use the same structure but with different outputs. For both networks, we use the Softmax activation function (Softmax()) with the L2-norm of networks as the last FC layer, resulting in an output range from 0 to 1. ▷Reward Function. At each time epoch t, the reward rc t of an agent c is calculated after each action ac t is taken to ensure that Ahaggar can learn from past experience. To do so, we adopt a well-know state-of-the-art reward function [11], [27], [35], [50], [53] that linearly combines ﬁve metrics (2): perceptual quality (qc t(lc t)), rebuffering duration (rdc t) and count (rcc t), quality oscillations (qoc t) and switches (qsc t).

**Fragmento 14 - p. 6 - score 2:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10383 via a stochastic gradient ascent using (5). θπc ←θπc + α Tθ  t=1 A πc θ t (bc t, ac t) ▽θ log πc θ(ac t, bc t) + β E, (5) where Tθ is the update interval, α is the learning rate and β is the entropy parameter that is set to a large value at the beginning of the training to encourage exploration and decreases over time to emphasize improving rewards. To calculate the advantage A(bc t, ac t) for a given experience, we have to estimate the value function V πc θ(b). This estimation is performed by the critic network that makes an objective assessment for all the states ∀bc t ∈B of an agent c during the training.

**Fragmento 15 - p. 7 - score 2:**

With this result, we ﬁnd DPPO is the best ﬁt for Ahaggar out of existing policy update techniques. B. Why MAML? We compare the performance of Ahaggar with MAML against Ahaggar with different well-known meta-RL ap- proaches [26]: PEARL, RL2, REPTILE, ANIL, and IMPALA. r PEARL uses the SAC policy for meta-training and adapts to new environments by performing inference over a latent context variable on which the policy is conditioned. r RL2 tries to structure the RL agent as a recurrent neural network(RNN),whichreceivesobservations,pastrewards, and actions, and retains its state across episodes in a given environment. Particularly, RL2 is encoded inside the weights of an RNN, which are learned slowly through a vanilla off-policy RL algorithm.

**Fragmento 16 - p. 7 - score 2:**

During the meta-testing phase, we use our HAS-based streaming system (Fig. 2), which consists of CMCD/SD-aware DASH clients running in Docker instances and a CMCD/SD-aware Node.js server with an HTTP server and an NJS application. NJS is written in JavaScript and extends the Node.js conﬁguration syntax to implement Ahag- gar’s bitrate guidance functions and communication with the dash.js clients. At runtime, for each client, the Ahaggar meta- model uses a JSON ﬁle that stores the model meta-parameters (θ and θi κ) and trajectories (D and Di κ) learned and captured every 40 shots during the ofﬂine phase. IV. Ahaggar DESIGN CHOICES A. Why DPPO? In Ahaggar, we used DPPO [25] as a policy update tech- nique.

**Fragmento 17 - p. 8 - score 2:**

BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING 10385 Fig. 4. MAML versus others. r REPTILE works by repeatedly sampling an environment, performing stochastic gradient descent on it, and updating the initial parameters towards the ﬁnal parameters learned on that environment. r ANIL is a simpliﬁed version of MAML that removes the inner-loop updates for all but the head (ﬁnal layer) of a neural network during training and inference. r IMPALA introduces a highly scalable distributed agent coupled with a new off-policy learning algorithm termed V-trace. V-trace is a general off-policy learning algorithm more stable and robust than other off-policy techniques for actor-critic agents.

**Fragmento 18 - p. 9 - score 2:**

To simplify the presentation of the QoE, we used a normalized QoElin (N-QoElin) with values between 0 and 1. To achieve that, we used the best achievable QoE (QoE⋆) in each session such that N-QoElin = QoElin / QoE⋆. The ITU P.1203 QoE model in Mode 0 (O.46) takes four metrics as input: bitrate, rebuffering duration, frame rate and content resolution. How to compute the QoEitu is described in [44]. This model outputs QoE values in the range of one to ﬁve (MOS) and we normalized them (N-QoEitu) to [0,1]. In addition, we computed (i) the total downloaded (TD) size (in MB) metric to measure how much bandwidth was consumed during the session, (ii) percentage of the HD (pHD) segments rendered at 720p or higher, and (iii) percentage of the UHD (pUHD) segments rendered at 2160p.

**Fragmento 19 - p. 9 - score 2:**

10386 IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024 TABLE II Ahaggar TRAINING/TESTING PARAMETERS guidance decisions. Another notable observation is that Fugu and Pensieve do not leverage meta-learning techniques. Thus, it takes longer for them to converge. V. PERFORMANCE EVALUATION A. Ahaggar Implementation 1) Choice of Ahaggar Parameters: To train the Ahag- gar model, we used a total of 2000 traces (1500 network and 500 content) from different datasets as described in Sec- tion III-B. We randomized them and then used 80% for training and 20% for testing. With an 80–20 train-test split, we per- formed a 5-fold walk-forward cross-validation on each dataset.

**Fragmento 20 - p. 9 - score 2:**

We (i) added new CMCD parameters (qt, dt, rs, ls, −→ QT, −→ LS) to support Ahaggar design, and (ii) used the mb = l (maximum suggested bitrate) CMSD-Dynamic parameter to convey Ahaggar’s bitrate guidance to each cor- responding client. On the server side, we used TensorFlow.js converter [45] to convert and load a pre-trained meta-model into a JavaScript Web-based application and run inference through TensorFlow.js. On the client side, we implemented a simple heuristic as our ABR scheme, which used Ahaggar bitrate guidance decisions to perform rate adaptation. To simplify input state data collection, we appended the manifest ﬁles by adding four tags: size, phone, hdtv and uhdtv.

**Fragmento 21 - p. 9 - score 2:**

4) Performance Metrics: We tested the ABR schemes using two main QoE models: Linear QoE [50] and ITU P.1203 QoE (Mode 0) [44]. For every session, we computed the accumulated QoElin using a linear function as follows: ω1 k  t=1 qc t(lc t)−ω2 k  t=1 rdc t −ω3rcc t −ω4 k  t=2 qoc t −ω5 k  t=2 qsc t, (10) where k t=1 qc t(lc t) is the accumulative perceived perceptual quality, k t=1 rdc t is the total rebuffering duration (RD), rcc t is the total rebuffering count (RC), k t=2 qoc t is the cumulative quality oscillations, k t=2 qsc t is the total number of quality switches, and k is the total number of segments. The coefﬁcients of ω1,2,3,4,5 are given in (2).

**Fragmento 22 - p. 9 - score 2:**

Training parameters can impact the performance of Ahag- gar, so we empirically set the parameters as summarized in Table II. 2) Ofﬂine Training: To train the Ahaggar meta-model, we used a customized trace-based segment-level Gym simu- lator based on Park [34]. This simulator was implemented in Python 3.6 to simulate a typical HAS system based on real- world network and content traces. We used TFLearn 1.5.0 [48], RLlib of Ray 1.12.0 [32] and TensorFlow 2.4.0 to implement Ahaggar’s NN architecture and build the training workﬂow. 3) Online Testing: To test Ahaggar, we implemented a CMCD/SD-enabled streaming system [2] with Ahaggar’s bi- trate guidance functions.


## 9. Checklist de informacion que Codex debe extraer de este paper

- Modelo/algoritmo exacto propuesto.
- Inputs/features realmente usados en decision o entrenamiento.
- Accion ABR y espacio de acciones.
- Reward/QoE/objetivo/loss.
- Teacher, experto, simulador o politica base si existe.
- Datos/trazas/datasets y splits.
- Baselines y evaluacion.
- Resultados numericos utiles.
- Limitaciones, costes, dependencias y riesgos de implementacion.
- Elementos transferibles a un controller propio en DashClientModular4.
- Elementos que NO deben copiarse por complejidad, leakage, GPU, dependencia o falta de defensa.


## 10. Extraccion cruda pagina a pagina

Texto extraido por pagina. Puede contener artefactos de dos columnas, referencias mezcladas, pies de figura o formulas degradadas. Para formulas/tablas/figuras, verificar PDF original.


### Pagina 1

```text
10378
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024
Bitrate Adaptation and Guidance With Meta
Reinforcement Learning
Abdelhak Bentaleb
, Member, IEEE, May Lim
, Mehmet N. Akcay
, Ali C. Begen
, Senior Member, IEEE,
and Roger Zimmermann
, Senior Member, IEEE
Abstract—Adaptive bitrate (ABR) schemes enable streaming
clients to adapt to time-varying network/device conditions for a
stall-free viewing experience. Most ABR schemes use manually
tuned heuristics or learning-based methods. Heuristics are easy to
implement but do not always perform well, whereas learning-based
methods generally perform well but are difﬁcult to deploy on
low-resource devices. To make the most out of both worlds, we
earlier developed Ahaggar, a learning-based scheme executing
on the server side that provides quality-aware bitrate guidance to
streaming clients running their own heuristics. Ahaggar’s novelty
is the meta reinforcement learning approach taking network condi-
tions, clients’ statuses and device resolutions, and streamed content
as input features to perform bitrate guidance. Ahaggar uses the
new Common Media Client/Server Data (CMCD/SD) protocols to
exchange the necessary metadata between the servers and clients.
While Ahaggar was a signiﬁcant step forward, in this study, we
focus on three open areas, namely, (i) exploring the performance of
Ahaggar in a heterogeneous environment including both Ahag-
gar and non-Ahaggar clients with varied network conditions
and device resolutions, and (ii) quantifying the impact of device
resolutions on QoE with Ahaggar. We thoroughly investigate these
areas and report our ﬁndings. We also (iii) discuss the Ahaggar
design choices. Experiments on an open-source system show that
Ahaggar adapts to unseen conditions fast and outperforms its
competitors in several viewer experience metrics.
Index Terms—Adaptive streaming, meta-RL, ABR, CMCD,
CMSD, bitrate guidance, quality awareness.
I. INTRODUCTION
W
ITH the prevalence of HTTP adaptive streaming (HAS),
the design of adaptive bitrate (ABR) logic—the algo-
rithm deciding which segments to download and when (pri-
marily based on the advertised encoding bitrate)—has received
Manuscript received 22 January 2024; accepted 5 March 2024. Date of
publication 12 March 2024; date of current version 3 October 2024. This
work was supported in part by Singapore MoE Academic Research Fund Tier
2 under MOE’s ofﬁcial under Grant T2EP20221-0023, and in part by the
ScientiﬁcandTechnologicalResearchCouncilofTürkiyeunderGrant120C154.
Recommended for acceptance by R. Zhang. (Corresponding author: Abdelhak
Bentaleb.)
Abdelhak Bentaleb is with the Gina Cody School of Engineering and Com-
puter Science, Concordia University, Montreal, QC H3G 1M8, Canada (e-mail:
abdelhak.bentaleb@concordia.ca).
May Lim and Roger Zimmermann are with the School of Computing,
National University of Singapore, Singapore 119077 (e-mail: maylim@comp.
nus.edu.sg; rogerz@comp.nus.edu.sg).
Mehmet N. Akcay and Ali C. Begen are with Ozyegin University,
34794 Istanbul, Türkiye (e-mail: necmettin.akcay@ozu.edu.tr; ali.begen@
ozyegin.edu.tr).
This
article
has
supplementary
downloadable
material
available
at
https://doi.org/10.1109/TMC.2024.3376560, provided by the authors.
Digital Object Identiﬁer 10.1109/TMC.2024.3376560
signiﬁcantresearchattention.ExistingABRschemes[15]canbe
broadly classiﬁed as heuristic or learning-based. ABR schemes
driven by heuristics make decisions based on client-side ob-
servations such as throughput estimation [31], playback buffer
level [47] or a combination of the two [53]. Although these
schemes are easy to implement, they heavily depend on some
conﬁguration parameters, and a poor setting may signiﬁcantly
hinder their efﬁcacy [27]. Hence, learning-based schemes have
become an alternative, beneﬁting from the latest breakthroughs
in machine learning (ML) such as deep reinforcement learning
(DRL), and supervised and imitation learning techniques [5].
Learning-basedschemesattaingoodstrategieswithoutrequiring
any presumptions about the environment.
Nonetheless, learning-based schemes are exposed to two
major limitations. First, their performance heavily depends on
the training data. Network environments can be quite diverse,
and their dynamics change over time. Therefore, future states
are not easy to predict accurately. Most schemes use classical
approaches to train an agent by giving feedback for decisions
while interacting with an environment. Such interaction can be
efﬁcientlyperformedinacontrolledtrace-drivensimulator. Still,
a mismatch may occur when the trained model is deployed in
a live system and encounters an environment not previously
seen [55]. As a result, the scheme may fail to perform proper
rate adaptation. Second, deploying learning-based schemes on
devices with scarce resources is impractical due to high storage
and computational costs. Prior work [55] showed that a learning
model trained on past network scenarios could hardly provide
a comparable performance under new conditions, and hence,
effective and continual model retraining/update was required.
Lastly, many studies [22], [30] claim that perceptual video
quality and device resolution must be considered in the ABR
logic to improve the quality of experience (QoE). Incorporating
these parameters into a learning model and then continually
retraining the model is also infeasible for clients running on
low-resource devices.
In our prior work (Ahaggar) [14], we have shown that
heuristic and learning-based schemes can complement each
other and leveraging the advantages of both solutions while
avoiding their shortcomings is the key. This brings up the
following three questions, which we seek to answer: ❶Can
we run a lightweight heuristic-based scheme on the client side
and learning-based bitrate guidance on the server side (which is
not as constrained as the clients) such that they can cooperate
harmoniously to deliver s better QoE? ❷How to implement
1536-1233 © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 2

```text
BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING
10379
bitrate guidance with perceptual quality and device resolution
awareness? ❸How to achieve continual learning for the server-
side bitrate guidance?
We answer the questions above in the context of Ahaggar,1 a
meta reinforcement learning (meta-RL)-based solution. Ahag-
gar has a server-side learning model that takes network condi-
tions, clients’ statuses, device resolutions and streamed content
as input features, and then provides quality and resolution-aware
bitrate guidance to the streaming clients. Leveraging the server’s
vastcomputationalpower,storagecapacityandmemory,Ahag-
gar enables model inference for performing bitrate guidance
tasks and helps resource-constrained streaming clients run their
lightweight heuristic-based ABR schemes. Ahaggar models
bitrate guidance tasks for multiple clients as a partially ob-
servable Markov decision process (POMDP) and leverages the
latest developments in DRL to dynamically adapt to the varying
network conditions. Speciﬁcally, it uses advantage Actor-Critic
networks (A2C) for model training and Distributed Proximal
Policy Optimization (DPPO) [25] with clip and Adam optimizer
for policy updates at each time interval. Considering the changes
in the environment, we adopt a Model Agnostic Meta-Learning
(MAML) [23] on-policy gradient-based meta-RL approach that
embeds policy gradient steps into the meta optimization. This al-
lows Ahaggar to update the model parameters to achieve good
generalization performance on unseen environments during the
inference. Therefore, our model can converge quickly to the best
performance and adapt to new unseen environments with only a
small number of (e.g., 40) shots. To our knowledge, this paper
is the ﬁrst study using meta-RL to improve QoE for adaptive
streaming clients while cleanly separating the responsibilities
for the servers and clients and respecting the client-driven nature
of HAS.
The Ahaggar solution comprises two phases: (i) (ofﬂine)
meta-training, where each RL agent trains the Ahaggar meta-
model on heterogeneous network environments, and (ii) (online)
meta-testing (also called inference), where each agent contin-
ually learns the system dynamics and rapidly optimizes the
meta-policy, adjusting the parameter weights that determine the
agent behavior according to the trajectories collected from both
the meta-training and meta-testing. We take inputs from the
network, clients and streamed content into the Ahaggar neural
network (NN) for bitrate guidance. The objective of Ahaggar
is to select the minimum bitrate (among the available options)
above which the next higher bitrate improves the perceptual
quality only insigniﬁcantly at the speciﬁc device resolution.
In this study, we use an objective full-reference perceptual
video quality metric known as Video Multi-method Assessment
Fusion (VMAF) [42].
To ensure healthy cooperation without incurring additional
complexities between the clients and servers, Ahaggar adopts
the emerging Common Media Client/Server Data standards:
CMCD [9], [13], [18] and CMSD [7], [19], [33]. CMCD deﬁnes
a set of information collected by a media client and sent along
with the HTTP requests to the server running Ahaggar in query
arguments or header extensions. CMSD allows the server to
1A highland region in the central Sahara in southern Algeria.
convey Ahaggar bitrate guidance decisions to media clients
through the HTTP response headers.
We evaluate the performance of Ahaggar against several
ABR solutions by running real-world trace-driven experiments.
These experiments cover multiple clients with heterogeneous
network conditions and device resolutions. Experimental re-
sults show that Ahaggar delivers consistent quality, improves
viewer QoE by up to 87.0%, reduces rebuffering duration by up
to 84.4% and reduces bandwidth consumption by up to 62.6%.
In addition, Ahaggar quickly converges to the best solution
during the training process with an improvement of 5.6× in
terms of the number of epochs required and 6× speedup on the
training time compared to the recent RL-based solutions such
as [35], [52].
This paper is an extended version of Ahaggar [14], focusing
on three main areas that remain open:
1) We conducted more experimental evaluations to assess the
performance of Ahaggar in more challenging scenarios,
especially in a heterogeneous environment that includes
both Ahaggar and non-Ahaggar clients with different
network conditions and device resolutions.
2) We investigated the impact of device resolution on Ahag-
gar QoE enhancement.
3) We explored the design choices of Ahaggar, including
why we used DPPO and MAML as the policy update
solution and the meta-RL algorithm, respectively. We also
examined the effects of the number of shots, the learning
episode and the Ahaggar model convergence.
The rest of the paper is organized as follows. Section II
shows the existing solutions for QoE optimization. Section III
describes the Ahaggar solution, followed by its design choices
in Section IV. The performance evaluation in Sections V and VI
concludes the paper.
II. RELATED WORK
Client-Driven Heuristic-Based ABR: These schemes use
heuristics based on estimated throughput (e.g., PANDA [31]),
buffer level (e.g., BOLA [47]), segment size (e.g., SARA [8]),
or a combination (e.g., MPCDASH [53]).
Client-Driven Learning-Based ABR: These schemes learn
from the streaming environment by training an NN using DRL
techniques [6], [17]. Mao et al. [35] proposed Pensieve, the
ﬁrst learning ABR that used DRL to generate a strategy toward
maximizing the viewer QoE. Bentaleb et al. [10] designed AMP
that implemented a set of learning-based bandwidth predictors
and model auto-selection for HAS. Similarly, Fugu [52] was
proposed to leverage the hidden Markov model for accurate
throughput prediction. Huang et al. [27] used imitation learning
to propose Comyco as ABR for on-demand videos.
Server-Driven Solutions: These solutions implement a rate
control on the server to control a client’s ABR decisions im-
plicitly or explicitly. In implicit control, the server does not
require cooperation from the client. To that end, some solutions
leveraged trafﬁc shaping [4], [57] or super-resolution [29]. In
explicit control, the server receives information from the clients
for intelligent QoE optimization decisions (e.g., [13]).
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 3

```text
10380
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024
Fig. 1.
MARL of Ahaggar.
Network-Driven Solutions: These solutions can be further cat-
egorized into: (1) In-network solutions where some works [11],
[12] use software-deﬁned networking to assist clients in their
ABR decisions, rate allocation [38] or multi-path delivery [16];
(2) Server and network assistance solutions where some pa-
pers [40], [49] leverage the SAND standard [1] that enables
data collection from various network entities involved in media
delivery. These data are then stored on a centralized server
for intelligent decisions, e.g., rate allocation; (3) Data-driven
solutions that combine SAND with AI capabilities for improved
decision making. These solutions collect QoE metrics from
many streaming sessions at a logically centralized controller that
maintains a global view of the real-time network conditions,
based on which the controller makes decisions regarding the
individual sessions (e.g., [24], [28]).
III. Ahaggar BITRATE GUIDANCE
Ahaggar serves multiple clients (agents in RL) with a shared
environment, distinct rewards and policies, as depicted in Fig. 1.
It performs bitrate guidance tasks at every time window and
decides the best bitrate for each client. Therefore, we consider a
fully cooperative multi-agent RL (MARL) [56] framework with
independent learners setting that involves a set of agents sharing
thesameenvironment. Inparticular,weuseacentralizedtraining
with decentralized execution (CTDE) paradigm [56] to train the
MARL agents. CTDE allows these agents to train decentralized
policies with global information during training and to make
decisions based on the individually learned policies during
inference. We also use MAML [23], the meta-RL algorithm,
to adapt to various network environments through parameter
learning. The overall workﬂow of Ahaggar is shown in Fig. 2,
where the steps are numbered as 1⃝– 8⃝.
A. Formulation of the Problem
At each segment download time epoch t, Ahaggar performs
the bitrate guidance tasks (denoted by Z) by selecting the best
bitrate (denoted by lc
t) with respect to the current state (denoted
by sc
t) of each client c. Mathematically, the bitrate guidance
problem for multiple clients can be formulated as
⎧
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪
⎩
ﬁnd lc,⋆
t (π), ∀c ∈[1, . . . , N], ∀t ∈[1, . . . , k]
arg max
π
QoEc
t (π)
s.t.
lc,⋆
t (π) ≤mtpc
t
C.1
N

c=1
lc,⋆
t (π) ≤BWtotal
C.2
,
(1)
where lc,⋆
t
is the best bitrate, which is the minimum among the
available options above and the next higher bitrate improves the
perceptual quality only insigniﬁcantly for the speciﬁc content
at the speciﬁc device resolution. Here, we use 1-JND (Just No-
ticeable Difference) as the threshold for being signiﬁcant [37].
Further in this formulation, π is an RL policy that decides the
bitrate for each client, N is the total number of clients, BWtotal
is the total server capacity and mtpc is the measured throughput
by client c.
The formulation in (1) is a multi-agent decision problem and
aims to ﬁnd the best bitrate lc,⋆
t
that maximizes the viewer QoEc
t
for each client c with respect to C.1–C.2. Here, each client has
access only to its local observations, and fully capturing the
state of the global environment experienced by all clients is not
feasible. Therefore, we cast the problem (1) as a partially observ-
able Markov decision process (POMDP), which is characterized
by its observation and historical information capabilities. The
POMDP model consists of 11-tuples POMDP = (S, A, O, R,
P, U, Z, C, N, α, γ), where:
r S = {S1, . . . , SN} is the set of the ﬁnite and discrete agent
states of N agents. For each agent c, we deﬁne the set of
agent states as Sc = {sc
1, . . . , sc
k}, where k = |Zc| is the
total number of bitrate guidance tasks.
r A = {A1, . . . , AN} is the ﬁnite and discrete set of actions
of N agents. For each agent c, we deﬁne the set of agent
actions as Ac = {ac
1, . . . , ac
k}, where each action is the
selected bitrate lc during a bitrate guidance task.
r O = {O1, . . . , ON} is the ﬁnite set of observation states
captured by the set of agents. For each client c, the set of
observations is Oc = {oc
1, . . . , oc
k}.
r R = {R1, . . . , RN} is the set of expected immediate re-
wards, which depends on states and actions taken by N
agents. For each client c, the set of rewards is Rc =
{rc
1, . . . , rc
k}.
r P = S × S × A →[0, 1] is the state transition probability
function P(s′|s, a) from the state s to s′ ∈S when action
a ∈A is taken.
r U = O × S × A →[0, 1] is the observation probability
function O(o′|s′, a) of observing o′ ∈O after transitioning
to s′ due to a.
r Z = {Z1, . . . , ZN} represents the bitrate guidance prob-
lem maxπ QoEc
t (π) for every agent c. The set of bi-
trate guidance tasks for agent c is thus deﬁned as Zc =
{zc
1, . . . , zc
k}.
r C = {1, . . . , N} is the set of N agents, where N is the total
number of agents and c ∈[1, . . . , N] is an agent.
r α and γ ∈[0, 1] are the learning rate and discount factor,
respectively.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 4

```text
BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING
10381
Fig. 2.
Overall bitrate guidance system of Ahaggar.
At each time t = [1, . . . , k], each agent c does not track the
exact state sc
t, but rather it uses the observations oc
t for any given
task zc
t. Therefore, it has to rely on the history of actions and
observations, denoted by hc
t, to perform the best actions that
result in higher rewards. We deﬁne the set of histories of client c
as Hc = {hc
1, . . . , hc
k} where hc
t = {(ac
t, oc
t); . . . ; (ac
1, oc
1)} and
the set of histories of N agents as H = {H1, . . . , HN}. Yet, hc
t
might exponentially grow with every action taken and every state
observed. In this case, the agent rather selects to use the belief
states, denoted by Bc, which are single-valued and represent
the observation probability U c over all possible histories Hc in
a given bitrate guidance task. For each bc
t ∈Bc, the observa-
tion probability distribution is denoted by uc
t = O(oc
t|hc
t, ac
t),
such that O(oc
t|hc
t, ac
t) = 
sc
t+1

sc
t P(sc
t|hc
t) P(sc
t+1|sc
t, ac
t)
O(oc
t+1|sc
t+1, ac
t), where P(sc
t|hc
t) is the belief state bc
t about the
state sc
t, Bc = {bc
1, . . . , bc
k} and B = {B1, . . . , BN} are the set
of belief states of agent c and the set of the ﬁnite and discrete
belief states of N agents, respectively. These belief states are
a sufﬁcient measure of histories and given a belief state bc
t, an
agent c strives to ﬁnd the effective optimal policy πc,⋆to solve
(1) by ﬁnding the best bitrate for each client that maximizes the
accumulated discounted reward (denoted by Gc
t and deﬁned in
Section III-B).
The Ahaggar learning model solves the POMDP problem
(1) using a multi-agent A2C [6] NN with clipped DPPO [25]
and Adam optimizer for policy (π) updates at every time in-
terval. For continual learning and quickly adapting to unseen
environments, it uses MAML—the meta-RL policy gradient
approach—allowing Ahaggar to learn hyper-parameter ini-
tialization and speed up the optimization of the learned model
during inference.
B. Ahaggar Meta-Training (Ofﬂine)
To train the Ahaggar meta-model, we use Park [34]—a
Python-based segment-level simulator that is based on OpenAI
and state-of-the-art ABR simulators [46] for RL-based model
training. This simulator faithfully emulates a streaming session
where the learning agent uses a large corpus of real-world net-
work and content traces to explore the streaming environment.
▷Network Traces. We used the Belgium 4G/LTE [51], Nor-
way 4G/LTE [43], NYU LTE [36] and Lumous 4G/5G [39]
datasets. Each trace entry consists of a throughput value (Mbps),
round-trip time (RTT; ms) and packet loss (%).
▷Content Traces. We used the Comyco [27] and Waterloo
SQoE-IV [22] datasets. To cover a wide range of device resolu-
tions, each source video was encoded at {0.24, 0.37, 0.57, 0.75,
1.0, 1.76, 2.36, 3.0, 4.3, 5.7, 8.0, 11, 16.6}Mbps at a resolution of
{180, 216, 288, 288, 360, 540, 720, 720, 1080, 1080, 1440, 2160,
2160}p, respectively. Each trace is comprised of video segments
with their corresponding encoded bitrates (Mbps), sizes (bytes)
and VMAF scores for three device resolutions (phone, HDTV
and UHDTV).
We performed customized modiﬁcations on the Park simula-
tor [34] to fully comply with the Ahaggar design. Speciﬁcally,
we revised (i) the problem space using POMDP instead of MDP,
(ii) input state, action and reward spaces, (iii) NN architecture
with policy update and meta-RL approaches, (iv) headless video
client by introducing three device resolutions, and (v) MARL
with CTDE and shared environment support. During the session,
the simulator used the traces and each client interaction with the
environment as input features to feed into the NN, from which
the RL agent, in turn, decided the segment bitrates at every time
step.
The Ahaggar uses an A2C NN. Without loss of generality
and since the agents are independent, we simplify the formu-
lation in the context of a single agent. At every time epoch
t, the segment-level statistics for each agent are collected and
aggregated as the environment input state. Different from MDP,
in POMDP, the agent cannot directly observe the complete
system state, but the agent makes observations that depend on
the state. The agent uses these observations to form a belief about
what state the system is currently in. This is called a belief state
and is expressed as a probability distribution over all possible
states. The solution of the POMDP is a policy prescribing which
action to take in each belief state. Formally, RL agents interact
with the environment that deﬁnes state space S, observation
space O and belief state space B. At each time epoch t, each RL
agent c observes a state oc
t ∈O and then receives a belief state
bc
t ∈B from the environment. Later, it takes an action ac
t ∈A
(aka lc,⋆
t ) while it receives a reward rc
t ∈R. Here, each agent
c aims to ﬁnd the optimal policy πc,⋆: S →O →B →A that
maps states-to-actions and maximizes the reward.
▷Input State. At each time epoch t, each agent c takes a
belief state with inputs deﬁned as bc
t = {mtpc
t, qtc
t, blc
t, lsc
t,
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 5

```text
10382
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024
dtc
t, rsc
t, −−→
LSc
t , −−→
QT c
t }, comprised of network, content and play-
back features of the last downloaded segment. These inputs are
measured throughput mtpc
t (Kbps), VMAF quality qtc
t (0–100),
current playback buffer length blc
t (second), segment size lsc
t
(KB), download time dtc
t (second), percentage of the remaining
segments in the video rsc
t (%), vector of m available sizes for
the next segment −−→
LSc
t (KB) and vector of m available VMAF
qualities for the next segment −−→
QT c
t (0–100). Instead of feeding
the A2C NN the exact values of the input state, we normalize
them to enable the agent to generalize the strategy better in an
unseen network environment [3].
▷Action Space. The action space A is deﬁned as the available
bitrate levels (i.e., n-dimensional vector) for a given video. In
each time epoch t, the Ahaggar policy πc,⋆of agent c maps bc
t
to compact discrete action space A and select ac,⋆
t
∈A.
▷Observation Space. We expose a subset of Ahaggar states
as the observations, where the agent c observes oc
t = {mtpc
t, qtc
t,
blc
t, lsc
t, dtc
t, rsc
t, −−→
LSc
t , −−→
QT c
t } for each time epoch t.
▷Output. The Ahaggar actor model returns 1×n-
dimensional vector representing bitrate levels with their associ-
ated probabilities. πc,⋆: bc
t →ac,⋆
t
maps the state bc
t to the best
action ac,⋆
t
based on the state-action probabilities, where ac,⋆
t
with the highest probability is selected under the current state.
The Ahaggar critic model outputs a single scalar indicating
the value function V c,π(bc
t) for the current state.
▷NN Architecture. The Ahaggar A2C NN architecture
consists of two networks: actor and critic. Each network uses
two 1DConv layers and six linear fully-connected (FC) layers to
extract the set of features. Each 1DConv layer consists of 3x3
convolution with feature number (=64) and kernel size (=1)
to feed the features −−→
LSc
t and −−→
QT c
t . Other inputs are fed into
FC layers with feature number (=64) and a Rectiﬁed Linear
Unit (ReLU()) activation function. Then, all input layers are
concatenated and ﬁnally fed into an FC layer with 64 neurons
and a slope of 0.5 to down-sample the concatenated features. The
actor and critic use the same structure but with different outputs.
For both networks, we use the Softmax activation function
(Softmax()) with the L2-norm of networks as the last FC layer,
resulting in an output range from 0 to 1.
▷Reward Function. At each time epoch t, the reward rc
t
of an agent c is calculated after each action ac
t is taken to
ensure that Ahaggar can learn from past experience. To do
so, we adopt a well-know state-of-the-art reward function [11],
[27], [35], [50], [53] that linearly combines ﬁve metrics (2):
perceptual quality (qc
t(lc
t)), rebuffering duration (rdc
t) and count
(rcc
t), quality oscillations (qoc
t) and switches (qsc
t).
rc
t = ω1 × qc
t(lc
t) −ω2 × rdc
t −ω3 × rcc
t −ω4 × qoc
t
−ω5 × qsc
t,
(2)
where qc
t(lc
t) maps the selected bitrate to the quality perceived
(VMAF) [11], [53], qoc
t = |qc
t(lc
t) −qc
t−1(lc
t−1)|, qsc
t = qoc
t/20,
and ωi are the coefﬁcients of the reward function. Herein,
following prior works [27], [50], we set qsc
t as the difference
of 20 in VMAF values of two consecutive segments. This QoE
model is developed based on linear regression on two datasets:
Comyco [27] and Waterloo SQoE-IV [22], where 70% of the
data is used for training and 30% for testing. We followed
the same setup to tune the coefﬁcients and our results show
that ω1 = 0.077, ω2 = 1.249, ω3 = 2.877, ω4 = 0.049, and
ω5 = 1.436 achieve the best trade-off between the ﬁve QoE
metrics. These results are similar to [50].
▷Policy Gradient and Training Algorithm. The essential
objective of Ahaggar is to improve the policy via boosting
the probabilities of high-reward samples from the collected
trajectories and declining the possibilities of failure samples
from the bad trajectories. For every time epoch t, each RL
agent c of Ahaggar selects the action ac
t that corresponds
to the bitrate for the next segment using the improved policy
π : πc,⋆
θ (bc
t, ac
t) →[0, 1] at state bc
t, which results in the best
accumulated discounted reward that is expressed as
Gc
t =
Tπc
θ

¯t=t
γ¯t−t × rc
t,
ac
t = arg max
a
E [Gc
t(bc
t, a)] ,
(3)
where Gc
t is computed from time t to the end of training,
Tπc
θ denotes the batch size for updating the gradient policy πc
θ,
γ ∈[0, 1] is the discount factor, θ is the policy parameter, and
πc,⋆
θ (bc
t, ac
t) is the probability that action ac
t is taken in state bc
t.
DPPO allows Ahaggar to run multi-agents (or workers), where
each agent has its own A2C network and data collection. Thus,
the gradient calculations are distributed over workers, as shown
in Fig. 1. For each episode, an agent c updates its gradient policy
such that Gc
t is maximized with respect to the policy parameters
θ, as follows:
▽¯Gc
t = 1
Θ
Θ

θ=1
Tπc
θ

t=1
A
πc
θ
t (bc
t, ac
t) ▽log πc
θ(ac
t, sc
t),
(4)
where Θ is the total number of episodes, Aπc
θ(bc
t, ac
t) is the
advantage function that represents the difference in the expected
cumulative reward after deterministically selecting the action ac
t
in state bc
t, compared with the expected reward for action drawn
from policy πc
θ. In PPO, the advantage function is calculated as
a function of Gc
t and baseline basec
t that has an impact on the
convergenceofGc
t.Priorwork[54]foundthatAπc
θ didnotgener-
alize well. Hence, in DPPO, we revise the advantage function by
using a truncated backpropagation through time with a window
of length κ such that Aπc
θ(bc
t, ac
t) = Qπc
θ(bc
t, ac
t) −V πc
θ(bc
t).
Qπc
θ is calculated by the actor network, which uses the κ-step
Temporal Difference (TD) approach given by: Qπc
θ(bc
t, ac
t) =
κ=Θ−1
κ=0
γκrc
t+κ + γΘV (bc
t+Θ). For each episode, the agent c
of the actor network aims to maximize Gc
t through maximizing
Aπc
θ, where it samples a trajectory of bitrate decisions and uses
the empirically computed advantage as an unbiased estimate
of Aπc
θ(bc
t, ac
t). To alleviate overﬁtting issues, Ahaggar uses
dropouts with probability (p = 0.5) to add a regularization term
to the update of the actor network. This regularization represents
the entropy E = H(πc
θ(.|bc
t)) of the probabilities over the bitrate
decisions. Therefore, the parameter θπc of the actor is updated
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 6

```text
BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING
10383
via a stochastic gradient ascent using (5).
θπc ←θπc + α
Tθ

t=1
A
πc
θ
t (bc
t, ac
t) ▽θ log πc
θ(ac
t, bc
t) + β E, (5)
where Tθ is the update interval, α is the learning rate and β is
the entropy parameter that is set to a large value at the beginning
of the training to encourage exploration and decreases over time
to emphasize improving rewards.
To calculate the advantage A(bc
t, ac
t) for a given experience,
we have to estimate the value function V πc
θ(b). This estimation
is performed by the critic network that makes an objective
assessment for all the states ∀bc
t ∈B of an agent c during the
training. To do so, the critic network uses the standard TD
method to compute the loss function and minimize its value.
The parameter θvc of the critic network is updated through a
stochastic gradient descent (SGD) algorithm using (6).
θvc ←θvc −¯α
Tθ

t=1
▽θ(rc
t + γV πc
θ(bc
t+1; θvc) −V πc
θ(bc
t; θvc))2,
(6)
where ¯α is the learning rate for the critic, V πc
θ(bc
t; θvc) and
V πc
θ(bc
t+1, θvc) are the objective assessments for bc
t and bc
t+1,
respectively, from the critic network.
Finally, we update the policy πθ periodically every κ-steps
using PPO with constrained clipped objective (CCO) and the
Adam optimizer. The constraint represents how much the policy
is allowed to change, expressed in terms of the Kullback-Leibler
(KL) divergence (KL[πc
θold|πc
θ]). Hence, the CCO is expressed
as: θκ+1 = arg maxθ LKLP EN
θκ
(θ), where
LKLP EN
θκ
(θ)=E
 Tθ

t=1
ratiot(θ)A
πc
θκ
t
−¯βKL[πc
θold|πc
θ]
	
, and,
(7)
E is the empirical expectation over time steps, ratiot(θ) (=
πc
θ(bc
t, ac
t)/ πc
θold(bc
t, ac
t)) is the ratio of the probabilities under
the new and old policies, ε is the clip hyperparameter (usually
ﬁxed to 0.1) and ¯β is the KL penalty hyperparameter.
▷Multi-agent Training with DPPO. In the training, Ahag-
gar spawns MARL agents in parallel (Fig. 1). Each agent is
conﬁgured to run independently with a shared environment such
that it experiences a different set of input states from the envi-
ronment. Here, the N agents continually send their parameters
θ to a central agent (termed the chief), which aggregates them
to generate a single Ahaggar model. For each sequence of
parameters θ that it receives, the chief uses the A2C algorithm to
compute a gradient based on (5) and (6). Then, the chief updates
the A2C networks and pushes out the new model to the agent
that sent the parameters. Such an update process can happen
synchronously or asynchronously among all agents, but we
foundthataveraginggradientsandapplyingthemsynchronously
leads to better results in the meta-testing phase.
The pseudocode for the DPPO used by Ahaggar is provided
in Algorithm 1 for the chief and Algorithm 2 for the workers.
In these algorithms, the hyperparameter KLtarget represents the
desired changes in the policy per time episode. The scaling term
˜α controls the adjustment of the KL-regularization coefﬁcient
Algorithm 1: Ahaggar DPPO (Central Agent; Chief).
1:
for Each agent c ∈{1, . . . , N} do
2:
while not done do
3:
Wait until N gradient parameters for actor (θπ) and
critic (θv) are available
4:
Average gradients and update global θπ and θv
5:
Update all the workers with global θπ and θv
6:
end while
7:
end for
Algorithm 2: Ahaggar DPPO (Workers).
1:
for Each agent c ∈{1, . . . , N} do
2:
while not done (for every t = [1, . . . , Tπc
θ]) do
3:
for Each κ ∈{0, . . . , Θ −1} do
4:
Run policy πc
θκ and collects {bc
t, ac
t, rc
t}
5:
Estimate discounted expected reward Gc
t
6:
Estimate advantages A
πc
θκ
t
7:
Store partial trajectory information
8:
end for
9:
πc
θold ←πc
θ
10:
Compute LKLP EN
θκ
(θ) using (7)
11:
if KL[πc
θold|πc
θ] > 4KLtarget then
12:
Break and continue with next time epoch t + 1
13:
end if
14:
Compute ▽θLKLP EN
θκ
15:
Send gradient actor parameters (θπc) to chief
16:
Send gradient critic parameters (θvc) to chief
17:
Wait until parameters are accepted or dropped
18:
Update parameters of worker c
19:
if KL[πc
θold|πc
θ] > ¯βhighKLtarget then
20:
¯β ←˜α¯β
21:
else if KL[πc
θold|πc
θ] < ¯βlowKLtarget then
22:
¯β ←¯β/˜α
23:
end if
24:
end while
25:
end for
if the actual change in the policy stays signiﬁcantly below or
above the target KL, i.e., it falls outside the interval [¯βlow ×
KLtarget, ¯βhigh × KLtarget].
▷Meta-Learned Policies for Training Algorithm. We adopt
the MAML approach, which allows learning model parameters
θ via meta-RL, i.e., ﬁnding the model parameters sensitive to
changes in the environment, allowing the Ahaggar model
to achieve fast adaptation to unseen environments during the
inference phase. The training algorithm consists of two loops:
(1) Inner Loop. For each episode, each agent c ﬁrst randomly
picks a speciﬁc network and content trace as the environment,
and sample X ∈D trajectories (also referred to as shots) where
D = {(bc
1, ac
1); . . . ; (bc
k, ac
k)} denotes the set of sampled tra-
jectories for inner loop in that environment according to the
current policy πc
θ. The Ahaggar meta-model then is optimized
by the collected trajectories with the DPPO and Adam opti-
mizer. In particular, we want to learn θ after a small number
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 7

```text
10384
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024
κ of policy gradient updates on the data from an environment
Evti ∼p(Evts) to obtain θi
κ. Here, i denotes the index of a
particular environment in a batch of environments Evts. This
set of κ updates is called inner-loop update. The updated θi
κ after
κ-step on data from Evti is given in (8).
θi
κ = θ −α ▽θ LDP P O
Evti
(fθ, D),
(8)
where fθ is the Ahaggar meta-model and LDP P O
Evti
(fθ) is the
loss on the environment Evti after κ-step of updates.
(2) Outer Loop. For each episode, each agent c continually
samples many trajectories (∈Di
κ; the set of sampled trajectories
for outer loop) from the randomized environments via meta-
policy πc
θiκ of meta-model fθiκ and calculates gradients for θ
with the trajectory. After that, these agents send the calculated
gradients to the chief, which in turn merges them via agents’
loss functions and the outer loop’s learning rate β. Formally, we
deﬁne a meta-objective (Lmeta(θ)) as Tπc
θ
t=1 LSGD
Evti (fθiκ). The
optimization of L is called the outer-loop update. The resulting
update for θ is given by (9).
θ = θ −β ▽θ
Tπc
θ

t=1
LSGD
Evti (fθiκ, Di
κ),
(9)
where the update is performed using SGD, β is a learning rate
and LSGD
Evti denotes the loss on the environment Evti.
C. Ahaggar Meta-Testing (Online)
The objective of Ahaggar is to learn how to adapt to hetero-
geneous network environments during the online phase through
continual learning enabled by MAML. During the meta-testing
phase, we use our HAS-based streaming system (Fig. 2), which
consists of CMCD/SD-aware DASH clients running in Docker
instances and a CMCD/SD-aware Node.js server with an HTTP
server and an NJS application. NJS is written in JavaScript and
extends the Node.js conﬁguration syntax to implement Ahag-
gar’s bitrate guidance functions and communication with the
dash.js clients. At runtime, for each client, the Ahaggar meta-
model uses a JSON ﬁle that stores the model meta-parameters (θ
and θi
κ) and trajectories (D and Di
κ) learned and captured every
40 shots during the ofﬂine phase.
IV. Ahaggar DESIGN CHOICES
A. Why DPPO?
In Ahaggar, we used DPPO [25] as a policy update tech-
nique. Here, we show the central insight of selecting DPPO
compared to popular vanilla DRL-based policy update tech-
niques [6], [21] such as asynchronous advantage actor-critic
(A3C), trust region policy optimization (TRPO), deep deter-
ministic policy gradient (DDPG), soft actor-critic (SAC), twin
delayed DDPG (TD3) and Random.
r A3C is an on-policy algorithm that extends actor-critic to
asynchronous and parallel learning, disturbs the correlation
between data, and improves training speed.
r TRPO is an on-policy algorithm that updates policies by
taking the largest step possible to improve performance
Fig. 3.
DPPO versus others.
while satisfying a KL-Divergence constraint on how close
the new and old policies are allowed to be.
r DDPG is an off-policy algorithm that combines DQN and
actor-critic algorithms to use deterministic policy gradients
for updating the policy via a DL approach.
r SAC is an off-policy algorithm that combines stochastic
policy optimization and DDPG-style approaches. It incor-
porates the clipped double-Q trick and entropy regulariza-
tion.
r TD3 is an off-policy algorithm that introduces clipped dou-
ble Q-learning mode and a delayed policy update strategy
to solve the overestimation problem of DDPG.
r Random is an algorithm that chooses an action randomly.
To compare the performance of Ahaggar with DPPO against
other policy update techniques, we prepared 10% as a validation
set from the 20% of the testing set comprising network and video
content traces. We implemented these techniques in Ahaggar
and then ran the experiment with 1,000 agents on the same
validation set every 500 episodes and recorded the validation
learning curve in Fig. 3. We can see that DPPO achieves the best
performance with (i) the highest possible N-QoElin (reward;
see Section V-B4) and (ii) trains and converges faster to the
highest reward value with only 3,000 episodes, compared to its
competitors.DPPOreliesonspecializedclippingintheobjective
function (7) to remove incentives for the new policy to get far
from the old policy. Hence, it allows robust policy optimization
for whole video sessions. Comparing DPPO with TRPO, we
observe that TRPO is the runner-up that typically obtains a high
reward, but it takes more time (6,000 episodes) to converge to
the best achievable reward. With this result, we ﬁnd DPPO is the
best ﬁt for Ahaggar out of existing policy update techniques.
B. Why MAML?
We compare the performance of Ahaggar with MAML
against Ahaggar with different well-known meta-RL ap-
proaches [26]: PEARL, RL2, REPTILE, ANIL, and IMPALA.
r PEARL uses the SAC policy for meta-training and adapts
to new environments by performing inference over a latent
context variable on which the policy is conditioned.
r RL2 tries to structure the RL agent as a recurrent neural
network(RNN),whichreceivesobservations,pastrewards,
and actions, and retains its state across episodes in a
given environment. Particularly, RL2 is encoded inside the
weights of an RNN, which are learned slowly through a
vanilla off-policy RL algorithm.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 8

```text
BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING
10385
Fig. 4.
MAML versus others.
r REPTILE works by repeatedly sampling an environment,
performing stochastic gradient descent on it, and updating
the initial parameters towards the ﬁnal parameters learned
on that environment.
r ANIL is a simpliﬁed version of MAML that removes the
inner-loop updates for all but the head (ﬁnal layer) of a
neural network during training and inference.
r IMPALA introduces a highly scalable distributed agent
coupled with a new off-policy learning algorithm termed
V-trace. V-trace is a general off-policy learning algorithm
more stable and robust than other off-policy techniques for
actor-critic agents.
We run the same experiment outlined in Section IV-A and
the meta-validation learning curve for this experiment is shown
in Fig. 4. With 3,000 episodes, we observe that MAML out-
performs existing meta-RL approaches in terms of N-QoElin
with an average improvement of 57.5% (PEARL: 64.4%, RL2:
65.3%, REPTILE: 79.9%, ANIL: 28.7%, IMPALA: 49.11%).
It also converges quickly to the best reward, requiring 3,000
episodes, 2x better than the runner-up approach (ANIL), which
shows the effectiveness of MAML in the meta-training phase.
ANIL generally performs better than RL2, IMPALA, REPTILE
and PEARL, as it is an extension of MAML without inner-loop
updates. However, they all, including ANIL, require more train-
ing time and episodes to converge. REPTILE fails to converge
and struggles to adapt/generalize to different environments. To
sum up, this result suggests the effectiveness of MAML against
its baselines.
C. Number of Shots and Learning Episodes
Although considering more trajectories X (or shots) results in
increased improvement in sampling efﬁciency, it generates more
computation cost overhead, which can hinder the performance
of the trained model and its generalization during inference.
A good solution should make a trade-off between sampling
efﬁciency, model generalization/convergence and computation
cost overhead. To ﬁnd the best value for X that leads to faster
convergence and minimizes the computation cost overhead,
we ran an experiment for Ahaggar with various shot values
X = {1, 20, 40, 60, 80, 100}. We used the same validation set
and setup as above Section IV-A. The meta-validation learning
curve for Ahaggar with various shot values is highlighted in
Fig. 5. We observe that Ahaggar with X = 100 converges
to the best N-QoElin with fewer episodes of 2,500. However,
it generates 2x, 4x, and 8x more computation cost overhead
Fig. 5.
Ahaggar convergence.
TABLE I
MODEL CONVERGENCE/GENERALIZATION FOR DIFFERENT SOLUTIONS TIME
compared to X = 80, X = 60 and X = 40, respectively. One
interesting observation is that Ahaggar with X = 40 (40-
shots) is the best trade-off point, allowing good sampling ef-
ﬁciency and convergence to its best generalization performance
(highestachievableN-QoElin)muchfaster(comparableto2,500
episodes) within 3,000 episodes, and signiﬁcant reduction in
computation cost overhead for both Ahaggar meta-training
and meta-testing phases compared to X = 100, X = 80, or
X = 60. Therefore, we set X=40 during the meta-training and
meta-testing (and meta-validation) phases. More notably, with
X = 1 or X = 20, the convergence was very slow (requiring
more episodes) compared to X > 20-shots.
D. Ahaggar Model Convergence
We trained each model on a physical workstation machine
with dual 20-core Intel E5-2630 v4 @ 2.20GHz processors,
192 GB memory, and 8 GPUs. Table I shows the convergence
time, episodes and shots required for a model to generalize and
converge to the best solution. We ﬁxed the number of shots to
40 and workers to 1,000 for all meta-RL techniques, including
Ahaggar, ANIL, PEARL, and RL2. During the training (80%
datasets), Ahaggar is able to converge faster and achieve the
best performance with 3,000 episodes (with 2,000 iterations
per episode), taking eight hours of training, compared to other
solutions. It requires 2x (2x), 4x (3x), 5x (5x), 7x (9x), and 10x
(12x) fewer episodes (time) to achieve its best generalization
performance compared to ANIL, IMPALA, RL2, Fugu and
Pensive, respectively. Similarly, in meta-testing (20% datasets),
Ahaggar generalizes well and converges within only 40-shots
(e.g., equal to watching 40 video sessions). In contrast, other
techniques require more shots to adapt to various environments.
For example, ANIL and PEAR require 100-shots and 150-
shots, respectively. This is an anticipated result from Ahaggar
because of DPPO multi-agent work distribution and MAML
fast adaptation capabilities. More notably, during the inference,
Ahaggar takes only a few milliseconds to perform the bitrate
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 9

```text
10386
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024
TABLE II
Ahaggar TRAINING/TESTING PARAMETERS
guidance decisions. Another notable observation is that Fugu
and Pensieve do not leverage meta-learning techniques. Thus, it
takes longer for them to converge.
V. PERFORMANCE EVALUATION
A. Ahaggar Implementation
1) Choice of Ahaggar Parameters: To train the Ahag-
gar model, we used a total of 2000 traces (1500 network
and 500 content) from different datasets as described in Sec-
tion III-B. We randomized them and then used 80% for training
and 20% for testing. With an 80–20 train-test split, we per-
formed a 5-fold walk-forward cross-validation on each dataset.
Training parameters can impact the performance of Ahag-
gar, so we empirically set the parameters as summarized in
Table II.
2) Ofﬂine Training: To train the Ahaggar meta-model,
we used a customized trace-based segment-level Gym simu-
lator based on Park [34]. This simulator was implemented in
Python 3.6 to simulate a typical HAS system based on real-
world network and content traces. We used TFLearn 1.5.0 [48],
RLlib of Ray 1.12.0 [32] and TensorFlow 2.4.0 to implement
Ahaggar’s NN architecture and build the training workﬂow.
3) Online Testing: To test Ahaggar, we implemented a
CMCD/SD-enabled streaming system [2] with Ahaggar’s bi-
trate guidance functions. We (i) added new CMCD parameters
(qt, dt, rs, ls, −→
QT, −→
LS) to support Ahaggar design, and (ii)
used the mb = l (maximum suggested bitrate) CMSD-Dynamic
parameter to convey Ahaggar’s bitrate guidance to each cor-
responding client. On the server side, we used TensorFlow.js
converter [45] to convert and load a pre-trained meta-model into
a JavaScript Web-based application and run inference through
TensorFlow.js. On the client side, we implemented a simple
heuristic as our ABR scheme, which used Ahaggar bitrate
guidance decisions to perform rate adaptation. To simplify input
state data collection, we appended the manifest ﬁles by adding
four tags: size, phone, hdtv and uhdtv. These tags represent the
segment sizes and VMAF scores for phone, HDTV and UHDTV,
respectively. The VMAF scores were computed using different
VMAF models depending on the device resolution. We provide
a sample manifest ﬁle in [2].
B. Methodology and Evaluation Setup
1) Video Sample and Parameters: The HTTP server hosted
the 4K DASH dataset [41] that was not used in training. We
encoded the 636 seconds long Big Buck Bunny (BBB) into four-
second segments in FFmpeg using the H.264 codec at 30 fps
and in 13 bitrates/resolutions. Further characteristics of BBB
are given in supplementary materials (Appendix B), available
online.
2) Network Traces: We used network traces with different
user mobility (bus, walking, car, train, bicycle, tram, ferry
and driving) to throttle the bandwidth between the server and
clients. These traces were extracted from the 20% of network
datasets for testing (Belgium 4G/LTE [51], NYU LTE [36],
Lumous 4G/5G [39]). We randomly extracted six network traces
from each dataset where the inter-variation duration between
the bandwidth values was ﬁxed to ﬁve seconds. Further char-
acteristics of the traces are given in supplementary materials
(Appendix A), available online.
3) ABRSchemes: WecomparedAhaggaragainstheuristics
such as throughput-based (TH), buffer-based (BOLA) and
Dynamic (TH+BOLA) from dash.js [20] and RobustMPC [53]
and
one
learning-based
scheme:
Pensieve
[35].
The
heuristic-based schemes were tuned and Pensieve was retrained
with our datasets and QoE metrics to ﬁt each experiment.
4) Performance Metrics: We tested the ABR schemes using
two main QoE models: Linear QoE [50] and ITU P.1203 QoE
(Mode 0) [44]. For every session, we computed the accumulated
QoElin using a linear function as follows:
ω1
k

t=1
qc
t(lc
t)−ω2
k

t=1
rdc
t −ω3rcc
t −ω4
k

t=2
qoc
t −ω5
k

t=2
qsc
t,
(10)
where k
t=1 qc
t(lc
t) is the accumulative perceived perceptual
quality, k
t=1 rdc
t is the total rebuffering duration (RD), rcc
t is
the total rebuffering count (RC), k
t=2 qoc
t is the cumulative
quality oscillations, k
t=2 qsc
t is the total number of quality
switches, and k is the total number of segments. The coefﬁcients
of ω1,2,3,4,5 are given in (2). To simplify the presentation of
the QoE, we used a normalized QoElin (N-QoElin) with values
between 0 and 1. To achieve that, we used the best achievable
QoE (QoE⋆) in each session such that N-QoElin = QoElin /
QoE⋆. The ITU P.1203 QoE model in Mode 0 (O.46) takes four
metrics as input: bitrate, rebuffering duration, frame rate and
content resolution. How to compute the QoEitu is described
in [44]. This model outputs QoE values in the range of one to
ﬁve (MOS) and we normalized them (N-QoEitu) to [0,1]. In
addition, we computed (i) the total downloaded (TD) size (in
MB) metric to measure how much bandwidth was consumed
during the session, (ii) percentage of the HD (pHD) segments
rendered at 720p or higher, and (iii) percentage of the UHD
(pUHD) segments rendered at 2160p.
5) Evaluation Setup and Scenarios: Our setup consisted of
onephysicalmachinerunningUbuntu18.04.6LTS,AMDRyzen
7 3700X 8-Core CPU and 32 GB memory. We ran a Docker
container for each client, in which we ran a CMCD/SD-aware
dash.js (v4.2.1) client on a Google Chrome browser (v103) with
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 10

```text
BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING
10387
TABLE III
AVERAGE RESULTS OF THE QOE AND ITS METRICS FOR DIFFERENT NETWORK TRACES FOR SCENARIO A1
headless mode enabled using Puppeteer (https://pptr.dev/). The
maximum playback buffer level was kept at the default value of
20 seconds. For network emulation, we used tc NetEm (https:
//man7.org/linux/man-pages/man8/tc-netem.8.html) to throttle
the total bandwidth available to the clients according to the
network traces described in Section V-B2. We adopted two types
of network emulations: (i) in server-side network emulation, the
throttling is done on the server port so that all sessions share a
single network trace, and (ii) in client-side network emulation,
the throttling is done within each client’s Docker container so
that session-speciﬁc network traces are used for each session.
We evaluated Ahaggar in different multi-client scenarios with
six clients in each scenario as summarized below:
r Scenario A1: The six clients are identical UHDTV clients.
This scenario evaluates the performance of Ahaggar
against the other ABR schemes. Client-side network emu-
lation is used.
r Scenario B1: The six clients contain a mix of device
resolutions, namely, two UHDTV, two HDTV, and two
phone clients. This scenario evaluates the effectiveness
of Ahaggar in adapting to different device resolutions.
Client-side network emulation is used.
r Scenario A2: A repeat of Scenario A1 except that server-
side network emulation is used.
r Scenario B2: A repeat of Scenario B1 except that server-
side network emulation is used.
r Scenario C: The six clients contain a mix of ABR schemes:
three Dynamic and three Ahaggar clients. This scenario
evaluates the impact of introducing Ahaggar clients
amongst clients that do not use Ahaggar. Client-side
network emulation is used.
Details of the network traces used in each scenario are given
in supplementary materials (Appendix A), available online.
C. Results for Multiple Identical Clients (Scenario A1)
For each ABR scheme, we ran multiple UHDTV clients.
Table III shows the total QoE and detailed breakdown of each
QoE metric for each ABR scheme for various network traces.
We provide the average and standard deviation values for six
clients and over ﬁve runs in the format of average ± std. In
general, Ahaggar gained the best possible performance in
terms of RC, RD and TD without sacriﬁcing the VMAF score
compared to other baselines in all network traces. Looking at
the averages across all the network traces, we see that Ahag-
gar reduced average RD by 62.81% (84.36%), average RC
by 53.52% (71.18%) and average TD by 53.27% (59.34%),
compared to the heuristic-based (learning-based) ABR schemes.
In addition, Ahaggar signiﬁcantly reduced the number of times
a UHD segment was picked when there was no noticeable
VMAF score difference compared to the other best-performing
schemes (RobustMPC and Dynamic) across all network traces.
Such reduction translates to signiﬁcant bandwidth savings (see
the Avg. TD column in Table III).
We anticipated these results because Ahaggar makes bitrate
guidance decisions based on not only the throughput, buffer
level and segment sizes, but also segment quality and device
resolution. It also uses MAML for continual learning and fast
adaptation to unseen environments. In contrast, other ABR
schemes use one or more heuristics or an NN combining these
heuristics and they do not necessarily perform well in unseen
environments. Fig. 6 and Table III conﬁrm this. For instance,
Pensieve achieved the highest average selected bitrate and
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 11

```text
10388
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024
Fig. 6.
Avg. QoE itu (O.46) and avg. rebuffering duration ratio in various
network traces for Scenario A1. The bottom (left) edge, mark and top (right)
edge indicate the average−std, average and average + std, respectively, with
a 95% conﬁdence interval.
average pUHD, but it performed poorly in most other metrics. In
thesamecontext,BOLAfailedtodelivergoodvideoqualitywith
inferior VMAF scores, and RobustMPC suffered from frequent
and long rebuffering events.
Similarly, Ahaggar achieved the highest average QoEitu
and lowest average rebuffering duration (see Fig. 6). In
detail, Ahaggar achieved the highest average QoE with an
improvement of [Lumous 4G Fig. 6(a): 22.28% (44.73%),
Belgium 4G/LTE Fig. 6(b): 49.49% (37.06%), NYU LTE Fig.
6(c): 55.04% (85.08%), Lumous 5G Fig. 6(d): 8.01% (31.10%)]
and lowest average rebuffering duration with a reduction of
62.81% (84.36%) across all network traces, compared to
heuristic-based (learning-based) ABR schemes. Compared to
Ahaggar, Dynamic achieved the second-best average results
in terms of the QoE and rebuffering duration. This is because
of the Dynamic design that combines the beneﬁts of BOLA and
TH by switching between both in runtime based on the stability
of the current buffer level. However, Pensieve, followed by
RobustMPC, suffered from low QoE and long RD due to wrong
ABR decisions. It is worth mentioning that all schemes faced
a few rebuffering events in Lumous 5G because sometimes
the bandwidth dropped signiﬁcantly and suddenly (caused by
the handoffs to 4G). This is a behavior known in 5G networks
operating in higher frequencies [39].
To understand how QoEitu (Mode 0) is computed for each
session, Table III (the eighth and ninth columns) highlights
the scores of its essential metrics (O.23: Rebufﬁng Duration
Score and O.46: Overall Score) for different ABR schemes.
The score of each metric is given in the MOS range of one to
ﬁve. Here, we deduce three important thrusts. First, Ahaggar
outperformed the baselines, achieving the best O.23 and O.46
scores for all network traces with an average improvement
of 67.55% (heuristic-based: 60.75%, learning-based: 94.75%)
TABLE IV
AVERAGE QOE itu (O.46) SCORES AND ITS METRICS PRODUCED BY Ahaggar
RUNNING ON DEVICES WITH DIFFERENT RESOLUTIONS FOR SCENARIO B1
and 36.86% (heuristic-based: 33.70%, learning-based: 49.49%)
across all network traces, respectively. It also achieved higher
O.35 (Visual Quality Score, not shown) scores with values
ranging between 4.60 and 4.94. These results conﬁrm how well
Ahaggar performs to balance the QoEitu metrics. Second, the
Belgium 4G/LTE dataset has the lowest bandwidth values in its
network traces. Therefore, all ABR schemes achieved the lowest
scores in terms of O.23, O.35 and O.46. Nonetheless, since
Ahaggar has been designed to adapt quickly to challenging
network conditions (thanks to MAML), it was able to obtain
the best O.23 (2.37) and O.46 (2.70) scores. Although other
baselines achieved a comparable O.35 score (not shown), they
faced frequent and long rebuffering events due to their greedy
bitrate selection strategy. Third, Dynamic was the runner-up,
receiving the second-best results in terms of O.23 and O.46.
Unexpectedly, Pensieve failed to produce good ABR decisions,
leading to multiple rebuffering events that contributed to the
lowest O.23 score, which impacted O.46 negatively in most
network traces.
WealsoconductedacomparisonbetweenQoEitu andQoElin.
We ﬁrst normalized both values (Section V-B4) and the com-
parison between different ABR schemes for various network
traces is listed in the last column of Table III. In each network
trace, Ahaggar achieved the highest and most consistent per-
formance in terms of N-QoEitu and N-QoElin (only in NYU
LTE, TH and Dynamic were slightly better) compared to other
ABR schemes. We can see that the N-QoEitu and N-QoElin
are almost identical for each dataset, and thus, can be used
interchangeably in practice.
D. Results for Multiple Mixed-Device Clients (Scenario B1)
To evaluate the effectiveness of Ahaggar in adapting to
different device resolutions (DR), we ran two clients with each
DR (a total of six). Table IV highlights the results over ﬁve runs.
The key takeaway is that Ahaggar achieved different average
results for each DR, conﬁrming Ahaggar’s DR awareness.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 12

```text
BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING
10389
TABLE V
AVERAGE RESULTS OF THE QOE AND ITS METRICS FOR DIFFERENT NETWORK TRACES FOR SCENARIO A2
Ahaggar picked a higher bitrate on the average for a UHDTV
compared to an HDTV and a phone. For instance, it selected
1.5x-2x higher bitrate for UHDTV compared to the phone with
almost a 1-JND difference between the VMAF scores for various
network traces. This is because devices with a phone-like res-
olution can achieve the highest VMAF score (95-98) requiring
only half of the bitrate that a UHDTV requires. We note that the
VMAF score differences at a similar bitrate level (e.g., phone
versus HDTV in NYU LTE) are due to the different per-device
VMAF models used to calculate the scores.
E. Results for Multiple Identical Clients With Shared Network
Trace (Scenario A2)
Similar to Scenario A1, we ran six UHDTV clients for each
ABR scheme in this scenario. However, in contrast to the client-
side network emulation used in Scenario A1, the clients in each
ABR scheme here share the same network trace via server-side
network emulation, which allows us to evaluate the performance
when the network is constrained at the server-end (before the
streams propagate to the downstream links that separate the
clients). Table V shows the total QoE and detailed breakdown
of each QoE metric for each ABR scheme for various network
traces. Generally speaking, with the exception of Lumous 5G,
Ahaggar achieved the best performance in terms of RC, RD
and TD with a much smaller trade-off in VMAF as compared
to the other ABR schemes. Speciﬁcally, the averages computed
across all the network traces show that Ahaggar reduced
average RD by 91.10% (97.95%), average RC by 83.85%
(91.47%) and average TD by 66.55% (70.90%) compared to
the heuristic-based (learning-based) ABR schemes. In contrast,
the average VMAF scores only dropped by 4.24% (5.54%)
compared to the heuristic-based (learning-based) ABR schemes
(or 4.00 (5.12) in absolute values which is less than a 1-JND
difference as compared to the other schemes). Moreover, Ahag-
gar picked a signiﬁcantly lower percentage of UHD segments,
speciﬁcally, a reduction of 41.80% (43.66%) compared to the
heuristic-based (learning-based) ABR schemes, while keeping
to within 1-JND difference in VMAF scores across all network
traces. This leads to large bandwidth savings as indicated by
the average TD performance. We also note that Lumous 5G
contains the least challenging traces with the highest bandwidth
range compared to the other three sets of traces, and hence, its
results do not show the same signiﬁcant improvements in the
rebufferingperformance(speciﬁcallyinaverageRDandaverage
RC) of Ahaggar when compared against the other schemes.
From Fig. 7, we can also see that Ahaggar achieved the
highest average QoEitu across all network traces and lowest
average rebuffering duration in all traces except Lumous 5G.
Speciﬁcally, Ahaggar achieved the highest average QoEitu
with an improvement of [Lumous 4G Fig. 7(a): 109.80%
(114.92%), Belgium 4G/LTE Fig. 7(b): 74.30% (90.16%), NYU
LTE Fig. 7(c): 104.20% (114.14%), Lumous 5G Fig. 7(d):
10.69% (10.87%)] and lowest average rebuffering duration with
areductionof[Lumous4GFig.7(a):93.58%(95.40%),Belgium
4G/LTE Fig. 7(b): 87.08% (98.74%), NYU LTE Fig. 7(c):
95.03% (98.75%), Lumous 5G Fig. 7(d): 1.57% (20.96%)],
compared to the heuristic-based (learning-based) ABR schemes.
The performance gains are most prominent in Lumous 4G,
Belgium 4G/LTE and NYU LTE, which is also evident in
Fig. 7(a)–(c) where Ahaggar is placed much further ahead
of the other schemes.
From the detailed analysis of the QoEitu scores in Table V,
we see that Ahaggar achieved the highest average O.23 and
O.46 scores for all network traces with an average improvement
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 13

```text
10390
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024
Fig. 7.
Avg. QoE itu (O.46) and avg. rebuffering duration ratio in various
network traces for Scenario A2. The bottom (left) edge, mark and top (right)
edge indicate the average−std, average and average + std, respectively, with
a 95% conﬁdence interval.
of 126.23% (143.87%) and 66.14% (73.69%) compared to the
heuristic-based (learning-based) ABR schemes, respectively.
These results again validate that Ahaggar is able to balance
the QoEitu metrics well. This observation is also consistent
with the N-QoElin results whereby Ahaggar achieved the
best or close to the best N-QoElin scores, ranging between 0.97
and 1.00 (with 1.00 being the highest possible score), in all
network traces. Similar to the results in Scenario A1, Dynamic
achieved the second-best results in terms of average O.23 and
O.46 scores, while Pensieve experienced multiple rebuffering
events that led to the lowest average O.23 and O.46 scores,
averaged across all network traces.
Comparing the ﬁndings between Scenario A1 and this
scenario (Scenario A2), we can see that they generally share
similar observations as to the performance gains Ahaggar
achieves compared to the other ABR schemes, which validates
its performance in both client-side and server-side network
emulation scenarios.
F. Results for Multiple Mixed-Device Clients With Shared
Network Trace (Scenario B2)
Similar to Scenario B1, we ran two clients with each device
resolution (DR) (total of six clients) to evaluate the effective-
ness of Ahaggar in adapting to different DRs. The results
are presented in Table VI. From the results, we can see that
Ahaggar is still able to showcase its DR awareness by selecting
the lowest average bitrates for phone, followed by HDTV, and
the highest average bitrates for UHDTV across all network
traces (except for Belgium 4G/LTE where the average selected
bitrate for phone and HDTV are comparable). This validates its
DR awareness capabilities in both client-side and server-side
network emulation scenarios.
G. Results for Multiple Mixed-ABR Clients (Scenario C)
In this scenario, we ran Dynamic and Ahaggar clients
concurrently (three clients each giving six clients in total) to
TABLE VI
AVERAGE QOE itu (O.46) SCORES AND ITS METRICS PRODUCED BY Ahaggar
RUNNING ON DEVICES WITH DIFFERENT RESOLUTIONS FOR SCENARIO B2
TABLE VII
AVERAGE RESULTS OF QOE itu (O.46) AND VMAF PRODUCED BY DYNAMIC
CLIENTS WHEN RAN CONCURRENTLY WITH AND WITHOUT Ahaggar
CLIENTS UNDER DIFFERENT NETWORK TRACES FOR SCENARIO C
study the effect of introducing new Ahaggar clients to a
pool of existing non-Ahaggar clients. The average QoEitu
(O.46) and VMAF results are presented in Table VII. From
the results, we can see that Dynamic clients in the mixed-ABR
environments that also contain Ahaggar clients performed bet-
ter than the Dynamic clients in the Dynamic-only environment
for all network traces except Belgium 4G/LTE. Speciﬁcally, the
Dynamic clients that ran concurrently with Ahaggar-UHDTV
(Ahaggar-HDTV)clientsachievedimprovementsinQoEitu of
[Lumous 4G: 12.36% (21.21%), NYU LTE: 6.87% (13.28%),
Lumous 5G: 14.15% (13.21%)], while keeping VMAF con-
sistent (within 0.19% (0.08%)) across these network traces,
when compared against the Dynamic clients in Dynamic-only
environment. The performance gain in QoEitu is primarily due
to the lower rebuffering duration (not shown in Table VII) where
the Dynamic clients in mixed-ABR environments achieved re-
duction in average rebuffering duration by [Lumous 4G: 20.05%
(30.03%), NYU LTE: 14.49% (11.34%), Lumous 5G: 47.95%
(51.42%)] when running concurrently with Ahaggar-UHDTV
(Ahaggar-HDTV) clients. This validates that the bandwidth
savings brought about by Ahaggar clients have positive spill-
over effects on other clients sharing the network as well (as
shown by the reduced rebuffering duration experienced by the
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 14

```text
BENTALEB et al.: BITRATE ADAPTATION AND GUIDANCE WITH META REINFORCEMENT LEARNING
10391
Dynamic clients in mixed-ABR environments). We note that
Belgium 4G/LTE contains the most challenging traces with the
lowest bandwidth range than the other three sets of traces, and
under these extreme network conditions, the Dynamic clients
were selecting much lower video bitrates that coincided with
the levels of bitrate selected by the Ahaggar clients. Hence, in
Belgium 4G/LTE, the introduction of Ahaggar clients did not
affect the amount of data transmitted over the network which
explains the absence of performance gains as seen in the other
sets of traces.
VI. CONCLUSION
This paper presented Ahaggar, a server-side, learning-
based, quality-aware bitrate guidance solution that complements
the client-side heuristic-based ABR schemes. Ahaggar adopts
two key enablers: (i) a meta-RL approach to ﬁnd the best bitrate
for each client under the given circumstances and quickly adapt
to changing network conditions, and (ii) CMCD/SD speciﬁ-
cation to simplify the metadata exchange between the server
and clients. Experiments show that Ahaggar delivers a better
user experience with less bandwidth consumption over various
network conditions.
REFERENCES
[1] ISO/IEC 23009–5:2017 Information technology–Dynamic adaptive
streaming over HTTP (DASH) – Part 5: Server and network assisted
DASH (SAND), 2017. Accessed: Mar. 8, 2024. [Online] Available: https:
//www.iso.org/standard/69079.html
[2] A. Bentaleb, M. Lim, M. N. Akcay, A. C. Begen, and R. Zimmermann,
“Ahaggar bitrate guidance,” 2023. Accessed: Mar. 8, 2024. [Online] Avail-
able: https://github.com/NUStreaming/Ahaggar
[3] S. Abbasloo, C.-Y. Yen, and H. J. Chao, “Classic meets modern: A prag-
matic learning-based congestion control for the Internet,” in Proc. Annu.
Conf. ACM Special Int. Group Data Commun. Appl. Technol. Architectures
Protoc. Comput. Commun., 2020, pp. 632–647.
[4] S. Akhshabi, L. Anantakrishnan, C. Dovrolis, and A. C. Begen, “Server-
basedtrafﬁcshapingforstabilizingoscillatingadaptivestreamingplayers,”
in Proc. 23rd ACM Workshop Netw. Operating Syst. Support Digit. Audio
Video, 2013, pp. 19–24, doi: 10.1145/2460782.2460786.
[5] E. Alpaydin, Introduction to Machine Learning. Cambridge, MA, USA:
MIT Press, 2020.
[6] K. Arulkumaran, M. P. Deisenroth, M. Brundage, and A. A. Bharath,
“Deepreinforcementlearning:Abriefsurvey,”IEEESignalProcess.Mag.,
vol. 34, no. 6, pp. 26–38, Nov. 2017.
[7] A. C. Begen, “Manus manum lavat: Media clients and servers cooperating
with common media client/server data,” in Proc. ACM Appl. Netw. Res.
Workshop, 2021, pp. 82–84, doi: 10.1145/3472305.3472886.
[8] A.C.Begen,M.N.Akcay,A.Bentaleb,andA.Giladi,“Adaptivestreaming
of content-aware-encoded videos in dash.js,” SMPTE Motion Imag. J.,
vol. 131, no. 4, pp. 30–38, May 2022, doi: 10.5594/JMI.2022.3160560.
[9] A. C. Begen, A. Bentaleb, D. Silhavy, S. Pham, R. Zimmermann, and W.
Law, “Road to salvation: Streaming clients and content delivery networks
working together,” IEEE Commun. Mag., vol. 59, no. 11, pp. 123–128,
Nov. 2021, doi: 10.1109/MCOM.121.2100137.
[10] A. Bentaleb, A. C. Begen, S. Harous, and R. Zimmermann, “Data-
driven bandwidth prediction models and automated model selection for
low latency,” IEEE Trans. Multimedia, vol. 23, pp. 2588–2601, 2021,
doi: 10.1109/TMM.2020.3013387.
[11] A. Bentaleb, A. C. Begen, and R. Zimmermann, “SDNDASH: Improv-
ing QoE of HTTP adaptive streaming using software deﬁned network-
ing,” in Proc. 24th ACM Int. Conf. Multimedia, 2016, pp. 1296–1305,
doi: 10.1145/2964284.2964332.
[12] A. Bentaleb, A. C. Begen, and R. Zimmermann, “ORL-SDN: Online
reinforcement learning for SDN-enabled HTTP adaptive streaming,” ACM
Trans. Multimedia Comput. Commun. Appl., vol. 14, no. 3, pp. 1–28, 2018,
doi: 10.1145/3219752.
[13] A. Bentaleb, M. Lim, M. N. Akcay, A. C. Begen, and R. Zimmermann,
“Common media client data (CMCD): Initial ﬁndings,” in Proc. 31st
ACM Workshop Netw. Operating Syst. Support Digit. Audio Video, 2021,
pp. 25–33, doi: 10.1145/3458306.3461444.
[14] A. Bentaleb, M. Lim, M. N. Akcay, A. C. Begen, and R. Zim-
mermann, “Meta reinforcement learning for rate adaptation,” in
Proc. IEEE Conf. Comput. Commun., 2023, pp. 1–10, doi: 10.1109/
INFOCOM53939.2023.10228951.
[15] A. Bentaleb, B. Taani, A. C. Begen, C. Timmerer, and R. Zimmermann,
“A survey on bitrate adaptation schemes for streaming media over HTTP,”
IEEE Commun. Surveys Tut., vol. 21, no. 1, pp. 562–585, First Quarter,
2019, doi: 10.1109/COMST.2018.2862938.
[16] A. Bentaleb, P. K. Yadav, W. T. Ooi, and R. Zimmermann, “DQ-DASH: A
queuing theory approach to distributed adaptive video streaming,” ACM
Trans. Multimedia Comput. Commun. Appl., vol. 16, no. 1, pp. 1–24,
2020.
[17] A. Bokani, M. Hassan, S. Kanhere, and X. Zhu, “Optimizing HTTP-based
adaptive streaming in vehicular environment using Markov decision pro-
cess,” IEEE Trans. Multimedia, vol. 17, no. 12, pp. 2297–2309, Dec. 2015.
[18] “CTA-5004: Web application video ecosystem – common media client
data,” 2020. Accessed: Mar. 8, 2024. [Online]. Available: https://cdn.cta.
tech/cta/media/media/resources/standards/pdfs/cta-5004-ﬁnal.pdf
[19] “CTA- 5006: Web application video ecosystem – common media server
data,” 2022. Accessed: Mar. 8, 2024. [Online]. Available: https://cdn.cta.
tech/cta/media/media/resources/standards/pdfs/cta-5006-ﬁnal.pdf
[20] DASH-IF, “DASH reference client,” 2021. Accessed: Mar. 8, 2024. [On-
line] Available: https://reference.dashif.org/dash.js/
[21] H. Dong, H. Dong, Z. Ding, S. Zhang, and Chang, Deep Reinforcement
Learning: Fundamentals, Research and Applications. Berlin, Germany:
Springer, 2020.
[22] Z. Duanmu et al., “Assessing the quality-of-experience of adaptive bitrate
video streaming,” 2020, arXiv: 2008.08804.
[23] C. Finn, P. Abbeel, and S. Levine, “Model-agnostic meta-learning for fast
adaptation of deep networks,” in Proc. 34th Int. Conf. Mach. Learn., 2017,
pp. 1126–1135.
[24] A. Ganjam et al., “C3: Internet-scale control plane for video quality opti-
mization,” in Proc. 12th USENIX Conf. Netw. Syst. Des. Implementation,
2015, pp. 131–144.
[25] N. Heess et al., “Emergence of locomotion behaviours in rich environ-
ments,” 2017, arXiv: 1707.02286.
[26] T. Hospedales, A. Antoniou, P. Micaelli, and A. Storkey, “Meta-learning
in neural networks: A survey,” 2020, arXiv: 2004.05439.
[27] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, “Comyco:
Quality-aware adaptive video streaming via imitation learning,” in Proc.
27th ACM Int. Conf. Multimedia, 2019, pp. 429–437.
[28] J. Jiang, V. Sekar, H. Milner, D. Shepherd, I. Stoica, and H. Zhang,
“CFA: A practical prediction system for video QoE optimization,”
in Proc. 13th USENIX Conf. Netw. Syst. Des. Implementation, 2016,
pp. 137–150.
[29] J. Kim, Y. Jung, H. Yeo, J. Ye, and D. Han, “Neural-enhanced live
streaming: Improving live video ingest via online learning,” in Proc. Annu.
Conf. ACM Special Int. Group Data Commun. Appl. Technol. Architectures
Protoc. Comput. Commun., 2020, pp. 107–125.
[30] Z. Li, A. C. Begen, J. Gahm, Y. Shan, B. Osler, and D. Oran, “Streaming
video over HTTP with consistent quality,” in Proc. 5th ACM Multimedia
Syst. Conf., 2014, pp. 248–258, doi: 10.1145/2557642.2557658.
[31] Z. Li et al., “Probe and adapt: Rate adaptation for HTTP video streaming at
scale,” IEEE J. Sel. Areas Commun., vol. 32, no. 4, pp. 719–733, Apr. 2014,
doi: 10.1109/JSAC.2014.140405.
[32] E. Liang et al., “RLlib: Abstractions for distributed reinforcement learn-
ing,” in Proc. 35th Int. Conf. Mach. Learn., 2018, pp. 3053–3062.
[33] M. Lim, M. N. Akcay, A. Bentaleb, A. C. Begen, and R. Zimmermann,
“The beneﬁts of server hinting when DASHing or HLSing,” in Proc. 1st
Mile-High Video Conf., 2022, pp. 52–55, doi: 10.1145/3510450.3517317.
[34] H. Mao et al., “Park: An open platform for learning-augmented com-
puter systems,” in Proc. 33rd Int. Conf. Neural Inf. Process. Syst., 2019,
pp. 2494–2506.
[35] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video streaming
with pensieve,” in Proc. Conf. ACM Special Int. Group Data Commun.,
2017, pp. 197–210.
[36] L. Mei et al., “Realtime mobile bandwidth prediction using LSTM NN,”
in Proc. Int. Conf. Passive Act. Netw. Meas., 2019, pp. 34–47.
[37] V. V. Menon, H. Amirpour, M. Ghanbari, and C. Timmerer, “OPTE:
Online per-title encoding for live video streaming,” in Proc. IEEE Int.
Conf. Acoust. Speech Signal Process., 2022, pp. 1865–1869.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 15

```text
10392
IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 23, NO. 11, NOVEMBER 2024
[38] M. Mu et al., “A scalable user fairness model for adaptive video streaming
over SDN-assisted future networks,” IEEE J. Sel. Areas Commun., vol. 34,
no. 8, pp. 2168–2184, Aug. 2016.
[39] A. Narayanan et al., “A variegated look at 5G in the wild: Performance,
power, and QoE implications,” in Proc. ACM SIGCOMM Conf., 2021,
pp. 610–625.
[40] S. Pham, P. Heeren, D. Silhavy, and S. Arbanowski, “Evaluation of shared
resource allocation using SAND for ABR streaming,” in Proc. 10th ACM
Multimedia Syst. Conf., 2019, pp. 165–174.
[41] J. J. Quinlan and C. J. Sreenan, “Multi-proﬁle ultra high deﬁnition (UHD)
AVC and HEVC 4K DASH datasets,” in Proc. 9th ACM Multimedia Syst.
Conf., 2018, pp. 375–380.
[42] R. Rassool, “VMAF reproducibility: Validating a perceptual practical
video quality metric,” in Proc. IEEE Int. Symp. Broadband Multimedia
Syst. Broadcast., 2017, pp. 1–2.
[43] H. Riiser, P. Vigmostad, C. Griwodz, and P. Halvorsen, “Commute path
bandwidth traces from 3G networks: Analysis and applications,” in Proc.
4th ACM Multimedia Syst. Conf., 2013, pp. 114–118.
[44] W. Robitza et al., “HTTP adaptive streaming QoE estimation with ITU-T
Rec. P. 1203: Open databases and software,” in Proc. 9th ACM Multimedia
Syst. Conf., 2018, pp. 466–471.
[45] D. Smilkov et al., “Tensorﬂow.js: Machine learning for the web and
beyond,” in Proc. Mach. Learn. Syst., vol. 1, pp. 309–321, 2019.
[46] K. Spiteri, R. Sitaraman, and D. Sparacio, “From theory to practice:
Improving bitrate adaptation in the DASH reference player,” ACM Trans.
Multimedia Comput. Commun. Appl., vol. 15, no. 2s, pp. 1–29, 2019.
[47] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal
bitrate adaptation for online videos,” IEEE/ACM Trans. Netw., vol. 28,
no. 4, pp. 1698–1711, Aug. 2020.
[48] Y. Tang, “TFLearn: TensorFlow’s high-level module for distributed ma-
chine learning,” 2016, arXiv:1612.04251.
[49] F. Tashtarian, A. Bentaleb, A. Erfanian, H. Hellwagner, C. Timmerer, and
R. Zimmermann, “HxL3: Optimized delivery architecture for HTTP low-
latency live streaming,” IEEE Trans. Multimedia, vol. 25, pp. 2585–2600,
2022.
[50] B. Turkkan et al., “GreenABR: Energy-aware adaptive bitrate streaming
with deep reinforcement learning,” in Proc. 13th ACM Multimedia Syst.
Conf., 2022, pp. 150–163.
[51] J. van der Hooft et al., “HTTP/2-based adaptive streaming of HEVC
video over 4G/LTE networks,” IEEE Commun. Lett., vol. 20, no. 11,
pp. 2177–2180, Nov. 2016.
[52] F. Y. Yan et al., “Learning in situ: A randomized experiment in video
streaming,” in Proc. 17th USENIX Conf. Netw. Syst. Des. Implementation,
2020, pp. 495–512.
[53] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic approach
for dynamic adaptive video streaming over HTTP,” in Proc. ACM Conf.
Special Int. Group Data Commun., 2015, pp. 325–338.
[54] C. Yu, A. Velu, E. Vinitsky, Y. Wang, A. Bayen, and Y. Wu, “The
surprising effectiveness of PPO in cooperative, multi-agent games,”
2021, arXiv:2103.01955.
[55] H. Zhang et al., “OnRL: Improving mobile video telephony via online
reinforcement learning,” in Proc. 26th Annu. Int. Conf. Mobile Comput.
Netw., 2020, Art. no. 29.
[56] C. Zhu, M. Dastani, and S. Wang, “A survey of multi-agent reinforcement
learning with communication,” 2022, arXiv:2203.08975.
[57] X. Zhu, S. Sen, and Z. M. Mao, “Livelyzer: Analyzing the ﬁrst-mile ingest
performance of live video streaming,” in Proc. 12th ACM Multimedia Syst.
Conf., 2021, pp. 36–50.
Abdelhak Bentaleb (Member, IEEE) received the
PhD degree in computer science from the National
University of Singapore (NUS), Singapore, in 2019.
He continued as a research fellow with the same
department until 2022. He is currently an assistant
professor with the Department of Computer Sci-
ence and Software Engineering, Concordia Univer-
sity, Canada. He is a co-founder of Atlastream Inc.,
Singapore. He received many prestigious awards like
SIGMM Award for Outstanding PhD Thesis Award,
DASH-IF Best PhD Dissertation Award and Dean’s
Graduate Research Excellence Award AY2018/2019. His research interests
include applied AI in multimedia systems and communication, video streaming
architectures, content delivery, distributed computing, computer networks and
protocols, wireless communications, and mobile networks.
May Lim received the BESc and MSc degree from
Nanyang Technological University (NTU), Singa-
pore, in 2015. She is currently working toward the
PhD degree in computer science with the National
University of Singapore (NUS), Singapore. Her cur-
rent research interest is primarily in multimedia
streaming systems and she has done several works
relating to low-latency streaming for live 2D and
6DoF videos.
Mehmet N. Akcay received the BSc degree in the
ﬁeld of computer engineering, from Istanbul Tech-
nical University, in 2005, and the MSc degree in the
same ﬁeld from Bogazici University, in 2008, and has
worked in the industry for more than 10 years, and
the PhD degree in computer science from Ozyegin
University, in 2022. His research interests are HTTP
adaptive streaming, low-latency live streaming and
software veriﬁcation using formal methods.
Ali C. Begen (Senior Member, IEEE) received the
PhD degree in electrical and computer engineering
from Georgia Tech. He has been a research and
development engineer since 2001, and has broad
experience in mathematical modeling, performance
analysis, optimization, standards development, intel-
lectual property and innovation. Between 2007 and
2015, he was with the Video and Content Platforms
Research and Advanced Development Group, Cisco.
Currently, he is afﬁliated with Ozyegin University,
where he teaches and advises students in the computer
science department. To date, he received several academic and industry awards
(including an Emmy Award for Technology and Engineering), and was granted
more than 30 US patents. In 2016, he was elected distinguished lecturer by
the IEEE Communications Society, and in 2018, he was re-elected for another
two-yearterm.In2017,heinitiatedandsincethenhasbeentheheadofdelegation
for the Turkish National Body for ISO/IEC JTC1/SC29 (JPEG and MPEG). He
was also listed among the world’s most inﬂuential scientists in the subﬁeld of
networking and telecommunications, in 2020 and 2021.
Roger Zimmermann (Senior Member, IEEE) re-
ceived the MS and PhD degrees from the University
of Southern California (USC), respectively. He is cur-
rently a professor with the Department of Computer
Science, National University of Singapore (NUS),
Singapore. He is also a lead investigator with the
Grab-NUS AI Lab and from 2011–2021 he was
deputy director with the Smart Systems Institute
(SSI), NUS. He has coauthored a book, seven patents,
and more than 350 conference publications, journal
articles, and book chapters in the areas of multimedia
processing, networking and data analytics. He is a distinguished member of the
ACM. He recently was Secretary of ACM SIGSPATIAL (2014–2017), a director
of the IEEE Multimedia Communications Technical Committee (MMTC) Re-
view Board and an editorial board member of the Springer Multimedia Tools and
Applications journal. He is also an associate editor with IEEE MultiMedia, ACM
TransactionsonMultimediaComputing,Communications,andApplicationsand
IEEE Open Journal of the Communications Society.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 09,2026 at 09:23:34 UTC from IEEE Xplore.  Restrictions apply.
```
