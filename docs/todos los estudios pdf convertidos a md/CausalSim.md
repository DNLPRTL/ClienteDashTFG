CausalSim: A Causal Framework for
Unbiased Trace-Driven Simulation
Abdullah Alomar, Pouya Hamadanian, Arash Nasr-Esfahany,
Anish Agarwal, Mohammad Alizadeh, and Devavrat Shah, MIT
https://www.usenix.org/conference/nsdi23/presentation/alomar
This paper is included in the
Proceedings of the 20th USENIX Symposium on
Networked Systems Design and Implementation.
April 17–19, 2023 • Boston, MA, USA
978-1-939133-33-5
Open access to the Proceedings of the
20th USENIX Symposium on Networked
Systems Design and Implementation
is sponsored by

CausalSim:ACausalFrameworkforUnbiasedTrace-DrivenSimulation
AbdullahAlomar PouyaHamadanian ArashNasr-Esfahany AnishAgarwal
|     |     |     | ∗   |     |     | ∗   |     |     | ∗   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | MIT |     |     |     | MIT |     |     | MIT |     |     |     | MIT |     |     |
aalomar@mit.edu pouyah@mit.edu arashne@mit.edu anish90@mit.edu
|     |     |     | MohammadAlizadeh |                  |     |     |                  | DevavratShah |     |     |     |     |     |     |
| --- | --- | --- | ---------------- | ---------------- | --- | --- | ---------------- | ------------ | --- | --- | --- | --- | --- | --- |
|     |     |     |                  |                  | MIT |     |                  | MIT          |     |     |     |     |     |     |
|     |     |     |                  | alizadeh@mit.edu |     |     | devavrat@mit.edu |              |     |     |     |     |     |     |
Abstract algorithm,orarchitecturalchoice.Toaccountfortheeffectof
WepresentCausalSim,acausalframeworkforunbiased theremainingcomponentsthatarenotsimulated,wecollect
atracecapturingtheirbehaviorandreplayitwhilesimulating
| trace-driven | simulation. |     | Current | trace-driven | simulators |     |     |     |     |     |     |     |     |     |
| ------------ | ----------- | --- | ------- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thecomponentofinterestwiththeproposedintervention.
| assume | that the interventions |     | being | simulated | (e.g.,a | new |                  |     |                                 |     |     |     |     |     |
| ------ | ---------------------- | --- | ----- | --------- | ------- | --- | ---------------- | --- | ------------------------------- | --- | --- | --- | --- | --- |
|        |                        |     |       |           |         |     | Thekeyassumption |     | hereisthattheinterventionswould |     |     |     |     |     |
algorithm)wouldnotaffectthevalidityofthetraces.However,
real-worldtracesareoftenbiasedbythechoicesalgorithms notaffectthetracebeingreplayed,whichwerefertoasthe
make during trace collection, and hence replaying traces exogenous trace assumption. If this assumption does not
hold,replayingthetraceisinvalidandcouldleadtoincorrect
underaninterventionmayleadtoincorrectresults.CausalSim
addresses this challenge by learning a causalmodelofthe simulationresults.Thisproblemhasbeenreferredtoasbias
intrace-driven(ordata-driven)simulation[15,37].
systemdynamicsandlatentfactorscapturingtheunderlying
system conditions during trace collection. It learns these Itisdifficulttoguaranteetheexogenoustraceassumption
modelsusinganinitialrandomizedcontroltrial(RCT)undera in traces collected from real-world systems. Consider,for
fixedsetofalgorithms,andthenappliesthemtoremovebiases example,trace-drivensimulationofadaptivebitrate(ABR)
fromtracedatawhensimulatingnewalgorithms. algorithms [35,50,63,75]. It is common to use network
KeytoCausalSimismappingunbiasedtrace-drivensim-
|     |     |     |     |     |     |     | throughput | traces | from real | video | streaming |     | sessions | on  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --------- | ----- | --------- | --- | -------- | --- |
ulationtoatensorcompletionproblemwithextremelysparse Internet paths [38,75]. However,the throughput achieved
observations.Byexploitingabasicdistributionalinvariance whentheplayerdownloadsavideochunkiscausedbycertain
property present in RCT data,CausalSim enables a novel latent properties of the network path (e.g.,the underlying
tensorcompletionmethoddespitethesparsityofobservations. bottleneck capacity, the number and type of competing
Our extensive evaluation of CausalSim on both real and flows,etc.),as well as the particular choices made by the
syntheticdatasets,includingmorethantenmonthsofrealdata ABRalgorithm(thebitratechosenforeachchunk).Inother
from thePuffervideostreamingsystem shows itimproves words,thetracedatareflectsthecombinedeffectofthesetwo
simulation accuracy,reducing errors by 53% and 61% on causesandisbiasedbytheABRalgorithmsusedduringtrace
averagecomparedtoexpert-designedandsupervisedlearning collection.Tosimulateanewalgorithm,weneedtoteaseapart
baselines.Moreover,CausalSimprovidesmarkedlydifferent theeffectofthetwocauses,andpredicthowthetracewould
insights about ABR algorithms compared to the biased havechangedunderthedecisionsofthenewalgorithm.
baselinesimulator,whichwevalidatewitharealdeployment.
WepresentCausalSim,acausalframeworkforunbiased
|     |     |     |     |     |     |     | trace-driven | simulation. | CausalSim     |     | relaxes  | the | exogenous |      |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | ------------- | --- | -------- | --- | --------- | ---- |
|     |     |     |     |     |     |     | trace        | assumption  | by explicitly |     | modeling |     | the fact  | that |
1 Introduction
|                           |     |     |                           |     |     |     | interventions | can          | affect trace | data. | Using | traces | collected |     |
| ------------------------- | --- | --- | ------------------------- | --- | --- | --- | ------------- | ------------ | ------------ | ----- | ----- | ------ | --------- | --- |
|                           |     |     |                           |     |     |     | from          | a randomized | control      | trial | (RCT) | under  | a fixed   | set |
| CausaLatetVisEstNotissima |     |     | – Thecauseishidden,butthe |     |     |     |               |              |              |       |       |        |           |     |
resultisknown.(Ovid:MetamorphosesIV,287) ofalgorithms,itinfersboththelatentfactorscapturingthe
underlyingconditionsofthesystemandacausalmodelofits
| Trace-driven | simulation |     | is a | widely | used method | for |     |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | ---- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
dynamics,includingtheunknownrelationshipbetweenlatents,
| evaluatingnewideasin |     | systems. |     | In contrasttofull-system |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | -------- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
algorithmdecisions,andobservedtracedata.Tosimulatea
simulation(e.g.,NS3[31]),whichrequiresdetailedknowledge
newalgorithm,CausalSimfirstestimatesthelatentfactorsat
| of system | characteristics |     | (e.g., | topology, | traffic patterns, |     |     |     |     |     |     |     |     |     |
| --------- | --------------- | --- | ------ | --------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
everytimestepofeachtrace.Then,itusestheestimatedlatent
| hardware | details, | etc.), trace-driven |     | simulation | does | not |     |     |     |     |     |     |     |     |
| -------- | -------- | ------------------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
factorstopredictthealternateevolutionofthetrace,actions,
| model all | components | of  | a system. | Instead,it | focuses | on  |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andobservedvariablesofthecomponentofinterest,underthe
simulatingone(orafew)componentsofinterest,wherewe
samelatentconditionsthatwerepresentwhenthetracewas
wishtoexperimentwithanintervention,e.g.,anewdesign,
collected.Thistwo-stepprocessallowsCausalSimtoremove
*Equalcontribution thebiasinthetracedatawhensimulatingnewalgorithms.
USENIX Association 20th USENIX Symposium on Networked Systems Design and Implementation    1115

CausalSimprovidestwobenefits:(i)itimprovestheaccu- toatraceiscompletelyrandominanRCT,thedistributionof
racyoftrace-drivensimulationwhentheinterventioncouldaf- latentfactorsshouldbethesameforthetracesobtainedusing
fect(inpossiblysubtleways)thetracedata;(ii)itenablestrace- differentalgorithms,i.e.,thelatentdistributionisinvariant
drivensimulationofsystemswheredefininganexogenous to the algorithm. We provide conditions on the RCT data
traceisnotpossibleandthereforestandardtrace-drivensimu- (e.g.,intermsofthenumberanddiversityofalgorithms)that
lationisnotapplicable.Weevaluatebothsettingsinthispaper, guarantee recoverability of the low-rank matrix using this
bysimulatingABRandheterogeneousserverloadbalancing invarianceproperty(§4.2),andweoperationalizethisideain
algorithmsasexamplesforcases(i)and(ii)respectively. apracticallearningmethodthatexploitstheinvarianceusing
CausalSim requires training data from an RCT. Large anadversarialneuralnetworktrainingtechnique(§5).
networkoperatorshaveincreasinglyinvestedinRCTinfras- WeevaluateCausalSimontwousecases,ABRandserver
tructuretoevaluatenewideas,butduetotheirlowthroughput loadbalancing,withbothreal-worldandsyntheticdatasets,and
andriskofdisruptionsorSLAviolations[42],theycanafford furtherverifyCausalSim’spredictionswithatestinthewildon
toevaluateonlyafractionofproposedideasinRCTs.Causal- thePuffer[71]videostreamingtestbed.Ourmainfindingsare:
SimgreatlyextendstheutilityofRCTdatabylearningamodel 1. We use CausalSim to debug and improve an ABR
thatcansimulateawiderangeofalgorithmsusingtracesfrom algorithm,BOLA1[53,63].Inatenmonthexperimenton
afixedsetofalgorithms.Periodicallyorwheneveranoperator Puffer[71],BOLA1exhibitedhighstallingcomparedto
believestheunderlyingsystemcharacteristicshavechanged BBA[35],withslightlybetterquality.UsingCausalSim,
significantly,theycancollectfreshdatausinganRCT(again, wetuneBOLA1’sparametersviaBayesianOptimization
withthesamefixedsetofalgorithms)toretrainCausalSim. anddeployourimprovedversiononPuffer.Weshowthat
CausalSim’s design begins with the observation that itimprovesthestallrateofthiswell-knownalgorithmby
unbiasedtrace-drivensimulationcanbeviewedasamatrix(or 2.6 ,achieving0.7 thestallrateofBBAwithsimilar
× ×
tensor)completionproblem[9,14].ConsideramatrixMof perceptualquality.Theexpert-designedbaselinesimu-
traces(itisatensoriftracesarehigherdimensional),withrows latorthatignoresbiaspredictstheexactopposite:that
correspondingtopossibleactionsandcolumnscorresponding thenewvariantshouldstall1.34 thestallrateofBBA.
×
todifferenttimestepsinthetracedata.Foreachcolumn,the Thiscasestudyshowsthatremovingbiasiscrucialto
entryforoneactionis“revealed”;allotherentriesaremissing. drawaccurateconclusionsfromtrace-drivensimulation.
Ourtaskcanbeviewedasrecoveringthemissingentries. 2. EvaluationofCausalSimonmorethantenmonthsofreal
Asignificantbodyofworkhasshownthatitispossibleto datafromPuffershowsthatCausalSim’serrorinstall
recoveramatrixfromsparseobservationsundercertainas- ratepredictionisboundedto28%,whileexpert-designed
sumptionsaboutthematrixandthepatternofmissingdata. andstandardsupervisedlearningbaselineshaveerrorsin
Roughlyspeaking,thetypicalassumptionsthatmakerecovery therangeof49–68%and29–187%respectively.Similar
feasiblearethatthematrixhaslowrank,theentriesrevealedare observationsarealsomadeforperceptualqualitymetrics
chosenatrandom,andthatenoughentriesarerevealed.Low- andbufferoccupancylevels.
rankstructureisprevalentinmanyreal-worldproblems[69] 3. CausalSimopensupnewavenuestoapplytrace-driven
andhasalsobeenobservedinnetworkmeasurementdata[16, simulation to systems where the exogenous trace
43,44,60].Butunfortunatelytheothertwoassumptionsdo assumption is invalid. Using a synthetic environment
notholdinourproblem.Aswedetailin§4.3,oneobserved modelingaheterogeneousserverloadbalancingproblem,
entrypercolumnisbelowtheinformation-theoreticboundfor we show how CausalSim reduces average simulation
low-rankmatrixcompletion(evenforrankr=1).Moreover, error by 5.1 , a stark improvement compared to a
×
notonlyaretheentriesrevealedinourproblemnotrandom, baselinesimulatorwithamedianerrorof124.3%.
theydependonotherentriesofthematrix,sincetheactions This workdoes notraise any ethicalissues. Ourcode is
arebeingtakenbyalgorithmsbasedonobservedvariables. available at https://github.com/CausalSim/Unbiased-Trace-
Toovercomethesechallenges,CausalSimexploitstwokey Driven-Simulation.
insights.First,itassumesacausalmodel(§3)wherethelatent
factorsareexogenousandarenotaffectedbytheinterventions
2 Motivation
wewanttosimulateinthecomponentofinterest.Thisexoge-
nouslatentassumptionrelaxes(andisthereforeimpliedby)
2.1 BiasinTrace-DrivenSimulation
theexogenoustraceassumptioninstandardtrace-drivensimu-
lation.Forexample,inABR,itsaysthatunderlyingfactorslike Trace-drivensimulationisawidelyusedtechniquetodesign
thebottlenecklinkspeedonanetworkpatharenotaffectedby andevaluatesystems.Unlikefull-systemsimulation,itfocuses
auser’sABRalgorithm,whereasABRdecisionscanimpact onsimulatingone(orafew)componentsofthesystemwhile
thetracethatuserobserves(i.e.,theachievedthroughput). capturingtheeffectofremainingcomponentsbyreplaying
Second, CausalSim uses a basic property of trace data atrace.Forexample,tosimulatenewABRalgorithms,itis
collectedviaanRCT.Sincetheassignmentofanalgorithm commontoreplaynetworkthroughputtracesfromrealInternet
1116 20th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

algorithms.Intheperiodofinterest(July27,2020–June2,
2021),thetestedalgorithmsincludeBuffer-BasedAlgorithm
(BBA) [35], two versions of BOLA-BASIC (henceforth
calledBOLA)[63]3,andtwoversionsofanalgorithmcalled
FugudevelopedbythePufferauthors.Thedatasetincludes
morethan56millionchunkdownloadsfrommorethan230
thousandstreamingsessions,totaling3.5yearsofstreamed
videos. Foreach streaming session,it provides logs of the
chosen chunk sizes,available chunk sizes,achieved chunk
downloadthroughputs,andplaybackbufferlevels.4
Consideratypicaltrace-drivensimulationscenario,where
(a)Trace-drivensimulation (b)CausalSim
wewishtosimulateanewABRalgorithmusingtracesfrom
previousvideostreamingsessions.Wedefinesuchataskon
Figure1:CausalSimrelaxestheexogenoustraceassumption
thePufferdataasfollows.Weletoneofthealgorithms,say
instandardtrace-drivensimulation.1
BBA,be the algorithm thatwe wishto simulate. We leave
outthedataforthisalgorithmandaskwhetheritispossible
topredictitsperformanceusingtheotheralgorithms’traces.
pathsinasimulatormodelingonlythevideoplayer/server.
InevaluatinganewABRalgorithm,wemaybeinterestedin
Aswealludedtoearlier,thekeyassumptionhereisthatthe
various performance measurements,e.g. bufferoccupancy,
interventionsbeingsimulatedwouldnotaffectthetracebeing
rebuffering rate, chosen bitrates, etc. Here, we focus on
replayed;otherwise,replayingthetracewouldbeinvalid.We
predictingthebehaviorofplaybackbufferoccupancy,whichis
refertothisastheexogenoustraceassumption,anditiscentral
oneofthekeyindicatorsofanABRalgorithm’sbehavior[35].
to standard trace-driven simulation. Figure 1a is a visual
The goal of trace-driven simulation is to predict the
depictionoftheexogenoustraceassumption.Inthefigure,a
trajectory of the system (e.g.,buffer,bitrates,etc.) for one
representstheinterventionwewanttosimulate;forexample,
algorithminthesameunderlyingconditionsthatwerepresent
theactionstakenbyanewalgorithm.oistheobservedstate
whenatracewascollectedusingadifferentalgorithm.When
ofthecomponentbeingsimulated.urepresentsthelatentstate
simulating algorithm B based on a trace collected using
oftherestofthesystem,whichwedonotobserveorsimulate.
algorithmA,wewillrefertoAasthe“source”algorithmand
Finally,misthetrace,whichcapturesthebehavioroftheother
components.2Theexistenceofeachedgerepresentsacausal toBasthe“target”algorithm.
Itisgenerallynotpossibletoevaluatetheaccuracyofindi-
effect.Forexample,thetracemandinterventionabothaffect
vidualsimulatedtrajectoriesusingreal-worlddata,becausewe
o.Notetheabsenceoftheedgefromatom,whichimplies
donothavegroundtruthtrajectoriesforthetargetalgorithmun-
thattheinterventioncannotaffectthetrace(theexogenous
derthesameexactnetworkconditionsthatwerepresentwhen
traceassumption).
runningthesourcealgorithm.However,sincethePufferdata
Thesimulatordesignermustdefinethetracecarefullyto
wasobtainedusinganRCT,wecanevaluatepredictionsabout
meetthisassumption.Butwhathappensifitdoesnothold,i.e.,
distributionalpropertiesofthetargetalgorithm,suchasthe
thereexistsanedgefromatom(asinFigure1b)?Ignoring
distributionofthebufferoccupancyachievedbythealgorithm
theviolationofexogenoustraceassumptionleadstobiased
overthepopulationofnetworkpathspresentintheRCT.
simulationoutcomes,aswewillseenext.
Tosummarize,ourtaskis: predictthedistributionofthe
bufferoccupancyfortheusersassignedtoBBA(thetarget
2.2 AnExampleUsingReal-worldTraces algorithm)inthePufferdataset,usingonlythedatafromthe
other(source)algorithms.
Inthissection,weusemorethantenmonthsofreal-world
data from Puffer [71], a recently deployed system for
experimentingwithvideostreamingprotocols,toillustrate 2.2.1 SimulationviaExpertModeling(ExpertSim)
theissueofbiasintrace-drivensimulation.
Asourfirststrawman,webuildasimpletrace-drivensimulator
PuffercollectsdatafromacontinualRandomizedControl
(ExpertSim) using ourknowledge of how an ABR system
Trial (RCT) that tests several Adaptive Bit Rate (ABR)
works.ExpertSimmodelstheplaybackbufferdynamicsfor
1Ingeneral,aanducanbecorrelated.Forexample,theycanbothdepend eachstep,whereastepcorrespondstooneABRdecisionand
onpriorlatentconditionsofthesystem.InABR,forinstance,recentlatent
pathconditionsarecorrelatedwithcurrentpathconditions(u),andalsoaffect 3BOLA1andBOLA2arevariationsonBOLAadjustedtotargetthe
theactiontakenbytheABRalgorithm(a).Correlationofaandu,however, SSIMqualitymetricinsteadofbitrate[53].Theypursuedifferentobjective
doesnotimplyacausalrelationshipbetweenthem.Inparticular,ourmodel functionsandusedifferentprinciplesforhyperparameteradjustment.
assumesexogenouslatents,i.e.adoesnotaffectu. 4Weuse‘slowstream’logs(byPuffer’sdefinition,streamswithTCP
2VariablesinFig.1acanbemultidimensionalandvarywithtime. deliveryratesbelow6Mbps)availableonthePufferwebsite[1].
USENIX Association 20th USENIX Symposium on Networked Systems Design and Implementation 1117

