Plume: A Framework for High Performance Deep RL
Network Controllers via Prioritized Trace Sampling
SAGARPATEL1,JUNYANGZHANG1,SANGEETHAABDUJYOTHI1,2,andNINANARODYTSKA2,
1UniversityofCaliforia,Irvine,USAand 2VMwareResearch,USA
DeepReinforcementLearning(DRL)hasshownpromiseinvariousnetworkingenvironments.However,
theseenvironmentspresentseveralfundamentalchallengesforstandardDRLtechniques.Theyaredifficultto
exploreandexhibithighlevelsofnoiseanduncertainty.Althoughthesechallengescomplicatethetraining
process,wefindthatinpracticewecansubstantiallymitigatetheireffectsandevenachievestate-of-the-art
real-worldperformancebyaddressingafactorthathasbeenpreviouslyoverlooked:theskewedinputtrace
distributioninDRLtrainingdatasets.
Weintroduceageneralizedframework,Plume,toautomaticallyidentifyandbalancetheskewusinga
three-stageprocess.First,weidentifythecriticalfeaturesthatdeterminethebehaviorofthetraces.Second,we
classifythetracesintoclusters.Finally,weprioritizethesalientclusterstoimprovetheoverallperformance
ofthecontroller.PlumeseamlesslyworksacrossDRLalgorithms,withoutrequiringanychangestotheDRL
workflow.WeevaluatedPlumeonthreenetworkingenvironments,includingAdaptiveBitrateStreaming,
CongestionControl,andLoadBalancing.Plumeofferssuperiorperformanceinbothsimulationandreal-world
settings,acrossdifferentcontrollersandDRLalgorithms.Forexample,ournovelABRcontroller,Gelatotrained
withPlumeconsistentlyoutperformspriorstate-of-the-artcontrollersonthelivestreamingplatformPuffer
foroverayear.Itisthefirstcontrollerontheplatformtodeliverstatisticallysignificantimprovementsin
bothvideoqualityandstalling,decreasingstallsbyasmuchas75%.
1 INTRODUCTION
Controlinreal-worldnetworksisahard-to-tackleproblem.Today,learningsolutionsholdpromise
inabroadrangeofnetworkenvironments.DeepReinforcementLearning(DRL)controllershave
shownencouragingresultsincongestioncontrol(CC)[5,22],AdaptiveBitrateStreaming(ABR)[31,
33],loadbalancing(LB)[35],clusterscheduling[34],networktrafficoptimization[11]andnetwork
planning[61],tonameafew.
Insystemsandnetworkingenvironments,unliketraditionalDRLenvironmentssuchasgaming
orrobotics,thereexistsanunpredictableunderlyinginputprocess.Forinstance,incongestion
control,thebehaviorofothertrafficsharingthenetworkpathdeterminesifcongestionoccurs.
Theseprocessesarereferredtoas“inputs”[35].Duringtraining,theyarereplayedusingadataset
ofinputtraces,orsystemlogs.Suchinput-drivenDRLenvironmentshaveseveralcharacteristics
that make DRL training difficult. First, input-driven RL environments require more extensive
explorationduringtraining[32].Second,thedependenceoftheenvironmentonexternalinputs
such as Internet traffic introduces high levels of uncertainty and noise [35]. These challenges
together make exploration and learning in network environments highly non-trivial, causing
severalpriorwork[31,32,58]toconcludethataddressingthemwasessentialforhighperformance
intherealworld.
Ouranalysisdiscoversakeyfactorexacerbatingtheimpactofthesechallengesinpractice:the
skeweddistributionofinputtracesintrainingdatasets.Skewleadstolimitedexplorationofrare
ortail-endtraces,introducessignificanterrorsinfeaturelearningforthesetail-endtraces,and
resultsinnoisylearningbyintroducingupdatesconsistingofanarrowsetoftraces.Moreover,
theperformanceofthesetail-endtracesisoftenlessthanoptimal,incontrasttothe“common”
traceswhichareheavilyoptimized.Thus,enhancingtail-endtraceperformancebecomescritical
forimprovingtheoverallcontrollerperformance[23].Unfortunately,suchskewisprevalentin
Authors’address:SagarPatel1;JunyangZhang1;SangeethaAbduJyothi1,2;NinaNarodytska2,
1UniversityofCaliforia,Irvine,Irvine,CA,USA and2VMwareResearch,PaloAlto,CA,USA,sagar.patel@uci.edu.
3202
voN
21
]GL.sc[
2v30421.2032:viXra

2 SagarPatel,JunyangZhang,SangeethaAbduJyothi,andNinaNarodytska
input-drivenenvironments.Forexample,duringaneight-monthdatacollectionperiod,thevideo
streamingplatformPuffer[58]recordedthatlow-bandwidthinputtracesmadeuplessthan20%
ofthetotaltraces,withonly4%ofthesetraceshavinganystalls.Therefore,addressingskewis
essentialfor(a)avoidingamplifyinginherentchallengesinlearning,and(b)improvingtheoverall
performanceofthecontrolleracrossboth“common”andtail-endinputtraces.
Whiletechniquesforaddressingdataskewareprevalentinvariouscontexts[14,15,27,29,40,
46,60],standardsupervisedlearningsolutionssuchasoversamplingorundersamplingspecific
labeledclassesdonotapplyinthecaseofreinforcementlearning,wherethecontrollerlearnsusing
states,actionsandrewards.ThefewsolutionsdesignedspecificallyforDRLareinadequatefor
networkcontrollersbecausetheyarerestrictedtostate-levelprioritizationandfailtocapturethe
trace-centricnatureofnetworkingenvironments(§3.2).Thus,toeffectivelyaddressthisskew,we
introduceanovelapproachdirectlytargetingtheinputtracesinnetworkingenvironments.
Inputtraces,whichrepresentlogsoftime-dependentcomplexprocesses,lackaconventional
mechanismtoidentifyandbalancetheskewwith.Thesetraceshavenofeaturesorlabelsand
donotdirectlycontributetoalossfunction.Tosystematicallytackleskewandimproveoverall
controllerperformance,amechanismtoidentifyandbalancetheskewininput-drivenenvironments
isneeded.Todoso,inthiswork,weintroduceageneralizableframework,Plume.Plumeemploys
anautomatedthree-stageprocess.CriticalFeatureIdentification:Weautomaticallydeterminethe
criticaltracefeaturesthatenableustoidentifythetraces.Clustering: Weemployclusteringto
convertthecriticalfeaturesintosalientidentifiers.Prioritization:Inthisstage,weprioritizethe
clusters,suchastoexposethecontrollertotraceswhereitcanlearnthemostfrom(§4).
UsingAdaptiveBitrateStreaming,CongestionControlandLoadBalancingasrepresentative
networkapplications,weshowthatPlumeoffersconsistentlyhighperformanceacrossawide
rangeofcontrollers—acrossdifferentenvironments,diversetracedistributions,andmultipleDRL
algorithms.WealsointroduceGelato,anovelDRLABRcontrollerthat,whentrainedwithPlume,
offersstate-of-the-artperformanceonthereal-worldlivestreamingplatformPuffer[58].Itisthe
first controller on the platform that offers statistically significant improvements in both video
qualityandstalling.Itoutperformsthepreviousstate-of-the-artcontrollers,CausalSim[8]and
Fugu[58],reducingstallsby75%and78%respectively.
Tofurtheranalyzeprioritizationstrategies,wealsointroduceacontrolledevaluationenviron-
ment,TraceBench.TraceBenchisasimplifiedAdaptiveBitrateenvironmentwithparametrically
generatedtraces.Parameterizedtracegenerationenablesuserstogenerateawiderangeoftesttrace
distributionsinacontrolledandaccuratemanner,whichcanthenserveinthoroughlyevaluating
samplingstrategies.
Insummary,wemakethefollowingcontributions:
• WesystematicallystudyanoverlookedaspectofDRLtraining,skeweddatasets,andfindthat
theycanhaveasurprisinglylargeimpactonperformance.
• WeproposePlumeasageneralizableframeworkforhandlingskeweddatasetsandimproving
theperformanceofinput-drivenDRLcontrollers.
• WedemonstratethesuperiorperformanceandrobustnessofPlumeinCongestionControl,Load
Balancing, and Adaptive Bitrate Selection, across multiple RL algorithms in simulation and
real-worldsettings.
• WeintroduceGelato,anewABRcontroller.Plume-trainedGelato,deployedonthereal-world
Pufferplatform[58]formorethanayear,isthefirstcontrollerthatachievessignficaintimprove-
mentsinbothvideoqualityandstalling,reducingstallingbyasmuchas75%overtheprevious
state-of-the-art.

Plume:AFrameworkforHighPerformanceDeepRLNetworkControllers 3
Fig.1. RLTrainingLoop:ThetrainingloopofDRLalgorithmsintrace-drivenenvironments.
• Wepresentanewbenchmarkingtool,TraceBench,andevaluatetheprioritizationtechniques
acrossawiderangeoftracedistributions;demonstratingthatPlumeisrobustacrossthem.
Wewillopen-sourcethecodeofthePlumelibrary,TraceBench,ourDRLenvironments,andour
state-of-the-artABRcontroller,Gelato.
2 BACKGROUND
Inthissection,wegiveabriefoverviewofreinforcementlearningtrainingandourrepresentative
applications—adaptivevideostreaming,congestioncontrol,andloadbalancing.
2.1 ReinforcementLearningPreliminiaries
InDeepReinforcementlearning(DRL),anagent interactswithanenvironment.Ateachtimestep,
theagentreceivesthecurrentsystemstate𝑠
𝑡
,andtakesanaction𝑎
𝑡
,drawnfromitspolicy,𝜋(𝑎|𝑠 𝑡).
The environment plays the action out and transitions to the next state𝑠 𝑡+1 , giving the agent a
reward𝑟 [6,50,52].
𝑡
Innetworkenvironments,non-deterministicnetworkconditionsaretheprimarysourcesof
noiseanduncertainty.Theseconditionsdeterminetheenvironment’sresponsetothecontroller’s
chosenactions.Forexample,incongestioncontrol,externaltrafficcandictatewhethercongestion
willoccur.
Formally,theseconditionsarecalled“inputs”,andinput-drivenenvironmentsformanInput-
DrivenMarkovDecisionProcess[35],definedbythetuple (𝑆,𝐴,𝑍,𝑃
𝑠
,𝑃
𝑧
,𝑟,𝛾).Here,𝑆 denotes
the set of states,𝐴 represents the set of actions,𝑍 is the set of training input traces, 𝑃 is the
𝑠
statetransitionfunction,𝑃 istheinputtransitionfunction,𝑟 istherewardfunction,and𝛾 isthe
𝑧
discount.
Thestatetransitionfunction𝑃 𝑠(𝑠 𝑡+1|𝑠
𝑡
,𝑎
𝑡
,𝑧 𝑡+1)definestheprobabilitydistributionofthenext
state𝑠 giventhecurrentstate𝑠 ,action𝑎 ,andupcominginputvalue𝑧 .Meanwhile,theinput
𝑡+1 𝑡 𝑡 𝑡+1
transitionfunction𝑃 𝑧(𝑧 𝑡+1|𝑧 𝑡)definestheprobabilityofthenextinputvaluebasedonthecurrent
one,leadingtoaneffectivetransitionfunctiongivenby𝑃 𝑠(𝑠 𝑡+1|𝑠
𝑡
,𝑎
𝑡
,𝑧 𝑡+1)𝑃 𝑧(𝑧 𝑡+1|𝑧 𝑡).
AsdepictedinFigure1,theDRLlearningprocessaimstoguidethepolicy𝜋 towardshigher
cumulative reward through a loop involving two steps: a policy evaluation step and a policy
improvementstep[20].Duringpolicyevaluation,theagentassessesitscurrentpolicy’sperformance
by gathering experience through acting in the environment and leveraging this experience in
functionlearning.Here,itupdatesitsneuralnetworktolearnaformofthevaluefunction𝑣𝜋(𝑠) =
E 𝜋[𝐺|𝑠
0
=𝑠],whichistheexpectedreturn𝐺 startingfromstate𝑠,where𝐺 isthediscountedsum
ofrewards𝐺 =(cid:205)
𝑡
∞
=0
𝛾𝑡𝑟
𝑡
.Subsequently,inthepolicyimprovementphase,theagentmodifiespolicy

4 SagarPatel,JunyangZhang,SangeethaAbduJyothi,andNinaNarodytska
𝜋 tomaximize𝑣𝜋.Throughthisiterativeprocessofestimatingandmaximizingthepolicy’svalue
function,theagentlearnsintheenvironment.
On-policyandOff-policyDRL.DRLalgorithmsarebroadlydividedintotwocategoriesbased
ontheirpolicyevaluationstages.On-policyRLalgorithmsperformpolicyevaluationfromscratch
ineachiteration,usingonlythedatacollectedwiththelatestversionofthepolicyforfunction
learning[52].Thesealgorithmshavefoundwideapplicationinnetworking[22,30,33].Onthe
otherhand,Off-policyRLalgorithmscontinuetousedatafromolderversionsofthepolicyalong
withnewdatatoimprovesampleefficiency.Theymaintainawindowofenvironmenttransitions,
describedbythetuple(𝑠
𝑡
,𝑎
𝑡
,𝑟
𝑡
,𝑠 𝑡+1),inaFIFObufferknownasExperienceReplay[38].Off-policy
algorithmsaresimilarlypopularinnetworking,asusedby[5,57].
2.2 Environments
Inthispaper,weuseadaptivebitratestreaming,congestioncontrol,andloadbalancingasrepre-
sentativenetworkingenvironments.
AdaptiveBitrateStreaming.InHTTPvideostreaming,thevideoisdividedintoshortchunks
andencoded,inadvance,atmultiplediscretebitrates.Duringstreaming,theABRalgorithmis
responsibleforsequentiallyselectingthebitrateofeachchunktomaximizetheviewer’sQualityof
Experience(QoE).Whilestreaming,theclientalsohasabuffertostorechunksyettobeplayed.
Typically,theQoEismeasuredwithanumericalfunctionthatawardshigherquality,andpenalizes
bothqualityfluctuationsandrebuffering.Thequalityofachunkmaybedenotedbyitsbitrateor
bymorecomplexmeasuressuchasStructuralSimilarityIndexMeasure(SSIM)[54].
CongestionControl.CongestionControl(CC)algorithmsareresponsiblefordeterminingthe
mostsuitabletransmissionratefordatatransferoverasharednetwork.Basedonnetworksignals
suchasround-triptimebetweenthesenderandreceiverandthelossrateofpackets,aCCalgorithm
estimatessendingratethatmaximizesthroughputandminimizeslossanddelay.
LoadBalancing.ALoadBalancing(LB)algorithminadistributedclusterdecideswhichserverto
serveanewjobat,suchastominimizethejob’stotalprocessingtime.Whenajobarrives,theLB
algorithmdoesnotknowhowbusyeachserverisorhowlongeachserverwilltaketoprocessthe
job.Tomakeagooddecision,itusesdatasuchasthetimebetweenjobarrivals,thedurationof
pastjobs,andthenumberofjobsalreadywaitingateachserver.
3 MOTIVATION
Inthissection,wediscussthechallengesassociatedwithtrainingDRLcontrollersandhowthey
areexacerbatedbyskewedtrainingdatasets.Then,wegiveabriefoverviewofcurrenttechniques
usedtohandleskewandmotivatetheneedforprioritizedtracesampling.
3.1 ChallengeswithDRLTraining
Input-drivenDRLtrainingenvironmentsusedinnetworkingsettingssufferfromseveraloverarch-
ingchallenges.
Challenge1:Needle-in-the-haystackexploration.Ininput-drivenenvironments,themajority
ofthestate-actionspacepresentslittledifferenceinrewardfeedback[32].Inthisscenario,standard
explorationtechniques,whichselectarandomactionwith𝜖 probabilityandfollowgreedyactions
otherwise,havealowchanceoffindingasuccessfulpolicy.Thecomplexityisfurtherexacerbated
bytheimbalanceinthetrainingdatasets,particularlytheunder-representationofrareortail-end
traces.Suchtracesareinfrequentlyencounteredbythecontroller,therebyfurtherlimitingthe

Plume:AFrameworkforHighPerformanceDeepRLNetworkControllers 5
Fig.2. PufferInputTracedistribution:DistributionofeffectivethroughputofPuffertracescollected
duringthetwo-monthperiod,Apr’21-May’21.Lessthan6.5%oftraceshaveaverageeffectivethroughput
belowtheaveragebitrateofthehighestqualityvideo.EachPufferstreamisatrace.
opportunityforthecontrollertodiscoversuccessfulstrategiesforthem.However,performancein
thesetail-endtracescanbecrucialforhigheroverallperformanceofthecontroller[23].
Challenge2:NoiseandUncertainty.Thenetworkconditions,orinputs,determinethebehavior
oftheenvironmentandconstitutethemainsourceofuncertainty.Forinstance,whenanAdaptive
Bitratecontrollerchoosesabitrate,itoperateswithoutknowledgeoftheclient’slinkbandwidth.
Thisunobservedfactordirectlyimpactstheamountoftimetheclientwillwaitforadatachunk.
Suchvariabilityintroducesnoiseintothelearningprocess,creatingasituationwhereidentical
statescanyieldwidelydifferentoutcomesbasedonthenetworkconditions[35].Thisvariabilityor
noiseisparticularlyamplifiedwhenthedistributionofnetworktracesisskewed.Inthesecases,
asingletrainingiterationmayinadequatelyrepresentthefullspectrumofinputtraces,thereby
leadingtodivergentornoisyupdates.
OtherChallengeswithskew.Skewinthedistributionofinputtracespresentschallengesduring
thefunctionlearningphaseofDRLtraining(Fig.1).Sincestatesaredependentontheseinput
traces, a skewed input distribution leads to a skewed state distribution. This imbalance in the
state distribution degrades the performance of the neural network and makes it vulnerable to
overfitting[24,59].
3.2 TowardsPrioritizingTraceSampling
Next, we discuss commonly used ML techniques for handling skew and establish the need for
prioritizedtracesamplingininput-drivenenvironments.
PrioritizedExperienceReplay(PER).Off-policyDRLalgorithmsuseabuffertostorepaststate
transitionsandapplyPrioritizedExperienceReplay(PER)[46]tosamplethemduringfunction
learning. PER employs prioritization, also known as importance sampling, to prioritize state
transitionsbasedontheirTemporalDifferenceerror.Thekeyideaistofocusontransitionswith
highererror,improvingthecontroller’spredictionswheremostneededratherthanonthemost
commontransitions.
WhilePERiseffectiveintraditionalDRLsettings[19,20],itislimitedinaddressingthechallenges
presentedbyskewininput-drivenenvironments.ThereasonisthatwhilePERaddressesthestate
skewinthefunctionlearningphase,theskewininputtracesadditionallyaffectstheactingphase
ofthetrainingloop(Fig.1).Thecontrollerhaslimitedopportunitytoactintail-endtraces.Without
modifyingwhichtracesareselectedduringactingphase,PERcannotincreasethefrequencyof
explorationintail-endtracesorensureacomprehensiveevaluationacrosstheentireinputtrace

6 SagarPatel,JunyangZhang,SangeethaAbduJyothi,andNinaNarodytska
Fig.3. ComparingPrioritizationTechniques:Performanceofsamplingtransitions(PERenabled/disabled)
comparedwithsamplingtraces(Randomvs.2-ClassEqualWeightedTraceSelection)onaDQN-variantof
CannoliABRcontrollertrainedusingtheoff-policyalgorithm,Ape-XDQN[20].2-ClassEqualWeightedTrace
Selectionofferssuperiorcontrollerperformanceandtrainingefficiency,whilePERdoesnot.95%confidence
intervalshownaserrorbands.
distribution.Consequently,theimportancesamplingPERusesisnotsufficienttohandletheskew
ofinputtracesinthedataset.
Prioritized Trace Sampling. We reexamine the DRL workflow and identify a more suitable
locationforprioritization.Weputforwardasimpletrainingparadigmininput-drivenenvironments:
prioritizingtracesamplingduringtheactingstep.Withthis,wecanachievehighstate-actionspace
explorationandrepresentativeevaluationonallkindsoftraces.
To test our hypothesis, we experiment by enabling prioritization at two points in the DRL
workflow:samplingtransitionsintheexperiencebufferatthefunctionlearningstep(PERenabled
vs. disabled) and sampling input traces in the acting step (Random sampling vs. 2-Class Equal
Weighted).2-ClassEqualWeightedisasimpleinputtraceprioritizationschemethatdividesthe
tracesfromthePufferPlatformintotwoclasses,thosewithmeanthroughputhigher/lowerthan
thehighestqualitybitrate,0.98Mbps(Figure2),andequallysamplesbothclasses.Weevaluate
theimpactofeachtechniqueonaDQNvariationofGelatocontrollerforABRtrainedusingthe
state-of-the-artalgorithmApe-XDQN[20](trainingsettingsdetailedin§5and§6.2).
In Figure 3, we observe that the simple 2-Class Equal Weighted gives the highest controller
performanceandtrainingstability.Byprioritizingthetail-endslowthroughputtraces,weachieved
highperformanceinbothallandslownetworktraceswithoutcompromisinganything.Enabling
PERdoesnotsignificantlyimprovecontrollerperformance.Eventhoughthereplaybuffercan
store2milliontransitions(over5000inputtraces),thecontrollerperformancefallsshortofthe
naivetraceprioritizationscheme.Thishighlightsthattheskewinthetracedistributioncannotbe
easilyovercomeatthefunctionlearningstep.
4 DESIGN
TowardimprovingtheperformanceofDRLtrainingbybalancingskew,weputforwardtheidea
thattraceselectionistheaptestlocationforprioritization.
Inordertobalancetheskewduringtraceselection,wetakeadvantageofakeyobservation:
inputtracesinherentlycorrespondtousersorworkloads,withgroupsofthemsharingsimilar
characteristics. To ensure a balanced representation of the underlying users, the dataset must

Plume:AFrameworkforHighPerformanceDeepRLNetworkControllers 7
Fig.4. PlumeSystemDiagram:ThePlumeWorkflowinvolvesthreekeystages:(1)CriticalFeatureIden-
tification,wherewecharacterizethetracesandtheirskew,(2)Clustering,wherewetrytosimplifythe
prioritizationproblembygroupingtraces,(3)Prioritization,whereweobservetheperformanceoftheagent
andattempttoprioritizeimportanttraceclusters.
containaroughlyuniformnumberofinputtracesacrossthem.Wedefineinputtracestohavea
setofuserattributesΦ= [𝜙
1
,𝜙
2
,...] givenbythefunctionΦ=𝑋(𝑡𝑟𝑎𝑐𝑒),where𝑋 dependsonthe
domain.Thesefeaturesidentifysimilaritiesbetweenusertraces,andplayakeyroleinobtaininga
balancedrepresentation.
Plumeisasystematicframeworktoautomaticallybalancethisskewininputtraces.Plumeallows
theagenttohavebalancedexplorationandstablelearningupdates.Figure4givesanoverviewof
thePlumeworkflow.PlumeisimplementedintheTraceSelectionmodulewhichisresponsible
forsupplyingtracestothesimulationenvironment.ThismodulesitsoutsideoftheDRLtraining
loopandisqueriedbytheenvironmenttogettracestoreplay.Plumehasthreekeystages:critical
featureidentification,clustering,andprioritization.
Inthecriticalfeatureidentificationstage(§4.1),Plumeidentifiestheattributesoftheinputtraces.
Intheclusteringstage(§4.2),itsimplifiestheprioritizationproblembyclusteringtheattributes.
Finally,inthePrioritization(§4.3)stage,Plumeprioritizesthetracestobalanceinputtracesusing
oneoftwotechniques:staticordynamic.
4.1 CriticalFeatureIdentification
Inputtraces,whicharetime-dependentseriesofvaluesthatdefinecomplexexternalconditions,can
beincrediblydifficulttocharacterizeandprioritizedirectly.Hence,thefirststeptowardsautomated
prioritizationoftracesisidentifyingtheattributesΦusingcriticalfeatureidentification.
Toextractallfeaturesassociatedwiththetimeseriestracedata,werelyonthepopularfeature
extractiontoolforthetimeseriesdata,tsfresh[12].Weextractalargesetoffeatures [𝜙 1 ,𝜙 2 ,...𝜙 𝑛]
broadlyapplicabletoallinput-drivenDRLenvironments.However,becausethislargesetoffeatures
maynotberelevanttoeveryapplication,weintroduceanautomatedthree-stepprocesstonarrow
down to the critical ones, inspired by the idea of recursive feature elimination in supervised
learning[3].
First,westartwiththelargesetoffeaturesandapplyclusteringtocreateafixedsmallnumberof
clusters.Thisisdenotedby𝑐 =𝐶([𝜙
1
,𝜙
2
,...𝜙 𝑛]),where𝑐istheclusterlabels,and𝐶istheclustering
function.

8 SagarPatel,JunyangZhang,SangeethaAbduJyothi,andNinaNarodytska
Second,weobtainthefeaturesmostrelevantinproducingthismapping.Todoso,weusethe
clusterlabels𝑐 andtraindecisiontreesbasedonthefeatures [𝜙
1
,𝜙
2
,...𝜙 𝑛].Withthistraining,we
cancomputetheinformationgain𝐼𝐺(𝑐,𝜙 𝑖) =𝐻(𝑐)−𝐻(𝑐|𝜙 𝑖) foreachfeature𝜙 𝑖 .Here,𝐻 isthe
Shannonentropyoftheclusterlabels,whichisameasureoftheaveragelevelof“uncertainty”.
Third,weeliminatefeatureswiththelowest𝐼𝐺 values.Wecontinuethiscycleofclustering,
classification, and feature elimination until we are left with only the features that have high
informationgain.Asweeliminatelessusefulfeatures,weincreasethenumberofclusterstoensure
thatthefinalfeaturesetissufficientlyexpressive.
Notethattheclusteringatthisstageissolelyforfeatureselectionandhasnoimpactonthemain
clusteringphase(§4.2).
4.2 Clustering
Thesecondstageinvolvesclusteringtracesusingthecriticalfeaturesidentifiedintheprevious
stage.Inthisstage,weattempttoreducethecomplexityofbalancingtheskewbyobtainingtheir
salientclusters.
Todetectskewinthedataset,wecanlookattheattributesΦofinputtraces.However,balancing
theskewbasedsolelyontheseattributesprovestobeacomplextask.Thisdifficultyarisesbecause
theattributes,representedas [𝜙
1
,𝜙
2
,...,𝜙 𝑛],arecontinuousrandomvariablesthatmaynotbe
independent.Inotherwords,modifyingtheskewofoneattributecouldnegativelyaffecttheskew
ofanother.Toaddressthisissue,weclusterthetracestoobtainasingledistributiontobalance.
Weachievethisusingaclusteringalgorithm𝐶 toobtainthelabels𝑐 sothatthemappingagain
becomes𝑐 =𝐶(Φ).Bydoingso,wecreatearankingfunctionthatallowsustoinsteadprioritizea
categoricaldistributionofinputtraces,wheretheclusterlabelsactasthecategories.Werepresent
thisdistributionas𝑦,where𝑦 isacategory,orsalienttraceclusterwithinit.
𝑖
Toclusterthetraces,weemployGaussianMixtureModels(GMM)withKmeans++initializa-
tion[42].GaussianMixtureModelsuseageneralizedExpectationMaximizationalgorithm[1]and
caneffectivelydealwiththelargevariationsfoundininputdata.Thus,GMMsareagoodfitforour
real-worldinputtracedatasets.However,GMMscanoftenconvergetolocaloptimaandrequireus
toknowthenumberofclustersapriori.Hence,toproduceaneffectiveclusteringautomatically,
weperformatwo-stagesearchforrandominitializationsusedinGMMsandthenumberofclus-
ters.First,fordifferentclustercounts,weevaluatetheGMM’slog-likelihoodscoreforthetrace
featuresacrossarangeofrandominitializationsandidentifytheinitializationthatmaximizesthe
log-likelihoodscoreforeachclustercount.Second,wedeterminetheoptimalnumberofclusters
fromtheoutputofthepreviousstagebasedonthehighestnormalizedSilhouettescore[4].
4.3 Prioritization
Withcriticalfeatureidentificationandclusteringstagescomplete,wehaveacategoricaldistribution
ofinputtraces𝑦thatwecanbalancebyprioritization.
Sofar,wehavediscussedbalancingthedistribution𝑦.Whilethiscanbedoneinanumberof
ways,toensurethatthebalancingleadstomeaningfulperformanceimprovements,weintroducea
targetfunctiontobalancethedistributionaround:“reward-to-go”.Reward-to-gorepresentsthe
additionalrewardsthatacontrollercanstillachieve.ThiscanbeformallydefinedbyEquation1:
Δ𝐺 𝑦𝑖 =E 𝑦𝑖 [𝐺𝜋∗ −𝐺𝜋𝜃 ] (1)
In this equation,𝑦 𝑖 is a category (§ 4.2) in the input trace distribution𝑦,𝐺 = (cid:205) 𝑡 ∞ =0 𝛾𝑡𝑟 𝑡 is the
discountedreturnofthetraceasdescribedinSection2.1,𝐺𝜋∗ isthereturnundertheoptimalpolicy
𝜋∗,and𝐺𝜋𝜃 isthereturnunderthecurrentpolicy.Weaimtobalancetheinputtracedistribution
basedonhowsuboptimallythecurrentpolicyperforms,ensuringauniformgapacrossalltraces.

Plume:AFrameworkforHighPerformanceDeepRLNetworkControllers 9
In other words, we seek to ensure that target function Δ𝐺 = Δ𝐺 for all categories𝑦 and
|     |     |     |     | 𝑦𝑖  | 𝑦𝑗 𝑖 |
| --- | --- | --- | --- | --- | ---- |
𝑦 . However, calculating reward-to-go is often not possible in real-world situations because it
𝑗
dependsonvariablessuchasthecontroller’strainingparametersandstatefeatures,andcanrequire
solvinganNPhardproblem[36].Inthiswork,weintroducetwostrategiestoapproximatethis
prioritization:StaticandDynamic.
StaticPrioritization.Inthisapproach,wetackleskewbystaticallybalancingthedistributionof
inputtraces.Specifically,weadjustthesamplingweightstobetheinverseofthedistribution𝑦,as
expressedinEquation2:
1
|     |     | 𝑊   | =   |     | (2) |
| --- | --- | --- | --- | --- | --- |
|     |     | 𝑦𝑖  | 𝑓(𝑦 |     |     |
𝑖)
Here,𝑊 signifies the prioritization weight for category𝑦 , and 𝑓(𝑦 𝑖) is the original probabil-
𝑦𝑖 𝑖
itydensityfunctionforthecategoricaldistribution𝑦.Whenwesampleaccordingtothesepri-
oritization weights, we modify the effective probability density function, which now becomes
𝑊 𝑓 ( 𝑦 𝑖)
𝑓′(𝑦 𝑖) = 𝑦 𝑖 .
(cid:205) 𝑊 𝑦 𝑓 (𝑦𝑘)
𝑦𝑘 ∈𝑦 𝑘
WhilethereexistsnoanalyticalwaytocomputeΔ𝐺 𝑦𝑖 ,insomecases,wecanshowthatstatic
prioritizationeffectivelybalancestheskew.First,considerthatunderrandomtracesampling,the
imbalancecanbearbitrarilylarge:
Proposition4.1. Let𝐿beaconstantand𝑦beacategoricaldistributionofinputtraces.Suppose
|     |     | Δ𝐺  | 𝑓(𝑦    |     |     |
| --- | --- | --- | ------ | --- | --- |
|     |     | 𝑦𝑖  | 𝑗)     |     |     |
|     |     |     | ≈      | ,   |     |
|     |     | Δ𝐺  | 𝑓(𝑦 𝑖) |     |     |
𝑦𝑗
thenthereexistsadistributionoftraces𝑦suchthat
|     |     | Δ𝐺  | 𝑦𝑖  |     |     |
| --- | --- | --- | --- | --- | --- |
≥𝐿.
|     |     | Δ𝐺  | 𝑦𝑗  |     |     |
| --- | --- | --- | --- | --- | --- |
Proof. Consideradistributionwithtwocategorieswhere
|          | 1   |         |           |      | 𝐿   |
| -------- | --- | ------- | --------- | ---- | --- |
| 𝑓(𝑦 1) = |     | and 𝑓(𝑦 | 2) =1−𝑓(𝑦 | 1) = | .   |
|          | 1+𝐿 |         |           |      | 𝐿+1 |
Fromtheabove,itfollowsthat
|     |     | Δ𝐺  | 𝑦2  |     |     |
| --- | --- | --- | --- | --- | --- |
≈𝐿.
|     |     | Δ𝐺  | 𝑦1  |     |     |
| --- | --- | --- | --- | --- | --- |
□
However,usingstaticprioritization,thisimbalancenolongerexists:
Proposition4.2. Let𝑦′ denotethere-weightedcategoricaldistributionofinputtraces.Suppose
|     |     | Δ𝐺 ′ | 𝑓′(𝑦 𝑗) |     |     |
| --- | --- | ---- | ------- | --- | --- |
𝑦 𝑖
|     |     |      | ≈       | ,   |     |
| --- | --- | ---- | ------- | --- | --- |
|     |     | Δ𝐺 ′ | 𝑓′(𝑦 𝑖) |     |     |
𝑦 𝑗
then
|     |     | Δ𝐺′ | ≈Δ𝐺′ | .   |     |
| --- | --- | --- | ---- | --- | --- |
|     |     | 𝑦𝑖  | 𝑦𝑗   |     |     |
Proof. Fromthegivencondition,wehave
| Δ𝐺 ′ | 𝑓′(𝑦    | 𝑊 𝑓(𝑦 | 𝑗) (cid:205) | 𝑊 𝑓(𝑦   | 𝑘)  |
| ---- | ------- | ----- | ------------ | ------- | --- |
| 𝑦    | 𝑗)      | 𝑦𝑗    |              | 𝑦𝑘∈𝑦 𝑦𝑘 |     |
| 𝑖 ≈  |         | =     | ·            |         | =1. |
| Δ𝐺 ′ | 𝑓′(𝑦 𝑖) | 𝑊 𝑓(𝑦 | 𝑖) (cid:205) | 𝑊 𝑓(𝑦   | 𝑘)  |
| 𝑦    |         | 𝑦𝑖    |              | 𝑦𝑘∈𝑦 𝑦𝑘 |     |
𝑗
□

10 SagarPatel,JunyangZhang,SangeethaAbduJyothi,andNinaNarodytska
Giventhesepropositions,itisevidentthatunderstaticprioritization,irrespectiveoftheinitial
inputtracedistribution,therelativereward-to-goratio Δ𝐺′𝑦𝑖 isclosetoone,whilethisratiocan
Δ𝐺′𝑦𝑗
takearbitrarilylargevaluesunderrandomtracesampling.Forbothpropositions,anunderlying
assumptionisthattheratio
Δ𝐺𝑦𝑖
isapproximatelyequaltotheinverseoftheratioofprobability
Δ𝐺𝑦𝑗
densities for the relevant categories. This assumption mirrors a real scenario: as the sampling
frequencyofacategoryincreases,thecontrolleralsobecomesbetterathandlingtracesfromthat
category.Consequently,thereward-to-gogapdecreaseswithincreasingsamplingprobabilityfor
thecategory.
DynamicPrioritization.Indynamicprioritization,wecomputeanapproximationofreward-
to-gothatadaptsasthetrainingprogresses.Reward-to-goofacategorycanvaryasthetraining
progresses,andhence,theextentofprioritizationofacategorytoachievehighperformancecan
differacrosscategoriesduringtraining.
Δ𝐺 𝑦𝑖 =E 𝑦𝑖 [𝐺𝜋∗ −𝐺𝜋𝜃 ]
Δ𝐺 𝑦𝑖 ≈E 𝑦𝑖 [𝐺ˆ (Φ)−𝐺𝜋𝜃 ] //Approximateunknownpolicy (3)
Δ𝐺 𝑦𝑖 ≈E 𝑦𝑖 [𝐺ˆ (Φ)−𝐺𝜋𝜃 ]−E 𝑦𝑖 [𝐺𝜋𝜃 ] //Compensatebiasin𝐺ˆ (Φ)
Astheoptimalreturncannotbecalculated,wereplacethereturn𝐺𝜋∗ withtheexpectedreturn
of the trace computed based on the corpus of seen traces,𝐺ˆ (Φ). Note that𝐺ˆ (Φ) is a function
approximatorthatistrainedcontinuously,inparallelwiththecontroller.Inabroadsense,thisallows
ustomeasuretheimprovementthecontrollercanstillachieveonagiventrace.Nonetheless,this
approximationisvulnerabletobias,especiallyininputtraceswherethecontroller’sperformanceis
poor.Insuchpoorconditions,theestimatemaybecomeoverlypessimisticandmightnotaccurately
capturethereward-to-go.Toaddressthisconcern,weintroducethesecondterm,−E
𝑦𝑖
[𝐺𝜋𝜃 ],which
givesprioritytotracesthathavelowreturns.
ThedynamicweightsareproportionaltothenormalizedsumofcomponentsofΔ𝐺 (Eq.3).
𝑦𝑖
NotethatourprioritizationstageisoutsidetheDRLalgorithm’strainingloopintheTraceSelection
module(Fig.4).
5 GELATO
WepresentanewcontrollerarchitectureforABR,Gelato.OurdesignisinspiredbyPensieve[33]but
withanumberofcrucialchanges.UnlikeotherDRLenvironments,whichhavesimplercontrollers,
ABRcanbenefitfromanewarchitecturetoimproveefficiencyandtrainingperformance.Wewill
demonstrateinSection6thatbycombiningGelatoandPlumeframeworkweobtainastate-of-the-
artcontrollerthatsurpassesallexistingABRcontrollersinbothreal-worldandsimulatedscenarios.
Foranoverview,seeFigure5.
Rewards.WeuseSSIMastheoptimizationgoalwiththerewardcoefficientsusedinFugu[58]
(+SSIM,−stalls,−ΔSSIM).WeusethevideochunksizesandSSIMvaluesfromtheloggeddata
publicly released by the Puffer platform. We also normalize rewards with the transformation
𝑟 :𝑠𝑖𝑔𝑛(𝑟)( √︁ |𝑟|+1−1)+𝜖𝑟 andclipping,where𝜖is10−2.Thetransformationhasbeenempirically
showntobetterhandlerewardswithlargescalesandvaryingdensity[43].Itpreventsextremely
largepositiveornegativevaluesofreward(e.gforanunusuallyhighSSIM,alongstall,etc)from
dramaticallyaffectingthecontroller.
Features.Weuserichapplication-levelfeatures,keepingahistoryoftheclientbufferandpast
rewards.Weadditionallyuseahistoryofstallsoveralonger30chunkhorizon,aggregatedusinga

Plume:AFrameworkforHighPerformanceDeepRLNetworkControllers 11
Fig.5. ArchitectureofGelato:Gelatotakesasinputcomplexfeaturesofthevideostream.
sumover3chunks.Thishistoryallowsthecontrollertogetadeepunderstandingoftheclient’s
qualityofexperienceandautomaticallycorrectitselfwhenthenetworkconditionsbecomepoor.
NotethatGelatodoesnotuselow-levelTCPstatisticsasFugudoes.However,similartoFugu,it
usestransmittimeinsteadofthroughput,andthevaluesofchunksizesandSSIMsatallencoded
bitratesoverthenextfivechunks.ThesevaluesareoftenavailabletoABRcontrollersbecausethe
chunkstobesentareencodedmorethan10secondsbeforebeingsent.
NeuralArchitecture.WedesignthedeepneuralnetworkofGelatotobeefficient.Wereducethe
totalnumberofparametersbyusinganadditionalconvolutionallayertodownsampletheinputs,
therebyreducingtheinputsizetotheFullyConnected(FC)layer.Gelato’sdeeperneuralnetwork
allowsformoreexpressivefeatureextractionwhilereducingthenumberoftrainableparameters
andMult-Addoperationsby76%and68%respectivelycomparedtoPensieve.
Fortheoff-policyDQNvariantofGelato(usedforcomparisonwithPERinFigure3),weusethe
samearchitecture,swappingthepolicyandvaluenetworkswithasingleduelingQ-network[55].
Fordetails,seeAppendixC.
6 EXPERIMENTS
In this section, we present the findings of testing the impact of Plume across multiple agent
architecturesandnetworkingenvironments,andacrosssimulationandreal-worldtrials.
6.1 Implementation
We now turn to detail our implementation of all the experiments performed in this paper. We
implementPlumeasaPythonlibrarycompatiblewithallmajorDRLframeworks.

12 SagarPatel,JunyangZhang,SangeethaAbduJyothi,andNinaNarodytska
Training environments and algorithms. We implement the standard ABR environment by
extendingtheParkProjectcode[32]andinterfacingwithPuffertraces[58].Weimplementthe
CCenvironmentbyextendingthesourcecodeprovidedbyAurora[22].WeimplementtheLoad
BalancingenvironmentusingtheopensourceParkProjectcode[32].WeusethestandardOpenAI
Gym[10]interfaceandtheRLlibrariesStable-Baselines3[44]andRLlib[28].
Plume. We implement Plume completely outside of the DRL workflow in the Trace Selection
Module.Toimplementthecriticalfeatureidentificationstage,weusetsfresh[12]foritsfeature-
extraction tools and Scikit-Learn [42] for its decision tree and clustering implementation. To
implementtheclusteringstage,weagainuseScikit-LearnforitsGaussianMixtureModeland
Silhouettescoringimplementation.Toimplementtheprioritizationstage,weemployNumpy[17]
andPyTorch[41].
AstraightforwardimplementationofPlumecandirectlyinterferewiththevariousdistributed
training paradigms used in many DRL algorithms [20, 37]. To this degree, we implement our
prioritizationstrategyusingthedistributedsharedobject-storeparadigminRay[39].Thisallows
ustosharethesamplingweightsacrossdistributedRLprocesseswithoutinterferingwithanyDRL
workflows.
Withourimplementation,theoverheadforPlumeisminimal.TheCriticalFeatureIdentification
andclusteringstagesarecompletedoncebeforetraining,withruntimesintheorderofminutes.
InPlume-Dynamic,wetrainaneuralnetworktomaptheattributesΦofaninputtracetothe
return𝐺𝜋𝜃 in that trace parallel to the training. We maintain a short bounded history of the
trace-returnpairsforeachcategoryandusethishistorytocomputethetwocomponentsofour
prioritizationfunction.Tocomputethefirstterminourapproximation,wetaketheground-truth
samplesoftracefeature-returnpairs,measurethemeanabsoluteerroroftheneuralnetworkfor
thesesamples,andaveragethemacrosseachcategory.Tocalculatethecompensationterm,we
takethenegativeofthemeanreturnfoundineachcategory.Wedothisprioritizationprocess
continuously,adjustingtheweightstothecontroller’scurrentneeds.Thisdynamicprioritization
calculationaddsacomputationaloverheadontheorderofmillisecondsperiteration.Thisadded
prioritizationcomputationishandledinparalleltotheDRLtraininganddoesnotslowitdown.
6.2 Settings
Inthissection,wepresentthesettingsusedinourexperiments.Wepresentourresultsasaverages
over4instances(4controllerstrainedusingthesameschemewithdifferentinitialrandomseeds).
ThisisconsistentwiththestandardreportingpracticeintheRLcommunity[20,25,37].Fortesting
onthePufferplatform,weselectthebestofthesefourseedsforbenchmarking.Formoredetails
onthesesettings,seeAppendixCandD.
AdaptiveBitrateStreaming.ForABR,weusethenetworktracesloggedbythePufferplatform
over the two-month period of April 2021 - May 2021. The traces are system logs of the video
streams.Eachtraceisatimeseriesoftuplesoverallchunkssentduringthesessionthatincludes(i)
thechunksizesandSSIMsatvariousbitrates,(ii)thebitratechosenbytheABRalgorithmforthat
chunk,and(iii)thetimetakentotransmitthatchunk.Wecalculatetheeffectivethroughputover
timeusingthisdataanduseitalongsidethechunksizesandSSIMsforsimulation.Weenforcea
minimumtracelengthrequirementof3stream-minutestoreduceI/Ooverhead.Moreover,during
training,werandomlysplitlongtracesintolengthsof500chunksinordertopreventthemfrom
dominatingtraining.Thisresultsinmorethan75,000traces,ofwhichwerandomlyselectabout
55,000,representingover4.25stream-years,forouranalysis.Ofthese,weuse40,000fortraining
andabout15,000fortesting.Weevaluateeverycontrollerusingthesametrainandtestset.

Plume:AFrameworkforHighPerformanceDeepRLNetworkControllers 13
ABRPufferPlatform.WetestGelatowithbothrandomsamplingandPlumeonthelivestreaming
researchplatformPufferfrom01October2022-01October2023.ThePufferplatformstreams
liveTVchannelssuchasABC,NBCorCBSoverthewide-areaInternettomorethan200,000
users[2].Overthistime,weanalyzedtheABRalgorithmsstreamedover58.9stream-yearsofvideo.
WereporttheperformanceasSSIMvs.stallratio,followingtheconventionusedbythePuffer
platform[58].
WecompareGelato-RandomandGelato-Plume-StaticwiththeperformanceoftheBuffer-based
controller BBA [21], the in-situ continuous training controller Fugu’s February version, Fugu-
Feb[58],andCausalSim[8],aversionofBola[51]tunedbytrace-drivencausalsimulation.Wenote
thatonthePufferplatform,Gelato-Randomiscalledbyitscodename“unagi”,Gelato-Plume-Static
iscalled“maguro”.WeadditionallycompareGelatowiththeoriginalversionofFuguoverthe
period07March2022-05October2022inFigure14inAppendixC.
CongestionControl.Forcongestioncontrol,weusethesyntheticnetworktracesemployedby
theDRLCCalgorithmAurora[22].Here,eachtraceisrepresentedby4keysimulationparameters:
throughput,latency,maximumqueuesize,andloss.Fortraining,wesamplethroughputfromthe
range[100,500]packetspersecond,latencyfromtherange[50,300]milliseconds,maximumqueue
sizefromtherange [2,50] packets,andlossratefrom [0,2] percent.Fortesting,webroadenthe
rangesandsamplethroughputfrom [50,1000],latencyfrom [25,500],maximumqueuesizefrom
[2,75],andlossfrom [0,3].Wesamplethroughput,maximumqueuesize,andlossratespaced
evenlyintherangeonageometricprogression,whilesamplinglatencyuniformlyevenly.Wenote
thatwedothissamplingonlyonceandfixitforbothtrainingandtestingforallcontrollers.
LoadBalancing.Inloadbalancing,weusesyntheticjobtracesfromtheParkProject[32].Each
tracerepresentsatimeseriesindicatingthesizeofarrivingjobsovertime.Followingstandard
parameters,theinter-arrivaltimesaresampledfromtheexponentialdistribution𝑒𝑥𝑝(𝜆 = 55),
andthejobsizesaresampledfromtheparetodistribution𝑝𝑎𝑟𝑒𝑡𝑜(𝑥 𝑚 = 1.5,𝛼 = 100).Welimit
thetracelengthto650toensurethatthecontrollerissufficientlypenalizedforpoorscheduling
decisions,andthatthevarianceofreturns𝐺 remainsfinite.Asincongestioncontrol,weperform
thissamplingonceandfixitforbothtrainingandtesting.
6.3 Results
Inthissection,wepresenttheresultsofourexperimentsevaluatingPlumeinABR,CCandLB.We
aimtoanswerthefollowingquestions:HowdoestheperformanceofPlumecomparewithrandom
sampling?HowdocontrollerstrainedwithPlumeperformintherealworld?
InFigure6,wepresentourresultscomparingPlumewithrandomsamplingandothercontrollers.
Wepresentourobservationsbelow.
Plumeoutperformsrandomtracesamplingacrossallbenchmarks.WithAdaptiveBitrate
Streaming,CongestionControl,andLoadBalancing,inbothsimulationandtherealworld,Plume
achieveshigherperformancethanrandomtracesampling.InFigure6a,weanalyzetheperformance
of Plume in ABR. We observe that Plume converges to a higher test reward, in both all traces
andslowtraces.WeadditionallyseethatPensieve-Plume-Dynamicsignificantlyimprovesupon
Pensieve-Random,butthattheimprovementisnotenoughtomatchtheperformanceofGelato.
InFigure6b,wefocusontheperformanceincongestioncontrol.Wefindasimilartrend,with
Plume-DynamicandPlume-Staticprovidingstatisticallysignificantimprovementsinconvergence
andperformanceoverrandominputtracesampling.Wefindthesamestoryinloadbalancingin
Figure6c.Wenotethatwhiletheabsolutenumericaldifferencesmayappearsmalldueinherent
scalesoftherewardfunction,theyexceedthe95%confidenceintervalbands,andtranslatetolarge
real-worlddifferencesaswewillseenext.

14 SagarPatel,JunyangZhang,SangeethaAbduJyothi,andNinaNarodytska
(a)AdaptiveBitrateStreaming
(b)CongestionControl (c)LoadBalancing
(d)ABRPufferPlatform
Fig.6. PlumeperformanceoverABR,CCandLB:Plumeoutperformsrandomsamplinginsimulation
andreal-worldplatformsforABR,CCandLB.TheABRPufferPlatformplotsvisualizedatafromthelive
streamingplatformPufferovertheperiod01Oct’22-01Oct’23,comprisingofover58.9stream-yearsofvideo.
Were-plotthedatafromthePufferwebsite[2]toaggregatethedifferentexperimentperiodstogether.95%
confidenceintervalsareshownaserrorbarsandbands.Wenotethattheaxisoftheplotsaredifferentdueto
inherentdifferencesbetweentheobjectivefunctions.

Plume:AFrameworkforHighPerformanceDeepRLNetworkControllers 15
Plume-StaticcloselytracksPlume-Dynamic.InFigures6a,6band6c,weobservethatPlume-
Static,whichemployedasimplerprioritizationstrategy,closelytrackstheperformanceofPlume-
Dynamic.Thisislikelyduetothefactthatinthesescenarios,theimpactofshiftingreward-to-go
valuesordifficultinputtracesisminimal.However,aswewillseelaterinSection7,whenthe
trainingdistributionisanomalousorissignificantlydifferentfromthetestingdistribution,Plume-
DynamiccanproveeffectiveoverPlume-Static.
Gelatooutperformsstate-of-the-artcontrollersintherealworldstreaminglivetelevision
overa1-yearperiod.TofurtherunderstandthebenefitofPlume,werunGelatowithPlume-Static
andrandomsamplingonthereal-worldlive-streamingPufferplatform[58].WeoptedforGelato
combinedwithPlume-StaticforthisevaluationgivenitsanalogousperformancetoPlume-Dynamic
inABR,butwithasimplerdesign.Additionally,weincludedGelatowithrandomsamplingasa
baselineforcomparativeanalysis.InFigure6d,weseethatGelato-Plume-Staticoutperformsthe
currentstate-of-the-artcontrollersFugu-FebandCausalSim,alongsidetheheuristic-basedBBA
inbothSSIMandstalling.Althoughpriorwork[8,58]reportedstatisticallysignificantstalling
improvementsonPuffer,GelatodistinguishesitselfbybecomingthefirstABRcontrollertoachieve
statistically significant improvements in both quality and stall reduction. This is particularly
noteworthyasGelatodoesnotdependonlow-levelTCPmetricslikeFuguorintricatesimulation
techniquesthatCausalSimuses.
Overthis1-yearperiod,thealgorithmsweanalyzestreamedover58.9stream-yearsofvideosto
over200,000viewersacrosstheInternet[2].Overthisduration,Gelato-Plume-Staticachieves75%,
78%and81%stallreductioncomparedtoCausalSim,FuguandBBArespectively(Fig.6d).Gelato-
Plume-StaticadditionallyachievesSSIMimprovementsof0.28,0.12and0.15dBoverCausalSim,
FuguandBBArespectively.NotethatthisqualityimprovementoverBBAismorethan5×thatof
Fugu,whichonlymanageda0.03dBimprovementoverBBA.CausalSimdidnotprovideanSSIM
improvementoverBBAoverthisperiod.Gelato-Plume-StatichasanaverageSSIMvariationof
0.77dB,comparedto0.67,0.53and0.78dBofCausalSim,FuguandBBArespectively.Moreover,
wefindthatGelato-Randomisastrongbaseline,achieving0.27dBSSIMimprovementand45%
stallreductionoverCausalSim.WemakesimilarobservationswhencomparingGelatowiththe
originalversionofFuguinFigure14inAppendixC.
7 PLUMEBENCHMARKING
HavingestablishedtheperformanceofPlumeonreal-worldcontrollersandexperimentsinSection6,
inthissection,wethoroughlymicrobenchmarkPlumeinordertostudyitsimpactinisolation.
WedemonstratePlume’sabilitytoofferhighperformanceandrobustnessacrossvarioustrace
distributions.
7.1 Settings
ToevaluatePlumeandvariousprioritizationstrategies,weintroduceacontrolledABRenvironment
formicrobenchmarkingprioritization:TraceBench.TraceBenchmakestwokeychangestothe
standardABRenvironment.First,itsimplifiesthequality-of-experiencemeasurementtoinclude
onlytwoterms,qualityandstalling.Second,itparameterizesthetracesbykeycharacteristics
of real-world traces: mean and variance of network throughput. With these modifications, we
canreliablyandthoroughlyevaluatethecontrolleracrossvariousnetworkconditions.Whilethis
designisasimplificationofthereal-worldenvironment,itgivesagoodapproximationofawide
range of realistic settings. We believe that the development of such a framework is important
forthecommunityasreal-worlddatasetsdonotallowmicrobenchmarkingofDRLcontrollersor
prioritizationstrategies.Weenvisionthatitcanbeusedbyothercontrollerdesigners.Wenote

16 SagarPatel,JunyangZhang,SangeethaAbduJyothi,andNinaNarodytska
Fig. 7. Trace Datasets of TraceBench: Distributions of traces present in each dataset employed in
TraceBench.Thebroadrangeoftracedistributionsallowsustothoroughlybenchmarkprioritizationtech-
niques.
Fig.8. ComparingPrioritizationTechniques:Performanceofrandomsampling,PrioritizedExperience
Replay(PER),Trace-ErrorWeightedsamplingandPlume-DynamicontheMajorityFastdatasetofTraceBench.
Plume-Dynamic,whichbalancesbothTrace-ErrorandLow-rewardweights,offersthehighestperformance.
95%confidenceintervalshownaserrorbands.
thatparameterizedtracegenerationisapartofTraceBench,usedtocreateavarietyofscenariosto
evaluatecontrollerson.Itisnotpartofanyoftheprioritizationstrategies.
IngeneratingTracesforTraceBench,wefocusontraceswithtwolevelsofmeanthroughput,
slowandfast,andtwolevelsofvarianceofthethroughput,highvarianceandlowvariance.Inthis
benchmark,wegeneratethreesetsofdatasetswithdifferentproportionsofthesetraces:Majority
Fast,Balanced,andMajoritySlow.SeeFigure7foravisualizationofthetracedistributions,andsee
Figure13inAppendixBforavisualizationofexampletraces.Notethatthetrainingandtesting
datasetsremaindisjoint:acontrollertrainedontheMajorityFastdatasetdoesnothaveaccessto
thetestingversionofit.
Weusetheoff-policyRLalgorithmApe-XDQN[20].Toevaluateprioritizationinisolation,we
usethesameDRLhyper-parametersforallagentsandpresentresultsaveragedover4instances.
Fordetailsofourtrainingparameters,seeAppendixB.
7.2 Results
Ourexperimentsinvestigatetwoimportantquestions.First,weevaluatehowtheversionsofPlume’s
prioritization,Plume-StaticandPlume-Dynamic,comparetorandomtracesampling,thestandard

Plume:AFrameworkforHighPerformanceDeepRLNetworkControllers 17
(a)Scenario1:TrainingontheMajorityFast,TestingontheMajoritySlowdataset.
(b)Scenario2:TrainingandTestingontheBalanceddataset.
(c)Scenario3:TrainingontheMajoritySlow,TestingontheMajorityFastdataset.
Fig.9. BenchmarkingPlumeacrossTraceDistributions:Webenchmarkprioritizationtechniquesacross
differenttrainingandtestingtracedistributions.Plume-Dynamicprovidesgeneralizableperformanceim-
provement,beatingrandomsamplingandPlume-Staticinscenarios(1),(2)and(3).95%confidenceinterval
shownaserrorbands.
tracesamplingtechnique.WeadditionallyevaluatetheimpactofPER[46],thestateprioritization
technique described in Section 3.2. Second, we investigate how sensitive these methods are to
networkconditionsdistributionshifts.Wewouldliketoemphasizeherethattheseexperimentsare
possibleinreal-worldsettings.
Focusingontail-endedperformanceisimportant.Westartourevaluationwithanablation
studyontheimpactoftheapproximationtermsinPlume-Dyanmic,aspresentedinSec.4.3.We
evaluateaversionofPlume-Dynamicwithoutthecompensationterm.Werefertothisversionas

18 SagarPatel,JunyangZhang,SangeethaAbduJyothi,andNinaNarodytska
Fig.10. VisualizationoftheprioritizationfoundbyPlume-Dynamicinvariousdatasets:Therelative
changeinsamplingweightforeachkindoftracesoverthetrainingprogress.Selectingallkindsoftracesat
weight1isequivalenttorandomsampling.Wenotethattheground-truthlabels(e.gSlow-HighVariance)
arenotprovidedtoPlume.
“Trace-Error”.WeuseMajorityFastdatasetforthisevaluationasitmodelsreal-worldworkloads
closely.InFigure8,wepresenttheresultsofrandomtracesampling,PER,Plume-Dynamic,and
Trace-errorontheMajorityFastdataset.WeobservethatTrace-errorcanbeworsethanrandom
sampling,particularlyinslowtraces,whereitnotonlyconvergestoalowrewardbuthashigh
variance over the training interval. Meanwhile, Plume-Dynamic, which balances both Trace-
errorandLow-reward,offerssignificantlybetterperformanceinbothFastandSlowtraces.This
resulthighlightsthefactthatfocusingonthelowperformingtracescanbevitaltogeneralizable
performance.
In Figure 9, we analyze the performance of Plume across various training and testing trace
distributions.Particularly,weanalyzethefollowingscenarios:
• Scenario1:Thetrainingdistributionissimilartotherealworldbutthetestingisadversarially
different,i.e.,wetrainontheMajorityFastbuttestontheMajoritySlowdataset.
• Scenario2:Bothtrainingandtestinghaveabalancedsetoftraces,i.e.,wetrainandtestonthe
Balanceddataset.
• Scenario3:Thetrainingdistributionlargelyconsistsofthetailendofthetestingdistribution,
i.e.,wetrainontheMajoritySlowbuttestontheMajorityFastdataset.
Plumeoutperformsrandomsamplingregardlessoftracedistribution.Asweobservein
Figures9aand9bforthetestrewardforscenarios(1)and(2),Plume-Dynamicprovidesasignificant
performanceimprovementoverrandomsampling.Moreover,eveninFigure9forscenario(3),
where we may least expect prioritization to help, Plume-Dynamic is still better than random
sampling.WeadditionallyobservethatPlume-Static,whichperformswellinscenario(1),falls
behindPlume-Dynamicinscenarios(2)and(3)wherethetraininginputtracedistributionsare
eitheranomalousoraredramaticallydifferentfromthetestingdistribution.
Plume-Dynamiceffectivelyadaptstoalltrainingtracedistribution.Tobetterunderstand
howPlume-Dynamicsoeffectivelygeneralizesacrossallofthesetracedistributions,wevisualize
thesamplingweightofdifferenttracesduringtraininginFigure10.Weobservethatwhiletraining
ontheMajorityFastdataset,itundersamplestheFasttracesandoversamplestheSlowones.In
theMajoritySlowdataset,itundersamplestheSlow–LowVariancetraceswhileoversamplingthe
FastandSlow–HighVarianceones.ThishighlightsthepowerofPlume-Dynamic’sautomated
prioritization:Itadaptsitselftothedistributionineachdatasetandallowsthecontrollertofocus
onclusterswiththemosttolearnfrom.

Plume:AFrameworkforHighPerformanceDeepRLNetworkControllers 19
ControllerstrainedwithPlumearerobusttotracedistributionshifts.Inthesecondrowof
plotsinFigures9a,9band9,wevisualizetheSlow-Tracesperformanceofdifferentprioritization
schemes.Weobservethatrandomtracesampling’sperformanceinslowtracesislargelydependent
onitstrainingdataset.IfthetrainingdatasethadfewSlowtraces,asinscenario(1),theperformance
issignificantlyworsethanitisinscenario(3),whereithadmany.However,Plume-Dynamic’s
performanceisrobusttothetrainingtracedistribution:thecontrollersallconvergetoasimilar
rewardinallthreescenarios.Intheever-changinglandscapeofusers,devices,andinfrastructure
inherenttothenetworkdomain,thisaddedrobustnesscanbeparticularlyimportant.Itreduces
theneedforretrainingandultimatelyreducesthecomputerequirementsandenergyconsumption
oftheentiresystem.
Below,wesummarizethefindingsofourexperimentswithABR,CCandLBpresentedinSection6,
andtheanalysisofourextensivePlumebenchmarkingpresentedinthissection.
• PlumeisageneralizedsolutionforDRLtrainingininput-drivenenvironmentsthatautomatically
balancesthetracedistribution,andofferssignificantimprovementinperformanceoverrandom
samplinginABR,CCandLB,insimulationandinreal-worldtesting,overbothon-policyand
off-policyalgorithms.
• Plume’s prioritization strategies work across trace distributions, providing controllers with
greaterperformanceandrobustnessinall.
• GelatotrainedwithPlumeoffersthebestperformancewhencomparedtopriorABRcontrollers
onthereal-worldPufferplatform.Itachieves75%and78%reductioninstallsoverCausalSim[8]
andFugu[58]respectively.ItalsoachievesastatisticallysignificantSSIMimprovementof0.28
dBoverCausalSimand0.12dBoverFugu.
8 DISCUSSIONANDLIMITATIONS
WeenvisionPlumetoopenanewavenueofresearchinthecontextofDRLtraining.Ratherthan
evolveintoanotherhyperparameterthatneedstuningincomplexRLsettings,theproblemoftrace
samplinglendsitselfwelltoprincipledanalysis,andinturnageneralizedandbroadlyapplicable
solution.However,ourworkstillleavesagapforfutureworktobuildupon.
Theneedforsystematicstudyofinput-drivenDRLtraining.OuranalysisofPlumehighlights
thesignificantimpactofskewandthebenefitsderivedfromaddressingit.Thisfindingprovides
a strong motivation to explore other overlooked factors that may also influence input-driven
DRL training. While the broader ML community has conducted in-depth studies on training
parameters[9],DRLenvironments[13],andevaluationmetrics[7],thereisalackofsuchresearch
inthenetworkingdomain.Engaginginsystematicstudiesinthisfrontcouldenabletheresearch
communitytobetterunderstandthepotentialofexistingsolutionsandpavewayforanempirical
assessmentoftherealchallengesfacedbyoptimizedinput-drivenDRLsolutions.
FuturedirectionforPlume.Inadditiontonetworkingenvironments,Plumecanalsobebeneficial
inothertrace-drivenDRLsettingssuchasdronecontrol,autonomousdriving,etc.Plume,aswe
presentedit,cannotbeuseddirectlyinsuchenvironmentswithmorecomplexinputprocesses.
However,extensionstoPlumeaspresentedinthispapermaybeaninterestingfuturedirection.
Sim2RealGap.Plumechangeswhichtracesgetsampledandnothowtheyaresimulated.Plume
does not address the problem related to the gap between the simulation environment and the
real-world setting (Sim2Real Gap). Solutions that bring simulation closer to reality while still
maintainingtrainingefficiencycanbecombinedwithPlume.
Large-ScaleTraining.Itispossiblethatthebenefitsofhigherstate-actionexplorationandfeature
learning offered by Plume diminish with a very deep neural network over a large number of

20 SagarPatel,JunyangZhang,SangeethaAbduJyothi,andNinaNarodytska
trainingstepsandparallelenvironments.OurexperimentalevidencesuggeststhatPlumeishighly
relevant for practical DRL environments and training settings. However, we cannot ascertain
theeffectivenessofPlumeatthescaleofstate-of-the-artGoagents[47],whichrequirestraining
capabilitiesonlyavailabletolargecompanies.
9 RELATEDWORK
PrioritizationinSupervisedlearning.Classimbalanceisfrequentlyachallengeinsupervised
data-drivennetworkingproblems,wheresamplesofsomeclassesofnetworkconditionsorscenarios
occur rarely [14, 27, 29, 60]. A popular technique to address this problem is to oversample or
undersamplecertainclassestoensurethatthemodeldoesnotdrownouttheerrorintheminority
classes[26].Suchtechniquescannotbeusedinreinforcementlearning,wherethelearninghappens
usingstates,actionsandrewardsratherthanafixeddatasetwithlabels.
Prioritization in DRL. While we present the first systematic methodology of prioritization
of input traces in DRL, prioritization/importance sampling has been applied at other points in
theDRLworkflow.PER[46]isusedtoprioritizetransitionsinthereplaybufferinactor-critic
algorithms[53],inthemulti-agentsetting[15],andintext-basedDRLenvironments[40]toimprove
sampleefficiency.Horganet.al[20]usedPERinconjunctionwithdistributedactingtoimprove
feature learning. Schulman et.al [48, 49] employed importance sampling to reduce variance of
on-policy training. However, as shown in our experiment (§ 3.2), these prior solutions do not
addresstheskewininput-drivenenvironments.
DRLforNetworkingandSystemsapplications.WhilePlumefocusesonimprovingtraining
overagiveninputdataset,Giladet.al.[16]employedRLtofindadditionaltrainingtracesthatcan
helptheDRLagentgeneralizetounseennetworkconditions.Buildingonthisidea,Xiaetal.[56]
introducedasystematicCurriculumLearningbasedapproachtogenerateadditionalenvironment
configurations.Bothofthetechniquesgenerateadditionaltrainingmaterialforperformancein
unseen conditions. However, while both of these techniques have been shown to improve the
performance of controllers trained with limited datasets (of a few hundred traces), generative
solutionshavenotbeendemonstratedtoprovidecompetitiveperformanceonreal-worldplatforms
suchasPuffertothebestofourknowledge.Incontrast,Plume-trainedGelatocontinuestobethe
bestperformingcontrolleronPuffersinceOctober2022.WenotethatPlume’strainingexclusively
usespubliclyavailabledatasetsanddoesnotrequiresolvinganytracegenerationproblems.Mao
et.al.[35]introducedthealgorithm-sideoptimizationofusinginput-dependentbaselinestoreduce
thevarianceofon-policyalgorithmsatthepolicyoptimizationstep.SincePlumeworksoutsidethe
DRLtrainingloop,itcanalsobeusedinconjunctionwithanysuchalgorithm-sideoptimizations.
DoublyRobustestimation[23]helpsinestimatingperformancevariationsduringinput-driven
evaluationbutdoesnotaddresstheskewinthedatasetdirectly.
10 CONCLUSION
PracticaladoptionofDRL-basednetworkcontrollersislimitedbecausetheresearchcommunity
doesnotfullyknowhowtoproducehighperformantcontrollers.Weuncoverthatskewinthe
inputdatasetsofDRLcontrollersplaysasignificantroleinperformance,andputforwardPlume,a
systematicmethodologyforaddressingskewininput-drivenDRL.Wethoroughlystudytheimpact
ofPlume,andshowthatPlumeprovidesgeneralizableperformanceimprovementacrossmultiple
tracedistributions,DRLenvironmentsandalgorithms.OurnovelDRL-basedABRcontroller,Gelato,
trainedwithPlumeoffersstate-of-the-artperformanceonthereal-worldlivestreamingplatform
Pufferovermorethanayear.Plumeopensanewavenueofresearchformethodicalcontrolover
DRLtrainingininput-drivennetworkingenvironmentsandbeyond.

Plume:AFrameworkforHighPerformanceDeepRLNetworkControllers 21
REFERENCES
[1] [n.d.]. Expectation–maximization algorithm - Wikipedia. https://en.wikipedia.org/wiki/Expectation%E2%80%
93maximization_algorithm. (Accessedon01/16/2023).
[2] [n.d.].Puffer.https://puffer.stanford.edu/results/. (Accessedon04/20/2022).
[3] [n.d.].Scikit-LearnRecursiveFeatureElimiation.https://scikit-learn.org/stable/modules/generated/sklearn.feature_
selection.RFE.html#sklearn.feature_selection.RFE. (Accessedon01/15/2023).
[4] [n.d.]. Silhouette(clustering)-Wikipedia. https://en.wikipedia.org/wiki/Silhouette_(clustering). (Accessedon
01/16/2023).
[5] SoheilAbbasloo,Chen-YuYen,andHJonathanChao.2020. Classicmeetsmodern:Apragmaticlearning-based
congestioncontrolfortheInternet.InProceedingsoftheAnnualconferenceoftheACMSpecialInterestGrouponData
Communicationontheapplications,technologies,architectures,andprotocolsforcomputercommunication.632–647.
[6] JoshuaAchiam.2018.SpinningUpinDeepReinforcementLearning.(2018).
[7] RishabhAgarwal,MaxSchwarzer,PabloSamuelCastro,AaronCCourville,andMarcBellemare.2021. Deeprein-
forcementlearningattheedgeofthestatisticalprecipice.Advancesinneuralinformationprocessingsystems34(2021),
29304–29320.
[8] AbdullahAlomar,PouyaHamadanian,ArashNasr-Esfahany,AnishAgarwal,MohammadAlizadeh,andDevavrat
Shah.2023. {CausalSim}:ACausalFrameworkforUnbiased{Trace-Driven}Simulation.In20thUSENIXSymposium
onNetworkedSystemsDesignandImplementation(NSDI23).1115–1147.
[9] MarcinAndrychowicz,AntonRaichuk,PiotrStańczyk,ManuOrsini,SertanGirgin,RaphaëlMarinier,Leonard
Hussenot,MatthieuGeist,OlivierPietquin,MarcinMichalski,etal.2020.Whatmattersforon-policydeepactor-critic
methods?alarge-scalestudy.InInternationalconferenceonlearningrepresentations.
[10] GregBrockman,VickiCheung,LudwigPettersson,JonasSchneider,JohnSchulman,JieTang,andWojciechZaremba.
2016.Openaigym.arXivpreprintarXiv:1606.01540(2016).
[11] LiChen,JustinasLingys,KaiChen,andFengLiu.2018. Auto:Scalingdeepreinforcementlearningfordatacenter-
scaleautomatictrafficoptimization.InProceedingsofthe2018conferenceoftheACMspecialinterestgroupondata
communication.191–205.
[12] MaximilianChrist,NilsBraun,JuliusNeuffer,andAndreasWKempa-Liehr.2018.Timeseriesfeatureextractionon
basisofscalablehypothesistests(tsfresh–apythonpackage).Neurocomputing307(2018),72–77.
[13] KaleighClary,EmmaTosch,JohnFoley,andDavidJensen.2019.Let’sPlayAgain:VariabilityofDeepReinforcement
LearningAgentsinAtariEnvironments.arXivpreprintarXiv:1904.06312(2019).
[14] ShiDong.2021.MulticlassSVMalgorithmwithactivelearningfornetworktrafficclassification.ExpertSystemswith
Applications176(2021),114885.
[15] JakobFoerster,NantasNardelli,GregoryFarquhar,TriantafyllosAfouras,PhilipHSTorr,PushmeetKohli,andShimon
Whiteson.2017.Stabilisingexperiencereplayfordeepmulti-agentreinforcementlearning.InInternationalconference
onmachinelearning.PMLR,1146–1155.
[16] TomerGilad,NathanHJay,MichaelShnaiderman,BrightenGodfrey,andMichaelSchapira.2019. Robustifying
networkprotocolswithadversarialexamples.InProceedingsofthe18thACMWorkshoponHotTopicsinNetworks.
85–92.
[17] CharlesR.Harris,K.JarrodMillman,StéfanJ.vanderWalt,RalfGommers,PauliVirtanen,DavidCournapeau,
EricWieser,JulianTaylor,SebastianBerg,NathanielJ.Smith,RobertKern,MattiPicus,StephanHoyer,MartenH.
vanKerkwijk,MatthewBrett,AllanHaldane,JaimeFernándezdelRío,MarkWiebe,PearuPeterson,PierreGérard-
Marchant,KevinSheppard,TylerReddy,WarrenWeckesser,HameerAbbasi,ChristophGohlke,andTravisE.Oliphant.
2020.ArrayprogrammingwithNumPy.Nature585,7825(Sept.2020),357–362. https://doi.org/10.1038/s41586-020-
2649-2
[18] DanHendrycksandKevinGimpel.2016.Gaussianerrorlinearunits(gelus).arXivpreprintarXiv:1606.08415(2016).
[19] MatteoHessel,JosephModayil,HadoVanHasselt,TomSchaul,GeorgOstrovski,WillDabney,DanHorgan,BilalPiot,
MohammadAzar,andDavidSilver.2018. Rainbow:Combiningimprovementsindeepreinforcementlearning.In
Thirty-secondAAAIconferenceonartificialintelligence.
[20] DanHorgan,JohnQuan,DavidBudden,GabrielBarth-Maron,MatteoHessel,HadoVanHasselt,andDavidSilver.
2018.Distributedprioritizedexperiencereplay.arXivpreprintarXiv:1803.00933(2018).
[21] Te-YuanHuang,RameshJohari,NickMcKeown,MatthewTrunnell,andMarkWatson.2014.Abuffer-basedapproach
torateadaptation:Evidencefromalargevideostreamingservice.InProceedingsofthe2014ACMconferenceon
SIGCOMM.187–198.
[22] NathanJay,NogaRotman,BrightenGodfrey,MichaelSchapira,andAvivTamar.2019.Adeepreinforcementlearning
perspectiveoninternetcongestioncontrol.InInternationalconferenceonmachinelearning.PMLR,3050–3059.
[23] JunchenJiang,VyasSekar,IonStoica,andHuiZhang.2017.Unleashingthepotentialofdata-drivennetworking.In
InternationalConferenceonCommunicationSystemsandNetworks.Springer,110–126.

