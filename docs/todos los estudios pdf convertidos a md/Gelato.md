Practically High Performant Neural Adaptive Video
Streaming
SAGARPATEL,UniversityofCalifornia,Irvine,USA
JUNYANGZHANG,UniversityofCalifornia,Irvine,USA
NINANARODYSTKA,VMwareResearchbyBroadcom,USA
SANGEETHAABDUJYOTHI,UniversityofCalifornia,Irvine,USAandVMwareResearchbyBroadcom,
USA
Despiteofferingearlypromise,DeepReinforcementLearning(DRL)suffersfromseveralchallengesinadaptive
bitratestreamingstemmingfromtheuncertaintyandnoiseinnetworkconditions.However,inthispaper,we
findthatalthoughthesechallengescomplicatethetrainingprocess,inpractice,wecansubstantiallymitigate
theireffectsbyaddressingakeyoverlookedfactor:theskewedinputtracedistributioninDRLtraining
datasets.
Weintroduceageneralizedframework,Plume,toautomaticallyidentifyandbalancetheskewusinga
three-stageprocess.First,weidentifythecriticalfeaturesthatdeterminethebehaviorofthetraces.Second,
weclassifythetracesintoclusters.Finally,weprioritizethesalientclusterstoimprovetheoverallperformance
ofthecontroller.WeimplementourideaswithanovelABRcontroller,Gelato,andevaluatetheperformance
againststate-of-the-artcontrollersintherealworldformorethanayear,streaming 59stream-yearsof
televisiontoover280,000usersonthelivestreamingplatformPuffer.GelatotrainedwithPlumeoutperforms
all baseline solutions and becomes the first controller on the platform to deliver statistically significant
improvementsinbothvideoqualityandstalling,decreasingstallsbyasmuchas75%.
CCSConcepts:•Networks→Applicationlayerprotocols.
AdditionalKeyWordsandPhrases:VideoStreaming,DeepReinforcementLearning
ACMReferenceFormat:
SagarPatel,JunyangZhang,NinaNarodystka,andSangeethaAbduJyothi.2024.PracticallyHighPerformant
Neural Adaptive Video Streaming. Proc. ACM Netw. 2, CoNEXT4, Article 30 (December 2024), 23 pages.
https://doi.org/10.1145/3696401
1 INTRODUCTION
Video streaming is the prominent Internet application, accounting for over 75% of the entire
traffic[14].Despitethis,deliveringhighqualityvideoovertheInternetcontinuestobechallenging,
primarilyduetothenoisyandhighlyunpredictablenetworkconditionsthevideoissentover[68,
71]. The primary approach to tackle this is to use Dynamic Adaptive Streaming over HTTP
(DASH)[57].Thisapproachdividesthevideointosmall,seconds-long,chunksandpre-encodes
thematmultiplebitrates.Then,duringstreaming,anAdaptiveBitrate(ABR)algorithmselectsthe
bitrateofeachchunk,adaptingtothenetworkconditionsandmaximizingthequalityofexperience.
Authors’ContactInformation:SagarPatel,UniversityofCalifornia,Irvine,USA,sagar.patel@uci.edu;JunyangZhang,
UniversityofCalifornia,Irvine,USA,junyanz9@uci.edu;NinaNarodystka,VMwareResearchbyBroadcom,USA,nina.
narodytska@broadcom.com;SangeethaAbduJyothi,UniversityofCalifornia,Irvine,USAandVMwareResearchby
Broadcom,USA,sangeetha.aj@uci.edu.
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalorclassroomuseisgrantedwithoutfee
providedthatcopiesarenotmadeordistributedforprofitorcommercialadvantageandthatcopiesbearthisnoticeand
thefullcitationonthefirstpage.Copyrightsforthird-partycomponentsofthisworkmustbehonored.Forallotheruses,
contacttheowner/author(s).
©2024Copyrightheldbytheowner/author(s).
ACM2834-5509/2024/12-ART30
https://doi.org/10.1145/3696401
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

30:2 SagarPatel,JunyangZhang,NinaNarodystka,andSangeethaAbduJyothi
Recentworkhasshownthepotentialofdata-drivenmachinelearningapproachestoABR[9,
58,65,70]insurpassingtraditionalheuristic-basedmethods[24,56,67].Thesetechniquesconsist
oftwomaincomponents:amachinelearningmodelthatpredictsfuturenetworkconditions(e.g.,
atransmissiontimepredictor)andaplanningalgorithmthatusesthesepredictionstoselectthe
optimalbitrate(e.g.,adynamicprogrammingalgorithm).Whilethesetechniquesaretheoretically
optimalwithaccuratepredictors,achievingsuchperformanceisdifficultduetotherequirements
oftheplanningcomponentandthecomplexitiesinmodelingtheInternet(§3.1).
DeepReinforcementLearning(DRL)offersapromisingapproachtoovercomingtheselimitations
byusingafundamentallydifferentmechanismfordata-drivendecision-making.Insteadofmodeling
theInternetandusingpredictionstoselectbitrates,DRLdirectlylearnsthebitrateselectionstrategy
byiterativelyoptimizingapolicy [59].Thisinvolvesevaluatingthecurrentpolicy,performing
actionstogatherstatesandrewards,andoptimizingittomaximizeselectingbitratesthatleadto
higherrewards.Thisapproachbypassestheneedtoaccuratelypredicttheoutcomeofsending
everybitrate,presentinganaturalwayoutofthecurrentgapsinInternetmodeling.
However,despitethepromiseofthepathpresentedbyDRL,obtaininghighreal-worldperfor-
manceinABRremainschallengingforDRL[36].ThisisbecauseinABR,unliketraditionalDRL
environmentssuchasgamingorrobotics,thereexistsanunpredictableunderlyinginputprocess:
thewide-areaInternet.Thisprocessisformallycalledan“inputprocess”[39].Duringtraining,
the inputs are replayed using a dataset of input traces, or system logs. Such input-driven DRL
environmentshaveseveralcharacteristicsthatmakeDRLtrainingdifficult.First,trainingininput-
drivenRLenvironmentsisinefficient,requiringasignificantnumberofiterations[37].Second,the
dependenceonexternalinputssuchasnetworkconditionsintroduceshighlevelsofuncertainty
andnoise[39].Thesechallengestogethermaketraininghighlynon-trivial,causingseveralprior
work[36,37,65]toconcludethataddressingthemwasessentialforreal-worldperformance.
Ouranalysisrevealsakeyoverlookedfactorbehindthesechallenges:theskeweddistributionof
inputtracesintrainingdatasets.Thisskewresultsinlimitedtrainingonrareortail-endtraces
andintroducesnoiseinlearningduetoupdatesbasedonanarrowsetoftraces.Consequently,the
performanceonthesetail-endtracesisoftensuboptimal,unliketheheavilyoptimized“common”
traces.However,focusingontheperformanceofthetail-endtracesisvitalfordata-drivencontrollers
inimprovingtheoverallperformanceoverbaselines[27].Unfortunately,suchskewisprevalent
inABR.Forexample,overan8-monthperiodonthevideostreamingplatformPuffer[65],low-
bandwidthinputtracesmadeuplessthan20%ofthetotal,withonly4%experiencinganystalls.
Therefore,addressingskewisessentialfor(a)mitigatingamplifiedlearningchallengesand(b)
improvingoverallcontrollerperformance,acrossboth“common”andtail-endinputtraces.
Whiletechniquesforaddressingdataskewareprevalentinvariouscontexts[16,18,31,34,44,
51,69],standardsupervisedlearningsolutionssuchasoversamplingorundersamplingspecific
labeledclassesdonotapplytoReinforcementLearning,wherethecontrollerlearnsusingstates,
actionsandrewards(§9).ThefewsolutionsdesignedspecificallyforDRLareinadequateforABR
controllersbecausetheyfailtocapturethetrace-centricnatureoftheproblem(§3.3).Thus,to
effectivelyaddressthisskew,weintroduceanovelapproachtargetingtheinputtraces.
Inputtraces,whichrepresentlogsoftime-dependentcomplexprocesses,lackaconventional
mechanismtoidentifyandbalancetheskewwith.Thesetraceshavenofeaturesorlabelsanddo
notdirectlycontributetoalossfunction.Thus,amechanismtoidentifyandbalancetheskew
in input-driven environments is needed. To do so, in this work, we introduce a generalizable
framework,Plume.Plumeemploysanautomatedthree-stageprocess.CriticalFeatureIdentification:
Weautomaticallydeterminethecriticaltracefeaturestoidentifythetraces.Clustering:Weemploy
clusteringtoconvertthecriticalfeaturesintosalientidentifiers.Prioritization:Inthisstage,we
prioritizetheclusters,suchastoexposethecontrollertotraceswhereitcanlearnthemost(§4).
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

PracticallyHighPerformantNeuralAdaptiveVideoStreaming 30:3
WeevaluateourideaswithGelato,anovelABRcontroller.TrainedwithPlume,Gelatooffers
SOTAperformanceonthereal-worldstreamingplatformPuffer[65],streaming59stream-years
ofliveTVtoover280,000users[2,65]inayear.Itisthefirstcontrollerontheplatformtoshow
statisticallysignificantimprovementsinbothvideoqualityandstalling.Itoutperformsprevious
SOTAdata-drivencontrollers,CausalSim[10]andFugu[65],reducingstallsby75%and78%.
ToassessthegeneralizabilityofPlume,weevaluateitsperformanceonvariousnetworktrace
distributionsandintwootherapplications,CongestionControlandLoadBalancing.Tofacilitate
this evaluation, we introduce TraceBench, a simplified ABR environment with parametrically
generatedtracestocreatediversetesttracedistributionsinacontrolledandprecisemanner.Using
it, we demonstrate Plume’s dynamic performance across controllers, environments, and trace
distributions(§7).
Insummary,wemakethefollowingcontributions:
• WesystematicallystudyanoverlookedaspectofDRLtraining—skeweddatasets—andfindthat
theycanhaveasurprisinglylargeimpactonperformance.
• WeproposePlumeasageneralizableframeworkforhandlingskeweddatasetsandimproving
theperformanceofDRLcontrollersinVideoStreaming.
• WeintroduceGelato,anewABRcontroller.Plume-trainedGelato,deployedonthereal-world
Pufferplatform[65]formorethanayear,isthefirstcontrollerwithsignificantimprovementsin
bothvideoqualityandstalling,reducingstallingby75%overthepreviousstate-of-the-art.
• WedemonstratethegeneralizabilityofPlume,acrossdifferentdistributionsofnetworkconditions
anddifferentnetworkingapplications.
Thisworkdoesnotraiseanyethicalconcerns.
2 BACKGROUND
Inthissection,wegiveabriefoverviewofreinforcementlearningandadaptivebitratestreaming.
2.1 ReinforcementLearningPreliminiaries
In Deep Reinforcement Learning (DRL), an agent interacts with an environment, receiving the
currentsystemstate𝑠
𝑡
ateachtimestepandtakingaction𝑎
𝑡
frompolicy𝜋(𝑎|𝑠 𝑡).Theenvironment
transitionstostate𝑠
𝑡+1
postaction,awardingagentreward𝑟
𝑡
[7,55,59].
Innetworkenvironments,non-deterministicnetworkconditionsareprimarysourcesofnoise
anduncertainty.Theseconditionsdeterminetheenvironment’sresponsetothecontroller’sactions.
E.g.inadaptivebitratestreaming,externalnetworkconditionsdictatewhetherastalloccurs.
Formally,theseconditionsarecalled“inputs”,andinput-drivenenvironmentsformanInput-
DrivenMarkovDecisionProcess[39],definedby(𝑆,𝐴,𝑍,𝑃
𝑠
,𝑃
𝑧
,𝑟,𝛾).Here,𝑆 isthestateset,𝐴the
actionset,𝑍 thetraininginputtraces,𝑃 and𝑃 thestateandinputtransitionfunctions,𝑟 thereward
𝑠 𝑧
function,and𝛾 thediscount.Thestatetransitionfunction𝑃 𝑠(𝑠 𝑡+1|𝑠
𝑡
,𝑎
𝑡
,𝑧 𝑡+1)definestheprobability
distributionofthenextstate𝑠 giventhecurrentstate𝑠 ,action𝑎 ,andupcominginput𝑧 .
𝑡+1 𝑡 𝑡 𝑡+1
Meanwhile,theinputtransitionfunction𝑃 𝑧(𝑧 𝑡+1|𝑧 𝑡)definestheprobabilityofthenextinputvalue
basedoncurrent,leadingtoaneffectivetransitionfunctiongivenby𝑃 𝑠(𝑠 𝑡+1|𝑠
𝑡
,𝑎
𝑡
,𝑧 𝑡+1)𝑃 𝑧(𝑧 𝑡+1|𝑧 𝑡).
TheDRLlearningprocessaimstoguidethepolicy𝜋 towardshighercumulativerewardthrough
aloopinvolvingtwosteps:apolicyevaluationstepandapolicyimprovement step[23].Inpolicy
evaluation,theagentassessesitspolicybygainingexperiencethroughactingintheenvironment
andusingitinfunctionlearning.Itupdatesitsneuralnetworktolearnvaluefunction𝑣𝜋(𝑠) =
E 𝜋[𝐺|𝑠 0 = 𝑠], the expected return𝐺 from state𝑠, where𝐺 is the discounted reward sum𝐺 =
(cid:205)∞ 𝛾𝑡𝑟 .Next,inpolicyimprovement,theagentalters𝜋 tomaximize𝑣𝜋,iterativelylearningby
𝑡=0 𝑡
estimatingandmaximizingthevaluefunction.
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

