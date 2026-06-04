12852 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.24,NO.12,DECEMBER2025
A Novel Spatial-Temporal Learning Method for
Enhancing Generalization in Adaptive
Video Streaming
GuanghuiZhang ,ZimingWang ,HuarenWei,MengbaiXiao ,HuiYuan ,SeniorMember,IEEE,
DongxiaoYu ,SeniorMember,IEEE,andXiuzhenCheng ,Fellow,IEEE
Abstract—Adaptivevideostreaminghasbecomeafundamental Internet.AsreportedbyCisco,globalvideostreamingtraffichas
technologyforvideodelivery.Withtheriseofdeepreinforcement surgedbyafactorof15overthepastfiveyearsandnowaccounts
learning(DRL),streamingvendorsareincreasinglyadoptingDRL-
forover80%oftheInternettraffic[1].
driven adaptive bitrate (ABR) algorithms. In real-world deploy-
However, the highly variable nature of the mobile networks
ments,mostABRapproachesaredevelopedwiththeaimofmain-
taininggoodperformanceacrossawidevarietyofnetworkenviron- (primarily caused by unstable radio signals) poses a major
ments.However,contrarytothisexpectation,ourempiricalfind- obstacle to video streaming. Smooth playback relies on stable
ingsshowthatevenwhentrainedonextensivereal-worldnetwork and consistent network throughput, which is difficult to main-
tracedata,theseDRL-basedABRalgorithmsachieveonly43.1%
tain in such dynamic environments. To tackle this issue, the
to 48.9% of Quality-of-Experience (QoE) under highly diverse
streamingvendorshaveturnedtheirattentiontoadaptivebitrate
networkconditions,whichfallssignificantlyshortofthe100%op-
timum.Wetermedthisproblemas“ABRUnder-Generalization”. (ABR)algorithms,aimingtoalleviatethenegativeeffectsofthe
To overcome this problem, we introduce BETA – a novel DRL- throughputfluctuations.TheseABRalgorithmsaretypicallyim-
basedABRframeworkthatincorporatesbothspatialandtemporal plementedundertheDASHprotocol[2].Theirkeycomponent
learningmechanisms:1)Spatially,BETAfeaturesadetectorthat
is an adaptive logic, which intelligently adjusts video quality
flags the network conditions likely to cause poor performance,
inrealtime(byselectingappropriatebitrates)basedonseveral
then trains specialized ABR models tailored for those conditions
and2)Temporally,BETAenhancesitslearningbyincorporating streaming metrics such as historical throughput measurements
multi-stepdecisionexperiencesateachtrainingepoch,enablingthe andcurrentbufferstatus.Theobjectiveistoenhancetheviewer’s
trainedmodeltoaccountforlong-termenvironmentaldynamics. QualityofExperience(QoE).
ComprehensiveevaluationsshowthatBETAoutperformsstate-of-
Most ABR algorithms are developed with the intention to
the-artABRalgorithms,yieldingaverageQoEgainsof19.4%to
perform reliably across the wide network environments of
50.9%,andachievingimprovementsofupto244.1%underseverely
fluctuatingnetworkconditions. any size and shape, e.g., from 3G networks with peak band-
widths of a few Mbps to 5G networks offering mean band-
Index Terms—Video streaming, mobile network, deep widths of 100+ Mbps. However, real-world experiments con-
reinforcementlearning,quality-of-experience.
sistently demonstrate that the existing ABR algorithms, while
effective under intended network conditions, suffer significant
I. INTRODUCTION
degradationwhenthenetworkconditionsvarywidely[3],[4],
IN RECENT years, video streaming has witnessed rapid [5], [6], [11]. This phenomenon, i.e., the operational range of
expansion,emergingasoneoftheprimaryapplicationsofthe an ABR algorithm is narrow, leads to a marked decrease in
the overall performance. We defined this problem as “ABR
Received9December2024;revised26June2025;accepted3July2025. Under-Generalization”.
Dateofpublication15July2025;dateofcurrentversion5November2025. The existing ABR algorithms can be generally divided
ThisworkwassupportedbytheNationalNaturalScienceFoundationofChina
into two major categories: heuristic-based and learning-based.
underGrant62302268,inpartbytheNaturalScienceFoundationofShandong
ProvinceunderGrant2023HWYQ-045andGrantZR2023QF060,inpartby The former [5], [6], [7], [8], [9], [19], [20], [21] rely on
Qingdao Natural Science Foundation under Grant 23-2-1-127-zyyd-jch, and pre-programmed ABR model with fixed control rules, which
in part by the Taishan Scholar Project of Shandong Province under Grant
inherently limits their adaptability to generalize the varying
tsqn202312051.Anearlierversionofthispaperwaspresentedinpartatthe
IEEEInternationalConferenceonSensing,Communication,andNetworking network environments. Consequently, the heuristic-based
[10.1109/SPCOM50965.2020.9179507].RecommendedforacceptancebyS. algorithmshavegraduallylostfavorinrecentyears.Incontrast,
Wang.(Correspondingauthor:HuiYuan.)
the learning-based algorithms, particularly those powered by
GuanghuiZhang,ZimingWang,HuarenWei,MengbaiXiao,DongxiaoYu,
andXiuzhenChengarewiththeSchoolofComputerScience andTechnol- deepreinforcementlearning(DRL)[3],[4],[10],[11],[18],[22],
ogy, Shandong University, Qingdao 266237, China (e-mail: gh.zhang@sdu. [23],[24],[25],[26],[27],[28],[29],[30],havegainedattention.
edu.cn;202235192@mail.sdu.edu.cn;202315182@mail.sdu.edu.cn;xiaomb@
They train neural networks using real network trace data,
sdu.edu.cn;dxyu@sdu.edu;xzcheng@sdu.edu.cn).
HuiYuaniswiththeSchoolofControlScienceandEngineering,Shandong resultinginABRmodelsthataremoreflexiblethantheheuristic
University,Jinan250061,China(e-mail:huiyuan@sdu.edu.cn). counterparts[10].
DigitalObjectIdentifier10.1109/TMC.2025.3588135
1536-1233©2025IEEE.Allrightsreserved,includingrightsfortextanddatamining,andtrainingofartificialintelligenceandsimilartechnologies.
Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

ZHANGetal.:NOVELSPATIAL-TEMPORALLEARNINGMETHODFORENHANCINGGENERALIZATIONINADAPTIVEVIDEOSTREAMING 12853
However,ourmeasurementstudy(refertoSectionII)reveals decisions, which not only better match the network dynamics
that when faced with a wide range of network conditions, butalsofullyutilizeavailablenetworkresources.
evenextensivelytrainedDRL-basedABRalgorithmscanonly Insummary,ourcontributionsarethree-fold:
achieve 43.1% ∼ 48.9% of the maximum possible QoE, far Large-Scale Measurement Study: We systematically evalu-
belowtheofflineoptimal100%.Thishighlightstheproblemof atedABRalgorithmstrainedbysixwell-knownDRLmethods,
ABR Under-Generalization, which contradicts the theoretical A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and
expectationthattrainingonlarge-scalerealtracesshouldyield SAC [17], clearly revealing the impact of the ABR Under-
generalizable ABR policies. The root cause appears to lie in Generalizationproblem(SectionII).
thedirectapplicationofthegenericDRLtechniques[12],[13], Design of BETA: We presented BETA, a DRL-based ABR
[14],[15],[16],[17],whichfailtocaptureallthekeyfeatures frameworkintegratingspatialandtemporalmodulestoenhance
requiredtoadaptacrossdifferentenvironments. generalization. The implementation of BETA has been open-
Motivated by this challenge, we proposed BETA, a new sourced on GitHub [32] to support reproducibility and future
DRL-based ABR framework specifically designed to enhance research(SectionIII).
the generalization of video streaming. BETA consists of two Comprehensive Evaluation: Through extensive evaluations,
core modules: spatial and temporal, which jointly tackle the weshowthatBETAsignificantlyoutperformsthestate-of-the-
above-mentionedchallenge: artABRalgorithms.Inaddition,weinvestigatedtheunderlying
Spatial Module: Our measurement study (Section II) shows reasonsforitseffectiveness(SectionIV).
thatnoneoftheABRalgorithmstrainedusingtheconventional
DRL approaches [12], [13], [14], [15], [16], [17] consistently
II. ABRUNDER-GENERALIZATION
maintain high performance across all network conditions. In
particular,allthemeasuredalgorithmsfailin8.1%to17.1%of Existinglearning-basedABRalgorithms[3],[4],[10],[11],
theevaluatedtraces,significantlydegradingtheoverallresults. [18], [22], [23], [24], [25], [26], [27], [28], [29], [30] (will be
Additionally,thespecifictraceswhereunderperformanceoccurs comprehensivelyreviewedinSectionV)predominantlyrelyon
differgreatlydependingonthespecificDRLmethodadopted. advanced DRL techniques [12], [13], [14], [15], [16], [17] for
To address this issue, BETA incorporates a spatial module. policytraining.TodemonstratetheABRUnder-Generalization
It begins by training a basic ABR model and benchmarks its problem, we conducted a measurement study evaluating the
QoEagainsttheofflineoptimalperformanceperstreamingses- ABRalgorithmstrainedusingsixwidelyadoptedDRLmethods:
sion.Thisprocesshelpsidentifytheunderperformingnetwork A3C [12], PPO [16], TD3 [14], DDPG [13], DQN [15], and
conditions,fromwhichthecorrespondingnetworkfeaturesare SAC[17].
extracted, and then are used to predict the potential network DRLConfiguration.Theneuralnetworkarchitectureadheres
conditions that might cause poor performance in the future. totheestablisheddesignsfrompriorliterature[3],[4],[10],[11],
BETA proceeds to train specialized ABR models specifically [18],[22],[23],[24],[25],[26],[27],[28],[29],[30].Specifi-
tailoredtothesechallengingnetworkconditions. cally,themodelinputcomprisesfivecategoriesofenvironmental
Temporal Module: We observed that the existing DRL- states:(i)themeasuredthroughputofthepast8segments,(ii)
trained ABR algorithms are often short-sighted, focusing only thedownloaddurationsofthepast8segments,(iii)thebitrateof
on single-step future planning. This is due to their training the most recently downloaded segment, (iv) the current buffer
approach, where each epoch updates the model based solely occupancy, and (v) the number of remaining segments in the
on the immediate reward of short-term feedback. This is ill- currentstreamingsession.Thefirsttwoinputsareprocessedvia
suitedforthevideostreamingcontextsthatrequireconsecutive convolutional neural networks (CNNs) with 128 filters, while
decision-makingacrossallthevideosegmentsineachstreaming theremainingthreearefedintofullyconnected(dense)layers
session. with 128 neurons. Then the outputs are subsequently merged
BETA addresses this issue with a temporal module. BETA throughadenseaggregationlayercomprising256neurons.The
samplesmulti-segmentdecisionsequencesduringtraining,each outputlayeroffersthediscretebitratelevel,whichservesasthe
consisting of a series of state-action-reward tuples. For each decisionaction.AllthesixDRLmethodsaretrainedusingthe
sequence,adiscountedactualrewardencompassingalltheseg- Adam optimizer, with training hyperparameters (e.g., learning
mentsiscalculated,alongwithanexpectedrewardbasedonthe rate,batchsize,experiencereplaybuffer)individuallytuned.
initialandfinalstatesofeachsequence.Bothoftherewardsare Streaming Environment: To emulate the realistic streaming
thenusedtoupdatetheneuronweightsbyminimizingthegap environment,webuiltanopen-sourceABRemulator[32]based
betweenthem.ThisapproachenablesthetrainedABRmodelto onthepreviousworkbyMaoetal.[10],applyingcustommodi-
makefar-sighteddecisions,therebyensuringmorestableQoE. ficationstoaccommodateourexperimentalsetup.Forexample,
Extensiveevaluationusinglarge-scalenetworktracedatasets eachstreamingsessionemulatestheplaybackofa192-second
demonstratestheeffectivenessofBETA.Comparedtostate-of- video, partitioned into 48 segments of 4 seconds each. Every
the-artABRalgorithms,BETAimprovesaverageQoEby19.4% segmentisencodedintoeightbitratelevels:{0.2,0.8,2.2,5.0,
to50.9%,withgainsreaching244.1%inhighlyvariablenetwork 10.0,18.0,32.0,50.0}Mbps,reflectingawiderangeofencoding
conditions.FortheinternalQoEmetrics,BETAachievesa7.9% options.
increaseinvideoqualityanda98.3%reductioninrebuffering The network condition is emulated using TCP throughput
events. These benefits are attributed to BETA’s flexible bitrate traces, with an average bandwidth of 17.66 Mbps and a peak
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