22 SagarPatel,JunyangZhang,SangeethaAbduJyothi,andNinaNarodytska
[24] JustinMJohnsonandTaghiMKhoshgoftaar.2020. Theeffectsofdatasamplingwithdeeplearningandhighly
imbalancedbigdata.InformationSystemsFrontiers22,5(2020),1113–1131.
[25] StevenKapturowski,GeorgOstrovski,JohnQuan,RemiMunos,andWillDabney.2018.Recurrentexperiencereplay
indistributedreinforcementlearning.InInternationalconferenceonlearningrepresentations.
[26] HarsurinderKaur,HusanbirSinghPannu,andAvleenKaurMalhi.2019. Asystematicreviewonimbalanceddata
challengesinmachinelearning:Applicationsandsolutions.ACMComputingSurveys(CSUR)52,4(2019),1–36.
[27] JoffreyLLeevy,TaghiMKhoshgoftaar,andJaredMPeterson.2021.Mitigatingclassimbalanceforiotnetworkintrusion
detection:asurvey.In2021IEEESeventhInternationalConferenceonBigDataComputingServiceandApplications
(BigDataService).IEEE,143–148.
[28] EricLiang,RichardLiaw,RobertNishihara,PhilippMoritz,RoyFox,KenGoldberg,JosephE.Gonzalez,MichaelI.
Jordan,andIonStoica.2018.RLlib:AbstractionsforDistributedReinforcementLearning.InInternationalConference
onMachineLearning(ICML).
[29] XiaoyuLiangandTaiebZnati.2019.AnempiricalstudyofintelligentapproachestoDDoSdetectioninlargescale
networks.In2019InternationalConferenceonComputing,NetworkingandCommunications(ICNC).IEEE,821–827.
[30] HongziMao,MohammadAlizadeh,IshaiMenache,andSrikanthKandula.2016.Resourcemanagementwithdeep
reinforcementlearning.InProceedingsofthe15thACMworkshoponhottopicsinnetworks.50–56.
[31] HongziMao,ShannonChen,DrewDimmery,ShaunSingh,DrewBlaisdell,YuandongTian,MohammadAlizadeh,and
EytanBakshy.2020.Real-worldvideoadaptationwithreinforcementlearning.arXivpreprintarXiv:2008.12858(2020).
[32] HongziMao,ParimarjanNegi,AkshayNarayan,HanruiWang,JiachengYang,HaonanWang,RyanMarcus,Mehrdad
KhaniShirkoohi,SongtaoHe,VikramNathan,etal.2019.Park:Anopenplatformforlearning-augmentedcomputer
systems.AdvancesinNeuralInformationProcessingSystems32(2019).
[33] HongziMao,RaviNetravali,andMohammadAlizadeh.2017. Neuraladaptivevideostreamingwithpensieve.In
ProceedingsoftheConferenceoftheACMSpecialInterestGrouponDataCommunication.197–210.
[34] HongziMao,MalteSchwarzkopf,ShaileshhBojjaVenkatakrishnan,ZiliMeng,andMohammadAlizadeh.2019.
Learningschedulingalgorithmsfordataprocessingclusters.InProceedingsoftheACMspecialinterestgroupondata
communication.270–288.
[35] HongziMao,ShaileshhBojjaVenkatakrishnan,MalteSchwarzkopf,andMohammadAlizadeh.2018.Variancereduction
forreinforcementlearningininput-drivenenvironments.arXivpreprintarXiv:1807.02264(2018).
[36] MelikaMeskovic,MladenKos,andAmirMeskovic.2015.Optimalchunkschedulingalgorithmbasedontaboosearch
foradaptivelivevideostreaminginCDN-P2P.In201523rdInternationalConferenceonSoftware,Telecommunications
andComputerNetworks(SoftCOM).IEEE,205–209.
[37] VolodymyrMnih,AdriaPuigdomenechBadia,MehdiMirza,AlexGraves,TimothyLillicrap,TimHarley,DavidSilver,
andKorayKavukcuoglu.2016.Asynchronousmethodsfordeepreinforcementlearning.InInternationalconferenceon
machinelearning.PMLR,1928–1937.
[38] VolodymyrMnih,KorayKavukcuoglu,DavidSilver,AlexGraves,IoannisAntonoglou,DaanWierstra,andMartin
Riedmiller.2013.PlayingAtariwithdeepreinforcementlearning.arXivpreprintarXiv:1312.5602(2013).
[39] PhilippMoritz,RobertNishihara,StephanieWang,AlexeyTumanov,RichardLiaw,EricLiang,MelihElibol,Zongheng
Yang,WilliamPaul,MichaelIJordan,etal.2018.Ray:Adistributedframeworkforemerging{AI}applications.In
13thUSENIXSymposiumonOperatingSystemsDesignandImplementation(OSDI18).561–577.
[40] KarthikNarasimhan,TejasKulkarni,andReginaBarzilay.2015.Languageunderstandingfortext-basedgamesusing
deepreinforcementlearning.arXivpreprintarXiv:1506.08941(2015).
[41] AdamPaszke,SamGross,FranciscoMassa,AdamLerer,JamesBradbury,GregoryChanan,TrevorKilleen,ZemingLin,
NataliaGimelshein,LucaAntiga,etal.2019.Pytorch:Animperativestyle,high-performancedeeplearninglibrary.
Advancesinneuralinformationprocessingsystems32(2019).
[42] F.Pedregosa,G.Varoquaux,A.Gramfort,V.Michel,B.Thirion,O.Grisel,M.Blondel,P.Prettenhofer,R.Weiss,V.
Dubourg,J.Vanderplas,A.Passos,D.Cournapeau,M.Brucher,M.Perrot,andE.Duchesnay.2011. Scikit-learn:
MachineLearninginPython.JournalofMachineLearningResearch12(2011),2825–2830.
[43] TobiasPohlen,BilalPiot,ToddHester,MohammadGheshlaghiAzar,DanHorgan,DavidBudden,GabrielBarth-Maron,
HadoVanHasselt,JohnQuan,MelVečerík,etal.2018.Observeandlookfurther:Achievingconsistentperformance
onAtari.arXivpreprintarXiv:1805.11593(2018).
[44] AntoninRaffin,AshleyHill,AdamGleave,AnssiKanervisto,MaximilianErnestus,andNoahDormann.2021.Stable-
Baselines3:ReliableReinforcementLearningImplementations.JournalofMachineLearningResearch22,268(2021),
1–8. http://jmlr.org/papers/v22/20-1364.html
[45] AntoninRaffin,JensKober,andFreekStulp.2022.Smoothexplorationforroboticreinforcementlearning.InConference
onRobotLearning.PMLR,1634–1644.
[46] TomSchaul,JohnQuan,IoannisAntonoglou,andDavidSilver.2015.Prioritizedexperiencereplay.arXivpreprint
arXiv:1511.05952(2015).

