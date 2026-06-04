2422 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.23,NO.3,MARCH2024
MetaABR: A Meta-Learning Approach on
Adaptative Bitrate Selection for Video Streaming
WenzhongLi ,Member,IEEE,XiangLi,YetingXu,YiYang,andSangluLu ,Member,IEEE
Abstract—VideostreamingisoneofthemostpopularInternet of21.3%from2022to2030.ThestudyfromEricsson2reported
applications that makes up a large amount of Internet traffic. A thatvideostreamingcurrentlystandsoutasthemostsignificant
fundamental mechanism in video streaming is adaptive bitrate
traffictypeconsumedbysmartphoneusers,anditisprojectedto
(ABR) selection which decides the proper compression level for
accountfor74percentofInternettrafficbytheendof2024.The
eachchunkofavideotooptimizetheusers’qualityofexperience
(QoE).TheexistingABRalgorithmsrequiresignificanttuningand fundamentaldesignofamediastreamingsystempaysincreasing
donotgeneralizetodiversenetworkconditionsandpersonalized attentiontoguaranteetheusers’QualityofExperience(QoE).
QoE objectives. In this article, we propose a novel framework Itwasshowed[1]thatusersstartedtoabandonavideoifittook
for meta-learning based ABR design and discuss challenges of
morethan2secondstostartup,witheachincrementaldelayof
deploying learning based ABR mechanism in real-world video
1 s resulting in a 5.8% increase in the abandonment rate, and
streamingsystems.Weutilizetheproposedframeworktodesign
MetaABR, a novel adaptive bitrate selection algorithm based on a moderate amount of interruptions can decrease the average
meta-reinforcement learning to maximize users’ QoE. By jointly play time of a viewer by a significant amount. Therefore, it is
trainingmultiplelearning taskswithasharedmeta-critic,itcan important for content providers to provide high-quality fluent
provide transferrable meta-knowledge to supervise bitrate selec-
videostreamingservicetotheirusers.
tion across tasks, and can be applied to efficiently learn a new
Dynamic Adaptive Streaming over HTTP (DASH) [2] is
task in unseen environment with only a few trials. We imple-
mentMetaABRonanemulationplatformwhichconnectstothe the predominant form of video delivery in Internet. In DASH
Linuxnetworkprotocolstackthroughvirtualnetworkinterfaces. systems,videosarestoredonserversasmultiplechunks,each
Extensive experiments based on real-world traces and wireless ofwhichisencodedatseveraldiscretebitrates,whereahigher
testbedshowthatMetaABRachievesthebestcomprehensiveQoE
bitrate implies a higher quality and a longer download time.
comparedwiththestate-of-the-artABRalgorithmsinavarietyof
Adaptive bitrate (ABR) selection is the fundamental logic in
networkenvironments.
video streaming that runs on the client-side video players and
IndexTerms—Bitrateadaptation,meta-learning,reinforcement
dynamicallychooseabitrateforeachvideochunktooptimize
learning,videostreaming.
users’ QoE. Selecting the right bitrate in dynamic network is
challengingduetothevariabilityofnetworkconditionsandthe
I. INTRODUCTION trade-offofconflictingvideoQoErequirements[3],[4],[5].
Conventional ABR algorithms adopted a model-based ap-
RECENT years have witnessed a rapid growth of Internet
proach that used mathematical models to describe network
videostreamingapplications.Videoondemand(VoD)ser-
conditions and made bitrate decisions based on the estimation
viceshavestimulatedarevolutioninvideocontentconsumption
of network throughput [6], [7], [8], [9], [10] and playback
byprovidingaudiencesaplatformtowatchwhatevertheywant
buffer occupancy [11], [12]. For example, FESTIVE [8] used
anytime. According to the report,1 the global video streaming
the harmonic mean of download speed over recent chunks to
market size was valued at USD 70.59 billion in 2022, and is
predictthethroughputandproposedastatefulbitrateselection
expectedtoexpandatacompoundannualgrowthrate(CAGR)
to compensate for the biased interaction between bitrate and
estimated bandwidth. BBA [11] was a buffer-based approach
whichselectedbitratesbasedonplaybackbufferoccupationand
Manuscriptreceived7May2022;revised26February2023;accepted7March
2023.Dateofpublication21March2023;dateofcurrentversion5February estimationoffuturecapacityfrompastobservations.MPC[13]
2024.ThisworkwaspartiallysupportedbytheNaturalScienceFoundationof developedamodelpredictivecontrolalgorithmthatcombined
JiangsuProvinceProject“ResearchonFrontierBasicTheoryandMethodof
both throughput estimates and buffer occupancy information
SecurityDefenseforPowerSystemswithHigh-dimensionalUncertainFactors”
underGrantBK20222003,inpartbytheNationalNaturalScienceFoundationof to select bitrates to maximize QoE over a horizon of several
ChinaGrants61972196,61832008,and61832005,inpartbytheCollaborative future chunks. However, model-based ABR algorithms failed
InnovationCenterofNovelSoftwareTechnologyandIndustrialization,andthe
to achieve optimal performance across a broad set of network
Sino-GermanInstitutesofSocialComputing.Recommendedforacceptanceby
G.Xylomenos.(Correspondingauthor:WenzhongLi.) conditionsandQoEobjectivesduetotheirfixedcontrolrules.
The authors are with the State Key Laboratory for Novel Software In recent years, learning-based ABR algorithms [4], [5],
Technology, Nanjing University, Nanjing, Jiangsu 210093, China (e-mail:
[14], [15], [16] were proposed to address the issues of bitrate
lwz@nju.edu.cn; mf1933051@smail.nju.edu.cn; mf20330097@smail.nju.
edu.cn;171860540@smail.nju.edu.cn;sanglu@nju.edu.cn).
DigitalObjectIdentifier10.1109/TMC.2023.3260086
1https://www.grandviewresearch.com/industry-analysis/video-streaming- 2https://www.ericsson.com/en/reports-and-papers/mobility-report/articles/
market streaming-video
1536-1233©2023IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:29:03 UTC from IEEE Xplore. Restrictions apply.

LIetal.:METAABR:AMETA-LEARNINGAPPROACHONADAPTATIVEBITRATESELECTIONFORVIDEOSTREAMING 2423
|     |     |     |     |     |     |     | Fig.2. PerformanceofPensieve[5]DRLagentstrainedwithdifferentdatasets, |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------------- |
whereHybridmeansthedatasetcombining3G,WiFiand4Gtraces(detailsare
Fig.1. Performanceofapre-trainedDRLagent(Pensieve[5]trainedon3G
| dataset)testingondifferentnetworkenvironments(detailsareinSectionV-C2). |            |         |                |            |          |      | inSectionV-C1). |
| ----------------------------------------------------------------------- | ---------- | ------- | -------------- | ---------- | -------- | ---- | --------------- |
| adaptation                                                              | in varying | network | conditions.    |            | CS2P [4] | used | a               |
| data-driven                                                             | approach   | to      | learn clusters | of similar | sessions | and  |                 |
aHidden-Markov-Model(HMM)basedmidstreampredictorto
| model the     | stateful       | evolution | of throughput. |            | Fugu [16]    | adopted  |     |
| ------------- | -------------- | --------- | -------------- | ---------- | ------------ | -------- | --- |
| a supervised  | learning       | approach  | from           | the server | side         | to train | a   |
| probabilistic | predictor      | of        | upcoming       | chunk      | transmission | times    |     |
| and used      | the prediction |           | information    | to improve | the          | control  |     |
policyofMPC.Afewworks [5],[14],[15],[17]appliedDeep Fig.3. Illustrationofmeta-criticbasedbitrateadaptation.
| Reinforcement | Learning |             | (DRL) to | train an         | agent to | generate |     |
| ------------- | -------- | ----------- | -------- | ---------------- | -------- | -------- | --- |
| ABR policy    | by       | interacting | with     | the environment. |          | They did |     |
not rely on pre-programmed models or assumptions about the itondifferentnetworkenvironmentsinFig.2.Asillustratedin
environment, and gradually learned the best policy for bitrate Figs.2(a)to(c),themodeltrainedwithmultiplenetworktraces
decisions through observation and experience. For example, does not improve adaptivity, and it performs even worse than
Pensieve[5]isastate-of-the-artABRschemebasedonDRL.It thosetrainedwithasinglenetworkdataset.Thepooradaptivity
representeditscontrolpolicyasaneuralnetworkthatmapped with mixture datasets is probably caused by dataset shift [18],
raw observations (e.g., throughput samples, playback buffer [19]:thejointdistributionofinputsandoutputsdiffersbetween
occupancy, video chunk sizes) to the bitrate decision for the trainingandteststages.Inourexample,theDRLmodeltrained
nextchunk,whichprovidedanexpressiveandscalablewayto tofitdataonawidedistribution(3G+WiFi+4G)andtestedonly
incorporatearichvarietyofobservationsintotheABRpolicy. onarelativelynarrowdistributionwillresultinadegradationof
| Despite | the flexibility |     | and effectiveness |     | of the DRL-based |     | performance. |
| ------- | --------------- | --- | ----------------- | --- | ---------------- | --- | ------------ |
ABR algorithms, there remain a number of challenges to de- Inthisarticle,weproposeMetaABR,anovelABRalgorithm
ploy them in real-world video streaming systems. (C1) Long basedonmeta-learningtoaddresstheabovechallenges.Meta-
bootstraptime:TheDRL-basedmethodsneedtocollectalarge learning is a learning approach that uses the experience and
amount of training data by exploring various of actions in meta-datafromthepastlearningtaskstoadaptquicklytonew
differentnetworkenvironments,whichtypicallyrequiresseveral tasks.ThebasicideaoftheproposedMetaABRisillustratedin
hours(e.g.,8hoursreportedinPensieve[5])toformapre-trained Fig. 3. Assume there are a number of learning tasks that learn
neural network model. (C2) Lack of knowledge transfer: The ABRpoliciesondifferentnetworkenvironments(e.g.,WiFi,4G
existingDRLalgorithmsaretypicallytask-specificandtrained andEthernet).UnlikeconventionalDRLmethodsthattrainthe
toworkonaspecificnetworkenvironmentindependently,which tasksseparatively,themeta-learningapproachtrainsallthetasks
arehardtodealwithunseenscenarios.Asanexample,weadopt jointlywithasharedmeta-criticmodule.Thebenefitsoftraining
thePensieve[5]algorithmtotrainaDRLagentona3Gnetwork, multipletaskswithameta-learningapproacharethreefold[20],
andthenapplytheagentforbitrateselectionondifferentnetwork [21],[22].Firstly,itcanlearntask-levelmetaexperiencesthat
conditions in Fig. 1. It is shown that the agent performs well helpalgorithmsbetteradapttonewtaskswithoptimizationof
on the working environment the same as the training network hyper parameters. Besides, because of its support of learning
(see Fig. 1(a)), whereas it performs poorly on the WiFi and fromfewersamples,itthusincreasesthespeedoftrainingpro-
4G networks, whose QoEs (see Fig. 1(b) and (c)) are close cessbylimitingthenecessaryexperiments.Finally,bylearning
to or lower than that of simple model-based algorithms such multipletasks,meta-learningcanbuildmoregeneralizedmodels
as BBA [11] and RobustMPC [13]. (C3) Poor adaptivity: The thatadaptbettertochangingconditions.
existingDRLmodelstrainedforaclientcannotbegeneralized In the proposed framework, each DRL agent observes the
tootherclientseventheyoperateonsimilarenvironments.Asa networkstatesincludingtheclientplaybackbufferoccupancy,
result,itishardtotrainageneralizedmodeltocopewithdifferent past bitrate decisions, and several raw network signals (e.g.,
network types even rich historical datasets are available. For throughput measurements), and feeds these values to its local
example, we use an augmented hybrid dataset combining 3G, model represented as a neural network. The client chooses a
WiFi and 4G network traces to train a DRL model and apply bitrateforthenextvideochunkbasedonthesemetrics,which
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:29:03 UTC from IEEE Xplore.  Restrictions apply.

