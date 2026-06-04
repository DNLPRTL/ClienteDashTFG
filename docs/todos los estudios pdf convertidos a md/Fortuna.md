IEEETRANSACTIONSONMULTIMEDIA,VOL.27,2025 8185
Optimizing Adaptive Video Streaming: Offline
Reinforcement Learning and Meta-Learning
in Diverse Networks
LingYi ,YongbinQin ,andRuizhangHuang
Abstract—Recent years have seen the optimization of quality quality level, enabling users to select the most suitable video
of experience (QoE) through learning adaptive bitrate (ABR) chunk according to available bandwidth. However, due to net-
algorithms from internet video streams. However, the complex
work bandwidth limitations, ABR algorithms may not always
nature of the real-world Internet, characterized by heavy-tailed
requesthigh-qualityvideosconsistently.
behavior, diversity, and unpredictability, hinder the effective
learningofoff-the-shelfreinforcementlearning(RL)-basedABR ThemainexistingABRalgorithmsusesimplecontrolrulesor
algorithms. As a result, existing methods inevitably fail to reinforcement learning (RL) based methods. For example, RB
achieve optimal performance under various network conditions algorithm[2]isonlybasedonnetworkbandwidthorbufferus-
and user QoE objectives. We propose Fortuna, a novel offline
agee.g.,BOLAalgorithm[3],[4],oracombinationofthetwo
meta RL ABR algorithm that can effectively learn from these
schemes (e.g., robustMPC [5], Oboe [6], Bayesian-MPC [7]).
heavy-tailed internet data features and become more practical.
Fortuna is primarily divided into two phases. In the offline These methods require careful adjustment and are unable to
phase,Fortunautilizesdiverseofflinedataforlearningtoreduce adapt to different network bandwidths or different QoE ob-
the costly online RL interaction expense, while in the online jectives. State-of-the-art MPC algorithm [5] uses future video
phase,wegraduallyincreasevideostreamingsessionscomplexity
chunksbydynamicallyoptimizingQoEmetrics,whichhasbet-
throughcurriculumlearningtoquicklyadapttospecificnetwork
ter performance than the simple fixed schemes e.g., BOLA,
conditions. Fortuna then utilizes meta-learning to optimize ABR
policiesandenhancegeneralization.Additionally,tobetterlearn RB.However,MPCreliesonaccuratenetworkbandwidthpre-
networkfeatures,FortunafurtheroptimizesQoEbylearninglow- dictions, especially on future networks. Due to the variability
level TCP congestion control information. Experimental results of network bandwidth, MPC is difficult to predict accurately,
from trace-driven and real-world scenarios demonstrate that
but inaccurate predictions may cause future video freezes and
Fortuna enhances learning efficiency by more than 7.5%–4 ×,
low-qualityvideoetc.Additionally,sinceBOLAandMPCcan-
reduces stall time by 4.6%–14.2%, and generalizes to different
networkconditionsandvideostreams. notadjustparametersaccordingtospecificnetworkconditions
andaretoosensitivetoparameters,thenOboe[6]isproposedto
Index Terms—Adaptive bitrate algorithm, offline meta
automaticallyadjustparameters,whichcanenhanceQoEvalue
reinforcementlearning,qualityofexperience.
inspecificscenarios.
Recently,Pensieve[8]wasproposedtofurtherimproveQoE
I. INTRODUCTION
by using RL to train a neural network to generate ABR algo-
VIDEO streaming is the primary internet application, ac-
rithms,whicheffectivelysolvesthelimitationsofexistingABR
countingfornearly75%ofalltraffic[1].Inadaptivebitrate
algorithms.Alternatively,PPO-basedpolicyoptimizationcanbe
(ABR)videostreaming,videosaretypicallydividedintovarious
utilized to learn more efficient ABR strategies [9],[10]. How-
small video chunks or segments. Video users can request spe-
ever, due to the randomness of network bandwidth, RL-based
cificvideochunksbasedontheirpreferencesandnetworkcon-
methods are difficult to converge quickly or generate a large
ditions. Each video chunk is assigned a particular bitrate and
amountofgradientvariance[52].Imitationlearning[11],[12]
isusedforsolvingMPCproblems,butthemethodisonlyappli-
Received18November2024;revised22January2025;accepted15Febru-
cable to known environments and cannot be used for complex
ary2025.Dateofpublication10September2025;dateofcurrentversion12
November2025.ThisworkwassupportedinpartbytheNationalNaturalSci- network scenarios. Fugu [13] combines classical control with
enceFoundationofChinaunderGrant62066008,inpartbytheKeyProjectsof a learned network predictor, trained with supervised learning
ScienceandTechnologyofGuizhouProvinceunderGrant[2020]1Z055,andin
in situ on data from the real deployment environment. Addi-
partbytheNationalKeyR&DProgramofChinaunderGrant2023YFC3304500.
Theassociateeditorcoordinatingthereviewofthisarticleandapprovingitfor tionally, ABRL [14] converts ABR policy into a linear model
publicationwasProf.QiangWu.(Correspondingauthor:YongbinQin.) forbettercomprehensionandsafety,allowinghumanengineers
The authors are with the Text Computing & Cognitive Intelligence Engi-
to verify it while slightly increasing the average stall rate by
neeringResearchCenterofNationalEducationMinistry,CollegeofComputer
ScienceandTechnology,GuizhouUniversity,Guiyang550025,China,andalso 0.8%.Anotherapproachistoemploymeta-RLtechniqueslike
withtheStateKeyLaboratoryofPublicBigData,CollegeofComputerScience MAML [15], [16], [17] or Pearl [18] to adaptive to various
andTechnology,GuizhouUniversity,Guiyang550025,China(e-mail:yiling-
network conditions. Moreover, Genet [19] introduces increas-
phd@gmail.com;ybqin@gzu.edu.cn;cse.rzhuang@gzu.edu.cn).
DigitalObjectIdentifier10.1109/TMM.2025.3604930 ingly challenging environments through a curriculum learning
1520-9210©2025IEEE.Allrightsreserved,includingrightsfortextanddatamining,andtrainingofartificialintelligenceandsimilartechnologies.
Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore. Restrictions apply.

| 8186                 |                |         |               |       |            |        |              |     |     | IEEETRANSACTIONSONMULTIMEDIA,VOL.27,2025 |     |     |     |     |     |
| -------------------- | -------------- | ------- | ------------- | ----- | ---------- | ------ | ------------ | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
| strategy             | [20], enabling |         | RL models     |       | to perform | better | across       | a   |     |                                          |     |     |     |     |     |
| wider range          | of             | network | environments. |       | However,   |        | this method  |     |     |                                          |     |     |     |     |     |
| fails to effectively |                | learn   | from          | large | volumes    | of     | offline data | as  |     |                                          |     |     |     |     |     |
wellasadapttothecomplexityofvideostreams.Zuoetal.[21]
introduceRuyi,anoff-policyRL-basedvideostreamingsystem
| that integrates |           | preference | awareness |       | into      | the QoE | model      | and |     |     |     |     |     |     |     |
| --------------- | --------- | ---------- | --------- | ----- | --------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| the ABR         | algorithm | [22],      | [23].     | It is | optimized | with    | a modified |     |     |     |     |     |     |     |     |
DeepQ-learningalgorithmusingexperiencereplay[24].Each
schemecanbeusedinaspecificenvironment,butcannoteffec-
tivelylearnandbegeneralizedtodiversenetworkenvironments
orbitratedecisions.ThisisbecauseonlinelearningofABRal- Fig.1. TheprincipleofHTTP-baseddynamicadaptivevideostreaming.
| gorithms | does not | explore | safely | and | cannot | effectively |     | learn |     |     |     |     |     |     |     |
| -------- | -------- | ------- | ------ | --- | ------ | ----------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
fromthesecomplexnetworkfeatures[25],[26].
|     |     |     |     |     |     |     |     |     | 2) AnovelRLtechniqueusescurriculumlearningtohandle |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Specifically,inreal-worldadaptivevideostreamingscenarios,
unboundedvideostreamingsessions.
learningalgorithmsrelyonspecificdataorenvironmentstotrain
|     |     |     |     |     |     |     |     |     | 3) Tobetterlearntheunderlyingnetworkbehaviorfeatures, |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
them.However,Internetdataisoftenvastandmassive,andABR
|                       |       |        |           |         |            |      |             |      | considering | that       | ABR algorithms |          | interact | with     | underly- |
| --------------------- | ----- | ------ | --------- | ------- | ---------- | ---- | ----------- | ---- | ----------- | ---------- | -------------- | -------- | -------- | -------- | -------- |
| algorithms            | adapt | to new | scenarios | by      | learning   | from | these       | net- |             |            |                |          |          |          |          |
|                       |       |        |           |         |            |      |             |      | ing TCP     | congestion | control,       | learning | these    | features | can      |
| work characteristics. |       |        | Because   | network | conditions |      | continually |      |             |            |                |          |          |          |          |
furtherreducerebufferingandoptimizeQoE.
| change over | time, | and | due to | different | user | preferences, |     | ABR |                |     |         |                 |     |                |     |
| ----------- | ----- | --- | ------ | --------- | ---- | ------------ | --- | --- | -------------- | --- | ------- | --------------- | --- | -------------- | --- |
|             |       |     |        |           |      |              |     |     | 4) We evaluate | QoE | metrics | in trace-driven |     | and real-world |     |
algorithmsmustbalancevariousQoEmetrics,suchasimprov-
|     |     |     |     |     |     |     |     |     | environments, | and | generalize | to 3G, | 4G, | 5G, WiFi, | syn- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | ------ | --- | --------- | ---- |
ingvideoqualityandreducingrebufferingtime.Unfortunately,
theticnetworks,anddifferentvideostreams(SectionV-C),
| learning | algorithms | often | perform |     | well on | the simple | training |     |            |     |            |              |     |       |         |
| -------- | ---------- | ----- | ------- | --- | ------- | ---------- | -------- | --- | ---------- | --- | ---------- | ------------ | --- | ----- | ------- |
|          |            |       |         |     |         |            |          |     | and deploy | the | algorithms | in streaming |     | media | systems |
andtestingdatasets,butrealinternetdatafeaturesarecomplex
(SectionVI).
andvariable,exhibitingheavy-tailedcharacteristics.Evenwith
| in situ learning, |     | adapting | to  | real-world | environments |     | quickly |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------- | --- | ---------- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
II. BACKGROUNDANDMOTIVATION
| proves to | be challenging. |     | Therefore, |     | learning | network | control |     |     |     |     |     |     |     |     |
| --------- | --------------- | --- | ---------- | --- | -------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
algorithmsfromtheseextensiveandrepresentativeInternetdata TheHTTP-basedABRalgorithmdynamicallyselectstheap-
andgeneralizingtonovelscenariosisbeyondthecapabilitiesof propriate bitrate for video segments by monitoring network
off-the-shelf methods [19], [27], [28]. This work will answer: bandwidth and player buffer status in real-time. It delivers
How to design a learning-based ABR algorithm that performs high-qualityvideowhennetworkconditionsaregoodandlow-
robustlyinthewildInternet. ers the quality during poorer conditions to prevent buffering,
ToaddressthesechallengesandmakeRLmorepractical,we thus optimizing the user QoE in Fig. 1. However, due to lim-
propose Offline RL-based ABR algorithm (Fortuna), which is ited network bandwidth, ABR algorithms may not always re-
capable of autonomously and efficiently learning ABR strate- questtheoptimalbitrate.ConsideringthediversityofthePuffer
gies in the face of the variability and heavy-tailed nature of dataset[13],wevisualizeitinFig.2,comprising10427streams,
heterogeneous network. Fortuna is primarily divided into two 1258stream-hours,andanalyzethedatacharacteristicsofthese
stages. In the offline phase, it leverages domain knowledge to real network users to illustrate why off-the-shelf ABR algo-
firstlearnfromexpertdata,andthencollectsrunsofRLdata.In rithmshavedifficultyinadaptingtotheseconditions.
theonlinephase,optimizationtakesplace,graduallyincreasing Case 1: Network conditions fluctuate over time, and long-
the complexity of the video stream through curriculum learn- duration video streams exhibit a heavy-tailed distribution. Ini-
ing [20], [29]. However, offline ABR strategies cannot adapt tialLowLoadPhase(0-5,000seconds),wherebandwidthfluc-
to new network conditions. To enhance the generalization of tuates at relatively low levels, mostly below 100 Mbps, with
Fortuna,weemploymeta-learningforcontinuousoptimization. frequent dips close to zero. This is followed by the Increased
Furthermore, ABR algorithms interact with TCP congestion FluctuationPhase(5,000-10,000seconds),duringwhichband-
controlmechanisms,suchascongestionwindow(CWND)and widthvariesbetween0and200Mbps,showingmorefrequent
round-triptime(RTT).Tobetterunderstandtheunderlyingnet- peaksandtroughs.Next,intheHighFluctuationPhase(10,000-
workbehaviorfeatures,weconsiderTCPcongestioncontrolto 20,000seconds),therangeofbandwidthfluctuationbroadens,
facilitatetheeffectivelearningofABRalgorithms.Tosuccess- often reaching up to 200 Mbps and occasionally exceeding
fully and efficiently develop high-quality ABR strategies, we 300Mbps.ThencomesthePeakPhase(around20,000-22,000
are driven to explore new data efficiency [30] approaches and seconds),wherebandwidthsurgestoitshighestlevels,exceed-
innovativeRLtechniques. ing400Mbpswithinashortperiod.Finally,intheDeclineand
Insummary,themaincontributionsofthispaperarethefol- Stabilization Phase (22,000-28,000 seconds), bandwidth grad-
lowing. ually decreases and stabilizes, with most values falling below
1) Weanalyzetheissuespresentinthecurrentheterogeneous 100 Mbps. These data usually contain samples from various
networkandproposeFortuna,amorepracticalofflinemeta scenarios,environments,orstates,whichcaneffectivelyreflect
RL-basedABRmethod. the diversity of data distributions. By training on diverse data,
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.