30:4 SagarPatel,JunyangZhang,NinaNarodystka,andSangeethaAbduJyothi
Fig.1.PufferInputTracedistri-
bution:DistributionofPuffertrace
effectivethroughputfromApr’21- Fig.2.ComparingPrioritizationTechniques:Evaluatingtransition
May’21.Under6.5%oftracesare sampling(PERon/off)versustracesampling(Randomvs.2-Class
belowthehighestqualityvideo’sav- Equal Weighted) using Ape-X DQN [23]. 2-Class Equal Weighted
eragebitrate.EachstreaminPuffer TraceSelectionexcelsinperformanceandtrainingefficiency,unlike
isconsideredatrace. PER.Errorbandsrepresent95%confidenceinterval.
On-policyandOff-policyDRL.DRLalgorithmsarebroadlydividedintotwocategoriesbasedon
theirpolicyevaluationstages.On-policyRLalgorithmsredopolicyevaluationeachiteration,using
datafromthelatestpolicy[59].Thesealgorithmshavefoundwideuseinnetworking[26,35,38].
Off-policyRLalgorithmspartiallyuseoldpolicydataforbetterefficiency.Theymaintainawindow
ofenvironmenttransitions,describedbythetuple(𝑠
𝑡
,𝑎
𝑡
,𝑟
𝑡
,𝑠 𝑡+1),inaFIFObuffercalledExperience
Replay[42].Off-policyalgorithmsaresimilarlypopularinnetworking,asusedby[6,64].
2.2 AdaptiveBitrateStreaming
In HTTP-based video streaming, the video is divided into chunks and encoded, in advance, at
multiple discrete bitrates. During streaming, the most appropriate bitrate is chosen per chunk
based on network conditions. The client also has a short buffer that can hold received chunks
thathavenotbeenviewedyet.TheABRalgorithmisresponsibleforsequentiallyselectingthe
videobitrateonachunkleveltomaximizetheviewer’sQualityofExperience(QoE).Typically,the
QoEismeasuredwithanumericalfunctionthatawardshigherquality,andpenalizesbothquality
fluctuationsandrebuffering.Thequalitymaybedefinedbytheencodedbitrateorbycomplex
measuressuchasStructuralSimilarityIndexMeasure(SSIM)[61].
3 MOTIVATION
WediscusswhyDeepReinforcementLearning(DRL)isusedforABRandthechallengeofskewed
trainingdatasets.Wethenoverviewcurrenttechniquesandtheneedforprioritizedtracesampling.
3.1 WhyuseDRLforAdaptiveBitrateStreaming
Severaldata-drivencontrollersforAdaptiveBitrateStreamingexisttoday[9,58,65,70].These
buildonclassicalcontrollerslikeMPC[67],withamachinelearningpredictorreplacingheuristics
liketheharmonicmean.Theyincludetwocomponents:themachinelearningpredictorforfuture
networkconditionsandtheplanningalgorithmforbitrateselection.
Withanaccuratepredictor,thesetechniquesaretheoreticallyoptimal.However,practicalper-
formanceislimitedbydifficultiespredictingInternetbehavior[17,46].Theplanningcomponent
needsaccuratepredictionsforallbitratesineverycondition,butpredictionsforrarelychosen
bitratescanbeinaccurateduetotheirout-of-distributionnature[10].Additionally,planningoften
involvesmultiplefuturechunks,compoundingpredictionerrorsovertimeascurrentpredictions
areusedforfutureones(e.g.,predictedbufferusedasstartingpointforthenextchunk)[25,32].
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

PracticallyHighPerformantNeuralAdaptiveVideoStreaming 30:5
DeepReinforcementLearning(DRL)overcomesthesechallengeswithafundamentallydifferent
data-drivendecision-makingprocess.InsteadofpredictingInternetbehaviorandthenselectingbi-
trates,DRLlearnsbitrateselectionthroughaloopbetweenpolicyevaluationandimprovement[59],
iterativelyoptimizingtheviewer’sexperience.Akeyadvantageisthatitonlyconsidersbitrates
similartothosealreadychosenbythepolicy[42].Additionally,itreliesonabootstrapofaggregated
performanceratherthanpreciselyneedingoutcomesforfuturechunks[22,42].Theseadvantages
makeDRLpromisingforABRwhiletheresearchcommunitycatchesuponInternetsimulation.
3.2 ChallengeswithDRLTraining
HavingestablishedthepromiseofDRLforvideostreaming,wenowdiscussitschallenges.
Challenge1:Inefficientexploration.Ininput-drivenenvironments,mostofthestate-action
space shows little reward feedback difference [37]. Standard exploration techniques, selecting
randomactionswith𝜖 probabilityandfollowinggreedyactionsotherwise,havealowchanceof
findingasuccessfulpolicyandrequiremanytrainingiterations.Theimbalanceintrainingdatasets,
especiallytheunder-representationofraretraces,exacerbatesthiscomplexity.Suchtracesarerarely
encounteredbythecontroller,limitingitsopportunitytodiscoversuccessfulstrategiesforthem.
However,performanceinthesetail-endtracescanbecrucialforhigheroverallperformance[27].
Challenge2:NoiseandUncertainty.Networkconditions,orinputs,determinetheenvironment’s
behaviorandarethemainsourceofuncertainty.Forinstance,whenanABRcontrollerchoosesa
bitrate,itlacksknowledgeoftheclient’slinkbandwidth.Thisunobservedfactordirectlyimpacts
theclient’swaittimeforthechunk.Suchvariabilityintroducesnoiseintothelearningprocess,
causingidenticalstatestoyieldwidelydifferentoutcomesbasedonnetworkconditions[39].This
noise is amplified when network trace distribution is skewed. In these cases, a single training
iterationmaynotrepresentthefullspectrumofinputtraces,leadingtodivergentornoisyupdates.
OtherChallengeswithskew.Skewinthedistributionofinputtracespresentschallengesduring
the function learning phase of DRL training (§ 2.1). Since states are dependent on these input
traces,askewedinputdistributionleadstoaskewedstatedistribution.Thisimbalanceinthestate
distributiondegradestheneuralnetworkperformance,makingitvulnerabletooverfitting[28,66].
3.3 TowardsPrioritizingTraceSampling
Next,wediscusspriorMLtechniquesforhandlingskewandshowtheneedforanewapproach.
PrioritizedExperienceReplay(PER).Off-policyDRLalgorithmsuseabuffertostorepaststate
transitionsandapplyPrioritizedExperienceReplay(PER)[51]tosamplethemduringfunction
learning.PERemploysprioritization,alsoknownasimportancesampling,toselectstatetransitions
basedontheirTemporalDifferenceerror,focusingontransitionswithhighererrortoimprovethe
controller’spredictionswheremostneeded.
WhilePERiseffectiveintraditionalDRLsettings[22,23],itislimitedininput-drivenenviron-
ments.PERaddressesstateskewinthefunctionlearningphase,butinputtraceskewaffectsthe
acting phase (§2.1). The controller haslimited opportunitiesto act intail-end traces. Without
modifyingtraceselectionduringtheactingphase,PERcannotincreaseexplorationintail-end
tracesorensurecomprehensiveevaluationacrosstheentiretracedistribution.
PrioritizedTraceSampling.WereexaminetheDRLworkflowandidentifyabetterlocation
forprioritization.Weproposeasimpletrainingparadigmininput-drivenenvironments:prioritiz-
ingtracesamplingduringtheactingstep.Thisachieveshighstate-actionspaceexplorationand
representativeevaluationonalltracetypes.
Totestourhypothesis,weenableprioritizationattwopointsintheDRLworkflow:sampling
transitionsintheexperiencebufferatthefunctionlearningstep(PERenabledvs.disabled)and
samplinginputtracesintheactingstep(Randomsamplingvs.2-ClassEqualWeighted).2-Class
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

30:6 SagarPatel,JunyangZhang,NinaNarodystka,andSangeethaAbduJyothi
Fig.3. PlumeSystemDiagram:ThePlumeWorkflowinvolvesthreekeystages:(1)CriticalFeatureIden-
tification,wherewecharacterizethetracesandtheirskew,(2)Clustering,wherewetrytosimplifythe
prioritizationproblembygroupingtraces,(3)Prioritization,whereweprioritizeimportanttraceclusters.
EqualWeightedisasimpleinputtraceprioritizationschemethatdividestracesintotwoclasses,
thosewithmeanthroughputhigher/lowerthan0.98Mbps(Figure1),andsamplesbothclasses
equally.Weevaluateeachtechnique’simpactonaDQNvariationofGelatocontrollerforABR,
trainedusingtheApe-XDQNalgorithm[23](trainingsettingsdetailedin§5and§6.2)
InFigure2,weobservethatthesimple2-ClassEqualWeightedgivesthehighestperformanceand
trainingstability.Byprioritizingtail-endslowthroughputtraces,weachievehighperformancein
bothallandslownetworktraceswithoutcompromises.EnablingPERdoesnotimproveperformance,
eventhoughthereplaybuffercanstore2Mtransitions(over5000traces).PER’sperformancefalls
shortofthenaivetraceprioritizationscheme.Thishighlightsthattracedistributionskewcannot
beovercomeatthefunctionlearningstep.
4 DESIGN
TowardimprovingtheperformanceofDRLtrainingbybalancingskew,weputforwardtheidea
thattraceselectionistheaptestlocationforprioritization.
Tobalancetheskewduringtraceselection,wetakeadvantageofakeyobservation:inputtraces
inherentlycorrespondtousersorworkloads,withgroupsofthemsharingsimilarcharacteristics.
Toensureabalancedrepresentationoftheunderlyingusers,thedatasetmustcontainaroughly
uniformnumberofinputtracesacrossthem.Wedefineinputtracestohaveasetofuserattributes
Φ= [𝜙
1
,𝜙
2
,...]givenbythefunctionΦ=𝑋(𝑡𝑟𝑎𝑐𝑒),where𝑋 dependsonthedomain.Thesefeatures
identifysimilaritiesbetweenusertraces,andplayakeyroleinbalancingtheskew.
Plumeisasystematicframeworktoautomaticallybalancethisskewininputtraces.Plumeallows
theagenttohavebalancedexplorationandstablelearningupdates.Figure3givesanoverviewof
thePlumeworkflow.PlumeisimplementedintheTraceSelectionmodulewhichisresponsible
forsupplyingtracestothesimulationenvironment.ThismodulesitsoutsideoftheDRLtraining
loopandisqueriedbytheenvironmenttogettracestoreplay.Plumehasthreekeystages:critical
featureidentification,clustering,andprioritization.
Inthecriticalfeatureidentificationstage(§4.1),Plumeidentifiestheattributesoftheinputtraces.
Intheclusteringstage(§4.2),itsimplifiestheprioritizationproblembyclusteringtheattributes.
Finally,inthePrioritization(§4.3)stage,Plumeprioritizesthetracestobalanceinputtracesusing
oneoftwotechniques:staticordynamic.
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

