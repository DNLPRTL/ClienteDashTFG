SABR: A Stable Adaptive Bitrate Framework
Using Behavior Cloning Pretraining and
Reinforcement Learning Fine-Tuning
Pengcheng Luo∗†, Yunyang Zhao∗†, Bowen Zhang∗†, Genke Yang∗†,
Boon-Hee Soong‡, Senior Member, IEEE, Chau Yuen‡, Fellow, IEEE
∗Ningbo Artificial Intelligence Institute, Shanghai Jiao Tong University, Ningbo, China
†School of Automation and Intelligent Sensing, Shanghai Jiao Tong University, Shanghai, China
Email: {luopeng69131, zyyfighting, bwz96sco, gkyang}@sjtu.edu.cn
‡School of Electrical and Electronic Engineering, Nanyang Technological University, Singapore
Email: {ebhsoong, chau.yuen}@ntu.edu.sg
Abstract—With the advent of 5G, the internet has entered a
new video-centric era. From short-video platforms like TikTok
to long-video platforms like Bilibili, online video services are
reshapinguserconsumptionhabits.AdaptiveBitrate(ABR)con-
trol is widely recognized as a critical factor influencing Quality
of Experience (QoE). Recent learning-based ABR methods have
attracted increasing attention. However, most of them rely on
limitednetworktracesetsduringtrainingandoverlookthewide- Fig.1. AnoverviewofABR.
distribution characteristics of real-world network conditions,
resulting in poor generalization in out-of-distribution (OOD)
scenarios.Toaddressthislimitation,weproposeSABR,atraining
As the user base continues to expand, video streaming
framework that combines behavior cloning (BC) pretraining
serviceprovidersaccumulatemassivevolumesofnetworkdata
with reinforcement learning (RL) fine-tuning. We also introduce
benchmarks,ABRBench-3GandABRBench-4G+,whichprovide on a daily basis. This wealth of data presents unprecedented
wide-coverage training traces and dedicated OOD test sets for opportunities for analyzing user behavior and optimizing
assessingrobustnesstounseennetworkconditions.Experimental streaming strategies, while also providing a solid foundation
results demonstrate that SABR achieves the best average rank
for applying artificial intelligence (AI) techniques to ABR re-
compared with Pensieve, Comyco, and NetLLM across the
search.AIapproachessuchasdeeplearningandreinforcement
proposedbenchmarks.TheseresultsindicatethatSABRenables
more stable learning across wide distributions and improves learning(RL)areincreasinglydrivingABRalgorithmstoward
generalization to unseen network conditions. higher performance and stronger adaptability. Nevertheless,
Index Terms—Adaptive Bitrate, pretraining, fine-tuning, be- currentresearchstillfacesthefollowingtwomajorchallenges:
havior cloning, reinforcement learning
• Limitedgeneralizationtounseendistributions:Moststud-
ies train ABR models on a specific network trace set,
I. INTRODUCTION without fully leveraging the vast amount of network
tracedata.Therefore,modelsexhibitlimitedperformance
The emergence of 5G networks marks a new stage of
when facing unseen network conditions.
internet development, in which video constitutes the dom-
• Degradation under wide-distribution training: When the
inant share of digital content. Short-form services such as
training dataset encompasses a broad spectrum of net-
TikTok and long-form streaming platforms such as Bilibili
work conditions, the efficiency and stability of the ABR
are reshaping content consumption habits, making video the
model training can be significantly undermined.
primary medium for information, entertainment, and social
Similar issues have been studied in the field of large
interaction worldwide. In this context, the smoothness and
languagemodels(LLMs),wherethetwo-stagetrainingframe-
clarityofvideoplaybackaredecisiveforuserexperience,with
workofpretraining+fine-tuninghasproventobeaneffective
Adaptive Bitrate (ABR) algorithms serving as a fundamental
solution [1], [2]. The pretraining stage enables the model
mechanismtoensurehighQualityofExperience(QoE).ABR
to acquire initial representations and understanding of wide-
algorithmsdynamicallyadjustvideobitrateinresponsetoreal-
distribution training data, while the fine-tuning stage enables
time fluctuations in network bandwidth, thereby minimizing
more effective generalization to the target environment. In
stalling and latency, as illustrated in Figure 1.
LLM alignment techniques, Supervised Fine-Tuning (SFT) +
Reinforcement Learning from Human Feedback (RLHF) can
Code:https://github.com/luopeng69131/SABR
Dataset:https://github.com/luopeng69131/ABRBench be regarded as an extension of this framework [3]. SFT uses
5202
guA
03
]IN.sc[
1v68401.9052:viXra

large-scale supervised data to help the model initially under- including ABR. Through multi-modal encoding and Low-
stand human instructions and task structures, while RLHF Rank adaptation (LoRA) [13], it reduced training costs and
leveragestheexplorationcapabilityofRLtoalignthemodel’s showcased the potential of LLMs in ABR tasks.
behavior with human preferences. This combination enables Whiletheseworkshaveadvancedlearning-basedABR,two
GenerativePre-trainedTransformer(GPT)modelstofaithfully limitations persist: limited generalization to unseen network
assist and serve humans in real-world daily applications. conditionsanddegradedstabilityunderwide-distributiontrain-
Inspiredbythis,weproposeatwo-stagetrainingframework ing. These issues underscore the necessity of more robust and
for ABR, termed SABR: Behavior Cloning (BC) pretraining efficient training paradigms, with comprehensive benchmarks
| +RLfine-tuning.Inthepretrainingstage,weadopttheDirect |              |     |       |     |           |     |            | for evaluation. |     |     |     |     |     |     |     |
| ----------------------------------------------------- | ------------ | --- | ----- | --- | --------- | --- | ---------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
| Preference                                            | Optimization |     | (DPO) | [4] | algorithm | to  | perform BC |                 |     |     |     |     |     |     |     |
III. PROPOSEDSABRFRAMEWORK
| on expert | data,    | obtaining | a    | base  | model.    | In the   | fine-tuning |          |           |     |          |     |             |              |     |
| --------- | -------- | --------- | ---- | ----- | --------- | -------- | ----------- | -------- | --------- | --- | -------- | --- | ----------- | ------------ | --- |
|           |          |           |      |       |           |          |             | The SABR | framework |     | consists | of  | two stages: | BC pretrain- |     |
| stage, we | optimize | the       | base | model | using the | Proximal | Policy      |          |           |     |          |     |             |              |     |
Optimization (PPO) [5] algorithm. We also integrate main- ing and RL fine-tuning. In the BC pretraining stage, we train
streamnetworktracesetsandvideostoconstructbenchmarks: the model on expert data using the DPO algorithm to obtain
|             |     |                   |     |     |      |           |      | a base model. | In  | the RL | fine-tuning |     | stage, we | refine the | base |
| ----------- | --- | ----------------- | --- | --- | ---- | --------- | ---- | ------------- | --- | ------ | ----------- | --- | --------- | ---------- | ---- |
| ABRBench-3G |     | and ABRBench-4G+. |     |     | Each | benchmark | con- |               |     |        |             |     |           |            |      |
tains a training set, a test set, and an Out-of-Distribution model via PPO training. An overview of the framework is
(OOD) set. Our main contributions are as follows: shown in Figure 2.
| We  | propose | a stable | framework, |     | SABR, | which | combines |     |     |     |     |     |     |     |     |
| --- | ------- | -------- | ---------- | --- | ----- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
•
| BC         | pretraining | and            | RL    | fine-tuning. | The        | framework | im-        |     |     |     |     |     |     |     |     |
| ---------- | ----------- | -------------- | ----- | ------------ | ---------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| proves     | ABR         | generalization |       | by           | leveraging | a         | wide range |     |     |     |     |     |     |     |     |
| of network |             | trace          | data. |              |            |           |            |     |     |     |     |     |     |     |     |
• WedesignSABRwithDPO-basedBCforfastandstable
| pretraining, |     | and PPO-based     |     | RL  | for         | deeper | exploration, |     |     |     |     |     |     |     |     |
| ------------ | --- | ----------------- | --- | --- | ----------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| enabling     |     | robust adaptation |     | to  | challenging |        | network dy-  |     |     |     |     |     |     |     |     |
namics.
| We  | release | two benchmarks, |     | which | provide |     | an effective |     |     |     |     |     |     |     |     |
| --- | ------- | --------------- | --- | ----- | ------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
•
| evaluation |             | of ABR   | models’ |      | generalization |          | to unseen |     |     |     |     |     |     |     |     |
| ---------- | ----------- | -------- | ------- | ---- | -------------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| network    | conditions. |          |         |      |                |          |           |     |     |     |     |     |     |     |     |
| • We       | empirically | validate |         | that | SABR           | achieves | the best  |     |     |     |     |     |     |     |     |
averagerankcomparedwithPensieve,Comyco,NetLLM,
| and | the other | baselines. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.2. ProposedSABRframework:BCpretraining+RLfine-tuning.
|                |     | II.       | RELATEDWORKS |            |          |             |     |                   |          |      |                |     |           |     |       |
| -------------- | --- | --------- | ------------ | ---------- | -------- | ----------- | --- | ----------------- | -------- | ---- | -------------- | --- | --------- | --- | ----- |
|                |     |           |              |            |          |             |     | A. BC pretraining |          | with | DPO            |     |           |     |       |
| Learning-based |     | ABR       | research     |            | has been | extensively | ex- |                   |          |      |                |     |           |     |       |
|                |     |           |              |            |          |             |     | Originally        | proposed |      | for preference |     | alignment | in  | LLMs, |
| plored, with   | the | core idea | of           | leveraging | neural   | networks    | and |                   |          |      |                |     |           |     |       |
RLtoovercomethelimitationsoftraditionalrule-basedbitrate DPO directly maximizes the likelihood ratio of human-
control. Pensieve [6] was the first to apply the RL model to preferred responses, thereby avoiding the need for reward
|     |     |     |     |     |     |     |     | models | and complex |     | RL optimization |     | commonly | used | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | --------------- | --- | -------- | ---- | --- |
ABR,usingnetworkstates(e.g.,throughputandbufferlength)
as inputs to train an A3C [7] policy on 3G network traces, traditionalRLHFpipelines.Motivatedbyitsabilitytodirectly
thereby demonstrating the feasibility and advantages of RL capture preferences from data, we adopt DPO to learn from
in ABR control. Comyco [8] further introduced quality-aware expert demonstrations for ABR. In the BC pretraining stage,
QoE metrics and employed imitation learning from Model we use DPO to efficiently learn from expert samples, treating
|            |         |                 |     |     |        |       |               | them as | preferred | actions. | This | initializes | a base | model | with |
| ---------- | ------- | --------------- | --- | --- | ------ | ----- | ------------- | ------- | --------- | -------- | ---- | ----------- | ------ | ----- | ---- |
| Predictive | Control | (MPC)-generated |     |     | expert | data, | significantly |         |           |          |      |             |        |       |      |
improving training efficiency and model performance. To stable performance and a stronger control policy for ABR.
address user differences in video quality preferences, Jade [9] In the original DPO algorithm, given a pair of candidate
|                                                       |     |     |     |     |     |     |     | trajectories | τ (the | “winner”) |     | and τ | (the “loser”), | it directly |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | --------- | --- | ----- | -------------- | ----------- | --- |
| incorporatedranking-basedQoEfeedbackintoRLHF,aligning |     |     |     |     |     |     |     |              | w      |           |     | l     |                |             |     |
the optimization objective and achieving QoE improvements maximizes the log-ratio of their probabilities to favor the
|                      |     |         |     |             |     |     |     | preferred | trajectory. | The | objective | is  | defined as: |     |     |
| -------------------- | --- | ------- | --- | ----------- | --- | --- | --- | --------- | ----------- | --- | --------- | --- | ----------- | --- | --- |
| across heterogeneous |     | network |     | conditions. |     |     |     |           |             |     |           |     |             |     |     |
Genet [10] introduced an automatic curriculum learning (cid:104) (cid:16) (cid:104)
|     |     |     |     |     |     |     |     | (θ)=−E |     |     |     |     | π θ (τ | w ) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | ------ | --- | --- |
approach [11], which starts from network environments with L logσ β· log
|                   |     |      |          |     |        |                 |     | DPO |     | (τw,τl)∼D |     |     | π (τ | )                               |     |
| ----------------- | --- | ---- | -------- | --- | ------ | --------------- | --- | --- | --- | --------- | --- | --- | ---- | ------------------------------- | --- |
|                   |     |      |          |     |        |                 |     |     |     |           |     |     | ref  | w                               |     |
| large performance |     | gaps | compared |     | to the | rule baselines, | and |     |     |           |     |     |      |                                 |     |
|                   |     |      |          |     |        |                 |     |     |     |           |     |     | π    | (τ ) (cid:105)(cid:17)(cid:105) |     |
gradually expands the training distribution, thereby enabling −log θ l . (1)
|           |     |         |                |     |          |     |            |     |     |     |     |     | π ref | (τ l ) |     |
| --------- | --- | ------- | -------------- | --- | -------- | --- | ---------- | --- | --- | --- | --- | --- | ----- | ------ | --- |
| the model | to  | improve | progressively. |     | However, |     | curriculum |     |     |     |     |     |       |        |     |
learning may suffer from distributional shift and forget- Here, π (τ) denotes the likelihood of trajectory τ under the
θ
ting issues when the training distribution becomes broad. current model, while π (τ) represents the likelihood under a
ref
NetLLM [12] adapted LLMs to multiple networking tasks, reference model, typically the initialization model. The scalar

β > 0 controls the update strength, and σ(·) denotes the PPO consists of both an actor network π and a critic
θ
sigmoid function. D is the set of preference trajectory pairs. network V . The objective of the actor network is formalized
ϕ
In BC training, since we focus on learning from each state- through the actor loss, given by:
action pair, we adapt the original DPO loss into a step-wise LActor(θ)=E (cid:104) min (cid:0) r (θ)A , clip(r (θ),1−ϵ,1+ϵ)A (cid:1)(cid:105) ,
formulation as follows: t t t t t
(3)
(cid:104) (cid:16) (cid:104) π (aw |s)
L (θ)=−E logσ β· log θ where
DPO-step (s,aw,al)∼D π (aw |s) π (a |s )
ref r (θ)= θ t t , (4)
−log π θ (al |s) (cid:105)(cid:17)(cid:105) . t π θold (a t |s t )
π ref (al |s) denotestheprobabilityratiobetweenthecurrentactornetwork
(2) π (a|s)andthepreviousactornetworkπ (a|s).A isthe
θ θold t
advantage estimate at time step t, and ϵ is the clipping thresh-
Here,(s,aw,al)∼Daresampledstate-actionpairs,whereaw
old. The advantage function A is typically computed using
is an expert (preferred) action and al is a less preferred (e.g., t
GeneralizedAdvantageEstimation(GAE)[18],whichreflects
randomlysampled)alternative.Thelossencouragesthemodel
the reward information that guides policy improvement.
to increase the preference margin for expert actions over less
preferred ones at each step.
Algorithm 2 RL fine-tuning with PPO
The BC training procedure is designed following the DAG-
1: Input: Actor network π θ (initialized from base model),
GER algorithm [14], as detailed in Algorithm 1. Through
critic network V , ABR simulator, iteration N , roll-
ϕ finetune
interactionwiththeABRsimulator,themodelcollectssamples
out steps T , PPO epochs E , mini-batch size
finetune finetune
that are subsequently used for training. The beam search
m , clipping parameter ϵ, discount factor γ, GAE
finetune
strategy follows the implementation from Comyco [8], [15].
parameter λ
Algorithm 1 BC pretraining with DPO 2: Empty buffer B ← ∅, obtain initial state s 1 from ABR
simulator
1: Input: Initial model π θ , BEAM SEARCH POLICY, ABR 3: for 1,2,...,N finetune do
simulator, iteration N , rollout step T , epoch
pretrain pretrain 4: for 1,2,...,T finetune do
E , mini-batch size m
2: In p it r i e a t l r i a z i e n π ref , buffer B ←∅ p , r o et b r t a a i i n n initial state s 1 from 5 6 : : S E e x l e e c c u t te ac a ti t o i n n a th t e ∼ A π B θ R (· s | i s m t u ) lator to obtain reward r t
ABR simulator
and next state s
t+1
3: for 1,2,...,N pretrain do 7: Append transition: B ←B∪{(s t ,a t ,r t ,s t+1 )}
4: for 1,2,...,T pretrain do 8: end for
5 6 : : S E e x l p e e c r t t a a c c t t i i o o n n a a t w t ∼ ← π θ B (· E | A s M t ) SEARCH POLICY(s t ) 9: F Vˆ or a = ll V tra ( n s sitio ) ns in B, compute Vˆ t = V ϕ (s t ) and
8 7 : : A Ra p n p d e o n m d l s y am se p l l e e c : t B an ← alt B er ∪ na { ti ( v s e t , a a c w t ti , o a n l t ) a } l t ̸=aw t 10: C ad t o + v m a 1 n p t u a t g e e ϕ s T A D ˆ t+1 v er ia ro G rs A δ E t w = ith ( r γ t , + λ) γVˆ t+1 − Vˆ t , then
t
9: E s xecute a t in the ABR simulator to obtain next state 11: Set target value V t target =Vˆ t +Aˆ t for critic updates
t+1 12: Augment each transition in B to
10: end for {(s ,a ,r ,s ,Aˆ ,Vtarget)}
1 1 1 3 2 1 : : : for U Sa 1 p m , d 2 a p , t l e . e . π m . θ , i E n u i p s - r i b n e a t g t r c a t h i h n e Bˆ d D o o P f O siz lo e s m s o pr n et B r ˆ a ( in Eq f . ro 2 m ) B 1 1 1 4 3 5 : : : for S U t a 1 p m , d 2 t a p , t l e . e t . m . p , a i t E n r + a i fi 1 - m n b e a e tu t t n c e t e h rs d B t o ˆ θ of an s d ize ϕ m u fin s e i t n un g e f t r h o e m fu B ll PPO
14: end for objective (Eq. 5) on Bˆ
15: end for 16: end for
16: Output: Base model π θ 17: Clear B ←∅
18: π θold ←π θ
19: end for
B. RL fine-tuning with PPO
20: Output: fine-tuned model π θ
OnlyBCtrainingisconstrainedtothedistributionofexpert
policies and lacks the capacity to explore a broader policy The full PPO objective combines the actor loss, critic loss,
space. To improve generalization in network environments, and an entropy regularization term, and is given by:
w PP e O pe is rfo a rm pol R ic L y-g fi r n a e d - i t e u n n t– in b g ase o d f t R h L e m ba e s t e ho m d o t d h e a l t r u e s s i t n r g ict P s P t O he . LPPO(θ)=E t (cid:104) LActor(θ)−c 1 (cid:0) V ϕ (s t )−V t target(cid:1)2 +c 2 S[π θ ](s t ) (cid:105) ,
extent of policy updates between iterations to prevent training (5)
instability and performance collapse. PPO has demonstrated whereV ϕ (s t )isthestatevaluepredictedbythecriticnetwork,
strong stability and sample efficiency in both continuous [16] with (cid:0) V (s ) − Vtarget(cid:1)2 as the critic loss where Vtarget is
ϕ t t t
and discrete tasks [17]. the target value; S[π ](s ) is an entropy regularization term
θ t

| encouraging | exploration; |     | and | c and c | are their | respective |     |     |     |          |     |     |     |     |
| ----------- | ------------ | --- | --- | ------- | --------- | ---------- | --- | --- | --- | -------- | --- | --- | --- | --- |
|             |              |     |     | 1       | 2         |            |     |     |     | TABLEIII |     |     |     |     |
HYPERPARAMETERSFORTHESABRFRAMEWORK
| weighting | coefficients. |     | The overall | RL  | fine-tuning | procedure |     |        |             |     |     |     |       |     |
| --------- | ------------- | --- | ----------- | --- | ----------- | --------- | --- | ------ | ----------- | --- | --- | --- | ----- | --- |
| with PPO  | is shown      | in  | Algorithm   | 2.  |             |           |     |        |             |     |     |     |       |     |
|           |               |     |             |     |             |           |     | Symbol | Description |     |     |     | Value |     |
DPOparameters
IV. PROPOSEDBENCHMARKS
|     |     |     |     |     |     |     |     | N   | Iteration(DPO) |     |     |     | 15  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
pretrain
We release two benchmarks: ABRBench-3G and E Epochsperpretrainingiteration 5
pretrain
ABRBench-4G+. Each benchmark consists of both video T pretrain Rolloutstepsperiteration 2000
content and network traces. The traces are reorganized and m pretrain Mini-batchsize(pretraining) 128
|     |     |     |     |     |     |     |     | α   | DPOlearningrate |     |     |     | 3e-4 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | ---- | --- |
pretrain
curated from publicly available trace sets on the internet, β DPOupdatescale 0.1
such as Lumos 4G/5G [19], [20] and FCC [6], [21], [22]. PPOparameters
Each benchmark contains multiple trace sets to ensure broad N finetune Iteration(PPO) 244
|     |     |     |     |     |     |     |     | E finetune | PPOepochsperupdate |     |     |     | 10  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------ | --- | --- | --- | --- | --- |
coverage of network conditions. T Rolloutstepsperenvironment 512
finetune
In each benchmark, traces are divided into training, testing, m Mini-batchsize(fine-tuning) 64
finetune
|           |       |           |                 |             |          |                |     | α        | PPOlearningrate   |     |     |     | 3e-4 |     |
| --------- | ----- | --------- | --------------- | ----------- | -------- | -------------- | --- | -------- | ----------------- | --- | --- | --- | ---- | --- |
| and OOD   | sets. | The       | training        | and testing | sets     | are created by |     | finetune |                   |     |     |     |      |     |
|           |       |           |                 |             |          |                |     | ϵ        | Clippingthreshold |     |     |     | 0.2  |     |
| splitting | each  | trace set | proportionally. | For         | example, | in FCC-        |     |          |                   |     |     |     |      |     |
|           |       |           |                 |             |          |                |     | γ        | Discountfactor    |     |     |     | 0.99 |     |
18, 75% of traces are allocated to the training set, while the λ GAEparameter 0.95
|           |          |       |              |              |        |               |     | c1  | Coefficientofcriticloss |     |     |     | 0.5 |     |
| --------- | -------- | ----- | ------------ | ------------ | ------ | ------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |
| remaining | 30%      | are   | used for     | testing. The | OOD    | set is also   |     |     |                         |     |     |     |     |     |
|           |          |       |              |              |        |               |     | c2  | Coefficientofentropy    |     |     |     | 0.0 |     |
| used to   | evaluate | model | performance, | but          | unlike | the test set, |     |     |                         |     |     |     |     |     |
Otherparameters
it specifically focuses on assessing generalization to unseen L beam Beamsearchfuturehorizon 5
distributions. Therefore, trace sets included in the OOD set Kmax Beamsearchmaximumbeam 5000
| are not split | or  | reused | in other    | sets. |            |              |     |     |                                  |     |     |     |     |     |
| ------------- | --- | ------ | ----------- | ----- | ---------- | ------------ | --- | --- | -------------------------------- | --- | --- | --- | --- | --- |
| For training, |     | models | are trained | on    | the entire | training set |     |     |                                  |     |     |     |     |     |
|               |     |        |             |       |            |              |     | R3G | = {300,750,1200,1850,2850,4300}, |     |     |     |     |     |
with all traces randomly shuffled. Evaluation is performed with while
separately for each trace set within the test and OOD sets. ABRBench-4G+ uses the Big Buck Bunny [30] video with
R4G+ ={1000,2500,5000,8000,16000,40000}.
| During evaluation, |      | we     | preserve | the trace | set granularity, | since    |     |     |     |     |     |     |     |     |
| ------------------ | ---- | ------ | -------- | --------- | ---------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| certain trace      | sets | (e.g., | those    | with high | bandwidth)       | can skew |     |     |     |     |     |     |     |     |
V. IMPLEMENTATIONDETAILS
theoverallaverageQoEandmasktheperformanceunderother
bandwidth conditions. Tables I and II present the trace set The state, action, reward function, and state transition in
information of ABRBench-3G and ABRBench-4G+. ourMarkovDecisionProcessareconsistentwiththoseinPen-
sieve[6].OurABRsimulatorfollowsthedesignofPensieve’s
TABLEI Python environment [6], while using the C++ implementation
ABRBENCH-3GTRACESTATISTICS from [8], [15] to improve efficiency. Apart from the C++
|     |     |     |     |     |     |     | simulator, | all | other components |     | are implemented |     | in Python. |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------------- | --- | --------------- | --- | ---------- | --- |
Group TraceSet Count Range(Mbps) The BC pretraining is implemented in PyTorch [31], while
|          |     |                     |     |      |            |     | RL fine-tuning  |                 | is based      | on the      | PPO         | algorithm | from             | Stable- |
| -------- | --- | ------------------- | --- | ---- | ---------- | --- | --------------- | --------------- | ------------- | ----------- | ----------- | --------- | ---------------- | ------- |
| Training |     | Samewithtest        |     | 1828 | 0.00∼45.38 |     |                 |                 |               |             |             |           |                  |         |
|          |     |                     |     |      |            |     | Baselines3      | (SB3)           | [32].         | During      | training,   | we        | utilize the      | Vector  |
|          |     | FCC-16[6],[21],[22] |     | 69   | 0.00∼8.95  |     |                 |                 |               |             |             |           |                  |         |
|          |     |                     |     |      |            |     | Environment     |                 | module        | of SB3      | to enable   | parallel  | sample           | col-    |
|          |     | FCC-18[23],[24]     |     | 100  | 0.00∼41.76 |     |                 |                 |               |             |             |           |                  |         |
| Test     |     | Oboe[25],[26]       |     | 100  | 0.16∼9.01  |     |                 |                 |               |             |             |           |                  |         |
|          |     |                     |     |      |            |     | lection,        | thereby         | improving     | training    | efficiency. |           | The number       | of      |
|          |     | Puffer-21[26],[27]  |     | 100  | 0.00∼25.14 |     |                 |                 |               |             |             |           |                  |         |
|          |     |                     |     |      |            |     | parallel        | environments    |               | is set to   | 4.          |           |                  |         |
|          |     | Puffer-22[26],[27]  |     | 100  | 0.00∼9.29  |     |                 |                 |               |             |             |           |                  |         |
|          |     |                     |     |      |            |     | In the          | implementations |               | of          | Pensieve    | [6]       | and Comyco       | [8],    |
| OOD      |     | HSR [24]            |     | 34   | 0.00∼44.68 |     |                 |                 |               |             |             |           |                  |         |
|          |     |                     |     |      |            |     | the input       | features        | are           | represented | as          | a 6-by-8  | matrix.          | In our  |
|          |     |                     |     |      |            |     | implementation, |                 | we flatten    | this        | matrix      | into      | a 48-dimensional |         |
|          |     |                     |     |      |            |     | vector.         | The             | actor network | π θ         | (base       | model)    | adopts           | a fully |
TABLEII connected network of [48,tanh,64,tanh,64,6], while the
ABRBENCH-4G+TRACESTATISTICS critic network is designed as [48,tanh,64,tanh,64,1]. The
|     |     |     |     |     |     |     | two networks |     | do not | share parameters. |     | For | both DPO | and |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | ----------------- | --- | --- | -------- | --- |
Group TraceSet Count Range(Mbps) PPO training, the Adam optimizer [33] is employed. The
Training Samewithtest 262 0.00∼1890.00 hyperparameter settings of the SABR are shown in Table III.
|     |     | Lumos4G[19],[20] |     | 53  | 0.00∼270.00 |     |     |     |     |     |     |     |     |     |
| --- | --- | ---------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
VI. EVALUATION
| Test |     | Lumos5G[19],[20] |     | 37  | 0.00∼1920.00 |     |                 |       |                |     |           |     |            |      |
| ---- | --- | ---------------- | --- | --- | ------------ | --- | --------------- | ----- | -------------- | --- | --------- | --- | ---------- | ---- |
|      |     | SolisWi-Fi[28]   |     | 24  | 0.00∼124.00  |     | A. Experimental |       | setup          |     |           |     |            |      |
|      |     | Ghent[24]        |     | 40  | 0.00∼110.97  |     |                 |       |                |     |           |     |            |      |
| OOD  |     |                  |     |     |              |     | We              | build | a trace-driven | ABR | simulator |     | [6], where | both |
|      |     | Lab[24]          |     | 61  | 0.16∼175.91  |     |                 |       |                |     |           |     |            |      |
networktracesandvideocontentaredrawnfromABRBench-
|     |     |     |     |     |     |     | 3G and | ABRBench-4G+. |     | Each | experiment |     | is conducted | on  |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------- | --- | ---- | ---------- | --- | ------------ | --- |
We denote the set of available bitrates as R. Specif- videos consisting of 49 chunks, with each chunk lasting 4
ically, ABRBench-3G uses the Envivio-Dash3 [29] video seconds, emulated over the collected network traces.

We evaluate performance using the QoE metrics: TABLEIV
QOEPERFORMANCECOMPARISONONTHEABRBENCH-3GTESTSETS
N N−1 N
(cid:88) (cid:88) (cid:12) (cid:12) (cid:88)
QoE = q(R
n
)−δ (cid:12)q(R
n+1
)−q(R
n
)(cid:12)−µ T
n
,
Algorithm FCC-16 FCC-18 Oboe Puffer-21 Puffer-22 AveRank
n=1 n=1 n=1 BB 25.37 131.54 82.74 -6.05 13.28 7.2
(6)
BOLA 32.51 123.42 81.02 38.35 30.99 6.0
where N represents the total number of video chunks, R is QUETRA 33.91 122.25 82.84 42.48 36.89 4.4
n
RobustMPC 36.56 143.30 96.14 34.13 36.90 3.4
the bitrate of the n-th chunk, and T denotes the rebuffering
n Pensieve 34.50 134.39 90.92 38.94 35.23 3.8
time at that step. The function q(R ) maps the bitrate R Comyco 32.10 143.89 96.23 -4.09 31.34 4.8
n n NetLLM 21.92 141.91 97.39 37.55 33.73 4.6
to a corresponding quality score. δ is the smoothness penalty SABR 36.68 145.18 99.68 36.05 40.05 1.8
coefficient, and µ is the rebuffering penalty coefficient.
Consistentwithpriorwork[6],[8],[34],weadoptq(R )=
n TABLEV
R n , where R n ∈R3G or R4G+. We set N =49, δ =1, and QOEPERFORMANCECOMPARISONONTHEABRBENCH-4G+TESTSETS
use µ = 4.3 for ABRBench-3G and µ = 40 for ABRBench-
4G+. We compare SABR against baselines: Algorithm Lumos4G Lumos5G SolisWi-Fi AveRank
• Buffer-Based(BB):Asimpleheuristicthatadaptsbitrates BB 1255.91 1726.66 429.34 5.0
BOLA 1200.05 1614.40 477.08 5.0
based on buffer occupancy to reduce rebuffering.
QUETRA 754.43 992.74 421.58 7.7
• BOLA [35]: Uses Lyapunov optimization to select bi- RobustMPC 1283.05 1696.77 589.64 3.0
trates solely considering buffer occupancy observations. Pensieve 1160.76 1828.24 447.84 5.0
Comyco 1285.43 1835.42 552.55 2.0
• RobustMPC [34]: An extension of the MPC method. It NetLLM 672.35 1510.35 474.15 6.7
maximizesagivenQoEmetricoverahorizonof5future SABR 1309.65 1832.14 576.33 1.7
chunks.
• QUETRA[36]:Aqueueing-theoreticalgorithmthatmod-
els the ABR task as an M/D/1/K system, enabling bitrate ABRBench-4G+, SABR achieved the highest QoE on Lumos
decisions based on expected buffer occupancy. 4G, while performing slightly worse than the best methods
• Pensieve [6]: An RL-based ABR method that trains a on the other two trace sets. Across both benchmarks, SABR
policy network with A3C to maximize a QoE reward. attains the lowest average rank among all methods, demon-
• Comyco[8]:Alearning-basedABRmethodthatemploys stratingitsoverallsuperiorperformanceandrobustnessacross
imitation learning to train a policy from MPC-generated diverse network conditions.
expert trajectories.
C. Evaluation on the OOD datasets
• NetLLM [12]: Adapts LLMs to ABR by combining
parameter-efficient fine-tuning (LoRA) with offline RL. To evaluate the generalization performance of the models
under unseen distributions, we conducted comparisons on the
For the comparative evaluation, each algorithm is executed
OOD datasets of ABRBench-3G (HSR) and ABRBench-4G+
ten times, and the average performance is reported. For
(Ghent and Lab). The learning-based models were trained on
the learning-based methods (SABR, Pensieve, Comyco, and
the corresponding benchmark training sets before testing. Ta-
NetLLM), each result is obtained by training ten separate
bleVIpresentstheQoEperformanceofthedifferentmethods.
models,andthereportedperformanceistheaverageacrossall
SABR obtained the lowest average rank (2.0), outperforming
modelsonthetestruns.Furthermore,wecomputetheaverage
Comyco (3.7), RobustMPC (4.0), and other baselines. This
rank of each algorithm across the multiple trace sets in each
indicates that SABR maintains strong performance on unseen
benchmark. Formally, let r denote the rank of algorithm i
i,j
distributions.
on trace set j, and let M be the total number of trace sets in
the benchmark. The average rank of algorithm i is defined as
TABLEVI
1 (cid:88)
M QOEPERFORMANCECOMPARISONONTHEOODSETS
Ave Rank(i)= r . (7)
M i,j
Algorithm HSR Ghent Lab AveRank
j=1
BB 138.86 834.30 1429.22 4.3
A lower average rank indicates better overall performance.
BOLA 137.02 912.39 1342.63 5.0
QUETRA 132.56 566.61 965.94 7.0
B. Proposed SABR vs. existing baselines
RobustMPC 122.37 1075.17 1527.84 4.0
To evaluate the generalization capability of the models, we Pensieve 137.82 652.45 1508.43 4.7
Comyco 130.22 963.94 1595.09 3.7
conducted comparisons across different methods on the test
NetLLM 129.25 1035.09 1307.49 5.3
sets of ABRBench-3G and ABRBench-4G+. The learning- SABR 142.20 1023.56 1561.18 2.0
based models were trained on the corresponding benchmark
training sets before testing. Tables IV and V show the QoE
performance of the different methods.
VII. CONCLUSION
For ABRBench-3G, SABR achieved the best QoE per- In this paper, we propose SABR, a two-stage framework
formance on FCC-16, FCC-18, Oboe, and Puffer-22. For consisting of BC pretraining and RL fine-tuning. The frame-

| work is designed | to  | improve | stability | and | training | efficiency |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------- | --------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
[15] T.Huang,“Comycoforlinear-basedQoE(comyco-lin),”https://github.
com/godka/comyco-lin,2025.
| under wide-distribution |     | data. | In the | pretraining |     | stage, we em- |     |     |     |     |     |     |     |     |
| ----------------------- | --- | ----- | ------ | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[16] E.Todorov,T.Erez,andY.Tassa,“Mujoco:Aphysicsengineformodel-
ployDPOtolearnfromexpertdemonstrations,whichprovides
basedcontrol,”in2012IEEE/RSJinternationalconferenceonintelligent
| the model | with an | initial understanding |     | of  | the training | distri- |                   |     |                         |     |     |     |     |     |
| --------- | ------- | --------------------- | --- | --- | ------------ | ------- | ----------------- | --- | ----------------------- | --- | --- | --- | --- | --- |
|           |         |                       |     |     |              |         | robotsandsystems. |     | IEEE,2012,pp.5026–5033. |     |     |     |     |     |
bution and establishes a basic control policy. The fine-tuning [17] P. C. Luo, H. Q. Xiong, B. W. Zhang, J. Y. Peng, and Z. F. Xiong,
|     |     |     |     |     |     |     | “Multi-resource |     | constrained | dynamic | workshop | scheduling |     | based on |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | ------- | -------- | ---------- | --- | -------- |
stagethenappliesPPOtofurtheroptimizethepolicy,enhanc-
|     |     |     |     |     |     |     | proximal | policy | optimisation,” | International |     | journal | of production | re- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | -------------- | ------------- | --- | ------- | ------------- | --- |
ing generalization to unseen network conditions. We further search,vol.60,no.19,pp.5937–5955,2022.
contribute two benchmarks, ABRBench-3G and ABRBench- [18] J. Schulman, P. Moritz, S. Levine, M. Jordan, and P. Abbeel, “High-
4G+, to evaluate performance across wide-distribution data dimensionalcontinuouscontrolusinggeneralizedadvantageestimation,”
arXivpreprintarXiv:1506.02438,2015.
and unseen environments. Experimental results show that, on [19] A.Narayanan,X.Zhang,R.Zhu,A.Hassan,S.Jin,X.Zhu,X.Zhang,
both benchmarks, SABR achieves the best average rank com- D.Rybkin,Z.Yang,Z.M.Maoetal.,“Avariegatedlookat5ginthe
wild:performance,power,andqoeimplications,”inProceedingsofthe
| pared with | methods | such as | Pensieve, | Comyco, |     | and NetLLM, |     |     |     |     |     |     |     |     |
| ---------- | ------- | ------- | --------- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
2021ACMSIGCOMM2021Conference,2021,pp.610–625.
demonstrating better generalization performance. In future [20] A. Narayanan, E. Ramadan, R. Mehta, X. Hu, Q. Liu, R. A. Fezeu,
work, we plan to extend our benchmarks with more traces U. K. Dayalan, S. Verma, P. Ji, T. Li et al., “Lumos5g: Mapping and
|            |            |        |               |     |     |                | predicting | commercial | mmwave |     | 5g throughput,” | in  | Proceedings | of the |
| ---------- | ---------- | ------ | ------------- | --- | --- | -------------- | ---------- | ---------- | ------ | --- | --------------- | --- | ----------- | ------ |
| and videos | to provide | a more | comprehensive |     |     | evaluation for |            |            |        |     |                 |     |             |        |
ACMinternetmeasurementconference,2020,pp.176–193.
ABR research.
|     |     |     |     |     |     |     | [21] H. Riiser, | P. Vigmostad, |             | C. Griwodz,  | and | P. Halvorsen, |                    | “Commute |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------------- | ----------- | ------------ | --- | ------------- | ------------------ | -------- |
|     |     |     |     |     |     |     | path            | bandwidth     | traces from | 3g networks: |     | Analysis      | and applications,” |          |
inProceedingsofthe4thACMMultimediaSystemsConference,2013,
REFERENCES
pp.114–118.
|     |     |     |     |     |     |     | [22] Federal | Communications |     |     | Commission, | “Raw |     | data - |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- | --- | --- | ----------- | ---- | --- | ------ |
[1] A.Radford,K.Narasimhan,T.Salimans,I.Sutskeveretal.,“Improving
|     |     |     |     |     |     |     | measuring | broadband |     | america |     | 2016,” | https://www.fcc. |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ------- | --- | ------ | ---------------- | --- |
languageunderstandingbygenerativepre-training,”2018. gov/reports-research/reports/measuring-broadband-america/
[2] J.Devlin,M.-W.Chang,K.Lee,andK.Toutanova,“Bert:Pre-training raw-data-measuring-broadband-america-2016,2016.
ofdeepbidirectionaltransformersforlanguageunderstanding,”inPro-
[23] ——,“Rawdatareleases-measuringbroadbandamerica2018,”https:
ceedingsofthe2019conferenceoftheNorthAmericanchapterofthe
//www.fcc.gov/oet/mba/raw-data-releases,2018.
associationforcomputationallinguistics:humanlanguagetechnologies,
[24] Z.Meng,J.Chen,Y.Guo,C.Sun,H.Hu,andM.Xu,“Pitree:Practical
volume1(longandshortpapers),2019,pp.4171–4186. implementationofabralgorithmsusingdecisiontrees,”inProceedings
[3] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, of the 27th ACM International Conference on Multimedia, 2019, pp.
|           |             |     |           | et  | al.,      |          |            |     |     |     |     |     |     |     |
| --------- | ----------- | --- | --------- | --- | --------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| C. Zhang, | S. Agarwal, | K.  | Slama, A. | Ray | “Training | language | 2431–2439. |     |     |     |     |     |     |     |
modelstofollowinstructionswithhumanfeedback,”Advancesinneural
|     |     |     |     |     |     |     | [25] Z. Akhtar, | Y. S. | Nam, R. | Govindan, | S. Rao, | J. Chen, | E. Katz-Bassett, |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ----- | ------- | --------- | ------- | -------- | ---------------- | --- |
informationprocessingsystems,vol.35,pp.27730–27744,2022.
B.Ribeiro,J.Zhan,andH.Zhang,“Oboe:Auto-tuningvideoabralgo-
[4] R. Rafailov, A. Sharma, E. Mitchell, C. D. Manning, S. Ermon, and rithms to network conditions,” in Proceedings of the 2018 Conference
C. Finn, “Direct preference optimization: Your language model is oftheACMSpecialInterestGrouponDataCommunication,2018,pp.
| secretly | a reward | model,” Advances |     | in neural | information | processing | 44–58. |     |     |     |     |     |     |     |
| -------- | -------- | ---------------- | --- | --------- | ----------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
systems,vol.36,pp.53728–53741,2023.
[26] N.Kan,Y.Jiang,C.Li,W.Dai,J.Zou,andH.Xiong,“Improvinggen-
[5] J.Schulman,F.Wolski,P.Dhariwal,A.Radford,andO.Klimov,“Prox-
|     |     |     |     |     |     |     | eralization | for neural | adaptive | video | streaming | via | meta reinforcement |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | -------- | ----- | --------- | --- | ------------------ | --- |
imalpolicyoptimizationalgorithms,”arXivpreprintarXiv:1707.06347, learning,”inProceedingsofthe30thACMinternationalconferenceon
| 2017. |     |     |     |     |     |     | multimedia,2022,pp.3006–3016. |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
[6] H.Mao,R.Netravali,andM.Alizadeh,“Neuraladaptivevideostream- [27] F. Y. Yan, H. Ayers, C. Zhu, S. Fouladi, J. Hong, K. Zhang, P. Levis,
ingwithpensieve,”inProceedingsoftheconferenceoftheACMspecial
|     |     |     |     |     |     |     | and K. | Winstein,“Learning |     | in situ: | a randomizedexperiment |     |     | in video |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------------ | --- | -------- | ---------------------- | --- | --- | -------- |
interestgroupondatacommunication,2017,pp.197–210.
streaming,”in17thUSENIXSymposiumonNetworkedSystemsDesign
[7] V. Mnih, A. P. Badia, M. Mirza, A. Graves, T. Lillicrap, T. Harley, andImplementation(NSDI20),2020,pp.495–511.
D.Silver,andK.Kavukcuoglu,“Asynchronousmethodsfordeeprein- [28] G. Lv, Q. Wu, W. Wang, Z. Li, and G. Xie, “Lumos: Towards
forcement learning,” in International conference on machine learning. better video streaming qoe through accurate throughput prediction,” in
PmLR,2016,pp.1928–1937.
IEEEINFOCOM2022-IEEEConferenceonComputerCommunications.
[8] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,X.Yao,andL.Sun,“Comyco:
IEEE,2022,pp.650–659.
Quality-aware adaptive video streaming via imitation learning,” in [29] DASH Industry Forum, “dash.js: Mpeg-dash reference client,” https://
Proceedings of the 27th ACM international conference on multimedia, github.com/Dash-Industry-Forum/dash.js,2012.
2019,pp.429–437. [30] BlenderFoundation,“Bigbuckbunny,”https://peach.blender.org/,2008.
[9] T. Huang, R.-X. Zhang, C. Wu, and L. Sun, “Optimizing adaptive [31] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan,
videostreamingwithhumanfeedback,”inProceedingsofthe31stACM
|     |     |     |     |     |     |     | T. Killeen, | Z.  | Lin, N. | Gimelshein, | L. Antiga | et  | al., “Pytorch: | An  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ----------- | --------- | --- | -------------- | --- |
InternationalConferenceonMultimedia,2023,pp.1707–1718. imperative style, high-performance deep learning library,” Advances in
[10] Z.Xia,Y.Zhou,F.Y.Yan,andJ.Jiang,“Genet:Automaticcurriculum neuralinformationprocessingsystems,vol.32,2019.
generationforlearningadaptationinnetworking,”inProceedingsofthe [32] A.Raffin,A.Hill,A.Gleave,A.Kanervisto,M.Ernestus,andN.Dor-
ACMSIGCOMM2022Conference,2022,pp.397–413. mann,“Stable-baselines3:Reliablereinforcementlearningimplementa-
[11] Y. Bengio, J. Louradour, R. Collobert, and J. Weston, “Curriculum tions,”Journalofmachinelearningresearch,vol.22,no.268,pp.1–8,
| learning,” | in Proceedings | of  | the 26th | annual | international | conference | 2021. |     |     |     |     |     |     |     |
| ---------- | -------------- | --- | -------- | ------ | ------------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
onmachinelearning,2009,pp.41–48. [33] D.P.KingmaandJ.Ba,“Adam:Amethodforstochasticoptimization,”
[12] D. Wu, X. Wang, Y. Qiao, Z. Wang, J. Jiang, S. Cui, and F. Wang, arXivpreprintarXiv:1412.6980,2014.
“Netllm:Adaptinglargelanguagemodelsfornetworking,”inProceed- [34] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic
ingsoftheACMSIGCOMM2024Conference,2024,pp.661–678. approachfordynamicadaptivevideostreamingoverhttp,”inProceed-
[13] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, ings of the 2015 ACM conference on special interest group on data
W.Chenetal.,“Lora:Low-rankadaptationoflargelanguagemodels.” communication,2015,pp.325–338.
ICLR,vol.1,no.2,p.3,2022. [35] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “Bola: Near-optimal
[14] S.Ross,G.Gordon,andD.Bagnell,“Areductionofimitationlearning bitrate adaptation for online videos,” IEEE/ACM transactions on net-
and structured prediction to no-regret online learning,” in Proceedings working,vol.28,no.4,pp.1698–1711,2020.
ofthefourteenthinternationalconferenceonartificialintelligenceand [36] P. K. Yadav, A. Shafiei, and W. T. Ooi, “Quetra: A queuing theory
statistics. JMLR Workshop and Conference Proceedings, 2011, pp. approach to dash rate adaptation,” in Proceedings of the 25th ACM
627–635. internationalconferenceonMultimedia,2017,pp.1130–1138.