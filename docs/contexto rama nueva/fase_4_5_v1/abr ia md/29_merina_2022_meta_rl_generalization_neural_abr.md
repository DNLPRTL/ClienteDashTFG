# MERINA: Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning

## 0. Ficha de archivo

- Archivo fuente: `MERINA.pdf`
- Paginas detectadas: 11
- SHA256 PDF: `eac15f42c69a998adfa5fadbdf38259bbc74386a50727702093940ae67c1024c`
- Texto crudo auxiliar: `raw_text/29_merina_2022_meta_rl_generalization_neural_abr.txt`
- Texto layout auxiliar: `raw_text_layout/29_merina_2022_meta_rl_generalization_neural_abr_layout.txt`
- Fecha de generacion: 2026-06-09T12:33:33

## 1. Uso previsto para Fase 4-5 v1

Fuente para generalizacion neural ABR mediante meta-RL y contexto latente. Relevante para Fase 4-5 v1 por OOD, entorno variable y estado temporal; probablemente demasiado complejo como base directa.

> Nota de fidelidad: este Markdown es una extraccion tecnica densa para Codex. No es un resumen narrativo ni sustituye al PDF. Para formulas, tablas y figuras criticas, revisar siempre el PDF original.

---

## 2. Identificacion textual de primeras paginas

```text
Improving Generalization for Neural Adaptive Video Streaming
via Meta Reinforcement Learning
Nuowen Kan
Shanghai Jiao Tong University
kannw_1230@sjtu.edu.cn
Yuankun Jiang
Shanghai Jiao Tong University
yuankunjiang@sjtu.edu.cn
Chenglin Li
Shanghai Jiao Tong University
lcl1985@sjtu.edu.cn
Wenrui Dai
Shanghai Jiao Tong University
daiwenrui@sjtu.edu.cn
Junni Zou
Shanghai Jiao Tong University
zoujunni@sjtu.edu.cn
Hongkai Xiong
Shanghai Jiao Tong University
xionghongkai@sjtu.edu.cn
ABSTRACT
In this paper, we present a meta reinforcement learning (Meta-RL)-
based neural adaptive bitrate streaming (ABR) algorithm that is
able to rapidly adapt its control policy to the changing network
throughput dynamics. Specifically, to allow rapid adaptation, we
discuss the necessity of detaching the inference of throughput
dynamics with the universal control mechanism that is in essence
shared by all potential throughput dynamics for neural ABR
algorithms. To meta-learn the ABR policy, we then build up a model-
free system framework, composed of a probabilistic latent encoder
that infers the underlying dynamics from the recent throughput
context, and a policy network that is conditioned on latent variable
and learns to quickly adapt to new environments. Additionally, to
address the difficulties caused by training the policy on mixed
dynamics, on-policy RL (or imitation learning) algorithms are
suggested for policy training, with a mutual information-based
regularization to make the latent variable more informative about
the policy. Finally, we implement our algorithm’s meta-training
and meta-adaptation procedures under a variety of throughput
dynamics. Empirical evaluations on different QoE metrics and
multiple datasets containing real-world network traces demonstrate
that our algorithm outperforms state-of-the-art ABR algorithms, in
terms of the performance on the average chunk QoE, consistency
and fast adaptation across a wide range of throughput patterns.
CCS CONCEPTS
• Information systems →Multimedia streaming; • Comput-
ing methodologies →Sequential decision making.
KEYWORDS
Rate adaptation, meta deep reinforcement learning, generalization.
ACM Reference Format:
Nuowen Kan, Yuankun Jiang, Chenglin Li, Wenrui Dai, Junni Zou, and Hongkai
Xiong. 2022. Improving Generalization for Neural Adaptive Video Streaming
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than ACM
must be honored. Abstracting with credit is permitted. To copy otherwise, or republish,
to post on servers or to redistribute to lists, requires prior specific permission and/or a
fee. Request permissions from permissions@acm.org.
MM ’22, October 10–14, 2022, Lisboa, Portugal
© 2022 Association for Computing Machinery.
ACM ISBN 978-1-4503-9203-7/22/10...$15.00
https://doi.org/10.1145/3503161.3548331
via Meta Reinforcement Learning. In Proceedings of the 30th ACM Inter-
national Conference on Multimedia (MM ’22), October 10–14, 2022, Lisboa,
Portugal. ACM, New York, NY, USA, 11 pages. https://doi.org/10.1145/
3503161.3548331
1
INTRODUCTION
Thanks to the emerging trend that watching videos online has
become a predominant Internet application, it becomes non-
negligible to provide a better quality of experience (QoE) for users
in video streaming via rate adaptation techniques. Through online
video delivery protocols, such as dynamic adaptive streaming over
HTTP (DASH) [20] and HTTP live streaming (HLS) [9], the bitrate,
which indicates the quality or compression level for each video
chunk (or segment), can be dynamically determined to adapt to the
time-varying network throughput and current buffer occupancy of
video player. In general, video quality can be enhanced by assigning
a higher bitrate for the chunk to be transmitted, which, however,
may result in a rebuffering event (i.e., stalling during playback)
especially when the network condition is poor and unstable.
As a key component of rate adaptation, adaptive bitrate stream-
ing (ABR) algorithms aim to solve a stochastic optimal control
problem that reveals how to strike an optimal trade-off between
maximizing the video quality and avoiding the rebuffering, by
determining the fine-grained bitrate combination sequentially for
continuously transmitted video chunks. However, due to the time-
varying and heterogeneous dynamics of network throughput in
real world, it is unfortunately intractable to achieve the optimal
trade-off with an explicit solution. In addition, the ABR algorithm
in practice is also expected to be able to implement quickly online,
because a higher overhead of inference time for rate adaptation
will inevitably increase the end-to-end latency.
To address this challenge, Yin et al. in [24] argued that the
model predictive control (MPC) approach is a natural fit for the
rate adaptation problem and proposed two simple yet effective
algorithms, namely RobustMPC and FastMPC, based on the pre-
diction of future network throughput with the harmonic mean
of past throughput. Following this principle, various studies (e.g.,
CS2P[22], BayesMPC[10], Fugu[23]) have been proposed to seek
for a higher QoE by improving the throughput prediction accuracy.
The weakness of these MPC-based methods is that they would
suffer from issues such as inevitable bias in throughput prediction
and high computational complexity in real world implementation,
which are then alleviated by learning-based methods. By exploiting
the strong non-linear fitting capability of neural networks (NNs),
these learning-based methods are able to directly achieve a superior
3006
MM ’22, October 10–14, 2022, Lisboa, Portugal
Nuowen Kan et al.
QoE performance without any iterative computation. Specifically,
formulated as a Markov decision process (MDP), neural ABR
algorithms consider the most recently recorded throughput values
and current buffer occupancy as the state 𝒔∈S, the selected
bitrate version as the action 𝒂∈A, and directly approximate
an optimal rate adaptation policy 𝜋: S →A without the
need of learning explicitly the throughput prediction. With this
intuition, many efforts have been made to provide users with a
(near)-optimal QoE, by exploiting deep reinforcement learning
```

## 3. Metadatos PDF detectados

```json
{
  "format": "PDF 1.6",
  "title": "Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning",
  "author": "Nuowen Kan",
  "subject": "-  Information systems  ->  Multimedia streaming.-  Computing methodologies  ->  Sequential decision making.",
  "keywords": "Rate adaptation, meta deep reinforcement learning, generalization.",
  "creator": "LaTeX with acmart 2022/04/09 v1.84 Typesetting articles for the Association for Computing Machinery and hyperref 2021-02-27 v7.00k Hypertext links for LaTeX",
  "producer": "Acrobat Distiller 22.0 (Windows)",
  "creationDate": "D:20220719232623+08'00'",
  "modDate": "D:20220830135914-04'00'",
  "trapped": "",
  "encryption": null
}
```

## 4. Mapa de secciones detectado

- p. 1: CCS CONCEPTS
- p. 1: INTRODUCTION
- p. 2: BACKGROUND AND MOTIVATION
- p. 3: PROPOSED METHOD
- p. 5: IMPLEMENTATION
- p. 6: PERFORMANCE EVALUATION
- p. 8: CONCLUSION
- p. 8: ACKNOWLEDGMENTS
- p. 9: REFERENCES
- p. 10: IMPLEMENTATION DETAILS
- p. 10: ADDITIONAL EXPERIMENTAL RESULTS

## 5. Figuras, tablas, algoritmos, ecuaciones o teoremas detectados

- p. 3: Figure 1: System framework of the proposed MERINA.
- p. 5: Algorithm 1 Meta-training Procedure of MERINA
- p. 5: Algorithm 2 Meta-adaptation Procedure of MERINA
- p. 6: Fig. 2(e) verify that in about 80% of sessions, MERINA outperforms
- p. 7: Figure 2: Performance comparison of different ABR algorithms in terms of the average chunk QoE value and the individual
- p. 7: Table 1: Performance comparison of different ABR algorithms in terms of the average chunk 𝑄𝑜𝐸𝑙𝑜𝑔value on different datasets.
- p. 7: Table 1 also includes results from the FCC and HSDPA datasets to
- p. 8: Figure 3: Comparison of 𝑄𝑜𝐸𝑙𝑜𝑔without adaption.
- p. 8: Fig. 4 depicts the performance of an adaptation procedure that
- p. 8: Figure 4: a) The adaptation curves of MERINA and Comyco,
- p. 8: Fig. 4(a) demonstrates that MERINA can outperform RobustMPC
- p. 11: Table 2: Performance comparison of different ABR algorithms in terms of the average chunk 𝑄𝑜𝐸𝑙𝑖𝑛value on different datasets.
- p. 11: Figure 5: Comparison of 𝑄𝑜𝐸𝑙𝑖𝑛without adaption.
- p. 11: Figure 6: a) The adaptation curves of MERINA and Comyco,

## 6. Lineas con posible contenido matematico/formal

Estas lineas NO son LaTeX verificado. Sirven para localizar formulas, objetivos, restricciones o pseudocodigo que hay que verificar en PDF.

- p. 2: `and current buffer occupancy as the state 𝒔∈S, the selected`
- p. 2: `bitrate version as the action 𝒂∈A, and directly approximate`
- p. 2: `of state transition (i.e., 𝒔′ = 𝑓(𝒔, 𝒂) with 𝑓being the dynamics`
- p. 2: `A = {𝑎1,𝑎2, · · · ,𝑎𝑀}, where 𝑀represents the total number of`
- p. 2: `bitrate versions. Let 𝑎𝑘∈A denote the bitrate version allocated for`
- p. 2: `𝐵𝑘= [(𝐵𝑘−1 −𝑑𝑘)+ + 𝐿], 𝑑𝑘= 𝐸𝑎𝑘/𝐶𝑘, (·)+ ≜max{·, 0},`
- p. 3: `as a Markov decision process (MDP), with the state 𝑠𝑘∈S for`
- p. 3: `with available bitrate versions for the 𝑘-th video chunk: 𝐸=`
- p. 3: `𝑟(𝑠𝑘,𝑎𝑘) = 𝑞(𝑎𝑘) −𝛼`
- p. 3: `where 𝑟∈𝑅, 𝑞(𝑎𝑘) can be any video quality metric (e.g., PSNR and`
- p. 3: `𝑘= arg max`
- p. 3: `𝑘=0 𝑟(𝑠𝑘,𝑎𝑘),`
- p. 3: `𝑠𝑘+1 = 𝑓(𝑠𝑘,𝑎𝑘), 𝑎𝑘∈A,`
- p. 3: `can be formulated as < S, A, 𝑃, 𝑅>, where 𝑃= 𝑝(𝑠𝑘+1|𝑠𝑘,𝑎𝑘)`
- p. 3: `a latent variable 𝒛∈𝑍, we can re-formulate the adaptive video`
- p. 3: `the state transition probability changes to 𝑃= 𝑝(𝑠𝑘+1|𝑠𝑘,𝑎𝑘,𝑧𝑘),`
- p. 4: `throughputs. Here, we define the throughput context as 𝒄𝑘−𝑝:𝑘=`
- p. 4: `𝝉= {𝒔, 𝒂, 𝒓} being corresponding samples, as will be detailed in`
- p. 4: `and employ the Gaussian factor 𝑞𝜙(𝒛|𝒄) = N (𝑓𝜇`
- p. 4: `the context 𝒄and the corresponding samples 𝝉= {𝒔, 𝒂, 𝒓}. Due`
- p. 4: `𝐽(𝒄,𝝉) = ˜𝐽(𝒄,𝝉). However, to enable throughput dynamics to be`
- p. 4: `the objective, i.e., maximizing 𝐽(𝒄,𝝉) = ˜𝐽(𝒄,𝝉) + 𝜆I(𝒂; 𝒛|𝒔), where`
- p. 4: `𝜆∈[0, 1] is an annealing parameter that adjusts the strength of`
- p. 4: `I(𝒂; 𝒛|𝒔) = H (𝒂|𝒔) −H (𝒂|𝒛, 𝒔)`
- p. 4: `= −E𝒂[log 𝜋(𝒂|𝒔)] + E𝒂[log 𝜋𝜃(𝒂|𝒔, 𝒛)].`
- p. 4: `𝜋(𝒂|𝒔) =`
- p. 4: `𝜋𝜃(𝒂|𝒔, 𝒛)𝑝(𝒛|𝒔)𝑑𝒛≈`
- p. 4: `𝑖=1 𝜋𝜃(𝒂|𝒔, 𝒛𝑖),`
- p. 4: `work can be optimized via the backward-pass vector ∇𝐽/∇𝒛, i.e.,`
- p. 5: `∇𝐽/∇𝜙= ∇𝐽/∇𝒛· ∇𝒛/∇𝜙. Note that we can pass the gradient from`
- p. 5: `˜𝐽𝜃(𝒄,𝝉) = E𝒛`
- p. 5: `𝜌(𝜃) = 𝜋𝜃(𝒂|𝒔, 𝒛)/𝜋𝜃′(𝒂|𝒔, 𝒛),`
- p. 5: `L𝜃𝑣(𝒄,𝝉) = 1`
- p. 5: `where 𝐺𝑘= 𝑟𝑘+ 𝛾𝑟𝑘+1 + 𝛾2𝑟𝑘+2 + · · · is the rollout QoE return of`
- p. 5: `the current state following 𝜋𝜃′(𝒂|𝒔, 𝒛),𝛾∈(0, 1] is a discount factor`
- p. 5: `2: while 𝑘<= 𝑁update do`
- p. 5: `Update the state with 𝑠𝑘+1 = 𝑓(𝑠𝑘,𝑎𝑘)`
- p. 5: `L𝑎𝑐𝑡𝑜𝑟(𝑏𝑘) = −E𝒛, ˆ𝒂log 𝜋𝜃( ˆ𝒂|𝒔, 𝒛) −𝜆I(𝒂; 𝒛|𝒔)`
- p. 5: `L𝐾𝐿(𝑏𝑘) = 𝛽𝐷KL(𝑞𝜙(𝒛|𝒄)||𝑝(𝒛))`
- p. 5: `𝜃←𝜃−𝛼1∇𝜃L𝑎𝑐𝑡𝑜𝑟(𝑏𝑘)`
- p. 5: `𝜙←𝜙−𝛼3∇𝜙[L𝑎𝑐𝑡𝑜𝑟(𝑏𝑘) + L𝐾𝐿(𝑏𝑘)]`
- p. 5: `Initialize replay buffer B, 𝜃′ = 𝜃`
- p. 5: `for 𝑘= 1, · · · , 𝑁exp do`
- p. 5: `Update the state with 𝑠𝑘+1 = 𝑓(𝑠𝑘,𝑎𝑘)`
- p. 5: `for 𝑖= 1, · · · , 𝑁u do`
- p. 5: `L𝑎𝑐𝑡𝑜𝑟(𝑏𝑖) = −˜𝐽𝜃−𝜆I(𝒂; 𝒛|𝒔), L𝑐𝑟𝑖𝑡𝑖𝑐(𝑏𝑖) = L𝜃𝑣(𝑏𝑖)`
- p. 5: `L𝐾𝐿(𝑏𝑖) = 𝛽𝐷KL(𝑞𝜙(𝒛|𝒄)||𝑝(𝒛))`
- p. 5: `𝜃←𝜃−𝛼1∇𝜃L𝑎𝑐𝑡𝑜𝑟(𝑏𝑖), 𝜃𝑣←𝜃𝑣−𝛼2∇𝜃𝑣L𝑐𝑟𝑖𝑡𝑖𝑐(𝑏𝑖)`
- p. 5: `𝜙←𝜙−𝛼3∇𝜙[L𝑎𝑐𝑡𝑜𝑟(𝑏𝑖) + L𝐾𝐿(𝑏𝑖)]`
- p. 5: `1: for 𝑖= 1, · · · , 𝑁adapt do`
- p. 5: `Initialize replay buffer B, 𝜃′ = 𝜃`
- p. 5: `Rollout policy 𝜋𝜃′(𝑎𝑘|𝑠𝑘,𝑧𝑘) with 𝑠𝑘+1 = 𝑓′(𝑠𝑘,𝑎𝑘) and`
- p. 5: `for 𝑖= 1, · · · , 𝑁u do`
- p. 5: `𝜃←𝜃−𝛼1∇𝜃L𝑎𝑐𝑡𝑜𝑟(𝑏𝑖), 𝜃𝑣←𝜃𝑣−𝛼2∇𝜃𝑣L𝑐𝑟𝑖𝑡𝑖𝑐(𝑏𝑖)`
- p. 5: `𝜙←𝜙−𝛼3∇𝜙[L𝑎𝑐𝑡𝑜𝑟(𝑏𝑖) + L𝐾𝐿(𝑏𝑖)]`
- p. 6: `the available bitrate set is A = {300, 750, 1200, 1850, 2850, 4300}`
- p. 6: `𝐾𝑏𝑝𝑠, the chunk duration is set as 𝐿= 4 seconds, the buffer`
- p. 6: `chunks is 𝐾= 49. For the QoE metric in Eq. (2), we adopt two widely`
- p. 6: `with 𝑞(𝑎𝑘) = 𝑎𝑘/1000, 𝛼= 1, 𝛽= 4.3; and 2) the log-form quality`
- p. 6: `metric 𝑄𝑜𝐸𝑙𝑜𝑔with 𝑞(𝑎𝑘) = log(𝑎𝑘/min(A)), 𝛼= 1, 𝛽= 2.66. For`
- p. 6: `adaptation, the discount factor is set as 𝛾= 0.99. The weights of`
- p. 6: `loss function are set as 𝛽= 0.02, 𝜆= 0.15. Also, we let 𝑝= 8,𝜖=`
- p. 6: `0.04, 𝑁𝑠𝑎= 10, 𝑁update = 650, 𝑁batch = 64, 𝑁𝑢= 2, 𝑁𝑒𝑥𝑝= 256, and`
- p. 6: `set the learning rates as 𝛼1 = 𝛼3 = 10−5, 𝛼2 = 10−4. Our code is`
- p. 6: `horizon of RobustMPC, Fugu and BayesMPC is set to ℎ= 3 chunks.`
- p. 7: `MERINA (nMI with 𝜆= 0, see Appendix B.3)`
- p. 7: `and the performance gap 𝑅𝑔𝑎𝑝= [(𝑟−𝑟∗)/𝑟∗] × 100% to the value`
- p. 10: `The throughput context 𝒄𝑘−𝑝:𝑘= {(𝐶𝑘−𝑝,𝑑𝑘−𝑝), · · · , (𝐶𝑘−1,𝑑𝑘−1)}`
- p. 10: `𝑝chunks. In this paper, we set 𝑝= 8 and input the context`
- p. 10: `the latent variable 𝒛having a dimension of |𝑍| = 64.`
- p. 10: `network consists of a fully connected layer with 𝑀= 6 neurons`
- p. 11: `MERINA (nMI with 𝜆= 0)`
- p. 11: `MERINA (nMI), by setting 𝜆= 0 for the actor loss, on the training`

## 7. Extraccion tecnica por categorias


### 7.1. modelo ia arquitectura algoritmo

Palabras clave usadas: `model, models, neural, architecture, algorithm, policy, agent, actor, critic, actor-critic, DQN, deep Q, Q-learning, PPO, proximal policy, A3C, reinforcement, DRL, deep reinforcement, meta reinforcement, meta-RL, meta learning, MAML, Mamba, state space, SSM, LSTM, policy network, prediction model, Pensieve, SODA, DQNReg, MetaABR, MERINA, Oboe`

**Fragmento 1 - p. 5 - score 12:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal ∇𝐽/∇𝜙= ∇𝐽/∇𝒛· ∇𝒛/∇𝜙. Note that we can pass the gradient from the policy network to inference network with the Gaussian re- parameterization trick [11], even though the latent variable input of policy network is sampled from the output of inference network, i.e., 𝒛∼𝑞𝜙(𝒛|𝒄). 4 IMPLEMENTATION 4.1 Meta-Policy Search with DRL To enable an effective policy search, we build up our algorithm on top of the proximal policy optimization (PPO) algorithm [19], a well known on-policy actor-critic method recognized for its reliable performance on policy improvement with trust region policy optimization. With PPO, we construct two networks: an actor network 𝜋𝜃(𝒂|𝒔, 𝒛) and a critic network 𝑉𝜃𝑣(𝒔, 𝒛). We jointly train the inference and actor networks to maximize the actor loss and the regularization I(𝒂; 𝒛|𝒔) on the parameters of 𝜃and 𝜙. As a result, the objective ˜𝐽𝜃(𝒄,𝝉) of the actor network is expressed as: ˜𝐽𝜃(𝒄,𝝉) = E𝒛

**Fragmento 2 - p. 5 - score 11:**

, (7) 𝜌(𝜃) = 𝜋𝜃(𝒂|𝒔, 𝒛)/𝜋𝜃′(𝒂|𝒔, 𝒛), 𝒛∼𝑞𝜙(𝒛|𝒄) where𝜃′ denotes the previous values of𝜃following the latest update epoch, clip[𝜌(𝜃), 1 −𝜖, 1 + 𝜖] ensures no incentive for moving 𝜌(𝜃) outside the interval [1−𝜖, 1+𝜖], and ˆ𝐴is the truncated generalized advantage estimation (GAE) function [18] generated from the value function 𝑉𝜃𝑣(𝒔, 𝒛) and 𝒓. Similarly, the critic loss is formulated as: L𝜃𝑣(𝒄,𝝉) = 1 2E¯𝒛  (𝑉𝜃𝑣(𝒔, ¯𝒛) −𝐺𝑘)2 , ¯𝒛∼𝑞𝜙(𝒛|𝒄), (8) where 𝐺𝑘= 𝑟𝑘+ 𝛾𝑟𝑘+1 + 𝛾2𝑟𝑘+2 + · · · is the rollout QoE return of the current state following 𝜋𝜃′(𝒂|𝒔, 𝒛),𝛾∈(0, 1] is a discount factor that attenuates exponentially the impact of future actions over the current expected QoE, and ¯𝒛indicates that gradients are not being computed through it. 4.2 Imitation Learning-Based Pre-Training In practice, due to the low sample efficiency of RL training [15], training the meta-RL from scratch is exceedingly time expensive and unstable in our setting of mixed dynamics. Therefore, we pre-train the parameters 𝜙and 𝜃following the imitation learning method proposed in [7], with a behavior cloning objective for the actor and inference networks: max 𝜃,𝜙 E𝒛, ˆ𝒂log 𝜋𝜃( ˆ𝒂|𝒔, 𝒛), 𝒛∼𝑞𝜙(𝒛|𝒄), ˆ𝒂∼𝜋𝑒(𝒂|𝒔), (9) where the model-based ABR algorithm RobustMPC [24] is adopted to obtain the expert policy 𝜋𝑒(𝒂|𝒔), with the QoE maximized over a horizon of future 3 chunks. Here, we skip the pre-training of critic network, since 𝜃𝑣may be rapidly converged with only a few trials following the policy 𝜋𝜃(𝒂|𝒔, 𝒛). Notably, we employ RobustMPC here primarily for its good QoE performance and low computational complexity, which will be also justified by the experimental evaluations in Section 5. However, variants of MERINA can be easily fulfilled by adopting other existing ABR algorithms to obtain the expert policy, resulting in a difference on the training time and overall QoE performance. In summary, the entire meta-training and meta-adaptation workflow of MERINA is given in Algorithm 1 and Algorithm 2, Algorithm 1 Meta-training Procedure of MERINA Require: Dynamics model 𝑓of the video streaming system with time-varying and heterogeneous network dynamics, learning rates 𝛼1, 𝛼2, 𝛼3 // First stage: pre-training with ex

**Fragmento 3 - p. 2 - score 10:**

In this paper, we introduce MERINA, a MEta ReInforcement learning (Meta-RL)-based Neural ABR algorithm, which is able to rapidly adapt its control policy to unfamiliar throughput dynamics. Specifically, we discuss that the rate adaptation problem can be in essence modeled as a partially observable Markov decision process (POMDP), in which the agent is unaware of the underlying information of throughput dynamics. To enable fast adaptation to new throughput dynamics for neural ABR algorithms, it is necessary to separate the dynamics inference from the universal control policy shared by all potential state transition functions. Thus, we adopt the context-based meta-RL method to construct a model-free system framework, consists of a probabilistic latent encoder that infers current throughput dynamics from recent throughput contexts, and a meta-policy network that selects the bitrate per chunk according to the state and sampled latent variable.

**Fragmento 4 - p. 9 - score 9:**

2017. Model-agnostic meta- learning for fast adaptation of deep networks. In International conference on machine learning. PMLR, 1126–1135. [4] Dash Industry Forum. 2022. Catalyzing the Adoption of MPEG-DASH. https: //dashif.org/ [5] Matteo Gadaleta, Federico Chiariotti, Michele Rossi, and Andrea Zanella. 2017. D-DASH: A Deep Q-Learning Framework for DASH Video Streaming. IEEE Transactions on Cognitive Communications and Networking 3, 4 (2017), 703–718. [6] Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. 2018. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. In Proceedings of the 35th International Conference on Machine Learning. 1861–1870. [7] Tianchi Huang, Chao Zhou, Xin Yao, Ruixiao Zhang, Chenglei Wu, Bing Yu, and Lifeng Sun.

**Fragmento 5 - p. 2 - score 7:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. QoE performance without any iterative computation. Specifically, formulated as a Markov decision process (MDP), neural ABR algorithms consider the most recently recorded throughput values and current buffer occupancy as the state 𝒔∈S, the selected bitrate version as the action 𝒂∈A, and directly approximate an optimal rate adaptation policy 𝜋: S →A without the need of learning explicitly the throughput prediction. With this intuition, many efforts have been made to provide users with a (near)-optimal QoE, by exploiting deep reinforcement learning (DRL)-based methods (e.g., Pensieve [14], D-DASH [5]) or imitation learning-based methods (e.g., Comyco [7, 8]).

**Fragmento 6 - p. 11 - score 7:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal Table 2: Performance comparison of different ABR algorithms in terms of the average chunk 𝑄𝑜𝐸𝑙𝑖𝑛value on different datasets. Mean ± std (𝑅𝑔𝑎𝑝) FCC HSDPA Oboe Puffer-Oct.17-21 Puffer-Feb.18-22 BOLA 0.96 ± 0.54 (−20%) 1.12 ± 0.81 (−16%) 1.96 ± 1.03 (−16%) 0.86 ± 1.83 (+1%) 0.66 ± 2.90 (−26%) RobustMPC 0.98 ± 0.75 (−18%) 1.22 ± 1.20 (−9%) 2.30 ± 1.24 (−2%) 0.73 ± 2.16 (−14%) 0.81 ± 2.97 (−9%) Pensieve 1.13 ± 0.65 (−5%) 1.28 ± 0.95 (−5%) 2.26 ± 1.15 (−4%) 0.14 ± 11.55 (−84%) 0.55 ± 8.67 (−44%) Comyco 1.15 ± 0.73 (−3%) 1.34 ± 1.05 (0%) 2.29 ± 1.21 (−2%) −0.13 ± 2.86 (−115%) 0.68 ± 3.06 (−24%) Fugu 1.11 ± 0.70 (−7%) 1.24 ± 1.04 (−7%) 2.31 ± 1.21 (−1%) 0.74 ± 2.13 (−13%) 0.83 ± 2.99 (−7%) BayesMPC 1.10 ± 0.83 (−8%) 1.26 ± 1.11 (−6%) 2.29 ± 1.23 (−2%) 0.33 ± 2.80 (−61%) 0.66 ± 3.34 (−26%) MERINA 1.19 ± 0.67 1.34 ± 0.99 2.34 ± 1.15 0.85 ± 2.02 0.90 ± 2.97 MERINA (nMI with 𝜆= 0) 1.08 ± 0.66 (−9%) 1.22 ± 1.11 (−9%) 2.25 ± 1.19 (−4%) 0.50 ± 2.68 (−61%) 0.72 ± 2.99 (−19%) Dataset distribution 1.13 ± 0.44 Mbps 1.61 ± 0.95 Mbps 2.60 ± 2.08 Mbps 1.85 ± 0.91 Mbps 1.60 ± 0.88 Mbps 0 1 2 3 4 5 4G Public WiFi International Link Average value BOLA RobustMPC Comyco MERINA Figure 5: Comparison of 𝑄𝑜𝐸𝑙𝑖𝑛without adaption.

**Fragmento 7 - p. 1 - score 6:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning Nuowen Kan Shanghai Jiao Tong University kannw_1230@sjtu.edu.cn Yuankun Jiang Shanghai Jiao Tong University yuankunjiang@sjtu.edu.cn Chenglin Li Shanghai Jiao Tong University lcl1985@sjtu.edu.cn Wenrui Dai Shanghai Jiao Tong University daiwenrui@sjtu.edu.cn Junni Zou Shanghai Jiao Tong University zoujunni@sjtu.edu.cn Hongkai Xiong Shanghai Jiao Tong University xionghongkai@sjtu.edu.cn ABSTRACT In this paper, we present a meta reinforcement learning (Meta-RL)- based neural adaptive bitrate streaming (ABR) algorithm that is able to rapidly adapt its control policy to the changing network throughput dynamics.

**Fragmento 8 - p. 2 - score 6:**

• We study the generalization problem of adaptive video streaming, and formulate the rate adaptation problem as a POMDP, rather than previously stated MDP. We then propose a model-free system framework based on context-based meta-RL to improve generalization for neural ABR algorithms, by decoupling the inference of throughput dynamics (referred to as latent encoder) from the universal control mechanism that is shared by all poten- tial throughput dynamics (referred to as meta-policy network). • To ensure rapid adaptation to time-varying yet indistinguishable throughput dynamics in real-world scenarios, we propose an efficient meta-policy search scheme for the mixed dynamics, which includes the use of on-policy RL algorithms (or imitation learning) to alleviate estimation bias for value function, and a mutual information-based regularization in the policy loss to make the latent variable more informative about the policy.

**Fragmento 9 - p. 3 - score 6:**

In the following, we will omit the subscript 𝑘for notational simplicity, i.e., 𝑠𝑘,𝑎𝑘,𝑟𝑘,𝑧𝑘written as 𝒔, 𝒂, 𝒓, 𝒛in places where there is no ambiguity. To the best of our knowledge, most of the previously proposed neural ABR algorithms neglect the variability of transition probabil- ity 𝑃(i.e., under the assumption that the throughput dynamics stay the same over time), thus incorporating the throughput information during download of the past several chunks to the state formulation. The agent trained with such a formulation can learn a universal ABR Video Players Time-varying and heterogeneous throughput dynamics Encoder ࣘ Inference Network (Latent Encoder) contexts l Buffer occupancy latent distribution state Policy Network Meta-Policy st latent Trained by on-policy RL or imitation learning ous bitrate Figure 1: System framework of the proposed MERINA.

**Fragmento 10 - p. 6 - score 6:**

1) BOLA [21]: a buffer-based algorithm that uses Lyapunov optimization to determine the optimal bitrate version under the constraint of buffer occupancy only. 2) RobustMPC [24]: a model-based algorithm that solves the optimization problem in Eq. (3) with a horizon of the future ℎ video chunks under the framework of model predictive control. The future throughput is predicted by the harmonic mean of average throughput measurements of the past 5 downloaded chunks. 3) Pensieve [14]: a DRL-based algorithm that uses the A3C algorithm to learn an optimal neural mapping from the dynamics of buffer occupancy, throughput and chunk size to the rate adaptation of the next chunk. 4) Comyco [7, 8]: a model-free neural ABR algorithm that uses NNs to directly approximate the offline near-optimal expert solution by lifelong imitation learning.

**Fragmento 11 - p. 7 - score 6:**

The results on out-of- distribution datasets (Oboe, Puffer-Oct.17-21 and Puffer-Feb.18- 22) reveal that the NN weights trained in F&H datasets using MERINA provide the highest degree of consistency or generalization performance among the learning-based baselines, over all ranges of varying throughput dynamics. The heuristic ABR algorithms (BOLA and RobustMPC) can always achieve a satisfactory QoE performance on different throughput dynamics, while BOLA beats all the other algorithms on Puffer-Oct.17-21 traces where the throughput dynamics are difficult to predict and considerably deviate from those on the F&H traces. In contrast, the other learning-based methods fail to generalize to the out-of-distribution datasets, verifying the generalization difficulty of DRL or imitation learning-based neural ABR algorithms.

**Fragmento 12 - p. 7 - score 6:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal #FUUFS (a) 𝑄𝑜𝐸𝑙𝑖𝑛 #FUUFS (b) 𝑄𝑜𝐸𝑙𝑖𝑛 0 0.2 0.4 0.6 0.8 1 1.2 1.4 Chunk QoE Bitrate utility Rebuffering penalty Smoothness penalty Averagevalue BOLA RobustMPC Pensieve Comyco Fugu BayesMPC MERINA (c) 𝑄𝑜𝐸𝑙𝑖𝑛 #FUUFS (d) 𝑄𝑜𝐸𝑙𝑜𝑔 #FUUFS (e) 𝑄𝑜𝐸𝑙𝑜𝑔 0 0.2 0.4 0.6 0.8 1 1.2 1.4 Chunk QoE Bitrate utility Rebuffering penalty Smoothness penalty Averagevalue BOLA RobustMPC Pensieve Comyco Fugu BayesMPC MERINA (f) 𝑄𝑜𝐸𝑙𝑜𝑔 Figure 2: Performance comparison of different ABR algorithms in terms of the average chunk QoE value and the individual QoE components with the QoE metrics 𝑄𝑜𝐸𝑙𝑖𝑛and 𝑄𝑜𝐸𝑙𝑜𝑔on F&H (FCC and HSDPA) throughput dataset.

**Fragmento 13 - p. 8 - score 6:**

6 CONCLUSION We have proposed the meta-RL-based adaptive video streaming system MERINA to learn a generalized ABR algorithm. Specifically, we introduced a model-free context-based system framework, composed of a probabilistic inference network (latent encoder) that inferred the underlying dynamics from the recent throughput context, and a latent-conditioned policy network that learned to rapidly adapt to unfamiliar throughput dynamics. We implemented the meta-training and meta-adaptation procedures for MERINA, and demonstrated its efficiency through empirical evaluations on multiple datasets and a real-world platform. The proposed idea for MERINA is not limited to the throughput dynamics. It, in fact, can be extended to video content (e.g., each video chunk may be encoded with different rate-distortion curves w.r.t.

**Fragmento 14 - p. 1 - score 5:**

Specifically, to allow rapid adaptation, we discuss the necessity of detaching the inference of throughput dynamics with the universal control mechanism that is in essence shared by all potential throughput dynamics for neural ABR algorithms. To meta-learn the ABR policy, we then build up a model- free system framework, composed of a probabilistic latent encoder that infers the underlying dynamics from the recent throughput context, and a policy network that is conditioned on latent variable and learns to quickly adapt to new environments. Additionally, to address the difficulties caused by training the policy on mixed dynamics, on-policy RL (or imitation learning) algorithms are suggested for policy training, with a mutual information-based regularization to make the latent variable more informative about the policy.

**Fragmento 15 - p. 7 - score 5:**

Concretely, the model-free neural algorithms (e.g., Pensieve and Comyco) suffer from retaining their capability on Oboe traces while degrading significantly on Puffer traces, particularly on the Puffer-Oct.17-21 dataset. While the model-based algorithms (e.g., Fugu and BayesMPC) that use 3012

**Fragmento 16 - p. 9 - score 5:**

197–210. [15] Anusha Nagabandi, Gregory Kahn, Ronald S. Fearing, and Sergey Levine. 2018. Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning. In 2018 IEEE International Conference on Robotics and Automation (ICRA). 7559–7566. [16] Kate Rakelly, Aurick Zhou, Chelsea Finn, Sergey Levine, and Deirdre Quillen. 2019. Efficient Off-Policy Meta-Reinforcement Learning via Probabilistic Context Variables. In Proceedings of the 36th International conference on machine learning. 5331–5340. [17] Haakon Riiser, Paul Vigmostad, Carsten Griwodz, and Pål Halvorsen. 2013. Commute Path Bandwidth Traces from 3G Networks: Analysis and Applications. In Proceedings of the 4th ACM Multimedia Systems Conference.

**Fragmento 17 - p. 9 - score 5:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal REFERENCES [1] Zahaib Akhtar, Yun Seong Nam, Ramesh Govindan, Sanjay Rao, Jessica Chen, Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan, and Hui Zhang. 2018. Oboe: Auto-Tuning Video ABR Algorithms to Network Conditions. In Proceedings of the Conference of the ACM Special Interest Group on Data Communication. 44–58. [2] Federal Communications Commission. 2016. Raw Data - Measuring Broadband America. (2016). https://www.fcc.gov/reports-research/reports/measuring- broadband-america/raw-data-measuring-broadband-america-2016 [3] Chelsea Finn, Pieter Abbeel, and Sergey Levine.

**Fragmento 18 - p. 10 - score 5:**

In this paper, we set 𝑝= 8 and input the context information of 𝑈𝑘−8 until chunk 𝑈𝑘−1 (i.e., {𝐶𝑘−8, · · · ,𝐶𝑘−1} and {𝑑𝑘−8, · · · ,𝑑𝑘−1}) separately into two one-dimensional convolution layers with 128 filters of size 4 with stride 1. The results of these two convolution layers are then merged into a fully connected layer with 512 neurons, followed by a LeakyReLU activation function. The collected features are finally fed into the output layer, which consists of two parallel fully connected layers with 64 neurons, which represent the outputs of 𝑓𝜇 𝜙(𝒄) and 𝑓𝜎 𝜙(𝒄), respectively, with the latent variable 𝒛having a dimension of |𝑍| = 64. A.2 Policy network The actor and critic networks have the same architecture except for the output layer, but do not share their parameters.

**Fragmento 19 - p. 10 - score 5:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. Appendix A IMPLEMENTATION DETAILS We implement MERINA on a desktop equipped with a 40-core Intel Xeon Silver 4114 Processor, 64GB DDR4 DRAM and an NVIDIA GeForce RTX 2080 graphics card. The inference neural network and the policy neural network that consists of an actor network and a critic network are constructed and trained on PyTorch-1.9.0. Note that we train MERINA on the GPU to maximize the efficiency, though it can be trained on CPUs as well. A.1 Inference Network The throughput context 𝒄𝑘−𝑝:𝑘= {(𝐶𝑘−𝑝,𝑑𝑘−𝑝), · · · , (𝐶𝑘−1,𝑑𝑘−1)} includes the average throughput values and time intervals of throughput measurements collected from the download of previous 𝑝chunks.

**Fragmento 20 - p. 2 - score 4:**

Once deployed in environments with different throughput dynamics, the ABR policy can be learned to adapt to corresponding dynamics with only a few trials. However, due to the time-varying yet indistinguishable feature of throughput dynamics, difficulties emerges in meta-policy search on such a mixed dynamics. Therefore, we propose an efficient meta-policy search scheme, which includes using on-policy RL (or imitation learning) algorithms to alleviate the estimation bias of value function, as well as a mutual information-based regularization in the policy loss to make the latent variable more informative about the policy. Finally, we implement our proposed ABR algorithm with a meta-training procedure where a regularized proximal policy optimization (PPO) algorithm is used to train the inference network (encoder) and the latent-conditioned meta- policy by following an imitation learning-based pre-training, and a meta-adaptation procedure that aims to rapidly adapt the meta- policy to unseen throughput dynamics by using the same PPO update.

**Fragmento 21 - p. 3 - score 4:**

policy that performs well if the distribution of throughput dynamics has been experienced in the training dataset, but may unfortunately present a very poor generalization in unseen (or out-of-distribution) network contexts. Meta-RL, as a popular method for fast adaptation to unseen environments, trains an agent from multiple sample tasks to construct a meta-policy over the shared structure across tasks [3, 16]. We are therefore motivated to propose MERINA, a context- based meta-RL approach for decoupling inference of underlying network dynamics 𝒛from the universal control mechanism. Other than learning a separate ABR control policy for each possible network throughput dynamic from millions of samples, we would like our ABR agent to discover a common control mechanism (i.e., meta-policy 𝜋(𝒂|𝒔, 𝒛)) shared across a range of possible throughput dynamics during the training.

**Fragmento 22 - p. 3 - score 4:**

Once learned, this policy is expected to adapt to new throughput dynamics with only a few trials when their necessary latent variable 𝒛is provided. In other words, with MERINA we intend to develop a generalized paradigm for neural ABR algorithms, by learning how to rapidly learn an appropriate ABR policy for each network environment. 3 PROPOSED METHOD The overall system framework of MERINA is illustrated in Fig. 1, comprising two following two key components. • 1) Meta-trained dynamics inference network (i.e., latent encoder). To endow the control policy with an effective represen- tation of current network dynamics, we capture the knowledge about underlying dynamics with a latent probabilistic context variable 𝒛based on recent experience of the current (new) dynamics.

**Fragmento 23 - p. 7 - score 4:**

Table 1: Performance comparison of different ABR algorithms in terms of the average chunk 𝑄𝑜𝐸𝑙𝑜𝑔value on different datasets. Mean ± std (𝑅𝑔𝑎𝑝) FCC HSDPA Oboe Puffer-Oct.17-21 Puffer-Feb.18-22 BOLA 0.95 ± 0.63 (−17%) 1.11 ± 0.64 (−9%) 1.63 ± 0.66 (−11%) 0.88 ± 1.29 (+20%) 0.75 ± 1.93 (−14%) RobustMPC 1.05 ± 0.63 (−8%) 1.16 ± 0.85 (−5%) 1.79 ± 0.73 (−2%) 0.76 ± 1.48 (+5%) 0.86 ± 2.01 (−2%) Pensieve 1.07 ± 0.62 (−7%) 1.21 ± 0.68 (−1%) 1.75 ± 0.69 (−4%) 0.40 ± 7.17 (−46%) 0.66 ± 5.40 (−25%) Comyco 1.11 ± 0.63 (−3%) 1.22 ± 0.78 (−0%) 1.76 ± 0.77 (−3%) −0.22 ± 2.20 (−130%) 0.65 ± 2.25 (−26%) Fugu 1.04 ± 0.70 (−10%) 1.16 ± 0.80 (−5%) 1.71 ± 0.78 (−6%) 0.54 ± 1.55 (−26%) 0.77 ± 1.94 (−12%) BayesMPC 1.05 ± 0.78 (−9%) 1.09 ± 0.84 (−2%) 1.78 ± 0.74 (−2%) 0.54 ± 1.88 (−26%) 0.76 ± 2.20 (−14%) MARINA 1.15 ± 0.66 1.22 ± 0.85 1.82 ± 0.70 0.73 ± 1.63 0.88 ± 2.00 MERINA (nMI with 𝜆= 0, see Appendix B.3) 1.05 ± 0.65 (−9%) 1.19 ± 0.71 (−2%) 1.74 ± 0.69 (−4%) 0.71 ± 1.58 (−2%) 0.83 ± 1.96 (−5%) Dataset distribution 1.13 ± 0.44 Mbps 1.61 ± 0.95 Mbps 2.60 ± 2.08 Mbps 1.85 ± 0.91 Mbps 1.60 ± 0.88 Mbps is just 0.3 less than RobustMPC’s.

**Fragmento 24 - p. 7 - score 4:**

Furthermore, the bar graphs in Figs. 2(c) and 2(f) indicate that MERINA can surprisingly achieve low rebuffering and smoothness penalties, similar to those of Pensieve. While other algorithms result in either a longer rebuffering time, as Comyco does, or a higher quality fluctuation, as BOLA does, during the video playback. Note that the results obtained for linear QoE metric 𝑄𝑜𝐸𝑙𝑖𝑛are similar to those for log-form QoE metric 𝑄𝑜𝐸𝑙𝑜𝑔w.r.t. all comparison algorithms. Therefore, we only show and compare the performance for 𝑄𝑜𝐸𝑙𝑜𝑔in the following, and move results of 𝑄𝑜𝐸𝑙𝑖𝑛to Appendix B due to page limit. 5.2 Consistency on Out-of-Distribution Traces To study the consistency of MERINA in comparison to other learning-based methods, we measure their performance on out- of-distribution datasets Oboe, Puffer-Oct.17-21 and Puffer-Feb.18- 22 (i.e., with a different distribution of throughput dynamics than F&H dataset) by using the same NN weights obtained in Section 5.1 (i.e., learned from the F&H dataset).

**Fragmento 25 - p. 8 - score 4:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. 0 0.5 1 1.5 2 2.5 3 4G Public WiFi International Link Average value BOLA RobustMPC Comyco MERINA Figure 3: Comparison of 𝑄𝑜𝐸𝑙𝑜𝑔without adaption. NNs to learn the throughput dynamics have a better consistency or generalization than Pensieve and Comyco, though they also perform much worse on Puffer traces than heuristic methods. This demonstrates that, besides meta-RL-based methods, model-based methods are another viable paradigm for addressing the general- ization challenge of adaptive video streaming. In conclusion, our MERINA performs consistently with out-of-distribution throughput dynamics, though it may have a worse QoE than BOLA in some sessions.

**Fragmento 26 - p. 9 - score 4:**

114–118. [18] John Schulman, Philipp Moritz, Sergey Levine, Michael Jordan, and Pieter Abbeel. 2018. High-Dimensional Continuous Control Using Generalized Advantage Estimation. arXiv:1506.02438 [cs.LG] [19] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. 2017. Proximal Policy Optimization Algorithms. arXiv:1707.06347 [cs.LG] [20] I. Sodagar. 2011. The MPEG-DASH Standard for Multimedia Streaming Over the Internet. IEEE MultiMedia 18, 4 (2011), 62–67. [21] Kevin Spiteri, Rahul Urgaonkar, and Ramesh Sitaraman. 2016. BOLA: Near- Optimal Bitrate Adaptation for Online Videos. In Proceedings of the 35th Annual IEEE International Conference on Computer Communications. 1–9. [22] Yi Sun, Xiaoqi Yin, Junchen Jiang, Vyas Sekar, Fuyuan Lin, Nanshu Wang, Tao Liu, and Bruno Sinopoli.


### 7.2. estado inputs features observaciones

Palabras clave usadas: `state, states, input, inputs, feature, features, observation, observations, throughput, bandwidth, buffer, download time, download duration, chunk size, segment size, history, past, remaining, last bitrate, network condition, QoE objective, task, environment, session, forecast, prediction, representation`

**Fragmento 1 - p. 3 - score 8:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal as a Markov decision process (MDP), with the state 𝑠𝑘∈S for downloading the chunk 𝑈𝑘represented by six features, namely the measured 1) average throughput 𝐶𝑘−1 and 2) corresponding download time 𝑑𝑘−1, 3) the vector of chunk sizes associated with available bitrate versions for the 𝑘-th video chunk: 𝐸= {𝐸𝑘𝑎1, 𝐸𝑘𝑎2, · · · , 𝐸𝑘𝑎𝑀}, 4) current buffer occupancy 𝐵𝑘−1, 5) selected bitrate 𝑎𝑘−1 of the last video chunk, and 6) the remaining number of video chunks that have not been downloaded yet. To quantify the user’s QoE, we employ a widely used objective metric that incorporates the trade-off between video quality, quality fluctuation and risk of rebuffering events as a linear combination: 𝑟(𝑠𝑘,𝑎𝑘) = 𝑞(𝑎𝑘) −𝛼 𝑞(𝑎𝑘) −𝑞(𝑎𝑘−1)  −𝛽(𝑑𝑘−𝐵𝑘−1)+ , (2) where 𝑟∈𝑅, 𝑞(𝑎𝑘) can be any video quality metric (e.g., PSNR and SSIM), and 𝛼and 𝛽are a non-negative penalty weight that ensures the temporal quality smoothness and penalizes the rebuffering delay, respectively.

**Fragmento 2 - p. 10 - score 8:**

The state of the video streaming system, includes the features as detailed in Section 2, is fed into the input layer of the actor and critic networks. Concretely, for the set of available bitrate versions A, we use a one-dimensional convolution layer with 128 filters, each of size 4 with stride 1, to process them. Meanwhile, five full connected layers with 128 neurons are placed at the input layer to deal with the remaining features of the state, including the measured average throughput 𝐶𝑘−1, time duration 𝑑𝑘−1 during the download of the last video chunk, current buffer occupancy 𝐵𝑘, selected bitrate 𝑎𝑘−1 of the last chunk, and the number of video chunks that have not been downloaded yet. For the latent variable sampled from the posterior 𝑞𝜙(𝒛|𝒄), we also use a fully connected layer with 1280 neurons to process the latent representations.

**Fragmento 3 - p. 2 - score 4:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. QoE performance without any iterative computation. Specifically, formulated as a Markov decision process (MDP), neural ABR algorithms consider the most recently recorded throughput values and current buffer occupancy as the state 𝒔∈S, the selected bitrate version as the action 𝒂∈A, and directly approximate an optimal rate adaptation policy 𝜋: S →A without the need of learning explicitly the throughput prediction. With this intuition, many efforts have been made to provide users with a (near)-optimal QoE, by exploiting deep reinforcement learning (DRL)-based methods (e.g., Pensieve [14], D-DASH [5]) or imitation learning-based methods (e.g., Comyco [7, 8]).

**Fragmento 4 - p. 3 - score 4:**

Encountering a new network environment, this latent variable 𝒛can reason about dynamics uncertainty, allowing for a stochastic exploration of meta-learned policy to explore states with potentially higher rewards while also quickly adapting to the new dynamics. Meanwhile, sampling the latent variable from a probabilistic distribution improves the generalization of control policies when a deterministic inference of dynamics is difficult. • 2) Latent-conditioned policy network (i.e., policy search). To identify a universal ABR control policy capable of adapting its behavior to the network throughput dynamics, we set a 𝜃- parameterized policy 𝜋𝜃(𝒂|𝒔, 𝒛) as conditioned on the latent variable 𝒛. Thus, if the latent variable 𝒛can be reliably inferred from the recent experience, the resulting policy 𝜋𝜃(𝒂|𝒔, 𝒛) will potentially adapt to a new network environment.

**Fragmento 5 - p. 3 - score 4:**

In the following, we will omit the subscript 𝑘for notational simplicity, i.e., 𝑠𝑘,𝑎𝑘,𝑟𝑘,𝑧𝑘written as 𝒔, 𝒂, 𝒓, 𝒛in places where there is no ambiguity. To the best of our knowledge, most of the previously proposed neural ABR algorithms neglect the variability of transition probabil- ity 𝑃(i.e., under the assumption that the throughput dynamics stay the same over time), thus incorporating the throughput information during download of the past several chunks to the state formulation. The agent trained with such a formulation can learn a universal ABR Video Players Time-varying and heterogeneous throughput dynamics Encoder ࣘ Inference Network (Latent Encoder) contexts l Buffer occupancy latent distribution state Policy Network Meta-Policy st latent Trained by on-policy RL or imitation learning ous bitrate Figure 1: System framework of the proposed MERINA.

**Fragmento 6 - p. 6 - score 4:**

1) BOLA [21]: a buffer-based algorithm that uses Lyapunov optimization to determine the optimal bitrate version under the constraint of buffer occupancy only. 2) RobustMPC [24]: a model-based algorithm that solves the optimization problem in Eq. (3) with a horizon of the future ℎ video chunks under the framework of model predictive control. The future throughput is predicted by the harmonic mean of average throughput measurements of the past 5 downloaded chunks. 3) Pensieve [14]: a DRL-based algorithm that uses the A3C algorithm to learn an optimal neural mapping from the dynamics of buffer occupancy, throughput and chunk size to the rate adaptation of the next chunk. 4) Comyco [7, 8]: a model-free neural ABR algorithm that uses NNs to directly approximate the offline near-optimal expert solution by lifelong imitation learning.

**Fragmento 7 - p. 6 - score 4:**

The CDFs in Figs. 2(b) and 2(e) illustrate the QoE improvements of the other algorithms over RobustMPC in all sessions. And the bar graphs in Figs. 2(c) and 2(f) show the average chunk QoE and each individual components in Eq. (2), where the error bars span ± one standard deviation from the average value. The key observation is that MERINA outperforms the other baseline algorithms in terms of the average chunk QoE value with both the linear and log-form QoE metrics on the F&H throughput dataset. The performance gap of the average chunk QoE between MERINA and the baseline algorithms is at least 3% and 4% for 𝑄𝑜𝐸𝑙𝑖𝑛and 𝑄𝑜𝐸𝑙𝑜𝑔, respectively. And Comyco beats the remaining baseline algorithms in terms of QoE (slightly better than Pensieve), demonstrating the effectiveness of imitation learning.

**Fragmento 8 - p. 10 - score 4:**

A.3 Virtual Player The virtual player, with reference to the open-sourced ABR simula- tor used by Pensieve and Comyco, includes three key components: 1) a video client that emulates the video playback and the buffer oc- cupancy; 2) a video delivery simulator that emulates the download of available video chunks from the video server to the client, under network conditions that are emulated from our stated datasets of network throughput, along with an 80 ms RTT and a packet loss rate of 0.95; and 3) an ABR controller that employs the ABR algorithms (e.g., MERINA and other baseline algorithms) to decide the rule of which bitrate version being requested for the next requested video chunk that has not been downloaded yet.

**Fragmento 9 - p. 1 - score 3:**

In general, video quality can be enhanced by assigning a higher bitrate for the chunk to be transmitted, which, however, may result in a rebuffering event (i.e., stalling during playback) especially when the network condition is poor and unstable. As a key component of rate adaptation, adaptive bitrate stream- ing (ABR) algorithms aim to solve a stochastic optimal control problem that reveals how to strike an optimal trade-off between maximizing the video quality and avoiding the rebuffering, by determining the fine-grained bitrate combination sequentially for continuously transmitted video chunks. However, due to the time- varying and heterogeneous dynamics of network throughput in real world, it is unfortunately intractable to achieve the optimal trade-off with an explicit solution.

**Fragmento 10 - p. 1 - score 3:**

In addition, the ABR algorithm in practice is also expected to be able to implement quickly online, because a higher overhead of inference time for rate adaptation will inevitably increase the end-to-end latency. To address this challenge, Yin et al. in [24] argued that the model predictive control (MPC) approach is a natural fit for the rate adaptation problem and proposed two simple yet effective algorithms, namely RobustMPC and FastMPC, based on the pre- diction of future network throughput with the harmonic mean of past throughput. Following this principle, various studies (e.g., CS2P[22], BayesMPC[10], Fugu[23]) have been proposed to seek for a higher QoE by improving the throughput prediction accuracy.

**Fragmento 11 - p. 2 - score 3:**

Once deployed in environments with different throughput dynamics, the ABR policy can be learned to adapt to corresponding dynamics with only a few trials. However, due to the time-varying yet indistinguishable feature of throughput dynamics, difficulties emerges in meta-policy search on such a mixed dynamics. Therefore, we propose an efficient meta-policy search scheme, which includes using on-policy RL (or imitation learning) algorithms to alleviate the estimation bias of value function, as well as a mutual information-based regularization in the policy loss to make the latent variable more informative about the policy. Finally, we implement our proposed ABR algorithm with a meta-training procedure where a regularized proximal policy optimization (PPO) algorithm is used to train the inference network (encoder) and the latent-conditioned meta- policy by following an imitation learning-based pre-training, and a meta-adaptation procedure that aims to rapidly adapt the meta- policy to unseen throughput dynamics by using the same PPO update.

**Fragmento 12 - p. 2 - score 3:**

However, the superior performance of existing neural ABR algo- rithms is subject to certain conditions, such as that the probability of state transition (i.e., 𝒔′ = 𝑓(𝒔, 𝒂) with 𝑓being the dynamics transition function) is identical or similar between the training and deployment environments. This condition is unfortunately not satisfied in many real-world scenarios, possibly resulting in a poor consistency of neural ABR algorithm’s performance across a range of network throughput patterns [1, 10, 13, 23]. Though a lifelong learning method was proposed in [7] to address this issue by continuously fine-tuning the NNs with new throughput data online, it is still not a natural choice for neural ABR algorithms, since NNs trained with certain known dynamics will lose their ability to quickly fit to new dynamics over time [12].

**Fragmento 13 - p. 3 - score 3:**

Therefore, the control policy of the ABR algorithm can be derived by solving a sequential decision-making problem that optimizes the average chunk QoE for the user under a constrained yet time-varying network throughput: 𝑎∗ 𝑘= arg max 𝑎 1 𝐾 𝐾 𝑘=0 𝑟(𝑠𝑘,𝑎𝑘), (3a) s.t. 𝑠𝑘+1 = 𝑓(𝑠𝑘,𝑎𝑘), 𝑎𝑘∈A, (3b) where the dynamics model 𝑓: S × A →S of the video streaming system includes the buffer occupancy as given in Eq. (1), as well as the dynamics of network throughput which unfortunately cannot be explicitly represented or predicted. As such, we are theoretically unable to find the global optimal solution of Eq. (3), but endeavour in practice to approach as closer as possible to this global optimum. 2.2 Learning How to Learn Bitrate Adaptation As a result, the MDP of an adaptive video streaming system can be formulated as < S, A, 𝑃, 𝑅>, where 𝑃= 𝑝(𝑠𝑘+1|𝑠𝑘,𝑎𝑘) is the state transition probability that mainly depends on the dynamics of network throughput.

**Fragmento 14 - p. 3 - score 3:**

policy that performs well if the distribution of throughput dynamics has been experienced in the training dataset, but may unfortunately present a very poor generalization in unseen (or out-of-distribution) network contexts. Meta-RL, as a popular method for fast adaptation to unseen environments, trains an agent from multiple sample tasks to construct a meta-policy over the shared structure across tasks [3, 16]. We are therefore motivated to propose MERINA, a context- based meta-RL approach for decoupling inference of underlying network dynamics 𝒛from the universal control mechanism. Other than learning a separate ABR control policy for each possible network throughput dynamic from millions of samples, we would like our ABR agent to discover a common control mechanism (i.e., meta-policy 𝜋(𝒂|𝒔, 𝒛)) shared across a range of possible throughput dynamics during the training.

**Fragmento 15 - p. 4 - score 3:**

In the following, we will often write 𝒄𝑘−𝑝:𝑘as 𝒄for notational simplicity. Due to the time-varying nature of the underlying network throughput dynamics, we only collect the past experience from the most recent 𝑝chunks, rather than from the beginning of video playback. Additionally, we make the assumption that the true chunk sizes will remain relatively constant throughout all video chunks for each bitrate version, thus omitting the dynamics inference for video content. To approximate the posterior 𝑝(𝒛|𝒄) over latent variable space 𝑍, we build up an inference network that generates the distribution 𝑞𝜙(𝒛|𝒄) parameterized by 𝜙. This inference network can be trained via a model-free manner by using the method described in [16], with the goal of directly maximizing a variational lower bound: E(𝒄,𝝉)∼B  𝐽(𝒄,𝝉) + 𝛽𝐷KL 𝑞𝜙(𝒛|𝒄)||𝑝(𝒛) , (4) where 𝑝(𝒛) is a unit Gaussian prior over 𝑍, and 𝐽(𝒄,𝝉) may be any objective chosen from a variety of those for policy search, with 𝝉= {𝒔, 𝒂, 𝒓} being corresponding samples, as will be detailed in Sections 3.2 and 4.

**Fragmento 16 - p. 4 - score 3:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. policy-gradient RL or imitation learning. However, the training data contain too many different types of underlying network dynamics to enable an informative latent representation about the policy. To solve this issue, a mutual information-based regularization is further proposed, in addition to the basic loss function. 3.1 Modeling the Uncertainty of Inference To facilitate adaptation, the latent variable 𝒛should encode an effective representation of the current network throughput dy- namics by exploiting a collection of past experienced network throughputs. Here, we define the throughput context as 𝒄𝑘−𝑝:𝑘= {(𝐶𝑘−𝑝,𝑑𝑘−𝑝), · · · , (𝐶𝑘−1,𝑑𝑘−1)}, which consists of the average throughput values and time intervals of throughput measurements collected from the download of chunk 𝑈𝑘−𝑝to chunk 𝑈𝑘−1.

**Fragmento 17 - p. 4 - score 3:**

Besides, modeling the uncertainty enables a stochastic exploration for meta-policy adaptation in response to new environments, hence increasing the sample efficiency of policy search. In the outer expectation of Eq. (4), the replay buffer B contains recent historical experience of environment interaction, including the context 𝒄and the corresponding samples 𝝉= {𝒔, 𝒂, 𝒓}. Due to the fact that the throughput dynamics in real world scenarios are time-varying and heterogeneous, it is infeasible to identify the distinct network throughput dynamics from the environment of adaptive video streaming. In other worlds, in an arbitrary trajectory {(𝒄0:𝑝,𝝉𝑝), · · · , (𝒄𝑘−𝑝:𝑘,𝝉𝑘), · · · } from interacting with the environment, the agent may experience multiple types of throughput dynamics, which we call the mixed dynamics.

**Fragmento 18 - p. 6 - score 3:**

Therefore, we re-implement Fugu and utilize it as a baseline ABR algorithm that optimizes the expectation of QoE with a probabilistic download time predictor. Additionally, the planning horizon of RobustMPC, Fugu and BayesMPC is set to ℎ= 3 chunks. Datasets of network throughput. We collect four public real- world network throughput datasets (3G/HSDPA [17], FCC [2], Oboe [1], Puffer [23]) to simulate various user and network conditions. The mean and standard deviation values of these datasets are listed in bottom row of Table 1. We combine the similar datasets FCC and 3G/HSDPA into one dataset (named F&H), which is then used to validate the in-distribution performance of different ABR algorithms. Note that the datasets 3G/HSDPA, FCC and Oboe contain only a small amount of traces, but the throughput data of Puffer is updated daily (data of a single day takes up to several GB) and has been regularly updated since January 2019.

**Fragmento 19 - p. 6 - score 3:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. 5 PERFORMANCE EVALUATION Experiment setup. To evaluate the performance in terms of the average chunk QoE, consistency and fast adaptation across a wide range of throughput patterns, we test MERINA on the virtual player as widely used in [1, 7, 8, 10, 14], which simulates the adaptive video streaming process by using the real-world network throughput datasets, in comparison to other ABR algorithms. For the sake of fairness, we also use the same environment settings as in [7, 8, 14]: the available bitrate set is A = {300, 750, 1200, 1850, 2850, 4300} 𝐾𝑏𝑝𝑠, the chunk duration is set as 𝐿= 4 seconds, the buffer occupancy is limited as 1 minute, and the total number of video chunks is 𝐾= 49.

**Fragmento 20 - p. 8 - score 3:**

The results indicate that after 30-epoch adaptation, the proportion of sessions that achieve much lower/higher QoE value than RobustMPC significantly decreases/increases. And after 200-epochs adaptation, MERINA has a similar distribution to BOLA, in terms of average QoE improvement. While Comyco’s performance cannot be improved rapidly due to its low initial performance, and also because the lifelong learning method cannot ensure policy improvement in a significantly changed environment. The asymptotic performance of MERINA indicates that it can achieve a superior QoE performance when compared to all baselines following a meta-adaptation pro- cedure, implying that MERINA can achieve the best generalization performance and will outperform baseline algorithms across a range of throughput dynamics through the adaptation.

**Fragmento 21 - p. 8 - score 3:**

More importantly, MERINA can further rapidly adapt to the new throughput dynamics via a few updates (see Section 5.3). Real-World Test. We then evaluate MERINA, Comyco (the state- of-the-art model-free ABR algorithm) and the heuristic algorithms BOLA and RobustMPC in the real world platform under three different network conditions: a 4G cellular network, a public WiFi network on campus, and a wide area network connecting Shanghai and Los Angeles, with mean and standard deviation of recorded throughput values of 5.74 ± 0.39𝑀𝑏𝑝𝑠, 2.04 ± 0.89𝑀𝑏𝑝𝑠 and 1.78 ± 1.10𝑀𝑏𝑝𝑠. The real-world platform based on Dash.js [4] is implemented similarly to that in [7, 14], and we thus omit its description for simplicity.

**Fragmento 22 - p. 10 - score 3:**

In this paper, we set 𝑝= 8 and input the context information of 𝑈𝑘−8 until chunk 𝑈𝑘−1 (i.e., {𝐶𝑘−8, · · · ,𝐶𝑘−1} and {𝑑𝑘−8, · · · ,𝑑𝑘−1}) separately into two one-dimensional convolution layers with 128 filters of size 4 with stride 1. The results of these two convolution layers are then merged into a fully connected layer with 512 neurons, followed by a LeakyReLU activation function. The collected features are finally fed into the output layer, which consists of two parallel fully connected layers with 64 neurons, which represent the outputs of 𝑓𝜇 𝜙(𝒄) and 𝑓𝜎 𝜙(𝒄), respectively, with the latent variable 𝒛having a dimension of |𝑍| = 64. A.2 Policy network The actor and critic networks have the same architecture except for the output layer, but do not share their parameters.

**Fragmento 23 - p. 1 - score 2:**

ACM ISBN 978-1-4503-9203-7/22/10...$15.00 https://doi.org/10.1145/3503161.3548331 via Meta Reinforcement Learning. In Proceedings of the 30th ACM Inter- national Conference on Multimedia (MM ’22), October 10–14, 2022, Lisboa, Portugal. ACM, New York, NY, USA, 11 pages. https://doi.org/10.1145/ 3503161.3548331 1 INTRODUCTION Thanks to the emerging trend that watching videos online has become a predominant Internet application, it becomes non- negligible to provide a better quality of experience (QoE) for users in video streaming via rate adaptation techniques. Through online video delivery protocols, such as dynamic adaptive streaming over HTTP (DASH) [20] and HTTP live streaming (HLS) [9], the bitrate, which indicates the quality or compression level for each video chunk (or segment), can be dynamically determined to adapt to the time-varying network throughput and current buffer occupancy of video player.

**Fragmento 24 - p. 1 - score 2:**

Specifically, to allow rapid adaptation, we discuss the necessity of detaching the inference of throughput dynamics with the universal control mechanism that is in essence shared by all potential throughput dynamics for neural ABR algorithms. To meta-learn the ABR policy, we then build up a model- free system framework, composed of a probabilistic latent encoder that infers the underlying dynamics from the recent throughput context, and a policy network that is conditioned on latent variable and learns to quickly adapt to new environments. Additionally, to address the difficulties caused by training the policy on mixed dynamics, on-policy RL (or imitation learning) algorithms are suggested for policy training, with a mutual information-based regularization to make the latent variable more informative about the policy.

**Fragmento 25 - p. 1 - score 2:**

Finally, we implement our algorithm’s meta-training and meta-adaptation procedures under a variety of throughput dynamics. Empirical evaluations on different QoE metrics and multiple datasets containing real-world network traces demonstrate that our algorithm outperforms state-of-the-art ABR algorithms, in terms of the performance on the average chunk QoE, consistency and fast adaptation across a wide range of throughput patterns. CCS CONCEPTS • Information systems →Multimedia streaming; • Comput- ing methodologies →Sequential decision making. KEYWORDS Rate adaptation, meta deep reinforcement learning, generalization. ACM Reference Format: Nuowen Kan, Yuankun Jiang, Chenglin Li, Wenrui Dai, Junni Zou, and Hongkai Xiong.

**Fragmento 26 - p. 1 - score 2:**

The weakness of these MPC-based methods is that they would suffer from issues such as inevitable bias in throughput prediction and high computational complexity in real world implementation, which are then alleviated by learning-based methods. By exploiting the strong non-linear fitting capability of neural networks (NNs), these learning-based methods are able to directly achieve a superior 3006


### 7.3. accion decision abr salida

Palabras clave usadas: `action, actions, bitrate, bit rate, quality level, representation, decision, decisions, select, selection, adaptation, output, score, guidance, recommend, priority, policy output, controller, rate adaptation, quality`

**Fragmento 1 - p. 2 - score 6:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. QoE performance without any iterative computation. Specifically, formulated as a Markov decision process (MDP), neural ABR algorithms consider the most recently recorded throughput values and current buffer occupancy as the state 𝒔∈S, the selected bitrate version as the action 𝒂∈A, and directly approximate an optimal rate adaptation policy 𝜋: S →A without the need of learning explicitly the throughput prediction. With this intuition, many efforts have been made to provide users with a (near)-optimal QoE, by exploiting deep reinforcement learning (DRL)-based methods (e.g., Pensieve [14], D-DASH [5]) or imitation learning-based methods (e.g., Comyco [7, 8]).

**Fragmento 2 - p. 2 - score 5:**

In this paper, we introduce MERINA, a MEta ReInforcement learning (Meta-RL)-based Neural ABR algorithm, which is able to rapidly adapt its control policy to unfamiliar throughput dynamics. Specifically, we discuss that the rate adaptation problem can be in essence modeled as a partially observable Markov decision process (POMDP), in which the agent is unaware of the underlying information of throughput dynamics. To enable fast adaptation to new throughput dynamics for neural ABR algorithms, it is necessary to separate the dynamics inference from the universal control policy shared by all potential state transition functions. Thus, we adopt the context-based meta-RL method to construct a model-free system framework, consists of a probabilistic latent encoder that infers current throughput dynamics from recent throughput contexts, and a meta-policy network that selects the bitrate per chunk according to the state and sampled latent variable.

**Fragmento 3 - p. 1 - score 4:**

ACM ISBN 978-1-4503-9203-7/22/10...$15.00 https://doi.org/10.1145/3503161.3548331 via Meta Reinforcement Learning. In Proceedings of the 30th ACM Inter- national Conference on Multimedia (MM ’22), October 10–14, 2022, Lisboa, Portugal. ACM, New York, NY, USA, 11 pages. https://doi.org/10.1145/ 3503161.3548331 1 INTRODUCTION Thanks to the emerging trend that watching videos online has become a predominant Internet application, it becomes non- negligible to provide a better quality of experience (QoE) for users in video streaming via rate adaptation techniques. Through online video delivery protocols, such as dynamic adaptive streaming over HTTP (DASH) [20] and HTTP live streaming (HLS) [9], the bitrate, which indicates the quality or compression level for each video chunk (or segment), can be dynamically determined to adapt to the time-varying network throughput and current buffer occupancy of video player.

**Fragmento 4 - p. 1 - score 4:**

In general, video quality can be enhanced by assigning a higher bitrate for the chunk to be transmitted, which, however, may result in a rebuffering event (i.e., stalling during playback) especially when the network condition is poor and unstable. As a key component of rate adaptation, adaptive bitrate stream- ing (ABR) algorithms aim to solve a stochastic optimal control problem that reveals how to strike an optimal trade-off between maximizing the video quality and avoiding the rebuffering, by determining the fine-grained bitrate combination sequentially for continuously transmitted video chunks. However, due to the time- varying and heterogeneous dynamics of network throughput in real world, it is unfortunately intractable to achieve the optimal trade-off with an explicit solution.

**Fragmento 5 - p. 3 - score 4:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal as a Markov decision process (MDP), with the state 𝑠𝑘∈S for downloading the chunk 𝑈𝑘represented by six features, namely the measured 1) average throughput 𝐶𝑘−1 and 2) corresponding download time 𝑑𝑘−1, 3) the vector of chunk sizes associated with available bitrate versions for the 𝑘-th video chunk: 𝐸= {𝐸𝑘𝑎1, 𝐸𝑘𝑎2, · · · , 𝐸𝑘𝑎𝑀}, 4) current buffer occupancy 𝐵𝑘−1, 5) selected bitrate 𝑎𝑘−1 of the last video chunk, and 6) the remaining number of video chunks that have not been downloaded yet. To quantify the user’s QoE, we employ a widely used objective metric that incorporates the trade-off between video quality, quality fluctuation and risk of rebuffering events as a linear combination: 𝑟(𝑠𝑘,𝑎𝑘) = 𝑞(𝑎𝑘) −𝛼 𝑞(𝑎𝑘) −𝑞(𝑎𝑘−1)  −𝛽(𝑑𝑘−𝐵𝑘−1)+ , (2) where 𝑟∈𝑅, 𝑞(𝑎𝑘) can be any video quality metric (e.g., PSNR and SSIM), and 𝛼and 𝛽are a non-negative penalty weight that ensures the temporal quality smoothness and penalizes the rebuffering delay, respectively.

**Fragmento 6 - p. 3 - score 4:**

Therefore, the control policy of the ABR algorithm can be derived by solving a sequential decision-making problem that optimizes the average chunk QoE for the user under a constrained yet time-varying network throughput: 𝑎∗ 𝑘= arg max 𝑎 1 𝐾 𝐾 𝑘=0 𝑟(𝑠𝑘,𝑎𝑘), (3a) s.t. 𝑠𝑘+1 = 𝑓(𝑠𝑘,𝑎𝑘), 𝑎𝑘∈A, (3b) where the dynamics model 𝑓: S × A →S of the video streaming system includes the buffer occupancy as given in Eq. (1), as well as the dynamics of network throughput which unfortunately cannot be explicitly represented or predicted. As such, we are theoretically unable to find the global optimal solution of Eq. (3), but endeavour in practice to approach as closer as possible to this global optimum. 2.2 Learning How to Learn Bitrate Adaptation As a result, the MDP of an adaptive video streaming system can be formulated as < S, A, 𝑃, 𝑅>, where 𝑃= 𝑝(𝑠𝑘+1|𝑠𝑘,𝑎𝑘) is the state transition probability that mainly depends on the dynamics of network throughput.

**Fragmento 7 - p. 9 - score 4:**

2016. CS2P: Improving Video Bitrate Selection and Adaptation with Data-Driven Throughput Prediction. In Proceedings of the Conference of the ACM Special Interest Group on Data Communication. 272–285. [23] Francis Y. Yan, Hudson Ayers, Chenzhi Zhu, Sadjad Fouladi, James Hong, Keyi Zhang, Philip Levis, and Keith Winstein. 2020. Learning in situ: A Randomized Experiment in Video Streaming. In Proceedings of the 17th USENIX Symposium on Networked Systems Design and Implementation (NSDI 20). 495–511. [24] Xiaoqi Yin, Abhishek Jindal, Vyas Sekar, and Bruno Sinopoli. 2015. A Control- Theoretic Approach for Dynamic Adaptive Video Streaming over HTTP. In Proceedings of the 2015 ACM Conference on Special Interest Group on Data Communication.

**Fragmento 8 - p. 10 - score 4:**

The whole video streaming process can be summarized as follows. At the beginning of video streaming, the video client first obtains the video information, including the number of total video chunks and the available bitrates for corresponding chunks. The client then requests video chunks one by one, using the ABR controller to select the bitrate for future chunks. The requested bitrate version of chunks are downloaded through the video delivery simulator. Once completely downloaded, a video chunk is played back to the client. The playback information, such as buffer occupancy, rebuffering event, bitrate version of the current chunk, is collected to calculate the QoE value during the playback. B ADDITIONAL EXPERIMENTAL RESULTS B.1 Consistency on Out-of-Distribution Traces As with the log-form quality metric 𝑄𝑜𝐸𝑙𝑜𝑔, we compare the consistency of MERINA to other baseline algorithms here, with the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛on in-distribution and out-of- distribution datasets.

**Fragmento 9 - p. 10 - score 4:**

This might be because the linear quality metric produces bigger quality intervals between the bitrate versions than the log-form metric, resulting in a more distinct feature for the bitrate selection. Additionally, Fugu outperforms RobustMPC in terms of the average chunk quality on the two puffer datasets when using the metric 𝑄𝑜𝐸𝑙𝑖𝑛, but performs much worse when using the metric 𝑄𝑜𝐸𝑙𝑜𝑔. B.1.1 Real-World Test for 𝑄𝑜𝐸𝑙𝑖𝑛. With the same settings for 𝑄𝑜𝐸𝑙𝑜𝑔, we evaluate the learning-based algorithms MERINA and Comyco, and the heuristic algorithms BOLA and RobustMPC, by using the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛in the real world platform under three different network conditions: a 4G cellular network, a public WiFi network on campus, and a wide area network connecting Shanghai and Los Angeles, with mean and standard 3015

**Fragmento 10 - p. 11 - score 4:**

This demonstrates that the regularization function facilitates the latent variable’s expressiveness (i.e. a more informative representation) to bitrate selection in mixed dynamics, therefore enhancing the generalization. In addition, without the imitation learning-based pre-training, the learning process of MERINA will be exceedingly unstable, and the training will always fall into a local optimum. This phenomenon may result from the probabilistic latent encoder and the mix dynamics setting in our paper. 3016

**Fragmento 11 - p. 1 - score 3:**

Finally, we implement our algorithm’s meta-training and meta-adaptation procedures under a variety of throughput dynamics. Empirical evaluations on different QoE metrics and multiple datasets containing real-world network traces demonstrate that our algorithm outperforms state-of-the-art ABR algorithms, in terms of the performance on the average chunk QoE, consistency and fast adaptation across a wide range of throughput patterns. CCS CONCEPTS • Information systems →Multimedia streaming; • Comput- ing methodologies →Sequential decision making. KEYWORDS Rate adaptation, meta deep reinforcement learning, generalization. ACM Reference Format: Nuowen Kan, Yuankun Jiang, Chenglin Li, Wenrui Dai, Junni Zou, and Hongkai Xiong.

**Fragmento 12 - p. 2 - score 3:**

Each video chunk is further encoded into multiple quality versions of different bitrates, with the set of available bitrates denoted by A = {𝑎1,𝑎2, · · · ,𝑎𝑀}, where 𝑀represents the total number of bitrate versions. Let 𝑎𝑘∈A denote the bitrate version allocated for the 𝑘-th chunk 𝑈𝑘. Then, once the chunk 𝑈𝑘has been completely downloaded, the buffer occupancy 𝐵𝑘of the video player deployed at the user side can be expressed as: 𝐵𝑘= [(𝐵𝑘−1 −𝑑𝑘)+ + 𝐿], 𝑑𝑘= 𝐸𝑎𝑘/𝐶𝑘, (·)+ ≜max{·, 0}, (1) where 𝐶𝑘is the average network throughput within the duration of downloading chunk𝑈𝑘, 𝐸𝑎𝑘denotes the actual size of𝑈𝑘associated with the selected bitrate version 𝑎𝑘, the term 𝑑𝑘then represents the corresponding time duration spent for downloading chunk 𝑈𝑘.

**Fragmento 13 - p. 3 - score 3:**

Note that the dynamics of network throughput are practically hidden from the agent and independent of the chosen actions, which are typically time-varying and heterogeneous in real world scenarios. Consequently, the state transition probability 𝑃will vary continuously over time and result in a variety of different MDPs, which in essence can be formulated more accurately as a partially observable Markov decision process (POMDP). By denoting the underlying throughput dynamics as a latent variable 𝒛∈𝑍, we can re-formulate the adaptive video streaming problem as a tuple < S, A, 𝑃,𝑍, 𝑅>, where the state space S, action space A and reward space 𝑅remain the same, while the state transition probability changes to 𝑃= 𝑝(𝑠𝑘+1|𝑠𝑘,𝑎𝑘,𝑧𝑘), with 𝑧𝑘representing the throughput dynamics during the duration of downloading chunk 𝑈𝑘.

**Fragmento 14 - p. 4 - score 3:**

Thus, we are unable to sample (𝒄,𝝉) pairs that belong to the same dynamics in Eq. (4), which is different from the typical setting used in most of previous works. We must calculate the expectation in Eq. (4) over trajectories sampled from the mixed dynamics, which complicates the process of meta-policy search for each throughput dynamic. 3.2 Meta-Policy Search on Mixed Dynamics To address the challenge raised by mixed dynamics, we explore the types of policy search methods that can be employed in this situation, and then design a mutual information-based regulariza- tion to make the latent variable more informative about the bitrate selection strategy. The policy network approximates the mapping from the latent variable and the state to an optimal ABR control policy 𝜋𝜃(𝒂|𝒔, 𝒛) : S × 𝑍↦→A.

**Fragmento 15 - p. 4 - score 3:**

In Eq. (5), the mutual information I(𝒂; 𝒛|𝒔) quantifies how much information about 𝒂can be known given 𝒛and 𝒔. In other words, maximizing this regularization entails increasing the diversity of policy when the throughput dynamics are uncertain, as measured by the entropy H (𝒂|𝒔), while making 𝒛more informative about the bitrate selection by minimizing the entropy H (𝒂|𝒛, 𝒔). Additionally, to simplify the computation of 𝜋(𝒂|𝒔), it can be estimated by: 𝜋(𝒂|𝒔) = ∫ 𝜋𝜃(𝒂|𝒔, 𝒛)𝑝(𝒛|𝒔)𝑑𝒛≈ ∫ 𝜋𝜃(𝒂|𝒔, 𝒛)𝑝(𝒛)𝑑𝒛 (6) ≈ 1 𝑁𝑠𝑎 𝑁𝑠𝑎 𝑖=1 𝜋𝜃(𝒂|𝒔, 𝒛𝑖), 𝒛𝑖∼𝑝(𝒛), where 𝑁𝑠𝑎denotes the number of samples from the prior 𝑝(𝒛). With the model-free approach, parameters 𝜙of inference net- work can be optimized via the backward-pass vector ∇𝐽/∇𝒛, i.e., 3009

**Fragmento 16 - p. 5 - score 3:**

, (7) 𝜌(𝜃) = 𝜋𝜃(𝒂|𝒔, 𝒛)/𝜋𝜃′(𝒂|𝒔, 𝒛), 𝒛∼𝑞𝜙(𝒛|𝒄) where𝜃′ denotes the previous values of𝜃following the latest update epoch, clip[𝜌(𝜃), 1 −𝜖, 1 + 𝜖] ensures no incentive for moving 𝜌(𝜃) outside the interval [1−𝜖, 1+𝜖], and ˆ𝐴is the truncated generalized advantage estimation (GAE) function [18] generated from the value function 𝑉𝜃𝑣(𝒔, 𝒛) and 𝒓. Similarly, the critic loss is formulated as: L𝜃𝑣(𝒄,𝝉) = 1 2E¯𝒛  (𝑉𝜃𝑣(𝒔, ¯𝒛) −𝐺𝑘)2 , ¯𝒛∼𝑞𝜙(𝒛|𝒄), (8) where 𝐺𝑘= 𝑟𝑘+ 𝛾𝑟𝑘+1 + 𝛾2𝑟𝑘+2 + · · · is the rollout QoE return of the current state following 𝜋𝜃′(𝒂|𝒔, 𝒛),𝛾∈(0, 1] is a discount factor that attenuates exponentially the impact of future actions over the current expected QoE, and ¯𝒛indicates that gradients are not being computed through it. 4.2 Imitation Learning-Based Pre-Training In practice, due to the low sample efficiency of RL training [15], training the meta-RL from scratch is exceedingly time expensive and unstable in our setting of mixed dynamics. Therefore, we pre-train the parameters 𝜙and 𝜃following the imitation learning method proposed in [7], with a behavior cloning objective for the actor and inference networks: max 𝜃,𝜙 E𝒛, ˆ𝒂log 𝜋𝜃( ˆ𝒂|𝒔, 𝒛), 𝒛∼𝑞𝜙(𝒛|𝒄), ˆ𝒂∼𝜋𝑒(𝒂|𝒔), (9) where the model-based ABR algorithm RobustMPC [24] is adopted to obtain the expert policy 𝜋𝑒(𝒂|𝒔), with the QoE maximized over a horizon of future 3 chunks. Here, we skip the pre-training of critic network, since 𝜃𝑣may be rapidly converged with only a few trials following the policy 𝜋𝜃(𝒂|𝒔, 𝒛). Notably, we employ RobustMPC here primarily for its good QoE performance and low computational complexity, which will be also justified by the experimental evaluations in Section 5. However, variants of MERINA can be easily fulfilled by adopting other existing ABR algorithms to obtain the expert policy, resulting in a difference on the training time and overall QoE performance. In summary, the entire meta-training and meta-adaptation workflow of MERINA is given in Algorithm 1 and Algorithm 2, Algorithm 1 Meta-training Procedure of MERINA Require: Dynamics model 𝑓of the video streaming system with time-varying and heterogeneous network dynamics, learning rates 𝛼1, 𝛼2, 𝛼3 // First stage: pre-training with ex

**Fragmento 17 - p. 6 - score 3:**

5) Fugu [23]: a model- based algorithm that uses NN-based transmission time predictor to predict the probability distribution of download times per bitrate version for future ℎchunks, and optimizes the bitrate selection via calculating the expectation of maximum future ℎ-horizon QoE return. 6) BayesMPC [10]: a model-based algorithm that uses Bayesian NNs to predict the lower bound of future throughputs, based on which a model predictive control is further employed to optimize the future ℎ-horizon QoE return. Note that Fugu is proposed to learn in situ, which is also proposed in [23] and said to be a more sound virtual player than the one employed in our paper. Due to the fact that the simulation platform has little effect on the success of MERINA in terms of generalization, we choose the virtual player that is widely deployed in the majority of prior works.

**Fragmento 18 - p. 6 - score 3:**

1) BOLA [21]: a buffer-based algorithm that uses Lyapunov optimization to determine the optimal bitrate version under the constraint of buffer occupancy only. 2) RobustMPC [24]: a model-based algorithm that solves the optimization problem in Eq. (3) with a horizon of the future ℎ video chunks under the framework of model predictive control. The future throughput is predicted by the harmonic mean of average throughput measurements of the past 5 downloaded chunks. 3) Pensieve [14]: a DRL-based algorithm that uses the A3C algorithm to learn an optimal neural mapping from the dynamics of buffer occupancy, throughput and chunk size to the rate adaptation of the next chunk. 4) Comyco [7, 8]: a model-free neural ABR algorithm that uses NNs to directly approximate the offline near-optimal expert solution by lifelong imitation learning.

**Fragmento 19 - p. 9 - score 3:**

114–118. [18] John Schulman, Philipp Moritz, Sergey Levine, Michael Jordan, and Pieter Abbeel. 2018. High-Dimensional Continuous Control Using Generalized Advantage Estimation. arXiv:1506.02438 [cs.LG] [19] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. 2017. Proximal Policy Optimization Algorithms. arXiv:1707.06347 [cs.LG] [20] I. Sodagar. 2011. The MPEG-DASH Standard for Multimedia Streaming Over the Internet. IEEE MultiMedia 18, 4 (2011), 62–67. [21] Kevin Spiteri, Rahul Urgaonkar, and Ramesh Sitaraman. 2016. BOLA: Near- Optimal Bitrate Adaptation for Online Videos. In Proceedings of the 35th Annual IEEE International Conference on Computer Communications. 1–9. [22] Yi Sun, Xiaoqi Yin, Junchen Jiang, Vyas Sekar, Fuyuan Lin, Nanshu Wang, Tao Liu, and Bruno Sinopoli.

**Fragmento 20 - p. 9 - score 3:**

2017. Model-agnostic meta- learning for fast adaptation of deep networks. In International conference on machine learning. PMLR, 1126–1135. [4] Dash Industry Forum. 2022. Catalyzing the Adoption of MPEG-DASH. https: //dashif.org/ [5] Matteo Gadaleta, Federico Chiariotti, Michele Rossi, and Andrea Zanella. 2017. D-DASH: A Deep Q-Learning Framework for DASH Video Streaming. IEEE Transactions on Cognitive Communications and Networking 3, 4 (2017), 703–718. [6] Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. 2018. Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor. In Proceedings of the 35th International Conference on Machine Learning. 1861–1870. [7] Tianchi Huang, Chao Zhou, Xin Yao, Ruixiao Zhang, Chenglei Wu, Bing Yu, and Lifeng Sun.

**Fragmento 21 - p. 10 - score 3:**

The state of the video streaming system, includes the features as detailed in Section 2, is fed into the input layer of the actor and critic networks. Concretely, for the set of available bitrate versions A, we use a one-dimensional convolution layer with 128 filters, each of size 4 with stride 1, to process them. Meanwhile, five full connected layers with 128 neurons are placed at the input layer to deal with the remaining features of the state, including the measured average throughput 𝐶𝑘−1, time duration 𝑑𝑘−1 during the download of the last video chunk, current buffer occupancy 𝐵𝑘, selected bitrate 𝑎𝑘−1 of the last chunk, and the number of video chunks that have not been downloaded yet. For the latent variable sampled from the posterior 𝑞𝜙(𝒛|𝒄), we also use a fully connected layer with 1280 neurons to process the latent representations.

**Fragmento 22 - p. 1 - score 2:**

In addition, the ABR algorithm in practice is also expected to be able to implement quickly online, because a higher overhead of inference time for rate adaptation will inevitably increase the end-to-end latency. To address this challenge, Yin et al. in [24] argued that the model predictive control (MPC) approach is a natural fit for the rate adaptation problem and proposed two simple yet effective algorithms, namely RobustMPC and FastMPC, based on the pre- diction of future network throughput with the harmonic mean of past throughput. Following this principle, various studies (e.g., CS2P[22], BayesMPC[10], Fugu[23]) have been proposed to seek for a higher QoE by improving the throughput prediction accuracy.

**Fragmento 23 - p. 2 - score 2:**

• We study the generalization problem of adaptive video streaming, and formulate the rate adaptation problem as a POMDP, rather than previously stated MDP. We then propose a model-free system framework based on context-based meta-RL to improve generalization for neural ABR algorithms, by decoupling the inference of throughput dynamics (referred to as latent encoder) from the universal control mechanism that is shared by all poten- tial throughput dynamics (referred to as meta-policy network). • To ensure rapid adaptation to time-varying yet indistinguishable throughput dynamics in real-world scenarios, we propose an efficient meta-policy search scheme for the mixed dynamics, which includes the use of on-policy RL algorithms (or imitation learning) to alleviate estimation bias for value function, and a mutual information-based regularization in the policy loss to make the latent variable more informative about the policy.

**Fragmento 24 - p. 4 - score 2:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. policy-gradient RL or imitation learning. However, the training data contain too many different types of underlying network dynamics to enable an informative latent representation about the policy. To solve this issue, a mutual information-based regularization is further proposed, in addition to the basic loss function. 3.1 Modeling the Uncertainty of Inference To facilitate adaptation, the latent variable 𝒛should encode an effective representation of the current network throughput dy- namics by exploiting a collection of past experienced network throughputs. Here, we define the throughput context as 𝒄𝑘−𝑝:𝑘= {(𝐶𝑘−𝑝,𝑑𝑘−𝑝), · · · , (𝐶𝑘−1,𝑑𝑘−1)}, which consists of the average throughput values and time intervals of throughput measurements collected from the download of chunk 𝑈𝑘−𝑝to chunk 𝑈𝑘−1.

**Fragmento 25 - p. 4 - score 2:**

Besides, modeling the uncertainty enables a stochastic exploration for meta-policy adaptation in response to new environments, hence increasing the sample efficiency of policy search. In the outer expectation of Eq. (4), the replay buffer B contains recent historical experience of environment interaction, including the context 𝒄and the corresponding samples 𝝉= {𝒔, 𝒂, 𝒓}. Due to the fact that the throughput dynamics in real world scenarios are time-varying and heterogeneous, it is infeasible to identify the distinct network throughput dynamics from the environment of adaptive video streaming. In other worlds, in an arbitrary trajectory {(𝒄0:𝑝,𝝉𝑝), · · · , (𝒄𝑘−𝑝:𝑘,𝝉𝑘), · · · } from interacting with the environment, the agent may experience multiple types of throughput dynamics, which we call the mixed dynamics.

**Fragmento 26 - p. 6 - score 2:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. 5 PERFORMANCE EVALUATION Experiment setup. To evaluate the performance in terms of the average chunk QoE, consistency and fast adaptation across a wide range of throughput patterns, we test MERINA on the virtual player as widely used in [1, 7, 8, 10, 14], which simulates the adaptive video streaming process by using the real-world network throughput datasets, in comparison to other ABR algorithms. For the sake of fairness, we also use the same environment settings as in [7, 8, 14]: the available bitrate set is A = {300, 750, 1200, 1850, 2850, 4300} 𝐾𝑏𝑝𝑠, the chunk duration is set as 𝐿= 4 seconds, the buffer occupancy is limited as 1 minute, and the total number of video chunks is 𝐾= 49.


### 7.4. reward qoe objetivo loss

Palabras clave usadas: `reward, QoE, quality of experience, utility, objective, loss, rebuffer, stall, stalling, smoothness, switching, quality variation, bitrate smoothness, video quality, penalty, consistent, consistency, risk, tail, latency`

**Fragmento 1 - p. 3 - score 7:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal as a Markov decision process (MDP), with the state 𝑠𝑘∈S for downloading the chunk 𝑈𝑘represented by six features, namely the measured 1) average throughput 𝐶𝑘−1 and 2) corresponding download time 𝑑𝑘−1, 3) the vector of chunk sizes associated with available bitrate versions for the 𝑘-th video chunk: 𝐸= {𝐸𝑘𝑎1, 𝐸𝑘𝑎2, · · · , 𝐸𝑘𝑎𝑀}, 4) current buffer occupancy 𝐵𝑘−1, 5) selected bitrate 𝑎𝑘−1 of the last video chunk, and 6) the remaining number of video chunks that have not been downloaded yet. To quantify the user’s QoE, we employ a widely used objective metric that incorporates the trade-off between video quality, quality fluctuation and risk of rebuffering events as a linear combination: 𝑟(𝑠𝑘,𝑎𝑘) = 𝑞(𝑎𝑘) −𝛼 𝑞(𝑎𝑘) −𝑞(𝑎𝑘−1)  −𝛽(𝑑𝑘−𝐵𝑘−1)+ , (2) where 𝑟∈𝑅, 𝑞(𝑎𝑘) can be any video quality metric (e.g., PSNR and SSIM), and 𝛼and 𝛽are a non-negative penalty weight that ensures the temporal quality smoothness and penalizes the rebuffering delay, respectively.

**Fragmento 2 - p. 5 - score 5:**

, (7) 𝜌(𝜃) = 𝜋𝜃(𝒂|𝒔, 𝒛)/𝜋𝜃′(𝒂|𝒔, 𝒛), 𝒛∼𝑞𝜙(𝒛|𝒄) where𝜃′ denotes the previous values of𝜃following the latest update epoch, clip[𝜌(𝜃), 1 −𝜖, 1 + 𝜖] ensures no incentive for moving 𝜌(𝜃) outside the interval [1−𝜖, 1+𝜖], and ˆ𝐴is the truncated generalized advantage estimation (GAE) function [18] generated from the value function 𝑉𝜃𝑣(𝒔, 𝒛) and 𝒓. Similarly, the critic loss is formulated as: L𝜃𝑣(𝒄,𝝉) = 1 2E¯𝒛  (𝑉𝜃𝑣(𝒔, ¯𝒛) −𝐺𝑘)2 , ¯𝒛∼𝑞𝜙(𝒛|𝒄), (8) where 𝐺𝑘= 𝑟𝑘+ 𝛾𝑟𝑘+1 + 𝛾2𝑟𝑘+2 + · · · is the rollout QoE return of the current state following 𝜋𝜃′(𝒂|𝒔, 𝒛),𝛾∈(0, 1] is a discount factor that attenuates exponentially the impact of future actions over the current expected QoE, and ¯𝒛indicates that gradients are not being computed through it. 4.2 Imitation Learning-Based Pre-Training In practice, due to the low sample efficiency of RL training [15], training the meta-RL from scratch is exceedingly time expensive and unstable in our setting of mixed dynamics. Therefore, we pre-train the parameters 𝜙and 𝜃following the imitation learning method proposed in [7], with a behavior cloning objective for the actor and inference networks: max 𝜃,𝜙 E𝒛, ˆ𝒂log 𝜋𝜃( ˆ𝒂|𝒔, 𝒛), 𝒛∼𝑞𝜙(𝒛|𝒄), ˆ𝒂∼𝜋𝑒(𝒂|𝒔), (9) where the model-based ABR algorithm RobustMPC [24] is adopted to obtain the expert policy 𝜋𝑒(𝒂|𝒔), with the QoE maximized over a horizon of future 3 chunks. Here, we skip the pre-training of critic network, since 𝜃𝑣may be rapidly converged with only a few trials following the policy 𝜋𝜃(𝒂|𝒔, 𝒛). Notably, we employ RobustMPC here primarily for its good QoE performance and low computational complexity, which will be also justified by the experimental evaluations in Section 5. However, variants of MERINA can be easily fulfilled by adopting other existing ABR algorithms to obtain the expert policy, resulting in a difference on the training time and overall QoE performance. In summary, the entire meta-training and meta-adaptation workflow of MERINA is given in Algorithm 1 and Algorithm 2, Algorithm 1 Meta-training Procedure of MERINA Require: Dynamics model 𝑓of the video streaming system with time-varying and heterogeneous network dynamics, learning rates 𝛼1, 𝛼2, 𝛼3 // First stage: pre-training with ex

**Fragmento 3 - p. 7 - score 5:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal #FUUFS (a) 𝑄𝑜𝐸𝑙𝑖𝑛 #FUUFS (b) 𝑄𝑜𝐸𝑙𝑖𝑛 0 0.2 0.4 0.6 0.8 1 1.2 1.4 Chunk QoE Bitrate utility Rebuffering penalty Smoothness penalty Averagevalue BOLA RobustMPC Pensieve Comyco Fugu BayesMPC MERINA (c) 𝑄𝑜𝐸𝑙𝑖𝑛 #FUUFS (d) 𝑄𝑜𝐸𝑙𝑜𝑔 #FUUFS (e) 𝑄𝑜𝐸𝑙𝑜𝑔 0 0.2 0.4 0.6 0.8 1 1.2 1.4 Chunk QoE Bitrate utility Rebuffering penalty Smoothness penalty Averagevalue BOLA RobustMPC Pensieve Comyco Fugu BayesMPC MERINA (f) 𝑄𝑜𝐸𝑙𝑜𝑔 Figure 2: Performance comparison of different ABR algorithms in terms of the average chunk QoE value and the individual QoE components with the QoE metrics 𝑄𝑜𝐸𝑙𝑖𝑛and 𝑄𝑜𝐸𝑙𝑜𝑔on F&H (FCC and HSDPA) throughput dataset.

**Fragmento 4 - p. 1 - score 4:**

In general, video quality can be enhanced by assigning a higher bitrate for the chunk to be transmitted, which, however, may result in a rebuffering event (i.e., stalling during playback) especially when the network condition is poor and unstable. As a key component of rate adaptation, adaptive bitrate stream- ing (ABR) algorithms aim to solve a stochastic optimal control problem that reveals how to strike an optimal trade-off between maximizing the video quality and avoiding the rebuffering, by determining the fine-grained bitrate combination sequentially for continuously transmitted video chunks. However, due to the time- varying and heterogeneous dynamics of network throughput in real world, it is unfortunately intractable to achieve the optimal trade-off with an explicit solution.

**Fragmento 5 - p. 7 - score 4:**

Furthermore, the bar graphs in Figs. 2(c) and 2(f) indicate that MERINA can surprisingly achieve low rebuffering and smoothness penalties, similar to those of Pensieve. While other algorithms result in either a longer rebuffering time, as Comyco does, or a higher quality fluctuation, as BOLA does, during the video playback. Note that the results obtained for linear QoE metric 𝑄𝑜𝐸𝑙𝑖𝑛are similar to those for log-form QoE metric 𝑄𝑜𝐸𝑙𝑜𝑔w.r.t. all comparison algorithms. Therefore, we only show and compare the performance for 𝑄𝑜𝐸𝑙𝑜𝑔in the following, and move results of 𝑄𝑜𝐸𝑙𝑖𝑛to Appendix B due to page limit. 5.2 Consistency on Out-of-Distribution Traces To study the consistency of MERINA in comparison to other learning-based methods, we measure their performance on out- of-distribution datasets Oboe, Puffer-Oct.17-21 and Puffer-Feb.18- 22 (i.e., with a different distribution of throughput dynamics than F&H dataset) by using the same NN weights obtained in Section 5.1 (i.e., learned from the F&H dataset).

**Fragmento 6 - p. 8 - score 3:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. 0 0.5 1 1.5 2 2.5 3 4G Public WiFi International Link Average value BOLA RobustMPC Comyco MERINA Figure 3: Comparison of 𝑄𝑜𝐸𝑙𝑜𝑔without adaption. NNs to learn the throughput dynamics have a better consistency or generalization than Pensieve and Comyco, though they also perform much worse on Puffer traces than heuristic methods. This demonstrates that, besides meta-RL-based methods, model-based methods are another viable paradigm for addressing the general- ization challenge of adaptive video streaming. In conclusion, our MERINA performs consistently with out-of-distribution throughput dynamics, though it may have a worse QoE than BOLA in some sessions.

**Fragmento 7 - p. 10 - score 3:**

The whole video streaming process can be summarized as follows. At the beginning of video streaming, the video client first obtains the video information, including the number of total video chunks and the available bitrates for corresponding chunks. The client then requests video chunks one by one, using the ABR controller to select the bitrate for future chunks. The requested bitrate version of chunks are downloaded through the video delivery simulator. Once completely downloaded, a video chunk is played back to the client. The playback information, such as buffer occupancy, rebuffering event, bitrate version of the current chunk, is collected to calculate the QoE value during the playback. B ADDITIONAL EXPERIMENTAL RESULTS B.1 Consistency on Out-of-Distribution Traces As with the log-form quality metric 𝑄𝑜𝐸𝑙𝑜𝑔, we compare the consistency of MERINA to other baseline algorithms here, with the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛on in-distribution and out-of- distribution datasets.

**Fragmento 8 - p. 1 - score 2:**

ACM ISBN 978-1-4503-9203-7/22/10...$15.00 https://doi.org/10.1145/3503161.3548331 via Meta Reinforcement Learning. In Proceedings of the 30th ACM Inter- national Conference on Multimedia (MM ’22), October 10–14, 2022, Lisboa, Portugal. ACM, New York, NY, USA, 11 pages. https://doi.org/10.1145/ 3503161.3548331 1 INTRODUCTION Thanks to the emerging trend that watching videos online has become a predominant Internet application, it becomes non- negligible to provide a better quality of experience (QoE) for users in video streaming via rate adaptation techniques. Through online video delivery protocols, such as dynamic adaptive streaming over HTTP (DASH) [20] and HTTP live streaming (HLS) [9], the bitrate, which indicates the quality or compression level for each video chunk (or segment), can be dynamically determined to adapt to the time-varying network throughput and current buffer occupancy of video player.

**Fragmento 9 - p. 1 - score 2:**

Finally, we implement our algorithm’s meta-training and meta-adaptation procedures under a variety of throughput dynamics. Empirical evaluations on different QoE metrics and multiple datasets containing real-world network traces demonstrate that our algorithm outperforms state-of-the-art ABR algorithms, in terms of the performance on the average chunk QoE, consistency and fast adaptation across a wide range of throughput patterns. CCS CONCEPTS • Information systems →Multimedia streaming; • Comput- ing methodologies →Sequential decision making. KEYWORDS Rate adaptation, meta deep reinforcement learning, generalization. ACM Reference Format: Nuowen Kan, Yuankun Jiang, Chenglin Li, Wenrui Dai, Junni Zou, and Hongkai Xiong.

**Fragmento 10 - p. 1 - score 2:**

In addition, the ABR algorithm in practice is also expected to be able to implement quickly online, because a higher overhead of inference time for rate adaptation will inevitably increase the end-to-end latency. To address this challenge, Yin et al. in [24] argued that the model predictive control (MPC) approach is a natural fit for the rate adaptation problem and proposed two simple yet effective algorithms, namely RobustMPC and FastMPC, based on the pre- diction of future network throughput with the harmonic mean of past throughput. Following this principle, various studies (e.g., CS2P[22], BayesMPC[10], Fugu[23]) have been proposed to seek for a higher QoE by improving the throughput prediction accuracy.

**Fragmento 11 - p. 4 - score 2:**

In the following, we will often write 𝒄𝑘−𝑝:𝑘as 𝒄for notational simplicity. Due to the time-varying nature of the underlying network throughput dynamics, we only collect the past experience from the most recent 𝑝chunks, rather than from the beginning of video playback. Additionally, we make the assumption that the true chunk sizes will remain relatively constant throughout all video chunks for each bitrate version, thus omitting the dynamics inference for video content. To approximate the posterior 𝑝(𝒛|𝒄) over latent variable space 𝑍, we build up an inference network that generates the distribution 𝑞𝜙(𝒛|𝒄) parameterized by 𝜙. This inference network can be trained via a model-free manner by using the method described in [16], with the goal of directly maximizing a variational lower bound: E(𝒄,𝝉)∼B  𝐽(𝒄,𝝉) + 𝛽𝐷KL 𝑞𝜙(𝒛|𝒄)||𝑝(𝒛) , (4) where 𝑝(𝒛) is a unit Gaussian prior over 𝑍, and 𝐽(𝒄,𝝉) may be any objective chosen from a variety of those for policy search, with 𝝉= {𝒔, 𝒂, 𝒓} being corresponding samples, as will be detailed in Sections 3.2 and 4.

**Fragmento 12 - p. 5 - score 2:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal ∇𝐽/∇𝜙= ∇𝐽/∇𝒛· ∇𝒛/∇𝜙. Note that we can pass the gradient from the policy network to inference network with the Gaussian re- parameterization trick [11], even though the latent variable input of policy network is sampled from the output of inference network, i.e., 𝒛∼𝑞𝜙(𝒛|𝒄). 4 IMPLEMENTATION 4.1 Meta-Policy Search with DRL To enable an effective policy search, we build up our algorithm on top of the proximal policy optimization (PPO) algorithm [19], a well known on-policy actor-critic method recognized for its reliable performance on policy improvement with trust region policy optimization. With PPO, we construct two networks: an actor network 𝜋𝜃(𝒂|𝒔, 𝒛) and a critic network 𝑉𝜃𝑣(𝒔, 𝒛). We jointly train the inference and actor networks to maximize the actor loss and the regularization I(𝒂; 𝒛|𝒔) on the parameters of 𝜃and 𝜙. As a result, the objective ˜𝐽𝜃(𝒄,𝝉) of the actor network is expressed as: ˜𝐽𝜃(𝒄,𝝉) = E𝒛

**Fragmento 13 - p. 6 - score 2:**

We download all traces on two randomly chosen dates (Oct. 17, 2021 and Feb. 18, 2022), and utilize them as two Puffer datasets with long-tailed throughput dynamics. Additionally, to match with the low video bitrate setting in the experiments, we shrink the throughput values of Puffer into 1/8 of their original values. 5.1 In-Distribution QoE Performance We first evaluate and compare the QoE performance of MERINA with other baselines on the F&H throughput dataset, with the two different QoE metric settings. All throughput traces in the F&H dataset, as used in [7, 8, 14, 24], are randomly split into three partitions: training, validation and test sets. The learning-based methods (MERINA, Pensieve, Comyco, Fugu and BayesMPC) are trained on the training set and evaluated on the validation set.

**Fragmento 14 - p. 6 - score 2:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. 5 PERFORMANCE EVALUATION Experiment setup. To evaluate the performance in terms of the average chunk QoE, consistency and fast adaptation across a wide range of throughput patterns, we test MERINA on the virtual player as widely used in [1, 7, 8, 10, 14], which simulates the adaptive video streaming process by using the real-world network throughput datasets, in comparison to other ABR algorithms. For the sake of fairness, we also use the same environment settings as in [7, 8, 14]: the available bitrate set is A = {300, 750, 1200, 1850, 2850, 4300} 𝐾𝑏𝑝𝑠, the chunk duration is set as 𝐿= 4 seconds, the buffer occupancy is limited as 1 minute, and the total number of video chunks is 𝐾= 49.

**Fragmento 15 - p. 6 - score 2:**

For the QoE metric in Eq. (2), we adopt two widely used settings as in [14, 21, 24]: 1) the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛 with 𝑞(𝑎𝑘) = 𝑎𝑘/1000, 𝛼= 1, 𝛽= 4.3; and 2) the log-form quality metric 𝑄𝑜𝐸𝑙𝑜𝑔with 𝑞(𝑎𝑘) = log(𝑎𝑘/min(A)), 𝛼= 1, 𝛽= 2.66. For the practical implementation of MERINA’s meta-training and meta- adaptation, the discount factor is set as 𝛾= 0.99. The weights of loss function are set as 𝛽= 0.02, 𝜆= 0.15. Also, we let 𝑝= 8,𝜖= 0.04, 𝑁𝑠𝑎= 10, 𝑁update = 650, 𝑁batch = 64, 𝑁𝑢= 2, 𝑁𝑒𝑥𝑝= 256, and set the learning rates as 𝛼1 = 𝛼3 = 10−5, 𝛼2 = 10−4. Our code is available at https://github.com/confiwent/merina. Baseline algorithms. We compare MERINA with the following six state-of-the-art ABR algorithms.

**Fragmento 16 - p. 7 - score 2:**

The results on out-of- distribution datasets (Oboe, Puffer-Oct.17-21 and Puffer-Feb.18- 22) reveal that the NN weights trained in F&H datasets using MERINA provide the highest degree of consistency or generalization performance among the learning-based baselines, over all ranges of varying throughput dynamics. The heuristic ABR algorithms (BOLA and RobustMPC) can always achieve a satisfactory QoE performance on different throughput dynamics, while BOLA beats all the other algorithms on Puffer-Oct.17-21 traces where the throughput dynamics are difficult to predict and considerably deviate from those on the F&H traces. In contrast, the other learning-based methods fail to generalize to the out-of-distribution datasets, verifying the generalization difficulty of DRL or imitation learning-based neural ABR algorithms.

**Fragmento 17 - p. 7 - score 2:**

We show in Table 1 the numerical results that are composed of the average chunk QoE value ± one standard deviation for all the comparison algorithms and the performance gap 𝑅𝑔𝑎𝑝= [(𝑟−𝑟∗)/𝑟∗] × 100% to the value of MERINA, where 𝑟∗is the average chunk QoE of MERINA and 𝑟is the average chunk QoE of each comparison algorithm. Additionally, Table 1 also includes results from the FCC and HSDPA datasets to demonstrate the consistency of all algorithms’ performance on a subset of the training throughput dynamics distribution. The results on FCC and HSDPA traces show that the learning- based baselines perform worse on FCC traces than on HSDPA traces, indicating that training these algorithms on mixed dynamics is unlikely to result in the acquisition of expertise that performs uniformly across all experienced dynamics.

**Fragmento 18 - p. 10 - score 2:**

The NN weights of learning-based algorithms are the same to those used in Section. 5.1 (i.e., learned from the F&H dataset). We also present the numerical results in Table 2 by using the same format. The primary difference between the findings for 𝑄𝑜𝐸𝑙𝑜𝑔and 𝑄𝑜𝐸𝑙𝑖𝑛is that MERINA and Fugu performs better with the metric 𝑄𝑜𝐸𝑙𝑖𝑛than with the metric 𝑄𝑜𝐸𝑙𝑜𝑔on the Puffer-Oct.17-21 dataset. MERINA, in particular, achieves a comparable performance in terms of the average chunk QoE value to BOLA, which also performs best on the Puffer-Oct.17-21 dataset. These results indicate that by using the 𝑄𝑜𝐸𝑙𝑖𝑛quality metric, MERINA presents a generalization capability consistently across all the throughput dynamics in these five datasets, without the requirement of any adaptation.

**Fragmento 19 - p. 11 - score 2:**

The results suggested that, after 1100- epoch adaptation, the proportion of sessions that achieve high QoE value rise significantly. B.3 Ablation Study Finally, we conduct some experiments to demonstrate the benefit to generalization as introduced by the proposed mutual information- based regularization function in Eq. (5), providing a further insight on MERINA. We train a modified version of MERINA, named MERINA (nMI), by setting 𝜆= 0 for the actor loss, on the training dateset F&H, and then evaluate its QoE performance on all the five datasets. The results of average chunk QoE achieved by MERINA (nMI) are also presented in Tables 1 and 2 for 𝑄𝑜𝐸𝑙𝑜𝑔and 𝑄𝑜𝐸𝑙𝑖𝑛, respectively, which reveal a critical finding: the mutual information- based regularizer improves the average QoE performance and generalization on both in- and out-of-distribution datasets.

**Fragmento 20 - p. 2 - score 1:**

Once deployed in environments with different throughput dynamics, the ABR policy can be learned to adapt to corresponding dynamics with only a few trials. However, due to the time-varying yet indistinguishable feature of throughput dynamics, difficulties emerges in meta-policy search on such a mixed dynamics. Therefore, we propose an efficient meta-policy search scheme, which includes using on-policy RL (or imitation learning) algorithms to alleviate the estimation bias of value function, as well as a mutual information-based regularization in the policy loss to make the latent variable more informative about the policy. Finally, we implement our proposed ABR algorithm with a meta-training procedure where a regularized proximal policy optimization (PPO) algorithm is used to train the inference network (encoder) and the latent-conditioned meta- policy by following an imitation learning-based pre-training, and a meta-adaptation procedure that aims to rapidly adapt the meta- policy to unseen throughput dynamics by using the same PPO update.

**Fragmento 21 - p. 2 - score 1:**

• We study the generalization problem of adaptive video streaming, and formulate the rate adaptation problem as a POMDP, rather than previously stated MDP. We then propose a model-free system framework based on context-based meta-RL to improve generalization for neural ABR algorithms, by decoupling the inference of throughput dynamics (referred to as latent encoder) from the universal control mechanism that is shared by all poten- tial throughput dynamics (referred to as meta-policy network). • To ensure rapid adaptation to time-varying yet indistinguishable throughput dynamics in real-world scenarios, we propose an efficient meta-policy search scheme for the mixed dynamics, which includes the use of on-policy RL algorithms (or imitation learning) to alleviate estimation bias for value function, and a mutual information-based regularization in the policy loss to make the latent variable more informative about the policy.

**Fragmento 22 - p. 2 - score 1:**

However, the superior performance of existing neural ABR algo- rithms is subject to certain conditions, such as that the probability of state transition (i.e., 𝒔′ = 𝑓(𝒔, 𝒂) with 𝑓being the dynamics transition function) is identical or similar between the training and deployment environments. This condition is unfortunately not satisfied in many real-world scenarios, possibly resulting in a poor consistency of neural ABR algorithm’s performance across a range of network throughput patterns [1, 10, 13, 23]. Though a lifelong learning method was proposed in [7] to address this issue by continuously fine-tuning the NNs with new throughput data online, it is still not a natural choice for neural ABR algorithms, since NNs trained with certain known dynamics will lose their ability to quickly fit to new dynamics over time [12].

**Fragmento 23 - p. 2 - score 1:**

• We implement MERINA’s meta-training and meta-adaptation procedures, and validate its improved generalization capability through numerous empirical evaluations on different QoE metrics and multiple datasets containing real-world network throughput traces, as well as a real-world test. These evaluations demonstrate that MERINA outperforms the state-of-the-art ABR algorithms in terms of both the average chunk QoE on the in-distribution throughput traces, and the capability of generalization and quick adaptation on the out-of-distribution throughput traces. 2 BACKGROUND AND MOTIVATION 2.1 Problem Formulation In a typical adaptive video streaming system, the video is temporally divided into 𝐾chunks (i.e., segments) with a fixed time duration 𝐿.

**Fragmento 24 - p. 2 - score 1:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. QoE performance without any iterative computation. Specifically, formulated as a Markov decision process (MDP), neural ABR algorithms consider the most recently recorded throughput values and current buffer occupancy as the state 𝒔∈S, the selected bitrate version as the action 𝒂∈A, and directly approximate an optimal rate adaptation policy 𝜋: S →A without the need of learning explicitly the throughput prediction. With this intuition, many efforts have been made to provide users with a (near)-optimal QoE, by exploiting deep reinforcement learning (DRL)-based methods (e.g., Pensieve [14], D-DASH [5]) or imitation learning-based methods (e.g., Comyco [7, 8]).

**Fragmento 25 - p. 2 - score 1:**

Empirically, we compare MERINA to other ABR baselines on different QoE metrics and real-world throughput traces, as well as a 3-hour real-world test. Evaluation results demonstrate that MERINA outperforms state-of-the-art ABR algorithms on the in-distribution traces by at least 3% in terms of average chunk QoE. On three out-of- distribution datasets and real-world test, MERINA beats all neural baselines in terms of the average chunk QoE without adaptation, presenting a performance gain of up to 26% between MERINA and the second-best algorithm, and achieves a higher average chunk QoE over all baselines with only about 200 epochs (i.e., 5 minutes) of adaptation. Our main contributions can be summarized as follows.

**Fragmento 26 - p. 2 - score 1:**

The rebuffering event will occur within the duration of (𝑑𝑘−𝐵𝑘−1)+ if the term 𝐵𝑘−1−𝑑𝑘is negative, i.e., the buffer has no video remaining while the next chunk 𝑈𝑘has not been completely downloaded yet. As conventionally adopted in many learning-based ABR algo- rithms, the adaptive video streaming system can be formulated 3007


### 7.5. entrenamiento optimizacion pipeline

Palabras clave usadas: `training, train, trained, episode, epoch, optimizer, learning rate, loss function, minibatch, clipped, probability ratio, experience, simulation, simulator, emulation, testbed, fine-tuning, pretrain, learning task, meta-training, adaptation, oracle, auto-tuning, offline, online`

**Fragmento 1 - p. 5 - score 6:**

, (7) 𝜌(𝜃) = 𝜋𝜃(𝒂|𝒔, 𝒛)/𝜋𝜃′(𝒂|𝒔, 𝒛), 𝒛∼𝑞𝜙(𝒛|𝒄) where𝜃′ denotes the previous values of𝜃following the latest update epoch, clip[𝜌(𝜃), 1 −𝜖, 1 + 𝜖] ensures no incentive for moving 𝜌(𝜃) outside the interval [1−𝜖, 1+𝜖], and ˆ𝐴is the truncated generalized advantage estimation (GAE) function [18] generated from the value function 𝑉𝜃𝑣(𝒔, 𝒛) and 𝒓. Similarly, the critic loss is formulated as: L𝜃𝑣(𝒄,𝝉) = 1 2E¯𝒛  (𝑉𝜃𝑣(𝒔, ¯𝒛) −𝐺𝑘)2 , ¯𝒛∼𝑞𝜙(𝒛|𝒄), (8) where 𝐺𝑘= 𝑟𝑘+ 𝛾𝑟𝑘+1 + 𝛾2𝑟𝑘+2 + · · · is the rollout QoE return of the current state following 𝜋𝜃′(𝒂|𝒔, 𝒛),𝛾∈(0, 1] is a discount factor that attenuates exponentially the impact of future actions over the current expected QoE, and ¯𝒛indicates that gradients are not being computed through it. 4.2 Imitation Learning-Based Pre-Training In practice, due to the low sample efficiency of RL training [15], training the meta-RL from scratch is exceedingly time expensive and unstable in our setting of mixed dynamics. Therefore, we pre-train the parameters 𝜙and 𝜃following the imitation learning method proposed in [7], with a behavior cloning objective for the actor and inference networks: max 𝜃,𝜙 E𝒛, ˆ𝒂log 𝜋𝜃( ˆ𝒂|𝒔, 𝒛), 𝒛∼𝑞𝜙(𝒛|𝒄), ˆ𝒂∼𝜋𝑒(𝒂|𝒔), (9) where the model-based ABR algorithm RobustMPC [24] is adopted to obtain the expert policy 𝜋𝑒(𝒂|𝒔), with the QoE maximized over a horizon of future 3 chunks. Here, we skip the pre-training of critic network, since 𝜃𝑣may be rapidly converged with only a few trials following the policy 𝜋𝜃(𝒂|𝒔, 𝒛). Notably, we employ RobustMPC here primarily for its good QoE performance and low computational complexity, which will be also justified by the experimental evaluations in Section 5. However, variants of MERINA can be easily fulfilled by adopting other existing ABR algorithms to obtain the expert policy, resulting in a difference on the training time and overall QoE performance. In summary, the entire meta-training and meta-adaptation workflow of MERINA is given in Algorithm 1 and Algorithm 2, Algorithm 1 Meta-training Procedure of MERINA Require: Dynamics model 𝑓of the video streaming system with time-varying and heterogeneous network dynamics, learning rates 𝛼1, 𝛼2, 𝛼3 // First stage: pre-training with ex

**Fragmento 2 - p. 6 - score 6:**

For the QoE metric in Eq. (2), we adopt two widely used settings as in [14, 21, 24]: 1) the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛 with 𝑞(𝑎𝑘) = 𝑎𝑘/1000, 𝛼= 1, 𝛽= 4.3; and 2) the log-form quality metric 𝑄𝑜𝐸𝑙𝑜𝑔with 𝑞(𝑎𝑘) = log(𝑎𝑘/min(A)), 𝛼= 1, 𝛽= 2.66. For the practical implementation of MERINA’s meta-training and meta- adaptation, the discount factor is set as 𝛾= 0.99. The weights of loss function are set as 𝛽= 0.02, 𝜆= 0.15. Also, we let 𝑝= 8,𝜖= 0.04, 𝑁𝑠𝑎= 10, 𝑁update = 650, 𝑁batch = 64, 𝑁𝑢= 2, 𝑁𝑒𝑥𝑝= 256, and set the learning rates as 𝛼1 = 𝛼3 = 10−5, 𝛼2 = 10−4. Our code is available at https://github.com/confiwent/merina. Baseline algorithms. We compare MERINA with the following six state-of-the-art ABR algorithms.

**Fragmento 3 - p. 2 - score 5:**

However, the superior performance of existing neural ABR algo- rithms is subject to certain conditions, such as that the probability of state transition (i.e., 𝒔′ = 𝑓(𝒔, 𝒂) with 𝑓being the dynamics transition function) is identical or similar between the training and deployment environments. This condition is unfortunately not satisfied in many real-world scenarios, possibly resulting in a poor consistency of neural ABR algorithm’s performance across a range of network throughput patterns [1, 10, 13, 23]. Though a lifelong learning method was proposed in [7] to address this issue by continuously fine-tuning the NNs with new throughput data online, it is still not a natural choice for neural ABR algorithms, since NNs trained with certain known dynamics will lose their ability to quickly fit to new dynamics over time [12].

**Fragmento 4 - p. 4 - score 5:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. policy-gradient RL or imitation learning. However, the training data contain too many different types of underlying network dynamics to enable an informative latent representation about the policy. To solve this issue, a mutual information-based regularization is further proposed, in addition to the basic loss function. 3.1 Modeling the Uncertainty of Inference To facilitate adaptation, the latent variable 𝒛should encode an effective representation of the current network throughput dy- namics by exploiting a collection of past experienced network throughputs. Here, we define the throughput context as 𝒄𝑘−𝑝:𝑘= {(𝐶𝑘−𝑝,𝑑𝑘−𝑝), · · · , (𝐶𝑘−1,𝑑𝑘−1)}, which consists of the average throughput values and time intervals of throughput measurements collected from the download of chunk 𝑈𝑘−𝑝to chunk 𝑈𝑘−1.

**Fragmento 5 - p. 8 - score 5:**

In a training epoch, the NN weights are updated twice, while each update is with a batch size of 64 samples. (a) Adaptation Curves #FUUFS (b) Puffer-Oct.17-21 Figure 4: a) The adaptation curves of MERINA and Comyco, and b) average chunk 𝑄𝑜𝐸𝑙𝑜𝑔improvement over RobustMPC. Fig. 4(a) demonstrates that MERINA can outperform RobustMPC with only a few of epochs, and achieve a QoE performance comparable to that of BOLA (performs best in this dataset) with around 200 training epochs (lasting about 10 minutes). To verify the performance further, we show the CDFs of QoE improvement of comparison algorithms over RobustMPC in Fig. 4(b), with MERINA-Offline, MERINA-Adp-30 and MERINA-Adp-200 denoting the proposed algorithm that employs the NN weights without adaptation, after 30-epoch adaptation, and after 200- epoch adaptation, respectively.

**Fragmento 6 - p. 1 - score 4:**

Finally, we implement our algorithm’s meta-training and meta-adaptation procedures under a variety of throughput dynamics. Empirical evaluations on different QoE metrics and multiple datasets containing real-world network traces demonstrate that our algorithm outperforms state-of-the-art ABR algorithms, in terms of the performance on the average chunk QoE, consistency and fast adaptation across a wide range of throughput patterns. CCS CONCEPTS • Information systems →Multimedia streaming; • Comput- ing methodologies →Sequential decision making. KEYWORDS Rate adaptation, meta deep reinforcement learning, generalization. ACM Reference Format: Nuowen Kan, Yuankun Jiang, Chenglin Li, Wenrui Dai, Junni Zou, and Hongkai Xiong.

**Fragmento 7 - p. 2 - score 4:**

Once deployed in environments with different throughput dynamics, the ABR policy can be learned to adapt to corresponding dynamics with only a few trials. However, due to the time-varying yet indistinguishable feature of throughput dynamics, difficulties emerges in meta-policy search on such a mixed dynamics. Therefore, we propose an efficient meta-policy search scheme, which includes using on-policy RL (or imitation learning) algorithms to alleviate the estimation bias of value function, as well as a mutual information-based regularization in the policy loss to make the latent variable more informative about the policy. Finally, we implement our proposed ABR algorithm with a meta-training procedure where a regularized proximal policy optimization (PPO) algorithm is used to train the inference network (encoder) and the latent-conditioned meta- policy by following an imitation learning-based pre-training, and a meta-adaptation procedure that aims to rapidly adapt the meta- policy to unseen throughput dynamics by using the same PPO update.

**Fragmento 8 - p. 2 - score 4:**

• We implement MERINA’s meta-training and meta-adaptation procedures, and validate its improved generalization capability through numerous empirical evaluations on different QoE metrics and multiple datasets containing real-world network throughput traces, as well as a real-world test. These evaluations demonstrate that MERINA outperforms the state-of-the-art ABR algorithms in terms of both the average chunk QoE on the in-distribution throughput traces, and the capability of generalization and quick adaptation on the out-of-distribution throughput traces. 2 BACKGROUND AND MOTIVATION 2.1 Problem Formulation In a typical adaptive video streaming system, the video is temporally divided into 𝐾chunks (i.e., segments) with a fixed time duration 𝐿.

**Fragmento 9 - p. 3 - score 4:**

policy that performs well if the distribution of throughput dynamics has been experienced in the training dataset, but may unfortunately present a very poor generalization in unseen (or out-of-distribution) network contexts. Meta-RL, as a popular method for fast adaptation to unseen environments, trains an agent from multiple sample tasks to construct a meta-policy over the shared structure across tasks [3, 16]. We are therefore motivated to propose MERINA, a context- based meta-RL approach for decoupling inference of underlying network dynamics 𝒛from the universal control mechanism. Other than learning a separate ABR control policy for each possible network throughput dynamic from millions of samples, we would like our ABR agent to discover a common control mechanism (i.e., meta-policy 𝜋(𝒂|𝒔, 𝒛)) shared across a range of possible throughput dynamics during the training.

**Fragmento 10 - p. 8 - score 4:**

6 CONCLUSION We have proposed the meta-RL-based adaptive video streaming system MERINA to learn a generalized ABR algorithm. Specifically, we introduced a model-free context-based system framework, composed of a probabilistic inference network (latent encoder) that inferred the underlying dynamics from the recent throughput context, and a latent-conditioned policy network that learned to rapidly adapt to unfamiliar throughput dynamics. We implemented the meta-training and meta-adaptation procedures for MERINA, and demonstrated its efficiency through empirical evaluations on multiple datasets and a real-world platform. The proposed idea for MERINA is not limited to the throughput dynamics. It, in fact, can be extended to video content (e.g., each video chunk may be encoded with different rate-distortion curves w.r.t.

**Fragmento 11 - p. 8 - score 4:**

The same test video is loaded repeatedly on each network using a randomly chosen ABR scheme. Each experiment takes about 1 hour to complete, and the NNs weights for MERINA and Comyco are all trained on F&H dataset. The results in Fig. 3 illustrates that MERINA performs similarly to RobustMPC, and outperforms BOLA and Comyco on these new network environments. While Comyco performs the worst under public WiFi and international link conditions. 5.3 Fast Adaptation to New Environments Section 5.2 exhibits the satisfactory consistency performance of MERINA when confronted with some unseen throughout dynamics, and reveals that MERINA will degrade performance on traces with dynamics that are significantly different from those in the training dataset.

**Fragmento 12 - p. 11 - score 4:**

It is also seen that MERINA’s performance will degrade after a few update epochs and then improve monotonously. This is because the initial parameters 𝜙and 𝜃may be near a local optimum for the new throughput dynamics, while exploring for a higher value (towards the global optimum) may experience a performance degradation (a) Adaptation Curves #FUUFS (b) Puffer-Oct.17-21 Figure 6: a) The adaptation curves of MERINA and Comyco, and b) average chunk 𝑄𝑜𝐸𝑙𝑖𝑛improvement over RobustMPC. at first and then the performance improvement. Additionally, we show the CDFs of QoE improvement of comparison algorithms over RobustMPC in Fig. 6(b), with MERINA-Offline, MERINA- Adp-100 and MERINA-Adp-1100 denoting the proposed algorithm that employs the NN weights without adaptation, after 100- epoch adaptation (before the performance degradation), and after 1100-epoch adaptation (performance improved again after the degradation), respectively.

**Fragmento 13 - p. 11 - score 4:**

These real-world test for 𝑄𝑜𝐸𝑙𝑖𝑛still can demonstrate the generalization capability of MERINA when deployed in the real-world scenarios. B.2 Fast Adaptation To New Environments Though MERINA performs slightly worse than BOLA in terms of the average chunk QoE value on the throughput dynamics of Puffer-Oct.17-21 when using the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛, we examine here MERINA’s ability to rapidly adapt to this dataset and study how much improvement can be achieved through adaptation. All the settings w.r.t. the meta-adaptation procedures are the same to those of Section 5.3, with the associated results illustrated in Fig. 6. It can be seen from Fig. 6(a) that when using the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛, MERINA can surpass BOLA (0.86) in terms of average chunk QoE value with around 100 training epochs (see MERINA-Adpt) and achieves a much higher chunk QoE value 1.10 asymptotically (see MERINA-Asy).

**Fragmento 14 - p. 11 - score 4:**

The results suggested that, after 1100- epoch adaptation, the proportion of sessions that achieve high QoE value rise significantly. B.3 Ablation Study Finally, we conduct some experiments to demonstrate the benefit to generalization as introduced by the proposed mutual information- based regularization function in Eq. (5), providing a further insight on MERINA. We train a modified version of MERINA, named MERINA (nMI), by setting 𝜆= 0 for the actor loss, on the training dateset F&H, and then evaluate its QoE performance on all the five datasets. The results of average chunk QoE achieved by MERINA (nMI) are also presented in Tables 1 and 2 for 𝑄𝑜𝐸𝑙𝑜𝑔and 𝑄𝑜𝐸𝑙𝑖𝑛, respectively, which reveal a critical finding: the mutual information- based regularizer improves the average QoE performance and generalization on both in- and out-of-distribution datasets.

**Fragmento 15 - p. 1 - score 3:**

ACM ISBN 978-1-4503-9203-7/22/10...$15.00 https://doi.org/10.1145/3503161.3548331 via Meta Reinforcement Learning. In Proceedings of the 30th ACM Inter- national Conference on Multimedia (MM ’22), October 10–14, 2022, Lisboa, Portugal. ACM, New York, NY, USA, 11 pages. https://doi.org/10.1145/ 3503161.3548331 1 INTRODUCTION Thanks to the emerging trend that watching videos online has become a predominant Internet application, it becomes non- negligible to provide a better quality of experience (QoE) for users in video streaming via rate adaptation techniques. Through online video delivery protocols, such as dynamic adaptive streaming over HTTP (DASH) [20] and HTTP live streaming (HLS) [9], the bitrate, which indicates the quality or compression level for each video chunk (or segment), can be dynamically determined to adapt to the time-varying network throughput and current buffer occupancy of video player.

**Fragmento 16 - p. 1 - score 3:**

Specifically, to allow rapid adaptation, we discuss the necessity of detaching the inference of throughput dynamics with the universal control mechanism that is in essence shared by all potential throughput dynamics for neural ABR algorithms. To meta-learn the ABR policy, we then build up a model- free system framework, composed of a probabilistic latent encoder that infers the underlying dynamics from the recent throughput context, and a policy network that is conditioned on latent variable and learns to quickly adapt to new environments. Additionally, to address the difficulties caused by training the policy on mixed dynamics, on-policy RL (or imitation learning) algorithms are suggested for policy training, with a mutual information-based regularization to make the latent variable more informative about the policy.

**Fragmento 17 - p. 3 - score 3:**

Therefore, the control policy of the ABR algorithm can be derived by solving a sequential decision-making problem that optimizes the average chunk QoE for the user under a constrained yet time-varying network throughput: 𝑎∗ 𝑘= arg max 𝑎 1 𝐾 𝐾 𝑘=0 𝑟(𝑠𝑘,𝑎𝑘), (3a) s.t. 𝑠𝑘+1 = 𝑓(𝑠𝑘,𝑎𝑘), 𝑎𝑘∈A, (3b) where the dynamics model 𝑓: S × A →S of the video streaming system includes the buffer occupancy as given in Eq. (1), as well as the dynamics of network throughput which unfortunately cannot be explicitly represented or predicted. As such, we are theoretically unable to find the global optimal solution of Eq. (3), but endeavour in practice to approach as closer as possible to this global optimum. 2.2 Learning How to Learn Bitrate Adaptation As a result, the MDP of an adaptive video streaming system can be formulated as < S, A, 𝑃, 𝑅>, where 𝑃= 𝑝(𝑠𝑘+1|𝑠𝑘,𝑎𝑘) is the state transition probability that mainly depends on the dynamics of network throughput.

**Fragmento 18 - p. 3 - score 3:**

Once learned, this policy is expected to adapt to new throughput dynamics with only a few trials when their necessary latent variable 𝒛is provided. In other words, with MERINA we intend to develop a generalized paradigm for neural ABR algorithms, by learning how to rapidly learn an appropriate ABR policy for each network environment. 3 PROPOSED METHOD The overall system framework of MERINA is illustrated in Fig. 1, comprising two following two key components. • 1) Meta-trained dynamics inference network (i.e., latent encoder). To endow the control policy with an effective represen- tation of current network dynamics, we capture the knowledge about underlying dynamics with a latent probabilistic context variable 𝒛based on recent experience of the current (new) dynamics.

**Fragmento 19 - p. 4 - score 3:**

In the following, we will often write 𝒄𝑘−𝑝:𝑘as 𝒄for notational simplicity. Due to the time-varying nature of the underlying network throughput dynamics, we only collect the past experience from the most recent 𝑝chunks, rather than from the beginning of video playback. Additionally, we make the assumption that the true chunk sizes will remain relatively constant throughout all video chunks for each bitrate version, thus omitting the dynamics inference for video content. To approximate the posterior 𝑝(𝒛|𝒄) over latent variable space 𝑍, we build up an inference network that generates the distribution 𝑞𝜙(𝒛|𝒄) parameterized by 𝜙. This inference network can be trained via a model-free manner by using the method described in [16], with the goal of directly maximizing a variational lower bound: E(𝒄,𝝉)∼B  𝐽(𝒄,𝝉) + 𝛽𝐷KL 𝑞𝜙(𝒛|𝒄)||𝑝(𝒛) , (4) where 𝑝(𝒛) is a unit Gaussian prior over 𝑍, and 𝐽(𝒄,𝝉) may be any objective chosen from a variety of those for policy search, with 𝝉= {𝒔, 𝒂, 𝒓} being corresponding samples, as will be detailed in Sections 3.2 and 4.

**Fragmento 20 - p. 6 - score 3:**

1) BOLA [21]: a buffer-based algorithm that uses Lyapunov optimization to determine the optimal bitrate version under the constraint of buffer occupancy only. 2) RobustMPC [24]: a model-based algorithm that solves the optimization problem in Eq. (3) with a horizon of the future ℎ video chunks under the framework of model predictive control. The future throughput is predicted by the harmonic mean of average throughput measurements of the past 5 downloaded chunks. 3) Pensieve [14]: a DRL-based algorithm that uses the A3C algorithm to learn an optimal neural mapping from the dynamics of buffer occupancy, throughput and chunk size to the rate adaptation of the next chunk. 4) Comyco [7, 8]: a model-free neural ABR algorithm that uses NNs to directly approximate the offline near-optimal expert solution by lifelong imitation learning.

**Fragmento 21 - p. 6 - score 3:**

We download all traces on two randomly chosen dates (Oct. 17, 2021 and Feb. 18, 2022), and utilize them as two Puffer datasets with long-tailed throughput dynamics. Additionally, to match with the low video bitrate setting in the experiments, we shrink the throughput values of Puffer into 1/8 of their original values. 5.1 In-Distribution QoE Performance We first evaluate and compare the QoE performance of MERINA with other baselines on the F&H throughput dataset, with the two different QoE metric settings. All throughput traces in the F&H dataset, as used in [7, 8, 14, 24], are randomly split into three partitions: training, validation and test sets. The learning-based methods (MERINA, Pensieve, Comyco, Fugu and BayesMPC) are trained on the training set and evaluated on the validation set.

**Fragmento 22 - p. 7 - score 3:**

We show in Table 1 the numerical results that are composed of the average chunk QoE value ± one standard deviation for all the comparison algorithms and the performance gap 𝑅𝑔𝑎𝑝= [(𝑟−𝑟∗)/𝑟∗] × 100% to the value of MERINA, where 𝑟∗is the average chunk QoE of MERINA and 𝑟is the average chunk QoE of each comparison algorithm. Additionally, Table 1 also includes results from the FCC and HSDPA datasets to demonstrate the consistency of all algorithms’ performance on a subset of the training throughput dynamics distribution. The results on FCC and HSDPA traces show that the learning- based baselines perform worse on FCC traces than on HSDPA traces, indicating that training these algorithms on mixed dynamics is unlikely to result in the acquisition of expertise that performs uniformly across all experienced dynamics.

**Fragmento 23 - p. 8 - score 3:**

Hence, we examine here MERINA’s ability to rapidly adapt to these unfamiliar throughput dynamics by investigating the performance of meta-adaption procedure given in Algorithm 2. Fig. 4 depicts the performance of an adaptation procedure that seeks to fine-tune the existing NN weights of MERINA and Comyco utilizing traces from Puffer-Oct.17-21 dataset. The test traces of Puffer-Oct.17-21 used in Section 5.2 are also used to assess the performance of comparison algorithms, and the training traces are additional data collected on the same day. Comyco is fine- turned using the suggested lifelong learning method (Comyco- Lifelong) in [7]. We refer to MERINA during the meta-adaptation procedure as MERINA-Adapt, and its asymptotic performance of adaptation (i.e., after converging to the optimum) as MERINA-Asy.

**Fragmento 24 - p. 1 - score 2:**

In addition, the ABR algorithm in practice is also expected to be able to implement quickly online, because a higher overhead of inference time for rate adaptation will inevitably increase the end-to-end latency. To address this challenge, Yin et al. in [24] argued that the model predictive control (MPC) approach is a natural fit for the rate adaptation problem and proposed two simple yet effective algorithms, namely RobustMPC and FastMPC, based on the pre- diction of future network throughput with the harmonic mean of past throughput. Following this principle, various studies (e.g., CS2P[22], BayesMPC[10], Fugu[23]) have been proposed to seek for a higher QoE by improving the throughput prediction accuracy.

**Fragmento 25 - p. 2 - score 2:**

Empirically, we compare MERINA to other ABR baselines on different QoE metrics and real-world throughput traces, as well as a 3-hour real-world test. Evaluation results demonstrate that MERINA outperforms state-of-the-art ABR algorithms on the in-distribution traces by at least 3% in terms of average chunk QoE. On three out-of- distribution datasets and real-world test, MERINA beats all neural baselines in terms of the average chunk QoE without adaptation, presenting a performance gain of up to 26% between MERINA and the second-best algorithm, and achieves a higher average chunk QoE over all baselines with only about 200 epochs (i.e., 5 minutes) of adaptation. Our main contributions can be summarized as follows.

**Fragmento 26 - p. 3 - score 2:**

In the following, we will omit the subscript 𝑘for notational simplicity, i.e., 𝑠𝑘,𝑎𝑘,𝑟𝑘,𝑧𝑘written as 𝒔, 𝒂, 𝒓, 𝒛in places where there is no ambiguity. To the best of our knowledge, most of the previously proposed neural ABR algorithms neglect the variability of transition probabil- ity 𝑃(i.e., under the assumption that the throughput dynamics stay the same over time), thus incorporating the throughput information during download of the past several chunks to the state formulation. The agent trained with such a formulation can learn a universal ABR Video Players Time-varying and heterogeneous throughput dynamics Encoder ࣘ Inference Network (Latent Encoder) contexts l Buffer occupancy latent distribution state Policy Network Meta-Policy st latent Trained by on-policy RL or imitation learning ous bitrate Figure 1: System framework of the proposed MERINA.


### 7.6. datos trazas datasets origen

Palabras clave usadas: `dataset, datasets, trace, traces, network trace, bandwidth trace, real-world, FCC, HSDPA, Norway, LTE, 4G, 5G, WiFi, WLAN, Mahimahi, emulation, testbed, Puffer, data, sessions, users, video, chunk, streaming server`

**Fragmento 1 - p. 11 - score 10:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal Table 2: Performance comparison of different ABR algorithms in terms of the average chunk 𝑄𝑜𝐸𝑙𝑖𝑛value on different datasets. Mean ± std (𝑅𝑔𝑎𝑝) FCC HSDPA Oboe Puffer-Oct.17-21 Puffer-Feb.18-22 BOLA 0.96 ± 0.54 (−20%) 1.12 ± 0.81 (−16%) 1.96 ± 1.03 (−16%) 0.86 ± 1.83 (+1%) 0.66 ± 2.90 (−26%) RobustMPC 0.98 ± 0.75 (−18%) 1.22 ± 1.20 (−9%) 2.30 ± 1.24 (−2%) 0.73 ± 2.16 (−14%) 0.81 ± 2.97 (−9%) Pensieve 1.13 ± 0.65 (−5%) 1.28 ± 0.95 (−5%) 2.26 ± 1.15 (−4%) 0.14 ± 11.55 (−84%) 0.55 ± 8.67 (−44%) Comyco 1.15 ± 0.73 (−3%) 1.34 ± 1.05 (0%) 2.29 ± 1.21 (−2%) −0.13 ± 2.86 (−115%) 0.68 ± 3.06 (−24%) Fugu 1.11 ± 0.70 (−7%) 1.24 ± 1.04 (−7%) 2.31 ± 1.21 (−1%) 0.74 ± 2.13 (−13%) 0.83 ± 2.99 (−7%) BayesMPC 1.10 ± 0.83 (−8%) 1.26 ± 1.11 (−6%) 2.29 ± 1.23 (−2%) 0.33 ± 2.80 (−61%) 0.66 ± 3.34 (−26%) MERINA 1.19 ± 0.67 1.34 ± 0.99 2.34 ± 1.15 0.85 ± 2.02 0.90 ± 2.97 MERINA (nMI with 𝜆= 0) 1.08 ± 0.66 (−9%) 1.22 ± 1.11 (−9%) 2.25 ± 1.19 (−4%) 0.50 ± 2.68 (−61%) 0.72 ± 2.99 (−19%) Dataset distribution 1.13 ± 0.44 Mbps 1.61 ± 0.95 Mbps 2.60 ± 2.08 Mbps 1.85 ± 0.91 Mbps 1.60 ± 0.88 Mbps 0 1 2 3 4 5 4G Public WiFi International Link Average value BOLA RobustMPC Comyco MERINA Figure 5: Comparison of 𝑄𝑜𝐸𝑙𝑖𝑛without adaption.

**Fragmento 2 - p. 6 - score 9:**

Therefore, we re-implement Fugu and utilize it as a baseline ABR algorithm that optimizes the expectation of QoE with a probabilistic download time predictor. Additionally, the planning horizon of RobustMPC, Fugu and BayesMPC is set to ℎ= 3 chunks. Datasets of network throughput. We collect four public real- world network throughput datasets (3G/HSDPA [17], FCC [2], Oboe [1], Puffer [23]) to simulate various user and network conditions. The mean and standard deviation values of these datasets are listed in bottom row of Table 1. We combine the similar datasets FCC and 3G/HSDPA into one dataset (named F&H), which is then used to validate the in-distribution performance of different ABR algorithms. Note that the datasets 3G/HSDPA, FCC and Oboe contain only a small amount of traces, but the throughput data of Puffer is updated daily (data of a single day takes up to several GB) and has been regularly updated since January 2019.

**Fragmento 3 - p. 1 - score 8:**

Finally, we implement our algorithm’s meta-training and meta-adaptation procedures under a variety of throughput dynamics. Empirical evaluations on different QoE metrics and multiple datasets containing real-world network traces demonstrate that our algorithm outperforms state-of-the-art ABR algorithms, in terms of the performance on the average chunk QoE, consistency and fast adaptation across a wide range of throughput patterns. CCS CONCEPTS • Information systems →Multimedia streaming; • Comput- ing methodologies →Sequential decision making. KEYWORDS Rate adaptation, meta deep reinforcement learning, generalization. ACM Reference Format: Nuowen Kan, Yuankun Jiang, Chenglin Li, Wenrui Dai, Junni Zou, and Hongkai Xiong.

**Fragmento 4 - p. 2 - score 8:**

• We implement MERINA’s meta-training and meta-adaptation procedures, and validate its improved generalization capability through numerous empirical evaluations on different QoE metrics and multiple datasets containing real-world network throughput traces, as well as a real-world test. These evaluations demonstrate that MERINA outperforms the state-of-the-art ABR algorithms in terms of both the average chunk QoE on the in-distribution throughput traces, and the capability of generalization and quick adaptation on the out-of-distribution throughput traces. 2 BACKGROUND AND MOTIVATION 2.1 Problem Formulation In a typical adaptive video streaming system, the video is temporally divided into 𝐾chunks (i.e., segments) with a fixed time duration 𝐿.

**Fragmento 5 - p. 7 - score 8:**

We show in Table 1 the numerical results that are composed of the average chunk QoE value ± one standard deviation for all the comparison algorithms and the performance gap 𝑅𝑔𝑎𝑝= [(𝑟−𝑟∗)/𝑟∗] × 100% to the value of MERINA, where 𝑟∗is the average chunk QoE of MERINA and 𝑟is the average chunk QoE of each comparison algorithm. Additionally, Table 1 also includes results from the FCC and HSDPA datasets to demonstrate the consistency of all algorithms’ performance on a subset of the training throughput dynamics distribution. The results on FCC and HSDPA traces show that the learning- based baselines perform worse on FCC traces than on HSDPA traces, indicating that training these algorithms on mixed dynamics is unlikely to result in the acquisition of expertise that performs uniformly across all experienced dynamics.

**Fragmento 6 - p. 10 - score 8:**

This might be because the linear quality metric produces bigger quality intervals between the bitrate versions than the log-form metric, resulting in a more distinct feature for the bitrate selection. Additionally, Fugu outperforms RobustMPC in terms of the average chunk quality on the two puffer datasets when using the metric 𝑄𝑜𝐸𝑙𝑖𝑛, but performs much worse when using the metric 𝑄𝑜𝐸𝑙𝑜𝑔. B.1.1 Real-World Test for 𝑄𝑜𝐸𝑙𝑖𝑛. With the same settings for 𝑄𝑜𝐸𝑙𝑜𝑔, we evaluate the learning-based algorithms MERINA and Comyco, and the heuristic algorithms BOLA and RobustMPC, by using the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛in the real world platform under three different network conditions: a 4G cellular network, a public WiFi network on campus, and a wide area network connecting Shanghai and Los Angeles, with mean and standard 3015

**Fragmento 7 - p. 2 - score 7:**

Empirically, we compare MERINA to other ABR baselines on different QoE metrics and real-world throughput traces, as well as a 3-hour real-world test. Evaluation results demonstrate that MERINA outperforms state-of-the-art ABR algorithms on the in-distribution traces by at least 3% in terms of average chunk QoE. On three out-of- distribution datasets and real-world test, MERINA beats all neural baselines in terms of the average chunk QoE without adaptation, presenting a performance gain of up to 26% between MERINA and the second-best algorithm, and achieves a higher average chunk QoE over all baselines with only about 200 epochs (i.e., 5 minutes) of adaptation. Our main contributions can be summarized as follows.

**Fragmento 8 - p. 6 - score 7:**

We download all traces on two randomly chosen dates (Oct. 17, 2021 and Feb. 18, 2022), and utilize them as two Puffer datasets with long-tailed throughput dynamics. Additionally, to match with the low video bitrate setting in the experiments, we shrink the throughput values of Puffer into 1/8 of their original values. 5.1 In-Distribution QoE Performance We first evaluate and compare the QoE performance of MERINA with other baselines on the F&H throughput dataset, with the two different QoE metric settings. All throughput traces in the F&H dataset, as used in [7, 8, 14, 24], are randomly split into three partitions: training, validation and test sets. The learning-based methods (MERINA, Pensieve, Comyco, Fugu and BayesMPC) are trained on the training set and evaluated on the validation set.

**Fragmento 9 - p. 7 - score 7:**

Table 1: Performance comparison of different ABR algorithms in terms of the average chunk 𝑄𝑜𝐸𝑙𝑜𝑔value on different datasets. Mean ± std (𝑅𝑔𝑎𝑝) FCC HSDPA Oboe Puffer-Oct.17-21 Puffer-Feb.18-22 BOLA 0.95 ± 0.63 (−17%) 1.11 ± 0.64 (−9%) 1.63 ± 0.66 (−11%) 0.88 ± 1.29 (+20%) 0.75 ± 1.93 (−14%) RobustMPC 1.05 ± 0.63 (−8%) 1.16 ± 0.85 (−5%) 1.79 ± 0.73 (−2%) 0.76 ± 1.48 (+5%) 0.86 ± 2.01 (−2%) Pensieve 1.07 ± 0.62 (−7%) 1.21 ± 0.68 (−1%) 1.75 ± 0.69 (−4%) 0.40 ± 7.17 (−46%) 0.66 ± 5.40 (−25%) Comyco 1.11 ± 0.63 (−3%) 1.22 ± 0.78 (−0%) 1.76 ± 0.77 (−3%) −0.22 ± 2.20 (−130%) 0.65 ± 2.25 (−26%) Fugu 1.04 ± 0.70 (−10%) 1.16 ± 0.80 (−5%) 1.71 ± 0.78 (−6%) 0.54 ± 1.55 (−26%) 0.77 ± 1.94 (−12%) BayesMPC 1.05 ± 0.78 (−9%) 1.09 ± 0.84 (−2%) 1.78 ± 0.74 (−2%) 0.54 ± 1.88 (−26%) 0.76 ± 2.20 (−14%) MARINA 1.15 ± 0.66 1.22 ± 0.85 1.82 ± 0.70 0.73 ± 1.63 0.88 ± 2.00 MERINA (nMI with 𝜆= 0, see Appendix B.3) 1.05 ± 0.65 (−9%) 1.19 ± 0.71 (−2%) 1.74 ± 0.69 (−4%) 0.71 ± 1.58 (−2%) 0.83 ± 1.96 (−5%) Dataset distribution 1.13 ± 0.44 Mbps 1.61 ± 0.95 Mbps 2.60 ± 2.08 Mbps 1.85 ± 0.91 Mbps 1.60 ± 0.88 Mbps is just 0.3 less than RobustMPC’s.

**Fragmento 10 - p. 7 - score 7:**

Furthermore, the bar graphs in Figs. 2(c) and 2(f) indicate that MERINA can surprisingly achieve low rebuffering and smoothness penalties, similar to those of Pensieve. While other algorithms result in either a longer rebuffering time, as Comyco does, or a higher quality fluctuation, as BOLA does, during the video playback. Note that the results obtained for linear QoE metric 𝑄𝑜𝐸𝑙𝑖𝑛are similar to those for log-form QoE metric 𝑄𝑜𝐸𝑙𝑜𝑔w.r.t. all comparison algorithms. Therefore, we only show and compare the performance for 𝑄𝑜𝐸𝑙𝑜𝑔in the following, and move results of 𝑄𝑜𝐸𝑙𝑖𝑛to Appendix B due to page limit. 5.2 Consistency on Out-of-Distribution Traces To study the consistency of MERINA in comparison to other learning-based methods, we measure their performance on out- of-distribution datasets Oboe, Puffer-Oct.17-21 and Puffer-Feb.18- 22 (i.e., with a different distribution of throughput dynamics than F&H dataset) by using the same NN weights obtained in Section 5.1 (i.e., learned from the F&H dataset).

**Fragmento 11 - p. 8 - score 7:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. 0 0.5 1 1.5 2 2.5 3 4G Public WiFi International Link Average value BOLA RobustMPC Comyco MERINA Figure 3: Comparison of 𝑄𝑜𝐸𝑙𝑜𝑔without adaption. NNs to learn the throughput dynamics have a better consistency or generalization than Pensieve and Comyco, though they also perform much worse on Puffer traces than heuristic methods. This demonstrates that, besides meta-RL-based methods, model-based methods are another viable paradigm for addressing the general- ization challenge of adaptive video streaming. In conclusion, our MERINA performs consistently with out-of-distribution throughput dynamics, though it may have a worse QoE than BOLA in some sessions.

**Fragmento 12 - p. 10 - score 7:**

The whole video streaming process can be summarized as follows. At the beginning of video streaming, the video client first obtains the video information, including the number of total video chunks and the available bitrates for corresponding chunks. The client then requests video chunks one by one, using the ABR controller to select the bitrate for future chunks. The requested bitrate version of chunks are downloaded through the video delivery simulator. Once completely downloaded, a video chunk is played back to the client. The playback information, such as buffer occupancy, rebuffering event, bitrate version of the current chunk, is collected to calculate the QoE value during the playback. B ADDITIONAL EXPERIMENTAL RESULTS B.1 Consistency on Out-of-Distribution Traces As with the log-form quality metric 𝑄𝑜𝐸𝑙𝑜𝑔, we compare the consistency of MERINA to other baseline algorithms here, with the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛on in-distribution and out-of- distribution datasets.

**Fragmento 13 - p. 11 - score 7:**

deviation of recorded throughput values of 4.52 ± 0.74𝑀𝑏𝑝𝑠, 2.52 ± 1.06𝑀𝑏𝑝𝑠and 1.63 ± 1.16𝑀𝑏𝑝𝑠. The same test video is loaded repeatedly on each network using a randomly chosen ABR scheme. Each experiment takes about 1 hour to complete, and the NNs weights for MERINA and Comyco are all trained on the F&H dataset. Fig. 5 illustrates the real-world results of four comparison algorithms without adaptation on these three scenarios. It can be seen that MERINA surpasses the other baseline algorithms on the public WiFi and international link conditions, but performs slightly worse than Comyco under 4G condition. Comyco, on the other hand, achieves the highest average chunk QoE value under 4G conditions, but performs poorly under public WiFi and international link conditions.

**Fragmento 14 - p. 6 - score 6:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. 5 PERFORMANCE EVALUATION Experiment setup. To evaluate the performance in terms of the average chunk QoE, consistency and fast adaptation across a wide range of throughput patterns, we test MERINA on the virtual player as widely used in [1, 7, 8, 10, 14], which simulates the adaptive video streaming process by using the real-world network throughput datasets, in comparison to other ABR algorithms. For the sake of fairness, we also use the same environment settings as in [7, 8, 14]: the available bitrate set is A = {300, 750, 1200, 1850, 2850, 4300} 𝐾𝑏𝑝𝑠, the chunk duration is set as 𝐿= 4 seconds, the buffer occupancy is limited as 1 minute, and the total number of video chunks is 𝐾= 49.

**Fragmento 15 - p. 7 - score 6:**

The results on out-of- distribution datasets (Oboe, Puffer-Oct.17-21 and Puffer-Feb.18- 22) reveal that the NN weights trained in F&H datasets using MERINA provide the highest degree of consistency or generalization performance among the learning-based baselines, over all ranges of varying throughput dynamics. The heuristic ABR algorithms (BOLA and RobustMPC) can always achieve a satisfactory QoE performance on different throughput dynamics, while BOLA beats all the other algorithms on Puffer-Oct.17-21 traces where the throughput dynamics are difficult to predict and considerably deviate from those on the F&H traces. In contrast, the other learning-based methods fail to generalize to the out-of-distribution datasets, verifying the generalization difficulty of DRL or imitation learning-based neural ABR algorithms.

**Fragmento 16 - p. 7 - score 6:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal #FUUFS (a) 𝑄𝑜𝐸𝑙𝑖𝑛 #FUUFS (b) 𝑄𝑜𝐸𝑙𝑖𝑛 0 0.2 0.4 0.6 0.8 1 1.2 1.4 Chunk QoE Bitrate utility Rebuffering penalty Smoothness penalty Averagevalue BOLA RobustMPC Pensieve Comyco Fugu BayesMPC MERINA (c) 𝑄𝑜𝐸𝑙𝑖𝑛 #FUUFS (d) 𝑄𝑜𝐸𝑙𝑜𝑔 #FUUFS (e) 𝑄𝑜𝐸𝑙𝑜𝑔 0 0.2 0.4 0.6 0.8 1 1.2 1.4 Chunk QoE Bitrate utility Rebuffering penalty Smoothness penalty Averagevalue BOLA RobustMPC Pensieve Comyco Fugu BayesMPC MERINA (f) 𝑄𝑜𝐸𝑙𝑜𝑔 Figure 2: Performance comparison of different ABR algorithms in terms of the average chunk QoE value and the individual QoE components with the QoE metrics 𝑄𝑜𝐸𝑙𝑖𝑛and 𝑄𝑜𝐸𝑙𝑜𝑔on F&H (FCC and HSDPA) throughput dataset.

**Fragmento 17 - p. 8 - score 6:**

6 CONCLUSION We have proposed the meta-RL-based adaptive video streaming system MERINA to learn a generalized ABR algorithm. Specifically, we introduced a model-free context-based system framework, composed of a probabilistic inference network (latent encoder) that inferred the underlying dynamics from the recent throughput context, and a latent-conditioned policy network that learned to rapidly adapt to unfamiliar throughput dynamics. We implemented the meta-training and meta-adaptation procedures for MERINA, and demonstrated its efficiency through empirical evaluations on multiple datasets and a real-world platform. The proposed idea for MERINA is not limited to the throughput dynamics. It, in fact, can be extended to video content (e.g., each video chunk may be encoded with different rate-distortion curves w.r.t.

**Fragmento 18 - p. 6 - score 5:**

By choosing the NNs weights that perform best on the validation set, the performance of all comparison algorithms is then tested on the test set. Note that the QoE performance may slightly vary with the random traces selection and unstable NNs training, so it is natural to notice some discrepancies between earlier works and ours. We simulate the playback of the same video once for each throughput trace (referred to as a session), and then collect QoE values of all chunks for comparison. Since the test and training sets share the same distribution of throughout traces, we call the results in-distribution QoE performance. Figs. 2(a) and 2(d) depict the cumulative distribution functions (CDFs) of all sessions’ average QoE for all algorithms.

**Fragmento 19 - p. 7 - score 5:**

Concretely, the model-free neural algorithms (e.g., Pensieve and Comyco) suffer from retaining their capability on Oboe traces while degrading significantly on Puffer traces, particularly on the Puffer-Oct.17-21 dataset. While the model-based algorithms (e.g., Fugu and BayesMPC) that use 3012

**Fragmento 20 - p. 8 - score 5:**

Hence, we examine here MERINA’s ability to rapidly adapt to these unfamiliar throughput dynamics by investigating the performance of meta-adaption procedure given in Algorithm 2. Fig. 4 depicts the performance of an adaptation procedure that seeks to fine-tune the existing NN weights of MERINA and Comyco utilizing traces from Puffer-Oct.17-21 dataset. The test traces of Puffer-Oct.17-21 used in Section 5.2 are also used to assess the performance of comparison algorithms, and the training traces are additional data collected on the same day. Comyco is fine- turned using the suggested lifelong learning method (Comyco- Lifelong) in [7]. We refer to MERINA during the meta-adaptation procedure as MERINA-Adapt, and its asymptotic performance of adaptation (i.e., after converging to the optimum) as MERINA-Asy.

**Fragmento 21 - p. 10 - score 5:**

The NN weights of learning-based algorithms are the same to those used in Section. 5.1 (i.e., learned from the F&H dataset). We also present the numerical results in Table 2 by using the same format. The primary difference between the findings for 𝑄𝑜𝐸𝑙𝑜𝑔and 𝑄𝑜𝐸𝑙𝑖𝑛is that MERINA and Fugu performs better with the metric 𝑄𝑜𝐸𝑙𝑖𝑛than with the metric 𝑄𝑜𝐸𝑙𝑜𝑔on the Puffer-Oct.17-21 dataset. MERINA, in particular, achieves a comparable performance in terms of the average chunk QoE value to BOLA, which also performs best on the Puffer-Oct.17-21 dataset. These results indicate that by using the 𝑄𝑜𝐸𝑙𝑖𝑛quality metric, MERINA presents a generalization capability consistently across all the throughput dynamics in these five datasets, without the requirement of any adaptation.

**Fragmento 22 - p. 10 - score 5:**

A.3 Virtual Player The virtual player, with reference to the open-sourced ABR simula- tor used by Pensieve and Comyco, includes three key components: 1) a video client that emulates the video playback and the buffer oc- cupancy; 2) a video delivery simulator that emulates the download of available video chunks from the video server to the client, under network conditions that are emulated from our stated datasets of network throughput, along with an 80 ms RTT and a packet loss rate of 0.95; and 3) an ABR controller that employs the ABR algorithms (e.g., MERINA and other baseline algorithms) to decide the rule of which bitrate version being requested for the next requested video chunk that has not been downloaded yet.

**Fragmento 23 - p. 11 - score 5:**

These real-world test for 𝑄𝑜𝐸𝑙𝑖𝑛still can demonstrate the generalization capability of MERINA when deployed in the real-world scenarios. B.2 Fast Adaptation To New Environments Though MERINA performs slightly worse than BOLA in terms of the average chunk QoE value on the throughput dynamics of Puffer-Oct.17-21 when using the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛, we examine here MERINA’s ability to rapidly adapt to this dataset and study how much improvement can be achieved through adaptation. All the settings w.r.t. the meta-adaptation procedures are the same to those of Section 5.3, with the associated results illustrated in Fig. 6. It can be seen from Fig. 6(a) that when using the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛, MERINA can surpass BOLA (0.86) in terms of average chunk QoE value with around 100 training epochs (see MERINA-Adpt) and achieves a much higher chunk QoE value 1.10 asymptotically (see MERINA-Asy).

**Fragmento 24 - p. 11 - score 5:**

The results suggested that, after 1100- epoch adaptation, the proportion of sessions that achieve high QoE value rise significantly. B.3 Ablation Study Finally, we conduct some experiments to demonstrate the benefit to generalization as introduced by the proposed mutual information- based regularization function in Eq. (5), providing a further insight on MERINA. We train a modified version of MERINA, named MERINA (nMI), by setting 𝜆= 0 for the actor loss, on the training dateset F&H, and then evaluate its QoE performance on all the five datasets. The results of average chunk QoE achieved by MERINA (nMI) are also presented in Tables 1 and 2 for 𝑄𝑜𝐸𝑙𝑜𝑔and 𝑄𝑜𝐸𝑙𝑖𝑛, respectively, which reveal a critical finding: the mutual information- based regularizer improves the average QoE performance and generalization on both in- and out-of-distribution datasets.

**Fragmento 25 - p. 6 - score 4:**

The CDFs in Figs. 2(b) and 2(e) illustrate the QoE improvements of the other algorithms over RobustMPC in all sessions. And the bar graphs in Figs. 2(c) and 2(f) show the average chunk QoE and each individual components in Eq. (2), where the error bars span ± one standard deviation from the average value. The key observation is that MERINA outperforms the other baseline algorithms in terms of the average chunk QoE value with both the linear and log-form QoE metrics on the F&H throughput dataset. The performance gap of the average chunk QoE between MERINA and the baseline algorithms is at least 3% and 4% for 𝑄𝑜𝐸𝑙𝑖𝑛and 𝑄𝑜𝐸𝑙𝑜𝑔, respectively. And Comyco beats the remaining baseline algorithms in terms of QoE (slightly better than Pensieve), demonstrating the effectiveness of imitation learning.

**Fragmento 26 - p. 8 - score 4:**

In a training epoch, the NN weights are updated twice, while each update is with a batch size of 64 samples. (a) Adaptation Curves #FUUFS (b) Puffer-Oct.17-21 Figure 4: a) The adaptation curves of MERINA and Comyco, and b) average chunk 𝑄𝑜𝐸𝑙𝑜𝑔improvement over RobustMPC. Fig. 4(a) demonstrates that MERINA can outperform RobustMPC with only a few of epochs, and achieve a QoE performance comparable to that of BOLA (performs best in this dataset) with around 200 training epochs (lasting about 10 minutes). To verify the performance further, we show the CDFs of QoE improvement of comparison algorithms over RobustMPC in Fig. 4(b), with MERINA-Offline, MERINA-Adp-30 and MERINA-Adp-200 denoting the proposed algorithm that employs the NN weights without adaptation, after 30-epoch adaptation, and after 200- epoch adaptation, respectively.


### 7.7. evaluacion baselines experimentos

Palabras clave usadas: `evaluation, experiment, experiments, baseline, baselines, compare, comparison, Pensieve, BBA, BOLA, MPC, RobustMPC, FastMPC, A3C, PPO, DQN, SODA, Oboe, MetaABR, results, outperform, ablation, scenario, test`

**Fragmento 1 - p. 6 - score 8:**

We download all traces on two randomly chosen dates (Oct. 17, 2021 and Feb. 18, 2022), and utilize them as two Puffer datasets with long-tailed throughput dynamics. Additionally, to match with the low video bitrate setting in the experiments, we shrink the throughput values of Puffer into 1/8 of their original values. 5.1 In-Distribution QoE Performance We first evaluate and compare the QoE performance of MERINA with other baselines on the F&H throughput dataset, with the two different QoE metric settings. All throughput traces in the F&H dataset, as used in [7, 8, 14, 24], are randomly split into three partitions: training, validation and test sets. The learning-based methods (MERINA, Pensieve, Comyco, Fugu and BayesMPC) are trained on the training set and evaluated on the validation set.

**Fragmento 2 - p. 8 - score 8:**

The results indicate that after 30-epoch adaptation, the proportion of sessions that achieve much lower/higher QoE value than RobustMPC significantly decreases/increases. And after 200-epochs adaptation, MERINA has a similar distribution to BOLA, in terms of average QoE improvement. While Comyco’s performance cannot be improved rapidly due to its low initial performance, and also because the lifelong learning method cannot ensure policy improvement in a significantly changed environment. The asymptotic performance of MERINA indicates that it can achieve a superior QoE performance when compared to all baselines following a meta-adaptation pro- cedure, implying that MERINA can achieve the best generalization performance and will outperform baseline algorithms across a range of throughput dynamics through the adaptation.

**Fragmento 3 - p. 2 - score 7:**

Empirically, we compare MERINA to other ABR baselines on different QoE metrics and real-world throughput traces, as well as a 3-hour real-world test. Evaluation results demonstrate that MERINA outperforms state-of-the-art ABR algorithms on the in-distribution traces by at least 3% in terms of average chunk QoE. On three out-of- distribution datasets and real-world test, MERINA beats all neural baselines in terms of the average chunk QoE without adaptation, presenting a performance gain of up to 26% between MERINA and the second-best algorithm, and achieves a higher average chunk QoE over all baselines with only about 200 epochs (i.e., 5 minutes) of adaptation. Our main contributions can be summarized as follows.

**Fragmento 4 - p. 5 - score 7:**

, (7) 𝜌(𝜃) = 𝜋𝜃(𝒂|𝒔, 𝒛)/𝜋𝜃′(𝒂|𝒔, 𝒛), 𝒛∼𝑞𝜙(𝒛|𝒄) where𝜃′ denotes the previous values of𝜃following the latest update epoch, clip[𝜌(𝜃), 1 −𝜖, 1 + 𝜖] ensures no incentive for moving 𝜌(𝜃) outside the interval [1−𝜖, 1+𝜖], and ˆ𝐴is the truncated generalized advantage estimation (GAE) function [18] generated from the value function 𝑉𝜃𝑣(𝒔, 𝒛) and 𝒓. Similarly, the critic loss is formulated as: L𝜃𝑣(𝒄,𝝉) = 1 2E¯𝒛  (𝑉𝜃𝑣(𝒔, ¯𝒛) −𝐺𝑘)2 , ¯𝒛∼𝑞𝜙(𝒛|𝒄), (8) where 𝐺𝑘= 𝑟𝑘+ 𝛾𝑟𝑘+1 + 𝛾2𝑟𝑘+2 + · · · is the rollout QoE return of the current state following 𝜋𝜃′(𝒂|𝒔, 𝒛),𝛾∈(0, 1] is a discount factor that attenuates exponentially the impact of future actions over the current expected QoE, and ¯𝒛indicates that gradients are not being computed through it. 4.2 Imitation Learning-Based Pre-Training In practice, due to the low sample efficiency of RL training [15], training the meta-RL from scratch is exceedingly time expensive and unstable in our setting of mixed dynamics. Therefore, we pre-train the parameters 𝜙and 𝜃following the imitation learning method proposed in [7], with a behavior cloning objective for the actor and inference networks: max 𝜃,𝜙 E𝒛, ˆ𝒂log 𝜋𝜃( ˆ𝒂|𝒔, 𝒛), 𝒛∼𝑞𝜙(𝒛|𝒄), ˆ𝒂∼𝜋𝑒(𝒂|𝒔), (9) where the model-based ABR algorithm RobustMPC [24] is adopted to obtain the expert policy 𝜋𝑒(𝒂|𝒔), with the QoE maximized over a horizon of future 3 chunks. Here, we skip the pre-training of critic network, since 𝜃𝑣may be rapidly converged with only a few trials following the policy 𝜋𝜃(𝒂|𝒔, 𝒛). Notably, we employ RobustMPC here primarily for its good QoE performance and low computational complexity, which will be also justified by the experimental evaluations in Section 5. However, variants of MERINA can be easily fulfilled by adopting other existing ABR algorithms to obtain the expert policy, resulting in a difference on the training time and overall QoE performance. In summary, the entire meta-training and meta-adaptation workflow of MERINA is given in Algorithm 1 and Algorithm 2, Algorithm 1 Meta-training Procedure of MERINA Require: Dynamics model 𝑓of the video streaming system with time-varying and heterogeneous network dynamics, learning rates 𝛼1, 𝛼2, 𝛼3 // First stage: pre-training with ex

**Fragmento 5 - p. 7 - score 7:**

The results on out-of- distribution datasets (Oboe, Puffer-Oct.17-21 and Puffer-Feb.18- 22) reveal that the NN weights trained in F&H datasets using MERINA provide the highest degree of consistency or generalization performance among the learning-based baselines, over all ranges of varying throughput dynamics. The heuristic ABR algorithms (BOLA and RobustMPC) can always achieve a satisfactory QoE performance on different throughput dynamics, while BOLA beats all the other algorithms on Puffer-Oct.17-21 traces where the throughput dynamics are difficult to predict and considerably deviate from those on the F&H traces. In contrast, the other learning-based methods fail to generalize to the out-of-distribution datasets, verifying the generalization difficulty of DRL or imitation learning-based neural ABR algorithms.

**Fragmento 6 - p. 8 - score 7:**

The same test video is loaded repeatedly on each network using a randomly chosen ABR scheme. Each experiment takes about 1 hour to complete, and the NNs weights for MERINA and Comyco are all trained on F&H dataset. The results in Fig. 3 illustrates that MERINA performs similarly to RobustMPC, and outperforms BOLA and Comyco on these new network environments. While Comyco performs the worst under public WiFi and international link conditions. 5.3 Fast Adaptation to New Environments Section 5.2 exhibits the satisfactory consistency performance of MERINA when confronted with some unseen throughout dynamics, and reveals that MERINA will degrade performance on traces with dynamics that are significantly different from those in the training dataset.

**Fragmento 7 - p. 7 - score 6:**

Table 1: Performance comparison of different ABR algorithms in terms of the average chunk 𝑄𝑜𝐸𝑙𝑜𝑔value on different datasets. Mean ± std (𝑅𝑔𝑎𝑝) FCC HSDPA Oboe Puffer-Oct.17-21 Puffer-Feb.18-22 BOLA 0.95 ± 0.63 (−17%) 1.11 ± 0.64 (−9%) 1.63 ± 0.66 (−11%) 0.88 ± 1.29 (+20%) 0.75 ± 1.93 (−14%) RobustMPC 1.05 ± 0.63 (−8%) 1.16 ± 0.85 (−5%) 1.79 ± 0.73 (−2%) 0.76 ± 1.48 (+5%) 0.86 ± 2.01 (−2%) Pensieve 1.07 ± 0.62 (−7%) 1.21 ± 0.68 (−1%) 1.75 ± 0.69 (−4%) 0.40 ± 7.17 (−46%) 0.66 ± 5.40 (−25%) Comyco 1.11 ± 0.63 (−3%) 1.22 ± 0.78 (−0%) 1.76 ± 0.77 (−3%) −0.22 ± 2.20 (−130%) 0.65 ± 2.25 (−26%) Fugu 1.04 ± 0.70 (−10%) 1.16 ± 0.80 (−5%) 1.71 ± 0.78 (−6%) 0.54 ± 1.55 (−26%) 0.77 ± 1.94 (−12%) BayesMPC 1.05 ± 0.78 (−9%) 1.09 ± 0.84 (−2%) 1.78 ± 0.74 (−2%) 0.54 ± 1.88 (−26%) 0.76 ± 2.20 (−14%) MARINA 1.15 ± 0.66 1.22 ± 0.85 1.82 ± 0.70 0.73 ± 1.63 0.88 ± 2.00 MERINA (nMI with 𝜆= 0, see Appendix B.3) 1.05 ± 0.65 (−9%) 1.19 ± 0.71 (−2%) 1.74 ± 0.69 (−4%) 0.71 ± 1.58 (−2%) 0.83 ± 1.96 (−5%) Dataset distribution 1.13 ± 0.44 Mbps 1.61 ± 0.95 Mbps 2.60 ± 2.08 Mbps 1.85 ± 0.91 Mbps 1.60 ± 0.88 Mbps is just 0.3 less than RobustMPC’s.

**Fragmento 8 - p. 7 - score 6:**

Furthermore, the bar graphs in Figs. 2(c) and 2(f) indicate that MERINA can surprisingly achieve low rebuffering and smoothness penalties, similar to those of Pensieve. While other algorithms result in either a longer rebuffering time, as Comyco does, or a higher quality fluctuation, as BOLA does, during the video playback. Note that the results obtained for linear QoE metric 𝑄𝑜𝐸𝑙𝑖𝑛are similar to those for log-form QoE metric 𝑄𝑜𝐸𝑙𝑜𝑔w.r.t. all comparison algorithms. Therefore, we only show and compare the performance for 𝑄𝑜𝐸𝑙𝑜𝑔in the following, and move results of 𝑄𝑜𝐸𝑙𝑖𝑛to Appendix B due to page limit. 5.2 Consistency on Out-of-Distribution Traces To study the consistency of MERINA in comparison to other learning-based methods, we measure their performance on out- of-distribution datasets Oboe, Puffer-Oct.17-21 and Puffer-Feb.18- 22 (i.e., with a different distribution of throughput dynamics than F&H dataset) by using the same NN weights obtained in Section 5.1 (i.e., learned from the F&H dataset).

**Fragmento 9 - p. 11 - score 6:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal Table 2: Performance comparison of different ABR algorithms in terms of the average chunk 𝑄𝑜𝐸𝑙𝑖𝑛value on different datasets. Mean ± std (𝑅𝑔𝑎𝑝) FCC HSDPA Oboe Puffer-Oct.17-21 Puffer-Feb.18-22 BOLA 0.96 ± 0.54 (−20%) 1.12 ± 0.81 (−16%) 1.96 ± 1.03 (−16%) 0.86 ± 1.83 (+1%) 0.66 ± 2.90 (−26%) RobustMPC 0.98 ± 0.75 (−18%) 1.22 ± 1.20 (−9%) 2.30 ± 1.24 (−2%) 0.73 ± 2.16 (−14%) 0.81 ± 2.97 (−9%) Pensieve 1.13 ± 0.65 (−5%) 1.28 ± 0.95 (−5%) 2.26 ± 1.15 (−4%) 0.14 ± 11.55 (−84%) 0.55 ± 8.67 (−44%) Comyco 1.15 ± 0.73 (−3%) 1.34 ± 1.05 (0%) 2.29 ± 1.21 (−2%) −0.13 ± 2.86 (−115%) 0.68 ± 3.06 (−24%) Fugu 1.11 ± 0.70 (−7%) 1.24 ± 1.04 (−7%) 2.31 ± 1.21 (−1%) 0.74 ± 2.13 (−13%) 0.83 ± 2.99 (−7%) BayesMPC 1.10 ± 0.83 (−8%) 1.26 ± 1.11 (−6%) 2.29 ± 1.23 (−2%) 0.33 ± 2.80 (−61%) 0.66 ± 3.34 (−26%) MERINA 1.19 ± 0.67 1.34 ± 0.99 2.34 ± 1.15 0.85 ± 2.02 0.90 ± 2.97 MERINA (nMI with 𝜆= 0) 1.08 ± 0.66 (−9%) 1.22 ± 1.11 (−9%) 2.25 ± 1.19 (−4%) 0.50 ± 2.68 (−61%) 0.72 ± 2.99 (−19%) Dataset distribution 1.13 ± 0.44 Mbps 1.61 ± 0.95 Mbps 2.60 ± 2.08 Mbps 1.85 ± 0.91 Mbps 1.60 ± 0.88 Mbps 0 1 2 3 4 5 4G Public WiFi International Link Average value BOLA RobustMPC Comyco MERINA Figure 5: Comparison of 𝑄𝑜𝐸𝑙𝑖𝑛without adaption.

**Fragmento 10 - p. 6 - score 5:**

1) BOLA [21]: a buffer-based algorithm that uses Lyapunov optimization to determine the optimal bitrate version under the constraint of buffer occupancy only. 2) RobustMPC [24]: a model-based algorithm that solves the optimization problem in Eq. (3) with a horizon of the future ℎ video chunks under the framework of model predictive control. The future throughput is predicted by the harmonic mean of average throughput measurements of the past 5 downloaded chunks. 3) Pensieve [14]: a DRL-based algorithm that uses the A3C algorithm to learn an optimal neural mapping from the dynamics of buffer occupancy, throughput and chunk size to the rate adaptation of the next chunk. 4) Comyco [7, 8]: a model-free neural ABR algorithm that uses NNs to directly approximate the offline near-optimal expert solution by lifelong imitation learning.

**Fragmento 11 - p. 6 - score 5:**

The CDFs in Figs. 2(b) and 2(e) illustrate the QoE improvements of the other algorithms over RobustMPC in all sessions. And the bar graphs in Figs. 2(c) and 2(f) show the average chunk QoE and each individual components in Eq. (2), where the error bars span ± one standard deviation from the average value. The key observation is that MERINA outperforms the other baseline algorithms in terms of the average chunk QoE value with both the linear and log-form QoE metrics on the F&H throughput dataset. The performance gap of the average chunk QoE between MERINA and the baseline algorithms is at least 3% and 4% for 𝑄𝑜𝐸𝑙𝑖𝑛and 𝑄𝑜𝐸𝑙𝑜𝑔, respectively. And Comyco beats the remaining baseline algorithms in terms of QoE (slightly better than Pensieve), demonstrating the effectiveness of imitation learning.

**Fragmento 12 - p. 6 - score 5:**

As for the variance of the results for all sessions, BOLA has the lowest standard deviation (0.72 for 𝑄𝑜𝐸𝑙𝑖𝑛 and 0.65 for 𝑄𝑜𝐸𝑙𝑜𝑔) but the worst average QoE, whereas MERINA also performs well, with a standard deviation of 0.87 and 0.71 for 𝑄𝑜𝐸𝑙𝑖𝑛and 𝑄𝑜𝐸𝑙𝑜𝑔, respectively. In addition, the results also reveal that MERINA performs robustly throughout all sessions, with a largest proportion of sessions achieving a higher QoE. For instance, Figs. 2(a) and 2(d) show that at least 95% of MERINA sessions achieve an average QoE greater than 0. The results in Fig. 2(b) and Fig. 2(e) verify that in about 80% of sessions, MERINA outperforms RobustMPC, and in the worst case the average QoE of MERINA 3011

**Fragmento 13 - p. 7 - score 5:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal #FUUFS (a) 𝑄𝑜𝐸𝑙𝑖𝑛 #FUUFS (b) 𝑄𝑜𝐸𝑙𝑖𝑛 0 0.2 0.4 0.6 0.8 1 1.2 1.4 Chunk QoE Bitrate utility Rebuffering penalty Smoothness penalty Averagevalue BOLA RobustMPC Pensieve Comyco Fugu BayesMPC MERINA (c) 𝑄𝑜𝐸𝑙𝑖𝑛 #FUUFS (d) 𝑄𝑜𝐸𝑙𝑜𝑔 #FUUFS (e) 𝑄𝑜𝐸𝑙𝑜𝑔 0 0.2 0.4 0.6 0.8 1 1.2 1.4 Chunk QoE Bitrate utility Rebuffering penalty Smoothness penalty Averagevalue BOLA RobustMPC Pensieve Comyco Fugu BayesMPC MERINA (f) 𝑄𝑜𝐸𝑙𝑜𝑔 Figure 2: Performance comparison of different ABR algorithms in terms of the average chunk QoE value and the individual QoE components with the QoE metrics 𝑄𝑜𝐸𝑙𝑖𝑛and 𝑄𝑜𝐸𝑙𝑜𝑔on F&H (FCC and HSDPA) throughput dataset.

**Fragmento 14 - p. 8 - score 5:**

In a training epoch, the NN weights are updated twice, while each update is with a batch size of 64 samples. (a) Adaptation Curves #FUUFS (b) Puffer-Oct.17-21 Figure 4: a) The adaptation curves of MERINA and Comyco, and b) average chunk 𝑄𝑜𝐸𝑙𝑜𝑔improvement over RobustMPC. Fig. 4(a) demonstrates that MERINA can outperform RobustMPC with only a few of epochs, and achieve a QoE performance comparable to that of BOLA (performs best in this dataset) with around 200 training epochs (lasting about 10 minutes). To verify the performance further, we show the CDFs of QoE improvement of comparison algorithms over RobustMPC in Fig. 4(b), with MERINA-Offline, MERINA-Adp-30 and MERINA-Adp-200 denoting the proposed algorithm that employs the NN weights without adaptation, after 30-epoch adaptation, and after 200- epoch adaptation, respectively.

**Fragmento 15 - p. 8 - score 5:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. 0 0.5 1 1.5 2 2.5 3 4G Public WiFi International Link Average value BOLA RobustMPC Comyco MERINA Figure 3: Comparison of 𝑄𝑜𝐸𝑙𝑜𝑔without adaption. NNs to learn the throughput dynamics have a better consistency or generalization than Pensieve and Comyco, though they also perform much worse on Puffer traces than heuristic methods. This demonstrates that, besides meta-RL-based methods, model-based methods are another viable paradigm for addressing the general- ization challenge of adaptive video streaming. In conclusion, our MERINA performs consistently with out-of-distribution throughput dynamics, though it may have a worse QoE than BOLA in some sessions.

**Fragmento 16 - p. 10 - score 5:**

This might be because the linear quality metric produces bigger quality intervals between the bitrate versions than the log-form metric, resulting in a more distinct feature for the bitrate selection. Additionally, Fugu outperforms RobustMPC in terms of the average chunk quality on the two puffer datasets when using the metric 𝑄𝑜𝐸𝑙𝑖𝑛, but performs much worse when using the metric 𝑄𝑜𝐸𝑙𝑜𝑔. B.1.1 Real-World Test for 𝑄𝑜𝐸𝑙𝑖𝑛. With the same settings for 𝑄𝑜𝐸𝑙𝑜𝑔, we evaluate the learning-based algorithms MERINA and Comyco, and the heuristic algorithms BOLA and RobustMPC, by using the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛in the real world platform under three different network conditions: a 4G cellular network, a public WiFi network on campus, and a wide area network connecting Shanghai and Los Angeles, with mean and standard 3015

**Fragmento 17 - p. 6 - score 4:**

Therefore, we re-implement Fugu and utilize it as a baseline ABR algorithm that optimizes the expectation of QoE with a probabilistic download time predictor. Additionally, the planning horizon of RobustMPC, Fugu and BayesMPC is set to ℎ= 3 chunks. Datasets of network throughput. We collect four public real- world network throughput datasets (3G/HSDPA [17], FCC [2], Oboe [1], Puffer [23]) to simulate various user and network conditions. The mean and standard deviation values of these datasets are listed in bottom row of Table 1. We combine the similar datasets FCC and 3G/HSDPA into one dataset (named F&H), which is then used to validate the in-distribution performance of different ABR algorithms. Note that the datasets 3G/HSDPA, FCC and Oboe contain only a small amount of traces, but the throughput data of Puffer is updated daily (data of a single day takes up to several GB) and has been regularly updated since January 2019.

**Fragmento 18 - p. 6 - score 4:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. 5 PERFORMANCE EVALUATION Experiment setup. To evaluate the performance in terms of the average chunk QoE, consistency and fast adaptation across a wide range of throughput patterns, we test MERINA on the virtual player as widely used in [1, 7, 8, 10, 14], which simulates the adaptive video streaming process by using the real-world network throughput datasets, in comparison to other ABR algorithms. For the sake of fairness, we also use the same environment settings as in [7, 8, 14]: the available bitrate set is A = {300, 750, 1200, 1850, 2850, 4300} 𝐾𝑏𝑝𝑠, the chunk duration is set as 𝐿= 4 seconds, the buffer occupancy is limited as 1 minute, and the total number of video chunks is 𝐾= 49.

**Fragmento 19 - p. 7 - score 4:**

We show in Table 1 the numerical results that are composed of the average chunk QoE value ± one standard deviation for all the comparison algorithms and the performance gap 𝑅𝑔𝑎𝑝= [(𝑟−𝑟∗)/𝑟∗] × 100% to the value of MERINA, where 𝑟∗is the average chunk QoE of MERINA and 𝑟is the average chunk QoE of each comparison algorithm. Additionally, Table 1 also includes results from the FCC and HSDPA datasets to demonstrate the consistency of all algorithms’ performance on a subset of the training throughput dynamics distribution. The results on FCC and HSDPA traces show that the learning- based baselines perform worse on FCC traces than on HSDPA traces, indicating that training these algorithms on mixed dynamics is unlikely to result in the acquisition of expertise that performs uniformly across all experienced dynamics.

**Fragmento 20 - p. 8 - score 4:**

More importantly, MERINA can further rapidly adapt to the new throughput dynamics via a few updates (see Section 5.3). Real-World Test. We then evaluate MERINA, Comyco (the state- of-the-art model-free ABR algorithm) and the heuristic algorithms BOLA and RobustMPC in the real world platform under three different network conditions: a 4G cellular network, a public WiFi network on campus, and a wide area network connecting Shanghai and Los Angeles, with mean and standard deviation of recorded throughput values of 5.74 ± 0.39𝑀𝑏𝑝𝑠, 2.04 ± 0.89𝑀𝑏𝑝𝑠 and 1.78 ± 1.10𝑀𝑏𝑝𝑠. The real-world platform based on Dash.js [4] is implemented similarly to that in [7, 14], and we thus omit its description for simplicity.

**Fragmento 21 - p. 10 - score 4:**

The whole video streaming process can be summarized as follows. At the beginning of video streaming, the video client first obtains the video information, including the number of total video chunks and the available bitrates for corresponding chunks. The client then requests video chunks one by one, using the ABR controller to select the bitrate for future chunks. The requested bitrate version of chunks are downloaded through the video delivery simulator. Once completely downloaded, a video chunk is played back to the client. The playback information, such as buffer occupancy, rebuffering event, bitrate version of the current chunk, is collected to calculate the QoE value during the playback. B ADDITIONAL EXPERIMENTAL RESULTS B.1 Consistency on Out-of-Distribution Traces As with the log-form quality metric 𝑄𝑜𝐸𝑙𝑜𝑔, we compare the consistency of MERINA to other baseline algorithms here, with the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛on in-distribution and out-of- distribution datasets.

**Fragmento 22 - p. 11 - score 4:**

These real-world test for 𝑄𝑜𝐸𝑙𝑖𝑛still can demonstrate the generalization capability of MERINA when deployed in the real-world scenarios. B.2 Fast Adaptation To New Environments Though MERINA performs slightly worse than BOLA in terms of the average chunk QoE value on the throughput dynamics of Puffer-Oct.17-21 when using the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛, we examine here MERINA’s ability to rapidly adapt to this dataset and study how much improvement can be achieved through adaptation. All the settings w.r.t. the meta-adaptation procedures are the same to those of Section 5.3, with the associated results illustrated in Fig. 6. It can be seen from Fig. 6(a) that when using the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛, MERINA can surpass BOLA (0.86) in terms of average chunk QoE value with around 100 training epochs (see MERINA-Adpt) and achieves a much higher chunk QoE value 1.10 asymptotically (see MERINA-Asy).

**Fragmento 23 - p. 11 - score 4:**

The results suggested that, after 1100- epoch adaptation, the proportion of sessions that achieve high QoE value rise significantly. B.3 Ablation Study Finally, we conduct some experiments to demonstrate the benefit to generalization as introduced by the proposed mutual information- based regularization function in Eq. (5), providing a further insight on MERINA. We train a modified version of MERINA, named MERINA (nMI), by setting 𝜆= 0 for the actor loss, on the training dateset F&H, and then evaluate its QoE performance on all the five datasets. The results of average chunk QoE achieved by MERINA (nMI) are also presented in Tables 1 and 2 for 𝑄𝑜𝐸𝑙𝑜𝑔and 𝑄𝑜𝐸𝑙𝑖𝑛, respectively, which reveal a critical finding: the mutual information- based regularizer improves the average QoE performance and generalization on both in- and out-of-distribution datasets.

**Fragmento 24 - p. 1 - score 3:**

In addition, the ABR algorithm in practice is also expected to be able to implement quickly online, because a higher overhead of inference time for rate adaptation will inevitably increase the end-to-end latency. To address this challenge, Yin et al. in [24] argued that the model predictive control (MPC) approach is a natural fit for the rate adaptation problem and proposed two simple yet effective algorithms, namely RobustMPC and FastMPC, based on the pre- diction of future network throughput with the harmonic mean of past throughput. Following this principle, various studies (e.g., CS2P[22], BayesMPC[10], Fugu[23]) have been proposed to seek for a higher QoE by improving the throughput prediction accuracy.

**Fragmento 25 - p. 2 - score 3:**

• We implement MERINA’s meta-training and meta-adaptation procedures, and validate its improved generalization capability through numerous empirical evaluations on different QoE metrics and multiple datasets containing real-world network throughput traces, as well as a real-world test. These evaluations demonstrate that MERINA outperforms the state-of-the-art ABR algorithms in terms of both the average chunk QoE on the in-distribution throughput traces, and the capability of generalization and quick adaptation on the out-of-distribution throughput traces. 2 BACKGROUND AND MOTIVATION 2.1 Problem Formulation In a typical adaptive video streaming system, the video is temporally divided into 𝐾chunks (i.e., segments) with a fixed time duration 𝐿.

**Fragmento 26 - p. 6 - score 3:**

By choosing the NNs weights that perform best on the validation set, the performance of all comparison algorithms is then tested on the test set. Note that the QoE performance may slightly vary with the random traces selection and unstable NNs training, so it is natural to notice some discrepancies between earlier works and ours. We simulate the playback of the same video once for each throughput trace (referred to as a session), and then collect QoE values of all chunks for comparison. Since the test and training sets share the same distribution of throughout traces, we call the results in-distribution QoE performance. Figs. 2(a) and 2(d) depict the cumulative distribution functions (CDFs) of all sessions’ average QoE for all algorithms.


### 7.8. resultados numericos metricas

Palabras clave usadas: `improvement, improve, gain, reduce, reduction, %, QoE gain, higher, lower, average, median, percentile, stall time, latency, overhead, accuracy, significant, p95, p99, score, ratio, duration`

**Fragmento 1 - p. 8 - score 6:**

The results indicate that after 30-epoch adaptation, the proportion of sessions that achieve much lower/higher QoE value than RobustMPC significantly decreases/increases. And after 200-epochs adaptation, MERINA has a similar distribution to BOLA, in terms of average QoE improvement. While Comyco’s performance cannot be improved rapidly due to its low initial performance, and also because the lifelong learning method cannot ensure policy improvement in a significantly changed environment. The asymptotic performance of MERINA indicates that it can achieve a superior QoE performance when compared to all baselines following a meta-adaptation pro- cedure, implying that MERINA can achieve the best generalization performance and will outperform baseline algorithms across a range of throughput dynamics through the adaptation.

**Fragmento 2 - p. 11 - score 5:**

It is also seen that MERINA’s performance will degrade after a few update epochs and then improve monotonously. This is because the initial parameters 𝜙and 𝜃may be near a local optimum for the new throughput dynamics, while exploring for a higher value (towards the global optimum) may experience a performance degradation (a) Adaptation Curves #FUUFS (b) Puffer-Oct.17-21 Figure 6: a) The adaptation curves of MERINA and Comyco, and b) average chunk 𝑄𝑜𝐸𝑙𝑖𝑛improvement over RobustMPC. at first and then the performance improvement. Additionally, we show the CDFs of QoE improvement of comparison algorithms over RobustMPC in Fig. 6(b), with MERINA-Offline, MERINA- Adp-100 and MERINA-Adp-1100 denoting the proposed algorithm that employs the NN weights without adaptation, after 100- epoch adaptation (before the performance degradation), and after 1100-epoch adaptation (performance improved again after the degradation), respectively.

**Fragmento 3 - p. 1 - score 4:**

In addition, the ABR algorithm in practice is also expected to be able to implement quickly online, because a higher overhead of inference time for rate adaptation will inevitably increase the end-to-end latency. To address this challenge, Yin et al. in [24] argued that the model predictive control (MPC) approach is a natural fit for the rate adaptation problem and proposed two simple yet effective algorithms, namely RobustMPC and FastMPC, based on the pre- diction of future network throughput with the harmonic mean of past throughput. Following this principle, various studies (e.g., CS2P[22], BayesMPC[10], Fugu[23]) have been proposed to seek for a higher QoE by improving the throughput prediction accuracy.

**Fragmento 4 - p. 2 - score 4:**

• We implement MERINA’s meta-training and meta-adaptation procedures, and validate its improved generalization capability through numerous empirical evaluations on different QoE metrics and multiple datasets containing real-world network throughput traces, as well as a real-world test. These evaluations demonstrate that MERINA outperforms the state-of-the-art ABR algorithms in terms of both the average chunk QoE on the in-distribution throughput traces, and the capability of generalization and quick adaptation on the out-of-distribution throughput traces. 2 BACKGROUND AND MOTIVATION 2.1 Problem Formulation In a typical adaptive video streaming system, the video is temporally divided into 𝐾chunks (i.e., segments) with a fixed time duration 𝐿.

**Fragmento 5 - p. 2 - score 4:**

Empirically, we compare MERINA to other ABR baselines on different QoE metrics and real-world throughput traces, as well as a 3-hour real-world test. Evaluation results demonstrate that MERINA outperforms state-of-the-art ABR algorithms on the in-distribution traces by at least 3% in terms of average chunk QoE. On three out-of- distribution datasets and real-world test, MERINA beats all neural baselines in terms of the average chunk QoE without adaptation, presenting a performance gain of up to 26% between MERINA and the second-best algorithm, and achieves a higher average chunk QoE over all baselines with only about 200 epochs (i.e., 5 minutes) of adaptation. Our main contributions can be summarized as follows.

**Fragmento 6 - p. 6 - score 4:**

The CDFs in Figs. 2(b) and 2(e) illustrate the QoE improvements of the other algorithms over RobustMPC in all sessions. And the bar graphs in Figs. 2(c) and 2(f) show the average chunk QoE and each individual components in Eq. (2), where the error bars span ± one standard deviation from the average value. The key observation is that MERINA outperforms the other baseline algorithms in terms of the average chunk QoE value with both the linear and log-form QoE metrics on the F&H throughput dataset. The performance gap of the average chunk QoE between MERINA and the baseline algorithms is at least 3% and 4% for 𝑄𝑜𝐸𝑙𝑖𝑛and 𝑄𝑜𝐸𝑙𝑜𝑔, respectively. And Comyco beats the remaining baseline algorithms in terms of QoE (slightly better than Pensieve), demonstrating the effectiveness of imitation learning.

**Fragmento 7 - p. 11 - score 4:**

These real-world test for 𝑄𝑜𝐸𝑙𝑖𝑛still can demonstrate the generalization capability of MERINA when deployed in the real-world scenarios. B.2 Fast Adaptation To New Environments Though MERINA performs slightly worse than BOLA in terms of the average chunk QoE value on the throughput dynamics of Puffer-Oct.17-21 when using the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛, we examine here MERINA’s ability to rapidly adapt to this dataset and study how much improvement can be achieved through adaptation. All the settings w.r.t. the meta-adaptation procedures are the same to those of Section 5.3, with the associated results illustrated in Fig. 6. It can be seen from Fig. 6(a) that when using the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛, MERINA can surpass BOLA (0.86) in terms of average chunk QoE value with around 100 training epochs (see MERINA-Adpt) and achieves a much higher chunk QoE value 1.10 asymptotically (see MERINA-Asy).

**Fragmento 8 - p. 2 - score 3:**

Each video chunk is further encoded into multiple quality versions of different bitrates, with the set of available bitrates denoted by A = {𝑎1,𝑎2, · · · ,𝑎𝑀}, where 𝑀represents the total number of bitrate versions. Let 𝑎𝑘∈A denote the bitrate version allocated for the 𝑘-th chunk 𝑈𝑘. Then, once the chunk 𝑈𝑘has been completely downloaded, the buffer occupancy 𝐵𝑘of the video player deployed at the user side can be expressed as: 𝐵𝑘= [(𝐵𝑘−1 −𝑑𝑘)+ + 𝐿], 𝑑𝑘= 𝐸𝑎𝑘/𝐶𝑘, (·)+ ≜max{·, 0}, (1) where 𝐶𝑘is the average network throughput within the duration of downloading chunk𝑈𝑘, 𝐸𝑎𝑘denotes the actual size of𝑈𝑘associated with the selected bitrate version 𝑎𝑘, the term 𝑑𝑘then represents the corresponding time duration spent for downloading chunk 𝑈𝑘.

**Fragmento 9 - p. 3 - score 3:**

Encountering a new network environment, this latent variable 𝒛can reason about dynamics uncertainty, allowing for a stochastic exploration of meta-learned policy to explore states with potentially higher rewards while also quickly adapting to the new dynamics. Meanwhile, sampling the latent variable from a probabilistic distribution improves the generalization of control policies when a deterministic inference of dynamics is difficult. • 2) Latent-conditioned policy network (i.e., policy search). To identify a universal ABR control policy capable of adapting its behavior to the network throughput dynamics, we set a 𝜃- parameterized policy 𝜋𝜃(𝒂|𝒔, 𝒛) as conditioned on the latent variable 𝒛. Thus, if the latent variable 𝒛can be reliably inferred from the recent experience, the resulting policy 𝜋𝜃(𝒂|𝒔, 𝒛) will potentially adapt to a new network environment.

**Fragmento 10 - p. 6 - score 3:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. 5 PERFORMANCE EVALUATION Experiment setup. To evaluate the performance in terms of the average chunk QoE, consistency and fast adaptation across a wide range of throughput patterns, we test MERINA on the virtual player as widely used in [1, 7, 8, 10, 14], which simulates the adaptive video streaming process by using the real-world network throughput datasets, in comparison to other ABR algorithms. For the sake of fairness, we also use the same environment settings as in [7, 8, 14]: the available bitrate set is A = {300, 750, 1200, 1850, 2850, 4300} 𝐾𝑏𝑝𝑠, the chunk duration is set as 𝐿= 4 seconds, the buffer occupancy is limited as 1 minute, and the total number of video chunks is 𝐾= 49.

**Fragmento 11 - p. 6 - score 3:**

As for the variance of the results for all sessions, BOLA has the lowest standard deviation (0.72 for 𝑄𝑜𝐸𝑙𝑖𝑛 and 0.65 for 𝑄𝑜𝐸𝑙𝑜𝑔) but the worst average QoE, whereas MERINA also performs well, with a standard deviation of 0.87 and 0.71 for 𝑄𝑜𝐸𝑙𝑖𝑛and 𝑄𝑜𝐸𝑙𝑜𝑔, respectively. In addition, the results also reveal that MERINA performs robustly throughout all sessions, with a largest proportion of sessions achieving a higher QoE. For instance, Figs. 2(a) and 2(d) show that at least 95% of MERINA sessions achieve an average QoE greater than 0. The results in Fig. 2(b) and Fig. 2(e) verify that in about 80% of sessions, MERINA outperforms RobustMPC, and in the worst case the average QoE of MERINA 3011

**Fragmento 12 - p. 8 - score 3:**

In a training epoch, the NN weights are updated twice, while each update is with a batch size of 64 samples. (a) Adaptation Curves #FUUFS (b) Puffer-Oct.17-21 Figure 4: a) The adaptation curves of MERINA and Comyco, and b) average chunk 𝑄𝑜𝐸𝑙𝑜𝑔improvement over RobustMPC. Fig. 4(a) demonstrates that MERINA can outperform RobustMPC with only a few of epochs, and achieve a QoE performance comparable to that of BOLA (performs best in this dataset) with around 200 training epochs (lasting about 10 minutes). To verify the performance further, we show the CDFs of QoE improvement of comparison algorithms over RobustMPC in Fig. 4(b), with MERINA-Offline, MERINA-Adp-30 and MERINA-Adp-200 denoting the proposed algorithm that employs the NN weights without adaptation, after 30-epoch adaptation, and after 200- epoch adaptation, respectively.

**Fragmento 13 - p. 10 - score 3:**

The state of the video streaming system, includes the features as detailed in Section 2, is fed into the input layer of the actor and critic networks. Concretely, for the set of available bitrate versions A, we use a one-dimensional convolution layer with 128 filters, each of size 4 with stride 1, to process them. Meanwhile, five full connected layers with 128 neurons are placed at the input layer to deal with the remaining features of the state, including the measured average throughput 𝐶𝑘−1, time duration 𝑑𝑘−1 during the download of the last video chunk, current buffer occupancy 𝐵𝑘, selected bitrate 𝑎𝑘−1 of the last chunk, and the number of video chunks that have not been downloaded yet. For the latent variable sampled from the posterior 𝑞𝜙(𝒛|𝒄), we also use a fully connected layer with 1280 neurons to process the latent representations.

**Fragmento 14 - p. 11 - score 3:**

The results suggested that, after 1100- epoch adaptation, the proportion of sessions that achieve high QoE value rise significantly. B.3 Ablation Study Finally, we conduct some experiments to demonstrate the benefit to generalization as introduced by the proposed mutual information- based regularization function in Eq. (5), providing a further insight on MERINA. We train a modified version of MERINA, named MERINA (nMI), by setting 𝜆= 0 for the actor loss, on the training dateset F&H, and then evaluate its QoE performance on all the five datasets. The results of average chunk QoE achieved by MERINA (nMI) are also presented in Tables 1 and 2 for 𝑄𝑜𝐸𝑙𝑜𝑔and 𝑄𝑜𝐸𝑙𝑖𝑛, respectively, which reveal a critical finding: the mutual information- based regularizer improves the average QoE performance and generalization on both in- and out-of-distribution datasets.

**Fragmento 15 - p. 2 - score 2:**

The rebuffering event will occur within the duration of (𝑑𝑘−𝐵𝑘−1)+ if the term 𝐵𝑘−1−𝑑𝑘is negative, i.e., the buffer has no video remaining while the next chunk 𝑈𝑘has not been completely downloaded yet. As conventionally adopted in many learning-based ABR algo- rithms, the adaptive video streaming system can be formulated 3007

**Fragmento 16 - p. 3 - score 2:**

Note that the dynamics of network throughput are practically hidden from the agent and independent of the chosen actions, which are typically time-varying and heterogeneous in real world scenarios. Consequently, the state transition probability 𝑃will vary continuously over time and result in a variety of different MDPs, which in essence can be formulated more accurately as a partially observable Markov decision process (POMDP). By denoting the underlying throughput dynamics as a latent variable 𝒛∈𝑍, we can re-formulate the adaptive video streaming problem as a tuple < S, A, 𝑃,𝑍, 𝑅>, where the state space S, action space A and reward space 𝑅remain the same, while the state transition probability changes to 𝑃= 𝑝(𝑠𝑘+1|𝑠𝑘,𝑎𝑘,𝑧𝑘), with 𝑧𝑘representing the throughput dynamics during the duration of downloading chunk 𝑈𝑘.

**Fragmento 17 - p. 5 - score 2:**

, (7) 𝜌(𝜃) = 𝜋𝜃(𝒂|𝒔, 𝒛)/𝜋𝜃′(𝒂|𝒔, 𝒛), 𝒛∼𝑞𝜙(𝒛|𝒄) where𝜃′ denotes the previous values of𝜃following the latest update epoch, clip[𝜌(𝜃), 1 −𝜖, 1 + 𝜖] ensures no incentive for moving 𝜌(𝜃) outside the interval [1−𝜖, 1+𝜖], and ˆ𝐴is the truncated generalized advantage estimation (GAE) function [18] generated from the value function 𝑉𝜃𝑣(𝒔, 𝒛) and 𝒓. Similarly, the critic loss is formulated as: L𝜃𝑣(𝒄,𝝉) = 1 2E¯𝒛  (𝑉𝜃𝑣(𝒔, ¯𝒛) −𝐺𝑘)2 , ¯𝒛∼𝑞𝜙(𝒛|𝒄), (8) where 𝐺𝑘= 𝑟𝑘+ 𝛾𝑟𝑘+1 + 𝛾2𝑟𝑘+2 + · · · is the rollout QoE return of the current state following 𝜋𝜃′(𝒂|𝒔, 𝒛),𝛾∈(0, 1] is a discount factor that attenuates exponentially the impact of future actions over the current expected QoE, and ¯𝒛indicates that gradients are not being computed through it. 4.2 Imitation Learning-Based Pre-Training In practice, due to the low sample efficiency of RL training [15], training the meta-RL from scratch is exceedingly time expensive and unstable in our setting of mixed dynamics. Therefore, we pre-train the parameters 𝜙and 𝜃following the imitation learning method proposed in [7], with a behavior cloning objective for the actor and inference networks: max 𝜃,𝜙 E𝒛, ˆ𝒂log 𝜋𝜃( ˆ𝒂|𝒔, 𝒛), 𝒛∼𝑞𝜙(𝒛|𝒄), ˆ𝒂∼𝜋𝑒(𝒂|𝒔), (9) where the model-based ABR algorithm RobustMPC [24] is adopted to obtain the expert policy 𝜋𝑒(𝒂|𝒔), with the QoE maximized over a horizon of future 3 chunks. Here, we skip the pre-training of critic network, since 𝜃𝑣may be rapidly converged with only a few trials following the policy 𝜋𝜃(𝒂|𝒔, 𝒛). Notably, we employ RobustMPC here primarily for its good QoE performance and low computational complexity, which will be also justified by the experimental evaluations in Section 5. However, variants of MERINA can be easily fulfilled by adopting other existing ABR algorithms to obtain the expert policy, resulting in a difference on the training time and overall QoE performance. In summary, the entire meta-training and meta-adaptation workflow of MERINA is given in Algorithm 1 and Algorithm 2, Algorithm 1 Meta-training Procedure of MERINA Require: Dynamics model 𝑓of the video streaming system with time-varying and heterogeneous network dynamics, learning rates 𝛼1, 𝛼2, 𝛼3 // First stage: pre-training with ex

**Fragmento 18 - p. 5 - score 2:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal ∇𝐽/∇𝜙= ∇𝐽/∇𝒛· ∇𝒛/∇𝜙. Note that we can pass the gradient from the policy network to inference network with the Gaussian re- parameterization trick [11], even though the latent variable input of policy network is sampled from the output of inference network, i.e., 𝒛∼𝑞𝜙(𝒛|𝒄). 4 IMPLEMENTATION 4.1 Meta-Policy Search with DRL To enable an effective policy search, we build up our algorithm on top of the proximal policy optimization (PPO) algorithm [19], a well known on-policy actor-critic method recognized for its reliable performance on policy improvement with trust region policy optimization. With PPO, we construct two networks: an actor network 𝜋𝜃(𝒂|𝒔, 𝒛) and a critic network 𝑉𝜃𝑣(𝒔, 𝒛). We jointly train the inference and actor networks to maximize the actor loss and the regularization I(𝒂; 𝒛|𝒔) on the parameters of 𝜃and 𝜙. As a result, the objective ˜𝐽𝜃(𝒄,𝝉) of the actor network is expressed as: ˜𝐽𝜃(𝒄,𝝉) = E𝒛

**Fragmento 19 - p. 7 - score 2:**

Table 1: Performance comparison of different ABR algorithms in terms of the average chunk 𝑄𝑜𝐸𝑙𝑜𝑔value on different datasets. Mean ± std (𝑅𝑔𝑎𝑝) FCC HSDPA Oboe Puffer-Oct.17-21 Puffer-Feb.18-22 BOLA 0.95 ± 0.63 (−17%) 1.11 ± 0.64 (−9%) 1.63 ± 0.66 (−11%) 0.88 ± 1.29 (+20%) 0.75 ± 1.93 (−14%) RobustMPC 1.05 ± 0.63 (−8%) 1.16 ± 0.85 (−5%) 1.79 ± 0.73 (−2%) 0.76 ± 1.48 (+5%) 0.86 ± 2.01 (−2%) Pensieve 1.07 ± 0.62 (−7%) 1.21 ± 0.68 (−1%) 1.75 ± 0.69 (−4%) 0.40 ± 7.17 (−46%) 0.66 ± 5.40 (−25%) Comyco 1.11 ± 0.63 (−3%) 1.22 ± 0.78 (−0%) 1.76 ± 0.77 (−3%) −0.22 ± 2.20 (−130%) 0.65 ± 2.25 (−26%) Fugu 1.04 ± 0.70 (−10%) 1.16 ± 0.80 (−5%) 1.71 ± 0.78 (−6%) 0.54 ± 1.55 (−26%) 0.77 ± 1.94 (−12%) BayesMPC 1.05 ± 0.78 (−9%) 1.09 ± 0.84 (−2%) 1.78 ± 0.74 (−2%) 0.54 ± 1.88 (−26%) 0.76 ± 2.20 (−14%) MARINA 1.15 ± 0.66 1.22 ± 0.85 1.82 ± 0.70 0.73 ± 1.63 0.88 ± 2.00 MERINA (nMI with 𝜆= 0, see Appendix B.3) 1.05 ± 0.65 (−9%) 1.19 ± 0.71 (−2%) 1.74 ± 0.69 (−4%) 0.71 ± 1.58 (−2%) 0.83 ± 1.96 (−5%) Dataset distribution 1.13 ± 0.44 Mbps 1.61 ± 0.95 Mbps 2.60 ± 2.08 Mbps 1.85 ± 0.91 Mbps 1.60 ± 0.88 Mbps is just 0.3 less than RobustMPC’s.

**Fragmento 20 - p. 7 - score 2:**

We show in Table 1 the numerical results that are composed of the average chunk QoE value ± one standard deviation for all the comparison algorithms and the performance gap 𝑅𝑔𝑎𝑝= [(𝑟−𝑟∗)/𝑟∗] × 100% to the value of MERINA, where 𝑟∗is the average chunk QoE of MERINA and 𝑟is the average chunk QoE of each comparison algorithm. Additionally, Table 1 also includes results from the FCC and HSDPA datasets to demonstrate the consistency of all algorithms’ performance on a subset of the training throughput dynamics distribution. The results on FCC and HSDPA traces show that the learning- based baselines perform worse on FCC traces than on HSDPA traces, indicating that training these algorithms on mixed dynamics is unlikely to result in the acquisition of expertise that performs uniformly across all experienced dynamics.

**Fragmento 21 - p. 11 - score 2:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal Table 2: Performance comparison of different ABR algorithms in terms of the average chunk 𝑄𝑜𝐸𝑙𝑖𝑛value on different datasets. Mean ± std (𝑅𝑔𝑎𝑝) FCC HSDPA Oboe Puffer-Oct.17-21 Puffer-Feb.18-22 BOLA 0.96 ± 0.54 (−20%) 1.12 ± 0.81 (−16%) 1.96 ± 1.03 (−16%) 0.86 ± 1.83 (+1%) 0.66 ± 2.90 (−26%) RobustMPC 0.98 ± 0.75 (−18%) 1.22 ± 1.20 (−9%) 2.30 ± 1.24 (−2%) 0.73 ± 2.16 (−14%) 0.81 ± 2.97 (−9%) Pensieve 1.13 ± 0.65 (−5%) 1.28 ± 0.95 (−5%) 2.26 ± 1.15 (−4%) 0.14 ± 11.55 (−84%) 0.55 ± 8.67 (−44%) Comyco 1.15 ± 0.73 (−3%) 1.34 ± 1.05 (0%) 2.29 ± 1.21 (−2%) −0.13 ± 2.86 (−115%) 0.68 ± 3.06 (−24%) Fugu 1.11 ± 0.70 (−7%) 1.24 ± 1.04 (−7%) 2.31 ± 1.21 (−1%) 0.74 ± 2.13 (−13%) 0.83 ± 2.99 (−7%) BayesMPC 1.10 ± 0.83 (−8%) 1.26 ± 1.11 (−6%) 2.29 ± 1.23 (−2%) 0.33 ± 2.80 (−61%) 0.66 ± 3.34 (−26%) MERINA 1.19 ± 0.67 1.34 ± 0.99 2.34 ± 1.15 0.85 ± 2.02 0.90 ± 2.97 MERINA (nMI with 𝜆= 0) 1.08 ± 0.66 (−9%) 1.22 ± 1.11 (−9%) 2.25 ± 1.19 (−4%) 0.50 ± 2.68 (−61%) 0.72 ± 2.99 (−19%) Dataset distribution 1.13 ± 0.44 Mbps 1.61 ± 0.95 Mbps 2.60 ± 2.08 Mbps 1.85 ± 0.91 Mbps 1.60 ± 0.88 Mbps 0 1 2 3 4 5 4G Public WiFi International Link Average value BOLA RobustMPC Comyco MERINA Figure 5: Comparison of 𝑄𝑜𝐸𝑙𝑖𝑛without adaption.

**Fragmento 22 - p. 1 - score 1:**

In general, video quality can be enhanced by assigning a higher bitrate for the chunk to be transmitted, which, however, may result in a rebuffering event (i.e., stalling during playback) especially when the network condition is poor and unstable. As a key component of rate adaptation, adaptive bitrate stream- ing (ABR) algorithms aim to solve a stochastic optimal control problem that reveals how to strike an optimal trade-off between maximizing the video quality and avoiding the rebuffering, by determining the fine-grained bitrate combination sequentially for continuously transmitted video chunks. However, due to the time- varying and heterogeneous dynamics of network throughput in real world, it is unfortunately intractable to achieve the optimal trade-off with an explicit solution.

**Fragmento 23 - p. 1 - score 1:**

Finally, we implement our algorithm’s meta-training and meta-adaptation procedures under a variety of throughput dynamics. Empirical evaluations on different QoE metrics and multiple datasets containing real-world network traces demonstrate that our algorithm outperforms state-of-the-art ABR algorithms, in terms of the performance on the average chunk QoE, consistency and fast adaptation across a wide range of throughput patterns. CCS CONCEPTS • Information systems →Multimedia streaming; • Comput- ing methodologies →Sequential decision making. KEYWORDS Rate adaptation, meta deep reinforcement learning, generalization. ACM Reference Format: Nuowen Kan, Yuankun Jiang, Chenglin Li, Wenrui Dai, Junni Zou, and Hongkai Xiong.

**Fragmento 24 - p. 2 - score 1:**

• We study the generalization problem of adaptive video streaming, and formulate the rate adaptation problem as a POMDP, rather than previously stated MDP. We then propose a model-free system framework based on context-based meta-RL to improve generalization for neural ABR algorithms, by decoupling the inference of throughput dynamics (referred to as latent encoder) from the universal control mechanism that is shared by all poten- tial throughput dynamics (referred to as meta-policy network). • To ensure rapid adaptation to time-varying yet indistinguishable throughput dynamics in real-world scenarios, we propose an efficient meta-policy search scheme for the mixed dynamics, which includes the use of on-policy RL algorithms (or imitation learning) to alleviate estimation bias for value function, and a mutual information-based regularization in the policy loss to make the latent variable more informative about the policy.

**Fragmento 25 - p. 3 - score 1:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal as a Markov decision process (MDP), with the state 𝑠𝑘∈S for downloading the chunk 𝑈𝑘represented by six features, namely the measured 1) average throughput 𝐶𝑘−1 and 2) corresponding download time 𝑑𝑘−1, 3) the vector of chunk sizes associated with available bitrate versions for the 𝑘-th video chunk: 𝐸= {𝐸𝑘𝑎1, 𝐸𝑘𝑎2, · · · , 𝐸𝑘𝑎𝑀}, 4) current buffer occupancy 𝐵𝑘−1, 5) selected bitrate 𝑎𝑘−1 of the last video chunk, and 6) the remaining number of video chunks that have not been downloaded yet. To quantify the user’s QoE, we employ a widely used objective metric that incorporates the trade-off between video quality, quality fluctuation and risk of rebuffering events as a linear combination: 𝑟(𝑠𝑘,𝑎𝑘) = 𝑞(𝑎𝑘) −𝛼 𝑞(𝑎𝑘) −𝑞(𝑎𝑘−1)  −𝛽(𝑑𝑘−𝐵𝑘−1)+ , (2) where 𝑟∈𝑅, 𝑞(𝑎𝑘) can be any video quality metric (e.g., PSNR and SSIM), and 𝛼and 𝛽are a non-negative penalty weight that ensures the temporal quality smoothness and penalizes the rebuffering delay, respectively.

**Fragmento 26 - p. 3 - score 1:**

Therefore, the control policy of the ABR algorithm can be derived by solving a sequential decision-making problem that optimizes the average chunk QoE for the user under a constrained yet time-varying network throughput: 𝑎∗ 𝑘= arg max 𝑎 1 𝐾 𝐾 𝑘=0 𝑟(𝑠𝑘,𝑎𝑘), (3a) s.t. 𝑠𝑘+1 = 𝑓(𝑠𝑘,𝑎𝑘), 𝑎𝑘∈A, (3b) where the dynamics model 𝑓: S × A →S of the video streaming system includes the buffer occupancy as given in Eq. (1), as well as the dynamics of network throughput which unfortunately cannot be explicitly represented or predicted. As such, we are theoretically unable to find the global optimal solution of Eq. (3), but endeavour in practice to approach as closer as possible to this global optimum. 2.2 Learning How to Learn Bitrate Adaptation As a result, the MDP of an adaptive video streaming system can be formulated as < S, A, 𝑃, 𝑅>, where 𝑃= 𝑝(𝑠𝑘+1|𝑠𝑘,𝑎𝑘) is the state transition probability that mainly depends on the dynamics of network throughput.


### 7.9. limitaciones riesgos coste

Palabras clave usadas: `limitation, limitations, future work, challenge, challenges, overhead, complexity, compute, GPU, CPU, deployment, real-world, generalization, out-of-distribution, OOD, unstable, fail, bias, sensitive, prediction error, horizon, scalability`

**Fragmento 1 - p. 5 - score 5:**

, (7) 𝜌(𝜃) = 𝜋𝜃(𝒂|𝒔, 𝒛)/𝜋𝜃′(𝒂|𝒔, 𝒛), 𝒛∼𝑞𝜙(𝒛|𝒄) where𝜃′ denotes the previous values of𝜃following the latest update epoch, clip[𝜌(𝜃), 1 −𝜖, 1 + 𝜖] ensures no incentive for moving 𝜌(𝜃) outside the interval [1−𝜖, 1+𝜖], and ˆ𝐴is the truncated generalized advantage estimation (GAE) function [18] generated from the value function 𝑉𝜃𝑣(𝒔, 𝒛) and 𝒓. Similarly, the critic loss is formulated as: L𝜃𝑣(𝒄,𝝉) = 1 2E¯𝒛  (𝑉𝜃𝑣(𝒔, ¯𝒛) −𝐺𝑘)2 , ¯𝒛∼𝑞𝜙(𝒛|𝒄), (8) where 𝐺𝑘= 𝑟𝑘+ 𝛾𝑟𝑘+1 + 𝛾2𝑟𝑘+2 + · · · is the rollout QoE return of the current state following 𝜋𝜃′(𝒂|𝒔, 𝒛),𝛾∈(0, 1] is a discount factor that attenuates exponentially the impact of future actions over the current expected QoE, and ¯𝒛indicates that gradients are not being computed through it. 4.2 Imitation Learning-Based Pre-Training In practice, due to the low sample efficiency of RL training [15], training the meta-RL from scratch is exceedingly time expensive and unstable in our setting of mixed dynamics. Therefore, we pre-train the parameters 𝜙and 𝜃following the imitation learning method proposed in [7], with a behavior cloning objective for the actor and inference networks: max 𝜃,𝜙 E𝒛, ˆ𝒂log 𝜋𝜃( ˆ𝒂|𝒔, 𝒛), 𝒛∼𝑞𝜙(𝒛|𝒄), ˆ𝒂∼𝜋𝑒(𝒂|𝒔), (9) where the model-based ABR algorithm RobustMPC [24] is adopted to obtain the expert policy 𝜋𝑒(𝒂|𝒔), with the QoE maximized over a horizon of future 3 chunks. Here, we skip the pre-training of critic network, since 𝜃𝑣may be rapidly converged with only a few trials following the policy 𝜋𝜃(𝒂|𝒔, 𝒛). Notably, we employ RobustMPC here primarily for its good QoE performance and low computational complexity, which will be also justified by the experimental evaluations in Section 5. However, variants of MERINA can be easily fulfilled by adopting other existing ABR algorithms to obtain the expert policy, resulting in a difference on the training time and overall QoE performance. In summary, the entire meta-training and meta-adaptation workflow of MERINA is given in Algorithm 1 and Algorithm 2, Algorithm 1 Meta-training Procedure of MERINA Require: Dynamics model 𝑓of the video streaming system with time-varying and heterogeneous network dynamics, learning rates 𝛼1, 𝛼2, 𝛼3 // First stage: pre-training with ex

**Fragmento 2 - p. 2 - score 3:**

• We study the generalization problem of adaptive video streaming, and formulate the rate adaptation problem as a POMDP, rather than previously stated MDP. We then propose a model-free system framework based on context-based meta-RL to improve generalization for neural ABR algorithms, by decoupling the inference of throughput dynamics (referred to as latent encoder) from the universal control mechanism that is shared by all poten- tial throughput dynamics (referred to as meta-policy network). • To ensure rapid adaptation to time-varying yet indistinguishable throughput dynamics in real-world scenarios, we propose an efficient meta-policy search scheme for the mixed dynamics, which includes the use of on-policy RL algorithms (or imitation learning) to alleviate estimation bias for value function, and a mutual information-based regularization in the policy loss to make the latent variable more informative about the policy.

**Fragmento 3 - p. 2 - score 3:**

• We implement MERINA’s meta-training and meta-adaptation procedures, and validate its improved generalization capability through numerous empirical evaluations on different QoE metrics and multiple datasets containing real-world network throughput traces, as well as a real-world test. These evaluations demonstrate that MERINA outperforms the state-of-the-art ABR algorithms in terms of both the average chunk QoE on the in-distribution throughput traces, and the capability of generalization and quick adaptation on the out-of-distribution throughput traces. 2 BACKGROUND AND MOTIVATION 2.1 Problem Formulation In a typical adaptive video streaming system, the video is temporally divided into 𝐾chunks (i.e., segments) with a fixed time duration 𝐿.

**Fragmento 4 - p. 7 - score 3:**

The results on out-of- distribution datasets (Oboe, Puffer-Oct.17-21 and Puffer-Feb.18- 22) reveal that the NN weights trained in F&H datasets using MERINA provide the highest degree of consistency or generalization performance among the learning-based baselines, over all ranges of varying throughput dynamics. The heuristic ABR algorithms (BOLA and RobustMPC) can always achieve a satisfactory QoE performance on different throughput dynamics, while BOLA beats all the other algorithms on Puffer-Oct.17-21 traces where the throughput dynamics are difficult to predict and considerably deviate from those on the F&H traces. In contrast, the other learning-based methods fail to generalize to the out-of-distribution datasets, verifying the generalization difficulty of DRL or imitation learning-based neural ABR algorithms.

**Fragmento 5 - p. 8 - score 3:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. 0 0.5 1 1.5 2 2.5 3 4G Public WiFi International Link Average value BOLA RobustMPC Comyco MERINA Figure 3: Comparison of 𝑄𝑜𝐸𝑙𝑜𝑔without adaption. NNs to learn the throughput dynamics have a better consistency or generalization than Pensieve and Comyco, though they also perform much worse on Puffer traces than heuristic methods. This demonstrates that, besides meta-RL-based methods, model-based methods are another viable paradigm for addressing the general- ization challenge of adaptive video streaming. In conclusion, our MERINA performs consistently with out-of-distribution throughput dynamics, though it may have a worse QoE than BOLA in some sessions.

**Fragmento 6 - p. 1 - score 2:**

Finally, we implement our algorithm’s meta-training and meta-adaptation procedures under a variety of throughput dynamics. Empirical evaluations on different QoE metrics and multiple datasets containing real-world network traces demonstrate that our algorithm outperforms state-of-the-art ABR algorithms, in terms of the performance on the average chunk QoE, consistency and fast adaptation across a wide range of throughput patterns. CCS CONCEPTS • Information systems →Multimedia streaming; • Comput- ing methodologies →Sequential decision making. KEYWORDS Rate adaptation, meta deep reinforcement learning, generalization. ACM Reference Format: Nuowen Kan, Yuankun Jiang, Chenglin Li, Wenrui Dai, Junni Zou, and Hongkai Xiong.

**Fragmento 7 - p. 1 - score 2:**

In addition, the ABR algorithm in practice is also expected to be able to implement quickly online, because a higher overhead of inference time for rate adaptation will inevitably increase the end-to-end latency. To address this challenge, Yin et al. in [24] argued that the model predictive control (MPC) approach is a natural fit for the rate adaptation problem and proposed two simple yet effective algorithms, namely RobustMPC and FastMPC, based on the pre- diction of future network throughput with the harmonic mean of past throughput. Following this principle, various studies (e.g., CS2P[22], BayesMPC[10], Fugu[23]) have been proposed to seek for a higher QoE by improving the throughput prediction accuracy.

**Fragmento 8 - p. 1 - score 2:**

The weakness of these MPC-based methods is that they would suffer from issues such as inevitable bias in throughput prediction and high computational complexity in real world implementation, which are then alleviated by learning-based methods. By exploiting the strong non-linear fitting capability of neural networks (NNs), these learning-based methods are able to directly achieve a superior 3006

**Fragmento 9 - p. 2 - score 2:**

However, the superior performance of existing neural ABR algo- rithms is subject to certain conditions, such as that the probability of state transition (i.e., 𝒔′ = 𝑓(𝒔, 𝒂) with 𝑓being the dynamics transition function) is identical or similar between the training and deployment environments. This condition is unfortunately not satisfied in many real-world scenarios, possibly resulting in a poor consistency of neural ABR algorithm’s performance across a range of network throughput patterns [1, 10, 13, 23]. Though a lifelong learning method was proposed in [7] to address this issue by continuously fine-tuning the NNs with new throughput data online, it is still not a natural choice for neural ABR algorithms, since NNs trained with certain known dynamics will lose their ability to quickly fit to new dynamics over time [12].

**Fragmento 10 - p. 3 - score 2:**

policy that performs well if the distribution of throughput dynamics has been experienced in the training dataset, but may unfortunately present a very poor generalization in unseen (or out-of-distribution) network contexts. Meta-RL, as a popular method for fast adaptation to unseen environments, trains an agent from multiple sample tasks to construct a meta-policy over the shared structure across tasks [3, 16]. We are therefore motivated to propose MERINA, a context- based meta-RL approach for decoupling inference of underlying network dynamics 𝒛from the universal control mechanism. Other than learning a separate ABR control policy for each possible network throughput dynamic from millions of samples, we would like our ABR agent to discover a common control mechanism (i.e., meta-policy 𝜋(𝒂|𝒔, 𝒛)) shared across a range of possible throughput dynamics during the training.

**Fragmento 11 - p. 4 - score 2:**

We also assume the Gaussian posterior over 𝑍 and employ the Gaussian factor 𝑞𝜙(𝒛|𝒄) = N (𝑓𝜇 𝜙(𝒄), 𝑓𝜎 𝜙(𝒄)), which make the proposed method tractable. As a function of the context, 𝑓(·) 𝜙 (𝒄) predicts the mean 𝜇and variance 𝜎for 𝑞𝜙(𝒛|𝒄), respectively. Therefore, the inference of network throughput dynamics can be done by sampling latent variable 𝒛from the posterior distribution 𝑞𝜙(𝒛|𝒄). This posterior can reason about uncertainty associated with the dynamics inference, particularly in light of the fact that the underlying throughput dynamics are difficult to identify due to the scarcity of data samples, i.e., epistemic uncertainty. Probabilistic sampling reduces the risk of biased latent representation, thus increasing the generalization capability of control policies.

**Fragmento 12 - p. 6 - score 2:**

5) Fugu [23]: a model- based algorithm that uses NN-based transmission time predictor to predict the probability distribution of download times per bitrate version for future ℎchunks, and optimizes the bitrate selection via calculating the expectation of maximum future ℎ-horizon QoE return. 6) BayesMPC [10]: a model-based algorithm that uses Bayesian NNs to predict the lower bound of future throughputs, based on which a model predictive control is further employed to optimize the future ℎ-horizon QoE return. Note that Fugu is proposed to learn in situ, which is also proposed in [23] and said to be a more sound virtual player than the one employed in our paper. Due to the fact that the simulation platform has little effect on the success of MERINA in terms of generalization, we choose the virtual player that is widely deployed in the majority of prior works.

**Fragmento 13 - p. 10 - score 2:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. Appendix A IMPLEMENTATION DETAILS We implement MERINA on a desktop equipped with a 40-core Intel Xeon Silver 4114 Processor, 64GB DDR4 DRAM and an NVIDIA GeForce RTX 2080 graphics card. The inference neural network and the policy neural network that consists of an actor network and a critic network are constructed and trained on PyTorch-1.9.0. Note that we train MERINA on the GPU to maximize the efficiency, though it can be trained on CPUs as well. A.1 Inference Network The throughput context 𝒄𝑘−𝑝:𝑘= {(𝐶𝑘−𝑝,𝑑𝑘−𝑝), · · · , (𝐶𝑘−1,𝑑𝑘−1)} includes the average throughput values and time intervals of throughput measurements collected from the download of previous 𝑝chunks.

**Fragmento 14 - p. 11 - score 2:**

These real-world test for 𝑄𝑜𝐸𝑙𝑖𝑛still can demonstrate the generalization capability of MERINA when deployed in the real-world scenarios. B.2 Fast Adaptation To New Environments Though MERINA performs slightly worse than BOLA in terms of the average chunk QoE value on the throughput dynamics of Puffer-Oct.17-21 when using the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛, we examine here MERINA’s ability to rapidly adapt to this dataset and study how much improvement can be achieved through adaptation. All the settings w.r.t. the meta-adaptation procedures are the same to those of Section 5.3, with the associated results illustrated in Fig. 6. It can be seen from Fig. 6(a) that when using the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛, MERINA can surpass BOLA (0.86) in terms of average chunk QoE value with around 100 training epochs (see MERINA-Adpt) and achieves a much higher chunk QoE value 1.10 asymptotically (see MERINA-Asy).

**Fragmento 15 - p. 11 - score 2:**

The results suggested that, after 1100- epoch adaptation, the proportion of sessions that achieve high QoE value rise significantly. B.3 Ablation Study Finally, we conduct some experiments to demonstrate the benefit to generalization as introduced by the proposed mutual information- based regularization function in Eq. (5), providing a further insight on MERINA. We train a modified version of MERINA, named MERINA (nMI), by setting 𝜆= 0 for the actor loss, on the training dateset F&H, and then evaluate its QoE performance on all the five datasets. The results of average chunk QoE achieved by MERINA (nMI) are also presented in Tables 1 and 2 for 𝑄𝑜𝐸𝑙𝑜𝑔and 𝑄𝑜𝐸𝑙𝑖𝑛, respectively, which reveal a critical finding: the mutual information- based regularizer improves the average QoE performance and generalization on both in- and out-of-distribution datasets.

**Fragmento 16 - p. 11 - score 2:**

This demonstrates that the regularization function facilitates the latent variable’s expressiveness (i.e. a more informative representation) to bitrate selection in mixed dynamics, therefore enhancing the generalization. In addition, without the imitation learning-based pre-training, the learning process of MERINA will be exceedingly unstable, and the training will always fall into a local optimum. This phenomenon may result from the probabilistic latent encoder and the mix dynamics setting in our paper. 3016

**Fragmento 17 - p. 1 - score 1:**

In general, video quality can be enhanced by assigning a higher bitrate for the chunk to be transmitted, which, however, may result in a rebuffering event (i.e., stalling during playback) especially when the network condition is poor and unstable. As a key component of rate adaptation, adaptive bitrate stream- ing (ABR) algorithms aim to solve a stochastic optimal control problem that reveals how to strike an optimal trade-off between maximizing the video quality and avoiding the rebuffering, by determining the fine-grained bitrate combination sequentially for continuously transmitted video chunks. However, due to the time- varying and heterogeneous dynamics of network throughput in real world, it is unfortunately intractable to achieve the optimal trade-off with an explicit solution.

**Fragmento 18 - p. 1 - score 1:**

2022. Improving Generalization for Neural Adaptive Video Streaming Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. MM ’22, October 10–14, 2022, Lisboa, Portugal © 2022 Association for Computing Machinery.

**Fragmento 19 - p. 1 - score 1:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning Nuowen Kan Shanghai Jiao Tong University kannw_1230@sjtu.edu.cn Yuankun Jiang Shanghai Jiao Tong University yuankunjiang@sjtu.edu.cn Chenglin Li Shanghai Jiao Tong University lcl1985@sjtu.edu.cn Wenrui Dai Shanghai Jiao Tong University daiwenrui@sjtu.edu.cn Junni Zou Shanghai Jiao Tong University zoujunni@sjtu.edu.cn Hongkai Xiong Shanghai Jiao Tong University xionghongkai@sjtu.edu.cn ABSTRACT In this paper, we present a meta reinforcement learning (Meta-RL)- based neural adaptive bitrate streaming (ABR) algorithm that is able to rapidly adapt its control policy to the changing network throughput dynamics.

**Fragmento 20 - p. 2 - score 1:**

Once deployed in environments with different throughput dynamics, the ABR policy can be learned to adapt to corresponding dynamics with only a few trials. However, due to the time-varying yet indistinguishable feature of throughput dynamics, difficulties emerges in meta-policy search on such a mixed dynamics. Therefore, we propose an efficient meta-policy search scheme, which includes using on-policy RL (or imitation learning) algorithms to alleviate the estimation bias of value function, as well as a mutual information-based regularization in the policy loss to make the latent variable more informative about the policy. Finally, we implement our proposed ABR algorithm with a meta-training procedure where a regularized proximal policy optimization (PPO) algorithm is used to train the inference network (encoder) and the latent-conditioned meta- policy by following an imitation learning-based pre-training, and a meta-adaptation procedure that aims to rapidly adapt the meta- policy to unseen throughput dynamics by using the same PPO update.

**Fragmento 21 - p. 2 - score 1:**

Empirically, we compare MERINA to other ABR baselines on different QoE metrics and real-world throughput traces, as well as a 3-hour real-world test. Evaluation results demonstrate that MERINA outperforms state-of-the-art ABR algorithms on the in-distribution traces by at least 3% in terms of average chunk QoE. On three out-of- distribution datasets and real-world test, MERINA beats all neural baselines in terms of the average chunk QoE without adaptation, presenting a performance gain of up to 26% between MERINA and the second-best algorithm, and achieves a higher average chunk QoE over all baselines with only about 200 epochs (i.e., 5 minutes) of adaptation. Our main contributions can be summarized as follows.

**Fragmento 22 - p. 3 - score 1:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal as a Markov decision process (MDP), with the state 𝑠𝑘∈S for downloading the chunk 𝑈𝑘represented by six features, namely the measured 1) average throughput 𝐶𝑘−1 and 2) corresponding download time 𝑑𝑘−1, 3) the vector of chunk sizes associated with available bitrate versions for the 𝑘-th video chunk: 𝐸= {𝐸𝑘𝑎1, 𝐸𝑘𝑎2, · · · , 𝐸𝑘𝑎𝑀}, 4) current buffer occupancy 𝐵𝑘−1, 5) selected bitrate 𝑎𝑘−1 of the last video chunk, and 6) the remaining number of video chunks that have not been downloaded yet. To quantify the user’s QoE, we employ a widely used objective metric that incorporates the trade-off between video quality, quality fluctuation and risk of rebuffering events as a linear combination: 𝑟(𝑠𝑘,𝑎𝑘) = 𝑞(𝑎𝑘) −𝛼 𝑞(𝑎𝑘) −𝑞(𝑎𝑘−1)  −𝛽(𝑑𝑘−𝐵𝑘−1)+ , (2) where 𝑟∈𝑅, 𝑞(𝑎𝑘) can be any video quality metric (e.g., PSNR and SSIM), and 𝛼and 𝛽are a non-negative penalty weight that ensures the temporal quality smoothness and penalizes the rebuffering delay, respectively.

**Fragmento 23 - p. 3 - score 1:**

Encountering a new network environment, this latent variable 𝒛can reason about dynamics uncertainty, allowing for a stochastic exploration of meta-learned policy to explore states with potentially higher rewards while also quickly adapting to the new dynamics. Meanwhile, sampling the latent variable from a probabilistic distribution improves the generalization of control policies when a deterministic inference of dynamics is difficult. • 2) Latent-conditioned policy network (i.e., policy search). To identify a universal ABR control policy capable of adapting its behavior to the network throughput dynamics, we set a 𝜃- parameterized policy 𝜋𝜃(𝒂|𝒔, 𝒛) as conditioned on the latent variable 𝒛. Thus, if the latent variable 𝒛can be reliably inferred from the recent experience, the resulting policy 𝜋𝜃(𝒂|𝒔, 𝒛) will potentially adapt to a new network environment.

**Fragmento 24 - p. 4 - score 1:**

In general, RL algorithms improve the policy by utilizing trajectories experienced with the same dynamics transition probability 𝑃, while meta-RL does the same by optimizing the policy for each different task or dynamic in turn. However, because of the time-varying characteristic of throughput dynamics, the trajectories (𝒄,𝝉) in our mixed dynamics situation cannot guarantee to have the same transition probability 𝑝(𝑠𝑘+1|𝑠𝑘,𝑎𝑘,𝑧𝑘). Thus, in our setting off-policy RL algorithms, such as SAC [6], will introduce more bias into estimating the value function than on-policy RL algorithms. This is because the off-policy algorithms cannot estimate the value function of target policy by reusing the trajectories explored by any other behavior policy that has encountered different types of underlying dynamics.

**Fragmento 25 - p. 4 - score 1:**

Thus, we are unable to sample (𝒄,𝝉) pairs that belong to the same dynamics in Eq. (4), which is different from the typical setting used in most of previous works. We must calculate the expectation in Eq. (4) over trajectories sampled from the mixed dynamics, which complicates the process of meta-policy search for each throughput dynamic. 3.2 Meta-Policy Search on Mixed Dynamics To address the challenge raised by mixed dynamics, we explore the types of policy search methods that can be employed in this situation, and then design a mutual information-based regulariza- tion to make the latent variable more informative about the bitrate selection strategy. The policy network approximates the mapping from the latent variable and the state to an optimal ABR control policy 𝜋𝜃(𝒂|𝒔, 𝒛) : S × 𝑍↦→A.

**Fragmento 26 - p. 5 - score 1:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal ∇𝐽/∇𝜙= ∇𝐽/∇𝒛· ∇𝒛/∇𝜙. Note that we can pass the gradient from the policy network to inference network with the Gaussian re- parameterization trick [11], even though the latent variable input of policy network is sampled from the output of inference network, i.e., 𝒛∼𝑞𝜙(𝒛|𝒄). 4 IMPLEMENTATION 4.1 Meta-Policy Search with DRL To enable an effective policy search, we build up our algorithm on top of the proximal policy optimization (PPO) algorithm [19], a well known on-policy actor-critic method recognized for its reliable performance on policy improvement with trust region policy optimization. With PPO, we construct two networks: an actor network 𝜋𝜃(𝒂|𝒔, 𝒛) and a critic network 𝑉𝜃𝑣(𝒔, 𝒛). We jointly train the inference and actor networks to maximize the actor loss and the regularization I(𝒂; 𝒛|𝒔) on the parameters of 𝜃and 𝜙. As a result, the objective ˜𝐽𝜃(𝒄,𝝉) of the actor network is expressed as: ˜𝐽𝜃(𝒄,𝝉) = E𝒛


### 7.10. ideas fase45 v1 controller defendible

Palabras clave usadas: `risk, safe, safety, robust, conservative, fallback, uncertainty, capacity, lower bound, tail, severe, low buffer, volatile, variable, fluctuation, drop, zero, consistent, smoothness, auto-tuning, regime, cluster, guidance, hybrid, generalization, environment-aware, prediction, selector`

**Fragmento 1 - p. 3 - score 4:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal as a Markov decision process (MDP), with the state 𝑠𝑘∈S for downloading the chunk 𝑈𝑘represented by six features, namely the measured 1) average throughput 𝐶𝑘−1 and 2) corresponding download time 𝑑𝑘−1, 3) the vector of chunk sizes associated with available bitrate versions for the 𝑘-th video chunk: 𝐸= {𝐸𝑘𝑎1, 𝐸𝑘𝑎2, · · · , 𝐸𝑘𝑎𝑀}, 4) current buffer occupancy 𝐵𝑘−1, 5) selected bitrate 𝑎𝑘−1 of the last video chunk, and 6) the remaining number of video chunks that have not been downloaded yet. To quantify the user’s QoE, we employ a widely used objective metric that incorporates the trade-off between video quality, quality fluctuation and risk of rebuffering events as a linear combination: 𝑟(𝑠𝑘,𝑎𝑘) = 𝑞(𝑎𝑘) −𝛼 𝑞(𝑎𝑘) −𝑞(𝑎𝑘−1)  −𝛽(𝑑𝑘−𝐵𝑘−1)+ , (2) where 𝑟∈𝑅, 𝑞(𝑎𝑘) can be any video quality metric (e.g., PSNR and SSIM), and 𝛼and 𝛽are a non-negative penalty weight that ensures the temporal quality smoothness and penalizes the rebuffering delay, respectively.

**Fragmento 2 - p. 4 - score 4:**

We also assume the Gaussian posterior over 𝑍 and employ the Gaussian factor 𝑞𝜙(𝒛|𝒄) = N (𝑓𝜇 𝜙(𝒄), 𝑓𝜎 𝜙(𝒄)), which make the proposed method tractable. As a function of the context, 𝑓(·) 𝜙 (𝒄) predicts the mean 𝜇and variance 𝜎for 𝑞𝜙(𝒛|𝒄), respectively. Therefore, the inference of network throughput dynamics can be done by sampling latent variable 𝒛from the posterior distribution 𝑞𝜙(𝒛|𝒄). This posterior can reason about uncertainty associated with the dynamics inference, particularly in light of the fact that the underlying throughput dynamics are difficult to identify due to the scarcity of data samples, i.e., epistemic uncertainty. Probabilistic sampling reduces the risk of biased latent representation, thus increasing the generalization capability of control policies.

**Fragmento 3 - p. 3 - score 3:**

Encountering a new network environment, this latent variable 𝒛can reason about dynamics uncertainty, allowing for a stochastic exploration of meta-learned policy to explore states with potentially higher rewards while also quickly adapting to the new dynamics. Meanwhile, sampling the latent variable from a probabilistic distribution improves the generalization of control policies when a deterministic inference of dynamics is difficult. • 2) Latent-conditioned policy network (i.e., policy search). To identify a universal ABR control policy capable of adapting its behavior to the network throughput dynamics, we set a 𝜃- parameterized policy 𝜋𝜃(𝒂|𝒔, 𝒛) as conditioned on the latent variable 𝒛. Thus, if the latent variable 𝒛can be reliably inferred from the recent experience, the resulting policy 𝜋𝜃(𝒂|𝒔, 𝒛) will potentially adapt to a new network environment.

**Fragmento 4 - p. 4 - score 3:**

In the following, we will often write 𝒄𝑘−𝑝:𝑘as 𝒄for notational simplicity. Due to the time-varying nature of the underlying network throughput dynamics, we only collect the past experience from the most recent 𝑝chunks, rather than from the beginning of video playback. Additionally, we make the assumption that the true chunk sizes will remain relatively constant throughout all video chunks for each bitrate version, thus omitting the dynamics inference for video content. To approximate the posterior 𝑝(𝒛|𝒄) over latent variable space 𝑍, we build up an inference network that generates the distribution 𝑞𝜙(𝒛|𝒄) parameterized by 𝜙. This inference network can be trained via a model-free manner by using the method described in [16], with the goal of directly maximizing a variational lower bound: E(𝒄,𝝉)∼B  𝐽(𝒄,𝝉) + 𝛽𝐷KL 𝑞𝜙(𝒛|𝒄)||𝑝(𝒛) , (4) where 𝑝(𝒛) is a unit Gaussian prior over 𝑍, and 𝐽(𝒄,𝝉) may be any objective chosen from a variety of those for policy search, with 𝝉= {𝒔, 𝒂, 𝒓} being corresponding samples, as will be detailed in Sections 3.2 and 4.

**Fragmento 5 - p. 7 - score 3:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal #FUUFS (a) 𝑄𝑜𝐸𝑙𝑖𝑛 #FUUFS (b) 𝑄𝑜𝐸𝑙𝑖𝑛 0 0.2 0.4 0.6 0.8 1 1.2 1.4 Chunk QoE Bitrate utility Rebuffering penalty Smoothness penalty Averagevalue BOLA RobustMPC Pensieve Comyco Fugu BayesMPC MERINA (c) 𝑄𝑜𝐸𝑙𝑖𝑛 #FUUFS (d) 𝑄𝑜𝐸𝑙𝑜𝑔 #FUUFS (e) 𝑄𝑜𝐸𝑙𝑜𝑔 0 0.2 0.4 0.6 0.8 1 1.2 1.4 Chunk QoE Bitrate utility Rebuffering penalty Smoothness penalty Averagevalue BOLA RobustMPC Pensieve Comyco Fugu BayesMPC MERINA (f) 𝑄𝑜𝐸𝑙𝑜𝑔 Figure 2: Performance comparison of different ABR algorithms in terms of the average chunk QoE value and the individual QoE components with the QoE metrics 𝑄𝑜𝐸𝑙𝑖𝑛and 𝑄𝑜𝐸𝑙𝑜𝑔on F&H (FCC and HSDPA) throughput dataset.

**Fragmento 6 - p. 8 - score 3:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. 0 0.5 1 1.5 2 2.5 3 4G Public WiFi International Link Average value BOLA RobustMPC Comyco MERINA Figure 3: Comparison of 𝑄𝑜𝐸𝑙𝑜𝑔without adaption. NNs to learn the throughput dynamics have a better consistency or generalization than Pensieve and Comyco, though they also perform much worse on Puffer traces than heuristic methods. This demonstrates that, besides meta-RL-based methods, model-based methods are another viable paradigm for addressing the general- ization challenge of adaptive video streaming. In conclusion, our MERINA performs consistently with out-of-distribution throughput dynamics, though it may have a worse QoE than BOLA in some sessions.

**Fragmento 7 - p. 1 - score 2:**

In addition, the ABR algorithm in practice is also expected to be able to implement quickly online, because a higher overhead of inference time for rate adaptation will inevitably increase the end-to-end latency. To address this challenge, Yin et al. in [24] argued that the model predictive control (MPC) approach is a natural fit for the rate adaptation problem and proposed two simple yet effective algorithms, namely RobustMPC and FastMPC, based on the pre- diction of future network throughput with the harmonic mean of past throughput. Following this principle, various studies (e.g., CS2P[22], BayesMPC[10], Fugu[23]) have been proposed to seek for a higher QoE by improving the throughput prediction accuracy.

**Fragmento 8 - p. 2 - score 2:**

• We study the generalization problem of adaptive video streaming, and formulate the rate adaptation problem as a POMDP, rather than previously stated MDP. We then propose a model-free system framework based on context-based meta-RL to improve generalization for neural ABR algorithms, by decoupling the inference of throughput dynamics (referred to as latent encoder) from the universal control mechanism that is shared by all poten- tial throughput dynamics (referred to as meta-policy network). • To ensure rapid adaptation to time-varying yet indistinguishable throughput dynamics in real-world scenarios, we propose an efficient meta-policy search scheme for the mixed dynamics, which includes the use of on-policy RL algorithms (or imitation learning) to alleviate estimation bias for value function, and a mutual information-based regularization in the policy loss to make the latent variable more informative about the policy.

**Fragmento 9 - p. 4 - score 2:**

MM ’22, October 10–14, 2022, Lisboa, Portugal Nuowen Kan et al. policy-gradient RL or imitation learning. However, the training data contain too many different types of underlying network dynamics to enable an informative latent representation about the policy. To solve this issue, a mutual information-based regularization is further proposed, in addition to the basic loss function. 3.1 Modeling the Uncertainty of Inference To facilitate adaptation, the latent variable 𝒛should encode an effective representation of the current network throughput dy- namics by exploiting a collection of past experienced network throughputs. Here, we define the throughput context as 𝒄𝑘−𝑝:𝑘= {(𝐶𝑘−𝑝,𝑑𝑘−𝑝), · · · , (𝐶𝑘−1,𝑑𝑘−1)}, which consists of the average throughput values and time intervals of throughput measurements collected from the download of chunk 𝑈𝑘−𝑝to chunk 𝑈𝑘−1.

**Fragmento 10 - p. 5 - score 2:**

, (7) 𝜌(𝜃) = 𝜋𝜃(𝒂|𝒔, 𝒛)/𝜋𝜃′(𝒂|𝒔, 𝒛), 𝒛∼𝑞𝜙(𝒛|𝒄) where𝜃′ denotes the previous values of𝜃following the latest update epoch, clip[𝜌(𝜃), 1 −𝜖, 1 + 𝜖] ensures no incentive for moving 𝜌(𝜃) outside the interval [1−𝜖, 1+𝜖], and ˆ𝐴is the truncated generalized advantage estimation (GAE) function [18] generated from the value function 𝑉𝜃𝑣(𝒔, 𝒛) and 𝒓. Similarly, the critic loss is formulated as: L𝜃𝑣(𝒄,𝝉) = 1 2E¯𝒛  (𝑉𝜃𝑣(𝒔, ¯𝒛) −𝐺𝑘)2 , ¯𝒛∼𝑞𝜙(𝒛|𝒄), (8) where 𝐺𝑘= 𝑟𝑘+ 𝛾𝑟𝑘+1 + 𝛾2𝑟𝑘+2 + · · · is the rollout QoE return of the current state following 𝜋𝜃′(𝒂|𝒔, 𝒛),𝛾∈(0, 1] is a discount factor that attenuates exponentially the impact of future actions over the current expected QoE, and ¯𝒛indicates that gradients are not being computed through it. 4.2 Imitation Learning-Based Pre-Training In practice, due to the low sample efficiency of RL training [15], training the meta-RL from scratch is exceedingly time expensive and unstable in our setting of mixed dynamics. Therefore, we pre-train the parameters 𝜙and 𝜃following the imitation learning method proposed in [7], with a behavior cloning objective for the actor and inference networks: max 𝜃,𝜙 E𝒛, ˆ𝒂log 𝜋𝜃( ˆ𝒂|𝒔, 𝒛), 𝒛∼𝑞𝜙(𝒛|𝒄), ˆ𝒂∼𝜋𝑒(𝒂|𝒔), (9) where the model-based ABR algorithm RobustMPC [24] is adopted to obtain the expert policy 𝜋𝑒(𝒂|𝒔), with the QoE maximized over a horizon of future 3 chunks. Here, we skip the pre-training of critic network, since 𝜃𝑣may be rapidly converged with only a few trials following the policy 𝜋𝜃(𝒂|𝒔, 𝒛). Notably, we employ RobustMPC here primarily for its good QoE performance and low computational complexity, which will be also justified by the experimental evaluations in Section 5. However, variants of MERINA can be easily fulfilled by adopting other existing ABR algorithms to obtain the expert policy, resulting in a difference on the training time and overall QoE performance. In summary, the entire meta-training and meta-adaptation workflow of MERINA is given in Algorithm 1 and Algorithm 2, Algorithm 1 Meta-training Procedure of MERINA Require: Dynamics model 𝑓of the video streaming system with time-varying and heterogeneous network dynamics, learning rates 𝛼1, 𝛼2, 𝛼3 // First stage: pre-training with ex

**Fragmento 11 - p. 5 - score 2:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal ∇𝐽/∇𝜙= ∇𝐽/∇𝒛· ∇𝒛/∇𝜙. Note that we can pass the gradient from the policy network to inference network with the Gaussian re- parameterization trick [11], even though the latent variable input of policy network is sampled from the output of inference network, i.e., 𝒛∼𝑞𝜙(𝒛|𝒄). 4 IMPLEMENTATION 4.1 Meta-Policy Search with DRL To enable an effective policy search, we build up our algorithm on top of the proximal policy optimization (PPO) algorithm [19], a well known on-policy actor-critic method recognized for its reliable performance on policy improvement with trust region policy optimization. With PPO, we construct two networks: an actor network 𝜋𝜃(𝒂|𝒔, 𝒛) and a critic network 𝑉𝜃𝑣(𝒔, 𝒛). We jointly train the inference and actor networks to maximize the actor loss and the regularization I(𝒂; 𝒛|𝒔) on the parameters of 𝜃and 𝜙. As a result, the objective ˜𝐽𝜃(𝒄,𝝉) of the actor network is expressed as: ˜𝐽𝜃(𝒄,𝝉) = E𝒛

**Fragmento 12 - p. 6 - score 2:**

5) Fugu [23]: a model- based algorithm that uses NN-based transmission time predictor to predict the probability distribution of download times per bitrate version for future ℎchunks, and optimizes the bitrate selection via calculating the expectation of maximum future ℎ-horizon QoE return. 6) BayesMPC [10]: a model-based algorithm that uses Bayesian NNs to predict the lower bound of future throughputs, based on which a model predictive control is further employed to optimize the future ℎ-horizon QoE return. Note that Fugu is proposed to learn in situ, which is also proposed in [23] and said to be a more sound virtual player than the one employed in our paper. Due to the fact that the simulation platform has little effect on the success of MERINA in terms of generalization, we choose the virtual player that is widely deployed in the majority of prior works.

**Fragmento 13 - p. 7 - score 2:**

Furthermore, the bar graphs in Figs. 2(c) and 2(f) indicate that MERINA can surprisingly achieve low rebuffering and smoothness penalties, similar to those of Pensieve. While other algorithms result in either a longer rebuffering time, as Comyco does, or a higher quality fluctuation, as BOLA does, during the video playback. Note that the results obtained for linear QoE metric 𝑄𝑜𝐸𝑙𝑖𝑛are similar to those for log-form QoE metric 𝑄𝑜𝐸𝑙𝑜𝑔w.r.t. all comparison algorithms. Therefore, we only show and compare the performance for 𝑄𝑜𝐸𝑙𝑜𝑔in the following, and move results of 𝑄𝑜𝐸𝑙𝑖𝑛to Appendix B due to page limit. 5.2 Consistency on Out-of-Distribution Traces To study the consistency of MERINA in comparison to other learning-based methods, we measure their performance on out- of-distribution datasets Oboe, Puffer-Oct.17-21 and Puffer-Feb.18- 22 (i.e., with a different distribution of throughput dynamics than F&H dataset) by using the same NN weights obtained in Section 5.1 (i.e., learned from the F&H dataset).

**Fragmento 14 - p. 7 - score 2:**

The results on out-of- distribution datasets (Oboe, Puffer-Oct.17-21 and Puffer-Feb.18- 22) reveal that the NN weights trained in F&H datasets using MERINA provide the highest degree of consistency or generalization performance among the learning-based baselines, over all ranges of varying throughput dynamics. The heuristic ABR algorithms (BOLA and RobustMPC) can always achieve a satisfactory QoE performance on different throughput dynamics, while BOLA beats all the other algorithms on Puffer-Oct.17-21 traces where the throughput dynamics are difficult to predict and considerably deviate from those on the F&H traces. In contrast, the other learning-based methods fail to generalize to the out-of-distribution datasets, verifying the generalization difficulty of DRL or imitation learning-based neural ABR algorithms.

**Fragmento 15 - p. 8 - score 2:**

The results indicate that after 30-epoch adaptation, the proportion of sessions that achieve much lower/higher QoE value than RobustMPC significantly decreases/increases. And after 200-epochs adaptation, MERINA has a similar distribution to BOLA, in terms of average QoE improvement. While Comyco’s performance cannot be improved rapidly due to its low initial performance, and also because the lifelong learning method cannot ensure policy improvement in a significantly changed environment. The asymptotic performance of MERINA indicates that it can achieve a superior QoE performance when compared to all baselines following a meta-adaptation pro- cedure, implying that MERINA can achieve the best generalization performance and will outperform baseline algorithms across a range of throughput dynamics through the adaptation.

**Fragmento 16 - p. 9 - score 2:**

2020. Quality-Aware Neural Adaptive Video Streaming With Lifelong Imitation Learning. IEEE Journal on Selected Areas in Communications 38, 10 (2020), 2324–2342. [8] Tianchi Huang, Chao Zhou, Rui-Xiao Zhang, Chenglei Wu, Xin Yao, and Lifeng Sun. 2019. Comyco: Quality-Aware Adaptive Video Streaming via Imitation Learning. In Proceedings of the 27th ACM International Conference on Multimedia (Nice, France) (MM ’19). 429–437. [9] Apple Inc. 2022. HTTP Live Streaming. https://developer.apple.com/streaming/ [10] Nuowen Kan, Chenglin Li, Caiyi Yang, Wenrui Dai, Junni Zou, and Hongkai Xiong. 2021. Uncertainty-Aware Robust Adaptive Video Streaming with Bayesian Neural Network and Model Predictive Control. In Proceedings of the 31st ACM Workshop on Network and Operating Systems Support for Digital Audio and Video (Istanbul, Turkey) (NOSSDAV ’21).

**Fragmento 17 - p. 9 - score 2:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal REFERENCES [1] Zahaib Akhtar, Yun Seong Nam, Ramesh Govindan, Sanjay Rao, Jessica Chen, Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan, and Hui Zhang. 2018. Oboe: Auto-Tuning Video ABR Algorithms to Network Conditions. In Proceedings of the Conference of the ACM Special Interest Group on Data Communication. 44–58. [2] Federal Communications Commission. 2016. Raw Data - Measuring Broadband America. (2016). https://www.fcc.gov/reports-research/reports/measuring- broadband-america/raw-data-measuring-broadband-america-2016 [3] Chelsea Finn, Pieter Abbeel, and Sergey Levine.

**Fragmento 18 - p. 10 - score 2:**

The state of the video streaming system, includes the features as detailed in Section 2, is fed into the input layer of the actor and critic networks. Concretely, for the set of available bitrate versions A, we use a one-dimensional convolution layer with 128 filters, each of size 4 with stride 1, to process them. Meanwhile, five full connected layers with 128 neurons are placed at the input layer to deal with the remaining features of the state, including the measured average throughput 𝐶𝑘−1, time duration 𝑑𝑘−1 during the download of the last video chunk, current buffer occupancy 𝐵𝑘, selected bitrate 𝑎𝑘−1 of the last chunk, and the number of video chunks that have not been downloaded yet. For the latent variable sampled from the posterior 𝑞𝜙(𝒛|𝒄), we also use a fully connected layer with 1280 neurons to process the latent representations.

**Fragmento 19 - p. 10 - score 2:**

The NN weights of learning-based algorithms are the same to those used in Section. 5.1 (i.e., learned from the F&H dataset). We also present the numerical results in Table 2 by using the same format. The primary difference between the findings for 𝑄𝑜𝐸𝑙𝑜𝑔and 𝑄𝑜𝐸𝑙𝑖𝑛is that MERINA and Fugu performs better with the metric 𝑄𝑜𝐸𝑙𝑖𝑛than with the metric 𝑄𝑜𝐸𝑙𝑜𝑔on the Puffer-Oct.17-21 dataset. MERINA, in particular, achieves a comparable performance in terms of the average chunk QoE value to BOLA, which also performs best on the Puffer-Oct.17-21 dataset. These results indicate that by using the 𝑄𝑜𝐸𝑙𝑖𝑛quality metric, MERINA presents a generalization capability consistently across all the throughput dynamics in these five datasets, without the requirement of any adaptation.

**Fragmento 20 - p. 11 - score 2:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning MM ’22, October 10–14, 2022, Lisboa, Portugal Table 2: Performance comparison of different ABR algorithms in terms of the average chunk 𝑄𝑜𝐸𝑙𝑖𝑛value on different datasets. Mean ± std (𝑅𝑔𝑎𝑝) FCC HSDPA Oboe Puffer-Oct.17-21 Puffer-Feb.18-22 BOLA 0.96 ± 0.54 (−20%) 1.12 ± 0.81 (−16%) 1.96 ± 1.03 (−16%) 0.86 ± 1.83 (+1%) 0.66 ± 2.90 (−26%) RobustMPC 0.98 ± 0.75 (−18%) 1.22 ± 1.20 (−9%) 2.30 ± 1.24 (−2%) 0.73 ± 2.16 (−14%) 0.81 ± 2.97 (−9%) Pensieve 1.13 ± 0.65 (−5%) 1.28 ± 0.95 (−5%) 2.26 ± 1.15 (−4%) 0.14 ± 11.55 (−84%) 0.55 ± 8.67 (−44%) Comyco 1.15 ± 0.73 (−3%) 1.34 ± 1.05 (0%) 2.29 ± 1.21 (−2%) −0.13 ± 2.86 (−115%) 0.68 ± 3.06 (−24%) Fugu 1.11 ± 0.70 (−7%) 1.24 ± 1.04 (−7%) 2.31 ± 1.21 (−1%) 0.74 ± 2.13 (−13%) 0.83 ± 2.99 (−7%) BayesMPC 1.10 ± 0.83 (−8%) 1.26 ± 1.11 (−6%) 2.29 ± 1.23 (−2%) 0.33 ± 2.80 (−61%) 0.66 ± 3.34 (−26%) MERINA 1.19 ± 0.67 1.34 ± 0.99 2.34 ± 1.15 0.85 ± 2.02 0.90 ± 2.97 MERINA (nMI with 𝜆= 0) 1.08 ± 0.66 (−9%) 1.22 ± 1.11 (−9%) 2.25 ± 1.19 (−4%) 0.50 ± 2.68 (−61%) 0.72 ± 2.99 (−19%) Dataset distribution 1.13 ± 0.44 Mbps 1.61 ± 0.95 Mbps 2.60 ± 2.08 Mbps 1.85 ± 0.91 Mbps 1.60 ± 0.88 Mbps 0 1 2 3 4 5 4G Public WiFi International Link Average value BOLA RobustMPC Comyco MERINA Figure 5: Comparison of 𝑄𝑜𝐸𝑙𝑖𝑛without adaption.

**Fragmento 21 - p. 11 - score 2:**

This demonstrates that the regularization function facilitates the latent variable’s expressiveness (i.e. a more informative representation) to bitrate selection in mixed dynamics, therefore enhancing the generalization. In addition, without the imitation learning-based pre-training, the learning process of MERINA will be exceedingly unstable, and the training will always fall into a local optimum. This phenomenon may result from the probabilistic latent encoder and the mix dynamics setting in our paper. 3016

**Fragmento 22 - p. 1 - score 1:**

Specifically, to allow rapid adaptation, we discuss the necessity of detaching the inference of throughput dynamics with the universal control mechanism that is in essence shared by all potential throughput dynamics for neural ABR algorithms. To meta-learn the ABR policy, we then build up a model- free system framework, composed of a probabilistic latent encoder that infers the underlying dynamics from the recent throughput context, and a policy network that is conditioned on latent variable and learns to quickly adapt to new environments. Additionally, to address the difficulties caused by training the policy on mixed dynamics, on-policy RL (or imitation learning) algorithms are suggested for policy training, with a mutual information-based regularization to make the latent variable more informative about the policy.

**Fragmento 23 - p. 1 - score 1:**

2022. Improving Generalization for Neural Adaptive Video Streaming Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. MM ’22, October 10–14, 2022, Lisboa, Portugal © 2022 Association for Computing Machinery.

**Fragmento 24 - p. 1 - score 1:**

Finally, we implement our algorithm’s meta-training and meta-adaptation procedures under a variety of throughput dynamics. Empirical evaluations on different QoE metrics and multiple datasets containing real-world network traces demonstrate that our algorithm outperforms state-of-the-art ABR algorithms, in terms of the performance on the average chunk QoE, consistency and fast adaptation across a wide range of throughput patterns. CCS CONCEPTS • Information systems →Multimedia streaming; • Comput- ing methodologies →Sequential decision making. KEYWORDS Rate adaptation, meta deep reinforcement learning, generalization. ACM Reference Format: Nuowen Kan, Yuankun Jiang, Chenglin Li, Wenrui Dai, Junni Zou, and Hongkai Xiong.

**Fragmento 25 - p. 1 - score 1:**

Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning Nuowen Kan Shanghai Jiao Tong University kannw_1230@sjtu.edu.cn Yuankun Jiang Shanghai Jiao Tong University yuankunjiang@sjtu.edu.cn Chenglin Li Shanghai Jiao Tong University lcl1985@sjtu.edu.cn Wenrui Dai Shanghai Jiao Tong University daiwenrui@sjtu.edu.cn Junni Zou Shanghai Jiao Tong University zoujunni@sjtu.edu.cn Hongkai Xiong Shanghai Jiao Tong University xionghongkai@sjtu.edu.cn ABSTRACT In this paper, we present a meta reinforcement learning (Meta-RL)- based neural adaptive bitrate streaming (ABR) algorithm that is able to rapidly adapt its control policy to the changing network throughput dynamics.

**Fragmento 26 - p. 1 - score 1:**

The weakness of these MPC-based methods is that they would suffer from issues such as inevitable bias in throughput prediction and high computational complexity in real world implementation, which are then alleviated by learning-based methods. By exploiting the strong non-linear fitting capability of neural networks (NNs), these learning-based methods are able to directly achieve a superior 3006


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
Improving Generalization for Neural Adaptive Video Streaming
via Meta Reinforcement Learning
Nuowen Kan
Shanghai Jiao Tong University
kannw_1230@sjtu.edu.cn
Yuankun Jiang
Shanghai Jiao Tong University
yuankunjiang@sjtu.edu.cn
Chenglin Li
Shanghai Jiao Tong University
lcl1985@sjtu.edu.cn
Wenrui Dai
Shanghai Jiao Tong University
daiwenrui@sjtu.edu.cn
Junni Zou
Shanghai Jiao Tong University
zoujunni@sjtu.edu.cn
Hongkai Xiong
Shanghai Jiao Tong University
xionghongkai@sjtu.edu.cn
ABSTRACT
In this paper, we present a meta reinforcement learning (Meta-RL)-
based neural adaptive bitrate streaming (ABR) algorithm that is
able to rapidly adapt its control policy to the changing network
throughput dynamics. Specifically, to allow rapid adaptation, we
discuss the necessity of detaching the inference of throughput
dynamics with the universal control mechanism that is in essence
shared by all potential throughput dynamics for neural ABR
algorithms. To meta-learn the ABR policy, we then build up a model-
free system framework, composed of a probabilistic latent encoder
that infers the underlying dynamics from the recent throughput
context, and a policy network that is conditioned on latent variable
and learns to quickly adapt to new environments. Additionally, to
address the difficulties caused by training the policy on mixed
dynamics, on-policy RL (or imitation learning) algorithms are
suggested for policy training, with a mutual information-based
regularization to make the latent variable more informative about
the policy. Finally, we implement our algorithm’s meta-training
and meta-adaptation procedures under a variety of throughput
dynamics. Empirical evaluations on different QoE metrics and
multiple datasets containing real-world network traces demonstrate
that our algorithm outperforms state-of-the-art ABR algorithms, in
terms of the performance on the average chunk QoE, consistency
and fast adaptation across a wide range of throughput patterns.
CCS CONCEPTS
• Information systems →Multimedia streaming; • Comput-
ing methodologies →Sequential decision making.
KEYWORDS
Rate adaptation, meta deep reinforcement learning, generalization.
ACM Reference Format:
Nuowen Kan, Yuankun Jiang, Chenglin Li, Wenrui Dai, Junni Zou, and Hongkai
Xiong. 2022. Improving Generalization for Neural Adaptive Video Streaming
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than ACM
must be honored. Abstracting with credit is permitted. To copy otherwise, or republish,
to post on servers or to redistribute to lists, requires prior specific permission and/or a
fee. Request permissions from permissions@acm.org.
MM ’22, October 10–14, 2022, Lisboa, Portugal
© 2022 Association for Computing Machinery.
ACM ISBN 978-1-4503-9203-7/22/10...$15.00
https://doi.org/10.1145/3503161.3548331
via Meta Reinforcement Learning. In Proceedings of the 30th ACM Inter-
national Conference on Multimedia (MM ’22), October 10–14, 2022, Lisboa,
Portugal. ACM, New York, NY, USA, 11 pages. https://doi.org/10.1145/
3503161.3548331
1
INTRODUCTION
Thanks to the emerging trend that watching videos online has
become a predominant Internet application, it becomes non-
negligible to provide a better quality of experience (QoE) for users
in video streaming via rate adaptation techniques. Through online
video delivery protocols, such as dynamic adaptive streaming over
HTTP (DASH) [20] and HTTP live streaming (HLS) [9], the bitrate,
which indicates the quality or compression level for each video
chunk (or segment), can be dynamically determined to adapt to the
time-varying network throughput and current buffer occupancy of
video player. In general, video quality can be enhanced by assigning
a higher bitrate for the chunk to be transmitted, which, however,
may result in a rebuffering event (i.e., stalling during playback)
especially when the network condition is poor and unstable.
As a key component of rate adaptation, adaptive bitrate stream-
ing (ABR) algorithms aim to solve a stochastic optimal control
problem that reveals how to strike an optimal trade-off between
maximizing the video quality and avoiding the rebuffering, by
determining the fine-grained bitrate combination sequentially for
continuously transmitted video chunks. However, due to the time-
varying and heterogeneous dynamics of network throughput in
real world, it is unfortunately intractable to achieve the optimal
trade-off with an explicit solution. In addition, the ABR algorithm
in practice is also expected to be able to implement quickly online,
because a higher overhead of inference time for rate adaptation
will inevitably increase the end-to-end latency.
To address this challenge, Yin et al. in [24] argued that the
model predictive control (MPC) approach is a natural fit for the
rate adaptation problem and proposed two simple yet effective
algorithms, namely RobustMPC and FastMPC, based on the pre-
diction of future network throughput with the harmonic mean
of past throughput. Following this principle, various studies (e.g.,
CS2P[22], BayesMPC[10], Fugu[23]) have been proposed to seek
for a higher QoE by improving the throughput prediction accuracy.
The weakness of these MPC-based methods is that they would
suffer from issues such as inevitable bias in throughput prediction
and high computational complexity in real world implementation,
which are then alleviated by learning-based methods. By exploiting
the strong non-linear fitting capability of neural networks (NNs),
these learning-based methods are able to directly achieve a superior
3006
```


### Pagina 2
```text
MM ’22, October 10–14, 2022, Lisboa, Portugal
Nuowen Kan et al.
QoE performance without any iterative computation. Specifically,
formulated as a Markov decision process (MDP), neural ABR
algorithms consider the most recently recorded throughput values
and current buffer occupancy as the state 𝒔∈S, the selected
bitrate version as the action 𝒂∈A, and directly approximate
an optimal rate adaptation policy 𝜋: S →A without the
need of learning explicitly the throughput prediction. With this
intuition, many efforts have been made to provide users with a
(near)-optimal QoE, by exploiting deep reinforcement learning
(DRL)-based methods (e.g., Pensieve [14], D-DASH [5]) or imitation
learning-based methods (e.g., Comyco [7, 8]).
However, the superior performance of existing neural ABR algo-
rithms is subject to certain conditions, such as that the probability
of state transition (i.e., 𝒔′ = 𝑓(𝒔, 𝒂) with 𝑓being the dynamics
transition function) is identical or similar between the training
and deployment environments. This condition is unfortunately
not satisfied in many real-world scenarios, possibly resulting in a
poor consistency of neural ABR algorithm’s performance across
a range of network throughput patterns [1, 10, 13, 23]. Though a
lifelong learning method was proposed in [7] to address this issue
by continuously fine-tuning the NNs with new throughput data
online, it is still not a natural choice for neural ABR algorithms,
since NNs trained with certain known dynamics will lose their
ability to quickly fit to new dynamics over time [12].
In this paper, we introduce MERINA, a MEta ReInforcement
learning (Meta-RL)-based Neural ABR algorithm, which is able to
rapidly adapt its control policy to unfamiliar throughput dynamics.
Specifically, we discuss that the rate adaptation problem can be
in essence modeled as a partially observable Markov decision
process (POMDP), in which the agent is unaware of the underlying
information of throughput dynamics. To enable fast adaptation to
new throughput dynamics for neural ABR algorithms, it is necessary
to separate the dynamics inference from the universal control policy
shared by all potential state transition functions. Thus, we adopt the
context-based meta-RL method to construct a model-free system
framework, consists of a probabilistic latent encoder that infers
current throughput dynamics from recent throughput contexts,
and a meta-policy network that selects the bitrate per chunk
according to the state and sampled latent variable. Once deployed in
environments with different throughput dynamics, the ABR policy
can be learned to adapt to corresponding dynamics with only a
few trials. However, due to the time-varying yet indistinguishable
feature of throughput dynamics, difficulties emerges in meta-policy
search on such a mixed dynamics. Therefore, we propose an
efficient meta-policy search scheme, which includes using on-policy
RL (or imitation learning) algorithms to alleviate the estimation
bias of value function, as well as a mutual information-based
regularization in the policy loss to make the latent variable more
informative about the policy. Finally, we implement our proposed
ABR algorithm with a meta-training procedure where a regularized
proximal policy optimization (PPO) algorithm is used to train
the inference network (encoder) and the latent-conditioned meta-
policy by following an imitation learning-based pre-training, and
a meta-adaptation procedure that aims to rapidly adapt the meta-
policy to unseen throughput dynamics by using the same PPO
update. Empirically, we compare MERINA to other ABR baselines on
different QoE metrics and real-world throughput traces, as well as a
3-hour real-world test. Evaluation results demonstrate that MERINA
outperforms state-of-the-art ABR algorithms on the in-distribution
traces by at least 3% in terms of average chunk QoE. On three out-of-
distribution datasets and real-world test, MERINA beats all neural
baselines in terms of the average chunk QoE without adaptation,
presenting a performance gain of up to 26% between MERINA and
the second-best algorithm, and achieves a higher average chunk
QoE over all baselines with only about 200 epochs (i.e., 5 minutes) of
adaptation. Our main contributions can be summarized as follows.
• We study the generalization problem of adaptive video streaming,
and formulate the rate adaptation problem as a POMDP, rather
than previously stated MDP. We then propose a model-free
system framework based on context-based meta-RL to improve
generalization for neural ABR algorithms, by decoupling the
inference of throughput dynamics (referred to as latent encoder)
from the universal control mechanism that is shared by all poten-
tial throughput dynamics (referred to as meta-policy network).
• To ensure rapid adaptation to time-varying yet indistinguishable
throughput dynamics in real-world scenarios, we propose an
efficient meta-policy search scheme for the mixed dynamics,
which includes the use of on-policy RL algorithms (or imitation
learning) to alleviate estimation bias for value function, and a
mutual information-based regularization in the policy loss to
make the latent variable more informative about the policy.
• We implement MERINA’s meta-training and meta-adaptation
procedures, and validate its improved generalization capability
through numerous empirical evaluations on different QoE metrics
and multiple datasets containing real-world network throughput
traces, as well as a real-world test. These evaluations demonstrate
that MERINA outperforms the state-of-the-art ABR algorithms
in terms of both the average chunk QoE on the in-distribution
throughput traces, and the capability of generalization and quick
adaptation on the out-of-distribution throughput traces.
2
BACKGROUND AND MOTIVATION
2.1
Problem Formulation
In a typical adaptive video streaming system, the video is temporally
divided into 𝐾chunks (i.e., segments) with a fixed time duration 𝐿.
Each video chunk is further encoded into multiple quality versions
of different bitrates, with the set of available bitrates denoted by
A = {𝑎1,𝑎2, · · · ,𝑎𝑀}, where 𝑀represents the total number of
bitrate versions. Let 𝑎𝑘∈A denote the bitrate version allocated for
the 𝑘-th chunk 𝑈𝑘. Then, once the chunk 𝑈𝑘has been completely
downloaded, the buffer occupancy 𝐵𝑘of the video player deployed
at the user side can be expressed as:
𝐵𝑘= [(𝐵𝑘−1 −𝑑𝑘)+ + 𝐿], 𝑑𝑘= 𝐸𝑎𝑘/𝐶𝑘, (·)+ ≜max{·, 0},
(1)
where 𝐶𝑘is the average network throughput within the duration of
downloading chunk𝑈𝑘, 𝐸𝑎𝑘denotes the actual size of𝑈𝑘associated
with the selected bitrate version 𝑎𝑘, the term 𝑑𝑘then represents the
corresponding time duration spent for downloading chunk 𝑈𝑘. The
rebuffering event will occur within the duration of (𝑑𝑘−𝐵𝑘−1)+ if
the term 𝐵𝑘−1−𝑑𝑘is negative, i.e., the buffer has no video remaining
while the next chunk 𝑈𝑘has not been completely downloaded yet.
As conventionally adopted in many learning-based ABR algo-
rithms, the adaptive video streaming system can be formulated
3007
```


### Pagina 3
```text
Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning
MM ’22, October 10–14, 2022, Lisboa, Portugal
as a Markov decision process (MDP), with the state 𝑠𝑘∈S for
downloading the chunk 𝑈𝑘represented by six features, namely
the measured 1) average throughput 𝐶𝑘−1 and 2) corresponding
download time 𝑑𝑘−1, 3) the vector of chunk sizes associated
with available bitrate versions for the 𝑘-th video chunk: 𝐸=
{𝐸𝑘𝑎1, 𝐸𝑘𝑎2, · · · , 𝐸𝑘𝑎𝑀}, 4) current buffer occupancy 𝐵𝑘−1, 5) selected
bitrate 𝑎𝑘−1 of the last video chunk, and 6) the remaining number
of video chunks that have not been downloaded yet.
To quantify the user’s QoE, we employ a widely used objective
metric that incorporates the trade-off between video quality, quality
fluctuation and risk of rebuffering events as a linear combination:
𝑟(𝑠𝑘,𝑎𝑘) = 𝑞(𝑎𝑘) −𝛼
𝑞(𝑎𝑘) −𝑞(𝑎𝑘−1)
 −𝛽(𝑑𝑘−𝐵𝑘−1)+ ,
(2)
where 𝑟∈𝑅, 𝑞(𝑎𝑘) can be any video quality metric (e.g., PSNR and
SSIM), and 𝛼and 𝛽are a non-negative penalty weight that ensures
the temporal quality smoothness and penalizes the rebuffering
delay, respectively. Therefore, the control policy of the ABR
algorithm can be derived by solving a sequential decision-making
problem that optimizes the average chunk QoE for the user under a
constrained yet time-varying network throughput:
𝑎∗
𝑘= arg max
𝑎
1
𝐾
𝐾
𝑘=0 𝑟(𝑠𝑘,𝑎𝑘),
(3a)
s.t.
𝑠𝑘+1 = 𝑓(𝑠𝑘,𝑎𝑘), 𝑎𝑘∈A,
(3b)
where the dynamics model 𝑓: S × A →S of the video streaming
system includes the buffer occupancy as given in Eq. (1), as well as
the dynamics of network throughput which unfortunately cannot
be explicitly represented or predicted. As such, we are theoretically
unable to find the global optimal solution of Eq. (3), but endeavour
in practice to approach as closer as possible to this global optimum.
2.2
Learning How to Learn Bitrate Adaptation
As a result, the MDP of an adaptive video streaming system
can be formulated as < S, A, 𝑃, 𝑅>, where 𝑃= 𝑝(𝑠𝑘+1|𝑠𝑘,𝑎𝑘)
is the state transition probability that mainly depends on the
dynamics of network throughput. Note that the dynamics of
network throughput are practically hidden from the agent and
independent of the chosen actions, which are typically time-varying
and heterogeneous in real world scenarios. Consequently, the state
transition probability 𝑃will vary continuously over time and result
in a variety of different MDPs, which in essence can be formulated
more accurately as a partially observable Markov decision process
(POMDP). By denoting the underlying throughput dynamics as
a latent variable 𝒛∈𝑍, we can re-formulate the adaptive video
streaming problem as a tuple < S, A, 𝑃,𝑍, 𝑅>, where the state
space S, action space A and reward space 𝑅remain the same, while
the state transition probability changes to 𝑃= 𝑝(𝑠𝑘+1|𝑠𝑘,𝑎𝑘,𝑧𝑘),
with 𝑧𝑘representing the throughput dynamics during the duration
of downloading chunk 𝑈𝑘. In the following, we will omit the
subscript 𝑘for notational simplicity, i.e., 𝑠𝑘,𝑎𝑘,𝑟𝑘,𝑧𝑘written as
𝒔, 𝒂, 𝒓, 𝒛in places where there is no ambiguity.
To the best of our knowledge, most of the previously proposed
neural ABR algorithms neglect the variability of transition probabil-
ity 𝑃(i.e., under the assumption that the throughput dynamics stay
the same over time), thus incorporating the throughput information
during download of the past several chunks to the state formulation.
The agent trained with such a formulation can learn a universal ABR
Video Players
Time-varying and heterogeneous
throughput dynamics
Encoder
ࣘ
Inference Network (Latent Encoder)
contexts
l
Buffer occupancy
latent distribution
state 
Policy Network
Meta-Policy
st
latent 
Trained by on-policy RL or imitation learning
ous
bitrate 
Figure 1: System framework of the proposed MERINA.
policy that performs well if the distribution of throughput dynamics
has been experienced in the training dataset, but may unfortunately
present a very poor generalization in unseen (or out-of-distribution)
network contexts. Meta-RL, as a popular method for fast adaptation
to unseen environments, trains an agent from multiple sample tasks
to construct a meta-policy over the shared structure across tasks
[3, 16]. We are therefore motivated to propose MERINA, a context-
based meta-RL approach for decoupling inference of underlying
network dynamics 𝒛from the universal control mechanism. Other
than learning a separate ABR control policy for each possible
network throughput dynamic from millions of samples, we would
like our ABR agent to discover a common control mechanism (i.e.,
meta-policy 𝜋(𝒂|𝒔, 𝒛)) shared across a range of possible throughput
dynamics during the training. Once learned, this policy is expected
to adapt to new throughput dynamics with only a few trials when
their necessary latent variable 𝒛is provided. In other words, with
MERINA we intend to develop a generalized paradigm for neural
ABR algorithms, by learning how to rapidly learn an appropriate
ABR policy for each network environment.
3
PROPOSED METHOD
The overall system framework of MERINA is illustrated in Fig. 1,
comprising two following two key components.
• 1) Meta-trained dynamics inference network (i.e., latent
encoder). To endow the control policy with an effective represen-
tation of current network dynamics, we capture the knowledge
about underlying dynamics with a latent probabilistic context
variable 𝒛based on recent experience of the current (new)
dynamics. Encountering a new network environment, this latent
variable 𝒛can reason about dynamics uncertainty, allowing for a
stochastic exploration of meta-learned policy to explore states
with potentially higher rewards while also quickly adapting to
the new dynamics. Meanwhile, sampling the latent variable from
a probabilistic distribution improves the generalization of control
policies when a deterministic inference of dynamics is difficult.
• 2) Latent-conditioned policy network (i.e., policy search).
To identify a universal ABR control policy capable of adapting
its behavior to the network throughput dynamics, we set a 𝜃-
parameterized policy 𝜋𝜃(𝒂|𝒔, 𝒛) as conditioned on the latent
variable 𝒛. Thus, if the latent variable 𝒛can be reliably inferred
from the recent experience, the resulting policy 𝜋𝜃(𝒂|𝒔, 𝒛) will
potentially adapt to a new network environment.
We train the above inference and policy networks with a model-free
approach, by optimizing their parameters via gradients from the
same loss function L𝑎𝑐𝑡𝑜𝑟. Additionally, it is straightforward to
search for the optimal policy by using a variety of methods, such as
3008
```


### Pagina 4
```text
MM ’22, October 10–14, 2022, Lisboa, Portugal
Nuowen Kan et al.
policy-gradient RL or imitation learning. However, the training data
contain too many different types of underlying network dynamics
to enable an informative latent representation about the policy.
To solve this issue, a mutual information-based regularization is
further proposed, in addition to the basic loss function.
3.1
Modeling the Uncertainty of Inference
To facilitate adaptation, the latent variable 𝒛should encode an
effective representation of the current network throughput dy-
namics by exploiting a collection of past experienced network
throughputs. Here, we define the throughput context as 𝒄𝑘−𝑝:𝑘=
{(𝐶𝑘−𝑝,𝑑𝑘−𝑝), · · · , (𝐶𝑘−1,𝑑𝑘−1)}, which consists of the average
throughput values and time intervals of throughput measurements
collected from the download of chunk 𝑈𝑘−𝑝to chunk 𝑈𝑘−1. In
the following, we will often write 𝒄𝑘−𝑝:𝑘as 𝒄for notational
simplicity. Due to the time-varying nature of the underlying
network throughput dynamics, we only collect the past experience
from the most recent 𝑝chunks, rather than from the beginning
of video playback. Additionally, we make the assumption that the
true chunk sizes will remain relatively constant throughout all
video chunks for each bitrate version, thus omitting the dynamics
inference for video content.
To approximate the posterior 𝑝(𝒛|𝒄) over latent variable space
𝑍, we build up an inference network that generates the distribution
𝑞𝜙(𝒛|𝒄) parameterized by 𝜙. This inference network can be trained
via a model-free manner by using the method described in [16],
with the goal of directly maximizing a variational lower bound:
E(𝒄,𝝉)∼B

𝐽(𝒄,𝝉) + 𝛽𝐷KL
𝑞𝜙(𝒛|𝒄)||𝑝(𝒛)
,
(4)
where 𝑝(𝒛) is a unit Gaussian prior over 𝑍, and 𝐽(𝒄,𝝉) may be any
objective chosen from a variety of those for policy search, with
𝝉= {𝒔, 𝒂, 𝒓} being corresponding samples, as will be detailed in
Sections 3.2 and 4. We also assume the Gaussian posterior over 𝑍
and employ the Gaussian factor 𝑞𝜙(𝒛|𝒄) = N (𝑓𝜇
𝜙(𝒄), 𝑓𝜎
𝜙(𝒄)), which
make the proposed method tractable. As a function of the context,
𝑓(·)
𝜙
(𝒄) predicts the mean 𝜇and variance 𝜎for 𝑞𝜙(𝒛|𝒄), respectively.
Therefore, the inference of network throughput dynamics can be
done by sampling latent variable 𝒛from the posterior distribution
𝑞𝜙(𝒛|𝒄). This posterior can reason about uncertainty associated
with the dynamics inference, particularly in light of the fact that the
underlying throughput dynamics are difficult to identify due to the
scarcity of data samples, i.e., epistemic uncertainty. Probabilistic
sampling reduces the risk of biased latent representation, thus
increasing the generalization capability of control policies. Besides,
modeling the uncertainty enables a stochastic exploration for
meta-policy adaptation in response to new environments, hence
increasing the sample efficiency of policy search.
In the outer expectation of Eq. (4), the replay buffer B contains
recent historical experience of environment interaction, including
the context 𝒄and the corresponding samples 𝝉= {𝒔, 𝒂, 𝒓}. Due
to the fact that the throughput dynamics in real world scenarios
are time-varying and heterogeneous, it is infeasible to identify
the distinct network throughput dynamics from the environment
of adaptive video streaming. In other worlds, in an arbitrary
trajectory {(𝒄0:𝑝,𝝉𝑝), · · · , (𝒄𝑘−𝑝:𝑘,𝝉𝑘), · · · } from interacting with
the environment, the agent may experience multiple types of
throughput dynamics, which we call the mixed dynamics. Thus, we
are unable to sample (𝒄,𝝉) pairs that belong to the same dynamics
in Eq. (4), which is different from the typical setting used in most of
previous works. We must calculate the expectation in Eq. (4) over
trajectories sampled from the mixed dynamics, which complicates
the process of meta-policy search for each throughput dynamic.
3.2
Meta-Policy Search on Mixed Dynamics
To address the challenge raised by mixed dynamics, we explore
the types of policy search methods that can be employed in this
situation, and then design a mutual information-based regulariza-
tion to make the latent variable more informative about the bitrate
selection strategy.
The policy network approximates the mapping from the latent
variable and the state to an optimal ABR control policy 𝜋𝜃(𝒂|𝒔, 𝒛) :
S × 𝑍↦→A. In general, RL algorithms improve the policy by
utilizing trajectories experienced with the same dynamics transition
probability 𝑃, while meta-RL does the same by optimizing the policy
for each different task or dynamic in turn. However, because of the
time-varying characteristic of throughput dynamics, the trajectories
(𝒄,𝝉) in our mixed dynamics situation cannot guarantee to have the
same transition probability 𝑝(𝑠𝑘+1|𝑠𝑘,𝑎𝑘,𝑧𝑘). Thus, in our setting
off-policy RL algorithms, such as SAC [6], will introduce more bias
into estimating the value function than on-policy RL algorithms.
This is because the off-policy algorithms cannot estimate the value
function of target policy by reusing the trajectories explored by
any other behavior policy that has encountered different types
of underlying dynamics. Consequently, it is preferable to train
the meta-policy 𝜋𝜃(𝒂|𝒔, 𝒛) by using on-policy RL algorithms or
imitation learning methods[7]. We refer to the objective of policy
search as ˜𝐽(𝒄,𝝉).
As stated in Section 3.1, the objective 𝐽(𝒄,𝝉) in Eq. (4) can
be any objective function of meta-policy 𝜋𝜃(𝒂|𝒔, 𝒛), including
𝐽(𝒄,𝝉) = ˜𝐽(𝒄,𝝉). However, to enable throughput dynamics to be
informative about the meta-policy in our setting of mixed dynamics,
we introduce additionally a mutual information regularization to
the objective, i.e., maximizing 𝐽(𝒄,𝝉) = ˜𝐽(𝒄,𝝉) + 𝜆I(𝒂; 𝒛|𝒔), where
𝜆∈[0, 1] is an annealing parameter that adjusts the strength of
regularization and I(𝒂; 𝒛|𝒔) can be expressed as:
I(𝒂; 𝒛|𝒔) = H (𝒂|𝒔) −H (𝒂|𝒛, 𝒔)
(5)
= −E𝒂[log 𝜋(𝒂|𝒔)] + E𝒂[log 𝜋𝜃(𝒂|𝒔, 𝒛)].
In Eq. (5), the mutual information I(𝒂; 𝒛|𝒔) quantifies how much
information about 𝒂can be known given 𝒛and 𝒔. In other words,
maximizing this regularization entails increasing the diversity of
policy when the throughput dynamics are uncertain, as measured
by the entropy H (𝒂|𝒔), while making 𝒛more informative about the
bitrate selection by minimizing the entropy H (𝒂|𝒛, 𝒔). Additionally,
to simplify the computation of 𝜋(𝒂|𝒔), it can be estimated by:
𝜋(𝒂|𝒔) =
∫
𝜋𝜃(𝒂|𝒔, 𝒛)𝑝(𝒛|𝒔)𝑑𝒛≈
∫
𝜋𝜃(𝒂|𝒔, 𝒛)𝑝(𝒛)𝑑𝒛
(6)
≈
1
𝑁𝑠𝑎
𝑁𝑠𝑎
𝑖=1 𝜋𝜃(𝒂|𝒔, 𝒛𝑖),
𝒛𝑖∼𝑝(𝒛),
where 𝑁𝑠𝑎denotes the number of samples from the prior 𝑝(𝒛).
With the model-free approach, parameters 𝜙of inference net-
work can be optimized via the backward-pass vector ∇𝐽/∇𝒛, i.e.,
3009
```


### Pagina 5
```text
Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning
MM ’22, October 10–14, 2022, Lisboa, Portugal
∇𝐽/∇𝜙= ∇𝐽/∇𝒛· ∇𝒛/∇𝜙. Note that we can pass the gradient from
the policy network to inference network with the Gaussian re-
parameterization trick [11], even though the latent variable input
of policy network is sampled from the output of inference network,
i.e., 𝒛∼𝑞𝜙(𝒛|𝒄).
4
IMPLEMENTATION
4.1
Meta-Policy Search with DRL
To enable an effective policy search, we build up our algorithm
on top of the proximal policy optimization (PPO) algorithm [19],
a well known on-policy actor-critic method recognized for its
reliable performance on policy improvement with trust region
policy optimization. With PPO, we construct two networks: an
actor network 𝜋𝜃(𝒂|𝒔, 𝒛) and a critic network 𝑉𝜃𝑣(𝒔, 𝒛). We jointly
train the inference and actor networks to maximize the actor loss
and the regularization I(𝒂; 𝒛|𝒔) on the parameters of 𝜃and 𝜙. As a
result, the objective ˜𝐽𝜃(𝒄,𝝉) of the actor network is expressed as:
˜𝐽𝜃(𝒄,𝝉) = E𝒛
	
min

𝜌(𝜃) ˆ𝐴, clip[𝜌(𝜃), 1 −𝜖, 1 + 𝜖] ˆ𝐴

,
(7)
𝜌(𝜃) = 𝜋𝜃(𝒂|𝒔, 𝒛)/𝜋𝜃′(𝒂|𝒔, 𝒛),
𝒛∼𝑞𝜙(𝒛|𝒄)
where𝜃′ denotes the previous values of𝜃following the latest update
epoch, clip[𝜌(𝜃), 1 −𝜖, 1 + 𝜖] ensures no incentive for moving 𝜌(𝜃)
outside the interval [1−𝜖, 1+𝜖], and ˆ𝐴is the truncated generalized
advantage estimation (GAE) function [18] generated from the value
function 𝑉𝜃𝑣(𝒔, 𝒛) and 𝒓. Similarly, the critic loss is formulated as:
L𝜃𝑣(𝒄,𝝉) = 1
2E¯𝒛

(𝑉𝜃𝑣(𝒔, ¯𝒛) −𝐺𝑘)2
,
¯𝒛∼𝑞𝜙(𝒛|𝒄),
(8)
where 𝐺𝑘= 𝑟𝑘+ 𝛾𝑟𝑘+1 + 𝛾2𝑟𝑘+2 + · · · is the rollout QoE return of
the current state following 𝜋𝜃′(𝒂|𝒔, 𝒛),𝛾∈(0, 1] is a discount factor
that attenuates exponentially the impact of future actions over the
current expected QoE, and ¯𝒛indicates that gradients are not being
computed through it.
4.2
Imitation Learning-Based Pre-Training
In practice, due to the low sample efficiency of RL training [15],
training the meta-RL from scratch is exceedingly time expensive
and unstable in our setting of mixed dynamics. Therefore, we
pre-train the parameters 𝜙and 𝜃following the imitation learning
method proposed in [7], with a behavior cloning objective for the
actor and inference networks:
max
𝜃,𝜙
E𝒛, ˆ𝒂log 𝜋𝜃( ˆ𝒂|𝒔, 𝒛), 𝒛∼𝑞𝜙(𝒛|𝒄), ˆ𝒂∼𝜋𝑒(𝒂|𝒔),
(9)
where the model-based ABR algorithm RobustMPC [24] is adopted
to obtain the expert policy 𝜋𝑒(𝒂|𝒔), with the QoE maximized over
a horizon of future 3 chunks. Here, we skip the pre-training of
critic network, since 𝜃𝑣may be rapidly converged with only a
few trials following the policy 𝜋𝜃(𝒂|𝒔, 𝒛). Notably, we employ
RobustMPC here primarily for its good QoE performance and
low computational complexity, which will be also justified by
the experimental evaluations in Section 5. However, variants of
MERINA can be easily fulfilled by adopting other existing ABR
algorithms to obtain the expert policy, resulting in a difference on
the training time and overall QoE performance.
In summary, the entire meta-training and meta-adaptation
workflow of MERINA is given in Algorithm 1 and Algorithm 2,
Algorithm 1 Meta-training Procedure of MERINA
Require: Dynamics model 𝑓of the video streaming system with
time-varying and heterogeneous network dynamics, learning
rates 𝛼1, 𝛼2, 𝛼3
// First stage: pre-training with expertise
1: Initialize replay buffer B
2: while 𝑘<= 𝑁update do
3:
Sample 𝑧𝑘∼𝑞𝜙(𝑧𝑘|𝒄𝑘−𝑝:𝑘), 𝑎𝑘∼𝜋𝜃(𝑎𝑘|𝑠𝑘,𝑧𝑘)
4:
Obtain the label ˆ𝑎𝑘∼𝜋𝑒(𝑎𝑘|𝑠𝑘), add (𝑠𝑘, 𝒄𝑘−𝑝:𝑘, ˆ𝑎𝑘) to B
5:
Update the state with 𝑠𝑘+1 = 𝑓(𝑠𝑘,𝑎𝑘)
6:
if 𝑘> 𝑁batch then
7:
Sample batch 𝑏𝑘∼B with a batch size of 𝑁batch
8:
L𝑎𝑐𝑡𝑜𝑟(𝑏𝑘) = −E𝒛, ˆ𝒂log 𝜋𝜃( ˆ𝒂|𝒔, 𝒛) −𝜆I(𝒂; 𝒛|𝒔)
9:
L𝐾𝐿(𝑏𝑘) = 𝛽𝐷KL(𝑞𝜙(𝒛|𝒄)||𝑝(𝒛))
10:
𝜃←𝜃−𝛼1∇𝜃L𝑎𝑐𝑡𝑜𝑟(𝑏𝑘)
11:
𝜙←𝜙−𝛼3∇𝜙[L𝑎𝑐𝑡𝑜𝑟(𝑏𝑘) + L𝐾𝐿(𝑏𝑘)]
12:
end if
13: end while
// Second stage: meta-policy improvement with regularized PPO
14: Fit 𝑉𝜃𝑣(𝒔, 𝒛) following the current 𝜃and 𝜙via Eq. (8)
15: repeat
16:
Initialize replay buffer B, 𝜃′ = 𝜃
17:
for 𝑘= 1, · · · , 𝑁exp do
18:
Sample 𝑧𝑘∼𝑞𝜙(𝑧𝑘|𝒄𝑘−𝑝:𝑘), 𝑎𝑘∼𝜋𝜃′(𝑎𝑘|𝑠𝑘,𝑧𝑘)
19:
Compute the reward 𝑟𝑘(𝑠𝑘,𝑎𝑘)
20:
Add(𝑠𝑘, 𝒄𝑘−𝑝:𝑘,𝑎𝑘,𝑟𝑘) to B
21:
Update the state with 𝑠𝑘+1 = 𝑓(𝑠𝑘,𝑎𝑘)
22:
end for
23:
for 𝑖= 1, · · · , 𝑁u do
24:
Sample batch 𝑏𝑖∼B with a batch size of 𝑁batch
25:
L𝑎𝑐𝑡𝑜𝑟(𝑏𝑖) = −˜𝐽𝜃−𝜆I(𝒂; 𝒛|𝒔), L𝑐𝑟𝑖𝑡𝑖𝑐(𝑏𝑖) = L𝜃𝑣(𝑏𝑖)
26:
L𝐾𝐿(𝑏𝑖) = 𝛽𝐷KL(𝑞𝜙(𝒛|𝒄)||𝑝(𝒛))
27:
𝜃←𝜃−𝛼1∇𝜃L𝑎𝑐𝑡𝑜𝑟(𝑏𝑖), 𝜃𝑣←𝜃𝑣−𝛼2∇𝜃𝑣L𝑐𝑟𝑖𝑡𝑖𝑐(𝑏𝑖)
28:
𝜙←𝜙−𝛼3∇𝜙[L𝑎𝑐𝑡𝑜𝑟(𝑏𝑖) + L𝐾𝐿(𝑏𝑖)]
29:
end for
30: until Converged
Algorithm 2 Meta-adaptation Procedure of MERINA
Require: Test dynamics model 𝑓′, learning rates 𝛼1, 𝛼2, 𝛼3
1: for 𝑖= 1, · · · , 𝑁adapt do
2:
Initialize replay buffer B, 𝜃′ = 𝜃
3:
Rollout policy 𝜋𝜃′(𝑎𝑘|𝑠𝑘,𝑧𝑘) with 𝑠𝑘+1 = 𝑓′(𝑠𝑘,𝑎𝑘) and
collect 𝑁exp samples to B
//Adaptation with regularized PPO
4:
for 𝑖= 1, · · · , 𝑁u do
5:
Sample batch 𝑏𝑖∼B with a batch size of 𝑁batch
6:
𝜃←𝜃−𝛼1∇𝜃L𝑎𝑐𝑡𝑜𝑟(𝑏𝑖), 𝜃𝑣←𝜃𝑣−𝛼2∇𝜃𝑣L𝑐𝑟𝑖𝑡𝑖𝑐(𝑏𝑖)
7:
𝜙←𝜙−𝛼3∇𝜙[L𝑎𝑐𝑡𝑜𝑟(𝑏𝑖) + L𝐾𝐿(𝑏𝑖)]
8:
end for
9: end for
respectively. We adopt a similar NN architecture to Pensieve [14]
for the actor-critic network, and a simple 1-D CNN-based encoder
for the inference network (see Appendix A for detail).
3010
```


### Pagina 6
```text
MM ’22, October 10–14, 2022, Lisboa, Portugal
Nuowen Kan et al.
5
PERFORMANCE EVALUATION
Experiment setup. To evaluate the performance in terms of the
average chunk QoE, consistency and fast adaptation across a wide
range of throughput patterns, we test MERINA on the virtual player
as widely used in [1, 7, 8, 10, 14], which simulates the adaptive video
streaming process by using the real-world network throughput
datasets, in comparison to other ABR algorithms. For the sake of
fairness, we also use the same environment settings as in [7, 8, 14]:
the available bitrate set is A = {300, 750, 1200, 1850, 2850, 4300}
𝐾𝑏𝑝𝑠, the chunk duration is set as 𝐿= 4 seconds, the buffer
occupancy is limited as 1 minute, and the total number of video
chunks is 𝐾= 49. For the QoE metric in Eq. (2), we adopt two widely
used settings as in [14, 21, 24]: 1) the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛
with 𝑞(𝑎𝑘) = 𝑎𝑘/1000, 𝛼= 1, 𝛽= 4.3; and 2) the log-form quality
metric 𝑄𝑜𝐸𝑙𝑜𝑔with 𝑞(𝑎𝑘) = log(𝑎𝑘/min(A)), 𝛼= 1, 𝛽= 2.66. For
the practical implementation of MERINA’s meta-training and meta-
adaptation, the discount factor is set as 𝛾= 0.99. The weights of
loss function are set as 𝛽= 0.02, 𝜆= 0.15. Also, we let 𝑝= 8,𝜖=
0.04, 𝑁𝑠𝑎= 10, 𝑁update = 650, 𝑁batch = 64, 𝑁𝑢= 2, 𝑁𝑒𝑥𝑝= 256, and
set the learning rates as 𝛼1 = 𝛼3 = 10−5, 𝛼2 = 10−4. Our code is
available at https://github.com/confiwent/merina.
Baseline algorithms. We compare MERINA with the following
six state-of-the-art ABR algorithms. 1) BOLA [21]: a buffer-based
algorithm that uses Lyapunov optimization to determine the
optimal bitrate version under the constraint of buffer occupancy
only. 2) RobustMPC [24]: a model-based algorithm that solves
the optimization problem in Eq. (3) with a horizon of the future ℎ
video chunks under the framework of model predictive control. The
future throughput is predicted by the harmonic mean of average
throughput measurements of the past 5 downloaded chunks. 3)
Pensieve [14]: a DRL-based algorithm that uses the A3C algorithm
to learn an optimal neural mapping from the dynamics of buffer
occupancy, throughput and chunk size to the rate adaptation of the
next chunk. 4) Comyco [7, 8]: a model-free neural ABR algorithm
that uses NNs to directly approximate the offline near-optimal
expert solution by lifelong imitation learning. 5) Fugu [23]: a model-
based algorithm that uses NN-based transmission time predictor to
predict the probability distribution of download times per bitrate
version for future ℎchunks, and optimizes the bitrate selection
via calculating the expectation of maximum future ℎ-horizon QoE
return. 6) BayesMPC [10]: a model-based algorithm that uses
Bayesian NNs to predict the lower bound of future throughputs,
based on which a model predictive control is further employed to
optimize the future ℎ-horizon QoE return.
Note that Fugu is proposed to learn in situ, which is also proposed
in [23] and said to be a more sound virtual player than the one
employed in our paper. Due to the fact that the simulation platform
has little effect on the success of MERINA in terms of generalization,
we choose the virtual player that is widely deployed in the majority
of prior works. Therefore, we re-implement Fugu and utilize it as a
baseline ABR algorithm that optimizes the expectation of QoE with
a probabilistic download time predictor. Additionally, the planning
horizon of RobustMPC, Fugu and BayesMPC is set to ℎ= 3 chunks.
Datasets of network throughput. We collect four public real-
world network throughput datasets (3G/HSDPA [17], FCC [2], Oboe
[1], Puffer [23]) to simulate various user and network conditions.
The mean and standard deviation values of these datasets are
listed in bottom row of Table 1. We combine the similar datasets
FCC and 3G/HSDPA into one dataset (named F&H), which is then
used to validate the in-distribution performance of different ABR
algorithms. Note that the datasets 3G/HSDPA, FCC and Oboe
contain only a small amount of traces, but the throughput data of
Puffer is updated daily (data of a single day takes up to several GB)
and has been regularly updated since January 2019. We download
all traces on two randomly chosen dates (Oct. 17, 2021 and Feb.
18, 2022), and utilize them as two Puffer datasets with long-tailed
throughput dynamics. Additionally, to match with the low video
bitrate setting in the experiments, we shrink the throughput values
of Puffer into 1/8 of their original values.
5.1
In-Distribution QoE Performance
We first evaluate and compare the QoE performance of MERINA
with other baselines on the F&H throughput dataset, with the
two different QoE metric settings. All throughput traces in the
F&H dataset, as used in [7, 8, 14, 24], are randomly split into three
partitions: training, validation and test sets. The learning-based
methods (MERINA, Pensieve, Comyco, Fugu and BayesMPC) are
trained on the training set and evaluated on the validation set. By
choosing the NNs weights that perform best on the validation set,
the performance of all comparison algorithms is then tested on the
test set. Note that the QoE performance may slightly vary with
the random traces selection and unstable NNs training, so it is
natural to notice some discrepancies between earlier works and
ours. We simulate the playback of the same video once for each
throughput trace (referred to as a session), and then collect QoE
values of all chunks for comparison. Since the test and training sets
share the same distribution of throughout traces, we call the results
in-distribution QoE performance.
Figs. 2(a) and 2(d) depict the cumulative distribution functions
(CDFs) of all sessions’ average QoE for all algorithms. The CDFs
in Figs. 2(b) and 2(e) illustrate the QoE improvements of the other
algorithms over RobustMPC in all sessions. And the bar graphs in
Figs. 2(c) and 2(f) show the average chunk QoE and each individual
components in Eq. (2), where the error bars span ± one standard
deviation from the average value. The key observation is that
MERINA outperforms the other baseline algorithms in terms of
the average chunk QoE value with both the linear and log-form
QoE metrics on the F&H throughput dataset. The performance
gap of the average chunk QoE between MERINA and the baseline
algorithms is at least 3% and 4% for 𝑄𝑜𝐸𝑙𝑖𝑛and 𝑄𝑜𝐸𝑙𝑜𝑔, respectively.
And Comyco beats the remaining baseline algorithms in terms of
QoE (slightly better than Pensieve), demonstrating the effectiveness
of imitation learning. As for the variance of the results for all
sessions, BOLA has the lowest standard deviation (0.72 for 𝑄𝑜𝐸𝑙𝑖𝑛
and 0.65 for 𝑄𝑜𝐸𝑙𝑜𝑔) but the worst average QoE, whereas MERINA
also performs well, with a standard deviation of 0.87 and 0.71 for
𝑄𝑜𝐸𝑙𝑖𝑛and 𝑄𝑜𝐸𝑙𝑜𝑔, respectively. In addition, the results also reveal
that MERINA performs robustly throughout all sessions, with a
largest proportion of sessions achieving a higher QoE. For instance,
Figs. 2(a) and 2(d) show that at least 95% of MERINA sessions
achieve an average QoE greater than 0. The results in Fig. 2(b) and
Fig. 2(e) verify that in about 80% of sessions, MERINA outperforms
RobustMPC, and in the worst case the average QoE of MERINA
3011
```


### Pagina 7
```text
Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning
MM ’22, October 10–14, 2022, Lisboa, Portugal
#FUUFS
(a) 𝑄𝑜𝐸𝑙𝑖𝑛
#FUUFS
(b) 𝑄𝑜𝐸𝑙𝑖𝑛
0
0.2
0.4
0.6
0.8
1
1.2
1.4
Chunk QoE
Bitrate utility
Rebuffering penalty
Smoothness penalty
Averagevalue
BOLA
RobustMPC
Pensieve
Comyco
Fugu
BayesMPC
MERINA
(c) 𝑄𝑜𝐸𝑙𝑖𝑛
#FUUFS
(d) 𝑄𝑜𝐸𝑙𝑜𝑔
#FUUFS
(e) 𝑄𝑜𝐸𝑙𝑜𝑔
0
0.2
0.4
0.6
0.8
1
1.2
1.4
Chunk QoE
Bitrate utility
Rebuffering penalty
Smoothness penalty
Averagevalue
BOLA
RobustMPC
Pensieve
Comyco
Fugu
BayesMPC
MERINA
(f) 𝑄𝑜𝐸𝑙𝑜𝑔
Figure 2: Performance comparison of different ABR algorithms in terms of the average chunk QoE value and the individual
QoE components with the QoE metrics 𝑄𝑜𝐸𝑙𝑖𝑛and 𝑄𝑜𝐸𝑙𝑜𝑔on F&H (FCC and HSDPA) throughput dataset.
Table 1: Performance comparison of different ABR algorithms in terms of the average chunk 𝑄𝑜𝐸𝑙𝑜𝑔value on different datasets.
Mean ± std (𝑅𝑔𝑎𝑝)
FCC
HSDPA
Oboe
Puffer-Oct.17-21
Puffer-Feb.18-22
BOLA
0.95 ± 0.63 (−17%)
1.11 ± 0.64 (−9%)
1.63 ± 0.66 (−11%)
0.88 ± 1.29 (+20%)
0.75 ± 1.93 (−14%)
RobustMPC
1.05 ± 0.63 (−8%)
1.16 ± 0.85 (−5%)
1.79 ± 0.73 (−2%)
0.76 ± 1.48 (+5%)
0.86 ± 2.01 (−2%)
Pensieve
1.07 ± 0.62 (−7%)
1.21 ± 0.68 (−1%)
1.75 ± 0.69 (−4%)
0.40 ± 7.17 (−46%)
0.66 ± 5.40 (−25%)
Comyco
1.11 ± 0.63 (−3%)
1.22 ± 0.78 (−0%)
1.76 ± 0.77 (−3%)
−0.22 ± 2.20 (−130%)
0.65 ± 2.25 (−26%)
Fugu
1.04 ± 0.70 (−10%)
1.16 ± 0.80 (−5%)
1.71 ± 0.78 (−6%)
0.54 ± 1.55 (−26%)
0.77 ± 1.94 (−12%)
BayesMPC
1.05 ± 0.78 (−9%)
1.09 ± 0.84 (−2%)
1.78 ± 0.74 (−2%)
0.54 ± 1.88 (−26%)
0.76 ± 2.20 (−14%)
MARINA
1.15 ± 0.66
1.22 ± 0.85
1.82 ± 0.70
0.73 ± 1.63
0.88 ± 2.00
MERINA (nMI with 𝜆= 0, see Appendix B.3)
1.05 ± 0.65 (−9%)
1.19 ± 0.71 (−2%)
1.74 ± 0.69 (−4%)
0.71 ± 1.58 (−2%)
0.83 ± 1.96 (−5%)
Dataset distribution
1.13 ± 0.44 Mbps
1.61 ± 0.95 Mbps
2.60 ± 2.08 Mbps
1.85 ± 0.91 Mbps
1.60 ± 0.88 Mbps
is just 0.3 less than RobustMPC’s. Furthermore, the bar graphs in
Figs. 2(c) and 2(f) indicate that MERINA can surprisingly achieve low
rebuffering and smoothness penalties, similar to those of Pensieve.
While other algorithms result in either a longer rebuffering time,
as Comyco does, or a higher quality fluctuation, as BOLA does,
during the video playback. Note that the results obtained for linear
QoE metric 𝑄𝑜𝐸𝑙𝑖𝑛are similar to those for log-form QoE metric
𝑄𝑜𝐸𝑙𝑜𝑔w.r.t. all comparison algorithms. Therefore, we only show
and compare the performance for 𝑄𝑜𝐸𝑙𝑜𝑔in the following, and
move results of 𝑄𝑜𝐸𝑙𝑖𝑛to Appendix B due to page limit.
5.2
Consistency on Out-of-Distribution Traces
To study the consistency of MERINA in comparison to other
learning-based methods, we measure their performance on out-
of-distribution datasets Oboe, Puffer-Oct.17-21 and Puffer-Feb.18-
22 (i.e., with a different distribution of throughput dynamics than
F&H dataset) by using the same NN weights obtained in Section
5.1 (i.e., learned from the F&H dataset). We show in Table 1 the
numerical results that are composed of the average chunk QoE
value ± one standard deviation for all the comparison algorithms
and the performance gap 𝑅𝑔𝑎𝑝= [(𝑟−𝑟∗)/𝑟∗] × 100% to the value
of MERINA, where 𝑟∗is the average chunk QoE of MERINA and 𝑟is
the average chunk QoE of each comparison algorithm. Additionally,
Table 1 also includes results from the FCC and HSDPA datasets to
demonstrate the consistency of all algorithms’ performance on a
subset of the training throughput dynamics distribution.
The results on FCC and HSDPA traces show that the learning-
based baselines perform worse on FCC traces than on HSDPA
traces, indicating that training these algorithms on mixed dynamics
is unlikely to result in the acquisition of expertise that performs
uniformly across all experienced dynamics. The results on out-of-
distribution datasets (Oboe, Puffer-Oct.17-21 and Puffer-Feb.18-
22) reveal that the NN weights trained in F&H datasets using
MERINA provide the highest degree of consistency or generalization
performance among the learning-based baselines, over all ranges
of varying throughput dynamics. The heuristic ABR algorithms
(BOLA and RobustMPC) can always achieve a satisfactory QoE
performance on different throughput dynamics, while BOLA beats
all the other algorithms on Puffer-Oct.17-21 traces where the
throughput dynamics are difficult to predict and considerably
deviate from those on the F&H traces. In contrast, the other
learning-based methods fail to generalize to the out-of-distribution
datasets, verifying the generalization difficulty of DRL or imitation
learning-based neural ABR algorithms. Concretely, the model-free
neural algorithms (e.g., Pensieve and Comyco) suffer from retaining
their capability on Oboe traces while degrading significantly on
Puffer traces, particularly on the Puffer-Oct.17-21 dataset. While
the model-based algorithms (e.g., Fugu and BayesMPC) that use
3012
```


### Pagina 8
```text
MM ’22, October 10–14, 2022, Lisboa, Portugal
Nuowen Kan et al.
0
0.5
1
1.5
2
2.5
3
4G
Public WiFi
International Link
Average  value
BOLA
RobustMPC
Comyco
MERINA
Figure 3: Comparison of 𝑄𝑜𝐸𝑙𝑜𝑔without adaption.
NNs to learn the throughput dynamics have a better consistency
or generalization than Pensieve and Comyco, though they also
perform much worse on Puffer traces than heuristic methods. This
demonstrates that, besides meta-RL-based methods, model-based
methods are another viable paradigm for addressing the general-
ization challenge of adaptive video streaming. In conclusion, our
MERINA performs consistently with out-of-distribution throughput
dynamics, though it may have a worse QoE than BOLA in some
sessions. More importantly, MERINA can further rapidly adapt to
the new throughput dynamics via a few updates (see Section 5.3).
Real-World Test. We then evaluate MERINA, Comyco (the state-
of-the-art model-free ABR algorithm) and the heuristic algorithms
BOLA and RobustMPC in the real world platform under three
different network conditions: a 4G cellular network, a public
WiFi network on campus, and a wide area network connecting
Shanghai and Los Angeles, with mean and standard deviation of
recorded throughput values of 5.74 ± 0.39𝑀𝑏𝑝𝑠, 2.04 ± 0.89𝑀𝑏𝑝𝑠
and 1.78 ± 1.10𝑀𝑏𝑝𝑠. The real-world platform based on Dash.js
[4] is implemented similarly to that in [7, 14], and we thus omit its
description for simplicity. The same test video is loaded repeatedly
on each network using a randomly chosen ABR scheme. Each
experiment takes about 1 hour to complete, and the NNs weights
for MERINA and Comyco are all trained on F&H dataset. The
results in Fig. 3 illustrates that MERINA performs similarly to
RobustMPC, and outperforms BOLA and Comyco on these new
network environments. While Comyco performs the worst under
public WiFi and international link conditions.
5.3
Fast Adaptation to New Environments
Section 5.2 exhibits the satisfactory consistency performance of
MERINA when confronted with some unseen throughout dynamics,
and reveals that MERINA will degrade performance on traces with
dynamics that are significantly different from those in the training
dataset. Hence, we examine here MERINA’s ability to rapidly adapt
to these unfamiliar throughput dynamics by investigating the
performance of meta-adaption procedure given in Algorithm 2.
Fig. 4 depicts the performance of an adaptation procedure that
seeks to fine-tune the existing NN weights of MERINA and Comyco
utilizing traces from Puffer-Oct.17-21 dataset. The test traces of
Puffer-Oct.17-21 used in Section 5.2 are also used to assess the
performance of comparison algorithms, and the training traces
are additional data collected on the same day. Comyco is fine-
turned using the suggested lifelong learning method (Comyco-
Lifelong) in [7]. We refer to MERINA during the meta-adaptation
procedure as MERINA-Adapt, and its asymptotic performance of
adaptation (i.e., after converging to the optimum) as MERINA-Asy.
In a training epoch, the NN weights are updated twice, while each
update is with a batch size of 64 samples.
(a) Adaptation Curves
#FUUFS
(b) Puffer-Oct.17-21
Figure 4: a) The adaptation curves of MERINA and Comyco,
and b) average chunk 𝑄𝑜𝐸𝑙𝑜𝑔improvement over RobustMPC.
Fig. 4(a) demonstrates that MERINA can outperform RobustMPC
with only a few of epochs, and achieve a QoE performance
comparable to that of BOLA (performs best in this dataset) with
around 200 training epochs (lasting about 10 minutes). To verify
the performance further, we show the CDFs of QoE improvement
of comparison algorithms over RobustMPC in Fig. 4(b), with
MERINA-Offline, MERINA-Adp-30 and MERINA-Adp-200
denoting the proposed algorithm that employs the NN weights
without adaptation, after 30-epoch adaptation, and after 200-
epoch adaptation, respectively. The results indicate that after
30-epoch adaptation, the proportion of sessions that achieve
much lower/higher QoE value than RobustMPC significantly
decreases/increases. And after 200-epochs adaptation, MERINA
has a similar distribution to BOLA, in terms of average QoE
improvement. While Comyco’s performance cannot be improved
rapidly due to its low initial performance, and also because the
lifelong learning method cannot ensure policy improvement in a
significantly changed environment. The asymptotic performance of
MERINA indicates that it can achieve a superior QoE performance
when compared to all baselines following a meta-adaptation pro-
cedure, implying that MERINA can achieve the best generalization
performance and will outperform baseline algorithms across a range
of throughput dynamics through the adaptation.
6
CONCLUSION
We have proposed the meta-RL-based adaptive video streaming
system MERINA to learn a generalized ABR algorithm. Specifically,
we introduced a model-free context-based system framework,
composed of a probabilistic inference network (latent encoder)
that inferred the underlying dynamics from the recent throughput
context, and a latent-conditioned policy network that learned to
rapidly adapt to unfamiliar throughput dynamics. We implemented
the meta-training and meta-adaptation procedures for MERINA,
and demonstrated its efficiency through empirical evaluations on
multiple datasets and a real-world platform. The proposed idea
for MERINA is not limited to the throughput dynamics. It, in fact,
can be extended to video content (e.g., each video chunk may be
encoded with different rate-distortion curves w.r.t. video content),
which will be one of our future research directions.
ACKNOWLEDGMENTS
This work was supported in part by NSFC under Grants 61931023,
61831018, 61871267, 62120106007, 61972256, T2122024, 62125109, by
Shanghai Rising-Star Program 20QA1404600 and SJTU-UCL Global
Strategic Partnership Fund. (Corresponding author: Chenglin Li.)
3013
```


### Pagina 9
```text
Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning
MM ’22, October 10–14, 2022, Lisboa, Portugal
REFERENCES
[1] Zahaib Akhtar, Yun Seong Nam, Ramesh Govindan, Sanjay Rao, Jessica Chen,
Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan, and Hui Zhang. 2018. Oboe:
Auto-Tuning Video ABR Algorithms to Network Conditions. In Proceedings of
the Conference of the ACM Special Interest Group on Data Communication. 44–58.
[2] Federal Communications Commission. 2016. Raw Data - Measuring Broadband
America. (2016).
https://www.fcc.gov/reports-research/reports/measuring-
broadband-america/raw-data-measuring-broadband-america-2016
[3] Chelsea Finn, Pieter Abbeel, and Sergey Levine. 2017. Model-agnostic meta-
learning for fast adaptation of deep networks. In International conference on
machine learning. PMLR, 1126–1135.
[4] Dash Industry Forum. 2022. Catalyzing the Adoption of MPEG-DASH.
https:
//dashif.org/
[5] Matteo Gadaleta, Federico Chiariotti, Michele Rossi, and Andrea Zanella. 2017.
D-DASH: A Deep Q-Learning Framework for DASH Video Streaming. IEEE
Transactions on Cognitive Communications and Networking 3, 4 (2017), 703–718.
[6] Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. 2018. Soft
Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a
Stochastic Actor. In Proceedings of the 35th International Conference on Machine
Learning. 1861–1870.
[7] Tianchi Huang, Chao Zhou, Xin Yao, Ruixiao Zhang, Chenglei Wu, Bing Yu,
and Lifeng Sun. 2020. Quality-Aware Neural Adaptive Video Streaming With
Lifelong Imitation Learning. IEEE Journal on Selected Areas in Communications
38, 10 (2020), 2324–2342.
[8] Tianchi Huang, Chao Zhou, Rui-Xiao Zhang, Chenglei Wu, Xin Yao, and Lifeng
Sun. 2019. Comyco: Quality-Aware Adaptive Video Streaming via Imitation
Learning. In Proceedings of the 27th ACM International Conference on Multimedia
(Nice, France) (MM ’19). 429–437.
[9] Apple Inc. 2022. HTTP Live Streaming. https://developer.apple.com/streaming/
[10] Nuowen Kan, Chenglin Li, Caiyi Yang, Wenrui Dai, Junni Zou, and Hongkai Xiong.
2021. Uncertainty-Aware Robust Adaptive Video Streaming with Bayesian Neural
Network and Model Predictive Control. In Proceedings of the 31st ACM Workshop
on Network and Operating Systems Support for Digital Audio and Video (Istanbul,
Turkey) (NOSSDAV ’21). 17–24.
[11] Diederik P Kingma and Max Welling. 2013. Auto-Encoding Variational Bayes.
arXiv:1312.6114 [cs.LG]
[12] Clare Lyle, Mark Rowland, and Will Dabney. 2022. Understanding and Preventing
Capacity Loss in Reinforcement Learning. In Proceedings of International
Conference on Learning Representations. 1–12.
[13] Hongzi Mao, Shannon Chen, Drew Dimmery, Shaun Singh, Drew Blaisdell,
Yuandong Tian, Mohammad Alizadeh, and Eytan Bakshy. 2020. Real-world
Video Adaptation with Reinforcement Learning. arXiv:2008.12858 [cs.NI]
[14] Hongzi Mao, Ravi Netravali, and Mohammad Alizadeh. 2017. Neural Adaptive
Video Streaming with Pensieve. In Proceedings of the Conference of the ACM
Special Interest Group on Data Communication. 197–210.
[15] Anusha Nagabandi, Gregory Kahn, Ronald S. Fearing, and Sergey Levine. 2018.
Neural Network Dynamics for Model-Based Deep Reinforcement Learning with
Model-Free Fine-Tuning. In 2018 IEEE International Conference on Robotics and
Automation (ICRA). 7559–7566.
[16] Kate Rakelly, Aurick Zhou, Chelsea Finn, Sergey Levine, and Deirdre Quillen.
2019. Efficient Off-Policy Meta-Reinforcement Learning via Probabilistic Context
Variables. In Proceedings of the 36th International conference on machine learning.
5331–5340.
[17] Haakon Riiser, Paul Vigmostad, Carsten Griwodz, and Pål Halvorsen. 2013.
Commute Path Bandwidth Traces from 3G Networks: Analysis and Applications.
In Proceedings of the 4th ACM Multimedia Systems Conference. 114–118.
[18] John Schulman, Philipp Moritz, Sergey Levine, Michael Jordan, and Pieter Abbeel.
2018. High-Dimensional Continuous Control Using Generalized Advantage
Estimation. arXiv:1506.02438 [cs.LG]
[19] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov.
2017. Proximal Policy Optimization Algorithms. arXiv:1707.06347 [cs.LG]
[20] I. Sodagar. 2011. The MPEG-DASH Standard for Multimedia Streaming Over the
Internet. IEEE MultiMedia 18, 4 (2011), 62–67.
[21] Kevin Spiteri, Rahul Urgaonkar, and Ramesh Sitaraman. 2016. BOLA: Near-
Optimal Bitrate Adaptation for Online Videos. In Proceedings of the 35th Annual
IEEE International Conference on Computer Communications. 1–9.
[22] Yi Sun, Xiaoqi Yin, Junchen Jiang, Vyas Sekar, Fuyuan Lin, Nanshu Wang,
Tao Liu, and Bruno Sinopoli. 2016. CS2P: Improving Video Bitrate Selection
and Adaptation with Data-Driven Throughput Prediction. In Proceedings of the
Conference of the ACM Special Interest Group on Data Communication. 272–285.
[23] Francis Y. Yan, Hudson Ayers, Chenzhi Zhu, Sadjad Fouladi, James Hong, Keyi
Zhang, Philip Levis, and Keith Winstein. 2020. Learning in situ: A Randomized
Experiment in Video Streaming. In Proceedings of the 17th USENIX Symposium
on Networked Systems Design and Implementation (NSDI 20). 495–511.
[24] Xiaoqi Yin, Abhishek Jindal, Vyas Sekar, and Bruno Sinopoli. 2015. A Control-
Theoretic Approach for Dynamic Adaptive Video Streaming over HTTP. In
Proceedings of the 2015 ACM Conference on Special Interest Group on Data
Communication. 325–338.
3014
```


### Pagina 10
```text
MM ’22, October 10–14, 2022, Lisboa, Portugal
Nuowen Kan et al.
Appendix
A
IMPLEMENTATION DETAILS
We implement MERINA on a desktop equipped with a 40-core Intel
Xeon Silver 4114 Processor, 64GB DDR4 DRAM and an NVIDIA
GeForce RTX 2080 graphics card. The inference neural network
and the policy neural network that consists of an actor network
and a critic network are constructed and trained on PyTorch-1.9.0.
Note that we train MERINA on the GPU to maximize the efficiency,
though it can be trained on CPUs as well.
A.1
Inference Network
The throughput context 𝒄𝑘−𝑝:𝑘= {(𝐶𝑘−𝑝,𝑑𝑘−𝑝), · · · , (𝐶𝑘−1,𝑑𝑘−1)}
includes the average throughput values and time intervals of
throughput measurements collected from the download of previous
𝑝chunks. In this paper, we set 𝑝= 8 and input the context
information of 𝑈𝑘−8 until chunk 𝑈𝑘−1 (i.e., {𝐶𝑘−8, · · · ,𝐶𝑘−1} and
{𝑑𝑘−8, · · · ,𝑑𝑘−1}) separately into two one-dimensional convolution
layers with 128 filters of size 4 with stride 1. The results of these
two convolution layers are then merged into a fully connected layer
with 512 neurons, followed by a LeakyReLU activation function.
The collected features are finally fed into the output layer, which
consists of two parallel fully connected layers with 64 neurons,
which represent the outputs of 𝑓𝜇
𝜙(𝒄) and 𝑓𝜎
𝜙(𝒄), respectively, with
the latent variable 𝒛having a dimension of |𝑍| = 64.
A.2
Policy network
The actor and critic networks have the same architecture except
for the output layer, but do not share their parameters. The state
of the video streaming system, includes the features as detailed in
Section 2, is fed into the input layer of the actor and critic networks.
Concretely, for the set of available bitrate versions A, we use a
one-dimensional convolution layer with 128 filters, each of size
4 with stride 1, to process them. Meanwhile, five full connected
layers with 128 neurons are placed at the input layer to deal with
the remaining features of the state, including the measured average
throughput 𝐶𝑘−1, time duration 𝑑𝑘−1 during the download of the
last video chunk, current buffer occupancy 𝐵𝑘, selected bitrate 𝑎𝑘−1
of the last chunk, and the number of video chunks that have not
been downloaded yet. For the latent variable sampled from the
posterior 𝑞𝜙(𝒛|𝒄), we also use a fully connected layer with 1280
neurons to process the latent representations. Additionally, these
individual input layers for different information are all followed
by the LeakyReLU activation function. The results of the input
layers are then merged into two full connected layers (512 and 128
neurons) that equip with the LeakyReLU activation function and
are eventually followed by the output layer. The output of actor
network consists of a fully connected layer with 𝑀= 6 neurons
followed by the softmax activation function, which generates the
probability of being the optimal choice for each available bitrate
version. While the output of critic network includes a linear neuron
(with no activation function) which outputs the estimate of the state-
value function. Note that increasing the number of parameters of
NNs is not the key factor in improving QoE, particularly in terms
of the generalization capability.
A.3
Virtual Player
The virtual player, with reference to the open-sourced ABR simula-
tor used by Pensieve and Comyco, includes three key components:
1) a video client that emulates the video playback and the buffer oc-
cupancy; 2) a video delivery simulator that emulates the download
of available video chunks from the video server to the client, under
network conditions that are emulated from our stated datasets of
network throughput, along with an 80 ms RTT and a packet loss rate
of 0.95; and 3) an ABR controller that employs the ABR algorithms
(e.g., MERINA and other baseline algorithms) to decide the rule of
which bitrate version being requested for the next requested video
chunk that has not been downloaded yet.
The whole video streaming process can be summarized as
follows. At the beginning of video streaming, the video client
first obtains the video information, including the number of total
video chunks and the available bitrates for corresponding chunks.
The client then requests video chunks one by one, using the ABR
controller to select the bitrate for future chunks. The requested
bitrate version of chunks are downloaded through the video
delivery simulator. Once completely downloaded, a video chunk is
played back to the client. The playback information, such as buffer
occupancy, rebuffering event, bitrate version of the current chunk,
is collected to calculate the QoE value during the playback.
B
ADDITIONAL EXPERIMENTAL RESULTS
B.1
Consistency on Out-of-Distribution Traces
As with the log-form quality metric 𝑄𝑜𝐸𝑙𝑜𝑔, we compare the
consistency of MERINA to other baseline algorithms here, with
the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛on in-distribution and out-of-
distribution datasets. The NN weights of learning-based algorithms
are the same to those used in Section. 5.1 (i.e., learned from the
F&H dataset). We also present the numerical results in Table 2 by
using the same format.
The primary difference between the findings for 𝑄𝑜𝐸𝑙𝑜𝑔and
𝑄𝑜𝐸𝑙𝑖𝑛is that MERINA and Fugu performs better with the metric
𝑄𝑜𝐸𝑙𝑖𝑛than with the metric 𝑄𝑜𝐸𝑙𝑜𝑔on the Puffer-Oct.17-21 dataset.
MERINA, in particular, achieves a comparable performance in terms
of the average chunk QoE value to BOLA, which also performs
best on the Puffer-Oct.17-21 dataset. These results indicate that by
using the 𝑄𝑜𝐸𝑙𝑖𝑛quality metric, MERINA presents a generalization
capability consistently across all the throughput dynamics in
these five datasets, without the requirement of any adaptation.
This might be because the linear quality metric produces bigger
quality intervals between the bitrate versions than the log-form
metric, resulting in a more distinct feature for the bitrate selection.
Additionally, Fugu outperforms RobustMPC in terms of the average
chunk quality on the two puffer datasets when using the metric
𝑄𝑜𝐸𝑙𝑖𝑛, but performs much worse when using the metric 𝑄𝑜𝐸𝑙𝑜𝑔.
B.1.1
Real-World Test for 𝑄𝑜𝐸𝑙𝑖𝑛. With the same settings for
𝑄𝑜𝐸𝑙𝑜𝑔, we evaluate the learning-based algorithms MERINA and
Comyco, and the heuristic algorithms BOLA and RobustMPC, by
using the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛in the real world platform
under three different network conditions: a 4G cellular network,
a public WiFi network on campus, and a wide area network
connecting Shanghai and Los Angeles, with mean and standard
3015
```


### Pagina 11
```text
Improving Generalization for Neural Adaptive Video Streaming via Meta Reinforcement Learning
MM ’22, October 10–14, 2022, Lisboa, Portugal
Table 2: Performance comparison of different ABR algorithms in terms of the average chunk 𝑄𝑜𝐸𝑙𝑖𝑛value on different datasets.
Mean ± std (𝑅𝑔𝑎𝑝)
FCC
HSDPA
Oboe
Puffer-Oct.17-21
Puffer-Feb.18-22
BOLA
0.96 ± 0.54 (−20%)
1.12 ± 0.81 (−16%)
1.96 ± 1.03 (−16%)
0.86 ± 1.83 (+1%)
0.66 ± 2.90 (−26%)
RobustMPC
0.98 ± 0.75 (−18%)
1.22 ± 1.20 (−9%)
2.30 ± 1.24 (−2%)
0.73 ± 2.16 (−14%)
0.81 ± 2.97 (−9%)
Pensieve
1.13 ± 0.65 (−5%)
1.28 ± 0.95 (−5%)
2.26 ± 1.15 (−4%)
0.14 ± 11.55 (−84%)
0.55 ± 8.67 (−44%)
Comyco
1.15 ± 0.73 (−3%)
1.34 ± 1.05 (0%)
2.29 ± 1.21 (−2%)
−0.13 ± 2.86 (−115%)
0.68 ± 3.06 (−24%)
Fugu
1.11 ± 0.70 (−7%)
1.24 ± 1.04 (−7%)
2.31 ± 1.21 (−1%)
0.74 ± 2.13 (−13%)
0.83 ± 2.99 (−7%)
BayesMPC
1.10 ± 0.83 (−8%)
1.26 ± 1.11 (−6%)
2.29 ± 1.23 (−2%)
0.33 ± 2.80 (−61%)
0.66 ± 3.34 (−26%)
MERINA
1.19 ± 0.67
1.34 ± 0.99
2.34 ± 1.15
0.85 ± 2.02
0.90 ± 2.97
MERINA (nMI with 𝜆= 0)
1.08 ± 0.66 (−9%)
1.22 ± 1.11 (−9%)
2.25 ± 1.19 (−4%)
0.50 ± 2.68 (−61%)
0.72 ± 2.99 (−19%)
Dataset distribution
1.13 ± 0.44 Mbps
1.61 ± 0.95 Mbps
2.60 ± 2.08 Mbps
1.85 ± 0.91 Mbps
1.60 ± 0.88 Mbps
0
1
2
3
4
5
4G
Public WiFi
International Link
Average  value
BOLA
RobustMPC
Comyco
MERINA
Figure 5: Comparison of 𝑄𝑜𝐸𝑙𝑖𝑛without adaption.
deviation of recorded throughput values of 4.52 ± 0.74𝑀𝑏𝑝𝑠,
2.52 ± 1.06𝑀𝑏𝑝𝑠and 1.63 ± 1.16𝑀𝑏𝑝𝑠. The same test video is
loaded repeatedly on each network using a randomly chosen ABR
scheme. Each experiment takes about 1 hour to complete, and the
NNs weights for MERINA and Comyco are all trained on the F&H
dataset. Fig. 5 illustrates the real-world results of four comparison
algorithms without adaptation on these three scenarios. It can
be seen that MERINA surpasses the other baseline algorithms on
the public WiFi and international link conditions, but performs
slightly worse than Comyco under 4G condition. Comyco, on
the other hand, achieves the highest average chunk QoE value
under 4G conditions, but performs poorly under public WiFi and
international link conditions. These real-world test for 𝑄𝑜𝐸𝑙𝑖𝑛still
can demonstrate the generalization capability of MERINA when
deployed in the real-world scenarios.
B.2
Fast Adaptation To New Environments
Though MERINA performs slightly worse than BOLA in terms
of the average chunk QoE value on the throughput dynamics of
Puffer-Oct.17-21 when using the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛, we
examine here MERINA’s ability to rapidly adapt to this dataset
and study how much improvement can be achieved through
adaptation. All the settings w.r.t. the meta-adaptation procedures
are the same to those of Section 5.3, with the associated results
illustrated in Fig. 6. It can be seen from Fig. 6(a) that when
using the linear quality metric 𝑄𝑜𝐸𝑙𝑖𝑛, MERINA can surpass BOLA
(0.86) in terms of average chunk QoE value with around 100
training epochs (see MERINA-Adpt) and achieves a much higher
chunk QoE value 1.10 asymptotically (see MERINA-Asy). It is also
seen that MERINA’s performance will degrade after a few update
epochs and then improve monotonously. This is because the initial
parameters 𝜙and 𝜃may be near a local optimum for the new
throughput dynamics, while exploring for a higher value (towards
the global optimum) may experience a performance degradation
(a) Adaptation Curves
#FUUFS
(b) Puffer-Oct.17-21
Figure 6: a) The adaptation curves of MERINA and Comyco,
and b) average chunk 𝑄𝑜𝐸𝑙𝑖𝑛improvement over RobustMPC.
at first and then the performance improvement. Additionally, we
show the CDFs of QoE improvement of comparison algorithms
over RobustMPC in Fig. 6(b), with MERINA-Offline, MERINA-
Adp-100 and MERINA-Adp-1100 denoting the proposed algorithm
that employs the NN weights without adaptation, after 100-
epoch adaptation (before the performance degradation), and after
1100-epoch adaptation (performance improved again after the
degradation), respectively. The results suggested that, after 1100-
epoch adaptation, the proportion of sessions that achieve high QoE
value rise significantly.
B.3
Ablation Study
Finally, we conduct some experiments to demonstrate the benefit to
generalization as introduced by the proposed mutual information-
based regularization function in Eq. (5), providing a further insight
on MERINA. We train a modified version of MERINA, named
MERINA (nMI), by setting 𝜆= 0 for the actor loss, on the training
dateset F&H, and then evaluate its QoE performance on all the five
datasets. The results of average chunk QoE achieved by MERINA
(nMI) are also presented in Tables 1 and 2 for 𝑄𝑜𝐸𝑙𝑜𝑔and 𝑄𝑜𝐸𝑙𝑖𝑛,
respectively, which reveal a critical finding: the mutual information-
based regularizer improves the average QoE performance and
generalization on both in- and out-of-distribution datasets. This
demonstrates that the regularization function facilitates the latent
variable’s expressiveness (i.e. a more informative representation)
to bitrate selection in mixed dynamics, therefore enhancing the
generalization. In addition, without the imitation learning-based
pre-training, the learning process of MERINA will be exceedingly
unstable, and the training will always fall into a local optimum.
This phenomenon may result from the probabilistic latent encoder
and the mix dynamics setting in our paper.
3016
```