2424 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.23,NO.3,MARCH2024
results in a QoE metric observed and passed back to the DRL detailedmechanismofbitrateadaptationbasedonmetalearn-
agentasareward.Thestatesandrewardsofthetasksarepassed ing.SectionIVproposesthetrainingmethodfortheproposed
tothemeta-critictotrainametamodeltosupervisetheagentsto meta-critic and task-specific actors. Section V evaluates the
selectsuitablebitratestomaximizetheQoEmetric.Byjointly system performance with extensive experiments. The paper is
trainingtheDRLagentswiththemeta-critic,thesharedmeta- concludedinSectionVI.
criticgainstheabilitytoprovidetransferrableknowledgeamong
past learning tasks, which can be applied to efficiently learn a II. RELATEDWORK
newtargettaskinunseenenvironment.
In this section, we introduce the related works in terms of
Specifically,theproposecMetaABRcaneffectivelyaddress
ABRschemesforvideostreamingandmetalearning.
the above challenges (C1-C3) of video streaming systems.
Firstly,MetaABRtrainsageneralmeta-modeltoteachtheDRL
A. ABRSchemesforVideoStreaming
agentstoperformbitrateselection,whichenablesanewagentto
befastlytrainedonatargetenvironment(withoutlongbootstrap The ABR schemes for video streaming can be classified
time).AsshowninSectionV-C3,MetaABRtrainsaDRLagent into two categories: the model-based and the learning-based
muchfasterthanregularDRLmethods,whoseconvergencetime methods.
is about 1/10 of that of Pensieve. Secondly, with the proposed 1) Model-Based Methods: Model-based methods estab-
meta-learning method, a DRL agent can be trained to learn lished mathematical models to describe network conditions
transferable knowledge from historical tasks, which gains the and make ABR decisions based on the estimation of available
abilitytobeappliedinunseenenvironment.Meta-learninghas networkbandwidthandplaybackbufferoccupancy.TheProbe
theadvantageofcapturingthegeneralknowledgeacrosssimilar AND Adapt (PANDA) [6] method estimated the bottleneck
learningtasksinthepasttoimprovetheperformanceoflearning bandwidthandtriedtoeliminatetheON-OFFsteadystateissue
new tasks to achieve knowledge transfer. As shown in Sec- aswellasreducebitrateoscillationswhenmultipleclientsshared
tionV-C2,aMeteABRmodelcanbetrainedwiththe3Gnetwork thesamebottlenecklink.ThepiStream[7]methodwasavideo
trace and then applied to the WiFi and 4G networks, whose adaptation framework for DASH clients in LTE networks that
performance is still maintained and is better than the model- enabledclientstoestimatetheavailablebandwidthbasedona
based ABR algorithms such as BBA and MPC. Thirdly, since resourcemonitormodulethatactedasaphysical-layerdaemon.
themeta-modelistypicallytrainedwithmultipledatasetsfrom FESTIVE[8]containedabandwidthestimatormodule,abitrate
different network environments, the historical experiences can selection and update method that tried to avoid unfairness of
belearnedbythemeta-model,whichcanbeusedtosupervise stateless bitrate selection by making the player stateful, and a
thetrainingofageneralagenttoadapttovariousenvironments. randomizedschedulerthatincorporatedthebuffersizetosched-
AsshowninSectionV-C1,theDRLmodelofMeteABRtrained ulethedownloadofthenextsegment.However,throughputcan
withacombineddataset(3G+WiFi+4Gtraces)clearlybeatsthe vary widely over time and result in poor ABR performance.
otherDRLmodelstrainedwithasingledataset. Therefore, BBA [11] adopted a buffer-based approach which
Thecontributionofourworkaresummarizedasfollows. pickedabitratebasedonplaybackbufferoccupation.However,
(cid:2)
Weformulateanovelframeworkformeta-learningbased it suffered from QoE degradation during long-term bandwidth
adaptivebitrateselectiondesign.Wediscussthechallenges fluctuations. BOLA [12] was also a buffer-based algorithm,
of deploying DRL-based ABR mechanism in real-world whichturnedtheABRproblemintoautility-maximizationprob-
video streaming systems, which are not trivial to address lemandsolveditbytheLyapunovfunction.MPC[13]developed
withinconventionalDRLformalism. a control-theoretic framework that allowed the understanding
(cid:2)
WeutilizetheproposedframeworktodesignMetaABR,a and exploration of the trade-offs between bandwidth-based
noveladaptivebitrateselectionalgorithmbasedonmeta- andbuffer-basedadaptationalgorithmsunderdifferentnetwork
learningtomaximizeusers’QoE.Byjointlytrainingmul- bandwidth variations. Oboe [23] auto-tuned the parameters of
tiple learning tasks with a shared meta-critic, it has the model-basedABRalgorithmsfordifferentnetworkconditions
ability to provide transferrable knowledge to supervise toimprovetheABR’sperformance.
bitrate selection, and can be applied to efficiently learn 2) Learning-BasedMethods: Sincemodel-basedalgorithms
a new task in unseen environment with much fewer data failed to achieve optimal performance across a broad set of
samplesandtrainngepoches. network conditions and QoE objectives because of their fixed
(cid:2)
WeimplementtheproposedMetaABRbasedonanemula- controlrules,thelearning-basedmethods[4],[5],[14],[15],[16]
tionplatformwhichconnectstotheLinuxnetworkprotocol wereproposedtolearnpersonalizedABRstrategiesforvarious
stackthroughavirtualnetworkinterfacetosendrealdata conditions.Basedontheobservationthatvideosessionssharing
packets for evaluation. Extensive experiments based on similarkeyfeaturespresentedsimilarinitialthroughputvalues
real-world traces show that MetaABR achieves the best anddynamicpatterns,theCS2P[4]methodusedadata-driven
comprehensive QoE compared with the state-of-the-art approach to learn clusters of similar sessions, and proposed a
ABRalgorithmsinavarietyofnetworkenvironments. Hidden-Markov-Model (HMM) based midstream predictor to
Therestofthepaperisorganizedasfollows.SectionIIintro- modelthestatefulevolutionofthroughputforbitrateadaptation.
duces the related works of media streaming bitrate adaptation D-DASH[14]formulatedtheDASHvideostreamingproblem
methodsandmetalearningalgorithms.SectionIIIpresentsthe withinaDeepQ-learningframework,andusedmixedlearning
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:29:03 UTC from IEEE Xplore. Restrictions apply.

LIetal.:METAABR:AMETA-LEARNINGAPPROACHONADAPTATIVEBITRATESELECTIONFORVIDEOSTREAMING 2425
architectures including feedforward and recurrent deep neural better adapt to changing conditions by training multiple tasks
networkstolearnvideoadaptationstrategiestoachievedagood to build more generalized models. At the architecture level,
trade-off between policy optimality and convergence speed. meta-learningisusuallyconceptualizedasinvolvingtwolearn-
Pensieve[5]proposedaDeepReinforcementLearning(DRL) ingsystems:alower-levelsystemthatlearnsrelativelyquickly
model that selected bitrates for future video chunks based on and is mainly responsible for adapting to new task; A slower
observations collected by DASH clients (i.e., throughput es- upper-levelsystemthatcanworkacrossmultipletaskstoadjust
timation and buffer occupancy) across large video streaming andimprovelower-levelsystemswithanobjectiveofgeneral-
experiments, which provided an expressive and scalable way izationperformance.
to incorporate a rich variety of observations into the control Inside and outside the deep learning community, various
policy. To address the issue of low sample efficiency of DRL, methodshavebeenexploredtoachievethebasicmeta-learning
Comyco [15] trained an ABR policy via imitating expert tra- setting[21].AnimportantmethodwasintroducedbyHochreiter
jectories to avoid redundant exploration. Stick [17] fused the et al. which used standard backpropagation to train recurrent
DRL method and traditional buffer-based method to output neural networks for a series of related tasks [31]. The basic
the buffer-bound, which was used to control the buffer-based process of learning each new task in Hochreiter method is
approach for maximizing the QoE metrics. Fugu [16] argued completelywithinthedynamicrangeoftherecurrentnetwork,
that in real-world setting, it was difficult for sophisticated or which was suitable for the structure of the task family trained
machine-learnedcontrolschemestooutperformasimplebuffer- acrossthenetwork[32].
basedcontrolscheme,notwithstandinggoodperformanceinnet- Reinforcement Learning (RL) learned control policies
workemulatorsorsimulators.Itusedsupervisedlearningwith through interacting with an environment, which enabled an
datafromrealdeploymentenvironmenttotrainaprobabilistic agenttoobtainhighrewardinachievingasequentialactiontask
predictor of upcoming chunk transmission times to improve within an environment. However, RL typically suffered from
a classical control policy. Recently, learning-based methods extreme sample inefficiency due to sparse rewards, the need
wereextendedtotheemerging3Dvideostreamingapplications ofexploration,andhigh-varianceoptimizationalgorithms[33].
and video conferencing systems [24], [25], [26], [27], [28]. Severalmeta-representationshadbeenexploredinRLincluding
Swift [24] adopted a layered encoder that learns to compress learningtheinitialconditions[34],[35],hyperparameters[36],
avideoframeintolayeredcodesandproposedanABRprotocol step directions [37], and step sizes [38], which enabled meta
basedondetectingavailablebandwidthandclient-sidecapacity. learning to train a neural network with fewer environmental
YuZu [25] adopted a neural-enhanced method for intra- and interactions[39],[40].
inter-frameoptimizationsusing3Dsuperresolutiontoincrease In addition to conventional RL that explored environment
thevisualqualityofvolumetricvideostreaming.Vues[26]was based on sampling random actions or hand-crafted heuris-
an edge-assisted transcoding system that transcoded a volu- tics [41], several meta-RL studies treated exploration strategy
metric video frame into multiple 2D views using lightweight or curiosity function as meta-knowledge, and modeled their
machinelearningmodelsandadaptivelyselectedtheviewthat acquisition as a meta-learning problem to improve sample ef-
optimizedtheQoEformobileclients.GSO-Simulcast[27]was ficiency [42]. A large number of meta-RL studies considered
amulti-partyvideo-conferencingsystemwhereamediaserver single-task setting, where loss, reward, and hyperparameters
globally coordinated the publishing and subscribing to decide weretookasmeta-knowledgetotraintogetherwiththebasepol-
theresolutionandbitrateofvideostreamsforeachparticipant. icytoimproveasinglelearningtask[43],[44],[45].Afewrecent
Optimization of video streaming dilivery were also studied in works designed meta-RL generalizations for the conventional
the aspects of routing path assignment [29] and inter-session off-policyRLmethodstoacceleratethetrainingandtestingby
multiplexingcongestioncontrol[30]. replaying buffer samples from meta-training [46], [47]. It had
Differentfromtheexistinglearningbasedmethods,thepro- been demonstrated that meta-RL was successfully applied in
posed MetaABR method introduces a novel meta-learning ap- real-worldphysicalrobot[48],imitationlearning[49],etc.
proachwithneural-enhancedbitrateselectionparticularlyobject
toimprovethegeneralization,robustness,andtrainingefficiency III. META-LEARNINGBASEDBITRATEADAPTATION
of the deep learning based ABR methods. To the best of our MECHANISM
knowledge,MetaABRisthefirsttoincorporatemeta-criticinto
Inthissection,weproposeameta-learningbasedbitrateadap-
thedesignofABRmechanismforvideostreaming.
tationmechanismcalledMetaABR.Wefirstprovidequantified
descriptionofQoEmetrics,thenformulatetheABRproblemas
B. Meta-Learning adeepreinforcementlearningtask,whichcanbesolvedwitha
meta-reinforcementlearningframework.Thekeynotationsused
Meta-learning,alsoknownaslearningtolearn,isamachine
throughoutthepaperaresummarizedinTableI.Thedetailsare
learning method that intends to learn the general knowledge
introducedasfollows.
acrosssimilarlearningtaskstoimproveitsperformanceinnew
tasksbasedonafewexamples[20],[21].Meta-learninghelps
A. QoEMetrics
toachievehighermodelaccuracy,becauseofitsoptimizationof
learning algorithms such as optimization of hyper parameters Toimproveusers’experience,mediastreamingserviceshould
to achieve the best results. It also helps to learn algorithms consider a variety of QoE goals such as maximizing video
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:29:03 UTC from IEEE Xplore. Restrictions apply.

