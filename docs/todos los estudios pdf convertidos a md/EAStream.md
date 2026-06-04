1176 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.19,NO.2,MARCH/APRIL2026
EAStream: An Environment-Aware Adaptive Bitrate
Algorithm for Reliable Video Streaming Services
ZemingHuang,WenjingXiao ,MiaojiangChen ,Member,IEEE,ZhiquanLiu ,MinChen ,Fellow,IEEE,
AthanasiosV.Vasilakos ,SeniorMember,IEEE,AhmedFarouk ,andHoubingHerbertSong ,Fellow,IEEE
Abstract—VideostreaminghasemergedasawidelyusedInter- component of global Internet traffic. According to the Global
netservice,inwhichadaptivebitrate(ABR)algorithmsplayacrit- Internet Phenomena Report 2024 [1], the traffic transporting
icalroleindeliveringhighqualityofexperience(QoE).However,
videoaccountsfor68%and64%ofthetotaldownlinktrafficof
existing learning-based ABR methods often suffer from limited
fixed and mobile networks, respectively. Given the industry’s
generalizationinunseenanddynamicallychangingnetworkcondi-
tions.Althoughsomemeta-reinforcementlearningtechniqueshave projected growth to $416.84 billion by 2030 [2], ensuring a
been proposed to mitigate this issue, they generally depend on superiorQualityofExperience(QoE)iscriticalforuserretention
additional online training or fine-tuning. To overcome these lim- andbusinesssuccess.Toachievethis,AdaptiveBitrate(ABR)
itations,thispaperintroducesEAStream,anenvironment-aware
technology has been widely adopted as the standard delivery
ABRalgorithmbasedonmeta-reinforcementlearningforreliable
mechanism [3], [4]. By dividing videos into chunks available
video streaming services. The method employs a variational au-
toencodertoextractalatentrepresentationofthecurrentnetwork at multiple quality levels, ABR algorithms dynamically select
environmentfromhistoricalinteractiondata.Thislatentvariable, the optimal bitrate for each chunk based on real-time network
along with the current system state, is fed into a policy network throughputandbufferoccupancy.However,theABRalgorithm
thatperceivesnetworkconditionsinrealtimeandadaptsbitrate
faces challenges because it needs to balance conflicting ob-
decisions accordingly, without requiring further online training.
jectives: maximizing video quality and minimizing playback
Acomprehensiveevaluationisconductedusingdiversereal-world
networktraces.ExperimentalresultsshowthatEAStreamnotonly interruptions.Specifically,highbitratechunkswillbeselected
achievesleadingperformanceonin-distributiontestsetscompared for better playback quality. However, it will increase the risk
tostate-of-the-artABRalgorithms,butalsodemonstratessuperior of playback stalls, especially in the case of unstable network
generalizationcapabilityonout-of-distributiontestscenarios.
conditions.
Index Terms—Adaptive video streaming, generalization, meta Traditional ABR algorithms primarily rely on fixed rules or
learning,networkuncertainty,qualityofexperience. control-theoretic models. Heuristic-based approaches, such as
therate-basedFESTIVE[5]andthebuffer-basedBBA[6],make
I. INTRODUCTION
decisions using predefined thresholds. While computationally
WITH the rapid development of the Internet in recent efficient and easy to deploy, these rule-based methods lack
years, video streaming has become the predominant theflexibilitytoadapttodiversenetworkscenariosorvarying
QoE preferences. To address this, Model Predictive Control
Received 2 December 2025; revised 9 February 2026; accepted 3 March (MPC)[7]wasintroducedtoenableproactivedecision-making
2026.Dateofpublication9March2026;dateofcurrentversion10April2026.
by optimizing QoE over a future horizon based on throughput
ThisworkwassupportedinpartbytheNationalNaturalScienceFoundationof
ChinaunderGrant62462002andGrant62502101,inpartbytheNaturalScience predictions. Although MPC generally outperforms heuristics,
FoundationofGuangxi,ChinaunderGrant2025GXNSFAA069958andGrant its reliability heavily depends on the accuracy of bandwidth
2025GXNSFBA069394, and in part by the Key Research and Development
estimation.
ProgramofGuangxiunderGrantAD25069071.(ZemingHuangandWenjing
Xiaoareco-firstauthors.)(Correspondingauthor:MiaojiangChen.) In recent years, considerable attention has been directed to-
Zeming Huang, Wenjing Xiao, and Miaojiang Chen are with the School wardsapplyinglearning-basedmethodstoABRstreaming[8],
of Computer, Electronics and Information, Guangxi University, Nanning
[9], [10], [11]. In contrast to traditional heuristic-based meth-
530004, China, and also with the Guangxi Key Laboratory of Multimedia
CommunicationsandNetworkTechnology,Nanning530004,China(e-mail: ods, learning-based methods typically train neural networks
zem@st.gxu.edu.cn;wenjingx@gxu.edu.cn;mjchen_cs@gxu.edu.cn). ondatasetsspanningmultiplenetworkconditions.Thisallows
Zhiquan Liu is with the College of Cyber Security, Jinan University,
themtocapturethecomplicatedcorrelationsinvideostreaming.
Guangzhou510632,China(e-mail:zqliu@jnu.edu.cn).
MinCheniswiththeSchoolofComputerScienceandEngineering,South The seminal method, Pensieve [8], uses deep reinforcement
China University of Technology, Guangzhou 510006, China, and also with learning algorithm (DRL) to learn bitrate adaptation policies.
PazhouLaboratory,Guangzhou510330,China(e-mail:minchen@ieee.org).
Unlike the MPC-based methods that rely on system models,
Athanasios V. Vasilakos is with the Department of ICT and Center for
AI Research, University of Agder(UiA), 4879 Grimstad, Norway (e-mail: the DRL algorithm directly learns the model-free strategies
thanos.vasilakos@uia.no). fromexperience,enablingittobetterhandledynamicnetworks.
Ahmed Farouk is with the Faculty of Computers and Artificial
Furthermore, DRL algorithms have long-term planning capa-
Intelligence, Hurghada University, Hurghada 83523, Egypt (e-mail:
ahmed.farouk@sci.svu.edu.eg). bilities, which allows them to make complex strategic trade-
Houbing Herbert Song is with the Department of Information Systems, offs that balance instant video quality and long-term viewing
UniversityofMaryland,Baltimore,MD21250USA(e-mail:h.song@ieee.org).
stability.
DigitalObjectIdentifier10.1109/TSC.2026.3671090
1939-1374©2026IEEE.Allrightsreserved,includingrightsfortextanddatamining,andtrainingofartificialintelligenceandsimilartechnologies.
Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore. Restrictions apply.

HUANGetal.:EASTREAM:ANENVIRONMENT-AWAREADAPTIVEBITRATEALGORITHMFORRELIABLEVIDEOSTREAMINGSERVICES 1177
Despite these advantages, one challenge DRL-based ABR bettergeneralizationabilityinunseen,out-of-distribution
methods face is their limited generalization to unseen net- environmentscomparedtostate-of-the-artalgorithms.
work conditions. This is because the learned policy is prone The remainder of this paper is structured as follows.
to overfitting to the training network environment. Such over- Section II reviews the related work in ABR streaming and
specializationisparticularlyproblematicasreal-worldnetworks meta-reinforcement learning. Section III formulates the ABR
are inherently dynamic and non-stationary. In fact, when de- problemandpresentsourBayesianadaptivemodelingapproach.
ployed in real-world scenarios, their performance has been SectionIVdetailsthesystemdesignofourproposedEAStream
shown to be even inferior to that of simple heuristic-based framework,includingitsarchitectureandtrainingmethodology.
methods[10]. Section V presents the comprehensive experimental evalua-
To tackle this generalization challenge, recent studies have tion and analysis of results. Finally, Section VI concludes the
| introducedmeta-reinforcementlearningapproaches,whichgen- |     |     |     |     |     |     |     | paper. |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
erallyfallintotwocategories.Optimization-basedmethods[12],
[13]learnanadaptableinitializationbuttypicallyrelyononline II. RELATEDWORK
gradientupdatesduringplayback.Thisrequirementintroduces
significant computational overhead and latency, making them This section will review the related work in the fields of
|            |                          |     |     |     |          |             |     | ABR streaming |     | and meta-learning, |     |     | particularly | focusing | on  |
| ---------- | ------------------------ | --- | --- | --- | -------- | ----------- | --- | ------------- | --- | ------------------ | --- | --- | ------------ | -------- | --- |
| less ideal | for resource-constrained |     |     |     | devices. | Conversely, | the |               |     |                    |     |     |              |          |     |
meta-reinforcementlearning.
context-basedmethod[14]adaptsbyinferringalatentcontext
vectorfromhistorywithoutonlinegradientupdates.However,it
reliesondeterministicembeddingssupervisedsolelybyreward A. ConventionalABRAlgorithms
| signals, | which limits |     | their ability | to  | model | the uncertainty | of  |     |     |     |     |     |     |     |     |
| -------- | ------------ | --- | ------------- | --- | ----- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ABRstreaminghasbeenthesubjectofextensiveresearchin
| stochastic | networks | and | fails | to capture | the | underlying | state |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ----- | ---------- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
thefieldofnetworkcommunicationoverthepastdecade.Early
transitiondynamics.
ABRalgorithmsprimarilyreliedonexplicitlydefinedrulesand
Toovercometheselimitations,weproposeEAStream,anovel mathematicalmodels.Theseapproachesaretypicallyclassified
| probabilistic | context-based |     | framework. |     | Unlike | optimization- |     |     |     |     |     |     |     |     |     |
| ------------- | ------------- | --- | ---------- | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
intotwomaincategories:heuristic-basedmethodsandcontrol-
basedmethods,EAStreamachievesrobustgeneralizationwith-
theoreticmethods.
| out any | online | parameter |     | updates. | Crucially, | distinct | from |     |     |     |     |     |     |     |     |
| ------- | ------ | --------- | --- | -------- | ---------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Heuristic-basedmethodsrepresenttheearliestclassofABR
thepreviouscontext-basedapproachthatreliesondeterministic
|     |     |     |     |     |     |     |     | algorithms, | selecting | bitrates |     | through | intuitive, |     | pre-defined |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | -------- | --- | ------- | ---------- | --- | ----------- |
vectors, we formulate the ABR problem as a Bayesian Adap- rules. These are primarily categorized into two classes: rate-
| tive Markov   | Decision    |     | Process | (BAMDP)     | [15]. | By   | leveraging |           |               |     |            |     |             |      |         |
| ------------- | ----------- | --- | ------- | ----------- | ----- | ---- | ---------- | --------- | ------------- | --- | ---------- | --- | ----------- | ---- | ------- |
|               |             |     |         |             |       |      |            | based and | buffer-based. |     | Rate-based |     | algorithms, | such | as FES- |
| a variational | autoencoder |     | to      | reconstruct | both  | next | states and |           |               |     |            |     |             |      |         |
TIVE[5],guidetheirdecisionsbymeasuringhistoricalnetwork
| rewards, | EAStream | infers | a   | probabilistic | belief | distribution |     |     |     |     |     |     |     |     |     |
| -------- | -------- | ------ | --- | ------------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
throughput.Toaddressthelagproblemofrate-basedmethods,
thatcapturestheenvironmentaldynamics.Thisenablestheagent
|     |     |     |     |     |     |     |     | buffer-based | algorithms |     | use buffer | occupancy |     | as a | key metric. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | ---------- | --------- | --- | ---- | ----------- |
to reason about uncertainty and adapt substantially better to BBA [6] matches bitrate actions by setting different buffer
unseen,non-stationarynetworkconditions.
|             |     |          |               |     |     |            |        | thresholds. | The      | more sophisticated |     |     | algorithm | BOLA | [16] is   |
| ----------- | --- | -------- | ------------- | --- | --- | ---------- | ------ | ----------- | -------- | ------------------ | --- | --- | --------- | ---- | --------- |
| In summary, |     | the main | contributions |     | of  | this paper | are as |             |          |                    |     |     |           |      |           |
|             |     |          |               |     |     |            |        | based on    | Lyapunov | optimization       |     | to  | maximize  | the  | QoE while |
follows:
(cid:2) ensuringthatthebufferisnotexhausted.Althoughtheheuristic
WeinnovativelyadoptedtheDynamicAdaptiveStreaming
methodissimpleandeffective,thefixedrulesalsolimititsability
overHTTP(DASH)architectureforvideostreaming,opti-
toadapttothedynamicandunstablenetworkenvironment.
mizingdynamicABRdecisionsthroughaBayesianAdap-
|     |     |     |     |     |     |     |     | To address |     | the passivity |     | of heuristic |     | approaches, | re- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------- | --- | ------------ | --- | ----------- | --- |
tiveMarkovDecisionProcess(BAMDP)(SectionIII).By
|     |     |     |     |     |     |     |     | searchers | have | introduced | prospective |     | control-theoretic |     | ap- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ---------- | ----------- | --- | ----------------- | --- | --- |
treating unknown parameters such as network bandwidth proaches. Among these approaches, Model Predictive Control
| as        | random     | variables | and           | maintaining |           | a probability | dis-      |       |            |      |              |           |     |            |     |
| --------- | ---------- | --------- | ------------- | ----------- | --------- | ------------- | --------- | ----- | ---------- | ---- | ------------ | --------- | --- | ---------- | --- |
|           |            |           |               |             |           |               |           | (MPC) | [7] is the | most | influential. | MPC-based |     | algorithms | use |
| tribution | (posterior |           | distribution) |             | for them, | the           | algorithm |       |            |      |              |           |     |            |     |
thepredictivebandwidthtooptimizeaseriesofbitratedecisions
| not | only makes | decisions |     | based | on the | current | estimated |     |     |     |     |     |     |     |     |
| --- | ---------- | --------- | --- | ----- | ------ | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
overthefuturehorizon.Subsequentresearchhasfocusedonen-
bandwidth,butalsobasedonthecompletestateofallpos-
hancingMPC’scoreissueofpredictionaccuracy.Forinstance,
sible bandwidth states and their occurrence probabilities, Fugu[10]improvesthepredictionmodulebyusingadeepneural
| making | ABR | decisions |     | more robust | in  | dynamic | network |          |       |          |          |                 |     |     |             |
| ------ | --- | --------- | --- | ----------- | --- | ------- | ------- | -------- | ----- | -------- | -------- | --------------- | --- | --- | ----------- |
|        |     |           |     |             |     |         |         | network, | while | AAR [17] | utilizes | server-assisted |     |     | information |
environments.
| (cid:2) |     |     |     |     |     |     |     | toachievemoreaccuratebandwidthprediction.BeyondMPC, |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
WeproposeEAStream(SectionIV),anovelenvironment-
|       |     |           |     |       |                       |     |     | other classical | control   | models          |     | have         | also been | explored,   | such   |
| ----- | --- | --------- | --- | ----- | --------------------- | --- | --- | --------------- | --------- | --------------- | --- | ------------ | --------- | ----------- | ------ |
| aware | ABR | framework |     | based | on meta-reinforcement |     |     |                 |           |                 |     |              |           |             |        |
|       |     |           |     |       |                       |     |     | as PIA          | [18] uses | a PI controller |     | to stabilize |           | the playout | buffer |
learning. Unlike optimization-based meta-learning meth- at the target level. The effectiveness of these approaches is
odsthatrequireonlinefine-tuning,EAStreamleveragesa
|     |     |     |     |     |     |     |     | fundamentally | dependent |     | on the | model’s |     | accuracy. | However, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | ------ | ------- | --- | --------- | -------- |
context-basedmechanismtoadapttonewenvironmentsin
thisisachallengeinrealdynamicnetworkenvironments.
real-timewithoutanygradientupdatesduringdeployment.
(cid:2)
| We         | conduct | extensive | experiments |          | across | a diversity | of          |                                |     |     |     |     |     |     |     |
| ---------- | ------- | --------- | ----------- | -------- | ------ | ----------- | ----------- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|            |         |           |             |          |        |             |             | B. Learning-BasedABRAlgorithms |     |     |     |     |     |     |     |
| real-world |         | network   | traces      | (Section | V).    | Our         | evaluations |                                |     |     |     |     |     |     |     |
show that EAStream not only achieves state-of-the-art Inrecentyears,moreresearchhasbeenconductedonABRal-
performance on in-distribution networks, but also shows gorithmsbasedonreinforcementlearning.Thepioneeringwork
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.

