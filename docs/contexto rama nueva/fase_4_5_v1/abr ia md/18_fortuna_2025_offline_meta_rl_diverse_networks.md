# Fortuna - Optimizing Adaptive Video Streaming: Offline Reinforcement Learning and Meta-Learning in Diverse Networks

## 0. Identificacion del archivo

- Archivo fuente: `Fortuna.pdf`
- Paginas detectadas: `14`
- SHA256 PDF: `40b70c8746ced2305a78797e8001ee8842e0f7458f4331816038755bbb63724b`
- Texto crudo auxiliar PyMuPDF: `raw_text/18_fortuna_2025_offline_meta_rl_diverse_networks.txt`
- Texto crudo auxiliar pdftotext -layout: `raw_text_layout/18_fortuna_2025_offline_meta_rl_diverse_networks_layout.txt`

## 1. Uso previsto para Fase 4-5 v1

Fuente frontera sobre offline RL + meta-learning en redes diversas/heavy-tailed. Relevante para entender limites, generalizacion, colas de red, adaptacion y por que una solucion TFG debe ser mas simple/reproducible aunque tome ideas de robustez.

## 2. Advertencia de fidelidad

Este archivo NO es un resumen breve. Es una extraccion tecnica densa para que Codex pueda leer el paper sin depender de conversiones Markdown corruptas. El PDF original sigue siendo la fuente de verdad para formulas, tablas, figuras, simbolos y resultados exactos. Cuando una formula, tabla o figura sea decisiva, se debe verificar contra el PDF original.

## 3. Identificacion textual extraida de las primeras paginas

```text
IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025
8185
Optimizing Adaptive Video Streaming: Ofﬂine
Reinforcement Learning and Meta-Learning
in Diverse Networks
Ling Yi
, Yongbin Qin
, and Ruizhang Huang
Abstract—Recent years have seen the optimization of quality
of experience (QoE) through learning adaptive bitrate (ABR)
algorithms from internet video streams. However, the complex
nature of the real-world Internet, characterized by heavy-tailed
behavior, diversity, and unpredictability, hinder the effective
learning of off-the-shelf reinforcement learning (RL)-based ABR
algorithms. As a result, existing methods inevitably fail to
achieve optimal performance under various network conditions
and user QoE objectives. We propose Fortuna, a novel ofﬂine
meta RL ABR algorithm that can effectively learn from these
heavy-tailed internet data features and become more practical.
Fortuna is primarily divided into two phases. In the ofﬂine
phase, Fortuna utilizes diverse ofﬂine data for learning to reduce
the costly online RL interaction expense, while in the online
phase, we gradually increase video streaming sessions complexity
through curriculum learning to quickly adapt to speciﬁc network
conditions. Fortuna then utilizes meta-learning to optimize ABR
policies and enhance generalization. Additionally, to better learn
network features, Fortuna further optimizes QoE by learning low-
level TCP congestion control information. Experimental results
from trace-driven and real-world scenarios demonstrate that
Fortuna enhances learning efﬁciency by more than 7.5%–4 ×,
reduces stall time by 4.6%–14.2%, and generalizes to different
network conditions and video streams.
Index
Terms—Adaptive
bitrate
algorithm,
ofﬂine
meta
reinforcement learning, quality of experience.
I. INTRODUCTION
V
IDEO streaming is the primary internet application, ac-
countingfornearly75%ofalltrafﬁc[1].Inadaptivebitrate
(ABR) video streaming, videos are typically divided into various
small video chunks or segments. Video users can request spe-
ciﬁc video chunks based on their preferences and network con-
ditions. Each video chunk is assigned a particular bitrate and
Received 18 November 2024; revised 22 January 2025; accepted 15 Febru-
ary 2025. Date of publication 10 September 2025; date of current version 12
November 2025. This work was supported in part by the National Natural Sci-
ence Foundation of China under Grant 62066008, in part by the Key Projects of
Science and Technology of Guizhou Province under Grant [2020]1Z055, and in
partbytheNationalKeyR&DProgramofChinaunderGrant2023YFC3304500.
The associate editor coordinating the review of this article and approving it for
publication was Prof. Qiang Wu. (Corresponding author: Yongbin Qin.)
The authors are with the Text Computing & Cognitive Intelligence Engi-
neering Research Center of National Education Ministry, College of Computer
Science and Technology, Guizhou University, Guiyang 550025, China, and also
with the State Key Laboratory of Public Big Data, College of Computer Science
and Technology, Guizhou University, Guiyang 550025, China (e-mail: yiling-
phd@gmail.com; ybqin@gzu.edu.cn; cse.rzhuang@gzu.edu.cn).
Digital Object Identiﬁer 10.1109/TMM.2025.3604930
quality level, enabling users to select the most suitable video
chunk according to available bandwidth. However, due to net-
work bandwidth limitations, ABR algorithms may not always
request high-quality videos consistently.
The main existing ABR algorithms use simple control rules or
reinforcement learning (RL) based methods. For example, RB
algorithm [2] is only based on network bandwidth or buffer us-
age e.g., BOLA algorithm [3], [4], or a combination of the two
schemes (e.g., robustMPC [5], Oboe [6], Bayesian-MPC [7]).
These methods require careful adjustment and are unable to
adapt to different network bandwidths or different QoE ob-
jectives. State-of-the-art MPC algorithm [5] uses future video
chunks by dynamically optimizing QoE metrics, which has bet-
ter performance than the simple ﬁxed schemes e.g., BOLA,
RB. However, MPC relies on accurate network bandwidth pre-
dictions, especially on future networks. Due to the variability
of network bandwidth, MPC is difﬁcult to predict accurately,
but inaccurate predictions may cause future video freezes and
low-quality video etc. Additionally, since BOLA and MPC can-
not adjust parameters according to speciﬁc network conditions
and are too sensitive to parameters, then Oboe [6] is proposed to
automatically adjust parameters, which can enhance QoE value
in speciﬁc scenarios.
Recently, Pensieve [8] was proposed to further improve QoE
by using RL to train a neural network to generate ABR algo-
rithms, which effectively solves the limitations of existing ABR
algorithms. Alternatively, PPO-based policy optimization can be
utilized to learn more efﬁcient ABR strategies [9], [10]. How-
ever, due to the randomness of network bandwidth, RL-based
methods are difﬁcult to converge quickly or generate a large
amount of gradient variance [52]. Imitation learning [11], [12]
is used for solving MPC problems, but the method is only appli-
cable to known environments and cannot be used for complex
network scenarios. Fugu [13] combines classical control with
a learned network predictor, trained with supervised learning
in situ on data from the real deployment environment. Addi-
tionally, ABRL [14] converts ABR policy into a linear model
for better comprehension and safety, allowing human engineers
```

## 4. Metadatos PDF detectados

```json
{
  "format": "PDF 1.4",
  "title": "Optimizing Adaptive Video Streaming: Offline Reinforcement Learning and Meta-Learning in Diverse Networks",
  "author": "",
  "subject": "IEEE Transactions on Multimedia;2025;27; ;10.1109/TMM.2025.3604930",
  "keywords": "",
  "creator": "LaTeX with hyperref package",
  "producer": "Acrobat Distiller 11.0 (Windows); modified using iText® Core 7.2.4 (AGPL version) ©2000-2022 iText Group NV",
  "creationDate": "D:20251106144832+05'30'",
  "modDate": "D:20251111202430-05'00'",
  "trapped": "",
  "encryption": null
}
```

## 5. Mapa de secciones detectado

- p. 1: I. INTRODUCTION
- p. 2: II. BACKGROUND AND MOTIVATION
- p. 3: III. DEFINE OFFLINE META ABR ALGORITHM
- p. 4: IV. DESIGN
- p. 4: B. Handling Unbounded Video Streaming Sessions With
- p. 5: C. Learning meta-ABR Algorithm
- p. 6: V. EXPERIMENTS AND ANALYSIS
- p. 7: A. Implementation
- p. 7: B. Evaluation
- p. 8: QOE MODELS AND THEIR CORRESPONDING PARAMETERS
- p. 9: C. Generalization
- p. 9: D. Comparing State-of-The-Art RL Algorithms
- p. 11: E. Deep Dive
- p. 12: VI. REAL-WORLD DEPLOYMENT AND EVALUATION
- p. 13: VII. CONCLUTION
- p. 13: ACKNOWLEDGMENT
- p. 13: REFERENCES

## 6. Figuras, tablas, algoritmos y ecuaciones detectadas

- p. 2: Fig. 1.
- p. 3: Fig. 2.
- p. 5: Fig. 3.
- p. 6: Algorithm 1: Learning meta-ABR policies through ofﬂine
- p. 6: Algorithm 2: Generalizing meta-ABR policies across di-
- p. 6: Algorithm 1 and 2 demonstrate how to learn meta-ABR poli-
- p. 7: Fig. 5 shows the video bitrate, rebuffering time and smoothing
- p. 8: Fig. 4.
- p. 8: Fig. 5.
- p. 8: Fig. 6.
- p. 8: TABLE I
- p. 9: Fig. 7.
- p. 10: Fig. 8.
- p. 10: Fig. 9.
- p. 10: Fig. 10.
- p. 10: Fig. 12. We found that Fortuna can effectively utilize ofﬂine data
- p. 11: Fig. 11.
- p. 11: Fig. 12.
- p. 11: Fig. 13.
- p. 12: Fig. 14.
- p. 12: algorithm in real-world streaming media systems. In this sec-
- p. 12: Fig. 15.
- p. 12: Fig. 15 shows that the QoE under 5G and WiFi network con-
- p. 2: Fig. 1. However, due to lim-
- p. 2: Fig. 2, comprising 10427 streams,
- p. 5: Fig. 3. The training process is as follows:
- p. 7: Fig. 4, Fortuna has a
- p. 8: Fig. 6, For-
- p. 9: Fig. 7, 5G
- p. 9: Fig. 8, Fortuna can achieve better performance
- p. 9: Fig. 9, average QoE value increased
- p. 9: Fig. 10, the results demonstrated that the gen-
- p. 10: Fig. 11(a), the
- p. 10: Fig. 11(b) and (c), it can improve performance by more
- p. 11: Fig. 13, we found that solely considering network
- p. 12: Fig. 14, we found that the simple Buffer-Based

## 7. Lineas con posible contenido matematico/formal

- p. 1: `of experience (QoE) through learning adaptive bitrate (ABR)`
- p. 1: `and user QoE objectives. We propose Fortuna, a novel ofﬂine`
- p. 1: `network features, Fortuna further optimizes QoE by learning low-`
- p. 1: `adapt to different network bandwidths or different QoE ob-`
- p. 1: `chunks by dynamically optimizing QoE metrics, which has bet-`
- p. 1: `automatically adjust parameters, which can enhance QoE value`
- p. 1: `Recently, Pensieve [8] was proposed to further improve QoE`
- p. 1: `algorithms. Alternatively, PPO-based policy optimization can be`
- p. 1: `tionally, ABRL [14] converts ABR policy into a linear model`
- p. 2: `introduce Ruyi, an off-policy RL-based video streaming system`
- p. 2: `that integrates preference awareness into the QoE model and`
- p. 2: `algorithms must balance various QoE metrics, such as improv-`
- p. 2: `further reduce rebuffering and optimize QoE.`
- p. 2: `4) We evaluate QoE metrics in trace-driven and real-world`
- p. 2: `thus optimizing the user QoE in Fig. 1. However, due to lim-`
- p. 3: `Case 2: The QoE of video users is inﬂuenced by the un-`
- p. 3: `pact ABR algorithm decisions, affecting QoE outcomes. Since`
- p. 3: `RTT inﬂuences QoE, TCP congestion control algorithms like`
- p. 3: `Ofﬂine-RL is conducting online learning of the optimal policy`
- p. 3: `π∗from prior data D (i.e., off-policy data, expert demos, prior`
- p. 3: `an action at (i.e., chunk bitrate Rn) according to its policy. The`
- p. 3: `state st+1, providing the agent with a reward rt. The goal of`
- p. 3: `the ABR agent is to learn a policy that maximizes the expected`
- p. 3: `cumulative discounted reward value E[∞`
- p. 3: `t=0 γtrt]. The entire`
- p. 3: `M = (S, A, O, P, R),whereS isthestatespace,Aistheaction`
- p. 3: `function, and R is the reward function.`
- p. 3: `Reward rt: The environment evaluates different actions at, re-`
- p. 3: `ﬂects the quality of at, and improves the policy πθ. rt reﬂects the`
- p. 3: `ing frequency. We adopt the QoE metric provided by MPC [5]`
- p. 3: `n=1 |q (Rn+1) −q (Rn)|`
- p. 3: `of parameters θ that maximizes the expected cumulative reward`
- p. 3: `θ∗= arg max`
- p. 3: `Eπψi(τ)[R(τ)], where ψi = fθ(Mi).`
- p. 3: `r ψi is the task-speciﬁc policy parameter derived from the`
- p. 3: `r fθ denotes the meta-policy function that leverages experi-`
- p. 3: `The goal of meta-ABR is to train a meta-policy that`
- p. 4: `thereby optimizing the QoE objective across a variety of`
- p. 4: `RL method that reﬁnes the policy based on historical data [37].`
- p. 4: `LAW R(θ, φ, D) =`
- p. 4: `Z(s) log πθ(a|s) exp (QD(s, a) −Vφ(s))`
- p. 4: `r Vφ(s) is the value function for the behavior policy.`
- p. 4: `state s, scaling the overall loss term.`
- p. 4: `action a. The policy objective LAW R can be seen as a weighted`
- p. 4: `the optimal policy π∗and generalize across various types of net-`
- p. 4: `work conditions, i.e., learn the optimal policy π∗from prior data`
- p. 4: `D = (si, ai, si+1, ri). One of the simplest methods for applying`
- p. 4: `policy lacks data efﬁciency as it cannot make efﬁcient use of`
- p. 4: `the algorithm be capable of reusing any non-policy data (e.g.,`
- p. 4: `off-policy data, expert demos, prior runs of RL) during online`
- p. 4: `at maximizing QoE based on the dynamic playback buffer, con-`
- p. 4: `video QoE objective, MPC typically performs better than tradi-`
- p. 4: `resents the training stage. Starting from the initial stage k = 1,`
- p. 4: `Tk = min (Tinit + ΔT · (k −1), Tmax)`
- p. 4: `r k is the current training stage (k = 1, 2, 3, . . . ).`
- p. 4: `(Tinit = 10) during the early stages of training, with an increase`
- p. 4: `of 5 seconds at each stage (ΔT = 5), and the maximum video`
- p. 4: `stream length is 50 seconds (Tmax = 50). Then, during the ﬁrst,`
- p. 4: `ing time exploring actions that do not improve the policy in`
- p. 5: `The policy architecture of Fortuna is used to generate the ABR algo-`
- p. 5: `the adaptation phase. The advantage head is not involved in the policy update`
- p. 5: `tializations φ and θ for a value function Vφ and meta policy πθ,`
- p. 5: `Fortuna uses the RL Actor-Critic (policy and value network)`
- p. 5: `responding action at based on the meta-policy πθ, and the prob-`
- p. 5: `back the reward rt corresponding to at to the agent, and the goal`
- p. 5: `is to obtain the maximum cumulative reward from the environ-`
- p. 5: `ment. Therefore, the reward rt is set according to the parameters`
- p. 5: `of the QoE metric, reﬂecting the individual components of the`
- p. 5: `QoE metric.`
- p. 5: `ate bitrate that maximizes QoE objectives.`
- p. 5: `The value function loss, dependent on the meta-training data`
- p. 5: `mizing the value function loss LV , which makes Vφ(s) a closer`
- p. 5: `where LV (φ; D) = Es,a∼D[(Vφ(s) −QD(s, a))2] and QD(s, a)`
- p. 5: `in D. By minimizing the loss, we aim to accurately predict the`
- p. 5: `expected reward for each bitrate choice in a given state.`
- p. 5: `ditions, our policy architecture has two output heads: one for`
- p. 5: `predicting the action given the state, πθ(·|s), and another for`
- p. 5: `ing process, leading to more stable and efﬁcient training. Policy`
- p. 5: `θ′ ←θ−α1∇θLπ(θ; φ′, Dtr`
- p. 5: `i ), where Lπ =LAW R+λLADV`
- p. 5: `tions. The AWR loss is given in (2), and the advantage regression`
- p. 5: `loss LADV is given by:`
- p. 5: `LADV (θ; φ′, D) = Es,a∼D`
- p. 5: `This loss function aims to optimize the advantage function`
- p. 5: `Aθ(s, a), ensuring that the policy selects bitrates that lead to`
- p. 6: `policy is consistent with both the value and action-value func-`
- p. 6: `tions. This helps improve the policy’s ability to adapt video bi-`
- p. 6: `Unlike the inner loop, we optimize the initial policy param-`
- p. 6: `EMi[LAW R(θ −α1∇θLπ(θ, φ′`
- p. 6: `where Lπ is deﬁned in (4) and LAW R is deﬁned in (2).`
- p. 6: `y = σ(Wx + b),`
- p. 6: `w = Wwtz,`
- p. 6: `W ∗= reshape(w[0 : d2]),`
- p. 6: `b∗= w[d2 : (d2 + d)].`
- p. 6: `y = σ(W ∗x + b∗).`
- p. 6: `rank(ΔW ∗) ≤min(d, c),`
- p. 6: `(policy), η1 (value); outer-loop learning rates α2, η2;`
- p. 6: `4: Initialize meta-policy parameters θ and value function`
- p. 6: `Tk = min(Tinit + ΔT · (k −1), Tmax)`
- p. 6: `Adapt policy: θ′ ←θ −α1∇θLπ(θ; φ′; Dtr`
- p. 6: `Lπ = LAW R + λLADV`
- p. 6: `Meta-update policy:`
- p. 6: `experience buffer D, meta-policy πθ, and meta-value`
- p. 6: `3: Initialize policy parameters θ0 = θ and value function`
- p. 6: `parameters φ0 = φ`
- p. 6: `Adapt policy: θt+1 ←θt −α1∇θLπ(θt; φt+1; D)`
- p. 6: `ferent network traces and QoE metrics. Further, we analyze the`
- p. 7: `The QoE metric parameters of (1) are set: N is 8, μ1 is 4.3,`
- p. 7: `is 100, γ = 0.99, Relu activation function [47] and the Adam`
- p. 7: `to the change of the loss function, the learning rates for the`
- p. 7: `the reward value fed back to the agent by the environment is`
- p. 7: `the QoE metric value.`
- p. 7: `effectively improve QoE.`
- p. 7: `problem that aims to maximize QoE for several upcoming`
- p. 7: `chunks. By focusing directly on improving QoE, MPC often`
- p. 7: `evaluate the overall distribution of QoE for different ABR algo-`
- p. 7: `lative probability and QoE. As shown in Fig. 4, Fortuna has a`
- p. 7: `higher QoE value than the existing ABR algorithms, due to the`
- p. 7: `improve QoE, but RMPC leads to insufﬁcient buffer utilization;`
- p. 7: `QoE breakdown: To better understand the performance of`
- p. 7: `Fortuna, we compare the individual components of QoE metric.`
- p. 7: `penalty, i.e., the components of QoE metric. Experimental re-`
- p. 7: `different networks to achieve higher QoE values. rebuffering`
- p. 7: `form existing solutions in every QoE metric. Instead, it is able to`
- p. 7: `maximize QoE by optimizing every metric. For example, when`
- p. 7: `of three common QoE models, highlighting their key character-`
- p. 7: `1) Linear QoE: Advantages: Simple and intuitive, suitable`
- p. 7: `2) Logarithmic QoE: QoE models user perception with`
- p. 7: `q(R) = log(R/Rmin).`
- p. 8: `Compare the QoE metrics of Fortuna and existing ABR algorithms on FCC, HSDPA/3G, and Belgium/4G networks. Examine the distribution of average`
- p. 8: `QoE values for each ABR algorithm.`
- p. 8: `Comparing the QoE metric individual compoments of Fortuna and existing ABR algorithms on FCC, HSDPA, and Belgium/4G networks. Error bars are`
- p. 8: `Comparison of Fortuna with existing ABR algorithms on FCC and HSDPA networks. QoE metrics are considered as listed in Table I, with results`
- p. 8: `QoE. Application: Ideal for adaptive bitrate streaming in`
- p. 8: `3) High-Deﬁnition QoE: Uses predeﬁned quality levels`
- p. 8: `ABR strategies tailored to various QoE objectives. Un-`
- p. 8: `QOE MODELS AND THEIR CORRESPONDING PARAMETERS`
- p. 9: `reward=[1, 2, 3, 12, 15, 20], (more detail in [55]), total video`
- p. 9: `maximize QoE objectives and minimize stall time as much as`
- p. 9: `that Fortuna can reduce stall time and maximize QoE even in`
- p. 9: `compared to Genet [19] in Fig. 9, average QoE value increased`
- p. 9: `The gap in QoE values is 2.8%. This ﬁnding suggests that our`
- p. 10: `Comparing the QoE metrics of Fortuna and Genet ABR algorithms on`
- p. 10: `to converge quickly, achieving an average reward improvement`
- p. 10: `function in the PPO algorithm mitigates policy ﬂuctuations, it`
- p. 10: `than 7.5%-4×, the average QoE can be improved by 3.7%.`
- p. 11: `Comparing how underlying TCP network characteristics affect QoE`
- p. 12: `When considering RTT, CWND, and Queue delay, QoE can`
- p. 12: `with Pensieve, BOLA, and MPC, and the collected QoE`
- p. 12: `Fig. 15 shows that the QoE under 5G and WiFi network con-`
- p. 12: `bly. At the same time, we found that the QoE of various ABR`
- p. 12: `QoE values by 2.9%–5.1%, 5.2%–12.5%, and 2.6%–11.2%,`
- p. 13: `Comparing the QoE metric of Fortuna and existing ABR algorithms`
- p. 13: `used in real-world streaming media networks. It can also max-`
- p. 13: `imize QoE values under different conditions and improve user`
- p. 13: `trol to further reduce rebuffering time, optimizing QoE ob-`
- p. 13: `isting approaches, with an average QoE improvement ranging`
- p. 13: `unseen network conditions and QoE user preferences.`
- p. 13: `[6] A. Lekharu, S. Kumar, A. Sur, and A. Sarkar, “A QoE aware LSTM`
- p. 13: `QoE preference for video streaming,” in Proc. IEEE INFOCOM 2022-`
- p. 13: `[23] X. Wei et al., “Reinforcement learning-based qoe-oriented dynamic`
- p. 14: `Off-policy`
- p. 14: `meta-policy search,” in Proc. ICLR, 2019, pp. 1–25.`
- p. 14: `power, and QoE implications,” in Proc. ACM SIGCOMM Conf., 2021,`
- p. 14: `policy meta-reinforcement learning via probabilistic context variables,” in`

## 8. Extraccion tecnica cruda por categorias


### 8.1. modelo algoritmo arquitectura

Palabras clave usadas: `model, algorithm, architecture, framework, policy, neural, network, deep reinforcement, reinforcement learning, DRL, DQN, PPO, A2C, A3C, actor, critic, agent, meta, meta-learning, MAML, offline reinforcement, curriculum, VAE, variational autoencoder, LSTM, BiLSTM, GRU, CNN, predictor, bandwidth prediction, Plume, Gelato, Ahaggar, CausalSim, IMDP, domain-specific prior`

**Fragmento 1 - p. 5 - score 7:**

Fortuna uses the RL Actor-Critic (policy and value network) approach in Fig. 3. The training process is as follows: Step 1: Input is the state st, which includes 7 variables, namely: throughtput Ct, chunk download time dk(Rk)/Ck, next chunk sizes Rn+1, RTT, and the buffer size Bt, remaining chunks N and chunk bitrate Rn. Neural networks: The number of hidden layers is 1, and 128 convolution kernels and a fully connected network are used for feature extraction. The size of the convolution kernel is 4 and the step size is 1. Step 2: When receiving the state st, the agent selects the cor- responding action at based on the meta-policy πθ, and the prob- ability distribution is deﬁned as : (st, at) →[0, 1], (st, at) is the probability that the action at may take in state st.

**Fragmento 2 - p. 7 - score 7:**

Since the playback buffer is relatively stable, it can effectively improve QoE. Pensieve [8]: ABR algorithm based on deep reinforcement learning (DRL), generating ABR algorithm by training neural network. However, the original Pensieve struggled with conver- gence due to the variability in network conditions when using the A3C algorithm. Therefore, we employed variance reduction techniques [52] in the training process to develop a more effec- tive ABR algorithm. RMPC: makes decisions about video bitrate by tackling a problem that aims to maximize QoE for several upcoming chunks. By focusing directly on improving QoE, MPC often performs better than methods that rely on ﬁxed rules [5].

**Fragmento 3 - p. 1 - score 6:**

Recently, Pensieve [8] was proposed to further improve QoE by using RL to train a neural network to generate ABR algo- rithms, which effectively solves the limitations of existing ABR algorithms. Alternatively, PPO-based policy optimization can be utilized to learn more efﬁcient ABR strategies [9], [10]. How- ever, due to the randomness of network bandwidth, RL-based methods are difﬁcult to converge quickly or generate a large amount of gradient variance [52]. Imitation learning [11], [12] is used for solving MPC problems, but the method is only appli- cable to known environments and cannot be used for complex network scenarios. Fugu [13] combines classical control with a learned network predictor, trained with supervised learning in situ on data from the real deployment environment.

**Fragmento 4 - p. 1 - score 6:**

Addi- tionally, ABRL [14] converts ABR policy into a linear model for better comprehension and safety, allowing human engineers to verify it while slightly increasing the average stall rate by 0.8%. Another approach is to employ meta-RL techniques like MAML [15], [16], [17] or Pearl [18] to adaptive to various network conditions. Moreover, Genet [19] introduces increas- ingly challenging environments through a curriculum learning 1520-9210 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission.

**Fragmento 5 - p. 5 - score 6:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8189 Fig. 3. The policy architecture of Fortuna is used to generate the ABR algo- rithm, solid lines show the data ﬂow during the forward pass, while dashed lines represent the gradient ﬂow during the backward pass, which occurs only during the adaptation phase. The advantage head is not involved in the policy update process of the outer loop. that the agent can reset and quickly retry from an idle state. We gradually increase the length of video streaming sessions throughout the entire training process. Thus, initially, the agent learns to short video streaming sessions sequences.

**Fragmento 6 - p. 10 - score 6:**

Ten- sorFlow TensorBoard was used to monitor the training process during the experimental procedures. As shown in Fig. 11(a), the original Pensieve was trained using A3C, due to the random na- ture of network conditions, and the ﬂuctuations were very dras- tic, thus we used Variance reduction to optimize training the per- formance more stable. PEARL, a context-driven meta-learning approach, tends to meta-overﬁtting, which leads to suboptimal performance in unseen network conditions. Contrastingly, For- tuna leverages ofﬂine data to rapidly learn meta-ABR policies, resulting in an improvement of over 6.6%–20.1% the previous performance. Additionally, we also compared Fortuna with online meta-RL methods, using PPO to optimize the ABR algorithm, as shown in Fig.

**Fragmento 7 - p. 10 - score 6:**

12. We found that Fortuna can effectively utilize ofﬂine data to converge quickly, achieving an average reward improvement of 9%. In contrast, Meta-PPO (However, the ofﬁcial code has not been released, and we have done our best to implement the algorithm according to the pseudocode description in the paper.) [60] converges more slowly due to the need for real- time interaction with the ABR environment. Although the clip function in the PPO algorithm mitigates policy ﬂuctuations, it remains relatively stable. Curriculum Learning: In this part, we utilize Curriculum Learning to gradually increase the complexity of the video stream in order to quickly adapt the bitrate to new network conditions.

**Fragmento 8 - p. 11 - score 6:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8195 Fig. 11. Comparison of training epochs and training time with and without curriculum learning by increasing the complexity of video streaming, i.e., from short video streams to long video streams. Fig. 12. The comparison of Fortuna with the existing state-of-the-art meta- ABR algorithm, Meta-PPO ABR [60]. video streams to more complex, longer video streams, en- abling it to better cope with ﬂuctuating network environ- ments and ensuring high-quality video streams under varying conditions. E. Deep Dive In this section, we explore microbenchmarks tailored to deepen our comprehension of Fortuna.

**Fragmento 9 - p. 14 - score 6:**

[40] A. Gupta, V. Kumar, C. Lynch, S. Levine, and K. Hausman, “Relay pol- icy learning: Solving long-horizon tasks via imitation and reinforcement learning,” in Proc. Conf. Robot Learn., 2019, pp. 1–13. [41] T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine, “Soft actor- critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor,” in Proc. Int. Conf. Mach. Learn., 2018, pp. 1861–1870. [42] J. Rothfuss, D. Lee, I. Clavera, T. Asfour, and P. Abbeel, “Promp: Proximal meta-policy search,” in Proc. ICLR, 2019, pp. 1–25. [43] C. M. Bishop and N. M. Nasrabadi, Pattern Recognition and Machine Learning, vol. 4. Berlin, Germany: Springer, 2006. [44] C. Finn and S.

**Fragmento 10 - p. 1 - score 5:**

IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 8185 Optimizing Adaptive Video Streaming: Ofﬂine Reinforcement Learning and Meta-Learning in Diverse Networks Ling Yi , Yongbin Qin , and Ruizhang Huang Abstract—Recent years have seen the optimization of quality of experience (QoE) through learning adaptive bitrate (ABR) algorithms from internet video streams. However, the complex nature of the real-world Internet, characterized by heavy-tailed behavior, diversity, and unpredictability, hinder the effective learning of off-the-shelf reinforcement learning (RL)-based ABR algorithms. As a result, existing methods inevitably fail to achieve optimal performance under various network conditions and user QoE objectives.

**Fragmento 11 - p. 1 - score 5:**

We propose Fortuna, a novel ofﬂine meta RL ABR algorithm that can effectively learn from these heavy-tailed internet data features and become more practical. Fortuna is primarily divided into two phases. In the ofﬂine phase, Fortuna utilizes diverse ofﬂine data for learning to reduce the costly online RL interaction expense, while in the online phase, we gradually increase video streaming sessions complexity through curriculum learning to quickly adapt to speciﬁc network conditions. Fortuna then utilizes meta-learning to optimize ABR policies and enhance generalization. Additionally, to better learn network features, Fortuna further optimizes QoE by learning low- level TCP congestion control information.

**Fragmento 12 - p. 2 - score 5:**

Fortuna is primarily divided into two stages. In the ofﬂine phase, it leverages domain knowledge to ﬁrst learn from expert data, and then collects runs of RL data. In the online phase, optimization takes place, gradually increasing the complexity of the video stream through curriculum learn- ing [20], [29]. However, ofﬂine ABR strategies cannot adapt to new network conditions. To enhance the generalization of Fortuna, we employ meta-learning for continuous optimization. Furthermore, ABR algorithms interact with TCP congestion control mechanisms, such as congestion window (CWND) and round-trip time (RTT). To better understand the underlying net- work behavior features, we consider TCP congestion control to facilitate the effective learning of ABR algorithms.

**Fragmento 13 - p. 3 - score 5:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8187 Fig. 2. Visualize network features, as well as video quality and buffering time of existing ABR algorithms, on the Puffer dataset. ofﬂine RL enables the model to learn the features and patterns across different distributions, enhancing its generalization abil- ity [31]. Case 2: The QoE of video users is inﬂuenced by the un- derlying TCP congestion control protocol [32], such as RTT. We observe varying network throughputs, ranging from 0 to 250 Mbps, with different RTT values across users. For example, users with a throughput of 75 Mbps exhibit a wide range of RTT values, while those with throughput between 25 and 50 Mbps of- ten experience high latency and a broader range of RTT values.

