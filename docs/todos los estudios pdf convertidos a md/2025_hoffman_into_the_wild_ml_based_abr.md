| Into | the | Wild:           |             | Real-World |     |     |     | Testing | for                 | ML-Based        |     |     | ABR |     |
| ---- | --- | --------------- | ----------- | ---------- | --- | --- | --- | ------- | ------------------- | --------------- | --- | --- | --- | --- |
|      |     | BenjaminHoffman |             |            |     |     |     |         | AlexanderDietmüller |                 |     |     |     |     |
|      |     |                 | ETHZürich   |            |     |     |     |         |                     | ETHZürich       |     |     |     |     |
|      |     |                 | AyushMishra |            |     |     |     |         |                     | LaurentVanbever |     |     |     |     |
|      |     |                 | ETHZürich   |            |     |     |     |         |                     | ETHZürich       |     |     |     |     |
Abstract
Current
Simulation Context
Machinelearning(ML)-basedAdaptiveBitrate(ABR)algo- test in Misleading
results
rithmsoftenstruggletobridgethegapbetweensimulation Training Context
ML-based
| andreality.Theirstrongperformanceinsyntheticenviron- |     |     |     |     |     |     |     | ABR |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mentsfrequentlyfailstogeneralizetoreal-worldconditions. ABR-ARENA Representative
test in
Researchershavethereforebeguntestingthesealgorithms benchmark
| over the | Internet | to incorporate |     | real-world |     | feedback | into |     |     |     |     |     |     |     |
| -------- | -------- | -------------- | --- | ---------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Proposed
theirdesign.Inthispaper,weshowthatsincenetworkcondi-
tionsvarysignificantlyacrosstheglobe,testinginindividual
|     |     |     |     |     |     |     |     |     |     | servers | clients |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | --- | --- | --- |
real-worldenvironmentscansufferfromthesamegeneral-
izationissuesaslab-basedtesting.Existingtestingplatforms
Figure1.ABR-Arenaenablesefficientlyevaluatingalgo-
face(andmightevenbeobliviousto)thislimitationbecause
rithmsinenvironmentsacrosstheglobe,allowingformore
theycoverasmallgeographicalregionandrelyonanarrow
representativeperformancebenchmarks.
setofusersaffectedbysurvivorshipbias.Asaresult,their
insightsonanalgorithm’sperformancegeneralizepoorlyto
otherdeploymentsacrosstheInternet,hinderingthewide-
| spreadadoptionofML-basedABRmethodsinpractice. |     |     |     |     |     |     |     | 1 Introduction |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
To address this gap, we present ABR-Arena, a global Video streaming is the most prominent workload on the
testingplatformthatenablesresearcherstoevaluatetheper-
Internet,accountingforover65%ofdownstreamtraffic[10].
formanceofABRalgorithmsacrossadiversesetofregions Consistently providing high Quality-of-Experience (QoE)
around the globe. As a result of its worldwide coverage, hasthereforebecomecriticalforcontentprovidersseeking
| ABR-Arena | can | reveal | the performance |     | shortcomings |     | of  |     |     |     |     |     |     |     |
| --------- | --- | ------ | --------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tomaintainuserengagement[4].Tomaximizeauser’sQoE,
severalstate-of-the-artML-basedapproaches.Itisextensible AdaptiveBitrate(ABR)algorithmsthatdynamicallyadjust
| and easy | to deploy | in  | additional | locations. |     | We will | make |               |          |             |     |             |     |         |
| -------- | --------- | --- | ---------- | ---------- | --- | ------- | ---- | ------------- | -------- | ----------- | --- | ----------- | --- | ------- |
|          |           |     |            |            |     |         |      | their sending | behavior | in response |     | to changing |     | network |
ABR-Arenaavailabletothecommunitytosupportthede-
|     |     |     |     |     |     |     |     | conditions | are commonly | used | in  | practice. | This typically |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | ---- | --- | --------- | -------------- | --- |
velopment of new ML-based approaches and to facilitate involvesselectingtheappropriatebitratetominimizedelays
meaningfulimprovementstoexistingalgorithms.
andstalltimeattheclient,whilemaximizingvideoquality.
OptimizingvideoQoEovertheInternetisadifficultprob-
| CCSConcepts: |     | •Informationsystems→Multimedia |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lemforclassicalheuristics-basedalgorithms.Theymustcon-
| streaming; | • Computing |     | methodologies |     |     | → Machine |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
tendwithahigh-dimensionalparameterspacethatspans
learning.
|     |     |     |     |     |     |     |     | network conditions, |     | user behavior, |     | device | capability, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | -------------- | --- | ------ | ----------- | --- |
Keywords: AdaptiveBitrateStreaming,MachineLearning videocharacteristics,makingithardtomodelaccurately.
|     |     |     |     |     |     |     |     | This complexity |     | creates | an opportunity |     | for ML-based |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | -------------- | --- | ------------ | --- |
ACMReferenceFormat:
methodstoshine.Theycanrapidlyinterpretvastamounts
BenjaminHoffman,AlexanderDietmüller,AyushMishra,andLau-
ofdata,processlargemodelingspaces,andreplaceheuristic
| rent Vanbever. | 2025. | Into | the Wild: | Real-World |     | Testing | for ML- |     |     |     |     |     |     |     |
| -------------- | ----- | ---- | --------- | ---------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
tuningwithlearningfromexperience.Onthispremise,re-
| Based ABR. | In Practical | Adoption |     | Challenges | of  | ML for Systems |     |     |     |     |     |     |     |     |
| ---------- | ------------ | -------- | --- | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
(PACMI’25),October13–16,2025,Seoul,RepublicofKorea.ACM,New searchhasincreasinglyshiftedawayfromclassicalmethods
York,NY,USA,5pages.https://doi.org/10.1145/3766882.3767186 towardsusingML-basedABRalgorithms[7–9,12,14,18].
|     |     |     |     |     |     |     |     | Theneedforreal-worldfeedback. |     |     |     | However,theadop- |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | ---------------- | --- | --- |
tionofML-basedABRschemesishamperedbyalackofreal-
ThisworkislicensedunderaCreativeCommonsAttribution-ShareAlike4.0 worldfeedback.Whilemanyalgorithmshaveshownpromise
InternationalLicense. whentestedwithintheiroriginaltrainingenvironment,they
PACMI’25,October13–16,2025,Seoul,RepublicofKorea
oftenfailtoperformwhendeployedinpractice[3,6,12].One
©2025Copyrightheldbytheowner/author(s).
possibleapproachcouldbetoevaluatetheminrepresentative
ACMISBN979-8-4007-2205-9/25/10
https://doi.org/10.1145/3766882.3767186 synthetic environments through simulation or emulation.
1
105