| 2426 |     |     |        |     |     |     |     | IEEETRANSACTIONSONMOBILECOMPUTING,VOL.23,NO.3,MARCH2024 |     |     |     |     |     |     |
| ---- | --- | --- | ------ | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|      |     |     | TABLEI |     |     |     |     | B. ABRasaDeepReinforcementLearningTask                  |     |     |     |     |     |     |
NOTATIONS
Adaptivebitrateselectionforvideostreamingcanbecasted
asadeepreinforcementlearning(DRL)task:anagentlearnsby
observingthestatesofthedynamicenvironment,andproduces
actionsbasedonaneuralnetworktoselecttheproperbitrateto
maximizetheexpectedlong-termQoE.Wediscussthefollowing
basicelementsofaDRLtask.
|     |     |     |     |     |     |     |     | Agent: | An agent | is an | entity | in the system | responsible | for |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ----- | ------ | ------------- | ----------- | --- |
performinglearningalgorithmandmakingsequentialdecisions.
IntheABRproblem,ateachtimestep,theagentistriggeredto
chooseabitrateforachunktobedownloaded.
State:Astateofthesystemconsistsofanumberofnetwork
|     |     |     |     |     |     |     |     | performance | measurements |     | that | are observed | by the | agent. At |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | ---- | ------------ | ------ | --------- |
timestept,thestateusedasinputtotheDRLagentisdenoted
by
quality, minimizing rebuffering time, and maintaining video s =(x(cid:2) ,τ(cid:2) ,n(cid:2) ,b ,c ,l t), (5)
|     |     |     |     |     |     |     |     |     |     | t   | t t | t t t |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
qualitysmoothness(i.e.,avoidingconstantbitratefluctuations).
For a satisfactory user-perceived QoE, ABR algorithm needs wherex(cid:2) isthenetworkthroughputmeasurementsforthepast
t
|     |     |     |     |     |     |     |     | k   |     | τ(cid:2) |     |     |     | k   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
to optimize several conflicting goals. For example, increasing video chunks; t is the download time of the past video
the bitrate may lead to longer rebuffering time. There exists chunks, which represents the time interval of the throughput
|                                                           |     |     |     |     |     |     |     | measurements; |     | n(cid:2) is a vector | of  | m available | sizes | for the next |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------------------- | --- | ----------- | ----- | ------------ |
| significantvarianceinuserpreferencesforvideostreamingQoE. |     |     |     |     |     |     |     |               |     | t                    |     |             |       |              |
|                                                           |     |     |     |     |     |     |     |               | b   |                      |     |             | c     |              |
Toformulatetheproblem,weadopt thequantification ofQoE video chunk; t isthe current buffer level; t isthe number of
metricsasintroducedin[13]. chunksremaininginthevideo;andl tisthebitrateatwhichthe
Specifically, users tend to prefer great average quality per lastchunkwasdownloaded.
chunk for high-definition content, which can be calculated on Action: Upon observing a state s t, the agent needs to take
themeanofn-thchunkofvideovby: an action a to determine the downloading bitrate for the next
t
|     |     |     |     |     |     |     |     | video chunk. | A   | video website |     | typically | encodes | a video with |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------- | --- | --------- | ------- | ------------ |
(cid:2)N
differentbitratelevelssuchas240p,480p,and1080p,andthe
|     | QoE | v   | =   | q(R n,v), |     |     | (1) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
h d
agentselectsbitratebasedonapolicylearnedbythemodel.In
n=1
DRL,theagentusesadeepneuralnetwork(DNN)torepresent
| R   |     |     |     | n   |     | v, q(·) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
where n,v is the bitrate of chunk of video and is a the policy with a number of model parameters θ. Using θ, we
non-decreasingfunctionwhichmapstheselectedbitratetothe candenotethepolicybyπ θ(s ,a
|     |     |     |     |     |     |     |     |     |     |     | t   | t). |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
videoqualityperceivedbyuser. Reward: At each time step t, the agent observes some state
Meanwhile,weneedtoensureafluentplaybackandminimize s t,andchoosesanactiona
t.Afterapplyingtheaction,thestate
therebufferingtimeofeverychunk,whichiscomputedby:
|     |     |     |     |     |     |     |     | oftheenvironmenttransitionstos |                                       |     |     | t+1 andtheagentreceivesa |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | ------------------------------------- | --- | --- | ------------------------ | --- | --- |
|     |     |     |     |     |     |     |     | rewardr                        | trepresentingacomprehensiveQoEmetric. |     |     |                          |     |     |
(cid:2)N
QoE v = T , (2) Withtheaboveformulation,thereinforcementlearningtask
|     |     | r   | eb  | n,v |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
forbitrateadaptationcanbedescribedasfollows.
n=1
| eT  |     |     |     |     |     |     |     | ReinforcementLearningTaskforBitrateAdaptation:Givena |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
w h e r n ,v is t h e re b u f fe ringtimethatresultsfromdownloading setofobservednetworkstates{s 1,s 2,···},learnadeepneural
| ch u n k n a tb it | r a te R | .   |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n , v network model that maps each state to an action (representing
Besides,thestreamingstrategyshouldreducesuddenandfre-
|     |     |     |     |     |     |     |     | thebitrateselectionpolicy):f(s |     |     |     | t)→a |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | ---- | --- | --- |
t,inordertomaximize
quentqualityvariations,whichmayimposenegativeexperience
thelong-termexpectedcumulativediscountedreward,i.e.,
forusers.Variationofvideoqualityiscalculatedby:
|     |     |     |     |     |     |     |     |     |     |     | (cid:3) | (cid:4) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | --- | --- |
(cid:2)∞
|     |      | N(cid:2)−1 |                 |     |     |       |     |     |     |     | E   | γtr , |     |     |
| --- | ---- | ---------- | --------------- | --- | --- | ----- | --- | --- | --- | --- | --- | ----- | --- | --- |
| QoE | v    |            | |q(R n+1,v)−q(R |     |     | ,v)|, |     |     |     |     |     | t     |     | (6) |
|     |      | =          |                 |     | n   |       | (3) |     |     |     |     |       |     |     |
|     | v ar |            |                 |     |     |       |     |     |     |     | t=0 |       |     |     |
n=1
|     |     |     |     |     |     |     |     | whereγ | ∈(0,1]isafactordiscountingfuturerewards. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------------------------------------- | --- | --- | --- | --- | --- |
whichpenalizeschangesinvideoqualitytofavorsmoothness.
Overallobjective:Theoverallobjectiveinacomprehensive
QoEmetricisaweightedsumofthethreemetricsonvideov, C. SolutionWithaMeta-LearningFramework
whichisdefinedas As discussed in Section I, conventional deep reinforcement
|      |        |     |        |      |        |      |     | learning       | for ABR | selection   | has | the drawbacks | of  | efficiency, |
| ---- | ------ | --- | ------ | ---- | ------ | ---- | --- | -------------- | ------- | ----------- | --- | ------------- | --- | ----------- |
| QoEv | =μ QoE | v   | −μ QoE | v    | −μ QoE | v ,  | (4) |                |         |             |     |               |     |             |
|      | 1      | h d | 2      | r eb | 3      | v ar |     |                |         |             |     |               |     |             |
|      |        |     |        |      |        |      |     | generalization | and     | robustness. |     | To overcome   | the | performance |
where M =(μ ,μ ,μ 3) is a set of non-negative weighting issues,weproposeanovelmetareinforcementlearning(MRL)
|     | 1 2 |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
parameters corresponding to users’ preference on the video based method called MetaABR for bitrate adaptation in video
quality,rebufferingtime,andvariation,respectively. streaming. In the proposed framework, we apply the A3C
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:29:03 UTC from IEEE Xplore.  Restrictions apply.