**Fragmento 14 - p. 5 - score 5:**

As its ABR strategy improves, we extend the episode length, making the problem more challenging. The concept of gradually increas- ing video stream sequence length—and, consequently, prob- lem complexity—during training realizes curriculum learning for ABR [29]. C. Learning meta-ABR Algorithm Fortuna is an ofﬂine meta-RL ABR algorithm that learns ini- tializations φ and θ for a value function Vφ and meta policy πθ, respectively, enabling rapid adaptation to a new network condi- tion encountered at meta-test time via gradient descent. Fortuna mainly consists of inner loops and outer loops [15], [42]. Next, we will provide a detailed overview of the implementation pro- cess.

**Fragmento 15 - p. 6 - score 5:**

Traditional gradient descent updates result in rank-1 changes, whereas with the latent vector z, the rank of weight updates is bounded by: rank(ΔW ∗) ≤min(d, c), allowing higher-rank transformations and richer adaptation strategies. Algorithm 1: Learning meta-ABR policies through ofﬂine RL with gradually increasing video stream length 1: Require: network environments {Mi}; ofﬂine datasets Di containing trajectories τ: (st, at, rt) 2: Require: Initial video stream length Tinit, increment ΔT, maximum stream length Tmax 3: Hyperparameters: Inner-loop learning rates α1 (policy), η1 (value); outer-loop learning rates α2, η2; training iterations k 4: Initialize meta-policy parameters θ and value function parameters φ 5: for k iterations do 6: for each network environment Mi do 7: Sample disjoint meta-training and meta-test data batches Dtr i and Dts i from Di 8: Calculate video stream length for the current stage: Tk = min(Tinit + ΔT · (k −1), Tmax) 9: Adapt value function: φ′ ←φ −η1∇φLV (φ; Dtr i ) 10: Adapt policy: θ′ ←θ −α1∇θLπ(θ; φ′; Dtr i ), where Lπ = LAW R + λLADV 11: end for 12: Meta-update value function: φ ←φ −η2  i ∇φLV (φ′; Dts i ) 13: Meta-update policy: θ ←θ −α2  i ∇θLAW R(θ′; φ′; Dts i ) 14: end for Algorithm 2: Generalizing meta-ABR policies across di- verse environments 1: Input: Test network environment Mj, ofﬂine experience buffer D, meta-policy πθ, and meta-value function Vφ 2: Hyperparameters: Learning rates α1, η1; number of adaptation steps k 3: Initialize policy parameters θ0 = θ and value function parameters φ0 = φ 4: for k adaptation steps do 5: Adapt value function: φt+1 ←φt −η1∇φLV (φt; D) 6: Adapt policy: θt+1 ←θt −α1∇θLπ(θt; φt+1; D) 7: end for In summary, the latent vector z enhances ABR algorithms by enabling dynamic weight and bias generatio

**Fragmento 16 - p. 12 - score 5:**

MPC predicts bitrates based on past network bandwidth. However, in a real environ- ment, these network characteristics are complex and variable, inﬂuenced by factors such as TCP and varying user preferences, making adaptation to real network conditions difﬁcult. Fugu ex- hibits weaker generalization in unknown network conditions us- ing supervised learning, whereas Fortuna consistently performs well in these unknown networks and user preferences. By learn- ing these features and underlying TCP controls, it can better understand the behavioral characteristics of the network. In addi- tion, we also found that off-the-shelf meta-learning-based ABR algorithms face challenges in adapting to new network condi- tions.

**Fragmento 17 - p. 13 - score 5:**

31st ACM Workshop Netw. Operating Syst. Support Digit. Audio Video, 2021, pp. 17–24. [8] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video streaming with pensieve,” in Proc. Conf. ACM Special Int. Group Data Commun. (SIGCOMM), 2017, pp. 197–210. [9] T. Huang, R.-X. Zhang, and L. Sun, “Zwei: A self-play reinforcement learning framework for video transmission services,” IEEE Trans. Multi- media, vol. 24, pp. 1350–1365, 2021. [10] A. Bentaleb, M. N. Akcay, M. Lim, A. C. Begen, and R. Zimmer- mann, “BoB: Bandwidth prediction for real-time communications using heuristic and reinforcement learning,” IEEE Trans. Multimedia, vol. 25, pp. 6930–6945, 2022. [11] T. Huang et al., “Quality-aware neural adaptive video streaming with life- long imitation learning,” IEEE J.

**Fragmento 18 - p. 13 - score 5:**

Sci., vol. 569, pp. 786–803, 2021. [24] V. Mnih, “Playing Atari with deep reinforcement learning,” 2013, arXiv:1312.5602. [25] H. Mao et al., “Park: An open platform for learning-augmented computer systems,” in Proc. Adv. Neural Inf. Process. Syst., 2019, pp. 1–20. [26] V. H. Pong, A. V. Nair, L. M. Smith, C. Huang, and S. Levine, “Ofﬂine meta-reinforcement learning with online self-supervision,” in Proc. Int. Conf. Mach. Learn., 2022, pp. 17811–17829. [27] S. Floyd and E. Kohler, “Internet research needs better models,” ACM SIGCOMM Comput. Commun. Rev., vol. 33, no. 1, pp. 29–34, 2003. [28] S. Floyd and V. Paxson, “Difﬁculties in simulating the internet,” IEEE/ACM Trans. Netw., vol.

**Fragmento 19 - p. 13 - score 5:**

Sel. Areas Commun., vol. 38, no. 10, pp. 2324–2342, Oct. 2020. [12] W. Li et al., “An apprenticeship learning approach for adaptive video streaming based on chunk quality and user preference,” IEEE Trans. Mul- timedia, vol. 25, pp. 2488–2502, 2022. [13] F. Y. Yan et al., “Learning in situ: A randomized experiment in video streaming,” in Proc. 17th USENIX Symp. Networked Syst. Des. Implemen- tation, 2020, pp. 495–511. [14] H. Mao et al., “Real-world video adaptation with reinforcement learning,” in Proc ICML workshop, 2019, pp. 1–10. [15] C. Finn, P. Abbeel, and S. Levine, “Model-agnostic meta-learning for fast adaptation of deep networks,” in Proc. Int. Conf. Mach. Learn., 2017, pp.

**Fragmento 20 - p. 13 - score 5:**

1126–1135. [16] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, and L. Sun, “Learning tai- lored adaptive bitrate algorithms to heterogeneous network conditions: A domain-speciﬁc priors and meta-reinforcement learning approach,” IEEE J. Sel. Areas Commun., vol. 40, no. 8, pp. 2485–2503, Aug. 2022. [17] S. Wang, J. Lin, and Y. Dai, “MMVS: Enabling robust adaptive video streaming for wildly ﬂuctuating and heterogeneous networks,” IEEE Trans. Multimedia, vol. 26, pp. 11018–11030, 2024. [18] N. Kan et al., “Improving generalization for neural adaptive video stream- ing via meta reinforcement learning,” in Proc. 30th ACM Int. Conf. Mul- timedia, 2022, pp. 3006–3016. [19] Z. Xia, Y. Zhou, F.

**Fragmento 21 - p. 14 - score 5:**

Levine, “Meta-learning and universality: Deep represen- tations and gradient descent can approximate any learning algorithm,” in Proc. ICLR, 2018, pp. 1–20. [45] E. Mitchell, R. Rafailov, X. B. Peng, S. Levine, and C. Finn, “Ofﬂine meta-reinforcementlearningwithadvantageweighting,”inProc.Int.Conf. Mach. Learn., 2021, pp. 7780–7791. [46] R. Netravali et al., “Mahimahi: Accurate {Record-and-Replay} for {HTTP},” in Proc. USENIX Annu. Tech. Conf., 2015, pp. 417–429. [47] J. Schmidt-Hieber, “Nonparametric regression using deep neural net- works with ReLU activation function,” Ann. Statist., vol. 48, no. 4, pp. 1875–1897, 2020. [48] Z. Zhang, “Improved adam optimizer for deep neural networks,” in Proc.

**Fragmento 22 - p. 1 - score 4:**

Experimental results from trace-driven and real-world scenarios demonstrate that Fortuna enhances learning efﬁciency by more than 7.5%–4 ×, reduces stall time by 4.6%–14.2%, and generalizes to different network conditions and video streams. Index Terms—Adaptive bitrate algorithm, ofﬂine meta reinforcement learning, quality of experience. I. INTRODUCTION V IDEO streaming is the primary internet application, ac- countingfornearly75%ofalltrafﬁc[1].Inadaptivebitrate (ABR) video streaming, videos are typically divided into various small video chunks or segments. Video users can request spe- ciﬁc video chunks based on their preferences and network con- ditions.


### 8.2. estado inputs features

Palabras clave usadas: `state, input, feature, observation, throughput, bandwidth, buffer, download time, chunk size, history, past, remaining, TCP, RTT, CWND, device, resolution, content, CMCD, CMSD, network condition, environment, latent, context, trace features`

**Fragmento 1 - p. 5 - score 8:**

Fortuna uses the RL Actor-Critic (policy and value network) approach in Fig. 3. The training process is as follows: Step 1: Input is the state st, which includes 7 variables, namely: throughtput Ct, chunk download time dk(Rk)/Ck, next chunk sizes Rn+1, RTT, and the buffer size Bt, remaining chunks N and chunk bitrate Rn. Neural networks: The number of hidden layers is 1, and 128 convolution kernels and a fully connected network are used for feature extraction. The size of the convolution kernel is 4 and the step size is 1. Step 2: When receiving the state st, the agent selects the cor- responding action at based on the meta-policy πθ, and the prob- ability distribution is deﬁned as : (st, at) →[0, 1], (st, at) is the probability that the action at may take in state st.

**Fragmento 2 - p. 11 - score 7:**

This delay can trigger the under- lying TCP connection to enter slow start mode, a behavior Fig. 13. Comparing how underlying TCP network characteristics affect QoE in the Belgium network. known as TCP slow start restart [61]. Slow start, in turn, hin- ders the video player from fully utilizing the available band- width, especially for small chunk sizes (low bitrates). This be- havior makes simulation challenging as it fundamentally links network throughput to the employed ABR algorithm. For in- stance, strategies that rapidly ﬁll the buffer will experience more instances of slow start, consequently reducing network utilization. Additionally, in the TCP congestion control process, we need to control network bandwidth based on queue delay, which in- volves subtracting the minimum RTT observed from the cur- rent RTT and adjusting CWND (congestion window) based on packet behavior.

**Fragmento 3 - p. 12 - score 6:**

8196 IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 Fig. 14. Long-duration video streaming sessions, i.e., varying network conditions and different user video streams. The average values for video quality and buffering are shown, with error bars spanning ± one standard deviation from the average. When considering RTT, CWND, and Queue delay, QoE can improve by 1.2-9.4%. This suggests that in a real network en- vironment, we cannot simply rely on network bandwidth for evaluation, but need to incorporate TCP congestion control for a better understanding of the ABR algorithm. These network behavioral characteristics contribute to a better understanding and learning of ABR algorithms.

**Fragmento 4 - p. 2 - score 5:**

Fortuna is primarily divided into two stages. In the ofﬂine phase, it leverages domain knowledge to ﬁrst learn from expert data, and then collects runs of RL data. In the online phase, optimization takes place, gradually increasing the complexity of the video stream through curriculum learn- ing [20], [29]. However, ofﬂine ABR strategies cannot adapt to new network conditions. To enhance the generalization of Fortuna, we employ meta-learning for continuous optimization. Furthermore, ABR algorithms interact with TCP congestion control mechanisms, such as congestion window (CWND) and round-trip time (RTT). To better understand the underlying net- work behavior features, we consider TCP congestion control to facilitate the effective learning of ABR algorithms.

**Fragmento 5 - p. 3 - score 5:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8187 Fig. 2. Visualize network features, as well as video quality and buffering time of existing ABR algorithms, on the Puffer dataset. ofﬂine RL enables the model to learn the features and patterns across different distributions, enhancing its generalization abil- ity [31]. Case 2: The QoE of video users is inﬂuenced by the un- derlying TCP congestion control protocol [32], such as RTT. We observe varying network throughputs, ranging from 0 to 250 Mbps, with different RTT values across users. For example, users with a throughput of 75 Mbps exhibit a wide range of RTT values, while those with throughput between 25 and 50 Mbps of- ten experience high latency and a broader range of RTT values.

**Fragmento 6 - p. 3 - score 5:**

These heterogeneous network characteristics signiﬁcantly im- pact ABR algorithm decisions, affecting QoE outcomes. Since RTT inﬂuences QoE, TCP congestion control algorithms like BBR [33] and CUBIC [34] adjust data sending rates to opti- mize RTT performance. ABR algorithms must adapt to chang- ing network conditions to improve video streaming quality by leveraging these underlying network characteristics. Case 3: Learning ABR strategies often leads to poor deci- sions when faced with unknown network conditions, resulting in suboptimal video quality and increased rebuffering time. We use the Puffer dataset, with a duration of 1000 hours and a time interval of 1 s, where the network bandwidth ranges from 0 to 400 Mbps.

**Fragmento 7 - p. 6 - score 5:**

Traditional gradient descent updates result in rank-1 changes, whereas with the latent vector z, the rank of weight updates is bounded by: rank(ΔW ∗) ≤min(d, c), allowing higher-rank transformations and richer adaptation strategies. Algorithm 1: Learning meta-ABR policies through ofﬂine RL with gradually increasing video stream length 1: Require: network environments {Mi}; ofﬂine datasets Di containing trajectories τ: (st, at, rt) 2: Require: Initial video stream length Tinit, increment ΔT, maximum stream length Tmax 3: Hyperparameters: Inner-loop learning rates α1 (policy), η1 (value); outer-loop learning rates α2, η2; training iterations k 4: Initialize meta-policy parameters θ and value function parameters φ 5: for k iterations do 6: for each network environment Mi do 7: Sample disjoint meta-training and meta-test data batches Dtr i and Dts i from Di 8: Calculate video stream length for the current stage: Tk = min(Tinit + ΔT · (k −1), Tmax) 9: Adapt value function: φ′ ←φ −η1∇φLV (φ; Dtr i ) 10: Adapt policy: θ′ ←θ −α1∇θLπ(θ; φ′; Dtr i ), where Lπ = LAW R + λLADV 11: end for 12: Meta-update value function: φ ←φ −η2  i ∇φLV (φ′; Dts i ) 13: Meta-update policy: θ ←θ −α2  i ∇θLAW R(θ′; φ′; Dts i ) 14: end for Algorithm 2: Generalizing meta-ABR policies across di- verse environments 1: Input: Test network environment Mj, ofﬂine experience buffer D, meta-policy πθ, and meta-value function Vφ 2: Hyperparameters: Learning rates α1, η1; number of adaptation steps k 3: Initialize policy parameters θ0 = θ and value function parameters φ0 = φ 4: for k adaptation steps do 5: Adapt value function: φt+1 ←φt −η1∇φLV (φt; D) 6: Adapt policy: θt+1 ←θt −α1∇θLπ(θt; φt+1; D) 7: end for In summary, the latent vector z enhances ABR algorithms by enabling dynamic weight and bias generatio

**Fragmento 8 - p. 12 - score 5:**

MPC predicts bitrates based on past network bandwidth. However, in a real environ- ment, these network characteristics are complex and variable, inﬂuenced by factors such as TCP and varying user preferences, making adaptation to real network conditions difﬁcult. Fugu ex- hibits weaker generalization in unknown network conditions us- ing supervised learning, whereas Fortuna consistently performs well in these unknown networks and user preferences. By learn- ing these features and underlying TCP controls, it can better understand the behavioral characteristics of the network. In addi- tion, we also found that off-the-shelf meta-learning-based ABR algorithms face challenges in adapting to new network condi- tions.

**Fragmento 9 - p. 14 - score 5:**

IEEE/ACM 26th Int. Symp. Qual. Service, 2018, pp. 1–2. [49] “FCC broadband dataset,” (n.d.). [Online].Available: http://data.fcc. gov/download/measuring-broadband-America/2016/data-raw-2016- jun.tar.gz [50] “Norway HSDPA bandwidth logs,” (n.d.). [Online]. Available: http:// home.iﬁ.uio.no/paalh/dataset/hsdpa-tcp-logs/ [51] “Belgium 4G/LTE bandwidth logs (bonus),” (n.d.). [Online]. Available: http://users.ugent.be/jvdrhoof/dataset-4g/logs/logs_all.zip [52] H. Mao, S. B. Venkatakrishnan, M. Schwarzkopf, and M. Alizadeh, “Vari- ance reduction for reinforcement learning in input-driven environments,” ICLR, 2019, pp. 1–20. [53] A. Narayanan et al., “Lumos5g: Mapping and predicting commercial mmWave 5G throughput,” in Proc.

**Fragmento 10 - p. 2 - score 4:**

This is because online learning of ABR al- gorithms does not explore safely and cannot effectively learn from these complex network features [25], [26]. Speciﬁcally,inreal-worldadaptivevideostreamingscenarios, learning algorithms rely on speciﬁc data or environments to train them. However, Internet data is often vast and massive, and ABR algorithms adapt to new scenarios by learning from these net- work characteristics. Because network conditions continually change over time, and due to different user preferences, ABR algorithms must balance various QoE metrics, such as improv- ing video quality and reducing rebuffering time. Unfortunately, learning algorithms often perform well on the simple training and testing datasets, but real internet data features are complex and variable, exhibiting heavy-tailed characteristics.

**Fragmento 11 - p. 2 - score 4:**

4) We evaluate QoE metrics in trace-driven and real-world environments, and generalize to 3G, 4G, 5G, WiFi, syn- theticnetworks,anddifferentvideostreams(SectionV-C), and deploy the algorithms in streaming media systems (Section VI). II. BACKGROUND AND MOTIVATION The HTTP-based ABR algorithm dynamically selects the ap- propriate bitrate for video segments by monitoring network bandwidth and player buffer status in real-time. It delivers high-quality video when network conditions are good and low- ers the quality during poorer conditions to prevent buffering, thus optimizing the user QoE in Fig. 1. However, due to lim- ited network bandwidth, ABR algorithms may not always re- quest the optimal bitrate.

**Fragmento 12 - p. 5 - score 4:**

Output masking is employed as part of the solution. For each video, a mask, represented as a binary vector [m1, m2, . . ., mk], is used to constrain the probability distribution of the output, including only the bitrate levels that the video supports. This mask, in conjunction with softmax [43], determines which bi- trates [i1, i2, . . ., ik] in the NN output are valid. Inner-Loop: The inner loop refers to real-time bitrate selec- tion adjustments based on the current network conditions and the existing strategy, aiming to optimize the short-term user ex- perience. For ABR algorithms, the inner loop uses bandwidth predictions, buffer status, and chunk sizes to select an appropri- ate bitrate that maximizes QoE objectives.

**Fragmento 13 - p. 7 - score 4:**

Fugu and Comyco’s inability to adaptively change strategies and long-term decision problems using imitative learning. Additionly, it is essentially solving the RMPC problems [5]. However, RMPC estimates the network bandwidth too conservatively use model control. For example, when the network throughput becomes low, it should make full use of the playback buffer and request a low bitrate to improve QoE, but RMPC leads to insufﬁcient buffer utilization; similarly, BOLA only considers the buffer usage. As shown, these simple ﬁxed heuristics are not applicable to complex net- work throughput. Additionally, Pensieve cannot adaptively learn network characteristics, resulting in inaccurate predictions un- der certain network conditions.

**Fragmento 14 - p. 11 - score 4:**

This element plays a vital role in ensuring high throughput and minimal latency. Therefore, when network con- gestion occurs, we should adjust the video bitrate based on TCP congestion control to provide a better user experience. In other words, bydynamicallymodifyingthevideobitrateinresponseto the TCP congestion window and queue delay, we can maintain an optimal balance between throughput and latency, ensuring smooth video streaming even in ﬂuctuating network conditions. To validate this behavior, we conducted 4 sets of experiments, one solely considering network bandwidth for selecting the bi- trate, while the other took TCP congestion control into account.

**Fragmento 15 - p. 13 - score 4:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8197 Fig. 15. Comparing the QoE metric of Fortuna and existing ABR algorithms on 5G, 4G and WiFi network conditions. In the bar chart, the averages are listed, and the error bars span ± one standard deviation from the average. by training in a simulated environment, can generalize and be used in real-world streaming media networks. It can also max- imize QoE values under different conditions and improve user experience. VII. CONCLUTION We introduce Fortuna, a novel ofﬂine RL-based adaptive video streams technique that effectively adapts to real-world Internet conditions, and combines with TCP congestion con- trol to further reduce rebuffering time, optimizing QoE ob- jectives.

**Fragmento 16 - p. 1 - score 3:**

We propose Fortuna, a novel ofﬂine meta RL ABR algorithm that can effectively learn from these heavy-tailed internet data features and become more practical. Fortuna is primarily divided into two phases. In the ofﬂine phase, Fortuna utilizes diverse ofﬂine data for learning to reduce the costly online RL interaction expense, while in the online phase, we gradually increase video streaming sessions complexity through curriculum learning to quickly adapt to speciﬁc network conditions. Fortuna then utilizes meta-learning to optimize ABR policies and enhance generalization. Additionally, to better learn network features, Fortuna further optimizes QoE by learning low- level TCP congestion control information.

**Fragmento 17 - p. 1 - score 3:**

State-of-the-art MPC algorithm [5] uses future video chunks by dynamically optimizing QoE metrics, which has bet- ter performance than the simple ﬁxed schemes e.g., BOLA, RB. However, MPC relies on accurate network bandwidth pre- dictions, especially on future networks. Due to the variability of network bandwidth, MPC is difﬁcult to predict accurately, but inaccurate predictions may cause future video freezes and low-quality video etc. Additionally, since BOLA and MPC can- not adjust parameters according to speciﬁc network conditions and are too sensitive to parameters, then Oboe [6] is proposed to automatically adjust parameters, which can enhance QoE value in speciﬁc scenarios.

**Fragmento 18 - p. 2 - score 3:**

To success- fully and efﬁciently develop high-quality ABR strategies, we are driven to explore new data efﬁciency [30] approaches and innovative RL techniques. In summary, the main contributions of this paper are the fol- lowing. 1) We analyze the issues present in the current heterogeneous networkandproposeFortuna,amorepracticalofﬂinemeta RL-based ABR method. Fig. 1. The principle of HTTP-based dynamic adaptive video streaming. 2) A novel RL technique uses curriculum learning to handle unbounded video streaming sessions. 3) To better learn the underlying network behavior features, considering that ABR algorithms interact with underly- ing TCP congestion control, learning these features can further reduce rebuffering and optimize QoE.

**Fragmento 19 - p. 2 - score 3:**

Next, in the High Fluctuation Phase (10,000- 20,000 seconds), the range of bandwidth ﬂuctuation broadens, often reaching up to 200 Mbps and occasionally exceeding 300 Mbps. Then comes the Peak Phase (around 20,000-22,000 seconds), where bandwidth surges to its highest levels, exceed- ing 400 Mbps within a short period. Finally, in the Decline and Stabilization Phase (22,000-28,000 seconds), bandwidth grad- ually decreases and stabilizes, with most values falling below 100 Mbps. These data usually contain samples from various scenarios, environments, or states, which can effectively reﬂect the diversity of data distributions. By training on diverse data, Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 20 - p. 3 - score 3:**

III. DEFINE OFFLINE META ABR ALGORITHM Ofﬂine-RL is conducting online learning of the optimal policy π∗from prior data D (i.e., off-policy data, expert demos, prior runs of RL). At time t, the agent observes the current state st (i.e., throughtput Ct, the buffer size Bt, chunk bitrate Rn), and selects an action at (i.e., chunk bitrate Rn) according to its policy. The video client then receives the action at and transitions to a new state st+1, providing the agent with a reward rt. The goal of the ABR agent is to learn a policy that maximizes the expected cumulative discounted reward value E[∞ t=0 γtrt]. The entire process follows a Markov decision process (MDP), denoted by M = (S, A, O, P, R),whereS isthestatespace,Aistheaction space, O is the observation space, P is the transition probability function, and R is the reward function.

**Fragmento 21 - p. 4 - score 3:**

Therefore, we demand that the algorithm be capable of reusing any non-policy data (e.g., off-policy data, expert demos, prior runs of RL) during online RL to achieve highly data-efﬁcient ﬁne-tuning. In the early stages, we needed to learn from expert- demonstrated data D. The state-of-the-art method, MPC [5], de- termines video bitrate by solving an optimization problem aimed at maximizing QoE based on the dynamic playback buffer, con- sidering several future video chunks. By directly optimizing the video QoE objective, MPC typically performs better than tradi- tional methods that rely on ﬁxed heuristics. Therefore, we use the MPC algorithm to collect expert demonstration data in order to reduce the need for online interaction between RL and the video streaming environment.

**Fragmento 22 - p. 7 - score 3:**

The HSDPA dataset : the granularity of user generation in subways, trams, trains, buses and ferries is 1 s, the number of traces is 86, and the throughput range is 0-3Mbit/s. Belgium/4G dataset: generated in static, pedestrian, car, bus, and train movement modes etc., granularity of 1 s, 5 hours in total, 40 traces, throughput range of 0-111Mbit/s. We used the Puffer dataset [13], which in 2020 had over 63,508 video users and streamed a total of 38.6 years of video content in that year. Now, in 2024, the number of video users and streams has grown even further. Network bandwidth ranges from 0 to 500 Mbps, with an interval of 1 s. These networks display variable characteristics with heavy-tailed distributions.


### 8.3. accion decision abr

Palabras clave usadas: `action, bitrate, quality level, representation, decision, select, selection, guidance, recommendation, adaptation, cap, mask, quality, download, chunk, rate`

**Fragmento 1 - p. 3 - score 6:**

III. DEFINE OFFLINE META ABR ALGORITHM Ofﬂine-RL is conducting online learning of the optimal policy π∗from prior data D (i.e., off-policy data, expert demos, prior runs of RL). At time t, the agent observes the current state st (i.e., throughtput Ct, the buffer size Bt, chunk bitrate Rn), and selects an action at (i.e., chunk bitrate Rn) according to its policy. The video client then receives the action at and transitions to a new state st+1, providing the agent with a reward rt. The goal of the ABR agent is to learn a policy that maximizes the expected cumulative discounted reward value E[∞ t=0 γtrt]. The entire process follows a Markov decision process (MDP), denoted by M = (S, A, O, P, R),whereS isthestatespace,Aistheaction space, O is the observation space, P is the transition probability function, and R is the reward function.

**Fragmento 2 - p. 5 - score 6:**

Fortuna uses the RL Actor-Critic (policy and value network) approach in Fig. 3. The training process is as follows: Step 1: Input is the state st, which includes 7 variables, namely: throughtput Ct, chunk download time dk(Rk)/Ck, next chunk sizes Rn+1, RTT, and the buffer size Bt, remaining chunks N and chunk bitrate Rn. Neural networks: The number of hidden layers is 1, and 128 convolution kernels and a fully connected network are used for feature extraction. The size of the convolution kernel is 4 and the step size is 1. Step 2: When receiving the state st, the agent selects the cor- responding action at based on the meta-policy πθ, and the prob- ability distribution is deﬁned as : (st, at) →[0, 1], (st, at) is the probability that the action at may take in state st.

**Fragmento 3 - p. 8 - score 6:**

Advantages: Reﬂects realistic user perception and balances quality with smoothness. Limitations: Requires careful selection of Rmin; more complex than linear QoE. Application: Ideal for adaptive bitrate streaming in constrained bandwidth conditions. 3) High-Deﬁnition QoE: Uses predeﬁned quality levels corresponding to bitrate ranges. Advantages: Simple computations by mapping bitrates to ﬁxed quality lev- els. Limitations: Quality changes are discontinuous and threshold-dependent. Application: Suitable for video ap- plications with standard resolution transitions, such as Standard Deﬁnition (SD), High Deﬁnition (HD), or Ultra- High Deﬁnition (UHD). The experimental results are shown in Fig.

**Fragmento 4 - p. 13 - score 6:**

ACKNOWLEDGMENT The authors thank Prof. Li Zeping and Dr. Huang Tianchi for their guidance regarding video streaming in practice, and the anonymous IEEE TON, TMM reviewers for their valuable feedback. REFERENCES [1] T. Barnett, S. Jain, U. Andra, and T. Khurana, “Cisco visual networking index (VNI) complete forecast update,” 2017–2022,” Americas/EMEAR Cisco Knowledge Network (CKN) Presentation, pp. 1–30, 2021. [2] Y. Sun et al., “CS2P: Improving video bitrate selection and adaptation with data-driven throughput prediction,” in Proc. ACM SIGCOMM Conf., 2016, pp. 272–285. [3] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal bitrate adaptation for online videos,” IEEE/ACM Trans.

**Fragmento 5 - p. 3 - score 5:**

Reward rt: The environment evaluates different actions at, re- ﬂects the quality of at, and improves the policy πθ. rt reﬂects the quality of different bitrates, rebuffering time and video switch- ing frequency. We adopt the QoE metric provided by MPC [5] QoEN = N  n=1 q (Rn) −μ1 N−1 n=1 |q (Rn+1) −q (Rn)| −μ2 N  n=1 Tn (1) A video consists of N chunks, q(.) represents video quality, such as SSIM [35] or VMAF [36], where μ1 and μ2 are the non-negative weight coefﬁcients corresponding to video quality switching frequency and rebuffering time. Meta-ABR Task: In meta-RL, tasks M are drawn from a dis- tribution p(M), representing the diversity of network condi- tions [15].

**Fragmento 6 - p. 4 - score 5:**

Therefore, we demand that the algorithm be capable of reusing any non-policy data (e.g., off-policy data, expert demos, prior runs of RL) during online RL to achieve highly data-efﬁcient ﬁne-tuning. In the early stages, we needed to learn from expert- demonstrated data D. The state-of-the-art method, MPC [5], de- termines video bitrate by solving an optimization problem aimed at maximizing QoE based on the dynamic playback buffer, con- sidering several future video chunks. By directly optimizing the video QoE objective, MPC typically performs better than tradi- tional methods that rely on ﬁxed heuristics. Therefore, we use the MPC algorithm to collect expert demonstration data in order to reduce the need for online interaction between RL and the video streaming environment.

**Fragmento 7 - p. 5 - score 5:**

Output masking is employed as part of the solution. For each video, a mask, represented as a binary vector [m1, m2, . . ., mk], is used to constrain the probability distribution of the output, including only the bitrate levels that the video supports. This mask, in conjunction with softmax [43], determines which bi- trates [i1, i2, . . ., ik] in the NN output are valid. Inner-Loop: The inner loop refers to real-time bitrate selec- tion adjustments based on the current network conditions and the existing strategy, aiming to optimize the short-term user ex- perience. For ABR algorithms, the inner loop uses bandwidth predictions, buffer status, and chunk sizes to select an appropri- ate bitrate that maximizes QoE objectives.

**Fragmento 8 - p. 6 - score 5:**

8190 IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 policy is consistent with both the value and action-value func- tions. This helps improve the policy’s ability to adapt video bi- trate to varying network conditions, such as bandwidth ﬂuctua- tions, to select the optimal bitrate. Outer-Loop: The outer loop focuses on globally optimizing the initial strategy across multiple different network environ- ments (tasks) M, aiming to enhance the generalization ability of the strategy for unseen network ﬂuctuations. For the outer loop update, we sample a distinct batch of data, meta-test Dts i , to promote few-shot generalization instead of memorizing the adaptation data.

