Improving Generalization for Neural Adaptive Video Streaming
via Meta Reinforcement Learning
NuowenKan YuankunJiang ChenglinLi
ShanghaiJiaoTongUniversity ShanghaiJiaoTongUniversity ShanghaiJiaoTongUniversity
kannw_1230@sjtu.edu.cn yuankunjiang@sjtu.edu.cn lcl1985@sjtu.edu.cn
WenruiDai JunniZou HongkaiXiong
ShanghaiJiaoTongUniversity ShanghaiJiaoTongUniversity ShanghaiJiaoTongUniversity
daiwenrui@sjtu.edu.cn zoujunni@sjtu.edu.cn xionghongkai@sjtu.edu.cn
ABSTRACT viaMetaReinforcementLearning.InProceedingsofthe30thACMInter-
Inthispaper,wepresentametareinforcementlearning(Meta-RL)- nationalConferenceonMultimedia(MM’22),October10–14,2022,Lisboa,
Portugal. ACM, New York, NY, USA, 11 pages. https://doi.org/10.1145/
basedneuraladaptivebitratestreaming(ABR)algorithmthatis
3503161.3548331
abletorapidlyadaptitscontrolpolicytothechangingnetwork
throughputdynamics.Specifically,toallowrapidadaptation,we 1 INTRODUCTION
discuss the necessity of detaching the inference of throughput
Thanks to the emerging trend that watching videos online has
dynamicswiththeuniversalcontrolmechanismthatisinessence
become a predominant Internet application, it becomes non-
shared by all potential throughput dynamics for neural ABR
negligibletoprovideabetterqualityofexperience(QoE)forusers
algorithms.Tometa-learntheABRpolicy,wethenbuildupamodel-
invideostreamingviarateadaptationtechniques.Throughonline
freesystemframework,composedofaprobabilisticlatentencoder
videodeliveryprotocols,suchasdynamicadaptivestreamingover
thatinferstheunderlyingdynamicsfromtherecentthroughput
HTTP(DASH)[20]andHTTPlivestreaming(HLS)[9],thebitrate,
context,andapolicynetworkthatisconditionedonlatentvariable
whichindicatesthequalityorcompressionlevelforeachvideo
andlearnstoquicklyadapttonewenvironments.Additionally,to
chunk(orsegment),canbedynamicallydeterminedtoadapttothe
address the difficulties caused by training the policy on mixed
time-varyingnetworkthroughputandcurrentbufferoccupancyof
dynamics, on-policy RL (or imitation learning) algorithms are
videoplayer.Ingeneral,videoqualitycanbeenhancedbyassigning
suggested for policy training, with a mutual information-based
ahigherbitrateforthechunktobetransmitted,which,however,
regularizationtomakethelatentvariablemoreinformativeabout
mayresultinarebufferingevent(i.e.,stallingduringplayback)
thepolicy.Finally,weimplementouralgorithm’smeta-training
especiallywhenthenetworkconditionispoorandunstable.
and meta-adaptation procedures under a variety of throughput
Asakeycomponentofrateadaptation,adaptivebitratestream-
dynamics. Empirical evaluations on different QoE metrics and
ing (ABR) algorithms aim to solve a stochastic optimal control
multipledatasetscontainingreal-worldnetworktracesdemonstrate
problemthatrevealshowtostrikeanoptimaltrade-offbetween
thatouralgorithmoutperformsstate-of-the-artABRalgorithms,in
maximizing the video quality and avoiding the rebuffering, by
termsoftheperformanceontheaveragechunkQoE,consistency
determiningthefine-grainedbitratecombinationsequentiallyfor
andfastadaptationacrossawiderangeofthroughputpatterns.
continuouslytransmittedvideochunks.However,duetothetime-
varyingandheterogeneousdynamicsofnetworkthroughputin
CCSCONCEPTS
realworld,itisunfortunatelyintractabletoachievetheoptimal
•Informationsystems→Multimediastreaming;•Comput- trade-offwithanexplicitsolution.Inaddition,theABRalgorithm
ingmethodologies→Sequentialdecisionmaking. inpracticeisalsoexpectedtobeabletoimplementquicklyonline,
becauseahigheroverheadofinferencetimeforrateadaptation
KEYWORDS willinevitablyincreasetheend-to-endlatency.
Rateadaptation,metadeepreinforcementlearning,generalization. To address this challenge, Yin et al. in [24] argued that the
modelpredictivecontrol(MPC)approachisanaturalfitforthe
ACMReferenceFormat: rate adaptation problem and proposed two simple yet effective
NuowenKan,YuankunJiang,ChenglinLi,WenruiDai,JunniZou,andHongkai algorithms,namelyRobustMPCandFastMPC,basedonthepre-
Xiong.2022.ImprovingGeneralizationforNeuralAdaptiveVideoStreaming
diction of future network throughput with the harmonic mean
ofpastthroughput.Followingthisprinciple,variousstudies(e.g.,
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
CS2P[22],BayesMPC[10],Fugu[23])havebeenproposedtoseek
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation forahigherQoEbyimprovingthethroughputpredictionaccuracy.
onthefirstpage.CopyrightsforcomponentsofthisworkownedbyothersthanACM The weakness of these MPC-based methods is that they would
mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,
sufferfromissuessuchasinevitablebiasinthroughputprediction
topostonserversortoredistributetolists,requirespriorspecificpermissionand/ora
fee.Requestpermissionsfrompermissions@acm.org. andhighcomputationalcomplexityinrealworldimplementation,
MM’22,October10–14,2022,Lisboa,Portugal whicharethenalleviatedbylearning-basedmethods.Byexploiting
©2022AssociationforComputingMachinery.
thestrongnon-linearfittingcapabilityofneuralnetworks(NNs),
ACMISBN978-1-4503-9203-7/22/10...$15.00
https://doi.org/10.1145/3503161.3548331 theselearning-basedmethodsareabletodirectlyachieveasuperior
3006

MM’22,October10–14,2022,Lisboa,Portugal NuowenKanetal.
QoEperformancewithoutanyiterativecomputation.Specifically, 3-hourreal-worldtest.EvaluationresultsdemonstratethatMERINA
formulated as a Markov decision process (MDP), neural ABR outperformsstate-of-the-artABRalgorithmsonthein-distribution
algorithmsconsiderthemostrecentlyrecordedthroughputvalues tracesbyatleast3%intermsofaveragechunkQoE.Onthreeout-of-
and current buffer occupancy as the state 𝒔 ∈ S, the selected distributiondatasetsandreal-worldtest,MERINAbeatsallneural
bitrate version as the action 𝒂 ∈ A, and directly approximate baselinesintermsoftheaveragechunkQoEwithoutadaptation,
an optimal rate adaptation policy 𝜋 : S → A without the presentingaperformancegainofupto26%betweenMERINAand
needoflearningexplicitlythethroughputprediction.Withthis thesecond-bestalgorithm,andachievesahigheraveragechunk
intuition,manyeffortshavebeenmadetoprovideuserswitha QoEoverallbaselineswithonlyabout200epochs(i.e.,5minutes)of
(near)-optimal QoE, by exploiting deep reinforcement learning adaptation.Ourmaincontributionscanbesummarizedasfollows.
(DRL)-basedmethods(e.g.,Pensieve[14],D-DASH[5])orimitation • Westudythegeneralizationproblemofadaptivevideostreaming,
learning-basedmethods(e.g.,Comyco[7,8]). andformulatetherateadaptationproblemasaPOMDP,rather
However,thesuperiorperformanceofexistingneuralABRalgo- than previously stated MDP. We then propose a model-free
rithmsissubjecttocertainconditions,suchasthattheprobability systemframeworkbasedoncontext-basedmeta-RLtoimprove
of state transition (i.e., 𝒔(cid:4) = 𝑓(𝒔,𝒂) with 𝑓 being the dynamics generalization for neural ABR algorithms, by decoupling the
transition function) is identical or similar between the training inferenceofthroughputdynamics(referredtoaslatentencoder)
and deployment environments. This condition is unfortunately fromtheuniversalcontrolmechanismthatissharedbyallpoten-
notsatisfiedinmanyreal-worldscenarios,possiblyresultingina tialthroughputdynamics(referredtoasmeta-policynetwork).
poorconsistencyofneuralABRalgorithm’sperformanceacross • Toensurerapidadaptationtotime-varyingyetindistinguishable
arangeofnetworkthroughputpatterns[1,10,13,23].Thougha throughputdynamicsinreal-worldscenarios,weproposean
lifelonglearningmethodwasproposedin[7]toaddressthisissue efficient meta-policy search scheme for the mixed dynamics,
bycontinuouslyfine-tuningtheNNswithnewthroughputdata whichincludestheuseofon-policyRLalgorithms(orimitation
online,itisstillnotanaturalchoiceforneuralABRalgorithms, learning)toalleviateestimationbiasforvaluefunction,anda
since NNs trained with certain known dynamics will lose their mutualinformation-basedregularizationinthepolicylossto
abilitytoquicklyfittonewdynamicsovertime[12]. makethelatentvariablemoreinformativeaboutthepolicy.
Inthispaper,weintroduceMERINA,aMEtaReInforcement • We implement MERINA’s meta-training and meta-adaptation
learning(Meta-RL)-basedNeuralABRalgorithm,whichisableto procedures,andvalidateitsimprovedgeneralizationcapability
rapidlyadaptitscontrolpolicytounfamiliarthroughputdynamics. throughnumerousempiricalevaluationsondifferentQoEmetrics
Specifically,wediscussthattherateadaptationproblemcanbe andmultipledatasetscontainingreal-worldnetworkthroughput
in essence modeled as a partially observable Markov decision traces,aswellasareal-worldtest.Theseevaluationsdemonstrate
process(POMDP),inwhichtheagentisunawareoftheunderlying thatMERINAoutperformsthestate-of-the-artABRalgorithms
informationofthroughputdynamics.Toenablefastadaptationto intermsofboththeaveragechunkQoEonthein-distribution
newthroughputdynamicsforneuralABRalgorithms,itisnecessary throughputtraces,andthecapabilityofgeneralizationandquick
toseparatethedynamicsinferencefromtheuniversalcontrolpolicy adaptationontheout-of-distributionthroughputtraces.
sharedbyallpotentialstatetransitionfunctions.Thus,weadoptthe
context-basedmeta-RLmethodtoconstructamodel-freesystem 2 BACKGROUNDANDMOTIVATION
framework,consistsofaprobabilisticlatentencoderthatinfers
2.1 ProblemFormulation
current throughput dynamics from recent throughput contexts,
and a meta-policy network that selects the bitrate per chunk Inatypicaladaptivevideostreamingsystem,thevideoistemporally
accordingtothestateandsampledlatentvariable.Oncedeployedin dividedinto𝐾 chunks(i.e.,segments)withafixedtimeduration𝐿.
environmentswithdifferentthroughputdynamics,theABRpolicy Eachvideochunkisfurtherencodedintomultiplequalityversions
canbelearnedtoadapttocorrespondingdynamicswithonlya ofdifferentbitrates,withthesetofavailablebitratesdenotedby
fewtrials.However,duetothetime-varyingyetindistinguishable A = {𝑎 1 ,𝑎 2 ,···,𝑎 𝑀 }, where𝑀 represents the total number of
featureofthroughputdynamics,difficultiesemergesinmeta-policy bitrateversions.Let𝑎 𝑘 ∈Adenotethebitrateversionallocatedfor
search on such a mixed dynamics. Therefore, we propose an the𝑘-thchunk𝑈 𝑘.Then,oncethechunk𝑈 𝑘 hasbeencompletely
efficientmeta-policysearchscheme,whichincludesusingon-policy downloaded,thebufferoccupancy𝐵 𝑘 ofthevideoplayerdeployed
RL(orimitationlearning)algorithmstoalleviatetheestimation attheusersidecanbeexpressedas:
bias of value function, as well as a mutual information-based
regularizationinthepolicylosstomakethelatentvariablemore
𝐵 𝑘 = [(𝐵 𝑘−1 −𝑑 𝑘 ) + +𝐿], 𝑑 𝑘 =𝐸 𝑎𝑘 /𝐶 𝑘 , (·) + (cid:2)max{·,0}, (1)
informativeaboutthepolicy.Finally,weimplementourproposed where𝐶 𝑘istheaveragenetworkthroughputwithinthedurationof
ABRalgorithmwithameta-trainingprocedurewherearegularized downloadingchunk𝑈 𝑘,𝐸 𝑎𝑘 denotestheactualsizeof𝑈 𝑘associated
proximal policy optimization (PPO) algorithm is used to train withtheselectedbitrateversion𝑎 𝑘,theterm𝑑 𝑘 thenrepresentsthe
theinferencenetwork(encoder)andthelatent-conditionedmeta- correspondingtimedurationspentfordownloadingchunk𝑈 𝑘.The
policybyfollowinganimitationlearning-basedpre-training,and rebufferingeventwilloccurwithinthedurationof(𝑑 𝑘 −𝐵 𝑘−1 ) +if
ameta-adaptationprocedurethataimstorapidlyadaptthemeta- theterm𝐵 𝑘−1 −𝑑 𝑘isnegative,i.e.,thebufferhasnovideoremaining
policy to unseen throughput dynamics by using the same PPO whilethenextchunk𝑈 𝑘 hasnotbeencompletelydownloadedyet.
update.Empirically,wecompareMERINAtootherABRbaselineson Asconventionallyadoptedinmanylearning-basedABRalgo-
differentQoEmetricsandreal-worldthroughputtraces,aswellasa rithms,theadaptivevideostreamingsystemcanbeformulated
3007