1178 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.19,NO.2,MARCH/APRIL2026
Pensieve[8]employsDeepReinforcementLearning(DRL)and steps.Acanonical example isModel-Agnostic Meta-Learning
outperformstraditionalalgorithms. (MAML) [36], which meta-learns a shared prior for fast fine-
The success of Pensieve has motivated a series of studies tuning.However,MAML’srelianceonsecond-orderderivatives
onLearning-basedABRalgorithms.Forinstance,Comyco[9] is computationally expensive. To address this, more efficient,
employs imitation learning to enhance sample efficiency. first-order alternatives were developed. FOMAML [37] and
Tiyuntsong [19] introduces a self-play framework to clearly Reptile[38]simplifytheupdatebyignoringorapproximating
definetheoptimizationobjective. higher-order terms, avoiding the need to differentiate through
Anothermajordirectionfocusesonjointlyoptimizingbitrate theentireoptimizationprocess.Otherworksfocusonimproving
withothermetrics.EarlyworkslikeAMIS[20]managebothbi- adaptationinhigh-dimensionalparameterspaces.Forinstance,
trateandplayoutspeedtomitigatetheriskofrebuffering.Recent LEO[39]decouplestheadaptationfromthehigh-dimensional
studiesextendtheseobjectivestoenergyandtrafficefficiency. parameterspaceviatheconstructionofalatentembeddingcon-
DeepBuffer [21] jointly controls the maximum buffer size to ditionedonthedataandconductingthemeta-learningupdates
avoid unnecessary bandwidth consumption. GreenABR+ [22] inthislow-dimensionalspace.
employsaDDPG-basedapproachtoreducepowerconsumption. Incontrast,context-basedmethodslearnasinglepolicycon-
BE-ABR [23] uses Transformer-based prediction to minimize ditionedonatask-specificcontextvariable,whichsummarizes
datawaste. the agent’s interaction history and enables adaptation without
DRL has also been tailored for specific environments. In test-time gradient updates. A pioneering approach, RL2 [40],
mobileedgecomputing(MEC),Guoetal.[24]jointlyoptimize usesarecurrentneuralnetwork(RNN)toimplicitlyinfertheen-
transcoding and bitrate decisions. QAVA [25] addresses the vironment’sunderlyingdynamics.Moreadvancedmethodslike
fairnessproblemamongmultipleclients.Moreover,researchers PEARL [41] extend this by training a probabilistic encoder to
tackle specific application challenges: CAST [26] prioritizes inferlatentcontextvariablesfromoff-policydata,significantly
intricatevideoscenes,L2AC-E[27]minimizeslatencyforlive improvingmeta-trainingsampleefficiency.
streaming, and DeepVR [28] predicts user field-of-view for Severalrecentworkshaveappliedoptimization-basedmeta-
panoramic video. To handle extreme mobility, EIE-ABR [29] learning to the ABR problem, requiring an online training
integrates environmental data to optimize streaming on high- phase to adapt. For instance, A2BR [12] employs a MAML-
speedrailways. based framework to learn a meta-policy offline, which is then
To address the black-box nature of deep learning, recent rapidly fine-tuned online to create a tailor-made policy for
research has increasingly focused on interpretability. Peretto specific network conditions. Similarly, MMVS [13] integrates
etal.[30]proposedanML-assistedarchitectureprovidinginter- the MAML-based framework with PPO to handle highly fluc-
pretablepredictionhints,andComTree[31]usedLLMstoselect tuatingnetworks,andproposesametaadvantagenormalization
comprehensibledecisiontrees.Furthermore,NeuroBA[32]pro- techniquetostabilizetheonlineadaptationprocess.Inadifferent
poses a neuro-symbolic framework, combining deep learning structure,MetaABR[14]extractslatentcontextsfromhistorical
with logic reasoning to handle uncertainty and enhance inter- trajectories to adjust policies without online gradient updates.
pretability. However, it relies on deterministic embeddings, ignoring the
Despitethesediverseadvances,akeylimitationpersists:most inherentuncertaintyinbandwidthevolution.
learning-basedagentssufferfrompoorgeneralizationtounseen In contrast, our proposed EAStream formulates the ABR
networkconditions.Toaddressthis,arecentworkNetLLM[33] problem as a BAMDP. By inferring a probabilistic belief over
exploresadaptingLargeLanguageModels(LLMs)asuniversal the environment via a VAE, our method explicitly models un-
foundationmodelstohandlediversenetworkingtasks.However, certainty,enablingrobustzero-shotadaptationtounseencondi-
it introduces significant computational overhead and latency, tions.
making it less ideal for real-time deployment on resource-
constraineddevices. III. METHODS
This section formulates the ABR decision process as an
C. Meta-ReinforcementLearningforGeneralization optimization task and models the network uncertainty using a
BAMDP. We then propose a Meta-RL-based ABR algorithm,
Totackletheoverfittingproblem,meta-learningoffersalearn-
calledEAStream,toapproximatetheBAMDPpolicy.
ing paradigm [34]. Its core idea is to train on a distribution of
relatedtaskstolearnaninductivebias,enablingfastadaptation
A. ProblemFormulation
tonew,unseentaskswithhighsampleefficiencyattesttime[35].
WhileconventionalRLagentstendtooverfitthetrainingtraces, AsshowninFig.1,atypicalABRstreamingsysteminvolves
Meta-Reinforcement Learning (Meta-RL) learns an adaptive complex video content preparation and delivery. The server
policy that generalizes across different network environments first encodes the raw video into multiple bitrate levels, each
fromthetaskdistribution[35]. corresponding to a discrete value in the set R. Each of these
Broadly,Meta-RL methods aretypicallycategorized astwo transcodedvideosisthensplitintoaseriesofNsmallerchunks,
mainparadigms:optimization-basedandcontext-based. all sharing a fixed duration of L seconds. Simultaneously, a
Optimization-basedmethodslearnasensitiveparameterini- manifest file named Media Presentation Description (MPD) is
tialization that allows for rapid adaptation via a few gradient createdtoprovidemetadataforthevideostream.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore. Restrictions apply.