YIetal.:OPTIMIZINGADAPTIVEVIDEOSTREAMING:OFFLINERLANDMETA-LEARNINGINDIVERSENETWORKS 8187
Fig.2. Visualizenetworkfeatures,aswellasvideoqualityandbufferingtimeofexistingABRalgorithms,onthePufferdataset.
offlineRLenablesthemodeltolearnthefeaturesandpatterns anactionat(i.e.,chunkbitrateRn)accordingtoitspolicy.The
acrossdifferentdistributions,enhancingitsgeneralizationabil- videoclientthenreceivestheactionat andtransitionstoanew
ity[31]. state st+1 , providing the agent with a reward rt. The goal of
Case 2: The QoE of video users is influenced by the un- theABRagentistolearnapolicythatm(cid:2)aximizestheexpected
derlying TCP congestion control protocol [32], such as RTT. cumulative discounted reward value E[ ∞
t=0
γtrt]. The entire
We observe varying network throughputs, ranging from 0 to processfollowsaMarkovdecisionprocess(MDP),denotedby
250Mbps,withdifferentRTTvaluesacrossusers.Forexample, M=(S,A,O,P,R),whereSisthestatespace,Aistheaction
userswithathroughputof75MbpsexhibitawiderangeofRTT space,Oistheobservationspace,Pisthetransitionprobability
values,whilethosewiththroughputbetween25and50Mbpsof- function,andRistherewardfunction.
tenexperiencehighlatencyandabroaderrangeofRTTvalues. Rewardrt:Theenvironmentevaluatesdifferentactionsat,re-
These heterogeneous network characteristics significantly im- flectsthequalityofat,andimprovesthepolicyπθ.rtreflectsthe
pactABRalgorithmdecisions,affectingQoEoutcomes.Since qualityofdifferentbitrates,rebufferingtimeandvideoswitch-
RTT influences QoE, TCP congestion control algorithms like ingfrequency.WeadopttheQoEmetricprovidedbyMPC[5]
BBR [33] and CUBIC [34] adjust data sending rates to opti-
(cid:3)N (cid:3)
m
in
i
g
ze
ne
R
tw
TT
or
p
k
e
c
rf
o
o
n
r
d
m
it
a
io
n
n
ce
s
.
t
A
o
B
im
R
p
a
ro
lg
v
o
e
ri
v
th
id
m
eo
sm
str
u
e
s
a
t
m
ad
in
a
g
pt
q
t
u
o
a
c
li
h
ty
an
b
g
y
- QoE N = q(Rn)−μ
1
N
n=
−
1
1 |q(Rn+1 )−q(Rn)|
n=1
leveragingtheseunderlyingnetworkcharacteristics.
Case 3: Learning ABR strategies often leads to poor deci- (cid:3)N
sions when faced with unknown network conditions, resulting
−μ
2
Tn (1)
insuboptimalvideoqualityandincreasedrebufferingtime.We n=1
usethePufferdataset,withadurationof1000hoursandatime
A video consists of N chunks, q(.) represents video quality,
intervalof1s,wherethenetworkbandwidthrangesfrom0to
such as SSIM [35] or VMAF [36], where μ and μ are the
1 2
400 Mbps. We compared several ABR algorithms, including
non-negativeweightcoefficientscorrespondingtovideoquality
Pensieve, Fugu, Comyco, BOLA, and MPC, in how well they
switchingfrequencyandrebufferingtime.
adapttounseennetworkconditions.Duetotherandomnessof Meta-ABRTask:Inmeta-RL,tasksMaredrawnfromadis-
networkbandwidth,traditionalmethodslikePensievestruggle tribution p(M), representing the diversity of network condi-
toconvergeeffectively.Fugu,whichcombinesneuralnetwork
tions [15]. The meta-ABR algorithm aims to find a shared set
training with MPC predictions, also encounters challenges in
ofparametersθthatmaximizestheexpectedcumulativereward
managingunknownnetworkconditions.Fortunaisthemostop-
acrossalltasks:
timal among all ABR algorithms in improving video quality
(cid:3)n
(SSIM) and reducing stalling time. Our findings indicate that
existingmethodsstruggletorespondeffectivelytotheseunpre- θ ∗ =argm θ ax E π ψi (τ) [R(τ)],where ψi =fθ(M i).
i=1
dictablescenarios.
Insummary,itishighlyimportanttoefficientlylearnrobust Inthisformulation:
(cid:2)
ABRalgorithmsunderwildInternetconditionsandgeneralize ψi is the task-specific policy parameter derived from the
themtodiversenetworkconditions. meta-parameterθ,adaptingtotaski.
(cid:2)
fθ denotesthemeta-policyfunctionthatleveragesexperi-
enceacrosstaskstooptimizefutureperformance.
III. DEFINEOFFLINEMETAABRALGORITHM (cid:2) M irepresentstheMDPforeachtask,encodingitsunique
Offline-RLisconductingonlinelearningoftheoptimalpolicy networkenvironment.
π∗ frompriordataD (i.e.,off-policydata,expertdemos,prior The goal of meta-ABR is to train a meta-policy that
runsofRL).Attimet,theagentobservesthecurrentstatest(i.e., quickly adapts to unseen network conditions, leveraging
throughtputCt,thebuffersizeBt,chunkbitrateRn),andselects knowledge gained frompreviouslyencountered environments,
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore. Restrictions apply.