**Fragmento 9 - p. 9 - score 5:**

Videos were segmented into a random number of chunks, between 20 and 100, and chunk sizes were varied by applying Gaussian noise to a standard 4-second chunk duration. This ap- proach ensured a broad range of video properties, including bi- trate options, chunk count, chunk sizes, and overall duration, to rigorously test the model’s adaptability and performance across different scenarios. As shown in Fig. 10, the results demonstrated that the gen- eralized ABR algorithm achieved nearly identical performance compared to a model exclusively trained on a reference video, The gap in QoE values is 2.8%. This ﬁnding suggests that our method’s server conﬁguration could effectively elevate stream- ing quality across a spectrum of videos, employing a concise selection of ABR algorithms.

**Fragmento 10 - p. 1 - score 4:**

IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 8185 Optimizing Adaptive Video Streaming: Ofﬂine Reinforcement Learning and Meta-Learning in Diverse Networks Ling Yi , Yongbin Qin , and Ruizhang Huang Abstract—Recent years have seen the optimization of quality of experience (QoE) through learning adaptive bitrate (ABR) algorithms from internet video streams. However, the complex nature of the real-world Internet, characterized by heavy-tailed behavior, diversity, and unpredictability, hinder the effective learning of off-the-shelf reinforcement learning (RL)-based ABR algorithms. As a result, existing methods inevitably fail to achieve optimal performance under various network conditions and user QoE objectives.

**Fragmento 11 - p. 1 - score 4:**

Digital Object Identiﬁer 10.1109/TMM.2025.3604930 quality level, enabling users to select the most suitable video chunk according to available bandwidth. However, due to net- work bandwidth limitations, ABR algorithms may not always request high-quality videos consistently. The main existing ABR algorithms use simple control rules or reinforcement learning (RL) based methods. For example, RB algorithm [2] is only based on network bandwidth or buffer us- age e.g., BOLA algorithm [3], [4], or a combination of the two schemes (e.g., robustMPC [5], Oboe [6], Bayesian-MPC [7]). These methods require careful adjustment and are unable to adapt to different network bandwidths or different QoE ob- jectives.

**Fragmento 12 - p. 1 - score 4:**

Experimental results from trace-driven and real-world scenarios demonstrate that Fortuna enhances learning efﬁciency by more than 7.5%–4 ×, reduces stall time by 4.6%–14.2%, and generalizes to different network conditions and video streams. Index Terms—Adaptive bitrate algorithm, ofﬂine meta reinforcement learning, quality of experience. I. INTRODUCTION V IDEO streaming is the primary internet application, ac- countingfornearly75%ofalltrafﬁc[1].Inadaptivebitrate (ABR) video streaming, videos are typically divided into various small video chunks or segments. Video users can request spe- ciﬁc video chunks based on their preferences and network con- ditions.

**Fragmento 13 - p. 2 - score 4:**

4) We evaluate QoE metrics in trace-driven and real-world environments, and generalize to 3G, 4G, 5G, WiFi, syn- theticnetworks,anddifferentvideostreams(SectionV-C), and deploy the algorithms in streaming media systems (Section VI). II. BACKGROUND AND MOTIVATION The HTTP-based ABR algorithm dynamically selects the ap- propriate bitrate for video segments by monitoring network bandwidth and player buffer status in real-time. It delivers high-quality video when network conditions are good and low- ers the quality during poorer conditions to prevent buffering, thus optimizing the user QoE in Fig. 1. However, due to lim- ited network bandwidth, ABR algorithms may not always re- quest the optimal bitrate.

**Fragmento 14 - p. 2 - score 4:**

8186 IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 strategy [20], enabling RL models to perform better across a wider range of network environments. However, this method fails to effectively learn from large volumes of ofﬂine data as well as adapt to the complexity of video streams. Zuo et al. [21] introduce Ruyi, an off-policy RL-based video streaming system that integrates preference awareness into the QoE model and the ABR algorithm [22], [23]. It is optimized with a modiﬁed Deep Q-learning algorithm using experience replay [24]. Each scheme can be used in a speciﬁc environment, but cannot effec- tively learn and be generalized to diverse network environments or bitrate decisions.

**Fragmento 15 - p. 5 - score 4:**

This dual-head design helps reduce variance in the learn- ing process, leading to more stable and efﬁcient training. Policy adaptation proceeds as: θ′ ←θ−α1∇θLπ(θ; φ′, Dtr i ), where Lπ =LAW R+λLADV (4) where λ is the weight of the normalization Z(s) of the advantage function, designed to better adapt to different network condi- tions. The AWR loss is given in (2), and the advantage regression loss LADV is given by: LADV (θ; φ′, D) = Es,a∼D  Aθ(s, a) −QD(s, a) + Vφ′ i(s) 2 (5) This loss function aims to optimize the advantage function Aθ(s, a), ensuring that the policy selects bitrates that lead to higher expected rewards. By minimizing the difference between Aθ(s, a), QD(s, a), and Vφ′ i(s), the algorithm ensures that the Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 16 - p. 5 - score 4:**

Step 3: After taking each action at, the environment feeds back the reward rt corresponding to at to the agent, and the goal is to obtain the maximum cumulative reward from the environ- ment. Therefore, the reward rt is set according to the parameters of the QoE metric, reﬂecting the individual components of the QoE metric. Step 4: The actor’s output bitrate poses challenges, primarily because different videos can be encoded at various bitrate levels, and due to variable bitrate encoding, their chunk sizes may also differ. To address this diversity, the typical approach would in- volve training a model for every possible combination of video bitrates, which is not a scalable solution.

**Fragmento 17 - p. 7 - score 4:**

Since the playback buffer is relatively stable, it can effectively improve QoE. Pensieve [8]: ABR algorithm based on deep reinforcement learning (DRL), generating ABR algorithm by training neural network. However, the original Pensieve struggled with conver- gence due to the variability in network conditions when using the A3C algorithm. Therefore, we employed variance reduction techniques [52] in the training process to develop a more effec- tive ABR algorithm. RMPC: makes decisions about video bitrate by tackling a problem that aims to maximize QoE for several upcoming chunks. By focusing directly on improving QoE, MPC often performs better than methods that rely on ﬁxed rules [5].

**Fragmento 18 - p. 12 - score 4:**

This ap- proach provides a spectrum of quality and bitrate choices for the video stream, catering to diverse network conditions and devices. As shown in Fig. 14, we found that the simple Buffer-Based ABR (BBA) algorithm [62] can achieve better performance, while the ABR algorithm generated purely through RL train- ing, known as Pensieve, performs poorly. Meanwhile, we have observed that meta-RL does not consistently achieve optimal performance due to the need for adaptation across a wide range of video stream conditions. In real-world scenarios with vary- ing user preferences, BBA, which relies on fewer assumptions and requests videos based on buffer occupancy, closely approx- imates the actual video playback process.

**Fragmento 19 - p. 13 - score 4:**

Moreover, Fortuna can handle unconstrained video stream sessions. In all considered internet video streaming sce- narios, Fortuna rivals or outperforms the state-of-the-art ex- isting approaches, with an average QoE improvement ranging from 1.2%-31.9%. Additionally, experimental results demon- strate that Fortuna exhibits better generalization capabilities in unseen network conditions and QoE user preferences. In practice, we believe that Fortuna can offer valuable insights not only for bitrate adaptation of video streaming but also for TCP congestion control, as it eliminates the costly expense of online learning while enabling swift adaptation to new network conditions.

**Fragmento 20 - p. 14 - score 4:**

Int. Conf. Mach. Learn., 2019, pp. 5331–5340. [59] “Meta RL,” (n.d.). [Online]. Available: https://github.com/katerakelly/ oyster [60] A. Bentaleb, M. Lim, M. N. Akcay, A. C. Begen, and R. Zimmer- mann, “Bitrate adaptation and guidance with meta reinforcement learn- ing,” IEEE Trans. Mobile Comput., vol. 23, no. 11, pp. 10378–10392, Nov. 2024. [61] M. Allman, V. Paxson, and E. Blanton, “RFC 5681: TCP congestion con- trol,” 2009. [62] T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Wat- son, “A buffer-based approach to rate adaptation: Evidence from a large video streaming service,” in Proc. ACM Conf. SIGCOMM, 2014, pp. 187–198. Ling Yi received the masters degree in computer science in 2022 from Guizhou University, Guiyang, China,whereheiscurrentlyworkingtowardthePh.D.

**Fragmento 21 - p. 1 - score 3:**

Each video chunk is assigned a particular bitrate and Received 18 November 2024; revised 22 January 2025; accepted 15 Febru- ary 2025. Date of publication 10 September 2025; date of current version 12 November 2025. This work was supported in part by the National Natural Sci- ence Foundation of China under Grant 62066008, in part by the Key Projects of Science and Technology of Guizhou Province under Grant [2020]1Z055, and in partbytheNationalKeyR&DProgramofChinaunderGrant2023YFC3304500. The associate editor coordinating the review of this article and approving it for publication was Prof. Qiang Wu. (Corresponding author: Yongbin Qin.) The authors are with the Text Computing & Cognitive Intelligence Engi- neering Research Center of National Education Ministry, College of Computer Science and Technology, Guizhou University, Guiyang 550025, China, and also with the State Key Laboratory of Public Big Data, College of Computer Science and Technology, Guizhou University, Guiyang 550025, China (e-mail: yiling- phd@gmail.com; ybqin@gzu.edu.cn; cse.rzhuang@gzu.edu.cn).

**Fragmento 22 - p. 1 - score 3:**

State-of-the-art MPC algorithm [5] uses future video chunks by dynamically optimizing QoE metrics, which has bet- ter performance than the simple ﬁxed schemes e.g., BOLA, RB. However, MPC relies on accurate network bandwidth pre- dictions, especially on future networks. Due to the variability of network bandwidth, MPC is difﬁcult to predict accurately, but inaccurate predictions may cause future video freezes and low-quality video etc. Additionally, since BOLA and MPC can- not adjust parameters according to speciﬁc network conditions and are too sensitive to parameters, then Oboe [6] is proposed to automatically adjust parameters, which can enhance QoE value in speciﬁc scenarios.


### 8.4. reward qoe objetivo

Palabras clave usadas: `reward, QoE, quality of experience, utility, objective, loss, rebuffer, stall, stalling, smoothness, switching, quality variation, latency, fairness, bitrate smoothness, video quality, tail, risk, severe`

**Fragmento 1 - p. 8 - score 6:**

6, For- tuna leverages ofﬂine meta-learning to pre-train adaptive ABR strategies tailored to various QoE objectives. Un- like traditional ABR algorithms with ﬁxed control laws or Pensieve’s online learning approach, Fortuna’s pre-trained model can rapidly adapt to QoElog, QoElin, and QoEhd scenarios: TABLE I QOE MODELS AND THEIR CORRESPONDING PARAMETERS r For QoElog, Fortuna minimizes rebuffering risk by prior- itizing bitrate stability while avoiding unnecessary high- bitrate jumps. r For QoElin, it aggressively increases bitrate to maxi- mize user-perceived quality without sacriﬁcing playback smoothness. r In QoEhd optimization, Fortuna employs foresight to rapidly build buffer with low bitrates and switches directly to HD quality once buffer conditions are favorable, all without online tuning.

**Fragmento 2 - p. 3 - score 5:**

Reward rt: The environment evaluates different actions at, re- ﬂects the quality of at, and improves the policy πθ. rt reﬂects the quality of different bitrates, rebuffering time and video switch- ing frequency. We adopt the QoE metric provided by MPC [5] QoEN = N  n=1 q (Rn) −μ1 N−1 n=1 |q (Rn+1) −q (Rn)| −μ2 N  n=1 Tn (1) A video consists of N chunks, q(.) represents video quality, such as SSIM [35] or VMAF [36], where μ1 and μ2 are the non-negative weight coefﬁcients corresponding to video quality switching frequency and rebuffering time. Meta-ABR Task: In meta-RL, tasks M are drawn from a dis- tribution p(M), representing the diversity of network condi- tions [15].

**Fragmento 3 - p. 1 - score 4:**

IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 8185 Optimizing Adaptive Video Streaming: Ofﬂine Reinforcement Learning and Meta-Learning in Diverse Networks Ling Yi , Yongbin Qin , and Ruizhang Huang Abstract—Recent years have seen the optimization of quality of experience (QoE) through learning adaptive bitrate (ABR) algorithms from internet video streams. However, the complex nature of the real-world Internet, characterized by heavy-tailed behavior, diversity, and unpredictability, hinder the effective learning of off-the-shelf reinforcement learning (RL)-based ABR algorithms. As a result, existing methods inevitably fail to achieve optimal performance under various network conditions and user QoE objectives.

**Fragmento 4 - p. 2 - score 4:**

This is because online learning of ABR al- gorithms does not explore safely and cannot effectively learn from these complex network features [25], [26]. Speciﬁcally,inreal-worldadaptivevideostreamingscenarios, learning algorithms rely on speciﬁc data or environments to train them. However, Internet data is often vast and massive, and ABR algorithms adapt to new scenarios by learning from these net- work characteristics. Because network conditions continually change over time, and due to different user preferences, ABR algorithms must balance various QoE metrics, such as improv- ing video quality and reducing rebuffering time. Unfortunately, learning algorithms often perform well on the simple training and testing datasets, but real internet data features are complex and variable, exhibiting heavy-tailed characteristics.

**Fragmento 5 - p. 3 - score 3:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8187 Fig. 2. Visualize network features, as well as video quality and buffering time of existing ABR algorithms, on the Puffer dataset. ofﬂine RL enables the model to learn the features and patterns across different distributions, enhancing its generalization abil- ity [31]. Case 2: The QoE of video users is inﬂuenced by the un- derlying TCP congestion control protocol [32], such as RTT. We observe varying network throughputs, ranging from 0 to 250 Mbps, with different RTT values across users. For example, users with a throughput of 75 Mbps exhibit a wide range of RTT values, while those with throughput between 25 and 50 Mbps of- ten experience high latency and a broader range of RTT values.

**Fragmento 6 - p. 3 - score 3:**

We compared several ABR algorithms, including Pensieve, Fugu, Comyco, BOLA, and MPC, in how well they adapt to unseen network conditions. Due to the randomness of network bandwidth, traditional methods like Pensieve struggle to converge effectively. Fugu, which combines neural network training with MPC predictions, also encounters challenges in managing unknown network conditions. Fortuna is the most op- timal among all ABR algorithms in improving video quality (SSIM) and reducing stalling time. Our ﬁndings indicate that existing methods struggle to respond effectively to these unpre- dictable scenarios. In summary, it is highly important to efﬁciently learn robust ABR algorithms under wild Internet conditions and generalize them to diverse network conditions.

**Fragmento 7 - p. 3 - score 3:**

These heterogeneous network characteristics signiﬁcantly im- pact ABR algorithm decisions, affecting QoE outcomes. Since RTT inﬂuences QoE, TCP congestion control algorithms like BBR [33] and CUBIC [34] adjust data sending rates to opti- mize RTT performance. ABR algorithms must adapt to chang- ing network conditions to improve video streaming quality by leveraging these underlying network characteristics. Case 3: Learning ABR strategies often leads to poor deci- sions when faced with unknown network conditions, resulting in suboptimal video quality and increased rebuffering time. We use the Puffer dataset, with a duration of 1000 hours and a time interval of 1 s, where the network bandwidth ranges from 0 to 400 Mbps.

**Fragmento 8 - p. 4 - score 3:**

8188 IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 thereby optimizing the QoE objective across a variety of tasks. Advantage-Weighted Regression (AWR): AWR is an ofﬂine RL method that reﬁnes the policy based on historical data [37]. Its objective function is: LAW R(θ, φ, D) = Es,a∼D  − 1 Z(s) log πθ(a|s) exp (QD(s, a) −Vφ(s))  (2) where: r QD(s, a) is the return from the dataset for action a in state s. r Vφ(s) is the value function for the behavior policy. r Z(s) > 0 is a normalization function dependent on the state s, scaling the overall loss term. The term QD(s, a) −Vφ(s) represents the advantage of an action a. The policy objective LAW R can be seen as a weighted regression problem, where actions with higher advantages re- ceive greater weight.

**Fragmento 9 - p. 7 - score 3:**

During the training process, the size of each epoch is 100, γ = 0.99, Relu activation function [47] and the Adam optimizer [48] are used. During the whole experiment, according to the change of the loss function, the learning rates for the inner and outer loops are 0.001 and 0.0001, respectively, and the reward value fed back to the agent by the environment is the QoE metric value. Network Traces: To evaluate Fortuna and existing ABR al- gorithms on different networks, we use FCC [49], HSDPA [50] and Belgium/4G [51] public network traces, and the dataset fea- tures are as follows. The FCC dataset contains 1 million net- work traces with an average network throughput of 2100 sec- onds each trace, granularity of 5 s, and a throughput range of 0-111Mbit/s, generated on trains, buses, cars etc.

**Fragmento 10 - p. 7 - score 3:**

For example, when network bandwidth is insufﬁcient, Fortuna uses a low bitrate to compensate for the low bandwidth and reduce video stalling. Video user preferences: This section provides a comparison of three common QoE models, highlighting their key character- istics. 1) Linear QoE: Advantages: Simple and intuitive, suitable for scenarios prioritizing higher bitrates. Limitations: Ig- nores diminishing returns of quality perception and is sensitive to bitrate ﬂuctuations. Application: Suitable for high-bandwidth video streaming environments. 2) Logarithmic QoE: QoE models user perception with diminishing returns using q(R) = log(R/Rmin). Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 11 - p. 9 - score 3:**

Wild ﬂuctuations can bring great challenges to the ABR algorithms, howtobalancecomponents of thevideobitrateandthestall time, thereby the ABR decision should be forward-looking enough to maximize QoE objectives and minimize stall time as much as possible. As shown in Fig. 8, Fortuna can achieve better performance on 4G and 5G networks, the stall time is reduced by 4.6%-12.2% and 0.5%-3.1% respectively. As shown, fortuna and ofﬂine- Fortuna can achieve better performance on 4G and 5G networks. However, Fugu [13] (supervised learning) cannot be adapted to different networks, as it requires speciﬁc data that cannot be adapted to new networks, and BOLA fail to achieve good performance using simple ﬁxed heuristics.

**Fragmento 12 - p. 1 - score 2:**

We propose Fortuna, a novel ofﬂine meta RL ABR algorithm that can effectively learn from these heavy-tailed internet data features and become more practical. Fortuna is primarily divided into two phases. In the ofﬂine phase, Fortuna utilizes diverse ofﬂine data for learning to reduce the costly online RL interaction expense, while in the online phase, we gradually increase video streaming sessions complexity through curriculum learning to quickly adapt to speciﬁc network conditions. Fortuna then utilizes meta-learning to optimize ABR policies and enhance generalization. Additionally, to better learn network features, Fortuna further optimizes QoE by learning low- level TCP congestion control information.

**Fragmento 13 - p. 1 - score 2:**

Experimental results from trace-driven and real-world scenarios demonstrate that Fortuna enhances learning efﬁciency by more than 7.5%–4 ×, reduces stall time by 4.6%–14.2%, and generalizes to different network conditions and video streams. Index Terms—Adaptive bitrate algorithm, ofﬂine meta reinforcement learning, quality of experience. I. INTRODUCTION V IDEO streaming is the primary internet application, ac- countingfornearly75%ofalltrafﬁc[1].Inadaptivebitrate (ABR) video streaming, videos are typically divided into various small video chunks or segments. Video users can request spe- ciﬁc video chunks based on their preferences and network con- ditions.

**Fragmento 14 - p. 2 - score 2:**

To success- fully and efﬁciently develop high-quality ABR strategies, we are driven to explore new data efﬁciency [30] approaches and innovative RL techniques. In summary, the main contributions of this paper are the fol- lowing. 1) We analyze the issues present in the current heterogeneous networkandproposeFortuna,amorepracticalofﬂinemeta RL-based ABR method. Fig. 1. The principle of HTTP-based dynamic adaptive video streaming. 2) A novel RL technique uses curriculum learning to handle unbounded video streaming sessions. 3) To better learn the underlying network behavior features, considering that ABR algorithms interact with underly- ing TCP congestion control, learning these features can further reduce rebuffering and optimize QoE.

**Fragmento 15 - p. 4 - score 2:**

Therefore, we demand that the algorithm be capable of reusing any non-policy data (e.g., off-policy data, expert demos, prior runs of RL) during online RL to achieve highly data-efﬁcient ﬁne-tuning. In the early stages, we needed to learn from expert- demonstrated data D. The state-of-the-art method, MPC [5], de- termines video bitrate by solving an optimization problem aimed at maximizing QoE based on the dynamic playback buffer, con- sidering several future video chunks. By directly optimizing the video QoE objective, MPC typically performs better than tradi- tional methods that rely on ﬁxed heuristics. Therefore, we use the MPC algorithm to collect expert demonstration data in order to reduce the need for online interaction between RL and the video streaming environment.

**Fragmento 16 - p. 5 - score 2:**

The value function loss, dependent on the meta-training data Dtr i , representing the i-th batch of ofﬂine data. In the ABR algo- rithm, the value function Vφ(s) estimates the long-term return or value of a state s. In this step, the goal is to update φ by mini- mizing the value function loss LV , which makes Vφ(s) a closer approximation to the action-value function QD(s, a). φ′ ←φ −η1∇φLV (φ; Dtr i ) (3) where LV (φ; D) = Es,a∼D[(Vφ(s) −QD(s, a))2] and QD(s, a) is the Monte Carlo return from state s taking action a observed in D. By minimizing the loss, we aim to accurately predict the expected reward for each bitrate choice in a given state. To effectively learn features from the changing network con- ditions, our policy architecture has two output heads: one for predicting the action given the state, πθ(·|s), and another for predicting the advantage given both state and action, Aθ(s, a) [44].

**Fragmento 17 - p. 5 - score 2:**

This dual-head design helps reduce variance in the learn- ing process, leading to more stable and efﬁcient training. Policy adaptation proceeds as: θ′ ←θ−α1∇θLπ(θ; φ′, Dtr i ), where Lπ =LAW R+λLADV (4) where λ is the weight of the normalization Z(s) of the advantage function, designed to better adapt to different network condi- tions. The AWR loss is given in (2), and the advantage regression loss LADV is given by: LADV (θ; φ′, D) = Es,a∼D  Aθ(s, a) −QD(s, a) + Vφ′ i(s) 2 (5) This loss function aims to optimize the advantage function Aθ(s, a), ensuring that the policy selects bitrates that lead to higher expected rewards. By minimizing the difference between Aθ(s, a), QD(s, a), and Vφ′ i(s), the algorithm ensures that the Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 18 - p. 5 - score 2:**

Output masking is employed as part of the solution. For each video, a mask, represented as a binary vector [m1, m2, . . ., mk], is used to constrain the probability distribution of the output, including only the bitrate levels that the video supports. This mask, in conjunction with softmax [43], determines which bi- trates [i1, i2, . . ., ik] in the NN output are valid. Inner-Loop: The inner loop refers to real-time bitrate selec- tion adjustments based on the current network conditions and the existing strategy, aiming to optimize the short-term user ex- perience. For ABR algorithms, the inner loop uses bandwidth predictions, buffer status, and chunk sizes to select an appropri- ate bitrate that maximizes QoE objectives.

**Fragmento 19 - p. 5 - score 2:**

Step 3: After taking each action at, the environment feeds back the reward rt corresponding to at to the agent, and the goal is to obtain the maximum cumulative reward from the environ- ment. Therefore, the reward rt is set according to the parameters of the QoE metric, reﬂecting the individual components of the QoE metric. Step 4: The actor’s output bitrate poses challenges, primarily because different videos can be encoded at various bitrate levels, and due to variable bitrate encoding, their chunk sizes may also differ. To address this diversity, the typical approach would in- volve training a model for every possible combination of video bitrates, which is not a scalable solution.

**Fragmento 20 - p. 7 - score 2:**

QoE breakdown: To better understand the performance of Fortuna, we compare the individual components of QoE metric. Fig. 5 shows the video bitrate, rebuffering time and smoothing penalty, i.e., the components of QoE metric. Experimental re- sults are evaluated on FCC, Belgium/4G, and HSDPA datasets. As shown, Fortuna is able to better limit rebuffering through different networks to achieve higher QoE values. rebuffering time is reduced by 4.6%-14.2% on FCC, Belgium/4G, and HS- DPA datasets by building enough buffers to handle sudden net- work ﬂuctuations. In addition, although Fortuna cannot outper- form existing solutions in every QoE metric. Instead, it is able to maximize QoE by optimizing every metric.

**Fragmento 21 - p. 8 - score 2:**

Advantages: Reﬂects realistic user perception and balances quality with smoothness. Limitations: Requires careful selection of Rmin; more complex than linear QoE. Application: Ideal for adaptive bitrate streaming in constrained bandwidth conditions. 3) High-Deﬁnition QoE: Uses predeﬁned quality levels corresponding to bitrate ranges. Advantages: Simple computations by mapping bitrates to ﬁxed quality lev- els. Limitations: Quality changes are discontinuous and threshold-dependent. Application: Suitable for video ap- plications with standard resolution transitions, such as Standard Deﬁnition (SD), High Deﬁnition (HD), or Ultra- High Deﬁnition (UHD). The experimental results are shown in Fig.

**Fragmento 22 - p. 9 - score 2:**

Different from the previous bitrate setting (e.g., 2.85 Mbps, 4.3 Mbps that can only support 3G and 4G network). However, 5G networks [53] (i.e., including 4G and 5G, there are 175 4G and 121 5G network traces with a granularity of 1 s, 2 types: driving and walking) can support higher bitrate videos, in order to match the corresponding network throughput with the video bitrate, to prevent high throughput from always meeting high and low bitrates. Inspired by literature [54], experiment bitrate settings, namely: (20, 40, 60, 80, 110, 160) Mbps, bitrate map reward=[1, 2, 3, 12, 15, 20], (more detail in [55]), total video chunks is 157, rebuf-penalty is 160, smooth-penalty is 1.


### 8.5. entrenamiento optimizacion

Palabras clave usadas: `training, train, trained, episode, epoch, optimizer, learning rate, experience replay, fine-tune, fine-tuning, pretrain, pre-training, behavior cloning, imitation, expert, simulation, simulator, offline, online, curriculum, loss function, joint optimization, dataset, sample`

**Fragmento 1 - p. 7 - score 7:**

During the training process, the size of each epoch is 100, γ = 0.99, Relu activation function [47] and the Adam optimizer [48] are used. During the whole experiment, according to the change of the loss function, the learning rates for the inner and outer loops are 0.001 and 0.0001, respectively, and the reward value fed back to the agent by the environment is the QoE metric value. Network Traces: To evaluate Fortuna and existing ABR al- gorithms on different networks, we use FCC [49], HSDPA [50] and Belgium/4G [51] public network traces, and the dataset fea- tures are as follows. The FCC dataset contains 1 million net- work traces with an average network throughput of 2100 sec- onds each trace, granularity of 5 s, and a throughput range of 0-111Mbit/s, generated on trains, buses, cars etc.

**Fragmento 2 - p. 6 - score 5:**

Traditional gradient descent updates result in rank-1 changes, whereas with the latent vector z, the rank of weight updates is bounded by: rank(ΔW ∗) ≤min(d, c), allowing higher-rank transformations and richer adaptation strategies. Algorithm 1: Learning meta-ABR policies through ofﬂine RL with gradually increasing video stream length 1: Require: network environments {Mi}; ofﬂine datasets Di containing trajectories τ: (st, at, rt) 2: Require: Initial video stream length Tinit, increment ΔT, maximum stream length Tmax 3: Hyperparameters: Inner-loop learning rates α1 (policy), η1 (value); outer-loop learning rates α2, η2; training iterations k 4: Initialize meta-policy parameters θ and value function parameters φ 5: for k iterations do 6: for each network environment Mi do 7: Sample disjoint meta-training and meta-test data batches Dtr i and Dts i from Di 8: Calculate video stream length for the current stage: Tk = min(Tinit + ΔT · (k −1), Tmax) 9: Adapt value function: φ′ ←φ −η1∇φLV (φ; Dtr i ) 10: Adapt policy: θ′ ←θ −α1∇θLπ(θ; φ′; Dtr i ), where Lπ = LAW R + λLADV 11: end for 12: Meta-update value function: φ ←φ −η2  i ∇φLV (φ′; Dts i ) 13: Meta-update policy: θ ←θ −α2  i ∇θLAW R(θ′; φ′; Dts i ) 14: end for Algorithm 2: Generalizing meta-ABR policies across di- verse environments 1: Input: Test network environment Mj, ofﬂine experience buffer D, meta-policy πθ, and meta-value function Vφ 2: Hyperparameters: Learning rates α1, η1; number of adaptation steps k 3: Initialize policy parameters θ0 = θ and value function parameters φ0 = φ 4: for k adaptation steps do 5: Adapt value function: φt+1 ←φt −η1∇φLV (φt; D) 6: Adapt policy: θt+1 ←θt −α1∇θLπ(θt; φt+1; D) 7: end for In summary, the latent vector z enhances ABR algorithms by enabling dynamic weight and bias generatio

**Fragmento 3 - p. 9 - score 5:**

9, average QoE value increased by12.5%. The advantage of Fortuna lies in its ability to opti- mize based on a comprehensive set of historical data and com- plex network environments. In contrast, ABR algorithms gener- ated through curriculum learning might face limitations due to constraints in the data and training strategies used during their development. Multiple videos: To evaluate Fortuna’s ability to gener- alize across varying video properties, we trained a sin- gle ABR model using 1,000 synthetic videos with diverse characteristics. Each video had a random number of bi- trate options, ranging from 3 to 10, with values chosen from {200, 300, 450, 750, 1200, 1850, 2350, 2850, 3500, 4300} kbps.

**Fragmento 4 - p. 11 - score 5:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8195 Fig. 11. Comparison of training epochs and training time with and without curriculum learning by increasing the complexity of video streaming, i.e., from short video streams to long video streams. Fig. 12. The comparison of Fortuna with the existing state-of-the-art meta- ABR algorithm, Meta-PPO ABR [60]. video streams to more complex, longer video streams, en- abling it to better cope with ﬂuctuating network environ- ments and ensuring high-quality video streams under varying conditions. E. Deep Dive In this section, we explore microbenchmarks tailored to deepen our comprehension of Fortuna.

**Fragmento 5 - p. 2 - score 4:**

This is because online learning of ABR al- gorithms does not explore safely and cannot effectively learn from these complex network features [25], [26]. Speciﬁcally,inreal-worldadaptivevideostreamingscenarios, learning algorithms rely on speciﬁc data or environments to train them. However, Internet data is often vast and massive, and ABR algorithms adapt to new scenarios by learning from these net- work characteristics. Because network conditions continually change over time, and due to different user preferences, ABR algorithms must balance various QoE metrics, such as improv- ing video quality and reducing rebuffering time. Unfortunately, learning algorithms often perform well on the simple training and testing datasets, but real internet data features are complex and variable, exhibiting heavy-tailed characteristics.

**Fragmento 6 - p. 5 - score 4:**