HUANGetal.:EASTREAM:ANENVIRONMENT-AWAREADAPTIVEBITRATEALGORITHMFORRELIABLEVIDEOSTREAMINGSERVICES 1179
user.Thefluctuationspenaltyiscalculatedbyaccumulatingthe
absolutevariationsinqualityvalueacrossconsecutivechunks.
(cid:2)N
|     |     |     |     |     |     |     |     |     | QoE | =   | |q(R | n)−q(R | n−1 | )|. | (4) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------ | --- | --- | --- |
var
n=2
QoEObjective:ThefinalQoEobjectiveisdefinedasalinear
combinationofthesethreecomponents:
|     |     |     |     |     |     |     |               |              | QoE=μ | QoE          | −μ            | QoE              | −μ           | QoE           | , (5)     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | ----- | ------------ | ------------- | ---------------- | ------------ | ------------- | --------- |
|     |     |     |     |     |     |     |               |              |       | 1            | qual          | 2 rebuf          |              | 3 var         |           |
|     |     |     |     |     |     |     | where         | µ=(μ         |       | ,μ ,μ        | ) is a vector | of               | non-negative |               | weighting |
|     |     |     |     |     |     |     |               |              | 1     | 2 3          |               |                  |              |               |           |
|     |     |     |     |     |     |     | coefficients. |              | These | coefficients |               | are customizable |              | hyperparam-   |           |
|     |     |     |     |     |     |     | eters         | representing |       | different    | user          | preferences.     |              | For instance, | in-       |
Fig.1. AschematicrepresentationoftheDynamicAdaptiveStreamingover
|                         |     |     |     |     |     |     | creasingμ |     | willpenalizerebufferingmoreheavily,guidingthe |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
| HTTP(DASH)architecture. |     |     |     |     |     |     |           |     | 2                                             |     |     |     |     |     |     |
algorithmtowardsamoreconservativestrategytoensuresmooth
playback.Inourexperiments,weadoptstandardfixedsettings
These prepared chunks and MPD files are often hosted on forfaircomparison.
Therefore,theABRdecision-makingprocesscanbemodeled
aContentDeliveryNetwork(CDN)[42]forefficientdelivery.
asanoptimizationtasksubjecttoconstraints.Thetaskistode-
Whentheclientplayerstartsplayingavideo,itwillfirstrequest
|                                                      |     |     |     |     |     |     | terminetheoptimalsequenceofbitratesR=(R |     |     |     |     |     |     | ,R  | ,...,R |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ |
| theMPDfile,whichwillinformtheclientoftheURLtorequest |     |     |     |     |     |     |                                         |     |     |     |     |     |     | 1 2 | N)     |
thatmaximizesthetotalQoE,subjecttothesystem’sdynamic
| the video. | The | player | then dynamically |     | requests | video | chunks |     |     |     |     |     |     |     |     |
| ---------- | --- | ------ | ---------------- | --- | -------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
constraints.Thisobjectivebalancesaggressivebitrateselection
| sequentially. | For | each | chunk | n, the | ABR algorithm | selects | a   |     |     |     |     |     |     |     |     |
| ------------- | --- | ---- | ----- | ------ | ------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bitrateR ∈R.Thebitrateselectiondeterminesthechunksize againstthephysicalconstraintsofbufferdynamics,ensuringthat
n
thestochasticnetworksupplymeetsthedeterministicplayback
| d n(R n), | which | is then | downloaded |     | from the | CDN through | a   |     |     |     |     |     |     |     |     |
| --------- | ----- | ------- | ---------- | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
networkwithanaveragethroughputofC n. demand.Mathematically,thisisformulatedas:
| ThegoaloftheABRalgorithmistooptimizethelong-term |     |     |     |     |     |     |     |     |     | maxR |          | QoE, |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ---- | --- | --- | --- |
|                                                  |     |     |     |     |     |     |     |     |     |      | 1 ,...,R | N    |     |     |     |
QoEofusers.QoEevaluatesthesubjectivesatisfactionofusers,
⎧
w h i c h i s c o m p o s e d o f t h r e e c o m p o n e n t s : v i d e o q u a l i ty , r e b u f f e r - ⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ t = t + T ( R ) + T ,
|               |               |              |             |     |     |     |     |     |     | n + 1 | n   | n   | n   |     |     |
| ------------- | ------------- | ------------ | ----------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
| i n g , a n d | q u a l i t y | fl u c t u a | t i o n s . |     |     |     |     |     |     |       |     |     |     |     |     |
(cid:7)
V i d e o Q u a l i ty : T h e v i d e o q u a l i t y r e fl e c t s t h e p e r c e i v e d v i s u a l t T (R
|     |     |     |     |     |     |     |     |     |     | Cˆ = | 1      | n + | n) c ( t) | d t , |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------ | --- | --------- | ----- | --- |
|     |     |     |     | R   |     |     |     |     |     | n    | T (R ) | t   |           |       |     |
q u a l i t y d e r i v e d f r o m t h e b i t r a t e n o f e a c h v i d e o c h u n k . U s e r s n n
| t e n d t o | w a t c h | v i d e o s | w i t h | h i g h a | v e r a g e v i s u | a l q u a l i | t y . I t i s |     |     |     |           |       |         |         |     |
| ----------- | --------- | ----------- | ------- | --------- | ------------------- | ------------- | ------------- | --- | --- | --- | --------- | ----- | ------- | ------- | --- |
|             |           |             |         |           |                     |               |               |     |     | B   | = m a x ( | 0 , B | − T ( R | ) ) +L, | (6) |
c a l c u l a t e d b a s e d o n t h e s u m o f t h e n - t h c h u n k : n + 1 n n
s.t.
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩
(cid:2) N
|     |     |     |           |     |        |     |      |     |     | B = | T , |     |     |     |     |
| --- | --- | --- | --------- | --- | ------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |           |     | q( R , |     |      |     |     | 1   | s   |     |     |     |     |
|     |     | Q o | E q u a l | =   | n )    |     | (1 ) |     |     |     |     |     |     |     |     |
n = 1
|     |     |     |     |     |     |     |     |     |     | 0 ≤ B | n ≤ B | ,   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- |
max
| where q(R | n) represe | n   | ts t h e | vid e o | q u al it y level | for the | bitra te |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | -------- | ------- | ----------------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
R n.Theselectionofq(R n)commonlyincludestherawbitrate R ∈R,∀n∈{1,...,N}.
n
| R     |               |     |         | log(R |               |             |     |     |     |     |     |     |     |     |     |
| ----- | ------------- | --- | ------- | ----- | ------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| n and | a logarithmic |     | mapping |       | n) to reflect | diminishing |     |     |     |     |     |     |     |     |     |
Theconstraintsofthisformulationmodelthecoredynamics
returnsofhigherbitrate.
ofastreamingsession:
| RebufferingPenalty:Rebuffering,orplaybackstalling,occurs |     |     |     |     |     |     |     | (cid:2) |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
TimeEvolution:Thefirstconstraintdescribesthechangeof
| when the | playback | buffer | is  | depleted, | severely | degrading | the |       |           |                |           |         |             |             |               |
| -------- | -------- | ------ | --- | --------- | -------- | --------- | --- | ----- | --------- | -------------- | --------- | ------- | ----------- | ----------- | ------------- |
|          |          |        |     |           |          |           |     | t h e | n e x t d | e c i s io n p | o i n t t | . T h e | n e x t tim | e p oi n te | q ua t es t o |
u s e r ’ s v i e w in g ex p e r i e n c e . L e t Cˆ d e n o t e s t h e a v e r a g e n e t w o r k n + 1
|     |     |     |     | n   |     |     |     |     |     |     |     | t   |     |     | T R |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n T t h e s u m o f t h e c u r r e n t t i m e n , t h e d o w nl oa d t im e ( n ) ,
| t h r o u g h p | u t . T he | r e b u f f | e r i n g t | i m e fo | r c h u n k , | d e n o t e d a | s n , i s |       |           |              |                   |          |     |     |     |
| --------------- | ---------- | ----------- | ----------- | -------- | ------------- | --------------- | --------- | ----- | --------- | ------------ | ----------------- | -------- | --- | --- | --- |
|                 |            |             |             |          |               |                 |           | a n d | t h e p o | s s ib l e r | e b u f f e r i n | g ti m e | T . |     |     |
t h e d u r a t i o n b y w h i c h i t s d o w n l o a d t i m e , T ( R ) = d ( R ) / C ˆ , (cid:2) n
|     |     |     |     |     | n   | n   | n n |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
B N e t w o r k T h r o u g h p u t : T h e se c o n d c o n s t ra in t is t h e a ve r a g e
ex c e e d s th e b u ff e r o c c u p ancy n−1 just before the download ˆ
|                 |           |            |       |     |     |     |     | n e t | w o r k t | h r o u g h p | u t C n w | h e n d o | w n l o a d | in g c h u | n k n . I t i s |
| --------------- | --------- | ---------- | ----- | --- | --- | --- | --- | ----- | --------- | ------------- | --------- | --------- | ----------- | ---------- | --------------- |
| b e g in s . It | is c a lc | u l at e d | a s : |     |     |     |     |       |           |               |           |           |             |            |                 |
calculatedbyintegratingtheinstantaneousthroughputc(t)
|     | T   | =max{T(R |     | n)−B | ,0}. |     |     |                            |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | ---- | ---- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | n        |     |      | n−1  |     | (2) | withtheactualdownloadtime. |     |     |     |     |     |     |     |
(cid:2)
|           |             |     |         |        |            |                 |     | Buffer | Dynamics: |     | The third | constraint |     | represents | the |
| --------- | ----------- | --- | ------- | ------ | ---------- | --------------- | --- | ------ | --------- | --- | --------- | ---------- | --- | ---------- | --- |
| The total | rebuffering |     | penalty | is the | sum of all | stall durations |     |        |           |     |           |            |     |            |     |
changeofbufferoccupancy.Specifically,Lrepresentsthe
throughoutthesession:
|     |     |     |     |          |     |     |     | fixed                                     | duration | of  | a chunk. | The new | buffer | level | B n+1 is |
| --- | --- | --- | --- | -------- | --- | --- | --- | ----------------------------------------- | -------- | --- | -------- | ------- | ------ | ----- | -------- |
|     |     |     |     | (cid:2)N |     |     |     | calculatedbysubtractingthedownloadtimeT(R |          |     |          |         |        |       | n)from   |
QoE = T . (3) thepreviouslevelB nandaddingthedurationLofthenew
|     |     |     | rebuf |     | n   |     |     |                  |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |       | n=1 |     |     |     | downloadedchunk. |     |     |     |     |     |     |     |
(cid:2)
QualityFluctuationsPenalty:Frequentandlargevariationsin BoundaryConditions:Thefinalconstraintssetthebound-
|     |     |     |     |     |     |     |     |     |     | B   | =T  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
videoqualitybetweenconsecutivechunkscanbejarringtothe ary conditions. s defines the initial buffer level.
1
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.

1180 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.19,NO.2,MARCH/APRIL2026
The buffer level B n is always capped between zero and Formally, the transition function in the hyper-state space
amaximumcapacityB max .Finally,thechosenbitrateR n S+ =S×B decomposes into the physical transition and the
mustbelongtothediscretesetofavailablebitratesR. informationstateupdate:
B. BayesianAdaptiveModelingforEnvironmental P+(s+ t+1 |s+ t ,a t ,r t)
Uncertainty =P+(s t+1 ,b t+1 |s t ,a t ,r t ,b t)
Tosolvetheproblem,acommonandeffectiveapproachisto = (cid:10) E b t [P(s t(cid:11)+(cid:12)1 |s t ,a t) (cid:13) ]·δ (cid:10) (b t+1 =Updat (cid:11) e (cid:12) (b t ,s t ,a t ,s t+1 ) (cid:13) ).
useReinforcementLearning(RL)basedonaMarkovDecision
Process(MDP).Thesystemconsistsof(S,A,R,P,ρ ,γ,H). PhysicalTransition BeliefUpdate
0 (8)
Here,P isthestatetransitionfunctionandρ istheinitialstate
0
distribution. The agent’s objective is to learn a policy π that Therewardfunctionforthehyper-statedependssolelyonthe
maximizesthelong-termcumulativereward: physical statetransition,astheuser’sQoEisderived fromthe
(cid:8) (cid:9) actualphysicalstates.Thus,itisdefinedas:
H(cid:2)−1
J(π)=E ρ 0 ,P,π γtR(r t+1 |s t ,a t ,s t+1 ) , (7) R+(s+ t ,a t ,s+ t+1 )=R(s t ,a t ,s t+1 ), (9)
t=0
where H denotes the time horizon of a video streaming ses- whereR(s t ,a t ,s t+1 )isthestandardQoErewarddefinedin(5).
This reformulation transforms the original MDP into a
sion, and γ ∈[0,1] is the discount factor that determines the BAMDP,denotedbyM+ =(S+,A,R+,P+,ρ+,γ,H).Con-
importanceoffuturerewards.However,acorelimitationofthe sequently,ourprimarygoalistofindapolicyπto 0 maximizethe
standardMDPliesinitsassumptionofastationaryorperfectly
accumulatedlong-termrewardintheBAMDP:
known transition function P(s t+1 |s t ,a t). This assumption is (cid:8) (cid:9)
frequently violated in real-world networks, where conditions
H(cid:2)−1
likebandwidtharehighlydynamicandnon-stationary.AnABR J+(π)=E b
0
,ρ+
0
,P+,π γtR+(r t+1 |s+ t ,a t ,s+ t+1 ) . (10)
agent trained under one specific network trace may fail to t=0
generalize to other fluctuating network conditions, leading to ThestrategythatachievesthisgoalistermedaBayes-optimal
suboptimalperformance. policy. While this problem can theoretically be addressed via
To address this limitation, where the true dynamics of the methodslikeposteriorsampling[43]orBayesianplanning[44],
environment are unknown, we model the ABR problem as a theseapproachestypicallyincurprohibitivecomputationalover-
Bayes-AdaptiveMarkovDecisionProcess(BAMDP)[15]. headforreal-timeABRdecisions.Computingexactbeliefup-
In a standard MDP, the agent assumes the network follows dates is also generally infeasible in practice. Therefore, we
a fixed rule. In contrast, a BAMDP agent acknowledges its leverageameta-reinforcementlearningparadigmtotacklethis
ignorance about the specific network scenario. It maintains a issue,asdetailedbelow.
beliefstate—aprobabilistic“mentalmodel”ofthecurrentnet-
workenvironment.Astheagentobservesnewstatetransitions, C. ApproximatingBayes-OptimalPoliciesViaMeta-Learning
itrecursivelyupdatesthisbelief,allowingittoadaptitsstrategy
ThetheoreticalsolutionforBAMDPiscomputationallydiffi-
dynamicallybasedonitsconfidenceintheenvironment’sstate.
cult.Ourapproach,EAStream,employsameta-learningstrategy
Inthisframework,theunknownnetworkdynamicsaretreated
inspiredbyVariBAD[45]toacquireasolutionthatapproximates
as a latent variable. The agent maintains a belief state, b t,
thispolicy.
definedastheposteriordistributionoverthesepossiblenetwork
Inthemeta-learningframework,wemodeldifferentnetwork
environmentsgiventheinteractionhistoryτ :t.
environments as individual tasks, each defined by a hidden
Thedecision-makingprocessinaBAMDPextendsthestan- latentvariablem i.Thislatentvariablecorrespondstothebelief
dard MDP cycle by incorporating a belief update step. The
in BAMDP. Since the latent variable is unknown, the agent
processproceedsasfollows: mustinferinformationaboutm ifromitshistoricalinformation.
1)
p
i S s t
h
a a
y
t h
s
e
i
y
c
R p
a
e e
l
p r
s
- r
t
s e
a
t s
t
a e
e
t n e
s
t s
t
a + t t
a
i
n
o =
d
n:
t
(
h
A s
e
t t ,
c
e b
u
a t
r
c )
r
h ,
e
c
n
t o i
t
m n
b
s e
e
i s
l
s
i
t t
e
e in
f
p g
b
t
t
, o
.
t f h t e he ag o e b n s t e ’ r s v s a t b a l t e e i S
T
n p
h
t e o
is
c a i
d
fi n
i
c
s
i a
t
n
r
l f l
i
y
b
e , r
u
r w
t
e
io
e d
n
e d m i
s
s
e
p t
r
r l
v
o ib
e
y u
s
a ti n
a
o
s
e n n
a
c q
n
o φ d (
in
m e
f
r
e
| t τ
r
o
e
:t t
n
) r
c
a w
e
ns i
o
f th o
f
i r n
t
m
h
t
e
t h h e
e
e
n
l t
v
a ra t
i
e
r
j
o
e n c
n
t t
m
o sp r
e
y a
n
c τ
t
e
’
:
s
t .
2) Action&Observation:Theagentselectsanactiona t.The
latentfeatures.
environmentthentransitionstoanewphysicalstates
t+1 ThelearningprocessusestheframeworkofVariationalAu-
andemitsarewardr t+1 basedonthetrue(butunknown) toencoder (VAE) [46]. We optimize the encoder network by
networkdynamics.
maximizingtheVariationalLowerBound(ELBO):
3) Belief Update: Upon observing the transition (cid:14)
(s t ,a t ,s t+1 ,r t+1 ), the agent updates its belief from ELBO=E ρ E q φ(m|τ :t) [logp θ(τ :H |m)]
t
b
h
t
e
to
ne
b
w
t+
e
1
vi
u
d
s
e
in
n
g
ce
B
in
ay
to
es
t
’
he
ru
a
le
g
.
en
T
t
h
’s
is
u
u
n
p
d
d
er
a
s
t
t
e
an
in
d
c
in
o
g
rp
o
o
f
ra
t
t
h
e
e
s −D
KL
(q φ(m|τ :t)||p θ(m))]. (11)
environment. Here,ρdenotesthetrajectorydistributioninducedbythecurrent
4) Transition: The system moves to the next hyper-state policy π and the initial state distribution ρ . This equation
0
s+ t+1 =(s t+1 ,b t+1 ). consistsoftwocomponents.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore. Restrictions apply.