LIetal.:METAABR:AMETA-LEARNINGAPPROACHONADAPTATIVEBITRATESELECTIONFORVIDEOSTREAMING 2427
|     |     |     |     |     |     |     | task the    | actor | should be       | trained | to solve.          | To  | achieve | this, the |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --------------- | ------- | ------------------ | --- | ------- | --------- |
|     |     |     |     |     |     |     | meta-critic | is    | further divided |         | into a task-config |     | network | and a     |
criticnetworkasshowninFig.4.Thetask-confignetworktakes
|     |     |     |     |     |     |     | the past | trails | of a RL | task represented |     | by  | a trajectory | of the |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------- | ---------------- | --- | --- | ------------ | ------ |
state,action,andrewardasinputtolearnhistoricalexperience,
|     |     |     |     |     |     |     | and it outputs |     | a task-actor | embedding |     | z which | represents | the |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --------- | --- | ------- | ---------- | --- |
task-specificfeatures.Thecriticnetworkusesthecurrent(state,
z
|     |     |     |     |     |     |     | action) | and the | task-actor | embedding |     | from | the task-config |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ---------- | --------- | --- | ---- | --------------- | --- |
networkasinputtoapproximatetherewardforaRLtask,where
z
|     |     |     |     |     |     |     | serves | as the | meta-knowledge |     | to decide | how | to criticise | the |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | -------------- | --- | --------- | --- | ------------ | --- |
currentactoronthespecifictask.Thetrainingdetailsaregiven
inSectionIV.
Fig.4. FrameworkofMetaABR. By jointly training the meta-critic with multiple actors, the
meta-criticgainstheabilitytocorrectlycriticiseanewtaskbased
ontheprovidedtask-confignetwork.Whenapplyingthemeta-
algorithm[50]fordeepreinforcementlearning.A3Cisastate- critictolearnanewtask,fromtheperspectiveofthenewtask’s
of-the-art DRL method that jointly trains a pair of actor-critic actor,itbenefitsfromapre-trainedmeta-criticwhichincreases
deepneuralnetworksforanyRLtasksothattheactorlearnsto learningspeedanddecreasesrequiredsamples.
solvetheproblem,andthecriticlearnstoeffectivelysupervise Themeta-criticbasedapproachhasanumberoffurtherbene-
the actor by approximating its reward. Following the learning fits.(1)ItcanaddressDRLtasks(i.e.,trainingagentsfordiffer-
tolearnmethod[50],[51],weadapttheA3Cmethodformeta- entnetworkenvironments)withinasingleframework,wherethe
learning by training a global meta-critic neural network based actorscanbenefitfromthemeta-critic’ssupervisionofwhatit
on cross-task knowledge to supervise multiple actor networks shoulddointhoseunlabelledstates(unseensituations).(2)The
to solve specific problems. In this way, the shared meta-critic proposed task-config and meta-criticnetworks can capture the
canprovidetransferableknowledgeintrainingactorstogener- correlationamongdiverselearningtasksfromthepast,andsuch
ate ABR policies for different network environments, and the history-dependentknowledgecanbetransferredtothelearning
experience of meta-critic can be learned by the actors on new ofanewtask,makingtheagentmorecapableofchoosingthe
problems with only a few trials to achieve adaptivity and fast suitablepolicytooptimizerewardswhenbeingexposedtoanew
| convergence. | Noted   | that  | there | are many | meta-learning | meth- | environment. |     |     |     |     |     |     |     |
| ------------ | ------- | ----- | ----- | -------- | ------------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| ods such     | as MAML | [34], | MAESN | [52],    | GrBAL/ReBAL   | [48], |              |     |     |     |     |     |     |     |
PEARL [53], etc., which we believe are also applicable to the IV. TRAININGMETHODS
| proposed | meta-learning |     | framework | for | adaptive | bitrate selec- |     |     |     |     |     |     |     |     |
| -------- | ------------- | --- | --------- | --- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Inthissection,weintroducethemethodsoftrainingthemeta-
| tion. However, | searching |     | for the | most | efficient | meta-learning |     |     |     |     |     |     |     |     |
| -------------- | --------- | --- | ------- | ---- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
criticandthetask-specificactorsindetail.
methodforMetaABRisbeyondthediscussionofthisarticle.
| The overall | framework |     | of MetaABR |     | is illustrated | in Fig. | 4.  |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ---------- | --- | -------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
A. TrainingtheMeta-Critic
| It consists | of a        | set of actor | networks |           | that learn | to solve spe- |             |          |            |           |         |          |           |       |
| ----------- | ----------- | ------------ | -------- | --------- | ---------- | ------------- | ----------- | -------- | ---------- | --------- | ------- | -------- | --------- | ----- |
| cific tasks | (e.g.,      | learning     | an ABR   | algorithm | for        | a particular  |             |          |            |           |         |          |           |       |
|             |             |              |          |           |            |               | In the      | proposed | framework, |           | we want | to train | a single  | meta- |
| network     | environment | such         | as       | WiFi and  | 3G),       | and a global  |             |          |            |           |         |          |           |       |
|             |             |              |          |           |            |               | critic that | can      | criticise  | any actor | to      | perform  | any task. | This  |
meta-criticnetworkthatlearnshowtoeffectivelysupervisethe
requirestwogeneralisations(taskandactorconditioning)com-
actors.Actor-criticisawell-knowndeepreinforcementlearning
|     |     |     |     |     |     |     | pared to | conventional |     | critic networks |     | that | criticise a | specific |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | --------------- | --- | ---- | ----------- | -------- |
methodwhereanactorisaneuralnetworkusedtoselectactions actorforaspecifictask.Thestructureofthemeta-criticisillus-
| and a critic | is another |     | neural | network | used to | learn a value |     |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | ------ | ------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tratedinFig.5,whichconsistsoftwosubnetworks:atask-config
functionandupdatetheactor’spolicyparametersinadirection
networkandacriticnetwork.
of performance improvement [50]. Unlike conventional actor- Thetask-confignetworkC ω,parameterisedbyω,hasathree-
critic networks [54], [55] that train a pair of actor-critic for layerneuralnetworkstructure.Ittakesthepastktrailsof(state,
eachlearningtaskindividually,theproposedframeworktrains action,reward)tripletsasinputtolearntask-specificexperience.
asharedmeta-critictoprovidetransferrableknowledgeamong
|     |     |     |     |     |     |     | The input | layer | is a concatenation |     | of  | a fully-connected |     | (FC) |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ------------------ | --- | --- | ----------------- | --- | ---- |
actors,whichallowstheactorstobetrainedwithonlyafewtrials
|     |     |     |     |     |     |     | layer (to | deal | with numerical |     | values) | and | a one-dimensional |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | -------------- | --- | ------- | --- | ----------------- | --- |
inadaptingtoanewtask.Forexample,byconsideringasetof convolutionalneuralnetwork(1D-CNN)layer(todealwithvec-
taskseachlearnsanABRpolicyinaparticularenvironmentsuch
tors).Itfollowsbyafully-connected(FC)layerandarecurrent
asEthernetorWiFinetworks,wecantrainatask-independent neuralnetwork(RNN)layertoproduceatask-actorembedding
meta-critic from them, and apply the meta-critic to efficiently z,whichencodesthetask-dependentfeaturesformeta-learning.
learnanactorforanewtargettasksuchasanewABRpolicy
Specifically,wemodelthetask-actorencoderasaLong-Short
for3Gnetworks. TermMemory(LSTM)[56]whoseinputisatrajectoryofpast
To apply the idea of meta-learning on solving the problem, ktrialseachrepresentedbyatriplet
| we need | to explicitly | condition |     | the meta-critic |     | on a task, so |     |     |     |     |     |          |     |     |
| ------- | ------------- | --------- | --- | --------------- | --- | ------------- | --- | --- | --- | --- | --- | -------- | --- | --- |
|         |               |           |     |                 |     |               |     |     | Lt  | =(s | ,a  | ,r t−k). |     |     |
thatatanymomentitknowswhatactoritistrainingandwhat t−k t−k (7)
t−k
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:29:03 UTC from IEEE Xplore.  Restrictions apply.

2428 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.23,NO.3,MARCH2024
B. TrainingtheTask-SpecificActors
The actor networks A , parameterised by θ(i), are a set
θ(i)
of task-specific neural networks that are used by the agents to
generateactionsforABRdecision.Theneuralnetworkstructure
oftheactornetworksissimilartothatoftheconfignetwork.The
hidden layer formed by the convolutional layer and the fully
connected layer in the actor networks have 128 neurons that
applythesoftmaxfunctionintheoutputlayer.
The actor network takes the state
s(i)
as input, then outputs
t
an action a(i) , i.e., a(i) =A (s(i) ). After applying each ac-
t t θ(i) t
tion, the agent observes a reward for that chunk. The goal of
each learning agent is to maximize the expected cumulative
(discounted)rewardthatitreceivesfromthenetworkenviron-
ment in terms of a specific QoE metric. In other words, the
actornetworkintendstomaximizethediscountedfuturereward
Q φ(s(
t
i),a(
t
i),z
t
(i) ) that is the estimated value from the output
ofthemeta-criticnetwork.Therefore,theoptimizeralternately
Fig.5. StructureofMeta-Critic. updatestheactornetworkwith:
(cid:7) (cid:8)
θ(i) ←argmaxQ φ s( t i),A θ(i) (s( t i) ),z t (i) . (10)
Theoutputofthetask-confignetworkisatask-actorembed- θ(i)
dingz tthatrepresentsthetask-dependentfeatures,where
Intheaboveequation,multipleactorsaretrainedjointlytofind
(cid:5) (cid:6)
z t =C ω Lt t−k ,Lt t−k+1 ,...,Lt t−1 . (8) theiroptimalmodelparametersθ(i) tomaximizetheestimated
rewardbasedontheoutputofthemeta-critic.
The rational of using the proposed task-actor embedding as
meta-knowledgetotrainametamodelareexplainedasfollows. V. EXPERIMENTS
Ontheonehand,itencodesasequenceofstate-actionpairs(the
Inthissection,weconductextensiveexperimentstoevaluate
choiceofactiondependsontheactor’sparameters),whichcanbe
theperformance ofMetaABR.Ourexperiments cover abroad
usedbythecritictocharacterizetheactor’spolicyitistocriticise.
setofnetworkconditionsandQoEmetrics.Wemainlyfocuson
On the other hand, it encodes the observed rewards of each
answeringthefollowingquestions.
action, which enables the critic to capture the characterization
(1)HowdoesMetaABRcomparetothestate-of-the-artABR
ofthetaskthattheactorissolving.
algorithms in terms of video QoE? We find that, in all of the
The critic network Q φ, parameterised by φ, has similar
consideredscenarios,MetaABRisabletorivaloroutperformthe
structure as that of the task-config network, which is used to
bestexistingscheme,withaverageQoEimprovementsranging
approximatetherewardforreinforcementlearningtasks.Apart
from3%-15%.
from the state s t and action a t, it further takes the task-actor
(2)DoestheMetaABRmethodperformmoreefficientlythan
embeddingzasinputtolearnanaction-valuefunction.Weuse
Q φ(s(
t
i),a(
t
i),z
t
(i) )todescribetheexpectedreturnrewardafter o
w
t
e
he
fi
r
n
re
d
in
t
f
h
o
a
r
t
ce
M
m
e
e
ta
n
A
tl
B
ea
R
rn
c
in
a
g
n
m
ac
e
h
th
ie
o
v
d
e
s?
c
T
om
hr
p
o
a
u
r
g
a
h
bl
t
e
he
p
e
e
x
r
p
fo
e
r
r
m
im
a
e
n
n
c
t
e
,
actoritakingactiona(
t
i) instates(
t
i)
withatask-actorembedding with other reinforcement learning methods with much fewer
z t (i) . samplesandtrainingepochs,anditperformsthebestevenbeing
The meta-critic is shared across all tasks and actors, which transferredtoadifferentnetworkenvironment.
istrainedtohelpactorstofindstrategiesthataremoresuitable (3) How is the trade-off between different conflicting QoE
fortheenvironment.AssumingthereareM learningtasks,the metrics? We find that MetaABR achieves a better trade-off
updaterulesforthemeta-criticmodelparametersareasfollows. between increasing bitrate and reducing rebuffering time and
variation,whichismoreclosertotheidealsituationcompared
(cid:2)M
φ,ω ←argmin (P φ,ω(s(
t
i),a(
t
i),z
t
(i) )) 2, tothebaselines.
φ,ω
i=1
A. ExperimentSetup
P φ,ω(s(
t
i),a(
t
i),z
t
(i) )=Q φ(s(
t
i),a(
t
i),C
ω
(i
,
)
t
)−r
t
1) Implementation: InourimplementationoftheMetaABR
−γQ φ(s(
t+
i)
1
,a(
t+
i)
1
,C
ω
(i
,
)
t+1
). (9) scheme, the task-config network C ω, the critic network Q φ,
andtheactornetworkA θarethree-layerfully-connectedneural
In the above equation, P φ,ω() is the error between the esti- networks that use rectified linear unit (ReLU) as the activa-
mated reward (the output of the critic network) and the actual tion function of each neuron. We train the neural networks
reward,andthelearningobjectiveistofindtheoptimalmodel onTensorFlow1.13.1usingRMSPropOptimizerwithlearning
parametersφandωthatminimizetheoverallsquarederror. rate 0.01 (C ω), 0.0001 (Q φ), and 0.001 (A θ) accordingly. The
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:29:03 UTC from IEEE Xplore. Restrictions apply.