PracticallyHighPerformantNeuralAdaptiveVideoStreaming 30:7
4.1 CriticalFeatureIdentification
Inputtraces,whicharetime-dependentseriesofvaluesthatdefinecomplexexternalconditions,can
beincrediblydifficulttocharacterizeandprioritizedirectly.Hence,thefirststeptowardsautomated
prioritizationoftracesisidentifyingtheattributesΦusingcriticalfeatureidentification.
Toextractallfeaturesofthetimeseriestracedata,werelyonthepopularfeatureextraction
toolforthetimeseriesdata,tsfresh[13].Weextractalargesetoffeatures [𝜙 1 ,𝜙 2 ,...𝜙 𝑛] broadly
applicabletoallinput-drivenDRLenvironments,suchastruncatedmean,ratioofvaluesbeyond
acertainstandarddeviation,meanabsolutechange,orautocorrelation.Forthefulllistofthese
features,seeAppendixA.However,becausethislargesetoffeaturesmaynotberelevanttoevery
application,weintroduceanautomatedthree-stepprocesstonarrowdowntothecriticalones,
inspiredbyrecursivefeatureeliminationinsupervisedlearning[4].
First,westartwiththelargefeaturesetandapplyclusteringtocreateasmallnumberofclusters.
Thisisdenotedby𝑐 =𝐶([𝜙
1
,𝜙
2
,...𝜙 𝑛]),where𝑐istheclusterlabels,and𝐶istheclusteringfunction.
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
thatthefinalfeaturesetissufficientlyexpressive.Wenotethatthisprocess,whileempirically
performant,isimperfectandcanbeimprovedwithexpertknowledgeofthefeatures.
Notethattheclusteringatthisstageissolelyforfeatureselectionandhasnoimpactonthe
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
ofanother.Toaddressthis,weclusterthetracestoobtainasingledistributiontobalance.Weuse
aclusteringalgorithm𝐶 toobtainthelabels𝑐 sothatthemappingagainbecomes𝑐 =𝐶(Φ).By
doingso,wecreatearankingfunctionthatallowsustoinsteadprioritizeacategoricaldistribution
ofinputtraces,wheretheclusterlabelsactasthecategories.Werepresentthisdistributionas𝑦,
where𝑦 isacategory,orsalienttraceclusterwithinit.
𝑖
Toclusterthetraces,weemployGaussianMixtureModels(GMM)withKmeans++[47].Gaussian
Mixture Models use a generalized Expectation Maximization algorithm [1] and can effectively
dealwiththelargevariationsfoundininputdata.NotehereGMMsmustalsobalancethenumber
ofclusterswiththevariationtoensurethatprioritizationdoesnotcollapsethedistribution.We
balancethisbyconductingasearchforthenumberusingSilhouettescores[5].Thisentireclustering
processcanaddaone-timeoverheadintheorderofminutes.
WevisualizetheclusteringofPuffertracesautomaticallyproducedbyPlumeinFig.4wherewe
plottheclustersacrosstwoidentifiedcriticalfeatures.Itproducesminimalclusterswhileseparating
salientcharacteristicssuchasmeanandvariationinthroughput.Notethattheratioofthroughput
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

30:8 SagarPatel,JunyangZhang,NinaNarodystka,andSangeethaAbduJyothi
beyond2.5stdisameasureofvariationthatcalculatestheproportionofthetracethatliesbeyond
2.5×standarddeviationofthemeanwithinthattrace.score[5].
4.3 Prioritization
Withcriticalfeatureidentificationandclusteringstagescomplete,wehaveacategoricaldistribution
ofinputtraces𝑦thatwecanbalancebyprioritization.
Sofar,wehavediscussedbalancingthedistribution𝑦.Whilethiscanbedoneinanumberof
ways,toensurethatthebalancingleadstomeaningfulperformanceimprovements,weintroducea
targetfunctiontobalancethedistributionaround:“reward-to-go”.Reward-to-gorepresentsthe
additionalrewardsthatacontrollercanstillachieve.ThiscanbeformallydefinedbyEquation1:
|     | Δ𝐺 =E | [𝐺𝜋∗ −𝐺𝜋𝜃 ] |     | (1) |
| --- | ----- | ----------- | --- | --- |
𝑦𝑖 𝑦𝑖
In this equation,𝑦 is a category (§ 4.2) in the input trace distribution𝑦,𝐺 (cid:205) ∞ 𝛾𝑡𝑟 is the
| 𝑖   |     |     | = 𝑡 =0 𝑡 |     |
| --- | --- | --- | -------- | --- |
discountedreturnofthetraceasdescribedinSection2.1,𝐺𝜋∗ isthereturnundertheoptimalpolicy
𝜋∗,and𝐺𝜋𝜃 isthereturnunderthecurrentpolicy.Weaimtobalancetheinputtracedistribution
basedonhowsuboptimallythecurrentpolicyperforms,ensuringauniformgapacrossalltraces.
Inotherwords,weseektoensurethattargetfunctionΔ𝐺 Δ𝐺 forallcategories𝑦 and𝑦 .
|     |     | 𝑦𝑖 = 𝑦𝑗 | 𝑖   | 𝑗   |
| --- | --- | ------- | --- | --- |
However,calculatingreward-to-goisoftennotpossibleinreal-worldsituationsbecauseitdepends
onvariablessuchasstatefeatures,andcanrequiresolvinganNP-hardproblem[40].Inthiswork,
weintroducetwostrategiestoapproximatethisprioritization:StaticandDynamic.
StaticPrioritization.Inthisapproach,wetackleskewbystaticallybalancingthedistributionof
inputtraces.Specifically,weadjustthesamplingweightstobetheinverseofthedistribution𝑦,as
expressedinEquation2:
1
|     | 𝑊   | =      |     | (2) |
| --- | --- | ------ | --- | --- |
|     | 𝑦𝑖  | 𝑓(𝑦 𝑖) |     |     |
Here,𝑊 signifiestheprioritizationweightforcategory𝑦 ,and𝑓(𝑦 𝑖)istheoriginalprobability
𝑦𝑖 𝑖
densityfunctionforthecategoricaldistribution𝑦.Whenwesampleaccordingtotheseprioritization
weights,wemodifytheeffectiveprobabilitydensityfunction,whichnowbecomes
𝑊 𝑓 𝑦
𝑦 ( 𝑖)
|     | 𝑓′(𝑦 𝑖) = | 𝑖 .        |     | (3) |
| --- | --------- | ---------- | --- | --- |
|     | (cid:205) | 𝑊 𝑓 (𝑦     |     |     |
|     |           | 𝑦𝑘 ∈𝑦 𝑦 𝑘) |     |     |
𝑘
WhilethereexistsnoanalyticalwaytocomputeΔ𝐺 ,insomecases,wecanshowthatstatic
𝑦𝑖
prioritizationeffectivelybalancestheskew.First,considerthatunderrandomtracesampling,the
imbalancecanbearbitrarilylarge:
Proposition4.1. Let𝐿beaconstantand𝑦beacategoricaldistributionofinputtraces.Suppose
|     | Δ𝐺 𝑦𝑖 | 𝑓(𝑦 𝑗) |     |     |
| --- | ----- | ------ | --- | --- |
≈ ,
|     | Δ𝐺 𝑦𝑗 | 𝑓(𝑦 𝑖) |     |     |
| --- | ----- | ------ | --- | --- |
thenthereexistsadistributionoftraces𝑦suchthat
|     | Δ𝐺  | 𝑦𝑖  |     |     |
| --- | --- | --- | --- | --- |
≥𝐿.
Δ𝐺
𝑦𝑗
Proof. Consideradistributionwithtwocategorieswhere
|          | 1   |                    | 𝐿   |     |
| -------- | --- | ------------------ | --- | --- |
| 𝑓(𝑦 1) = | and | 𝑓(𝑦 2) =1−𝑓(𝑦 1) = | .   |     |
|          | 1+𝐿 | 𝐿+1                |     |     |
Fromtheabove,itfollowsthat
|     | Δ𝐺  | 𝑦1  |     |     |
| --- | --- | --- | --- | --- |
≈𝐿.
Δ𝐺
𝑦2
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