However,inthecontextofnetworking,creatingrepresenta- ofPuffer.Moreover,sincePufferisoftenusedasthedefacto
tiveenvironmentsfortestingortrainingischallenging:it state-of-the-artdatacollectionandtestingplatformforABR
hasbeenshownthatthecomplexandheavy-tailednature algorithms,itslimitationsalsoriskmisguidingthedesignsof
ofInternettrafficmakesitparticularlyhardtoreplicateina futureML-basedalgorithmsviaperformancefeedbackthat
controlledsetting[1,14,15].Inotherwords,toevaluatethe mightbetoospecifictoitsnarrowcontextandcoverage.
trueperformanceofanML-basedalgorithm,weneedtotest
it in real-world scenarios. Therefore, the current strategy OurApproach. Toaddressthisgapinalgorithmevalua-
formakingthesealgorithmssuitablefortheInternetisto tion,aswellastheshortcomingsinpriorwork,wepropose
directlytrainandevaluatetheminsitu,ontheInternetitself. ABR-Arena,aPython-basedtestinginfrastructureforthe
ProjectslikePuffer[14]currentlyleadthechargeonthis efficientevaluationandcomparisonofABRalgorithmper-
front. Puffer is an open-source YouTube-like service that formance across diverse real-world environments (fig. 1).
streamslivetelevisiontorealusersacrosstheUnitedStates Bycontainerizingstreamingserversanddeployingthemto
usingbothclassicalandML-basedABRalgorithms.Several cloudinstancesworldwide,wedesignABR-Arenatobeeasy
state-of-the-artML-basedapproaches,inparticularFugu[14], touseandtoextendtonewlocations.Wemitigatetheimpact
Maguro[8],andUnagi[8],havebeenshowntooutperform ofsurvivorshipbiasbynotrelyingonreturningusers,but
classicalbuffer-basedorthroughput-basedABRschemes[5, ratherstreamtorandomuserssourcedviaAmazonMechan-
11, 17] when trained using Puffer data and tested within icalTurk(MTurk),apopularcrowdsourcingmarketplace.
Puffer’sreal-worldenvironment.Fugu’screatorsreportcon- Inthispaper,weuseABR-Arenatoevaluatestate-of-the-
sistentlyoutperformingalltestedclassicalmethods1interms artML-basedABRalgorithmsinfourdiverseregions.We
ofvideoquality,andallbutoneintermsofstalltime[14]. demonstratethatalgorithmstrainedonPuffer’sdatamight
Similarly,Maguro’screatorsevenclaimtoachieve78%lower generalizepoorlytootherreal-worldenvironments,insome
stalltimethanFugu,aswellasimprovedvideoquality[8]. casesevenlosingtheiradvantageoverclassicalschemes.
Tothisdate,MaguroandUnagiremainthebest-performing Tosummarize,wemakethefollowingkeycontributions:
algorithmsonthePufferplatform,showcasingthebenefits
1. We propose ABR-Arena, an infrastructure for effi-
ofusingML-basedABRalgorithmsovertheInternet.
cientlyevaluatingmultipleABRalgorithmsacrossdi-
Despiteitsmerits,Pufferhasthreemainlimitationshinder-
verseenvironmentsaroundtheglobe.
ingitsresultsfromgeneralizingtodeploymentsinpractice.
2. Weaddresstheshortcomingsofpreviousworkbyde-
1. Lackofregionaldiversity.ThePufferinfrastructure
ployingourstreamingserversinmultiplecontinents
isdeployedonasingleserverinStanfordanditsview-
andstreamingtorealusersglobally,ensuringcoverage
ershipisrestrictedtotheUnitedStates,whichlimits
ofalargediversityofnetworkconditions–similarly
theplatform’sabilitytocapturearepresentativeset
towhatPantheondidforcongestioncontrol(CC)[15].
ofglobalnetworkconditions.Aswewillshowin§3,
Toavoidthepresenceofsurvivorshipbias,westream
thislackofdiversitycanbeamajorhurdlewhenmea-
toQoE-insensitiveuserssourcedviaMTurk.
suringanABRalgorithm’sperformanceinpractice.
3. Wedemonstratetheeffectivenessofourapproachby
2. Survivorshipbias.ThePufferdataalsosuggeststhe
evaluatingtheperformanceofthreestate-of-the-art
presenceofsurvivorshipbiasintheirusers.Forexam-
ML-basedABRalgorithmsacrossfourreal-worlden-
ple,thestudy’sproposedalgorithmFuguimprovedby
vironmentsinEurope,theAmericas,andAsia.
roughly50%intermsofstallratiowhencomparing
4. Weshowthatanalgorithm’sperformanceinasingle
Februaryof2025toitsinitialperformanceinFebru-
environment–especiallyitstrainingenvironment–
aryof2019withoutanyretraining.Whilethestudy
canvarygreatlyfromitsresultsinothercontexts,in
initiallyattractedadiversesetofusersatitslaunch,
somecasesperformingworsethannon-MLmethods.
Fugu’sperformanceimprovementovertimeindicates
thatusersexperiencinghigherQoEaremorelikelyto We plan to make ABR-Arena available to researchers
continueusingtheplatform,hencebiasingtheresults. aroundtheworldtoaidthedevelopmentofML-basedABR
3. Hardtodeploy.Finally,sincePufferisdesignedtobe algorithmsandtheiradoptioninpracticebyprovidingmore
highlyavailableandproduction-grade,intheauthor’s diversereal-worldfeedbackontheirperformance.
ownwords[16],itisnon-trivialtobuildanddeploy.It
isthereforecumbersometoreplicatefromscratchin
2 SystemDesign
multipleregionstogathermorediversedata.
WedesignABR-Arenatoaddressthreekeychallenges(fig.2):
Theselimitationscanleaveresearchersoblivioustotheir
(i) providingahigherdiversityofreal-worldtestingenvi-
algorithm’sperformanceinreal-worldenvironmentsoutside
ronments,(ii)mitigatingthepresenceofsurvivorshipbias,
1FuguoutperformsBBA[5],MPC-HMandRobustMPC-HM[17]interms and(iii) ensuringeaseofdeploymentandextensibilityto
ofvideoqualityandallbutRobustMPC-HMintermsofstalltime. additionallocationsandABRalgorithms.
2
106