LIetal.:METAABR:AMETA-LEARNINGAPPROACHONADAPTATIVEBITRATESELECTIONFORVIDEOSTREAMING 2429
TABLEII oursettings,theclientvideoplayerisGoogleChrome(version
THELAYERPARAMETERSOFMETAABR
85)andchromedriver(version85.0.4183.38).Thevideoserver
is Apache (version 2.4.7). We use Mahimahi [57] to emulate
network environments from the network traces between the
clientandtheserverwith80msRTT.
5) DatasetsandNetworkTraces: ToevaluatetheABRalgo-
rithms on realistic network conditions, we created a corpus of
networktracesusingseveralreal-worldnetworkcommunication
datasets.
(cid:2)
3G[59]:Thisdatasetwascollectedfrompopularcommute
routesinandaroundOslo(Norway).Itincludesthroughput
rewarddiscountfactorγ =0.99bydefault.Theneuralnetwork
measurementsofreal-worldadaptiveHTTPstreamingper-
structureofMetaABRisillustratedinTableII. formed over 3G networks using mobile devices traveling
2) EvaluationPlatform: Theexperimentsareconductedon withdifferenttypesofpublictransportation(metro,tram,
a PC server (CPU: Intel(R) Xeon(R) CPU E5-2630 v4 @ train, bus and ferry). The throughput of the network is
2.20 GHz; Memory: 32 GB DDR4 2400Mhz*4; OS: 64-bit between0.1∼1Mbps.
(cid:2)
Ubuntu 16.04). We implement the proposed MetaABR frame- WiFi[5]:Thisdatasetisfromthework[5],whichistai-
workbasedontheMahimahi[57]emulationplatform,whichis loredfromabroadbanddatasetprovidedbytheFCC[60].
connectedtotheLinuxnetworkprotocolstackthroughavirtual Sincetheoriginaldatasetcontainslargeamountbroadband
networkinterfaceandsendsrealdatapackets.Mahimahicanbe datalogoveroneyear,theauthorsin[5]selectedthe“Web
usedtorecordtrafficfromHTTP-basedapplicationsandreplay browsing” category in the Aug 2016 collection and only
it under emulated network conditions, which is ideal for fair keepstraceswhoseaveragethroughputislessthan6Mbps
comparisonofdifferentABRalgorithmsforvideostreaming. toavoidtrivialABRsolutions.
(cid:2)
3) Baseline Algorithms: We compare MetaABR with three 4G Syd [61]: This dataset was collected from SpeedTest
state-of-the-artABRalgorithms: measurementsconductedinSydneyon4Gnetworksunder
(cid:2)
BBA [11]: a buffer-based approach which selects bitrates vehicular driving conditions. In the dataset, throughput
basedonplaybackbufferoccupation. measurements samples were collected within 72 trips in
(cid:2)
RobustMPC[13]:amodelpredictivecontrolalgorithmthat differentdayandnighttimestoconsiderOnandOffpeak
combinesboththroughputestimatesandbufferoccupancy hoursoftraffic.Thethroughputofthe4Gnetworkranges
informationtoselectbitrates. from5∼10Mbps.
(cid:2) (cid:2)
Pensieve[5]:astate-of-the-artABRschemebasedondeep Hybrid (3G+WiFi+4G Syd): We combine the data
(cid:2)
reinforcementlearning. sampes of the above 3G, WiFi, and 4GSyd datasets to
BayesMPC [58]: an uncertainty-aware robust ABR algo- generateahybriddataset.Itsimulatesthereal-lifescenarios
rithmbasedonBayesianneuralnetwork(BNN)andmodel wherethreenetworksaredynamicallyswitchingduetothe
predictivecontrol(MPC). mobilityofsmartphones.Theperformanceinthisdataset
(cid:2)
Comyco[15]:avideoquality-awareABRapproachlever- can well reflect the generalization ability of the ABR
agingimitationlearningtoacceleratethetrainingprocess method.
(cid:2)
forABRtasks. 4G NY [62]:ThisdatasetwascollectedonNewYorkCity
Notethatwedonotcomparewithotherdeeplearningbased MTAbusandsubway.Thedatawasrecordedwithamobile
ABRalgorithmssuchasFugu[16],Oboe[23],andStick[17], phone running iPerf to log TCP throughput every 1000
sinceeithertheyareimplementedontheserverside,orthereare milliseconds.Thethroughputofthenetworkenvironment
lackofopen-sourcecodetoreproducetheirwork. isbetween1∼108Mbps.
(cid:2)
4) Video Parameters: We have modified dash.js3 to sup- 5G [63]: This dataset was collected from a major Irish
port MetaABR and the above baseline ABR algorithms. For mobileoperator.Itwasgeneratedfromtwomobilitypat-
MetaABR,Pensieve,andRobustMPC,weconfiguredash.jsto terns(staticandcar)acrosstwoapplicationpatterns(video
obtainthebitrateselectiondecisionfromanABRprocessthat streamingandfiledownload).Itconsistsoftwoparts:the
implementsthecorrespondingalgorithm.TheDASHplayeris firstisaproductiondatasetcollectedfromreal-worldand
configuredtohaveaplaybackbuffercapacityof60seconds.Our the second is synthetic data generated from a large-scale
evaluation used the “Envivio-Dash3” video of the DASH-246 multi-cell5G/mmwavens-3platform.Weselectedthedata
JavaScript reference client. In addition, the video is divided generated fromthe Amazon Primeand Netflix streaming
into 48 blocks with a total length of 193 seconds. This video servicesintheexperiments,andthethroughputofthe5G
isencodedbytheH.264/MPEG-4codecatbitratesin300,750, networkisintherangeof3∼202.5Mbps.
1200,1850,2850,4300kbps(whichcorrespondstovideomodes The basic information of the datasets are listed in Table III.
in 240p, 360p, 480p, 720p, 1080p, 1440p). Therefore, each ThestatisticalcharacteristicsofthedatasetsareshowninFig.6.
blockrepresentsapproximately4secondsofvideoplayback.In According to the figure, both 3G and WiFi traces have small
throughput and low variations. It is observed that over 95%
3https://github.com/Dash-Industry-Forum/dash.js/,Akamai,2020. throughput of 4GSyd are concentrated on 8-9 Mbps, and the
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:29:03 UTC from IEEE Xplore. Restrictions apply.

2430 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.23,NO.3,MARCH2024
TABLEIII TABLEIV
DATASETSSTATISTICS THEQOEMETRICSCONSIDEREDINTHEEVALUATION
a sliding window across the 4GNY and 5G network traces to
formthetestsets.
6) QoEMetrics: Similartotheliterature,weconsiderthree
QoE metrics with different choices of the combination of
q(R (cid:2)n,v)andM.
QoE std:q(R n,v)=R n,M =(1,4.3,1).Thisisthestan-
dardQoEmetricthathadbeenwidelyusedinthestate-of-
the-artABRsystemssuchasMPC[64]andPensieve[5].
(cid:2)
QoE fluent: q(R n,v)=R n, M =(1,8,1). This metric
emphasizesthefluencyofthevideo.Itusesamuchhigher
penaltyonrebufferingtimetocalculatethereward,which
intendstoprovidemorefluentvideostreamingserviceto
theuser.
(cid:2)
QoE hd:M =(1,8,1).Thismetricfavorshighdefinition
Fig.6. Characteristicsofdatasets. (HD)video.Itadoptsaq(R n,v)mappingthatassignsqual-
ityscoresaccordingtothebitratesasillustratedinTableIV,
whereHDbitrateshavesignificantlyhigherqualityscore
standarddeviationislessthan0.5.Thereasonisthat4GSydwas
thanthatofnon-HDbitrates.
collectedwiththeTestSpeedAPPwhichformsstablethroughput The exact values of q(R n,v) for the QoE are provided in
testingfromdifferentlocations.The4GNY and5Gdatasetsare
Table IV. In our experiments, we report the average QoE per
morediverse,whosethroughputspreadfromawiderangewith
chunk,i.e.,thetotalQoEmetricdividedbythenumberofchunks
largerdeviations.
inthevideo.
Foreachoftheabovedataset,wefollowthemethodproposed
inPensieve[5]togeneratetracesforreinforcementlearningand
B. ComparisonWithBaselineAlgorithms
totesttheABRalgorithms.Forthe3Gand4GSyddatasets,we
generated 1000 throughput traces each with a duration of 320 In this section, we compare the performance of MetaABR
secondsbyusingaslidingwindowacrossthenetworktraces.For withthebaselinealgorithmswithdifferentnetworktraces.
theWiFidataset,wegenerated1000traces(eachwith320sec- The Cumulative Distribution Functions (CDFs) of the algo-
onds)byconcatenatingrandomlyselectedtracesfromthe“Web rithmsondifferentQoEmetricsareillustratedinFigs.7,8,9,
browsing”categoryintheAug2016collection.FortheHybrid and10,andtheaverageresultsareshowninTableV.Wemake
scenario,wesimplycombinedthethroughputtracesgenerated thefollowingdiscussionsontheresults.
from the 3G, WiFi, and 4GSyd datasets together to form the Firstly,MetaABReithermatchesorexceedstheperformance
dataset. We reformatted the generated throughput traces to fit ofthestate-of-the-artABRalgorithmsoneachQoEmetricand
the Mahimahi [57] emulation platform, so that the same trace network considered. According to Table V, MetaABR trained
canbereplayedtotestdifferentABRalgorithms.Werandomly from individual network trace (e.g., 3G, WiFi, and 4GSyd)
partitionthegeneratedtracesintotrainandtestdatasets,where performs very close to Pensieve. MetaABR trained from hy-
80%ofdataareusedfortrainingmachinelearningmodelsand bridtracesignificantlyoutperformstheotheralgorithms,which
20% are used for testing all compared algorithms by default. achieves the best QoE on almost all network conditions. This
Amongthetrainset,20%ofdataareusedtoformavalidation showsthepowerofmeta-learning:itcanlearnexperiencesfrom
setforhyperperametertuning. different network conditions to improve performance and be
Since the traces of the 4GNY and 5G datasets are much adaptable to different scenarios. For QoE std, a widely con-
smaller than that of the other datasets, we only used them sidered metric in the literature [5], [64], the average QoE for
for testing the adaptivity and knowledge transfer of the DRL MetaABRis5%higherthanthatofPensieveon3Gnetworks,
algorithms. That is, we trained the DRL models using other and 3%∼15% higher in other networks. The gaps between
datasets, and then tested the pre-trained models on the 4GNY MetaABRandothermethodsarealsofoundinQoE fluent and
and5Gdatasetstoshowtheirperformanceonunseennetwork QoE hd. It is noticed that the CDFs in 4GSyd show stair-like
environments. Following similar principle, we generated 200 shapes in Fig. 9, and the reason is explained as follows. Since
throughputtraceseachwithadurationof320secondsbyusing the 4GSyd trace has very stable throughput, where over 95%
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:29:03 UTC from IEEE Xplore. Restrictions apply.