|     |     | CausalSim |     |     |     |     |     | 2.2.2 SimulationviaSupervisedLearning(SLSim) |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
| 70  |     | ExpertSim |     |     |     |     |     |                                              |     |     |     |     |
SLSim
PerhapsthesimplemodelofbufferdynamicsinExpertSim
| )%(FDC 50 |     | BBA(target) |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
doesnotaccuratelyreflecttheactualsystembehavior.Asanext
BOLA2(source)
| 30  |     |     |     |     |     |     |     | attempt,weturntomachinelearningandtrytolearnthesystem |              |             |               |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | ------------ | ----------- | ------------- | --- |
| 10  |     |     |     |     |     |     |     | dynamicsfromdata.Specifically,weusesupervisedlearning |              |             |               |     |
|     |     |     |     |     |     |     |     | to train a Neural                                     | Network (NN) | that models | the step-wise |     |
|     | 0   |     | 5   | 10  |     | 15  |     | dynamicsofthesystem.ThisfullyconnectedNNincludes2     |              |             |               |     |
BufferOccupancy(seconds) hiddenlayers,eachwith128ReLUactivatedneurons.Foreach
timestept,theNNtakesasinputthebufferlevelbeforedown-
|     |     |     | (a) |     |     |     |     | loadingthetthchunkb,theachievedthroughputcˆ |                                  |     |            |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | -------------------------------- | --- | ---------- | --- |
|     |     |     |     |     |     |     |     |                                             | t                                |     | t forchunk |     |
| 70  |     |     |     |     |     |     |     | t,andthechunksizes                          | (whichdependsonthebiratechosenby |     |            |     |
|     |     | BBA |     |     |     |     |     |                                             | t                                |     |            |     |
ABR).TheNNoutputsthedownloadtimeofthetthchunk,and
| )%(FDC |     | BOLA2 |     |     |     |     |     |     |     |     |     |     |
| ------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
50
|     |     |     |     |     |     |     |     | theresultingbufferlevelb | .WetraintheNNtominimizethe |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | -------------------------- | --- | --- | --- |
t+1
| 30  |     |     |     |     |     |     |     | predictionerroronourdataset.Toavoidinformationleaking, |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- |
weexcludethelogsforBBAfromthetrainingdata.
10
Figure2ashowsthepredictedbufferleveldistributionvia
|     |     | 1   | 2   | 3   | 4   | 5   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thisapproach(SLSim)forBBA.AswithExpertSim,weuse
ObservedThroughput(Mbps) thetracescollectedfromBOLA2usersasthesourcealgorithm.
TheresultsaresimilartoExpertSim;onceagain,thepredicted
(b)
bufferdistributionisclosertothatofBOLA2thanBBA.
| Figure | 2: CausalSim |     | is  | accurate | in predicting |     | buffer |     |     |     |     |     |
| ------ | ------------ | --- | --- | -------- | ------------- | --- | ------ | --- | --- | --- | --- | --- |
(a)
| leveldistribution |     | ofBBA | users,while |     | baseline | simulators’ |     |                      |     |     |     |     |
| ----------------- | --- | ----- | ----------- | --- | -------- | ----------- | --- | -------------------- | --- | --- | --- | --- |
|                   |     |       |             |     |          |             |     | 2.2.3 WhatWentWrong? |     |     |     |     |
predictionsaresimilartoBOLA2users.(b)Distributionof
achievedthroughputisdifferentinBBAandBOLA2users. TounderstandthelimitationsofExpertSimandSLSim,we
plotthedistributionofachievedper-chunkthroughputforusers
assignedtoBOLA2andBBAinFigure2b.Sincealgorithm
| thedownloadofasinglevideochunk.Letcˆ |     |     |     |     | bethethroughput |     |     |                                                       |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --------------- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
|                                      |     |     |     |     | t               |     |     | selectioniscompletelyrandom,wewouldexpectinherentnet- |     |     |     |     |
achievedinstept(forthetthchunk)ofaparticularvideostream-
workpathpropertiessuchasbottlenecklinkcapacitytohave
| ing session | using,say,the |     | BOLA2 | algorithm. |     | To simulate |     |     |     |     |     |     |
| ----------- | ------------- | --- | ----- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
thesamedistributionforusersassignedtodifferentABRalgo-
BBAforthesameuser,ExpertSimassumesthattheuserwould
rithms.However,suchaninvarianceshouldnotbeexpectedfor
| achievethesamethroughputcˆ |     |     |     | ineachstepundertheBBAal- |     |     |     |                                                      |     |     |     |     |
| -------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- |
|                            |     |     |     | t                        |     |     |     | achievedthroughput,becauseevenonthesamepathdifferent |     |     |     |     |
gorithmaswell.Inotherwords,itassumesthatABRdecisions
ABRalgorithmscouldachievedifferentthroughput.Forexam-
donotaffecttheobservednetworkthroughput(theexogenous ple,sincecongestioncontrolprotocolstaketimetodiscover
traceassumption).Underthisassumption,ExpertSimmodels
availablebandwidth(e.g.,inslowstart)orconvergetotheir
| theevolutionofthevideoplaybackbufferasfollows.Letb |     |     |     |     |     |     | be  |                                                   |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- |
|                                                    |     |     |     |     |     |     | t   | fairshareratewhencompetingagainstotherflows,anABR |     |     |     |     |
thebufferlevelatthebeginningofstept(beforethedownload
algorithmthattendstochooselowerbitrates(andhencedown-
| ofchunkt),r | bethebitratechoseninstept,ands |     |     |     |     | bethesize |     |                                                     |     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- | --- | --------- | --- | --------------------------------------------------- | --- | --- | --- | --- |
|             | t                              |     |     |     |     | t         |     | loadlessdataperchunk)mayachievelessthroughputthanan |     |     |     |     |
ofthetthchunkimpliedbythechosenbitrate.Thenthebuffer
ABRalgorithmthatpickshigherbitrates[34,64].Wecansee
| attheendofsteptisderivedas:b |     |     |     | =max(0,b |     | s/cˆ)+T, |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- |
t+1 t − t t thisbehaviorinthePufferdataset.Theachievedthroughput
| where T | is the | chunk | duration.5 |     | Although | simple, | the |     |     |     |     |     |
| ------- | ------ | ----- | ---------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- |
forBOLA2andBBAisclearlydifferentinFigure2b.
| assumption | that | throughput | is  | an exogenous |     | property | of a |     |     |     |     |     |
| ---------- | ---- | ---------- | --- | ------------ | --- | -------- | ---- | --- | --- | --- | --- | --- |
ThisconfirmsthatABRalgorithmscauseabiasinthemea-
| networkpathiscommoninmodellingABRprotocols. |     |     |     |     |     |     | For |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
suredthroughputtraces,andtheexogenoustracepropertydoes
example,bothFastMPC[75]andFESTIVE[38]assumethat nothold.Toperformaccuratetrace-drivensimulation,weneed
theobservedthroughputdoesnotdependonthechosenbitrate.
toaccountforthisbiaswhensimulatingnewABRalgorithms.
| Figure | 2a shows | the | true distribution |     | of  | buffer level | for |     |     |     |     |     |
| ------ | -------- | --- | ----------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
BOLA2andBBAusersinthePufferdataset(thetwodashed
|     |     |     |     |     |     |     |     | 2.3 CausalInferencetotheRescue! |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- |
lines),aswellasthedistributionpredictedbyrunningBBA
onthetracescollectedfromBOLA2usersusingExpertSim Ifthetracesweretheunderlyingnetworkcapacitywheneach
| (solidblueline). |     | Thepredictionsareinaccurate: |     |     |     | thebuffer |     |     |     |     |     |     |
| ---------------- | --- | ---------------------------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
chunkwasdownloaded(ratherthantheachievedthroughput),
| distribution | generatedbyExpertSim |     |     |     | is more | similarto | the |     |     |     |     |     |
| ------------ | -------------------- | --- | --- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- |
theexogenoustraceassumptionwouldholdandourproblem
bufferdistributionofBOLA2users(thesourcealgorithm)than would be simple. First, we would learn the relationship
thebufferdistributionofBBAusers(thetargetalgorithm).
|     |     |     |     |     |     |     |     | between network | capacity | and achieved | throughput | for |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | -------- | ------------ | ---------- | --- |
differentABRactionsusingourdata.Then,tosimulateBBA
5Thecompletebufferdynamicequationisslightlymorecomplextohandle
caseswithfullbuffers.Referto§C.1intheappendixforfurtherclarification. foragiventrace,wewouldstartwiththenetworkcapacity
1118    20th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

ateachstepofthetraceandpredicttheachievedthroughput equations,andalso visualizedin Figure 1b by the absence
taking into accountthe bitrate chosen byBBA in thatstep. oftheedgefromatou. Notethatthisisastrictrelaxation
Thiswouldthenallowustopredicthowthebufferevolves. oftheexogenoustraceassumptioninstandardtrace-driven
Thisworksbecauseunlikeachievedthroughput,underlying simulation.There,thetraceitselfisassumedtobeunaffected
capacityisanexogenouspropertyofanetworkpathandis byintervention,whichalsoimpliesexogenouslatentfactors.
notaffectedbytheABRactions. InourrunningABRexample,wewanttosimulatethevideo
However,underlyingnetworkcapacityisalatentquantity playerandserver(componentsofinterest)withoutprecisely
— wedonotobserveitinourtraces. Thekeychallengeis modelingtheentirenetworkpath(therestofthesystem).Each
therefore to infersuchlatentquantities from observational timesteptcorrespondstothedownloadofanewchunk,andu
t
data.Concretely,inourrunningexample,wewishtoestimate
representslatentnetworkconditionsduringthattransmission,
thelatentfactorslikenetworkcapacityineachstepofatrace, e.g.,bottlenecklinkspeed,numberofflowssharingthesame
using observations such as the bitrate,the chunk size,the networkpath,typeofcongestioncontrolusedbycompeting
achievedthroughput,etc.6
flows,etc.Ateachtimestep,theABRalgorithmchoosesa
Inferring such latent confounders and using them for bitratea,whichtogetherwithu generatem,theachieved
|     |     |     |     |     | t   |     |     | t   | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
counterfactualpredictionisthecoreissueinthefieldofcausal
|     |     |     |     | throughput |     | when downloading |     | a chunk. | Typically, | latent |
| --- | --- | --- | --- | ---------- | --- | ---------------- | --- | -------- | ---------- | ------ |
inference [57,58]. In this paper,we develop CausalSim,a networkconditionsareexogenousfactors,beyondtheimpact
causalframeworkforunbiasedtrace-drivensimulation.Causal- ofaparticularuser’sactions.Forinstance,thebottlenecklink
Simrelaxestheexogenoustraceassumptionintrace-driven speedandtypeofcongestioncontrolthatcompetingflowsuse,
simulation.Itexplicitlymodelsthefactthatinterventionscan arenotaffectedbytheactionsoftheABRalgorithm.
affecttracedata(theedgefromatominFigure1b),andinfers
|     |     |     |     | Note | that | the achieved | throughput | depends | on  | the ABR |
| --- | --- | --- | --- | ---- | ---- | ------------ | ---------- | ------- | --- | ------- |
boththelatentfactorsandacausalmodelofthesystemdynam- actionaswellasthelatentnetworkconditions.Equation(1)
ics.ThisallowsCausalSimtocorrectforthebiasintracedata capturesthisrelationshipandisthesourceofthebiasinduced
whensimulatinganintervention.Asanillustration,Figure2a bytheABRalgorithm,whichwedemonstratedin§2.2.3.
showsthepredictedbufferoccupancydistributionwhensim- Thecausalmodelapplies
Whenisthemodelapplicable?
ulatingBBAonthetracesofusersassignedtoBOLA2,using
inanytrace-drivensimulationsettingwherethetracemaybe
CausalSim.CausalSimmatchestheground-truthdistribution impactedbyinterventions.Examplesinclude:
forBBAmuchmoreaccuratelythanthealternatives.
• Jobscheduling,wherewewishtosimulateaworkload’s
performanceunderdifferenttypesofmachines.Thetrace
3 ModelandProblemStatement
isthejobperformance(e.g.,runtime),interventionsare
theschedulingdecisions,andlatentfactorsareintrinsic
3.1 CausalModel
propertiesofeachjob(e.g.,computeintensity)orlatent
Consider the following discrete-time dynamical model7 aspectsofthemachinessuchascollocatedinterfering
| correspondingtoFigure1b: |      |          |     |     | workloads. |     |     |     |     |     |
| ------------------------ | ---- | -------- | --- | --- | ---------- | --- | --- | --- | --- | --- |
|                          | m =F | (a ,u ), | (1) |     |            |     |     |     |     |     |
t trace t t • Network simulation,where we wish to simulate how
o =F (o,m,a). (2) someaspectofnetwork’sdesign(e.g.,congestioncontrol,
|     | t+1 system | t t t |     |     |        |             |         |              |       |         |
| --- | ---------- | ----- | --- | --- | ------ | ----------- | ------- | ------------ | ----- | ------- |
|     |            |       |     |     | packet | scheduling, | traffic | engineering, | etc.) | impacts |
Here,t denotes the time index, m t is the trace, a t is the applicationperformance. Thetraceisanapplication’s
intervention,u isthelatentfactor,ando istheobservedstate traffic pattern,the intervention is the network design,
| t                                     |     | t         |     |     |     |     |     |     |     |     |
| ------------------------------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ofthecomponentofinterest.ThefunctionF |     | modelsthe |     |     |     |     |     |     |     |     |
trace andlatentfactorsaretheinternalsoftheapplicationthat
effectofinterventionsonthetrace(whichtraditionalmethods dictateitstrafficdemand.
| ignore),andF | modelsthedynamicsofthecomponent |     |     |     |     |     |     |     |     |     |
| ------------ | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
system
|     |     |     |     | In some | cases,like |     | our running | ABR example,the |     | exoge- |
| --- | --- | --- | --- | ------- | ---------- | --- | ----------- | --------------- | --- | ------ |
ofinterest.Whentheinterventionchangesanalgorithminthe
componentofinterest,a canbeviewedastheactiontaken nous trace assumption may not hold exactly but still be
t
bythatalgorithmattimet. roughlyvalid.8Here,CausalSimremovesbiasandimproves
Weassumethatinterventionsdonotaffecttheinternalstate simulation accuracy. Butin certain problems,ignoring the
oftherestofthesystem,i.e.,thatthelatentfactorsareexoge- effectofinterventionsismeaningless.Forexample,consider
|                       |               |                     |     | scheduling |                | or load balancing |          | on heterogeneous |       | machines |
| --------------------- | ------------- | ------------------- | --- | ---------- | -------------- | ----------------- | -------- | ---------------- | ----- | -------- |
| nous. This assumption | is implicitin | the dynamicalsystem |     |            |                |                   |          |                  |       |          |
|                       |               |                     |     | (e.g.,     | with different |                   | hardware | capabilities).   | Given | a trace  |
6Forsimplicity,weonlymentionnetworkcapacityhere,butotherlatent
|     |     |     |     | of job | performance |     | on specific | machines,it | isn’t | possible |
| --- | --- | --- | --- | ------ | ----------- | --- | ----------- | ----------- | ----- | -------- |
pathconditionslikethenumberofcompetingflowscouldalsoaffectachieved
tomerelyreplaythetracefornewmachineassignments.In
throughputandthesamereasoningappliestothem.
7ThismodelissimilartoaspecialtypeofPartiallyObservableMarkovian
DecisionProcesses(POMDPs)inwhichtheunobservedpartofthestateis 8Eveninthesecases,thesesubtlybiasedsimulationscanproduceentirely
| exogenous[51]. |     |     |     | incorrectconclusions(§6.2). |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
USENIX Association 20th USENIX Symposium on Networked Systems Design and Implementation    1119

suchproblems,CausalSim enables trace-driven simulation 4 CausalSim:TheoreticalInsights
byexplicitlymodelingtheeffectofinterventionsonthetrace.
Whenisthemodelinvalid? Ourcausalmodelrelaxesthe This section describes the theory behind CausalSim. We
exogenous trace assumption but still requires exogenous discusshowtooperationalizethistheoryinapracticallearning
algorithmin§5.Webeginbycastingcounterfactualestimation
latents,i.e.thatthelatentsareunaffectedbytheintervention.
Thiswon’tholdinallsystems.Forexample,wecannotmodel asachallengingvariantofthematrixcompletionproblem[14].
Wethenformalizeconditionsthatallowustocompletethe
theeffectofnetworkroutingpolicies(e.g.,BGP)onobserved
matrixusingacertaindistributionalinvariancepropertythat
videostreamingthroughputinthisway,sincechangingthe
pathwouldchangethelatentnetworkconditionsthatimpact ispresentindatacollectedinanRCT.
| a video  | stream. | Another  | example | is simulating |                | the effect |     |     |     |     |
| -------- | ------- | -------- | ------- | ------------- | -------------- | ---------- | --- | --- | --- | --- |
| of a CPU | feature | like the | branch  | predictor     | on instruction |            |     |     |     |     |
4.1 CounterfactualEstimation
throughput.Here,wecan’tmodelthestateoftheinstruction/- asMatrixCompletion
datacachesasanexogenouslatentfactor,sincechangingthe
branchpredictorcanchangetheirinternalstatesignificantly. Recall from §3.2 the task of estimating the counterfactual
|     |     |     |     |     |     |     | m˜i | Hi  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Overall,asimulation designerneedstoreason aboutthe trace consistentwithEquation(1).Inthissection,we
{ t}t=1
causalstructure ofobservedandlatentquantities to define posethistaskasavariantoftheclassicalmatrixcompletion
ai
theappropriatemodelintheformofEquations(1)and (2). problem. Forsimplicity,letaction t be one ofthe finitely
However,thedesignerdoesnotneedtopreciselyspecifythe manyoptions 1,...,A forsomeA 2.ImagineanAbyU
|     |     |     |     |     |     |     |     | { } | ≥   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
meaningofthelatentsorthedynamics(thefunctionsF matrixM,whererowscorrespondtoApotentialactions,and
trace
|     |     |     |     |     |     |     |     |     | ∑N  | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andF ).CausalSimlearnsbothfromobservationaldata. columns corresponds toU = H i latent factors (u for
| system |     |     |     |     |     |     |     |     | i=1 | t   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
differentchoicesofiandt)inthedataset.Toorderthecolumns,
ui
|     |     |     |     |     |     |     | we may index | t as a tuple | (i, t) andorderthese | tuples in |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | -------------------- | --------- |
3.2 ProblemFormulation lexicographic order. The matrix M is called the potential
outcomematrixinthecausalinferenceliterature[61].
We are given N trajectories, collected using K specific tth ith
|     |     |     |     |     |     |     | At the | step of the | trajectory, | we observe |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ----------- | ---------- |
policies.9 Let H be the length of trajectory i 1,...,N . m i = F (a i,u i), which is the entry in M in the row
|     |     | i   |     |     | ∈ { | }   | t trace | t t |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
Fortrajectoryi,we (mi,oi,ai)Hi correspondingtoaiandthecolumncorrespondingtoui.The
|     |     | observe |     | t t t t=1 | . We assume | that |     | t   |     | t   |
| --- | --- | ------- | --- | --------- | ----------- | ---- | --- | --- | --- | --- |
trajectories are generated using an RCT, i.e., that each counterfactual quantities of interest,m˜i = F (a˜i,ui) for
|     |     |     |     |     |     |     |     |     | t trace | t t |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
trajectoryisassignedtooneoftheKpoliciesatrandom. a˜i=ai,arethemissingentriesinMinthesamecolumn.In
t t
̸
Ourgoalistoestimatetheobservationsunderanarbitrary summary,weobserveoneentrypercolumnofthematrixM
givenintervention(e.g.,anewalgorithm)foreachoftheN andwewishtoestimatethemissingvaluesinthematrix.
ui Hi
trajectories.Let betheexogenouslatentfactorsfor Thetaskoffillingmissingvaluesinamatrixbasedonits
{ t}t=1
trajectoryi.Formally,foranygiventrajectoryiandgivena partiallyobservedentriesisknownasMatrixCompletion[19],
a˜i Hi ,startingwithobservationoi a topic that has seen tremendous progress in the past two
| sequenceofactions |     | t}t=1 |     |     |     | 1 and |     |     |     |     |
| ----------------- | --- | ----- | --- | --- | --- | ----- | --- | --- | --- | --- |
{
underthesamesequenceoflatentfactors ui Hi ,wewish decades[18,20,47]. However,standardmatrixcompletion
|                                         |     |     |     |     | t t= 1  |           |                                                   |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | ------- | --------- | ------------------------------------------------- | --- | --- | --- |
|                                         |     |     |     |     | { } H   |           | methodsdonotapplytoourproblem(see§4.3fordetails). |     |     |     |
| toestimatethecounterfactualobservations |     |     |     |     | o˜ i    | i thatare |                                                   |     |     |     |
|                                         |     |     |     |     | { t}t=1 |           |                                                   |     |     |     |
consistentwithEquations(1)and(2). Weuseadistributionalinvariancepropertyofdatacollected
usinganRCTtocompletethepotentialoutcomematrixM.
Thisisacounterfactualestimationproblemsinceitrequires
Thekeyobservationisthat,inanRCT,thelatentfactorsfor
| (i)estimatinglatent |     | ui  | Hi factorsforobservedtrajectoryi |     |     |     |     |     |     |     |
| ------------------- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- |
t}t=1
|                                               |                    | {   |       |      |              |        | trajectoriescollectedundereachofthepolicieswillhavethe |                                   |     |     |
| --------------------------------------------- | ------------------ | --- | ----- | ---- | ------------ | ------ | ------------------------------------------------------ | --------------------------------- | --- | --- |
| andusingthemalongwiththecounterfactualactions |                    |     |       |      |              | a˜i Hi |                                                        |                                   |     |     |
|                                               |                    |     |       |      |              | t}t=1  | samedistribution.                                      | Forexample,inPuffer’sRCT,incoming |     |     |
|                                               |                    |     |       |      | H            | {      |                                                        |                                   |     |     |
| to predict                                    | the counterfactual |     | trace | m˜ i | i consistent | with   |                                                        |                                   |     |     |
{ t }t = 1 usersareassignedtoanABRalgorithmatrandom.Therefore
| Equation | (1), and | then | (ii) using | the | counterfactual | trace |     |     |     |     |
| -------- | -------- | ---- | ---------- | --- | -------------- | ----- | --- | --- | --- | --- |
eachABRalgorithmwill“experience”thesamedistribution
i H
and actions to predict counterfactual observations o˜ i ofunderlyinglatentnetworkconditions,whichisprecisely
|     |     |     |     |     |     | { t }t = 1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
consistentwithEquation(2).
whywecancomparetheirperformanceintheRCT.Thesame
For (ii), learning F is a supervised learning task propertyhelpsusrecoverthematrixM,asweshownext.
system
| because | its inputs, | (oi,mi,ai), |     | and output, | oi , | are fully |     |     |     |     |
| ------- | ----------- | ----------- | --- | ----------- | ---- | --------- | --- | --- | --- | --- |
|         |             | t           | t t |             | t+1  |           |     |     |     |     |
Hi
| observed.       | If ui   | wasobserved,then(i)wouldalsoboil |     |     |     |     |                                      |     |     |     |
| --------------- | ------- | -------------------------------- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- |
|                 | { t}t=1 |                                  |     |     |     |     | 4.2 ExploitingRCTforMatrixCompletion |     |     |     |
| downtolearningF |         | inasupervisedmanner.Itisthelack  |     |     |     |     |                                      |     |     |     |
trace
|     |     | ui  | Hi  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of observability of that makes our simulation task Weuseaminimalnon-trivialexampletogiveintuitionabout
{ t}t=1
extremelychallenging.Inshort,weareleftwith(i),thetask how we can exploitan RCT formatrix completion,before
i H i andlearningF
| ofestimating | m˜  | t   |     | trace | .   |     | statingourmaintheoreticalresult. |     |     |     |
| ------------ | --- | --- | --- | ----- | --- | --- | -------------------------------- | --- | --- | --- |
{ }t = 1
ConsiderasimpleexamplewhereA=2andU=2n,and
9Weusepolicyandalgorithminterchangeablyinthispaper. therankofpotentialoutcomematrixMisequalto1.Rank1
1120    20th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

impliesthatM=auT forsomea R2andu R2nwithM = 1. (Low-Rank Factorization) M is a low-rank tensor
∈ ∈
α,β
a u .10SupposewehaveK=2policies,whereeachpolicyal- (rank = r),i.e.,it admits the following factorization:
w α a · ys β choosesonlyoneofthetwoactions.Furthermore,wecon- M α,β,γ =∑r ℓ=1 a αℓ u βℓ z γℓ .
sideranRCTsetting.Thatis,thedistributionoflatentfactors 2. (Invertibility) The factorization implies existence ofa
acrosstrajectoriesassignedtobothpoliciesshouldbethesame. linearmappingfromlatentencodingtotraceforeach
Withoutlossofgenerality,wecanre-orderthecolumnsof action.Thislinearmappingisinvertible.
Msothatthefirstncolumnscorrespondtothelatentfactorsof 3. (Sufficientmeasurements)D r.
≥
thetrajectoriesassignedtopolicy1,andthesecondncolumns 4. (Sufficient,Diverse Policies) The number of policies
arethoseassignedtopolicy2.Thentheobservedentriesof K Ar,andthe matrixS RAr × K is full-rankwhere
matrixMappearas x S ] w P . ≥ D (a :( c w t + io 1) n .D _ , i x nd = ex E = [m | w ac p t o io li n c ∈ _ y i _ n i d n e d x ex = = w, x p ) o . l L ic i y n _ e i a n r d i e n x d = e-
M M ... M ⋆ ... ⋆ ⋆ |
1,1 1,2 1,n pendenceofcolumnsofScanbeinterpretedasdiversity
⋆ ⋆ ... ⋆ M ... M M
2,n+1 2,2n 1 1,2n amongpolicies(AppendixA).
(cid:20) − (cid:21)
where⋆representsthemissingvalues.
LetusconsiderrecoveringthemissingobservationM .
2,1 4.3 Discussion
Forcolumn1,weknowtheobservationunderthefirstaction,
i.e.M .Duetorank1structure,wehave Whynotstandardtensorcompletion?Tensorcompletion
1,1
methods [26,41,48,78] make several assumptions. First,
M a u a
2,1 = 2 1 = 2 . (3) the tensor M must be (approximately) low rank, which
M a u a
1,1 1 1 1 CausalSimalsorequires.Low-rankstructureholdsinmany
Therefore,tofindM (andbyasimilarargument,tofindall real-worldproblems[69]andhasbeenobservedinnetwork
2,1
missingentriesofM),weneedtoestimatetheratio a2. measurements,e.g.,in traffic matrices [16,43,44,60] and
DuetothedistributionalinvarianceinducedbyR
a1
CT,the networkdistance(i.e.,RTT)[46,52,66].Asanexampleof
samples u ,...,u (which correspond to the latent factors howitemerges in the problems we studyin this paper,we
1 n
encounteredby policy 1) come from the same distribution useasimplemodelofcongestioncontrolinAppendixC.4to
asthesamplesu ,...,u (whichcorrespondtothelatent provideintuitionaboutlow-rankstructureinABRdata.
n+1 2n
factorsencounteredbypolicy2),forlargeenoughn. Thus, Second,thepatternofmissingentriesshouldberandom.
theirexpectedvalueshouldbeequal: Ifthemissingpatternsisnotrandomanddependsonlatent
factors or the entries themselves [8],standard approaches
1 n 1 2n havedifficultyrecoveringthetensor.Thisassumptiondoes
∑u ∑ u (4)
n β≈n β not hold in trace-driven simulation. Revealed entries are
β=1 β=n+1
determinedbytheactionstakenbythepolicies,whichoften
Equation(4)implies userecentobservationstomaketheirdecisions(e.g.,anABR
∑n β=1 M 1,β = ∑n β=1 a 1 · u β a 1 . (5) p th o e li r c e y ve m al a e y d/ u m s i e ss r i e n c g e e n n t t t r h ie r s ou in gh a p c u o t lu m m e n as a u re re n m o e t n ra ts n ) d . o H m e a n n c d e
∑2 β n =n+1 M 2,β ∑2 β n =n+1 a 2 · u β ≈a 2 dependontheentriesinpreviouscolumns.
Third,asufficientnumberofentriesneedtoberevealed.
ThisprovidespreciselythequantityofinterestinEquation(3)
Forexample,whenD=1(i.e.,whenM isamatrix),thein-
basedon the observedentries,enabling us to complete the
formationtheoreticlowerboundtoonthenumberofrevealed
matrix.
entriesneededtorecoverMis4Ur r2 [39,70].Thuseven
FormalResult. This simple illustrative example reliedon −
forrankr=1,itrequires4entriespercolumn,whereasonly
a convenient observational pattern (based on policies that
oneentrypercolumnisrevealedintrace-drivensimulation.
alwayschooseoneaction)andrank1structure.Buttheidea
Sincethesecondandthirdassumptionsdonotnecessarily
can be generalized. If the trace includes D measurements,
M RA U Dbecomesatensorratherthanamatrix,where holdinoursetup,wecannotuseexistingtensorcompletion
α,β,γ∈ × ×
methods. However, as we argued in §4.2, exploiting the
α,β,andγindextheactions,latentfactors,andmeasurements,
additionalproblemstructureimposedbyRCTdatacanmake
respectively. The following theorem provides conditions
tensorcompletionfeasibleincertainconditions.
where completion is possible fora rankr tensor. Formore
detailsandtheproof,refertoAppendixA. Limitations of Theorem 4.1. The proof of Theorem 4.1
(AppendixA)providesananalyticalmethodforrecovering
Theorem 4.1. We can recover all entries of M by only thetensorMthatgeneralizestheproceduredescribedforthe
observingoneD dimensionalelementineachcolumn(corre- simpleexamplein§4.2.Whilethisprovidesatheoreticalbasis
−
spondingtoonelatentandaction)ifthefollowingissatisfied: forwhytensorrecoveryispossible,theanalyticalapproach
10Notethatforreadability,weareabusingnotationbyoverloadingaand isnotpractical.First,itreliesonMbeingexactlyrankr;ifit
utorefertoboththeactionandlatent,andtheirencodingsinthefactorization. isapproximatelyrankr,wehavefoundthecalculationtobe
USENIX Association 20th USENIX Symposium on Networked Systems Design and Implementation 1121

Algorithm1CausalSimTraining
a˜t
1: initializeparametervectorsγ,θ,ϕ
2: initializehyper-parametersnum_disc_it,κ
|     |     | oi  |     | oi  | initializedatasetD |     |     |     | (o ,m ,a | ,π ) | m fromanRCT |     |
| --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | -------- | ---- | ----------- | --- |
|     |     | t̂  |     | t̂  | 3:                 |     |     |     | i i      | i i  | i=1         |     |
|     |     |     |     | +1  |                    |     |     | ←{  |          | }    |             |     |
4: foreachiterationdo
a
| t   |                               |      |                    |              | 5 :                     | fornu  | m _   | d is c_ it  | d o         |                 |          |         |
| --- | ----------------------------- | ---- | ------------------ | ------------ | ----------------------- | ------ | ----- | ----------- | ----------- | --------------- | -------- | ------- |
|     |                               | u t̂ | +                  |              |                         |        |       |             |             |                 |          |         |
|     |                               |      |                    |              |                         |        |       |             |             |                 | (o ,m ,a | ,π ) b  |
|     |                               |      |                    |              | 6 : rotanimircsiD       |        | s a m | p le m      | in i batchB |                 | l l      | l l l=1 |
| m   |                               |      |                    |              |                         |        |       |             |             | ←{              |          | }       |
| t   | Latent                        |      |                    |              | 7:                      |        | u     | E (m        | ,a )forl    | 1,...b          |          |         |
|     | F a c t o r                   |      |                    |              |                         |        | l ←   | θ           | l l         | ∈ {             | }        |         |
|     |                               |      |                    |              |                         |        | L     | 1Σb         | log         | W (π            | u )      |         |
|     | E xt r a c t o r              |      |                    |              | 8:                      |        | d isc | ←b          | l=1         | γ               | l l      |         |
|     |                               |      |                    |              |                         |        |       |             | −           |                 | |        |         |
|     |                               |      |                    |              | 9:                      |        | γ=γ   | λ γ         | ∇ γ L disc  |                 |          |         |
|     |                               |      |                    | P(π t |u t̂) |                         |        |       | −           | · (cid:2)   |                 | (cid:3)  |         |
|     |                               |      |                    |              | 10:                     | endfor |       |             |             |                 |          |         |
|     |                               |      |                    |              |                         | s a mp | le m  | in i b a tc | h B         | ( o ,o          | ,m ,a    | ,π ) b  |
|     |                               |      | P o lic y          |              | 1 1 :                   |        |       |             |             | l + 1           | l l      | l l l=1 |
|     |                               |      | Disc r im in a tor |              |                         |        |       |             | ←{          |                 |          | }       |
|     |                               |      |                    |              | 1 2 : seludoMnoitalumiS | u      | E (m  | , a )       | f or l      | 1 , .. . b      |          |         |
|     |                               |      |                    |              |                         | l      | ← θ   | l l         | ∈{          | }               |          |         |
|     |                               |      |                    |              |                         | L      | 1Σb   |             | logW        | (π u )          |          |         |
|     |                               |      |                    |              | 13:                     | disc   | ←b    | l=1         | γ           | l l             |          |         |
|     | Figure3:CausalSimArchitecture |      |                    |              |                         |        |       | −           |             | |               |          |         |
|     |                               |      |                    |              |                         | L      | 1     | Σb          | o           | P (o ,a(cid:3)l | ,u ) 2   |         |
|     |                               |      |                    |              | 14:                     | pred   |       | l=1(cid:2)  | l+1         | ϕ l             | l        |         |
|     |                               |      |                    |              |                         |        | ← b   |             | −           |                 |          |         |
|     |                               |      |                    |              |                         | L      | L     | hκ          | L           |                 |          |         |
brittle.Second,itappliesonlytodiscreteactionspaces.Third, 15: total pred (cid:0)· disc (cid:1) i
|                                                         |     |     |     |     |     |     | ←   | −       |       |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | --- | --- | --- |
|                                                         |     |     |     |     | 16: | θ=θ | λ   | θ ∇ θ L | total |     |     |     |
| itgivessufficientconditionsforrecovery,butthey’renotall |     |     |     |     |     |     | −   | ·       |       |     |     |     |
|                                                         |     |     |     |     | 17: | ϕ=ϕ | λ   | ∇ L     |       |     |     |     |
necessary.Onereasonisthattheanalyticalmethodusesonly − ϕ · ϕ pred
| meaninvariance,i.e.thefactthatthemeanofthelatentfactors |     |     |     |     | 18: endfor |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
isthesameacrossallpolicies(asinEq.(4)),eventhoughRCT
datahasthestrongerpropertythattheentiredistributionof
|     |     |     |     |     | accesstothesimulatedtrace(m˜ |     |     |     | t )values. |     |     |     |
| --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | ---------- | --- | --- | --- |
latentsdoesnotdependonthepolicy.Inthenextsection,we
|     |     |     |     |     | Overall, | CausalSim |     | uses | three | NNs | for counterfactual |     |
| --- | --- | --- | --- | --- | -------- | --------- | --- | ---- | ----- | --- | ------------------ | --- |
describeourpracticalimplementationofCausalSimthatuses
simulation;E
learningtechniquesandNNstoovercometheselimitations θ asthelatentfactorextractor,W γ asthepolicy
|                                        |     |     |     |     | discriminatorandP |     |     | asthecombinationofF |     |     |       | andF . |
| -------------------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | ------------------- | --- | --- | ----- | ------ |
| (attheexpenseoftheoreticalguarantees). |     |     |     |     |                   |     |     | ϕ                   |     |     | trace | system |
Figure3depictsthestructure.TrainingtheseNNsisquick;
onanA100NvidiaGPU,CausalSim’stimetoconvergence
5 CausalSim:Algorithm
on56Mdatapoints(230Kstreams)waslessthan10minutes,
CausalSim builds upon the insights presented earlier but and each simulation step in inference (on CPU) takes less
than150µs.Afullinferencerunonthesamevolumeofdata
replacesthefactorizedmodelwithalearningalgorithmbased
takeslessthan6hoursonasingleCPUcoreandlessthan20
onNNs.Foreaseofnotation,wewilldropthetrajectoryindex
minuteson32cores.
forallvariablesinthedataset,e.g.wewillrefertothelatent
factorui:t H,i Nasu :t H. Training procedure. CausalSim’s training procedure
| t   | ≤ i ≤ | t ≤ |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
alternatesbetween:(i)trainingthepolicydiscriminatorusinga
| CausalSim | architecture. | As discussed, | CausalSim | aims |     |     |     |     |     |     |     |     |
| --------- | ------------- | ------------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
to extract u and learn F and F from observed discriminationlossL disc ;and(ii)trainingothermodulesusing
|     | t   | trace | system |     |               |     |      |     |           |     |          |            |
| --- | --- | ----- | ------ | --- | ------------- | --- | ---- | --- | --------- | --- | -------- | ---------- |
|     |     |       |        |     | an aggregated |     | loss | L . | Algorithm | 1   | provides | a detailed |
trajectories (o t+1 ,o,m,a) t t t : t < H. Figure 3 summarizes total
CausalSim’salgorithmicstructure. pseudocodeofthistrainingprocedure.
Toextractlatentfactors,weuseaNNthattakesina t andm, t Training the policy discriminator (Lines 5–10 in Algo-
andcomputesuˆ (anestimateofu).Toapplyinvarianceonthe rithm 1). Distributional invariance means restricting the
|                                      | t   | t   |                     |     |                                                          |     |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | ------------------- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| extractedlatents,i.e.distributionofu |     |     | beingthesameregard- |     |                                                          |     |     |     |     |     |     |     |
|                                      |     |     | t                   |     | distributionoflatentfactorsutobeidenticalacrosspolicies. |     |     |     |     |     |     |     |
lessofthepolicyappliedtoit,weuseaNNcalledthePolicy Tothatend,wefirstuseE toextractlatentsuˆ,andthensearch
|     |     |     |     |     |     |     |     | θ   |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Discriminator.ThisNNaimstopredictthepolicypertaining forinvarianceviolationsviaadiscriminatorNN,astandard
tothatsamplegivenuˆ,andifinvarianceisupheld,itwillfailto t approach in the paradigm of adversarial learning [29,68].
doso.Unliketheanalyticalapproach,thepolicydiscriminator Specifically,thepolicydiscriminatoraimstopredictthepolicy
canenforcepolicyinvarianceontheentirelatentdistribution,
|     |     |     |     |     | π i thattookactiona |     |     | t fromtheestimatedlatentfactoruˆ |     |     |     | t (see |
| --- | --- | --- | --- | --- | ------------------- | --- | --- | -------------------------------- | --- | --- | --- | ------ |
potentiallyimprovingtheaccuracyoftheestimate. Figure3).Towardsthat,weuseacross-entropylosstotrain
To calculate the counterfactual traces and observations, thepolicydiscriminator:
| weneedtolearnF | andF  |                               |     |     |     |     |     |     |     |     |     |     |
| -------------- | ----- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                | trace | system .However,wecansimplify |     |     |     |     |     |     |     |     |     |     |
thelearningproblembymergingthesetwointoonesingle L =E [ logW (πuˆ)], (6)
|     |     |     |     |     |     |     | disc |     | B − | γ | |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
combinedfunction.Thus,weuseaNNthattakesincounter-
factualactionsa˜,observationo t t andestimatedlatentuˆ,and t wheretheexpectationisovertheasampledminibatchBfrom
computescounterfactualobservationo˜ .Ofcourse,wecan datasetD.Wetrainthepolicydiscriminatortominimizethis
t+1
| explicitlyuseseparateNNsforF |     |     | andF |     |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
trace system ifwerequire loss,byrepeatinggradientdecentnum_disc_it times,asthe
1122    20th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

policydiscriminatorneedsmultipleiterationstocatchupto todownload;2)averageStructuralSimilarityIndexMeasure
changesinthelatentfactors. (SSIM)indecibels,whichisaperceptualqualitymetric.Our
Trainingsimulationmodules(Lines11–17inAlgorithm1). groundtruthdatacomesfrompubliclogsof‘slowstreams’on
Puffer.Wheneveraclientinitiatesavideostreamingsession
Inthisstep,weneedtoimposeconsistencywithobservations,
allwhilepreservingthedistributionalinvariance. Thus,we inPuffer’swebsite,arandomABRalgorithmischosenand
computelatentfactorsuˆ withE andsimulatethenextstep assignedtothatsession. Sessionsarelogged(bufferlevels,
|     |     |     | t   | θ   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
chunksizes,timestamps,downloadtimes,etc)anonymously
| ofthetrajectoryoˆ |     | t+1 | withP | .Weuseanaggregatedlossto |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ----- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ϕ
enforceconsistencyandinvariance.Thislosscombinesthe andthedataisavailableforpublicuse.Ourdatasetcontains
morethan230KtrajectoriesfromanRCTduringJuly2020
negateddiscriminatorlosswithaquadraticconsistencyloss
|     |     |     |     |     |     |     |     | to June 2021,where |     | five | ABR algorithms | (BBA,BOLA1, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ---- | -------------- | ----------- | --- |
usingamixinghyper-parameterκ.
BOLA2,Fugu-CL,Fugu-2019)wereevaluated.Exhaustive
|           |             | =E  |           | )2     |           |           |     | detailsofthesetupanddatacanbefoundin§B.8. |     |     |     |     |     |
| --------- | ----------- | --- | --------- | ------ | --------- | --------- | --- | ----------------------------------------- | --- | --- | --- | --- | --- |
|           | L total     |     | B (o t+1  | oˆ t+1 | κL        | disc ,    | (7) |                                           |     |     |     |     |     |
|           |             |     |           | −      | −         |           |     |                                           |     |     |     |     |     |
|           |             |     | (cid:104) |        | (cid:105) |           |     |                                           |     |     |     |     |     |
| where the | expectation |     | is over   | the a  | sampled   | minibatch | B   |                                           |     |     |     |     |     |
fromdatasetD.Here,weusedaquadraticlossfunction,but 6.1.1 CanCausalSimsimulateapolicyithasnotseen?
onecoulduseanyconsistencylossfittothespecifictypeof
|     |     |     |     |     |     |     |     | WechooseoneofBBA,BOLA1,andBOLA211 |     |     |     |     | asthenew |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | -------- |
variable(e.g.Huberloss,Crossentropy,...).
Notethenegativesignofdiscriminatorloss,whichmeans policythatwewanttosimulate,andcallitthetargetpolicy.
wetraintheseNNstomaximizediscriminatorlossi.e.,fool Theremainingfourpoliciesarecalledsourcepolicies.Traces
thediscriminatortoensurepolicyinvariance.Iftheextracted assigned to the four source policies comprise our training
latent factors are policy invariant,the policy discriminator dataset,whichweusefortrainingCausalSimandthetwobase-
shoulddonobetteratitstaskthanguessingatrandom. lines.Thegoalistosimulatetheoutcomeofapplyingthetarget
Counterfactualestimation.Toproducecounterfactualesti- policyontrajectoriesassignedtoanyofthesourcepolicies.
mates,asdescribedabove,theestimatedlatentsuˆ t areextracted Figure 4a plots the stallrate andSSIM in the simulated
fromobserveddata.Usingtheextractedlatentsfactors,along trajectoriesandgroundtruth,denotingeachtargetpolicywith
withthelearnedcombinedfunctionP adifferentcolor.Foursourcepoliciesgiveusfourseparate
|     |     |     |     |     | γ ,westartwitho |     | 1 and |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
predictcounterfactualobservationsoˆ ,onestepatatime. predictionspertargetpolicyandsimulator.Eachpointdepicts
t+1
theaverageofthesefourpredictions,andtheintervalsshow
6 Evaluation theminimumandmaximumamongthefour.Foreithermetric,
|     |     |     |     |     |     |     |     | CausalSim   | is the         | most | faithful to ground     | truth | among all |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | ---- | ---------------------- | ----- | --------- |
|     |     |     |     |     |     |     |     | simulators. | Forinstance,in |      | stall rate,CausalSim’s |       | relative  |
WeevaluateCausalSim’sabilitytodoaccuratecounterfactual
simulation(§6.1and§6.3)usingtracedatafromonereal-world error spans 2 28%, while ExpertSim spans 49 68%
|         |           |          |     |            |       |             |     |           | −     |     |                 |     | −          |
| ------- | --------- | -------- | --- | ---------- | ----- | ----------- | --- | --------- | ----- | --- | --------------- | --- | ---------- |
|         |           |          |     |            |       |             |     | and SLSim | spans | 29  | 187%. CausalSim | may | not always |
| and one | synthetic | dataset. | As  | a rigorous | proof | of concept, |     |           |       | −   |                 |     |            |
predictthecorrectrelativeorderingamongpolicieswithclose
| we debug | andimprove |     | an ill-performing |     | ABR | policywith |     |     |     |     |     |     |     |
| -------- | ---------- | --- | ----------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
CausalSim(§6.2),andverifyitthroughdeploymentonapublic performance.Forexample,BOLA1andBOLA2(shownin
orangeandred)havesimilarperformanceinbothstallrateand
ABRtestinginfrastructure.Ourbaselinesareasfollows:
1. ExpertSim:Usestheanalyticalmodeldescribedin§2.2.1. SSIM.CausalSimpredictsthatthesepoliciesaresimilarbutit
2. SLSim:Usesastandardsupervised-learningtechniqueto inferstheirrelativeorderingincorrectly.However,CausalSim
|     |     |     |     |     |     |     |     | avoidsthelargeerrorsmadebythebaselinesimulators. |     |     |     |     | In  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
learnsystemdynamicsfromdata,asdescribedin§2.2.2.
Finally, we show how CausalSim enables trace-driven absoluteterms,itspredictionsareclosetothegroundtruth.
simulationinproblemswheredefininganexogenoustrace CausalSimalsohasthemostconsistentpredictionsacross
isnotstraightforwardandtraditionaltrace-drivensimulation differentsourcepolicies,becauseitremovesthebiasesofthe
isnotapplicable(§6.4).Furthersupportingexperimentsinthe sourcepolicies.Asanexample,weinvestigateallfoursimula-
appendixprovidemoredetailsabouthowCausalSimoperates tionresultsforBOLA1inFigure4b.SLSimandExpertSim’s
(§B.1,§B.2,§B.3,§B.4,§B.5,§B.7,§C.2,§C.3,§C.4 and simulationresultsareonlygoodwhenthesourcealgorithm
| §D.1). |     |     |     |     |     |     |     | isBOLA2(asimilaralgorithmtoBOLA1performance-wise). |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
However,theirpredictionsarefarofffromthegroundtruth
fortheotherthreesourcealgorithms.CausalSim’ssimulation
6.1 SimulationAccuracy
|     |     |     |     |     |     |     |     | results,on | the otherhand,are |     | allclose | to the groundtruth |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------------- | --- | -------- | ------------------ | --- |
WeuseCausalSimtopredicttheendperformanceofABR target.Appendix§B.7demonstratesthesameobservationfor
| policies, | and | compare | them | with | ground | truth data. | We  |     |     |     |     |     |     |
| --------- | --- | ------- | ---- | ---- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
othertargetalgorithms,i.e.BBAandBOLA2.
explorethesametwometricsreportedbyPuffertoevaluate
algorithms;1)stallrate,whichisthefractionoftimeauser
11WeexcludeFuguasatestpolicysincewecouldnotreproduceitslogged
| spentrebuffering,i.e. |     |     | pausedandwaiting |     | fora | new | chunk | actions(see§B.8). |     |     |     |     |     |
| --------------------- | --- | --- | ---------------- | --- | ---- | --- | ----- | ----------------- | --- | --- | --- | --- | --- |
USENIX Association 20th USENIX Symposium on Networked Systems Design and Implementation    1123

