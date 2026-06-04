Oboe: Auto-tuning Video ABR Algorithms to
Network Conditions
Zahaib Akhtar* Yun Seong Nam* Ramesh Govindan
UniversityofSouthernCalifornia PurdueUniversity UniversityofSouthernCalifornia
Sanjay Rao Jessica Chen Ethan Katz-Bassett
PurdueUniversity UniversityofWindsor ColumbiaUniversity
Bruno Ribeiro Jibin Zhan Hui Zhang
PurdueUniversity Conviva Conviva
ABSTRACT Network Conditions. In SIGCOMM ’18: ACM SIGCOMM 2018
Mostcontentprovidersareinterestedinprovidinggoodvideo Conference, August 20–25, 2018, Budapest, Hungary. 15 pages.
deliveryQoEforallusers,notjustonaverage.State-of-the-art https://doi.org/10.1145/3230543.3230558
ABRalgorithmslikeBOLAandMPCrelyonparametersthat
1 INTRODUCTION
aresensitivetonetworkconditions,somayperformpoorly
for some users and/or videos. In this paper, we propose a Internet video forms a major fraction of Internet traffic to-
techniquecalledOboetoauto-tunetheseparameterstodif- day[13],anddeliveringhighqualityofexperience(QoE)is
ferentnetworkconditions.Oboepre-computes,foragiven criticalsinceitcorrelateswithuserengagementandrevenue
ABRalgorithm,thebestpossibleparametersfordifferentnet- [6,23,31].Todeliverhighqualityvideoacrossdiversenet-
workconditions,thendynamicallyadaptstheparametersat workconditions,mostInternetvideodeliveryusesadaptive
run-timeforthecurrentnetworkconditions.Usingtestbedex- bitrate(ABR)algorithms[32,48,59],combinedwithHTTP
periments,weshowthatOboesignificantlyimprovesBOLA,
chunk-basedstreamingprotocols(e.g.,Apple’sHTTPLive
MPC,andacommerciallydeployedABR.Oboealsobetters Streaming,Adobe’sHTTPDynamicStreaming).ABRalgo-
arecentlyproposedreinforcementlearningbasedABR,Pen-
rithms(a)chopavideointochunks,eachofwhichisencoded
sieve,by24%onaverageonacompositeQoEmetric,inpart at a range of bitrates (or qualities); and (b) choose which
becauseitisabletobetterspecializeABRbehavioracross bitrateleveltofetchachunkatbasedonconditionssuchas
differentnetworkstates. the amount of video the client has buffered and the recent
throughputachievedbytheclient.Withinthisgeneralframe-
CCSCONCEPTS work,ABR algorithmsdifferinhowbitratelevelselection
• Information systems → Information systems applica- decisionsaremade,andthesedecisionsimpactmetricssuch
tions;Multimediastreaming; astheaveragebitrateortherebufferingratio.Wecallthese
QoEmetrics,becausetheyhavebeenshowntocorrelatewell
KEYWORDS withQoE[23],butotherperceptualvideoqualitymetrics[2]
Videodelivery,Adaptivebitratealgorithms mayalsoinfluenceQoE.
ABRalgorithmdesignremainsanactiveresearchareabe-
ACMReferenceFormat:
causecontentproviderscontinuetobeinterestedinimproving
Zahaib Akhtar*, Yun Seong Nam*, Ramesh Govindan, Sanjay
Rao,JessicaChen,EthanKatz-Bassett,BrunoRibeiro,JibinZhan, theperformanceofvideodelivery.CurrentABRalgorithms
andHuiZhang.2018.Oboe:Auto-tuningVideoABRAlgorithmsto performwellonaverage,butsomeuserscanexperiencepoor
deliveryperformanceasmeasuredbytheQoEmetrics.These
*Bothauthorscontributedequallytothispaperandcanbecontactedatfollowing: userssufferbecauseABRalgorithmshavelimiteddynamic
zakhtar@usc.edu,nam21@purdue.edu
range:theydonotperformuniformlywellacrosstherangeof
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor networkconditionsseeninpracticebecausetheirparameters
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
aresensitivetothroughputvariability(§2).
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation
onthefirstpage.CopyrightsforcomponentsofthisworkownedbyothersthanACM Contributions. In this paper, we present the design of
mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish, Oboe1 (§3), a system that takes the first step towards
topostonserversortoredistributetolists,requirespriorspecificpermissionand/ora
fee.Requestpermissionsfrompermissions@acm.org. overcomingthesehurdles.Oboeimprovesthedynamicrange
SIGCOMM’18,August20–25,2018,Budapest,Hungary ofABRalgorithmsbyautomaticallytuningABRbehaviorto
©2018AssociationforComputingMachinery.
ACMISBN978-1-4503-5567-4/18/08...$15.00
https://doi.org/10.1145/3230543.3230558 1InorchestrasallinstrumentstunetotheOboe.
44

SIGCOMM’18,August20–25,2018,Budapest,Hungary Z.Akhtaretal.
thecurrentnetworkstateofaclientconnection,specifically 2 BACKGROUNDANDMOTIVATION
tothroughputandthroughputvariability. TheInternetvideodeliveryecosystemconsistsofhundreds
Oboe’sdesignisbasedontheobservationmadebyprior ofcontentpublishersandhundredsofclientsideapplications
work [17, 35, 38, 52, 60] that TCP connections are well- thatstreamvideocontenttodiverseuserdevices.Publishers,
modeled as traversing a piecewise-stationary sequence of contentdeliverynetworks,andusersallseektoimproveuser
network states (§3.1): the connection consists of multiple quality of experience (QoE). There are many factors that
non-overlappingsegmentswhereeachsegmentisinadistinct affectQoEincludingstartuplatency,theaveragebitratefora
stationary network state. For each possible network state, videosession,aswellastherebufferingratio(thepercentage
Oboepre-computes,offline,thebestparameterconfiguration of time playback is stalled because of drained buffer) [23].
foragivenABRalgorithm(§3.2).Itdoesthisbysubjecting Video players improve QoE using adaptive bitrate (ABR)
thealgorithm,foreachstate,todifferentparametervalues, algorithms which select bitrates for each chunk while (1)
andpickingtheonethatresultsinthebestperformance.Then, ensuring the bitrate seen by the user is as high as possible
during video playback, Oboe continuously uses a change- and(2)avoidingrebufferingeventsattheclient.SomeABR
pointdetectionalgorithmtodetectchangesinnetworkstate algorithms may also try to minimize the number of bitrate
andselectstheparameteridentifiedbytheofflineanalysisas switchestomaketheplaybacksmooth.
bestforthecurrentstate.Thus,ifavideosessionencounters Contentpublishersservedifferenttypesofcontentinclud-
varyingnetworkstateduringitslifetime,Oboeautomatically ingVoD(VideoonDemand)orLivebroadcasts.Theymay
specializestheABRparametertoeachstate(§3.3). also serve streams of different qualities ranging from HD
WehaveimplementedOboeanddemonstratedseveralas- (high definition) to SD (standard definition). These differ-
pects of its performance through testbed experiments and encesimpacthowtheyservevideos.Forexample,publishers
tracedrivensimulations.First,Oboesignificantlyimproves whoserveVoDcontentcanuseplayerbuffersaslargeas4
performanceofQoEmetricsforthreequalitativelydifferent minutes [32], whereas publishers serving live content may
ABRalgorithms,onethatmakesbitrateswitchingdecisions haveatime-to-live2requirementbetween15-45seconds.Sim-
onbufferoccupancyalone(BOLA)[48],anotherthatuses ilarly,basedonthequalityofstreamstheyserve,publishers
both throughput and buffer occupancy (HYB, a widely de- mayusedifferentbitratelevelsorchunksizes.Further,pub-
ployedalgorithm),andathirdthatalsooptimizesdecisions lishersmayhavedifferentQoEobjectives.Forexample,some
acrossafinitelookaheadhorizon(RobustMPC)[59].Ineach maystrictlyprefertominimizerebufferingandothersmay
ofthesecases,Oboeresultsinsignificantimprovement.For relax their tolerance for rebuffering to prioritize higher bi-
instance,Oboereducessessionswithrebufferingfrom33.3% trates. We use the term publisher specifications to denote
to5.3%relativetoRobustMPCwhilealsosignificantlyim- theirchoiceofbitratelevels,chunksizes,contenttype,and
provingacompositeQoEmetric. rebufferingtolerance.
Oboe,whenappliedtoRobustMPC,alsoperformssignifi-
2.1 BackgroundonABRAlgorithms
cantlybetterthananewlyproposedapproachcalledPensieve
thatlearns,fromrealtraces(usingreinforcementlearning), ABRalgorithmsfallintwobroadcategories:(i)thosethat
howtoadapttoavarietyofnetworkconditions.Fornearly usebothpredictionofnetworkthroughputandbufferoccu-
80%ofthesessionsinourdataset,Oboeimprovesthesame pancy[34,51,59];and(ii)thosethatareprimarilybasedon
compositemetric,withbenefitsexceeding20%for25%ofthe bufferoccupancy[32,48].Withintheabovetwocategories,
traces.ComparedtoOboe,whichcanspecializeparameters ABRalgorithmscanbedesignedusingapproachesranging
to individual network states, Pensieve is unable to special- fromheuristicstostochasticoptimization.In§4,wediscuss
izeacrosstheentirerangeofnetworkthroughputs.Wehave arecentlyproposedABRalgorithmbasedonaqualitatively
triedtrainingspecializedPensievemodelsfordifferentranges differentapproach,reinforcementlearning[39].
ofnetworkthroughputsanddynamicallyswitchingmodels MPC:Throughputpredictionandbufferoccupancywith
basedonestimatedsessionthroughput.Thishelps,butasig- look-ahead.Selectsbitratebysolvinganoptimizationprob-
nificantgapbetweenthetwoapproachesstillremains(§4.4). lem. MPC [59] predicts throughput of future chunk down-
WhileavarietyofviablepathwaysexisttodeployingOboe, loadsbasedonthroughputsamplesofrecentlydownloaded
wefocusonanarchitecturewhereOboeandtheentireABR chunks,thenusesthispredictedthroughputtoselectbitrates
logicaredeployedonthecloudwhichenablesrapidevolution to optimize a given QoE function (§4) over a look-ahead
andfine-graincustomizability.Weshowtheviabilityofthis window of 5 future chunks. The aggressive version of the
architecturewithresultsfromapilotdeployment. algorithm(FastMPC)directlyusesathroughputestimateob-
tainedusingaharmonicmeanpredictor.Tocompensatefor
2Forlivecontent,thetimebetweentheeventanditsbroadcasttousers.Thisbounds
themaximumbufferthataplayerstreamingaliveeventcanbuild.
45