| 8188 |     |     |     |     | IEEETRANSACTIONSONMULTIMEDIA,VOL.27,2025 |     |     |     |
| ---- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- |
thereby optimizing the QoE objective across a variety of videoQoEobjective,MPCtypicallyperformsbetterthantradi-
tasks. tional methods that rely on fixed heuristics. Therefore, we use
Advantage-Weighted Regression (AWR): AWR is an offline theMPCalgorithmtocollectexpertdemonstrationdatainorder
RLmethodthatrefinesthepolicybasedonhistoricaldata[37]. to reduce the need for online interaction between RL and the
| Itsobjectivefunctionis: |     |     |     | videostreamingenvironment. |     |     |     |     |
| ----------------------- | --- | --- | --- | -------------------------- | --- | --- | --- | --- |
L AWR(θ,φ,D)=
B. HandlingUnboundedVideoStreamingSessionsWith
| (cid:4) |     |     |     | (cid:5) |     |     |     |     |
| ------- | --- | --- | --- | ------- | --- | --- | --- | --- |
CurriculumLearning
1
| E − | logπθ(a|s)exp(QD(s,a)−Vφ(s)) |     |     | (2) |     |     |     |     |
| --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
s,a∼D
Z(s) We will construct a strategy for gradually increasing video
streamlengthfromamathematicalperspectiveandcombineit
where: with the decaying process of environmental resets, observing
(cid:2)
QD(s,a)isthereturnfromthedatasetforactionainstate
|            |     |     |     | how these | two factors | work together | to optimize | the training |
| ---------- | --- | --- | --- | --------- | ----------- | ------------- | ----------- | ------------ |
| (cid:2) s. |     |     |     | process.  |             |               |             |              |
Vφ(s)isthevaluefunctionforthebehaviorpolicy.
(cid:2) Let the video stream length be denoted as Tk, where k rep-
| Z(s)>0 | is a normalization | function | dependent | on the |     |     |     |     |
| ------ | ------------------ | -------- | --------- | ------ | --- | --- | --- | --- |
resentsthetrainingstage.Startingfromtheinitialstagek =1,
states,scalingtheoveralllossterm. thevideostreamlengthgraduallyincreasesasthetrainingpro-
| The term QD(s,a)−Vφ(s) |     | represents | the advantage | of an |     |     |     |     |
| ---------------------- | --- | ---------- | ------------- | ----- | --- | --- | --- | --- |
gresses.
| actiona.ThepolicyobjectiveL |     | AWRcanbeseenasaweighted |     |     |     |     |     |     |
| --------------------------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
Wecandescribethegradualincreaseofvideostreamlength
| regression problem, | where | actions with higher | advantages | re- |     |     |     |     |
| ------------------- | ----- | ------------------- | ---------- | --- | --- | --- | --- | --- |
usingthefollowingmathematicalformula:
ceivegreaterweight.
·(k−1),T
|     |     |        |     |     | Tk =min(T | init +ΔT |     | max ) |
| --- | --- | ------ | --- | --- | --------- | -------- | --- | ----- |
|     | IV. | DESIGN |     |     |           |          |     |       |
Where: (cid:2)
Inthissection,basedonofflineRLtheory,wedescribehowto T istheinitialvideostreamlength.
|     |     |     |     | (cid:2) init |     |     |     |     |
| --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
ΔT istheincreaseinvideostreamlengthforeachstage.
| efficientlylearnarobustABRalgorithm.Wethenutilizemeta- |     |     |     | (cid:2) |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | ------- | --- | --- | --- | --- |
learningtolearnmeta-ABRpoliciestoadapttodifferentnetwork kisthecurrenttrainingstage(k =1,2,3,...).
(cid:2)
T isthemaximumvideostreamlength,representingthe
| conditions. |     |     |     | max |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
task’smaximumcomplexity.
Thisapproachensuresthatthevideostreamlengthincreases
A. AddressingDataEfficiencyIssuesinRL.
|     |     |     |     | gradually | and does not | exceed | the maximum | value T , pre- |
| --- | --- | --- | --- | --------- | ------------ | ------ | ----------- | -------------- |
max
Academia and industry are actively researching neural net- ventingthetaskfrombecomingtoocomplex.
work efficiency [31], [38], [39]. In traditional deep RL with Example:Supposethevideostreamlengthstartsat10seconds
real-timeonlineinteractionslikePensieve,itoftentakesaround (T init =10)duringtheearlystagesoftraining,withanincrease
50,000iterationsand4hourstoconverge[8].However,whenap- of5secondsateachstage(ΔT =5),andthemaximumvideo
plyingthistoreal-worldenvironments,likelearninginsitu[13], streamlengthis50seconds(T =50).Then,duringthefirst,
max
convergencecouldtakeupto2years.Thishighlightstheprac- second, and third stages of training, the video stream lengths
ticalchallengesofneuralnetworktraining,particularlyforreal- will be 10 seconds, 15 seconds, and 20 seconds, respectively.
worldapplications. Whentrainingreachesthemaximumlength(the9thstage),the
Inpractice,RL-basedABRalgorithmsneedtoquicklylearn videostreamlengthwillbe50seconds.
theoptimalpolicyπ∗andgeneralizeacrossvarioustypesofnet- To learn a robust ABR strategy effectively, the agent needs
workconditions,i.e.,learntheoptimalpolicyπ∗frompriordata
|     |     |     |     | to undergo | training | in “streaming” | scenarios | where the video |
| --- | --- | --- | --- | ---------- | -------- | -------------- | --------- | --------------- |
D =(si,ai,si+1 ,ri).Oneofthesimplestmethodsforapplying streaming session continuously arrive over time. Training in
RListousepriordataD,suchaspre-trainedpoliciesfromimita- “batch”scenarios,wherevideostreamingsessionsarrivesimul-
tionlearning(e.g.,Comyco[11]),andthenrefinethemthrough taneously at the beginning of an episode, leads to inefficient
RL [40], [41]. However, this approach has two limitations: strategies in a “streaming” environment, such as different ran-
(1) the prior data may not be optimal, and (2) fine-tuning the domseeds.However,trainingwithacontinuousflowofvideo
policy lacks data efficiency as it cannot make efficient use of streamarrivalspresentschallenges.Theagent’sinitialstrategy
priordataduringRL[37].Inreal-worldenvironment,dataeffi- ispoor,mainlybecausetheinitialparametersarerandom.Con-
ciencyisofparamountimportance.Therefore,wedemandthat sequently, during early training episodes, the agent struggles
the algorithm be capable of reusing any non-policy data (e.g., to process video stream as they arrive, resulting in a signifi-
off-policy data, expert demos, prior runs of RL) during online cantvideostreamqueuebuildup.Additionally,whentheagent’s
RLtoachievehighlydata-efficientfine-tuning. strategy is not optimal, video requests may experience delays,
In the early stages, we needed to learn from expert- resultinginaqueuebeforebeingservicedratherthanreceiving
demonstrateddataD.Thestate-of-the-artmethod,MPC[5],de-
immediatesatisfaction.
terminesvideobitratebysolvinganoptimizationproblemaimed In order to avoid spending a significant amount of train-
atmaximizingQoEbasedonthedynamicplaybackbuffer,con- ing time exploring actions that do not improve the policy in
sideringseveralfuturevideochunks.Bydirectlyoptimizingthe this scenario, we prematurely terminate the initial episodes so
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.

YIetal.:OPTIMIZINGADAPTIVEVIDEOSTREAMING:OFFLINERLANDMETA-LEARNINGINDIVERSENETWORKS 8189
istoobtainthemaximumcumulativerewardfromtheenviron-
ment.Therefore,therewardrtissetaccordingtotheparameters
oftheQoEmetric,reflectingtheindividualcomponentsofthe
QoEmetric.
Step4:Theactor’soutputbitrateposeschallenges,primarily
becausedifferentvideoscanbeencodedatvariousbitratelevels,
andduetovariablebitrateencoding,theirchunksizesmayalso
differ.Toaddressthisdiversity,thetypicalapproachwouldin-
volvetrainingamodelforeverypossiblecombinationofvideo
bitrates,whichisnotascalablesolution.
Outputmaskingisemployedaspartofthesolution.Foreach
|     |     |     |     |     |     |     | video,amask,representedasabinaryvector[m |     |     |     |     |     | ,m ,...,mk], |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- |
1 2
|     |     |     |     |     |     |     | is used to           | constrain                                  | the     | probability | distribution |            | of the    | output, |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | ------------------------------------------ | ------- | ----------- | ------------ | ---------- | --------- | ------- |
|     |     |     |     |     |     |     | including            | only the                                   | bitrate | levels      | that the     | video      | supports. | This    |
|     |     |     |     |     |     |     | mask, in conjunction |                                            | with    | softmax     | [43],        | determines | which     | bi-     |
|     |     |     |     |     |     |     | trates[i ,i          | ,...,ik]intheNNoutputarevalid.             |         |             |              |            |           |         |
|     |     |     |     |     |     |     | 1                    | 2                                          |         |             |              |            |           |         |
|     |     |     |     |     |     |     | Inner-Loop:          | Theinnerloopreferstoreal-timebitrateselec- |         |             |              |            |           |         |
Fig.3. ThepolicyarchitectureofFortunaisusedtogeneratetheABRalgo-
rithm,solidlinesshowthedataflowduringtheforwardpass,whiledashedlines tion adjustments based on the current network conditions and
representthegradientflowduringthebackwardpass,whichoccursonlyduring theexistingstrategy,aimingtooptimizetheshort-termuserex-
theadaptationphase.Theadvantageheadisnotinvolvedinthepolicyupdate perience. For ABR algorithms, the inner loop uses bandwidth
processoftheouterloop.
predictions,bufferstatus,andchunksizestoselectanappropri-
atebitratethatmaximizesQoEobjectives.
Thevaluefunctionloss,dependentonthemeta-trainingdata
that the agent can reset and quickly retry from an idle state. Dtr,representingthei-thbatchofofflinedata.IntheABRalgo-
| We gradually | increase |     | the length | of  | video streaming | sessions | i          |                |     |       |           |               |     |        |
| ------------ | -------- | --- | ---------- | --- | --------------- | -------- | ---------- | -------------- | --- | ----- | --------- | ------------- | --- | ------ |
|              |          |     |            |     |                 |          | rithm, the | value function |     | Vφ(s) | estimates | the long-term |     | return |
throughouttheentiretrainingprocess.Thus,initially,theagent
orvalueofastates.Inthisstep,thegoalistoupdateφbymini-
learnstoshortvideostreamingsessionssequences.AsitsABR
|          |           |     |        |             |         |            | mizingthevaluefunctionlossL |     |     |     | V,whichmakesVφ(s)acloser |     |     |     |
| -------- | --------- | --- | ------ | ----------- | ------- | ---------- | --------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- |
| strategy | improves, | we  | extend | the episode | length, | making the |                             |     |     |     |                          |     |     |     |
approximationtotheaction-valuefunctionQD(s,a).
| problem   | more   | challenging. | The         | concept | of gradually  | increas- |     |     |              |     |         |     |     |     |
| --------- | ------ | ------------ | ----------- | ------- | ------------- | -------- | --- | --- | ------------ | --- | ------- | --- | --- | --- |
| ing video | stream | sequence     | length—and, |         | consequently, | prob-    |     |     |              |     |         |     |     |     |
|           |        |              |             |         |               |          |     |     | (cid:6) ←φ−η | ∇   | L V(φ;D | tr  |     |     |
|           |        |              |             |         |               |          |     |     | φ            |     | φ       | )   |     | (3) |
lem complexity—during training realizes curriculum learning 1 i
forABR[29].
|     |     |     |     |     |     |     | whereL V(φ;D)=E |     | s,a∼D[(Vφ(s)−QD(s,a))2]andQD(s,a) |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------------------------------- | --- | --- | --- | --- | --- |
C. Learningmeta-ABRAlgorithm istheMonteCarloreturnfromstatestakingactionaobserved
inD.Byminimizingtheloss,weaimtoaccuratelypredictthe
Fortunaisanofflinemeta-RLABRalgorithmthatlearnsini-
expectedrewardforeachbitratechoiceinagivenstate.
tializationsφandθforavaluefunctionVφandmetapolicyπθ,
Toeffectivelylearnfeaturesfromthechangingnetworkcon-
respectively,enablingrapidadaptationtoanewnetworkcondi-
|     |     |     |     |     |     |     | ditions, our | policy | architecture |     | has two output |     | heads: | one for |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ------------ | --- | -------------- | --- | ------ | ------- |
tionencounteredatmeta-testtimeviagradientdescent.Fortuna
πθ(·|s),
|     |     |     |     |     |     |     | predicting | the action | given | the | state, | and | another | for |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ----- | --- | ------ | --- | ------- | --- |
mainlyconsistsofinnerloopsandouterloops[15],[42].Next,
|     |     |     |     |     |     |     | predicting | the advantage |     | given | both state | and action, | Aθ(s,a) |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | ----- | ---------- | ----------- | ------- | --- |
wewillprovideadetailedoverviewoftheimplementationpro-
[44].Thisdual-headdesignhelpsreducevarianceinthelearn-
cess.
ingprocess,leadingtomorestableandefficienttraining.Policy
FortunausestheRLActor-Critic(policyandvaluenetwork)
adaptationproceedsas:
approachinFig.3.Thetrainingprocessisasfollows:
| St e p 1 | : I n p u | t i s t h e | s ta t e | s t , w h | ic h i n c lu | d e s 7 v a r ia b l e | s ,            |     |       |                  |            |        |     |     |
| -------- | --------- | ----------- | -------- | --------- | ------------- | ---------------------- | -------------- | --- | ----- | ---------------- | ---------- | ------ | --- | --- |
|          |           |             |          |           |               |                        | θ (cid:6) ←θ−α | ∇ L | π(θ;φ | (cid:6) ,D tr ), | whereL π=L | AWR+λL |     |     |
nam e l y: th r o u g h tp u t C ,c h u n k d o w n lo a dt i m e d k ( R k) / C , n e x t 1 θ i ADV
|     |     | t   |     |     |     | k   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(4)
| chunk sizes | Rn+1 | , RTT, | and | the buffer | size | Bt, remaining |     |     |     |     |     |     |     |     |
| ----------- | ---- | ------ | --- | ---------- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
whereλistheweightofthenormalizationZ(s)oftheadvantage
| chunksN | andchunkbitrateRn. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Neuralnetworks:Thenumberofhiddenlayersis1,and128 function, designed to better adapt to different network condi-
tions.TheAWRlossisgivenin(2),andtheadvantageregression
convolutionkernelsandafullyconnectednetworkareusedfor
|                     |     |     |         |                 |     |                 | lossL | isgivenby: |     |         |     |     |     |         |
| ------------------- | --- | --- | ------- | --------------- | --- | --------------- | ----- | ---------- | --- | ------- | --- | --- | --- | ------- |
| feature extraction. |     | The | size of | the convolution |     | kernel is 4 and | ADV   |            |     |         |     |     |     |         |
| thestepsizeis1.     |     |     |         |                 |     |                 |       |            |     | (cid:6) |     |     |     | (cid:7) |
|                     |     |     |         |                 |     |                 |       | (cid:6)    |     |         |     |     |     | 2       |
Step2:Whenreceivingthestatest,theagentselectsthecor- L ADV(θ;φ ,D)=E s,a∼D Aθ(s,a)−QD(s,a)+Vφ(cid:6)(s)
i
| respondingactionatbasedonthemeta-policyπθ,andtheprob- |     |     |     |     |     |     |     |     |     |     |     |     |     | (5) |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
abilitydistributionisdefinedas:(st,at)→[0,1],(st,at)isthe
|     |     |     |     |     |     |     | This loss | function | aims | to optimize | the | advantage |     | function |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ---- | ----------- | --- | --------- | --- | -------- |
probabilitythattheactionatmaytakeinstatest. Aθ(s,a), ensuring that the policy selects bitrates that lead to
Step 3: After taking each action at, the environment feeds higherexpectedrewards.Byminimizingthedifferencebetween
backtherewardrtcorrespondingtoattotheagent,andthegoal Aθ(s,a), QD(s,a), and Vφ(cid:6)(s), the algorithm ensures that the
i
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.