Plume:AFrameworkforHighPerformanceDeepRLNetworkControllers 23
[47] JulianSchrittwieser,IoannisAntonoglou,ThomasHubert,KarenSimonyan,LaurentSifre,SimonSchmitt,Arthur
Guez,EdwardLockhart,DemisHassabis,ThoreGraepel,etal.2020.MasteringAtari,Go,ChessandShogibyplanning
withalearnedmodel.Nature588,7839(2020),604–609.
[48] JohnSchulman,SergeyLevine,PieterAbbeel,MichaelJordan,andPhilippMoritz.2015.Trustregionpolicyoptimization.
InInternationalconferenceonmachinelearning.PMLR,1889–1897.
[49] JohnSchulman,FilipWolski,PrafullaDhariwal,AlecRadford,andOlegKlimov.2017.Proximalpolicyoptimization
algorithms.arXivpreprintarXiv:1707.06347(2017).
[50] DavidSilver.2015.LecturesonReinforcementLearning.url:https://www.davidsilver.uk/teaching/.
[51] KevinSpiteri,RahulUrgaonkar,andRameshKSitaraman.2020.BOLA:Near-optimalbitrateadaptationforonline
videos.IEEE/ACMTransactionsonNetworking28,4(2020),1698–1711.
[52] RichardSSuttonandAndrewGBarto.2018.Reinforcementlearning:Anintroduction.MITpress.
[53] ZiyuWang,VictorBapst,NicolasHeess,VolodymyrMnih,RemiMunos,KorayKavukcuoglu,andNandodeFreitas.
2016.Sampleefficientactor-criticwithexperiencereplay.arXivpreprintarXiv:1611.01224(2016).
[54] ZhouWang,AlanCBovik,HamidRSheikh,andEeroPSimoncelli.2004. Imagequalityassessment:fromerror
visibilitytostructuralsimilarity.IEEEtransactionsonimageprocessing13,4(2004),600–612.
[55] ZiyuWang,TomSchaul,MatteoHessel,HadoHasselt,MarcLanctot,andNandoFreitas.2016. Duelingnetwork
architecturesfordeepreinforcementlearning.InInternationalconferenceonmachinelearning.PMLR,1995–2003.
[56] ZhengxuXia,YajieZhou,FrancisYYan,andJunchenJiang.2022.Genet:automaticcurriculumgenerationforlearning
adaptationinnetworking.InProceedingsoftheACMSIGCOMM2022Conference.397–413.
[57] ZhiyingXu,FrancisYYan,RacheeSingh,JustinTChiu,AlexanderMRush,andMinlanYu.2023. Teal:Learning-
AcceleratedOptimizationofWANTrafficEngineering.InProceedingsoftheACMSIGCOMM2023Conference.378–393.
[58] FrancisYYan,HudsonAyers,ChenzhiZhu,SadjadFouladi,JamesHong,KeyiZhang,PhilipLevis,andKeithWinstein.
2020.Learninginsitu:arandomizedexperimentinvideostreaming.In17thUSENIXSymposiumonNetworkedSystems
DesignandImplementation(NSDI20).495–511.
[59] Han-JiaYe,Hong-YouChen,De-ChuanZhan,andWei-LunChao.2020. Identifyingandcompensatingforfeature
deviationinimbalanceddeeplearning.arXivpreprintarXiv:2001.01385(2020).
[60] QizhenZhang,KelvinKWNg,CharlesKazer,ShenYan,JoãoSedoc,andVincentLiu.2021.MimicNet:fastperformance
estimatesfordatacenternetworkswithmachinelearning.InProceedingsofthe2021ACMSIGCOMM2021Conference.
287–304.
[61] HangZhu,VarunGupta,SatyajeetSinghAhuja,YuandongTian,YingZhang,andXinJin.2021.Networkplanning
withdeepreinforcementlearning.InProceedingsofthe2021ACMSIGCOMM2021Conference.258–271.