As its ABR strategy improves, we extend the episode length, making the problem more challenging. The concept of gradually increas- ing video stream sequence length—and, consequently, prob- lem complexity—during training realizes curriculum learning for ABR [29]. C. Learning meta-ABR Algorithm Fortuna is an ofﬂine meta-RL ABR algorithm that learns ini- tializations φ and θ for a value function Vφ and meta policy πθ, respectively, enabling rapid adaptation to a new network condi- tion encountered at meta-test time via gradient descent. Fortuna mainly consists of inner loops and outer loops [15], [42]. Next, we will provide a detailed overview of the implementation pro- cess.

**Fragmento 7 - p. 9 - score 4:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8193 Fig. 7. The overall probability distribution of 4G and 5G network traces. By eliminating online exploration and relying on pre-trained policies, Fortuna consistently delivers high performance across changing conditions, surpassing the adaptability and efﬁciency of Pensieve. C. Generalization In Section V-B, Fortuna is tested using common network traces, which have relatively short durations. In practice, how- ever, Fortuna may encounter new network bandwidths, bitrates and require different optimal ABR strategies. To evaluate the generalization ability of Fortuna to the new network, we con- duct 2 sets of experiments.

**Fragmento 8 - p. 10 - score 4:**

Ten- sorFlow TensorBoard was used to monitor the training process during the experimental procedures. As shown in Fig. 11(a), the original Pensieve was trained using A3C, due to the random na- ture of network conditions, and the ﬂuctuations were very dras- tic, thus we used Variance reduction to optimize training the per- formance more stable. PEARL, a context-driven meta-learning approach, tends to meta-overﬁtting, which leads to suboptimal performance in unseen network conditions. Contrastingly, For- tuna leverages ofﬂine data to rapidly learn meta-ABR policies, resulting in an improvement of over 6.6%–20.1% the previous performance. Additionally, we also compared Fortuna with online meta-RL methods, using PPO to optimize the ABR algorithm, as shown in Fig.

**Fragmento 9 - p. 14 - score 4:**

R. Sheikh, and E. P. Simoncelli, “Image quality assessment: From error visibility to structural similarity,” IEEE Trans. Image Process., vol. 13, no. 4, pp. 600–612, Apr. 2004. [36] V.Netﬂix,“Videomulti-methodassessmentfusion,”2019.[Online].Avail- able: https://github.com/Netﬂix/vmaf [37] A. Nair, A. Gupta, M. Dalal, and S. Levine, “Awac: Accelerating on- line reinforcement learning with ofﬂine datasets,” in Proc. ICLR, 2021, pp. 1–17. [38] Z. Huo et al., “Faster on-device training using new federated momentum algorithm,” 2020, arXiv:2002.02090. [39] X. Jiang et al., “MNN: A universal and efﬁcient inference engine,” in Proc. Mach. Learn. Syst., 2020, vol. 2, pp. 1–13.

**Fragmento 10 - p. 1 - score 3:**

Recently, Pensieve [8] was proposed to further improve QoE by using RL to train a neural network to generate ABR algo- rithms, which effectively solves the limitations of existing ABR algorithms. Alternatively, PPO-based policy optimization can be utilized to learn more efﬁcient ABR strategies [9], [10]. How- ever, due to the randomness of network bandwidth, RL-based methods are difﬁcult to converge quickly or generate a large amount of gradient variance [52]. Imitation learning [11], [12] is used for solving MPC problems, but the method is only appli- cable to known environments and cannot be used for complex network scenarios. Fugu [13] combines classical control with a learned network predictor, trained with supervised learning in situ on data from the real deployment environment.

**Fragmento 11 - p. 1 - score 3:**

Addi- tionally, ABRL [14] converts ABR policy into a linear model for better comprehension and safety, allowing human engineers to verify it while slightly increasing the average stall rate by 0.8%. Another approach is to employ meta-RL techniques like MAML [15], [16], [17] or Pearl [18] to adaptive to various network conditions. Moreover, Genet [19] introduces increas- ingly challenging environments through a curriculum learning 1520-9210 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission.

**Fragmento 12 - p. 2 - score 3:**

Fortuna is primarily divided into two stages. In the ofﬂine phase, it leverages domain knowledge to ﬁrst learn from expert data, and then collects runs of RL data. In the online phase, optimization takes place, gradually increasing the complexity of the video stream through curriculum learn- ing [20], [29]. However, ofﬂine ABR strategies cannot adapt to new network conditions. To enhance the generalization of Fortuna, we employ meta-learning for continuous optimization. Furthermore, ABR algorithms interact with TCP congestion control mechanisms, such as congestion window (CWND) and round-trip time (RTT). To better understand the underlying net- work behavior features, we consider TCP congestion control to facilitate the effective learning of ABR algorithms.

**Fragmento 13 - p. 2 - score 3:**

Next, in the High Fluctuation Phase (10,000- 20,000 seconds), the range of bandwidth ﬂuctuation broadens, often reaching up to 200 Mbps and occasionally exceeding 300 Mbps. Then comes the Peak Phase (around 20,000-22,000 seconds), where bandwidth surges to its highest levels, exceed- ing 400 Mbps within a short period. Finally, in the Decline and Stabilization Phase (22,000-28,000 seconds), bandwidth grad- ually decreases and stabilizes, with most values falling below 100 Mbps. These data usually contain samples from various scenarios, environments, or states, which can effectively reﬂect the diversity of data distributions. By training on diverse data, Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 14 - p. 3 - score 3:**

III. DEFINE OFFLINE META ABR ALGORITHM Ofﬂine-RL is conducting online learning of the optimal policy π∗from prior data D (i.e., off-policy data, expert demos, prior runs of RL). At time t, the agent observes the current state st (i.e., throughtput Ct, the buffer size Bt, chunk bitrate Rn), and selects an action at (i.e., chunk bitrate Rn) according to its policy. The video client then receives the action at and transitions to a new state st+1, providing the agent with a reward rt. The goal of the ABR agent is to learn a policy that maximizes the expected cumulative discounted reward value E[∞ t=0 γtrt]. The entire process follows a Markov decision process (MDP), denoted by M = (S, A, O, P, R),whereS isthestatespace,Aistheaction space, O is the observation space, P is the transition probability function, and R is the reward function.

**Fragmento 15 - p. 4 - score 3:**

IV. DESIGN In this section, based on ofﬂine RL theory, we describe how to efﬁciently learn a robust ABR algorithm. We then utilize meta- learningtolearnmeta-ABRpoliciestoadapttodifferentnetwork conditions. A. Addressing Data Efﬁciency Issues in RL. Academia and industry are actively researching neural net- work efﬁciency [31], [38], [39]. In traditional deep RL with real-time online interactions like Pensieve, it often takes around 50,000 iterations and 4 hours to converge [8]. However, when ap- plying this to real-world environments, like learning in situ [13], convergence could take up to 2 years. This highlights the prac- tical challenges of neural network training, particularly for real- world applications.

**Fragmento 16 - p. 4 - score 3:**

B. Handling Unbounded Video Streaming Sessions With Curriculum Learning We will construct a strategy for gradually increasing video stream length from a mathematical perspective and combine it with the decaying process of environmental resets, observing how these two factors work together to optimize the training process. Let the video stream length be denoted as Tk, where k rep- resents the training stage. Starting from the initial stage k = 1, the video stream length gradually increases as the training pro- gresses. We can describe the gradual increase of video stream length using the following mathematical formula: Tk = min (Tinit + ΔT · (k −1), Tmax) Where: r Tinit is the initial video stream length.

**Fragmento 17 - p. 4 - score 3:**

Con- sequently, during early training episodes, the agent struggles to process video stream as they arrive, resulting in a signiﬁ- cant video stream queue buildup. Additionally, when the agent’s strategy is not optimal, video requests may experience delays, resulting in a queue before being serviced rather than receiving immediate satisfaction. In order to avoid spending a signiﬁcant amount of train- ing time exploring actions that do not improve the policy in this scenario, we prematurely terminate the initial episodes so Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 18 - p. 4 - score 3:**

In practice, RL-based ABR algorithms need to quickly learn the optimal policy π∗and generalize across various types of net- work conditions, i.e., learn the optimal policy π∗from prior data D = (si, ai, si+1, ri). One of the simplest methods for applying RL is to use prior data D, such as pre-trained policies from imita- tion learning (e.g., Comyco [11]), and then reﬁne them through RL [40], [41]. However, this approach has two limitations: (1) the prior data may not be optimal, and (2) ﬁne-tuning the policy lacks data efﬁciency as it cannot make efﬁcient use of prior data during RL [37]. In real-world environment, data efﬁ- ciency is of paramount importance.

**Fragmento 19 - p. 4 - score 3:**

When training reaches the maximum length (the 9th stage), the video stream length will be 50 seconds. To learn a robust ABR strategy effectively, the agent needs to undergo training in “streaming” scenarios where the video streaming session continuously arrive over time. Training in “batch” scenarios, where video streaming sessions arrive simul- taneously at the beginning of an episode, leads to inefﬁcient strategies in a “streaming” environment, such as different ran- dom seeds. However, training with a continuous ﬂow of video stream arrivals presents challenges. The agent’s initial strategy is poor, mainly because the initial parameters are random.

**Fragmento 20 - p. 5 - score 3:**

This dual-head design helps reduce variance in the learn- ing process, leading to more stable and efﬁcient training. Policy adaptation proceeds as: θ′ ←θ−α1∇θLπ(θ; φ′, Dtr i ), where Lπ =LAW R+λLADV (4) where λ is the weight of the normalization Z(s) of the advantage function, designed to better adapt to different network condi- tions. The AWR loss is given in (2), and the advantage regression loss LADV is given by: LADV (θ; φ′, D) = Es,a∼D  Aθ(s, a) −QD(s, a) + Vφ′ i(s) 2 (5) This loss function aims to optimize the advantage function Aθ(s, a), ensuring that the policy selects bitrates that lead to higher expected rewards. By minimizing the difference between Aθ(s, a), QD(s, a), and Vφ′ i(s), the algorithm ensures that the Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 21 - p. 5 - score 3:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8189 Fig. 3. The policy architecture of Fortuna is used to generate the ABR algo- rithm, solid lines show the data ﬂow during the forward pass, while dashed lines represent the gradient ﬂow during the backward pass, which occurs only during the adaptation phase. The advantage head is not involved in the policy update process of the outer loop. that the agent can reset and quickly retry from an idle state. We gradually increase the length of video streaming sessions throughout the entire training process. Thus, initially, the agent learns to short video streaming sessions sequences.

**Fragmento 22 - p. 7 - score 3:**

For this study, we selected 4 different datasets. We used 80% of the data for training and 20% as test data. B. Evaluation Network datasets: FCC, HSDPA, and Belgium/4G; video: di- vided into 48 video chunks, each chunk has approximately 4 seconds, the total duration is 193 seconds; H.264/MPEG-4 en- coding: {300, 750, 1200, 1850, 2850, 4300} kbps; video player: Google Chrome (built-in DASH.js), playback buffer capacity is set to 60 seconds, all ABR algorithms run in dash.js; video server: Apache2, video is deployed on the server. ABR algorithms: We compare Fortuna with state-of-art ABR algorithms. BOLA [3]: optimizing buffer occupancy using Lyapunov al- gorithm.


### 8.6. datos trazas datasets

Palabras clave usadas: `dataset, trace, traces, network trace, bandwidth trace, FCC, HSDPA, Norway, LTE, 4G, WiFi, Puffer, Starlink, cellular, synthetic, simulation, testbed, Mahimahi, live streaming, real-world, stream-years, users, sessions, heavy-tailed, CMCD, CMSD`

**Fragmento 1 - p. 7 - score 8:**

The HSDPA dataset : the granularity of user generation in subways, trams, trains, buses and ferries is 1 s, the number of traces is 86, and the throughput range is 0-3Mbit/s. Belgium/4G dataset: generated in static, pedestrian, car, bus, and train movement modes etc., granularity of 1 s, 5 hours in total, 40 traces, throughput range of 0-111Mbit/s. We used the Puffer dataset [13], which in 2020 had over 63,508 video users and streamed a total of 38.6 years of video content in that year. Now, in 2024, the number of video users and streams has grown even further. Network bandwidth ranges from 0 to 500 Mbps, with an interval of 1 s. These networks display variable characteristics with heavy-tailed distributions.

**Fragmento 2 - p. 7 - score 7:**

During the training process, the size of each epoch is 100, γ = 0.99, Relu activation function [47] and the Adam optimizer [48] are used. During the whole experiment, according to the change of the loss function, the learning rates for the inner and outer loops are 0.001 and 0.0001, respectively, and the reward value fed back to the agent by the environment is the QoE metric value. Network Traces: To evaluate Fortuna and existing ABR al- gorithms on different networks, we use FCC [49], HSDPA [50] and Belgium/4G [51] public network traces, and the dataset fea- tures are as follows. The FCC dataset contains 1 million net- work traces with an average network throughput of 2100 sec- onds each trace, granularity of 5 s, and a throughput range of 0-111Mbit/s, generated on trains, buses, cars etc.

**Fragmento 3 - p. 14 - score 7:**

IEEE/ACM 26th Int. Symp. Qual. Service, 2018, pp. 1–2. [49] “FCC broadband dataset,” (n.d.). [Online].Available: http://data.fcc. gov/download/measuring-broadband-America/2016/data-raw-2016- jun.tar.gz [50] “Norway HSDPA bandwidth logs,” (n.d.). [Online]. Available: http:// home.iﬁ.uio.no/paalh/dataset/hsdpa-tcp-logs/ [51] “Belgium 4G/LTE bandwidth logs (bonus),” (n.d.). [Online]. Available: http://users.ugent.be/jvdrhoof/dataset-4g/logs/logs_all.zip [52] H. Mao, S. B. Venkatakrishnan, M. Schwarzkopf, and M. Alizadeh, “Vari- ance reduction for reinforcement learning in input-driven environments,” ICLR, 2019, pp. 1–20. [53] A. Narayanan et al., “Lumos5g: Mapping and predicting commercial mmWave 5G throughput,” in Proc.

**Fragmento 4 - p. 9 - score 5:**

First, Fortuna is evaluated on the real 5G network traces, and analyse the differences with 4G network. Second, we take the generalisation of Fortuna to the extreme, i.e. training purely with synthetic networks and generalising to real Belgium/4G and comparing with Genet [19]. 5G and 4G network traces: To analyze the distribution of 5G network versus 4G network, we performed network traces analysis using the CDF distribution map. As shown in Fig. 7, 5G network is able to support higher network bandwidth in the range of 0-1800 Mbps, and 4G is 0-300 Mbps. Second, 5G network are capable of supporting high network, which means we need corresponding bitrates to match.

**Fragmento 5 - p. 9 - score 5:**

Furthermore, RMPC algorithm performs poorly on 5G networks due to overly con- servative predictions. However, in these heterogeneous network data, the environment is more complex and requires better ABR decisions. In contrast, RL can adaptively select the optimal bi- trates based on the network scenario. These experiments show that Fortuna can reduce stall time and maximize QoE even in the case of high and ﬂuctuating network traces, despite these networks have never encountered. Training with synthetic dataset: The training dataset has a signiﬁcant impact on the performance of RL-based algorithms and may hinder the optimal ABR strategy for RL learning.

**Fragmento 6 - p. 2 - score 4:**

Considering the diversity of the Puffer dataset [13], we visualize it in Fig. 2, comprising 10427 streams, 1258 stream-hours, and analyze the data characteristics of these real network users to illustrate why off-the-shelf ABR algo- rithms have difﬁculty in adapting to these conditions. Case 1: Network conditions ﬂuctuate over time, and long- duration video streams exhibit a heavy-tailed distribution. Ini- tial Low Load Phase (0 - 5,000 seconds), where bandwidth ﬂuc- tuates at relatively low levels, mostly below 100 Mbps, with frequent dips close to zero. This is followed by the Increased Fluctuation Phase (5,000-10,000 seconds), during which band- width varies between 0 and 200 Mbps, showing more frequent peaks and troughs.

**Fragmento 7 - p. 2 - score 4:**

4) We evaluate QoE metrics in trace-driven and real-world environments, and generalize to 3G, 4G, 5G, WiFi, syn- theticnetworks,anddifferentvideostreams(SectionV-C), and deploy the algorithms in streaming media systems (Section VI). II. BACKGROUND AND MOTIVATION The HTTP-based ABR algorithm dynamically selects the ap- propriate bitrate for video segments by monitoring network bandwidth and player buffer status in real-time. It delivers high-quality video when network conditions are good and low- ers the quality during poorer conditions to prevent buffering, thus optimizing the user QoE in Fig. 1. However, due to lim- ited network bandwidth, ABR algorithms may not always re- quest the optimal bitrate.

**Fragmento 8 - p. 7 - score 4:**

QoE breakdown: To better understand the performance of Fortuna, we compare the individual components of QoE metric. Fig. 5 shows the video bitrate, rebuffering time and smoothing penalty, i.e., the components of QoE metric. Experimental re- sults are evaluated on FCC, Belgium/4G, and HSDPA datasets. As shown, Fortuna is able to better limit rebuffering through different networks to achieve higher QoE values. rebuffering time is reduced by 4.6%-14.2% on FCC, Belgium/4G, and HS- DPA datasets by building enough buffers to handle sudden net- work ﬂuctuations. In addition, although Fortuna cannot outper- form existing solutions in every QoE metric. Instead, it is able to maximize QoE by optimizing every metric.

**Fragmento 9 - p. 7 - score 4:**

For this study, we selected 4 different datasets. We used 80% of the data for training and 20% as test data. B. Evaluation Network datasets: FCC, HSDPA, and Belgium/4G; video: di- vided into 48 video chunks, each chunk has approximately 4 seconds, the total duration is 193 seconds; H.264/MPEG-4 en- coding: {300, 750, 1200, 1850, 2850, 4300} kbps; video player: Google Chrome (built-in DASH.js), playback buffer capacity is set to 60 seconds, all ABR algorithms run in dash.js; video server: Apache2, video is deployed on the server. ABR algorithms: We compare Fortuna with state-of-art ABR algorithms. BOLA [3]: optimizing buffer occupancy using Lyapunov al- gorithm.

**Fragmento 10 - p. 7 - score 4:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8191 performance of Fortuna on the 5G network, as well as the train- ing situation. A. Implementation NVIDIA RTX A6000 GPU and a CPU with 128 cores, 128 G RAM, 64-bit Ubuntu 20.04, and MacOS operating system were selected as the experimental platform, and development tools such as Python3.5, Torch1.6, Apache2, Google Chrome, and FFmpeg. We use Mahimahi [46] to simulate network conditions, with RTT ranging from 0 to 80 ms, based on collected network traces between the client and server. The QoE metric parameters of (1) are set: N is 8, μ1 is 4.3, and μ2 is 1.

**Fragmento 11 - p. 9 - score 4:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8193 Fig. 7. The overall probability distribution of 4G and 5G network traces. By eliminating online exploration and relying on pre-trained policies, Fortuna consistently delivers high performance across changing conditions, surpassing the adaptability and efﬁciency of Pensieve. C. Generalization In Section V-B, Fortuna is tested using common network traces, which have relatively short durations. In practice, how- ever, Fortuna may encounter new network bandwidths, bitrates and require different optimal ABR strategies. To evaluate the generalization ability of Fortuna to the new network, we con- duct 2 sets of experiments.

**Fragmento 12 - p. 9 - score 4:**

Different from the previous bitrate setting (e.g., 2.85 Mbps, 4.3 Mbps that can only support 3G and 4G network). However, 5G networks [53] (i.e., including 4G and 5G, there are 175 4G and 121 5G network traces with a granularity of 1 s, 2 types: driving and walking) can support higher bitrate videos, in order to match the corresponding network throughput with the video bitrate, to prevent high throughput from always meeting high and low bitrates. Inspired by literature [54], experiment bitrate settings, namely: (20, 40, 60, 80, 110, 160) Mbps, bitrate map reward=[1, 2, 3, 12, 15, 20], (more detail in [55]), total video chunks is 157, rebuf-penalty is 160, smooth-penalty is 1.

**Fragmento 13 - p. 12 - score 4:**

Furthermore, Fortuna learns the ABR algorithm perfor- mance suboptimally from ofﬂine datasets, as ofﬂine datasets are not always optimal. In contrast, Fortuna, which learns from di- verse datasets, such as those from RL and expert demonstrations, exhibits better performance. VI. REAL-WORLD DEPLOYMENT AND EVALUATION In this section, we describe the speciﬁc deployment of For- tuna in streaming systems and evaluate it on 5G, 4G, and WiFi networks. In Section V-B, we conducted experiments using a simu- lation platform to illustrate the generalization of the Fortuna algorithm in real-world streaming media systems. In this sec- tion, we deploy Fortuna in the real world and conduct three sets of experiments.

**Fragmento 14 - p. 1 - score 3:**

Experimental results from trace-driven and real-world scenarios demonstrate that Fortuna enhances learning efﬁciency by more than 7.5%–4 ×, reduces stall time by 4.6%–14.2%, and generalizes to different network conditions and video streams. Index Terms—Adaptive bitrate algorithm, ofﬂine meta reinforcement learning, quality of experience. I. INTRODUCTION V IDEO streaming is the primary internet application, ac- countingfornearly75%ofalltrafﬁc[1].Inadaptivebitrate (ABR) video streaming, videos are typically divided into various small video chunks or segments. Video users can request spe- ciﬁc video chunks based on their preferences and network con- ditions.

**Fragmento 15 - p. 2 - score 3:**

This is because online learning of ABR al- gorithms does not explore safely and cannot effectively learn from these complex network features [25], [26]. Speciﬁcally,inreal-worldadaptivevideostreamingscenarios, learning algorithms rely on speciﬁc data or environments to train them. However, Internet data is often vast and massive, and ABR algorithms adapt to new scenarios by learning from these net- work characteristics. Because network conditions continually change over time, and due to different user preferences, ABR algorithms must balance various QoE metrics, such as improv- ing video quality and reducing rebuffering time. Unfortunately, learning algorithms often perform well on the simple training and testing datasets, but real internet data features are complex and variable, exhibiting heavy-tailed characteristics.

**Fragmento 16 - p. 3 - score 3:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8187 Fig. 2. Visualize network features, as well as video quality and buffering time of existing ABR algorithms, on the Puffer dataset. ofﬂine RL enables the model to learn the features and patterns across different distributions, enhancing its generalization abil- ity [31]. Case 2: The QoE of video users is inﬂuenced by the un- derlying TCP congestion control protocol [32], such as RTT. We observe varying network throughputs, ranging from 0 to 250 Mbps, with different RTT values across users. For example, users with a throughput of 75 Mbps exhibit a wide range of RTT values, while those with throughput between 25 and 50 Mbps of- ten experience high latency and a broader range of RTT values.

**Fragmento 17 - p. 6 - score 3:**

More mathemat- ical proofs can be found in [45]. Algorithm 1 and 2 demonstrate how to learn meta-ABR poli- cies through ofﬂine RL and generalize them to various video streaming environments. V. EXPERIMENTS AND ANALYSIS In this section, we experimentally evaluate Fortuna on dif- ferent network traces and QoE metrics. Further, we analyze the Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 18 - p. 8 - score 3:**

8192 IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 Fig. 4. Compare the QoE metrics of Fortuna and existing ABR algorithms on FCC, HSDPA/3G, and Belgium/4G networks. Examine the distribution of average QoE values for each ABR algorithm. Fig. 5. Comparing the QoE metric individual compoments of Fortuna and existing ABR algorithms on FCC, HSDPA, and Belgium/4G networks. Error bars are drawn to represent the mean value with a margin of one standard deviation. Fig. 6. Comparison of Fortuna with existing ABR algorithms on FCC and HSDPA networks. QoE metrics are considered as listed in Table I, with results normalized against the performance of Fortuna. Error bars represent ± one standard deviation.

**Fragmento 19 - p. 12 - score 3:**

During these experiments, the video client was running on a MacBook Pro laptop, accessing the video server running on Ubuntu 20.04 through the HTTP proto- col. These algorithms were deployed on dash.js, and the ex- periment was repeated several times. Video clients requested the bitrate from an Apache2 server, which ﬁrst went through the ABR algorithms before sending a signal to request video from the server. Due to the round-trip delay between the ABR algorithms and the video server, we calculated the av- erage round-trip delay under 5G, 4G, and WiFi network con- ditions, which were 4.21 ms, 70.32 ms, and 14.22 ms, re- spectively. During the experiment, Fortuna was compared with Pensieve, BOLA, and MPC, and the collected QoE dataset was normalized.

**Fragmento 20 - p. 12 - score 3:**

Long-duration video streaming sessions: To gain a deeper insight into Fortuna’s performance in diverse real-world video streaming networks, it’s important to consider that these net- works exhibit heavy-tailedness and TCP-related characteris- tics, we utilize SSIM for video quality assessment. The video undergoes de-interlacing using ffmpeg to generate a “canoni- cal” 1080p60 or 720p60 source suitable for compression. Each video chunk is encoded into ten different H.264 versions us- ing the libx264 encoder in veryfast mode. These encodings en- compass a range of options, from 240p60 video with a con- stant rate factor (CRF) of 26 (approximately 200 kbps) to 1080p60 video with a CRF of 20 (about 5,500 kbps).

**Fragmento 21 - p. 13 - score 3:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8197 Fig. 15. Comparing the QoE metric of Fortuna and existing ABR algorithms on 5G, 4G and WiFi network conditions. In the bar chart, the averages are listed, and the error bars span ± one standard deviation from the average. by training in a simulated environment, can generalize and be used in real-world streaming media networks. It can also max- imize QoE values under different conditions and improve user experience. VII. CONCLUTION We introduce Fortuna, a novel ofﬂine RL-based adaptive video streams technique that effectively adapts to real-world Internet conditions, and combines with TCP congestion con- trol to further reduce rebuffering time, optimizing QoE ob- jectives.

**Fragmento 22 - p. 1 - score 2:**

IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 8185 Optimizing Adaptive Video Streaming: Ofﬂine Reinforcement Learning and Meta-Learning in Diverse Networks Ling Yi , Yongbin Qin , and Ruizhang Huang Abstract—Recent years have seen the optimization of quality of experience (QoE) through learning adaptive bitrate (ABR) algorithms from internet video streams. However, the complex nature of the real-world Internet, characterized by heavy-tailed behavior, diversity, and unpredictability, hinder the effective learning of off-the-shelf reinforcement learning (RL)-based ABR algorithms. As a result, existing methods inevitably fail to achieve optimal performance under various network conditions and user QoE objectives.


### 8.7. evaluacion baselines experimentos

Palabras clave usadas: `evaluation, experiment, baseline, compare, comparison, Pensieve, BBA, BOLA, MPC, RobustMPC, FastMPC, Rate-based, Comyco, Oboe, A2BR, Fugu, Puffer, Ahaggar, Gelato, Plume, results, performance, ablation`

**Fragmento 1 - p. 3 - score 6:**

We compared several ABR algorithms, including Pensieve, Fugu, Comyco, BOLA, and MPC, in how well they adapt to unseen network conditions. Due to the randomness of network bandwidth, traditional methods like Pensieve struggle to converge effectively. Fugu, which combines neural network training with MPC predictions, also encounters challenges in managing unknown network conditions. Fortuna is the most op- timal among all ABR algorithms in improving video quality (SSIM) and reducing stalling time. Our ﬁndings indicate that existing methods struggle to respond effectively to these unpre- dictable scenarios. In summary, it is highly important to efﬁciently learn robust ABR algorithms under wild Internet conditions and generalize them to diverse network conditions.

**Fragmento 2 - p. 7 - score 5:**

Fugu and Comyco’s inability to adaptively change strategies and long-term decision problems using imitative learning. Additionly, it is essentially solving the RMPC problems [5]. However, RMPC estimates the network bandwidth too conservatively use model control. For example, when the network throughput becomes low, it should make full use of the playback buffer and request a low bitrate to improve QoE, but RMPC leads to insufﬁcient buffer utilization; similarly, BOLA only considers the buffer usage. As shown, these simple ﬁxed heuristics are not applicable to complex net- work throughput. Additionally, Pensieve cannot adaptively learn network characteristics, resulting in inaccurate predictions un- der certain network conditions.

**Fragmento 3 - p. 12 - score 5:**

During these experiments, the video client was running on a MacBook Pro laptop, accessing the video server running on Ubuntu 20.04 through the HTTP proto- col. These algorithms were deployed on dash.js, and the ex- periment was repeated several times. Video clients requested the bitrate from an Apache2 server, which ﬁrst went through the ABR algorithms before sending a signal to request video from the server. Due to the round-trip delay between the ABR algorithms and the video server, we calculated the av- erage round-trip delay under 5G, 4G, and WiFi network con- ditions, which were 4.21 ms, 70.32 ms, and 14.22 ms, re- spectively. During the experiment, Fortuna was compared with Pensieve, BOLA, and MPC, and the collected QoE dataset was normalized.

**Fragmento 4 - p. 1 - score 4:**

Digital Object Identiﬁer 10.1109/TMM.2025.3604930 quality level, enabling users to select the most suitable video chunk according to available bandwidth. However, due to net- work bandwidth limitations, ABR algorithms may not always request high-quality videos consistently. The main existing ABR algorithms use simple control rules or reinforcement learning (RL) based methods. For example, RB algorithm [2] is only based on network bandwidth or buffer us- age e.g., BOLA algorithm [3], [4], or a combination of the two schemes (e.g., robustMPC [5], Oboe [6], Bayesian-MPC [7]). These methods require careful adjustment and are unable to adapt to different network bandwidths or different QoE ob- jectives.

**Fragmento 5 - p. 1 - score 4:**

State-of-the-art MPC algorithm [5] uses future video chunks by dynamically optimizing QoE metrics, which has bet- ter performance than the simple ﬁxed schemes e.g., BOLA, RB. However, MPC relies on accurate network bandwidth pre- dictions, especially on future networks. Due to the variability of network bandwidth, MPC is difﬁcult to predict accurately, but inaccurate predictions may cause future video freezes and low-quality video etc. Additionally, since BOLA and MPC can- not adjust parameters according to speciﬁc network conditions and are too sensitive to parameters, then Oboe [6] is proposed to automatically adjust parameters, which can enhance QoE value in speciﬁc scenarios.

**Fragmento 6 - p. 8 - score 4:**

8192 IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 Fig. 4. Compare the QoE metrics of Fortuna and existing ABR algorithms on FCC, HSDPA/3G, and Belgium/4G networks. Examine the distribution of average QoE values for each ABR algorithm. Fig. 5. Comparing the QoE metric individual compoments of Fortuna and existing ABR algorithms on FCC, HSDPA, and Belgium/4G networks. Error bars are drawn to represent the mean value with a margin of one standard deviation. Fig. 6. Comparison of Fortuna with existing ABR algorithms on FCC and HSDPA networks. QoE metrics are considered as listed in Table I, with results normalized against the performance of Fortuna. Error bars represent ± one standard deviation.

**Fragmento 7 - p. 10 - score 4:**

Ten- sorFlow TensorBoard was used to monitor the training process during the experimental procedures. As shown in Fig. 11(a), the original Pensieve was trained using A3C, due to the random na- ture of network conditions, and the ﬂuctuations were very dras- tic, thus we used Variance reduction to optimize training the per- formance more stable. PEARL, a context-driven meta-learning approach, tends to meta-overﬁtting, which leads to suboptimal performance in unseen network conditions. Contrastingly, For- tuna leverages ofﬂine data to rapidly learn meta-ABR policies, resulting in an improvement of over 6.6%–20.1% the previous performance. Additionally, we also compared Fortuna with online meta-RL methods, using PPO to optimize the ABR algorithm, as shown in Fig.

**Fragmento 8 - p. 1 - score 3:**

