# EAStream - Environment-Aware Adaptive Bitrate Algorithm for Reliable Video Streaming Services

## 0. Identificacion del archivo

- Archivo fuente: `EAStream.pdf`
- Paginas detectadas: `14`
- SHA256 PDF: `83d86a17ba893e7529497f64087a6c561017a52328d8617305c40f671749da14`
- Texto crudo auxiliar PyMuPDF: `raw_text/24_eastream_2026_environment_aware_abr_meta_rl_vae.txt`
- Texto crudo auxiliar pdftotext -layout: `raw_text_layout/24_eastream_2026_environment_aware_abr_meta_rl_vae_layout.txt`

## 1. Uso previsto para Fase 4-5 v1

Fuente 2026 sobre meta-RL y representacion latente del entorno mediante VAE para generalizar sin fine-tuning online. Relevante para Fase 4-5 v1 por environment awareness/OOD, aunque su complejidad debe compararse con soluciones CPU-first defendibles.

## 2. Advertencia de fidelidad

Este archivo NO es un resumen breve. Es una extraccion tecnica densa para que Codex pueda leer el paper sin depender de conversiones Markdown corruptas. El PDF original sigue siendo la fuente de verdad para formulas, tablas, figuras, simbolos y resultados exactos. Cuando una formula, tabla o figura sea decisiva, se debe verificar contra el PDF original.

## 3. Identificacion textual extraida de las primeras paginas

```text
1176
IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026
EAStream: An Environment-Aware Adaptive Bitrate
Algorithm for Reliable Video Streaming Services
Zeming Huang, Wenjing Xiao
, Miaojiang Chen
, Member, IEEE, Zhiquan Liu
, Min Chen
, Fellow, IEEE,
Athanasios V. Vasilakos
, Senior Member, IEEE, Ahmed Farouk
, and Houbing Herbert Song
, Fellow, IEEE
Abstract—Video streaming has emerged as a widely used Inter-
net service, in which adaptive bitrate (ABR) algorithms play a crit-
ical role in delivering high quality of experience (QoE). However,
existing learning-based ABR methods often suffer from limited
generalization in unseen and dynamically changing network condi-
tions. Although some meta-reinforcement learning techniques have
been proposed to mitigate this issue, they generally depend on
additional online training or ﬁne-tuning. To overcome these lim-
itations, this paper introduces EAStream, an environment-aware
ABR algorithm based on meta-reinforcement learning for reliable
video streaming services. The method employs a variational au-
toencoder to extract a latent representation of the current network
environment from historical interaction data. This latent variable,
along with the current system state, is fed into a policy network
that perceives network conditions in real time and adapts bitrate
decisions accordingly, without requiring further online training.
A comprehensive evaluation is conducted using diverse real-world
network traces. Experimental results show that EAStream not only
achieves leading performance on in-distribution test sets compared
to state-of-the-art ABR algorithms, but also demonstrates superior
generalization capability on out-of-distribution test scenarios.
Index Terms—Adaptive video streaming, generalization, meta
learning, network uncertainty, quality of experience.
I. INTRODUCTION
W
ITH the rapid development of the Internet in recent
years, video streaming has become the predominant
Received 2 December 2025; revised 9 February 2026; accepted 3 March
2026. Date of publication 9 March 2026; date of current version 10 April 2026.
This work was supported in part by the National Natural Science Foundation of
China under Grant 62462002 and Grant 62502101, in part by the Natural Science
Foundation of Guangxi, China under Grant 2025GXNSFAA069958 and Grant
2025GXNSFBA069394, and in part by the Key Research and Development
Program of Guangxi under Grant AD25069071. (Zeming Huang and Wenjing
Xiao are co-ﬁrst authors.) (Corresponding author: Miaojiang Chen.)
Zeming Huang, Wenjing Xiao, and Miaojiang Chen are with the School
of Computer, Electronics and Information, Guangxi University, Nanning
530004, China, and also with the Guangxi Key Laboratory of Multimedia
Communications and Network Technology, Nanning 530004, China (e-mail:
zem@st.gxu.edu.cn; wenjingx@gxu.edu.cn; mjchen_cs@gxu.edu.cn).
Zhiquan Liu is with the College of Cyber Security, Jinan University,
Guangzhou 510632, China (e-mail: zqliu@jnu.edu.cn).
Min Chen is with the School of Computer Science and Engineering, South
China University of Technology, Guangzhou 510006, China, and also with
Pazhou Laboratory, Guangzhou 510330, China (e-mail: minchen@ieee.org).
Athanasios V. Vasilakos is with the Department of ICT and Center for
AI Research, University of Agder(UiA), 4879 Grimstad, Norway (e-mail:
thanos.vasilakos@uia.no).
Ahmed
Farouk
is
with
the
Faculty
of
Computers
and
Artiﬁcial
Intelligence,
Hurghada
University,
Hurghada
83523,
Egypt
(e-mail:
ahmed.farouk@sci.svu.edu.eg).
Houbing Herbert Song is with the Department of Information Systems,
University of Maryland, Baltimore, MD 21250 USA (e-mail: h.song@ieee.org).
Digital Object Identiﬁer 10.1109/TSC.2026.3671090
component of global Internet trafﬁc. According to the Global
Internet Phenomena Report 2024 [1], the trafﬁc transporting
video accounts for 68% and 64% of the total downlink trafﬁc of
ﬁxed and mobile networks, respectively. Given the industry’s
projected growth to $416.84 billion by 2030 [2], ensuring a
superiorQualityofExperience(QoE)iscriticalforuserretention
and business success. To achieve this, Adaptive Bitrate (ABR)
technology has been widely adopted as the standard delivery
mechanism [3], [4]. By dividing videos into chunks available
at multiple quality levels, ABR algorithms dynamically select
the optimal bitrate for each chunk based on real-time network
throughput and buffer occupancy. However, the ABR algorithm
faces challenges because it needs to balance conﬂicting ob-
jectives: maximizing video quality and minimizing playback
interruptions. Speciﬁcally, high bitrate chunks will be selected
for better playback quality. However, it will increase the risk
of playback stalls, especially in the case of unstable network
conditions.
```

## 4. Metadatos PDF detectados

```json
{
  "format": "PDF 1.4",
  "title": "EAStream: An Environment-Aware Adaptive Bitrate Algorithm for Reliable Video Streaming Services",
  "author": "",
  "subject": "IEEE Transactions on Services Computing;2026;19;2;10.1109/TSC.2026.3671090",
  "keywords": "",
  "creator": "LaTeX with hyperref package",
  "producer": "Acrobat Distiller 11.0 (Windows); modified using iText® Core 7.2.4 (AGPL version) ©2000-2022 iText Group NV",
  "creationDate": "D:20260328100955+05'30'",
  "modDate": "D:20260409192445-04'00'",
  "trapped": "",
  "encryption": null
}
```

## 5. Mapa de secciones detectado

- p. 1: I. INTRODUCTION
- p. 2: II. RELATED WORK
- p. 2: A. Conventional ABR Algorithms
- p. 2: B. Learning-Based ABR Algorithms
- p. 3: C. Meta-Reinforcement Learning for Generalization
- p. 3: III. METHODS
- p. 3: A. Problem Formulation
- p. 5: B. Bayesian Adaptive Modeling for Environmental
- p. 5: C. Approximating Bayes-Optimal Policies Via Meta-Learning
- p. 6: IV. SYSTEM DESIGN
- p. 6: A. System Architecture Overview
- p. 7: C. Neural Network Architectures
- p. 8: V. EVALUATION
- p. 8: A. Experimental Setup
- p. 9: 4 G vehicular networks under driving conditions in Sydney,
- p. 9: CHARACTERISTICS OF NETWORK TRACE DATASETS
- p. 9: PARAMETERS FOR DIFFERENT QOE METRICS
- p. 10: C. Effectiveness Analysis
- p. 12: TABLE III
- p. 12: RESOURCE CONSUMPTION AND INFERENCE LATENCY COMPARISON
- p. 12: D. Discussion and Limitations
- p. 12: VI. CONCLUSION
- p. 12: REFERENCES
- p. 14: W.Ellersick Prize in 2017, IEEE Jack Neubauer Memorial Award in 2019, and

## 6. Figuras, tablas, algoritmos y ecuaciones detectadas

- p. 4: Fig. 1.
- p. 6: Fig. 2.
- p. 6: Fig. 3.
- p. 7: Fig. 4.
- p. 7: Algorithm 1 and Algorithm 2 respectively.
- p. 8: Algorithm 1: Ofﬂine Meta-Training.
- p. 8: Algorithm 2: Online Adaptation.
- p. 9: TABLE I
- p. 9: TABLE II
- p. 9: Fig. 5.
- p. 9: Table II provides a summary of the parameters used for each
- p. 10: Fig. 6.
- p. 10: Fig. 6 illustrates the normalized average QoE scores for both
- p. 11: Fig. 7.
- p. 11: Fig. 8.
- p. 11: Fig. 9.
- p. 11: Fig. 10.
- p. 11: Fig. 11.
- p. 12: Fig. 12.
- p. 12: TABLE III
- p. 3: Fig. 1, a typical ABR streaming system involves
- p. 6: Fig. 2 .
- p. 7: Fig. 3, this module is
- p. 7: Fig. 4, this module is the
- p. 10: Fig. 5 illustrates the normalized average QoE scores
- p. 10: Fig. 5, our proposed EAStream consistently
- p. 10: Fig. 7 and Fig. 8 provide a more detailed
- p. 10: Fig. 9, EAStream has excel-
- p. 10: table 4GNY trajectory (as shown in Table I), which
- p. 10: Fig. 10, EAStream achieved the highest QoE
- p. 10: Fig. 11, the belief vectors form three distinct
- p. 10: Fig. 12(a), the agent achieves the best performance
- p. 10: Fig. 12(b). A small β makes the latent space irregular

## 7. Lineas con posible contenido matematico/formal

- p. 1: `ical role in delivering high quality of experience (QoE). However,`
- p. 1: `along with the current system state, is fed into a policy network`
- p. 1: `superiorQualityofExperience(QoE)iscriticalforuserretention`
- p. 1: `QoE preferences. To address this, Model Predictive Control`
- p. 1: `by optimizing QoE over a future horizon based on throughput`
- p. 2: `work conditions. This is because the learned policy is prone`
- p. 2: `relies on deterministic embeddings supervised solely by reward`
- p. 2: `based on Lyapunov optimization to maximize the QoE while`
- p. 3: `policy that generalizes across different network environments`
- p. 3: `In contrast, context-based methods learn a single policy con-`
- p. 3: `infer latent context variables from off-policy data, signiﬁcantly`
- p. 3: `based framework to learn a meta-policy ofﬂine, which is then`
- p. 3: `rapidly ﬁne-tuned online to create a tailor-made policy for`
- p. 3: `called EAStream, to approximate the BAMDP policy.`
- p. 4: `QoE of users. QoE evaluates the subjective satisfaction of users,`
- p. 4: `QoEqual =`
- p. 4: `thedurationbywhichitsdownloadtime,T(Rn) = dn(Rn)/ ˆCn,`
- p. 4: `Tn = max {T(Rn) −Bn−1, 0} .`
- p. 4: `QoErebuf =`
- p. 4: `QoEvar =`
- p. 4: `QoE Objective: The ﬁnal QoE objective is deﬁned as a linear`
- p. 4: `QoE = μ1QoEqual −μ2QoErebuf −μ3QoEvar,`
- p. 4: `where µ = (μ1, μ2, μ3) is a vector of non-negative weighting`
- p. 4: `termine the optimal sequence of bitrates R = (R1, R2, . . ., RN)`
- p. 4: `that maximizes the total QoE, subject to the system’s dynamic`
- p. 4: `maxR1,...,RN QoE,`
- p. 4: `tn+1 = tn + T(Rn) + Tn,`
- p. 4: `Bn+1 = max(0, Bn −T(Rn)) + L,`
- p. 4: `B1 = Ts,`
- p. 4: `0 ≤Bn ≤Bmax,`
- p. 4: `ary conditions. B1 = Ts deﬁnes the initial buffer level.`
- p. 5: `distribution. The agent’s objective is to learn a policy π that`
- p. 5: `maximizes the long-term cumulative reward:`
- p. 5: `J(π) = Eρ0,P,π`
- p. 5: `t = (st, bt), consisting of the observable`
- p. 5: `and emits a reward rt+1 based on the true (but unknown)`
- p. 5: `t+1 = (st+1, bt+1).`
- p. 5: `S+ = S × B decomposes into the physical transition and the`
- p. 5: `= P +(st+1, bt+1|st, at, rt, bt)`
- p. 5: `= Ebt[P(st+1|st, at)]`
- p. 5: `· δ(bt+1 = Update(bt, st, at, st+1))`
- p. 5: `The reward function for the hyper-state depends solely on the`
- p. 5: `physical state transition, as the user’s QoE is derived from the`
- p. 5: `t+1) = R(st, at, st+1),`
- p. 5: `where R(st, at, st+1) is the standard QoE reward deﬁned in (5).`
- p. 5: `BAMDP, denoted by M + = (S+, A, R+, P +, ρ+`
- p. 5: `sequently, our primary goal is to ﬁnd a policy π to maximize the`
- p. 5: `accumulated long-term reward in the BAMDP:`
- p. 5: `J+(π) = Eb0,ρ+`
- p. 5: `0 ,P +,π`
- p. 5: `policy. While this problem can theoretically be addressed via`
- p. 5: `this policy.`
- p. 5: `ELBO = Eρ`
- p. 5: `policy π and the initial state distribution ρ0. This equation`
- p. 6: `environmental awareness, and a DRL Policy Module for adaptive decision-making.`
- p. 6: `log pθ(τ:H|m) = log pθ(s0|m) +`
- p. 6: `state and reward at each time step, enforcing a precise modeling`
- p. 6: `a smooth latent space that facilitates stable policy optimization.`
- p. 6: `Based on the inferred belief, the DRL policy πψ is optimized`
- p. 6: `to approximate a Bayes-Optimal policy. At each timestep t, a`
- p. 6: `mt ∼qφ(m|τ:t). The policy then takes the current physical state`
- p. 6: `st and the latent variable as input, denoted as πψ(at|st, mt).`
- p. 6: `L(φ, θ, ψ) = Ep(M) [J(ψ, φ) + λ · ELBO(φ, θ)] ,`
- p. 6: `p(M). In this equation, J(ψ, φ) denotes the expected return for`
- p. 6: `approximate policy, and the second term is the task inference`
- p. 6: `maximizing the RL reward and the accuracy of belief recon-`
- p. 6: `and a policy module for decision-making. The overall EAStream`
- p. 6: `processes the agent’s historical interaction trajectory (τt =`
- p. 7: `Architecture of the DRL Policy Module.`
- p. 7: `π(at|st, mt), which takes in the current state and belief and`
- p. 7: `QoE reward. Unlike traditional DRL-based agents, our policy`
- p. 7: `environment. This allows the policy to learn not just one ﬁxed`
- p. 7: `strategy, but a highly adaptive meta-policy.`
- p. 7: `B. State, Action, and Reward Deﬁnition`
- p. 7: `reward function, as well as the state and action space.`
- p. 7: `st = (⃗xt, ⃗τt, ⃗nt, bt, ct, lt).`
- p. 7: `and transmission time of the past w video chunks(We set w = 8`
- p. 7: `A = {0, 1, . . . , K −1}.`
- p. 7: `▷Reward: To optimize the QoE objective in (5), we deﬁne the`
- p. 7: `reward function rt accordingly. Once the t-th video chunk has`
- p. 7: `been successfully transmitted, the agent will receive a reward of`
- p. 7: `rt = μ1 · q(Rt) −μ2 · Tt −μ3 · |q(Rt) −q(Rt−1)|.`
- p. 7: `This reward function directly guides the behavior of the agent.`
- p. 7: `nents: the Belief Inference Module and the DRL Policy Module.`
- p. 7: `ˆst, while a Reward Head predicts the reward ˆrt. Both heads are`
- p. 7: `▷DRL Policy Module: As shown in Fig. 4, this module is the`
- p. 7: `policy capable of inferring environmental characteristics and`
- p. 8: `1: Initialize belief params φ, θ; policy params ψ; entropy`
- p. 8: `2: Initialize replay buffer Dbelief; loss weights λs, λr, β.`
- p. 8: `//Update Policy Module`
- p. 8: `Update ψ by minimizing PPO loss:`
- p. 8: `L(ψ) = ˆEt[−LCLIP(ψ) + LVF(ψ) −αH[πψ](st, mt)]`
- p. 8: `Compute average entropy ¯H = ˆEt[H[πψ(·|st, mt)]]`
- p. 8: `// Calculate weighted loss`
- p. 8: `Lstate = −Ej,t[log pθ(sj,t+1|sj,t, aj,t, mj)].`
- p. 8: `Lreward = −Ej,t[log pθ(rj,t+1| . . . , mj)].`
- p. 8: `LKL = Ej[DKL(qφ(m|τj)||p(m))].`
- p. 8: `LELBO = λsLstate + λrLreward + βLKL`
- p. 8: `policy’s early exploration.`
- p. 8: `policy and belief modules separately.`
- p. 8: `The policy network is updated using the Proximal Policy`
- p. 8: `Optimization (PPO) algorithm [47]. While off-policy algorithms`
- p. 8: `select the on-policy PPO to ensure training stability in our`
- p. 8: `continuously, data stored in an off-policy replay buffer would`
- p. 8: `LCLIP(ψ) = ˆEt`
- p. 8: `entropy adjustment mechanism. The ﬁnal policy loss combines`
- p. 8: `the clipped loss, the value function loss LVF, and the entropy`
- p. 8: `L(ψ) = ˆEt`
- p. 8: `−LCLIP(ψ) + LVF(ψ) −αH[πψ](st, mt)`
- p. 8: `1: Load qφ and policy πψ.`
- p. 8: `3: for t = 1, 2, . . . , N do`
- p. 8: `// Policy Decision`
- p. 8: `Select action at ∼πψ(at|st, mt).`
- p. 8: `Crucially, gradients from the policy update are not backprop-`
- p. 8: `replay buffer. The objective is to minimize the ELBO loss`
- p. 8: `derived in (11), which aggregates the state reconstruction loss,`
- p. 8: `reward prediction loss, and the KL divergence regularization`
- p. 8: `The adaptability of policy is achieved entirely through real-time`
- p. 8: `state st are jointly input into the policy network πψ to decide the`
- p. 8: `and observes the new state and reward. During the entire online`
- p. 8: `the policy and value network, the learning rate is set to 1 × 10−4.`
- p. 8: `of ϵ = 0.2, a reward discount factor of γ = 0.99 and a target`
- p. 8: `entropy of Htarget = 0.1. For belief inference module (φ, θ), the`
- p. 8: `weights for its loss function are set to λs = 1.0, λr = 1.0, and`
- p. 8: `β = 0.1, respectively. The dimension of the latent belief m is`
- p. 9: `PARAMETERS FOR DIFFERENT QOE METRICS`
- p. 9: `Normalized average QoE comparison on the in-distribution Hybrid`
- p. 9: `▷QoE Metrics: To evaluate the algorithm performance based`
- p. 9: `on different user preferences, we adopted two distinct QoE`
- p. 9: `model for each QoE objective. The speciﬁc deﬁnition is as`
- p. 9: `QoE metric.`
- p. 9: `present the normalized average QoE scores in Figs. 5 and 6.`
- p. 10: `Normalized average QoE comparison on the out-of-distribution test`
- p. 10: `datasets. Fig. 5 illustrates the normalized average QoE scores`
- p. 10: `achieves the highest, or joint-highest, average QoE across all`
- p. 10: `and stable policy even when trained on a diverse hybrid dataset.`
- p. 10: `suggests that EAStream not only achieves a higher average QoE`
- p. 10: `Fig. 6 illustrates the normalized average QoE scores for both`
- p. 10: `QoE metrics on these two unseen datasets. The results clearly`
- p. 10: `the highest average QoE. Speciﬁcally, its performance on the`
- p. 10: `As shown in Fig. 10, EAStream achieved the highest QoE`
- p. 11: `CDF of QoE scores on the out-of-distribution test sets (Oboe and 4GNy).`
- p. 12: `of the belief inference and policy modules. However, this cost`
- p. 13: `[25] X. Ma et al., “QAVA: QoE-Aware adaptive video bitrate aggregation`
- p. 13: `policy meta-reinforcement learning via probabilistic context variables,” in`
- p. 13: `policy optimization algorithms,” 2017, arXiv:1707.06347.`
- p. 14: `Min Chen (Fellow, IEEE) is currently a full pro-`

## 8. Extraccion tecnica cruda por categorias


### 8.1. modelo algoritmo arquitectura

Palabras clave usadas: `model, algorithm, architecture, framework, policy, neural, network, deep reinforcement, reinforcement learning, DRL, DQN, PPO, A2C, A3C, actor, critic, agent, meta, meta-learning, MAML, offline reinforcement, curriculum, VAE, variational autoencoder, LSTM, BiLSTM, GRU, CNN, predictor, bandwidth prediction, Plume, Gelato, Ahaggar, CausalSim, IMDP, domain-specific prior`

**Fragmento 1 - p. 5 - score 8:**

. (10) The strategy that achieves this goal is termed a Bayes-optimal policy. While this problem can theoretically be addressed via methods like posterior sampling [43] or Bayesian planning [44], these approaches typically incur prohibitive computational over- head for real-time ABR decisions. Computing exact belief up- dates is also generally infeasible in practice. Therefore, we leverageameta-reinforcementlearningparadigmtotacklethis issue, as detailed below. C. Approximating Bayes-Optimal Policies Via Meta-Learning The theoretical solution for BAMDP is computationally difﬁ- cult.Ourapproach,EAStream,employsameta-learningstrategy inspiredbyVariBAD[45]toacquireasolutionthatapproximates this policy. In the meta-learning framework, we model different network environments as individual tasks, each deﬁned by a hidden latent variable mi. This latent variable corresponds to the belief in BAMDP. Since the latent variable is unknown, the agent must infer information about mi from its historical information. Speciﬁcally,weemployanencodertotransformthetrajectoryτ:t into an inferred distribution qφ(m|τ:t) within the latent space. This distribution serves as an inference of the environment’s latent features. The learning process uses the framework of Variational Au- toencoder (VAE) [46]. We optimize the encoder network by maximizing the Variational Lower Bound (ELBO): ELBO = Eρ  Eqφ(m|τ:t)[log pθ(τ:H|m)] −DKL(qφ(m|τ:t)||pθ(m))] . (11) Here, ρ denotes the trajectory distribution induced by the current policy π and the initial state distribution ρ0. This equation consists of two components. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 2 - p. 7 - score 8:**

In parallel, the Critic Network with a similar architecture outputs a state value estimation V (st, mt) to guide the learning of the actor. D. Ofﬂine Training and Online Adaptation This section details the learning and adaptation workﬂow of EAStream. The process consists of two stages summarized in Algorithm 1 and Algorithm 2 respectively. ▷Ofﬂine Meta-Training: This stage aims to learn a meta- policy capable of inferring environmental characteristics and adapting decisions across diverse network conditions. By ex- posing the agent to a wide variety of environments at this stage, we force it to learn how to identify potential network conditions rather than memorizing speciﬁc training trajectories.

**Fragmento 3 - p. 7 - score 8:**

The output of GRU is subsequently passed through FC to generate the parameters of a Gaussian distribution, representing the posterior belief mt. The Decoder provides the training objective by using two separate networks to reconstruct the system’s dynamics. Speciﬁcally, consistent with the factorization of the trajectory likelihood in (12), a State Transition Head predicts the next state ˆst, while a Reward Head predicts the reward ˆrt. Both heads are implemented as fully connected layers. ▷DRL Policy Module: As shown in Fig. 4, this module is the agent’s core decision-making component and is implemented withanActor-Criticarchitecture.ItbeginswithaFeatureExtrac- tor that processes the raw state.

**Fragmento 4 - p. 2 - score 7:**

r We conduct extensive experiments across a diversity of real-world network traces (Section V). Our evaluations show that EAStream not only achieves state-of-the-art performance on in-distribution networks, but also shows better generalization ability in unseen, out-of-distribution environments compared to state-of-the-art algorithms. The remainder of this paper is structured as follows. Section II reviews the related work in ABR streaming and meta-reinforcement learning. Section III formulates the ABR problem and presents our Bayesian adaptive modeling approach. Section IV details the system design of our proposed EAStream framework, including its architecture and training methodology.

**Fragmento 5 - p. 3 - score 7:**

To address this, a recent work NetLLM [33] explores adapting Large Language Models (LLMs) as universal foundation models to handle diverse networking tasks. However, it introduces signiﬁcant computational overhead and latency, making it less ideal for real-time deployment on resource- constrained devices. C. Meta-Reinforcement Learning for Generalization Totackletheoverﬁttingproblem, meta-learningoffers alearn- ing paradigm [34]. Its core idea is to train on a distribution of related tasks to learn an inductive bias, enabling fast adaptation to new, unseen tasks with high sample efﬁciency at test time [35]. While conventional RL agents tend to overﬁt the training traces, Meta-Reinforcement Learning (Meta-RL) learns an adaptive policy that generalizes across different network environments from the task distribution [35].

**Fragmento 6 - p. 7 - score 7:**

The weighting coefﬁcients μ1, μ2, μ3 control the balance. C. Neural Network Architectures The proposed EAStream framework consists of two compo- nents: the Belief Inference Module and the DRL Policy Module. ▷Belief Inference Module: As shown in Fig. 3, this module is designed to infer the characteristics of the network conditions, which contains a recurrent encoder and a predictive decoder. The Encoder sequentially processes the interaction history. For each time step t, tuple (at−1, rt, st) is ﬁrst passed through their respective fully connected layers (FC), then merged into a feature vector. This feature vector is then fed into a Gated Recurrent Unit (GRU) to capture sequential patterns.

**Fragmento 7 - p. 13 - score 7:**

Distrib. Syst. Lab., Univ. Melbourne, Parkville, VIC, Australia, Tech. Rep., vol. 4, no. 2007, p. 70, 2007. [43] M. Strens, “A Bayesian framework for reinforcement learning,” in Proc. Int. Conf. Mach. Learn., 2000, pp. 943–950. [44] A. Guez, D. Silver, and P. Dayan, “Efﬁcient Bayes-adaptive reinforcement learning using sample-based search,” in Proc. Adv. Neural Inf. Process. Syst., vol. 25, 2012, pp. 1–9. [45] L. Zintgraf et al., “Varibad: A very good method for Bayes-adaptive deep RL via meta-learning,” in Proc. Int. Conf. Learn. Representations (ICLR), 2019, pp. 1–14. [46] D. P. Kingma and M. Welling, “Auto-encoding variational Bayes,” 2013, arXiv:1312.6114. [47] J.Schulman,F.Wolski,P.Dhariwal,A.Radford,andO.Klimov,“Proximal policy optimization algorithms,” 2017, arXiv:1707.06347.

**Fragmento 8 - p. 13 - score 7:**

[33] D. Wu et al., “NetLLM: Adapting large language models for networking,” in Proc. ACM SIGCOMM 2024 Conf., 2024, pp. 661–678. [34] T. Hospedales, A. Antoniou, P. Micaelli, and A. Storkey, “Meta-learning in neural networks: A survey,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 44, no. 9, pp. 5149–5169, Sep. 2022. [35] J. Beck et al., “A tutorial on meta-reinforcement learning,” Found. Trends Mach. Learn., vol. 18, no. 2/3, pp. 224–384, 2025. [36] C. Finn, P. Abbeel, and S. Levine, “Model-agnostic meta-learning for fast adaptation of deep networks,” in Proc. Int. Conf. Mach. Learn., 2017, pp. 1126–1135. [37] A. Nichol, J. Achiam, and J. Schulman, “On ﬁrst-order meta-learning algorithms,” 2018, arXiv:1803.02999.

**Fragmento 9 - p. 1 - score 6:**

The seminal method, Pensieve [8], uses deep reinforcement learning algorithm (DRL) to learn bitrate adaptation policies. Unlike the MPC-based methods that rely on system models, the DRL algorithm directly learns the model-free strategies from experience, enabling it to better handle dynamic networks. Furthermore, DRL algorithms have long-term planning capa- bilities, which allows them to make complex strategic trade- offs that balance instant video quality and long-term viewing stability. 1939-1374 © 2026 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission.

**Fragmento 10 - p. 2 - score 6:**

Section V presents the comprehensive experimental evalua- tion and analysis of results. Finally, Section VI concludes the paper. II. RELATED WORK This section will review the related work in the ﬁelds of ABR streaming and meta-learning, particularly focusing on meta-reinforcement learning. A. Conventional ABR Algorithms ABR streaming has been the subject of extensive research in the ﬁeld of network communication over the past decade. Early ABR algorithms primarily relied on explicitly deﬁned rules and mathematical models. These approaches are typically classiﬁed into two main categories: heuristic-based methods and control- theoretic methods. Heuristic-based methods represent the earliest class of ABR algorithms, selecting bitrates through intuitive, pre-deﬁned rules.

**Fragmento 11 - p. 2 - score 6:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1177 Despite these advantages, one challenge DRL-based ABR methods face is their limited generalization to unseen net- work conditions. This is because the learned policy is prone to overﬁtting to the training network environment. Such over- specialization is particularly problematic as real-world networks are inherently dynamic and non-stationary. In fact, when de- ployed in real-world scenarios, their performance has been shown to be even inferior to that of simple heuristic-based methods [10]. To tackle this generalization challenge, recent studies have introduced meta-reinforcement learning approaches, which gen- erally fall into two categories.

**Fragmento 12 - p. 2 - score 6:**

By treating unknown parameters such as network bandwidth as random variables and maintaining a probability dis- tribution (posterior distribution) for them, the algorithm not only makes decisions based on the current estimated bandwidth, but also based on the complete state of all pos- sible bandwidth states and their occurrence probabilities, making ABR decisions more robust in dynamic network environments. r We propose EAStream (Section IV), a novel environment- aware ABR framework based on meta-reinforcement learning. Unlike optimization-based meta-learning meth- ods that require online ﬁne-tuning, EAStream leverages a context-based mechanism to adapt to new environments in real-time without any gradient updates during deployment.

**Fragmento 13 - p. 3 - score 6:**

In a different structure, MetaABR [14] extracts latent contexts from historical trajectories to adjust policies without online gradient updates. However, it relies on deterministic embeddings, ignoring the inherent uncertainty in bandwidth evolution. In contrast, our proposed EAStream formulates the ABR problem as a BAMDP. By inferring a probabilistic belief over the environment via a VAE, our method explicitly models un- certainty, enabling robust zero-shot adaptation to unseen condi- tions. III. METHODS This section formulates the ABR decision process as an optimization task and models the network uncertainty using a BAMDP. We then propose a Meta-RL-based ABR algorithm, called EAStream, to approximate the BAMDP policy.

**Fragmento 14 - p. 3 - score 6:**

More advanced methods like PEARL [41] extend this by training a probabilistic encoder to infer latent context variables from off-policy data, signiﬁcantly improving meta-training sample efﬁciency. Several recent works have applied optimization-based meta- learning to the ABR problem, requiring an online training phase to adapt. For instance, A2BR [12] employs a MAML- based framework to learn a meta-policy ofﬂine, which is then rapidly ﬁne-tuned online to create a tailor-made policy for speciﬁc network conditions. Similarly, MMVS [13] integrates the MAML-based framework with PPO to handle highly ﬂuc- tuating networks, and proposes a meta advantage normalization technique to stabilize the online adaptation process.