24 SagarPatel,JunyangZhang,SangeethaAbduJyothi,andNinaNarodytska
PotentialTraceFeatures Parametersforfeature
Mean –
Quantile 2.5𝑡ℎ
Quantile 5𝑡ℎ
Quantile 95𝑡ℎ
TruncatedMean 5𝑡ℎ quantile
TruncatedMean 12.5𝑡ℎ quantile
TruncatedMean 25𝑡ℎ quantile
AbsoluteFourierTransformSpectrum SpectralCentroid
RatioofValuesbeyondstandarddev. Beyond1×standarddev.
RatioofValuesbeyondstandarddev. Beyond2.5×standarddev.
VariationCoefficient –
CentralApproximationofSecondDerivative MeanAggregation
TruncatedMeanAbsoluteChange Truncatedbeyond5𝑡ℎ and95𝑡ℎ quantile
TruncatedMeanAbsoluteChange Truncatedbeyond1.25𝑡ℎ and98.75𝑡ℎ quantile
Autocorelation Lagof3
Autocorelation Lagof4
Autocorelation Lagof8
Table1. AlloftheTracefeaturesextractedusingthelibrarytsfresh[12].Thesefeaturesareextractedfor
eachtracedatasetandthenautomaticallyfilteredbyournovelfeatureselectiontechnique.