12854 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.24,NO.12,DECEMBER2025
TABLEI theaverage videobitrate,totalrebufferingduration,andvideo
COMPARISONOFQOEANDSTREAMINGPERFORMANCEOVERSIXDRL-BASED qualityvariation.SeetheirdefinitionsinEq.(1).Thesemetrics
ABRALGORITHMS
collectivelycharacterizethetradeoffseachalgorithmmakesin
adaptivestreamingscenarios.
|     |     |     |     |     | From | Table | I, two key | observations | can | be made | regarding |     |
| --- | --- | --- | --- | --- | ---- | ----- | ---------- | ------------ | --- | ------- | --------- | --- |
theQoEperformanceofdifferentDRL-basedABRalgorithms.
|     |     |     |     |     | First, there | exists   | a substantial |          | performance   | disparity |     | among |
| --- | --- | --- | --- | --- | ------------ | -------- | ------------- | -------- | ------------- | --------- | --- | ----- |
|     |     |     |     |     | the DRL      | methods. | For           | example, | the TD3-based |           | ABR | model |
achievesthehighestabsoluteQoE(A-QoE)of346.7,whereas
|     |     |     |     |     | the SAC-based |     | model | performs | the worst, | with | an A-QoE | of  |
| --- | --- | --- | --- | --- | ------------- | --- | ----- | -------- | ---------- | ---- | -------- | --- |
only305.9.Second,thenormalizedQoE(N-QoE)revealsthatall
thesixmethodsattainonlysuboptimalperformance,achieving
|     |     |     |     |     | merely 43.1%      |                | to 48.9%   | of the          | offline optimal  |                | QoE. This   | is    |
| --- | --- | --- | --- | --- | ----------------- | -------------- | ---------- | --------------- | ---------------- | -------------- | ----------- | ----- |
|     |     |     |     |     | significantly     | lower          | than       | the theoretical | upper            | bound          | of          | 100%. |
|     |     |     |     |     | While the         | offline        | optimal,   | derived         | under            | the assumption |             | of    |
|     |     |     |     |     | perfect foresight |                | of future  | throughput,     | is               | unattainable   | in          | real- |
|     |     |     |     |     | world settings    |                | due to the | inherent        | unpredictability |                | of network  |       |
|     |     |     |     |     | dynamics,         | the pronounced |            | QoE             | gap highlights   | the            | substantial |       |
roomforperformanceimprovement.
|     |     |     |     |     | In Table | I,  | the best-performing |     | DRL | method | under | each |
| --- | --- | --- | --- | --- | -------- | --- | ------------------- | --- | --- | ------ | ----- | ---- |
metricishighlightedinbold.Togaindeeperinsightsintothese
|     |     |     |     |     | top-performing |     | models, | we further | analyzed | their | per-session |     |
| --- | --- | --- | --- | --- | -------------- | --- | ------- | ---------- | -------- | ----- | ----------- | --- |
performance.Specifically,sinceTD3achievesthehighestnor-
valueofupto131.44Mbps.Thesetraceswerecollectedfrom malizedQoE(48.9%),weselectedtworepresentativestreaming
real-world cellular networks, including 3G, 4G, 5G, and Wi- sessionsandvisualizedtheirperformanceinFig.1(a)and(b).In
| Fi, over a continuous | 77-day | period. The | data collection | was |     |     |     |     |     |     |     |     |
| --------------------- | ------ | ----------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Sample1(Fig.1(a)),TD3exhibitseffectivebitrateadaptation,
conductedacrossfourtypesofgeographiclocations:subways, resulting in a high QoE score of 1405.9, which is close to the
campuses,shoppingmalls,andhomes.Thecompletedatasethas
offlineoptimalof1574.0.Bycontrast,inSample2(Fig.1(b)),
beenmadepubliclyavailableonGitHub[36].Inthisevaluation, TD3failstoadaptappropriatelytodynamicnetworkconditions,
80% of the data is used for model training, and the remaining leading to a significant rebuffering event. Specifically, at the
20%isreservedforonlinetesting.Boththetrainingandtesting
|     |     |     |     |     | 30th segment, |     | the available | throughput | drops | sharply, |     | yet the |
| --- | --- | --- | --- | --- | ------------- | --- | ------------- | ---------- | ----- | -------- | --- | ------- |
sets comprehensively cover the three network types, the four selected bitrate remains high, rapidly depleting the playback
geographiclocations,andallthetimeperiodsinoneday.
bufferandcausingan8.9-secondrebufferingevent.Thisresults
Forthestreamingperformancemetric,weadoptedanexisting inaseverelydegradedQoEof–31.1,farbelowthecorresponding
| QoEfunctionproposedbyMaoetal.[10]: |     |     |     |     | offlineoptimalof685.0. |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
AlthoughTD3achievesthehighestoverallQoE,itperforms
| N(cid:2)−1 | N(cid:2)−1 | N(cid:2)−2 |     |     |     |     |     |     |     |     |     |     |
| ---------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
QoE = F(b )−σ× θ − |F(b )−F(b )| suboptimallyintermsofrebufferingdurationandqualityvaria-
|     | t   | t   | t+1 | t   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tion,asshowninTableI.Incontrast,PPOyieldsthebestresults
| t=0 | t=0 | t=0 |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(1) forthesetwometrics.Tothisend,weappliedPPOtothesame
wherethefirsttermofEq.(1)denotesthevideoqualityutility, twostreamingsessions(i.e.,Sample1andSample2)andvisual-
and the last two denote the penalties for playback rebuffering izedthestreamingperformanceinFig.1(c)and(d),respectively.
(coefficient σ = 50) and video quality variation respectively. Interestingly,PPOexhibitsamarkedlydifferentadaptationbe-
Specifically, bt is the video bitrate of segment t, θ is the havior compared to TD3. In Sample 1, PPO achieves a QoE
t
rebufferingdurationindownloadingsegmentt,F(.)denotesthe of 577.3, which is significantly lower than both the offline
mappingfrombitratetovideoqualitywhereweadoptedlinear optimal(1574.0)andtheresultachievedbyTD3(1405.9).This
mappingF(bt)=bt
[10]inthisevaluation. underperformance is primarily due to its conservative bitrate
ResultsAnalysis:TableIsummarizestheperformanceofthe selection, i.e., PPO chooses bitrates substantially below the
six DRL-based ABR algorithms. QoE is reported using two availablethroughput,leadingtoinefficientutilizationofnetwork
representations:theabsoluteQoEscore(denotedasA-QoE)and resources. Conversely, in Sample 2, PPO achieves a QoE of
thenormalizedQoEscore(denotedasN-QoE).Thenormalized 327.2, which, although still below the offline optimal (685.0),
score is obtained by dividing the absolute score by the offline ismarkedlysuperiortothatofTD3(–31.1).Thisimprovement
optimal.TheoptimalQoEservesasthetheoreticalupperbound, islargelyattributabletoPPO’seffectiveavoidanceofplayback
which is computed based on dynamic programming, using rebufferingevents,astherebufferingdurationapproacheszero.
an omniscient policy with perfect foresight of future network From the above results, several important insights emerge.
throughput(moredetailsarereferredtoSpiterietal.[8],andthe WhiletheDRL-basedABRalgorithmscanperformadequately
implementationisavailablein[31]).InadditiontotheQoE,we under their intended network conditions, the effectiveness de-
furtherevaluatedthethreecoremetricsthatcontributetoQoE: gradesconsiderablyinothers.Thislimitationstemsfromtheir
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore.  Restrictions apply.

ZHANGetal.:NOVELSPATIAL-TEMPORALLEARNINGMETHODFORENHANCINGGENERALIZATIONINADAPTIVEVIDEOSTREAMING 12855
Fig.1. Per-sessionstreamingperformance(thex-axis–segmentindex,withthewidthofeachsegmentscaledbyitsplaybacktime).
TABLEII beconstrainedbytheirlimitedadaptability,ultimatelybecoming
THEPROPORTIONOFUNDERPERFORMEDSTREAMINGSESSIONS
abottleneckinreal-worlddeploymentscenarios.
III. METHODOLOGY
BuildingupontheinsightsderivedinSectionII,weproposed
BETA, a new DRL-based framework designed to address the
lackofgeneralizationcapabilityacrossdiversenetworkcondi-
ABRUnder-Generalizationproblem.Theoveralldescriptionof
tions(i.e.,theproblem“ABRUnder-Generalization”described
BETA is presented in Section III-A, followed by the details
in Section I). To further quantify this problem, we introduce
of its two key modules in Sections III-B and Section III-C,
a metric that captures the proportion of streaming sessions
respectively.
in which a DRL-based ABR method yields QoE significantly
belowtheofflineoptimal.Specifically,wedefinethisproportion
asfollows: A. BETAOverall
|{κ |o −r >δ,j =0,1,...,J −1}|
ε= j j j (2) Fig.2plotstheoverallarchitectureofBETA,whichcomprises
J
twoprimarymodules:SpatialandTemporal.TheSpatialModule
whererjistheachievedQoEofsessionj,ojisthecorresponding serves as the master routine, while the Temporal Module is a
optimum,δistheQoEgap(δissetto700.Notethatthissetting sub-routinethatisperiodicallyinvokedbytheSpatialModule.
istoreflectthelargegapbetweentheactualQoEandtheoffline Spatial Module: As shown in the measurement study in
optimal. A sensitivity analysis is performed in Section IV-E), Section II, ABR algorithms trained with the state-of-the-art
symbol|.|calculatestheelementnumberoftheset,Jisthetotal DRL methods [12], [13], [14], [15], [16], [17] only achieve
sessionnumber(denominator),andεistheoutputproportion. 43.1%to48.9%oftheoptimalQoE,primarilyduetothesevere
TableIIpresentstheresultsoftheunder-performingpropor- underperformancein8.1%to17.1%ofthestreamingsessions.
tion across all six DRL-based ABR algorithms. The observed To address this issue, BETA introduces the Spatial Module.
valuesarenon-negligible,rangingfrom8.1%to17.1%.Given Specifically, BETA initially invokes the Temporal Module to
the pre-defined QoE gap δ = 700, such a high proportion of train a base ABR model, which is then evaluated across all
poorly performing sessions substantially degrades the overall training network traces by comparing the achieved QoE with
QoE. We hypothesize that this suboptimality stems from the the corresponding offline optimum. Based on this evaluation,
directapplicationofconventionalDRLmethods[12],[13],[14], the training traces are partitioned into two subsets: one where
[15],[16],[17]totheABRtask.Despiteextensivetrainingon theABRmodelperformsadequately,andtheotherwhereitfails
large-scale real-world network traces, these DRL methods fail togeneralizewell.Fromtheselabeledtraces,BETAextractsin-
tofullycapturethecriticalfeaturesnecessaryforrobustperfor- ternalnetworkfeaturestotrainaclassifierthatpredictswhethera
mance across diverse network environments. This problem is givennetworktraceislikelytoresultinunderperformance.This
particularly problematic in practice, where streaming services classifier enables BETA to dynamically distinguish between
must operate across a wide spectrum of network conditions, “normal” and “difficult” traces in real-time. Accordingly, two
rangingfromlow-capacity3Gnetworkstohigh-speed5Genvi- complementary ABR models are trained for each trace subset
ronments.Withoutaddressingthegeneralizationdeficiency,the by invoking the Temporal Module, and during online stream-
performanceoftheDRL-basedABRalgorithmswillinevitably ing, BETA dynamically selects the appropriate logic to better
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

