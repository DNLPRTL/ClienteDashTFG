Neural Adaptive Video Streaming with Pensieve
Hongzi Mao, Ravi Netravali, Mohammad Alizadeh
MIT Computer Science and Artificial Intelligence Laboratory
{hongzi,ravinet,alizadeh}@mit.edu
ABSTRACT contentproviders[12,25].Nevertheless,contentproviderscontinue
Client-sidevideoplayersemployadaptivebitrate(ABR)algorithms tostrugglewithdeliveringhigh-qualityvideototheirviewers.
tooptimizeuserqualityofexperience(QoE).Despitetheabundance Adaptivebitrate(ABR)algorithmsaretheprimarytoolthatcon-
ofrecentlyproposedschemes,state-of-the-artABRalgorithmssuffer tentprovidersusetooptimizevideoquality.Thesealgorithmsrun
fromakeylimitation:theyusefixedcontrolrulesbasedonsimplified onclient-sidevideoplayersanddynamicallychooseabitratefor
orinaccuratemodelsofthedeploymentenvironment.Asaresult, eachvideochunk(e.g.,4-secondblock).ABRalgorithmsmakebi-
existing schemes inevitably fail to achieve optimal performance tratedecisionsbasedonvariousobservationssuchastheestimated
acrossabroadsetofnetworkconditionsandQoEobjectives. networkthroughputandplaybackbufferoccupancy.Theirgoalis
WeproposePensieve,asystemthatgeneratesABRalgorithms to maximize the user’s QoE by adapting the video bitrate to the
usingreinforcementlearning(RL).Pensievetrainsaneuralnetwork underlyingnetworkconditions.However,selectingtherightbitrate
modelthatselectsbitratesforfuturevideochunksbasedonobser- canbeverychallengingdueto(1)thevariabilityofnetworkthrough-
vations collected by client video players. Pensieve does not rely put[18,42,49,52,53];(2)theconflictingvideoQoErequirements
onpre-programmedmodelsorassumptionsabouttheenvironment. (highbitrate,minimalrebuffering,smoothness,etc.);(3)thecascad-
Instead,itlearnstomakeABRdecisionssolelythroughobservations ingeffectsofbitratedecisions(e.g.,selectingahighbitratemay
oftheresultingperformanceofpastdecisions.Asaresult,Pensieve draintheplaybackbuffertoadangerouslevelandcauserebuffering
automaticallylearnsABRalgorithmsthatadapttoawiderangeof inthefuture);and(4)thecoarse-grainednatureofABRdecisions.
environmentsandQoEmetrics.WecomparePensievetostate-of-the- Weelaborateonthesechallengesin§2.
artABRalgorithmsusingtrace-drivenandrealworldexperiments ThemajorityofexistingABRalgorithms(§7)developfixedcon-
spanningawidevarietyofnetworkconditions,QoEmetrics,and trolrulesformakingbitratedecisionsbasedonestimatednetwork
videoproperties.Inallconsideredscenarios,Pensieveoutperforms throughput(“rate-based”algorithms[21,42]),playbackbuffersize
thebeststate-of-the-artscheme,withimprovementsinaverageQoE (“buffer-based” schemes [19, 41]), or a combination of the two
of12%–25%.Pensievealsogeneralizeswell,outperformingexisting signals[26].Theseschemesrequiresignificanttuninganddonot
schemesevenonnetworksforwhichitwasnotexplicitlytrained. generalizetodifferentnetworkconditionsandQoEobjectives.The
state-of-the-artapproach,MPC[51],makesbitratedecisionsbysolv-
CCSConcepts:Informationsystems→Multimediastreaming;Networks
ingaQoEmaximizationproblemoverahorizonofseveralfuture
→Networkresourcesallocation;Computingmethodologies→Reinforce-
chunks.ByoptimizingdirectlyforthedesiredQoEobjective,MPC
mentlearning
canperformbetterthanapproachesthatusefixedheuristics.How-
Keywords:bitrateadaptation,videostreaming,reinforcementlearning ever,MPC’sperformancereliesonanaccuratemodelofthesystem
ACMReferenceformat:HongziMao,RaviNetravali,MohammadAlizadeh dynamics—particularly, a forecast of future network throughput.
MITComputerScienceandArtificialIntelligenceLaboratory.2017.Neural Asourexperimentsshow,thismakesMPCsensitivetothroughput
AdaptiveVideoStreamingwithPensieve.InProceedingsofSIGCOMM’17,
predictionerrorsandthelengthoftheoptimizationhorizon(§3).
August21-25,2017,LosAngeles,CA,USA,14pags. Inthispaper,weproposePensieve,1 asystemthatlearnsABR
DOI:http://dx.doi.org/10.1145/3098822.3098843
algorithmsautomatically,withoutusinganypre-programmedcon-
trolrulesorexplicitassumptionsabouttheoperatingenvironment.
1 INTRODUCTION Pensieveusesmodernreinforcementlearning(RL)techniques[27,
RecentyearshaveseenarapidincreaseinthevolumeofHTTP- 30,43]tolearnacontrolpolicyforbitrateadaptationpurelythrough
basedvideostreamingtraffic[7,39].Concurrentwiththisincrease experience.Duringtraining,Pensievestartsknowingnothingabout
hasbeenasteadyriseinuserdemandsonvideoquality.Manystudies thetaskathand.ItthengraduallylearnstomakebetterABRde-
haveshownthatuserswillquicklyabandonvideosessionsifthe cisionsthroughreinforcement,intheformofrewardsignalsthat
qualityisnotsufficient,leadingtosignificantlossesinrevenuefor reflectvideoQoEforpastdecisions.
Pensieve’slearningtechniquesmineinformationabouttheactual
performanceofpastchoicestooptimizeitscontrolpolicyforthe
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed characteristicsofthenetwork.Forexample,Pensievecanlearnhow
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation muchplaybackbufferisnecessarytomitigatetheriskofrebuffering
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or inaspecificnetwork,basedonthenetwork’sinherentthroughput
republish,topostonserversortoredistributetolists,requirespriorspecificpermission variability.Oritcanlearnhowmuchtorelyonthroughputversus
and/orafee.Requestpermissionsfrompermissions@acm.org.
bufferoccupancysignals,orhowfarintothefuturetoplanitsdeci-
SIGCOMM’17,LosAngeles,CA,USA
sionsautomatically.Bycontrast,approachesthatusefixedcontrol
©2017Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
978-1-4503-4653-5/17/08...$15.00
DOI:http://dx.doi.org/10.1145/3098822.3098843 1ApensieveisadeviceusedinHarryPotter[38]toreviewmemories.
197

SIGCOMM’17,August21-25,2017,LosAngeles,CA,USA H.Maoetal.
rulesorsimplifiednetworkmodelsareunabletooptimizetheirbi-
Video Player Video
tratedecisionsbasedonallavailableinformationabouttheoperating Server
Throughput Estimate
environment. Throughput
Pensieverepresentsitscontrolpolicyasaneuralnetworkthat Rendered Predictor Chunk ABR
maps“raw”observations(e.g.,throughputsamples,playbackbuffer video chunks Info Controller
Playback
occupancy,videochunksizes)tothebitratedecisionforthenext Buffer Buffer Occupancy CDN
chunk.Theneuralnetworkprovidesanexpressiveandscalableway
toincorporatearichvarietyofobservationsintothecontrolpolicy.2
Figure1:AnoverviewofHTTPadaptivevideostreaming.
PensievetrainsthisneuralnetworkusingA3C[30],astate-of-the-art
actor-criticRLalgorithm.Wedescribethebasictrainingalgorithm
bitrateimpliesahigherqualityandthusalargerchunksize.Chunks
andpresentextensionsthatallowasingleneuralnetworkmodelto
acrossbitratesarealignedtosupportseamlessqualitytransitions,
generalizetovideoswithdifferentproperties,e.g.,thenumberof
i.e.,avideoplayercanswitchtoadifferentbitrateatanychunk
encodingsandtheirbitrates(§4).
boundarywithoutfetchingredundantbitsorskippingpartsofthe
Totrainitsmodels,Pensieveusessimulationsoveralargecorpus
video.
ofnetworktraces.Pensieveusesafastandsimplechunk-levelsimu-
Figure1illustratestheend-to-endprocessofstreamingavideo
lator.WhilePensievecouldalsotrainusingpacket-levelsimulations,
overHTTPtoday.Asshown,aplayerembeddedinaclientapplica-
emulations,ordatacollectedfromlivevideoclients(§6),thechunk-
tionfirstsendsatokentoavideoserviceproviderforauthentication.
levelsimulatorismuchfasterandallowsPensieveto“experience”
Theproviderrespondswithamanifestfilethatdirectstheclient
100hoursofvideodownloadsinonly10minutes.WeshowthatPen-
toaCDNhostingthevideoandliststheavailablebitratesforthe
sieve’ssimulatorfaithfullymodelsvideostreamingwithlivevideo
video.Theclientthenrequestsvideochunksonebyone,usingan
players,providedthatthetransportstackisconfiguredtoachieve
adaptivebitrate(ABR)algorithm.Thesealgorithmsuseavarietyof
closetothetruenetworkcapacity(§4.1).
differentinputs(e.g.,playbackbufferoccupancy,throughputmea-
WeevaluatePensieveusingafullsystemimplementation(§4.4).
surements,etc.)toselectthebitrateforfuturechunks.Aschunks
OurimplementationdeploysPensieve’sneuralnetworkmodelonan
aredownloaded,theyareplayedbacktotheclient;notethatplay-
ABRserver,whichvideoclientsquerytogetthebitratetouseforthe
backofagivenchunkcannotbeginuntiltheentirechunkhasbeen
nextchunk;clientrequestsincludeobservationsaboutthroughput,
downloaded.
bufferoccupancy,andvideoproperties.Thisdesignremovesthe
burdenofperformingneuralnetworkcomputationonvideoclients, Challenges: The policies employed by ABR algorithms heavily
whichmayhavelimitedcomputationpower,e.g.,TVs,mobilede- influencevideostreamingperformance.However,thesealgorithms
vices,etc.(§6). facefourprimarypracticalchallenges:
WecomparePensievetostate-of-the-artABRalgorithmsusing (1) Networkconditionscanfluctuateovertimeandcanvarysignifi-
abroadsetofnetworkconditions(bothwithtrace-basedemulation cantlyacrossenvironments.Thiscomplicatesbitrateselection
andinthewild)andQoEmetrics(§5.2).Wefindthatinallcon- asdifferentscenariosmayrequiredifferentweightsforinput
sideredscenarios,Pensieverivalsoroutperformsthebestexisting signals.Forexample,ontime-varyingcellularlinks,throughput
scheme,withaverageQoEimprovementsrangingfrom12%–25%. predictionisofteninaccurateandcannotaccountforsuddenfluc-
Additionally, ourresultsshowPensieve’sability togeneralizeto tuationsinnetworkbandwidth—inaccuratepredictionscanlead
unseennetworkconditionsandvideoproperties.Forexample,on tounderutilizednetworks(lowervideoquality)orinflateddown-
bothbroadbandandHSDPAnetworks,Pensievewasabletooutper- loaddelays(rebuffering).Toovercomethis,ABRalgorithms
formallexistingABRalgorithmsbytrainingsolelywithasynthetic mustprioritizemorestableinputsignalslikebufferoccupancy
dataset.Finally,wepresentresultswhichhighlightPensieve’slow inthesescenarios.
overheadandlackofsensitivitytosystemparameters,e.g.,inthe (2) ABRalgorithmsmustbalanceavarietyofQoEgoalssuchas
neuralnetwork(§5.4). maximizingvideoquality(i.e.,highestaveragebitrate),mini-
mizingrebufferingevents(i.e.,scenarioswheretheclient’splay-
2 BACKGROUND backbufferisempty),andmaintainingvideoqualitysmoothness
(i.e.,avoidingconstantbitratefluctuations).However,manyof
HTTP-basedadaptivestreaming(standardizedasDASH[2])isthe
thesegoalsareinherentlyconflicting[3,18,21].Forexample,
predominantformofvideodeliverytoday.Bytransmittingvideo
onnetworkswithlimitedbandwidth,consistentlyrequesting
usingHTTP,contentprovidersareabletoleverageexistingCDN
chunksencodedatthehighestpossiblebitratewillmaximize
infrastructureandmaintainsimplified(stateless)backends.Further,
quality,butmayincreaserebufferrates.Conversely,onvary-
HTTPiscompatiblewithamultitudeofclient-sideapplicationssuch
ingnetworks,choosingthehighestbitratethatthenetworkcan
aswebbrowsersandmobileapplications.
supportatanytimecouldleadtosubstantialqualityfluctuation,
InDASHsystems,videosarestoredonserversasmultiplechunks,
andhencedegradedsmoothness.Tofurthercomplicatematters,
eachofwhichrepresentsafewsecondsoftheoverallvideoplayback.
preferencesamongtheseQoEfactorsvarysignificantlyacross
Eachchunkisencodedatseveraldiscretebitrates,whereahigher
users[23,31,32,34].
2Afewpriorschemes[6,8,9,47]haveappliedRLtovideostreaming.Butthese (3) Bitrateselectionforagivenchunkcanhavecascadingeffects
schemesusebasic“tabular”RLapproaches[43].Asaresult,theymustrelyonsimplified
onthestateofthevideoplayer.Forexample,selectingahigh
networkmodelsandperformpoorlyinrealnetworkconditions.Wediscussthese
schemesfurtherin§5.4and§7. bitratemaydepletetheplaybackbufferandforcesubsequent
198