HUANGetal.:EASTREAM:ANENVIRONMENT-AWAREADAPTIVEBITRATEALGORITHMFORRELIABLEVIDEOSTREAMINGSERVICES 1181
Fig. 2. Overall Architecture of the EAStream Framework. The system comprises two main modules: a Belief Inference Module responsible for learning
environmentalawareness,andaDRLPolicyModuleforadaptivedecision-making.
| The     | first  | is the reconstruction |                 | likelihood. |            | Crucially, | the     |     |     |     |     |     |     |     |
| ------- | ------ | --------------------- | --------------- | ----------- | ---------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- |
|         | p      |                       |                 |             |            |            | τ       |     |     |     |     |     |     |     |
| decoder | θ      | is tasked             | with predicting |             | the entire | trajectory | :H      |     |     |     |     |     |     |     |
| based   | on the | latent belief         | m.              | This forces | m          | to capture | the un- |     |     |     |     |     |     |     |
derlyingpredictivedynamicsofthenetwork,ratherthanmerely
compressinginteractionhistory.UsingtheMarkovproperty,this
likelihooddecomposesinto:
H(cid:2)−1
| logp | θ(τ | |m)= logp | θ(s |m)+ |     | [logp | θ(s | |s ,a ,m) |     |     |     |     |     |     |     |
| ---- | --- | --------- | -------- | --- | ----- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
|      | :H  |           | 0        |     |       | t+1 | t t       |     |     |     |     |     |     |     |
t=0
|     |     | +logp | θ(r | |s ,a | ,s    | ,m)]. |      |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | ----- | ----- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
|     |     |       |     | t+1 t | t t+1 |       | (12) |     |     |     |     |     |     |     |
Thisfactorizationallowsthemodeltoiterativelypredictthenext
Fig.3. ArchitectureoftheBeliefInferenceModule.
stateandrewardateachtimestep,enforcingaprecisemodeling
ofthestep-wisedynamics.
| The | second | component | is  | the KL | divergence, |     | which acts |     |     |     |     |     |     |     |
| --- | ------ | --------- | --- | ------ | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
asaregularizer.Itconstrainsthelearnedposteriorq φtoremain IV. SYSTEMDESIGN
closetothepriorp(m)(typicallyastandardGaussian),ensuring
|     |     |     |     |     |     |     |     | This section | details | the architecture |     | and | training | methodol- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ---------------- | --- | --- | -------- | --------- |
asmoothlatentspacethatfacilitatesstablepolicyoptimization.
|     |     |     |     |     |     |     |     | ogy of EAStream, |     | our proposed | meta-reinforcement |     |     | learning |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------ | ------------------ | --- | --- | -------- |
Basedontheinferredbelief,theDRLpolicyπ
|     |     |     |     |     |     | ψ isoptimized |     | frameworkforadaptivebitratestreaming. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
toapproximateaBayes-Optimalpolicy.Ateachtimestept,a
| latentvariablem |     | tissampledfromthecurrentbeliefdistribution, |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
m ∼q φ(m|τ
t :t).Thepolicythentakesthecurrentphysicalstate A. SystemArchitectureOverview
| s and | the | latent variable | as  | input, denoted |     | as π ψ(a | |s ,m t). |                                                   |     |     |     |     |     |     |
| ----- | --- | --------------- | --- | -------------- | --- | -------- | --------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| t     |     |                 |     |                |     |          | t t       | TheEAStreamframeworkconsistsoftwocoremodules:abe- |     |     |     |     |     |     |
Consequently,theagentcanadaptitsdecision-makingprocess
liefinferencemoduleresponsibleforenvironmentalawareness,
inresponsetotheestimatedhiddendynamics.
andapolicymodulefordecision-making.TheoverallEAStream
| The | overall | training | objective | is to | optimize | the | combined |     |     |     |     |     |     |     |
| --- | ------- | -------- | --------- | ----- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
architectureisillustratedinFig.2.
objective:
|     |     |     |     |     |     |     |     | The belief | inference | module | is  | designed | based | on the prin- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ------ | --- | -------- | ----- | ------------ |
L(φ,θ,ψ)=E [J(ψ,φ)+λ·ELBO(φ,θ)], ciples of VAE. It comprises two modules: a recurrent Be-
|     |     | p(M) |     |     |     |     | (13) |              |       |            |          |     |        |         |
| --- | --- | ---- | --- | --- | --- | --- | ---- | ------------ | ----- | ---------- | -------- | --- | ------ | ------- |
|     |     |      |     |     |     |     |      | lief Encoder | and a | predictive | Decoder. | The | Belief | Encoder |
whereE p(M) denotestheexpectationoverthetaskdistribution processes the agent’s historical interaction trajectory (τ t =
p(M).Inthisequation,J(ψ,φ)denotestheexpectedreturnfor (s ,a ,r ,...,s t))toinferalatentvariable,m.Thislatentvari-
0 0 1
m
approximate policy, and the second term is the task inference able represents its probabilistic belief regarding the hidden
objective.Thehyperparameterλcontrolsthetrade-offbetween characteristics of the current network conditions. The Belief
m.
maximizing the RL reward and the accuracy of belief recon- Encoder reconstructs the entire trajectory from the belief
m
struction. Predicting future trajectories enables belief to capture the
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.

1182 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.19,NO.2,MARCH/APRIL2026
r t:
|     |     |     |     |     |     |     | r =μ | ·q(R t)−μ | ·T  | −μ  | ·|q(R | t)−q(R | )|. |      |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------- | --- | --- | ----- | ------ | --- | ---- |
|     |     |     |     |     |     |     | t    | 1         | 2   | t   | 3     |        | t−1 | (16) |
Thisrewardfunctiondirectlyguidesthebehavioroftheagent.
|     |     |     |     |     |     |     | It enables             | agent to       | learn       | strategies | for | choosing | high-quality |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | -------------- | ----------- | ---------- | --- | -------- | ------------ | --- |
|     |     |     |     |     |     |     | chunks                 | while reducing | rebuffering |            | and | bitrate  | changes.     | The |
|     |     |     |     |     |     |     | weightingcoefficientsμ |                | ,μ          | ,μ         |     |          |              |     |
1 2 3 controlthebalance.
|     |     |     |     |     |     |     | C. NeuralNetworkArchitectures |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
TheproposedEAStreamframeworkconsistsoftwocompo-
nents:theBeliefInferenceModuleandtheDRLPolicyModule.
(cid:2)BeliefInferenceModule:AsshowninFig.3,thismoduleis
Fig.4. ArchitectureoftheDRLPolicyModule.
designedtoinferthecharacteristicsofthenetworkconditions,
|     |     |     |     |     |     |     | which contains | a recurrent |     | encoder | and | a predictive | decoder. |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | --- | ------- | --- | ------------ | -------- | --- |
TheEncodersequentiallyprocessestheinteractionhistory.For
| potential | dynamics | of  | the network | environment | rather | than |           |         |          |     |          |              |     |         |
| --------- | -------- | --- | ----------- | ----------- | ------ | ---- | --------- | ------- | -------- | --- | -------- | ------------ | --- | ------- |
|           |          |     |             |             |        |      | each time | step t, | tuple (a | ,r  | ,s t) is | first passed |     | through |
t−1 t
merelycompressingpastinformation.
|            |     |         |         |                      |     |            | their respective | fully        | connected |        | layers (FC), | then     | merged | into    |
| ---------- | --- | ------- | ------- | -------------------- | --- | ---------- | ---------------- | ------------ | --------- | ------ | ------------ | -------- | ------ | ------- |
| The second |     | part is | the DRL | strategy responsible |     | for action |                  |              |           |        |              |          |        |         |
|            |     |         |         |                      |     |            | a feature        | vector. This | feature   | vector | is           | then fed | into   | a Gated |
selection. The objective is to learn a near-optimal strategy RecurrentUnit(GRU)tocapturesequentialpatterns.Theoutput
| π(a |s ,m | t), which | takes | in the    | current state | and belief | and |        |                 |     |        |         |       |          |     |
| --------- | --------- | ----- | --------- | ------------- | ---------- | --- | ------ | --------------- | --- | ------ | ------- | ----- | -------- | --- |
| t t       |           |       |           |               |            |     | of GRU | is subsequently |     | passed | through | FC to | generate | the |
| outputs   | an action | that  | maximizes | the long-term | cumulative |     |        |                 |     |        |         |       |          |     |
parametersofaGaussiandistribution,representingtheposterior
| QoE reward. | Unlike | traditional |     | DRL-based | agents, our | policy | beliefm |     |     |     |     |     |     |     |
| ----------- | ------ | ----------- | --- | --------- | ----------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
t.TheDecoderprovidesthetrainingobjectivebyusing
| network | is conditional |     | on state | s and belief | m t. This | dual- |     |     |     |     |     |     |     |     |
| ------- | -------------- | --- | -------- | ------------ | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
t two separate networks to reconstruct the system’s dynamics.
input structure is the key to achieving adaptability. The state Specifically, consistent with the factorization of the trajectory
s t providesthemostrecentstateoftheenvironment,whilethe
likelihoodin(12),aStateTransitionHeadpredictsthenextstate
| belief m | provides | richer, | history-based | information |     | about the |                                                       |     |     |     |     |     |     |     |
| -------- | -------- | ------- | ------------- | ----------- | --- | --------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|          | t        |         |               |             |     |           | sˆt,whileaRewardHeadpredictstherewardrˆt.Bothheadsare |     |     |     |     |     |     |     |
environment.Thisallowsthepolicytolearnnotjustonefixed implementedasfullyconnectedlayers.
strategy,butahighlyadaptivemeta-policy. (cid:2)DRLPolicyModule:AsshowninFig.4,thismoduleisthe
|     |     |     |     |     |     |     | agent’s core | decision-making |     | component |     | and is | implemented |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --------------- | --- | --------- | --- | ------ | ----------- | --- |
B. State,Action,andRewardDefinition
withanActor-Criticarchitecture.ItbeginswithaFeatureExtrac-
torthatprocessestherawstate.Vector-basedinputs,including
| To train | the | DRL agent, | this | section explicitly | defines | the |                               |     |                                |     |     |     |              |     |
| -------- | --- | ---------- | ---- | ------------------ | ------- | --- | ----------------------------- | --- | ------------------------------ | --- | --- | --- | ------------ | --- |
|          |     |            |      |                    |         |     | thethroughputhistoryx(cid:10) |     | t,downloadtimehistoryτ(cid:10) |     |     |     | t,andthevec- |     |
rewardfunction,aswellasthestateandactionspace.
torofnextchunksizesn(cid:10)
(cid:2) State: For every time step t, the agent receives a state t,arefedintoone-dimensionalconvo-
s lutionallayerstocapturetemporalfeatures.Concurrently,scalar
| t. This | state | is a multi-dimensional |     | vector | that includes | in- |                                     |     |     |     |                    |     |     |     |
| ------- | ----- | ---------------------- | --- | ------ | ------------- | --- | ----------------------------------- | --- | --- | --- | ------------------ | --- | --- | --- |
|         |       |                        |     |        |               |     | inputs,includingthebufferoccupancyb |     |     |     | t,remainingchunksc |     |     |     |
formation about the playback status and network conditions. t,
FollowingthedesignofPensieve[8],weformulatethestates andthelastselectedbitratel t,areprocessedbydedicatedfully
t
connectedlayers.Thesefeaturesarethenconcatenatedwiththe
asfollows:
latentbeliefm
t.Theresultinghigh-dimensionalfeaturevector
|     |     | s =(x(cid:10) | ,τ(cid:10) ,n(cid:10) | ,b ,c ,l t). |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------- | --------------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t t t t t t (14) serves as the input to two independent networks. The Actor
Here,x(cid:10) tandτ(cid:10) tarevectorsrepresentingthehistoricalthroughput Network,amulti-layernetworkwithafinalSoftmaxactivation,
andtransmissiontimeofthepastwvideochunks(Wesetw mapsthesefeaturestoaprobabilitydistributioncorresponding
=8
|                                                    |     |     |     |     |                 |     | to the bitrates.                            | In  | parallel, | the Critic | Network |     | with a      | similar |
| -------------------------------------------------- | --- | --- | --- | --- | --------------- | --- | ------------------------------------------- | --- | --------- | ---------- | ------- | --- | ----------- | ------- |
| followingthestandardconfigurationin[8].);n(cid:10) |     |     |     |     | tdenotesthefile |     |                                             |     |           |            |         |     |             |         |
|                                                    |     |     |     |     |                 |     | architectureoutputsastatevalueestimationV(s |     |           |            |         |     | ,m          |         |
| sizeforKavailablebitratesofnextchunk;b             |     |     |     |     |                 |     |                                             |     |           |            |         |     | t t)toguide |         |
tisthecurrentbuffer
|            | c   |         |            |             |         |     | l thelearningoftheactor. |     |     |     |     |     |     |     |
| ---------- | --- | ------- | ---------- | ----------- | ------- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
| occupancy; | t   | denotes | the number | of unplayed | chunks; | and | t                        |     |     |     |     |     |     |     |
denotesthelastchunk’sbitrate.
(cid:2)Action:InanABRsystem,theagent’staskistoselectthe D. OfflineTrainingandOnlineAdaptation
video quality for the subsequent chunk. The action space A is Thissectiondetailsthelearningandadaptationworkflowof
thusformulatedasadiscreteset:
|     |     |     |     |     |     |     | EAStream. | The process | consists |     | of two | stages summarized |     | in  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | -------- | --- | ------ | ----------------- | --- | --- |
Algorithm1andAlgorithm2respectively.
|     |     | A={0,1,...,K−1}. |     |     |     | (15) |     |     |     |     |     |     |     |     |
| --- | --- | ---------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:2)
|     |     |     |     |     |     |     | Offline | Meta-Training: |     | This | stage | aims to | learn | a meta- |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --- | ---- | ----- | ------- | ----- | ------- |
Here, K represents the number of candidate bitrates. These policy capable of inferring environmental characteristics and
discreteoptionscorrespondtodifferentvideoresolutionssuch adapting decisions across diverse network conditions. By ex-
as360p,480p,720p,and1080p. posingtheagenttoawidevarietyofenvironmentsatthisstage,
(cid:2)Reward:TooptimizetheQoEobjectivein(5),wedefinethe weforceittolearnhowtoidentifypotentialnetworkconditions
| rewardfunctionr |     | accordingly.Oncethet-thvideochunkhas |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t rather than memorizing specific training trajectories. Further-
beensuccessfullytransmitted,theagentwillreceivearewardof more,EAStreamadoptsaseparatedoptimizationstrategy.This
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.