**Fragmento 15 - p. 3 - score 6:**

Other works focus on improving adaptation in high-dimensional parameter spaces. For instance, LEO [39] decouples the adaptation from the high-dimensional parameter space via the construction of a latent embedding con- ditioned on the data and conducting the meta-learning updates in this low-dimensional space. In contrast, context-based methods learn a single policy con- ditioned on a task-speciﬁc context variable, which summarizes the agent’s interaction history and enables adaptation without test-time gradient updates. A pioneering approach, RL2 [40], uses a recurrent neural network (RNN) to implicitly infer the en- vironment’s underlying dynamics.

**Fragmento 16 - p. 6 - score 6:**

Consequently, the agent can adapt its decision-making process in response to the estimated hidden dynamics. The overall training objective is to optimize the combined objective: L(φ, θ, ψ) = Ep(M) [J(ψ, φ) + λ · ELBO(φ, θ)] , (13) where Ep(M) denotes the expectation over the task distribution p(M). In this equation, J(ψ, φ) denotes the expected return for approximate policy, and the second term is the task inference objective. The hyperparameter λ controls the trade-off between maximizing the RL reward and the accuracy of belief recon- struction. Fig. 3. Architecture of the Belief Inference Module. IV. SYSTEM DESIGN This section details the architecture and training methodol- ogy of EAStream, our proposed meta-reinforcement learning framework for adaptive bitrate streaming.

**Fragmento 17 - p. 6 - score 6:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1181 Fig. 2. Overall Architecture of the EAStream Framework. The system comprises two main modules: a Belief Inference Module responsible for learning environmental awareness, and a DRL Policy Module for adaptive decision-making. The ﬁrst is the reconstruction likelihood. Crucially, the decoder pθ is tasked with predicting the entire trajectory τ:H based on the latent belief m. This forces m to capture the un- derlying predictive dynamics of the network, rather than merely compressing interaction history. Using the Markov property, this likelihood decomposes into: log pθ(τ:H|m) = log pθ(s0|m) + H−1  t=0 [log pθ(st+1|st, at, m) + log pθ(rt+1|st, at, st+1, m)].

**Fragmento 18 - p. 6 - score 6:**

A. System Architecture Overview The EAStream framework consists of two core modules: a be- lief inference module responsible for environmental awareness, and a policy module for decision-making. The overall EAStream architecture is illustrated in Fig. 2 . The belief inference module is designed based on the prin- ciples of VAE. It comprises two modules: a recurrent Be- lief Encoder and a predictive Decoder. The Belief Encoder processes the agent’s historical interaction trajectory (τt = (s0, a0, r1, . . . , st)) to infer a latent variable, m. This latent vari- able m represents its probabilistic belief regarding the hidden characteristics of the current network conditions.

**Fragmento 19 - p. 8 - score 6:**

While off-policy algorithms like SAC are known for high sample efﬁciency, we explicitly select the on-policy PPO to ensure training stability in our meta-learning framework. Since the Belief Encoder evolves continuously, data stored in an off-policy replay buffer would contain obsolete belief representations. PPO avoids this issue by strictly learning from fresh trajectories consistent with the current encoder. We utilize the clipped surrogate objective to prevent destruc- tive large updates: LCLIP(ψ) = ˆEt  min  rt(ψ) ˆAt, clip(rt(ψ), 1 −ϵ, 1 + ϵ) ˆAt  , (17) where rt(ψ) is the probability ratio, ϵ is a hyperparameter used to limit the variation of the probability ratio and ˆAt is the advantage estimate.

**Fragmento 20 - p. 8 - score 6:**

V. EVALUATION A. Experimental Setup ▷Implementation: We implement EAStream in PyTorch and optimize the model parameters using the Adam optimizer. For the policy and value network, the learning rate is set to 1 × 10−4. The PPO algorithm is conﬁgured with a clipping parameter of ϵ = 0.2, a reward discount factor of γ = 0.99 and a target entropy of Htarget = 0.1. For belief inference module (φ, θ), the learning rate is 1 × 10−3, and it is trained using a replay buffer with a capacity of 1000 trajectories and a batch size of 32. The weights for its loss function are set to λs = 1.0, λr = 1.0, and β = 0.1, respectively. The dimension of the latent belief m is set to 16.

**Fragmento 21 - p. 9 - score 6:**

r FESTIVE [5]: A rate-based heuristic algorithm. This al- gorithm uses the harmonic average of the nearest chunks download rates for throughput estimation. r RobustMPC [7]: An algorithm based on the theory of MPC. This algorithm predicts the future optimal sequence by combining throughput estimation and buffer informa- tion. r Pensieve [8]: A state-of-the-art ABR algorithm leveraging deep reinforcement learning. r NetLLM [33]: The ﬁrst framework using LLMs for net- working tasks through ﬁne-tuning to enhance generaliza- tion and performance. r Comyco [9]: A quality-aware ABR method based on im- itation learning. It trains the neural network by imitating the expert actions.

**Fragmento 22 - p. 12 - score 6:**

Finally, in extreme outlier scenarios that deviate signiﬁcantly from the training distribution, the inferred belief may become inaccurate. As noted in Section VI, leveraging the reconstruction error for anomaly detection offers a promising avenue to mitigate this issue in future work. VI. CONCLUSION This paper presents EAStream, a context-based meta- reinforcement learning framework designed to address the gen- eralization challenge in adaptive bitrate streaming. By modeling theproblemasaBAMDPandutilizingavariationalautoencoder, EAStream infers latent beliefs about network dynamics from interactionhistory.Thismechanismenablesthepolicytoachieve zero-shot adaptation to unseen network conditions without re- quiring computationally expensive online ﬁne-tuning.


### 8.2. estado inputs features

Palabras clave usadas: `state, input, feature, observation, throughput, bandwidth, buffer, download time, chunk size, history, past, remaining, TCP, RTT, CWND, device, resolution, content, CMCD, CMSD, network condition, environment, latent, context, trace features`

**Fragmento 1 - p. 7 - score 9:**

Vector-based inputs, including the throughput history ⃗xt, download time history ⃗τt, and the vec- tor of next chunk sizes ⃗nt, are fed into one-dimensional convo- lutional layers to capture temporal features. Concurrently, scalar inputs, including the buffer occupancy bt, remaining chunks ct, and the last selected bitrate lt, are processed by dedicated fully connected layers. These features are then concatenated with the latent belief mt. The resulting high-dimensional feature vector serves as the input to two independent networks. The Actor Network, a multi-layer network with a ﬁnal Softmax activation, maps these features to a probability distribution corresponding to the bitrates.

**Fragmento 2 - p. 5 - score 7:**

, (7) where H denotes the time horizon of a video streaming ses- sion, and γ ∈[0, 1] is the discount factor that determines the importance of future rewards. However, a core limitation of the standard MDP lies in its assumption of a stationary or perfectly known transition function P(st+1|st, at). This assumption is frequently violated in real-world networks, where conditions like bandwidth are highly dynamic and non-stationary. An ABR agent trained under one speciﬁc network trace may fail to generalize to other ﬂuctuating network conditions, leading to suboptimal performance. To address this limitation, where the true dynamics of the environment are unknown, we model the ABR problem as a Bayes-Adaptive Markov Decision Process (BAMDP) [15]. In a standard MDP, the agent assumes the network follows a ﬁxed rule. In contrast, a BAMDP agent acknowledges its ignorance about the speciﬁc network scenario. It maintains a belief state—a probabilistic “mental model” of the current net- work environment. As the agent observes new state transitions, it recursively updates this belief, allowing it to adapt its strategy dynamically based on its conﬁdence in the environment’s state. In this framework, the unknown network dynamics are treated as a latent variable. The agent maintains a belief state, bt, deﬁned as the posterior distribution over these possible network environments given the interaction history τ:t. The decision-making process in a BAMDP extends the stan- dard MDP cycle by incorporating a belief update step. The process proceeds as follows: 1) State Representation: At each timestep t, the agent’s state is a hyper-state s+ t = (st, bt), consisting of the observable physical state st and the current belief bt. 2) Action & Observation: The agent selects an action at. The env

**Fragmento 3 - p. 2 - score 5:**

Optimization-based methods [12], [13] learn an adaptable initialization but typically rely on online gradient updates during playback. This requirement introduces signiﬁcant computational overhead and latency, making them less ideal for resource-constrained devices. Conversely, the context-based method [14] adapts by inferring a latent context vector from history without online gradient updates. However, it relies on deterministic embeddings supervised solely by reward signals, which limits their ability to model the uncertainty of stochastic networks and fails to capture the underlying state transition dynamics. To overcome these limitations, we propose EAStream, a novel probabilistic context-based framework.

**Fragmento 4 - p. 7 - score 5:**

This allows the policy to learn not just one ﬁxed strategy, but a highly adaptive meta-policy. B. State, Action, and Reward Deﬁnition To train the DRL agent, this section explicitly deﬁnes the reward function, as well as the state and action space. ▷State: For every time step t, the agent receives a state st. This state is a multi-dimensional vector that includes in- formation about the playback status and network conditions. Following the design of Pensieve [8], we formulate the state st as follows: st = (⃗xt, ⃗τt, ⃗nt, bt, ct, lt). (14) Here, ⃗xt and ⃗τt are vectors representing the historical throughput and transmission time of the past w video chunks(We set w = 8 following the standard conﬁguration in [8].); ⃗nt denotes the ﬁle size for K available bitrates of next chunk; bt is the current buffer occupancy; ct denotes the number of unplayed chunks; and lt denotes the last chunk’s bitrate.

**Fragmento 5 - p. 7 - score 5:**

1182 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 Fig. 4. Architecture of the DRL Policy Module. potential dynamics of the network environment rather than merely compressing past information. The second part is the DRL strategy responsible for action selection. The objective is to learn a near-optimal strategy π(at|st, mt), which takes in the current state and belief and outputs an action that maximizes the long-term cumulative QoE reward. Unlike traditional DRL-based agents, our policy network is conditional on state st and belief mt. This dual- input structure is the key to achieving adaptability. The state st provides the most recent state of the environment, while the belief mt provides richer, history-based information about the environment.

**Fragmento 6 - p. 1 - score 4:**

Although some meta-reinforcement learning techniques have been proposed to mitigate this issue, they generally depend on additional online training or ﬁne-tuning. To overcome these lim- itations, this paper introduces EAStream, an environment-aware ABR algorithm based on meta-reinforcement learning for reliable video streaming services. The method employs a variational au- toencoder to extract a latent representation of the current network environment from historical interaction data. This latent variable, along with the current system state, is fed into a policy network that perceives network conditions in real time and adapts bitrate decisions accordingly, without requiring further online training.

**Fragmento 7 - p. 2 - score 4:**

Unlike optimization- based methods, EAStream achieves robust generalization with- out any online parameter updates. Crucially, distinct from the previous context-based approach that relies on deterministic vectors, we formulate the ABR problem as a Bayesian Adap- tive Markov Decision Process (BAMDP) [15]. By leveraging a variational autoencoder to reconstruct both next states and rewards, EAStream infers a probabilistic belief distribution thatcapturestheenvironmentaldynamics.Thisenablestheagent to reason about uncertainty and adapt substantially better to unseen, non-stationary network conditions. In summary, the main contributions of this paper are as follows: r We innovatively adopted the Dynamic Adaptive Streaming over HTTP (DASH) architecture for video streaming, opti- mizing dynamic ABR decisions through a Bayesian Adap- tive Markov Decision Process (BAMDP) (Section III).

**Fragmento 8 - p. 2 - score 4:**

By treating unknown parameters such as network bandwidth as random variables and maintaining a probability dis- tribution (posterior distribution) for them, the algorithm not only makes decisions based on the current estimated bandwidth, but also based on the complete state of all pos- sible bandwidth states and their occurrence probabilities, making ABR decisions more robust in dynamic network environments. r We propose EAStream (Section IV), a novel environment- aware ABR framework based on meta-reinforcement learning. Unlike optimization-based meta-learning meth- ods that require online ﬁne-tuning, EAStream leverages a context-based mechanism to adapt to new environments in real-time without any gradient updates during deployment.

**Fragmento 9 - p. 3 - score 4:**

In a different structure, MetaABR [14] extracts latent contexts from historical trajectories to adjust policies without online gradient updates. However, it relies on deterministic embeddings, ignoring the inherent uncertainty in bandwidth evolution. In contrast, our proposed EAStream formulates the ABR problem as a BAMDP. By inferring a probabilistic belief over the environment via a VAE, our method explicitly models un- certainty, enabling robust zero-shot adaptation to unseen condi- tions. III. METHODS This section formulates the ABR decision process as an optimization task and models the network uncertainty using a BAMDP. We then propose a Meta-RL-based ABR algorithm, called EAStream, to approximate the BAMDP policy.

**Fragmento 10 - p. 4 - score 4:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1179 Fig. 1. A schematic representation of the Dynamic Adaptive Streaming over HTTP (DASH) architecture. These prepared chunks and MPD ﬁles are often hosted on a Content Delivery Network (CDN) [42] for efﬁcient delivery. When the client player starts playing a video, it will ﬁrst request the MPD ﬁle, which will inform the client of the URL to request the video. The player then dynamically requests video chunks sequentially. For each chunk n, the ABR algorithm selects a bitrate Rn ∈R. The bitrate selection determines the chunk size dn(Rn), which is then downloaded from the CDN through a network with an average throughput of Cn.

**Fragmento 11 - p. 5 - score 4:**

. (10) The strategy that achieves this goal is termed a Bayes-optimal policy. While this problem can theoretically be addressed via methods like posterior sampling [43] or Bayesian planning [44], these approaches typically incur prohibitive computational over- head for real-time ABR decisions. Computing exact belief up- dates is also generally infeasible in practice. Therefore, we leverageameta-reinforcementlearningparadigmtotacklethis issue, as detailed below. C. Approximating Bayes-Optimal Policies Via Meta-Learning The theoretical solution for BAMDP is computationally difﬁ- cult.Ourapproach,EAStream,employsameta-learningstrategy inspiredbyVariBAD[45]toacquireasolutionthatapproximates this policy. In the meta-learning framework, we model different network environments as individual tasks, each deﬁned by a hidden latent variable mi. This latent variable corresponds to the belief in BAMDP. Since the latent variable is unknown, the agent must infer information about mi from its historical information. Speciﬁcally,weemployanencodertotransformthetrajectoryτ:t into an inferred distribution qφ(m|τ:t) within the latent space. This distribution serves as an inference of the environment’s latent features. The learning process uses the framework of Variational Au- toencoder (VAE) [46]. We optimize the encoder network by maximizing the Variational Lower Bound (ELBO): ELBO = Eρ  Eqφ(m|τ:t)[log pθ(τ:H|m)] −DKL(qφ(m|τ:t)||pθ(m))] . (11) Here, ρ denotes the trajectory distribution induced by the current policy π and the initial state distribution ρ0. This equation consists of two components. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 12 - p. 12 - score 4:**

Finally, in extreme outlier scenarios that deviate signiﬁcantly from the training distribution, the inferred belief may become inaccurate. As noted in Section VI, leveraging the reconstruction error for anomaly detection offers a promising avenue to mitigate this issue in future work. VI. CONCLUSION This paper presents EAStream, a context-based meta- reinforcement learning framework designed to address the gen- eralization challenge in adaptive bitrate streaming. By modeling theproblemasaBAMDPandutilizingavariationalautoencoder, EAStream infers latent beliefs about network dynamics from interactionhistory.Thismechanismenablesthepolicytoachieve zero-shot adaptation to unseen network conditions without re- quiring computationally expensive online ﬁne-tuning.

**Fragmento 13 - p. 1 - score 3:**

To address this, Model Predictive Control (MPC) [7] was introduced to enable proactive decision-making by optimizing QoE over a future horizon based on throughput predictions. Although MPC generally outperforms heuristics, its reliability heavily depends on the accuracy of bandwidth estimation. In recent years, considerable attention has been directed to- wards applying learning-based methods to ABR streaming [8], [9], [10], [11]. In contrast to traditional heuristic-based meth- ods, learning-based methods typically train neural networks on datasets spanning multiple network conditions. This allows them to capture the complicated correlations in video streaming.

**Fragmento 14 - p. 2 - score 3:**

These are primarily categorized into two classes: rate- based and buffer-based. Rate-based algorithms, such as FES- TIVE [5], guide their decisions by measuring historical network throughput. To address the lag problem of rate-based methods, buffer-based algorithms use buffer occupancy as a key metric. BBA [6] matches bitrate actions by setting different buffer thresholds. The more sophisticated algorithm BOLA [16] is based on Lyapunov optimization to maximize the QoE while ensuring that the buffer is not exhausted. Although the heuristic methodissimpleandeffective,theﬁxedrulesalsolimititsability to adapt to the dynamic and unstable network environment.

**Fragmento 15 - p. 3 - score 3:**

More advanced methods like PEARL [41] extend this by training a probabilistic encoder to infer latent context variables from off-policy data, signiﬁcantly improving meta-training sample efﬁciency. Several recent works have applied optimization-based meta- learning to the ABR problem, requiring an online training phase to adapt. For instance, A2BR [12] employs a MAML- based framework to learn a meta-policy ofﬂine, which is then rapidly ﬁne-tuned online to create a tailor-made policy for speciﬁc network conditions. Similarly, MMVS [13] integrates the MAML-based framework with PPO to handle highly ﬂuc- tuating networks, and proposes a meta advantage normalization technique to stabilize the online adaptation process.

**Fragmento 16 - p. 3 - score 3:**

DeepBuffer [21] jointly controls the maximum buffer size to avoid unnecessary bandwidth consumption. GreenABR+ [22] employsaDDPG-basedapproachtoreducepowerconsumption. BE-ABR [23] uses Transformer-based prediction to minimize data waste. DRL has also been tailored for speciﬁc environments. In mobile edge computing (MEC), Guo et al. [24] jointly optimize transcoding and bitrate decisions. QAVA [25] addresses the fairness problem among multiple clients. Moreover, researchers tackle speciﬁc application challenges: CAST [26] prioritizes intricate video scenes, L2AC-E [27] minimizes latency for live streaming, and DeepVR [28] predicts user ﬁeld-of-view for panoramic video.

**Fragmento 17 - p. 3 - score 3:**

Other works focus on improving adaptation in high-dimensional parameter spaces. For instance, LEO [39] decouples the adaptation from the high-dimensional parameter space via the construction of a latent embedding con- ditioned on the data and conducting the meta-learning updates in this low-dimensional space. In contrast, context-based methods learn a single policy con- ditioned on a task-speciﬁc context variable, which summarizes the agent’s interaction history and enables adaptation without test-time gradient updates. A pioneering approach, RL2 [40], uses a recurrent neural network (RNN) to implicitly infer the en- vironment’s underlying dynamics.

**Fragmento 18 - p. 4 - score 3:**

. . , N}. (6) The constraints of this formulation model the core dynamics of a streaming session: r Time Evolution: The ﬁrst constraint describes the change of the next decision point tn+1. The next time point equates to the sum of the current time tn, the download time T(Rn), and the possible rebuffering time Tn. r Network Throughput: The second constraint is the average network throughput ˆCn when downloading chunk n. It is calculated by integrating the instantaneous throughput c(t) with the actual download time. r Buffer Dynamics: The third constraint represents the change of buffer occupancy. Speciﬁcally, L represents the ﬁxed duration of a chunk.

**Fragmento 19 - p. 5 - score 3:**

1180 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 The buffer level Bn is always capped between zero and a maximum capacity Bmax. Finally, the chosen bitrate Rn must belong to the discrete set of available bitrates R. B. Bayesian Adaptive Modeling for Environmental Uncertainty To solve the problem, a common and effective approach is to use Reinforcement Learning (RL) based on a Markov Decision Process (MDP). The system consists of (S, A, R, P, ρ0, γ, H). Here, P is the state transition function and ρ0 is the initial state distribution. The agent’s objective is to learn a policy π that maximizes the long-term cumulative reward: J(π) = Eρ0,P,π H−1  t=0 γtR(rt+1|st, at, st+1)

**Fragmento 20 - p. 6 - score 3:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1181 Fig. 2. Overall Architecture of the EAStream Framework. The system comprises two main modules: a Belief Inference Module responsible for learning environmental awareness, and a DRL Policy Module for adaptive decision-making. The ﬁrst is the reconstruction likelihood. Crucially, the decoder pθ is tasked with predicting the entire trajectory τ:H based on the latent belief m. This forces m to capture the un- derlying predictive dynamics of the network, rather than merely compressing interaction history. Using the Markov property, this likelihood decomposes into: log pθ(τ:H|m) = log pθ(s0|m) + H−1  t=0 [log pθ(st+1|st, at, m) + log pθ(rt+1|st, at, st+1, m)].

**Fragmento 21 - p. 6 - score 3:**

(12) This factorization allows the model to iteratively predict the next state and reward at each time step, enforcing a precise modeling of the step-wise dynamics. The second component is the KL divergence, which acts as a regularizer. It constrains the learned posterior qφ to remain close to the prior p(m) (typically a standard Gaussian), ensuring a smooth latent space that facilitates stable policy optimization. Based on the inferred belief, the DRL policy πψ is optimized to approximate a Bayes-Optimal policy. At each timestep t, a latent variable mt is sampled from the current belief distribution, mt ∼qφ(m|τ:t). The policy then takes the current physical state st and the latent variable as input, denoted as πψ(at|st, mt).

**Fragmento 22 - p. 6 - score 3:**

A. System Architecture Overview The EAStream framework consists of two core modules: a be- lief inference module responsible for environmental awareness, and a policy module for decision-making. The overall EAStream architecture is illustrated in Fig. 2 . The belief inference module is designed based on the prin- ciples of VAE. It comprises two modules: a recurrent Be- lief Encoder and a predictive Decoder. The Belief Encoder processes the agent’s historical interaction trajectory (τt = (s0, a0, r1, . . . , st)) to infer a latent variable, m. This latent vari- able m represents its probabilistic belief regarding the hidden characteristics of the current network conditions.


### 8.3. accion decision abr

Palabras clave usadas: `action, bitrate, quality level, representation, decision, select, selection, guidance, recommendation, adaptation, cap, mask, quality, download, chunk, rate`

**Fragmento 1 - p. 4 - score 8:**

The goal of the ABR algorithm is to optimize the long-term QoE of users. QoE evaluates the subjective satisfaction of users, which is composed of three components: video quality, rebuffer- ing, and quality ﬂuctuations. Video Quality: The video quality reﬂects the perceived visual quality derived from the bitrate Rn of each video chunk. Users tend to watch videos with high average visual quality. It is calculated based on the sum of the n-th chunk: QoEqual = N  n=1 q(Rn), (1) where q(Rn) represents the video quality level for the bitrate Rn. The selection of q(Rn) commonly includes the raw bitrate Rn and a logarithmic mapping log(Rn) to reﬂect diminishing returns of higher bitrate.

**Fragmento 2 - p. 4 - score 7:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1179 Fig. 1. A schematic representation of the Dynamic Adaptive Streaming over HTTP (DASH) architecture. These prepared chunks and MPD ﬁles are often hosted on a Content Delivery Network (CDN) [42] for efﬁcient delivery. When the client player starts playing a video, it will ﬁrst request the MPD ﬁle, which will inform the client of the URL to request the video. The player then dynamically requests video chunks sequentially. For each chunk n, the ABR algorithm selects a bitrate Rn ∈R. The bitrate selection determines the chunk size dn(Rn), which is then downloaded from the CDN through a network with an average throughput of Cn.

**Fragmento 3 - p. 1 - score 6:**

Digital Object Identiﬁer 10.1109/TSC.2026.3671090 component of global Internet trafﬁc. According to the Global Internet Phenomena Report 2024 [1], the trafﬁc transporting video accounts for 68% and 64% of the total downlink trafﬁc of ﬁxed and mobile networks, respectively. Given the industry’s projected growth to $416.84 billion by 2030 [2], ensuring a superiorQualityofExperience(QoE)iscriticalforuserretention and business success. To achieve this, Adaptive Bitrate (ABR) technology has been widely adopted as the standard delivery mechanism [3], [4]. By dividing videos into chunks available at multiple quality levels, ABR algorithms dynamically select the optimal bitrate for each chunk based on real-time network throughput and buffer occupancy.

**Fragmento 4 - p. 1 - score 6:**

However, the ABR algorithm faces challenges because it needs to balance conﬂicting ob- jectives: maximizing video quality and minimizing playback interruptions. Speciﬁcally, high bitrate chunks will be selected for better playback quality. However, it will increase the risk of playback stalls, especially in the case of unstable network conditions. Traditional ABR algorithms primarily rely on ﬁxed rules or control-theoretic models. Heuristic-based approaches, such as the rate-based FESTIVE [5] and the buffer-based BBA [6], make decisions using predeﬁned thresholds. While computationally efﬁcient and easy to deploy, these rule-based methods lack the ﬂexibility to adapt to diverse network scenarios or varying QoE preferences.

**Fragmento 5 - p. 7 - score 6:**

▷Action: In an ABR system, the agent’s task is to select the video quality for the subsequent chunk. The action space A is thus formulated as a discrete set: A = {0, 1, . . . , K −1}. (15) Here, K represents the number of candidate bitrates. These discrete options correspond to different video resolutions such as 360p, 480p, 720p, and 1080p. ▷Reward: To optimize the QoE objective in (5), we deﬁne the reward function rt accordingly. Once the t-th video chunk has been successfully transmitted, the agent will receive a reward of rt: rt = μ1 · q(Rt) −μ2 · Tt −μ3 · |q(Rt) −q(Rt−1)|. (16) This reward function directly guides the behavior of the agent. It enables agent to learn strategies for choosing high-quality chunks while reducing rebuffering and bitrate changes.

**Fragmento 6 - p. 7 - score 6:**

Vector-based inputs, including the throughput history ⃗xt, download time history ⃗τt, and the vec- tor of next chunk sizes ⃗nt, are fed into one-dimensional convo- lutional layers to capture temporal features. Concurrently, scalar inputs, including the buffer occupancy bt, remaining chunks ct, and the last selected bitrate lt, are processed by dedicated fully connected layers. These features are then concatenated with the latent belief mt. The resulting high-dimensional feature vector serves as the input to two independent networks. The Actor Network, a multi-layer network with a ﬁnal Softmax activation, maps these features to a probability distribution corresponding to the bitrates.

**Fragmento 7 - p. 9 - score 6:**

1184 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 ▷Video Parameters: The video content selected for our experiments is the “EnvivioDash3” test sequence [48]. It has a total duration of 193 seconds and is segmented into 48 chunks, each with a playback time of approximately 4 seconds. Each chunk is pre-encoded into six different bitrate levels to facilitate adaptive streaming: 300, 750, 1200, 1850, 2850, and 4300 kbps. ▷Baseline Algorithms: We select several state-of-the-art ABR algorithms that represent different design paradigms for comparison: r BOLA [16]: A buffer-based algorithm based on Lyapunov optimization. This algorithm ensures that the video quality is maximized while guaranteeing the stability of the buffer.

**Fragmento 8 - p. 11 - score 6:**

1186 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 Fig. 7. CDF of QoElin scores on the in-distribution Hybrid test set (3G, FCC, 4GSyd). Fig. 8. CDF of QoElog scores on the in-distribution Hybrid test set (3G, FCC, 4GSyd). Fig. 9. CDF of QoE scores on the out-of-distribution test sets (Oboe and 4GNy). Fig. 10. Bitrate selection of EAStream, Pensieve, and RobustMPC on the bandwidth drop trace. uninformative due to over-regularization, known as posterior collapse. The results conﬁrm that a moderate latent dimension and KL coefﬁcient provide the best balance for the latent belief representation. Fig. 11. t-SNE visualization of the latent belief vectors collected from three distinct network datasets.

**Fragmento 9 - p. 12 - score 6:**

2485–2503, Aug. 2022. [13] S. Wang, J. Lin, and Y. Dai, “MMVS: Enabling robust adaptive video streaming for wildly ﬂuctuating and heterogeneous networks,” IEEE Trans. Multimedia, vol. 26, pp. 11018–11030, 2024. [14] W. Li, X. Li, Y. Xu, Y. Yang, and S. Lu, “MetaABR: A meta-learning approach on adaptative bitrate selection for video streaming,” IEEE Trans. Mobile Comput., vol. 23, no. 3, pp. 2422–2437, Mar. 2024. [15] M. O. Duff, “Optimal Learning: Computational procedures for Bayes- adaptive Markov decision processes,” Univ. Massachusetts Amherst, Amherst, MA, USA, 2002. [16] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal bitrate adaptation for online videos,” IEEE/ACM Trans.

**Fragmento 10 - p. 1 - score 5:**

The seminal method, Pensieve [8], uses deep reinforcement learning algorithm (DRL) to learn bitrate adaptation policies. Unlike the MPC-based methods that rely on system models, the DRL algorithm directly learns the model-free strategies from experience, enabling it to better handle dynamic networks. Furthermore, DRL algorithms have long-term planning capa- bilities, which allows them to make complex strategic trade- offs that balance instant video quality and long-term viewing stability. 1939-1374 © 2026 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission.

**Fragmento 11 - p. 1 - score 5:**

Although some meta-reinforcement learning techniques have been proposed to mitigate this issue, they generally depend on additional online training or ﬁne-tuning. To overcome these lim- itations, this paper introduces EAStream, an environment-aware ABR algorithm based on meta-reinforcement learning for reliable video streaming services. The method employs a variational au- toencoder to extract a latent representation of the current network environment from historical interaction data. This latent variable, along with the current system state, is fed into a policy network that perceives network conditions in real time and adapts bitrate decisions accordingly, without requiring further online training.

**Fragmento 12 - p. 4 - score 5:**

Therefore, the ABR decision-making process can be modeled as an optimization task subject to constraints. The task is to de- termine the optimal sequence of bitrates R = (R1, R2, . . ., RN) that maximizes the total QoE, subject to the system’s dynamic constraints. This objective balances aggressive bitrate selection against the physical constraints of buffer dynamics, ensuring that the stochastic network supply meets the deterministic playback demand. Mathematically, this is formulated as: maxR1,...,RN QoE, s.t. ⎧ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎨ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎩ tn+1 = tn + T(Rn) + Tn, ˆCn = 1 T (Rn)  tn+T (Rn) tn c(t)dt, Bn+1 = max(0, Bn −T(Rn)) + L, B1 = Ts, 0 ≤Bn ≤Bmax, Rn ∈R, ∀n ∈{1, .

**Fragmento 13 - p. 5 - score 5:**

, (7) where H denotes the time horizon of a video streaming ses- sion, and γ ∈[0, 1] is the discount factor that determines the importance of future rewards. However, a core limitation of the standard MDP lies in its assumption of a stationary or perfectly known transition function P(st+1|st, at). This assumption is frequently violated in real-world networks, where conditions like bandwidth are highly dynamic and non-stationary. An ABR agent trained under one speciﬁc network trace may fail to generalize to other ﬂuctuating network conditions, leading to suboptimal performance. To address this limitation, where the true dynamics of the environment are unknown, we model the ABR problem as a Bayes-Adaptive Markov Decision Process (BAMDP) [15]. In a standard MDP, the agent assumes the network follows a ﬁxed rule. In contrast, a BAMDP agent acknowledges its ignorance about the speciﬁc network scenario. It maintains a belief state—a probabilistic “mental model” of the current net- work environment. As the agent observes new state transitions, it recursively updates this belief, allowing it to adapt its strategy dynamically based on its conﬁdence in the environment’s state. In this framework, the unknown network dynamics are treated as a latent variable. The agent maintains a belief state, bt, deﬁned as the posterior distribution over these possible network environments given the interaction history τ:t. The decision-making process in a BAMDP extends the stan- dard MDP cycle by incorporating a belief update step. The process proceeds as follows: 1) State Representation: At each timestep t, the agent’s state is a hyper-state s+ t = (st, bt), consisting of the observable physical state st and the current belief bt. 2) Action & Observation: The agent selects an action at. The env