8190 IEEETRANSACTIONSONMULTIMEDIA,VOL.27,2025
policyisconsistentwithboththevalueandaction-valuefunc- Algorithm1:Learningmeta-ABRpoliciesthroughoffline
tions.Thishelpsimprovethepolicy’sabilitytoadaptvideobi- RLwithgraduallyincreasingvideostreamlength
tratetovaryingnetworkconditions,suchasbandwidthfluctua- 1:Require:networkenvironments{M
i
};offlinedatasets
tions,toselecttheoptimalbitrate. D icontainingtrajectoriesτ:(st,at,rt)
Outer-Loop: The outer loop focuses on globally optimizing
2:Require:InitialvideostreamlengthT ,increment
init
the initial strategy across multiple different network environ-
ΔT,maximumstreamlengthT
ments (tasks) M, aiming to enhance the generalization ability max
3:Hyperparameters:Inner-looplearningratesα
1
ofthestrategyforunseennetworkfluctuations.
(policy),η (value);outer-looplearningratesα ,η ;
1 2 2
Fortheouterloopupdate,wesampleadistinctbatchofdata,
trainingiterationsk
meta-test Dts, to promote few-shot generalization instead of
i 4:Initializemeta-policyparametersθandvaluefunction
memorizingtheadaptationdata.
parametersφ
Themeta-learningforthevaluefunctionfollowstheMAML
5:forkiterationsdo
approachandemploysthesupervisedMonteCarloobjective: 6: foreachnetworkenvironmentM ido
m φ inE M i [L V(φ (cid:6) i ,D i ts )] 7: b S a a t m ch p e le sD di i s tr jo a in n t d m D e i t t s a- f t r r o a m ini D ng i andmeta-testdata
=m φ inE M i [L V(φ−η 1 ∇ φ L V(φ,D i tr ),D i ts )] (6) 8: T C k al = cul m at i e n v (T id in e i o t + str Δ ea T m · l ( e k ng − th 1 f ) o , r T t m h a e x ) currentstage:
This objective optimizes for a set of initial value function pa- 9: Adaptvaluefunction:φ(cid:6) ←φ−η 1 ∇ φ L V(φ;D i tr)
rameterssuchthatoneorafewinnergradientstepsleadtoan 10: Adaptpolicy:θ(cid:6) ←θ−α 1 ∇ θ L π(θ;φ(cid:6);D i tr),where
accuratevalueestimator. L π =L AWR+λL ADV
Unliketheinnerloop,weoptimizetheinitialpolicyparam- 11: endfor
etersintheouterloopusingastandardadvantage-weightedre- 12: Meta-update(cid:2)valuefunction:
gressionobjectivesinceexpressivenessconcernsmainlyapply φ←φ−η 2 i ∇ φ L V(φ(cid:6);D i ts)
totheinnerloopwithfewergradientsteps. 13: Meta-update(cid:2)policy:
m θ inE M i [L AWR(θ (cid:6) ,φ (cid:6) ,D i ts )] 14:en θ d ← for θ−α 2 i ∇ θ L AWR(θ(cid:6);φ(cid:6);D i ts)
=m θ inE M i [L AWR(θ−α 1 ∇ θ L π(θ,φ (cid:6) i ,D i tr ),φ 0 ,D i ts )] (7)
Algorithm 2: Generalizing meta-ABR policies across di-
whereL π isdefinedin(4)andL AWR isdefinedin(2). verseenvironments
Weight Transform Layers z: The standard fully connected 1:Input:TestnetworkenvironmentM j,offline
layerhastheoutput: experiencebufferD,meta-policyπθ,andmeta-value
y =σ(Wx+b), functionVφ
2:Hyperparameters:Learningratesα ,η ;numberof
whereW ∈Rd×distheweightmatrix,b∈Rdisthebiasvector, 1 1
adaptationstepsk
x∈Rdistheinputvector,andσistheactivationfunction.
3:Initializepolicyparametersθ =θandvaluefunction
Byintroducingalatentvectorz ∈Rc andaweighttransfor- 0
parametersφ =φ
mation matrix W
∈R(d2+d)×c,
dynamic weights and biases
0
wt 4:forkadaptationstepsdo
aregenerated: 5: Adaptvaluefunction:φt+1 ←φt −η 1 ∇ φ L V(φt;D)
w =W z, 6: Adaptpolicy:θt+1 ←θt −α 1 ∇ θ L π(θt;φt+1 ;D)
wt
7:endfor
where the first d2 components of w reshape into the weight
matrix W∗ ∈Rd×d, and the last d components form the bias
vectorb∗ ∈Rd:
In summary, the latent vector z enhances ABR algorithms
W ∗ =reshape(w[0:d2]), b ∗ =w[d2 :(d2+d)]. by enabling dynamic weight and bias generation, supporting
higher-rankweightupdates,andimprovingadaptabilitytovary-
Theforwardpassbecomes:
ing network conditions, leading to more flexible and scalable
y =σ(W ∗ x+b ∗ ). performanceoptimizationinvideostreaming.Moremathemat-
icalproofscanbefoundin[45].
Unlikefixedweightsinstandardlayers,dynamicgenerationof Algorithm1and2demonstratehowtolearnmeta-ABRpoli-
W∗ and b∗ allows more flexible updates. Traditional gradient cies through offline RL and generalize them to various video
descentupdatesresultinrank-1changes,whereaswiththelatent streamingenvironments.
vectorz,therankofweightupdatesisboundedby:
rank(ΔW ∗ )≤min(d,c), V. EXPERIMENTSANDANALYSIS
allowing higher-rank transformations and richer adaptation In this section, we experimentally evaluate Fortuna on dif-
strategies. ferentnetworktracesandQoEmetrics.Further,weanalyzethe
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore. Restrictions apply.

