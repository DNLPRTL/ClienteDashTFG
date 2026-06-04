10378 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.23,NO.11,NOVEMBER2024
Bitrate Adaptation and Guidance With Meta
Reinforcement Learning
AbdelhakBentaleb ,Member,IEEE,MayLim ,MehmetN.Akcay ,AliC.Begen ,SeniorMember,IEEE,
andRogerZimmermann ,SeniorMember,IEEE
Abstract—Adaptive bitrate (ABR) schemes enable streaming significantresearchattention.ExistingABRschemes[15]canbe
clients to adapt to time-varying network/device conditions for a broadlyclassifiedasheuristicorlearning-based.ABRschemes
stall-free viewing experience. Most ABR schemes use manually
driven by heuristics make decisions based on client-side ob-
tunedheuristicsorlearning-basedmethods.Heuristicsareeasyto
servationssuchasthroughputestimation[31],playbackbuffer
implementbutdonotalwaysperformwell,whereaslearning-based
methods generally perform well but are difficult to deploy on level [47] or a combination of the two [53]. Although these
low-resource devices. To make the most out of both worlds, we schemes are easy to implement, they heavily depend on some
earlier developed Ahaggar, a learning-based scheme executing configuration parameters, and a poor setting may significantly
ontheserversidethatprovidesquality-awarebitrateguidanceto
hindertheirefficacy[27].Hence,learning-basedschemeshave
streamingclientsrunningtheirownheuristics.Ahaggar’snovelty
becomeanalternative,benefitingfromthelatestbreakthroughs
isthemetareinforcementlearningapproachtakingnetworkcondi-
tions,clients’statusesanddeviceresolutions,andstreamedcontent inmachinelearning(ML)suchasdeepreinforcementlearning
asinputfeaturestoperformbitrateguidance.Ahaggarusesthe (DRL), and supervised and imitation learning techniques [5].
newCommonMediaClient/ServerData(CMCD/SD)protocolsto Learning-basedschemesattaingoodstrategieswithoutrequiring
exchangethenecessarymetadatabetweentheserversandclients.
anypresumptionsabouttheenvironment.
WhileAhaggarwasasignificantstepforward,inthisstudy,we
Nonetheless, learning-based schemes are exposed to two
focusonthreeopenareas,namely,(i)exploringtheperformanceof
AhaggarinaheterogeneousenvironmentincludingbothAhag- major limitations. First, their performance heavily depends on
gar and non-Ahaggar clients with varied network conditions the training data. Network environments can be quite diverse,
and device resolutions, and (ii) quantifying the impact of device and their dynamics change over time. Therefore, future states
resolutionsonQoEwithAhaggar.Wethoroughlyinvestigatethese
are not easy to predict accurately. Most schemes use classical
areasandreportourfindings.Wealso(iii)discusstheAhaggar
approaches to train an agent by giving feedback for decisions
designchoices.Experimentsonanopen-sourcesystemshowthat
Ahaggar adapts to unseen conditions fast and outperforms its whileinteractingwithanenvironment.Suchinteractioncanbe
competitorsinseveralviewerexperiencemetrics. efficientlyperformedinacontrolledtrace-drivensimulator.Still,
a mismatch may occur when the trained model is deployed in
Index Terms—Adaptive streaming, meta-RL, ABR, CMCD,
a live system and encounters an environment not previously
CMSD,bitrateguidance,qualityawareness.
seen [55]. As a result, the scheme may fail to perform proper
rate adaptation. Second, deploying learning-based schemes on
I. INTRODUCTION
deviceswithscarceresourcesisimpracticalduetohighstorage
WITHtheprevalenceofHTTPadaptivestreaming(HAS),
andcomputationalcosts.Priorwork[55]showedthatalearning
the design of adaptive bitrate (ABR) logic—the algo-
model trained on past network scenarios could hardly provide
rithm deciding which segments to download and when (pri-
a comparable performance under new conditions, and hence,
marilybasedontheadvertisedencodingbitrate)—hasreceived
effective and continual model retraining/update was required.
Lastly, many studies [22], [30] claim that perceptual video
Manuscript received 22 January 2024; accepted 5 March 2024. Date of quality and device resolution must be considered in the ABR
publication 12 March 2024; date of current version 3 October 2024. This
logictoimprovethequalityofexperience(QoE).Incorporating
workwassupportedinpartbySingaporeMoEAcademicResearchFundTier
2 under MOE’s official under Grant T2EP20221-0023, and in part by the these parameters into a learning model and then continually
ScientificandTechnologicalResearchCouncilofTürkiyeunderGrant120C154. retraining the model is also infeasible for clients running on
RecommendedforacceptancebyR.Zhang.(Correspondingauthor:Abdelhak
low-resourcedevices.
Bentaleb.)
AbdelhakBentalebiswiththeGinaCodySchoolofEngineeringandCom- In our prior work (Ahaggar) [14], we have shown that
puterScience,ConcordiaUniversity,Montreal,QCH3G1M8,Canada(e-mail: heuristic and learning-based schemes can complement each
abdelhak.bentaleb@concordia.ca).
other and leveraging the advantages of both solutions while
May Lim and Roger Zimmermann are with the School of Computing,
NationalUniversityofSingapore,Singapore119077(e-mail:maylim@comp. avoiding their shortcomings is the key. This brings up the
nus.edu.sg;rogerz@comp.nus.edu.sg). following three questions, which we seek to answer: ❶ Can
Mehmet N. Akcay and Ali C. Begen are with Ozyegin University,
werunalightweightheuristic-basedschemeontheclientside
34794 Istanbul, Türkiye (e-mail: necmettin.akcay@ozu.edu.tr; ali.begen@
ozyegin.edu.tr). andlearning-basedbitrateguidanceontheserverside(whichis
This article has supplementary downloadable material available at not as constrained as the clients) such that they can cooperate
https://doi.org/10.1109/TMC.2024.3376560,providedbytheauthors. harmoniously to deliver s better QoE? ❷ How to implement
DigitalObjectIdentifier10.1109/TMC.2024.3376560
1536-1233©2024IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:30:43 UTC from IEEE Xplore. Restrictions apply.

BENTALEBetal.:BITRATEADAPTATIONANDGUIDANCEWITHMETAREINFORCEMENTLEARNING 10379
bitrate guidance with perceptual quality and device resolution convey Ahaggar bitrate guidance decisions to media clients
awareness?❸Howtoachievecontinuallearningfortheserver- throughtheHTTPresponseheaders.
sidebitrateguidance? We evaluate the performance of Ahaggar against several
WeanswerthequestionsaboveinthecontextofAhaggar,1a ABRsolutionsbyrunningreal-worldtrace-drivenexperiments.
metareinforcementlearning(meta-RL)-basedsolution.Ahag- These experiments cover multiple clients with heterogeneous
garhasaserver-sidelearningmodelthattakesnetworkcondi- network conditions and device resolutions. Experimental re-
tions,clients’statuses,deviceresolutionsandstreamedcontent sultsshowthatAhaggardeliversconsistentquality,improves
asinputfeatures,andthenprovidesqualityandresolution-aware viewerQoEbyupto87.0%,reducesrebufferingdurationbyup
bitrateguidancetothestreamingclients.Leveragingtheserver’s to84.4%andreducesbandwidthconsumptionbyupto62.6%.
vastcomputationalpower,storagecapacityandmemory,Ahag- In addition, Ahaggar quickly converges to the best solution
gar enables model inference for performing bitrate guidance during the training process with an improvement of 5.6× in
tasksandhelpsresource-constrainedstreamingclientsruntheir termsofthenumberofepochsrequiredand6×speeduponthe
lightweight heuristic-based ABR schemes. Ahaggar models training time compared to the recent RL-based solutions such
bitrate guidance tasks for multiple clients as a partially ob- as[35],[52].
servableMarkovdecisionprocess(POMDP)andleveragesthe ThispaperisanextendedversionofAhaggar [14],focusing
latestdevelopmentsinDRLtodynamicallyadapttothevarying onthreemainareasthatremainopen:
networkconditions.Specifically,itusesadvantageActor-Critic 1) Weconductedmoreexperimentalevaluationstoassessthe
networks (A2C) for model training and Distributed Proximal performanceofAhaggarinmorechallengingscenarios,
PolicyOptimization(DPPO)[25]withclipandAdamoptimizer especially in a heterogeneous environment that includes
forpolicyupdatesateachtimeinterval.Consideringthechanges bothAhaggarandnon-Ahaggarclientswithdifferent
intheenvironment,weadoptaModelAgnosticMeta-Learning networkconditionsanddeviceresolutions.
(MAML)[23]on-policygradient-basedmeta-RLapproachthat 2) WeinvestigatedtheimpactofdeviceresolutiononAhag-
embedspolicygradientstepsintothemetaoptimization.Thisal- garQoEenhancement.
lowsAhaggartoupdatethemodelparameterstoachievegood 3) We explored the design choices of Ahaggar, including
generalizationperformanceonunseenenvironmentsduringthe why we used DPPO and MAML as the policy update
inference.Therefore,ourmodelcanconvergequicklytothebest solutionandthemeta-RLalgorithm,respectively.Wealso
performanceandadapttonewunseenenvironmentswithonlya examinedtheeffectsofthenumberofshots,thelearning
smallnumberof(e.g.,40)shots.Toourknowledge,thispaper episodeandtheAhaggarmodelconvergence.
is the first study using meta-RL to improve QoE for adaptive The rest of the paper is organized as follows. Section II
streaming clients while cleanly separating the responsibilities shows the existing solutions for QoE optimization. Section III
fortheserversandclientsandrespectingtheclient-drivennature describestheAhaggarsolution,followedbyitsdesignchoices
ofHAS. inSectionIV.TheperformanceevaluationinSectionsVandVI
The Ahaggar solution comprises two phases: (i) (offline) concludesthepaper.
meta-training,whereeachRLagenttrainstheAhaggarmeta-
modelonheterogeneousnetworkenvironments,and(ii)(online)
II. RELATEDWORK
meta-testing (also called inference), where each agent contin-
ually learns the system dynamics and rapidly optimizes the Client-Driven Heuristic-Based ABR: These schemes use
meta-policy,adjustingtheparameterweightsthatdeterminethe heuristics based on estimated throughput (e.g., PANDA [31]),
agentbehavioraccordingtothetrajectoriescollectedfromboth bufferlevel(e.g.,BOLA[47]),segmentsize(e.g.,SARA[8]),
the meta-training and meta-testing. We take inputs from the oracombination(e.g.,MPCDASH[53]).
network,clientsandstreamedcontentintotheAhaggarneural Client-Driven Learning-Based ABR: These schemes learn
network(NN)forbitrateguidance.TheobjectiveofAhaggar fromthestreamingenvironmentbytraininganNNusingDRL
istoselecttheminimumbitrate(amongtheavailable options) techniques [6], [17]. Mao et al. [35] proposed Pensieve, the
above which the next higher bitrate improves the perceptual firstlearningABRthatusedDRLtogenerateastrategytoward
quality only insignificantly at the specific device resolution. maximizingtheviewerQoE.Bentalebetal.[10]designedAMP
In this study, we use an objective full-reference perceptual thatimplementedasetoflearning-basedbandwidthpredictors
videoqualitymetricknownasVideoMulti-methodAssessment and model auto-selection for HAS. Similarly, Fugu [52] was
Fusion(VMAF)[42]. proposed to leverage the hidden Markov model for accurate
To ensure healthy cooperation without incurring additional throughputprediction.Huangetal.[27]usedimitationlearning
complexitiesbetweentheclientsandservers,Ahaggaradopts toproposeComycoasABRforon-demandvideos.
the emerging Common Media Client/Server Data standards: Server-Driven Solutions: These solutions implement a rate
CMCD[9],[13],[18]andCMSD[7],[19],[33].CMCDdefines control on the server to control a client’s ABR decisions im-
asetofinformationcollectedbyamediaclientandsentalong plicitly or explicitly. In implicit control, the server does not
withtheHTTPrequeststotheserverrunningAhaggarinquery requirecooperationfromtheclient.Tothatend,somesolutions
arguments or header extensions. CMSD allows the server to leveraged traffic shaping [4], [57] or super-resolution [29]. In
explicitcontrol,theserverreceivesinformationfromtheclients
1AhighlandregioninthecentralSaharainsouthernAlgeria. forintelligentQoEoptimizationdecisions(e.g., [13]).
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:30:43 UTC from IEEE Xplore. Restrictions apply.

