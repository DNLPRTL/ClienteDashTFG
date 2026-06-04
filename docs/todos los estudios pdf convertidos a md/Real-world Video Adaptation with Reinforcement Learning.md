|     | Real-world |     | Video | Adaptation |     | with Reinforcement |     |     | Learning |     |     |     |
| --- | ---------- | --- | ----- | ---------- | --- | ------------------ | --- | --- | -------- | --- | --- | --- |
HongziMao12 ShannonChen2 DrewDimmery2 ShaunSingh2 DrewBlaisdell2 YuandongTian2
|     |     |     |     | MohammadAlizadeh1 |     | EytanBakshy2 |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
Abstract ments and playback buffer occupancy. Their goal is to
optimizethevideo’squalityofexperience(QoE)byadapt-
| Client-side | video | players | employ | adaptive | bi- |     |     |     |     |     |     |     |
| ----------- | ----- | ------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
0202 guA 82  ]IN.sc[  1v85821.8002:viXra ingthevideobitratetotheunderlyingnetworkconditions.
trate(ABR)algorithmstooptimizeuserquality
|                                  |          |          |          |               |      | However,           | designing | a strong      | ABR             | algorithm | with             | hand- |
| -------------------------------- | -------- | -------- | -------- | ------------- | ---- | ------------------ | --------- | ------------- | --------------- | --------- | ---------------- | ----- |
| of experience                    |          | (QoE).We | evaluate | recently      | pro- |                    |           |               |                 |           |                  |       |
|                                  |          |          |          |               |      | tuned heuristics   |           | is difficult, | mainly          | due       | to hard-to-model |       |
| posed                            | RL-based | ABR      | methods  | in Facebook’s |      |                    |           |               |                 |           |                  |       |
|                                  |          |          |          |               |      | network variations |           | and           | hard-to-balance |           | conflicting      | video |
| web-basedvideostreamingplatform. |          |          |          | Real-world    |      |                    |           |               |                 |           |                  |       |
|                                  |          |          |          |               |      | QoE objectives     | (e.g.,    | maximizing    |                 | bitrate   | vs. minimizing   |       |
ABRcontainsseveralchallengesthatrequirescus-
stalls)(Yinetal.,2015).
| tomized | designs | beyond | off-the-shelf | RL  | algo- |     |     |     |     |     |     |     |
| ------- | ------- | ------ | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
rithms—weimplementascalableneuralnetwork Facingthesedifficulties,recentstudieshaveconsideredus-
architecture that supports videos with arbitrary ingreinforcementlearning(RL)asadata-drivenapproach
bitrateencodings;wedesignatrainingmethodto toautomaticallyoptimizetheABRalgorithms(Maoetal.,
copewiththevarianceresultingfromthestochas- 2017). RLoptimizesitscontrolpolicybasedontheactual
ticityinnetworkconditions;andweleveragecon- performanceofpastchoices,anditisabletodiscoverpoli-
strainedBayesianoptimizationforrewardshap- ciesthatoutperformalgorithmsthatrelyonfixedheuristics
inginordertooptimizetheconflictingQoEob- oruseinaccuratesystemmodels. Forexample,asexplained
jectives. Inaweek-longworldwidedeployment inMaoetal.(2017),RLmethodscanlearnhowmuchplay-
with more than 30 million video streaming ses- back buffer is necessary to mitigate the risk of stall in a
sions,ourRLapproachoutperformstheexisting specificnetwork,basedonthenetwork’sinherentthrough-
human-engineeredABRalgorithms. putvariability. Incontrolledexperimentswithafixedset
ofvideosandnetworktraces,anumberofpriorworkhas
|     |     |     |     |     |     | shown promising |     | results | for RL | methods | (van | der Hooft |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | ------ | ------- | ---- | --------- |
1.Introduction etal.;Claeysetal.,2013). However,itremainsunknown
howtheRL-basedmethodscomparetothealreadydeployed
Thevolumeofvideostreamingtraffichasbeenrapidlygrow-
heuristic-basedABRmethodsinlarge-scale,real-worldset-
ing in recent years (Cisco, 2016; Sandvine, 2015), reach- tings,wheregeneralizationandrobustnessarecrucialfor
ingalmost60%ofalltheInternettraffic(Sandvine,2018).
goodperformance(Systems&Research,2019).
| Meanwhile, | therehasbeenasteadyriseinuserdemands |     |     |     |     |                |     |         |                |     |            |     |
| ---------- | ------------------------------------ | --- | --- | --- | --- | -------------- | --- | ------- | -------------- | --- | ---------- | --- |
|            |                                      |     |     |     |     | In this paper, | we  | present | the deployment |     | experience | of  |
onvideoquality—viewersquicklyleavethevideosessions
withinsufficientquality(Dobrianetal.,2011). Asaresult, ABRL, an RL-based ABR module in Facebook’s produc-
|     |     |     |     |     |     | tionweb-basedvideoplatform. |     |     |     | IndesigningofABRL,we |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | -------------------- | --- | --- |
contentprovidersarestrivingtoimprovethevideoquality
theydelivertotheusers(Krishnan&Sitaraman,2012). foundthatoff-the-shelfRLmethodswerenotsufficientto
addressthechallengesthatweencounteredwhenattempting
Adaptivebitrate(ABR)algorithmsareaprimarytoolthat todeployRL-basedcontrolpoliciesinreal-worldenviron-
contentprovidersusetooptimizevideoqualitysubjectto
ments. Tolearnhigh-qualityABRalgorithmsthatsurpass
bandwidthconstraints. Thesealgorithmsrunonclient-side thedeployedheuristics,wehadtodesignnewcomponents
| video players | and | dynamically | choose | a bitrate | for each |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | ------ | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
inABRL’slearningproceduretosolvethefollowingchal-
videochunk(e.g.,2-secondblock),basedonnetworkand
lenges.
| video observations |     | such as | network | throughput | measure- |     |     |     |     |     |     |     |
| ------------------ | --- | ------- | ------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
First,videosinproductionhavedifferentavailablebitrate
1MITComputerScienceandArtificialIntelligenceLaboratory
encodings,e.g.,somevideosonlyhaveHD/SDencodings,
2Facebook.Correspondenceto:HongziMao<hongzi@mit.edu>,
whileothervideoshaveafullspectrumofbitrateencodings.
EytanBakshy<ebakshy@fb.com>.
However,standardRLapproachesuseneuralnetworks(Ha-
ganetal.,1996)thatprovidefixedoutputsbothinthenum-
ReinforcementLearningforRealLife(RL4RealLife)Workshopin
the36th ber of bitrates and the corresponding bitrate levels (e.g.,
InternationalConferenceonMachineLearning,Long
Beach,California,USA,2019.Copyright2019bytheauthor(s).

Real-worldVideoAdaptationwithReinforcementLearning
thethirdoutputalwayscorrespondsto720Pencoding). To outperforms the heuristic-based ABR policy by 1.6% in
represent arbitrary bitrate encodings, we design ABRL’s averagebitratesandreducesstallsby0.4%. Forvideoses-
neuralnetworktooutputasinglepriorityvalueforeachbi- sions with poor network connectivity, in which cases the
trateencoding;andwerepeatedlyusethesamecopyofthe ABRtaskismorechallenging,ABRLprovides5.9%higher
neuralnetworkforallencodingsofavideo. Thisapproach bitrateand2.4%fewerstalls. ForFacebook,evenasmall
scalestoanyvideoABRLservesandsupportsend-to-end improvementinvideoQoEissubstantialgiventhescaleof
RLtraining(§3.2). itsvideoplatform,whichconsistsofmillionsofhoursof
|     |     |     |     |     |     | videowatchesperday(Wagner,2016). |     | Inthisscale,afrac- |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- | ------------------ | --- |
Second,ABRLexperiencesawidevarietyofnetworkcon-
tionofapercentconsistentreductioninvideobufferingis
| ditionsanddifferentvideodurationsduringtraining. |     |     |     |     | This |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
significant;eachday,thiswouldsaveyearsofvideoloading
introducesundesirablevariancesinceconventionalRLtrain-
timeinaggregate.
ingalgorithmscannottellwhethertheobservedQoEfeed-
backoftwoABRdecisionsdiffersduetodisparatenetwork
2.Background
conditions,orduetothequalityofthelearnedABRpolicy.
| To cope | with the | stochasticity | of network | conditions, | we  |     |     |     |     |
| ------- | -------- | ------------- | ---------- | ----------- | --- | --- | --- | --- | --- |
Weprovideareviewofthebasicconceptsofadaptivevideo
isolatetherewardsontheactualnetworktraceexperienced
streamingoverHTTP.Videosarestoredasmultiplechunks,
inatrainingsession,usingarecenttechniqueforRLinenvi-
eachofwhichrepresentsafewsecondsofvideoplayback.
ronmentswithstochasticinputprocesses(Maoetal.,2019).
Eachchunkisencodedatseveraldiscretebitrates,wherea
ThisapproachseparatesthecontributionsoftheABRpolicy
higherbitrateimpliesahigherresolutionandthusalarger
fromtheoverallfeedback,enablingABRLtolearnrobust
|     |     |     |     |     |     | chunksize. | Thechunksarealignedforseamlesstransitions |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | ----------------------------------------- | --- | --- |
policiesacrossdifferentdeploymentconditions(§3.3).
acrossbitrates,i.e.,videoplayerscanswitchbitratesatany
Third, production ABR requires balancing and co- chunkboundarywithoutfetchingredundantbitsorskipping
| optimizing  | multiple | objectives | together | (e.g., maximize   |     | partsofthevideo. |     |     |     |
| ----------- | -------- | ---------- | -------- | ----------------- | --- | ---------------- | --- | --- | --- |
| bitrate and | minimize | stalls).   | But RL   | requires a single | re- |                  |     |     |     |
Whenaclientwatchesavideo,thevideoproviderinitially
| ward value | as the | training | feedback. | Prior work | merges |                  |            |                   |                 |
| ---------- | ------ | -------- | --------- | ---------- | ------ | ---------------- | ---------- | ----------------- | --------------- |
|            |        |          |           |            |        | sends the client | a manifest | file that directs | the client to a |
themulti-dimensionalobjectiveswithaweightedsum(Yin
|              |                                       |     |     |     |     | specific source                  | (e.g., a CDN) | hosting the           | video and lists |
| ------------ | ------------------------------------- | --- | --- | --- | --- | -------------------------------- | ------------- | --------------------- | --------------- |
| etal.,2015). | Inpractice,sinceABRL’sgoalistooutper- |     |     |     |     |                                  |               |                       |                 |
|              |                                       |     |     |     |     | theavailablebitratesforthevideo. |               | Theclientthenrequests |                 |
formtheexistingABRalgorithmineverydimensionofthe
videochunksonebyone,usinganadaptivebitrate(ABR)
| objective, | this does | not amount | to  | a specific, pre-defined |     |     |     |     |     |
| ---------- | --------- | ---------- | --- | ----------------------- | --- | --- | --- | --- | --- |
algorithm.Thesealgorithmsuseavarietyofdifferentinputs
| tradeoff | between | different | objectives. | To determine | the |     |     |     |     |
| -------- | ------- | --------- | ----------- | ------------ | --- | --- | --- | --- | --- |
(e.g.,playbackbufferoccupancy,throughputmeasurements,
weightsfordifferentrewardcomponents,weformulatethe
|     |     |     |     |     |     | etc.) toselectthebitrateforfuturechunks. |     |     | Aschunksare |
| --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | ----------- |
multi-objectiveoptimizationproblemasaconstrainedopti-
downloaded,theyarestoredintheplaybackbufferonthe
mizationproblem(i.e.,optimizingoneobjectivesubjectto
|                                          |     |     |     |            |     | client. Playback              | of a given | chunk cannot          | begin until the |
| ---------------------------------------- | --- | --- | --- | ---------- | --- | ----------------------------- | ---------- | --------------------- | --------------- |
| boundeddegradationalongotherobjectives). |     |     |     | Thisallows |     |                               |            |                       |                 |
|                                          |     |     |     |            |     | entirechunkhasbeendownloaded. |            | Inourexperiments(§4), |                 |
ustouseconstrainedBayesianoptimization(Lethametal.,
wedeployABRLonFacebook’sweb-basedvideostreaming
2018)toefficientlysearchforrewardweightswhichbest
platformforeaseofdeployment.
meettop-lineobjectives(§3.4).
| Lastly, foreaseofunderstandingandensuringsafety, |     |     |     |     | we  | 3.Design |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
translateABRL’slearnedABRpolicyintoaninterpretable
formfordeployment. Specifically,werealizefromthepol- InthissectionwedescribethedesignofABRL,asystem
icyvisualizationthatthelearnedABRalgorithmexhibits that generates RL-based ABR policies to deploy in Face-
approximatelylinearbehaviorintheobservedstateofnet- book’sproductionvideoplatform. Westartbydescribing
workandbufferoccupancy. Thus,wefitalinearfunction thesimulatorthathostsRLtraininginthebackend(§3.1).
of network throughput and buffer occupancy to approxi- Next,weexplaintheRLtrainingframework(§3.2),which
mateABRL’slearnedABRpolicy(§3.5). Suchtranslation includesthevariancereduction(§3.3)andrewardshaping
degradestheaveragestallrateby0.8%, butprovidesfull (§3.4)techniquesneededforthisapplication. Finally,we
interpretabilityforhumanengineers. Thisallowsengineers describehowABRLtranslatesthelearnedABRpolicyto
to understand the policy well enough to verify the learn deployinthefrontend(§3.5). Figure1showsanoverview.
policy.
3.1.Simulator
| We run A/B | tests | that compare | ABRL | with the | existing |     |     |     |     |
| ---------- | ----- | ------------ | ---- | -------- | -------- | --- | --- | --- | --- |
ABR algorithms on Facebook’s web-based video stream- To train the ABR agent with RL, we first build a simula-
| ingplatform. | Inaweek-longworldwidedeploymentwith |     |     |     |     |     |     |     |     |
| ------------ | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
torthatmodelstheplaybackbufferdynamicsduringvideo
morethan30millionvideostreamingsessions(§4),ABRL streaming. Thebufferdynamicsaregovernedbythestan-

Real-worldVideoAdaptationwithReinforcementLearning
|                    | Front end |               |                  | Back end         |      |                | Reward	shaping	(§3.4) |            |     |              |     |
| ------------------ | --------- | ------------- | ---------------- | ---------------- | ---- | -------------- | --------------------- | ---------- | --- | ------------ | --- |
|                    |           |               | Store experience |                  | RL A | g e n t   (    | § 3 .2 )              | Simulator  |     |              |     |
| State observations |           | Video session |                  | Simulator	(§3.1) |      |                |                       | (§3.1)     |     |              |     |
|                    |           |               |                  |                  |      | P o li c y   n | e u ra l network      |            |     | Network	and	 |     |
watch	time
240P
Translated	 Update model RL	training	(§3.2-4) etatS 360P Sample trace	replay
|     |      |                     |     |                           |     |                                                | 720P   | 720P |     | (§3.3) |     |
| --- | ---- | ------------------- | --- | ------------------------- | --- | ---------------------------------------------- | ------ | ---- | --- | ------ | --- |
|     |      | ABR	model           |     |                           |     |                                                | action |      |     |        |     |
|     | 720P |                     |     | Policy	translation	(§3.5) |     |                                                | 1080P  |      |     |        |     |
|     |      | Next bitrate action |     |                           |     | Observe predicted bandwidth and current buffer |        |      |     |        |     |
Figure1.Designoverview.Foreachvideosessionintheproduc-
|     |     |     |     |     | Figure2.Backend |     | RL training | framework. | ABRL | updates | the |
| --- | --- | --- | --- | --- | --------------- | --- | ----------- | ---------- | ---- | ------- | --- |
tionexperiment, ABRLcollectstheexperienceofvideowatch ABRpolicyneuralnetworkbyobservingtheoutcomewheninter-
timeandthenetworkbandwidthmeasurementsandpredictions. actingwithasimulator. Thesimulatorusesproductiontracesto
Itthensimulatesthebufferdynamicsofthevideostreamingus- simulatethevideobufferdynamics.
| ingtheseexperiencesinthebackend. |     |     | AfterRLtraining,ABRL |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
deploysthetranslatedABRmodeltotheuserfrontend.
3.2.ReinforcementLearning
ThetrainingsetupshowninFigure2followsthestandard
|                                |     |     |                      |     | RLframework. |             | Inthissection,wedescribethedetailsof |                |          |                |        |
| ------------------------------ | --- | --- | -------------------- | --- | ------------ | ----------- | ------------------------------------ | -------------- | -------- | -------------- | ------ |
|                                |     |     |                      |     | the          | RL agent    | and the policy                       | gradient       | training | algorithm.     |        |
|                                |     |     |                      |     | In           | particular, | we explain                           | the challenges |          | we encountered |        |
|                                |     |     |                      |     | to motivate  |             | the variance                         | reduction      | (§3.3)   | and the        | reward |
| dardABRproceduredescribedin§2. |     |     | Specifically,thesim- |     |              |             |                                      |                |          |                |        |
shaping(§3.4)techniques.
| ulator | maintains | an internal | representation | of the client’s |     |        |                  |     |            |       |         |
| ------ | --------- | ----------- | -------------- | --------------- | --- | ------ | ---------------- | --- | ---------- | ----- | ------- |
|        |           |             |                |                 | RL  | setup. | Upon downloading |     | each video | chunk | at each |
playbackbuffer,whichincludesthecurrentsizeofbuffer
and the buffer capacity. The simulator invokes the ABR step t, the RL agent observes the state s t = (x t ,o t ,(cid:126)n t ),
wherex isthebandwidthpredictionforthenextchunk,o
| logicateachvideochunkdownloadevent,wheretheABR |     |     |     |     |     | t   |     |     |     |     | t   |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
isthecurrentbufferoccupancyand(cid:126)n
logicdictatesthebitratedecisionforthenextchunk. For t isavectorofthefile
eachchunkdownload,thesimulatordeterminesthedown- sizesforthenextvideochunk. Asafeedbackforthebitrate
|           |       |        |                  |                 | actiona | ,theagentreceivesareward |     |     | r   | constructedasa |     |
| --------- | ----- | ------ | ---------------- | --------------- | ------- | ------------------------ | --- | --- | --- | -------------- | --- |
| load time | based | on the | file size of the | video chunk and |         | t                        |     |     | t   |                |     |
thenetworkthroughputfromthetraces. Sincethevideois weightedcombinationofselectedbitrateb t andstalltimeof
| playedinrealtime,thesimulatorthendrainstheplayback |     |     |     |     | thepastchunkd |     | :   |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
t
bufferbythedownloadtimeofthecurrentchunkrepresent- bvb dvd [1(d
|     |     |     |     |     |     |     | r =w −w | +w  |     | >0)], | (1) |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | ----- | --- |
ingthevideoplaybackduringthedownload. Ifthesizeof t b t d t c t
where1(·)isanindicatorfunctioncountingthenumberof
currentplaybackbufferissmallerthanthedownloadtime,
weemptythebufferandissueastallevent. Subsequently, stalls,andw ,w ,w ,v ,v arethetuningweightsforthe
|     |     |     |     |     |     |     | b d c | b d |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
thebufferaddsthedurationofthedownloadedchunkinto reward. Noticethattheseweightscannotbepredetermined,
theplaybackbuffer.Inthecasewherethebufferexceedsthe because the goal of RL-based ABR is to outperform the
capacity,thesimulatorticksthetimeforwardinthetrace existingABRalgorithmineverydimensionofthemetric
withoutdownloadinganychunk(i.e.,moveforwardinthe (i.e.,higherbitrate,lessstalltimeandlessstallcount),which
bandwidthtrace). Thesimulatedvideosessionterminatesat does not amount to a quantitative objective. In §3.4 we
theendofeachtrace(correspondingtotheendofawatch). describe how we use Bayesian optimization to shape the
Duringtraining,ABRLrepeatsthesimulatedvideosessions weightsforoptimizingthemulti-dimensionalobjective.
byloadingtracesrandomlyateachtime.
|     |     |     |     |     | Policy. | As  | shown in | Figure | 3, the agent | samples | the |
| --- | --- | --- | --- | --- | ------- | --- | -------- | ------ | ------------ | ------- | --- |
The simulator utilizes sampled traces collected from the next bitrate action a t based on its parametrized policy:
actualvideoplaybacksessionsfromthefrontend. Ateach π (a |s ) → [0,1]. In practice, since the number of bi-
θ t t
trateencodings(thusthelengthof(cid:126)n
videochunkdownloadevent,welogtothebackendatuple t )variesacrossdiffer-
of(1)networkbandwidthestimation,(2)bandwidthmea- ent videos (Lederer et al., 2012), we architect the policy
surementforthepreviouschunkdownload,(3)theelapsed networktotakeanarbitrarynumberoffilesizesasinput.
time of downloading the previous chunk and (4) the file Specifically,foreachbitrate,theinputtothepolicynetwork
sizes corresponding to different bitrate encodings of the consistsofthepredictedbandwidthandbufferoccupancy,
videochunk. Thebandwidthestimationisanoutputfroma concatenatedwiththecorrespondingfilesize. Wethencopy
Facebooknetworkingmodule. Notethatthelengthofthe thesameneuralnetworkforeachofthebitrateencodings
tracevariesnaturallyacrossdifferentvideosessionsdueto (e.g.,theneuralnetworksshowninFigure3sharethesame
the difference in the watch time. In our training, we use weights θ). Each copy of the policy network outputs a
morethan100,000tracesfromproductionvideostreaming “priority” value qi for selecting the corresponding bitrate
t
| sessions. |     |     |     |     | i. Afterwards,weuseasoftmax(Bishop,2006)operation |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |

Real-worldVideoAdaptationwithReinforcementLearning
|     |     |     |     | Parameters θ |     | π(a|s) |     | htdiwdnaB                |     |     |         |     |
| --- | --- | --- | --- | ------------ | --- | ------ | --- | ------------------------ | --- | --- | ------- | --- |
|     |     |     | x   |              |     | θ t t  |     | 4 Same bitrate action    |     |     | Trace 1 |     |
|     |     |     | t   |              |     |        |     | )spbm( at the same state |     |     |         |     |
|     |     |     | o t |              |     |        |     | 2                        |     |     |         |     |
|     |     |     |     |              | q1t | p1t    |     |                          |     |     | Trace 2 |     |
n1
|     |     |     | t   |     |     |     |     | 0   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Softmax
|            |        |      |     | Policy         |     |     |     | draweR 4 |     |     |     |     |
| ---------- | ------ | ---- | --- | -------------- | --- | --- | --- | -------- | --- | --- | --- | --- |
| x t o t n1 | t n2 t | nM t |     | neural network |     |     |     |          |     |     |     |     |
2
Bandwidth estimate Buffer occupancy  File size of bitrate 1 File size of bitrate 2 File size of bitrate M Watch 1 ends
|     |     |     | x   |     |     |     |     | 0 But get vastly  |     |     |              |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | ------------ | --- |
|     |     |     | t   |     |     |     |     | different rewards |     |     | Watch 2 ends |     |
-2
o t
|     |     |     |     |     | qMt | pMt |     | 0   | 50 100 | 150            | 200 250 | 300 350 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------------- | ------- | ------- |
|     |     |     | nM  |     |     |     |     |     |        | Time (seconds) |         |         |
t
Parameters θ
Figure4.Illustrativeexampleofhowthedifferenceinthetraces
ofnetworkbandwidthandvideowatchtimecreatessignificant
Figure3.Policynetworkarchitecture.Foreachbitrate,theinput
variancefortherewardfeedback.
isfedtoacopyofthesamepolicyneuralnetwork.Wethenapply
a(parameter-free)softmaxoperatortocomputetheprobability
| distribution | of the | next bitrate. | This | architecture |     | can scale to |     |     |     |     |     |     |
| ------------ | ------ | ------------- | ---- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- |
nificantlyaffectsthetotalrewardobservedbytheRLagent.
arbitrarynumberofbitrateencodings.
ConsideranillustrativeexampleshowninFigure4,where
weuseafixedbuffer-basedABRpolicy(Huangetal.,2014)
tomapthesepriorityvaluesintoaprobabilitydistribution to make the bitrate action at time τ. Even for this fixed
(cid:80)M
| pi overeachbitrate: |     | pi  | =exp(qi)/ |     | [exp(qi)]. | Impor- |     |     |     |     |     |     |
| ------------------- | --- | --- | --------- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- |
t t i=1 t policy, if the future trace happens to contain large band-
tantly,thewholepolicynetworkarchitectureisend-to-end
width(e.g.,Trace1),therewardfeedbackwillnaturallybe
differentiableandcanbetrainedwiththepolicygradient large, since the network can support high bitrate without
algorithms(Suttonetal.,1999).
stalls. Incontrast,ifthefuturenetworkconditionbecomes
|           |                                           |     |     |     |     |     | poor | (e.g., Trace | 2), | the reward | will | likely be lower than |
| --------- | ----------------------------------------- | --- | --- | --- | --- | --- | ---- | ------------ | --- | ---------- | ---- | -------------------- |
| Training. | Weusethepolicygradientmethod(Suttonetal., |     |     |     |     |     |      |              |     |            |      |                      |
1999; Sutton & Barto, 2017; Tian et al., 2017) to update average. Moreimportantly,thevideodurationdetermines
thepossiblelengthofABRinteractions,whichdictatesthe
thepolicyneuralnetworkparametersinordertooptimize
totalrewardtheRLagentcanreceivefortraining(e.g.,the
| for the objective. |     | Consider | a simulated |     | video | streaming |     |     |     |     |     |     |
| ------------------ | --- | -------- | ----------- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- |
sessionoflengthT,wheretheagentcollects(state,action, longerwatchtimeinTrace1leadstolargertotalreward).
Thekeyproblemisthatthedifferenceacrossthetracesisin-
| reward) experiences, |     | i.e., | (s ,a | ,r ) | at each | step t. The |                                                     |     |     |     |     |     |
| -------------------- | --- | ----- | ----- | ---- | ------- | ----------- | --------------------------------------------------- | --- | --- | --- | --- | --- |
|                      |     |       | t     | t t  |         |             | dependentwiththebitrateactionattimeτ—e.g.,thefuture |     |     |     |     |     |
policygradientmethodupdatesthepolicyparameterθusing
bandwidthmightfluctuateduetotheinherentstochasticity
theestimatedgradientofthecumulativereward:
inthenetwork;orausermightstopwatchingavideoregard-
|     |          |     |     | (cid:32) |     | (cid:33) |                   |     |                                      |     |     |     |
| --- | -------- | --- | --- | -------- | --- | -------- | ----------------- | --- | ------------------------------------ | --- | --- | --- |
|     |          | T   |     |          | T   |          | lessofthequality. |     | Asaresult,thiscreateslargevariancein |     |     |     |
|     | (cid:88) |     |     | (cid:88) |     |          |                   |     |                                      |     |     |     |
θ ←θ+α ∇ θ logπ θ (s t ,a t ) r t(cid:48) −b t , (2) therewardfeedbackusedforestimatingthepolicygradient
|     | t=1 |     |     | t(cid:48)=t |     |     | inEquation(2). |     |     |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | -------------- | --- | --- | --- | --- | --- |
whereαisthelearningrateandb k isabaselineforreducing Tosolvethisproblem,weadoptarecentlyproposedtech-
thevarianceofthepolicygradient(Weaver&Tao,2001). niqueforhandlinganexogenous,stochasticprocessinthe
|     |     |     |     |     |     |     | environment |     | when training |     | RL agents | (Mao et al., 2019). |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------- | --- | --------- | ------------------- |
Noticethattheestimationoftheadvantageovertheaverage
ThekeyideaistomodifythebaselineinEquation(2)toan
| casereliesontheaccurateestimationoftheaverage. |     |     |     |     |     | For |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thisproblem,thestandardbaselines,suchasthetime-based “input-dependent”onethattakestheinputprocess(e.g.,the
|     |     |     |     |     |     |     | traceinthisproblem)intoaccountexplicitly. |     |     |     |     | Inparticular, |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | ------------- |
baseline(Greensmithetal.,2004;Williams,1992)orvalue
forthisproblem,weimplementtheinput-dependentbase-
function(Mnihetal.,2016),sufferfromlargevariancedue
linebyloadingthesametrace(i.e.,thesametime-seriesfor
| to the stochasticity |     | in  | the traces | (Mao | et al., | 2019). We |     |     |     |     |     |     |
| -------------------- | --- | --- | ---------- | ---- | ------- | --------- | --- | --- | --- | --- | --- | --- |
networkbandwidthandthesamevideowatchtime)multi-
furtherdescribethedetailsofthisvariancein§3.3andour
approachtoreducingit. pletimesandcomputingtheaveragetotalrewardateach
|     |     |     |     |     |     |     | timestepamongthesevideosessions. |     |     |     |     | Essentially,thisuses |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | -------------------- |
thetime-basedbaseline(Greensmithetal.,2004)forEqua-
3.3.VarianceReduction
tion(2)butcomputestheaveragereturnconditionalonthe
ABRL’sRLtrainingonthesimulatorispoweredbyalarge specificinstantiationofatrace. Duringtraining,werepeat
numberofnetworktracescollectedfromthefrontendvideo thisprocedureforalargenumberofrandomly-samplednet-
platform(§3.1). Duringtraining,ABRLmustexperience work traces. As a result, this approach entirely removes
a wide variety of network conditions and video watches thevariancecausedbythedifferenceinfuturenetworkcon-
inordertogeneralizeitsABRpolicywell. However,this dition or the video duration. Since the difference in the
createsachallengefortraining:differenttracescontainvery rewardfeedbackisonlyduetothedifferenceintheactions,
differentnetworkbandwidthandvideoduration,whichsig- thisenablestheRLagenttoassessthequalityofdifferent

Real-worldVideoAdaptationwithReinforcementLearning
actionsmuchmoreaccurately. InFigure7,weshowhow navigatestheexplore/exploittradeoffbasedonasurrogate
thisapproachhelpsimprovethetrainingperformance. model(mostcommonlyaGP).
ApopularacquisitionfunctionforBayesianoptimizationis
3.4.RewardShapingwithBayesianOptimization
|     |     |     |     |     |     |     |     | expectedimprovement(EI)(seeFrazier(2018,§4.1)). |     |     |     |     | The |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- |
ThegoalofABRListooutperformtheexistingABRpolicy basicversionofEIsimplycomputestheexpectedvalueof
accordingtomultipleteam-wideobjectives(i.e.,increasing improvement at each point relative to the best observed
|     |     |     |     |     |     |     |     | point: α | ((cid:126)x|f∗) | =   | E [max(0,f(y) |     | − f∗)], |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | ------------- | --- | ------- |
thevideoqualitywhilereducingthestalltime). Recallthat EI y∼g((cid:126)x|D)
therewardweightsinEquation(1)dictatestheperformance where D (cid:44) {w(cid:126) ,q(w(cid:126) )}N represents N runs of data
|     |     |     |     |     |     |     |     |     |     | i i | i=1 |     |                 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |
|     |     |     |     |     |     |     |     | f∗  |     |     |     |     | g((cid:126)x|D) |
of ABRL’s learned ABR policy in each of the objective points, is the current best observed value and
dimensions. These objectives have an inherent trade-off: denotesthetheposteriordistributionof f valuefromthe
| optimizing | one | dimension | (by | tuning | up the | correspond- |     | surrogate. |     |     |     |     |     |
| ---------- | --- | --------- | --- | ------ | ------ | ----------- | --- | ---------- | --- | --- | --- | --- | --- |
ingrewardweight)diminishestheperformanceinanother
|           |        |      |       |                   |     |     |         | We use | a variant | of EI—Noisy | Expected | Improvement |     |
| --------- | ------ | ---- | ----- | ----------------- | --- | --- | ------- | ------ | --------- | ----------- | -------- | ----------- | --- |
| dimension | (e.g., | high | video | quality increases |     | the | risk of |        |           |             |          |             |     |
(NEI)—whichsupportsoptimizationofnoisy,constrained
stalls).
|     |     |     |     |     |     |     |     | functionevaluations(Lethametal.,2018). |     |     |     | WhileEIand |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | ---------- | --- |
Todeterminethepropercombinationoftherewardweights, its constrained variants (e.g., (Letham et al., 2018)), are
wetreatABRL’sRLtrainingmodule(§3.2,§3.3)asablack designedtooptimizedeterministicfunctions(whichhave
boxfunctionf(w(cid:126)) → (q,l)thatmapstherewardweights aknownbestfeasiblevalues),NEIintegratesovertheun-
w(cid:126) (cid:44)(w ,w ,w ,v ,v )fromEquation(1)toanoisyesti- certaintyinwhichobservedpointsarebest,andweightsthe
|     | b d | c b | d   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mateoftheaveragevideoqualityqandstallratelinunseen valueofeachpointbytheprobabilityoffeasibility.
testvideosessions.
|     |     |     |     |     |     |     |     | NEI naturally | fits | the structure | of the optimization |     | task, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | ------------- | ------------------- | --- | ----- |
Then,weuseBayesianoptimization(Shahriarietal.,2016) sincethetrainingprocedureisstochastic(e.g.,itdepends
toefficientlysearchfortheweightcombinationsthatleadsto ontherandomseed). WethereforeevaluatetheABRLRL
better(q,l),withonlyafewinvocationsoftheRLtraining trainingmodulewithagivenw(cid:126) multipletimesandcompute
module. Thisprocedureoftuningtheweightsinthereward itsstandarderror,whicharethenpassedintotheNEIalgo-
functionisarealizationofrewardshaping(Ngetal.,1999). rithm. NEIsupportsbatchupdating,allowingustoevaluate
Weformulatethemulti-dimensionaloptimizationproblem multiplerewardparameterizationsinparallel.
asaconstrainedoptimizationproblem:
3.5.PolicyTranslation
l(w(cid:126))
|     | argmax | q(w(cid:126)), | subjectto |     | ≤C  |     | (3) |     |     |     |     |     |     |
| --- | ------ | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
w(cid:126) l Inpractice,mostvideoplayersexecutetheABRalgorithms
s
inthefrontendtoavoidtheextralatencyconnectingtothe
Whereq(w(cid:126))andl(w(cid:126))arethequalityandstallrateevaluated backend(Akhshabietal.,2011;Sodagar,2011;Adhikari
|     |     |     |     |     |     |     |     | et al., 2012; | Huang | et al., | 2014). Therefore, | we  | need to |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | ------- | ----------------- | --- | ------- |
atw(cid:126),l s isthestallrateoftheexistingpolicy(non-RLbased)
usedinproductionatFacebook,andC issomeconstraint deploythelearnedABRpolicytotheusersdirectly—i.e.,
value. the design of an ABR server in the back end hosting the
|        |          |          |      |          |         |      |        | requestsfromallusersisnotideal(Maoetal.,2017). |     |     |     |     | To  |
| ------ | -------- | -------- | ---- | -------- | ------- | ---- | ------ | ---------------------------------------------- | --- | --- | --- | --- | --- |
| Notice | that the | function | q(·) | and l(·) | are can | only | be ob- |                                                |     |     |     |     |     |
massivelydeploy,wemakeuseoftheweb-basedvideoplat-
servedbyrunningtheRLtrainingmodule—acomputation-
formatFacebook,wherethefrontendservice(ifuncached)
| ally intensive |     | procedure. | We  | solve this | constrained |     | opti- |     |     |     |     |     |     |
| -------------- | --- | ---------- | --- | ---------- | ----------- | --- | ----- | --- | --- | --- | --- | --- | --- |
fetchesthemostup-to-datevideoplayer(includingtheABR
| mization | problem | with | Bayesian | optimization. |     | Bayesian |     |     |     |     |     |     |     |
| -------- | ------- | ---- | -------- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
policy)fromthebackendserveratthebeginningofavideo
| optimization |     | uses a Gaussian |     | process | (GP) | (Rasmussen, |     |     |     |     |     |     |     |
| ------------ | --- | --------------- | --- | ------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
streamingsession.
2004)surrogatemodeltoapproximatetheresultsoftheRL
trainingprocedureusingalimitednumberoftrainingruns. Foreaseofunderstandingandmaintenanceindeployment,
Gaussian processes are flexible non-parametric Bayesian we translate the neural network ABR policy to an inter-
modelsrepresentingaposteriordistributionoverpossible pretable form. In particular, we found that the learned
|        |           |            |     |          |       |         |      | ABR policies | approximately |     | exhibit a linear | structure— |     |
| ------ | --------- | ---------- | --- | -------- | ----- | ------- | ---- | ------------ | ------------- | --- | ---------------- | ---------- | --- |
| smooth | functions | compatible |     | with the | data. | We find | that |              |               |     |                  |            |     |
GPsareexcellentmodelsoftheoutputoftheRLtraining the bitrate decision boundaries are approximately linear
module,assmallchangestotherewardfunctionwillresult and the distances between the boundaries are constant in
insmallchangesintheoveralloutcomes. Furthermore,GPs part of the decision space. As a result, we approximate
areknowntoproducegoodestimatesofuncertainty. thelearnedABRpolicywithadeterministiclinearfitting
|     |     |     |     |     |     |     |     | function. | Specifically,wefirstrandomlypickN |     |     |     | tuplesof |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------------------------------- | --- | --- | --- | -------- |
UsingBayesianoptimization,westartfromaninitialsetof
|          |        |                |       |             |      |     |        | bandwidth | prediction | x and     | buffer occupancy | o      | (see the |
| -------- | ------ | -------------- | ----- | ----------- | ---- | --- | ------ | --------- | ---------- | --------- | ---------------- | ------ | -------- |
| M design | points | {w(cid:126) }M | , and | iteratively | test | new | points |           |            |           |                  |        |          |
|          |        | i              | i=1   |             |      |     |        | inputs in | Figure     | 3). Then, | for each tuple   | values | (x,o)    |
ontheRLmoduleaccordingtoanacquisitionfunctionthat

Real-worldVideoAdaptationwithReinforcementLearning
| and for each                                          | of the M                           | equally spaced | bitrates | with file |     |               |     |     |            |     |
| ----------------------------------------------------- | ---------------------------------- | -------------- | -------- | --------- | --- | ------------- | --- | --- | ---------- | --- |
|                                                       |                                    |                |          |           |     | Video quality |     |     | Stall rate |     |
| sizesn1,n2,···                                        | ,nM,weinvokethepolicynetworktocom- |                |          |           |     |               |     |     |            |     |
|                                                       |                                    |                |          |           | 4%  |               |     | 4%  |            |     |
| putetheprobabilityofselectingthecorrespondingbitrate: |                                    |                |          |           | 2%  |               |     | 2%  |            |     |
|                                                       |                                    |                |          |           | 0   |               |     | 0   |            |     |
| π(a1|x,o,n1),π(a2|x,o,n2),···                         |                                    | ,π(aM|x,o,nM). |          | Next,     |     |               |     |     |            |     |
|                                                       |                                    |                |          |           | -2% |               |     | -2% |            |     |
wedeterminethe“intended”bitrateusingaweightedsum:
|     |     |     |     |     | -4% |     |     | -4% |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:80)M
n¯ = niπ(ai|x,o,ni). Thisservesasthetargetbitrate Mon Tue Wed Thu Fri Sat Sun Mon Tue Wed Thu Fri Sat Sun
i=1
fortheoutputofthelinearfittingfunction. Finally,weuse (a) Videoquality (b) Stallrate
threeparametersa,b,andc,tofitalinearmodelofband-
Figure5.Aweek-longperformancecomparisonwithproduction
| width prediction            | and buffer | occupancy, | which   | minimizes |            |                                         |     |     |     |     |
| --------------------------- | ---------- | ---------- | ------- | --------- | ---------- | --------------------------------------- | --- | --- | --- | --- |
|                             |            |            |         |           | ABRpolicy. | Thecomparisonissampledfromover30million |     |     |     |     |
| themeansquarederroroverallN |            |            | points: |           |            |                                         |     |     |     |     |
videostreamingsession.Theboxspans95%confidenceintervals
andthebarsspans99%confidenceintervals.
N
|     | (cid:88)(cid:12) |               | (cid:12)2   |     |     |     |     |     |     |     |
| --- | ---------------- | ------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
|     | (cid:12)ax       | i +bo i +c−n¯ | i(cid:12) . | (4) |     |     |     |     |     |     |
i=1
andstallrate.
| Here, we | use the standard | least square | estimator | for the |     |     |     |     |     |     |
| -------- | ---------------- | ------------ | --------- | ------- | --- | --- | --- | --- | --- | --- |
modelfitting,whichistheoptimalunbiasedlinearestima- Overall,ABRLachievesa1.6%increaseinaveragebitrate
tor(Zyskind&Martin,1969). Atinferencetime,thefront and a 0.4% decrease in stall rate. Most notably, ABRL
endvideoplayerusesthefittedlinearmodeltodetermine consistentlyselectshigherbitratethroughthewholeweek
theintendedbitrateandthenselectsthemaximumavailable (99% confidence intervals all positive). However, choos-
bitratethatisbelowtheintendedbitrate. ing higher bitrates does not sacrifice stall rate— ABRL
|     |     |     |     |     | rivals or | outperforms | the | default scheme | on the | average |
| --- | --- | --- | --- | --- | --------- | ----------- | --- | -------------- | ------ | ------- |
TranslatingtheneuralnetworkABRpolicyprovidesinter-
stallrateeveryday,evenonThursdaywhengainsinvideo
pretabilityforhumanengineersbutitisalsoacompromise
|     |     |     |     |     | qualityarehighest. |     | ThisshowsABRLusestheoutputfrom |     |     |     |
| --- | --- | --- | --- | --- | ------------------ | --- | ------------------------------ | --- | --- | --- |
intermsofABRperformance(§4.2empiricallyevaluates
thebandwidthpredictionmodulebetterthanthefine-tuned
| thistrade-off). | Also,addingmorecontextualbasedfeatures |     |     |     |            |             |             |      |              |       |
| --------------- | -------------------------------------- | --- | --- | --- | ---------- | ----------- | ----------- | ---- | ------------ | ----- |
|                 |                                        |     |     |     | heuristic. | By directly | interacting | with | the observed | data, |
wouldlikelyrequireanon-linearpolicyencodeddirectlyin
ABRLlearnsquantitativelyhowconservativeoraggressive
| aneuralnetwork(§5).                     | Itisworthnotingthatdirectlyusing |     |     |            |              |           |         |                     |             |        |
| --------------------------------------- | -------------------------------- | --- | --- | ---------- | ------------ | --------- | ------- | ------------------- | ----------- | ------ |
|                                         |                                  |     |     |            | the ABR      | should    | be with | different predicted | bandwidths. |        |
| RLtotrainalinearpolicyisanaturalchoice. |                                  |     |     | However,to |              |           |         |                     |             |        |
|                                         |                                  |     |     |            | As a result, | this also | leads   | to a 0.2%           | improvement | in the |
oursurprise,trainingABRLwithalinearpolicyfunction
end-uservideowatchtime.
leadstoworseABRperformancethantheexistingheuris-
tics. Wehypothesizethisisbecausepolicygradientwith Theseimprovementnumbersmaylookmodestcomparedto
aweakfunctionapproximatorsuchasalinearonehasdif- thethosereportedbyrecentacademicpapers(Huangetal.,
ficultyconvergingtotheoptimal,eventhoughtheoptimal 2014;Spiterietal.,2016;Yinetal.,2015;Maoetal.,2017).
policycanbesimple(Luetal.,2018;Fujimotoetal.,2018; Thisismostlybecauseweonlyexperimentwithwebbased
Fairbank&Alonso,2012;Achiametal.,2019). videos,whichprimarilyconsistofwell-connecteddesktop
orlaptoptraffic,differentfromthepriorschemesthatmostly
|     |     |     |     |     | concerncellularandunstablenetworks. |     |     |     | Nonetheless,any |     |
| --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --------------- | --- |
4.Experiments
non-zeroimprovementissignificantgiventhemassivevol-
WeevaluateABRLwithFacebook’sweb-basedproduction umeofFacebookvideos. Inthefollowing,weprofilethe
videoplatform. Ourexperimentsanswerthefollowingques- performancegainatamoregranularlevel.
tions: (1)DoesABRLprovidegainsinperformanceover
theexistingheuristic-basedproductionABRalgorithm? (2) 4.2.DetailedAnalysisofRLPipeline
HowaredifferentsubgroupsaffectedbytheABRL-based
|                                        |     |     |     |         | Rewardshaping. |     | Tooptimizethemulti-dimensionalobjec- |     |     |     |
| -------------------------------------- | --- | --- | --- | ------- | -------------- | --- | ------------------------------------ | --- | --- | --- |
| policy? (3)WhatABRpolicydoesABRLlearn? |     |     |     | (4)Dur- |                |     |                                      |     |     |     |
ingtraining,howdodifferentdesigncomponentsaffectthe tive,weuseaBayesianOptimizationapproachforreward
|     |     |     |     |     | shaping(§3.4). | Thegoalistotunetheweightsinthereward |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | ------------------------------------ | --- | --- | --- | --- |
learningprocedure?
functioninordertotrainapolicythatoperatesonthePareto
frontierofvideoqualityandstall(and,ideally,outperform
4.1.Overallliveperformance
|     |     |     |     |     | theexistingpolicyinbothdimensions). |     |     |     | Figure6showsthe |     |
| --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --------------- | --- |
Inaweek-longdeploymentonFacebook’sproductionvideo performancefromdifferentrewardweightsduringthere-
platform, we compare the performance of ABRL’s trans- wardshapingprocedure.Ateachiteration,wesetthereward
latedABRpolicy(§3.5)withthatoftheexistingheuristic- weights using the output from the Bayesian optimization
based ABR algorithm. The experiment includes over 30 module, andtreatABRL’sRLmoduleasablackbox, in
millionworldwidevideoplaybacksessions. Figure5shows whichthepolicyistraineduntilconvergenceaccordingto
therelativeimprovementofABRLintermsofvideoquality thechosenrewardweights.TheBayesianoptimizationmod-

