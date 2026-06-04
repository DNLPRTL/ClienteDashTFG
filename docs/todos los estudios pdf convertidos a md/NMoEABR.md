This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665094
Generalizing Adaptive Video Streaming with
Mixture of Experts in Heterogeneous Wireless
Networks
Shuoyao Wang, Senior Member, IEEE, Boyuan Li, Xiaowen Cao, Member, IEEE, and Lifeng Xie, Member, IEEE
Abstract—Adaptivevideostreaminghasbecomeacoretechnol- Dynamic Adaptive Streaming over HTTP (DASH) stands
ogy for modern video delivery, particularly in cellular networks. out as a promising technology to efficiently deliver video
However, the growing dynamics of mobile environments and the
contentacrossdiversenetworkconditions[1].DASHsegments
diversity of user preferences present major challenges for adap-
video content into multiple chunks, each encoded at various
tivebitrate(ABR)algorithms.Existingapproachesoftenstruggle
to maintain a balance between high in-distribution performance bitrate levels. To ensure seamless playback, the client-side
and strong generalization across heterogeneous network condi- player employs an Adaptive BiRrate (ABR) algorithm, which
tionsandpersonalizedQualityofExperience(QoE)demands.To dynamically select the most appropriate bitrate for each seg-
addressthesechallenges,weproposeNMoEABR,aunifiedABR
mentbasedonreal-timenetworkconditions,bufferoccupancy,
decision-makingframeworkthatintegratesanonlinearMixture-
and playback status, thereby ensuring smooth streaming and
of-Experts (NMoE) architecture with preference-aware meta-
reinforcement learning. Specifically, we design an NMoE-based maximizing visual quality.
actornetworkthatadaptivelyaggregatesexpertpoliciesthrough Over the past decade, extensive research has focused on
dynamic convolution conditioned on real-time network states, ABR algorithms to enhance users’ quality of experience
thereby enhancing robustness and cross-network generalization
(QoE). These approaches can generally be divided into two
in a zero-hot manner. Furthermore, to mitigate convergence
categories: heuristic-based methods and learning-based meth-
difficulties arising from the joint optimization of expert policies
and expert-weight prediction, we introduce a preference-aware ods.Theformertypicallyemploycontrolrulestomakebitrate
meta-RL strategy that incorporates user preference embeddings decisions based on estimated network conditions [2], and
andvirtualpreferencesynthesistostabilizemeta-policyupdates. playback buffer size [3], or directly using model predic-
Comprehensive evaluations on real-world traces and wireless
tive control (MPC) [4]. However, such methods introduce
testbed demonstrate that NMoEABR consistently outperforms
a large number of parameters that require fine-tuning and
mainstreamABRbenchmarksintermsofaverageQoE,stability,
and adaptability, particularly under unseen network conditions often rely on assumptions about the operating environment,
and diverse user preference distributions. resulting in unstable performance. In contrast, some deep
IndexTerms—Adaptivevideostreaming,Generalizable,Meta- reinforcement learning (DRL)-based ABR methods, such as
RL, Mixture of Experts
Pensieve [5], have been proposed to enhance nonlinear policy
modeling capabilities. Although these methods demonstrate
I. INTRODUCTION
better performance in various simulation environments, they
Withthecontinuousadvancementofmobilecommunication are typically trained offline on specific network datasets and
technologies, video services have become increasingly diver- struggletogeneralizetopreviouslyunseennetworkconditions
sified, expanding from traditional video-on-demand to real- or user configurations. Moreover, they lack mechanisms for
time live streaming, virtual reality (VR), video conferencing, explicitlymodelinguser-levelQoEpreferencesandoftenincur
and short-form videos. These services have greatly enriched highcomputationalcostsduringpolicyadaptationanddeploy-
users’audiovisualexperiencesandsimultaneouslyhavedriven ment, which restricts their applicability in real-time and edge
a rapid increase in network bandwidth demands. Extensive scenarios. This limitation arises because existing approaches
studies have demonstrated a significant causal relationship typically optimize for average rewards or a single generalized
betweenvideoservicequalityanduserbehavior.Forinstance, policythatstrugglestoadapttodiverseuserpreferences.Con-
frequent playback interruptions considerably increases the sequently, existing ABR approaches still suffer from limited
likelihood of user abandonment. Accordingly, improving the flexibility and generalization across heterogeneous networks
stability and quality of video transmission has become a and diverse user profiles.
critical objective for enhancing user Quality of Experience The rising complexity of network environments and the di-
(QoE). versityofuserrequirementsdemandhighlyadaptableandgen-
eralizableABRstrategies,asshowninFig.1.Whileemerging
S. Wang, B. Li, and X. Cao are with the College of Electronic and technologies (e.g., 5G, millimeter-wave) provide higher band-
InformationEngineering,ShenzhenUniversity,Shenzhen518066,China.
width and lower latency, they also cause frequent handovers,
LifengXieiswithDepartmentofBroadbandCommunication,Pengcheng
Laboratory,Shenzhen518066,China. severethroughputfluctuations,anddynamictopologychanges,
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:41:18 UTC from IEEE Xplore. Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