12856 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.24,NO.12,DECEMBER2025
Fig.2. ThewholestructureofBETAwiththespatialmoduleandthetemporalmodule.
accommodate the diverse network conditions. The details are thisphasefocusesonidentifyingsuchproblematicconditions.
elaboratedinSectionIII-B. However, a key challenge arises: even if these conditions are
Temporal Module: Existing DRL-based ABR algorithms well identified during offline training, the trained models may
[12],[13],[14],[15],[16],[17]oftenexhibitshort-sightedness. notworkwellatruntime,asthefuturenetworkconditionsofan
Thisisproblematicinadaptivevideostreaming,whereQoEis ongoingstreamingsessionarenotknownapriori.
influencedbytemporalcontinuityandcumulativeeffectsofthe To tackle the challenge, in this work, a binary classifier is
ABRdecisionsovermultiplesegments.Toovercomethisissue, trainedfortheidentificationofnetworkconditions.Atthestart,
BETAintroducestheTemporalModule.Duringtraining,BETA BETAtrainsabasicABRmodelviathetemporalmodule(will
recordsastate–action–rewardtupleforeachsegmentandstores beintroducedinSectionIII-C),andteststheQoEperformancerj
theminanexperiencebuffer,maintainingahistoryofdecision underthethroughputtracedataκ jofstreamingsessionj.Then,
sequences. Fromthisbuffer,itsamples tuplesequences where BETAcomparesQoErjtotheofflineoptimumoj(c.f.SectionII
eachconsistsofnconsecutivesegments.Foreachsequence,a forthecalculationoftheoptimalQoE),andusestheirgap,i.e.,
discountedactualrewardencompassingallthesegmentsiscal- (oj – rj), to classifyall the throughput traces into two subsets,
culated,alongwithanexpectedrewardbasedontheinitialand namely,Λ normal andΛ under:
finalstatesofeachsequence.Thesetworewardsareintegrated
intothetraining,wheretheneuralnetworkweightsareadjusted Λ normal ={κ j |o j −r j ≤δ,j =0,1,...,J −1} (3)
to minimize the discrepancy between the two. Through this Λ under ={κ j |o j −r j >δ,j =0,1,...,J −1} (4)
approach,thetrainingABRmodellearnstooptimizedecisions
across temporally extended horizons, thereby improving QoE Theintuitionbehindthetwoequationsisthat,iftheQoEgap
consistency across entire streaming sessions. The details are is larger than QoE threshold δ (e.g., = 700) then throughput
providedinSectionIII-C. traceκ j willbeincorporatedintosetΛ under thatconsistsofall
under-performedtraces.Onthecontrary,traceκ jwillbeintothe
normal-performedsetΛ normal.Onthisbasis,BETAwilltrain
B. SpatialModule
abinaryclassifierviasupervisedlearningwheretheclassifieris
ThestructureoftheSpatialModuleisillustratedinFig.2-left. modeled with convolutional neural networks (CNN). The two
Itoperatesinthreesequentialphases:offlineclassifiertraining, trace sets {Λ normal, Λ under} work as the ground truth during
offlinemulti-modeltraining,andonlinedifferentialstreaming. thetraining.
The three phases are encapsulated in Algorithm 1 as three OfflineMulti-modelTraining:PriortotrainingtheABRmod-
distinct functions: lines 4∼17, lines 18∼29, and lines 30∼38, els,thethroughputtraceswillbere-classifiedusingthebinary
respectively.Themainexecutionflow(lines1∼3)invokesthese classifier.OnemightquestionwhyBETAdoesnotsimplyrely
functions in sequence. In the following, we elaborate on each ontheground-truthclassificationobtainedvia(3)and(4).The
phaseindetail. reason is that the binary classifier will be ultimately applied
Offline Classifier Training: The primary objective of the in the online streaming, but it is inherently imperfect to cope
Spatial Module is to enhance the generalization capability of with the unknown network conditions at runtime, and thus,
ABRalgorithms,namely,toensurerobustperformanceacross the online classification inevitably has errors. If such misclas-
awidespectrumofnetworkconditions.Achievingthisrequires sifications are not exposed to the ABR models during offline
targeting the improvements of the network condition where training,themodelswilllackthenecessaryrobustnesstohandle
the ABR model exhibits degraded performance. To this end, thematruntime.Consequently,thiswouldleadtoasignificant
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

ZHANGetal.:NOVELSPATIAL-TEMPORALLEARNINGMETHODFORENHANCINGGENERALIZATIONINADAPTIVEVIDEOSTREAMING 12857
degradationinthestreamingperformance.Therefore,thebinary
Algorithm1:SpatialModule.
| classifier |     | must be | applied | consistently |     | in both | the offline | and |     |     |     |
| ---------- | --- | ------- | ------- | ------------ | --- | ------- | ----------- | --- | --- | --- | --- |
Input:Trainingthroughputtraceofallstreamingsessionsj:
| online | phases | to  | enable the | ABR | models | to learn | how | to cope |     |     |     |
| ------ | ------ | --- | ---------- | --- | ------ | -------- | --- | ------- | --- | --- | --- |
Λ={κ j|(cid:2)j}
withtheclassificationerrors.
#Step1:Input-trainingtracedataΛ;Output-trainedclassifierC
Λ
In this work, we re-defined two new trace datasets L1 andbasicABRmodelMbasic.
and Λ L2, and re-classified the throughput traces. Specifically, =Offline_Classifier_Training(Λ)
1:C,Mbasic
normal-performedtracesetΛ andunder-performedtraceset #Step2:Input-classifierC,trainingtraceΛ,basicABRmodel
L1
Λ
L2 are labeled by L1 and L2, respectively. BETA executes Mbasic;Output–twotrainedABRmodels,i.e.,ML1,ML2.
thebinaryclassifier,denotedbyfunctionC(.),tocategorizethe 2:ML1,ML2 =Offline_MultiModel_Training(C,Λ,Mbasic)
|                 |     |                   |      |           |            | {κ   | =     |       | #Step3:Input-classifierC,andtrainedABRmodelsML1,ML2. |     |     |
| --------------- | --- | ----------------- | ---- | --------- | ---------- | ---- | ----- | ----- | ---------------------------------------------------- | --- | --- |
| traces          | of  | all the streaming |      | sessions, | i.e.,      | j, j | 01,…, | J-1}, |                                                      |     |     |
| intothetwosets: |     |                   |      |           |            |      |       |       | 3:Online_Differential_Streaming(C,ML1,ML2)           |     |     |
|                 | Λ   | ={κ               | |C(κ | )≡L1,j    | =0,1,...,J |      | −1}   |       |                                                      |     |     |
L1 j j (5) 4:FunctionOffline_Classifier_Training(Λ={κ j|(cid:2)j})
|                                                       |     |     |      |        |            |     |     |     | 5 : Tr a i | n A B R m o d               | e l M withΛviatemporalmodule |
| ----------------------------------------------------- | --- | --- | ---- | ------ | ---------- | --- | --- | --- | ---------- | --------------------------- | ---------------------------- |
|                                                       | Λ   | ={κ | |C(κ | )≡L2,j | =0,1,...,J |     | −1} | (6) |            |                             | ba sic                       |
|                                                       | L2  |     | j j  |        |            |     |     |     | 6: Λ       | = Ø , Λ                     | = Ø                          |
|                                                       |     |     |      |        |            |     |     |     | n o        | r m al                      | u n d er                     |
|                                                       |     |     |      |        |            |     |     |     | fortraceκ  | jinstreamingsessionj=1toJdo |                              |
| Thereafter,withthetwotracesets,BETAinvokesthetemporal |     |     |      |        |            |     |     |     | 7:         |                             |                              |
TestMbasicwithκ
moduletotrainABRmodelML1andML2specificallyforeach 8: j,andobtainQoErj
|     |     |     |     |     |     |     |     |     | 9: ComputeoptimalQoEunderκ |     | j,denotedbyoj |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | ------------- |
ofthetwonetworkclasses.Thesetwomodelscanbeexecuted
|     |     |     |     |     |     |     |     |     | 10: ifoj–rj | >δthen |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --- |
complementarilyattheonlinephase.
|     |     |     |     |     |     |     |     |     | 11: | Λ ←κ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
Online Differential Streaming: At runtime, the two trained under j
|                                                         |      |       |        |         |            |     |      |         | 12: else   |        |     |
| ------------------------------------------------------- | ---- | ----- | ------ | ------- | ---------- | --- | ---- | ------- | ---------- | ------ | --- |
| ABRmodels,denotedasML1andML2,areselectivelyexecuted     |      |       |        |         |            |     |      |         |            | Λ ←κ   |     |
|                                                         |      |       |        |         |            |     |      |         | 13:        | normal | j   |
| by                                                      | BETA | based | on the | network | conditions | of  | each | stream- |            |        |     |
|                                                         |      |       |        |         |            |     |      |         | 14: endif  |        |     |
| ingsession.Specifically,BETAcontinuouslymonitorsthenet- |      |       |        |         |            |     |      |         | 15: endfor |        |     |
work environment and records the observed video download 16: SupervisedlearningtotrainbinaryclassifierCvia{Λ normal,
| throughput |           | in the  | form of  | trace     | data during | the      | online | phase.  | Λ under}    |     |     |
| ---------- | --------- | ------- | -------- | --------- | ----------- | -------- | ------ | ------- | ----------- | --- | --- |
| At         | the start | of each | new      | streaming | session,    | the      | most   | recent  | 17: returnC |     |     |
| trace      | data      | is fed  | into the | binary    | classifier  | to infer | the    | network |             |     |     |
18:FunctionOffline_MultiModel_Training(C,Λ={κ j|(cid:2)j},
conditionanddeterminethecorrespondingsessionlabel.Ifthe
Mbasic)
| classifier |     | predicts | L1, indicating |     | a normal | network | condition, |     |           |         |       |
| ---------- | --- | -------- | -------------- | --- | -------- | ------- | ---------- | --- | --------- | ------- | ----- |
|            |     |          |                |     |          |         |            |     | 1 9 : Λ ’ | = Ø , Λ | ’ = Ø |
B E T A d e p l o y s M fo r t h a t se s si o n . C o n v er s e ly , if th e o u tp u t no r m a l u n de r
|     |     |     | L 1 |     |     |     |     |     |             | κ               | essionj=1toJdo  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | --------------- |
|     |     |     |     |     |     |     |     |     | 2 0 : f o r | tr a c e j in s | tr e a m i ng s |
is L 2 ,s u g g e s ti n g a po te n t ia l ly u n d e r pe r fo r m i n g o r ch a lle n g in g ifC(κ j)==L1then
21:
| network   | condition, |           | ML2     | is selected | instead. | This        | differential |     |          |           |     |
| --------- | ---------- | --------- | ------- | ----------- | -------- | ----------- | ------------ | --- | -------- | --------- | --- |
|           |            |           |         |             |          |             |              |     | 22:      | Λ L1 ←κ j |     |
| execution |            | mechanism | enables | BETA        | to       | dynamically | adapt        | its |          |           |     |
|           |            |           |         |             |          |             |              |     | 23: else |           |     |
ABRpolicyinresponsetoreal-timenetworkconditions,thereby 24: Λ ←κ
L2 j
enhancingtherobustnessandconsistencyacrossheterogeneous
|               |                |     |     |     |     |     |     |     | 25: endif                                     |     |       |
| ------------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | ----- |
| environments. |                |     |     |     |     |     |     |     | 26: endfor                                    |     |       |
|               |                |     |     |     |     |     |     |     | 27: TrainABRmodelML1(uponMbasic)withtracesetΛ |     | L1via |
| C.            | TemporalModule |     |     |     |     |     |     |     | temporalmodule                                |     |       |
|               |                |     |     |     |     |     |     |     | 28: TrainABRmodelML2(uponMbasic)withtracesetΛ |     | L2via |
ThestructureoftheTemporalModuleisillustratedinFig.2-
temporalmodule
| right. | It is | composed | of  | six neural | networks | in  | total: | an actor |                   |     |     |
| ------ | ----- | -------- | --- | ---------- | -------- | --- | ------ | -------- | ----------------- | --- | --- |
|        |       |          |     |            |          |     |        |          | 29: returnML1,ML2 |     |     |
network,atargetactornetwork,twocriticnetworks,andtwotar-
getcriticnetworks,followingthearchitectureproposedin[14]. 30:FunctionOnline_Differential_Streaming(C,ML1,ML2)
Among these, only the actor network is responsible for ABR 31: whileanewstreamingsessionstartsdo
|     |     |     |     |     |     |     |     |     | 32: Obtaintheonlinecapturedthroughputtrace,denotedbyκ |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
decisions,andtheremainingfiveallserveastrainingassistants.
ifC(κ)==L1then
| Fortheactor-network,theinputlayercontainsfiveenviron- |           |                   |           |              |             |          |            |          | 33:                                     |                                     |     |
| ----------------------------------------------------- | --------- | ----------------- | --------- | ------------ | ----------- | -------- | ---------- | -------- | --------------------------------------- | ----------------------------------- | --- |
|                                                       |           |                   |           |              |             |          |            |          | 34: ApplyABRmodelML1tothecurrentsession |                                     |     |
| ment                                                  | states    | that characterize |           | both         | the network |          | conditions | and      |                                         |                                     |     |
|                                                       |           |                   |           |              |             |          |            |          | 35: else                                |                                     |     |
| the                                                   | streaming | context,          | including |              | (i) the     | measured | throughput |          |                                         |                                     |     |
|                                                       |           |                   |           |              |             |          |            |          | 36:                                     | ApplyABRmodelML2tothecurrentsession |     |
| over                                                  | the       | past eight        | segments  | (represented |             | as       | a list),   | (ii) the |                                         |                                     |     |
|                                                       |           |                   |           |              |             |          |            |          | 37: endif                               |                                     |     |
segmentdownloadtimesoverthepasteightsegments(alsoasa
|     |     |     |     |     |     |     |     |     | 38: endwhile |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- |
list),(iii)thebitrateselectedforthemostrecentlydownloaded
segment,(iv)thecurrentbufferoccupancy(inseconds),and(v)
thenumberofremainingsegmentsyettobedownloadedinthe
currentstreamingsession.Thisinputdesignisconsistentwith eachpassedthroughseparatefullyconnected(dense)layerswith
theDRLsettingsintroducedinSectionII. 128 neurons. The outputs of all the five are then concatenated
Inthehiddenlayers,thefirsttwostates(amongthefive)are andpassedthroughanadditionaldenselayerconsistingof256
individually processed by two CNNs, each with 128 filters, to neurons, which serves as the final hidden representation for
extracttemporalpatterns.Theremainingthreescalarstatesare actiongeneration.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore.  Restrictions apply.