HUANGetal.:EASTREAM:ANENVIRONMENT-AWAREADAPTIVEBITRATEALGORITHMFORRELIABLEVIDEOSTREAMINGSERVICES 1183
Algorithm1:OfflineMeta-Training. Algorithm2:OnlineAdaptation.
1:Initializebeliefparamsφ,θ;policyparamsψ;entropy 1:Loadq φ andpolicyπ ψ.
weightα;targetentropyH ; 2:Initializerecurrenthiddenstateh .
target 0
2:InitializereplaybufferD belief ;lossweightsλ s ,λ r ,β. 3:fort=1,2,...,N do
3:foreachtrainingiterationdo 4: // Belief Inference
4: Collectabatchofrecenttrajectories{τ i }. 5: Updateh t ←RNNφ(h t−1 ,(a t−1 ,r t ,s t)).
5: Storetrajectories{τ i }inD belief . 6: Samplebelieffromencoderm t ∼q φ(h t).
6: //Update Policy Module 7: // Policy Decision
7: Computebeliefm tfor{τ i }usingfixedencoderq φ. 8: Observecurrentstates t.
8: UpdateψbyminimizingPPOloss: 9: Selectactiona t ∼π ψ(a t |s t ,m t).
L(ψ)=Eˆ t[−LCLIP(ψ)+LVF(ψ)−αH[π ψ](s t ,m t)] 10: // Environment Interaction
9: ComputeaverageentropyH¯ =Eˆ t[H[π ψ(·|s t ,m t)]] 11: Executea t,observes t+1 ,r t+1 .
10: Updateentropyweightα←α−(H¯ −H ) 12:endfor
target
11: //Update Belief Module
12: Sampleabatchoftrajectories{τ j }∼D belief .
13: Foreachτ j,inferlatentbeliefm j ∼q φ(m|τ j). aga C te ru d c t i o al t l h y e ,g b r e a l d ie ie f n m ts o f d r u o l m e. t T h h e e p e o n li c c o y d u e p r d a a n t d e d a e re co n d o e t r b ( a φ c , k θ p ) ro a p re -
14: // Calculate weighted loss
updatedindependentlybysamplingtrajectoriesfromaseparate
components
15: L state =−E j,t[logp θ(s j,t+1 |s j,t ,a j,t ,m j)]. replay buffer. The objective is to minimize the ELBO loss
16: L reward =−E j,t[logp θ(r j,t+1 |...,m j)]. derivedin(11),whichaggregatesthestatereconstructionloss,
17: L
KL
=E j[D
KL
(q φ(m|τ j)||p(m))]. reward prediction loss, and the KL divergence regularization
1 1 9 8: : L U E p L d B a O te = φ, λ θ s L by sta m te i + nim λ r iz L in re g wa L rd +β . L KL ter (cid:2) m. OnlineAdaptation:Whendeployedtotheclient,themodel
ELBO
willadaptonlineinthenewnetworkenvironment.Whenrunning
20:endfor
online,thereisnoneedforreal-timegradientupdatesortraining.
Theadaptabilityofpolicyisachievedentirelythroughreal-time
inference.
separationpreventsthebelieflearningfrombeingbiasedbythe
policy’searlyexploration.
Initially,thelatestinteractiontuple(a t−1 ,r t ,s t)isfedintothe
BeliefEncoderq φtoupdatetherecurrenthiddenstateh t.Given
In each training iteration, multiple parallel agents collect
thishiddenstate,theencoderperformsforwardpassingtoinfer
interactiontrajectories.Thecollecteddataisusedtoupdatethe
thebeliefm t.Thisbeliefrepresentstheagent’sperceptionofthe
policyandbeliefmodulesseparately.
currentnetworkenvironment.Thenthebeliefm tandthecurrent
The policy network is updated using the Proximal Policy
states tarejointlyinputintothepolicynetworkπ ψtodecidethe
Optimization(PPO)algorithm[47].Whileoff-policyalgorithms
next chunk’s bitrate a t. Finally, the agent performs the action
like SAC are known for high sample efficiency, we explicitly
andobservesthenewstateandreward.Duringtheentireonline
select the on-policy PPO to ensure training stability in our
phase,theauxiliarydecodermoduleisdeprecated,andtheagent
meta-learning framework. Since the Belief Encoder evolves
operatedinpureinferencemode.Unliketheoptimization-based
continuously, data stored in an off-policy replay buffer would
meta-learning methods that require gradient updates during
contain obsolete belief representations. PPO avoids this issue
testing, our method relies solely on forward propagation. This
by strictly learning from fresh trajectories consistent with the
structuraldesignreducescomputationaloverheadandmakesit
currentencoder.
moresuitableforresource-constrainedclientdeployments.
Weutilizetheclippedsurrogateobjectivetopreventdestruc-
tivelargeupdates:
V. EVALUATION
(cid:15) (cid:16)
LCLIP(ψ)=Eˆ t min r t(ψ)Aˆ t , A. ExperimentalSetup
(cid:17)(cid:18) (cid:2)Implementation:WeimplementEAStreaminPyTorchand
clip(r t(ψ),1−(cid:13),1+(cid:13))Aˆ t , (17) optimizethemodelparametersusingtheAdamoptimizer.For
thepolicyandvaluenetwork,thelearningrateissetto1×10−4.
wherer t(ψ)istheprobabilityratio,(cid:13)isahyperparameterusedto
The PPO algorithm is configured with a clipping parameter
limitthevariationoftheprobabilityratioandAˆ tistheadvantage of (cid:13)=0.2, a reward discount factor of γ =0.99 and a target
estimate.Toencourageexploration,weincorporateanautomatic entropyofH =0.1.Forbeliefinferencemodule(φ,θ),the
target
entropyadjustmentmechanism.Thefinalpolicylosscombines learningrateis1×10−3,anditistrainedusingareplaybuffer
the clipped loss, the value function loss LVF, and the entropy withacapacityof1000trajectoriesandabatchsizeof32.The
bonus: weightsforitslossfunctionaresettoλ
s
=1.0,λ
r
=1.0,and
(cid:14) (cid:19) β =0.1, respectively. The dimension of the latent belief m is
L(ψ)=Eˆ t −LCLIP(ψ)+LVF(ψ)−αH[π ψ](s t ,m t) . setto16.Theselectionofβ andmisfurtherjustifiedthrough
(18)
sensitivityanalysisinSectionV-C.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore. Restrictions apply.