ImprovingGeneralizationforNeuralAdaptiveVideoStreamingviaMetaReinforcementLearning MM’22,October10–14,2022,Lisboa,Portugal
asaMarkovdecisionprocess(MDP),withthestate𝑠 ∈ S for Inference Network (Latent Encoder)
𝑘
downloadingthechunk𝑈
|     |     |     | 𝑘 representedbysixfeatures,namely |     |     |     |     | contexts |     | Encoder |     |     |
| --- | --- | --- | --------------------------------- | --- | --- | --- | --- | -------- | --- | ------- | --- | --- |
themeasured1)averagethroughput𝐶
|     |     |     |     | 𝑘−1 | and2)corresponding |     |     |     |     | (cid:2264) |     |     |
| --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | ---------- | --- | --- |
latent distribution
| download | time 𝑑 𝑘−1 | , 3) | the vector | of chunk | sizes | associated |     |     |     |     |     |     |
| -------- | ---------- | ---- | ---------- | -------- | ----- | ---------- | --- | --- | --- | --- | --- | --- |
𝐸(cid:5)
| with available | bitrate       | versions     | for             | the 𝑘-th   | video       | chunk:    | =           |                   |                                 |                |             |     |
| -------------- | ------------- | ------------ | --------------- | ---------- | ----------- | --------- | ----------- | ----------------- | ------------------------------- | -------------- | ----------- | --- |
|                |               |              |                 |            |             |           |             | Video Pllayers    |                                 | Policy Network | latent      |     |
| {𝐸 𝑘 , 𝐸 𝑘 ,   | · ·· , 𝐸 𝑘    | } , 4 ) c u  | r r en t b u ff | e r o cc u | p a n c y 𝐵 | , 5 )s    | e le c te d |                   |                                 |                |             |     |
| 𝑎 𝑎            | 𝑎 𝑀           |              |                 |            |             | 𝑘 − 1     |             |                   |                                 | ssttate        |             |     |
| 1 𝑎2           |               |              |                 |            |             |           |             |                   |                                 |                | Meta-Policy |     |
| b it r a t e 𝑘 | − 1 o f t h e | la s t v i d | e o c h u n k   | , an d 6 ) | t h e r em  | a in in g | n u m b e r |                   |                                 |                |             |     |
|                |               |              |                 |            |             |           |             | Time-v a r yi n g |  a n d   h e te r og e neoouuss | bitrate        |             |     |
ofvideochunksthathavenotbeendownloadedyet. th r o u g h p u t  d y n a m ic s
Toquantifytheuser’sQoE,weemployawidelyusedobjective Buffer occupancy Trained by on-policy RL or imitation learning
Figure1:SystemframeworkoftheproposedMERINA.
metricthatincorporatesthetrade-offbetweenvideoquality,quality
fluctuationandriskofrebufferingeventsasalinearcombination:
policythatperformswellifthedistributionofthroughputdynamics
|     |     | (cid:2) |     | (cid:2) |     |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑟(𝑠 ,𝑎 )=𝑞(𝑎 )−𝛼(cid:2)𝑞(𝑎 )−𝑞(𝑎 )(cid:2)−𝛽(𝑑 −𝐵 ) , hasbeenexperiencedinthetrainingdataset,butmayunfortunately
| 𝑘   | 𝑘 𝑘 |     | 𝑘   | 𝑘−1 | 𝑘   | 𝑘−1 | + (2) |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
where𝑟 ∈𝑅,𝑞(𝑎 )canbeanyvideoqualitymetric(e.g.,PSNRand presentaverypoorgeneralizationinunseen(orout-of-distribution)
𝑘
SSIM),and𝛼 and𝛽areanon-negativepenaltyweightthatensures networkcontexts.Meta-RL,asapopularmethodforfastadaptation
tounseenenvironments,trainsanagentfrommultiplesampletasks
| the temporal | quality | smoothness |     | and penalizes |     | the rebuffering |     |     |     |     |     |     |
| ------------ | ------- | ---------- | --- | ------------- | --- | --------------- | --- | --- | --- | --- | --- | --- |
toconstructameta-policyoverthesharedstructureacrosstasks
| delay, respectively. |     | Therefore, | the | control | policy | of the | ABR |     |     |     |     |     |
| -------------------- | --- | ---------- | --- | ------- | ------ | ------ | --- | --- | --- | --- | --- | --- |
[3,16].WearethereforemotivatedtoproposeMERINA,acontext-
algorithmcanbederivedbysolvingasequentialdecision-making
basedmeta-RLapproachfordecouplinginferenceofunderlying
problemthatoptimizestheaveragechunkQoEfortheuserundera networkdynamics𝒛fromtheuniversalcontrolmechanism.Other
constrainedyettime-varyingnetworkthroughput:
(cid:3) than learning a separate ABR control policy for each possible
|     |     |     | 1   | 𝐾   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑎 ∗ =arg 𝑟(𝑠 ,𝑎 ), n et w o r k th r ou g h p ut dy n a m ic fr o m m ill io n s o f s a m p le s , w e wo u l d
|     | 𝑘   |     | max 𝐾 |     | 𝑘 𝑘 |     | (3a) |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
𝑎 𝑘 =0 lik e o u r A B R a g en t to di s c ov er a c om m o n c o n tr o l m e c h a ni sm ( i. e .,
𝑠 =𝑓(𝑠 ,𝑎 ), 𝑎 ∈A, meta-policy𝜋(𝒂|𝒔,𝒛))sharedacrossarangeofpossiblethroughput
|     | s.t. | 𝑘+1 | 𝑘   | 𝑘 𝑘 |     |     | (3b) |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
wherethedynamicsmodel𝑓 :S×A→Softhevideostreaming dynamicsduringthetraining.Oncelearned,thispolicyisexpected
toadapttonewthroughputdynamicswithonlyafewtrialswhen
systemincludesthebufferoccupancyasgiveninEq.(1),aswellas
theirnecessarylatentvariable𝒛isprovided.Inotherwords,with
thedynamicsofnetworkthroughputwhichunfortunatelycannot
MERINAweintendtodevelopageneralizedparadigmforneural
beexplicitlyrepresentedorpredicted.Assuch,wearetheoretically
ABRalgorithms,bylearninghowtorapidlylearnanappropriate
unabletofindtheglobaloptimalsolutionofEq.(3),butendeavour
inpracticetoapproachascloseraspossibletothisglobaloptimum. ABRpolicyforeachnetworkenvironment.
| 2.2 LearningHowtoLearnBitrateAdaptation |     |     |     |     |     |     |     | 3 PROPOSEDMETHOD |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
TheoverallsystemframeworkofMERINAisillustratedinFig.1,
| As a result, | the MDP | of  | an adaptive | video | streaming |     | system |     |     |     |     |     |
| ------------ | ------- | --- | ----------- | ----- | --------- | --- | ------ | --- | --- | --- | --- | --- |
< S,A,𝑃,𝑅 >, 𝑃 = 𝑝(𝑠 |𝑠 ,𝑎 ) comprisingtwofollowingtwokeycomponents.
| can be formulated |            | as          |     | where       |         | 𝑘+1 | 𝑘 𝑘    |                                                      |     |     |     |     |
| ----------------- | ---------- | ----------- | --- | ----------- | ------- | --- | ------ | ---------------------------------------------------- | --- | --- | --- | --- |
|                   |            |             |     |             |         |     |        | • 1)Meta-traineddynamicsinferencenetwork(i.e.,latent |     |     |     |     |
| is the state      | transition | probability |     | that mainly | depends |     | on the |                                                      |     |     |     |     |
dynamics of network throughput. Note that the dynamics of encoder).Toendowthecontrolpolicywithaneffectiverepresen-
network throughput are practically hidden from the agent and tationofcurrentnetworkdynamics,wecapturetheknowledge
independentofthechosenactions,whicharetypicallytime-varying aboutunderlyingdynamicswithalatentprobabilisticcontext
|     |     |     |     |     |     |     |     | variable 𝒛 based | on  | recent experience | of the current | (new) |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------------- | -------------- | ----- |
andheterogeneousinrealworldscenarios.Consequently,thestate
transitionprobability𝑃willvarycontinuouslyovertimeandresult dynamics.Encounteringanewnetworkenvironment,thislatent
variable𝒛canreasonaboutdynamicsuncertainty,allowingfora
inavarietyofdifferentMDPs,whichinessencecanbeformulated
moreaccuratelyasapartiallyobservableMarkovdecisionprocess stochasticexplorationofmeta-learnedpolicytoexplorestates
(POMDP).Bydenotingtheunderlyingthroughputdynamicsas withpotentiallyhigherrewardswhilealsoquicklyadaptingto
alatentvariable𝒛 ∈ 𝑍,wecanre-formulatetheadaptivevideo thenewdynamics.Meanwhile,samplingthelatentvariablefrom
streamingproblemasatuple< S,A,𝑃,𝑍,𝑅 >,wherethestate aprobabilisticdistributionimprovesthegeneralizationofcontrol
spaceS,actionspaceAandrewardspace𝑅remainthesame,while policieswhenadeterministicinferenceofdynamicsisdifficult.
•
thestatetransitionprobabilitychangesto𝑃 = 𝑝(𝑠 𝑘+1 |𝑠 𝑘 ,𝑎 𝑘 ,𝑧 𝑘 ), 2)Latent-conditionedpolicynetwork(i.e.,policysearch).
with𝑧 representingthethroughputdynamicsduringtheduration ToidentifyauniversalABRcontrolpolicycapableofadapting
𝑘
|                |       | 𝑈   |           |            |     |           |     | itsbehaviortothenetworkthroughputdynamics,weseta𝜃- |     |     |     |     |
| -------------- | ----- | --- | --------- | ---------- | --- | --------- | --- | -------------------------------------------------- | --- | --- | --- | --- |
| of downloading | chunk |     | 𝑘. In the | following, | we  | will omit | the |                                                    |     |     |     |     |
subscript𝑘 fornotationalsimplicity,i.e.,𝑠 ,𝑎 ,𝑟 ,𝑧 parameterized policy 𝜋 (𝒂|𝒔,𝒛) as conditioned on the latent
|     |     |     |     |     | 𝑘 𝑘 | 𝑘 𝑘 writtenas |     |     |     | 𝜃   |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
variable𝒛.Thus,ifthelatentvariable𝒛canbereliablyinferred
𝒔,𝒂,𝒓,𝒛inplaceswherethereisnoambiguity.
|                                                     |     |     |     |     |     |     |     | fromtherecentexperience,theresultingpolicy𝜋 |     |     | (𝒂|𝒔,𝒛)will |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | ----------- | --- |
| Tothebestofourknowledge,mostofthepreviouslyproposed |     |     |     |     |     |     |     |                                             |     |     | 𝜃           |     |
neuralABRalgorithmsneglectthevariabilityoftransitionprobabil- potentiallyadapttoanewnetworkenvironment.
ity𝑃(i.e.,undertheassumptionthatthethroughputdynamicsstay
Wetraintheaboveinferenceandpolicynetworkswithamodel-free
thesameovertime),thusincorporatingthethroughputinformation approach,byoptimizingtheirparametersviagradientsfromthe
L
duringdownloadofthepastseveralchunkstothestateformulation. samelossfunction 𝑎𝑐𝑡𝑜𝑟.Additionally,itisstraightforwardto
TheagenttrainedwithsuchaformulationcanlearnauniversalABR searchfortheoptimalpolicybyusingavarietyofmethods,suchas
3008