15.75
15.50
15.25
15.00
10 8 6 4 2
TimeSpentStalled(%)
)Bd(MISSegarevA
GroundTruth CausalSim ExpertSim SLSim
(a)
15.75
15.50
15.25
15.00
10 8 6 4 2
TimeSpentStalled(%)
)Bd(MISSegarevA
15.5
15.0
14.5
2.5 2.0 1.5 1.0
TimeSpentStalled(%)
GroundTruth CausalSim ExpertSim SLSim
(b)
Figure4:(a)Inareal-worlddatasetoflivevideostreaming,
CausalSimisthemostfaithful,comparedtotraditionaltrace-
driven(ExpertSim)ordata-driven(SLSim)simulators.Colors
indicate different target ABR algorithms. (b) Predictions
for BOLA1, separated by the source policy. Each point
indicatesadifferentsourceABRalgorithm.ExpertSimand
SLSimpredictionscarryoverbiasesofthesourcedata,while
CausalSimmitigatesthebias.
6.2 CaseStudy:CausalSimintheWild
An accurate simulator allows researchers to debug and
improveprotocolswithoutrepeatedandinvasivedeployments.
WeshalldemonstratethiswithCausalSim,byimprovinga
well-known ABR policy,andverifying ourfindings witha
real-worlddeploymentonPuffer.
RecallthatintheparticularRCTweusedin§6.1,fiveABR
algorithms(BBA,BOLA1,BOLA2,Fugu-CL,Fugu-2019)
wereevaluated.Figure5showstheresultofthisevaluation
for BBA, BOLA1 and BOLA2, across ‘slow streams’.12
SimilartoFigure4a,theX-axisshowsthestallrate,andthe
Y-axis is the average SSIM. BOLA1 exhibited 82% more
rebufferingcomparedtoBBA.ArevisedversionofBOLA1,
calledBOLA2,wasdeployedalongsideit,sincethePuffer
12ThedataforthisplotcomesdirectlyfromPuffer[2,3].
)Bd(MISSegarevA
BBA(Jul’20-Jun’21) BBA(Aug’22-Dec’22)
BOLA1(Jul’20-Jun’21) BOLA1-CausalSim(Aug’22-Dec’22)
BOLA2(Jul’20-Jun’21)
Figure 5: In an experiment preceding this work, BOLA1
exhibitshighstalling.BydeployingaBOLA1variantinalater
experimentCausalSimimprovedthestallrateby2.6 ,with
×
comparablequalitytoBBA.Userpopulationis‘slowstreams’
anderrorbarsdenote2.5%–97.5%confidenceintervals.
teamandtheauthorsofBOLAbelievedtheSSIMmetric(in
decibels) is incompatible withthe protocol [53]. This new
versionhad12.8%lessrebufferingandslightlyhigherquality,
butstillfartoomuchstallingcomparedtoBBA.
BOLA1 is an ABR policy with two hyperparameters,
similarto BBA,and ourhypothesis was that BOLA1 uses
sub-optimalhyperparameters.Toinvestigatethis,weusedthe
loggeddatapertainingtothatplotalongwithCausalSimto
exhaustivelyanalyzetheperformanceofBOLA1andBBAfor
arangeofhyperparameters.UsingBayesianOptimization13,
weexploredtheparameterspaceandcreatedaParetofrontier
curveforeachpolicy.Duringthisprocess,weevaluatedover
150differentalgorithmsintwodays,whichisachievableonly
inasimulator.Eachcurvedemonstratesthetrade-offbetween
qualityandstallrateinthatpolicy.Figure6presentsthecurves,
wheretheleftandrightplotsshowCausalSimandExpertSim
predictions.Foreaseofcomparison,wehighlightwherethe
originalBOLA1andBBAlie.CausalSimconfirmsoursus-
picion;thecurveforBOLA1isstrictlybetterthanthatofBBA.
WecanrevisethehyperparametersinBOLA1foranimproved
BOLA1variant,henceforthcalled‘BOLA1-CausalSim’.We
choseBOLA1-CausalSim,suchthatitwouldhavebetterstall
rateandmarginallybetterSSIMcomparedtoBBA.
Interestingly,ExpertSim predicts the complete opposite.
It predicts that not only will BBA always improve on any
BOLA1variantinatleastonemetric,butalsothatanyBOLA1
variant will stall more. This serves as a great opportunity
to test CausalSim’s edge compared to traditional (biased)
trace-drivensimulation,whichisusedinpriorwork[38,50,75].
TheresultsofBOLA1-CausalSim’sdeploymentcanbeseen
inFigure5.Consideringconfidenceintervals,itisclearthat
itstalls less than BBA; in fact,BBA stalls 43% more than
BOLA1-CausalSimonaverage.Theconfidenceintervalsfor
13WeuseaGaussianProcesspriorwithaMaternKernel[54].
1124 20th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

|     | BBAPareto |     |     | BBA |     | BOLA1-CausalSim |     |     |     |     |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
90
|     | BOLA1Pareto |     |     | BOLA1 |     |     |     |     |     |     |     | 0.7 |     |     |     |
| --- | ----------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Harder
|                 |     | CausalSim |     |     |     | ExpertSim |        | 70  |     |     |     |     |     |     |     |
| --------------- | --- | --------- | --- | --- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| )Bd(MISSegarevA |     |           |     |     |     |           |        |     |     |     |     | 0.5 |     |     |     |
| 15.50           |     |           |     |     |     |           | )%(FDC | 50  |     |     |     |     |     |     |     |
DME
|     |     |     |     |     |     |     |     | 30  |     | CausalSim |     | 0.3 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
15.25
ExpertSim
|     |     |     |     |     |     |     |     | 10  |     |     |     | 0.1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SLSim
| 15.00 |     | Better |     |     |     |     |     |     |     |     |     |      |      |      |     |
| ----- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | ---- | --- |
|       |     |        |     |     |     |     |     | 0.0 | 0.3 | 0.6 | 0.9 | 0.50 | 0.75 | 1.00 |     |
14.75
|     |     |     |     |     |     |         |     |     | EMD |     |     | BitrateMAD(Mbps) |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- |
|     |     | 5.0 |     | 2.5 |     | 5.0 2.5 |     |     |     |     |     |                  |     |     |     |
|     |     |     |     |     |     |         |     |     | (a) |     |     |                  | (b) |     |     |
TimeSpentStalled(%)
Figure7:Onaverage,CausalSimimprovestheEMDdistance
Figure6:ParetofrontiercurvesforBOLA1andBBAvariants. metriccomparedtoExpertSimandSLSimby53%and61%
CausalSim correctly predicts BOLA1’s potential,while respectively.(a)DistributionofCausalSim,ExpertSim,and
ExpertSimfailstodoso. SLSim EMDs over all possible source/target choices. (b)
Error(EMD)increasesforbaselineassimulationscenarios
qualityarewideandwillneedmoredatatobeseparable14, getharder,butCausalSimmaintainsgoodaccuracy.
butbasedontheongoingtrend,BOLA1-CausalSimwillhave
similarqualitycomparedtoBBA.
bufferlevel)mustbesimilarinthesimulatedtrajectoryand
OurgoalwastoshowCausalSim’spotential,andforthat
groundtruthtraceassignedtothetargetpolicy.Thismotivates
wetargetedoneofseveralplotsonPuffer(‘slowstreams’).
usingdistributionalsimilarityasourperformancemetric.
Wecouldhavechosenadifferentplottooptimizeon,butit
|                                                     |            |          |           |                |                      |                   |            | To quantify |                 | the similarity                     | of            | two   | distributions, |               | we use |
| --------------------------------------------------- | ---------- | -------- | --------- | -------------- | -------------------- | ----------------- | ---------- | ----------- | --------------- | ---------------------------------- | ------------- | ----- | -------------- | ------------- | ------ |
| wouldnotaffectthe                                   |            |          | takeaway. | Note           | thatouropportunities |                   |            |             |                 |                                    |               |       |                |               |        |
|                                                     |            |          |           |                |                      |                   | the        | Earth       | Mover           | Distance                           | (EMD)         | [62]. | We             | can calculate |        |
| for                                                 | deployment |          | on Puffer | are limited,as |                      | other researchers |            |             |                 |                                    |               |       |                |               |        |
|                                                     |            |          |           |                |                      |                   | EMD        | for         | one-dimensional |                                    | distributions |       | as EMD(P,Q)    |               | =      |
| use                                                 | Puffer     | as well; | hence     | we only        | deployed             | one BOLA1         | (cid:82)+∞ |             |                 |                                    |               |       |                |               |        |
|                                                     |            |          |           |                |                      |                   |            | P(x)        | Q(x)dx,         |                                    | where P       | and Q | are the        | Cumulative    |        |
| variant.Furthermore,wehopedtoalsocompareCausalSim’s |            |          |           |                |                      |                   |            | ∞ |         | −               | |                                  |               |       |                |               |        |
|                                                     |            |          |           |                |                      |                   | D−is       | tr ibution  | Functio         | n(CDF)sofpandq,respectively.Asmall |               |       |                |               |        |
predictionofstallrateandqualitywiththedeploymentresults,
EMDbetweentwodistributionsimpliesthattheyaresimilar.
buttheclientandnetworkpopulationhasclearlychanged;as
|     |     |     |     |     |     |     |     | Figure | 7a shows | the | CDF of | the EMD | (between |     | actual |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | ------ | ------- | -------- | --- | ------ |
showninFigure5,BBAachievesadifferentSSIMvaluefor
andsimulatedbufferleveldistributions)forCausalSimand
| thetwoperiodsoftime. |     |     |     | SinceCausalSim’spredictionsare |     |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
baselines,overallpossiblesource/targetpolicypairs.EMD
basedondatafromthepreviousRCT,directlycomparingthe
ofCausalSimissmallerthanEMDofbaselinesacrossalmost
predictedvaluestoresultsfromthenewRCTisn’tmeaningful.
|     |     |     |     |     |     |     | all | experiments. |     | In terms | of the | average | EMD | across | all |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ------ | ------- | --- | ------ | --- |
However,asourresultsshow,theoldRCTdataallowsusto
experiments,CausalSimbestsExpertSimandSLSimby53%
comparedifferentschemes.Forexample,CausalSimpredicts
|     |     |     |     |     |     |     | and | 61% | respectively. |     | Figure | 2a visualized |     | differences | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | ------------- | --- | ----------- | --- |
BBAstalls58%morethanBOLA1-CausalSimonnetwork
bufferleveldistributionsforthesimulationscenariowhere
distributionoftheoldRCT,whichisreasonablyclosetothe
BOLA2andBBAaresourceandtargetpolicies,respectively.
43%observedinthenewRCT(ignoringconfidenceintervals).
Toobservebufferleveldistributionsforallscenarios,referto
Figure9.
6.3 ACloserLookatSimulatedTrajectories In about 30% of cases, SLSim is slightly better than
|     |     |     |     |     |     |     | CausalSim. |     | These | cases | are “easy” |     | simulation | scenarios |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----- | ----- | ---------- | --- | ---------- | --------- | --- |
For a deep dive in simulator accuracy,we focus on buffer where the source and target policies make similar actions
occupancylevel,akeyindicatorofABRalgorithmbehavior.
(Formoredetailssee§B.3).Inthesecases,theEMDislow
Ideally,wewouldliketocomparesimulatedtrajectoriesto forbothCausalSimandbaselinesimulators(<0.15),andall
ground truth. But this isn’t possible using real trace data, performwell.Forinstance,Figure9c(intheAppendix)shows
sinceitrequiresustohavemultipletracesofdifferentpolicies
|     |     |     |     |     |     |     | source,target,andsimulatedbufferleveldistribution |     |     |     |     |     |     |     | in an |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- |
runningundertheexactsameunderlyingpathconditions.To easyscenario,whereBOLA2andBOLA1arethetargetand
| overcome |     | this issue,we |     | resort to | distributional | evaluation. |        |          |     |               |     |                           |     |     |     |
| -------- | --- | ------------- | --- | --------- | -------------- | ----------- | ------ | -------- | --- | ------------- | --- | ------------------------- | --- | --- | --- |
|          |     |               |     |           |                |             | source | policies |     | respectively. | In  | this example,allsimulated |     |     |     |
PufferdataiscollectedinanRCTsetting;hencethecharacter-
distributionsmatchthetargetdistributionquitewell.
isticsofnetworkpathsassignedtoeachpolicyisthesame.If
Figure7bshowswhereCausalSimmostshines,i.e.hard
weaccuratelysimulatethetargetpolicyontracesassignedto
simulationscenarios.TheY-axisistheerror(EMD),andthe
oneofthesourcepolicies,thedistributionofeachvariable(e.g. X-axisisthemeanabsolutedifference(MAD)betweenactions
takenbythesourcepolicyandthetargetpolicy,inSLSimsimu-
14Updatedplotscanbefoundonthe‘ExperimentalResults’pageofthe
lation.Thelargertheactiondifference,theharderthescenario
Pufferwebsite[1],under"Currentexperiment,fullcontiguousduration,slow
streamsonly". (§B.3).Aswemovetowardharderscenarios,theerrorincreases
USENIX Association 20th USENIX Symposium on Networked Systems Design and Implementation    1125

significantlyforthebaselines,whileCausalSimismorerobust. Wegenerateacollectionof5000trajectorieseachwith1000
stepsanduse16policiesintheloadbalancer.Foradetailed
explanationofthepolicies,jobsizegenerationprocess,and
6.3.1 Additionalexperiments
serverprocessingrates,referto§D.2.
We perform further evaluations of CausalSim in the ABR
environment.Duetospaceconstraints,wesummarizethese 6.4.1 Experimentsetup
resultshereanddeferdetailstotheappendix.
The aim of this experiment is to evaluate whether we can
Amorefine-grainedevaluation.Intheresultsabove,weeval-
simulate new unseen server assignment policies in this
uatedtheperformanceofCausalSimandbaselinesusingthe
environment,usingtracescollectedwithotherpolicies.Recall
distributionofbufferoccupancyacrossthewholepopulation.
thatwhile we observe the processing time ofeachjob,the
Onewaytofurthervalidatetheresultsistotestwhetherthey
actualsizeofthejobisnotobserved,i.e.,itactsasthelatent
willholdoncarefullypartitionedsub-populations. In§B.4,
factorinthisproblem.Forallsimulators,weassumeaccessto
weshowthatthisisindeedthecasewhenthesub-populations
F (thequeuemodel)andfocusonthemorechallenging
arepartitionedaccordingtotheMinRoundTripTime(RTT), system
taskoflearningF andestimatingthecounterfactualtraces
anetworkpropertythatisindependentoftheselectedABR trace
mˆtfori 5000,andt 1000.Algorithmically,thistranslates
algorithminPuffer. i ≤ ≤
toenforcingconsistencyfortheobservedtraces(m),rather
Hyperparameterstuning.Counterfactualestimation(§3.2) t
than the observations (o) (see §5). The trace we collectis
isinherentlyanOutofDistribution(OOD)predictiontask. t
theprocessingtimewhenusingasourceserverassignment
Hence,typicalsupervised-learninghyper-parametertuning
policy.Tosimulateatargetserverassignmentpolicy,weneed
methods do not work. In §B.5, we describe and evaluate
toestimatetheprocessingtimeofajobonserversotherthan
CausalSim’shyper-parametertuningprocedure.
the one where its processing time was measured (without
Groundtruthevaluation.Realdatanevercomeswithground
knowingeitherthejobsizeortheserverprocessingrates).
truthcounterfactuallabels. As a result,we cannotevaluate
Standardtrace-driven simulation assumes an exogenous
CausalSim’ssimulationsforeachtimestepinrealdata,butwe
trace(jobprocessingtime),butthisisthesameasassuming
candothisinareproduciblesyntheticenvironment.In§C.2,
servershaveequalprocessingrates.Thiscontradictstheprob-
we evaluate CausalSim using ground truth counterfactual
lemsetup,andstandardtrace-drivensimulation(analogousto
labelsandshowthatitstilloutperformsbaselinesintheMean
ExpertSiminABR)isnotapplicabletothisproblem.Thus,we
Absolute Percentage Error (MAPE) metric.15 Specfically,
compareCausalSimwithSLSimsimulations.SLSim(realized
CausalSimachievesanMAPEof( 5%),whichissignificantly
∼ byanNN)takesasinputtheobservedprocessingtimeandthe
lowerthanbothExpertSim’sandSLSim’s( 10%).
∼ targetserver,anditsoutputistheprocessingtimeunderthe
targetedserver.However,theobservedandtargetprocessing
6.4 ASecondExample:ServerLoadBalancing time are always the same in training data,and hence it is
impossible forSLSim to learn the true dynamics (e.g.,the
We now focus on simulating load balancing policies with
server’sunderlyingprocessingpower).CausalSimsidesteps
heterogeneousservers,wheredefininganexogenoustraceis
thisproblembyexplicitlyestimatinglatentfactors.Fordetails
notpossibleandthereforestandardtrace-drivensimulation
regarding the network architecture and training details for
isnotapplicable.ThisexampleshowshowCausalSimopens
bothSLSimandCausalSim,refertoTable8intheappendix.
upnewavenuesintrace-drivensimulation.
PerformanceMetric.WecompareCausalSimandSLSim
WeuseasyntheticenvironmentwhichconsistsofN=8
withtheunderlyinggroundtruthusingtheMAPEmetric.
servers (and a queue for each) with different processing
powers,aloadbalancer,andaseriesofjobsthatneedtobe
processedontheseservers.Eachjobhasaspecificsizewhich 6.4.2 CanCausalSimFaithfullySimulateNewPolicies?
isunknowntotheloadbalancer.Eachservercanprocessjobs
AsisdoneintheABRcasestudies,wetrainCausalSimand
ataspecificrate r N ,whichisalsounknowntotheload
{ i }i=1 SLSimmodelsbasedonadatasetgeneratedusingallpolicies
balancer. The load balancerreceives jobs and must assign
exceptone,whichwillbethetargetpolicy.Weusethesame
themtooneofN servers.Assumingthektharrivingjobhas
hyper-parameter tuning approaches explained in §B.5 for
sizeS andgetsassignedtoservera ,thejobprocessingtime
k k CausalSimand§B.6forSLSim.Wecarryoutthisevaluation
willbe S /r . Ifthis jobis notblockedbysome otherjob
k ak oneighttargetpolicies.Weevaluatetheperformanceforeach
beingprocessed,itslatencywillequalitsprocessingtime.If
pairofsource-targetpolicies,aswasdonein§6.1.Intotal,we
itisblocked,andthejobsaheadofitinthequeuetakeT to
k have120differentsource/targetpolicypairs.
beprocessed,theincurredlatencyisS /r +T .
k ak k InFigure8aandFigure8b,weshowtheCDFoftheMAPE
ofestimatingtheprocessingtimeandthelatency,respectively,
gro 1 u 5L nd et t p r ˆ u = th { q pˆ u i a } n N i= ti 1 ty an o d fi p nt = er { es p t i , } r N i e = s 1 p d ec e t n i o ve te ly s . th T e h v en ec , t M or A s P o E fp i r s ed d i e c fi te n d ed an a d s usingbothCausalSimandSLSim. Asevidentinthesetwo
MAPE(p,pˆ)=1 N 00∑N i=1| pˆi−pi pi|. figures,CausalSim’serrorissignificantlylowerthanthatof
1126 20th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

100
50
0
0 100 200 300
ProcessingtimeMAPE(%)
)%(FDC
100
50
CausalSim
SLSim 0
0 200 400
LatencyMAPE(%)
(a)
)%(FDC
InversePropensityScoring[33]andDoublyRobust[15]aim
topredictpopulation-levelperformancestatisticsforagivenin-
tervention.WISE[67]buildsaCausalBayesianNetworkfrom
thedatathatisabletoanswerinterventional(what-if)queries
CausalSim aboutthefuture,butthemethodrequiresabsenceoflatentcon-
SLSim foundingvariables.Sage[25]usesaCausalBayesianNetwork
modelwithlatentfactorstodiagnoseperformanceissuesin
microserviceapplications.Itanswerswhat-ifquestionsabout
(b) howinterventionslikechangingtheresourcesallocatedtoami-
croserviceimpactstheend-to-endapplicationlatency.Trace-
Figure8:DistributionofCausalSimandSLSimMAPEsover drivensimulationisdistinctfromallthesemethods,inthat
allsourcetargetpairs. itrequirescounterfactualpredictionsofhowanintervention
wouldhavechangedspecificpreviously-measuredtrajectories
SLSimforboththeprocessingtimeandlatency.Inparticular, ratherthanhowitchangespopulation-levelstatistics.16
themedianMAPEwhenestimatingprocessingtime/latencyis
24.4%/27.0%forCausalSimand124.3%/467.8%forSLSim.
8 ConcludingRemarks
For a complementary view,we compare the latent factors
CausalSimextractstothereallatentjobsizesandobservehow
Theexogenoustraceassumptioniscentraltotraditionaltrace-
closelytheymatch,in§D.1intheappendix.
driven simulation. CausalSim relaxes this key assumption,
bymodelingtheinterventioneffectonthetraceandlearning
7 Related-Work toreplaythetraceinanunbiasedmanner.Weshowedhow
thisimprovestheaccuracyoftrace-drivensimulationusing
Data-driven simulation. Traditional packet-level sim- real-worldABRdata,andhowCausalSimprovidesinsights
ulators [21, 31, 45] tend to sacrifice either scalability or foralgorithmimprovementthatareincontrastwithstandard
accuracy when simulating large networks. MimicNet [77] trace-drivensimulators’predictions,whichwevalidatedina
and DeepQueueNet [73] use machine learning to improve real-worlddeployment.Furthermore,weshowedhowthisex-
simulationspeedofdatacenternetworks. Theaforementioned pandstheapplicabilityoftrace-drivensimulationtoproblems
approaches are all full-system packet-level simulators, wheredefininganexogenoustraceisnotpossiblebyapplyingit
whereasCausalSimfocusesontrace-drivensimulationofa toheterogeneousserverloadbalancing.WebelieveCausalSim
specificsystemcomponentandmustthereforedealwithlatent couldbeappliedtomanyothersystemsimulationtasks.
factorsandbiasespresentintracedata. CausalSim opens up several interesting paths for future
Averyrecentwork,Veritas[17](publishedonarXivinAug. work.First,evaluatingCausalSiminproblemswithahigher-
2022),modelstrace-drivensimulationforABRasaHidden dimensionallatentfactorswouldbeinteresting.Second,itis
MarkovModel(HMM)withaknownemissionprocess.This anaturalnextsteptouseCausalSimformorecomplexpolicy
isequivalenttoassumingthatF trace isknowninourmodel(see optimizationmethods,e.g.,usingreinforcementlearning.Last,
Eq.(1)).VeritasusestheViterbialgorithmtodecodethelatent asdiscussedin§4.3,ourtheoreticalanalysisofCausalSim’s
factors,which are then used for counterfactual simulation. approach,i.e.exploitingthepolicyinvarianceoflatentfactors
CausalSimsolvesamoregeneralproblemwhereF trace isnot distributions,isnottight,andimprovingitcouldpotentially
knownandmustbelearned.Itthereforerequireslessknowl- relaxtheassumptionsofouranalyticalmethod.
edgeofthesystem’slatentsandunderlyingdynamicstoapply.
On the otherhand,CausalSim requires RCT data whereas
9 Acknowledgement
Veritasdoesnot.Comparingthefidelityoftheseapproaches
usingreal-worldABRdatawouldbeinterestingfuturework
WethankourshepherdKeithWinsteinforin-depthsuggestions,
(Veritasevaluatesitsmethodinanetworkemulator).
andourreviewersforinsightfulcomments.WethankthePuffer
Panthon’scalibratedemulators[72]modeltheend-to-end
team,specificallyEmilyMarxandFrancisY.Yanforproviding
behaviourofanetworkpathwithasimplemodelincluding
uswiththedataweusedin§6.1andthealgorithmdeployment
a handfulofparameters,e.g.,bottlenecklinkrate,constant
in §6.2. This workwas supportedby NSF grants 1751009
propagation delay,etc.,which are tuned to fit a collection
and1955370,anawardfromtheSystemsThatLearn@CSAIL
ofpackettraces collectedfrom this pathusing a varietyof
program,andagiftfromIntelaspartoftheMITDataSystems
congestioncontrolprotocols.iBox[13]extendsthisapproach
andAILab(DSAIL).A.AlomarandD.Shahweresupported
bymodeling cross-traffic. CausalSim does notassume any
inpartbyDSO-Singaporeproject,MIT-IBMprojectonCausal
knownmodelforthedynamicsofthenetwork.Furthermore,
representationlearningandNSFFODSIproject.
ithasaccesstoonlyasingletracefromeachnetworkpath.
Policy evaluation. Policy evaluation techniques such as 16AppendixEprovidesabroaderoverviewofthecausalinferenceliterature.
USENIX Association 20th USENIX Symposium on Networked Systems Design and Implementation 1127

References [13] SachinAshok,ShubhamTiwari,NagarajanNatarajan,
VenkataNPadmanabhan,andSundararajanSellaman-
| [1] Puffer: | Experimental |     | results. https://puffer. |     |        |                                           |     |     |     |
| ----------- | ------------ | --- | ------------------------ | --- | ------ | ----------------------------------------- | --- | --- | --- |
|             |              |     |                          |     | ickam. | Data-drivennetworkpathsimulationwithibox. |     |     |     |
stanford.edu/results/. Accessed:2023-2-22. ProceedingsoftheACMonMeasurementandAnalysis
ofComputingSystems,6(1):1–26,2022.
| [2] Puffer: | Total | scheme                      | statistics | - decmeber |            |               |         |         |             |
| ----------- | ----- | --------------------------- | ---------- | ---------- | ---------- | ------------- | ------- | ------- | ----------- |
| 27th,       | 2022. | https://storage.googleapis. |            |            |            |               |         |         |             |
|             |       |                             |            |            | [14] Susan | Athey, Mohsen | Bayati, | Nikolay | Doudchenko, |
com/puffer-data-release/2022-12-27T11_
|     |     |     |     |     | GuidoImbens,andKhashayarKhosravi. |     |     |     | Matrixcom- |
| --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | ---------- |
2022-12-28T11/duration_slow_scheme_stats_ pletionmethodsforcausalpaneldatamodels. Journalof
| 2022-12-27T11_2022-12-28T11.txt. |     |     |     | Accessed: |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
theAmericanStatisticalAssociation,pages1–15,2021.
2023-2-22.
[15] MihovilBartulovic,JunchenJiang,SivaramanBalakr-
[3] Puffer:Totalschemestatistics-july2nd,2021.https:// ishnan, Vyas Sekar, and Bruno Sinopoli. Biases in
storage.googleapis.com/puffer-data-release/ data-drivennetworking,andwhattodoaboutthem. In
2021-06-01T11_2021-06-02T11/duration_slow_
Proceedingsofthe16thACMWorkshoponHotTopics
scheme_stats_2021-06-01T11_2021-06-02T11. inNetworks,pages192–198,2017.
| txt.                                     | Accessed:2023-2-22. |     |     |           |                                        |                |         |        |              |
| ---------------------------------------- | ------------------- | --- | --- | --------- | -------------------------------------- | -------------- | ------- | ------ | ------------ |
|                                          |                     |     |     |           | [16] Vineet                            | Bharti, Pankaj | Kankar, | Lokesh | Setia, Gonca |
| [4] A.Abadie,A.Diamond,andJ.Hainmueller. |                     |     |     | Synthetic |                                        |                |         |        |              |
|                                          |                     |     |     |           | Gürsun,AnukoolLakhina,andMarkCrovella. |                |         |        | Inferring    |
controlmethodsforcomparativecasestudies:Estimat- invisibletraffic. InProceedingsofthe6thInternational
ingtheeffectofcaliforniaâstobaccocontrolprogram. COnference,Co-NEXT’10,NewYork,NY,USA,2010.
JournaloftheAmericanStatisticalAssociation,2010. AssociationforComputingMachinery.
[5] A.AbadieandJ.Gardeazabal. Theeconomiccostsof [17] ChandanBothra,JianfeiGao,SanjayRao,andBruno
conflict:Acasestudyofthebasquecountry. American Ribeiro. Veritas:Answeringcausalqueriesfromvideo
EconomicReview,2003.
|                                        |     |     |     |            | streamingtraces. | arXiv/2208.12596,August2022. |           |       |               |
| -------------------------------------- | --- | --- | --- | ---------- | ---------------- | ---------------------------- | --------- | ----- | ------------- |
| [6] AnishAgarwal,AbdullahAlomar,Varkey |     |     |     | Alumootil, |                  |                              |           |       |               |
|                                        |     |     |     |            | [18] Changxiao   | Cai,Gen                      | Li,Yuejie | Chi,H | Vincent Poor, |
DevavratShah,DennisShen,ZhiXu,andCindyYang. andYuxinChen. Subspaceestimationfromunbalanced
Persim: Data-efficient offline reinforcement learning andincompletedatamatrices:ℓ statisticalguarantees.
2,∞
withheterogeneousagentsviapersonalizedsimulators. TheAnnalsofStatistics,49(2):944–967,2021.
arXivpreprintarXiv:2102.06961,2021.
|     |     |     |     |     | [19] EmmanuelJCandèsandBenjaminRecht. |     |     |     | Exactmatrix |
| --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | ----------- |
[7] AnishAgarwal,AbdullahAlomar,andDevavratShah. completion via convex optimization. Foundations of
On multivariate singular spectrum analysis. arXiv Computationalmathematics,9(6):717–772,2009.
e-prints,pagesarXiv–2006,2020.
|     |     |     |     |     | [20] EmmanuelJCandèsandTerenceTao. |     |     |     | Thepowerofcon- |
| --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | -------------- |
[8] Anish Agarwal, Munther A. Dahleh, Devavrat Shah, vexrelaxation:Near-optimalmatrixcompletion. IEEE
andDennis Shen. Causalmatrixcompletion. ArXiv, TransactionsonInformationTheory,56(5):2053–2080,
| abs/2109.15154,2021. |     |     |     |     | 2010. |     |     |     |     |
| -------------------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
[9] AnishAgarwal,DevavratShah,andDennisShen. Syn- [21] XinjieChang. Networksimulationswithopnet. InPro-
theticinterventions. arXivpreprintarXiv:2006.07691, ceedingsofthe31stConferenceonWinterSimulation:
| 2021. |     |     |     |     | Simulation—aBridgetotheFuture-Volume1,WSC’99, |     |     |     |     |
| ----- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- |
page307–314,NewYork,NY,USA,1999.Association
| [10] Anish | Agarwal, | Devavrat | Shah, Dennis | Shen, and |     |     |     |     |     |
| ---------- | -------- | -------- | ------------ | --------- | --- | --- | --- | --- | --- |
forComputingMachinery.
| Dogyoon | Song. | On robustness | of principal | compo- |     |     |     |     |     |
| ------- | ----- | ------------- | ------------ | ------ | --- | --- | --- | --- | --- |
nent regression. Journal of the American Statistical [22] DASHIndustryForm. Referenceclient2.4.0,2016.
Association,2021.
|     |     |     |     |     | [23] RajeevHDehejiaandSadekWahba. |     |     |     | Causaleffectsin |
| --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --------------- |
[11] MuhammadAmjad,VishalMisra,DevavratShah,and nonexperimentalstudies: Reevaluatingtheevaluation
DennisShen. Mrsc:Multi-dimensionalrobustsynthetic oftrainingprograms. JournaloftheAmericanstatistical
control. Proc. ACMMeas. Anal. Comput. Syst.,3(2), Association,94(448):1053–1062,1999.
June2019.
|     |     |     |     |     | [24] Andrew | Forney, Judea | Pearl, | and Elias | Bareinboim. |
| --- | --- | --- | --- | --- | ----------- | ------------- | ------ | --------- | ----------- |
[12] MuhammadAmjad,DevavratShah,andDennisShen. Counterfactual data-fusion for online reinforcement
Robustsyntheticcontrol. JournalofMachineLearning learners. In International Conference on Machine
Research,19(22):1–51,2018. Learning,pages1156–1164.PMLR,2017.
1128    20th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

[25] Yu Gan, Mingyu Liang, Sundar Dev, David Lo, and video streaming service. In Proceedings ofthe 2014
Christina Delimitrou. Sage: Practical and scalable ACMConferenceonSIGCOMM,SIGCOMM’14,page
ml-drivenperformancedebugginginmicroservices. In 187–198,NewYork,NY,USA,2014. Associationfor
Proceedingsofthe26thACMInternationalConference ComputingMachinery.
onArchitecturalSupportforProgrammingLanguages
|              |                |     |          |          | [36] GuidoWImbens.                       |     | Nonparametricestimationofaverage |     |     |     |        |
| ------------ | -------------- | --- | -------- | -------- | ---------------------------------------- | --- | -------------------------------- | --- | --- | --- | ------ |
| andOperating | Systems,ASPLOS |     | ’21,page | 135–151, |                                          |     |                                  |     |     |     |        |
|              |                |     |          |          | treatmenteffectsunderexogeneity:Areview. |     |                                  |     |     |     | Review |
NewYork,NY,USA,2021.AssociationforComputing
ofEconomicsandstatistics,86(1):4–29,2004.
Machinery.
[37] JunchenJiang,VyasSekar,IonStoica,andHuiZhang.
[26] SilviaGandy,BenjaminRecht,andIsaoYamada.Tensor
|     |     |     |     |     | Unleashingthepotentialofdata-drivennetworking. |     |     |     |     |     | In  |
| --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- |
completionandlow-n-ranktensorrecoveryviaconvex
InternationalConferenceonCommunicationSystems
| optimization. | Inverseproblems,27(2):025010,2011. |     |     |     |     |     |     |     |     |     |     |
| ------------- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andNetworks,pages110–126.Springer,2017.
[27] SahajGarg,VincentPerot,NicoleLimtiaco,AnkurTaly,
|                       |     |                          |     |     | [38] JunchenJiang,VyasSekar,andHuiZhang. |     |     |     |     | Improving |     |
| --------------------- | --- | ------------------------ | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --------- | --- |
| EdHChi,andAlexBeutel. |     | Counterfactualfairnessin |     |     |                                          |     |     |     |     |           |     |
fairness,efficiency,andstabilityinhttp-basedadaptive
| textclassificationthroughrobustness. |     |     | InProceedings |     |       |           |      |          |                |     |        |
| ------------------------------------ | --- | --- | ------------- | --- | ----- | --------- | ---- | -------- | -------------- | --- | ------ |
|                                      |     |     |               |     | video | streaming | with | festive. | In Proceedings |     | of the |
ofthe2019AAAI/ACMConferenceonAI,Ethics,and
8thinternationalconferenceonEmergingnetworking
Society,pages219–226,2019.
experimentsandtechnologies,pages97–108,2012.
| [28] Ian Goodfellow, | Jean Pouget-Abadie, |     | Mehdi | Mirza, |     |     |     |     |     |     |     |
| -------------------- | ------------------- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
[39] MaryiaKabanava,HolgerRauhut,andUlrichTerstiege.
| Bing Xu, | David Warde-Farley, | Sherjil | Ozair, | Aaron |     |     |     |     |     |     |     |
| -------- | ------------------- | ------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
Ontheminimalnumberofmeasurementsinlow-rank
| Courville,andYoshuaBengio. |     | Generativeadversarial |     |     |                 |     |                                 |     |     |     |     |
| -------------------------- | --- | --------------------- | --- | --- | --------------- | --- | ------------------------------- | --- | --- | --- | --- |
|                            |     |                       |     |     | matrixrecovery. |     | In2015InternationalConferenceon |     |     |     |     |
nets.Advancesinneuralinformationprocessingsystems,
|     |     |     |     |     | Sampling | Theory | and | Applications | (SampTA), |     | pages |
| --- | --- | --- | --- | --- | -------- | ------ | --- | ------------ | --------- | --- | ----- |
27,2014.
382–386,2015.
[29] IanGoodfellow,JeanPouget-Abadie,MehdiMirza,Bing
|     |     |     |     |     | [40] DiederikPKingmaandJimmyBa. |     |     |     | Adam:Amethodfor |     |     |
| --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --------------- | --- | --- |
Xu,DavidWarde-Farley,SherjilOzair,AaronCourville, stochasticoptimization.arXivpreprintarXiv:1412.6980,
| andYoshuaBengio. | Generativeadversarialnetworks. |     |     |     |     |     |     |     |     |     |     |
| ---------------- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2014.
CommunicationsoftheACM,63(11):139–144,2020.
|     |     |     |     |     | [41] Daniel | Kressner, | Michael |     | Steinlechner, | and | Bart |
| --- | --- | --- | --- | --- | ----------- | --------- | ------- | --- | ------------- | --- | ---- |
[30] RuochengGuo,LuCheng,JundongLi,PRichardHahn,
|     |     |     |     |     | Vandereycken. |     | Low-rank | tensor | completion |     | by rie- |
| --- | --- | --- | --- | --- | ------------- | --- | -------- | ------ | ---------- | --- | ------- |
and Huan Liu. A survey of learning causality with mannian optimization. BIT Numerical Mathematics,
| data:Problemsandmethods. |     | ACMComputingSurveys |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
54(2):447–468,2014.
(CSUR),53(4):1–37,2020.
|     |     |     |     |     | [42] SShunmugaKrishnanandRameshKSitaraman. |     |     |     |     |     | Video |
| --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | ----- |
[31] ThomasRHenderson,MathieuLacage,GeorgeFRiley,
|     |     |     |     |     | stream | quality | impacts | viewer | behavior: | inferring |     |
| --- | --- | --- | --- | --- | ------ | ------- | ------- | ------ | --------- | --------- | --- |
CraigDowell,andJosephKopena. Networksimulations causalityusingquasi-experimentaldesigns. IEEE/ACM
| with the ns-3 | simulator. | SIGCOMM | demonstration, |     |     |     |     |     |     |     |     |
| ------------- | ---------- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
TransactionsonNetworking,21(6):2001–2014,2013.
14(14):527,2008.
|     |     |     |     |     | [43] Anukool | Lakhina, | Mark | Crovella, | and | Christophe |     |
| --- | --- | --- | --- | --- | ------------ | -------- | ---- | --------- | --- | ---------- | --- |
[32] Paul W Holland. Statistics and causal inference. Diot. Diagnosing network-wide traffic anomalies.
Journal of the American statistical Association, ACM SIGCOMM computer communication review,
81(396):945–960,1986.
34(4):219–230,2004.
[33] Daniel G Horvitz and Donovan J Thompson. A [44] Anukool Lakhina, Konstantina Papagiannaki, Mark
generalization ofsampling withoutreplacementfrom Crovella,ChristopheDiot,EricD.Kolaczyk,andNina
a finite universe. Journalofthe American statistical Taft. Structuralanalysisofnetworktrafficflows. SIG-
Association,47(260):663–685,1952.
METRICSPerform.Eval.Rev.,32(1):61–72,jun2004.
[34] Te-Yuan Huang, Nikhil Handigol, Brandon Heller, [45] BobLantz,BrandonHeller,andNickMcKeown. Anet-
NickMcKeown,andRameshJohari. Confused,timid, workinalaptop:rapidprototypingforsoftware-defined
and unstable: picking a video streaming rate is hard. networks. InProceedingsofthe9thACMSIGCOMM
| In Proceedings | of the 2012 | internet | measurement |     |     |     |     |     |     |     |     |
| -------------- | ----------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
WorkshoponHotTopicsinNetworks,pages1–6,2010.
conference,pages225–238,2012.
[46] YongjunLiao,WeiDu,PierreGeurts,andGuyLeduc.
[35] Te-Yuan Huang, Ramesh Johari, Nick McKeown, Dmfsgd:Adecentralizedmatrixfactorizationalgorithm
MatthewTrunnell,andMarkWatson. Abuffer-based for network distance prediction. IEEE/ACM Trans.
approach to rate adaptation: Evidence from a large Netw.,21(5):1511–1524,oct2013.
USENIX Association 20th USENIX Symposium on Networked Systems Design and Implementation    1129

[47] GregLinden,BrentSmith,andJeremyYork. Amazon. [60] Matthew Roughan,Yin Zhang,Walter Willinger,and
com recommendations: Item-to-item collaborative Lili Qiu. Spatio-temporal compressive sensing and
filtering. IEEEInternetcomputing,7(1):76–80,2003. internettrafficmatrices(extendedversion). IEEE/ACM
TransactionsonNetworking,20(3):662–676,2012.
[48] JiLiu,PrzemyslawMusialski,PeterWonka,andJieping
Ye. Tensorcompletionforestimatingmissingvaluesin [61] DonaldBRubin. Causalinferenceusingpotentialout-
visualdata. IEEEtransactionsonpatternanalysisand comes:Design,modeling,decisions.JournaloftheAmer-
machineintelligence,35(1):208–220,2012. icanStatisticalAssociation,100(469):322–331,2005.
|           |       |           |     |           |      |             | [62] Yossi Rubner,Carlo |     | Tomasi,and | Leonidas | J Guibas. |     |
| --------- | ----- | --------- | --- | --------- | ---- | ----------- | ----------------------- | --- | ---------- | -------- | --------- | --- |
| [49] Dong | Lu,Yi | Qiao,P.A. |     | Dinda,and | F.E. | Bustamante. |                         |     |            |          |           |     |
Characterizingandpredictingtcpthroughputonthewide A metric for distributions with applications to image
areanetwork. In25thIEEEInternationalConference databases. In Sixth International Conference on
|     |     |     |     |     |     |     | ComputerVision(IEEECat. |     |     | No. 98CH36271),pages |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | -------------------- | --- | --- |
onDistributedComputingSystems(ICDCS’05),pages
| 414–424,2005. |     |     |     |     |     |     | 59–66.IEEE,1998. |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
[50] HongziMao,RaviNetravali,andMohammadAlizadeh. [63] Kevin Spiteri, Rahul Urgaonkar, and Ramesh K.
Neuraladaptivevideostreamingwithpensieve. InPro- Sitaraman. Bola: Near-optimalbitrate adaptation for
|     |     |     |     |     |     |     | onlinevideos. | IEEE/ACMTransactionsonNetworking, |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------------------------------- | --- | --- | --- | --- |
ceedingsoftheConferenceoftheACMSpecialInterest
GrouponDataCommunication,pages197–210,2017. 28(4):1698–1711,2020.
|     |     |     |     |     |     |     | [64] P.C.Sruthi,SanjayRao,andBrunoRibeiro. |     |     |     | Pitfallsof |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | ---------- | --- |
[51] HongziMao,ShaileshhBojjaVenkatakrishnan,Malte
Schwarzkopf, and Mohammad Alizadeh. Variance data-drivennetworking: Acasestudyoflatentcausal
|                    |     |                   |     |          |     |              | confounders                              | in video | streaming. | In Proceedings |     | of  |
| ------------------ | --- | ----------------- | --- | -------- | --- | ------------ | ---------------------------------------- | -------- | ---------- | -------------- | --- | --- |
| reduction          |     | for reinforcement |     | learning | in  | input-driven |                                          |          |            |                |     |     |
| environments,2018. |     |                   |     |          |     |              | theWorkshoponNetworkMeetsAI&ML,NetAI’20, |          |            |                |     |     |
page42–47,NewYork,NY,USA,2020.Associationfor
[52] Yun Mao,LawrenceK. Saul,andJonathanM. Smith. ComputingMachinery.
| Ides: | An  | internet | distance | estimation |     | service for |     |     |     |     |     |     |
| ----- | --- | -------- | -------- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
[65] YiSun,XiaoqiYin,JunchenJiang,VyasSekar,Fuyuan
| large | networks. |     | IEEE Journal |     | on Selected | Areas in |                                         |     |     |     |     |       |
| ----- | --------- | --- | ------------ | --- | ----------- | -------- | --------------------------------------- | --- | --- | --- | --- | ----- |
|       |           |     |              |     |             |          | Lin,NanshuWang,TaoLiu,andBrunoSinopoli. |     |     |     |     | Cs2p: |
Communications,24(12):2273–2284,2006.
Improvingvideobitrateselectionandadaptationwith
[53] Emily Marx, Francis Y. Yan, and Keith Winstein. data-driventhroughputprediction. InProceedingsof
Implementingbola-basiconpuffer:Lessonsfortheuse the2016ACMSIGCOMMConference,SIGCOMM’16,
ofssiminabrlogic,2020. page272–285,NewYork,NY,USA,2016.Association
forComputingMachinery.
| [54] BertilMatérn. |     | Spatialvariation,volume36. |     |     |     | Springer |     |     |     |     |     |     |
| ------------------ | --- | -------------------------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
Science&BusinessMedia,2013. [66] LiyingTangandMarkCrovella. Virtuallandmarksfor
|     |     |     |     |     |     |     | theinternet. | InProceedingsofthe3rdACMSIGCOMM |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------------------------- | --- | --- | --- | --- |
[55] Cross-DisorderGroupofthePsychiatricGenomicsCon-
|     |     |     |     |     |     |     | Conference | on Internet | Measurement,IMC |     | ’03,page |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --------------- | --- | -------- | --- |
sortiumetal.Identificationofrisklociwithsharedeffects
|     |            |             |     |            |               |     | 143–152,NewYork,NY,USA,2003. |     |     | Associationfor |     |     |
| --- | ---------- | ----------- | --- | ---------- | ------------- | --- | ---------------------------- | --- | --- | -------------- | --- | --- |
| on  | five major | psychiatric |     | disorders: | a genome-wide |     |                              |     |     |                |     |     |
ComputingMachinery.
| analysis. |     | TheLancet,381(9875):1371–1379,2013. |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[67] MukarramTariq,AmgadZeitoun,VytautasValancius,
| [56] Adam | Paszke, |     | Sam Gross, | Francisco | Massa, | Adam |                               |     |     |                  |     |     |
| --------- | ------- | --- | ---------- | --------- | ------ | ---- | ----------------------------- | --- | --- | ---------------- | --- | --- |
|           |         |     |            |           |        |      | NickFeamster,andMostafaAmmar. |     |     | Answeringwhat-if |     |     |
Lerer,JamesBradbury,GregoryChanan,TrevorKilleen,
|     |     |     |     |     |     |     | deploymentandconfigurationquestionswithwise. |     |     |     |     | In  |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
Zeming Lin, Natalia Gimelshein, Luca Antiga, et al. ProceedingsoftheACMSIGCOMM2008conference
| Pytorch: |     | An imperative |     | style,high-performance |     | deep |     |     |     |     |     |     |
| -------- | --- | ------------- | --- | ---------------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
onDatacommunication,pages99–110,2008.
| learning |     | library. | Advances | in  | neural | information |                      |     |              |            |     |        |
| -------- | --- | -------- | -------- | --- | ------ | ----------- | -------------------- | --- | ------------ | ---------- | --- | ------ |
|          |     |          |          |     |        |             | [68] Eric Tzeng,Judy |     | Hoffman,Kate | Saenko,and |     | Trevor |
processingsystems,32:8026–8037,2019.
|     |     |     |     |     |     |     | Darrell. | Adversarialdiscriminativedomainadaptation. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------------------------------------ | --- | --- | --- | --- |
[57] JudeaPearl.Causality:Models,ReasoningandInference. In Proceedings of the IEEE conference on computer
CambridgeUniversityPress,USA,2ndedition,2009.
visionandpatternrecognition,pages7167–7176,2017.
[58] JonasPeters,DominikJanzing,andBernhardSchölkopf. [69] MadeleineUdellandAlexTownsend. Whyarebigdata
Elementsofcausalinference:foundationsandlearning matrices approximately low rank? SIAM Journal on
algorithms. TheMITPress,2017. MathematicsofDataScience,1(1):144–160,2019.
[59] James M Robins,Miguel AngelHernan,andBabette [70] ZhiqiangXu. Theminimalmeasurementnumberfor
Brumback. Marginal structural models and causal low-rankmatrixrecovery. AppliedandComputational
inferenceinepidemiology,2000. HarmonicAnalysis,44(2):497–508,2018.
1130    20th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

[71] Francis Y. Yan,Hudson Ayers,Chenzhi Zhu,Sadjad
Fouladi,James Hong,Keyi Zhang,Philip Levis,and
KeithWinstein. Learninginsitu:arandomizedexperi-
mentinvideostreaming.In17thUSENIXSymposiumon
NetworkedSystemsDesignandImplementation(NSDI
20),pages 495–511,Santa Clara,CA,February 2020.
USENIXAssociation.
[72] FrancisYYan,JestinMa,GregDHill,DeeptiRaghavan,
RiadSWahby,PhilipLevis,andKeithWinstein. Pan-
theon:thetraininggroundforinternetcongestion-control
research. In2018 USENIX AnnualTechnicalConfer-
{ }
ence( USENIX ATC 18),pages731–743,2018.
{ }{ }
[73] Qingqing Yang,Xi Peng,Li Chen,Libin Liu,Jingze
Zhang,HongXu,BaochunLi,andGongZhang. Deep-
queuenet: Towards scalable and generalized network
performanceestimationwithpacket-levelvisibility. In
ProceedingsoftheACMSIGCOMM2022Conference,
SIGCOMM’22,page441–457,NewYork,NY,USA,
2022.AssociationforComputingMachinery.
[74] YuzheYang,GuoZhang,DinaKatabi,andZhiXu. Me-
net:Towardseffectiveadversarialrobustnesswithmatrix
estimation. arXivpreprintarXiv:1905.11971,2019.
[75] Xiaoqi Yin,Abhishek Jindal,Vyas Sekar,and Bruno
Sinopoli. A control-theoretic approach for dynamic
adaptivevideostreamingoverhttp. SIGCOMMComput.
Commun.Rev.,45(4):325–338,August2015.
[76] DongZhang,HanwangZhang,JinhuiTang,Xiansheng
Hua,andQianruSun. Causalinterventionforweakly-
supervised semantic segmentation. arXiv preprint
arXiv:2009.12547,2020.
[77] QizhenZhang,KelvinK.W.Ng,CharlesKazer,Shen
Yan, João Sedoc, and Vincent Liu. Mimicnet: Fast
performance estimates for data center networks with
machine learning. In Proceedings of the 2021 ACM
SIGCOMM 2021 Conference, SIGCOMM ’21, page
287–304,NewYork,NY,USA,2021.Associationfor
ComputingMachinery.
[78] Zemin Zhang and Shuchin Aeron. Exact tensor
completionusingt-svd. IEEETransactionsonSignal
Processing,65(6):1511–1526,2016.
USENIX Association 20th USENIX Symposium on Networked Systems Design and Implementation 1131

AppendixA TensorCompletion Distributional invariance and RCT. As before,we shall
withpolicyinvariance assumethatthedistributionoflatentfactorsisthesameacross
different policies due to random assignment of policies to
Here, we discuss a more generic version of the problem trajectoriesinthesetupofRCT.Inthecontextofthetensor
considered in §4.2 from the lens of tensor completion. M,thiscorrespondstothedistributioninvarianceoffactors
S th p e e t c r i a fi c c e a w ll a y s ,i c n o § ns 4 id w e e re c d o t n o si b d e e o re n d e- t d h i e m s e im ns p io li n fi a e l d .H se e t r t e in ,w g e w s h h e a r l e l y p β =· ∈ p ′ Rr [P o ] v a e n r d β ℓ ∈ [ Π r], p w fo e r h a a n v y e p ∈ [P]. Concretely,forany
̸ ∈ ∈
considerhigherdimensionaltraces.This,naturallysuggests
1 1
usingthelensofTensorinsteadofMatrixcompletion.Wewill ∑ y ∑ y . (9)
a
o
l
f
s
m
od
o
i
r
s
e
c
c
u
o
s
m
sh
p
o
le
w
x
h
s
i
y
g
s
h
te
e
m
rd
d
im
yn
e
a
n
m
sio
ic
n
s
a
o
l
r
tr
m
ac
o
e
d
c
e
a
ls
n
c
e
o
n
m
ab
p
l
a
e
r
r
e
e
d
c
t
o
o
ve
th
ry
e
U pβ
∈
Πp βℓ ≈U p ′β′∈ Π
p′
β′ ℓ
simplesolutionwediscussedin§4forrank1setup. More generally, any finite moment (not just first moment
oraverage)oflatentfactorsshouldbeempiricallyinvariant
Potential Outcomes Tensor. As considered in §4 let all
acrosspolicies.Asin§4,wewouldliketoutilizeproperty(9)
possible actions be denoted as [A] = 1,...,A for some
{ } toestimatethetensorM.
A 2.LetthetracebeofDdimension.Asbefore,wehave
≥
Ntrajectoriesofinterestwithtrajectoryi [N]beingoflength A Simple Estimation Method and When It Works. We
∈
H i ≥ 1timesteps.Asbefore,letU=∑N i=1 H i . describe a simple method that can recoverentire tensoras
Consideran order-3 tensorM of dimension A U D, longasrankr D.Forsimplicity,weshallassumer=D(the
where M = [m αβγ : α ∈ [A],β ∈ [U],γ ∈ [D]] w × ith m × αβγ largestpossibl ≤ erankforwhichmethodwillwork).By(8),for
correspondstotheγthco-ordinateoftheD-dimensionaltrace agivenfixedα [A]andacrossβ [U],γ [D],
correspondingtoactiona =α [A]whenlatentfactorisu ∈ ∈ ∈
t i,t
∈
withβcorrespondingtoenumerationof(i,t)forsomei [N] r
∈ m =∑y z˜α, (10)
andt H
i
.Recallthat,asexplainedinSection4,allpossible αβγ βℓ γℓ
≤ ℓ=1
(i,t):t H,i [N]aremappedtoanintegerin[U].Wecall
i
≤ ∈
thistensorMasthePotentialOutcomesTensor. wherez˜α =x z .SinceD=r,thematrixZ˜α=[z˜α :γ [D],ℓ
Indeed,ifweknowMcompletely,thenwecananswerthe γℓ αℓ γℓ γℓ ∈ ∈
[r]]isasquarematrix.Withthisnotation,wehavethatforany
task of simulation or counterfactual estimation well since fixedα [A],thematrixMα=[m :β [U],γ [D]] RU D
wewillbeabletoestimatethemediatorforeachtrajectory (orRU ∈ rsincer=D)canberepre α s β e γ nte ∈ das ∈ ∈ ×
×
under a given possible sequence of counterfactual actions,
and subsequently estimate the counterfactual observation Mα=YZ˜α,T, (11)
(assumingwecouldlearntheF ).
systems
the
W
se
e
tr
s
a
h
c
a
e
l
s
la
w
s
h
su
er
m
e
e
ob
th
s
a
e
t
rv
th
ed
er
.
e
In
ar
p
e
ar
P
ti
≥
cu
1
la
p
r,
o
e
li
a
c
c
i
h
es
tr
u
a
n
je
d
c
e
to
r
r
w
y
h
w
ic
a
h
s
whereY=[y βℓ :β
∈
[U],ℓ
∈
[r]]
∈
RU × r.
observedunderoneofthesePpoliciesandtheassignmentof Assumption3(invertibility).WeshallassumethattheD D
×
policytothetrajectorywasdoneuniformlyatrandom.Define (i.e.r r)squarematricesZ˜αforeachα [A]arefullrankand
× ∈
Π [U]ascollectionofindicescorrespondingtotrajectories henceinvertible.
p
i [ ⊂ N]andtheirtimest H i wheretrajectoryiwasassigned The Assumption 3 implies thatY = Mα Z˜α,T − 1 forall
∈ ≤
policypforp [P].LetU = Π . α [A].
∈ p | p | ∈ (cid:0) (cid:1)
Forpolicyp [P],indicesβ Π arerelevant.Foragiven
Tensorfactorization,low CP-rank. The tensorM admits β Π ,ifthep ∈ olicy putilized ∈ act p ionα [A],m RD is
(not necessarily unique) factorization of the form: for any
ob
∈
serv
p
ed. Tothatend,letΠ = β Π
∈
:poli
α
c
β
y
·∈
utilized
α [A],β [U],γ [D] p,α { ∈ p
∈ ∈ ∈ action α . LetU p,α = Π p,α foranyα [A]. Then,define
m αβγ = ℓ ∑ = r 1 x αℓ y βℓ z γℓ , (8) Y Π p p , , α α , = γ ∈ [y } [ β D ℓ ] : ]. β T ∈ he Π n p w ,α e ,ℓ h | a ∈ ve [r Y ] | ] p ∈ ,α R = U M p,α α × ,p r, ∈ Z M ˜α α ,T ,p − = 1 . [m αβγ :β ∈
Therefore,foranyℓ [r=D],
forsomer 1.Foranytensor,suchafactorizationexitswith ∈ (cid:0) (cid:1)
≥
ratmostpoly(A,U,D). ∑ y
βℓ
=1p,α,TYp,αeℓ
Assumption 1 (low-rank factorization). We shall make an β ∈ Πp,α
assumptionthatrissmall,i.e.doesnotscalewithA,U,Dand =eTYp,α,T1p,α
ℓ
specificallyasmallconstant. =eT ℓ Z˜α − 1 Mα,p,T1p,α, (12)
Assumption2(sufficientmeasurements). Weshallassume
thatnumberofmeasurementsperinstance,D,isatleastas where1p,α RUp,α isvecto (cid:0) rof (cid:1) all1s,andeℓ Rr bevector
∈ ∈
largeastheunderlyingrankrofthetensorM,i.e.D r. withallentries0buttheℓ [r]thco-ordinate1.
≥ ∈
1132 20th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

Then,foranyℓ [r]andp [P], non-redundantlinearequations.LetmatrixV RAr
×
P
−
1be
∈ ∈ ∈
formedbystackingv1,2,...,v1,Pcolumn-wise.
1 ∑ y = 1 ∑ ∑ y Furthermore,letusdefinesp RAr as[M1,p, ,MA,p] ⊺ .
U pβ
∈
Πp βℓ U pα
∈
[A]β
∈
Πp,α βℓ DefineS
∈
RAr × Pbystackings1,
·
∈
··
,sPcolumn-wis · e ·· .
= U 1 pα ∑ [A] eT ℓ Z˜α − 1 Mα,p,T1p,α A th s e su ra m n p k ti o o f n S 4 = ( A Su r. fficient,DiversePolicies).LetP ≥ Arand
∈ (cid:0) (cid:1) NotethatwecanderiveVfromSbysubtractingthefirst
= ∑ eT ℓ Z˜α − 1 U 1 Mα,p,T1p,α columnfromallothercolumns,andremovingthefirstcolumn.
α ∈ [A] (cid:0) (cid:1) (cid:16) p (cid:17) Thus,UnderAssumption4,the+rankofVisatleastAr − 1.
= ∑ eT ℓ Z˜α − 1Mα,p, (13) Further,givenAssumption3whichexcludesthescenarioZ=0,
itfollowsthattherankofVisAr 1.AsrankofVisAr 1,we
α ∈ [A] (cid:0) (cid:1) canuniquely(uptoscaling)reco − verZbysolvingforsy − stemof
whereMα,p= 1 Mα,p,T1p,α Rr,1 isanobservedquantity, linearequationZV=0asthenullspaceofVisofdimension1.
Up ∈
whileZ˜α,T isunknown.Using(13)and(9),weobtainthatfor Once we know z,i.e. by undoing flattening,we obtain
anyℓ [r]andp=p [P], Z˜α,T − 1 foreachα [A].Sinceforeachpolicy p [P]and
∈ ∑ eT ℓ Z˜α ̸ − 1 ′ M ∈ α,p ≈ ∑ eT ℓ Z˜α − 1Mα,p′. (14) (cid:0) α rec ∈ o [ v A e (cid:1) ] r , Y Y p p , , α α a = nd M h α e , n p c (cid:0) ∈ e Z˜α su ,T b (cid:1) s − eq 1 u a e n n d tl w y e Y o ∈ b R se U r × ve r. Mα,p ∈ ,wecan
α [A] α [A] By(11),wecannowrecoversliceoftensorM,theMαfor
∈ (cid:0) (cid:1) ∈ (cid:0) (cid:1)
eachα [A],andhence we can recoverentire tensorM as
Letz˜α,ℓ=eT ℓ Z˜α − 1 ∈ R1,rbetheℓthrowtheofr × rmatrix desired. ∈
Z˜α − 1 .Then (cid:0) (14 (cid:1) )impliesthatforanyℓ [r]andp=p ′ [P], Interpretation ofAssumption 4. Considerβth Column of
∈ ̸ ∈ thematrixS,i.e., E[m ⊺ i=1,π ]P(i=1π ), ,E[m ⊺ i=
(cid:0) (cid:1) ∑ z˜α,ℓ(Mα,p Mα,p′) 0. (15) A,π ]P(i=Aπ ) ⊺ where | idenote β stheacti | on β ind ·· e · xandβ | the
− ≈ β | β (cid:2)
α [A] policyindex.Thiscolumnisavectorofstatisticsassociated
∈
(cid:3)
with traces collected using policy β. Each element in this
Whichcanbewritteninmatrixformas
vectorconsistsoftwocomponents:thefirstcomponentisthe
conditionalmeanofthetracegivenaspecificaction,andthe
M1,p M1,p′ secondelementis the probabilityoftaking this action. We
−
M2,p M2,p′ interpretlinearindependenceofeachofthesecomponentsfor
z˜1,ℓ z˜2,ℓ ... z˜A,ℓ  − . =0 (16) differentpolicyvectorsaspolicydiversity.Forinstance,think
.
.
  ofthesecondcomponentwhichcapturesprobabilityvectors
(cid:2) (cid:3)

MA,p
−
MA,p′
 ofdifferentactionsforeachpolicy.Itslinearindependence
 
across different policies roughly means that each policy
Bynotingthatthatthisholdforallℓ [r],andrecallingthat
∈ should assign new probability vectors to different actions,
z˜α,ℓistheℓ-throwtheofther rmatrix Z˜α − 1 ,weget, andnotaprobabilityvectorsimilar(linearlydependent)to
×
thatofpreviouspolicies.Alsonotethatthisassumptionisnot
M (cid:0)1,p(cid:1) M1,p′
− satisfiedifanactionisnottakenbyanyofthepolicieswhich
Z˜1 − 1 Z˜2 − 1 ... Z˜A − 1 
M2,p
− .
M2,p′
=0, makesallelementsofthecorrespondingrowequaltozero.
.
.
(cid:104) (cid:105) 
(cid:0) (cid:1) (cid:0) (cid:1) (cid:0) (cid:1) MA,p MA,p′
 − 
  (17)
where0isavectorofzerosofsizer.Notethattheaboveisa
systemofrlinearequations,withAr2unknowns(recallthatthe
r rmatrices Z˜α − 1 areunknownforα [A]).LetZ Rr × Ar
× ∈ ∈
andvp,p′ RAr denotethefirstandsecondmatrixintheleft
∈ (cid:0) (cid:1)
handside,respectively,then(17)canbere-writtenas,
Zvp,p′ 0. (18)
≈
Bydefinition,vp,p′ isobservedquantityforeachp=p
′
[P].
̸ ∈
NowifweconsiderP 1equationsproducedbyconsidering
−
pairofpolicies(1,2),(1,3),...,(1,P)in(18),bydesigntheyare
USENIX Association 20th USENIX Symposium on Networked Systems Design and Implementation 1133

| AppendixB |     | Real-worldABR |     |     |     |              |             | Prediction |     |           |
| --------- | --- | ------------- | --- | --- | --- | ------------ | ----------- | ---------- | --- | --------- |
|           |     |               |     |     |     | SourcePolicy | BOLA2 BOLA1 | Fugu-CL    |     | Fugu-2019 |
B.1 Comprehensiveresults
|     |     |     |     |     |     | BOLA2 | 22.44% 22.58% | 26.99% |     | 27.99% |
| --- | --- | --- | --- | --- | --- | ----- | ------------- | ------ | --- | ------ |
In Figure 7a, we presented a concise view of simulator BOLA1 22.43% 22.58% 26.99% 27.99%
fidelity, for an internal variable in ABR sessions called Fugu-CL 22.44% 22.58% 26.99% 27.99%
|        |           |        |               |               |     | Fugu-2019 | 22.44% 22.58% | 26.99% |     | 28.00% |
| ------ | --------- | ------ | ------------- | ------------- | --- | --------- | ------------- | ------ | --- | ------ |
| buffer | occupancy | level. | Specifically, | we considered | the |           |               |        |     |        |
simulationofatargetpolicy,giventrajectoriescollectedusing
SourcePolicy
| a different |     | source policy. | We measured | the error | between |     |             |         |     |           |
| ----------- | --- | -------------- | ----------- | --------- | ------- | --- | ----------- | ------- | --- | --------- |
|             |     |                |             |           |         |     | BOLA2 BOLA1 | Fugu-CL |     | Fugu-2019 |
buffersimulationsandgroundtruththroughEMD,asimilarity
indexfordistributions.Foracomplementaryview,weprovide Population 22.45% 22.50% 27.11% 27.94%
thefulldistributionsinFigure9,forallsimulatorsandground
(a)Left-outpolicyisBBA
truthfortargetandsourcepolicies.Beloweachplot,wealso
reporttheEMDofCausalSimpredictions.
Predictions
B.2 PolicyDiscriminatorand SourcePolicy BOLA2 Fugu-CL Fugu-2019 BBA
|     | LatentInvariance |                 |           |                |     | BOLA2     | 21.34% | 26.04% | 26.75% | 25.87% |
| --- | ---------------- | --------------- | --------- | -------------- | --- | --------- | ------ | ------ | ------ | ------ |
|     |                  |                 |           |                |     | Fugu-CL   | 21.33% | 26.05% | 26.75% | 25.87% |
| The | policy           | discriminator(W | in Figure | 3) describedin | §5  |           |        |        |        |        |
|     |                  |                 | γ         |                |     | Fugu-2019 | 21.33% | 26.04% | 26.77% | 25.86% |
has the goal of predicting the source policy,given a latent BBA 21.33% 26.04% 26.76% 25.87%
| factorgeneratedbythelatentfactorextractor(E |          |              |      |             | inFigure3). |     |               |              |     |     |
| ------------------------------------------- | -------- | ------------ | ---- | ----------- | ----------- | --- | ------------- | ------------ | --- | --- |
|                                             |          |              |      | θ           |             |     |               | SourcePolicy |     |     |
| Since                                       | our data | is collected | with | an RCT, the | true latent |     |               |              |     |     |
|                                             |          |              |      |             |             |     | BOLA2 Fugu-CL | Fugu-2019    |     | BBA |
factordistributionshouldbeindifferenttothesourcepolicy.
Therefore,ifthelatentfactorextractorgeneratestheground
|     |     |     |     |     |     | Population | 21.48% | 25.94% | 26.74% | 25.84% |
| --- | --- | --- | --- | --- | --- | ---------- | ------ | ------ | ------ | ------ |
truthlatentfactors,thepolicydiscriminatorshouldnotbeable
(b)Left-outpolicyisBOLA1
topredictthesourcepolicyaccurately.Infact,eventheoptimal
| policy | discriminator | outputs | the population | share | of each |     |     |     |     |     |
| ------ | ------------- | ------- | -------------- | ----- | ------- | --- | --- | --- | --- | --- |
sourcepolicy(e.g.whatfractionofthedatacomesfromBBA) Predictions
inthetrainingdata[28].Toassessthisstatement,wepresent
theconfusionmatrixandpopulationshareofsourcedata,for SourcePolicy BOLA1 Fugu-CL Fugu-2019 BBA
three left-outpolicies in Table 1. Eachrowcorresponds to BOLA1 21.46% 26.00% 26.76% 25.78%
onesourcepolicy,andeachcolumncorrespondstothepolicy Fugu-CL 21.45% 26.01% 26.77% 25.76%
|     |     |     |     |     |     | Fugu-2019 | 21.45% | 26.00% | 26.79% | 25.76% |
| --- | --- | --- | --- | --- | --- | --------- | ------ | ------ | ------ | ------ |
discriminator’spredictionofthesourcepolicy.Weobserve
|     |     |     |     |     |     | BBA | 21.45% | 25.99% | 26.76% | 25.80% |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ------ | ------ |
thatpredictionsdonotchangenoticeablywithdifferentsource
policies,andthattheycloselymatchthepopulationsharefor
SourcePolicy
eachleft-outpolicy.Thisdemonstratesthattheextractedlatent
|     |     |     |     |     |     |     | BOLA1 Fugu-CL | Fugu-2019 |     | BBA |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | --- |
featureswereindeedinvarianttothesourcepolicy.
|     |                      |     |     |     |     | Population | 21.52%                   | 25.93% | 26.72% | 25.83% |
| --- | -------------------- | --- | --- | --- | --- | ---------- | ------------------------ | ------ | ------ | ------ |
| B.3 | Whatmakesasimulation |     |     |     |     |            | (c)Left-outpolicyisBOLA2 |        |        |        |
scenarioeasy/hard?
|     |     |     |     |     |     | Table 1: Confusion | matrixandpopulation |     | statistics | forthe |
| --- | --- | --- | --- | --- | --- | ------------------ | ------------------- | --- | ---------- | ------ |
policydiscriminatorwiththreeleftoutpolicies.
In§6.3,wecomparedtheaccuracyofCausalSim,ExpertSim
| and | SLSim, | in a simulation | task | on real ABR | data. We |     |     |     |     |     |
| --- | ------ | --------------- | ---- | ----------- | -------- | --- | --- | --- | --- | --- |
observedthatinabout30%ofscenarios,whichwecalleasy
scenarios,allsimulatorsperformwell.However,inabout70% issimilartothecounterfactualachievedthroughput(ofthe
ofthesource/targetscenarios,whichwecallhardsimulation targetpolicy).ThisiswhatbothExpertSim(explicitly)and
scenarios,baselinepredictionsarehighlybiasedtowardsthe SLSim(implicitly)assumefordoingsimulation.Makingthis
source distributions. In these hardscenarios,CausalSim is assumptionisthecorereasontheirsimulationsarebiasedin
|     |     |     |     |     |     | hard cases,where | source and | target policies | take | different |
| --- | --- | --- | --- | --- | --- | ---------------- | ---------- | --------------- | ---- | --------- |
abletode-biasthetrajectoriesanditspredictionsmatchthe
targetdistributionwell,asobservableinFigure9. actions,aswediscussedindetailin§2.2.3.
Soitisnaturaltowonderwhatmakesasimulationscenario Figure 10 validates our reasoning for what makes a
easy/hard?Aneasysimulationscenariohappenswhensource simulation scenario difficult. The X axis shows the Mean
andtargetpoliciestakesimilaractions.Similaractionmeans AbsoluteDifference(MAD)betweensourceandsimulation
that the factual achieved throughput (of the source policy) actions(bitrates)whensimulatingwithSLSiminaspecific
1134    20th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

CausalSimpredictions CausalSimpredictions CausalSimpredictions
ExpertSimpredictions ExpertSimpredictions ExpertSimpredictions
| 90        |                  |       | 90        |                  | 90        |                  |
| --------- | ---------------- | ----- | --------- | ---------------- | --------- | ---------------- |
|           | SLSimpredictions |       |           | SLSimpredictions |           | SLSimpredictions |
|           | BBA(left-out)    |       |           | BOLA1(left-out)  |           | BOLA2(left-out)  |
| )%(FDC 70 |                  |       | )%(FDC 70 |                  | )%(FDC 70 |                  |
|           | BOLA1(source)    |       |           | BOLA2(source)    |           | BOLA1(source)    |
| 50        |                  |       | 50        |                  | 50        |                  |
| 30        |                  |       | 30        |                  | 30        |                  |
| 10        |                  |       | 10        |                  | 10        |                  |
| 0         | 5                | 10 15 | 0         | 5 10 15          | 0         | 5 10 15          |
BufferOccupancy(seconds) BufferOccupancy(seconds) BufferOccupancy(seconds)
(a)CausalSimEMD=0.19 (b)CausalSimEMD=0.10 (c)CausalSimEMD=0.13
CausalSimpredictions CausalSimpredictions CausalSimpredictions
ExpertSimpredictions ExpertSimpredictions ExpertSimpredictions
| 90     | SLSimpredictions |       | 90     | SLSimpredictions | 90     | SLSimpredictions |
| ------ | ---------------- | ----- | ------ | ---------------- | ------ | ---------------- |
| 70     | BBA(left-out)    |       | 70     | BOLA1(left-out)  | 70     | BOLA2(left-out)  |
| )%(FDC |                  |       | )%(FDC |                  | )%(FDC |                  |
|        | BOLA2(source)    |       |        | BBA(source)      |        | BBA(source)      |
| 50     |                  |       | 50     |                  | 50     |                  |
| 30     |                  |       | 30     |                  | 30     |                  |
| 10     |                  |       | 10     |                  | 10     |                  |
| 0      | 5                | 10 15 | 0      | 5 10 15          | 0      | 5 10 15          |
BufferOccupancy(seconds) BufferOccupancy(seconds) BufferOccupancy(seconds)
(d)CausalSimEMD=0.16 (e)CausalSimEMD=0.31 (f)CausalSimEMD=0.22
CausalSimpredictions CausalSimpredictions CausalSimpredictions
ExpertSimpredictions ExpertSimpredictions ExpertSimpredictions
| 90  |                  |     | 90  |                  | 90  |                  |
| --- | ---------------- | --- | --- | ---------------- | --- | ---------------- |
|     | SLSimpredictions |     |     | SLSimpredictions |     | SLSimpredictions |
)%(FDC 70 BBA(left-out) )%(FDC 70 BOLA1(left-out) )%(FDC 70 BOLA2(left-out)
|     | Fugu-2019(source) |       |     | Fugu-2019(source) |     | Fugu-2019(source) |
| --- | ----------------- | ----- | --- | ----------------- | --- | ----------------- |
| 50  |                   |       | 50  |                   | 50  |                   |
| 30  |                   |       | 30  |                   | 30  |                   |
| 10  |                   |       | 10  |                   | 10  |                   |
| 0   | 5                 | 10 15 | 0   | 5 10 15           | 0   | 5 10 15           |
BufferOccupancy(seconds) BufferOccupancy(seconds) BufferOccupancy(seconds)
(g)CausalSimEMD=0.14 (h)CausalSimEMD=0.25 (i)CausalSimEMD=0.22
CausalSimpredictions CausalSimpredictions CausalSimpredictions
ExpertSimpredictions ExpertSimpredictions ExpertSimpredictions
| 90  |                  |     | 90  |                  | 90  |                  |
| --- | ---------------- | --- | --- | ---------------- | --- | ---------------- |
|     | SLSimpredictions |     |     | SLSimpredictions |     | SLSimpredictions |
)%(FDC 70 BBA(left-out) )%(FDC 70 BOLA1(left-out) )%(FDC 70 BOLA2(left-out)
|     | Fugu-CL(source) |       |     | Fugu-CL(source) |     | Fugu-CL(source) |
| --- | --------------- | ----- | --- | --------------- | --- | --------------- |
| 50  |                 |       | 50  |                 | 50  |                 |
| 30  |                 |       | 30  |                 | 30  |                 |
| 10  |                 |       | 10  |                 | 10  |                 |
| 0   | 5               | 10 15 | 0   | 5 10 15         | 0   | 5 10 15         |
BufferOccupancy(seconds) BufferOccupancy(seconds) BufferOccupancy(seconds)
(j)CausalSimEMD=0.09 (k)CausalSimEMD=0.21 (l)CausalSimEMD=0.17
Figure9:Bufferleveldistributionofsource,target,CausalSimpredictions,andbaselinepredictionsacrossallsource/targetscenarios.
USENIX Association 20th USENIX Symposium on Networked Systems Design and Implementation    1135

0.9 ExpertSimPredictions
SLSimPredictions
0.7
0.5
0.3
0.1
0.50 0.75 1.00
DME
RCT.MinRTTisaninherentpropertyofanetworkpath17,
andwewouldexpectMinRTTdistributiontobethesamefor
usersassignedtodifferentABRpolicies.
We use the MinRTT to create the following four
sub-populations:
1. Sub1:userswithMinRTT<35ms
2. Sub2:userswith35ms MinRTT<70ms
≤
3. Sub3:userswith70ms MinRTT<100ms
≤
4. Sub4:userswith100ms MinRTT
BitrateMAD(Mbps) ≤
Now,wecanaskquestionofthefollowingtype:hadtheusers
Figure 10: Simulation difficultyis relatedto howdifferent
insub-populationtwo,whowereassignedthesourceABRalgo-
counterfactualactionsarefromfactualones.Thisfigureshows
rithm,insteadusedtheleft-outABRalgorithm,whatwouldthe
scatterplotofEMDversusmeanabsolutebitratedifference,
distributionoftheirbufferlevellooklike?Asthegroundtruth
forExpertSimandSLSim,overallpossiblesourceleft-out
answertothisquestion,wecanusethebufferleveldistribution
pairs.Thepinkclustersignifiesthe‘easy’scenariosandthe
ofusersinsub-populationtwoassignedtotheleft-outpolicy.
greenclustersignifies‘hard’ones.
Figure11ashowstheCDFofCausalSim’sEMDwhensim-
ulatingtheleft-outABRalgorithmovereachoftheabovesub-
populations.WecanseethatCausalSimmaintainsasuperior
source/targetscenario.YaxisshowsEMD(Ourperformance
EMDCDFcomparedtoExpertSimandSLSim,andremainsac-
metricforsimulation,smallerisbetter)ofbothbaselinesin
curateacrossdifferentsub-populations.Thisfurthersuggests
thatspecificscenario.
thatevenatsurgicallysmallsubpopulations,CausalSimmain-
Twomainclusterofpointsareclearlyvisibleinthisfigure.
tainsaccuracy,anddoesnotoverfittothewholedistribution.
The pink cluster on the bottom left corresponds to easy
simulations.Itincludesallsource/targetsimulationscenarios
wherebaselinesperformwell(bottom),andatthesametime, B.5 HowtoTuneCausalSim’s
sourceandtargetactionsarequitesimilar(left). Hyper-parameters?
Thegreenclusteratthetoprightcorrespondstothehard
Counterfactualpredictionisnotastandardsupervisedlearning
simulations.Itincludesallsource/targetsimulationscenarios
taskthatoptimizesin-distributiongeneralization.Rather,it
wherebaselinesfailtoperformanunbiasedsimulation(top),
is always an OOD generalization problem,i.e.,we collect
and at the same time, source and target actions are quite
data from a training policy (distribution 1), and want to
different(right).
accuratelysimulatedataunderadifferentpolicy(distribution
2). Sincewedonotusedatafrom thetestpolicywhen we
B.4 AMoreFine-grained trainCausalSim,weusethefollowingnaturalproxyfortuning
hyper-parameters:SimulatingABRalgorithmsinthetraining
Evaluation
datausingtrajectoriesofotherABRalgorithmsinthetraining
Ideally,wewouldliketoevaluateCausalSim’ssimulationto data.ThisofcoursecanbeviewedasanOODproblemas
groundtruthonastep-by-stepbasisforagiventrajectory.But well.Weclaimthatifachoiceofhyper-parametersresultsin
asdiscussedin§6.3,thisisnotpossibleinreal-worlddata,aswe arobustmodelthatperformswellOODacrossallvalidation
onlyseetheoutcomeofoneABRalgorithm’schosenactionfor ABRalgorithmsinthetrainingdata,itshouldworkwellfor
asinglestep.Inotherwords,thereisnowaytogetgroundtruth theactualleft-outtestpolicyaswell.
forindividualstepsintheobservationaldata,whichisreferred Weverifythishyper-parametertuningprocedureempiri-
toasthefundamentalproblemofCausalInference[32].This cally.Foreachchoiceofthethreeleft-outABRalgorithms
isthereasonweevaluatedpredictionsonadistributionallevel. (hencetrainingdataset),wetrainelevendifferentCausalSim
However,thereisawaytoevaluateCausalSim’spredictions modelswithdifferentchoicesofκ(definedinEquation(7)).
atamorefine-grainedlevel.Insteadofevaluatingthepredicted Weconsidertwometrics:(i)TestEMD,definedastheaverage
distributionofbufferoccupancyacrossthewholepopulation, EMDwhensimulatingtheleft-outABRalgorithmwithtrajec-
wecanevaluateoncertainsub-populationsofusers.Theonly toriesinthetrainingdataset.Thisisourmainperformanceob-
requirementisthatthewayweselectthesesub-populations jective.(ii)ValidationEMD,definedastheaverageEMDwhen
shouldbestatisticallyindependentoftheABRalgorithm.For
17Thisistruetoafirstorderapproximation,ifweignorethepossibilitythat
example,wecanpartitionusersbyametricsuchasMinRTT,
avideostreamingsessiondrivesupqueueingdelaysthroughoutthecourse
whichisindependentofthepolicychosenforeachuserinthe ofavideo,therebyinflatingtheobservedMinRTT.
1136 20th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

|     |     | CausalSim     |     | ExpertSim |        | SLSim   |     | B.6                                                  | HowtoTuneSLSim’s  |          |             |     |             |               |     |
| --- | --- | ------------- | --- | --------- | ------ | ------- | --- | ---------------------------------------------------- | ----------------- | -------- | ----------- | --- | ----------- | ------------- | --- |
|     |     | minrtt [0,35) |     |           | minrtt | [35,70) |     |                                                      | Hyper-parameters? |          |             |     |             |               |     |
|     |     | ∈             |     |           |        | ∈       |     |                                                      |                   |          |             |     |             |               |     |
|     | 80  |               |     |           |        |         |     | SLSimtakesasinputthecurrentbuffervalue,selectedchunk |                   |          |             |     |             |               |     |
|     |     |               |     |           |        |         |     | size                                                 | and               | observed | throughput, |     | and similar | to CausalSim, |     |
50
|        |     |     |     |     |     |     |     | predicts  |     | the next                                  | buffer        | bˆ and   | download | time | dˆ. We   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----------------------------------------- | ------------- | -------- | -------- | ---- | -------- |
|        |     |     |     |     |     |     |     |           |     |                                           |               | t+1      |          |      | t        |
|        | 20  |     |     |     |     |     |     | addtwo    |     | knobs                                     | to tune while | training | SLSim:   | (1)  | The loss |
|        |     |     |     |     |     |     |     | functionL |     | (,)usedtosteertheNNoutputtothegroundtruth |               |          |          |      |          |
| )%(FDC |     |     |     |     |     |     |     |           |     | ξ ··                                      |               |          |          |      |          |
[70,100) [100,∞) output,and(2)Therelativeweightingofthelossfunctionfor
|     |     | minrtt |     |     | minrtt |     |     |                                                    |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | ------ | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | ∈      |     |     |        | ∈   |     | downloadtimewithrespecttothatofthebufferoccupancy, |     |     |     |     |     |     |     |
|     | 80  |        |     |     |        |     |     | η.Concretely,weusethefollowingtotalloss:           |     |     |     |     |     |     |     |
50
|     |     |     |     |     |     |     |     |     | =E    |          | 1 (bˆ |            | η   | (dˆ,d) |          |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ----- | ---------- | --- | ------ | -------- |
|     | 20  |     |     |     |     |     |     | L   |       |          | .L    | t+1 ,b t+1 | )+  | .L     | (19)     |
|     |     |     |     |     |     |     |     |     | slsim | B η+1    | ξ     |            | η+1 | ξ t t  |          |
|     |     |     |     |     |     |     |     |     |       | (cid:20) |       |            |     |        | (cid:21) |
|     | 0.1 | 0.5 | 0.9 |     | 0.1 | 0.5 | 0.9 |     |       |          |       |            |     |        |          |
wheretheexpectationisovertheasampledminibatchB
EMD
|     |     |     |     |     |     |     |     | fromdatasetD,andb                                  |         |         | t+1 andd       | t denotethegroundtruthvalues |         |                |          |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | ------- | ------- | -------------- | ---------------------------- | ------- | -------------- | -------- |
|     |     |     |     | (a) |     |     |     | fornextbufferlevelandchunkdownloadtime.Table3lists |         |         |                |                              |         |                |          |
|     | 3   |     |     |     |     |     |     | thelossfunctionsandηvaluesconsidered.              |         |         |                |                              |         |                |          |
|     |     |     |     |     |     |     |     |                                                    | To tune | these   | values,we      | use                          | ground  | truth data     | from all |
|     |     |     |     |     |     |     |     | policies                                           |         | excepta | leftoutpolicy. |                              | We then | proceedwiththe |          |
DMEtseT
2
proxytuningobjectiveusedin§B.5,i.e.welookforthecon-
figurationwiththehighestaccuracyatsimulatingalgorithms
1
inthetrainingdatausingtrajectoriesofotheralgorithmsin
thetrainingdata.Wethenusetheresultingconfiguration(and
|     | 0   |       |     |     |     |       |     | model)tosimulatetheleft-outpolicyonthetrainingdata. |      |                 |     |            |      |             |      |
| --- | --- | ----- | --- | --- | --- | ----- | --- | --------------------------------------------------- | ---- | --------------- | --- | ---------- | ---- | ----------- | ---- |
|     |     |       |     |     |     |       |     |                                                     | From | the perspective |     | of tuning, | this | methodology | puts |
|     |     | 0 0.5 |     | 1   | 1.5 | 2 2.5 |     |                                                     |      |                 |     |            |      |             |      |
SLSimonequalgroundwithrespecttoCausalSim,andmakes
ValidationEMD
forafaircomparison.Notethatwedonottunelossfunction
|     |     |     |     | (b) |     |     |     | type | or  | η with | CausalSim | due | to limited | computational |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ------ | --------- | --- | ---------- | ------------- | --- |
resources,buttuningthoseaswellcouldpotentiallyimprove
Figure11:(a)ComparingthedistributionofCausalSimEMDs
CausalSim’saccuracy.
| withExpertSim |     | andSLSim |     | overdifferentsub-populations. |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | -------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(b)ValidationEMDandtestEMDarehighlycorrelated.This
B.7 SimulationAccuracy:Continued
justifiesourhyper-parametertuningstrategy.
In§6.1.1,westatedthatExpertSimandSLSimpredictionsare
significantlyaffectedbythesourcedatatheyaresimulating
on,anddemonstratedtheeffectofsourcepoliciesonBOLA1
|     |     |     |     |     |     |     |     | predictions |     | in  | Figure 4b. | Here,we | demonstrate | the       | same |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ---------- | ------- | ----------- | --------- | ---- |
|     |     |     |     |     |     |     |     | figure      | for | BBA | in Figure  | 12a and | BOLA2       | in Figure | 12b. |
CausalSimisdesignedtoremovethebiasofthealgorithm
simulatingABRalgorithmsinthetrainingdatasetwithtrajecto-
riesinthetrainingdatathatwerecollectedwithotherABRalgo- usedforcollectingsourcedatawhensimulatingatargetpolicy
|     |     |     |     |     |     |     |     | andits | predictions |     | remains | unaffectedby |     | the performance |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | ------- | ------------ | --- | --------------- | --- |
rithms.Thisisourproxyobjectiveforhyper-parametertuning.
ofthatsourcepolicy.ExpertSimandSLSimhowever,dueto
theviolationoftheexogenoustraceassumption,willpredict
Foreachmodel(33in all: 3datasets,11examplehyper- differentmetricswhenusingdifferentsourcetraces.
| parameters), |     | we calculate |     | both | Test EMD | and | Validation |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | --- | ---- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
EMD,whichresultsinone(ValidationEMD,TestEMD)point
B.8 Dataset&Algorithms
| in  | Figure | 11b. The | Pearson | Correlation |     | Coefficient | (PCC) |     |     |     |     |     |     |     |     |
| --- | ------ | -------- | ------- | ----------- | --- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
betweenValidEMDandTestEMDis0.92,whichshowshigh Ourtrajectoriesinthereal-world(Puffer)datacomefrom‘slow
linearcorrelation.Hence,thoughCausalSimmightnotalways streams‘inthetimespanofJuly27,2020untilJune2,2021.In
performwell(i.e.,TestEMDisnotlowforsomecombinations thisperiodoftime,5ABRalgorithmsappearconsistentlyand
oftrainingdatasetandhyper-parameters),wecanhaveavery arelistedinTable2.Eachtrajectoryisanactiveclientsession
goodideaofhowwellitworksbymeasuringValidationEMD. streamingaliveTVchannel.WefollowPuffer’sdefinitionof
USENIX Association 20th USENIX Symposium on Networked Systems Design and Implementation    1137

|     | Policies | Hyperparameter |     | Value             |     | Usedassource | Usedasleftout |     |
| --- | -------- | -------------- | --- | ----------------- | --- | ------------ | ------------- | --- |
|     |          | Cushion        |     | 3(asusedinpuffer) |     | ✓            | ✓             |     |
BBA
|     |     | Reservoir |     | 10.5(asusedinpuffer)      |     |     |     |     |
| --- | --- | --------- | --- | ------------------------- | --- | --- | --- | --- |
|     |     | V         |     | 0.67(Ascomputedinpuffer)  |     |     |     |     |
|     |     | γ         |     | -0.43(Ascomputedinpuffer) |     |     |     |     |
|     |     |           |     |                           |     | ✓   | ✓   |     |
BOLA-BASICv1
|     |     | Utilityfunction |     | log (1 ssim)(Asusedinpuffer) |     |     |     |     |
| --- | --- | --------------- | --- | ---------------------------- | --- | --- | --- | --- |
10
−
|     |     | Minimumutility |     | 0dB(Asusedinpuffer)       |     |     |     |     |
| --- | --- | -------------- | --- | ------------------------- | --- | --- | --- | --- |
|     |     | Maximumutility |     | 60dB(Asusedinpuffer)      |     |     |     |     |
|     |     | V              |     | 51.4(Ascomputedinpuffer)  |     |     |     |     |
|     |     | γ              |     | -0.43(Ascomputedinpuffer) |     |     |     |     |
|     |     |                |     |                           |     | ✓   | ✓   |     |
BOLA-BASICv2
|     |         | Utilityfunction |     | ssim(Asusedinpuffer) |     |     |     |     |
| --- | ------- | --------------- | --- | -------------------- | --- | --- | --- | --- |
|     |         | Minimumutility  |     | 0(Asusedinpuffer)    |     |     |     |     |
|     |         | Maximumutility  |     | 1(Asusedinpuffer)    |     |     |     |     |
|     | Fugu-CL | -               |     | -                    |     | ✓   |     |     |
×
|     | Fugu-2019 | -   |     | -   |     | ✓   |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- |
×
Table2:ABRalgorithmsusedinthereal-worlddatasetandexperiments
‘slowstreams’;streamswithTCPdeliveryratesbelow6Mbps. report that obeys a set of rules is used. We,however,
Weuse‘slowstreams‘data,sincethehighestqualitychunks have to compute stall time and watch time using our
rarelysurpass6 7Mbps,andpathswithhigherbandwidth mergedlogs(mergedlogsarealsowhatwegetoutof
−
willalwaysstreamthehighestqualitychunksunderallpolicies. simulation). This would be easy on the original data,
Pufferusesthesamereasoningandevaluatesalgorithmsat if‘client‘logsand‘video_sent’wereinsync,butthey
twopopulationlevels;’slowstreams’and’allstreams’. arenot;wheneverarebufferingisreportedbytheclient,
Inaggregating‘slowstream‘logs,wemetseveraldifficul- ‘client’ log is updated but ‘video_sent’ is updated in
tiesthatweoutlinehereforreproducibility.Datawithoutthese thenextfewchunks.Tocircumventthis,werecompute
difficultieswouldpotentiallyimproveCausalSim’saccuracy. rebufferingast =max(0,t b),wheret isrebuffering,
|     |     |     |     |     |     | r   | d r |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
−
Note thatthis does notaffectFigure 5,as the data forthat b is buffer occupancy and t d is download time. This
figureisreporteddirectlyonPuffer[2,3]. formulaisoffbyhalfofanRTT,andempiricallyinflates
|             |              |          |          |               | stallratesby1.26 | 1.31x,forallpolicies.Intheabsence |     |     |
| ----------- | ------------ | -------- | -------- | ------------- | ---------------- | --------------------------------- | --- | --- |
| Puffer logs | are reported | as three | separate | event groups; |                  |                                   |     |     |
−
1) ‘video_sent’: the first packet of a chunk is sent, 2) of synchronized data,this is the best we can recover,
‘video_acked’:Thelastpacketofachunkisacknowledged,3) but it does not affect the comparison among policies.
‘client’:Theclientsentamessage.Stallrateiscomputedusing Hence,webelievesimulatingwiththisdatashouldlead
the‘client’logsandqualityiscomputedusingthe‘video_sent’ tosimilartrendsaswithcleanunperturbeddata.
logs.
1. To compute download time, we have to merge 3. We cannot calculate watch time as Pufferdoes,since
‘video_sent’and‘video_acked’,andensurethatmerged wehavetousethemergedlog.Wetriedseveralsimple
|      |                 |                |      |             | formulas | that should calculate | watch time,but | oddly |
| ---- | --------------- | -------------- | ---- | ----------- | -------- | --------------------- | -------------- | ----- |
| logs | are consecutive | in timestamps, | i.e. | no chunk is |          |                       |                |       |
missinginbetweentwootherchunks.However,inthe mostturnouttobeinaccurate.Onereasonisthatinsome
streams,bufferplaybackrateisnot1,i.e.onesecondof
currentdatathisremovesallchunksthathavebeensent
butnotacknowledged,usuallythelastchunk.Pufferuses bufferisnotdepletedpersecond.Thesestreamsarelikely
these chunks in measuring quality level,butwe can’t. duetobrowsertabsputinbackground,andthrottledby
thebrowserthreadingsystem.Asaworkaround,weuse
Thisdidnothaveanymeasurableimpact,however.
theoriginalwatchtimeminustheoriginalstalltimethat
2. Tocomputestallrate,bothtotalstalltimeandtotalwatch Puffercomputedforastream,andoffsetitbythetotal
timearecomputedwith‘client’logs.Forthis,thelatest stalltimeinthesimulation.
1138    20th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