Recently, Pensieve [8] was proposed to further improve QoE by using RL to train a neural network to generate ABR algo- rithms, which effectively solves the limitations of existing ABR algorithms. Alternatively, PPO-based policy optimization can be utilized to learn more efﬁcient ABR strategies [9], [10]. How- ever, due to the randomness of network bandwidth, RL-based methods are difﬁcult to converge quickly or generate a large amount of gradient variance [52]. Imitation learning [11], [12] is used for solving MPC problems, but the method is only appli- cable to known environments and cannot be used for complex network scenarios. Fugu [13] combines classical control with a learned network predictor, trained with supervised learning in situ on data from the real deployment environment.

**Fragmento 9 - p. 7 - score 3:**

Comyco [11]: The imitation MPC algorithm [5] uses neural networks to generate the ABR algorithm. Fugu [13]: Train the neural network using supervised learn- ing, and then use MPC [5] for video bitrate decision-making. CDFs: Cumulative distribution functions (CDFs) are used to evaluate the overall distribution of QoE for different ABR algo- rithms. The higher the CDF to the right, the higher the cumu- lative probability and QoE. As shown in Fig. 4, Fortuna has a higher QoE value than the existing ABR algorithms, due to the characteristics of the autonomous learning robust ABR policies, improvement range of 8.5%-31.9%. The reason is that Fortuna can better learn a wide range of network features, resulting in strong generalization on unseen networks.

**Fragmento 10 - p. 7 - score 3:**

QoE breakdown: To better understand the performance of Fortuna, we compare the individual components of QoE metric. Fig. 5 shows the video bitrate, rebuffering time and smoothing penalty, i.e., the components of QoE metric. Experimental re- sults are evaluated on FCC, Belgium/4G, and HSDPA datasets. As shown, Fortuna is able to better limit rebuffering through different networks to achieve higher QoE values. rebuffering time is reduced by 4.6%-14.2% on FCC, Belgium/4G, and HS- DPA datasets by building enough buffers to handle sudden net- work ﬂuctuations. In addition, although Fortuna cannot outper- form existing solutions in every QoE metric. Instead, it is able to maximize QoE by optimizing every metric.

**Fragmento 11 - p. 7 - score 3:**

For this study, we selected 4 different datasets. We used 80% of the data for training and 20% as test data. B. Evaluation Network datasets: FCC, HSDPA, and Belgium/4G; video: di- vided into 48 video chunks, each chunk has approximately 4 seconds, the total duration is 193 seconds; H.264/MPEG-4 en- coding: {300, 750, 1200, 1850, 2850, 4300} kbps; video player: Google Chrome (built-in DASH.js), playback buffer capacity is set to 60 seconds, all ABR algorithms run in dash.js; video server: Apache2, video is deployed on the server. ABR algorithms: We compare Fortuna with state-of-art ABR algorithms. BOLA [3]: optimizing buffer occupancy using Lyapunov al- gorithm.

**Fragmento 12 - p. 9 - score 3:**

Videos were segmented into a random number of chunks, between 20 and 100, and chunk sizes were varied by applying Gaussian noise to a standard 4-second chunk duration. This ap- proach ensured a broad range of video properties, including bi- trate options, chunk count, chunk sizes, and overall duration, to rigorously test the model’s adaptability and performance across different scenarios. As shown in Fig. 10, the results demonstrated that the gen- eralized ABR algorithm achieved nearly identical performance compared to a model exclusively trained on a reference video, The gap in QoE values is 2.8%. This ﬁnding suggests that our method’s server conﬁguration could effectively elevate stream- ing quality across a spectrum of videos, employing a concise selection of ABR algorithms.

**Fragmento 13 - p. 9 - score 3:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8193 Fig. 7. The overall probability distribution of 4G and 5G network traces. By eliminating online exploration and relying on pre-trained policies, Fortuna consistently delivers high performance across changing conditions, surpassing the adaptability and efﬁciency of Pensieve. C. Generalization In Section V-B, Fortuna is tested using common network traces, which have relatively short durations. In practice, how- ever, Fortuna may encounter new network bandwidths, bitrates and require different optimal ABR strategies. To evaluate the generalization ability of Fortuna to the new network, we con- duct 2 sets of experiments.

**Fragmento 14 - p. 9 - score 3:**

Wild ﬂuctuations can bring great challenges to the ABR algorithms, howtobalancecomponents of thevideobitrateandthestall time, thereby the ABR decision should be forward-looking enough to maximize QoE objectives and minimize stall time as much as possible. As shown in Fig. 8, Fortuna can achieve better performance on 4G and 5G networks, the stall time is reduced by 4.6%-12.2% and 0.5%-3.1% respectively. As shown, fortuna and ofﬂine- Fortuna can achieve better performance on 4G and 5G networks. However, Fugu [13] (supervised learning) cannot be adapted to different networks, as it requires speciﬁc data that cannot be adapted to new networks, and BOLA fail to achieve good performance using simple ﬁxed heuristics.

**Fragmento 15 - p. 9 - score 3:**

Furthermore, RMPC algorithm performs poorly on 5G networks due to overly con- servative predictions. However, in these heterogeneous network data, the environment is more complex and requires better ABR decisions. In contrast, RL can adaptively select the optimal bi- trates based on the network scenario. These experiments show that Fortuna can reduce stall time and maximize QoE even in the case of high and ﬂuctuating network traces, despite these networks have never encountered. Training with synthetic dataset: The training dataset has a signiﬁcant impact on the performance of RL-based algorithms and may hinder the optimal ABR strategy for RL learning.

**Fragmento 16 - p. 12 - score 3:**

This ap- proach provides a spectrum of quality and bitrate choices for the video stream, catering to diverse network conditions and devices. As shown in Fig. 14, we found that the simple Buffer-Based ABR (BBA) algorithm [62] can achieve better performance, while the ABR algorithm generated purely through RL train- ing, known as Pensieve, performs poorly. Meanwhile, we have observed that meta-RL does not consistently achieve optimal performance due to the need for adaptation across a wide range of video stream conditions. In real-world scenarios with vary- ing user preferences, BBA, which relies on fewer assumptions and requests videos based on buffer occupancy, closely approx- imates the actual video playback process.

**Fragmento 17 - p. 12 - score 3:**

The experimental results are shown in Fig. 15. Fig. 15 shows that the QoE under 5G and WiFi network con- ditions is generally higher than that under 4G networks. This is because 5G and WiFi networks have relatively high band- widths, which can support higher bitrates and lower latency, allowing the ABR algorithms to request high bitrates more sta- bly. At the same time, we found that the QoE of various ABR algorithms on 5G networks is more stable. Compared to WiFi networks, ﬂuctuations in network bandwidth can cause ABR algorithms to fail to continuously request high bitrates. Un- der 5G, 4G, and WiFi network conditions, Fortuna improved QoE values by 2.9%–5.1%, 5.2%–12.5%, and 2.6%–11.2%, respectively.

**Fragmento 18 - p. 12 - score 3:**

Furthermore, Fortuna learns the ABR algorithm perfor- mance suboptimally from ofﬂine datasets, as ofﬂine datasets are not always optimal. In contrast, Fortuna, which learns from di- verse datasets, such as those from RL and expert demonstrations, exhibits better performance. VI. REAL-WORLD DEPLOYMENT AND EVALUATION In this section, we describe the speciﬁc deployment of For- tuna in streaming systems and evaluate it on 5G, 4G, and WiFi networks. In Section V-B, we conducted experiments using a simu- lation platform to illustrate the generalization of the Fortuna algorithm in real-world streaming media systems. In this sec- tion, we deploy Fortuna in the real world and conduct three sets of experiments.

**Fragmento 19 - p. 1 - score 2:**

Experimental results from trace-driven and real-world scenarios demonstrate that Fortuna enhances learning efﬁciency by more than 7.5%–4 ×, reduces stall time by 4.6%–14.2%, and generalizes to different network conditions and video streams. Index Terms—Adaptive bitrate algorithm, ofﬂine meta reinforcement learning, quality of experience. I. INTRODUCTION V IDEO streaming is the primary internet application, ac- countingfornearly75%ofalltrafﬁc[1].Inadaptivebitrate (ABR) video streaming, videos are typically divided into various small video chunks or segments. Video users can request spe- ciﬁc video chunks based on their preferences and network con- ditions.

**Fragmento 20 - p. 3 - score 2:**

These heterogeneous network characteristics signiﬁcantly im- pact ABR algorithm decisions, affecting QoE outcomes. Since RTT inﬂuences QoE, TCP congestion control algorithms like BBR [33] and CUBIC [34] adjust data sending rates to opti- mize RTT performance. ABR algorithms must adapt to chang- ing network conditions to improve video streaming quality by leveraging these underlying network characteristics. Case 3: Learning ABR strategies often leads to poor deci- sions when faced with unknown network conditions, resulting in suboptimal video quality and increased rebuffering time. We use the Puffer dataset, with a duration of 1000 hours and a time interval of 1 s, where the network bandwidth ranges from 0 to 400 Mbps.

**Fragmento 21 - p. 7 - score 2:**

Since the playback buffer is relatively stable, it can effectively improve QoE. Pensieve [8]: ABR algorithm based on deep reinforcement learning (DRL), generating ABR algorithm by training neural network. However, the original Pensieve struggled with conver- gence due to the variability in network conditions when using the A3C algorithm. Therefore, we employed variance reduction techniques [52] in the training process to develop a more effec- tive ABR algorithm. RMPC: makes decisions about video bitrate by tackling a problem that aims to maximize QoE for several upcoming chunks. By focusing directly on improving QoE, MPC often performs better than methods that rely on ﬁxed rules [5].

**Fragmento 22 - p. 7 - score 2:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8191 performance of Fortuna on the 5G network, as well as the train- ing situation. A. Implementation NVIDIA RTX A6000 GPU and a CPU with 128 cores, 128 G RAM, 64-bit Ubuntu 20.04, and MacOS operating system were selected as the experimental platform, and development tools such as Python3.5, Torch1.6, Apache2, Google Chrome, and FFmpeg. We use Mahimahi [46] to simulate network conditions, with RTT ranging from 0 to 80 ms, based on collected network traces between the client and server. The QoE metric parameters of (1) are set: N is 8, μ1 is 4.3, and μ2 is 1.


### 8.8. resultados numericos

Palabras clave usadas: `improve, improvement, outperform, gain, %, QoE gain, higher, lower, average, result, achieve, compared to, reduce, decrease, increase, stall time, stream-years, users, ms, latency`

**Fragmento 1 - p. 12 - score 8:**

The experimental results are shown in Fig. 15. Fig. 15 shows that the QoE under 5G and WiFi network con- ditions is generally higher than that under 4G networks. This is because 5G and WiFi networks have relatively high band- widths, which can support higher bitrates and lower latency, allowing the ABR algorithms to request high bitrates more sta- bly. At the same time, we found that the QoE of various ABR algorithms on 5G networks is more stable. Compared to WiFi networks, ﬂuctuations in network bandwidth can cause ABR algorithms to fail to continuously request high bitrates. Un- der 5G, 4G, and WiFi network conditions, Fortuna improved QoE values by 2.9%–5.1%, 5.2%–12.5%, and 2.6%–11.2%, respectively.

**Fragmento 2 - p. 13 - score 7:**

Moreover, Fortuna can handle unconstrained video stream sessions. In all considered internet video streaming sce- narios, Fortuna rivals or outperforms the state-of-the-art ex- isting approaches, with an average QoE improvement ranging from 1.2%-31.9%. Additionally, experimental results demon- strate that Fortuna exhibits better generalization capabilities in unseen network conditions and QoE user preferences. In practice, we believe that Fortuna can offer valuable insights not only for bitrate adaptation of video streaming but also for TCP congestion control, as it eliminates the costly expense of online learning while enabling swift adaptation to new network conditions.

**Fragmento 3 - p. 1 - score 6:**

Experimental results from trace-driven and real-world scenarios demonstrate that Fortuna enhances learning efﬁciency by more than 7.5%–4 ×, reduces stall time by 4.6%–14.2%, and generalizes to different network conditions and video streams. Index Terms—Adaptive bitrate algorithm, ofﬂine meta reinforcement learning, quality of experience. I. INTRODUCTION V IDEO streaming is the primary internet application, ac- countingfornearly75%ofalltrafﬁc[1].Inadaptivebitrate (ABR) video streaming, videos are typically divided into various small video chunks or segments. Video users can request spe- ciﬁc video chunks based on their preferences and network con- ditions.

**Fragmento 4 - p. 7 - score 6:**

Comyco [11]: The imitation MPC algorithm [5] uses neural networks to generate the ABR algorithm. Fugu [13]: Train the neural network using supervised learn- ing, and then use MPC [5] for video bitrate decision-making. CDFs: Cumulative distribution functions (CDFs) are used to evaluate the overall distribution of QoE for different ABR algo- rithms. The higher the CDF to the right, the higher the cumu- lative probability and QoE. As shown in Fig. 4, Fortuna has a higher QoE value than the existing ABR algorithms, due to the characteristics of the autonomous learning robust ABR policies, improvement range of 8.5%-31.9%. The reason is that Fortuna can better learn a wide range of network features, resulting in strong generalization on unseen networks.

**Fragmento 5 - p. 9 - score 5:**

Videos were segmented into a random number of chunks, between 20 and 100, and chunk sizes were varied by applying Gaussian noise to a standard 4-second chunk duration. This ap- proach ensured a broad range of video properties, including bi- trate options, chunk count, chunk sizes, and overall duration, to rigorously test the model’s adaptability and performance across different scenarios. As shown in Fig. 10, the results demonstrated that the gen- eralized ABR algorithm achieved nearly identical performance compared to a model exclusively trained on a reference video, The gap in QoE values is 2.8%. This ﬁnding suggests that our method’s server conﬁguration could effectively elevate stream- ing quality across a spectrum of videos, employing a concise selection of ABR algorithms.

**Fragmento 6 - p. 9 - score 5:**

Wild ﬂuctuations can bring great challenges to the ABR algorithms, howtobalancecomponents of thevideobitrateandthestall time, thereby the ABR decision should be forward-looking enough to maximize QoE objectives and minimize stall time as much as possible. As shown in Fig. 8, Fortuna can achieve better performance on 4G and 5G networks, the stall time is reduced by 4.6%-12.2% and 0.5%-3.1% respectively. As shown, fortuna and ofﬂine- Fortuna can achieve better performance on 4G and 5G networks. However, Fugu [13] (supervised learning) cannot be adapted to different networks, as it requires speciﬁc data that cannot be adapted to new networks, and BOLA fail to achieve good performance using simple ﬁxed heuristics.

**Fragmento 7 - p. 10 - score 5:**

We compared the training steps and time as shown in Fig. 11(b) and (c), it can improve performance by more than 7.5%-4×, the average QoE can be improved by 3.7%. Speciﬁcally, it is divided into two steps. First, Reset Envi- ronment: A higher reset probability in the initial stages al- lows the agent to explore different strategies. Gradually re- ducing this probability helps stabilize learning and focus on long-term decision-making. Second, Gradual Increase of Video Stream Length: The core idea is to gradually increase task complexity. The agent transitions from handling simple, short Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.

**Fragmento 8 - p. 10 - score 5:**

12. We found that Fortuna can effectively utilize ofﬂine data to converge quickly, achieving an average reward improvement of 9%. In contrast, Meta-PPO (However, the ofﬁcial code has not been released, and we have done our best to implement the algorithm according to the pseudocode description in the paper.) [60] converges more slowly due to the need for real- time interaction with the ABR environment. Although the clip function in the PPO algorithm mitigates policy ﬂuctuations, it remains relatively stable. Curriculum Learning: In this part, we utilize Curriculum Learning to gradually increase the complexity of the video stream in order to quickly adapt the bitrate to new network conditions.

**Fragmento 9 - p. 3 - score 4:**

These heterogeneous network characteristics signiﬁcantly im- pact ABR algorithm decisions, affecting QoE outcomes. Since RTT inﬂuences QoE, TCP congestion control algorithms like BBR [33] and CUBIC [34] adjust data sending rates to opti- mize RTT performance. ABR algorithms must adapt to chang- ing network conditions to improve video streaming quality by leveraging these underlying network characteristics. Case 3: Learning ABR strategies often leads to poor deci- sions when faced with unknown network conditions, resulting in suboptimal video quality and increased rebuffering time. We use the Puffer dataset, with a duration of 1000 hours and a time interval of 1 s, where the network bandwidth ranges from 0 to 400 Mbps.

**Fragmento 10 - p. 7 - score 4:**

QoE breakdown: To better understand the performance of Fortuna, we compare the individual components of QoE metric. Fig. 5 shows the video bitrate, rebuffering time and smoothing penalty, i.e., the components of QoE metric. Experimental re- sults are evaluated on FCC, Belgium/4G, and HSDPA datasets. As shown, Fortuna is able to better limit rebuffering through different networks to achieve higher QoE values. rebuffering time is reduced by 4.6%-14.2% on FCC, Belgium/4G, and HS- DPA datasets by building enough buffers to handle sudden net- work ﬂuctuations. In addition, although Fortuna cannot outper- form existing solutions in every QoE metric. Instead, it is able to maximize QoE by optimizing every metric.

**Fragmento 11 - p. 8 - score 4:**

8192 IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 Fig. 4. Compare the QoE metrics of Fortuna and existing ABR algorithms on FCC, HSDPA/3G, and Belgium/4G networks. Examine the distribution of average QoE values for each ABR algorithm. Fig. 5. Comparing the QoE metric individual compoments of Fortuna and existing ABR algorithms on FCC, HSDPA, and Belgium/4G networks. Error bars are drawn to represent the mean value with a margin of one standard deviation. Fig. 6. Comparison of Fortuna with existing ABR algorithms on FCC and HSDPA networks. QoE metrics are considered as listed in Table I, with results normalized against the performance of Fortuna. Error bars represent ± one standard deviation.

**Fragmento 12 - p. 9 - score 4:**

In part, we take Fortuna to the extreme and train it purely using synthetic networks and generalize it to the real network. The simulated dataset utilized in the study encompasses a diverse range of network bandwidths, with the average through- put spanning from 0.2 Mbps to 4.3 Mbps, which aligns with the training video bitrates (such as H.264 encoding at 300 kbps, 750 kbps, 4300 kbps, etc.). The dataset’s transitions between states were generated using Markov modeling, and the resulting bandwidth values follow a Gaussian distribution with a granu- larity of 1 s and a uniform variance ranging from 0.05 to 0.5 [8]. We ﬁnd that Fortuna performs better on each CDF trajectory compared to Genet [19] in Fig.

**Fragmento 13 - p. 9 - score 4:**

9, average QoE value increased by12.5%. The advantage of Fortuna lies in its ability to opti- mize based on a comprehensive set of historical data and com- plex network environments. In contrast, ABR algorithms gener- ated through curriculum learning might face limitations due to constraints in the data and training strategies used during their development. Multiple videos: To evaluate Fortuna’s ability to gener- alize across varying video properties, we trained a sin- gle ABR model using 1,000 synthetic videos with diverse characteristics. Each video had a random number of bi- trate options, ranging from 3 to 10, with values chosen from {200, 300, 450, 750, 1200, 1850, 2350, 2850, 3500, 4300} kbps.

**Fragmento 14 - p. 10 - score 4:**

Ten- sorFlow TensorBoard was used to monitor the training process during the experimental procedures. As shown in Fig. 11(a), the original Pensieve was trained using A3C, due to the random na- ture of network conditions, and the ﬂuctuations were very dras- tic, thus we used Variance reduction to optimize training the per- formance more stable. PEARL, a context-driven meta-learning approach, tends to meta-overﬁtting, which leads to suboptimal performance in unseen network conditions. Contrastingly, For- tuna leverages ofﬂine data to rapidly learn meta-ABR policies, resulting in an improvement of over 6.6%–20.1% the previous performance. Additionally, we also compared Fortuna with online meta-RL methods, using PPO to optimize the ABR algorithm, as shown in Fig.

**Fragmento 15 - p. 10 - score 4:**

8194 IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 Fig. 8. Compare the average bitrate and rebuffering time of Fortuna with existing ABR algorithms, using 95% conﬁdence intervals. Fig. 9. Comparing the QoE metrics of Fortuna and Genet ABR algorithms on Belgium/4G dataset. Fig. 10. Comparing ABR algorithms trained on a diverse set of videos with those speciﬁcally trained on the test video under varying network conditions. Variance reduction [52], Jade, an RL-based ABR algorithm with human feedback (learning the ABR algorithm using Duel-PPO and adaptive entropy RL techniques [56], [57]), PEARL [58], [59], a contextualized meta-RL approach (i.e., recently used for meta-RL to achieve better ABR policies performance [18]).

**Fragmento 16 - p. 12 - score 4:**

8196 IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 Fig. 14. Long-duration video streaming sessions, i.e., varying network conditions and different user video streams. The average values for video quality and buffering are shown, with error bars spanning ± one standard deviation from the average. When considering RTT, CWND, and Queue delay, QoE can improve by 1.2-9.4%. This suggests that in a real network en- vironment, we cannot simply rely on network bandwidth for evaluation, but need to incorporate TCP congestion control for a better understanding of the ABR algorithm. These network behavioral characteristics contribute to a better understanding and learning of ABR algorithms.

**Fragmento 17 - p. 13 - score 4:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8197 Fig. 15. Comparing the QoE metric of Fortuna and existing ABR algorithms on 5G, 4G and WiFi network conditions. In the bar chart, the averages are listed, and the error bars span ± one standard deviation from the average. by training in a simulated environment, can generalize and be used in real-world streaming media networks. It can also max- imize QoE values under different conditions and improve user experience. VII. CONCLUTION We introduce Fortuna, a novel ofﬂine RL-based adaptive video streams technique that effectively adapts to real-world Internet conditions, and combines with TCP congestion con- trol to further reduce rebuffering time, optimizing QoE ob- jectives.

**Fragmento 18 - p. 1 - score 3:**

IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 8185 Optimizing Adaptive Video Streaming: Ofﬂine Reinforcement Learning and Meta-Learning in Diverse Networks Ling Yi , Yongbin Qin , and Ruizhang Huang Abstract—Recent years have seen the optimization of quality of experience (QoE) through learning adaptive bitrate (ABR) algorithms from internet video streams. However, the complex nature of the real-world Internet, characterized by heavy-tailed behavior, diversity, and unpredictability, hinder the effective learning of off-the-shelf reinforcement learning (RL)-based ABR algorithms. As a result, existing methods inevitably fail to achieve optimal performance under various network conditions and user QoE objectives.

**Fragmento 19 - p. 2 - score 3:**

Considering the diversity of the Puffer dataset [13], we visualize it in Fig. 2, comprising 10427 streams, 1258 stream-hours, and analyze the data characteristics of these real network users to illustrate why off-the-shelf ABR algo- rithms have difﬁculty in adapting to these conditions. Case 1: Network conditions ﬂuctuate over time, and long- duration video streams exhibit a heavy-tailed distribution. Ini- tial Low Load Phase (0 - 5,000 seconds), where bandwidth ﬂuc- tuates at relatively low levels, mostly below 100 Mbps, with frequent dips close to zero. This is followed by the Increased Fluctuation Phase (5,000-10,000 seconds), during which band- width varies between 0 and 200 Mbps, showing more frequent peaks and troughs.

**Fragmento 20 - p. 3 - score 3:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8187 Fig. 2. Visualize network features, as well as video quality and buffering time of existing ABR algorithms, on the Puffer dataset. ofﬂine RL enables the model to learn the features and patterns across different distributions, enhancing its generalization abil- ity [31]. Case 2: The QoE of video users is inﬂuenced by the un- derlying TCP congestion control protocol [32], such as RTT. We observe varying network throughputs, ranging from 0 to 250 Mbps, with different RTT values across users. For example, users with a throughput of 75 Mbps exhibit a wide range of RTT values, while those with throughput between 25 and 50 Mbps of- ten experience high latency and a broader range of RTT values.

**Fragmento 21 - p. 4 - score 3:**

Therefore, we demand that the algorithm be capable of reusing any non-policy data (e.g., off-policy data, expert demos, prior runs of RL) during online RL to achieve highly data-efﬁcient ﬁne-tuning. In the early stages, we needed to learn from expert- demonstrated data D. The state-of-the-art method, MPC [5], de- termines video bitrate by solving an optimization problem aimed at maximizing QoE based on the dynamic playback buffer, con- sidering several future video chunks. By directly optimizing the video QoE objective, MPC typically performs better than tradi- tional methods that rely on ﬁxed heuristics. Therefore, we use the MPC algorithm to collect expert demonstration data in order to reduce the need for online interaction between RL and the video streaming environment.

**Fragmento 22 - p. 5 - score 3:**

This dual-head design helps reduce variance in the learn- ing process, leading to more stable and efﬁcient training. Policy adaptation proceeds as: θ′ ←θ−α1∇θLπ(θ; φ′, Dtr i ), where Lπ =LAW R+λLADV (4) where λ is the weight of the normalization Z(s) of the advantage function, designed to better adapt to different network condi- tions. The AWR loss is given in (2), and the advantage regression loss LADV is given by: LADV (θ; φ′, D) = Es,a∼D  Aθ(s, a) −QD(s, a) + Vφ′ i(s) 2 (5) This loss function aims to optimize the advantage function Aθ(s, a), ensuring that the policy selects bitrates that lead to higher expected rewards. By minimizing the difference between Aθ(s, a), QD(s, a), and Vφ′ i(s), the algorithm ensures that the Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.


### 8.9. limitaciones riesgos

Palabras clave usadas: `limitation, future work, challenge, overhead, complexity, generalization, real-world, deployment, cost, computational, unstable, fail, failure, heterogeneous, bias, biased, unbiased, trace-driven, heavy-tailed, unseen, uncertainty, unpredictable, privacy, fairness`

**Fragmento 1 - p. 1 - score 4:**

We propose Fortuna, a novel ofﬂine meta RL ABR algorithm that can effectively learn from these heavy-tailed internet data features and become more practical. Fortuna is primarily divided into two phases. In the ofﬂine phase, Fortuna utilizes diverse ofﬂine data for learning to reduce the costly online RL interaction expense, while in the online phase, we gradually increase video streaming sessions complexity through curriculum learning to quickly adapt to speciﬁc network conditions. Fortuna then utilizes meta-learning to optimize ABR policies and enhance generalization. Additionally, to better learn network features, Fortuna further optimizes QoE by learning low- level TCP congestion control information.

**Fragmento 2 - p. 2 - score 4:**

Even with in situ learning, adapting to real-world environments quickly proves to be challenging. Therefore, learning network control algorithms from these extensive and representative Internet data and generalizing to novel scenarios is beyond the capabilities of off-the-shelf methods [19], [27], [28]. This work will answer: How to design a learning-based ABR algorithm that performs robustly in the wild Internet. To address these challenges and make RL more practical, we propose Ofﬂine RL-based ABR algorithm (Fortuna), which is capable of autonomously and efﬁciently learning ABR strate- gies in the face of the variability and heavy-tailed nature of heterogeneous network.

**Fragmento 3 - p. 1 - score 3:**

IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 8185 Optimizing Adaptive Video Streaming: Ofﬂine Reinforcement Learning and Meta-Learning in Diverse Networks Ling Yi , Yongbin Qin , and Ruizhang Huang Abstract—Recent years have seen the optimization of quality of experience (QoE) through learning adaptive bitrate (ABR) algorithms from internet video streams. However, the complex nature of the real-world Internet, characterized by heavy-tailed behavior, diversity, and unpredictability, hinder the effective learning of off-the-shelf reinforcement learning (RL)-based ABR algorithms. As a result, existing methods inevitably fail to achieve optimal performance under various network conditions and user QoE objectives.

**Fragmento 4 - p. 12 - score 3:**

Furthermore, Fortuna learns the ABR algorithm perfor- mance suboptimally from ofﬂine datasets, as ofﬂine datasets are not always optimal. In contrast, Fortuna, which learns from di- verse datasets, such as those from RL and expert demonstrations, exhibits better performance. VI. REAL-WORLD DEPLOYMENT AND EVALUATION In this section, we describe the speciﬁc deployment of For- tuna in streaming systems and evaluate it on 5G, 4G, and WiFi networks. In Section V-B, we conducted experiments using a simu- lation platform to illustrate the generalization of the Fortuna algorithm in real-world streaming media systems. In this sec- tion, we deploy Fortuna in the real world and conduct three sets of experiments.

**Fragmento 5 - p. 13 - score 3:**

Moreover, Fortuna can handle unconstrained video stream sessions. In all considered internet video streaming sce- narios, Fortuna rivals or outperforms the state-of-the-art ex- isting approaches, with an average QoE improvement ranging from 1.2%-31.9%. Additionally, experimental results demon- strate that Fortuna exhibits better generalization capabilities in unseen network conditions and QoE user preferences. In practice, we believe that Fortuna can offer valuable insights not only for bitrate adaptation of video streaming but also for TCP congestion control, as it eliminates the costly expense of online learning while enabling swift adaptation to new network conditions.

**Fragmento 6 - p. 1 - score 2:**

Recently, Pensieve [8] was proposed to further improve QoE by using RL to train a neural network to generate ABR algo- rithms, which effectively solves the limitations of existing ABR algorithms. Alternatively, PPO-based policy optimization can be utilized to learn more efﬁcient ABR strategies [9], [10]. How- ever, due to the randomness of network bandwidth, RL-based methods are difﬁcult to converge quickly or generate a large amount of gradient variance [52]. Imitation learning [11], [12] is used for solving MPC problems, but the method is only appli- cable to known environments and cannot be used for complex network scenarios. Fugu [13] combines classical control with a learned network predictor, trained with supervised learning in situ on data from the real deployment environment.

**Fragmento 7 - p. 1 - score 2:**

Experimental results from trace-driven and real-world scenarios demonstrate that Fortuna enhances learning efﬁciency by more than 7.5%–4 ×, reduces stall time by 4.6%–14.2%, and generalizes to different network conditions and video streams. Index Terms—Adaptive bitrate algorithm, ofﬂine meta reinforcement learning, quality of experience. I. INTRODUCTION V IDEO streaming is the primary internet application, ac- countingfornearly75%ofalltrafﬁc[1].Inadaptivebitrate (ABR) video streaming, videos are typically divided into various small video chunks or segments. Video users can request spe- ciﬁc video chunks based on their preferences and network con- ditions.

**Fragmento 8 - p. 2 - score 2:**

This is because online learning of ABR al- gorithms does not explore safely and cannot effectively learn from these complex network features [25], [26]. Speciﬁcally,inreal-worldadaptivevideostreamingscenarios, learning algorithms rely on speciﬁc data or environments to train them. However, Internet data is often vast and massive, and ABR algorithms adapt to new scenarios by learning from these net- work characteristics. Because network conditions continually change over time, and due to different user preferences, ABR algorithms must balance various QoE metrics, such as improv- ing video quality and reducing rebuffering time. Unfortunately, learning algorithms often perform well on the simple training and testing datasets, but real internet data features are complex and variable, exhibiting heavy-tailed characteristics.

**Fragmento 9 - p. 2 - score 2:**

Fortuna is primarily divided into two stages. In the ofﬂine phase, it leverages domain knowledge to ﬁrst learn from expert data, and then collects runs of RL data. In the online phase, optimization takes place, gradually increasing the complexity of the video stream through curriculum learn- ing [20], [29]. However, ofﬂine ABR strategies cannot adapt to new network conditions. To enhance the generalization of Fortuna, we employ meta-learning for continuous optimization. Furthermore, ABR algorithms interact with TCP congestion control mechanisms, such as congestion window (CWND) and round-trip time (RTT). To better understand the underlying net- work behavior features, we consider TCP congestion control to facilitate the effective learning of ABR algorithms.