Oboe SIGCOMM’18,August20–25,2018,Budapest,Hungary
Figure1—PerformanceofABRalgorithmsusingdifferentconfigurationsfortwosessionswithdifferentthroughputbehaviors
Figure2—IllustratinghowpolicyforsettingdiscountfactorsinMPCimpactsperformancefordifferenttraces
throughputpredictionerrors,amoreconservativeversion,Ro- is because, while deployed ABR algorithms work well on
bustMPC,reducespredictedthroughputbyadiscountfactor average,theydonotworkuniformlywellacrossallnetwork
1+𝑑,where𝑑isthemaximumerrorinthroughputpredictions conditions.AkeyreasonforthisisthatABRalgorithmshave
experiencedinthelastfivechunkdownloads. parameters(whichwehenceforthrefertoasconfigurations)
BOLA: Buffer occupancy, selects bitrate by solving an thatmustbesetinamannersensitivetonetworkconditions.
optimization problem. BOLA is a buffer-based algorithm ABRalgorithmsneedtorunonmanydifferentnetworks,rang-
used in Dash.js [7], so it does not employ throughput pre- ingfromcellularandWiFinetworksatoneend,tohigh-speed
dictioninmakingbitratedecisions[48].Italsomodelsbitrate broadbandconnectionsattheother.Giventhisdiversity,net-
selection as an optimization problem which it solves for a workconditionscanvarysignificantly.Packetlossconditions
givenvalueofthebuffer.Itusesaparameter𝛾whichisaratio canvarybyanorderofmagnitudeormoreacrosstheglobe
of(i)aminimumbufferthreshold,belowwhichitdownloads [25].Networkthroughputscanalsovarywidely:for90%of
thelowestbitrateand(ii)atargetbufferthresholdwhichit tracesinalargedataset,thetrace’smaximumthroughputis
triestomaintain.Conceptually𝛾 controlshowstronglythe morethantwiceitsaveragethroughput.Yet,unfortunately,
ABRshouldavoidrebuffering[48].Highervaluesof𝛾 make mostABRalgorithmstodayeitheremployfixedconfigura-
thealgorithmconservative. tionsorsimpleheuristicstoadapttheseconfigurations(§2.1).
HYB:Throughputpredictionwithoutlookahead.Selects Figures1(a)and1(b)showhowthechoiceofABRconfig-
bitrateusingasimpleheuristic. Analgorithmwidelyusedin urationdependsonnetworkconditions.Figure1(a)showsthe
production(§5),HYBconsidersboththepredictedthroughput bitrateandrebufferingratiofortwoclientsessionswiththe
andcurrentbufferoccupancy(HYBisshortforhybrid).For HYBalgorithmforthreedifferentvaluesofits𝛽 parameter,
each chunk, HYB picks the highest bitrate that can avoid Cons (Conservative), Mod (Moderate), and Aggr (Aggres-
rebuffering.Specifically,if𝑆 (𝑖)denotesthesizeofchunk𝑗 sive).Thethroughputbehaviorofthetwosessionsisshown
𝑗
encodedatbitrate𝑖,𝐵isthepredictedthroughputbasedon inFigure1(c).Ifapublisherpreferstoeliminaterebuffering,
pastsamples,and𝐿thelengthofthebuffer.HYBpicksthe ModissuitableforsessionA,butConsisbetterforsessionB.
largestbitrate𝑖suchthat
𝑆𝑗(𝑖)
< 𝐿×𝛽.Here,𝛽 canhave
Figure1(b)showsthatBOLAbehavessimilarly,withMod
𝐵 beingthepreferredsettingforsessionAandConsforsession
valuesbetween0and1(highervaluesrepresentaggressive
B,toavoidrebuffering.
ABRbehavior).𝛽 canbetunedtooffsetpredictionerrorsin
Figures 2(a) and 2(b) show the difficulty in setting the
throughputandtocompensateforthegreedynatureofthe
discount factor with MPC, by comparing the performance
approachwhichmaymakeitsusceptibletofuturebuffering
ofFastMPC(nodiscountfactor),andRobustMPC(discount
eventsowingtounexpectedthroughputdips.
factorsetbylocalheuristic)fortwothroughputtraceswith
2.2 EnsuringHighQoEforAllUsers different characteristics. In each figure, the top subgraphs
showtheavailablethroughput(greencurve)andthethrough-
Despitewidespreaddeployment,ABRalgorithmscontinue
putestimateofFastMPC(red)andRobustMPC(blue).For
tobeanactiveareaofresearch[32,34,39,48,51,59].This
46

SIGCOMM’18,August20–25,2018,Budapest,Hungary Z.Akhtaretal.
theleftgraph,althoughthethroughputisgenerallygood,the
suddenvariationsforceRobustMPCtomakeoverlyconserva-
tivebitratedecisions,aswellasincurmorebitrateswitches.
(bottomsubgraph).Incontrast,inFigure2(b),thequickerand
morefrequentthroughputchanges(topsubgraph)resultin
FastMPCexperiencingrebuffering(middlesubgraph),while
RobustMPCdoesnot.Thisisjustoneexampleillustrating
thedifficultyinpickingparameters–inourevaluations(§4), Figure3—ThelogicaldiagramoftheofflinepipelineusedbyOboe
we found that RobustMPC was itself too aggressive when
selectingdiscountfactorsforsometraces. downloadedchunks.Thisperceivedthroughputalreadyac-
Whilethissectionusessynthetictracesforillustrativepur- countsfornetworkdelaysandloss-rates,aswellasthedy-
poses,ourevaluationswithrealtraces(§4)moreextensively namicsoftheunderlyingtransportprotocol.
demonstrate the limitations of current approaches with re- Thenetworkthroughputalongapathisnotnecessarilya
specttoselectingparametersandthebenefitsofautomatically stationaryprocess[17,35,38,52,60]:flowsatthebottleneck
tuningABRparameterstonetworkconditions. alongapathmaychangeovertimeresultinginchangesto
availablethroughput,orthebottleneckitselfmayshift[35].
Ananalysisofthethroughputtracesusedinourevaluations
3 OBOEDESIGN
(§4)confirmsthelackofstationaritywhenappliedtotheen-
OboeaimstoensuregoodQoEforallusersbyenablingABR
tiretrace.WeanalyzethroughputtracesusingtheAugmented
algorithmstoperformbetteracrossawiderangeofnetwork
Dickey-Fuller(ADF[26])test,ahypothesistesttocheckfor
conditions.TheconfigurationsofmanyABRalgorithmsare
stationarityinatimeseries.Ourevaluationsonadatasetof
sensitivetonetworkstate,specificallytothevalueandvari-
15,000videostreamingthroughputtracesshowthat59.5%
abilityoftheavailablethroughputbetweentheclientandthe
werenon-stationary(see§4.2fordetailsofthedataset),imply-
videoserver.Forexample,𝛽 inHYBshouldbesmallerwhen
ingthepresenceofdistinctmeanand/orvarianceindifferent
available throughput is highly variable, while 𝛾 in BOLA
segmentsofthetraces.
shouldbehigher.Thisexplainswhythealgorithmsperform
However,priorwork[17,35,38,52,60]showsthatTCP
differentlyfordifferentvaluesofparametersonagivenclient
connection throughput can be modeled as a piecewise sta-
trace(§2.2).However,alineofpriorwork[17,35,38,52,60]
tionary process; the connection consists of multiple non-
hasobservedthatnetworkconnectionsarepiecewisestation-
overlappingsegmentswhereeachsegmentisstationaryand
ary:thatis,connectionscanbeinoneofseveraldistinctstates
often lasts for tens of seconds or minutes (e.g., Figure 8).
(§3.1),whereeachstateisdistinguishedbystationarityinthe
Moreover,Zhangetal.[60]showthatthethroughputineach
statisticalsense(informally,aprocessisstationaryifitssta-
segmentmaybemodeledasani.i.d.process.
tisticalpropertiesincludingmeanandvariancedonotchange
Motivated by these observations, Oboe defines network
overtime-see[43]foramoreformaldefinition).
state𝑠byatuple< 𝜇 ,𝜎 >,where𝜇 isthemeanand𝜎
𝑠 𝑠 𝑠 𝑠
Oboeleveragesthepiecewisestationarityofnetworkcon-
thestandarddeviationoftheclient-perceivedthroughputina
nectionstoaddressthekeychallengeofsensitivityofconfig-
(stationary)segmentoftheunderlyingTCPconnection.
urationstonetworkconditions.Itdoessousingatwostage
design:(a)anofflinestagewhereitpre-computesthebestcon-
3.2 OfflineMappingofNetworkStates
figurationchoiceforeach(stationary)networkstate(§3.2),
and (b) and an online stage, where during a session, it de- TomapnetworkstatestotheiroptimalABRconfigurations,
tectschangesinnetworkstateandappliesthepre-computed Oboeusesapipeline(Figure3)consistingofthreecompo-
best configuration for the current (stationary) state (§3.3).
nents–theConfigEvaluator,theVirtualPlayerandtheCon-
Oboe can also accommodate publisher specifications such
figSelector.TheConfigEvaluatortakesastationarythrough-
as session type (live vs. video-on-demand, time-to-live re- puttraceasinput,whichrepresentsaparticularnetworkstate,
quirements),bitratelevelsoranyexplicitQoEtradeoffs(e.g., anddrivestheexplorationofdifferentABRconfigurations
preferencebetweenrebufferingandaveragebitrate)(§3.2),by overthistrace.ItdoessobyusingtheVirtualPlayerwhich
usingthesetoinfluencetheselectionofthebestconfiguration models the dynamics of an actual video player. The Virtu-
foreach(stationary)networkstateintheofflinestage. alPlayerinterfaceswiththeABRalgorithmimplementation
andoutputstheperformanceofdifferentconfigurationsofthe
ABR.Finally,theConfigSelectorcomparestheperformance
3.1 RepresentingNetworkState
of different configurations and builds a ConfigMap, which
Most ABR algorithms today adapt bitrates based on the
mapsagivennetworkstatetothebestconfiguration.
throughput(moreprecisely,goodput)achievedbyrecently
47