| MM’22,October10–14,2022,Lisboa,Portugal |     |     |     |     |     |     |     |     |     |     |     |     | NuowenKanetal. |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- |
policy-gradientRLorimitationlearning.However,thetrainingdata throughputdynamics,whichwecallthemixeddynamics.Thus,we
areunabletosample(𝒄,𝝉)pairsthatbelongtothesamedynamics
containtoomanydifferenttypesofunderlyingnetworkdynamics
to enable an informative latent representation about the policy. inEq.(4),whichisdifferentfromthetypicalsettingusedinmostof
Tosolvethisissue,amutualinformation-basedregularizationis previousworks.WemustcalculatetheexpectationinEq.(4)over
furtherproposed,inadditiontothebasiclossfunction. trajectoriessampledfromthemixeddynamics,whichcomplicates
theprocessofmeta-policysearchforeachthroughputdynamic.
3.1 ModelingtheUncertaintyofInference
|               |             |     |            |          |          |        |     | 3.2 Meta-PolicySearchonMixedDynamics |     |     |     |     |     |     |
| ------------- | ----------- | --- | ---------- | -------- | -------- | ------ | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
| To facilitate | adaptation, |     | the latent | variable | 𝒛 should | encode | an  |                                      |     |     |     |     |     |     |
Toaddressthechallengeraisedbymixeddynamics,weexplore
| effective | representation |     | of the | current | network | throughput | dy- |     |     |     |     |     |     |     |
| --------- | -------------- | --- | ------ | ------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
thetypesofpolicysearchmethodsthatcanbeemployedinthis
| namics by | exploiting |     | a collection | of past | experienced | network |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ------------ | ------- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
situation,andthendesignamutualinformation-basedregulariza-
| throughputs.Here,wedefinethethroughputcontextas𝒄 |     |     |     |     |     |     | 𝑘−𝑝:𝑘 = |     |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
tiontomakethelatentvariablemoreinformativeaboutthebitrate
| {(𝐶 𝑘−𝑝 ,𝑑 | 𝑘−𝑝 ),···,(𝐶 | 𝑘−1 | ,𝑑 𝑘−1 )}, | which | consists | of the | average |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | ---------- | ----- | -------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
selectionstrategy.
throughputvaluesandtimeintervalsofthroughputmeasurements
Thepolicynetworkapproximatesthemappingfromthelatent
|     |     |     |     |     | 𝑈   | 𝑈   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
c o lle c t e d fr om t h e d o w n lo a d o f c h un k 𝑘 −𝑝 to ch u nk 𝑘 − 1 . I n 𝜋 ( 𝒂 |𝒔 ,𝒛 )
𝒄 𝒄 v ar ia ble and th e st at e t o a n op ti m a l A B R c o n tr o l p o li c y 𝜃 :
| th e f o l lo | w in g, | w e w i ll | o ft e n     | w r i te 𝑘− | 𝑝 :𝑘 as | fo r no        | t at i o n a l | S × 𝑍 ↦→ | A    |            |           |               |                 |                      |
| ------------- | ------- | ---------- | ------------ | ----------- | ------- | -------------- | -------------- | -------- | ---- | ---------- | --------- | ------------- | --------------- | -------------------- |
|               |         |            |              |             |         |                |                |          | . In | g e n e ra | l , R L a | lg o r it h m | s i m p r o v e | t h e p o l ic y b y |
| simplicity.   | Due     | to the     | time-varying | nature      | of      | the underlying |                |          |      |            |           |               |                 |                      |
utilizingtrajectoriesexperiencedwiththesamedynamicstransition
networkthroughputdynamics,weonlycollectthepastexperience
probability𝑃,whilemeta-RLdoesthesamebyoptimizingthepolicy
| fromthemostrecent𝑝 |     |     | chunks,ratherthanfromthebeginning |     |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
foreachdifferenttaskordynamicinturn.However,becauseofthe
ofvideoplayback.Additionally,wemaketheassumptionthatthe
time-varyingcharacteristicofthroughputdynamics,thetrajectories
true chunk sizes will remain relatively constant throughout all (𝒄,𝝉)inourmixeddynamicssituationcannotguaranteetohavethe
v id e o ch un k s fo r e a c h b i t ra teversion,thusomittingthedynamics sametransitionprobability𝑝(𝑠 |𝑠 ,𝑎 ,𝑧 ).Thus,inoursetting
|               |           |           |          |     |     |     |     |     |     |     | 𝑘+1 | 𝑘 𝑘 | 𝑘   |     |
| ------------- | --------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| in fe r en ce | fo r v id | e o c o n | t e n t. |     |     |     |     |     |     |     |     |     |     |     |
off-policyRLalgorithms,suchasSAC[6],willintroducemorebias
Toapproximatetheposterior𝑝(𝒛|𝒄)overlatentvariablespace
intoestimatingthevaluefunctionthanon-policyRLalgorithms.
𝑍,webuildupaninferencenetworkthatgeneratesthedistribution
Thisisbecausetheoff-policyalgorithmscannotestimatethevalue
𝑞 (𝒛|𝒄)parameterizedby𝜙.Thisinferencenetworkcanbetrained
𝜙
functionoftargetpolicybyreusingthetrajectoriesexploredby
viaamodel-freemannerbyusingthemethoddescribedin[16],
|     |     |     |     |     |     |     |     | any other | behavior | policy | that | has encountered | different | types |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------ | ---- | --------------- | --------- | ----- |
withthegoalofdirectlymaximizingavariationallowerbound:
|     |     |         |     |         |     |                |     | of underlying | dynamics. |     | Consequently, |     | it is preferable | to train |
| --- | --- | ------- | --- | ------- | --- | -------------- | --- | ------------- | --------- | --- | ------------- | --- | ---------------- | -------- |
|     |     | (cid:4) |     | (cid:5) |     | (cid:6)(cid:7) |     |               |           |     |               |     |                  |          |
E 𝐽(𝒄,𝝉)+𝛽𝐷 𝑞 (𝒛|𝒄)||𝑝(𝒛) , (4) the meta-policy 𝜋 𝜃 (𝒂|𝒔,𝒛) by using on-policy RL algorithms or
|     | (𝒄,𝝉)∼B |     |     | KL 𝜙 |     |     |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
imitationlearningmethods[7].Werefertotheobjectiveofpolicy
| where𝑝(𝒛)isaunitGaussianpriorover𝑍,and𝐽(𝒄,𝝉)maybeany |     |     |     |     |     |     |     | searchas𝐽˜(𝒄,𝝉). |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
objectivechosenfromavarietyofthoseforpolicysearch,with 𝐽(𝒄,𝝉)
|     |     |     |     |     |     |     |     | As stated | in  | Section | 3.1, the | objective | in  | Eq. (4) can |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------- | -------- | --------- | --- | ----------- |
𝝉 = {𝒔,𝒂,𝒓}beingcorrespondingsamples,aswillbedetailedin
|     |     |     |     |     |     |     |     | be any | objective | function | of meta-policy |     | 𝜋 𝜃 (𝒂|𝒔,𝒛), | including |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | -------- | -------------- | --- | ------------ | --------- |
𝑍
S ec t io n s 3 . 2 a n d 4 . W e a ls o a s s u m e t h e G a us s i a n p o s t er i o r o v er 𝐽 ( 𝒄 , 𝝉 ) = 𝐽˜ (𝒄 , 𝝉 ) . H o w ev e r , t o e n a b le th r o u g h p u t dy n a m i c s t o b e
|     |     |     | 𝑞   | (𝒛 | 𝒄 ) = | N ( 𝑓 𝜇 (𝒄 | ) , 𝑓 𝜎 ( 𝒄 ) | ),  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---------- | ---------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
an d e m p l o y t h e G a u ss ia n f ac t o r 𝜙 𝜙 𝜙 w h ic h i n f o r m a tiv e a b o u t th e m et a - p o li c y i n ou r s et t in g o f m ix e d d y n a m i cs ,
maketheproposedmethodtractable.Asafunctionofthecontext,
weintroduceadditionallyamutualinformationregularizationto
𝑓 (·)(𝒄)predictsthemean𝜇andvariance𝜎for𝑞 (𝒛|𝒄),respectively. theobjective,i.e.,maximizing𝐽(𝒄,𝝉)=𝐽˜(𝒄,𝝉)+𝜆I(𝒂;𝒛|𝒔),where
𝜙
𝜙
Therefore,theinferenceofnetworkthroughputdynamicscanbe 𝜆 ∈ [0,1] isanannealingparameterthatadjuststhestrengthof
donebysamplinglatentvariable𝒛fromtheposteriordistribution regularizationandI(𝒂;𝒛|𝒔)canbeexpressedas:
𝑞 (𝒛|𝒄).Thisposteriorcanreasonaboutuncertaintyassociated
| 𝜙   |     |     |     |     |     |     |     | I(𝒂;𝒛|𝒔)=H(𝒂|𝒔)−H(𝒂|𝒛,𝒔) |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
(5)
withthedynamicsinference,particularlyinlightofthefactthatthe
|     |     |     |     |     |     |     |     |     |     | =−E | [log𝜋(𝒂|𝒔)]+E |     | [log𝜋 (𝒂|𝒔,𝒛)]. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------------- | --- |
underlyingthroughputdynamicsaredifficulttoidentifyduetothe 𝒂 𝒂 𝜃
scarcityofdatasamples,i.e.,epistemicuncertainty.Probabilistic InEq.(5),themutualinformationI(𝒂;𝒛|𝒔)quantifieshowmuch
informationabout𝒂canbeknowngiven𝒛and𝒔.Inotherwords,
| sampling | reduces | the | risk of biased | latent | representation, |     | thus |     |     |     |     |     |     |     |
| -------- | ------- | --- | -------------- | ------ | --------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
increasingthegeneralizationcapabilityofcontrolpolicies.Besides, maximizingthisregularizationentailsincreasingthediversityof
modeling the uncertainty enables a stochastic exploration for policywhenthethroughputdynamicsareuncertain,asmeasured
meta-policyadaptationinresponsetonewenvironments,hence bytheentropyH(𝒂|𝒔),whilemaking𝒛moreinformativeaboutthe
increasingthesampleefficiencyofpolicysearch. bitrateselectionbyminimizingtheentropyH(𝒂|𝒛,𝒔).Additionally,
IntheouterexpectationofEq.(4),thereplaybufferBcontains tosimplifythecomputationof𝜋(𝒂|𝒔),itcanbeestimatedby:
|     |     |     |     |     |     |     |     |     |     | ∫   |     |     | ∫   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
recenthistoricalexperienceofenvironmentinteraction,including
thecontext 𝒄 andthecorrespondingsamples𝝉 = {𝒔,𝒂,𝒓}.Due 𝜋(𝒂|𝒔)= 𝜋 𝜃 (𝒂|𝒔,𝒛)𝑝(𝒛|𝒔)𝑑𝒛≈ 𝜋 𝜃 (𝒂|𝒔,𝒛)𝑝(𝒛)𝑑𝒛 (6)
tothefactthatthethroughputdynamicsinrealworldscenarios (cid:3)
1 𝑁
a re ti m e -v ar y i n g a nd h e te r o g e n eo u s , it i s in f ea s ib l e t o i d e nt i fy ≈ 𝑠 𝑎𝜋 (𝒂|𝒔,𝒛 ), 𝒛 ∼𝑝(𝒛),
|               |            |            |              |             |               |                 |             |        |                                              | 𝑁   | 𝜃     | 𝑖   | 𝑖   |     |
| ------------- | ---------- | ---------- | ------------ | ----------- | ------------- | --------------- | ----------- | ------ | -------------------------------------------- | --- | ----- | --- | --- | --- |
|               |            |            |              |             |               |                 |             |        |                                              | 𝑠𝑎  | 𝑖 = 1 |     |     |     |
| th ed i sti n | ct n e t w | or k th    | ro u g h p u | t d y n a m | ic s fr o m t | h e e n v ir    | o n m e n t |        |                                              |     |       |     |     |     |
|               |            |            |              |             |               |                 |             | where𝑁 | 𝑠𝑎denotesthenumberofsamplesfromtheprior𝑝(𝒛). |     |       |     |     |     |
| of adaptive   | video      | streaming. |              | In other    | worlds,       | in an arbitrary |             |        |                                              |     |       |     |     |     |
trajectory{(𝒄 ,𝝉 ),···,(𝒄 ,𝝉 ),···}frominteractingwith Withthemodel-freeapproach,parameters𝜙
|     | 0:𝑝 | 𝑝   | 𝑘−𝑝:𝑘 | 𝑘   |     |     |     |     |     |     |     |     | ofinferencenet- |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |
the environment, the agent may experience multiple types of workcanbeoptimizedviathebackward-passvector∇𝐽/∇𝒛,i.e.,
3009