**Fragmento 10 - p. 2 - score 2:**

4) We evaluate QoE metrics in trace-driven and real-world environments, and generalize to 3G, 4G, 5G, WiFi, syn- theticnetworks,anddifferentvideostreams(SectionV-C), and deploy the algorithms in streaming media systems (Section VI). II. BACKGROUND AND MOTIVATION The HTTP-based ABR algorithm dynamically selects the ap- propriate bitrate for video segments by monitoring network bandwidth and player buffer status in real-time. It delivers high-quality video when network conditions are good and low- ers the quality during poorer conditions to prevent buffering, thus optimizing the user QoE in Fig. 1. However, due to lim- ited network bandwidth, ABR algorithms may not always re- quest the optimal bitrate.

**Fragmento 11 - p. 2 - score 2:**

8186 IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 strategy [20], enabling RL models to perform better across a wider range of network environments. However, this method fails to effectively learn from large volumes of ofﬂine data as well as adapt to the complexity of video streams. Zuo et al. [21] introduce Ruyi, an off-policy RL-based video streaming system that integrates preference awareness into the QoE model and the ABR algorithm [22], [23]. It is optimized with a modiﬁed Deep Q-learning algorithm using experience replay [24]. Each scheme can be used in a speciﬁc environment, but cannot effec- tively learn and be generalized to diverse network environments or bitrate decisions.

**Fragmento 12 - p. 3 - score 2:**

We compared several ABR algorithms, including Pensieve, Fugu, Comyco, BOLA, and MPC, in how well they adapt to unseen network conditions. Due to the randomness of network bandwidth, traditional methods like Pensieve struggle to converge effectively. Fugu, which combines neural network training with MPC predictions, also encounters challenges in managing unknown network conditions. Fortuna is the most op- timal among all ABR algorithms in improving video quality (SSIM) and reducing stalling time. Our ﬁndings indicate that existing methods struggle to respond effectively to these unpre- dictable scenarios. In summary, it is highly important to efﬁciently learn robust ABR algorithms under wild Internet conditions and generalize them to diverse network conditions.

**Fragmento 13 - p. 4 - score 2:**

IV. DESIGN In this section, based on ofﬂine RL theory, we describe how to efﬁciently learn a robust ABR algorithm. We then utilize meta- learningtolearnmeta-ABRpoliciestoadapttodifferentnetwork conditions. A. Addressing Data Efﬁciency Issues in RL. Academia and industry are actively researching neural net- work efﬁciency [31], [38], [39]. In traditional deep RL with real-time online interactions like Pensieve, it often takes around 50,000 iterations and 4 hours to converge [8]. However, when ap- plying this to real-world environments, like learning in situ [13], convergence could take up to 2 years. This highlights the prac- tical challenges of neural network training, particularly for real- world applications.

**Fragmento 14 - p. 4 - score 2:**

In practice, RL-based ABR algorithms need to quickly learn the optimal policy π∗and generalize across various types of net- work conditions, i.e., learn the optimal policy π∗from prior data D = (si, ai, si+1, ri). One of the simplest methods for applying RL is to use prior data D, such as pre-trained policies from imita- tion learning (e.g., Comyco [11]), and then reﬁne them through RL [40], [41]. However, this approach has two limitations: (1) the prior data may not be optimal, and (2) ﬁne-tuning the policy lacks data efﬁciency as it cannot make efﬁcient use of prior data during RL [37]. In real-world environment, data efﬁ- ciency is of paramount importance.

**Fragmento 15 - p. 6 - score 2:**

8190 IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 policy is consistent with both the value and action-value func- tions. This helps improve the policy’s ability to adapt video bi- trate to varying network conditions, such as bandwidth ﬂuctua- tions, to select the optimal bitrate. Outer-Loop: The outer loop focuses on globally optimizing the initial strategy across multiple different network environ- ments (tasks) M, aiming to enhance the generalization ability of the strategy for unseen network ﬂuctuations. For the outer loop update, we sample a distinct batch of data, meta-test Dts i , to promote few-shot generalization instead of memorizing the adaptation data.

**Fragmento 16 - p. 7 - score 2:**

Comyco [11]: The imitation MPC algorithm [5] uses neural networks to generate the ABR algorithm. Fugu [13]: Train the neural network using supervised learn- ing, and then use MPC [5] for video bitrate decision-making. CDFs: Cumulative distribution functions (CDFs) are used to evaluate the overall distribution of QoE for different ABR algo- rithms. The higher the CDF to the right, the higher the cumu- lative probability and QoE. As shown in Fig. 4, Fortuna has a higher QoE value than the existing ABR algorithms, due to the characteristics of the autonomous learning robust ABR policies, improvement range of 8.5%-31.9%. The reason is that Fortuna can better learn a wide range of network features, resulting in strong generalization on unseen networks.

**Fragmento 17 - p. 9 - score 2:**

Wild ﬂuctuations can bring great challenges to the ABR algorithms, howtobalancecomponents of thevideobitrateandthestall time, thereby the ABR decision should be forward-looking enough to maximize QoE objectives and minimize stall time as much as possible. As shown in Fig. 8, Fortuna can achieve better performance on 4G and 5G networks, the stall time is reduced by 4.6%-12.2% and 0.5%-3.1% respectively. As shown, fortuna and ofﬂine- Fortuna can achieve better performance on 4G and 5G networks. However, Fugu [13] (supervised learning) cannot be adapted to different networks, as it requires speciﬁc data that cannot be adapted to new networks, and BOLA fail to achieve good performance using simple ﬁxed heuristics.

**Fragmento 18 - p. 12 - score 2:**

MPC predicts bitrates based on past network bandwidth. However, in a real environ- ment, these network characteristics are complex and variable, inﬂuenced by factors such as TCP and varying user preferences, making adaptation to real network conditions difﬁcult. Fugu ex- hibits weaker generalization in unknown network conditions us- ing supervised learning, whereas Fortuna consistently performs well in these unknown networks and user preferences. By learn- ing these features and underlying TCP controls, it can better understand the behavioral characteristics of the network. In addi- tion, we also found that off-the-shelf meta-learning-based ABR algorithms face challenges in adapting to new network condi- tions.

**Fragmento 19 - p. 12 - score 2:**

Long-duration video streaming sessions: To gain a deeper insight into Fortuna’s performance in diverse real-world video streaming networks, it’s important to consider that these net- works exhibit heavy-tailedness and TCP-related characteris- tics, we utilize SSIM for video quality assessment. The video undergoes de-interlacing using ffmpeg to generate a “canoni- cal” 1080p60 or 720p60 source suitable for compression. Each video chunk is encoded into ten different H.264 versions us- ing the libx264 encoder in veryfast mode. These encodings en- compass a range of options, from 240p60 video with a con- stant rate factor (CRF) of 26 (approximately 200 kbps) to 1080p60 video with a CRF of 20 (about 5,500 kbps).

**Fragmento 20 - p. 13 - score 2:**

Netw., vol. 28, no. 4, pp. 1698–1711, Aug. 2020. [4] B. Wang, M. Xu, F. Ren, and J. Wu, “Improving robustness of DASH against unpredictable network variations,” IEEE Trans. Multimedia, vol. 24, pp. 323–337, 2022. [5] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic approach for dynamic adaptive video streaming over HTTP,” in Proc. ACM Conf. Special Int. Group Data Commun. (SIGCOMM), 2015, pp. 325–338. [6] A. Lekharu, S. Kumar, A. Sur, and A. Sarkar, “A QoE aware LSTM based bit-rate prediction model for DASH video,” in Proc. 10th Int. Conf. Commun. Syst. Netw. (COMSNETS), 2018, pp. 392–395. [7] N. Kan et al., “Uncertainty-aware robust adaptive video streaming with bayesian neural network and model predictive control,” in Proc.

**Fragmento 21 - p. 13 - score 2:**

1126–1135. [16] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, and L. Sun, “Learning tai- lored adaptive bitrate algorithms to heterogeneous network conditions: A domain-speciﬁc priors and meta-reinforcement learning approach,” IEEE J. Sel. Areas Commun., vol. 40, no. 8, pp. 2485–2503, Aug. 2022. [17] S. Wang, J. Lin, and Y. Dai, “MMVS: Enabling robust adaptive video streaming for wildly ﬂuctuating and heterogeneous networks,” IEEE Trans. Multimedia, vol. 26, pp. 11018–11030, 2024. [18] N. Kan et al., “Improving generalization for neural adaptive video stream- ing via meta reinforcement learning,” in Proc. 30th ACM Int. Conf. Mul- timedia, 2022, pp. 3006–3016. [19] Z. Xia, Y. Zhou, F.

**Fragmento 22 - p. 1 - score 1:**

Digital Object Identiﬁer 10.1109/TMM.2025.3604930 quality level, enabling users to select the most suitable video chunk according to available bandwidth. However, due to net- work bandwidth limitations, ABR algorithms may not always request high-quality videos consistently. The main existing ABR algorithms use simple control rules or reinforcement learning (RL) based methods. For example, RB algorithm [2] is only based on network bandwidth or buffer us- age e.g., BOLA algorithm [3], [4], or a combination of the two schemes (e.g., robustMPC [5], Oboe [6], Bayesian-MPC [7]). These methods require careful adjustment and are unable to adapt to different network bandwidths or different QoE ob- jectives.


### 8.10. ideas phase45 v1 controller

Palabras clave usadas: `safe, safety, risk, risk-aware, risk-calibrated, conservative, fallback, uncertainty, lower bound, buffer, low buffer, variable, fluctuation, tail, severe, rebuffering, stall, guidance, expert, hybrid, meta, environment-aware, trace skew, cluster, prioritize, fairness, multi-user, TCP, BPM, BSM`

**Fragmento 1 - p. 2 - score 5:**

This is because online learning of ABR al- gorithms does not explore safely and cannot effectively learn from these complex network features [25], [26]. Speciﬁcally,inreal-worldadaptivevideostreamingscenarios, learning algorithms rely on speciﬁc data or environments to train them. However, Internet data is often vast and massive, and ABR algorithms adapt to new scenarios by learning from these net- work characteristics. Because network conditions continually change over time, and due to different user preferences, ABR algorithms must balance various QoE metrics, such as improv- ing video quality and reducing rebuffering time. Unfortunately, learning algorithms often perform well on the simple training and testing datasets, but real internet data features are complex and variable, exhibiting heavy-tailed characteristics.

**Fragmento 2 - p. 8 - score 5:**

6, For- tuna leverages ofﬂine meta-learning to pre-train adaptive ABR strategies tailored to various QoE objectives. Un- like traditional ABR algorithms with ﬁxed control laws or Pensieve’s online learning approach, Fortuna’s pre-trained model can rapidly adapt to QoElog, QoElin, and QoEhd scenarios: TABLE I QOE MODELS AND THEIR CORRESPONDING PARAMETERS r For QoElog, Fortuna minimizes rebuffering risk by prior- itizing bitrate stability while avoiding unnecessary high- bitrate jumps. r For QoElin, it aggressively increases bitrate to maxi- mize user-perceived quality without sacriﬁcing playback smoothness. r In QoEhd optimization, Fortuna employs foresight to rapidly build buffer with low bitrates and switches directly to HD quality once buffer conditions are favorable, all without online tuning.

**Fragmento 3 - p. 1 - score 4:**

Addi- tionally, ABRL [14] converts ABR policy into a linear model for better comprehension and safety, allowing human engineers to verify it while slightly increasing the average stall rate by 0.8%. Another approach is to employ meta-RL techniques like MAML [15], [16], [17] or Pearl [18] to adaptive to various network conditions. Moreover, Genet [19] introduces increas- ingly challenging environments through a curriculum learning 1520-9210 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission.

**Fragmento 4 - p. 2 - score 4:**

To success- fully and efﬁciently develop high-quality ABR strategies, we are driven to explore new data efﬁciency [30] approaches and innovative RL techniques. In summary, the main contributions of this paper are the fol- lowing. 1) We analyze the issues present in the current heterogeneous networkandproposeFortuna,amorepracticalofﬂinemeta RL-based ABR method. Fig. 1. The principle of HTTP-based dynamic adaptive video streaming. 2) A novel RL technique uses curriculum learning to handle unbounded video streaming sessions. 3) To better learn the underlying network behavior features, considering that ABR algorithms interact with underly- ing TCP congestion control, learning these features can further reduce rebuffering and optimize QoE.

**Fragmento 5 - p. 13 - score 4:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8197 Fig. 15. Comparing the QoE metric of Fortuna and existing ABR algorithms on 5G, 4G and WiFi network conditions. In the bar chart, the averages are listed, and the error bars span ± one standard deviation from the average. by training in a simulated environment, can generalize and be used in real-world streaming media networks. It can also max- imize QoE values under different conditions and improve user experience. VII. CONCLUTION We introduce Fortuna, a novel ofﬂine RL-based adaptive video streams technique that effectively adapts to real-world Internet conditions, and combines with TCP congestion con- trol to further reduce rebuffering time, optimizing QoE ob- jectives.

**Fragmento 6 - p. 14 - score 4:**

Int. Conf. Mach. Learn., 2019, pp. 5331–5340. [59] “Meta RL,” (n.d.). [Online]. Available: https://github.com/katerakelly/ oyster [60] A. Bentaleb, M. Lim, M. N. Akcay, A. C. Begen, and R. Zimmer- mann, “Bitrate adaptation and guidance with meta reinforcement learn- ing,” IEEE Trans. Mobile Comput., vol. 23, no. 11, pp. 10378–10392, Nov. 2024. [61] M. Allman, V. Paxson, and E. Blanton, “RFC 5681: TCP congestion con- trol,” 2009. [62] T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Wat- son, “A buffer-based approach to rate adaptation: Evidence from a large video streaming service,” in Proc. ACM Conf. SIGCOMM, 2014, pp. 187–198. Ling Yi received the masters degree in computer science in 2022 from Guizhou University, Guiyang, China,whereheiscurrentlyworkingtowardthePh.D.

**Fragmento 7 - p. 1 - score 3:**

We propose Fortuna, a novel ofﬂine meta RL ABR algorithm that can effectively learn from these heavy-tailed internet data features and become more practical. Fortuna is primarily divided into two phases. In the ofﬂine phase, Fortuna utilizes diverse ofﬂine data for learning to reduce the costly online RL interaction expense, while in the online phase, we gradually increase video streaming sessions complexity through curriculum learning to quickly adapt to speciﬁc network conditions. Fortuna then utilizes meta-learning to optimize ABR policies and enhance generalization. Additionally, to better learn network features, Fortuna further optimizes QoE by learning low- level TCP congestion control information.

**Fragmento 8 - p. 2 - score 3:**

Fortuna is primarily divided into two stages. In the ofﬂine phase, it leverages domain knowledge to ﬁrst learn from expert data, and then collects runs of RL data. In the online phase, optimization takes place, gradually increasing the complexity of the video stream through curriculum learn- ing [20], [29]. However, ofﬂine ABR strategies cannot adapt to new network conditions. To enhance the generalization of Fortuna, we employ meta-learning for continuous optimization. Furthermore, ABR algorithms interact with TCP congestion control mechanisms, such as congestion window (CWND) and round-trip time (RTT). To better understand the underlying net- work behavior features, we consider TCP congestion control to facilitate the effective learning of ABR algorithms.

**Fragmento 9 - p. 3 - score 3:**

III. DEFINE OFFLINE META ABR ALGORITHM Ofﬂine-RL is conducting online learning of the optimal policy π∗from prior data D (i.e., off-policy data, expert demos, prior runs of RL). At time t, the agent observes the current state st (i.e., throughtput Ct, the buffer size Bt, chunk bitrate Rn), and selects an action at (i.e., chunk bitrate Rn) according to its policy. The video client then receives the action at and transitions to a new state st+1, providing the agent with a reward rt. The goal of the ABR agent is to learn a policy that maximizes the expected cumulative discounted reward value E[∞ t=0 γtrt]. The entire process follows a Markov decision process (MDP), denoted by M = (S, A, O, P, R),whereS isthestatespace,Aistheaction space, O is the observation space, P is the transition probability function, and R is the reward function.

**Fragmento 10 - p. 3 - score 3:**

YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS 8187 Fig. 2. Visualize network features, as well as video quality and buffering time of existing ABR algorithms, on the Puffer dataset. ofﬂine RL enables the model to learn the features and patterns across different distributions, enhancing its generalization abil- ity [31]. Case 2: The QoE of video users is inﬂuenced by the un- derlying TCP congestion control protocol [32], such as RTT. We observe varying network throughputs, ranging from 0 to 250 Mbps, with different RTT values across users. For example, users with a throughput of 75 Mbps exhibit a wide range of RTT values, while those with throughput between 25 and 50 Mbps of- ten experience high latency and a broader range of RTT values.

**Fragmento 11 - p. 3 - score 3:**

These heterogeneous network characteristics signiﬁcantly im- pact ABR algorithm decisions, affecting QoE outcomes. Since RTT inﬂuences QoE, TCP congestion control algorithms like BBR [33] and CUBIC [34] adjust data sending rates to opti- mize RTT performance. ABR algorithms must adapt to chang- ing network conditions to improve video streaming quality by leveraging these underlying network characteristics. Case 3: Learning ABR strategies often leads to poor deci- sions when faced with unknown network conditions, resulting in suboptimal video quality and increased rebuffering time. We use the Puffer dataset, with a duration of 1000 hours and a time interval of 1 s, where the network bandwidth ranges from 0 to 400 Mbps.

**Fragmento 12 - p. 3 - score 3:**

Reward rt: The environment evaluates different actions at, re- ﬂects the quality of at, and improves the policy πθ. rt reﬂects the quality of different bitrates, rebuffering time and video switch- ing frequency. We adopt the QoE metric provided by MPC [5] QoEN = N  n=1 q (Rn) −μ1 N−1 n=1 |q (Rn+1) −q (Rn)| −μ2 N  n=1 Tn (1) A video consists of N chunks, q(.) represents video quality, such as SSIM [35] or VMAF [36], where μ1 and μ2 are the non-negative weight coefﬁcients corresponding to video quality switching frequency and rebuffering time. Meta-ABR Task: In meta-RL, tasks M are drawn from a dis- tribution p(M), representing the diversity of network condi- tions [15].

**Fragmento 13 - p. 5 - score 3:**

Fortuna uses the RL Actor-Critic (policy and value network) approach in Fig. 3. The training process is as follows: Step 1: Input is the state st, which includes 7 variables, namely: throughtput Ct, chunk download time dk(Rk)/Ck, next chunk sizes Rn+1, RTT, and the buffer size Bt, remaining chunks N and chunk bitrate Rn. Neural networks: The number of hidden layers is 1, and 128 convolution kernels and a fully connected network are used for feature extraction. The size of the convolution kernel is 4 and the step size is 1. Step 2: When receiving the state st, the agent selects the cor- responding action at based on the meta-policy πθ, and the prob- ability distribution is deﬁned as : (st, at) →[0, 1], (st, at) is the probability that the action at may take in state st.

**Fragmento 14 - p. 10 - score 3:**

8194 IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 Fig. 8. Compare the average bitrate and rebuffering time of Fortuna with existing ABR algorithms, using 95% conﬁdence intervals. Fig. 9. Comparing the QoE metrics of Fortuna and Genet ABR algorithms on Belgium/4G dataset. Fig. 10. Comparing ABR algorithms trained on a diverse set of videos with those speciﬁcally trained on the test video under varying network conditions. Variance reduction [52], Jade, an RL-based ABR algorithm with human feedback (learning the ABR algorithm using Duel-PPO and adaptive entropy RL techniques [56], [57]), PEARL [58], [59], a contextualized meta-RL approach (i.e., recently used for meta-RL to achieve better ABR policies performance [18]).

**Fragmento 15 - p. 12 - score 3:**

MPC predicts bitrates based on past network bandwidth. However, in a real environ- ment, these network characteristics are complex and variable, inﬂuenced by factors such as TCP and varying user preferences, making adaptation to real network conditions difﬁcult. Fugu ex- hibits weaker generalization in unknown network conditions us- ing supervised learning, whereas Fortuna consistently performs well in these unknown networks and user preferences. By learn- ing these features and underlying TCP controls, it can better understand the behavioral characteristics of the network. In addi- tion, we also found that off-the-shelf meta-learning-based ABR algorithms face challenges in adapting to new network condi- tions.

**Fragmento 16 - p. 1 - score 2:**

IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025 8185 Optimizing Adaptive Video Streaming: Ofﬂine Reinforcement Learning and Meta-Learning in Diverse Networks Ling Yi , Yongbin Qin , and Ruizhang Huang Abstract—Recent years have seen the optimization of quality of experience (QoE) through learning adaptive bitrate (ABR) algorithms from internet video streams. However, the complex nature of the real-world Internet, characterized by heavy-tailed behavior, diversity, and unpredictability, hinder the effective learning of off-the-shelf reinforcement learning (RL)-based ABR algorithms. As a result, existing methods inevitably fail to achieve optimal performance under various network conditions and user QoE objectives.

**Fragmento 17 - p. 1 - score 2:**

Experimental results from trace-driven and real-world scenarios demonstrate that Fortuna enhances learning efﬁciency by more than 7.5%–4 ×, reduces stall time by 4.6%–14.2%, and generalizes to different network conditions and video streams. Index Terms—Adaptive bitrate algorithm, ofﬂine meta reinforcement learning, quality of experience. I. INTRODUCTION V IDEO streaming is the primary internet application, ac- countingfornearly75%ofalltrafﬁc[1].Inadaptivebitrate (ABR) video streaming, videos are typically divided into various small video chunks or segments. Video users can request spe- ciﬁc video chunks based on their preferences and network con- ditions.

**Fragmento 18 - p. 2 - score 2:**

Considering the diversity of the Puffer dataset [13], we visualize it in Fig. 2, comprising 10427 streams, 1258 stream-hours, and analyze the data characteristics of these real network users to illustrate why off-the-shelf ABR algo- rithms have difﬁculty in adapting to these conditions. Case 1: Network conditions ﬂuctuate over time, and long- duration video streams exhibit a heavy-tailed distribution. Ini- tial Low Load Phase (0 - 5,000 seconds), where bandwidth ﬂuc- tuates at relatively low levels, mostly below 100 Mbps, with frequent dips close to zero. This is followed by the Increased Fluctuation Phase (5,000-10,000 seconds), during which band- width varies between 0 and 200 Mbps, showing more frequent peaks and troughs.

**Fragmento 19 - p. 4 - score 2:**

Therefore, we demand that the algorithm be capable of reusing any non-policy data (e.g., off-policy data, expert demos, prior runs of RL) during online RL to achieve highly data-efﬁcient ﬁne-tuning. In the early stages, we needed to learn from expert- demonstrated data D. The state-of-the-art method, MPC [5], de- termines video bitrate by solving an optimization problem aimed at maximizing QoE based on the dynamic playback buffer, con- sidering several future video chunks. By directly optimizing the video QoE objective, MPC typically performs better than tradi- tional methods that rely on ﬁxed heuristics. Therefore, we use the MPC algorithm to collect expert demonstration data in order to reduce the need for online interaction between RL and the video streaming environment.

**Fragmento 20 - p. 5 - score 2:**

As its ABR strategy improves, we extend the episode length, making the problem more challenging. The concept of gradually increas- ing video stream sequence length—and, consequently, prob- lem complexity—during training realizes curriculum learning for ABR [29]. C. Learning meta-ABR Algorithm Fortuna is an ofﬂine meta-RL ABR algorithm that learns ini- tializations φ and θ for a value function Vφ and meta policy πθ, respectively, enabling rapid adaptation to a new network condi- tion encountered at meta-test time via gradient descent. Fortuna mainly consists of inner loops and outer loops [15], [42]. Next, we will provide a detailed overview of the implementation pro- cess.

**Fragmento 21 - p. 6 - score 2:**

Traditional gradient descent updates result in rank-1 changes, whereas with the latent vector z, the rank of weight updates is bounded by: rank(ΔW ∗) ≤min(d, c), allowing higher-rank transformations and richer adaptation strategies. Algorithm 1: Learning meta-ABR policies through ofﬂine RL with gradually increasing video stream length 1: Require: network environments {Mi}; ofﬂine datasets Di containing trajectories τ: (st, at, rt) 2: Require: Initial video stream length Tinit, increment ΔT, maximum stream length Tmax 3: Hyperparameters: Inner-loop learning rates α1 (policy), η1 (value); outer-loop learning rates α2, η2; training iterations k 4: Initialize meta-policy parameters θ and value function parameters φ 5: for k iterations do 6: for each network environment Mi do 7: Sample disjoint meta-training and meta-test data batches Dtr i and Dts i from Di 8: Calculate video stream length for the current stage: Tk = min(Tinit + ΔT · (k −1), Tmax) 9: Adapt value function: φ′ ←φ −η1∇φLV (φ; Dtr i ) 10: Adapt policy: θ′ ←θ −α1∇θLπ(θ; φ′; Dtr i ), where Lπ = LAW R + λLADV 11: end for 12: Meta-update value function: φ ←φ −η2  i ∇φLV (φ′; Dts i ) 13: Meta-update policy: θ ←θ −α2  i ∇θLAW R(θ′; φ′; Dts i ) 14: end for Algorithm 2: Generalizing meta-ABR policies across di- verse environments 1: Input: Test network environment Mj, ofﬂine experience buffer D, meta-policy πθ, and meta-value function Vφ 2: Hyperparameters: Learning rates α1, η1; number of adaptation steps k 3: Initialize policy parameters θ0 = θ and value function parameters φ0 = φ 4: for k adaptation steps do 5: Adapt value function: φt+1 ←φt −η1∇φLV (φt; D) 6: Adapt policy: θt+1 ←θt −α1∇θLπ(θt; φt+1; D) 7: end for In summary, the latent vector z enhances ABR algorithms by enabling dynamic weight and bias generatio

**Fragmento 22 - p. 7 - score 2:**

Fugu and Comyco’s inability to adaptively change strategies and long-term decision problems using imitative learning. Additionly, it is essentially solving the RMPC problems [5]. However, RMPC estimates the network bandwidth too conservatively use model control. For example, when the network throughput becomes low, it should make full use of the playback buffer and request a low bitrate to improve QoE, but RMPC leads to insufﬁcient buffer utilization; similarly, BOLA only considers the buffer usage. As shown, these simple ﬁxed heuristics are not applicable to complex net- work throughput. Additionally, Pensieve cannot adaptively learn network characteristics, resulting in inaccurate predictions un- der certain network conditions.


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
IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025
8185
Optimizing Adaptive Video Streaming: Ofﬂine
Reinforcement Learning and Meta-Learning
in Diverse Networks
Ling Yi
, Yongbin Qin
, and Ruizhang Huang
Abstract—Recent years have seen the optimization of quality
of experience (QoE) through learning adaptive bitrate (ABR)
algorithms from internet video streams. However, the complex
nature of the real-world Internet, characterized by heavy-tailed
behavior, diversity, and unpredictability, hinder the effective
learning of off-the-shelf reinforcement learning (RL)-based ABR
algorithms. As a result, existing methods inevitably fail to
achieve optimal performance under various network conditions
and user QoE objectives. We propose Fortuna, a novel ofﬂine
meta RL ABR algorithm that can effectively learn from these
heavy-tailed internet data features and become more practical.
Fortuna is primarily divided into two phases. In the ofﬂine
phase, Fortuna utilizes diverse ofﬂine data for learning to reduce
the costly online RL interaction expense, while in the online
phase, we gradually increase video streaming sessions complexity
through curriculum learning to quickly adapt to speciﬁc network
conditions. Fortuna then utilizes meta-learning to optimize ABR
policies and enhance generalization. Additionally, to better learn
network features, Fortuna further optimizes QoE by learning low-
level TCP congestion control information. Experimental results
from trace-driven and real-world scenarios demonstrate that
Fortuna enhances learning efﬁciency by more than 7.5%–4 ×,
reduces stall time by 4.6%–14.2%, and generalizes to different
network conditions and video streams.
Index
Terms—Adaptive
bitrate
algorithm,
ofﬂine
meta
reinforcement learning, quality of experience.
I. INTRODUCTION
V
IDEO streaming is the primary internet application, ac-
countingfornearly75%ofalltrafﬁc[1].Inadaptivebitrate
(ABR) video streaming, videos are typically divided into various
small video chunks or segments. Video users can request spe-
ciﬁc video chunks based on their preferences and network con-
ditions. Each video chunk is assigned a particular bitrate and
Received 18 November 2024; revised 22 January 2025; accepted 15 Febru-
ary 2025. Date of publication 10 September 2025; date of current version 12
November 2025. This work was supported in part by the National Natural Sci-
ence Foundation of China under Grant 62066008, in part by the Key Projects of
Science and Technology of Guizhou Province under Grant [2020]1Z055, and in
partbytheNationalKeyR&DProgramofChinaunderGrant2023YFC3304500.
The associate editor coordinating the review of this article and approving it for
publication was Prof. Qiang Wu. (Corresponding author: Yongbin Qin.)
The authors are with the Text Computing & Cognitive Intelligence Engi-
neering Research Center of National Education Ministry, College of Computer
Science and Technology, Guizhou University, Guiyang 550025, China, and also
with the State Key Laboratory of Public Big Data, College of Computer Science
and Technology, Guizhou University, Guiyang 550025, China (e-mail: yiling-
phd@gmail.com; ybqin@gzu.edu.cn; cse.rzhuang@gzu.edu.cn).
Digital Object Identiﬁer 10.1109/TMM.2025.3604930
quality level, enabling users to select the most suitable video
chunk according to available bandwidth. However, due to net-
work bandwidth limitations, ABR algorithms may not always
request high-quality videos consistently.
The main existing ABR algorithms use simple control rules or
reinforcement learning (RL) based methods. For example, RB
algorithm [2] is only based on network bandwidth or buffer us-
age e.g., BOLA algorithm [3], [4], or a combination of the two
schemes (e.g., robustMPC [5], Oboe [6], Bayesian-MPC [7]).
These methods require careful adjustment and are unable to
adapt to different network bandwidths or different QoE ob-
jectives. State-of-the-art MPC algorithm [5] uses future video
chunks by dynamically optimizing QoE metrics, which has bet-
ter performance than the simple ﬁxed schemes e.g., BOLA,
RB. However, MPC relies on accurate network bandwidth pre-
dictions, especially on future networks. Due to the variability
of network bandwidth, MPC is difﬁcult to predict accurately,
but inaccurate predictions may cause future video freezes and
low-quality video etc. Additionally, since BOLA and MPC can-
not adjust parameters according to speciﬁc network conditions
and are too sensitive to parameters, then Oboe [6] is proposed to
automatically adjust parameters, which can enhance QoE value
in speciﬁc scenarios.
Recently, Pensieve [8] was proposed to further improve QoE
by using RL to train a neural network to generate ABR algo-
rithms, which effectively solves the limitations of existing ABR
algorithms. Alternatively, PPO-based policy optimization can be
utilized to learn more efﬁcient ABR strategies [9], [10]. How-
ever, due to the randomness of network bandwidth, RL-based
methods are difﬁcult to converge quickly or generate a large
amount of gradient variance [52]. Imitation learning [11], [12]
is used for solving MPC problems, but the method is only appli-
cable to known environments and cannot be used for complex
network scenarios. Fugu [13] combines classical control with
a learned network predictor, trained with supervised learning
in situ on data from the real deployment environment. Addi-
tionally, ABRL [14] converts ABR policy into a linear model
for better comprehension and safety, allowing human engineers
to verify it while slightly increasing the average stall rate by
0.8%. Another approach is to employ meta-RL techniques like
MAML [15], [16], [17] or Pearl [18] to adaptive to various
network conditions. Moreover, Genet [19] introduces increas-
ingly challenging environments through a curriculum learning
1520-9210 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and similar technologies.
Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 2