LIetal.:METAABR:AMETA-LEARNINGAPPROACHONADAPTATIVEBITRATESELECTIONFORVIDEOSTREAMING 2431
Fig.7. CDFofQoEmetrics(3Gnetwork).
Fig.8. CDFofQoEmetrics(WiFinetwork).
Fig.9. CDFofQoEmetrics(4Gsydnetwork).
throughput are concentrated on 8-9 Mbps with standard de- environments,whereasthemodel-basedABRalgorithmssuch
viation less than 0.5 as shown in Fig. 6, it is easy to form as BBA and Robust MPC struggle to optimize for different
a trivial solution for bitrate selection. That is, it can use full environments and QoE objectives. Since the model-based al-
(near-constant)bandwidthtosatisfytheQoEinahighlevelfor gorithms employ fixed control laws, they are not flexible for
the vast majority of ABR cases. Therefore, machine learning optimizing for multiple QoE objectives with different ABR
methods did not show significant performance improvement policies.Forexample,whennetworkbandwidthisinadequate,
compared to model-based methods in the 4GSyd datasets, and theABRalgorithmshouldbuildtheplaybackbufferasquickly
mostalgorithmsachievehighQoEswithmorethan95%ofcases aspossibleusingthelowestbitrate.Asillustratedbytheresultsin
concentratingonahighlevel. hybridnetwork,MetaABRisabletolearnsuchapolicywithout
Secondly, MetaABR is able to automatically learn suitable expert involvement, while other algorithms have difficulty to
ABR policies with a shared meta-critic on Hybrid network optimizesuchlongtermstrategies.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:29:03 UTC from IEEE Xplore. Restrictions apply.

| 2432 |     |     |     |     | IEEETRANSACTIONSONMOBILECOMPUTING,VOL.23,NO.3,MARCH2024 |     |     |     |     |
| ---- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- |
Fig.10. CDFofQoEmetrics(Hybridnetwork).
TABLEV
COMPARISONOFAVERAGEBITRATE(MBPS),REBUFFERINGTIME(SECOND),VARIATIONS,ANDTHEIRCORRESPONDINGQOEMETRICSONDIFFERENTNETWORK
ENVIRONMENTS,WHEREMETAABR(HYBRID)MEANSAMETAABRMODELTRAINEDWITHTHEHybridDATASET,ANDSOARETHEREST
C. EffectivenessofMeta-CriticLearning
|     |     |     |     |     | 2) AbilityofKnowledgeTransfer: |     | Wethentesttheabilityof |     |     |
| --- | --- | --- | --- | --- | ------------------------------ | --- | ---------------------- | --- | --- |
knowledgetransfer.SimilartotheexperimentsinSectionV-B,
| 1) Adaptivity: | ThemajoradvantageofMetaABRisitsadap- |     |     |     |     |     |     |     |     |
| -------------- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
weusetheHybriddatasettopre-trainaDRLmodel,andapply
| tivity on | different network | traces, | which enables | a machine |     |     |     |     |     |
| --------- | ----------------- | ------- | ------------- | --------- | --- | --- | --- | --- | --- |
learning ABR algorithm to learn once and be applied to any- the model to unseen networks (i.e., 4GNY and 5G) to test its
|     |     |     |     |     | performance. | The results | are shown in Table | VI, Figs. | 11 and |
| --- | --- | --- | --- | --- | ------------ | ----------- | ------------------ | --------- | ------ |
where.Withtheproposedmeta-learningmethodwecantraina
generalmodelMetaABR(Hybrid)basedontheHybriddataset 12.ClearlyMetaABR(Hybrid)achievesthebestQoEsinmost
|                |           |                |         |               | cases, and | it beats the personally | trained         | method    | Comyco on |
| -------------- | --------- | -------------- | ------- | ------------- | ---------- | ----------------------- | --------------- | --------- | --------- |
| and then apply | it to the | other networks | without | modification. |            |                         |                 |           |           |
|                |           |                |         |               | most QoE   | metrics, thanks         | to its power of | knowledge | transfer  |
AsillustratedinTableV,MetaABR(Hybrid)performscloseor
betterthanthosemodelspersonallytrainedonspecificnetworks. from other learning tasks. Pensieve(Hybrid) performs close to
|     |     |     |     |     | or worse | than the model-based | methods | such as | BBA and |
| --- | --- | --- | --- | --- | -------- | -------------------- | ------- | ------- | ------- |
Forexample,MetaABR(Hybrid)outperformsMetaABR(WiFi)
on the WiFi network, and outperforms MetaABR(4GSyd) on RobustMPC, which shows poor ability of knowledge transfer
the 4G network, which generally achieves the best perfor- withoutmeta-learning.
|          |                    |     |                 |              | To test | whether the training | knowledge | from single | dataset |
| -------- | ------------------ | --- | --------------- | ------------ | ------- | -------------------- | --------- | ----------- | ------- |
| mance on | all test datasets. | On  | the other hand, | conventional |         |                      |           |             |         |
DRL method such as Pensieve has poor adaptivity, e.g., Pen- is transferable to multiple datasets, we train both MetaABR
andPensieveonthe3Gdataset,andthenapplythepre-trained
sieve(Hybrid)clearlyperformsmuchworsethanPensieve(3G)
modeltotherestnetworks.TheresultsareshowninTableVII.
andPensieve(WiFi)onthecorrespondingdatasets.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:29:03 UTC from IEEE Xplore.  Restrictions apply.

LIetal.:METAABR:AMETA-LEARNINGAPPROACHONADAPTATIVEBITRATESELECTIONFORVIDEOSTREAMING 2433
TABLEVI
COMPARISONOFQOEMETRICSFORTRANSFERRINGAPRE-TRAINEDMODELTOUNSEENNETWORKENVIRONMENTS,WHEREMETAABR(HYBRID)MEANSA
METAABRMODELTRAINEDWITHTHEHybridDATASET,ANDSOARETHEREST
Fig.11. CDFofQoEmetrics(Trainset:Hybrid;Testset:4GNY).
Fig.12. CDFofQoEmetrics(Trainset:Hybrid;Testset:5G).
TABLEVII
COMPARISONOFQoE stdMETRICFORTRANSFERRINGAPRE-TRAINED
MODELON3GDATASETTOMULTIPLENETWORKENVIRONMENTS
Fig.13. ConvergenceofMetaABR.
According to the table, both MetaABR and Pensieve perform
well in 3G network (where train and test environment are the
same). After applying to other networks, Pensieve performs butMetaABRstillperformsthebestamongallscenarios.This
worsethanthemodel-basedapproachesBBAandRobustMPC, verifiesthepowerofmeta-learninginknowledgetransfer.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:29:03 UTC from IEEE Xplore. Restrictions apply.

2434 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.23,NO.3,MARCH2024
Fig.14. PerformanceofMetaABRwithdifferentpercentagesoftrainset.
Fig.15. Trade-offbetweenbitrate,rebufferingtimeandvariance.
3) Convergence: Wefurthershowthetrainingefficiencyof thatRobustMPCachieveshigherbitratewithlargerrebuffering
MetaABR.Figs.13(a)and(b)showthelossfunctionandreward timeandvariation.PensieveandBBAhavemodestbitrateand
oftrainingaPensievemodel,trainingaMetaABRmodelfrom rebuffering time/variation. Compared to the other algorithms,
scratch, and training a new task with a pre-trained meta-critic MetaABR achieves the best trade-off between different QoE
on3Gnetwork.ItisshownthatMetaABRconvergencesmore metrics,whichismuchmoreclosertotheidealsituation.
faster than that of Pensieve, whose loss approaches 0 after
50 epoches. The reward of MetaABR is significantly higher
E. PerformanceonMulti-VideoScenario
than that of Pensieve, which means it learns a better policy of
QoE optimization. It is noticed that learning a new task with Inthisexperiment,wetestthepre-trainedDRLmodelsona
MetaABRcanconvergewithin20epochs,whilePensievetakes multi-videoscenariotoevaluatetheirabilitytogeneralizeacross
about200epochstoconverge. multiple video streaming properties. We generate the trace of
4) Performance With Small Samples: Fig. 14 shows the re- multiplevideostreamingscenarioasfollows.Wegenerate1000
sults of MetaABR with different percentages of training sam- synthetic video traces with diverse bitrates, chunk sizes, and
ples. It is shown that even using only 10% of the total train video duration. The value of bitrate is randomly chosen from
dataset,MetaABRstillhascomparableperformancewithPen- {200, 300, 450, 750, 1200, 1850, 2850, 4300, 6000, 8000}
sievewithfulldataset. Kbps.Thechunksizeofeachvideoisameansizemultiplyinga
GaussiandistributionN(1,0.1).Thedurationofeachvideoisa
randomchunknumberintherange[20,100].WeapplytheDRL
D. Trade-OffBetweenQoEMetrics
modeltrainedwithHybriddatasetonthemulti-videoscenario,
Westudythetrade-offbetweendifferentconflictingQoEmet- andtheexperimentalresultsareillustratedinFig.16.Asshown
rics,andthenormalizedresultsareshowninFig.15.Itisshown inthefigure,MetaABRstilloutperformsthebaselinealgorithms
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:29:03 UTC from IEEE Xplore. Restrictions apply.