| Oboe |     |     |     |     |     |     |     | SIGCOMM’18,August20–25,2018,Budapest,Hungary |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
Generating throughput traces for ConfigEvaluator. To BuildingtheConfigMapusingConfigSelector. Tobuild
exploreconfigurationspaceofanABRalgorithmoneachnet- theConfigMap,theConfigEvaluatordrivestheexplorationof
workstate𝑠,ConfigEvaluatorneedsastationarythroughput differentconfigurationsforanABRalgorithm.Foragiven
tracetorepresent𝑠.Togeneratesuchatrace,weexploredtwo network state 𝑠, ConfigEvaluator sweeps through possible
differentapproaches.Inoneapproach,weextractedstationary configurationsoftheABRalgorithmusingtheVirtualPlayer.
segmentsfromrealtracesusingofflinechangepointdetec- Forexample,the𝛽 parameterinHYBcantakevaluesfrom0
to1,soConfigEvaluatorplaysthetraceforstate𝑠formultiple
tion([10],describedin§3.3).Changepointscapturepoints
wherethedistributionchanges.However,becausewearenot valuesof𝛽 (quantizedforefficiency,seebelow)inthisrange.
guaranteedcoverage(i.e.,notallstatesmightbeobservable Foreachparametervalue𝑐 ,VirtualPlayeroutputsaper-
𝑖
=<𝑣
in real traces), we also explored a second approach which formancevector𝑉 𝑖 1 ,𝑣 2 ,...𝑣 𝑚 >whereeach𝑣 𝑘 cor-
involvedgeneratingasynthetictraceforeach𝑠with𝑠’smean respondstothevaluesachievedby𝑐 foraQoEmetric(e.g.,
𝑖
andstandarddeviation,assumingaGaussiandistributionfor bitrate,rebufferingratio,andmoregenerallyjointimeand
thethroughputsamples.ThiswasmotivatedbyDindaetal. frequencyofswitchingbitrates[23]).Thissetofperformance
[38] who showed that the throughput of TCP flows of the vectorswiththecorrespondingparametervaluesarethensent
samesizeinagivenstationarysegmentmaybemodeledas toConfigSelectorforpickingthebestconfiguration.
a Gaussian distribution (also see §3.1). More recent work ConfigSelector takes the set of performance vectors and
alsoshowsthatTCPthroughputiswellmodeledasaMarkov determines the best configuration from them using vector
process,eachofwhosestatesmaybemodeledasaGaussian dominance. A configuration 𝑐 is said to dominate 𝑐 if 𝑉
|     |     |     |     |     |     |     |     |     |     |     | 𝑖   |     | 𝑗 𝑖 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
distribution[49].WefoundthatOboewithsynthetictraces element-wisedominates𝑉 (i.e.,eachelementof𝑉 isbet-
|     |     |     |     |     |     |     |     |     |     | 𝑗   |     |     | 𝑖   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
performedcomparablytostationarysegmentsfromrealtraces. terthanorequaltothecorrespondingelementof𝑉 𝑗 ).This
So,ConfigEvaluatorusessynthetictraces. step also takes into account any rebuffering tolerance, and
Specifically, ConfigEvaluator quantizes both mean and ConfigSelectorappliesthistolerancetoselectthemaximal
standard deviation of throughput using a quantum (in our performancevector.Deferringtheselectionofthemaximal
experiments,of50Kbps),resultinginstates(inourexperi- vectorforagivenrebufferingtolerancetothisstage(instead
ments,10,000),spreadoveratwodimensionalspace(inour offilteringvectorsinthepreviousstep)isbeneficial:itmini-
experiments,0.05-10Mbps)ofthroughputandstandarddevi- mizesrecomputationbyallowingOboetoquicklycomputea
ation.Foreachstate,wegenerateasyntheticstationarytrace. newmaximalvectorifthepublisherchangestherebuffering
Wefoundthatthebenefitsoffinerquantizationaremarginal. tolerance. At the end of this stage, Oboe obtains the Con-
|            |     |             |     |      |               |     |     | figMap, a | complete | mapping | of each network | state | to its |
| ---------- | --- | ----------- | --- | ---- | ------------- | --- | --- | --------- | -------- | ------- | --------------- | ----- | ------ |
| Estimating | ABR | performance |     | with | VirtualPlayer |     | and |           |          |         |                 |       |        |
publisher specifications. Oboe uses VirtualPlayer, a trace- correspondingoptimalABRconfiguration.
basedsimulatorthatmimicsthebehaviorofanactualvideo Twooptimizationscanbeusedtoquickentherateofex-
plorationoftheConfigEvaluator.Thefirstistoquantizethe
| player without |     | downloading |     | or rendering |     | actual | videos. |     |     |     |     |     |     |
| -------------- | --- | ----------- | --- | ------------ | --- | ------ | ------- | --- | --- | --- | --- | --- | --- |
It takes as input a throughput trace and outputs the QoE parameter sweep, so that configurations are evaluated at a
|             |         |     |         |         |     |       |           | coarser granularity. |     | This trades | off some performance |     | for |
| ----------- | ------- | --- | ------- | ------- | --- | ----- | --------- | -------------------- | --- | ----------- | -------------------- | --- | --- |
| performance | metrics | of  | a video | session |     | for a | specified |                      |     |             |                      |     |     |
lowercomputationalcomplexity.Thesecondoptimizationis
| ABR algorithm. |     | We have | validated |     | VirtualPlayer |     | in §4.7. |     |     |     |     |     |     |
| -------------- | --- | ------- | --------- | --- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- |
In designing VirtualPlayer, we have decoupled ABR logic basedontheobservationthatthereisgenerallyamonotonic
relationshipbetweenparametervaluesandtheperformance.
| (Figure 3), | so the | same | implementation |     | of  | the ABR | logic |     |     |     |     |     |     |
| ----------- | ------ | ---- | -------------- | --- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- |
canbeusedinOboe’sofflineandonlinestage.Further,this For instance, for HYB (§2.1), the rebuffering ratio and av-
eragebitratearemonotonicallynon-decreasingwiththepa-
| design provides |     | an interface | to  | the ABR | designer |     | through |     |     |     |     |     |     |
| --------------- | --- | ------------ | --- | ------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- |
rameter𝛽.Basedonthisobservation,wecaninsteadusean
| which they | can | easily integrate |     | their | ABR | algorithm | with |     |     |     |     |     |     |
| ---------- | --- | ---------------- | --- | ----- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- |
OboewithouthavingtoknowaboutOboe’sinternals. 𝑂(log𝑛)binarysearchoftheconfigurationspaceinsteadof
doingafull𝑂(𝑛)sweepofallconfigurations.
TheVirtualPlayeralsotakesintoaccountpublisherspec-
ificationsforbitratelevels,playerbuffersizes(determined
3.3 OnlineABRTuning
| by time-to-live |     | requirements) |     | and chunk | size. | These | spec- |     |     |     |     |     |     |
| --------------- | --- | ------------- | --- | --------- | ----- | ----- | ----- | --- | --- | --- | --- | --- | --- |
OboeusestheConfigMapgeneratedoffline,andlivethrough-
| ifications | are used | by VirtualPlayer |     |     | when | it executes | ABR |     |     |     |     |     |     |
| ---------- | -------- | ---------------- | --- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
algorithmsontheinputtraces,ensuringthattheresultingCon- put measurements from the video player to dynamically
changeABRconfigurationsduringavideoplayback.Itdoes
figMapmeetsthepublisherspecifications.Finally,Oboealso
|            |           |     |            |         |     |             |     | this by using | an  | online change | point detection | algorithm |     |
| ---------- | --------- | --- | ---------- | ------- | --- | ----------- | --- | ------------- | --- | ------------- | --------------- | --------- | --- |
| allows the | publisher | to  | optionally | express |     | an explicit | QoE |               |     |               |                 |           |     |
tradeoffsuchasmaintainingtherebufferingunderadesired [14]. This algorithm identifies, in an online fashion, if
|     |     |     |     |     |     |     |     | the distribution |     | of the throughput | samples | has changed |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------------- | ------- | ----------- | --- |
threshold𝑥%.OboederivesaConfigMapthatmeetsthere-
bufferingthresholdinabesteffortmanner.Weevaluatethe significantly, signaling a state transition. When a change
pointisdetected,thealgorithmalsoprovidesthenewstate
efficacyofthisflexibilityin§4.7.
48

SIGCOMM’18,August20–25,2018,Budapest,Hungary Z.Akhtaretal.
ofthechunkdownload.Thisisacceptablesinceanyaction
thatcanbetakenbytheABRalgorithm(suchasabitrate
switch)onlyimpactssubsequentchunks.Intherarercasethat
anABRalgorithmabandonsthedownloadofachunkthat
takestoolong,thereportissentwhenthechunkdownloadis
abandoned.§4.8evaluatestheoverheadsofChangeDetector.
Analternativeapproachtochangingconfigurationsisto
Figure4—LogicaldiagramofOboe’sonlinepipeline
useanexponentiallyweightedmovingaverage(EWMA)of
𝑠’s mean and standard deviation. Oboe’s ChangeDetector themeanandstandarddeviationofthroughputsamplesand
(Figure4)implementsthechangepointdetectionalgorithm, tolookupthecorrespondingconfiguration.Weexperimented
and the ReconfEngine is responsible for updating the withsuchanapproachandfounditsperformanceunsatisfac-
ABR configuration based on a new network state and the tory.Theapproachcanresultincontinualandunnecessary
ConfigMap. reconfigurations,sincethroughputmayvaryacrosssamples
evenwhenthenetworkis(statistically)stationary.Damping
Changepointdetectionalgorithms. Suchalgorithmsana-
thesechangescanresultinslowreactiontimeswhenarecon-
lyzeatimeseriesandcheckifthereareregionsinthetime
figurationisactuallybeneficial.Incontrast,Oboe(i)models
serieswheretheunderlyingdistributionofthedatachanges
theunderlyingTCPconnectionasasequenceofstates;(ii)
toadifferentsetofparameters.Offlinechange-pointmethods
doesnotmakechangestotheconfigurationwithinagiven
require the full time series to be available, whereas online
networkstate;and(iii)onlyreconfigureswhenastatechange
methodsworkwithacontinuousstreamofsamplesasthey
isobserved.
becomeavailable.Wefocusononlinemethods,sinceOboe
ReconfiguringABRAlgorithm. Whenachangeinthenet-
identifieschangepointsforanin-progresssessionanddynam-
workstateisdetected,theChangeDetectorsignalsthechange
icallychangesconfigurations.
andthenewnetworkstate𝑠totheReconfEngine.TheRecon-
Whileseveraltechniquesexistforchangepointdetection
fEnginethensearchesaneighborhoodofradius𝑟intheCon-
[22,33,36,44,54,58],wefocusonprobabilisticmethods
figMaptoselecttheconfigurationtouseforstate𝑠.Specifi-
[14, 18, 24, 57]. Further, we use a Bayesian online proba-
cally,ifstate𝑠isapointina2-dimensionalspaceofaverage
bilisticchange-pointdetector[14]fortworeasons.First,in
throughputandstandarddeviationofthroughput,thenitpicks
[14],asequenceofobservationscanbepartitionedintonon-
themostconservativeABRconfigurationwithinasearchra-
overlappingstatessuchthattheobservationsarei.i.d.condi-
dius𝑟 around𝑠.Itdoesthisfortworeasons.First,because
tionedonagivennetworkstate𝑠.Thisviewalignswellwith
Oboequantizesthenetworkstates,itmightnothaveprecom-
thewaywehavedefinedanetworkstate(§3.1).Further,theal-
putedthebestconfigurationfor𝑠.Second,theestimatednew
gorithmisfastandrequiresnopriorknowledgeaboutthedata
network state 𝑠 may have some error, for example, due to
stream,matchingourscenario.Weusetheimplementation
inefficienciesintheclientdownloadstack[27].Giventhese
providedin[10]andintegrateitwiththeChangeDetector.
sourcesofuncertainty,Oboechoosestobesafeinitsselec-
Detecting changes in network state. During a video ses- tion of the best configuration for 𝑠. Finally, ReconfEngine
sion,ChangeDetectoriscontinuallyfedwithaseriesofobser- configures the ABR algorithm, and the reconfigured ABR
vationsofthenetworkthroughput,whichitusestodetectstate algorithmisreadytocomputethebitratedecisiontobeused
changes.ChangeDetectorcalculatesthroughputandstandard forthenextchunkatthispoint.
deviationbyonlyconsideringthosesampleswhichbelong
to the current state. To generate inputs to ChangeDetector, 4 EVALUATION
oneapproachistouseeachdownloadedchunktoobtaina Inthissection,wedemonstrateOboe’sabilitytoauto-tune
singlethroughputsample.However,thismaybetoocoarse- threeexistingalgorithms:RobustMPC,BOLAandHYB.We
grained, and prevent detection of changes in network state alsocompareanOboe-tunedRobustMPCtoPensieve[39].
thatoccurduringthechunkdownload.Instead,weusefine
grainedsamplesrecordedatperiodicintervals(tensofmil- 4.1 Metrics
liseconds)duringthedownloadofeachchunk.Playerssuch Theperformanceofavideosessiondependsonmultiplefac-
asDash.jsalreadyperiodicallylogintermediatethroughput tors.Averagebitrateandrebufferingratiowerefoundtohave
samplesduringachunkdownload,soobtainingthesesam- themostimpactonuserqualityofexperience[23],though
plesdoesnotincuranyadditionaloverhead.Weonlyneed otherfactorssuchaschangesinbitratesduringasessioncan
tomodifyplayerstoreportthesesamplestoOboe.Theset playarole[23].Thereisnoconsensusonhowtobestcap-
ofsamplesareprovidedtoChangeDetectorafterthechunk tureauser’sQoE.Consequently,ABRalgorithmstodayare
download,andanychangeinstateisonlydetectedattheend designed to optimize different metrics. For instance, HYB
49