GroundTruth CausalSim ExpertSim SLSim ourimplementationisfaithfulandlogsmatchruntimeinputs.
ForthelogsinJuly27th,2020,weobserve100%matching
15.6
forBOLA1andBOLA2and99.993%forBBA.Forthelatter,
)Bd(MISSegarevA therearerarecaseswheretwoencodingsareseeminglyequal
15.4
inSSIMuptothe6loggeddecimalplaces,butwerelikely
slightlydifferentindoubleprecisionformatatruntime.These
instancesarerareenoughthatwecanignorethem.
15.2
|     |     |     |     |     |     | For Fugu-2019 |       | or Fugu-CL | however,our |               | reproductions |         |
| --- | --- | --- | --- | --- | --- | ------------- | ----- | ---------- | ----------- | ------------- | ------------- | ------- |
|     |     |     |     |     |     | did not       | match | in 6% and  | 19% of      | cases,whether |               | we used |
15.0
theoriginalCimplementationorourownPythonport.The
Pufferteaminformedusofause-after-freeissueregarding
|     | 2.0 | 1.5 | 1.0 |     | 0.5 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theTransmissionControlProtocol(TCP)infostructthatwas
TimeSpentStalled(%)
fixedinMarch7th,2022.Henceweretriedthisprocessfor
|     |     | (a) |     |     |     | thelogspertainingtoJuly27th,2022andtheerrorrateshrank |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
to0.53%and0.64%.Unfortunately,a0.5%errorrateisstill
|     | GroundTruth | CausalSim | ExpertSim |     | SLSim |                 |     |                                    |             |     |       |          |
| --- | ----------- | --------- | --------- | --- | ----- | --------------- | --- | ---------------------------------- | ----------- | --- | ----- | -------- |
|     |             |           |           |     |       | too highandeven |     | ifwe ignore                        | that,limits |     | us to | RCT logs |
|     |             |           |           |     |       | afterMarch7th.  |     | Therefore,wedonotconsiderFugu-2019 |             |     |       |          |
15.6
| )Bd(MISSegarevA |     |     |     |     |     | orFugu-CLascandidatesforleft-outalgorithms. |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
B.9 Trainingsetup
15.4
WeuseMultiLayerPerceptrons(MLPs)astheNNstructures
forCausalSimmodelsandtheSLSimmodel.Allimplementa-
| 15.2 |     |     |     |     |     | tionsusethePytorch[56]library.Table3isacomprehensive |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
listofallhyperparametersusedintraining.
|     | 10  | 8 6 |     | 4   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TimeSpentStalled(%)
|     |     |     |     |     |     | AppendixC |     | SyntheticABR |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | ------------ | --- | --- | --- | --- |
(b)
|     |     |     |     |     |     | As explained |     | in §6.3.1, | we also | evaluate | CausalSim | in  |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | ------- | -------- | --------- | --- |
Figure12:Predictionsfor(a)BBAand(b)BOLA2,separated
|     |     |     |     |     |     | a synthetic | ABR | environment, | in  | which | we  | can obtain |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | --- | ----- | --- | ---------- |
bytheABRalgorithmsourcedatawascollectedwith.Each
|     |     |     |     |     |     | ground | truthforindividualcounterfactual |     |     |     | predictions | on a |
| --- | --- | --- | --- | --- | --- | ------ | -------------------------------- | --- | --- | --- | ----------- | ---- |
pointindicatesaspecificsourceABRalgorithm.
step-by-stepbasisforatrajectory.Intheseexperiments,we
alsousealargersetofpoliciesthanavailableintherealdata.
4. Ateachstep,thebuffershouldnotincreasebymorethan
| a single | chunk,2.002 | seconds,butitdoes |     | (sometimes |     |     |     |     |     |     |     |     |
| -------- | ----------- | ----------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
C.1 SimulationDynamics
byasmuchas14seconds).Wefiltersuchdataout.
|     |     |     |     |     |     | In each | simulated | training | session,we | start | with | an empty |
| --- | --- | --- | --- | --- | --- | ------- | --------- | -------- | ---------- | ----- | ---- | -------- |
5. When we are aboutto senda chunk,ourlastreported playbackbufferanda latentnetworkpathcharacterizedby
buffervaluemustneverdipbelow2.002(exceptinthe anRTTandacapacitytrace.Ineachstep,anABRalgorithm
beginning).Whenbufferisbelow15seconds,thenext choosesachunksize,whichistransportedoverthisnetwork
chunk must be sent immediately after the last one. If path to the client as the bufferis depleting. Once the user
rebufferingoccurs,thenextbuffervaluewillbeexactly
|     |     |     |     |     |     | receives | the chunk,the | bufferlevelincreases |     |     | by  | the chunk |
| --- | --- | --- | --- | --- | --- | -------- | ------------- | -------------------- | --- | --- | --- | --------- |
2.002andifitdoesn’t,itwillbelargerthan2.002.We duration.Thissimplesystemcanbemodeledasfollows:
| frequently                                     | (more | than one million | instances) |     | observe |     |     |          |     |       |     |      |
| ---------------------------------------------- | ----- | ---------------- | ---------- | --- | ------- | --- | --- | -------- | --- | ----- | --- | ---- |
|                                                |       |                  |            |     |         |     |     | b =min(b | d   | ,0)+c |     | (20) |
| buffervaluesbelow2.002.Wedonotfilterthemout,as |       |                  |            |     |         |     |     | t+1      | t t |       |     |      |
−
thiswouldinvalidatemostlogs.
|     |     |     |     |     |     | whereb,d | t t andcrefertothebufferlevelattimestept,the |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | -------------------------------------------- | --- | --- | --- | --- | --- |
TotestoutCausalSim,weneedtosimulatethestreaming downloadtimeofthechunkattimestept,andthechunkvideo
session using a different algorithm than the one that was length in seconds,respectively. Streaming the next chunk
actuallyusedinthatsession. Thisrequiresimplementation isstartedimmediatelyfollowingreceivingthepreviousone,
of the ABR algorithms. To ensure our implementations except when the buffer level surpasses a certain value (in
are correct,we attempt to reconstruct the choices made at ourcase,10 seconds to mimic a live-stream ABR setting).
runtime by each policy, and compare them to the logged To compute d,we model the transport as a TCP session
t
choices. Weexpectourreproduction tomatch100%when withanAdditiveIncrease-MultiplicativeDecrease(AIMD)
USENIX Association 20th USENIX Symposium on Networked Systems Design and Implementation    1139

|     |                                      |     | Model |     |     | Hyperparameter                |     | Value                     |     |     |
| --- | ------------------------------------ | --- | ----- | --- | --- | ----------------------------- | --- | ------------------------- | --- | --- |
|     |                                      |     |       |     |     | Hiddenlayers                  |     | (128,128)                 |     |     |
|     |                                      |     |       |     |     | HiddenlayerActivationfunction |     | RectifiedLinearUnit(ReLU) |     |     |
|     |                                      |     |       |     |     | OutputlayerActivationfunction |     | Identitymapping           |     |     |
|     |                                      |     |       |     |     | Optimizer                     |     | Adam[40]                  |     |     |
|     | SLSim(1network),CausalSim(3networks) |     |       |     |     | Learningrate                  |     | 0.001                     |     |     |
|     |                                      |     |       |     |     | β1                            |     | 0.9                       |     |     |
|     |                                      |     |       |     |     | β2                            |     | 0.999                     |     |     |
|     |                                      |     |       |     |     | ε                             |     | 10− 8                     |     |     |
|     |                                      |     |       |     |     | Batchsize                     |     | 217                       |     |     |
{0.05,0.1,0.5,1,5,
κ
10,15,20,25,30,40}
|     |     |     |     |     |     | Trainingiterations(num_train_it) |     | 5000 |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- | ---- | --- | --- |
CausalSim
|     |     |     |       |     |     | num_disc_it                    |     | 10                    |     |     |
| --- | --- | --- | ----- | --- | --- | ------------------------------ | --- | --------------------- | --- | --- |
|     |     |     |       |     |     | Lossfunction                   |     | Huber(δ=0.2)          |     |     |
|     |     |     |       |     |     | η(downloadtimeweightwrtbuffer) |     | 1                     |     |     |
|     |     |     |       |     |     | Trainingiterations             |     | 10000                 |     |     |
|     |     |     | SLSim |     |     | Lossfunction                   |     | {Huber(δ=0.2),L1,MSE} |     |     |
|     |     |     |       |     |     | η(downloadtimeweightwrtbuffer) |     | {0.5,1,10}            |     |     |
Table3:Trainingsetupandhyperparametersforthereal-worldABRexperiment
congestion control mechanism with slow start. For every • A video, with several bit-rates available. We use
chunk,theTCPconnectionstartsfromtheminimumwindow "Envivio-Dash3" from the DASH-246 JavaScript
size of 2 packets and increases the window according to referenceclient[22].
| slow  | start. Therefore, |     | it takes      | the transport | some              | time to |     |     |     |     |
| ----- | ----------------- | --- | ------------- | ------------- | ----------------- | ------- | --- | --- | --- | --- |
| begin | fully utilizing   |     | the available |               | network capacity. | The     |     |     |     |     |
overhead incurred by slow start depends on the RTT and • AnABRalgorithm.Wehaveasetof9policiestochoose
bandwidth-delay product of the path. When downloading from,presentedinTable4.
chunkswithlargesizes,theprobingoverheadisminimalbutit
canbesignificantforsmallchunks.Therefore,asweobserved
inthePufferdata,thethroughputachievedforagivenchunk • A network path,which is characterized by the latent
networkcapacityandthepathRTT.
inthissyntheticsimulationdependsonthesizeofthechunk.
PerformanceMetric:WecompareCausalSimpredictions
|                                               |     |     |     |     |     |          | We use random | generative processes | to generate | 5000 |
| --------------------------------------------- | --- | --- | --- | --- | --- | -------- | ------------- | -------------------- | ----------- | ---- |
| withgroundtruthcounterfactualtrajectories,via |     |     |     |     |     | the Mean |               |                      |             |      |
SquaredError(MSE)distancebetweenthetwotimeseries: networktracesandRTTs.TheRTTforastreamingsession
issampledrandomly,accordingtoauniformdistribution:
2
|     |     | MSE(p,q)= |     | p   | q ||2 | (21) |     |     |     |     |
| --- | --- | --------- | --- | --- | ----- | ---- | --- | --- | --- | --- |
|| −
rtt Unif(10ms,500ms)
| Here,p= | p   | N andq= |     | q N     | aretimeseriesvectors. |     |     | ∼   |     |     |
| ------- | --- | ------- | --- | ------- | --------------------- | --- | --- | --- | --- | --- |
|         | t   | }t =1   |     | t }t =1 |                       |     |     |     |     |     |
|         | {   |         |     | {       |                       |     |     |     |     |     |
BetterpredictionsyieldsmallerMSEvalues,whereanideal
MSEis0. OurtracegeneratorisaboundedGaussiandistribution,whose
meancomesfromaMarkovchain.PriorworkshowsMarkov
chainsareappropriatemodelsforTCPthroughput[65],and
C.1.1 Data&Algorithms
Gaussiandistributionscanmodelthroughputsinstationary
segmentsofTCPflows[49].
| Simulating | a trajectory |     | in oursynthetic |     | ABR environment |     |     |     |     |     |
| ---------- | ------------ | --- | --------------- | --- | --------------- | --- | --- | --- | --- | --- |
needsthreecomponents: Concretely,atthestartofthetrace,thefollowingparameters
1140    20th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

|     | Policies |     | Hyperparameter | Value |     |     | Usedassource | Usedasleftout |     |
| --- | -------- | --- | -------------- | ----- | --- | --- | ------------ | ------------- | --- |
|     |          |     | Cushion        | 5     |     |     |              | ✓             | ✓   |
BBA
|                    |            |     | Reservoir       | 10                                    |     |     |     |     |     |
| ------------------ | ---------- | --- | --------------- | ------------------------------------- | --- | --- | --- | --- | --- |
|                    |            |     | V               | 0.71(Computedusingpufferformula)      |     |     |     |     |     |
|                    | BOLA-BASIC |     |                 |                                       |     |     |     | ✓   | ✓   |
|                    |            |     | γ               | 0.22(Computedusingpufferformula)      |     |     |     |     |     |
|                    |            |     | Utilityfunction | ln(chunksizes)(AsusedinBOLApaper[63]) |     |     |     |     |     |
|                    |            |     |                 |                                       |     |     |     | ✓   | ✓   |
|                    | Random     |     | -               | -                                     |     |     |     |     |     |
|                    |            |     | Cushion         | 5                                     |     |     |     |     |     |
| BBA-Randommixture1 |            |     |                 |                                       |     |     |     | ✓   | ✓   |
|                    |            |     | Reservoir       | 10                                    |     |     |     |     |     |
|                    |            |     | Randomchoices   | 50%                                   |     |     |     |     |     |
|                    |            |     | Cushion         | 10                                    |     |     |     |     |     |
|                    |            |     |                 |                                       |     |     |     | ✓   | ✓   |
BBA-Randommixture2
|     |     |     | Reservoir       | 20  |     |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
|     |     |     | Randomchoices   | 50% |     |     |     |     |     |
|     |     |     | Lookbacklength  | 5   |     |     |     |     |     |
|     |     |     | Lookaheadlength | 5   |     |     |     | ✓   | ✓   |
MPC
|     |            |     | Rebufferpenalty    | 4.3          |     |     |     |     |     |
| --- | ---------- | --- | ------------------ | ------------ | --- | --- | --- | --- | --- |
|     |            |     | Throughputestimate | Harmonicmean |     |     |     |     |     |
|     |            |     | Lookbacklength     | 5            |     |     |     |     |     |
|     | Rate-based |     |                    |              |     |     |     | ✓   | ✓   |
|     |            |     | Throughputestimate | Harmonicmean |     |     |     |     |     |
|     |            |     | Lookbacklength     | 5            |     |     |     |     |     |
|     |            |     |                    |              |     |     |     | ✓   | ✓   |
OptimisticRate-based
|     |     |     | Throughputestimate | Max |     |     |     |     |     |
| --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
|     |     |     | Lookbacklength     | 5   |     |     |     | ✓   | ✓   |
PessimisticRate-based
|     |     |     | Throughputestimate | Min |     |     |     |     |     |
| --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
Table4:ABRalgorithmsusedinthesyntheticABRexperiments.
arerandomlysampled: Finally,thenetworkcapacityc ineachstepissampledfrom
t
aGaussiandistribution,definedbytheseparameters:
v Unif(30,100)
∼
|     |     | p = | 1/v           |     |     | c   | Normal(s,s | c )     |     |
| --- | --- | --- | ------------- | --- | --- | --- | ---------- | ------- | --- |
|     |     |     |               |     |     | t ∼ |            | t t · σ |     |
|     |     | l,h | Unif(0.5,4.5) |     |     |     |            |         |     |
∼
h l
C.1.2 Trainingsetup
|     |     | s.t. | − > 0.3 |     |     |     |     |     |     |
| --- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- |
h+l
Similartothereal-worldABRexperiment,weuseMLPsas
|     |     | s 0 | Unif(l,h)      |                                                      |     |     |     |     |     |
| --- | --- | --- | -------------- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
|     |     | ∼   |                | theNNstructuresforCausalSimmodelsandtheSLSimmodel.   |     |     |     |     |     |
|     |     | c   | Unif(0.05,0.3) |                                                      |     |     |     |     |     |
|     |     | σ ∼ |                | Wetuneallthehyperparametersofbothbaselinesasisdonein |     |     |     |     |     |
thereal-worldABRexperiment(see§B.5and§B.6).Table5
Ateachtimestep,thestateremainsunchangedwithprobability
1 pandchangesotherwise.Whenchanging,thenextstate comprehensivelylistsallhyperparametersusedintraining.
−
issampledfromadoubleexponentialdistributioncentered
aroundthepreviousstate:
C.2 CanCausalSimFaithfullySimulate
|     | λ = solve       | R+(1 | ex(h st 1) ex(st | 1− l)=0)                                              |              |     |     |     |     |
| --- | --------------- | ---- | ---------------- | ----------------------------------------------------- | ------------ | --- | --- | --- | --- |
|     |                 | x    | − −              | −                                                     | NewPolicies? |     |     |     |     |
|     |                 | ∈    | − −              |                                                       |              |     |     |     |     |
|     | s = DoubleExp(s |      | ,λ)              |                                                       |              |     |     |     |     |
|     | t               |      | t 1              |                                                       |              |     |     |     |     |
|     |                 |      | −                | Similartoourreal-dataevaluations,wetrainmodelsbasedon |              |     |     |     |     |
Thepointforthisspecifictransitionkernelisthatsmallchanges trainingdatageneratedusingallpoliciesexceptaleft-outpol-
innetworkcapacityshouldbemorelikelythandrasticchanges. icy,forwhichthemodeldoesnotobserveanydata.Although
USENIX Association 20th USENIX Symposium on Networked Systems Design and Implementation    1141

|                      | Model | Hyperparameter                                     |     | Value             |     |     |
| -------------------- | ----- | -------------------------------------------------- | --- | ----------------- | --- | --- |
|                      |       | Hiddenlayers(SLSim)                                |     | (128,128)         |     |     |
|                      |       | Hiddenlayers(CausalSim:Extractor,DiscriminatorandF |     | system) (128,128) |     |     |
|                      |       | Hiddenlayers(CausalSim:Actionencoder)              |     | (64,64)           |     |     |
|                      |       | Rankr                                              |     | 2                 |     |     |
| CausalSim(4networks) |       | HiddenlayerActivationfunction                      |     | ReLU              |     |     |
|                      |       | OutputlayerActivationfunction                      |     | Identitymapping   |     |     |
|                      |       | Optimizer                                          |     | Adam[40]          |     |     |
| SLSim(1network)      |       | Learningrate                                       |     | 0.0001            |     |     |
|                      |       | β1                                                 |     | 0.9               |     |     |
|                      |       | β2                                                 |     | 0.999             |     |     |
8
|     |     | ε   |     | 10− |     |     |
| --- | --- | --- | --- | --- | --- | --- |
213
Batchsize
|     |     | κ                                |     | {0.01,0.1,1,10,100} |     |     |
| --- | --- | -------------------------------- | --- | ------------------- | --- | --- |
|     |     | Trainingiterations(num_train_it) |     | 20000               |     |     |
CausalSim
|     |       | num_disc_it        |     | 10                    |     |     |
| --- | ----- | ------------------ | --- | --------------------- | --- | --- |
|     |       | Lossfunction       |     | {MSE}                 |     |     |
|     | SLSim | Trainingiterations |     | 20000                 |     |     |
|     |       | Lossfunction       |     | {Huber(δ=1.0),L1,MSE} |     |     |
Table5:TrainingsetupandhyperparametersforthesyntheticABRexperiments.
tracescomefromthesamegenerativeprocess,notwotrajec- forallthreemethodsaswemovefrowardintime.However,
toriesinthedatasetcollectedwithdifferentpoliciessharethe CausalSimmaintainsaMAPEof( 5.1%)whichsignificantly
∼
exactsametrace,asthiswouldbeanunrealisticdatacollection lowerthanbothExpertSim’sandSLSim’s( 10%).
∼
scenario.Giventhatwehave9possiblepoliciestoleaveout,
wehave9possibledatasetsandmodels.Thereare8possible C.3 LearningABRpolicieswithCausalSim
groupsoftrajectoriestochooseassources,basedonthepolicy
thatgeneratedthem.Intotalthisleaves72differentcombina- We observedhowCausalSim can be usedto design an im-
tionsandscenarios.Weusethesamehyper-parametertuning provedpolicyin§6.2,andverifiedthisthroughdeploymentin
approachexaminedin§B.5.Figure13acomparestheCDFof thewild.Wewouldliketotaketheseexperimentsonestepfur-
MSEvaluesresultingfromCausalSimandthetwobaselines. therandaskcanCausalSimbeusedtodesignlearning-based
Asevident,bothbaselinessufferfrominaccuratepredictions policies,suchaswithReinforcementLearning(RL)?
and in some cases are catastrophically inaccurate. On the Recent work has shown that RL algorithms can learn
contrary,CausalSimmaintainsfavorableperformance,evenin strongABRpoliciesbylearningthroughinteractionswiththe
thetailofitsMSEdistribution.Figure13bgivesacloserlook environment[50].CouldweuseaCausalSimmodeltotrain
attheCDFcurves.WeseeCausalSimdominatesateveryscale. high-performanceABRpolicieswithoutdirectenvironment
Figure13cisaheatmapofthetwodimensionalhistogram interaction?Asafirststep,wedecidedtocarryoutaninitial
ofCausalSimpredictionsandgroundtruths.Afullyaccurate experimentin the syntheticABR environment. We builda
prediction scheme wouldperfectly matchthe groundtruth CausalSimmodelusingtracesfroma“simulatedRCT”on
andonlythediagonalofthishistogramwouldbepopulated. thesyntheticenvironment.
CausalSim almost achieves that, indicating it produces PerformanceMetric.ABRalgorithmsaretypicallyevaluated
accuratetrajectoriesonastep-by-stepbasis. throughQoEmetrics[75].Assumingthechosenbitrateatstep
Further,inFigure14,wecomparethetheMeanAbsolute
|     |     |     | twasq,thedownloadtimewasd t |     | t andthebufferwasb,we | t   |
| --- | --- | --- | --------------------------- | --- | --------------------- | --- |
Percentage Error (MAPE) of CausalSim, ExpertSim and usethefollowingQoEdefinition:
| SLSim predictions | across all | trajectories at each time | step |     |     |     |
| ----------------- | ---------- | ------------------------- | ---- | --- | --- | --- |
forthefirst35steps.Notethattheerrornaturallyaccumulates QoE t =q t q t q t 1 µ max(0,d t b t 1 )
|     |     |     |     | −| − − | |− · | − − |
| --- | --- | --- | --- | ------ | ---- | --- |
1142    20th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

3
10
| 90  |     | 90  |     | snoitciderPs’miSlasuaC |     |
| --- | --- | --- | --- | ---------------------- | --- |
)%(noitalupoP
| )%(FDC 70 |     | )%(FDC 70 |     |     | 2   |
| --------- | --- | --------- | --- | --- | --- |
8
| 50   |                      | 50    |                      |       |     |
| ---- | -------------------- | ----- | -------------------- | ----- | --- |
| 30   |                      | 30    |                      |       |     |
|      | CausalSimpredictions |       | CausalSimpredictions | 6     | 1   |
| 10   | ExpertSimpredictions | 10    | ExpertSimpredictions |       |     |
|      | SLSimpredictions     |       | SLSimpredictions     |       |     |
|      |                      |       |                      | 4     | 0   |
| 0 10 | 20 30                | 0 0.5 | 1 1.5 2              |       |     |
|      |                      |       |                      | 4 6 8 | 10  |
|      | MSE                  |       | MSE                  |       |     |
GroundTruth
| (a) |     | (b) |     |     |     |
| --- | --- | --- | --- | --- | --- |
(c)
Figure13:(a)DistributionofCausalSim,ExpertSim,andSLSimMSEsoverallpossiblesourceleft-outpairs.(b)Thesamefigure
withasmallerMSErange.Inthismagnifiedview,CausalSimclearlyoutperformsthebaselines.(c)Two-dimensionalhistogram
heatmapofCausalSimpredictionsvs.groundtruth.
|     |     |     | C.3.2 | DoesCausalSimtrainbetterpolicies? |     |
| --- | --- | --- | ----- | --------------------------------- | --- |
10
)%(EPAM
Figure15aplotstheCDFofaveragesessionQoEthateach
| 5   |     |     | policy | attains. Here, Real Environment | refers to training |
| --- | --- | --- | ------ | ------------------------------- | ------------------ |
CausalSimpredictions directlywiththesyntheticABRenvironment,andCausalSim,
ExpertSimpredictions
ExpertSimandSLSimrefertopoliciestrainedbyusingeach
| 0   |     | SLSimpredictions |     |     |     |
| --- | --- | ---------------- | --- | --- | --- |
ofthesesimulators.CausalSimtrainspoliciesnearlyaswell
0 5 10 15 20 25 30 as training directly on the environment,while ExpertSim
Chunkindex andSLSimfailtoproviderobustpoliciesacrossallsessions.
Figure15bplotstheCDFsforthehighRTT(above300ms)
Figure14:AtimeseriesplotoftheMeanAbsolutePercentage
clients,wherethegapbetweenCausalSimandthebaseline
Error(MAPE)acrossalltrajectories,forCausalSim,Expert- simulatorsisevenlarger.
SimandSLSimpredictions.Noticehowerrorsaccumulate
intrajectorysimulation. Inthisenvironment,chunkaredownloadedaccordingto
theslowstartmodel,wherecongestioncontrolmustrampup
itswindowsizeoverseveralRTTsbeforethedownloadrate
ThisQoEmetriccapturesthreegoals(insuccession): 1) canreachtheavailablebandwidth.Asaresult,downloadsof
Streaminhighquality,2)Maintainastablequality,3)Avoid smallerchunks(withlowerbitrates)incuranoticeableover-
rebuffering.BetterpoliciesyieldhigherQoEvalues,where
head,particularlyonhigh-RTTpaths.Thisoverheadbecomes
anidealQoEisequaltothemaxbitrate. lessapparentaschosenbitratesbecomelarger.Biasedsim-
ulatorssuchasSLSimandExpertSim,whichassumeallac-
tionsleadtothesameobservedbandwidth,overestimatethe
C.3.1 Howtotrainpoliciesviasimulators?
achievedratewhencounterfactualbitratesaresmallerthan
To train the RL agent,we take a set of logged trajectories factualones(chosenbythesourcepolicy)andunderestimate
wherethesourcepolicywasMPCandfeedthemtoCausalSim. itwhenthecounterfactualbitratesarelarger.Sincethesource
Ineachstep,CausalSimwillpredictthenextcounterfactual policyisconservativeandtendstochooselowbitrates,Expert-
observation and reward,and the RL agent will choose the SimandSLSimfindlargerbitratestobeundesirableinthe
next counterfactual action based on that observation. This QoEtrade-off.ThiscanbeseeninFigure15c,whichvisualizes
processrepeatsuntilthissimulatedsessionisover,afterwhich the3aspectsofQoEintermsoftherebufferingrateandthe
the counterfactual trajectory is used to train the RL agent. smoothedbirate,i.ethechosenbitrateswiththesmoothnes
FortheRLalgorithm,weutilizetheAdvantageActorCritic penalty.Noticehowpoliciestrainedontherealenvironment
(A2C)method,aprominenton-policyalgorithm,alongwith andCausalSimutilizethenetworkby200kbpsmorethanother
GeneralizedAdvantageEstimation(GAE).Table6listsall policies.TheextrarebufferingthatCausalSimincursisneg-
hyperparametersfortheRLtraining. ligiblecomparedtotheextrabitrate:5.9secondseveryhour.
USENIX Association 20th USENIX Symposium on Networked Systems Design and Implementation    1143