12858 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.24,NO.12,DECEMBER2025
(cid:7)
Algorithm2:TemporalModule. h=0,...,H −1 (7)
Initialize:critic-networksQθ1andQθ2(neuronweightθ1,
Q θ θ 2 2 θ _ ) 1 ; t _ a a t r c a , t r o φ , r Q _ -n t θ a e 2 r t _ w ) t o ar rk ,a π n φ d ( π n φ e _ u t r a o r n ( w ne e u ig ro h n tφ w ) e , i t g a h rg t e θ t 1 n _ e ta tw r, orks w {η h h er | e h η = h 0 i 1 s , o … ne ,H e - n 1 c } o ( d t i o n t g al b H itr v a e t r e si v o e n r s s ) i , o a n n i d n th th e e o b u i t t p r u at t e bt p i r s ofi th le e
finalbitratedecisionforsegmentt.
Input:throughputtracedataofallstreamingsessionsj:
The critic network shares a similar structure with the actor
{κ j|(cid:2)j}
network, but differs in two key aspects: its input and output
Output:trainedactor-networkπ
φ
layers. On the input side, in addition to the five environment
states(i.e.,theinputoftheactornetwork),thecriticnetworkalso
1:foreachstreamingsessionjdo
2: forsegmentt=1toTdo
receivestheactionatoutputbytheactornetwork(corresponding
to the current state). This additional input allows the critic
3: Observestatestanddecideactionat:at =π φ(st)
networktoevaluatethequalityofagivenstate–actionpair.On
4: Mapat tobitratebt anddownloadsegmenttwith
theoutputside,unliketheactornetworkthatoutputsanaction,
throughputtraceκ
j
thecriticnetworkoutputsascalarQ-value(associatedwiththe
5: Observerewardrt(i.e.,QoE),andnewstatest+1
inputstate–actionpair),whichisusedtocomputethetemporal
6: Storetuple(st,at,rt,st+1)inanexperiencebufferΠ
difference (TD) error, that in turn guides the update of the
7: Sampleamini-batchΩfromΠ,includingabatchof
neuralnetworkduringtraining.Itisworthnotingthatthetarget
tuplesequences,eachwithnconsecutivetuples:
criticnetworkandtargetactornetworkadoptexactlythesame
Ω←(cid:6)(s ,a ,r ,s )(cid:8)
t(cid:7)+i t(cid:7)+i t(cid:7)+i t(cid:7)+1+i i=0,1,...,n−1 architecture as their respective primary networks (critic and
8: Qtar =Compute_Target_Q(Ω,n)
actor), and are used solely for stabilizing the training process.
9: UpdatecriticsQθ1,Qθ2byminimizingtheloss
Therefore,theirstructuraldetailsareomittedhereforbrevity.
function:
min
θ1/2
[Q
θ1/2
(s
t(cid:7)
,a
t(cid:7)
)−Q
tar
]2 The running procedure of the temporal module is described
inAlgorithm2.Specifically,inonestreamingsession,foreach
10: if(tmodσ)==0then
11: Updateactorπ φbymaximizingtheQvalue:
video segment t,the environment statest is fedinto the actor-
max
φ
Q
θ1
[s
t(cid:7)
,π
φ
(s
t(cid:7))
]
networktoobtainactionatwhichisthenmappedtotheavailable
bitrate version according to (7). Under the bitrate decision,
12: Softlyupdatetargetnetworks:φ_tar=τ×φ_tar+
segment twillbestreamed inavirtualstreaming environment
(1-τ)×φθ1_tar=τ×θ1_tar+(1-τ)×θ1
θ2_tar=τ×θ2_tar+(1-τ)×θ2
[10], and then the resultant reward rt (quantified by the QoE
function like (1)) and new state st+1 will be obtained. These
13: endif
metricswillbeformulatedintoa4-factortuple,denotedby(st,
14: endfor
at,rt,st+1,),andstoredintoanexperiencebufferΠ(c.f.line1
15:endfor
∼line6inAlgorithm2).Then,fromΠ,BETAwillrandomly
16:returntrainedactornetworkπ
φ sampleabatchoftuplesequences,denotedbyΩ,eachconsisting
ofnconsecutivetuples(line7):
17:FunctionCompute_Target_Q(Ω,n)
(cid:8) (cid:9)
18: Initializecumulativereward:R=0
19: for(st’+i,at’+i,rt’+i,st’+1+i)inΩandi=0ton-1 Ω← (s t(cid:7)+i ,a t(cid:7)+i ,r t(cid:7)+i ,s t(cid:7)+1+i ) i=0,1,...n−1 (8)
do
where the tuples are sorted by segment index i = 01,…,n-1.
20: UpdateRwithrewardrt’+ianddiscountfactorβ:
EachtuplesequenceinΩcontainsthestate-actionpairsandthe
R=R+βi×rt’+i
correspondingrewardsofnconsecutivesegments(steps),which
21: endfor
giveslong-termenvironmentalfeedbacktothebitratedecisions
22: Calculatetargetactionwiththelaststatest’+ninΩ:
made by the neural network. These historical experiences will
atar =π φ_tar(st’+n)+N(μ,σ2)
befurtherfedbackintothetrainingprocess,offeringtheneural
23: CalculateminimumtargetQvalue:
networkalong-termdecisionhorizon.
Qtar1 =Qθ1_tar(st’+n,atar),Qtar2 =Qθ2_tar(st’+n,
Toincorporatetheexperiencesintothetraining,BETAuses
atar)
thedatainΩforcalculatingatargetQvalue(line8):
min_Q=min(Qtar1,Qtar2)
(cid:10) (cid:11)
24: returnR+βn×min_Q (cid:2)n−1
Q tar = βir t(cid:7)+i +βnmin(Q tar1 ,Q tar2 ) (9)
i=0
The output layer has only one neuron with the activation
function Tanh. The output action, denoted by at (for segment
whereQtar1andQtar2aretheQ-valuesoutputbythetwotarget-
t), is continuous-valued, ranging from −1 to +1. To map it to critic-networksrespectively,rt’+iistherewards(i.e.,QoE)ofthe
ithsegmentinΩ(c.f.(8)),βisadiscountfactor,andnisthetotal
theencodingbitrateversion,wedefinedamappingpolicy:
(cid:3) (cid:4) (cid:5) (cid:6) tuplenumber.Thedetailedimplementationforcalculatingtarget
b =max η (cid:4) (cid:4)η ≤ η +(η −η ) (a t +1) , QvalueQtarisdescribedbythefunctionCompute_Target_Q(.)
t h(cid:4) h 0 H−1 0 2 inAlgorithm2(line17∼line24).
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

ZHANGetal.:NOVELSPATIAL-TEMPORALLEARNINGMETHODFORENHANCINGGENERALIZATIONINADAPTIVEVIDEOSTREAMING 12859
Onthisbasis,thenextstepistoupdatethetwocritic-networks TABLEIII
Qθ1andQθ2.TheobjectiveistomaketheQ-valueoutputbythe BETAPARAMETERS
| critic-networksclosetothetargetQvalueQtar |     |     |       |                                  |     | throughtuning |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | ----- | -------------------------------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
| theneuronweightsθ                         |     |     |       | ofthetwocriticsrespectively(line |     |               |     |     |     |     |     |     |
|                                           |     |     | j =12 |                                  |     |               |     |     |     |     |     |     |
9).Thisstepisimplementedviaexecutingadeterministicpolicy
gradienttominimizethefollowinglossfunction:
|     |     | (cid:12) |     |     | (cid:13) |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
2,j
|       | min       | Q          | (s ,a        | )−Q      |           | =1,2  |        | (10)  |     |     |     |     |
| ----- | --------- | ---------- | ------------ | -------- | --------- | ----- | ------ | ----- | --- | --- | --- | --- |
|       |           | θ j        | θ j t(cid:7) | t(cid:7) | tar       |       |        |       |     |     |     |     |
| where | state st’ | and action | at’          | are in   | the first | tuple | in the | tuple |     |     |     |     |
sequenceΩ(i.e.,indexi=0,see(8)).Theactor-networkπ
φwill
thenbeupdatedbygradientdescentbasedonthenewlylearned
critic-network-1Qθ1tomaximizeitsoutputQ-value(line11):
|     |     | max | Q   | [s ,π      | (s )]      |     |     | (11) |     |     |     |     |
| --- | --- | --- | --- | ---------- | ---------- | --- | --- | ---- | --- | --- | --- | --- |
|     |     |     | φ   | θ t(cid:7) | φ t(cid:7) |     |     |      |     |     |     |     |
1
TABLEIV
| wherestatest’ |     | isinthefirsttupleofthetuplesequenceΩ.The |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
COMPARISONOFQOEACROSSSEVENABRALGORITHMS
intuitionbehind(8)∼(11)istogivethetwocritic-networksa
longer-termviewsothattheycanmoreaccuratelyassesstheben-
efitsderivedfromtheactionsmadebythecurrentactor-network.
| In this | way, as | the training |     | proceeds, | the | ABR algorithm, |     | i.e., |     |     |     |     |
| ------- | ------- | ------------ | --- | --------- | --- | -------------- | --- | ----- | --- | --- | --- | --- |
theactor-network,willbegraduallyofferedtheabilitytomake
far-sighteddecisions.
| At the      | end        | of each  | training    | epoch, | all        | target | networks,     | in-     |     |     |     |     |
| ----------- | ---------- | -------- | ----------- | ------ | ---------- | ------ | ------------- | ------- | --- | --- | --- | --- |
| cluding     | the target | actor    | and         | the    | two target | critic | networks,     |         |     |     |     |     |
| are updated |            | using an | exponential |        | weighted   | moving |               | average |     |     |     |     |
| (EWMA)      | policy.    | This     | soft        | update | mechanism  |        | incrementally |         |     |     |     |     |
incorporatestheparametersofthenewlyupdatedactorandcritic
| networks | into | their | corresponding |     | target | networks | (line | 12), |     |     |     |     |
| -------- | ---- | ----- | ------------- | --- | ------ | -------- | ----- | ---- | --- | --- | --- | --- |
therebyenhancingtrainingstabilityandmitigatingoscillations.
Afterasufficientnumberoftrainingepochs,thelearningprocess
converges,andthefinalactornetworkisexportedasthetrained
| ABR decision |     | model, | which | is subsequently |     | deployed |     | in the |     |     |     |     |
| ------------ | --- | ------ | ----- | --------------- | --- | -------- | --- | ------ | --- | --- | --- | --- |
streaming environment to make bitrate adaptation decisions Performancemetrics:ToevaluatetheQoEcomprehensively,
(line16).
theQoEfunctioninEq.(1)isfurtherextendedtothreevariants
(basedonMaoetal.[10])intermsofthemappingfrombitrate
bt( segmentt)tovideoqualityF(.):
|     |     | IV. PERFORMANCEEVALUATION |     |     |     |     |     |     | (cid:2) |     |     |     |
| --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
QoElinmaintainsalinearrelationshipbetweenbitrateand
| In this | section, | we  | evaluated | the | performance |     | of BETA | and |     |     |     |     |
| ------- | -------- | --- | --------- | --- | ----------- | --- | ------- | --- | --- | --- | --- | --- |
videoquality,i.e.,F(bt)=bt.Thepenaltycoefficientσ=
comparedittothestate-of-the-artABRalgorithms.Inaddition,
|             |     |                |     |         |                 |     |     |        | (cid:2) 50;      |                    |                 |     |
| ----------- | --- | -------------- | --- | ------- | --------------- | --- | --- | ------ | ---------------- | ------------------ | --------------- | --- |
| we explored |     | the underlying |     | factors | that contribute |     | to  | BETA’s |                  |                    |                 |     |
|             |     |                |     |         |                 |     |     |        | QoElog maintains | a log relationship | between bitrate | and |
superiority.
videoquality,i.e.,F(bt)=log(bt/rmin),rmin=0.2Mbps.
Thepenaltycoefficientσ=5.52;
| A. ExperimentalSetup |     |     |     |     |     |     |     |     | (cid:2)          |                     |               |         |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------------------- | ------------- | ------- |
|                      |     |     |     |     |     |     |     |     | QoEhd prefers    | high video quality: | if bt<5 Mbps, | then    |
|                      |     |     |     |     |     |     |     |     | F(bt) = 1.6bt+1; | if 5 Mbps<bt<10     | Mbps, then    | F(bt) = |
Baseline:TobenchmarktheperformanceofBETA,weimple-
|     |     |     |     |     |     |     |     |     | 1.6bt+25; | Mbps<bt<50 |     | =   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | --- |
mented six state-of-the-art ABR algorithms. These include: 1) if 10 Mbps, then F(bt)
1.6bt+50.Thepenaltycoefficientσ=30.
Twobasicalgorithms:MPC[7](heuristic-based),andPensieve
[10](DRL-based);2)Fouralgorithmsthatfocusonimproving
| the ABR | generalization: |     | PSQA | [5] | (parameter-tunning), |     |     | EAS |     |     |     |     |
| ------- | --------------- | --- | ---- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
B. QoEPerformance
[3](ensemblelearning),Genet[18](curriculumlearning),and
Merina [4] (meta reinforcement learning). A comprehensive TableIVsummarizestheQoEperformanceofthesevenABR
reviewoftheseABRapproachesisshowninSectionV. algorithms under three different QoE functions, as defined in
BETAparameter:Thedefaultsettingofthehyperparameters SectionIV-A.Acrossallthreecases,theproposedBETAcon-
of BETA is summarized in Table III. A sensitivity analysis sistentlyoutperformsthestate-of-the-artbaselines,achievinga
examiningtheirimpactwillbepresentedinSectionIV-E.Ad- 14.8%to37.9%improvementinmeanQoE.Tofurtherillustrate
ditionally,thestreamingenvironmentsettings,includingvideo thedistributionalcharacteristics,Fig.3presentstheCumulative
segmentation,bitrateladder,andnetworktracecharacteristics, DistributionFunction(CDF)ofper-sessionQoE.Comparedto
aredescribedindetailinSectionII. otheralgorithms,BETAyieldsasignificantlylowerproportion
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore.  Restrictions apply.