Oboe SIGCOMM’18,August20–25,2018,Budapest,Hungary
Dash.js to send client player state information (e.g. buffer
length, video play state and throughput measurements) to
Oboe(§5).ThisplayerrunsontheGoogleChromebrowser
(version61)inourexperiments.In§5,weshowthatOboe
canalsoberunasacloudservice.
Testbedsetup. OurevaluationsmeasureABRperformance
bydeliveringavideostream(the“EnvivioDash3”videofrom
theMPEG-DASHreferencevideos[12])fromavideohost-
Figure5—AscatterplotofaveragebitrateandrebufferingratiobetweentheVirtu-
ingservertoaclient,whilevaryingnetworkconditionsus-
alPlayerandrealDash.jsplayer
ing throughput traces from real user sessions. We use bi-
andBOLAprimarilymaximizeaveragebitratesubjecttolow trates{300,750,1200,1850,2850,4300}𝑘𝑏𝑝𝑠witha4sec-
rebuffering.Incontrast,otheralgorithms[39,59]havebeen ondchunkdurationandtotallengthof192seconds.Wefocus
designedtooptimizeaQoEmetricwhichisalinearcombina- onthisvideoasithasbeenusedinpriorwork[39],andwe
tionofbitrate,rebufferingandbitratechanges(smoothness). donotconsidervideosoflongerdurationbecauseweonly
WithOboe,ourprimaryevaluationgoalistodemonstrate have throughput traces available for a video publisher that
theextenttowhichitcanimprovetheunderlyingmetricsthat servesshortmusicvideos(aswediscussbelow).Thevideo
anABRalgorithmisdesignedfor.Thus,ourevaluationswith is hosted on an Apache server. Both the server and client
BOLA and HYB focus on average bitrate and rebuffering, softwarerunonthesame8-core,4Ghz,Inteli7commodity
whilethosewithMPC+Oboefocusonthelinearcombination desktopwith12GBRAMrunningUbuntu16.04.Between
of QoE (which we refer to as QoE-lin, [59]), defined as server and client, we emulate different network conditions
follows. For a video with 𝑁 chunks, let 𝑅 be the bitrate usingtheChromeDevToolsAPI[9].Thisallowsustocontrol
𝑖
chosenforchunk𝑖.Then,themagnitudeofbitratechanges theupload/downloadthroughputaswellaslatencyusingthe
𝑀 maybedefinedas𝑀 = ∑︀𝑁 𝑖 −1|𝑅 𝑖+1 −𝑅 𝑖 |.Iftheses- Chrome-Remote-Interfacebasedonthroughputtraces[5].We
sion experiences a total of 𝑇 seconds of rebuffering, then,
use571throughputtraces3fromourdataset(discussedbelow)
QoE-lin(𝑝,𝑐) = 1 * ∑︀ (𝑅 −𝑝𝑇−𝑐*𝑀),where𝑝and𝑐 forthisemulation.Allourtestbedexperimentsuseaclient
𝑁 𝑖 𝑖
representscalingpenaltiesappliedtorebufferingandchanges bufferof2minutes.
inthesession.Thisfunctionmaybeviewedasthesession Datasets. Weusethroughputtracesfromrealusersessions
QoE averaged over the number of chunks. For our videos collectedoverathreemonthperiod.Eachtracecontainsthein-
thathadamaximumbitrateof4.3Mbps,weuse𝑝=4.3and dividualchunksizesandtheirdownloadtimesforon-demand
𝑐=1asourdefaultparameters(followingpreviousworkthat videosessionsfromapublisherthatservesshort(4-6minute)
setdefaultrebufferingpenaltyequaltothemaximumbitrate musicvideos.Wederivethroughputbydividingthechunk
value[39,59]). sizesbytheirdownloaddurations.Thetracescontainsessions
Even when an algorithm optimizes a metric such as thatuseddesktopswithwiredconnectionsandalsosessions
QoE-lin,itisimportanttounderstandthedistributionsof onmobiledevicesusingWiFiorcellularconnections.Like
underlyingfactors.Theunderlyingfactorsrepresentconcrete previous work [39, 59], we primarily focus on traces that
applicationperformancethatpublishersunderstandhowto havelessthan6Mbpsaveragethroughput,sincethisisthe
reasonabout.Moreover,aunifiedmetriclikeQoE-lincan regimewherebitrateswitchingdecisionsarelikelytohave
obscure important differences. For example, two sessions QoEimpact.Wefilteredouttraceswhichweretooshortfor
mayhavethesameQoE-linbutdifferentperformancein playingourentire192secondvideo,afterwhichweobtained
underlyingmetrics,leadingtovarieduserexperience.So,we 5Ktracesfromwireddesktopsand4KsessionsfromWiFior
alsopresentgraphsofthesemetrics. 3G/4Gmobiledevices.Ourtestbedexperimentsuseasubset
of571traceswithroughlythesamenumberoftracessampled
4.2 Methodology fromeachofdesktopandmobileclients.
Implementation. For RobustMPC, we used the imple- VirtualPlayer setup. Recall that Oboe uses the Virtu-
mentation available at [11]. Our implementation of BOLA alPlayer to obtain a ConfigMap for any ABR algorithm.
[@bola] is from the Dash.js player. The implementation Sincethemajorityofourresultsuseanactualtestbedwith
of HYB is a variant of the algorithm used in a large-scale the Dash.js player, the benefits of Oboe in our evaluation
deployment.TheseABRalgorithmsandOboe’sonlinestage resultsalreadyarisedespiteanyinaccuraciesinbuildingthe
(change point detection and ABR reconfiguration) run on ConfigMaponaccountofusingtheVirtualPlayer.Thatsaid,
the server in our experiments. Our client runs the Dash.js wehavealsoverifiedthattheVirtualPlayerdoesagoodjob
videoplayer(version1.2),areferenceplayerimplemented
inJavaScriptbytheMPEG-DASHforum[7].Wemodified 3Availableathttps://github.com/USC-NSL/Oboe
50

| SIGCOMM’18,August20–25,2018,Budapest,Hungary |     |     |     |     |     |     |     |     |     |     | Z.Akhtaretal. |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- |
Figure6—ThepercentageimprovementinQoE-linofMPC+OboeoverRobustMPCfortheTestbedexperiment.Thedistributionofaveragebitrate,rebufferingratioandbitrate
changemagnitudefortheschemesisalsoshown.
Figure7—QoE-linofMPC+OboecomparedtoRobustMPC
| of tracking | the performance |     | of the | actual | ABR algorithms. |     |     |     |     |     |     |     |     |
| ----------- | --------------- | --- | ------ | ------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Forinstance,Figure5(a)and5(b)demonstratesthisforthe
| HYB algorithm.  | The         | figures     | shows    | the correlation |                | for the |     |     |     |     |     |     |     |
| --------------- | ----------- | ----------- | -------- | --------------- | -------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| average         | bitrate and | rebuffering | ratio    | for             | 100 throughput |         |     |     |     |     |     |     |     |
| traces randomly |             | sampled     | from our | dataset         | using          | HYB     |     |     |     |     |     |     |     |
Figure8—AnexamplesessionshowinghowMPC+OboeisabletooutperformRo-
on the VirtualPlayer compared to using an actual Dash.js bustMPCbyreconfiguringthediscountparameterwhenanetworkstatechangeisde-
tected.
| player.    | For both   | metrics, | the graph    | closely | tracks | the   |     |     |     |     |     |     |     |
| ---------- | ---------- | -------- | ------------ | ------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
| 𝑦 = 𝑥 line | indicating | close    | correlation. | Given   | these  | close |     |     |     |     |     |     |     |
medianperchunkchangemagnitudeby38%(Figure6(d)).Fi-
| correlations, | we use | the | VirtualPlayer | in  | §4.7 to | explore |     |     |     |     |     |     |     |
| ------------- | ------ | --- | ------------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
nally,Figure7showstheCDFofQoE-linforMPC+Oboe
Oboe’sperformanceoveralargerrangeofdiversesettings andRobustMPC,andindicatesMPC+Oboedistributionally
andourentiresetoftraces.
performsbetter.
Figure8illustrates,usingasinglesession,whyMPC+Oboe
4.3 OboewithRobustMPC
|     |     |     |     |     |     |     | performs | better than RobustMPC. |     |     | The top graph | shows |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------------------- | --- | --- | ------------- | ----- | --- |
WenowdemonstratethatOboecanbeusedtoauto-tuneRo-
|     |     |     |     |     |     |     | throughput | as a function | of time, | which | includes | an  | initial |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | -------- | ----- | -------- | --- | ------- |
bustMPC,thebestperformingvariantoftheMPCalgorithms. stable state followed by a drop in throughput. The middle
TheresultingMPC+Oboeusesthebestvalueofthediscount
graphshowshowthediscountfactor𝑑ofbothRobustMPC,
parameter𝑑correspondingtothecurrentnetworkstate,re-
|                                                     |     |     |     |     |     |     | and MPC+Oboe               | vary (the | predicted |     | throughput       | for | each |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------------------- | --------- | --------- | --- | ---------------- | --- | ---- |
| placingRobustMPC’sonlineadaptationbasedonthroughput |     |     |     |     |     |     |                            |           |           | 1   |                  |     |      |
|                                                     |     |     |     |     |     |     | systemisreducedbyafactorof |           |           | 1+𝑑 | ,where𝑑isshownon |     |      |
estimatesobtainedoverthepast5chunks(§2).
|     |     |     |     |     |     |     | the y-axis). | During the | initialstable |     | state, when | prediction |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | ------------- | --- | ----------- | ---------- | --- |
Figure6(a)showstheCDFofthepercentageimprovement errorsarelow,RobustMPCsteadilylowersitsdiscountfactor
inQoE-linofMPC+OboeoverRobustMPC.4MPC+Oboe
|     |     |     |     |     |     |     | leading to | more aggressive | bitrate | selections |     | (not shown). |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | ------- | ---------- | --- | ------------ | --- |
improvesQoE-linfor71%ofsessions,withanoverallav-
Thisresultsinarebufferingevent44secondsintothesession
erageQoE-linimprovementof17.62%acrossallsessions.
|                |         |     |               |         |     |          | (lowest graph | shows buffer | occupancy |     | with 0 | indicating | a   |
| -------------- | ------- | --- | ------------- | ------- | --- | -------- | ------------- | ------------ | --------- | --- | ------ | ---------- | --- |
| In particular, | for 19% | of  | the sessions, | QoE-lin |     | improves |               |              |           |     |        |            |     |
rebufferingevent).Incontrast,MPC+Oboedoesnotincura
bymorethan20%.ForthesessionsMPC+Oboeisunableto rebufferingeventandmaintainsafixed𝑑duringtheinitial
improveRobustMPC,itsperformancedegradationismostly
stablestate.At29sec,itdetectsachangeinthenetworkstate
under8%.Figures6(b),6(c)and6(d)showtheconstituent
andadaptsitsdiscountfactor,leadingtomoreconservative
| QoEmetrics.WhileMPC+Oboeachievesdistributionallysim- |     |     |     |     |     |     | bitrateselections. |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
ilarbitratesasRobustMPCasshownin6(b),itsignificantly
reducesrebufferingacrosssessions:thenumberofsessions 4.4 Oboevs.Pensieve
| with rebuffering | reduces |     | from 33.2% | to 5.3%. | Further, | it  |          |                |               |     |          |      |      |
| ---------------- | ------- | --- | ---------- | -------- | -------- | --- | -------- | -------------- | ------------- | --- | -------- | ---- | ---- |
|                  |         |     |            |          |          |     | Pensieve | [39] uses deep | reinforcement |     | learning | [41, | 42], |
alsoachievesbetterplaybacksmoothnessbyimprovingthe
|     |     |     |     |     |     |     | a combination | of deep      | learning | with | reinforcement |          | learn- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | -------- | ---- | ------------- | -------- | ------ |
|     |     |     |     |     |     |     | ing [50],     | and has been | shown    | to   | outperform    | existing |        |
4TheincreaseinQoE-linoverRobustMPCrelativetotheabsoluteQoE-linvalue
ofRobustMPCexpressedasapercentage. ABRs, including RobustMPC [39] in some settings. Since
51