10380 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.23,NO.11,NOVEMBER2024
problemformultipleclientscanbeformulatedas
⎧
|     |     |     |     | fi    | n d l c ,(cid:2) (π ) , ∀c | ∈ [1,...,N],∀t∈[1,...,k] |     |     |     |
| --- | --- | --- | --- | ----- | -------------------------- | ------------------------ | --- | --- | --- |
|     |     |     |     | ⎪⎪⎪⎪⎨ | t                          |                          |     |     |     |
|     |     |     |     |       | Q o E                      | π)                       |     |     |     |
|     |     |     |     | ar    | g m a x                    | c(                       |     |     |     |
t
|     |     |     |     |       | lc,(cid:2)(π)≤mtpc π |     | C.1 |     | ,   |
| --- | --- | --- | --- | ----- | -------------------- | --- | --- | --- | --- |
|     |     |     |     | s.t.  |                      |     |     |     | (1) |
|     |     |     |     | ⎪⎪⎪⎪⎩ | t                    | t   |     |     |     |
(cid:6)N
|     |     |     |     |     | lc,(cid:2)(π)≤BW |     | C.2 |     |     |
| --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
total
t
c=1
wherelc,(cid:2)
isthebestbitrate,whichistheminimumamongthe
t
availableoptionsaboveandthenexthigherbitrateimprovesthe
|     |     |     |     | perceptual | quality only | insignificantly | for | the specific | content |
| --- | --- | --- | --- | ---------- | ------------ | --------------- | --- | ------------ | ------- |
atthespecificdeviceresolution.Here,weuse1-JND(JustNo-
ticeableDifference)asthethresholdforbeingsignificant[37].
Fig.1. MARLofAhaggar.
π
|     |     |     |     | Further in             | this formulation, | is                           | an RL policy | that | decides the |
| --- | --- | --- | --- | ---------------------- | ----------------- | ---------------------------- | ------------ | ---- | ----------- |
|     |     |     |     | bitrateforeachclient,N |                   | isthetotalnumberofclients,BW |              |      |             |
total
isthetotalservercapacityandmtpcisthemeasuredthroughput
| Network-DrivenSolutions:Thesesolutionscanbefurthercat- |     |     |     | byclientc. |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
egorizedinto:(1)In-networksolutionswheresomeworks[11], Theformulationin(1)isamulti-agentdecisionproblemand
[12] use software-defined networking to assist clients in their aimstofindthebestbitratelc,(cid:2)thatmaximizestheviewerQoEc
|     |     |     |     |     |     | t   |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ABRdecisions,rateallocation[38]ormulti-pathdelivery[16]; foreachclientcwithrespecttoC.1–C.2.Here,eachclienthas
(2) Server and network assistance solutions where some pa- access only to its local observations, and fully capturing the
| pers [40], | [49] leverage | the SAND standard | [1] that enables |     |     |     |     |     |     |
| ---------- | ------------- | ----------------- | ---------------- | --- | --- | --- | --- | --- | --- |
stateoftheglobalenvironmentexperiencedbyallclientsisnot
datacollectionfromvariousnetworkentitiesinvolvedinmedia feasible.Therefore,wecasttheproblem(1)asapartiallyobserv-
delivery. These data are then stored on a centralized server ableMarkovdecisionprocess(POMDP),whichischaracterized
| for intelligent | decisions, | e.g., rate allocation; | (3) Data-driven |                    |     |            |             |               |     |
| --------------- | ---------- | ---------------------- | --------------- | ------------------ | --- | ---------- | ----------- | ------------- | --- |
|                 |            |                        |                 | by its observation | and | historical | information | capabilities. | The |
solutionsthatcombineSANDwithAIcapabilitiesforimproved POMDPmodelconsistsof11-tuplesPOMDP=(S,A,O,R,
decision making. These solutions collect QoE metrics from P,U,Z,C,N,α,γ),where:
(cid:2)
manystreamingsessionsatalogicallycentralizedcontrollerthat ={S1,...,SN}isthesetofthefiniteanddiscreteagent
S
maintains a global view of the real-time network conditions, statesofN agents.Foreachagentc,wedefinethesetof
based on which the controller makes decisions regarding the Sc ={sc,...,sc}, k =|Zc|
|     |     |     |     | agent | states as | 1   | where |     | is the |
| --- | --- | --- | --- | ----- | --------- | --- | ----- | --- | ------ |
k
individualsessions(e.g., [24],[28]). totalnumberofbitrateguidancetasks.
(cid:2)
A={A1,...,AN}isthefiniteanddiscretesetofactions
|     |     |     |     | ofN | agents.Foreachagentc,wedefinethesetofagent |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
III. AhaggarBITRATEGUIDANCE
|     |     |     |     | actions | as Ac ={ac,...,ac}, |     | where | each | action is the |
| --- | --- | --- | --- | ------- | ------------------- | --- | ----- | ---- | ------------- |
1 k
Ahaggarservesmultipleclients(agentsinRL)withashared selectedbitratelcduringabitrateguidancetask.
(cid:2)
environment,distinctrewardsandpolicies,asdepictedinFig.1. O ={O1,...,ON} is the finite set of observation states
It performs bitrate guidance tasks at every time window and capturedbythesetofagents.Foreachclientc,thesetof
|     |     |     |     | observationsisOc |     | ={oc,...,oc}. |     |     |     |
| --- | --- | --- | --- | ---------------- | --- | ------------- | --- | --- | --- |
decidesthebestbitrateforeachclient.Therefore,weconsidera
|     |     |     |     | (cid:2) |     | 1   | k   |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
fullycooperativemulti-agentRL(MARL)[56]frameworkwith R={R1,...,RN} is the set of expected immediate re-
| independentlearnerssettingthatinvolvesasetofagentssharing |     |     |     |        |               |     |            |         | N        |
| --------------------------------------------------------- | --- | --- | --- | ------ | ------------- | --- | ---------- | ------- | -------- |
|                                                           |     |     |     | wards, | which depends | on  | states and | actions | taken by |
thesameenvironment.Inparticular,weuseacentralizedtraining agents. For each client c, the set of rewards is Rc =
withdecentralizedexecution(CTDE)paradigm[56]totrainthe {rc,...,rc}.
|     |     |     |     | (cid:2) 1 | k   |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
P =S×S×A→[0,1]isthestatetransitionprobability
MARLagents.CTDEallowstheseagentstotraindecentralized
policies with global information during training and to make functionP(s(cid:7)|s,a)fromthestatestos(cid:7) ∈S whenaction
decisions based on the individually learned policies during a∈Aistaken.
(cid:2)
inference. We also use MAML [23], the meta-RL algorithm, U =O×S×A→[0,1] is the observation probability
to adapt to various network environments through parameter functionO(o(cid:7)|s(cid:7),a)ofobservingo(cid:7) ∈Oaftertransitioning
learning.TheoverallworkflowofAhaggarisshowninFig.2, tos(cid:7)duetoa.
|     |     | (cid:2) (cid:2) |     | (cid:2) |     |     |     |     |     |
| --- | --- | --------------- | --- | ------- | --- | --- | --- | --- | --- |
wherethestepsarenumberedas 1 – 8 . Z ={Z1,...,ZN}representsthebitrateguidanceprob-
|     |     |     |     |     | QoEc(π) |     |             | c.  |            |
| --- | --- | --- | --- | --- | ------- | --- | ----------- | --- | ---------- |
|     |     |     |     | lem | max π   | for | every agent | The | set of bi- |
t
|     |     |     |     | trate | guidance tasks | for agent | c is thus | defined | as Zc = |
| --- | --- | --- | --- | ----- | -------------- | --------- | --------- | ------- | ------- |
A. FormulationoftheProblem
{zc,...,zc}.
|     |     |     |     | (cid:2) 1 | k   |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
Ateachsegmentdownloadtimeepocht,Ahaggarperforms C ={1,...,N}isthesetofNagents,whereNisthetotal
thebitrateguidancetasks(denotedbyZ)byselectingthebest numberofagentsandc∈[1,...,N]isanagent.
(cid:2)
bitrate(denotedbylc)withrespecttothecurrentstate(denoted αandγ ∈[0,1]arethelearningrateanddiscountfactor,
t
by sc) of each client c. Mathematically, the bitrate guidance respectively.
t
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:30:43 UTC from IEEE Xplore.  Restrictions apply.

BENTALEBetal.:BITRATEADAPTATIONANDGUIDANCEWITHMETAREINFORCEMENTLEARNING 10381
Fig.2. OverallbitrateguidancesystemofAhaggar.
t=[1,...,k], c datasets.Eachtraceentryconsistsofathroughputvalue(Mbps),
| At each | time |     |     | each agent |     | does not | track the |     |     |     |     |     |     |
| ------- | ---- | --- | --- | ---------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- |
exactstatesc,butratheritusestheobservationsocforanygiven
round-triptime(RTT;ms)andpacketloss(%).
|     | t   |     |     |     |     | t   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
task zc. Therefore, it has to rely on the history of actions and (cid:2) Content Traces. We used the Comyco [27] and Waterloo
t
hc,
observations, denoted by to perform the best actions that SQoE-IV[22]datasets.Tocoverawiderangeofdeviceresolu-
t
resultinhigherrewards.Wedefinethesetofhistoriesofclientc tions,eachsourcevideowasencodedat{0.24,0.37,0.57,0.75,
asHc ={hc,...,hc}wherehc ={(ac,oc);...;(ac,oc)}and 1.0,1.76,2.36,3.0,4.3,5.7,8.0,11,16.6}Mbpsataresolutionof
|                      | 1   | k   |                              | t   | t t |     | 1 1 |     |     |     |     |     |     |
| -------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thesetofhistoriesofN |     |     | agentsasH={H1,...,HN}.Yet,hc |     |     |     |     |     |     |     |     |     |     |
{180,216,288,288,360,540,720,720,1080,1080,1440,2160,
t
mightexponentiallygrowwitheveryactiontakenandeverystate 2160}p,respectively.Eachtraceiscomprisedofvideosegments
observed.Inthiscase,theagentratherselectstousethebelief withtheircorrespondingencodedbitrates(Mbps),sizes(bytes)
states, denoted by Bc, which are single-valued and represent and VMAF scores for three device resolutions (phone, HDTV
| theobservationprobabilityUcoverallpossiblehistoriesHcin |     |     |     |     |     |     |     | andUHDTV). |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
bc ∈Bc,
a given bitrate guidance task. For each the observa- WeperformedcustomizedmodificationsontheParksimula-
t
tion probability distributio(cid:6)n is de(cid:6)noted by uc =O(oc |hc ,ac ), tor[34]tofullycomplywiththeAhaggardesign.Specifically,
|                      |     |       |     |     |              | t   | t t t   |                                                    |     |     |     |     |     |
| -------------------- | --- | ----- | --- | --- | ------------ | --- | ------- | -------------------------------------------------- | --- | --- | --- | --- | --- |
| suchthatO(oc|hc,ac)= |     |       |     |     | P(sc|hc)P(sc |     | |sc,ac) |                                                    |     |     |     |     |     |
|                      |     |       | sc  | sc  |              |     | t+1     | werevised(i)theproblemspaceusingPOMDPinsteadofMDP, |     |     |     |     |     |
|                      |     | t t t | t+1 | t   | t            | t   | t       | t                                                  |     |     |     |     |     |
O(oc |sc ,ac),whereP(sc|hc)isthebeliefstatebcaboutthe (ii)inputstate,actionandrewardspaces,(iii)NNarchitecture
| t+1 | t+1 | t   | t   | t   |     |     | t   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
statesc,Bc ={bc,...,bc}andB ={B1,...,BN}aretheset withpolicyupdateandmeta-RLapproaches,(iv)headlessvideo
| t   |     | 1   | k   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of belief states of agent c and the set of the finite and discrete client by introducing three device resolutions, and (v) MARL
|               |     | N       |               |     |       |        |            | withCTDEandsharedenvironmentsupport.Duringthesession, |     |     |     |     |     |
| ------------- | --- | ------- | ------------- | --- | ----- | ------ | ---------- | ----------------------------------------------------- | --- | --- | --- | --- | --- |
| belief states | of  | agents, | respectively. |     | These | belief | states are |                                                       |     |     |     |     |     |
asufficientmeasureofhistoriesandgiven abeliefstatebc,an thesimulatorusedthetracesandeachclientinteractionwiththe
t
agentcstrivestofindtheeffectiveoptimalpolicyπc,(cid:2) tosolve environmentasinputfeaturestofeedintotheNN,fromwhich
theRLagent,inturn,decidedthesegmentbitratesateverytime
(1)byfindingthebestbitrateforeachclientthatmaximizesthe
| accumulateddiscountedreward(denotedbyGc |     |     |     |     |     | anddefinedin |     | step. |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | ----- | --- | --- | --- | --- | --- |
t
TheAhaggarusesanA2CNN.Withoutlossofgenerality
SectionIII-B).
|     |         |          |       |        |     |       |         | and since | the agents | are independent, |     | we simplify | the formu- |
| --- | ------- | -------- | ----- | ------ | --- | ----- | ------- | --------- | ---------- | ---------------- | --- | ----------- | ---------- |
| The | Ahaggar | learning | model | solves | the | POMDP | problem |           |            |                  |     |             |            |
(1) using a multi-agent A2C [6] NN with clipped DPPO [25] lation in the context of a single agent. At every time epoch
(π) t, the segment-level statistics for each agent are collected and
| and Adam | optimizer |     | for policy | updates |     | at every | time in- |     |     |     |     |     |     |
| -------- | --------- | --- | ---------- | ------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- |
terval. For continual learning and quickly adapting to unseen aggregatedastheenvironmentinputstate.DifferentfromMDP,
|                   |     |         |          |          |                 |        |          | in POMDP,     | the agent | cannot | directly | observe      | the complete   |
| ----------------- | --- | ------- | -------- | -------- | --------------- | ------ | -------- | ------------- | --------- | ------ | -------- | ------------ | -------------- |
| environments,     |     | it uses | MAML—the |          | meta-RL         | policy | gradient |               |           |        |          |              |                |
|                   |     |         |          |          |                 |        |          | system state, | but the   | agent  | makes    | observations | that depend on |
| approach—allowing |     | Ahaggar |          | to learn | hyper-parameter |        | ini-     |               |           |        |          |              |                |
tializationand speed up theoptimization of thelearned model thestate.Theagentusestheseobservationstoformabeliefabout
whatstatethesystemiscurrentlyin.Thisiscalledabeliefstate
duringinference.
|     |     |     |     |     |     |     |     | and is expressed | as  | a probability | distribution |     | over all possible |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------- | ------------ | --- | ----------------- |
states.ThesolutionofthePOMDPisapolicyprescribingwhich
actiontotakeineachbeliefstate.Formally,RLagentsinteract
| B. AhaggarMeta-Training(Offline) |     |     |     |     |     |     |     |          |             |      |         |             | S,          |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ---- | ------- | ----------- | ----------- |
|                                  |     |     |     |     |     |     |     | with the | environment | that | defines | state space | observation |
To train the Ahaggar meta-model, we use Park [34]—a spaceOandbeliefstatespaceB.Ateachtimeepocht,eachRL
|                                                       |     |     |     |     |     |     |     | agentcobservesastateoc |     |     | ∈Oandthenreceivesabeliefstate |     |       |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | ----------------------------- | --- | ----- |
| Python-basedsegment-levelsimulatorthatisbasedonOpenAI |     |     |     |     |     |     |     |                        |     | t   |                               |     |       |
|                                                       |     |     |     |     |     |     |     | bc ∈B                  |     |     |                               |     | ac ∈A |
and state-of-the-art ABR simulators [46] for RL-based model from the environment. Later, it takes an action
|     |     |     |     |     |     |     |     | t   |     |     |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
training.Thissimulatorfaithfullyemulatesastreamingsession (aka lc,(cid:2)) while it receives a reward rc ∈R. Here, each agent
|     |     |     |     |     |     |     |     | t                                     |     |     |     | t     |           |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | ----- | --------- |
|     |     |     |     |     |     |     |     | caimstofindtheoptimalpolicyπc,(cid:2) |     |     |     | :S →O | →B →Athat |
wherethelearningagentusesalargecorpusofreal-worldnet-
workandcontenttracestoexplorethestreamingenvironment. mapsstates-to-actionsandmaximizesthereward.
(cid:2)NetworkTraces.WeusedtheBelgium4G/LTE[51],Nor- (cid:2) Input State. At each time epoch t, each agent c takes a
|     |     |     |     |     |     |     |     |     |     |     |     | bc {mtpc, | qtc, blc, lsc, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------------- |
way 4G/LTE [43], NYU LTE [36] and Lumous 4G/5G [39] belief state with inputs defined as =
|     |     |     |     |     |     |     |     |     |     |     |     | t   | t t t t |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- |
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:30:43 UTC from IEEE Xplore.  Restrictions apply.

10382 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.23,NO.11,NOVEMBER2024
−−→ −−→
dtc,rsc,LSc,QTc},comprisedofnetwork,contentandplay- Comyco [27] and Waterloo SQoE-IV [22], where 70% of the
t t t t
data is used for training and 30% for testing. We followed
backfeaturesofthelastdownloadedsegment.Theseinputsare
measuredthroughputmtpc(Kbps),VMAFqualityqtc(0–100), the same setup to tune the coefficients and our results show
current playback buffer le t ngth blc (second), segmen t t size lsc that ω 1 =0.077, ω 2 =1.249, ω 3 =2.877, ω 4 =0.049, and
(KB),downloadtimedtc(second) t ,percentageoftheremaining t ω 5 =1.436 achieve the best trade-off between the five QoE
t
segments inthevideorsc (%),vector ofmavailable sizesfor metrics.Theseresultsaresimilarto[50].
−−→ t (cid:2) Policy Gradient and Training Algorithm. The essential
the next segment LSc (KB) and vector of m available VMAF
t −−→ objective of Ahaggar is to improve the policy via boosting
qualitiesforthenextsegmentQTc (0–100).Insteadoffeeding
t the probabilities of high-reward samples from the collected
the A2C NN the exact values of the input state, we normalize
trajectories and declining the possibilities of failure samples
themtoenabletheagenttogeneralizethestrategybetterinan from the bad trajectories. For every time epoch t, each RL
unseennetworkenvironment[3]. agent c of Ahaggar selects the action ac that corresponds
(cid:2)ActionSpace.TheactionspaceAisdefinedastheavailable t
to the bitrate for the next segment using the improved policy
bitrate levels (i.e., n-dimensional vector) for a given video. In π :πc,(cid:2)(bc,ac)→[0,1] at state bc, which results in the best
eachtimeepocht,theAhaggarpolicyπc,(cid:2)ofagentcmapsbc θ t t t
t accumulateddiscountedrewardthatisexpressedas
tocompactdiscreteactionspaceAandselectac,(cid:2) ∈A.
t
(cid:2)ObservationSpace.WeexposeasubsetofAhaggarstates
astheobservations,wheretheagentcobservesoc={mtpc,qtc, (cid:7)Tπ θ c
blc,lsc,dtc,rsc,L −− S → c,Q −− T → c}foreachtimeepoc t ht. t t Gc t = γt¯−t×r t c, ac t =argmaxE[Gc t (bc t ,a)], (3)
t (cid:2) t Outp t ut. t The t Ahag t gar actor model returns 1×n- t¯=t a
dimensionalvectorrepresentingbitratelevelswiththeirassoci-
atedprobabilities.πc,(cid:2) :bc →ac,(cid:2)mapsthestatebctothebest where Gc
t
is computed from time t to the end of training,
action ac t ,(cid:2) based on the s t tate-a t ction probabilities, t where ac t ,(cid:2) T γ π ∈ θ c d [0 e , n 1 o ] te is s t t h h e e d b i a s t c c o h u s n i t ze fa f c o t r or u , p θ da is tin th g e th p e ol g ic r y ad p ie a n ra t m po e l t i e c r y , a π n θ c d ,
withthehighestprobabilityisselectedunderthecurrentstate.
πc,(cid:2)(bc,ac)istheprobabilitythatactionac istakeninstatebc.
The Ahaggar critic model outputs a single scalar indicating θ t t t t
thevaluefunctionVc,π(bc)forthecurrentstate. DPPOallowsAhaggartorunmulti-agents(orworkers),where
t
(cid:2) NN Architecture. The Ahaggar A2C NN architecture eachagenthasitsownA2Cnetworkanddatacollection.Thus,
thegradientcalculationsaredistributedoverworkers,asshown
consists of two networks: actor and critic. Each network uses
two1DConvlayersandsixlinearfully-connected(FC)layersto
inFig.1.Foreachepisode,anagentcupdatesitsgradientpolicy
extract the set of features. Each 1DConv layer consists of 3x3 suchthatGc t ismaximizedwithrespecttothepolicyparameters
θ,asfollows:
convolution with feature number (=64) and kernel size (=1)
−−→ −−→
to feed the features LSc and QTc. Other inputs are fed into
t t
F U C nit la ( y R e e rs LU w ( it ) h ) f a e c a t t i u v r a e tio n n um fu b n e c r ti ( o = n 6 . 4 T ) h a e n n d , a a ll R in e p c u ti t fi l e a d ye L r i s ne a a re r (cid:8)G¯c = 1 (cid:7)Θ (cid:7)Tπ θ c Aπθ c (bc,ac)(cid:8)logπc(ac,sc), (4)
t Θ t t t θ t t
concatenated and finally fed into an FC layer with 64 neurons θ=1t=1
andaslopeof0.5todown-sampletheconcatenatedfeatures.The
actorandcriticusethesamestructurebutwithdifferentoutputs. where Θ is the total number of episodes, Aπθ c (bc,ac) is the
t t
For both networks, we use the Softmax activation function advantagefunctionthatrepresentsthedifferenceintheexpected
(Softmax())withtheL2-normofnetworksasthelastFClayer, cumulativerewardafterdeterministicallyselectingtheactionac
t
resultinginanoutputrangefrom0to1. instatebc,comparedwiththeexpectedrewardforactiondrawn
t
(cid:2) Reward Function. At each time epoch t, the reward rc frompolicyπc.InPPO,theadvantagefunctioniscalculatedas
t θ
of an agent c is calculated after each action ac is taken to a function of Gc and baseline basec that has an impact on the
t t t
ensure that Ahaggar can learn from past experience. To do convergenceofGc.Priorwork[54]foundthatAπθ c didnotgener-
t
so,weadoptawell-knowstate-of-the-artrewardfunction[11], alizewell.Hence,inDPPO,werevisetheadvantagefunctionby
[27], [35], [50], [53] that linearly combines five metrics (2): usingatruncatedbackpropagationthroughtimewithawindow
perceptualquality(q
t
c(l
t
c)),rebufferingduration(rdc
t
)andcount of length κ such that Aπθ c (bc
t
,ac
t
)=Qπθ c (bc
t
,ac
t
)−Vπθ c (bc
t
).
(rcc
t
),qualityoscillations(qoc
t
)andswitches(qsc
t
). Qπθ c is calculated by the actor network, which uses the κ-step
r t c =ω 1 ×q t c(l t c)−ω 2 ×rdc t −ω 3 ×rcc t −ω 4 ×qoc t (cid:6) Tem κ κ = = p Θ 0 o − ra 1 l γ D κ i r f t c f + er κ en + ce γΘ (T V D ( ) bc t a + p Θ p ) r . oa F c o h re g a iv ch en ep b i y s : od Q e π , θ c th (b e c t a , g a e c t n ) t = c
−ω 5 ×qsc t , (2) A of π t θ c h , e w a h c e to re rn it e s tw am or p k le a s im a s tr t a o je m ct a o x r i y m o i f ze bi G tra c t t t e h d ro e u c g is h io m ns ax a i n m d iz u i s n e g s
whereqc(lc)mapstheselectedbitratetothequalityperceived the empirically computed advantage as an unbiased estimate
t t
(VMAF)[11],[53],qoc
t
=|q
t
c(l
t
c)−q
t
c
−1
(l
t
c
−1
)|,qsc
t
=qoc
t
/20, of Aπθ c (bc
t
,ac
t
). To alleviate overfitting issues, Ahaggar uses
and ω are the coefficients of the reward function. Herein, dropoutswithprobability(p=0.5)toaddaregularizationterm
i
following prior works [27], [50], we set qsc as the difference totheupdateoftheactornetwork.Thisregularizationrepresents
t
of20inVMAFvaluesoftwoconsecutivesegments.ThisQoE theentropyE =H(πc(.|bc))oftheprobabilitiesoverthebitrate
θ t
modelisdevelopedbasedonlinearregressionontwodatasets: decisions.Therefore,theparameterθ πc oftheactorisupdated
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:30:43 UTC from IEEE Xplore. Restrictions apply.

BENTALEBetal.:BITRATEADAPTATIONANDGUIDANCEWITHMETAREINFORCEMENTLEARNING 10383
viaastochasticgradientascentusing(5). Algorithm1:AhaggarDPPO(CentralAgent;Chief).
(cid:7)Tθ 1: forEachagentc∈{1,...,N}do
θ πc ←θ πc +α Aπ t θ c (bc t ,ac t )(cid:8) θ logπ θ c(ac t ,bc t )+βE, (5) 2: whilenotdonedo
t=1 3: WaituntilN gradientparametersforactor(θ
π
)and
whereT θ istheupdateinterval,αisthelearningrateandβ is critic(θ v )areavailable
theentropyparameterthatissettoalargevalueatthebeginning 4: Averagegradientsandupdateglobalθ π andθ v
ofthetrainingtoencourageexplorationanddecreasesovertime 5: Updatealltheworkerswithglobalθ π andθ v
toemphasizeimprovingrewards. 6: endwhile
TocalculatetheadvantageA(bc,ac)foragivenexperience, 7: endfor
t t
wehavetoestimatethevaluefunctionVπθ c (b).Thisestimation
is performed by the critic network that makes an objective
Algorithm2:AhaggarDPPO(Workers).
assessment for all the states ∀bc ∈B of an agent c during the
t 1: forEachagentc∈{1,...,N}do
training. To do so, the critic network uses the standard TD
method to compute the loss function and minimize its value.
2: whilenotdone(foreveryt=[1,...,T
πθ
c])do
The parameter θ vc of the critic network is updated through a
4
3:
:
fo
R
r
u
E
n
ac
p
h
ol
κ
ic
∈
yπ
{
c
0,.
a
.
n
.
d
,Θ
col
−
lec
1
t
}
s
d
{
o
bc,ac,rc}
stochasticgradientdescent(SGD)algorithmusing(6). θκ t t t
5: EstimatediscountedexpectedrewardGc
t
θ vc ←θ vc −α¯ (cid:7)Tθ (cid:8) θ (r t c+γVπθ c (bc t+1 ;θ vc)−Vπθ c (bc t ;θ vc)) 2, 6 7 : : E St s o ti r m e a p t a e rt a i d al va tr n a t j a e g c e to s r A y π t in θ c κ formation
t=1
(6) 8: endfor
where α¯ is the learning rate for the critic, Vπθ c (bc t ;θ vc) and 9: π θ c old ←π θ c
Vπθ c (bc
t+1
,θ vc) are the objective assessments for bc
t
and bc
t+1
, 10: ComputeLK
θκ
LPEN(θ)using(7)
respectively,fromthecriticnetwork. 11: ifKL[π θ c old |π θ c]>4KL target then
Finally, we update the policy π periodically every κ-steps 12: Breakandcontinuewithnexttimeepocht+1
θ
using PPO with constrained clipped objective (CCO) and the 13: endif
Adamoptimizer.Theconstraintrepresentshowmuchthepolicy 14: Compute(cid:8) θ LK θκ LPEN
isallowedtochange,expressedintermsoftheKullback-Leibler 15: Sendgradientactorparameters(θ πc)tochief
(KL)divergence(KL[π
θ
c
old
|π
θ
c]).Hence,theCCOisexpressed 16: Sendgradientcriticparameters(θ vc)tochief
as:θ κ+1 =argma (cid:8) x θ LK θκ LPEN(θ),where (cid:9) 1 1 7 8 : : W Up a d it a u te nt p i a l r p a a m ra e m te e rs te o rs f a w r o e r a k c e c r e c ptedordropped
LK θκ LPEN(θ)=E (cid:7)Tθ ratio t (θ)Aπ t θ c κ −β¯KL[π θ c old |π θ c] ,and, 2 1 0 9 : : if β K ¯ L ← [π α˜ θ c o β¯ ld |π θ c]>β¯ high KL target then
t=1 21: elseifKL[πc |πc]<β¯ KL then
(7) θold θ low target
E is the empirical expectation over time steps, ratio (θ) (= 22: β¯←β¯/α˜
t
πc(bc,ac)/ πc (bc,ac)) is the ratio of the probabilities under 23: endif
θ t t θold t t
thenewandoldpolicies,εisthecliphyperparameter(usually 24: endwhile
fixedto0.1)andβ¯istheKLpenaltyhyperparameter. 25: endfor
(cid:2)Multi-agentTrainingwithDPPO.Inthetraining,Ahag-
gar spawns MARL agents in parallel (Fig. 1). Each agent is
configuredtorunindependentlywithasharedenvironmentsuch if the actual change in the policy stays significantly below or
thatitexperiencesadifferentsetofinputstatesfromtheenvi- above the target KL, i.e., it falls outside the interval [β¯ ×
low
ronment.Here,theN agentscontinuallysendtheirparameters KL ,β¯ ×KL ].
target high target
θ toacentralagent(termedthechief),whichaggregates them (cid:2) Meta-Learned Policies for Training Algorithm. We adopt
to generate a single Ahaggar model. For each sequence of theMAMLapproach,whichallowslearningmodelparameters
parametersθthatitreceives,thechiefusestheA2Calgorithmto θ via meta-RL, i.e., finding the model parameters sensitive to
computeagradientbasedon(5)and(6).Then,thechiefupdates changes in the environment, allowing the Ahaggar model
the A2C networks and pushes out the new model to the agent to achieve fast adaptation to unseen environments during the
that sent the parameters. Such an update process can happen inferencephase.Thetrainingalgorithmconsistsoftwoloops:
synchronously or asynchronously among all agents, but we (1)InnerLoop.Foreachepisode,eachagentcfirstrandomly
foundthataveraginggradientsandapplyingthemsynchronously picksaspecificnetworkandcontenttraceastheenvironment,
leadstobetterresultsinthemeta-testingphase. andsampleX ∈Dtrajectories(alsoreferredtoasshots)where
ThepseudocodefortheDPPOusedbyAhaggarisprovided D ={(bc,ac);...;(bc,ac)} denotes the set of sampled tra-
1 1 k k
in Algorithm 1 for the chief and Algorithm 2 for the workers. jectories for inner loop in that environment according to the
Inthesealgorithms,thehyperparameterKL representsthe currentpolicyπc.TheAhaggarmeta-modelthenisoptimized
target θ
desiredchangesinthepolicypertimeepisode.Thescalingterm by the collected trajectories with the DPPO and Adam opti-
α˜ controls the adjustment of the KL-regularization coefficient mizer. In particular, we want to learn θ after a small number
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:30:43 UTC from IEEE Xplore. Restrictions apply.

10384 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.23,NO.11,NOVEMBER2024
| κ of | policy   | gradient | updates | on  | the data        | from an | environment |      |     |     |     |     |     |     |
| ---- | -------- | -------- | ------- | --- | --------------- | ------- | ----------- | ---- | --- | --- | --- | --- | --- | --- |
| Evt  | ∼p(Evts) | to       | obtain  | θi. | Here, i denotes | the     | index       | of a |     |     |     |     |     |     |
|      | i        |          |         | κ   |                 |         |             |      |     |     |     |     |     |     |
Evts.
| particular                                         |     | environment | in  | a batch | of environments |     |     | This  |     |     |     |     |     |     |
| -------------------------------------------------- | --- | ----------- | --- | ------- | --------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
| setofκupdatesiscalledinner-loopupdate.Theupdatedθi |     |             |     |         |                 |     |     | after |     |     |     |     |     |     |
κ
κ-stepondatafromEvt
|                         |     |                                  | i   | isgivenin(8).         |      |      |        |        |                   |     |     |     |     |     |
| ----------------------- | --- | -------------------------------- | --- | --------------------- | ---- | ---- | ------ | ------ | ----------------- | --- | --- | --- | --- | --- |
|                         |     | θi =θ−α(cid:8)                   |     | LDPPO(f               |      | ,D), |        | (8)    |                   |     |     |     |     |     |
|                         |     | κ                                |     | θ                     | Evti | θ    |        |        |                   |     |     |     |     |     |
| wheref                  |     | istheAhaggarmeta-modelandLDPPO(f |     |                       |      |      | )isthe |        |                   |     |     |     |     |     |
|                         | θ   |                                  |     |                       |      | Evti | θ      |        |                   |     |     |     |     |     |
| lossontheenvironmentEvt |     |                                  |     | afterκ-stepofupdates. |      |      |        |        |                   |     |     |     |     |     |
|                         |     |                                  |     | i                     |      |      |        | Fig.3. | DPPOversusothers. |     |     |     |     |     |
c
| (2) | Outer | Loop. | For each | episode, | each | agent | continually |     |     |     |     |     |     |     |
| --- | ----- | ----- | -------- | -------- | ---- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
samplesmanytrajectories(∈Di;thesetofsampledtrajectories
κ
for outer loop) from the randomized environments via meta- whilesatisfyingaKL-Divergenceconstraintonhowclose
| policy                                                   | π c | of meta-model |     | f    | and calculates | gradients |     | for θ |                                     |     |     |     |     |     |
| -------------------------------------------------------- | --- | ------------- | --- | ---- | -------------- | --------- | --- | ----- | ----------------------------------- | --- | --- | --- | --- | --- |
|                                                          | θ i |               |     | θκ i |                |           |     |       | thenewandoldpoliciesareallowedtobe. |     |     |     |     |     |
| withthetrajectory.Afterthat,theseagentssendthecalculated | κ   |               |     |      |                |           |     |       | (cid:2)                             |     |     |     |     |     |
DDPGisanoff-policyalgorithmthatcombinesDQNand
| gradients |     | to the chief, | which | in  | turn merges | them | via agents’ |     |     |     |     |     |     |     |
| --------- | --- | ------------- | ----- | --- | ----------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
actor-criticalgorithmstousedeterministicpolicygradients
lossfunctionsandtheouterloop’slearningrateβ.Formally,we
forupdatingthepolicyviaaDLapproach.
|     |     |     |     |     | (cid:6) | T c |     |     | (cid:2) |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
meta-objective (L (θ)) π θ LS G D (f i). SAC is an off-policy algorithm that combines stochastic
| define                                                  | a   |     |     | meta | as  | t= 1 | θκ  | The |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| optimizationofLiscalledtheouter-loopupdate.Theresulting |     |     |     |      |     | E vt | i   |     |     |     |     |     |     |     |
policyoptimizationandDDPG-styleapproaches.Itincor-
updateforθisgivenby(9). poratestheclippeddouble-Qtrickandentropyregulariza-
tion.
(cid:2)
(cid:7)Tπ c
|     |     |               |     | θ   |           |        |     |     | TD3isanoff-policyalgorithmthatintroducesclippeddou- |     |     |     |     |     |
| --- | --- | ------------- | --- | --- | --------- | ------ | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- |
|     |     | θ =θ−β(cid:8) |     |     | LS G D (f | ,D i), |     |     |                                                     |     |     |     |     |     |
|     |     |               |     | θ   |           | i      |     | (9) | bleQ-learningmodeandadelayedpolicyupdatestrategy    |     |     |     |     |     |
|     |     |               |     |     | E vt i    | θκ κ   |     |     |                                                     |     |     |     |     |     |
t=1
(cid:2) tosolvetheoverestimationproblemofDDPG.
wheretheupdateisperformedusingSGD,β isalearningrate Randomisanalgorithmthatchoosesanactionrandomly.
andLSGD denotesthelossontheenvironmentEvt TocomparetheperformanceofAhaggarwithDPPOagainst
i .
Evti
otherpolicyupdatetechniques,weprepared10%asavalidation
AhaggarMeta-Testing(Online) setfromthe20%ofthetestingsetcomprisingnetworkandvideo
C.
contenttraces.WeimplementedthesetechniquesinAhaggar
TheobjectiveofAhaggaristolearnhowtoadapttohetero-
|     |     |     |     |     |     |     |     | and | then | ran the experiment |     | with 1,000 | agents | on the same |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------------ | --- | ---------- | ------ | ----------- |
geneousnetworkenvironmentsduringtheonlinephasethrough
|     |     |     |     |     |     |     |     | validation |     | set every 500 | episodes | and | recorded | the validation |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------- | -------- | --- | -------- | -------------- |
continuallearningenabledbyMAML.Duringthemeta-testing
learningcurveinFig.3.WecanseethatDPPOachievesthebest
phase,weuseourHAS-basedstreamingsystem(Fig.2),which
|     |     |     |     |     |     |     |     | performance |     | with (i) | the highest | possible | N-QoElin | (reward; |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | ----------- | -------- | -------- | -------- |
consistsofCMCD/SD-awareDASHclientsrunninginDocker
|     |     |     |     |     |     |     |     | see | Section | V-B4) and | (ii) trains | and | converges | faster to the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ----------- | --- | --------- | ------------- |
instancesandaCMCD/SD-awareNode.jsserverwithanHTTP
highestrewardvaluewithonly3,000episodes,comparedtoits
serverandanNJSapplication.NJSiswritteninJavaScriptand
competitors.DPPOreliesonspecializedclippingintheobjective
extendstheNode.jsconfigurationsyntaxtoimplementAhag-
|       |         |          |           |     |                   |     |      | function |     | (7) to remove | incentives | for the | new | policy to get far |
| ----- | ------- | -------- | --------- | --- | ----------------- | --- | ---- | -------- | --- | ------------- | ---------- | ------- | --- | ----------------- |
| gar’s | bitrate | guidance | functions |     | and communication |     | with | the      |     |               |            |         |     |                   |
fromtheoldpolicy.Hence,itallowsrobustpolicyoptimization
dash.jsclients.Atruntime,foreachclient,theAhaggarmeta-
modelusesaJSONfilethatstoresthemodelmeta-parameters(θ for whole video sessions. Comparing DPPO with TRPO, we
observethatTRPOistherunner-upthattypicallyobtainsahigh
andθi)andtrajectories(DandDi)learnedandcapturedevery
κ κ reward, butittakes more time(6,000 episodes) to converge to
40shotsduringtheofflinephase.
thebestachievablereward.Withthisresult,wefindDPPOisthe
bestfitforAhaggaroutofexistingpolicyupdatetechniques.
|             |     | IV. | AhaggarDESIGNCHOICES |     |     |     |     |     |          |     |     |     |     |     |
| ----------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
| A. WhyDPPO? |     |     |                      |     |     |     |     | B.  | WhyMAML? |     |     |     |     |     |
In Ahaggar, we used DPPO [25] as a policy update tech- We compare the performance of Ahaggar with MAML
nique. Here, we show the central insight of selecting DPPO against Ahaggar with different well-known meta-RL ap-
compared to popular vanilla DRL-based policy update tech- proaches[26]:PEARL,RL2,REPTILE,ANIL,andIMPALA.
(cid:2)
niques [6], [21] such as asynchronous advantage actor-critic PEARLusestheSACpolicyformeta-trainingandadapts
(A3C), trust region policy optimization (TRPO), deep deter- tonewenvironmentsbyperforminginferenceoveralatent
ministic policy gradient (DDPG), soft actor-critic (SAC),twin (cid:2) contextvariableonwhichthepolicyisconditioned.
delayedDDPG(TD3)andRandom. RL2 tries to structure the RL agent as a recurrent neural
(cid:2)
A3Cisanon-policyalgorithmthatextendsactor-criticto network(RNN),whichreceivesobservations,pastrewards,
asynchronousandparallellearning,disturbsthecorrelation and actions, and retains its state across episodes in a
betweendata,andimprovestrainingspeed. givenenvironment.Particularly,RL2isencodedinsidethe
(cid:2)
TRPO is an on-policy algorithm that updates policies by weights of an RNN, which are learned slowly through a
taking the largest step possible to improve performance vanillaoff-policyRLalgorithm.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:30:43 UTC from IEEE Xplore.  Restrictions apply.

BENTALEBetal.:BITRATEADAPTATIONANDGUIDANCEWITHMETAREINFORCEMENTLEARNING 10385
Fig.4. MAMLversusothers. Fig.5. Ahaggarconvergence.
(cid:2) TABLEI
REPTILEworksbyrepeatedlysamplinganenvironment, MODELCONVERGENCE/GENERALIZATIONFORDIFFERENTSOLUTIONSTIME
performingstochasticgradientdescentonit,andupdating
theinitialparameterstowardsthefinalparameterslearned
onthatenvironment.
(cid:2)
ANILisasimplifiedversionofMAMLthatremovesthe
inner-loop updates for all but the head (final layer) of a
neuralnetworkduringtrainingandinference.
(cid:2)
IMPALA introduces a highly scalable distributed agent
coupled with a new off-policy learning algorithm termed
V-trace.V-traceisageneraloff-policylearningalgorithm compared to X =80, X =60 and X =40, respectively. One
morestableandrobustthanotheroff-policytechniquesfor interesting observation is that Ahaggar with X =40 (40-
actor-criticagents. shots) is the best trade-off point, allowing good sampling ef-
We run the same experiment outlined in Section IV-A and ficiencyandconvergencetoitsbestgeneralizationperformance
themeta-validationlearningcurveforthisexperimentisshown (highestachievableN-QoElin)muchfaster(comparableto2,500
in Fig. 4. With 3,000 episodes, we observe that MAML out- episodes) within 3,000 episodes, and significant reduction in
performs existing meta-RL approaches in terms of N-QoElin computation cost overhead for both Ahaggar meta-training
withanaverageimprovementof57.5%(PEARL:64.4%,RL2: and meta-testing phases compared to X =100, X =80, or
65.3%, REPTILE: 79.9%, ANIL: 28.7%, IMPALA: 49.11%). X =60.Therefore,wesetX=40duringthemeta-trainingand
It also converges quickly to the best reward, requiring 3,000 meta-testing (and meta-validation) phases. More notably, with
episodes,2xbetterthantherunner-upapproach(ANIL),which X =1 or X =20, the convergence was very slow (requiring
shows the effectiveness of MAML in the meta-training phase. moreepisodes)comparedtoX >20-shots.
ANILgenerallyperformsbetterthanRL2,IMPALA,REPTILE
andPEARL,asitisanextensionofMAMLwithoutinner-loop D. AhaggarModelConvergence
updates.However,theyall,includingANIL,requiremoretrain-
We trained each model on a physical workstation machine
ingtimeandepisodestoconverge.REPTILEfailstoconverge
with dual 20-core Intel E5-2630 v4 @ 2.20GHz processors,
andstrugglestoadapt/generalizetodifferentenvironments.To
192 GBmemory, and 8GPUs.TableIshows theconvergence
sumup,thisresultsuggeststheeffectivenessofMAMLagainst
time,episodesandshotsrequiredforamodeltogeneralizeand
itsbaselines.
converge tothebestsolution.Wefixedthenumberofshotsto
40andworkersto1,000forallmeta-RLtechniques,including
C. NumberofShotsandLearningEpisodes
Ahaggar,ANIL,PEARL,andRL2.Duringthetraining(80%
AlthoughconsideringmoretrajectoriesX(orshots)resultsin datasets),Ahaggarisabletoconvergefasterandachievethe
increasedimprovementinsamplingefficiency,itgeneratesmore best performance with 3,000 episodes (with 2,000 iterations
computationcostoverhead,whichcanhindertheperformance perepisode),takingeighthoursoftraining,comparedtoother
of the trained model and its generalization during inference. solutions.Itrequires2x(2x),4x(3x),5x(5x),7x(9x),and10x
A good solution should make a trade-off between sampling (12x) fewer episodes (time) to achieve its best generalization
efficiency, model generalization/convergence and computation performance compared to ANIL, IMPALA, RL2, Fugu and
costoverhead.TofindthebestvalueforX thatleadstofaster Pensive,respectively.Similarly,inmeta-testing(20%datasets),
convergence and minimizes the computation cost overhead, Ahaggargeneralizeswellandconvergeswithinonly40-shots
we ran an experiment for Ahaggar with various shot values (e.g., equal to watching 40 video sessions). In contrast, other
X ={1,20,40,60,80,100}. We used the same validation set techniquesrequiremoreshotstoadapttovariousenvironments.
andsetupasaboveSectionIV-A.Themeta-validationlearning For example, ANIL and PEAR require 100-shots and 150-
curve for Ahaggar with various shot values is highlighted in shots,respectively.ThisisananticipatedresultfromAhaggar
Fig. 5. We observe that Ahaggar with X =100 converges because of DPPO multi-agent work distribution and MAML
to the best N-QoElin with fewer episodes of 2,500. However, fastadaptationcapabilities.Morenotably,duringtheinference,
it generates 2x, 4x, and 8x more computation cost overhead Ahaggartakesonlyafewmillisecondstoperformthebitrate
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:30:43 UTC from IEEE Xplore. Restrictions apply.

10386 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.23,NO.11,NOVEMBER2024
|     |     |     | TABLEII |     |     |     | B.  | MethodologyandEvaluationSetup |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
AhaggarTRAINING/TESTINGPARAMETERS
|     |     |     |     |     |     |     | 1)  | VideoSampleandParameters: |         |      |      | TheHTTPserverhosted |      |              |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | ------- | ---- | ---- | ------------------- | ---- | ------------ | --- |
|     |     |     |     |     |     |     | the | 4K DASH                   | dataset | [41] | that | was not             | used | in training. | We  |
encodedthe636secondslongBigBuckBunny(BBB)intofour-
|     |     |     |     |     |     |     | second | segments | in                    | FFmpeg | using     | the H.264       |     | codec at      | 30 fps |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --------------------- | ------ | --------- | --------------- | --- | ------------- | ------ |
|     |     |     |     |     |     |     | and    | in 13    | bitrates/resolutions. |        | Further   | characteristics |     |               | of BBB |
|     |     |     |     |     |     |     | are    | given    | in supplementary      |        | materials | (Appendix       |     | B), available |        |
online.
|     |     |     |     |     |     |     | 2)       | Network  | Traces:     | We       | used      | network | traces    | with different |         |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ----------- | -------- | --------- | ------- | --------- | -------------- | ------- |
|     |     |     |     |     |     |     | user     | mobility | (bus,       | walking, | car,      | train,  | bicycle,  | tram,          | ferry   |
|     |     |     |     |     |     |     | and      | driving) | to throttle | the      | bandwidth | between |           | the server     | and     |
|     |     |     |     |     |     |     | clients. | These    | traces      | were     | extracted | from    | the 20%   | of             | network |
|     |     |     |     |     |     |     | datasets | for      | testing     | (Belgium | 4G/LTE    |         | [51], NYU | LTE            | [36],   |
Lumous4G/5G[39]).Werandomlyextractedsixnetworktraces
|          |            |         |         |             |     |              | from | each      | dataset where | the | inter-variation |               | duration | between |       |
| -------- | ---------- | ------- | ------- | ----------- | --- | ------------ | ---- | --------- | ------------- | --- | --------------- | ------------- | -------- | ------- | ----- |
| guidance | decisions. | Another | notable | observation |     | is that Fugu |      |           |               |     |                 |               |          |         |       |
|          |            |         |         |             |     |              | the  | bandwidth | values        | was | fixed to        | five seconds. |          | Further | char- |
andPensievedonotleveragemeta-learningtechniques.Thus,it acteristics of the traces are given in supplementary materials
takeslongerforthemtoconverge.
(AppendixA),availableonline.
|     |     |     |     |     |     |     | 3)   | ABRSchemes:         |     | WecomparedAhaggaragainstheuristics |       |              |     |        |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------------------- | --- | ---------------------------------- | ----- | ------------ | --- | ------ | --- |
|     |     |     |     |     |     |     | such | as throughput-based |     |                                    | (TH), | buffer-based |     | (BOLA) | and |
V. PERFORMANCEEVALUATION
Dynamic(TH+BOLA)fromdash.js[20]andRobustMPC[53]
A. AhaggarImplementation and one learning-based scheme: Pensieve [35]. The
heuristic-basedschemesweretunedandPensievewasretrained
| 1) Choice | of  | Ahaggar | Parameters: | To  | train | the Ahag- |     |     |     |     |     |     |     |     |     |
| --------- | --- | ------- | ----------- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
withourdatasetsandQoEmetricstofiteachexperiment.
| gar model, | we       | used | a total of | 2000 traces | (1500     | network |     |                     |     |     |                            |     |     |     |     |
| ---------- | -------- | ---- | ---------- | ----------- | --------- | ------- | --- | ------------------- | --- | --- | -------------------------- | --- | --- | --- | --- |
|            |          |      |            |             |           |         | 4)  | PerformanceMetrics: |     |     | WetestedtheABRschemesusing |     |     |     |     |
| and 500    | content) | from | different  | datasets as | described | in Sec- |     |                     |     |     |                            |     |     |     |     |
twomainQoEmodels:LinearQoE[50]andITUP.1203QoE
tionIII-B.Werandomizedthemandthenused80%fortraining
(Mode0)[44].Foreverysession,wecomputedtheaccumulated
| and 20% | for testing. | With | an 80–20 | train-test | split, | we per- |     |     |     |     |     |     |     |     |     |
| ------- | ------------ | ---- | -------- | ---------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
QoElin
usingalinearfunctionasfollows:
formeda5-foldwalk-forwardcross-validationoneachdataset.
Training parameters can impact the performance of Ahag- (cid:7)k (cid:7)k (cid:7)k (cid:7)k
gar, so we empirically set the parameters as summarized in ω q c(l c)−ω rdc −ω rcc −ω qoc −ω qsc ,
|          |     |     |     |     |     |     | 1   |     | 2   |     | 3   | 4   |     | 5   |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|          |     |     |     |     |     |     |     | t   | t   | t   |     | t   |     | t   | t   |
| TableII. |     |     |     |     |     |     |     | t=1 | t=1 |     |     |     | t=2 |     | t=2 |
2) Offline Training: To train the Ahaggar meta-model, (cid:6) (10)
|     |     |     |     |     |     |     | where |     | k q c(l c) | is the | accumulative |     | perceived | perceptual |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ---------- | ------ | ------------ | --- | --------- | ---------- | --- |
we used a customized trace-based segment-level Gym simu- (cid:6) t=1 t t
|     |     |     |     |     |     |     |     |     | k rdc |     |     | feringduration(RD),rcc |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ---------------------- | --- | --- | --- |
lator based on Park [34]. This simulator was implemented in quality, t=1 isthetotalrebuf (cid:6) is
|     |     |     |     |     |     |     |     |     | t   |     |     |     |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Python 3.6 to simulate a typical HAS system based on real- the total rebuffering count (RC), k qoc is the cumulative
|     |     |     |     |     |     |     |     |     |     | (cid:6) |     | t=2 | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
worldnetworkandcontenttraces.WeusedTFLearn1.5.0[48], quality oscillations, k qsc is the total number of quality
|     |     |     |     |     |     |     |     |     |     | t=2 | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
RLlib of Ray 1.12.0 [32] and TensorFlow 2.4.0 to implement switches,andkisthetotalnumberofsegments.Thecoefficients
| Ahaggar’sNNarchitectureandbuildthetrainingworkflow. |     |     |     |     |     |     | ω   |           |           |         |     |          |     |              |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------- | --- | -------- | --- | ------------ | --- |
|                                                     |     |     |     |     |     |     | of  | 1,2,3,4,5 | are given | in (2). | To  | simplify | the | presentation | of  |
3) Online Testing: To test Ahaggar, we implemented a theQoE,weusedanormalizedQoElin(N-QoElin)withvalues
CMCD/SD-enabledstreamingsystem[2]withAhaggar’sbi-
|     |     |     |     |     |     |     | between | 0   | and 1. To | achieve | that, | we used | the | best achievable |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --------- | ------- | ----- | ------- | --- | --------------- | --- |
trateguidance f unc t ions.We(i)addednewCMCDparameters QoE (QoE(cid:2)) in each session such that N-QoElin = QoElin /
− → − →
(qt,dt,rs,ls,QT,LS) to support Ahaggar design, and (ii) QoE(cid:2).TheITUP.1203QoEmodelinMode0(O.46)takesfour
usedthemb=l(maximumsuggestedbitrate)CMSD-Dynamic
|     |     |     |     |     |     |     | metrics | as  | input: bitrate, | rebuffering |     | duration, |     | frame | rate and |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --------------- | ----------- | --- | --------- | --- | ----- | -------- |
parametertoconveyAhaggar’sbitrateguidancetoeachcor- content resolution. How to compute the QoEitu is described
responding client. On the server side, we used TensorFlow.js in [44]. This model outputs QoE values in the range of one to
converter[45]toconvertandloadapre-trainedmeta-modelinto five (MOS) and we normalized them (N-QoEitu) to [0,1]. In
a JavaScript Web-based application and run inference through addition, we computed (i) the total downloaded (TD) size (in
TensorFlow.js. On the client side, we implemented a simple MB) metric to measure how much bandwidth was consumed
heuristic as our ABR scheme, which used Ahaggar bitrate during the session, (ii) percentage of the HD (pHD) segments
guidancedecisionstoperformrateadaptation.Tosimplifyinput rendered at 720p or higher, and (iii) percentage of the UHD
statedatacollection,weappendedthemanifestfilesbyadding (pUHD)segmentsrenderedat2160p.
fourtags:size,phone,hdtvanduhdtv.Thesetagsrepresentthe 5) Evaluation Setup and Scenarios: Our setup consisted of
segmentsizesandVMAFscoresforphone,HDTVandUHDTV, onephysicalmachinerunningUbuntu18.04.6LTS,AMDRyzen
respectively.TheVMAFscoreswerecomputedusingdifferent 7 3700X 8-Core CPU and 32 GB memory. We ran a Docker
VMAFmodelsdependingonthedeviceresolution.Weprovide container for each client,inwhich weranaCMCD/SD-aware
asamplemanifestfilein[2]. dash.js(v4.2.1)clientonaGoogleChromebrowser(v103)with
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:30:43 UTC from IEEE Xplore.  Restrictions apply.

