Veritas: Answering Causal Queries from Video Streaming Traces
ChandanBothra∗ JianfeiGao∗
PurdueUniversity PurdueUniversity
SanjayRao BrunoRibeiro
PurdueUniversity PurdueUniversity
ABSTRACT ACMReferenceFormat:
ChandanBothra∗,JianfeiGao∗,SanjayRao,andBrunoRibeiro.2023.Veritas:
Inthispaper,weconsiderthetaskofansweringwhat-if questions
AnsweringCausalQueriesfromVideoStreamingTraces.InACMSIGCOMM
inthecontextofadaptivebitrate(ABR)videostreamingwithout
2023Conference(ACMSIGCOMM’23),September10–14,2023,NewYork,
accesstorandomizedcontroltrials(RCTs)(e.g.,noA/Btesting)
NY,USA.ACM,NewYork,NY,USA,16pages.https://doi.org/10.1145/
–i.e.,givenrecordeddataofanexistingdeployedsystem,what 3603269.3604828
wouldbetheperformanceimpactifwechangeditsdesign.Our
workmakesthreecontributions.First,weshowtheproblemischal- 1 INTRODUCTION
lengingsincedatamayonlybeavailableforasingleABRalgorithm
Acentralthemeofdata-drivennetworkingisansweringwhat-if
withoutRCTs,andsinceitisnecessarytodealwiththecascading
questions—givendataobtainedfromareal-worlddeploymentof
effectsthatpastABRdecisionshaveonfuturedecisions.Nextwe
anexistingdeployedsystem,wewanttoinferwhatwouldhave
presentVeritas,thefirstframeworkthattacklescausalreasoning
happenedifwehadusedadifferentsystemdesign.Forinstance,
forvideostreamingwithoutrequiringdatacollectedthroughRCTs.
givendatacollectedfromrealvideostreamingsessions,avideo
IntegraltoVeritasisaneasy-to-interpretdomain-specificMLmodel
publishermaywishtounderstandtheperformanceifadifferent
thatrelatesthelatentstochasticprocess(intrinsicbandwidththat
AdaptiveBitrate(ABR)algorithmwereused(Figure1),orifanew
thevideosessioncanachieve)toactualobservations(download
videoquality(e.g.,an8Kresolution)wereaddedtotheABRse-
times),whileexploitingcounterfactualqueriesviaabductionusing
lection,oranexistingbitratechoicewereremoved(e.g.,during
theobservedTCPstates(e.g.,congestionwindow)forblockingthe
theCOVIDcrisis,manyvideopublishersrestrictedthemaximum
cascadingdependencies.Third,weevaluateVeritas’sabilitytoac-
bitrate[4]).Answeringwhat-if questionsofthisnatureisalso
curatelyanswerawiderangeofwhat-ifquestionsusingemulation
knownascausalreasoning.Causalinferenceconsiderstheeffectof
experiments,anddataofrealvideosessionsfromPuffer.Theresults
eventsthatdidnotoccurwhilethedatawasbeingrecorded[34],
showthat(i)Veritasaccuratelytacklesawiderrangeofwhat-if
andhasbeenexploredindomainsasdiverseaseconomics[9]and
questions(e.g.,changeofbuffersizeorvideoquality)thatexisting
epidemiology[38].
approachescannot;(ii)VeritaswithoutRCTtrainingdataachieves
Shortcomingsoftraditional(associational)machinelearn-
performancecomparableorbetterthanarecentparallelapproach
ing(ML).Severalwidely-usedMLtoolsareinadequateforcausal
thatrequiresRCTdata;and(iii)inmanyscenariosVeritasachieves
inference.Manyapproaches(e.g.,neuralnetworksanddecision
accuracyclosetoanidealoracle.
trees)merelycapturecorrelationsincollecteddata,limitingthem
CCSCONCEPTS toassociationspredictions,i.e.,predictionsthatarerelatedtoassoci-
ationsbetweenobservationsinadeployedsystem.Associations,
•Networks→Applicationlayerprotocols;Networkmeasure-
however,areinadequatetoanswercausalquestions.Forinstance,
ment;Networkperformancemodeling;
peoplecarryingumbrellasonasunnymorningisagoodpredic-
torofrainintheafternoon.However,forbiddingpeopletocarry
KEYWORDS
umbrellasinthemorningdoesnotpreventrainintheafternoon.
Videostreaming;CausalInference;Predictivemodels;Applying Similarly,invideostreaming,anABRalgorithmcouldchooselower
machinelearningtonetworks. bitrateswhennetworkconditionsarepoor,resultinginanassocia-
tionbetweenlowervideobitratesandrebufferingevents.However,
decreasingbitratewillnotcausemorerebufferingevents–rather,
theoppositeislikelytohappen.
The approach widely considered to be the gold standard for
causalinferenceisRandomizedControlTrials(RCTs).BothRCTs
andotherapproachessuchasReinforcementLearningallowreason-
This work is licensed under a Creative Commons Attribution‐NonCommercial‐
ShareAlike International 4.0 License. ingaboutaredesignedsystembutrequireactiveinterventionsthat
ACMSIGCOMM’23,September10–14,2023,NewYork,NY,USA involvechangingasystem,andobservingitsperformanceamong
©2023Copyrightheldbytheowner/author(s).
realusers.Whiletheseapproacheshaveseveraladvantages,they
ACMISBN979-8-4007-0236-5/23/09.
https://doi.org/10.1145/3603269.3604828 mustbeconservativelydeployedastheycouldbedisruptivetothe
performanceofrealusers,andmayincreaseinequalityofservice
*Bothauthorscontributedequallytothispaperandcanbecontactedatfollowing:
cbothra@purdue.edu,gao462@purdue.edu
738

ACMSIGCOMM’23,September10–14,2023,NewYork,NY,USA ChandanBothra∗,JianfeiGao∗,SanjayRao,andBrunoRibeiro
Veritasonlyreliesoneasy-to-interpretandlow-complexityML
Video Network
Quality Streaming Conditions models,whileonlyrequiringpre-recordeddata.Thechallengethat
Algorithm A Veritastacklesisabduction[34,Section4.2.4],whichinvolves(i)
inferringasetoflikelyvaluesforlatentvariablesconsistentwith
Video theobservations;and(ii)modelingtheproposedchangestoreturn
Quality?
A
S
lg
tr
o
e
r
a
it
m
hm
in g
B Log
theanswertoawhat-ifqueryusingtheinferredlatentvariables.
Whileabductionischallengingingeneral,thekeyinsightsofVeritas
are(a)acarefulselectionofcontrolvariables(theTCPstatesat
thestartofeachchunkdownload)thatsimplifiesthecausaltask,
what-if? and(b)aMLmethodtoperformabductionthatisprincipled,yet
accesibleandeasytointerpretgivenitleveragesdomaininsights.
Morespecifically,aspartofVeritas,wehavedesignedadomain-
Figure1:Examplewhat-ifquestionaskedbyanetworkde-
specificMLmodelthatrelatesthelatentstochasticprocess(intrinsic
signer:whatwouldbethequalityifalgorithmBhadbeen
bandwidththatthevideosessioncanachieveifTCPwereinsteady
usedinsteadofAunderthesamenetworkconditions?
statethroughoutthesession)toactualobservations(actualthrough-
putobservedbychunkdownloads),whenalsogivenasequenceof
(A/Btestingmaybeperformedonlower-tiercustomersratherthan
additionalcontrolvariablesintheformoftheTCPstatesatthestart
premiumcustomers).Further,theycannotanswerwhat-ifquestions
ofeachchunkdownload.Thiscontrolisneededsincetheactualob-
aboutpastsessions(§2).
servedthroughputdependsontheTCPstateoftheconnection(e.g.,
Confoundersinvideostreaming.Incontrasttotheabove
whetherslow-startisinprogress),andthesizeofthedownloaded
approaches, our work focuses on causal inference on passively
object.Thecontrolallowsusto“invert”theobservedthroughput
collecteddata.OurapproachdoesnotrequireRCTs,andcancom-
variablesinordertogetthelatentbandwidthvariables.
plementthem.Forinstance,ourapproachenablesmoreaccurate
Toensurewerepresentthestatisticaldependenciesinthela-
trace-drivenemulationsandsimulationsofawiderangeofdesign
tentbandwidthtimeseriesduringtheinversionprocess,wede-
alternativeswithoutimpactingtheperformanceofliveusers.The
velopanHigh-orderEmbeddedHiddenMarkovModel(HoEHMM),
mostpromisingalternativesmaythenbetestedusingRCTs.We
whichembedsadomain-specificmodelfortheemissionprocess.A
considercausalinferencenotonlyabouthowtheproposedchange
BayesianposteriorsamplingoftheHoEHMMallowsustocapture
wouldaffectsessionsinthefuture(alsoreferredtoasinterventional
theuncertaintyinherentinthecombinationofourinversion,sto-
inference)butalsohowitwouldhaveaffectedagivensessionin
chasticmodeling,andthedata.Onceasampledinvertedbandwidth
thepast(alsoreferredtoascounterfactualinference).Weexpand
processisobtained,wecannowdirectlyevaluatetheproposed
onthedistinctionsin§2.1.
Whilecausalinferencecanbenefitmanynetworkingtasks,in
changes,andreturntheanswertothewhat-ifquery.Ratherthana
thisworkwefocusonvideostreaming.First,itisadomainwhere
singlepointestimate,Veritasprovidesarangeofpotentialoutcomes
reflectingtheinherentuncertaintyininferencesthatcanbemade
therehasbeenmuchinterestindata-drivendesignoptimizations[11,
fromthedata.
24,26,29,43,50].Second,videostreamingreliesonadaptivebit
rate (ABR) algorithms, where decisions made by the algorithm
Evaluation.WeevaluateVeritaswithrespecttoitsabilityto
dependonnetworkconditions,whichinturnimpactobservable
answerarangeofwhat-ifcausalqueriesincludingtheimpactof(i)
changingtheABRalgorithm;(ii)changingthebuffersize;and(iii)
measurements.Owingtotheadaptivenature,thenetworkconditions
changingthesetofvideoqualitiesthattheABRalgorithmcould
encounteredduringthesessionactasasequenceoflatentconfounding
select.WecomparethepredictionsfromVeritaswith:(a)abaseline
variables,resultingincomplexspuriouscorrelationsindata,which
approachthatusesthelogsdirectlywithoutexplicitcausaladjust-
canimpairtheuseofcommonMLapproaches.
ments;and(b)CausalSim[8],aparallelwork,whichalsoseeksto
Cascading effects complicate causal inference in video
performcausalinferenceforvideostreaming.CausalSimhasan
streaming.Thedynamicnatureofvideostreamingmakescausal
RCTrequirementinthetrainingphasewhereeachof𝑁 sessionsis
inferencechallenging.Considerthefollowingwhat-ifquestionfora
assignedtooneofmanyABRpoliciesatrandom.Weperformcom-
recordedvideosession:whatifbitrate𝑏′ratherthantheoriginal𝑏
parisonsin:(a)controlledemulationsettingswheregroundtruth
hadbeenchosenforvideochunk𝑛 ≥1,𝑏′ ≠𝑏?Thiswhat-ifchange
bandwidthinformationisavailable.Here,wealsocompareVeritas
(from𝑏to𝑏′atchunk𝑛)hasacascadingimpactonthesession’s
withanoraclethatknowsgroundtruth;and(b)"in-the-wild"set-
futurebufferoccupancy,andbitrateselectiondecisions,aswell
tingsusingdataofrealvideostreamingsessiondataobtainedfrom
asthestarttimesoffuturechunkdownloads.Thus,allobserved
Puffer[50].Here,wealsocompareVeritas’spredictionswiththe
variablesdescribingchunk𝑛′ ≥𝑛canpotentiallychangeduetoa
trueperformanceexperiencedbyadistributionallysimilargroup
differentdecisionforchunk𝑛.Datarecordedinthesessionafter
ofusers.
chunk𝑛nolongerrepresentswhatwillhappeninthesessioneven
ifnootherchangesweremadeinthefuture.
Results:Wesummarizeourkeyresults:
•Forwhat-ifquestionspertainingtouseofhighervideoqualitiesor
TamingthecomplexityofcausalinferencewithVeritas.
adifferentbuffersize,VeritassignificantlyoutperformsCausalSim
Motivated by the above challenges we design Veritas, a novel
andthebaselinewhileperformingclosetotheoracle–e.g.,when
frameworkforansweringcausalqueriesforvideostreaming.Rather
predictingthemedianqualityacrosssessionsifhighervideoquali-
thancomplexMLmodels,orresortingtorandomizedtrials(RCTs),
tiesareused,Veritasachievesapredictionerroroflessthan0.022%,
739