YIetal.:OPTIMIZINGADAPTIVEVIDEOSTREAMING:OFFLINERLANDMETA-LEARNINGINDIVERSENETWORKS 8191
performanceofFortunaonthe5Gnetwork,aswellasthetrain- network.However,theoriginalPensievestruggledwithconver-
ingsituation. gence due to the variability in network conditions when using
theA3Calgorithm.Therefore,weemployedvariancereduction
techniques[52]inthetrainingprocesstodevelopamoreeffec-
A. Implementation
tiveABRalgorithm.
NVIDIARTXA6000GPUandaCPUwith128cores,128G RMPC: makes decisions about video bitrate by tackling a
RAM,64-bitUbuntu20.04,andMacOSoperatingsystemwere problem that aims to maximize QoE for several upcoming
selected as the experimental platform, and development tools chunks. By focusing directly on improving QoE, MPC often
such as Python3.5, Torch1.6, Apache2, Google Chrome, and performsbetterthanmethodsthatrelyonfixedrules[5].
FFmpeg.WeuseMahimahi[46]tosimulatenetworkconditions, Comyco[11]:TheimitationMPCalgorithm[5]usesneural
withRTTrangingfrom0to80ms,basedoncollectednetwork networkstogeneratetheABRalgorithm.
tracesbetweentheclientandserver. Fugu[13]:Traintheneuralnetworkusingsupervisedlearn-
TheQoEmetricparametersof(1)areset:N is8,μ is4.3, ing,andthenuseMPC[5]forvideobitratedecision-making.
1
andμ is1.Duringthetrainingprocess,thesizeofeachepoch CDFs:Cumulativedistributionfunctions(CDFs)areusedto
2
is 100, γ = 0.99, Relu activation function [47] and the Adam evaluatetheoveralldistributionofQoEfordifferentABRalgo-
optimizer[48]areused.Duringthewholeexperiment,according rithms. The higher the CDF to the right, the higher the cumu-
to the change of the loss function, the learning rates for the lative probability and QoE. As shown in Fig. 4, Fortuna has a
inner and outer loops are 0.001 and 0.0001, respectively, and higherQoEvaluethantheexistingABRalgorithms,duetothe
the reward value fed back to the agent by the environment is characteristicsoftheautonomouslearningrobustABRpolicies,
theQoEmetricvalue. improvementrangeof8.5%-31.9%.ThereasonisthatFortuna
Network Traces: To evaluate Fortuna and existing ABR al- can better learn a wide range of network features, resulting in
gorithmsondifferentnetworks,weuseFCC[49],HSDPA[50] stronggeneralizationonunseennetworks.FuguandComyco’s
andBelgium/4G[51]publicnetworktraces,andthedatasetfea- inabilitytoadaptivelychangestrategiesandlong-termdecision
tures are as follows. The FCC dataset contains 1 million net- problems using imitative learning. Additionly, it is essentially
work traces with an average network throughput of 2100 sec- solvingtheRMPCproblems[5].However,RMPCestimatesthe
onds each trace, granularity of 5 s, and a throughput range of network bandwidth too conservatively use model control. For
0-111Mbit/s, generated on trains, buses, cars etc. The HSDPA example,whenthenetworkthroughputbecomeslow,itshould
dataset : the granularity of user generation in subways, trams, makefulluseoftheplaybackbufferandrequestalowbitrateto
trains,busesandferriesis1s,thenumberoftracesis86,andthe improveQoE,butRMPCleadstoinsufficientbufferutilization;
throughput range is 0-3Mbit/s. Belgium/4G dataset: generated similarly, BOLA only considers the buffer usage. As shown,
in static, pedestrian, car, bus, and train movement modes etc., thesesimplefixedheuristicsarenotapplicabletocomplexnet-
granularityof1s,5hoursintotal,40traces,throughputrange workthroughput.Additionally,Pensievecannotadaptivelylearn
of0-111Mbit/s. networkcharacteristics,resultingininaccurate predictions un-
We used the Puffer dataset [13], which in 2020 had over dercertainnetworkconditions.
63,508videousersandstreamedatotalof38.6yearsofvideo QoE breakdown: To better understand the performance of
content in that year. Now, in 2024, the number of video users Fortuna,wecomparetheindividualcomponentsofQoEmetric.
andstreamshasgrownevenfurther.Networkbandwidthranges Fig.5showsthevideobitrate,rebufferingtimeandsmoothing
from 0 to 500 Mbps, with an interval of 1 s. These networks penalty, i.e., the components of QoE metric. Experimental re-
displayvariablecharacteristicswithheavy-taileddistributions. sultsareevaluatedonFCC,Belgium/4G,andHSDPAdatasets.
Forthisstudy,weselected4differentdatasets.Weused80%of Asshown,Fortunaisabletobetterlimitrebufferingthrough
thedatafortrainingand20%astestdata. different networks to achieve higher QoE values. rebuffering
timeisreducedby4.6%-14.2%onFCC,Belgium/4G,andHS-
DPAdatasetsbybuildingenoughbufferstohandlesuddennet-
B. Evaluation
workfluctuations.Inaddition,althoughFortunacannotoutper-
Networkdatasets:FCC,HSDPA,andBelgium/4G;video:di- formexistingsolutionsineveryQoEmetric.Instead,itisableto
vided into 48 video chunks, each chunk has approximately 4 maximizeQoEbyoptimizingeverymetric.Forexample,when
seconds,thetotaldurationis193seconds;H.264/MPEG-4en- networkbandwidthisinsufficient,Fortunausesalowbitrateto
coding:{300,750,1200,1850,2850,4300}kbps;videoplayer: compensateforthelowbandwidthandreducevideostalling.
Google Chrome (built-in DASH.js), playback buffer capacity Video user preferences: This section provides a comparison
is set to 60 seconds, all ABR algorithms run in dash.js; video ofthreecommonQoEmodels,highlightingtheirkeycharacter-
server:Apache2,videoisdeployedontheserver. istics.
ABRalgorithms:WecompareFortunawithstate-of-artABR 1) Linear QoE: Advantages: Simple and intuitive, suitable
algorithms. forscenariosprioritizinghigherbitrates.Limitations:Ig-
BOLA[3]:optimizingbufferoccupancyusingLyapunoval- nores diminishing returns of quality perception and is
gorithm. Since the playback buffer is relatively stable, it can sensitivetobitratefluctuations.Application:Suitablefor
effectivelyimproveQoE. high-bandwidthvideostreamingenvironments.
Pensieve [8]: ABR algorithm based on deep reinforcement 2) Logarithmic QoE: QoE models user perception with
learning (DRL), generating ABR algorithm by training neural diminishing returns using q(R)=log(R/R ).
min
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore. Restrictions apply.

| 8192 |     |     |     |     |     |     |     | IEEETRANSACTIONSONMULTIMEDIA,VOL.27,2025 |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- |
Fig.4. ComparetheQoEmetricsofFortunaandexistingABRalgorithmsonFCC,HSDPA/3G,andBelgium/4Gnetworks.Examinethedistributionofaverage
QoEvaluesforeachABRalgorithm.
Fig.5. ComparingtheQoEmetricindividualcompomentsofFortunaandexistingABRalgorithmsonFCC,HSDPA,andBelgium/4Gnetworks.Errorbarsare
drawntorepresentthemeanvaluewithamarginofonestandarddeviation.
Fig.6. ComparisonofFortunawithexistingABRalgorithmsonFCCandHSDPAnetworks.QoEmetricsareconsideredaslistedinTableI,withresults
normalizedagainsttheperformanceofFortuna.Errorbarsrepresent±onestandarddeviation.
| Advantages: |     | Reflects | realistic | user | perception | and |     |     | TABLEI |     |
| ----------- | --- | -------- | --------- | ---- | ---------- | --- | --- | --- | ------ | --- |
QOEMODELSANDTHEIRCORRESPONDINGPARAMETERS
balancesqualitywithsmoothness.Limitations:Requires
| careful | selection | of R | ; more | complex | than | linear |     |     |     |     |
| ------- | --------- | ---- | ------ | ------- | ---- | ------ | --- | --- | --- | --- |
min
QoE.Application:Idealforadaptivebitratestreamingin
constrainedbandwidthconditions.
| 3) High-Definition |              | QoE:       | Uses predefined |                   | quality | levels |     |     |     |     |
| ------------------ | ------------ | ---------- | --------------- | ----------------- | ------- | ------ | --- | --- | --- | --- |
| corresponding      |              | to bitrate | ranges.         | Advantages:       |         | Simple |     |     |     |     |
| computations       |              | by mapping | bitrates        | to fixed          | quality | lev-   |     |     |     |     |
| els.               | Limitations: | Quality    | changes         | are discontinuous |         | and    |     |     |     |     |
threshold-dependent.Application:Suitableforvideoap-
(cid:2)
plications with standard resolution transitions, such as ForQoE ,Fortunaminimizesrebufferingriskbyprior-
log
StandardDefinition(SD),HighDefinition(HD),orUltra- itizing bitrate stability while avoiding unnecessary high-
| HighDefinition(UHD). |     |     |     |     |     |     | bitratejumps. |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- |
(cid:2)
| The | experimental | results | are | shown in | Fig. | 6, For- |         |                       |                   |          |
| --- | ------------ | ------- | --- | -------- | ---- | ------- | ------- | --------------------- | ----------------- | -------- |
|     |              |         |     |          |      |         | For QoE | lin , it aggressively | increases bitrate | to maxi- |
tuna leverages offline meta-learning to pre-train adaptive mize user-perceived quality without sacrificing playback
ABR strategies tailored to various QoE objectives. Un- smoothness.
(cid:2)
like traditional ABR algorithms with fixed control laws or In QoE optimization, Fortuna employs foresight to
hd
Pensieve’s online learning approach, Fortuna’s pre-trained rapidlybuildbufferwithlowbitratesandswitchesdirectly
| model can | rapidly | adapt | to QoE | , QoE | , and | QoE |     |     |     |     |
| --------- | ------- | ----- | ------ | ----- | ----- | --- | --- | --- | --- | --- |
log lin hd to HD quality once buffer conditions are favorable, all
| scenarios: |     |     |     |     |     |     | withoutonlinetuning. |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- |
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.

YIetal.:OPTIMIZINGADAPTIVEVIDEOSTREAMING:OFFLINERLANDMETA-LEARNINGINDIVERSENETWORKS 8193
However, Fugu [13] (supervised learning) cannot be adapted
to different networks, as it requires specific data that cannot
be adapted to new networks, and BOLA fail to achieve good
performanceusingsimplefixedheuristics.Furthermore,RMPC
algorithmperformspoorlyon5Gnetworksduetooverlycon-
servativepredictions.However,intheseheterogeneousnetwork
data,theenvironmentismorecomplexandrequiresbetterABR
decisions.Incontrast,RLcanadaptivelyselecttheoptimalbi-
tratesbasedonthenetworkscenario.Theseexperimentsshow
that Fortuna can reduce stall time and maximize QoE even in
the case of high and fluctuating network traces, despite these
networkshaveneverencountered.
Fig.7. Theoverallprobabilitydistributionof4Gand5Gnetworktraces.
Training with synthetic dataset: The training dataset has a
significantimpactontheperformanceofRL-basedalgorithms
Byeliminatingonlineexplorationandrelyingonpre-trained
and may hinder the optimal ABR strategy for RL learning. In
policies,Fortunaconsistentlydelivershighperformanceacross
part, we take Fortuna to the extreme and train it purely using
changingconditions,surpassingtheadaptabilityandefficiency
syntheticnetworksandgeneralizeittotherealnetwork.
ofPensieve.
The simulated dataset utilized in the study encompasses a
diverserangeofnetworkbandwidths,withtheaveragethrough-
C. Generalization
put spanning from 0.2 Mbps to 4.3 Mbps, which aligns with
In Section V-B, Fortuna is tested using common network thetrainingvideobitrates(suchasH.264encodingat300kbps,
traces,whichhaverelativelyshortdurations.Inpractice,how- 750 kbps, 4300 kbps, etc.). The dataset’s transitions between
ever,Fortunamayencounternewnetworkbandwidths,bitrates statesweregeneratedusingMarkovmodeling,andtheresulting
and require different optimal ABR strategies. To evaluate the bandwidthvaluesfollowaGaussiandistributionwithagranu-
generalization ability of Fortuna to the new network, we con- larityof1sandauniformvariancerangingfrom0.05to0.5[8].
duct2setsofexperiments.First,Fortunaisevaluatedonthereal We find that Fortuna performs better on each CDF trajectory
5Gnetworktraces,andanalysethedifferenceswith4Gnetwork. comparedtoGenet[19]inFig.9,averageQoEvalueincreased
Second, we take the generalisation of Fortuna to the extreme, by12.5%. The advantage of Fortuna lies in its ability to opti-
i.e.trainingpurelywithsyntheticnetworksandgeneralisingto mizebasedonacomprehensivesetofhistoricaldataandcom-
realBelgium/4GandcomparingwithGenet[19]. plexnetworkenvironments.Incontrast,ABRalgorithmsgener-
5G and 4G network traces: To analyze the distribution of atedthroughcurriculumlearningmightfacelimitationsdueto
5G network versus 4G network, we performed network traces constraintsinthedataandtrainingstrategiesusedduringtheir
analysisusingtheCDFdistributionmap.AsshowninFig.7,5G development.
networkisabletosupporthighernetworkbandwidthintherange Multiple videos: To evaluate Fortuna’s ability to gener-
of 0-1800 Mbps, and 4G is 0-300 Mbps. Second, 5G network alize across varying video properties, we trained a sin-
arecapableofsupportinghighnetwork,whichmeansweneed gle ABR model using 1,000 synthetic videos with diverse
correspondingbitratestomatch. characteristics. Each video had a random number of bi-
Different from the previous bitrate setting (e.g., 2.85 Mbps, trate options, ranging from 3 to 10, with values chosen
4.3Mbpsthatcanonlysupport3Gand4Gnetwork).However, from{200,300,450,750,1200,1850,2350,2850,3500,4300}
5Gnetworks[53](i.e.,including4Gand5G,thereare1754G kbps.Videosweresegmentedintoarandomnumberofchunks,
and 121 5G network traces with a granularity of 1 s, 2 types: between20and100,andchunksizeswerevariedbyapplying
drivingandwalking)cansupporthigherbitratevideos,inorder Gaussiannoisetoastandard4-secondchunkduration.Thisap-
tomatchthecorrespondingnetworkthroughputwiththevideo proachensuredabroadrangeofvideoproperties,includingbi-
bitrate, to prevent high throughput from always meeting high trateoptions,chunkcount,chunksizes,andoverallduration,to
andlowbitrates.Inspiredbyliterature[54],experimentbitrate rigorouslytestthemodel’sadaptabilityandperformanceacross
settings,namely:(20,40,60,80,110,160)Mbps,bitratemap differentscenarios.
reward=[1, 2, 3, 12, 15, 20], (more detail in [55]), total video As shown in Fig. 10, the results demonstrated that the gen-
chunksis157,rebuf-penaltyis160,smooth-penaltyis1.Wild eralizedABRalgorithmachievednearlyidenticalperformance
fluctuationscanbringgreatchallengestotheABRalgorithms, comparedtoamodelexclusivelytrainedonareferencevideo,
howtobalancecomponentsofthevideobitrateandthestalltime, ThegapinQoEvaluesis2.8%.Thisfindingsuggeststhatour
therebytheABRdecisionshouldbeforward-lookingenoughto method’sserverconfigurationcouldeffectivelyelevatestream-
maximize QoE objectives and minimize stall time as much as ing quality across a spectrum of videos, employing a concise
possible. selectionofABRalgorithms.
AsshowninFig.8,Fortunacanachievebetterperformance
D. ComparingState-of-The-ArtRLAlgorithms
on4Gand5Gnetworks,thestalltimeisreducedby4.6%-12.2%
and 0.5%-3.1% respectively. As shown, fortuna and offline- To compare the training efficiency of existing RL algo-
Fortunacanachievebetterperformanceon4Gand5Gnetworks. rithms,wecompareseveralABRalgorithms,i.e.,Pensieve[8],
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore. Restrictions apply.

