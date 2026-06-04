Chinese Journal of Electronics
vol. 34, no. 4, pp. 1309–1320, July 2025
https://doi.org/10.23919/cje.2024.00.202
RESEARCH ARTICLE
Learning Robust Adaptive Bitrate Algorithms with
Adversarial Inverse Reinforcement Learning
Ling Yi1,2 and Yongbin Qin1,2
1. Text Computing & Cognitive Intelligence Engineering Research Center of National Education Ministry, College of
Computer Science and Technology, Guizhou University, Guiyang 550025, China
2. State Key Laboratory of Public Big Data, College of Computer Science and Technology, Guizhou University,
Guiyang 550025, China
Corresponding author: Yongbin Qin, Email: ybqin@gzu.edu.cn
Manuscript Received July 31, 2024; Accepted December 4, 2024; Published Online December 31, 2024
Copyright © 2025 Chinese Institute of Electronics
Abstract — Adaptive bitrate (ABR) algorithms are crucial for video streaming services by dynamically adjusting
video bitrate based on current network conditions to ensure better quality of experience (QoE). However, traditional
ABR algorithms often face challenges in adapting to diverse network environments and fail to fully utilize expert
knowledge. In this study, we propose a novel approach using adversarial inverse reinforcement learning (AIRL) to
learn ABR algorithms. Unlike traditional methods, AIRL can effectively leverage expert demonstrations to learn ro-
bust reward functions and generate stable ABR policies. Simultaneously, the learned ABR policy adjusts based on
the updated reward function, aiming to closely emulate the video bitrate decision-making behavior of experts. More-
over, by decoupling the reward function, we can develop a more robust ABR strategy that can effectively adapt video
bitrates to significant fluctuations in network conditions, while also optimizing different video QoE objectives. We
conducted experiments across various network conditions, demonstrating that the proposed method exhibits stable
and superior performance.
Keywords — Adaptive bitrate algorithm, Quality of experience, Adversarial inverse reinforcement learning.
Citation — Ling Yi and Yongbin Qin, “Learning robust adaptive bitrate algorithms with adversarial inverse re-
inforcement learning,” Chinese Journal of Electronics, vol. 34, no. 4, pp. 1309–1320, 2025. doi: 10.23919/cje.2024.00.
202.
I. Introduction optimizes a specified quality of experience (QoE) metric
using Lyapunov optimization, or a combination of the
In recent years, video streaming volume has surged to
two schemes (e.g., model predictive control, MPC [4]).
comprise 75% of total internet traffic, accompanied by a
These methods require careful adjustment and fail to
growing demand for higher video quality from users [1]. adapt bitrate to different network bandwidths or differ-
In video live streaming or on-demand scenarios, videos ent QoE objectives. State-of-the-art MPC algorithm [4]
are encoded at various bitrates. Adaptive bitrate (ABR) determines bitrate by addressing a QoE maximization
algorithms select the optimal bitrate based on network problem over a future time horizon encompassing sever-
conditions or user preferences. Nevertheless, due to the al chunks. MPC achieves superior performance com-
limitation of network bandwidth, ABR algorithms may pared to methods utilizing fixed heuristics, as it directly
not consistently select for the optimal bitrate, leading to optimizes for the desired QoE objective. Nonetheless, the
low-quality video or video rebuffering. efficacy of MPC relies on an accurate model of system
The primary ABR algorithms encompass both fixed dynamics, specifically an anticipation of future network
heuristic methods and learning-based approaches. For ex- throughput. Our experiments reveal that MPC is sensi-
ample, rate-based (RB) algorithm [2] forecasts throughput tive to errors in throughput prediction and the duration
by calculating the harmonic mean of the past 5 chunk of the optimization horizon. Additionally, since BOLA
download throughputs. Or buffer-based approaches e.g., and MPC cannot adjust parameters according to specific
buffer occupancy based Lyapunov algorithm (BOLA) [3] network conditions and are too sensitive to parameters,
Associate Editor: Prof. Ding Wang, Beijing University of Technology.

1310 Chinese Journal of Electronics, vol. 34, no. 4
then Oboe [5] is proposed to automatically adjust param- demonstration anticipates future scenarios within a speci-
eters, which can enhance QoE value in specific scenarios. fied horizon and addresses an optimization challenge. It
In contrast, learning-based ABR algorithms dispense optimizes the QoE objective throughout this horizon,
with the need for predefined assumptions and instead di- taking into account the dynamics specific to the ABR
rectly learn from data-driven processes. Pensieve [6] was system. Subsequently, it identifies the primary solution
proposed to further improve QoE by using reinforcement step for the ensuing bitrate determination. In the genera-
learning (RL) to train a neural network to generate ABR tion phase, we optimize the generated ABR strategy us-
algorithms, which effectively solves the limitations of ex- ing a discriminator and enhance the exploration strategy
isting ABR algorithms. Imitation learning [7], by imitat- by maximizing entropy. Additionally, the learning ABR
ing the MPC approach, effectively learns the ABR algo- algorithm encounters various network conditions and dif-
rithm, but the method is only applicable to known envi- ferent video durations. To develop a robust ABR algo-
ronments and cannot be used for complex network sce- rithm, one that is not influenced by the dynamics of the
narios. Fugu [8] combines classical MPC control with a environment, we separate the reward function to learn a
learned network predictor, trained with supervised learn- more resilient ABR strategy across different network
ing in situ on data from the real deployment environ- conditions.
ment, enabling it to adapt to known network conditions.
II. Background and Motivation
Additionally, RL-based ABR (ABRL) [9] converts ABR
policy into a linear model for better comprehension and Today, hypertext transfer protocol (HTTP)-based adap-
safety, allowing human engineers to verify it while slight- tive streaming, known as dynamic adaptive streaming
ly increasing the average stall rate by 0.8%. Another ap- over HTTP (DASH), is the leading method for video de-
proach is to employ meta-RL techniques like model- livery. Figure 1 illustrates that the core principle behind
agnostic meta-learning (MAML) algorithm [10], [11] or video clients using the adaptive bitrate (ABR) algo-
Pearl [12]–[14] to adaptive bitrate to various network rithm for HTTP streaming is to dynamically select and
conditions. Moreover, Genet [15] introduces increasingly switch the most suitable video quality based on real-time
challenging environments through a curriculum learning network conditions, ensuring users receive a smooth and
strategy [16], enabling RL models to perform better high-quality viewing experience across various network
across a wider range of network environments. Zuo et al. environments. To further enhance the user experience,
[17] introduce Ruyi, an off-policy RL-based video stream- the ABR algorithm integrates preloading and buffering
ing system that integrates preference awareness into the strategies. Video clients proactively download and cache
QoE model and the ABR algorithm [18], [19]. It is opti- several video segments of varying quality levels. This en-
mized with a modified deep Q-learning algorithm using sures continuous, uninterrupted playback even in cases of
experience replay [20]. In short, these methods learn network instability or interruptions, minimizing disrup-
strategies from observed video client behavior but do not tions from frequent loading or buffering. However, due to
directly infer QoE rewards. Moreover, they lack adver- the complexity and heterogeneity of networks, current
sarial capabilities in adapting video bitrate to new net- ABR algorithms cannot optimize different QoE objec-
work conditions or video QoE objectives. tives, we use two examples to illustrate the limitations of
Essentially, ABR algorithms have been designed to the current ABR algorithm.
operate in any video streaming environment, across net-
works with very diverse and unique characteristics, but Video player
its “one-size-fits-all” approach is not adequate for the de-
Throughput
manding performance requirements of internet video predictor Video chunk
streaming traffic distribution. The problems are rooted in ABR
Video server
algorithm
the limitations of network bandwidth [3] and conflicting
Playback HTTP
QoE objectives (e.g., maximizing video bitrate vs. mini- buffer
mizing rebuffering time) [4]. Additionally, learned ABR
algorithms have significant limitations in generalization:
the learned reward functions lack robustness to network
changes, such as selecting the optimal bitrate in unseen
Play video
network conditions, and make it difficult to infer ABR
agents’ intentions [9], [21], [22]. In Section II, we illus-
trate this issue with two examples. Figure 1 The video player utilizes the ABR algorithm for HTTP
adaptive video streaming.
Facing these challenges, to learn a practical and
scalable ABR algorithm (PSABR) that can adapt video Case 1: The first scenario considers situations where
bitrate to heterogeneous network conditions, we intro- network throughput fluctuates. Figure 2(a) compares the
duce a novel ABR algorithm based on adversarial in- actual network throughput with the predicted through-
verse RL (AIRL). The proposed method is primarily di- put by MPC. As shown, MPC’s estimates are overly con-
vided into two stages. In the inference phase, expert servative, remaining consistently around 3 Mbps rather

Learning Robust Adaptive Bitrate Algorithms with Adversarial Inverse Reinforcement Learning 1311

