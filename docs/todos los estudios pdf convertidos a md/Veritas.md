Veritas: Answering Causal Queries from Video Streaming Traces
ChandanBothra∗1,JianfeiGao∗1,SanjayRao1,andBrunoRibeiro1
1PurdueUniversity
April20,2022
Abstract choicewereremoved(e.g.,duringtheCOVIDcrisis,many
videopublishersrestrictedthemaximumbitrate[3]).Answer-
Inthispaper,weseektoanswerwhat-if questions–i.e.,given
ingwhat-if questionsofthisnatureisalsoknownascausal
recordeddataofanexistingdeployednetworkedsystem,what
reasoning.Causalinferenceconsiderstheeffectofeventsthat
wouldbetheperformanceimpactifwechangedthedesignof
didnotoccurwhilethedatawasbeingrecorded[33],andhas
thesystem(ataskalsoknownascausalinference).Wemake
been exploredin domains as diverse as economics [8] and
threecontributions.First,weexposethecomplexityofcausal
epidemiology[35]. inferenceinthecontextofadaptivebitratevideostreaming,
achallengingdomainwherethenetworkconditionsduring Shortcomings of traditional (associational) machine
thesessionactasasequenceoflatentandconfoundingvari- learning. Severalwidelyusedmachinelearning(ML)tools
ables,andachangeatanypointinthesessionhasacascading areinadequateforcausalinference.Manyapproaches(e.g.,
impactontherestofthesession.Second,wepresentVeritas, neuralnetworksanddecisiontrees)merelycapturecorrela-
a novel framework that tackles causal reasoning for video tionsincollecteddata,limitingthemtoassociationspredic-
streamingwithoutresortingtorandomizedtrials.Integralto tions,i.e.,predictionsthatarerelatedtoassociationsbetween
Veritas is an easy to interpret domain-specific ML model observationsinadeployedsystem.Associations,however,are
(anembeddedHiddenMarkovModel)thatrelatesthelatent inadequatetoanswercausalquestions.Forinstance,people
stochasticprocess(intrinsicbandwidththatthevideosession carryingumbrellasonasunnymorningisagoodpredictorof
canachieve)toactualobservations(downloadtimes)while rainintheafternoon.However,forbiddingpeopletocarryum-
exploitingcontrolvariablessuchastheTCPstate(e.g.,con- brellasinthemorningdoesnotpreventrainintheafternoon.
gestion window) observed at the start of the download of Similarly,invideostreaming,anABRalgorithmcouldchoose
videochunks.Weshowthroughexperimentsonanemulation lowerbitrates when networkconditions are poor,resulting
testbedthatVeritascananswerbothcounterfactualqueries inanassociationbetweenlowervideobitratesandrebuffer-
(e.g.,the performance of a completed video session had it ingevents.However,decreasingbitratewillnotcausemore
usedadifferentbuffersize)andinterventionalqueries(e.g., rebufferingevents–rather,theoppositeislikelytohappen.
estimatingthedownloadtimeforeverypossiblevideoquality OtherapproachessuchasReinforcementLearningandRan-
choiceforthenextchunkinasessioninprogress).Indoing domizedControlTrialsallowreasoningaboutaredesigned
so,Veritasachievesaccuracyclosetoanidealoracle,while systembutrequireactiveinterventionsthatinvolvechanging
significantlyoutperformingbothacommonlyusedbaseline a system,and observing its performance among real users.
approach,andFugu(anoff-the-shelfneuralnetwork)neither Theseapproachescouldbedisruptivetotheperformanceof
ofwhichaccountforcausaleffects. real users,and cannot answer what-if questions about past
sessions(§2).
1 Introduction
Confoundersinvideostreaming. Incontrasttotheabove
Acentralthemeofdata-drivennetworkingisansweringwhat-
approaches,our work focuses on causal inference on pas-
if questions — given data obtained from a real-world de-
sively collected data,which is not disruptive to the perfor-
ploymentofanexistingsystem,wewanttoinferwhatwould
manceofliveusers.Weconsidercausalinferencenotonly
havehappenedifwehadusedadifferentsystemdesign.For
abouthowtheproposedchangewouldaffectsessionsinthe
instance,givendatacollectedfromrealvideostreamingses-
future(alsoreferredtoasinterventionalinference)butalso
sions,avideopublishermaywishtounderstandtheperfor-
howitwouldhaveaffectedagivensessioninthepast(also
manceifadifferentAdaptiveBitrate(ABR)algorithmwere
referredto as counterfactualinference). Weexpandon the
used(Figure1),orifanewvideoquality(e.g.,an8Kresolu-
distinctionsin§2.1.
tion)wereaddedtotheABRselection,oranexistingbitrate
Whilecausalinferencecanbenefitmanynetworkingtasks,
*Theseauthorscontributedequallytothiswork. inthisworkwefocusonvideostreaming.First,itisadomain
1
2202
guA
62
]IN.sc[
1v69521.8022:viXra

startofeachchunkdownload)thatsimplifiesthecausaltask,
Video Network
Quality Streaming Conditions and(b)aMLmethodtoperformabductionthatisprincipled,
Algorithm A yetaccesibleandeasytointerpretgivenitleveragesdomain
insights.
Video
Morespecifically,aspartofVeritas,wehavedesigneda
Streaming
Quality?
Algorithm B Log domain-specific ML model that relates the latent stochas-
tic process (intrinsic bandwidth that the video session can
achieveifTCPwereinsteadystatethroughoutthesession)
toactualobservations(actualthroughputobservedbychunk
what-if?
downloads),whenalsogivenasequenceofadditionalcon-
Figure1:Examplewhat-ifquestionaskedbyanetworkde-
trol variables in the form of the TCP states at the start of
signer: whatwouldbe the quality ifalgorithm B hadbeen
eachchunkdownload.Thiscontrolisneededsincetheactual
usedinsteadofAunderthesamenetworkconditions?
observed throughput depends on the TCP state of the con-
nection(e.g.,whetherslow-startisinprogress),andthesize
where there has been much interest in using data to drive
ofthedownloadedobject.Thecontrolallowsusto“invert”
designoptimizations[10,22,24,28,40,47].Second,video
theobservedthroughputvariablesinordertogetthelatent
streamingreliesonadaptivebitrate(ABR)algorithms,where
bandwidthvariables.
decisionsmadebythealgorithmdependonnetworkcondi-
Toensurewerepresentthestatisticaldependenciesinthe
tions,whichinturnimpactobservablemeasurements.Owing
latent bandwidth time series during the inversion process,
totheadaptivenature,thenetworkconditionsencountered
wedevelopanEmbeddedHiddenMarkovModel(EHMM),
duringthe session actas asequence oflatentconfounding
whichembedsadomain-specificmodelfortheemissionpro-
variables,resultingincomplexspuriouscorrelationsindata,
cess.ABayesianposteriorsamplingoftheEHMMallowsus
which can impairthe use of common ML approaches. We
tocapturetheuncertaintyinherentinthecombinationofour
demonstratethisbyshowingthatFugu[47],arecentwork
inversion,stochasticmodeling,andthedata.Onceasampled
thatusesaneuralnetworktopredictdownloadtimesinvideo
invertedbandwidthprocessisobtained,wecannowdirectly
sessions, can suffer significant biases when asking causal
evaluatetheproposedchanges,andreturntheanswertothe
questions(§2.2).
what-if query. Rather than a single point estimate, Veritas
Cascading effects complicate causal inference in video providesarangeofpotentialoutcomesreflectingtheinherent
streaming. Thedynamicnatureofvideostreamingmakes uncertaintyininferencesthatcanbemadefromthedata.
causalinferenceachallengingtask.Consideraskingthefol-
Evaluation. WeevaluateVeritaswithrespecttoitsabilityto
lowingwhat-ifquestionforarecordedvideosession:what
answerarangeofwhat-ifcausalqueriesincludingtheimpact
if bitrate b(cid:48) rather than the original b had been chosen for
of(i)changingtheABRalgorithm;(ii)changingthebuffer
videochunkn≥1,b(cid:48)(cid:54)=b? Thiswhat-ifchange(frombto
size;and(iii)changingthesetofvideoqualitiesthattheABR
b(cid:48)atchunkn)hasacascadingimpactonthesession’sfuture
algorithmcouldselectfromusinganemulationtestbed.Our
bufferoccupancy,andbitrateselectiondecisions,aswellas
evaluation approach involves emulating a video streaming
thestarttimesoffuturechunkdownloads.Thus,allobserved
systeminitsoriginalsetting,mimickingadeployedsystem
variablesdescribingchunkn(cid:48)≥ncanpotentiallychangedue
withbandwidthtracesthatserveasthegroundtruth.Wethen
toadifferentdecisionforchunkn.Here,thedatarecorded
applyVeritasonthelogsofthedeployedsystems(excluding
inthesessionafterchunknnolongerrepresentswhatwill
thegroundtruthbandwidthtraces)anduseVeritas’sabduction
happeninthesessionevenifnootherchangesweremadein
topredicttheimpactofthewhat-ifchange.Wecomparethe
thefuture.
predictions from Veritas with predictions from a baseline
Taming the complexity of causal inference with Veritas. approachthatusesthelogsdirectlywithoutexplicitcausal
MotivatedbytheabovechallengeswedesignVeritas,anovel adjustments, and an oracle approach that knows the exact
framework for answering causal queries for video stream- ground truth bandwidth values. Across the board, Veritas
ing. RatherthancomplexMLmodels,orresorttorandom- returnssignificantlymoreaccurateresultstocausalinferences
izedtrials,Veritasonlyreliesoneasy-to-interpretandlow- than the baseline approach, and close to the ground truth
complexityMLmodels,whileonlyrequiringpre-recorded values.Forexample,whenchangingtohighvideoqualities,
data.ThechallengethatVeritastacklesisabduction[33,Sec- Veritas predicted negligible rebuffering ratio across all the
tion4.2.4],whichinvolves(i)inferringasetoflikelyvalues traces,closetotheoracle,whileBaselinepredictedamuch
forlatentvariablesconsistentwiththeobservations;and(ii) highermedianrebufferingratiovalueofaround6.7%.
modelingtheproposedchangestoreturntheanswertoawhat- WealsoevaluateVeritas’sabilitytoanswerinterventional
ifqueryusingtheinferredlatentvariables.Whileabduction queries(inferencesrelatedtothefuture)byfocusingonits
ischallengingingeneral,thekeyinsightsofVeritasare(a)a abilitytopredictthedownloadtimeoffuturevideochunks
carefulselectionofcontrolvariables(theTCPstatesatthe giveninformationaboutpastchunkdownloadstatistics.Note
2

that Veritas must be able to make predictions under new someaspectofthesystemwerechanged(e.g.,changingthe
unseen scenarios (e.g., session logs of the previously de- setofvideoqualitiestheclientcouldchoosefrom,thebuffer
ployedABRalgorithmmayonlycontaincertainchunksize size,ortheABRalgorithm).
sequences,while the intervention may need to make deci- Wenextdefinethetwotypesofcausalinferencealgorithms
sionsaboutmoregeneralsequences).Weshowthatforsuch ofinterestinourwork,refiningacommondefinitionoflearn-
interventionalqueries,Veritasachievesmuchhigheraccura- ingalgorithms[27,Chapter1.1].
ciesthanFugu[47],whichreliesonanassociationalmethod.
Overall,theresultsshowtheimportanceandbenefitsofVeri- Definition1(Learninginterventionalinferencefornetwork
tas. tasks). Given(i)anetworkingtaskoveranunseensession
with a new method; (ii) training experience (e.g.,existing
2 BackgroundandMotivation
recordedsessions)obtainedwithanoldmethod;and(iii)a
performancemeasure;then,acomputerprogramissaidto
In this section,we motivate the need for causal reasoning,
and why ML tools used for associational predictions, and
learninterventionsifitspredictionperformanceinthenew
method at the task (new sessions) improves if given more
approaches such as Reinforcement Learning and Random-
experience(e.g.,givenmorerecordedsessionswiththeold
izedControlTrialsfallshort.Weillustratethisinthecontext
method).
of video streaming,and show how a state-of-the-art video
streamingsystem[47]thatusesassociationalreasoningfora
WefurtherrefineDefinition1forcounterfactuals.
causaltaskfallsshort.
2.1 Causalvs.AssociationalQueries Definition2(Learningcounterfactualinferencefornetwork
tasks). Given(i)trainingexperience(e.g.,existingrecorded
Videostreamingtodaytypicallyinvolvessplittingvideointo
sessions)runninganoldmethod;(ii)anewmethod;and(iii)
chunks,eachencodedatmultiplequalities.Clientspickqual-
aperformancemeasure,acomputerprogramissaidtolearn
ities for each chunk using Adaptive Bit Rate (ABR) al-
toperformcounterfactualinferenceifitsabilitytopredictthe
gorithms so as to balance between achieving high video
performanceofthenewmethodifithadbeenusedinplace
quality, while avoiding rebuffering based on network con-
oftheoldmethodinthesamerecordedsessionsimprovesif
ditions[6,17,19,26,38,44,48].
given more experience (e.g.,given more recorded sessions
Consider data collected from a video streaming system, withtheoldmethod).
whereforeachsessioninformationiscollectedregardingthe
chunksizeandthedownloadtime.Twoquestionsmaybeof In this work we introduce Veritas, a computer program
interesttoadesigner: thatisabletoperformbothinterventionalandcounterfactual
Q1.Givenasetofobservationsofchunksizesanddownload learning(Definitions1and2,respectively).
timesofavideosession,ifthevideosessionweregoingto
2.2 Challengeswithcausalqueries
nextdownloadachunkofsizes,whatwouldbethedownload
time? Associationalapproachesareinadequate.MostMLmeth-
Q2.Givenasetofobservationsofchunksizesanddownload odsworkbylearningassociationsinexistingdata,and,hence,
timesofavideosession,ifthedesignerhadintervenedinthe areonlyappropriateforassociationalpredictions. Unfortu-
sessionandhadaskedtonextdownloadachunkofsizes(cid:48), nately,theresultofanassociationalpredictionmaybewildly
s(cid:48)(cid:54)=s,whatwouldbethedownloadtime? inaccurateforacausalquestion.Wenextillustratethisinthe
Question Q1 pertains to passively observing the system contextofFugu[47],whichusesanassociationalMLmodel
athandwithitsexistingABRalgorithmandsettings.These foracausalquery.Specifically,Fugu[47]proposesaneural
offlineobservationscanbeusedtomakepredictionsabout networkwhichpredictsthedownloadtimeofavideochunk
thesystemundersimilarconditions.Morebroadly,anasso- givenitssize,andgiventhesizeandthedownloadtimesofthe
ciationalprediction seeks to predictoutcomes ofa system previousK chunks.ConsiderFugutrainedwithdataobtained
withoutinterfering(intervening)withitsoperation.Incon- fromthedeploymentofanABRalgorithm,sayAlgorithm
trast,manyreal-worldnetworkingtasksarelikeQ2,which A. This effectively trains Fugu to answerthe associational
requiregoingbeyondpassivelypredictingtheoutcomesofan QuestionQ1whichinvolvespredictingthedownloadtime
existingsystem.Thesetasksrequirecausalinference,which forthechunksizeselectedbyAlgorithmA(§2.1).However,
predictstheoutcomeofanintervention,achangeintheway considerthatthetrainedFugumodelisactuallydeployedas
thesystemoperates.Specifically,Q2pertainstotheimpact apredictorinarealvideostreamingsession,inamannerthat
ofaninterventionalchangetothesystemdesign:specifically interveneswithbitrateselection.Thatis,atanygiventime
using a different decision procedure that leads to a chunk stepofalivesession,Fuguisusedtopredictthedownload
ofsizes(cid:48) beingdownloadedratherthantheoriginalABR’s timesforallpossiblechunksizes,andanappropriatechunk
decisionofdownloadingsizes.Moregenerally,thedesigner sizeisselectedbasedonthesepredictions.Then,effectively,
maywishtounderstandtheimplicationsonperformanceif FuguisbeingusedtotacklethecausalqueryQ2(§2.1).
3

| )s( emit noissimsnarT lautcA |     |     |     | sdnoces ni emit daolnwoD |        |     |     |                   |     |     |     |     |
| ---------------------------- | --- | --- | --- | ------------------------ | ------ | --- | --- | ----------------- | --- | --- | --- | --- |
|                              |     |     |     |                          | Actual |     |     | )spbM( tuphguorhT |     |     |     |     |
4
|     |     |     |     |     | Predicted |     |     | 15  |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
40
3
10
2
20
| 1   |     |     |     |     |     |     |     | 5   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
| <0.02 | 0.02-0.0         | 4 .04-0.10 0.1-1.0 1.0-2.0 | 2.0-4.2 | 0   |                     |     |              | 0   |     |                 |     |     |
| ----- | ---------------- | -------------------------- | ------- | --- | ------------------- | --- | ------------ | --- | --- | --------------- | --- | --- |
|       |                  | 0                          |         |     | Low Quality         |     | High Quality | 1 2 | 3 4 | 5 6 7 8 9101112 |     |     |
|       | Chunk sizes (MB) |                            |         |     | Next selected chunk |     |              |     | log | 2 Size(KB)      |     |     |
|       |                  | (a)                        |         |     |                     | (b) |              |     |     | (c)             |     |     |
Figure2:(a)DistributionofdownloadtimesfordifferentgroupsofchunksizeswiththeMPCalgorithmonasubsetofFCC
traces [1].Therelationshipisnotmonotonicowingtotheadaptivenatureofthealgorithm.(b)PredictionerrorinFugu [47]
withcausalqueries.(c)Varianceinobservedthroughputwithchunksizeforsameemulatednetworkbandwidth.
Unfortunately,theassociationalapproachsuffersfroma whereSisthesize,andDthedownloadtime.Forinstance,
bias because the deployedABR algorithm A tends to pick the neural network from [47] could use a sequence of ob-
lower(resp.higher)sizedchunkswhennetworkbandwidth servedchunkthroughputs,andpredictthethroughputofthe
isbad(resp. good). Consequently,thedownloadtimewith nextchunk.Unfortunately,theobservedthroughputitselfis
anABRalgorithmmanynotnecessarilyshowtheexpected dependent on the size of chunks owing to TCP slow start
dependencewithsize.Toillustratethis,weconductedcon- effects [10, 28, 47]. Figure 2(c) presents a distribution of
trolledexperimentswherewetrainedFuguon100traces,50 throughput for chunks in a given size range in controlled
withpoornetworkconditions[0-0.3Mbps]and50withgood experimentsusingTCPwhereweemulatedaconstantnet-
networkcondition[9-10Mbps]withtheMPCalgorithmin workbandwidthof18Mbpsinaclientserversetup,andsent
anemulationtestbed(detailsin§4)usingtheFCCthrough- payloadsofvaryingsizes(2KBto4MB). Notethatthegap
puttraces[1] Figure2(a)presentsthedownloadtimeofall betweenpayloadsimpactswhetherTCPentersaslow-start
chunksacrossallthevideosessions,witheachboxplotcorre- restartphase[12].Thegraphshowsthatforsmallsizes(less
spondingtochunkswithaparticularsizerange.Thefigure thanthebandwidthdelayproductofthenetwork),throughput
showsthatthedownloadtimesdonotgrowinalinearfashion is much smaller,while it is closer to the intrinsic network
withchunksize,rathershowanon-monotonicdependence. bandwidthforlargersizes.Notethatforintermediatesizes
This is because ofthe adaptive bitrate selection described (around 26 to 210 Kilobytes) there is significant variability
above. in throughput based on the gap between the transmission
oftwoconsecutivepayloads,andwhetherTCPentersslow
WenexttestFuguonanewtracewithpoornetworkcondi-
|     |     |     |     |     |     |     | startrestartornot. | Thus,simply |     | considering | throughputis |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | ----------- | --- | ----------- | ------------ | --- |
tions.WeconsiderapointintimewheretheABRalgorithm
insufficient,andwhileitwouldbedesirabletoconsiderthe
haspickedasequenceoflowerqualitychunks.Wethenuse
|     |     |     |     |     |     |     | intrinsincnetworkbandwidth,this |     |     | is a hidden | variable | not |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | ----------- | -------- | --- |
Fugutoanswerthewhat-ifquestions,whatwouldthedown-
| loadtimebeif(i)thenextchunkselectedwerehighquality; |     |     |     |     |     |     | availableindata. |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
and(ii)thenextchunkselectedwerelowquality.Figure2(b)
2.3 Whynotactivelyintervene?
showsthedownloadtimespredictedbyFuguandtheactual
downloadtimesineachcase.ThefigureshowsthatFugusig- Ratherthanmakingpredictionsbypassivelyobservingasys-
nificantlyunderestimatesdownloadtimesforthehighquality tem,some approaches can evaluate the impact of a design
chunk,butdoesagoodjobforthelowqualitychunk.Thisis
changebyactivelyintervening(changing)thesystem,andob-
becauseFuguusesanassociationalmodelthatiseffectiveat servingtheperformance.ThesetechniquesincludeRandom-
predictingdownloadtimesforachunksizethatthedeployed
izedControlTrials(RCTs),A/BTesting,andReinforcement
| algorithm | would | have selected | next,but | not | the download |     |     |     |     |     |     |     |
| --------- | ----- | ------------- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Learning[41].
| times if | the chunk | size | had been forced | to  | be a particular |     |     |     |     |     |     |     |
| -------- | --------- | ---- | --------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
RCTs[15]canmeasuretheeffectsofinterventions.How-
value.Consequently,whilethemodeleffectivelypredictsthe
|     |     |     |     |     |     |     | ever, there | are several | disadvantages | to  | RCTs. First, | such |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | ------------- | --- | ------------ | ---- |
downloadtimeofchunksizesactuallychosenbythedeployed trials may lead to degraded performance to some viewers.
| ABR,itperforms |     | poorlywhen | answering |     | the causalquery |     |               |                |     |                 |            |     |
| -------------- | --- | ---------- | --------- | --- | --------------- | --- | ------------- | -------------- | --- | --------------- | ---------- | --- |
|                |     |            |           |     |                 |     | For instance, | in the context | of  | video streaming | algorithm, |     |
whatwouldhappenifanalternatesizewerechosen.
|     |     |     |     |     |     |     | even ifchunkbitrates |     | are chosen | randomlywithoutregard |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ---------- | --------------------- | --- | --- |
Latentvariablescomplicatecausalqueries.Apotentialal- tonetworkconditions,achunk’sstarttimeisnotrandomas
ternativetotheaboveapproachistoconsidertheobserved it still depends on the download end time of the previous
throughputwhendownloadingavideochunk,definedasS/D. chunk[39].AnotherapproachistouseA/Btestingofanew
4

C<latexit sha1_base64="hrcvMkvW7pC0Gc3Lz0FclJpnOWk=">AAACI3icbVDLSsNAFJ3UV62vqDvdDBZBsJZEirosduOygn1AG8JkMmmHTiZhZlIsoeDP6Fb/w524ceFP+AVO2yxs64ELh3PuGeYeL2ZUKsv6MnIrq2vrG/nNwtb2zu6euX/QlFEiMGngiEWi7SFJGOWkoahipB0LgkKPkZY3qE381pAISSP+oEYxcULU4zSgGCktueZRzU2Jyy/scanL/EjJkhaky8/tsWsWrbI1BVwmdkaKIEPdNX+6foSTkHCFGZKyY1uxclIkFMWMjAvdRJIY4QHqkY6mHIVEOun0hjE81YoPg0jo4QpO1bmEP6SxzDKPs9BfP0WhlKPQ0y+FSPXlojcR//M6iQpunJTyOFGE49lHgoRBFcFJYdCngmDFRpogLKi+BeI+EggrXWtBl2QvVrJMmpdl+6pcua8Uq7dZXXlwDE7AGbDBNaiCO1AHDYDBE3gBr+DNeDbejQ/jc7aaM7LMIZiD8f0LNAqksg==</latexit> en  1 ,...,C sn+1 C<latexit sha1_base64="BKB4e0qbcyA2TPqedMTmrTc/GUg=">AAACK3icbVDNSsNAGNzUv1r/oh69hBZBsJZEinos9uKxgv2BNoTNZtMu3WzC7qZYQu6+jF71PTwpXn0Bn8Btk4NtHXZhmNn52G/ciBIhTfNDK6ytb2xuFbdLO7t7+wf64VFHhDFHuI1CGvKeCwWmhOG2JJLiXsQxDFyKu+64OfO7E8wFCdmDnEbYDuCQEZ8gKJXk6OWmk2AnYRdWqk51QL1QiqoSRSaeW6mjV8yaOYexSqycVECOlqP/DLwQxQFmElEoRN8yI2knkEuCKE5Lg1jgCKIxHOK+ogwGWNjJfJfUOFWKZ/ghV5dJY64uJLwJiUSeecxCf/0EBkJMA1dNCqAciWVvJv7n9WPp39gJYVEsMUPZR/yYGjI0ZsUZHuEYSTpVBCJO1C4GGkEOkVT1llRJ1nIlq6RzWbOuavX7eqVxm9dVBCegDM6ABa5BA9yBFmgDBJ7AC3gFb9qz9q59al/Z04KWZ47BArTvXxRYp64=</latexit> en  1  1 ,...,C sn  1+1
d-separates past and future
Figure3:Causalmodelof(embedded)dependenciesinanABRalgorithmstartingate ,thearrivaltimeofthe(n−1)-st
n−1
chunk,untile ,thearrivaltimeofthen-thchunk.Shadedgrayvariablesareobserved,whilewhite(unshaded)variablesare
n
hidden.AsufficientconditionforasetU ofvariablestod-separateasetAandBisthatallundirectedpathsintheDAGbetween
AandBincludeatleastonevariablefromU,andnosuchpathshavearrowscollide“head-to-head”inthevariablesinU.
designchange.SinceA/Btestingcanimpacttheperformance tifyacausaleffect,andhowtomaketheadjustment(§3.2).
oflive users,itis onlyusedin a conservative fashion ifan Finally,§3.3discusseshowVeritasputsallthesemethodsto-
offline analysis approach indicates the design change has gethertoperformcounterfactualandinterventionalinference.
sufficientpotential.Thus,thereremainsaneedtoanswera
3.1 Modelingcausaldependencies
questionofflinewithtracedataalone.
Reinforcement learning may be viewed as a sequential A key factor that impacts the decisions made by a video
RCTinthattheagentdynamicallylearnsthebestdecisions streaming algorithm is the Ground Truth Bandwidth
totakeateachstateofthesystem.Thecollectionofallpairs (henceforth abbreviated as GTBW), which captures the
(bestdecisions,currentsystemstates)isdenotedapolicy.A bandwidth the network is intrinsically capable of,without
drawbackofRCTsingeneral,andreinforcementlearningin consideringdependenceonsize,andtheslowstarteffectsof
particular,isthatitonlyanswersthequestionofwhichdeci- thetransportprotocol–i.e.,whatthetransportprotocolwould
sions,outofasetoftesteddecisions,arethebesttotakefor intrinsicallyseeifitwererunninginsteadystate.Wemodel
agivensystemstate.Ifoursetofpossibledecisionschanges, the evolution ofGTBW as a discrete process overdiscrete
theRCT/RLtestsmustberunagainonnewsessions. timeintervalst∈{1,...,T}(eachofwall-clocktimelength
AnotherimportantpointisthatbothRCTsandreinforce- ofδ),withtheGTBWduringanytimeintervalbeingacon-
mentlearningcannotdirectlyanswercounterfactualqueries, stant.Timeisassumedtobediscretetosimplifyourapproach,
althoughtheirrandomized(exploration)measurementsmay sinceδcanbeasfine-grainedasnecessary.
still be used by counterfactual estimators in some special Consider that the session downloads a series of chunks
cases(e.g.,[9]).Hence,interventionalmethodsmaynotbe 1...N.Chunkn∈{1,...,N}startsitsdownloadattimes ∈
n
usefulinsomescenariosbecausetheycanonlybetestedinfu- {1,...,T}andfinishesattimee ∈{s ,...,T}. Thevariables
n n
turesessions:Imagineseeingrarenetworkconditionswherea thatevolveovertimeare:(i)C ∈C,theaverageGTBWat
t
deployedalgorithmperformedpoorly.Sincetheseconditions time interval ((t−1)δ,tδ]; (ii) B, the amount of buffer in
t
arerare,wewouldliketoknowifacertainchangetotheal- thevideoplayerattimet∈{1,...,T},and(iii)W,theTCP
t
gorithmwouldhavesignificantlyimprovedtheperformance. stateattimet.TheTCPstateincludesparameterssuchasthe
ThisisacounterfactualqueryandRCTsandreinforcement congestionwindow,slowstartthreshold,RTT,minRTT,time
learningaregenerallynotapplicableinthisscenariosincethe sincelastdatasend,andRTO.
eventisinthepast,andanyRCTtotestanewintervention Thevariablesthatevolveateachchunkrequestare:(i)the
onthesystemcanonlybeappliedinfuturesessions. size(S )ofthen-threquestedchunkand(ii)D ,itsdownload
n n
time,n=1,...,N.Thethroughputobservedduringthedown-
3 Veritas: A causal inference framework for
load(Y )canbecalculatedusingthechunksizeanddownload
videostreaming n
time.
Inthissection,wepresentVeritas,ourframeworkforanswer- Henceforth,foranyrandomvariableX wedefinethese-
ing causal queries related to video streaming. We start by quencesX :=(X ,...,X )andX :=(X ,...,X ).More-
a:b a b sa:b sa sb
presentingacausalgraph(DAG)whichmodelsthevariables over,letS =∪N {s }andE =∪N {e }bethesetofran-
n=1 n n=1 n
involvedwithvideostreaming,andthedependenciesorcausal domvariablesofshowingthediscretetimeswhereachunk
relationshipsbetweenthem(§3.1).Wethendiscusshowthe startsandendsdownloading,respectively.Weassumethatthe
DAGleadsustodecidewhatadjustmentsareneededtoiden- variablesinW ,B ,S ,S,E andY (showninshaded
s1:N s1:N 1:N 1:N
5

grayinFigure3)aregenerallyobserved variablesinvideo ifwecouldinferC wewouldbeabletohandleanycounter-
1:T
streamingsessions(thatis,alltheinformationregardingthem factualorinterventionalqueryneeded.Thisproceduretoinfer
iseitherdirectlyavailable,orcanbecalculatedfromthedata). aconfounder(C 1:T )torespondtocausalqueriesisknownas
NotethatTCPstateinformationiseasytocollect(e.g,using abduction[33,Section4.2.4].Abductioninvolves(i)“invert-
thetcp_infostructureinLinuxsystems[5]).Further,although ing”theobservedvariablestogetthehiddenconfounders;and
wecouldcollecttheinformation,wedonotrequirethevalues (ii)thenmodelingtheproposedchanges(assumingthehidden
{W} ,{B} ,andtreatthesevariablesas confoundervaluesarenowknown)toreturntheanswertothe
| t t∈{1,...,T}\S | t t∈{1,...,T}\S |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
hidden. what-ifquery.AbductionapproachesintheMLliteraturetyp-
Figure 3 shows a directed acyclic graph (DAG) describ- icallyrelyoncomposablestatisticalmodelsusinghigh-level
programminglanguages[11,13,29]that,unfortunately,do
ingthecausaldependenciesforvideostreaming.Notethat
Figure3onlyillustratestheembeddedprocessof{C} , noteffectivelydealwiththeuseofifstatementsandotherde-
|     |     |     |     |     | t   | t∈S∪E |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
{W} ,and{B} ,attheeventtimeswhereanew terministicdecisionfunctionscommoninnetworking.Hence,
| t t∈S∪E | t t∈S∪E |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
chunk is requested or finishes downloading. It is impor- ourworkproposestheVeritascustomabductionmethodtai-
tant to note that the variables C ,W ,B also evolve loredtoourtask,describedinthenextfewparagraphs.
|     |     |     | 1:T | 1:T | 1:T |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in the time between these chunk events, but for any time TheVeritasabductionofC
1:T .Inoursetting,abductionre-
t∈{1,...,T}\{S∪E}thathappensbetweenchunkstartand quiressamplingthenetworkGTBWgivenalltheobservations
| endtimes,therandomvariablesB |     |     | dependsonlyonB   |     |     | (just   | inasession: |     |     |     |     |     |     |
| ---------------------------- | --- | --- | ---------------- | --- | --- | ------- | ----------- | --- | --- | --- | --- | --- | --- |
|                              |     |     | t                |     | t−1 |         |             |     |     |     |     |     |     |
| thevideobeingplayed)andC     |     |     | t dependsonlyonC |     | t−1 | ,butW t |             |     |     |     |     |     |     |
depends on bothW andC if there is an active chunk C ∼P(c |S ,D ,B ,W ), (1)
|          | t−1            |      | t−1 |          |       |        |     | 1:T |     | 1:N 1:N | 1:N s1:N | s1:N |     |
| -------- | -------------- | ---- | --- | -------- | ----- | ------ | --- | --- | --- | ------- | -------- | ---- | --- |
| download | at time t (and | only | onW | if there | is no | active |     |     |     |         |          |      |     |
t−1
| download). |     |     |     |     |     |     | whereR∼gdenotesthatrandomvariableRissampledwith |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
Then-thchunksizeS isinfluenced(throughtheABRalgo- distributiong.OncetheconfoundingvariablesC aresam-
|     |     | n   |     |     |     |     |     |     |     |     |     |     | 1:T |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rithm)byboththebufferstateB sn atthestartofdownloadof pledgiventheobservedvariables,wecansimulatetheeffect
chunknandthelastobservedthroughputY (andpossibly ofthecausalqueryinthesampledC (nowassumedknown).
|     |     |     |     | n−1 |     |     |     |     |     |     | 1:T |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Y ,...,Y The sampling in Equation (1) accounts forthe non-unique
| n−2 | 1 (notshownintheDAG)).Thechunksizevalue |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
S influencesthedownloadtimeD .Further,theTCPstate nature of the “inversion”,imposing a distribution over the
| n   |     |     | n   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
W determines whether the TCP connection of the chunk what-ifqueryresults.ObtainingC requiresconnectingit
| sn  |     |     |     |     |     |     |     |     |     |     | 1:T |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
download experiences slow start restart, initial congestion totheobservedvariables,includingtheobservedthroughput
window etc.,all of which togetherwith S andC ,...,C Y ,TCPstatesW ,asequenceofbufferstatesB ,and
|     |     |     |     | n   | sn  | en  | 1:N |     | s1:N |     |     |     | s1:N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- |
alsoinfluencethedownloadtimeD .Akeyparameterofthe chunksizesS .WediscusshowVeritasachievesthisnext.
|     |     |     | n   |     |     |     |     |     | 1:N |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TCPstateisthegapsincethelastpacketwastransmitted.This AbductionofC viaEHMMs.Veritasusesaspecialtype
1:T
inturndependsonthevideoapplication.Whenthebufferis ofHiddenMarkovModel(HMM)[45].AnHMMisspecified
full,theplayerdoesnotsendfurtherrequests,butwhennot by (i) a set of hidden states C; (ii) a matrix that captures
full,it may triggerrequests immediately. Hence,W itself thetransitionprobabilitiesfromonehiddenstatetoanother;
sn
| dependsonB | ,whichdefinesanewchunkrequestattime |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
en−1 (iii) a set of observations; (iv) a set of probabilities (a.k.a.
s .Finally,asdiscussedaboveS andD togetherdetermine emission probabilities), which capture the likelihood of a
| n   |     |     | n   | n   |     |     |                                                     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| Y . |     |     |     |     |     |     | particularobservationbeinggeneratedfromagivenhidden |     |     |     |     |     |     |
n
Confounders:TheDAGinFigure3showsthatC 1:T arecon- state;and(v)aninitialprobabilitydistributionoverstates.In
foundervariablesbetweenS ,D ,andW .Confounders ourcontext,theGTBWsequenceC ∈CT correspondsto
|     |     | 1:N | 1:N | s1:N |     |     |     |     |     |     | 1:T |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thehiddenstates,whilethethroughputY
arehiddenvariables(notavailableinthedata)thatjointlyin- n istheobservation
fluencemultipleobservedvariables.Moreover,wemakethe jointlyemittedbythestatesC .
sn:en
| simplifyingassumptionthatC |     |     | arenotinfluencedbyany |     |     |     |                |     |              |     | statesW |      |             |
| -------------------------- | --- | --- | --------------------- | --- | --- | --- | -------------- | --- | ------------ | --- | ------- | ---- | ----------- |
|                            |     |     | 1:T                   |     |     |     | The importance |     | of observing |     | TCP     | s1:N | . Note that |
othervariableinthemodel(thatis,chunkdownloadsdonot inanHMM,becauseoftheMarkovproperty,giventhehidden
impacttheGTBW).Ourmodelalsoassumeswearerunninga variable(C ),theemissions(Y )areindependentofthepast
|     |     |     |     |     |     |     |     | sn  |     |     | n   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
particularversionofTCP(e.g.,Cubic,orBBR)andcannotdi- emissions(Y n−1 ,...,Y 1 ).Ingraphicalmodellanguagewesay
rectlybeusedtomodeltheimpactofwhat-ifquestionswhere C needs to d-separateY and {Y ,...,Y }. A sufficient
|     |     |     |     |     |     |     | sn  |     |     | n   | n−1 | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theTCPversionitselfmightchange.Thiswouldrequiremod- conditionforasetU ofvariablestod-separateasetAandBis
eling more intrinsic hidden factors such as the number of thatallundirectedpathsintheDAGbetweenAandBinclude
simultaneousflowsinrouters,etc.. atleastonevariablefromU,andnosuchpathshavearrows
|     |     |     |     |     |     |     | collide“head-to-head”inthevariablesinU |     |     |     |     | [33,Definition |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | -------------- | --- |
3.2 Veritasabductionforcausalqueries
|                                                    |     |     |     |     |     |     | 1.2.3].ThechallengeisthatC |                    |     |     | doesnotd-separateY |     | and |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------------------- | ------------------ | --- | --- | ------------------ | --- | --- |
|                                                    |     |     |     |     |     |     |                            |                    |     |     | sn                 |     | n   |
|                                                    |     |     |     |     |     |     | Y ,...,Y                   | intheDAGofFigure3. |     |     |                    |     |     |
| SincenoothervariablesaffecttheconfoundervariablesC |     |     |     |     |     | 1:T | n−1                        | 1                  |     |     |                    |     |     |
butC directlyorindirectlyaffectallothervariables(i.e., In order to achieve this d-separation independence,Ver-
1:T
allothervariablesaredescendantsofsomevariableinC ), itas conditions the entire HMM on the sequence of TCP
1:T
6

Real Time
Capacity
Transitions
Downloading
Chunks
Capacity-of-Chunk
Transitions
Figure4: TranslationfromRealTimeCapacityTransitiontoDownloadingChunkCapacityTransition.Onthetop,the
GTBW evolves every δ time units. We assume C t is constant in the interval [(t−1)δ,tδ). In the middle lines shows five
downloadingchunks,beginningats andendingate ,n=1,...,5.Atthebottom,underthearrows,weshowthenumberof
|     |     |     |     | n   |     | n   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
GTBWtransitions∆ n betweenconsecutivechunks.Forexample,chunk2andchunk3startatthesametimewindow,so∆ 3 =0,
| whilechunk4andchunk5bothstartatwindow3and5respectively,so∆ |     |     |     |     |     |     |     | =2. |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5
andbuffer1 statesatthechunkstarttimes(W andB ), {0.0Mbps,0.5Mbps,1.0Mbps,···}.Bothhyperparametersδ
|     |     |     |     |     | s1:N | s1:N |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
togetherwiththesequenceofrequestedchunksizes(S 1:N ). andεmaybekeptassmallasneeded.
Thisconditioningultimatelyallowsustod-separateY and ThesequenceC ismodeledasafirst-orderMarkovchain
|     |     |     |     |     |     | n   |     |     |     | 1:T |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{Y ,...,Y }intheDAGofFigure3.Itiseasytocheckthat P(C|C ,···,C )=P(C|C ),1<t≤T.Theconditional
| n−1 | 1   |     |     |     |     |     | t   | 1   | t−1 |     | t t−1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
the variablesC ,W ,B ,S —circledin redin Figure 3— distributionP(C|C )isparameterizedbyatransitionmatrix
|                                 | sn sn | sn  | n   |       |        |     |           |     | t   | t−1 |     |     |     |     |
| ------------------------------- | ----- | --- | --- | ----- | ------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
| blockanyundirectedpathsbetweenY |       |     |     | and{Y | ,...,Y | }in | Asuchthat |     |     |     |     |     |     |     |
|                                 |       |     |     | n     | n−1    | 1   |           |     |     |     |     |     |     |     |
theDAG.
|                                              |     |     |     |     |     |     |     | A   | =P(C | = jε|C | =iε), | 1<t≤T. |     | (2) |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------ | ----- | ------ | --- | --- |
| TheVeritasembeddedMarkovchain.TheHMMthatVer- |     |     |     |     |     |     |     |     | i,j  | t      | t−1   |        |     |     |
itas uses (which we refer to as EHMM) also departs from Fort=1,sincetherearenotransitions,wewilldirectlymodel
| standard | HMM models | in  | other | ways. First, | HMMs | tradi- |             |     |              |     |      |                   |     |         |
| -------- | ---------- | --- | ----- | ------------ | ---- | ------ | ----------- | --- | ------------ | --- | ---- | ----------------- | --- | ------- |
|          |            |     |       |              |      |        | the initial |     | distribution | of  | GTBW | by a distribution |     | u, with |
tionallyusecommonparameterizedprobabilitydistributions
|     |     |     |     |     |     |     | hyperparameter |     | u   | =P(C | =iε). | Finally,given | two | hyper- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | ---- | ----- | ------------- | --- | ------ |
|     |     |     |     |     |     |     |                |     |     | i    | 1     |               |     |        |
(e.g.,multinomial,Guassian)tomodelemissionprobabilities. parameters,GTBWtransitionintervalsizeδandminimum
Instead,Veritasembedsadomain-specificmodelforitsemis-
GTBWdiscrepancyε,wecanmodeltheGTBWevolution
sions.ThemodelcaptureshowGTBW,chunksizes,andTCP
bythetransitionmatrixA(Equation(2))andtheinitialdistri-
statesgetstranslatedintoobservedthroughput.Second,intra-
butionu,thuscanmeasureGTBWevolutiondistributionby
d i t io n a l H M M s , ea c h h i d d e n s ta t e is a s so c i a t e d w it h a si n g l e (cid:0) (cid:1) (cid:0) (cid:1) (cid:0) (cid:12) (cid:1)
|              |                      |           |            |            |                 |              | P C             | =P  | C ∏t | P           | C (cid:12)C           | .        |     |         |
| ------------ | -------------------- | --------- | ---------- | ---------- | --------------- | ------------ | --------------- | --- | ---- | ----------- | --------------------- | -------- | --- | ------- |
|              |                      |           |            |            |                 |              | 1:t             |     | 1    | t(cid:48)=2 | t(cid:48) t(cid:48)−1 |          |     |         |
| o b s e rv a | t io n. H o w e v er | , i n o u | r c o n te | x t, o b s | e r v a ti on s | a re o n l y |                 |     |      |             |                       |          |     |         |
|              |                      |           |            |            |                 |              | Domain-specific |     |      | model       | for emission          | process. |     | As dis- |
associatedwiththosehiddenGTBWstateswherechunksare
beingdownloaded.ThehiddenGTBWitselfchangesduring cussedinSection3.1,foranychunk1≤n≤N,withstarttime
|                                                  |     |     |     |     |     |     | s andendtimee |            |     | ,wewillobservecorrespondingthrough- |     |                 |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------------- | ---------- | --- | ----------------------------------- | --- | --------------- | --- | --- |
| theoffperiodswherenochunksarebeingdownloaded,and |     |     |     |     |     |     | n             |            |     | n                                   |     |                 |     |     |
|                                                  |     |     |     |     |     |     | putY          | ,TCPstateW |     | andchunksizeS                       |     | .ThethroughputY |     |     |
therearenoobservationsavailableduringthistime.Further, n sn n n
|                                                     |     |     |     |     |     |     | observedbyvideochunknisafunctionofGTBWC |     |     |                   |     |     |              | ,the  |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | ----------------- | --- | --- | ------------ | ----- |
| itispossiblethattherearemultiplechunksdownloadedin  |     |     |     |     |     |     |                                         |     |     |                   |     |     |              | sn:en |
|                                                     |     |     |     |     |     |     | startingTCPstateW                       |     |     | ,andthechunksizeS |     |     | ,andwewantto |       |
| thesametimeinterval((t−1)δ,tδ],t∈{1,...,T}.Tohandle |     |     |     |     |     |     |                                         |     |     | sn                |     |     | n            |       |
this,Veritas’sEHMMallowseachGTBWstatetobeassoci- testifanarbitraryGTBWcanfittheobservedchunk.
|                                                    |     |     |     |     |     |     | WedevelopasimplemodelofTCPtoestimateY |                                                 |     |     |     |     | ,denoted |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------------------- | ----------------------------------------------- | --- | --- | --- | --- | -------- | --- |
| atedwithzero,oneormoreobservations(correspondingto |     |     |     |     |     |     |                                       |                                                 |     |     |     |     | n        |     |
|                                                    |     |     |     |     |     |     | by f                                  | (Algorithm4intheAppendix),whichmodelscongestion |     |     |     |     |          |     |
thenumberofchunksdownloadedinthecorrespondinginter-
controlwithslowstart,congestionavoidanceandslowstart
val).NotethatVeritas’suseofEHMMisconsistentwithprior
restart(TCPSSR)[12].IfthenetworkisidleandWlast_send
| work[6,40],whichhasmodeledTCPthroughputevolutionas |     |     |     |     |     |     |     |     |     |     |     |     |     | sn  |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
isgreaterthantheretransmissiontimeoutWrto,TCPSSRis
| aMarkovprocess,butVeritasaddressescomplexitiesassoci- |     |     |     |     |     |     |                                  |     |     |     |     |       | sn           |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | ----- | ------------ | --- |
|                                                       |     |     |     |     |     |     | triggeredandthecongestionwindowW |     |     |     |     | c wnd | andslowstart |     |
| atedwithembeddingacustomemissionprocess,d-separation, |     |     |     |     |     |     |                                  |     |     |     |     | s     |              |     |
n
andthefocusisonabductionforcausalinference. thresholdWssthreshareupdatedaccordingtotheLinuxkernel
sn
implementationbasedon[32].Wecalculatethenumberof
| Hiddenstatetransitions.                             |                 |         | Asdiscussedin§3.1,evolution |             |             |        |              |         |                  |         |               |       |                  |          |
| --------------------------------------------------- | --------------- | ------- | --------------------------- | ----------- | ----------- | ------ | ------------ | ------- | ---------------- | ------- | ------------- | ----- | ---------------- | -------- |
|                                                     |                 |         |                             |             |             |        | transmission |         | rounds           | needed  | to transmit   | a     | chunk with       | size     |
| ofGTBWismodeledasadiscretesequenceC                 |                 |         |                             |             | 1:T ,whereC | t      |              |         |                  |         |               |       |                  |          |
|                                                     |                 |         |                             |             |             |        | S based      | on      | the updatedWcwnd |         | andWssthresh. |       | This             | calcula- |
| denotestheaverageGTBWduringtimeinterval((t−1)δ,tδ]. |                 |         |                             |             |             |        | n            |         |                  |         | sn            | sn    |                  |          |
|                                                     |                 |         |                             |             |             |        | tion         | assumes | that             | in each | round,the     | total | data transmitted |          |
| Further,                                            | for simplicity, | Veritas | uses                        | a quantized | set         | of ca- |              |         |                  |         |               |       |                  |          |
istheminimumoftheBandwidthDelayProduct(BDP)of
| pacities | to ensure the | number | of  | states is | discrete. | GTBW |     |     |     |     |     |     |     |     |
| -------- | ------------- | ------ | --- | --------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
thenetwork,orthecongestionwindow,whicheverislower.
| values C | are quantized | via | a hyperparameter |     | ε > | 0. For |     |     |     |     |     |     |     |     |
| -------- | ------------- | --- | ---------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Wemodelevolutionofthecongestionwindowwithinrounds
| instance, | ε = 0.5 implies |     | that the | hidden | states | are C = |     |     |     |     |     |     |     |     |
| --------- | --------------- | --- | -------- | ------ | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
usingtypicalTCPslowstartbehavior,andusingasimplead-
1ItisinfactnotnecessarytoobserveBs1:N ditiveschemeforcongestionavoidance.Further,lossevents
,asdiscussedintheAppendix.
7

|     |     |     |     |     |     |     |     |                           |          |            |                               | (cid:0)   | (cid:12)                 | (cid:1)        |       |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | -------- | ---------- | ----------------------------- | --------- | ------------------------ | -------------- | ----- |
|     |     |     |     |     |     |     |     | n−1andn,wewilldefineP     |          |            |                               | C =       | jε (cid:12)C             | =iε =(A∆n)     | ,     |
|     |     |     |     |     |     |     |     |                           |          |            |                               | sn        | sn−1                     |                | i,j   |
|     |     |     |     |     |     |     |     | where∆                    |          | =s −s      | andAisasdefinedinEquation(2). |           |                          |                |       |
|     |     |     |     |     |     |     |     |                           | n        | n n−1      |                               |           |                          |                |       |
|     |     |     |     |     |     |     |     | SamplingC                 |          | 1:T . We   | are                           | now ready | to sample                | from           | Equa- |
|     |     |     |     |     |     |     |     | tion                      | (1) with | ourVeritas |                               | EHMM.     | Forease                  | of notation,we |       |
|     |     |     |     |     |     |     |     | define                    | I        | =(I ,···,I | ),where                       | I         | is the discretizedcapac- |                |       |
|     |     |     |     |     |     |     |     |                           | 1:N      | 1          | N                             |           | n                        |                |       |
|     |     |     |     |     |     |     |     | ityindexofchunkn,thatis,C |          |            |                               | sn =I     | n ε.Then,themaximum      |                |       |
likelihoodcapacityassignmentforallchunkswillbe
Figure5:Relativeerrorof f showsacceptableuncertainty. I(cid:63) (cid:0) (cid:1)
|     |     |     |     |     |     |     |     |     |     | 1:N =argmaxlogP |     | I 1:N | |Y 1:N ,W s1:N | ,S 1:N , | (4) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----- | -------------- | -------- | --- |
I1:N
arenotmodeled.Thenumberoftransmissionrounds,themin-
| imumRTTinW |     | ,andthechunksizeS |     |     | ,areallusedtogether |     |     | where |     |     |     |     |     |     |     |
| ---------- | --- | ----------------- | --- | --- | ------------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
|            |     | sn                |     |     | n                   |     |     |       |     |     |     |     |     |     |     |
toestimatetheobservedthroughputofthevideochunk.We
emphasize thatmore detailedmodels thatcapture intricate P(I 1:N |Y 1:N ,W s1:N ,S 1:N )=P(C s1 =I ε) (5)
1
detailsofspecificTCPversionscanbeeasilyincorporatedin
N
ε)∏A∆ n
Veritasinthefuture,buttheabovemodel,whilesimple,helps ×P(Y 1 ,|W s1 ,S 1 ,C s1 =I 1 P(Y n |W sn ,S n ,C sn =I n ε)
In −1,In
| toillustratethefeasibilityandpotentialofVeritas’soverall |     |     |     |     |     |     |     |     |     |     |     | n=2 |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
approachintacklingcausalinference.
|                        |     |     |     |                            |     |     |     | andP(Y | n   | |W sn ,S n ,C | sn =I n | ε)asdefinedinEquation(3). |     |     |     |
| ---------------------- | --- | --- | --- | -------------------------- | --- | --- | --- | ------ | --- | ------------- | ------- | ------------------------- | --- | --- | --- |
| Wetesttheperformanceof |     |     |     | f inanemulationenvironment |     |     |     |        |     |               |         |                           |     |     |     |
TogetEquation(4),weusetheViterbialgorithmwhich
withaservertransmittingpayloadsofdifferentsizes[2KBto
|     |     |     |     |     |     |     |     | searches |     | —via dynamic |     | programming— | for | the values | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------ | --- | ------------ | --- | ---------- | --- |
4MB]toaclient,withrandomintervalsofwaittime[0.12s
|                                               |     |     |     |     |     |     |           | C   | 1:T that | give the | highest | likelihood | in Equation | (5). | The |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | -------- | ------- | ---------- | ----------- | ---- | --- |
| to8s]betweentransmissionofsuccessivepayloads. |     |     |     |     |     |     | f derives |     |          |          |         |            |             |      |     |
vanillaViterbialgorithm[45]assumesaconstanttransition
W sn using the socket stats utility in Linux [4]. The GTBW matrix,whichwereplacebyA∆n
inVeritas.Moredetailsof
| between | client | and server |     | is varied | from | 0.5 to | 10 Mbps, |     |     |     |     |     |     |     |     |
| ------- | ------ | ---------- | --- | --------- | ---- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
theVeritasViterbivariantisprovidedinAlgorithm3inthe
| and the | end to | end delay | is  | varied | from | 5 to 40 | ms using |     |     |     |     |     |     |     |     |
| ------- | ------ | --------- | --- | ------ | ---- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Appendix.
mahimahi[31]acrossexperiments.TheGTBWanddelayis
WewillthenuseViterbioutput(maximumlikelihoodes-
keptconstantforaparticularexperiment.Figure5showsa
timate)tosamplehiddenstatesaccordingtotheposteriorin
CDFoftherelativeerrorbetweentheactualthroughputob-
|                                             |     |     |     |     |     |     |          | Equation                               |     | (1),similarto | [14, | 34, | 36]. Forthe | sampling,we |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | -------------------------------------- | --- | ------------- | ---- | --- | ----------- | ----------- | --- |
| servedbyapayloadandthethroughputestimatedby |     |     |     |     |     |     | f across |                                        |     |               |      |     | (cid:0)     |             |     |
|                                             |     |     |     |     |     |     |          | willadditionallyrequiretheprobabilityP |     |               |      |     |             | C =iε,C     | =   |
allGTBWanddelays.Inmostcases,thepredictedthroughput (cid:12) (cid:1) sn n+1
|     |     |     |     |     |     |     |     | jε(cid:12)Y | ,W  | ,S       | whichcanbeobtainedfromourvariant |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | -------------------------------- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |             | 1:N | s1:N 1:N |                                  |     |     |     |     |
iswithinarangeof1Mbpsoftheobservedthroughputbythe
oftheBaum-Welchforward-backwardalgorithm(seeAlgo-
payload.
rithm2intheAppendix).Wedenotethispairdistribution
f
| If  | were a | perfect | estimator, |                  | we may | have    | modeled |     |     |     |     |     |     |     |     |
| --- | ------ | ------- | ---------- | ---------------- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |        |         |            | (cid:0) (cid:12) |        | (cid:1) |         |     |     |     |     |     |     |     |     |
e m i s si o n p r o b a b ili ti e s a s P Y (cid:12) W , S ,C = c = 1 i f Y = =P (cid:0) C =iε,C = jε (cid:12) (cid:12)Y ,W ,S (cid:1)
(cid:0) (cid:1) (cid:0) (cid:12) n s n n (cid:1) s n n Γ i,j,n sn sn+1 1:N s1:N 1:N . (6)
| f c , W | ,S , a | n d P Y | (cid:12)W | , S , C | = c = | 0 o th | er wi s e . T o |     |     |     |     |     |     |     |     |
| ------- | ------ | ------- | --------- | ------- | ----- | ------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| s n     | n      |         | n s n     | n s     | n     |        |                 |     |     |     |     |     |     |     |     |
taketheuncertaintyof f (Figure5)intoconsideration,wein- ThesamplingalgorithmforC isdefinedasAlgorithm1.
s1:N
cludeawhite-noiseGaussian-distributederrorwithvariance TheintermediatevaluesC wheret∈∪N {s +1,s −1}
|     |     |     |     |     |     |     |     |     |     |     |     | t   | n=2 | n−1 | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
σ2(ahyperparameter):
|     |       |               |     |     |               |                |     | areinterpolatedfromsampledC |                                                  |     |     | s1:N | .   |     |     |
| --- | ----- | ------------- | --- | --- | ------------- | -------------- | --- | --------------------------- | ------------------------------------------------ | --- | --- | ---- | --- | --- | --- |
| P(Y | |W ,S | ,C =c)=Normal |     |     | (cid:0) f(c,W | ,S ),σ2(cid:1) | (3) |                             |                                                  |     |     |      |     |     |     |
| n   | sn n  | sn            |     |     |               | sn n           | .   |                             |                                                  |     |     |      |     |     |     |
|     |       |               |     |     |               |                |     |                             | Input:StatespaceC,LengthT,ViterbioutputI(cid:63) |     |     |      |     |     | ,   |
1:N
NotethattheemissioninEquation(3)doesnotaccountfor TransitionA,PairdistributionΓ
C ,...,C .Inpractice,thissimplificationdoesnothavea Output:AsampledcapacitytraceC
| sn+1                                   | en  |     |     |     |     |              |     |     |      |           |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | ---- | --------- | --- | --- | --- | --- | --- |
| significantimpactinourabilitytosampleC |     |     |     |     |     | asourevalua- |     |     | C =I | (cid:63)ε |     |     |     |     |     |
|                                        |     |     |     |     |     | 1:T          |     |     | sN   | N         |     |     |     |     |     |
forn=N−1to1do
| tionshows.AlsonotethatY |     |     | n   | intheDAGofFigure3doesnot |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
dependonB ,B ,...givenW ,S ,andC (ands ),thus ξ n,i =Γ i,Csn+1 ,n+1 ,iε∈C
|                             | sn  | sn−1 |     | sn              | n                | sn  | n   |     |       |                |         |     |     |     |     |
| --------------------------- | --- | ---- | --- | --------------- | ---------------- | --- | --- | --- | ----- | -------------- | ------- | --- | --- | --- | --- |
| thereisnoneedtouseB         |     |      | ,B  | ,...inestimator |                  |     | f.  |     | Z     | =∑ ξ           |         |     |     |     |     |
|                             |     |      | sn  | sn−1            |                  |     |     |     | n     | i∈C i          |         |     |     |     |     |
|                             |     |      |     |                 |                  |     |     |     | π n,i | =ξ n,i /Z      | n ,iε∈C |     |     |     |     |
| EvolutionoftheembeddedGTBW. |     |      |     |                 | Wenextdiscusshow |     |     |     |       |                |         |     |     |     |     |
|                             |     |      |     |                 |                  |     |     |     | C     | ∼Multinomial(π |         | )   |     |     |     |
we deal with the fact that there may be no observations sn n,:
| attached | to a particular |     | hidden | state | C,  | while | there may |     | end |     |     |     |     |     |     |
| -------- | --------------- | --- | ------ | ----- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
t
Algorithm1:CapacitySampler.Itobtainsthelaststate
| be more | than | one observation |     | for | a different | hidden | C t(cid:48), |     |     |     |     |     |     |     |     |
| ------- | ---- | --------------- | --- | --- | ----------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
N asthelaststateofViterbioutput,thenforwardsamples
| t,t(cid:48) ∈{1,...,T}.           |                                                 | We  | handle | this | through | embedded         | transi-  |                             |     |       |         |     |              |     |     |
| --------------------------------- | ----------------------------------------------- | --- | ------ | ---- | ------- | ---------------- | -------- | --------------------------- | --- | ----- | ------- | --- | ------------ | --- | --- |
|                                   |                                                 |     |        |      |         |                  |          | eachstate                   |     | 1≤n<N | basedon |     | sampledstate | n+1 | and |
| tionsinC                          | s1:N inaproceduresimilartoNealetal.[30].Thatis, |     |        |      |         |                  |          |                             |     |       |         |     |              |     |     |
|                                   |                                                 |     |        |      | (cid:0) | (cid:12) (cid:1) |          | scoresdefinedbyEquation(6). |     |       |         |     |              |     |     |
| fort∈{1,...,T},insteadofmodelingP |                                                 |     |        |      | C       | t(cid:12)C       | ,wemodel |                             |     |       |         |     |              |     |     |
t−1
| the transitions |     | P (cid:0) C | (cid:12) (cid:12)C (cid:1) | ,where | 1<n≤N. | Forchunks |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ----------- | -------------------------- | ------ | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                 |     | sn          | sn−1                       |        |        |           |     |     |     |     |     |     |     |     |     |
8

Counterfactualquery fromthestarttimeofthechunkdownloadtotheendtimeof
Deployed
download.Duringoffperiodswhennoestimateisavailable,
|     |     | Groundtruth |     | Kcounterfactual |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ----------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
answers
|     |     | (GTBW) |     |     |     |     |     | linearinterpolationofthethroughputobservedbytheprevi- |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
ousandnextchunksisused.Theschemeiscommonlyused
SettingA SettingB inmostvideostreamingevaluationstoday.Itisexpectedtobe
KsamplesofC 1:T amoreaccuraterepresentationwhentheobservedthroughput
Observed
|     |     |     |     | Veritas |     |     |     | isclosetoGTBW,butunderestimatesotherwise,andmaybe |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
logs
inaccurateduringoff-periods.
Figure6:UsingVeritasforcounterfactualqueries.
Evaluationsetup.Whenevaluatingcounterfactualques-
3.3 HowVeritasanswerscausalqueries tions,weusetheevaluationsetupsimilartoFigure6.First,
werunavideostreamingsessioninSettingAemulatinga
Figure 6 shows how Veritas may be used to answer coun- groundtruthnetworkbandwidth(GTBW)trace,whichresults
| terfactualandinterventionalqueries. |     |     |     | Thesystem |     | deployed |     |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
inasetoflogs(asdiscussedin§3.3).Next,werunthevideo
inthewild(SettingA)produceslogswhichforeachchunk streamingsessioninSettingBemulatingtracesapproximat-
includes(i)size;(ii)starttimeofdownload;(iii)endtimeof ingGTBWinferredbyVeritasandBaseline,aswellasthe
download;and(iv)TCPstateincludingcwnd,ssthresh,and
originalGTBWtrace.ForVeritas,wesamplemultipletraces
rto[5].Veritasperformstheabductionstep,whichallowsfor (5bydefault),andsummarizearangeofoutcomes.Were-
| thesamplingK |           | likelyGTBWsequencesC |               |     |              | throughEqua- |     |                                                    |     |     |     |     |     |     |
| ------------ | --------- | -------------------- | ------------- | --- | ------------ | ------------ | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|              |           |                      |               |     | 1:T          |              |     | porttheperformancepredictedinSettingBwitheachofthe |     |     |     |     |     |     |
| tion (1).    | The video | session              | is emulatedin |     | a newSetting |              | B   | approaches.                                        |     |     |     |     |     |     |
correspondingtothecounterfactualquery(e.g.,SettingBmay
Evaluationmetrics.Wecompareresultspredictedbyeach
correspondtoadifferentalgorithm,orbuffersize)byreplay-
|     |     |     |     |     |     |     |     | of Veritas,Baseline,and |     | GTBW | with | respect | to  | the actual |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | ---- | ---- | ------- | --- | ---------- |
ingeachofthesesampletracesC 1:T . Veritasthenprovides what-ifscenario.Ourcounterfactualquestionspertaintoim-
| K outcomes | forthe | counterfactual |     | query | ratherthan |     | just a |              |            |     |             |     |            |          |
| ---------- | ------ | -------------- | --- | ----- | ---------- | --- | ------ | ------------ | ---------- | --- | ----------- | --- | ---------- | -------- |
|            |        |                |     |       |            |     |        | pactofchange | of setting | on  | the quality |     | of a video | session. |
singleone,capturingtheuncertaintyinherentintheabduction Hence,weusestandardmetricssuchasvideoquality(mea-
| step given | the | observed | data. While | the | above | description |     |     |     |     |     |     |     |     |
| ---------- | --- | -------- | ----------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
suredbySSIM)andrebufferingratios.
pertainstocounterfactualqueries,Veritascanalsobeusedfor
|     |     |     |     |     |     |     |     | Setup details. | We  | use the | evaluation |     | setup provided | by  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | ---------- | --- | -------------- | --- |
interventionalqueriesaswedescribein§4.4. Fugu [47] to run ouremulation experiments withdifferent
4 Evaluation ABRalgorithms.WeemulateFCCthroughputtraces [1]us-
|                    |     |          |         |               |     |     |     | ingMahimahi | [31]toplaya10minutepre-recordedvideo |     |     |     |     |     |
| ------------------ | --- | -------- | ------- | ------------- | --- | --- | --- | ----------- | ------------------------------------ | --- | --- | --- | --- | --- |
| In this section,we |     | evaluate | Veritas | withrespectto |     | how | ef- |             |                                      |     |     |     |     |     |
clipwithbitraterangingfrom0.1Mbpsto4Mbps.Weuse
fectivelyitcanrespondtocausalqueries(what-ifquestions) theSSIMindex [46]asameasureofvideoquality.Theav-
whengiventracescollectedfromavideostreamingsystem. erageSSIMindexoflowestqualityandhighestqualityare
WestartbyevaluatingVeritas’sabilitytotacklecounterfactual
0.908and0.986respectively.Theclientsarelaunchedinside
queries(§4.1)andthenevaluateitseffectivenessinhandling amahimahishellwitha80msendtoenddelayanddownlink
interventionalqueries(§4.4).
|     |     |     |     |     |     |     |     | GTBW limited | by FCC | traces. | The | GTBW | of FCC | traces |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ------- | --- | ---- | ------ | ------ |
variesfrom3Mbpsto8Mbps.Inourevaluation,weuseMPC
4.1 Evaluationwithcounterfactuals
[48]asdefaultABRalgorithmwithabuffersizeof5seconds.
Giventracescollectedfromavideostreamingsystemwitha VeritasusestheEHMMdescribedin§3.2withGTBWtran-
particularsetofdesigndecisions,weevaluatetheeffective- sitionintervalsizeδ=5sandminimumGTBWdiscrepancy
nessofVeritaswhenansweringwhat-ifquestionsrelatedto
ε=0.5Mbps,varianceσ=0.5,atridiagonaltransitionmatrixA
the performance ofthe system on the same setoftraces if andauniforminitialdistributionuthroughallcapacitystates.
onecouldgobackinthepastanduseanewsetofdecisions. ThetridiagonaltransitionmatrixprioritizesGTBWstatesto
Thedecisionsthatweconsiderinclude(i)changingthesetof bestable,butitallowsvariationovertime.Veritasusesthe
videoqualitiesthatthestreamingalgorithmmaychoosefrom; throughputestimatordescribedin§3.2
(ii)changingthebuffersizeavailabletothevideoplayer;and
|     |     |     |     |     |     |     |     | 4.2 InferencewithVeritas:Example |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- |
(iii)changingtheunderlyingABRalgorithmitself.
Schemescompared.WecompareVeritas’sabilitytohan-
WestartbyillustratingVeritas’sabilitytomoreaccuratelyin-
dlecounterfactualswithtwoapproaches: fertheGTBWtimeseriescomparedtoBaselinewithanexam-
•GroundTruth(GTBW):Thisreferstothegroundtruth ple.Figure7(a)illustratestheGTBWseenduringthesession
bandwidth,definedin §3.1. When answering what-ifques- foran example trace,as wellas the performance observed
tions,results using this technique serve as the idealbench- byBaseline.Therearesignificantperiods(e.g.upto120sec-
mark,thatVeritasandotherapproachesmustseektoachieve. onds,andbetween270and350seconds)whereBaselineis
•Baseline:Thisschemedirectlyusestheobservedthrough- conservativeinitsestimationofGTBW.Thisisbecausein
putofeachchunk,andassumesthisthroughputvalueholds these periods the deployed ABR algorithm selects smaller
9

)spbM( ciffarT noissimsnarT 6 Baseline GTBW )spbM( ciffarT noissimsnarT 6 Veritas (Samples) GTBW
| 5   |     |     |     | 5   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4   |     |     |     | 4   |     |     |     |     |     |
| 3   |     |     |     | 3   |     |     |     |     |     |
| 2   |     |     |     | 2   |     |     |     |     |     |
| 1   |     |     |     | 1   |     |     |     |     |     |
| 0   |     |     |     | 0   |     |     |     |     |     |
0 50 100 150 200 250 300 350 400 0 50 100 150 200 250 300 350 400
|     | Relative Time from Beginning (sec) |     |     |     | Relative Time from Beginning (sec) |     |     |     |     |
| --- | ---------------------------------- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
|     | (a) GTBWandBaseline.               |     |     |     | (b) GTBWandVeritassamples.         |     |     |     |     |
Figure7:ComparingBaseline,GTBWandVeritassamplesforanexampletrace.
chunksizes(eitherlowerqualities,orlower-sizedchunksof
higherqualitygivenvariablebitratevideo). Consequently,  oitar gnireffubeR 6 Baseline
|     |     |     |     | 0.98 |     |     | )noisses fo %(  |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --------------- | --- | --- |
observedthroughputintheseperiodsissignificantlylower Groundtruth (GTBW)
Veritas (Low)
|           |     |     |     | MISS |     |     | 4              |     |     |
| --------- | --- | --- | --- | ---- | --- | --- | -------------- | --- | --- |
| thanGTBW. |     |     |     |      |     |     | Veritas (High) |     |     |
0.97
| Figure7(b)illustratesthetimeseriesreconstructedbyVer- |     |     |     |     |     |     | 2   |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
itasforthesameGTBWtrace.Veritasdoesnotprovideone
|     |     |     |     | 0.96 |     |     | 0   |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
singletrace,butallowssamplingofmultiplecandidatetraces, 0 25 50 75 100
|     |     |     |     | 0   | 25 50 75 | 100 |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
withmoreprobabletraceshavingahigherlikelihoodofbeing Traces Traces
|     |     |     |     |     | (a) SSIM |     | (b) | Rebuffering |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | ----------- | --- |
sampled.ThefigureshowsfivesampletracesfromVeritas.
We make several observations. First,all these samples are Figure9:PredictedperformanceifABRwaschangedfrom
MPCtoBBA.
| closer to GTBW | than Baseline. | Second, in | regions where |     |     |     |     |     |     |
| -------------- | -------------- | ---------- | ------------- | --- | --- | --- | --- | --- | --- |
BaselineisclosetoGTBW(e.g.,between120and270sec-
|     |     |     |     | 0.985 |     |     | 0.15 |     |     |
| --- | --- | --- | --- | ----- | --- | --- | ---- | --- | --- |
onds),allsamplesfromVeritasarealsoclosetoGTBW.This  oitar gnireffubeR
|     |     |     |     | 0.980 |     |     | )noisses fo %(  |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --------------- | --- | --- |
isbecauseintheseregions,thechunksizesselectedbythede- MISS 0.10
0.975
ployedalgorithmexceedthebandwidthdelayproduct(BDP)
|                 |                   |            |              | 0.970 |     |     | 0.05 |     |     |
| --------------- | ----------------- | ---------- | ------------ | ----- | --- | --- | ---- | --- | --- |
| of the network. | Here,the observed | throughput | is closer to |       |     |     |      |     |     |
0.965
| GTBW,andVeritasisrelativelymorecertain. |     |     | Third,inre- |     |       |        | 0.00 |       |        |
| --------------------------------------- | --- | --- | ----------- | --- | ----- | ------ | ---- | ----- | ------ |
|                                         |     |     |             | 0   | 25 50 | 75 100 | 0    | 25 50 | 75 100 |
gionswhereBaselineisconservative,allVeritassamplesare
|     |     |     |     |     | Traces |     |     | Traces |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | ------ | --- |
significantly less conservative. However,in some of these (a) SSIM (b) Rebuffering
regions(e.g.,0to120seconds),Veritasexhibitsmoreuncer-
Figure10:Predictedperformanceifbuffersizewasincreased
tainty.Thisoccursbecauseifsmallerchunksizesarechosen
to30s.
bythedeployedalgorithm,arangeofdifferentGTBWvalues
mayhaveresultedinthesamethroughputobservations.This
ChangeofABRalgorithm.Considerthatthevideostream-
isintrinsic,reflectingtheuncertaintyinherentintheavailable ingapplicationhasbeendeployedwithagivenABR.Weask
data.NotethatVeritas’suseofHMMsallowsittopickmore
thecounterfactualwhatwouldhavehappenedifanalternate
probablesamplesbasedontransitionprobabilities(i.e.,since
ABRalgorithmwereinsteadused.Westudythisquestionin
itinfersGTBWinsomeregionswithhighercertainty,thetran-
thecontextofmovingfromtheMPCalgorithm[48]tothe
sitionprobabilitiesconstraintherangeofGTBWpossibilities
BBAalgorithm[18].Figures8(a)and8(b)showtheSSIM
inthelesscertainregions). andrebufferingratioachievedbyMPCandBBAwhenusing
thesamesetofGTBWtraces.Ineachgraph,eachpointon
|     |     |     |     | the X-Axis | corresponds | to a | GTBW trace,and | each | graph |
| --- | --- | --- | --- | ---------- | ----------- | ---- | -------------- | ---- | ----- |
Setting A (MPC)
| 0.98 |     |  oitar gnireffubeR )noisses fo %(  3 |     |     |     |     |     |     |     |
| ---- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
Setting B (BBA) plotstheSSIM(orrebufferingratio)forthattracewiththe
| 0.97 |     |     |     | two algorithms. | Notice | that | BBA is more | aggressive | with |
| ---- | --- | --- | --- | --------------- | ------ | ---- | ----------- | ---------- | ---- |
| MISS |     | 2   |     |                 |        |      |             |            |      |
largerSSIMvaluesandhigherrebuffering.
0.96
1
Setting A (MPC) We next evaluate the ability of Baseline and Veritas to
Setting B (BBA)
0.95 0 predictthe impacton video performance if(i) logs from a
| 0 25 | 50 75 100 | 0 25 | 50 75 100 |     |     |     |     |     |     |
| ---- | --------- | ---- | --------- | --- | --- | --- | --- | --- | --- |
Traces Traces deployment of the MPC algorithm were provided; and (ii)
|     |      |                 |     | the BBA algorithm |     | were used | instead. Foreach |     | video ses- |
| --- | ---- | --------------- | --- | ----------------- | --- | --------- | ---------------- | --- | ---------- |
| (a) | SSIM | (b) Rebuffering |     |                   |     |           |                  |     |            |
sion,weinferfivesampleGTBWtimeseriesusingVeritas,
Figure8:TrueimpactofchangingABRalgorithmfromMPC
| toBBA. |     |     |     | andemulateeachvideosessionundereachofthefiveVeritas |        |          |              |     |          |
| ------ | --- | --- | --- | --------------------------------------------------- | ------ | -------- | ------------ | --- | -------- |
|        |     |     |     | samples. Each                                       | sample | provides | a prediction | of  | SSIM and |
4.3 Results:Veritaswithcounterfactuals
rebufferingwithVeritas.Weconsiderthesecondlowestand
We nextevaluate Veritas’s ability to answerthree example secondlargestpredictionforeachmetricacrossthesamples,
counterfactualquestions. whichwerefertoasVeritas(Low)andVeritas(High)respec-
10

|     |     |     |     |     |     | to slightly | over-estimate | SSIM | relative to | GTBW. This | is  |
| --- | --- | --- | --- | --- | --- | ----------- | ------------- | ---- | ----------- | ---------- | --- |
0.987
 oitar gnireffubeR because in mosttraces in the deployment,the downloaded
| 0.986 |     |     | )noisses fo %(  |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
10
|            | Baseline           |     |     |     |     | chunksizeswereunderthebandwidthdelayproduct,leading |     |     |     |     |     |
| ---------- | ------------------ | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- |
| MISS 0.985 | Groundtruth (GTBW) |     |     |     |     |                                                     |     |     |     |     |     |
toawiderangeofpossibleGTBWtimeseriesconsistentwith
| 0.984 | Veritas (Low) |     | 5   |     |     |     |     |     |     |     |     |
| ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Veritas (High) theobservedthroughputvalues.Suchvarianceisinherentto
0.983
0 the information in the data. Veritas can provide a range of
0.982
0 25 50 75 100 0 25 50 75 100 outcomesingeneral,andobtainingmoresamplescouldpo-
|     | Traces |     |     | Traces |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
(a) SSIM (b) Rebuffering tentiallyleadtolowerestimates.Overall,Veritasiseffective
inansweringthecounterfactualsandfarmoreaccuratethan
| Figure 11: | Predicted performance |     | if highervideo |     | qualities |     |     |     |     |     |     |
| ---------- | --------------------- | --- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
Baseline.
wereused.
4.4 Evaluationsoninterventionals
tively.ThisprovidesarangeofpredictionswithVeritasfor
Sofar,wehaveevaluatedVeritasoncounterfactualqueries
eachtrace.
Figures 9(a) and 9(b) present the SSIM and rebuffering that involve evaluation on a trace if one could go back to
ratiopredictedbyBaselineandVeritas.Thetrueimpactof thepastandchangethesetting. WenextevaluateVeritas’s
potentialforinterventionalqueries,whichrelatetothefuture
thechange(GTBW)isalsoshownforcomparison.Thegraph
showsthatBaselinepredictsanoticeablylowerSSIMthan (§2),focusingontheabilitytopredictchunkdownloadtimes
GTBW2,andasignificantlyhigherrebufferingratio.Thisis inabias-freefashion.Wecomparetwoschemes:
because Baseline underestimates GTBW as we have seen. •FuguNN:Thisreferstoaneuralnetworkproposedin[47]
In contrast,the range of estimates from Veritas is close to whichpredictsthedownloadtimeofchunksbasedonthesizes
anddownloadtimesofpriorchunks.Whiletheapproachis
GTBWacrossthetracesandfairlytightindicatingVeritasis
confidentinassessingtheimpactofthischange. effectiveatpredictingchunkdownloadtimesforsizesselected
bythedeployedABR,itsuffersfromabiaswhenpredicting
| In the Appendix, | we  | have | also evaluated | the | impact of |     |     |     |     |     |     |
| ---------------- | --- | ---- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
changingfromMPCtotheBOLAalgorithm,whichshows downloadtimesforalternatechunksizesdifferentthanwhat
similarresults:Veritasdoesagoodjobofpredictingtheim- thedeployedABRmayhaveselectedasshownin§2.1.
•Veritas:Usingonlythechunksdownloadeduptoaparticu-
pactofthechange,butBaselinedoesnot.
Change of buffer size. Consider that the video streaming larpointinthesession,weuseVeritastoinferGTBWtime
seriesforthepast.WeconsiderasinglesamplefromVeritas
applicationhasbeendeployedwithanABRandabuffersize.
The designer then asks: what would have been the perfor- correspondingtothemostlikelyone.Wethenusethetransi-
mance if a different buffer size had been used? Intuitively, tionmatrixtogettheexpectedvalueofGTBWforthenext
chunk.
increasingthebuffersizeshouldimprovevideoqualityand
lowerrebuffering,butlowerthelivenessfortheapplication.
)s( emit daolnwod detciderP 50
WedeploytheMPCalgorithmwithabuffersizeof5seconds Perfect predictor
| (SettingA),andusingthelogssoobtained,evaluatetheim- |     |     |     |     |     |     |     | Fugu NN |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
40 Veritas
| pact predicted | by different | schemes | if  | the buffersize | were |     |     |     |     |     |     |
| -------------- | ------------ | ------- | --- | -------------- | ---- | --- | --- | --- | --- | --- | --- |
30
increasedto30seconds(SettingB).Figures10(a)and10(b)
| show the results. | Veritas | accurately | predicts | SSIM | and re- |     | 20  |     |     |     |     |
| ----------------- | ------- | ---------- | -------- | ---- | ------- | --- | --- | --- | --- | --- | --- |
bufferingratio(closetoGTBW),withtherangeofestimates
10
foreachtracebeingrelativelytight.Baselineunderestimates
| SSIMformosttraces,andslightlyover-estimatesrebuffering |     |     |     |     |     |     | 0   |                        |       |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ---------------------- | ----- | --- | --- |
|                                                        |     |     |     |     |     |     | 0   | 10 20                  | 30 40 | 50  |     |
| ratiosforsometraces.                                   |     |     |     |     |     |     |     | True download time (s) |       |     |     |
Changeofqualities.Considerthatthevideostreamingappli- Figure12:ComparingFuguNNandHMMfordownloadtime
predictioninaninterventionalcontext.
cationhasbeendeployedwithagivensetofvideoqualities.
Wenextconsiderthecounterfactual:whatwouldbetheim-
|                                             |     |     |     |     |          | We train | FuguNN | using traces | obtained | by running | the |
| ------------------------------------------- | --- | --- | --- | --- | -------- | -------- | ------ | ------------ | -------- | ---------- | --- |
| pactifahighersetofqualitieswereusedinstead? |     |     |     |     | Figure11 |          |        |              |          |            |     |
MPCalgorithmon100FCCtracessampleduniformlyfrom
shows thatVeritas achieves SSIM andrebuffering close to alltraceswithaverageGTBWvaluesrangingfrom0.5to10
GTBW.However,BaselineunderestimatesSSIMandsignif-
Mbps.Wethencreateaseparatesetof30tracesdrawnfrom
icantlyoverestimatesrebuffering(theestimatesofrebuffer- the same range of GTBW,but where bit rates are selected
ingratiowithBaselineareinthe5-10%rangeacrosstraces, randomly rather than use an ABR algorithm to serve as a
| while the | estimates are | close to | 0 withGTBW |     | andVeritas |     |     |     |     |     |     |
| --------- | ------------- | -------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
testset.ThepurposeistoevaluateFuguNNandVeritason
formosttraces).Notethatforthiscasestudy,Veritastends their ability to predict chunk download times for arbitrary
chunksequences,notspecifictowhatonemayencounterin
2Averagebitrateforthemediantracereducesfromthetruevalueof3.5
thedeployedalgorithm.Eachtesttracegivesusgroundtruth
Mbpsto3.1Mbpsforbaseline.SeeAppendixwhichpresentstheimpacton
informationforthesizeanddownloadtimeforseveralchunk
averagebitrateforallcounterfactualqueries.
11

sequences.WethenrunFuguNNandVeritasofflineforevery worksonlyinferifacorrelationisanindicationofacausalre-
chunksequenceofeachtrace,andobtainthedownloadtime lationshipbutdonotanswerwhat-ifquestions,anddonotdeal
predictedbyeachofthesemethods.Theresultsareshownin withlatentconfounders. Otherworks[20,37,42]consider
Figure12.FuguNNunderestimatesthedownloadtimedueto whatifanalysesforvariousapplications,butdonotaddress
itsassociationalmodelandisunabletoestimatecorrectlyfor confoundingvariables.
interventionalqueriesthatinvolvechunksequencesdifferent Recentwork[23]considerscausalquestionswhileconsid-
thanwhatonemightexpectwiththedeployedABR.Veritas eringimplicitfeedbackinthecontextofcloudsystems–e.g.,
howevercaneffectivelyhandlesuchinterventionalqueries. whenasystemwaitsX minutesforaneventtooccur,there
Notethatasdiscussedin§2.2,thisisimportantwhenusing isimplictfeedbackintermsofwhatwouldhavehappenedif
usingFuguNNasapredictorinalivesessionsinceateach asmallerwaittimewereused.Thisapproachreliesonran-
time step, it is used to predict the download times for all domizedexperiments(fromRLexploration)and,thus,does
possiblechunksizes(notjustthesizethedeployedalgorithm notneedtoexplicitlyconsiderallpossibleconfounders.In
wouldhaveselected). contrast,we are interested in scenarios where randomized
experimentsarelimitedornotavailable.
5 RelatedWork
6 Conclusion
• Biases with video streaming. A very recent parallel
work[7]andapreliminaryworkshoppaper[39]aremotivated Inthispaper,wehavemadethreecontributions.First,wehave
bysimilargoalsasthispaper.However,[39]isrestrictedtoa showncausalreasoningiscomplexwithABRvideo,since
squarewavebandwidthprocess,doesnotmodelthedepen- thequalityofselectedvideochunksiscausallydependenton
denceofobservedthroughputonchunksize,orhandlethe GTBW,whichactsasasequenceoflatentandconfounding
uncertaintyininference.Finally,theuseofmatchingin[39] variables.Second,wepresentVeritas,anovelframeworkthat
requiresbitratestobeoccasionallychosenrandomly.[7]has tacklescausalreasoningforvideostreamingwithoutresort-
anRCTrequirementinthetrainingphasewhereeachofN ingtorandomizedtrials.VeritasusesanembeddedHidden
sessionsisassignedtooneofK ABRpoliciescompletelyat MarkovModelthatrelatesthelatentGTBWtimeseriesto
random,andproposescounterfactualestimationasamatrix throughputobservedbytheapplication.Akeyinsightbehind
completiontask. Asdiscussedin Section2.3,itisunclear VeritasisexploitinginformationabouttheTCPstateatthe
howsuchapproachescanevaluateactionsthatwereoutside start of each chunk download to simplify the causal infer-
thescopeoftheinitialRCTexperiment(e.g.,whatiftheABR ence.Third,weshowtheeffectivenessofVeritasinanswer-
nowallowed8Kvideos,orcoulduseadifferentbuffersize?). ingawiderangeofcounterfactualandinterventionalqueries
Moreover,deployingRCTABRalgorithmstocollecttraces throughemulationtestbedexperiments.Forexample,when
canimpacttheperformanceofreal-worldusers.Incontrast, predictingtheimpactofusinghighervideoqualities,Veritas
ourworkdoes notrequire RCT traces andcan answerany predicts neglible rebuffering ratios,matching ground truth.
what-ifquerywithoutconstraints. However,Baseline(whichdoesnotadjustforcausaleffects)
predictsmuchhighermedianrebufferingratios(6.7%).With
Anotherwork[10]hasobservedthatsmallerchunksizes
interventionalqueriesrelatedtochunkdownloadtimes,Veri-
may see poorerthroughputthan largerones owing to TCP
taspredictsdownloadtimesclosetotruevalues,whileFugu’s
slow start effects. To handle this, [10] compares the total
associationalapproachcanunderestimatechunkdownload
reward seen by algorithm B on a trace collected from an
timesby5.8secondsfor10%ofthechunks,andunderesti-
algorithm A by only considering those chunks where the
matedownloadtimesbyasmuchas35secondsintheworst
new algorithm picks the same bitrate as the old algorithm.
case.
Theapproachdoesnottacklewhat-ifquestions,assumesa
constantbandwidthprocess,anddoesnotmodelthecausal References
dependenceofchunksizeselectionbytheABRalgorithmon
[1] Federal communications commission. 2016. raw
bandwidth.Wetackletheharderproblemofinferringalatent
data - measuring broadband america. (2016).
andvariablebandwidthprocessfromobservedthroughput,
https://www.fcc.gov/reports-research/
deal with the uncertainty in such inference, and address a
reports/measuring-broadband-america/raw-
widerangeofcausalwhat-ifqueries.
data-measuring-broadband-america-2016.
•Inferringcausaldependenciesandwhat-ifanalysis.Sev-
eral works [21, 25, 42] infer causal dependencies using [2] Implementing BOLA-BASIC on puffer. https://
correlations but do not consider latent confounders. Some puffer.stanford.edu/bola/#footnote-1.
work[16,21,22,43]dealswithobservedconfounders–e.g.,
Krishnanetal.[22]exploredwhethervideostreamquality [3] NetflixandYouTubeagreetoreducebitrateduringCoro-
(e.g.,rebuffering ratios) causallyimpacts userengagement naviruscrisis. https://www.broadbandtvnews.com/
metricswhileacccountingforobservedconfounderssuchas 2020/03/19/netflix-agrees-to-reduce-
userconnectiontype(DSLvs.mobile)andlocation.These bitrate-during-coronavirus-crisis/.
12

[4] ss - Linux manualpage. https://man7.org/linux/ [15] AngusDeatonandNancyCartwright. Understanding
man-pages/man8/ss.8.html. andmisunderstandingrandomizedcontrolledtrials. So-
cialScience&Medicine,210:2–21,August2018.
https://man7.org/linux/
[5] tcp-Linuxmanualpage.
man-pages/man7/tcp.7.html. [16] HadrienHours,ErnstBiersack,andPatrickLoiseau. A
|     |     |     |     | Causal | Approach | to the | Study of TCP | Performance. |
| --- | --- | --- | --- | ------ | -------- | ------ | ------------ | ------------ |
[6] Zahaib Akhtar, Yun Seong Nam, Ramesh Govindan, ACMTransactionsonIntelligentSystemsandTechnol-
SanjayRao,JessicaChen,EthanKatz-Bassett,Bruno ogy,7(2):25:1–25:25,December2015.
| Ribeiro,JibinZhan,andHuiZhang.         |                 | Oboe:auto-tuning |         |                                |        |        |              |               |
| -------------------------------------- | --------------- | ---------------- | ------- | ------------------------------ | ------ | ------ | ------------ | ------------- |
|                                        |                 |                  |         | [17] Te-Yuan                   | Huang, | Ramesh | Johari, Nick | McKeown,      |
| videoABRalgorithmstonetworkconditions. |                 |                  | InPro-  |                                |        |        |              |               |
|                                        |                 |                  |         | MatthewTrunnell,andMarkWatson. |        |        |              | Abuffer-based |
| ceedings ofthe                         | 2018 Conference | ofthe ACM        | Special |                                |        |        |              |               |
InterestGrouponDataCommunication-SIGCOMM approachtorateadaptation:Evidencefromalargevideo
streamingservice.InProceedingsofthe2014ACMCon-
’18,pages44–58,Budapest,Hungary,2018.ACMPress.
ferenceonSIGCOMM,SIGCOMM’14,pages187–198,
[7] Abdullah Alomar, Pouya Hamadanian, Arash Nasr- NewYork,NY,USA,2014.ACM.
Esfahany,AnishAgarwal,MohammadAlizadeh,and
|                |            |          |              | [18] Te-Yuan | Huang, | Ramesh | Johari, Nick | McKeown, |
| -------------- | ---------- | -------- | ------------ | ------------ | ------ | ------ | ------------ | -------- |
| Devavrat Shah. | Causalsim: | Toward a | causal data- |              |        |        |              |          |
MatthewTrunnell,andMarkWatson.Abuffer-basedap-
| drivensimulatorfornetworkprotocols. |     | arXivpreprint |     |     |     |     |     |     |
| ----------------------------------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
proachtorateadaptation:Evidencefromalargevideo
arXiv:2201.01811,2022.
|     |     |     |     | streaming | service. | In Proceedings | of  | the 2014 ACM |
| --- | --- | --- | --- | --------- | -------- | -------------- | --- | ------------ |
[8] JoshuaDAngrist,GuidoWImbens,andDonaldBRu- ConferenceonSIGCOMM,SIGCOMM’14,2014.
bin. Identificationofcausaleffectsusinginstrumental
|                                                    |     |     |     | [19] JunchenJiang,VyasSekar,andHuiZhang. |     |     |     | Improving |
| -------------------------------------------------- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --------- |
| variables. JournaloftheAmericanstatisticalAssocia- |     |     |     |                                          |     |     |     |           |
fairness,efficiency,andstabilityinhttp-basedadaptive
tion,91(434):444–455,1996.
|     |     |     |     | video | streaming | with festive. | In Proceedings | of the |
| --- | --- | --- | --- | ----- | --------- | ------------- | -------------- | ------ |
8thInternationalConferenceonEmergingNetworking
[9] EliasBareinboim,AndrewForney,andJudeaPearl.Ban-
ExperimentsandTechnologies,CoNEXT’12,pages97–
ditswithunobservedconfounders:Acausalapproach.
Advances in Neural Information Processing Systems, 108,NewYork,NY,USA,2012.ACM.
28:1342–1350,2015.
[20] YurongJiang,LeninRavindranathSivalingam,Suman
|     |     |     |     | Nath, | and Ramesh | Govindan. | WebPerf: | Evaluating |
| --- | --- | --- | --- | ----- | ---------- | --------- | -------- | ---------- |
[10] MihovilBartulovic,JunchenJiang,SivaramanBalakr-
What-IfScenariosforCloud-hostedWebApplications.
| ishnan,VyasSekar,andBrunoSiñopoli. |     | BiasesinData- |     |     |     |     |     |     |
| ---------------------------------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
InProceedingsoftheConferenceoftheACMSpecial
| DrivenNetworking,andWhattoDoAboutThem. |     |     | In  |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
InterestGrouponDataCommunication-SIGCOMM
Proceedingsofthe16thACMWorkshoponHotTopics
’16,pages258–271,Florianopolis,Brazil,2016.ACM
inNetworks-HotNets-XVI,pages192–198,PaloAlto,
Press.
CA,USA,2017.ACMPress.
[21] SatoruKobayashi,KazukiOtomo,KensukeFukuda,and
[11] EliBingham,JonathanPChen,MartinJankowiak,Fritz HiroshiEsaki. MiningCausalityofNetworkEventsin
Obermeyer,NeerajPradhan,TheofanisKaraletsos,Ro-
|     |     |     |     | LogData. | IEEETransactionsonNetworkandService |     |     |     |
| --- | --- | --- | --- | -------- | ----------------------------------- | --- | --- | --- |
hitSingh,PaulSzerlip,PaulHorsfall,andNoahDGood-
Management,15(1):53–67,March2018.
man. Pyro:DeepUniversalProbabilisticProgramming.
Journal of Machine Learning Research, 20(28):1–6, [22] S. Shunmuga Krishnan and Ramesh K. Sitaraman.
| 2019. |     |     |     | Video                                        | stream quality | impacts | viewer | behavior: infer- |
| ----- | --- | --- | --- | -------------------------------------------- | -------------- | ------- | ------ | ---------------- |
|       |     |     |     | ringcausalityusingquasi-experimentaldesigns. |                |         |        | InPro-           |
[12] EthanBlanton,Dr.VernPaxson,andMarkAllman.TCP ceedingsofthe2012InternetMeasurementConference,
| CongestionControl. | RFC5681,September2009. |     |     |     |     |     |     |     |
| ------------------ | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
IMC’12,pages211–224,Boston,Massachusetts,USA,
November2012.AssociationforComputingMachinery.
[13] BobCarpenter,AndrewGelman,MatthewD.Hoffman,
DanielLee,BenGoodrich,MichaelBetancourt,Marcus [23] Mathias Lécuyer, Sang Hoon Kim, Mihir Nanavati,
Brubaker,JiqiangGuo,PeterLi,andAllenRiddell.Stan:
JunchenJiang,SiddharthaSen,AleksandrsSlivkins,and
A Probabilistic Programming Language. Journal of AmitSharma. Sayer:UsingImplicitFeedbacktoOp-
StatisticalSoftware,76(i01),2017.
|     |     |     |     | timize | System Policies. |     | ACM Symposium | on Cloud |
| --- | --- | --- | --- | ------ | ---------------- | --- | ------------- | -------- |
Computing(SOCC),NewYork,NY,USA,2021.
| [14] SiddharthaChib. | Calculatingposteriordistributionsand |     |     |     |     |     |     |     |
| -------------------- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
modalestimatesinmarkovmixturemodels. Journalof [24] XiLiu,FlorinDobrian,HenryMilner,JunchenJiang,
Econometrics,75(1):79–97,1996. VyasSekar,Ion Stoica,andHui Zhang. A casefora
13

coordinated internet video control plane. ACM SIG- [35] KennethJ.RothmanandSanderGreenland. Causation
COMMComputerCommunicationReview,42(4):359– andcausalinferenceinepidemiology.AmericanJournal
| 370,2012. |     |     |     | ofPublicHealth,95Suppl1:S144–150,2005. |                                    |     |     |     |
| --------- | --- | --- | --- | -------------------------------------- | ---------------------------------- | --- | --- | --- |
|           |     |     |     | [36] StevenLScott.                     | Bayesiananalysisofatwo-statemarkov |     |     |     |
[25] AjayAnilMahimkar,ZihuiGe,AmanShaikh,JiaWang,
JenniferYates,YinZhang,andQiZhao. Towardsauto- modulatedpoissonprocess. JournalofComputational
andGraphicalStatistics,8(3):662–670,1999.
matedperformancediagnosisinalargeIPTVnetwork.
| ACM SIGCOMM | Computer | Communication | Review, |     |     |     |     |     |
| ----------- | -------- | ------------- | ------- | --- | --- | --- | --- | --- |
[37] RahulSingh,PrashantShenoy,MaitreyaNatu,Vaishali
39(4):231–242,2009. Publisher:ACMNewYork,NY, Sadaphal,and Harrick Vin. Analytical modeling for
USA.
what-ifanalysisincomplexcloudcomputingapplica-
|     |     |     |     | tions. | ACM SIGMETRICS | Performance |     | Evaluation |
| --- | --- | --- | --- | ------ | -------------- | ----------- | --- | ---------- |
[26] HongziMao,RaviNetravali,andMohammadAlizadeh.
Review,40(4):53–62,April2013.
| Neuraladaptivevideostreamingwithpensieve. |     |     | InPro- |     |     |     |     |     |
| ----------------------------------------- | --- | --- | ------ | --- | --- | --- | --- | --- |
ceedingsoftheConferenceoftheACMSpecialInterest [38] KevinSpiteri,RahulUrgaonkar,andRameshKSitara-
GrouponDataCommunication,pages197–210.ACM, man. Bola:Near-optimalbitrateadaptationforonline
| 2017. |     |     |     | videos. | In IEEE INFOCOM | 2016-The | 35th | Annual |
| ----- | --- | --- | --- | ------- | --------------- | -------- | ---- | ------ |
IEEEInternationalConferenceonComputerCommuni-
[27] TomMitchellandMachineLearningMcGraw-Hill.Edi-
cations,pages1–9.IEEE,2016.
tion,1997.
|     |     |     |     | [39] P.C.Sruthi,SanjayRao,andBrunoRibeiro. |     |     |     | Pitfallsof |
| --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | ---------- |
[28] Yun Seong Nam,Jianfei Gao,Chandan Bothra,Ehab data-drivennetworking: Acasestudyoflatentcausal
Ghabashneh,Sanjay Rao,Bruno Ribeiro,Jibin Zhan, confounders in video streaming. In Proceedings of
theWorkshoponNetworkMeetsAI&ML,NetAI’20,
| and Hui | Zhang. Xatu: Richer | neural network | based |     |     |     |     |     |
| ------- | ------------------- | -------------- | ----- | --- | --- | --- | --- | --- |
prediction for video streaming. ACM SIGMETRICS, page 42–47,New York,NY,USA,2020. Association
forComputingMachinery.
2022.
[40] YiSun,XiaoqiYin,JunchenJiang,VyasSekar,Fuyuan
[29] SiddharthNarayanaswamy,BrooksPaige,Jan-Willem
|                                  |     |     |          | Lin,NanshuWang,TaoLiu,andBrunoSinopoli. |     |     |     | Cs2p: |
| -------------------------------- | --- | --- | -------- | --------------------------------------- | --- | --- | --- | ----- |
| vandeMeent,AlbanDesmaison,NoahD. |     |     | Goodman, |                                         |     |     |     |       |
Improvingvideobitrateselectionandadaptationwith
| Pushmeet                                           | Kohli, Frank D. | Wood, and Philip | H. S. |             |                       |     |                |     |
| -------------------------------------------------- | --------------- | ---------------- | ----- | ----------- | --------------------- | --- | -------------- | --- |
|                                                    |                 |                  |       | data-driven | throughputprediction. |     | In Proceedings | of  |
| Torr. Learningdisentangledrepresentationswithsemi- |                 |                  |       |             |                       |     |                |     |
the2016ACMSIGCOMMConference,pages272–285,
| supervised | deep generative | models. In | NIPS, pages |     |     |     |     |     |
| ---------- | --------------- | ---------- | ----------- | --- | --- | --- | --- | --- |
2016.
5927–5937,2017.
|     |     |     |     | [41] CharlesSuttonandAndrewMccallum. |     |     | AnIntroduction |     |
| --- | --- | --- | --- | ------------------------------------ | --- | --- | -------------- | --- |
[30] RadfordNeal,MatthewBeal,andSamRoweis.Inferring
toConditionalRandomFieldsforRelationalLearning.
statesequencesfornon-linearsystemswithembedded Graph.Models,7:93,2002.
| hiddenmarkovmodels. | Advancesinneuralinformation |     |     |     |     |     |     |     |
| ------------------- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
[42] MukarramTariq,AmgadZeitoun,VytautasValancius,
processingsystems,16,2003.
NickFeamster,andMostafaAmmar.Answeringwhat-if
[31] Ravi Netravali, Anirudh Sivaraman, Keith Winstein, deploymentandconfigurationquestionswithwise. In
Somak Das, Ameesh Goyal, and Hari Balakrishnan. ProceedingsoftheACMSIGCOMM2008Conference
onDatacommunication,pages99–110,2008.
Mahimahi:Alightweighttoolkitforreproducibleweb
| measurement. | InProceedingsofthe2014ACMCon- |     |     |               |                   |     |                    |     |
| ------------ | ----------------------------- | --- | --- | ------------- | ----------------- | --- | ------------------ | --- |
|              |                               |     |     | [43] Mukarram | Bin Tariq,Murtaza |     | Motiwala,NickFeam- |     |
ferenceonSIGCOMM,SIGCOMM’14,page129–130,
|     |     |     |     | ster,andMostafaAmmar. |     | Detectingnetworkneutrality |     |     |
| --- | --- | --- | --- | --------------------- | --- | -------------------------- | --- | --- |
NewYork,NY,USA,2014.AssociationforComputing
|     |     |     |     | violationswithcausalinference. |     |     | InProceedingsofthe |     |
| --- | --- | --- | --- | ------------------------------ | --- | --- | ------------------ | --- |
Machinery.
5thInternationalConferenceonEmergingNetworking
ExperimentsandTechnologies,pages289–300,2009.
[32] JitendraPadhye,SallyFloyd,andMarkJ.Handley.TCP
CongestionWindowValidation. RFC2861,June2000. [44] GuibinTianandYongLiu. Towardsagileandsmooth
|                   |                      |            |        | videoadaptationindynamichttpstreaming. |     |     |     | InProceed- |
| ----------------- | -------------------- | ---------- | ------ | -------------------------------------- | --- | --- | --- | ---------- |
| [33] Judea Pearl. | Causality. Cambridge | university | press, |                                        |     |     |     |            |
ingsofthe8thInternationalConferenceonEmerging
2009.
|     |     |     |     | Networking | Experiments | and Technologies,CoNEXT |     |     |
| --- | --- | --- | --- | ---------- | ----------- | ----------------------- | --- | --- |
’12,2012.
| [34] ChristianPRobertandDMTitterington. |     | Reparameteri- |     |     |     |     |     |     |
| --------------------------------------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
zationstrategiesforhiddenmarkovmodelsandbayesian [45] AndrewJViterbi. Apersonalhistoryoftheviterbial-
approachestomaximumlikelihoodestimation. Statis- gorithm. IEEESignalProcessingMagazine,23(4):120–
| ticsandComputing,8(2):145–158,1998. |     |     |     | 142,2006. |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --------- | --- | --- | --- | --- |
14

[46] ZhouWang,A.C.Bovik,H.R.Sheikh,andE.P.Simon-
| celli. | Image      | quality     | assessment: | from         | errorvisibility |       |
| ------ | ---------- | ----------- | ----------- | ------------ | --------------- | ----- |
| to     | structural | similarity. | IEEE        | Transactions | on              | Image |
Processing,13(4):600–612,2004.
| [47] Francis              | Y.        | Yan, Hudson  | Ayers, | Chenzhi            | Zhu,       | Sadjad |
| ------------------------- | --------- | ------------ | ------ | ------------------ | ---------- | ------ |
| Fouladi,                  |           | Jam˜es Hong, | Keyi   | Zhang, Philip      | Levis,     | and    |
| Keith                     | Winstein. | Learning     |        | in situ: a         | randomized | ex-    |
| perimentinvideostreaming. |           |              |        | In17thUSENIXSympo- |            |        |
siumonNetworkedSystemsDesignandImplementation
(NSDI20),pages495–511,2020.
| [48] Xiaoqi                     | Yin,Abhishek |                     | Jindal,Vyas | Sekar,and       |             | Bruno |
| ------------------------------- | ------------ | ------------------- | ----------- | --------------- | ----------- | ----- |
| Sinopoli.                       |              | A control-theoretic |             | approach        | for dynamic |       |
| adaptivevideostreamingoverhttp. |              |                     |             | InProceedingsof |             |       |
the2015ACMConferenceonSpecialInterestGroupon
DataCommunication,SIGCOMM’15,London,United
Kingdom,2015.
15

| A Appendix         |     |     |     |     |     | withGTBWforvariouscounterfactualqueries. |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
| A.1 FurtherResults |     |     |     |     |     | A.2 ModelandAlgorithms                   |     |     |     |     |     |
Inthispart,wewillclarifysomedetailsofourmodelsand
presentpseudocodeforallalgorithms:Viterbivariant,Baum-
0.98  oitar gnireffubeR Baseline Welchforward-backwardvariantandnetworkthroughputes-
|           |     |     | )noisses fo %(  | Groundtruth (GTBW) |     |                       |     |     |     |     |     |
| --------- | --- | --- | --------------- | ------------------ | --- | --------------------- | --- | --- | --- | --- | --- |
|           |     |     | 10              |                    |     | timatorusedinourEHMM. |     |     |     |     |     |
| MISS 0.97 |     |     |                 | Veritas (Low)      |     |                       |     |     |     |     |     |
Veritas (High)
| 0.96 |     |     |     |     |     | WhyB                                                    | neednotbeobserved. |     | InFigure3’sDAG,start        |     |     |
| ---- | --- | --- | --- | --- | --- | ------------------------------------------------------- | ------------------ | --- | --------------------------- | --- | --- |
|      |     |     | 5   |     |     | s1:N                                                    |                    |     |                             |     |     |
| 0.95 |     |     |     |     |     | times 1:N arenotdefinedasrandomvariablestosimplifyexpo- |                    |     |                             |     |     |
|      |     |     | 0   |     |     | sition.Ifwehaddefineds                                  |                    |     | asanobservedrandomvariable, |     |     |
1:N
0 25 50 75 100 0 25 50 75 100 s couldhavebeenusedinplaceofB todefinethesuffi-
|     | Traces |     |     | Traces |     | 1:N |     |     | sn−1 |     |     |
| --- | ------ | --- | --- | ------ | --- | --- | --- | --- | ---- | --- | --- |
(a) SSIM (b) Rebuffering cientsetofobservedvariablesinourd-separationargument.
|     |     |     |     |     |     |                                |     |     | (cid:0) | (cid:12)      | (cid:1) |
| --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | ------- | ------------- | ------- |
|     |     |     |     |     |     | LookingatthedependencebetweenP |     |     | C       | = jε(cid:12)C | =iε     |
|     |     |     |     |     |     |                                |     |     | sn      |               | sn−1    |
Figure13:ChangeofABRfromMPCtoBola.
|     |     |     |     |     |     | and ∆ n makes | it clearthat | observing | s 1:N is | also | necessary |
| --- | --- | --- | --- | --- | --- | ------------- | ------------ | --------- | -------- | ---- | --------- |
Figure13(b)andFigure13(a)showtheSSIMandrebuffering forourMarkovmodel.Toconclude,then,wedonotactually
ratiopredictedbyVeritasandBaselinewhenwechangethe need to log B since s is necessary and sufficient and
s1:N 1:N
algorithmfromMPCandBola[38].WeusetheBolaBasicV1 readilyavailableinthetrace.
algorithmimplementedinthePuffersetupforthisanalysis[2].
|     |     |     |     |     |     | Algorithm | Pseudo Codes. |     | As introduced | in Section | 3.2, |
| --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | ------------- | ---------- | ---- |
TheresultsaresimilartothatofchangingtheABRfromMPC ourViterbiandBaum-Welchforward-backwardvariantsare
toBBA.BaselineunderestimatestheGTBWwhichleadsto
|     |     |     |     |     |     | nearly the | same as their | origins, | but replace | the | transition |
| --- | --- | --- | --- | --- | --- | ---------- | ------------- | -------- | ----------- | --- | ---------- |
lowerSSIMandhigherrebuffering.Veritasdoesagoodjob
|     |     |     |     |     |     | matrixfromconstantmatrixAtoA∆n |     |     | where∆ | isasshown |     |
| --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | ------ | --------- | --- |
n
ofpredictingtheimpactofthechange,butBaselinedoesnot.
inSection3.2andFigure4,andreplacetheemissionprocess
byourproposalasEquation(3).Thepseudocodesofboth
| 4.0                 |     |     |                     |     |     | algorithmsareprovidedinAlgorithm3andAlgorithm2. |     |                                 |     |     |     |
| ------------------- | --- | --- | ------------------- | --- | --- | ----------------------------------------------- | --- | ------------------------------- | --- | --- | --- |
| )spbM( etartib .gvA |     |     | )spbM( etartib .gvA |     |     |                                                 |     |                                 |     |     |     |
| 3.5                 |     |     |                     |     |     | Weuseasimplemodel                               |     | f,whichestimatesthroughputgiven |     |     |     |
3.5
| 3.0 |     |     |     |     |     | GTBW,TCPstateandsizeofrelateddownloadchunk.The |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- |
3.0
| 2.5 |     |     |     |     |     | pseudocodeisprovidedinAlgorithm4. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- |
2.0
2.5
Setting A
| 1.5                 |        | Setting B    |                                 |        |        |     |     |     |     |     |     |
| ------------------- | ------ | ------------ | ------------------------------- | ------ | ------ | --- | --- | --- | --- | --- | --- |
| 0                   | 25 50  | 75           | 100 0                           | 25 50  | 75 100 |     |     |     |     |     |     |
|                     | Traces |              |                                 | Traces |        |     |     |     |     |     |     |
| (a) Avg. bitratein  |        | SettingAandB | (b) Avg.bitrateforchangefromMPC |        |        |     |     |     |     |     |     |
| (MPCandBBA).        |        |              | toBBA.                          |        |        |     |     |     |     |     |     |
| )spbM( etartib .gvA |        |              | )spbM( etartib .gvA             |        |        |     |     |     |     |     |     |
| 3.5                 |        |              | 3.5                             |        |        |     |     |     |     |     |     |
Baseline
| 3.0 |     |     | 3.0 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Groundtruth (GTBW)
Veritas (Low)
| 2.5                             |        |     | 2.5                               | Veritas (High) |     |     |     |     |     |     |     |
| ------------------------------- | ------ | --- | --------------------------------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
| 0                               | 20 40  | 60  | 80 0                              | 25 50          | 75  |     |     |     |     |     |     |
|                                 | Traces |     |                                   | Traces         |     |     |     |     |     |     |     |
| (c) Avg.bitrateforchangefromMPC |        |     | (d) Avg. bitrateforchangingbuffer |                |     |     |     |     |     |     |     |
| toBola.                         |        |     | size.                             |                |     |     |     |     |     |     |     |
)spbM( etartib .gvA
3.5
Baseline
Groundtruth (GTBW)
|     |     | 3.0 | Veritas (Low) |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Veritas (High)
2.5
2.0
|     |     | 0   | 25 50 75 | 100 |     |     |     |     |     |     |     |
| --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Traces
|     | (e) | Avg. bitrate | forchanging | quali- |     |     |     |     |     |     |     |
| --- | --- | ------------ | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
ties.
Figure14:Avg.bitrateforcounterfactualqueries.
| Figure14comparestheAvg.bitrateforBaselineand |     |     |     |     | Veritas |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
16

Input:StateSpaceC,TransitiontimesT,Initial
|     | distributionu |                            | 1 ,TransitionmatrixA,Emission |     |     |     |     |     |     |     |     |     |     |
| --- | ------------- | -------------------------- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | processE      | (Equation(3)),ThroughputsY |                               |     |     | ,   |     |     |     |     |     |     |     |
1:N
|     | TCPstatesW |     | ,ChunksizesS |     |               |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |            |     | s1:N         |     | 1:T ,interval |     |     |     |     |     |     |     |     |
gaps∆,capacityunitε
Output:ConditionalJointDistributionΓ
| /* Alias    |      |              |                                |                |         | */  |     |     |     |     |     |     |     |
| ----------- | ---- | ------------ | ------------------------------ | -------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ξb a c k=A∆ | n E  | (cid:0) Y ,W | ,S (cid:12) (cid:12)jε (cid:1) | ,∀i,j∈C,∀2≤n≤N |         |     |     |     |     |     |     |     |     |
| i, j ,n     | i, j | n sn         | n                              |                |         |     |     |     |     |     |     |     |     |
| ξf o r e    | ∆    | (cid:0)      |                                | (cid:12)       | (cid:1) |     |     |     |     |     |     |     |     |
=A n +1E Y n+1 ,W sn+1 ,S n+1 (cid:12)jε ,∀i,j∈C,∀1≤ Input:StateSpaceC,TransitiontimesT,Initial
| i, j , n | i, j |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n≤N−1
|            |         |       |                   |     |     |     |     | distributionu |     | 1 ,TransitionmatrixA,Emission |     |               |     |
| ---------- | ------- | ----- | ----------------- | --- | --- | --- | --- | ------------- | --- | ----------------------------- | --- | ------------- | --- |
| /* Forward |         |       |                   |     |     | */  |     |               |     |                               |     |               |     |
|            |         |       |                   |     |     |     |     | processE      |     | (Equation(3)),ThroughputsY    |     |               | ,   |
|            | (cid:0) |       | (cid:12) (cid:1)  |     |     |     |     |               |     |                               |     |               | 1:N |
| α =u       | E Y     | ,W ,S | 1(cid:12)iε ,∀i∈C |     |     |     |     | TCPstatesW    |     | ,ChunksizesS                  |     |               |     |
| 1,i        | 1,i     | 1 s1  |                   |     |     |     |     |               |     | s1:N                          |     | 1:T ,interval |     |
| forn=2−→N  |         | do    |                   |     |     |     |     |               |     |                               |     |               |     |
gaps∆,capacityunitε
| α   | = ∑ | α     | ξb a c k,∀i∈C |     |     |     | Output:MostLikelyStateTraceI∗ |        |          |                         |     |     |     |
| --- | --- | ----- | ------------- | --- | --- | --- | ----------------------------- | ------ | -------- | ----------------------- | --- | --- | --- |
| n,i |     | n−1,j | j, i ,n       |     |     |     |                               |        |          |                         |     |     |     |
|     | j∈C |       |               |     |     |     |                               |        | (cid:0)  | (cid:12) (cid:1)        |     |     |     |
|     |     |       |               |     |     |     | ξ 1,i                         | =u 1,i | E Y 1 ,W | s1 ,S 1(cid:12)iε ,∀i∈C |     |     |     |
end
|          |           |     |     |     |     |     | forn=2−→N |                |     | do         |           |                       |     |
| -------- | --------- | --- | --- | --- | --- | --- | --------- | -------------- | --- | ---------- | --------- | --------------------- | --- |
| / * B ac | k w a r d |     |     |     |     | */  |           |                |     |            |           |                       |     |
|          |           |     |     |     |     |     |           |                |     | A∆ (cid:0) |           | (cid:12) (cid:1)      |     |
|          |           |     |     |     |     |     |           | x n,i =argmaxξ |     | 1,j n E    | Y n ,W sn | ,S n (cid:12)iε ,∀i∈C |     |
| β N,i =  | 1 , ∀ i ∈ | C   |     |     |     |     |           |                |     | j, i       |           |                       |     |
j∈C
| forn = | N− 1   | − → 1    | d o         |     |     |     |     |      |        | (cid:0)   | (cid:12)      | (cid:1) |     |
| ------ | ------ | -------- | ----------- | --- | --- | --- | --- | ---- | ------ | --------- | ------------- | ------- | --- |
|        |        |          |             |     |     |     |     | ξ =ξ | A∆     | n E Y ,W  | ,S (cid:12)iε | ,∀i∈C   |     |
|        |        | f o r e  |             |     |     |     |     | n,i  | 1,xn,i | xn ,i,i n | sn n          |         |     |
| β n    | ,i = ∑ | ξ β n    | + 1,j ,∀i∈C |     |     |     |     |      |        |           |               |         |     |
|        |        | i, j , n |             |     |     |     | end |      |        |           |               |         |     |
j∈C
I ∗ =argmaxξ
| end          |     |     |     |     |     |     | N   |     | N,i |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /* Posterior |     |     |     |     |     | */  |     | i∈C |     |     |     |     |     |
forn=N−1−→1do
forn=1−→N−1do
I ∗=x
|        |     |     |     |     |     |     |     | n   | n+1,I ∗ |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
| fori∈C |     | do  |     |     |     |     |     |     | n +1    |     |     |     |     |
end
|     | fori∈C | do  |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
f o r e Algorithm 3: Viterbi Algorithm. It can search for the
|     |     |     | α n ,iξ i , j | , n β n + 1 , j βn | + 1, j |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------- | ------------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Γ i,j,n = m o s t l ik e l y G T B W st a t e t ra c e I ∗ w h i ch c a n g en e r at e g iv e n
|     |     |     | ∑ ∑ α | ξ f o r e β | ,lβ |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t , k k , l , n n + 1 n +1,l ob s e r v a ti o n s Y ,W S , o n a l l ch u n k s th r o u g h d y -
|     |     | k∈  | C l∈ C |     |     |     |     |     | 1:N | s , 1 :N |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
|     | end |     |        |     |     |     |     |     |     | 1 :N     |     |     |     |
namicprogramming.
end
end
| Algorithm | 2:  | Forward-Backward |     |     | Algorithm. | It  |     |     |     |     |     |     |     |
| --------- | --- | ---------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:0)
| first computes |         | forward              | distribution |           | α = P          | C =     |     |     |     |     |     |     |     |
| -------------- | ------- | -------------------- | ------------ | --------- | -------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| (cid:12)       |         | (cid:1)              |              |           | n,i            | sn      |     |     |     |     |     |     |     |
| iε(cid:12)Y ,W | ,S      | ; thencomputesbackwa |              |           | rddistribution |         |     |     |     |     |     |     |     |
| 1:n            | s1:n    | 1:n                  |              |           |                |         |     |     |     |     |     |     |     |
|                | (cid:0) | (cid:12)             |              |           | (cid:1)        |         |     |     |     |     |     |     |     |
| β n,i =        | P C sn  | = iε(cid:12)Y n+1:N  | ,W           | sn+1:N ,S | n+1:N ; and    | finally |     |     |     |     |     |     |     |
(cid:0)
| achieve | conditional            | joint    | distribution |                             | Γ = P | C = |     |     |     |     |     |     |     |
| ------- | ---------------------- | -------- | ------------ | --------------------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
|         |                        |          |              |                             | i,j,n | sn  |     |     |     |     |     |     |     |
| iε,C    | = jε(cid:12)Y (cid:12) | ,W       | ,S           | (cid:1) bycombiningαandβfor |       |     |     |     |     |     |     |     |     |
| sn+1    |                        | 1:N s1:N | 1:N          |                             |       |     |     |     |     |     |     |     |     |
alli,jinGTBWstatespacefrom1toN−1chunks.
17