Backbone. ABR-Arenaconsistsoffourkeycomponents:
Deployment pipeline
aPythoninterface,adeployablestreamingserver,adeploy-
mentandmonitoringpipeline,aswellasaQoEdatacollec- Crowdsourcing
Desired config Cloud provider
tionandevaluationpipeline(fig.2).Inourstreamingserver platform
(ABRs, model weights,
implementation,weextendtheinfrastructuremadeavail- cc, locations, provider, servers users
stream time, etc.)
ablebyPufferandusetheirpre-embeddedvideosources.To globally
maketestingviacrowdsourcedusersstraightforward,we
extendstreamingsupporttoallmajorbrowsersandprevent
Evaluation
browser-basedbackgroundthrottling.Byrandomlyassign- pipeline
ing an algorithm to each streaming session, we maintain
Puffer’s randomized controlled trial property. For deploy-
ment,wecontainerizeourstreamingserverandpushitto
DockerHub.Webuildourdeploymentandmonitoring,as QoE data collection pipeline
wellasourdatacollectionandevaluationpipelinesinPython,
usingthenetUnicornlibraryandservices[2].Thissetupal-
lowsustosimultaneouslydeployourserversonmultiple Figure2.WithABR-Arena,weprovideaccesstomoredi-
cloudinstancesacrosstheglobeandmonitortheexperiments versetestingenvironmentsforABRalgorithmsbyenabling
onarollingbasis,usingrsynctocontinuouslytransferQoE easydeploymenttoserversacrosstheglobe,aswellasmain-
measurementdatatoourlocalmachineforevaluation. tainingextensibilitytofurtherlocationsandABRschemes.
Regionaldiversity. WewanttouseABR-Arenatotest
ABRalgorithmsinavarietyofreal-worldenvironments.To thesamegeneralizationpitfallsPufferhasovertheyears.A
thisend,forthepreliminaryevaluationspresentedinthis usercaneasilyinteractwiththesystembysettingthedesired
paper,wedeployedourstreamingserverstocloudinstances configurations,e.g.,whichABRstotest,theirweightsorvari-
inSaoPaulo,Zurich,Mumbai,andOhio.Wechosethismix ants,whichCCalgorithmtouse,inwhichlocationstodeploy
as a good starting point that covers diverse geographical theservers,whichcloudproviderstouse,howlongtostream
locations.However,thankstoABR-Arena’sextensibility,it toeachuser,etc.Basedontheseinputs,ABR-Arenadeploys
caneasilybeexpandedtomorelocationsgloballyaswell. thedesiredstreamingservers,whiletheusercanmonitor
theinfrastructureandevaluatetheresultsontheirlocalma-
Crowdsourcinganunbiaseduserbase. UnlikePuffer, chineinrealtime.Newtestinglocationscanbereadilyadded
which streams to a returning audience, we field random toABR-Arenaviaatemplate(often,aone-timesetupon
usersviaAmazon’sMTurkservice,similarlytoapproaches thecloudprovider’splatformisrequired),andwemaintain
such as Sensei [19]. Amazon MTurk is a crowdsourcing Puffer’sabilitytohostnewABRschemes.Wewillrelease
marketplacethatprovidesaccesstoabroadsetofInternet ourdatasets,aswellasmakeABR-Arena’scodeavailable,
userstocompletevirtualtasks.Asourusersstemfromapaid enabling researchers to independently build, deploy, and
platform,wemitigatethepresenceofsurvivorshipbiasin extendABR-Arenatoconducttheirownexperiments.
ourresults.Inotherwords,whileresultsfromPufferindicate
thatuserswithagoodstreamingexperiencetendtoreturn 3 PreliminaryResults
more frequently, narrowing the diversity of sessions and
WedemonstratetheeffectivenessofABR-Arenabyevaluat-
biasing the results, our users are insensitive to QoE and ingtheperformanceofFugu,2Maguro,andUnagiacrossfour
arenotaffectedbythesamemechanism.Asthisrestricts
real-worldenvironments.FugucombinesML-basedthrough-
us from capturing additional statistics on user behaviour,
putpredictionwithanMPCcontrollertoformahybridABR
wefocusprimarilyonmeasuringQoEperformancemetrics.
approachandwastrainedonPufferdata.MaguroandUnagi
By using MTurk, we can also handpick the geographical
aretwoRL-basedalgorithms.Botharesimilarlytrainedin
locationofouruserbaseforeachexperiment.Further,we
simulationusingPuffertraces,Unagiusingrandomlycho-
askuserstoprovideadditionalinformationonhow(wired,
sentraces,andMagurousingsamplingintendedtoaddress
wifi,orcellular)andwhere(residential,work,oruniversity)
datasetskewness.Asanon-MLbaseline,wedeployBBA,a
their device is connected to the Internet as metadata. In
simplerbuffer-basedABRalgorithm[5].WeuseABR-Arena
our preliminary results presented here, we fielded 11,156
to deploy our streaming infrastructure to AWS instances
usersfrom93countries.Overall,ourmeasurementscostus
inZurich,Ohio,SaoPaulo,andMumbai,andcollectQoE
roughly500USD.Thisworkdoesnotraiseanyethicalissues.
measurementsbystreamingtousersacrosstheglobe.Addi-
tionally,wecompareourresultstotheperformancethese
Easeofdeploymentandextensibility. WedesignABR-
Arenatobelight-weightandeasilydeployable.Thisallows 2WeuseFugufeb,aFuguvarianttrainedonPufferdatafromFebruary2019
ittobeextendedtonewlocationsgloballyandnotfallinto andusedintheexperimentsintheoriginalpaper[14].
3
107