Plume:AFrameworkforHighPerformanceDeepRLNetworkControllers 25
(a)AdaptiveBitrateStreamingTraces
(b)CongestionControlTraces
(c)LoadBalancingTraces
Fig.11. VisualizationofPlumeClusteringinABR,CCandLB:Wevisualizetheclusteringautomatically
producedbyPlumeinABR,CCandLB.WeseethatPlumeproducesminimalclusterswhilealsoseparating
salientcharacteristicssuchasmeanthroughputandlatency.NotethatthroughputCVistheper-trace
coefficientofvariationofthroughput,andthattheaxesaredifferent.

26 SagarPatel,JunyangZhang,SangeethaAbduJyothi,andNinaNarodytska
(a)MajorityFastDataset
(b)BalancedDataset
(c)MajoritySlowDataset
Fig.12. VisualizationofPlumeClusteringinTraceBench:Wevisualizetheclusteringautomatically
producedbyPlumeintheMajorityFast,Balanced,andMajoritySlowdatasets.Ineachofthedatasets,we
seethatPlumecansuccessfullyseparatethetwolevelsofthroughputandvariance.Notethatthroughput
CVistheper-tracecoefficientofvariationofthroughput,andthattheaxesaredifferentacrossallplots.
Fig.13. VisualizationofTracesgeneratedinTraceBench:AThroughputvsTimeplotofexampletraces
usedinTraceBench.Thebroadcoverageofthemeanandvarianceofthethroughputrequirestheagentto
learntoadapttoeachkindoftracedifferently.