1184 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.19,NO.2,MARCH/APRIL2026
(cid:2) Video Parameters: The video content selected for our TABLEI
experimentsisthe“EnvivioDash3”testsequence[48].Ithasa CHARACTERISTICSOFNETWORKTRACEDATASETS
totaldurationof193secondsandissegmentedinto48chunks,
| each with | a playback | time | of  | approximately |     | 4 seconds. | Each |     |     |     |     |     |
| --------- | ---------- | ---- | --- | ------------- | --- | ---------- | ---- | --- | --- | --- | --- | --- |
chunkispre-encodedintosixdifferentbitratelevelstofacilitate
adaptivestreaming:300,750,1200,1850,2850,and4300kbps.
| (cid:2) Baseline |     | Algorithms:    | We  | select    | several | state-of-the-art |     |     |     |     |     |     |
| ---------------- | --- | -------------- | --- | --------- | ------- | ---------------- | --- | --- | --- | --- | --- | --- |
| ABR algorithms   |     | that represent |     | different | design  | paradigms        | for |     |     |     |     |     |
comparison:
| (cid:2) |     |     |     |     |     |     |     |     |     | TABLEII |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
BOLA[16]:Abuffer-basedalgorithmbasedonLyapunov PARAMETERSFORDIFFERENTQOEMETRICS
optimization.Thisalgorithmensuresthatthevideoquality
ismaximizedwhileguaranteeingthestabilityofthebuffer.
(cid:2)
| FESTIVE |      | [5]: A       | rate-based | heuristic |     | algorithm.  | This al- |     |     |     |     |     |
| ------- | ---- | ------------ | ---------- | --------- | --- | ----------- | -------- | --- | --- | --- | --- | --- |
| gorithm | uses | the harmonic |            | average   | of  | the nearest | chunks   |     |     |     |     |     |
downloadratesforthroughputestimation.
(cid:2)
| RobustMPC |     | [7]: | An algorithm |     | based | on the | theory of |     |     |     |     |     |
| --------- | --- | ---- | ------------ | --- | ----- | ------ | --------- | --- | --- | --- | --- | --- |
MPC.Thisalgorithmpredictsthefutureoptimalsequence
| by  | combining | throughput |     | estimation | and | buffer | informa- |     |     |     |     |     |
| --- | --------- | ---------- | --- | ---------- | --- | ------ | -------- | --- | --- | --- | --- | --- |
tion.
(cid:2)
Pensieve[8]:Astate-of-the-artABRalgorithmleveraging
deepreinforcementlearning.
(cid:2)
| NetLLM | [33]: | The | first | framework | using | LLMs | for net- |     |     |     |     |     |
| ------ | ----- | --- | ----- | --------- | ----- | ---- | -------- | --- | --- | --- | --- | --- |
workingtasksthroughfine-tuningtoenhancegeneraliza-
tionandperformance. Fig.5. NormalizedaverageQoEcomparisononthein-distributionHybrid
(cid:2)
Comyco[9]:Aquality-awareABRmethodbasedonim- testset(3G,FCC,4GSyd).
| itation | learning. | It  | trains | the neural | network |     | by imitating |     |     |     |     |     |
| ------- | --------- | --- | ------ | ---------- | ------- | --- | ------------ | --- | --- | --- | --- | --- |
theexpertactions.
(cid:2)NetworkTraces:Torigorouslyevaluatealgorithmperfor-
|     |     |     |     |     |     |     |     | on network | conditions similar | to those | seen | during train- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------ | -------- | ---- | ------------- |
mance, we utilize network traces collected from a variety of ing. The 4G and Oboe datasets are kept entirely separate
NY
real-worldcommunicationdatasets.
(cid:2) from the training process. They serve exclusively as out-of-
3G[49]:Thisdatasetcomprisesthroughputmeasurements distributiontestsetstorigorouslyassessthegeneralizationca-
from3Gmobilenetworks,collectedonpublictransporta- pabilitiesofthepre-trainedmodelsincompletelynovelnetwork
| (cid:2) tionroutesinOslo,Norway. |     |     |     |     |     |     |     | environments. |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
FCC [50]: Sourced from broadband network traces re- (cid:2)QoEMetrics:Toevaluatethealgorithmperformancebased
leasedbytheU.S.FederalCommunicationsCommission
|     |     |     |     |     |     |     |     | on different | user preferences, | we adopted | two | distinct QoE |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------------- | ---------- | --- | ------------ |
(FCC),thesetracesareselectedfromthe“Webbrowsing” targetsfromPensieve[8].Forlearning-basedalgorithms(Pen-
category and are characterized by moderate bandwidth sieve,Comyco,NetLLMandEAStream),wetrainadedicated
conditions.
(cid:2) model for each QoE objective. The specific definition is as
| 4GSyd | [51]: | This | dataset | contains | traces | gathered | from | follows: |     |     |     |     |
| ----- | ----- | ---- | ------- | -------- | ------ | -------- | ---- | -------- | --- | --- | --- | --- |
(cid:2)
4GvehicularnetworksunderdrivingconditionsinSydney,
|            |     |     |     |     |     |     |     | QoE                            | lin This metric considers | that | the video | quality in- |
| ---------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | ------------------------- | ---- | --------- | ----------- |
| Australia. |     |     |     |     |     |     |     | creaseslinearlywiththebitrate. |                           |      |           |             |
| (cid:2)    |     |     |     |     |     |     |     | (cid:2)                        |                           |      |           |             |
Oboe [52]: This dataset contains traces from a commer- QoE This metric considers a higher bitrate to have
log
| cial | on-demand | music | video | service, |     | capturing | sessions |     |     |     |     |     |
| ---- | --------- | ----- | ----- | -------- | --- | --------- | -------- | --- | --- | --- | --- | --- |
diminishingreturnstoperceptualquality.
from a mix of users on both wired desktop and mobile TableIIprovidesasummaryoftheparametersusedforeach
| (WiFi/cellular)connections. |     |     |     |     |     |     |     | QoEmetric. |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
(cid:2)
| 4GNY   | [53]: | Collected | on       | New   | York City’s | public    | transit |     |     |     |     |     |
| ------ | ----- | --------- | -------- | ----- | ----------- | --------- | ------- | --- | --- | --- | --- | --- |
| system | (bus  | and       | subway), | these | traces      | represent | highly  |     |     |     |     |     |
B. EAStreamVs.ExistingABRAlgorithms
variableurbanmobilenetworkconditions.
We provide an overview of the primary characteristics for In this section, we compare EAStream with the baseline
thesedatasetsinTableI. algorithms. The test dataset includes in-distribution (Hybrid)
Fortrainingourlearning-basedmodels(EAStreamandPen- and out-of-distribution (Oboe, 4G NY ). We use bar charts to
sieve),wecreateasingle,unifieddatasettofostergeneralization. present the normalized average QoE scores in Figs. 5 and 6.
We combine the traces from the 3G, FCC, and 4G sources We analyzed the performance distribution using CDF plots in
Syd
toformaHybriddataset.FromthisHybriddataset,80%ofthe Figs.7,8,and9.
tracesarerandomlysampledtoconstitutethetrainingset. (cid:2)PerformanceontheHybridTestSet:Wefirstevaluatethe
The remaining 20% of the Hybrid dataset is held out as performance of all algorithms on the in-distribution test set,
the in-distribution test set, used to evaluate performance which is composed of traces from the 3G, FCC, and 4G
Syd
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.

HUANGetal.:EASTREAM:ANENVIRONMENT-AWAREADAPTIVEBITRATEALGORITHMFORRELIABLEVIDEOSTREAMINGSERVICES 1185
key finding is the performance of Pensieve. Pensieve demon-
strateddecentperformanceonthe4G dataset,butitdropped
Syd
significantly on the 4G dataset. This might be due to the
NY
highlyunstable4G trajectory(asshowninTable I),which
NY
suggestspoorgeneralizationofPensieve.Incontrast,EAStream
maintainsstableperformanceinbothin-distributionandout-of-
distributiontests.Thisgeneralizationperformancedemonstrates
theeffectivenessofourmeta-learningframeworkinlearningto
rapidlyadapttonetworkuncertainty.
Fig.6. NormalizedaverageQoEcomparisonontheout-of-distributiontest
sets(Oboe,4GNY).
C. EffectivenessAnalysis
(cid:2) Case Study: We synthesized a challenging trajectory by
datasets. Fig. 5 illustrates the normalized average QoE scores concatenating4G and3GsegmentstoevaluateEAStream’s
Syd
forbothQoE andQoE metrics. adaptabilityunderabruptnon-stationarychanges(e.g.,asharp
lin log
As shown in Fig. 5, our proposed EAStream consistently bandwidthdropat5s).
achieves the highest, or joint-highest, average QoE across all As shown in Fig. 10, EAStream achieved the highest QoE
three network conditions for both QoE and QoE metrics. (1.40),outperformingPensieve (1.21)andRobustMPC(1.07).
lin log
This demonstrates that EAStream can learn a highly effective While the sudden transition caused initial rebuffering for all
andstablepolicyevenwhentrainedonadiversehybriddataset. algorithms due to high-bitrate inertia, EAStream recovered
This is a notable advantage, as prior work [14] has shown most effectively. It rapidly detected the deterioration, down-
thatbaselineDRLagentslikePensievecansufferperformance shiftingto300kbpstostabilizeplaybackbeforesmoothlytran-
degradation when trained on mixed network conditions rather sitioning upward as buffers replenished. Conversely, Pensieve
thanasingleenvironment. and RobustMPC struggled with persistent rebuffering and fre-
For instance, in the low-bandwidth 3G and FCC dataset, quent switching. This confirms that EAStream’s environment-
EAStream outperforms the standard DRL method Pensieve awareness mechanism facilitates superior long-term decision-
and the recent LLM-based algorithm NetLLM. In the high- makingindynamicnetworks.
bandwidth 4GSyd scenario, EAStream achieves comparable (cid:2) Analysis of Latent Belief Space: We evaluated whether
performancetothestrongbaselineComyco.Thisbalancedsuc- EAStream’s belief module learns meaningful environmental
cesscontrastswithPensieve,whichperformsnotablyweakerin representations using t-SNE [54] visualization. Average 16-
thelow-bandwidthtraces.ThisgapsuggestsPensievemayhave dimensionalbeliefvectorswerecollectedfromtheQoE model
lin
over-specializedonthehigh-bandwidthtraceswithinthehybrid acrossthreedistinctdatasets:3G(lowbandwidth),4G (stable
Syd
dataset,whereasEAStreamlearnsamoreeffectivestrategythat highbandwidth),and4G (unstablehighbandwidth).
NY
mastersthefulltrainingdistribution. As shown in Fig. 11, the belief vectors form three distinct
The CDF plots in Fig. 7 and Fig. 8 provide a more detailed clusters corresponding to each environment. This separation
viewoftheperformancedistribution.Inallsubplots,EAStream demonstratesthatthemoduleeffectivelycapturesbothcoarse-
isconsistentlypositionedtotherightofallotheralgorithms.This grainedbandwidthlevelsandfine-grainedvolatilitydifferences
suggeststhatEAStreamnotonlyachievesahigheraverageQoE betweenthetwo4Gnetworks.Theseresultsvalidatethatlatent
butalsoprovidesamorestableexperienceforthevastmajority beliefs encode critical environmental dynamics, providing the
ofusers,minimizingthepoorexperiencesessions. necessaryawarenessforoptimaladaptivedecisions.
(cid:2) Generalization to Unseen Network Environments. To (cid:2)AblationandSensitivityAnalysis:Weconductablationand
evaluate the aspect of generalization, we now assess the per- sensitivitystudiestoevaluatetheimpactofthebeliefrepresen-
formance on two unseen (out-of-distribution, OOD) test sets: tation by varying the latent dimension and the KL coefficient
Oboeand4G .Thesenetworktraceswerenotexposedtoany usingthe3Gdataset.Specifically,adimensionof0represents
NY
learning-basedmodelsduringthetrainingphase. thebaselinemodelwherethebeliefmoduleisentirelyremoved.
Fig.6illustratesthenormalizedaverageQoEscoresforboth AsshowninFig.12(a),theagentachievesthebestperformance
QoE metrics on these two unseen datasets. The results clearly with a dimension of 16, outperforming the baseline model
demonstratethesuperiorgeneralizationcapabilityofEAStream. withouttheBeliefmodule.Thisprovestheeffectivenessofthe
Inallfourscenarios,EAStreamachievedthehighestornearly Beliefmodule.Meanwhile,whenthedimensionistoosmall,the
the highest average QoE. Specifically, its performance on the latentvectorlacksthecapacitytosufficientlyencodecomplex
Oboe dataset outperforms all other algorithms, including the networkdynamics.Conversely,adimensionlargerthan16leads
strong baseline Comyco. It also achieves top-tier performance toperformancedegradation,likelyduetoincreasedoptimization
onthe4GNYdataset,comparabletoComycoandsignificantly difficulty.
betterthanPensieveandNetLLM. Similarly, we test the sensitivity to the KL coefficient β, as
In all four CDF subplots in Fig. 9, EAStream has excel- showninFig.12(b).Asmallβmakesthelatentspaceirregular
lent performance compared with other baseline algorithms. A and hurts performance. If β is too large, the belief becomes
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore. Restrictions apply.

1186 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.19,NO.2,MARCH/APRIL2026
| Fig.7. CDFofQoE | scoresonthein-distributionHybridtestset(3G,FCC,4GSyd). |     |     |
| --------------- | ------------------------------------------------------ | --- | --- |
lin
scoresonthein-distributionHybridtestset(3G,FCC,4GSyd).
| Fig.8. CDFofQoE | log |     |     |
| --------------- | --- | --- | --- |
Fig.9. CDFofQoEscoresontheout-of-distributiontestsets(Oboeand4GNy).
Fig.11. t-SNEvisualizationofthelatentbeliefvectorscollectedfromthree
| Fig. 10. Bitrate | selection of EAStream, | Pensieve, and RobustMPC | on the |
| ---------------- | ---------------------- | ----------------------- | ------ |
distinctnetworkdatasets.
bandwidthdroptrace.
(cid:2)OverheadAnalysis:TotesttheoverheadofEAStream,we
| uninformative | due to over-regularization, | known as | posterior |
| ------------- | --------------------------- | -------- | --------- |
collapse.Theresultsconfirmthatamoderatelatentdimension conductedaquantitativeanalysisofitscomputationaloverhead
andKLcoefficientprovidethebestbalanceforthelatentbelief and memory usage. We compared EAStream with Pensieve,
representation. RobustMPC and NetLLM. The experiments were carried out
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.