PracticallyHighPerformantNeuralAdaptiveVideoStreaming 30:9
□
However,usingstaticprioritization,thisimbalancenolongerexists:
Proposition4.2. Let𝑦′
denotethere-weightedcategoricaldistributionofinputtraces.Suppose
|     |     | Δ𝐺 ′ 𝑓′(𝑦 |     |     |     |
| --- | --- | --------- | --- | --- | --- |
|     |     | 𝑦         | 𝑗)  |     |     |
|     |     | 𝑖 ≈       | ,   |     |     |
|     |     | Δ𝐺 ′ 𝑓′(𝑦 |     |     |     |
|     |     | 𝑦         | 𝑖)  |     |     |
𝑗
then
|     |     | Δ𝐺′ ≈Δ𝐺′ | .   |     |     |
| --- | --- | -------- | --- | --- | --- |
𝑦𝑖 𝑦𝑗
Proof. Fromthegivencondition,wehave
(cid:205)
| Δ𝐺 ′ | 𝑓′(𝑦 𝑗) | 𝑊 𝑦𝑗 𝑓(𝑦 𝑗) | 𝑊 𝑦𝑘 𝑓(𝑦    | 𝑘)  |     |
| ---- | ------- | ----------- | ----------- | --- | --- |
| 𝑦 𝑖  |         |             | 𝑦𝑘∈𝑦        | =1. |     |
|      | ≈ =     |             | · (cid:205) |     |     |
| Δ𝐺 ′ | 𝑓′(𝑦 𝑖) | 𝑊 𝑦𝑖 𝑓(𝑦 𝑖) | 𝑊 𝑦𝑘 𝑓(𝑦    | 𝑘)  |     |
| 𝑦 𝑗  |         |             | 𝑦𝑘∈𝑦        |     |     |
□
Giventhesepropositions,itisevidentthatunderstaticprioritization,irrespectiveoftheinitial
Δ𝐺′𝑦𝑖
inputtracedistribution,therelativereward-to-goratio isclosetoone,whilethisratiocan
Δ𝐺′𝑦𝑗
belargeunderrandomtracesampling.Forbothpropositions,anunderlyingassumptionisthat
theratio Δ𝐺𝑦𝑖 isapproximatelyequaltotheinverseoftheratioofprobabilitydensitiesforthe
Δ𝐺𝑦𝑗
relevantcategories.Thisassumptionrestsontheobservationthatthemeanlossreductionused
inoptimizingthecontrollerisexpectedtoaccruelargererroronthespacelessrepresentedinits
samples.Consequently,thereward-to-gogapdecreaseswithincreasingsamplingprobability.
DynamicPrioritization.Indynamicprioritization,wecomputeanapproximationofreward-to-go
thatadaptstothetrainingprocess.Reward-to-goofacategorycanvaryasthetrainingprogresses,
andhence,theextentofprioritizationneededforacategorycandifferacrosstraining.
| Δ𝐺 =E | [𝐺𝜋∗ −𝐺𝜋𝜃 | ]   |     |     |     |
| ----- | --------- | --- | --- | --- | --- |
𝑦𝑖 𝑦𝑖
[𝐺ˆ (Φ)−𝐺𝜋𝜃
| Δ𝐺 ≈E |     | ]   | Approximatepolicy |     | (4) |
| ----- | --- | --- | ----------------- | --- | --- |
𝑦𝑖 𝑦𝑖
| Δ𝐺 ≈E | [𝐺ˆ (Φ)−𝐺𝜋𝜃 | ]−E | [𝐺𝜋𝜃             |     |     |
| ----- | ----------- | --- | ---------------- | --- | --- |
| 𝑦𝑖    | 𝑦𝑖          | 𝑦𝑖  | ] Compensatebias |     |     |
Astheoptimalreturncannotbecalculated,wereplacethereturn𝐺𝜋∗
withthelearnedexpected
return𝐺ˆ (Φ).𝐺ˆ isafunctionapproximatortrainedalongsidecontrollertrainingandexplorationto
mapthetraceattributesΦtotheobservedreturnobtainedbasedonarollingset.Thedifference
fromthislearnedestimateservesasameasureforimprovementyettobeachievedbythecontroller.
However,becausethisestimateisbasedonthereturnsamplesseensofar,thisapproximation
canbepessimisticandrequireanexplicitoptimismcompensation.Toaddressthisconcern,we
introducethesecondterm,−E [𝐺𝜋𝜃 ],whichgivesprioritytotracesthathavelowreturns.
𝑦𝑖
ThedynamicweightsareproportionaltothenormalizedsumofcomponentsofΔ𝐺 (Eq.4).
𝑦𝑖
NotethattheprioritizationisoutsidetheDRLalgorithm’strainingloopinTraceSelection(Fig.3).
5 GELATO
WeintroduceGelato,anovelABRcontrollerarchitecture.UnlikesimplerDRLenvironments,ABR
benefitsfromthisnewarchitecture,enhancingtrainingefficiencyandperformance.Asshownin
Section6,combiningGelatowiththePlumeframeworkyieldsacontrollerthatcanoutperformall
existingABRcontrollersinreal-worldandsimulatedsettings.RefertoFigure5foranoverview.
Rewards.WeoptimizeforSSIM,usingrewardcoefficientsfromFugu[65](+SSIM,−stalls,−ΔSSIM).
WeutilizevideochunksizesandSSIMvaluesfromPuffer’spubliclogs.Rewardsarenormalized
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

30:10 SagarPatel,JunyangZhang,NinaNarodystka,andSangeethaAbduJyothi
Fig.4.ClusteringVisualization:We Fig.5.ArchitectureofGelato:Gelatotakesasinput
showtheclusteringproducedbyPlume. complexfeaturesofthevideostream.
using𝑟 :𝑠𝑖𝑔𝑛(𝑟)( √︁ |𝑟|+1−1)+𝜖𝑟 andclipping,with𝜖 = 10−2.Thisnormalization,empirically
effectiveforvaried,large-scalerewards[48],mitigatestheimpactofextremerewardvalues.
Features.Gelatoemployscomprehensiveapplication-levelfeatures,includingclientbufferand
pastrewardshistory,andalongerhistoryofstallsover30chunks,aggregatedevery3chunks.This
approachenhancesthecontroller’sadaptabilitytonetworkconditions.UnlikeFugu,Gelatoomits
low-levelTCPstatistics,yetsimilarlyutilizestransmittimeandthesizesandSSIMsofupcoming
chunks,availableduetochunksbeingpre-encodedinABR.
Neural Architecture. Gelato’s neural network is optimized for efficiency, featuring an extra
convolutionallayertodownsampleinputs,thusreducingFClayerinputsize.Thisdeepernetwork
enablesadvancedfeatureextractionwhilecuttingtrainableparametersandMult-Addoperations
by76%and68%respectively,comparedtoPensieve[38].
ForGelato’soff-policyDQNvariant(contrastedwithPERinFigure2),weemploythesame
architecture,substitutingthepolicyandvaluenetworkswithasingleduelingQ-network[62].
DetailsareinAppx.B.
6 EXPERIMENTS
In this section, we present the findings of testing the impact of Plume across multiple agent
architectures,andacrosssimulationandreal-worldtrials.
6.1 Implementation
We now turn to detail our implementation of all the experiments performed in this paper. We
implementPlumeasaPythonlibrarycompatiblewithallmajorDRLframeworks.
Trainingenvironmentsandalgorithms.WeimplementtheABRenvironmentbyextendingthe
ParkProject[37]andinterfacingwithPuffertraces[65].WeusetheOpenAIGym[12]interface
andtheRLlibrariesStable-Baselines3[49]andRLlib[33].
Plume
1.WeimplementPlumecompletelyoutsideoftheDRLworkflowintheTraceSelection
Module.Toimplementthecriticalfeatureidentificationstage,weusetsfresh[13]foritsfeature-
extraction tools and Scikit-Learn [47] for its decision tree and clustering implementation. To
1https://github.com/sagar-pa/plume
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

PracticallyHighPerformantNeuralAdaptiveVideoStreaming 30:11
implementtheclusteringstage,weuseScikit-LearnforitsGaussianMixtureModelandSilhou-
ettescoringimplementation.Toimplementtheprioritizationstage,weemployNumpy[20]and
PyTorch[45].Formoredetails,seeAppx.F.
6.2 Settings
Inthissection,wepresentthesettingsusedinourexperiments.Wepresentourresultsasaverages
over4instances(4controllerstrainedusingthesameschemewithdifferentinitialrandomseeds).
ThisisconsistentwiththestandardreportingpracticeintheRLcommunity[23,29,41].Fortesting
onthePufferplatform,weselectthebestseedforbenchmarking.Fordetails,seeAppx.BandD.
Simulation.ForABR,weusethePufferplatformnetworktracesfromApril2021-May2021.We
enforceatracelengthrequirementof3−17stream-minutestoreduceI/Ooverheadandprevent
longtracesfromdominatingtraining,randomlysplittinglongtraces.Thisresultsinmorethan
75,000traces,ofwhichwerandomlyselectabout55,000,representingover4.25stream-years,for
ouranalysis.Weuse40,000fortrainingandabout15,000fortesting.Weevaluateeverycontroller
usingthesametrainandtestset.
PufferPlatform.WetestGelatowithbothrandomsamplingandPlumeonthelivestreaming
platformPufferfrom01Oct2022-01Oct2023.ThePufferplatformstreamsliveTVchannelssuch
asABC,NBCorCBSoverthewide-areaInternettomorethan280,000users[2,65].Overthis
time,weanalyzedtheABRalgorithmsstreamedover58.9stream-yearsofvideo.Wereportthe
performanceasSSIMvs.stallratio,followingtheconventionusedbythePufferplatform[65].
WecompareGelato-RandomandGelato-Plume-StaticwiththeperformanceoftheBuffer-based
controller BBA [24], the classical planning controller MPC [67], Puffer optimized versions of
theBOLA,v1andv2[3,56],thein-situcontinuoustrainingcontrollerFugu’sFebruaryversion,
Fugu-Feb[65],andCausalSim[10],aversionofBolatunedbytrace-drivencausalsimulation.
6.3 Results
Inthissection,wepresenttheresultsofourexperimentsinsimulatedandreal-worldABR.
InFig.6,wepresentourresultsevaluatingPlume.Wepresentourobservationsbelow.
Plumeoutperformsrandomtracesamplinginbothsimulationandreal-worldtesting.
InFigures6aand 6d,weanalyzetheperformanceofPlumeacrosstrainingprogress.Weobserve
thatPlumeconvergestoahighernormalizedQoE(definedastherewardin§5),inbothalltraces
andslowtraces.WeadditionallyseethatPensieve-Plume-Dynamicsignificantlyimprovesupon
Pensieve-Random,butthattheimprovementisnotenoughtomatchtheperformanceofGelato.
InFig.6bandFig.6e,webenchmarkthetrainedRLcontrollerswithclassicalcontrollers.Dueto
ABR’stail-endnature,wealsoaddrandombitrateselectionasabaselineforvisualization.Wefind
PlumetooutperformrandomtracesamplingandtheclassicalcontrollersBBA,MPC,andBola.We
notethatwhilethenumericaldifferencesmayappearsmallduetotheinherentscaleofthemetrics,
theyexceedthe95%confidenceintervalbands,andtranslatetolargereal-worlddifferencesaswe
willsee.
Plume-StaticcloselytracksPlume-Dynamic.InFigs.6a, 6d,weobservethatPlume-Static,
whichemployedasimplerprioritizationstrategy,closelytrackstheperformanceofPlume-Dynamic.
Thisislikelyduetothefactthatinthesescenarios,theimpactofshiftingreward-to-govalues
or difficult input traces is minimal. However, as we will see later in Sec. 7, when the training
distributionisanomalousorissignificantlydifferentfromthetestingdistribution,Plume-Dynamic
canproveeffectiveoverPlume-Static.
Gelatooutperformsstate-of-the-artcontrollersintherealworldstreaminglivetelevision
overa1-yearperiod.TofurtherunderstandthebenefitofPlume,werunGelatowithPlume-Static
andrandomsamplingonthereal-worldlive-streamingPufferplatform[65].WeoptedforGelato
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

30:12 SagarPatel,JunyangZhang,NinaNarodystka,andSangeethaAbduJyothi
(a)RLTraining: (b)Simulation: (c)Real-WorldStreaming:
Alltraces Alltraces Alltraces
(d)RLTraining: (e)Simulation: (f)Real-WorldStreaming:
Slowtraces(<0.75Mbps) Slowtraces(<0.75Mbps) Slowtraces(<0.75Mbps)
Fig.6. PlumeperformanceoverSimulationandReal-WorldStreaming:Plumesurpassesrandom
samplinginbothcontrolledsimulation-basedexperimentsandinreal-worldsettings.Thesimulationand
trainingplotsmeasuretheQoEoftheclient,definedasrewardinSec.5.Real-worldStreamingplotsare
basedondatafromPufferstreams(Oct’22-Oct’23),aggregatingover58.9stream-years.Dataisre-plotted
fromitssite[2]tocombinedifferentexperimentperiods.Errorbarsandbandsshow95%confidenceintervals.
Plotaxesvaryduetodifferingobjectivescales.
combinedwithPlume-StaticforthisevaluationgivenitsanalogousperformancetoPlume-Dynamic
inABR,butwithasimplerdesign.Additionally,weincludedGelatowithrandomsamplingasa
baselineforcomparativeanalysis.InFigures6cand6f,weseethatGelato-Plume-Staticoutperforms
the current state-of-the-art controllers Fugu-Feb and CausalSim, alongside the heuristic-based
BBA in both SSIM and stalling. Although prior work [10, 65] reported statistically significant
stallingimprovementsonPuffer,GelatodistinguishesitselfbybecomingthefirstABRcontrollerto
achievestatisticallysignificantimprovementsinbothqualityandstallreduction.Thisisparticularly
noteworthyasGelatodoesnotdependonlow-levelTCPmetricslikeFuguorintricatesimulation
techniquesthatCausalSimuses.
Overthis1yearperiod,thealgorithmsstreamedover58.9stream-yearsofvideostoover280,000
viewersacrosstheInternet[2,65].Overthisduration,Gelato-Plume-Staticachieves75%,78%and
81%stallreductioncomparedtoCausalSim,FuguandBBArespectively(Fig.6c).Gelato-Plume-
StaticadditionallyachievesSSIMimprovementsof0.28,0.12and0.15dBoverCausalSim,Fuguand
BBArespectively.ThisqualityimprovementoverBBAismorethan5×thatofFugu,whichonly
manageda0.03dBimprovementoverBBA.CausalSimdidnotprovideanSSIMimprovementover
BBAoverthisperiod.Gelato-Plume-StatichasanaverageSSIMvariationof0.77dB,comparedto
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