LIetal.:METAABR:AMETA-LEARNINGAPPROACHONADAPTATIVEBITRATESELECTIONFORVIDEOSTREAMING 2435
CDFofQoEmetricsofmulti-videoscenariotestingonWiFinetwork.
Fig.16.
| Fig.17. CDFofQoE | stdmetricsunderreal-worldnetworkscenarios. |     |     |     |     |     |     |     |     |     |     |
| ---------------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TABLEVIII
COMPARISONOFAVERAGEBITRATE(MBPS),REBUFFERINGTIME(SECOND),VARIATIONS,ANDQoE stdMETRICONREAL-WORLDSCENARIOS
on a variety of QoE metrics, and significant performance im- Bus:theclientisconnectedtoa4Gnetworkanditisplacedon
provementisfoundintheQoE fluentmetric.Theresultssuggest aschoolbuswithconstantmovement.
thatMetaABRcanbeadaptedtothemultiplevideostreaming TheCDFofQoEofdifferentABRalgorithmsunderdifferent
scenarioswithdiverseQoEproperties. scenariosiscomparedinFig.17,andtheaverageQoEmetrics
|     |     |     |     |     |     | are illustrated | in Table VIII. | Due | to page | limit, we only | show |
| --- | --- | --- | --- | --- | --- | --------------- | -------------- | --- | ------- | -------------- | ---- |
F. PerformanceonReal-WorldScenarios the QoE std metric for comparison. According to Fig. 17, the
CDFcurveofMetaABRislowerthanthatofotheralgorithms
Apartfromtrace-drivenexperiments,wedeploythecompared
inthreescenarios,whichmeansMetaABRisconcentratingon
algorithmsinawirelessnetworktestbedtotesttheperformance
|                  |            |     |       |        |                | the region | of higher QoE | std. According |     | to Table VIII, | in the |
| ---------------- | ---------- | --- | ----- | ------ | -------------- | ---------- | ------------- | -------------- | --- | -------------- | ------ |
| under real-world | scenarios. | We  | use a | laptop | (lenovo savior |            |               |                |     |                |        |
dormitoryscenario,MetaABRimprovestheQoEperformance
| y7000, windows | 10) as            | client, | and it connects |         | to a HUAWEI |         |                      |     |           |             |         |
| -------------- | ----------------- | ------- | --------------- | ------- | ----------- | ------- | -------------------- | --- | --------- | ----------- | ------- |
|                |                   |         |                 |         |             | by 4.2% | compared to Pensieve |     | and 57.4% | higher than | that of |
| P20 (Harmony   | 2.0.0) smartphone |         | which           | is used | as a proxy  | to      |                      |     |           |             |         |
RobustMPC.Similarly,significantQoEimprovementisfoundin
| establish | Wi-Fi or 4G connections. |     | The | laptop uses | a Chrome |     |     |     |     |     |     |
| --------- | ------------------------ | --- | --- | ----------- | -------- | --- | --- | --- | --- | --- | --- |
thelibraryandtheschoolbusscenarios.Insummary,MetaABR
browsertoaccessvideo-on-demandservicefromamediaserver
achievesthehighestQoEinallthreereal-worldscenarios,and
(Intel(R)Xeon(R)CPUE5-2630v4@2.20GHz;32GBDDR4
itsrebuffingtimeandvariationsaremuchlowerthanthatofthe
2400Mhz*4;64-bitUbuntu16.04),andtheABRalgorithmsare
baselinealgorithms.
| implemented | in dash.js | that is | used by | the player | for adaptive |     |     |     |     |     |     |
| ----------- | ---------- | ------- | ------- | ---------- | ------------ | --- | --- | --- | --- | --- | --- |
bitrateselection.Weconductexperimentsbasedonthreereal-
|                  |                |     |            |           |           |     | VI. | CONCLUSION |     |     |     |
| ---------------- | -------------- | --- | ---------- | --------- | --------- | --- | --- | ---------- | --- | --- | --- |
| world scenarios. | (1) Dormitory: |     | the client | is almost | static in | a   |     |            |     |     |     |
university dormitory and it connects to a small WiFi network. In this article, we addressed the challenges of deploying
(2) Library: the client is connected to a library WiFi network learningbasedABRmechanisminreal-worldvideostreaming
withmany usersaround and occasional movement. (3)School systems, and proposed a novel framework for meta-learning
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:29:03 UTC from IEEE Xplore.  Restrictions apply.

2436 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.23,NO.3,MARCH2024
based ABR design. Based on the proposed framework, we [22] Z.Lin,G.Thomas,G.Yang,andT.Ma,“Model-basedadversarialmeta-
proposedMetaABR,anoveladaptivebitrateselectionalgorithm reinforcementlearning,”inProc.34thInt.Conf.NeuralInf.Process.Syst.,
RedHook,NY,USA:CurranAssociatesInc.2020,pp.10161–10173.
basedonmeta-critictomaximizeusers’QoE.MetaABRjointly
[23] Z. Akhtar et al., “Oboe: Auto-tuning video abr algorithms to network
trainedmultiplelearningtaskswithasharedmeta-critic,andit conditions,”inProc.Conf.ACMSpecialInt.GroupDataCommun.,2018,
could provide transferrable knowledge to supervise bitrate se- pp.44–58.
[24] M. Dasari, K. Kahatapitiya, S. R. Das, A. Balasubramanian, and D.
lectionacrosstasks.Extensiveexperimentsbasedonreal-world
Samaras,“Swift:Adaptivevideostreamingwithlayeredneuralcodecs,”
tracesandtestbedshowedthatMetaABRachievedthebestQoE Proc.19thUSENIXSymp.NetworkedSyst.Des.Implementation,Renton,
comparedwiththestate-of-the-arts. WA,USA:USENIXAssociation,2022,pp.103–118.
[25] A.Zhang,C.Wang,B.Han,andF.Qian,“YuZu:Neural-enhancedvol-
umetricvideostreaming,”inProc.19thUSENIXSymp.NetworkedSyst.
REFERENCES Des. Implementation, Renton, WA, USA: USENIX Association, 2022,
pp.137–154.
[1] S.KrishnanandR.Sitaraman,“Videostreamqualityimpactsviewerbe- [26] Y.Liu,B.Han,F.Qian,A.Narayanan,andZ.-L.Zhang,“Vues:Practical
havior:Inferringcausalityusingquasi-experimentaldesigns,”IEEE/ACM mobile volumetric video streaming through multiview transcoding,” in
Trans.Netw.,vol.21,pp.2001–2014,Dec.2013. Proc.28thAnnu.Int.Conf.MobileComput.Netw.,NewYork,NY,USA:
[2] T.Stockhammer,“DynamicadaptivestreamingoverHTTP:Standardsand AssociationforComputingMachinery,2022,pp.514–527.
designprinciples,”inProc.2ndAnnu.ACMConf.MultimediaSyst.,2011, [27] X.Linetal.,“GSO-simulcast:Globalstreamorchestrationinsimulcast
pp.133–144. videoconferencingsystems,”inProc.ACMSIGCOMMConf.,NewYork,
[3] T.-Y.Huang,N.Handigol,B.Heller,N.McKeown,andR.Johari,“Con- NY,USA:AssociationforComputingMachinery,2022,pp.826–839.
fused,timid,andunstable:Pickingavideostreamingrateishard,”inProc. [28] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, and L. Sun, “Learning tai-
InternetMeas.Conf.,2012,pp.225–238. loredadaptivebitratealgorithmstoheterogeneousnetworkconditions:A
[4] Y.Sunetal.,“CS2P:Improvingvideobitrateselectionandadaptation domain-specificpriorsandmeta-reinforcementlearningapproach,”IEEE
withdata-driventhroughputprediction,”inProc.ACMSIGCOMMConf., J.Sel.AreasCommun.,vol.40,no.8,pp.2485–2503,Aug.2022.
2016,pp.272–285. [29] J.Lietal.,“LiveNet:Alow-latencyvideotransportnetworkforlarge-scale
[5] H.Mao,R.Netravali,andM.Alizadeh,“Neuraladaptivevideostreaming livestreaming,”inProc.ACMSIGCOMMConf.,NewYork,NY,USA:
withpensieve,”inProc.Conf.ACMSpecialInt.GroupDataCommun., AssociationforComputingMachinery,2022,pp.812–825.
2017,pp.197–210. [30] B. Wu, T. Li, C. Luo, C. Ouyang, X. Du, and F. Wang, “AutoPlex:
[6] Z.Lietal.,“Probeandadapt:RateadaptationforHTTPvideostreamingat Inter-session multiplexing congestion control for large-scale live video
scale,”IEEEJ.Sel.AreasCommun.,vol.32,no.4,pp.719–733,Apr.2014. services,”inProc.ACMSIGCOMMWorkshopNetw.-ApplicationIntegra-
[7] X. Xie, X. Zhang, S. Kumar, and L. E. Li, “piStream: Physical layer tion,NewYork,NY,USA:AssociationforComputingMachinery,2022,
informedadaptivevideostreamingoverLTE,”inProc.21stAnnu.Int. pp.1–6.
Conf.MobileComput.Netw.,2015,pp.413–425. [31] S.Hochreiter,A.S.Younger,andP.R.Conwell,“Learningtolearnusing
[8] J. Jiang, V. Sekar, and H. Zhang, “Improving fairness, efficiency, and gradientdescent,”inProc.Int.Conf.Artif.NeuralNetw.,2001,pp.87–94.
stabilityinHTTP-basedadaptivevideostreamingwithfestive,”inProc. [32] D.V.Prokhorov,L.Feldkarnp,andI.Y.Tyukin,“Adaptivebehaviorwith
8thInt.Conf.Emerg.Netw.ExperimentsTechnol.,2012,pp.97–108. fixedweightsinRNN:Anoverview,”inProc.IEEEInt.JointConf.Neural
[9] C. Yue, R. Jin, K. Suh, Y. Qin, B. Wang, and W. Wei, “Linkforecast: Netw.,2002,pp.2018–2022.
CellularlinkbandwidthpredictioninLTEnetworks,”IEEETrans.Mobile [33] R. J. Williams, “Simple statistical gradient-following algorithms for
Comput.,vol.17,no.7,pp.1582–1594,Jul.2018. connectionist reinforcement learning,” Mach. Learn., vol. 8, no. 3/4,
[10] L.Meietal.,“RealtimemobilebandwidthpredictionusingLSTMneu- pp.229–256,1992.
ralnetwork,”inPassiveandActiveMeasurement,D.ChoffnesandM. [34] C.Finn,P.Abbeel,andS.Levine,“Model-agnosticmeta-learningforfast
BarcellosEds.,Cham,Switzerland:Springer,2019,pp.34–47. adaptation of deep networks,” in Proc. Int. Conf. Mach. Learn., 2017,
[11] T.-Y.Huang,R.Johari,N.McKeown,M.Trunnell,andM.Watson,“A pp.1126–1135.
buffer-based approach to rate adaptation: Evidence from a large video [35] C.Fernandoetal.,“Meta-learningbythebaldwineffect,”inProc.Genet.
streamingservice,”inProc.ACMConf.SIGCOMM,2014,pp.187–198. Evol.ComputationConf.Companion,2018,pp.1313–1320.
[12] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal [36] M. Jaderberg et al., “Human-level performance in 3D multiplayer
bitrateadaptationforonlinevideos,”IEEE/ACMTrans.Netw.,vol.28, gameswithpopulation-basedreinforcementlearning,”Science,vol.364,
no.4,pp.1698–1711,Aug.2020. no.6443,pp.859–865,2019.
[13] X.Yin,A.Jindal,V.Sekar,andB.Sinopoli,“Acontrol-theoreticapproach [37] Z.Li,F.Zhou,F.Chen,andH.Li,“Meta-SGD:Learningtolearnquickly
fordynamicadaptivevideostreamingoverHTTP,”inProc.ACMConf. forfew-shotlearning,”2017,arXiv:1707.09835.
SpecialInt.GroupDataCommun.,2015,pp.325–338. [38] K.Young,B.Wang,andM.E.Taylor,“Metatraceactor-critic:Onlinestep-
[14] M.Gadaleta,F.Chiariotti,M.Rossi,andA.Zanella,“D-DASH:Adeep sizetuningbymeta-gradientdescentforreinforcementlearningcontrol,”
q-learning framework for dash video streaming,” IEEE Trans. Cogn. 2018,arXiv:1805.04514.
Commun.Netw.,vol.3,no.4,pp.703–718,Dec.2017. [39] N.Mishra,M.Rohaninejad,X.Chen,andP.Abbeel,“Asimpleneural
[15] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,X.Yao,andL.Sun,“Comyco: attentivemeta-learner,”2017,arXiv:1707.03141.
Quality-awareadaptivevideostreamingviaimitationlearning,”inProc. [40] Y.Duan,J.Schulman,X.Chen,P.L.Bartlett,I.Sutskever,andP.Abbeel,
27thACMInt.Conf.Multimedia,2019,pp.429–437. “RL2: Fast reinforcement learning via slow reinforcement learning,”
[16] F. Y. Yan et al., “Learning in situ: A randomized experiment in video 2016,arXiv:1611.02779.
streaming,”inProc.17thUSENIXSymp.NetworkedSyst.Des.Implemen- [41] J.Schulman,F.Wolski,P.Dhariwal,A.Radford,andO.Klimov,“Proximal
tation,2020,pp.495–511. policyoptimizationalgorithms,”2017,arXiv:1707.06347.
[17] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,X.Yao,andL.Sun,“Stick:Ahar- [42] F.Alet,M.F.Schneider,T.Lozano-Perez,andL.P.Kaelbling,“Meta-
moniousfusionofbuffer-basedandlearning-basedapproachforadaptive learningcuriosityalgorithms,”2020,arXiv:2003.05325.
streaming,”inProc.IEEEConf.Comput.Commun.,2020,pp.1967–1976. [43] V. Veeriah et al., “Discovery of useful questions as auxiliary tasks,”
[18] J. Quionero-Candela, M. Sugiyama, A. Schwaighofer, and N. D. 2019,arXiv:1909.04607.
Lawrence, Dataset Shift in Machine Learning. Cambridge, MA, USA: [44] Z.Zheng,J.Oh,andS.Singh,“Onlearningintrinsicrewardsforpolicy
MITPress,2009. gradientmethods,”2018,arXiv:1804.06459.
[19] R.Taori,A.Dave,V.Shankar,N.Carlini,B.Recht,andL.Schmidt,“Mea- [45] Z.Xu,H.vanHasselt,andD.Silver,“Meta-gradientreinforcementlearn-
suringrobustnesstonaturaldistributionshiftsinimageclassification,”in ing,”2018,arXiv:1805.09801.
AdvancesinNeuralInformationProcessingSystems,H.Larochelle,M. [46] K.Rakelly,A.Zhou,C.Finn,S.Levine,andD.Quillen,“Efficientoff-
Ranzato,R.Hadsell,M.Balcan,andH.Lin,Eds.,vol.33.RedHook,NY, policymeta-reinforcementlearningviaprobabilisticcontextvariables,”in
USA:CurranAssociates,Inc.,2020,pp.18583–18599. Proc.Int.Conf.Mach.Learn.,2019,pp.5331–5340.
[20] J.Schmidhuber,J.Zhao,andM.A.Wiering,“TechnicalreportIDSIA,” [47] W. Zhou, Y. Li, Y. Yang, H. Wang, and T. M. Hospedales, “Online
Tech.Rep.,vol.69–96,pp.1–23,1996.[Online].Available:https://dspace. meta-critic learning for off-policy actor-critic methods,” 2020, arXiv:
library.uu.nl/handle/1874/25022 2003.05334.
[21] S.ThrunandL.Pratt,“Learningtolearn:Introductionandoverview,”in [48] A.Nagabandietal.,“Learningtoadaptindynamic,real-worldenviron-
LearningtoLearn.Berlin,Germany:Springer,1998,pp.3–17. mentsthroughmeta-reinforcementlearning,”2018,arXiv:1803.11347.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:29:03 UTC from IEEE Xplore. Restrictions apply.