| Oboe |     |     |     |     |     |     | SIGCOMM’18,August20–25,2018,Budapest,Hungary |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
Figure9—ThepercentageimprovementinQoE-linofMPC+OboeoverPensieveforthe0-6Mbpsthroughputregion.Thedistributionofaveragebitrate,rebufferingratioand
bitratechangemagnitudefortheschemesisalsoshown.
Havingvalidatedourretrainingmethodology,wetrained
|     |     |     |     |     |     |     | Pensieve | on our | dataset | with the same | complete | strategy |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------- | ------------- | -------- | -------- |
describedabove.Forthis,wepick1600tracesrandomlyfrom
ourdatasetwithaveragethroughputinthe0-6Mbpsrange.
Thenumberoftrainingtraces,thenumberofiterationsper
trace,andtherangeofthroughputaresimilarto[39].Wethen
|                      |        |          |        | 11—QoE-lin |     |          | comparePensieveandMPC+Oboeoveraseparatetestsetof |     |     |     |     |     |
| -------------------- | ------ | -------- | ------ | ---------- | --- | -------- | ------------------------------------------------ | --- | --- | --- | --- | --- |
| Figure 10—Validation | of our | training | Figure |            | of  | MPC+Oboe |                                                  |     |     |     |     |     |
methodologyforPensieve. comparedtoPensieve tracesalsointherangeof0-6Mbps(§4.2).
|     |     |     |     |     |     |     | ComparisonwithPensieve. |             |     | Figure9(a)showstheCDFof |     |          |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | ----------- | --- | ----------------------- | --- | -------- |
|     |     |     |     |     |     |     | the percentage          | improvement |     | in QoE-lin              | for | MPC+Oboe |
overPensieve.MPC+OboeoutperformsPensievefor81%of
thesessions,withaQoE-linimprovementof23.9%inaver-
ageacrossallsessions.25%ofthesessionsachievemorethan
20%QoE-linimprovement.ForthesessionsMPC+Oboe
Figure 12—Benefits of specializing Figure 13—QoE improvement of isunabletoimproveoverPensieve,theperformancediffer-
Pensievemodels.Eachcurveshowsthe MPC+Oboe over two ways of dy- enceismostlylessthan5%.Figures9(b),9(c)and9(d)show
| QoEimprovementofMPC+Oboerela- |     |     | namically | selecting | from | specialized |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --------- | --------- | ---- | ----------- | --- | --- | --- | --- | --- | --- |
tivetoeachPensievemodel. Pensievemodels. thatMPC+OboedistributionallyoutperformsPensievewith
|          |             |           |     |     |          |         | respect to | all underlying |     | metrics. It | reduces | the number of |
| -------- | ----------- | --------- | --- | --- | -------- | ------- | ---------- | -------------- | --- | ----------- | ------- | ------------- |
| MPC+Oboe | outperforms | RobustMPC |     | as  | well, we | explore |            |                |     |             |         |               |
sessionswithrebufferingfrom10.7%to5.3%,reducesthe
| how MPC+Oboe | performs | relative |     | to Pensieve. | Our | exper- |     |     |     |     |     |     |
| ------------ | -------- | -------- | --- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- |
medianperchunkchangemagnitudeby43.9%,andimproves
| iments use | the Pensieve | implementation |     |     | provided | by the |     |     |     |     |     |     |
| ---------- | ------------ | -------------- | --- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- |
medianand95thpercentileaveragebitrateby2.6%and4.7%
authors[11].
respectively.Finally,Figure11showstheCDFofQoE-lin
forMPC+OboeandPensieve,andindicatesMPC+Oboeper-
| PensieveRe-TrainingandValidation. |     |     |     |     | Beforeevaluating |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
Pensieveonourdataset,weretrainPensieveusingthesource formsdistributionallybetter.
codeonthetracedatasetprovidedbythePensieveauthors Analyzing Pensieve performance. To understand where
[11]. This helps us validate our retraining given that deep theseperformanceimprovementswerecomingfrom,weex-
reinforcementlearningresultsarenoteasytoreproduce[29].
aminedtherelativeperformanceofthesetwoschemesinthe
Weexperimentedwithfivedifferentinitialentropyweights 0-3Mbpsrange(i.e.,traceshavinganaveragethroughputbe-
intheauthorsuggestedrangeof1to5,andlinearlyreduced tween0-3Mbps).Inthismoreconstrainedrangeofnetwork
their values in a gradual fashion using plateaus, with five conditions,wefoundthatMPC+Oboeachievesbiggergains
differentdecreaseratesuntiltheentropyweighteventually overPensieve(averageQoE-linimprovementin0-3Mbps
| reached | 0.1. This rate | scheduler | follows |     | best-practice | [55]. |     |     |     |     |     |     |
| ------- | -------------- | --------- | ------- | --- | ------------- | ----- | --- | --- | --- | --- | --- | --- |
is46.23%).Wehypothesizethatthisperformancedifference
From the trained set of models, we then selected the best stemsfromthefactthatPensievebuildsasinglemodelwhich
performing model (an initial entropy weight of 1 reduced doesnotspecializetodifferentthroughputranges.
every800iterationsuntilitreaches0.1over100Kiterations)
Totestthis,wetrainedaseparatePensievemodelonlywith
and compared its performance to the pre-trained Pensieve traces that have an average throughput between 0-3 Mbps
| model provided | by the | authors. | Figure | 10  | shows | CDFs of |           |          |         |           |        |          |
| -------------- | ------ | -------- | ------ | --- | ----- | ------- | --------- | -------- | ------- | --------- | ------ | -------- |
|                |        |          |        |     |       |         | range and | compared | it with | MPC+Oboe. | Figure | 12 shows |
QoE-linforthepretrained(Original)modelandthemodel thepersessionQoE-linimprovementofMPC+Oboecom-
trainedbyus(Retrained).Theperformancedistributionofthe pared to Pensieve models trained for 0-3 Mbps (which we
twomodelsarealmostidenticaloverthetesttracesprovided
|     |     |     |     |     |     |     | refer to | as Pens-Specialized) |     | and for | 0-6 Mbps. | The me- |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------------------- | --- | ------- | --------- | ------- |
by the Pensieve authors, thereby validating our retraining dian QoE-lin improvement with MPC+Oboe over Pens-
methodology.
Specializedis10.49%,whilethemedianimprovementover
52

| SIGCOMM’18,August20–25,2018,Budapest,Hungary |     |     |     |     |     |     |     |     | Z.Akhtaretal. |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
Figure14—PercentageimprovementinbitrateandrebufferingofBOLA+OboeoverBOLA(a),(b)andHYB+OboeoverHYB(c),(d)
offerssomeimprovementsoverthe0-6MbpsPensievemodel,
|     |     |     |     | the benefits | are | modest. | We hypothesize |     | that this | behavior |
| --- | --- | --- | --- | ------------ | --- | ------- | -------------- | --- | --------- | -------- |
isduetothedynamicselectionofdistinctPensievemodels,
|     |     |     |     | which can | interfere | with   | reinforcement | learning’s        |     | decision |
| --- | --- | --- | --- | --------- | --------- | ------ | ------------- | ----------------- | --- | -------- |
|     |     |     |     | choices,  | since,    | during | training,     | the reinforcement |     | learning |
algorithmassumesthereisnosuchthirdpartyintervention.
4.5 OboewithotherABRAlgorithms
Figure15—AverageQoE-linofMPC+Oboewithvariousthroughputpredictors OboecanalsoimproveotherexistingABRalgorithmssuch
asBOLAandHYB,whicharedesignedtomaximizeaverage
Pensieveis19.9%.Thisindicatesspecializingthemodeldoes
bitratewhileminimizingrebuffering.
improvePensieve’sperformance.
|     |     |     |     | BOLA. | BOLA+Oboetunes𝛾 |     |     | (§2),whichdetermineshow |     |     |
| --- | --- | --- | --- | ----- | --------------- | --- | --- | ----------------------- | --- | --- |
Thus,Pensieve’smodelisasyetunabletocreatespecial-
muchthealgorithmstrivestoavoidrebuffering.BOLA,as
ized versions of itself based on the session characteristics. =
|     |     |     |     | implemented | in  | Dash.js, | uses | a fixed default | value | of 𝛾 |
| --- | --- | --- | --- | ----------- | --- | -------- | ---- | --------------- | ----- | ---- |
Bycontrast,Oboespecializesparametersforeverynetwork
−10.28.Figure14(a)and14(b)showCDFsofpersession
stateandthereforeperformsbetter.Wehavealsovalidated
|     |     |     |     | performance | improvement |     | over | BOLA with | respect | to av- |
| --- | --- | --- | --- | ----------- | ----------- | --- | ---- | --------- | ------- | ------ |
Pensieve’sinabilitytospecializeinseveralotherways:build-
eragebitrateandrebufferingratio.BOLA+Oboemaintains
ingamodelforthe3-6Mbpsandshowingthatitperforms
therebufferingratioofBOLAwhileimprovingaveragebi-
| better with | test data in that | range compared | to a 0-6 Mbps |     |     |     |     |     |     |     |
| ----------- | ----------------- | -------------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
tratesformorethan83%ofsessionswithanoverallincrease
model;checkingthata0-6Mbpsmodelperformsbetterfor
|         |                     |                 |            | of 7.2% | in average | across | all sessions. | For | sessions | where |
| ------- | ------------------- | --------------- | ---------- | ------- | ---------- | ------ | ------------- | --- | -------- | ----- |
| data in | that range compared | to a 0-100 Mbps | model; and |         |            |        |               |     |          |       |
BOLA+OboedoesnotoutperformBOLA,itsdegradationis
ensuringthattheseresultsholdevenwhenthetrainingsetis
lessthan3.1%.
doubled.ItishardtopinpointexactlywhyPensieveisunable
HYB. TheperformanceofHYBissensitivetothechoice
tolearntobemoreconservativeinthe0-3Mbpsrange;deep
of𝛽parameter,whichHYB+Oboetunes.Inproduction,HYB
neuralnetworkmodelsremainablackboxdespiteeffortsby
uses𝛽 =0.25,determinedusingA/Btestsinalarge-scalede-
themachinelearningcommunitytomakethesemodelsmore
ployment.Figure14(c)and14(d)showCDFsofpersession
transparent[45],andobtainingsuchunderstandingmayneed
|     |     |     |     | performance | improvement |     | of average | bitrate | and | rebuffer- |
| --- | --- | --- | --- | ----------- | ----------- | --- | ---------- | ------- | --- | --------- |
furtheradvancesininterpretabledeeplearningmodels.
ingratiooverHYB.AswithBOLA,HYB+Oboemaintains
| AmodelselectorwithPensieve. |     | OnewaytoimprovePen- |     |         |             |        |          |           |     |          |
| --------------------------- | --- | ------------------- | --- | ------- | ----------- | ------ | -------- | --------- | --- | -------- |
|                             |     |                     |     | similar | rebuffering | ratios | as shown | in 14(d), | but | improves |
sieve’sspecializationmightbetotraindifferentmodelsfor
bitratesfor98%ofsessionswithanoverallaveragebitrate
differentthroughputrangesandusethemodelmoresuited improvementof8.32%inaverageacrossallsessions.
| to the network | conditions. | To test the efficacy | of this ap- |     |     |     |     |     |     |     |
| -------------- | ----------- | -------------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
4.6 Sensitivityexperiments
proach,weusedtwomodels(specializedfor0-3Mbpsand
3-6 Mbps), and tried two different model selectors. Pens- Alternativethroughputtraces. TounderstandhowOboe
SelMultipleswitchesmodelsthroughoutthesession,using
worksonthroughputdatasetsbeyondthosediscussedin§4.2,
theaveragethroughputofthepast5chunks.Pens-SelOnce weevaluatedOboeontwootherdatasets,FCC[8]andHS-
startswiththe0-6Mbpsmodel,selectseitherthe0-3Mbps DPA[46]thathavebeenusedinrecentwork[39,59].FCC
or3-6Mbpsmodelbasedontheaveragethroughputofthe is a broadband dataset, while HSDPA contains throughput
first5initialchunks,anddoesnotswitchthereafter. tracescollectedfromvideostreamingsessionsover3Gnet-
Figure13showsCDFsofper-sessionQoE-linimprove-
worksinNorwayusingmobiledevices.Ourcomparisonsuse
mentofMPC+Oboeovertheseselectors.MPC+Oboeisable thetracesandaPensievemodelpre-trainedforthosetraces
tooutperformbothPens-SelMultileandPens-SelOnce,with availableat[11].WefocusourevaluationsonMPC+Oboe
averageQoE-linimprovementsof14.2%and24.32%re-
|     |     |     |     | and Pensieve, |     | given that | Pensieve | has been | shown | to out- |
| --- | --- | --- | --- | ------------- | --- | ---------- | -------- | -------- | ----- | ------- |
spectively.Eventhoughoneofthemodelselectionschemes perform existing ABR schemes including RobustMPC on
53