PracticallyHighPerformantNeuralAdaptiveVideoStreaming 30:13
0.67,0.53and0.78dBofCausalSim,FuguandBBArespectively.Moreover,wefindthatGelato-
Randomisastrongbaseline,achieving0.27dBSSIMimprovementand45%stallreductionover
CausalSim.
7 GENERALIZATION
HavingestablishedtheperformanceofPlumeonreal-worldcontrollersandexperimentsinSection6,
in this section, we thoroughly microbenchmark Plume to study its generalizability across the
distributionoftracesusedinABR,aswellasacrossothernetworkingapplications.
7.1 Settings
7.1.1 Generalizationacrossinputtracedistributions:TraceBench. ToassessPlume’sgeneralizability
acrossvariousinputtracedistributionsandnotjusttheonegivenbytheusersofPuffer,weintroduce
acontrolledABRenvironment,TraceBench.TraceBenchimplementstwoprincipalmodifications
tothestandardABRsetting:simplifyingquality-of-experiencemeasurementtoqualityandstalling,
andparameterizingtracesbyreal-worldtraceattributes:meanandvarianceofnetworkthroughput.
These changes enable comprehensive controller evaluation under diverse network conditions.
Althoughasimplification,TraceBenchcloselyapproximatesabroadspectrumofrealisticscenarios.
Notethatparameterizedtracegeneration,integraltoTraceBenchforcreatingvariedscenarios,is
notacomponentoftheprioritizationstrategiesthemselves.ForTraceBenchtraces,wefocuson
twomeanthroughputlevels,slowandfast,andtwothroughputvariancelevels,highandlow.We
createthreedatasetsetswithdifferenttraceproportions:MajorityFast,Balanced,andMajority
Slow.ExampletracevisualizationsareinFig.12(Appx.C).
7.1.2 Generalizationacrossnetworkingapplications:congestioncontrolandloadbalancing.
CongestionControl.CongestionControl(CC)algorithmsareresponsiblefordeterminingthe
mostsuitabletransmissionratefordatatransferoverasharednetwork.Basedonnetworksignals
suchasround-triptimebetweenthesenderandreceiverandthelossrateofpackets,aCCalgorithm
estimatessendingratethatmaximizesthroughputandminimizeslossanddelay.WeevaluatePlume
inCCbyextendingthecodeofAurora[26].Here,eachtraceisrepresentedby4keysimulation
parameters:throughput,latency,maximumqueuesize,andloss.Fortraining,wesamplethroughput
fromrange[100,500]packetspersecond,latencyfrom[50,300]milliseconds,maxqueuesizefrom
[2,50] packets,andlossratefrom [0,2] percent.Fortesting,webroadentherangesandsample
throughputfrom[50,1000],latencyfrom[25,500],maxqueuesizefrom[2,75],andlossfrom[0,3].
Wesamplelatencyuniformlyevenlyintherange,whilesamplingtherestevenlyonageometric
progression.Wenotethatwedothissamplingonlyonceandfixitforbothtrainingandtesting.
LoadBalancing.ALoadBalancing(LB)algorithminadistributedclusterdecideswhichserverto
serveanewjobat,suchastominimizethejob’stotalprocessingtime.Whenajobarrives,theLB
algorithmdoesnotknowhowbusyeachserverisorhowlongeachserverwilltaketoprocess
thejob.Tomakeagooddecision,itusesdatasuchasthetimebetweenjobarrivals,theduration
ofpastjobs,andthenumberofjobsalreadywaitingateachserver.Toevaluate,weusethePark
Project[37]’simplementation.Eachtracerepresentsatimeseriesindicatingthesizeofarrivingjobs
overtime.Followingstandardparameters,theinter-arrivaltimesaresampledfromtheexponential
distribution𝑒𝑥𝑝(𝜆 =55),andthejobsizesfromtheparetodistribution𝑝𝑎𝑟𝑒𝑡𝑜(𝑥
𝑚
=1.5,𝛼 =100).
Welimitthetracelengthto650toensurethatthevarianceofreturns𝐺 isfinite.Asincongestion
control,weperformthissamplingonceandfixitforbothtrainingandtesting.
FurtherdetailsonthesesettingsareinAppendicesC,DandE.
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

30:14 SagarPatel,JunyangZhang,NinaNarodystka,andSangeethaAbduJyothi
(a)Scenario1:TrainingonMajor- (b)Scenario2:TrainingandTesting (c)Scenario3:TrainingonMajor-
ityFast,TestingonMajoritySlow ontheBalanceddataset. itySlow,TestingonMajorityFast
dataset. dataset.
Fig.7. BenchmarkingPlumeacrossTraceDistributions:Webenchmarkprioritizationtechniquesacross
differenttrainingandtestingtracedistributions.Plume-Dynamicprovidesgeneralizableperformanceim-
provement,beatingtheothersinscenarios(1),(2)and(3).95%confidenceintervalshownaserrorbands.
Fig.8.PerformanceofPlumeincongestioncontrol. Fig.9.PerformanceofPlumeinLoadBalancing.95%
95%confidenceintervalshownaserrorbands. confidenceintervalshownaserrorbands.
7.2 Results
Ourexperimentsinvestigatetwoimportantquestions.First,weinvestigatehowtheversionsof
Plume,Plume-StaticandPlume-Dynamicgeneralizegeneralizetoothernetworkdistributionsin
ABR,whichcanbepossibleinreal-worldsettings.Second,weevaluatehowPlumegeneralizesto
othernetworkingapplications,congestioncontrolandloadbalancing.
InFigure7,weanalyzetheperformanceofPlumeacrossvarioustracedistributions.Particularly,
• Scenario1:Thetrainingdistributionissimilartotherealworldbutthetestingisadversarially
different,i.e.,wetrainontheMajorityFastbuttestontheMajoritySlowdataset.
• Scenario2:Bothtrainingandtestinghaveabalancedsetoftraces,i.e.,wetrainandtestonthe
Balanceddataset.
• Scenario3:Thetrainingdistributionlargelyconsistsofthetailendofthetestingdistribution,
i.e.,wetrainontheMajoritySlowbuttestontheMajorityFastdataset.
Plumeoutperformsrandomsamplingregardlessoftracedistribution.Asweobservein
Figures 7a and 7b for the QoE for scenarios (1) and (2), Plume-Dynamic provides a significant
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

PracticallyHighPerformantNeuralAdaptiveVideoStreaming 30:15
performanceimprovementoverrandomsampling.Moreover,eveninFigure7cforscenario(3),
where we may least expect prioritization to help, Plume-Dynamic is still better than random
sampling.WeadditionallyobservethatPlume-Static,whichperformswellinscenario(1),falls
behindPlume-Dynamicinscenarios(2)and(3)wherethetraininginputtracedistributionsare
eitheranomalousoraredramaticallydifferentfromthetestingdistribution.Tobetterunderstand
howPTSsoeffectivelygeneralizesacrossallofthesetracedistributions,wevisualizetheselection
weightofdifferenttracesduringtraininginFig.10inAppx.A.3.
ControllerstrainedwithPlumearerobusttotracedistributionshifts.Inthesecondrowof
plotsinFigures7a,7band7c,wevisualizetheslowtraceperformanceofdifferentprioritization
schemes.Weobservethatrandomtracesampling’sperformanceinslowtracesislargelydependent
onitstrainingdataset.Ifthetrainingdatasethadfewslowtraces,asinscenario(1),theperformance
issignificantlyworsethanitisinscenario(3),whereithadmany.However,Plume-Dynamic’s
performanceisrobusttothetrainingtracedistribution:thecontrollersallconvergetoasimilar
QoEinallthreescenarios.Intheever-changinglandscapeofusers,devices,andinfrastructure
inherenttothenetworkdomain,thisaddedrobustnesscanbeparticularlyimportanttoreducethe
needforretrainingandultimatelythecomputeandenergyrequirementsoftheentiresystem.
Plume’sperformancegainsarerobustacrossnetworkingapplications.InFig.8,wevisualize
theperformanceofRandomtracesampling,Plume-StaticandPlume-Dynamicacrosstrainingin
congestioncontrol.SimilartotheresultsforPlumeinABR(§6),weobservethatPlumeconverges
toahigherperformance,withPlume-StaticcloselytrackingPlume-Dynamic.InFig.9,weobserve
asimilarpatterninloadbalancing,withPlumealsoconvergingtoaloweraveragejobcompletion
time(JCT)thanstandardrandomtracesampling.
Below,wesummarizethefindingsofourexperimentswithABR,CCandLBpresentedinSection6,
andtheanalysisofourextensivePlumebenchmarkingpresentedinthissection.
• PlumeisageneralizedsolutionforDRLtraininginadaptivebitratestreamingthatautomatically
balancesthetracedistribution,andofferssignificantimprovementinperformanceoverrandom
samplinginsimulationandinreal-worldtesting,overbothon-policyandoff-policyalgorithms.
• Plume’sprioritizationstrategiesworkacrosstracedistributionsandnetworkingapplications,
providingcontrollerswithgreaterperformanceandrobustnessinall.
• GelatotrainedwithPlumeoffersthebestperformancewhencomparedtopriorABRcontrollers
onthereal-worldPufferplatform.Itachieves75%and78%reductioninstallsoverCausalSim[10]
andFugu[65]respectively.ItalsoachievesastatisticallysignificantSSIMimprovementof0.28
dBoverCausalSimand0.12dBoverFugu.
8 DISCUSSIONANDLIMITATIONS
WeenvisionPlumetoopenanewavenueofresearchforDRLtraining.Ratherthanevolveinto
anotherhyperparameter,theproblemoftracesamplinglendsitselftoprincipledanalysis,anda
generalizedandbroadlyapplicablesolution.However,ourworkstillleavesagapforfuturework.
Theneedforsystematicstudyofinput-drivenDRLtraining.OuranalysisofPlumehighlights
thesignificantimpactofskewandthebenefitsderivedfromaddressingit.Thisfindingprovides
a strong motivation to explore other overlooked factors that may also influence input-driven
DRL training. While the broader ML community has conducted in-depth studies on training
parameters[11],DRLenvironments[15],andevaluationmetrics[8],thereisalackofsuchresearch
inthenetworkingdomain.Engaginginsystematicstudiesinthisfrontcouldenabletheresearch
communitytobetterunderstandthepotentialofexistingsolutionsandpavewayforanempirical
assessmentoftherealchallengesfacedbyoptimizedinput-drivenDRLsolutions.
FuturedirectionforPlume.Inadditiontonetworkingenvironments,Plumecanalsobebeneficial
inothertrace-drivenDRLsettingssuchasdronecontrol,autonomousdriving,etc.Plume,aswe
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