Plume:AFrameworkforHighPerformanceDeepRLNetworkControllers 27
A PRIORITIZEDTRACESAMPLINGDETAILS
Inthissection,weprovidedetails,visualizationsandanalysisofthePlumeanditsthreestages.
A.1 CriticalFeatureIdentification
WerecallthatintheCriticalFeatureIdentificationstage,Plumeidentifiestracesbyfirstextracting
awiderangeoffeaturesandthenfilteringthemtofindthecriticalfeatures.
Awiderangeoffeaturesisextractedforeachtraceinthedatasetoftraces.Then,thissetof
featuresgoesthroughourautomatedfilteringprocess.Duringthisprocess,about40%ofthefeatures
areeliminated.InTable1,wepresentthelistofallthefeaturesextracted.Thelistcontains16
features,ofwhich7describethecentraltendencyand9describethespreadoftheinputvalues.
InTraceBench,thefollowingcriticalfeaturesofthenetworkthroughputtracesareidentified.
MajorityFastdataset:TruncatedMeanAbsoluteChangeof5𝑡ℎ and95𝑡ℎ quantile,TruncatedMean
AbsoluteChangeof1.25𝑡ℎ and98.75𝑡ℎ quantile,TruncatedMeanofthe5𝑡ℎ quantile,Truncated
Meanofthe12.5𝑡ℎquantile,TruncatedMeanofthe25𝑡ℎquantile,andVariationCoefficient.Balanced
dataset: Truncated Mean Absolute Change of 5𝑡ℎ and 95𝑡ℎ quantile, Truncated Mean Absolute
Changeof1.25𝑡ℎ and98.75𝑡ℎ quantile,TruncatedMeanofthe5𝑡ℎ quantile,TruncatedMeanof
the 12.5𝑡ℎ quantile, Truncated Mean of the 25𝑡ℎ quantile, and Variation Coefficient. Majority
Slowdataset:Autocorrelationwithlag3,Autocorrelationwithlag8,TruncatedMeanofthe5𝑡ℎ
quantile,TruncatedMeanofthe12.5𝑡ℎquantile,TruncatedMeanofthe25𝑡ℎquantile,andVariation
Coefficient.
InABR,thefollowingcriticalfeaturesofthroughputareidentified:Autocorrelationwithlag3,
Mean,SpectralCentroidoftheAbsoluteFourierTransformSpectrum,2.5𝑡ℎ quantile,5𝑡ℎ quantile,
95𝑡ℎ quantile,Ratioofvaluesbeyond2.5×standarddeviation,TruncatedMeanAbsoluteChangeof
5𝑡ℎ and95𝑡ℎ quantile,andTruncatedMeanAbsoluteChangeof1.25𝑡ℎ and98.75𝑡ℎ quantile.
InCongestionControl,becausetracesarenottime-varyingseries,butinsteadatupleofkey
simulationvalues,thetupleistreatedasthesetofcriticalfeatures.Thesekeysimulationvalues
includeBandwidth,Latency,Max.QueueSize,andLoss.
In Load Balancing, the following features of the incoming job sizes over time are identified
askey:Autocorrelationwithlag3,TruncatedMeanAbsoluteChangeof5𝑡ℎ and95𝑡ℎ quantile,
SpectralCentroidoftheAbsoluteFourierTransformSpectrum,Mean,Centralapproximationof
SecondDerivative,5𝑡ℎ QuantileTruncatedMean,12.5𝑡ℎ QuantileTruncatedMean,andVariation
Coefficient.
WeobservethatPlumefindsdifferentfeaturestobecriticalfordifferentdatasets.Thishighlights
theabilityofPlumetoeffectivelyadapttothedistributionoftrainingtracestosuccessfullyseparate
them.
A.2 Clustering
WerecallthatintheClusteringstageofPlume,wegroupsimilartracestogethertoattemptto
reducethecomplexityoftheprioritizationproblemfromatrace-leveltoacluster.
Wedothisbyautomaticallyfindingboththeclusteringandtheoptimalnumberoffeatures
throughasearchprocedure.InTraceBench,wesearchforthenumberofclustersintherange[3,
7].InABR,wesearchintherange[6,15],inCC,wesearchintherange[4,9]andintherange
[3,8]inLB.InFigures11and12,wevisualizetheclusteringfoundbyPlume.WeseethatPlume
effectivelygroupsandseparatestracesinallsixtracedatasets.