LIetal.:METAABR:AMETA-LEARNINGAPPROACHONADAPTATIVEBITRATESELECTIONFORVIDEOSTREAMING 2437
[49] Y.Duanetal.,“One-shotimitationlearning,”inProc.Int.Conf.Neural XiangLireceivedtheBSdegreeincomputerscience
Inf.Process.Syst.,2017,pp.1–12. fromtheHarbinInstituteofTechnology,China.He
[50] V.Mnihetal.,“Asynchronousmethodsfordeepreinforcementlearning,” iscurrentlyworkingtowardthemaster’sdegreewith
inProc.33rdInt.Conf.Int.Conf.Mach.Learn.,2016,pp.1928–1937. theDepartmentofComputerScience,NanjingUni-
[51] F. Sung, L. Zhang, T. Xiang, T. M. Hospedales, and Y. Yang, versity.Hehaspublishedseveralpeer-reviewpapers
“Learningtolearn:Meta-criticnetworksforsampleefficientlearning,” at international conferences and journals including
2017,arXiv:1706.09529. IEEEJournalonSelectedAreasinCommunications
[52] A. Gupta, R. Mendonca, Y. Liu, P. Abbeel, and S. Levine, “Meta- (JSAC).Hisresearchinterestsincludemediastream-
reinforcementlearningofstructuredexplorationstrategies,”inProc.Int. ing,networkcongestioncontrol,anddeeplearning.
Conf.NeuralInf.Process.Syst.,2018,pp.1–10.
[53] K.Rakelly,A.Zhou,D.Quillen,C.Finn,andS.Levine,“Efficientoff-
policymeta-reinforcementlearningviaprobabilisticcontextvariables,”,
2019,arXiv:1903.08254.
[54] A. G. Barto, R. S. Sutton, and C. W. Anderson, “Neuronlike adaptive
elementsthatcansolvedifficultlearningcontrolproblems,”IEEETrans.
Systems,Man,Cybern.,vol.13,no.5,pp.834–846,Sep./Oct.1983.
[55] I.Grondman,L.Busoniu,G.A.Lopes,andR.Babuska,“Asurveyofactor- YetingXureceivedtheBSdegreeincomputersci-
criticreinforcementlearning:Standardandnaturalpolicygradients,”IEEE ence from Central South University, China. She is
Trans.Systems,Man,Cybern.CAppl.Rev.,vol.42,no.6,pp.1291–1307, currentlyworkingtowardthemaster’sdegreewiththe
Nov.2012. DepartmentofComputerScience,NanjingUniver-
[56] S. Hochreiter and J. Schmidhuber, “Longshort-term memory,” Neural sity.Herresearchinterestsincludemediastreaming,
Computation,vol.9,no.8,pp.1735–1780,1997. networkcongestioncontrol,anddeepreinforcement
[57] R.Netravalietal.,“Mahimahi:Accuraterecord-and-replayforHTTP,”in learning.
Proc.USENIXAnnu.Tech.Conf.,2015,pp.417–429.
[58] N.Kan,C.Li,C.Yang,W.Dai,J.Zou,andH.Xiong,“Uncertainty-aware
robustadaptivevideostreamingwithbayesianneuralnetworkandmodel
predictivecontrol,”inProc.31stACMWorkshopNetw.OperatingSyst.
SupportDigit.AudioVideo,2021,pp.17–24.
[59] H.Riiser,P.Vigmostad,C.Griwodz,andP.Halvorsen,“Commutepath
bandwidthtracesfrom3Gnetworks:Analysisandapplications,”inProc.
4thACMMultimediaSyst.Conf.,2013,pp.114–118. YiYangreceivedtheBSdegreeincomputerscience
[60] “Raw data - measuring broadband America2016,” 2021. [Online]. fromNanjingUniversity,China.Heiscurrentlywork-
Available: https://www.fcc.gov/reports-research/reports/measuring- ingtowardthePhDdegreewiththeDepartmentof
broadband-america/raw-data-measuring-broadband-america-2016 ComputerScience,NanjingUniversity.Hisresearch
[61] A.Bokani,M.Hassan,S.S.Kanhere,J.Yao,andG.Zhong,“Comprehen- interests include network congestion control, rein-
sivemobilebandwidthtracesfromvehicularnetworks,”inProc.7thInt. forcementlearning,andedgecomputing.
Conf.MultimediaSyst.,2016,pp.1–6.
[62] L. Mei et al., “Realtime mobile bandwidth prediction using LSTM
neural network and bayesian fusion,” Comput. Netw., vol. 182, 2020,
Art.no.107515.
[63] D.Raca,D.Leahy,C.J.Sreenan,andJ.J.Quinlan,“Beyondthroughput,
thenextgeneration:A5Gdatasetwithchannelandcontextmetrics,”in
Proc.11thACMMultimediaSyst.Conf.,2020,pp.303–308.
[64] P.Wawrzynski,“Controlpolicywithautocorrelatednoiseinreinforcement Sanglu Lu (Member, IEEE) received the BS, MS,
learningforrobotics,”Int.J.Mach.Learn.Comput.,vol.5,no.2,2015, andPhDdegreesincomputersciencefromNanjing
Art.no.91. University, in 1992, 1995, and 1997, respectively.
SheiscurrentlyaprofessorwiththeDepartmentof
Computer Science and Technology and the deputy
directorofStateKeyLaboratoryforNovelSoftware
Technology.Herresearchinterestsincludedistributed
computing, pervasive computing, and wireless net-
works.Shehaspublishedmorethan100papersin
referredjournalsandconferencesintheaboveareas.
SheisamemberACM.
WenzhongLi(Member,IEEE)receivedtheBSand
PhDdegreesincomputersciencefromNanjingUni-
versity,China.HewasanAlexandervonHumboldt
Scholar fellow with the University of Goettingen,
Germany.HeisnowafullprofessorwiththeDepart-
mentofComputerScience,NanjingUniversity.His
researchinterestsincludedistributedcomputing,data
mining,mobilecloudcomputing,wirelessnetworks,
pervasive computing, and social networks. He has
publishedmorethan100peer-reviewpapersatinter-
nationalconferencesandjournals,whichincludeIN-
FOCOM,UBICOMP,IJCAI,ACMMultimedia,ICDCS,IEEECommunications
Magazine, IEEE/ACM Transactions on Networking (ToN), IEEE Journal on
SelectedAreasinCommunications(JSAC),IEEETransactionsonParalleland
DistributedSystems(TPDS),IEEETransactionsonWirelessCommunications
(TWC),etc.HeservedasProgramco-chairofMobiArch2013andRegistration
ChairofICNP2013.HewastheTPCmemberofseveralinternationalcon-
ferencesandthereviewerofmanyjournals.Heistheprincipleinvestigatorof
threefundingsfromNSFC,andtheco-principleinvestigatorofaChina-Europe
internationalresearchstaffexchangeprogram.HeisamemberofACM,and
ChinaComputerFederation(CCF).HewasalsothewinneroftheBestPaper
AwardofICC2009andAPNet2018.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:29:03 UTC from IEEE Xplore. Restrictions apply.