ImprovingGeneralizationforNeuralAdaptiveVideoStreamingviaMetaReinforcementLearning MM’22,October10–14,2022,Lisboa,Portugal
∇𝐽/∇𝜙 =∇𝐽/∇𝒛·∇𝒛/∇𝜙.Notethatwecanpassthegradientfrom Algorithm1Meta-trainingProcedureofMERINA
the policy network to inference network with the Gaussian re- Require: Dynamicsmodel𝑓 ofthevideostreamingsystemwith
parameterizationtrick[11],eventhoughthelatentvariableinput time-varyingandheterogeneousnetworkdynamics,learning
ofpolicynetworkissampledfromtheoutputofinferencenetwork, rates𝛼
1
,𝛼
2
,𝛼
3
i.e.,𝒛∼𝑞
𝜙
(𝒛|𝒄).
//Firststage:pre-trainingwithexpertise
4 IMPLEMENTATION 1: InitializereplaybufferB
4.1 Meta-PolicySearchwithDRL 2: while𝑘 <=𝑁 update do
3:
Sample𝑧
𝑘
∼𝑞
𝜙
(𝑧
𝑘
|𝒄
𝑘−𝑝:𝑘
),𝑎
𝑘
∼𝜋
𝜃
(𝑎
𝑘
|𝑠
𝑘
,𝑧
𝑘
)
Toenableaneffectivepolicysearch,webuildupouralgorithm
4:
Obtainthelabel𝑎ˆ𝑘 ∼𝜋𝑒(𝑎
𝑘
|𝑠
𝑘
),add(𝑠
𝑘
,𝒄
𝑘−𝑝:𝑘
,𝑎ˆ𝑘 )toB
ontopoftheproximalpolicyoptimization(PPO)algorithm[19],
5:
Updatethestatewith𝑠
𝑘+1
=𝑓(𝑠
𝑘
,𝑎
𝑘
)
a well known on-policy actor-critic method recognized for its 6: if𝑘 >𝑁 batch then
reliable performance on policy improvement with trust region
7:
Samplebatch𝑏𝑘 ∼Bwithabatchsizeof𝑁
batch
policy optimization. With PPO, we construct two networks: an
8:
L
𝑎𝑐𝑡𝑜𝑟
(𝑏𝑘)=−E
𝒛,𝒂ˆ
log𝜋
𝜃
(𝒂ˆ|𝒔,𝒛)−𝜆I(𝒂;𝒛|𝒔)
actornetwork𝜋 𝜃 (𝒂|𝒔,𝒛)andacriticnetwork𝑉 𝜃𝑣 (𝒔,𝒛).Wejointly
9:
L
𝐾𝐿
(𝑏𝑘)=𝛽𝐷
KL
(𝑞
𝜙
(𝒛|𝒄)||𝑝(𝒛))
traintheinferenceandactornetworkstomaximizetheactorloss 𝜃 ←𝜃−𝛼 ∇ L (𝑏𝑘)
andtheregularizationI(𝒂;𝒛|𝒔)ontheparametersof𝜃 and𝜙.Asa 10:
𝜙 ←𝜙−𝛼
1
∇
𝜃
[L
𝑎𝑐𝑡𝑜𝑟
(𝑏𝑘)+L (𝑏𝑘)]
result,theobjective𝐽˜
𝜃
(𝒄,𝝉)oftheactornetworkisexpressedas: 11: 3 𝜙 𝑎𝑐𝑡𝑜𝑟 𝐾𝐿
(cid:9) (cid:10) (cid:11)(cid:12) 12: endif
𝐽˜ 𝜃 (𝒄,𝝉)=E 𝒛 min 𝜌(𝜃)𝐴ˆ,clip[𝜌(𝜃),1−𝜖,1+𝜖]𝐴ˆ , (7) 13: endwhile
//Secondstage:meta-policyimprovementwithregularizedPPO
𝜌(𝜃)=𝜋 (𝒂|𝒔,𝒛)/𝜋 (𝒂|𝒔,𝒛), 𝒛∼𝑞 (𝒛|𝒄)
𝜃 𝜃(cid:4) 𝜙 14: Fit𝑉 𝜃𝑣 (𝒔,𝒛)followingthecurrent𝜃 and𝜙 viaEq.(8)
where𝜃(cid:4) denotesthepreviousvaluesof𝜃followingthelatestupdate 15: repeat
epoch,clip[𝜌(𝜃),1−𝜖,1+𝜖]ensuresnoincentiveformoving𝜌(𝜃)
16:
InitializereplaybufferB,𝜃(cid:4)=𝜃
outsidetheinterval[1−𝜖,1+𝜖],and𝐴ˆisthetruncatedgeneralized 17: for𝑘 =1,···,𝑁 expdo
advantageestimation(GAE)function[18]generatedfromthevalue 18: Sample𝑧 𝑘 ∼𝑞 𝜙 (𝑧 𝑘 |𝒄 𝑘−𝑝:𝑘 ),𝑎 𝑘 ∼𝜋 𝜃(cid:4) (𝑎 𝑘 |𝑠 𝑘 ,𝑧 𝑘 )
function𝑉
𝜃𝑣
(𝒔,𝒛)and𝒓.Similarly,thecriticlossisformulatedas:
19:
Computethereward𝑟
𝑘
(𝑠
𝑘
,𝑎
𝑘
)
1 (cid:4) (cid:7) 20: Add(𝑠 𝑘 ,𝒄 𝑘−𝑝:𝑘 ,𝑎 𝑘 ,𝑟 𝑘 )toB
L 𝜃𝑣 (𝒄,𝝉)=
2
E 𝒛¯ (𝑉 𝜃𝑣 (𝒔,𝒛¯)−𝐺 𝑘 )2 , 𝒛¯∼𝑞 𝜙 (𝒛|𝒄), (8) 21: Updatethestatewith𝑠 𝑘+1 =𝑓(𝑠 𝑘 ,𝑎 𝑘 )
22: endfor
w th h e e c r u e r 𝐺 re 𝑘 nt = st 𝑟 a 𝑘 te + f 𝛾 o 𝑟 ll 𝑘 o + w 1 i + ng 𝛾2 𝜋 𝑟 𝜃 𝑘 (cid:4) + ( 2 𝒂| + 𝒔, · 𝒛 · ) · ,𝛾 is ∈ th ( e 0, r 1 o ] ll i o s u a t d Q is o c E ou r n et t u fa rn cto o r f 2 2 3 4 : : for Sa 𝑖 m = p 1 l , e · b · a · t , c 𝑁 h u 𝑏𝑖 do ∼Bwithabatchsizeof𝑁 batch
t
c
h
u
a
r
t
re
a
n
tt
t
e
e
n
x
u
p
a
e
t
c
e
t
s
e
e
d
x
Q
po
o
n
E
e
,
n
an
ti
d
al
𝒛
l
¯
y
in
th
d
e
ic
i
a
m
te
p
s
a
t
c
h
t
a
o
t
f
g
f
r
u
a
t
d
u
i
r
e
e
n
a
t
c
s
t
a
io
re
ns
n
o
o
v
t
e
b
r
ei
t
n
h
g
e 25: L
L
𝑎𝑐𝑡𝑜
(𝑏
𝑟
𝑖
(
)
𝑏𝑖
=
)=
𝛽𝐷
−𝐽˜ 𝜃
(
−
𝑞
𝜆
(
I
𝒛|
(
𝒄
𝒂
)
;
|
𝒛
|𝑝
|𝒔
(
)
𝒛
,
)
L
)
𝑐𝑟𝑖𝑡𝑖𝑐 (𝑏𝑖)=L 𝜃𝑣 (𝑏𝑖)
26: 𝐾𝐿 KL 𝜙
computedthroughit.
27:
𝜃 ←𝜃−𝛼
1
∇
𝜃
L
𝑎𝑐𝑡𝑜𝑟
(𝑏𝑖),𝜃
𝑣
←𝜃
𝑣
−𝛼
2
∇
𝜃𝑣
L
𝑐𝑟𝑖𝑡𝑖𝑐
(𝑏𝑖)
𝜙 ←𝜙−𝛼 ∇ [L (𝑏𝑖)+L (𝑏𝑖)]
4.2 ImitationLearning-BasedPre-Training 28: 3 𝜙 𝑎𝑐𝑡𝑜𝑟 𝐾𝐿
29: endfor
Inpractice,duetothelowsampleefficiencyofRLtraining[15],
30: untilConverged
trainingthemeta-RLfromscratchisexceedinglytimeexpensive
and unstable in our setting of mixed dynamics. Therefore, we
pre-traintheparameters𝜙 and𝜃 followingtheimitationlearning Algorithm2Meta-adaptationProcedureofMERINA
methodproposedin[7],withabehaviorcloningobjectiveforthe Require: Testdynamicsmodel𝑓(cid:4) ,learningrates𝛼 1 ,𝛼 2 ,𝛼 3
actorandinferencenetworks: 1: for𝑖 =1,···,𝑁 adapt do
max E 𝒛,𝒂ˆ log𝜋 𝜃 (𝒂ˆ|𝒔,𝒛), 𝒛∼𝑞 𝜙 (𝒛|𝒄), 𝒂ˆ∼𝜋𝑒(𝒂|𝒔), (9) 2: InitializereplaybufferB,𝜃(cid:4)=𝜃
𝜃,𝜙 3: Rollout policy 𝜋 𝜃(cid:4) (𝑎 𝑘 |𝑠 𝑘 ,𝑧 𝑘 ) with 𝑠 𝑘+1 = 𝑓(cid:4)(𝑠 𝑘 ,𝑎 𝑘 ) and
wherethemodel-basedABRalgorithmRobustMPC[24]isadopted collect𝑁 expsamplestoB
toobtaintheexpertpolicy𝜋𝑒(𝒂|𝒔),withtheQoEmaximizedover
//AdaptationwithregularizedPPO
ahorizonoffuture3chunks.Here,weskipthepre-trainingof 4: for𝑖 =1,···,𝑁 udo
critic network, since𝜃 𝑣 may be rapidly converged with only a 5: Samplebatch𝑏𝑖 ∼Bwithabatchsizeof𝑁 batch
few trials following the policy 𝜋 𝜃 (𝒂|𝒔,𝒛). Notably, we employ 6: 𝜃 ←𝜃−𝛼 1 ∇ 𝜃 L 𝑎𝑐𝑡𝑜𝑟 (𝑏𝑖),𝜃 𝑣 ←𝜃 𝑣 −𝛼 2 ∇ 𝜃𝑣 L 𝑐𝑟𝑖𝑡𝑖𝑐 (𝑏𝑖)
RobustMPC here primarily for its good QoE performance and 7: 𝜙 ←𝜙−𝛼 3 ∇ 𝜙 [L 𝑎𝑐𝑡𝑜𝑟 (𝑏𝑖)+L 𝐾𝐿 (𝑏𝑖)]
low computational complexity, which will be also justified by 8: endfor
theexperimentalevaluationsinSection5.However,variantsof 9: endfor
MERINA can be easily fulfilled by adopting other existing ABR
algorithmstoobtaintheexpertpolicy,resultinginadifferenceon
thetrainingtimeandoverallQoEperformance. respectively.WeadoptasimilarNNarchitecturetoPensieve[14]
In summary, the entire meta-training and meta-adaptation fortheactor-criticnetwork,andasimple1-DCNN-basedencoder
workflow of MERINA is given in Algorithm 1 and Algorithm 2, fortheinferencenetwork(seeAppendixAfordetail).
3010

