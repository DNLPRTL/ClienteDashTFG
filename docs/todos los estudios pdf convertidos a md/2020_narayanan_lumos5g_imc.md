Lumos5G: Mapping and Predicting
Commercial mmWave 5G Throughput
ArvindNarayanan,EmanRamadan,RishabhMehta,XinyueHu,QingxuLiu,RostandA.K.Fezeu,
UdhayaKumarDayalan,SaurabhVerma,PeiqiJi,TaoLi,FengQian,Zhi-LiZhang
DepartmentofComputerScience&Engineering,UniversityofMinnesota–TwinCities,U.S.A.
fivegophers@umn.edu*
ABSTRACT 1 INTRODUCTION
Theemerging5Gservicesoffernumerousnewopportunitiesfornet- With new radio (NR) specifications (5G NR [19]) that cover a
workedapplications.Inthisstudy,weseektoanswertwokeyques- wide spectrum of frequencies from low-band, to mid-band and
tions:i)isthethroughputofmmWave5Gpredictable,andii)can high-bandwithflexiblewaveform,the5thgeneration(5G)cellular
webuild“good”machinelearningmodelsfor5Gthroughputpredic- technologyisenvisagedtoofferawholegamutofnewservices
tion?Tothisend,weconductameasurementstudyofcommercial from Ultra-Reliable Low-Latency Communication (URLLC) and
mmWave5GservicesinamajorU.S.city,focusingonthethrough- massive Machine Type Communication (mMTC) to enhanced
putasperceivedbyapplicationsrunningonuserequipment(UE). Mobile Broadband (eMBB) services1. Exciting new applications
Throughextensiveexperimentsandstatisticalanalysis,weiden- enabledbytheseservicesinclude(Industrial)Internet-of-Things
tifykeyUE-sidefactorsthataffect5Gperformanceandquantify (IoT),autonomousdriving,Augmented/VirtualReality(AR/VR),
towhatextentthe5Gthroughputcanbepredicted.Wethenpro- andultra-HDinteractivevideoservices.
poseLumos5G–acomposablemachinelearning(ML)framework 2019sawthecommercialdeploymentof5GservicesinUSand
thatjudiciouslyconsidersfeaturesandtheircombinations,andap- worldwide,withmajorityusing5GNRmid-bandandlow-band
plystate-of-the-artMLtechniquesformakingcontext-aware5G frequenciesandafewusing5GNRmillimeterwave(mmWave)
throughputpredictions.Wedemonstratethatourframeworkisable high-band frequencies (e.g., Verizon in US). We are particularly
toachieve1.37×to4.84×reductioninpredictionerrorcompared interestedinmmWave5Gperformanceforseveralreasons.First
toexistingmodels.Ourworkcanbeviewedasafeasibilitystudy ofall,theultra-highbandwidth(theoreticallyupto20Gbps)of
forbuildingwhatweenvisageasadynamic5Gthroughputmap mmWave5Goffersexcitingnewopportunitiestosupportavariety
(akintoGoogletrafficmap).Webelievethisapproachprovides ofemergingandfuturebandwidth-intensiveapplicationsexpectedof
opportunitiesandchallengesinbuildingfuture5G-awareapps. the5GeMBBservice.Ontheotherhand,fromtheoreticalanalysis,
simulationstudies,controlledexperimentsandlimitedfieldtesting,
CCSCONCEPTS ithasbeenwidelyknownthattherearemanytechnicalchallenges
facing mmWave radios (see, e.g., [31, 33, 39, 40, 51, 66, 68, 69]
•Networks→Mobilenetworks;Networkmeasurement;Net-
andthereferencestherein),makingdesigningandmanaging5G
workperformanceanalysis;•Generalandreference→Mea-
servicesbasedonmmWaveradioadauntingtask.Forexample,
surement;Estimation;
duetothedirectionalityandlimitedrangeofmmWaveradioand
KEYWORDS its high sensitivity to obstructions (e.g., surrounding buildings,
movingbodies,foliage,etc.),establishingandmaintainingastable
5G, machine learning, deep learning, throughput prediction,
communication link with user equipment (UE) can be difficult,
mmWave,prediction,bandwidthestimation,Lumos5G
especiallywhentheUEismovingaround[17].
ACMReferenceFormat: Indeed,ourveryrecentmeasurementstudyofcommercial5G
ArvindNarayanan,EmanRamadan,RishabhMehta,XinyueHu,Qingxu servicesinUS[47]hasshownboththeexcitingnewopportunities
Liu,RostandA.K.Fezeu,UdhayaKumarDayalan,SaurabhVerma,PeiqiJi, offeredbymmWave5Gbutalsothedifficultchallengesinvolved:
TaoLi,FengQian,Zhi-LiZhang.2020.Lumos5G:MappingandPredicting (i)commercialmmWave5Gservicescanofferultra-highbandwidth
CommercialmmWave5GThroughput.InACMInternetMeasurementCon-
(upto2Gbps)whichmakesitpossibletosupportnewclassesof
ference(IMC’20),October27–29,2020,VirtualEvent,USA.ACM,NewYork,
applicationswithhighbandwidthrequirements;(ii)thechallenges
NY,USA,18pages.https://doi.org/10.1145/3419394.3423629
lieinthat5Gperformancecanfluctuatewildlyovertimeandfrom
*Correspondingauthors:{arvind,eman,zhzhang@cs.umn.edu},fengqian@umn.edu. onelocationtoanother,reachingashighas2Gbpsbutsometimes
quickly dropping below that of 4G or to nearly zero (5G “dead
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor zones”).Forillustrativepurposes,Figs.1and2summarizethese
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation
onthefirstpage.CopyrightsforcomponentsofthisworkownedbyothersthanACM 1Intermsofbandwidth,5Glow-bandofferssimilarcapacityas4G(lessthan100Mbps).
mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish, 5Gmid-bandoffersbandwidthusuallyintherangeof100–400Mbpssimilarto
topostonserversortoredistributetolists,requirespriorspecificpermissionand/ora thatofadvanced4GLTE.Bothlow-bandandmid-bandradiosignalsarelargely
fee.Requestpermissionsfrompermissions@acm.org. omni-directional,thusprovidinglargecoverageareaswithoutrequiringline-of-sight
IMC’20,October27–29,2020,VirtualEvent,USA (LoS)touserequipment(UE).However,withflexiblewaveformandnumerology,they
©2020AssociationforComputingMachinery. areexpectedtobemorereliableandcapableofproviding1mslatencytosupportURLLC
ACMISBN978-1-4503-8138-3/20/10...$15.00 andmMTCservices.URLLCandmMTC,togetherwitheMBBsupportedprimarilyby
https://doi.org/10.1145/3419394.3423629 5GNRhigh-band,formthethreenew5GservicesasenvisionedbytheITU-R.
176

IMC’20,October27–29,2020,VirtualEvent,USA ArvindNarayanan,EmanRamadan,RishabhMehta,XinyueHu,etal.
Figure1:WalkinginaLoop. Figure2:DrivinginaLoop.
observations.Giventhesefindings,itisthereforenaturaltoask: containsthroughputsamplescapturedbywalkingover331kmand
whatnewtoolsandmechanismsareneededtohelpemergingeMBB drivingover132km(§3.2),partofwhichhavebeenmadepublicly
applicationstoeffectivelyleveragetheultra-highbandwidthoffered availableonourwebsite:https://lumos5g.umn.edu.
by5Gwhilemitigatingitschallenges,thusmakingthem5G-aware? • To understand their potential impact on 5G throughput,
Inthispaper,weconductasystematicmeasurementstudyto we identify several UE-side factors and decompose them into
characterizeandmapmmWave5Gthroughputperformance,with quantifiablefactors.In§4,weconductnumerousempiricaland
thegoaltodevelopeffectivetoolsforpredicting5Gthroughput.As statisticalanalysisoverthefactorsindividuallytounderstandtheir
furtherarticulatedin§2,wefocuson5Gthroughputmeasurement impacton5Gthroughputbehavioranditspredictability.Wefind
(asopposedto,e.g.,“low-level”signalstrengthmeasurement)asthis that5Gthroughputperformanceisdrivenbyawidespectrumof
iswhatmatterstoemergingapplicationssuchas4K/8K,360°and factorsandtheirinterplaythataremuchmorecomplexcompared
volumetricvideostreaming,cloudgaming,AR/VR,whichrequire totraditionalcellulartechnologiessuchas3Gand4G.
ultra-high bandwidth. Tools for throughput predictions [20, 26, •Basedonourmeasurementfindings,wedevelopLumos5G–a
44, 45, 54, 58, 63, 70] are essential to these applications, e.g., in holisticandrobustMLframeworkthatpredicts5Gthroughputboth
aidingtheminbandwidthadaptationtomaximizeuserquality-of- qualitatively(viaclassification)andquantitatively(viaregression).
experience(QoE).Thediverseimpactfactorsandtheircomplex Our framework is “composable” in that it judiciously considers
interplayon5Gperformancealsocallfordata-driven,machine differentfeaturegroups(geographiclocation,mobility,tower-based,
learning(ML)toolsforthroughputprediction. radio connection) as well as their combinations. This is to our
Ourwork canbeviewedasa “feasibility”studyforbuilding knowledge the first study taking a look at the predictability of
whatweenvisageasa(dynamic)5Gthroughputmap(akintoa commercial5Gperformanceusingreal-worlddata.
Google traffic map) that not only depicts 5G coverage but also • Using Lumos5G, we conduct extensive evaluations and
feedsvariegatedthroughputperformanceinformationtomobile demonstratethatitachievesaccurateandreliable5Gthroughput
applicationsovertime;furthermore,itcapturesandincorporates prediction, and that using 5G-specific features significantly
key impacting factors specific to a user’s environs and context improvesthepredictionresults(§6.1-§6.2).Poweredbyjudicious
intheformofdownloadableMLmodels.Suchathroughputmap feature and ML model selection, our framework achieves an
augmentedwiththeMLmodelscanthenaida5G-awareapplication overall weighted average F1 score of up to 0.96 (with three
to,e.g.,selecttheinitialbitrateforvideostreaming[27,62,70], predictionclasses),and1.37×to4.84×reductioninthroughput
and predict future throughput for rate adaptation (see §2.2 for prediction error compared to existing approaches designed for
potentialusecases).Werecognizethat5Gdeploymentisstillin 3G/4G (§6.3-§7). Finally, we reveal other interesting research
itsinfancy,themeasurementfindingsandtoolsdevelopedinthis opportunitiesconsequentialtoourwork(§8).
studywillneedtoberevisedandevolvedovertime.Nonethelesswe
2 BACKGROUND&OVERVIEW
believethatthisisalsotheperfecttimetoconsiderthedesignand
developmentoftoolsthatcanbeincorporatedinuser-sidesystems Wefirstprovideaquickbackgroundonthecurrentcommercially
andapps,makingthem5G-aware.Whilewefocusontheuserside, available5Gservicesandtheirmeasurement.Wethenpresentthe
ourfindingsandMLmodelscanalsohelp5Gcarriersinimproving rationaleforourworkandpotentialusecases.
their5Gservices(see§8fordetails).
Key Contributions and Roadmap: In the following we 2.1 5GDeployment&Measurement
summarizethekeycontributionsofourwork,whichalsoserveas
Today’scommercial5Gservicesarealldeployedintheso-called
aroadmaptothetechnicalpartofthepaper.
NSA(non-standalone)mode:namely,5GNRisdeployedwithits
• Due to lack of publicly available tools/APIs for 5G
ownantennas,butsharesthe4Gpacketcoreinfrastructure.As
measurements,wedevelopourown5Gservicemonitoringand
such, 5G “towers” are eitherco-located with orare close to 4G
throughput measurement platform (§3.1). We use our tools to
towers. With NSA, much of the touted 5G benefits come from
conduct extensive, and repeated on-field experiments for 5G
5GNR.5GNRencompassesawidespectrumfromlow-band(<1
throughputdatacollectioninalargeU.S.city.Whileensuringdata
GHz), mid-band (1-6 GHz) to high-band (>24 GHz) frequencies.
qualityremainshigh,wecarefullydesignsystematicmeasurement
Low-bandandmid-band5Gformthebasisofmostoftoday’sinitial
methodologiestomeasure5Gthroughputundervarioussettings
5Gservicedeploymentintheworld–theyofferonlymoderately
(indoor/outdoor,mobilityscenarios,etc.).Aftercleaning,ourdataset
higherbandwidththanexisting4GLTEoradvancedLTEservices.
177

Lumos5G:MappingandPredictingCommercialmmWave5GThroughput IMC’20,October27–29,2020,VirtualEvent,USA
Incontrast,high-band5G–whichcoversthemmWavefrequency Several studies have shown that even in the case of 3G/4G
bands – offers bandwidth as high as 20 Gbps theoretically, but networks, location alone cannot provide a good prediction of
considerablylowerbandwidthinpractice2. signalstrengthorthroughput.Asconfirmedbyourmeasurement
Thecommercialdeploymentof5Gservicesoffersanewoppor- results, there are far more factors affecting 5G performance.
tunitytoconduct“inthefield"measurementof5Gperformance, Wethereforefocuson5Gthroughputmeasurementdirectlyby
especially mmWave 5G that is known to be highly sensitive to building a measurement platform (an app) that can run on 5G
variousradiosignalqualityimpairmentsandenvironmentalfac- mobile handsets (§3.1). The ability of predicting 5G throughput
tors[17,31,33,39,40,66].Ourrecentwork[47]conductedamea- with a reasonable accuracy can help improve transport-layer
surementstudyofcommercial5Gdeployment,includingmid-band mechanisms[22–24,42]neededtoaddressnewchallengesposed
and mmWave 5G services offered by several carriers in the US. by5G.Itcanalsobenefitmanyapplications,e.g.,adaptivevideo
It shows that commercial mmWave 5G services can deliver up bitratestreaming[27,58,62,70].Forexample,itisshownin[58]
to2GbpsbandwidthperUE,buttheirperformanceissubjectto that with a prediction error ≤ 20%, the QoE of adaptive video
variousenvironmentalandotherfactors. streamingcanbeimprovedclosetooptimal(>85)%.Webelievethat
Buildingupon[47]whichprovidesabroad,generalmeasure- suchanabilityismorecriticaltoemerging5GeMBBapplications
mentstudyof5Gperformancefromvariousaspects,thispaper thatrequireultra-highbandwidth.Conventionalmethodsadopted
focusesonunderstandingthekeyuser-sidefactors(i.e.,features) by applications for throughput estimation and prediction have
affectingmmWave5Gthroughputperformance,andhowtobuild been mostly “in situ” in that applications either use past data
goodmachinelearningmodelsthatcanutilizesuchuser-sidefea- transmissionsorgenerateafewprobestoestimateandpredict
turestopredict5Gthroughputperformance.Hereafterwhennot (immediate)futurethroughput[45].Someoftheseapproachesalso
explicitlystated,5GreferstommWave5G.Tohelpillustrateand heavilyrelyonhavingaccesstoPHY-layerinformation[20,43,54].
motivatetheproblemswestudyinthispaper,Figs.1&2showtwo However, to address modern-day security concerns, mobile OS
sample5Gthroughputtracesundertwomobilityscenariosfrom developers have increasingly started to restrict third-party app
ourmeasurementstudy.Weseethat5Gthroughputperformance developers from having access to OS-level APIs which earlier
canvarywidelyandwildlyfromashighas2Gbpstoaslowasclose provided easy access to low-level PHY-layer information [54].
to0;usermobilityandobstructionsalsocreatefrequenthandoffs Goingforward,webelievethatconventionalmethodswouldbe
(see§4forfurtherdiscussion).Suchhighvariabilityposesmany inadequatefor5Gapplicationstoestimatethroughputperformance.
challengesfornewapplicationsthatrelyontheultra-highband- Moreover, inorder topredict5G throughputwitha reasonable
widthofferedbymmWave5GeMBBservices.Ourstudytherefore accuracy,itisalsoimportanttocaptureandaccountforvarious
focusesoncharacterizingandmapping5Gthroughputperformance, environment,contextual,andotherexogenousfactors.Weshow
withthegoalofidentifyingthekey(especially,UE-side)impact thatthecarrier’s5Gcoveragemap(seeFig.3a)aswellasthe5G
factorsandquantifyingthe(short-&long-term)predictabilityof coverage mapped by us (see Fig. 3b that shows the percentage
5Gthroughputperformanceviarepeatedexperiments. of5Gconnectivity)areinsufficienttounderstand5Gthroughput.
Wethusadvocatebuilding5Gthroughputmaps(e.g.,seeFig.3c)
2.2 CaseforMapping&PredictingmmWave
basedonuser-led(collaborative)5Gthroughputmeasurementdata.
5GThroughput
Such throughput maps not only show 5G coverage and depict
Astherationaleforourwork,weanswertwokeyquestions:(i)why 5Gthroughputvariabilityovertimeandacrossdifferentlocales,
5Gthroughputmappingisimportant;and(ii)whytakeanML- but more importantly, they also incorporate (mmWave-specific)
basedapproachfor5Gthroughputprediction. environmentalandcontextualfactors(intheformofMLmodels)
5G coverage provided # of samples with active 5G Average throughput tohelpappsbetterutilize5G’shigh-throughput.
by carrier connectivity over total samples • Why ML Models for 5G Throughput Prediction? For a
5G service area 0 % 100 % <60Mbps 1000+Mbps longtime,MLhasbeenusedforthroughputpredictionnotonly
inwirelessnetworksbutalsoinwirednetworks[32,46].However,
duetothevagaryofwirelesssignalsandtherecentadvancements
inML,data-drivenmachinelearning(ML)modelshavebecome
popularfor3G/4Gcellularnetworkmanagement(see§7).Giventhe
diversearrayofimpactfactorsandtheircomplexinterplay,theneed
forMLmodelsfor5Gnetworksismoreacute.However,insteadof
(a)ByCarrier[13]. (b)5GCoverageMap. (c)5GThroughputMap. blindlyapplyingmachinelearningtotheproblemof5Gthroughput
Figure3:5GPerformance. prediction,weseektoanswerafewbasicquestions:(i)IsmmWave
5G throughput predictable, and to what extent? (ii) What key
•Why5GThroughputMapping?Signalstrength,spectrum
UE-sidefactors(orfeatures)mostaffect5Gthroughput?(iii)In
and channel state measurements have been widely studied in
ordertocapturethesekeyfactors,whattypesofMLmodelsarebest
wireless and cellular networks, many from the perspective of
suitedfor5Gthroughputprediction?Inparticular,canwedevelop
a cellular provider, e.g., for 3G/4G cellular channel scheduling.
MLmodelsthatareexplainable?Tothisend,wecarefullydesign
2High-band(especiallymmWave)5Gradiosignalsareknowntobehighlydirectional, ourmeasurementsundervarioussettings(e.g.,selectingindoorand
requireline-of-sight(LoS),andhavelimitedranges.Particularly,theyaresensitive
outdoorareas,consideringbothstationaryandmobilityscenarios
totheenvironmentandcanbeblockedbyconcretestructures,tintedglass,human
bodies,andothermovingobjects[47,66]. of various moving speeds), and conduct extensive and repeated
178