**Fragmento 14 - p. 5 - score 5:**

1180 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 The buffer level Bn is always capped between zero and a maximum capacity Bmax. Finally, the chosen bitrate Rn must belong to the discrete set of available bitrates R. B. Bayesian Adaptive Modeling for Environmental Uncertainty To solve the problem, a common and effective approach is to use Reinforcement Learning (RL) based on a Markov Decision Process (MDP). The system consists of (S, A, R, P, ρ0, γ, H). Here, P is the state transition function and ρ0 is the initial state distribution. The agent’s objective is to learn a policy π that maximizes the long-term cumulative reward: J(π) = Eρ0,P,π H−1  t=0 γtR(rt+1|st, at, st+1)

**Fragmento 15 - p. 6 - score 5:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1181 Fig. 2. Overall Architecture of the EAStream Framework. The system comprises two main modules: a Belief Inference Module responsible for learning environmental awareness, and a DRL Policy Module for adaptive decision-making. The ﬁrst is the reconstruction likelihood. Crucially, the decoder pθ is tasked with predicting the entire trajectory τ:H based on the latent belief m. This forces m to capture the un- derlying predictive dynamics of the network, rather than merely compressing interaction history. Using the Markov property, this likelihood decomposes into: log pθ(τ:H|m) = log pθ(s0|m) + H−1  t=0 [log pθ(st+1|st, at, m) + log pθ(rt+1|st, at, st+1, m)].

**Fragmento 16 - p. 8 - score 5:**

To encourage exploration, we incorporate an automatic entropy adjustment mechanism. The ﬁnal policy loss combines the clipped loss, the value function loss LVF, and the entropy bonus: L(ψ) = ˆEt  −LCLIP(ψ) + LVF(ψ) −αH[πψ](st, mt)  . (18) Algorithm 2: Online Adaptation. 1: Load qφ and policy πψ. 2: Initialize recurrent hidden state h0. 3: for t = 1, 2, . . . , N do 4: // Belief Inference 5: Update ht ←RNNφ(ht−1, (at−1, rt, st)). 6: Sample belief from encoder mt ∼qφ(ht). 7: // Policy Decision 8: Observe current state st. 9: Select action at ∼πψ(at|st, mt). 10: // Environment Interaction 11: Execute at, observe st+1, rt+1. 12: end for Crucially, gradients from the policy update are not backprop- agated to the belief module.

**Fragmento 17 - p. 9 - score 5:**

r FESTIVE [5]: A rate-based heuristic algorithm. This al- gorithm uses the harmonic average of the nearest chunks download rates for throughput estimation. r RobustMPC [7]: An algorithm based on the theory of MPC. This algorithm predicts the future optimal sequence by combining throughput estimation and buffer informa- tion. r Pensieve [8]: A state-of-the-art ABR algorithm leveraging deep reinforcement learning. r NetLLM [33]: The ﬁrst framework using LLMs for net- working tasks through ﬁne-tuning to enhance generaliza- tion and performance. r Comyco [9]: A quality-aware ABR method based on im- itation learning. It trains the neural network by imitating the expert actions.

**Fragmento 18 - p. 1 - score 4:**

1176 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 EAStream: An Environment-Aware Adaptive Bitrate Algorithm for Reliable Video Streaming Services Zeming Huang, Wenjing Xiao , Miaojiang Chen , Member, IEEE, Zhiquan Liu , Min Chen , Fellow, IEEE, Athanasios V. Vasilakos , Senior Member, IEEE, Ahmed Farouk , and Houbing Herbert Song , Fellow, IEEE Abstract—Video streaming has emerged as a widely used Inter- net service, in which adaptive bitrate (ABR) algorithms play a crit- ical role in delivering high quality of experience (QoE). However, existing learning-based ABR methods often suffer from limited generalization in unseen and dynamically changing network condi- tions.

**Fragmento 19 - p. 2 - score 4:**

These are primarily categorized into two classes: rate- based and buffer-based. Rate-based algorithms, such as FES- TIVE [5], guide their decisions by measuring historical network throughput. To address the lag problem of rate-based methods, buffer-based algorithms use buffer occupancy as a key metric. BBA [6] matches bitrate actions by setting different buffer thresholds. The more sophisticated algorithm BOLA [16] is based on Lyapunov optimization to maximize the QoE while ensuring that the buffer is not exhausted. Although the heuristic methodissimpleandeffective,theﬁxedrulesalsolimititsability to adapt to the dynamic and unstable network environment.

**Fragmento 20 - p. 3 - score 4:**

A. Problem Formulation As shown in Fig. 1, a typical ABR streaming system involves complex video content preparation and delivery. The server ﬁrst encodes the raw video into multiple bitrate levels, each corresponding to a discrete value in the set R. Each of these transcoded videos is then split into a series of N smaller chunks, all sharing a ﬁxed duration of L seconds. Simultaneously, a manifest ﬁle named Media Presentation Description (MPD) is created to provide metadata for the video stream. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 21 - p. 7 - score 4:**

This allows the policy to learn not just one ﬁxed strategy, but a highly adaptive meta-policy. B. State, Action, and Reward Deﬁnition To train the DRL agent, this section explicitly deﬁnes the reward function, as well as the state and action space. ▷State: For every time step t, the agent receives a state st. This state is a multi-dimensional vector that includes in- formation about the playback status and network conditions. Following the design of Pensieve [8], we formulate the state st as follows: st = (⃗xt, ⃗τt, ⃗nt, bt, ct, lt). (14) Here, ⃗xt and ⃗τt are vectors representing the historical throughput and transmission time of the past w video chunks(We set w = 8 following the standard conﬁguration in [8].); ⃗nt denotes the ﬁle size for K available bitrates of next chunk; bt is the current buffer occupancy; ct denotes the number of unplayed chunks; and lt denotes the last chunk’s bitrate.

**Fragmento 22 - p. 7 - score 4:**

1182 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 Fig. 4. Architecture of the DRL Policy Module. potential dynamics of the network environment rather than merely compressing past information. The second part is the DRL strategy responsible for action selection. The objective is to learn a near-optimal strategy π(at|st, mt), which takes in the current state and belief and outputs an action that maximizes the long-term cumulative QoE reward. Unlike traditional DRL-based agents, our policy network is conditional on state st and belief mt. This dual- input structure is the key to achieving adaptability. The state st provides the most recent state of the environment, while the belief mt provides richer, history-based information about the environment.


### 8.4. reward qoe objetivo

Palabras clave usadas: `reward, QoE, quality of experience, utility, objective, loss, rebuffer, stall, stalling, smoothness, switching, quality variation, latency, fairness, bitrate smoothness, video quality, tail, risk, severe`

**Fragmento 1 - p. 4 - score 6:**

Rebuffering Penalty: Rebuffering, or playback stalling, occurs when the playback buffer is depleted, severely degrading the user’s viewing experience. Let ˆCn denotes the average network throughput. The rebuffering time for chunk n, denoted as Tn, is thedurationbywhichitsdownloadtime,T(Rn) = dn(Rn)/ ˆCn, exceeds the buffer occupancy Bn−1 just before the download begins. It is calculated as: Tn = max {T(Rn) −Bn−1, 0} . (2) The total rebuffering penalty is the sum of all stall durations throughout the session: QoErebuf = N  n=1 Tn. (3) Quality Fluctuations Penalty: Frequent and large variations in video quality between consecutive chunks can be jarring to the user.

**Fragmento 2 - p. 7 - score 5:**

▷Action: In an ABR system, the agent’s task is to select the video quality for the subsequent chunk. The action space A is thus formulated as a discrete set: A = {0, 1, . . . , K −1}. (15) Here, K represents the number of candidate bitrates. These discrete options correspond to different video resolutions such as 360p, 480p, 720p, and 1080p. ▷Reward: To optimize the QoE objective in (5), we deﬁne the reward function rt accordingly. Once the t-th video chunk has been successfully transmitted, the agent will receive a reward of rt: rt = μ1 · q(Rt) −μ2 · Tt −μ3 · |q(Rt) −q(Rt−1)|. (16) This reward function directly guides the behavior of the agent. It enables agent to learn strategies for choosing high-quality chunks while reducing rebuffering and bitrate changes.

**Fragmento 3 - p. 1 - score 4:**

However, the ABR algorithm faces challenges because it needs to balance conﬂicting ob- jectives: maximizing video quality and minimizing playback interruptions. Speciﬁcally, high bitrate chunks will be selected for better playback quality. However, it will increase the risk of playback stalls, especially in the case of unstable network conditions. Traditional ABR algorithms primarily rely on ﬁxed rules or control-theoretic models. Heuristic-based approaches, such as the rate-based FESTIVE [5] and the buffer-based BBA [6], make decisions using predeﬁned thresholds. While computationally efﬁcient and easy to deploy, these rule-based methods lack the ﬂexibility to adapt to diverse network scenarios or varying QoE preferences.

**Fragmento 4 - p. 3 - score 3:**

1178 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 Pensieve [8] employs Deep Reinforcement Learning (DRL) and outperforms traditional algorithms. The success of Pensieve has motivated a series of studies on Learning-based ABR algorithms. For instance, Comyco [9] employs imitation learning to enhance sample efﬁciency. Tiyuntsong [19] introduces a self-play framework to clearly deﬁne the optimization objective. Another major direction focuses on jointly optimizing bitrate with other metrics. Early works like AMIS [20] manage both bi- trate and playout speed to mitigate the risk of rebuffering. Recent studies extend these objectives to energy and trafﬁc efﬁciency.

**Fragmento 5 - p. 3 - score 3:**

DeepBuffer [21] jointly controls the maximum buffer size to avoid unnecessary bandwidth consumption. GreenABR+ [22] employsaDDPG-basedapproachtoreducepowerconsumption. BE-ABR [23] uses Transformer-based prediction to minimize data waste. DRL has also been tailored for speciﬁc environments. In mobile edge computing (MEC), Guo et al. [24] jointly optimize transcoding and bitrate decisions. QAVA [25] addresses the fairness problem among multiple clients. Moreover, researchers tackle speciﬁc application challenges: CAST [26] prioritizes intricate video scenes, L2AC-E [27] minimizes latency for live streaming, and DeepVR [28] predicts user ﬁeld-of-view for panoramic video.

**Fragmento 6 - p. 4 - score 3:**

The ﬂuctuations penalty is calculated by accumulating the absolute variations in quality value across consecutive chunks. QoEvar = N  n=2 |q(Rn) −q(Rn−1)| . (4) QoE Objective: The ﬁnal QoE objective is deﬁned as a linear combination of these three components: QoE = μ1QoEqual −μ2QoErebuf −μ3QoEvar, (5) where µ = (μ1, μ2, μ3) is a vector of non-negative weighting coefﬁcients. These coefﬁcients are customizable hyperparam- eters representing different user preferences. For instance, in- creasing μ2 will penalize rebuffering more heavily, guiding the algorithm towards a more conservative strategy to ensure smooth playback. In our experiments, we adopt standard ﬁxed settings for fair comparison.

**Fragmento 7 - p. 4 - score 3:**

The goal of the ABR algorithm is to optimize the long-term QoE of users. QoE evaluates the subjective satisfaction of users, which is composed of three components: video quality, rebuffer- ing, and quality ﬂuctuations. Video Quality: The video quality reﬂects the perceived visual quality derived from the bitrate Rn of each video chunk. Users tend to watch videos with high average visual quality. It is calculated based on the sum of the n-th chunk: QoEqual = N  n=1 q(Rn), (1) where q(Rn) represents the video quality level for the bitrate Rn. The selection of q(Rn) commonly includes the raw bitrate Rn and a logarithmic mapping log(Rn) to reﬂect diminishing returns of higher bitrate.

**Fragmento 8 - p. 6 - score 3:**

Consequently, the agent can adapt its decision-making process in response to the estimated hidden dynamics. The overall training objective is to optimize the combined objective: L(φ, θ, ψ) = Ep(M) [J(ψ, φ) + λ · ELBO(φ, θ)] , (13) where Ep(M) denotes the expectation over the task distribution p(M). In this equation, J(ψ, φ) denotes the expected return for approximate policy, and the second term is the task inference objective. The hyperparameter λ controls the trade-off between maximizing the RL reward and the accuracy of belief recon- struction. Fig. 3. Architecture of the Belief Inference Module. IV. SYSTEM DESIGN This section details the architecture and training methodol- ogy of EAStream, our proposed meta-reinforcement learning framework for adaptive bitrate streaming.

**Fragmento 9 - p. 7 - score 3:**

1182 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 Fig. 4. Architecture of the DRL Policy Module. potential dynamics of the network environment rather than merely compressing past information. The second part is the DRL strategy responsible for action selection. The objective is to learn a near-optimal strategy π(at|st, mt), which takes in the current state and belief and outputs an action that maximizes the long-term cumulative QoE reward. Unlike traditional DRL-based agents, our policy network is conditional on state st and belief mt. This dual- input structure is the key to achieving adaptability. The state st provides the most recent state of the environment, while the belief mt provides richer, history-based information about the environment.

**Fragmento 10 - p. 8 - score 3:**

The encoder and decoder (φ, θ) are updated independently by sampling trajectories from a separate replay buffer. The objective is to minimize the ELBO loss derived in (11), which aggregates the state reconstruction loss, reward prediction loss, and the KL divergence regularization term. ▷Online Adaptation: When deployed to the client, the model willadaptonlineinthenewnetworkenvironment.Whenrunning online, there is no need for real-time gradient updates or training. The adaptability of policy is achieved entirely through real-time inference. Initially, the latest interaction tuple (at−1, rt, st) is fed into the Belief Encoder qφ to update the recurrent hidden state ht.

**Fragmento 11 - p. 1 - score 2:**

1176 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 EAStream: An Environment-Aware Adaptive Bitrate Algorithm for Reliable Video Streaming Services Zeming Huang, Wenjing Xiao , Miaojiang Chen , Member, IEEE, Zhiquan Liu , Min Chen , Fellow, IEEE, Athanasios V. Vasilakos , Senior Member, IEEE, Ahmed Farouk , and Houbing Herbert Song , Fellow, IEEE Abstract—Video streaming has emerged as a widely used Inter- net service, in which adaptive bitrate (ABR) algorithms play a crit- ical role in delivering high quality of experience (QoE). However, existing learning-based ABR methods often suffer from limited generalization in unseen and dynamically changing network condi- tions.

**Fragmento 12 - p. 2 - score 2:**

Optimization-based methods [12], [13] learn an adaptable initialization but typically rely on online gradient updates during playback. This requirement introduces signiﬁcant computational overhead and latency, making them less ideal for resource-constrained devices. Conversely, the context-based method [14] adapts by inferring a latent context vector from history without online gradient updates. However, it relies on deterministic embeddings supervised solely by reward signals, which limits their ability to model the uncertainty of stochastic networks and fails to capture the underlying state transition dynamics. To overcome these limitations, we propose EAStream, a novel probabilistic context-based framework.

**Fragmento 13 - p. 4 - score 2:**

Therefore, the ABR decision-making process can be modeled as an optimization task subject to constraints. The task is to de- termine the optimal sequence of bitrates R = (R1, R2, . . ., RN) that maximizes the total QoE, subject to the system’s dynamic constraints. This objective balances aggressive bitrate selection against the physical constraints of buffer dynamics, ensuring that the stochastic network supply meets the deterministic playback demand. Mathematically, this is formulated as: maxR1,...,RN QoE, s.t. ⎧ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎨ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎩ tn+1 = tn + T(Rn) + Tn, ˆCn = 1 T (Rn)  tn+T (Rn) tn c(t)dt, Bn+1 = max(0, Bn −T(Rn)) + L, B1 = Ts, 0 ≤Bn ≤Bmax, Rn ∈R, ∀n ∈{1, .

**Fragmento 14 - p. 5 - score 2:**

1180 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 The buffer level Bn is always capped between zero and a maximum capacity Bmax. Finally, the chosen bitrate Rn must belong to the discrete set of available bitrates R. B. Bayesian Adaptive Modeling for Environmental Uncertainty To solve the problem, a common and effective approach is to use Reinforcement Learning (RL) based on a Markov Decision Process (MDP). The system consists of (S, A, R, P, ρ0, γ, H). Here, P is the state transition function and ρ0 is the initial state distribution. The agent’s objective is to learn a policy π that maximizes the long-term cumulative reward: J(π) = Eρ0,P,π H−1  t=0 γtR(rt+1|st, at, st+1)

**Fragmento 15 - p. 5 - score 2:**

Belief Update . (8) The reward function for the hyper-state depends solely on the physical state transition, as the user’s QoE is derived from the actual physical states. Thus, it is deﬁned as: R+(s+ t , at, s+ t+1) = R(st, at, st+1), (9) where R(st, at, st+1) is the standard QoE reward deﬁned in (5). This reformulation transforms the original MDP into a BAMDP, denoted by M + = (S+, A, R+, P +, ρ+ 0 , γ, H). Con- sequently, our primary goal is to ﬁnd a policy π to maximize the accumulated long-term reward in the BAMDP: J+(π) = Eb0,ρ+ 0 ,P +,π H−1  t=0 γtR+(rt+1|s+ t , at, s+ t+1)

**Fragmento 16 - p. 7 - score 2:**

The output of GRU is subsequently passed through FC to generate the parameters of a Gaussian distribution, representing the posterior belief mt. The Decoder provides the training objective by using two separate networks to reconstruct the system’s dynamics. Speciﬁcally, consistent with the factorization of the trajectory likelihood in (12), a State Transition Head predicts the next state ˆst, while a Reward Head predicts the reward ˆrt. Both heads are implemented as fully connected layers. ▷DRL Policy Module: As shown in Fig. 4, this module is the agent’s core decision-making component and is implemented withanActor-Criticarchitecture.ItbeginswithaFeatureExtrac- tor that processes the raw state.

**Fragmento 17 - p. 8 - score 2:**

V. EVALUATION A. Experimental Setup ▷Implementation: We implement EAStream in PyTorch and optimize the model parameters using the Adam optimizer. For the policy and value network, the learning rate is set to 1 × 10−4. The PPO algorithm is conﬁgured with a clipping parameter of ϵ = 0.2, a reward discount factor of γ = 0.99 and a target entropy of Htarget = 0.1. For belief inference module (φ, θ), the learning rate is 1 × 10−3, and it is trained using a replay buffer with a capacity of 1000 trajectories and a batch size of 32. The weights for its loss function are set to λs = 1.0, λr = 1.0, and β = 0.1, respectively. The dimension of the latent belief m is set to 16.

**Fragmento 18 - p. 8 - score 2:**

13: For each τj, infer latent belief mj ∼qφ(m|τj). 14: // Calculate weighted loss components 15: Lstate = −Ej,t[log pθ(sj,t+1|sj,t, aj,t, mj)]. 16: Lreward = −Ej,t[log pθ(rj,t+1| . . . , mj)]. 17: LKL = Ej[DKL(qφ(m|τj)||p(m))]. 18: LELBO = λsLstate + λrLreward + βLKL 19: Update φ, θ by minimizing LELBO. 20: end for separation prevents the belief learning from being biased by the policy’s early exploration. In each training iteration, multiple parallel agents collect interaction trajectories. The collected data is used to update the policy and belief modules separately. The policy network is updated using the Proximal Policy Optimization (PPO) algorithm [47].

**Fragmento 19 - p. 9 - score 2:**

The speciﬁc deﬁnition is as follows: r QoElin This metric considers that the video quality in- creases linearly with the bitrate. r QoElog This metric considers a higher bitrate to have diminishing returns to perceptual quality. Table II provides a summary of the parameters used for each QoE metric. B. EAStream Vs. Existing ABR Algorithms In this section, we compare EAStream with the baseline algorithms. The test dataset includes in-distribution (Hybrid) and out-of-distribution (Oboe, 4GNY). We use bar charts to present the normalized average QoE scores in Figs. 5 and 6. We analyzed the performance distribution using CDF plots in Figs. 7, 8, and 9. ▷Performance on the Hybrid Test Set: We ﬁrst evaluate the performance of all algorithms on the in-distribution test set, which is composed of traces from the 3G, FCC, and 4GSyd Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 20 - p. 9 - score 2:**

5. Normalized average QoE comparison on the in-distribution Hybrid test set (3G, FCC, 4GSyd). on network conditions similar to those seen during train- ing. The 4GNY and Oboe datasets are kept entirely separate from the training process. They serve exclusively as out-of- distribution test sets to rigorously assess the generalization ca- pabilities of the pre-trained models in completely novel network environments. ▷QoE Metrics: To evaluate the algorithm performance based on different user preferences, we adopted two distinct QoE targets from Pensieve [8]. For learning-based algorithms (Pen- sieve, Comyco, NetLLM and EAStream), we train a dedicated model for each QoE objective.

**Fragmento 21 - p. 10 - score 2:**

While the sudden transition caused initial rebuffering for all algorithms due to high-bitrate inertia, EAStream recovered most effectively. It rapidly detected the deterioration, down- shifting to 300 kbps to stabilize playback before smoothly tran- sitioning upward as buffers replenished. Conversely, Pensieve and RobustMPC struggled with persistent rebuffering and fre- quent switching. This conﬁrms that EAStream’s environment- awareness mechanism facilitates superior long-term decision- making in dynamic networks. ▷Analysis of Latent Belief Space: We evaluated whether EAStream’s belief module learns meaningful environmental representations using t-SNE [54] visualization.

**Fragmento 22 - p. 1 - score 1:**

Digital Object Identiﬁer 10.1109/TSC.2026.3671090 component of global Internet trafﬁc. According to the Global Internet Phenomena Report 2024 [1], the trafﬁc transporting video accounts for 68% and 64% of the total downlink trafﬁc of ﬁxed and mobile networks, respectively. Given the industry’s projected growth to $416.84 billion by 2030 [2], ensuring a superiorQualityofExperience(QoE)iscriticalforuserretention and business success. To achieve this, Adaptive Bitrate (ABR) technology has been widely adopted as the standard delivery mechanism [3], [4]. By dividing videos into chunks available at multiple quality levels, ABR algorithms dynamically select the optimal bitrate for each chunk based on real-time network throughput and buffer occupancy.


### 8.5. entrenamiento optimizacion

Palabras clave usadas: `training, train, trained, episode, epoch, optimizer, learning rate, experience replay, fine-tune, fine-tuning, pretrain, pre-training, behavior cloning, imitation, expert, simulation, simulator, offline, online, curriculum, loss function, joint optimization, dataset, sample`

**Fragmento 1 - p. 12 - score 6:**

This conﬁrms that EAStream is suitable for resource- constrained client deployments. D. Discussion and Limitations Despite the demonstrated advantages, we acknowledge cer- tain limitations of the EAStream framework. First, the ofﬂine meta-training process incurs higher computational overhead compared to standard DRL methods due to the joint optimization of the belief inference and policy modules. However, this cost is strictly conﬁned to the ofﬂine phase and does not impact the low-latency requirements of online inference. Second, the algorithm’s generalization capability is inherently dependent on the diversity of the network traces used during meta-training; a narrow task distribution may limit the effective range of adaptation.

**Fragmento 2 - p. 8 - score 5:**

V. EVALUATION A. Experimental Setup ▷Implementation: We implement EAStream in PyTorch and optimize the model parameters using the Adam optimizer. For the policy and value network, the learning rate is set to 1 × 10−4. The PPO algorithm is conﬁgured with a clipping parameter of ϵ = 0.2, a reward discount factor of γ = 0.99 and a target entropy of Htarget = 0.1. For belief inference module (φ, θ), the learning rate is 1 × 10−3, and it is trained using a replay buffer with a capacity of 1000 trajectories and a batch size of 32. The weights for its loss function are set to λs = 1.0, λr = 1.0, and β = 0.1, respectively. The dimension of the latent belief m is set to 16.

**Fragmento 3 - p. 2 - score 4:**

Optimization-based methods [12], [13] learn an adaptable initialization but typically rely on online gradient updates during playback. This requirement introduces signiﬁcant computational overhead and latency, making them less ideal for resource-constrained devices. Conversely, the context-based method [14] adapts by inferring a latent context vector from history without online gradient updates. However, it relies on deterministic embeddings supervised solely by reward signals, which limits their ability to model the uncertainty of stochastic networks and fails to capture the underlying state transition dynamics. To overcome these limitations, we propose EAStream, a novel probabilistic context-based framework.

**Fragmento 4 - p. 3 - score 4:**

To address this, a recent work NetLLM [33] explores adapting Large Language Models (LLMs) as universal foundation models to handle diverse networking tasks. However, it introduces signiﬁcant computational overhead and latency, making it less ideal for real-time deployment on resource- constrained devices. C. Meta-Reinforcement Learning for Generalization Totackletheoverﬁttingproblem, meta-learningoffers alearn- ing paradigm [34]. Its core idea is to train on a distribution of related tasks to learn an inductive bias, enabling fast adaptation to new, unseen tasks with high sample efﬁciency at test time [35]. While conventional RL agents tend to overﬁt the training traces, Meta-Reinforcement Learning (Meta-RL) learns an adaptive policy that generalizes across different network environments from the task distribution [35].

**Fragmento 5 - p. 3 - score 4:**

More advanced methods like PEARL [41] extend this by training a probabilistic encoder to infer latent context variables from off-policy data, signiﬁcantly improving meta-training sample efﬁciency. Several recent works have applied optimization-based meta- learning to the ABR problem, requiring an online training phase to adapt. For instance, A2BR [12] employs a MAML- based framework to learn a meta-policy ofﬂine, which is then rapidly ﬁne-tuned online to create a tailor-made policy for speciﬁc network conditions. Similarly, MMVS [13] integrates the MAML-based framework with PPO to handle highly ﬂuc- tuating networks, and proposes a meta advantage normalization technique to stabilize the online adaptation process.

**Fragmento 6 - p. 9 - score 4:**

r 4GNY [53]: Collected on New York City’s public transit system (bus and subway), these traces represent highly variable urban mobile network conditions. We provide an overview of the primary characteristics for these datasets in Table I. For training our learning-based models (EAStream and Pen- sieve), we create a single, uniﬁed dataset to foster generalization. We combine the traces from the 3G, FCC, and 4GSyd sources to form a Hybrid dataset. From this Hybrid dataset, 80% of the traces are randomly sampled to constitute the training set. The remaining 20% of the Hybrid dataset is held out as the in-distribution test set, used to evaluate performance TABLE I CHARACTERISTICS OF NETWORK TRACE DATASETS TABLE II PARAMETERS FOR DIFFERENT QOE METRICS Fig.

**Fragmento 7 - p. 9 - score 4:**

5. Normalized average QoE comparison on the in-distribution Hybrid test set (3G, FCC, 4GSyd). on network conditions similar to those seen during train- ing. The 4GNY and Oboe datasets are kept entirely separate from the training process. They serve exclusively as out-of- distribution test sets to rigorously assess the generalization ca- pabilities of the pre-trained models in completely novel network environments. ▷QoE Metrics: To evaluate the algorithm performance based on different user preferences, we adopted two distinct QoE targets from Pensieve [8]. For learning-based algorithms (Pen- sieve, Comyco, NetLLM and EAStream), we train a dedicated model for each QoE objective.

**Fragmento 8 - p. 12 - score 4:**

Extensive experiments on real-world datasets demonstrate that EAStream not only matches state-of-the-art performance on in-distribution traces but signiﬁcantly outperforms existing baselines in out-of- distribution scenarios. In future work, we intend to explore the online utilization of the Belief Decoder, which is currently only reserved for ofﬂine training. Speciﬁcally, we plan to leverage the real-time reconstruction errors for anomaly detection to identify extreme network outliers. REFERENCES [1] Sandvine, “2024 Global internet phenomena report,” 2024. [Online]. Available: https://www.applogicnetworks.com/global-internet-phenom ena-report-2024 [2] G.

**Fragmento 9 - p. 1 - score 3:**

Although some meta-reinforcement learning techniques have been proposed to mitigate this issue, they generally depend on additional online training or ﬁne-tuning. To overcome these lim- itations, this paper introduces EAStream, an environment-aware ABR algorithm based on meta-reinforcement learning for reliable video streaming services. The method employs a variational au- toencoder to extract a latent representation of the current network environment from historical interaction data. This latent variable, along with the current system state, is fed into a policy network that perceives network conditions in real time and adapts bitrate decisions accordingly, without requiring further online training.

**Fragmento 10 - p. 5 - score 3:**

, (7) where H denotes the time horizon of a video streaming ses- sion, and γ ∈[0, 1] is the discount factor that determines the importance of future rewards. However, a core limitation of the standard MDP lies in its assumption of a stationary or perfectly known transition function P(st+1|st, at). This assumption is frequently violated in real-world networks, where conditions like bandwidth are highly dynamic and non-stationary. An ABR agent trained under one speciﬁc network trace may fail to generalize to other ﬂuctuating network conditions, leading to suboptimal performance. To address this limitation, where the true dynamics of the environment are unknown, we model the ABR problem as a Bayes-Adaptive Markov Decision Process (BAMDP) [15]. In a standard MDP, the agent assumes the network follows a ﬁxed rule. In contrast, a BAMDP agent acknowledges its ignorance about the speciﬁc network scenario. It maintains a belief state—a probabilistic “mental model” of the current net- work environment. As the agent observes new state transitions, it recursively updates this belief, allowing it to adapt its strategy dynamically based on its conﬁdence in the environment’s state. In this framework, the unknown network dynamics are treated as a latent variable. The agent maintains a belief state, bt, deﬁned as the posterior distribution over these possible network environments given the interaction history τ:t. The decision-making process in a BAMDP extends the stan- dard MDP cycle by incorporating a belief update step. The process proceeds as follows: 1) State Representation: At each timestep t, the agent’s state is a hyper-state s+ t = (st, bt), consisting of the observable physical state st and the current belief bt. 2) Action & Observation: The agent selects an action at. The env

**Fragmento 11 - p. 7 - score 3:**

In parallel, the Critic Network with a similar architecture outputs a state value estimation V (st, mt) to guide the learning of the actor. D. Ofﬂine Training and Online Adaptation This section details the learning and adaptation workﬂow of EAStream. The process consists of two stages summarized in Algorithm 1 and Algorithm 2 respectively. ▷Ofﬂine Meta-Training: This stage aims to learn a meta- policy capable of inferring environmental characteristics and adapting decisions across diverse network conditions. By ex- posing the agent to a wide variety of environments at this stage, we force it to learn how to identify potential network conditions rather than memorizing speciﬁc training trajectories.

**Fragmento 12 - p. 8 - score 3:**

Given this hidden state, the encoder performs forward passing to infer the belief mt. This belief represents the agent’s perception of the current network environment. Then the belief mt and the current state st are jointly input into the policy network πψ to decide the next chunk’s bitrate at. Finally, the agent performs the action and observes the new state and reward. During the entire online phase, the auxiliary decoder module is deprecated, and the agent operated in pure inference mode. Unlike the optimization-based meta-learning methods that require gradient updates during testing, our method relies solely on forward propagation. This structural design reduces computational overhead and makes it more suitable for resource-constrained client deployments.