30:16 SagarPatel,JunyangZhang,NinaNarodystka,andSangeethaAbduJyothi
presentedit,cannotbeuseddirectlyinsuchenvironmentswithmorecomplexinputprocesses.
However,extensionstoPlumeaspresentedinthispapermaybeaninterestingfuturedirection.
Sim2RealGap.Plumechangeswhichtracesgetsampledandnothowtheyaresimulated.Plume
does not address the problem related to the gap between the simulation environment and the
real-worldsetting(Sim2RealGap).Thus,Plumecannothandlethescenariowheretrainingtraces
areincompleteorhaveexperienceddatashiftfromtheruntimeenvironment.Trainingandruntime
solutionsthatbringsimulationclosertorealitycanbecombinedwithPlume.
Large-ScaleTraining.Thebenefitsofhigherstate-actionexplorationandfeaturelearningoffered
byPlumemaydiminishwithaverydeepneuralnetworkoveralargenumberoftrainingsteps
andparallelenvironments.OurexperimentalevidencesuggeststhatPlumeishighlyrelevantfor
practicalDRLenvironmentsandtrainingsettings.However,wecannotascertaintheeffectiveness
ofPlumeatthescaleofstate-of-the-artGoagents[52],whichrequirestrainingcapabilitiesonly
availabletolargecompanies.
9 RELATEDWORK
PrioritizationinSupervisedlearning.Classimbalanceisfrequentlyachallengeinsupervised
data-drivennetworkingproblems,wheresamplesofsomeclassesofnetworkconditionsorscenarios
occur rarely [16, 31, 34, 69]. A popular technique to address this problem is to oversample or
undersamplecertainclassestoensurethatthemodeldoesnotdrownouttheerrorintheminority
classes[30].Suchtechniquescannotbeusedinreinforcementlearning,wherethelearninghappens
usingstates,actionsandrewardsratherthanafixeddatasetwithlabels.
Prioritization in DRL. While we present the first systematic methodology of prioritization
of input traces in DRL, prioritization/importance sampling has been applied at other points in
theDRLworkflow.PER[51]isusedtoprioritizetransitionsinthereplaybufferinactor-critic
algorithms[60],inthemulti-agentsetting[18],andintext-basedDRLenvironments[44]toimprove
sampleefficiency.Horganet.al[23]usedPERinconjunctionwithdistributedactingtoimprove
feature learning. Schulman et.al [53, 54] employed importance sampling to reduce variance of
on-policytraining.However,asshowninourexperiment(§3.3),thesesolutionsdonotaddressthe
skewininput-drivenenvironments.
DRL for Networking and Systems applications. Following the promise of DRL, a number
ofpriorworkshaveworkedtoimproveitsperformanceinnetworking,improvingsim2realgap
and efficiency. Gilad et.al. [19] employed RL to find additional training traces to help the DRL
agentgeneralizetounseennetworkconditions.Buildingonthisidea,Xiaetal.[63]introduceda
systematicCurriculumLearningbasedapproachforthesamegoal.ItintroducedthemetricGap-to-
baselineforenvironmentconfigurationsandsystematicallygeneratedtheadditionalenvironment
configurationsneededforgreatergeneralizaiblity.Bothofthesetechniquesaddressingsim2realgap
arefftangentialtoPlumeandcanbeusedalongsideit.Maoet.al.[39]introducedthealgorithm-side
optimizationofusinginput-dependentbaselinestoreducethevarianceofon-policyalgorithms
atthepolicyoptimizationstep.DoublyRobustestimation[27]helpsinestimatingperformance
variationsduringinput-drivenevaluationbutdoesnotaddresstheskewinlearning.Thesesolutions,
addressing various other challenges in DRL, serve as crucial motivation to address the skew
underpinningDRLinadaptivebitratestreamingandcanbecombinedwithPlume.
10 CONCLUSION
PracticaladoptionofDRL-basedABRcontrollersislimitedbecausetheresearchcommunitydoes
notfullyknowhowtoproducehigh-performancecontrollers.Weuncoverthatskewintheinput
datasets of DRL controllers plays a significant role in performance, and put forward Plume, a
systematic,generalizable,andhigh-performantmethodologyforaddressingthatskew.
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

PracticallyHighPerformantNeuralAdaptiveVideoStreaming 30:17
REFERENCES
[1] [n.d.]. Expectation–maximization algorithm - Wikipedia. https://en.wikipedia.org/wiki/Expectation%E2%80%
93maximization_algorithm. (Accessedon01/16/2023).
[2] [n.d.].Puffer.https://puffer.stanford.edu/results/. (Accessedon04/20/2022).
[3] [n.d.].Puffer.https://puffer.stanford.edu/bola/. (Accessedon06/09/2024).
[4] [n.d.].Scikit-LearnRecursiveFeatureElimiation.https://scikit-learn.org/stable/modules/generated/sklearn.feature_
selection.RFE.html#sklearn.feature_selection.RFE. (Accessedon01/15/2023).
[5] [n.d.]. Silhouette(clustering)-Wikipedia. https://en.wikipedia.org/wiki/Silhouette_(clustering). (Accessedon
01/16/2023).
[6] SoheilAbbasloo,Chen-YuYen,andHJonathanChao.2020. Classicmeetsmodern:Apragmaticlearning-based
congestioncontrolfortheInternet.InProceedingsoftheAnnualconferenceoftheACMSpecialInterestGrouponData
Communicationontheapplications,technologies,architectures,andprotocolsforcomputercommunication.632–647.
[7] JoshuaAchiam.2018.SpinningUpinDeepReinforcementLearning.(2018).
[8] RishabhAgarwal,MaxSchwarzer,PabloSamuelCastro,AaronCCourville,andMarcBellemare.2021. Deeprein-
forcementlearningattheedgeofthestatisticalprecipice.Advancesinneuralinformationprocessingsystems34(2021),
29304–29320.
[9] ZahaibAkhtar,YunSeongNam,RameshGovindan,SanjayRao,JessicaChen,EthanKatz-Bassett,BrunoRibeiro,Jibin
Zhan,andHuiZhang.2018.Oboe:Auto-tuningvideoABRalgorithmstonetworkconditions.InProceedingsofthe
2018ConferenceoftheACMSpecialInterestGrouponDataCommunication.44–58.
[10] AbdullahAlomar,PouyaHamadanian,ArashNasr-Esfahany,AnishAgarwal,MohammadAlizadeh,andDevavrat
Shah.2023. {CausalSim}:ACausalFrameworkforUnbiased{Trace-Driven}Simulation.In20thUSENIXSymposium
onNetworkedSystemsDesignandImplementation(NSDI23).1115–1147.
[11] MarcinAndrychowicz,AntonRaichuk,PiotrStańczyk,ManuOrsini,SertanGirgin,RaphaëlMarinier,Leonard
Hussenot,MatthieuGeist,OlivierPietquin,MarcinMichalski,etal.2020.Whatmattersforon-policydeepactor-critic
methods?alarge-scalestudy.InInternationalconferenceonlearningrepresentations.
[12] GregBrockman,VickiCheung,LudwigPettersson,JonasSchneider,JohnSchulman,JieTang,andWojciechZaremba.
2016.Openaigym.arXivpreprintarXiv:1606.01540(2016).
[13] MaximilianChrist,NilsBraun,JuliusNeuffer,andAndreasWKempa-Liehr.2018.Timeseriesfeatureextractionon
basisofscalablehypothesistests(tsfresh–apythonpackage).Neurocomputing307(2018),72–77.
[14] VCisco.2018.Ciscovisualnetworkingindex:Forecastandtrends,2017–2022.Whitepaper1,1(2018).
[15] KaleighClary,EmmaTosch,JohnFoley,andDavidJensen.2019.Let’sPlayAgain:VariabilityofDeepReinforcement
LearningAgentsinAtariEnvironments.arXivpreprintarXiv:1904.06312(2019).
[16] ShiDong.2021.MulticlassSVMalgorithmwithactivelearningfornetworktrafficclassification.ExpertSystemswith
Applications176(2021),114885.
[17] SallyFloydandVernPaxson.2001.DifficultiesinsimulatingtheInternet.IEEE/ACmTransactionsonNetworking9,4
(2001),392–403.
[18] JakobFoerster,NantasNardelli,GregoryFarquhar,TriantafyllosAfouras,PhilipHSTorr,PushmeetKohli,andShimon
Whiteson.2017.Stabilisingexperiencereplayfordeepmulti-agentreinforcementlearning.InInternationalconference
onmachinelearning.PMLR,1146–1155.
[19] TomerGilad,NathanHJay,MichaelShnaiderman,BrightenGodfrey,andMichaelSchapira.2019. Robustifying
networkprotocolswithadversarialexamples.InProceedingsofthe18thACMWorkshoponHotTopicsinNetworks.
85–92.
[20] CharlesR.Harris,K.JarrodMillman,StéfanJ.vanderWalt,RalfGommers,PauliVirtanen,DavidCournapeau,Eric
Wieser,JulianTaylor,SebastianBerg,NathanielJ.Smith,RobertKern,MattiPicus,StephanHoyer,MartenH.van
Kerkwijk,MatthewBrett,AllanHaldane,JaimeFernándezdelRío,MarkWiebe,PearuPeterson,PierreGérard-Marchant,
KevinSheppard,TylerReddy,WarrenWeckesser,HameerAbbasi,ChristophGohlke,andTravisE.Oliphant.2020.
ArrayprogrammingwithNumPy.Nature585,7825(Sept.2020),357–362. https://doi.org/10.1038/s41586-020-2649-2
[21] DanHendrycksandKevinGimpel.2016.Gaussianerrorlinearunits(gelus).arXivpreprintarXiv:1606.08415(2016).
[22] MatteoHessel,JosephModayil,HadoVanHasselt,TomSchaul,GeorgOstrovski,WillDabney,DanHorgan,Bilal
Piot,MohammadAzar,andDavidSilver.2018.Rainbow:Combiningimprovementsindeepreinforcementlearning.In
Thirty-secondAAAIconferenceonartificialintelligence.
[23] DanHorgan,JohnQuan,DavidBudden,GabrielBarth-Maron,MatteoHessel,HadoVanHasselt,andDavidSilver.
2018.Distributedprioritizedexperiencereplay.arXivpreprintarXiv:1803.00933(2018).
[24] Te-YuanHuang,RameshJohari,NickMcKeown,MatthewTrunnell,andMarkWatson.2014.Abuffer-basedapproach
torateadaptation:Evidencefromalargevideostreamingservice.InProceedingsofthe2014ACMconferenceon
SIGCOMM.187–198.
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