| MM’22,October10–14,2022,Lisboa,Portugal |     |     |     |     |     |     |     |     |     |     | NuowenKanetal. |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- |
5 PERFORMANCEEVALUATION The mean and standard deviation values of these datasets are
Experimentsetup.Toevaluatetheperformanceintermsofthe listedinbottomrowofTable1.Wecombinethesimilardatasets
averagechunkQoE,consistencyandfastadaptationacrossawide FCCand3G/HSDPAintoonedataset(namedF&H),whichisthen
rangeofthroughputpatterns,wetestMERINAonthevirtualplayer usedtovalidatethein-distributionperformanceofdifferentABR
|     |     |     |     |     |     |     | algorithms. | Note that the datasets | 3G/HSDPA, |     | FCC and | Oboe |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------------------- | --------- | --- | ------- | ---- |
aswidelyusedin[1,7,8,10,14],whichsimulatestheadaptivevideo
containonlyasmallamountoftraces,butthethroughputdataof
streamingprocessbyusingthereal-worldnetworkthroughput
datasets,incomparisontootherABRalgorithms.Forthesakeof Pufferisupdateddaily(dataofasingledaytakesuptoseveralGB)
fairness,wealsousethesameenvironmentsettingsasin[7,8,14]: andhasbeenregularlyupdatedsinceJanuary2019.Wedownload
theavailablebitratesetis A = {300,750,1200,1850,2850,4300} alltracesontworandomlychosendates(Oct.17,2021andFeb.
𝐾𝑏𝑝𝑠, 𝐿 = 18,2022),andutilizethemastwoPufferdatasetswithlong-tailed
| the | chunk duration |     | is set as |     | 4 seconds, | the buffer |     |     |     |     |     |     |
| --- | -------------- | --- | --------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
throughputdynamics.Additionally,tomatchwiththelowvideo
occupancyislimitedas1minute,andthetotalnumberofvideo
bitratesettingintheexperiments,weshrinkthethroughputvalues
| chunksis𝐾 | =49.FortheQoEmetricinEq.(2),weadopttwowidely |     |     |     |     |     |     |     |     |     |     |     |
| --------- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofPufferinto1/8oftheiroriginalvalues.
usedsettingsasin[14,21,24]:1)thelinearqualitymetric𝑄𝑜𝐸
𝑙𝑖𝑛
| with𝑞(𝑎 ) | =𝑎 /1000,𝛼 | =1,𝛽 | =4.3;and2)thelog-formquality |     |      |           |                                   |     |     |     |     |     |
| --------- | ---------- | ---- | ---------------------------- | --- | ---- | --------- | --------------------------------- | --- | --- | --- | --- | --- |
| 𝑘         | 𝑘          |      |                              |     |      |           | 5.1 In-DistributionQoEPerformance |     |     |     |     |     |
| metric𝑄𝑜𝐸 | 𝑙𝑜𝑔with𝑞(𝑎 | )    | =log(𝑎 /min(A)),𝛼            |     | =1,𝛽 | =2.66.For |                                   |     |     |     |     |     |
|           |            | 𝑘    | 𝑘                            |     |      |           |                                   |     |     |     |     |     |
WefirstevaluateandcomparetheQoEperformanceofMERINA
thepracticalimplementationofMERINA’smeta-trainingandmeta-
|                                      |     |     |     |                    |     |     | with other | baselines on the | F&H throughput | dataset, | with | the |
| ------------------------------------ | --- | --- | --- | ------------------ | --- | --- | ---------- | ---------------- | -------------- | -------- | ---- | --- |
| adaptation,thediscountfactorissetas𝛾 |     |     |     | =0.99.Theweightsof |     |     |            |                  |                |          |      |     |
lossfunctionaresetas𝛽 =0.02,𝜆 =0.15.Also,welet𝑝 =8,𝜖 = two different QoE metric settings. All throughput traces in the
0.04,𝑁 =10,𝑁 =650,𝑁 =64,𝑁 =2,𝑁 =256,and F&Hdataset,asusedin[7,8,14,24],arerandomlysplitintothree
| 𝑠𝑎  | update |     | batch |     | 𝑢 𝑒𝑥𝑝 |     |     |     |     |     |     |     |
| --- | ------ | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
setthelearningratesas𝛼 = 𝛼 = −5,𝛼 = −4.Ourcodeis partitions:training,validationandtestsets.Thelearning-based
|     |     |     | 1 3 | 10  | 2 10 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
methods(MERINA,Pensieve,Comyco,FuguandBayesMPC)are
availableathttps://github.com/confiwent/merina.
trainedonthetrainingsetandevaluatedonthevalidationset.By
Baselinealgorithms.WecompareMERINAwiththefollowing
sixstate-of-the-artABRalgorithms.1)BOLA[21]:abuffer-based choosingtheNNsweightsthatperformbestonthevalidationset,
theperformanceofallcomparisonalgorithmsisthentestedonthe
| algorithm | that uses | Lyapunov | optimization |     | to determine | the |     |     |     |     |     |     |
| --------- | --------- | -------- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
testset.NotethattheQoEperformancemayslightlyvarywith
optimalbitrateversionundertheconstraintofbufferoccupancy
|     |     |     |     |     |     |     | the random | traces selection | and unstable | NNs training, |     | so it is |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------- | ------------ | ------------- | --- | -------- |
only.2)RobustMPC[24]:amodel-basedalgorithmthatsolves
naturaltonoticesomediscrepanciesbetweenearlierworksand
theoptimizationprobleminEq.(3)withahorizonofthefutureℎ
videochunksundertheframeworkofmodelpredictivecontrol.The ours.Wesimulatetheplaybackofthesamevideoonceforeach
throughputtrace(referredtoasasession),andthencollectQoE
futurethroughputispredictedbytheharmonicmeanofaverage
valuesofallchunksforcomparison.Sincethetestandtrainingsets
throughputmeasurementsofthepast5downloadedchunks.3)
sharethesamedistributionofthroughouttraces,wecalltheresults
Pensieve[14]:aDRL-basedalgorithmthatusestheA3Calgorithm
in-distributionQoEperformance.
tolearnanoptimalneuralmappingfromthedynamicsofbuffer
occupancy,throughputandchunksizetotherateadaptationofthe Figs.2(a)and2(d)depictthecumulativedistributionfunctions
(CDFs)ofallsessions’averageQoEforallalgorithms.TheCDFs
nextchunk.4)Comyco[7,8]:amodel-freeneuralABRalgorithm
inFigs.2(b)and2(e)illustratetheQoEimprovementsoftheother
| that uses | NNs to | directly | approximate | the | offline near-optimal |     |     |     |     |     |     |     |
| --------- | ------ | -------- | ----------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
algorithmsoverRobustMPCinallsessions.Andthebargraphsin
expertsolutionbylifelongimitationlearning.5)Fugu[23]:amodel-
Figs.2(c)and2(f)showtheaveragechunkQoEandeachindividual
basedalgorithmthatusesNN-basedtransmissiontimepredictorto
componentsinEq.(2),wheretheerrorbarsspan±onestandard
predicttheprobabilitydistributionofdownloadtimesperbitrate
versionforfutureℎ chunks,andoptimizesthebitrateselection deviation from the average value. The key observation is that
viacalculatingtheexpectationofmaximumfutureℎ-horizonQoE MERINAoutperformstheotherbaselinealgorithmsintermsof
theaveragechunkQoEvaluewithboththelinearandlog-form
| return. 6) | BayesMPC | [10]: | a model-based |     | algorithm | that uses |             |                       |     |              |             |     |
| ---------- | -------- | ----- | ------------- | --- | --------- | --------- | ----------- | --------------------- | --- | ------------ | ----------- | --- |
|            |          |       |               |     |           |           | QoE metrics | on the F&H throughput |     | dataset. The | performance |     |
BayesianNNstopredictthelowerboundoffuturethroughputs,
gapoftheaveragechunkQoEbetweenMERINAandthebaseline
basedonwhichamodelpredictivecontrolisfurtheremployedto
|                                      |     |     |     |     |     |     | algorithmsisatleast3%and4%for𝑄𝑜𝐸 |     | 𝑙𝑖𝑛and𝑄𝑜𝐸 |                   |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --------- | ----------------- | --- | --- |
| optimizethefutureℎ-horizonQoEreturn. |     |     |     |     |     |     |                                  |     |           | 𝑙𝑜𝑔,respectively. |     |     |
AndComycobeatstheremainingbaselinealgorithmsintermsof
NotethatFuguisproposedtolearninsitu,whichisalsoproposed
QoE(slightlybetterthanPensieve),demonstratingtheeffectiveness
in[23]andsaidtobeamoresoundvirtualplayerthantheone
|     |     |     |     |     |     |     | of imitation | learning. As for | the variance | of the | results | for all |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------------- | ------------ | ------ | ------- | ------- |
employedinourpaper.Duetothefactthatthesimulationplatform
sessions,BOLAhastheloweststandarddeviation(0.72for𝑄𝑜𝐸
haslittleeffectonthesuccessofMERINAintermsofgeneralization, 𝑙𝑖𝑛
and0.65for𝑄𝑜𝐸
wechoosethevirtualplayerthatiswidelydeployedinthemajority 𝑙𝑜𝑔)buttheworstaverageQoE,whereasMERINA
alsoperformswell,withastandarddeviationof0.87and0.71for
ofpriorworks.Therefore,were-implementFuguandutilizeitasa
|     |     |     |     |     |     |     | 𝑄𝑜𝐸 𝑙𝑖𝑛and𝑄𝑜𝐸 | 𝑙𝑜𝑔,respectively.Inaddition,theresultsalsoreveal |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------------------------------------------------ | --- | --- | --- | --- |
baselineABRalgorithmthatoptimizestheexpectationofQoEwith
thatMERINAperformsrobustlythroughoutallsessions,witha
aprobabilisticdownloadtimepredictor.Additionally,theplanning
largestproportionofsessionsachievingahigherQoE.Forinstance,
horizonofRobustMPC,FuguandBayesMPCissettoℎ=3chunks.
Datasetsofnetworkthroughput.Wecollectfourpublicreal- Figs. 2(a) and 2(d) show that at least 95% of MERINA sessions
achieveanaverageQoEgreaterthan0.TheresultsinFig.2(b)and
worldnetworkthroughputdatasets(3G/HSDPA[17],FCC[2],Oboe
Fig.2(e)verifythatinabout80%ofsessions,MERINAoutperforms
[1],Puffer[23])tosimulatevarioususerandnetworkconditions.
RobustMPC,andintheworstcasetheaverageQoEofMERINA
3011