Veritas:AnsweringCausalQueriesfromVideoStreamingTraces ACMSIGCOMM’23,September10–14,2023,NewYork,NY,USA
whilethebaselineandCausalSimhaveapredictionerrorof4.06% outcomesofanexistingsystem.Thesetasksrequirecausalinference,
and3.89%respectively.Notethatthecounterfactualcapababilities whichpredictstheoutcomeofanintervention,achangeintheway
ofCausalSimarelimited,sinceitisunabletoaccuratelyevaluate thesystemoperates.Specifically,Q2pertainstotheimpactofan
actionsthatwereoutsidethescopeoftheinitialRCTexperiment interventionalchangetothesystemdesign:howchangingtheABR
asisthecasewiththesewhat-ifqueries. logictodownloadachunkofdifferentsizeimpactsdownloadtime
•ForquestionspertainingtotheperformanceofanewABRalgo- (andthesessionasawhole).Moregenerally,thedesignermaywish
rithm,ourresultsshowVeritaswithoutRCTdata(i.e.,withdataof tounderstandtheimplicationsonperformanceifsomeaspectof
onlyasinglepreviouslydeployedalgorithm)performscompara- thesystemwerechanged(e.g.,changingthesetofvideoqualities
blytoCausalSimwithRCTdataobtainedfromatleasttwoother theclientcouldchoosefrom,thebuffersize,ortheABRalgorithm).
ABRalgorithms.Further,Veritasoutperformsboththebaselineand Wenextdefinethetwotypesofcausalinferencealgorithmsof
CausalSimwithoutRCTtrainingdata.Forexample,inasetting interestinourwork.
wherebothVeritasandCausalSimwithRCTdatacorrectlypredict
Definition1(Interventionalinferencefornetworktasks).
norebuffering,CausalSimwithoutRCTdataincorrectlypredicts
rebufferingforabout18%ofthesessions. Given(i)existingrecordedsessionsrunninganoldmethod;(ii)anda
•VeritaswithoutRCTdatamatchestheperformanceofCausalSim newmethod;ourtaskistopredicttheperformanceofthenewmethod
withRCTdatainansweringwhat-ifquestionsusingrealworld onnewsessions.
videostreamingobtainedfromPuffer,insomecasesevenperform-
Definition2(Counterfactualinferencefornetworktasks).
ingbetterinestimatingbufferoccupancyandrebufferingratioof
Given(i)existingrecordedsessionsrunninganoldmethod;(ii)anda
thevideosessions.
newmethod;ourgoalistopredicttheperformanceofthenewmethod
Overall,theresultsshownewcapabilitiesandthepromiseof
ifithadbeenusedinplaceoftheoldmethodinthesamerecorded
Veritasintacklingawiderangeofwhat-ifquerieswhilenotrequir-
sessions.
ingRCTtrainingdata.WehavemadethesourcecodeofVeritas
publiclyavailable1.
2.2 Confounderswithvideostreaming.
2 BACKGROUNDANDMOTIVATION MostMLmethodsworkbylearningassociationsinexistingdata,
Inthissection,wemotivatetheneedforcausalreasoningincon- and,hence,areonlyappropriateforassociationalpredictions.Un-
textofvideostreaming,andwhyMLtoolsusedforassociational fortunately,theresultofanassociationalpredictionmaybewildly
predictions,andapproachessuchasReinforcementLearningand inaccurateforacausalquestionowingtoconfounders.Inthecon-
RandomizedControlTrialsfallshort. textofvideostreamingtherearemanyconfounders:
Intrinsicnetworkbandwidth(INB)asanunobservedcon-
2.1 Causalvs.associationalqueries. founder.INBcapturesthebandwidththenetworkisintrinsically
Causalvs.associationalqueries. Videostreamingtodaytypi- capableof,withoutconsideringdependenceonsize,andthetrans-
callyinvolvessplittingvideointochunks,eachencodedatmultiple portprotocol–i.e.,whatthetransportprotocolwouldintrinsically
qualities.ClientspickqualitiesforeachchunkusingAdaptiveBit seeifitwererunninginsteadystate.InordertoexplainINBasan
Rate(ABR)algorithmssoastobalancebetweenachievinghigh unobservedconfounder,wefirstpresentanillustrativeexample.We
videoquality,whileavoidingrebufferingbasedonnetworkcondi- conductcontrolledemulationexperimentson100FCCthroughput
tions[7,20,21,28,41,47,51]. traces[2],splitequallybetweenpoor[0-0.3Mbps]andgood[9-10
Considerdatacollectedfromavideostreamingsystem,whichin- Mbps]networkconditions,withtheMPCalgorithm[35]inanemu-
cludesthesizesanddownloadtimesofchunksforeachsession.The lationtestbed(detailsin§4.1).Figure2(a)showsdownloadtimesof
followingquestionsshowcasethedifferencebetweenassociational chunksacrossallvideosessions,witheachboxplotcorresponding
andcausalqueries: tochunkswithinaparticularsizerange.
Q1.Givenasetofobservationsofchunksizesanddownloadtimes Figure2(a)showsaseemlyoddassociation,wherebyincreasing
ofavideosession,ifthenextdownloadinthelogisachunkofsize thechunksizemaydecreasethedownloadtime.Thisisaconse-
𝑠,whatwouldbethedownloadtime? quenceoftheadaptivebitrate(ABR)algorithmmakingtheINBan
Q2.Givenasetofobservationsofchunksizesanddownloadtimes unobservedconfounderbetweenchunksizeanddownloadtimes.
ofavideosession,ifthedesignerhadintervenedinthesessionand Whennetworkconditionsarepoor(i.e.,theINBislow),theABR
hadaskedtonextdownloadachunkofsize𝑠′,𝑠′ ≠𝑠,whatwould tendstoselectsmallerchunksizes.Whennetworkconditionsare
bethedownloadtime? good(i.e.,theINBishigh),theABRtendstoselectlargerchunks.
QuestionQ1pertainstopassivelyobservingthesystemathand Hence,smallerchunkscanhavelongerdownloadtimesthanlarger
withitsexistingABRalgorithmandsettings.Theseofflineobser- chunks.
vationscanbeusedtomakepredictionsaboutthesystemunder TCPstateasanunobservedconfounder.Onemaynaively
similarconditions.Morebroadly,anassociationalpredictionseeks think that, while the association between download times and
topredictoutcomesofasystemwithoutinterfering(intervening) chunksizeshastheINBasaconfounder,theassociationbetween
withitsoperation.Incontrast,manyreal-worldnetworkingtasks observedthroughputandchunksizesshouldnothaveunobserved
arelikeQ2,whichrequiregoingbeyondpassivelypredictingthe confounders.Thisisnotthecase.Figure2(b)showshowobserved
throughputisdependentonthesizeofchunksowingtoTCPbe-
1Availableathttps://github.com/Purdue-ISL/Veritas havior[11,29,50].Figure2(b)showsthedistributionofthroughput
740