NeuralAdaptiveVideoStreamingwithPensieve SIGCOMM’17,August21-25,2017,LosAngeles,CA,USA
QoEmetric andaconservativethroughputestimatewhichnormalizesthede-
Reward
bandwidth faultthroughputpredictionwiththemaxpredictionerroroverthe
ABR agentNeural Networkbitrates
past5chunks.AstheMPCpapershows,andourresultsvalidate,
240P
bit rate robustMPC’sconservativethroughputpredictionsignificantlyim-
state 4 7 8 2 0 0 P P 720P provesperformanceoverdefaultMPC,andachievesahighlevel
buffer 1080P ofperformanceinmostcases(§5.2).However,heuristicslikero-
bustMPC’s throughput prediction require careful tuning and can
Client-side network and video player measurements
backfirewhentheirdesignassumptionsareviolated.
Figure 2: Applying reinforcement learning to bitrate adapta-
tion. Example1:Thefirstexampleconsidersascenarioinwhichthe
networkthroughputishighlyvariable.Figure3acomparesthenet-
chunkstobedownloadedatlowbitrates(toavoidrebuffering). workthroughputspecifiedbytheinputtracewiththethroughput
Additionally,agivenbitrateselectionwilldirectlyinfluencethe estimatesusedbyrobustMPC.Asshown,robustMPC’sestimates
nextdecisionwhensmoothnessisconsidered—ABRalgorithms areoverlycautious,hoveringaround2Mbpsinsteadoftheaverage
willbelessinclinedtochangebitrates. networkthroughputofroughly4.5Mbps.Theseinaccuratethrough-
(4) ThecontroldecisionsavailabletoABRalgorithmsarecoarse- putpredictionspreventrobustMPCfromreachinghighbitrateseven
grainedastheyarelimitedtotheavailablebitratesforagiven thoughtheoccupancyoftheplaybackbuffercontinuallyincreases.
video.Thus,thereexistscenarioswheretheestimatedthrough- Incontrast,theRL-generatedalgorithmisabletoproperlyassess
putfallsjustbelowonebitrate,butwellabovethenextavailable thehighaveragethroughput(despitefluctuations)andswitchtothe
bitrate.Inthesecases,theABRalgorithmmustdecidewhether highestavailablebitrateonceithasenoughcushionintheplayback
toprioritizehigherqualityortheriskofrebuffering. buffer.TheRL-generatedalgorithmconsideredherewastrainedon
alargecorpusofrealnetworktraces(§5.1),notthesynthetictrace
3 LEARNINGABRALGORITHMS inthisexperiment.Yet,itwasabletomaketheappropriatedecision.
Inthispaper,weconsideralearning-basedapproachtogenerating
Example2:Inoursecondexample,bothrobustMPCandtheRL-
ABRalgorithms.Unlikeapproacheswhichusepresetrulesinthe
generatedABRalgorithmoptimizeforanewQoEmetricwhichis
form of fine-tuned heuristics, our techniques attempt to learn an
gearedtowardsuserswhostronglypreferHDvideo.Thismetric
ABRpolicyfromobservations.Specifically,ourapproachisbasedon
assignshighrewardtoHDbitratesandlowrewardtoallotherbitrates
reinforcementlearning(RL).RLconsidersageneralsettinginwhich
(detailsinTable1),whilestillfavoringsmoothnessandpenalizing
anagentinteractswithanenvironment.Ateachtimestept,theagent
rebuffering.Tooptimizeforthismetric,anABRalgorithmshould
observessomestatest,andchoosesanactionat.Afterapplying
attempttobuildtheclient’splaybackbuffertoahighenoughlevel
theaction,thestateoftheenvironmenttransitionstost+1andthe
suchthattheplayercanswitchuptoandmaintainanHDbitratelevel.
a th g e en e t xp re e c c e te iv d e c s u a m r u e l w at a iv rd ed r i t s . c T ou h n e te g d oa r l ew of ar l d e : a E rni(cid:102)n (cid:80) g t ∞ = is 0 γ to tr m t (cid:103)a , x w im he iz r e e U tim si e ng sp t e h n is t a st p r p e r a o m a i c n h g ,t H h D ev v i i d d e e o o, p w la h y i e l r e c m an in m im a i x z i i m ng iz r e eb th u e ff a e m rin o g un ti t m o e f
γ ∈ (0,1]isafactordiscountingfuturerewards.
andbitratetransitions.However,performingwellinthisscenario
Figure2summarizeshowRLcanbeappliedtobitrateadaptation.
requireslongtermplanningsinceatanygiveninstant,thepenaltyof
Asshown,thedecisionpolicyguidingtheABRalgorithmisnot
selectingahigherbitrate(HDornot)maybeincurredmanychunks
handcrafted.Instead,itisderivedfromtraininganeuralnetwork.The
inthefuturewhenthebuffercannotsupportmultipleHDdownloads.
ABRagentobservesasetofmetricsincludingtheclientplayback
Figure3billustratesthebitrateselectionsmadebyeachofthese
bufferoccupancy,pastbitratedecisions,andseveralrawnetwork
algorithms,andtheeffectsthatthesedecisionshaveontheplayback
signals(e.g.,throughputmeasurements)andfeedsthesevaluestothe
buffer.NotethatrobustMPCandtheRL-generatedalgorithmwere
neuralnetwork,whichoutputstheaction,i.e.,thebitratetousefor
bothconfiguredtooptimizeforthisnewQoEmetric.Asshown,
thenextchunk.TheresultingQoEisthenobservedandpassedback
robustMPCisunabletoapplytheaforementionedpolicy.Instead,
totheABRagentasareward.Theagentusestherewardinformation
robustMPCmaintainsamedium-sizedplaybackbufferandrequests
totrainandimproveitsneuralnetworkmodel.Moredetailsabout
chunks at bitrates that fall between the lowest level (300 kbps)
thespecifictrainingalgorithmsweusedareprovidedin§4.2.
andthelowestHDlevel(1850kbps).Thereasonisthat,despite
To motivate learning-based ABR algorithms, we now provide
beingtunedtoconsiderahorizonoffuturechunksateverystep,
twoexampleswhereexistingtechniquesthatrelyonfixedheuristics
robustMPC fails to plan far enough into the future. In contrast,
canperformpoorly.Wechoosetheseexamplesforillustrativepur-
the RL-generated ABR algorithm is able to actively implement
poses.Wedonotclaimthattheyareindicativeoftheperformance
thepolicyoutlinedabove.Itquicklygrowstheplaybackbufferby
gainswithlearninginrealisticnetworkscenarios.Weperformthor-
requestingchunksat300kbps,andthenimmediatelyjumpstothe
oughquantitativeevaluationscomparinglearning-generatedABR
HDqualityof1850kbps;itisabletothenmaintainthislevelfor
algorithmstoexistingschemesin§5.2.
nearly80seconds,therebyensuringqualitysmoothness.
Intheseexamples,wecompareRL-generatedABRalgorithmsto
MPC[51].MPCusesboththroughputestimatesandobservations Summary:robustMPChasdifficulty(1)factoringthroughputfluc-
aboutbufferoccupancytoselectbitratesthatmaximizeagivenQoE tuationsandpredictionerrorsintoitsdecisions,and(2)choosingthe
metricacrossafuturechunkhorizon.HereweconsiderrobustMPC, appropriateoptimizationhorizon.Thesedeficienciesexistbecause
aversionofMPCthatisconfiguredtouseahorizonof5chunks, MPClacksanaccuratemodelofnetworkdynamics—thusitrelieson
199