HUANGetal.:EASTREAM:ANENVIRONMENT-AWAREADAPTIVEBITRATEALGORITHMFORRELIABLEVIDEOSTREAMINGSERVICES 1187
|     |     |     |     |     |     |     |     | EAStream | infers | latent | beliefs | about network |     | dynamics | from |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------ | ------- | ------------- | --- | -------- | ---- |
interactionhistory.Thismechanismenablesthepolicytoachieve
|     |     |     |     |     |     |     |     | zero-shot | adaptation | to  | unseen | network | conditions | without | re- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ------ | ------- | ---------- | ------- | --- |
quiringcomputationallyexpensiveonlinefine-tuning.Extensive
experimentsonreal-worlddatasetsdemonstratethatEAStream
notonlymatchesstate-of-the-artperformanceonin-distribution
tracesbutsignificantlyoutperformsexistingbaselinesinout-of-
distributionscenarios.Infuturework,weintendtoexplorethe
onlineutilizationoftheBeliefDecoder,whichiscurrentlyonly
reservedforofflinetraining.Specifically,weplantoleveragethe
Fig.12. Ablationstudiesonthelatentbeliefrepresentation.
real-timereconstructionerrorsforanomalydetectiontoidentify
extremenetworkoutliers.
TABLEIII
RESOURCECONSUMPTIONANDINFERENCELATENCYCOMPARISON
REFERENCES
|     |     |     |     |     |     |     |     | [1] Sandvine, | “2024                                                   | Global | internet | phenomena | report,” | 2024. | [Online]. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------------------------------------------------- | ------ | -------- | --------- | -------- | ----- | --------- |
|     |     |     |     |     |     |     |     | Available:    | https://www.applogicnetworks.com/global-internet-phenom |        |          |           |          |       |           |
ena-report-2024
[2] G.V.Research,“Videostreamingmarketsizetoreach416.84billionby
|     |     |     |     |     |     |     |     | 2030,” | 2024. | [Online]. | Available: | https://www.grandviewresearch.com/ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | --------- | ---------- | ---------------------------------- | --- | --- | --- |
press-release/global-video-streaming-market
[3] T.Stockhammer,“DynamicadaptivestreamingoverHTTP–Standards
anddesignprinciples,”inProc.2ndAnnu.ACMConf.MultimediaSyst.,
2011,pp.133–144.
[4] R.PantosandW.May,“HTTPlivestreaming,”RFC8216,Aug.2017.
| on a server | equipped | with | an  | Intel i9-13900 | K   | CPU and | were |     |     |     |     |     |     |     |     |
| ----------- | -------- | ---- | --- | -------------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
[Online].Available:https://www.rfc-editor.org/info/rfc8216
runinasingle-threadedmode.
|     |     |     |     |     |     |     |     | [5] J. Jiang, | V. Sekar, | and | H. Zhang, | “Improving | fairness, | efficiency, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | --------- | ---------- | --------- | ----------- | --- |
As shown in Table III, the overhead of introducing the Be- stabilityinHTTP-basedadaptivevideostreamingwithfestive,”inProc.
lief module is extremely small (0.0224 MFLOPs). Although 8thInt.Conf.Emerg.Netw.ExperimentsTechnol.,2012,pp.97–108.
|     |     |     |     |     |     |     |     | [6] T.-Y. | Huang, | R. Johari, | N. McKeown, | M.  | Trunnell, | and | M. Watson, |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ---------- | ----------- | --- | --------- | --- | ---------- |
it is slightly higher than Pensieve, the total inference latency “A buffer-based approach to rate adaptation: Evidence from a large
of EAStream is only 0.2258 milliseconds. For a video chunk videostreamingservice,”inProc.2014ACMConf.SIGCOMM,2014,
| durationof4seconds,ouralgorithmaccountsforonly0.0056% |     |     |     |     |     |     |     | pp.187–198. |     |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
[7] X.Yin,A.Jindal,V.Sekar,andB.Sinopoli,“Acontrol-theoreticapproach
of it. EAStream’s speed is significantly faster than the widely fordynamicadaptivevideostreamingoverHTTP,”inProc.2015ACM
used RobustMPC (3.1315 milliseconds), and much faster than Conf.SpecialInt.GroupDataCommun.,2015,pp.325–338.
[8] H.Mao,R.Netravali,andM.Alizadeh,“Neuraladaptivevideostreaming
NetLLM.ThisconfirmsthatEAStreamissuitableforresource-
withpensieve,”inProc.Conf.ACMSpecialInt.GroupDataCommun.,
constrainedclientdeployments.
2017,pp.197–210.
[9] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,X.Yao,andL.Sun,“COMYCO:
Quality-awareadaptivevideostreamingviaimitationlearning,”inProc.
D. DiscussionandLimitations
27thACMInt.Conf.Multimedia,2019,pp.429–437.
|     |     |     |     |     |     |     |     | [10] F. Y. | Yan et | al., “Learning | in situ: | A randomized |     | experiment | in video |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | -------------- | -------- | ------------ | --- | ---------- | -------- |
Despite the demonstrated advantages, we acknowledge cer- streaming,”inProc.17thUSENIXSymp.Netw.Syst.Des.Implementation,
tain limitations of the EAStream framework. First, the offline 2020,pp.495–511.
meta-training process incurs higher computational overhead [11] H.Zhangetal.,“LOKI:Improvinglongtailperformanceoflearning-based
real-timevideoadaptationbyfusingrule-basedmodels,”inProc.27th
comparedtostandardDRLmethodsduetothejointoptimization
Annu.Int.Conf.MobileComput.Netw.,2021,pp.775–788.
of the belief inference and policy modules. However, this cost [12] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, and L. Sun, “Learning tai-
loredadaptivebitratealgorithmstoheterogeneousnetworkconditions:A
| is strictly | confined | to the | offline | phase | and | does not | impact |     |     |     |     |     |     |     |     |
| ----------- | -------- | ------ | ------- | ----- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
domain-specificpriorsandmeta-reinforcementlearningapproach,”IEEE
| the low-latency |     | requirements |     | of online | inference. | Second, | the |     |     |     |     |     |     |     |     |
| --------------- | --- | ------------ | --- | --------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
J.Sel.AreasCommun.,vol.40,no.8,pp.2485–2503,Aug.2022.
algorithm’sgeneralizationcapabilityisinherentlydependenton
|               |     |             |        |      |        |                |     | [13] S. Wang, | J.  | Lin, and | Y. Dai, “MMVS: | Enabling          | robust | adaptivevideo |      |
| ------------- | --- | ----------- | ------ | ---- | ------ | -------------- | --- | ------------- | --- | -------- | -------------- | ----------------- | ------ | ------------- | ---- |
|               |     |             |        |      |        |                |     | streaming     | for | wildly   | fluctuating    | and heterogeneous |        | networks,”    | IEEE |
| the diversity | of  | the network | traces | used | during | meta-training; |     |               |     |          |                |                   |        |               |      |
Trans.Multimedia,vol.26,pp.11018–11030,2024.
| a narrow | task | distribution | may | limit | the effective | range | of  |     |     |     |     |     |     |     |     |
| -------- | ---- | ------------ | --- | ----- | ------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[14] W.Li,X.Li,Y.Xu,Y.Yang,andS.Lu,“MetaABR:Ameta-learning
adaptation. Finally, in extreme outlier scenarios that deviate approachonadaptativebitrateselectionforvideostreaming,”IEEETrans.
significantly from the training distribution, the inferred belief MobileComput.,vol.23,no.3,pp.2422–2437,Mar.2024.
|     |     |     |     |     |     |     |     | [15] M. O. | Duff, | “Optimal | Learning: | Computational | procedures |     | for Bayes- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | -------- | --------- | ------------- | ---------- | --- | ---------- |
maybecomeinaccurate.AsnotedinSectionVI,leveragingthe
|     |     |     |     |     |     |     |     | adaptive | Markov | decision | processes,” | Univ. | Massachusetts |     | Amherst, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | -------- | ----------- | ----- | ------------- | --- | -------- |
reconstruction error for anomaly detection offers a promising Amherst,MA,USA,2002.
avenuetomitigatethisissueinfuturework. [16] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal
bitrateadaptationforonlinevideos,”IEEE/ACMTrans.Netw.,vol.28,
no.4,pp.1698–1711,Aug.2020.
VI. CONCLUSION [17] J. Chen, Y. Yu, L. Wang, Y. Chen, T. Huang, and L. Sun, “En-
|     |     |     |     |     |     |     |     | hanced | bandwidth | measurement |     | and robust | rate | adaptation | for low- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ----------- | --- | ---------- | ---- | ---------- | -------- |
This paper presents EAStream, a context-based meta- latencylivestreaming,”inProc.IEEEConf.Comput.Commun.,2025,
| reinforcementlearningframeworkdesignedtoaddressthegen- |     |     |     |     |     |     |     | pp.1–10. |     |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
[18] Y.Qinetal.,“AcontroltheoreticapproachtoABRvideostreaming:A
eralizationchallengeinadaptivebitratestreaming.Bymodeling freshlookatPID-basedrateadaptation,”IEEETrans.MobileComput.,
theproblemasaBAMDPandutilizingavariationalautoencoder, vol.19,no.11,pp.2505–2519,Nov.2020.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore.  Restrictions apply.