ImprovingGeneralizationforNeuralAdaptiveVideoStreamingviaMetaReinforcementLearning MM’22,October10–14,2022,Lisboa,Portugal
1.4
|     |     |     |     |     |     |     |     |     |     | BOLA | RobustMPC |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --------- | --- |
1.2
|     |     |     |     |     | eulav(cid:3)(cid:3)egarevA | 1   |     |     |     | Pensieve | Comyco   |     |
| --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | -------- | -------- | --- |
|     |     |     |     |     |                            |     |     |     |     | Fugu     | BayesMPC |     |
0.8
|     |                                                                                 |     |     | (cid:35)(cid:70)(cid:85)(cid:85)(cid:70)(cid:83)(cid:1)(cid:30)(cid:30)(cid:31) |     |       |     |     |     | MERINA |     |     |
| --- | ------------------------------------------------------------------------------- | --- | --- | ------------------------------------------------------------------------------- | --- | ----- | --- | --- | --- | ------ | --- | --- |
|     | (cid:35)(cid:70)(cid:85)(cid:85)(cid:70)(cid:83)(cid:1)(cid:30)(cid:30)(cid:31) |     |     |                                                                                 |     | 0 . 6 |     |     |     |        |     |     |
|     |                                                                                 |     |     |                                                                                 |     | 0 . 4 |     |     |     |        |     |     |
0.2
0
|     |           |     |           |     |     | ChunkQoE |     | Bitrateutility | Rebufferingpenalty |     | Smoothnesspenalty |     |
| --- | --------- | --- | --------- | --- | --- | -------- | --- | -------------- | ------------------ | --- | ----------------- | --- |
|     | (a)𝑄𝑜𝐸𝑙𝑖𝑛 |     | (b)𝑄𝑜𝐸𝑙𝑖𝑛 |     |     |          |     |                | (c)𝑄𝑜𝐸𝑙𝑖𝑛          |     |                   |     |
1.4
|     |     |     |     |     |     |     |     |     |     | BOLA | RobustMPC |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --------- | --- |
1.2
|     |     |     |     |     | eulav(cid:3)(cid:3)egarevA |     |     |     |     | Pensieve | Comyco |     |
| --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | -------- | ------ | --- |
1
|     |                                                                                 |     |     |                                                                                 |     | 0.8   |     |     |     | Fugu   | BayesMPC |     |
| --- | ------------------------------------------------------------------------------- | --- | --- | ------------------------------------------------------------------------------- | --- | ----- | --- | --- | --- | ------ | -------- | --- |
|     |                                                                                 |     |     | (cid:35)(cid:70)(cid:85)(cid:85)(cid:70)(cid:83)(cid:1)(cid:30)(cid:30)(cid:31) |     |       |     |     |     | MERINA |          |     |
|     | (cid:35)(cid:70)(cid:85)(cid:85)(cid:70)(cid:83)(cid:1)(cid:30)(cid:30)(cid:31) |     |     |                                                                                 |     | 0 . 6 |     |     |     |        |          |     |
|     |                                                                                 |     |     |                                                                                 |     | 0 . 4 |     |     |     |        |          |     |
0.2
0
|     |           |     |           |     |     | ChunkQoE |     | Bitrateutility | Rebufferingpenalty |     | Smoothnesspenalty |     |
| --- | --------- | --- | --------- | --- | --- | -------- | --- | -------------- | ------------------ | --- | ----------------- | --- |
|     | (d)𝑄𝑜𝐸𝑙𝑜𝑔 |     | (e)𝑄𝑜𝐸𝑙𝑜𝑔 |     |     |          |     |                | (f)𝑄𝑜𝐸𝑙𝑜𝑔          |     |                   |     |
Figure2:PerformancecomparisonofdifferentABRalgorithmsintermsoftheaveragechunkQoEvalueandtheindividual
QoEcomponentswiththeQoEmetrics𝑄𝑜𝐸 𝑙𝑖𝑛and𝑄𝑜𝐸 𝑙𝑜𝑔onF&H(FCCandHSDPA)throughputdataset.
Table1:PerformancecomparisonofdifferentABRalgorithmsintermsoftheaveragechunk𝑄𝑜𝐸
𝑙𝑜𝑔valueondifferentdatasets.
Mean±std(𝑅𝑔𝑎𝑝)
|     |     |     | FCC |     | HSDPA |     |     | Oboe | Puffer-Oct.17-21 |     | Puffer-Feb.18-22 |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | ---- | ---------------- | --- | ---------------- | --- |
BOLA 0.95±0.63(−17%) 1.11±0.64(−9%) 1.63±0.66(−11%) 0.88±1.29(+20%) 0.75±1.93(−14%)
|     |     |     | 1.05±0.63(−8%) |     | 1.16±0.85(−5%) |     | 1.79±0.73(−2%) |     | 0.76±1.48(+5%) |     | 0.86±2.01(−2%) |     |
| --- | --- | --- | -------------- | --- | -------------- | --- | -------------- | --- | -------------- | --- | -------------- | --- |
RobustMPC
Pensieve 1.07±0.62(−7%) 1.21±0.68(−1%) 1.75±0.69(−4%) 0.40±7.17(−46%) 0.66±5.40(−25%)
|     |     |     | 1.11±0.63(−3%) |     | 1.22±0.78(−0%) |     | 1.76±0.77(−3%) |     | −0.22±2.20(−130%) |     | 0.65±2.25(−26%) |     |
| --- | --- | --- | -------------- | --- | -------------- | --- | -------------- | --- | ----------------- | --- | --------------- | --- |
Comyco
Fugu 1.04±0.70(−10%) 1.16±0.80(−5%) 1.71±0.78(−6%) 0.54±1.55(−26%) 0.77±1.94(−12%)
|     |     |     | 1.05±0.78(−9%) |     | 1.09±0.84(−2%) |     | 1.78±0.74(−2%) |     | 0.54±1.88(−26%) |     | 0.76±2.20(−14%) |     |
| --- | --- | --- | -------------- | --- | -------------- | --- | -------------- | --- | --------------- | --- | --------------- | --- |
BayesMPC
|     | MARINA |     | 1.15±0.66 |     | 1.22±0.85 |     | 1.82±0.70 |     | 0.73±1.63 |     | 0.88±2.00 |     |
| --- | ------ | --- | --------- | --- | --------- | --- | --------- | --- | --------- | --- | --------- | --- |
MERINA(nMIwith𝜆=0,seeAppendixB.3) 1.05±0.65(−9%) 1.19±0.71(−2%) 1.74±0.69(−4%) 0.71±1.58(−2%) 0.83±1.96(−5%)
Datasetdistribution 1.13±0.44Mbps 1.61±0.95Mbps 2.60±2.08Mbps 1.85±0.91Mbps 1.60±0.88Mbps
isjust0.3lessthanRobustMPC’s.Furthermore,thebargraphsin
demonstratetheconsistencyofallalgorithms’performanceona
Figs.2(c)and2(f)indicatethatMERINAcansurprisinglyachievelow subsetofthetrainingthroughputdynamicsdistribution.
rebufferingandsmoothnesspenalties,similartothoseofPensieve. TheresultsonFCCandHSDPAtracesshowthatthelearning-
Whileotheralgorithmsresultineitheralongerrebufferingtime, based baselines perform worse on FCC traces than on HSDPA
asComycodoes,orahigherqualityfluctuation,asBOLAdoes, traces,indicatingthattrainingthesealgorithmsonmixeddynamics
duringthevideoplayback.Notethattheresultsobtainedforlinear isunlikelytoresultintheacquisitionofexpertisethatperforms
QoEmetric𝑄𝑜𝐸
𝑙𝑖𝑛 aresimilartothoseforlog-formQoEmetric uniformlyacrossallexperienceddynamics.Theresultsonout-of-
𝑄𝑜𝐸 𝑙𝑜𝑔w.r.t.allcomparisonalgorithms.Therefore,weonlyshow distribution datasets (Oboe, Puffer-Oct.17-21 and Puffer-Feb.18-
and compare the performance for𝑄𝑜𝐸 in the following, and 22) reveal that the NN weights trained in F&H datasets using
𝑙𝑜𝑔
moveresultsof𝑄𝑜𝐸 𝑙𝑖𝑛toAppendixBduetopagelimit. MERINAprovidethehighestdegreeofconsistencyorgeneralization
performanceamongthelearning-basedbaselines,overallranges
5.2 ConsistencyonOut-of-DistributionTraces ofvaryingthroughputdynamics.TheheuristicABRalgorithms
(BOLAandRobustMPC)canalwaysachieveasatisfactoryQoE
| To study | the consistency | of MERINA | in comparison | to  | other |     |     |     |     |     |     |     |
| -------- | --------------- | --------- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
performanceondifferentthroughputdynamics,whileBOLAbeats
learning-basedmethods,wemeasuretheirperformanceonout-
|     |     |     |     |     |     | all the | other | algorithms | on Puffer-Oct.17-21 |     | traces | where the |
| --- | --- | --- | --- | --- | --- | ------- | ----- | ---------- | ------------------- | --- | ------ | --------- |
of-distributiondatasetsOboe,Puffer-Oct.17-21andPuffer-Feb.18-
|     |     |     |     |     |     | throughput |     | dynamics | are difficult | to predict | and considerably |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ------------- | ---------- | ---------------- | --- |
22(i.e.,withadifferentdistributionofthroughputdynamicsthan
|     |     |     |     |     |     | deviate | from | those | on the F&H | traces. | In contrast, | the other |
| --- | --- | --- | --- | --- | --- | ------- | ---- | ----- | ---------- | ------- | ------------ | --------- |
F&Hdataset)byusingthesameNNweightsobtainedinSection
learning-basedmethodsfailtogeneralizetotheout-of-distribution
5.1(i.e.,learnedfromtheF&Hdataset).WeshowinTable1the
datasets,verifyingthegeneralizationdifficultyofDRLorimitation
numericalresultsthatarecomposedoftheaveragechunkQoE
learning-basedneuralABRalgorithms.Concretely,themodel-free
value±onestandarddeviationforallthecomparisonalgorithms
andtheperformancegap𝑅 = [(𝑟−𝑟∗)/𝑟∗]×100%tothevalue neuralalgorithms(e.g.,PensieveandComyco)sufferfromretaining
𝑔𝑎𝑝
ofMERINA,where𝑟∗ istheaveragechunkQoEofMERINAand𝑟 theircapabilityonOboetraceswhiledegradingsignificantlyon
is
Puffertraces,particularlyonthePuffer-Oct.17-21dataset.While
theaveragechunkQoEofeachcomparisonalgorithm.Additionally,
themodel-basedalgorithms(e.g.,FuguandBayesMPC)thatuse
Table1alsoincludesresultsfromtheFCCandHSDPAdatasetsto
3012

| MM’22,October10–14,2022,Lisboa,Portugal |      |           |        |     |        |     |     |     |     |     |     |     | NuowenKanetal. |
| --------------------------------------- | ---- | --------- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | -------------- |
|                                         | BOLA | RobustMPC | Comyco |     | MERINA |     |     |     |     |     |     |     |                |
eulav  egarevA 3
2.5
2
1.5
1 (cid:35)(cid:70)(cid:85)(cid:85)(cid:70)(cid:83)(cid:1)(cid:30)(cid:30)(cid:31)
0.5
0
|     |     | 4G  | Public WiFi | International Link |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure3:Comparisonof𝑄𝑜𝐸
𝑙𝑜𝑔withoutadaption.
|     |     |     |     |     |     |     |     | (a)AdaptationCurves |     |     | (b)Puffer-Oct.17-21 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------------------- | --- | --- |
NNstolearnthethroughputdynamicshaveabetterconsistency
Figure4:a)TheadaptationcurvesofMERINAandComyco,
or generalization than Pensieve and Comyco, though they also andb)averagechunk𝑄𝑜𝐸 𝑙𝑜𝑔improvementoverRobustMPC.
performmuchworseonPuffertracesthanheuristicmethods.This
Fig.4(a)demonstratesthatMERINAcanoutperformRobustMPC
demonstratesthat,besidesmeta-RL-basedmethods,model-based
methodsareanotherviableparadigmforaddressingthegeneral- with only a few of epochs, and achieve a QoE performance
izationchallengeofadaptivevideostreaming.Inconclusion,our comparabletothatofBOLA(performsbestinthisdataset)with
around200trainingepochs(lastingabout10minutes).Toverify
MERINAperformsconsistentlywithout-of-distributionthroughput
theperformancefurther,weshowtheCDFsofQoEimprovement
dynamics,thoughitmayhaveaworseQoEthanBOLAinsome
|     |     |     |     |     |     |     | of comparison | algorithms |     | over | RobustMPC | in  | Fig. 4(b), with |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | --- | ---- | --------- | --- | --------------- |
sessions.Moreimportantly,MERINAcanfurtherrapidlyadaptto
thenewthroughputdynamicsviaafewupdates(seeSection5.3). MERINA-Offline, MERINA-Adp-30 and MERINA-Adp-200
Real-WorldTest.WethenevaluateMERINA,Comyco(thestate- denotingtheproposedalgorithmthatemploystheNNweights
|     |     |     |     |     |     |     | without | adaptation, | after | 30-epoch | adaptation, |     | and after 200- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ----- | -------- | ----------- | --- | -------------- |
of-the-artmodel-freeABRalgorithm)andtheheuristicalgorithms
|           |           |             |                   |          |       |          | epoch adaptation, |             | respectively. |            | The results | indicate | that after   |
| --------- | --------- | ----------- | ----------------- | -------- | ----- | -------- | ----------------- | ----------- | ------------- | ---------- | ----------- | -------- | ------------ |
| BOLA and  | RobustMPC |             | in the real world | platform | under | three    |                   |             |               |            |             |          |              |
|           |           |             |                   |          |       |          | 30-epoch          | adaptation, | the           | proportion | of          | sessions | that achieve |
| different | network   | conditions: | a 4G cellular     | network, |       | a public |                   |             |               |            |             |          |              |
WiFinetworkoncampus,andawideareanetworkconnecting much lower/higher QoE value than RobustMPC significantly
ShanghaiandLosAngeles,withmeanandstandarddeviationof decreases/increases. And after 200-epochs adaptation, MERINA
recordedthroughputvaluesof5.74±0.39𝑀𝑏𝑝𝑠,2.04±0.89𝑀𝑏𝑝𝑠 has a similar distribution to BOLA, in terms of average QoE
and1.78±1.10𝑀𝑏𝑝𝑠.Thereal-worldplatformbasedonDash.js improvement.WhileComyco’sperformancecannotbeimproved
rapidlyduetoitslowinitialperformance,andalsobecausethe
[4]isimplementedsimilarlytothatin[7,14],andwethusomitits
descriptionforsimplicity.Thesametestvideoisloadedrepeatedly lifelonglearningmethodcannotensurepolicyimprovementina
on each network using a randomly chosen ABR scheme. Each significantlychangedenvironment.Theasymptoticperformanceof
MERINAindicatesthatitcanachieveasuperiorQoEperformance
experimenttakesabout1hourtocomplete,andtheNNsweights
whencomparedtoallbaselinesfollowingameta-adaptationpro-
| for MERINA | and | Comyco | are all trained | on  | F&H dataset. | The |     |     |     |     |     |     |     |
| ---------- | --- | ------ | --------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
cedure,implyingthatMERINAcanachievethebestgeneralization
| results in | Fig. 3 | illustrates | that MERINA | performs | similarly | to  |     |     |     |     |     |     |     |
| ---------- | ------ | ----------- | ----------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
performanceandwilloutperformbaselinealgorithmsacrossarange
RobustMPC,andoutperformsBOLAandComycoonthesenew
networkenvironments.WhileComycoperformstheworstunder ofthroughputdynamicsthroughtheadaptation.
publicWiFiandinternationallinkconditions.
6 CONCLUSION
5.3 FastAdaptationtoNewEnvironments Wehaveproposedthemeta-RL-basedadaptivevideostreaming
systemMERINAtolearnageneralizedABRalgorithm.Specifically,
Section5.2exhibitsthesatisfactoryconsistencyperformanceof
|     |     |     |     |     |     |     | we introduced | a   | model-free | context-based |     | system | framework, |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | ------------- | --- | ------ | ---------- |
MERINAwhenconfrontedwithsomeunseenthroughoutdynamics,
|     |     |     |     |     |     |     | composed | of a probabilistic |     | inference | network | (latent | encoder) |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------------ | --- | --------- | ------- | ------- | -------- |
andrevealsthatMERINAwilldegradeperformanceontraceswith
thatinferredtheunderlyingdynamicsfromtherecentthroughput
dynamicsthataresignificantlydifferentfromthoseinthetraining
dataset.Hence,weexaminehereMERINA’sabilitytorapidlyadapt context,andalatent-conditionedpolicynetworkthatlearnedto
rapidlyadapttounfamiliarthroughputdynamics.Weimplemented
| to these | unfamiliar | throughput | dynamics | by  | investigating | the |     |     |     |     |     |     |     |
| -------- | ---------- | ---------- | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
themeta-trainingandmeta-adaptationproceduresforMERINA,
| performance | of  | meta-adaption | procedure | given | in Algorithm | 2.  |     |     |     |     |     |     |     |
| ----------- | --- | ------------- | --------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
anddemonstrateditsefficiencythroughempiricalevaluationson
| Fig. 4 depicts | the | performance | of an | adaptation | procedure | that |     |     |     |     |     |     |     |
| -------------- | --- | ----------- | ----- | ---------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
multipledatasetsandareal-worldplatform.Theproposedidea
seekstofine-tunetheexistingNNweightsofMERINAandComyco
utilizingtracesfromPuffer-Oct.17-21dataset.Thetesttracesof forMERINAisnotlimitedtothethroughputdynamics.It,infact,
canbeextendedtovideocontent(e.g.,eachvideochunkmaybe
| Puffer-Oct.17-21 |     | used in | Section 5.2 are | also used | to  | assess the |     |     |     |     |     |     |     |
| ---------------- | --- | ------- | --------------- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
encodedwithdifferentrate-distortioncurvesw.r.t.videocontent),
| performance | of  | comparison | algorithms, | and the | training | traces |     |     |     |     |     |     |     |
| ----------- | --- | ---------- | ----------- | ------- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
whichwillbeoneofourfutureresearchdirections.
| are additional | data | collected | on the | same day. | Comyco | is fine- |     |     |     |     |     |     |     |
| -------------- | ---- | --------- | ------ | --------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
turnedusingthesuggestedlifelonglearningmethod(Comyco-
ACKNOWLEDGMENTS
Lifelong)in[7].WerefertoMERINAduringthemeta-adaptation
ThisworkwassupportedinpartbyNSFCunderGrants61931023,
procedureasMERINA-Adapt,anditsasymptoticperformanceof
61831018,61871267,62120106007,61972256,T2122024,62125109,by
adaptation(i.e.,afterconvergingtotheoptimum)asMERINA-Asy.
ShanghaiRising-StarProgram20QA1404600andSJTU-UCLGlobal
Inatrainingepoch,theNNweightsareupdatedtwice,whileeach
updateiswithabatchsizeof64samples. StrategicPartnershipFund.(Correspondingauthor:ChenglinLi.)
3013