**Fragmento 13 - p. 8 - score 3:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1183 Algorithm 1: Ofﬂine Meta-Training. 1: Initialize belief params φ, θ; policy params ψ; entropy weight α; target entropy Htarget; 2: Initialize replay buffer Dbelief; loss weights λs, λr, β. 3: for each training iteration do 4: Collect a batch of recent trajectories {τi}. 5: Store trajectories {τi} in Dbelief. 6: //Update Policy Module 7: Compute belief mt for {τi} using ﬁxed encoder qφ. 8: Update ψ by minimizing PPO loss: L(ψ) = ˆEt[−LCLIP(ψ) + LVF(ψ) −αH[πψ](st, mt)] 9: Compute average entropy ¯H = ˆEt[H[πψ(·|st, mt)]] 10: Update entropy weight α ←α −( ¯H −Htarget) 11: //Update Belief Module 12: Sample a batch of trajectories {τj} ∼Dbelief.

**Fragmento 14 - p. 8 - score 3:**

While off-policy algorithms like SAC are known for high sample efﬁciency, we explicitly select the on-policy PPO to ensure training stability in our meta-learning framework. Since the Belief Encoder evolves continuously, data stored in an off-policy replay buffer would contain obsolete belief representations. PPO avoids this issue by strictly learning from fresh trajectories consistent with the current encoder. We utilize the clipped surrogate objective to prevent destruc- tive large updates: LCLIP(ψ) = ˆEt  min  rt(ψ) ˆAt, clip(rt(ψ), 1 −ϵ, 1 + ϵ) ˆAt  , (17) where rt(ψ) is the probability ratio, ϵ is a hyperparameter used to limit the variation of the probability ratio and ˆAt is the advantage estimate.

**Fragmento 15 - p. 8 - score 3:**

The encoder and decoder (φ, θ) are updated independently by sampling trajectories from a separate replay buffer. The objective is to minimize the ELBO loss derived in (11), which aggregates the state reconstruction loss, reward prediction loss, and the KL divergence regularization term. ▷Online Adaptation: When deployed to the client, the model willadaptonlineinthenewnetworkenvironment.Whenrunning online, there is no need for real-time gradient updates or training. The adaptability of policy is achieved entirely through real-time inference. Initially, the latest interaction tuple (at−1, rt, st) is fed into the Belief Encoder qφ to update the recurrent hidden state ht.

**Fragmento 16 - p. 10 - score 3:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1185 Fig. 6. Normalized average QoE comparison on the out-of-distribution test sets (Oboe, 4GNY). datasets. Fig. 5 illustrates the normalized average QoE scores for both QoElin and QoElog metrics. As shown in Fig. 5, our proposed EAStream consistently achieves the highest, or joint-highest, average QoE across all three network conditions for both QoElin and QoElog metrics. This demonstrates that EAStream can learn a highly effective and stable policy even when trained on a diverse hybrid dataset. This is a notable advantage, as prior work [14] has shown that baseline DRL agents like Pensieve can suffer performance degradation when trained on mixed network conditions rather than a single environment.

**Fragmento 17 - p. 10 - score 3:**

For instance, in the low-bandwidth 3G and FCC dataset, EAStream outperforms the standard DRL method Pensieve and the recent LLM-based algorithm NetLLM. In the high- bandwidth 4GSyd scenario, EAStream achieves comparable performance to the strong baseline Comyco. This balanced suc- cess contrasts with Pensieve, which performs notably weaker in the low-bandwidth traces. This gap suggests Pensieve may have over-specialized on the high-bandwidth traces within the hybrid dataset, whereas EAStream learns a more effective strategy that masters the full training distribution. The CDF plots in Fig. 7 and Fig. 8 provide a more detailed view of the performance distribution.

**Fragmento 18 - p. 10 - score 3:**

In all subplots, EAStream is consistently positioned to the right of all other algorithms. This suggests that EAStream not only achieves a higher average QoE but also provides a more stable experience for the vast majority of users, minimizing the poor experience sessions. ▷Generalization to Unseen Network Environments. To evaluate the aspect of generalization, we now assess the per- formance on two unseen (out-of-distribution, OOD) test sets: Oboe and 4GNY. These network traces were not exposed to any learning-based models during the training phase. Fig. 6 illustrates the normalized average QoE scores for both QoE metrics on these two unseen datasets.

**Fragmento 19 - p. 12 - score 3:**

Finally, in extreme outlier scenarios that deviate signiﬁcantly from the training distribution, the inferred belief may become inaccurate. As noted in Section VI, leveraging the reconstruction error for anomaly detection offers a promising avenue to mitigate this issue in future work. VI. CONCLUSION This paper presents EAStream, a context-based meta- reinforcement learning framework designed to address the gen- eralization challenge in adaptive bitrate streaming. By modeling theproblemasaBAMDPandutilizingavariationalautoencoder, EAStream infers latent beliefs about network dynamics from interactionhistory.Thismechanismenablesthepolicytoachieve zero-shot adaptation to unseen network conditions without re- quiring computationally expensive online ﬁne-tuning.

**Fragmento 20 - p. 1 - score 2:**

The seminal method, Pensieve [8], uses deep reinforcement learning algorithm (DRL) to learn bitrate adaptation policies. Unlike the MPC-based methods that rely on system models, the DRL algorithm directly learns the model-free strategies from experience, enabling it to better handle dynamic networks. Furthermore, DRL algorithms have long-term planning capa- bilities, which allows them to make complex strategic trade- offs that balance instant video quality and long-term viewing stability. 1939-1374 © 2026 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission.

**Fragmento 21 - p. 1 - score 2:**

To address this, Model Predictive Control (MPC) [7] was introduced to enable proactive decision-making by optimizing QoE over a future horizon based on throughput predictions. Although MPC generally outperforms heuristics, its reliability heavily depends on the accuracy of bandwidth estimation. In recent years, considerable attention has been directed to- wards applying learning-based methods to ABR streaming [8], [9], [10], [11]. In contrast to traditional heuristic-based meth- ods, learning-based methods typically train neural networks on datasets spanning multiple network conditions. This allows them to capture the complicated correlations in video streaming.

**Fragmento 22 - p. 2 - score 2:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1177 Despite these advantages, one challenge DRL-based ABR methods face is their limited generalization to unseen net- work conditions. This is because the learned policy is prone to overﬁtting to the training network environment. Such over- specialization is particularly problematic as real-world networks are inherently dynamic and non-stationary. In fact, when de- ployed in real-world scenarios, their performance has been shown to be even inferior to that of simple heuristic-based methods [10]. To tackle this generalization challenge, recent studies have introduced meta-reinforcement learning approaches, which gen- erally fall into two categories.


### 8.6. datos trazas datasets

Palabras clave usadas: `dataset, trace, traces, network trace, bandwidth trace, FCC, HSDPA, Norway, LTE, 4G, WiFi, Puffer, Starlink, cellular, synthetic, simulation, testbed, Mahimahi, live streaming, real-world, stream-years, users, sessions, heavy-tailed, CMCD, CMSD`

**Fragmento 1 - p. 9 - score 12:**

▷Network Traces: To rigorously evaluate algorithm perfor- mance, we utilize network traces collected from a variety of real-world communication datasets. r 3G [49]: This dataset comprises throughput measurements from 3G mobile networks, collected on public transporta- tion routes in Oslo, Norway. r FCC [50]: Sourced from broadband network traces re- leased by the U.S. Federal Communications Commission (FCC), these traces are selected from the “Web browsing” category and are characterized by moderate bandwidth conditions. r 4GSyd [51]: This dataset contains traces gathered from 4 G vehicular networks under driving conditions in Sydney, Australia. r Oboe [52]: This dataset contains traces from a commer- cial on-demand music video service, capturing sessions from a mix of users on both wired desktop and mobile (WiFi/cellular) connections.

**Fragmento 2 - p. 10 - score 7:**

In all subplots, EAStream is consistently positioned to the right of all other algorithms. This suggests that EAStream not only achieves a higher average QoE but also provides a more stable experience for the vast majority of users, minimizing the poor experience sessions. ▷Generalization to Unseen Network Environments. To evaluate the aspect of generalization, we now assess the per- formance on two unseen (out-of-distribution, OOD) test sets: Oboe and 4GNY. These network traces were not exposed to any learning-based models during the training phase. Fig. 6 illustrates the normalized average QoE scores for both QoE metrics on these two unseen datasets.

**Fragmento 3 - p. 9 - score 6:**

r 4GNY [53]: Collected on New York City’s public transit system (bus and subway), these traces represent highly variable urban mobile network conditions. We provide an overview of the primary characteristics for these datasets in Table I. For training our learning-based models (EAStream and Pen- sieve), we create a single, uniﬁed dataset to foster generalization. We combine the traces from the 3G, FCC, and 4GSyd sources to form a Hybrid dataset. From this Hybrid dataset, 80% of the traces are randomly sampled to constitute the training set. The remaining 20% of the Hybrid dataset is held out as the in-distribution test set, used to evaluate performance TABLE I CHARACTERISTICS OF NETWORK TRACE DATASETS TABLE II PARAMETERS FOR DIFFERENT QOE METRICS Fig.

**Fragmento 4 - p. 10 - score 6:**

For instance, in the low-bandwidth 3G and FCC dataset, EAStream outperforms the standard DRL method Pensieve and the recent LLM-based algorithm NetLLM. In the high- bandwidth 4GSyd scenario, EAStream achieves comparable performance to the strong baseline Comyco. This balanced suc- cess contrasts with Pensieve, which performs notably weaker in the low-bandwidth traces. This gap suggests Pensieve may have over-specialized on the high-bandwidth traces within the hybrid dataset, whereas EAStream learns a more effective strategy that masters the full training distribution. The CDF plots in Fig. 7 and Fig. 8 provide a more detailed view of the performance distribution.

**Fragmento 5 - p. 9 - score 5:**

The speciﬁc deﬁnition is as follows: r QoElin This metric considers that the video quality in- creases linearly with the bitrate. r QoElog This metric considers a higher bitrate to have diminishing returns to perceptual quality. Table II provides a summary of the parameters used for each QoE metric. B. EAStream Vs. Existing ABR Algorithms In this section, we compare EAStream with the baseline algorithms. The test dataset includes in-distribution (Hybrid) and out-of-distribution (Oboe, 4GNY). We use bar charts to present the normalized average QoE scores in Figs. 5 and 6. We analyzed the performance distribution using CDF plots in Figs. 7, 8, and 9. ▷Performance on the Hybrid Test Set: We ﬁrst evaluate the performance of all algorithms on the in-distribution test set, which is composed of traces from the 3G, FCC, and 4GSyd Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 6 - p. 1 - score 4:**

A comprehensive evaluation is conducted using diverse real-world network traces. Experimental results show that EAStream not only achieves leading performance on in-distribution test sets compared to state-of-the-art ABR algorithms, but also demonstrates superior generalization capability on out-of-distribution test scenarios. Index Terms—Adaptive video streaming, generalization, meta learning, network uncertainty, quality of experience. I. INTRODUCTION W ITH the rapid development of the Internet in recent years, video streaming has become the predominant Received 2 December 2025; revised 9 February 2026; accepted 3 March 2026. Date of publication 9 March 2026; date of current version 10 April 2026.

**Fragmento 7 - p. 2 - score 4:**

r We conduct extensive experiments across a diversity of real-world network traces (Section V). Our evaluations show that EAStream not only achieves state-of-the-art performance on in-distribution networks, but also shows better generalization ability in unseen, out-of-distribution environments compared to state-of-the-art algorithms. The remainder of this paper is structured as follows. Section II reviews the related work in ABR streaming and meta-reinforcement learning. Section III formulates the ABR problem and presents our Bayesian adaptive modeling approach. Section IV details the system design of our proposed EAStream framework, including its architecture and training methodology.

**Fragmento 8 - p. 11 - score 4:**

1186 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 Fig. 7. CDF of QoElin scores on the in-distribution Hybrid test set (3G, FCC, 4GSyd). Fig. 8. CDF of QoElog scores on the in-distribution Hybrid test set (3G, FCC, 4GSyd). Fig. 9. CDF of QoE scores on the out-of-distribution test sets (Oboe and 4GNy). Fig. 10. Bitrate selection of EAStream, Pensieve, and RobustMPC on the bandwidth drop trace. uninformative due to over-regularization, known as posterior collapse. The results conﬁrm that a moderate latent dimension and KL coefﬁcient provide the best balance for the latent belief representation. Fig. 11. t-SNE visualization of the latent belief vectors collected from three distinct network datasets.

**Fragmento 9 - p. 12 - score 4:**

Extensive experiments on real-world datasets demonstrate that EAStream not only matches state-of-the-art performance on in-distribution traces but signiﬁcantly outperforms existing baselines in out-of- distribution scenarios. In future work, we intend to explore the online utilization of the Belief Decoder, which is currently only reserved for ofﬂine training. Speciﬁcally, we plan to leverage the real-time reconstruction errors for anomaly detection to identify extreme network outliers. REFERENCES [1] Sandvine, “2024 Global internet phenomena report,” 2024. [Online]. Available: https://www.applogicnetworks.com/global-internet-phenom ena-report-2024 [2] G.

**Fragmento 10 - p. 13 - score 4:**

[48] “EnvivioDash3,” 2016. [Online]. Available: https://dash.akamaized.net/ envivio/EnvivioDash3/ [49] H. Riiser, P. Vigmostad, C. Griwodz, and P. Halvorsen, “Commute path bandwidth traces from 3G networks: Analysis and applications,” in Proc. 4th ACM Multimedia Syst. Conf., 2013, pp. 114–118. [50] Federal Communications Commission, “Raw data - measuring broadband America 2016,” Dec. 2016. Accessed: Oct. 16, 2025. [Online]. Available: https://www.fcc.gov/reports-research/reports/measuring-broadband- america/raw-data-measuring-broadband-america-2016 [51] A. Bokani, M. Hassan, S. S. Kanhere, J. Yao, and G. Zhong, “Comprehen- sive mobile bandwidth traces from vehicular networks,” in Proc.

**Fragmento 11 - p. 5 - score 3:**

, (7) where H denotes the time horizon of a video streaming ses- sion, and γ ∈[0, 1] is the discount factor that determines the importance of future rewards. However, a core limitation of the standard MDP lies in its assumption of a stationary or perfectly known transition function P(st+1|st, at). This assumption is frequently violated in real-world networks, where conditions like bandwidth are highly dynamic and non-stationary. An ABR agent trained under one speciﬁc network trace may fail to generalize to other ﬂuctuating network conditions, leading to suboptimal performance. To address this limitation, where the true dynamics of the environment are unknown, we model the ABR problem as a Bayes-Adaptive Markov Decision Process (BAMDP) [15]. In a standard MDP, the agent assumes the network follows a ﬁxed rule. In contrast, a BAMDP agent acknowledges its ignorance about the speciﬁc network scenario. It maintains a belief state—a probabilistic “mental model” of the current net- work environment. As the agent observes new state transitions, it recursively updates this belief, allowing it to adapt its strategy dynamically based on its conﬁdence in the environment’s state. In this framework, the unknown network dynamics are treated as a latent variable. The agent maintains a belief state, bt, deﬁned as the posterior distribution over these possible network environments given the interaction history τ:t. The decision-making process in a BAMDP extends the stan- dard MDP cycle by incorporating a belief update step. The process proceeds as follows: 1) State Representation: At each timestep t, the agent’s state is a hyper-state s+ t = (st, bt), consisting of the observable physical state st and the current belief bt. 2) Action & Observation: The agent selects an action at. The env

**Fragmento 12 - p. 9 - score 3:**

5. Normalized average QoE comparison on the in-distribution Hybrid test set (3G, FCC, 4GSyd). on network conditions similar to those seen during train- ing. The 4GNY and Oboe datasets are kept entirely separate from the training process. They serve exclusively as out-of- distribution test sets to rigorously assess the generalization ca- pabilities of the pre-trained models in completely novel network environments. ▷QoE Metrics: To evaluate the algorithm performance based on different user preferences, we adopted two distinct QoE targets from Pensieve [8]. For learning-based algorithms (Pen- sieve, Comyco, NetLLM and EAStream), we train a dedicated model for each QoE objective.

**Fragmento 13 - p. 12 - score 3:**

This conﬁrms that EAStream is suitable for resource- constrained client deployments. D. Discussion and Limitations Despite the demonstrated advantages, we acknowledge cer- tain limitations of the EAStream framework. First, the ofﬂine meta-training process incurs higher computational overhead compared to standard DRL methods due to the joint optimization of the belief inference and policy modules. However, this cost is strictly conﬁned to the ofﬂine phase and does not impact the low-latency requirements of online inference. Second, the algorithm’s generalization capability is inherently dependent on the diversity of the network traces used during meta-training; a narrow task distribution may limit the effective range of adaptation.

**Fragmento 14 - p. 3 - score 2:**

To address this, a recent work NetLLM [33] explores adapting Large Language Models (LLMs) as universal foundation models to handle diverse networking tasks. However, it introduces signiﬁcant computational overhead and latency, making it less ideal for real-time deployment on resource- constrained devices. C. Meta-Reinforcement Learning for Generalization Totackletheoverﬁttingproblem, meta-learningoffers alearn- ing paradigm [34]. Its core idea is to train on a distribution of related tasks to learn an inductive bias, enabling fast adaptation to new, unseen tasks with high sample efﬁciency at test time [35]. While conventional RL agents tend to overﬁt the training traces, Meta-Reinforcement Learning (Meta-RL) learns an adaptive policy that generalizes across different network environments from the task distribution [35].

**Fragmento 15 - p. 10 - score 2:**

Average 16- dimensional belief vectors were collected from the QoElin model across three distinct datasets: 3G (low bandwidth), 4GSyd (stable high bandwidth), and 4GNY (unstable high bandwidth). As shown in Fig. 11, the belief vectors form three distinct clusters corresponding to each environment. This separation demonstrates that the module effectively captures both coarse- grained bandwidth levels and ﬁne-grained volatility differences between the two 4 G networks. These results validate that latent beliefs encode critical environmental dynamics, providing the necessary awareness for optimal adaptive decisions. ▷Ablation and Sensitivity Analysis: We conduct ablation and sensitivity studies to evaluate the impact of the belief represen- tation by varying the latent dimension and the KL coefﬁcient using the 3G dataset.

**Fragmento 16 - p. 10 - score 2:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1185 Fig. 6. Normalized average QoE comparison on the out-of-distribution test sets (Oboe, 4GNY). datasets. Fig. 5 illustrates the normalized average QoE scores for both QoElin and QoElog metrics. As shown in Fig. 5, our proposed EAStream consistently achieves the highest, or joint-highest, average QoE across all three network conditions for both QoElin and QoElog metrics. This demonstrates that EAStream can learn a highly effective and stable policy even when trained on a diverse hybrid dataset. This is a notable advantage, as prior work [14] has shown that baseline DRL agents like Pensieve can suffer performance degradation when trained on mixed network conditions rather than a single environment.

**Fragmento 17 - p. 10 - score 2:**

The results clearly demonstrate the superior generalization capability of EAStream. In all four scenarios, EAStream achieved the highest or nearly the highest average QoE. Speciﬁcally, its performance on the Oboe dataset outperforms all other algorithms, including the strong baseline Comyco. It also achieves top-tier performance on the 4GNY dataset, comparable to Comyco and signiﬁcantly better than Pensieve and NetLLM. In all four CDF subplots in Fig. 9, EAStream has excel- lent performance compared with other baseline algorithms. A key ﬁnding is the performance of Pensieve. Pensieve demon- strated decent performance on the 4GSyd dataset, but it dropped signiﬁcantly on the 4GNY dataset.

**Fragmento 18 - p. 1 - score 1:**

Zhiquan Liu is with the College of Cyber Security, Jinan University, Guangzhou 510632, China (e-mail: zqliu@jnu.edu.cn). Min Chen is with the School of Computer Science and Engineering, South China University of Technology, Guangzhou 510006, China, and also with Pazhou Laboratory, Guangzhou 510330, China (e-mail: minchen@ieee.org). Athanasios V. Vasilakos is with the Department of ICT and Center for AI Research, University of Agder(UiA), 4879 Grimstad, Norway (e-mail: thanos.vasilakos@uia.no). Ahmed Farouk is with the Faculty of Computers and Artiﬁcial Intelligence, Hurghada University, Hurghada 83523, Egypt (e-mail: ahmed.farouk@sci.svu.edu.eg). Houbing Herbert Song is with the Department of Information Systems, University of Maryland, Baltimore, MD 21250 USA (e-mail: h.song@ieee.org).

**Fragmento 19 - p. 1 - score 1:**

To address this, Model Predictive Control (MPC) [7] was introduced to enable proactive decision-making by optimizing QoE over a future horizon based on throughput predictions. Although MPC generally outperforms heuristics, its reliability heavily depends on the accuracy of bandwidth estimation. In recent years, considerable attention has been directed to- wards applying learning-based methods to ABR streaming [8], [9], [10], [11]. In contrast to traditional heuristic-based meth- ods, learning-based methods typically train neural networks on datasets spanning multiple network conditions. This allows them to capture the complicated correlations in video streaming.

**Fragmento 20 - p. 2 - score 1:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1177 Despite these advantages, one challenge DRL-based ABR methods face is their limited generalization to unseen net- work conditions. This is because the learned policy is prone to overﬁtting to the training network environment. Such over- specialization is particularly problematic as real-world networks are inherently dynamic and non-stationary. In fact, when de- ployed in real-world scenarios, their performance has been shown to be even inferior to that of simple heuristic-based methods [10]. To tackle this generalization challenge, recent studies have introduced meta-reinforcement learning approaches, which gen- erally fall into two categories.

**Fragmento 21 - p. 3 - score 1:**

Broadly, Meta-RL methods are typically categorized as two main paradigms: optimization-based and context-based. Optimization-based methods learn a sensitive parameter ini- tialization that allows for rapid adaptation via a few gradient steps. A canonical example is Model-Agnostic Meta-Learning (MAML) [36], which meta-learns a shared prior for fast ﬁne- tuning. However, MAML’s reliance on second-order derivatives is computationally expensive. To address this, more efﬁcient, ﬁrst-order alternatives were developed. FOMAML [37] and Reptile [38] simplify the update by ignoring or approximating higher-order terms, avoiding the need to differentiate through the entire optimization process.

**Fragmento 22 - p. 3 - score 1:**

DeepBuffer [21] jointly controls the maximum buffer size to avoid unnecessary bandwidth consumption. GreenABR+ [22] employsaDDPG-basedapproachtoreducepowerconsumption. BE-ABR [23] uses Transformer-based prediction to minimize data waste. DRL has also been tailored for speciﬁc environments. In mobile edge computing (MEC), Guo et al. [24] jointly optimize transcoding and bitrate decisions. QAVA [25] addresses the fairness problem among multiple clients. Moreover, researchers tackle speciﬁc application challenges: CAST [26] prioritizes intricate video scenes, L2AC-E [27] minimizes latency for live streaming, and DeepVR [28] predicts user ﬁeld-of-view for panoramic video.


### 8.7. evaluacion baselines experimentos

Palabras clave usadas: `evaluation, experiment, baseline, compare, comparison, Pensieve, BBA, BOLA, MPC, RobustMPC, FastMPC, Rate-based, Comyco, Oboe, A2BR, Fugu, Puffer, Ahaggar, Gelato, Plume, results, performance, ablation`

**Fragmento 1 - p. 10 - score 7:**

The results clearly demonstrate the superior generalization capability of EAStream. In all four scenarios, EAStream achieved the highest or nearly the highest average QoE. Speciﬁcally, its performance on the Oboe dataset outperforms all other algorithms, including the strong baseline Comyco. It also achieves top-tier performance on the 4GNY dataset, comparable to Comyco and signiﬁcantly better than Pensieve and NetLLM. In all four CDF subplots in Fig. 9, EAStream has excel- lent performance compared with other baseline algorithms. A key ﬁnding is the performance of Pensieve. Pensieve demon- strated decent performance on the 4GSyd dataset, but it dropped signiﬁcantly on the 4GNY dataset.

**Fragmento 2 - p. 9 - score 6:**

r FESTIVE [5]: A rate-based heuristic algorithm. This al- gorithm uses the harmonic average of the nearest chunks download rates for throughput estimation. r RobustMPC [7]: An algorithm based on the theory of MPC. This algorithm predicts the future optimal sequence by combining throughput estimation and buffer informa- tion. r Pensieve [8]: A state-of-the-art ABR algorithm leveraging deep reinforcement learning. r NetLLM [33]: The ﬁrst framework using LLMs for net- working tasks through ﬁne-tuning to enhance generaliza- tion and performance. r Comyco [9]: A quality-aware ABR method based on im- itation learning. It trains the neural network by imitating the expert actions.

**Fragmento 3 - p. 1 - score 5:**

A comprehensive evaluation is conducted using diverse real-world network traces. Experimental results show that EAStream not only achieves leading performance on in-distribution test sets compared to state-of-the-art ABR algorithms, but also demonstrates superior generalization capability on out-of-distribution test scenarios. Index Terms—Adaptive video streaming, generalization, meta learning, network uncertainty, quality of experience. I. INTRODUCTION W ITH the rapid development of the Internet in recent years, video streaming has become the predominant Received 2 December 2025; revised 9 February 2026; accepted 3 March 2026. Date of publication 9 March 2026; date of current version 10 April 2026.

**Fragmento 4 - p. 9 - score 5:**

5. Normalized average QoE comparison on the in-distribution Hybrid test set (3G, FCC, 4GSyd). on network conditions similar to those seen during train- ing. The 4GNY and Oboe datasets are kept entirely separate from the training process. They serve exclusively as out-of- distribution test sets to rigorously assess the generalization ca- pabilities of the pre-trained models in completely novel network environments. ▷QoE Metrics: To evaluate the algorithm performance based on different user preferences, we adopted two distinct QoE targets from Pensieve [8]. For learning-based algorithms (Pen- sieve, Comyco, NetLLM and EAStream), we train a dedicated model for each QoE objective.

**Fragmento 5 - p. 10 - score 5:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1185 Fig. 6. Normalized average QoE comparison on the out-of-distribution test sets (Oboe, 4GNY). datasets. Fig. 5 illustrates the normalized average QoE scores for both QoElin and QoElog metrics. As shown in Fig. 5, our proposed EAStream consistently achieves the highest, or joint-highest, average QoE across all three network conditions for both QoElin and QoElog metrics. This demonstrates that EAStream can learn a highly effective and stable policy even when trained on a diverse hybrid dataset. This is a notable advantage, as prior work [14] has shown that baseline DRL agents like Pensieve can suffer performance degradation when trained on mixed network conditions rather than a single environment.

**Fragmento 6 - p. 11 - score 5:**

1186 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 Fig. 7. CDF of QoElin scores on the in-distribution Hybrid test set (3G, FCC, 4GSyd). Fig. 8. CDF of QoElog scores on the in-distribution Hybrid test set (3G, FCC, 4GSyd). Fig. 9. CDF of QoE scores on the out-of-distribution test sets (Oboe and 4GNy). Fig. 10. Bitrate selection of EAStream, Pensieve, and RobustMPC on the bandwidth drop trace. uninformative due to over-regularization, known as posterior collapse. The results conﬁrm that a moderate latent dimension and KL coefﬁcient provide the best balance for the latent belief representation. Fig. 11. t-SNE visualization of the latent belief vectors collected from three distinct network datasets.

**Fragmento 7 - p. 11 - score 5:**

▷Overhead Analysis: To test the overhead of EAStream, we conducted a quantitative analysis of its computational overhead and memory usage. We compared EAStream with Pensieve, RobustMPC and NetLLM. The experiments were carried out Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 8 - p. 12 - score 5:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1187 Fig. 12. Ablation studies on the latent belief representation. TABLE III RESOURCE CONSUMPTION AND INFERENCE LATENCY COMPARISON on a server equipped with an Intel i9-13900 K CPU and were run in a single-threaded mode. As shown in Table III, the overhead of introducing the Be- lief module is extremely small (0.0224 MFLOPs). Although it is slightly higher than Pensieve, the total inference latency of EAStream is only 0.2258 milliseconds. For a video chunk duration of 4 seconds, our algorithm accounts for only 0.0056% of it. EAStream’s speed is signiﬁcantly faster than the widely used RobustMPC (3.1315 milliseconds), and much faster than NetLLM.

**Fragmento 9 - p. 2 - score 4:**

r We conduct extensive experiments across a diversity of real-world network traces (Section V). Our evaluations show that EAStream not only achieves state-of-the-art performance on in-distribution networks, but also shows better generalization ability in unseen, out-of-distribution environments compared to state-of-the-art algorithms. The remainder of this paper is structured as follows. Section II reviews the related work in ABR streaming and meta-reinforcement learning. Section III formulates the ABR problem and presents our Bayesian adaptive modeling approach. Section IV details the system design of our proposed EAStream framework, including its architecture and training methodology.

**Fragmento 10 - p. 9 - score 4:**

The speciﬁc deﬁnition is as follows: r QoElin This metric considers that the video quality in- creases linearly with the bitrate. r QoElog This metric considers a higher bitrate to have diminishing returns to perceptual quality. Table II provides a summary of the parameters used for each QoE metric. B. EAStream Vs. Existing ABR Algorithms In this section, we compare EAStream with the baseline algorithms. The test dataset includes in-distribution (Hybrid) and out-of-distribution (Oboe, 4GNY). We use bar charts to present the normalized average QoE scores in Figs. 5 and 6. We analyzed the performance distribution using CDF plots in Figs. 7, 8, and 9. ▷Performance on the Hybrid Test Set: We ﬁrst evaluate the performance of all algorithms on the in-distribution test set, which is composed of traces from the 3G, FCC, and 4GSyd Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 11 - p. 9 - score 4:**

1184 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 ▷Video Parameters: The video content selected for our experiments is the “EnvivioDash3” test sequence [48]. It has a total duration of 193 seconds and is segmented into 48 chunks, each with a playback time of approximately 4 seconds. Each chunk is pre-encoded into six different bitrate levels to facilitate adaptive streaming: 300, 750, 1200, 1850, 2850, and 4300 kbps. ▷Baseline Algorithms: We select several state-of-the-art ABR algorithms that represent different design paradigms for comparison: r BOLA [16]: A buffer-based algorithm based on Lyapunov optimization. This algorithm ensures that the video quality is maximized while guaranteeing the stability of the buffer.

**Fragmento 12 - p. 10 - score 4:**

This might be due to the highly unstable 4GNY trajectory (as shown in Table I), which suggests poor generalization of Pensieve. In contrast, EAStream maintains stable performance in both in-distribution and out-of- distribution tests. This generalization performance demonstrates the effectiveness of our meta-learning framework in learning to rapidly adapt to network uncertainty. C. Effectiveness Analysis ▷Case Study: We synthesized a challenging trajectory by concatenating 4GSyd and 3G segments to evaluate EAStream’s adaptability under abrupt non-stationary changes (e.g., a sharp bandwidth drop at 5 s). As shown in Fig. 10, EAStream achieved the highest QoE (1.40), outperforming Pensieve (1.21) and RobustMPC (1.07).

**Fragmento 13 - p. 10 - score 4:**