IMC’20,October27–29,2020,VirtualEvent,USA ArvindNarayanan,EmanRamadan,RishabhMehta,XinyueHu,etal.
experimentsfordatacollection,throughputcharacterizationand 3.1 OurMeasurementPlatform
factoranalysis(see§4).Basedontheseresults,wemotivateand MeasurementApp.Atthetimeofthisstudy,thestate-of-the-art
presentourproposedMLmodelsin§5. AndroidOS(version10)claimstoprovideaccessto5G-NRrelated
APIs[2–4].However,noneofthe5Gcarriersprovideanymean-
2.3 PotentialUseCases
ingfulresponsestotheseAPIs.Withnomaturetoolsavailableto
Weconcludethissectionbyillustratingsomepotentialusecases collect5Ginformationandabsenceof5Gdatasets,wehavedevel-
of Lumos5G framework when in action, and its proposed 5G opedourownsuiteofAndroidappandtoolsfor5Gperformance
throughputmapsandMLmodels. monitoringandthroughputmeasurement.Weparseraw-string
representationofAndroid’sServiceState&SignalStrengthob-
jectstogetinformationaboutphonestate,servicestate,andsignal
1000+ Mbps
strength.Ourapplogsinformationsampledeverysecondsuchas
theUE’sgeolocation,orientation(i.e.,compassdirection),tower(or
panel)ID,movingspeed,activeradiotype(e.g.,5G-NRorLTE),etc.
N🧭
Panel Direction
Figure4:Lumos5GinAction.
<60 Mbps θ
θ
θ
5
d
m
p
G
:
:
:
P
P
U
U
an
a
E
E
θ e
n
l d
e
m
p
l
o
θ
o
d
s
p
b
i
i
θ
t
r
il
i
m
e
i
o
t
c
n
y
t
a
i
a
o
l
n
n
a
g
n
l
g
e
U
l
s
e
w
e r
w
. r
M
.
.
r
t
o
.
.
t
v
θ
.
in
d
θ
g
P
d
D
ix
i
e
r
l
e
iz
c
e
ti
d
o n
Location
Coordinates
ConsiderfourusersAlice,Bob,Charlie,andDaisyareallstream- Figure5:{Panel,Positional,Moving}Angles.
inghigh-resolutionvideos(seeFig.4).Aliceistakingarideinside Withtheknowledgeofthe5Gpanel4locationandorientation
ataxi,whileBobiswalkingonthepedestrianstreetinthesame (identifiedbymanuallysurveyingthearea),wecomputeadditional
directionasAlice’sride.Charlieiswalkingontheotherside,while fieldsoftheUEwithrespecttoeachpaneltostudytheirimpact
Daisyiswalkinginsidethepark.WithLumos5G,theirUEsauto- on5Gthroughput.AsdepictedinFig.5,theUE-Paneldistance
maticallydownloads5GthroughputmapswithMLmodelsbased isshownwiththeredlinebetweenpixelizedlocationofUEand
ontheirgeographiclocations;thevideostreamingappinteracts towerpanel.Thegreenarrowindicatesthepaneldirectionwith
(viaappropriateAPIs)withtheMLmodelswhichtakeintoaccount respectto(w.r.t.)theNorthpole.UE-Panelpositionalangle𝜃 𝑝 is
thecontextandvariousfactorssuchaslocation,movingspeed&di- theangleoftheUEw.r.t.panelirrespectiveofmovingdirection.
rection,typeofavailableservice3topredict5Gthroughput(shown UE-Panelmobilityangle𝜃 𝑚istheanglebetweenthelinenormalto
asaconicalheatmap).Accordingly,theappcanmakeintelligent thefront-faceofthepanelandtheUE’strajectory.Table1listsall
decisions(e.g.,bitrateadaptation)toimproveuserQoE. thefieldsthatourappcollects.Theywillbeusedinoursubsequent
Forinstance,usermobilityhasasignificantimpacton5Gper- measurementanalysisandfeaturesforML.
formance.Hence,Alicewhoistakingataxirideatarelativelyhigh ObtainingThroughputGroundTruth.Togetthethroughput
speedshouldexpecttoexperiencedegradedperformancecompared groundtruth,ourtoolmeasuresthebulktransferthroughputover
toBobwhoiswalkingalongthesametrajectory.Similarly,when 5G.Wecross-compileiPerf 3.7[8]andintegrateitintoourapp
Charlieisabouttowalkacrossahandoffpatch(aslearnedbythe suchthataUEisperiodicallydownloadingcontentfromabackend
model),therewillbeamomentarydegradationinperformance server.Thisenablesustonotonlycollectvitalstatisticsaboutthe
whichtheappcananticipateandpreparefor.Daisywhoiswalking networkstate,butalsoevaluate5Gthroughputperformanceunder
intheparkdoesnothaveaclearlineofsighttothe5Gtower; differentsettingssuchasmobilitymode,geolocation,etc.Toensure
howeverduetotheconcretehigh-risebuildingsaroundher,signals wefullysaturatetheavailablebandwidthprovidedbythe5Gcarrier,
mayreflectback,providingdegraded5Gperformance.Thus,5G weestablish8parallelTCPconnectionswiththebackendserver,
carrierscanincorporateLumos5GanditsMLmodelstosupply astheUEwasnotabletofullyutilize5G’sdownlinkbandwidth
appswiththroughputpredictionbytakingintoaccountthekey using1TCPconnection[47].
factorsbasedontheusercontext,andaidtheapps(alaservice PreventInternetbeingBottleneck.Withtheultra-highband-
orcontentproviders)inmakingintelligentdecisions.UEcanalso widthofferedbymmWave5G,thebottleneckofanend-to-endpath
providefeedbackinformationtohelpcarriersinmakingresource betweenaUEandthebackendserver(i.e.,thecontentserver)may
allocationandschedulingdecisionsbasedonapplicationneeds. shiftfromtheradioaccessnetworkorcarrier’sinfrastructureto
theInternet.Toavoidthisandensuremoreaccurate5Gthroughput
3 DATACOLLECTION&QUALITY
measurementresults,wehaveconductedextensivemeasurements
We focus on 5G throughput measurement with the goal of
usingavarietyofservershostedbymultiplepublicandprivate
identifyingandcharacterizingthekeyUE-sidefactorsimpacting5G
cloudprovidersatdiversegeographicallocations.Weobservethat
throughputperformance.Inthefollowing,welistthechallengesin
factorssuchasserverlocationandcloudserviceprovideraffect5G
collecting5Gthroughputdata,presentourmeasurementplatform,
performance.Takingcuesfromourpriorwork[47],weconduct
keyconsiderationswemaketoensuredataqualityremainshigh, severalexperiments(atleast5×60-secondruns)usingserversfrom
andsummarizethedetailsofourdatasets.
4WeobservedeachmmWave5Gtowerdeploymenthadonetothree5Gpanelsor
3e.g.,mmWave,mid-bandorlow-band5G,LTE,LTE-AorLTE-CA transceivers(ofteninstalledonpoles)facingdifferentdirections.
179

Lumos5G:MappingandPredictingCommercialmmWave5GThroughput IMC’20,October27–29,2020,VirtualEvent,USA
| Table1:FieldsRecordedbyOur5GMonitoringTool |     |     |     |     |     | 3.2 Datasets |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
(*FieldsWithanAccuracy%ProvidedbyAndroid).
Spanningacrossadurationof6months,weuseour5Gmonitoring
Field Description tool (see Table 1 for details of the recorded fields) to measure
Rawvalues/objectsobtainedfromAndroidAPIs Verizon’s5GserviceinMinneapolis(alargemetropolitancityin
| timestamp |     | logsthedateandtimeeverysec |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
latitude*, UE’sfine-grainedgeographiccoordinates(i.e.,geolocation)&its theU.S.)using4×SamsungGalaxyS105Gsmartphones.
| longitude* |     | estimatedaccuracyreportedbyAndroidAPI |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Table2:DetailsAboutAreas.
| detected     |     | reportsifuseriswalking,still,driving,etc.usingGoogle’sActivity |     |     |     |             |              |     |                 |                        |      |     |
| ------------ | --- | -------------------------------------------------------------- | --- | --- | --- | ----------- | ------------ | --- | --------------- | ---------------------- | ---- | --- |
| Activity*    |     | RecognitionAPI                                                 |     |     |     | Area        | Intersection |     | Airport         |                        | Loop |     |
| movingspeed* |     | reportsUE’smovingspeedusingAndroidAPI                          |     |     |     |             |              |     |                 |                        |      |     |
|              |     |                                                                |     |     |     |             | Outdoor4-    |     | Indoormall-area | w/railroadcrossings,   |      |     |
| compass      |     | ThehorizontaldirectionoftraveloftheUEw.r.t.NorthPole(also      |     |     |     |             |              |     |                 |                        |      |     |
|              |     |                                                                |     |     |     | Description | waytraffic   |     | w/shopping      | trafficsignals,andopen |      |     |
| direction*   |     | referredtoasazimuthbearing)&itsaccuracy                        |     |     |     |             |              |     |                 |                        |      |     |
|              |     |                                                                |     |     |     |             | intersection |     | booths          | parkrestaurants        |      |     |
Valuesobtainedafterpost-processingorfromothersources
|     |     | DownlinkthroughputreportedbyiPerf |     | 3.7 |     | Trajectories |     | 12  |     | 2   | 2   |     |
| --- | --- | --------------------------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
throughput
radiotype UEconnectedto5Gor4G,identifiedbyparsingitfromraw Traj.Length 232to274m 324to369m 1300m
ServiceStateobject
cellID mCid(toweridentity)theUEisconnectedto,parsedfromraw We judiciously select three urban areas with mmWave 5G
ServiceStateobject coverage(seeTable2forsummary).(1)Intersection:anoutdoor
| signalstrength |     | SignalstrengthofLTE(rsrp,rsrq,rssi)&5G(ssrsrp,ssrsrq,ssrssi) |     |     |     |          |         |              |     |           |                |     |
| -------------- | --- | ------------------------------------------------------------ | --- | --- | --- | -------- | ------- | ------------ | --- | --------- | -------------- | --- |
|                |     |                                                              |     |     |     | four-way | traffic | intersection | at  | the heart | of Minneapolis |     |
respectively,parsedfromrawSignalStrengthobject
|                   |     |                                           |     |     |     | downtown    | region   | consisting   |     | of 3 dual-panel |           | faced 5G |
| ----------------- | --- | ----------------------------------------- | --- | --- | --- | ----------- | -------- | ------------ | --- | --------------- | --------- | -------- |
| horizontalhandoff |     | UEswitchesfromone5Gpanel(cellID)toanother |     |     |     |             |          |              |     |                 |           |          |
|                   |     |                                           |     |     |     | towers, (2) | Airport: | representing |     | an indoor       | mall-area | inside   |
| verticalhandoff   |     | UEswitchesbetweenradiotype(e.g.,4Gto5G)   |     |     |     |             |          |              |     |                 |           |          |
UE-PanelDist. distancebetweentheUEandpanelitisconnectedto Minneapolis-St.Paul(MSP)InternationalAirportwithtwohead-on
| Positional |     | anglebetweenUE’spositionrelativetothelinenormaltothe |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
single-panel5Gtowers∼200mapart,and(3)Loop:a1300-meter
| Angle(𝜃𝑝) |     | front-faceof5Gpanel(seeFig.5forillustration) |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
loopnearU.S.BankStadiuminMinneapolisdowntownareathat
| Mobility |     | anglebetweenthelinenormaltothefront-faceof5Gpaneland |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Angle(𝜃𝑚) covers roads, railroad crossings, restaurants, coffee shops, and
UE’strajectory(seeFig.5forillustration)
recreationaloutdoorparks.Theseareasarerepresentativeasthey
multiplecloudserviceproviders(threepublicandoneprivate).We coverindoorandoutdoorenvironmentsinanurbansetting.
thenchooseserversusingthefollowingfilteringcriteria:(1)down-
loadingfromtheseserversyieldsthehighest5Gthroughput(sta- Table3:FullDatasetStatistics.
tistically)comparedtoserversinotherlocationsand/orproviders;
|     |     |     |     |     |     | DataPoints |     | 563,840(per-sec.throughputw/feature)samples |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ------------------------------------------- | --- | --- | --- | --- |
and(2)downloadingfromtheseserversusingotherwired(non-
|     |     |     |     |     |     | MobilityModes |     | Walking(331km),Driving(132km),Stationary |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ---------------------------------------- | --- | --- | --- | --- |
mobile)hostsyieldsatleast3Gbpsthroughput,wellbeyondthe Data 38,632GBsofdatadownloadedover5G
peak5Gthroughput.Finally,toconfirmtheaccuracyofourmea- Duration 6months
surements,wealsousethecommercialOoklaSpeedtest[11]toolto
Foreacharea,weselectseveraltrajectoriesandperformmultiple
testthethroughputandensurethattheirresultsmatchours,with
walkingpassespertrajectory(atleast30×).Forinstance,the4-way
adifferencelessthan5%.
intersectionhad12differentwalkingtrajectories.Inadditionto
EnsuringHighDataQuality.GPScoordinates,compassdi- walking,wealsoconductdrivingtestsattheLoopareawithspeeds
| rection, and | moving | speed reported | by Android |     | APIs are often |                 |     |         |       |                  |        |        |
| ------------ | ------ | -------------- | ---------- | --- | -------------- | --------------- | --- | ------- | ----- | ---------------- | ------ | ------ |
|              |        |                |            |     |                | ranging between |     | 0 to 45 | kmph. | Our full dataset | covers | 331 km |
inaccurateenoughespeciallywhenfinegranularitymatters.Hence,
walkingand132kmdriving(seeTable3forotherstatistics).
| direct usage | of  | these values | can be misleading. |     | To ensure data |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | ------------------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
EthicalConsideration.Thisstudywascarriedoutbypaidand
qualityremainshigh,we:(1)repeatedlyconductmultiplemeasure-
|     |     |     |     |     |     | volunteer | graduate | and undergraduate |     | students. | No  | personally |
| --- | --- | --- | --- | --- | --- | --------- | -------- | ----------------- | --- | --------- | --- | ---------- |
mentspertrajectoryondifferentdatesandtimesofdaytoensure
identifiableinformation(PII)wascollectedorused,norwereany
thecollecteddataisstatisticallyrepresentative(see§3.2),(2)dis-
humansubjectsinvolved.Ourstudycomplieswiththecustomer
carddatawheretheaverageGPSerror(reportedbytheAndroid
agreementsofthewirelesscarrier.
LocationAPI)isgreaterthan5metersalongthetrajectory,(3)add
a“bufferperiod”atthebeginningofeachwalk/drivetestwaiting
4 5GTHROUGHPUTMEASUREMENT&
| for the UEto | perform | GPS/compass | calibration, |     | and (4) reduce |     |     |     |     |     |     |     |
| ------------ | ------- | ----------- | ------------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
IMPACTFACTORANALYSIS
thelocalizationnoisebydiscretizingrawGPScoordinatestothe
Usingourcollecteddataset,weinvestigatehowawiderangeof
nearestknown(pre-calculated)pixelizedcoordinates.Thepixel
coordinatesaredefinedbyGoogleMapsJavascriptAPI[9]foreach factors affect 5G throughput. This provides insight for feature
zoomlevelaGooglemapisviewedat.Thishelpscreateagridover selectionofourML-basedframeworkin§5.Asummaryofour
thegeographicmap.Forinstance,atzoomlevel17,eachpixel’s findingsisshowninTable4.
spatialresolutionrangesbetween0.99to1.19meters(∼1meterfor
4.1 ImpactofGeolocation
thispaper)[6,12].Inourstudy,weuse17asthezoomlevelasthis
resolutionprovidesanicebalancewithoutbeingoverlypreciseas In3G/4Gnetworks,geographiclocationisthedominantfactorfor
GPScoordinatesarebutatthesametimerepresentsageographic indicatingthroughputperformance[20,25,26,53]ortheircoverage.
locationwithareasonablespatialresolution.Pixelizedcoordinates However,asshownearlier,ourinitialexperimentson5Gnetworks
alsohelpreducethesparsenessthatexistsinhighresolutionGPS- indicatethatthethroughputperformancewildlyfluctuateseven
basedcoordinates.Intherestofthepaper,geolocationcoordinates forareasknowntohave5Gservice.Next,westudytheimpact
refertopixelized(X,Y)coordinatesatzoomlevel17. ofgeolocation(i.e.,pixelizedlatitude,longitudeinformation,see
180

IMC’20,October27–29,2020,VirtualEvent,USA ArvindNarayanan,EmanRamadan,RishabhMehta,XinyueHu,etal.
Table4:SummaryofFactorsAffecting5GThroughputandItsPredictabilityfortheIndoor(Airport)Area
(SeeAppendixA.1forMoreDetailsandtheResultsfortheOtherAreas).
| Results⇒        |                               | StatisticalAnalysis |               | SimplePred.Models |           |                 |
| --------------- | ----------------------------- | ------------------- | ------------- | ----------------- | --------- | --------------- |
|                 | CV                            | Norm.Test           | Sp.Coeff.     | KNN               | RF[20,54] | KeyObservations |
| ⇓UE-SideFactors | ±std.dev.)(p-val.>0.001)(mean |                     | ±std.dev.)MAE |                   |           |                 |
|                 | (mean                         |                     |               | RMSE MAE          | RMSE      |                 |
Geolocationaloneisinsufficienttocharacterize&
| (1)Geolocation | 57.60% | ±22.24 51.56% | 0.021±0.19 | 240 326 | 228 313 |     |
| -------------- | ------ | ------------- | ---------- | ------- | ------- | --- |
predict5Gthroughput,butitstillremainsakeyfactor.
(2)Mobility+(1)
| ⊢UE-PanelDistance |     |     |     |     | Alongwithgeolocation,accountingfor |     |
| ----------------- | --- | --- | --- | --- | ---------------------------------- | --- |
⊢UE-PanelPositionalAngle 40.24% ±20.94 78.05% 0.68 ±0.14 167 247 135 201 mobility-relatedfactorsdecreasesvariation
⊢UE-PanelMobilityAngle in5Gthroughputandimprovesitspredictability.
⊢MovingSpeed
Throughput < 60 Mbps 1000+ Mbps Table 5: Statistical Analysis to Show the Percentage of
5G Panel Location & Orientation GeolocationsWhoseThroughputSignificantlyDiffersFrom
EachOther(p-val<0.1).
| (a) Indoor | NorthPanel |     |     |                    |        |                                   |
| ---------- | ---------- | --- | --- | ------------------ | ------ | --------------------------------- |
| Airport    |            |     |     |                    | Indoor | Outdoor KeyObservation            |
|            |            |     |     | Pairwiset-test     | 70.86% | 69.66% Geolocationstillmattersfor |
|            |            |     |     | PairwiseLevenetest | 64.26% | 61.06% 5Gthroughputprediction.    |
Thep-valueresults(seeFig.7a)showthatconsideringasignifi-
cancelevelof0.1,onaverage,themeanthroughputmeasurements
of70.86%ofgeolocationpairsforindoorareasignificantlydiffer
fromeachother.Thesenumbersimplythatgeolocationisoneof
|            |     | 4-way Traffic  |     | thekeyfactorstocapturethroughputdifferences.Similarresults |     |     |
| ---------- | --- | -------------- | --- | ---------------------------------------------------------- | --- | --- |
| SouthPanel |     | (b) Outdoor    |     |                                                            |     |     |
|            |     | Intersection   |     | forOutdoor(4-wayintersection)areincludedinTable5.          |     |     |
Figure6:5GThroughputMaps. Next,westudythethroughputvariabilityatthesamegeoloca-
(a)Indoor(Airport)v/s(b)Outdoor(Intersection) tion.ThenormalitytestresultsinTable4showthatthroughput
measurementsofroughly48%ofgeolocations(i.e.,almosthalfthe
Table1fordetails)on5Gthroughput.Weexemplifyusingdata
|     |     |     |     | area)attheairportdonot | follownormaldistribution.Toreduce |     |
| --- | --- | --- | --- | ---------------------- | --------------------------------- | --- |
fromtheAirportandIntersectionareas. thefalsepositivesindetectingnormaldistributions,weusetwo
Fig.6showsthe5Gthroughputmapvisualizedasa(scatter-plot) typesofnormalitytests:(1)D’Agostino-Pearsontest[28,29],and
heatmap,whereeachpointrepresentsagridof2𝑚×2𝑚area.For
(2)Anderson-Darlingtest[21].Weconsiderthemeasurementsas-
eachgrid,wecalculatethemeanofallthroughputmeasurements
sociatedwithageolocationasnormaliftheypassanyofthetwo
color-codedtorepresentdifferentthroughputlevels:darkredfor
types.Wealsocalculatethemeanandcoefficientofvariation(CV)
below60Mbpsandlimegreenforabove1Gbps.5Gpanellocations ofthroughputsamplesateachgeolocation.Wefindthatapprox-
(pinkarrow)arealsomarkedindicatingthedirectionofcoverage. imately53%ofgeolocationshaveCVvalues ≥ 50%(seeCDFin
We make the following observations: (1) in certain patches 5G Fig.7b),(theplotsfortheothertestsareinAppendixA.1.1).This
throughputisconsistentlyhigh;(2)inotherpatches5Gthroughput
confirmsourobservationthat5Gthroughputvariessignificantly
isconsistentlypoor,e.g.,duetofrequenthorizontaland/orvertical
evenatthesamegeolocation.Indeed,whenweattempttobuild
handoffscausedbyobstructionsinandaroundtheenvironment; MLmodelsusinggeolocationastheonlyfeature,wefindthatthe
(3)finally,therearepatcheswherethethroughputisuncertain. models(weuseKNNandRandomForest,seeTable4)yieldpoorac-
curacy–anaverageMAEandRMSEof∼234Mbpsand∼320Mbps,
| 1.00 |     | 1.00 |     |     |     |     |
| ---- | --- | ---- | --- | --- | --- | --- |
respectively.Theresultsindicatethatgeolocationaloneisinsuf-
| 0.75   |     | 0.75 |        | ficienttocharacterizeorpredict5Gthroughput. |     |     |
| ------ | --- | ---- | ------ | ------------------------------------------- | --- | --- |
| FDC    |     | FDC  |        |                                             |     |     |
| 0.50   |     | 0.50 |        | 4.2 ImpactofMobilityDirection               |     |     |
| Indoor |     |      | Indoor |                                             |     |     |
0.25 0.25 Besidesgeolocation,wenowinvestigatehowmobilitydirection
| Outdoor |     |     | Outdoor |     |     |     |
| ------- | --- | --- | ------- | --- | --- | --- |
affects5Gthroughput.Weselectmobilitydirectionasafactorsince
| 0.00 |     | 0.00 |     |     |     |     |
| ---- | --- | ---- | --- | --- | --- | --- |
unlikeomnidirectionalsignalsin3G/4G,5GmmWavesignalsare
| 0.00 0.05 | 0.10 0.15 0.20 | 0 25 50 | 75 100 125 |     |     |     |
| --------- | -------------- | ------- | ---------- | --- | --- | --- |
t test(p-val)
− CV(in%) highlydirectional,andsensitivetoobstructionssuchashuman
(a) Similarity of throughput (b) Variability of throughput bodyorstructures[47,55,57,67].Forinstance,walkingawayfrom
samplesbetweengeolocations samples within the same a5GpanelwillnaturallyobstructtheUE’sLoStothe5Gpaneldue
usingpairwiset-test. geolocationusingCV. touser’sbody,thusneedingtoacquireaNLoSreflectivepath.
WeexemplifyourfindingusingtheAirportareadata.Wefil-
Figure7:Measuring5GThroughputSimilarity&Variability
terdatarepresentingtwowalkingtrajectories:NB(north-bound)
Toquantifythethroughputdifferencesacrossdifferentgeoloca- andSB(south-bound).Thedatarepresentsthroughputtracescol-
tions,weperformpairwiset-testandLevenetestofthroughput lectedbywalkingeachofthetwotrajectoriesrepeatedlyforover
measurementsforeverypairofgeolocation(orgrid)attheairport. 30times.Eachofthe∼340-meterlongwalkingsessionscaptured
181