```text
8186
IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025
strategy [20], enabling RL models to perform better across a
wider range of network environments. However, this method
fails to effectively learn from large volumes of ofﬂine data as
well as adapt to the complexity of video streams. Zuo et al. [21]
introduce Ruyi, an off-policy RL-based video streaming system
that integrates preference awareness into the QoE model and
the ABR algorithm [22], [23]. It is optimized with a modiﬁed
Deep Q-learning algorithm using experience replay [24]. Each
scheme can be used in a speciﬁc environment, but cannot effec-
tively learn and be generalized to diverse network environments
or bitrate decisions. This is because online learning of ABR al-
gorithms does not explore safely and cannot effectively learn
from these complex network features [25], [26].
Speciﬁcally,inreal-worldadaptivevideostreamingscenarios,
learning algorithms rely on speciﬁc data or environments to train
them. However, Internet data is often vast and massive, and ABR
algorithms adapt to new scenarios by learning from these net-
work characteristics. Because network conditions continually
change over time, and due to different user preferences, ABR
algorithms must balance various QoE metrics, such as improv-
ing video quality and reducing rebuffering time. Unfortunately,
learning algorithms often perform well on the simple training
and testing datasets, but real internet data features are complex
and variable, exhibiting heavy-tailed characteristics. Even with
in situ learning, adapting to real-world environments quickly
proves to be challenging. Therefore, learning network control
algorithms from these extensive and representative Internet data
and generalizing to novel scenarios is beyond the capabilities of
off-the-shelf methods [19], [27], [28]. This work will answer:
How to design a learning-based ABR algorithm that performs
robustly in the wild Internet.
To address these challenges and make RL more practical, we
propose Ofﬂine RL-based ABR algorithm (Fortuna), which is
capable of autonomously and efﬁciently learning ABR strate-
gies in the face of the variability and heavy-tailed nature of
heterogeneous network. Fortuna is primarily divided into two
stages. In the ofﬂine phase, it leverages domain knowledge to
ﬁrst learn from expert data, and then collects runs of RL data. In
the online phase, optimization takes place, gradually increasing
the complexity of the video stream through curriculum learn-
ing [20], [29]. However, ofﬂine ABR strategies cannot adapt
to new network conditions. To enhance the generalization of
Fortuna, we employ meta-learning for continuous optimization.
Furthermore, ABR algorithms interact with TCP congestion
control mechanisms, such as congestion window (CWND) and
round-trip time (RTT). To better understand the underlying net-
work behavior features, we consider TCP congestion control to
facilitate the effective learning of ABR algorithms. To success-
fully and efﬁciently develop high-quality ABR strategies, we
are driven to explore new data efﬁciency [30] approaches and
innovative RL techniques.
In summary, the main contributions of this paper are the fol-
lowing.
1) We analyze the issues present in the current heterogeneous
networkandproposeFortuna,amorepracticalofﬂinemeta
RL-based ABR method.
Fig. 1.
The principle of HTTP-based dynamic adaptive video streaming.
2) A novel RL technique uses curriculum learning to handle
unbounded video streaming sessions.
3) To better learn the underlying network behavior features,
considering that ABR algorithms interact with underly-
ing TCP congestion control, learning these features can
further reduce rebuffering and optimize QoE.
4) We evaluate QoE metrics in trace-driven and real-world
environments, and generalize to 3G, 4G, 5G, WiFi, syn-
theticnetworks,anddifferentvideostreams(SectionV-C),
and deploy the algorithms in streaming media systems
(Section VI).
II. BACKGROUND AND MOTIVATION
The HTTP-based ABR algorithm dynamically selects the ap-
propriate bitrate for video segments by monitoring network
bandwidth and player buffer status in real-time. It delivers
high-quality video when network conditions are good and low-
ers the quality during poorer conditions to prevent buffering,
thus optimizing the user QoE in Fig. 1. However, due to lim-
ited network bandwidth, ABR algorithms may not always re-
quest the optimal bitrate. Considering the diversity of the Puffer
dataset [13], we visualize it in Fig. 2, comprising 10427 streams,
1258 stream-hours, and analyze the data characteristics of these
real network users to illustrate why off-the-shelf ABR algo-
rithms have difﬁculty in adapting to these conditions.
Case 1: Network conditions ﬂuctuate over time, and long-
duration video streams exhibit a heavy-tailed distribution. Ini-
tial Low Load Phase (0 - 5,000 seconds), where bandwidth ﬂuc-
tuates at relatively low levels, mostly below 100 Mbps, with
frequent dips close to zero. This is followed by the Increased
Fluctuation Phase (5,000-10,000 seconds), during which band-
width varies between 0 and 200 Mbps, showing more frequent
peaks and troughs. Next, in the High Fluctuation Phase (10,000-
20,000 seconds), the range of bandwidth ﬂuctuation broadens,
often reaching up to 200 Mbps and occasionally exceeding
300 Mbps. Then comes the Peak Phase (around 20,000-22,000
seconds), where bandwidth surges to its highest levels, exceed-
ing 400 Mbps within a short period. Finally, in the Decline and
Stabilization Phase (22,000-28,000 seconds), bandwidth grad-
ually decreases and stabilizes, with most values falling below
100 Mbps. These data usually contain samples from various
scenarios, environments, or states, which can effectively reﬂect
the diversity of data distributions. By training on diverse data,
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 3

```text
YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS
8187
Fig. 2.
Visualize network features, as well as video quality and buffering time of existing ABR algorithms, on the Puffer dataset.
ofﬂine RL enables the model to learn the features and patterns
across different distributions, enhancing its generalization abil-
ity [31].
Case 2: The QoE of video users is inﬂuenced by the un-
derlying TCP congestion control protocol [32], such as RTT.
We observe varying network throughputs, ranging from 0 to
250 Mbps, with different RTT values across users. For example,
users with a throughput of 75 Mbps exhibit a wide range of RTT
values, while those with throughput between 25 and 50 Mbps of-
ten experience high latency and a broader range of RTT values.
These heterogeneous network characteristics signiﬁcantly im-
pact ABR algorithm decisions, affecting QoE outcomes. Since
RTT inﬂuences QoE, TCP congestion control algorithms like
BBR [33] and CUBIC [34] adjust data sending rates to opti-
mize RTT performance. ABR algorithms must adapt to chang-
ing network conditions to improve video streaming quality by
leveraging these underlying network characteristics.
Case 3: Learning ABR strategies often leads to poor deci-
sions when faced with unknown network conditions, resulting
in suboptimal video quality and increased rebuffering time. We
use the Puffer dataset, with a duration of 1000 hours and a time
interval of 1 s, where the network bandwidth ranges from 0 to
400 Mbps. We compared several ABR algorithms, including
Pensieve, Fugu, Comyco, BOLA, and MPC, in how well they
adapt to unseen network conditions. Due to the randomness of
network bandwidth, traditional methods like Pensieve struggle
to converge effectively. Fugu, which combines neural network
training with MPC predictions, also encounters challenges in
managing unknown network conditions. Fortuna is the most op-
timal among all ABR algorithms in improving video quality
(SSIM) and reducing stalling time. Our ﬁndings indicate that
existing methods struggle to respond effectively to these unpre-
dictable scenarios.
In summary, it is highly important to efﬁciently learn robust
ABR algorithms under wild Internet conditions and generalize
them to diverse network conditions.
III. DEFINE OFFLINE META ABR ALGORITHM
Ofﬂine-RL is conducting online learning of the optimal policy
π∗from prior data D (i.e., off-policy data, expert demos, prior
runs of RL). At time t, the agent observes the current state st (i.e.,
throughtput Ct, the buffer size Bt, chunk bitrate Rn), and selects
an action at (i.e., chunk bitrate Rn) according to its policy. The
video client then receives the action at and transitions to a new
state st+1, providing the agent with a reward rt. The goal of
the ABR agent is to learn a policy that maximizes the expected
cumulative discounted reward value E[∞
t=0 γtrt]. The entire
process follows a Markov decision process (MDP), denoted by
M = (S, A, O, P, R),whereS isthestatespace,Aistheaction
space, O is the observation space, P is the transition probability
function, and R is the reward function.
Reward rt: The environment evaluates different actions at, re-
ﬂects the quality of at, and improves the policy πθ. rt reﬂects the
quality of different bitrates, rebuffering time and video switch-
ing frequency. We adopt the QoE metric provided by MPC [5]
QoEN =
N

n=1
q (Rn) −μ1
N−1
n=1 |q (Rn+1) −q (Rn)|
−μ2
N

n=1
Tn
(1)
A video consists of N chunks, q(.) represents video quality,
such as SSIM [35] or VMAF [36], where μ1 and μ2 are the
non-negative weight coefﬁcients corresponding to video quality
switching frequency and rebuffering time.
Meta-ABR Task: In meta-RL, tasks M are drawn from a dis-
tribution p(M), representing the diversity of network condi-
tions [15]. The meta-ABR algorithm aims to ﬁnd a shared set
of parameters θ that maximizes the expected cumulative reward
across all tasks:
θ∗= arg max
θ
n

i=1
Eπψi(τ)[R(τ)], where ψi = fθ(Mi).
In this formulation:
r ψi is the task-speciﬁc policy parameter derived from the
meta-parameter θ, adapting to task i.
r fθ denotes the meta-policy function that leverages experi-
ence across tasks to optimize future performance.
r Mi represents the MDP for each task, encoding its unique
network environment.
The goal of meta-ABR is to train a meta-policy that
quickly adapts to unseen network conditions, leveraging
knowledge gained from previously encountered environments,
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 4

```text
8188
IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025
thereby optimizing the QoE objective across a variety of
tasks.
Advantage-Weighted Regression (AWR): AWR is an ofﬂine
RL method that reﬁnes the policy based on historical data [37].
Its objective function is:
LAW R(θ, φ, D) =
Es,a∼D

−
1
Z(s) log πθ(a|s) exp (QD(s, a) −Vφ(s))

(2)
where:
r QD(s, a) is the return from the dataset for action a in state
s.
r Vφ(s) is the value function for the behavior policy.
r Z(s) > 0 is a normalization function dependent on the
state s, scaling the overall loss term.
The term QD(s, a) −Vφ(s) represents the advantage of an
action a. The policy objective LAW R can be seen as a weighted
regression problem, where actions with higher advantages re-
ceive greater weight.
IV. DESIGN
In this section, based on ofﬂine RL theory, we describe how to
efﬁciently learn a robust ABR algorithm. We then utilize meta-
learningtolearnmeta-ABRpoliciestoadapttodifferentnetwork
conditions.
A. Addressing Data Efﬁciency Issues in RL.
Academia and industry are actively researching neural net-
work efﬁciency [31], [38], [39]. In traditional deep RL with
real-time online interactions like Pensieve, it often takes around
50,000 iterations and 4 hours to converge [8]. However, when ap-
plying this to real-world environments, like learning in situ [13],
convergence could take up to 2 years. This highlights the prac-
tical challenges of neural network training, particularly for real-
world applications.
In practice, RL-based ABR algorithms need to quickly learn
the optimal policy π∗and generalize across various types of net-
work conditions, i.e., learn the optimal policy π∗from prior data
D = (si, ai, si+1, ri). One of the simplest methods for applying
RL is to use prior data D, such as pre-trained policies from imita-
tion learning (e.g., Comyco [11]), and then reﬁne them through
RL [40], [41]. However, this approach has two limitations:
(1) the prior data may not be optimal, and (2) ﬁne-tuning the
policy lacks data efﬁciency as it cannot make efﬁcient use of
prior data during RL [37]. In real-world environment, data efﬁ-
ciency is of paramount importance. Therefore, we demand that
the algorithm be capable of reusing any non-policy data (e.g.,
off-policy data, expert demos, prior runs of RL) during online
RL to achieve highly data-efﬁcient ﬁne-tuning.
In the early stages, we needed to learn from expert-
demonstrated data D. The state-of-the-art method, MPC [5], de-
termines video bitrate by solving an optimization problem aimed
at maximizing QoE based on the dynamic playback buffer, con-
sidering several future video chunks. By directly optimizing the
video QoE objective, MPC typically performs better than tradi-
tional methods that rely on ﬁxed heuristics. Therefore, we use
the MPC algorithm to collect expert demonstration data in order
to reduce the need for online interaction between RL and the
video streaming environment.
B. Handling Unbounded Video Streaming Sessions With
Curriculum Learning
We will construct a strategy for gradually increasing video
stream length from a mathematical perspective and combine it
with the decaying process of environmental resets, observing
how these two factors work together to optimize the training
process.
Let the video stream length be denoted as Tk, where k rep-
resents the training stage. Starting from the initial stage k = 1,
the video stream length gradually increases as the training pro-
gresses.
We can describe the gradual increase of video stream length
using the following mathematical formula:
Tk = min (Tinit + ΔT · (k −1), Tmax)
Where:
r Tinit is the initial video stream length.
r ΔT is the increase in video stream length for each stage.
r k is the current training stage (k = 1, 2, 3, . . . ).
r Tmax is the maximum video stream length, representing the
task’s maximum complexity.
This approach ensures that the video stream length increases
gradually and does not exceed the maximum value Tmax, pre-
venting the task from becoming too complex.
Example: Suppose the video stream length starts at 10 seconds
(Tinit = 10) during the early stages of training, with an increase
of 5 seconds at each stage (ΔT = 5), and the maximum video
stream length is 50 seconds (Tmax = 50). Then, during the ﬁrst,
second, and third stages of training, the video stream lengths
will be 10 seconds, 15 seconds, and 20 seconds, respectively.
When training reaches the maximum length (the 9th stage), the
video stream length will be 50 seconds.
To learn a robust ABR strategy effectively, the agent needs
to undergo training in “streaming” scenarios where the video
streaming session continuously arrive over time. Training in
“batch” scenarios, where video streaming sessions arrive simul-
taneously at the beginning of an episode, leads to inefﬁcient
strategies in a “streaming” environment, such as different ran-
dom seeds. However, training with a continuous ﬂow of video
stream arrivals presents challenges. The agent’s initial strategy
is poor, mainly because the initial parameters are random. Con-
sequently, during early training episodes, the agent struggles
to process video stream as they arrive, resulting in a signiﬁ-
cant video stream queue buildup. Additionally, when the agent’s
strategy is not optimal, video requests may experience delays,
resulting in a queue before being serviced rather than receiving
immediate satisfaction.
In order to avoid spending a signiﬁcant amount of train-
ing time exploring actions that do not improve the policy in
this scenario, we prematurely terminate the initial episodes so
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 5

```text
YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS
8189
Fig. 3.
The policy architecture of Fortuna is used to generate the ABR algo-
rithm, solid lines show the data ﬂow during the forward pass, while dashed lines
represent the gradient ﬂow during the backward pass, which occurs only during
the adaptation phase. The advantage head is not involved in the policy update
process of the outer loop.
that the agent can reset and quickly retry from an idle state.
We gradually increase the length of video streaming sessions
throughout the entire training process. Thus, initially, the agent
learns to short video streaming sessions sequences. As its ABR
strategy improves, we extend the episode length, making the
problem more challenging. The concept of gradually increas-
ing video stream sequence length—and, consequently, prob-
lem complexity—during training realizes curriculum learning
for ABR [29].
C. Learning meta-ABR Algorithm
Fortuna is an ofﬂine meta-RL ABR algorithm that learns ini-
tializations φ and θ for a value function Vφ and meta policy πθ,
respectively, enabling rapid adaptation to a new network condi-
tion encountered at meta-test time via gradient descent. Fortuna
mainly consists of inner loops and outer loops [15], [42]. Next,
we will provide a detailed overview of the implementation pro-
cess.
Fortuna uses the RL Actor-Critic (policy and value network)
approach in Fig. 3. The training process is as follows:
Step 1: Input is the state st, which includes 7 variables,
namely: throughtput Ct, chunk download time dk(Rk)/Ck, next
chunk sizes Rn+1, RTT, and the buffer size Bt, remaining
chunks N and chunk bitrate Rn.
Neural networks: The number of hidden layers is 1, and 128
convolution kernels and a fully connected network are used for
feature extraction. The size of the convolution kernel is 4 and
the step size is 1.
Step 2: When receiving the state st, the agent selects the cor-
responding action at based on the meta-policy πθ, and the prob-
ability distribution is deﬁned as : (st, at) →[0, 1], (st, at) is the
probability that the action at may take in state st.
Step 3: After taking each action at, the environment feeds
back the reward rt corresponding to at to the agent, and the goal
is to obtain the maximum cumulative reward from the environ-
ment. Therefore, the reward rt is set according to the parameters
of the QoE metric, reﬂecting the individual components of the
QoE metric.
Step 4: The actor’s output bitrate poses challenges, primarily
because different videos can be encoded at various bitrate levels,
and due to variable bitrate encoding, their chunk sizes may also
differ. To address this diversity, the typical approach would in-
volve training a model for every possible combination of video
bitrates, which is not a scalable solution.
Output masking is employed as part of the solution. For each
video, a mask, represented as a binary vector [m1, m2, . . ., mk],
is used to constrain the probability distribution of the output,
including only the bitrate levels that the video supports. This
mask, in conjunction with softmax [43], determines which bi-
trates [i1, i2, . . ., ik] in the NN output are valid.
Inner-Loop: The inner loop refers to real-time bitrate selec-
tion adjustments based on the current network conditions and
the existing strategy, aiming to optimize the short-term user ex-
perience. For ABR algorithms, the inner loop uses bandwidth
predictions, buffer status, and chunk sizes to select an appropri-
ate bitrate that maximizes QoE objectives.
The value function loss, dependent on the meta-training data
Dtr
i , representing the i-th batch of ofﬂine data. In the ABR algo-
rithm, the value function Vφ(s) estimates the long-term return
or value of a state s. In this step, the goal is to update φ by mini-
mizing the value function loss LV , which makes Vφ(s) a closer
approximation to the action-value function QD(s, a).
φ′ ←φ −η1∇φLV (φ; Dtr
i )
(3)
where LV (φ; D) = Es,a∼D[(Vφ(s) −QD(s, a))2] and QD(s, a)
is the Monte Carlo return from state s taking action a observed
in D. By minimizing the loss, we aim to accurately predict the
expected reward for each bitrate choice in a given state.
To effectively learn features from the changing network con-
ditions, our policy architecture has two output heads: one for
predicting the action given the state, πθ(·|s), and another for
predicting the advantage given both state and action, Aθ(s, a)
[44]. This dual-head design helps reduce variance in the learn-
ing process, leading to more stable and efﬁcient training. Policy
adaptation proceeds as:
θ′ ←θ−α1∇θLπ(θ; φ′, Dtr
i ), where Lπ =LAW R+λLADV
(4)
where λ is the weight of the normalization Z(s) of the advantage
function, designed to better adapt to different network condi-
tions. The AWR loss is given in (2), and the advantage regression
loss LADV is given by:
LADV (θ; φ′, D) = Es,a∼D

Aθ(s, a) −QD(s, a) + Vφ′
i(s)
2
(5)
This loss function aims to optimize the advantage function
Aθ(s, a), ensuring that the policy selects bitrates that lead to
higher expected rewards. By minimizing the difference between
Aθ(s, a), QD(s, a), and Vφ′
i(s), the algorithm ensures that the
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 6

```text
8190
IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025
policy is consistent with both the value and action-value func-
tions. This helps improve the policy’s ability to adapt video bi-
trate to varying network conditions, such as bandwidth ﬂuctua-
tions, to select the optimal bitrate.
Outer-Loop: The outer loop focuses on globally optimizing
the initial strategy across multiple different network environ-
ments (tasks) M, aiming to enhance the generalization ability
of the strategy for unseen network ﬂuctuations.
For the outer loop update, we sample a distinct batch of data,
meta-test Dts
i , to promote few-shot generalization instead of
memorizing the adaptation data.
The meta-learning for the value function follows the MAML
approach and employs the supervised Monte Carlo objective:
min
φ EMi[LV (φ′
i, Dts
i )]
= min
φ EMi[LV (φ −η1∇φLV (φ, Dtr
i ), Dts
i )] (6)
This objective optimizes for a set of initial value function pa-
rameters such that one or a few inner gradient steps lead to an
accurate value estimator.
Unlike the inner loop, we optimize the initial policy param-
eters in the outer loop using a standard advantage-weighted re-
gression objective since expressiveness concerns mainly apply
to the inner loop with fewer gradient steps.
min
θ
EMi[LAW R(θ′, φ′, Dts
i )]
= min
θ
EMi[LAW R(θ −α1∇θLπ(θ, φ′
i, Dtr
i ), φ0, Dts
i )] (7)
where Lπ is deﬁned in (4) and LAW R is deﬁned in (2).
Weight Transform Layers z: The standard fully connected
layer has the output:
y = σ(Wx + b),
where W ∈Rd×d is the weight matrix, b ∈Rd is the bias vector,
x ∈Rd is the input vector, and σ is the activation function.
By introducing a latent vector z ∈Rc and a weight transfor-
mation matrix Wwt ∈R(d2+d)×c, dynamic weights and biases
are generated:
w = Wwtz,
where the ﬁrst d2 components of w reshape into the weight
matrix W ∗∈Rd×d, and the last d components form the bias
vector b∗∈Rd:
W ∗= reshape(w[0 : d2]),
b∗= w[d2 : (d2 + d)].
The forward pass becomes:
y = σ(W ∗x + b∗).
Unlike ﬁxed weights in standard layers, dynamic generation of
W ∗and b∗allows more ﬂexible updates. Traditional gradient
descent updates result in rank-1 changes, whereas with the latent
vector z, the rank of weight updates is bounded by:
rank(ΔW ∗) ≤min(d, c),
allowing higher-rank transformations and richer adaptation
strategies.
Algorithm 1: Learning meta-ABR policies through ofﬂine
RL with gradually increasing video stream length
1: Require: network environments {Mi}; ofﬂine datasets
Di containing trajectories τ: (st, at, rt)
2: Require: Initial video stream length Tinit, increment
ΔT, maximum stream length Tmax
3: Hyperparameters: Inner-loop learning rates α1
(policy), η1 (value); outer-loop learning rates α2, η2;
training iterations k
4: Initialize meta-policy parameters θ and value function
parameters φ
5: for k iterations do
6:
for each network environment Mi do
7:
Sample disjoint meta-training and meta-test data
batches Dtr
i and Dts
i from Di
8:
Calculate video stream length for the current stage:
Tk = min(Tinit + ΔT · (k −1), Tmax)
9:
Adapt value function: φ′ ←φ −η1∇φLV (φ; Dtr
i )
10:
Adapt policy: θ′ ←θ −α1∇θLπ(θ; φ′; Dtr
i ), where
Lπ = LAW R + λLADV
11:
end for
12:
Meta-update value function:
φ ←φ −η2

i ∇φLV (φ′; Dts
i )
13:
Meta-update policy:
θ ←θ −α2

i ∇θLAW R(θ′; φ′; Dts
i )
14: end for
Algorithm 2: Generalizing meta-ABR policies across di-
verse environments
1: Input: Test network environment Mj, ofﬂine
experience buffer D, meta-policy πθ, and meta-value
function Vφ
2: Hyperparameters: Learning rates α1, η1; number of
adaptation steps k
3: Initialize policy parameters θ0 = θ and value function
parameters φ0 = φ
4: for k adaptation steps do
5:
Adapt value function: φt+1 ←φt −η1∇φLV (φt; D)
6:
Adapt policy: θt+1 ←θt −α1∇θLπ(θt; φt+1; D)
7: end for
In summary, the latent vector z enhances ABR algorithms
by enabling dynamic weight and bias generation, supporting
higher-rank weight updates, and improving adaptability to vary-
ing network conditions, leading to more ﬂexible and scalable
performance optimization in video streaming. More mathemat-
ical proofs can be found in [45].
Algorithm 1 and 2 demonstrate how to learn meta-ABR poli-
cies through ofﬂine RL and generalize them to various video
streaming environments.
V. EXPERIMENTS AND ANALYSIS
In this section, we experimentally evaluate Fortuna on dif-
ferent network traces and QoE metrics. Further, we analyze the
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 7

```text
YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS
8191
performance of Fortuna on the 5G network, as well as the train-
ing situation.
A. Implementation
NVIDIA RTX A6000 GPU and a CPU with 128 cores, 128 G
RAM, 64-bit Ubuntu 20.04, and MacOS operating system were
selected as the experimental platform, and development tools
such as Python3.5, Torch1.6, Apache2, Google Chrome, and
FFmpeg. We use Mahimahi [46] to simulate network conditions,
with RTT ranging from 0 to 80 ms, based on collected network
traces between the client and server.
The QoE metric parameters of (1) are set: N is 8, μ1 is 4.3,
and μ2 is 1. During the training process, the size of each epoch
is 100, γ = 0.99, Relu activation function [47] and the Adam
optimizer [48] are used. During the whole experiment, according
to the change of the loss function, the learning rates for the
inner and outer loops are 0.001 and 0.0001, respectively, and
the reward value fed back to the agent by the environment is
the QoE metric value.
Network Traces: To evaluate Fortuna and existing ABR al-
gorithms on different networks, we use FCC [49], HSDPA [50]
and Belgium/4G [51] public network traces, and the dataset fea-
tures are as follows. The FCC dataset contains 1 million net-
work traces with an average network throughput of 2100 sec-
onds each trace, granularity of 5 s, and a throughput range of
0-111Mbit/s, generated on trains, buses, cars etc. The HSDPA
dataset : the granularity of user generation in subways, trams,
trains, buses and ferries is 1 s, the number of traces is 86, and the
throughput range is 0-3Mbit/s. Belgium/4G dataset: generated
in static, pedestrian, car, bus, and train movement modes etc.,
granularity of 1 s, 5 hours in total, 40 traces, throughput range
of 0-111Mbit/s.
We used the Puffer dataset [13], which in 2020 had over
63,508 video users and streamed a total of 38.6 years of video
content in that year. Now, in 2024, the number of video users
and streams has grown even further. Network bandwidth ranges
from 0 to 500 Mbps, with an interval of 1 s. These networks
display variable characteristics with heavy-tailed distributions.
For this study, we selected 4 different datasets. We used 80% of
the data for training and 20% as test data.
B. Evaluation
Network datasets: FCC, HSDPA, and Belgium/4G; video: di-
vided into 48 video chunks, each chunk has approximately 4
seconds, the total duration is 193 seconds; H.264/MPEG-4 en-
coding: {300, 750, 1200, 1850, 2850, 4300} kbps; video player:
Google Chrome (built-in DASH.js), playback buffer capacity
is set to 60 seconds, all ABR algorithms run in dash.js; video
server: Apache2, video is deployed on the server.
ABR algorithms: We compare Fortuna with state-of-art ABR
algorithms.
BOLA [3]: optimizing buffer occupancy using Lyapunov al-
gorithm. Since the playback buffer is relatively stable, it can
effectively improve QoE.
Pensieve [8]: ABR algorithm based on deep reinforcement
learning (DRL), generating ABR algorithm by training neural
network. However, the original Pensieve struggled with conver-
gence due to the variability in network conditions when using
the A3C algorithm. Therefore, we employed variance reduction
techniques [52] in the training process to develop a more effec-
tive ABR algorithm.
RMPC: makes decisions about video bitrate by tackling a
problem that aims to maximize QoE for several upcoming
chunks. By focusing directly on improving QoE, MPC often
performs better than methods that rely on ﬁxed rules [5].
Comyco [11]: The imitation MPC algorithm [5] uses neural
networks to generate the ABR algorithm.
Fugu [13]: Train the neural network using supervised learn-
ing, and then use MPC [5] for video bitrate decision-making.
CDFs: Cumulative distribution functions (CDFs) are used to
evaluate the overall distribution of QoE for different ABR algo-
rithms. The higher the CDF to the right, the higher the cumu-
lative probability and QoE. As shown in Fig. 4, Fortuna has a
higher QoE value than the existing ABR algorithms, due to the
characteristics of the autonomous learning robust ABR policies,
improvement range of 8.5%-31.9%. The reason is that Fortuna
can better learn a wide range of network features, resulting in
strong generalization on unseen networks. Fugu and Comyco’s
inability to adaptively change strategies and long-term decision
problems using imitative learning. Additionly, it is essentially
solving the RMPC problems [5]. However, RMPC estimates the
network bandwidth too conservatively use model control. For
example, when the network throughput becomes low, it should
make full use of the playback buffer and request a low bitrate to
improve QoE, but RMPC leads to insufﬁcient buffer utilization;
similarly, BOLA only considers the buffer usage. As shown,
these simple ﬁxed heuristics are not applicable to complex net-
work throughput. Additionally, Pensieve cannot adaptively learn
network characteristics, resulting in inaccurate predictions un-
der certain network conditions.
QoE breakdown: To better understand the performance of
Fortuna, we compare the individual components of QoE metric.
Fig. 5 shows the video bitrate, rebuffering time and smoothing
penalty, i.e., the components of QoE metric. Experimental re-
sults are evaluated on FCC, Belgium/4G, and HSDPA datasets.
As shown, Fortuna is able to better limit rebuffering through
different networks to achieve higher QoE values. rebuffering
time is reduced by 4.6%-14.2% on FCC, Belgium/4G, and HS-
DPA datasets by building enough buffers to handle sudden net-
work ﬂuctuations. In addition, although Fortuna cannot outper-
form existing solutions in every QoE metric. Instead, it is able to
maximize QoE by optimizing every metric. For example, when
network bandwidth is insufﬁcient, Fortuna uses a low bitrate to
compensate for the low bandwidth and reduce video stalling.
Video user preferences: This section provides a comparison
of three common QoE models, highlighting their key character-
istics.
1) Linear QoE: Advantages: Simple and intuitive, suitable
for scenarios prioritizing higher bitrates. Limitations: Ig-
nores diminishing returns of quality perception and is
sensitive to bitrate ﬂuctuations. Application: Suitable for
high-bandwidth video streaming environments.
2) Logarithmic QoE: QoE models user perception with
diminishing
returns
using
q(R) = log(R/Rmin).
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 8