For instance, in the low-bandwidth 3G and FCC dataset, EAStream outperforms the standard DRL method Pensieve and the recent LLM-based algorithm NetLLM. In the high- bandwidth 4GSyd scenario, EAStream achieves comparable performance to the strong baseline Comyco. This balanced suc- cess contrasts with Pensieve, which performs notably weaker in the low-bandwidth traces. This gap suggests Pensieve may have over-specialized on the high-bandwidth traces within the hybrid dataset, whereas EAStream learns a more effective strategy that masters the full training distribution. The CDF plots in Fig. 7 and Fig. 8 provide a more detailed view of the performance distribution.

**Fragmento 14 - p. 2 - score 3:**

These are primarily categorized into two classes: rate- based and buffer-based. Rate-based algorithms, such as FES- TIVE [5], guide their decisions by measuring historical network throughput. To address the lag problem of rate-based methods, buffer-based algorithms use buffer occupancy as a key metric. BBA [6] matches bitrate actions by setting different buffer thresholds. The more sophisticated algorithm BOLA [16] is based on Lyapunov optimization to maximize the QoE while ensuring that the buffer is not exhausted. Although the heuristic methodissimpleandeffective,theﬁxedrulesalsolimititsability to adapt to the dynamic and unstable network environment.

**Fragmento 15 - p. 10 - score 3:**

While the sudden transition caused initial rebuffering for all algorithms due to high-bitrate inertia, EAStream recovered most effectively. It rapidly detected the deterioration, down- shifting to 300 kbps to stabilize playback before smoothly tran- sitioning upward as buffers replenished. Conversely, Pensieve and RobustMPC struggled with persistent rebuffering and fre- quent switching. This conﬁrms that EAStream’s environment- awareness mechanism facilitates superior long-term decision- making in dynamic networks. ▷Analysis of Latent Belief Space: We evaluated whether EAStream’s belief module learns meaningful environmental representations using t-SNE [54] visualization.

**Fragmento 16 - p. 12 - score 3:**

Extensive experiments on real-world datasets demonstrate that EAStream not only matches state-of-the-art performance on in-distribution traces but signiﬁcantly outperforms existing baselines in out-of- distribution scenarios. In future work, we intend to explore the online utilization of the Belief Decoder, which is currently only reserved for ofﬂine training. Speciﬁcally, we plan to leverage the real-time reconstruction errors for anomaly detection to identify extreme network outliers. REFERENCES [1] Sandvine, “2024 Global internet phenomena report,” 2024. [Online]. Available: https://www.applogicnetworks.com/global-internet-phenom ena-report-2024 [2] G.

**Fragmento 17 - p. 1 - score 2:**

However, the ABR algorithm faces challenges because it needs to balance conﬂicting ob- jectives: maximizing video quality and minimizing playback interruptions. Speciﬁcally, high bitrate chunks will be selected for better playback quality. However, it will increase the risk of playback stalls, especially in the case of unstable network conditions. Traditional ABR algorithms primarily rely on ﬁxed rules or control-theoretic models. Heuristic-based approaches, such as the rate-based FESTIVE [5] and the buffer-based BBA [6], make decisions using predeﬁned thresholds. While computationally efﬁcient and easy to deploy, these rule-based methods lack the ﬂexibility to adapt to diverse network scenarios or varying QoE preferences.

**Fragmento 18 - p. 1 - score 2:**

The seminal method, Pensieve [8], uses deep reinforcement learning algorithm (DRL) to learn bitrate adaptation policies. Unlike the MPC-based methods that rely on system models, the DRL algorithm directly learns the model-free strategies from experience, enabling it to better handle dynamic networks. Furthermore, DRL algorithms have long-term planning capa- bilities, which allows them to make complex strategic trade- offs that balance instant video quality and long-term viewing stability. 1939-1374 © 2026 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission.

**Fragmento 19 - p. 2 - score 2:**

Section V presents the comprehensive experimental evalua- tion and analysis of results. Finally, Section VI concludes the paper. II. RELATED WORK This section will review the related work in the ﬁelds of ABR streaming and meta-learning, particularly focusing on meta-reinforcement learning. A. Conventional ABR Algorithms ABR streaming has been the subject of extensive research in the ﬁeld of network communication over the past decade. Early ABR algorithms primarily relied on explicitly deﬁned rules and mathematical models. These approaches are typically classiﬁed into two main categories: heuristic-based methods and control- theoretic methods. Heuristic-based methods represent the earliest class of ABR algorithms, selecting bitrates through intuitive, pre-deﬁned rules.

**Fragmento 20 - p. 2 - score 2:**

To address the passivity of heuristic approaches, re- searchers have introduced prospective control-theoretic ap- proaches. Among these approaches, Model Predictive Control (MPC) [7] is the most inﬂuential. MPC-based algorithms use the predictive bandwidth to optimize a series of bitrate decisions over the future horizon. Subsequent research has focused on en- hancing MPC’s core issue of prediction accuracy. For instance, Fugu [10] improves the prediction module by using a deep neural network, while AAR [17] utilizes server-assisted information to achieve more accurate bandwidth prediction. Beyond MPC, other classical control models have also been explored, such as PIA [18] uses a PI controller to stabilize the playout buffer at the target level.

**Fragmento 21 - p. 3 - score 2:**

1178 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 Pensieve [8] employs Deep Reinforcement Learning (DRL) and outperforms traditional algorithms. The success of Pensieve has motivated a series of studies on Learning-based ABR algorithms. For instance, Comyco [9] employs imitation learning to enhance sample efﬁciency. Tiyuntsong [19] introduces a self-play framework to clearly deﬁne the optimization objective. Another major direction focuses on jointly optimizing bitrate with other metrics. Early works like AMIS [20] manage both bi- trate and playout speed to mitigate the risk of rebuffering. Recent studies extend these objectives to energy and trafﬁc efﬁciency.

**Fragmento 22 - p. 4 - score 2:**

The ﬂuctuations penalty is calculated by accumulating the absolute variations in quality value across consecutive chunks. QoEvar = N  n=2 |q(Rn) −q(Rn−1)| . (4) QoE Objective: The ﬁnal QoE objective is deﬁned as a linear combination of these three components: QoE = μ1QoEqual −μ2QoErebuf −μ3QoEvar, (5) where µ = (μ1, μ2, μ3) is a vector of non-negative weighting coefﬁcients. These coefﬁcients are customizable hyperparam- eters representing different user preferences. For instance, in- creasing μ2 will penalize rebuffering more heavily, guiding the algorithm towards a more conservative strategy to ensure smooth playback. In our experiments, we adopt standard ﬁxed settings for fair comparison.


### 8.8. resultados numericos

Palabras clave usadas: `improve, improvement, outperform, gain, %, QoE gain, higher, lower, average, result, achieve, compared to, reduce, decrease, increase, stall time, stream-years, users, ms, latency`

**Fragmento 1 - p. 10 - score 5:**

The results clearly demonstrate the superior generalization capability of EAStream. In all four scenarios, EAStream achieved the highest or nearly the highest average QoE. Speciﬁcally, its performance on the Oboe dataset outperforms all other algorithms, including the strong baseline Comyco. It also achieves top-tier performance on the 4GNY dataset, comparable to Comyco and signiﬁcantly better than Pensieve and NetLLM. In all four CDF subplots in Fig. 9, EAStream has excel- lent performance compared with other baseline algorithms. A key ﬁnding is the performance of Pensieve. Pensieve demon- strated decent performance on the 4GSyd dataset, but it dropped signiﬁcantly on the 4GNY dataset.

**Fragmento 2 - p. 10 - score 5:**

In all subplots, EAStream is consistently positioned to the right of all other algorithms. This suggests that EAStream not only achieves a higher average QoE but also provides a more stable experience for the vast majority of users, minimizing the poor experience sessions. ▷Generalization to Unseen Network Environments. To evaluate the aspect of generalization, we now assess the per- formance on two unseen (out-of-distribution, OOD) test sets: Oboe and 4GNY. These network traces were not exposed to any learning-based models during the training phase. Fig. 6 illustrates the normalized average QoE scores for both QoE metrics on these two unseen datasets.

**Fragmento 3 - p. 1 - score 4:**

A comprehensive evaluation is conducted using diverse real-world network traces. Experimental results show that EAStream not only achieves leading performance on in-distribution test sets compared to state-of-the-art ABR algorithms, but also demonstrates superior generalization capability on out-of-distribution test scenarios. Index Terms—Adaptive video streaming, generalization, meta learning, network uncertainty, quality of experience. I. INTRODUCTION W ITH the rapid development of the Internet in recent years, video streaming has become the predominant Received 2 December 2025; revised 9 February 2026; accepted 3 March 2026. Date of publication 9 March 2026; date of current version 10 April 2026.

**Fragmento 4 - p. 12 - score 4:**

This conﬁrms that EAStream is suitable for resource- constrained client deployments. D. Discussion and Limitations Despite the demonstrated advantages, we acknowledge cer- tain limitations of the EAStream framework. First, the ofﬂine meta-training process incurs higher computational overhead compared to standard DRL methods due to the joint optimization of the belief inference and policy modules. However, this cost is strictly conﬁned to the ofﬂine phase and does not impact the low-latency requirements of online inference. Second, the algorithm’s generalization capability is inherently dependent on the diversity of the network traces used during meta-training; a narrow task distribution may limit the effective range of adaptation.

**Fragmento 5 - p. 1 - score 3:**

Digital Object Identiﬁer 10.1109/TSC.2026.3671090 component of global Internet trafﬁc. According to the Global Internet Phenomena Report 2024 [1], the trafﬁc transporting video accounts for 68% and 64% of the total downlink trafﬁc of ﬁxed and mobile networks, respectively. Given the industry’s projected growth to $416.84 billion by 2030 [2], ensuring a superiorQualityofExperience(QoE)iscriticalforuserretention and business success. To achieve this, Adaptive Bitrate (ABR) technology has been widely adopted as the standard delivery mechanism [3], [4]. By dividing videos into chunks available at multiple quality levels, ABR algorithms dynamically select the optimal bitrate for each chunk based on real-time network throughput and buffer occupancy.

**Fragmento 6 - p. 2 - score 3:**

To address the passivity of heuristic approaches, re- searchers have introduced prospective control-theoretic ap- proaches. Among these approaches, Model Predictive Control (MPC) [7] is the most inﬂuential. MPC-based algorithms use the predictive bandwidth to optimize a series of bitrate decisions over the future horizon. Subsequent research has focused on en- hancing MPC’s core issue of prediction accuracy. For instance, Fugu [10] improves the prediction module by using a deep neural network, while AAR [17] utilizes server-assisted information to achieve more accurate bandwidth prediction. Beyond MPC, other classical control models have also been explored, such as PIA [18] uses a PI controller to stabilize the playout buffer at the target level.

**Fragmento 7 - p. 2 - score 3:**

r We conduct extensive experiments across a diversity of real-world network traces (Section V). Our evaluations show that EAStream not only achieves state-of-the-art performance on in-distribution networks, but also shows better generalization ability in unseen, out-of-distribution environments compared to state-of-the-art algorithms. The remainder of this paper is structured as follows. Section II reviews the related work in ABR streaming and meta-reinforcement learning. Section III formulates the ABR problem and presents our Bayesian adaptive modeling approach. Section IV details the system design of our proposed EAStream framework, including its architecture and training methodology.

**Fragmento 8 - p. 4 - score 3:**

The goal of the ABR algorithm is to optimize the long-term QoE of users. QoE evaluates the subjective satisfaction of users, which is composed of three components: video quality, rebuffer- ing, and quality ﬂuctuations. Video Quality: The video quality reﬂects the perceived visual quality derived from the bitrate Rn of each video chunk. Users tend to watch videos with high average visual quality. It is calculated based on the sum of the n-th chunk: QoEqual = N  n=1 q(Rn), (1) where q(Rn) represents the video quality level for the bitrate Rn. The selection of q(Rn) commonly includes the raw bitrate Rn and a logarithmic mapping log(Rn) to reﬂect diminishing returns of higher bitrate.

**Fragmento 9 - p. 9 - score 3:**

The speciﬁc deﬁnition is as follows: r QoElin This metric considers that the video quality in- creases linearly with the bitrate. r QoElog This metric considers a higher bitrate to have diminishing returns to perceptual quality. Table II provides a summary of the parameters used for each QoE metric. B. EAStream Vs. Existing ABR Algorithms In this section, we compare EAStream with the baseline algorithms. The test dataset includes in-distribution (Hybrid) and out-of-distribution (Oboe, 4GNY). We use bar charts to present the normalized average QoE scores in Figs. 5 and 6. We analyzed the performance distribution using CDF plots in Figs. 7, 8, and 9. ▷Performance on the Hybrid Test Set: We ﬁrst evaluate the performance of all algorithms on the in-distribution test set, which is composed of traces from the 3G, FCC, and 4GSyd Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**Fragmento 10 - p. 10 - score 3:**

Speciﬁcally, a dimension of 0 represents the baseline model where the belief module is entirely removed. As shown in Fig. 12(a), the agent achieves the best performance with a dimension of 16, outperforming the baseline model without the Belief module. This proves the effectiveness of the Belief module. Meanwhile, when the dimension is too small, the latent vector lacks the capacity to sufﬁciently encode complex network dynamics. Conversely, a dimension larger than 16 leads to performance degradation, likely due to increased optimization difﬁculty. Similarly, we test the sensitivity to the KL coefﬁcient β, as shown in Fig. 12(b). A small β makes the latent space irregular and hurts performance.

**Fragmento 11 - p. 10 - score 3:**

For instance, in the low-bandwidth 3G and FCC dataset, EAStream outperforms the standard DRL method Pensieve and the recent LLM-based algorithm NetLLM. In the high- bandwidth 4GSyd scenario, EAStream achieves comparable performance to the strong baseline Comyco. This balanced suc- cess contrasts with Pensieve, which performs notably weaker in the low-bandwidth traces. This gap suggests Pensieve may have over-specialized on the high-bandwidth traces within the hybrid dataset, whereas EAStream learns a more effective strategy that masters the full training distribution. The CDF plots in Fig. 7 and Fig. 8 provide a more detailed view of the performance distribution.

**Fragmento 12 - p. 12 - score 3:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1187 Fig. 12. Ablation studies on the latent belief representation. TABLE III RESOURCE CONSUMPTION AND INFERENCE LATENCY COMPARISON on a server equipped with an Intel i9-13900 K CPU and were run in a single-threaded mode. As shown in Table III, the overhead of introducing the Be- lief module is extremely small (0.0224 MFLOPs). Although it is slightly higher than Pensieve, the total inference latency of EAStream is only 0.2258 milliseconds. For a video chunk duration of 4 seconds, our algorithm accounts for only 0.0056% of it. EAStream’s speed is signiﬁcantly faster than the widely used RobustMPC (3.1315 milliseconds), and much faster than NetLLM.

**Fragmento 13 - p. 1 - score 2:**

However, the ABR algorithm faces challenges because it needs to balance conﬂicting ob- jectives: maximizing video quality and minimizing playback interruptions. Speciﬁcally, high bitrate chunks will be selected for better playback quality. However, it will increase the risk of playback stalls, especially in the case of unstable network conditions. Traditional ABR algorithms primarily rely on ﬁxed rules or control-theoretic models. Heuristic-based approaches, such as the rate-based FESTIVE [5] and the buffer-based BBA [6], make decisions using predeﬁned thresholds. While computationally efﬁcient and easy to deploy, these rule-based methods lack the ﬂexibility to adapt to diverse network scenarios or varying QoE preferences.

**Fragmento 14 - p. 1 - score 2:**

To address this, Model Predictive Control (MPC) [7] was introduced to enable proactive decision-making by optimizing QoE over a future horizon based on throughput predictions. Although MPC generally outperforms heuristics, its reliability heavily depends on the accuracy of bandwidth estimation. In recent years, considerable attention has been directed to- wards applying learning-based methods to ABR streaming [8], [9], [10], [11]. In contrast to traditional heuristic-based meth- ods, learning-based methods typically train neural networks on datasets spanning multiple network conditions. This allows them to capture the complicated correlations in video streaming.

**Fragmento 15 - p. 2 - score 2:**

Section V presents the comprehensive experimental evalua- tion and analysis of results. Finally, Section VI concludes the paper. II. RELATED WORK This section will review the related work in the ﬁelds of ABR streaming and meta-learning, particularly focusing on meta-reinforcement learning. A. Conventional ABR Algorithms ABR streaming has been the subject of extensive research in the ﬁeld of network communication over the past decade. Early ABR algorithms primarily relied on explicitly deﬁned rules and mathematical models. These approaches are typically classiﬁed into two main categories: heuristic-based methods and control- theoretic methods. Heuristic-based methods represent the earliest class of ABR algorithms, selecting bitrates through intuitive, pre-deﬁned rules.

**Fragmento 16 - p. 3 - score 2:**

To address this, a recent work NetLLM [33] explores adapting Large Language Models (LLMs) as universal foundation models to handle diverse networking tasks. However, it introduces signiﬁcant computational overhead and latency, making it less ideal for real-time deployment on resource- constrained devices. C. Meta-Reinforcement Learning for Generalization Totackletheoverﬁttingproblem, meta-learningoffers alearn- ing paradigm [34]. Its core idea is to train on a distribution of related tasks to learn an inductive bias, enabling fast adaptation to new, unseen tasks with high sample efﬁciency at test time [35]. While conventional RL agents tend to overﬁt the training traces, Meta-Reinforcement Learning (Meta-RL) learns an adaptive policy that generalizes across different network environments from the task distribution [35].

**Fragmento 17 - p. 3 - score 2:**

1178 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 Pensieve [8] employs Deep Reinforcement Learning (DRL) and outperforms traditional algorithms. The success of Pensieve has motivated a series of studies on Learning-based ABR algorithms. For instance, Comyco [9] employs imitation learning to enhance sample efﬁciency. Tiyuntsong [19] introduces a self-play framework to clearly deﬁne the optimization objective. Another major direction focuses on jointly optimizing bitrate with other metrics. Early works like AMIS [20] manage both bi- trate and playout speed to mitigate the risk of rebuffering. Recent studies extend these objectives to energy and trafﬁc efﬁciency.

**Fragmento 18 - p. 3 - score 2:**

Broadly, Meta-RL methods are typically categorized as two main paradigms: optimization-based and context-based. Optimization-based methods learn a sensitive parameter ini- tialization that allows for rapid adaptation via a few gradient steps. A canonical example is Model-Agnostic Meta-Learning (MAML) [36], which meta-learns a shared prior for fast ﬁne- tuning. However, MAML’s reliance on second-order derivatives is computationally expensive. To address this, more efﬁcient, ﬁrst-order alternatives were developed. FOMAML [37] and Reptile [38] simplify the update by ignoring or approximating higher-order terms, avoiding the need to differentiate through the entire optimization process.

**Fragmento 19 - p. 3 - score 2:**

DeepBuffer [21] jointly controls the maximum buffer size to avoid unnecessary bandwidth consumption. GreenABR+ [22] employsaDDPG-basedapproachtoreducepowerconsumption. BE-ABR [23] uses Transformer-based prediction to minimize data waste. DRL has also been tailored for speciﬁc environments. In mobile edge computing (MEC), Guo et al. [24] jointly optimize transcoding and bitrate decisions. QAVA [25] addresses the fairness problem among multiple clients. Moreover, researchers tackle speciﬁc application challenges: CAST [26] prioritizes intricate video scenes, L2AC-E [27] minimizes latency for live streaming, and DeepVR [28] predicts user ﬁeld-of-view for panoramic video.

**Fragmento 20 - p. 5 - score 2:**

. (10) The strategy that achieves this goal is termed a Bayes-optimal policy. While this problem can theoretically be addressed via methods like posterior sampling [43] or Bayesian planning [44], these approaches typically incur prohibitive computational over- head for real-time ABR decisions. Computing exact belief up- dates is also generally infeasible in practice. Therefore, we leverageameta-reinforcementlearningparadigmtotacklethis issue, as detailed below. C. Approximating Bayes-Optimal Policies Via Meta-Learning The theoretical solution for BAMDP is computationally difﬁ- cult.Ourapproach,EAStream,employsameta-learningstrategy inspiredbyVariBAD[45]toacquireasolutionthatapproximates this policy. In the meta-learning framework, we model different network environments as individual tasks, each deﬁned by a hidden latent variable mi. This latent variable corresponds to the belief in BAMDP. Since the latent variable is unknown, the agent must infer information about mi from its historical information. Speciﬁcally,weemployanencodertotransformthetrajectoryτ:t into an inferred distribution qφ(m|τ:t) within the latent space. This distribution serves as an inference of the environment’s latent features. The learning process uses the framework of Variational Au- toencoder (VAE) [46]. We optimize the encoder network by maximizing the Variational Lower Bound (ELBO): ELBO = Eρ  Eqφ(m|τ:t)[log pθ(τ:H|m)] −DKL(qφ(m|τ:t)||pθ(m))] . (11) Here, ρ denotes the trajectory distribution induced by the current policy π and the initial state distribution ρ0. This equation consists of two components. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 21 - p. 8 - score 2:**

Given this hidden state, the encoder performs forward passing to infer the belief mt. This belief represents the agent’s perception of the current network environment. Then the belief mt and the current state st are jointly input into the policy network πψ to decide the next chunk’s bitrate at. Finally, the agent performs the action and observes the new state and reward. During the entire online phase, the auxiliary decoder module is deprecated, and the agent operated in pure inference mode. Unlike the optimization-based meta-learning methods that require gradient updates during testing, our method relies solely on forward propagation. This structural design reduces computational overhead and makes it more suitable for resource-constrained client deployments.

**Fragmento 22 - p. 8 - score 2:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1183 Algorithm 1: Ofﬂine Meta-Training. 1: Initialize belief params φ, θ; policy params ψ; entropy weight α; target entropy Htarget; 2: Initialize replay buffer Dbelief; loss weights λs, λr, β. 3: for each training iteration do 4: Collect a batch of recent trajectories {τi}. 5: Store trajectories {τi} in Dbelief. 6: //Update Policy Module 7: Compute belief mt for {τi} using ﬁxed encoder qφ. 8: Update ψ by minimizing PPO loss: L(ψ) = ˆEt[−LCLIP(ψ) + LVF(ψ) −αH[πψ](st, mt)] 9: Compute average entropy ¯H = ˆEt[H[πψ(·|st, mt)]] 10: Update entropy weight α ←α −( ¯H −Htarget) 11: //Update Belief Module 12: Sample a batch of trajectories {τj} ∼Dbelief.


### 8.9. limitaciones riesgos

Palabras clave usadas: `limitation, future work, challenge, overhead, complexity, generalization, real-world, deployment, cost, computational, unstable, fail, failure, heterogeneous, bias, biased, unbiased, trace-driven, heavy-tailed, unseen, uncertainty, unpredictable, privacy, fairness`

**Fragmento 1 - p. 3 - score 6:**

To address this, a recent work NetLLM [33] explores adapting Large Language Models (LLMs) as universal foundation models to handle diverse networking tasks. However, it introduces signiﬁcant computational overhead and latency, making it less ideal for real-time deployment on resource- constrained devices. C. Meta-Reinforcement Learning for Generalization Totackletheoverﬁttingproblem, meta-learningoffers alearn- ing paradigm [34]. Its core idea is to train on a distribution of related tasks to learn an inductive bias, enabling fast adaptation to new, unseen tasks with high sample efﬁciency at test time [35]. While conventional RL agents tend to overﬁt the training traces, Meta-Reinforcement Learning (Meta-RL) learns an adaptive policy that generalizes across different network environments from the task distribution [35].

**Fragmento 2 - p. 12 - score 6:**

This conﬁrms that EAStream is suitable for resource- constrained client deployments. D. Discussion and Limitations Despite the demonstrated advantages, we acknowledge cer- tain limitations of the EAStream framework. First, the ofﬂine meta-training process incurs higher computational overhead compared to standard DRL methods due to the joint optimization of the belief inference and policy modules. However, this cost is strictly conﬁned to the ofﬂine phase and does not impact the low-latency requirements of online inference. Second, the algorithm’s generalization capability is inherently dependent on the diversity of the network traces used during meta-training; a narrow task distribution may limit the effective range of adaptation.

**Fragmento 3 - p. 2 - score 5:**

Optimization-based methods [12], [13] learn an adaptable initialization but typically rely on online gradient updates during playback. This requirement introduces signiﬁcant computational overhead and latency, making them less ideal for resource-constrained devices. Conversely, the context-based method [14] adapts by inferring a latent context vector from history without online gradient updates. However, it relies on deterministic embeddings supervised solely by reward signals, which limits their ability to model the uncertainty of stochastic networks and fails to capture the underlying state transition dynamics. To overcome these limitations, we propose EAStream, a novel probabilistic context-based framework.

**Fragmento 4 - p. 2 - score 4:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1177 Despite these advantages, one challenge DRL-based ABR methods face is their limited generalization to unseen net- work conditions. This is because the learned policy is prone to overﬁtting to the training network environment. Such over- specialization is particularly problematic as real-world networks are inherently dynamic and non-stationary. In fact, when de- ployed in real-world scenarios, their performance has been shown to be even inferior to that of simple heuristic-based methods [10]. To tackle this generalization challenge, recent studies have introduced meta-reinforcement learning approaches, which gen- erally fall into two categories.

**Fragmento 5 - p. 3 - score 4:**

To handle extreme mobility, EIE-ABR [29] integrates environmental data to optimize streaming on high- speed railways. To address the black-box nature of deep learning, recent research has increasingly focused on interpretability. Peretto et al. [30] proposed an ML-assisted architecture providing inter- pretable prediction hints, and ComTree [31] used LLMs to select comprehensible decision trees. Furthermore, NeuroBA [32] pro- poses a neuro-symbolic framework, combining deep learning with logic reasoning to handle uncertainty and enhance inter- pretability. Despite these diverse advances, a key limitation persists: most learning-based agents suffer from poor generalization to unseen network conditions.

**Fragmento 6 - p. 12 - score 4:**

Finally, in extreme outlier scenarios that deviate signiﬁcantly from the training distribution, the inferred belief may become inaccurate. As noted in Section VI, leveraging the reconstruction error for anomaly detection offers a promising avenue to mitigate this issue in future work. VI. CONCLUSION This paper presents EAStream, a context-based meta- reinforcement learning framework designed to address the gen- eralization challenge in adaptive bitrate streaming. By modeling theproblemasaBAMDPandutilizingavariationalautoencoder, EAStream infers latent beliefs about network dynamics from interactionhistory.Thismechanismenablesthepolicytoachieve zero-shot adaptation to unseen network conditions without re- quiring computationally expensive online ﬁne-tuning.

**Fragmento 7 - p. 1 - score 3:**

However, the ABR algorithm faces challenges because it needs to balance conﬂicting ob- jectives: maximizing video quality and minimizing playback interruptions. Speciﬁcally, high bitrate chunks will be selected for better playback quality. However, it will increase the risk of playback stalls, especially in the case of unstable network conditions. Traditional ABR algorithms primarily rely on ﬁxed rules or control-theoretic models. Heuristic-based approaches, such as the rate-based FESTIVE [5] and the buffer-based BBA [6], make decisions using predeﬁned thresholds. While computationally efﬁcient and easy to deploy, these rule-based methods lack the ﬂexibility to adapt to diverse network scenarios or varying QoE preferences.

**Fragmento 8 - p. 1 - score 3:**

A comprehensive evaluation is conducted using diverse real-world network traces. Experimental results show that EAStream not only achieves leading performance on in-distribution test sets compared to state-of-the-art ABR algorithms, but also demonstrates superior generalization capability on out-of-distribution test scenarios. Index Terms—Adaptive video streaming, generalization, meta learning, network uncertainty, quality of experience. I. INTRODUCTION W ITH the rapid development of the Internet in recent years, video streaming has become the predominant Received 2 December 2025; revised 9 February 2026; accepted 3 March 2026. Date of publication 9 March 2026; date of current version 10 April 2026.

**Fragmento 9 - p. 2 - score 3:**

Unlike optimization- based methods, EAStream achieves robust generalization with- out any online parameter updates. Crucially, distinct from the previous context-based approach that relies on deterministic vectors, we formulate the ABR problem as a Bayesian Adap- tive Markov Decision Process (BAMDP) [15]. By leveraging a variational autoencoder to reconstruct both next states and rewards, EAStream infers a probabilistic belief distribution thatcapturestheenvironmentaldynamics.Thisenablestheagent to reason about uncertainty and adapt substantially better to unseen, non-stationary network conditions. In summary, the main contributions of this paper are as follows: r We innovatively adopted the Dynamic Adaptive Streaming over HTTP (DASH) architecture for video streaming, opti- mizing dynamic ABR decisions through a Bayesian Adap- tive Markov Decision Process (BAMDP) (Section III).

**Fragmento 10 - p. 2 - score 3:**

r We conduct extensive experiments across a diversity of real-world network traces (Section V). Our evaluations show that EAStream not only achieves state-of-the-art performance on in-distribution networks, but also shows better generalization ability in unseen, out-of-distribution environments compared to state-of-the-art algorithms. The remainder of this paper is structured as follows. Section II reviews the related work in ABR streaming and meta-reinforcement learning. Section III formulates the ABR problem and presents our Bayesian adaptive modeling approach. Section IV details the system design of our proposed EAStream framework, including its architecture and training methodology.

**Fragmento 11 - p. 5 - score 3:**

, (7) where H denotes the time horizon of a video streaming ses- sion, and γ ∈[0, 1] is the discount factor that determines the importance of future rewards. However, a core limitation of the standard MDP lies in its assumption of a stationary or perfectly known transition function P(st+1|st, at). This assumption is frequently violated in real-world networks, where conditions like bandwidth are highly dynamic and non-stationary. An ABR agent trained under one speciﬁc network trace may fail to generalize to other ﬂuctuating network conditions, leading to suboptimal performance. To address this limitation, where the true dynamics of the environment are unknown, we model the ABR problem as a Bayes-Adaptive Markov Decision Process (BAMDP) [15]. In a standard MDP, the agent assumes the network follows a ﬁxed rule. In contrast, a BAMDP agent acknowledges its ignorance about the speciﬁc network scenario. It maintains a belief state—a probabilistic “mental model” of the current net- work environment. As the agent observes new state transitions, it recursively updates this belief, allowing it to adapt its strategy dynamically based on its conﬁdence in the environment’s state. In this framework, the unknown network dynamics are treated as a latent variable. The agent maintains a belief state, bt, deﬁned as the posterior distribution over these possible network environments given the interaction history τ:t. The decision-making process in a BAMDP extends the stan- dard MDP cycle by incorporating a belief update step. The process proceeds as follows: 1) State Representation: At each timestep t, the agent’s state is a hyper-state s+ t = (st, bt), consisting of the observable physical state st and the current belief bt. 2) Action & Observation: The agent selects an action at. The env

**Fragmento 12 - p. 8 - score 3:**

Given this hidden state, the encoder performs forward passing to infer the belief mt. This belief represents the agent’s perception of the current network environment. Then the belief mt and the current state st are jointly input into the policy network πψ to decide the next chunk’s bitrate at. Finally, the agent performs the action and observes the new state and reward. During the entire online phase, the auxiliary decoder module is deprecated, and the agent operated in pure inference mode. Unlike the optimization-based meta-learning methods that require gradient updates during testing, our method relies solely on forward propagation. This structural design reduces computational overhead and makes it more suitable for resource-constrained client deployments.

**Fragmento 13 - p. 10 - score 3:**