| Oboe |     |     |     |     |     |     |     | SIGCOMM’18,August20–25,2018,Budapest,Hungary |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
Figure16—ComparingHYBwithmultiplefixedconfigurationsandHYB+Oboeforvarioussettings
thesetraces.OurresultsshowthatMPC+Oboecontinuesto withRobustMPC,whichdependsontheexactsequenceof
performbetterthanRobustMPConthesetraces.Further,rela- bitrateschosenduringthelook-aheadwindow.Theduration
tivetoPensieve,MPC+OboeimprovesQoE-linbyanaver- isnotknownapriori,sinceRobustMPCitselfdeterminesthe
ageof6.94%acrosstheFCCdatasetand10.92%acrossthe bitratesbasedonaprovidedprediction.Second,thedecisions
HSDPAdataset.Theseimprovementsaremoremodestthan madebyRobustMPCareoverasmalllook-aheadwindow,
thoseinFigure9(a).ThevastmajorityoftracesintheFCC whichmaynotguaranteeoptimalityovertheentiresession
| andHSDPAsethaveanaveragethroughputunder3Mbps |     |     |     |     |     |     |     | duration. |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
(over95%forFCCand98%forHSDPA).Theresultscor-
4.7 OboeAcrossVariousSettings
roborateFigure12whichindicatesthatMPC+Oboeprovides
moremodestgainsoverPensievewhenthelatteristrained In §4.5 we have shown that Oboe outperforms other ABR
and evaluated on datasets with a narrow throughput range. algorithms when compared to their default configurations.
|     |     |     |     |     |     |     |     | We now | explore, for HYB, | whether Oboe outperforms |     | all |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------------- | ------------------------ | --- | --- |
MPC+Oboeprovideslargergainsinsettingslikethetraces
discussedin§4.2,whereonly41%tracesareunder3Mbps parameter settings of HYB and whether it can tune ABRs
basedoncontenttypeandpublisherspecifications.Forthese
| and59%areinthe3-6 |     |     | Mbpsrange. |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
experiments,weusetheVirtualPlayerdescribedin§3.2.
| Alternative | throughput |     | prediction |     | methods. | Our | experi- |                                          |     |     |           |     |
| ----------- | ---------- | --- | ---------- | --- | -------- | --- | ------- | ---------------------------------------- | --- | --- | --------- | --- |
|             |            |     |            |     |          |     |         | Comparisonagainstallfixedconfigurations. |     |     | Toexplore |     |
mentswithRobustMPCrelyonthroughputpredictionbased
differentfixedconfigurations,werunHYBwith10different
ontheharmonicmeanofpriorthroughputsamples(follow- fixed𝛽sandcomparewithHYB+Oboe.Wesummarizethe
ingearlierwork[39,59]),withOboetuningtheconfigura-
|     |     |     |     |     |     |     |     | performance | for each configuration | by considering |     | the (i) |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------------------- | -------------- | --- | ------- |
tion to compensate for prediction errors. We next consider medianoftheaveragebitrateandthe(ii)90thpercentileof
| if Oboe’s | benefits | hold | if RobustMPC |     | were | to have | more |     |     |     |     |     |
| --------- | -------- | ---- | ------------ | --- | ---- | ------- | ---- | --- | --- | --- | --- | --- |
therebufferingratioacrosstesttraces.Inthisexperiment,we
| accurate | throughput | predictions, |     | potentially |     | by using | alter- |     |     |     |     |     |
| -------- | ---------- | ------------ | --- | ----------- | --- | -------- | ------ | --- | --- | --- | --- | --- |
alsoconsideranOraclewhichisthebestfixedconfiguration
nate prediction methods [49]. Rather than using a specific for each throughput trace with respect to two metrics that
predictiontechnique,weconsideranideal(andunachievable)
HYBtriestooptimize.
approachthatwedenoteasIdeal(T),whichcanexactlypredict
|     |     |     |     |     |     |     |     | Figure | 16(a) and 16(b) compare | HYB, HYB+Oboe |     | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------------------- | ------------- | --- | --- |
theaveragethroughputoverthenextTseconds.Ourexperi-
Oracleoverdesktop,andmobiletracesrespectively.While
mentswereconductedinsimulation,usingtheVirtualPlayer,
OracleandHYB+Oboearedepictedassingledotssincetheir
andthetestbedexperimenttraces(§4.2). performance is uniquely determined, we present a frontier
Figure15showstheaverageQoE-linacrossthetraces
forHYBthatshowsitsperformancefordifferentfixedcon-
forRobustMPCandMPC+Oboeusingboththedefaulthar-
figuration.Figure16(a)showsthatHYB+Oboeoutperforms
monicmeanapproachandIdeal(T)fordifferentvaluesofT.
HYBinthesensethatthereisnofixedconfigurationforHYB
AlthoughRobustMPCperformsbetterwithanidealpredictor,
thatdoesbetterthanHYB+Oboeperformance.HYB+Oboe
Oboestillprovidesbenefits,achievinganaverageimprove- improvestheaveragebitratesofthemediansessionby3.2%,
| ment in | QoE-lin | of  | 6.34% | for Ideal(5) |     | and of | 1.8% for |                 |                     |                     |     |        |
| ------- | ------- | --- | ----- | ------------ | --- | ------ | -------- | --------------- | ------------------- | ------------------- | --- | ------ |
|         |         |     |       |              |     |        |          | while achieving | similar rebuffering | ratio. Alternately, |     | it re- |
Ideal(10),comparedtoa16.1%improvementwiththehar-
ducesthe90thpercentilerebufferingratiofrom1.9%to0%,
| monic mean | estimator. |     | While | the magnitude |     | of benefits | is  |     |     |     |     |     |
| ---------- | ---------- | --- | ----- | ------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
whilemaintainingsimilarbitrates.Asimilarresultholdsfor
smallerwiththeidealpredictionapproach,inpracticeOboe
mobiletraces(Figure16(b)).Thus,evenifpublisherswere
willlikelyresultinlargerbenefits,sinceevenmoresophisti- tofindthebestfixedparameterchoiceforHYB,Oboewould
catedschemes[49]cannotachievetheidealpredictions,and
|     |     |     |     |     |     |     |     | outperform | that choice because | it dynamically | adapts | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------- | -------------- | ------ | --- |
theerrorsarelikelytogrowwithlargerT.
parameters.
Oboe can improve performance over RobustMPC even Comparison under different publisher specifications.
whenanIdeal(T)predictionmethodisusedfortworeasons.
OurresultssofarareforaVoD(videoondemand)setting
𝑇
First, may not match the duration of chunk downloads with a maximum buffer size of 2 minutes. Figure 16(c)
54

| SIGCOMM’18,August20–25,2018,Budapest,Hungary |     |              |                    |     |                  |     |     |     |     |     | Z.Akhtaretal. |     |
| -------------------------------------------- | --- | ------------ | ------------------ | --- | ---------------- | --- | --- | --- | --- | --- | ------------- | --- |
| Figure 17—Avg.                               | of  | avg. bitrate | and Figure 18—Avg. | of  | avg. bitrate and |     |     |     |     |     |               |     |
fractionofsessionswithrebufferingfor fraction of sessions with rebuffering Figure19—ComparingprototypeOboewithcommercialclientsideABRimplemen-
HYB+Oboeanddifferentpublisherpref- forRobustMPCanddifferentpublisher tationinaveragebitrateandrebufferingratio.
| erences |     |     | preferences |     |     |     |     |     |     |     |     |     |
| ------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
depictsperformanceforlivevideo(whichusesamaximum
buffersizeof20secondstomimiclivesettings).HYB+Oboe
| outperforms   | HYB  | for this   | setting, though | we        | note that the |     |     |     |     |     |     |     |
| ------------- | ---- | ---------- | --------------- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| bitrate of    | both | approaches | degrades        | relative  | to the VoD    |     |     |     |     |     |     |     |
| setting since | the  | baseline   | HYB switches    | to higher | bitrates      |     |     |     |     |     |     |     |
moreconservativelyowingtothesmallerbuffersizes.
|          |        |       |                     |     |            | Figure20—Timebetweenconsecutive |     |                | Figure                             | 21—Variance | in bitrate | levels |
| -------- | ------ | ----- | ------------------- | --- | ---------- | ------------------------------- | --- | -------------- | ---------------------------------- | ----------- | ---------- | ------ |
| Finally, | Figure | 16(d) | depicts performance | for | higher bi- |                                 |     |                |                                    |             |            |        |
|          |        |       |                     |     |            | bitrate switches                | for | two commercial | acrossvideosfromtwocontentpublish- |             |            |        |
|          |        |       |                     |     |            | ABRs                            |     |                | ers.                               |             |            |        |
tratelevels({1002,1434,2738,3585,4661,5886}𝑘𝑏𝑝𝑠)and
achunksizeof5seconds.Evenforthesechoices,HYB+Oboe
cycleacrossourexperiments,andthemeasurementindicates
outperformsHYB,demonstratingitsabilitytoadapttodiffer-
thatthemedianprocessingtimeofChangeDetectorisaround
entpublisherspecification.
14ms.Sinceeachdecisionismadeatachunkboundaryand
| Accommodatingpublisher’srebufferingtolerance. |     |     |     |     | Oboe |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
chunksare4seconds,ChangeDetectoraccountsforlessthan
| allows the | publisher | to optionally | specify | explicit | rebuffer- |     |     |     |     |     |     |     |
| ---------- | --------- | ------------- | ------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
0.35%overhead.
ingpreferences(§3).ABRalgorithmssuchasRobustMPC
whichusetheQoE-linfunctionmaypermitthisindirectly
byadjustingQoE-linweights(§2.1).Figure17showsthe 5 DEPLOYMENTCONSIDERATIONS
| effectiveness | of  | these approaches, | showing | the | average of |     |     |     |     |     |     |     |
| ------------- | --- | ----------------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
TheofflinestageofOboecanberunonthecloud,butseveral
averagebitrates,andthefractionofsessionswithrebuffering
choicesexistfortheonlinestage,rangingfromembedding
forHYB+Oboe.Asthepublishermakesitsrebufferingpref-
theonlinestageentirelyintheclientplayer,ormovingsome
| erence stricter | (from | 2%-0%), | HYB+Oboe | achieves | lower |     |     |     |     |     |     |     |
| --------------- | ----- | ------- | -------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
oralloftheonlinestagetothecloud.Inourimplementation,
rebufferingratiosclosetothetargetrebufferingtolerance.In
|     |     |     |     |     |     | Oboe’s components |     | run on | the server | side. | This mimics | a   |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | ------ | ---------- | ----- | ----------- | --- |
contrast,Figure18showsthatRobustMPCislesseffective
cloudimplementation,whichhasthebenefitsofothercloud
atcontrollingrebufferingbyadjustingitsrebufferingpenalty
software:fastupdatedeployment,deviceindependence,etc.
whentheweightontherebufferingtermisvariedbetween
[4].Weleaveadetailedcomparisonofthesechoicestofuture
100(strictlyavoidrebuffering)to4.3.5Wefindthatevenwith
work,butexplore,inthissection,thefeasibilityofrunning
averyhighrebufferingpenaltyof100,RobustMPCcauses
theonlinestageonthecloud.
rebufferingin11%ofthesessions.Thisshowsthebenefitof
Tothisend,wehaveimplementedarestrictedversionof
Oboe’sapproachwhichgivesdirectcontrolovertheunderly-
|     |     |     |     |     |     | HYB+Oboe | on  | AWS. This | limited | version | of Oboe imple- |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --------- | ------- | ------- | -------------- | --- |
ingmetrics.
mentsHYBandincorporatestuningbasedonpublisherspeci-
ficationsbutnotnetworkstate.Inourimplementation,aclient
4.8 OboeOverhead
playerperiodicallyreportsplayerstate(suchasbufferlength
ComputingtheConfigMapincursaone-timecost,sincethe
andcurrentbitrate)andthroughputsamplestoaOboecloud
mapcanbereusedacrossallclientsoncetheitisbuilt.Com-
serverandreceivesbitratedecisionsinreturn.For10player
putingthebestparameterconfigurationforonenetworkstate
featuresandtwochunkdownloadspersecond,thecommu-
takesabout12secondsonasinglecore.Thistaskisperfectly
nicationoverheadis6.4Kbps,negligiblysmallcomparedto
| parallelizable, | so  | computing | 10K network | states | (§3) will |     |     |     |     |     |     |     |
| --------------- | --- | --------- | ----------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
thesizeofvideochunks.Figures19(a)and19(b)comparethe
takeapproximately3.5hourstoexplorewithtwomachines
performanceofthisimplementationagainstaclientplayer
of48coreseach.Wehavealsoanalyzedtheprocessingover-
runningHYBover20Ksessionscollectedduringatwo-week
headincurredbytheChangeDetectormoduleofOboe.We
pilotdeployment.Oboeiscomparableinperformancetothe
measurethetimetakenbyChangeDetectorforeverydecision
clientsideplayerandevenimprovesbitrateslightly(because
itwastunedtothispublisher’sspecification).
5Weusedachangepenaltyof0forfaircomparison.
55