28 SagarPatel,JunyangZhang,SangeethaAbduJyothi,andNinaNarodytska
Fig.14. PerformancePlotsfromthePufferPlatform[2],presentingresultsfrom07Mar’2022—05Oct’2022.
Theresultsvisualize25.5steam-yearsofdata.Similarlytoourmainresults,weseethatGelato-Plume-Static
(maguro)outperformsallotherstate-of-the-artABRcontrollersinbothvideoqualityandstalling,andthat
Gelato-Random(unagi)improvesoverallvideoqualitywhileachievingsimilarstallingperformance.
B TRACEBENCHDETAILS
IndesigningTraceBench,ourobjectiveistocreateanenvironmenttothoroughlyevaluateand
validatedifferentprioritizationtechniques.
We build our environment on top of the standard ABR implementation found in the Park
Project[32].Weallowtheclienttohaveamaximumbufferof15seconds.Weconsidertraceswith
amaximumlengthof100seconds,withchunksof1second.Thechunksizesaregeneratedby
samplingaGaussiandistributionaroundthebitrates[1.0,3.0,6.0]megabytespersecond.
Whengeneratingthetraces,weconsidertwolevelsofthroughput,fastandslow,andtwolevels
ofvariance,high-varianceandlow-variance.Whengeneratingatrace,weusea2-stateMarkov
modelswitchingbetweenhighandlowthroughputwithdifferentswitchingprobabilitiesforeach
kind of trace. In Figure 13, we present a throughput vs. time visualization of each of the four
differentkindsoftraces.
WhentrainingthecontrollersinTraceBench,weusethestate-of-the-artfeed-forwardDQN
algorithmApe-XDqn[20].Weuseframestackingofhistorylength10.Weadditionallyuseastandard
reward normalization function [43] to normalize the rewards. We use the training parameters
definedinTable5.Weuseasimplefullyconnectedarchitecturewith2layersof256units.We
additionallyusetheduelinganddoubleDQNarchitecturewithahiddenfullyconnectedlayerof
256units.
C ADAPTIVEBITRATESTREAMINGDETAILS
InABR,weintroducethenovelcontrollerarchitectureGelato.
Gelato’sneuralarchitectureusesframe-stackingwith10pastvaluesfortheclientdata,and5
futurevaluesofchunksizesandSSIMsateveryencodedbitrate.Theclientdataispassedthrough
a1Dconvolutionwithakernelsizeof3and64filters,followedbyanother1Dconvolutionofthe
samekernelsizeandfilters.ThechunksizesandSSIMsareeachpassedthroughtheirown1D
convolutionwithakernelsizeof5and32filters,eachfollowedbyanother1Dconvolutionwith
thesamekernelsizeandnumberoffilters.Thesecondlayerofconvolutionsreducesthesizeof
theresultingoutputbyafactorproportionaltothesizeofthekernel.Theresultingfeaturesare