This might be due to the highly unstable 4GNY trajectory (as shown in Table I), which suggests poor generalization of Pensieve. In contrast, EAStream maintains stable performance in both in-distribution and out-of- distribution tests. This generalization performance demonstrates the effectiveness of our meta-learning framework in learning to rapidly adapt to network uncertainty. C. Effectiveness Analysis ▷Case Study: We synthesized a challenging trajectory by concatenating 4GSyd and 3G segments to evaluate EAStream’s adaptability under abrupt non-stationary changes (e.g., a sharp bandwidth drop at 5 s). As shown in Fig. 10, EAStream achieved the highest QoE (1.40), outperforming Pensieve (1.21) and RobustMPC (1.07).

**Fragmento 14 - p. 1 - score 2:**

1176 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 EAStream: An Environment-Aware Adaptive Bitrate Algorithm for Reliable Video Streaming Services Zeming Huang, Wenjing Xiao , Miaojiang Chen , Member, IEEE, Zhiquan Liu , Min Chen , Fellow, IEEE, Athanasios V. Vasilakos , Senior Member, IEEE, Ahmed Farouk , and Houbing Herbert Song , Fellow, IEEE Abstract—Video streaming has emerged as a widely used Inter- net service, in which adaptive bitrate (ABR) algorithms play a crit- ical role in delivering high quality of experience (QoE). However, existing learning-based ABR methods often suffer from limited generalization in unseen and dynamically changing network condi- tions.

**Fragmento 15 - p. 3 - score 2:**

In a different structure, MetaABR [14] extracts latent contexts from historical trajectories to adjust policies without online gradient updates. However, it relies on deterministic embeddings, ignoring the inherent uncertainty in bandwidth evolution. In contrast, our proposed EAStream formulates the ABR problem as a BAMDP. By inferring a probabilistic belief over the environment via a VAE, our method explicitly models un- certainty, enabling robust zero-shot adaptation to unseen condi- tions. III. METHODS This section formulates the ABR decision process as an optimization task and models the network uncertainty using a BAMDP. We then propose a Meta-RL-based ABR algorithm, called EAStream, to approximate the BAMDP policy.

**Fragmento 16 - p. 3 - score 2:**

DeepBuffer [21] jointly controls the maximum buffer size to avoid unnecessary bandwidth consumption. GreenABR+ [22] employsaDDPG-basedapproachtoreducepowerconsumption. BE-ABR [23] uses Transformer-based prediction to minimize data waste. DRL has also been tailored for speciﬁc environments. In mobile edge computing (MEC), Guo et al. [24] jointly optimize transcoding and bitrate decisions. QAVA [25] addresses the fairness problem among multiple clients. Moreover, researchers tackle speciﬁc application challenges: CAST [26] prioritizes intricate video scenes, L2AC-E [27] minimizes latency for live streaming, and DeepVR [28] predicts user ﬁeld-of-view for panoramic video.

**Fragmento 17 - p. 8 - score 2:**

13: For each τj, infer latent belief mj ∼qφ(m|τj). 14: // Calculate weighted loss components 15: Lstate = −Ej,t[log pθ(sj,t+1|sj,t, aj,t, mj)]. 16: Lreward = −Ej,t[log pθ(rj,t+1| . . . , mj)]. 17: LKL = Ej[DKL(qφ(m|τj)||p(m))]. 18: LELBO = λsLstate + λrLreward + βLKL 19: Update φ, θ by minimizing LELBO. 20: end for separation prevents the belief learning from being biased by the policy’s early exploration. In each training iteration, multiple parallel agents collect interaction trajectories. The collected data is used to update the policy and belief modules separately. The policy network is updated using the Proximal Policy Optimization (PPO) algorithm [47].

**Fragmento 18 - p. 10 - score 2:**

In all subplots, EAStream is consistently positioned to the right of all other algorithms. This suggests that EAStream not only achieves a higher average QoE but also provides a more stable experience for the vast majority of users, minimizing the poor experience sessions. ▷Generalization to Unseen Network Environments. To evaluate the aspect of generalization, we now assess the per- formance on two unseen (out-of-distribution, OOD) test sets: Oboe and 4GNY. These network traces were not exposed to any learning-based models during the training phase. Fig. 6 illustrates the normalized average QoE scores for both QoE metrics on these two unseen datasets.

**Fragmento 19 - p. 11 - score 2:**

▷Overhead Analysis: To test the overhead of EAStream, we conducted a quantitative analysis of its computational overhead and memory usage. We compared EAStream with Pensieve, RobustMPC and NetLLM. The experiments were carried out Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 20 - p. 12 - score 2:**

2485–2503, Aug. 2022. [13] S. Wang, J. Lin, and Y. Dai, “MMVS: Enabling robust adaptive video streaming for wildly ﬂuctuating and heterogeneous networks,” IEEE Trans. Multimedia, vol. 26, pp. 11018–11030, 2024. [14] W. Li, X. Li, Y. Xu, Y. Yang, and S. Lu, “MetaABR: A meta-learning approach on adaptative bitrate selection for video streaming,” IEEE Trans. Mobile Comput., vol. 23, no. 3, pp. 2422–2437, Mar. 2024. [15] M. O. Duff, “Optimal Learning: Computational procedures for Bayes- adaptive Markov decision processes,” Univ. Massachusetts Amherst, Amherst, MA, USA, 2002. [16] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal bitrate adaptation for online videos,” IEEE/ACM Trans.

**Fragmento 21 - p. 12 - score 2:**

Extensive experiments on real-world datasets demonstrate that EAStream not only matches state-of-the-art performance on in-distribution traces but signiﬁcantly outperforms existing baselines in out-of- distribution scenarios. In future work, we intend to explore the online utilization of the Belief Decoder, which is currently only reserved for ofﬂine training. Speciﬁcally, we plan to leverage the real-time reconstruction errors for anomaly detection to identify extreme network outliers. REFERENCES [1] Sandvine, “2024 Global internet phenomena report,” 2024. [Online]. Available: https://www.applogicnetworks.com/global-internet-phenom ena-report-2024 [2] G.

**Fragmento 22 - p. 2 - score 1:**

By treating unknown parameters such as network bandwidth as random variables and maintaining a probability dis- tribution (posterior distribution) for them, the algorithm not only makes decisions based on the current estimated bandwidth, but also based on the complete state of all pos- sible bandwidth states and their occurrence probabilities, making ABR decisions more robust in dynamic network environments. r We propose EAStream (Section IV), a novel environment- aware ABR framework based on meta-reinforcement learning. Unlike optimization-based meta-learning meth- ods that require online ﬁne-tuning, EAStream leverages a context-based mechanism to adapt to new environments in real-time without any gradient updates during deployment.


### 8.10. ideas phase45 v1 controller

Palabras clave usadas: `safe, safety, risk, risk-aware, risk-calibrated, conservative, fallback, uncertainty, lower bound, buffer, low buffer, variable, fluctuation, tail, severe, rebuffering, stall, guidance, expert, hybrid, meta, environment-aware, trace skew, cluster, prioritize, fairness, multi-user, TCP, BPM, BSM`

**Fragmento 1 - p. 4 - score 5:**

Rebuffering Penalty: Rebuffering, or playback stalling, occurs when the playback buffer is depleted, severely degrading the user’s viewing experience. Let ˆCn denotes the average network throughput. The rebuffering time for chunk n, denoted as Tn, is thedurationbywhichitsdownloadtime,T(Rn) = dn(Rn)/ ˆCn, exceeds the buffer occupancy Bn−1 just before the download begins. It is calculated as: Tn = max {T(Rn) −Bn−1, 0} . (2) The total rebuffering penalty is the sum of all stall durations throughout the session: QoErebuf = N  n=1 Tn. (3) Quality Fluctuations Penalty: Frequent and large variations in video quality between consecutive chunks can be jarring to the user.

**Fragmento 2 - p. 3 - score 4:**

DeepBuffer [21] jointly controls the maximum buffer size to avoid unnecessary bandwidth consumption. GreenABR+ [22] employsaDDPG-basedapproachtoreducepowerconsumption. BE-ABR [23] uses Transformer-based prediction to minimize data waste. DRL has also been tailored for speciﬁc environments. In mobile edge computing (MEC), Guo et al. [24] jointly optimize transcoding and bitrate decisions. QAVA [25] addresses the fairness problem among multiple clients. Moreover, researchers tackle speciﬁc application challenges: CAST [26] prioritizes intricate video scenes, L2AC-E [27] minimizes latency for live streaming, and DeepVR [28] predicts user ﬁeld-of-view for panoramic video.

**Fragmento 3 - p. 5 - score 4:**

. (10) The strategy that achieves this goal is termed a Bayes-optimal policy. While this problem can theoretically be addressed via methods like posterior sampling [43] or Bayesian planning [44], these approaches typically incur prohibitive computational over- head for real-time ABR decisions. Computing exact belief up- dates is also generally infeasible in practice. Therefore, we leverageameta-reinforcementlearningparadigmtotacklethis issue, as detailed below. C. Approximating Bayes-Optimal Policies Via Meta-Learning The theoretical solution for BAMDP is computationally difﬁ- cult.Ourapproach,EAStream,employsameta-learningstrategy inspiredbyVariBAD[45]toacquireasolutionthatapproximates this policy. In the meta-learning framework, we model different network environments as individual tasks, each deﬁned by a hidden latent variable mi. This latent variable corresponds to the belief in BAMDP. Since the latent variable is unknown, the agent must infer information about mi from its historical information. Speciﬁcally,weemployanencodertotransformthetrajectoryτ:t into an inferred distribution qφ(m|τ:t) within the latent space. This distribution serves as an inference of the environment’s latent features. The learning process uses the framework of Variational Au- toencoder (VAE) [46]. We optimize the encoder network by maximizing the Variational Lower Bound (ELBO): ELBO = Eρ  Eqφ(m|τ:t)[log pθ(τ:H|m)] −DKL(qφ(m|τ:t)||pθ(m))] . (11) Here, ρ denotes the trajectory distribution induced by the current policy π and the initial state distribution ρ0. This equation consists of two components. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore. Restrictions apply.

**Fragmento 4 - p. 1 - score 3:**

However, the ABR algorithm faces challenges because it needs to balance conﬂicting ob- jectives: maximizing video quality and minimizing playback interruptions. Speciﬁcally, high bitrate chunks will be selected for better playback quality. However, it will increase the risk of playback stalls, especially in the case of unstable network conditions. Traditional ABR algorithms primarily rely on ﬁxed rules or control-theoretic models. Heuristic-based approaches, such as the rate-based FESTIVE [5] and the buffer-based BBA [6], make decisions using predeﬁned thresholds. While computationally efﬁcient and easy to deploy, these rule-based methods lack the ﬂexibility to adapt to diverse network scenarios or varying QoE preferences.

**Fragmento 5 - p. 1 - score 3:**

Although some meta-reinforcement learning techniques have been proposed to mitigate this issue, they generally depend on additional online training or ﬁne-tuning. To overcome these lim- itations, this paper introduces EAStream, an environment-aware ABR algorithm based on meta-reinforcement learning for reliable video streaming services. The method employs a variational au- toencoder to extract a latent representation of the current network environment from historical interaction data. This latent variable, along with the current system state, is fed into a policy network that perceives network conditions in real time and adapts bitrate decisions accordingly, without requiring further online training.

**Fragmento 6 - p. 3 - score 3:**

More advanced methods like PEARL [41] extend this by training a probabilistic encoder to infer latent context variables from off-policy data, signiﬁcantly improving meta-training sample efﬁciency. Several recent works have applied optimization-based meta- learning to the ABR problem, requiring an online training phase to adapt. For instance, A2BR [12] employs a MAML- based framework to learn a meta-policy ofﬂine, which is then rapidly ﬁne-tuned online to create a tailor-made policy for speciﬁc network conditions. Similarly, MMVS [13] integrates the MAML-based framework with PPO to handle highly ﬂuc- tuating networks, and proposes a meta advantage normalization technique to stabilize the online adaptation process.

**Fragmento 7 - p. 3 - score 3:**

1178 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 Pensieve [8] employs Deep Reinforcement Learning (DRL) and outperforms traditional algorithms. The success of Pensieve has motivated a series of studies on Learning-based ABR algorithms. For instance, Comyco [9] employs imitation learning to enhance sample efﬁciency. Tiyuntsong [19] introduces a self-play framework to clearly deﬁne the optimization objective. Another major direction focuses on jointly optimizing bitrate with other metrics. Early works like AMIS [20] manage both bi- trate and playout speed to mitigate the risk of rebuffering. Recent studies extend these objectives to energy and trafﬁc efﬁciency.

**Fragmento 8 - p. 4 - score 3:**

The ﬂuctuations penalty is calculated by accumulating the absolute variations in quality value across consecutive chunks. QoEvar = N  n=2 |q(Rn) −q(Rn−1)| . (4) QoE Objective: The ﬁnal QoE objective is deﬁned as a linear combination of these three components: QoE = μ1QoEqual −μ2QoErebuf −μ3QoEvar, (5) where µ = (μ1, μ2, μ3) is a vector of non-negative weighting coefﬁcients. These coefﬁcients are customizable hyperparam- eters representing different user preferences. For instance, in- creasing μ2 will penalize rebuffering more heavily, guiding the algorithm towards a more conservative strategy to ensure smooth playback. In our experiments, we adopt standard ﬁxed settings for fair comparison.

**Fragmento 9 - p. 8 - score 3:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1183 Algorithm 1: Ofﬂine Meta-Training. 1: Initialize belief params φ, θ; policy params ψ; entropy weight α; target entropy Htarget; 2: Initialize replay buffer Dbelief; loss weights λs, λr, β. 3: for each training iteration do 4: Collect a batch of recent trajectories {τi}. 5: Store trajectories {τi} in Dbelief. 6: //Update Policy Module 7: Compute belief mt for {τi} using ﬁxed encoder qφ. 8: Update ψ by minimizing PPO loss: L(ψ) = ˆEt[−LCLIP(ψ) + LVF(ψ) −αH[πψ](st, mt)] 9: Compute average entropy ¯H = ˆEt[H[πψ(·|st, mt)]] 10: Update entropy weight α ←α −( ¯H −Htarget) 11: //Update Belief Module 12: Sample a batch of trajectories {τj} ∼Dbelief.

**Fragmento 10 - p. 1 - score 2:**

A comprehensive evaluation is conducted using diverse real-world network traces. Experimental results show that EAStream not only achieves leading performance on in-distribution test sets compared to state-of-the-art ABR algorithms, but also demonstrates superior generalization capability on out-of-distribution test scenarios. Index Terms—Adaptive video streaming, generalization, meta learning, network uncertainty, quality of experience. I. INTRODUCTION W ITH the rapid development of the Internet in recent years, video streaming has become the predominant Received 2 December 2025; revised 9 February 2026; accepted 3 March 2026. Date of publication 9 March 2026; date of current version 10 April 2026.

**Fragmento 11 - p. 2 - score 2:**

HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES 1177 Despite these advantages, one challenge DRL-based ABR methods face is their limited generalization to unseen net- work conditions. This is because the learned policy is prone to overﬁtting to the training network environment. Such over- specialization is particularly problematic as real-world networks are inherently dynamic and non-stationary. In fact, when de- ployed in real-world scenarios, their performance has been shown to be even inferior to that of simple heuristic-based methods [10]. To tackle this generalization challenge, recent studies have introduced meta-reinforcement learning approaches, which gen- erally fall into two categories.

**Fragmento 12 - p. 2 - score 2:**

By treating unknown parameters such as network bandwidth as random variables and maintaining a probability dis- tribution (posterior distribution) for them, the algorithm not only makes decisions based on the current estimated bandwidth, but also based on the complete state of all pos- sible bandwidth states and their occurrence probabilities, making ABR decisions more robust in dynamic network environments. r We propose EAStream (Section IV), a novel environment- aware ABR framework based on meta-reinforcement learning. Unlike optimization-based meta-learning meth- ods that require online ﬁne-tuning, EAStream leverages a context-based mechanism to adapt to new environments in real-time without any gradient updates during deployment.

**Fragmento 13 - p. 2 - score 2:**

r We conduct extensive experiments across a diversity of real-world network traces (Section V). Our evaluations show that EAStream not only achieves state-of-the-art performance on in-distribution networks, but also shows better generalization ability in unseen, out-of-distribution environments compared to state-of-the-art algorithms. The remainder of this paper is structured as follows. Section II reviews the related work in ABR streaming and meta-reinforcement learning. Section III formulates the ABR problem and presents our Bayesian adaptive modeling approach. Section IV details the system design of our proposed EAStream framework, including its architecture and training methodology.

**Fragmento 14 - p. 3 - score 2:**

In a different structure, MetaABR [14] extracts latent contexts from historical trajectories to adjust policies without online gradient updates. However, it relies on deterministic embeddings, ignoring the inherent uncertainty in bandwidth evolution. In contrast, our proposed EAStream formulates the ABR problem as a BAMDP. By inferring a probabilistic belief over the environment via a VAE, our method explicitly models un- certainty, enabling robust zero-shot adaptation to unseen condi- tions. III. METHODS This section formulates the ABR decision process as an optimization task and models the network uncertainty using a BAMDP. We then propose a Meta-RL-based ABR algorithm, called EAStream, to approximate the BAMDP policy.

**Fragmento 15 - p. 3 - score 2:**

Other works focus on improving adaptation in high-dimensional parameter spaces. For instance, LEO [39] decouples the adaptation from the high-dimensional parameter space via the construction of a latent embedding con- ditioned on the data and conducting the meta-learning updates in this low-dimensional space. In contrast, context-based methods learn a single policy con- ditioned on a task-speciﬁc context variable, which summarizes the agent’s interaction history and enables adaptation without test-time gradient updates. A pioneering approach, RL2 [40], uses a recurrent neural network (RNN) to implicitly infer the en- vironment’s underlying dynamics.

**Fragmento 16 - p. 4 - score 2:**

. . , N}. (6) The constraints of this formulation model the core dynamics of a streaming session: r Time Evolution: The ﬁrst constraint describes the change of the next decision point tn+1. The next time point equates to the sum of the current time tn, the download time T(Rn), and the possible rebuffering time Tn. r Network Throughput: The second constraint is the average network throughput ˆCn when downloading chunk n. It is calculated by integrating the instantaneous throughput c(t) with the actual download time. r Buffer Dynamics: The third constraint represents the change of buffer occupancy. Speciﬁcally, L represents the ﬁxed duration of a chunk.

**Fragmento 17 - p. 5 - score 2:**

1180 IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026 The buffer level Bn is always capped between zero and a maximum capacity Bmax. Finally, the chosen bitrate Rn must belong to the discrete set of available bitrates R. B. Bayesian Adaptive Modeling for Environmental Uncertainty To solve the problem, a common and effective approach is to use Reinforcement Learning (RL) based on a Markov Decision Process (MDP). The system consists of (S, A, R, P, ρ0, γ, H). Here, P is the state transition function and ρ0 is the initial state distribution. The agent’s objective is to learn a policy π that maximizes the long-term cumulative reward: J(π) = Eρ0,P,π H−1  t=0 γtR(rt+1|st, at, st+1)

**Fragmento 18 - p. 6 - score 2:**

Consequently, the agent can adapt its decision-making process in response to the estimated hidden dynamics. The overall training objective is to optimize the combined objective: L(φ, θ, ψ) = Ep(M) [J(ψ, φ) + λ · ELBO(φ, θ)] , (13) where Ep(M) denotes the expectation over the task distribution p(M). In this equation, J(ψ, φ) denotes the expected return for approximate policy, and the second term is the task inference objective. The hyperparameter λ controls the trade-off between maximizing the RL reward and the accuracy of belief recon- struction. Fig. 3. Architecture of the Belief Inference Module. IV. SYSTEM DESIGN This section details the architecture and training methodol- ogy of EAStream, our proposed meta-reinforcement learning framework for adaptive bitrate streaming.

**Fragmento 19 - p. 7 - score 2:**

This allows the policy to learn not just one ﬁxed strategy, but a highly adaptive meta-policy. B. State, Action, and Reward Deﬁnition To train the DRL agent, this section explicitly deﬁnes the reward function, as well as the state and action space. ▷State: For every time step t, the agent receives a state st. This state is a multi-dimensional vector that includes in- formation about the playback status and network conditions. Following the design of Pensieve [8], we formulate the state st as follows: st = (⃗xt, ⃗τt, ⃗nt, bt, ct, lt). (14) Here, ⃗xt and ⃗τt are vectors representing the historical throughput and transmission time of the past w video chunks(We set w = 8 following the standard conﬁguration in [8].); ⃗nt denotes the ﬁle size for K available bitrates of next chunk; bt is the current buffer occupancy; ct denotes the number of unplayed chunks; and lt denotes the last chunk’s bitrate.

**Fragmento 20 - p. 7 - score 2:**

▷Action: In an ABR system, the agent’s task is to select the video quality for the subsequent chunk. The action space A is thus formulated as a discrete set: A = {0, 1, . . . , K −1}. (15) Here, K represents the number of candidate bitrates. These discrete options correspond to different video resolutions such as 360p, 480p, 720p, and 1080p. ▷Reward: To optimize the QoE objective in (5), we deﬁne the reward function rt accordingly. Once the t-th video chunk has been successfully transmitted, the agent will receive a reward of rt: rt = μ1 · q(Rt) −μ2 · Tt −μ3 · |q(Rt) −q(Rt−1)|. (16) This reward function directly guides the behavior of the agent. It enables agent to learn strategies for choosing high-quality chunks while reducing rebuffering and bitrate changes.

**Fragmento 21 - p. 7 - score 2:**

In parallel, the Critic Network with a similar architecture outputs a state value estimation V (st, mt) to guide the learning of the actor. D. Ofﬂine Training and Online Adaptation This section details the learning and adaptation workﬂow of EAStream. The process consists of two stages summarized in Algorithm 1 and Algorithm 2 respectively. ▷Ofﬂine Meta-Training: This stage aims to learn a meta- policy capable of inferring environmental characteristics and adapting decisions across diverse network conditions. By ex- posing the agent to a wide variety of environments at this stage, we force it to learn how to identify potential network conditions rather than memorizing speciﬁc training trajectories.

**Fragmento 22 - p. 8 - score 2:**

While off-policy algorithms like SAC are known for high sample efﬁciency, we explicitly select the on-policy PPO to ensure training stability in our meta-learning framework. Since the Belief Encoder evolves continuously, data stored in an off-policy replay buffer would contain obsolete belief representations. PPO avoids this issue by strictly learning from fresh trajectories consistent with the current encoder. We utilize the clipped surrogate objective to prevent destruc- tive large updates: LCLIP(ψ) = ˆEt  min  rt(ψ) ˆAt, clip(rt(ψ), 1 −ϵ, 1 + ϵ) ˆAt  , (17) where rt(ψ) is the probability ratio, ϵ is a hyperparameter used to limit the variation of the probability ratio and ˆAt is the advantage estimate.


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
1176
IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026
EAStream: An Environment-Aware Adaptive Bitrate
Algorithm for Reliable Video Streaming Services
Zeming Huang, Wenjing Xiao
, Miaojiang Chen
, Member, IEEE, Zhiquan Liu
, Min Chen
, Fellow, IEEE,
Athanasios V. Vasilakos
, Senior Member, IEEE, Ahmed Farouk
, and Houbing Herbert Song
, Fellow, IEEE
Abstract—Video streaming has emerged as a widely used Inter-
net service, in which adaptive bitrate (ABR) algorithms play a crit-
ical role in delivering high quality of experience (QoE). However,
existing learning-based ABR methods often suffer from limited
generalization in unseen and dynamically changing network condi-
tions. Although some meta-reinforcement learning techniques have
been proposed to mitigate this issue, they generally depend on
additional online training or ﬁne-tuning. To overcome these lim-
itations, this paper introduces EAStream, an environment-aware
ABR algorithm based on meta-reinforcement learning for reliable
video streaming services. The method employs a variational au-
toencoder to extract a latent representation of the current network
environment from historical interaction data. This latent variable,
along with the current system state, is fed into a policy network
that perceives network conditions in real time and adapts bitrate
decisions accordingly, without requiring further online training.
A comprehensive evaluation is conducted using diverse real-world
network traces. Experimental results show that EAStream not only
achieves leading performance on in-distribution test sets compared
to state-of-the-art ABR algorithms, but also demonstrates superior
generalization capability on out-of-distribution test scenarios.
Index Terms—Adaptive video streaming, generalization, meta
learning, network uncertainty, quality of experience.
I. INTRODUCTION
W
ITH the rapid development of the Internet in recent
years, video streaming has become the predominant
Received 2 December 2025; revised 9 February 2026; accepted 3 March
2026. Date of publication 9 March 2026; date of current version 10 April 2026.
This work was supported in part by the National Natural Science Foundation of
China under Grant 62462002 and Grant 62502101, in part by the Natural Science
Foundation of Guangxi, China under Grant 2025GXNSFAA069958 and Grant
2025GXNSFBA069394, and in part by the Key Research and Development
Program of Guangxi under Grant AD25069071. (Zeming Huang and Wenjing
Xiao are co-ﬁrst authors.) (Corresponding author: Miaojiang Chen.)
Zeming Huang, Wenjing Xiao, and Miaojiang Chen are with the School
of Computer, Electronics and Information, Guangxi University, Nanning
530004, China, and also with the Guangxi Key Laboratory of Multimedia
Communications and Network Technology, Nanning 530004, China (e-mail:
zem@st.gxu.edu.cn; wenjingx@gxu.edu.cn; mjchen_cs@gxu.edu.cn).
Zhiquan Liu is with the College of Cyber Security, Jinan University,
Guangzhou 510632, China (e-mail: zqliu@jnu.edu.cn).
Min Chen is with the School of Computer Science and Engineering, South
China University of Technology, Guangzhou 510006, China, and also with
Pazhou Laboratory, Guangzhou 510330, China (e-mail: minchen@ieee.org).
Athanasios V. Vasilakos is with the Department of ICT and Center for
AI Research, University of Agder(UiA), 4879 Grimstad, Norway (e-mail:
thanos.vasilakos@uia.no).
Ahmed
Farouk
is
with
the
Faculty
of
Computers
and
Artiﬁcial
Intelligence,
Hurghada
University,
Hurghada
83523,
Egypt
(e-mail:
ahmed.farouk@sci.svu.edu.eg).
Houbing Herbert Song is with the Department of Information Systems,
University of Maryland, Baltimore, MD 21250 USA (e-mail: h.song@ieee.org).
Digital Object Identiﬁer 10.1109/TSC.2026.3671090
component of global Internet trafﬁc. According to the Global
Internet Phenomena Report 2024 [1], the trafﬁc transporting
video accounts for 68% and 64% of the total downlink trafﬁc of
ﬁxed and mobile networks, respectively. Given the industry’s
projected growth to $416.84 billion by 2030 [2], ensuring a
superiorQualityofExperience(QoE)iscriticalforuserretention
and business success. To achieve this, Adaptive Bitrate (ABR)
technology has been widely adopted as the standard delivery
mechanism [3], [4]. By dividing videos into chunks available
at multiple quality levels, ABR algorithms dynamically select
the optimal bitrate for each chunk based on real-time network
throughput and buffer occupancy. However, the ABR algorithm
faces challenges because it needs to balance conﬂicting ob-
jectives: maximizing video quality and minimizing playback
interruptions. Speciﬁcally, high bitrate chunks will be selected
for better playback quality. However, it will increase the risk
of playback stalls, especially in the case of unstable network
conditions.
Traditional ABR algorithms primarily rely on ﬁxed rules or
control-theoretic models. Heuristic-based approaches, such as
the rate-based FESTIVE [5] and the buffer-based BBA [6], make
decisions using predeﬁned thresholds. While computationally
efﬁcient and easy to deploy, these rule-based methods lack
the ﬂexibility to adapt to diverse network scenarios or varying
QoE preferences. To address this, Model Predictive Control
(MPC) [7] was introduced to enable proactive decision-making
by optimizing QoE over a future horizon based on throughput
predictions. Although MPC generally outperforms heuristics,
its reliability heavily depends on the accuracy of bandwidth
estimation.
In recent years, considerable attention has been directed to-
wards applying learning-based methods to ABR streaming [8],
[9], [10], [11]. In contrast to traditional heuristic-based meth-
ods, learning-based methods typically train neural networks
on datasets spanning multiple network conditions. This allows
them to capture the complicated correlations in video streaming.
The seminal method, Pensieve [8], uses deep reinforcement
learning algorithm (DRL) to learn bitrate adaptation policies.
Unlike the MPC-based methods that rely on system models,
the DRL algorithm directly learns the model-free strategies
from experience, enabling it to better handle dynamic networks.
Furthermore, DRL algorithms have long-term planning capa-
bilities, which allows them to make complex strategic trade-
offs that balance instant video quality and long-term viewing
stability.
1939-1374 © 2026 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and similar technologies.
Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 2