30:18 SagarPatel,JunyangZhang,NinaNarodystka,andSangeethaAbduJyothi
[25] MichaelJanner,JustinFu,MarvinZhang,andSergeyLevine.2019.Whentotrustyourmodel:Model-basedpolicy
optimization.Advancesinneuralinformationprocessingsystems32(2019).
[26] NathanJay,NogaRotman,BrightenGodfrey,MichaelSchapira,andAvivTamar.2019.Adeepreinforcementlearning
perspectiveoninternetcongestioncontrol.InInternationalconferenceonmachinelearning.PMLR,3050–3059.
[27] JunchenJiang,VyasSekar,IonStoica,andHuiZhang.2017.Unleashingthepotentialofdata-drivennetworking.In
InternationalConferenceonCommunicationSystemsandNetworks.Springer,110–126.
[28] JustinMJohnsonandTaghiMKhoshgoftaar.2020. Theeffectsofdatasamplingwithdeeplearningandhighly
imbalancedbigdata.InformationSystemsFrontiers22,5(2020),1113–1131.
[29] StevenKapturowski,GeorgOstrovski,JohnQuan,RemiMunos,andWillDabney.2018.Recurrentexperiencereplay
indistributedreinforcementlearning.InInternationalconferenceonlearningrepresentations.
[30] HarsurinderKaur,HusanbirSinghPannu,andAvleenKaurMalhi.2019. Asystematicreviewonimbalanceddata
challengesinmachinelearning:Applicationsandsolutions.ACMComputingSurveys(CSUR)52,4(2019),1–36.
[31] JoffreyLLeevy,TaghiMKhoshgoftaar,andJaredMPeterson.2021.Mitigatingclassimbalanceforiotnetworkintrusion
detection:asurvey.In2021IEEESeventhInternationalConferenceonBigDataComputingServiceandApplications
(BigDataService).IEEE,143–148.
[32] SergeyLevine,AviralKumar,GeorgeTucker,andJustinFu.2020.Offlinereinforcementlearning:Tutorial,review,and
perspectivesonopenproblems.arXivpreprintarXiv:2005.01643(2020).
[33] EricLiang,RichardLiaw,RobertNishihara,PhilippMoritz,RoyFox,KenGoldberg,JosephE.Gonzalez,MichaelI.
Jordan,andIonStoica.2018.RLlib:AbstractionsforDistributedReinforcementLearning.InInternationalConference
onMachineLearning(ICML).
[34] XiaoyuLiangandTaiebZnati.2019.AnempiricalstudyofintelligentapproachestoDDoSdetectioninlargescale
networks.In2019InternationalConferenceonComputing,NetworkingandCommunications(ICNC).IEEE,821–827.
[35] HongziMao,MohammadAlizadeh,IshaiMenache,andSrikanthKandula.2016. Resourcemanagementwithdeep
reinforcementlearning.InProceedingsofthe15thACMworkshoponhottopicsinnetworks.50–56.
[36] HongziMao,ShannonChen,DrewDimmery,ShaunSingh,DrewBlaisdell,YuandongTian,MohammadAlizadeh,and
EytanBakshy.2020.Real-worldvideoadaptationwithreinforcementlearning.arXivpreprintarXiv:2008.12858(2020).
[37] HongziMao,ParimarjanNegi,AkshayNarayan,HanruiWang,JiachengYang,HaonanWang,RyanMarcus,Mehrdad
KhaniShirkoohi,SongtaoHe,VikramNathan,etal.2019.Park:Anopenplatformforlearning-augmentedcomputer
systems.AdvancesinNeuralInformationProcessingSystems32(2019).
[38] HongziMao,RaviNetravali,andMohammadAlizadeh.2017. Neuraladaptivevideostreamingwithpensieve.In
ProceedingsoftheConferenceoftheACMSpecialInterestGrouponDataCommunication.197–210.
[39] HongziMao,ShaileshhBojjaVenkatakrishnan,MalteSchwarzkopf,andMohammadAlizadeh.2018.Variancereduction
forreinforcementlearningininput-drivenenvironments.arXivpreprintarXiv:1807.02264(2018).
[40] MelikaMeskovic,MladenKos,andAmirMeskovic.2015.Optimalchunkschedulingalgorithmbasedontaboosearch
foradaptivelivevideostreaminginCDN-P2P.In201523rdInternationalConferenceonSoftware,Telecommunications
andComputerNetworks(SoftCOM).IEEE,205–209.
[41] VolodymyrMnih,AdriaPuigdomenechBadia,MehdiMirza,AlexGraves,TimothyLillicrap,TimHarley,DavidSilver,
andKorayKavukcuoglu.2016.Asynchronousmethodsfordeepreinforcementlearning.InInternationalconferenceon
machinelearning.PMLR,1928–1937.
[42] VolodymyrMnih,KorayKavukcuoglu,DavidSilver,AlexGraves,IoannisAntonoglou,DaanWierstra,andMartin
Riedmiller.2013.PlayingAtariwithdeepreinforcementlearning.arXivpreprintarXiv:1312.5602(2013).
[43] PhilippMoritz,RobertNishihara,StephanieWang,AlexeyTumanov,RichardLiaw,EricLiang,MelihElibol,Zongheng
Yang,WilliamPaul,MichaelIJordan,etal.2018.Ray:Adistributedframeworkforemerging{AI}applications.In
13thUSENIXSymposiumonOperatingSystemsDesignandImplementation(OSDI18).561–577.
[44] KarthikNarasimhan,TejasKulkarni,andReginaBarzilay.2015.Languageunderstandingfortext-basedgamesusing
deepreinforcementlearning.arXivpreprintarXiv:1506.08941(2015).
[45] AdamPaszke,SamGross,FranciscoMassa,AdamLerer,JamesBradbury,GregoryChanan,TrevorKilleen,ZemingLin,
NataliaGimelshein,LucaAntiga,etal.2019.Pytorch:Animperativestyle,high-performancedeeplearninglibrary.
Advancesinneuralinformationprocessingsystems32(2019).
[46] VernPaxsonandSallyFloyd.1997. Whywedon’tknowhowtosimulatetheInternet.InProceedingsofthe29th
conferenceonWintersimulation.1037–1044.
[47] F.Pedregosa,G.Varoquaux,A.Gramfort,V.Michel,B.Thirion,O.Grisel,M.Blondel,P.Prettenhofer,R.Weiss,V.
Dubourg,J.Vanderplas,A.Passos,D.Cournapeau,M.Brucher,M.Perrot,andE.Duchesnay.2011.Scikit-learn:Machine
LearninginPython.JournalofMachineLearningResearch12(2011),2825–2830.
[48] TobiasPohlen,BilalPiot,ToddHester,MohammadGheshlaghiAzar,DanHorgan,DavidBudden,GabrielBarth-Maron,
HadoVanHasselt,JohnQuan,MelVečerík,etal.2018.Observeandlookfurther:Achievingconsistentperformance
onAtari.arXivpreprintarXiv:1805.11593(2018).
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

PracticallyHighPerformantNeuralAdaptiveVideoStreaming 30:19
[49] AntoninRaffin,AshleyHill,AdamGleave,AnssiKanervisto,MaximilianErnestus,andNoahDormann.2021.Stable-
Baselines3:ReliableReinforcementLearningImplementations.JournalofMachineLearningResearch22,268(2021),
1–8. http://jmlr.org/papers/v22/20-1364.html
[50] AntoninRaffin,JensKober,andFreekStulp.2022.Smoothexplorationforroboticreinforcementlearning.InConference
onRobotLearning.PMLR,1634–1644.
[51] TomSchaul,JohnQuan,IoannisAntonoglou,andDavidSilver.2015. Prioritizedexperiencereplay. arXivpreprint
arXiv:1511.05952(2015).
[52] JulianSchrittwieser,IoannisAntonoglou,ThomasHubert,KarenSimonyan,LaurentSifre,SimonSchmitt,Arthur
Guez,EdwardLockhart,DemisHassabis,ThoreGraepel,etal.2020.MasteringAtari,Go,ChessandShogibyplanning
withalearnedmodel.Nature588,7839(2020),604–609.
[53] JohnSchulman,SergeyLevine,PieterAbbeel,MichaelJordan,andPhilippMoritz.2015.Trustregionpolicyoptimization.
InInternationalconferenceonmachinelearning.PMLR,1889–1897.
[54] JohnSchulman,FilipWolski,PrafullaDhariwal,AlecRadford,andOlegKlimov.2017.Proximalpolicyoptimization
algorithms.arXivpreprintarXiv:1707.06347(2017).
[55] DavidSilver.2015.LecturesonReinforcementLearning.url:https://www.davidsilver.uk/teaching/.
[56] KevinSpiteri,RahulUrgaonkar,andRameshKSitaraman.2020.BOLA:Near-optimalbitrateadaptationforonline
videos.IEEE/ACMTransactionsonNetworking28,4(2020),1698–1711.
[57] ThomasStockhammer.2011.DynamicadaptivestreamingoverHTTP–standardsanddesignprinciples.InProceedings
ofthesecondannualACMconferenceonMultimediasystems.133–144.
[58] YiSun,XiaoqiYin,JunchenJiang,VyasSekar,FuyuanLin,NanshuWang,TaoLiu,andBrunoSinopoli.2016.CS2P:
Improvingvideobitrateselectionandadaptationwithdata-driventhroughputprediction.InProceedingsofthe2016
ACMSIGCOMMConference.272–285.
[59] RichardSSuttonandAndrewGBarto.2018.Reinforcementlearning:Anintroduction.MITpress.
[60] ZiyuWang,VictorBapst,NicolasHeess,VolodymyrMnih,RemiMunos,KorayKavukcuoglu,andNandodeFreitas.
2016.Sampleefficientactor-criticwithexperiencereplay.arXivpreprintarXiv:1611.01224(2016).
[61] ZhouWang,AlanCBovik,HamidRSheikh,andEeroPSimoncelli.2004. Imagequalityassessment:fromerror
visibilitytostructuralsimilarity.IEEEtransactionsonimageprocessing13,4(2004),600–612.
[62] ZiyuWang,TomSchaul,MatteoHessel,HadoHasselt,MarcLanctot,andNandoFreitas.2016. Duelingnetwork
architecturesfordeepreinforcementlearning.InInternationalconferenceonmachinelearning.PMLR,1995–2003.
[63] ZhengxuXia,YajieZhou,FrancisYYan,andJunchenJiang.2022.Genet:automaticcurriculumgenerationforlearning
adaptationinnetworking.InProceedingsoftheACMSIGCOMM2022Conference.397–413.
[64] ZhiyingXu,FrancisYYan,RacheeSingh,JustinTChiu,AlexanderMRush,andMinlanYu.2023. Teal:Learning-
AcceleratedOptimizationofWANTrafficEngineering.InProceedingsoftheACMSIGCOMM2023Conference.378–393.
[65] FrancisYYan,HudsonAyers,ChenzhiZhu,SadjadFouladi,JamesHong,KeyiZhang,PhilipLevis,andKeithWinstein.
2020.Learninginsitu:arandomizedexperimentinvideostreaming.In17thUSENIXSymposiumonNetworkedSystems
DesignandImplementation(NSDI20).495–511.
[66] Han-JiaYe,Hong-YouChen,De-ChuanZhan,andWei-LunChao.2020. Identifyingandcompensatingforfeature
deviationinimbalanceddeeplearning.arXivpreprintarXiv:2001.01385(2020).
[67] XiaoqiYin,AbhishekJindal,VyasSekar,andBrunoSinopoli.2015.Acontrol-theoreticapproachfordynamicadaptive
videostreamingoverHTTP.InProceedingsofthe2015ACMConferenceonSpecialInterestGrouponDataCommunication.
325–338.
[68] YasirZaki,ThomasPötsch,JayChen,LakshminarayananSubramanian,andCarmelitaGörg.2015.Adaptivecongestion
controlforunpredictablecellularnetworks.InProceedingsofthe2015ACMConferenceonSpecialInterestGroupon
DataCommunication.509–522.
[69] QizhenZhang,KelvinKWNg,CharlesKazer,ShenYan,JoãoSedoc,andVincentLiu.2021.MimicNet:fastperformance
estimatesfordatacenternetworkswithmachinelearning.InProceedingsofthe2021ACMSIGCOMM2021Conference.
287–304.
[70] XuZhang,YiyangOu,SiddharthaSen,andJunchenJiang.2021. {SENSEI}:Aligningvideostreamingqualitywith
dynamicusersensitivity.In18thUSENIXSymposiumonNetworkedSystemsDesignandImplementation(NSDI21).
303–320.
[71] XuanKelvinZou,JeffreyErman,VijayGopalakrishnan,EmirHalepovic,RittwikJana,XinJin,JenniferRexford,and
RakeshKSinha.2015.Canaccuratepredictionsimprovevideostreamingincellularnetworks?.InProceedingsofthe
16thInternationalWorkshoponMobileComputingSystemsandApplications.57–62.
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