| (a)            | 4   | Ours |     | (b)            | Ours |     |     |     |
| -------------- | --- | ---- | --- | -------------- | ---- | --- | --- | --- |
| )spbM( etartiB |     |      |     | )spbM( etartiB |      |     |     |     |
|                |     | MPC  |     |                | RL   |     |     |     |
|                | 3   |      |     |                | 2    |     |     |     |
2
1
1
|                        | 0 25 50 | 75 100 125 | 150 175 |                        | 0   | 25 50 75 | 100 125 | 150 175 |
| ---------------------- | ------- | ---------- | ------- | ---------------------- | --- | -------- | ------- | ------- |
| )s( noitazilitu reffuB |         |            |         | )s( noitazilitu reffuB |     |          |         |         |
|                        | Ours    |            |         |                        |     |          |         | Ours    |
30
|     | MPC |     |     | 40  |     |     |     | RL  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
20
20
10
|                   | 0 25 50 | 75 100 125 | 150 175 |                   | 0   | 25 50 75 | 100 125 | 150 175 |
| ----------------- | ------- | ---------- | ------- | ----------------- | --- | -------- | ------- | ------- |
| )spbM( tuphguorhT | 5       |            |         | )spbM( tuphguorhT |     |          |         |         |
|                   |         |            |         | 3.0               |     |          |         | RL      |
4
Real
2.5
3
2.0
2
|     | MPC |     |     | 1.5 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
Real
1.0
|     | 0 25 50 | 75 100 125 | 150 175 |     | 0   | 25 50 75 | 100 125 | 150 175 |
| --- | ------- | ---------- | ------- | --- | --- | -------- | ------- | ------- |
|     |         | Time (s)   |         |     |     | Time (s) |         |         |
Figure 2  Analyzing bitrate selection, buffer utilization, and throughput prediction using MPC, RL, and IRL algorithms on the FCC
dataset. (a) Case 1; (b) Case 2.
than the average 4 Mbps. These inaccurate predictions to effectively balance QoE components, such as prioritiz-
limit MPC’s ability to reach higher bitrates, even when ing  HD  bitrates  without  jeopardizing  buffer  stability,
the playback buffer occupancy stays stable. In contrast, rendering it unable to meet the specific needs of HD-fo-
the inverse RL (IRL)-generated algorithm effectively as- cused users.
sesses higher average throughput (despite fluctuations) In contrast, the IRL-generated algorithm successful-
and switches to the highest available bitrate when suffi-
ly aligns with user preferences. It rapidly builds the play-
cient buffer space is present. Here, the IRL-generated al- back buffer by fetching data at 750 kbps, then transi-
gorithm was trained on an extensive set of real network tions to 2850 kbps (an HD level), maintaining this quali-
traces, rather than simply emulating MPC in this experi- ty for nearly 70 s. This approach ensures consistent HD
ment. This enables it to make suitable bitrate decisions playback with minimal rebuffering, delivering a smoother
by learning the underlying intent of ABR algorithms. and more satisfying user experience.
Case  2:  In  our  second  scenario,  ABR  algorithms In summary, existing approaches fail to adapt video
based on RL and IRL were optimized for a new QoE bitrate to varying user preferences and dynamic network
metric designed for video users with a strong preference conditions, resulting in suboptimal bitrate selection. This
for high definition (HD) quality. This metric assigns high
limitation arises because MPC and RL cannot infer the
rewards to HD bitrates and low rewards to non-HD bit- underlying objectives of ABR or effectively account for
rates, while still prioritizing smooth playback and penal-
|     |     |     |     | the  complexities |     |  of  network |  variability. |  Consequently, |
| --- | --- | --- | --- | ----------------- | --- | ------------ | ------------- | -------------- |
izing rebuffering. To excel under this metric, an ABR al- they fall short in delivering personalized and adaptive
gorithm must ensure a sufficiently high playback buffer
bitrate decisions.

level to enable the video player to switch to and sustain
III. Methods
HD bitrates. This approach maximizes time spent in HD
streaming  while  minimizing  rebuffering  and  bitrate In this section, we employ inverse RL methods to learn
switches. However, achieving this balance requires opti-
ABR algorithms and enhance performance using adver-
mizing multiple QoE dimensions (video quality vs. re- sarial techniques. Subsequently, we decouple the learned
buffering), as selecting HD bitrates prematurely may de-
QoE reward adapt bitrate to heterogeneous network con-
plete the buffer and cause playback interruptions.
ditions.
| Figure 2(b) depicts the bitrate decisions of each al- |     |     |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
1. Learning ABR algorithms with AIRL
gorithm and their impact on the playback buffer. Both
RL and IRL-based algorithms were trained to optimize We aim to develop an ABR algorithm based on expert
for the new QoE metric. As shown, RL struggles to im- strategies (cid:25)(cid:3), which select the appropriate bitrate under
plement the intended policy. It maintains a medium- varying network conditions. Unlike traditional RL algo-
sized buffer and selects bitrates between 300 kbps and 1850 rithms that directly interact with the video client envi-
kbps (the lowest HD level). This occurs because RL fails ronment, our inverse RL (IRL) approach first learns the

|   1312 |     |     |     |     |     |     |     | Chinese Journal of Electronics, vol. 34, no. 4 |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- |
underlying reward function  r  (e.g., maximizing video bitrates, rebuffering time, and video switching frequency.
t
quality while minimizing rebuffering) from expert demon- We adopt the QoE metric provided by MPC [4]
strations (cid:25)(cid:3). The learned reward function is then used to
|     |     |     |     |     |     |     |     | ∑N  | N∑(cid:0)1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- |
train a robust ABR policy via reinforcement learning.
|     |     |     |     |     |     |     | QoEN | = q(R )(cid:0)(cid:22) |     | jq(R | )(cid:0)q(R | )j  |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---------------------- | --- | ---- | ----------- | --- |
|     |     |     |     |     |     |     |      | n                      | 1   | n+1  |             | n   |
Our method builds on the maximum causal entropy
|     |     |     |     |     |     |     |     | n=1 | n=1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
IRL framework [23], which models an entropy-regular-
∑N
ized Markov decision process (MDP)  (S;A;T;r;(cid:13);(cid:26) 0 ). (cid:0)(cid:22) T (5)
|                        |     |                                |     |     |     |     |     | 2   | n   |     |     |     |
| ---------------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Here, the state space  |     | S includes network throughput, |     |     |     |     |     |     |     |     |     |     |
n=1
chunk download time, and playback buffer occupancy.
where a video consists of N chunks, q((cid:1)) represents video
The discrete action space A corresponds to the bitrates
for the next video chunk. The transition dynamics of net- quality metrics such as structure similarity index meas-
work conditions are defined by T(s′js;a). The discount ure (SSIM) [26] or video multi-method assessment fusion
factor is denoted by (cid:13) 2(0;1), and (cid:26)  denotes the ini- (VMAF) [27] (we evaluated both SSIM and VMAF in
0
|                          |     |     |     |     |     |     | this work to better assess video variations). Here, (cid:22) |     |     |     |     |  and |
| ------------------------ | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | ---- |
| tial state distribution. |     |     |     |     |     |     |                                                              |     |     |     |     | 1    |
The goal is to find the optimal policy (cid:25)(cid:3) that maxi-
|     |     |     |     |     |     |     | (cid:22) 2  are non-negative weight coefficients corresponding to |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- |
mizes the expected entropy-regularized QoE reward video quality switching frequency and rebuffering time,
respectively.
|     |     | [   |     |     |     | ]   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | ∑T  |     |     |     |     |     |     |     |     |     |     |
|     |     |     | (   |     |     | )   |     |     |     |     |     |     |
(cid:3) =argmaxE (cid:13)t )+H((cid:25)((cid:1)js 2. Expert demonstration
| (cid:25) |     | (cid:28)(cid:24)(cid:25) | r(s t ;a t |     | t )) | (1) |     |     |     |     |     |     |
| -------- | --- | ------------------------ | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
(cid:25)
|     |     | t=0 |     |     |     |     | Rather than directly learning the ABR policy, IRL aims |     |     |     |                    |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | ------------------ | --- |
|     |     |     |     |     |     |     | to deduce the QoE reward function r                    |     |     |     | (s ;a ) from a set |     |
|     |     |     |     |     |     |     |                                                        |     |     | t   | t t                |     |
where  (cid:28) =(s 1 ;a 1 ;s 2 ;a 2 ;:::;s T ;a T )  is  a  trajectory  of of demonstrations D =f(cid:28) g, assuming these are
;:::;(cid:28)
states and actions, the optimal policy (cid:25)(cid:3)(ajs) is given 1 N
generated by an optimal policy (cid:25)(cid:3)(ajs). In video bitrate
| as (cid:25)(cid:3)(ajs)/expfQ(cid:3) |       | (s;a)g [24], H((cid:1)) is the policy en- |              |     |            |     |                                                      |     |     |     |     |     |
| ------------------------------------ | ----- | ----------------------------------------- | ------------ | --- | ---------- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
|                                      |       | soft                                      |              |     |            |     | adaptation, once the network bandwidth is known, the |     |     |     |     |     |
| tropy  term                          |  that |  encourages                               |  exploration |  by |  promoting |     |                                                      |     |     |     |     |     |
playback buffer dynamics become predictable: each bi-
higher entropy.
|     |     |     |     |     |     |     | trate  decision |  deterministically |     |  determines |     |  the  video |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------------------ | --- | ----------- | --- | ----------- |
The value function V(cid:25)(s) in RL is defined as
quality and stall duration. Given varying network band-
|     |     | [   |     |     | ]   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  ∑1 width, selecting the optimal bitrate a for a state s re-
V(cid:25)(s)=E (cid:13)tr(s ;a )js =s (2) duces to a dynamic programming problem, where the
|     |     |     | t t | 0   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
goal is to maximize QoE by balancing video quality and
t=0
|                                                          |     |     |     |      |     |     | rebuffering |  time.  To  address |     |  this,  MPC |  [4] |  optimizes |
| -------------------------------------------------------- | --- | --- | --- | ---- | --- | --- | ----------- | ------------------- | --- | ----------- | ---- | ---------- |
| where (cid:13) is the discount factor (0(cid:20)(cid:13) |     |     |     | <1). |     |     |             |                     |     |             |      |            |
QoE over multiple upcoming video chunks. Unlike fixed-
| Assuming |     |  the  rewards  | r(s ;a | )  are  bounded, |     |  i.e., |     |     |     |     |     |     |
| -------- | --- | -------------- | ------ | ---------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
t t
heuristic methods, MPC explicitly solves a QoE objec-
| jr(s ;a )j(cid:20)R |     | , the geometric series property ensures |     |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t t max tive optimization problem, often achieving superior per-
that
formance. Therefore, we infer the QoE reward function
|     |     | ∑1  | 1   |     |     |     | using the MPC method to develop the ABR algorithm. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
(cid:13)t
|     |     |     | =   |     |     | (3) | Define a feature function f(s;a), which character- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
1(cid:0)(cid:13)
t=0 izes the state-action pair in adaptive video streaming sce-
Thus, the value function V(cid:25)(s) is finite and con- narios. For example, f(s;a) may include buffer occupan-
verges as cy, video bitrate, playback smoothness, and network con-
ditions. Different users may have varying QoE objec-
|     |     |                         |         | 1   |     |     |                                                            |     |     |     |     |     |
| --- | --- | ----------------------- | ------- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- |
|     |     | jV(cid:25)(s)j(cid:20)R | (cid:1) |     |     |     |                                                            |     |     |     |     |     |
|     |     |                         |         |     |     | (4) | tives, such as prioritizing video resolution or minimizing |     |     |     |     |     |
max 1(cid:0)(cid:13)
rebuffering. We define a linear reward function based on
This demonstrates the convergence of V(cid:25)(s) under user preferences as follows:
| discounted |  rewards, |  ensuring |  stability |  in |  the  learning |     |     |     |     |     |     |     |
| ---------- | --------- | --------- | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     | r(s;a)=(cid:18)Tf(s;a) |     |     |     | (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- |
process.
The discriminator reaches its global minimum when
where (cid:18) is the parameter vector to be learned. By opti-
| the ABR policy  |     | (cid:25) aligns with the expert policy  |     |     |     | (cid:25) | ,   |     |     |     |     |     |
| --------------- | --- | --------------------------------------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
E
mizing (cid:18), the system can dynamically adapt the reward
which was used to collect the demonstration data [25].
function to match user-specific QoE goals.
At this point, the discriminator outputs 1 for every state-
The expert’s behavior is described by their policy (cid:25)(cid:3),
2
| action pair (s;a). Hence, it follows that exp(f |     |     |     |     | (s;a))=  |     |                                                          |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | -------- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                 |     |     |     |     | (cid:18) |     | where the probability of taking action a in state s fol- |     |     |     |     |     |
(cid:25) (ajs). This can also be written as the expression
E
f(cid:3)(s;a)=log(cid:25) (ajs)=A(cid:3)(s;a), lows a softmax distribution
|     |     |     |  indicating |     |  that |  the |     |     |     |     |     |     |
| --- | --- | --- | ----------- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- |
E
| policies are aligned.                             |     |                             |     |                |     |     |     |         | exp(Q(cid:3)(s;a)) |      |     |     |
| ------------------------------------------------- | --- | --------------------------- | --- | -------------- | --- | --- | --- | ------- | ------------------ | ---- | --- | --- |
|                                                   |     |                             |     |                |     |     |     | T(ajs)= |                    |      |     | (7) |
| QoE metric: The ABR environment evaluates differ- |     |                             |     |                |     |     |     |         |                    | Z(s) |     |     |
| ent actions a                                     |     | , reflects the quality of a |     | , and improves |     |     |     |         |                    |      |     |     |
|                                                   | t   |                             |     | t              |     |     |     |         |                    |      |     |     |
where Z(s) is the partition function defined as
| the policy (cid:25) | (cid:18) | . r t (s t ;a t ) reflects the quality of different |     |     |     |     |     |     |     |     |     |     |
| ------------------- | -------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Learning Robust Adaptive Bitrate Algorithms with Adversarial Inverse Reinforcement Learning 1313
∑
(cid:3) ′ to significant variations in reward feedback for estimat-
|     |     | Z(s)= | exp(Q | (s;a)) |     | (8) |     |     |     |     |     |     |     |
| --- | --- | ----- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ing the reward function.
a′

|     | The value Q(cid:3)(s;a) represents the action-value func- |     |     |     |     |     |     |     |     |     |     |         |     |
| --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
|     |                                                           |     |     |     |     |     |     |     | 4   |     |     | Trace 1 |     |
Trace 2
tion, which combines the immediate reward and the ex-
| pected future value, as shown in (9). |     |     |     |     |     |     |     |     | 2   |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
drawer EoQ
∑
|     |           |                       |     |     |                 |            |     |     | 0   |     |     |     |     |
| --- | --------- | --------------------- | --- | --- | --------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
|     | Q (cid:3) | (s;a)=r(s;a)+(cid:13) |     | T(s | ′js;a)V (cid:3) | (s ′ ) (9) |     |     |     |     |     |     |     |
|     |           |                       |     | s′  |                 |            |     |     | −2  |     |     |     |     |
where r(s;a) is the immediate reward, and the second
−4
term captures the discounted future value with discount
|     |     |     |     |     |     |     |     |     | 0   | 20 40 | 60  | 80  | 100 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
factor (cid:13). The normalization term Z(s) ensures that the
5
action probabilities form a valid probability distribution,
smoothing the decision-making process.
|     |     |     |     |     |     |     |     | )spbM( htdiwdnaB | 4   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
By learning the optimal weight vector (cid:18), the ABR
| agent can align its decisions with individual user prefer- |     |     |     |     |     |     |     |     | 3   |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ences, thereby enhancing QoE.
|     |     |     |     |     |     |     |     |     | 2   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3. Decoupling rewards
Trace 1
| However, when learning the ABR algorithm from real- |     |     |     |     |     |     |     |     | 1   |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Trace 2
world video streaming scenarios, it encounters diverse
|     |     |     |     |     |     |     |     |     | 0   | 20 40 | 60  | 80  | 100 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
network situations, and existing solutions often lack the
Time (s)
robustness to handle these effectively. Suppose an IRL
Figure 3  Examples show how varying network bandwidths affect re-
| algorithm                                                 |  recovers |  a  |  shaped, |  policy-invariant |     |  reward |                |     |     |     |     |     |     |
| --------------------------------------------------------- | --------- | --- | -------- | ----------------- | --- | ------- | -------------- | --- | --- | --- | --- | --- | --- |
| r′(s;a;s′) under an MDP M where (cid:8)̸=0. In this case, |           |     |          |                   |     |         | ward feedback. |     |     |     |     |     |     |

there exist MDP pairs M and M′ such that changing
To eliminate undesired reward shaping, the learned
the transition model from T to T′ breaks policy invari-
|     |     |     |     |     |     |     | reward |  function |  should |  depend |  solely |  on  the |  current |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ------- | ------- | ------- | -------- | -------- |
ance on MDP M′. For example, consider deterministic
state s. This requires network dynamics to satisfy a de-
dynamics T(s;a)!s′ and state-action rewards
|     |     |                                                         |     |     |     |      | composability                                        |     |  condition, |  where |  functions |  over |  current |
| --- | --- | ------------------------------------------------------- | --- | --- | --- | ---- | ---------------------------------------------------- | --- | ----------- | ------ | ---------- | ----- | -------- |
|     |     |                                                         |     |     |     |      | and next states can be isolated from their sum f(s)+ |     |             |        |            |       |          |
|     | r   | ′ (s;a)=r(s;a)+(cid:13)(cid:8)(T(s;a))(cid:0)(cid:8)(s) |     |     |     | (10) |                                                      |     |             |        |            |       |          |
g(s′).
The method presented in generative adversarial imi-
It is evident that changing the dynamics from T to
T′(s;a)̸=T(s;a) means that  r′(s;a) no tation learning (GAIL) [28] cannot learn a state-only
T′ such that
|     |     |     |     |     |     |     | QoE reward function r |     |     | (s), as it does not prevent re- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | ------------------------------- | --- | --- | --- |
longer lies in the equivalence class defined by (10) for M′. (cid:18)
ward shaping [21]. To address this, we propose modify-
In other words, due to the dynamic nature of network
ing GAIL’s discriminator as follows:
conditions, the learned reward function is influenced by
various scenarios, ultimately affecting decisions on video   expff (s;a;s′)g
| bitrate. |     |     |     |     |     |     |     | D          | (s;a;s | ′ )=  | (cid:18);ϕ              |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ----- | ----------------------- | --- | --- |
|          |     |     |     |     |     |     |     | (cid:18);ϕ |        | expff | (s;a;s′)g+(cid:25)(ajs) |     |     |
(cid:18);ϕ
Consider the illustrative example shown in Figure 3,
| where |  a  fixed |  buffer-based |  ABR |  policy |  is |  utilized  to |         |     |            |                 |              |                |     |
| ----- | --------- | ------------- | ---- | ------- | --- | ------------- | ------- | --- | ---------- | --------------- | ------------ | -------------- | --- |
|       |           |               |      |         |     |               | where f |     | (s;a;s′)=g | (s;a)+(cid:13)h | (s′)(cid:0)h | (s). The shap- |     |
make bitrate decisions at time 0. We formalize this no- (cid:18);ϕ (cid:18) ϕ ϕ
ing term mitigates undesired effects on the reward ap-
tion by studying policy invariance in two MDPs trace1
|                                                         |     |     |     |     |     |     | proximator g |     | .        |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | --- | --- | --- | --- |
| and trace 2 which share the same reward and differ only |     |     |     |     |     |     |              |     | (cid:18) |     |     |     |     |
The algorithm alternates between training a discrim-
T′,
| in  the |  dynamics, |  denoted |  as  | T  and  |  respectively. |     |     |     |     |     |     |     |     |
| ------- | ---------- | -------- | ---- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
inator to distinguish expert data from policy-generated
Even with a fixed policy, if future traces include high
samples and updating the policy to deceive the discrimi-
bandwidth (e.g., trace 1), the reward feedback will be
|     |     |     |     |     |     |     | nator. This approach allows g |     |     |     | (cid:18) (s) to depend solely on |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | -------------------------------- | --- | --- |
substantial since the network can support high bitrates
the state, disentangling rewards from video streaming
without stalling. Conversely, if network conditions wors-
dynamics.
en (e.g., trace 2), the reward may be below average.
Algorithm 1 summarizes how to learn ABR algo-
Moreover, video duration affects the number of ABR in-
rithms from heterogeneous network environments using
teractions, determining the total training reward for the
AIRL.
RL agent (e.g., longer viewing time in trace 1 results in a
higher total reward). The key issue is that trace differ-
Algorithm 1  Learning ABR algorithms using AIRL
ences are unrelated to bitrate behavior at time 0—band-
1: Sample heterogeneous networks p(env);
| width |  may |  fluctuate  due |  to |  network |  randomness, |  or |     |     |     |     |     |     |     |
| ----- | ---- | --------------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
2: Collect expert trajectories (cid:28)E;
| users may stop watching regardless of quality. This leads |     |     |     |     |     |     |     |     |     | i   |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|   1314 |     |     |     |     |     |     |     |     |     | Chinese Journal of Electronics, vol. 34, no. 4 |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- |
3: Initialize ABR policy (cid:25) and discriminator D ; where, ED represents the expectation over expert data,
(cid:18);ϕ
|                               |     |     |     |     |     |     |     | and E |  represents the expectation over data sampled |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --------------------------------------------- | --- | --- | --- | --- |
| 4: for step t in f1;:::;Ng do |     |     |     |     |     |     |     |       | (cid:25)t                                     |     |     |     |     |
from the current policy.
| 5:　　Collect trajectories (cid:28) |     |     | =(s | ;a ;:::;s | ;a  | ) by executing (cid:25) |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
i 1 1 t t Step 3  The reward r(s;a) is inferred from the dis-
| 6:　　Train D |     | (cid:18);ϕ  using binary logistic regression to classify |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
criminator’s output. The reward function is given by
|     | expert data (cid:28)E from samples (cid:28) |     |     |     | ;   |     |     |     |     |     |     |     |     |
| --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |                                             |     | i   |     | i   |     |     |     |     |     |     |     |     |

7:　　Update reward r(s;a) using gradient descent: r ′ (s ;a)=log(D (s;a;s ′ ))(cid:0)log(1(cid:0)D (s;a;s ′ )) (13)
|                  |     |            |                              |     |            |     |     |     |     | (cid:18);ϕ |     | (cid:18);ϕ |     |
| ---------------- | --- | ---------- | ---------------------------- | --- | ---------- | --- | --- | --- | --- | ---------- | --- | ---------- | --- |
| 　　　　　(cid:0)logD |     |            | (s;a;s′)(cid:0)log(1(cid:0)D |     | (s;a;s′))  |     |     |     |     |            |     |            |     |
|                  |     | (cid:18);ϕ |                              |     | (cid:18);ϕ |     |     |     |     |            |     |            |     |
This reward is used to replace the standard rein-
| 8:　　Update (cid:25) with respect to r |     |     |     |  using the duel-PPO [29] |     |     |     |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:18);ϕ forcement learning objective, enabling the policy to learn
policy optimization method;
| 9: end for |     |     |     |     |     |     |     | from expert demonstrations effectively. |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- |
Step 4  For a given video, we modify the output of

4. Training methodology the final softmax layer in the police network by apply-
ing a mask [30]. This mask ensures that the output prob-
We use the AIRL approach as shown in Figure 4, which
ability distribution includes only the bitrates supported
demonstrates the interaction between the generator (pol-
by the video. The mask is represented by a binary vec-
icy network) and discriminator in generating ABR algo-
|                                        |     |     |     |     |     |     |     | tor [m                          | ;m ;:::;m | ], where each m |     |  is either 0 or 1. Giv- |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --------- | --------------- | --- | ----------------------- | --- |
| rithms based on expert demonstrations. |     |     |     |     |     |     |     |                                 | 1 2       | k               |     | i                       |     |
|                                        |     |     |     |     |     |     |     | en the neural network output [z |           |                 |     | ;z ;:::;z ], the modi-  |     |
|                                        |     |     |     |     |     |     |     |                                 |           |                 |     | 1 2 k                   |     |
fied softmax is calculated as

Expert
|     | demonstration |     | Real |     |     |     |     |     |     |          |     | ezi |      |
| --- | ------------- | --- | ---- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | ---- |
|     |               |     |      |     |     |     |     |     |     |          | m   | i   |      |
|     |               |     |      |     |     |     |     |     |     | (cid:25) | = ∑ |     | (14) |
i
|     |     |     |     |     | Discriminator |     |     |     |     |     |     | m ezj |     |
| --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | ----- | --- |
j
j
|     | ABR algorithm |     | Fake |     |     |     |     |                |                                                |     |     |     |     |
| --- | ------------- | --- | ---- | --- | --- | --- | --- | -------------- | ---------------------------------------------- | --- | --- | --- | --- |
|     |               |     |      |     |     |     |     | where (cid:25) | i  is the normalized probability for action i. |     |     |     |     |

IV. Experiments and Analysis
| Figure 4  Adversarial |     |     |  Inverse  Reinforcement |     |  Learning |  framework |     |     |     |     |     |     |     |
| --------------------- | --- | --- | ----------------------- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
generates ABR algorithms based on expert demonstration data and
In this section, we experimentally evaluate PSABR on
a discriminator.
|     |     |     |     |     |     |     |     | different network traces and QoE metrics. Furthermore, |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- |
The training process is described as follows: we analyze the performance of PSABR on different video
|     | Step 1  The policy (cid:25) |     |  samples trajectories based on |     |     |     |     |                   |     |     |     |     |     |
| --- | --------------------------- | --- | ------------------------------ | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
|     |                             |     | E                              |     |     |     |     | user preferences. |     |     |     |     |     |

network traces, i.e., (s;a), where s is the state of the
1. Implementation
video player, a is the bitrate of the next video chunk. In-
We selected the NVIDIA RTX A6000 graphics process-
| put is the state s |     |     | t , which includes 6 variables, namely: |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ing unit, 64-bit Ubuntu 20.04, and macOS operating sys-
| throughtput C |     | , chunk download time dk(R |     |     |     | )/C | , next |     |     |     |     |     |     |
| ------------- | --- | -------------------------- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
|               |     | t                          |     |     |     | k   | k      |     |     |     |     |     |     |
chunk  sizes  R ,  and  the  buffer  size  B ,  remaining tem as the experimental platform, and development tools
|     |     | n+1 |     |     |     | t   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
such as Python 3.6, Torch 1.6, Apache2, Google Chrome,
| chunks N and chunk bitrate R |     |     |     | .   |     |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n
Neural networks: The generator and discriminator and FFmpeg. We use Mahimahi to simulate network
conditions, with round-trip time (RTT) ranging from 0
use the same network structure. The number of hidden
layers is 1, and 128 convolution kernels and a fully con- ms to 80 ms, based on collected network traces between
the client and server.
nected network are used for feature extraction. The size
The QoE metric parameters of equation (5) are set
of the convolution kernel is 4 and the step size is 1.
Step 2  The discriminator is optimized for (cid:25)  and as N is 8, (cid:22)  is 4.3, and (cid:22)  is 1. During the training pro-
|                 |                                                              |     |     |     |     |     | E   |                                               | 1   |     | 2   |                     |     |
| --------------- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | ------------------- | --- |
|                 |                                                              |     |     |     |     |     |     | cess, the size of each epoch is 100, (cid:13) |     |     |     | =0:99, Relu activa- |     |
| f ((cid:28)), D | ((cid:28)) represents the probability of trajectory (cid:28) |     |     |     |     |     |     |                                               |     |     |     |                     |     |
| (cid:18)        | (cid:18)                                                     |     |     |     |     |     |     |                                               |     |     |     |                     |     |
according to the learned model, f ((cid:28)) (learned function) tion function [31] and the Adam optimizer [32] are used.
(cid:18)
During the whole experiment, according to the change of
is the output of the model for trajectory (cid:28), and (cid:25)((cid:28)) is
the loss function, the learning rates of the generator and
the probability of trajectory (cid:28) under the behavioral poli-
discriminator networks are adjusted to 0.0001 and 0.001
cy (expert trajectory).
respectively.
  expff ((cid:28))g Network Traces  To evaluate PSABR and existing
|     |     | D   | ((cid:28))= | (cid:18) |     |     | (11) |     |     |     |     |     |     |
| --- | --- | --- | ----------- | -------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
(cid:18) expff ((cid:28))g+(cid:25)((cid:28)) ABR algorithms on different networks, we use FCC [33],
(cid:18)
3G/HSDPA [34] and Belgium/4G [35] public network
The discriminator is trained to minimize the follow- traces, and the dataset features are as follows. The FCC
dataset contains 1 million network traces with an average
ing cross-entropy loss:
network throughput of 2100 s each trace, granularity of
|     |     |     | ∑T  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5 s, and a throughput range of 0–111 Mbit/s, generated
|     | L((cid:18))= |     | ((cid:0)ED[logD |            |        | ′   |     |     |                  |        |            |                  |      |
| --- | ------------ | --- | --------------- | ---------- | ------ | --- | --- | --- | ---------------- | ------ | ---------- | ---------------- | ---- |
|     |              |     |                 | (cid:18);ϕ | (s;a;s | )]  |     |     |                  |        |            |                  |      |
|     |              |     |                 |            |        |     |     | on  |  trains,  buses, |  cars, |  etc.  The |  HSDPA  dataset: |  the |
t=0 granularity of user generation in subways, trams, trains,
|     |     |     | (cid:0)E [log(1(cid:0)D |            |        | ′    |      |     |     |     |     |     |     |
| --- | --- | --- | ----------------------- | ---------- | ------ | ---- | ---- | --- | --- | --- | --- | --- | --- |
|     |     |     | (cid:25)t               | (cid:18);ϕ | (s;a;s | ))]) | (12) |     |     |     |     |     |     |
buses and ferries is 1 s, the number of traces is 86, and

Learning Robust Adaptive Bitrate Algorithms with Adversarial Inverse Reinforcement Learning 1315
the throughput range is 0–3 Mbit/s. we utilize robust MPC (RMPC) to achieve better perfor-
| We utilized the Puffer dataset [8], which had over |     |     |     | mance. |     |     |
| -------------------------------------------------- | --- | --- | --- | ------ | --- | --- |
63508 video users in 2020, streaming a total of 38.6 years • Comyco [7]: Utilizing imitation learning to mimic
of video content in the past year. And now, in 2024, the MPC [4], aiming to make the learned ABR algo-
there are even more video users and streams. These net- rithm similar to the MPC algorithm.
works exhibit variable characteristics with heavy-tailed • Fugu [8]: Training neural networks through super-
vised learning and then selecting video bitrates based on
distributions. For this work, we selected and used 8 dif-
| ferent datasets. |     |     |     | MPC. |     |     |
| ---------------- | --- | --- | --- | ---- | --- | --- |

To evaluate the performance of PSABR in different
2. Evaluation
network scenarios, we compared VMAF (i.e., QoE user
Network datasets including FCC, HSDPA, and Belgium/
preferences) and rebuffering time. VMAF is an advanced
4G; Video: divided into 48 video chunks, each chunk has video quality assessment metric that accurately evalu-
approximately 4 s, the total duration is 193 s; H.264/
ates human subjective perception and video quality. A
MPEG-4 encoding: {300, 750, 1200, 1850, 2850, 4300} higher VMAF score indicates better video quality, lead-
kbps; Video player: Google Chrome (built-in DASH.js),
ing to improved user QoE. Figure 5 demonstrates that
playback buffer capacity is set to 60 s, all ABR algo- PSABR can offer better QoE across various scenarios, in-
rithms run in dash.js; Video server: Apache2, video is de- dicating  higher  video  quality  and  less  buffering  time.
ployed on the server.
Overall, there is a VMAF improvement ranging from 4.3%
ABR algorithms  We compare PSABR with the fol- to 9.6%, with a reduction in stall time of 1.1%–6.2%.
lowing state-of-the-art bitrate selection algorithms.
MPC requires accurate network bandwidth prediction.
• Buffer occupancy based Lyapunov algorithm (BO- However, due to the variability of the network, MPC
LA) [3]: Optimizing buffer occupancy using Lyapunov al- struggles with  accurate  prediction.  Inaccurate   predic-
gorithm. Since the playback buffer is relatively stable, it tions can result in video buffering and low-quality video
can effectively improve QoE. playback. Comyco and Fugu are essentially based on imi-
• Pensieve [6]: Using deep RL to train the ABR al-
tation learning and supervised learning. Due to their in-
gorithm based on observations of network conditions and ability to explore different network conditions, they per-
video player. form poorly when adapting to new network scenarios.
• MPC [4]: Maximizes bitrate selection to achieve BOLA is based on control rules using buffer occupancy,
predefined QoE objectives based on predictions within but it cannot generalize to unknown network scenarios.
the next five video chunks, taking into account buffer In these heterogeneous network scenarios, PSABR dem-
occupancy and network throughput. In this experiment, onstrates sufficient foresight to adapt bitrate according
|     |       | Two dimentional QoE for car |     |     | Two dimentional QoE for bus |      |
| --- | ----- | --------------------------- | --- | --- | --------------------------- | ---- |
|     | (a)68 |                             |     | (b) |                             | BOLA |
|     |       |                             |     | 80  |                             | RMPC |
Fugu
|     | 67         |     |     |               |     | Pensieve |
| --- | ---------- | --- | --- | ------------- | --- | -------- |
|     | erocs FAMV |     |     | erocs FAMV 78 |     | Comyco   |
Our
66
76
BOLA
65 RMPC
|     |     | Fugu |     | 74  |     |     |
| --- | --- | ---- | --- | --- | --- | --- |
Pensieve
Comyco
|     | 64  |     |     | 72  |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Our
|     |               | 2 3 4 5                       | 6        |               | 1.2 1.4 1.6 1.8               | 2.0 2.2  |
| --- | ------------- | ----------------------------- | -------- | ------------- | ----------------------------- | -------- |
|     |               | Time spent on stall (%)       |          |               | Time spent on stall (%)       |          |
|     |               | Two dimentional QoE for ferry |          |               | Two dimentional QoE for metro |          |
|     | (c)           |                               | BOLA     | (d)           |                               | BOLA     |
|     |               |                               | RMPC     |               |                               | RMPC     |
|     | 80            |                               |          | 64            |                               |          |
|     |               |                               | Fugu     |               |                               | Fugu     |
|     |               |                               | Pensieve |               |                               | Pensieve |
|     | erocs FAMV 78 |                               | Comyco   | erocs FAMV 63 |                               | Comyco   |
|     |               |                               | Our      |               |                               | Our      |
76
62
74
61
72
60
2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0
|     |     | Time spent on stall (%) |     |     | Time spent on stall (%) |     |
| --- | --- | ----------------------- | --- | --- | ----------------------- | --- |
Figure 5  PSABR was compared with existing algorithms on videos from various scenarios on the 3G/HSDPA dataset, with assessments
made based on VMAF scores and time spent on stall. (a) Car; (b) Bus; (c) Ferry; (d) Metro.

|   1316 |     |     |     |     | Chinese Journal of Electronics, vol. 34, no. 4 |     |     |
| ------ | --- | --- | --- | --- | ---------------------------------------------- | --- | --- |
to different conditions, maximizing QoE. When network   1.0 (a) BOLA
|           |                    |           |                    | EoQ egareva dezilamroN | robustMPC |     |     |
| --------- | ------------------ | --------- | ------------------ | ---------------------- | --------- | --- | --- |
| bandwidth |  is  insufficient, |  the  ABR |  algorithm  should |                        |           |     |     |
Pensieve
|     |     |     |     | 0.8 | Fugu |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- |
swiftly establish playback at the lowest available bitrate
PSABR
| to utilize the playback buffer. Once network bandwidth |               |                  |                   | 0.6 |     |     |     |
| ------------------------------------------------------ | ------------- | ---------------- | ----------------- | --- | --- | --- | --- |
| or  buffer                                             |  availability |  improves,  then |  higher  bitrates |     |     |     |     |
0.4
should be selected to maximize QoE.

| 3. Video user preferences |     |     |     | 0.2 |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- |
Considering that ABR algorithms will encounter differ-
0
|     |     |     |     |     | QoE | QoE | QoE |
| --- | --- | --- | --- | --- | --- | --- | --- |
ent video user preferences in real-world network scenar- lin log hd
ios, here we consider three distinct QoE user preferences 1.0 BOLA
(b)
|     |     |     |     | EoQ egareva dezilamroN |     | robustMPC |     |
| --- | --- | --- | --- | ---------------------- | --- | --------- | --- |
as detailed in Table 1. Using Belgium/4G as the train- Pensieve
|     |     |     |     | 0.8 |     | Fugu |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
ing dataset. We observe that existing ABR algorithms
PSABR
struggle to optimize QoE objectives because they fail to
0.6
customize network conditions. Different QoE objectives
| need unique ABR strategies. For instance, with QoE |     |     |     | , 0.4 |     |     |     |
| -------------------------------------------------- | --- | --- | --- | ----- | --- | --- | --- |
log
| where higher bitrates provide diminishing returns in per- |     |     |     | 0.2 |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
ceived quality, the best approach is to avoid high bit-
0
rates when rebuffering risk is high. In contrast, optimiz-
|     |     |     |     |     | QoE | QoE | QoE |
| --- | --- | --- | --- | --- | --- | --- | --- |
ing  for  QoE   requires  a  more  aggressive  strategy. lin log hd
lin
PSABR can automatically learn these strategies, main-
|     |     |     |     | Figure 6  Comparing |  PSABR |  with  existing  ABR |  algorithms  on |
| --- | --- | --- | --- | ------------------- | ------ | -------------------- | --------------- |
taining high performance as conditions change. broadband and 3G/HSDPA networks. The QoE metrics consid-
  ered include different video user preferences. Results are normal-

Table 1  QoE models and their corresponding parameters ized against the performance of PSABR using Min-Max normaliza-
tion. Error bars span ± one standard deviation from the average
| Metrics |     |     | Rebuffer penalty (cid:22) |     |     |     |     |
| ------- | --- | --- | ------------------------- | --- | --- | --- | --- |
Bitrate utility q(R) QoE. (a) FCC broadband network; (b) 3G/HSDPA network.
QoE
lin R 4.3 ing Pensieve [6], a DRL-based ABR algorithm that uti-
| QoE | log(R/R | )   |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- |
log min 2.66 lizes the Asynchronous Advantage Actor-Critic (A3C)
0.3!1, 0.75!2, 1.2!3 framework to optimize video quality, rebuffering, and bit-
| QoE |     |     | 8   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
hd 1.85!12, 2.85!15, 4.3!20 rate smoothness; Meta-ABR [11], which quickly learns
|                     |     |                              |     | ABR policies from limited data using meta-RL to im- |     |     |     |
| ------------------- | --- | ---------------------------- | --- | --------------------------------------------------- | --- | --- | --- |
| The results for QoE |     |  highlight this further. QoE |     |                                                     |     |     |     |
hd hd prove performance. Since the official code is unavailable,
prioritizes HD video, giving the highest utility to the top
we implemented it ourselves using inner and outer loops;
three bitrates of our test video. As discussed in Section
|                        |     |                                |     | and  Jade                                          |  [18],  an  ABR |  algorithm  that |  incorporates |
| ---------------------- | --- | ------------------------------ | --- | -------------------------------------------------- | --------------- | ---------------- | ------------- |
| II, optimizing for QoE |     |  involves more long-term plan- |     |                                                    |                 |                  |               |
|                        |     | hd                             |     | ChatGPT-assisted human feedback in RL and utilizes |                 |                  |               |
ning than the other QoE metrics. When network band-
adaptive entropy to enhance QoE. To accommodate the
width is insufficient, the ABR algorithm should quickly
varying network conditions that the Puffer dataset may
build the playback buffer with the lowest bitrate. Once
experience, we have chosen 4K DASH videos. The bitrate
the buffer is large enough, it should directly switch to
ranges from 235 kbps to 40 Mbps to match the network
the lowest HD quality, skipping intermediate bitrates.
bandwidth. The specific bitrates are: 235 kbps, 375 kbps,
However, achieving a buffer level that avoids rebuffering
560 kbps, 750 kbps, 1.05 Mbps, 1.75 Mbps, 2.35 Mbps,
and ensures smooth playback requires significant fore-
3 Mbps, 3.85 Mbps, 4.3 Mbps, 15 Mbps, 25 Mbps, and 40
sight. As shown in Figure 6, PSABR can learn this poli-
cy without any tuning or designer intervention, whereas Mbps [36], providing a comprehensive evaluation of ABR
performance.
other methods like RMPC struggle with long-term strat-
As illustrated in Figure 7, vanilla RL Pensieve per-
egy optimization. PSABR can infer implicit QoE reward
structures from video user behavior rather than relying formed the worst due to its sample inefficiency and poor
adaptability to new network conditions. Meta-RL ABR
directly on explicit reward signals. This makes the algo-
rithm more flexible, capable of adapting to various defi- demonstrated  improved  performance  by  leveraging
nitions of reward signals. knowledge across multiple tasks but still suffered from
|     |     |     |     | high computational demands. Inverse RL outperformed |     |     |     |
| --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- |
V. Deep Dive
these methods by effectively mimicking expert behavior,
thereby enhancing generalization. The best performance
In this section, we analyze the efficiency of existing algo-
rithms and conduct an analysis in a long-duration video was achieved by adversarial inverse RL with decoupled
rewards (PSABR), which combined adversarial training
streaming environment.
  and  reward  decoupling  to  enable  robust  and  efficient
1. Comparing state-of-the-art RL algorithms
adaptation to varying network environments.
In order to evaluate the training efficiency of existing RL Comprehensive  review  To  evaluate  PSABR,  we
algorithms, we analyzed several ABR methods, includ- compared it with the ChatGPT-based human feedback

Learning Robust Adaptive Bitrate Algorithms with Adversarial Inverse Reinforcement Learning 1317
|     |            |     |     |     |     |            |     |     |     |
| --- | ---------- | --- | --- | --- | --- | ---------- | --- | --- | --- |
|     | 1.00       |     |     |     |     | 1.00       |     |     |     |
|     | 0.75       |     |     |     |     | 0.75       |     |     |     |
|     | 0.50       |     |     |     |     | 0.50       |     |     |     |
|     | drawer EoQ |     |     |     |     | drawer EoQ |     |     |     |
|     | 0.25       |     |     |     |     | 0.25       |     |     |     |
|     | 0          |     |     |     |     | 0          |     |     |     |
|     | −0.25      |     |     |     |     | −0.25      |     |     |     |
Gail
|     | −0.50 |     |     |     |     | −0.50 |     |     |     |
| --- | ----- | --- | --- | --- | --- | ----- | --- | --- | --- |
PSABR
|     |       |     |      | Meta-ABR |     |        |                | Jade           |      |
| --- | ----- | --- | ---- | -------- | --- | ------ | -------------- | -------------- | ---- |
|     | −0.75 |     |      |          |     | −0.75  |                |                |      |
|     |       |     |      | Pensieve |     |        |                | PSABR          |      |
|     | −1.00 |     |      | ×104     |     | −1.00  |                |                | ×105 |
|     | 0     | 1 2 | 3 4  | 5 6      |     | 0 0.25 | 0.50 0.75 1.00 | 1.25 1.50 1.75 | 2.00 |
|     |       |     | Step |          |     |        | Step           |                |      |
Figure 7  Comparing the QoE reward value of PSABR with exist- Figure 8  Comparing PSABR with ChatGPT human feedback-based
ing RL-based ABR algorithms on the Puffer dataset. RL ABR algorithms. Shaded area spans (cid:6) standard deviation.
RL ABR algorithm. The experiment utilized 1000 hours
ample, a video streaming client must choose bitrates for
of Puffer data. As shown in Figure 8, Jade exhibits un-
upcoming video chunks based on uncertain bandwidth
stable performance during training, possibly due to its
predictions, while maintaining robust performance across
reliance on large experiential datasets that do not gener-
varying screen sizes and network environments.
| alize |  well  to |  varying  network |  conditions. |  In  contrast, |     |     |     |     |     |
| ----- | --------- | ----------------- | ------------ | -------------- | --- | --- | --- | --- | --- |
Slow networks  To better evaluate image variations,
PSABR learns ABR strategies from expert demonstra-
we calculate the SSIM of the videos. This metric helps
tions, enabling it to adapt effectively to diverse scenarios.
|     |     |     |     |     | in assessing the quality of the video by comparing the |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- |
2. Different types of networks
structural similarity between frames [37], [38]. In the ex-
|     |     |     |     |     | perimental |  process, |  we  used  ffmpeg |  to  calculate |  the |
| --- | --- | --- | --- | --- | ---------- | --------- | ----------------- | -------------- | ---- |
Practical ABR optimization must adapt bitrate to di-
verse and unpredictable conditions that fixed, simplified, SSIM values for each ABR algorithm.
or machine learning models cannot fully capture. For ex- As shown in Figure 9, PSABR shows a reduction in
  Slow streams, 7956 streams, 1579 streams-hours Slow streams, 384089 streams, 50526 streams-hours
|     | (a) | BOLA    |     |     | (b) | BOLA |     |     |     |
| --- | --- | ------- | --- | --- | --- | ---- | --- | --- | --- |
|     |     | 1.2 BBA |     |     |     | BBA  |     |     |     |
1.0
|     |                      | Fugu         |     |     |                      | Fugu     |     |     |     |
| --- | -------------------- | ------------ | --- | --- | -------------------- | -------- | --- | --- | --- |
|     | )Bd( MISS dezilamroN | 1.0 Pensieve |     |     | )Bd( MISS dezilamroN | Pensieve |     |     |     |
|     |                      | MPC          |     |     | 0.8                  | MPC      |     |     |     |
|     |                      | 0.8 meta-ABR |     |     |                      | meta-ABR |     |     |     |
|     |                      | IRL-ABR      |     |     |                      | IRL-ABR  |     |     |     |
0.6
|     |     | 0.6 PSABR |     |     |     | PSABR |     |     |     |
| --- | --- | --------- | --- | --- | --- | ----- | --- | --- | --- |
0.4
0.4
0.2
0.2
0
|     |     | −0.2 |     |     |     | 0   |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
−0.4
0.200 0.175 0.150 0.125 0.100 0.075 0.050 0.025 0 3.0 2.5 2.0 1.5 1.0 0.5 0
|     |     |     | Time spent stalled (%) |     |     | Time spent stalled (%) |     |     |     |
| --- | --- | --- | ---------------------- | --- | --- | ---------------------- | --- | --- | --- |
Slow streams, 9475 streams, 1328 streams-hours Slow streams, 8253 streams, 1240 streams-hours
|     | (c)                  | BOLA         |     |     | (d)                  | BOLA     |     |     |     |
| --- | -------------------- | ------------ | --- | --- | -------------------- | -------- | --- | --- | --- |
|     |                      | 1.0 BBA      |     |     |                      | BBA      |     |     |     |
|     |                      | Fugu         |     |     |                      | 3 Fugu   |     |     |     |
|     | )Bd( MISS dezilamroN | 0.8 Pensieve |     |     | )Bd( MISS dezilamroN | Pensieve |     |     |     |
|     |                      | MPC          |     |     |                      | MPC      |     |     |     |
2
|     |     | 0.6 meta-ABR |     |     |     | meta-ABR |     |     |     |
| --- | --- | ------------ | --- | --- | --- | -------- | --- | --- | --- |
|     |     | IRL-ABR      |     |     |     | IRL-ABR  |     |     |     |
|     |     | PSABR        |     |     |     | PSABR    |     |     |     |
|     |     | 0.4          |     |     |     | 1        |     |     |     |
0.2
0
0
−1
−0.2
|     |     | 0.6 0.5 | 0.4 0.3                | 0.2 0.1 | 0   | 7 6 5                  | 4 3 2 | 1 0 |     |
| --- | --- | ------- | ---------------------- | ------- | --- | ---------------------- | ----- | --- | --- |
|     |     |         | Time spent stalled (%) |         |     | Time spent stalled (%) |       |     |     |
Figure 9  In slow networks (< 6 Mbps), we compared the SSIM and time spent stalled of videos across various streaming scenarios with
those of the existing state-of-the-art ABR algorithms, using a 95% confidence interval error bar. All QoE metrics were normalized using
Min-Max normalization, with PSABR as the baseline. (a) 7956 streams, 1579 stream-hours; (b) 384089 streams, 50526 stream-hours; (c) 9475
streams, 1328 stream-hours; (d) 8253 streams, 1240 stream-hours.

buffering time by 0.055%–2.6%. We found that the sim- encounter various types of network technologies and
ple buffer-based algorithm (BBA) can achieve better per- standards, including wired and wireless networks such as
formance, while the ABR algorithm generated purely Local Area Network, Wide Area Network, Wi-Fi, and
through RL training, known as Pensieve, performs poor- cellular networks (e.g., 3G, 4G, 5G). The challenges
ly. Meanwhile, we have observed that meta-RL does not faced by ABR algorithms on all networks primarily re-
consistently achieve optimal performance due to the need volve around the diversity and instability of network
for adaptation across a wide range of video stream condi- conditions, the variety of user devices, and the optimiza-
tions. In real-world scenarios with varying user prefer- tion of network resources utilization. In encountering
ences, BBA, which relies on fewer assumptions and re- these scenarios, ABR algorithms need to balance video
quests videos based on buffer occupancy, closely approxi- quality and rebuffering time to achieve better quality of
mates the actual video playback process. MPC predicts experience. We observed that in Figure 10(a), PSABR
bitrates based on past network bandwidth. However, in a achieves superior video quality, while in Figure 10(b) and
real environment, these network characteristics are com- Figure 10(c), it performs well in both video quality and
plex and variable, influenced by factors such as Trans- buffering time, with a reduction in buffering time by
mission Control Protocol and varying user preferences, 0.054%–0.14%. The overall improvement of all networks
making it challenging to adapt video bitrate to real net- relative to slow networks is relatively small, as slow net-
work conditions. Fugu exhibits weaker generalization in works are specifically targeted for scenarios where net-
unknown network conditions using supervised learning, work throughput is less than 6 Mbps. This inspires us
whereas IRL-ABR consistently performs well in these un- that in specific network scenarios, we can customize spe-
known networks and user preferences. Furthermore, cific ABR algorithms. For example, during peak hours,
PSABR achieves the best performance because it utilizes holidays, specific time periods, as well as particular net-
inverse RL methods to infer the true intent of the ABR work environments.
algorithm based on expert knowledge, thereby maximiz-
VI. Conclusion
ing video quality (SSIM) and reducing rebuffering time
in specific scenarios. In this work, we optimize the QoE objectives of different
All networks Considering that ABR algorithms will video users based on inverse RL in heterogeneous net-
(a) (b)
1.0
0.8
0.6
0.4
0.2
0
0.200 0.175 0.150 0.125 0.100 0.075 0.050 0.025 0
Time spent stalled (%)
(c) (d)
)Bd(
MISS
dezilamroN
1.0
0.8
0.6
0.4
0.2
0
0.200 0.175 0.150 0.125 0.100 0.075 0.050 0.025 0
Time spent stalled (%)
)Bd(
MISS
dezilamroN
1.2
1.0
0.8
0.6
0.4
0.2
0
−0.2
−0.4
0.6 0.5 0.4 0.3 0.2 0.1 0
Time spent stalled (%)
)Bd(
MISS
dezilamroN
1.2
1.0
0.8
0.6
0.4
0.2
0
−0.2
)Bd(
MISS
dezilamroN
1318 Chinese Journal of Electronics, vol. 34, no. 4
All streams, 435547streams, 107225 streams-hours All streams, 434757 streams, 107260 streams-hours
BOLA BOLA
BBA BBA
Fugu Fugu
Pensieve Pensieve
MPC MPC
meta-ABR meta-ABR
IRL-ABR IRL-ABR
PSABR PSABR
All streams, 11692 streams, 2500 streams-hours All streams, 103258 streams, 25002 streams-hours
BOLA BOLA
BBA BBA
Fugu Fugu
Pensieve Pensieve
MPC MPC
meta-ABR meta-ABR
IRL-ABR IRL-ABR
PSABR PSABR
0.40 0.35 0.30 0.25 0.20 0.15 0.10 0.05 0
Time spent stalled (%)
Figure 10 In all networks, we compared the SSIM and stall time of videos across various streaming scenarios with those of the existing
state-of-the-art ABR algorithms, using a 95% confidence interval error bar. (a) 435547 streams, 107225 streamhours; (b) 434757 streams, 107260
streamhours; (c) 11692 streams, 2500 stream-hours; (d) 103258 streams, 25002 streamhours.

Learning Robust Adaptive Bitrate Algorithms with Adversarial Inverse Reinforcement Learning 1319
work environments. Unlike previous learned methods IEEE Journal on Selected Areas in Communications, vol.
that directly train fixed QoE objectives, instead, we opti- 38, no. 10, pp. 2324–2342, 2020
[8] F. Y. Yan, H. Ayers, C. Z. Zhu, et al., “Learning in situ: A
mize different users’ QoE preferences based on expert
randomized experiment in video streaming,” in Proceedings
knowledge. This allows the learned ABR algorithm to se- of the 17th USENIX Conference on Networked Systems De-
lect the optimal bitrate across different scenarios, opti- sign and Implementation, Santa Clara, CA, USA, pp.
mizing conflicting QoE objectives. Additionally, we uti- 495–511, 2020.
[9] H. Z. Mao, S. Chen, D. Dimmery, et al., “Real-world video
lize adversarial training and decoupled QoE rewards to
adaptation with reinforcement learning,” in Proceedings of
make the learned ABR policy more robust when adapt-
the 36th International Conference on Machine Learning,
ing to significant variations and unencountered network Long Beach, CA, USA, 2019.
conditions. The experimental results show that across all [10] C. Finn, P. Abbeel, and S. Levine, “Model-agnostic meta-
considered video streaming scenarios, our approach re- learning for fast adaptation of deep networks”, in Proceed-
ings of the 34th International Conference on Machine Learn-
duces stall time by 0.054%-6.2% and enhances video
ing, New York, USA, pp. 1126–1135, 2017.
quality by 4.3%-9.4% compared to existing methods. [11] T. C. Huang, C. Zhou, R. X. Zhang, et al., “Learning tai-
Moreover, we can improve the comprehensiveness and lored adaptive bitrate algorithms to heterogeneous network
accuracy of video quality assessment by leveraging two conditions: A domain-specific priors and meta-reinforcement
learning approach,” IEEE Journal on Selected Areas in
key metrics: SSIM and VMAF. This enables a compre-
Communications, vol. 40, no. 8, pp. 2485–2503, 2022
hensive and thorough analysis and evaluation of video
[12] N. Kan, Y. K. Jiang, C. L. Li, et al., “Improving generaliza-
quality. Our approach offers a new perspective on video tion for neural adaptive video streaming via meta reinforce-
streaming methods, optimizing video distribution and en- ment learning,” in Proceedings of the 30th ACM Internation-
hancing the quality of user experience. al Conference on Multimedia, Lisboa, Portugal, pp.
3006–3016, 2022.
Acknowledgements [13] K. Rakelly, A. Zhou, C. Finn, et al., “Efficient off-policy
meta-reinforcement learning via probabilistic context vari-
This work was supported by the Joint Funds of the Na- ables”, in Proceedings of the 36th International Conference
on Machine Learning, New York, USA, pp. 5331–5340, 2019.
tional Natural Science Foundation of China (Grant No.
[14] “Meta rl”, Available at: https://github.com/katerakelly/oys-
62066008), the National Key R&D Program of China
ter, 2025-06-09.
(Grant No. 2023YFC3304500), and the Key Projects of [15] Z. X. Xia, Y. J. Zhou, F. Y. Yan, et al., “Genet: Automatic
Science and Technology of Guizhou Province (Grant No. curriculum generation for learning adaptation in networking,”
[2020]1Z055). We sincerely thank Prof. Li Zeping for his in Proceedings of the ACM SIGCOMM 2022 Conference,
Amsterdam, Netherlands, pp. 397–413, 2022.
guidance in video streaming. We would also like to ex-
[16] Y. Bengio, J. Louradour, R. Collobert, et al., “Curriculum
press our gratitude to the anonymous reviewers and the learning,” in Proceedings of the 26th Annual International
editor for their valuable comments and suggestions, Conference on Machine Learning, Montreal, Canada, pp.
which significantly improved the quality of this work. 41–48, 2009.
[17] X. T. Zuo, J. Y. Yang, M. W. Wang, et al., “Adaptive bi-
References trate with user-level QoE preference for video streaming,” in
Proceedings of the IEEE INFOCOM 2022-IEEE Conference
[1] “Cisco Annual Internet Report (2018--2023)”, Available at: on Computer Communications, London, United Kingdom,
https://www.cisco.com/c/en/us/solutions/executive-perspec- pp. 1279–1288, 2022.
tives/annual-internet-report/index.html, 2025-06-09. [18] T. C. Huang, R. X. Zhang, C. L. Wu, et al., “Optimizing
[2] Y. Sun, X. Q. Yin, J. C. Jiang, et al., “CS2P: Improving adaptive video streaming with human feedback,” in Proceed-
video bitrate selection and adaptation with data-driven ings of the 31st ACM International Conference on Multime-
throughput prediction,” in Proceedings of the 2016 ACM dia, Ottawa, Canada, pp. 1707–1718, 2023.
SIGCOMM Conference, Florianopolis, Brazil, pp. 272–285, [19] X. K. Wei, M. L. Zhou, S. Kwong, et al., “Reinforcement
2016. learning-based QoE-oriented dynamic adaptive streaming
[3] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: framework,” Information Sciences, vol. 569, pp. 786–803,
Near-optimal bitrate adaptation for online videos,” 2021
IEEE/ACM Transactions on Networking, vol. 28, no. 4, pp. [20] V. Mnih, K. Kavukcuoglu, D. Silver, et al., “Playing Atari
1698–1711, 2020 with deep reinforcement learning,” arXiv preprint, arXiv:
[4] X. Q. Yin, A. Jindal, V. Sekar, et al., “A control-theoretic 1312.5602, 2013.
approach for dynamic adaptive video streaming over HTTP,” [21] J. Fu, K. Luo, and S. Levine, “Learning robust rewards with
in Proceedings of the 2015 ACM Conference on Special In- adversarial inverse reinforcement learning,” arXiv preprint,
terest Group on Data Communication, London, United King- arXiv: 1710.11248, 2018.
dom, pp. 325–338, 2015. [22] Q. Feng, B. Letham, H. Z. Mao, et al., “High-dimensional
[5] A. Lekharu, S. Kumar, A. Sur, et al., “A QoE aware LSTM contextual policy search with unknown context rewards us-
based bit-rate prediction model for dash video,” in Proceed- ing Bayesian optimization,” in Proceedings of the 34th Inter-
ings of 2018 10th International Conference on Communica- national Conference on Neural Information Processing Sys-
tion Systems & Networks, Bengaluru, India, pp. 392–395, tems, Vancouver, Canada, article no. 1848, 2020.
2018. [23] B. D. Ziebart, Modeling Purposeful Adaptive Behavior with
[6] H. Z. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive the Principle of Maximum Causal Entropy. Carnegie Mellon
video streaming with pensieve,” in Proceedings of the Con- University, Schenley Park Pittsburgh, PA, United States,
ference of the ACM Special Interest Group on Data Commu- 2010.
nication, Los Angeles, CA, USA, pp. 197–210, 2017. [24] T. Haarnoja, H. R. Tang, P. Abbeel, et al., “Reinforcement
[7] T. C. Huang, C. Zhou, X. Yao, et al., “Quality-aware neural learning with deep energy-based policies,” in Proceedings of
adaptive video streaming with lifelong imitation learning,” the 34th International Conference on Machine Learning,

1320 Chinese Journal of Electronics, vol. 34, no. 4
Sydney, Australia, pp. 1352–1361, 2017. metrics,” in Proceedings of the 9th ACM Multimedia Sys-
[25] I. Goodfellow, J. Pouget-Abadie, M. Mirza, et al., “Genera- tems Conference, Amsterdam, Netherlands, pp. 460–465,
tive adversarial nets,” in Proceedings of the 27th Internation- 2018.
al Conference on Neural Information Processing Systems, [36] J. J. Quinlan and C. J. Sreenan, “Multi-profile ultra high def-
Montreal, Canada, pp. 2672–2680, 2014. inition (UHD) AVC and HEVC 4K DASH datasets,” in Pro-
[26] Z. Wang, A. C. Bovik, H. R. Sheikh, et al., “Image quality ceedings of the 9th ACM Multimedia Systems Conference,
assessment: From error visibility to structural similarity,”
Amsterdam, Netherlands, pp. 375–380, 2018.
IEEE Transactions on Image Processing, vol. 13, no. 4, pp.
[37] Z. F. Duanmu, K. Zeng, K. D. Ma, et al., “A quality-of-expe-
600–612, 2004
rience index for streaming video,” IEEE Journal of Selected
[27] Netflix, “Video multi-method assessment fusion”, Available
Topics in Signal Processing, vol. 11, no. 1, pp. 154–166, 2017
at: https://github.com/Netflix/vmaf, 2025-06-09.
[38] A. Alomar, P. Hamadanian, A. Nasr-Esfahany, et al.,
[28] J. Ho and S. Ermon, “Generative adversarial imitation learn-
“CausalSim: A causal framework for unbiased trace-driven
ing,” in Proceedings of the 30th International Conference on
simulation,” in Proceedings of the 20th USENIX Symposium
Neural Information Processing Systems, Barcelona, Spain,
pp. 4572–4580, 2016. on Networked Systems Design and Implementation, Boston,
[29] D. H. Ye, Z. Liu, M. F. Sun, et al., “Mastering complex con- MA, USA, pp. 1115–1147, 2023.
trol in MOBA games with deep reinforcement learning,” in
Proceedings of the 34th AAAI Conference on Artificial In- Ling Yi received the M.S. degree in com-
telligence, pp. 6672–6679, 2021. puter science in 2022 and is now pursuing the
[30] C. M. Bishop, Pattern Recognition and Machine Learning. Ph.D. degree at Guizhou University, Guiyang,
Springer, New York, NY, USA, pp. 1122–1128, 2006. China. His research interests include video
[31] J. Schmidt-Hieber, “Nonparametric regression using deep streaming technologies, network congestion
neural networks with ReLU activation function,” The An- control, natural language processing, and rein-
nals of Statistics, vol. 48, no. 4, pp. 1875–1897, 2020 forcement learning for real-world applications.
[32] Z. J. Zhang, “Improved Adam optimizer for deep neural net- (Email: yilingphd@gmail.com)
works,” in Proceedings of 2018 IEEE/ACM 26th Interna-
tional Symposium on Quality of Service, Banff, Canada, pp.
1–2, 2018.
Yongbin Qin is a Professor with the School of
[33] S. Bauer, D. Clark, W. Lehr, “Gigabit broadband measure-
Computer Science and Technology, Guizhou
ment workshop report,” ACM SIGCOMM Computer Com-
University, Guiyang, China. His primary re-
munication Review, vol. 50, no. 1, pp. 60–65, 2020
search interests include machine learning and
[34] H. Riiser, P. Vigmostad, C. Griwodz, et al., “Commute path
natural language processing.
bandwidth traces from 3G networks: Analysis and applica-
(Email: ybqin@gzu.edu.cn)
tions,” in Proceedings of the 4th ACM Multimedia Systems
Conference, New York, USA, pp. 114–118, 2013.
[35] D. Raca, J. J. Quinlan, A. H. Zahran, et al., “Beyond
throughput: A 4G LTE dataset with channel and context