| Oboe |     |     |     |     |     |     | SIGCOMM’18,August20–25,2018,Budapest,Hungary |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
Weexpectedacloudimplementationwouldperformworse onnetworkstate,andpublisherspecifications.Theapproach
becauseofthelatencyinducedbyclient-servercommunica- is generically applicable to many ABR algorithms. Newer
tion.However,wefoundthatmostofthebitrateswitching congestioncontrolprotocolslikeBBR[19]estimatenetwork
decisions occur on timescales much longer than the client- throughput,whichifexposed,couldbenefitOboe.
serverlatencies.Figure20showstheCDFofthetimeinterval LearningABRAlgorithms. AmongABRalgorithmsthat
betweenconsecutivebitrateswitchesforABRalgorithmsin useReinforcementLearningandothermachinelearningtech-
two widely used video players(Adobe’s Flash [3] and Mi- niques[20,21,39,40,53],Pensieve[39]hasbeenshownto
crosoftSmoothStreaming[1]).Thefigureshowsthatover performthebest.WhilePensievedoesnotspecializetodiffer-
| 95% of switching | decisions |     | occur | at intervals | higher | than |     |     |     |     |     |     |
| ---------------- | --------- | --- | ----- | ------------ | ------ | ---- | --- | --- | --- | --- | --- | --- |
entthroughputregimes,Oboeperformsbetterbyspecializing
1secondforbothplayers.Thissuggeststhatacloud-based parametervaluesforeachnetworkstateindependently.
deploymentisviable.
|     |     |     |     |     |     |     | Otherworkinself-tuning. |     |     | BeyondABRalgorithms,self- |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | ------------------------- | --- | --- |
tuningapproacheshavebeenexploredinothercontexts.Win-
6 DISCUSSIONANDFUTUREWORK
steinetal.[56]usedsimulationstodetermineTCPparameters
| Performance | improvements |     | for | all sessions. | As  | our re- |     |     |     |     |     |     |
| ----------- | ------------ | --- | --- | ------------- | --- | ------- | --- | --- | --- | --- | --- | --- |
fordifferentsettings,whileSemkeetal.[47]proposedtuning
(e.g.,
sults Figure 6(a)) show, Oboe improves the perfor- TCPsocketbufferstoensurehighthroughput.Moregener-
manceformostbutnotallsessionsrelativetotheABRal-
ally,GoogleVizier[28]performssuchblack-boxtuningas
| gorithm | it tunes. For | instance, | after | inspecting | the | results |     |     |     |     |     |     |
| ------- | ------------- | --------- | ----- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- |
aservice.WhileViziercanpotentiallybeusedtoimplement
in§4.3,wehavefoundthatMPC+Oboetypicallyimproves the offline phase of Oboe, our work identifies underlying
performancerelativetoRobustMPCbyreducingrebuffering
|     |     |     |     |     |     |     | principles | (such | as the piecewise | stationarity |     | of available |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ---------------- | ------------ | --- | ------------ |
and/orthemagnitudeofbitratechanges,butattheexpenseof
throughput)thatformsthebasisforthetuning.
slightlylowerbitrates.TheresultingQoE-linisimproved
|     |     |     |     |     |     |     | Video | QoE. Several | researchers | have | pointed | out that |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | ----------- | ---- | ------- | -------- |
formostsessions,indicatingOboedoesagoodjobofproperly
|           |             |          |     |               |     |       | sub-optimal     | ABR | performance | can     | significantly | impact      |
| --------- | ----------- | -------- | --- | ------------- | --- | ----- | --------------- | --- | ----------- | ------- | ------------- | ----------- |
| balancing | the various | factors, | but | some sessions | see | lower |                 |     |             |         |               |             |
|           |             |          |     |               |     |       | user-engagement |     | and hence   | revenue | [16, 37].     | Others have |
QoE-lin.Moregenerally,designinganABRapproachthat
|     |     |     |     |     |     |     | looked at | quality | issues that | occur when | multiple | players |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ----------- | ---------- | -------- | ------- |
canoptimizetheperformanceofallsessionsisahardproblem
starttocompeteforbandwidth[15,30,31,34]Incontrast,
thatneedsmoreresearch.
|         |           |        |         |      |      |          | Oboe improves |     | the QoE performance |     | of  | several ABR |
| ------- | --------- | ------ | ------- | ---- | ---- | -------- | ------------- | --- | ------------------- | --- | --- | ----------- |
| Sharing | ConfigMap | across | videos. | Oboe | need | not per- |               |     |                     |     |     |             |
algorithmsacrossarangeofdifferentnetworkconditionsby
form offline precomputation for each individual video, as automaticallytuningtheirparameters.
itcanuseasingleConfigMapforaclassofvideosthatfollow
asimilarbitrateencodingscheme.Figure21showsthattwo
|     |     |     |     |     |     |     | 8 CONCLUSION |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
popularvideopublishersusesimilarencodingschemesacross
OboeisasystemforautomaticallytuningABRalgorithms
twothousandvideoseach.Publisher1uses7distinctbitrate
|     |     |     |     |     |     |     | by adapting | ABR | configurations | in realtime |     | to match the |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------------- | ----------- | --- | ------------ |
levels,andthecoefficientofvarianceacrossbitrateswithin current network state. Picking configurations in a manner
| each level | is only 0.13, | while | Publisher2, | uses | 10  | distinct |     |     |     |     |     |     |
| ---------- | ------------- | ----- | ----------- | ---- | --- | -------- | --- | --- | --- | --- | --- | --- |
informedbynetworkstateandpublisherpreferencesdistin-
bitratelevels,andthecoefficientofvarianceacrossbitrates
guishesOboe’sapproachfromheuristicsusedtodaythatdo
withineachlevelisonly0.067.Thisindicatesthepotentialto
notconsiderthesefactors.Oboesignificantlyimprovesthe
shareasingleConfigMapacrossvideos.
performanceofBOLA,HYBandRobustMPC;further,for
GeneralityofOboe. WhilewehaveshownthatOboecan nearly 80% of the sessions in our dataset, Oboe integrated
tuneavarietyofconfigurationparametersacrossseveralABR
|     |     |     |     |     |     |     | with RobustMPC |     | improves QoE-lin |     | relative | to Pensieve |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------------- | --- | -------- | ----------- |
algorithms,whetherOboecantuneallalgorithmsandallpa-
andtheimprovementsexceed20%for25%ofthesessions.
rametersisanopenquestion.ItisunclearifOboecandirectly
augmentPensieve,sinceamodellearnedbyreinforcement Acknowledgments.Wethankourshepherd,MohammadAl-
|          |                  |     |           |                |     |         | izadeh and | the anonymous | reviewers |     | for their | constructive |
| -------- | ---------------- | --- | --------- | -------------- | --- | ------- | ---------- | ------------- | --------- | --- | --------- | ------------ |
| learning | may not interact |     | well with | intermediaries |     | such as |            |               |           |     |           |              |
Oboe.However,combiningthebenefitsofOboeandPensieve feedback. We thank Oleg White, Yan Li and Shubo Liu
inotherwaysisaninterestingavenueforfuturework. for their assistance obtaining the throughput data and for
|     |     |     |     |     |     |     | helpful discussions. |     | This work | was funded |     | in part by the |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --------- | ---------- | --- | -------------- |
7 RELATEDWORK
NationalScienceFoundation(NSF)AwardsCNS-1618921,
TuningABRAlgorithmConfigurations. TheBBA2algo- CNS-1564242,andCNS-1413978;andtheARO,underthe
rithm[32]tunesitslowerreservoirbasedonbufferoccupancy U.S.ArmyResearchLaboratoryawardW911NF-09-2-0053.
dynamics,whileMPC[59]adaptsitsthroughputdiscountfac- Anyopinions,findingsandconclusionsorrecommendations
expressedinthismaterialarethoseoftheauthorsanddonot
torbasedonpastpredictionerrors(§2).Incontrasttosuchad-
hocheuristics,Oboeselectsconfigurationparametersbased necessarilyreflecttheviewsofNSForARO.
56