| SIGCOMM’17,August21-25,2017,LosAngeles,CA,USA |     |     |     |     |     |     | H.Maoetal. |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- |
Pensieve robustMPC
|     |                   |     |     | 2               | Pensieve | robustMPC |     |     |
| --- | ----------------- | --- | --- | --------------- | -------- | --------- | --- | --- |
|     | )spbM(	etar	tiB 4 |     |     | )spbM(	etar	tiB |          |           |     |     |
1.6
3
1.2
2
0.8
|     | 1                 |                    |     | 0.4                  |          |           |     |     |
| --- | ----------------- | ------------------ | --- | -------------------- | -------- | --------- | --- | --- |
|     | 0                 |                    |     | 0                    |          |           |     |     |
|     |                   | Pensieve robustMPC |     |                      | Pensieve | robustMPC |     |     |
|     | )ces(	ezis	reffuB |                    |     | )ces(	ezis	reffuB 40 |          |           |     |     |
40
|     | 20  |          |     | 20  |     |        |     |     |
| --- | --- | -------- | --- | --- | --- | ------ | --- | --- |
|     | 0 0 | 30 60 90 | 120 | 0 0 | 40  | 80 120 | 160 |     |
True	bandwidth robustMPC	estimation 1.5 True	bandwidth robustMPC	estimation
|     | )spbM(	tuphguorhT 9 |     |     | )spbM(	tuphguorhT |     |     |     |     |
| --- | ------------------- | --- | --- | ----------------- | --- | --- | --- | --- |
|     | 7                   |     |     | 1.2               |     |     |     |     |
0.9
5
|     | 3    |            |     | 0.6 |     |            |     |     |
| --- | ---- | ---------- | --- | --- | --- | ---------- | --- | --- |
|     | 1    |            |     | 0.3 |     |            |     |     |
|     | 0 30 | 60 90      | 120 | 0   | 40  | 80 120     | 160 |     |
|     |      | Time	(sec) |     |     |     | Time	(sec) |     |     |
(b)HSDPAnetwork.
(a)Syntheticnetwork.
Figure3:Profilingbitrateselections,bufferoccupancy,andthroughputestimateswithrobustMPC[51]andPensieve.
simpleandsub-optimalheuristicssuchasconservativethroughput throughputtraces.Thesimulatorthendrainstheplaybackbufferby
predictionsandasmalloptimizationhorizon.Moregenerally,any thecurrentchunk’sdownloadtime,torepresentvideoplaybackdur-
ABRalgorithmthatreliesonfixedheuristicsorsimplifiedsystem ingthedownload,andaddstheplaybackdurationofthedownloaded
modelssuffersfromtheselimitations.Bycontrast,RL-generated chunktothebuffer.Thesimulatorcarefullykeepstrackofrebuffer-
algorithmslearnfromactualperformanceresultingfromdifferent ingeventsthatariseasthebufferoccupancychanges,i.e.,scenarios
decisions.Byincorporatingthisinformationintoaflexibleneural wherethechunkdownloadtimeexceedsthebufferoccupancyat
networkpolicy,RL-generatedABRalgorithmscanautomatically thestartofthedownload.Inscenarioswheretheplaybackbuffer
optimizefordifferentnetworkcharacteristicsandQoEobjectives. cannot accommodate video from an additional chunk download,
Pensieve’ssimulatorpausesrequestsfor500msbeforeretrying.3
4 DESIGN Aftereachchunkdownload,thesimulatorpassesseveralstateobser-
vationstotheRLagentforprocessing:thecurrentbufferoccupancy,
Inthissection,wedescribethedesignandimplementationofPen-
rebufferingtime,chunkdownloadtime,sizeofthenextchunk(at
sieve,asystemthatgeneratesRL-basedABRalgorithmsandapplies
allbitrates),andthenumberofremainingchunksinthevideo.We
themtovideostreamingsessions.Westartbyexplainingthetraining
describehowthisinputisusedbytheRLagentinmoredetailin
methodology(§4.1)andalgorithms(§4.2)underlyingPensieve.We
§4.2.Usingthischunk-levelsimulator,Pensievecan“experience”
thendescribeanenhancementtothebasictrainingalgorithm,which
100hoursofvideodownloadsinonly10minutes.
enablesPensievetosupportdifferentvideosusingasinglemodel
Thoughmodelingtheapplicationlayersemanticsofclientvideo
(§4.3).Finally,weexplaintheimplementationdetailsofPensieve
|     |     |     |     | players is | straightforward, | faithful simulation | is complicated | by  |
| --- | --- | --- | --- | ---------- | ---------------- | ------------------- | -------------- | --- |
andhowitapplieslearnedmodelstorealstreamingsessions(§4.4).
|     |     |     |     | intricacies | at the transport | layer. Specifically, | video players | may |
| --- | --- | --- | --- | ----------- | ---------------- | -------------------- | ------------- | --- |
notrequestfuturechunksassoonasachunkdownloadcompletes,
4.1 TrainingMethodology
e.g.,becausetheplaybackbufferisfull.Suchdelayscantrigger
ThefirststepofPensieveistogenerateanABRalgorithmusing theunderlyingTCPconnectiontoreverttoslowstart,abehavior
RL(§3).Todothis,Pensieverunsatrainingphaseinwhichthe knownasslow-start-restart[4].Slowstartmayinturnpreventthe
videoplayerfromfullyusingtheavailablebandwidth,particularly
| learning agent | explores a video | streaming environment. | Ideally, |     |     |     |     |     |
| -------------- | ---------------- | ---------------------- | -------- | --- | --- | --- | --- | --- |
trainingwouldoccurusingactualvideostreamingclients.However, forsmallchunksizes(lowbitrates).Thisbehaviormakessimulation
emulatingthestandardvideostreamingenvironmententailsusinga challenging as it inherently ties network throughput to the ABR
webbrowsertocontinuallydownloadvideochunks.Thisapproach algorithm being used, e.g., schemes that fill buffers quickly will
isslow,asthetrainingalgorithmmustwaituntilallofthechunksin experiencemoreslowstartphasesandthuslessnetworkutilization.
Toverifythisbehavior,weloadedthetestvideodescribedin§5.1
avideoarecompletelydownloadedbeforeupdatingitsmodel.
Toacceleratethisprocess,PensievetrainsABRalgorithmsina overanemulated6MbpslinkusingfourABRalgorithms,eachof
simplesimulationenvironmentthatfaithfullymodelsthedynamics whichcontinuallyrequestschunksatasinglebitrate.Weloadedthe
ofvideostreamingwithrealclientapplications.Pensieve’ssimulator videowitheachschemetwice,bothwithslow-start-restartenabled
maintainsaninternalrepresentationoftheclient’splaybackbuffer.
Foreachchunkdownload,thesimulatorassignsadownloadtime
thatissolelybasedonthechunk’sbitrateandtheinputnetwork 3ThisisthedefaultrequestretryrateusedbyDASHplayers[2].
200

NeuralAdaptiveVideoStreamingwithPensieve SIGCOMM’17,August21-25,2017,LosAngeles,CA,USA
|     |                   | 2.85	Mbps | 1.2	Mbps | 0.75	Mbps | 0.3Mbps |     |           |              | 1D-CNN | Actor network |            |     |
| --- | ----------------- | --------- | -------- | --------- | ------- | --- | --------- | ------------ | ------ | ------------- | ---------- | --- |
|     | )spbM(	tuphguorhT |           |          |           |         |     |           |              |        |               | policy     |     |
|     | 6                 |           |          |           |         |     | States    | t            |        |               | π (s , a ) |     |
|     |                   |           |          |           |         |     | Past chun | k throughput | 1D-CNN |               | θ t t      |     |
|     | 5                 |           |          |           |         |     | xt        | xt-1 xt-k+1  | 1D-CNN |               |            |     |
Past chunk download time
4
|     |     |     |     |     |     |     | τt               | τt-1 τt-k+1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ----------- | --- | --- | --- | --- |
|     | 3   |     |     |     |     |     | Next chunk sizes |             |     |     |     |     |
|     | 0   |     | 30  | 60  | 90  |     | n1               | n2          | nm  |     |     |     |
Time	(sec)
|     |     |     |     |     |     |     | Current buffer size |     | 1D-CNN |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------ | --- | --- | --- |
(a)TCPslowstartrestartenabled
|     |     |     |     |     |     |     |     |     | bt  | Critic network |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- |
1D-CNN
)spbM(	tuphguorhT 2.85	Mbps 1.2	Mbps 0.75	Mbps 0.3	Mbps Number of chunks left value
|     |     |     |     |     |     |     |     |     | 1D-CNN |     | vπθ(s t ) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --------- | --- |
|     | 6   |     |     |     |     |     |     |     | ct     |     |           |     |
Last chunk bit rate
lt
5
|     | 0   |     | 30  | 60  | 90  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Time	(sec) Figure5:TheActor-CriticalgorithmthatPensieveusestogen-
(b)TCPslowstartrestartdisabled erateABRpolicies(describedin§4.4).
Figure4:Profilingthethroughputusageper-chunkofcommod-
ityvideoplayerswithandwithoutTCPslowstartrestart. Policy:Uponreceivingst,Pensieve’sRLagentneedstotakean
actionat thatcorrespondstothebitrateforthenextvideochunk.
anddisabled.4Figure4showsthethroughputusageduringchunk Theagentselectsactionsbasedonapolicy,definedasaprobability
|     |     |     |     |     |     | distribution |     | over actions | π : π(st,at) | → [0,1]. | π(st,at) | is the |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ------------ | ------------ | -------- | -------- | ------ |
downloadsforeachbitrateinbothscenarios.Asshown,withslow-
|     |     |     |     |     |     | probabilitythatactionat |     |     | istakeninstatest.Inpractice,thereare |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | ------------------------------------ | --- | --- | --- |
start-restartenabled,thethroughputdependsonthebitrateofthe
intractablymany{state,action}pairs,e.g.,throughputestimatesand
chunk;ABRalgorithmsusinglowerbitrates(smallerchunksizes)
achievelessthroughputperchunk.However,throughputisconsistent bufferoccupanciesarecontinuousrealnumbers.Toovercomethis,
Pensieveusesaneuralnetwork(NN)[15]torepresentthepolicy
andmatchestheavailablebandwidth(6Mbps)fordifferentbitrates
withamanageablenumberofadjustableparameters,θ,whichwe
ifwedisableslow-start-restart.
refertoaspolicyparameters.Usingθ,wecanrepresentthepolicy
Pensieve’ssimulatorassumesthatthethroughputspecifiedby
asπ (st,at).NNshaverecentlybeenappliedsuccessfullytosolve
| thetraceisentirelyusedbyeachchunkdownload.Astheabove |     |     |     |     |     |     | θ   |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
resultsshow,thiscanbeachievedbydisablingslow-start-restarton large-scaleRLtasks[27,29,40].AnadvantageofNNsisthatthey
|     |     |     |     |     |     | do not | need | hand-crafted | features | and can be | applied directly | to  |
| --- | --- | --- | --- | --- | --- | ------ | ---- | ------------ | -------- | ---------- | ---------------- | --- |
thevideoserver.Disablingslow-start-restartcouldincreasetraffic
“raw”observationsignals.TheactornetworkinFigure5depictshow
burstiness,butrecentstandardseffortsaretacklingthesameproblem
PensieveusesanNNtorepresentanABRpolicy.Wedescribehow
forvideostreamingmoregracefullybypacingtheinitialburstfrom
wedesignthespecificarchitectureoftheNNin§5.3.
TCPfollowinganidleperiod[13,17].
Whileitispossibletouseamoreaccuratesimulator(e.g.,packet-
Policygradienttraining:Afterapplyingeachaction,thesimulated
level)totrainPensieve,intheend,nosimulationcancaptureall
|     |     |     |     |     |     | environmentprovidesthelearningagentwitharewardrt |     |     |     |     |     | forthat |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | ------- |
realworldsystemartifactswith100%accuracy.However,wefind chunk. Recall from §3 that the primary goal of the RL agent is
thatPensievecanlearnveryhighqualityABRalgorithms(§5.2) tomaximizetheexpectedcumulative(discounted)rewardthatit
usingimperfectsimulations,aslongasitexperiencesalargeenough
receivesfromtheenvironment.Thus,therewardissettoreflectthe
varietyofnetworkconditionsduringtraining.Thisisaconsequence
performanceofeachchunkdownloadaccordingtothespecificQoE
ofPensieve’sstronggeneralizationability(§5.3).
metricwewishtooptimize.See§5forexamplesofQoEmetrics.
Theactor-criticalgorithmusedbyPensievetotrainitspolicyis
4.2 BasicTrainingAlgorithm
|     |     |     |     |     |     | apolicygradientmethod |     |     | [44].Wehighlightthekeystepsofthe |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | -------------------------------- | --- | --- | --- |
We now describe our training algorithms. As shownin Figure 5, algorithm,focusingontheintuition.Thekeyideainpolicygradient
Pensieve’strainingalgorithmusesA3C[30],astate-of-the-artactor- methods is to estimate the gradient of the expected total reward
critic method which involves training two neural networks. The byobservingthetrajectoriesofexecutionsobtainedbyfollowing
detailedfunctionalitiesofthesenetworksareexplainedbelow. thepolicy.Thegradientofthecumulativediscountedrewardwith
respecttothepolicyparameters,θ,canbecomputedas[30]:
Inputs:Afterthedownloadofeachchunkt,Pensieve’slearning
|     |     |     |     |     |     |     |     |    |    |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ag e n t ta k es s t a te i n p u ts st = (x (cid:126)t , τ(cid:126) t, n(cid:126) t, b , c , lt ) t o i t s n e u r al n e t-  (cid:88)∞  (cid:102) (cid:103)
|     |     |     |     | t t |     |     |     |    |    |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
w o r k s. x(cid:126) is t h e n e t w o rk th rou g h p u t m e a s u r e m e n t s f o r t h e p as t k ∇ E  γtrt  =E ∇ logπ (s,a)Aπθ(s,a) . (1)
|                         | t   |                             |     |     |              |     | θ πθ |      |  πθ θ | θ   |     |     |
| ----------------------- | --- | --------------------------- | --- | --- | ------------ | --- | ---- | ----- | ------ | --- | --- | --- |
|                         |     |                             |     |     |              |     |      |  t=0 |       |     |     |     |
| videochunks;τ(cid:126)t |     | isthedownloadtimeofthepastk |     |     | videochunks, |     |      |       |        |     |     |     |
whichrepresentsthetimeintervalofthethroughputmeasurements; Aπθ(s,a)istheadvantagefunction,whichrepresentsthedifference
n(cid:126)t isavectorofmavailablesizesforthenextvideochunk;bt is intheexpectedtotalrewardwhenwedeterministicallypickaction
thecurrentbufferlevel;ct isthenumberofchunksremaininginthe ainstates,comparedwiththeexpectedrewardforactionsdrawn
| video;andlt |     | isthebitrateatwhichthelastchunkwasdownloaded. |     |     |     |             |     |                                              |     |     |     |     |
| ----------- | --- | --------------------------------------------- | --- | --- | --- | ----------- | --- | -------------------------------------------- | --- | --- | --- | --- |
|             |     |                                               |     |     |     | frompolicyπ |     | θ .Theadvantagefunctionencodeshowmuchbettera |     |     |     |     |
4InLinux,thenet.ipv4.tcp_slow_start_after_idleparametercanbe specificactioniscomparedtothe“averageaction”takenaccording
| usedtosetthisconfiguration. |     |     |     |     |     | tothepolicy. |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
201

| SIGCOMM’17,August21-25,2017,LosAngeles,CA,USA |     |     |     |     |     |     |     |     |     |     | H.Maoetal. |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
Inpractice,theagentsamplesatrajectoryofbitratedecisionsand Actor network
|     |     |     |     |     |     |     | l c | b τ x |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
usestheempiricallycomputedadvantageA(st,at),asanunbiased t t t t t
estimateofAπθ(st,at).Eachupdateoftheactornetworkparameter sezis knuhc txeN n p
|                             |        |          |                         |     |     |     |     | 1   |     |         | 1   |     |
| --------------------------- | ------ | -------- | ----------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
| θ followsthepolicygradient, |        |          |                         |     |     |     |     | n 2 |     | Softmax | p 2 |     |
|                             |        | (cid:88) |                         |     |     |     |     | 0   |     |         | 0   |     |
|                             | θ ←θ+α |          | ∇ logπ (st,at)A(st,at), |     |     | (2) |     |     |     |         |     |     |
|                             |        |          | θ θ                     |     |     |     |     | n   |     |         | p   |     |
|                             |        | t        |                         |     |     |     |     | 3   |     |         | 3   |     |
|                             |        |          |                         |     |     |     |     | 0   |     |         | 0   |     |
whereαisthelearningrate.Theintuitionbehindthisupdateruleisas Mask
follows.Thedirection∇ θ logπ θ (st,at)specifieshowtochangethe (1 1 0 1 0)
| policyparametersinordertoincreaseπ |                                                   |     |     | (st,at)(i.e.,theprobability |     |     |                                                        |     |     |     |     |     |
| ---------------------------------- | ------------------------------------------------- | --- | --- | --------------------------- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- |
|                                    |                                                   |     |     | θ                           |     |     | Figure6:Modificationtothestateinputandthesoftmaxoutput |     |     |     |     |     |
| ofactionat                         | atstatest).Equation2takesastepinthisdirection.The |     |     |                             |     |     |                                                        |     |     |     |     |     |
tosupportmultiplevideos.
sizeofthestepdependsonthevalueoftheadvantageforactionat
instatest.Thus,theneteffectistoreinforceactionsthatempirically
sentthattuple.Notethatthiscanhappenasynchronouslyamongall
leadtobetterreturns. agents,i.e.,thereisnolockingbetweenagents[36].
TocomputetheadvantageA(st,at)foragivenexperience,we
Choiceofalgorithm:Avarietyofdifferentalgorithmscouldbe
needanestimateofthevaluefunction,vπθ(s)—theexpectedtotal
rewardstartingatstates andfollowingthepolicyπ .Theroleof usedtotrainthelearningagentintheabstractRLframeworkde-
θ
thecriticnetworkinFigure5istolearnanestimateofvπθ(s)from scribed above (e.g., DQN [29], REINFORCE [44], etc.). In our
design,wechosetouseA3C[30]because(1)tothebestofour
| empirically | observed | rewards. | We follow | the standard | Temporal |     |     |     |     |     |     |     |
| ----------- | -------- | -------- | --------- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- |
knowledge,itisthestate-of-artandithasbeensuccessfullyapplied
Differencemethod[43]totrainthecriticnetworkparametersθv,
tomanyotherconcretelearningproblems[20,48,50];and(2)in
|        | (cid:88)    | (cid:16) |                           |     |     | (cid:17)2 |     |     |     |     |     |     |
| ------ | ----------- | -------- | ------------------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
| θv ←θv | −α (cid:48) | ∇ rt     | +γVπθ(st+1;θv)−Vπθ(st;θv) |     |     | , (3)     |     |     |     |     |     |     |
θv thevideostreamingapplication,theasynchronousparalleltraining
|     |     | t   |     |     |     |     | frameworksupportsonlinetraininginwhichmanyusersconcur- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- |
whereVπθ(·;θv)istheestimateofvπθ(·),outputbythecriticnet-
rentlysendtheirexperiencefeedbacktotheagent.Wealsocompare
work,andα(cid:48) isthelearningrateforthecritic.Foranexperience PensievewithprevioustabularQ-learningschemes[6]in§5.4.
| (st,at,rt,st+1)(i.e.,takeactionat |     |     | instatest,receiverewardrt,and |     |     |     |                                  |     |     |     |     |     |
| --------------------------------- | --- | --- | ----------------------------- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- |
|                                   |     |     |                               |     |     |     | 4.3 Enhancementformultiplevideos |     |     |     |     |     |
transitiontost+1),theadvantageA(st,at)cannowbeestimatedas
+γVπθ(st+1;θv)−Vπθ(st;θv).See[24]formoredetails.
rt Thebasicalgorithmdescribedin§4.2hassomepracticalissues.The
Itisimportanttonotethatthecriticnetworkmerelyhelpstotrain primarychallengeisthatvideoscanbeencodedatdifferentbitrate
theactornetwork.Post-training,onlytheactornetworkisrequired levelsandmayhavediversechunksizesduetovariablebitrateen-
toexecutetheABRalgorithmandmakebitratedecisions. coding[41],e.g.,chunksizesfor720pvideoarenotidenticalacross
Finally,wemustensurethattheRLagentexplorestheaction videos.Handlingthisvariationwouldrequireeachneuralnetwork
space adequately during training to discover good policies. One totakeavariablesizedsetofinputsandproduceavariablesizedset
common practice to encourage exploration is to add an entropy ofoutputs.Thenaivesolutiontosupportingabroadrangeofvideos
regularizationtermtotheactor’supdaterule[30];thiscanbecrit- istotrainamodelforeachpossiblesetofvideoproperties.Unfortu-
icalinhelpingthelearningagentconvergetoagoodpolicy[50]. nately,thissolutionisnotscalable.Toovercomethis,wedescribe
Concretely,wemodifyEquation2tobe, twoenhancementstothebasicalgorithmthatenablePensieveto
(cid:88) generateasinglemodeltohandlemultiplevideos(Figure6).
| ←θ+α | ∇   |          | (st,at)A(st,at)+β∇ |       | (·|st)), |     |     |     |     |     |     |     |
| ---- | --- | -------- | ------------------ | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
| θ    |     | θ logπ θ |                    | θ H(π | θ        | (4) |     |     |     |     |     |     |
First,wepickcanonicalinputandoutputformatsthatspanthe
t
maximumnumberofbitratelevelsweexpecttoseeinpractice.For
whereH(·)istheentropyofthepolicy(theprobabilitydistribution
|     |     |     |     |     |     |     | example, a range | of 13 levels covers | the | entire | DASH reference |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ------------------- | --- | ------ | -------------- | --- |
overactions)ateachtimestep.Thistermencouragesexploration
clientvideolist[11].Then,todeterminetheinputstateforaspecific
| bypushingθ | inthedirectionofhigherentropy.Theparameterβ |     |     |     |     | is  |     |     |     |     |     |     |
| ---------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
video,wetakethechunksizesandmapthemtotheindexwhichhas
settoalargevalueatthestartoftraining(toencourageexploration)
theclosestbitrate.Theremaininginputstates,whichpertaintothe
anddecreasesovertimetoemphasizeimprovingrewards(§4.4).
bitratesthatthevideodoesnotsupport,arezeroedout.Forexample,
Thedetailedderivationandpseudocodecanbefoundin[30](§4
inFigure6,chunksizes(n1,n2,n3)aremappedtothecorresponding
andAlgorithmS3).
indices,whiletheremaininginputvaluesarefilledwithzeroes.
Paralleltraining:Tofurtherenhanceandspeeduptraining,Pen- Thesecondchangepertainstohowtheoutputoftheactornet-
sievespawnsmultiplelearningagentsinparallel,assuggestedbythe
workisinterpreted.Foragivenvideo,weapplyamasktotheoutput
A3Cpaper[30].Bydefault,Pensieveuses16parallelagents.Each of the final softmax [5] layer in the actor network, such that the
learningagentisconfiguredtoexperienceadifferentsetofinput outputprobabilitydistributionisonlyoverthebitratesthatthevideo
parameters(e.g.,networktraces).However,theagentscontinually actually supports. Formally, the mask is presented by a 0-1 vec-
sendtheir {state,action,reward} tuplestoacentralagent,which tor[m1,m2,...,m ],andthemodifiedsoftmaxfortheNNoutput
k
| aggregates | them | to generate | a single | ABR algorithm | model. | For |                        |     |     |     |     |     |
| ---------- | ---- | ----------- | -------- | ------------- | ------ | --- | ---------------------- | --- | --- | --- | --- | --- |
|            |      |             |          |               |        |     | [z1,z2,...,z k ]willbe |     | z   |     |     |     |
eachsequenceoftuplesthatitreceives,thecentralagentusesthe = m ie i
|     |     |     |     |     |     |     |     | pi (cid:80) | ,   |     |     | (5) |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
m e zj
actor-criticalgorithmtocomputeagradientandperformagradient j j
descentstep(Equations(3)and(4)).Thecentralagentthenupdates wherepi isthenormalizedprobabilityforactioni.Withthismod-
theactornetworkandpushesoutthenewmodeltotheagentwhich ification,theoutputprobabilitiesarestillacontinuousfunctionof
202

NeuralAdaptiveVideoStreamingwithPensieve SIGCOMM’17,August21-25,2017,LosAngeles,CA,USA
thenetworkparameters.Thereasonisthatthemaskvalues {mi } (2) DomodelslearnedbyPensievegeneralizetonewnetworkcon-
areindependentofthenetworkparameters,andareonlyafunction ditionsandvideos?WefindthatPensieve’sABRalgorithmsare
oftheinputvideo.Asaresult,thestandardback-propagationof abletomaintainhighlevelsofperformancebothinthepresence
thegradientintheNNstillholdsandthetrainingtechniquesestab- ofnewnetworkconditionsandnewvideoproperties(§5.3).
lishedin§4.2canbeappliedwithoutmodification.Weevaluatethe (3) HowsensitiveisPensievetovariousparameterssuchastheneu-
effectivenessofthesemodificationsinmoredetailin§5.4. ralnetworkarchitectureandthelatencybetweenthevideoclient
andABRserver?Ourexperimentssuggestthatperformance
islargelyunaffectedbytheseparameters(Tables2and3).For
4.4 Implementation
example,applying100msRTTvaluesbetweenclientsandthe
TogenerateABRalgorithms,Pensievepassesk =8pastbandwidth
PensieveserverreducesaverageQoEbyonly3.5%(§5.4).
measurementstoa1Dconvolutionlayer(CNN)with128filters,
eachofsize4withstride1.Nextchunksizesarepassedtoanother 5.1 Methodology
1D-CNNwiththesameshape.Resultsfromtheselayersarethen
aggregatedwithotherinputsinahiddenlayerthatuses128neurons Network traces: To evaluate Pensieve and state-of-the-art ABR
toapplythesoftmaxfunction(Figure5).Thecriticnetworkuses algorithmsonrealisticnetworkconditions,wecreatedacorpusof
thesameNNstructure,butitsfinaloutputisalinearneuron(with networktracesbycombiningseveralpublicdatasets:abroadband
noactivationfunction).Duringtraining,weuseadiscountfactor datasetprovidedbytheFCC[10]anda3G/HSDPAmobiledataset
γ =0.99,whichimpliesthatcurrentactionswillbeinfluencedby collectedinNorway[37].TheFCCdatasetcontainsover1million
100futuresteps.Thelearningratesfortheactorandcriticarecon- throughputtraces,eachofwhichlogstheaveragethroughputover
figuredtobe10−4and10−3,respectively.Additionally,theentropy 2100seconds,ata5secondgranularity.Wegenerated1000traces
factorβiscontrolledtodecayfrom1to0.1over105iterations.We forourcorpus,eachwithadurationof320seconds,byconcatenating
keepallthesehyperparametersfixedthroughoutourexperiments. randomlyselectedtracesfromthe“Webbrowsing”categoryinthe
Whilesometuningisuseful,wefoundthatPensieveperformswell August2016collection.TheHSDPAdatasetcomprises30minutes
forawiderangeofhyperparametervalues.Thuswedidnotuse ofthroughputmeasurements,generatedusingmobiledevicesthat
sophisticatedhyperparametertuningmethods[14].Weimplemented werestreamingvideowhileintransit(e.g.,viabus,train,etc.).To
thisarchitectureusingTensorFlow[1].Forcompatibility,welever- matchthedurationoftheFCCtracesincludedinourcorpus,we
agedtheTFLearndeeplearninglibrary’sTensorFlowAPI[46]to generated1000traces(eachspanning320seconds)usingasliding
declaretheneuralnetworkduringbothtrainingandtesting. windowacrosstheHSDPAdataset.Toavoidscenarioswherebitrate
OncePensievehasgeneratedanABRalgorithmusingitssimula- selectionistrivial,i.e.,situationswherepickingthemaximumbitrate
tor,itmustapplythemodel’srulestorealvideostreamingsessions. isalwaystheoptimalsolution,orwherethenetworkcannotsupport
Todothis,PensieverunsonastandaloneABRserver,implemented anyavailablebitrateforanextendedperiod,weonlyconsidered
using the Python BaseHTTPServer. Client requests are modified originaltraceswhoseaveragethroughputislessthan6Mbps,and
toincludeadditionalinformationaboutthepreviouschunkdown- whose minimum throughput is above 0.2 Mbps. We reformatted
loadandthevideobeingstreamed(§4.2).Bycollectinginformation throughput traces from both datasets to be compatible with the
throughclientrequests,Pensieve’sserverandABRalgorithmcan Mahimahi [33] network emulation tool. Unless otherwise noted,
remainstatelesswhilestillbenefittingfromobservationsthatcan weusedarandomsampleof80%ofourcorpusasatrainingset
solelybecollectedinclientvideoplayers.Asclientrequestsforindi- forPensieve;weusedtheremaining20%asatestsetforallABR
vidualchunksarriveatthevideoserver,Pensievefeedstheprovided algorithms.Allinall,ourtestsetcomprisesofover30hoursof
observationsthroughitsactorNNmodelandrespondstothevideo networktraces.
clientwiththebitrateleveltouseforthenextchunkdownload;the
Adaptation algorithms: We compare Pensieve to the following
clientthencontactstheappropriateCDNtofetchthecorresponding
algorithmswhichcollectivelyrepresentthestate-of-the-artinbitrate
chunk.ItisimportanttonotethatPensieve’sABRalgorithmcould
adaptation:
alsooperatedirectlyinsidevideoplayers.Weevaluatetheoverhead
(1) Buffer-Based(BB):mimicsthebuffer-basedalgorithmdescribed
thataserver-sidedeploymenthasonvideoQoEin§5.4,anddiscuss
byHuangetal.[19]whichusesareservoirof5secondsanda
otherdeploymentmodelsinmoredetailin§6.
cushionof10seconds,i.e.,itselectsbitrateswiththegoalof
keepingthebufferoccupancyabove5seconds,andautomati-
5 EVALUATION callychoosesthehighestavailablebitrateifthebufferoccupancy
exceeds15seconds.
Inthissection,weexperimentallyevaluatePensieve.Ourexperi-
(2) Rate-Based(RB):predictsthroughputusingtheharmonicmean
mentscoverabroadsetofnetworkconditions(bothtrace-based
oftheexperiencedthroughputforthepast5chunkdownloads.
andinthewild)andQoEmetrics.Ourresultsanswerthefollowing
It then selects the highest available bitrate that is below the
questions:
predictedthroughput.
(1) HowdoesPensievecomparetostate-of-the-artABRalgorithms
(3) BOLA[41]:usesLyapunovoptimizationtoselectbitratessolely
intermsofvideoQoE?Wefindthat,inalloftheconsidered
consideringbufferoccupancyobservations.WeusetheBOLA
scenarios,Pensieveisabletorivaloroutperformthebestex-
implementationindash.js[2].
istingscheme,withaverageQoEimprovementsrangingfrom
(4) MPC[51]:usesbufferoccupancyobservationsandthroughput
12.1%–24.6%(§5.2);Figure7providesasummary.
predictions (computed in the same way as RB) to select the
203

| SIGCOMM’17,August21-25,2017,LosAngeles,CA,USA |     |     |     |     |     |     |     | H.Maoetal. |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- |
bitratewhichmaximizesagivenQoEmetricoverahorizonof Name bitrateutility(q(R)) rebuffer
penalty(µ)
| 5futurechunks. |     |     |     |     |     | QoElin | R   | 4.3 |
| -------------- | --- | --- | --- | --- | --- | ------ | --- | --- |
(5) robustMPC[51]:usesthesameapproachasMPC,butaccounts QoEloд log(R/Rmin) 2.66
0 . 3→ 1 , 0 . 7 5→ 2 , 1 . 2 → 3
forerrorsseenbetweenpredictedandobservedthroughputsby QoEhd 8
|     |     |     |     |     |     | 1.8 5 → | 12 , 2 . 8 5 → 1 5 , 4 . 3→ 20 |     |
| --- | --- | --- | --- | --- | --- | ------- | ------------------------------ | --- |
normalizingthroughputestimatesbythemaxerrorseeninthe
past5chunks. Table1:TheQoEmetricsweconsiderinourevaluation.Each
Note:MPCinvolvessolvinganoptimizationproblemforeachbitrate metricisavariantofEquation6.
decisionwhichmaximizestheQoEmetricoverthenext5video
|                                                      |     |     |     |     | (3) QoE | :ThismetricfavorsHighDefinition(HD)video.Itas- |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | ------- | ---------------------------------------------- | --- | --- |
| chunks.TheMPC[51]paperdescribesamethod,fastMPC,which |     |     |     |     |         | hd                                             |     |     |
signsalowqualityscoretonon-HDbitratesandahighquality
precomputesthesolutiontothisoptimizationproblemforaquan-
tizedsetofinputvalues(e.g.,buffersize,throughputprediction,etc.). scoretoHDbitrates.
BecausetheimplementationoffastMPCisnotpubliclyavailable, Theexactvaluesofq(Rn) forourbaselinevideoareprovidedin
Table1.Inthissection,wereporttheaverageQoEperchunk,i.e.,
weimplementedMPCusingourABRserverasfollows.Foreach
thetotalQoEmetricdividedbythenumberofchunksinthevideo.
bitratedecision,wesolvetheoptimizationproblemexactlyonthe
ABRserverbyenumeratingallpossibilitiesforthenext5chunks.
5.2 Pensievevs.ExistingABRalgorithms
Wefoundthatthecomputationtakesatmost27msfor6bitrate
levelsandhasnegligibleimpactonQoE. To evaluate Pensieve, we compared it with state-of-the-art ABR
Experimentalsetup:Wemodifieddash.js(version2.4)[2]tosup- algorithmsoneachQoEmetriclistedinTable1.Ineachexperiment,
Pensieve’sABRalgorithmwastrainedtooptimizefortheconsidered
porteachoftheaforementionedstate-of-the-artABRalgorithms.
QoEmetric,usingtheentiretrainingcorpusdescribedin§5.1;both
| For Pensieve | and both variants | of MPC, | dash.js was | configured |     |     |     |     |
| ------------ | ----------------- | ------- | ----------- | ---------- | --- | --- | --- | --- |
MPCvariantswerealsomodifiedtooptimizefortheconsidered
| to fetch | bitrate selection | decisions from | an ABR server | that im- |     |     |     |     |
| -------- | ----------------- | -------------- | ------------- | -------- | --- | --- | --- | --- |
QoEmetric.Forcomparison,wealsopresentresultsfortheoffline
| plemented | the corresponding | algorithm. | ABR servers | ran on the |     |     |     |     |
| --------- | ----------------- | ---------- | ----------- | ---------- | --- | --- | --- | --- |
optimalscheme,whichiscomputedusingdynamicprogramingwith
| same machine | as the client, | and requests | to these | servers were |     |     |     |     |
| ------------ | -------------- | ------------ | -------- | ------------ | --- | --- | --- | --- |
madeusingXMLHttpRequests.Allotheralgorithmsrandirectly completefuturethroughputinformation.Theofflineoptimalserves
asan(unattainable)upperboundontheQoEthatanomniscient
indash.js.TheDASHplayerwasconfiguredtohaveaplayback
policywithcompleteandperfectknowledgeofthefuturenetwork
buffercapacityof60seconds.Ourevaluationsusedthe“Envivio-
throughputcouldachieve.
Dash3”videofromtheDASH-246JavaScriptreferenceclient[11].
Figure7showstheaverageQoEthateachschemeachieveson
| This video | is encoded by | the H.264/MPEG-4 | codec | at bitrates |     |     |     |     |
| ---------- | ------------- | ---------------- | ----- | ----------- | --- | --- | --- | --- |
{300,750,1200,1850,2850,4300} ourentiretestcorpus.Figures8and9providemoredetailedresults
| in  |     | kbps | (which pertain | to video |     |     |     |     |
| --- | --- | ---- | -------------- | -------- | --- | --- | --- | --- |
intheformoffullCDFsforeachnetwork.Therearethreekeytake-
modesin{240,360,480,720,1080,1440}p).Additionally,thevideo
awaysfromtheseresults.First,wefindthatPensieveeithermatches
wasdividedinto48chunksandhadatotallengthof193seconds.
|            |                   |               |           |          | or exceeds | the performance | of the best existing | ABR algorithm |
| ---------- | ----------------- | ------------- | --------- | -------- | ---------- | --------------- | -------------------- | ------------- |
| Thus, each | chunk represented | approximately | 4 seconds | of video |            |                 |                      |               |
oneachQoEmetricandnetworkconsidered.Theclosestcompet-
playback.Inoursetup,theclientvideoplayerwasaGoogleChrome
browser(version53)andthevideoserver(Apacheversion2.4.7) ingschemeisrobustMPC;thisshowstheimportanceoftuning,as
withoutrobustMPC’sconservativethroughputestimates,MPCcan
ranonthesamemachineastheclient.WeusedMahimahi[33]to
becometooaggressive(relyingontheplaybackbuffer)andperform
emulatethenetworkconditionsfromourcorpusofnetworktraces,
|                                                     |     |     |     |     | worsethanevenanaiverate-basedscheme.ForQoE |     |     | ,whichwas |
| --------------------------------------------------- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --------- |
| alongwithan80msRTT,betweentheclientandserver.Unless |     |     |     |     |                                            |     |     | lin       |
consideredintheMPCpaper[51],theaverageQoEforPensieveis
otherwisenoted,allexperimentswereperformedonAmazonEC2
t2.2xlargeinstances. 15.5%higherthanrobustMPContheFCCbroadbandnetworktraces.
ThegapbetweenPensieveandrobustMPCwidensto18.9%and
QoEmetrics:Thereexistssignificantvarianceinuserpreferences
|     |     |     |     |     | 24.6%forQoE | andQoE | .Theresultsarequalitativelysimilar |     |
| --- | --- | --- | --- | --- | ----------- | ------ | ---------------------------------- | --- |
|     |     |     |     |     |             | loд    | hd                                 |     |
for video streaming QoE [23, 31, 32, 34]. Thus, we consider a fortheNorwayHSDPAnetworktraces.
varietyofQoEmetrics.WestartwiththegeneralQoEmetricused Second,weobservethattheperformanceofexistingABRalgo-
byMPC[51],whichisdefinedas
rithmsstruggletooptimizefordifferentQoEobjectives.Thereason
(cid:88)N (cid:88)N N(cid:88)−1(cid:12) (cid:12) (cid:12) (cid:12) isthatthesealgorithmsemployfixedcontrollaws,eventhoughop-
| QoE= |     |     | (cid:12) (cid:12)q(Rn+1)−q(Rn)(cid:12) |     |     |     |     |     |
| ---- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- |
q(Rn)−µ Tn − (cid:12) (6) timizingfordifferentQoEobjectivesrequiresinherentlydifferent
|     |     |     | (cid:12) | (cid:12) |     |     |     |     |
| --- | --- | --- | -------- | -------- | --- | --- | --- | --- |
n=1 n=1 n=1 ABRstrategies.Forexample,forQoE ,sincethemarginalim-
loд
foravideowithNchunks.Rn representsthebitrateofchunkn and provementinuser-perceivedqualitydiminishesathigherbitrates,
theoptimalstrategyistoavoidjumpingtohighbitratelevelswhen
| q(Rn)mapsthatbitratetothequalityperceivedbyauser.Tn |     |     |     | repre- |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | ------ | --- | --- | --- | --- |
sentstherebufferingtimethatresultsfromdownloadingchunkn at the risk of rebuffering is high. However, to optimize forQoE lin ,
bitrateRn,whilethefinaltermpenalizeschangesinvideoqualityto theABRalgorithmneedstobemoreaggressive.Pensieveisable
favorsmoothness. to automatically learn these policies and thus, performance with
Weconsiderthreechoicesofq(Rn): Pensieveremainsconsistentlyhighasconditionschange.
(1) :q(Rn)=Rn.ThismetricwasusedbyMPC[51]. The results forQoE further illustrate this point. Recall that
| QoE lin |     |     |     |     |     | hd  |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- |
:q(Rn)=log(R/Rmin).Thismetriccapturesthenotion
(2) QoE loд QoE hd favorsHDvideo,assigningthehighestutilitytothetopthree
that,forsomeusers,themarginalimprovementinperceived bitratesavailableforourtestvideo(seeTable1).Asdiscussedin
qualitydecreasesathigherbitratesandwasusedbyBOLA[41]. §3,optimizingforQoE requireslongertermplanningthanthe
hd
204

NeuralAdaptiveVideoStreamingwithPensieve SIGCOMM’17,August21-25,2017,LosAngeles,CA,USA
Buffer-based Rate-based BOLA MPC robustMPC Pensieve Buffer-based Rate-based BOLA MPC robustMPC Pensieve
1
| 1   |     |     |     |     |     | EoQ	egarevA	dezilamroN |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- |
EoQ	egareva	dezilamroN
| 0.8 |     |     |     |     |     | 0.8 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.6 |     |     |     |     |     | 0.6 |     |     |     |     |     |
| 0.4 |     |     |     |     |     | 0.4 |     |     |     |     |     |
| 0.2 |     |     |     |     |     | 0.2 |     |     |     |     |     |
0
0
|     | QoE_lin |                        | QoE_log | QoE_hd |     |     | QoE_lin |                       | QoE_log |     | QoE_hd |
| --- | ------- | ---------------------- | ------- | ------ | --- | --- | ------- | --------------------- | ------- | --- | ------ |
|     |         | (a)FCCbroadbanddataset |         |        |     |     |         | (b)NorwayHSDPAdataset |         |     |        |
Figure7:ComparingPensievewithexistingABRalgorithmsonbroadbandand3G/HSDPAnetworks.TheQoEmetricsconsidered
arepresentedinTable1.ResultsarenormalizedagainsttheperformanceofPensieve.Errorbarsspan±onestandarddeviationfrom
theaverage.
| 1   |     |     |              | 1   |     |              |     | 1   |     |     |              |
| --- | --- | --- | ------------ | --- | --- | ------------ | --- | --- | --- | --- | ------------ |
|     |     |     |              |     |     | Buffer-based |     |     |     |     | Buffer-based |
|     |     |     | Buffer-based |     |     |              |     |     |     |     | Rate-based   |
| FDC |     |     | Rate-based   | FDC |     | Rate-based   |     | FDC |     |     |              |
| 0.5 |     |     |              | 0.5 |     | BOLA         |     | 0.5 |     |     | BOLA         |
BOLA
|     |     |     | MPC |     |     | MPC       |     |     |     |     | MPC       |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --------- |
|     |     |     |     |     |     | robustMPC |     |     |     |     | robustMPC |
robustMPC
|     |             |     | Pensieve        |      |             | Pensieve        |     |     |     |             | Pensieve        |
| --- | ----------- | --- | --------------- | ---- | ----------- | --------------- | --- | --- | --- | ----------- | --------------- |
|     |             |     | Offline	optimal |      |             | Offline	optimal |     |     |     |             | Offline	optimal |
| 0   |             |     |                 | 0    |             |                 |     | 0   |     |             |                 |
|     | -0.5 0.5    | 1.5 | 2.5             | -0.5 | 0.5         | 1.5             | 2.5 |     | -1  | 2 5         | 8 11 14         |
|     | Average	QoE |     |                 |      | Average	QoE |                 |     |     |     | Average	QoE |                 |
|     | (a)QoElin   |     |                 |      | (b)QoEloд   |                 |     |     |     | (c)QoEhd    |                 |
Figure8:ComparingPensievewithexistingABRalgorithmsontheQoEmetricslistedinTable1.ResultswerecollectedontheFCC
broadbanddataset.AverageQoEvaluesarelistedforeachABRalgorithm.
| 1   |     |     |     | 1   |     |     |     | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Buffer-based
|     |     |     | Buffer-based |     |     | Buffer-based |     |     |     |     |            |
| --- | --- | --- | ------------ | --- | --- | ------------ | --- | --- | --- | --- | ---------- |
|     |     |     | Rate-based   |     |     | Rate-based   |     |     |     |     | Rate-based |
| FDC |     |     |              | FDC |     |              |     | FDC |     |     |            |
| 0.5 |     |     | BOLA         | 0.5 |     | BOLA         |     | 0.5 |     |     | BOLA       |
|     |     |     | MPC          |     |     | MPC          |     |     |     |     | MPC        |
|     |     |     | robustMPC    |     |     | robustMPC    |     |     |     |     | robustMPC  |
|     |     |     | Pensieve     |     |     |              |     |     |     |     | Pensieve   |
Pensieve
|      |             |     | Offline	optimal |      |             | Offline	optimal |     |     |      |             | Offline	optimal |
| ---- | ----------- | --- | --------------- | ---- | ----------- | --------------- | --- | --- | ---- | ----------- | --------------- |
| 0    |             |     |                 | 0    |             |                 |     | 0   |      |             |                 |
| -0.5 | 0.5         | 1.5 | 2.5             | -0.5 | 0.5         | 1.5             | 2.5 |     | -1 2 | 5           | 8 11 14         |
|      | Average	QoE |     |                 |      | Average	QoE |                 |     |     |      | Average	QoE |                 |
|      | (a)QoElin   |     |                 |      | (b)QoEloд   |                 |     |     |      | (c)QoEhd    |                 |
Figure 9: Comparing Pensieve with existing ABR algorithms on the QoE metrics listed in Table 1. Results were collected on the
NorwayHSDPAdataset.AverageQoEvaluesarelistedforeachABRalgorithm.
other two QoE metrics. When network bandwidth is inadequate, QoE breakdown: To better understand the QoE gains obtained
theABRalgorithmshouldbuildtheplaybackbufferasquicklyas byPensieve,weanalyzedPensieve’sperformanceontheindivid-
possibleusingthelowestavailablebitrate.Oncethebufferislarge ualtermsinourgeneralQoEdefinition(Equation6).Specifically,
enough,itshouldthenmakeadirecttransitiontothelowestHD Figure10comparesPensievetostate-of-the-artABRalgorithmsin
quality(bypassingintermediatebitrates).However,buildingbuffers termsoftheutilityfromtheaverageplaybackbitrate,thepenalty
toalevelwhichcircumventsrebufferingandmaintainssufficient fromrebuffering,andthepenaltyfromswitchingbitrates(i.e.,the
smoothnessrequiresalotofforesight.Asillustratedbytheexample smoothnesspenalty).Inotherwords,agivenscheme’sQoEcanbe
inFigure3b,Pensieveisabletolearnsuchapolicywithzerotuning computedbysubtractingtherebufferingpenaltyandsmoothness
ordesignerinvolvement,whileotherschemessuchasrobustMPC penaltyfromthebitrateutility.Intheinterestofspace,Figure10
havedifficultyoptimizingsuchlongtermstrategies. combinestheresultsfortheFCCbroadbandandHSDPAtraces.
Finally, Pensieve’s performance is within 9.6%–14.3% of the Asshown,alargeportionofPensieve’sperformancegainscome
offlineoptimalschemeacrossallnetworktracesandQoEmetrics. fromitsabilitytolimitrebufferingacrossthedifferentnetworksand
Recallthattheofflineoptimalperformancecannotbeachievedin QoEmetricsconsidered.Pensievereducesrebufferingby10.6%–
practice as it requires complete knowledge of future throughput. 32.8%acrossthethreemetricsbybuildingupsufficientbufferto
Thisshowsthatthereislikelytobelittleroomforanyonlinealgo- handlethenetwork’sthroughputfluctuations.Additionally,Figure6
rithm(withoutfutureknowledge)toimproveoverPensieveinthese illustrates that Pensieve does not outperform all state-of-the-art
scenarios.WerevisitthequestionofPensieve’soptimalityin§5.4. schemesoneveryQoEfactor.Instead,Pensieveisabletobalance
205

| SIGCOMM’17,August21-25,2017,LosAngeles,CA,USA |            |          |                    |     |      |           | H.Maoetal. |     |
| --------------------------------------------- | ---------- | -------- | ------------------ | --- | ---- | --------- | ---------- | --- |
| Buffer-based                                  | Rate-based | BOLA MPC | robustMPC Pensieve |     |      |           |            |     |
|                                               |            |          |                    |     | BOLA | robustMPC | Pensieve   |     |
| 1.4                                           |            |          |                    | 2.5 |      |           |            |     |
1.2
| eulav	egarevA |     |     |     | EoQ	egarevA | 2   |     |     |     |
| ------------- | --- | --- | --- | ----------- | --- | --- | --- | --- |
1
| 0.8 |     |     |     | 1.5 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.6 |     |     |     |     | 1   |     |     |     |
0.4
0.5
0.2
0
0
Bitrate	utility Rebuffering	penalty Smoothness	penalty LTE Public	WiFi International	link
(a)QoElin Figure11:ComparingPensievewithexistingABRalgorithms
Buffer-based Rate-based BOLA MPC robustMPC Pensieve inthewild.ResultsarefortheQoE metricandwerecollected
lin
1.4
|     |     |     |     | on the Verizon | LTE cellular | network, a | public WiFi network, |     |
| --- | --- | --- | --- | -------------- | ------------ | ---------- | -------------------- | --- |
1.2
eulav	egarevA andthewideareanetworkbetweenShanghaiandBoston.Bars
1
listaveragesanderrorbarsspan±onestandarddeviationfrom
0.8
theaverage.
0.6
0.4
| 0.2 |     |     |     | laptop,contactedavideoserverrunningonadesktopmachinelo- |     |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- |
0
catedinBoston.WeconsideredasubsetoftheABRalgorithmslisted
|     | Bitrate	utility | Rebuffering	penalty | Smoothness	penalty |                                                    |     |     |     |     |
| --- | --------------- | ------------------- | ------------------ | -------------------------------------------------- | --- | --- | --- | --- |
|     |                 | (b)QoEloд           |                    | in§5.1:BOLA,robustMPC,andPensieve.Oneachnetwork,we |     |     |     |     |
loadedourtestvideotentimeswitheachscheme,randomlyselecting
| Buffer-based | Rate-based | BOLA MPC | robustMPC Pensieve |     |     |     |     |     |
| ------------ | ---------- | -------- | ------------------ | --- | --- | --- | --- | --- |
theorderamongthem.ThePensieveABRalgorithmevaluatedhere
7
| 6   |     |     |     | wassolelytrainedusingthebroadbandandHSDPAtracesinour |     |     |     |     |
| --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- |
eulav	egarevA
| 5   |     |     |     | corpus.However,evenonthesenewnetworks,Pensievewasable |     |     |                   |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | ----------------- | --- |
| 4   |     |     |     | tooutperformtheotherschemesontheQoE                   |     |     | metric(Figure11). |     |
| 3   |     |     |     |                                                       |     |     | lin               |     |
ExperimentswiththeotherQoEmetricsshowsimilarresults.
2
1
| 0   |     |     |     | Trainingwithasyntheticdataset:CanwetrainPensievewithout |     |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- |
Bitrate	utility Rebuffering	penalty Smoothness	penalty anyrealnetworkdata?Learningfromsyntheticdataalonewould
(c)QoEhd
|     |     |     |     | of course | be undesirable, | but we use it | as a challenging | test of |
| --- | --- | --- | --- | --------- | --------------- | ------------- | ---------------- | ------- |
Figure10:ComparingPensievewithexistingABRalgorithms Pensieve’sabilitytogeneralize.
byanalyzingtheirperformanceontheindividualcomponents Wedesignadatasettocoverarelativelybroadsetofnetwork
| in the general | QoE definition | (Equation | 6). Results consider |     |     |     |     |     |
| -------------- | -------------- | --------- | -------------------- | --- | --- | --- | --- | --- |
conditions,withaveragethroughputsrangingfrom0.2Mbpsto4.3
boththebroadbandandHSDPAnetworks.Errorbarsspan±
Mbps.Specifically,thedatasetwasgeneratedusingaMarkovian
onestandarddeviationfromtheaverage. modelinwhicheachstaterepresentedanaveragethroughputinthe
aforementionedrange.Statetransitionswereperformedata1second
eachfactorinawaythatoptimizestheQoEmetric.Forexample,to granularityandfollowedageometricdistribution(makingitmore
| optimizeQoE | hd ,Pensieveachievesthebestbitrateutilitybyalways |     |     |     |     |     |     |     |
| ----------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
likelytotransitiontoanearbyaveragethroughput).Eachthroughput
tryingtodownloadchunksatHDbitrates,whilewhenoptimizingfor
valuewasthendrawnfromaGaussiandistributioncenteredaround
| QoE orQoE | ,Pensievefocusesonachievingsufficientlyhigh |     |     |     |     |     |     |     |
| --------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
lin loд theaveragethroughputforthecurrentstate,withvarianceuniformly
bitrateswiththesmallestamountofrebufferingandbitrateswitches.
distributedbetween0.05and0.5.
WethenusedPensievetocomparetwoABRalgorithmsonthe
5.3 Generalization
testdatasetdescribedabove(i.e.,acombinationoftheHSDPAand
Intheexperimentsabove,Pensievewastrainedwithasetoftraces
broadbanddatasets):onetrainedsolelyusingthesyntheticdataset,
collectedonthesamenetworksthatwereusedduringtesting;note andanothertrainedexplicitlyonbroadbandandHSDPAnetwork
thatnotesttracesweredirectlyincludedinthetrainingset.How- traces. Figure 12 illustrates our results for all three QoE metrics
ever,inpractice,Pensieve’sABRalgorithmscouldencounternew listedinTable1.Asshown,Pensieve’sABRalgorithmthatwas
networks,withdifferentconditions(andthus,withdifferentoptimal
trainedonthesyntheticdatasetisabletogeneralizeacrossthesenew
strategies).ToevaluatePensieve’sabilitytogeneralizetonewnet-
networks,outperformingrobustMPCandachievingaverageQoE
workconditions,weconducttwoexperiments.First,weevaluate valueswithin1.6%–10.8%oftheABRalgorithmtraineddirectly
Pensieveinthewildontworealnetworks.Second,wetakegeneral- onthetestnetworks.Theseresultssuggestthat,inpractice,Pen-
itytotheextremeandshowhowPensievecanbetrainedtoperform sievewilllikelybeabletogeneralizetoabroadrangeofnetwork
wellacrossmultipleenvironmentsusingapurelysyntheticdataset. conditionsencounteredbyitsclients.
Realworldexperiments:WeevaluatedPensieveandseveralstate-
of-the-artABRalgorithmsinthewildusingthreedifferentnetworks: Multiplevideos:Asafinaltestofgeneralization,weevaluatedPen-
sieve’sabilitytogeneralizeacrossmultiplevideoproperties.Todo
theVerizonLTEcellularnetwork,apublicWiFinetworkatalo-
this,wetrainedasingleABRmodelon1,000syntheticvideosusing
calcoffeeshop,andthewideareanetworkbetweenShanghaiand
Boston.Intheseexperiments,aclient,runningonaMacbookPro thetechniquesdescribedin§4.3.Thenumberofavailablebitrates
206

NeuralAdaptiveVideoStreamingwithPensieve SIGCOMM’17,August21-25,2017,LosAngeles,CA,USA
| 1   |     |           |     | 1   |     |           |     |     | 1   |     |           |     |
| --- | --- | --------- | --- | --- | --- | --------- | --- | --- | --- | --- | --------- | --- |
| 0.8 |     |           |     | 0.8 |     |           |     | 0.8 |     |     |           |     |
| 0.6 |     |           |     | 0.6 |     |           |     | 0.6 |     |     |           |     |
| FDC |     |           |     | FDC |     |           |     | FDC |     |     |           |     |
| 0.4 |     | robustMPC |     | 0.4 |     | robustMPC |     | 0.4 |     |     | robustMPC |     |
Pensieve	(synthetic) Pensieve	(synthetic) Pensieve	(synthetic)
| 0.2  |             | Pensieve |     | 0.2  |             | Pensieve |     | 0.2 |      |             | Pensieve |     |
| ---- | ----------- | -------- | --- | ---- | ----------- | -------- | --- | --- | ---- | ----------- | -------- | --- |
| 0    |             |          |     | 0    |             |          |     |     | 0    |             |          |     |
| -0.5 | 0.5         | 1.5      | 2.5 | -0.5 | 0.5         | 1.5      | 2.5 |     | -1 2 | 5           | 8 11     | 14  |
|      | Average	QoE |          |     |      | Average	QoE |          |     |     |      | Average	QoE |          |     |
|      | (a)QoElin   |          |     |      | (b)QoEloд   |          |     |     |      | (c)QoEhd    |          |     |
Figure12:ComparingtwoABRalgorithmswithPensieveonthebroadbandandHSDPAnetworks:onealgorithmwastrainedon
syntheticnetworktraces,whiletheotherwastrainedusingasetoftracesdirectlyfromthebroadbandandHSDPAnetworks.Results
areaggregatedacrossthetwodatasets.
|     | 1       |     |     |     |     |     |     | 1   |     |                    |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- |
|     | 0.8     |     |     |     |     |     | 0.8 |     |     |                    |     |     |
|     |         |     |     |     |     |     | 0.6 |     |     | Tabular	Q-learning |     |     |
|     | FDC 0.6 |     |     |     |     |     | FDC |     |     |                    |     |     |
Pensieve	1	past	chunk
|     | 0.4 |     |                       |     |     |     | 0.4 |     |     |                         |     |     |
| --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- |
|     |     |     | Multi-video	Pensieve  |     |     |     |     |     |     | Pensieve	8	past	chunks  |     |     |
|     | 0.2 |     |                       |     |     |     | 0.2 |     |     |                         |     |     |
|     |     |     | Single-video	Pensieve |     |     |     |     |     |     | Pensieve	16	past	chunks |     |     |
0
0
|     | -0.5 | 0.5         | 1.5 | 2.5 |     |     |     | 0   | 1           |     | 2   |     |
| --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
|     |      | Average	QoE |     |     |     |     |     |     | Average	QoE |     |     |     |
Figure13:ComparingABRalgorithmstrainedacrossmultiple Figure 14:Comparing existingtabular RLschemes withvari-
videoswiththosetrainedexplicitlyonthetestvideo.Themea- ants of Pensieve that consider different numbers of past
suringmetricisQoE lin . throughout measurements. Results are evaluated with QoE lin
foreachvideowasrandomlyselectedfrom[3,10],5andthevalue fortheHSDPAnetwork.
foreachbitratewasthenrandomlychosenfrom{200,300,450,750,
|     |     |     |     |     |     | Comparison | to  | tabular | RL schemes: | A   | few recent | schemes [6, |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | ----------- | --- | ---------- | ----------- |
1200,1850,2350,2850,3500,4300}kbps.Thenumberofvideochunks
|     |     |     |     |     |     | 8, 9, 47] | have | applied “tabular” |     | RL to video | streaming. | Tabular |
| --- | --- | --- | --- | --- | --- | --------- | ---- | ----------------- | --- | ----------- | ---------- | ------- |
foreachvideowasrandomlygeneratedfrom[20,100];chunksizes
methodsrepresentthemodeltobelearnedasatable,withseparate
werecomputedbymultiplyingthestandard4-secondchunksize
|     |     |     |     |     |     | entries for | all states | (e.g., | client | observations) | and | actions (e.g., |
| --- | --- | --- | --- | --- | --- | ----------- | ---------- | ------ | ------ | ------------- | --- | -------------- |
withGaussiannoise∼N(1,0.1).Thus,thesevideosdivergeonnu-
bitratedecisions).Tabularmethodsdonotscaletolargestate/action
merouspropertiesincludingthebitrateoptions(boththenumberof
|     |     |     |     |     |     | spaces. As | a result, | such | schemes | are forced | to restrict | the state |
| --- | --- | --- | --- | --- | --- | ---------- | --------- | ---- | ------- | ---------- | ----------- | --------- |
optionsandvalueofeach),numberofchunks,chunksizesandvideo
|     |     |     |     |     |     | space by | making | simplified | (and | unrealistic) | assumptions | about |
| --- | --- | --- | --- | --- | --- | -------- | ------ | ---------- | ---- | ------------ | ----------- | ----- |
duration.Importantly,weensuredthatnoneofthegeneratedtraining
networkbehavior.Forexample,themostrecenttabularRLscheme
videoshadtheexactsamebitrateoptionsasthetestingvideo.
forABR[6]assumesnetworkthroughputisMarkovian,i.e.,the
Wecomparethisnewlytrainedmodeltotheoriginalmodel,which
futurebandwidthdependsonlyonthethroughputobservedinthe
wastrainedsolelyonthe“EnvivioDash3”videodescribedin§5.1
lastchunkdownload.
| (thetestvideo).OurresultsmeasureQoE |     |     |     | onbroadbandandHS- |     |                                                     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | ----------------- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                                     |     |     | lin |                   |     | TocomparetheseapproacheswithPensieve,weimplementeda |     |     |     |     |     |     |
DPAnetworktracesandaredepictedinFigure13.Asshown,the
tabularRLschemewithQ-learning[29].Ourimplementationismod-
generalizedABRalgorithmtrainedacrossmultiplevideosisable
eledafterthedesignin[6].Thestatespaceisthesameasdescribed
| toachieveaverageQoE |     | lin valueswithin3.2%ofthemodeltrained |     |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in§4.2exceptthatthepastbandwidthmeasurementisrestricted
explicitlyonthetestvideo.Theseresultssuggestthatinpractice,
toonly1sample(asin[6]).Thepastbandwidthmeasurementand
PensieveserverscanbeconfiguredtouseasmallnumberofABR
bufferoccupancyarequantizedwith0.5Mbpsand1secondgranu-
algorithmstoimprovestreamingforadiversesetofvideos.
larityrespectively.Ourquantizationismorefine-grainedthanthat
5.4 PensieveDeepDive usedin[6];wefoundthatthisresultedinbetterperformanceinour
experiments.(Notethatsimulationresultsin[6]usedsynthetically
Inthissection,wedescribemicrobenchmarksthatprovideadeeper
generatednetworktraceswiththeMarkovproperty.)
understandingofPensieveandshedlightonsomepracticalconcerns Figure14showsasignificantperformancegap(46.3%)between
withusingRL-generatedABRalgorithms.Webeginbycomparing the tabular scheme and Pensieve. This result shows that simple
Pensieve’sRLalgorithmtotabularRLschemes,whichareusedby
networkmodels(e.g.,Markoviandynamics)failtocapturetheintri-
somepreviousproposalsforapplyingRLtovideostreaming.We
caciesofrealnetworks.UnliketabularRLmethods,Pensievecan
thenanalyzehowrobustPensieveistovaryingsystemparameters
incorporatealargeamountofthroughputhistoryintoitsstatespace
(e.g.,neuralnetworkhyperparameters,client-to-ABRserverlatency) tooptimizeforactualnetworkcharacteristics.
andevaluateitstrainingtime.Finally,weconductexperimentsto Tobetterunderstandtheimportanceofthroughputhistory,we
understandhowclosePensieveistotheoptimalscheme. triedtoanswer:howmanypastchunksarenecessarytoincludeinthe
5Thisrangerepresentsthetwoendsofthespectrumforthenumberofbitratessupported statespace?Todothis,wegeneratedthreeABRalgorithmswithPen-
bythevideosprovidedbytheDASHreferenceclient[11]. sievethatconsiderdifferentnumbersofthroughputmeasurements:
207

| SIGCOMM’17,August21-25,2017,LosAngeles,CA,USA |     |     |     |     |     |     | H.Maoetal. |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- |
Numberofneuronsandfilters(each) AverageQoEhd RTT(ms) AverageQoEhd
|     |     | 3.850±1.215 |     |     |     | 5.407±1.820 |     |
| --- | --- | ----------- | --- | --- | --- | ----------- | --- |
|     | 4   |             |     |     | 0   |             |     |
|     | 16  | 4.681±1.369 |     |     | 20  | 5.356±1.768 |     |
|     | 32  | 5.106±1.452 |     |     | 40  | 5.309±1.768 |     |
|     |     | 5.496±1.411 |     |     |     | 5.271±1.773 |     |
|     | 64  |             |     |     | 60  |             |     |
|     | 128 | 5.489±1.378 |     |     | 80  | 5.217±1.742 |     |
|     |     |             |     |     | 100 | 5.219±1.748 |     |
Table2:SweepingthenumberofCNNfiltersandhiddenneu-
ronsinPensieve’slearningarchitecture. Table4:AverageQoE valueswhendifferentRTTvaluesare
hd
imposedbetweentheclientandPensieve’sABRserver.
|     | Numberofhiddenlayers | AverageQoEhd |     |     |     |     |     |
| --- | -------------------- | ------------ | --- | --- | --- | --- | --- |
1 Pensieve
|     | 1   | 5.489±1.378 |     |     |     |     |     |
| --- | --- | ----------- | --- | --- | --- | --- | --- |
0.8
|     | 2   | 5.396±1.434 |     |     | Online	optimal |     |     |
| --- | --- | ----------- | --- | --- | -------------- | --- | --- |
4.253±1.219
|     | 5   |     |     | 0.6 | Offline	optimal |     |     |
| --- | --- | --- | --- | --- | --------------- | --- | --- |
FDC
0.4
| Table 3: Sweeping     | the number | of hidden layers | in Pensieve’s |     |     |     |     |
| --------------------- | ---------- | ---------------- | ------------- | --- | --- | --- | --- |
| learningarchitecture. |            |                  |               | 0.2 |     |     |     |
0
|     |     |     |     |     | -0.5 0.5 | 1.5 | 2.5 |
| --- | --- | --- | --- | --- | -------- | --- | --- |
1,8,and16pastvideochunks.AsshowninFigure14,considering Average	QoE
| only 1 past chunk | does not provide | enough information | to infer |     |     |     |     |
| ----------------- | ---------------- | ------------------ | -------- | --- | --- | --- | --- |
Figure15:ComparingPensievewithonlineandofflineoptimal.
futurenetworkcharacteristicsandhurtsperformance.Considering TheexperimentusestheQoE metric.
lin
thepast8chunksallowsPensievetoextractmoreinformationand
improveitspolicy.However,thebenefitsofadditionalthroughput
measurementseventuallyplateau.Forexample,providingPensieve server,consideringvaluesfrom0ms–100ms.Thisexperimentused
withmeasurementsforthepast16chunksonlyimprovestheaver- thesamesetupdescribedin§5.1,andmeasuredtheQoE hd metric.
Table4listsourresults,highlightingthatthelatencyfromthisad-
ageQoEby1%comparedtousingthroughputmeasurementsfor
ditionalRTThasminimalimpactonQoE:theaverageQoE with
| 8chunks.Thismarginalimprovementcomesatthecostofhigher |     |     |     |     |     |     | hd  |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
a100mslatencywaswithin3.5%ofthatwhenthelatencywas0
burdenduringtraining.
ms.Thereasonisthatthelatencyincurredfromtheadditionalround
Neuralnetwork(NN)architecture:StartingwithPensieve’sde-
|     |     |     |     | trip to Pensieve’s | ABR server | is masked by | the playback buffer |
| --- | --- | --- | --- | ------------------ | ---------- | ------------ | ------------------- |
faultlearningarchitecture(Figure5),wesweptarangeofNNpa-
occupancyandchunkdownloadtimes[18,21].
| rameterstounderstandtheimpactthateachhasonQoE |     |     | 6.First, |     |     |     |     |
| --------------------------------------------- | --- | --- | -------- | --- | --- | --- | --- |
hd
Trainingtime:TomeasuretheoverheadofgeneratingABRalgo-
usingasinglefixedhiddenlayer,wevariedthenumberoffiltersin
the1D-CNNandthenumberofneuronsinthehiddenmergelayer. rithmsusingRL,weprofiledPensieve’strainingprocess.Training
Theseparametersweresweptintandem,i.e.,when4filterswere asinglealgorithmrequiredapproximately50,000iterations,where
used,4neuronswereused.Resultsfromthissweeparepresentedin eachiterationtook300msandcorrespondedto16agentsupdating
Table2.Asshown,performancebeginstoplateauoncethenumber theirparametersinparallel(usingthetrainingapproachdescribedin
§4.2).Thus,intotal,trainingtookapproximately4hours.Wenote
offiltersandneuronseachexceed32.Additionally,noticethatonce
thesevaluesreach128(Pensieve’sdefaultconfiguration),variance thatthiscostisincurredofflineandcanbeperformedinfrequently
levelsdecreasewhileaverageQoEvaluesremainstable. dependingonenvironmentstability.
Next,afterfixingthenumberoffiltersandhiddenneuronsto128,
Optimality:OurresultsillustratethatPensieveisabletooutperform
wevariedthenumberofhiddenlayersinPensieve’sarchitecture.
existingABRalgorithms.However,Figures8and9showthatthere
| TheresultingQoE | hd valuesarelistedinTable3.Interestingly,we |     |     |                |                      |         |                        |
| --------------- | ------------------------------------------- | --- | --- | -------------- | -------------------- | ------- | ---------------------- |
|                 |                                             |     |     | still exists a | gap between Pensieve | and the | offline optimal. It is |
findthattheshallowestnetworkof1hiddenlayeryieldsthebestper-
uncleartowhatextentthisgapcanbeclosedsincetheofflineoptimal
formance;thisrepresentsthedefaultvalueinPensieve.Performance
schememakesdecisionswithperfectknowledgeoffuturebandwidth
steadilydegradesasweincreasethenumberofhiddenlayers.How-
(§5.1).Apracticalonlinealgorithmwouldonlyknowtheunderlying
ever,itisimportanttonotethatoursweepusedafixedlearningrate
distributionoffuturenetworkthroughput(ratherthantheprecise
andnumberoftrainingiterations.Tuningtheseparameterstocater
throughputvalues).ThusPensievemayinfactbemuchclosertothe
todeepernetworksmayimproveperformance,asthesenetworks
optimalonlinescheme.
generallytakelongertotrain.
Ofcourse,wecannotcomputetheoptimalonlinealgorithmfor
Client-to-ABR server latency: Recall that Pensieve deploys the real network traces, as we do not know the stochastic processes
RL-generatedABRmodelonanABRserver(notthevideostream- underlyingthesetraces.Thus,tounderstandhowPensievecompares
ingclients).Underthisdeploymentmodel,clientsmustfirstquery
tothebestonlinealgorithm,weconductedacontrolledexperiment
thePensieve’sABRservertodeterminethebitratetouseforthe
wherethedownloadtimeforeachchunkisgeneratedaccordingtoa
nextchunk,beforedownloadingthatchunkfromaCDNserver.To knownMarkovprocess.Specifically,wesimulatethedownloadtime
understandtheoverheadincurredbythisadditionalroundtrip,we TnofchunknasTn = Tn−1(cid:17) (Rn/Rn−1)+ϵ,whereRnisthebitrateof
(cid:16)
performedasweepoftheRTTbetweentheclientplayerandABR chunknandϵ ∼N 0, σ2 .Forthismodel,itisstraightforwardto
6QoEhd computetheoptimalonlinedecisionsusingdynamicprogramming.
isusedfortheparametersweepexperimentsasithighlightsperformances
| differencesmoreclearly. |     |     |     | See[28]fordetails. |     |     |     |
| ----------------------- | --- | --- | --- | ------------------ | --- | --- | --- |
208

NeuralAdaptiveVideoStreamingwithPensieve SIGCOMM’17,August21-25,2017,LosAngeles,CA,USA
TocomparetheoptimalonlinealgorithmwithPensieve,wesetthe 7 RELATEDWORK
videochunklengthδtobe4seconds,mimickingthe“EnvivioDash3” The earliest ABR algorithms can be primarily grouped into two
videodescribedin§5.1.TheinitialdownloadtimeT0wassetto4 classes:rate-basedandbuffer-based.Rate-basedalgorithms[21,42]
secondsforbitrateR0 =2kbps,andthestandarddeviationσ ofthe first estimate the available network bandwidth using past chunk
Gaussiannoisewassetto0.5.Bothbufferoccupancyanddownload downloads,andthenrequestchunksatthehighestbitratethatthe
timewerequantizedto0.1secondtorundynamicprogramming. networkispredictedtosupport.Forexample,Festive[21]predicts
Weusedthesamesetupin§5.1totrainaPensieveagentinthis throughputtobetheharmonicmeanoftheexperiencedthroughput
simulatedenvironment,andcomparedPensieve’sperformancewith forthepast5chunkdownloads.However,thesemethodsarehin-
theonlineandofflineoptimalschemes.Ourexperimentconsiders deredbythebiasespresentwhenestimatingavailablebandwidth
theQoE lin metricandtheresultsaredepictedinFigure15.Asex- on top of HTTP [22, 26]. Several systems aim to correct these
pected,theofflineoptimaloutperformstheonlineoptimalby9.1% throughputestimatesusingsmoothingheuristicsanddataaggrega-
onaverage.ThisiscomparabletotheperformancegapbetweenPen- tiontechniques[42],butaccuratethroughputpredictionremainsa
sieveandtheofflineoptimalobservedin§5.2.Indeed,theaverage challengeinpractice[53].
QoEachievedbyPensieveiswithin0.2%oftheonlineoptimal. Incontrast,buffer-basedapproaches[19,41]solelyconsiderthe
client’splaybackbufferoccupancywhendecidingthebitratesfor
6 DISCUSSION futurechunks.Thegoalofthesealgorithmsistokeepthebuffer
occupancyatapre-configuredlevelwhichbalancesrebufferingand
videoquality.Themostrecentbuffer-basedapproach,BOLA[41],
Deploying Pensieve in practice: In our current implementation, optimizesforaspecifiedQoEmetricusingaLyapunovoptimization
Pensieve’sABRserverrunsontheserver-sideofvideostreaming formulation.BOLAalsosupportschunkdownloadabandonment,
applications.Thisapproachoffersseveraladvantagesoverdeploy- wherebyavideoplayercanrestartachunkdownloadatalower
mentinclientvideoplayers.First,avarietyofclient-sidedevices bitratelevelifitsuspectsthatrebufferingisimminent.
areusedforvideostreamingtoday,rangingfrommulti-coredesktop Eachoftheseapproachesperformswellincertainsettingsbut
machines to mobile devices to TVs. By using an ABR server to notinothers.Specifically,rate-basedapproachesarebestatstartup
simplyguideclientbitrateselection,Pensievecaneasilysupport timeandwhenlinkratesarestable,whilebuffer-basedapproaches
thisbroadrangeofvideoclientswithoutmodificationsthatmaysac- aresufficientandmorerobustinsteadystateandinthepresenceof
rificeperformance.Additionally,ABRalgorithmsaretraditionally time-varyingnetworks[19].Consequently,recentlyproposedABR
deployedonclientswhichcanquicklyreacttochangingenviron- algorithmshavealsoinvestigatedcombiningthesetwotechniques.
ments[51].However,asnotedin§4,Pensievepreservesthisability Thestate-of-the-artapproachisMPC[51],whichemploysmodel
by having clients include observations about the environment in predictivecontrolalgorithmsthatuseboththroughputestimatesand
eachrequestsenttotheABRserver.Further,ourresultssuggestthat bufferoccupancyinformationtoselectbitratesthatareexpectedto
theadditionallatencyrequiredtocontactPensieve’sABRserver maximizeQoEoverahorizonofseveralfuturechunks.However,
hasnegligibleimpactonQoE(§5.4).Ifdirectdeploymentinclient MPCstillreliesheavilyonaccuratethroughputestimateswhichare
videoplayersispreferred,Pensievecouldusecompressedneural notalwaysavailable.Whenthroughputpredictionsareincorrect,
networks[16]orrepresenttheminlanguagessupportedbymany MPC’sperformancecandegradesignificantly.Addressingthisissue
clientapplications,e.g.,JavaScript[45]. requiresheuristicsthatmakethroughputpredictionsmoreconser-
vative.However,tuningsuchheuristicstoperformwellindifferent
environmentsischallenging.Further,asweobservedin§3,MPCis
Periodicandonlinetraining:Inthispaper,weprimarilydescribed
oftenunabletoplanfarenoughintothefuturetoapplythepolicies
RL-basedABRalgorithmgenerationasanofflinetask.Thatis,with
thatwouldmaximizeperformanceingivensettings.
Pensieve,weassumedthattheABRalgorithmwasgeneratedapriori
AseparatelineofworkhasproposedapplyingRLtoadaptive
(duringatrainingphase)andwasthenunmodifiedafterdeployment.
video streaming [6, 8, 9, 47]. All of these schemes apply RL in
However,Pensievecannaturallysupportanapproachinwhichan
a “tabular form,” which stores and learns the value function for
ABRalgorithmisgeneratedorupdatedperiodicallyasnewdata
allstatesandactionsexplicitly,ratherthanusingfunctionapprox-
arrives. This technique would enable ABR algorithms to further
imators(e.g.,neuralnetworks).Asaresult,theseschemesdonot
adapttotheexactconditionsthatvideoclientsareexperiencingata
scaletothelargestatespacesnecessaryforgoodperformancein
giventime.Theextremeversionofthisapproachistotrainonline
realnetworks,andtheirevaluationhasbeenlimitedtosimulations
directlyonthevideoclient.However,onlinetrainingonvideoclients
withsyntheticnetworkmodels.Forexample,themostrecenttabu-
raisestwochallenges.First,itincreasesthecomputationaloverhead
larscheme[6]reliesonthefundamentalassumptionthatnetwork
for the client. Second, it requires algorithms that can learn from
bandwidthisMarkovian,i.e.,thefuturebandwidthdependsonlyon
smallamountsofdataandconvergetoagoodpolicyquickly.
thethroughputobservedinthelastchunkdownload.Thisassump-
Retrainingfrequencydependsonhowquicklynewnetworkbe-
tionconfinesthestatespacetoconsideronlyonepastbandwidth
haviorsemergetowhichexistingmodelsdonotgeneralize.While
measurement,makingthetabularapproachfeasibletoimplement.
ourgeneralizationresults(§5.3)suggestthatretrainingfrequently
Aswesawin§5.4,theinformationcontainedinonepastchunkis
maynotbenecessary,techniquestodeterminewhentoretrainand
notsufficienttoaccuratelyinferthedistributionoffuturebandwidth.
investigatingthetradeoffswithonlinetrainingareinterestingareas
Nevertheless,someofthetechniquesusedintheexistingRLvideo
forfuturework.
209

SIGCOMM’17,August21-25,2017,LosAngeles,CA,USA H.Maoetal.
streamingschemes(e.g.,Post-DecisionStates[6,35])couldbeused [21] J.Jiang,V.Sekar,andH.Zhang.2012.ImprovingFairness,Efficiency,and
toacceleratelearninginPensieveaswell. StabilityinHTTP-basedAdaptiveVideoStreamingwithFESTIVE.InCoNEXT.
[22] J.Jiangetal.2016.CFA:APracticalPredictionSystemforVideoQoE
Optimization.InNSDI.USENIXAssociation.
8 CONCLUSION [23] I.Ketykóetal.2010.QoEMeasurementofMobileYouTubeVideoStreaming.In
Proceedingsofthe3rdWorkshoponMobileVideoDelivery(MoViD).ACM.
WepresentedPensieve,asystemwhichgeneratesABRalgorithms [24] V.RKondaandJ.N.Tsitsiklis.2000.Actor-criticalgorithms.InAdvancesin
usingreinforcementlearning.UnlikeABRalgorithmsthatusefixed neuralinformationprocessingsystems.1008–1014.
[25] S.S.KrishnanandR.K.Sitaraman.2012.VideoStreamQualityImpactsViewer
heuristicsorinaccuratesystemmodels,Pensieve’sABRalgorithms Behavior:InferringCausalityUsingQuasi-experimentalDesigns.InProceedings
aregeneratedusingobservationsoftheresultingperformanceof ofthe2012ACMConferenceonInternetMeasurementConference(IMC).ACM.
[26] Z.Lietal.2014.ProbeandAdapt:RateAdaptationforHTTPVideoStreaming
pastdecisionsacrossalargenumberofvideostreamingexperiments.
AtScale.IEEEJournalonSelectedAreasinCommunications(2014).
ThisallowsPensievetooptimizeitspolicyfordifferentnetwork [27] H.Mao,M.Alizadeh,I.Menache,andS.Kandula.2016.ResourceManagement
characteristicsandQoEmetricsdirectlyfromexperience.Overa withDeepReinforcementLearning.InHotNets.ACM.
[28] H.Mao,R.Netravali,andM.Alizadeh.2017.NeuralAdaptiveVideoStreaming
broadsetofnetworkconditionsandQoEmetrics,wefoundthat
withPensieve.(2017).
PensieveoutperformedexistingABRalgorithmsby12%–25%. http://web.mit.edu/pensieve/content/pensieve-tech-report.pdf
[29] V.Mnihetal.2015.Human-levelcontrolthroughdeepreinforcementlearning.
Nature518(2015),529–533.
Acknowledgments.Wethankourshepherd,JohnByers,andthe
[30] V.Mnihetal.2016.Asynchronousmethodsfordeepreinforcementlearning.In
anonymousSIGCOMMreviewersfortheirvaluablefeedback.We InternationalConferenceonMachineLearning.1928–1937.
alsothankTe-YuanHuangforherguidanceregardingvideostream- [31] R.K.P.Mok,E.W.W.Chan,X.Luo,andR.K.C.Chang.2011.Inferringthe
QoEofHTTPVideoStreamingfromUser-viewingActivities.InProceedingsof
inginpractice,andJiamingLuoforfruitfuldiscussionsregarding theFirstACMSIGCOMMWorkshoponMeasurementsUptheStack(W-MUST).
thelearningaspectsofthedesign.Thisworkwasfundedinpartby [32] R.K.P.Mok,E.W.W.Chan,andR.K.C.Chang.2011.Measuringthequality
ofexperienceofHTTPvideostreaming.In12thIFIP/IEEEInternational
NSFgrantsCNS-1617702,CNS-1563826,andCNS-1407470,the
SymposiumonIntegratedNetworkManagement(IM2011)andWorkshops.
MITCenterforWirelessNetworksandMobileComputing,anda [33] R.Netravalietal.2015.Mahimahi:AccurateRecord-and-ReplayforHTTP.In
QualcommInnovationFellowship. ProceedingsofUSENIXATC.
[34] K.Piamrat,C.Viho,J.M.Bonnin,andA.Ksentini.2009.QualityofExperience
MeasurementsforVideoStreamingoverWirelessNetworks.InProceedingsof
REFERENCES the2009SixthInternationalConferenceonInformationTechnology:New
Generations(ITNG).IEEEComputerSociety.
[1] M.Abadietal.2016.TensorFlow:ASystemforLarge-scaleMachineLearning. [35] W.B.Powell.2007.ApproximateDynamicProgramming:Solvingthecursesof
InOSDI.USENIXAssociation. dimensionality.Vol.703.JohnWiley&Sons.
[2] Akamai.2016.dash.js.https://github.com/Dash-Industry-Forum/dash.js/.(2016). [36] B.Recht,C.Re,S.Wright,andF.Niu.2011.Hogwild:Alock-freeapproachto
parallelizingstochasticgradientdescent.InAdvancesinNeuralInformation
[3] S.Akhshabi,A.C.Begen,andC.Dovrolis.2011.AnExperimentalEvaluationof ProcessingSystems.693–701.
Rate-adaptationAlgorithmsinAdaptiveStreamingoverHTTP.InMMSys. [37] H.Riiseretal.2013.CommutePathBandwidthTracesfrom3GNetworks:
[4] M.Allman,V.Paxson,andE.Blanton.2009.TCPcongestioncontrol.RFC5681. AnalysisandApplications.InProceedingsofthe4thACMMultimediaSystems
Conference(MMSys).ACM.
[5] C.M.Bishop.2006.PatternRecognitionandMachineLearning.Springer. [38] J.K.Rowling.2000.HarryPotterandtheGobletofFire.London:Bloomsbury.
[6] F.Chiariottietal.2016.OnlinelearningadaptationstrategyforDASHclients.In [39] Sandvine.2015.GlobalInternetPhenomena-LatinAmerican&NorthAmerica.
Proceedingsofthe7thInternationalConferenceonMultimediaSystems.ACM,8. [40] D.Silveretal.2016.MasteringthegameofGowithdeepneuralnetworksand
treesearch.Nature529(2016),484–503.
[7] Cisco.2016.CiscoVisualNetworkingIndex:ForecastandMethodology, [41] K.Spiteri,R.Urgaonkar,andR.K.Sitaraman.2016.BOLA:Near-Optimal
2015-2020. BitrateAdaptationforOnlineVideos.CoRRabs/1601.06748(2016).
[8] M.Claeysetal.2013.DesignofaQ-learning-basedclientqualityselection [42] Y.Sunetal.2016.CS2P:ImprovingVideoBitrateSelectionandAdaptationwith
algorithmforHTTPadaptivevideostreaming.InAdaptiveandLearningAgents Data-DrivenThroughputPrediction.InSIGCOMM.ACM.
Workshop. [43] R.S.SuttonandA.G.Barto.1998.ReinforcementLearning:AnIntroduction.
[9] M.Claeysetal.2014.Designandoptimisationofa(FA)Q-learning-basedHTTP MITPress.
adaptivestreamingclient.ConnectionScience(2014). [44] R.S.Suttonetal.1999.Policygradientmethodsforreinforcementlearningwith
[10] FederalCommunicationsCommission.2016.RawData-MeasuringBroadband functionapproximation..InNIPS,Vol.99.1057–1063.
America.(2016).https://www.fcc.gov/reports-research/reports/ [45] Synaptic.2016.synaptic.js–Thejavascriptarchitecture-freeneuralnetwork
measuring-broadband-america/raw-data-measuring-broadband-america-2016 libraryfornode.jsandthebrowser.https://synaptic.juancazala.com/.(2016).
[11] DASHIndustryForm.2016.ReferenceClient2.4.0.http://mediapm.edgesuite. [46] TFLearn.2017.TFLearn:Deeplearninglibraryfeaturingahigher-levelAPIfor
net/dash/public/nightly/samples/dash-if-reference-player/index.html.(2016). TensorFlow.http://tflearn.org/.(2017).
[12] F.Dobrianetal.2011.UnderstandingtheImpactofVideoQualityonUser [47] J.vanderHooftetal.Alearning-basedalgorithmforimproved
Engagement.InSIGCOMM.ACM. bandwidth-awarenessofadaptivestreamingclients.In2015IFIP/IEEE
[13] G.Fairhurstetal.2015.UpdatingTCPtoSupportRate-LimitedTraffic.RFC InternationalSymposiumonIntegratedNetworkManagement.IEEE.
7661(2015). [48] A.S.Vezhnevetsetal.2017.FeUdalNetworksforHierarchicalReinforcement
[14] XavierGlorotandYoshuaBengio.2010.Understandingthedifficultyoftraining Learning.arXivpreprintarXiv:1703.01161(2017).
deepfeedforwardneuralnetworks..InAistats,Vol.9.249–256. [49] K.Winstein,A.Sivaraman,andH.Balakrishnan.StochasticForecastsAchieve
[15] M.T.Hagan,H.B.Demuth,M.H.Beale,andO.DeJesús.1996.Neural HighThroughputandLowDelayoverCellularNetworks.InNSDI.
networkdesign.PWSpublishingcompanyBoston. [50] Y.WuandY.Tian.2017.Trainingagentforfirst-personshootergamewith
[16] S.Han,H.Mao,andW.J.Dally.2015.Deepcompression:Compressingdeep actor-criticcurriculumlearning.InICLR.
neuralnetworkwithpruning,trainedquantizationandhuffmancoding.CoRR, [51] X.Yin,A.Jindal,V.Sekar,andB.Sinopoli.2015.AControl-TheoreticApproach
abs/1510.001492(2015). forDynamicAdaptiveVideoStreamingoverHTTP.InSIGCOMM.ACM.
[17] M.Handley,J.Padhye,andS.Floyd.2000.TCPCongestionWindowValidation. [52] Y.Zakietal.2015.Adaptivecongestioncontrolforunpredictablecellular
RFC2861(2000). networks.InACMSIGCOMMComputerCommunicationReview.ACM.
[18] T.Y.Huangetal.2012.Confused,Timid,andUnstable:PickingaVideo [53] X.K.Zou.2015.CanAccuratePredictionsImproveVideoStreaminginCellular
StreamingRateisHard.InProceedingsofthe2012ACMConferenceonInternet Networks?.InHotMobile.ACM.
MeasurementConference(IMC).ACM.
[19] T.Y.Huangetal.2014.ABuffer-basedApproachtoRateAdaptation:Evidence
fromaLargeVideoStreamingService.InSIGCOMM.ACM.
[20] M.Jaderbergetal.2017.Reinforcementlearningwithunsupervisedauxiliary
tasks.InICLR.
210