12860 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.24,NO.12,DECEMBER2025
| Fig. 3. | Cumulative | Distribution |     | Function | (CDF) distributions | of per- |     |     |     |     |     |     |     |
| ------- | ---------- | ------------ | --- | -------- | ------------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
streaming-sessionQoEperformance.
Fig.5. Comparisonofvideoqualityandrebufferingover7algorithms.
Fig.4. Comparisonofbitrateandrebufferingover7ABRalgorithms.
ofpoor-performingsessions(i.e.,QoE<0)andahighercon-
centrationofhigh-performingsessions,whichcontributestoits
superiormeanperformance. Fig. 6. QoE comparison over three different network conditions. Low
(0∼15Mbps),Medium(15∼25Mbps),andHigh(>25Mbps)arethreenetwork
| Among | the | comparison | algorithms, |     | EAS achieves | the most |     |     |     |     |     |     |     |
| ----- | --- | ---------- | ----------- | --- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- |
tracedatasetswithdifferentmeanthroughputs.
consistentperformanceacrossthethreeQoEfunctions,within
83.8%to84.7%ofBETA’sQoE.Incontrast,otheralgorithms
| exhibit morevariability.For |     |     |     | instance, | Merinaperformspoorly |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --------- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ofeachalgorithmbycomparingtheirQoEperformanceunder
| under the | Linear | QoE | (normalized | score | of 0.661), | due to | a   |     |     |     |     |     |     |
| --------- | ------ | --- | ----------- | ----- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
varyingnetworkconditions,asshowninFig.6.Specifically,the
highfractionofsessionswithsubstantialrebufferingevents,but
networktraceswerepartitionedintothreesubsetsbasedontheir
performsbetterundertheHDQoE(scoreof0.806).Others,such
|     |     |     |     |     |     |     |                  |     | (0∼15 |        |        | (15∼25 |        |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----- | ------ | ------ | ------ | ------ |
|     |     |     |     |     |     |     | mean throughput: |     | low   | Mbps), | medium |        | Mbps), |
asPSQAandMPC,showsimilartrendswithMerina.
|     |     |     |     |     |     |     | and high | (>25 | Mbps), | to reflect | different | ranges | of realistic |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ------ | ---------- | --------- | ------ | ------------ |
Fig.4comparestheaveragevideobitrateandrebufferingdu-
operatingenvironments.
rationacrossallalgorithms.Theresultsareparticularlyinsight-
|     |     |     |     |     |     |     | In Fig. | 6 (upper | left), | BETA | consistently | outperforms | all |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------ | ---- | ------------ | ----------- | --- |
ful.AlthoughBETAachievesthebestQoE,itsselectedbitrate
baselinealgorithmsacrossthethreenetworkconditions.Inthe
isnotalwaysthehighest.Instead,itmaintainsaconsistentlylow
mixednetworksetting,BETAachieves19.4%to50.9%higher
rebufferingduration,especiallyundertheLinearandLogQoE
meanQoE.Morenotably,underthelow-throughputcondition,
| functions    | where | rebuffering |         | carries a | greater    | penalty weight. |          |               |     |         |             |     |             |
| ------------ | ----- | ----------- | ------- | --------- | ---------- | --------------- | -------- | ------------- | --- | ------- | ----------- | --- | ----------- |
|              |       |             |         |           |            |                 | which is | characterized | by  | greater | variability | and | constrained |
| In contrast, | under | the         | HD QoE, | which     | emphasizes | high video      |          |               |     |         |             |     |             |
bandwidth,BETA’sadvantageisevenmorepronounced,achiev-
quality,BETAadaptsbyselectinghigherbitratesattheexpense
ingupto244.1%improvementovertheweakestbaselineandat
| of slightly | increased | rebuffering. |     | These | results | reflect BETA’s |             |      |               |      |     |                |        |
| ----------- | --------- | ------------ | --- | ----- | ------- | -------------- | ----------- | ---- | ------------- | ---- | --- | -------------- | ------ |
|             |           |              |     |       |         |                | least 39.3% | over | the strongest | one. | The | primary driver | behind |
abilitytoadaptitsABRpolicyflexiblyinaccordancewiththe
thisperformancegainisBETA’sabilitytosignificantlyreduce
varyingobjectivefunctions.
|     |     |     |     |     |     |     | rebuffering | events, | as illustrated |     | in Fig. | 6 (lower left). | Across |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | -------------- | --- | ------- | --------------- | ------ |
AmongthethreeQoEfunctions,onlytheLinearQoEdirectly
allnetworksubsets,BETAconsistentlyrecordstheshortestre-
| uses bitrate | to  | represent | video | quality. | The Log | and HD QoE |     |     |     |     |     |     |     |
| ------------ | --- | --------- | ----- | -------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
bufferingduration,highlightingitsrobustnessinadaptingtoboth
| functions | apply | nonlinear | mappings |     | (see Section | IV-A). To |     |     |     |     |     |     |     |
| --------- | ----- | --------- | -------- | --- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
bandwidth-limitedandhighlyfluctuatingnetworkconditions.
| better assess | the | actual | video | quality | across | algorithms, we |     |     |     |     |     |     |     |
| ------------- | --- | ------ | ----- | ------- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- |
ForadeeperunderstandingofBETA’ssuperiority,inFig.7(a),
| replaced      | the bitrate | values     | on    | the x-axis | of Fig. | 4 with their   |            |            |                 |           |     |                 |      |
| ------------- | ----------- | ---------- | ----- | ---------- | ------- | -------------- | ---------- | ---------- | --------------- | --------- | --- | --------------- | ---- |
|               |             |            |       |            |         |                | we plotted | its        | buffer dynamics | under     | the | three network   | con- |
| corresponding |             | quantified | video | quality    | scores, | and re-plotted |            |            |                 |           |     |                 |      |
|               |             |            |       |            |         |                | ditions    | to see its | ABR decision    | behavior. |     | The differences | are  |
theresultsinFig.5.Theoveralltrendsremainconsistent:BETA
readilyapparentacrossthethreecases.Forexample,atthelow
achievesthemostfavorabletrade-offbetweenvideoqualityand
|              |          |     |            |             |     |                  | network,  | it is  | clear that | the buffer | level  | of BETA    | is higher |
| ------------ | -------- | --- | ---------- | ----------- | --- | ---------------- | --------- | ------ | ---------- | ---------- | ------ | ---------- | --------- |
| rebuffering, | offering | a   | principled | explanation |     | for its superior |           |        |            |            |        |            |           |
|              |          |     |            |             |     |                  | than that | of the | other      | two cases  | (i.e., | the medium | and the   |
QoEperformanceacrossallevaluationcriteria.
highnetworks).Itintentionallyselectsthebitratesmuchlower
thanthemeasuredthroughputbecausethenetworkconditionis
C. NetworkRobustness
judgedtobepoorandhighmeasuredthroughputistreatedasthe
To assess whether the ABR Under-Generalization problem exceptionthatisunlikelytolast.Thus,maintainingahighbuffer
is effectively addressed, we evaluated the network robustness levelwouldeffectivelypreventthepotentialrebufferingevents
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore.  Restrictions apply.