SIGCOMM’18,August20–25,2018,Budapest,Hungary Z.Akhtaretal.
BIBLIOGRAPHY
[30] RémiHoudailleandStéphaneGouache. ShapingHTTPAdaptiveStreamsfora
[1] MicrosoftSmoothStreaming. http://www.iis.net/downloads/microsoft/smooth- BetterUserExperience. InProceedingsoftheMultimediaSystemsConference,
streaming. MMSys,2012.
[2] Toward A Practical Perceptual Video Quality Metric. https://medium. [31] Te-YuanHuang,NikhilHandigol,BrandonHeller,NickMcKeown,andRamesh
com/netflix-techblog/toward-a-practical-perceptual-video-quality-metric- Johari.Confused,Timid,andUnstable:PickingaVideoStreamingRateisHard.
653f208b9652. InProceedingsoftheACMConferenceonInternetMeasurementConference,
[3] AdobeOSMFplayer.http://www.osmf.org. IMC,2012.
[4] Oracle:5ReasonstoConsiderSaaSforYourBusinessApplications.http://www. [32] Te-YuanHuang,RameshJohari,NickMcKeown,MatthewTrunnell,andMark
oracle.com/us/solutions/cloud/saas-business-applications-1945540.pdf. Watson. ABuffer-basedApproachtoRateAdaptation:EvidencefromaLarge
[5] Chrome Remote Interface. https://github.com/cyrus-and/chrome-remote- VideoStreamingService. InProceedingsoftheACMConferenceonSpecial
interface. InterestGrouponDataCommunication,SIGCOMM,2014.
[6] Cisco:ItCametoMeinaStream.https://www.cisco.com/web/about/ac79/docs/ [33] DanielR.Jeske,VeronicaMontesDeOca,WolfgangBischoff,andMazdaMar-
sp/Online-Video-Consumption_Consumers.pdf. vasti. CusumTechniquesforTimeslotSequenceswithApplicationstoNetwork
[7] DASHIndustryForum.https://github.com/Dash-Industry-Forum/dash.js. Surveillance.ComputationalStatisticsandDataAnalysis,53:4332–4344,2009.
[8] FederalCommunicationsCommission.RawData-MeasuringBroadbandAmer- [34] JunchenJiang,VyasSekar,andHuiZhang.ImprovingFairness,Efficiency,and
ica. www.fcc.gov/reports-research/reports/measuring-broadband-america/raw- StabilityinHTTP-basedAdaptiveVideoStreamingwithFESTIVE.InProceed-
data-measuring-broadband-america-2016. ingsoftheACMInternationalConferenceonEmergingNetworkingExperiments
[9] Google-Chrome:ChromeDevToolsProtocol. https://chromedevtools.github.io/ andTechnologies,CoNEXT,2012.
devtools-protocol/tot/Network/. [35] JamesJobin,MichalisFaloutsos,SatishKTripathi,andSrikanthVKrishna-
[10] Bayesian Changepoint Detection. https://github.com/hildensia/bayesian_ murthy. UnderstandingtheEffectsofHotspotsinWirelessCellularNetworks.
changepoint_detection. InProceedingsoftheConferenceoftheIEEEComputerandCommunications
[11] Pensieve.https://github.com/hongzimao/pensieve. Societies,INFOCOM,2004.
[12] DASHIndustryForum.https://dash.akamaized.net/envivio/EnvivioDash3. [36] EamonnJ.Keogh,SelinaChu,DavidHart,andMichaelJ.Pazzani. AnOnline
[13] Sandvine: Global Internet phenomena report . https://www.sandvine.com/ AlgorithmforSegmentingTimeSeries.InProceedingsoftheIEEEInternational
downloads/general/global-internet-phenomena/2014/2h-2014-global-internet- ConferenceonDataMining,ICDM,2001.
phenomena-report.pdf. [37] S.ShunmugaKrishnanandRameshK.Sitaraman. VideoStreamQualityIm-
[14] RyanPrescottAdamsandDavidJCMacKay. BayesianOnlineChangepoint pactsViewerBehavior:InferringCausalityUsingQuasi-experimentalDesigns.
Detection.InarXiv:0710.3742v1,2007. InProceedingsoftheACMConferenceonInternetMeasurementConference,
[15] Saamer Akhshabi, Lakshmi Anantakrishnan, Ali C Begen, and Constantine IMC,2012.
Dovrolis. WhatHappenswhenHTTPAdaptiveStreamingPlayersCompetefor [38] DongLu,YiQiao,PeterADinda,andFabianEBustamante.Characterizingand
Bandwidth? IntheInternationalWorkshoponNetworkandOperatingSystem PredictingTCPThroughputontheWideAreaNetwork. InIEEEInternational
SupportforDigitalAudioandVideo,NOSSDAV,2012. ConferenceonDistributedComputingSystems,ICDCS,2005.
[16] AthulaBalachandran,VyasSekar,AdityaAkella,SrinivasanSeshan,IonStoica, [39] HongziMao,RaviNetravali,andMohammadAlizadeh.NeuralAdaptiveVideo
andHuiZhang. DevelopingaPredictiveModelofQualityofExperiencefor StreamingwithPensieve. InProceedingsoftheACMConferenceonSpecial
InternetVideo.InProceedingsoftheACMConferenceonSpecialInterestGroup InterestGrouponDataCommunication,SIGCOMM,2017.
onDataCommunication,SIGCOMM,2013. [40] VirginiaMartín,JuliánCabrera,andNarcisoGarcía. Design,Optimizationand
[17] HariBalakrishnan,MarkStemm,SrinivasanSeshan,andRandyHKatz. Ana- EvaluationofaQ-learningHTTPAdaptiveStreamingClient.IEEETransactions
lyzingStabilityinWide-areaNetworkPerformance.ACMSIGMETRICSPerfor- onConsumerElectronics,62(4):380–388,2016.
manceEvaluationReview,25:2–12,1997. [41] VolodymyrMnih,KorayKavukcuoglu,DavidSilver,AndreiARusu,JoelVe-
[18] DanielBarryandJohnAHartigan.ABayesianAnalysisforChangePointProb- ness, Marc G Bellemare, Alex Graves, Martin Riedmiller, Andreas K Fidje-
lems.JournaloftheAmericanStatisticalSociety,88(421):309–319,1993. land,GeorgOstrovski,etal.Human-levelControlThroughDeepReinforcement
[19] NealCardwell,YuchungCheng,C.StephenGunn,SoheilHassasYeganeh,and Learning.Nature,518(7540):529–533,2015.
VanJacobson. BBR:Congestion-BasedCongestionControl. ACMQueue,14: [42] VolodymyrMnih,AdriaPuigdomenechBadia,MehdiMirza,AlexGraves,Tim-
20–53,2016. othyLillicrap,TimHarley,DavidSilver,andKorayKavukcuoglu.Asynchronous
[20] FedericoChiariotti,StefanoD’Aronco,LauraToni,andPascalFrossard.Online MethodsforDeepReinforcementLearning.InProceedingsoftheInternational
LearningAdaptationStrategyforDASHClients.InProceedingsoftheInterna- ConferenceonMachineLearning,ICML,2016.
tionalConferenceonMultimediaSystems,MMSys,2016. [43] HosseinPishro-Nik. IntroductiontoProbability,StatisticsandRandomPro-
[21] MaximClaeys,StevenLatré,JeroenFamaey,TingyaoWu,WernerVanLeek- cesses.KappaResearch,2014.
wijck,andFilipDeTurck. DesignandOptimisationofa(FA)Q-learning-based [44] ThanawinRakthanmanon,EamonnJ.Keogh,StefanoLonardi,andScottEvans.
HTTPAdaptiveStreamingClient.ConnectionScience,26(1):25–43,2014. TimeSeriesEpenthesis:ClusteringTimeSeriesStreamsRequiresIgnoringSome
[22] Frédéric Desobry, Manuel Davy, and Christian Doncarli. An Online Kernel Data. InProceedingsoftheInternationalConferenceonDataMining,ICML,
ChangeDetectionAlgorithm. IEEETransactionsonSignalProcessing,53(8): 2011.
2961–2974,2005. [45] MarcoTulioRibeiro,SameerSingh,andCarlosGuestrin. WhyShouldITrust
[23] FlorinDobrian,VyasSekar,AsadAwan,IonStoica,DilipJoseph,AdityaGan- You?:ExplainingthePredictionsofAnyClassifier. InProceedingsoftheACM
jam,JibinZhan,andHuiZhang.UnderstandingtheImpactofVideoQualityon InternationalConferenceonKnowledgeDiscoveryandDataMining,SIGKDD,
UserEngagement. InProceedingsoftheACMConferenceonSpecialInterest 2016.
GrouponDataCommunication,SIGCOMM,2011. [46] HaakonRiiser,PaulVigmostad,CarstenGriwodz,andPålHalvorsen.Commute
[24] PaulFernhead.ExactandEfficientBayesianInferenceforMultipleChangepoint PathBandwidthTracesfrom3GNetworks:AnalysisandApplications. InPro-
Problems.StatisticsandComputing,16(2):203–213,2006. ceedingsoftheACMMultimediaSystemsConference,MMSys,2013.
[25] TobiasFlach,PavlosPapageorge,AndreasTerzis,LuisPedrosa,YuchungCheng, [47] JeffreySemke,JamshidMahdavi,andMatthewMathis. AutomaticTCPBuffer
TayebKarim,EthanKatz-Bassett,andRameshGovindan. AnInternet-Wide Tuning. InProceedingsoftheACMConferenceonSpecialInterestGroupon
AnalysisofTrafficPolicing. InProceedingsoftheACMConferenceonSpecial DataCommunication,SIGCOMM,1998.
InterestGrouponDataCommunication,SIGCOMM,2016. [48] KevinSpiteri,RahulUrgaonkar,andRameshKSitaraman.BOLA:Near-optimal
[26] WayneAFuller. IntroductiontoStatisticalTimeSeries. JohnWileyandSons, BitrateAdaptationforOnlineVideos. InProceedingsoftheIEEEInternational
1976. ConferenceonComputerCommunications,INFOCOM,2016.
[27] MojganGhasemi,ParthaKanuparthy,AhmedMansy,TheophilusBenson,and [49] YiSun,XiaoqiYin,JunchenJiang,VyasSekar,FuyuanLin,NanshuWang,Tao
JenniferRexford.PerformanceCharacterizationofaCommercialVideoStream- Liu,andBrunoSinopoli.CS2P:ImprovingVideoBitrateSelectionandAdapta-
ingService. InProceedingsoftheACMConferenceonInternetMeasurement tionwithData-DrivenThroughputPrediction. InProceedingsoftheACMCon-
Conference,IMC,2016. ferenceonSpecialInterestGrouponDataCommunication,SIGCOMM,2016.
[28] Daniel Golovin, Benjamin Solnik, Subhodeep Moitra, Greg Kochanski, John [50] RichardSSuttonandAndrewGBarto.Reinforcementlearning:Anintroduction.
Karro,andD.Sculley. GoogleVizier:AServiceforBlack-BoxOptimization. MITpressCambridge,1998.
InProceedingsoftheACMInternationalConferenceonKnowledgeDiscovery [51] GuibinTianandYongLiu. TowardsAgileandSmoothVideoAdaptationin
andDataMining,SIGKDD,2017. DynamicHTTPStreaming. IntheACMInternationalConferenceonEmerging
[29] PeterHenderson,RiashatIslam,PhilipBachman,JoellePineau,DoinaPrecup, NetworkingExperimentsandTechnologies,CoNEXT,2012.
andDavidMeger.DeepReinforcementLearningthatMatters.InProceedingsof [52] GuillaumeUrvoy-Keller. OntheStationarityofTCPBulkDataTransfers. In
theAssociationforAdvancementofArtificialIntelligence,AAAI,2018. ProceedingsofthePassiveandActiveMeasurementConference,PAM,2005.
57

Oboe SIGCOMM’18,August20–25,2018,Budapest,Hungary
[53] JeroenvanderHooft,StefanoPetrangeli,MaximClaeys,JeroenFamaey,and
FilipDeTurck.ALearning-basedAlgorithmforImprovedBandwidth-awareness
| ofAdaptiveStreamingClients. |     | InSymposiumonIntegratedNetworkManage- |     |     |
| --------------------------- | --- | ------------------------------------- | --- | --- |
ment,IM,2015.
| [54] LiWeiandEamonnKeogh. |     | Semi-supervisedTimeSeriesClassification. |     | In  |
| ------------------------- | --- | ---------------------------------------- | --- | --- |
ProceedingsoftheACMInternationalConferenceonKnowledgeDiscoveryand
DataMining,SIGKDD,2006.
| [55] RonaldJWilliamsandJingPeng. |     | FunctionOptimizationusingConnectionist |     |     |
| -------------------------------- | --- | -------------------------------------- | --- | --- |
ReinforcementLearningAlgorithms.ConnectionScience,3(3):241–268,1991.
| [56] KeithWinsteinandHariBalakrishnan. |                                                  | TCPExMachina:Computer-generated |     |     |
| -------------------------------------- | ------------------------------------------------ | ------------------------------- | --- | --- |
| CongestionControl.                     | InProceedingsoftheACMConferenceonSpecialInterest |                                 |     |     |
GrouponDataCommunication,SIGCOMM,2013.
| [57] XuanXiangandKevinMurphy. |     | ModellingChangingDependencyStructurein      |     |     |
| ----------------------------- | --- | ------------------------------------------- | --- | --- |
| MultivariateTimeSeries.       |     | InProceedingsoftheInternationalConferenceon |     |     |
DataMining,ICML,2007.
| [58] KenjiYamanishiandJun-ichiTakeuchi.                  |     | AUnifyingFrameworkforDetecting |     |            |
| -------------------------------------------------------- | --- | ------------------------------ | --- | ---------- |
| OutliersandChangePointsfromNon-stationaryTimeSeriesData. |     |                                |     | InProceed- |
ingsoftheACMInternationalConferenceonKnowledgeDiscoveryandData
Mining,SIGKDD,2002.
| [59] Xiaoqi                                                | Yin, Abhishek Jindal, | Vyas Sekar, | and Bruno Sinopoli. | A Control- |
| ---------------------------------------------------------- | --------------------- | ----------- | ------------------- | ---------- |
| TheoreticApproachforDynamicAdaptiveVideoStreamingoverHTTP. |                       |             |                     | In         |
ProceedingsoftheACMConferenceonSpecialInterestGrouponDataCom-
munication,SIGCOMM,2015.
| [60] YinZhangandNickDuffield. |     | OntheConstancyofInternetPathProperties. |     | In  |
| ----------------------------- | --- | --------------------------------------- | --- | --- |
ProceedingsoftheACMSIGCOMMWorkshoponInternetMeasurement,2001.
58