Plume:AFrameworkforHighPerformanceDeepRLNetworkControllers 29
| Hyperparameter        |     | Value       |
| --------------------- | --- | ----------- |
| Learningrate          |     | 0.001       |
| Numberofparallelenvs. |     | 64          |
| Numberoftrainingsteps |     | 4e8         |
| Updatehorizon(𝑡       | )   | 15env.steps |
𝑚𝑎𝑥
| GAEN-stepreturn                |     | 15            |
| ------------------------------ | --- | ------------- |
| 𝛾                              |     | 0.95          |
| Valuefunctioncoefficientinloss |     | 0.9           |
| Entropy                        |     | [5.75,0.0025] |
| Entropyannealinginterval       |     | 2e8steps      |
| MaxGradientNorm                |     | 0.4           |
Table2. Gelato’straininghyperparameters.Parametersleftunspecifiedfollowthedefaultonesprovidedin
Stable-Baselines3v2.0[44]fortheA2Calgorithm.
| Hyperparameter        |     | Value       |
| --------------------- | --- | ----------- |
| Learningrate          |     | 0.000125    |
| Numberofparallelenvs. |     | 16          |
| Numberoftrainingsteps |     | 5e6         |
| Updatehorizon(𝑡       | )   | 15env.steps |
𝑚𝑎𝑥
| GAEN-stepreturn                |     | 15          |
| ------------------------------ | --- | ----------- |
| 𝛾                              |     | 0.975       |
| Valuefunctioncoefficientinloss |     | 0.05        |
| Entropy                        |     | [0.1,0.005] |
| Entropyannealinginterval       |     | 2.5e6steps  |
| MaxGradientNorm                |     | 0.25        |
Table3. Aurora’straininghyperparameters.Parametersleftunspecifiedfollowthedefaultonesprovidedin
Stable-Baselines3v2.0[44]fortheA2Calgorithm.
concatenatedandpassedthroughapolicyandavaluenetworkeachmadeupofasinglehidden
layerof256neurons.Notethatthevaluenetworkisnotusedoutsideoftraining.Aninference
onGelato’sneuralnetworktakeslessthan0.35msonaverageonacoreofour𝑥86−64CPU
serverinPython—aminimalper-chunkoverheadforPuffer’s2.002secondchunkduration.Totrain
Gelato,weusetheA2Calgorithm[37]usingastandardrewardnormalizationstrategy[43]and
thetrainingparametersdefinedinTable2.
Theoff-policyDQNvariantofGelatousesthesamearchitecture,swappingthefinalpolicyand
valuenetworksforasingleduelingQ-networkmadeupofasinglehiddenlayerof256neurons.
Weadditionallyuseastandardrewardnormalizationfunction[43]tonormalizetherewards.To
trainthisvariantofGelato,weusetheApe-XDQNalgorthm[20]usingthetrainingparameters
definedinTable6.
WetrainPensieve[33]usingitsoriginalarchitecture.However,becausetheoriginalimplemen-
tationcouldonlyworkwiththetracesprovidedbytheauthors,toadaptPensievetonewtraces,
weusethesametrainingenvironmentandDRLparametersasGelato.
InpresentingtheresultsforGelatointherealworld,were-plotthedatafoundonthePuffer
Platform[58]inFigure6inSection6.Inouranalysis,wepresentthedatafromdates01Oct’2022

30 SagarPatel,JunyangZhang,SangeethaAbduJyothi,andNinaNarodytska
Hyperparameter Value
Learningrate 2e−4
Numberofparallelenvs. 16
Numberoftrainingsteps 5e6
BatchSize 256
GAE𝜆 0.975
AdvantageNormalization None
Nepochsperupdate 30
Valuefunctioncoefficientinloss 1e−4
Entropy [0.1,1e−6]
Entropyannealinginterval 5e6steps
ClipRange 0.1
MaxGradientNorm 0.2
Table 4. Load Balancing training hyperparameters. Parameters left unspecified follow the default ones
providedinStable-Baselines3v2.0[44]forthePPOalgorithm.
Hyperparameter Value
Numberofactors 4
Numberoftrainingsteps 4e6
Learningrate 7.5e−6
Replaybatchsize 32
𝛾 0.975
Replaybuffersize 250000
N-stepreturn 7
𝜖 annealinginterval 7e5steps
Valueclipping [-32,32]
Table5. TraceBenchtrainingparametersforApe-XDQN[20].Parametersleftunspecifiedfollowthedefault
onesprovidedinRLlibv0.13[28].
through01Oct2023.However,becausetheplatformwasexperiencingissuesandbenchmarking
otherABRcontrollers,thisdataissplitacrossmultipleplots.Toaggregatethedatatogether,wefirst
downloadthepre-processedpublicdataavailablefromthePufferWebsite[2].Second,wefollow
thesametechniqueusedbytheplatform,andemployasampling-basedapproachtoestimatethe
meanand95%confidenceintervalofquality,qualitychangeandstallingforeachABRalgorithm.
Weignoreallthedayswhentheplatformwasundermaintenance(suchas16January2023)and
dayswhentheplatformproducedfaultydataduetoaknownbuginthecode(suchas21January
2023).
Forcompleteness,wepresenttheolderresultsfromthePufferPlatforminFigure14benchmarking
theoriginalversionoftheFugucontroller,whichwastakenofftheplatformon06October2022.In
thisplot,weanalyze25.5stream-yearsofdata,collectedovertheperiod07March2022through
05October2022.WeobservethatGelato-Plume-Staticstilloutperformsthestate-of-the-artABR
algorithmsinbothqualityandstalling.ThisresulthighlightshowPlumecansuccessfullytrain
robustandhighperformantcontrollersinsimulation,evenoutperformingin-situtrainedcontroller
updateddaily.

Plume:AFrameworkforHighPerformanceDeepRLNetworkControllers 31
Hyperparameter Value
Numberofactors 64
Numberoftrainingsteps 1e9
Learningrate 7.5e−6
Replaybatchsize 128
𝛾 0.95
Replaybuffersize 2M
N-stepreturn 7
Valueclipping [-32,32]
Table6. Trainingparametersfortheoff-policyvariantofGelato.Parametersleftunspecifiedfollowthe
defaultonesprovidedinRLlibv0.13[28].
D CONGESTIONCONTROLDETAILS
InCC,wetrainandevaluateAurora[22]withdifferentprioritizationtechniques.Weuseframes-
tacking with a history length of 25. We use a 2-layer fully connected neural architecture with
64unitsforboththepolicyandvaluefunction.WeadditionallyuseState-Dependentnoisefor
exploration[45]andrewardscaling.WeusethetrainingparametersdefinedinTable3withthe
algorithmA2C[37].
E LOADBALANCINGDETAILS
InLB,weevaluatedifferentprioritizationtechniquesusingstandardparameters.Weusea2-layer
fullyconnectedneuralarchitecturewith[256,128]unitsandGeLUactivation[18]forboththe
policyandvaluefunction.Weadditionallyuserewardscaling,andthetrainingparametersdefined
inTable4withthealgorithmPPO[49].