ZHANGetal.:NOVELSPATIAL-TEMPORALLEARNINGMETHODFORENHANCINGGENERALIZATIONINADAPTIVEVIDEOSTREAMING 12861
TABLEV
COMPARISONOFQOEACROSSSEVENDRLMETHODS
Fig.8. ComparisonoftrainingQoEoversevenDRLmethods.
dynamicsinFig.7(notethatduetothesimilarityoftheresults,
we only show the results of EAS and Merina in Fig. 7(b) and
(c), respectively). It is observed that both EAS and Merina
perform differently from BETA. For example, the buffer level
ofEASisroughlyconsistentregardlessofwhetherthenetwork
fluctuates drastically or not in the three network conditions,
which is due to its dynamic ABR aggressiveness adjustment.
While such decisions can effectively reduce rebuffering, the
networkresourcescannotbefullyutilizedespeciallywhenthe
networkishigh.Bycontrast,Merine’sABRisfarlessflexible.
Ithasmuchlessbufferinginthelownetworkthaninthemedium
andhighnetworks,sosignificantrebufferingandunderutilized
networkresourcesareinevitablyincurred.
Fig.7. Bufferdynamicsoverthreedifferentnetworkconditions.Low(0∼15
Mbps),Medium(15∼25Mbps),andHigh(>25Mbps)arethreenetworktrace
D. TrainingEfficiency
datasetswithdifferentmeanthroughputs.
BETA’s model training plays a decisive role in its superior
performance.InSectionII,weevaluatedthetrainingefficiency
inthefuture.Atthemediumnetwork,BETAismoremoderate oftheexistingDRLmethods.Inthissection,wewillcompare
andbalanced.Atthehighnetwork,thebufferlevelismuchlower BETA to the existing ones in terms of QoE, video bitrate, re-
becauseBETAismoreaggressiveandevenoccasionallyselects buffering,andqualityvariations.Theresultsaresummarizedin
bitrates higher than the measured throughput. The intuition is TableV.ItisobservedthattheQoEofBETAismuchbetterthan
thatthelowmeasuredthroughputatthehighnetworkislikely the existing DRLs by 19.1% ∼ 25.0%. The major contributor
short-term so keeping high bitrates can prevent unnecessary is the substantial rebuffering reduction, by 37.3% ∼ 143.1%.
QoE degradations. Overall, BETA’s behavior fundamentally While the bitrate and the quality variation achieved by BETA
stemsfromitsflexibletuningofABRadaptationaggressiveness, are not the best among all these methods, BETA maintains a
whichenablesittomakenotonlyfine-graineddecisionsbutalso morebalancedresultbetweenthethreemetrics,offeringabetter
long-sightedplanning. overallQoE(i.e.,theoptimizationobjectiveofthetraining).
Amongthesecomparisonalgorithms,somehavegeneraliza- To further investigate the training behavior of the evaluated
tion awareness such as PSQA [5], EAS [3], Genet [18], and DRLmethods,Fig.8presentstheevolutionofQoEovertraining
Merina [4]. To see their effectiveness, we plotted the buffer epochs(x-axis). Importantly, QoE is evaluated on a validation
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

12862 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.24,NO.12,DECEMBER2025
Fig.10. SensitivityanalysisonthekeyparametersofBETA.
Fig.9. AblationanalysisfortemporalandspatialmodulesofBETA.
| trace set, | which | is completely |     | isolated | from | the | training set |     |     |     |     |     |     |     |     |
| ---------- | ----- | ------------- | --- | -------- | ---- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
atthevalueof5andtoosmall/largeavaluedegradestheresult.
| to ensure | generalization |     | assessment. |     | From | the figure, | we ob- |     |     |     |     |     |     |     |     |
| --------- | -------------- | --- | ----------- | --- | ---- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Thisindicatesthatitisnotasintuitivethatalongerlookahead
| served that | although | BETA |     | converges | more | slowly | compared |     |     |     |     |     |     |     |     |
| ----------- | -------- | ---- | --- | --------- | ---- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
horizonbringsbetterperformance.
| to methods | such | as DDPG |     | and SAC, | it ultimately |     | achieves |            |     |               |     |       |        |         |           |
| ---------- | ---- | ------- | --- | -------- | ------------- | --- | -------- | ---------- | --- | ------------- | --- | ----- | ------ | ------- | --------- |
|            |      |         |     |          |               |     |          | The second |     | key parameter |     | works | in the | spatial | module of |
substantiallyhigherQoE.Incontrast,thebaselineDRLmethods
|     |     |     |     |     |     |     |     | the training | which | is  | a pre-defined |     | QoE | threshold | (i.e., the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | --- | ------------- | --- | --- | --------- | ---------- |
exhibitsignificantinstability,particularlyTD3andDDPG,both
|          |        |       |     |             |          |     |              | gap between    | the | actual               | QoE | and the | offline | optimal)        | for the |
| -------- | ------ | ----- | --- | ----------- | -------- | --- | ------------ | -------------- | --- | -------------------- | --- | ------- | ------- | --------------- | ------- |
| of which | suffer | sharp | QoE | drops after | reaching |     | early peaks, |                |     |                      |     |         |         |                 |         |
|          |        |       |     |             |          |     |              | classification | of  | the normal-performed |     |         | and     | under-performed |         |
suggestingpossibleoverfittingorpoorgeneralization.
networktraces(c.f.SectionIII-B).Wetuneditsvaluefrom100
BETA’strainingframeworkintegratestwokeymodules:the
to2000toseetheeffectonQoEandclassificationaccuracy.In
TemporalModuleandtheSpatialModule(refertoSectionIII).
Fig.10-middle,itisobservedthatastheQoEthresholdincreases,
| To assess | their | individual | contributions, |     | we  | performed | an ab- |                    |     |          |       |             |     |      |             |
| --------- | ----- | ---------- | -------------- | --- | --- | --------- | ------ | ------------------ | --- | -------- | ----- | ----------- | --- | ---- | ----------- |
|           |       |            |                |     |     |           |        | the classification |     | accuracy | keeps | increasing. |     | This | is expected |
lationstudy,comparingtworeducedversionsofBETAagainst
|           |           |          |                    |     |         |          |             | because | the larger | the     | threshold, | the | easier | it is | to segregate |
| --------- | --------- | -------- | ------------------ | --- | ------- | -------- | ----------- | ------- | ---------- | ------- | ---------- | --- | ------ | ----- | ------------ |
| the full. | The first | variant, | BETA_w/o_Temporal, |     |         | excludes | the         |         |            |         |            |     |        |       |              |
|           |           |          |                    |     |         |          |             | the two | types of   | traces. | However,   | the | QoE    | shows | a different  |
| temporal  | module    | while    | retaining          | the | spatial | one.     | The second, |         |            |         |            |     |        |       |              |
patternwhichpeaksat700.From700to2000(QoEthreshold),
| BETA_w/o_Spatial, |     | removes |     | the spatial | module | but | preserves |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------- | --- | ----------- | ------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
eventhoughtheclassificationaccuracyincreases,theQoEdrops
| the temporal | logic.         | As  | shown       | in Fig.  | 9, both   | variants | exhibit      |                |     |            |          |     |          |        |                |
| ------------ | -------------- | --- | ----------- | -------- | --------- | -------- | ------------ | -------------- | --- | ---------- | -------- | --- | -------- | ------ | -------------- |
|              |                |     |             |          |           |          |              | substantially. | The | reason     | is that, | at  | runtime, | the    | classification |
| significant  | degradation    |     | in QoE      | compared |           | to the   | full version |                |     |            |          |     |          |        |                |
|              |                |     |             |          |           |          |              | inevitably     | has | errors. If | this is  | not | shown    | to the | ABR model      |
| of BETA.     | In particular, |     | the removal |          | of either | module   | leads        | to             |     |            |          |     |          |        |                |
duringtheofflinetraining,thenthetrainedABRmodelcannot
| a marked | increase | in         | rebuffering | duration |         | and a | reduction | in        |           |           |      |           |         |          |               |
| -------- | -------- | ---------- | ----------- | -------- | ------- | ----- | --------- | --------- | --------- | --------- | ---- | --------- | ------- | -------- | ------------- |
|          |          |            |             |          |         |       |           | get the   | knowledge | to cope   | with | such      | errors. | As       | a result, the |
| average  | bitrate, | indicating | that        | both     | modules | are   | essential | to        |           |           |      |           |         |          |               |
|          |          |            |             |          |         |       |           | ABR model | takes     | erroneous |      | behaviors | at      | runtime, | degrading     |
achievingBETA’srobustperformance.
theresultantQoE.
InSectionIV-C,weplottedthebufferdynamicstogaininsight
Thethirdparameteristhenetworktracelengthwhichisthe
| into the | network | robustness |     | of ABR | decisions, | where | BETA |           |           |      |         |        |            |     |             |
| -------- | ------- | ---------- | --- | ------ | ---------- | ----- | ---- | --------- | --------- | ---- | ------- | ------ | ---------- | --- | ----------- |
|          |         |            |     |        |            |       |      | length of | the input | data | for the | binary | classifier | in  | the spatial |
candynamicallyadjusttheABRaggressivenessacrossdifferent
|         |            |      |      |           |         |       |        | module | of the | training. | We tuned | its | value | from 20 | sec to 400 |
| ------- | ---------- | ---- | ---- | --------- | ------- | ----- | ------ | ------ | ------ | --------- | -------- | --- | ----- | ------- | ---------- |
| network | conditions | (see | Fig. | 7(a)). To | uncover | which | module |        |        |           |          |     |       |         |            |
sectoseeitseffectontheclassificationaccuracy.InFig.10-right,
| of BETA | achieves | this | efficacy, | we  | plot the | buffer | dynamics |     |     |     |     |     |     |     |     |
| ------- | -------- | ---- | --------- | --- | -------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
asexpected,theQoEincreasesasthelengthgetslongerbecause
| of BETA_w/o_Spatial |     |     | (i.e., | removing | the | spatial | module) | in  |     |     |     |     |     |     |     |
| ------------------- | --- | --- | ------ | -------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
theclassifierisabletoobtainmorecomprehensiveknowledge
| Fig. 7(d). | However, | it  | shows | a pattern | very | similar | to the full |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ----- | --------- | ---- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
withmorehistoricaltraces.
versionofBETA(Fig.7(a)).Tothisend,wefurtherremovedthe
|          |        |      |                   |     |     |         |             | To further | validate | the | robustness |     | of the | setting | of the QoE |
| -------- | ------ | ---- | ----------------- | --- | --- | ------- | ----------- | ---------- | -------- | --- | ---------- | --- | ------ | ------- | ---------- |
| temporal | module | from | BETA_w/o_Spatial, |     |     | leaving | the rest as |            |          |     |            |     |        |         |            |
threshold,wepartitionedtheevaluationnetworkdatabothtem-
theoriginalTD3[14]toobservetheeffect.InFig.7(e),thediffer-
porallyandspatially.Notably,thenetworktracedata[36]was
encesbegintoemerge(comparedtoBETA_w/o_Spatial),with
collectedfromrealmobilenetworksoveraspanof77consec-
| TD3’sbuffer | beingmoreconsistentacrossthethreenetworks. |     |     |     |     |     |     |             |     |            |       |           |     |           |          |
| ----------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------- | ----- | --------- | --- | --------- | -------- |
|             |                                            |     |     |     |     |     |     | utive days. | The | collection | sites | encompass |     | a diverse | range of |
ThisresultclearlydemonstratestheefficacyofBETA’stemporal
|     |     |     |     |     |     |     |     | geographic | locations, | including |     | subways, | campuses, |     | shopping |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --------- | --- | -------- | --------- | --- | -------- |
module,whichgivesthetrainedABRmodelalong-termview
malls,andmore.
andmoreflexibilitytomakedecisionsforspecificnetworks.
First,wedividedthenetworkdatatemporallyintofourgroups
|     |     |     |     |     |     |     |     | based on | their | collection | time: | 0:00–6:00, |     | 6:00–12:00, | 12:00– |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ---------- | ----- | ---------- | --- | ----------- | ------ |
E. SensitivityAnalysis
|     |     |     |     |     |     |     |     | 18:00, 18:00–24:00. |     | We  | then | conducted | a   | sensitivity | analysis |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ---- | --------- | --- | ----------- | -------- |
In BETA, some key parameters may significantly affect its fortheQoEthresholdacrosseachofthesetime-basedgroups.
performance so we conducted a sensitivity analysis on them. The results, presented in Table VI, consistently indicate that a
First, in the temporal module of the training, there is a look QoE threshold of 700 achieves the highest QoE performance
aheadhorizonincludingnconsecutivesegmentstocalculatethe acrossallfourcases.Second,toassessthesensitivityspatially,
expectedreward(c.f.SectionIII-C).ThisiskeytoBETAbecause we further extracted three groups of network data collected
itprovidesalong-sightedviewofthetrainingABRmodel.To from different geographic locations. The results, presented in
seeitseffectsonQoE,wetunedthevaluefrom1to40andthen Table VII, show that the QoE threshold of 700 consistently
plottedtheresultinFig.10-left.WeobservedthattheQoEpeaks achievesthehighestQoEacrossallthreecases.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore.  Restrictions apply.