| Input:C,TCPstateW | ,ChunksizeS  |       |     |
| ----------------- | ------------ | ----- | --- |
|                   | Sn           | n     |     |
| Output:Y n        |              |       |     |
| /* Calculating    | ssthresh and | cwnd. | */  |
ifWlast_snd
>Wrtothen
| Sn      | Sn             |     |     |
| ------- | -------------- | --- | --- |
| /* Slow | start restart. |     | */  |
init_cwnd←10
while((Wlast_snd−Wrto)>0)and
Sn Sn
| (Wcwnd | >init_cwnd))do |     |     |
| ------ | -------------- | --- | --- |
Sn
| Wlast_snd | =Wlast_snd−Wrto |     |     |
| --------- | --------------- | --- | --- |
| Sn        | Sn              | Sn  |     |
| Wcwnd     | ←Wcwnd <<2      |     |     |
| Sn        | Sn              |     |     |
end
| Wssthresh←max(Wssthresh,(Wcwnd |     | >>  |     |
| ------------------------------ | --- | --- | --- |
| Sn                             | Sn  | Sn  |     |
1)+(Wcwnd
>>2))
Sn
end
| /* Get number                | of data segments. |     | */  |
| ---------------------------- | ----------------- | --- | --- |
| data_segments←get_segments(S |                   | )   |     |
n
bdp_segments←get_segments(GTBW∗Wmin_rtt)
Sn
ifWcwnd >bdp_segmentsthen
Sn
ifdata_segments>bdp_segmentsthen
returnC
else
/Wmin_rtt
returnS
n Sn
end
else
rounds←0
sent←0
whilesent<data_segmentsdo
sent←sent+min(Wcwnd,bdp_segments)
Sn
| ifWcwnd | <Wssthreshthen |     |     |
| ------- | -------------- | --- | --- |
Sn Sn
Wcwnd ←2∗Wcwnd
Sn Sn
else
Wcwnd ←Wcwnd+1
Sn Sn
end
rounds←rounds+1
end
/(rounds∗Wmin_rtt),C)
returnmin((S
|     | n   | Sn  |     |
| --- | --- | --- | --- |
end
| Algorithm4:Networkthroughputestimator: |     |     | f   |
| -------------------------------------- | --- | --- | --- |
18