0.9
Real CausalSim
)spbM(etartiBhtoomS
| 90     |     |     |     |     | 90     |     |     |     |     |     |          |
| ------ | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | -------- |
| 70     |     |     |     |     | 70     |     |     |     | 0.8 |     | QoE=0.75 |
| )%(FDC |     |     |     |     | )%(FDC |     |     |     |     |     |          |
| 50     |     |     |     |     | 50     |     |     |     |     |     |          |
RealEnvironment
| 30  |     |     | CausalSim |     | 30  |     |     |     |     | MPC | QoE=0.65 |
| --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | -------- |
0.7 SLSim
ExpertSim
SLSim
| 10  |     |     |     |     | 10  |     |     |     |           |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
|     |     |     | MPC |     |     |     |     |     | ExpertSim |     |     |
0.6
|     | 0.5 |     | 1.5 |     |     | 0.5 |     | 1.5 |      |      |      |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | ---- |
|     | 0   | 1   |     | 2   | 0   |     | 1   |     | 0.1% | 0.2% | 0.3% |
|     |     | QoE |     |     |     | QoE |     |     |      |      |      |
RebufferingRate
|     | (a)Fullpopulation |     |     |     | (b)HighRTTclients |     |     |     |     |     |     |
| --- | ----------------- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
(c)QoEbreakdowninHighRTTclients
Figure15:CausalSimtrainedpoliciesperformwell,onlymarginallybehindtrainingontherealenvironment.DistributionofQualityof
Experience(QoE)inpoliciestrainedwiththerealenvironment,CausalSim,ExpertSim,andtheMPCpolicy.CausalSimdoesnotunderestimate
bandwidthinhighRTTclientsandtrainspoliciesthatstrikethebestbalanceinQoEgoals.
|     |     |     | Group | Hyperparameter                |     |     |     | Value   |     |     |     |
| --- | --- | --- | ----- | ----------------------------- | --- | --- | --- | ------- | --- | --- | --- |
|     |     |     |       | Hiddenlayers                  |     |     |     | (32,32) |     |     |     |
|     |     |     |       | Hiddenlayeractivationfunction |     |     |     | ReLU    |     |     |     |
A2Cactor:Softmax
Outputlayeractivationfunction
A2Ccritic:Identitymapping
|     |     |     |     | Optimizer |     |     |     | Adam[40] |     |     |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | -------- | --- | --- | --- |
NeuralNetwork
|     |     |     |     | Learningrate |     |     |     | 0.001 |     |     |     |
| --- | --- | --- | --- | ------------ | --- | --- | --- | ----- | --- | --- | --- |
|     |     |     |     | β1           |     |     |     | 0.9   |     |     |     |
|     |     |     |     | β2           |     |     |     | 0.999 |     |     |     |
|     |     |     |     | ε            |     |     |     | 10− 8 |     |     |     |
4
|     |     |     |     | Weightdecay             |     |     |     | 10−                  |     |     |     |
| --- | --- | --- | --- | ----------------------- | --- | --- | --- | -------------------- | --- | --- | --- |
|     |     |     |     | Episodelengths          |     |     |     | 490                  |     |     |     |
|     |     |     |     | Epochstoconvergence(Tc) |     |     |     | 8000(3920000samples) |     |     |     |
|     |     |     |     | Randomseeds             |     |     |     | 4                    |     |     |     |
A2Ctraining
|     |     |     |     | γ               |     |     |     | 0.96               |     |     |     |
| --- | --- | --- | --- | --------------- | --- | --- | --- | ------------------ | --- | --- | --- |
|     |     |     |     | Entropyschedule |     |     |     | 0.1to0in5000epochs |     |     |     |
|     |     |     |     | λ(forGAE)       |     |     |     | 0.95               |     |     |     |
|     |     |     |     | Chunklengthc    |     |     |     | 4                  |     |     |     |
Environment
|     |     |     |     | Numberofactions(bitrates) |     |     |     | 6   |     |     |     |
| --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- |
Table6:TrainingsetupandhyperparametersforlearningRLpoliciesinthesyntheticABRenvironment.
C.4 Low-rankstructure latent factoris the network bottleneck capacity c18. F
t trace
describeshowtheachievedthroughput(thetrace)relatesto
thislatentfactor.Intuitively,thisshouldbeaclose-to-linear
As discussed in §4.1,we can formulate the counterfactual function,m c. But it’s not exactly linear; forexample,
|            |         |     |             |           |             |     |     | t t |     |     |     |
| ---------- | ------- | --- | ----------- | --------- | ----------- | --- | --- | --- | --- | --- | --- |
| estimation | problem | in  | the context | of matrix | completion. |     |     | ≈   |     |     |     |
congestioncontrolmayunder-utilizethenetworkcapacityfor
Foreachtimestep,weknowthechosenbitrate(action)and
| the achievedthroughput(trace). |     |     |     | We also knowthe | trace | is  |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --------------- | ----- | --- | --- | --- | --- | --- | --- |
18Theremaybeotherlatentfactorsbutbottleneckcapacityislikelytohave
computedusingalatentfactorandtheaction. Supposethe thestrongestinfluenceontheachievedthroughput.
1144    20th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

|     | edutingaMeulaVralugniS |     |     |     |     |     | erutaefdetcartxes’miSlasuaC |     |     |     |     |     |     |
| --- | ---------------------- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
5,000
|     |     |     |     |     |     |     |     | 20  |     |     |     | tnuocnoitalupoP |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |
400
4,000
3,000
200
10
2,000
0
1,000
|     |     | 1   | 2   | 3   | 4 5 | 6   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
0
SingularValueIndex
|     |     |     |     |     |     |     |     |     | 0 500 | 1,000 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- |
Latentjobsize
| Figure | 16: | Singular | values | of matrix | M in synthetic | ABR |     |     |     |     |     |     |     |
| ------ | --- | -------- | ------ | --------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure17:Two-dimensionalhistogramheatmapofCausalSim
suggestthatMisapproximatelyrank2.
extractedlatentstatevs.latentjobsizes.
ducingaccuratecounterfactualpredictions,asthearchitecture
smalltransfersonhigh-RTTpaths.
ofCausalSimsuggests.Todoso,wecompareCausalSim’ses-
| WeformamatrixM,wheretherowsdenoteactionsa |     |     |     |     |     | t [A] |                                                        |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | ----- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
|                                           |     |     |     |     |     | ∈     | timatedlatentstatewiththeunderlyingjobsizes—thejobsize |     |     |     |     |     |     |
andthecolumnsdenotethelatentfactorsuiforeachtrajectory.
|     |     |     |     |     | t   |     | isindeedthelatentstatethatdictatesthedynamicsintheload |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
The‘factual’datawehavearesingleobservedtracevaluesin
balancingenvironment.Wefindthattheestimatedlatentstates
eachcolumn,i.eforeachstepandeachlatent,wehaveobserved
andthejobsizesarehighlycorrelated,asillustratedinFig-
thetracefromasingleaction.Toestimatecounterfactuals,we
ure17,withaPCCof0.994.ThisdemonstratesthatCausalSim
mustcompletethematrix.Wehavenowayofknowingthetrue
canlearnfaithfulrepresentationsoftruelatentstates.
F inthePufferdataset.Buttogetasenseforwhatitmight
trace
looklikeandwhetherit’splausiblethatMislowrank,wecan
D.2 Data&Algorithms
investigatethisinthesyntheticABRenvironmentinstead.
FortheTCPslowstartmodelthisenvironmentuses,F
|     |     |     |     |     |     | trace | Tosimulatetheloadbalancingproblemdescribedin§6.4.1, |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
takesthefollowingform:
|     |     |     |     |     |     |     | weneedtosettheserverprocessingrates |     |     |     |     | r N ,andarriving |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | ---------------- | --- |
i }i=1
{
|     |     |     |     |     |     |     | jobsizesS | k .Serverratesaregeneratedrandomly,asfollows: |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------------------------------------------- | --- | --- | --- | --- | --- |
RTT
|     | Let | RTˆT:= |     |     |     | (22) |     |     | r   | = eui |     |     | (24) |
| --- | --- | ------ | --- | --- | --- | ---- | --- | --- | --- | ----- | --- | --- | ---- |
i
ln(2)
|     |     |        |     |     |             |     |     | where | u   | Unif( | ln(5),ln(5)) |     | (25) |
| --- | --- | ------ | --- | --- | ----------- | --- | --- | ----- | --- | ----- | ------------ | --- | ---- |
|     |     |        | c   |     |             |     |     |       | i   |       |              |     |      |
|     |     |        | t   |     | ifs RTˆT.(c | c˙) |     |       |     | ∼     | −            |     |      |
|     |     | 1+RTˆT |     |     | t           | t   |     |       |     |       |              |     |      |
(ln(ct/c˙) ct+c˙) ≥ − We generate job sizes using a time-varying Gaussian
|     | =  |     | · st − |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
m (23) distribution.Atstepkofthetrajectory,jobsizeS issampled
|     | t  |      | s      |     |           |     |            |     |     |          |      | k   |     |
| --- | ------ | ---- | ------ | --- | --------- | --- | ---------- | --- | --- | -------- | ---- | --- | --- |
|     |        |      | t      |     | otherwise |     |            |     |     |          |      |     |     |
|     |        | RTˆT | st     |     |           |     | asfollows: |     |     |          |      |     |     |
|     |        | ln(  | +1)    |     |           |     |            |     |     |          |      |     |     |
|     |        | ·    | RTˆTc˙ |     |           |     |            |     | S   | Normal(µ | ,σ ) |     |     |
|     |        |      | ·      |     |           |     |            |     | k   | ∼        | k k  |     |     |
s
where isthechun ksize(whichitselfisdeterminedby whereµ andσ signifythemeanandvarianceofthegenerative
|     |         | t      |        |         |              |          | k   |     | k   |     |     |     |     |
| --- | ------- | ------ | ------ | ------- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- |
| the | bitrate | chosen | byABR) | andc˙is | the starting | download |     |     |     |     |     |     |     |
distributionattimestepk.Ateachtimestep,withaprobability
rateintheslowstartalgorithm(inourcase,equalto2MTUs). ofp=1/12000,themeanandvariancechangeandwithaprob-
We use this model to generate a version of M with A = 6 abilityof1 p,theyremainthesame.Themeanandvariance
| actionsandU=49000latentnetworkconditions.Wecompute |     |     |     |     |     |     |     | −   |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
valuesaredrawnfromrandomdistributions,bothatthestartof
thesingularvaluedecompositionwiththe6singularvalues atrajectoryandwhenachangeoccurs,inthefollowingmanner:
| representedinnon-increasingorder(σ |     |     |     |     | σ       | σ ).The |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
|                                    |     |     |     |     | 1 2     | 6       |     |     |     |     |     |     |     |
|                                    |     |     |     |     | ≥ ≥···≥ |         |     |     |     |     |     |     |     |
total“energy”ofmatrixisgivenbysumofsquaresofthese
Ifk=0(startoftrace)or,meanandvariancemustchange:
σ2+σ2
| singularvalues.Itturnsoutthat                        |     |     |     |             | 1 2 ismorethan0.999. |     |     |             |     |        |          |     |      |
| ---------------------------------------------------- | --- | --- | --- | ----------- | -------------------- | --- | --- | ----------- | --- | ------ | -------- | --- | ---- |
|                                                      |     |     |     | totalenergy |                      |     | µ   | Pareto(α=1, |     | L=101, | H=102.5) |     | (26) |
| Thissuggeststhatmostofthematrixiscapturedbyitsrank-2 |     |     |     |             |                      |     | k   |             |     |        |          |     |      |
∼
|                                                   |     |     |     |     |     |     | σ   | Unif(0, | 0.5µ | )   |     |     | (27) |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | --- | --- | --- | ---- |
| approximation,asdepictedinFigure16.Inotherwords,M |     |     |     |     |     |     | k   |         |      | k   |     |     |      |
∼
| isapproximatelylow(=2)rank. |     |     |     |     |     |     | Else: |     |     |     |     |     |      |
| --------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | ---- |
|                             |     |     |     |     |     |     | µ =µ  |     |     |     |     |     | (28) |
|                             |     |     |     |     |     |     | k     | k 1 |     |     |     |     |      |
−
| AppendixD |     |     | LoadBalancing |     |     |     | σ =σ |     |     |     |     |     | (29) |
| --------- | --- | --- | ------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | ---- |
|           |     |     |               |     |     |     | k    | k 1 |     |     |     |     |      |
−
|     |      |           |     |            |       |        | Jobs        | generated | according | to  | this process | are temporally  |     |
| --- | ---- | --------- | --- | ---------- | ----- | ------ | ----------- | --------- | --------- | --- | ------------ | --------------- | --- |
| D.1 | Does | CausalSim |     | Faithfully | Infer | Latent |             |           |           |     |              |                 |     |
|     |      |           |     |            |       |        | correlated, | and       | therefore | not | independent  | and identically |     |
States?
|     |     |     |     |     |     |     | distributed. | Training | data | consists | of 5000 | trajectories | of  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | ---- | -------- | ------- | ------------ | --- |
Wetesttheclaimthatestimatingtheexogenouslatentstate length1000,eachofwhichwasrandomlyassignedapolicy
andusingittopredictthenextstatewasindeedthekeytopro- fromasetof16policies,describedinTable7.
USENIX Association 20th USENIX Symposium on Networked Systems Design and Implementation    1145

|     | Policies |     | Description |     | Usedassource | Usedasleftout |
| --- | -------- | --- | ----------- | --- | ------------ | ------------- |
✓
| Serverlimitedpolicy(8variations) |     |     | Randomlyassigntoonlytwoservers |     |     |     |
| -------------------------------- | --- | --- | ------------------------------ | --- | --- | --- |
×
|     |               |     |                                 |     | ✓   | ✓   |
| --- | ------------- | --- | ------------------------------- | --- | --- | --- |
|     | Shortestqueue |     | Assigntoserverwithsmallestqueue |     |     |     |
Powerofk(k 2,3,4,5 ) Pollqueuelengthsofkserverandassigntoshortestqueue ✓ ✓
|     | ∈{  | }   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Normalizequeuesizeswithserverrates
|     | Oracleoptimal |     |     |     | ✓   | ✓   |
| --- | ------------- | --- | --- | --- | --- | --- |
andassigntoshortestnormalizedqueue
|     |     |     | Similartooracle,butestimatesserverrates |     | ✓   | ✓   |
| --- | --- | --- | --------------------------------------- | --- | --- | --- |
Trackeroptimal
withhistoricalobservationsofprocessingtimes
Table7:Schedulingpoliciesusedintheloadbalancingexperiment.
D.3 Trainingsetup
Asbefore,weuseMLPsastheNNstructuresforCausalSim
modelsandtheSLSimmodelandTable8isacomprehensive
| list of all | hyperparameters | used | in training. | We tune the |     |     |
| ----------- | --------------- | ---- | ------------ | ----------- | --- | --- |
parameterκforCausalSimandthelossfunctioninSLSimina
similarfashiontowhatisdescribedin§B.5and§B.6.Notethat,
asmentionedin§6.4.1,weassumeaccesstoF
|     |     |     |     | system andfocus |     |     |
| --- | --- | --- | --- | --------------- | --- | --- |
onthemorechallengingtaskofestimatingthetracequantities,
forbothCausalSimandSLSim.Therefore,intraining,there
| arenoobservationsandhenceL |     | total | consistoftwoterms:the |     |     |     |
| -------------------------- | --- | ----- | --------------------- | --- | --- | --- |
squaredlossofthetracequantitiesandthediscriminatorloss.
| AppendixE | CausalInferenceRelatedWork |     |     |     |     |     |
| --------- | -------------------------- | --- | --- | --- | --- | --- |
Identifyingcausalrelationshipsfromobservationaldataisa
criticalprobleminmanydomains[30],includingmedicine
[55],epidemiology[59],economics[36],andeducation[23].
| Indeed, | identifying causal | structure | and | answering causal |     |     |
| ------- | ------------------ | --------- | --- | ---------------- | --- | --- |
inferencequeriesisanemergingthemeindifferentmachine
| learning | tasks recently,including |     | computervision | [74,76], |     |     |
| -------- | ------------------------ | --- | -------------- | -------- | --- | --- |
reinforcementlearning[6,24],fairness[27],andtime-series
| analysis | [7] to name a | few. One | important | aspect about |     |     |
| -------- | ------------- | -------- | --------- | ------------ | --- | --- |
causalinferenceisitsabilitytoanswercounterfactualqueries.
| For such | queries, many | methods | were developed; | where |     |     |
| -------- | ------------- | ------- | --------------- | ----- | --- | --- |
someapproachesaremotivatedbyPearl’sstructuralcausal
model[57],andbyRubin’spotentialoutcomeframework[61].
Werefertheinterestedreadertorecentsurveyssuchas[30]and
referencesthereinforanoverviewofrecentadvancesinour
abilitytoinfercausalrelationshipsfromobservationaldata.
Anotherrelatedlineofworkwithinthisliteratureissyn-
theticcontrolsanditsextensionsyntheticinterventions,which
aimstobuildsynthetictrajectoriesofdifferentunits(e.g.indi-
viduals,geographiclocations)underunseeninterventionsby
appropriatelylearningacrossobservedtrajectories[4,5,9–12].
However,theseapproachesassumeastaticsetofintervention
anddonotapplytooursetting.
1146    20th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

| Model                | Hyperparameter                                  | Value               |
| -------------------- | ----------------------------------------------- | ------------------- |
|                      | Hiddenlayers(SLSim)                             | (128,128)           |
|                      | Hiddenlayers(CausalSim:Extractor,Discriminator) | (128,128)           |
|                      | Hiddenlayers(CausalSim:Actionencoder)           | Nohiddenlayers      |
|                      | Rankr                                           | 1                   |
| CausalSim(3networks) | HiddenlayerActivationfunction                   | ReLU                |
|                      | OutputlayerActivationfunction                   | Identitymapping     |
|                      | Optimizer                                       | Adam[40]            |
| SLSim(1network)      | Learningrate                                    | 0.0001              |
|                      | β1                                              | 0.9                 |
|                      | β2                                              | 0.999               |
|                      | ε                                               | 10− 8               |
|                      | Batchsize                                       | 213                 |
|                      | κ                                               | {0.01,0.1,1,10,100} |
CausalSim
|       | Trainingiterations(num_train_it) | 10000        |
| ----- | -------------------------------- | ------------ |
|       | num_disc_it                      | 10           |
| SLSim | Trainingiterations               | 10000        |
|       | Lossfunction                     | Huber,L1,MSE |
Table8:Trainingsetupandhyperparametersfortheloadbalancingexperiment.
USENIX Association 20th USENIX Symposium on Networked Systems Design and Implementation    1147