ZHANGetal.:NOVELSPATIAL-TEMPORALLEARNINGMETHODFORENHANCINGGENERALIZATIONINADAPTIVEVIDEOSTREAMING 12863
TABLEVI TABLEIX
TEMPORALSENSITIVITYOFTHEQOETHRESHOLD TRAININGUPDATEFREQUENCY
TABLEVII
SPATIALSENSITIVITYOFTHEQOETHRESHOLD
TABLEX
ACTIONNOISEINTRODUCTION
TABLEVIII
TABLEXI
QVALUEESTIMATIONMETHODS
ONLINECOMPLEXITYANALYSIS
In conclusion, the QoE threshold keeps stable across the
diverse network environments. This stability stems from the
fact that the QoE threshold quantifies the performance gap
between the actual QoE and the offline optimum within each
videosession.Sincethisgapisarelativemeasure,itislargely
unaffectedbyvariationsinnetworkenvironments.Forexample,
inalow-bandwidthenvironment,boththeactualQoEandtheof-
flineoptimalQoEtendtobelower,whereasinahigh-bandwidth
environment,bothvaluesarehigher.Thus,therelativeQoEgap representinga6%improvementcomparedto=1.Additionally,
keepsfairlyconsistentacrossthetwoscenarios.Therefore,there thetrainingspeedimprovesastheepochnumberincreases.This
isnoneedtofine-tunetheQoEthresholdfordifferentnetwork isexpectedbecausewhentheepochnumberbetweenupdating
environments. theActorisincreased,thesystemrequiresfewerupdates,leading
At last, we test some training parameters. The first is the tolesscomputationalresourceconsumption.
Q-valueestimationmethod.Wetestedtwocandidatemethods: The third is the Action noise, which is to avoid premature
oneistheQ-valueestimatedbycalculatingtheaverageofthetwo convergence.TotestitsimpactonQoE,wevariedthestandard
targetvalues;theotheristhesmallerofthetwotargetQ-values. deviationoftheactionnoisewithin0.0to2.0,where0represents
As shown in Table VIII,the former one achieves only 93% of noactionnoise.AsshowninTableX,theQoEperformanceis
theperformancecomparedtothelatterone.Thisdifferencecan degraded when the noise is either too small or too large. The
beattributedtothefactthattakingthesmallerofthetwotarget best performance is achieved with a standard deviation of 1.0,
Q-values helps effectively avoid Q-value overestimation. The demonstratingthatthislevelofactionnoiseprovidestheoptimal
overestimation primarily results from the randomness in the balanceforenhancingQoE.
estimation process, such as the random tuple sampling from
theexperiencebuffer.
F. ComplexityAnalysis
Thenextisthetrainingupdatefrequency,whichreferstothe
number of epochs between two updates of the actor network. In the last experiment, we evaluated the complexity of the
We tuned it within the range 1 ∼ 32 to assess its impact on ABRalgorithms.Wequantifythecomplexitywiththepractical
QoE performance and training speed. As shown in Table IX, algorithmic runtime and the average memory occupancy eval-
astheepochnumberincreases,theQoEinitiallyincreasesand uated in the online streaming phase. Table XI summarizes the
then decreases, with the peak performance occurring at = 4, resultwherethealgorithmicruntimeistheaccumulationof100
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

12864 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.24,NO.12,DECEMBER2025
streamingsessions(atotalof19200sec),andthememoryoccu- includeDeepBuffer[25],abuffer-awareABRalgorithmtrained
pancyistheaverageusageofeachsecond.First,itisobserved via DCPPG; Jade [26], which incorporates human feedback
thatPSQAandMPChavesignificantlylongerruntimes(249.9 to align decisions with QoE preferences; and Incendio [27],
secand226.5sec)thanothers.ThisisbecausetheABRdecision whichusesmulti-agentreinforcementlearning[37]withexpert
of the two requires repeated querying of the hash tables [5], guidance.OthernotableexamplesincludeGreenABR[28],an
[7] while all other algorithms adopt neural networks that have energy-efficient ABR model trained via DQN; CAST [29],
a faster mapping speed. Second, Merina occupies the largest whichemploysself-playDRLtoconsidervideoscenecomplex-
memory usage (1188.7 MByte) among the all, which is due ity; and a data-wastage-aware ABR algorithm by Zhang et al.
to the meta-reinforcement-learning that holds a more complex [30],trainedwithA3Ctoreducebandwidthinefficiency.
neuralnetworkstructure[4],[34].Third,inboththealgorithmic Generalization-Aware ABR Solution: To address the ABR
runtimeandthememoryoccupancy,thecomplexityofBETAis Under-Generalizationproblem,severalrepresentativesolutions
moderateamongallthealgorithms. have been proposed in recent years. PSQA [5], developed by
Next, regarding the resource-intensive nature of computing Zhang et al., provides a general framework for tuning internal
the offline optimal, we provided a complexity analysis for the ABRparametersforspecificnetworkconditions.EAS[3],also
offlinetrainingofBETA(thetrainingincludestheofflineoptimal byZhangetal.,constructsanensembleofABRmodelstailored
computation).Thecomputingserverspecificationsare:CPU– to different mean throughput levels. Genet [18], proposed by
Intel Xeon Platinum 8375C @ 2.90 GHz; CPU cores – 128; Xiaetal.,adoptscurriculumlearningtodynamicallyadjustthe
Motherboard – R0K8F35; Operating system – Ubuntu 22.04 trainingdatadistributiontoimprovegeneralization.Inparallel,
LTS;Memory–256GB;GPU–NVIDIAGeForceRTX4090; meta-reinforcement learning has been explored by Kan et al.
GPUCores–2. [4]andBentalebetal.[11],bothofwhichemployanauxiliary
Thetrainingcomplexityissummarizedasfollows: featureextractionnetworktoenablerapidadaptationoftheABR
(cid:2)
DRLtrainingspeed–96epochsperminute policytodiversenetworks.
(cid:2)
TotalDRLtrainingtime–2∼2.5hours Discussion: The key limitation of the existing ABR algo-
(cid:2)
GPUutilization–8% rithms, including both heuristic-based and learning-based ap-
(cid:2)
Memoryconsumption–0.45GB proaches, is that they typically rely on a single ABR model
(cid:2)
Offlineoptimalcomputation(usingthedynamicprogram- (e.g.,astandaloneneuralnetwork),asseeninthestate-of-the-art
ming algorithm with a time granularity of 0.05) – 1 hour algorithmssuchastheA3C-basedPensieve[10],thecurriculum
for1000epochs learning-basedGenet[18],andthemeta-reinforcementlearning-
Overall,theofflinetrainingofBETAistypicallycompleted basedMerina[4].However,real-worldnetworkconditionsare
within4hours,makingthecomputationaloverheadmanageable highlycomplexandcharacterizedbydiversefeatures,someof
withinastandardserverenvironment. which cannot even be quantified. As a result, the solo ABR
model struggles to incorporate all the network features effec-
tivelyandfailstoachievebalancedresultsinheterogeneousnet-
V. RELATEDWORK
workenvironments.Thisisthekeycauseofthegeneralization
Overthepastdecade,adaptivevideostreaminghasundergone issue.
significantadvancementsunderthestandardizationprotocolof Fundamentally, BETA differs from the existing ABR algo-
DASH[2],[33].Inthissection,weprovideastructuredreview rithms.Itfirstclassifiesthenetworkdataofallstreamingsessions
oftheexistingABRresearch. into two categories by analyzing the gap between the actual
Heuristic-basedABR:Heuristic-basedalgorithmsrelyonpre- QoEandtheofflineoptimalQoEofeachsession.Sessionswith
definedrules.Forexample,Jiangetal.[6]proposedFESTIVE, a large QoE gap are labeled as poor-performing, while those
which selects the bitrate based on the harmonic mean of past withasmallgapareconsiderednormal.BETAthentrainstwo
throughput.Spiterietal.[8]developedBOLA,whichusesbuffer distinct ABR models for these two categories. At runtime, it
occupancyandLyapunovoptimizationfordecision-making.Yin dynamically switches between the two models based on real-
etal.[7]introducedRobustMPC,whichformulatesbitrateselec- time network conditions. This design provides a practical and
tionasaQoEmaximizationproblem.Akhtaretal.[9]proposed effective solution to the long-standing generalization issue in
Oboe,whichdynamicallyadjustsRobustMPC’sdiscountfactor ABRdecision-making.
to better adapt to network variability. Zuo et al. [19] designed
Ruyi, which incorporates user preferences into QoE optimiza-
VI. CONCLUSIONANDFUTUREWORK
tion. Xu et al. [20] presented Karma, using causal sequence
modeling for adaptive decisions. Chen et al. [21] proposed This work reveals the ABR Under-Generalization problem
SODA,whichappliessmoothedonlineconvexoptimizationto that exists in the state-of-the-art ABR algorithms. To address
reducequalityfluctuations. this problem, we proposed BETA, a novel DRL-based ABR
Learning-basedABR:Theotherbranchleveragesdeeprein- framework that incorporates spatial and temporal modules to
forcementlearning(DRL)totrainABRalgorithms.Forexam- enhance generalization across diverse network environments.
ple, Pensieve [10] is one of the earliest DRL-based methods, ExtensiveevaluationsdemonstratethatBETAconsistentlyout-
using A3C [12] for policy learning. Several follow-up imple- performs the existing algorithms in terms of QoE, while also
mentations have explored alternative DRLalgorithms,suchas exhibiting strong robustness. This indicates that it effectively
PPO[22],SAC[23],andDQN[24].Morerecentadvancements overcomesthegeneralizationproblem.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.