Rebuffering
Quality
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665094
adaptation/generalization, especially for unseen scenario
generalization.
• Toenhanceadaptability,weproposetheNon-linearMoE
(NMoE)–based actor network architecture for ABR. By
employing dynamic convolution to non-linearly combine
expert policies conditioned on real-time network states,
the NMoE–based actor improves robustness and gener-
alization in diverse and complex network environments
(a) Hetergenous Network (b) Hetergenous Preference
with negligible additional computation overhead.
Fig. 1: Heterogeneous Challenges in Real-World Environments • To improve the convergence over heterogeneous user
preference and wireless networks, we introduce user
preference-aware meta-reinforcement learning strategy.
especially in high-mobility or cross-network scenarios [6]. Byincorporatingpreferenceembeddingsandvirtualpref-
Meanwhile, user QoE preferences vary widely across devices, erence synthesis technique, the meta-policy learns a con-
contexts, and content types [7], with some prioritizing visual tinuousandsmoothadaptationsurfaceoverthepreference
quality and others favoring playback continuity under con- space.
strained conditions. Moreover, content characteristics such as • We evaluate our framework on multiple real-world
sports,education,orentertainmentfurtherinfluencesensitivity traces and wireless testbeds. Results demonstrate that
to clarity, smoothness, and responsiveness. NMoEABR significantly outperforms mainstream ABR
In recent years, a few studies [8] [9] have proposed using strategies in terms of in-distribution average QoE as well
meta-reinforcement learning (meta-RL) to conduct extensive as generalization across networks and users.
offline training across diverse network conditions and person-
Thepaper’ssubsequentsectionsarestructuredasfollows.In
alized QoE objectives. However, these methods still require
Section II and III, we provide an overview of related research
non-negligible online training to adapt to the current environ-
andsystemmodel,respectively.SectionsIVencompassthein-
mentandoftensacrificesite-specificperformanceinexchange
troductionoftheproblemformulation,actornetworkarchitec-
for improved generalization across different networks. Over-
ture, and the implementation of meta-reinforcement learning
all, the limited adaptability and generalization capabilities of
strategy. Experimental results and performance analyses are
existing ABR strategies are becoming increasingly inadequate
presented in Section V. Lastly, the paper concludes in Section
to meet the demands of complex network environments and
VI.
heterogeneous user requirements.
To address these dual challenges posed by network hetero-
II. RELATEDWORKS
geneity and user preference diversity, this paper proposes a
A. Adaptive Video Streaming
unifiedzero-shotABRdecision-makingframeworkthatjointly
optimizes for generalization and personalization. Inspired by ABRschemesforvideostreamingcanbebroadlyclassified
the recent success of Mixture of Experts (MoE) in large into four categories: heuristic-based strategies, Model Predic-
language models [10], [11], we propose NMoE-ABR, a Non- tive Control (MPC)-based strategies, Reinforcement Learning
linearMixture-of-Experts–basedarchitecture.Inparticular,the (RL)-based strategies, and preference-aware and network-
key challenges for MoE-based ABR algorithms are twofold. aware strategies.
On the one hand, in conventional MoE, although only a 1) Heuristic: Heuristic-based ABR schemes include rate-
subsetofexpertsisactivated,thisstillintroducesconsiderable matching[12],whichalignsbitratewithestimatedthroughput,
additional inference overhead compared with learning-based and buffer-controlling [13], which regulates buffer occupancy
ABR methods that employ only a single decision network. to avoid rebuffering. However, maintaining buffer stability
Moreover, adaptive expert selection further increases com- often reduces bitrate utility under dynamic network condi-
putation. Thus, designing efficient MoE decision modules is tions. To address this, BBA+ [14] combines rate-matching
critical for high-frequency, latency-sensitive scenarios such and buffer-controlling via a nonlinear throughput-aware map-
as video streaming. Moreover, most MoE models rely on ping from buffer occupancy to bitrate decisions. Nonetheless,
large-scale supervised training, which is costly and ill-suited heuristic methods generally fail to balance multiple QoE
to ABR, where reinforcement learning already faces slow factors, such as bitrate utility and smoothness.
convergence. This highlights the need for efficient RL-based 2) Model Predictive Control: MPC-based methods seek to
training methods for ABR. To the best of our knowledge, we balanceQoEfactorsthroughthroughputpredictionandfuture-
areamongthefirsttointegratethelearning-basedABRpolicy aware bitrate selection. For example, RobustMPC [4] uses the
withMoEtechniques.Themaincontributionsofthisworkare harmonicmeanofpastthroughputtomaximizelong-termQoE
as follows: undertheassumptionofaccurateprediction.Subsequentwork
• We propose NMoEABR, an innovative ABR algorithm has focused on improving prediction accuracy, such as Oboe
integratingreal-timeMoEtechnique,capableofenhances [15], or refining prediction granularity, e.g., Fugu [16], which
both network conditions as well as user preferences predicts chunk-average rather than time-average throughput.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:41:18 UTC from IEEE Xplore. Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665094
Morerecentstudies[17],[18]modelthroughputasaprobabil- Overall, using MoE to design a unified ABR strategy
itydistribution.However,rapidlyfluctuatingwirelesschannels for QoE personalization and network heterogeneity offers
(e.g., in 5G) limit prediction accuracy, even in distributional distinct advantages. MoE consists of multiple experts, each
form, while the introduction of extra hyperparameters reduces specializing in different representational preferences, enabling
robustness across networks. adaptation to heterogeneous networks (e.g., 5G vs. WiFi).
3) Learning-based: Learning-based approaches leverage The gating network activates only a subset of experts per
machine learning, particularly deep reinforcement learning input, yielding an input-adaptive dynamic architecture. This
(DRL),todirectlyoptimize ABRpoliciesfromdata.Pensieve makes MoE an input-adaptive dynamic network structure,
[5] pioneered this paradigm using policy gradients to max- providing a new dimension of adaptability. In contrast, prior
imize QoE. Later extensions explored Multi-Agent RL [19], methods—including self-attention and meta-RL—use a fixed
[20],imitationlearning[21],[22],self-playRL[23],Decision computation graph regardless of the input features. Further-
Transformer [24], and hybrid RL–optimization methods [25]. more, MoE can enhance generalization to unseen scenarios
Despite their effectiveness in specific scenarios, these models by recombining existing experts.
oftenstruggletogeneralizeacrossheterogeneousnetworksand The key challenges for MoE-based ABR algorithms are
diverse QoE objectives due to limited adaptability of deep twofold.Ontheonehand,inconventionalMoE,althoughonly
architectures. a subset of experts is activated, this still introduces consider-
4) Preference-Aware and Network-aware: To meet hetero- able additional inference overhead compared with learning-
geneoususerpreference,priorworks[26]–[28]leveragemulti- based ABR methods that employ only a single decision
objectiveoptimization,meta-learning,andself-attention-based network.Moreover,adaptiveexpertselectionfurtherincreases
representation learning for personalized bitrate adaptation. To computation. Thus, designing efficient MoE decision modules
handle diverse network conditions, [29] and [30] introduces is critical for high-frequency, latency-sensitive scenarios such
spatial–temporal learning and information bottleneck based as video streaming. Moreover, most MoE models rely on
Meta-RLrespectivelytoimprovedomainadaptationabilityof large-scale supervised training, which is costly and ill-suited
DRL-based ABR. However, these methods degrade in unseen to ABR, where reinforcement learning already faces slow
scenarios and usually address either QoE personalization or convergence. Overall, the power of MoE, together with the
network heterogeneity, but not both. To tackle both aspects, challenges for MoE-based ABR, motivates this paper.
[8] [9] propose a meta-RL-based ABR system. However, this
method requires non-negligible online fine-tuning for domain
III. SYSTEMMODEL
adaptation.
A. Video Streaming Model
B. Mixture of Experts
We consider a DASH system where the source video is
The MoE framework is a model architecture that enhances
dividedintoI chunks,eachoflengthLseconds.Eachchunkis
representational capacity and computational efficiency by dy-
encoded into multiple versions at different bitrates. The ABR
namically routing inputs to a set of specialized expert subnet-
algorithm selects an appropriate bitrate to ensure high QoE.
works. Initially proposed by Jacobs et al. [31], MoE divides
Let R = {R ,R ,...,R } denote the set of available
theinputspacesuchthateachexpertfocusesonasubsetofthe 1 2 |R|
bitrates, ordered as R > R > ··· > R . The bitrate of
datadistribution,enablingspecializationandmodularlearning. 1 2 |R|
chunk i is denoted by r ∈R.
i
Modern deep learning implementations of MoE, such as
The client downloads chunks through a wireless downlink.
the sparsely-gated MoE introduced by [32], utilize a gating
The download time of chunk i is given by:
network to assign sparse, instance-specific weights to each
expert. This sparse gating mechanism enables conditional
s (r)
computation — only a small subset of experts are activated τ i = 1 (cid:82)ti i +τic dt , (1)
for each input, reducing overall computation while preserving τi ti t
large model capacity. The switch Transformer [33] further
where s (r) is the size of the chunk with bitrate r, t is the
improves scalability and efficiency by limiting each input to i i
start time, and c denotes the downlink bandwidth at time t.
a single expert, enabling training of models with hundreds of t
billions of parameters. Beyond natural language processing, To support smooth playback, a buffer is drained during
MoE has found successful applications in diverse domains, viewingandfilledwithLsecondsonceachunkisdownloaded.
such as multi-task learning [34] and resource scheduling [35]. The buffer occupancy when chunk i starts downloading is:
In sequence modeling, MoE enables specialized experts to
capture distinct temporal or contextual patterns. In multi- b i+1 =[b i −τ i ]++L, (2)
task learning, experts can focus on different tasks, facilitat-
ing knowledge sharing and task-specific specialization. For where [·]+ denotes the ceiling operation, b ∈[0,B], and B is
i
resource scheduling, dynamic routing helps allocate compu- thebuffercapacity.Ifb <τ ,thebufferdepletesandplayback
i i
tational resources adaptively based on input characteristics. stalls until the chunk completes.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:41:18 UTC from IEEE Xplore. Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665094
B. Problem Formulation where s is the initial state, π : S → A the policy, and γ ∈
0
(0,1] the discount factor.
The goal of ABR is to design a policy π that maximizes
overall QoE. Following [5], we adopt a cumulative QoE
function: IV. METHODOLOGY
I I I
(cid:88) (cid:88) (cid:88) As stated in (8), the bitrate selection problem is formulated
QoE=α q(r )−α |q(r )−q(r )|−α [τ −b ]+,
1 i 2 i i−1 3 i i
as a sequential decision-making problem under the MDP
i=1 i=2 i=1
(3) framework. The objective is to learn an optimal policy π :
where q(r ) is the video quality at bitrate r . The first term S →Athatmapseachsystemstates∈S toanactiona∈A,
i i
rewards higher quality, the second penalizes rebuffering, and aimingtomaximizetheexpectedcumulativerewardovertime.
the third penalizes quality variation. The weights α ,α and To improve exploration efficiency and policy robustness, we
1 2
α balance these factors. adopt an entropy-regularized objective function, defined as
3
The QoE maximization problem can be written as:
(cid:34) I (cid:35)
max QoE (4a) J(π)=Eπ (cid:88) γi(cid:0) v (s ,a )−λH(π(·|s )) (cid:1) , (9)
i i i i
r,τ,t
i=0
s.t. r ∈R,∀i, (4b)
i
s (r) where γ ∈[0,1) is the discount factor that controls the trade-
τ i = 1 (cid:82)ti i +τic dt ,∀i, (4c) off between short-term and long-term rewards, and v i (s i ,a i )
τi ti t denotes the immediate reward obtained by taking action a
i
b =[b −τ ]++L,∀i, (4d) at state s . The term λ ≥ 0 balances the impact of reward
i+1 i i i
t =t +τ ,∀i, (4e) maximization against policy entropy, encouraging a better
i+1 i i
exploration–exploitation trade-off.
with r ≜(r 1 ,...,r I ), τ ≜(τ 1 ,...,τ I ), and t≜(t 1 ,...,t I ). The policy entropy H(π(·|s)) is defined as
Since QoE depends on both bitrate and download time, auxil-
iaryvariablesτ andtareintroduced.Givenfullknowledgeof H(π(·|s))=− (cid:88) π(a|s)logπ(a|s), (10)
c ,(P1)isanMixedIntegerNonlinearProgramming(MINLP),
t a
generally intractable in real time.
In practice, c is unpredictable, particularly in wireless where π(a|s) represents the probability of selecting action a
t
networks.Thus,ABRmakessequentialbitratedecisionsbased when the system is in state s. Incorporating entropy into the
only on observable past and current information. This moti- objectiveensuresthattheagentavoidsprematureconvergence
vates formulating the problem as a Markov Decision Process to suboptimal deterministic strategies, thereby promoting di-
(MDP) with state, action, and reward. verse action exploration in highly dynamic environments.
1) Action: At the start of chunk i downloading, the action Given the objective in (9), the state-value function under
is the bitrate choice: policy π is defined as
a =r ∈R. (5) (cid:34) I (cid:35)
i i Vπ(s)=Eπ (cid:88) γi(cid:0) v (s ,a )−λH(π(·|s )) (cid:1) |s =s ,
i i i i 0
2) State: The state aggregates features informative for
i=0
decision-making. Specifically, it includes: (i) past k down- (11)
load times τi = (τ ,...,τ ), (ii) measured throughput which measures the expected cumulative entropy-regularized
i−k+1 i
pi = (
ni
r
−
i−
k
k
+
+
1
1,...,
ni
ri), (iii) sizes of candidate versions of
reward starting from state s.
τi−k+1 τi Tosolvethisoptimizationproblem,weadoptanactor-critic
the next chunk ni = (ni ,...,ni ), (iv) current buffer
R1 R|R| reinforcement learning architecture, where two parameterized
occupancy b , (v) previous bitrate r , and (vi) number of
i i−1 components are introduced:
remaining chunks m .
i
Thus, the state at chunk i is: • A value function V ϕ π(s), parameterized by ϕ, estimates
the expected return and serves as the critic.
s i =(pi,τi,ni,r i−1 ,b i ,m i ). (6) • A stochastic policy π θ (· | s), parameterized by θ, de-
termines the action-selection strategy and serves as the
3) Reward: The reward function is derived from (3), cap-
actor.
turing per-chunk QoE:
As shown in Fig. 2, we design an NMoE-based actor net-
v (s ,a )=q(r )−α [τ −b ]+−α |q(r )−q(r )|. (7)
i i i i 1 i i 2 i i−1 work architecture in SectionIV.A, which effectively captures
diverse user contexts and network dynamics. Furthermore, a
The ABR agent aims to maximize the expected cumulative
user preference-aware meta-reinforcement learning strategy is
reward:
proposed in SectionIV.B to jointly optimize θ and ϕ, enabling
(cid:34) I (cid:35)
(cid:88) fast policy adaptation under heterogeneous user preferences
max V (s )=E γiv (s ,a )|π,s , (8)
π 0 i i i 0
π and varying network conditions.
i=1
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:41:18 UTC from IEEE Xplore. Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665094
|     | Weight Prediction |     |     |     | Expert-1    | Expert-N |             | Last Chunk Bitrate |     | Embedding |     |     |                |     |     |
| --- | ----------------- | --- | --- | --- | ----------- | -------- | ----------- | ------------------ | --- | --------- | --- | --- | -------------- | --- | --- |
|     |                   |     |     |     | 1DCNN       | 1DCNN    |             |                    |     |           |     |     |                |     |     |
|     |                   |     |     | ×   | 1DCNN 1DCNN |          | 1DCNN 1DCNN | Buffer Occupancy   |     | Embedding |     |     | Dynamic 1D-CNN |     |     |
F F
C C
Dynamic
| State |     |     |     | Weighting |     | ... |     | Remain Chunks |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --------- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
1DCNN
| Preferences |     |     |     |     |     |     |     |     |     |     |     |     |     | FC  |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Dynamic
|     |                |     |     |               |                   |         |     | Next chunk size    |     |          |     |     |     |     | (  1) |
| --- | -------------- | --- | --- | ------------- | ----------------- | ------- | --- | ------------------ | --- | -------- | --- | --- | --- | --- | ----- |
|     |                |     |     | Actor Network |                   |         |     |                    |     | 1DCNN    |     |     |     |     |       |
|     |                |     |     |               |                   |         |     |                    |     |          |     |     |     |     | (  2) |
|     |                |     |     | Dynamic       |                   |         |     | Past Download Time |     | Dynamic  |     |     |     |     |       |
|     | Critic Network |     |     |               | Dynamic  Dynamic  | Bitrate |     |                    |     | 1DCNN    |     |     |     |     | ...   |
Decision
|     |     |     |     |     |     |     |     | Past Throughput |     | Dynamic  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | --- | --- | --- | --- | --- |
1DCNN
|     |     |     |     | Only  |     | Feedback QoE |     |     |     |     | (a) | Actor |     |     |     |
| --- | --- | --- | --- | ----- | --- | ------------ | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
Training
Update State
Last Chunk Bitrate
|     | Fig. | 2:  |          |             |     |     |     |                  |     | Embedding |     | FC  |     |     |     |
| --- | ---- | --- | -------- | ----------- | --- | --- | --- | ---------------- | --- | --------- | --- | --- | --- | --- | --- |
|     |      |     | Overview | of NMoEABR. |     |     |     |                  |     |           |     |     |     |     |     |
|     |      |     |          |             |     |     |     | Buffer Occupancy |     | Embedding |     | FC  |     |     |     |
A. Non-linear Mixture of Experts-based Network Remain Chunks FC
|             |            |                 |            |         |               |          |     |                 |     |       |     |     | FC  | FC  |       |
| ----------- | ---------- | --------------- | ---------- | ------- | ------------- | -------- | --- | --------------- | --- | ----- | --- | --- | --- | --- | ----- |
| To overcome |            | the limitations |            | of      | traditional   | adaptive | bi- |                 |     |       |     |     |     |     |       |
|             |            |                 |            |         |               |          |     | Next chunk size |     | 1DCNN |     |     |     |     |       |
|             |            |                 |            |         |               |          |     |                 |     |       |     |     |     |     | V(  ) |
| trate (ABR) | algorithms |                 | in diverse | network | environments, |          | we  |                 |     |       |     |     |     |     |       |
propose NMoE-ABR, a real-time yet expressive framework Past Download Time 1DCNN
| based on   | a Non-linear  |               | Mixture-of-Experts |               | (NMoE)    |                 | structure |                 |     |       |     |        |     |     |     |
| ---------- | ------------- | ------------- | ------------------ | ------------- | --------- | --------------- | --------- | --------------- | --- | ----- | --- | ------ | --- | --- | --- |
|            |               |               |                    |               |           |                 |           | Past Throughput |     | 1DCNN |     |        |     |     |     |
| in Fig. 2. | Unlike        | conventional  |                    | MoE           | models    | that incur      | high      |                 |     |       |     |        |     |     |     |
| inference  | costs         | with multiple |                    | expert        | networks, | our             | method    |                 |     |       |     |        |     |     |     |
|            |               |               |                    |               |           |                 |           |                 |     |       | (b) | Critic |     |     |     |
| realizes   | expert fusion |               | through            | a non-linear, |           | parameter-level |           |                 |     |       |     |        |     |     |     |
mixing strategy via dynamic convolution. Fig. 3: The Actor and Critic Networks in NMoEABR.
| 1) Limitations |       | of Conventional |           | MoE   | Structures: |           | Mixture- |     |     |     |     |     |     |     |     |
| -------------- | ----- | --------------- | --------- | ----- | ----------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| of-Experts     | (MoE) | is a            | classical | model | ensemble    | mechanism |          |     |     |     |     |     |     |     |     |
widely used to enhance capacity in deep neural networks. It efficient MoE decision modules is critical for high-frequency,
latency-sensitivescenariossuchasvideostreaming.Moreover,
| consists | of M expert | networks |     | {E 1 ,E | 2 ,...,E | M } and | a gating |     |     |     |     |     |     |     |     |
| -------- | ----------- | -------- | --- | ------- | -------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
network G(x) that computes a soft weighting of the expert most MoE models rely on large-scale supervised training,
outputs given an input x. The output of a standard MoE layer whichiscostlyandill-suitedtoABR,whereRLalreadyfaces
|                   |     |     |     |     |     |     |     | slow convergence. |     | This | highlights |     | the need | of efficient | RL- |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---- | ---------- | --- | -------- | ------------ | --- |
| can be formulated |     | as: |     |     |     |     |     |                   |     |      |            |     |          |              |     |
basedtrainingmethodsforABR.Tothebestofourknowledge,
|     |     |     | M   |     |     |     |     | we are | among | the first | to integrate |     | the learning-based |     | ABR |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | --------- | ------------ | --- | ------------------ | --- | --- |
(cid:88)
|     |     | y = | η   | (x)·E | (x), |     | (12) |               |     |             |        |     |         |              |     |
| --- | --- | --- | --- | ----- | ---- | --- | ---- | ------------- | --- | ----------- | ------ | --- | ------- | ------------ | --- |
|     |     |     | m   |       | m    |     |      | policy with   | MoE | techniques. |        |     |         |              |     |
|     |     |     | m=1 |       |      |     |      | 2) Non-linear |     | Expert      | Fusion | via | Dynamic | Convolution: |     |
where η m (x) represents the gating weight for expert m, To address the aforementioned challenges, we propose a non-
computed via a softmax function over the gating logits: linear expert fusion mechanism using dynamic convolution.
|     |     |     |     |       |      |     |     | LetE ={E | ,E  | ,...,E | }andW |     | ,...,W | denoteM | expert |
| --- | --- | --- | --- | ----- | ---- | --- | --- | -------- | --- | ------ | ----- | --- | ------ | ------- | ------ |
|     |     |     |     | exp(G | (x)) |     |     |          | 1   | 2      | M     | 1   | M      |         |        |
m
η m (x)= . (13) networks and their corresponding parameters, respectively,
|     |     |     | (cid:80)M | exp(G | (x)) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j=1 j where each expert is implemented as a lightweight policy
Despite its scalability, the conventional MoE design in- model with an identicalarchitecture but independently trained
parameters.
| curs high | inference | costs, | as  | all experts | need | to  | compute |     |     |     |     |     |     |     |     |
| --------- | --------- | ------ | --- | ----------- | ---- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Insteadofexplicitlyselectingorevaluatingmultipleexperts,
| their forward | passes |     | regardless | of whether |     | they contribute |     |     |     |     |     |     |     |     |     |
| ------------- | ------ | --- | ---------- | ---------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
significantly to the final decision. Sparse MoE variants try to NMoE-ABR constructs a single adaptive policy network by
fusingexpertparametersinalayer-wisemannerusinglearned
activateonlythetop-kexperts,butstillfaceissuesinreal-time
environments. attention weights. These weights are computed once per de-
|             |          |        |           |          |             |             |     | cision step | based      | on the | current | input | state, | thereby | ensuring |
| ----------- | -------- | ------ | --------- | -------- | ----------- | ----------- | --- | ----------- | ---------- | ------ | ------- | ----- | ------ | ------- | -------- |
| MoE         | has been | widely | adopted   | in       | large-scale | models      | for |             |            |        |         |       |        |         |          |
|             |          |        |           |          |             |             |     | efficient   | inference. |        |         |       |        |         |          |
| its ability | to scale | model  | capacity. | However, |             | traditional | MoE |             |            |        |         |       |        |         |          |
implementations suffer from several drawbacks when applied Formally, let f and f represent the input and
|                                                      |     |     |     |     |     |     |     |        |          | input        |     | output |         |     |            |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ------------ | --- | ------ | ------- | --- | ---------- |
|                                                      |     |     |     |     |     |     |     | output | features | of a network |     | layer, | and let | WC  | denote the |
| totime-criticaltaskssuchasABRstreaming:Ontheonehand, |     |     |     |     |     |     |     |        |          |              |     |        |         | m   |            |
in conventional MoE, although only a subset of experts is C-th layer parameters of the m-th expert. The final adaptive
|     |     |     |     |     |     |     |     | network | layer is | computed | as  | follows: |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | -------- | --- | -------- | --- | --- | --- |
activated,thisstillintroducesconsiderableadditionalinference
| overhead | compared | with | learning-based |     | ABR | methods | that |     |     |     |            |     |          |     |     |
| -------- | -------- | ---- | -------------- | --- | --- | ------- | ---- | --- | --- | --- | ---------- | --- | -------- | --- | --- |
|          |          |      |                |     |     |         |      |     |     |     | (cid:32) M |     | (cid:33) |     |     |
employ only a single decision network. Moreover, adaptive (cid:88)
|     |     |     |     |     |     |     |     |     | f      | =σ  |     | η WC | ∗f  | ,     | (14) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | ---- | --- | ----- | ---- |
|     |     |     |     |     |     |     |     |     | output |     |     | m    | m   | input |      |
expertselectionfurtherincreasescomputation.Thus,designing
m=1
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:41:18 UTC from IEEE Xplore.  Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665094
Algorithm 1: Non-linear Expert Fusion via Dynamic This nonlinear, preference-adaptive expert fusion greatly en-
Convolution hances the model’s representational capacity, enabling robust
Require: Input state s, Expert parameters adaptation to diverse network conditions and heterogeneous
{W ,W ,...,W }, Gating subnetwork F user preferences.
1 2 M
Ensure: Output features f 3) Efficiency and Generalization Benefits: Compared to
output
1: Step 1: Compute Dynamic Weights traditional MoE designs, NMoE-ABR offers several key ad-
2: η =F(s,α 1 ,α 2 ,α 3 ) { Adaptive weights from the vantages:
gating subnetwork} • SingleInferencePath:UnlikeconventionalMoEmethods
3: Step 2: Initialize Input Features that evaluate multiple experts in parallel, NMoE-ABR
4: f input =initial input features composes one fused policy network dynamically, reduc-
5: Step 3: Layer-Wise Parameter Fusion ing inference cost significantly.
6: for each layer C in the network do • State-aware Adaptation: The dynamic weighting mecha-
7: W f C used = (cid:80)M m=1 η m W m C {Fuse expert parameters nism ensures that the resulting network adapts to chang-
using η} ing network conditions in real-time, while maintaining
8: f output =σ(W f C used ∗f input ) { Activation + convolution high inference speed.
operation} • Expert Specialization via Shared Structure: All experts
9: f input =f output { Update input features for the next sharethesamearchitecturebutlearndifferentparameter-
layer} izationsduringtraining,effectivelyspecializingfordiffer-
10: end for ent network scenarios and enabling generalization across
11: return f output heterogeneous conditions, even for unseen conditions.
By using non-linear mixing at the parameter level, NMoE-
ABR retains the representational power of multiple experts
whileavoidingtheheavycostassociatedwithtraditionalMoE
where η = F(s,α ,α ,α ) are adaptive weighting coeffi-
1 2 3 inference. This makes it particularly suitable for real-time
cients learned from a lightweight gating subnetwork condi-
ABR tasks in dynamic and resource-limited environments.
tioned on the input state, as shown in the dark blue part
of Fig. 2. Here, Gating subnetwork F(·) s a lightweight B. User Preference-aware Meta-RL Strategy
fully connected network that computes adaptive weighting
Without loss of generality, we adopt the proximal policy
coefficients η based on the input state s, enabling dynamic
optimization (PPO)-based reinforcement learning framework
fusionofexpertparametersinastate-dependentmanner..σ(·)
tojointlyoptimizetheactorandcriticnetworks.Thegoalisto
denotesthenon-linearactivationfunctionand∗representsthe learnapolicyπ parameterizedbyθandavaluefunctionVπθ
θ ϕ
convolution operation. In this way, the parameters of each
parameterizedbyϕthatapproximatestheexpectedcumulative
layer across all experts are adaptively fused to form a uni-
discounted reward.
fied, input-dependent network. The step-by-step computation Let M = {(s ,a ,v )}I denote the collected batch of I
i i i i=1
process of non-linear expert fusion via dynamic convolution
transitions, where s is the state, a is the action, and v is the
i i i
is summarized as Algorithm 1.
immediate reward at step i. The discount factor is denoted by
In conventional mixture-of-experts (MoE) frameworks, the γ ∈[0,1).
weighting factors of each layer are computed by an indepen- 1) Critic Network Optimization: The critic network aims
dent gating network conditioned on the feature maps of the to approximate the expected return under policy π :
θ
precedinglayer,leadingtosubstantialcomputationaloverhead.
In contrast, our method learns a single set of network- and Vπθ(s )≈E (cid:34) (cid:88) ∞ γkv (cid:12) (cid:12)s (cid:35) . (15)
preference-adaptive weights η that are shared across all con- ϕ i i+k(cid:12) i
k=0
volution layers, achieving high efficiency.
To achieve this, ϕ is trained by minimizing the temporal-
To facilitate dynamic convolution implementation in Ten-
difference (TD) error:
sorFlow, the fully connected layers in the critic network are
replaced with 1×1 one-dimensional convolution (1D-CNN) L(ϕ)=E (cid:104)(cid:0) y −Vπθ(s ) (cid:1)2 (cid:105) , (16)
i∈M i ϕ i
layers in actor network of Fig. 3, as a fully connected layer
where the one-step TD target y is defined as:
is mathematically equivalent to a 1×1 1D convolution—both i
perform a weighted linear combination of input channels y =v +γVπθ(s ). (17)
i i ϕ i+1
followed by an optional bias term. Hence, an FC layer can
be regarded as a special case of convolution with kernel size Substituting y i into Eq. (16) yields:
1 and stride 1. L(ϕ)=E (cid:104)(cid:0) v +γVπθ(s )−Vπθ(s ) (cid:1)2 (cid:105) . (18)
Our framework inherits the principle of the MoE model i∈M i ϕ i+1 ϕ i
but extends it into a nonlinear regime owing to the activation This formulation ensures that the critic learns to minimize the
functions in intermediate layers. The resulting actor–critic Bellman residual and accurately estimates the expected long-
architecture of the proposed NMoE-ABR is shown in Fig. 3. term reward.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:41:18 UTC from IEEE Xplore. Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665094
| 2)       | Actor | Network  | Optimization: |     | The actor | network        | param- |                    |     |           |     |     |     |     |
| -------- | ----- | -------- | ------------- | --- | --------- | -------------- | ------ | ------------------ | --- | --------- | --- | --- | --- | --- |
|          |       |          |               |     |           |                |        | Last Chunk Bitrate |     | Embedding |     |     |     |     |
| eterized | by    | θ learns | a policy      | π   | θ (a|s)   | that maximizes | the    |                    |     |           |     |     |     |     |
expected advantage. To stabilize training, we adopt the PPO Buffer Occupancy Embedding
Dynamic 1D-CNN
| objective | with | clipped | probability |     | ratios. | Let: |     |     |     |     |     |     |     |     |
| --------- | ---- | ------- | ----------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Dynamic
Remain Chunks
1DCNN
|     |     |     |        | π θ (a | i |s i ) |     |      |                 |     |          |     |     |     |     |
| --- | --- | --- | ------ | ------ | -------- | --- | ---- | --------------- | --- | -------- | --- | --- | --- | --- |
|     |     |     | ρ (θ)= |        |          | ,   | (19) |                 |     | Dynamic  |     |     |     |     |
|     |     |     | i      | π (a   | |s )     |     |      | Next chunk size |     |          |     |     |     |     |
|     |     |     |        | θold   | i i      |     |      |                 |     | 1DCNN    |     |     |     |     |
FC
|     | π   |     |     |     |     |     |     |     |     | Dynamic  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
where θold is the policy from the previous iteration. The Past Download Time 1DCNN 1)
 (
| clipped | surrogate | objective |     | is formulated |     | as: |     |                 |     |          |     |     |     | (  2) |
| ------- | --------- | --------- | --- | ------------- | --- | --- | --- | --------------- | --- | -------- | --- | --- | --- | ----- |
|         |           |           |     |               |     |     |     | Past Throughput |     | Dynamic  |     |     |     |       |
|         |           |           |     |               |     |     |     |                 |     | 1DCNN    |     |     |     | ...   |
(cid:34)
|        |     |     | (cid:16) | (cid:104)       |        | (cid:0)   |     |     |     |     |     |     |     |     |
| ------ | --- | --- | -------- | --------------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| L(θ)=E |     | max | min      | ρ (θ)A(cid:98)i | , clip | ρ (θ),1−ϵ | ,1+ |     |     |     |     |     |     |     |
|        | i∈M |     |          | i               |        | i         | 1   |     |     |     |     |     |     |     |
(cid:35)
|     |     |     |     |     | (cid:105) | (cid:17) |     | Preference |     | FC  |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
(cid:1)
|     |     |     |     | ϵ 1 A(cid:98)i | ,ϵ 2 A(cid:98)i | +λH(π(·|s | i )) , |     |     |     |     |     |     |     |
| --- | --- | --- | --- | -------------- | --------------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
Fig. 4:
|     |     |     |     |     |     |     |     |     | Actor | Network | with | Preference | Embedding. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ---- | ---------- | ---------- | --- |
(20)
| where      | A(cid:98)i is | the estimated | advantage |       | at step | i, clip(·) | restricts |      |           |     |       |         |            |       |
| ---------- | ------------- | ------------- | --------- | ----- | ------- | ---------- | --------- | ---- | --------- | --- | ----- | ------- | ---------- | ----- |
| the policy | update        | within        | the       | trust | region  | controlled | by ϵ , ϵ  |      |           |     |       |         |            |       |
|            |               |               |           |       |         |            | 1 2       | Task | sampling: | A   | batch | of user | preference | tasks |
•
controls an additional conservative penalty to avoid excessive T ,...,T p(T),
|        |          |         |     |         |     |        |              | 1     | N    | is sampled    | from | the task | distribution |            |
| ------ | -------- | ------- | --- | ------- | --- | ------ | ------------ | ----- | ---- | ------------- | ---- | -------- | ------------ | ---------- |
| policy | updates, | H(π(·|s | ))  | denotes | the | policy | entropy that |       |      |               |      |          |              |            |
|        |          |         | i   |         |     |        |              | where | each | task reflects | a    | specific | user’s QoE   | preference |
λ
encourages exploration, and is a weighting factor for the and environmental dynamics.
entropy term.
|     |           |             |     |            |     |                 |            | • Inner  | loop | (adaptation): |       | For each  | task Ti, | the policy    |
| --- | --------- | ----------- | --- | ---------- | --- | --------------- | ---------- | -------- | ---- | ------------- | ----- | --------- | -------- | ------------- |
| 3)  | Advantage | Estimation: |     | To compute |     | A(cid:98)i , we | employ the |          |      |               |       |           |          |               |
|     |           |             |     |            |     |                 |            | performs | k    | gradient      | steps | to obtain | the      | task-specific |
GeneralizedAdvantageEstimation(GAE)approach,wherethe adapted parameters:
| advantage | is  | defined | as: |     |     |     |     |     |     |     |       |      |       |      |
| --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ----- | ---- |
|           |     |         |     |     |     |     |     |     |     | θ′  | =θ−α∇ | L    | (π ), | (24) |
|           |     |         |     | I−i |     |     |     |     |     | i   |       | θ Ti | θ     |      |
(cid:88)
|     |     |     | A(cid:98)i = | γkδ | ,   |     | (21) |       |       |          |          |         |          |          |
| --- | --- | --- | ------------ | --- | --- | --- | ---- | ----- | ----- | -------- | -------- | ------- | -------- | -------- |
|     |     |     |              |     | i+k |     |      | where | LT is | the loss | function | defined | in (20), | and α is |
i
k=0
|     |     |     |     |     |     |     |     | the inner | learning | rate. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ----- | --- | --- | --- | --- |
with the TD residual δ i given by: • Outer loop (meta-update): The meta-parameters are up-
|               |     |                |          |            |          |            |         | dated  | to minimize |               | the cumulative |          | post-adaptation | losses |
| ------------- | --- | -------------- | -------- | ---------- | -------- | ---------- | ------- | ------ | ----------- | ------------- | -------------- | -------- | --------------- | ------ |
|               |     | δ =v           | +γVπθ(s  |            | )−Vπθ(s  | ).         | (22)    |        |             |               |                |          |                 |        |
|               |     | i              | i ϕ      | i+1        | ϕ        | i          |         |        |             |               |                |          |                 |        |
|               |     |                |          |            |          |            |         | across | all sampled |               | tasks:         |          |                 |        |
| Substituting  |     | δ into         | Eq. (21) | yields:    |          |            |         |        |             |               |                |          |                 |        |
|               |     | i              |          |            |          |            |         |        |             |               |                | (cid:88) |                 |        |
|               |     |                |          |            |          |            |         |        |             | θ ←θ−β∇       |                | θ L      | Ti (π ′ ),      | (25)   |
|               |     | πθ(s           |          | +···+γI−iV |          |            | πθ(s    |        |             |               |                |          | θ i             |        |
| A(cid:98)i    | =−V | )+v            | +γv      |            |          |            | ). (23) |        |             |               |                | i        |                 |        |
|               | ϕ   | i              | i        | i+1        |          | ϕ          | I       |        |             |               |                |          |                 |        |
|               |     |                |          |            |          |            |         | where  | β is the    | meta-learning |                | rate     | for the outer   | loop.  |
| This provides |     | a low-variance |          | yet        | unbiased | estimation | of the  |        |             |               |                |          |                 |        |
relative advantage of action a at state s . This procedure enables the policy to learn common struc-
|     |     |     |     | i   |     | i   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4) Meta-Reinforcement Learning: we adopt Model- tures among heterogeneous tasks and preserve adaptability to
Agnostic Meta-Learning (MAML) [36] to enhance policy unseen user preferences, thus improving convergence stability
generalization across user preference distributions. Each and generalization performance in dynamic network environ-
| combination |     | of preference |     | and distribution |     | is  | modeled as a | ments. |     |     |     |     |     |     |
| ----------- | --- | ------------- | --- | ---------------- | --- | --- | ------------ | ------ | --- | --- | --- | --- | --- | --- |
task T . The meta-policy π learns an initialization θ that can 5) Preference Embedding and Virtual Preference: Despite
|     | i   |     | θ   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rapidly adapt to any T with a few gradient updates. the generalization ability of MAML, direct gradient aggrega-
i
To cope with the training divergence arising from the tion across tasks in (25) may still induce training instability,
complex structure of the Neural Mixture-of-Experts (NMoE), especiallywhenusers’QoEpreferencesarehighlyconflicting.
heterogeneousdownlinkconditions,andconflictingQoEpref- To mitigate this issue, we propose a two-part enhancement:
erences across users, we adopt a Meta-Reinforcement Learn- Preference Embedding and Virtual Preference.
ing (Meta-RL) framework based on Model-Agnostic Meta- AsillustratedinFig.4,wedesignauserpreferenceembed-
Learning(MAML)[36].Thekeyideaistoenablethepolicyto dingmodulethattransformseachuser’sQoEpreferencevector
rapidly adapt to various user preference distributions through into a compact latent representation through a preference
a few gradient updates, rather than retraining from scratch. encoder. This module and its associated feature extractor are
Each unique combination of user preference and network placed only in the inner loop, allowing the model to capture
conditionismodeledasataskT .Themeta-policyπ learnsan fine-grained and task-specific user preference features during
|                                                            |     |     |     | i   |     |     | θ   |                  |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
| initializationparameterθthatgeneralizeswellacrosstheentire |     |     |     |     |     |     |     | task adaptation. |     |     |     |     |     |     |
task space and can be fine-tuned efficiently for any specific Meanwhile,thestatefeatureextractionmoduleintheshared
user or scenario. meta-policyremainspreference-agnosticandfocusesonlearn-
The meta-training process consists of the following steps: ing generalizable semantic and environmental patterns. This
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:41:18 UTC from IEEE Xplore.  Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665094
TABLE I: Summary of Network Bandwidth Datasets
Dataset Network Throughput(Mbps) Description
Norway 3G/HSDPA 1.32±0.59 Contains30minutesofvideostreamingusingtransportation.
Ghent LTE 7.86±10.51 Consistsof40trajectoriesof6typesoftransportation.
FCC18 Broadband 6.31±2.50 Rawdatacollectedfrom7ISPsintheUnitedStates.
Oboe-trace Wi-Fi/3G/LTE 2.77±1.50 Datasetcollectedwhilestreamingvideo.
decoupled design alleviates the gradient interference caused through an additional FC layer to capture complex cross-
by heterogeneous user preferences, thus improving overall feature interactions.
training convergence and stability. In the 1D-CNN, we use 128 filters with a kernel size of 4
To further enhance the smoothness and stability of the and a stride of 1, while the FC layers consist of 128 neurons
meta-optimization process, we introduce a Virtual Preference each. We adopt the ReLU activation function and optimize
Generation mechanism. Specifically, after sampling a batch all parameters using the Adam optimizer. For the embedding
of user preference tasks T ,...,T , we synthesize several layers, the input dimension corresponds to the number of
1 N
virtual preference tasks T˜ ,...,T˜ via linear interpolation of available bitrate levels, and the output dimension is set to 2.
1 M
the existing preference embeddings: For buffer occupancy, we discretize the buffer size into 10
groups, where the input dimension of the embedding layer
N
T˜ = (cid:88) w T , (26) matches the number of groups, and the output dimension is
m m,i i
alsosetto2.Foractiongeneration,theactornetworkproduces
i=1
an action probability distribution using a softmax function,
with
(cid:88) whereas the critic network outputs state-value estimates using
w =1,,w ≥0. (27)
m,i m,i
a linear neuron. During training, we set the discount factor
i
γ =0.99. The state history length is set to k =8.
These virtual tasks effectively fill the gaps between discrete
For the meta-learning, the learning rates for the inner
user preferences, encouraging the meta-policy to learn a con-
loop and outter loop are configured to 0.0001 and 0.001,
tinuous and smooth adaptation surface over the preference
respectively. Following [37], the clipping interval parameter
space. In this case, the meta-update process can be rewritten
(ϵ ,ϵ ) is chosen as (0.2,3). The total number of tasks is set
1 2
as:
16,andthenumberofsampledtracesineachinnerloopagent
θ ←θ−β∇ (cid:0)(cid:88) L (π )+ (cid:88) L (π ) (cid:1) , (28) is 12.
θ Ti θ i ′ T˜ i θ m ′ To enable dynamic weight calculation in a neural mixture-
i m
of-experts (NMoE) manner, we employ the dynamic convolu-
By enriching the task distribution with interpolated pref-
tion technique [38] to parameterize the convolutional kernels
erences, the meta-policy encounters a denser and more di-
forboththeCNNandFClayers,asexpressedinEq.(14).Note
verse set of training tasks, which helps to stabilize gradient
thatFClayerscanbemathematicallyimplementedusing1×1
aggregation in (25) and accelerate convergence. Moreover,
convolutional layers. To ensure efficient inference, the gating
this mechanism reduces overfitting to extreme or sparse user
network F is designed using two lightweight FC layers.
preferences and enhances the policy’s ability to generalize to
unseen preference combinations.
V. EVALUATION
C. Neural Network Implementations In this section, we conduct extensive experiments based
Followingtheconventionaldesignoftheactor-criticframe- on real-world Internet traces and diverse user QoE prefer-
work in reinforcement learning (RL), we adopt the same ence settings to evaluate the performance of the proposed
neural network architecture for both the actor and critic NMoEABR strategy. We compare NMoEABR with several
networks. Specifically, for vectorized sequential inputs, such baseline methods under various network and user preference
as historical download times and bandwidths, we employ conditions to validate its adaptability, generalizability, and
a one-dimensional convolutional neural network (1D-CNN) QoE optimization effectiveness.
to extract temporal dependencies. For discrete integer in-
A. Experiment Setup
puts, including the remaining number of video segments
and the user preference vector, Fully Connected (FC) layers Toensureacomprehensiveevaluation,weadoptthefollow-
are utilized for feature extraction. Moreover, to effectively ing experimental setup.
capture representations of the playback buffer size and the 1) Baseline Algorithms: We select the following represen-
bitrate of the previously downloaded segment, we introduce tativebitrateadaptationstrategiesforcomparisonwithNMoE-
an embedding layer before the FC layers, where the buffer ABR:
size is discretized into multiple states. The features extracted • Buffer-Based (BB) [13]: A throughput-based approach
from all input modalities are then concatenated and passed thatestimatesthedownloadbandwidthbycomputingthe
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:41:18 UTC from IEEE Xplore. Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665094
harmonic mean of the past n video chunk throughputs. TABLE II: User Preference Settings for Training and Testing
The strategy selects the highest available bitrate below
the estimated throughput.
UserPreference α1 α2 α3
• Rate-Based (RB) [12]: A buffer-based scheme that aims QualityPriority 1.5 2.0 0.3
to keep the buffer occupancy above a predefined thresh- Train StabilityPriority 1.0 5.0 0.5
old. If the buffer level is sufficiently high, the algorithm BalancedFluency-Stability 1.0 4.3 1.0
switches to the highest available bitrate. FluencyPriority 1.0 4.3 4.3
Test
• BOLA [3]: A buffer-based algorithm that uses Lyapunov Ultra-Stable 1.0 8.6 1.0
optimization to select bitrates by considering buffer oc-
cupancy only. It seeks to minimize rebuffering while
maximizing average bitrate. across a wide range of network conditions. To further investi-
• RobustMPC [4]: A model predictive control method that gate the adaptability of the proposed approach to user hetero-
combines both estimated bandwidth and buffer dynamics geneity,wedefinefivedistinctgroupsofuserpreferences,each
tomakebitratedecisionsoverafinitepredictionhorizon. represented by a specific QoE weight vector, as summarized
• Pensieve [5]: The first deep reinforcement learning in Table II. Among them, three preference configurations are
(DRL)-based ABR strategy. It employs the A3C algo- used for training:
rithm to directly learn an ABR policy within a simulated • Quality Priority: Users prioritize video quality and are
training environment. willing to tolerate occasional rebuffering or bitrate vari-
• Comyco [21]: An imitation learning-based ABR ap- ations in exchange for clearer visuals.
proachthatacceleratesthetrainingprocessbymimicking • Stability Priority: This setting emphasizes smooth play-
expert behaviors and then refining the policy with rein- back and minimizes rebuffering, even at the expense of
forcement learning. lower visual quality.
2) Video: We evaluated UPM-ABR using the “Envivio- • Balanced Fluency-Stability: A default configuration that
Dash3” video of the DASH-IF reference player (DASH-246) balances quality, fluency, and stability, suitable for the
implementedinJavaScript.Thevideowaspre-processedusing majority of users.
FFmpeg [39] and MP4Box1, and segmented into 48 segments
Toevaluatethegeneralizationabilityofthemodeltounseen
with a duration of 4 seconds each, resulting in a total video
userpreferences,twoadditionaltestingprofilesareintroduced:
lengthof193seconds.Thevideocontentisencodedusingthe
• Fluency Priority: Aims to improve visual quality under
H.264/MPEG-4codecatsixdiscretebitratelevels:{300,750,
the condition of avoiding playback stalls, emphasizing
1200, 1850, 2850, 4300} kbps.
fluent viewing.
3) Datasets: To evaluate the performance of NMoE-ABR
• Ultra-Stable: Represents an extreme preference for un-
in various types of network environments, we adopt four
interrupted playback, assigning a significantly higher
widely used public network bandwidth trace datasets [15],
penalty to rebuffering while being tolerant of quality
[40]–[42], as summarized in Table I. These datasets capture
degradation or bitrate fluctuation.
diverse real-world scenarios. Specifically, the HSDPA dataset
All the computations are executed on a machine with an
includes traces collected while traveling on different modes
Intel(R)Xeon(R)Silver4214CPU@2.20GHz,twoNVIDIA
of transportation, such as buses, ferries, trams, trains, and
RTX3090GPUs,and128GBRAM.TheDRLalgorithmsare
cars. The Ghent data set covers six types of mobility: walk-
constructed using Tensorflow 2.3.0, tflearn 0.5.0, and Python
ing, cycling, bus, tram, train, and car. Among the datasets,
3.8 for computational speed boost. All experimental results
the Ghent trace exhibits substantial fluctuations. Such high
are the average results over five models trained with different
volatility in network conditions can result in playback stalls
randomseeds.Weevaluatetheproposedmethodtoanswerthe
duringperiodsofreducedthroughput.Toensurecompatibility
following questions:
withthestreamingrequirementsoftheencodedvideo,theraw
bandwidth traces were scaled by a fixed factor. This rescaling • Does the unified NMoEABR policy enhance adaptation
ensures that the available bandwidth remains aligned with the capability and thereby improve the average QoE under
bitrate levels used in the experiments, facilitating a stable diverse network conditions and user preferences? (Sec-
and realistic evaluation environment. For model training and tion V.B)
evaluation, the Norway, FCC18 and Ghent datasets are split • Does the unified NMoEABR policy enhance generaliza-
intotrainingandtestingsetswithan8:2ratio.TheOboedata tion capability and thereby improve the average QoE
setisexclusivelyusedfortestingtoassessthegeneralizability under unseen network conditions and user preferences?
of the model in unseen network scenarios. (Section V.C)
4) QoEMetrics: Inthecontextofheterogeneousnetworks, • Does the proposed NMoEABR framework introduce
we evaluate ABR strategies using fixed QoE weights (e.g., negligible additional computation overhead, showing its
[1,4.3,1])to testperformance.Thisenables afaircomparison feasibility for practical deployment? (Section V.D)
• Does the unified NMoEABR policy improve the average
1https://wiki.gpac.io/MP4Box/MP4Box/ andquantileQoEunderreal-worldplatformdeployment?
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:41:18 UTC from IEEE Xplore. Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665094
|                  | (a) HSDPA   | Trace   |             |              |         |          | (b) Ghent     | Trace       |           |           |           | (c)       | FCC18 Trace        |
| ---------------- | ----------- | ------- | ----------- | ------------ | ------- | -------- | ------------- | ----------- | --------- | --------- | --------- | --------- | ------------------ |
|                  |             |         |             | Fig.         | 5: CDFs | of QoE   | Performance   | under       | Different | Networks. |           |           |                    |
|                  | (a) HSDPA   | Trace   |             |              |         |          | (b) Ghent     | Trace       |           |           |           | (c)       | FCC18 Trace        |
|                  |             | Fig.    | 6: The      | relationship |         | between  | video bitrate | and penalty | risk      | under     | different | networks. |                    |
|                  |             |         |             |              |         |          |               | TABLE       |           | III: QoE  | versus    | Various   | Network Conditions |
| (Section         | V.E)        |         |             |              |         |          |               |             |           |           |           |           |                    |
|                  |             |         |             |              |         |          |               | Method      |           |           | HSDPA     | Ghent     | FCC18 Average      |
| B. Adaptation    | Comparisons |         |             |              |         |          |               |             |           |           |           |           |                    |
|                  |             |         |             |              |         |          |               | NMoEABR     |           |           | 0.976     | 4.032     | 3.067 2.692        |
|                  |             |         |             |              |         |          |               | Pensieve    |           |           | 0.871     | 3.973     | 2.927 2.590        |
| 1) Heterogeneous |             | Network | Conditions: |              | To      | evaluate | the ef-       |             |           |           |           |           |                    |
fectiveness of NMoE-ABR under different network scenarios, Comyco 0.966 4.009 2.972 2.649
|                 |        |             |         |      |               |         |          | RobustMPC  |     |     | 0.863 | 3.924 | 2.931 2.573 |
| --------------- | ------ | ----------- | ------- | ---- | ------------- | ------- | -------- | ---------- | --- | --- | ----- | ----- | ----------- |
| we compared     | its    | performance |         | with | various       | bitrate | adapta-  |            |     |     |       |       |             |
|                 |        |             |         |      |               |         |          | Rate-Based |     |     | 0.409 | 3.973 | 2.687 2.356 |
| tion strategies | across | diverse     | network |      | environments. |         | Figure 5 |            |     |     |       |       |             |
presents the cumulative distribution functions (CDFs) of dif- Buffer-Based 0.673 3.522 2.476 2.224
|                   |     |                |     |         |         |       |          | BOLA           |     |     | 0.817 | 3.538 | 2.517 2.291 |
| ----------------- | --- | -------------- | --- | ------- | ------- | ----- | -------- | -------------- | --- | --- | ----- | ----- | ----------- |
| ferent strategies |     | under multiple |     | network | traces, | while | the cor- |                |     |     |       |       |             |
|                   |     |                |     |         |         |       |          | Pensieve-HSDPA |     |     | 0.954 | -     | - 2.577     |
respondingQoEmetricsandtheiraveragesaresummarizedin
|                |               |                 |          |             |                 |               |            | Pensieve-Ghent |     |     | -   | 3.864 | - 1.799     |
| -------------- | ------------- | --------------- | -------- | ----------- | --------------- | ------------- | ---------- | -------------- | --- | --- | --- | ----- | ----------- |
| Table III.     | Specifically, | Pensieve-HSDPA, |          |             | Pensieve-Ghent, |               | and        |                |     |     |     |       |             |
|                |               |                 |          |             |                 |               |            | Pensieve-FCC18 |     |     | -   | -     | 2.991 2.589 |
| Pensieve-FCC18 |               | represent       | Pensieve | models      |                 | trained       | individu-  |                |     |     |     |       |             |
| ally on        | the HSDPA,    | Ghent,          | and      | FCC18       | traces,         | respectively. |            |                |     |     |     |       |             |
| In contrast,   | Pensieve,     | Comyco,         |          | and NMoEABR |                 | are           | trained on |                |     |     |     |       |             |
mixed network environments to evaluate their generalization Incontrast,model-basedmethodsrelyonfixedcontrolrules,
capability. A detailed discussion of the experimental results is which limit flexibility in dynamic environments. For example,
provided below. RobustMPC achieves acceptable performance under relatively
As shown in Table III, the proposed NMoE-ABR con- stable networks like Ghent and FCC18 but suffers significant
sistently outperforms baseline strategies across all network degradation in poor networks such as HSDPA. Similarly,
conditions, achieving QoE improvements ranging from 1.0% learning-basedapproachestrainedonasingleenvironmentfail
to 138.0% on HSDPA, 0.6% to 14.5% on Ghent, and 3.1% to generalize; for instance, Pensieve-Ghent performs poorly
to 23.8% on FCC18, demonstrating its strong adaptability to under HSDPA. This is primarily due to severe video stalls
diversenetworkscenarios.Leveraginganonlinearmixture-of- during playback, which severely degrades the user QoE.
experts mechanism based on adaptive dynamic convolution, Moreover,directlytrainingexistingmethodsonmixeddatasets
NMoE-ABR learns environment-aware ABR strategies in het- tends to lead to policy averaging, resulting in compromised
erogeneous networks. performance in individual environments, as observed in the
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:41:18 UTC from IEEE Xplore.  Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665094
TABLE IV: QoE versus Various User Preferences TABLE V: Performance Comparison over Unseen Preferences
Network Method Quality Stability Fluency- Average Method FluencyPriority Ultra-Stable Average
|     |          |     | Priority | Priority |     | Stability |       |          |     |     |       |     |       |       |     |
| --- | -------- | --- | -------- | -------- | --- | --------- | ----- | -------- | --- | --- | ----- | --- | ----- | ----- | --- |
|     |          |     |          |          |     |           |       | NMoEABR  |     |     | 0.680 |     | 0.901 | 0.790 |     |
|     | NMoEABR  |     | 1.642    | 1.025    |     | 0.982     | 1.216 |          |     |     |       |     |       |       |     |
|     | Comyco   |     | 1.569    | 0.975    |     | 0.943     | 1.162 | Comyco   |     |     | 0.675 |     | 0.888 | 0.781 |     |
|     | Pensieve |     | 1.030    | 0.987    |     | 0.928     | 0.982 | Pensieve |     |     | 0.511 |     | 0.898 | 0.704 |     |
HSDPA RobustMPC 1.627 0.903 0.863 1.131 RobustMPC 0.392 0.684 0.538
|     | RB       |     | 1.496 | 0.574 |     | 0.409 | 0.826 |      |     |     |        |     |       |        |     |
| --- | -------- | --- | ----- | ----- | --- | ----- | ----- | ---- | --- | --- | ------ | --- | ----- | ------ | --- |
|     | BB       |     | 1.453 | 0.857 |     | 0.674 | 0.995 | RB   |     |     | -1.048 |     | 0.068 | -0.490 |     |
|     | BOLA     |     | 1.527 | 0.934 |     | 0.817 | 1.093 | BB   |     |     | -0.539 |     | 0.673 | 0.067  |     |
|     |          |     |       |       |     |       |       | BOLA |     |     | 0.032  |     | 0.804 | 0.418  |     |
|     | NMoEABR  |     | 6.283 | 4.098 |     | 4.044 | 4.808 |      |     |     |        |     |       |        |     |
|     | Comyco   |     | 5.694 | 4.049 |     | 4.008 | 4.583 |      |     |     |        |     |       |        |     |
|     | Pensieve |     | 6.228 | 3.983 |     | 3.949 | 4.720 |      |     |     |        |     |       |        |     |
Ghent RobustMPC 6.039 3.979 3.925 4.648 parameters for every network environment and preference
RB 6.182 4.060 3.973 4.738 setting.Incontrast,theproposedNMoEABRwastrainedonce
|     | BB  |     | 5.469 | 3.599 |     | 3.522 | 4.197 |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | ----- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
BOLA 5.485 3.612 3.539 4.212 pernetworkenvironmentusingmixedpreferencedataandthen
|     |     |     |     |     |     |     |     | evaluated | separately | under | each | user preference. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ----- | ---- | ---------------- | --- | --- | --- |
NMoEABR 4.752 3.071 3.031 3.618 We observe that NMoEABR consistently outperforms all
|     | Comyco |     | 4.586 | 2.925 |     | 2.908 | 3.473 |     |     |     |     |     |     |     |     |
| --- | ------ | --- | ----- | ----- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Pensieve 4.661 2.964 2.933 3.519 baseline methods across all datasets and preference configu-
FCC18 RobustMPC 4.667 2.980 2.931 3.526 rations. Specifically, it achieves average QoE improvements
|     | RB  |     | 4.648 | 2.808 |     | 2.687 | 3.381 |               |     |           |     |            |     |           |     |
| --- | --- | --- | ----- | ----- | --- | ----- | ----- | ------------- | --- | --------- | --- | ---------- | --- | --------- | --- |
|     |     |     |       |       |     |       |       | of 4.2%–47.2% |     | on HSDPA, |     | 1.5%–14.6% |     | on Ghent, | and |
|     | BB  |     | 4.114 | 2.608 |     | 2.476 | 3.066 |               |     |           |     |            |     |           |     |
BOLA 4.150 2.625 2.517 3.097 2.6%–18.0% on FCC18. These results clearly demonstrate
|          |          |           |             |        |              |           |          | that NMoEABR      |            | significantly | enhances   |          | user experience |                  | across |
| -------- | -------- | --------- | ----------- | ------ | ------------ | --------- | -------- | ----------------- | ---------- | ------------- | ---------- | -------- | --------------- | ---------------- | ------ |
|          |          |           |             |        |              |           |          | diverse           | preference | scenarios,    |            | further  | confirming      | the              | strong |
|          |          |           |             |        |              |           |          | adaptability      | of         | the proposed  | framework. |          |                 |                  |        |
| Pensieve | and      | Comyco    | benchmarks. |        | By contrast, | NMoE-ABR, |          |                   |            |               |            |          |                 |                  |        |
| trained  | on mixed | datasets, | achieves    |        | 12.1%,       | 1.5%,     | and 4.8% |                   |            |               |            |          |                 |                  |        |
|          |          |           |             |        |              |           |          | C. Generalization |            | Comparison    |            |          |                 |                  |        |
| higher   | QoE than | Pensieve  | on          | HSDPA, | Ghent,       | and       | FCC18,   |                   |            |               |            |          |                 |                  |        |
|          |          |           |             |        |              |           |          | 1) Generalization |            | to            | Unseen     | Network: | In              | this experiment, |        |
respectively.
alllearning-basedmethodsaretrainedonthemixeddatasetof
| Video | bitrate | utility | conflicts | with | rebuffering |     | and bitrate |     |     |     |     |     |     |     |     |
| ----- | ------- | ------- | --------- | ---- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Gheat,HSDPA,andFCC18,andtestedontheOboedatasetto
variationpenalties,andthegoalofbitrateadaptationstrategies
evaluatetheirgeneralizationperformance.AsshowninFig.7,
| is to balance |     | these three | factors | to  | maximize | overall | QoE. |     |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | ------- | --- | -------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
NMoE-ABRsignificantlyoutperformsbothlearning-basedand
| This section | examines |     | the relationship |     | between | video | bitrate |     |     |     |     |     |     |     |     |
| ------------ | -------- | --- | ---------------- | --- | ------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
model-basedbaselinesontheunseendataset,achievinganav-
| and the | combined | penalty |     | risk of | rebuffering | and | bitrate |     |     |     |     |     |     |     |     |
| ------- | -------- | ------- | --- | ------- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
erage13.2%improvementinQoEoverallcomparedmethods.
| variation   | under      | different    | network     | environments. |          | Experimental |              |               |              |         |             |                    |       |            |       |
| ----------- | ---------- | ------------ | ----------- | ------------- | -------- | ------------ | ------------ | ------------- | ------------ | ------- | ----------- | ------------------ | ----- | ---------- | ----- |
|             |            |              |             |               |          |              |              | Specifically, | we           | observe | that        | the learning-based |       | benchmarks |       |
| results     | indicate   | that         | model-based |               | methods  | (e.g.,       | BOLA and     |               |              |         |             |                    |       |            |       |
|             |            |              |             |               |          |              |              | Pensieve      | and Comyco,  |         | trained     | on the             | mixed | dataset,   | tend  |
| RobustMPC), |            | which        | rely on     | fixed         | decision | rules,       | exhibit rel- |               |              |         |             |                    |       |            |       |
|             |            |              |             |               |          |              |              | to adopt      | conservative |         | strategies, | leading            | to    | relatively | lower |
| atively     | consistent | distribution |             | trends        | across   | different    | network      |               |              |         |             |                    |       |            |       |
averagebitrates.Incontrast,ourproposedmethodachievesthe
environments.Learning-basedstrategiesachieveacompromise
highestaveragebitratewhilesimultaneouslyattainingthelow-
amongvideobitrate,rebufferingduration,andbitratevariation.
|        |         |      |      |        |              |        |     | est rebuffering |          | time, which | is       | 39.83%      | lower | than the      | second- |
| ------ | ------- | ---- | ---- | ------ | ------------ | ------ | --- | --------------- | -------- | ----------- | -------- | ----------- | ----- | ------------- | ------- |
|        |         |      |      |        |              |        |     | best method,    | Comyco,  |             | and also | achieves    | the   | second-lowest |         |
| We can | observe | from | Fig. | 6 that | the proposed | method | not |                 |          |             |          |             |       |               |         |
|        |         |      |      |        |              |        |     | variance        | penalty. | This        | superior | performance |       | is attributed | to      |
onlyachievesthehighestoverallQoEacrossdifferentnetwork
|              |     |          |            |         |              |     |         | MoE’s | ability to | adapt | rapidly | to unseen | network |     | conditions |
| ------------ | --- | -------- | ---------- | ------- | ------------ | --- | ------- | ----- | ---------- | ----- | ------- | --------- | ------- | --- | ---------- |
| environments |     | but also | adaptively | adjusts | optimization |     | strate- |       |            |       |         |           |         |     |            |
bynonlinearlycombininglearnedexpertsbasedonthecurrent
| gies among       | QoE     | metrics         | according     |        | to specific  | environmental |            |                   |             |     |           |        |              |          |            |
| ---------------- | ------- | --------------- | ------------- | ------ | ------------ | ------------- | ---------- | ----------------- | ----------- | --- | --------- | ------ | ------------ | -------- | ---------- |
|                  |         |                 |               |        |              |               |            | network           | state.      |     |           |        |              |          |            |
| characteristics. |         | This capability |               | allows | NMoEABR      | to            | approach   |                   |             |     |           |        |              |          |            |
|                  |         |                 |               |        |              |               |            | 2) Generalization |             | to  | Unseen    | User   | Preferences: |          | Similarly, |
| an ideal         | balance | and             | better aligns | with   | the research |               | objectives |                   |             |     |           |        |              |          |            |
|                  |         |                 |               |        |              |               |            | in this           | experiment, | we  | train the | models | under        | “Quality | Pri-       |
of this work. Compared with Pensieve, the proposed method ority”, “Stability Priority”, and “Balanced Fluency-Stability”
| achieves | QoE | improvements |     | of 1.3%, | 3.7%, | and | 0.3% | in           |     |          |      |            |          |     |            |
| -------- | --- | ------------ | --- | -------- | ----- | --- | ---- | ------------ | --- | -------- | ---- | ---------- | -------- | --- | ---------- |
|          |     |              |     |          |       |     |      | preferences, | and | evaluate | them | on Fluency | Priority |     | and Ultra- |
differentnetworkenvironments,withthelargestgainobserved
|                  |          |     |                   |     |        |     |             | Stable Mode | user         | preferences. |       | The       | results     | on the | HSDPA    |
| ---------------- | -------- | --- | ----------------- | --- | ------ | --- | ----------- | ----------- | ------------ | ------------ | ----- | --------- | ----------- | ------ | -------- |
| in the Ghent     | network. |     |                   |     |        |     |             |             |              |              |       |           |             |        |          |
|                  |          |     |                   |     |        |     |             | dataset     | are reported | in           | Table | V. It can | be observed |        | that the |
| 2) Heterogeneous |          |     | User Preferences: |     | Tables | IV  | present the |             |              |              |       |           |             |        |          |
|                  |          |     |                   |     |        |     |             | proposed    | method       | consistently |       | achieves  | the best    | QoE    | perfor-  |
QoE performance on the HSDPA, Ghent, and FCC18 datasets mance under various unseen preference conditions within this
| under different |        | user | preference         | modes. | It         | is worth        | noting   |               |              |                  |     |            |     |     |     |
| --------------- | ------ | ---- | ------------------ | ------ | ---------- | --------------- | -------- | ------------- | ------------ | ---------------- | --- | ---------- | --- | --- | --- |
|                 |        |      |                    |        |            |                 |          | network       | environment. |                  |     |            |     |     |     |
| that, unlike    | Table  | III, | the learning-based |        | benchmarks |                 | Pensieve |               |              |                  |     |            |     |     |     |
|                 |        |      |                    |        |            |                 |          | D. Comparison |              | of Computational |     | Complexity |     |     |     |
| and Comyco      | failed | to   | converge           | when   | trained    | in environments |          |               |              |                  |     |            |     |     |     |
with mixed user preferences. Therefore, in Tables IV, each The primary motivation behind NMoEABR is to enhance
learning-basedbenchmarkwasretrainedwithdedicatedmodel the adaptability of adaptive bitrate (ABR) strategies in hetero-
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:41:18 UTC from IEEE Xplore.  Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665094
Performance Comparison on the Unseen Oboe Network
QoE Bitrate (Mbps) Rebuffering Time Bitrate Variation
2.0 2.248 2.146 2.153 2.232 1.889 1.754 1.841 2 2 . . 0 5 2.456 2.260 2.323 2.457 2.507 2.212 2.228 0 0 . . 3 3 0 5 0.275 0.337 0 0 . . 4 5 0.487 0.454 0.379
0.25 0.241
1.5 0.218 0.212 0.217
1.5 0.20 0.3
1.0 0.15 0.145
1.0 0.2
0.160 0.157
0.10 0.122
0.5 0.5 0.1 0.088
0.05
0.0 0.0 0.00 0.0
Ours Comyco Pensie
R
v
o
e bustMPC RB BB BOLA Ours Comyco Pensie
R
v
o
e bustMPC RB BB BOLA Ours Comyco Pensie
R
v
o
e bustMPC RB BB BOLA Ours Comyco Pensie
R
v
o
e bustMPC RB BB BOLA
Fig. 7: Performance Comparison on Unseen Oboe Network
TABLE VI: Comparison of Inference Time low to high bitrate, to support adaptive bitrate selection under
varyingnetworkconditions.Testswereconductedonmultiple
Method BB RB BOLA RobustMPC Comyco Pensieve Ours
client devices, including an Android smartphone (Xiaomi 14,
Latency(µs) 0.8 2.0 12.0 28126.1 575.3 612.4 722.6
Chrome),aniPad9(Safari),anddesktopandlaptopcomputers
using Chrome and Edge browsers.
geneous network environments through an MoE framework. Each network–client combination repeatedly streamed the
However, conventional MoE architectures typically require same video using a randomly selected ABR algorithm, and
the computation of multiple experts at each layer, which is the reported results represent the average performance over
unsuitable for real-time video streaming scenarios due to the ten-hour sessions. The neural network weights of Comyco
associated computational overhead. To address this limitation, and Pensieve were pre-trained on the HSDPA/FCC16 dataset
we propose a nonlinear combination of multiple pre-trained with “Balanced Fluency–Stability” QoE preferences, consis-
expert models using dynamic convolution techniques. This tent with Table III. The weights of NMoEABR remained
enables the deployment of a single adaptive policy model, the same as those used in Table III. Fig. 94 present QoE
significantly reducing computational cost while maintaining comparisons under WiFi and cellular networks, respectively.
high performance under varying network conditions. NMoE-ABR consistently achieves the highest average QoE,
As shown in Table VI, we evaluate the decision la- demonstrating superior robustness and adaptability.
tency of different ABR strategies, with all experiments con- IntheWiFiscenario,theaccesspointwaslocatedinanadja-
ducted on an Intel(R) Xeon(R) Silver 4214 processor. Model- centroom,andsignalattenuationthroughthewallsignificantly
based strategies demonstrate superior inference speed, yet limiteddownlinkthroughput.AsshowninFig.9a,theaverage
RobustMPC incurs higher computational complexity due to QoE scores of NMoEABR, Comyco, and Pensieve are 0.88,
its dynamic programming-based search procedure. Notably, –1.01,and0.68,respectively.Allmethodsexperiencerebuffer-
NMoEABR, similar to other learning-based methods, achieves ingduetobandwidthconstraints.Comyco’simitationlearning
sub-millisecond decision latency, indicating its feasibility for policy selects aggressive bitrates, causing severe rebuffering
real-time deployment in practical video streaming systems. andnegativeQoE,whilePensieveadoptsconservativebitrates,
resulting in lower visual quality. NMoEABR achieves compa-
E. Real-World Platform Evaluation rable visual quality to Comyco while substantially reducing
We further evaluated NMoEABR, Comyco, and Pensieve rebuffering penalties, yielding a 29.41% QoE improvement
on a real-world platform under two wireless access network over Pensieve.
environments: a WiFi network on the Shenzhen University In the cellular scenario, high user mobility caused frequent
campus and a cellular network in Shenzhen, as shown in base station handovers and throughput fluctuations. As shown
Fig. 8b and 8c, respectively. The platform was implemented in Fig. 9c, NMoEABR, Comyco, and Pensieve achieve average
based on Dash.js2 using the open-source Pitree framework3, QoEs of 3.00, 2.55, and 2.89, respectively. Both Comyco and
as shown in Fig. 8a. A remote cloud server rented from Pensieve exhibit high inter-session variability under unstable
Tencent Cloud serves as the core server, equipped with the networkconditions(Fig.9d).Incontrast,NMoEABRmaintains
Ubuntu Server 22.04 LTS 64-bit operating system. It features
4The plots in (b) and (d) are box plots that summarize the distribution
high bandwidth and large-capacity storage to host all video of the data. In these plots, the middle line within each box represents the
resources. The server stores all bitrate versions of videos median (i.e., the 50th percentile) of the data. The top and bottom edges
of the box correspond to the upper quartile (Q3) and lower quartile (Q1),
encodedwithH.264,coveringacompletesetofsegmentsfrom
respectively, meaning the box contains the interquartile range (IQR), which
representsthemiddle50%ofthedata.The”whiskers”(linesextendingfrom
2Dash Industry Forum. Catalyzing the Adoption of MPEG-DASH. thebox)representtheminimumandmaximumvaluesinthedata,excluding
https://dashif.org/ outliers.Therefore,theheightoftheboxreflectsthevariabilityorspreadof
3https://github.com/transys-project/pitree thedata,whilethewhiskersprovideadditionalcontextabouttherange.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:41:18 UTC from IEEE Xplore. Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665094
Transmitt
er
Receiver Receiver
1 2
(a) Online Testing Platform OSCAP (b)WiFi Test Environment (c) Cellular Test Subway Route
Fig. 8: Video Streaming Website, WiFi Deployment Details, and Cellular Network Map.
(a) Average QoE @WiFi (b) Quantile QoE @WiFi (c) Average QoE @Cellular (d) Quantile QoE @Cellular
Fig. 9: Comparison in Real-World Platform.
stable performance and generalizes well across dynamic real- [2] Y. Sun, X. Yin, J. Jiang, V. Sekar, F. Lin, N. Wang, T. Liu, and
world environments, highlighting its advantage over existing B. Sinopoli, “Cs2p: Improving video bitrate selection and adaptation
with data-driven throughput prediction,” in Proceedings of the 2016
ABR schemes.
ACMSIGCOMMConference,2016,p.272–285.
[3] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “Bola: Near-optimal
VI. CONCLUSIONS bitrate adaptation for online videos,” IEEE/ACM transactions on net-
working,vol.28,no.4,pp.1698–1711,2020.
In this work, we tackle the challenge of adaptive bitrate [4] X. Yin et al., “A control-theoretic approach for dynamic adaptive
video streaming over http,” in Proceedings of the ACM conference on
(ABR) selection under heterogeneous networks and diverse
SIGCOMM,2015.
user preferences. We propose NMoEABR, a unified ABR [5] H.Mao,R.Netravali,andM.Alizadeh,“Neuraladaptivevideostream-
framework that integrates a nonlinear Mixture-of-Experts ing with pensieve,” in Proceedings of the Conference of ACM SIG-
COMM,2017,pp.197–210.
(NMoE)–based actor network with a user preference–aware
[6] A.Yaqoob,T.Bi,andG.-M.Muntean,“Asurveyonadaptive360video
meta-reinforcement learning strategy. The NMoE actor dy-
streaming:Solutions,challengesandopportunities,”IEEECommunica-
namically combines expert policies through dynamic convo- tionsSurveys&Tutorials,vol.22,no.4,pp.2801–2838,2020.
lution conditioned on real-time network states, enhancing ro- [7] A.Balachandran,V.Sekar,A.Akella,S.Seshan,I.Stoica,andH.Zhang,
“Developing a predictive model of quality of experience for internet
bustnessandcross-networkgeneralizationincomplexenviron-
video,” ACM SIGCOMM Computer Communication Review, vol. 43,
ments. Meanwhile, the preference-aware meta-RL component no.4,pp.339–350,2013.
incorporates user preference embeddings and synthesizing, [8] W.Li,X.Li,Y.Xu,Y.Yang,andS.Lu,“MetaABR:Ameta-learning
approach on adaptative bitrate selection for video streaming,” IEEE
enablingfastconvergence.Extensiveevaluationsonreal-world
Trans.Mob.Comput.,vol.23,no.3,pp.2422–2437,2024.
traces and wireless testbed demonstrate that NMoEABR con- [9] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,andL.Sun,“Learningtailored
sistently outperforms mainstream ABR methods, particularly adaptive bitrate algorithms to heterogeneous network conditions: A
domain-specificpriorsandmeta-reinforcementlearningapproach,”IEEE
in unseen networks and user preference.
JSelAreasCommun,vol.40,no.8,pp.2485–2503,2022.
[10] Y.Li,H.Zhang,Y.Zhang,X.Ma,W.Ye,N.Song,S.Wang,H.Xiong,
REFERENCES D. Yin, and L. Chen, “M2oerank: Multi-objective mixture-of-experts
enhanced ranking for satisfaction-oriented web search,” in 2025 IEEE
[1] M.Seufert,S.Egger,M.Slanina,T.Zinner,T.Hoßfeld,andP.Tran-Gia, 41stInternationalConferenceonDataEngineering(ICDE),2025,pp.
“A survey on quality of experience of http adaptive streaming,” IEEE 4441–4454.
CommunicationsSurveys&Tutorials,vol.17,no.1,pp.469–492,2014. [11] Z. Lyu, M. Xiao, J. Xu, M. Skoglund, and M. D. Renzo, “The
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:41:18 UTC from IEEE Xplore. Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665094
larger the merrier? efficient large ai model inference in wireless edge [32] N. Shazeer, A. Mirhoseini, K. Maziarz, A. Davis, Q. Le, G. Hinton,
networks,”2025.[Online].Available:https://arxiv.org/abs/2505.09214 and J. Dean, “Outrageously large neural networks: The sparsely-gated
[12] B. Rainer, S. Lederer, C. Mu¨ller, and C. Timmerer, “A seamless web mixture-of-expertslayer,”arXivpreprintarXiv:1701.06538,2017.
integration of adaptive http streaming,” in Proceedings of the 20th [33] W. Fedus, B. Zoph, and N. Shazeer, “Switch transformers: Scaling to
EuropeanSignalProcessingConference,2012,pp.1519–1523. trillionparametermodelswithsimpleandefficientsparsity,”Journalof
[13] T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Watson, MachineLearningResearch,vol.23,no.120,pp.1–39,2022.
“A buffer-based approach to rate adaptation: Evidence from a large [34] I. Misra, A. Shrivastava, A. Gupta, and M. Hebert, “Cross-stitch net-
video streaming service,” in Proceedings of the ACM conference on works for multi-task learning,” in Proceedings of the IEEE conference
SIGCOMM,2014,pp.187–198. oncomputervisionandpatternrecognition,2016,pp.3994–4003.
[35] A. Mirhoseini, H. Pham, Q. V. Le, B. Steiner, R. Larsen, Y. Zhou,
[14] J.Liu,Z.Liu,J.Huang,W.Jiang,andJ.Wang,“Abuffer-basedadaptive
bitrate approach in wireless networks with iterative correction,” IEEE N. Kumar, M. Norouzi, S. Bengio, and J. Dean, “Device placement
WirelessCommunicationsLetters,vol.11,no.8,pp.1644–1648,2022. optimization with reinforcement learning,” in International conference
onmachinelearning,2017,pp.2430–2439.
[15] Z. Akhtar, Y. S. Nam, R. Govindan, S. Rao, J. Chen, E. Katz-Bassett,
[36] C. Finn, P. Abbeel, and S. Levine, “Model-agnostic meta-learning
B. Ribeiro, J. Zhan, and H. Zhang, “Oboe: Auto-tuning video ABR
for fast adaptation of deep networks,” in International conference on
algorithmstonetworkconditions,”inProceedingsoftheConferenceof
machinelearning,2017,pp.1126–1135.
ACMSIGCOMM,2018,pp.44–58.
[37] D. Y. et al., “Mastering complex control in moba games with deep
[16] F. Y. Yan, H. Ayers, C. Zhu, S. Fouladi, J. Hong, K. Zhang, P. Levis,
reinforcementlearning,”inProceedingsofAAAI,2020.
and K. Winstein,“Learning in situ: a randomizedexperiment in video
[38] Y. Chen, X. Dai, M. Liu, D. Chen, L. Yuan, and Z. Liu, “Dynamic
streaming,” in Proc. USENIX Symp. Networked Syst. Des. Implement.
convolution: Attention over convolution kernels,” in Proceedings of
(NSDI),2020.
CVPR),2020,pp.11027–11036.
[17] N. Kan, C. Li, C. Yang, W. Dai, J. Zou, and H. Xiong, “Uncertainty- [39] S.Tomar,“Convertingvideoformatswithffmpeg,”Linuxjournal,vol.
awarerobustadaptivevideostreamingwithbayesianneuralnetworkand 2006,no.146,p.10,2006.
model predictive control,” in Proceedings of the 31st ACM workshop [40] H. Riiser, P. Vigmostad, C. Griwodz, and P. Halvorsen, “Commute
onnetworkandoperatingsystemssupportfordigitalaudioandvideo, path bandwidth traces from 3g networks: Analysis and applications,”
2021,pp.17–24. inProceedingsofthe4thACMMultimediaSystemsConference,2013,
[18] W. Feng, S. Wang, and Y. Dai, “Adaptive 360-degree streaming: Op- pp.114–118.
timizing with multi-window and stochastic viewport prediction,” IEEE [41] Federal Communications Commission (FCC). (2018) Raw data -
Trans.Mob.Comput.,vol.24,no.7,pp.5903–5915,2025. MeasuringBroadbandAmerica.FederalCommunicationsCommission.
[19] H. Wang, Z. Long, H. Dong, and A. El Saddik, “Madrl-based rate [Online].Available:https://www.fcc.gov/reports-research/reports/
adaptation for 360° video streaming with multiviewpoint prediction,” [42] J.VanDerHooft,S.Petrangeli,T.Wauters,R.Huysegems,P.R.Alface,
IEEEInternetThingsJ.,vol.11,no.15,pp.26503–26517,2024. T.Bostoen,andF.DeTurck,“Http/2-basedadaptivestreamingofhevc
[20] J.Zeng,X.Zhou,andK.Li,“Madrl-basedjointedgecachingandbitrate video over 4g/lte networks,” IEEE Communications Letters, vol. 20,
selectionformulticategory360°videostreaming,”IEEEInternetThings no.11,pp.2177–2180,2016.
J.,vol.11,no.1,pp.584–596,2024.
[21] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,X.Yao,andL.Sun,“Comyco:
Quality-aware adaptive video streaming via imitation learning,” in
Proceedings of the 27th ACM international conference on multimedia,
2019,pp.429–437.
[22] S. Wang, J. Lin, and F. Ye, “Imitation learning for adaptive video
streaming with future adversarial information bottleneck principle,”
IEEETrans.Mob.Comput.,vol.23,no.12,pp.13670–13683,2024.
[23] T.Huang,R.-X.Zhang,and L.Sun,“Zwei:Aself-playreinforcement
learningframeworkforvideotransmissionservices,”IEEETransMul-
timedia,vol.24,pp.1350–1365,2022.
[24] L. Wei, Y. Liu, F. Wang, D. Zhang, and D. Wang, “Vsas: Decision
transformer-based on-demand volumetric video streaming with passive
frame dropping,” IEEE Internet Things J., vol. 11, no. 8, pp. 13752–
13767,2024.
[25] S.Wang,S.Bi,andY.-J.A.Zhang,“Deepreinforcementlearningwith
communicationtransformerforadaptivelivestreaminginwirelessedge
networks,” IEEE J Sel Areas Commun, vol. 40, no. 1, pp. 308–322,
2022.
[26] C. Qiao, J. Wang, and Y. Liu, “Beyond qoe: Diversity adaptation in
videostreamingattheedge,”IEEE/ACMTransactionsonNetworking,
vol.29,no.1,pp.289–302,2020.
[27] G.Zhang,J.Zhang,Y.Liu,H.Hu,J.Y.Lee,andV.Aggarwal,“Adaptive
video streaming with automatic quality-of-experience optimization,”
IEEETrans.Mob.Comput.,vol.22,no.8,pp.4456–4470,2022.
[28] D. Wu, P. Wu, M. Zhang, and F. Wang, “Mansy: Generalizing neural
adaptive immersive video streaming with ensemble and representation
learning,” IEEE Trans. Mob. Comput., vol. 24, no. 3, pp. 1654–1668,
2025.
[29] G.Zhang,Z.Wang,H.Wei,M.Xiao,H.Yuan,D.Yu,andX.Cheng,“A
novelspatial-temporallearningmethodforenhancinggeneralizationin
adaptivevideostreaming,”IEEETrans.Mob.Comput.,pp.1–16,2025.
[30] N.Kan,C.Li,Y.Jiang,W.Dai,J.Zou,H.Xiong,andL.Toni,“Merina+:
Improving generalization for neural video adaptation via information-
theoretic meta-reinforcement learning,” IEEE Transactions on Circuits
andSystemsforVideoTechnology,pp.1–1,2025.
[31] R.A.Jacobs,M.I.Jordan,S.J.Nowlan,andG.E.Hinton,“Adaptive
mixturesoflocalexperts,”NeuralComputation,vol.3,no.1,pp.79–87,
1991.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:41:18 UTC from IEEE Xplore. Restrictions apply.
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.