4%
3%
2%
1%
0%
Maguro Unagi Fugufeb BBA
]%[
gnillatS
tnepS
emiT
17.8
17.6
17.4
17.2
17.0
Maguro Unagi Fugufeb BBA
]Bd[
MISS
egarevA
Puffer Saopaulo Zurich Mumbai Ohio
Figure3.Thelargevariationsinstallratio(left–lowerisbetter)andvideoquality(right–higherisbetter)acrossdeployments
showthattestinginasingleenvironmentdoesnotallowforarepresentativeevaluationofanABR’sperformance.Inparticular,
analgorithm’sperformanceinitstrainingcontext—herePuffer—canbemarkedlydifferentfromitsperformanceinpractice.
Weplotthemeanandthebootstrapped95%confidenceintervalsforeachalgorithmineachenvironment.
algorithmsachieveonPuffer.Inourexperiments,wecollect inourenvironmentscomparedtoPuffer(fig.3).Asbefore,
510streaminghoursacross11,156users,eachstreamingfor this gap is especially stark for both RL-based algorithms,
2minutesand45secondsonaverage,betweenFebruaryand MaguroandUnagi,comparedtoFugu,whichisconsiderably
June of 2025. Given the uneven distribution of streaming moreresilient.AlthoughbothMaguroandUnagioutperform
hours(302hoursinZurich,95hoursinOhio,93hoursinSao FuguonPuffer,inourexperimentsinABR-Arena,theirstall
Paulo,20hoursinMumbai),wecomputemetricsperstream- ratiosaresignificantlyhigherthanFugu’s–by276.8%and
ingsessionandcomparetheiraveragesperenvironment. 264.8%,respectively.ThedifferencesinSSIMbetweenPuffer
andABR-Arenaweresmaller,butstillpresent.
Performancemetrics. Tocomparetheperformanceof
When considering BBA, the results are even more sur-
anABRalgorithm,weevaluatetheQoEitprovidesviatwo
prising.DespitecominglastonPuffer,BBA’sstallreduction
majormetricsshowntodriveauser’sengagementwithvideo
outperformsbothMaguroandUnagiinourenvironments,
content:thevideoqualityandthebufferingtime[4,11].We
equallingFugu.WhileBBA’sSSIMislower,itstrikesabet-
useSSIM3(higherisbetter)tomeasuretheperceivedquality
tertrade-offbetweenstallingandqualitythanMaguroand
ofavideo[13],andthestallratio(lowerisbetter),i.e.,the
Unagiinchallengingenvironments,whosestallratiosreach
percentageoftimespentstalling,tomeasurebufferingtime. > 3%inSaoPaulo.OnlyFuguofferssimilarlyrobustper-
Varianceacrossenvironments. TheQoEperformance formance.Theseresultssuggestthat,duetoitslimitations,
ofallalgorithmsvariesmarkedlyacrossourenvironments, testingonPufferdoesnotnecessarilyrevealthesensitivityof
bothabsolutelyandrelatively(fig.3).Thisisespeciallypro- ML-basedABRstoOut-of-Distribution(OOD)environments.
nouncedfortheRL-basedschemes,MaguroandUnagi,with
theirvarianceinstallratioacrossourenvironmentsbeing 4 Discussion
roughly10timeshigherthanFugu’s.WhiletheSaoPauloen-
Overall,ourresultshighlightboththevalueandnecessity
vironmentprovesthemostchallenging,regionalproficiency
ofABR-Arena:QoEperformancevariessignificantlyacross
variesbetweenalgorithms.Forinstance,Maguroperforms
real-worldenvironments,andcomparisonswithPufferre-
worseinOhiothanZurich,whileUnagishowstheopposite
veal how much ML-based ABR performance can diverge
trend.Fugu,thankstoitshybriddesign,ismorerobustto
betweentraininganddeployment.Areliableevaluationof
environmentalchanges,butstillnotimmunetothem.InSao
thesealgorithmscanonlybedonebytestingthemacross
Paulo,Fugu’sstallratiois86.4%higheranditsSSIM0.14dB
diverseregionswithvaryingnetworkconditions.
lowerthaninOhio.Similarly,ournon-MLbaseline,BBA,
However,achievingsufficient diversityduringevaluation
varieslessthanMaguroandUnagiintermsofstallratio.
remainsachallenge.WhileABR-Arenaimprovesonpre-
viousworkand,byitsextensibledesign,allowsittogrow
Traininganddeploymentgap. Toassesshowwellal-
morediverseinthefuture,ithasitslimitations.Ourcurrent
gorithmsgeneralizebeyondtheirtrainingcontexts,wecom-
deployments—limitedtomajorcloudprovidersandauni-
paretheirperformanceinABR-Arenaagainsttheirperfor-
versitynetwork—maynotreflectproductionenvironments
manceonPuffer.Tothisend,weanalyzed23,236streaming
oflargestreamingplatforms.Ourpreliminarydatasetisalso
hours (around 186,329 individual sessions) of Puffer data
smaller than the Puffer dataset, despite covering more re-
fromMarch2025.Acrosstheboard,stallratiosareworse
gions.Weplantoremedythisbycontinuingtocapturemore
3Asin[14],weconvertthestandardSSIMmetrictoadecibelscale. results to further substantiate our findings. Finally, while
4
108

we measure the performance gap that can exist between [8] SagarPatel,JunyangZhang,NinaNarodystka,andSangeethaAbdu
traininganddeployment,withsomealgorithmsevenlosing Jyothi.2024. PracticallyHighPerformantNeuralAdaptiveVideo
theiredgeoverclassicalmethods,wedonotofferanysolu- Streaming. Proc.ACMNetw.2,CoNEXT4,Article30(Nov.2024),
23pages.doi:10.1145/3696401
tionsonhowtocloseit.ABR-Arenacanperhapsaidhere
[9] FelipeRosa,SimoneFerlin,AnnaBrunstrom,andBrunoKimura.2025.
aswell,byhelpingcollectmorediversetrainingdatafrom
End-to-End360°VideoStreamingoverHTTP/3:Architectureand
differentenvironmentstolearnalgorithmsthatgeneralizeto Implementation.InProceedingsofthe2025AppliedNetworkingResearch
deploymentsacrosstheInternet.Thisremainsfuturework. Workshop(Madrid,Spain)(ANRW’25).AssociationforComputing
Machinery,NewYork,NY,USA,9–16. doi:10.1145/3744200.3744784
[10] SandvineCorporation.2023.VideoPermeates,StreamingDominates.
5 Conclusion 14–15pages. https://www.sandvine.com/hubfs/Sandvine_Redesign_
2019/Downloads/2023/reports/SandvineGIPR2023.pdf
Inthiswork,wepresentABR-Arena,aglobaltestingplat-
[11] KevinSpiteri,RahulUrgaonkar,andRameshK.Sitaraman.2020.BOLA:
form for evaluating (ML-based) ABR algorithms across a
Near-OptimalBitrateAdaptationforOnlineVideos.IEEE/ACMTrans-
diversesetofreal-worldenvironments.UsingABR-Arena, actionsonNetworking28,4(2020),1698–1711.doi:10.1109/TNET.2020.
weaddressandrevealthevarianceofanalgorithm’sQoE 2996964
performancebetweenitstrainingenvironmentanditsde- [12] YiSun,XiaoqiYin,JunchenJiang,VyasSekar,FuyuanLin,Nanshu
Wang,TaoLiu,andBrunoSinopoli.2016. CS2P:ImprovingVideo
ployment,aswellasacrossdifferentgeographicalregions.
BitrateSelectionandAdaptationwithData-DrivenThroughputPre-
Bydesigningourplatformtobeeasytouse,todeploy,and
diction.InProceedingsofthe2016ACMSIGCOMMConference(Floria-
toextend,wehopetosupportresearchersintesting,devel- nopolis,Brazil)(SIGCOMM’16).AssociationforComputingMachinery,
oping, and adopting new ML-based approaches that offer NewYork,NY,USA,272–285. doi:10.1145/2934872.2934898
meaningfulimprovementsoverexistingschemes. [13] ZhouWang,A.C.Bovik,H.R.Sheikh,andE.P.Simoncelli.2004.Image
qualityassessment:fromerrorvisibilitytostructuralsimilarity.IEEE
TransactionsonImageProcessing13,4(2004),600–612. doi:10.1109/
References TIP.2003.819861
[14] FrancisY.Yan,HudsonAyers,ChenzhiZhu,SadjadFouladi,James
[1] Mihovil Bartulovic, Junchen Jiang, Sivaraman Balakrishnan, Vyas
Hong,KeyiZhang,PhilipLevis,andKeithWinstein.2020.Learning
Sekar,andBrunoSinopoli.2017. BiasesinData-DrivenNetwork-
insitu:arandomizedexperimentinvideostreaming.In17thUSENIX
ing,andWhattoDoAboutThem.InProceedingsofthe16thACM
SymposiumonNetworkedSystemsDesignandImplementation(NSDI
WorkshoponHotTopicsinNetworks(PaloAlto,CA,USA)(HotNets’17).
20).USENIXAssociation,SantaClara,CA,495–511. https://www.
AssociationforComputingMachinery,NewYork,NY,USA,192–198.
usenix.org/conference/nsdi20/presentation/yan
doi:10.1145/3152434.3152448
[15] FrancisY.Yan,JestinMa,GregD.Hill,DeeptiRaghavan,RiadS.Wahby,
[2] RomanBeltiukov,WenboGuo,ArpitGupta,andWalterWillinger.
PhilipLevis,andKeithWinstein.2018.Pantheon:thetrainingground
2023. InSearchofnetUnicorn:AData-CollectionPlatformtoDe-
forInternetcongestion-controlresearch.In2018USENIXAnnualTech-
velopGeneralizableMLModelsforNetworkSecurityProblems.In
nicalConference(USENIXATC18).USENIXAssociation,Boston,MA,
Proceedingsofthe2023ACMSIGSACConferenceonComputerand
731–743. https://www.usenix.org/conference/atc18/presentation/yan-
CommunicationsSecurity(Copenhagen,Denmark)(CCS’23).Asso-
francis
ciationforComputingMachinery,NewYork,NY,USA,2217–2231.
[16] Francis Y. Yan and the Stanford Network Research Group. 2020.
doi:10.1145/3576915.3623075
PufferDocumentation. https://github.com/StanfordSNR/puffer/wiki/
[3] PaulCrewsandHudsonAyers.2018.CS244’18:RecreatingandExtend-
DocumentationAccessedJuly29,2025.
ingPensieve. https://reproducingnetworkresearch.wordpress.com/
[17] XiaoqiYin,AbhishekJindal,VyasSekar,andBrunoSinopoli.2015.A
wp-content/uploads/2018/07/recreating_pensieve.pdf
Control-TheoreticApproachforDynamicAdaptiveVideoStreaming
[4] FlorinDobrian,VyasSekar,AsadAwan,IonStoica,DilipJoseph,Aditya
overHTTP.InProceedingsofthe2015ACMConferenceonSpecial
Ganjam,JibinZhan,andHuiZhang.2011.Understandingtheimpact
InterestGrouponDataCommunication(London,UnitedKingdom)
ofvideoqualityonuserengagement.InProceedingsoftheACMSIG-
(SIGCOMM’15).AssociationforComputingMachinery,NewYork,NY,
COMM2011Conference(Toronto,Ontario,Canada)(SIGCOMM’11).
USA,325–338. doi:10.1145/2785956.2787486
AssociationforComputingMachinery,NewYork,NY,USA,362–373.
[18] HibaYousef,JeanLeFeuvre,andAlexandreStorelli.2020.ABRpre-
doi:10.1145/2018436.2018478
dictionusingsupervisedlearningalgorithms.In2020IEEE22ndIn-
[5] Te-YuanHuang,RameshJohari,NickMcKeown,MatthewTrunnell,
ternationalWorkshoponMultimediaSignalProcessing(MMSP).1–6.
andMarkWatson.2014.Abuffer-basedapproachtorateadaptation:
doi:10.1109/MMSP48831.2020.9287123
evidencefromalargevideostreamingservice.InProceedingsofthe2014
[19] XuZhang,YiyangOu,SiddharthaSen,andJunchenJiang.2021.SEN-
ACMConferenceonSIGCOMM(Chicago,Illinois,USA)(SIGCOMM’14).
SEI:AligningVideoStreamingQualitywithDynamicUserSensitiv-
AssociationforComputingMachinery,NewYork,NY,USA,187–198.
ity.In18thUSENIXSymposiumonNetworkedSystemsDesignand
doi:10.1145/2619239.2626296
Implementation (NSDI 21). USENIX Association, 303–320. https:
[6] HongziMao,ShannonChen,DrewDimmery,ShaunSingh,Drew
//www.usenix.org/conference/nsdi21/presentation/zhang-xu
Blaisdell,YuandongTian,MohammadAlizadeh,andEytanBakshy.
2019.Real-WorldVideoAdaptationwithReinforcementLearning.In
ProceedingsoftheICML2019WorkshoponReinforcementLearningfor
RealLife(RL4RealLife).
[7] HongziMao,RaviNetravali,andMohammadAlizadeh.2017. Neu-
ralAdaptiveVideoStreamingwithPensieve.InProceedingsofthe
ConferenceoftheACMSpecialInterestGrouponDataCommunication
(LosAngeles,CA,USA)(SIGCOMM’17).AssociationforComputing
Machinery,NewYork,NY,USA,197–210.doi:10.1145/3098822.3098843
5
109