Real-worldVideoAdaptationwithReinforcementLearning
Default ABR policy
|     | )delacs tinu( emit llatS Initial random search |     |     |              | 5.0 |     |
| --- | ---------------------------------------------- | --- | --- | ------------ | --- | --- |
|     | 4 BO 1st round                                 |     |     |              |     |     |
|     | BO 2nd round                                   |     |     | drawer latoT | 2.5 |     |
BO 3rd round
|     | 3   |     |     |     | 0.0 |     |
| --- | --- | --- | --- | --- | --- | --- |
B etter
2.5
2
|     |       |       |       |     | 5.0         | Input dependent |
| --- | ----- | ----- | ----- | --- | ----------- | --------------- |
|     |       |       |       |     | 7.5         | State dependent |
|     | 1     |       |       |     | 0 2000 4000 | 6000 8000 10000 |
|     | 1 1.5 | 2 2.5 | 3 3.5 | 4   |             |                 |
Iterations
Video quality (unit scaled)
Figure7.Improvementslearningperformanceduetovariancere-
duction.Thenetworkconditionandwatchtimeindifferenttraces
| Figure6.Reward | shaping | via Bayesian | optimization | using the |     |     |
| -------------- | ------- | ------------ | ------------ | --------- | --- | --- |
introducesvarianceinthepolicygradientestimation.Theinput-
| ABRLsimulator. | Theinitialroundhas64randominitialparam- |     |     |     |     |     |
| -------------- | --------------------------------------- | --- | --- | --- | --- | --- |
dependentbaselinehelpsreducesuchvarianceandimprovetrain-
eters. SuccessivebatchesofBayesianoptimizationconvergeto
ingperformance.Shadedareaspans±std.
optimalweightingsthatimprovevideoqualitywhilereducingstall
rate.Theperformanceistestedonheldoutnetworktraces.
ulethenobservesthetestingoutcomes(bothvideoquality
andstall)andsetsthesearchcriteriaforthenextiterationto
be“expectedimprovementinvideoqualitysuchthatstall
| timedegradesnomorethan5%”. |     |     | Asshown,withinthree |     |     |     |
| -------------------------- | --- | --- | ------------------- | --- | --- | --- |
iterations,ABRLisabletohoneinontheempiricalPareto
frontier. Inthissearchspace,therearemanymoreweight
| configurations | that lead | to better | video quality | (i.e., right |     |     |
| -------------- | --------- | --------- | ------------- | ------------ | --- | --- |
ofthedashedline)thantheconfigurationsleadingtofewer
| stalls | (i.e., lower than | the dashed | line). Compared | to the |     |     |
| ------ | ----------------- | ---------- | --------------- | ------ | --- | --- |
existingABRscheme,ABRLfindsafewcandidatereward
weightsthatleadtobetterABRpolicybothintermsofvideo
qualityandstalls(i.e.,lowerandtotherightoftheexisting (a) Videoquality (b) Stall
policy). Fortheproductionexperimentin§4.1,wedeploy
Figure8.PerformancecomparisonofABRLanditslinearapprox-
thepolicieswithintheregionthatshowsthelargestimprove-
imatedvariant.Theagentsaretestedwithunseentracesinsimula-
mentinstall. Afterthissearchprocedure,engineersonthe tion.Translatingthepolicydegradestheaverageperformanceby
videoteamcanpickpoliciesbasedondifferentdeployment 0.8%installand0.6%inquality.
objectivesaswell.
| Variancereduction. | Toreducethevarianceintroducedby |     |     |     |     |     |
| ------------------ | ------------------------------- | --- | --- | --- | --- | --- |
thepolicygradientestimationgiventheuncertaintiesinthe
thenetworkandthewatchtimeacrossdifferentthetraces,
trace. Fixingthetraceateachtrainingiterationremovesthe
wecomputethebaselineforpolicygradientbyaveraging
varianceintroducedbytheexternalinputprocess,making
overthecumulativerewardsfromthesametrace(inallthe
thetrainingsignificantlymorestable.
parallelrollouts)ateachiteration,effectivelyachievingthe
input-dependentbaseline(§3.3). Forcomparison,wealso Trade-off of performance for interpretability. Figure 8
trainanagentwiththeregularstate-dependentbaseline(i.e., shows how the testing performance of video quality and
outputfromavaluefunctionthatonlytakesthestateobser- stallinsimulationdifferbetweenABRL’soriginalneural
vationasinput). Figure7evaluatestheimpactofvariance networkpolicyandthetranslatedpolicy(§3.5). Mostno-
reductionbycomparingthelearningcurvetrainedwiththe ticeably, making the ABR policy linear and interpretable
input-dependentbaselinetothatwiththestate-dependent incursa0.8%and8.9%degradationinthemeanand95th
baseline. As shown, the agent with the input-dependent percentile of stall rate. This accounts for the tradeoff to
baselineachievesabout12%highereventualtotalreward makethelearnedABRpolicyfullyinterpretable. Also,we
(i.e., the direct objective of RL training). Moreover, we triedtotrainalinearpolicydirectlyfromscratch(byremov-
findthattheagentwithinput-dependentbaselineconverges inghiddenlayersintheneuralnetworkandremovingallthe
faster in terms of the entropy of thepolicy, whichis also non-lineartransformations). However,theperformanceof
indicatedbythenarrowershadedareainFigure7. Ateach thedirectlylearnedlinearpolicydoesnotoutperformtheex-
point in the learning curve, the standard deviation of re- istingbaseline. Thisinpartisbecauseover-parametrization
wards is around half as large under the input-dependent inthepolicynetworkhelpslearnamorerobustpolicy(Lu
baseline. Thisisexpectedbecauseofthelargevariancein etal.,2018;Fairbank&Alonso,2012).

Real-worldVideoAdaptationwithReinforcementLearning
Second,weprimarilyevaluateABRLonFacebook’sweb-
|     |     |     |     | basedvideoplatform, |     | becauseithasthefastestcodebase |     |     |
| --- | --- | --- | --- | ------------------- | --- | ------------------------------ | --- | --- |
updatecycle(unlikemobiledevelopment,wheretheupdates
|     |     |     |     | arebatchedinnewversionreleases). |     |     | However,thenetwork |     |
| --- | --- | --- | --- | -------------------------------- | --- | --- | ------------------ | --- |
conditionsforcellularnetworkshavelargervariabilityand
aremoreunpredictable,wherethegainofanRL-basedABR
schemecanbelarger(e.g.,weobservedlargerperformance
gainforABRLwhenthenetworkconditionispoorin§4.2.
Developingasimilarlearningframeworkformobileclients
canpotentiallyleadtolargerABRimprovements.
|     |     |     |     | Third, the | gains from | using ABRL | are rather | modest, as |
| --- | --- | --- | --- | ---------- | ---------- | ---------- | ---------- | ---------- |
theyuseonlythesamestatevariables(§3.2)asthecurrent
|                           |     |                        |     | heuristic-basedABRalgorithm. |     |     | Givenafixedparameteriza- |     |
| ------------------------- | --- | ---------------------- | --- | ---------------------------- | --- | --- | ------------------------ | --- |
| (a) Videoqualitybreakdown |     | (b) Stallratebreakdown |     |                              |     |     |                          |     |
tionofasimplepolicy,othertechniquessuchasBayesian
optimizationcurrentlyserveasamorepracticalalternative
Figure9.Breakdowntheperformancecomparisonwithdifferent
toRL.However,ABRLcanalsoweextendthestatespaceto
| networkqualityfortheliveexperiment. |     | “slownetwork”corre- |     |     |     |     |     |     |
| ----------------------------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
incorporatemorecontextualfeatures,suchasvideostream-
| spondsto< | 500kbpsmeasurednetworkbandwidth, |     | and“fast |     |     |     |     |     |
| --------- | -------------------------------- | --- | -------- | --- | --- | --- | --- | --- |
network”correspondsto>10mbpsbandwidth. Theboxspans ingregions,temporalinformation,andthecontentsofthe
95%confidenceintervalsandthebarsspans99%confidencein- video itself (since categorizing and optimizing the video
qualitybasedonvideocontenttypescanlikelyresultinbet-
tervals.
terperceptualquality),whichengineerscannoteasilyfold
|                   |                               |     |     | intoheuristics. | WeexpectthatRLmethodsprovidemore |     |     |     |
| ----------------- | ----------------------------- | --- | --- | --------------- | -------------------------------- | --- | --- | --- |
| Subgroupanalysis. | TobetterunderstandhowABRLout- |     |     |                 |                                  |     |     |     |
practicalbenefitwhenthestatefeaturesbecomericher.
performstheexistingABRscheme,webreakdowntheper-
formancegainindifferentnetworkconditionsandwevisu- Lastly,thereexistsadiscrepancybetweensimulatedbuffer
alizetheABRpolicylearnedbyABRL.
dynamicsandtherealvideostreamingsessioninpractice.
Betterbridgingthisgapcanincreasethegeneralizabilityof
InFigure9,wecategorizethevideosessionsbasedonthe
|                                   |     |     |              | ABRL’slearnedpolicy. |     | Tothisend,thereisongoingwork |     |     |
| --------------------------------- | --- | --- | ------------ | -------------------- | --- | ---------------------------- | --- | --- |
| averagemeasurednetworkbandwidths. |     |     | Asshown,ABRL |                      |     |                              |     |     |
addressingthediscrepancybetweensimulationandreality
| overall achieves | a higher bitrate | while | maintaining fewer |     |     |     |     |     |
| ---------------- | ---------------- | ----- | ----------------- | --- | --- | --- | --- | --- |
withBayesianoptimizationinrewardshaping(Letham&
| stallsinbothfastandslownetworks. |     | Moreover,ABRLper- |     |     |     |     |     |     |
| -------------------------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
formssignificantlybetterinslownetworkconditions,where Bakshy,2019). Furthermore,anotherviableapproachisto
|                  |                |           |                 | directlyperformRLtrainingontheproductionsystem. |             |              |             | The           |
| ---------------- | -------------- | --------- | --------------- | ----------------------------------------------- | ----------- | ------------ | ----------- | ------------- |
| it delivers 5.9% | higher bitrate | with 2.4% | fewer stalls on |                                                 |             |              |             |               |
|                  |                |           |                 | challenge                                       | for this is | to construct | a similarly | safe training |
average. Whenthenetworkconnectivityisunstable,ABR
mechanism(Alshiekhetal.,2018)thatpreventstheinitial
ischallenging—acontrollermustagilelyswitchtolower
RLtrialsfromdecreasingperceptualqualityofavideo(e.g.,
bitratewhenthebandwidthpredictionorbufferlevelislow,
butmustavoidbeingtooconservativebypersistentlystick- restrictingtheinitialRLpolicyfromrandomlyselectpoor
bitrates).
ingwithlowbitrates(whenisisfeasibletousehigherbitrate
| withoutstalling). | Intheslownetworkcondition,ABRLem- |     |     |     |     |     |     |     |
| ----------------- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
6.Conclusion
piricallyusesthenoisynetworkbandwithestimationbetter
thantheheuristicsysteminordertomaintainbetterbuffer
levels. ThisindicatesthatABRLoptimizesalgorithmper- We presented ABRL, a system that uses RL to automat-
|     |     |     |     | ically learn | high-quality | ABR algorithms | for | Facebook’s |
| --- | --- | --- | --- | ------------ | ------------ | -------------- | --- | ---------- |
formanceundernetworkconditionsthatexistingschemes
|     |     |     |     | productionweb-basedvideoplatform. |     |     | ABRLhasseveral |     |
| --- | --- | --- | --- | --------------------------------- | --- | --- | -------------- | --- |
mayoverlook.
customizedcomponentsforsolvingthechallengesinpro-
|     |     |     |     | ductiondeployment, |     | includingascalablearchitecturefor |     |     |
| --- | --- | --- | --- | ------------------ | --- | --------------------------------- | --- | --- |
5.Discussion videoswitharbitrarybitrates,avariancereductionRLtrain-
ingmethodandaBayesianoptimizationschemeforreward
Weintendtoworkonseveraldirectionstofurtherenhance
shaping. Fordeployment,wetranslateABRL’spolicytoan
| ABRLintheproductionsystems. |     | First,ABRL’straining |     |     |     |     |     |     |
| --------------------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
isonlyperformedonceofflinewithpre-collectednetwork interpretableformforbettermaintenanceandsafety. Ina
week-longworldwidedeploymentwithmorethan30mil-
traces. Tobetterincorporatewiththeupdatesinthebackend
lionvideostreamingsessions,ourRLapproachoutperforms
infrastructure,wecansetupacontinualretrainingroutine
theexistingcarefully-tunedABRalgorithmbyatleast1.6%
| weekly or daily. | Prior studies | have shown | the benefit of |     |     |     |     |     |
| ---------------- | ------------- | ---------- | -------------- | --- | --- | --- | --- | --- |
invideoqualityand0.4%install.
continualtrainingwitheverupdatingsystems(Systems&
Research,2019).

Real-worldVideoAdaptationwithReinforcementLearning
| References |             |     |             |            |         | Hagan,M.T.,Demuth,H.B.,Beale,M.H.,andDeJesu´s, |                 |     |                |         |     |
| ---------- | ----------- | --- | ----------- | ---------- | ------- | ---------------------------------------------- | --------------- | --- | -------------- | ------- | --- |
|            |             |     |             |            |         | O. Neural                                      | network design. |     | PWS publishing | company |     |
| Achiam,    | J., Knight, | E., | and Abbeel, | P. Towards | charac- |                                                |                 |     |                |         |     |
Boston,1996.
| terizing | divergence | in  | deep q-learning. | arXiv | preprint |     |     |     |     |     |     |
| -------- | ---------- | --- | ---------------- | ----- | -------- | --- | --- | --- | --- | --- | --- |
arXiv:1903.08894,2019.
Huang,T.-Y.,Johari,R.,McKeown,N.,Trunnell,M.,and
Watson,M.ABuffer-basedApproachtoRateAdaptation:
| Adhikari,V.K.,Jain,S.,Chen,Y.,andZhang,Z.-L. |     |                           |     |     | Vivi-  |               |         |       |           |          |     |
| -------------------------------------------- | --- | ------------------------- | --- | --- | ------ | ------------- | ------- | ----- | --------- | -------- | --- |
|                                              |     |                           |     |     |        | Evidence from | a Large | Video | Streaming | Service. | In  |
| sectingyoutube:                              |     | Anactivemeasurementstudy. |     |     | In2012 |               |         |       |           |          |     |
Proceedingsofthe2014ACMConferenceonSIGCOMM,
| Proceedings |     | IEEE INFOCOM, | pp. | 2521–2525. | IEEE, |     |     |     |     |     |     |
| ----------- | --- | ------------- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- |
SIGCOMM.ACM,2014.
2012.
|                                       |     |     |     |              |     | Krishnan,S.S.andSitaraman,R.K. |     |     | VideoStreamQual-        |     |     |
| ------------------------------------- | --- | --- | --- | ------------ | --- | ------------------------------ | --- | --- | ----------------------- | --- | --- |
| Akhshabi,S.,Begen,A.C.,andDovrolis,C. |     |     |     | Anexperimen- |     |                                |     |     |                         |     |     |
|                                       |     |     |     |              |     | ityImpactsViewerBehavior:      |     |     | InferringCausalityUsing |     |     |
talevaluationofrate-adaptationalgorithmsinadaptive
|     |     |     |     |     |     | Quasi-experimentalDesigns. |     |     | InProceedingsofthe2012 |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | ---------------------- | --- | --- |
streamingoverhttp.InProceedingsoftheSecondAnnual
ACMConferenceonInternetMeasurementConference,
ACMConferenceonMultimediaSystems,MMSys.ACM,
IMC.ACM,2012.
2011.
|           |     |            |             |                  |        | Lederer,S.,Mu¨ller,C.,andTimmerer,C. |                    |     | Dynamicadaptive |        |     |
| --------- | --- | ---------- | ----------- | ---------------- | ------ | ------------------------------------ | ------------------ | --- | --------------- | ------ | --- |
| Alshiekh, | M., | Bloem,     | R., Ehlers, | R., Ko¨nighofer, | B.,    |                                      |                    |     |                 |        |     |
|           |     |            |             |                  |        | streaming                            | over http dataset. |     | In Proceedings  | of the | 3rd |
| Niekum,   | S., | and Topcu, | U. Safe     | reinforcement    | learn- |                                      |                    |     |                 |        |     |
MultimediaSystemsConference,pp.89–94.ACM,2012.
| ingviashielding. |     | InThirty-SecondAAAIConferenceon |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ArtificialIntelligence,2018. Letham,B.andBakshy,E. Bayesianoptimizationforpolicy
|             |     |                                       |     |     |     | searchviaonline-offlineexperimentation. |     |     |     | arXivpreprint |     |
| ----------- | --- | ------------------------------------- | --- | --- | --- | --------------------------------------- | --- | --- | --- | ------------- | --- |
| Bishop,C.M. |     | PatternRecognitionandMachineLearning. |     |     |     |                                         |     |     |     |               |     |
arXiv:1904.01049,2019.
| Springer,2006. |     | ISBN0387310738. |     |     |     |                                               |     |     |     |     |      |
| -------------- | --- | --------------- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | ---- |
|                |     |                 |     |     |     | Letham,B.,Karrer,B.,Ottoni,G.,Bakshy,E.,etal. |     |     |     |     | Con- |
Cisco. Ciscovisualnetworkingindex:Forecastandmethod-
strainedbayesianoptimizationwithnoisyexperiments.
| ology,2015-2020. |     | 2016. |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
BayesianAnalysis,2018.
Claeys,M.,Latre´,S.,Famaey,J.,Wu,T.,VanLeekwijck, Lu,T.,Schuurmans,D.,andBoutilier,C. Non-delusional
| W.,andDeTurck,F. |     | Designofaq-learning-basedclient |     |     |     |            |                      |     |            |              |     |
| ---------------- | --- | ------------------------------- | --- | --- | --- | ---------- | -------------------- | --- | ---------- | ------------ | --- |
|                  |     |                                 |     |     |     | q-learning | and value-iteration. |     | In Bengio, | S., Wallach, |     |
qualityselectionalgorithmforhttpadaptivevideostream- H.,Larochelle,H.,Grauman,K.,Cesa-Bianchi,N.,and
ing. InAdaptiveandLearningAgentsWorkshop,2013. Garnett,R.(eds.),AdvancesinNeuralInformationPro-
cessingSystems31,pp.9949–9959.2018.
| Dobrian, | F., Sekar, | V., | Awan, A., Stoica, | I., | Joseph, D., |     |     |     |     |     |     |
| -------- | ---------- | --- | ----------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Ganjam, A., Zhan, J., and Zhang, H. Understanding Mao,H.,Netravali,R.,andAlizadeh,M. Neuraladaptive
the Impact of Video Quality on User Engagement. In Proceedings of the
|     |     |     |     |     |     | video streaming | with | pensieve. | In  |     |     |
| --- | --- | --- | --- | --- | --- | --------------- | ---- | --------- | --- | --- | --- |
ProceedingsoftheACMSIGCOMM2011Conference,
ACMSIGCOMM2017Conference.ACM,2017.
SIGCOMM.ACM,2011.
|                         |     |     |                           |     |     | Mao, H., Venkatakrishnan, |                                         | S.  | B., Schwarzkopf, | M., | and |
| ----------------------- | --- | --- | ------------------------- | --- | --- | ------------------------- | --------------------------------------- | --- | ---------------- | --- | --- |
| Fairbank,M.andAlonso,E. |     |     | Thedivergenceofreinforce- |     |     |                           |                                         |     |                  |     |     |
|                         |     |     |                           |     |     | Alizadeh,M.               | Variancereductionforreinforcementlearn- |     |                  |     |     |
mentlearningalgorithmswithvalue-iterationandfunc- ingininput-drivenenvironments. Proceedingsofthe7th
tionapproximation. InThe2012InternationalJointCon- InternationalConferenceonLearningRepresentations
| ference | on Neural | Networks | (IJCNN), | pp. | 1–8. IEEE, |     |     |     |     |     |     |
| ------- | --------- | -------- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
(ICLR),2019.
2012.
Mnih,V.,Badia,A.P.,Mirza,M.,Graves,A.,Harley,T.,
Frazier, P. I. A tutorial on bayesian optimization. arXiv Lillicrap,T.P.,Silver,D.,andKavukcuoglu,K. Asyn-
preprintarXiv:1807.02811,2018.
|     |     |     |     |     |     | chronousmethodsfordeepreinforcementlearning. |     |     |     |     | In  |
| --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
ProceedingsoftheInternationalConferenceonMachine
Fujimoto,S.,Hoof,H.,andMeger,D. Addressingfunction Learning,pp.1928–1937,2016.
| approximationerrorinactor-criticmethods. |     |     |     |     | InInterna- |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
tionalConferenceonMachineLearning,pp.1582–1591, Ng, A. Y., Harada, D., and Russell, S. Policy invariance
| 2018. |     |     |     |     |     | underrewardtransformations: |                                  |     | Theoryandapplicationto |     |     |
| ----- | --- | --- | --- | --- | --- | --------------------------- | -------------------------------- | --- | ---------------------- | --- | --- |
|       |     |     |     |     |     | rewardshaping.              | InICML,volume99,pp.278–287,1999. |     |                        |     |     |
Greensmith,E.,Bartlett,P.L.,andBaxter,J.Variancereduc-
tiontechniquesforgradientestimatesinreinforcement Rasmussen,C.E. Gaussianprocessesinmachinelearning.
learning. JournalofMachineLearningResearch,5(Nov): In Advanced lectures on machine learning, pp. 63–71.
| 1471–1530,2004. |     |     |     |     |     | Springer,2004. |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |

Real-worldVideoAdaptationwithReinforcementLearning
Sandvine. Global internet phenomena-latin american & Yin,X.,Jindal,A.,Sekar,V.,andSinopoli,B. AControl-
northamerica. 2015. TheoreticApproachforDynamicAdaptiveVideoStream-
ingoverHTTP. InProceedingsofthe2015ACMConfer-
Sandvine, I. Global internet phenomena report. North enceonSpecialInterestGrouponDataCommunication,
AmericaandLatinAmerica,2018. SIGCOMM.ACM,2015.
Shahriari, B., Swersky, K., Wang, Z., Adams, R. P., and Zyskind, G. and Martin, F. B. On best linear estimation
DeFreitas,N.Takingthehumanoutoftheloop:Areview andgeneralgauss-markovtheoreminlinearmodelswith
ofbayesianoptimization. ProceedingsoftheIEEE,104 arbitrarynonnegativecovariancestructure. SIAMJournal
(1):148–175,2016. onAppliedMathematics,17(6):1190–1202,1969.
Sodagar,I. Thempeg-dashstandardformultimediastream-
ing over the internet. IEEE MultiMedia, 18(4):62–67,
2011.
Spiteri, K., Urgaonkar, R., and Sitaraman, R. K. BOLA:
near-optimalbitrateadaptationforonlinevideos. InInfo-
com,2016.
Sutton,R.S.andBarto,A.G. ReinforcementLearning: An
Introduction,SecondEdition. MITPress,2017.
Sutton,R.S.,McAllester,D.A.,Singh,S.P.,andMansour,
Y. Policy gradient methods for reinforcement learning
with function approximation. In NIPS, volume 99, pp.
1057–1063,1999.
Systems, S. and Research, N. Puffer: stream live tv in
yourbrowser. https://puffer.stanford.edu/
faq/,2019.
Tian,Y.,Gong,Q.,Shang,W.,Wu,Y.,andZitnick,C.L.Elf:
Anextensive,lightweightandflexibleresearchplatform
for real-time strategy games. In Advances in Neural
InformationProcessingSystems,pp.2659–2669,2017.
vanderHooft,J.,Petrangeli,S.,Claeys,M.,Famaey,J.,and
DeTurck,F. Alearning-basedalgorithmforimproved
bandwidth-awarenessofadaptivestreamingclients. In
2015IFIP/IEEEInternationalSymposiumonIntegrated
NetworkManagement.IEEE.
Wagner, K. Facebook says video is huge –
100-million-hours-per-day huge. https:
//www.vox.com/2016/1/27/11589140/
facebook-says-video-is-huge-100-million-hours-per-day-huge,
2016.
Weaver, L. and Tao, N. The optimal reward baseline for
gradient-basedreinforcementlearning. InProceedings
oftheSeventeenthconferenceonUncertaintyinartificial
intelligence,pp.538–545.MorganKaufmannPublishers
Inc.,2001.
Williams,R.J. Simplestatisticalgradient-followingalgo-
rithmsforconnectionistreinforcementlearning. Machine
learning,8(3-4):229–256,1992.