8194 IEEETRANSACTIONSONMULTIMEDIA,VOL.27,2025
Fig.8. ComparetheaveragebitrateandrebufferingtimeofFortunawithexistingABRalgorithms,using95%confidenceintervals.
duringtheexperimentalprocedures.AsshowninFig.11(a),the
originalPensievewastrainedusingA3C,duetotherandomna-
tureofnetworkconditions,andthefluctuationswereverydras-
tic,thusweusedVariancereductiontooptimizetrainingtheper-
formancemorestable.PEARL,acontext-drivenmeta-learning
approach,tendstometa-overfitting,whichleadstosuboptimal
performanceinunseennetworkconditions.Contrastingly,For-
tunaleveragesofflinedatatorapidlylearnmeta-ABRpolicies,
resultinginanimprovementofover6.6%–20.1%theprevious
performance.
Additionally,wealsocomparedFortunawithonlinemeta-RL
methods,usingPPOtooptimizetheABRalgorithm,asshownin
Fig.9. ComparingtheQoEmetricsofFortunaandGenetABRalgorithmson
Fig.12.WefoundthatFortunacaneffectivelyutilizeofflinedata
Belgium/4Gdataset.
toconvergequickly,achievinganaveragerewardimprovement
of 9%. In contrast, Meta-PPO (However, the official code has
not been released, and we have done our best to implement
the algorithm according to the pseudocode description in the
paper.) [60] converges more slowly due to the need for real-
timeinteractionwiththeABRenvironment.Althoughtheclip
function in the PPO algorithm mitigates policy fluctuations, it
remainsrelativelystable.
Curriculum Learning: In this part, we utilize Curriculum
Learning to gradually increase the complexity of the video
stream in order to quickly adapt the bitrate to new network
conditions.Wecomparedthetrainingstepsandtimeasshown
in Fig. 11(b) and (c), it can improve performance by more
Fig.10. ComparingABRalgorithmstrainedonadiversesetofvideoswith
thosespecificallytrainedonthetestvideoundervaryingnetworkconditions. than 7.5%-4×, the average QoE can be improved by 3.7%.
Specifically, it is divided into two steps. First, Reset Envi-
Variancereduction[52],Jade,anRL-basedABRalgorithmwith ronment: A higher reset probability in the initial stages al-
humanfeedback(learningtheABRalgorithmusingDuel-PPO lows the agent to explore different strategies. Gradually re-
and adaptive entropy RL techniques [56], [57]), PEARL [58], ducing this probability helps stabilize learning and focus on
[59],acontextualizedmeta-RLapproach(i.e.,recentlyusedfor long-termdecision-making.Second,GradualIncreaseofVideo
meta-RLtoachievebetterABRpoliciesperformance[18]).Ten- Stream Length: The core idea is to gradually increase task
sorFlowTensorBoardwasusedtomonitorthetrainingprocess complexity. The agent transitions from handling simple, short
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore. Restrictions apply.

YIetal.:OPTIMIZINGADAPTIVEVIDEOSTREAMING:OFFLINERLANDMETA-LEARNINGINDIVERSENETWORKS 8195
Fig.11. Comparisonoftrainingepochsandtrainingtimewithandwithoutcurriculumlearningbyincreasingthecomplexityofvideostreaming,i.e.,fromshort
videostreamstolongvideostreams.
Fig.13. ComparinghowunderlyingTCPnetworkcharacteristicsaffectQoE
Fig.12. ThecomparisonofFortunawiththeexistingstate-of-the-artmeta- intheBelgiumnetwork.
ABRalgorithm,Meta-PPOABR[60].
known as TCP slow start restart [61]. Slow start, in turn, hin-
ders the video player from fully utilizing the available band-
video streams to more complex, longer video streams, en-
width,especiallyforsmallchunksizes(lowbitrates).Thisbe-
abling it to better cope with fluctuating network environ-
havior makes simulation challenging as it fundamentally links
ments and ensuring high-quality video streams under varying
network throughput to the employed ABR algorithm. For in-
conditions.
stance, strategies that rapidly fill the buffer will experience
more instances of slow start, consequently reducing network
utilization.
E. DeepDive
Additionally,intheTCPcongestioncontrolprocess,weneed
In this section, we explore microbenchmarks tailored to tocontrolnetworkbandwidthbasedonqueuedelay,whichin-
deepen our comprehension of Fortuna. Additionally, these volves subtracting the minimum RTT observed from the cur-
benchmarksshedlightonpracticalconcernsthatemergewhen rentRTTandadjustingCWND(congestionwindow)basedon
implementing ABR algorithms generated through RL, such as packetbehavior.Thiselementplaysavitalroleinensuringhigh
the influence of TCP congestion control and the diverse video throughputandminimallatency.Therefore,whennetworkcon-
streamingsessions. gestionoccurs,weshouldadjustthevideobitratebasedonTCP
TCPcongestioncontrol:Inrealinternetconditions,thevideo congestioncontroltoprovideabetteruserexperience.Inother
stream interacts with TCP congestion control. Simulated en- words,bydynamicallymodifyingthevideobitrateinresponseto
vironments often fail to accurately replicate real network con- theTCPcongestionwindowandqueuedelay,wecanmaintain
gestion control. Therefore, we take into consideration under- an optimal balance between throughput and latency, ensuring
lying TCP network characteristics. These abundant data in- smoothvideostreamingeveninfluctuatingnetworkconditions.
sights can be beneficial for learning robust ABR algorithms Tovalidatethisbehavior,weconducted4setsofexperiments,
acrossvariousnetworkenvironments.Specifically,videoplay- onesolelyconsideringnetworkbandwidthforselectingthebi-
ers may not immediately request future video chunks after trate,whiletheothertookTCPcongestioncontrolintoaccount.
completing the download of a video chunk, for instance, due AsshowninFig.13,wefoundthatsolelyconsideringnetwork
to a full playback buffer. This delay can trigger the under- bandwidthdoesnotaccuratelysimulaterealnetworkconditions,
lying TCP connection to enter slow start mode, a behavior whereashavingTCPcontrolinformationalwaysperformswell.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore. Restrictions apply.