```text
8192
IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025
Fig. 4.
Compare the QoE metrics of Fortuna and existing ABR algorithms on FCC, HSDPA/3G, and Belgium/4G networks. Examine the distribution of average
QoE values for each ABR algorithm.
Fig. 5.
Comparing the QoE metric individual compoments of Fortuna and existing ABR algorithms on FCC, HSDPA, and Belgium/4G networks. Error bars are
drawn to represent the mean value with a margin of one standard deviation.
Fig. 6.
Comparison of Fortuna with existing ABR algorithms on FCC and HSDPA networks. QoE metrics are considered as listed in Table I, with results
normalized against the performance of Fortuna. Error bars represent ± one standard deviation.
Advantages:
Reﬂects
realistic
user
perception
and
balances quality with smoothness. Limitations: Requires
careful selection of Rmin; more complex than linear
QoE. Application: Ideal for adaptive bitrate streaming in
constrained bandwidth conditions.
3) High-Deﬁnition QoE: Uses predeﬁned quality levels
corresponding to bitrate ranges. Advantages: Simple
computations by mapping bitrates to ﬁxed quality lev-
els. Limitations: Quality changes are discontinuous and
threshold-dependent. Application: Suitable for video ap-
plications with standard resolution transitions, such as
Standard Deﬁnition (SD), High Deﬁnition (HD), or Ultra-
High Deﬁnition (UHD).
The experimental results are shown in Fig. 6, For-
tuna leverages ofﬂine meta-learning to pre-train adaptive
ABR strategies tailored to various QoE objectives. Un-
like traditional ABR algorithms with ﬁxed control laws or
Pensieve’s online learning approach, Fortuna’s pre-trained
model can rapidly adapt to QoElog, QoElin, and QoEhd
scenarios:
TABLE I
QOE MODELS AND THEIR CORRESPONDING PARAMETERS
r For QoElog, Fortuna minimizes rebuffering risk by prior-
itizing bitrate stability while avoiding unnecessary high-
bitrate jumps.
r For QoElin, it aggressively increases bitrate to maxi-
mize user-perceived quality without sacriﬁcing playback
smoothness.
r In QoEhd optimization, Fortuna employs foresight to
rapidly build buffer with low bitrates and switches directly
to HD quality once buffer conditions are favorable, all
without online tuning.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 9

```text
YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS
8193
Fig. 7.
The overall probability distribution of 4G and 5G network traces.
By eliminating online exploration and relying on pre-trained
policies, Fortuna consistently delivers high performance across
changing conditions, surpassing the adaptability and efﬁciency
of Pensieve.
C. Generalization
In Section V-B, Fortuna is tested using common network
traces, which have relatively short durations. In practice, how-
ever, Fortuna may encounter new network bandwidths, bitrates
and require different optimal ABR strategies. To evaluate the
generalization ability of Fortuna to the new network, we con-
duct 2 sets of experiments. First, Fortuna is evaluated on the real
5G network traces, and analyse the differences with 4G network.
Second, we take the generalisation of Fortuna to the extreme,
i.e. training purely with synthetic networks and generalising to
real Belgium/4G and comparing with Genet [19].
5G and 4G network traces: To analyze the distribution of
5G network versus 4G network, we performed network traces
analysis using the CDF distribution map. As shown in Fig. 7, 5G
network is able to support higher network bandwidth in the range
of 0-1800 Mbps, and 4G is 0-300 Mbps. Second, 5G network
are capable of supporting high network, which means we need
corresponding bitrates to match.
Different from the previous bitrate setting (e.g., 2.85 Mbps,
4.3 Mbps that can only support 3G and 4G network). However,
5G networks [53] (i.e., including 4G and 5G, there are 175 4G
and 121 5G network traces with a granularity of 1 s, 2 types:
driving and walking) can support higher bitrate videos, in order
to match the corresponding network throughput with the video
bitrate, to prevent high throughput from always meeting high
and low bitrates. Inspired by literature [54], experiment bitrate
settings, namely: (20, 40, 60, 80, 110, 160) Mbps, bitrate map
reward=[1, 2, 3, 12, 15, 20], (more detail in [55]), total video
chunks is 157, rebuf-penalty is 160, smooth-penalty is 1. Wild
ﬂuctuations can bring great challenges to the ABR algorithms,
howtobalancecomponents of thevideobitrateandthestall time,
thereby the ABR decision should be forward-looking enough to
maximize QoE objectives and minimize stall time as much as
possible.
As shown in Fig. 8, Fortuna can achieve better performance
on 4G and 5G networks, the stall time is reduced by 4.6%-12.2%
and 0.5%-3.1% respectively. As shown, fortuna and ofﬂine-
Fortuna can achieve better performance on 4G and 5G networks.
However, Fugu [13] (supervised learning) cannot be adapted
to different networks, as it requires speciﬁc data that cannot
be adapted to new networks, and BOLA fail to achieve good
performance using simple ﬁxed heuristics. Furthermore, RMPC
algorithm performs poorly on 5G networks due to overly con-
servative predictions. However, in these heterogeneous network
data, the environment is more complex and requires better ABR
decisions. In contrast, RL can adaptively select the optimal bi-
trates based on the network scenario. These experiments show
that Fortuna can reduce stall time and maximize QoE even in
the case of high and ﬂuctuating network traces, despite these
networks have never encountered.
Training with synthetic dataset: The training dataset has a
signiﬁcant impact on the performance of RL-based algorithms
and may hinder the optimal ABR strategy for RL learning. In
part, we take Fortuna to the extreme and train it purely using
synthetic networks and generalize it to the real network.
The simulated dataset utilized in the study encompasses a
diverse range of network bandwidths, with the average through-
put spanning from 0.2 Mbps to 4.3 Mbps, which aligns with
the training video bitrates (such as H.264 encoding at 300 kbps,
750 kbps, 4300 kbps, etc.). The dataset’s transitions between
states were generated using Markov modeling, and the resulting
bandwidth values follow a Gaussian distribution with a granu-
larity of 1 s and a uniform variance ranging from 0.05 to 0.5 [8].
We ﬁnd that Fortuna performs better on each CDF trajectory
compared to Genet [19] in Fig. 9, average QoE value increased
by12.5%. The advantage of Fortuna lies in its ability to opti-
mize based on a comprehensive set of historical data and com-
plex network environments. In contrast, ABR algorithms gener-
ated through curriculum learning might face limitations due to
constraints in the data and training strategies used during their
development.
Multiple videos: To evaluate Fortuna’s ability to gener-
alize across varying video properties, we trained a sin-
gle ABR model using 1,000 synthetic videos with diverse
characteristics. Each video had a random number of bi-
trate options, ranging from 3 to 10, with values chosen
from {200, 300, 450, 750, 1200, 1850, 2350, 2850, 3500, 4300}
kbps. Videos were segmented into a random number of chunks,
between 20 and 100, and chunk sizes were varied by applying
Gaussian noise to a standard 4-second chunk duration. This ap-
proach ensured a broad range of video properties, including bi-
trate options, chunk count, chunk sizes, and overall duration, to
rigorously test the model’s adaptability and performance across
different scenarios.
As shown in Fig. 10, the results demonstrated that the gen-
eralized ABR algorithm achieved nearly identical performance
compared to a model exclusively trained on a reference video,
The gap in QoE values is 2.8%. This ﬁnding suggests that our
method’s server conﬁguration could effectively elevate stream-
ing quality across a spectrum of videos, employing a concise
selection of ABR algorithms.
D. Comparing State-of-The-Art RL Algorithms
To compare the training efﬁciency of existing RL algo-
rithms, we compare several ABR algorithms, i.e., Pensieve [8],
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 10

```text
8194
IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025
Fig. 8.
Compare the average bitrate and rebuffering time of Fortuna with existing ABR algorithms, using 95% conﬁdence intervals.
Fig. 9.
Comparing the QoE metrics of Fortuna and Genet ABR algorithms on
Belgium/4G dataset.
Fig. 10.
Comparing ABR algorithms trained on a diverse set of videos with
those speciﬁcally trained on the test video under varying network conditions.
Variance reduction [52], Jade, an RL-based ABR algorithm with
human feedback (learning the ABR algorithm using Duel-PPO
and adaptive entropy RL techniques [56], [57]), PEARL [58],
[59], a contextualized meta-RL approach (i.e., recently used for
meta-RL to achieve better ABR policies performance [18]). Ten-
sorFlow TensorBoard was used to monitor the training process
during the experimental procedures. As shown in Fig. 11(a), the
original Pensieve was trained using A3C, due to the random na-
ture of network conditions, and the ﬂuctuations were very dras-
tic, thus we used Variance reduction to optimize training the per-
formance more stable. PEARL, a context-driven meta-learning
approach, tends to meta-overﬁtting, which leads to suboptimal
performance in unseen network conditions. Contrastingly, For-
tuna leverages ofﬂine data to rapidly learn meta-ABR policies,
resulting in an improvement of over 6.6%–20.1% the previous
performance.
Additionally, we also compared Fortuna with online meta-RL
methods, using PPO to optimize the ABR algorithm, as shown in
Fig. 12. We found that Fortuna can effectively utilize ofﬂine data
to converge quickly, achieving an average reward improvement
of 9%. In contrast, Meta-PPO (However, the ofﬁcial code has
not been released, and we have done our best to implement
the algorithm according to the pseudocode description in the
paper.) [60] converges more slowly due to the need for real-
time interaction with the ABR environment. Although the clip
function in the PPO algorithm mitigates policy ﬂuctuations, it
remains relatively stable.
Curriculum Learning: In this part, we utilize Curriculum
Learning to gradually increase the complexity of the video
stream in order to quickly adapt the bitrate to new network
conditions. We compared the training steps and time as shown
in Fig. 11(b) and (c), it can improve performance by more
than 7.5%-4×, the average QoE can be improved by 3.7%.
Speciﬁcally, it is divided into two steps. First, Reset Envi-
ronment: A higher reset probability in the initial stages al-
lows the agent to explore different strategies. Gradually re-
ducing this probability helps stabilize learning and focus on
long-term decision-making. Second, Gradual Increase of Video
Stream Length: The core idea is to gradually increase task
complexity. The agent transitions from handling simple, short
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 11

```text
YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS
8195
Fig. 11.
Comparison of training epochs and training time with and without curriculum learning by increasing the complexity of video streaming, i.e., from short
video streams to long video streams.
Fig. 12.
The comparison of Fortuna with the existing state-of-the-art meta-
ABR algorithm, Meta-PPO ABR [60].
video streams to more complex, longer video streams, en-
abling it to better cope with ﬂuctuating network environ-
ments and ensuring high-quality video streams under varying
conditions.
E. Deep Dive
In this section, we explore microbenchmarks tailored to
deepen our comprehension of Fortuna. Additionally, these
benchmarks shed light on practical concerns that emerge when
implementing ABR algorithms generated through RL, such as
the inﬂuence of TCP congestion control and the diverse video
streaming sessions.
TCP congestion control: In real internet conditions, the video
stream interacts with TCP congestion control. Simulated en-
vironments often fail to accurately replicate real network con-
gestion control. Therefore, we take into consideration under-
lying TCP network characteristics. These abundant data in-
sights can be beneﬁcial for learning robust ABR algorithms
across various network environments. Speciﬁcally, video play-
ers may not immediately request future video chunks after
completing the download of a video chunk, for instance, due
to a full playback buffer. This delay can trigger the under-
lying TCP connection to enter slow start mode, a behavior
Fig. 13.
Comparing how underlying TCP network characteristics affect QoE
in the Belgium network.
known as TCP slow start restart [61]. Slow start, in turn, hin-
ders the video player from fully utilizing the available band-
width, especially for small chunk sizes (low bitrates). This be-
havior makes simulation challenging as it fundamentally links
network throughput to the employed ABR algorithm. For in-
stance, strategies that rapidly ﬁll the buffer will experience
more instances of slow start, consequently reducing network
utilization.
Additionally, in the TCP congestion control process, we need
to control network bandwidth based on queue delay, which in-
volves subtracting the minimum RTT observed from the cur-
rent RTT and adjusting CWND (congestion window) based on
packet behavior. This element plays a vital role in ensuring high
throughput and minimal latency. Therefore, when network con-
gestion occurs, we should adjust the video bitrate based on TCP
congestion control to provide a better user experience. In other
words, bydynamicallymodifyingthevideobitrateinresponseto
the TCP congestion window and queue delay, we can maintain
an optimal balance between throughput and latency, ensuring
smooth video streaming even in ﬂuctuating network conditions.
To validate this behavior, we conducted 4 sets of experiments,
one solely considering network bandwidth for selecting the bi-
trate, while the other took TCP congestion control into account.
As shown in Fig. 13, we found that solely considering network
bandwidth does not accurately simulate real network conditions,
whereas having TCP control information always performs well.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 12

```text
8196
IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025
Fig. 14.
Long-duration video streaming sessions, i.e., varying network conditions and different user video streams. The average values for video quality and
buffering are shown, with error bars spanning ± one standard deviation from the average.
When considering RTT, CWND, and Queue delay, QoE can
improve by 1.2-9.4%. This suggests that in a real network en-
vironment, we cannot simply rely on network bandwidth for
evaluation, but need to incorporate TCP congestion control for
a better understanding of the ABR algorithm. These network
behavioral characteristics contribute to a better understanding
and learning of ABR algorithms.
Long-duration video streaming sessions: To gain a deeper
insight into Fortuna’s performance in diverse real-world video
streaming networks, it’s important to consider that these net-
works exhibit heavy-tailedness and TCP-related characteris-
tics, we utilize SSIM for video quality assessment. The video
undergoes de-interlacing using ffmpeg to generate a “canoni-
cal” 1080p60 or 720p60 source suitable for compression. Each
video chunk is encoded into ten different H.264 versions us-
ing the libx264 encoder in veryfast mode. These encodings en-
compass a range of options, from 240p60 video with a con-
stant rate factor (CRF) of 26 (approximately 200 kbps) to
1080p60 video with a CRF of 20 (about 5,500 kbps). This ap-
proach provides a spectrum of quality and bitrate choices for
the video stream, catering to diverse network conditions and
devices.
As shown in Fig. 14, we found that the simple Buffer-Based
ABR (BBA) algorithm [62] can achieve better performance,
while the ABR algorithm generated purely through RL train-
ing, known as Pensieve, performs poorly. Meanwhile, we have
observed that meta-RL does not consistently achieve optimal
performance due to the need for adaptation across a wide range
of video stream conditions. In real-world scenarios with vary-
ing user preferences, BBA, which relies on fewer assumptions
and requests videos based on buffer occupancy, closely approx-
imates the actual video playback process. MPC predicts bitrates
based on past network bandwidth. However, in a real environ-
ment, these network characteristics are complex and variable,
inﬂuenced by factors such as TCP and varying user preferences,
making adaptation to real network conditions difﬁcult. Fugu ex-
hibits weaker generalization in unknown network conditions us-
ing supervised learning, whereas Fortuna consistently performs
well in these unknown networks and user preferences. By learn-
ing these features and underlying TCP controls, it can better
understand the behavioral characteristics of the network. In addi-
tion, we also found that off-the-shelf meta-learning-based ABR
algorithms face challenges in adapting to new network condi-
tions. Furthermore, Fortuna learns the ABR algorithm perfor-
mance suboptimally from ofﬂine datasets, as ofﬂine datasets are
not always optimal. In contrast, Fortuna, which learns from di-
verse datasets, such as those from RL and expert demonstrations,
exhibits better performance.
VI. REAL-WORLD DEPLOYMENT AND EVALUATION
In this section, we describe the speciﬁc deployment of For-
tuna in streaming systems and evaluate it on 5G, 4G, and WiFi
networks.
In Section V-B, we conducted experiments using a simu-
lation platform to illustrate the generalization of the Fortuna
algorithm in real-world streaming media systems. In this sec-
tion, we deploy Fortuna in the real world and conduct three
sets of experiments. During these experiments, the video client
was running on a MacBook Pro laptop, accessing the video
server running on Ubuntu 20.04 through the HTTP proto-
col. These algorithms were deployed on dash.js, and the ex-
periment was repeated several times. Video clients requested
the bitrate from an Apache2 server, which ﬁrst went through
the ABR algorithms before sending a signal to request video
from the server. Due to the round-trip delay between the
ABR algorithms and the video server, we calculated the av-
erage round-trip delay under 5G, 4G, and WiFi network con-
ditions, which were 4.21 ms, 70.32 ms, and 14.22 ms, re-
spectively. During the experiment, Fortuna was compared
with Pensieve, BOLA, and MPC, and the collected QoE
dataset was normalized. The experimental results are shown in
Fig. 15.
Fig. 15 shows that the QoE under 5G and WiFi network con-
ditions is generally higher than that under 4G networks. This
is because 5G and WiFi networks have relatively high band-
widths, which can support higher bitrates and lower latency,
allowing the ABR algorithms to request high bitrates more sta-
bly. At the same time, we found that the QoE of various ABR
algorithms on 5G networks is more stable. Compared to WiFi
networks, ﬂuctuations in network bandwidth can cause ABR
algorithms to fail to continuously request high bitrates. Un-
der 5G, 4G, and WiFi network conditions, Fortuna improved
QoE values by 2.9%–5.1%, 5.2%–12.5%, and 2.6%–11.2%,
respectively. These experiments show that Fortuna, generated
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 13

```text
YI et al.: OPTIMIZING ADAPTIVE VIDEO STREAMING: OFFLINE RL AND META-LEARNING IN DIVERSE NETWORKS
8197
Fig. 15.
Comparing the QoE metric of Fortuna and existing ABR algorithms
on 5G, 4G and WiFi network conditions. In the bar chart, the averages are listed,
and the error bars span ± one standard deviation from the average.
by training in a simulated environment, can generalize and be
used in real-world streaming media networks. It can also max-
imize QoE values under different conditions and improve user
experience.
VII. CONCLUTION
We introduce Fortuna, a novel ofﬂine RL-based adaptive
video streams technique that effectively adapts to real-world
Internet conditions, and combines with TCP congestion con-
trol to further reduce rebuffering time, optimizing QoE ob-
jectives. Moreover, Fortuna can handle unconstrained video
stream sessions. In all considered internet video streaming sce-
narios, Fortuna rivals or outperforms the state-of-the-art ex-
isting approaches, with an average QoE improvement ranging
from 1.2%-31.9%. Additionally, experimental results demon-
strate that Fortuna exhibits better generalization capabilities in
unseen network conditions and QoE user preferences.
In practice, we believe that Fortuna can offer valuable insights
not only for bitrate adaptation of video streaming but also for
TCP congestion control, as it eliminates the costly expense of
online learning while enabling swift adaptation to new network
conditions.
ACKNOWLEDGMENT
The authors thank Prof. Li Zeping and Dr. Huang Tianchi
for their guidance regarding video streaming in practice, and
the anonymous IEEE TON, TMM reviewers for their valuable
feedback.
REFERENCES
[1] T. Barnett, S. Jain, U. Andra, and T. Khurana, “Cisco visual networking
index (VNI) complete forecast update,” 2017–2022,” Americas/EMEAR
Cisco Knowledge Network (CKN) Presentation, pp. 1–30, 2021.
[2] Y. Sun et al., “CS2P: Improving video bitrate selection and adaptation
with data-driven throughput prediction,” in Proc. ACM SIGCOMM Conf.,
2016, pp. 272–285.
[3] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal
bitrate adaptation for online videos,” IEEE/ACM Trans. Netw., vol. 28,
no. 4, pp. 1698–1711, Aug. 2020.
[4] B. Wang, M. Xu, F. Ren, and J. Wu, “Improving robustness of DASH
against unpredictable network variations,” IEEE Trans. Multimedia,
vol. 24, pp. 323–337, 2022.
[5] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic approach
for dynamic adaptive video streaming over HTTP,” in Proc. ACM Conf.
Special Int. Group Data Commun. (SIGCOMM), 2015, pp. 325–338.
[6] A. Lekharu, S. Kumar, A. Sur, and A. Sarkar, “A QoE aware LSTM
based bit-rate prediction model for DASH video,” in Proc. 10th Int. Conf.
Commun. Syst. Netw. (COMSNETS), 2018, pp. 392–395.
[7] N. Kan et al., “Uncertainty-aware robust adaptive video streaming with
bayesian neural network and model predictive control,” in Proc. 31st
ACM Workshop Netw. Operating Syst. Support Digit. Audio Video, 2021,
pp. 17–24.
[8] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video streaming
with pensieve,” in Proc. Conf. ACM Special Int. Group Data Commun.
(SIGCOMM), 2017, pp. 197–210.
[9] T. Huang, R.-X. Zhang, and L. Sun, “Zwei: A self-play reinforcement
learning framework for video transmission services,” IEEE Trans. Multi-
media, vol. 24, pp. 1350–1365, 2021.
[10] A. Bentaleb, M. N. Akcay, M. Lim, A. C. Begen, and R. Zimmer-
mann, “BoB: Bandwidth prediction for real-time communications using
heuristic and reinforcement learning,” IEEE Trans. Multimedia, vol. 25,
pp. 6930–6945, 2022.
[11] T. Huang et al., “Quality-aware neural adaptive video streaming with life-
long imitation learning,” IEEE J. Sel. Areas Commun., vol. 38, no. 10,
pp. 2324–2342, Oct. 2020.
[12] W. Li et al., “An apprenticeship learning approach for adaptive video
streaming based on chunk quality and user preference,” IEEE Trans. Mul-
timedia, vol. 25, pp. 2488–2502, 2022.
[13] F. Y. Yan et al., “Learning in situ: A randomized experiment in video
streaming,” in Proc. 17th USENIX Symp. Networked Syst. Des. Implemen-
tation, 2020, pp. 495–511.
[14] H. Mao et al., “Real-world video adaptation with reinforcement learning,”
in Proc ICML workshop, 2019, pp. 1–10.
[15] C. Finn, P. Abbeel, and S. Levine, “Model-agnostic meta-learning for fast
adaptation of deep networks,” in Proc. Int. Conf. Mach. Learn., 2017,
pp. 1126–1135.
[16] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, and L. Sun, “Learning tai-
lored adaptive bitrate algorithms to heterogeneous network conditions: A
domain-speciﬁc priors and meta-reinforcement learning approach,” IEEE
J. Sel. Areas Commun., vol. 40, no. 8, pp. 2485–2503, Aug. 2022.
[17] S. Wang, J. Lin, and Y. Dai, “MMVS: Enabling robust adaptive video
streaming for wildly ﬂuctuating and heterogeneous networks,” IEEE
Trans. Multimedia, vol. 26, pp. 11018–11030, 2024.
[18] N. Kan et al., “Improving generalization for neural adaptive video stream-
ing via meta reinforcement learning,” in Proc. 30th ACM Int. Conf. Mul-
timedia, 2022, pp. 3006–3016.
[19] Z. Xia, Y. Zhou, F. Y. Yan, and J. Jiang, “Genet: Automatic curriculum gen-
eration for learning adaptation in networking,” in Proc. ACM SIGCOMM
Conf., 2022, pp. 397–413.
[20] Y. Bengio, J. Louradour, R. Collobert, and J. Weston, “Curriculum learn-
ing,” in Proc. 26th Annu. Int. Conf. Mach. Learn., 2009, pp. 41–48.
[21] X. Zuo, J. Yang, M. Wang, and Y. Cui, “Adaptive bitrate with user-level
QoE preference for video streaming,” in Proc. IEEE INFOCOM 2022-
IEEE Conf. Comput. Commun., 2022, pp. 1279–1288.
[22] T. Huang, R.-X. Zhang, C. Wu, and L. Sun, “Optimizing adaptive video
streamingwithhumanfeedback,”inProc.31stACMInt.Conf.Multimedia,
2023, pp. 1707–1718.
[23] X. Wei et al., “Reinforcement learning-based qoe-oriented dynamic
adaptive streaming framework,” Inf. Sci., vol. 569, pp. 786–803,
2021.
[24] V. Mnih, “Playing Atari with deep reinforcement learning,” 2013,
arXiv:1312.5602.
[25] H. Mao et al., “Park: An open platform for learning-augmented computer
systems,” in Proc. Adv. Neural Inf. Process. Syst., 2019, pp. 1–20.
[26] V. H. Pong, A. V. Nair, L. M. Smith, C. Huang, and S. Levine, “Ofﬂine
meta-reinforcement learning with online self-supervision,” in Proc. Int.
Conf. Mach. Learn., 2022, pp. 17811–17829.
[27] S. Floyd and E. Kohler, “Internet research needs better models,”
ACM SIGCOMM Comput. Commun. Rev., vol. 33, no. 1, pp. 29–34,
2003.
[28] S. Floyd and V. Paxson, “Difﬁculties in simulating the internet,”
IEEE/ACM Trans. Netw., vol. 9, no. 4, pp. 392–403, Aug. 2001.
[29] H. Mao, M. Schwarzkopf, S. B. Venkatakrishnan, Z. Meng, and M. Al-
izadeh, “Learning scheduling algorithms for data processing clusters,” in
Proc. ACM Special Int. Group Data Commun., 2019, pp. 270–288.
[30] A. Kumar, R. Agarwal, X. Geng, G. Tucker, and S. Levine, “Ofﬂine Q-
learning on diverse multi-task data both scales and generalizes,” in Proc.
ICLR, 2023.
[31] A. Kumar et al., “DR3: Value-based deep reinforcement learning requires
explicit regularization,” in Proc. ICLR, 2024, pp. 1–41.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 14

```text
8198
IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 27, 2025
[32] H. Haile, K.-J. Grinnemo, S. Ferlin, P. Hurtig, and A. Brunstrom, “Perfor-
mance of QUIC congestion control algorithms in 5G networks,” in Proc.
ACM SIGCOMM Workshop 5G Beyond Netw. Measurements, Modeling,
Use Cases, 2022, pp. 15–21.
[33] N. Cardwell, Y. Cheng, C. S. Gunn, S. H. Yeganeh, and V. Jacobson, “BBR:
Congestion-based congestion control: Measuring bottleneck bandwidth
and round-trip propagation time,” Queue, vol. 14, no. 5, pp. 20–53, 2016.
[34] S. Ha, I. Rhee, and L. Xu, “Cubic: A new TCP-friendly high-speed tcp
variant,” ACM SIGOPS operating Syst. Rev., vol. 42, no. 5, pp. 64–74,
2008.
[35] Z. Wang, A. C. Bovik, H. R. Sheikh, and E. P. Simoncelli, “Image quality
assessment: From error visibility to structural similarity,” IEEE Trans.
Image Process., vol. 13, no. 4, pp. 600–612, Apr. 2004.
[36] V.Netﬂix,“Videomulti-methodassessmentfusion,”2019.[Online].Avail-
able: https://github.com/Netﬂix/vmaf
[37] A. Nair, A. Gupta, M. Dalal, and S. Levine, “Awac: Accelerating on-
line reinforcement learning with ofﬂine datasets,” in Proc. ICLR, 2021,
pp. 1–17.
[38] Z. Huo et al., “Faster on-device training using new federated momentum
algorithm,” 2020, arXiv:2002.02090.
[39] X. Jiang et al., “MNN: A universal and efﬁcient inference engine,” in Proc.
Mach. Learn. Syst., 2020, vol. 2, pp. 1–13.
[40] A. Gupta, V. Kumar, C. Lynch, S. Levine, and K. Hausman, “Relay pol-
icy learning: Solving long-horizon tasks via imitation and reinforcement
learning,” in Proc. Conf. Robot Learn., 2019, pp. 1–13.
[41] T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine, “Soft actor-
critic:
Off-policy
maximum
entropy
deep
reinforcement
learning
with a stochastic actor,” in Proc. Int. Conf. Mach. Learn., 2018,
pp. 1861–1870.
[42] J. Rothfuss, D. Lee, I. Clavera, T. Asfour, and P. Abbeel, “Promp: Proximal
meta-policy search,” in Proc. ICLR, 2019, pp. 1–25.
[43] C. M. Bishop and N. M. Nasrabadi, Pattern Recognition and Machine
Learning, vol. 4. Berlin, Germany: Springer, 2006.
[44] C. Finn and S. Levine, “Meta-learning and universality: Deep represen-
tations and gradient descent can approximate any learning algorithm,” in
Proc. ICLR, 2018, pp. 1–20.
[45] E. Mitchell, R. Rafailov, X. B. Peng, S. Levine, and C. Finn, “Ofﬂine
meta-reinforcementlearningwithadvantageweighting,”inProc.Int.Conf.
Mach. Learn., 2021, pp. 7780–7791.
[46] R. Netravali et al., “Mahimahi: Accurate {Record-and-Replay} for
{HTTP},” in Proc. USENIX Annu. Tech. Conf., 2015, pp. 417–429.
[47] J. Schmidt-Hieber, “Nonparametric regression using deep neural net-
works with ReLU activation function,” Ann. Statist., vol. 48, no. 4,
pp. 1875–1897, 2020.
[48] Z. Zhang, “Improved adam optimizer for deep neural networks,” in Proc.
IEEE/ACM 26th Int. Symp. Qual. Service, 2018, pp. 1–2.
[49] “FCC broadband dataset,” (n.d.). [Online].Available: http://data.fcc.
gov/download/measuring-broadband-America/2016/data-raw-2016-
jun.tar.gz
[50] “Norway HSDPA bandwidth logs,” (n.d.). [Online]. Available: http://
home.iﬁ.uio.no/paalh/dataset/hsdpa-tcp-logs/
[51] “Belgium 4G/LTE bandwidth logs (bonus),” (n.d.). [Online]. Available:
http://users.ugent.be/jvdrhoof/dataset-4g/logs/logs_all.zip
[52] H. Mao, S. B. Venkatakrishnan, M. Schwarzkopf, and M. Alizadeh, “Vari-
ance reduction for reinforcement learning in input-driven environments,”
ICLR, 2019, pp. 1–20.
[53] A. Narayanan et al., “Lumos5g: Mapping and predicting commercial
mmWave 5G throughput,” in Proc. ACM Internet Meas. Conf., 2020,
pp. 176–193.
[54] A. Narayanan et al., “A variegated look at 5G in the wild: Performance,
power, and QoE implications,” in Proc. ACM SIGCOMM Conf., 2021,
pp. 610–625.
[55] “sigcomm 2021,dash video, 5G,” (n.d.). [Online]. Available: https://drive.
google.com/drive/folders/1_Hxz6M8qxZJnpJz38ll-Bw7OV1U4FDSk
[56] J. Li et al., “Suphx: Mastering Mahjong with deep reinforcement learning,”
2020, arXiv:2003.13590.
[57] D. Ye et al., “Mastering complex control in MOBA games with deep
reinforcement learning,” in Proc. AAAI Conf. Artif. Intell., 2020, vol. 34,
pp. 6672–6679.
[58] K. Rakelly, A. Zhou, C. Finn, S. Levine, and D. Quillen, “Efﬁcient off-
policy meta-reinforcement learning via probabilistic context variables,” in
Proc. Int. Conf. Mach. Learn., 2019, pp. 5331–5340.
[59] “Meta RL,” (n.d.). [Online]. Available: https://github.com/katerakelly/
oyster
[60] A. Bentaleb, M. Lim, M. N. Akcay, A. C. Begen, and R. Zimmer-
mann, “Bitrate adaptation and guidance with meta reinforcement learn-
ing,” IEEE Trans. Mobile Comput., vol. 23, no. 11, pp. 10378–10392,
Nov. 2024.
[61] M. Allman, V. Paxson, and E. Blanton, “RFC 5681: TCP congestion con-
trol,” 2009.
[62] T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Wat-
son, “A buffer-based approach to rate adaptation: Evidence from a
large video streaming service,” in Proc. ACM Conf. SIGCOMM, 2014,
pp. 187–198.
Ling Yi received the masters degree in computer
science in 2022 from Guizhou University, Guiyang,
China,whereheiscurrentlyworkingtowardthePh.D.
degree. His research interests include video stream-
ing technologies, network congestion control, natural
language processing, and reinforcement learning for
realworld applications.
Yongbin Qin is currently a Professor with the School
of Computer Science and Technology, Guizhou Uni-
versity, Guiyang, China. His primary research inter-
ests include machine learning, natural language pro-
cessing, and large language models.
Ruizhang Huang received the Ph.D. degree from the
Chinese University of Hong Kong, Hong Kong, in
2008. She is currently a Professor with the School of
Computer Science and Technology, Guizhou Univer-
sity, Guiyang, China. Her primary research interests
include machine learning and natural language pro-
cessing.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.
```