ImprovingGeneralizationforNeuralAdaptiveVideoStreamingviaMetaReinforcementLearning MM’22,October10–14,2022,Lisboa,Portugal
REFERENCES [13] HongziMao,ShannonChen,DrewDimmery,ShaunSingh,DrewBlaisdell,
[1] ZahaibAkhtar,YunSeongNam,RameshGovindan,SanjayRao,JessicaChen, YuandongTian,MohammadAlizadeh,andEytanBakshy.2020. Real-world
EthanKatz-Bassett,BrunoRibeiro,JibinZhan,andHuiZhang.2018. Oboe: VideoAdaptationwithReinforcementLearning. arXiv:2008.12858[cs.NI]
Auto-TuningVideoABRAlgorithmstoNetworkConditions.InProceedingsof [14] HongziMao,RaviNetravali,andMohammadAlizadeh.2017.NeuralAdaptive
theConferenceoftheACMSpecialInterestGrouponDataCommunication.44–58. VideoStreamingwithPensieve.InProceedingsoftheConferenceoftheACM
[2] FederalCommunicationsCommission.2016.RawData-MeasuringBroadband SpecialInterestGrouponDataCommunication.197–210.
America.(2016). https://www.fcc.gov/reports-research/reports/measuring- [15] AnushaNagabandi,GregoryKahn,RonaldS.Fearing,andSergeyLevine.2018.
broadband-america/raw-data-measuring-broadband-america-2016 NeuralNetworkDynamicsforModel-BasedDeepReinforcementLearningwith
[3] ChelseaFinn,PieterAbbeel,andSergeyLevine.2017. Model-agnosticmeta- Model-FreeFine-Tuning.In2018IEEEInternationalConferenceonRoboticsand
learningforfastadaptationofdeepnetworks.InInternationalconferenceon Automation(ICRA).7559–7566.
machinelearning.PMLR,1126–1135. [16] KateRakelly,AurickZhou,ChelseaFinn,SergeyLevine,andDeirdreQuillen.
[4] DashIndustryForum.2022. CatalyzingtheAdoptionofMPEG-DASH. https: 2019.EfficientOff-PolicyMeta-ReinforcementLearningviaProbabilisticContext
//dashif.org/ Variables.InProceedingsofthe36thInternationalconferenceonmachinelearning.
[5] MatteoGadaleta,FedericoChiariotti,MicheleRossi,andAndreaZanella.2017. 5331–5340.
D-DASH:ADeepQ-LearningFrameworkforDASHVideoStreaming. IEEE [17] HaakonRiiser,PaulVigmostad,CarstenGriwodz,andPålHalvorsen.2013.
TransactionsonCognitiveCommunicationsandNetworking3,4(2017),703–718. CommutePathBandwidthTracesfrom3GNetworks:AnalysisandApplications.
[6] TuomasHaarnoja,AurickZhou,PieterAbbeel,andSergeyLevine.2018. Soft InProceedingsofthe4thACMMultimediaSystemsConference.114–118.
Actor-Critic:Off-PolicyMaximumEntropyDeepReinforcementLearningwitha [18] JohnSchulman,PhilippMoritz,SergeyLevine,MichaelJordan,andPieterAbbeel.
StochasticActor.InProceedingsofthe35thInternationalConferenceonMachine 2018. High-DimensionalContinuousControlUsingGeneralizedAdvantage
Learning.1861–1870. Estimation. arXiv:1506.02438[cs.LG]
[7] TianchiHuang,ChaoZhou,XinYao,RuixiaoZhang,ChengleiWu,BingYu, [19] JohnSchulman,FilipWolski,PrafullaDhariwal,AlecRadford,andOlegKlimov.
andLifengSun.2020. Quality-AwareNeuralAdaptiveVideoStreamingWith 2017.ProximalPolicyOptimizationAlgorithms. arXiv:1707.06347[cs.LG]
LifelongImitationLearning.IEEEJournalonSelectedAreasinCommunications [20] I.Sodagar.2011.TheMPEG-DASHStandardforMultimediaStreamingOverthe
38,10(2020),2324–2342. Internet.IEEEMultiMedia18,4(2011),62–67.
[8] TianchiHuang,ChaoZhou,Rui-XiaoZhang,ChengleiWu,XinYao,andLifeng [21] KevinSpiteri,RahulUrgaonkar,andRameshSitaraman.2016. BOLA:Near-
Sun.2019. Comyco:Quality-AwareAdaptiveVideoStreamingviaImitation OptimalBitrateAdaptationforOnlineVideos.InProceedingsofthe35thAnnual
Learning.InProceedingsofthe27thACMInternationalConferenceonMultimedia IEEEInternationalConferenceonComputerCommunications.1–9.
(Nice,France)(MM’19).429–437. [22] YiSun,XiaoqiYin,JunchenJiang,VyasSekar,FuyuanLin,NanshuWang,
[9] AppleInc.2022.HTTPLiveStreaming. https://developer.apple.com/streaming/ TaoLiu,andBrunoSinopoli.2016. CS2P:ImprovingVideoBitrateSelection
[10] NuowenKan,ChenglinLi,CaiyiYang,WenruiDai,JunniZou,andHongkaiXiong. andAdaptationwithData-DrivenThroughputPrediction.InProceedingsofthe
2021.Uncertainty-AwareRobustAdaptiveVideoStreamingwithBayesianNeural ConferenceoftheACMSpecialInterestGrouponDataCommunication.272–285.
NetworkandModelPredictiveControl.InProceedingsofthe31stACMWorkshop [23] FrancisY.Yan,HudsonAyers,ChenzhiZhu,SadjadFouladi,JamesHong,Keyi
onNetworkandOperatingSystemsSupportforDigitalAudioandVideo(Istanbul, Zhang,PhilipLevis,andKeithWinstein.2020.Learninginsitu:ARandomized
Turkey)(NOSSDAV’21).17–24. ExperimentinVideoStreaming.InProceedingsofthe17thUSENIXSymposium
[11] DiederikPKingmaandMaxWelling.2013.Auto-EncodingVariationalBayes. onNetworkedSystemsDesignandImplementation(NSDI20).495–511.
arXiv:1312.6114[cs.LG] [24] XiaoqiYin,AbhishekJindal,VyasSekar,andBrunoSinopoli.2015.AControl-
[12] ClareLyle,MarkRowland,andWillDabney.2022.UnderstandingandPreventing TheoreticApproachforDynamicAdaptiveVideoStreamingoverHTTP.In
Capacity Loss in Reinforcement Learning. In Proceedings of International Proceedings of the 2015 ACM Conference on Special Interest Group on Data
Communication.325–338.
ConferenceonLearningRepresentations.1–12.
3014

MM’22,October10–14,2022,Lisboa,Portugal NuowenKanetal.
Appendix A.3 VirtualPlayer
Thevirtualplayer,withreferencetotheopen-sourcedABRsimula-
A IMPLEMENTATIONDETAILS torusedbyPensieveandComyco,includesthreekeycomponents:
1)avideoclientthatemulatesthevideoplaybackandthebufferoc-
WeimplementMERINAonadesktopequippedwitha40-coreIntel
cupancy;2)avideodeliverysimulatorthatemulatesthedownload
XeonSilver4114Processor,64GBDDR4DRAMandanNVIDIA
ofavailablevideochunksfromthevideoservertotheclient,under
GeForceRTX2080graphicscard.Theinferenceneuralnetwork
networkconditionsthatareemulatedfromourstateddatasetsof
andthepolicyneuralnetworkthatconsistsofanactornetwork
networkthroughput,alongwithan80msRTTandapacketlossrate
andacriticnetworkareconstructedandtrainedonPyTorch-1.9.0.
of0.95;and3)anABRcontrollerthatemploystheABRalgorithms
NotethatwetrainMERINAontheGPUtomaximizetheefficiency,
(e.g.,MERINAandotherbaselinealgorithms)todecidetheruleof
thoughitcanbetrainedonCPUsaswell.
whichbitrateversionbeingrequestedforthenextrequestedvideo
chunkthathasnotbeendownloadedyet.
A.1 InferenceNetwork
The whole video streaming process can be summarized as
Thethroughputcontext𝒄 𝑘−𝑝:𝑘 ={(𝐶 𝑘−𝑝 ,𝑑 𝑘−𝑝 ),···,(𝐶 𝑘−1 ,𝑑 𝑘−1 )} follows. At the beginning of video streaming, the video client
includes the average throughput values and time intervals of firstobtainsthevideoinformation,includingthenumberoftotal
throughputmeasurementscollectedfromthedownloadofprevious videochunksandtheavailablebitratesforcorrespondingchunks.
𝑝 chunks. In this paper, we set 𝑝 = 8 and input the context Theclientthenrequestsvideochunksonebyone,usingtheABR
informationof𝑈 𝑘−8 untilchunk𝑈 𝑘−1 (i.e.,{𝐶 𝑘−8 ,···,𝐶 𝑘−1 }and controllertoselectthebitrateforfuturechunks.Therequested
{𝑑 𝑘−8 ,···,𝑑 𝑘−1 })separatelyintotwoone-dimensionalconvolution bitrate version of chunks are downloaded through the video
layerswith128filtersofsize4withstride1.Theresultsofthese deliverysimulator.Oncecompletelydownloaded,avideochunkis
twoconvolutionlayersarethenmergedintoafullyconnectedlayer playedbacktotheclient.Theplaybackinformation,suchasbuffer
with512neurons,followedbyaLeakyReLUactivationfunction. occupancy,rebufferingevent,bitrateversionofthecurrentchunk,
Thecollectedfeaturesarefinallyfedintotheoutputlayer,which iscollectedtocalculatetheQoEvalueduringtheplayback.
consistsoftwoparallelfullyconnectedlayerswith64neurons,
whichrepresenttheoutputsof𝑓
𝜙
𝜇 (𝒄)and𝑓
𝜙
𝜎(𝒄),respectively,with
B ADDITIONALEXPERIMENTALRESULTS
thelatentvariable𝒛havingadimensionof|𝑍|=64.
B.1 ConsistencyonOut-of-DistributionTraces
As with the log-form quality metric 𝑄𝑜𝐸 𝑙𝑜𝑔, we compare the
A.2 Policynetwork
consistencyofMERINAtootherbaselinealgorithmshere,with
Theactorandcriticnetworkshavethesamearchitectureexcept the linear quality metric 𝑄𝑜𝐸 𝑙𝑖𝑛 on in-distribution and out-of-
fortheoutputlayer,butdonotsharetheirparameters.Thestate distributiondatasets.TheNNweightsoflearning-basedalgorithms
ofthevideostreamingsystem,includesthefeaturesasdetailedin arethesametothoseusedinSection.5.1(i.e.,learnedfromthe
Section2,isfedintotheinputlayeroftheactorandcriticnetworks. F&Hdataset).WealsopresentthenumericalresultsinTable2by
Concretely,forthesetofavailablebitrateversionsA,weusea
usingthesameformat.
one-dimensionalconvolutionlayerwith128filters,eachofsize The primary difference between the findings for𝑄𝑜𝐸 𝑙𝑜𝑔 and
4withstride1,toprocessthem.Meanwhile,fivefullconnected 𝑄𝑜𝐸 𝑙𝑖𝑛 isthatMERINAandFuguperformsbetterwiththemetric
layerswith128neuronsareplacedattheinputlayertodealwith 𝑄𝑜𝐸 𝑙𝑖𝑛thanwiththemetric𝑄𝑜𝐸 𝑙𝑜𝑔onthePuffer-Oct.17-21dataset.
theremainingfeaturesofthestate,includingthemeasuredaverage MERINA,inparticular,achievesacomparableperformanceinterms
throughput𝐶 𝑘−1 ,timeduration𝑑 𝑘−1 duringthedownloadofthe oftheaveragechunkQoEvaluetoBOLA,whichalsoperforms
lastvideochunk,currentbufferoccupancy𝐵 𝑘,selectedbitrate𝑎
𝑘−1 bestonthePuffer-Oct.17-21dataset.Theseresultsindicatethatby
ofthelastchunk,andthenumberofvideochunksthathavenot usingthe𝑄𝑜𝐸 𝑙𝑖𝑛qualitymetric,MERINApresentsageneralization
beendownloadedyet.Forthelatentvariablesampledfromthe capability consistently across all the throughput dynamics in
posterior𝑞
𝜙
(𝒛|𝒄),wealsouseafullyconnectedlayerwith1280
these five datasets, without the requirement of any adaptation.
neuronstoprocessthelatentrepresentations.Additionally,these Thismightbebecausethelinearqualitymetricproducesbigger
individualinputlayersfordifferentinformationareallfollowed qualityintervalsbetweenthebitrateversionsthanthelog-form
by the LeakyReLU activation function. The results of the input metric,resultinginamoredistinctfeatureforthebitrateselection.
layersarethenmergedintotwofullconnectedlayers(512and128 Additionally,FuguoutperformsRobustMPCintermsoftheaverage
neurons)thatequipwiththeLeakyReLUactivationfunctionand chunkqualityonthetwopufferdatasetswhenusingthemetric
areeventuallyfollowedbytheoutputlayer.Theoutputofactor 𝑄𝑜𝐸 𝑙𝑖𝑛,butperformsmuchworsewhenusingthemetric𝑄𝑜𝐸 𝑙𝑜𝑔.
networkconsistsofafullyconnectedlayerwith𝑀 = 6neurons
followedbythesoftmaxactivationfunction,whichgeneratesthe B.1.1 Real-World Test for 𝑄𝑜𝐸 𝑙𝑖𝑛 . With the same settings for
probabilityofbeingtheoptimalchoiceforeachavailablebitrate 𝑄𝑜𝐸 𝑙𝑜𝑔,weevaluatethelearning-basedalgorithmsMERINAand
version.Whiletheoutputofcriticnetworkincludesalinearneuron Comyco,andtheheuristicalgorithmsBOLAandRobustMPC,by
(withnoactivationfunction)whichoutputstheestimateofthestate- usingthelinearqualitymetric𝑄𝑜𝐸 𝑙𝑖𝑛 intherealworldplatform
valuefunction.Notethatincreasingthenumberofparametersof underthreedifferentnetworkconditions:a4Gcellularnetwork,
NNsisnotthekeyfactorinimprovingQoE,particularlyinterms a public WiFi network on campus, and a wide area network
ofthegeneralizationcapability. connectingShanghaiandLosAngeles,withmeanandstandard
3015