```text
HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES
1177
Despite these advantages, one challenge DRL-based ABR
methods face is their limited generalization to unseen net-
work conditions. This is because the learned policy is prone
to overﬁtting to the training network environment. Such over-
specialization is particularly problematic as real-world networks
are inherently dynamic and non-stationary. In fact, when de-
ployed in real-world scenarios, their performance has been
shown to be even inferior to that of simple heuristic-based
methods [10].
To tackle this generalization challenge, recent studies have
introduced meta-reinforcement learning approaches, which gen-
erally fall into two categories. Optimization-based methods [12],
[13] learn an adaptable initialization but typically rely on online
gradient updates during playback. This requirement introduces
signiﬁcant computational overhead and latency, making them
less ideal for resource-constrained devices. Conversely, the
context-based method [14] adapts by inferring a latent context
vector from history without online gradient updates. However, it
relies on deterministic embeddings supervised solely by reward
signals, which limits their ability to model the uncertainty of
stochastic networks and fails to capture the underlying state
transition dynamics.
To overcome these limitations, we propose EAStream, a novel
probabilistic context-based framework. Unlike optimization-
based methods, EAStream achieves robust generalization with-
out any online parameter updates. Crucially, distinct from
the previous context-based approach that relies on deterministic
vectors, we formulate the ABR problem as a Bayesian Adap-
tive Markov Decision Process (BAMDP) [15]. By leveraging
a variational autoencoder to reconstruct both next states and
rewards, EAStream infers a probabilistic belief distribution
thatcapturestheenvironmentaldynamics.Thisenablestheagent
to reason about uncertainty and adapt substantially better to
unseen, non-stationary network conditions.
In summary, the main contributions of this paper are as
follows:
r We innovatively adopted the Dynamic Adaptive Streaming
over HTTP (DASH) architecture for video streaming, opti-
mizing dynamic ABR decisions through a Bayesian Adap-
tive Markov Decision Process (BAMDP) (Section III). By
treating unknown parameters such as network bandwidth
as random variables and maintaining a probability dis-
tribution (posterior distribution) for them, the algorithm
not only makes decisions based on the current estimated
bandwidth, but also based on the complete state of all pos-
sible bandwidth states and their occurrence probabilities,
making ABR decisions more robust in dynamic network
environments.
r We propose EAStream (Section IV), a novel environment-
aware ABR framework based on meta-reinforcement
learning. Unlike optimization-based meta-learning meth-
ods that require online ﬁne-tuning, EAStream leverages a
context-based mechanism to adapt to new environments in
real-time without any gradient updates during deployment.
r We conduct extensive experiments across a diversity of
real-world network traces (Section V). Our evaluations
show that EAStream not only achieves state-of-the-art
performance on in-distribution networks, but also shows
better generalization ability in unseen, out-of-distribution
environments compared to state-of-the-art algorithms.
The remainder of this paper is structured as follows.
Section II reviews the related work in ABR streaming and
meta-reinforcement learning. Section III formulates the ABR
problem and presents our Bayesian adaptive modeling approach.
Section IV details the system design of our proposed EAStream
framework, including its architecture and training methodology.
Section V presents the comprehensive experimental evalua-
tion and analysis of results. Finally, Section VI concludes the
paper.
II. RELATED WORK
This section will review the related work in the ﬁelds of
ABR streaming and meta-learning, particularly focusing on
meta-reinforcement learning.
A. Conventional ABR Algorithms
ABR streaming has been the subject of extensive research in
the ﬁeld of network communication over the past decade. Early
ABR algorithms primarily relied on explicitly deﬁned rules and
mathematical models. These approaches are typically classiﬁed
into two main categories: heuristic-based methods and control-
theoretic methods.
Heuristic-based methods represent the earliest class of ABR
algorithms, selecting bitrates through intuitive, pre-deﬁned
rules. These are primarily categorized into two classes: rate-
based and buffer-based. Rate-based algorithms, such as FES-
TIVE [5], guide their decisions by measuring historical network
throughput. To address the lag problem of rate-based methods,
buffer-based algorithms use buffer occupancy as a key metric.
BBA [6] matches bitrate actions by setting different buffer
thresholds. The more sophisticated algorithm BOLA [16] is
based on Lyapunov optimization to maximize the QoE while
ensuring that the buffer is not exhausted. Although the heuristic
methodissimpleandeffective,theﬁxedrulesalsolimititsability
to adapt to the dynamic and unstable network environment.
To address the passivity of heuristic approaches, re-
searchers have introduced prospective control-theoretic ap-
proaches. Among these approaches, Model Predictive Control
(MPC) [7] is the most inﬂuential. MPC-based algorithms use
the predictive bandwidth to optimize a series of bitrate decisions
over the future horizon. Subsequent research has focused on en-
hancing MPC’s core issue of prediction accuracy. For instance,
Fugu [10] improves the prediction module by using a deep neural
network, while AAR [17] utilizes server-assisted information
to achieve more accurate bandwidth prediction. Beyond MPC,
other classical control models have also been explored, such
as PIA [18] uses a PI controller to stabilize the playout buffer
at the target level. The effectiveness of these approaches is
fundamentally dependent on the model’s accuracy. However,
this is a challenge in real dynamic network environments.
B. Learning-Based ABR Algorithms
In recent years, more research has been conducted on ABR al-
gorithms based on reinforcement learning. The pioneering work
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 3

```text
1178
IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026
Pensieve [8] employs Deep Reinforcement Learning (DRL) and
outperforms traditional algorithms.
The success of Pensieve has motivated a series of studies
on Learning-based ABR algorithms. For instance, Comyco [9]
employs imitation learning to enhance sample efﬁciency.
Tiyuntsong [19] introduces a self-play framework to clearly
deﬁne the optimization objective.
Another major direction focuses on jointly optimizing bitrate
with other metrics. Early works like AMIS [20] manage both bi-
trate and playout speed to mitigate the risk of rebuffering. Recent
studies extend these objectives to energy and trafﬁc efﬁciency.
DeepBuffer [21] jointly controls the maximum buffer size to
avoid unnecessary bandwidth consumption. GreenABR+ [22]
employsaDDPG-basedapproachtoreducepowerconsumption.
BE-ABR [23] uses Transformer-based prediction to minimize
data waste.
DRL has also been tailored for speciﬁc environments. In
mobile edge computing (MEC), Guo et al. [24] jointly optimize
transcoding and bitrate decisions. QAVA [25] addresses the
fairness problem among multiple clients. Moreover, researchers
tackle speciﬁc application challenges: CAST [26] prioritizes
intricate video scenes, L2AC-E [27] minimizes latency for live
streaming, and DeepVR [28] predicts user ﬁeld-of-view for
panoramic video. To handle extreme mobility, EIE-ABR [29]
integrates environmental data to optimize streaming on high-
speed railways.
To address the black-box nature of deep learning, recent
research has increasingly focused on interpretability. Peretto
et al. [30] proposed an ML-assisted architecture providing inter-
pretable prediction hints, and ComTree [31] used LLMs to select
comprehensible decision trees. Furthermore, NeuroBA [32] pro-
poses a neuro-symbolic framework, combining deep learning
with logic reasoning to handle uncertainty and enhance inter-
pretability.
Despite these diverse advances, a key limitation persists: most
learning-based agents suffer from poor generalization to unseen
network conditions. To address this, a recent work NetLLM [33]
explores adapting Large Language Models (LLMs) as universal
foundation models to handle diverse networking tasks. However,
it introduces signiﬁcant computational overhead and latency,
making it less ideal for real-time deployment on resource-
constrained devices.
C. Meta-Reinforcement Learning for Generalization
Totackletheoverﬁttingproblem, meta-learningoffers alearn-
ing paradigm [34]. Its core idea is to train on a distribution of
related tasks to learn an inductive bias, enabling fast adaptation
to new, unseen tasks with high sample efﬁciency at test time [35].
While conventional RL agents tend to overﬁt the training traces,
Meta-Reinforcement Learning (Meta-RL) learns an adaptive
policy that generalizes across different network environments
from the task distribution [35].
Broadly, Meta-RL methods are typically categorized as two
main paradigms: optimization-based and context-based.
Optimization-based methods learn a sensitive parameter ini-
tialization that allows for rapid adaptation via a few gradient
steps. A canonical example is Model-Agnostic Meta-Learning
(MAML) [36], which meta-learns a shared prior for fast ﬁne-
tuning. However, MAML’s reliance on second-order derivatives
is computationally expensive. To address this, more efﬁcient,
ﬁrst-order alternatives were developed. FOMAML [37] and
Reptile [38] simplify the update by ignoring or approximating
higher-order terms, avoiding the need to differentiate through
the entire optimization process. Other works focus on improving
adaptation in high-dimensional parameter spaces. For instance,
LEO [39] decouples the adaptation from the high-dimensional
parameter space via the construction of a latent embedding con-
ditioned on the data and conducting the meta-learning updates
in this low-dimensional space.
In contrast, context-based methods learn a single policy con-
ditioned on a task-speciﬁc context variable, which summarizes
the agent’s interaction history and enables adaptation without
test-time gradient updates. A pioneering approach, RL2 [40],
uses a recurrent neural network (RNN) to implicitly infer the en-
vironment’s underlying dynamics. More advanced methods like
PEARL [41] extend this by training a probabilistic encoder to
infer latent context variables from off-policy data, signiﬁcantly
improving meta-training sample efﬁciency.
Several recent works have applied optimization-based meta-
learning to the ABR problem, requiring an online training
phase to adapt. For instance, A2BR [12] employs a MAML-
based framework to learn a meta-policy ofﬂine, which is then
rapidly ﬁne-tuned online to create a tailor-made policy for
speciﬁc network conditions. Similarly, MMVS [13] integrates
the MAML-based framework with PPO to handle highly ﬂuc-
tuating networks, and proposes a meta advantage normalization
technique to stabilize the online adaptation process. In a different
structure, MetaABR [14] extracts latent contexts from historical
trajectories to adjust policies without online gradient updates.
However, it relies on deterministic embeddings, ignoring the
inherent uncertainty in bandwidth evolution.
In contrast, our proposed EAStream formulates the ABR
problem as a BAMDP. By inferring a probabilistic belief over
the environment via a VAE, our method explicitly models un-
certainty, enabling robust zero-shot adaptation to unseen condi-
tions.
III. METHODS
This section formulates the ABR decision process as an
optimization task and models the network uncertainty using a
BAMDP. We then propose a Meta-RL-based ABR algorithm,
called EAStream, to approximate the BAMDP policy.
A. Problem Formulation
As shown in Fig. 1, a typical ABR streaming system involves
complex video content preparation and delivery. The server
ﬁrst encodes the raw video into multiple bitrate levels, each
corresponding to a discrete value in the set R. Each of these
transcoded videos is then split into a series of N smaller chunks,
all sharing a ﬁxed duration of L seconds. Simultaneously, a
manifest ﬁle named Media Presentation Description (MPD) is
created to provide metadata for the video stream.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 4

```text
HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES
1179
Fig. 1.
A schematic representation of the Dynamic Adaptive Streaming over
HTTP (DASH) architecture.
These prepared chunks and MPD ﬁles are often hosted on
a Content Delivery Network (CDN) [42] for efﬁcient delivery.
When the client player starts playing a video, it will ﬁrst request
the MPD ﬁle, which will inform the client of the URL to request
the video. The player then dynamically requests video chunks
sequentially. For each chunk n, the ABR algorithm selects a
bitrate Rn ∈R. The bitrate selection determines the chunk size
dn(Rn), which is then downloaded from the CDN through a
network with an average throughput of Cn.
The goal of the ABR algorithm is to optimize the long-term
QoE of users. QoE evaluates the subjective satisfaction of users,
which is composed of three components: video quality, rebuffer-
ing, and quality ﬂuctuations.
Video Quality: The video quality reﬂects the perceived visual
quality derived from the bitrate Rn of each video chunk. Users
tend to watch videos with high average visual quality. It is
calculated based on the sum of the n-th chunk:
QoEqual =
N

n=1
q(Rn),
(1)
where q(Rn) represents the video quality level for the bitrate
Rn. The selection of q(Rn) commonly includes the raw bitrate
Rn and a logarithmic mapping log(Rn) to reﬂect diminishing
returns of higher bitrate.
Rebuffering Penalty: Rebuffering, or playback stalling, occurs
when the playback buffer is depleted, severely degrading the
user’s viewing experience. Let ˆCn denotes the average network
throughput. The rebuffering time for chunk n, denoted as Tn, is
thedurationbywhichitsdownloadtime,T(Rn) = dn(Rn)/ ˆCn,
exceeds the buffer occupancy Bn−1 just before the download
begins. It is calculated as:
Tn = max {T(Rn) −Bn−1, 0} .
(2)
The total rebuffering penalty is the sum of all stall durations
throughout the session:
QoErebuf =
N

n=1
Tn.
(3)
Quality Fluctuations Penalty: Frequent and large variations in
video quality between consecutive chunks can be jarring to the
user. The ﬂuctuations penalty is calculated by accumulating the
absolute variations in quality value across consecutive chunks.
QoEvar =
N

n=2
|q(Rn) −q(Rn−1)| .
(4)
QoE Objective: The ﬁnal QoE objective is deﬁned as a linear
combination of these three components:
QoE = μ1QoEqual −μ2QoErebuf −μ3QoEvar,
(5)
where µ = (μ1, μ2, μ3) is a vector of non-negative weighting
coefﬁcients. These coefﬁcients are customizable hyperparam-
eters representing different user preferences. For instance, in-
creasing μ2 will penalize rebuffering more heavily, guiding the
algorithm towards a more conservative strategy to ensure smooth
playback. In our experiments, we adopt standard ﬁxed settings
for fair comparison.
Therefore, the ABR decision-making process can be modeled
as an optimization task subject to constraints. The task is to de-
termine the optimal sequence of bitrates R = (R1, R2, . . ., RN)
that maximizes the total QoE, subject to the system’s dynamic
constraints. This objective balances aggressive bitrate selection
against the physical constraints of buffer dynamics, ensuring that
the stochastic network supply meets the deterministic playback
demand. Mathematically, this is formulated as:
maxR1,...,RN QoE,
s.t.
⎧
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎩
tn+1 = tn + T(Rn) + Tn,
ˆCn =
1
T (Rn)
 tn+T (Rn)
tn
c(t)dt,
Bn+1 = max(0, Bn −T(Rn)) + L,
B1 = Ts,
0 ≤Bn ≤Bmax,
Rn ∈R, ∀n ∈{1, . . . , N}.
(6)
The constraints of this formulation model the core dynamics
of a streaming session:
r Time Evolution: The ﬁrst constraint describes the change of
the next decision point tn+1. The next time point equates to
the sum of the current time tn, the download time T(Rn),
and the possible rebuffering time Tn.
r Network Throughput: The second constraint is the average
network throughput ˆCn when downloading chunk n. It is
calculated by integrating the instantaneous throughput c(t)
with the actual download time.
r Buffer Dynamics: The third constraint represents the
change of buffer occupancy. Speciﬁcally, L represents the
ﬁxed duration of a chunk. The new buffer level Bn+1 is
calculated by subtracting the download time T(Rn) from
the previous level Bn and adding the duration L of the new
downloaded chunk.
r Boundary Conditions: The ﬁnal constraints set the bound-
ary conditions. B1 = Ts deﬁnes the initial buffer level.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 5

```text
1180
IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026
The buffer level Bn is always capped between zero and
a maximum capacity Bmax. Finally, the chosen bitrate Rn
must belong to the discrete set of available bitrates R.
B. Bayesian Adaptive Modeling for Environmental
Uncertainty
To solve the problem, a common and effective approach is to
use Reinforcement Learning (RL) based on a Markov Decision
Process (MDP). The system consists of (S, A, R, P, ρ0, γ, H).
Here, P is the state transition function and ρ0 is the initial state
distribution. The agent’s objective is to learn a policy π that
maximizes the long-term cumulative reward:
J(π) = Eρ0,P,π
H−1

t=0
γtR(rt+1|st, at, st+1)
	
,
(7)
where H denotes the time horizon of a video streaming ses-
sion, and γ ∈[0, 1] is the discount factor that determines the
importance of future rewards. However, a core limitation of the
standard MDP lies in its assumption of a stationary or perfectly
known transition function P(st+1|st, at). This assumption is
frequently violated in real-world networks, where conditions
like bandwidth are highly dynamic and non-stationary. An ABR
agent trained under one speciﬁc network trace may fail to
generalize to other ﬂuctuating network conditions, leading to
suboptimal performance.
To address this limitation, where the true dynamics of the
environment are unknown, we model the ABR problem as a
Bayes-Adaptive Markov Decision Process (BAMDP) [15].
In a standard MDP, the agent assumes the network follows
a ﬁxed rule. In contrast, a BAMDP agent acknowledges its
ignorance about the speciﬁc network scenario. It maintains a
belief state—a probabilistic “mental model” of the current net-
work environment. As the agent observes new state transitions,
it recursively updates this belief, allowing it to adapt its strategy
dynamically based on its conﬁdence in the environment’s state.
In this framework, the unknown network dynamics are treated
as a latent variable. The agent maintains a belief state, bt,
deﬁned as the posterior distribution over these possible network
environments given the interaction history τ:t.
The decision-making process in a BAMDP extends the stan-
dard MDP cycle by incorporating a belief update step. The
process proceeds as follows:
1) State Representation: At each timestep t, the agent’s state
is a hyper-state s+
t = (st, bt), consisting of the observable
physical state st and the current belief bt.
2) Action & Observation: The agent selects an action at. The
environment then transitions to a new physical state st+1
and emits a reward rt+1 based on the true (but unknown)
network dynamics.
3) Belief
Update:
Upon
observing
the
transition
(st, at, st+1, rt+1), the agent updates its belief from
bt to bt+1 using Bayes’ rule. This update incorporates
the new evidence into the agent’s understanding of the
environment.
4) Transition: The system moves to the next hyper-state
s+
t+1 = (st+1, bt+1).
Formally, the transition function in the hyper-state space
S+ = S × B decomposes into the physical transition and the
information state update:
P +(s+
t+1|s+
t , at, rt)
= P +(st+1, bt+1|st, at, rt, bt)
= Ebt[P(st+1|st, at)]



Physical Transition
· δ(bt+1 = Update(bt, st, at, st+1))



Belief Update
.
(8)
The reward function for the hyper-state depends solely on the
physical state transition, as the user’s QoE is derived from the
actual physical states. Thus, it is deﬁned as:
R+(s+
t , at, s+
t+1) = R(st, at, st+1),
(9)
where R(st, at, st+1) is the standard QoE reward deﬁned in (5).
This reformulation transforms the original MDP into a
BAMDP, denoted by M + = (S+, A, R+, P +, ρ+
0 , γ, H). Con-
sequently, our primary goal is to ﬁnd a policy π to maximize the
accumulated long-term reward in the BAMDP:
J+(π) = Eb0,ρ+
0 ,P +,π
H−1

t=0
γtR+(rt+1|s+
t , at, s+
t+1)
	
. (10)
The strategy that achieves this goal is termed a Bayes-optimal
policy. While this problem can theoretically be addressed via
methods like posterior sampling [43] or Bayesian planning [44],
these approaches typically incur prohibitive computational over-
head for real-time ABR decisions. Computing exact belief up-
dates is also generally infeasible in practice. Therefore, we
leverageameta-reinforcementlearningparadigmtotacklethis
issue, as detailed below.
C. Approximating Bayes-Optimal Policies Via Meta-Learning
The theoretical solution for BAMDP is computationally difﬁ-
cult.Ourapproach,EAStream,employsameta-learningstrategy
inspiredbyVariBAD[45]toacquireasolutionthatapproximates
this policy.
In the meta-learning framework, we model different network
environments as individual tasks, each deﬁned by a hidden
latent variable mi. This latent variable corresponds to the belief
in BAMDP. Since the latent variable is unknown, the agent
must infer information about mi from its historical information.
Speciﬁcally,weemployanencodertotransformthetrajectoryτ:t
into an inferred distribution qφ(m|τ:t) within the latent space.
This distribution serves as an inference of the environment’s
latent features.
The learning process uses the framework of Variational Au-
toencoder (VAE) [46]. We optimize the encoder network by
maximizing the Variational Lower Bound (ELBO):
ELBO = Eρ

Eqφ(m|τ:t)[log pθ(τ:H|m)]
−DKL(qφ(m|τ:t)||pθ(m))] .
(11)
Here, ρ denotes the trajectory distribution induced by the current
policy π and the initial state distribution ρ0. This equation
consists of two components.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 6

```text
HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES
1181
Fig. 2.
Overall Architecture of the EAStream Framework. The system comprises two main modules: a Belief Inference Module responsible for learning
environmental awareness, and a DRL Policy Module for adaptive decision-making.
The ﬁrst is the reconstruction likelihood. Crucially, the
decoder pθ is tasked with predicting the entire trajectory τ:H
based on the latent belief m. This forces m to capture the un-
derlying predictive dynamics of the network, rather than merely
compressing interaction history. Using the Markov property, this
likelihood decomposes into:
log pθ(τ:H|m) = log pθ(s0|m) +
H−1

t=0
[log pθ(st+1|st, at, m)
+ log pθ(rt+1|st, at, st+1, m)].
(12)
This factorization allows the model to iteratively predict the next
state and reward at each time step, enforcing a precise modeling
of the step-wise dynamics.
The second component is the KL divergence, which acts
as a regularizer. It constrains the learned posterior qφ to remain
close to the prior p(m) (typically a standard Gaussian), ensuring
a smooth latent space that facilitates stable policy optimization.
Based on the inferred belief, the DRL policy πψ is optimized
to approximate a Bayes-Optimal policy. At each timestep t, a
latent variable mt is sampled from the current belief distribution,
mt ∼qφ(m|τ:t). The policy then takes the current physical state
st and the latent variable as input, denoted as πψ(at|st, mt).
Consequently, the agent can adapt its decision-making process
in response to the estimated hidden dynamics.
The overall training objective is to optimize the combined
objective:
L(φ, θ, ψ) = Ep(M) [J(ψ, φ) + λ · ELBO(φ, θ)] ,
(13)
where Ep(M) denotes the expectation over the task distribution
p(M). In this equation, J(ψ, φ) denotes the expected return for
approximate policy, and the second term is the task inference
objective. The hyperparameter λ controls the trade-off between
maximizing the RL reward and the accuracy of belief recon-
struction.
Fig. 3.
Architecture of the Belief Inference Module.
IV. SYSTEM DESIGN
This section details the architecture and training methodol-
ogy of EAStream, our proposed meta-reinforcement learning
framework for adaptive bitrate streaming.
A. System Architecture Overview
The EAStream framework consists of two core modules: a be-
lief inference module responsible for environmental awareness,
and a policy module for decision-making. The overall EAStream
architecture is illustrated in Fig. 2 .
The belief inference module is designed based on the prin-
ciples of VAE. It comprises two modules: a recurrent Be-
lief Encoder and a predictive Decoder. The Belief Encoder
processes the agent’s historical interaction trajectory (τt =
(s0, a0, r1, . . . , st)) to infer a latent variable, m. This latent vari-
able m represents its probabilistic belief regarding the hidden
characteristics of the current network conditions. The Belief
Encoder reconstructs the entire trajectory from the belief m.
Predicting future trajectories enables belief m to capture the
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 7

```text
1182
IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026
Fig. 4.
Architecture of the DRL Policy Module.
potential dynamics of the network environment rather than
merely compressing past information.
The second part is the DRL strategy responsible for action
selection. The objective is to learn a near-optimal strategy
π(at|st, mt), which takes in the current state and belief and
outputs an action that maximizes the long-term cumulative
QoE reward. Unlike traditional DRL-based agents, our policy
network is conditional on state st and belief mt. This dual-
input structure is the key to achieving adaptability. The state
st provides the most recent state of the environment, while the
belief mt provides richer, history-based information about the
environment. This allows the policy to learn not just one ﬁxed
strategy, but a highly adaptive meta-policy.
B. State, Action, and Reward Deﬁnition
To train the DRL agent, this section explicitly deﬁnes the
reward function, as well as the state and action space.
▷State: For every time step t, the agent receives a state
st. This state is a multi-dimensional vector that includes in-
formation about the playback status and network conditions.
Following the design of Pensieve [8], we formulate the state st
as follows:
st = (⃗xt, ⃗τt, ⃗nt, bt, ct, lt).
(14)
Here, ⃗xt and ⃗τt are vectors representing the historical throughput
and transmission time of the past w video chunks(We set w = 8
following the standard conﬁguration in [8].); ⃗nt denotes the ﬁle
size for K available bitrates of next chunk; bt is the current buffer
occupancy; ct denotes the number of unplayed chunks; and lt
denotes the last chunk’s bitrate.
▷Action: In an ABR system, the agent’s task is to select the
video quality for the subsequent chunk. The action space A is
thus formulated as a discrete set:
A = {0, 1, . . . , K −1}.
(15)
Here, K represents the number of candidate bitrates. These
discrete options correspond to different video resolutions such
as 360p, 480p, 720p, and 1080p.
▷Reward: To optimize the QoE objective in (5), we deﬁne the
reward function rt accordingly. Once the t-th video chunk has
been successfully transmitted, the agent will receive a reward of
rt:
rt = μ1 · q(Rt) −μ2 · Tt −μ3 · |q(Rt) −q(Rt−1)|.
(16)
This reward function directly guides the behavior of the agent.
It enables agent to learn strategies for choosing high-quality
chunks while reducing rebuffering and bitrate changes. The
weighting coefﬁcients μ1, μ2, μ3 control the balance.
C. Neural Network Architectures
The proposed EAStream framework consists of two compo-
nents: the Belief Inference Module and the DRL Policy Module.
▷Belief Inference Module: As shown in Fig. 3, this module is
designed to infer the characteristics of the network conditions,
which contains a recurrent encoder and a predictive decoder.
The Encoder sequentially processes the interaction history. For
each time step t, tuple (at−1, rt, st) is ﬁrst passed through
their respective fully connected layers (FC), then merged into
a feature vector. This feature vector is then fed into a Gated
Recurrent Unit (GRU) to capture sequential patterns. The output
of GRU is subsequently passed through FC to generate the
parameters of a Gaussian distribution, representing the posterior
belief mt. The Decoder provides the training objective by using
two separate networks to reconstruct the system’s dynamics.
Speciﬁcally, consistent with the factorization of the trajectory
likelihood in (12), a State Transition Head predicts the next state
ˆst, while a Reward Head predicts the reward ˆrt. Both heads are
implemented as fully connected layers.
▷DRL Policy Module: As shown in Fig. 4, this module is the
agent’s core decision-making component and is implemented
withanActor-Criticarchitecture.ItbeginswithaFeatureExtrac-
tor that processes the raw state. Vector-based inputs, including
the throughput history ⃗xt, download time history ⃗τt, and the vec-
tor of next chunk sizes ⃗nt, are fed into one-dimensional convo-
lutional layers to capture temporal features. Concurrently, scalar
inputs, including the buffer occupancy bt, remaining chunks ct,
and the last selected bitrate lt, are processed by dedicated fully
connected layers. These features are then concatenated with the
latent belief mt. The resulting high-dimensional feature vector
serves as the input to two independent networks. The Actor
Network, a multi-layer network with a ﬁnal Softmax activation,
maps these features to a probability distribution corresponding
to the bitrates. In parallel, the Critic Network with a similar
architecture outputs a state value estimation V (st, mt) to guide
the learning of the actor.
D. Ofﬂine Training and Online Adaptation
This section details the learning and adaptation workﬂow of
EAStream. The process consists of two stages summarized in
Algorithm 1 and Algorithm 2 respectively.
▷Ofﬂine Meta-Training: This stage aims to learn a meta-
policy capable of inferring environmental characteristics and
adapting decisions across diverse network conditions. By ex-
posing the agent to a wide variety of environments at this stage,
we force it to learn how to identify potential network conditions
rather than memorizing speciﬁc training trajectories. Further-
more, EAStream adopts a separated optimization strategy. This
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 8

```text
HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES
1183
Algorithm 1: Ofﬂine Meta-Training.
1: Initialize belief params φ, θ; policy params ψ; entropy
weight α; target entropy Htarget;
2: Initialize replay buffer Dbelief; loss weights λs, λr, β.
3: for each training iteration do
4:
Collect a batch of recent trajectories {τi}.
5:
Store trajectories {τi} in Dbelief.
6:
//Update Policy Module
7:
Compute belief mt for {τi} using ﬁxed encoder qφ.
8:
Update ψ by minimizing PPO loss:
L(ψ) = ˆEt[−LCLIP(ψ) + LVF(ψ) −αH[πψ](st, mt)]
9:
Compute average entropy ¯H = ˆEt[H[πψ(·|st, mt)]]
10:
Update entropy weight α ←α −( ¯H −Htarget)
11:
//Update Belief Module
12:
Sample a batch of trajectories {τj} ∼Dbelief.
13:
For each τj, infer latent belief mj ∼qφ(m|τj).
14:
// Calculate weighted loss
components
15:
Lstate = −Ej,t[log pθ(sj,t+1|sj,t, aj,t, mj)].
16:
Lreward = −Ej,t[log pθ(rj,t+1| . . . , mj)].
17:
LKL = Ej[DKL(qφ(m|τj)||p(m))].
18:
LELBO = λsLstate + λrLreward + βLKL
19:
Update φ, θ by minimizing LELBO.
20: end for
separation prevents the belief learning from being biased by the
policy’s early exploration.
In each training iteration, multiple parallel agents collect
interaction trajectories. The collected data is used to update the
policy and belief modules separately.
The policy network is updated using the Proximal Policy
Optimization (PPO) algorithm [47]. While off-policy algorithms
like SAC are known for high sample efﬁciency, we explicitly
select the on-policy PPO to ensure training stability in our
meta-learning framework. Since the Belief Encoder evolves
continuously, data stored in an off-policy replay buffer would
contain obsolete belief representations. PPO avoids this issue
by strictly learning from fresh trajectories consistent with the
current encoder.
We utilize the clipped surrogate objective to prevent destruc-
tive large updates:
LCLIP(ψ) = ˆEt

min

rt(ψ) ˆAt,
clip(rt(ψ), 1 −ϵ, 1 + ϵ) ˆAt

,
(17)
where rt(ψ) is the probability ratio, ϵ is a hyperparameter used to
limit the variation of the probability ratio and ˆAt is the advantage
estimate. To encourage exploration, we incorporate an automatic
entropy adjustment mechanism. The ﬁnal policy loss combines
the clipped loss, the value function loss LVF, and the entropy
bonus:
L(ψ) = ˆEt

−LCLIP(ψ) + LVF(ψ) −αH[πψ](st, mt)

.
(18)
Algorithm 2: Online Adaptation.
1: Load qφ and policy πψ.
2: Initialize recurrent hidden state h0.
3: for t = 1, 2, . . . , N do
4:
// Belief Inference
5:
Update ht ←RNNφ(ht−1, (at−1, rt, st)).
6:
Sample belief from encoder mt ∼qφ(ht).
7:
// Policy Decision
8:
Observe current state st.
9:
Select action at ∼πψ(at|st, mt).
10:
// Environment Interaction
11:
Execute at, observe st+1, rt+1.
12: end for
Crucially, gradients from the policy update are not backprop-
agated to the belief module. The encoder and decoder (φ, θ) are
updated independently by sampling trajectories from a separate
replay buffer. The objective is to minimize the ELBO loss
derived in (11), which aggregates the state reconstruction loss,
reward prediction loss, and the KL divergence regularization
term.
▷Online Adaptation: When deployed to the client, the model
willadaptonlineinthenewnetworkenvironment.Whenrunning
online, there is no need for real-time gradient updates or training.
The adaptability of policy is achieved entirely through real-time
inference.
Initially, the latest interaction tuple (at−1, rt, st) is fed into the
Belief Encoder qφ to update the recurrent hidden state ht. Given
this hidden state, the encoder performs forward passing to infer
the belief mt. This belief represents the agent’s perception of the
current network environment. Then the belief mt and the current
state st are jointly input into the policy network πψ to decide the
next chunk’s bitrate at. Finally, the agent performs the action
and observes the new state and reward. During the entire online
phase, the auxiliary decoder module is deprecated, and the agent
operated in pure inference mode. Unlike the optimization-based
meta-learning methods that require gradient updates during
testing, our method relies solely on forward propagation. This
structural design reduces computational overhead and makes it
more suitable for resource-constrained client deployments.
V. EVALUATION
A. Experimental Setup
▷Implementation: We implement EAStream in PyTorch and
optimize the model parameters using the Adam optimizer. For
the policy and value network, the learning rate is set to 1 × 10−4.
The PPO algorithm is conﬁgured with a clipping parameter
of ϵ = 0.2, a reward discount factor of γ = 0.99 and a target
entropy of Htarget = 0.1. For belief inference module (φ, θ), the
learning rate is 1 × 10−3, and it is trained using a replay buffer
with a capacity of 1000 trajectories and a batch size of 32. The
weights for its loss function are set to λs = 1.0, λr = 1.0, and
β = 0.1, respectively. The dimension of the latent belief m is
set to 16. The selection of β and m is further justiﬁed through
sensitivity analysis in Section V-C.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 9

```text
1184
IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026
▷Video Parameters: The video content selected for our
experiments is the “EnvivioDash3” test sequence [48]. It has a
total duration of 193 seconds and is segmented into 48 chunks,
each with a playback time of approximately 4 seconds. Each
chunk is pre-encoded into six different bitrate levels to facilitate
adaptive streaming: 300, 750, 1200, 1850, 2850, and 4300 kbps.
▷Baseline Algorithms: We select several state-of-the-art
ABR algorithms that represent different design paradigms for
comparison:
r BOLA [16]: A buffer-based algorithm based on Lyapunov
optimization. This algorithm ensures that the video quality
is maximized while guaranteeing the stability of the buffer.
r FESTIVE [5]: A rate-based heuristic algorithm. This al-
gorithm uses the harmonic average of the nearest chunks
download rates for throughput estimation.
r RobustMPC [7]: An algorithm based on the theory of
MPC. This algorithm predicts the future optimal sequence
by combining throughput estimation and buffer informa-
tion.
r Pensieve [8]: A state-of-the-art ABR algorithm leveraging
deep reinforcement learning.
r NetLLM [33]: The ﬁrst framework using LLMs for net-
working tasks through ﬁne-tuning to enhance generaliza-
tion and performance.
r Comyco [9]: A quality-aware ABR method based on im-
itation learning. It trains the neural network by imitating
the expert actions.
▷Network Traces: To rigorously evaluate algorithm perfor-
mance, we utilize network traces collected from a variety of
real-world communication datasets.
r 3G [49]: This dataset comprises throughput measurements
from 3G mobile networks, collected on public transporta-
tion routes in Oslo, Norway.
r FCC [50]: Sourced from broadband network traces re-
leased by the U.S. Federal Communications Commission
(FCC), these traces are selected from the “Web browsing”
category and are characterized by moderate bandwidth
conditions.
r 4GSyd [51]: This dataset contains traces gathered from
4 G vehicular networks under driving conditions in Sydney,
Australia.
r Oboe [52]: This dataset contains traces from a commer-
cial on-demand music video service, capturing sessions
from a mix of users on both wired desktop and mobile
(WiFi/cellular) connections.
r 4GNY [53]: Collected on New York City’s public transit
system (bus and subway), these traces represent highly
variable urban mobile network conditions.
We provide an overview of the primary characteristics for
these datasets in Table I.
For training our learning-based models (EAStream and Pen-
sieve), we create a single, uniﬁed dataset to foster generalization.
We combine the traces from the 3G, FCC, and 4GSyd sources
to form a Hybrid dataset. From this Hybrid dataset, 80% of the
traces are randomly sampled to constitute the training set.
The remaining 20% of the Hybrid dataset is held out as
the in-distribution test set, used to evaluate performance
TABLE I
CHARACTERISTICS OF NETWORK TRACE DATASETS
TABLE II
PARAMETERS FOR DIFFERENT QOE METRICS
Fig. 5.
Normalized average QoE comparison on the in-distribution Hybrid
test set (3G, FCC, 4GSyd).
on network conditions similar to those seen during train-
ing. The 4GNY and Oboe datasets are kept entirely separate
from the training process. They serve exclusively as out-of-
distribution test sets to rigorously assess the generalization ca-
pabilities of the pre-trained models in completely novel network
environments.
▷QoE Metrics: To evaluate the algorithm performance based
on different user preferences, we adopted two distinct QoE
targets from Pensieve [8]. For learning-based algorithms (Pen-
sieve, Comyco, NetLLM and EAStream), we train a dedicated
model for each QoE objective. The speciﬁc deﬁnition is as
follows:
r QoElin This metric considers that the video quality in-
creases linearly with the bitrate.
r QoElog This metric considers a higher bitrate to have
diminishing returns to perceptual quality.
Table II provides a summary of the parameters used for each
QoE metric.
B. EAStream Vs. Existing ABR Algorithms
In this section, we compare EAStream with the baseline
algorithms. The test dataset includes in-distribution (Hybrid)
and out-of-distribution (Oboe, 4GNY). We use bar charts to
present the normalized average QoE scores in Figs. 5 and 6.
We analyzed the performance distribution using CDF plots in
Figs. 7, 8, and 9.
▷Performance on the Hybrid Test Set: We ﬁrst evaluate the
performance of all algorithms on the in-distribution test set,
which is composed of traces from the 3G, FCC, and 4GSyd
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 10