Lumos5G:MappingandPredictingCommercialmmWave5GThroughput IMC’20,October27–29,2020,VirtualEvent,USA
)spbM(tuphguorhT
1600
|     | Location    | 5G Panel |     |      |     |     |     |     |     |     |     |
| --- | ----------- | -------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
|     | Coordinates |          |     | 1200 |     |     |     |     |     |     |     |
800
|     | θm=180° | User Walking  |     |     |     |     |     |     |     |     |     |
| --- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Direction
400
|     | θm=90° | θm=270° |     |     |     |     |     |     |     |     |     |
| --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
|     |     |     |     |     | [0,15) [15,30) [30,45) | [45,60) [60,75) ) | ) ) ) ) | ) ) ) ) | ) ) ) ) | ) ) | ) ) ) 5,360] |
| --- | --- | --- | --- | --- | ---------------------- | ----------------- | ------- | ------- | ------- | --- | ------------ |
Us er  W a l k ing [75,90 90,10 5 05,12 0 0,13 5 5,15 0 0,16 5 5,18 0 0,19 5 5,21 0 0,22 5 5,24 0 0,25 5 5,27 0 0,28 5 5,30 0 0,31 5 5,33 0 0,34 5
D ir ect i o n Line normal to the  2 3 5 6 8 9 1 2 4 5 7 8 0 1 3 4
|     |     |     |     |     |     | [   | [ 1 [1 [1 [1 | [1 [1 [1 [2 | [2 [2 [2 [2 | [2 [3 [3 | [3 [3 |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | ----------- | -------- | ----- |
θm=0° front-face of 5G panel UE-PanelMobilityAngleinDegrees(rangeofθpin◦)
Figure8:ImpactofUE-PanelMobilityAngle𝜃 on5Gthroughput.Seeleftsideforillustrationofdifferentvaluesof𝜃
|     |     |     |     |     |     | 𝑚   |     |     |     |     | 𝑚.  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Throughput < 60 Mbps 1000+ Mbps RecallfromourpreviousanalysisthatwebuildKNNandRF
Handoff
5G Panel Location & Orientation Patch modelsusingonlythegeolocationfeaturetopredictthethroughput,
|     |        |            |     |        |            |     | and got poor | accuracy. | Based on those | models, | by additionally |
| --- | ------ | ---------- | --- | ------ | ---------- | --- | ------------ | --------- | -------------- | ------- | --------------- |
|     | (a) NB | NorthPanel |     | (b) SB | NorthPanel |     |              |           |                |         |                 |
accountingformobilitydirection,weareabletoreduceRMSEby
24%and36%forKNNandRF,respectively.Theresultsindicatethat
|     |     | Direction |     |     | Direction |     |              |                 |                   |         |               |
| --- | --- | --------- | --- | --- | --------- | --- | ------------ | --------------- | ----------------- | ------- | ------------- |
|     |     |           |     |     |           |     | in addition  | to the absolute | geolocation,      | further | considering   |
|     |     |           |     |     |           |     | the movement | direction       | leads to improved |         | 5G throughput |
Walking
|     |     |            |     | Walking  |            |     | prediction.      |            |                  |            |     |
| --- | --- | ---------- | --- | -------- | ---------- | --- | ---------------- | ---------- | ---------------- | ---------- | --- |
|     |     |            |     |          |            |     | )spbM(tuphguorhT | NorthPanel | )spbM(tuphguorhT | SouthPanel |     |
|     |     | SouthPanel |     |          | SouthPanel |     | 1600             |            |                  |            |     |
1600
|     |     |     |     |     |     |     | 1200 |     | 1200 |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- |
Figure9:(a)NBv/s(b)SB:AirportThroughputMaps.
|                                                        |     |     |     |     |     |     | 800 |     | 800 |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                                        |     |     |     |     |     |     | 400 |     | 400 |     |     |
| a∼200-secondthroughputtrace.Fig.9showsboththesetrajec- |     |     |     |     |     |     |     |     | 0   |     |     |
0
toriesaswellasthelocationofthehead-on5Gpanelsoneither [0,25) [25,50) [50,75) [75,100) [0,25) [25,50) [50,75 ) 75,10 0 ) 00,12 5 ) 25,150)
sidesofthemall-area.Wealsoannotatethemapswithpatches [ [ 1 [ 1
|     |     |     |     |     |     |     | UE-PanelDistance(inmeters) |     | UE-PanelDistance(inmeters) |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | -------------------------- | --- | --- |
wherehandoffsusuallyoccur(seecyanrectangularpatches).We
select airport area because both panel locations were equipped Figure11:VaryingImpactofUE-to-PanelDistance.
withsingle-sided5Gpanelunlikedual-panelinstallationsseenin
4.3 ImpactofUE-PanelDistance
outdoorenvironments.Thisensuresthatweareconnectedtoonly
onesideofthepanel,thusallowingustounderstandtheimpactof Inspiredbyourfindingsin§4.2,wenowtakeamoredetailedlook
mobilitydirection.5GthroughputmapsfortrajectoriesNBandSB atthegeometricrelationshipamong5Gpanel,UE,andmoving
areshowninFigs.9aand9b,respectively.Wefindthatalthough direction.Weidentifythreegeometricfactors:(1)theUE-paneldis-
|     |     |     |     |     |     |     | tance,(2)theUE-panelmobilityangle(𝜃 |     |     | 𝑚),and(3)theUE-panel |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | -------------------- | --- |
NBandSBareinoppositedirections(withpartialoverlapintheir
|     |     |     |     |     |     |     | positional | angle (𝜃 𝑝). We | quantify their | impact | on 5G through- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | -------------- | ------ | -------------- |
coveragefootprints),theirheatmapsarehighlydifferent,indicating
thatmobilitydirectionhasasignificantimpacton5Gthroughput putinthissubsection,§4.4,and§4.5,respectively.Duetoitshigh
performance.Similarobservationsweremadeinotherareas. frequency,mmWavesignalsbearhighattenuationastheypropa-
Tofurtherquantifytheabove gate.Therefore,asshowninFig.11a(thenorthpanelatAirport),
observation,weuseSpearman’s thethroughputdegradesfastasthedistanceincreases.However,
1.00
thedetailed,quantitativedistance-throughputrelationshipdiffers
| rank | correlation | coefficient | to  |     |     |     |     |     |     |     |     |
| ---- | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.75
measure the monotonic trend NB+SB fromonelocationtoanotherduetotheenvironmentalimpact.For
FDC
(i.e., a consistent upward or 0.50 NBonly example,Fig.11bforthesouthpanelatAirportshowsthatthe
downward trend) between SBonly throughputfirst(statistically)goesdownandthenrampsupasthe
0.25
distanceincreases.ThisisbecausethereisNLoSbetween50and
throughputtraces.Theaverage
|          |              |     |     | 0.00 |           |           | 100mduetoobstacles(causedduetoopen-spacerestaurantsand |     |     |     |     |
| -------- | ------------ | --- | --- | ---- | --------- | --------- | ------------------------------------------------------ | --- | --- | --- | --- |
| Spearman | coefficients |     | of  |      |           |           |                                                        |     |     |     |     |
|          |              |     |     | 0.00 | 0.25 0.50 | 0.75 1.00 |                                                        |     |     |     |     |
throughputtracesbelongingto informationbooths)inthemall-area.TheUEregainsLoSbeyond
Spearmancoefficient
NB and SB are 0.61 and 0.74, 100m,andtheregainedthroughputoutweighsthepenaltyincurred
respectively.Inotherwords,with Figure10:Impactof bydistanceincrease.
| values | above 0.5, | throughput |     | MobilityTrajectory. |     |     |     |     |     |     |     |
| ------ | ---------- | ---------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
4.4 ImpactofUE-PanelMobilityAngle
tracesinthesamedirectionshowsaconsistenttrendinincrease
ordecreaseofthroughputvaluesalongthetrajectory.However, WedefinetheUE-panelmobilityangle(𝜃 𝑚)astheanglebetween
the average Spearman coefficients between throughput traces thelinenormaltothefront-faceof5GpanelandUE’strajectory.It
belonging to different directions is only 0.021. Fig. 10 further representsUE’smovementwithrespecttothefaceofthe5Gpanel.
showsthedrasticincreaseinSpearman’scoefficientsbygrouping AsillustratedinFig.8,when𝜃 =180°,theUEismovinghead-on
𝑚
tracesaccordingtotheirmobilitydirections.Similarly,29.76%of towards5Gpanel,and0°whenwalkingalongthesamedirection
geolocationshavethroughputsampleswithCVvaluesgreaterthan asthe5Gpanel’sfacingdirection.Thus,ifaUEishand-heldby
50%–adecreaseof23%(seeAppendixA.1.2forextendedresults). awalking-user,𝜃 𝑚 = 0°willmaketheuser’sbodyobstructthe
182

IMC’20,October27–29,2020,VirtualEvent,USA ArvindNarayanan,EmanRamadan,RishabhMehta,XinyueHu,etal.
LoSbetweenUEandthe5Gpanel(thecaseinourexperiments),
|     |     |     |     |     | tuphguorhT 1600 |     | Drivingonly |     |
| --- | --- | --- | --- | --- | --------------- | --- | ----------- | --- |
)spbM(
| causingperformancedegradation.Weindeedobservethishigh-        |     |     |     |     | 1200 |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- |
| leveltrendinallthreeareas.However,again,differentgeolocations |     |     |     |     | 800  |     |     |     |
| exhibitdiscrepancy.Forexample,weidentifyone“outlier”where     |     |     |     |     | 400  |     |     |     |
0
| 𝜃 𝑚 ∈ [30°,75°) | atthesouthpanel(seeFig.18inAppendixA.1.3 |     |     |     |           |                        |                 |                         |
| --------------- | ---------------------------------------- | --- | --- | --- | --------- | ---------------------- | --------------- | ----------------------- |
|                 |                                          |     |     |     | (a) [0,5) | [5,10) [10,15) [15,20) | [20,25) [25,30) | [30,35) [35,40) [40,45) |
fortheanalysisofeachpanelseparately).Despitetheusermoving
MovingSpeed(range)inkmph
awayfromthe5Gpanel,thethroughputappearstobehigh.Thisis
likelybecausethesignalisproperlydeflectedbytheenvironment, tuphguorhT Driving Walking
1600
| mitigatinganysevereperformancedegradationincurredbyNLoS. |     |     |     |     | )spbM( 1200 |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
800
| 4.5 ImpactofUE-PanelPositionalAngle |     |     |     |     | 400 |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
0
We define the UE-panel positional B (b) [0,1) [1,2) [2,3) [3,4) [4,5) [5,6) [6,7)
angle(𝜃 𝑝)astheanglebetweentheline BR BL MovingSpeed(range)inkmph
θ=180°
| normal to                      | the 5G panel  | and the line  | p        |        |                                                   |     |     |     |
| ------------------------------ | ------------- | ------------- | -------- | ------ | ------------------------------------------------- | --- | --- | --- |
|                                |               |               |          | =300 ° | Figure14:ImpactofMobilitySpeedon5Gthroughput.     |     |     |     |
| connectingtheUEtothepanel.When |               |               | 5G Tower |        |                                                   |     |     |     |
|                                |               |               | R        | θp L   |                                                   |     |     |     |
| 𝜃                              |               |               |          |        | to45kmphwhilewalkingspeedshoveredbetween0to7kmph. |     |     |     |
| 𝑝 is close                     | to 0° (“F” in | Fig. 12), the |          |        |                                                   |     |     |     |
UEisinfrontofthepanel;when𝜃 5° Fig. 14 shows the throughput distributions of different ground
|     |     | 𝑝   | is FR= 5 | FL  |     |     |     |     |
| --- | --- | --- | -------- | --- | --- | --- | --- | --- |
speeds(reportedbyAndroidAPI[16]),whereeachboxrepresents
| around180°(“B”inFig.12),theUEis |     |     | θpF |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
onthebacksideofthepanel,creating 1-secondsamplesmeasuredforagivenspeedrange.Intheupper
Line normal to the
a NLoS situation leading to potential front-face of 5G panel plot (Fig. 14a), we find that mobility under driving mode has a
Figure12:UE-Panel significantimpacton5Gthroughput.Statistically,thethroughput
performancedegradation.Similarly,we
PositionalAngle𝜃 𝑝. decreasesasthedrivingspeedincreases.Underno-mobilitytovery
| can define | positions such | as left (“L”) |     |     |     |     |     |     |
| ---------- | -------------- | ------------- | --- | --- | --- | --- | --- | --- |
lowmovingspeeds(<5kmph)representingtimeswhenthecar
andright(“R”).AgeneraltrendwefindisthattheFpositionexhibits
farbetterperformancecomparedtotheL,R,andBpositions,in isabouttostop/startorstationary(duetoatrafficstopsignor
particularwhentheUE-paneldistanceisshort,asexemplifiedin a red light), the throughput peaks at ∼1.8 Gbps with a median
Fig.13(thesouthpanelatAirport).Thereisasubtledifference throughputof∼557Mbps.Beyond5kmph,5Gperformancetakes
between𝜃 and𝜃 𝑚.AUEwith𝜃 ahugedegradationasthemedian5Gthroughputfallsto4G-like
|     | 𝑝   | 𝑚 =180°neednotnecessitatethat |     |     |     |     |     |     |
| --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
performance,rangingbetween164Mbpsand60Mbps.Atthesame
| itisinfrontofthe5Gpanel.Forinstance,aUEwith𝜃 |     |     |     | 𝑝 = 180° |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | -------- | --- | --- | --- | --- |
positionedattheback(“B”)of5Gpanelcanalsohave𝜃 𝑚 =180°.In time,peakthroughputformovingspeedsbetween5and30kmph
otherwords,asshownearlierinFig.5,𝜃 differsfrom𝜃 asthe areabove850Mbpssuggestingotherfactorsmightstillboostthe
|     |     |     | 𝑝   | 𝑚   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
formerconsiderstheUE’sabsolutepositioninsteadofitsmoving throughputperformance.
direction.Thus,boththeseangles(𝜃 and𝜃 However, this is not the case while walking. To investigate
|     |     |     | 𝑝 𝑚)coupledwiththe |     |               |               |                       |           |
| --- | --- | --- | ------------------ | --- | ------------- | ------------- | --------------------- | --------- |
|     |     |     |                    |     | further, Fig. | 14b considers | the mode of transport | and shows |
UE-paneldistanceisusefulincapturingtheUE’slocationfromthe
5Gpanel’sperspective(moreaboutthesefeaturesin§5). a side-by-side throughput distribution comparison of walking
|     |     |     |     |     | v/s driving with | a finer-grained | speed range | (1 kmph) per box. |
| --- | --- | --- | --- | --- | ---------------- | --------------- | ----------- | ----------------- |
)spbM(tuphguohT
d=[0-25)in m [25-50) [50-75) [75-100) >100 Comparedtodrivingmode,weclearlyfindthatthereislittleto
1600
nosignificantdegradationin5Gthroughputforwalkingasthe
1200
speedincreases.Peakthroughputwhilewalkingisabletoreach
800
| 400 |     |     |     |     | highlevelsofabove1.8Gbpsacrosstheentirerangeofmoving |     |     |     |
| --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- |
0
speed(i.e.,0to7kmph).Atthesametime,wealsoseethemedian
| B   | BL F FL L | B F FL L | B F L B | F L F |     |     |     |     |
| --- | --------- | -------- | ------- | ----- | --- | --- | --- | --- |
throughputwhilewalkingisconsistentlybetter(by148to457Mbps)
Figure13:Impactof{PositionalAngle&Distance}factors
thanthatwhiledriving.Suchpoorperformancewhiledrivingisnot
betweenUEandSouthPanelon5Gthroughput.
surprisingasmmWavesignalsneedtoreachtheUEbypropagating
throughthecar’sbody(e.g.,windshieldsorsidewindows)that
4.6 ImpactofMobilitySpeeds
attenuatesthesignalstrengthcausingthroughputdegradation.
MobilityisamajortechnicalchallengeinmmWave5Gduetothe Thus,thisstudyshowsthat5Gthroughputisalsoaffectedbya
physical layer characteristics of mmWave that make its signals combinationofeffectscausednotonlybygroundmobilityspeeds
highlyfluctuatingthuscausingwildvariationsinperformance[17, butalsothemodeoftransportfurtherhighlightingthecomplex
interplayoffactorsimpacting5Gthroughput.
47].Next,weconductexperimentsinthewildtoinvestigatethe
impactofmobilityspeedson5Gthroughput.Werepeatedlyconduct Summary. Through in-the-field experiments, we reveal that
walkinganddrivingtestsonthe1300mLooparea(atleast30× numerousfactorsimpact5Gthroughput:geolocation,mobilitydi-
times).Forthedrivingtests,wemountedthephoneonthecar’s rection,UE-Panelorientation,UE-Paneldistance,UE’smobility
windshieldwhileforthewalkingtests,wehand-heldthephone speed,etc.–farmoresophisticatedthanthoseimpacting4G/LTE.
Insteadofindependentlyaffectingtheperformance,thesefactors
infrontofus.LocatedintheMinneapolisdowntownregion,this
area covers a number of traffic/pedestrian lights, public transit maycausecomplexinterplaythatisdifficulttomodelanalytically.
railcrossings,restaurantsandpopularjoints,highrisebuildings, Table4summarizesthestatisticalfindingsandthe5Gthroughput
andapublicpark.Drivingspeedsonthelooprangedbetween0 predictionaccuracyusingexistingmodels.Itclearlyshowsthat
183

Lumos5G:MappingandPredictingCommercialmmWave5GThroughput IMC’20,October27–29,2020,VirtualEvent,USA
accountingforUE-sidemobility-relatedfactorsinadditiontoUE’s Table6:FeatureGroupings.
geolocationisabletobettercharacterize5Gthroughput(thuslead- Feature ListofFeatures
ingtobetterpredictionaccuracy)comparedtousinggeolocation Group
alone.Thismotivatesustoseekforalearningbasedapproachfor
5Gthroughputprediction.
5 LUMOS5G:CONTEXT-AWAREMLMODELS
FOR5GTHROUGHPUTPREDICTION
Buildingontheinsightsobtainedin§4,inthissectionwediscuss
the key considerations and criteria we employ for developing
MLmodelsinLumos5Gframeworkfor5Gthroughputprediction.
Inparticular,weintroducetheideaoffeaturegroupstoaccount
for diverse sets of impact factors at the UE-side, and develop
“composable” ML models that employ different sets of features
dependingontheavailabilityofthefeaturesandusagecontext.
5.1 FeatureSelection&Grouping
Asdiscussed,thereareawholegamutofdiversefactorsthatimpact
5Gperformance,manyofthem,e.g.,channelstate,variousradio
impairmentsthatmaybesensedbythe5Gbasestation,arenot
readilyavailabletoapplicationsrunningontheUE.Hencewefocus
onUE-sidefeaturesthatcanbemeasuredandcollected.Wewill
alsotakeadvantageofadditionalfeatures,e.g.,radiotype,signal
strength,handoffinformationfromthePHYlayer,whenavailable.
Weintroducethenotionoffeaturegroupsbyclassifyingfeaturesinto
severalcategories.Thisnotionoffersseveralbenefits.(1)Ithelps
accountforthecollectiveeffectsandinterplayofsimilarfeatures.
(2)Itallowsustoselectavailableandrelevantfeatures,andcompose
featuresetsdependingontheusagecase(e.g.,stationaryv/s.mobile
scenarios).(3)ItenablesustocompareMLmodelswithdifferent
feature combinations to investigate the importance of various
featuregroupsunderdiversesettingsanddevelopexplainableML
modelsfor5Gthroughputprediction.
Table 6 lists four primary feature groups we consider in our
study.Lrepresentsthebasiclocation-basedfeaturegroupwhich
contains(pixelized)geographiclocationcoordinates.Mrepresents
thebasicmobility-basedfeaturegroupwhichincludesmovingspeed
andcompassdirection(i.e.,azimuthangle)thatcanbemeasured
using sensors on the UE. In place of location-based features, T
representsthe(moreadvanced)tower-basedfeaturegroupwhich
containsfeaturessuchasthedistancefromaUEtothe5Gpanel,
positional (𝜃 𝑝) and mobility (𝜃 𝑚) angles to the 5G panel (see
Fig. 5 for illustrations). These features can be collected by the
UE but rely on exogenous information obtained, i.e., via the 5G
towerlocation/directioninformationmeasuredbyusorsupplied
by the carrier. Despite that, ML models trained using them are
likelymoretransferabletootherareaswithsimilargeolocation
characteristics as the features do not depend on the absolute
locationsoftheUEs,i.e.,beinglocation-agnostic.Crepresentsthe
connection-basedfeaturegroupwhichincludes,e.g.,(theimmediate)
pastthroughputvaluesmeasuredbyanapplicationand/orvarious
low-levelPHY-layerfeaturesprovidedbytheUE,whenavailable.
Next, in Table 6, we list four feature group combinations
“composed” of multiple primary feature groups: (i) L+M (the
Location+Mobility model); (ii) T+M (the Tower+Mobility model);
(iii) L+M+C (the Location+Mobility+Connection model); and
(iv)T+M+C(theTower+Mobility+Connectionmodel).Wechoosethese
yramirP
L PixelizedLongitude&Latitudecoordinates
M UEMovingSpeed+UECompassDirection
T UE-PanelDistance+UE-PanelPositionalAngle+
UE-PanelMobilityAngle
C Pastthroughputmeasurements+(PHYfeatures:Radio
Type+LTESignalStrength+5GSignalStrength+
HorizontalHandoff+VerticalHandoff)
snoitanibmoC
L+M (L)+UEMovingSpeed+UECompassDirection
T+M UEMovingSpeed+UE-PanelDistance+
UE-PanelPositionalAngle+UE-PanelMobilityAngle
L+M+C (L+M)+RadioType+LTESignalStrength+5GSignal
Strength+HorizontalHandoff+VerticalHandoff
T+M+C (T+M)+RadioType+LTESignalStrength+5GSignal
Strength+HorizontalHandoff+VerticalHandoff
fourcombinationstocomparetheperformanceofMLmodelsusing
different feature groups under mobility scenarios, and to study
the feature group importance in 5G throughput prediction. We
considerMLmodelswithandwithoutconnection-basedfeatures
fordifferentusecasesasconnection-basedfeaturesrequirea5G
connectiontobeestablishedforcollectingmeasurementdata.ML
modelswithoutconnectionfeaturesarestilluseful,forexample,for
initialbitrateselectioninadaptivevideostreaming.Inadditionto
theabovefourcombinations,otherfeaturegroupcombinationsmay
alsobeformedtosupportotherusagescenarios.Otherprimary
feature groups such as “static features” containing information
abouttheUEdevicemodelandspecificationsarealsoimportant
for5Gthroughputprediction.However,ourstudyislimitedtoonly
onedevicemodel,hencewedonotconsiderthisfeaturegroup.This
isalimitationofourstudyandwediscussmoreaboutthisin§8.
5.2 ProposedMLModels
Before we present our ML models proposed as part of the
Lumos5G framework, we first describe the basic settings. We
formalizethe5Gthroughputpredictioneitherasaclassification
problemorasaregressionproblem.Wealsoconsidertheshort-term
versuslong-termpredictionproblems.Thesesettingsaremotivated
bydifferentusecasesfortheMLmodels.
5GThroughputPredictionasaClassificationProblem.In
manysettings,weareinterestedinknowingthe“level”orrangeof
throughputausermayreceive,e.g.,lowthroughput(e.g.,100Mbps)
or high throughput (e.g., 700 Mbps and above) or somewhere
in between, given her current location and usage context. This
reducesthe5Gthroughputpredictionproblemtoaclassification
problem:givenasetoffeatures/featuregroups,predictthelevelof
5Gthroughputausercanbeexpectedtoreceive(similartothethe
signalbarsonacellphone).Thisinformationcanbeused,e.g.,for
initialbitrateselectionforvariousapplications.Weconsiderthree
throughputclasses:low(below300Mbps),medium(from300Mbps
to700Mbps),andhigh(above700Mbps)5.
5G Throughput Prediction as a Regression Problem. In
manysettings,however,wemayhaveaccessto,e.g.,atrajectoryof
5Theselevelsarechosenpartiallybasedonouranalysisof5Gthroughputvariability.As
shownin§4,5Gthroughputoftenfluctuates±200Mbps,duetovarious“uncontrollable”
randomeffects.OurMLmodelsalsoworkwellwithotherchoicesofthroughputclasses;
theresultsforwhichareomitted.
184

IMC’20,October27–29,2020,VirtualEvent,USA ArvindNarayanan,EmanRamadan,RishabhMehta,XinyueHu,etal.
featurevaluesmeasuredorcalculatedbytheUEasauserismoving Encoder
alongaroute.Givensuchdata,wewanttopredicttheexpected
LSTM LSTM LSTM throughputvalueatthenexttimeslot(e.g.,1second)ornext𝑘time
Class 0 [0, 300 Mbps) slots(e.g.,30seconds).Regression-based5Gthroughputprediction Class 1 [300 Mbps, 700 Mbps)
canaidmanyapplicationsinmakingfine-graineddecisionsinthe Class 2 [700 Mbps, ∞)
durationofanongoingsession,e.g.,topredictandselectthequality y y y
1 2 20
levelsforadaptivevideostreaming.
Short-Termv/s.Long-TermPrediction.Intheexamplescited LSTM LSTM … LSTM
above,throughputpredictionisshort-term,i.e.,inthetimescales
ofseconds;theyutilizecurrent(orrecentpast)measuredfeature Input Sequence, Length = 20 Decoder
values to predict the immediate future throughput. Such short-
termpredictionismostusefulfordynamicapplicationdecision
making;MLinferencemustberelativelylight-weight.Forgeneral
5G throughput mapping, we are also interested in longer-term
predictionproblems(e.g.,inthetimescalesofminutes,hours,or
evendays).Longer-termpredictionwillallowustoemploymore
datasetsanddevotemorecomputationresourcesfortrainingand
inference;whichcanbevaluablefornetworkmanagementand
planningapplications,amongothers.
InLumos5G,weconsidertwoclassesofMLmodels,onebased
onaclassicalmachinelearningmethod–gradientdecisionboosted
trees(GDBT)[30],andanotherbasedonadeeplearningtechnique–
sequence-to-sequence(Seq2Seq)[59]whichisparticularlysuitedfor
time-series/trajectory-basedregressionproblems.Wenowbriefly
describethesetwoclassesofMLmodels.
•GDBTMLModels.GradientboostingisaclassofMLalgo-
rithmsthatproducesastrongpredictionmodelintheformofa
weightedcombinationofweaklearnerswhichoptimizeadiffer-
entiablelossfunctionbygradientdescentinfunctionalspace.It
followsanadditivemulti-stageapproachinwhichweaklearners
areaddedoneatatimeandgradientdescentprocedureisused
tominimizethelosswhenlearnersareadded.Theweaklearners
aretypicallydepth-boundeddecisiontrees.WechooseGDBTfor
severalreasons.First,itislightweight,requiringlittlecomputation
power.Second,itiscomposable,allowingdifferentsetsoffeatures
(featuregroups)tobeeasilyaddedandcombinedasweaklearners.
Third,itcanbeusedforbothclassificationandregression.Fourth,
itisinterpretableasitspredictivepowerhasstrongmathematical
justificationsandprovidesuswiththeabilitytocomputeandana-
lyzethe(global)featureimportance.Lastbutnottheleast,aswillbe
shownin§6.3,itoutperformsotherclassicalmachinelearningmeth-
odssuchasRandomForest(RF)and𝑘-NearestNeighbors(KNN)
whichhavebeenproposedfor3G/4Gsignalstrength/bandwidth
predictionproblemsintheliterature[20,34,54,60].
•Seq2SeqMLModels.Initiallydevisedfornaturallanguage
processingandmachinetranslation,Seq2Seqlearninghasnowbe-
comeubiquitousforsolvingvarioushigh-dimensionaltimeseries
predictionproblems[49,50,61].Unlikethestandardlongshort-
termmemory(LSTM)models[35],Seq2Seqallowsustomodelan
arbitrary lengthofthepredictedoutputsequenceinsteadofan
immediateone-timeprediction,thuscapableofpredictingovera
longerhorizonintothefuture.Formally,let𝑋 𝑡 = {𝑥 1 ,𝑥 2 ,...,𝑥 𝑡}
beasequenceofinputsknownaprioriattime𝑡 whereeach𝑥 𝑡 isa
featurevector.Let𝑌 𝑡 ={𝑦 1 ,𝑦 2 ,...,𝑦 𝑘}beasequenceof𝑘outputs
tobepredicted.Inourcase,𝑌 𝑡 isasequenceoffuturethroughput
valuestobepredictedoverthefuture𝑘timeslots.Thetimeslots
aredefinedbasedonthepredictionproblemathand(e.g.,seconds
]
Length = 20 (Predicted Throughput)
etatS
redocnE
(moving speed, geolocation, Embeddingcompass direction, 5G status, Throughput
Binning signal strength, etc.)
…
…
x 1
] ]
Classifica…tion Output
…
Regression Output
x x 2 20
Figure15:Seq2Seqw/Encoder-DecoderArchitecture.
forshort-timeprediction,orminutes/hoursforlong-termpredic-
tion).InourdesignoftheSeq2SeqMLmodels(seeFig.15forits
illustration),weincorporateanencoder-decoderarchitectureusing
anLSTM-typenetwork.Ourmodelscanworkwithdifferentfeature
groupsrepresentedasasequenceofhigh-dimensionalinputs.
6 PERFORMANCEEVALUATION
Using the proposed Lumos5G framework for 5G throughput
prediction,weevaluatetheperformanceofGDBTandSeq2Seq
models using different feature groups and their combinations.
We also compare our models with several other analytical
and ML models proposed in the literature for 3G/4G signal
strength/throughputprediction.
6.1 EvaluationFramework
Westartbypresentingthemodelsetupsandevaluationmetrics
usedinourevaluationframework.
ModelSetupsforGDBT&Seq2Seq.Weperformgridsearch
fortuningthehyperparametersforbothSeq2SeqandGDBTmodels
usingthroughputtracesrepresentinganewarea,thusnotpartof
thetrainingortestingdata.Althoughthemodelswerefairlyrobust
tomultiplehyperparametervalues,weselectasetthatprovided
bestperformance.ForGDBTmodels,weuseagradientboosting
regressor(andclassifier)with8000estimators,boundedbydepth
ofsize8andwith0.01learningrate.ForSeq2Seqmodels,weuse
atwo-layerLSTMEncoder-Decoderarchitecturewith128hidden
units.WerunSeq2Seqexperimentsfor2000epochs,wherethe
batch size is set to 256. The input and output sequence length
is set to be 20. We keep the hyperparameters fixed throughout
allourexperiments.Toobtainclassificationresults,duringpost-
processing,weadditionallyassociateourpredictedthroughputwith
throughputclass.ForbothGDBTandSeq2Seq,werandomlysplit
ourdatasetsusinga70/30ratiofortrainingandtesting,respectively.
Weconsidermean-squared-error(MSE)asthelossfunction.All
experimentsarerunonasinglemachinewithIntelCorei7-6850K
(12-core)CPUand2×NVIDIATITANVGPUs.Timetotraineach
oftheSeq2SeqandGDBTmodelsvarieddependingonthearea
oritsdatasetsize.Thenumberofdatapointsrepresentingeach
areaaregovernedbythetrajectorylength(seeTable2fordetails).
Seq2Seqtook6to44hoursfortrainingeachmodelwhileGDBT
wascomparativelymuchquickertaking10-30minutes.
EvaluationMetrics.Forregression,weevaluateusingstandard
metrics– MeanAverageError(MAE)andRootMeanSquaredError
(RMSE). For classification, we consider the weighted average F1
scoreasthemainmetricforevaluation.Inaddition,wealsouse
185

Lumos5G:MappingandPredictingCommercialmmWave5GThroughput IMC’20,October27–29,2020,VirtualEvent,USA
Table7:ClassificationResults:ComparisonofModelsUsingWeighted Average F1 Score↑andRecall↑Metrics.
Feature Areas 4-wayIntersection(Outdoor) 1300mLoop(Outdoor) Airport(Indoor) Global
Groups⇓ Models GDBT Seq2Seq GDBT Seq2Seq GDBT Seq2Seq GDBT Seq2Seq
L 0.79 0.60 0.86 0.71 0.58 0.74 0.65 0.56 0.79 0.88 0.83 0.85 0.78 0.73 0.73 0.46
L+M 0.91 0.85 0.94 0.89 0.79 0.88 0.89 0.92 0.91 0.95 0.91 0.94 0.90 0.89 0.93 0.92
T+M 0.91 0.85 0.95 0.93 – – 0.91 0.96 0.93 0.96 0.91 0.89 0.94 0.93
L+M+C 0.92 0.87 0.97 0.95 0.89 0.93 0.96 0.98 0.92 0.96 0.91 0.95 0.92 0.92 0.96 0.95
T+M+C 0.93 0.87 0.96 0.94 – – 0.92 0.97 0.91 0.95 0.92 0.93 0.95 0.95
Metrics. ↑WeightedAverageF1-score ↑Recalloflow-throughputclass[0,300)
Table8:RegressionResults:ComparisonofModelsUsingMean Average Error↓andRoot Mean Square Error↓Metrics.
Feature Areas 4-wayIntersection(Outdoor) 1300mLoop(Outdoor) Airport(Indoor) Global
Groups⇓ Models GDBT Seq2Seq GDBT Seq2Seq GDBT Seq2Seq GDBT Seq2Seq
L 236 347 151 218 313 395 234 327 170 283 133 223 225 314 208 273
L+M 121 188 68 137 220 293 81 147 79 146 67 133 127 186 74 144
T+M 117 181 58 120 – – 76 142 57 126 115 173 52 109
L+M+C 114 177 54 116 130 192 28 65 72 139 71 138 109 166 49 112
T+M+C 107 166 67 131 – – 69 131 70 147 100 154 57 119
Metrics. ↓MeanAbsoluteError(MAE) ↓RootMeanSquareError(RMSE)
2000
recalltoevaluatethelow-throughputclass(i.e.,below300Mbps)
prediction.TherecallisdefinedasTruePositives/(TruePositives+ 1500
FalseNegatives).Therationaleofusingrecallforthelow-throughput
1000
classisthat,misclassifyinglow-throughputashigh-throughput
mayoftentimesincurmoreQoEdegradation(e.g.,avideostall) 500
comparedtomisclassifyinghigh-throughputaslow(e.g.,onlyvideo
0
qualitydegradationwithoutastall).Therefore,inmostcases,we TestingSamples(sortedbygroundtruththroughput)
preferthatthelow-throughputclassgetsahighrecallvalue.
6.2 ResultsandObservations
Table 7 shows the classification results for both GDBT and
Seq2Seqmodelsunderdifferentfeaturegroupings,whileTable8
showtheregressionresults.Datasetscollectedfromthreeareas
understationary+walking(4-wayIntersection&Airport)and
stationary+walking+driving(1300mLoop)mobilityscenariosare
usedfortrainingandtesting.Weadditionallybuildamodelby
combiningdatafromallareaswithknown5Gpanellocationsinto
asingledataset–referredtoasGlobal.InthecaseofGDBT,the
predictionisbasedonlyonthecurrentfeaturevalues,whereasin
thecaseofSeq2Seq,recentfeaturehistoryvalues(i.e.,asequenceof
featurevalues)areusedforprediction.Theclassificationresultsof
eachmodelinTable7containtwovaluesineachcell:theweighted
averageF1-scoreandrecalloflow-throughputclass[0,300)Mbps–as
indicatedatthebottomofthetable.For1300mLoop,noresultsare
reportedforT+MandT+M+C,asweareunabletoreliablyobtainthe
5Gpanellocationinformation.InTable8,weshowtheregression
resultsofGDBTandSeq2Seqmodelsofalltheareas.Additionally,
Fig.16showssampleregressionpredictionplotsforL+M+Cfeature
grouponGlobaldatasetusingGDBTandSeq2Seq,with±200Mbps
errorboundsshaded.
Key Observations. The results in Tables 7 and 8 clearly
demonstrate that both Seq2Seq and GDBT are able to achieve
overall good prediction results especially under feature group
combinationsthataccountforadditionalUE-sidefeaturesbeyond
geolocation. Location-based feature group alone is in general
inadequatetoachievehighpredictionaccuracy,especiallyunder
)spbM(tuphguorhT Groundtruththroughput
(shadedregion: +/-200Mbpserror)
Predictedthroughput
GDBT
2000
1500
1000
500
0
TestingSamples(sortedbygroundtruththroughput)
)spbM(tuphguorhT Groundtruththroughput
(shadedregion:+/-200Mbpserror)
Predictedthroughput
Seq2Seq
Figure16:RegressionplotsforSeq2SeqandGDBTusing
L+M+CfeaturegroupsonGlobaldataset.
high mobility. By combining additional features from mobility
and/orconnection-relatedfeaturegroups,theweightedaverageF1
scoresforbothGDBTandSeq2Seqthroughputclasspredictions
areconsistentlyabove0.89exceptforoneL+MresultforGDBT
at the Loop area. The Seq2Seq model produces slightly better
predictionresultsoverGDBTforpossiblytworeasons:(i)inthe
caseofthroughputclassprediction,Seq2Sequsesasequenceofpast
featurevalues,whichindicatesthebenefitsofincorporatinghistory
dataforprediction;and(ii)asanLSTM-basedgeneral-purpose
encoder-decoder,Seq2Seqisknowntohavestrongerrepresentation
power[37,59]comparedtoGDBT.Thisisbestdemonstratedinthe
regressionresultsshowninTable8whereformostcasesSeq2Seq
hasfarlowerMAEsandRMSEs.
Transferability Analysis. Comparing feature groups – L+M
v/s. T+M and L+M+C v/s. T+M+C, we see that the prediction
results obtained using tower-based (T*) features, which are
location-agnostic,matchthoseusinglocation-based(L*)features.A
keyadvantageinusingtheT-basedfeaturegroupsisthatMLmodels
trainedononeareamaypotentiallybetransferabletoanotherarea
ifbothsharesimilarenvironments.Todemonstratethat,atthe
186

IMC’20,October27–29,2020,VirtualEvent,USA ArvindNarayanan,EmanRamadan,RishabhMehta,XinyueHu,etal.
Table9:PerformanceComparisonWithBaselineModelson 37%intheweightedaverageF1-score.History-basedmodelssuch
GlobalDataset-BothRegressionandClassificationSetups.
asHarmonicMean(HM)–thattypicallyusetheimmediatepast
Feature throughputobservationstomakefuturepredictionsinreal-time–
|        | KNN | RF[20] | OK6[26] | GDBT | Seq2Seq |                                                       |     |     |     |     |     |     |
| ------ | --- | ------ | ------- | ---- | ------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| Group⇓ |     |        |         |      |         | alsosufferduetothewildandfrequentfluctuationsinmmWave |     |     |     |     |     |     |
5Gthroughput.ThesuperiorityofLumos5Gmostlystemsfrom
|     |     | Regression(Metrics–MAE |     | RMSE) |     |     |     |     |     |     |     |     |
| --- | --- | ---------------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
tworeasons:(1)judiciousfeatureselectionbyconsideringdiverse
| L   | 285 | 362 300 378 | 316 442 | 225 | 314 208 273 |     |     |     |     |     |     |     |
| --- | --- | ----------- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
L+M 229 303 256 330 NA 127 186 74 144 impactfactorsaffecting5Gthroughput,and(2)theexpressiveness
oftheMLmodelsthemselves,e.g.,the“deep”natureoftheSeq2Seq
| T+M | 252 | 326 173 253 | NA  | 115 | 173 52 109 |     |     |     |     |     |     |     |
| --- | --- | ----------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
model(§5.2).ResultsforotherareascanbefoundinAppendixA.3.
| L+M+C | 223                                            | 311 162 241 | NA   | 109  | 166 49 112 |               |     |     |     |     |     |     |
| ----- | ---------------------------------------------- | ----------- | ---- | ---- | ---------- | ------------- | --- | --- | --- | --- | --- | --- |
| T+M+C | 228                                            | 320 163 241 | NA   | 100  | 154 57 119 |               |     |     |     |     |     |     |
|       | Classification(Metric–WeightedaverageF1-score) |             |      |      |            | 7 RELATEDWORK |     |     |     |     |     |     |
| L     | 0.67                                           | 0.61        | 0.63 | 0.78 | 0.73       |               |     |     |     |     |     |     |
VariousML-basedoranalyticalmodelshavebeenproposedfor
| L+M   | 0.74 | 0.68 | NA  | 0.90 | 0.93 |                 |             |             |              |            |                  |          |
| ----- | ---- | ---- | --- | ---- | ---- | --------------- | ----------- | ----------- | ------------ | ---------- | ---------------- | -------- |
|       |      |      |     |      |      | 3G/4G cellular  | networks.   |             | For example, | Margolies  | et               | al. [43] |
| T+M   | 0.73 | 0.70 | NA  | 0.91 | 0.95 |                 |             |             |              |            |                  |          |
|       |      |      |     |      |      | incorporate     | UE mobility | prediction  |              | in channel | state estimation |          |
| L+M+C | 0.75 | 0.72 | NA  | 0.92 | 0.96 |                 |             |             |              |            |                  |          |
|       |      |      |     |      |      | for 3G resource |             | scheduling. | Schulman     | et al.     | [56] consider    | UE       |
| T+M+C | 0.73 | 0.75 | NA  | 0.92 | 0.95 |                 |             |             |              |            |                  |          |
Model:HistorybasedHarmonicMean(HM)[38,64] signal strength measurement for energy-aware scheduling of
|                |     |                    |     |         |     | user data          | sessions.    | Chakraborty | et            | al. [26] | employ Ordinary |         |
| -------------- | --- | ------------------ | --- | ------- | --- | ------------------ | ------------ | ----------- | ------------- | -------- | --------------- | ------- |
|                |     | Regression(Metric– | MAE | RMSE)   |     |                    |              |             |               |          |                 |         |
|                |     |                    |     |         |     | Kriging (OK)-based |              | geospatial  | interpolation |          | that relies     | on      |
| PastThroughput |     |                    |     | 231 340 |     |                    |              |             |               |          |                 |         |
|                |     |                    |     |         |     | strong spatial     | correlations |             | to build      | spectrum | maps,           | whereas |
Classification(Metric–WeightedaverageF1score)
Alimpertisetal.[20]useRandomForest(RF)modelstopredictLTE
| PastThroughput |     |     |     | 0.73 |     |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
signalstrengthsandbuildcampus-wide(orcity-wide)4Gsignal
Airportarea,usingthedatacollectedfromUEsconnectedtoNorth strengthmaps.Asimilareffortisalsoseenin[54]whichstudies
panel,wetrainaT+Mmodel.Wethenusethatmodeltotestthe the key information needed for 4G throughput prediction. An
LSTM-baseddeeplearningmodelisproposedin[45]forpredicting
| features | associated | with the | South panel, | and | achieve a decent |     |     |     |     |     |     |     |
| -------- | ---------- | -------- | ------------ | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
3G/4Gthroughputattheimmediatenexttimeslotonly.Severalof
weightedaverageF1-score(w-avgF1)of0.71.WhentheUE-Panel
thesestudieshavepointedoutthatlocation-aloneisinsufficient
distanceislessthan25m,thew-avgF1furtherincreasesto0.91as
thereexistshighenvironmentalsimilaritybetweentheNorthand topredict3G/4Gsignalstrengths/throughputperformance;other
Southpanelswithinthisrange. factorssuchasmobility,indoor/outdoor,etc.mustbeaccountedfor.
InthecaseofmmWave5Gthroughputprediction,therearefarmore
FeatureImportanceAnalysis.WeuseGDBT’scapabilityof
complexfactorsatplay,and5Gthroughputpredictionisfarharder
reportingthefeatures’globalimportancetounderstandhoweach
than3G/4Gprediction.Forexample,duetovariousobstructionsin
| individual | feature | contributes | to the | final prediction | outcome. |     |     |     |     |     |     |     |
| ---------- | ------- | ----------- | ------ | ---------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Overall, we find that no single feature or feature group alone anenvironment,therearefarlessspatialcorrelations.Wecannot
dominatesinpredicting5Gthroughput.Weincludeamoredetailed relyongeospatialinterpolationalonetobuild5Gthroughputmaps.
Aswehaveshownearlier,theexistingMLmodelsproposedinthe
analysisofglobalfeatureimportanceinAppendixA.2.Theresults
literaturedonotperformaswellasourmethods.Todemonstrate
furthersupportourargumentthatvariousfactorsandtheircomplex
thekeydifferencesbetween5Gand3G/4Gperformanceprediction,
interplaycollectivelyaffect5Gthroughput.
wehaveconductedacomparativestudydetailsofwhichcanbe
6.3 ComparisonwithExistingModels
foundinAppendixA.4.
We now compare the performance of our ML models used in Ourworkfurtherdiffersfromexisting3G/4GMLmodelsinsev-
Lumos5Gwithseveralbaselinemodelsthathavebeenproposed eralotheraspects.Allexistingmodelsuseafixedsetoffeatures
in the literature for 3G/4G performance prediction: (1) forprediction(someofwhichmaybemissingorinaccessibleby
Classic
ML: Random Forest (RF) [20], KNN; (2) Analytical: Ordinary UE).Instead,byintroducingprimaryandcomposedfeaturegroups,
Kriging(OK)[26],HarmonicMean(HM)[38,64].WhileHMis Lumos5Gframeworkenablestoselectandcomposefeaturegroups
usedforshort-termpredictions,othershavebeenusedintheshort thatcanbereadilycollectedandrelevanttothecurrentusecase
andlongtermpredictioncontexts. andcontext.Furthermore,weconsidertwoclassesofMLmodels
Tocompareclassification-basedmodels,weagainuseweighted inconjunctionwithfeaturegrouping.Thisallowsustotakeadvan-
tageofthemorepowerfulSeq2Seqforhigherpredictionaccuracy,
| averageF1-score |     | (w-avgF1)asthemetric,whileMAE |     |     | andRMSE |     |     |     |     |     |     |     |
| --------------- | --- | ----------------------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
areusedforregression.Wecombineallthedata(i.e.,theGlobal whileemployinglight-weight,interpretableGDBTtoinvestigate
datasetdiscussedearlier)andevaluateourmodelsagainstthese thefeatureimportanceandbuildbest“explainable”MLmodels
baselines. Table 9 shows a summary of the results. The results for5Gthroughputprediction.Inaddition,byconsideringlocation-
clearlyshowthesuperiorityofGDBTandSeq2Seqmodelsover agnostictower-basedfeatures,wehaveshownthereispotentialin
developingtransferableMLmodelsthatarelocation-independent.
| the baseline | models | across | all the feature | groups. | For instance, |     |     |     |     |     |     |     |
| ------------ | ------ | ------ | --------------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
ourregressionmodelsareabletoachieve27%to79%reductionin
8 DISCUSSION
MAE,whileclassificationmodelsshowanimprovementof9%to
Next,wediscussthelimitationsofourworkandalsohighlightthe
6OrdinaryKriging(OK)isagridinterpolationalgorithm,hencecanonlyworkon
Lfeaturegroup.Forotherfeaturegroups,OKisthereforenotapplicable(NA). possiblefutureextensions.
187

Lumos5G:MappingandPredictingCommercialmmWave5GThroughput IMC’20,October27–29,2020,VirtualEvent,USA
8.1 LimitationsofOurWork Withallsuchinformationalreadyavailable,5Gcarrierscanclearly
With the goal to build ML models for throughput prediction, adopt/adaptLumos5GframeworkandbuildsimilarMLmodels.
our study relies primarily on the measurement of key UE-side User-CarrierCollaborative&CrowdsourcedPlatforms.We
factors affecting 5G throughput performance, as well as other furthersuggestauser-carriercollaborativeapproachtotacklethe
exogenousinformation(e.g.,5Gtowerandpanellocations)that challengesposedby5Gnetworkstoreapthebenefitsofferedby
canbegathered.WedonotheavilyutilizePHY-layerfeaturesdue 5G.Forexample,channelstate,handoff,andotherinformationob-
totworeasons:(1)noabilityyettounlockbootloaders(thusno tainedat5Gtowerscanbeusedby5Gcarriersforbetterthroughput
rootaccess)formmWave-based5Gsmartphonemodelssupported predictionwhichcanbefedbackto5G-awareapplicationsthrough
byUScarriers,(2)Android10’s5G-NRAPIsforaccessingsignal APIsprovidedbymobileOSessuchasAndroid,e.g.,viatheMOWIE
strength(e.g.,getCsiRsrp()orgetDbm(),see[4]forAPIdetails) mechanismproposedin[65].Likewise,UEcanprovideapplication
didnotalwaysprovidemeaningfuldata,hencenothighlyreliable. informationsuchasitsdemandsto5Gtowersthatcanaidcarri-
Ourstudyisalsolimitedtoonesmartphonedevicemodel.Ideally, ersinresourceallocationandscheduling.Recognizingsuchneeds,
UEdevicemodelshouldalsobeincludedasaninputfeature(say, severalformalefforts[1,5]areunderway,butarenotyetfully
partofafeaturegroupcalled“StaticFeatures”).Undoubtedly,differ- operational.Conventionally,cellularprovidershavereliedontheir
entdevicemodelsandtheirspecificationssuchasprocessor/RAM, ownradiosignalqualitytesting,congestion,andcoveragemapping
5Gmodemcapabilities[7,10,18],antennadesign[36],etc.will tohelpconfigureandmanagetheirradioaccessnetworks(RANs).
likelyhavehighimpactonthe5Gthroughputperformance.Study- ThecomplexityofmmWave5Gandfuturemultiband5G[14,15]
ingtheimpactofdevicemodelwillbeleftaspartofourfuture makessuchoperationsfarmorecostly,ifnotimpractical.Webe-
work.Wearealsounabletoaccountfortheimpactofother“un- lieveauser-carriercollaborative,crowdsourcedplatformisthemost
controllable”factorssuchasradioresourcecontention7 atRAN promisingavenuetorealizeourenvisaged5Gthroughputmap-
orcongestionatthewiredcorenetwork/Internet.Ourstudyalso ping,bringingbenefitstoallstakeholders–from5Gcarriersto
revealsotherresearchopportunities,including:(1)transferability users/customerstoapplicationdevelopersandproviders.
ofourproposedMLmodelsacrossdifferentareas;(2)temporalgen- Building5G-AwareApps.Ourstudypointsoutboththeop-
eralizabilityofsuchmodelsoverultra-short(daily),short(seasonal) portunitiesandchallengesinbuilding5G-awareapps.Inparticular,
andlong(yearly)timescales;and(3)sensitivityofthemodelsto totacklehighbandwidthvariability,newmechanismsarecalledfor.
inaccuraciesininputfeaturevalues.Amorecomprehensivestudy Ourpreliminarystudyshowsthatexistingadaptivebitrateadap-
ontheseaspectsisleftaspartoffuturework. tion(ABR)algorithmsbasedonthroughputmeasurementalone
Whilewehaveconductedextensivemeasurementsandexperi- donotworkwellforultra-HD(e.g.,8K)videostreamingover5G.
mentsatvariouslocations(bothindoorandoutdoor)inalargeU.S. UsingLumos5Gforthroughputprediction,weproposenewrate
cityanddownloadedover35,000GBsofdatausing5Gnetwork, adaptationalgorithmswithlayeredvideocoding,“contentbursting”
thecoverageofourstudyisstilllimited.Clearly,thereisaneed andmulti-radioswitchingmechanisms.Clearly,fullyexploringthe
foramuchlargercorpusofdatawithincreaseduserparticipation issuesindeveloping5G-awareappswarrantsanotherpaper.
indatacollection–highlightingtheimportanceofcrowdsourced
9 CONCLUDINGREMARKS
platforms[48].Nonetheless,ourstudydemonstratesthefeasibility
ofpredictingmmWavethroughputperformancewithareasonable Wehaveconductedafirst-of-its-kindstudyonunderstandingthe
accuracybasedprimarilyonUE-sidefactors. predictabilityofmmWave5Gthroughput.DespitemmWave5G’s
fastattenuationanditssensitivitytoenvironment/mobility,wefind
8.2 NeedforCollaborativeEfforts
thatitisindeedfeasibletopredictitsthroughput,bothqualitatively
Lumos5GanditsMLmodelsaredesignedtopredict5Gthroughput and quantitatively, via a carefully designed ML framework –
withanemphasisonaidingapplicationsusing5GservicesonUE. Lumos5G.Ourexperiencesindicatetheimportanceofselecting
Manyofthefeaturesrequiredbyourproposedmodelssuchas composable 5G-specific features discovered from our extensive
userlocation,mobilityspeeds,etc.mightnotalwaysbeavailableto measurements, as well as the benefits of using expressive deep
applicationdevelopers.Thisraisesquestionsonhowsuchmodels learningarchitecturesthatcanminethecomplexinterplayamong
canbebuiltorwhowillbuildthem.Mobilecarriersareplausible thefeatures.Ourstudyhintsthepotentialofdevelopingacity-level
candidates,astheyalreadycollectUE-sidedatasuchasthetower or even country-level fine-grained “performance map” of 5G
UEsareconnectedto,radiosignalstrength,userdatausage,etc. services,whichcanbenefitnumerousapplicationsover5G.
forbillingandresourcemanagementpurposes.Additionally,as
mmWavesignalsarehighlydirectionalinnature[41,52],carriers ACKNOWLEDGMENTS
providingmmWave-based5Gserviceneedtotrackusermovement
WethankourshepherdNeilSpringandtheanonymousreviewers
forbeamformingandmobilitymanagementpurposes.Moreimpor-
fortheirinsightfulsuggestionsandfeedback.WealsothankGlenn
tantly,carriersalsohaveknowledgeabouttheir5Gnetworksuch
Hutt,JeffBjorklund,MetropolitanAirportsCommissionandMSP
asthelocation/propertiesof5Gpanels/services,bandssupported
Airportauthoritiestoaidandallowusconductourmeasurement
by their 5G network (e.g., low-/mid-/high- band or multiband),
studyattheMinneapolis-SaintPaulInternational(MSP)airport.
carrier’sback-haulcapacity,UEcongestionaroundthetower,etc.
ThisresearchwasinpartsupportedbyNSFunderGrantsCNS-
1903880,CNS-1915122,CNS-1618339,CNS-1617729,CNS-1814322,
7AsimpleandpreliminarystudyontheimpactofthenumberofUEsoverindividual
CNS-1831140,CNS-1836772,andCNS-1901103.
UE’s5GdatarateisincludedinAppendixA.1.4.
188

IMC’20,October27–29,2020,VirtualEvent,USA ArvindNarayanan,EmanRamadan,RishabhMehta,XinyueHu,etal.
REFERENCES
[27] JiasiChen,RajeshMahindra,MohammadAmirKhojastepour,SampathRan-
[1] 2017. Mobile Throughput Guidance Inband Signaling Proto- garajan,andMungChiang.2013.ASchedulingFrameworkforAdaptiveVideo
col. (2017). Retrieved June 2020 from https://tools.ietf.org/html/ DeliveryoverCellularNetworks.InProceedingsofthe19thAnnualInternational
draft-flinck-mobile-throughput-guidance-04 ConferenceonMobileComputing&Networking(MobiCom’13).Associationfor
[2] 2019.CellIdentityNr|AndroidDevelopers.(2019).RetrievedJune2020fromhttps: ComputingMachinery,NewYork,NY,USA,389–400. https://doi.org/10.1145/
//developer.android.com/reference/kotlin/android/telephony/CellIdentityNr 2500423.2500433
[3] 2019. CellInfoNr|AndroidDevelopers. (2019). RetrievedJune2020from [28] RALPHD’AGOSTINOandEgonSPearson.1973. Tests√fordeparturefrom
https://developer.android.com/reference/kotlin/android/telephony/CellInfoNr normality.Empiricalresultsforthedistributionsofb2and 𝑏.Biometrika60,3
[4] 2019. CellSignalStrengthNr|AndroidDevelopers. (2019). RetrievedJune (1973),613–622.
2020fromhttps://developer.android.com/reference/kotlin/android/telephony/ [29] RalphBd’Agostino.1971.Anomnibustestofnormalityformoderateandlarge
CellSignalStrengthNr sizesamples.Biometrika58,2(1971),341–348.
[5] 2019. Developers: It’s your 5G wake-up call - time to [30] JeromeH.Friedman.2001.Greedyfunctionapproximation:Agradientboosting
start designing it into your apps. (2019). Retrieved June machine. Ann.Statist.29,5(102001),1189–1232. https://doi.org/10.1214/aos/
2020 from https://www.qualcomm.com/news/onq/2019/05/10/ 1013203451
developers-its-your-5g-wake-call-time-start-designing-it-your-apps [31] SignalsResearchGroup.2019.AGlobalPerspectiveof5GNetworkPerformance.
[6] 2019. Google Employee | Google Groups. (2019). Retrieved June 2020 (2019).RetrievedJune2020fromhttps://www.qualcomm.com/media/documents/
fromhttps://groups.google.com/d/msg/google-maps-js-api-v3/hDRO4oHVSeM/ files/signals-research-group-s-5g-benchmark-study.pdf
osOYQYXg2oUJ [32] QiHe,ConstantineDovrolis,andMostafaAmmar.2005.OnthePredictabilityof
[7] 2019. HuaweiLaunches5GMulti-modeChipsetand5GCPEPro. (2019). Re- LargeTransferTCPThroughput.SIGCOMMComput.Commun.Rev.35,4(Aug.
trievedJune2020fromhttps://www.huawei.com/en/press-events/news/2019/1/ 2005),145–156. https://doi.org/10.1145/1090191.1080110
huawei-5g-multi-mode-chipset-5g-cpe-pro [33] K.Heimann,J.Tiemann,D.Yolchyan,andC.Wietfeld.2019.Experimental5G
[8] 2019. iperf3–iperf33.7documentation. (2019). RetrievedJune2020from mmWaveBeamTrackingTestbedforEvaluationofVehicularCommunications.
https://software.es.net/iperf/ In2019IEEE2nd5GWorldForum(5GWF).382–387. https://doi.org/10.1109/
[9] 2019.MapandTileCoordinates|MapsJavaScriptAPI|GoogleDevelopers.(2019). 5GWF.2019.8911692
RetrievedJune2020fromhttps://developers.google.com/maps/documentation/ [34] J.D.Herath,A.Seetharam,andA.Ramesh.2019. ADeepLearningModel
javascript/coordinates forWirelessChannelQualityPrediction.InICC2019-2019IEEEInternational
[10] 2019.SnapdragonX505Gmodem-RFsystem.(2019).RetrievedJune2020from ConferenceonCommunications(ICC).1–6.
https://www.qualcomm.com/products/snapdragon-x50-5g-modem [35] SeppHochreiterandJürgenSchmidhuber.1997.Longshort-termmemory.Neural
[11] 2019.SpeedtestbyOokla.(2019).RetrievedJune2020fromhttps://www.speedtest. computation9,8(1997),1735–1780.
net/ [36] W.Hong,K.Baek,Y.Lee,Y.Kim,andS.Ko.2014. Studyandprototypingof
[12] 2019. Tiles - Google Maps: Coordinates, Tile Bounds and Projec- practicallylarge-scalemmWaveantennasystemsfor5Gcellulardevices.IEEE
tion - conversion to EPSG:3785 and EPSG:4326 (WGS84) - Map- CommunicationsMagazine52,9(2014),63–69.
Tiler. (2019). Retrieved June 2020 from https://www.maptiler.com/ [37] KurtHornik,MaxwellStinchcombe,HalbertWhite,etal.1989.Multilayerfeed-
google-maps-coordinates-tile-bounds-projection/ forwardnetworksareuniversalapproximators. Neuralnetworks2,5(1989),
[13] 2020.5GCoverageMap:Thisis5GBuiltRight|Verizon.(2020).RetrievedJune 359–366.
2020fromhttps://www.verizon.com/5g/coverage-map/ [38] JunchenJiang,VyasSekar,andHuiZhang.2012.ImprovingFairness,Efficiency,
[14] 2020.5GLowLatencyRequirements.(2020).RetrievedJune2020fromhttps: andStabilityinHTTP-BasedAdaptiveVideoStreamingwithFESTIVE.InPro-
//broadbandlibrary.com/5g-low-latency-requirements/ ceedingsofthe8thInternationalConferenceonEmergingNetworkingExperiments
[15] 2020. 5Gspectrum: strategies tomaximize allbands. (2020). Retrieved andTechnologies(CoNEXT’12).AssociationforComputingMachinery,NewYork,
June2020fromhttps://www.ericsson.com/en/networks/trending/hot-topics/ NY,USA,97–108. https://doi.org/10.1145/2413176.2413189
5g-spectrum-strategies-to-maximize-all-bands [39] WooseongKim.2019. ExperimentalDemonstrationofMmWaveVehicle-to-
[16] 2020.getSpeed()|Location|AndroidDevelopers.(2020).RetrievedJune2020from VehicleCommunicationsUsingIEEE802.11ad.Sensors19,9(2019),2057.
https://developer.android.com/reference/android/location/Location#getSpeed() [40] K.Larsson,B.Halvarsson,D.Singh,R.Chana,J.Manssour,M.Na,C.Choi,
[17] 2020.KeysightTechnologies|Engineeringthe5GWorldJustGotEasier.(2020). andS.Jo.2017.High-SpeedBeamTrackingDemonstratedUsinga28GHz5G
RetrievedJune2020fromhttps://www.keysight.com/us/en/assets/7119-1223/ TrialSystem.In2017IEEE86thVehicularTechnologyConference(VTC-Fall).1–5.
ebooks/Engineering-the-5G-World.pdf https://doi.org/10.1109/VTCFall.2017.8288043
[18] 2020.SnapdragonX555Gmodem-RFsystem.(2020).RetrievedJune2020from [41] X.Liu,J.Yu,H.Qi,J.Yang,W.Rong,X.Zhang,andY.Gao.2020. Learning
https://www.qualcomm.com/products/snapdragon-x55-5g-modem toPredicttheMobilityofUsersinMobilemmWaveNetworks. IEEEWireless
[19] 3rdGenerationPartnershipProject.2019. Release15. (April2019). Retrieved Communications27,1(2020),124–131.
June2020fromhttps://www.3gpp.org/release-15 [42] FengLu,HaoDu,AnkurJain,GeoffreyM.Voelker,AlexC.Snoeren,andAndreas
[20] EmmanouilAlimpertis,AthinaMarkopoulou,CarterButts,andKonstantinos Terzis.2015. CQIC:RevisitingCross-LayerCongestionControlforCellular
Psounis.2019.City-WideSignalStrengthMaps:PredictionwithRandomForests. Networks.InProceedingsofthe16thInternationalWorkshoponMobileComputing
InTheWorldWideWebConference(WWW’19).AssociationforComputing SystemsandApplications(HotMobile’15).AssociationforComputingMachinery,
Machinery,NewYork,NY,USA,2536–2542. https://doi.org/10.1145/3308558. NewYork,NY,USA,45–50. https://doi.org/10.1145/2699343.2699345
3313726 [43] Robert Margolies, Ashwin Sridharan, Vaneet Aggarwal, Rittwik Jana, NK
[21] TheodoreWAndersonandDonaldADarling.1952. Asymptotictheoryof Shankaranarayanan,VinayAVaishampayan,andGilZussman.2016.Exploiting
certain"goodnessoffit"criteriabasedonstochasticprocesses. Theannalsof mobilityinproportionalfaircellularscheduling:Measurementsandalgorithms.
mathematicalstatistics(1952),193–212. IEEE/ACMTransactionsonNetworking(TON)24,1(2016),355–367.
[22] A.BakreandB.R.Badrinath.1995. I-TCP:indirectTCPformobilehosts.In [44] R.Margolies,A.Sridharan,V.Aggarwal,R.Jana,N.K.Shankaranarayanan,V.A.
Proceedingsof15thInternationalConferenceonDistributedComputingSystems. Vaishampayan,andG.Zussman.2016.ExploitingMobilityinProportionalFair
136–143. CellularScheduling:MeasurementsandAlgorithms.IEEE/ACMTransactionson
[23] HariBalakrishnan,SrinivasanSeshan,ElanAmir,andRandyH.Katz.1995. Networking24,1(2016),355–367.
ImprovingTCP/IPPerformanceoverWirelessNetworks.InProceedingsofthe1st [45] LifanMei,RunchenHu,HouweiCao,YongLiu,ZifaHan,FengLi,andJinLi.2019.
AnnualInternationalConferenceonMobileComputingandNetworking(MobiCom Realtimemobilebandwidthpredictionusinglstmneuralnetwork.InInternational
’95).AssociationforComputingMachinery,NewYork,NY,USA,2–11. https: ConferenceonPassiveandActiveNetworkMeasurement.Springer,34–47.
//doi.org/10.1145/215530.215544 [46] MariyamMirza,JoelSommers,PaulBarford,andXiaojinZhu.2007.AMachine
[24] KevinBrownandSureshSingh.1997.M-TCP:TCPforMobileCellularNetworks. LearningApproachtoTCPThroughputPrediction.InProceedingsofthe2007
SIGCOMMComput.Commun.Rev.27,5(Oct.1997),19–43. https://doi.org/10. ACMSIGMETRICSInternationalConferenceonMeasurementandModelingof
1145/269790.269794 ComputerSystems(SIGMETRICS’07).AssociationforComputingMachinery,
[25] NicolaBui,MatteoCesana,SAmirHosseini,QiLiao,IlariaMalanchini,and NewYork,NY,USA,97–108. https://doi.org/10.1145/1254882.1254894
JoergWidmer.2017.Asurveyofanticipatorymobilenetworking:Context-based [47] ArvindNarayanan,EmanRamadan,JasonCarpenter,QingxuLiu,YuLiu,Feng
classification,predictionmethodologies,andoptimizationtechniques. IEEE Qian,andZhi-LiZhang.2020.AFirstLookatCommercial5GPerformanceon
CommunicationsSurveys&Tutorials19,3(2017),1790–1821. Smartphones.InProceedingsofTheWebConference2020(WWW’20).Association
[26] A.Chakraborty,M.S.Rahman,H.Gupta,andS.R.Das.2017.SpecSense:Crowd- forComputingMachinery,NewYork,NY,USA,894–905. https://doi.org/10.1145/
sensingforefficientqueryingofspectrumoccupancy.InIEEEINFOCOM2017 3366423.3380169
-IEEEConferenceonComputerCommunications.1–9. https://doi.org/10.1109/ [48] ArvindNarayanan,EmanRamadan,JacobQuant,PeiqiJi,FengQian,andZhi-Li
INFOCOM.2017.8057113 Zhang.2020.5GTracker–ACrowdsourcedPlatformtoEnableResearchUsing
189

Lumos5G:MappingandPredictingCommercialmmWave5GThroughput IMC’20,October27–29,2020,VirtualEvent,USA
Commercial5GServices.InProceedingsoftheACMSIGCOMM2020Conference 5163–5167.
PostersandDemos(SIGCOMMPostersandDemos’20).AssociationforComputing [67] KunZhao,JakobHelander,DanielSjöberg,SailingHe,ThomasBolin,andZhi-
Machinery,VirtualEvent,USA. https://doi.org/10.1145/3405837.3411394 nongYing.2016.Userbodyeffectonphasedarrayinuserequipmentforthe5G
[49] ArvindNarayanan,SaurabhVerma,EmanRamadan,PariyaBabaie,andZhi-Li mmWavecommunicationsystem.IEEEantennasandwirelesspropagationletters
Zhang.2019.MakingContentCachingPolicies’Smart’UsingtheDeepCache 16(2016),864–867.
Framework.SIGCOMMComput.Commun.Rev.48,5(Jan.2019),64–69. https: [68] K.Zhao,J.Helander,D.Sjöberg,S.He,T.Bolin,andZ.Ying.2017.UserBody
//doi.org/10.1145/3310165.3310174 EffectonPhasedArrayinUserEquipmentforthe5GmmWaveCommunication
[50] RohitPrabhavalkar,KanishkaRao,TaraSainath,BoLi,LeifJohnson,andNavdeep System.IEEEAntennasandWirelessPropagationLetters16(2017),864–867.
Jaitly.2017.AComparisonofSequence-to-SequenceModelsforSpeechRecogni- [69] YiboZhu,ZengbinZhang,ZhinusMarzi,ChrisNelson,UpamanyuMadhow,
tion.http://www.isca-speech.org/archive/Interspeech_2017/pdfs/0233.PDF BenY.Zhao,andHaitaoZheng.2014.Demystifying60GHzOutdoorPicocells.In
[51] T.S.Rappaport,G.R.MacCartney,M.K.Samimi,andS.Sun.2015.Wideband Proceedingsofthe20thAnnualInternationalConferenceonMobileComputingand
Millimeter-WavePropagationMeasurementsandChannelModelsforFuture Networking(MobiCom’14).AssociationforComputingMachinery,NewYork,
WirelessCommunicationSystemDesign.IEEETransactionsonCommunications NY,USA,5–16. https://doi.org/10.1145/2639108.2639121
63,9(2015),3029–3056. [70] XuanKelvinZou,JeffreyErman,VijayGopalakrishnan,EmirHalepovic,Rit-
[52] MaryamEslamiRasekh,ZhinusMarzi,YanziZhu,UpamanyuMadhow,and twikJana,XinJin,JenniferRexford,andRakeshK.Sinha.2015.CanAccurate
HaitaoZheng.2017. NoncoherentMmWavePathTracking.InProceedingsof PredictionsImproveVideoStreaminginCellularNetworks?.InProceedingsof
the18thInternationalWorkshoponMobileComputingSystemsandApplications the16thInternationalWorkshoponMobileComputingSystemsandApplications
(HotMobile’17).AssociationforComputingMachinery,NewYork,NY,USA, (HotMobile’15).AssociationforComputingMachinery,NewYork,NY,USA,
13–18. https://doi.org/10.1145/3032970.3032974 57–62. https://doi.org/10.1145/2699343.2699359
[53] Haakon Riiser, Tore Endestad, Paul Vigmostad, Carsten Griwodz, and Pâl
Halvorsen.2012. Videostreamingusingalocation-basedbandwidth-lookup
A APPENDICES
serviceforbitrateplanning.ACMTransactionsonMultimediaComputing,Com-
munications,andApplications(TOMM)8,3(2012),1–19.
A.1 5GThroughputPerformanceImpact
[54] A.Samba,Y.Busnel,A.Blanc,P.Dooze,andG.Simon.2017. Instantaneous
throughputpredictionincellularnetworks:Whichinformationisneeded?.In FactorAnalysis:ExtendedResults
2017IFIP/IEEESymposiumonIntegratedNetworkandServiceManagement(IM).
624–627. A.1.1 ImpactofGeolocation. Fig.17showsextendedresults
[55] MathewKSamimiandTheodoreSRappaport.2016.3-Dmillimeter-wavestatisti- forthenormalityandLevenetestsfor§4.1.Usingasignificance
calchannelmodelfor5Gwirelesssystemdesign.IEEETransactionsonMicrowave
TheoryandTechniques64,7(2016),2207–2225.
valueof(0.001),thenormalitytestshowsthatthroughputmea-
[56] AaronSchulman,VishnuNavda,RamachandranRamjee,NeilSpring,Pralhad surements of roughly 48% of geolocations (i.e., almost half the
Deshpande,CalvinGrunewald,KamalJain,andVenkataNPadmanabhan.2010. area)attheindoor(Airport)donot follownormaldistribution;
Bartendr:apracticalapproachtoenergy-awarecellulardatascheduling.InPro-
ceedingsofthesixteenthannualinternationalconferenceonMobilecomputingand similarlyfortheoutdoor(Intersection)thepercentageofgeolo-
networking.ACM,85–96. cationsis∼33%.Usingasignificancevalueof(0.1),theLevenetest
[57] SumitSingh,FedericoZiliotto,UpamanyuMadhow,EBelding,andMarkRodwell.
showsthatthevariancesofthroughputmeasurementsof64.26%
2009.Blockageanddirectivityin60GHzwirelesspersonalareanetworks:From
cross-layermodeltomultihopMACdesign. IEEEJournalonSelectedAreasin and61.06%ofthegeolocationpairssignificantlydifferfromeach
Communications27,8(2009),1400–1413. otherfortheIndoor(Airport)andtheoutdoor(Intersection),
[58] YiSun,XiaoqiYin,JunchenJiang,VyasSekar,FuyuanLin,NanshuWang,Tao
Liu,andBrunoSinopoli.2016.CS2P:ImprovingVideoBitrateSelectionandAdap- respectively.
tationwithData-DrivenThroughputPrediction.InProceedingsofthe2016ACM 1.00
SIGCOMMConference(SIGCOMM’16).AssociationforComputingMachinery,
NewYork,NY,USA,272–285. https://doi.org/10.1145/2934872.2934898 0.75
[59] IlyaSutskever,OriolVinyals,andQuocVLe.2014.Sequencetosequencelearning
withneuralnetworks.InAdvancesinneuralinformationprocessingsystems.3104– 0.50
3112.
[60] N.Theera-Ampornpunt,T.Mangla,S.Bagchi,R.Panta,K.Joshi,M.Ammar,and 0.25
E.Zegura.2016. TANGO:TowardaMoreReliableMobileStreamingthrough
CooperationbetweenCellularNetworkandMobileDevices.In2016IEEE35th 0.00
SymposiumonReliableDistributedSystems(SRDS).297–306. 0.00 0.05 0.10 0.15 0.20
[61] S.Venugopalan,M.Rohrbach,J.Donahue,R.Mooney,T.Darrell,andK.Saenko.
normality test(p-val)
2015.SequencetoSequence–VideotoText.In2015IEEEInternationalConference
onComputerVision(ICCV).4534–4542.
[62] XiufengXie,XinyuZhang,SwarunKumar,andLiErranLi.2016.PiStream:Physi-
calLayerInformedAdaptiveVideoStreamingOverLTE.GetMobile:MobileComp.
andComm.20,2(Oct.2016),31–34. https://doi.org/10.1145/3009808.3009819
[63] QiangXu,SanjeevMehrotra,ZhuoqingMao,andJinLi.2013.PROTEUS:Net-
workPerformanceForecastforReal-Time,InteractiveMobileApplications.In
Proceedingofthe11thAnnualInternationalConferenceonMobileSystems,Appli-
cations,andServices(MobiSys’13).AssociationforComputingMachinery,New
York,NY,USA,347–360. https://doi.org/10.1145/2462456.2464453
[64] XiaoqiYin,AbhishekJindal,VyasSekar,andBrunoSinopoli.2015.AControl-
TheoreticApproachforDynamicAdaptiveVideoStreamingoverHTTP.In
Proceedingsofthe2015ACMConferenceonSpecialInterestGrouponDataCom-
munication(SIGCOMM’15).AssociationforComputingMachinery,NewYork,
NY,USA,325–338. https://doi.org/10.1145/2785956.2787486
[65] YunfeiZhang,GangLi,ChunshanXiong,YixueLei,WeiHuang,YunboHan,
AnwarWalid,Y.RichardYang,andZhi-LiZhang.2020. MoWIE:Toward
Systematic, Adaptive Network Information Exposure as an Enabling Tech-
niqueforCloud-BasedApplicationsover5GandBeyond(InvitedPaper).In
Proceedings of the 2020 Workshop on Network Application Integration/CoDe-
sign,NAI@SIGCOMM2020,VirtualEvent,USA,August14,2020.ACM,20–27.
https://doi.org/10.1145/3405672.3409489
[66] HangZhao,RimmaMayzus,ShuSun,MathewSamimi,JocelynKSchulz,Yaniv
Azar,KevinWang,GeorgeNWong,FelixGutierrezJr,andTheodoreSRappa-
port.2013.28GHzmillimeterwavecellularcommunicationmeasurementsfor
reflectionandpenetrationlossinandaroundbuildingsinNewYorkcity..InICC.
FDC
1.00
0.75
0.50
Indoor 0.25
Outdoor
0.00
0.00 0.05 0.10 0.15 0.20
Levene test(p-val)
FDC
Indoor
Outdoor
Figure17:Indoorv/sOutdoor:Normality&LeveneTests.
A.1.2 (Indoor)ImpactofMobilityDirection. Withthesamemo-
bilitydirection,78.05%ofgeolocationshavethroughputsamples
thatarenormallydistributed–anincreaseofover25%,compared
tothecasewhenmobilitydirectionisignoredasshowninTable4.
Asforthepairwiset-test,withtheconsiderationofthemobility
direction information, 80.87% of the geolocation pairs have sig-
nificantlydifferentthroughputmeans(i.e.,anincreaseof10.01%).
Moreover,29.76%ofgeolocationshavethroughputsampleswith
CVvaluesgreaterthan50%–adecreaseof23%whenmobility
directionwasignored.Thisindicatesthatthevariancesofthrough-
putsamplesatagivengeolocationdecreaseswhenthemobility
directionisaccountedfor.Fig.19showsextendedresultsforthe
impactofmobilitydirectionoftheindoor(Airport)areain§4.2
ofbothtrajectories(NB,SB)aswellasthecombinedtrajectories
whenthemobilitydirectionisignored(NB+SB).
Fig.20showsthe12trajectoriesoftheoutdoor(Intersection)
areaaswellastheimpactwhenthemobilitydirectionisaccounted
190

IMC’20,October27–29,2020,VirtualEvent,USA ArvindNarayanan,EmanRamadan,RishabhMehta,XinyueHu,etal.
NorthPanel
)spbM(tuphguorhT
1600
1200
800
400
0
[0,15) [15,30) [30,45) [45,60) [60,75) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) 5,360]
|     |     |     |     | [75,90 90,10 5 | 05,12 0 0,13 5 5,15 0 0,16 | 5 5,18 0 0,19 | 5 5,21 0 0,22 | 5 5,24 0 0,25 | 5 5,27 0 0,28 | 5 5,30 0 0,31 5 | 5,33 0 0,34 5 |     |     |
| --- | --- | --- | --- | -------------- | -------------------------- | ------------- | ------------- | ------------- | ------------- | --------------- | ------------- | --- | --- |
4
|     |     |     |     | [ [ 1 | [1 2 [1 3 [1 5 | [1 6 [1 8 | [1 9 [2 1 [2 | 2 [2 4 [2 | 5 [2 7 | [2 8 [3 0 [3 | 1 [3 3 [3 |     |     |
| --- | --- | --- | --- | ----- | -------------- | --------- | ------------ | --------- | ------ | ------------ | --------- | --- | --- |
UE-PanelMobilityAngleinDegrees(rangeofθpin◦)
SouthPanel
)spbM(tuphguorhT
1600
1200
800
400
0
[0,15) [15,30) [30,45) [45,60) [60,75) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) 5,360]
|     |     |     |     | [75,90 90,10 5 | 05,12 0 0,13 5 5,15 0 0,16 | 5 5,18 0 0,19 | 5 5,21 0 0,22 | 5 5,24 0 0,25 | 5 5,27 0 0,28 | 5 5,30 0 0,31 5 | 5,33 0 0,34 5 |     |     |
| --- | --- | --- | --- | -------------- | -------------------------- | ------------- | ------------- | ------------- | ------------- | --------------- | ------------- | --- | --- |
|     |     |     |     | [ 1            | [1 2 [1 3 [1 5             | [1 6 [1 8 [1  | 9 [2 1 [2     | 2 [2 4 [2     | 5 [2 7        | [2 8 [3 0 [3    | 1 [3 3 [3 4   |     |     |
[
UE-PanelMobilityAngleinDegrees(rangeofθpin◦)
Figure18:ImpactofUE-PanelMobilityAngle𝜃 𝑝 byindividual5Gpanelson5GthroughputattheAirportarea.
|     | 1.00 |        |     | 1.00        |     |     | All    | t5only |     | t6only | d1only | t3only        |        |
| --- | ---- | ------ | --- | ----------- | --- | --- | ------ | ------ | --- | ------ | ------ | ------------- | ------ |
|     |      |        |     |             |     |     |        |        |     | All    | t5only | t6only d1only | t3only |
|     |      |        |     |             |     |     | t2only | t1only |     | d2only | t8only | t7only        |        |
|     | 0.75 |        |     | 0.75        |     |     |        |        |     | t2only | t1only | d2only t8only | t7only |
|     |      |        |     |             |     |     | t4only | d4only |     | d3only |        |               |        |
|     |      |        |     |             |     |     |        |        |     | t4only | d4only | d3only        |        |
| FDC |      |        | FDC |             |     |     |        |        |     |        |        |               |        |
|     | 0.50 |        |     | 0.50        |     |     | 1.0    |        |     | 1.0    |        |               |        |
|     |      | NB+SB  |     | NB+SB       |     |     |        |        |     |        |        |               |        |
|     | 0.25 | NBonly |     | 0.25 NBonly |     |     |        |        |     | 0.8    |        |               |        |
0.8
|     |      | SBonly |     | SBonly |     |     |     |     |     |     |     |     |     |
| --- | ---- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 0.00 |        |     | 0.00   |     |     |     |     |     | 0.6 |     |     |     |
FDC
|     | 0.00 0.05 | 0.10 0.15 | 0.20 | 0.00 0.05 | 0.10 0.15 0.20 | FDC | 0.6 |     |     |     |     |     |     |
| --- | --------- | --------- | ---- | --------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
0.4
|     | normality | test(p-val) |     | t test(p-val) |     |     |     |     |     |     |          |     |     |
| --- | --------- | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
|     |           |             |     | −             |     |     | 0.4 |     |     |     |          |     |     |
|     | 1.00      |             |     | 1.00          |     |     |     |     |     | 0.2 |          |     |     |
|     | 0.75      |             |     | 0.75          |     |     | 0.2 |     |     | 0.0 |          |     |     |
| FDC |           |             | FDC |               |     |     |     |     |     | 0   | 25 50 75 | 100 |     |
|     | 0.50      |             |     | 0.50          |     |     | 0.0 |     |     |     |          |     |     |
CV(in%)
|     |     | NB+SB |     |     | NB+SB |     | 0   | 25 50 | 75  | 100 |     |     |     |
| --- | --- | ----- | --- | --- | ----- | --- | --- | ----- | --- | --- | --- | --- | --- |
0.25 0.25 NBonly Figure20:(Outdoor)ImpactofMobilityTrajectory.
|     |      | NBonly |     |      |        |     |     | CV(in%) |     |     |     |     |     |
| --- | ---- | ------ | --- | ---- | ------ | --- | --- | ------- | --- | --- | --- | --- | --- |
|     |      | SBonly |     |      | SBonly |     |     |         |     |     |     |     |     |
|     | 0.00 |        |     | 0.00 |        |     |     |         |     |     |     |     |     |
panel),poorthroughputisobservedmostlikelyduetopoorNLoS
|     | 0.00 0.05 | 0.10 0.15   | 0.20 | 0 25 50 | 75 100 125 |                              |     |     |     |     |     |     |     |
| --- | --------- | ----------- | ---- | ------- | ---------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     | Levene    | test(p-val) |      | CV(in%) |            | pathintheairport’small-area. |     |     |     |     |     |     |     |
Figure19:(Indoor)ImpactofMobilityTrajectoryon
|     |     |     |     |     |     |     | A.1.4 CongestionwithotherUEs. |     |     | WhenmultipleUEsconnect |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | ---------------------- | --- | --- | --- |
NormalityTest,t-test,LeveneTest&CV.
tothesame5Gpanel,howdoes5Gthroughputgetaffected?To
answerthisquestion,weperformanexperimentintheAirport
forv/s.whenitisignored.Thesameobservationstillholds:con- areabyplacingmultipleUEsside-by-sidesuchthattheyallfallin
sideringmobilitydirectioninformationsignificantlyreducesthe thecoveragefootprintofasingle5Gpanel.Wedecideonalocation
thatisatadistanceof∼25mfromthe5Gpanelwithclearlineof
variancesofthroughputsamplesatagivengeolocation.
|     |     |     |     |     |     | sight(LoS).Weuse4UEs–𝑈𝐸 |     |     |     | ,𝑈𝐸 ,𝑈𝐸 | ,𝑈𝐸 –whereeachof |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | ------- | ---------------- | --- | --- |
|     |     |     |     |     |     |                         |     |     |     | 1 2     | 3 4              |     |     |
A.1.3 Impact of UE-Panel Mobility Angle. Fig. 18 shows the theUEsisscheduledtostartaniPerfsessionsuchthattheses-
effectoftheUE-panelmobilityangle𝜃
𝑚 on5Gthroughputw.r.t. sionstarttimestampsofeachdeviceareseparatedbyagapof1
thesouthandnorthpanels.Wecannoticethat,forbothpanels, minuteandtheendtimestampsarethesameforalldevices.Each
throughputishighwhentheUEismovingstraighttowardseither iPerfsessiononaUEisatleast1minutelong(thus,eachsetof
panels–i.e.,𝜃 𝑚 isintherange[165°,180°)(seeillustrationof𝜃 𝑚 experimentwithallthe4UEswas4-minutelong,seeFig.21).This
valuesinFig.8).Southpanelseemstohaveabettercoverageas allowedustooverlapiPerfsessionsrunningonseparateUEsthat
theUEcanachieverelativelygoodthroughputevenwhilemoving
areconnectedtothesame5Gpanelandobservetheimpactofthe
awayfromthepanel(i.e.,when𝜃
𝑚in[30°,75°]).Forcertainranges “artificiallyinduced”congestion.iPerfserversarerunningonVMs
suchas[210°,240°)forthesouthpaneland[90°,120°)forthenorth provisionedindifferentpublicclouds(e.g.,GoogleCloud,Amazon
191

Lumos5G:MappingandPredictingCommercialmmWave5GThroughput IMC’20,October27–29,2020,VirtualEvent,USA
Table10:SummaryofFactorsAffecting5GThroughputandItsPredictabilityfortheOutdoor(Intersection)Area.
|     |     | Results⇒ |     |     | StatisticalAnalysis |     |           |     | SimplePred.Models |     |           |     |     |
| --- | --- | -------- | --- | --- | ------------------- | --- | --------- | --- | ----------------- | --- | --------- | --- | --- |
|     |     |          |     | CV  | Norm.Test           |     | Sp.Coeff. |     |                   | KNN | RF[20,54] |     |     |
⇓UE-SideFactors (mean ±std.dev.)(p-val.>0.001)(mean ±std.dev.)MAE RMSE MAE RMSE
(1)Geolocation 52.83% ±20.28 66.54% 0.17 ±0.36 297 376 258 336
(2)Mobility+(1)
⊢UE-PanelDistance
⊢UE-PanelPositionalAngle 43.08% ±20.30 84.17% 0.49 ±0.08 258 337 238 310
⊢UE-PanelMobilityAngle
⊢MovingSpeed
|                    | Single   | 2           | 3           | 4           |     |     |     | LocationCoordinates |     |     | UE-PanelMobilityAngle |     |     |
| ------------------ | -------- | ----------- | ----------- | ----------- | --- | --- | --- | ------------------- | --- | --- | --------------------- | --- | --- |
|                    | client   | concu×rrent | concu×rrent | concu×rrent |     |     |     |                     |     |     |                       |     |     |
|                    |          |             |             |             |     |     |     | UECompassDirection  |     |     | UE-PanelAngle         |     |     |
|                    | download | download    | download    | download    |     |     |     | MovingSpeed         |     |     | RadioType             |     |     |
| )spbMni(tuphguorhT | 2000     |             |             |             |     |     |     | UE-TowerDistance    |     |     | Others                |     |     |
UE1PerceivedThroughput
4-wayIntersection(Outdoor)
|     | 1500 |     |     |     |     |       |     |      |      |     |      | ⇓    |      |
| --- | ---- | --- | --- | --- | --- | ----- | --- | ---- | ---- | --- | ---- | ---- | ---- |
|     |      |     |     |     |     | T+M+C |     | 21.9 | 21.8 |     | 21.7 | 20.0 | 8.2  |
|     |      |     |     |     |     | L+M+C |     | 39.9 |      |     | 22.3 | 16.2 | 15.7 |
1000
|                                                 |     |                     |     |     |     | T+M   |     | 31.0 |      | 30.0            |       | 27.0 | 12.0      |
| ----------------------------------------------- | --- | ------------------- | --- | --- | --- | ----- | --- | ---- | ---- | --------------- | ----- | ---- | --------- |
|                                                 | 500 |                     |     |     |     | L+M   |     |      | 54.0 |                 |       | 24.0 | 22.0      |
|                                                 |     |                     |     |     |     |       | L   |      |      |                 | 100.0 |      |           |
|                                                 | 0   |                     |     |     |     |       |     |      |      | Airport(Indoor) | ⇓19.8 |      |           |
|                                                 |     |                     |     |     |     | T+M+C |     | 32.9 |      | 21.0            |       |      | 11.5 11.4 |
|                                                 | 0   | 1                   | 2   | 3   | 4   |       |     |      |      |                 |       |      |           |
|                                                 |     |                     |     |     |     | L+M+C |     | 33.4 |      |                 | 28.5  | 25.9 | 11.7      |
|                                                 |     | Timeline(inminutes) |     |     |     | T+M   |     |      | 42.7 |                 | 26.6  |      | 18.4 12.3 |
|                                                 |     |                     |     |     |     | L+M   |     |      | 59.5 |                 |       | 25.2 | 15.3      |
| Figure21:Impacton5Gthroughputperceivedbyasingle |     |                     |     |     |     |       | L   |      |      |                 | 100.0 |      |           |
UEwhenmultipleUEsareconnectedtothesame5Gpanel.
Loop(Outdoor)
|     |     |     |     |     |     | L+M+C |     |     | 42.6 |     | 24.2 ⇓ | 15.3 | 9.6 8.3 |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | ---- | --- | ------ | ---- | ------- |
|     |     |     |     |     |     | L+M   |     |     | 47.6 |     |        | 31.4 | 21.0    |
WebServices,MicrosoftAzure).ToavoidInternetbeingthebottle- L 100.0
neck,wetake2approaches.(1)Werepeatedlyruntheexperiment
Global
|     |     |     |     |     |     | T+M+C |     | 27.2 |     | 19.2 | ⇓19.2 | 16.3 | 10.7 7.4 |
| --- | --- | --- | --- | --- | --- | ----- | --- | ---- | --- | ---- | ----- | ---- | -------- |
sets.(2)WeshuffletheUE-VMcombinationineachiterationtoen-
|     |     |     |     |     |     | L+M+C |     | 35.1 |     |     | 27.9 | 13.8 | 11.9 11.3 |
| --- | --- | --- | --- | --- | --- | ----- | --- | ---- | --- | --- | ---- | ---- | --------- |
surenodevice-sideorserver-sideissuesaffecttheexperiment,and T+M 35.9 28.1 25.1 10.9
additionallytoreducetheimpactofInternetbeingthebottleneck. L+M 58.5 22.8 18.7
Fig.21showsarepresentativerunofthisexperimentandreports L 100.0
thethroughputperceivedby𝑈𝐸 1–thedevicethatranfortheen- 0 20 40 60 80 100
tire4-minutelongduration.Inthefirstminutewhen𝑈𝐸 1’siPerf FeatureImportance(in%)
sessionwasrunningalone,weseegreatthroughputperformance
Figure22:FeatureImportanceusingGDBT.
| ofmorethan1.5Gbps.However,assoonas𝑈𝐸             |     |     | 2starteditssession, |     |      |     |     |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | ------------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| 𝑈𝐸 1’sthroughputnearlyhalved.Althoughnotshown,𝑈𝐸 |     |     |                     |     | also |     |     |     |     |     |     |     |     |
2
| experiencedsimilarthroughputasthatseenon𝑈𝐸 |     |     |     | 1.Sincetheseex- |     |     |     |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
area.TheobservationsmadeforIndoorareaalsoholdtrueforthe
perimentsweredoneduringlatenighthours,webelievetherewas Outdoorarea:(i)Geolocationaloneisinsufficienttocharacterize&
littletonoimpactonourexperimentsbyotherpassengersinthe predict5Gthroughput,butitstillremainsakeyfactor;(ii)Along
airportwhomightalsopotentiallybeusing5Gserviceinthisarea. withgeolocation,accountingformobility-relatedfactorsdecreases
| WeseesimilarbehaviorwhentheiPerfsessionsof𝑈𝐸 |     |     |     |     | 3and𝑈𝐸 |                                                      |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | ------ | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                                              |     |     |     |     | 4      | variationin5Gthroughputandimprovesitspredictability. |     |     |     |     |     |     |     |
started.ThisexperimenthighlightsanotherUE-sidefactorimpact-
| ing5Gthroughputwhichpracticallyreflectsa“dynamic” |     |     |     |     | factoror |     |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
A.2 FeatureImportance
thetime-of-dayeffect.Sincewedidnothavetheinformationonthe
UsingGDBT’sabilitytoreportglobalfeatureimportance,Fig.22
numberofusersactivelyservedbydifferent5Gtowersatacertain
showsthefeatureimportancescorein5Gthroughputprediction.
time,wecouldnotaccountforthisfactorinthispaper.However,
Thisscoreisavaluebetween0and100%wherescoresofallfeatures
duetotheexpandablenatureoffeaturegroupsinLumos5G,we
believe5Gcarrierscanextendandadaptthefeaturegroupsand sumupto100%.Wemakethefollowingkeyobservations:(1)In
general,thereisnosinglefeaturethatdominatesthethroughput
usethenumberofsubscribersconnectedtoa5Gpanelasanother
predictionproblemin5G.Forinstance,inthecaseofT+M+C,wesee
inputfeaturetofurtherimprove5Gthroughputpredictioninreal
connectionstatus(RadioType/Strength),UE-Panelmobilityangle,
deployments.
UE-Paneldistance,UE-Panelpositionalangle,andUE’smoving
A.1.5 StatisticalAnalysisforIntersectionArea. SimilartoTable4 speedallshowsignificantimportanceinpredictingthethroughput.
whichrepresentedtheIndoor/Airportareainmaintext,Table10 Thisobservationisadditionalevidencethataccountingforinterplay
summarizesthestatisticalanalysisoftheOutdoor(Intersection) betweendifferenttypesoffeaturesyieldsbetterperformancethan
192

IMC’20,October27–29,2020,VirtualEvent,USA ArvindNarayanan,EmanRamadan,RishabhMehta,XinyueHu,etal.
onlyconsideringlocation-basedfeatures.(2)Itisalsointerestingto
findthattheperformanceofbothL+MandT+Mfeaturegroupsare
comparabletoeachother.Whenconsideredwithinasingleregion,
thisobservationisintuitiveasbothL+MandT+Marethesame,itis
justthattheformer’sfeaturesarefromtheUE’sperspectivewhile
thelatterispurelyfromthe5Gpanel’sperspective.
A.3 PerformanceImprovementofLumos5G
OverExistingBaselines
1.0
0.5
0.0
L L+M+C
Intersection
.gvAdethgieW
erocS1-F
A.4 4Gv/s.5GThroughputPrediction
In3G/4G,locationaloneisknowntobeusefulforpredictingcel-
lularperformance[43,56].Tofurtherinvestigate,weconstruct
adatasetbyholdingtwo5Gsmartphonesside-by-side,onecon-
nectedto4Gnetworkandtheotherto5G,andwalkthe1300m
loopmentionedearlierforover30timesspanningacrossmultiple
days,andlogtheperceivedthroughputtraces.Wethenapplyex-
istingapproachessuchasKNNclassifier,OK[26],RF[20]which
areknowntoworkwellfor4Gthroughputestimationon5Gtraces.
Resultsshowthatthemeanabsoluteerror(MAE)on4Gtracesis
about[29.01,69.13,25.94]MbpsforKNN,OKandRF,respectively, OK
KNN whilethesameapproacheson5GtracesshowtheMAEtobe10×
RF higher–[325.95,625.83,339.57]Mbps,respectively.Theseresults
GDBT
exemplifiesthatwhileexistingmodelsworkwellforpredicting Seq2Seq
L L+M+C L L+M+C
Airport Loop 4Gthroughput,butareunabletopredict5Gthroughput.Thisis
becausesuch methods are unableto account for thesensitivity
Figure 23: Performance Comparison with existing models
ofmmWave-based5Gtotheenvironment–asmallperturbation
onIntersection,Airport&LoopAreas.
(e.g.,deviceorientation,movingdirection,movingspeed)affects5G
InFig.23,wecomparetheperformanceofourmodelstoexisting performanceasdiscussedearlierin§4.Thus,geolocationaloneis
approachesindifferentareasusingfeaturegroups.Approachesus- infeasibletoestimatemmWavebased5Gperformanceasshownin
ingnaivelocation-basedmodels(L)andspatialinterpolationmeth- §6.Inthispaper,weproposeLumos5Gframeworkthatgeneralizes
ods(OK)performpoorlycomparedtoourmodelswhichaccountfor theclassicallocation-basedcellularperformancepredictioninto
mobilityandconnectioninformation.Ourmodelsachieve16%to context-awarepredictionproblem.Theframeworkshowsthatin
113%higherw-avgF1thanpure-locationbasedKrigingmethod,and future,adatadrivenmodelcouldpotentiallyuseawiderangeof
achieve5%to88%higherw-avgF1thanpure-locationbasedKNN contextualandenvironmentaldatasuchaslocation,time,mobility
andRFmodels.Thisshowstheimportanceofmobilityandcon- level,movingorientation,trafficinformation, etc. tomodeland
nectionfeaturesfor5Gthroughputprediction.Ourresultsclearly predict5G(allbands)+LTE+otherlowerbandperformanceto
indicatethesuperiorityofbothSeq2SeqandGDBTmodelsover accountforseveralchallengesfacedbymmWave.
existingthroughputpredictionmethods.
193