30:20 SagarPatel,JunyangZhang,NinaNarodystka,andSangeethaAbduJyothi
Fig.10. VisualizationoftheprioritizationfoundbyPlume-Dynamicinvariousdatasets:Therelative
changeinsamplingweightforeachkindoftracesoverthetraining.Selectingallkindsoftracesatweight1
isequivalenttorandomsampling.
A PLUMEDETAILS
Inthissection,weprovidedetails,visualizations,andanalysisofthePlumeanditsthreestages.
A.1 CriticalFeatureIdentification
WerecallthatintheCriticalFeatureIdentificationstage,Plumeidentifiestracesbyfirstextracting
awiderangeoffeaturesandthenfilteringthemtofindthecriticalfeatures.
A wide range of features is extracted for each trace in the dataset of traces. Then, this set
offeaturesgoesthroughourautomatedfilteringprocess.Duringthisprocess,about40%ofthe
featuresareeliminated.Westartwith16features,ofwhich7describethecentraltendencyand
9 describe the spread. The features of central tendency include Mean, Quantiles of the 2.5𝑡ℎ,
5𝑡ℎ, and 95𝑡ℎ, Truncated mean of 5𝑡ℎ, 12.5𝑡ℎ, and 25𝑡ℎ quantiles, and the Spectral Centroid of
theAbsoluteFourierTransformSpectrum.The9featuresofthespreadaretheRatioofvalues
beyond1×and2.5×standarddeviation,CoefficientofVariation,CentralapproximationofSecond
Derivative,MeanAbsoluteChangetruncatedbeyondthe[5𝑡ℎ,95𝑡ℎ]and[1.25𝑡ℎ,98.75𝑡ℎ]quantiles,
andAutocorrelationwithlagof3,5,and8.
A.2 Clustering
WerecallthatintheClusteringstageofPlume,wegroupsimilartracestogethertoattemptto
reducethecomplexityoftheprioritizationproblemfromatrace-leveltoacluster.
Wedothisbyautomaticallyfindingboththeclusteringandtheoptimalnumberoffeatures
throughasearchprocedure.InABR,wesearchforthenumberofclustersintherange[6,15],[3,7]
inTraceBench, [4,9] inCC,andintherange [3,8] inLB.
A.3 Prioritization
WerecallthatinthePrioritizationstageofPlume-Dynamic,weobservethecontroller’straining
anddynamicallyprioritizeclusterstofocusonthosewiththemosttolearnfrom.
Plume-Dynamiceffectivelyadaptstoalltrainingtracedistribution.Tobetterunderstand
howPlume-Dynamicsoeffectivelygeneralizesacrossallofthesetracedistributions,wevisualize
thesamplingweightofdifferenttracesduringtraininginFigure10.Weobservethatwhiletraining
ontheMajorityFastdataset,itundersamplestheFasttracesandoversamplestheSlowones.In
theMajoritySlowdataset,itundersamplestheSlow–LowVariancetraceswhileoversamplingthe
FastandSlow–HighVarianceones.ThishighlightsthepowerofPlume-Dynamic’sautomated
prioritization:Itadaptsitselftothedistributionineachdatasetandallowsthecontrollertofocus
onclusterswiththemosttolearnfrom.
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

PracticallyHighPerformantNeuralAdaptiveVideoStreaming 30:21
Fig.11. PerformancePlotsfromthePufferPlatform[2],presentingresultsfrom07Mar’2022—05Oct’2022.
Theresultsvisualize25.5steam-yearsofdata.Similarlytoourmainresults,weseethatGelato-Plume-Static
(maguro)outperformsallotherstate-of-the-artABRcontrollersinbothvideoqualityandstallingandthat
Gelato-Random(unagi)improvesoverallvideoqualitywhileachievingsimilarstallingperformance.
B ADAPTIVEBITRATESTREAMINGDETAILS
InABR,weintroducethenovelcontrollerarchitectureGelato.
Gelato’sneuralarchitectureusesframe-stackingwith10pastvaluesfortheclientdata,and5
futurevaluesofchunksizesandSSIMsateveryencodedbitrate.Theclientdataispassedthrough
a1Dconvolutionwithakernelsizeof3and64filters,followedbyanother1Dconvolutionofthe
samekernelsizeandfilters.ThechunksizesandSSIMsareeachpassedthroughtheirown1D
convolutionwithakernelsizeof5and32filters,eachfollowedbyanother1Dconvolutionwith
thesamekernelsizeandnumberoffilters.Thesecondlayerofconvolutionsreducesthesizeof
theresultingoutputbyafactorproportionaltothesizeofthekernel.Theresultingfeaturesare
concatenatedandpassedthroughapolicyandavaluenetworkeachmadeupofasinglehidden
layerof256neurons.Notethatthevaluenetworkisnotusedoutsideoftraining.Aninference
onGelato’sneuralnetworktakeslessthan0.35msonaverageonacoreofour𝑥86−64CPU
serverinPython—aminimalper-chunkoverheadforPuffer’s2.002secondchunkduration.Totrain
Gelato,weusetheA2Calgorithm[41]usingastandardrewardnormalizationstrategy[48]and
thetrainingparameters:learningrateof0.001,64parallelenvs.,4𝑒8trainingsteps,𝑡 of15,GAE
𝑚𝑎𝑥
N-stepreturnof15,𝛾 of0.95,0..9valuefunctioncoefficient,Entropyof [5.75,.0025] annealedover
2𝑒8steps,andMaxGradientNormof0.4.
Theoff-policyDQNvariantofGelatousesthesamearchitecture,swappingthefinalpolicyand
valuenetworksforasingleduelingQ-networkmadeupofasinglehiddenlayerof256neurons.
Weadditionallyuseastandardrewardnormalizationfunction[48]tonormalizetherewards.To
trainthisvariantofGelato,weusetheApe-XDQNalgorthm[23]usingthetrainingparameters:
64actors,1𝑒9trainingsteps,learningrateof7.5𝑒−6,replaybatchsizeof128,0.95𝛾,replaybuffer
sizeof2𝑀,N-stepreturnof7andvalueclippingbetween [−32,32].
We use the Puffer Platform to gather traces for our simulation environment. The traces are
system logs of the video streams—time series that include (i) the chunk sizes and SSIMs at all
bitrates,(ii)thebitratechosenbytheABRalgorithm,and(iii)thetimetakentotransmitthatchunk.
WecalculatetheeffectivethroughputovertimeanduseitalongsidethechunksizesandSSIMsfor
simulation.
WetrainPensieve[38]usingitsoriginalarchitecture.However,becausetheoriginalimplemen-
tationcouldonlyworkwiththetracesprovidedbytheauthors,toadaptPensievetonewtraces,
weusethesametrainingenvironmentandDRLparametersasGelato.
InpresentingtheresultsforGelatointherealworld,were-plotthedatafoundonthePuffer
Platform[65]inFigure6inSection6.Inouranalysis,wepresentthedatafromdates01Oct’2022
through01Oct2023.However,becausetheplatformwasexperiencingissuesandbenchmarking
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

30:22 SagarPatel,JunyangZhang,NinaNarodystka,andSangeethaAbduJyothi
Fig.12. VisualizationofTracesgeneratedinTraceBench:AThroughputvsTimeplotofexampletraces
usedinTraceBench.Thebroadcoverageofthemeanandvarianceofthethroughputrequirestheagentto
learntoadapttoeachkindoftracedifferently.
otherABRcontrollers,thisdataissplitacrossmultipleplots.Toaggregatethedatatogether,wefirst
downloadthepre-processedpublicdataavailablefromthePufferWebsite[2].Second,wefollow
thesametechniqueusedbytheplatformandemployasampling-basedapproachtoestimatethe
meanand95%confidenceintervalofquality,qualitychange,andstallingforeachABRalgorithm.
Weignoreallthedayswhentheplatformwasundermaintenance(suchas16January2023)and
dayswhentheplatformproducedfaultydataduetoaknownbug(suchas21January2023).
Forcompleteness,wepresenttheolderresultsfromthePufferPlatforminFigure11benchmarking
theoriginalversionoftheFugucontroller,whichwastakenofftheplatformon06October2022.In
thisplot,weanalyze25.5stream-yearsofdata,collectedfrom07March2022through05October
2022.WeobservethatGelato-Plume-Staticstilloutperformsthestate-of-the-artABRalgorithms
inbothqualityandstalling.ThisresulthighlightshowPlumecansuccessfullytrainrobustand
high-performantcontrollersinsimulation,evenoutperformingin-situtrainedcontrollersupdated
daily.
C TRACEBENCHDETAILS
IndesigningTraceBench,ourobjectiveistocreateanenvironmenttothoroughlyevaluateand
validatedifferentprioritizationtechniques.
We build our environment on top of the standard ABR implementation found in the Park
Project[37].Weallowtheclienttohaveamaximumbufferof15seconds.Weconsidertraceswith
amaximumlengthof100seconds,withchunksof1second.Thechunksizesaregeneratedby
samplingaGaussiandistributionaroundthebitrates[1.0,3.0,6.0]megabytespersecond.
Whengeneratingthetraces,weconsidertwolevelsofthroughput,fastandslow,andtwolevels
ofvariance,high-varianceandlow-variance.Whengeneratingatrace,weusea2-stateMarkov
modelswitchingbetweenhighandlowthroughputwithdifferentswitchingprobabilitiesforeach
kind of trace. In Figure 12, we present a throughput vs. time visualization of each of the four
differentkindsoftraces.
WhentrainingthecontrollersinTraceBench,weusethestate-of-the-artfeed-forwardDQN
algorithm Ape-X Dqn [23]. We use framestacking of history length 10. We additionally use a
standard reward normalization function [48] to normalize the rewards. We use a simple fully
connectedarchitecturewith2layersof256units.WeadditionallyusetheduelinganddoubleDQN
architecturewithahiddenfullyconnectedlayerof256units.Weusethetrainingparameters:4
actors,4𝑒6trainingsteps,32replaybatchsize,.975𝛾,250000replaybuffersize,N-stepreturnof7,𝜖
annealingover7𝑒5stepsandvalueclippingbetween [−32,32].
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.

PracticallyHighPerformantNeuralAdaptiveVideoStreaming 30:23
D CONGESTIONCONTROLDETAILS
InCC,wetrainandevaluateAurora[26]withdifferentprioritizationtechniques.Weuseframes-
tacking with a history length of 25. We use a 2-layer fully connected neural architecture with
64unitsforboththepolicyandvaluefunction.WeadditionallyuseState-Dependentnoisefor
exploration[50]andrewardscaling.WeusethealgorithmA2C[41]withtrainingparameters:
learningrateof.000125,16parallelenvs.,5𝑒6trainingsteps,𝑡 of15,GAEN-stepreturnof15
𝑚𝑎𝑥
steps,.975𝛾,valuecoefficientof0.05,entropyof [.1,.005] annealedoverinterval2.5𝑒6stepsand
maxgradientnormof0.25.
E LOADBALANCINGDETAILS
InLB,weevaluatedifferentprioritizationtechniquesusingstandardparameters.Weusea2-layer
fullyconnectedneuralarchitecturewith[256,128]unitsandGeLUactivation[21]forboththe
policyandvaluefunction.Weadditionallyuserewardscaling,andthealgorithmPPO[54]with
trainingparameters:learningrateof2𝑒−4,16parallelenvs.,5𝑒6trainingsteps,batchsizeof256,
GAE𝜆of.975,noadvantagenormalization,30epochsperupdate,1𝑒−4valuefunctioncoefficient,
entropyof [.1,1𝑒−6] annealedover5𝑒6steps,cliprangeof0.1andmaxgradientnormof0.2.
F IMPLEMENTATIONDETAILS
AstraightforwardimplementationofPlumecandirectlyinterferewiththevariousdistributed
training paradigms used in many DRL algorithms [23, 41]. To this degree, we implement our
prioritizationstrategyusingthedistributedsharedobject-storeparadigminRay[43].Thisallows
ustosharethesamplingweightsacrossRLprocesseswithoutinterferingwithanyDRLworkflows.
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
ReceivedJune2024;revisedSeptember2024;acceptedOctober2024
Proc.ACMNetw.,Vol.2,No.CoNEXT4,Article30.Publicationdate:December2024.