ZHANGetal.:NOVELSPATIAL-TEMPORALLEARNINGMETHODFORENHANCINGGENERALIZATIONINADAPTIVEVIDEOSTREAMING 12865
While BETA focuses on improving generalization with [20] B. Xu, H. Chen, and Z. Ma, “Karma: Adaptive video streaming via
respect to network conditions, real-world streaming scenar- causalsequencemodeling,”inProc.ACMInt.Conf.Multimedia,2023,
pp.1527–1535.
| ios involve broader | challenges, including | heterogeneous | QoE |                                                                     |     |     |     |     |     |     |
| ------------------- | --------------------- | ------------- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                     |                       |               |     | [21] T.Chenetal.,“SODA:Anadaptivebitratecontrollerforconsistenthigh |     |     |     |     |     |     |
preferences,evolvinguserbehaviors,anddevicediversity.Ad- qualityvideostreaming,”inProc.ACMSpecialInt.GroupDataCommun.,
2024,pp.1–14.
dressingtheseaspectsremainsapromisingdirectionforfuture
|     |     |     |     | [22] “PensieveimplementedbyPPO,”2021,[Online].Available:https://github. |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
research.
com/godka/Pensieve-PPO
|     |     |     |     | [23] “Pensieve | implemented |     | by SAC,” | 2021, [Online]. | Available: | https:// |
| --- | --- | --- | --- | -------------- | ----------- | --- | -------- | --------------- | ---------- | -------- |
github.com/godka/Pensieve-SAC
ACKNOWLEDGMENT
|     |     |     |     | [24] “Pensieve | implemented |     | by DQN,” | 2021, [Online]. | Available: | https:// |
| --- | --- | --- | --- | -------------- | ----------- | --- | -------- | --------------- | ---------- | -------- |
github.com/godka/Pensieve-PPO/tree/dqn
Theauthorswishtothanktheassociateeditorandtheanony-
|     |     |     |     | [25] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,andL.Sun,“Bufferawareness |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
mousreviewersfortheirinsightfulcommentsinimprovingthis
neuraladaptivevideostreamingforavoidingextrabufferconsumption,”
inProc.IEEEConf.Comput.Commun.,2023,pp.1–10.
paper.
|     |     |     |     | [26] T. Huang, | R.  | Zhang, C. | Wu, and | L. Sun, “Optimizing | adaptive | video |
| --- | --- | --- | --- | -------------- | --- | --------- | ------- | ------------------- | -------- | ----- |
streamingwithhumanfeedback,”inProc.ACMInt.Conf.Multimedia,
|     | REFERENCES |     |     | 2023,pp.1707–1718. |           |           |          |        |                |     |
| --- | ---------- | --- | --- | ------------------ | --------- | --------- | -------- | ------ | -------------- | --- |
|     |            |     |     | [27] Y. Li,        | Q. Zheng, | Z. Zhang, | H. Chen, | and Z. | Ma, “Improving | ABR |
[1] Cisco Visual Networking Index: Global Mobile Data Traffic Forecase performanceforshortvideostreamingusingmulti-agentreinforcement
Update,2017-2022.SanJose,CA,USA:CiscoInc.,Mar.2020.[Online]. learningwithexpertguidance,”inProc.WorkshopNetw.OperatingSystem
Available: https://www.cisco.com/c/en/us/solutions/collateral/service- SupportDigit.AudioVideo,2023,pp.58–64.
“GreenABR+:
provider/visual-networking-index-vni/white-paper-c11-741490.html [28] B. Turkkan et al., Generalized energy-aware adaptive
[2] T. Stockhammer, “Dynamic adaptive streaming over HTTP: Standards bitrate streaming,” ACM Trans. Multimedia Comput. Commun. Appl.,
and design principles,” in Proc. ACM Conf. Multimedia System, 2011, vol.20,2024,Art.no.269.
pp.133–144. [29] W. Li et al., “Optimizing video streaming in dynamic networks: An
[3] G.ZhangandJ.Lee,“Ensembleadaptivestreaming–Anewparadigmto intelligentadaptivebitratesolutionconsideringsceneintricacyanddata
generatestreamingalgorithmsviaspecializations,”IEEETrans.Mobile budget,”IEEETrans.MobileComput.,vol.23,no.12,pp.12280–12297,
| Comput.,vol.19,no.6,pp.1346–1358,Jun.2020. |     |     |     | May2024. |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
[4] N. Kan, Y. Jiang, C. Li, W. Dai, J. Zou, and H. Xiong, “Improving [30] G. Zhang et al., “DUASVS: A mobile data saving strategy in short-
generalizationforneuraladaptivevideostreamingviametareinforcement form video streaming,” IEEE Trans. Serv. Comput., vol. 16, no. 2,
learning,”inProc.ACMInt.Conf.Multimedia,2022,pp.3006–3016. pp.1066–1078,Mar.2023.
[5] G. Zhang, J. Zhang, Y. Liu, H. Hu, J. Y. B. Lee, and V. Aggarwal, [31] “Video streaming emulator,” 2017, [Online]. Available: https://github.
“Adaptive video streaming with automatic quality-of-experience opti- com/hongzimao/pensieve
mization,”IEEETrans.MobileComput.,vol.22,no.8,pp.4456–4470, [32] “The source code of BETA,” 2024, [Online]. Available: https://github.
| Aug.2023. |     |     |     | com/ZM-SDUr/BETA/ |     |     |     |     |     |     |
| --------- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
[6] J.Jiang,V.Sekar,andH.Zhang,“Improvingfairness,efficiency,andstabil- [33] “dash.js,” 2014, [Online]. Available: https://github.com/Dash-Industry-
| ityinHTTP-basedadaptivevideostreamingwithFESTIVE,”IEEE/ACM |     |     |     | Forum/dash.js/wiki |          |         |          |              |         |            |
| ---------------------------------------------------------- | --- | --- | --- | ------------------ | -------- | ------- | -------- | ------------ | ------- | ---------- |
|                                                            |     |     |     | [34] W. Du,        | L. Geng, | J. Liu, | Z. Zhao, | C. Wang, and | J. Huo, | “Decoupled |
Trans.Netw.,vol.22,no.1,pp.97–108,Feb.2014.
[7] X.Yin,A.Jindal,V.Sekar,andB.Sinopoli,“AControl-TheoreticAp- knowledgedistillationmethodbasedonmeta-learning,”High-Confidence
proachforDynamicAdaptiveVideoStreamingoverHTTP,”inProc.ACM Comput.,vol.4,no.1,Mar.2024,Art.no.100164.
SpecialInt.GroupDataCommun.,London,U.K.,2015,pp.325–338. [35] Z. Wang, G. Zhang, M. Xiao, D. Yu, and X. Cheng, “BETA: A novel
[8] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal learning-based adaptive streaming approach with spatial and temporal
bitrateadaptationforonlinevideos,”IEEE/ACMTrans.Netw.,vol.28, optimization,”inProc.IEEEInt.Conf.Sens.Commun.Netw.,Phoenix,
| no.4,pp.1698–1711,Aug.2020. |     |     |     | AZ,USA,2024,pp.1–9. |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
[9] Z.Akhtar,Y.S.Nam,andR.Govindan,“Oboe:Auto-tuningvideoABR [36] “Network trace data,” 2022, [Online]. Available: https://github.com/
algorithmstonetworkcondition,”inProc.ACMSpecialInt.GroupData Streaming-code/TraceData/releases/tag/TraceData
Commun.,2018,pp.44–58. [37] H.Liu,“Cooperativemulti-agentgamebasedonreinforcementlearning,”
[10] H.Mao,R.Netravali,andM.Alizadeh,“Neuraladaptivevideostreaming High-ConfidenceComput.,vol.4,no.1,Mar.2024,Art.no.100205.
withpensieve,”inProc.ACMSpecialInt.GroupDataCommun.,2017,
pp.197–210.
[11] A.Bentaleb,M.Lim,M.N.Akcay,A.C.Begen,andR.Zimmermann, Guanghui Zhang received the PhD degree from
“Metareinforcementlearningforrateadaptation,”inProc.IEEEConf. theDepartmentofInformationEngineering,Chinese
Comput.Commun.,2023,pp.1–10.
UniversityofHongKong,in2020,andtheMSdegree
[12] V.Mnih,A.P.Badia,M.Mirza,andA.Graves,“Asynchronousmethods
|     |     |     |     |     |     | in  | electronic science | and technology |     | from Peking |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | -------------- | --- | ----------- |
fordeepreinforcementlearning,”inProc.Int.Conf.Mach.Learn.,2016, University,in2016.Heiscurrentlyaprofessorwith
| pp.1928–1937. |     |     |     |     |     | the | School of | Computer Science | and | Technology, |
| ------------- | --- | --- | --- | --- | --- | --- | --------- | ---------------- | --- | ----------- |
[13] T.Lillicrapetal.,“Continuouscontrolwithdeepreinforcementlearning,” ShandongUniversity,China.From2020to2022,he
Sep.2015,arXiv:1509.02971.
workedasapostdoctoralresearcherwiththeChinese
[14] S.Fujimoto,H.Hoof,andD.Meger,“Addressingfunctionapproximation
|     |     |     |     |     |     | University | of Hong | Kong, | and then | as a research |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | ----- | -------- | ------------- |
error in actor-critic methods,” in Proc. Int. Conf. Mach. Learn., 2018, assistantprofessorwiththeHongKongBaptistUni-
pp.1587–1596. versity.Hisresearchinterestsincludebroadlyliesin
[15] V.Mnihetal.,“Human-levelControlthroughDeepReinforcementLearn- networkingsystems,multimediasystems,andmachinelearning.
ing,”Nature,vol.518,no.7540,pp.529–533,Feb.2015.
[16] J.Schulman,F.Wolski,P.Dhariwal,A.Radford,andO.Klimov,“Proximal
ZimingWangiscurrentlyworkingtowardtheMSc
Policyoptimizationalgorithms,”2017,arXiv:1707.06347.
|     |     |     |     |     |     | degree | with the | School of | Computer | Science and |
| --- | --- | --- | --- | --- | --- | ------ | -------- | --------- | -------- | ----------- |
[17] T.Haarnoja,A.Zhou,P.Abbeel,andS.Levine,“Softactor-critic:Off-
|     |     |     |     |     |     | Technology, | Shandong | University, | China. | His re- |
| --- | --- | --- | --- | --- | --- | ----------- | -------- | ----------- | ------ | ------- |
policymaximumentropydeepreinforcementlearningwithastochastic
actor,”inProc.Int.Conf.Mach.Learn.,2018,pp.1861–1870. search interests include broadly lies in networking
systems,multimediasystems,andmachinelearning.
[18] Z.Xia,Y.Zhou,F.Y.Yan,andJ.Jiang,“Genet:Automaticcurriculum
generationforlearningadaptationinnetworking,”inProc.ACMSpecial
Int.GroupDataCommun.,2022,pp.397–413.
[19] X.Zuo,J.Yang,M.Wang,andY.Cui,“Adaptivebitratewithuser-level
QoEpreferenceforvideostreaming,”inProc.IEEEConf.Comput.Com-
mun.,022,pp.1279–1288.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore.  Restrictions apply.

12866 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.24,NO.12,DECEMBER2025
Huaren Weiis currentlyworkingtowardtheMSc DongxiaoYu(SeniorMember,IEEE)receivedthe
degree with the School of Computer Science and BSdegreeinmathematicsfromShandongUniversity,
Technology, Shandong University, China. His re- in2006,andthePhDdegreeincomputersciencefrom
searchinterestsincludebroadlynetworkingsystems, theUniversityofHongKong,in2014.Hebecame
multimediasystems,andmachinelearning. anassociateprofessorwiththeSchoolofComputer
Science and Technology, Huazhong University of
ScienceandTechnology,in2016.Currently,heisa
professorwiththeSchoolofComputerScienceand
Technology,ShandongUniversity.Hisresearchinter-
estsincludewirelessnetworking,distributedcomput-
ing,andgraphalgorithms.
MengbaiXiaoreceivedtheMSdegreeinsoftware
engineeringfromtheUniversityofScienceandTech-
nologyofChina,in2011,andthePhDdegreeincom-
putersciencefromGeorgeMasonUniversity,in2018.
HeisaprofessorwiththeSchoolofComputerScience
andTechnology,ShandongUniversity,China.Hewas
apostdoctoralresearcherwiththeHPCSLab,Ohio XiuzhenCheng(Fellow,IEEE)receivedtheMSand
StateUniversity.Hisresearchinterestsincludemul- PhDdegreesincomputersciencefromtheUniver-
timediasystems,parallelanddistributedsystems.He sityofMinnesota–TwinCities,in2000and2002,
haspublishedpapersinprestigiousconferences,such respectively.ShewasafacultymemberwiththeDe-
asACMMultimedia,ACMICS,IEEEICDE,IEEE partmentofComputerScience,GeorgeWashington
ICDCS,andIEEEINFOCOM. University,from2002-2020.Currently,sheisapro-
fessorofcomputersciencewithShandongUniver-
sity,Qingdao,China.Herresearchinterestsinclude
focusesonblockchaincomputing,IOTSecurity,and
privacy-awarecomputing.
HuiYuan(SeniorMember,IEEE)receivedtheBE
and PhD degrees in telecommunication engineer-
ing from Xidian University, Xi’an, China, in 2006
and 2011, respectively. In 2011, he joined Shan-
dongUniversity,Ji’nan,China,asalecturer(April
2011–December2014),anassociateprofessor(Jan-
uary2015-August2016),andaprofessor(September
2016).Hisresearchinterestsinclude3Dvisualmedia
codingandcommunication.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:42:15 UTC from IEEE Xplore. Restrictions apply.