ACMSIGCOMM’23,September10–14,2023,NewYork,NY,USA ChandanBothra∗,JianfeiGao∗,SanjayRao,andBrunoRibeiro
4
2
0
lt
0.02 0.02-0.04 0.04-0.10 0.1-1.0 1.0-2.0 2.0-4.2
(a)Chunksizes(MB)
daolnwodlautcA
)s(emit 15
10
5
0 1 2 3 4 5 6 7 8 9101112
(b)log Size(KB) 2
)spbM(tuphguorhT
1.00
0.75
0.50
0.25
0.00 0.0 0.1
Rebufratio
Figure 2: (a) Distribution of download times for different
groupsofchunksizeswiththeMPCalgorithmonasubsetof
FCCtraces.(b)Observedthroughputvarieswithpayloadsize
inthesameTCPsessionalthoughthebandwidthemulated
isthesame.
forpayloadsinagivensizerangeincontrolledexperimentsus-
ingTCPwhereweemulatedaconstantnetworkbandwidthof18
Mbps.Theexperimentsinvolvedsendingpayloadsofvaryingsizes
(2KBto4MB)inthesameTCPsession.Thegraphshowsthatfor
smallsizes(lessthanthebandwidthdelayproductofthenetwork),
throughputismuchsmaller,whileitisclosertotheintrinsicnet-
workbandwidthforlargersizes.Thus,simplyusingthethroughput
observedinlogsinatrace-drivensimulationisinadequateasit
maynotaccuratelyreflecttheperformanceifadifferentsizehad
beenchosen.
2.3 Whynotactivelyinterveneonliveusers?
Ratherthanmakingpredictionsbypassivelyobservingasystem,
RandomizedControlTrials(RCTs),A/BTesting,andReinforcement
Learning (RL) [44] can evaluate the impact of a design change
byactivelyintervening(changing)thesystem,andobservingthe
performance. While these approaches are valuable, they must
beusedjudicioulsyasactiveinterventionmayleadtodegraded
performancetosomeviewers.Inpractice,A/Btestingistypically
usedinaconservativefashiononlyafteraninitialofflineanalysis
approachindicatesthedesignchangehassufficientpotential.
RLmaybeviewedasasequentialRCTinthattheagentdynami-
callylearnsthebestdecisionstotakeateachstateofthesystem.A
drawbackofRCTsingeneral,andRLinparticular,isthatitonly
answersthequestionforpre-defineddecisions.Ifoursetofpossi-
bledecisionschanges,theRCT/RLalgorithmsmustberunagain.
Further,bothRCTsandRLcannotdirectlyanswercounterfactual
queries,althoughtheirrandomized(exploration)measurements
maystillbeusedbycounterfactualestimatorsinsomespecialcases
(e.g.,[10]).Forinstance,imagineseeingrarenetworkconditions
whereadeployedalgorithmperformedpoorly.RCTsandRLare
generallynotapplicableinthisscenariosincetheeventisinthe
past,andanyRCTtotestanewinterventiononthesystemcan
onlybeappliedinfuturesessions(wheretherareeventmaybe
difficulttoreproduce).
2.4 Recentworkandlimitations.
Aparallelwork,CausalSim[8],supportscausalqueriesbutrequires
atrainingphasewhereeachof𝑁 sessionsisassignedtooneof
snoissesfonoitroporP
1.00
Ground
Truth 0.75
CausalSim
0.50 (RCT)
CausalSim 0.25 (NoRCT)
0.00 0.0 0.1 0.2
Rebufratio
(a)ChangeofABRalgorithm:CausalSim
performspoorlywithoutRCTtraining
data.
snoissesfonoitroporP
Ground
Truth
CausalSim (RCT)
(b)Increaseinvideoquality.CausalSim
performspoorlyasitislimitedbythe
scopeofRCT.
Figure3:LimitationsofCausalSim.
manyABRpoliciescompletelyatrandom(RCTtraces).Whilea
goodadvance,therearetwocruciallimitationsofCausalSim.
First,theapproachinherentlyrequirestrainingdatausingRCTs.
Tobetterunderstandthisrequirement,considerthatwearegiven
tracesfromtheMPCalgorithm[35],andwewouldliketounder-
stand the performance if we moved to the BBA algorithm [20].
Figure3(a)presentstherebufferingratios(ratioofstallinasession
tototaldurationofthesession)seenwithCausalSiminsucha
setting(§4providesdetailsoftheevaluationmethodology).Clearly,
therebufferingratiopredictedbyCausalSim(NoRCT)incorrectly
hasasharptail.Incontrast,iftwodifferentalgorithms(MPCand
Bola[41])wereassignedtosessionsusinganRCT,andthenCausal-
Simweretrainedusingdatacollectedfrombothalgorithms,the
accuracyinpredictingrebufferingwithBBAisfarimprovedand
closertoGroundTruth.DeployingABRalgorithmsusingRCTto
collecttracescanimpacttheperformanceofreal-worldusersas
discussedearlierandsuchdatamaynotalwaysbeavailable.
Second,CausalSimcanfailout-of-distribution,wherenewac-
tionsareavailableoutsidethescopeoftheinitialRCTexperiment
(e.g.,whatiftheABRnowallowedhighervideoqualities,orifwe
usedadifferentbuffersize).ConsiderCausalSimtrainedondata
fromtwoABRalgorithms:MPCandBBA,buteachdeployedwith
asmallsetofvideoqualities.Now,letsassumeweareinterested
inevaluatingperformanceifhigherqualitieswereusedwithBBA.
Figure3(b)showsthatinsuchscenario,CausalSimrebufferingratio
predictionsarefarfromGroundTruth.ThisisbecauseCausalSim
wastrainedwithdatawherevideoqualitylooksindependentof
rebufferingratios,sinceforlowqualitiesthebandwidthwassuffi-
cienttoavoidrebufferingevents.Unfortunately,thisassociationis
incorrectforhigherqualities,wherethebandwidthisnowinade-
quate(asshownbytheGroundTruthinFigure3(b)).Veritascausal
inferencewillnotbeimpactedbythislackofassociation.
3 VERITAS:ACAUSALINFERENCE
FRAMEWORKFORVIDEOSTREAMING
ThissectionpresentsVeritas,ourframeworkforansweringcausal
queriesinvideostreaming.§3.1presentsthecausalgraph(DAG)
inFigure4,whichmodelsthevariablesinvolvedinvideostream-
ingandtheircausalrelationships.UsingtheDAGinFigure4we
choosevariablesthatblockthecascadingdependenciestopropose
anefficient(andtheoreticallysound)abductionprocedurein§3.2.
741

Veritas:AnsweringCausalQueriesfromVideoStreamingTraces ACMSIGCOMM’23,September10–14,2023,NewYork,NY,USA
|     |     |     |     | ,...,Csn+1 |     | Cen−1−1 | ,...,C sn−1+1 |     |     |     |     |     |     |
| --- | --- | --- | --- | ---------- | --- | ------- | ------------- | --- | --- | --- | --- | --- | --- |
Cen−1
d-separatespastandfuture
Figure4:Causalmodelof(embedded)dependenciesinvideostreaming,startingat𝑒 𝑛−1(whenthe(𝑛−1)-thchunkfinishes
download),until𝑒 𝑛,(whenthe𝑛-thchunkfinishes).Shadedgrayvariablesareobserved,whilewhite(unshaded)variablesare
hidden.RedcontourshowskeyvariablesfordefiningourMarkovprocess.
Finally,§3.3discusseshowVeritasputsallthesemethodstogether tonotethatthevariables𝐶 ,𝑊 ,𝐵 alsoevolveinthetimebe-
|     |     |     |     |     |     |     |     |     |     | 1:𝑇 1:𝑇 1:𝑇 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
toperformcounterfactualandinterventionalinference. tweenthesechunkevents,butforanytime𝑡 ∈{1,...,𝑇}\{S∪E}
thathappensbetweenchunkstartandendtimes,therandomvari-
3.1 Causaldependenciesinvideostreaming ables𝐵 dependsonlyon𝐵 𝑡−1 (justthevideobeingplayed)and𝐶
|     |     |     |     |     |     |     | 𝑡              |     |       |                |     |      | 𝑡   |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | -------------- | --- | ---- | --- |
|     |     |     |     |     |     |     | dependsonlyon𝐶 |     | ,but𝑊 | dependsonboth𝑊 |     | and𝐶 | if  |
Akeyfactorthatimpactsthedecisionsmadebyavideostreaming 𝑡−1 𝑡 𝑡−1 𝑡−1
|     |     |     |     |     |     |     | thereisanactivechunkdownloadattime𝑡 |     |     |     | (andonlyon𝑊 |     | if  |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | ----------- | --- | --- |
algorithmistheintrinsicnetworkbandwidth(INB).Figure4shows 𝑡−1
thereisnoactivedownload).
adirectedacyclicgraph(DAG)describingthecausaldependencies
|     |     |     |     |     |     |     | The𝑛-thchunksize𝑆 |     | 𝑛 isinfluenced(throughtheABRalgorithm) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------------------------------------- | --- | --- | --- | --- |
forvideostreaming.Figure4describestheevolutionofINBasa
|                                                        |     |     |     |     |                  |     | byboththebufferstate𝐵         |     |     | 𝑠𝑛 atthestartofdownloadofchunk𝑛 |                     |     |        |
| ------------------------------------------------------ | --- | --- | --- | --- | ---------------- | --- | ----------------------------- | --- | --- | ------------------------------- | ------------------- | --- | ------ |
| discreteprocessoverdiscretetimeintervals𝑡              |     |     |     |     | ∈ {1,...,𝑇}(each |     |                               |     |     |                                 |                     |     |        |
|                                                        |     |     |     |     |                  |     | andthelastobservedthroughput𝑌 |     |     |                                 | .Thechunksizevalue𝑆 |     |        |
| ofwall-clocktimelengthof𝛿),withtheINBwithinaninterval  |     |     |     |     |                  |     |                               |     |     | 𝑛−1                             |                     |     | 𝑛      |
|                                                        |     |     |     |     |                  |     | influencesthedownloadtime𝐷    |     |     | .Further,theTCPstate𝑊           |                     |     | (which |
| assumedconstant.Timeisassumedtobediscretetosimplifyour |     |     |     |     |                  |     |                               |     |     | 𝑛                               |                     | 𝑠𝑛  |        |
includestheinitialcongestionwindowandRTT)alongwith𝑆
𝑛
approach,since𝛿canbeasfine-grainedasnecessary.
|                                                |     |     |     |     |     |     | and𝐶 𝑠𝑛 ,...,𝐶 | 𝑒𝑛  | alsoinfluencethedownloadtime𝐷 |     |     | 𝑛 .𝑊 𝑠𝑛 | itself |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------------------------- | --- | --- | ------- | ------ |
| Thesessiondownloadsaseriesofchunks1...𝑁.Chunk𝑛 |     |     |     |     |     | ∈   |                |     |                               |     |     |         |        |
potentiallydependsonthebufferattheendofthepreviouschunk
| {1,...,𝑁}startsdownloadingattime𝑠 |      |                                            |     | ∈{1,...,𝑇}andfinishes |     |     |                                                      |     |     |     |     |     |     |
| --------------------------------- | ---- | ------------------------------------------ | --- | --------------------- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                                   |      |                                            |     | 𝑛                     |     |     | 𝐵 ,asthisdeterminestheidletimebetweenchunkdownloads, |     |     |     |     |     |     |
| attime𝑒                           | ∈ {𝑠 | ,...,𝑇}.Thevariablesthatevolveovertimeare: |     |                       |     |     | 𝑒 𝑛 −1                                               |     |     |     |     |     |     |
𝑛 𝑛 th a t canimpactTCPstateforsomeimplementations.Finally,as
| (i)𝐶 | C,theaverageINBintimeinterval((𝑡 |     |     |     | −1)𝛿,𝑡𝛿];(ii)𝐵 | ,   |                 |     |      |                    |     |     |     |
| ---- | -------------------------------- | --- | --- | --- | -------------- | --- | --------------- | --- | ---- | ------------------ | --- | --- | --- |
| 𝑡 ∈  |                                  |     |     |     |                | 𝑡   | discussedabove𝑆 |     | and𝐷 | togetherdetermine𝑌 |     | .   |     |
theamountofbufferinthevideoplayerattime𝑡 ∈{1,...,𝑇},and 𝑛 𝑛 𝑛
|     |     |     |     |     |     |     | Confounders:TheDAGinFigure4showsthat𝐶 |     |     |     | 1:𝑇 | areconfounder |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | ------------- | --- |
(iii)𝑊 𝑡 ,theTCPstateattime𝑡.TheTCPstateincludesparameters
|     |     |     |     |     |     |     | variablesbetween𝑆 |     | 1:𝑁 ,𝐷 | 1:𝑁 ,and𝑊 𝑠1:𝑁 .Confoundersarevariables |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------ | --------------------------------------- | --- | --- | --- |
suchasthecongestionwindow,RTTandminRTT.
(oftennotavailableinthedata)thatcausespuriousassociations
Thevariablesthatevolveateachchunkrequestare:(i)thesize
betweenmultipleobservedvariables.Moreover,wemakethesimpli-
| (𝑆 )ofthe𝑛-threquestedchunkand(ii)𝐷                |     |     |     |     | ,itsdownloadtime, |     |                      |     |      |                                    |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | ----------------- | --- | -------------------- | --- | ---- | ---------------------------------- | --- | --- | --- |
| 𝑛                                                  |     |     |     |     | 𝑛                 |     | fyingassumptionthat𝐶 |     |      | arenotinfluencedbyanyothervariable |     |     |     |
| 𝑛=1,...,𝑁.Thethroughputobservedduringthedownload(𝑌 |     |     |     |     |                   | )   |                      |     | 1 :𝑇 |                                    |     |     |     |
𝑛
|                       |     |        |     |     |     |     | inthemodel(thatis,c |     | h unkdownloadsdonotimpacttheINB). |     |     |     |     |
| --------------------- | --- | ------ | --- | --- | --- | --- | ------------------- | --- | --------------------------------- | --- | --- | --- | --- |
| canbecalculatedusing𝑆 |     | 𝑛 and𝐷 | 𝑛 . |     |     |     |                     |     |                                   |     |     |     |     |
VeritascurrentassumeswearerunningaparticularversionofTCP
| Henceforth,foranyrandomvariable𝑋 |     |     |     | wedefinethesequences |     |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(e.g.,Cubic,orBBR)andcurrentlydoesnotaddresstheimpactof
| 𝑋 : = | ( 𝑋 , . . | ., 𝑋 𝑏) a nd 𝑋 | : = | ( 𝑋 , . . | . ,𝑋 ). Mo r e o | v e r , l et |     |     |     |     |     |     |     |
| ----- | --------- | -------------- | --- | --------- | ---------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
𝑎 :𝑏 𝑎 𝑠𝑎 : 𝑏 𝑠𝑎 𝑠 𝑏 what-ifquestionswheretheTCPversionitselfchanges.
| 𝑁          | 𝑠 a   | n d 𝑁     | 𝑒 b   | et h e s e t | o f ra n d om v a r ia | b l e s o f |     |     |     |     |     |     |     |
| ---------- | ----- | --------- | ----- | ------------ | ---------------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| S = ∪ 𝑛 =1 | { 𝑛 } | E = ∪ 𝑛 1 | { 𝑛 } |              |                        |             |     |     |     |     |     |     |     |
=
showingthediscretetimeswhereachunkstartsandendsdown- 3.2 Veritasabductionforcausalqueries
| loading,respectively.Weassumethatthevariablesin𝑊 |     |                                       |     |     | 𝑠1:𝑁 | ,𝐵 𝑠1:𝑁 , |                                                    |     |     |     |     |     |         |
| ------------------------------------------------ | --- | ------------------------------------- | --- | --- | ---- | --------- | -------------------------------------------------- | --- | --- | --- | --- | --- | ------- |
|                                                  |     |                                       |     |     |      |           | Sincenoothervariablesaffecttheconfoundervariables𝐶 |     |     |     |     |     | 1:𝑇 but |
| 𝑆 ,S,Eand𝑌                                       |     | (showninshadedgrayinFigure4)aregener- |     |     |      |           |                                                    |     |     |     |     |     |         |
1:𝑁 1:𝑁 𝐶 1:𝑇 directlyorindirectlyaffectallothervariables(i.e.,allother
allyobservedvariablesinvideostreamingsessions(thatis,allthe
|     |     |     |     |     |     |     | variablesaredescendantsofsomevariablein𝐶 |     |     |     |     | ),ifwecouldinfer |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | ---------------- | --- |
informationregardingthemiseitherdirectlyavailable,orcanbe 1:𝑇
|                                                          |     |     |     |     |     |     | 𝐶 wewouldbeabletohandleanycounterfactualorinterven- |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| calculatedfromthedata).NotethatTCPstateinformationiseasy |     |     |     |     |     |     | 1:𝑇                                                 |     |     |     |     |     |     |
|                                                          |     |     |     |     |     |     | tionalqueryneeded.Thisproceduretoinferaconfounder(𝐶 |     |     |     |     |     | )   |
1:𝑇
tocollect(e.g,usingthetcp_infostructureinLinuxsystems[6]). torespondtocausalqueriesisknownasabduction[34,Section
Further,althoughwecouldcollecttheinformation,wedonotre-
4.2.4].Abductioninvolves(i)“inverting”theobservedvariablesto
| quirethevalues{𝑊 |     | 𝑡}𝑡∈{1,...,𝑇}\S | ,{𝐵 | 𝑡}𝑡∈{1,...,𝑇}\S | ,andtreatthese |     |     |     |     |     |     |     |     |
| ---------------- | --- | --------------- | --- | --------------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
getthehiddenconfounders;and(ii)thenmodelingtheproposed
variablesashidden.
changes(assumingthehiddenconfoundervaluesarenowknown)
| Note | that Figure | 4 only | illustrates | the | embedded process | of  |     |     |     |     |     |     |     |
| ---- | ----------- | ------ | ----------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
toreturntheanswertothewhat-ifquery.Abductionapproachesin
{𝐶 𝑡}𝑡∈S∪E ,{𝑊 𝑡}𝑡∈S∪E ,and{𝐵 𝑡}𝑡∈S∪E ,attheeventtimeswhere MLtypicallyrelyoncomposablestatisticalmodelsusinghigh-level
anewchunkisrequestedorfinishesdownloading.Itisimportant
programminglanguages[12,14,30],anddonoteffectivelydeal
742

ChandanBothra∗,JianfeiGao∗,SanjayRao,andBrunoRibeiro
ACMSIGCOMM’23,September10–14,2023,NewYork,NY,USA
withtheuseof“if”statementsanddeterministicdecisionfunctions modelforitsemissions.ThemodelcaptureshowINB,chunksizes,
commoninnetworking.Hence,weproposeacustomabduction andTCPstatesgetstranslatedintoobservedthroughput.
methodtailoredtoourtask. Second,intraditionalHMMs,eachhiddenstateisassociated
Thetask:Inoursetting,abductionrequiressamplingthenetwork withasingleobservation.However,inourcontext,observations
INBgivenalltheobservationsinasession: areonlyassociatedwiththosehiddenINBstateswherechunksare
beingdownloaded.ButthehiddenINBitselfstillchangesduring
| 𝐶 ∼𝑃(𝐶 | =𝑐  | 1:𝑇|⟨AllObservedVariables⟩), |     | (1) |     |     |     |     |
| ------ | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
1:𝑇 1:𝑇 theoffperiods(withouchunkdownloads)andnoobservationsare
where𝐶 ∼𝑃(𝐶 =𝑐|𝐻 =ℎ)meansrandomvariable𝐶 issampled availableduringtheseintervals.Further,itispossiblethatthereare
fromitsdistributionconditionedonobserving𝐻 ℎ.Oncethe multiplechunksdownloadedinthesametimeinterval((𝑡−1)𝛿,𝑡𝛿],
=
| confoundingvariables𝐶 |     | aresampledgiventheobservables,ab- |     |     |     |     |     |     |
| --------------------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
1:𝑇 𝑡 ∈ {1,...,𝑇}. To handle this, Veritas’s HoEHMM allows each
ductionallowsustosimulatetheeffectofthecausalqueryover INB state to be associated with zero, one or more observations
thesampled𝐶 (nowassumedknown).WediscusshowVeritas (correspondingtothenumberofchunksdownloadedinthecor-
1:𝑇
achievesthisnext. respondinginterval).Veritas’sHoEHMMisconsistentwithprior
work[7,43],whichhasmodeledTCPthroughputevolutionasa
| Veritas’s High-order |     | Embedded | Hidden | Markov |     |     |     |     |
| -------------------- | --- | -------- | ------ | ------ | --- | --- | --- | --- |
Model(HoEHMM).SamplingtheINBtimeseriesasdescribedin
Markovprocess,butVeritasaddressessignificantcomplexitiesasso-
Equation(1)isnon-trivial.HiddenMarkovModels(HMMs)[48]are ciatedwithembeddingacustomemissionprocess,and𝑑-separation.
commonlyusedtosampletimeseries,butstandardHMMswould Further,ourfocusisonabductionforcausalinference.
requiretheemission𝑌 tobeonlydependonasinglehiddenvari- HiddenstatetransitionsofVeritas’sHoEHMM.InFigure4,
𝑛
| able(say,𝐶 ).Unfortunately,𝑌 |     | intheDAGofFigure4depends |     |     |     |     |     |     |
| ---------------------------- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
𝑠𝑛 𝑛 only𝑆 𝑛 ,𝑊 𝑠𝑛 and𝐶 𝑒𝑛:𝑠𝑛 affect𝑌 𝑛 .Since𝐵 ℎ ,𝑆 ℎ and𝑊 𝑠ℎ areobserved
onalargesetofvariables.
foranyℎ,1 ≤ ℎ ≤ 𝑁,wenowonlyneedtofocusonthetransi-
E x te n d i n g H M M s :F u n d a m e nt a l ly ,H M M s r e li e s o n t h e co n ce p t o f t io n p r o b a bi li ti e s 𝑃 ( 𝐶 | 𝐶 ) . O u rm o d e l a ss u m e s
|     |     |     |     |     |     | (𝑠 𝑛 + 1 − 1 ) :𝑠 𝑛 | (𝑠𝑛 − 1) :𝑠 𝑛− 1 |     |
| --- | --- | --- | --- | --- | --- | ------------------- | ---------------- | --- |
d-s ep a r a ti o n t o av o id c a sc a d in g t e m p or al de p e n d e n c ie s . A su ffi c i en t a t im e - h o m o g e n e o u s fi r s t - o r d e r M a rk o v p r o c e ss 𝑃( 𝐶 |𝐶 ) =
𝑡 + 1 1 :𝑡
conditionforaset𝑈 ofrandomvariablesto𝑑-separateaset𝐴and 𝑃(𝐶 𝑡+1|𝐶 𝑡),1 𝑡 𝑇,where𝐶 denotestheaverageINBdur-
|     |     |     |     |     | ≤ ≤ |     | 𝑡   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝐵isthatallundirectedpathsintheDAGbetween𝐴and𝐵include
ingtimeinterval((𝑡−1)𝛿,𝑡𝛿](see§3.1fordetails).Forinstance,
atleastonevariablefrom𝑈,andnosuchpathshavearrowscollide
𝜖 =0.5impliesthatthehiddenstatesareC={0.0Mbps,0.5Mbps,
“head-to-head”inthevariablesin𝑈 [34,Definition1.2.3].Oneof 1.0Mbps,...}.Bothhyperparameters𝛿 and𝜖 canbeassmallas
thechallengingaspectsofVeritasisthat𝐶 𝑠𝑛 doesnotd-separate desiredifcomputationallyfeasible.Theconditionaldistribution
𝑌 and𝑌 𝑛−1,...,𝑌1 intheDAGofFigure4,whichthencreates 𝑃(𝐶 𝑡|𝐶 𝑡−1)isgivenbythetransitionprobabilitymatrix
𝑛
| cascadingdependenciesbetween𝑌 |     | andallothervariablesattime |     |     |        |               |         |     |
| ----------------------------- | --- | -------------------------- | --- | --- | ------ | ------------- | ------- | --- |
|                               |     | 𝑛                          |     |     | 𝐴 =𝑃(𝐶 | 𝑗𝜖|𝐶 𝑡−1=𝑖𝜖), | 1<𝑡 ≤𝑇, | (2) |
steps𝑒 ,...,𝑠 ,...,𝑒1,...,𝑠1 .IfwewanttocreateaMarkovmodel 𝑖,𝑗 𝑡 =
| 𝑛 𝑛 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
forVeritas,wemustachieved-separation.Forthis,Veritas’sMarkov wheretheprior𝑃(𝐶1)isalsoahyperparameterofourmodel(as-
chainisdefinedoveranextendedvariable-dimensionalsetofstates. sumeduniforminourexperiments).
InspectingtheDAGinFigure4,wecanseethat𝐶 ,𝑊 ,𝐵 , Parameterizedhiddenstatetransitionmatrix.Inourmodel,
|     |     |     | 𝑠𝑛  | 𝑠𝑛 𝑠𝑛 |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- |
and𝑆 ,circledinred,blockanyundirectedpathsbetween𝑌 and practitionerscandefinecustomparameterizedstatetransitionmod-
| 𝑛                         |     |                           |     | 𝑛   |     |     |     |     |
| ------------------------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
| {𝑌 𝑛−1,...,𝑌1}.Moreover,𝑌 |     | alsodependsonthesequence𝐶 |     | ,   |     |     |     |     |
𝑛 𝑠𝑛:𝑒𝑛 elsviaPytorch[5]differentiableparameters(henceforthdenoted
whichhasvariablesize.
𝜃).Forinstance,afullyflexibletransitionmodelcanbedefinedas
WenowdefineVeritas’sHigh-orderEmbeddedHiddenMarkov 𝐴 =𝜃 .Ourexperimentsconsiderthefollowingparameterized
𝑖,𝑗 𝑖,𝑗
Model(HoEHMM),characterizedby(i)asetofvariable-dimensional transitionmatrix:
| high-order |     | hidden |     | states |     |       | 1(𝑗−𝑖)2(cid:19) |     |
| ---------- | --- | ------ | --- | ------ | --- | ----- | --------------- | --- |
|            |     |        |     |        |     | (1−𝜂) | (cid:18)        |     |
{(𝐶 ,𝐵 ,𝑆 ,𝑊 𝑁 ;(ii)amatrixthatcapturesthetran- 𝐴 𝑖,𝑗(𝜃)= exp − +𝜂, (3)
| (𝑠𝑛:𝑠𝑛+1−1)                                                | 𝑠𝑛 𝑛 𝑠𝑛 )} | 𝑛 =1 |     |     |     | 𝑍   | 2 𝜃2 |     |
| ---------------------------------------------------------- | ---------- | ---- | --- | --- | --- | --- | ---- | --- |
| sitionprobabilitiesfromonehiddenstatetoanother;(iii)asetof |            |      |     |     |     | 𝑖   |      |     |
where𝜃2 > 0isthelearnablevarianceofazero-meanGaussian
| observations(which | wewill | definelater); | (iv) asetof | emission |     |     |     |     |
| ------------------ | ------ | ------------- | ----------- | -------- | --- | --- | --- | --- |
probabilitiesfor {𝑌 ,...,𝑌1},whichcapturethelikelihoodofa distribution,𝜂 ∈ [0,1)isasmoothinghyperparameter,and𝑍 𝑖 is
𝑁
particularobservationbeinggeneratedfromagivenhiddenstate; normalizationfactorensuringthat(cid:205) 𝑗 𝐴 𝑖,𝑗 =1.Inallexperiments,
and(v)aninitialprobabilitydistributionoverthestates. weuseafixedsmoothing𝜂 =0.05.
Creating a hidden Markov model of the evolution of Domain-specificemissionmodel.Thethroughput𝑌 observed
𝑛
𝑁
{( 𝐶 𝑠 𝑛: 𝑠 1 , 𝐵 𝑠 ,𝑆 𝑛 , 𝑊 𝑠𝑛 )} w o u l d b e u n n e c es s a r il y c o m p l e x . b y v i de o ch u n k 𝑛 w it h s ta r t ti m e 𝑠 𝑛 a n d e n d ti m e 𝑒 𝑛 i s a f un c ti o n
| ( 𝑛 + 1 − ) | 𝑛   | 𝑛 = 1 |     |     |     |     |     |     |
| ----------- | --- | ----- | --- | --- | --- | --- | --- | --- |
T h a n k f u l l y , w e c a n t a m e th is c om p l e x it y t h ro u g h p a r t i al o b se r v a - o fI N B 𝐶 𝑠𝑛 :𝑒 ,c h un k s iz e 𝑆 𝑛 a n d th es t a rt in g T C P s t at e 𝑊 𝑠 w h i c h
|     |     |     |     |     | 𝑛   |     |     | 𝑛   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
tions.Specifically,weobserve{(𝐵 ,𝑆 ,𝑊 )} 𝑁 .Buffersize𝐵 includescongestionwindow𝑊 c wndandminimumRTT𝑊 m inRTT.
|     |     | 𝑠𝑛 𝑛 | 𝑠𝑛 𝑛 =1 | 𝑠𝑛  |     | 𝑠 𝑛 |     | 𝑠 𝑛 |
| --- | --- | ---- | ------- | --- | --- | --- | --- | --- |
andchunksize𝑆 arecommonobservationsinvideostreaming. WedevelopasimpleTCPmodel(Algorithm4intheAppendix)
𝑛
ObservingTCPstateatthestartofachunkrequest𝑊 ,whilenot denotedby𝑓 toestimate𝑌 .Themodelisbasedonthefollowing
|     |     |     | 𝑠𝑛  |     |     | 𝑛   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
ascommon,hasprecedentintheliterature[50],andiskeytotame insight:theobservedthroughputmatchesINBifchunksizesare
temporaldependencies. sufficientlylarge,andtransmissionisnotlimitedbycwnd.However,
Veritas’sHoEHMMalsodepartsfromstandardHMMmodelsin throughputisloweriflimitedbysizeorcwnd.
otherways.First,HMMstraditionallyusecommonparameterized Inmoredetail,wefirstcalculatetheBandwidthDelayProduct
probability distributions (e.g., multinomial, Gaussian) to model (BDP)usingtheINB,𝐶 and𝑊 m inRTT.Ifboth𝑊 c wndand𝑆 ,are
|     |     |     |     |     |     | 𝑠𝑛:𝑒𝑛 | 𝑠 𝑠 | 𝑛   |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- |
|     |     |     |     |     |     |       | 𝑛 𝑛 |     |
emissionprobabilities.Instead,Veritasembedsadomain-specific largerthantheBDP,𝑌 𝑛 isclosetotheintrinsicnetworkbandwidth,
743

Veritas:AnsweringCausalQueriesfromVideoStreamingTraces ACMSIGCOMM’23,September10–14,2023,NewYork,NY,USA
Real Time
Capacity
Transitions
Downloading
Chunks
Capacity-of-Chunk
Transitions
Figure5:HowINBinrealtimemapstocapacityofdownloadedchunks.INBevolvesevery𝛿timeunits(topline).𝐶
𝑡 isconstant
ininterval[(𝑡−1)𝛿,𝑡𝛿).Themiddle(green)linesshowfivechunkdownloads.TheevolutionoftheMarkovchain(asafunction
oftimestepsΔ 𝑛)isshownatthebottomunderthearrows.Forinstance,chunks2and3startinthesametimewindow,hence
| Δ 3=0.Chunks4and5startinwindows3and5respectively,henceΔ |     |     |     |                       |     |          | 5=2. |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --------------------- | --- | -------- | ---- | --- | --- | --- | --- |
| INB.However,if𝑊cwndislargebut𝑆                          |     |     |     | issmallerthanBDP,then |     |          |      |     |     |     |     |
|                                                         |     | 𝑠𝑛  |     | 𝑛                     |     |          |      |     |     |     |     |
| ourTCPconnectionissize-limitedand𝑌                      |     |     |     | iscloseto𝑆            | 𝑛/𝑊 | m inRTT. |      |     |     |     |     |
|                                                         |     |     |     | 𝑛                     |     | 𝑠 𝑛      |      |     |     |     |     |
Whenthroughputislimitedbycwnd(𝑊cwndissmallerthanBDP),
𝑠𝑛
wecalculatethenumberoftransmissionroundsneededtotransmit
| size𝑆   | 𝑛 andestimate𝑌 | 𝑛                                     | usingthenumberoftransmissionrounds, |     |     |     |     |     |     |     |     |
| ------- | -------------- | ------------------------------------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 𝑊minRTT | and𝑆           | .Weusealinearincreasetomodelthegrowth |                                     |     |     |     |     |     |     |     |     |
| 𝑠𝑛      |                | 𝑛                                     |                                     |     |     |     |     |     |     |     |     |
of𝑊cwnd
𝑠𝑛 acrossrounds.AlthoughthissimplifiesTCPbehavior,
wepreferredthisapproachsinceitismoregenericacrossconges-
| tioncontrolalgorithmsandbecauseVeritastolerateserrorin |     |     |     |     |     | 𝑓   |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(asdiscussedbelow).Further,eventhissimpleapproachproduces
promisingempiricalresults(§4).Wehaveextensivelyexperimented
withalternate𝑓 functionswhichindicatedthatwhileitisimportant Figure6:UsingVeritasforcounterfactualqueries.
tomodeltheimpactonthroughputwithlowcwnd,theperformance
waslesssensitivetohowchangesincwndwithinachunkdown- methods[15,37,39].Thesamplingrequirescomputingthejoint
loadweremodeled.Finally,𝑓 isahyper-parameterforVeritas,and probability𝑃(𝐶 =𝑖𝜖,𝐶 𝑗𝜖(cid:12) 𝑌 ,𝑊 ,𝑆 1:𝑁),whichweob-
|     |     |     |     |     |     |     |     | 𝑠𝑛  | 𝑠𝑛+1 = (cid:12) 1:𝑁 | 𝑠1:𝑁 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | ---- | --- |
custom𝑓 functionsthatcapturedetailsofspecificTCPalgorithms tainfromourvariantoftheBaum-Welchforward-backwardalgo-
canbeeasilyincorporated(althoughthismayrequireloggingmore rithm(seeAlgorithm1intheAppendix)andAlgorithm3inthe
TCPstateinformation(e.g.,ssthresh,timesincelastlossevent,etc.). Appendixpresentsthecompletesamplingalgorithmfor𝐶 1:𝑇 .Itis
If𝑓 weretoperfectlymodelTCPbehaviorwecoulddefinethe dividedintotwosteps.First,wesample𝐶 .Then,wesamplethe
𝑠1:𝑁
emissionprobabilitydistributionas intermediatevalues𝐶 ,where𝑡 𝑁 {𝑠 𝑛−1+1,𝑠 𝑛−1}according
|     |                      |                       |                        |       |            |     |             | 𝑡                       | ∈∪ 𝑛 =2                 |                 |                  |
| --- | -------------------- | --------------------- | ---------------------- | ----- | ---------- | --- | ----------- | ----------------------- | ----------------------- | --------------- | ---------------- |
|     |                      |                       |                        |       |            |     | t o tr a n  | s it io n m a tr ix 𝐴 b | as e d o n c h u n k    | sa m p le s𝐶    | . N o t e thatit |
|     | 𝑃(cid:0)𝑌 =𝑦(cid:12) |                       | (cid:1) =1{𝑦=𝑓(cid:0)𝐶 |       | (cid:1)},  |     |             |                         |                         | 𝑠               |                  |
|     | 𝑛                    | (cid:12) 𝑊 𝑠𝑛 ,𝑆 𝑛 ,𝐶 | 𝑠𝑛:𝑒𝑛                  | 𝑠𝑛:𝑒𝑛 | ,𝑊 𝑠𝑛 ,𝑆 𝑛 | (4) |             |                         |                         | 1: 𝑁            |                  |
|     |                      |                       |                        |       |            |     | is p o s si | b le t o sa m p le IN   | B v a lu e s b e y o nd | t im e 𝑇 if n e | c e ss a r y.    |
where1{}istheindicatorfunction.SinceourTCPmodelisimper-
fect,weadduncertaintyintheformofGaussianwhitenoisewitha
learnablevariance.Inourexperimentsweuseahighervariancefor
|     |     |     |     |     |     |     | 3.3 | HowVeritasanswerscausalqueries |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- |
thefirstfewchunkstomodelTCPslowstarteffectsatthestartof
thesession.PleaserefertoEquation(5)intheAppendixforfurther Figure6showshowVeritasmaybeusedtoanswercounterfactual
details. andinterventionalqueries.Thesystemdeployedinthewild(Setting
EvolutionoftheembeddedINB.Wenowdiscusshowtoestimate A)produceslogswhichforeachchunk,whichincludes(i)size;(ii)
hiddenstates𝐶 usinganembeddedMarkovchain.Ourembed- starttimeofdownload;(iii)endtimeofdownload;and(iv)TCP
1:𝑇
dingisinspiredbytheembeddinginNealetal.[31](seeFigure5). stateincludingcwnd,minRTT,andRTT[6]atthestartofeach
(cid:12)
| Moreprecisely,for𝑡 |     | ∈{1,...,𝑇},insteadofmodeling𝑃(cid:0)𝐶 |     |     |     | 𝑡 𝐶 𝑡−1 (cid:1), | download. |     |     |     |     |
| ------------------ | --- | ------------------------------------- | --- | --- | --- | ---------------- | --------- | --- | --- | --- | --- |
(cid:12)
w e m o d e l th e t r a n s i t i o n s 𝑃 (cid:0) 𝐶 (cid:12) 𝐶 (cid:1) , w h e r e 1 < 𝑛 ≤ 𝑁 . F o r V e r i t a s p e r f o r m s th e a b d u c t io n s te p b y s a m p l in g 𝐾 l i k e l y I N B
𝑠 𝑛 (cid:12) 𝑠 𝑛 1
(cid:0) − (cid:12) (cid:1) Δ s e q u e n c e s 𝐶 ( E q ua ti o n ( 1) ) a s d e s c r i b e d e a r l i e r . T h e c o u n t er f a c -
| ch u n | k s 𝑛 − 1 a n | d 𝑛 , w e w i | ll d efi n e 𝑃 𝐶 𝑠 | = 𝑗𝜖 (cid:12) 𝐶 𝑠 | = 𝑖 𝜖 = (𝐴 | 𝑛 )𝑖 ,𝑗 , |     | 1 :𝑇 |     |     |     |
| ------ | ------------- | ------------- | ------------------ | ----------------- | ---------- | --------- | --- | ---- | --- | --- | --- |
𝑛 𝑛 − 1 tu a l q u e r y is a v i d e o s e s s i o n e m u l a te d w i th t h e n e w S e tti n g B u s i n g
| w h e r                                                | e Δ 𝑛 = 𝑠 𝑛 | − 𝑠 𝑛 1 a | n d 𝐴 i s a s d e fi | n e d in E q u | at i o n (2 ) . |     |                      |     |                                |     |     |
| ------------------------------------------------------ | ----------- | --------- | -------------------- | -------------- | --------------- | --- | -------------------- | --- | ------------------------------ | --- | --- |
|                                                        |             | −         |                      |                |                 |     | thesampledINBtraces𝐶 |     | (e.g.,SettingBmaycorrespondtoa |     |     |
| LearningVeritas’sHoEHMM.Finally,thealgorithmtolearnthe |             |           |                      |                |                 |     |                      |     | 1:𝑇                            |     |     |
modelparametersisavariationoftheBaum-Welchalgorithm[36] differentalgorithm,orbuffersize).Veritas’semulationprovides𝐾
outcomesforthecounterfactualqueryratherthanjustasingleone,
withgradientdescentupdates,specificallytailoredtoourmodel
capturingtheuncertaintyinherentintheabductionstepgiventhe
(seeAlgorithm2intheAppendix).
observeddata.Whiletheabovedescriptionpertainstocounterfac-
| Abductionof𝐶 |     | 1:𝑇.Oncethemodelparametersarelearnedfora |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tualqueries,Veritascanalsobeusedforinterventionalqueriesas
givensession,Veritas’sabductionisperformedbysampling𝐶
1:𝑇
| giventhoseHoEHMMparameters.Wesample𝐶 |     |     |     |     | accordingto |     | describedin§4.3. |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | ----------- | --- | ---------------- | --- | --- | --- | --- |
1:𝑇
theposteriorinEquation(1)usingtraditionalBayesiansampling
744

ACMSIGCOMM’23,September10–14,2023,NewYork,NY,USA ChandanBothra∗,JianfeiGao∗,SanjayRao,andBrunoRibeiro
Question CausalSim Veritas toobtainthemetricspredictedbytheseschemes,andgroundtruth.
(RCTrequired) (NoRCT Veritassamplesmultipleinferredtraces(fivebydefault)foreach
required) videosession,eachofwhichareemulated.CausalSimdoesnotre-
ChangeofABR 50%MPC 100%MPC quireemulation—instead,itdirectlypredictsthemetricsofinterest
(MPCtoBBA) 50%Bola1 usingthevideologsfromSettingAasinputtoaNeuralNetwork
Changeofbuffer 50%BBA(15s) 100%BBA model.
(15sto5s) 50%MPC(15s) (15s) Training.Table1summarizesthewhat-ifquestionsthatwe
Changeofqualities 50%BBA(Low) 100%BBA explore,andthetrainingdatausedforeachofVeritasandCausal-
(LowtoHigh) 50%MPC(Low) (Low) Sim.NotethatCausalSimrequiresRCTtrainingdatacollectedfrom
twodifferentABRalgorithmstoevaluateperformanceinthetarget
algorithminSettingB,whileVeritasonlyrequiresdatafromthe
Table 1: What-if questions explored in emulation experi-
sourcealgorithminSettingA.WetraintheCausalSimmodel[8]for
ments.VeritasonlyneedstrainingdatafromasingleABR
GroundTruthevaluationwiththeoptimalhyperparametersshared
algorithm,whileCausalSimrequirestrainingdatafrommul-
bytheauthors[1].VeritasusestheHoEHMMdescribedin§3.2and
tiplealgorithmsusinganRCT.
istrainedwiththevideologsfromtheSettingA.Weoptimisethe
HoEHMMmodelusingnativegradientdescentalgorithm.Inour
4 EVALUATION experimentswediscretiseINBusing𝜖 ∈ {0.05,0.5,1}Mbps,and
discretisethetimestepswith𝜎 ∈{1,5}seconds.Fortheconstruc-
WeevaluateVeritaswithrespecttoitsabilitytoanswerarangeof
tionoftransitionmatrixofHoEHMM,weassumethemaximum
what-ifquestionsusingtwosetsofexperiments:
capacitytobe1.5xthemaximumobservedthroughputobseevedin
•Emulationexperiments,whichcomparesVeritas’spredictions
thesession.
togroundtruth.Theseexperimentsallowevaluationswithvariety
Metrics.Foranywhat-ifquestion,eachschemepredictsstan-
ofwhat-ifquestions(changeofvideoqualities,buffersizeandABR
dard video session metrics such as video quality (measured by
algorithm),andalsoallowevaluationofcounterfactualquestions
SSIM[49])andrebufferingratios.Wealsopresentthedistribution
(i.e.,questionspertainingtotheexactsametraceifalternatesetting
ofbufferoccupancy,andchunkdownloadtimespredictedbyeach
wereconsidered).
scheme.
•Realworldexperiments,whereweuseVeritastopredictthe
Setupdetails.WeusetheevaluationsetupofYanetal.[50]
resultofwhat-ifquestionsonlogsofrealworldvideosessionscol-
torunouremulationexperimentswithdifferentABRalgorithms
lectedbyPuffer[50].Here,groundtruthisunavailableforcounter-
andsystemsettings.WeemulateFCCthroughputtraces[2]toplay
factualqueries,butthedatasetallowsevaluationofinterventional
a5minutepre-recordedvideoclipwithbitraterangingfrom0.1
queries(i.e.,predictionsonsessionswithsimilarcharacteristics)
Mbpsto4MbpsusingMahimahi[32].Ouremulationexperiments
thoughonlyaclassofqueriespertainingtoachangeofABRalgo-
useTCPCUBIC[18],anddisableTCPSlowStartRestart[13,33]
rithmmaybevalidated(§4.3).
astypicallydoneinproductionvideoservers(ourPufferdatain
§4.3isbasedonsessionsrunningBBR).Weuseastandardvideo
4.1 Evaluationwithcounterfactuals
providedwithPuffer[50],whoseaverageSSIMindexforthelowest
Schemescompared.WecompareVeritas’sabilitytoperformcoun- andhighestqualityare10.36dBand18.58dBrespectively.The
terfactualinferenceagainstseveralapproaches: clientsarelaunchedinsideamahimahishellwitha80msendto
•GroundTruth:Thisreferstothemetricscollectedwhenemu- enddelayanddownlinkbandwidthlimitedbyFCCtraces.Weselect
latingtheintrinsicgroundtruthnetworkbandwidth(INB),defined FCCtraceswithnetworkbandwidthvaryingbetween1Mbpsto5
in§3.1.Thisservesastheidealbenchmarkotherapproachesmust Mbps,arangeofbandwidthtypicallyusedfornon-trivialbitrate
achieve. adaptations[7,28,50].
•Baseline:ThisschemeestimatesINBusingtheobservedthrough-
putofeachchunkoverthedurationofchunkdownloads.During
offperiods,whennoestimateisavailable,linearinterpolationof
thethroughputobservedbythepreviousandnextchunksisused.
Thisschemeiscommonlyusedinmostvideostreamingevaluations
5
today[7,28,51]butdoesnotaccountforunobservedconfounders.
•CausalSim:Asdiscussedin§2.4,CausalSim[8]answerscausal
queriesbutrequirestrainingdataobtainedusinganRCTwhere
sessionsareassignedtooneof𝐾 ABRpoliciesatrandom.Weuse 0
0 50 100 150 200
thecodeprovidedbytheauthors[1]inourexperiments.
ElapsedTime(sec)
Evaluationsetup. WeuseanevaluationsetupsimilartoFig-
ure6.AvideosessioninSettingAisemulatedusingagroundtruth
networkbandwidth(INB)trace.Theresultinglogsareprovided
tothedifferentschemes.BothVeritasandBaselineproducetraces
inferringINB.AvideosessionisemulatedinSettingBwiththe
tracesinferredbytheseschemesaswellastheoriginalINBtrace
spbM
Baseline INB Veritassamples
Figure7:ComparingINB,BaselineandVeritassamplesina
typicalexperiment.
745

Veritas:AnsweringCausalQueriesfromVideoStreamingTraces ACMSIGCOMM’23,September10–14,2023,NewYork,NY,USA
1.0
0.5
0.0
17 18
(a)SSIM(dB)
snoissesfonoitroporP 1.0
0.5
0.0
0.0 0.2 0.4
(b)Rebufratio
snoissesfonoitroporP 1.0
0.5
0.0
0 25 50
(c)Buffer(s)
sknuhcfonoitroporP
GroundTruth
Baseline
Veritas
CausalSim
(RCT)
CausalSim-
Bounded(RCT)
Figure8:Predictingimpactofhighervideoqualities:VeritasperformsclosetoGroundTruth,whileCausalSimandBaselinedo
not.
1.0
0.5
0.0
12.5 15.0 17.5
(a)SSIM(dB)
snoissesfonoitroporP 1.0
0.5
0.0
0.0 0.2
(b)Rebufratio
snoissesfonoitroporP 1.0
0.5
0.0
0 10
(c)Buffer(s)
sknuhcfonoitroporP
GroundTruth
Baseline
Veritas
CausalSim
(RCT)
CausalSim-
Bounded(RCT)
Figure9:Predictingimpactofchangingdeployedbuffersizefrom15sto5s.VeritasismuchclosertoGroundTruthcompared
withCausalSimandBaseline.
4.2 Resultswithcounterfactuals thestartofeachchunkacrossallsessions.SinceVeritasprovides
manysamplespersession,weplotaCDFofallsamples.
WefirstillustrateVeritas’ssampledINBsforatypicalFCCtrace.
Figure8showsVeritasperformsbetterthanallalternatives.First,
Then,compareVeritas’sabilitytoaccuratelyanswercounterfactual
VeritasisclosetoGroundTruthforallmetrics.Second,Baseline
querieswiththeabilityofexistingmethods.
predictslowerbufferoccupancies,higherrebufferingratiosand
IllustratingVeritas.Figure7illustratesVeritasinactionina
lowerSSIMsthanGroundTruth.ThismakessensesinceBaseline
typicalexperiment.Thegreencurve(INB)referstotheintrinsic
usesobservedthroughputwhichtendstobeconservative.Third,
groundtruthbandwidthwhichisemulated.Theredcurveshows
CausalSimpredictsmuchhigherbufferoccupancies,higherSSIM
thetracecreatedusingtheBaselineapproach.Clearly,Baselineis
andlowerrebufferingthanINB.Thisisbecausethetrainingdata
conservativeinitsestimationofINB,especiallyinperiodswherethe
(lowqualities)isfromaregimewherethebandwidthissufficient
ABRalgorithmselectssmallerchunksizes(eitherlowerqualities,or
tosupportthevideoqualities.However,thewhat-ifqueriesthat
lower-sizedchunksofhigherqualitygivenvariablebitratevideo).
relatetohighervideoqualitiespertaintoaregimewherethesame
Thus,trace-drivenemulationsusingBaselinetoanswer"what-if"
bandwidth is now inadequate. This highlights the limitation of
questionswillleadtoincorrectresults.
predictingcounterfactualqueriesusingassociationsinthetraining
ThebluecurvesinFigure7showfivesampletracesinferred
data(asCausalSim’sneuralnetworkdoes).
byVeritasforthesameINBtrace.Allthesesamplesarecloserto
NotethatCausalSimpredictsbufferoccupanciesmuchhigher
INBthanBaselineandsignificantlylessconservative.Veritasmay
thantheclientbuffer(15s).Hence,wealsoconsideranalternate
exhibitmoreuncertaintyinregionswherearangeofdifferentINB
policy,CausalSim-Bounded,wherepredictedbufferoccupancyis
valuesmayresultinthesamethroughputobservations.Thisis
theminimumbetweenCausalSimpredictionsandthemaximum
theintendedbehavior,sinceourcausalestimatesmustaccountfor
buffercapacity.ThisbuffervalueisthenusedbythesimulatedABR
estimationuncertainty.
algorithminCausalSim.Figure8showsthatwhilethiscapsthe
Changeofvideoqualities.Considerascenariowhereavideo
predictedbuffertothemaximum15s,theresultingpredictionsare
streamingapplicationhasbeendeployedwithagivensetoflow
stillnotclosetogroundtruth.Overall,theresultsnotonlyshow
videoqualitiesandwewanttoknowthecounterfactualwhatwould
theeffectivenessofVeritasbutalsothelimitationsofCausalSim
havehappenedifasetofhighervideoqualitieswereusedinstead?
whenevaluatingactionsoutsidethescopeoftheinitialRCT.
Figures8(a)and(b)presentthecumulativedensities(CDFs)of
averageSSIMandrebufferingratiosacrosssessionsforalltested
Changeofbuffer.Next,weconsiderawhat-ifquerypertaining
toachangeinclientbuffersize.GivenlogsofanABRalgorithm
methods.Figure8(c)presentstheCDFofthebufferoccupancyat
746

ACMSIGCOMM’23,September10–14,2023,NewYork,NY,USA ChandanBothra∗,JianfeiGao∗,SanjayRao,andBrunoRibeiro
deployedwitha15sbuffer,thegoalistopredicttheperformanceif Source Target CausalSim(RCT) Veritas
thebuffersizewerereducedto5stomoveclosertoalivestreaming ABR ABR training training
setting.Figure9presentsresults.Again,Veritasperformscloseto Bola1 Bola1,Bola2 Bola1
BBA
GroundTruthinallmetrics.Baselineismoreconservativepredict- Bola2 Bola1,Bola2 Bola2
inglowerbufferoccupancies,lowerSSIMandhigherrebuffering BBA BBA,Bola2 BBA
Bola1
ratios.Incontrast,CausalSimisoptimisticinthesemetrics.Inpar- Bola2 BBA,Bola2 Bola1
ticular,itpredictshighbufferoccupanciessimilartothevalues Bola1 Bola1,BBA Bola1
Bola2
observedinthetrainingdata(whichisbasedona15sbuffer).Dur- BBA Bola1,BBA BBA
inginference,sincethepredictedbuffervaluesarehigh,CausalSim
predictshigherqualitychunksareselected,andpredictslowre-
buffering. Table2:ExperimentsonPufferdataset.Foreachsourceand
WeagainconsiderapolicyCausalSim-Bounded,whichlimits targetpair,Veritasisonlytrainedondatafromasinglesource
thepredictedbuffersizetomaximumof5sorthepredictedbuffer ABR,whileCausalSimistrainedonRCTdatafrommultiple
occupancy,whicheverislower.TheABRalgorithmsimulatedby sourcealgorithms.
CausalSiminthewhat-ifquerytakesthisadjustedbufferprediction.
CausalSim-Boundedpredictsbufferoccupanciesof5secformost
chunks,stillnotclosetogroundtruth.Interestinglyhowever,it comparedtotheperformanceobservedbysessionsassignedto
nowunderestimatesSSIM,andoverestimatesrebufferingratios. algorithmB.Thus,thepredictionsmaybevalidatedwithdatafrom
Thisisbecauseinthetrainingdata,a5sbufferisassociatedwith adifferentsetofsessions,butwithsimilarnetworkcharacteristics.
poorernetworkconditionsintheoriginaltrainingdata.Thisleads Notethatwecanonlyvalidatequestionsrelatedtoachangeof
CausalSim-Boundedtopredictlowervideoqualitiesandhigher ABRalgorithmusingthisdatasetasPufferdoesnotassignbuffer
rebufferingratios. sizesorqualitiesrandomlytosessions.
Changeofalgorithm.Considerthatthevideostreamingap- Evaluationsetup:Weconsideradayofdata(Aug24,2020)and
plicationhasbeendeployedwithagivenABR.Weaskthecoun- focusonthreeABRalgorithmsdeployedonthisday:BBA[20],
terfactualwhatwouldhavehappenedifanalternateABRalgorithm andtwoversionsofBOLA2[41],whichwerefertoasBola1and
wereinsteadused.Westudythisquestionincontextofmovingfrom Bola2.Weconsiderallsixcombinationsofsourceandtargetalgo-
theMPC[35]algorithmtoBBA[20]algorithm.Recallthatinthis rithmsshowninTable2,andcomparethepredictionsofVeritasand
setting,VeritasdoesnothaveaccesstoRCTdata,butCausalSim CausalSim.CausalSimistrainedonRCTdatafrommultiplesource
does.Figure10presentsresultswhichshowdespitethis,bothVeri- ABRalgorithms,whileVeritasisonlytrainedondatafromasingle
tasandCausalSimperformsimilarly.WealsopresentCausalSim sourceasshown.WetrainCausalSimforeachtargetalgorithm
(NoRCT),wheretheschemelikeVeritasistrainedwithoutRCT usingthatday’sdataandtunetheirlosshyperparameterforeach
data(tomakethecomparisonfair).WithoutRCT,CausalSimin- trainingdatasetusingauthorprovidedscripts.
correctlypredictsrebufferingforabout13%ofthesessions,andit Results.Wepresentresultsforslowstreams(definedbyPuffer
erroneouslyunder-predictsandover-predictsbufferoccupaniesin asstreamswithmeandeliveryratelessthan6Mbps),whichare
somecasesasindicatedbythetails.Finally,whentheSSIMmetric morelikelytoinvolvenontrivialbitrateadaptation[8,50].Fig-
isconsidered,CausalSimunderpredicts,andVeritasoverpredicts, ure11comparesCausalSimandVeritaswiththerealworlddata
butthepredictionerrorsarecomparable.Wealsonotethatamore ofthetargetalgorithm.Resultsfromallsixsourcetargetcombina-
conservativeestimateispossiblewithVeritasbytakingthemore tionsarecombinedforbrevityforeachmetric.Wemakeseveral
conservativeofitspredictionsacrosssamples(weelaboratefur- points.First,althoughVeritasdoesnotuseRCT,itmatchesand
therin§4.3).Overall,theresultsshowsthatCausalSim(NoRCT) evenslightlyoutperformsCausalSimwhichneedsRCTtraining
performspoorly,butVeritasmatchesCausalSim(RCT)without data.Whenpredictingdownloadtimeacrosschunksandaverage
requiringRCTdata. SSIMpersession,bothschemesarealmostindistinguishablefrom
eachother,andfromtheperformanceofrealworldtargetsessions.
4.3 Validationswithrealworlddata
Whenbufferoccupancyisconsidered,Veritasslightlyoverestimates
WenextvalidateourresultswithrealInternetvideosessiondata butCausalSimunderestimates–themedianbufferoccupancyof
collectedbyPuffer[50],avideostreamingplatform.InPuffer,each realworldsessionsis9.08s,whilethemedianwithVeritasis9.51s,
videosessionisassignedanABRalgorithmrandomlychosenfroma andwithCausalSimis7.98s.Finally,Veritasslighlyunderestimates
setofalgorithms.Owingtotherandomassignment,thedistribution rebuffering,whileCausalSimoverestimates–forinstance,although
of network characteristics across sessions assigned to different 12%ofrealworldsessionsseerebuffering,CausalSimestimates20%
algorithmsmaybeassumedsimilar.Puffermakeslogsavailablefor seerebuffering,whileVeritasestimates10%seerebuffering.
allvideosessionswhichincludeinformationsuchaschunksizes, Recall,Veritasgenerates𝐾(=5)candidatesamplesforeachinput
chunkdownloadtimes,andbuffersize. traceandourresultssofarconsiderallpredictionsforeachses-
GivenlogscollectedfromanABRalgorithmA1(sourcealgo- sion(whichisakintotakingthemedianprediction).Apractioner
rithm),considerawhat-ifquerythataskswhatwouldbetheper- mayinsteadwishtoobtainconservativeestimatesofSSIMand
formanceifanalgorithmB(targetalgorithm)wereusedinstead. rebufferingwhenmakingaproposedchange.Wealsoconsidera
SinceINBisunknown,wecannotvalidatetheresultingprediction
withgroundtruth.However,thepredictionsofthisquerymaybe 2PufferdeploystwoversionsofBOLAwithdifferentqualityobjectives[3].
747

Veritas:AnsweringCausalQueriesfromVideoStreamingTraces ACMSIGCOMM’23,September10–14,2023,NewYork,NY,USA
| snoissesfonoitroporP | 1.0 |     |     | snoissesfonoitroporP | 1.0 |     | sknuhcfonoitroporP |     |     |     |     |
| -------------------- | --- | --- | --- | -------------------- | --- | --- | ------------------ | --- | --- | --- | --- |
1.0
GroundTruth
|     |     |     |     |     |     |     |     |     | CausalSim |     | Baseline |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- |
|     |     |     |     |     |     |     |     | 0.5 |           |     | Veritas  |
|     | 0.5 |     |     |     | 0.5 |     |     |     | (No RCT)  |     |          |
CausalSim
(RCT)
|     |     |             |     |     |               |     |     | 0.0 |              |     | CausalSim |
| --- | --- | ----------- | --- | --- | ------------- | --- | --- | --- | ------------ | --- | --------- |
|     | 0.0 |             |     |     | 0.0           |     |     |     |              |     |           |
|     | 12  | 14          | 16  |     | 0.0           | 0.1 |     |     | 0            | 20  | (NoRCT)   |
|     |     | (a)SSIM(dB) |     |     | (b)Rebufratio |     |     |     | (c)Buffer(s) |     |           |
Figure10:PredictedperformanceifABRwaschanged.Veritas(withoutRCTtrainingdata)performscomparablytoCausalSim
withRCT,andoutperformsCausalSimwithoutRCT.
1.0
|                    | 1.00 |     |     | 1.00               |     |     | 1.00                 |     |     | snoissesfonoitroporP |     |
| ------------------ | ---- | --- | --- | ------------------ | --- | --- | -------------------- | --- | --- | -------------------- | --- |
| sknuhcfonoitroporP |      |     |     | sknuhcfonoitroporP |     |     | snoissesfonoitroporP |     |     |                      |     |
Real
|     | 0.75 |     |     | 0.75 |     |     | 0.75 |     |     |     |       |
| --- | ---- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- | ----- |
|     |      |     |     |      |     |     |      |     |     | 0.9 | world |
Veritas
Real
|     | 0.50 |     |     | 0.50 |     | world   | 0.50 |     |     |     | (Conservative) |
| --- | ---- | --- | --- | ---- | --- | ------- | ---- | --- | --- | --- | -------------- |
|     |      |     |     |      |     | Veritas |      |     |     | 0.8 | Veritas        |
|     | 0.25 |     |     | 0.25 |     |         | 0.25 |     |     |     | CausalSim      |
CausalSim
|     |      |           |     |      |                 | (RCT) |      |     |          |         | (RCT)       |
| --- | ---- | --------- | --- | ---- | --------------- | ----- | ---- | --- | -------- | ------- | ----------- |
|     | 0.00 |           |     | 0.00 |                 |       | 0.00 |     |          | 0.7 0.0 | 0.2 0.4 0.6 |
|     | 0    | 5         | 10  | 15   | 0 2             | 4     |      | 10  | 20       |         |             |
|     |      | Buffer(s) |     |      | Downloadtime(s) |       |      |     | SSIM(dB) |         | Rebufratio  |
Figure11:Veritas’spredictionsareclosetoRealworldforPufferdataset(slowstreams).VeritaswithoutRCTmatchesCausalSim
withRCTandevenslightlyoutperformsonsomemetrics.
schemethatwerefertoasVeritas(Conservative),whichforeach server,butthechunkscanbeservedfromdifferentlayersofthe
sessiononlyconsidersthemostconservativeestimateofSSIMand CDNowingtocachemissesintheedgelayer,especiallyforless
rebufferingratiosacrossthefivesamples.Veritas(Conservative) popularcontent[17].Investigatingandaddressingsuchadditional
performsveryclosetotherealworldsessions,estimatesa95%tile confounderscouldfurtherimprovetheperformanceofVeritas.
rebufferingratiotobe5.97%,whichisclosetorealworldvalue Anotherimportantfuturedirectionisexploringhowtocombine
of7.39%.Inaddition,Veritas(Conservative)ispracticallyindistin- VeritasandRCTs,whichhavecomplementarybenefits.Dealing
guishablefromVeritasandotherschemesinSSIM,indicatingSSIM withconfoundingvariablesmightbeeasierwithRCTsastheydi-
predictionsacrosssamplesareclose. rectlymeasuretheimpactofinterventiononactiveusers.However,
Finally,wealsocomparedtheperformanceofVeritasandCausal- doingsocanleadtodegradedperformanceandthusRCTstends
Simacrossallthesessionsfortheday.Veritas(withoutRCT)and tobeusedsparingly.TechinquessuchasVeritascanbeusedfor
CausalSim(withRCT)performsimilarlyandarecomparabletoreal offlineanalysistoexploreawiderangeofdesignalternativeswith
worldsessionsacrossallthemetrics—wedefertheseresultstothe themostpromisingdesignchoicesthentestedusingRCTs.
Appendix(Figure12).
6 RELATEDWORK
5 DISCUSSION
•Biasesinvideostreaming.Apreliminaryworkshoppaper[42]
VeritasfocusesonINBasaconfoundingvariablewhileusingob- inspiredbothCausalSim[8]andourwork.However,[42]isre-
servationsofRTTandotherTCPstatevariables.Veritasmodels strictedtoasquarewavebandwidthprocess,doesnotmodelthe
packetlossimplicitlyaslossrateisoneofthefactorsthatimpact dependenceofobservedthroughputonchunksize,orhandletheun-
INB.Anopenquestionforthefutureiswhethermodelinglossrate certaintyininference.Finally,theuseofmatchingin[42]requires
moreexplicitlycanimprovetheperformanceofVeritas. bitratestobeoccasionallychosenrandomly.Anotherwork[11]has
Veritasassumesthatthebitratedecisionsmadebyavideoclient observedthatsmallerchunksizesmayseepoorerthroughputthan
doesnotimpacttheINBexperiencedbythevideosession.This largeronesowingtoTCPslowstarteffects.Tohandlethis,[11]
isreasonablewhenthebottlenecklinkhaslargenumberofcon- comparesthetotalrewardseenbyalgorithm𝐵onatracecollected
currentsessions.However,whenthebottlenecklinkhasonlya fromanalgorithm𝐴byonlyconsideringthosechunkswherethe
smallnumberofconcurrentsessions(e.g.,onalinkconnecting newalgorithmpicksthesamebitrateastheoldalgorithm.The
ahomenetworktotheInternet),moreexplicitlymodellingthe approachdoesnottacklewhat-ifquestions,assumesaconstant
effectofconcurrentsessionsinVeritasmaybeimportant.Veritas bandwidthprocess,anddoesnotmodelthecausaldependenceof
assumeschunksofavideosessionareservedfromasingleCDN chunksizeselectionbytheABRalgorithmonbandwidth.Wetackle
748

ACMSIGCOMM’23,September10–14,2023,NewYork,NY,USA ChandanBothra∗,JianfeiGao∗,SanjayRao,andBrunoRibeiro
theharderproblemofinferringalatentandvariablebandwidth REFERENCES
processfromobservedthroughput,dealwiththeuncertaintyin
[1] CausalSim GitHub. https://github.com/CausalSim/Unbiased-Trace-Driven-
suchinference,andaddressawiderangeofcausalwhat-ifqueries. Simulation.
•Inferringcausaldependenciesandwhat-ifanalysis.Sev- [2] Federalcommunicationscommission.2016.rawdata-measuringbroadband
america. (2016). https://www.fcc.gov/reports-research/reports/measuring-
eralworks[23,27,45]infercausaldependenciesusingcorrelations
broadband-america/raw-data-measuring-broadband-america-2016.
butdonotconsiderlatentconfounders.Somework[19,23,24,46] [3] Implementing BOLA-BASIC on puffer. https://puffer.stanford.edu/bola/
dealswithobservedconfounders–e.g.,Krishnanetal.[24]explored #footnote-1.
[4] Netflix and YouTube agree to reduce bitrate during Coronavirus cri-
whethervideostreamquality(e.g.,rebufferingratios)causallyim-
sis.https://www.broadbandtvnews.com/2020/03/19/netflix-agrees-to-reduce-
pacts user engagement metrics while acccounting for observed bitrate-during-coronavirus-crisis/.
confounderssuchasuserconnectiontype(DSLvs.mobile)and [5] PyTorch.https://pytorch.org/.
[6] tcp-Linuxmanualpage.https://man7.org/linux/man-pages/man7/tcp.7.html.
location.Theseworksonlyinferifacorrelationisanindicationof [7] ZahaibAkhtar,YunSeongNam,RameshGovindan,SanjayRao,JessicaChen,
acausalrelationshipbutdonotanswerwhat-ifquestions,anddo EthanKatz-Bassett,BrunoRibeiro,JibinZhan,andHuiZhang. Oboe:auto-
notdealwithlatentconfounders.Otherworks[22,40,45]consider
tuningvideoABRalgorithmstonetworkconditions.InProceedingsofthe2018
ConferenceoftheACMSpecialInterestGrouponDataCommunication-SIGCOMM
whatifanalysesforvariousapplications,butdonotaddresscon- ’18,pages44–58,Budapest,Hungary,2018.ACMPress.
foundingvariables.Recentwork[25]considerscausalquestions [8] AbdullahAlomar,PouyaHamadanian,ArashNasr-Esfahany,AnishAgarwal,
MohammadAlizadeh,andDevavratShah. Causalsim:Towardacausaldata-
whileconsideringimplicitfeedbackinthecontextofcloudsystems.
drivensimulatorfornetworkprotocols.arXivpreprintarXiv:2201.01811,2022.
relyingonrandomizedexperiments(fromRLexploration). [9] JoshuaDAngrist,GuidoWImbens,andDonaldBRubin. Identificationof
causaleffectsusinginstrumentalvariables.JournaloftheAmericanstatistical
Association,91(434):444–455,1996.
7 CONCLUSION [10] EliasBareinboim,AndrewForney,andJudeaPearl. Banditswithunobserved
confounders:Acausalapproach. AdvancesinNeuralInformationProcessing
Inthispaper,wemakethreecontributions.First,wehaveshown Systems,28:1342–1350,2015.
[11] MihovilBartulovic,JunchenJiang,SivaramanBalakrishnan,VyasSekar,and
theviabilityofansweringwhat-ifcounterfactualandinterventional
BrunoSiñopoli.BiasesinData-DrivenNetworking,andWhattoDoAboutThem.
queriesrelatedtovideostreamingwithoutaccesstoRCTdata(A/B InProceedingsofthe16thACMWorkshoponHotTopicsinNetworks-HotNets-
testing)throughcausalinference.Next,wepresentVeritas,thefirst XVI,pages192–198,PaloAlto,CA,USA,2017.ACMPress.
[12] EliBingham,JonathanPChen,MartinJankowiak,FritzObermeyer,NeerajPrad-
frameworkthattacklescausalinferenceforvideostreamingusing
han,TheofanisKaraletsos,RohitSingh,PaulSzerlip,PaulHorsfall,andNoahD
datafromasingleABRalgorithm(i.e.,noneedforA/Btesting,RCT Goodman.Pyro:DeepUniversalProbabilisticProgramming.JournalofMachine
trainingdata).VeritasusesaHigh-orderEmbeddedHiddenMarkov LearningResearch,20(28):1–6,2019.
[13] EthanBlanton,Dr.VernPaxson,andMarkAllman. TCPCongestionControl.
Model(HoEHMM)thatrelatestheunobservedINBtimeseriesto RFC5681,September2009.
thethroughputobservedbytheapplication.Akeyinsightbehind [14] BobCarpenter,AndrewGelman,MatthewD.Hoffman,DanielLee,BenGoodrich,
MichaelBetancourt,MarcusBrubaker,JiqiangGuo,PeterLi,andAllenRiddell.
VeritasisexploitinginformationabouttheTCPstateatthestartof
Stan:AProbabilisticProgrammingLanguage. JournalofStatisticalSoftware,
eachchunkdownloadtosimplifythecausalinferencemodel.Third, 76(i01),2017.
weshowtheeffectivenessofVeritasinansweringawiderangeof [15] SiddharthaChib. Calculatingposteriordistributionsandmodalestimatesin
counterfactualandinterventionalqueriesusingemulationtestbed
markovmixturemodels.JournalofEconometrics,75(1):79–97,1996.
[16] DmitryDuplyakin,RobertRicci,AleksanderMaricq,GaryWong,Jonathon
experimentsandreal-worlddatasets.Inacounterfactualqueryper- Duerig,EricEide,LeighStoller,MikeHibler,DavidJohnson,KirkWebb,Aditya
tainingtoincreaseinvideoquality,Veritasestimatesthemedian Akella,KuangchingWang,GlennRicart,LarryLandweber,ChipElliott,Michael
Zink,EmmanuelCecchet,SnigdhaswinKar,andPrabodhMishra.Thedesignand
qualityofvideosessionswithin0.022%oftheGroundTruthwhile operationofCloudLab.InProceedingsoftheUSENIXAnnualTechnicalConference
BaselineandCausalSimincuranerrorof4.06%and3.89%respec- (ATC),pages1–14,July2019.
[17] EhabGhabashnehandSanjayRao.Exploringtheinterplaybetweencdncaching
tively.OnquestionsthatinvolveachangeofABRalgorithm,Veritas
andvideostreamingperformance.In2020IEEEConferenceonComputerCommu-
(withoutRCTtrainingdata)performscomparablytoGroundTruth nications(INFOCOM).IEEE,2020.
andCausalSimwhichhasaccesstoRCTdata;CausalSimwithout [18] SangtaeHa,InjongRhee,andLisongXu.Cubic:Anewtcp-friendlyhigh-speed
RCTdataincorrectlypredictsrebufferingformorethan13%ofthe
tcpvariant.SIGOPSOper.Syst.Rev.,42(5):64–74,jul2008.
[19] HadrienHours,ErnstBiersack,andPatrickLoiseau. ACausalApproachto
sessions.Validationswithrealworlddatasetsconfirmthepromise theStudyofTCPPerformance. ACMTransactionsonIntelligentSystemsand
ofVeritas. Technology,7(2):25:1–25:25,December2015.
[20] Te-YuanHuang,RameshJohari,NickMcKeown,MatthewTrunnell,andMark
Watson.Abuffer-basedapproachtorateadaptation:Evidencefromalargevideo
Thisworkdoesnotraiseanyethicalissues. streamingservice. InProceedingsofthe2014ACMConferenceonSIGCOMM,
SIGCOMM’14,pages187–198,NewYork,NY,USA,2014.ACM.
[21] JunchenJiang,VyasSekar,andHuiZhang.Improvingfairness,efficiency,and
stabilityinhttp-basedadaptivevideostreamingwithfestive. InProceedings
8 ACKNOWLEDGEMENT ofthe8thInternationalConferenceonEmergingNetworkingExperimentsand
Technologies,CoNEXT’12,pages97–108,NewYork,NY,USA,2012.ACM.
[22] YurongJiang,LeninRavindranathSivalingam,SumanNath,andRameshGovin-
WethankCloudlab[16]forprovidinguswiththecomputingre-
dan.WebPerf:EvaluatingWhat-IfScenariosforCloud-hostedWebApplications.
sourcestoruntheexperiments.WethankFrancisYanandKeith InProceedingsoftheConferenceoftheACMSpecialInterestGrouponDataCom-
WinsteinforhelpfuldiscussionsaboutthePuffertestbed.Finally, munication-SIGCOMM’16,pages258–271,Florianopolis,Brazil,2016.ACM
Press.
we thank our shepherd, Michael Schapira, and the anonymous [23] SatoruKobayashi,KazukiOtomo,KensukeFukuda,andHiroshiEsaki.Mining
reviewersfortheirfeedbackwhichgreatlyhelpedimprovethepa- CausalityofNetworkEventsinLogData. IEEETransactionsonNetworkand
per.ThisworkwasfundedinpartbyanAmazonResearchAward,
ServiceManagement,15(1):53–67,March2018.
[24] S.ShunmugaKrishnanandRameshK.Sitaraman.Videostreamqualityimpacts
andbyNationalScienceFoundation(NSF)AwardsIIS-1943364and viewerbehavior:inferringcausalityusingquasi-experimentaldesigns.InProceed-
CNS-2212160. ingsofthe2012InternetMeasurementConference,IMC’12,pages211–224,Boston,
Massachusetts,USA,November2012.AssociationforComputingMachinery.
749

Veritas:AnsweringCausalQueriesfromVideoStreamingTraces ACMSIGCOMM’23,September10–14,2023,NewYork,NY,USA
[25] MathiasLécuyer,SangHoonKim,MihirNanavati,JunchenJiang,Siddhartha Processing,13(4):600–612,2004.
Sen,AleksandrsSlivkins,andAmitSharma. Sayer:UsingImplicitFeedbackto [50] FrancisY.Yan,HudsonAyers,ChenzhiZhu,SadjadFouladi,Jam˜esHong,Keyi
OptimizeSystemPolicies.ACMSymposiumonCloudComputing(SOCC),New Zhang,PhilipLevis,andKeithWinstein.Learninginsitu:arandomizedexper-
York,NY,USA,2021. imentinvideostreaming. In17thUSENIXSymposiumonNetworkedSystems
[26] XiLiu,FlorinDobrian,HenryMilner,JunchenJiang,VyasSekar,IonStoica, DesignandImplementation(NSDI20),pages495–511,2020.
andHuiZhang. Acaseforacoordinatedinternetvideocontrolplane. ACM [51] XiaoqiYin,AbhishekJindal,VyasSekar,andBrunoSinopoli.Acontrol-theoretic
SIGCOMMComputerCommunicationReview,42(4):359–370,2012. approachfordynamicadaptivevideostreamingoverhttp. InProceedingsof
[27] AjayAnilMahimkar,ZihuiGe,AmanShaikh,JiaWang,JenniferYates,Yin the2015ACMConferenceonSpecialInterestGrouponDataCommunication,
Zhang,andQiZhao.TowardsautomatedperformancediagnosisinalargeIPTV SIGCOMM’15,London,UnitedKingdom,2015.
network.ACMSIGCOMMComputerCommunicationReview,39(4):231–242,2009.
Publisher:ACMNewYork,NY,USA.
[28] HongziMao,RaviNetravali,andMohammadAlizadeh.Neuraladaptivevideo
streamingwithpensieve. InProceedingsoftheConferenceoftheACMSpecial
InterestGrouponDataCommunication,pages197–210.ACM,2017.
[29] YunSeongNam,JianfeiGao,ChandanBothra,EhabGhabashneh,SanjayRao,
BrunoRibeiro,JibinZhan,andHuiZhang.Xatu:Richerneuralnetworkbased
predictionforvideostreaming.ACMSIGMETRICS,2022.
[30] SiddharthNarayanaswamy,BrooksPaige,Jan-WillemvandeMeent,AlbanDes-
maison,NoahD.Goodman,PushmeetKohli,FrankD.Wood,andPhilipH.S.Torr.
Learningdisentangledrepresentationswithsemi-superviseddeepgenerative
models.InNIPS,pages5927–5937,2017.
[31] RadfordNeal,MatthewBeal,andSamRoweis. Inferringstatesequencesfor
non-linearsystemswithembeddedhiddenmarkovmodels.Advancesinneural
informationprocessingsystems,16,2003.
[32] RaviNetravali,AnirudhSivaraman,KeithWinstein,SomakDas,AmeeshGoyal,
andHariBalakrishnan.Mahimahi:Alightweighttoolkitforreproducibleweb
measurement. InProceedingsofthe2014ACMConferenceonSIGCOMM,SIG-
COMM’14,page129–130,NewYork,NY,USA,2014.AssociationforComputing
Machinery.
[33] JitendraPadhye,SallyFloyd,andMarkJ.Handley. TCPCongestionWindow
Validation.RFC2861,June2000.
[34] JudeaPearl.Causality.Cambridgeuniversitypress,2009.
[35] YanyuanQin,RuofanJin,ShuaiHao,KrishnaRPattipati,FengQian,Subhabrata
Sen,ChaoqunYue,andBingWang.Acontroltheoreticapproachtoabrvideo
streaming:Afreshlookatpid-basedrateadaptation.IEEETransactionsonMobile
Computing,2019.
[36] LawrenceRRabiner.Atutorialonhiddenmarkovmodelsandselectedapplica-
tionsinspeechrecognition.ProceedingsoftheIEEE,77(2):257–286,1989.
[37] ChristianPRobertandDMTitterington.Reparameterizationstrategiesforhidden
markovmodelsandbayesianapproachestomaximumlikelihoodestimation.
StatisticsandComputing,8(2),1998.
[38] KennethJ.RothmanandSanderGreenland.Causationandcausalinferencein
epidemiology.AmericanJournalofPublicHealth,95Suppl1:S144–150,2005.
[39] StevenLScott. Bayesiananalysisofatwo-statemarkovmodulatedpoisson
process.JournalofComputationalandGraphicalStatistics,8(3):662–670,1999.
[40] RahulSingh,PrashantShenoy,MaitreyaNatu,VaishaliSadaphal,andHarrick
Vin. Analyticalmodelingforwhat-ifanalysisincomplexcloudcomputing
applications. ACMSIGMETRICSPerformanceEvaluationReview,40(4):53–62,
April2013.
[41] KevinSpiteri,RahulUrgaonkar,andRameshKSitaraman.Bola:Near-optimal
bitrateadaptationforonlinevideos. InIEEEINFOCOM2016-The35thAnnual
IEEEInternationalConferenceonComputerCommunications,pages1–9.IEEE,
2016.
[42] P.C.Sruthi,SanjayRao,andBrunoRibeiro.Pitfallsofdata-drivennetworking:
Acasestudyoflatentcausalconfoundersinvideostreaming.InProceedingsof
theWorkshoponNetworkMeetsAI&ML,NetAI’20,page42–47,NewYork,NY,
USA,2020.AssociationforComputingMachinery.
[43] YiSun,XiaoqiYin,JunchenJiang,VyasSekar,FuyuanLin,NanshuWang,TaoLiu,
andBrunoSinopoli.Cs2p:Improvingvideobitrateselectionandadaptationwith
data-driventhroughputprediction.InProceedingsofthe2016ACMSIGCOMM
Conference,pages272–285,2016.
[44] CharlesSuttonandAndrewMccallum.AnIntroductiontoConditionalRandom
FieldsforRelationalLearning.Graph.Models,7:93,2002.
[45] Mukarram Tariq, Amgad Zeitoun, Vytautas Valancius, Nick Feamster, and
MostafaAmmar.Answeringwhat-ifdeploymentandconfigurationquestions
withwise.InProceedingsoftheACMSIGCOMM2008ConferenceonDatacommu-
nication,pages99–110,2008.
[46] MukarramBinTariq,MurtazaMotiwala,NickFeamster,andMostafaAmmar.
Detectingnetworkneutralityviolationswithcausalinference. InProceedings
ofthe5thInternationalConferenceonEmergingNetworkingExperimentsand
Technologies,pages289–300,2009.
[47] GuibinTianandYongLiu.Towardsagileandsmoothvideoadaptationindynamic
httpstreaming.InProceedingsofthe8thInternationalConferenceonEmerging
NetworkingExperimentsandTechnologies,CoNEXT’12,2012.
[48] AndrewJViterbi. Apersonalhistoryoftheviterbialgorithm. IEEESignal
ProcessingMagazine,23(4):120–142,2006.
[49] ZhouWang,A.C.Bovik,H.R.Sheikh,andE.P.Simoncelli.Imagequalityassess-
ment:fromerrorvisibilitytostructuralsimilarity.IEEETransactionsonImage
750

ACMSIGCOMM’23,September10–14,2023,NewYork,NY,USA ChandanBothra∗,JianfeiGao∗,SanjayRao,andBrunoRibeiro
A APPENDIX processbyourproposalasEquation(5).Thepseudocodeofvari-
antsforBaum-Welchforward-backwardandupdateareprovided
Appendicesaresupportingmaterialthathasnotbeenpeer-reviewed.
inAlgorithm1andAlgorithm2.Besides,wealsoprovideINDsam-
A.1 ModelsandAlgorithms plingalgorithminAlgorithm3.Inwhatfollowswedenotethepair
Inthispart,wewillclarifysomedetailsofourmodelsandpresent distribution
p
ri
s
t
e
h
u
m
d
s
o
1
c
a
o
n
d
d
e
2
f
,
o
i
r
nt
a
r
l
i
l
ns
a
i
l
c
go
n
r
e
i
t
t
w
hm
or
s
k
:
b
o
a
u
n
r
d
B
w
a
i
u
dt
m
h
-
(
W
IN
e
B
lc
)
h
sa
v
m
ar
p
i
l
a
i
n
n
t
g
A
A
l
l
g
g
o
o
-
-
Γ 𝑖,𝑗,𝑛 =𝑃 (cid:0)𝐶 𝑠𝑛 =𝑖𝜖,𝐶 𝑠𝑛+1 = 𝑗𝜖(cid:12) (cid:12) 𝑌 1:𝑁 ,𝑊 𝑠1:𝑁 ,𝑆 1:𝑁 (cid:1). (6)
rithm3,andnetworkthroughputestimatorAlgorithm4usedin
Input:StateSpaceC,Transitiontimes𝑇,Initialdistribution
ourHoEHMM.
𝑢1 ,Transitionmatrix𝐴,Emissionprocess𝐸
𝑠
W
a
h
r
y
en
𝐵
o
𝑠1
t
:𝑁
de
n
fi
e
n
e
e
d
d
n
a
o
s
t
r
b
an
e
d
o
o
b
m
se
v
r
a
v
r
e
i
d
ab
.
l
I
e
n
s
F
t
i
o
gu
s
r
im
e4
p
’
l
s
if
D
y
A
e
G
xp
,
o
st
s
a
it
r
i
t
o
t
n
im
.I
e
f
(Equation(5)),Throughputs𝑌 1:𝑁 ,TCPstates𝑊 𝑠1:𝑁 ,
1:𝑁 Chunksizes𝑆 ,intervalgapsΔ,capacityunit𝜖
1:𝑇
wehaddefined𝑠 asanobservedrandomvariable,𝑠 could
1:𝑁 1:𝑁 Output:ForwardDistribution𝛼,BackwardDistribution𝛽,
have been used in place of 𝐵 to define the sufficient set of
𝑠𝑛−1 ConditionalDistributionΞ,ConditionalJoint
observedvariablesinour𝑑-separationargument.Lookingatthe
DistributionΓ
dependencebetween𝑃(cid:0)𝐶 𝑠𝑛 = 𝑗𝜖(cid:12) (cid:12) 𝐶 𝑠𝑛−1 =𝑖𝜖(cid:1)andΔ 𝑛 makesitclear /* Alias */
thatobserving𝑠 isalsonecessaryforourMarkovmodel.To
c n o e n ce c s lu sa d r e y ,t a h n e d n s , u w 1 ffi : e 𝑁 c d ie o n n t o a t n a d c r t e u a a d ll i y ly n a e v e a d ila to bl l e o i g n 𝐵 t 𝑠 h 1 e :𝑁 tr s a i c n e c . e𝑠 1:𝑁 is 𝜉 𝜉 𝑖 𝑖 f b , , o a 𝑗 𝑗 r , , c 𝑛 𝑛 e k = = 𝐴 𝐴 𝑖 Δ 𝑖 Δ , , 𝑛 𝑗 𝑛 𝑗 + 𝐸 1𝐸 (cid:0)𝑌 (cid:0) 𝑛 𝑌 , 𝑛 𝑊 +1 𝑠 , 𝑛 𝑊 ,𝑆 𝑠 𝑛 𝑛+ (cid:12) (cid:12) 1 𝑗 , 𝜖 𝑆 (cid:1) 𝑛 ,∀ + 𝑖 1 𝜖 (cid:12) (cid:12) 𝑗 , 𝜖 𝑗𝜖 (cid:1),∀ ∈ 𝑖𝜖 C , , 𝑗 ∀ 𝜖 2 ∈ ≤ C 𝑛 ,∀ ≤ 1 𝑁 ≤𝑛 ≤
Domainspecificemissionprocess.Weuseasimplemodel𝑓, 𝑁 −1
whichestimatesthroughputgivenINB,TCPstateandsizeofrelated /* Forward */
download chunk. The pseudo code is provided in Algorithm 4. 𝛼1,𝑖 =𝑢1,𝑖 𝐸(cid:0)𝑌1,𝑊 𝑠1 ,𝑆1 (cid:12) (cid:12) 𝑖𝜖(cid:1),∀𝑖𝜖 ∈C
Besides,wecannotguarantee𝑓 beingaperfectestimatorforreal- for𝑛=2−→𝑁 do
worldthroughputs,thuswealsoneedtotakeuncertaintyof𝑓 by 𝛼 𝑛,𝑖 = (cid:205) 𝛼 𝑛−1,𝑗 𝜉b 𝑗, a 𝑖, c 𝑛 k,∀𝑖𝜖 ∈C
Gaussiannoise(Equation(4))asshownbelowinEquation(5).The 𝑗𝜖∈C
varianceishigherintheinitialstageofthesessiontomodelTCP end
slowstarteffectsatthestartofasession. /* Backward */
𝑃 (cid:0)𝑌 𝑛 (cid:12) (cid:12) 𝑊 𝑠𝑛 ,𝑆 𝑛 ,𝐶 𝑠𝑛 (cid:1) 𝛽 𝑁,𝑖 =1,∀𝑖𝜖 ∈C
=   𝑍 𝑍 1 1 𝑖 𝑖 e e x x p p (cid:18) (cid:18) − − 1 2 1 2 ( ( 𝑓 𝑓 ( ( 𝐶 𝐶 𝑠 𝑠 𝑛 𝑛 , , 𝑊 𝑊 𝑠 𝑠 𝜎 𝜎 𝑛 𝑛 1 2 2 2 , , 𝑆 𝑆 𝑛 𝑛 ) ) − − 𝑌 𝑌 𝑛 𝑛 ) ) 2 2 (cid:19) (cid:19) 𝑠 𝑠 𝑛 𝑛 > ≤ 𝑇 𝑇 s s t t a a b b l l e e . (5) / f e o * n r d P 𝛽 𝑛 o 𝑛 = s ,𝑖 t 𝑁 = er 𝑗 − i 𝜖 (cid:205) o ∈ 1 r C − 𝜉 → 𝑖 f , o 𝑗 r ,𝑛 e 1 𝛽 d 𝑛 o +1,𝑗 ,∀𝑖𝜖 ∈C */

Here,𝑇
stable
istheswitchingtimebetweentheinitialphasethat for𝑛=1−→𝑁 −1do
includesslowstartandthesteadystatephaseand𝑍 𝑖 isanormal- for𝑖𝜖 ∈Cdo
i a z n a d tio w n e f t a a c k t e or t . h T is he in u to nc c e o r n ta s i i n d t e y ra o t f io 𝑓 n w w i i l t l h va tw ry o b v e a tw ria e n en ce tw 𝜎2 o a s n ta d g 𝜎 es 2 , Ξ 𝑖,𝑛 = (cid:205) 𝛼𝑛 𝛼 ,𝑖 𝑛 𝛽 , 𝑛 𝑗𝛽 ,𝑖 𝑛,𝑗
1 2 𝑗𝜖∈C
foreachstagerespectively. end
ParameterTuning.Therearetwogroupsoflearnableparame-
end
ters:Oneistransitionmatrixparameters𝜃,theotherisestimator for𝑛=1−→𝑁 −1do
uncertaintyparameters𝜎.SinceourHoEHMMcanbetreatedasa for𝑖𝜖 ∈Cdo
variantofHMM-Gaussianmodel,wecanutilizetheBaum-Welch for𝑗𝜖 ∈Cdo
a m [3 lg a 6 o t ] r . r i S i x t u h a p m n p d , os w e e m h t i h i c s e h s t io r c a a n n n v si p a ti r r o i o a n v n i m c d e e a s s tr ( t i u h x n e a c n b e d e rt s e a t m in e i s t s y t s i ) i m o g n a iv t v i e o a n n ria t o r n f a c i t e n r s i a n l n e g s a i r d t n i a o e t n d a Γ 𝑖,𝑗,𝑛 = 𝑘𝜖 (cid:205) ∈C 𝛼 𝑙𝜖 (cid:205) 𝑛 ∈ ,𝑖 C 𝜉 𝛼 𝑖 f , o 𝑛 𝑗 r , e , 𝑛 𝑘 𝛽 𝜉 𝑛 𝑘 fo , + 𝑙 r 1 , e 𝑛 ,𝑗 𝛽 𝛽 𝑛 𝑛 + + 1 1 ,𝑙 ,𝑗 𝛽𝑛+1,𝑙
byBaum-Welchare𝐴∗and(𝜎∗)2,wecanconstructaMeanSquared end
Error(MSE)lossfunction end
end
𝑙(𝜃,𝜎)=∥𝐴∗−𝐴(𝜃)∥+∥(𝜎∗) 2 −𝜎2 ∥ Algorithm1:Forward-BackwardAlgorithm.Itfirstcom-
and use vanilla gradient descent algorithm to update learnable putesforwarddistribution𝛼 𝑛,𝑖 = 𝑃(cid:0)𝐶 𝑠𝑛 =𝑖𝜖(cid:12) (cid:12) 𝑌1:𝑛 ,𝑊 𝑠1:𝑛 ,𝑆1:𝑛 (cid:1);
parameters𝜃and𝜎ineachBaum-Welchiteration.Thepseudocode then computes backward distribution 𝛽 𝑛,𝑖 = 𝑃(cid:0)𝐶 𝑠𝑛 =
ofa A f l u g l o l r u i p th da m te P it s e e ra u t d io o n C is o p d r e o . v A id s ed in i t n ro A d l u g c o e r d ith in m S 2 e . ction3.2,our 𝑖 d 𝜖 i (cid:12) (cid:12) s 𝑌 t 𝑛 ri + b 1 u :𝑁 ti , o 𝑊 n 𝑠 Γ 𝑛 𝑖 + , 1 𝑗 : , 𝑁 𝑛 , = 𝑆 𝑛 𝑃 + (cid:0) 1 𝐶 :𝑁 𝑠𝑛 (cid:1); = an 𝑖𝜖 d , fi 𝐶 n 𝑠𝑛 a + l 1 ly = ac 𝑗 h 𝜖 i (cid:12) (cid:12) 𝑌 ev 1: e 𝑁 c , o 𝑊 n 𝑠 d 1 i :𝑁 tio ,𝑆 n 1 a :𝑁 lj (cid:1) oi b n y t
Baum-Welchvariantisnearlythesameastheirorigins,butreplace combining𝛼and𝛽forall𝑖,𝑗inINBstatespacefrom1to𝑁−1
thetransitionmatrixfromconstantmatrix𝐴to𝐴Δ𝑛 whereΔ
𝑛
is chunks.
as shown in Section 3.2 and Figure 5, and replace the emission
751

Veritas:AnsweringCausalQueriesfromVideoStreamingTraces ACMSIGCOMM’23,September10–14,2023,NewYork,NY,USA
Input:StateSpaceC,Stableandunstablethreshold𝑇 stable , Input:IntrinsicNetworkBandwidth𝐶,TCPstate𝑊 𝑠𝑛 ,
|     | Parametrictransitionmatrix𝐴(𝜃),Uncertainty |     |     |     |     |     | Chunksize𝑆 | 𝑛   |     |     |
| --- | ------------------------------------------ | --- | --- | --- | --- | --- | ---------- | --- | --- | --- |
parameter𝜎,Throughputs𝑌 ,Conditional Output:Estimatedthroughput𝑌
|     |     |     |     | 1:𝑁 |     |     |     |     | 𝑛   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
DistributionΞ,ConditionalJointDistributionΓ, /* Get number of data segments. */
Transitionlearningrate𝜂1 ,Uncertaintylearning 𝑑𝑎𝑡𝑎_𝑠𝑒𝑔𝑚𝑒𝑛𝑡𝑠 ←𝑔𝑒𝑡_𝑠𝑒𝑔𝑚𝑒𝑛𝑡𝑠(𝑆
𝑛)
𝑚 𝑖𝑛 _ 𝑟𝑡𝑡
r a te 𝜂 2 𝑏 𝑑 𝑝_ 𝑠 𝑒 𝑔 𝑚 𝑒 𝑛 𝑡 𝑠 ← 𝑔 𝑒 𝑡 _ 𝑠 𝑒 𝑔 𝑚 𝑒 𝑛 𝑡 𝑠 ( 𝐶 ∗ 𝑊 𝑠 )
|     |     |     | meter𝜃ˆ,Updated |     |     |     |     |     |     | 𝑛   |
| --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Output : U p d a t e d t r an s i t io n p a ra 𝑊 𝑐 𝑤 𝑛 𝑑 > 𝑏 𝑑 𝑝_ 𝑠 𝑒 𝑔 𝑚 𝑒 𝑛 𝑡 𝑠
|     |     |     |     |     |     | if 𝑠 |     | t   | h e n |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | ----- | --- |
u n c e r t a in t y p a r a m e te r 𝜎ˆ 𝑛 𝑑 𝑎 𝑡𝑎 𝑠 𝑒 𝑔 𝑚 𝑒 𝑛 𝑡 𝑠 > 𝑏 𝑑 𝑝 𝑠 𝑒 𝑔 𝑚 𝑒 𝑛 𝑡𝑠
|     |     |     |     |     |     | i f | _   |     | _   | th e n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
𝑚 𝑖𝑛_𝑟𝑡𝑡
/ * B au m - W e l c h U p d a t e */ return(𝑆 𝑛)/((𝑆 𝑛/𝐶)+𝑊 )
𝑠 𝑛
| 𝐴 ★  | (cid:205) 𝑁 − 1  | Γ𝑖 ,𝑗 ,𝑛, 𝑖 𝜖 , 𝑗𝜖 |     |     |     |      |         |          |     |     |
| ---- | ---------------- | ------------------ | --- | --- | --- | ---- | ------- | -------- | --- | --- |
| 𝑖 ,𝑗 | = 𝑛 = 1          | ∀                  | ∈C  |     |     | else |         |          |     |     |
|      | (cid:205) 𝑁 − 1Ξ | 𝑖,𝑛                |     |     |     |      |         | 𝑚 𝑖𝑛_𝑟𝑡𝑡 |     |     |
| N    | ={𝑛 |1 𝑛 = 1     | 𝑛 ≤𝑇               |     |     |     |      | return𝑆 | 𝑛/𝑊 𝑠    |     |     |
| 1    | ≤                | stable}            |     |     |     |      |         | 𝑛        |     |     |
end
| N 2={𝑛|𝑇 | stable        | <𝑛 ≤𝑁}          |     |     |     |       |                 |                 |            |     |
| -------- | ------------- | --------------- | --- | --- | --- | ----- | --------------- | --------------- | ---------- | --- |
| for𝑝     | =1,2do        |                 |     |     |     | else  |                 |                 |            |     |
|          | (cid:205)     |                 |     |     |     | 𝑟 𝑜 𝑢 | 𝑛 𝑑 𝑠 0         |                 |            |     |
|          | 𝑤 𝑝 = 𝑠       | N Ξ 𝑖 , 𝑛       |     |     |     |       | ←               |                 |            |     |
|          |               | 𝑛 ∈ 𝑝           |     |     |     | 𝑠 𝑒 𝑛 | 𝑡 0             |                 |            |     |
|          | 𝐻 = (cid:205) | Ξ 𝑌             |     |     |     |       | ←               |                 |            |     |
|          | 𝑝 𝑠           | 𝑛 ∈ N 𝑝 𝑖 , 𝑛 𝑛 |     |     |     |       | 𝑐               | 𝑤 𝑛 𝑑           |            |     |
|          | (cid:205)     | 2               |     |     |     | 𝑐 𝑤   | 𝑛 𝑑 ← 𝑊 𝑠       |                 |            |     |
|          | 𝐺 𝑝 = 𝑠       | N Ξ 𝑖 , 𝑛 𝑌 𝑛   |     |     |     |       | 𝑛               |                 |            |     |
|          |               | 𝑛 ∈ 𝑝           |     |     |     | w h   | i l e 𝑠 𝑒 𝑛 𝑡 < | 𝑑 𝑎𝑡 𝑎 _𝑠 𝑒 𝑔 𝑚 | 𝑒 𝑛 𝑡𝑠 d o |     |
𝐻
|     | 𝜇 𝑝 = 𝑝 |                |     |     |     |     | 𝑠 𝑒 𝑛 𝑡 𝑠   | 𝑒𝑛 𝑡 𝑚 𝑖 𝑛 𝑊 | 𝑐 𝑤 𝑛𝑑 , 𝑏𝑑𝑝_𝑠𝑒𝑔𝑚𝑒𝑛𝑡𝑠) |     |
| --- | ------- | -------------- | --- | --- | --- | --- | ----------- | ------------ | ---------------------- | --- |
|     | 𝑤 𝑝     |                |     |     |     |     | ←           | + (          | 𝑠                      |     |
|     |         |                | 2   |     |     |     |             |              | 𝑛                      |     |
|     | (𝜎 ★)2  | 𝐺𝑝−2𝐻𝑝 𝜇 𝑝+𝑤𝑝𝜇 | 𝑝   |     |     |     | 𝑐 𝑤 𝑛 𝑑 ←   | 𝑐𝑤 𝑛 𝑑 + 1   |                        |     |
|     | 𝑝 =     | 𝑤              |     |     |     |     |             |              |                        |     |
|     |         | 𝑝              |     |     |     |     | 𝑟 𝑜𝑢 𝑛 𝑑𝑠 ← | 𝑟𝑜 𝑢 𝑛 𝑑𝑠 +1 |                        |     |
| end |         |                |     |     |     | end |             |              |                        |     |
/ * G ra d ie n t D e sc e n t Up d at e */ return(𝑆 𝑛/(𝑟𝑜𝑢𝑛𝑑𝑠∗𝑊 𝑚 𝑖𝑛_𝑟𝑡𝑡 )
𝑠 𝑛
| 𝑙 = | ∥𝐴 ∗ − 𝐴 ( | 𝜃) ∥ + ∥ ( 𝜎 ∗)2 | − 𝜎 2 ∥ |     |     |     |     |     |     |     |
| --- | ---------- | ---------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
end
| 𝜃ˆ =𝜃−𝜂1𝜕 | 𝜕 𝑙 |     |     |     |     |                                         |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- |
|           | 𝜃   |     |     |     |     | Algorithm4:Networkthroughputestimator:𝑓 |     |     |     |     |
| 𝜎ˆ =𝜎−𝜂2𝜕 | 𝜕   | 𝑙   |     |     |     |                                         |     |     |     |     |
𝜎
Algorithm2:HoEHMMUpdate.ItisacombinationofBaum-
Welchandgradientdescentupdate.ItfirstusesBaum-Welch
algorithmtoachieveexpectedtransitionmatrixanduncertainty,
thenusesgradientofMeanSquaredError(MSE)losstoupdate
transitionanduncertaintyparameters.
Input:StatespaceC,Length𝑇,Forwarddistribution𝛼
fromAlgorithm1,Transition𝐴,PairdistributionΓ
Output:Asampledcapacitytrace𝐶
| /*   | Chunk-level    | sampling.   |               |     | */  |     |     |     |     |     |
| ---- | -------------- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| 𝐶 𝑠𝑁 | ∼Multinomial(𝛼 | 𝑛/(cid:205) | 𝑗𝜖∈C 𝛼 𝑛,𝑗)·𝜖 |     |     |     |     |     |     |     |
for𝑛=𝑁 −1to1do
|     | 𝜉 = Γ               | , 𝑖             | 𝜖 ∈ C  |     |     |     |     |     |     |     |
| --- | ------------------- | --------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     | 𝑛 , 𝑖 𝑖 ,𝐶          | 𝑠 / 𝜖, 𝑛 +1     |        |     |     |     |     |     |     |     |
|     | 𝜋 𝜉                 | 𝑛 (cid:205)+1 𝜉 | , 𝑖𝜖   |     |     |     |     |     |     |     |
|     | 𝑛 , 𝑖 = 𝑛           | ,𝑖 / 𝑗𝜖 ∈ C 𝑛   | , 𝑗 ∈C |     |     |     |     |     |     |     |
|     | 𝐶 𝑠𝑛 ∼Multinomial(𝜋 |                 | 𝑛)·𝜖   |     |     |     |     |     |     |     |
end
| /*        | Interval-level | sampling. |     |     | */  |     |     |     |     |     |
| --------- | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| for𝑛=1to𝑁 |                | −1do      |     |     |     |     |     |     |     |     |
(cid:12)
|     | 𝑝 ′ =𝑃 (cid:0)𝑌 | 𝑛 (cid:12) 𝑊 𝑠𝑛 ,𝑆 𝑛 ,𝐶 | 𝑠𝑛 (cid:1) |     |     |     |     |     |     |     |
| --- | --------------- | ----------------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
𝑡
|     | for𝑡 =𝑠            | 𝑛+1to𝑠 𝑛+1−1do |                |     |     |     |     |     |     |     |
| --- | ------------------ | -------------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
|     | 𝜉 ′                | 𝐴 𝑝            | ′ 𝐴 𝑠 − 𝑡      | ,𝑖𝜖 |     |     |     |     |     |     |
|     | 𝑡 , 𝑖 =            | 𝐶 1/𝜖 , 𝑖 ·    | 𝑡 · 𝑛 + 1      | ∈C  |     |     |     |     |     |     |
|     |                    | 𝑡 −            | 𝑖 , 𝐶 𝑠 𝑛 1 /𝜖 |     |     |     |     |     |     |     |
|     | 𝜋 ′                | 𝜉 ′ (cid:205)  | 𝜉 ′ , 𝑖 𝜖 +    |     |     |     |     |     |     |     |
|     | 𝑡 , 𝑖 =            | 𝑡 ,𝑖 / 𝑗 𝜖 ∈ C | 𝑡 ,𝑗 ∈ C       |     |     |     |     |     |     |     |
|     | 𝐶 𝑡 ∼Multinomial(𝜋 |                | ′)·𝜖           |     |     |     |     |     |     |     |
𝑡
end
end
| Algorithm3:CapacitySampler.Itobtainsthelaststate𝑁 |     |     |     |     | as  |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thelaststateofViterbioutput,thenforwardsampleseachstate
1≤𝑛<𝑁 basedonsampledstate𝑛+1andscoresdefinedby
Equation(6).Aftersamplingcapacitiesofchunks,itsamplesa
secondtimetogeneratecapacitiesofeveryinterval.
752

ChandanBothra∗,JianfeiGao∗,SanjayRao,andBrunoRibeiro
ACMSIGCOMM’23,September10–14,2023,NewYork,NY,USA
| 1.00 |     |     |     |     |     | 1.00 |     | 1.00 |     |
| ---- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- |
sknuhcfonoitroporP 1.00 snoissesfonoitroporP snoissesfonoitroporP
|      | Real    |     | sknuhcfonoitroporP |     |     |      |     |      | Real    |
| ---- | ------- | --- | ------------------ | --- | --- | ---- | --- | ---- | ------- |
|      | world   |     |                    |     |     |      |     |      | world   |
| 0.75 |         |     | 0.75               |     |     | 0.75 |     | 0.95 |         |
|      | Veritas |     |                    |     |     |      |     |      | Veritas |
(Conservative)
| 0.50 | CausalSim |     |      |     |     | 0.50 |     | 0.90 |         |
| ---- | --------- | --- | ---- | --- | --- | ---- | --- | ---- | ------- |
|      | (RCT)     |     | 0.50 |     |     |      |     |      | Veritas |
CausalSim
| 0.25 |           |     | 0.25    |                 |         | 0.25 |          | 0.85 | (RCT)       |
| ---- | --------- | --- | ------- | --------------- | ------- | ---- | -------- | ---- | ----------- |
| 0.00 |           |     | 0.0 0   |                 |         | 0.00 |          | 0.80 |             |
| 0    | 5         | 10  | 15 1 0− | 2 10− 1         | 100 101 |      | 10 20    | 0.0  | 0.2 0.4 0.6 |
|      | Buffer(s) |     |         | Downloadtime(s) |         |      | SSIM(dB) |      | Rebufratio  |
|      | (a)       |     |         | (b)             |         |      | (c)      |      | (d)         |
Figure12:ValidationwithallrealvideosessionsobtainedfromPufferduringaday.VeritaswithoutRCTdatamatchesthe
performanceofCausalSimwithRCTdata.Thecurvesareindistinguishablefordownloadtime,bufferandSSIM.WhileVeritas
underestimatesandCausalSimoverestimatestherebufferingratio,Veritas(Conservative)ismuchclosertoGroundTruth
rebufferingratio.
753