ImprovingGeneralizationforNeuralAdaptiveVideoStreamingviaMetaReinforcementLearning MM’22,October10–14,2022,Lisboa,Portugal
Table2:PerformancecomparisonofdifferentABRalgorithmsintermsoftheaveragechunk𝑄𝑜𝐸
𝑙𝑖𝑛valueondifferentdatasets.
Mean±std(𝑅𝑔𝑎𝑝)
|     |     |     |     | FCC |     | HSDPA | Oboe |     | Puffer-Oct.17-21 |     | Puffer-Feb.18-22 |     |
| --- | --- | --- | --- | --- | --- | ----- | ---- | --- | ---------------- | --- | ---------------- | --- |
BOLA 0.96±0.54(−20%) 1.12±0.81(−16%) 1.96±1.03(−16%) 0.86±1.83(+1%) 0.66±2.90(−26%)
|     |     |     | 0.98±0.75(−18%) |     | 1.22±1.20(−9%) |     | 2.30±1.24(−2%) |     | 0.73±2.16(−14%) |     | 0.81±2.97(−9%) |     |
| --- | --- | --- | --------------- | --- | -------------- | --- | -------------- | --- | --------------- | --- | -------------- | --- |
RobustMPC
Pensieve 1.13±0.65(−5%) 1.28±0.95(−5%) 2.26±1.15(−4%) 0.14±11.55(−84%) 0.55±8.67(−44%)
|     |     |     | 1.15±0.73(−3%) |     |     | 1.34±1.05(0%) | 2.29±1.21(−2%) |     | −0.13±2.86(−115%) |     | 0.68±3.06(−24%) |     |
| --- | --- | --- | -------------- | --- | --- | ------------- | -------------- | --- | ----------------- | --- | --------------- | --- |
Comyco
Fugu 1.11±0.70(−7%) 1.24±1.04(−7%) 2.31±1.21(−1%) 0.74±2.13(−13%) 0.83±2.99(−7%)
|     |     |     | 1.10±0.83(−8%) |     | 1.26±1.11(−6%) |     | 2.29±1.23(−2%) |     | 0.33±2.80(−61%) |     | 0.66±3.34(−26%) |     |
| --- | --- | --- | -------------- | --- | -------------- | --- | -------------- | --- | --------------- | --- | --------------- | --- |
BayesMPC
|     | MERINA |     | 1.19±0.67 |     |     | 1.34±0.99 | 2.34±1.15 |     | 0.85±2.02 |     | 0.90±2.97 |     |
| --- | ------ | --- | --------- | --- | --- | --------- | --------- | --- | --------- | --- | --------- | --- |
MERINA(nMIwith𝜆=0) 1.08±0.66(−9%) 1.22±1.11(−9%) 2.25±1.19(−4%) 0.50±2.68(−61%) 0.72±2.99(−19%)
|     |     |     | 1.13±0.44Mbps |     |     | 1.61±0.95Mbps | 2.60±2.08Mbps |     | 1.85±0.91Mbps |     | 1.60±0.88Mbps |     |
| --- | --- | --- | ------------- | --- | --- | ------------- | ------------- | --- | ------------- | --- | ------------- | --- |
Datasetdistribution
|     | BOLA RobustMPC |     | Comyco |     | MERINA |     |     |     |     |     |     |     |
| --- | -------------- | --- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
eulav  egarevA 5
4
3 (cid:35)(cid:70)(cid:85)(cid:85)(cid:70)(cid:83)(cid:1)(cid:30)(cid:30)(cid:31)
2
1
0
|     | 4G  |     | Public WiFi | International Link |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Figure5:Comparisonof𝑄𝑜𝐸
𝑙𝑖𝑛withoutadaption.
|     |     |     |     |     |     |     |     | (a)AdaptationCurves |     |     | (b)Puffer-Oct.17-21 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------------------- | --- |
deviation of recorded throughput values of 4.52 ± 0.74𝑀𝑏𝑝𝑠, Figure6:a)TheadaptationcurvesofMERINAandComyco,
2.52 ± 1.06𝑀𝑏𝑝𝑠 and 1.63 ± 1.16𝑀𝑏𝑝𝑠. The same test video is andb)averagechunk𝑄𝑜𝐸
𝑙𝑖𝑛improvementoverRobustMPC.
loadedrepeatedlyoneachnetworkusingarandomlychosenABR
atfirstandthentheperformanceimprovement.Additionally,we
scheme.Eachexperimenttakesabout1hourtocomplete,andthe
showtheCDFsofQoEimprovementofcomparisonalgorithms
NNsweightsforMERINAandComycoarealltrainedontheF&H
|     |     |     |     |     |     |     | over RobustMPC |     | in Fig. 6(b), | with | MERINA-Offline, | MERINA- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------- | ---- | --------------- | ------- |
dataset.Fig.5illustratesthereal-worldresultsoffourcomparison
algorithms without adaptation on these three scenarios. It can Adp-100andMERINA-Adp-1100denotingtheproposedalgorithm
beseenthatMERINAsurpassestheotherbaselinealgorithmson that employs the NN weights without adaptation, after 100-
epochadaptation(beforetheperformancedegradation),andafter
thepublicWiFiandinternationallinkconditions,butperforms
|                |             |     |          |            |         |     | 1100-epoch | adaptation | (performance |     | improved again | after the |
| -------------- | ----------- | --- | -------- | ---------- | ------- | --- | ---------- | ---------- | ------------ | --- | -------------- | --------- |
| slightly worse | than Comyco |     | under 4G | condition. | Comyco, | on  |            |            |              |     |                |           |
degradation),respectively.Theresultssuggestedthat,after1100-
| the other | hand, achieves | the | highest average |     | chunk | QoE value |     |     |     |     |     |     |
| --------- | -------------- | --- | --------------- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- |
epochadaptation,theproportionofsessionsthatachievehighQoE
under4Gconditions,butperformspoorlyunderpublicWiFiand
internationallinkconditions.Thesereal-worldtestfor𝑄𝑜𝐸 𝑙𝑖𝑛still valuerisesignificantly.
candemonstratethegeneralizationcapabilityofMERINAwhen
B.3 AblationStudy
deployedinthereal-worldscenarios.
Finally,weconductsomeexperimentstodemonstratethebenefitto
B.2 FastAdaptationToNewEnvironments generalizationasintroducedbytheproposedmutualinformation-
basedregularizationfunctioninEq.(5),providingafurtherinsight
| Though MERINA | performs | slightly | worse | than | BOLA | in terms |            |     |                  |     |                    |       |
| ------------- | -------- | -------- | ----- | ---- | ---- | -------- | ---------- | --- | ---------------- | --- | ------------------ | ----- |
|               |          |          |       |      |      |          | on MERINA. | We  | train a modified |     | version of MERINA, | named |
oftheaveragechunkQoEvalueonthethroughputdynamicsof
MERINA(nMI),bysetting𝜆=0fortheactorloss,onthetraining
| Puffer-Oct.17-21whenusingthelinearqualitymetric𝑄𝑜𝐸 |     |     |     |     |     | 𝑙𝑖𝑛,we |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
datesetF&H,andthenevaluateitsQoEperformanceonallthefive
| examine | here MERINA’s | ability | to rapidly | adapt | to this | dataset |     |     |     |     |     |     |
| ------- | ------------- | ------- | ---------- | ----- | ------- | ------- | --- | --- | --- | --- | --- | --- |
datasets.TheresultsofaveragechunkQoEachievedbyMERINA
| and study | how much | improvement | can | be achieved |     | through |                                          |     |     |     |           |      |
| --------- | -------- | ----------- | --- | ----------- | --- | ------- | ---------------------------------------- | --- | --- | --- | --------- | ---- |
|           |          |             |     |             |     |         | (nMI)arealsopresentedinTables1and2for𝑄𝑜𝐸 |     |     |     | 𝑙𝑜𝑔and𝑄𝑜𝐸 | 𝑙𝑖𝑛, |
adaptation.Allthesettingsw.r.t.themeta-adaptationprocedures
respectively,whichrevealacriticalfinding:themutualinformation-
arethesametothoseofSection5.3,withtheassociatedresults
|             |               |        |           |      |      |           | based regularizer |     | improves | the average | QoE performance | and |
| ----------- | ------------- | ------ | --------- | ---- | ---- | --------- | ----------------- | --- | -------- | ----------- | --------------- | --- |
| illustrated | in Fig. 6. It | can be | seen from | Fig. | 6(a) | that when |                   |     |          |             |                 |     |
usingthelinearqualitymetric𝑄𝑜𝐸 generalizationonbothin-andout-of-distributiondatasets.This
𝑙𝑖𝑛,MERINAcansurpassBOLA
(0.86) demonstratesthattheregularizationfunctionfacilitatesthelatent
| in  | terms of average | chunk | QoE | value | with around | 100 |     |     |     |     |     |     |
| --- | ---------------- | ----- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
variable’sexpressiveness(i.e.amoreinformativerepresentation)
trainingepochs(seeMERINA-Adpt)andachievesamuchhigher
tobitrateselectioninmixeddynamics,thereforeenhancingthe
chunkQoEvalue1.10asymptotically(seeMERINA-Asy).Itisalso
generalization.Inaddition,withouttheimitationlearning-based
seenthatMERINA’sperformancewilldegradeafterafewupdate
pre-training,thelearningprocessofMERINAwillbeexceedingly
epochsandthenimprovemonotonously.Thisisbecausetheinitial
parameters𝜙 and𝜃 unstable,andthetrainingwillalwaysfallintoalocaloptimum.
|     | may | be  | near a local | optimum | for | the new |     |     |     |     |     |     |
| --- | --- | --- | ------------ | ------- | --- | ------- | --- | --- | --- | --- | --- | --- |
Thisphenomenonmayresultfromtheprobabilisticlatentencoder
throughputdynamics,whileexploringforahighervalue(towards
andthemixdynamicssettinginourpaper.
theglobaloptimum)mayexperienceaperformancedegradation
3016