8196 IEEETRANSACTIONSONMULTIMEDIA,VOL.27,2025
Fig.14. Long-durationvideostreamingsessions,i.e.,varyingnetworkconditionsanddifferentuservideostreams.Theaveragevaluesforvideoqualityand
bufferingareshown,witherrorbarsspanning±onestandarddeviationfromtheaverage.
When considering RTT, CWND, and Queue delay, QoE can algorithms face challenges in adapting to new network condi-
improve by 1.2-9.4%. This suggests that in a real network en- tions. Furthermore, Fortuna learns the ABR algorithm perfor-
vironment, we cannot simply rely on network bandwidth for mancesuboptimallyfromofflinedatasets,asofflinedatasetsare
evaluation,butneedtoincorporateTCPcongestioncontrolfor notalwaysoptimal.Incontrast,Fortuna,whichlearnsfromdi-
a better understanding of the ABR algorithm. These network versedatasets,suchasthosefromRLandexpertdemonstrations,
behavioral characteristics contribute to a better understanding exhibitsbetterperformance.
andlearningofABRalgorithms.
VI. REAL-WORLDDEPLOYMENTANDEVALUATION
Long-duration video streaming sessions: To gain a deeper
insightintoFortuna’s performance indiverse real-worldvideo In this section, we describe the specific deployment of For-
streaming networks, it’s important to consider that these net- tunainstreamingsystemsandevaluateiton5G,4G,andWiFi
works exhibit heavy-tailedness and TCP-related characteris- networks.
tics, we utilize SSIM for video quality assessment. The video In Section V-B, we conducted experiments using a simu-
undergoes de-interlacing using ffmpeg to generate a “canoni- lation platform to illustrate the generalization of the Fortuna
cal”1080p60or720p60sourcesuitableforcompression.Each algorithm in real-world streaming media systems. In this sec-
video chunk is encoded into ten different H.264 versions us- tion, we deploy Fortuna in the real world and conduct three
ingthelibx264encoderinveryfastmode.Theseencodingsen- setsofexperiments.Duringtheseexperiments,thevideoclient
compass a range of options, from 240p60 video with a con- was running on a MacBook Pro laptop, accessing the video
stant rate factor (CRF) of 26 (approximately 200 kbps) to server running on Ubuntu 20.04 through the HTTP proto-
1080p60videowithaCRFof20(about5,500kbps).Thisap- col. These algorithms were deployed on dash.js, and the ex-
proach provides a spectrum of quality and bitrate choices for periment was repeated several times. Video clients requested
the video stream, catering to diverse network conditions and the bitrate from an Apache2 server, which first went through
devices. the ABR algorithms before sending a signal to request video
AsshowninFig.14,wefoundthatthesimpleBuffer-Based from the server. Due to the round-trip delay between the
ABR (BBA) algorithm [62] can achieve better performance, ABR algorithms and the video server, we calculated the av-
while the ABR algorithm generated purely through RL train- erage round-trip delay under 5G, 4G, and WiFi network con-
ing,knownasPensieve,performspoorly.Meanwhile,wehave ditions, which were 4.21 ms, 70.32 ms, and 14.22 ms, re-
observed that meta-RL does not consistently achieve optimal spectively. During the experiment, Fortuna was compared
performanceduetotheneedforadaptationacrossawiderange with Pensieve, BOLA, and MPC, and the collected QoE
of video stream conditions. In real-world scenarios with vary- datasetwasnormalized.Theexperimentalresultsareshownin
inguserpreferences,BBA,whichreliesonfewerassumptions Fig.15.
andrequestsvideosbasedonbufferoccupancy,closelyapprox- Fig.15showsthattheQoEunder5GandWiFinetworkcon-
imatestheactualvideoplaybackprocess.MPCpredictsbitrates ditions is generally higher than that under 4G networks. This
basedonpastnetworkbandwidth. However, inarealenviron- is because 5G and WiFi networks have relatively high band-
ment, these network characteristics are complex and variable, widths, which can support higher bitrates and lower latency,
influencedbyfactorssuchasTCPandvaryinguserpreferences, allowingtheABRalgorithmstorequesthighbitratesmoresta-
makingadaptationtorealnetworkconditionsdifficult.Fuguex- bly.Atthesametime,wefoundthattheQoEofvariousABR
hibitsweakergeneralizationinunknownnetworkconditionsus- algorithms on 5G networks is more stable. Compared to WiFi
ingsupervisedlearning,whereasFortunaconsistentlyperforms networks, fluctuations in network bandwidth can cause ABR
wellintheseunknownnetworksanduserpreferences.Bylearn- algorithms to fail to continuously request high bitrates. Un-
ing these features and underlying TCP controls, it can better der 5G, 4G, and WiFi network conditions, Fortuna improved
understandthebehavioralcharacteristicsofthenetwork.Inaddi- QoE values by 2.9%–5.1%, 5.2%–12.5%, and 2.6%–11.2%,
tion,wealsofoundthatoff-the-shelfmeta-learning-basedABR respectively. These experiments show that Fortuna, generated
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore. Restrictions apply.

YIetal.:OPTIMIZINGADAPTIVEVIDEOSTREAMING:OFFLINERLANDMETA-LEARNINGINDIVERSENETWORKS 8197
|     |     |     |     |     |     | [6] A. Lekharu, | S. Kumar, | A.  | Sur, and A. | Sarkar, | “A QoE | aware LSTM |
| --- | --- | --- | --- | --- | --- | --------------- | --------- | --- | ----------- | ------- | ------ | ---------- |
basedbit-ratepredictionmodelforDASHvideo,”inProc.10thInt.Conf.
Commun.Syst.Netw.(COMSNETS),2018,pp.392–395.
[7] N.Kanetal.,“Uncertainty-awarerobustadaptivevideostreamingwith
|     |     |     |     |     |     |          |        |             |                  |     |           | Proc. 31st |
| --- | --- | --- | --- | --- | --- | -------- | ------ | ----------- | ---------------- | --- | --------- | ---------- |
|     |     |     |     |     |     | bayesian | neural | network and | model predictive |     | control,” | in         |
ACMWorkshopNetw.OperatingSyst.SupportDigit.AudioVideo,2021,
pp.17–24.
[8] H.Mao,R.Netravali,andM.Alizadeh,“Neuraladaptivevideostreaming
withpensieve,”inProc.Conf.ACMSpecialInt.GroupDataCommun.
(SIGCOMM),2017,pp.197–210.
|     |     |     |     |     |     | [9] T. Huang,R.-X. |     | Zhang,andL.Sun, | “Zwei: | Aself-play |     | reinforcement |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | --------------- | ------ | ---------- | --- | ------------- |
learningframeworkforvideotransmissionservices,”IEEETrans.Multi-
media,vol.24,pp.1350–1365,2021.
Fig.15. ComparingtheQoEmetricofFortunaandexistingABRalgorithms
|     |     |     |     |     |     | [10] A. Bentaleb, | M.  | N. Akcay, | M. Lim, | A. C. Begen, | and | R. Zimmer- |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | --------- | ------- | ------------ | --- | ---------- |
on5G,4GandWiFinetworkconditions.Inthebarchart,theaveragesarelisted, mann,“BoB:Bandwidthpredictionforreal-timecommunicationsusing
andtheerrorbarsspan±onestandarddeviationfromtheaverage.
heuristicandreinforcementlearning,”IEEETrans.Multimedia,vol.25,
pp.6930–6945,2022.
|             |                |              |     |            |        | [11] T.Huangetal.,“Quality-awareneuraladaptivevideostreamingwithlife- |     |     |     |     |     |     |
| ----------- | -------------- | ------------ | --- | ---------- | ------ | --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| by training | in a simulated | environment, | can | generalize | and be |                                                                       |     |     |     |     |     |     |
longimitationlearning,”IEEEJ.Sel.AreasCommun.,vol.38,no.10,
usedinreal-worldstreamingmedianetworks.Itcanalsomax- pp.2324–2342,Oct.2020.
|     |     |     |     |     |     | [12] W. Li | et al., “An | apprenticeship | learning | approach | for | adaptive video |
| --- | --- | --- | --- | --- | --- | ---------- | ----------- | -------------- | -------- | -------- | --- | -------------- |
imizeQoEvaluesunderdifferentconditionsandimproveuser
streamingbasedonchunkqualityanduserpreference,”IEEETrans.Mul-
experience.
timedia,vol.25,pp.2488–2502,2022.
|     |     |     |     |     |     | [13] F. Y. | Yan et al., | “Learning | in situ: A | randomized | experiment | in video |
| --- | --- | --- | --- | --- | --- | ---------- | ----------- | --------- | ---------- | ---------- | ---------- | -------- |
streaming,”inProc.17thUSENIXSymp.NetworkedSyst.Des.Implemen-
|     | VII. | CONCLUTION |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tation,2020,pp.495–511.
|              |          |         |                  |     |          | [14] H.Maoetal.,“Real-worldvideoadaptationwithreinforcementlearning,” |     |     |     |     |     |     |
| ------------ | -------- | ------- | ---------------- | --- | -------- | --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| We introduce | Fortuna, | a novel | offline RL-based |     | adaptive |                                                                       |     |     |     |     |     |     |
inProcICMLworkshop,2019,pp.1–10.
| video streams | technique | that effectively | adapts | to  | real-world |                                                                      |     |     |     |     |     |     |
| ------------- | --------- | ---------------- | ------ | --- | ---------- | -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|               |           |                  |        |     |            | [15] C.Finn,P.Abbeel,andS.Levine,“Model-agnosticmeta-learningforfast |     |     |     |     |     |     |
Internet conditions, and combines with TCP congestion con- adaptation of deep networks,” in Proc. Int. Conf. Mach. Learn., 2017,
pp.1126–1135.
| trol to further     | reduce rebuffering |            | time, optimizing |     | QoE ob- |                |          |       |           |         |         |                |
| ------------------- | ------------------ | ---------- | ---------------- | --- | ------- | -------------- | -------- | ----- | --------- | ------- | ------- | -------------- |
|                     |                    |            |                  |     |         | [16] T. Huang, | C. Zhou, | R.-X. | Zhang, C. | Wu, and | L. Sun, | “Learning tai- |
| jectives. Moreover, | Fortuna            | can handle | unconstrained    |     | video   |                |          |       |           |         |         |                |
loredadaptivebitratealgorithmstoheterogeneousnetworkconditions:A
domain-specificpriorsandmeta-reinforcementlearningapproach,”IEEE
streamsessions.Inallconsideredinternetvideostreamingsce-
J.Sel.AreasCommun.,vol.40,no.8,pp.2485–2503,Aug.2022.
| narios, Fortuna    | rivals or | outperforms | the state-of-the-art |     | ex-     |               |            |             |        |               |            |               |
| ------------------ | --------- | ----------- | -------------------- | --- | ------- | ------------- | ---------- | ----------- | ------ | ------------- | ---------- | ------------- |
|                    |           |             |                      |     |         | [17] S. Wang, | J. Lin,    | and Y. Dai, | “MMVS: | Enabling      | robust     | adaptivevideo |
| isting approaches, | with an   | average     | QoE improvement      |     | ranging |               |            |             |        |               |            |               |
|                    |           |             |                      |     |         | streaming     | for wildly | fluctuating | and    | heterogeneous | networks,” | IEEE          |
from 1.2%-31.9%. Additionally, experimental results demon- Trans.Multimedia,vol.26,pp.11018–11030,2024.
|     |     |     |     |     |     | [18] N.Kanetal.,“Improvinggeneralizationforneuraladaptivevideostream- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
stratethatFortunaexhibitsbettergeneralizationcapabilitiesin
ingviametareinforcementlearning,”inProc.30thACMInt.Conf.Mul-
unseennetworkconditionsandQoEuserpreferences. timedia,2022,pp.3006–3016.
Inpractice,webelievethatFortunacanoffervaluableinsights [19] Z.Xia,Y.Zhou,F.Y.Yan,andJ.Jiang,“Genet:Automaticcurriculumgen-
not only for bitrate adaptation of video streaming but also for erationforlearningadaptationinnetworking,”inProc.ACMSIGCOMM
Conf.,2022,pp.397–413.
TCP congestion control, as it eliminates the costly expense of [20] Y.Bengio,J.Louradour,R.Collobert,andJ.Weston,“Curriculumlearn-
onlinelearningwhileenablingswiftadaptationtonewnetwork ing,”inProc.26thAnnu.Int.Conf.Mach.Learn.,2009,pp.41–48.
|     |     |     |     |     |     | [21] X.Zuo,J.Yang,M.Wang,andY.Cui,“Adaptivebitratewithuser-level |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
conditions.
QoEpreferenceforvideostreaming,”inProc.IEEEINFOCOM2022-
IEEEConf.Comput.Commun.,2022,pp.1279–1288.
|     |     |     |     |     |     | [22] T.Huang,R.-X.Zhang,C.Wu,andL.Sun,“Optimizingadaptivevideo |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
ACKNOWLEDGMENT
streamingwithhumanfeedback,”inProc.31stACMInt.Conf.Multimedia,
The authors thank Prof. Li Zeping and Dr. Huang Tianchi 2023,pp.1707–1718.
|     |     |     |     |     |     | [23] X. Wei | et al., | “Reinforcement | learning-based |     | qoe-oriented | dynamic |
| --- | --- | --- | --- | --- | --- | ----------- | ------- | -------------- | -------------- | --- | ------------ | ------- |
for their guidance regarding video streaming in practice, and adaptive streaming framework,” Inf. Sci., vol. 569, pp.786–803,
| theanonymousIEEETON,TMMreviewersfortheirvaluable |     |     |     |     |     | 2021. |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
feedback. [24] V. Mnih, “Playing Atari with deep reinforcement learning,” 2013,
arXiv:1312.5602.
|     |     |     |     |     |     | [25] H.Maoetal.,“Park:Anopenplatformforlearning-augmentedcomputer |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
REFERENCES systems,”inProc.Adv.NeuralInf.Process.Syst.,2019,pp.1–20.
|     |     |     |     |     |     | [26] V.H.Pong,A.V.Nair,L.M.Smith,C.Huang,andS.Levine,“Offline |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
[1] T.Barnett,S.Jain,U.Andra,andT.Khurana,“Ciscovisualnetworking meta-reinforcementlearningwithonlineself-supervision,”inProc.Int.
index(VNI)completeforecastupdate,”2017–2022,”Americas/EMEAR Conf.Mach.Learn.,2022,pp.17811–17829.
CiscoKnowledgeNetwork(CKN)Presentation,pp.1–30,2021. [27] S. Floyd and E. Kohler, “Internet research needs better models,”
[2] Y.Sunetal.,“CS2P:Improvingvideobitrateselectionandadaptation ACM SIGCOMM Comput. Commun. Rev., vol. 33, no. 1, pp.29–34,
| withdata-driventhroughputprediction,”inProc.ACMSIGCOMMConf., |     |     |     |     |     | 2003. |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
2016,pp.272–285. [28] S. Floyd and V. Paxson, “Difficulties in simulating the internet,”
[3] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal IEEE/ACMTrans.Netw.,vol.9,no.4,pp.392–403,Aug.2001.
|     |     |     |     |     |     | [29] H.Mao,M.Schwarzkopf,S.B.Venkatakrishnan,Z.Meng,andM.Al- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
bitrateadaptationforonlinevideos,”IEEE/ACMTrans.Netw.,vol.28,
no.4,pp.1698–1711,Aug.2020. izadeh,“Learningschedulingalgorithmsfordataprocessingclusters,”in
[4] B.Wang,M.Xu,F.Ren,andJ.Wu,“ImprovingrobustnessofDASH Proc.ACMSpecialInt.GroupDataCommun.,2019,pp.270–288.
against unpredictable network variations,” IEEE Trans. Multimedia, [30] A.Kumar,R.Agarwal,X.Geng,G.Tucker,andS.Levine,“OfflineQ-
vol.24,pp.323–337,2022. learningondiversemulti-taskdatabothscalesandgeneralizes,”inProc.
ICLR,2023.
[5] X.Yin,A.Jindal,V.Sekar,andB.Sinopoli,“Acontrol-theoreticapproach
fordynamicadaptivevideostreamingoverHTTP,”inProc.ACMConf. [31] A.Kumaretal.,“DR3:Value-baseddeepreinforcementlearningrequires
SpecialInt.GroupDataCommun.(SIGCOMM),2015,pp.325–338. explicitregularization,”inProc.ICLR,2024,pp.1–41.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore.  Restrictions apply.