```text
HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES
1185
Fig. 6.
Normalized average QoE comparison on the out-of-distribution test
sets (Oboe, 4GNY).
datasets. Fig. 5 illustrates the normalized average QoE scores
for both QoElin and QoElog metrics.
As shown in Fig. 5, our proposed EAStream consistently
achieves the highest, or joint-highest, average QoE across all
three network conditions for both QoElin and QoElog metrics.
This demonstrates that EAStream can learn a highly effective
and stable policy even when trained on a diverse hybrid dataset.
This is a notable advantage, as prior work [14] has shown
that baseline DRL agents like Pensieve can suffer performance
degradation when trained on mixed network conditions rather
than a single environment.
For instance, in the low-bandwidth 3G and FCC dataset,
EAStream outperforms the standard DRL method Pensieve
and the recent LLM-based algorithm NetLLM. In the high-
bandwidth 4GSyd scenario, EAStream achieves comparable
performance to the strong baseline Comyco. This balanced suc-
cess contrasts with Pensieve, which performs notably weaker in
the low-bandwidth traces. This gap suggests Pensieve may have
over-specialized on the high-bandwidth traces within the hybrid
dataset, whereas EAStream learns a more effective strategy that
masters the full training distribution.
The CDF plots in Fig. 7 and Fig. 8 provide a more detailed
view of the performance distribution. In all subplots, EAStream
is consistently positioned to the right of all other algorithms. This
suggests that EAStream not only achieves a higher average QoE
but also provides a more stable experience for the vast majority
of users, minimizing the poor experience sessions.
▷Generalization to Unseen Network Environments. To
evaluate the aspect of generalization, we now assess the per-
formance on two unseen (out-of-distribution, OOD) test sets:
Oboe and 4GNY. These network traces were not exposed to any
learning-based models during the training phase.
Fig. 6 illustrates the normalized average QoE scores for both
QoE metrics on these two unseen datasets. The results clearly
demonstrate the superior generalization capability of EAStream.
In all four scenarios, EAStream achieved the highest or nearly
the highest average QoE. Speciﬁcally, its performance on the
Oboe dataset outperforms all other algorithms, including the
strong baseline Comyco. It also achieves top-tier performance
on the 4GNY dataset, comparable to Comyco and signiﬁcantly
better than Pensieve and NetLLM.
In all four CDF subplots in Fig. 9, EAStream has excel-
lent performance compared with other baseline algorithms. A
key ﬁnding is the performance of Pensieve. Pensieve demon-
strated decent performance on the 4GSyd dataset, but it dropped
signiﬁcantly on the 4GNY dataset. This might be due to the
highly unstable 4GNY trajectory (as shown in Table I), which
suggests poor generalization of Pensieve. In contrast, EAStream
maintains stable performance in both in-distribution and out-of-
distribution tests. This generalization performance demonstrates
the effectiveness of our meta-learning framework in learning to
rapidly adapt to network uncertainty.
C. Effectiveness Analysis
▷Case Study: We synthesized a challenging trajectory by
concatenating 4GSyd and 3G segments to evaluate EAStream’s
adaptability under abrupt non-stationary changes (e.g., a sharp
bandwidth drop at 5 s).
As shown in Fig. 10, EAStream achieved the highest QoE
(1.40), outperforming Pensieve (1.21) and RobustMPC (1.07).
While the sudden transition caused initial rebuffering for all
algorithms due to high-bitrate inertia, EAStream recovered
most effectively. It rapidly detected the deterioration, down-
shifting to 300 kbps to stabilize playback before smoothly tran-
sitioning upward as buffers replenished. Conversely, Pensieve
and RobustMPC struggled with persistent rebuffering and fre-
quent switching. This conﬁrms that EAStream’s environment-
awareness mechanism facilitates superior long-term decision-
making in dynamic networks.
▷Analysis of Latent Belief Space: We evaluated whether
EAStream’s belief module learns meaningful environmental
representations using t-SNE [54] visualization. Average 16-
dimensional belief vectors were collected from the QoElin model
across three distinct datasets: 3G (low bandwidth), 4GSyd (stable
high bandwidth), and 4GNY (unstable high bandwidth).
As shown in Fig. 11, the belief vectors form three distinct
clusters corresponding to each environment. This separation
demonstrates that the module effectively captures both coarse-
grained bandwidth levels and ﬁne-grained volatility differences
between the two 4 G networks. These results validate that latent
beliefs encode critical environmental dynamics, providing the
necessary awareness for optimal adaptive decisions.
▷Ablation and Sensitivity Analysis: We conduct ablation and
sensitivity studies to evaluate the impact of the belief represen-
tation by varying the latent dimension and the KL coefﬁcient
using the 3G dataset. Speciﬁcally, a dimension of 0 represents
the baseline model where the belief module is entirely removed.
As shown in Fig. 12(a), the agent achieves the best performance
with a dimension of 16, outperforming the baseline model
without the Belief module. This proves the effectiveness of the
Belief module. Meanwhile, when the dimension is too small, the
latent vector lacks the capacity to sufﬁciently encode complex
network dynamics. Conversely, a dimension larger than 16 leads
to performance degradation, likely due to increased optimization
difﬁculty.
Similarly, we test the sensitivity to the KL coefﬁcient β, as
shown in Fig. 12(b). A small β makes the latent space irregular
and hurts performance. If β is too large, the belief becomes
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 11

```text
1186
IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026
Fig. 7.
CDF of QoElin scores on the in-distribution Hybrid test set (3G, FCC, 4GSyd).
Fig. 8.
CDF of QoElog scores on the in-distribution Hybrid test set (3G, FCC, 4GSyd).
Fig. 9.
CDF of QoE scores on the out-of-distribution test sets (Oboe and 4GNy).
Fig. 10.
Bitrate selection of EAStream, Pensieve, and RobustMPC on the
bandwidth drop trace.
uninformative due to over-regularization, known as posterior
collapse. The results conﬁrm that a moderate latent dimension
and KL coefﬁcient provide the best balance for the latent belief
representation.
Fig. 11.
t-SNE visualization of the latent belief vectors collected from three
distinct network datasets.
▷Overhead Analysis: To test the overhead of EAStream, we
conducted a quantitative analysis of its computational overhead
and memory usage. We compared EAStream with Pensieve,
RobustMPC and NetLLM. The experiments were carried out
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 12

```text
HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES
1187
Fig. 12.
Ablation studies on the latent belief representation.
TABLE III
RESOURCE CONSUMPTION AND INFERENCE LATENCY COMPARISON
on a server equipped with an Intel i9-13900 K CPU and were
run in a single-threaded mode.
As shown in Table III, the overhead of introducing the Be-
lief module is extremely small (0.0224 MFLOPs). Although
it is slightly higher than Pensieve, the total inference latency
of EAStream is only 0.2258 milliseconds. For a video chunk
duration of 4 seconds, our algorithm accounts for only 0.0056%
of it. EAStream’s speed is signiﬁcantly faster than the widely
used RobustMPC (3.1315 milliseconds), and much faster than
NetLLM. This conﬁrms that EAStream is suitable for resource-
constrained client deployments.
D. Discussion and Limitations
Despite the demonstrated advantages, we acknowledge cer-
tain limitations of the EAStream framework. First, the ofﬂine
meta-training process incurs higher computational overhead
compared to standard DRL methods due to the joint optimization
of the belief inference and policy modules. However, this cost
is strictly conﬁned to the ofﬂine phase and does not impact
the low-latency requirements of online inference. Second, the
algorithm’s generalization capability is inherently dependent on
the diversity of the network traces used during meta-training;
a narrow task distribution may limit the effective range of
adaptation. Finally, in extreme outlier scenarios that deviate
signiﬁcantly from the training distribution, the inferred belief
may become inaccurate. As noted in Section VI, leveraging the
reconstruction error for anomaly detection offers a promising
avenue to mitigate this issue in future work.
VI. CONCLUSION
This paper presents EAStream, a context-based meta-
reinforcement learning framework designed to address the gen-
eralization challenge in adaptive bitrate streaming. By modeling
theproblemasaBAMDPandutilizingavariationalautoencoder,
EAStream infers latent beliefs about network dynamics from
interactionhistory.Thismechanismenablesthepolicytoachieve
zero-shot adaptation to unseen network conditions without re-
quiring computationally expensive online ﬁne-tuning. Extensive
experiments on real-world datasets demonstrate that EAStream
not only matches state-of-the-art performance on in-distribution
traces but signiﬁcantly outperforms existing baselines in out-of-
distribution scenarios. In future work, we intend to explore the
online utilization of the Belief Decoder, which is currently only
reserved for ofﬂine training. Speciﬁcally, we plan to leverage the
real-time reconstruction errors for anomaly detection to identify
extreme network outliers.
REFERENCES
[1]
Sandvine, “2024 Global internet phenomena report,” 2024. [Online].
Available:
https://www.applogicnetworks.com/global-internet-phenom
ena-report-2024
[2] G. V. Research, “Video streaming market size to reach 416.84 billion by
2030,” 2024. [Online]. Available: https://www.grandviewresearch.com/
press-release/global-video-streaming-market
[3] T. Stockhammer, “Dynamic adaptive streaming over HTTP– Standards
and design principles,” in Proc. 2nd Annu. ACM Conf. Multimedia Syst.,
2011, pp. 133–144.
[4] R. Pantos and W. May, “HTTP live streaming,” RFC 8216, Aug. 2017.
[Online]. Available: https://www.rfc-editor.org/info/rfc8216
[5] J. Jiang, V. Sekar, and H. Zhang, “Improving fairness, efﬁciency, and
stability in HTTP-based adaptive video streaming with festive,” in Proc.
8th Int. Conf. Emerg. Netw. Experiments Technol., 2012, pp. 97–108.
[6] T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Watson,
“A buffer-based approach to rate adaptation: Evidence from a large
video streaming service,” in Proc. 2014 ACM Conf. SIGCOMM, 2014,
pp. 187–198.
[7] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic approach
for dynamic adaptive video streaming over HTTP,” in Proc. 2015 ACM
Conf. Special Int. Group Data Commun., 2015, pp. 325–338.
[8] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video streaming
with pensieve,” in Proc. Conf. ACM Special Int. Group Data Commun.,
2017, pp. 197–210.
[9] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, “COMYCO:
Quality-aware adaptive video streaming via imitation learning,” in Proc.
27th ACM Int. Conf. Multimedia, 2019, pp. 429–437.
[10] F. Y. Yan et al., “Learning in situ: A randomized experiment in video
streaming,” in Proc. 17th USENIX Symp. Netw. Syst. Des. Implementation,
2020, pp. 495–511.
[11] H. Zhang et al., “LOKI: Improving long tail performance of learning-based
real-time video adaptation by fusing rule-based models,” in Proc. 27th
Annu. Int. Conf. Mobile Comput. Netw., 2021, pp. 775–788.
[12] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, and L. Sun, “Learning tai-
lored adaptive bitrate algorithms to heterogeneous network conditions: A
domain-speciﬁc priors and meta-reinforcement learning approach,” IEEE
J. Sel. Areas Commun., vol. 40, no. 8, pp. 2485–2503, Aug. 2022.
[13] S. Wang, J. Lin, and Y. Dai, “MMVS: Enabling robust adaptive video
streaming for wildly ﬂuctuating and heterogeneous networks,” IEEE
Trans. Multimedia, vol. 26, pp. 11018–11030, 2024.
[14] W. Li, X. Li, Y. Xu, Y. Yang, and S. Lu, “MetaABR: A meta-learning
approach on adaptative bitrate selection for video streaming,” IEEE Trans.
Mobile Comput., vol. 23, no. 3, pp. 2422–2437, Mar. 2024.
[15] M. O. Duff, “Optimal Learning: Computational procedures for Bayes-
adaptive Markov decision processes,” Univ. Massachusetts Amherst,
Amherst, MA, USA, 2002.
[16] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal
bitrate adaptation for online videos,” IEEE/ACM Trans. Netw., vol. 28,
no. 4, pp. 1698–1711, Aug. 2020.
[17] J. Chen, Y. Yu, L. Wang, Y. Chen, T. Huang, and L. Sun, “En-
hanced bandwidth measurement and robust rate adaptation for low-
latency live streaming,” in Proc. IEEE Conf. Comput. Commun., 2025,
pp. 1–10.
[18] Y. Qin et al., “A control theoretic approach to ABR video streaming: A
fresh look at PID-based rate adaptation,” IEEE Trans. Mobile Comput.,
vol. 19, no. 11, pp. 2505–2519, Nov. 2020.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 13

```text
1188
IEEE TRANSACTIONS ON SERVICES COMPUTING, VOL. 19, NO. 2, MARCH/APRIL 2026
[19] T. Huang, X. Yao, C. Wu, R.-X. Zhang, Z. Pang, and L. Sun, “Tiyuntsong:
A self-play reinforcement learning approach for abr video streaming,” in
Proc. 2019 IEEE Int. Conf. Multimedia Expo., 2019, pp. 1678–1683.
[20] P. K. Mu, J. Zheng, T. H. Luan, L. Zhu, M. Dong, and Z. Su, “AMIS: Edge
computing based adaptive mobile video streaming,” in Proc. IEEE Conf.
Comput. Commun., 2021, pp. 1–10.
[21] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, and L. Sun, “Buffer awareness
neural adaptive video streaming for avoiding extra buffer consumption,”
in Proc. IEEE Conf. Comput. Commun., 2023, pp. 1–10.
[22] B. O. Turkkan et al., “GreenABR : Generalized energy-aware adaptive
bitrate streaming,” ACM Trans. Multimedia Comput., Commun. Appl.,
vol. 20, no. 9, pp. 1–24, 2024.
[23] H. Su, S. Wang, S. Yang, T. Huang, and X. Ren, “Reducing trafﬁc wastage
in video streaming via bandwidth-efﬁcient bitrate adaptation,”IEEE Trans.
Mobile Comput., vol. 23, no. 11, pp. 10361–10377, Nov. 2024.
[24] Y. Guo, F. R. Yu, J. An, K. Yang, C. Yu, and V. C. Leung, “Adaptive
bitrate streaming in wireless networks with transcoding at network edge
using deep reinforcement learning,” IEEE Trans. Veh. Technol., vol. 69,
no. 4, pp. 3879–3892, Apr. 2020.
[25] X. Ma et al., “QAVA: QoE-Aware adaptive video bitrate aggregation
for HTTP live streaming based on smart edge computing,” IEEE Trans.
Broadcast., vol. 68, no. 3, pp. 661–676, Sep. 2022.
[26] W. Li et al., “Optimizing video streaming in dynamic networks: An
intelligent adaptive bitrate solution considering scene intricacy and data
budget,” IEEE Trans. Mobile Comput., vol. 23, no. 12, pp. 12280–12297,
Dec. 2024.
[27] Y. Zhao, Q.-W. Shen, W. Li, T. Xu, W.-H. Niu, and S.-R. Xu, “Latency
aware adaptive video streaming using ensemble deep reinforcement learn-
ing,” in Proc. 27th ACM Int. Conf. Multimedia, 2019, pp. 2647–2651.
[28] G. Xiao, M. Wu, Q. Shi, Z. Zhou, and X. Chen, “DeepVR: Deep reinforce-
ment learning for predictive panoramic video streaming,” IEEE Trans.
Cogn. Commun. Netw., vol. 5, no. 4, pp. 1167–1177, Dec. 2019.
[29] L. Yang, G. Liu, S. Li, J. Zhao, and T. Jiang, “Environment information
enhanced neural adaptive bitrate video streaming for intercity railway,”
IEEE Trans. Broadcast., vol. 71, no. 3, pp. 849–861, Sep. 2025.
[30] E. R. Peretto, M. N. R. Soares Filho, D. C. S. Sousa, L. P. Gaspary, and B.
I. Grisci, “Towards an ML assisted dash-based architecture: Leveraging
predictive network analyses with interpretability,” in Proc. 21st Int. Conf.
Netw. Serv. Manage., 2025, pp. 1–7.
[31] L. Jia et al., “Beyond interpretability: Exploring the comprehensibility of
adaptive video streaming through large language models,” in Proc. 33rd
ACM Int. Conf. Multimedia, 2025, pp. 12035–120 44.
[32] M. Chen et al., “NeuroBA: Neuro-symbolic bitrate adaptation for irs-aided
mobilevideostreaming,”IEEETrans.Netw.,vol.34,pp.2558–2572,2026.
[33] D. Wu et al., “NetLLM: Adapting large language models for networking,”
in Proc. ACM SIGCOMM 2024 Conf., 2024, pp. 661–678.
[34] T. Hospedales, A. Antoniou, P. Micaelli, and A. Storkey, “Meta-learning
in neural networks: A survey,” IEEE Trans. Pattern Anal. Mach. Intell.,
vol. 44, no. 9, pp. 5149–5169, Sep. 2022.
[35] J. Beck et al., “A tutorial on meta-reinforcement learning,” Found. Trends
Mach. Learn., vol. 18, no. 2/3, pp. 224–384, 2025.
[36] C. Finn, P. Abbeel, and S. Levine, “Model-agnostic meta-learning for fast
adaptation of deep networks,” in Proc. Int. Conf. Mach. Learn., 2017,
pp. 1126–1135.
[37] A. Nichol, J. Achiam, and J. Schulman, “On ﬁrst-order meta-learning
algorithms,” 2018, arXiv:1803.02999.
[38] A. Nichol and J. Schulman, “Reptile: A scalable metalearning algorithm,”
2018, arXiv:1803.02999.
[39] A. A. Rusu et al., “Meta-learning with latent embedding optimization,” in
Proc. Int. Conf. Learn. Representations (ICLR), 2018, pp. 1–13.
[40] Y. Duan, J. Schulman, X. Chen, P. L. Bartlett, I. Sutskever, and P. Abbeel,
“Rl2: Fast reinforcement learning via slow reinforcement learning,” 2016,
arXiv:1611.02779.
[41] K. Rakelly, A. Zhou, C. Finn, S. Levine, and D. Quillen, “Efﬁcient off-
policy meta-reinforcement learning via probabilistic context variables,” in
Proc. Int. Conf. Mach. Learn., 2019, pp. 5331–5340.
[42] A.-M. K. Pathan et al., “A taxonomy and survey of content delivery
networks,” Grid Comput. Distrib. Syst. Lab., Univ. Melbourne, Parkville,
VIC, Australia, Tech. Rep., vol. 4, no. 2007, p. 70, 2007.
[43] M. Strens, “A Bayesian framework for reinforcement learning,” in Proc.
Int. Conf. Mach. Learn., 2000, pp. 943–950.
[44] A. Guez, D. Silver, and P. Dayan, “Efﬁcient Bayes-adaptive reinforcement
learning using sample-based search,” in Proc. Adv. Neural Inf. Process.
Syst., vol. 25, 2012, pp. 1–9.
[45] L. Zintgraf et al., “Varibad: A very good method for Bayes-adaptive deep
RL via meta-learning,” in Proc. Int. Conf. Learn. Representations (ICLR),
2019, pp. 1–14.
[46] D. P. Kingma and M. Welling, “Auto-encoding variational Bayes,” 2013,
arXiv:1312.6114.
[47] J.Schulman,F.Wolski,P.Dhariwal,A.Radford,andO.Klimov,“Proximal
policy optimization algorithms,” 2017, arXiv:1707.06347.
[48] “EnvivioDash3,” 2016. [Online]. Available: https://dash.akamaized.net/
envivio/EnvivioDash3/
[49] H. Riiser, P. Vigmostad, C. Griwodz, and P. Halvorsen, “Commute path
bandwidth traces from 3G networks: Analysis and applications,” in Proc.
4th ACM Multimedia Syst. Conf., 2013, pp. 114–118.
[50]
Federal Communications Commission, “Raw data - measuring broadband
America 2016,” Dec. 2016. Accessed: Oct. 16, 2025. [Online]. Available:
https://www.fcc.gov/reports-research/reports/measuring-broadband-
america/raw-data-measuring-broadband-america-2016
[51] A. Bokani, M. Hassan, S. S. Kanhere, J. Yao, and G. Zhong, “Comprehen-
sive mobile bandwidth traces from vehicular networks,” in Proc. 7th Int.
Conf. Multimedia Syst., 2016, pp. 1–6.
[52] Z. Akhtar et al., “OBOE: Auto-tuning video ABR algorithms to network
conditions,” in Proc. 2018 Conf. ACM Special Int. Group Data Commun.,
2018, pp. 44–58.
[53] L. Mei et al., “Realtime mobile bandwidth prediction using LSTM neu-
ral network and Bayesian fusion,” Comput. Netw., vol. 182, 2020, Art.
no. 107515.
[54] L. v. d. Maaten and G. Hinton, “Visualizing data using T-SNE,” J. Mach.
Learn. Res., vol. 9, Nov., pp. 2579–2605, 2008.
Zeming Huang received the BS degree in informa-
tion and computing science from the Nanjing Uni-
versity of Posts and Telecommunications, Nanjing,
China, in 2023. He is currently working toward the
MS degree in electronic information (computer tech-
nology) with the School of Computer, Electronics
and Information, Guangxi University, Nanning. His
research interests include adaptive video streaming,
deep reinforcement learning, and meta-learning.
Wenjing Xiao received the bachelor-straight-to-
doctoratedegreefromEmbeddedandPervasiveCom-
puting Lab, School of Computer Science and Tech-
nology, Huazhong University of Science and Tech-
nology, Wuhan, China. She is currently an assistant
professor with the School of Computer and Elec-
tronic Information, Guangxi University, China. Her
research interests include cloud computing, Internet
of Things, and cognitive computing.
Miaojiang Chen (Member, IEEE) received the PhD
degree in computer science from Central South Uni-
versity, in 2023. He is currently an associate pro-
fessor with the School of Computer and Electronic
Information, Guangxi University, China. He has au-
thored or coauthored several journal and conference
papers in the IEEE Journal on Selected Areas in
Communications, IEEE Transactions on Network-
ing, IEEE Transactions on Mobile Computing, IEEE
Transactions on Services computing, AAAI, IEEE
Transactions on Intelligent Transportation Systems,
IEEE Transactions on Network Science and Engineering, IEEE Transactions
on Emerging Topics in Computational Intelligence, IEEE Transactions on
Consumer Electronics, Knowledge-Based Systems, ACM Transactions on Au-
tonomous and Adaptive Systems, and ACM Transactions on Multimedia Com-
puting Communications and Applications. His research interests include deep
reinforcement learning, Internet of Things, edge computing, transfer learning,
and optimization. He is also reviewer of the top-tier conferences and journals,
including ICML, IEEE Transactions on Parallel and Distributed Systems, IEEE
Transactions on Information Forensics and Security, IEEE Transactions on In-
dustrial Informatics, IEEE Transactions on Intelligent Transportation Systems,
IEEE Internet of things journal. He was the recipient of the IEEE HITC 2025
Award for Excellence in Hyper-Intelligence (Early Career Researchers), and
Young Talents of the Guangxi High-Level Personnel Special Support Program.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.
```


### Pagina 14

```text
HUANG et al.: EASTREAM: AN ENVIRONMENT-AWARE ADAPTIVE BITRATE ALGORITHM FOR RELIABLE VIDEO STREAMING SERVICES
1189
Zhiquan Liu received the BS degree from the School
of Science, Xidian University, Xi’an, China, in 2012,
and the PhD degree from the School of Computer Sci-
ence and Technology, Xidian University, in 2017. He
is currently a full professor with the College of Cyber
Security, Jinan University, Guangzhou, China. His
research interests include security, trust, and privacy
in vehicular networks. He is also an associate editors
for IEEE Transactions on Information Forensics and
Security, IEEE Transactions on Industrial Informat-
ics, IEEE Internet of Things Journal, IEEE Network,
and Computer Networks, and the editor-in-chief of Advances in Transportation
and Logistics.
Min Chen (Fellow, IEEE) is currently a full pro-
fessor with the School of Computer Science and
Engineering, South China University of Technology,
Guangzhou, China. He was an assistant professor
with the School of Computer Science and Engineer-
ing, Seoul National University, Seoul, South Korea.
He is also the director with Embedded and Perva-
sive Computing Laboratory, Huazhong University of
Science and Technology, Wuhan, China. He is the
founding chair of IEEE Computer Society Special
Technical Communities on Big Data, and was the
chair of IEEE Globecom in 2022 eHealth Symposium. His Google Scholar
citations reached more than 40,500 with an H-index of 95. His top paper was
cited more than 4,100 times. From 2018 to 2022, he was selected as highly cited
researcher. He was the recipient of the IEEE Communications Society Fred
W.Ellersick Prize in 2017, IEEE Jack Neubauer Memorial Award in 2019, and
IEEE ComSoc APB Oustanding Paper Award in 2022.
Athanasios V. Vasilakos (Senior Member, IEEE)
is currently with the Center for AI Research, UiA,
and also with the European Academy of Sciences
and Arts(elected recently Dean of the Class VI). He
was or is as the editor for many technical journals,
such as IEEE Transactions on AI, IEEE Transac-
tions on Network and Service Management, IEEE
Transactions on Cloud Computing, IEEE Transac-
tions on Information Forensics and Security, IEEE
Transactions on Cybernetics, IEEE Transactions on
Nanobioscience, IEEE Transactions on Information
Technology in Biomedicine, ACM Transactions on Autonomous and Adaptive
Systems, IEEE Journal on Selected Areas in Communications. He is also the
WoS highly cited researcher.
Ahmed Farouk is currently an associate professor
with the Faculty of Computers and Artiﬁcial In-
telligence, Hurghada University, Egypt. He is also
an early career scientist demonstrating excellence
in quantum communication, cryptography, machine
learning, and cybersecurity research. He has authored
or coauthored more than 100 research papers with
high impact. He was the recipient of the the Egyptian
State Encouragement Award in advanced technolog-
ical sciences, the University Encouragement Award
in Basic Sciences and Engineering, Prof. Dr. Tarek
Kamel Award in Communications and Information Technology, and many more.
He has also been selected as one of 17 researchers from Africa to participate in
the prestigious Lindau Nobel Laureate Meetings, chosen by the U.S. National
Academy of Sciences to participate in the 2nd and 3rd U.S.-Africa Frontiers of
Science, Engineering, and Medicine symposium and his work been recognized
as one of Stanford’s World Top 2% scientists. He was also the recipient of the
travel and entire grants from the IEEE Computer Society, Lindau Foundation,
Baden-Württemberg International, U.S. National Academy of Sciences and
Okinawa Institute of Science and Technology. He has also chaired the IEEE
Computer Society Chapter and was elected as an ofﬁcer for the Consumer
Technology Society (CTSoc) on Quantum Consumer Technology Technical
Committee (QCT).
Houbing Herbert Song (Fellow, IEEE) received
the PhD degree in electrical engineering from the
University of Virginia, Charlottesville, VA, USA, in
2012. He is currently a tenured associate professor,
the director with the NSF Center for Aviation Big
DataAnalytics(Planning),andassociatedirectorwith
Leadership of the DoT Transportation Cybersecu-
rity Center for Advanced Research and Education,
University of Maryland, Baltimore County (UMBC),
Baltimore, MD, USA. He was an associate technical
editor of IEEE Communications Magazine, guest ed-
itor of IEEE Journal on Selected Areas in Communications, and an associate
editor for IEEE Transactions on Artiﬁcial Intelligence, IEEE Internet of Things
Journal, IEEE Transactions on Intelligent Transportation Systems, and IEEE
Journal on Miniaturization for Air and Space Systems. His research interests
include cyber-physical systems, Big Data analytics, and Internet of Things.
He has been a Highly Cited Researcher identiﬁed by Clarivate and a Top
1000 Computer Scientist identiﬁed by Research.com. He was a recipient of
10+ Best Paper Awards from major international conferences, including IEEE
CPSCom 2019, IEEE ICII 2019, IEEE/AIAA ICNS 2019, IEEE CBDCom 2020,
WASA 2020, AIAA/ IEEE DASC 2021, IEEE GLOBECOM 2021, and IEEE
INFOCOM 2022. He is also an ACM distinguished member, ACM distinguished
speaker, and IEEE Vehicular Technology Society Distinguished Lecturer.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.
```