1188 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.19,NO.2,MARCH/APRIL2026
[19] T.Huang,X.Yao,C.Wu,R.-X.Zhang,Z.Pang,andL.Sun,“Tiyuntsong: [46] D.P.KingmaandM.Welling,“Auto-encodingvariationalBayes,”2013,
Aself-playreinforcementlearningapproachforabrvideostreaming,”in arXiv:1312.6114.
Proc.2019IEEEInt.Conf.MultimediaExpo.,2019,pp.1678–1683. [47] J.Schulman,F.Wolski,P.Dhariwal,A.Radford,andO.Klimov,“Proximal
[20] P.K.Mu,J.Zheng,T.H.Luan,L.Zhu,M.Dong,andZ.Su,“AMIS:Edge policyoptimizationalgorithms,”2017,arXiv:1707.06347.
computingbasedadaptivemobilevideostreaming,”inProc.IEEEConf. [48] “EnvivioDash3,” 2016. [Online]. Available: https://dash.akamaized.net/
Comput.Commun.,2021,pp.1–10. envivio/EnvivioDash3/
[21] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,andL.Sun,“Bufferawareness [49] H.Riiser,P.Vigmostad,C.Griwodz,andP.Halvorsen,“Commutepath
neuraladaptivevideostreamingforavoidingextrabufferconsumption,” bandwidthtracesfrom3Gnetworks:Analysisandapplications,”inProc.
inProc.IEEEConf.Comput.Commun.,2023,pp.1–10. 4thACMMultimediaSyst.Conf.,2013,pp.114–118.
[22] B.O.Turkkanetal.,“GreenABR:Generalizedenergy-awareadaptive [50] FederalCommunicationsCommission,“Rawdata-measuringbroadband
bitrate streaming,” ACM Trans. Multimedia Comput., Commun. Appl., America2016,”Dec.2016.Accessed:Oct.16,2025.[Online].Available:
vol.20,no.9,pp.1–24,2024. https://www.fcc.gov/reports-research/reports/measuring-broadband-
[23] H.Su,S.Wang,S.Yang,T.Huang,andX.Ren,“Reducingtrafficwastage america/raw-data-measuring-broadband-america-2016
invideostreamingviabandwidth-efficientbitrateadaptation,”IEEETrans. [51] A.Bokani,M.Hassan,S.S.Kanhere,J.Yao,andG.Zhong,“Comprehen-
MobileComput.,vol.23,no.11,pp.10361–10377,Nov.2024. sivemobilebandwidthtracesfromvehicularnetworks,”inProc.7thInt.
[24] Y.Guo,F.R.Yu,J.An, K.Yang, C.Yu,andV.C.Leung,“Adaptive Conf.MultimediaSyst.,2016,pp.1–6.
bitratestreaminginwirelessnetworkswithtranscodingatnetworkedge [52] Z.Akhtaretal.,“OBOE:Auto-tuningvideoABRalgorithmstonetwork
usingdeepreinforcementlearning,”IEEETrans.Veh.Technol.,vol.69, conditions,”inProc.2018Conf.ACMSpecialInt.GroupDataCommun.,
no.4,pp.3879–3892,Apr.2020. 2018,pp.44–58.
[25] X. Ma et al., “QAVA: QoE-Aware adaptive video bitrate aggregation [53] L.Meietal.,“RealtimemobilebandwidthpredictionusingLSTMneu-
forHTTPlivestreamingbasedonsmartedgecomputing,”IEEETrans. ralnetworkandBayesianfusion,”Comput.Netw.,vol.182,2020,Art.
Broadcast.,vol.68,no.3,pp.661–676,Sep.2022. no.107515.
[26] W. Li et al., “Optimizing video streaming in dynamic networks: An [54] L.v.d.MaatenandG.Hinton,“VisualizingdatausingT-SNE,”J.Mach.
intelligentadaptivebitratesolutionconsideringsceneintricacyanddata Learn.Res.,vol.9,Nov.,pp.2579–2605,2008.
budget,”IEEETrans.MobileComput.,vol.23,no.12,pp.12280–12297,
Dec.2024.
[27] Y.Zhao,Q.-W.Shen,W.Li,T.Xu,W.-H.Niu,andS.-R.Xu,“Latency
awareadaptivevideostreamingusingensembledeepreinforcementlearn- ZemingHuangreceivedtheBSdegreeininforma-
ing,”inProc.27thACMInt.Conf.Multimedia,2019,pp.2647–2651. tionandcomputingsciencefromtheNanjingUni-
[28] G.Xiao,M.Wu,Q.Shi,Z.Zhou,andX.Chen,“DeepVR:Deepreinforce- versityofPostsandTelecommunications,Nanjing,
ment learning for predictive panoramic video streaming,” IEEE Trans. China,in2023.Heiscurrentlyworkingtowardthe
Cogn.Commun.Netw.,vol.5,no.4,pp.1167–1177,Dec.2019. MSdegreeinelectronicinformation(computertech-
[29] L.Yang,G.Liu,S.Li,J.Zhao,andT.Jiang,“Environmentinformation nology) with the School of Computer, Electronics
enhancedneuraladaptivebitratevideostreamingforintercityrailway,” andInformation,GuangxiUniversity,Nanning.His
IEEETrans.Broadcast.,vol.71,no.3,pp.849–861,Sep.2025. researchinterestsincludeadaptivevideostreaming,
[30] E.R.Peretto,M.N.R.SoaresFilho,D.C.S.Sousa,L.P.Gaspary,andB. deepreinforcementlearning,andmeta-learning.
I.Grisci,“TowardsanMLassisteddash-basedarchitecture:Leveraging
predictivenetworkanalyseswithinterpretability,”inProc.21stInt.Conf.
Netw.Serv.Manage.,2025,pp.1–7.
[31] L.Jiaetal.,“Beyondinterpretability:Exploringthecomprehensibilityof Wenjing Xiao received the bachelor-straight-to-
adaptivevideostreamingthroughlargelanguagemodels,”inProc.33rd doctoratedegreefromEmbeddedandPervasiveCom-
ACMInt.Conf.Multimedia,2025,pp.12035–12044. putingLab,SchoolofComputerScienceandTech-
[32] M.Chenetal.,“NeuroBA:Neuro-symbolicbitrateadaptationforirs-aided nology,HuazhongUniversityofScienceandTech-
mobilevideostreaming,”IEEETrans.Netw.,vol.34,pp.2558–2572,2026. nology,Wuhan,China.Sheiscurrentlyanassistant
[33] D.Wuetal.,“NetLLM:Adaptinglargelanguagemodelsfornetworking,” professor with the School of Computer and Elec-
inProc.ACMSIGCOMM2024Conf.,2024,pp.661–678. tronicInformation,GuangxiUniversity,China.Her
[34] T.Hospedales,A.Antoniou,P.Micaelli,andA.Storkey,“Meta-learning researchinterestsincludecloudcomputing,Internet
inneuralnetworks:Asurvey,”IEEETrans.PatternAnal.Mach.Intell., ofThings,andcognitivecomputing.
vol.44,no.9,pp.5149–5169,Sep.2022.
[35] J.Becketal.,“Atutorialonmeta-reinforcementlearning,”Found.Trends
Mach.Learn.,vol.18,no.2/3,pp.224–384,2025.
[36] C.Finn,P.Abbeel,andS.Levine,“Model-agnosticmeta-learningforfast
adaptation of deep networks,” in Proc. Int. Conf. Mach. Learn., 2017, MiaojiangChen(Member,IEEE)receivedthePhD
pp.1126–1135. degreeincomputersciencefromCentralSouthUni-
[37] A. Nichol, J. Achiam, and J. Schulman, “On first-order meta-learning versity, in 2023. He is currently an associate pro-
algorithms,”2018,arXiv:1803.02999. fessorwiththeSchoolofComputerandElectronic
[38] A.NicholandJ.Schulman,“Reptile:Ascalablemetalearningalgorithm,” Information,GuangxiUniversity,China.Hehasau-
2018,arXiv:1803.02999. thoredorcoauthoredseveraljournalandconference
[39] A.A.Rusuetal.,“Meta-learningwithlatentembeddingoptimization,”in papers in the IEEE Journal on Selected Areas in
Proc.Int.Conf.Learn.Representations(ICLR),2018,pp.1–13. Communications, IEEE Transactions on Network-
[40] Y.Duan,J.Schulman,X.Chen,P.L.Bartlett,I.Sutskever,andP.Abbeel,
ing,IEEETransactionsonMobileComputing,IEEE
“Rl2:Fastreinforcementlearningviaslowreinforcementlearning,”2016, Transactions on Services computing, AAAI, IEEE
arXiv:1611.02779. TransactionsonIntelligentTransportationSystems,
[41] K.Rakelly,A.Zhou,C.Finn,S.Levine,andD.Quillen,“Efficientoff-
IEEETransactionsonNetworkScienceandEngineering,IEEETransactions
policymeta-reinforcementlearningviaprobabilisticcontextvariables,”in
on Emerging Topics in Computational Intelligence, IEEE Transactions on
Proc.Int.Conf.Mach.Learn.,2019,pp.5331–5340. ConsumerElectronics,Knowledge-BasedSystems,ACMTransactionsonAu-
[42] A.-M. K. Pathan et al., “A taxonomy and survey of content delivery
tonomousandAdaptiveSystems,andACMTransactionsonMultimediaCom-
networks,”GridComput.Distrib.Syst.Lab.,Univ.Melbourne,Parkville,
putingCommunicationsandApplications.Hisresearchinterestsincludedeep
VIC,Australia,Tech.Rep.,vol.4,no.2007,p.70,2007. reinforcementlearning,InternetofThings,edgecomputing,transferlearning,
[43] M.Strens,“ABayesianframeworkforreinforcementlearning,”inProc. andoptimization.Heisalsoreviewerofthetop-tierconferencesandjournals,
Int.Conf.Mach.Learn.,2000,pp.943–950. includingICML,IEEETransactionsonParallelandDistributedSystems,IEEE
[44] A.Guez,D.Silver,andP.Dayan,“EfficientBayes-adaptivereinforcement
TransactionsonInformationForensicsandSecurity,IEEETransactionsonIn-
learningusingsample-basedsearch,”inProc.Adv.NeuralInf.Process. dustrialInformatics,IEEETransactionsonIntelligentTransportationSystems,
Syst.,vol.25,2012,pp.1–9. IEEEInternetofthingsjournal.HewastherecipientoftheIEEEHITC2025
[45] L.Zintgrafetal.,“Varibad:AverygoodmethodforBayes-adaptivedeep AwardforExcellenceinHyper-Intelligence(EarlyCareerResearchers),and
RLviameta-learning,”inProc.Int.Conf.Learn.Representations(ICLR), YoungTalentsoftheGuangxiHigh-LevelPersonnelSpecialSupportProgram.
2019,pp.1–14.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore. Restrictions apply.

HUANGetal.:EASTREAM:ANENVIRONMENT-AWAREADAPTIVEBITRATEALGORITHMFORRELIABLEVIDEOSTREAMINGSERVICES 1189
ZhiquanLiureceivedtheBSdegreefromtheSchool AhmedFaroukiscurrentlyanassociateprofessor
ofScience,XidianUniversity,Xi’an,China,in2012, with the Faculty of Computers and Artificial In-
andthePhDdegreefromtheSchoolofComputerSci- telligence, Hurghada University, Egypt. He is also
enceandTechnology,XidianUniversity,in2017.He an early career scientist demonstrating excellence
iscurrentlyafullprofessorwiththeCollegeofCyber inquantumcommunication,cryptography,machine
Security, Jinan University, Guangzhou, China. His learning,andcybersecurityresearch.Hehasauthored
researchinterestsincludesecurity,trust,andprivacy or coauthored more than 100 research papers with
invehicularnetworks.Heisalsoanassociateeditors highimpact.HewastherecipientofthetheEgyptian
forIEEETransactionsonInformationForensicsand StateEncouragementAwardinadvancedtechnolog-
Security,IEEETransactionsonIndustrialInformat- icalsciences,theUniversityEncouragementAward
ics,IEEEInternetofThingsJournal,IEEENetwork, inBasicSciencesandEngineering,Prof.Dr.Tarek
andComputerNetworks,andtheeditor-in-chiefofAdvancesinTransportation KamelAwardinCommunicationsandInformationTechnology,andmanymore.
andLogistics. Hehasalsobeenselectedasoneof17researchersfromAfricatoparticipatein
theprestigiousLindauNobelLaureateMeetings,chosenbytheU.S.National
AcademyofSciencestoparticipateinthe2ndand3rdU.S.-AfricaFrontiersof
Science,Engineering,andMedicinesymposiumandhisworkbeenrecognized
asoneofStanford’sWorldTop2%scientists.Hewasalsotherecipientofthe
travelandentiregrantsfromtheIEEEComputerSociety,LindauFoundation,
Baden-Württemberg International, U.S. National Academy of Sciences and
OkinawaInstituteofScienceandTechnology.HehasalsochairedtheIEEE
Min Chen (Fellow, IEEE) is currently a full pro- Computer Society Chapter and was elected as an officer for the Consumer
fessor with the School of Computer Science and Technology Society (CTSoc) on Quantum Consumer Technology Technical
Engineering,SouthChinaUniversityofTechnology, Committee(QCT).
Guangzhou, China. He was an assistant professor
withtheSchoolofComputerScienceandEngineer-
ing,SeoulNationalUniversity,Seoul,SouthKorea.
He is also the director with Embedded and Perva-
siveComputingLaboratory,HuazhongUniversityof
Science and Technology, Wuhan, China. He is the
founding chair of IEEE Computer Society Special
Technical Communities on Big Data, and was the Houbing Herbert Song (Fellow, IEEE) received
chair of IEEE Globecom in 2022 eHealth Symposium. His Google Scholar the PhD degree in electrical engineering from the
citationsreachedmorethan40,500withanH-indexof95.Histoppaperwas UniversityofVirginia,Charlottesville,VA,USA,in
citedmorethan4,100times.From2018to2022,hewasselectedashighlycited 2012.Heiscurrentlyatenuredassociateprofessor,
researcher. He was the recipient of the IEEE Communications Society Fred the director with the NSF Center for Aviation Big
W.EllersickPrizein2017,IEEEJackNeubauerMemorialAwardin2019,and DataAnalytics(Planning),andassociatedirectorwith
IEEEComSocAPBOustandingPaperAwardin2022. Leadership of the DoT Transportation Cybersecu-
rity Center for Advanced Research and Education,
UniversityofMaryland,BaltimoreCounty(UMBC),
Baltimore,MD,USA.Hewasanassociatetechnical
editorofIEEECommunicationsMagazine,guested-
itorofIEEEJournalonSelectedAreasinCommunications,andanassociate
editorforIEEETransactionsonArtificialIntelligence,IEEEInternetofThings
Journal,IEEETransactionsonIntelligentTransportationSystems,andIEEE
Athanasios V. Vasilakos (Senior Member, IEEE) JournalonMiniaturizationforAirandSpaceSystems.Hisresearchinterests
iscurrentlywiththeCenterforAIResearch,UiA, include cyber-physical systems, Big Data analytics, and Internet of Things.
and also with the European Academy of Sciences He has been a Highly Cited Researcher identified by Clarivate and a Top
andArts(electedrecentlyDeanoftheClassVI).He 1000 Computer Scientist identified by Research.com. He was a recipient of
wasorisastheeditorformanytechnicaljournals, 10+BestPaperAwardsfrommajorinternationalconferences,includingIEEE
such as IEEE Transactions on AI, IEEE Transac- CPSCom2019,IEEEICII2019,IEEE/AIAAICNS2019,IEEECBDCom2020,
tions on Network and Service Management, IEEE WASA2020,AIAA/IEEEDASC2021,IEEEGLOBECOM2021,andIEEE
Transactions on Cloud Computing, IEEE Transac- INFOCOM2022.HeisalsoanACMdistinguishedmember,ACMdistinguished
tions on Information Forensics and Security, IEEE speaker,andIEEEVehicularTechnologySocietyDistinguishedLecturer.
TransactionsonCybernetics,IEEETransactionson
Nanobioscience,IEEETransactionsonInformation
TechnologyinBiomedicine,ACMTransactionsonAutonomousandAdaptive
Systems,IEEEJournalonSelectedAreasinCommunications.Heisalsothe
WoShighlycitedresearcher.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:39:45 UTC from IEEE Xplore. Restrictions apply.