BENTALEBetal.:BITRATEADAPTATIONANDGUIDANCEWITHMETAREINFORCEMENTLEARNING 10387
TABLEIII
AVERAGERESULTSOFTHEQOEANDITSMETRICSFORDIFFERENTNETWORKTRACESFORSCENARIOA1
headlessmodeenabledusingPuppeteer(https://pptr.dev/).The Detailsofthenetworktracesusedineachscenarioaregiven
maximumplaybackbufferlevelwaskeptatthedefaultvalueof insupplementarymaterials(AppendixA),availableonline.
| 20 seconds. | For | network | emulation, | we  | used | tc NetEm | (https: |     |     |     |     |     |     |     |     |
| ----------- | --- | ------- | ---------- | --- | ---- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
//man7.org/linux/man-pages/man8/tc-netem.8.html)tothrottle C. ResultsforMultipleIdenticalClients(ScenarioA1)
| the total | bandwidth | available |     | to the | clients | according | to the |          |     |         |     |              |     |       |          |
| --------- | --------- | --------- | --- | ------ | ------- | --------- | ------ | -------- | --- | ------- | --- | ------------ | --- | ----- | -------- |
|           |           |           |     |        |         |           |        | For each | ABR | scheme, | we  | ran multiple |     | UHDTV | clients. |
networktracesdescribedinSectionV-B2.Weadoptedtwotypes
|     |     |     |     |     |     |     |     | Table IIIshows |     | thetotalQoE |     | and detailed | breakdown |     | ofeach |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | --- | ------------ | --------- | --- | ------ |
ofnetworkemulations:(i)inserver-sidenetworkemulation,the
throttlingisdoneontheserverportsothatallsessionssharea QoE metric for each ABR scheme for various network traces.
|     |     |     |     |     |     |     |     | We provide | the | average | and standard |     | deviation | values | for six |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | ------------ | --- | --------- | ------ | ------- |
singlenetworktrace,and(ii)inclient-sidenetworkemulation,
|                       |     |             |        |          |        |           |          | clients and | over    | five runs | in  | the format    | of average | ±           | std. In |
| --------------------- | --- | ----------- | ------ | -------- | ------ | --------- | -------- | ----------- | ------- | --------- | --- | ------------- | ---------- | ----------- | ------- |
| the throttling        | is  | done within | each   | client’s | Docker | container | so       |             |         |           |     |               |            |             |         |
|                       |     |             |        |          |        |           |          | general,    | Ahaggar | gained    | the | best possible |            | performance | in      |
| that session-specific |     | network     | traces | are      | used   | for each  | session. |             |         |           |     |               |            |             |         |
termsofRC,RDandTDwithoutsacrificingtheVMAFscore
WeevaluatedAhaggarindifferentmulti-clientscenarioswith
|     |     |     |     |     |     |     |     | compared | to other | baselines | in  | all network | traces. | Looking | at  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --------- | --- | ----------- | ------- | ------- | --- |
sixclientsineachscenarioassummarizedbelow:
(cid:2)
|     |     |     |     |     |     |     |     | theaverages | across | allthenetwork |     | traces,weseethatAhag- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------------- | --- | --------------------- | --- | --- | --- |
ScenarioA1:ThesixclientsareidenticalUHDTVclients.
|      |          |           |     |                 |     |     |         | gar reduced |          | average | RD by       | 62.81% | (84.36%), | average   | RC  |
| ---- | -------- | --------- | --- | --------------- | --- | --- | ------- | ----------- | -------- | ------- | ----------- | ------ | --------- | --------- | --- |
| This | scenario | evaluates |     | the performance |     | of  | Ahaggar |             |          |         |             |        |           |           |     |
|      |          |           |     |                 |     |     |         | by 53.52%   | (71.18%) |         | and average | TD     | by 53.27% | (59.34%), |     |
againsttheotherABRschemes.Client-sidenetworkemu-
comparedtotheheuristic-based(learning-based)ABRschemes.
lationisused.
(cid:2) Inaddition,Ahaggarsignificantlyreducedthenumberoftimes
| Scenario     |     | B1: The | six clients | contain |     | a mix | of device |       |         |     |        |            |     |               |     |
| ------------ | --- | ------- | ----------- | ------- | --- | ----- | --------- | ----- | ------- | --- | ------ | ---------- | --- | ------------- | --- |
|              |     |         |             |         |     |       |           | a UHD | segment | was | picked | when there | was | no noticeable |     |
| resolutions, |     | namely, | two         | UHDTV,  | two | HDTV, | and two   |       |         |     |        |            |     |               |     |
VMAFscoredifferencecomparedtotheotherbest-performing
| phone | clients. | This        | scenario | evaluates    |        | the effectiveness |     |                                                     |     |     |     |     |     |     |     |
| ----- | -------- | ----------- | -------- | ------------ | ------ | ----------------- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|       | Ahaggar  |             |          |              |        |                   |     | schemes(RobustMPCandDynamic)acrossallnetworktraces. |     |     |     |     |     |     |     |
| of    |          | in adapting |          | to different | device | resolutions.      |     |                                                     |     |     |     |     |     |     |     |
Suchreductiontranslatestosignificantbandwidthsavings(see
Client-sidenetworkemulationisused.
| (cid:2) |     |     |     |     |     |     |     | theAvg.TDcolumninTableIII). |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
ScenarioA2:ArepeatofScenarioA1exceptthatserver-
WeanticipatedtheseresultsbecauseAhaggarmakesbitrate
sidenetworkemulationisused.
(cid:2) guidance decisions based on not only the throughput, buffer
ScenarioB2:ArepeatofScenarioB1exceptthatserver-
|     |     |     |     |     |     |     |     | level and | segment | sizes, | but | also segment | quality | and | device |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------ | --- | ------------ | ------- | --- | ------ |
(cid:2) sidenetworkemulationisused.
|     |     |     |     |     |     |     |     | resolution. | It also | uses | MAML | for continual |     | learning | and fast |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ---- | ---- | ------------- | --- | -------- | -------- |
ScenarioC:ThesixclientscontainamixofABRschemes:
|     |     |     |     |     |     |     |     | adaptation | to  | unseen | environments. | In  | contrast, | other | ABR |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | ------------- | --- | --------- | ----- | --- |
threeDynamicandthreeAhaggarclients.Thisscenario
schemesuseoneormoreheuristicsoranNNcombiningthese
| evaluates |     | the impact   | of  | introducing |          | Ahaggar | clients     |            |     |         |                 |     |         |         |        |
| --------- | --- | ------------ | --- | ----------- | -------- | ------- | ----------- | ---------- | --- | ------- | --------------- | --- | ------- | ------- | ------ |
|           |     |              |     |             |          |         |             | heuristics | and | they do | not necessarily |     | perform | well in | unseen |
| amongst   |     | clients that | do  | not use     | Ahaggar. |         | Client-side |            |     |         |                 |     |         |         |        |
networkemulationisused. environments. Fig. 6 and Table III confirm this. For instance,
|     |     |     |     |     |     |     |     | Pensieve | achieved | the | highest | average | selected | bitrate | and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | ------- | ------- | -------- | ------- | --- |
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:30:43 UTC from IEEE Xplore.  Restrictions apply.

10388 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.23,NO.11,NOVEMBER2024
TABLEIV
AVERAGEQOEitu(O.46)SCORESANDITSMETRICSPRODUCEDBYAhaggar
RUNNINGONDEVICESWITHDIFFERENTRESOLUTIONSFORSCENARIOB1
Avg.QoEitu
| Fig.6. |     | (O.46)andavg.rebufferingdurationratioinvarious |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------ | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
networktracesforScenarioA1.Thebottom(left)edge,markandtop(right)
edgeindicatetheaverage−std,averageandaverage+std,respectively,with
and36.86%(heuristic-based:33.70%,learning-based:49.49%)
a95%confidenceinterval.
|     |     |     |     |     |     |     |     | across all   | network | traces, | respectively. |     | It     | also achieved | higher      |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ------- | ------------- | --- | ------ | ------------- | ----------- |
|     |     |     |     |     |     |     |     | O.35 (Visual | Quality |         | Score,        | not | shown) | scores        | with values |
rangingbetween4.60and4.94.Theseresultsconfirmhowwell
averagepUHD,butitperformedpoorlyinmostothermetrics.In
AhaggarperformstobalancetheQoEitumetrics.Second,the
thesamecontext,BOLAfailedtodelivergoodvideoqualitywith
Belgium4G/LTEdatasethasthelowestbandwidthvaluesinits
inferiorVMAFscores,andRobustMPCsufferedfromfrequent
networktraces.Therefore,allABRschemesachievedthelowest
andlongrebufferingevents.
|                 |         |          |             |          |         |         |             | scores in | terms       | of O.23,      | O.35     | and       | O.46.   | Nonetheless, | since       |
| --------------- | ------- | -------- | ----------- | -------- | ------- | ------- | ----------- | --------- | ----------- | ------------- | -------- | --------- | ------- | ------------ | ----------- |
| Similarly,      | Ahaggar |          | achieved    | the      | highest | average | QoEitu      |           |             |               |          |           |         |              |             |
|                 |         |          |             |          |         |         |             | Ahaggar   | has         | been designed |          | to adapt  | quickly | to           | challenging |
| and lowest      | average |          | rebuffering | duration |         | (see    | Fig. 6). In |           |             |               |          |           |         |              |             |
|                 |         |          |             |          |         |         |             | network   | conditions  | (thanks       |          | to MAML), |         | it was able  | to obtain   |
| detail, Ahaggar |         | achieved | the         | highest  | average | QoE     | with an     |           |             |               |          |           |         |              |             |
|                 |         |          |             |          |         |         |             | the best  | O.23 (2.37) |               | and O.46 | (2.70)    | scores. | Although     | other       |
| improvement     | of      | [Lumous  | 4G          | Fig.     | 6(a):   | 22.28%  | (44.73%),   |           |             |               |          |           |         |              |             |
baselinesachievedacomparableO.35score(notshown),they
| Belgium | 4G/LTE | Fig. | 6(b): 49.49% |     | (37.06%), | NYU | LTE Fig. |                |     |      |             |     |        |        |              |
| ------- | ------ | ---- | ------------ | --- | --------- | --- | -------- | -------------- | --- | ---- | ----------- | --- | ------ | ------ | ------------ |
|         |        |      |              |     |           |     |          | faced frequent | and | long | rebuffering |     | events | due to | their greedy |
6(c):55.04%(85.08%),Lumous5GFig.6(d):8.01%(31.10%)]
|            |          |             |     |          |         |             |     | bitrate selection |                 | strategy. | Third,  | Dynamic |       | was the | runner-up, |
| ---------- | -------- | ----------- | --- | -------- | ------- | ----------- | --- | ----------------- | --------------- | --------- | ------- | ------- | ----- | ------- | ---------- |
| and lowest | average  | rebuffering |     | duration | with    | a reduction | of  |                   |                 |           |         |         |       |         |            |
|            |          |             |     |          |         |             |     | receiving         | the second-best |           | results | in      | terms | of O.23 | and O.46.  |
| 62.81%     | (84.36%) | across      | all | network  | traces, | compared    |     | to                |                 |           |         |         |       |         |            |
Unexpectedly,PensievefailedtoproducegoodABRdecisions,
| heuristic-based |         | (learning-based) |             | ABR             | schemes.  | Compared |            | to          |             |             |          |        |      |             |         |
| --------------- | ------- | ---------------- | ----------- | --------------- | --------- | -------- | ---------- | ----------- | ----------- | ----------- | -------- | ------ | ---- | ----------- | ------- |
|                 |         |                  |             |                 |           |          |            | leading     | to multiple | rebuffering |          | events | that | contributed | to the  |
| Ahaggar,        | Dynamic | achieved         |             | the second-best |           | average  | results    |             |             |             |          |        |      |             |         |
|                 |         |                  |             |                 |           |          |            | lowest O.23 | score,      | which       | impacted |        | O.46 | negatively  | in most |
| in terms        | of the  | QoE and          | rebuffering |                 | duration. | This     | is because |             |             |             |          |        |      |             |         |
networktraces.
oftheDynamicdesignthatcombinesthebenefitsofBOLAand
WealsoconductedacomparisonbetweenQoEituandQoElin.
THbyswitchingbetweenbothinruntimebasedonthestability
|                |     |        |        |          |           |          |     | We first | normalized | both      | values | (Section |     | V-B4) and   | the com- |
| -------------- | --- | ------ | ------ | -------- | --------- | -------- | --- | -------- | ---------- | --------- | ------ | -------- | --- | ----------- | -------- |
| of the current |     | buffer | level. | However, | Pensieve, | followed | by  |          |            |           |        |          |     |             |          |
|                |     |        |        |          |           |          |     | parison  | between    | different | ABR    | schemes  |     | for various | network  |
RobustMPC,sufferedfromlowQoEandlongRDduetowrong
tracesislistedinthelastcolumnofTableIII.Ineachnetwork
| ABR decisions. |     | It is worth | mentioning |     | that | all schemes | faced |     |     |     |     |     |     |     |     |
| -------------- | --- | ----------- | ---------- | --- | ---- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
trace,Ahaggarachievedthehighestandmostconsistentper-
| a few rebuffering |     | events  | in            | Lumous | 5G           | because | sometimes  |          |          |     |          |     |          |       |        |
| ----------------- | --- | ------- | ------------- | ------ | ------------ | ------- | ---------- | -------- | -------- | --- | -------- | --- | -------- | ----- | ------ |
|                   |     |         |               |        |              |         |            |          |          |     | N-QoEitu |     | N-QoElin |       |        |
|                   |     |         |               |        |              |         |            | formance | in terms | of  |          | and |          | (only | in NYU |
| the bandwidth     |     | dropped | significantly |        | and suddenly |         | (caused by |          |          |     |          |     |          |       |        |
LTE,THandDynamicwereslightlybetter)comparedtoother
thehandoffsto4G).Thisisabehaviorknownin5Gnetworks
|     |     |     |     |     |     |     |     | ABR schemes. |     | We can | see | that the | N-QoEitu | and | N-QoElin |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | --- | -------- | -------- | --- | -------- |
operatinginhigherfrequencies[39].
|               |     |     |        |       |       |          |          | are almost | identical | for | each | dataset, | and | thus, | can be used |
| ------------- | --- | --- | ------ | ----- | ----- | -------- | -------- | ---------- | --------- | --- | ---- | -------- | --- | ----- | ----------- |
| To understand |     | how | QoEitu | (Mode | 0) is | computed | for each |            |           |     |      |          |     |       |             |
interchangeablyinpractice.
| session,   | Table  | III (the  | eighth  | and ninth | columns) |           | highlights |     |     |     |     |     |     |     |     |
| ---------- | ------ | --------- | ------- | --------- | -------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| the scores | of its | essential | metrics | (O.23:    |          | Rebuffing | Duration   |     |     |     |     |     |     |     |     |
D. ResultsforMultipleMixed-DeviceClients(ScenarioB1)
| Score and | O.46: | Overall | Score) | for | different | ABR | schemes. |     |     |     |     |     |     |     |     |
| --------- | ----- | ------- | ------ | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
The score of each metric is given in the MOS range of one to To evaluate the effectiveness of Ahaggar in adapting to
five.Here,wededucethreeimportantthrusts.First,Ahaggar differentdeviceresolutions(DR),werantwoclientswitheach
outperformed the baselines, achieving the best O.23 and O.46 DR(atotalofsix).TableIVhighlightstheresultsoverfiveruns.
ThekeytakeawayisthatAhaggarachieveddifferentaverage
| scores for | all | network | traces | with | an average | improvement |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ------- | ------ | ---- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of 67.55% (heuristic-based: 60.75%, learning-based: 94.75%) results for each DR, confirming Ahaggar’s DR awareness.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:30:43 UTC from IEEE Xplore.  Restrictions apply.

BENTALEBetal.:BITRATEADAPTATIONANDGUIDANCEWITHMETAREINFORCEMENTLEARNING 10389
TABLEV
AVERAGERESULTSOFTHEQOEANDITSMETRICSFORDIFFERENTNETWORKTRACESFORSCENARIOA2
AhaggarpickedahigherbitrateontheaverageforaUHDTV (or 4.00 (5.12) in absolute values which is less than a 1-JND
compared to an HDTV and a phone. For instance, it selected differenceascomparedtotheotherschemes).Moreover,Ahag-
1.5x-2xhigherbitrateforUHDTVcomparedtothephonewith garpickedasignificantlylowerpercentageofUHDsegments,
almosta1-JNDdifferencebetweentheVMAFscoresforvarious specifically, a reduction of 41.80% (43.66%) compared to the
network traces. This is because devices with a phone-like res- heuristic-based (learning-based) ABR schemes, while keeping
olutioncanachievethehighestVMAFscore(95-98)requiring towithin1-JNDdifferenceinVMAFscoresacrossallnetwork
onlyhalfofthebitratethataUHDTVrequires.Wenotethatthe traces. This leads to large bandwidth savings as indicated by
VMAF score differences at a similar bitrate level (e.g., phone the average TD performance. We also note that Lumous 5G
versusHDTVinNYULTE)areduetothedifferentper-device containstheleastchallengingtraceswiththehighestbandwidth
VMAFmodelsusedtocalculatethescores. rangecomparedtotheotherthreesetsoftraces,andhence,its
|     |     |     |     |     |     |     | results do | not show | the | same significant |     | improvements | in the |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | ---------------- | --- | ------------ | ------ |
rebufferingperformance(specificallyinaverageRDandaverage
E. ResultsforMultipleIdenticalClientsWithSharedNetwork
Trace(ScenarioA2) RC)ofAhaggarwhencomparedagainsttheotherschemes.
|                                                 |     |     |     |     |     |     | From Fig.       | 7,  | we can | also see | that Ahaggar |        | achieved the |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------ | -------- | ------------ | ------ | ------------ |
| SimilartoScenarioA1,weransixUHDTVclientsforeach |     |     |     |     |     |     |                 |     | QoEitu |          |              |        |              |
|                                                 |     |     |     |     |     |     | highest average |     |        | across   | all network  | traces | and lowest   |
ABRschemeinthisscenario.However,incontrasttotheclient-
|     |     |     |     |     |     |     | average rebuffering |     | duration | in  | all traces | except | Lumous 5G. |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | -------- | --- | ---------- | ------ | ---------- |
sidenetworkemulationusedinScenarioA1,theclientsineach Specifically, Ahaggar achieved the highest average QoEitu
ABRschemeheresharethesamenetworktraceviaserver-side
|     |     |     |     |     |     |     | with an | improvement | of  | [Lumous | 4G  | Fig. | 7(a): 109.80% |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | ------- | --- | ---- | ------------- |
networkemulation,whichallowsustoevaluatetheperformance
(114.92%),Belgium4G/LTEFig.7(b):74.30%(90.16%),NYU
| when the          | network is | constrained    | at  | the server-end |      | (before the  |          |       |         |            |        |     |               |
| ----------------- | ---------- | -------------- | --- | -------------- | ---- | ------------ | -------- | ----- | ------- | ---------- | ------ | --- | ------------- |
|                   |            |                |     |                |      |              | LTE Fig. | 7(c): | 104.20% | (114.14%), | Lumous |     | 5G Fig. 7(d): |
| streams propagate | to         | the downstream |     | links          | that | separate the |          |       |         |            |        |     |               |
10.69%(10.87%)]andlowestaveragerebufferingdurationwith
clients). Table V shows the total QoE and detailed breakdown areductionof[Lumous4GFig.7(a):93.58%(95.40%),Belgium
ofeachQoEmetricforeachABRschemeforvariousnetwork
|                   |           |      |     |           |     |            | 4G/LTE           | Fig. 7(b): | 87.08% | (98.74%), |            | NYU   | LTE Fig. 7(c): |
| ----------------- | --------- | ---- | --- | --------- | --- | ---------- | ---------------- | ---------- | ------ | --------- | ---------- | ----- | -------------- |
| traces. Generally | speaking, | with | the | exception | of  | Lumous 5G, |                  |            |        |           |            |       |                |
|                   |           |      |     |           |     |            | 95.03% (98.75%), |            | Lumous | 5G        | Fig. 7(d): | 1.57% | (20.96%)],     |
Ahaggar achieved the best performance in terms of RC, RD comparedtotheheuristic-based(learning-based)ABRschemes.
| and TD with | a much | smaller | trade-off | in  | VMAF | as compared |                 |     |       |          |           |     |            |
| ----------- | ------ | ------- | --------- | --- | ---- | ----------- | --------------- | --- | ----- | -------- | --------- | --- | ---------- |
|             |        |         |           |     |      |             | The performance |     | gains | are most | prominent | in  | Lumous 4G, |
totheotherABRschemes.Specifically,theaveragescomputed Belgium 4G/LTE and NYU LTE, which is also evident in
| across all | the network  | traces    | show | that    | Ahaggar | reduced   |               |       |         |     |           |      |               |
| ---------- | ------------ | --------- | ---- | ------- | ------- | --------- | ------------- | ----- | ------- | --- | --------- | ---- | ------------- |
|            |              |           |      |         |         |           | Fig. 7(a)–(c) | where | Ahaggar |     | is placed | much | further ahead |
| average    | RD by 91.10% | (97.95%), |      | average | RC      | by 83.85% |               |       |         |     |           |      |               |
oftheotherschemes.
(91.47%) and average TD by 66.55% (70.90%) compared to FromthedetailedanalysisoftheQoEitu scoresinTableV,
theheuristic-based(learning-based)ABRschemes.Incontrast,
|     |     |     |     |     |     |     | we see that | Ahaggar | achieved |     | the highest | average | O.23 and |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | -------- | --- | ----------- | ------- | -------- |
the average VMAF scores only dropped by 4.24% (5.54%) O.46scoresforallnetworktraceswithanaverageimprovement
comparedtotheheuristic-based(learning-based)ABRschemes
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:30:43 UTC from IEEE Xplore.  Restrictions apply.

10390 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.23,NO.11,NOVEMBER2024
TABLEVI
AVERAGEQOEitu(O.46)SCORESANDITSMETRICSPRODUCEDBYAhaggar
RUNNINGONDEVICESWITHDIFFERENTRESOLUTIONSFORSCENARIOB2
Avg.QoEitu
| Fig.7. |     | (O.46)andavg.rebufferingdurationratioinvarious |     |     |     |     |     |     |     |     |     |
| ------ | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
networktracesforScenarioA2.Thebottom(left)edge,markandtop(right)
edgeindicatetheaverage−std,averageandaverage+std,respectively,with
a95%confidenceinterval.
TABLEVII
of126.23%(143.87%)and66.14%(73.69%)comparedtothe
AVERAGERESULTSOFQOEitu(O.46)ANDVMAFPRODUCEDBYDYNAMIC
heuristic-based (learning-based) ABR schemes, respectively. CLIENTSWHENRANCONCURRENTLYWITHANDWITHOUTAhaggar
These results again validate that Ahaggar is able to balance CLIENTSUNDERDIFFERENTNETWORKTRACESFORSCENARIOC
| the QoEitu | metrics | well. | This observation |     | is also consistent |     |     |     |     |     |     |
| ---------- | ------- | ----- | ---------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
N-QoElin
| with the |     | results | whereby | Ahaggar | achieved | the |     |     |     |     |     |
| -------- | --- | ------- | ------- | ------- | -------- | --- | --- | --- | --- | --- | --- |
bestorclosetothebestN-QoElinscores,rangingbetween0.97
| and 1.00 | (with | 1.00 being | the highest |     | possible score), | in all |     |     |     |     |     |
| -------- | ----- | ---------- | ----------- | --- | ---------------- | ------ | --- | --- | --- | --- | --- |
networktraces.SimilartotheresultsinScenarioA1,Dynamic
| achieved     | the second-best |          | results in     | terms | of average O.23      | and     |     |     |     |     |     |
| ------------ | --------------- | -------- | -------------- | ----- | -------------------- | ------- | --- | --- | --- | --- | --- |
| O.46 scores, | while           | Pensieve | experienced    |       | multiple rebuffering |         |     |     |     |     |     |
| events that  | led             | to the   | lowest average | O.23  | and O.46             | scores, |     |     |     |     |     |
averagedacrossallnetworktraces.
| Comparing |           | the findings | between | Scenario | A1 and         | this  |     |     |     |     |     |
| --------- | --------- | ------------ | ------- | -------- | -------------- | ----- | --- | --- | --- | --- | --- |
| scenario  | (Scenario | A2),         | we can  | see that | they generally | share |     |     |     |     |     |
Ahaggar
similar observations as to the performance gains study the effect of introducing new Ahaggar clients to a
achievescomparedtotheotherABRschemes,whichvalidates pool of existing non-Ahaggar clients. The average QoEitu
its performance in both client-side and server-side network (O.46) and VMAF results are presented in Table VII. From
emulationscenarios. theresults,wecanseethatDynamicclientsinthemixed-ABR
environmentsthatalsocontainAhaggarclientsperformedbet-
F. ResultsforMultipleMixed-DeviceClientsWithShared terthantheDynamicclientsintheDynamic-onlyenvironment
NetworkTrace(ScenarioB2) forallnetworktracesexceptBelgium4G/LTE.Specifically,the
DynamicclientsthatranconcurrentlywithAhaggar-UHDTV
SimilartoScenarioB1,werantwoclientswitheachdevice
(Ahaggar-HDTV)clientsachievedimprovementsinQoEituof
| resolution    | (DR)    | (total of   | six clients) | to           | evaluate the effective- |          |                 |            |                |               |                 |
| ------------- | ------- | ----------- | ------------ | ------------ | ----------------------- | -------- | --------------- | ---------- | -------------- | ------------- | --------------- |
|               |         |             |              |              |                         |          | [Lumous         | 4G: 12.36% | (21.21%),      | NYU LTE:      | 6.87% (13.28%), |
| ness of       | Ahaggar | in adapting | to           | different    | DRs. The                | results  |                 |            |                |               |                 |
|               |         |             |              |              |                         |          | Lumous          | 5G: 14.15% | (13.21%)],     | while keeping | VMAF con-       |
| are presented | in      | Table       | VI. From     | the results, | we can                  | see that |                 |            |                |               |                 |
|               |         |             |              |              |                         |          | sistent (within |            | 0.19% (0.08%)) | across these  | network traces, |
AhaggarisstillabletoshowcaseitsDRawarenessbyselecting
|     |     |     |     |     |     |     | when compared |     | against the Dynamic | clients | in Dynamic-only |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------------- | ------- | --------------- |
thelowestaveragebitratesforphone,followedbyHDTV,and
|             |         |          |     |       |            |         | environment.TheperformancegaininQoEitu |     |     |     | isprimarilydue |
| ----------- | ------- | -------- | --- | ----- | ---------- | ------- | -------------------------------------- | --- | --- | --- | -------------- |
| the highest | average | bitrates | for | UHDTV | across all | network |                                        |     |     |     |                |
tothelowerrebufferingduration(notshowninTableVII)where
traces(exceptforBelgium4G/LTEwheretheaverageselected
theDynamicclientsinmixed-ABRenvironmentsachievedre-
bitrateforphoneandHDTVarecomparable).Thisvalidatesits
ductioninaveragerebufferingdurationby[Lumous4G:20.05%
| DR awareness |     | capabilities | in both | client-side | and server-side |     |     |     |     |     |     |
| ------------ | --- | ------------ | ------- | ----------- | --------------- | --- | --- | --- | --- | --- | --- |
(30.03%),NYULTE:14.49%(11.34%),Lumous5G:47.95%
networkemulationscenarios.
(51.42%)]whenrunningconcurrentlywithAhaggar-UHDTV
|     |     |     |     |     |     |     | (Ahaggar-HDTV) |     | clients. | This validates | that the bandwidth |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | -------------- | ------------------ |
G. ResultsforMultipleMixed-ABRClients(ScenarioC) savingsbroughtaboutbyAhaggarclientshavepositivespill-
In this scenario, we ran Dynamic and Ahaggar clients over effects on other clients sharing the network as well (as
concurrently (three clients each giving six clients in total) to shown bythereduced rebuffering duration experienced bythe
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:30:43 UTC from IEEE Xplore.  Restrictions apply.

BENTALEBetal.:BITRATEADAPTATIONANDGUIDANCEWITHMETAREINFORCEMENTLEARNING 10391
Dynamic clients in mixed-ABR environments). We note that [13] A.Bentaleb,M.Lim,M.N.Akcay,A.C.Begen,andR.Zimmermann,
Belgium4G/LTEcontainsthemostchallengingtraceswiththe “Common media client data (CMCD): Initial findings,” in Proc. 31st
ACMWorkshopNetw.OperatingSyst.SupportDigit.AudioVideo,2021,
lowestbandwidthrangethantheotherthreesetsoftraces,and
pp.25–33,doi:10.1145/3458306.3461444.
| under these    | extreme |      | network | conditions,    | the  | Dynamic   | clients |                   |            |               |          |              |           |              |          |
| -------------- | ------- | ---- | ------- | -------------- | ---- | --------- | ------- | ----------------- | ---------- | ------------- | -------- | ------------ | --------- | ------------ | -------- |
|                |         |      |         |                |      |           |         | [14] A. Bentaleb, |            | M. Lim,       | M.       | N. Akcay, A. | C. Begen, | and          | R. Zim-  |
|                |         |      |         |                |      |           |         | mermann,          | “Meta      | reinforcement |          | learning     | for rate  | adaptation,” | in       |
| were selecting |         | much | lower   | video bitrates | that | coincided | with    |                   |            |               |          |              |           |              |          |
|                |         |      |         |                |      |           |         | Proc.             | IEEE Conf. | Comput.       | Commun., | 2023,        | pp. 1–10, | doi:         | 10.1109/ |
thelevelsofbitrateselectedbytheAhaggarclients.Hence,in
INFOCOM53939.2023.10228951.
Belgium4G/LTE,theintroductionofAhaggarclientsdidnot
|     |     |     |     |     |     |     |     | [15] A.Bentaleb,B.Taani,A.C.Begen,C.Timmerer,andR.Zimmermann, |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
“AsurveyonbitrateadaptationschemesforstreamingmediaoverHTTP,”
| affect the | amount | of  | data transmitted |     | over the | network | which |     |     |     |     |     |     |     |     |
| ---------- | ------ | --- | ---------------- | --- | -------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
IEEECommun.SurveysTut.,vol.21,no.1,pp.562–585,FirstQuarter,
explainstheabsenceofperformancegainsasseenintheother
2019,doi:10.1109/COMST.2018.2862938.
setsoftraces. [16] A.Bentaleb,P.K.Yadav,W.T.Ooi,andR.Zimmermann,“DQ-DASH:A
queuingtheoryapproachtodistributedadaptivevideostreaming,”ACM
|      |       |           |                |     |                |     |           | Trans.                                                          | Multimedia | Comput. | Commun. | Appl., | vol. 16, | no. 1, | pp. 1–24, |
| ---- | ----- | --------- | -------------- | --- | -------------- | --- | --------- | --------------------------------------------------------------- | ---------- | ------- | ------- | ------ | -------- | ------ | --------- |
|      |       |           | VI. CONCLUSION |     |                |     |           | 2020.                                                           |            |         |         |        |          |        |           |
|      |       |           |                |     |                |     |           | [17] A.Bokani,M.Hassan,S.Kanhere,andX.Zhu,“OptimizingHTTP-based |            |         |         |        |          |        |           |
| This | paper | presented | Ahaggar,       |     | a server-side, |     | learning- |                                                                 |            |         |         |        |          |        |           |
adaptivestreaminginvehicularenvironmentusingMarkovdecisionpro-
based,quality-awarebitrateguidancesolutionthatcomplements
cess,”IEEETrans.Multimedia,vol.17,no.12,pp.2297–2309,Dec.2015.
|     |     |     |     |     |     |     |     | [18] “CTA-5004:Webapplicationvideoecosystem–commonmediaclient |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
theclient-sideheuristic-basedABRschemes.Ahaggaradopts
data,”2020.Accessed:Mar.8,2024.[Online].Available:https://cdn.cta.
twokeyenablers:(i)ameta-RLapproachtofindthebestbitrate
tech/cta/media/media/resources/standards/pdfs/cta-5004-final.pdf
foreachclientunderthegivencircumstancesandquicklyadapt
|     |     |     |     |     |     |     |     | [19] “CTA-5006:Webapplicationvideoecosystem–commonmediaserver |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
to changing network conditions, and (ii) CMCD/SD specifi- data,”2022.Accessed:Mar.8,2024.[Online].Available:https://cdn.cta.
tech/cta/media/media/resources/standards/pdfs/cta-5006-final.pdf
| cation to | simplify | the | metadata | exchange | between |     | the server |                                                                  |     |     |     |     |     |     |     |
| --------- | -------- | --- | -------- | -------- | ------- | --- | ---------- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|           |          |     |          |          |         |     |            | [20] DASH-IF,“DASHreferenceclient,”2021.Accessed:Mar.8,2024.[On- |     |     |     |     |     |     |     |
andclients.ExperimentsshowthatAhaggardeliversabetter line]Available:https://reference.dashif.org/dash.js/
userexperiencewithlessbandwidthconsumptionovervarious [21] H.Dong,H.Dong,Z.Ding,S.Zhang,andChang,DeepReinforcement
networkconditions. Learning:Fundamentals,ResearchandApplications.Berlin,Germany:
Springer,2020.
|     |     |     |            |     |     |     |     | [22] Z.Duanmuetal.,“Assessingthequality-of-experienceofadaptivebitrate |     |     |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- | ---------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | REFERENCES |     |     |     |     | videostreaming,”2020,arXiv:2008.08804.                                 |     |     |     |     |     |     |     |
|     |     |     |            |     |     |     |     | [23] C.Finn,P.Abbeel,andS.Levine,“Model-agnosticmeta-learningforfast   |     |     |     |     |     |     |     |
adaptationofdeepnetworks,”inProc.34thInt.Conf.Mach.Learn.,2017,
| [1] ISO/IEC | 23009–5:2017 |     | Information | technology–Dynamic |     |     | adaptive |     |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | ----------- | ------------------ | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
pp.1126–1135.
| streaming | over | HTTP | (DASH) | – Part 5: | Server | and network | assisted |                                                                       |     |     |     |     |     |     |     |
| --------- | ---- | ---- | ------ | --------- | ------ | ----------- | -------- | --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|           |      |      |        |           |        |             |          | [24] A.Ganjametal.,“C3:Internet-scalecontrolplaneforvideoqualityopti- |     |     |     |     |     |     |     |
DASH(SAND),2017.Accessed:Mar.8,2024.[Online]Available:https:
//www.iso.org/standard/69079.html mization,”inProc.12thUSENIXConf.Netw.Syst.Des.Implementation,
[2] A.Bentaleb,M.Lim,M.N.Akcay,A.C.Begen,andR.Zimmermann, 2015,pp.131–144.
|     |     |     |     |     |     |     |     | [25] N.Heessetal.,“Emergenceoflocomotionbehavioursinrichenviron- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
“Ahaggarbitrateguidance,”2023.Accessed:Mar.8,2024.[Online]Avail-
ments,”2017,arXiv:1707.02286.
able:https://github.com/NUStreaming/Ahaggar
[3] S.Abbasloo,C.-Y.Yen,andH.J.Chao,“Classicmeetsmodern:Aprag- [26] T.Hospedales,A.Antoniou,P.Micaelli,andA.Storkey,“Meta-learning
maticlearning-basedcongestioncontrolfortheInternet,”inProc.Annu. inneuralnetworks:Asurvey,”2020,arXiv:2004.05439.
Conf.ACMSpecialInt.GroupDataCommun.Appl.Technol.Architectures [27] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,X.Yao,andL.Sun,“Comyco:
Quality-awareadaptivevideostreamingviaimitationlearning,”inProc.
Protoc.Comput.Commun.,2020,pp.632–647.
27thACMInt.Conf.Multimedia,2019,pp.429–437.
[4] S.Akhshabi,L.Anantakrishnan,C.Dovrolis,andA.C.Begen,“Server-
basedtrafficshapingforstabilizingoscillatingadaptivestreamingplayers,” [28] J. Jiang, V. Sekar, H. Milner, D. Shepherd, I. Stoica, and H. Zhang,
inProc.23rdACMWorkshopNetw.OperatingSyst.SupportDigit.Audio “CFA: A practical prediction system for video QoE optimization,”
Video,2013,pp.19–24,doi:10.1145/2460782.2460786. in Proc. 13th USENIX Conf. Netw. Syst. Des. Implementation, 2016,
pp.137–150.
[5] E.Alpaydin,IntroductiontoMachineLearning.Cambridge,MA,USA:
|     |     |     |     |     |     |     |     | [29] J. Kim, | Y. Jung, | H.  | Yeo, J. | Ye, and D. | Han, “Neural-enhanced |     | live |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------- | ---------- | --------------------- | --- | ---- |
MITPress,2020.
[6] K. Arulkumaran, M. P. Deisenroth, M. Brundage, and A. A. Bharath, streaming:Improvinglivevideoingestviaonlinelearning,”inProc.Annu.
“Deepreinforcementlearning:Abriefsurvey,”IEEESignalProcess.Mag., Conf.ACMSpecialInt.GroupDataCommun.Appl.Technol.Architectures
vol.34,no.6,pp.26–38,Nov.2017. Protoc.Comput.Commun.,2020,pp.107–125.
|     |     |     |     |     |     |     |     | [30] Z.Li,A.C.Begen,J.Gahm,Y.Shan,B.Osler,andD.Oran,“Streaming |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[7] A.C.Begen,“Manusmanumlavat:Mediaclientsandserverscooperating
videooverHTTPwithconsistentquality,”inProc.5thACMMultimedia
withcommonmediaclient/serverdata,”inProc.ACMAppl.Netw.Res.
Workshop,2021,pp.82–84,doi:10.1145/3472305.3472886. Syst.Conf.,2014,pp.248–258,doi:10.1145/2557642.2557658.
[8] A.C.Begen,M.N.Akcay,A.Bentaleb,andA.Giladi,“Adaptivestreaming [31] Z.Lietal.,“Probeandadapt:RateadaptationforHTTPvideostreamingat
of content-aware-encoded videos in dash.js,” SMPTE Motion Imag. J., scale,”IEEEJ.Sel.AreasCommun.,vol.32,no.4,pp.719–733,Apr.2014,
doi:10.1109/JSAC.2014.140405.
vol.131,no.4,pp.30–38,May2022,doi:10.5594/JMI.2022.3160560.
|     |     |     |     |     |     |     |     | [32] E.Liangetal.,“RLlib:Abstractionsfordistributedreinforcementlearn- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[9] A.C.Begen,A.Bentaleb,D.Silhavy,S.Pham,R.Zimmermann,andW.
Law,“Roadtosalvation:Streamingclientsandcontentdeliverynetworks ing,”inProc.35thInt.Conf.Mach.Learn.,2018,pp.3053–3062.
workingtogether,”IEEECommun.Mag.,vol.59,no.11,pp.123–128, [33] M.Lim,M.N.Akcay,A.Bentaleb,A.C.Begen,andR.Zimmermann,
“ThebenefitsofserverhintingwhenDASHingorHLSing,”inProc.1st
Nov.2021,doi:10.1109/MCOM.121.2100137.
Mile-HighVideoConf.,2022,pp.52–55,doi:10.1145/3510450.3517317.
| [10] A. Bentaleb, |     | A. C. | Begen, | S. Harous, | and R. | Zimmermann, | “Data- |             |         |        |         |              |                    |     |      |
| ----------------- | --- | ----- | ------ | ---------- | ------ | ----------- | ------ | ----------- | ------- | ------ | ------- | ------------ | ------------------ | --- | ---- |
|                   |     |       |        |            |        |             |        | [34] H. Mao | et al., | “Park: | An open | platform for | learning-augmented |     | com- |
drivenbandwidthpredictionmodelsandautomatedmodelselectionfor
low latency,” IEEE Trans. Multimedia, vol. 23, pp. 2588–2601, 2021, putersystems,”inProc.33rdInt.Conf.NeuralInf.Process.Syst.,2019,
| doi:10.1109/TMM.2020.3013387. |     |     |     |     |     |     |     | pp.2494–2506.                                                      |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|                               |     |     |     |     |     |     |     | [35] H.Mao,R.Netravali,andM.Alizadeh,“Neuraladaptivevideostreaming |     |     |     |     |     |     |     |
[11] A.Bentaleb,A.C.Begen,andR.Zimmermann,“SDNDASH:Improv-
withpensieve,”inProc.Conf.ACMSpecialInt.GroupDataCommun.,
ingQoEofHTTPadaptivestreamingusingsoftwaredefinednetwork-
| ing,” | in Proc. | 24th ACM | Int. | Conf. Multimedia, | 2016, | pp. | 1296–1305, | 2017,pp.197–210. |     |     |     |     |     |     |     |
| ----- | -------- | -------- | ---- | ----------------- | ----- | --- | ---------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
doi:10.1145/2964284.2964332. [36] L.Meietal.,“RealtimemobilebandwidthpredictionusingLSTMNN,”
[12] A. Bentaleb, A. C. Begen, and R. Zimmermann, “ORL-SDN: Online inProc.Int.Conf.PassiveAct.Netw.Meas.,2019,pp.34–47.
|     |     |     |     |     |     |     |     | [37] V. V. | Menon, | H. Amirpour, |     | M. Ghanbari, | and C. | Timmerer, | “OPTE: |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ------------ | --- | ------------ | ------ | --------- | ------ |
reinforcementlearningforSDN-enabledHTTPadaptivestreaming,”ACM
|     |     |     |     |     |     |     |     | Online | per-title | encoding | for | live video streaming,” |     | in Proc. | IEEE Int. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | -------- | --- | ---------------------- | --- | -------- | --------- |
Trans.MultimediaComput.Commun.Appl.,vol.14,no.3,pp.1–28,2018,
doi:10.1145/3219752. Conf.Acoust.SpeechSignalProcess.,2022,pp.1865–1869.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:30:43 UTC from IEEE Xplore.  Restrictions apply.

10392 IEEETRANSACTIONSONMOBILECOMPUTING,VOL.23,NO.11,NOVEMBER2024
[38] M.Muetal.,“Ascalableuserfairnessmodelforadaptivevideostreaming MayLimreceivedtheBEScandMScdegreefrom
overSDN-assistedfuturenetworks,”IEEEJ.Sel.AreasCommun.,vol.34, Nanyang Technological University (NTU), Singa-
no.8,pp.2168–2184,Aug.2016. pore,in2015.Sheiscurrentlyworkingtowardthe
[39] A.Narayananetal.,“Avariegatedlookat5Ginthewild:Performance, PhDdegreeincomputerscience withtheNational
power,andQoEimplications,” inProc. ACMSIGCOMMConf.,2021, UniversityofSingapore(NUS),Singapore.Hercur-
pp.610–625. rent research interest is primarily in multimedia
[40] S.Pham,P.Heeren,D.Silhavy,andS.Arbanowski,“Evaluationofshared streamingsystemsandshehasdoneseveralworks
resourceallocationusingSANDforABRstreaming,”inProc.10thACM relating to low-latency streaming for live 2D and
MultimediaSyst.Conf.,2019,pp.165–174. 6DoFvideos.
[41] J.J.QuinlanandC.J.Sreenan,“Multi-profileultrahighdefinition(UHD)
AVCandHEVC4KDASHdatasets,”inProc.9thACMMultimediaSyst.
Conf.,2018,pp.375–380.
[42] R. Rassool, “VMAF reproducibility: Validating a perceptual practical
videoqualitymetric,”inProc.IEEEInt.Symp.BroadbandMultimedia
Syst.Broadcast.,2017,pp.1–2. MehmetN.AkcayreceivedtheBScdegreeinthe
[43] H.Riiser,P.Vigmostad,C.Griwodz,andP.Halvorsen,“Commutepath fieldofcomputerengineering,fromIstanbulTech-
bandwidthtracesfrom3Gnetworks:Analysisandapplications,”inProc. nicalUniversity,in2005,andtheMScdegreeinthe
4thACMMultimediaSyst.Conf.,2013,pp.114–118. samefieldfromBogaziciUniversity,in2008,andhas
[44] W.Robitzaetal.,“HTTPadaptivestreamingQoEestimationwithITU-T workedintheindustryformorethan10years,and
Rec.P.1203:Opendatabasesandsoftware,”inProc.9thACMMultimedia thePhDdegreeincomputersciencefromOzyegin
Syst.Conf.,2018,pp.466–471. University,in2022.HisresearchinterestsareHTTP
[45] D. Smilkov et al., “Tensorflow.js: Machine learning for the web and adaptive streaming, low-latency live streaming and
beyond,”inProc.Mach.Learn.Syst.,vol.1,pp.309–321,2019. softwareverificationusingformalmethods.
[46] K. Spiteri, R. Sitaraman, and D. Sparacio, “From theory to practice:
ImprovingbitrateadaptationintheDASHreferenceplayer,”ACMTrans.
MultimediaComput.Commun.Appl.,vol.15,no.2s,pp.1–29,2019.
[47] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal
bitrateadaptationforonlinevideos,”IEEE/ACMTrans.Netw.,vol.28,
no.4,pp.1698–1711,Aug.2020.
[48] Y.Tang,“TFLearn:TensorFlow’shigh-levelmodulefordistributedma-
AliC.Begen(SeniorMember,IEEE)receivedthe
chinelearning,”2016,arXiv:1612.04251. PhDdegreeinelectricalandcomputerengineering
[49] F.Tashtarian,A.Bentaleb,A.Erfanian,H.Hellwagner,C.Timmerer,and from Georgia Tech. He has been a research and
R.Zimmermann,“HxL3:OptimizeddeliveryarchitectureforHTTPlow- development engineer since 2001, and has broad
latencylivestreaming,”IEEETrans.Multimedia,vol.25,pp.2585–2600, experienceinmathematicalmodeling,performance
2022. analysis,optimization,standardsdevelopment,intel-
[50] B.Turkkanetal.,“GreenABR:Energy-awareadaptivebitratestreaming lectualpropertyandinnovation.Between2007and
withdeepreinforcementlearning,”inProc.13thACMMultimediaSyst. 2015,hewaswiththeVideoandContentPlatforms
Conf.,2022,pp.150–163. ResearchandAdvancedDevelopmentGroup,Cisco.
[51] J. van der Hooft et al., “HTTP/2-based adaptive streaming of HEVC Currently, he is affiliated with Ozyegin University,
video over 4G/LTE networks,” IEEE Commun. Lett., vol. 20, no. 11, whereheteachesandadvisesstudentsinthecomputer
pp.2177–2180,Nov.2016. sciencedepartment.Todate,hereceivedseveralacademicandindustryawards
[52] F. Y. Yan et al., “Learning in situ: A randomized experiment in video (includinganEmmyAwardforTechnologyandEngineering),andwasgranted
streaming,”inProc.17thUSENIXConf.Netw.Syst.Des.Implementation, more than 30 US patents. In 2016, he was elected distinguished lecturer by
2020,pp.495–512. theIEEECommunicationsSociety,andin2018,hewasre-electedforanother
[53] X.Yin,A.Jindal,V.Sekar,andB.Sinopoli,“Acontrol-theoreticapproach two-yearterm.In2017,heinitiatedandsincethenhasbeentheheadofdelegation
fordynamicadaptivevideostreamingoverHTTP,”inProc.ACMConf. fortheTurkishNationalBodyforISO/IECJTC1/SC29(JPEGandMPEG).He
SpecialInt.GroupDataCommun.,2015,pp.325–338. wasalsolistedamongtheworld’smostinfluentialscientistsinthesubfieldof
[54] C. Yu, A. Velu, E. Vinitsky, Y. Wang, A. Bayen, and Y. Wu, “The networkingandtelecommunications,in2020and2021.
surprising effectiveness of PPO in cooperative, multi-agent games,”
2021,arXiv:2103.01955.
[55] H.Zhangetal.,“OnRL:Improvingmobilevideotelephonyviaonline
reinforcementlearning,”inProc.26thAnnu.Int.Conf.MobileComput.
Netw.,2020,Art.no.29. Roger Zimmermann (Senior Member, IEEE) re-
[56] C.Zhu,M.Dastani,andS.Wang,“Asurveyofmulti-agentreinforcement ceivedtheMSandPhDdegreesfromtheUniversity
learningwithcommunication,”2022,arXiv:2203.08975. ofSouthernCalifornia(USC),respectively.Heiscur-
[57] X.Zhu,S.Sen,andZ.M.Mao,“Livelyzer:Analyzingthefirst-mileingest rentlyaprofessorwiththeDepartmentofComputer
performanceoflivevideostreaming,”inProc.12thACMMultimediaSyst. Science, National University of Singapore (NUS),
Conf.,2021,pp.36–50. Singapore. He is also a lead investigator with the
Grab-NUS AI Lab and from 2011–2021 he was
Abdelhak Bentaleb (Member, IEEE) received the deputy director with the Smart Systems Institute
PhDdegreeincomputersciencefromtheNational (SSI),NUS.Hehascoauthoredabook,sevenpatents,
UniversityofSingapore(NUS),Singapore,in2019. andmorethan350conferencepublications,journal
He continued as a research fellow with the same articles,andbookchaptersintheareasofmultimedia
department until 2022. He is currently an assistant processing,networkinganddataanalytics.Heisadistinguishedmemberofthe
professor with the Department of Computer Sci- ACM.HerecentlywasSecretaryofACMSIGSPATIAL(2014–2017),adirector
enceandSoftwareEngineering,ConcordiaUniver- oftheIEEEMultimediaCommunicationsTechnicalCommittee(MMTC)Re-
sity,Canada.Heisaco-founderofAtlastreamInc., viewBoardandaneditorialboardmemberoftheSpringerMultimediaToolsand
Singapore.Hereceivedmanyprestigiousawardslike Applicationsjournal.HeisalsoanassociateeditorwithIEEEMultiMedia,ACM
SIGMMAwardforOutstandingPhDThesisAward, TransactionsonMultimediaComputing,Communications,andApplicationsand
DASH-IFBestPhDDissertationAwardandDean’s IEEEOpenJournaloftheCommunicationsSociety.
Graduate Research Excellence Award AY2018/2019. His research interests
includeappliedAIinmultimediasystemsandcommunication,videostreaming
architectures,contentdelivery,distributedcomputing,computernetworksand
protocols,wirelesscommunications,andmobilenetworks.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:30:43 UTC from IEEE Xplore. Restrictions apply.