8198 IEEETRANSACTIONSONMULTIMEDIA,VOL.27,2025
[32] H.Haile,K.-J.Grinnemo,S.Ferlin,P.Hurtig,andA.Brunstrom,“Perfor- [56] J.Lietal.,“Suphx:MasteringMahjongwithdeepreinforcementlearning,”
manceofQUICcongestioncontrolalgorithmsin5Gnetworks,”inProc. 2020,arXiv:2003.13590.
ACMSIGCOMMWorkshop5GBeyondNetw.Measurements,Modeling, [57] D. Ye et al., “Mastering complex control in MOBA games with deep
UseCases,2022,pp.15–21. reinforcementlearning,”inProc.AAAIConf.Artif.Intell.,2020,vol.34,
[33] N.Cardwell,Y.Cheng,C.S.Gunn,S.H.Yeganeh,andV.Jacobson,“BBR: pp.6672–6679.
Congestion-based congestion control: Measuring bottleneck bandwidth [58] K.Rakelly,A.Zhou,C.Finn,S.Levine,andD.Quillen,“Efficientoff-
andround-trippropagationtime,”Queue,vol.14,no.5,pp.20–53,2016. policymeta-reinforcementlearningviaprobabilisticcontextvariables,”in
[34] S.Ha,I.Rhee,andL.Xu,“Cubic:AnewTCP-friendlyhigh-speedtcp Proc.Int.Conf.Mach.Learn.,2019,pp.5331–5340.
variant,”ACMSIGOPSoperatingSyst.Rev.,vol.42,no.5,pp.64–74, [59] “Meta RL,” (n.d.). [Online]. Available: https://github.com/katerakelly/
2008. oyster
[35] Z.Wang,A.C.Bovik,H.R.Sheikh,andE.P.Simoncelli,“Imagequality [60] A. Bentaleb, M. Lim, M. N. Akcay, A. C. Begen, and R. Zimmer-
assessment: From error visibility to structural similarity,” IEEE Trans. mann,“Bitrateadaptationandguidancewithmetareinforcementlearn-
ImageProcess.,vol.13,no.4,pp.600–612,Apr.2004. ing,” IEEE Trans. Mobile Comput., vol. 23, no. 11, pp.10378–10392,
[36] V.Netflix,“Videomulti-methodassessmentfusion,”2019.[Online].Avail- Nov.2024.
able:https://github.com/Netflix/vmaf [61] M.Allman,V.Paxson,andE.Blanton,“RFC5681:TCPcongestioncon-
[37] A. Nair, A. Gupta, M. Dalal, and S. Levine, “Awac: Accelerating on- trol,”2009.
linereinforcementlearningwithofflinedatasets,”inProc.ICLR,2021, [62] T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Wat-
pp.1–17. son, “A buffer-based approach to rate adaptation: Evidence from a
[38] Z.Huoetal.,“Fasteron-devicetrainingusingnewfederatedmomentum largevideostreamingservice,”inProc.ACMConf.SIGCOMM,2014,
algorithm,”2020,arXiv:2002.02090. pp.187–198.
[39] X.Jiangetal.,“MNN:Auniversalandefficientinferenceengine,”inProc.
Mach.Learn.Syst.,2020,vol.2,pp.1–13.
[40] A.Gupta,V.Kumar,C.Lynch,S.Levine,andK.Hausman,“Relaypol-
icylearning:Solvinglong-horizontasksviaimitationandreinforcement
learning,”inProc.Conf.RobotLearn.,2019,pp.1–13.
[41] T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine, “Soft actor-
critic: Off-policy maximum entropy deep reinforcement learning Ling Yi received the masters degree in computer
with a stochastic actor,” in Proc. Int. Conf. Mach. Learn., 2018, sciencein2022fromGuizhouUniversity,Guiyang,
pp.1861–1870. China,whereheiscurrentlyworkingtowardthePh.D.
[42] J.Rothfuss,D.Lee,I.Clavera,T.Asfour,andP.Abbeel,“Promp:Proximal degree.Hisresearchinterestsincludevideostream-
meta-policysearch,”inProc.ICLR,2019,pp.1–25. ingtechnologies,networkcongestioncontrol,natural
[43] C.M.BishopandN.M.Nasrabadi,PatternRecognitionandMachine languageprocessing,andreinforcementlearningfor
Learning,vol.4.Berlin,Germany:Springer,2006. realworldapplications.
[44] C.FinnandS.Levine,“Meta-learninganduniversality:Deeprepresen-
tationsandgradientdescentcanapproximateanylearningalgorithm,”in
Proc.ICLR,2018,pp.1–20.
[45] E.Mitchell,R.Rafailov,X.B.Peng,S.Levine,andC.Finn,“Offline
meta-reinforcementlearningwithadvantageweighting,”inProc.Int.Conf.
Mach.Learn.,2021,pp.7780–7791.
[46] R. Netravali et al., “Mahimahi: Accurate {Record-and-Replay} for
{HTTP},”inProc.USENIXAnnu.Tech.Conf.,2015,pp.417–429. YongbinQiniscurrentlyaProfessorwiththeSchool
[47] J. Schmidt-Hieber, “Nonparametric regression using deep neural net- ofComputerScienceandTechnology,GuizhouUni-
works with ReLU activation function,” Ann. Statist., vol. 48, no. 4, versity,Guiyang,China.Hisprimaryresearchinter-
pp.1875–1897,2020. estsincludemachinelearning,naturallanguagepro-
[48] Z.Zhang,“Improvedadamoptimizerfordeepneuralnetworks,”inProc. cessing,andlargelanguagemodels.
IEEE/ACM26thInt.Symp.Qual.Service,2018,pp.1–2.
[49] “FCC broadband dataset,” (n.d.). [Online].Available: http://data.fcc.
gov/download/measuring-broadband-America/2016/data-raw-2016-
jun.tar.gz
[50] “Norway HSDPA bandwidth logs,” (n.d.). [Online]. Available: http://
home.ifi.uio.no/paalh/dataset/hsdpa-tcp-logs/
[51] “Belgium4G/LTEbandwidthlogs(bonus),”(n.d.).[Online].Available:
http://users.ugent.be/jvdrhoof/dataset-4g/logs/logs_all.zip
[52] H.Mao,S.B.Venkatakrishnan,M.Schwarzkopf,andM.Alizadeh,“Vari-
RuizhangHuangreceivedthePh.D.degreefromthe
ancereductionforreinforcementlearningininput-drivenenvironments,”
Chinese University of Hong Kong, Hong Kong, in
ICLR,2019,pp.1–20.
2008.SheiscurrentlyaProfessorwiththeSchoolof
[53] A. Narayanan et al., “Lumos5g: Mapping and predicting commercial
ComputerScienceandTechnology,GuizhouUniver-
mmWave 5G throughput,” in Proc. ACM Internet Meas. Conf., 2020,
sity,Guiyang,China.Herprimaryresearchinterests
pp.176–193.
includemachinelearningandnaturallanguagepro-
[54] A.Narayananetal.,“Avariegatedlookat5Ginthewild:Performance,
cessing.
power,andQoEimplications,” inProc. ACMSIGCOMMConf.,2021,
pp.610–625.
[55] “sigcomm2021,dashvideo,5G,”(n.d.).[Online].Available:https://drive.
google.com/drive/folders/1_Hxz6M8qxZJnpJz38ll-Bw7OV1U4FDSk
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:38:19 UTC from IEEE Xplore. Restrictions apply.