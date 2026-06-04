An End-to-End Pipeline Perspective on Video Streaming in
Best-Effort Networks: A Survey and Tutorial
LEONARDOPERONI,UC3M,Leganes,Spain
SERGEYGORINSKY,IMDEANetworksInstitute,Leganes,Spain
RemainingadominantforceinInternettraffic,videostreamingcaptivatesendusers,serviceproviders,and
researchers.Thisarticletakesapragmaticapproachtoreviewingrecentadvancesinthefieldbyfocusing
ontheprevalentstreamingparadigmthatinvolvesdeliveringlong-formtwo-dimensionalvideosoverthe
best-effortInternetwithclient-sideadaptivebitrate(ABR)algorithmsandassistancefromcontentdelivery
networks(CDNs).Toenhanceaccessibility,wesupplementthesurveywithtutorialmaterial.Unlikeexisting
surveysthatofferfragmentedviews,ourworkprovidesaholisticperspectiveontheentireend-to-endstream-
ingpipeline,fromvideocapturebyacamera-equippeddevicetoplaybackbytheenduser.Ournovelper-
spectivecoverstheingestion,processing,anddistributionstagesofthepipelineandaddresseskeychallenges
suchasvideocompression,upload,transcoding,ABRalgorithms,CDNsupport,andqualityofexperience.
Wereviewover200papersandclassifystreamingdesignsbyproblem-solvingmethodology,whetherbased
onintuition,theory,ormachinelearning.Thesurveyfurtherrefinesthesemethodology-basedcategoriesand
characterizeseachdesignbyadditionaltraitssuchascompatiblecodecs.Weconnectthereviewedresearch
toreal-worldapplicationsbydiscussingthepracticesofcommercialstreamingplatforms.Finally,thesurvey
highlightsprominentcurrenttrendsandoutlinesfuturedirectionsinvideostreaming.
CCSConcepts:•Generalandreference→Surveysandoverviews;•Networks→Applicationlayer
protocols;In-networkprocessing;•Informationsystems→Multimediastreaming;•Computing
methodologies→Machinelearning;
AdditionalKeyWordsandPhrases:Videostreaming,end-to-endpipeline,ingestion,processing,distribution,
problem-solvingmethodology,intuition,theory,machinelearning,coding,adaptivebitratealgorithm,con-
tentdeliverynetwork,qualityofexperience
ACMReferenceFormat:
Leonardo Peroni and Sergey Gorinsky. 2025. An End-to-End Pipeline Perspective on Video Streaming in
Best-EffortNetworks:ASurveyandTutorial.ACMComput.Surv.57,12,Article322(July2025),47pages.
https://doi.org/10.1145/3742472
The research was supported in part by project PID2022-140560OB-I00 (DRONAC), funded by MICIU/AEI/10.13039/
501100011033,ERDF,andEU.
Authors’ Contact Information: Leonardo Peroni, UC3M, Leganes, Madrid, Spain; e-mail: leonardo.peroni@imdea.org;
SergeyGorinsky,IMDEANetworksInstitute,Leganes,Madrid,Spain;e-mail:sergey.gorinsky@imdea.org.
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalorclassroomuseisgrantedwithoutfee
providedthatcopiesarenotmadeordistributedforprofitorcommercialadvantageandthatcopiesbearthisnoticeand
thefullcitationonthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthantheauthor(s)mustbe
honored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,topostonserversortoredistributetolists,
requirespriorspecificpermissionand/orafee.Requestpermissionsfrompermissions@acm.org.
©2025Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
ACM0360-0300/2025/07-ART322
https://doi.org/10.1145/3742472
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:2 L.PeroniandS.Gorinsky
1 Introduction
Video streaming fuels dramatic Internet traffic growth and continues to expand. Video traffic
quadruplesbetween2017and2022,increasingitsshareoftotalInternettrafficfrom75%to82%,
while live streaming traffic rises 15-fold [37]. Streaming time grows significantly, with a 90% in-
creaseinAsiaanda14%globalrisebetween2021and2022[38].
Streamingoperatesinaneconomicallydiverseecosystem.Toboostsubscriptionsandrevenue,
streamingplatformsenhancethequalityofexperience(QoE)forusers.Contentproviders
(CPs)supplyvideos,whilecontentdeliverynetworks(CDNs)distributethemwithlowlatency,
minimizingcostsandmaintaininghighcachehitrates.Internetserviceproviders(ISPs)offer
networkconnectivity,characterizedbyqualityofservice(QoS)metrics.Entitiesoftenplaymul-
tipleroles,andtheirrelationshipsevolvecontinuously.
The technological landscape of video streaming is also heterogeneous and evolving. Major
streamingplatformstypicallyexploitthehypertexttransferprotocol(HTTP)andscalablydis-
tribute video content to global audiences via CDN-assisted HTTP adaptive streaming (HAS)
whereclient-sideadaptivebitrate(ABR) algorithmstacklethediversityandvariabilityofnet-
workconnectivitybetweenserversandclients.Ontheotherhand,interactivevideoapplications
intheirreal-timecommunicationscommonlyturntopeer-to-peer(P2P)technologiesandincor-
poratetheirowncongestioncontrol(CC)algorithmstodealwithdynamicnetworkconditions.
Even within the HAS paradigm, short-form and 360-degree videos employ somewhat different
streaming techniques than long-form two-dimensional (2D) videos. Software-defined net-
working(SDN)andnameddatanetworking(NDN)representenhancementsofthecurrentIn-
ternetarchitecturethatintroducesignificantnewopportunitiesandchallengesforvideostreaming.
AppendicesAandBexpandallmentionedacronymsandofferaglossaryofkeyterms,respectively.
ThissurveyprovidesanextensiveoverviewofrecentresearchonHASof2Dvideosoverbest-
effortnetworkswithclient-sideABRalgorithms,whichconstitutesthemajorparadigmforvideo
streamingonthecurrentInternet.Weprimarilyfocusonlong-form2Dvideos,eventhoughmany
oftherevieweddesignsarealsorelevanttoshort-formand360-degreevideos.Despiterestricting
thescope,oursurveycoversavastamountofmaterialbyreviewingmorethan200papers.The
surveyalsoincludesessentialtutorialstomakethecontentaccessible,especiallyfornewcomers.
Amajornoveltyofourapproachisinsurveyingthe2DHASprocessfromtheperspectiveof
itsend-to-endpipeline.Figure1depictsthispipelineasconsistingofingestion,processing,and
distribution stages. At ingestion, a camera-equipped device captures raw footage, encodes it to
reduce size, and uploads the video to a media server. The processing stage includes video stor-
age,segmentation,andtranscodingtocreatemultiplerepresentationsofthevideoinaccordance
withanencodingladder.Duringdistribution,aCDNscalablydisseminatesthevideotohetero-
geneoususerdevicesfordecodingandplayback.Unlikeearliersurveysthatfocusonindividual
stagesortasks,weofferanintegratedunderstandingoftheentirepipeline.Whilesometechniques
andmetricsspanmultiplestages,oursurveyhighlightstheseinterconnectionstofurtherpromote
theholisticunderstanding.
WeintroduceanewtaxonomyinSection3andapplyitlatertostructureourdiscussionofrecent
works.Thestageoftheend-to-endstreamingpipelineconstitutesthetoplevelofthetaxonomy,
differentiatingbetweentheingestion(Section4),processing(Section5),anddistribution(Section6)
stages.Atthedistributionstage,weseparatelyconsideritsABR,CDN,andQoEaspects.Thelower
classificationlevelscategorizeeachworkaccordingtoitsmethodologyfortacklingtheproblem.
Eachleafcategorylistsitsdesignsinchronologicalorder.Inadditiontoclassifyingtheworks,we
also describe each of them in terms of various characteristics, such as the codec used. After the
thoroughreviewoftheresearchworks,wediscussreal-worldapplications(Section7),trends,and
futuredirections(Section8).
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:3
Fig.1. Theend-to-endstreamingpipelineanditsingestion,processing,anddistributionstages.
Oursurveymakesthefollowingmaincontributions:
—We present an extensive review of recent research on video streaming and, in particular,
CDN-assistedHASoflong-form2Dvideosoverthebest-effortInternetwithclient-sideABR
algorithms.
—We cover the topic from the novel perspective of the end-to-end streaming pipeline and
discussmorethan200papersaccordingtoanewtaxonomy.Withineachofthepipeline’s
ingestion, processing, and distribution stages, the scheme organizes the discussed works
basedontheirproblem-solvingmethodology.
—Beyond the literature review, we report on real-world applications, trends, and promising
futuredirections.
2 Background
2.1 End-to-EndStreamingPipeline
The end-to-end streaming pipeline starts at the ingestion stage with the capture of raw video
byacamera-equippeddevice,withacodecapplyingspatialandtemporalcompressiontotheraw
footageforreducingthevideosize,andsubsequentuploadoftheencodedvideoovertheInternet
toamediaserver.Thisstageattractssignificantresearchefforts,drivenbythegrowinginterest
invideoanalyticsandlivestreaming.Ingestion-stagedesignsaimtoimproveanalyticsaccuracy,
encodingcomplexity,videoquality,bandwidthutilization,anduploadlatency,whichisespecially
importantforinteractiveapplications.
Theprocessingstage,whichprimarilyinvolvesinternaloperationswithinthemediaserver,
handlesthestorageandtransformationofingestedvideo.Transformationtasks,suchasvideoseg-
mentationandtranscoding,enablethepipelinetomanageheterogeneityinnetworkconnectivity
anddevicecapabilities.Videosegmentationdividesthevideointosmallerchunks,whiletranscod-
ing converts these chunks into multiple representations with different resolutions, bitrates, and
framerates.Numerousresearcheffortstargettheintegrationoftranscodingwithtasksatthein-
gestionanddistributionstagestooptimizepipelineperformance.
Thedistributionstagehandlesvideodeliveryfromthemediaservertoauserdevice,which
decodesandplaysbackthecontent.InadditiontoISPsprovidingnetworkconnectivity,thisstage
involves CDNs that disseminate video from their edge servers to user devices with low latency
and high QoE. To address the heterogeneity of user devices and variable network conditions, a
media player on the user device runs an ABR algorithm. Among the components of the end-to-
endpipeline,ABR,QoE,andCDNaspectsattractthemostresearchefforts.
QoEmodelsexpressusers’subjectiveexperienceasafunctionofmeasurableinfluencefac-
tors(IFs)likestalldurationandvideoquality.Theyrelyonsubjectivetestinganduserexperience
design.Networkengineeringensureslowlatencyandhighbitrate,whichQoEmodelsaccountfor
directlyorthroughotherIFs.Datascienceenhancestheirpredictivepowerwithlearning-based
techniques.
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:4 L.PeroniandS.Gorinsky
2.2 2DStreamingModes
Videoondemand(VoD) isthemostdominantofthetwostreamingmodesconsideredinthis
survey.Thismodecloselyalignswithreal-worldapplicationsofmajorstreamingplatforms,such
as Netflix, and specifically involves serving pre-stored video from a media server. The reliance
onthemediaservereffectivelydecouplestheingestionanddistributionstages:whiledistribution
operatesinrealtime,ingestionoccursbeforehandunderlessstringentlatencyconstraints.Asa
result,VoDemploysdifferentcommunicationdesignsattheingestionanddistributionstages.
Livestreamingreferstoanincreasinglypopularvariantthatrequiresreal-timeoperationof
theentirepipelinefromvideocapturetoplayback."Real-time"isarelativenotionwhereacceptable
latencydependsontheparticularapplication.ThissurveyconsidersHAS-basedlivestreamingfor
applications such as live broadcasting. HAS improves its support for live streaming through a
varietyoftechniques,suchasreducingchunkduration,deliveringachunkinmultiplefragments,
andprefetchingexpectedchunksbytheCDNedgeserver.
2.3 StreamingProtocols
Thecurrentstreamingecosysteminvolvesalargenumberofprotocolswiththeirpopularityvary-
ingacrossthepipelinestages.Apple’sHTTPlivestreaming(HLS)constitutesthemostpopular
protocolduetoitsdominanceatthedistributionstage.ThemaincompetitorsofHLSatthisstage
aredynamicadaptivestreamingoverHTTP(DASH)[173],whichisanopenstandardmain-
tained by the moving picture experts group (MPEG). The real-time messaging protocol
(RTMP)maintainsitsprominenceastheleadinguploadprotocolattheingestionstage.Webreal-
timecommunication(WebRTC)isanewerprotocolchallengingthedominantroleofRTMPat
thisstage.WhereasRTMPusesthetransmissioncontrolprotocol(TCP)asitstransportproto-
col,bothWebRTCreliesinsteadontheuserdatagramprotocol(UDP)tosupportlow-latency
upload.Ref.[178]presentstheusageofstreamingprotocolsby391globalbroadcastersinsports,
radio,gaming,andotherindustries.
2.4 PreviousSurveys
Alargenumberofearliersurveystackletheimportanttopicofvideostreaming.Duetothecom-
plexity of the end-to-end streaming pipeline, these surveys often focus on individual stages or
specificelementswithinastage.Forinstance,[19,109,162]concentrateonABRalgorithmsatthe
distributionstage.Refs.[13,97,211]addressQoEinvideostreamingandemphasizeQoEmodel-
ing,while[12]dealswithQoEmanagementinnovelnetworkarchitectures.Ref.[2]surveysvideo
streamingovermultiplewirelesspaths.Whereas[216]discussesCDNsupportforvideostreaming
andothertrafficclasses,[117]coverscloud-basedvideostreaming.Incontrasttotheprevioussur-
veys,ourworkoffersaholisticoverviewofvideostreamingacrosstheentireend-to-endpipeline.
InadditiontoCDNsupport,QoE,andABRalgorithmsatthedistributionstage,oursurveyalso
reportsonadvancesinvideostreamingattheingestionandprocessingstages.Besides,weoffer
anup-to-dateperspectivebyhighlightingmorerecentresearchfindingsinthefield.
2.5 RelatedTopicsBeyondtheSurveyScope
While this survey offers a new end-to-end pipeline perspective on HAS of long-form 2D videos
overthebest-effortnetworks,therichareaofvideostreamingcontainsrelatedtopicsoutsidethe
surveyscope.Inparticular,wedonotreportonP2PsolutionsexemplifiedbyWebRTC[125,172]
whereacamera-equippeddevicetransmitsvideodirectlytoauserdevicewithoutanyassistance
fromamediaserver.BydeviatingfromtheHASpipelineandrelyingonUDPinsteadofTCP,such
P2P solutions seek to provide ultra-low end-to-end latency for effective support of interactive
applications, such as video conferencing [92]. Because UDP does not provide CC, these P2P
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:5
streamingsystemsimplementtheirownCCalgorithms.Forinstance,WebRTCemploysGoogle
congestioncontrol(GCC)[29]asitsdefaultCCalgorithm.AlthoughaP2Pstreamingsystemis
abletoportfromTCPanexistingCCalgorithm,suchasCUBIC[75]orbottleneckbandwidth
and round-trip propagation time (BBR) [28], these general-purpose CC algorithms do not
caterspecificallyfortheneedsofvideostreaming.Theworkonstreaming-specificCCalgorithms
includesself-clockedrateadaptationformultimedia(SCReAM)[94]andnetwork-assisted
dynamicadaptation(NADA)[214].
Compared to long-form videos, streaming of short-form videos differs significantly in its re-
quirements and solutions. With a common duration of 15 to 60 s, depending on the streaming
platform,ashort-formvideorequiresmuchlessstorageandbandwidth,makingitfeasibletoim-
plementtechniquessuchasprefetchingtheentirevideo[217],relyingonprogressivedownload
instead of HAS [76], using equal-size rather than equal-duration chunks [121], simplifying the
ABRalgorithm,oreventransmittingtheentirevideoatasinglebitrate[71].Withastrongerem-
phasis on user engagement and interaction, short-form streaming designs explicitly account for
user behavior, such as screen scrolling [206]. Short-form video streaming and recommen-
dation(SSR)[160]representssolutionsthatjointlyoptimizevideorecommendationandbitrate
adaptation.Inshort,short-formstreamingisavasttopicdeservingaseparatesurvey.
360-degreevideostreamingalsofacesdistinctchallenges.Todeliverimmersiveexperiencesin
virtual reality (VR), augmented reality (AR), and mixed reality (MR), 360-degree videos
requirespecializedequipmentforcaptureandplayback.Thisincludescameraarrays,omnidirec-
tionalcameras,curvedscreens,andhead-mounteddisplays(HMDs).Thecreationandpresen-
tationofseamlesspanoramicvideosinvolveadvancedstitchingandprojectionmethods[212].To
managethehigherstorage,processing,andbandwidthrequirements,360-degreevideostreaming
employstile-based[65]andviewport-based[77]techniques,whichlieoutsideoursurveyscope.
Future Internet architectures, such as SDN and NDN, offer radically new opportunities for
videostreamingandotherapplications[147].Specifically,in-transitcomputing[102]promises
to make streaming more efficient by leveraging the processing capabilities of network devices
alongthedeliverypath.OurarticlereviewsvideostreamingdesignswithinthecurrentInternet
architecture.
3 Taxonomy
Figure2illustratesthetaxonomyusedinoursurvey.Figure2(a)presentsthetoplevelofthehierar-
chy,whichclassifiesstreamingdesignsbasedontheiroperationattheingestion,processing,ordis-
tributionstageofthepipeline.Thelowerlevelsfurtherclassifydesignsbasedontheirsolution
methodology. Figure 2(b)–(d) provides these methodology-based taxonomies for the ingestion,
processing,anddistributionstages,respectively,withSections4–6surveyingthecorrespondingre-
centresults.Theclassificationschemeincludesbranchesofvaryingbreadthanddepthtoreflectthe
complexityanddiversityofthereviewedworks.Forexample,Figure2(d)categorizesdistribution-
stagedesignsintoABR,CDN,andQoE groups.Eachfinalcategorylistsworksinchronological
orderanddescribesthembasedonadditionalcharacteristics.WhileSection3.1elaborateson
ourmethodology-basedclassifications,Section3.2discussestheseadditionalcharacteristics.
3.1 Methodology-BasedClassifications
Ourmethodology-basedtaxonomiesdifferentiatedesignsaccordingtotheirrelianceonintuition,
theory,ormachinelearning(ML),asdiscussedbelow.
3.1.1 Intuition-Based Methods. In an intuition-based method, a human expert leverages do-
mainknowledgeandtrial-and-errorexperimentationtodevelopasimpleheuristicsolution.Itis
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:6 L.PeroniandS.Gorinsky
Fig.2. Hierarchicaltaxonomyofthesurveyedstreamingdesigns.
commonforaninformalintuition-basedmethodtoundergosubsequentformalanalysis,supplying
insights into the underlying principles. An intuition-based heuristic might prove broadly appli-
cable beyond the initial problem. A notable example is the additive-increase multiplicative-
decrease(AIMD)algorithm[35],originallydesignedfornetworkCCandnowemployedwidely
invideostreamingandotherfields.Forintuition-basedABRalgorithms,weincludeadeeperlevel
of classification that considers buffer-centric, throughput-centric, and hybrid categories,
where ABR decisions rely on playback-buffer occupancy, network-bandwidth estimate, or both,
respectively.
3.1.2 Theory-BasedMethods. Atheory-basedmethodabstractsspecificdetailstoformulatea
problem within a general formal theory and systematically applies principles of rational logic
to derive a solution, often with guarantees of correctness and performance. In comparison to
intuition-based methods, the derived solution might be less intuitive or even counterintuitive.
Mixed-integerprogramming(MIP)constitutesaprominenttheory-basedmethodforformulat-
ingandsolvingoptimizationproblems[1].Control-theoretictechniques,suchasmodelpredic-
tivecontrol(MPC),proportional-integral-derivative(PID)controllers[63],andLyapunov
optimization(LO)[141],commonlyunderpinsolutionsinvideostreaming.Bayesianoptimiza-
tion (BO) [56] represents a popular statistical optimization method. Our classification utilizes
theseMIP,MPC,PID,LO,andBOcategoriescommensuratelywiththediversityofreviewedworks:
MIPandMPCattheingestionstage,onlyMIPattheprocessingstage,andallfivecategoriesfor
ABRalgorithmsatthedistributionstage.Thesixthcategory,calledother,containstheory-based
techniquesappliedlessfrequentlyinvideostreaming,suchasdynamicprogramming(DP)[15].
3.1.3 ML-BasedMethods. MLtrainsmodelsonsampledatatogeneralizeandproduceaccurate
predictionsonnewdata,ratherthanfollowingexplicitinstructions.ThefocusofMLisonlearning
generalizable patterns and minimizing error on unseen samples, distinguishing it from theory-
basedmethodsthatoptimizesolelyforthegivendata.Whilepromisingbetterperformance,ML
raisesconcernsabouthigheroverheadandpoorerexplainability.WeclassifyMLtechniquesinto
four categories based on their model training methodology as reinforcement learning (RL),
imitationlearning(IL),supervisedlearning(SL),andunsupervisedlearning(UL)[177].At
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:7
Fig.3. Theingestionstageoftheend-to-endVoDstreamingpipeline.
thedistributionstage,ourclassificationschemefurtherdividesRLintoasynchronousadvantage
actorcritic(A3C),advantageactorcritic(A2C),actorcritic(AC)[69],andothermethods.
Attheprocessingandingestionstages,thereviewedworksemployRL,SL,orUL.
3.2 AdditionalDesignCharacteristics
InadditiontoapplyingthetaxonomyfromFigure2,wedescribeeachrevieweddesignusingaset
ofextracharacteristics,whichvarybydesigncategory.Foreverydesign,wespecifyitscoretech-
nique,afree-formcharacteristicofthedesign’smaindistinguishingtrait,andcodeccompatibility.
Forexample,whendiscussingML-baseddesigns,thecoretechniquecharacterizestheusedmodel,
such as a decision tree (DT), random forest (RF), naive Bayes (NB), multilayer percep-
tron(MLP),convolutionneuralnetwork(CNN),generativeadversarialnetwork(GAN),
autoencoder(AE),generativepre-trainedtransformer(GPT),oranotherdeepneuralnet-
work(DNN)[8,155].
3.3 MainTakeaways
The hierarchical taxonomy classifies streaming designs by pipeline stage (ingestion, processing,
distribution),withthedistributionstageadditionallydividedintoABR,CDN,andQoEcategories,
andbysolutionmethodology(intuition,theory,ML).Intuition-basedmethodsrelyonheuristics
anddomainexpertise,theory-basedmethodsuseformallogicwithperformanceguarantees,and
ML-based methods learn from data. Additional pipeline-wide and stage-specific characteristics
provide further insights. With varying depth and breadth, this taxonomy captures the diversity
andcomplexityofstreamingresearch.
4 IngestionStage
4.1 Background
Weproceedbyprovidingadditionalbackgroundoningestion,withFigure3illustratingthisstage
forVoDwithaflowchart.Thestagestartswiththecamera-equippeddevicecapturingrawfootage.
Then,thedeviceappliespre-processing,suchascolorcorrectionandbalancing,andencodesthe
videowithacodec.Afterpost-processing,suchasartifactfiltering,theingestionstageprovidesop-
tionalsupportforvideoanalytics,e.g.,objectdetectionandrecognition.Thestageconcludeswith
uploadingtheencodedvideotothemediaserver.Hostingthemediaserverincloudinfrastructure
isincreasinglycommoninbothVoDandlivestreaming[143].
4.1.1 VideoEncoding. Compression,whichmightoccurduringbothingestionandprocessing,
iseitherlossyorlossless.Lossycompressionreducesstorageandbandwidthneedsbydiscarding
some information while maintaining high content quality. Spatial compression removes redun-
dancy within a frame, e.g., by using discrete cosine transform (DCT) and quantization, and
encodestheresulttoreducethebitcount.Temporalcompression,whichismorecomputationally
demanding,reducesredundancyacrossmultipleframesthroughmotionestimationandcompen-
sation.Thecodecorpost-processingappliesfilteringtocorrectblockboundaries,mosquitonoise,
ringing,andotherartifactsintroducedbylossycompression[95].
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:8 L.PeroniandS.Gorinsky
A compressed video involves different frame types. Intra-frames (I-frames), resulting from
spatial compression, serve as reference points, prevent error accumulation, and facilitate video
search.Predictiveframes(P-frames)usemotioncompensationbasedonpreviousframes,while
bipredictive frames (B-frames) leverage both preceding and following frames. A group of
pictures(GOP)referstoasequencestartingwithanI-frame,followedbyP-framesandB-frames.
Asinglecontainerformatfilestorestheencodedvideoalongwithaudio,synchronization,subtitle,
andothermetadata.
Videoencodingiscomputationallyintensive,withinnovationsaimedprimarilyatfasterprocess-
ing.Alongsidealgorithmicadvances,hardware-acceleratedencodingbecomesmoreprevalentand
offloads tasks to specialized components. Examples include Nvidia encoder (NVENC), which
shiftsvideoencodingfromthecentralprocessingunittothegraphicsprocessingunit(GPU),
andvideocodingengine(VCE),aGPU-integratedunitdedicatedtovideocompression.
Encodingparameters:Acodecbalancestradeoffsbetweenvideoquality,latency,andotherper-
formancemetricsthroughvariousencodingparameters.Higherresolutionsenhanceimagesharp-
ness but demand more storage and bandwidth. For optimal results, the video resolution should
match the display resolution. Frame rates typically range from 24 to 60 fps. Some applications,
suchasgaming,mayrequireupto120fps[128].TheGOPstructuredefinesthenumberofframes
per GOP and the spacing between keyframes (I-frames and P-frames). Larger GOPs with more
B-framesreducevideosizebutincreaseprocessingcomplexityandlatency.
Prominentcodecs:Advancedvideocoding(AVC)orH.264isoneofthemostwidelyused
compressionstandards[44].Itemploysmacroblocksandmotioncompensationforefficientvideo
encoding.KeyfeaturesincludeintegerDCT,variableblock-sizesegmentation,multi-frameinter-
frameprediction,andin-loopdeblockingfiltering.H.264remainsthemostpopularcodecdueto
itsbroadsupportacrosscommercialdevices[23].
High efficiency video coding (HEVC) or H.265, a successor to H.264, achieves up to 50%
better compression efficiency while maintaining the same video quality. It replaces 16×16 mac-
roblocks with coding tree units (CTUs) up to 64×64 in size and uses both integer DCT and
discrete sine transform (DST). HEVC simplifies deblocking filtering, making it easier to par-
allelize [174]. Despite superior performance, adoption is slow due to royalty issues and limited
browsersupport.
VP9,anopenroyalty-freecodecdevelopedbyGoogleandutilizedonYouTube,employs64×64
superblockswithquadtree(QT) partitioningandintra-framepredictionwithsixobliquedirec-
tions for linear extrapolation of pixels. While less efficient in compression than H.265 [68], VP9
reducesencodinglatencyandenjoysbroadbrowsersupport.
AOMediavideo1(AV1),aroyalty-freesuccessortoVP9,diversifiescodingoptionsforbetter
videoinputhandlingandusesrectangularDCTs,asymmetricDSTs,andsuperblocksupto128×128.
Italsoemploysin-loopandloop-restorationfilters.WhileAV1incurshighercomputationalcom-
plexitytoimprovecompressionefficiencyoverH.265[33],subjectivetestsofvideoqualityshow
minimaldifferences[101].
Scalable video coding (SVC) extends H.264 by enabling layered encoding into multiple
streams, where enhancement layers build upon the base layer. These layers improve the frame
rate,resolution,bitrate,orcombinationsthereof[164].Althoughlessefficientincompressionthan
H.264,SVCbettermanageshighlyvariablebandwidth[53].
Versatile video coding (VVC) or H.266 [25], adopted in 2020, is a successor to H.265 that
supportslosslessandsubjectivelylosslesscompression.Itaimstosupportawiderangeofvideo
applications through layered coding and flexible bitstream handling. VVC offers significant im-
provementsincompressionefficiencyoverH.265andrequiresmorecomputationalresources[181].
TheroyaltysituationforVVCisstilluncertain.
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:9
Essentialvideocoding(EVC)[36],introducedin2020aswell,featuresinnovationssuchasa
binary-ternarytreestructure,splitunitcodingorder,andadaptiveloopfilter.Itimprovescompres-
sionefficiencybyabout30%overH.265,albeitwithfivetimesthecomputationalcomplexity[67].
EVCisavailableinbothroyalty-basedandroyalty-freeprofiles.
Lowcomplexityenhancementvideocoding(LCEVC)[133]constitutesanovelapproach
tovideoenhancement.LCEVCaddsanenhancementlayertoabaselayerencodedwithadifferent
codec,withanobjectivetoreducebothencodinganddecodingcomplexity.
4.1.2 Perceptual Compression. Unlike codecs that reduce statistical redundancy, perceptual
videocompressionleveragespropertiesofthehumanvisualsystemtoreducethevideosizewith-
outcompromisingtheperceivedquality.Itidentifiesregionsofinterest(ROIs)asspatial,tem-
poral,orspatio-temporalareascriticalforperceptionandencodesROIslosslessly,whileapplying
strongercompressiontolesscriticalparts.Thisprocessinvolvestwophases:detectingROIswith
techniques ranging from user input to non-visual information [114], and ROI-aware encoding,
whichmighttakeplaceduringpre-processingoractualencoding[134].
4.1.3 SuperResolution(SR). SR[99]referstoacomputer-visiontaskthatreconstructshigh-
resolution (HR) images from low-resolution (LR) versions. In video streaming, SR reduces
network-bandwidthconsumptionbytransmittingLRframesandreconstructingHRvideoatthe
recipient.WhiletraditionalSRreliesonspatial-frequencysubstitutionandgeometrictechniques,
modern ML-based approaches employ GANs, CNNs, and other DNNs [189]. Despite improving
videoqualityandbandwidthefficiency,ML-basedSRtechniquesfacechallengessuchaspoorgen-
eralization,highparameterdimensionality,andbalancinginferenceaccuracywithspeed.
4.2 RecentResults
Recentworksattheingestionstagecommonlytackletaskssuchasvideoencoding,analytics,and
upload.Thesestudiesevaluatetheeffectivenessoftheirsolutionswithinthestageviametricsof
bandwidthutilization,encodingcomplexity,videoquality,analyticsaccuracy,uploadlatency,and
computationaloverhead.Additionally,somestudiesassessuserexperiencebymeansofQoEmod-
els.Toachievetheirgoals,therevieweddesignsexplorevariousapproaches,includingassistance
fromSR,transport-layersignals,andedgeservers.
This section, along with Table 1, organizes our discussion of the recent works according to
themethodology-basedclassificationspresentedinSection3.1:intuition,theory(MIP,MPC,and
other),andML(SLandUL).Inadditiontothecoretechniqueandcodeccharacteristicsexplained
in Section 3.2, Table 1 describes each ingestion-stage design based on five stage-specific binary
characteristics:(1)SRusage,(2)utilizationofawell-definedQoEmodelindesignorevaluation,
(3)relianceontransport-layersignals,(4)leverageofedgeinfrastructure,and(5)bandwidth-
efficiencyevaluationinthereviewedwork.
4.2.1 Intuition-BasedMethods. GuidedbymeasurementsofTCPuplinkthroughputinaradio
accessnetwork,[126]intuitivelyreducesthenumberofbitratelevelsintheencodingladderand
therebyconservesbandwidth.Thistechniquecombinesreal-timeandhistoricalthroughputdata,
usingtheformerforongoingsessionsandthelatteratthestartofsessionsorduringhandovers.
Ref. [190] proposes dynamic selection of the upload protocol by a mobile broadcasting applica-
tion. The application considers latency, join-time, goodput, and overhead metrics, picks one of
them,evaluatesthismetricinrealtime,andperiodicallydecideswhethertoswitchtoanotherup-
loadprotocol.Whilethismethodperformsaswellasthebestprotocolforeachindividualmetric,
theswitchingbetweenprotocolsincursundesirabledelay.Ref.[150]monitorstheaverageinter-
arrival time of video frames and dynamically adjusts the encoding rate on a camera-equipped
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

| 322:10 |     |     |     |     |     | L.PeroniandS.Gorinsky |     |     |
| ------ | --- | --- | --- | --- | --- | --------------------- | --- | --- |
Table1. DesignsattheIngestionStageoftheEnd-to-EndStreamingPipeline(uAbbreviatesUnspecified)
|     |     |     |     |     |     | Transport- | Edge | Bandwidth- |
| --- | --- | --- | --- | --- | --- | ---------- | ---- | ---------- |
Name[reference] Year Coretechnique Codec SR QoE layer infras- efficiency
|       | Method |                            |     |       | model |         |          |            |
| ----- | ------ | -------------------------- | --- | ----- | ----- | ------- | -------- | ---------- |
|       |        |                            |     |       |       | signals | tructure | evaluation |
|       |        |                            |     |       | ✘ ✘   | ✔       | ✘        | ✘          |
| [126] |        | 2015 dynamicencodingladder |     | H.264 |       |         |          |            |
switchbetween
| [190] |     | 2016 |     | u   | ✘ ✘ | ✘   | ✘   | ✘   |
| ----- | --- | ---- | --- | --- | --- | --- | --- | --- |
uploadprotocols
Intuition
|       |     | AIMD-basedencoding-rate |     |       | ✘ ✘ | ✘   | ✘   | ✘   |
| ----- | --- | ----------------------- | --- | ----- | --- | --- | --- | --- |
| [150] |     | 2017                    |     | H.264 |     |     |     |     |
control
zero-inference
| NeuroScaler[198] |     | 2022 |     | VP9 | ✔ ✘ | ✘   | ✘   | ✘   |
| ---------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
selectionofanchors
VP8,aVP9
| Vantage[161] |     | MIP 2019 regressionheuristic |     |     | ✘ ✔ | ✔   | ✘   | ✘   |
| ------------ | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
predecessor
| LiveSRVC[32] |     | MPC 2021                 | SR  | H.264 | ✔ ✔ | ✘   | ✘   | ✔   |
| ------------ | --- | ------------------------ | --- | ----- | --- | --- | --- | --- |
|              |     |                          |     |       | ✘ ✔ | ✘   | ✘   | ✘   |
| [167]        |     | 2017 DP,greedyheuristics |     | SVC   |     |     |     |     |
knapsack-likeproblem,
| CHN[148] |     | 2019 |     | u   | ✘ ✘ | ✔   | ✔   | ✘   |
| -------- | --- | ---- | --- | --- | --- | --- | --- | --- |
greedyroundingheuristic
Theory
| [31]         |     | Other2019 relaxation-basedheuristic |     | u     | ✘ ✔ | ✘   | ✔   | ✘   |
| ------------ | --- | ----------------------------------- | --- | ----- | --- | --- | --- | --- |
|              |     |                                     |     |       | ✘ ✘ | ✘   | ✘   | ✔   |
| DDS[47]      |     | 2020 adaptivefeedbackcontrol        |     | H.264 |     |     |     |     |
| LiveNAS[103] |     | 2020 concaveoptimization            |     | u     | ✔ ✘ | ✔   | ✘   | ✔   |
problem,gradientascent
|                  |     |                            |                 |               | ✘ ✘ | ✘   | ✘   | ✘   |
| ---------------- | --- | -------------------------- | --------------- | ------------- | --- | --- | --- | --- |
| [213]            |     | 2017                       | CNNs            | H.265-based   |     |     |     |     |
| [27]             |     | 2020                       | CNNs            | ROI-based     | ✘ ✘ | ✘   | ✘   | ✘   |
| CrowdSR[127]     |     | SL 2021                    | unspecifiedDNNs | u             | ✔ ✘ | ✘   | ✘   | ✘   |
| DIVA[193]        |     | 2021 AlexNetvariants(CNNs) |                 | H.264         | ✘ ✘ | ✘   | ✘   | ✔   |
|                  | ML  |                            |                 |               | ✘ ✘ | ✘   | ✘   | ✘   |
| MobileCodec[112] |     | 2022                       | CNNs            | MobileCodec   |     |     |     |     |
|                  |     |                            |                 |               | ✘ ✘ | ✘   | ✘   | ✘   |
| DeepFovea[98]    |     | 2019                       | WassersteinGAN  | DeepFovea     |     |     |     |     |
| Reducto[118]     |     | UL 2020 k-meansclustering  |                 | H.264         | ✘ ✘ | ✘   | ✘   | ✔   |
| [116]            |     | 2023                       | AE              | data-scalable | ✘ ✘ | ✘   | ✘   | ✘   |
mobile device via the AIMD algorithm. By increasing the average encoding rate and decreasing
thepacketloss,thealgorithmimprovesreal-timeupstreamingunderchangingnetworkconditions.
NeuroScaler[198]enhancesthescalabilityofSR-basedlivestreamingbyloweringbothoverhead
andencodingtimeofSR.Thedesignincludesanovelschedulerandenhanceroftheanchorframes
usedbySR.Theanchorschedulerleveragescodec-levelinformationtoselecttheanchorframes
inrealtimewithoutanyneuralinference.Theanchorenhancercomplementsavideocodecwith
asimpleimagecodecandemploysthelatterforcompressionoftheanchorframesonly.
4.2.2 Theory-BasedMethods. Vantage[161]referstoaMIP-basedapproachthattargetssocial
live streams and improves QoE for time-shifted viewers through frame retransmissions. When
bandwidthallows,itretransmitsearlierframesatahigherbitrate,enhancingtheexperiencefor
viewers watching with time shifts. Vantage employs MIP for retransmission scheduling. LiveS-
RVC [32]isanMPC-basedsolutionforlive-streamingestion,aiming todecreasebandwidthus-
ageandlatencyviaSR.ItcompressesI-framesatthecamerasideandtrainsanSRmodelonlineto
reconstructthemontheserver.Guidedbyestimateduplinkbandwidth,SRprocessingtime,and
accuracy,LiveSRVCusesMPCtoselecttheI-framecompressionratioandchunkbitrates.
Other theory-based ingestion works include [167], which, similar to Vantage, strives to max-
imize video quality in live streaming for multiple clients with heterogeneous upload latencies.
The design involves a series of algorithms that leverage a greedy low-complexity DP-based ap-
proach.Conversely,thecontentharvestnetwork(CHN) [148]achievesbothlowlatencyand
efficientbandwidthutilizationduringingestionbyemployingedgedevicesasrelaystodirecttraf-
fic from broadcasters to servers. To determine the path for each broadcaster, CHN employs two
strategiesondifferenttimescales.Whereasfindingagloballyoptimalpathisanondeterminis-
ticpolynomialtime(NP)andNP-hardproblem,acentralizedserverperiodicallysolvesitviaa
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:11
polynomial-timegreedyroundingalgorithm.Ref.[31]selectsboththeuploadserverandencoding
bitratetojointlymaximizethevideorateandminimizeend-to-endlatency.Itdevelopsalgorithms
forbothone-hop-overlayandfull-overlayarchitectures.Theone-hop-overlayalgorithmisanop-
timal polynomial-time solution. The paper proves NP-completeness of the full-overlay problem
andsolvesitwithanefficientheuristicsolutionbasedonconvexrelaxation.
DNN-driven streaming (DDS) [47] refers to a theory-based solution where the camera-
equipped device optimizes bandwidth usage across two streams to enhance inference accuracy
whileminimizingbandwidthconsumptioninanalyticsapplications.Thefirststreamtransmitslow-
qualityvideototheserver,whichidentifiesROIsforDNNinference.Thesecondstreamprovides
high-qualityvideoforthedetectedROIs,improvinginferenceaccuracywhilemanagingbandwidth
efficiently.DDSappliesaKalmanfiltertoestimatebasebandwidthandadjustsbandwidthusage
bytuningtheresolutionandquantizationparameter(QP).Withasimilarfocusoncameraup-
loads,LiveNAS[103]employsSRforhigh-qualitylivestreaming.Alongwiththelivevideo,the
camera-equippeddevicealsouploadshigh-qualityframepatches.Theserverutilizesthesepatches
to train a DNN for SR in real time. LiveNAS allocates upload bandwidth between the live video
andpatchesbymeansofgradientascenttomaximizebothvideoqualityandDNNaccuracy,while
minimizingoverheadforingestclients.
4.2.3 ML-BasedMethods. Refs.[27,213]presentSL-basedcodecsforperceptualcompression,
targeting improvements in coding efficiency. Compared to standard codecs, these designs in-
crease video quality and decrease storage requirements while decreasing the encoding speed.
Ref. [213] extends the H.265 codec by incorporating a hybrid compression algorithm that em-
ploys a CNN for spatial saliency and then extracts temporal saliency from motion information
in the compressed domain. Ref. [27] introduces an ROI codec that combines CNNs with an en-
tropy codec to achieve better encoding efficiency than previous ROI codecs, though its decod-
ing performance is less effective. CrowdSR [127] enhances live streaming from low-end de-
vices via SR-based video uploading. It periodically trains an SR model with high-quality video
patches from similar content broadcasters. CrowdSR outperforms existing counterparts in re-
gard to the peak signal-to-noise ratio (PSNR) [88] and structural similarity index mea-
sure(SSIM)[188].Incontrast,DIVA[193]improvesvideoanalyticsefficiencybyleveragingboth
camera-equippeddeviceandserver.Itprocessesonlykeyvideoframesonthecamera-equipped
devicetoavoidunnecessaryuploads.Utilizingthesparseanalyticaldata,theservertrainsCNNs,
specifically variants of AlexNet [108], and sends them back to the camera-equipped device to
identify I-frames for upload. This iterative approach enhances analytics performance and op-
erates 100 times faster than real-time video. Recent work on neural codecs includes Mobile-
Codec[112],whichadoptsaDNNarchitectureandSLtosupportefficientcodingformobilede-
vices.Itfeaturesaninter-framemodulewithfullyconvolutionaloperations,asymmetricaldesign
forfasterreal-timedecoding,andactivationquantizationwithsimulatedstraight-throughgradient
estimation.
Applying UL to perceptual compression, DeepFovea [98] proposes foveated coding that
strengthenscompressionforareasoutsidethefovea.ThecodecemploysaGANtoreconstructreal-
isticperipheralvideofromaminimalsetofframepixels.ItoperatesquicklyenoughforHMDsand
deliverssuperiorperceptualqualityinsubjectiveevaluations.Incontrast,Reducto[118]aimsto
reducebandwidthconsumptioninUL-basedvideoanalytics.Ittracksbasicfeatures,suchaspixel
andedgedifferences,andidentifiesrelevantfeaturesforspecificqueries.Reductoreliesonk-means
clusteringtoestablishadynamicthresholdforframefilteringatthecamera-equippeddevice.By
filteringoutlessimportantframes,itreducesuploadtrafficwhilemaintaininganalyticsaccuracy.
Among the latest advancements in neural codecs, [116] introduces a data-scalable codec that
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:12 L.PeroniandS.Gorinsky
Fig.4. Transcodingattheprocessingstageoftheend-to-endstreamingpipeline.
employsAEstrainedwithULandcustomlossfunction.Thiscodecenhancescompressionquality
witheachnewpacketreceivedandachievesthehighestqualitywhenthereisnopacketloss.
4.3 MainTakeaways
Thereviewofrecentresearchoningestion-stagedesignsrevealsastrongfocusonlivestreaming.
Thisemphasisstemsfromthegrowingimportanceandsignificanttechnicalchallengesofthelive
mode.Thestricterend-to-endlatencyconstraintsoflivestreamingaffecttheingestionstageand
promoteatrendtowardintegratedend-to-endstreamingsolutions.Anothertrendistheincreasing
computationalroleofcamera-equippeddevicesabletooffloadprocessingfrommediaservers.This
offloadingdeliversfastervideoanalyticsanddecreasesuploadbandwidthconsumption.ML-based
methodsareincreasinglyprominentattheingestionstage,eitherascorealgorithmsorsupporting
components.Inparticular,ML-basedSRmethodsreceiveconsiderableattentionandsuccess,with
aprevalenceofadaptingexistingmodelsandeffectivetrainingstrategiesratherthandeveloping
newMLtechniques.
5 Processing
5.1 Background
Theprocessingstageliesbetweeningestionanddistributionintheend-to-endstreamingpipeline.
Itoperatesondedicatedorcloudserversandperformsvarioustaskstosupporttheadjacentstages.
TheessentialtaskattheprocessingstageoftheHASpipelineistranscoding[4],whichconverts
encoded video into multiple representations. Since transcoding produces compressed videos, it
sharessimilaritieswiththevideocompressionperformedduringtheingestionstage,makingthe
backgroundinformationinSection4.1.1relevant.However,therearekeydifferences.Whilethe
primary goal of encoding on the camera-equipped device is to efficiently utilize the ingestion
bandwidth,transcodingleveragesthesuperiorcomputationalandstorageresourcesofthemedia
servertocreatecompressedvideossuitablefordistributiontoawiderangeofuserdevices.
Figure4presentsaflowchartoftranscoding.Afterreceivingencodedvideoasinput,thetask
decodes the video and applies pre-processing, such as noise filtering. Then, the task defines an
encodingladderbyspecifyingthetargetbitrate,resolution,andframerateofeachrepresentation.
Transratingandtranssizingrefertotranscodingwherethegeneratedrepresentationsdifferonly
in their bitrate or resolution, respectively. For each rung of the encoding ladder, the process re-
encodesthedecodedvideotocreateacorrespondingnewrepresentation.Afterpost-processing,
suchassubtitleembedding,thetranscodingtaskstoresthecreatedrepresentationsonthemedia
serverandrecordstheencodingladderinamanifestfile.
Alongsidetranscoding,whichisintrinsictotheHASpipelineanddirectlyimpactsend-to-end
streamingperformance,theprocessingstageperformsavarietyofauxiliarytasks.Videosplitting
divides the video into smaller chunks for HTTP compatibility, typically ranging from 2 to 10 s
induration,withthisvariationsignificantlyaffectingthequalityofvideostreaming[207].Video
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:13
Table2. TranscodingDesignsattheProcessingStage(uAbbreviatesUnspecified)
Name[reference] Method Year Coretechnique Codec Type Performance Infrastructure
statistics-driven
| [202] |     | 2017 |     | H.264→H.265 | u   | processing | u   |
| ----- | --- | ---- | --- | ----------- | --- | ---------- | --- |
earlytermination
Intuition
joint
| [165] |     | 2018 |     | H.264,H.265 | u   | processing | u   |
| ----- | --- | ---- | --- | ----------- | --- | ---------- | --- |
crypto-transcoding
frame-rate
| EVSO[149] |     | 2018 | adjustment | H.264 | offline | energy | u   |
| --------- | --- | ---- | ---------- | ----- | ------- | ------ | --- |
LwTE[51] 2021 MILP,binarysearch H.265 hybrid storage,processing edge
| ARTEMIS[179] |     | MIP 2023 | MILP | u   | onlineprocessing,bandwidth |     | CDN |
| ------------ | --- | -------- | ---- | --- | -------------------------- | --- | --- |
ALPHAS[180] 2025 ILPsubmodularity H.264 online processing CDN
| [107] | Theory | 2015  | Markovmodel   | H.264 | hybrid  | processing | CDN |
| ----- | ------ | ----- | ------------- | ----- | ------- | ---------- | --- |
|       |        | Other | context-aware |       |         |            |     |
| [30]  |        | 2018  |               | H.264 | offline | bandwidth  | u   |
ladderoptimization
knapsack-like
| [113] |     | 2020 | optimization | H.264 | hybrid | energy | u   |
| ----- | --- | ---- | ------------ | ----- | ------ | ------ | --- |
problem
MAMUT[39] 2018 multi-agentQL H.265 online processing,energy u
RL
AC,dual-clipPPO,
| DeepLadder[81] |     | 2021 |     | H.264 | online | bandwidth,storage | u   |
| -------------- | --- | ---- | --- | ----- | ------ | ----------------- | --- |
DNNwith1DCNNs
ML
| [26] |     | 2018 | DTs | H.265 | online | processing,energy | u   |
| ---- | --- | ---- | --- | ----- | ------ | ----------------- | --- |
RFs
| [66]        |     | SL 2018 |               | H.265     | u   | processing | u   |
| ----------- | --- | ------- | ------------- | --------- | --- | ---------- | --- |
| FastTTPS[3] |     | 2020    | MLP           | H.264     | u   | processing | u   |
| HEQUS[60]   |     | 2021    | NBclassifiers | H.265→VVC | u   | processing | u   |
editingaltersthevideocontent,e.g.,byaddingadvertisementsorremovingcensoredmaterial.Tra-
ditionallycarriedoutattheprocessingstage,videoanalyticsemploystechniquesfromcomputer
visionforobjectdetectionandimagesegmentation,classification,andrecognition.Videostorage
onthemediaserverisparticularlyimportantforVoD,wherevideosneedtoremainavailableover
extendedperiods.
5.2 RecentResults
Our review of recent research at the processing stage focuses on its main task of transcoding.
These studies typically aim to reduce processing time, energy consumption, storage needs, and
bandwidthusage.
Again,wepresentthereviewedworksaccordingtothemethodology-basedclassificationsout-
linedinSection3.1:intuition,theory(MIPandother),andML(RLandSL).Besidesthecoretech-
niqueandcodec,whicharerelevantacrossallstages,Table2alsocharacterizestheprocessing-
stagedesignsbasedon:(1)optimizationtypeasonline,offline,orhybrid,(2)processing,energy,
storage,orbandwidthasperformanceimprovementobjectives,and(3)explicitconsiderationof
edgeorCDNinfrastructure.
5.2.1 Intuition-Based Methods. To support fast low-complexity transcoding from H.264 to
H.265, [202] employs intuitive statistics-driven heuristics for different types of coding units
(CUs).TheseheuristicsallowforearlyterminationofCUpartitioningandpredictionunitmode
selection. Ref. [165] deals with transcoding video streams encrypted in the H.264 or H.265 for-
mats. Because decrypting and re-encrypting these streams introduces significant latency, this
work develops a joint crypto-transcoding scheme that enables transcoding of encrypted video
streamswithoutdecryptingthemorexposingthedecryptionkeyatintermediatedevices.Tore-
duceenergyconsumptiononmobiledevices,environment-awarevideostreamingoptimiza-
tion(EVSO)[149]considersthedevice’sbatterystatusandgeneratesencodingladdersthatadjust
theframerateofdifferentvideochunksbasedonanewmetricofperceptualsimilarity.
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:14 L.PeroniandS.Gorinsky
5.2.2 Theory-Based Methods. To minimize storage and processing requirements, both light-
weighttranscodingattheedge(LwTE)[51]andadaptivebitrateladderoptimizationfor
livevideostreaming(ARTEMIS)[179]relyonMIP.InLwTE,theedgeserverperformspartial
transcoding based on the optimal CU partitioning structure received from the origin server. By
applying binary search to a mixed-integer linear programming (MILP) formulation, LwTE
heuristicallydistinguishesbetweenpopularandunpopularvideochunks.Forunpopularchunks,it
storesonlythehighestbitratelevelandgenerateslowerbitratelevelsontheflythroughmetadata-
acceleratedtranscoding.Incontrast,ARTEMISdynamicallydefinestheencodingladderforalive
streamingsessionbyconsideringcontentcomplexity,networkconditions,anddetailedclientfeed-
back in a standard format [17]. ARTEMIS advertises many representations via a mega-manifest
file and employs MILP to select a smaller subset of these representations for the encoding lad-
der.Similarly,adaptivebitrateladderoptimizationformulti-liveHAS(ALPHAS)[180]con-
structsencodingladdersformultiplelivestreamsbydynamicallygeneratingacontent-awarebi-
trateladderforeachstream.Itaccountsforencodercomputationalcapabilities,CDNbandwidth
constraints,andstreamprioritization,integratesthemega-manifestconceptwithreal-timevideo
multimethodassessmentfusion(VMAF)[120]prediction,andsolvesanintegerlinearpro-
gramming(ILP)formulationbyleveragingitssubmodularproperties.
Othertheory-basedworksinclude[107],whereaCDNperformsonlinejust-in-timetranscod-
ing of a video chunk to the needed bitrate only when a user requests it. This design relies on a
Markovmodeltopredictthebitraterequestedforthenextchunk,enablingtheCDNtostartde-
liveringthetranscodedchunkimmediatelyuponreceivingtherequest.Ref.[30]explorescontext-
awareencodingandformulatesencoding-ladderdefinitionasanoptimizationproblemthatmod-
els the client’s bandwidth estimates and viewport sizes as stationary random processes. To sup-
portenergy-efficienttranscoding,[113]selectsbetweenthreeoptions:offlinetranscoding,online
transcoding,andservingthechunkatalowerthanrequestedbitrate.Theselectionseekstomaxi-
mizevideoqualitywithinalimitimposedonthetotaltranscodingtime,formulatesaknapsack-like
problem,andsolvestheproblemviaagreedyheuristic.
5.2.3 ML-BasedMethods. MAMUT [39]andDeepLadder[81]areRL-baseddesignsforeffi-
cientreal-timetranscoding.MAMUTemploysmulti-agentQ-learning(QL) inanenvironment
withmultipleusers,wherethreeagentscollaborativelyadjustthenumberofencodingthreads,QP,
and processor frequency. This optimization seeks to maximize a reward function that combines
theframerate,bitrate,PSNR,andpowerconsumption.Ontheotherhand,DeepLadderleverages
contentfeatures,availablebandwidth,andstoragecoststotranscodeeachchunkaccordingtoan
encodingladderdefinedviaadual-clippedversionof proximalpolicyoptimization(PPO).
Refs.[26,66]applySLtolimittheencoder’sparametersearchandtherebyreducetranscoding
time.Ref.[26]employsDTstoconstrainthemaximumCTUdepth,aimingtobalancetranscoding
time,energyconsumption,andvideoquality.Ref.[66]acceleratescascadedpixel-domaintranscod-
ingbyemployingtwoRFclassifierstosetupperandlowerlimitsontheCTUdepth.Fastvideo
transcoding time prediction and scheduling (FastTTPS) [3] considers features of source
videos,trainsanMLPtopredicttranscodingtime,andleveragesthepredictionstoscheduleparal-
lelexecutionsoftranscodingtasks.HEVC-basedquadtreesplitting(HEQUS)[60]reducesthe
encoder’sparametersearchfortranscodingfromH.265toVVC.IttrainsNBclassifierstopartition
the first QT level into 128×128 blocks and uses the H.265 CU partitioning to guide QT splitting
decisionsfor64×64blocksandlowerlevels.
5.3 MainTakeaways
Recent research efforts at the processing stage put a key focus on faster processing and lower
power consumption. In particular, transcoding acceleration enables on-the-fly definition of
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:15
Fig.5. Thedistributionstageoftheend-to-endVoDstreamingpipeline.
encoding ladders, which not only decreases storage demands but also aligns with the growing
trendtowardlivestreaming.Theexplicitconsiderationofdistribution-stageinfrastructure,such
asCDNoredgeservers,reflectsacloserintegrationacrosspipelinestages.ML-basedmethodsare
increasingly prominent in processing-stage designs and, in contrast to the ingestion stage, tend
toemploysimplemodelsratherthandeepnetworks.Additionally,mostdesignsassumetheuse
ofH.264orH.265codecsratherthanmoreadvancedoptions.
6 Distribution
6.1 Background
The end-to-end streaming pipeline concludes with the distribution stage, which delivers the re-
quested video to the user device and plays it on the screen. Figure 5 illustrates the distribution
stageofHASforVoD.Atthisstage,theuserdevicerequestsonevideochunkatatimefromthe
CDN,whichcacheseachchunkinmultiplerepresentationsprovidedbythemediaserver.TheCDN
supports scalable low-latency delivery by utilizing its extensive network of edge servers spread
acrossdifferentgeographicalregions.TheABRalgorithmontheuserdevicedynamicallychooses
theappropriaterepresentationforthenextrequestedchunkbasedonpredictionsofvaryingnet-
workbandwidth.Thisalgorithmaimstobalanceuninterruptedplaybackwithhighvideoquality,
ultimately ensuring high QoE for the user. Live streaming employs shorter chunks, downloads
themfromthecamera-equippeddevicetotheuserdeviceinrealtime,andimposesmorestringent
requirementsondistribution,promptingdifferentapproachestoCDNsupportandQoEimprove-
ment.ThissurveyfocusesonthekeyABR,CDN,andQoEaspectsofthedistributionstage.
6.1.1 ABRAlgorithms. TheABRalgorithmdynamicallyselectsthechunkrepresentationand
servesasacornerstoneofHAS,withHLSandDASHbeingthepredominantHASprotocols.While
HLScommonlyemploysachunkdurationof6s(10soriginally)andiscompatiblewiththeH.264
orH.265codecs,DASHtypicallyhasachunkdurationbetween2and10sandiscodec-agnostic.
OursurveyfocusesontheprevailingHASapproachthatusesclient-sideABRalgorithms.
Figure6depictstheABRalgorithmasaflowchart.Atthestartofthestreamingsession,theclient
downloadsamanifestfilefromthemediaserver.Themanifestincludesanencodingladderthat
describestheavailablerepresentationsforeachvideochunkintermsoftheirbitrate,resolution,
and frame rate. The ABR algorithm updates a control metric based on the monitored network
conditions.Forexample,thecontrolmetricistypicallyplayback-bufferoccupancyandnetwork-
bandwidthestimatein,respectively,buffer-centricandthroughput-centricABRalgorithms.Ifthe
controlmetricindicatesthatthecurrentrepresentationistoolow,theABRalgorithmincreasesthe
representationforthenextchunktoenhancevideoquality.Ifthecontrolmetricistoohigh,the
algorithmdecreasestherepresentationtoavoidvideostallingandrebuffering,whichoccurwhen
chunksarrivetoolateforsmoothplayback.Otherwise,therepresentationremainsunchanged.In
allthreecases,theclientdownloadsthenextchunkintheselectedrepresentation.Thiscycleof
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:16 L.PeroniandS.Gorinsky
Fig.6. TheABRalgorithm.
updatingthecontrolmetric,selectingtheappropriaterepresentation,anddownloadingthechunk
continuesuntiltheendofthestreamingsession.
Representation selection is challenging due to a priori unknown network conditions, mis-
matchesbetweenthemanifest-filedescriptionsandactualchunkbitrates,largegapsbetweenthe
bitratesofadjacentrepresentations,andconflictingperformanceobjectives.BecauseoptimalABR
controlisanNP-hardproblem[85],practicalABRalgorithmsemployvariousheuristics,e.g.,pre-
dictingtheavailablenetworkbandwidthfromtheclient’shistoricalthroughputmeasurements.
6.1.2 CDN Support. A CDN refers to a system of cache servers distributed across wide geo-
graphicalareastoimprovetheperformanceofcontentdeliveryfromCPstoendusers[151].The
CDN stores videos and other content collected from CPs’ origin servers in cache servers placed
nearusers,reducingnetworktrafficandenablinglow-latencycontentdelivery[130].Thoughorig-
inallyoptional,CDNsareindispensableinthemodernInternetecosystemandhandleestimated
56%and72%ofallInternettrafficin2017and2022,respectively[37].
EconomicrelationshipswithCPsformthebasisforclassifyingCDNsaspublic,private,orhy-
brid. A public CDN, e.g., Akamai [43], acts as a third party and charges the CPs for its content-
deliveryservices.AprivateCDNbelongstothesameorganizationastheCPsutilizingit,whilea
hybridCDNservesbothinternalandexternalCPs.DuetoCDNs’differencesinscalability,pricing,
andQoEacrossregionsandtime[186],CPsoftendelivercontentovermultipleCDNs.
Standards such as common media client data (CMCD) [17] and common media server
data (CMSD) [10], introduced in 2020 and 2022 respectively, enable information exchange be-
tweenaCDNandclientstosupportdataanalysisandQoEmonitoring.Additionally,edgeinfras-
tructureextendstheoriginalCDNconceptbyinvolvingnetworkoperatorsincontentcachingand
offersnewoptionsforvideostreaming[22].
6.1.3 QoE. In contrast to the earlier notion of QoS, which encompasses individual network-
level metrics such as packet loss, latency, and throughput, QoE captures the user’s subjective
satisfaction with the overall performance of a streaming service [90]. QoE is crucial for stream-
ingplatformsbecauseusersatisfactionstronglycorrelateswithcustomerattractionandretention
and,ultimately,providerrevenues.However,userperceptionofserviceperformanceiscomplex
anddependsonnumerousIFs,suchasnetworkbandwidth,latency,andvideoquality[168].
AssessingQoEischallengingduetoitssubjectiveinterdisciplinarynature.Directmeasurement
typically involves subjective tests where users rate their streaming experience. These tests typi-
cally take place in controlled lab environments and follow well-established protocols informed
byuserexperiencedesign[211].Onlinecrowdsourcingimprovestestingscalabilityandweakens
controloverexperimentalsettings[78].ThepredominantapproachtoQoEevaluationisindirect
andreliesonsubjectiveteststobuildaQoEmodelthatexpressesQoEasafunctionofobjectively
measurableIFs.DatascienceenhancesthepredictivepowerofQoEmodelsviaML-basedmethods.
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:17
Fig.7. QoEmodeling.
QoE models commonly represent QoE in terms of the mean opinion score (MOS) [91], the
averageratinggivenbyusersinasubjectivestudy.
Figure7illustratesQoEmodelingthatconstructsaQoEmodeliteratively.Theprocessiden-
tifies the IFs of the QoE model and enters a cycle of conducting a subjective test, recording the
respective IF values, collecting a user-provided QoE score, and mapping the IFs to the score to
updatetheQoEmodel.Thisiterativerefinementallowsthecurrentmodeltoinformtheconfigu-
rationofthesubsequenttest,therebyreducingthenumberofsubjectivetestsneededtodevelop
an accurate QoE model [153]. After the construction is complete, the process utilizes a separate
datasettovalidatethemodelandoutputsthevalidatedQoEmodel.
Onceconstructed,aQoEmodelsupportsautomaticQoEcomputationbasedontheobjectively
measurable IFs, eliminating the need for human feedback and enabling QoE evaluation at scale.
Existing QoE models vary widely in terms of the IFs considered and the methods used for con-
struction[159].DespitethesignificanceofQoEanditsmodels,theirtreatmentoftenlacksstan-
dardizationandrigor,creatingopportunitiesforimprovement[152].
6.2 RecentResults
6.2.1 ABRAlgorithms. RecentresearchonABRalgorithmsaimstoimproveQoEforendusers,
eitherdirectlyorindirectly.DirectapproachesexplicitlyincorporateaQoEmodelintothecontrol
metricoftheABRalgorithm,e.g.,employingaQoEmodelastherewardfunctioninanRL-based
ABRalgorithm.IndirectapproachesfocusonindividualIFs,suchasthebitrate,PSNR,SSIM,and
VMAF to capture video quality. In addition to video quality and its stability, prominent IFs in
thedesignandevaluationofABRalgorithmsincludethefrequencyanddurationofvideostalls.
Efficient utilization of network bandwidth and its fair distribution among multiple sessions are
commondesigngoals.Forlivestreaming,ABRalgorithmsalsoprioritizereducinglatency.
WestructureourcoverageofABRdesignsinaccordancewiththetaxonomygiveninSection3.1:
intuition-based(buffer-centric,throughput-centric,andhybrid),theory-based(MIP,MPC,PID,LO,
BO, and other), and ML-based (RL, IL, SL, and UL), with the RL-based ABR algorithms catego-
rized further by their reliance on A3C, A2C, AC, or other methods. Tables 3–5 summarize the
intuition-based,theory-based,andML-basedABRalgorithms,respectively.Inadditiontotheuni-
versalcoretechniqueandcodeccharacteristics,eachtabledescribesthereviewedworkswith
respectto:(1)theirapplicationmodeasVoDorlivestreaming,(2)SRusage,(3)employmentofa
QoEmodelindesignorevaluation,(4)bandwidth-efficiencyevaluation,and(5)bandwidth-
fairnessevaluation.
Intuition-based methods: Laying the groundwork for buffer-centric designs, a series of
buffer-basedalgorithms(BBAs)[86]maptheoccupancyleveloftheplaybackbuffertoacon-
trolmetric.BBA-0employspiecewiselinearmappingofthebufferoccupancytoabitrate.BBA-1
performsthemappingtoachunksize.BBA-2extendsBBA-1byestimatingtheavailablenetwork
bandwidthandincreasingthebitratemoreaggressivelyduringastartupphase.Segment-aware
rateadaptation(SARA)[96]enhancesthemanifestfilewithchunksizesandswitchesbetween
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

| 322:18 |     |     |     | L.PeroniandS.Gorinsky |     |
| ------ | --- | --- | --- | --------------------- | --- |
Table3. Intuition-BasedABRAlgorithmsattheDistributionStageoftheEnd-to-EndStreamingPipeline
(uAbbreviatesUnspecified)
|     |     |     |     | Bandwidth | Bandwidth |
| --- | --- | --- | --- | --------- | --------- |
|     |     |     |     | QoE       | fairness  |
Name[reference] Method Year Coretechnique Codec Mode SR model efficiency
|         |      |                        |       | evaluation | evaluation |
| ------- | ---- | ---------------------- | ----- | ---------- | ---------- |
| BBA[86] | 2014 | linearpiecewisemapping | u VoD | ✘ ✘ ✘      | ✘          |
buffer-
switchbetween
| SARA[96] | centric 2015 |     | u VoD | ✘ ✘ ✘ | ✘   |
| -------- | ------------ | --- | ----- | ----- | --- |
adaptationmodes
| ABMA+[14] | 2016 | rebuffering-probability | u VoD | ✘ ✘ ✔ | ✘   |
| --------- | ---- | ----------------------- | ----- | ----- | --- |
characterization
| [46]          | 2015        | proxycaching                 | u VoD      | ✘ ✘ ✘ | ✘   |
| ------------- | ----------- | ---------------------------- | ---------- | ----- | --- |
|               |             |                              |            | ✘ ✘ ✘ | ✘   |
| LOLYPOP[137]  | 2016        | stall-probabilityprediction  | H.264 live |       |     |
|               | throughput- |                              | H.264,     |       |     |
| ARBITER+[204] | 2018        | hybridthroughputsampling     | VoD        | ✘ ✘ ✘ | ✔   |
|               | centric     |                              | H.265      |       |     |
|               |             |                              |            | ✘ ✘ ✔ | ✔   |
| PREPARE[169]  | 2019        | server-clientcooperation     | u VoD      |       |     |
| STALLION[73]  | 2020        | sliding-windowmeasurement    | u live     | ✘ ✘ ✘ | ✘   |
| FESTIVE[93]   | 2014        | statefuldelayedbitrateupdate | u VoD      | ✘ ✘ ✔ | ✔   |
| PANDA[122]    | 2014        | AIMD-basedestimation         | u VoD      | ✘ ✘ ✔ | ✔   |
|               |             |                              |            | ✘ ✘ ✘ | ✔   |
| SQUAD[187]    | hybrid 2016 | spectrumminimization         | u VoD      |       |     |
| Oboe[6]       | 2018        | offlineparameteroptimization | u VoD      | ✘ ✘ ✘ | ✘   |
| BANQUET[104]  | 2021        | brute-forcesearch            | H.264 VoD  | ✘ ✔ ✔ | ✘   |
its four adaptation modes depending on the buffer occupancy. Aiming to eliminate video stalls,
theadaptationandbuffermanagementalgorithm(ABMA+)[14]reliesonbuffer-occupancy
mappingtocharacterizetherebufferingprobability.
Amongthroughput-centricschemes,[46]cachesvideochunksonanaccesspoint(AP)tosup-
porteffectiveABRstreamingoverthewirelesslinkfromtheAPtotheclient.WhiletheAPselects
chunksforprefetchingintothecache,theclientdetermineswhichchunkstorequestfromeither
theAPoraremoteserver.Low-latencyprediction-basedadaptation(LOLYPOP) [137]tar-
getslive streaming andstrivestoimprove QoE byoptimizing theoperatingpoint, ametricthat
combineslatency,stallfrequency,andbitrate-changefrequency.LOLYPOPpredictsTCPthrough-
putoverperiodsrangingfrom1to10sandassessesthepredictionerror.Interestingly,thestudy
findsthatthesimplemethodofusingthelastsampleasthepredictionisthemostaccurate.Devel-
oped for streaming over mobile networks, adaptive rate-based intelligent HTTP streaming
(ARBITER+) [204] addresses dynamic network conditions and bitrate variability through tech-
niquessuchastunablesmoothingandhybridthroughputsampling.Playbackrateandpriority
adaptive bitrate selection (PREPARE) [169] is a throughput-centric ABR algorithm that ac-
counts for client priority and playback speed. PREPARE improves average bitrate and stability
by involving the server into prediction of the network bandwidth. Designed for live streaming,
standardlow-latencyvideocontrol(STALLION) [73]usesaslidingwindowtomeasurethe
meanandstandarddeviationofbothbandwidthandlatency.TheimplementationofSTALLIONin
dash.js,apopularstreamingclient,outperformstheclient’sbuilt-inABRalgorithmbysignificantly
increasingthebitrateanddecreasingthenumberofstalls.
Representing a hybrid approach, the fair, efficient, and stable adaptive algorithm
(FESTIVE)[93]combinesseveralmechanismstoensureefficiency,fairness,andstabilityinABR
streamingtomultipleclients.Thesemechanismsincluderandomizedschedulingofchunkrequests,
harmonic-meanestimationofnetworkbandwidth,andstatefulbitrateselectionwithdelayedup-
dates.Pursuingsimilargoals,probeandadapt(PANDA)[122]incorporatesestimation,smooth-
ing,quantization,andschedulingtechniquesand,inparticular,appliesAIMDtoestimatenetwork
bandwidth.AccountingforinteractionsbetweenDASHandTCP,spectrum-basedqualityadap-
tation(SQUAD) [187]improvesQoEbyminimizingthespectrum,ametricthatreflectsbitrate
variation.ForagivenABRalgorithm,Oboecomputesanofflinemapofnetworkconditionstoan
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:19
Table4. Theory-BasedABRAlgorithmsattheDistributionStageofthePipeline(uAbbreviates
Unspecified)
|     |     |     |     |     | Bandwidth | Bandwidth |
| --- | --- | --- | --- | --- | --------- | --------- |
|     |     |     |     | QoE |           | fairness  |
Name[reference] Method Year Coretechnique Codec Mode SR efficiency
|               |          |                         |           | model | evaluation | evaluation |
| ------------- | -------- | ----------------------- | --------- | ----- | ---------- | ---------- |
|               |          |                         |           | ✘ ✔   | ✔          | ✘          |
| OSCAR[203]    | MIP 2016 | MINLP                   | H.264 VoD |       |            |            |
| RobustMPC and |          |                         |           |       |            |            |
|               | 2015     | harmonic-meanestimation | u VoD     | ✘ ✔   | ✘          | ✘          |
FastMPC[200]
| IAA[58]   | 2018     | TF-IDF                      | u VoD      | ✘ ✔ | ✘   | ✘   |
| --------- | -------- | --------------------------- | ---------- | --- | --- | --- |
|           |          |                             |            | ✘ ✔ | ✘   | ✘   |
| LDM[119]  | MPC 2020 | framedropping               | H.264 live |     |     |     |
| Fugu[196] | 2020     | transmission-timeprediction | H.264 VoD  | ✘ ✔ | ✘   | ✘   |
| iMPC[176] | 2021     | iLQR-basedlinearization     | H.264 live | ✘ ✔ | ✘   | ✘   |
| PIA[158]  | 2017     | PIcontrolwithlinearization  | u VoD      | ✘ ✔ | ✘   | ✘   |
|           | PID      |                             | H.264,     | ✘ ✔ | ✔   | ✘   |
| QUAD[157] | 2019     | least-squareoptimization    | VoD        |     |     |     |
H.265
| BOLA[171] | 2020 | utilitymaximization | u VoD | ✘ ✔ | ✘   | ✘   |
| --------- | ---- | ------------------- | ----- | --- | --- | --- |
LO
| Elephanta[156] | 2020    | renewalsystem          | u VoD | ✘ ✔ | ✘   | ✘   |
| -------------- | ------- | ---------------------- | ----- | --- | --- | --- |
|                |         |                        |       | ✘ ✔ | ✘   | ✘   |
| ERUDITE[42]    | 2019    | parameterconfiguration | u VoD |     |     |     |
|                |         |                        |       | ✘ ✔ | ✘   | ✘   |
| [105]          | BO 2021 | Gaussianprocesses      | u VoD |     |     |     |
| QUETRA[195]    | 2017    | M/D/1/Kqueuing         | u VoD | ✘ ✔ | ✘   | ✔   |
Other
| ACAA[79] | 2019 | DP  | u VoD | ✘ ✔ | ✘   | ✘   |
| -------- | ---- | --- | ----- | --- | --- | --- |
optimalconfigurationofalgorithmparametersandautomaticallytunestheseparametersonline
in response to current network conditions [6]. Balancing quality of experience and traffic
(BANQUET) [104] aimstominimize thetrafficvolume whileproviding theQoE level specified
byeithertheuserorthestreamingprovider.Toestimatetheimpactofbitratechoicesontraffic
andQoE,BANQUETemploysbrute-forcesearchacrossallpossiblebitratepatternsforthenext
fewchunksviapredictionsofbuffertransitionsandthroughput.
Theory-basedmethods:Optimizedstall-cautiousadaptivebitrate(OSCAR)[203]repre-
sentsaMIP-basedapproach.Foratransientrangeofthebufferoccupancy,itmodelstheavailable
networkbandwidthusingtheKumaraswamydistributionandformulatesbitrateadaptationover
aslidinglook-aheadwindowasamixed-integernonlinearprogramming(MINLP)problem.
OSCAR’soptimizationobjectivecombinesaswitchingpenaltywithbitrateutility.
MPC forms a prominent basis for recent ABR algorithms. Contributing several innovations,
[200]introducestwoMPC-basedalgorithms:RobustMPCandFastMPC.WhileRobustMPCper-
forms better, FastMPC incurs significantly lower overhead. Additionally, this article proposes a
QoE model that underpins many subsequent ABR designs. As an MPC enhancement aimed at
improvingQoE,theinterest-awareapproach(IAA)[58]adjuststhebitratebyconsideringthe
user’s interest in video scenes. IAA embeds content properties into the manifest file, allowing
theclienttoanalyzethesepropertiesandquantifytheuser’sinterestinthecontentviatheterm
frequency-inversedocumentfrequency(TF-IDF) method.LDM[119]utilizesMPCforlive
streaminganddropsframestoensurelowlatency.Fugu[196]isanMPC-basedapproachthatpre-
dictstransmissiontimeforeachchunkviaaDNNtrainedviaSLinsitu,i.e.,intheactualdeploy-
mentenvironment.Toachievelowlatency,iLQRbasedmodelpredictivecontrol(iMPC)[176]
combinesMPCwiththeiterativeLinearQuadraticRegulator(iLQR).iMPCemploysMPCto
predicttheavailablenetworkbandwidthanditerativelylinearizesthecontrolsystemaroundits
operationpointtodeterminethebitrateviaiLQR.
RelyingonPIDasitsmainmethod,PID-controlbasedABRstreaming(PIA)[158]removes
thederivative(D)componentfromthestandardPIDcontrollerandlinearizestheclosed-loopcon-
trolsystemtomaintainthebufferoccupancyatatargetedlevel.PIAalsoequipsthisproportional-
integral(PI) controllerwithmechanismsforfasterinitialramp-up,reductionofbitratefluctua-
tion, and avoidance of bitrate saturation. Using the same PI controller as PIA, quality-aware
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:20 L.PeroniandS.Gorinsky
data-efficientstreaming(QUAD)[157]strivestomaintainvideoqualityatanintendedlevelto
preventstalls,enhanceplaybacksmoothness,andreducebandwidthconsumption.
LO-baseddesignsincludethebufferoccupancybasedLyapunovalgorithm(BOLA)[171],
whichjointlyoptimizesplaybacksmoothnessandbitrateutilityunderaratestabilityconstraint.
BOLAprovidestheoreticalguaranteesontheachievedutilityandperformsexcellentlyinpractice.
Elephanta[156]addressesthediversityofQoEperceptionamongdifferentusers.Itoffersanin-
terfaceforuserstoadjustQoEperceptionparameters,modelsvideostreamingasarenewalsystem,
andselectsthebitratebyminimizingauser-specificfunctionthatcombinespenaltiesanddrift.
ByemployingBO,thedeepneuralnetworkforoptimaltuningofadaptivevideostream-
ingcontrollers(ERUDITE)[42]configurestheparametersofthefeedbacklinearizationadap-
tivestreamingcontroller(ELASTIC) [41]tojointlyoptimizeQoEandcontrolrobustness.At
runtime,ERUDITEusesanoffline-trainedCNNtotunethecontrollerparametersinaccordance
withreal-timebandwidthmeasurementsandvideofeatures.Ref.[105]developsacontext-aware
ABRalgorithmtomaintainQoEattheminimumlevelacceptabletotheuser.Thisalgorithmlever-
agesGaussianprocessestodeterminethetargetQoElevelandthenselectsabitrateviaBANQUET.
Among other theory-based ABR algorithms, queuing theory-based rate adaptation
(QUETRA)[195]usestheMarkoviandeterministicsingle-serverfinite-capacity(M/D/1/K)
queuingmodeltoassessthebufferoccupancy.Thealgorithmtakesintoaccountthebuffercapacity
andnetworkbandwidth,adjustingthebitratetokeepthebufferapproximatelyhalf-full.QUETRA
is notable for not requiring parameter tuning and performs well across various heterogeneous
scenarios. To address the diversity of QoE perception among users, affective content-aware
adaptation(ACAA)[79]considerstheemotionalrelevanceofcontentfordifferentusers.ACAA
characterizesvideochunksanduserswithconfidencelevelsforsixbasicemotions,formulatesa
QoEmaximizationproblembasedonthisemotionalinformation,andsolvestheproblembymeans
ofDP.
ML-based methods: Pensieve [131] revolutionizes ABR streaming by applying deep RL
(DRL)and,inparticular,theA3Cmethod.PensieveformulatesbitrateselectionasaDRLproblem
andsolvesitusingA3Cwherethefunctionapproximatorcombinesone-dimensional(1D)CNNs
andfullyconnectedlayers.TheDNNsupportsdifferentencodingladders.Toacceleratestatetran-
sitions, Pensieve trains its DNN with a chunk-level simulator, a technique that influences many
subsequentDRL-basedABRapproaches.
NAS [197] is another A3C-based algorithm that leverages content-aware DNNs and anytime
prediction to improve QoE via SR. For each video, the server trains multiple DNNs of different
sizesandperformancelevels.TheclientpicksthelargestDNNabletooperateinrealtime.Further-
more,eachDNNisscalableandconsistsofmultiplelayers.Thisenablestheclienttoprogressively
downloadtheentireDNN,immediatelybenefitfromthedownloadedDNNlayers,anddynamically
selectaDNNconfigurationforSRofthecurrentframes.NASemploysA3Ctobalancebitratese-
lectionwithprogressiveDNNdownload.Super-resolutionbasedadaptivevideostreaming
(SRAVS)[210]alsocombinesA3CwithSR.UsinganSRCNN[45]forvideoreconstruction,SRAVS
maintainsseparatedownloadingandplaybackbuffers.Theseparationdecouplesbitrateselection
fromreconstructiondecisions,allowingforindependentoptimizationofbothprocesses.
Grad [124] applies A3C to design ABR algorithms for SVC-encoded videos. It mitigates SVC-
related coding overhead and improves QoE through jump-enabled hybrid coding (HYBJ),
where a single layer delivers multiple levels of video-quality enhancement. Ref. [9] jointly max-
imizesQoEandfairnessinvideostreamingtomultipleclientsoverasharedbottlenecklink.Its
A3Cactorincorporatesalongshort-termmemory(LSTM) layer,andtheserverdynamically
configuresthemanifestfilebasedontransport-layersignalsaboutthelossrate.Withthroughput
measurementsunderlyingmanyABRalgorithms,accuratenetworkthroughput(ANT) [199]
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:21
Table5. ML-BasedABRAlgorithmsattheDistributionStageofthePipeline(uAbbreviatesUnspecified)
|     |     |     |     |     | Bandwidth Bandwidth |
| --- | --- | --- | --- | --- | ------------------- |
Name[reference] Method Year Coretechnique Codec Mode SR QoE efficiency fairness
model
|                |             |                       |           |     | evaluation evaluation |
| -------------- | ----------- | --------------------- | --------- | --- | --------------------- |
|                |             |                       |           | ✘ ✔ | ✘ ✘                   |
| Pensieve[131]  | 2017        | DNNwith1DCNNs         | u VoD     |     |                       |
| NAS[197]       | 2018        | content-awareDNNs,SR  | H.264 VoD | ✔ ✔ | ✔ ✘                   |
| SRAVS[210]     | 2020        | CNN,SR                | u VoD     | ✔ ✔ | ✘ ✘                   |
| Grad[124]      | A3C 2020    | DNNwith1DCNNs,HYBJ    | SVC VoD   | ✘ ✔ | ✔ ✘                   |
|                |             |                       |           | ✘ ✔ | ✘ ✔                   |
| [9]            | 2020        | LSTM,manifestupdate   | H.264 VoD |     |                       |
| ANT[199]       | 2021        | CNN,k-meansclustering | u VoD     | ✘ ✔ | ✘ ✘                   |
| FedABR[194]    | 2023        | CNN,LSTM,FL           | H.264 VoD | ✘ ✔ | ✘ ✘                   |
| Ahaggar[18]    | RL A2C 2023 | DPPO,DNNwith1DCNNs    | H.264 VoD | ✘ ✔ | ✔ ✘                   |
|                |             |                       |           | ✘ ✔ | ✘ ✘                   |
| Fastconv[135]  | 2019        | CNNs                  | H.264 VoD |     |                       |
|                |             |                       |           | ✘ ✔ | ✘ ✘                   |
| MLMP[87]       | AC 2020     | PPO,LSTM              | u VoD     |     |                       |
| Vabis[54]      | 2020        | ACKTR,DNNs            | u live    | ✘ ✔ | ✘ ✘                   |
| Stick[84]      | 2020        | DDPG,DNNwith1DCNNs    | H.264 VoD | ✘ ✔ | ✘ ✘                   |
| Tiyuntsong[80] | 2019        | self-playRL,GAN       | u VoD     | ✘ ✘ | ✘ ✘                   |
|                | Other       |                       |           | ✘ ✔ | ✘ ✘                   |
| Ruyi[218]      | 2022        | DQL,DNNwithCNNs       | H.264 VoD |     |                       |
| PiTree[136]    | 2019        | DTs                   | u VoD     | ✘ ✘ | ✘ ✘                   |
| [70]           | IL 2020     | DTs                   | u VoD     | ✘ ✘ | ✘ ✘                   |
| Comyco[83]     | 2020        | DNN                   | H.264 VoD | ✘ ✔ | ✘ ✘                   |
|                |             |                       |           | ✘ ✘ | ✘ ✘                   |
| SMASH[163]     | 2020        | RFs                   | H.264 VoD |     |                       |
|                | SL          |                       |           | ✘ ✔ | ✘ ✘                   |
| Karma[192]     | 2023        | GPT                   | H.264 VoD |     |                       |
| Swift[40]      | UL 2022     | AEs                   | LNCs VoD  | ✘ ✔ | ✔ ✘                   |
seekstopreciselymodelthefullspectrumofavailablenetworkbandwidth.ANTperformsk-means
clusteringofthroughputtracesovershortperiods,trainsaCNNforcluster-specificbandwidthpre-
dictionoverthenextperiod,andutilizesthepredictiontoselectthebitrateviaA3C.Alsobased
onA3C,FedABR[194]providesfastertrainingandpreservesdataprivacyviafederatedlearn-
ing (FL). After receiving from multiple clients their locally trained ABR policies, the FedABR
serverproducesaglobalaggregateABRpolicyanddisseminatesitbacktotheclientsforfurther
refinementoftheirABRalgorithmsbasedonlocaldata.
Ahaggar[18]trainsA2C,asynchronizedvariantofA3C,withdistributedPPO(DPPO)for
server-side bitrate adaptation across multiple clients. Ahaggar leverages CMCD and CMSD for
communication with clients and accelerates learning in new network conditions through meta-
RL.AdditionalABRsolutionsinthegeneralACcategoryincludeFastconv[135],whichsupports
the fast training of a simple AC network by prepending an adapter that converts highly fluctu-
ating input features into a more stable signal. The meta-learning framework for multi-user
preferences(MLMP)[87]utilizesmulti-taskDRLwithPPOforpolicyupdates,ensuringthatbi-
trateadaptationfordifferentusersaccountsforuser-specificsensitivitiestothreeQoEmetrics.De-
signedforlow-latencylivestreaming,thevideoadaptationbitratesystem(Vabis)[54]relieson
actorcriticusingKronecker-factoredtrustregion(ACKTR)initsserver-sideABRalgorithm
andoperatesatthegranularityofframestosynchronizestateinformationduringtrainingandtest-
ing.VabisalsoincorporatesthreeplaybackmodesontheclientsideandaspecializedABRregime
for poor network conditions. Stick [84] combines the deep deterministic policy gradient
(DDPG)withBBAtoimproveABRperformanceandreducecomputationalcosts.StickusesDDPG
totrainanACnetworkthatcontrolsthebuffer-occupancyboundarieswithintheBBAapproach.
Tiyuntsong[80]andRuyi[218]representotherRL-basedABRsolutions.Tiyuntsongemploys
self-playRL,wheretwoABRalgorithmscompeteagainsteachotherinthesamestreamingenvi-
ronment.TherewardsfortheRLagentscomefromwinsandlossesinthisongoingcompetition,
ratherthanfromtraditionalQoEmetrics.Additionally,eachRLagentinTiyuntsongutilizesaGAN
toextracthiddenfeaturesfromextensivehistoricaldata.Ruyiintegratesuserpreferencesintoits
QoEmodelandleveragesthemodeltotrainadeepQL(DQL) algorithm.Ruyiallowsusersto
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:22 L.PeroniandS.Gorinsky
providetheirpreferencesinrealtime,enablingadaptationtothesedynamicpreferenceswithout
modelretraining.
Relying on IL, PiTree [136] employs teacher-student learning in a simulated video player to
convert DNN-based and other sophisticated ABR algorithms into accurate DT representations,
therebyenablingtheefficientonlineoperationofthesealgorithms.InspiredbyPiTree,[70]uses
DTstoreconstructproprietaryABRalgorithmsinahuman-interpretablemannerallowingdomain
expertstoinspect,understand,andmodifytheDTrepresentationsofthealgorithms.Comyco[83]
incorporatesasolvertogenerateexpertABRpoliciesaimedatmaximizingQoEandtrainsaDNN
bycloningthebehavioroftheseexpertpolicies.Itembraceslifelonglearningthroughcontinuous
updatesoftheDNNwithnewlycollectedtraces.
Supervised machine learning approach to adaptive video streaming over HTTP
(SMASH) [163] and Karma [192] are SL-based designs. SMASH trains an RF classifier on out-
puts of nine existing ABR algorithms across various streaming scenarios, while Karma employs
causalsequencemodelingonamultidimensionaltimeseriesandtrainsaGPTviaSLtoenhance
thegeneralizabilityofABRdecisions.BasedonUL,Swift[40]addressesthechallengesofcoding
overhead and latency in layered coding. It incorporates a chain of AEs to create residual-based
layeredcodesontheserverside,asingle-shotdecoderontheclientside,andaPensieve-likeABR
algorithmcompatiblewithlayeredneuralcodecs(LNCs).
6.2.2 CDNSupport. LikeABRalgorithms,CDNsultimatelyaimtoimproveQoEforendusers.
Recent research on CDN support focuses on achieving this goal by improving the integration
ofCDNsintothestreamingpipeline.Thisincludescoordinatingwithtranscodingdesignsatthe
processingstage,collaboratingwithclient-sideABRalgorithms,deployingCDNservers,assigning
users to appropriate servers, and enhancing caching performance. The proposed solutions are
either specific to video streaming or also applicable to other types of traffic. Additionally, some
studiesinvestigatetheutilityofedgecomputingforvideostreaming.
Intuition-basedworksincludethesequentialauctionmechanism(SAM)[175],whichoper-
atesinacrowdsourcedCDNwherethird-partyedgedevicessupplementCDNserversandcharge
CPsforleasedcachespace.Anotherexampleisintelligentnetworkflow(INFLOW)[185],an
intuition-baseddesignfordynamicallyselectingthemostsuitableCDNfrommultipleoptions.It
uses measurements from video players to predict available network bandwidth and latency via
LSTM.Guidedbythesepredictionsandbusinessconstraints,INFLOWintuitivelyselectstheap-
propriateCDNforeachplayerandupdatesthemanifestfileaccordingly.
Theory serves as a major foundation for CDN designs. The video delivery network
(VDN) [139] exemplifies video-specific CDN optimizations and incorporates a centralized con-
trol plane that constructs distribution trees for videos to enable scalable and highly responsive
CDN operation. VDN formulates the tree construction as an integer program and approximates
the program through initial solutions and early termination. To improve upon traditional CDN
cachingheuristics,AdaptSize[20]utilizesaMarkovmodelforcontentadmissionintothecache.
Toaddressbothcachingandtranscodinginaradioaccessnetwork,[21]formulatesanILPprob-
lemtominimizeCDNcostsandsolvesitwithagreedyheuristic.ForenhancingABRperformance,
[61]monitorsvideostreamingoftwopopularCPsacrossthreemajorCDNsanddevelopsaCDN-
awarevariantofRobustMPC.Incontrast,FastTrack[7]aimstominimizetheprobabilitythatstall
durationinCDN-assistedvideostreamingexceedsapredefinedthreshold.FastTrackachievesthis
byformulatinganon-convexoptimizationproblem,dividingitintofoursubproblems,andsolving
themiterativelywithanalgorithmthatreplacesthenon-convexobjectivefunctionwithconvex
approximations.ToimproveQoEbycombiningSRwithedgecomputing,videosuper-resolution
andcaching(VISCA)[205]cachesLRchunksattheedge,accountsforchunkqualityandrequest
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:23
frequencyintheevictionpolicy,increasesresolutionviaSR,andstreamsvideostoplayersviaan
edge-basedABRalgorithm.
Representing ML-based solutions, learning-based edge with caching and prefetching
(LEAP)[166]employsaDNNtoprefetchandcachechunksattheedge,predictingQoEinscenar-
iosofcachehitvs.cachemiss.Meanwhile,RL-Cache[106]utilizesafeedforwardneuralnetwork
for cache admission and trains this network via a new DRL method that relies on direct policy
search.
6.2.3 QoE. Since QoE models are essential for both evaluating and designing video stream-
ingsystems,researchinthisareaheavilyfocusesontheinterdisciplinarytopicofQoEmodeling.
ThemainobjectiveistoincreasethepredictivepowerofQoEmodelsbyapplyingadvanceddata-
science techniques and incorporating new IFs, such as content characteristics and user engage-
ment.RecentstudiesalsoemphasizepersonalizationofQoEmodelstoprovidebetterservicefor
individualusers.
Relianceon intuitioniscommon in QoE modeling. YouQ [215] contributesa novel modeling
techniquethatsupportssubjectivetestsonFacebook’ssocialmediaplatform.ManyABRproposals
come with intuition-based improvements to QoE models. For example, while [200] introduces a
QoEmodelthatincludesvideoqualityasanIF,BOLA[171]redefinesthisfactorasthelogarithm
oftheratiobetweenthebitrateandthelowestbitrateintheencodingladder.Comyco[83]further
changes this IF to VMAF. In contrast, the QoE model proposed by SENSEI [208] incorporates
dynamicsensitivitytovideocontent.
Recent theory-based research explores the relationship between user engagement and QoE.
Whereas the queuing-theoretic analysis in [138] shows a strong correlation between these two
notions,VidHoc[209]utilizesuserengagementasaproxyforQoEinitsmodeling.Specifically,
VidHocdynamicallylimitsavailablenetworkbandwidthandleveragesthecollecteddatatocon-
structapersonalizedQoEmodelviaregretminimization.
AmongML-basedstudies,[154]predictsQoEfromfacialexpressionsandgazedirection,while
[110]considersDTs,RFs,andk-NearestNeighborsalgorithm(k-NN)forQoEpredictionbased
on user engagement and other factors. P.1203 [89] refers to a standard QoE model that utilizes
RFs to predict MOS on a five-point scale. LSTM-QoE [52] models QoE via an LSTM network.
Meanwhile,videoassessmentoftemporalartifactsandstalls(VideoATLAS)[11]expresses
QoEbyapplyingsupportvectorregression(SVR)tofeaturesrelatedtoperceptualquality,re-
buffering,andmemoryeffects.TopersonalizeQoEmodels,[59]performsFLonsparsedataand
accountsforchangesinIFsovertime.Guidedbyuserexperiencedesignandinvolvingtheuserin
abriefseriesofsubjectiveassessments,individualizedQoE(iQoE)[153]iterativelyconstructs
anaccuratepersonalizedQoEmodelthroughactivelearning.Lastly,Jade[82]reliesonDRLwith
PPOtotrainaQoEmodelbasedontherelativeranks,ratherthantheabsolutevalues,ofsubjective
scores.
6.3 MainTakeaways
Recent research on the ABR, CDN, and QoE aspects at the distribution stage primarily focuses
on ABR algorithms, particularly for the VoD streaming mode. ABR algorithms increasingly rely
on ML and, especially, DRL and AC methods. Studies on ABR algorithms for live streaming are
lessextensive,partlybecausetheHASparadigmoffersfeweropportunitiesforlatencyreduction,
whichiscriticalforlivestreaming.Additionally,theadoptionofDRL-basedABRalgorithmsinlive
streamingischallengingduetotheirhighcomputationaldemands.Forsimilarreasons,theuseof
SR at the distribution stage remains relatively rare compared to the ingestion stage. Regarding
codecs, theresearchtendency mirrors thatat theprocessingstage, with a predominant reliance
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:24 L.PeroniandS.Gorinsky
onH.264orH.265asopposedtocutting-edgeproprietaryalternatives.However,recentworkwith
newlayeredcodecsshowspromisingresults.
The general trend toward integrated designs is evident at the distribution stage, particularly
in research on CDN and QoE aspects. ABR designs that are CDN-aware or utilize well-defined
QoE models become more common. Additionally, personalized QoE modeling represents an ac-
tive research area. On the other hand, cooperation between the application and lower network
layersstrugglestogaintraction.Asaresult,application-layerABRalgorithmsprimarilyfocuson
bandwidthefficiency,whilefairnessinnetworksharingremainsmostlytheresponsibilityofthe
transportlayer.
7 Real-WorldApplications
Commercial streaming platforms play a major role in shaping the HAS practice for long-form
2Dvideos.Thesecompaniesinformthetechnicalcommunityandgeneralpublicabouttheirtech-
nologies through corporate blogs, white papers, open-source tools, standardization efforts, and
academicpartnerships.Additionally,researchersprovideindependentinsightsbymeasuringand
reverse-engineeringproprietarytechnologies.
7.1 Netflix
Netflixregularlyutilizesitstechnologyblogtosharein-depthinsightsintoitspracticesandinnova-
tions.WhilesupportingH.264,H.265,VP9,andAV1codecs,NetflixprefersVP9andAV1toreduce
licensingcostsandenhanceaccessibility.AsamajordeveloperofAV1[145],Netflixactivelyadvo-
catesforthecodecandoffersAV1streamingonarangeofdevices,includingtelevisionsets[72].
NetflixalsosupportsAVCHi-MobileandVP9-Mobile,whichareprofilesofAVC/H.264andVP9tai-
loredformobiledevices[144].Additionally,Netflixemploysthedynamicoptimizer(DO)[100],
acodec-agnosticsystemthatsegmentsvideointoshotsandconstructsrepresentationsoptimized
forvisualperception.AimingtoenhanceQoE,Netflixappliesitsdeepdownscaler(DD)[57]in
videopreprocessingtoscaledownfromHRtoLRwhilepreservingimportantvisualdetails.DD
leverages ML-based SR techniques and trains CNNs and GANs via SL. At the distribution stage,
NetflixreliesonOpenConnect[24,142],itsproprietaryCDNthatintegratesabackbonenetwork
withtensofthousandsoflocalserversdeployedacrossmorethanonehundredcountries.Devel-
oped by Netflix, VMAF [120] is an open-source technique that employs SL to fuse PSNR, SSIM,
andothermetricsofvideoquality.ForNetflixandmanythirdparties,VMAFservesasapreferred
metricforassessingvideoqualityinapplicationsrelatedtoABRandQoE.Besides,Netflixtailors
avariantofVMAFforhighdynamicrange(HDR) [132]video,whichsupportsawiderrange
ofcolorandluminance.
7.2 YouTube
Similar to Netflix, YouTube supports H.264, H.265, VP9, and AV1 [115]. However, YouTube fo-
cusesonVP9asthedefaultcodecformostvideos,employsH.264forcompatibility,andgradually
adoptsAV1,particularlyforhigh-qualitystreaming[146,201].Onaverage,YouTubeencodesits
VoDcontentinto20representationswithvariouscombinationsofbitrateandresolution.Forlive
streaming,YouTubegeneratesfiveorsixrepresentations[115]andoperatesinlowandultra-low
latencymodes,requestingchunksatintervalsof2sand1s,respectively[129].Thedistribution
stageleveragestheYouTubeCDN[62],whichGooglemaintainsspecificallyforservingYouTube
videos. Independent measurements suggest that YouTube’s proprietary ABR algorithm employs
quickUDPInternetconnections(QUIC)[111]orTCPflowstodownloadmultiplechunkscon-
currently[74],utilizeslessthan60%oftheavailablenetworkbandwidth,sizestheplaybackbuffer
toalargedurationof80s,andredownloadschunksinhigherrepresentations[123].
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:25
7.3 AmazonPrimeVideo
PrimeVideo,whichisastreamingserviceofferedbyAmazon,typicallysupportsH.264andH.265
codecsanddevelopsproprietaryoptimizationsforvideoencoding.Forexample,itintroducesthe
encoder-awaremotioncompensatedtemporalfilter(EA-MCTF)[184]forvideopreprocess-
ing in conjunction with H.265 to improve video quality while maintaining low encoding time
overhead.Atthedistributionstage,PrimeVideoprimarilyreliesonCloudFront,Amazon’sown
CDN,whilealsoleveragingthird-partyCDNstoenhanceperformance,ensurereliability,andopti-
mizedeliveryacrossdifferentregions[170].Additionally,PrimeVideofosterstechnologicalinno-
vationthroughacademicpartnerships.Forinstance,itexploresspatio-temporallearningofvideo
quality[55]andencodingparameterchoicesinHDRvideo[34].SimilartoNetflix,AmazonPrime
VideodevelopsChipQAasano-referencemetricofvideoqualitybasedonspace-time(ST)chips,
whicharelocalizedsegmentsofvideo[49].
7.4 Twitch
TwitchprimarilyemploystheH.264codecwithNVENChardwareacceleration[182]andadvances
itssupportforH.265[183],VP9[50],andAV1[183].Toovercomethelimitationsofopen-source
transcodingtools,Twitchdevelopsitsowntranscoder,whichenhancesdownsamplingandmeta-
datainsertion[64].Likeothermajorstreamingplatforms,TwitchreliesonitsownCDNfordistri-
bution[191],complementedbythird-partyCDNservices.IndependentmeasurementsofTwitch’s
proprietaryABRalgorithmindicatethatittypicallyfillsnearly20softhebufferbeforestarting
playback,utilizeslessthan60%oftheavailablenetworkbandwidth,andassessesvideoqualityby
accountingforhumanperception[123].
7.5 MainTakeaways
StreamingplatformssuchasNetflix,YouTube,AmazonPrimeVideo,andTwitchplayapivotalrole
inadvancingHASpracticesforlong-form2Dvideos.Whiletheydevelopproprietarytechnologies
forencoding,distribution,andqualityassessment,theyalsoshareinsightsviablogs,whitepapers,
andopen-sourcetools.NetflixprioritizesVP9andAV1codecstocutcostsandimproveaccessibil-
ity,utilizingtoolslikeDO,DD,andVMAFforqualityoptimization.YouTubefocusesonVP9and
AV1,usesQUICorTCPforefficientchunkdownloads,andreliesonitsdedicatedCDN.Amazon
Prime Video employs H.264 and H.265, leverages CloudFront and third-party CDNs, and collab-
orateswithacademiaonqualityimprovements.TwitchenhancestranscodingandCDNdelivery,
emphasizinghumanperceptioninitsABRalgorithms.
8 TrendsandFutureDirections
AfterreviewingrecentresearchinSections4through6andreal-worldapplicationsinSection7,
wenowdistillcurrentprominenttrendsanddiscussfutureresearchdirectionsinvideostreaming.
8.1 Trends
8.1.1 Continued Growth of Live Streaming. Live streaming continues to expand in traffic and
attractincreasingattentionfromresearchers.Attheingestionstage,researchfocusesonenhancing
videocapture,analytics,compression,anduploadtoensurelowlatency.Theprocessingstagealso
seessomeworkrelatedtolivestreaming,suchason-the-flytranscoding.Atthedistributionstage,
themainresearchfocusremainsonVoDratherthanlivestreaming.
8.1.2 Increasing Diversity of Devices. The camera-equipped devices, media servers, CDN
servers, and user devices that make up the streaming pipeline are diverse in type and capabil-
ity.Thisdiversitycontinuestogrowasnewdevicesemergealongsidelegacyequipment.Ongoing
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:26 L.PeroniandS.Gorinsky
changes in device capabilities enable novel pipeline configurations. For instance, smart cameras
now support deep learning and play a larger role in video analytics and encoding-ladder defini-
tion,taskstraditionallyhandledbyservers.Additionally,ABRalgorithmsincreasinglyshiftfrom
the classic client-side paradigm toward greater server-side support. Furthermore, the server in-
frastructurediversifiesitseconomicmodelsbyinvolvingCDN,edge,andcloudoperatorsatthe
distributionstage.Deviceheterogeneityismostpronouncedatbothendsofthepipeline,driven
byinterestinnewstreamingmodesandimprovementsinQoE.
8.1.3 Integration Across the End-to-End Pipeline. Live streaming and advanced devices drive
thetrendtowardunifiedsolutionsacrossthestreamingpipeline,promisingmoreefficientdesigns
andimprovedend-to-endperformance.Forexample,thedistinctionbetweeninitialcompression
incamera-equippeddevicesandtranscodinginmediaserversbecomesblurry,asrecentdesigns
dynamicallysplitcodingtasksbetweenthecamera-equippeddeviceandmediaservertosupport
lowlatency,conserveenergy,decreasestoragerequirements,andreducebandwidthconsumption.
Similarly,videoanalyticsadoptsjointdesignsoperatingatbothingestionandprocessingstages.SR
methodsareincreasinglyimportantformanaginglownetworkbandwidthduringvideoingestion
and distribution. ABR algorithms and processing-stage tasks, such as transcoding, benefit from
greaterawarenessofCDN,edge,andotherdistributioninfrastructures.QoEmodelsplayagrowing
roleinevaluatingdesignsnotonlyatthedistributionstage,whichdirectlyinteractswithendusers,
butalsothroughouttheentirestreamingpipeline.
8.1.4 ShiftTowardMLMethodologies. Theavailabilityofdeviceswithlargermemoryandpro-
cessing capabilities also drives a greater reliance on ML methods in streaming designs. Recent
results across all three stages of the streaming pipeline consistently show that ML gains popu-
larityoverintuitionandtheoryasthebasisforproblemsolving.Withcheapermemoryandpro-
cessingpower,theinterestinresource-intensivedata-driventechniquesisunsurprising.However,
our survey reveals significant divergence in the ML models and training approaches employed
at different stages. Ingestion-stage designs tend to rely on UL or SL with DNNs, such as CNNs.
Processing-stagesolutionspredominantlytrainsimplermodels,suchasDTsandRFs,viaSL.At
thedistributionstage,DRLrepresentsthemostcommonapproach,withACmethodsbeingpar-
ticularlyprominent.Thesedifferenceshighlightchallengesfortheintegrationtrend,asdesigning
aunifiedML-basedsolutionthatworkseffectivelyacrossallstagesmightbedifficult.
8.1.5 DesignforBetterTradeoffs. Videostreamingisacomplexproblemwithconflictingobjec-
tivesrelatedtoperformanceandresourceconsumption,makingitinfeasibletooptimizeallmetrics
simultaneously.Hence,practicalsolutionsaimtoofferattractivetradeoffs.Technologicaladvances
impacttheavailabilityandrelativecostsofnetworkbandwidth,memory,processing,energy,and
otherresources,therebyaffectingwhichtradeoffsareachievable.TheshifttowardMLmethodolo-
gies,discussedinSection8.1.4,exemplifiesnewdesirabletradeoffs.Additionally,theintegration
trendbroadenstherangeofviabletradeoffsbyallowingmoreflexibleplacementoffunctionalities
acrossthepipeline.ThissearchforbettertradeoffsisevidentinthewideadoptionofSRtechniques,
whichreducenetworkbandwidthconsumptionatthecostofincreasedprocessingrequirements.
8.2 FutureDirections
Building on the trends discussed in Section 8.1, we project future developments in the field and
examinetheirpotentialandchallenges.
8.2.1 ML-BasedStreaming. Drivenbyincreasinglyaffordablememoryandprocessingpower,
the shift toward ML methodologies is likely to continue. Another key enabler is the wealth of
unexplored opportunities, as many existing ML techniques have yet to be applied to streaming
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:27
problems.Forexample,applyingtransformerstostreamingdeservesfurtherinvestigation.Addi-
tionally, rapid advances in DNN architectures and training approaches continue to yield novel
MLmethods,potentiallyformingthebasisforinnovativestreamingdesigns.However,thisabun-
dance of research opportunities also presents challenges, particularly due to uncertainty about
whichdirectionsholdthegreatestpromise.Specifically,asnotedinSection8.1.4,thereisnoclear
understandingofwhichMLmethodsaremosteffectiveinsupportingdesignsthatspanmultiple
stagesofthestreamingpipeline.TheproliferationofMLdesignsacrossdifferentstagesalsoraises
questions about interoperability and mutual influence. While ML-based streaming matures, we
arelikelytoseethedevelopmentofmethodstailoredspecificallyforvideostreaming,ratherthan
continuedrelianceongenericMLtechniques.
8.2.2 Pipeline-WideDesigns. Thetrendsofstageintegrationandnewtradeoffs,asdiscussedin
Sections8.1.3and8.1.5,convergeintoafuturedirectiongearedtowardpipeline-widesolutions.A
recentsurgeinresearchattheingestionstagesuggestsamorebalancedapproachtoallthreestages
andtheirtraditionalroles.Cross-stagedesignsnowbenefitfromtheabilitytoshiftorsplittasks
betweenstages,optimizingresourceutilizationandperformance.Forexample,movingcertainan-
alyticsfunctionsfrommediaserverstocamera-equippeddeviceshasthepotentialtosavenetwork
bandwidthandreduceuploadlatency.Whilepipeline-widedesignsholdtremendouspromiseand
numerousunexploredopportunities,itisdesirableforunifiedsolutionstomaintainflexibility,ide-
ally through loose coupling. SR is likely to play a key role in these designs due to its ability to
operateacrossallthreestagesoftheend-to-endpipeline.
8.2.3 Transition to Advanced Codecs. While the surveyed research predominantly employs
H.264 or H.265 due to their wide availability, a promising future direction is to build streaming
systemsaroundstate-of-the-artcodecssuchasVVC,EVC,andLCEVC.Sincecutting-edgecodecs
are often proprietary, research in this area is likely to involve reverse-engineering efforts, open-
sourceinitiatives,andcollaborationswithcodecdevelopers.
8.2.4 MoreABRResearchwithDifferentFoci. ABRdesignsvarywidelyincomplexityandper-
formance. Recent research often focuses on complex high-performing DNN-based algorithms,
while deployed systems typically use simpler solutions of lower effectiveness. This divergence
indicatestheneedforABRdesignswithabetterbalancebetweencomplexityandperformance.A
promisingdirectionistoimproveinterpretabilityofDNN-basedABRsolutions,leadingtostronger
confidenceintheirrobustness.Althoughstudiedinotherdomains,workonunderstandingblack-
boxABRalgorithmsandconvertingthemtosimplerinterpretableforms[136]isrelativelyscarce
andneedsfurtherinvestigation.AnotherpromisingresearchdirectionisautomatictuningofABR
algorithms. Early efforts, such as [6, 42], explore parameter tuning via simulations. Developing
efficientautomatictuningtechniquesforadvancedDNN-basedABRalgorithmsrepresentsanap-
pealingfutureresearcharea.
8.2.5 Personalized Streaming. Despite significant variations in QoE perception among
users [87], streaming services typically rely on one-size-fits-all QoE models that capture QoE
as MOS, often failing to accurately reflect individual users’ experiences. Personalization of QoE
models showsimmense promisefor theenhancementofstreaming services.However, inferring
auser’sQoEperceptionnon-intrusivelyischallengingduetothecomplexityofhumancognition,
emotions, and actions. Interdisciplinary collaborations that integrate insights from network
engineering, data science, and user experience design offer significant potential for progress in
thisarea.WhenconstructingapersonalizedQoEmodelrequiresexplicitfeedbackonsubjective
QoEperception,thisfeedbackshouldbeexpressible,actionable,andminimaltoensureaccurate
QoE modeling without overburdening the user. The application of transfer learning and the
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:28 L.PeroniandS.Gorinsky
development of multiple MOS-based QoE models for different reference groups, with each user
assigned the most representative model, are practical alternatives. However, these methods also
needtoaddressconcernsaboutaccuracyandoverhead.
8.2.6 Application-NetworkInteraction. VideostreamingwithintheHASparadigmoperateson
topofTCPasthestandardtransportprotocol.Theindependentallocationofnetworkbandwidth
by application-layer ABR logic and transport-layer CC algorithms creates problems for the effi-
ciency,fairness,andstabilityofbandwidthutilization[5].Toaddresstheseissues,somesurveyed
ABRdesignsexploitexistingtransport-layersignals,whileotherstackletheproblemsbymodify-
ingthetransportornetworklayers[16,140].TheemergenceofQUIC[111]asapromisingtrans-
port protocol reinvigorates research interest in the interactions between streaming applications
andunderlyingprotocols.However,theareaofapplication-networkinteractionremainsunderex-
plored,presentingopportunitiesforbetterunderstandinganddevelopingintegratedsolutions.
8.2.7 IncreasedFocusonNewerModes. WhilethissurveycoversrecentdevelopmentsinVoD
andlivemodesof2DHAS,weanticipateagrowingshiftininterestfromVoDtolivestreaming.
CPs,streamingplatforms,andendusersflocktolivestreamingbecauselivecontentisnoweasy
to create, profitable to distribute, and appealing to consume. From a research perspective, live
streamingintroducesnewchallenges,suchasfurtherreducingend-to-endlatencywithintheHAS
paradigm. Beyond 2D videos, 360-degree video streaming becomes increasingly important due
to the wider availability of specialized equipment like omnidirectional cameras and HMDs. In
additionto360-degreevideostreaming,AR,VR,andMRapplications,epitomizedbythevisionof
themetaverse[48],arepoisedtocontinueattractingsignificantattentionfrombothindustryand
researchcommunities.
8.3 MainTakeaways
Livestreaminggrowsinbothtrafficandresearchinterest,withafocusonreducinglatencyandim-
provingthestreamingpipeline.Astrongtrendtowardintegratingsolutionsacrosstheend-to-end
pipeline aims to improve efficiency and reduce resource consumption. The increasing diversity
of devices in the streaming ecosystem drives novel configurations and encourages more server-
side support in ABR algorithms. The shift toward ML-based methodologies accelerates, though
challengesremaininharmonizingmodelsacrossdifferentstagesofthepipeline.Futuredirections
emphasizepipeline-widedesigns,transitiontoadvancedcodecs,personalizedstreaming,anden-
hancedABRsolutions.Growinginterestinapplication-networkinteractionpresentsopportunities
to explore the integration of transport-layer signals and new protocols like QUIC. Additionally,
researchshiftstowardnewerstreamingmodes,particularlylivestreamingandimmersiveexperi-
encessuchas360-degreevideo,AR,andVR.
9 Conclusion
This survey, supplemented by tutorial materials, provides a holistic overview of the end-to-end
videostreamingpipeline,encompassingtheingestion,processing,anddistributionstages.Itsfo-
cusonHASoflong-form2DvideosoverCDN-assistedbest-effortnetworksviaclient-sideABR
algorithmsreflectsadominantparadigmofmodernInternetvideostreaming.Reviewingover200
research papers, the survey covers key topics such as video compression, upload, transcoding,
bitrate adaptation, CDN support, and QoE modeling. A new taxonomy organizes the reviewed
designsbytheirproblem-solvingmethodology,whetherbasedonintuition,theory,orML.Wedis-
tinguish between MIP, MPC, PID, LO, and BO as theoretical foundations and RL, IL, SL, and UL
categoriesofML,withfurtherrefinementofRLintoA3C,A2C,AC,andothermethods.Inaddition,
we characterizeeach design by its core techniqueand traits such as codeccompatibilityand SR
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:29
usage.Thisclassificationandtraitcharacterizationenhancethesystematicunderstandingofvideo
streamingresearch.Toconnectwithreal-worldapplications,wealsoreportonpracticesandinno-
vationsbymajorstreamingplatforms,suchasNetflixandYouTube.Thesurveydistillsprominent
currenttrends,includingthecontinuedgrowthoflivestreaming,shifttowardMLmethodologies,
integrationacrosstheend-to-endpipeline,anddesignforbettertradeoffs,fueledbyincreasingde-
vicediversity.Lookingahead,thesurveyidentifiespromisingfutureresearchdirections:pipeline-
wide optimization, integration of advanced codecs, further expansion of ABR research, support
ofpersonalizedstreaming,enhancedapplication-networkinteraction,andstrongeremphasison
newermodesofstreaming.Theseareasrepresenttheforefrontofinnovationandpotentialinthe
field.
References
[1] Tobias Achterberg and Roland Wunderling. 2013. Mixed Integer Programming: Analyzing 12 Years of Progress.
Springer.
[2] SamiraAfzal,VanessaTestoni,ChristianEsteveRothenberg,PrakashKolan,andImedBouazizi.2023.Aholistic
surveyofmultipathwirelessvideostreaming.JNCA212,article103581(2023),1–41.
[3] PrateekAgrawal,AnatoliyZabrovskiy,AdithyanIlangovan,ChristianTimmerer,andRaduProdan.2021.FastTTPS:
FastapproachforvideotranscodingtimepredictionandschedulingforHTTPadaptivestreamingvideos.Cluster
Computing24,3(2021),1605–1621.
[4] IshfaqAhmad,XiaohuiWei,YuSun,andYa-QinZhang.2005.Videotranscoding:Anoverviewofvarioustechniques
andresearchissues.IEEETMM7,5(2005),793–804.
[5] SaamerAkhshabi,SethumadhavanNarayanaswamy,AliC.Begen,andConstantineDovrolis.2012.Anexperimen-
tal evaluation of rate-adaptive video players over HTTP. Signal Processing: Image Communication 27, 4 (2012),
271–287.
[6] ZahaibAkhtar,SanjayRao,BrunoRibeiro,YunSeongNam,JessicaChen,JibinZhan,RameshGovindan,EthanKatz-
Bassett,andHuiZhang.2018.Oboe:Auto-tuningvideoABRalgorithmstonetworkconditions.InSIGCOMM2018.
44–58.
[7] AbubakrO.Al-Abbasi,VaneetAggarwal,TianLan,YuXiang,Moo-RyongRa,andYih-FarnChen.2021.FastTrack:
MinimizingstallsforCDN-basedover-the-topvideostreamingsystems.IEEETCC9,4(2021),1453–1466.
[8] EthemAlpaydin.2020.IntroductiontoMachineLearning.MITPress.
[9] Sa’diAltamimiandShervinShirmohammadi.2020.QoE-FairDASHvideostreamingusingserver-sidereinforcement
learning.ACMTOMM16,2s,Article68(2020),1–21.
[10] ConsumerTechnologyAssociation.2022.CTA-5006:WebApplicationVideoEcosystem–CommonMediaServer
Data.November2022.Retrieved9June2025fromhttps://cdn.cta.tech/cta/media/media/resources/standards/pdfs/
cta-5006-final.pdf
[11] ChristosG.BampisandAlanC.Bovik.2018.Feature-basedpredictionofstreamingvideoQoE:Distortions,stalling
andmemory.SignalProcessing:ImageCommunication68(2018),218–228.
[12] AlcardoAlexBarakabitze,NabajeetBarman,ArslanAhmad,SamanZadtootaghaj,LingfenSun,MariaG.Martini,
andLuigiAtzori.2019.QoEmanagementofmultimediastreamingservicesinfuturenetworks:Atutorialandsurvey.
IEEECOMST22,1(2019),526–565.
[13] NabajeetBarmanandMariaG.Martini.2019.QoEmodelingforHTTPadaptivevideostreaming–Asurveyand
openchallenges.IEEEAccess7(2019),30831–30859.
[14] A.Beben,P.Wiśniewski,J.MongayBatalla,andP.Krawiec.2016.ABMA+:Lightweightandefficientalgorithmfor
HTTPadaptivestreaming.InMMSys2016.1–11.
[15] RichardBellman.1966.Dynamicprogramming.Science153,3731(1966),34–37.
[16] AbdelhakBentaleb,AliC.Begen,andRogerZimmermann.2016.SDNDASH:ImprovingQoEofHTTPadaptive
streamingusingsoftwaredefinednetworking.InMM2016.1296–1305.
[17] AbdelhakBentaleb,MayLim,MehmetN.Akcay,AliC.Begen,andRogerZimmermann.2021.Commonmediaclient
data(CMCD):Initialfindings.InNOSSDAV2021.
[18] AbdelhakBentaleb,MayLim,MehmetN.Akcay,AliC.Begen,andRogerZimmermann.2023.Metareinforcement
learningforrateadaptation.InINFOCOM2023.1–10.
[19] AbdelhakBentaleb,BayanTaani,AliC.Begen,ChristianTimmerer,andRogerZimmermann.2019.Asurveyon
bitrateadaptationschemesforstreamingmediaoverHTTP.IEEECOMST21,1(2019),562–585.
[20] DanielS.Berger,RameshK.Sitaraman,andMorHarchol-Balter.2017.AdaptSize:Orchestratingthehotobjectmem-
orycacheinacontentdeliverynetwork.InNSDI2017.483–498.
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:30 L.PeroniandS.Gorinsky
[21] KashifBilal,EmnaBaccour,AimanErbad,AmrMohamed,andMohsenGuizani.2019.Collaborativejointcaching
andtranscodinginmobileedgenetworks.JNCA136(2019),86–99.
[22] KashifBilalandAimanErbad.2017.Edgecomputingforinteractivemediaandvideostreaming.InFMEC2017.68–73.
[23] Bitmovin.2020.BitmovinVideoDeveloper.Report.Bitmovin.Retrievedfromhttps://bitmovin.com/video-developer-
report#pdf
[24] TimmBöttger,FelixCuadrado,GarethTyson,IgnacioCastro,andSteveUhlig.2018.OpenConnecteverywhere:A
glimpseattheinternetecosystemthroughthelensoftheNetflixCDN.ACMSIGCOMMCCR48,1(2018),28–34.
[25] BenjaminBross,Ye-KuiWang,YanYe,ShanLiu,JianleChen,GaryJ.Sullivan,andJens-RainerOhm.2021.Overview
oftheversatilevideocoding(VVC)standardanditsapplications.IEEETCSVT31,10(2021),3736–3764.
[26] ThiagoLuizAlvesBubolz,RuhanA.Conceição,MateusGrellert,LucianoAgostini,BrunoZatt,andGuilhermeCor-
rea.2019.Qualityandenergy-awareHEVCtransratingbasedonmachinelearning.IEEETCSI66,6(2019),2124–2136.
[27] ChunleiCai,LiChen,XiaoyunZhang,andZhiyongGao.2020.End-to-endoptimizedROIimagecompression.IEEE
TIP29(2020),3442–3457.
[28] NealCardwell,YuchungCheng,C.StephenGunn,SoheilHassasYeganeh,andVanJacobson.2016.BBR:Congestion-
basedcongestioncontrol:Measuringbottleneckbandwidthandround-trippropagationtime.Queue14,5(2016),
20–53.
[29] GaetanoCarlucci,LucaDeCicco,StefanHolmer,andSaverioMascolo.2016.AnalysisanddesignoftheGoogle
congestioncontrolforwebreal-timecommunication(WebRTC).InMMSys2016.12pages.
[30] ChaoChen,Yao-ChungLin,SteveBenting,andAnilKokaram.2018.Optimizedtranscodingforlargescaleadaptive
streamingusingplaybackstatistics.InICIP2018.3269–3273.
[31] JiasiChen,BharathBalasubramanian,andZheHuang.2019.Liv(e)-ingontheedge:User-uploadedlivestreams
drivenby“First-Mile”edgedecisions.InEDGE2019.41–50.
[32] YingChen,QingLi,AoyangZhang,LonghaoZou,YongJiang,ZhiminXu,JunlinLi,andZhenhuiYuan.2021.Higher
qualitylivestreamingunderloweruplinkbandwidth:Anapproachofsuper-resolutionbasedvideocoding.InNOSS-
DAV2021.75–81.
[33] YueChen,DebarghaMurherjee,JingningHan,AdrianGrange,YaowuXu,ZoeLiu,SarahParker,ChengChen,Hui
Su,UrvangJoshi,etal.2018.AnoverviewofcorecodingtoolsintheAV1videocodec.InPCS2018.41–45.
[34] Yixu Chen, Yongjun Wu, Hai Wei, and Sriram Sethuraman. 2023. Subjective and Objective Video Quality
Assessment of High Dynamic Range Sports Content. Technology Blog, Amazon Science. Retrieved 9 June
2025 from https://www.amazon.science/publications/subjective-and-objective-video-quality-assessment-of-high-
dynamic-range-sports-content
[35] Dah-MingChiuandRajJain.1989.Analysisoftheincreaseanddecreasealgorithmsforcongestionavoidancein
computernetworks.ComputerNetworksandISDN17,1(1989),1–14.
[36] KihoChoi,JianleChen,DmytroRusanovskyy,Kwang-PyoChoi,andEueeS.Jang.2020.AnoverviewoftheMPEG-5
essentialvideocodingstandard[StandardsinaNutshell].IEEESPM37,3(2020),160–167.
[37] Cisco.2019.CiscoVisualNetworkingIndex:ForecastandTrends,2017-2022.WhitePaperC11-741490-00.Retrieved
9June2025fromhttps://branden.biz/wp-content/uploads/2018/12/Cisco-Visual-Networking-Index_Forecast-and-
Trends_2017_2022.pdf
[38] Conviva.2022.Conviva’sStateofStreamingQ22022.Report.Conviva.Retrievedfromhttps://www.conviva.com/wp-
content/uploads/2022/09/Q2-SoS.pdf
[39] LuisCostero,ArmanIranfar,MarinaZapater,FranciscoD.Igual,KatzalinOlcoz,andDavidAtienza.2019.MAMUT:
Multi-agentreinforcementlearningforefficientreal-timemulti-uservideotranscoding.InDATE2019.558–563.
[40] MalleshamDasari,KumaraKahatapitiya,SamirR.Das,ArunaBalasubramanian,andDimitrisSamaras.2022.Swift:
Adaptivevideostreamingwithlayeredneuralcodecs.InNSDI2022.103–118.
[41] LucaDeCicco,VitoCaldaralo,VittorioPalmisano,andSaverioMascolo.2013.ELASTIC:Aclient-sidecontrollerfor
dynamicadaptivestreamingoverHTTP(DASH).InPV2013.
[42] LucaDeCicco,GiuseppeCilli,andSaverioMascolo.2019.ERUDITE:Adeepneuralnetworkforoptimaltuningof
adaptivevideostreamingcontrollers.InMMSys2019.13–24.
[43] JohnDilley,BruceM.Maggs,JayParikh,HaraldProkop,RameshK.Sitaraman,andBillWeihl.2002.Globallydis-
tributedcontentdelivery.IEEEIC6,5(2002),50–58.
[44] HumbertoDominguez,OsslanVergara,VianeySanchez,EfrenCasas,andK.Rao.2014.TheH.264videocoding
standard.IEEEPotentials33,2(2014),32–38.
[45] ChaoDong,ChenChangeLoy,KaimingHe,andXiaoouTang.2015.Imagesuper-resolutionusingdeepconvolutional
networks.IEEETPAMI38,2(2015),295–307.
[46] KaiDong,JunHe,andWeiSong.2015.QoE-awareadaptivebitratevideostreamingovermobilenetworkswith
cachingproxy.InICNC2015.737–741.
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:31
[47] KuntaiDu,AhsanPervaiz,XinYuan,AakankshaChowdhery,QizhengZhang,HenryHoffmann,andJunchenJiang.
2020.Server-drivenvideostreamingfordeeplearninginference.InSIGCOMM2020.557–570.
[48] HaihanDuan,JiayeLi,SizhengFan,ZhonghaoLin,XiaoWu,andWeiCai.2021.Metaverseforsocialgood:Auni-
versitycampusprototype.InMM2021.153–161.
[49] JoshuaP.Ebenezer,ZaixiShang,YongjunWu,HaiWei,andAlanC.Bovik.2020.No-ReferenceVideoQualityAssess-
mentUsingSpace-TimeChips.TechnologyBlog,AmazonScience.Retrieved9June2025fromhttps://www.amazon.
science/publications/no-reference-video-quality-assessment-using-space-time-chips
[50] AkrumElkhazin,AvinashRamachandran,RoshanBaliga,JaiKrishnan,TarekAmara,AlexConverse,andYueshi
Shen.2018.HowVP9DeliversValueforTwitch’sEsportsLiveStreaming.TechnologyBlog,Twitch.Retrieved9
June2025fromhttps://blog.twitch.tv/en/2018/12/19/how-v-p9-delivers-value-for-twitch-s-esports-live-streaming-
35db26f6322f/
[51] AlirezaErfanian,HadiAmirpour,FarzadTashtarian,ChristianTimmerer,andHermannHellwagner.2021.LwTE:
Light-weighttranscodingattheedge.IEEEAccess9(2021),112276–112289.
[52] NagabhushanEswara,S.Ashique,AnandPanchbhai,SoumenChakraborty,HemanthP.Sethuram,KiranKuchi,
AbhinavKumar,andSumohanaS.Channappayya.2020.StreamingvideoQoEmodelingandprediction:Along
short-termmemoryapproach.IEEETCSVT30,3(2020),661–673.
[53] JeroenFamaey,StevenLatré,NielsBouten,WimVandeMeerssche,BartDeVleeschauwer,WernerVanLeekwijck,
andFilipDeTurck.2013.OnthemeritsofSVC-basedHTTPadaptivestreaming.InIM2013.419–426.
[54] TongtongFeng,HaifengSun,QiQi,JingyuWang,andJianxinLiao.2020.Vabis:Videoadaptationbitratesystemfor
time-criticallivestreaming.IEEETMM22,11(2020),2963–2976.
[55] DarioFontanel,DavidHigham,andBenoitQuentinArthurVallade.2023.OntheImportanceofSpatio-Temporal
LearningforVideoQualityAssessment.TechnologyBlog,AmazonScience.Retrieved9June2025fromhttps://
www.amazon.science/publications/on-the-importance-of-spatio-temporal-learning-for-video-quality-assessment
[56] PeterI.Frazier.2018.AtutorialonBayesianoptimization.arXiv:1807.02811.Retrievedfromhttps://arxiv.org/abs/
1807.02811
[57] ChristosG.Bampis,Li-HengChen,andZhiLi.2022.ForYourEyesOnly:ImprovingNetflixVideoQualitywith
NeuralNetworks.TechnologyBlog,Netflix.Retrieved9June2025fromhttps://netflixtechblog.com/for-your-eyes-
only-improving-netflix-video-quality-with-neural-networks-5b8d032da09c
[58] GuanyuGao,HuaizhengZhang,HanHu,YonggangWen,JianfeiCai,ChongLuo,andWenjunZeng.2018.Optimizing
qualityofexperienceforadaptivebitratestreamingviaviewerinterestinference.IEEETMM20,12(2018),3399–3413.
[59] YunGao,XinWei,andLiangZhou.2020.PersonalizedQoEimprovementfornetworkingvideoservice.IEEEJSAC
38,10(2020),2311–2323.
[60] D.García-Lucas,G.Cebrián-Márquez,A.J.Díaz-Honrubia,T.Mallikarachchi,andP.Cuenca.2021.Cost-efficient
HEVC-basedquadtreesplitting(HEQUS)forVVCvideotranscoding.SignalProcessing:ImageCommunication94,
article116199(2021),1–13.
[61] EhabGhabashnehandSanjayRao.2020.ExploringtheinterplaybetweenCDNcachingandvideostreamingperfor-
mance.InINFOCOM2020.516–525.
[62] DaniloGiordano,StefanoTraverso,LuigiGrimaudo,MarcoMellia,ElenaBaralis,AlokTongaonkar,andSabyasachi
Saha.2015.YouLighter:AnunsupervisedmethodologytounveilYouTubeCDNchanges.InITC2015.19–27.
[63] TorkelGladandLennartLjung.2017.ControlTheory.CRCPress.
[64] JeffGong,SahilDhanju,Chih-ChiangLu,andYueshiShen.2017.LiveVideoTransmuxing/Transcoding:FFmpegvs
TwitchTranscoder,PartI.TechnologyBlog,Twitch.Retrieved9June2025fromhttps://blog.twitch.tv/en/2017/10/10/
live-video-transmuxing-transcoding-f-fmpeg-vs-twitch-transcoder-part-i-489c1c125f28/
[65] MarioGraf,ChristianTimmerer,andChristopherMueller.2017.Towardsbandwidthefficientadaptivestreamingof
omnidirectionalvideooverHTTP:Design,implementation,andevaluation.InMMSys2017.261–271.
[66] MateusGrellert,TiagoOliveira,CarlosRafaelDuarte,andLuisA.daSilvaCruz.2018.FastHEVCtransratingusing
randomforests.InVCIP2018.1–4.
[67] DanGrois,AlexGiladi,KihoChoi,MinWooPark,YinjiPiao,MinsooPark,andKwangPyoChoi.2021.Performance
comparisonofemergingEVCandVVCvideocodingstandardswithHEVCandAV1.SMPTEMotionImagingJournal
130,4(2021),1–12.
[68] Dan Grois, Detlev Marpe, Amit Mulayoff, Benaya Itzhaky, and Ofer Hadar. 2013. Performance comparison of
H.265/MPEG-HEVC,VP9,andH.264/MPEG-AVCencoders.InPCS2013.394–397.
[69] IvoGrondman,LucianBusoniu,GabrielA.D.Lopes,andRobertBabuska.2012.Asurveyofactor-criticreinforcement
learning:Standardandnaturalpolicygradients.IEEESMCC42,6(2012),1291–1307.
[70] MaximilianGrüner,MelissaLicciardello,andAnkitSingla.2020.Reconstructingproprietaryvideostreamingalgo-
rithms.InUSENIXATC2020.529–542.
[71] JingGuoandGuanghuiZhang.2021.Avideo-qualitydrivenstrategyinshortvideostreaming.InMSWiM2021.
221–228.
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:32 L.PeroniandS.Gorinsky
[72] Liwei Guo, Ashwin Kumar Gopi Valliammal, Raymond Tam, Chris Pham, Agata Opalach, and Weibo Ni. 2021.
Bringing AV1 Streaming to Netflix Members’ TVs. Technology Blog, Netflix. Retrieved 9 June 2025 from https:
//netflixtechblog.com/bringing-av1-streaming-to-netflix-members-tvs-b7fc88e42320
[73] CraigGutterman,BraynFridman,TreyGilliland,YushengHu,andGilZussman.2020.STALLION:Videoadaptation
algorithmforlow-latencyvideostreaming.InMMSys2020.327–332.
[74] CraigGutterman,KatherineGuo,SarthakArora,TreyGilliland,XiaoyangWang,LesWu,EthanKatz-Bassett,and
GilZussman.2020.Requet:Real-timeQoEmetricdetectionforencryptedYouTubetraffic.ACMTOMM16,2s(2020),
1–28.
[75] SangtaeHa,InjongRhee,andLisongXu.2008.CUBIC:AnewTCP-friendlyhigh-speedTCPvariant.ACMOSR42,
5(2008),64–74.
[76] JianchaoHe,MiaoHu,YipengZhou,andDiWu.2020.LiveClip:Towardsintelligentmobileshort-formvideostream-
ingwithdeepreinforcementlearning.InNOSSDAV2020.54–59.
[77] MohammadHosseiniandViswanathanSwaminathan.2016.Adaptive360VRvideostreaming:Divideandconquer.
InIEEEISM.107–110.
[78] TobiasHoßfeldandChristianKeimel.2014.CrowdsourcinginQoEevaluation.InQualityofExperience:Advanced
Concepts,ApplicationsandMethods,SebastianMöllerandAlexanderRaake(Eds.).Springer,315–327.
[79] ShenghongHu,MinXu,HaiminZhang,ChunxiaXiao,andChaoGui.2019.Affectivecontent-awareadaptation
schemeonQoEoptimizationofadaptivestreamingoverHTTP.ACMTOMM15,3s,article100(2019),1–18.
[80] TianchiHuang,XinYao,ChengleiWu,Rui-XiaoZhang,ZhengyuanPang,andLifengSun.2019.Tiyuntsong:A
self-playreinforcementlearningapproachforABRvideostreaming.InICME2019.1678–1683.
[81] TianchiHuang,Rui-XiaoZhang,andLifengSun.2021.Deepreinforcedbitrateladdersforadaptivevideostreaming.
InNOSSDAV2021.66–73.
[82] TianchiHuang,Rui-XiaoZhang,ChengleiWu,andLifengSun.2023.Optimizingadaptivevideostreamingwith
humanfeedback.InMM2023.1707–1718.
[83] TianchiHuang,ChaoZhou,XinYao,Rui-XiaoZhang,ChengleiWu,BingYu,andLifengSun.2020.Quality-aware
neuraladaptivevideostreamingwithlifelongimitationlearning.IEEEJSAC38,10(2020),2324–2342.
[84] TianchiHuang,ChaoZhou,Rui-XiaoZhang,ChengleiWu,XinYao,andLifengSun.2020.Stick:Aharmonious
fusionofbuffer-basedandlearning-basedapproachforadaptivestreaming.InINFOCOM2020.1967–1976.
[85] Te-YuanHuang,ChaitanyaEkanadham,AndrewJ.Berglund,andZhiLi.2019.Hindsight:Evaluatevideobitrate
adaptationatscale.InMMSys2019.86–97.
[86] Te-YuanHuang,RameshJohari,NickMcKeown,MatthewTrunnell,andMarkWatson.2014.Abuffer-basedapproach
torateadaptation:Evidencefromalargevideostreamingservice.InSIGCOMM2014.187–198.
[87] LiangyuHuo,ZulinWang,MaiXu,YongLi,ZhiguoDing,andHaoWang.2020.Ameta-learningframeworkfor
learningmulti-userpreferencesinQoEoptimizationofDASH.IEEETCSVT30,9(2020),3210–3225.
[88] QuanHuynh-ThuandMohammedGhanbari.2008.ScopeofvalidityofPSNRinimage/videoqualityassessment.
ElectronicsLetters44,13(2008),800–801.
[89] International Telecommunication Union. 2017. Parametric Bitstream-Based Quality Assessment of Progressive
DownloadandAdaptiveAudiovisualStreamingServicesoverReliableTransport,Amendment1.Recommendation
P.1203.Retrieved9June2025fromhttps://www.itu.int/rec/T-REC-P.1203
[90] InternationalTelecommunicationUnion.2017.VocabularyforPerformance,QualityofServiceandQualityofExpe-
rience.RecommendationP.10.Retrieved9June2025fromhttps://www.itu.int/rec/T-REC-P.10-201711-I/en
[91] InternationalTelecommunicationUnion.July2016.MeanOpinionScoreInterpretationandReporting.Recommen-
dationP.800.2.Retrieved9June2025fromhttps://www.itu.int/rec/T-REC-P.800.2
[92] BartJansen,TimothyGoodwin,VarunGupta,FernandoKuipers,andGilZussman.2018.Performanceevaluationof
WebRTC-basedvideoconferencing.ACMSIGMETRICSPER45,3(2018),56–68.
[93] JunchenJiang,VyasSekar,andHuiZhang.2014.Improvingfairness,efficiency,andstabilityinHTTP-basedadaptive
videostreamingwithFESTIVE.IEEE/ACMToN22,1(2014),326–340.
[94] IngemarJohanssonandSarkerZaheduzzaman.2017.Self-ClockedRateAdaptationforMultimedia.December2017,
RFC8298,IETF.Retrieved9June2025fromhttps://www.rfc-editor.org/rfc/rfc8298.html
[95] MadhuriA.Joshi,MehulS.Raval,YogeshH.Dandawate,KalyaniR.Joshi,andShilpaP.Metkar.2014.Imageand
VideoCompression:Fundamentals,Techniques,andApplications.CRCPress.
[96] ParikshitJuluri,VenkateshTamarapalli,andDeepMedhi.2015.SARA:Segmentawarerateadaptationalgorithmfor
dynamicadaptivestreamingoverHTTP.InICCW2015.1765–1770.
[97] ParikshitJuluri,VenkateshTamarapalli,andDeepMedhi.2016.Measurementofqualityofexperienceofvideo-on-
demandservices:Asurvey.IEEECOMST18,1(2016),401–418.
[98] AntonS.Kaplanyan,AntonSochenov,ThomasLeimkühler,MikhailOkunev,ToddGoodall,andGizemRufo.2019.
DeepFovea:Neuralreconstructionforfoveatedrenderingandvideocompressionusinglearnedstatisticsofnatural
videos.ACMTOG38,6(2019),1–13.
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:33
[99] AggelosK.Katsaggelos,RafaelMolina,andJavierMateos.2007.SuperResolutionofImagesandVideo.Springer.
[100] IoannisKatsavounidis.2018.DynamicOptimizer–APerceptualVideoEncodingOptimizationFramework.Technol-
ogyBlog,Netflix.Retrieved9June2025fromhttps://netflixtechblog.com/dynamic-optimizer-a-perceptual-video-
encoding-optimization-framework-e19f1e3a277f
[101] AngelikiV.Katsenou,FanZhang,MarianaAfonso,andDavidR.Bull.2019.AsubjectivecomparisonofAV1and
HEVCforadaptivevideostreaming.InICIP2019.4145–4149.
[102] SomayehKianpishehandTarikTaleb.2023.Asurveyonin-networkcomputing:Programmabledataplaneand
technologyspecificapplications.IEEECOMST25,1(2023),701–761.
[103] JaehongKim,YoungmokJung,HyunhoYeo,JuncheolYe,andDongsuHan.2020.Neural-enhancedlivestreaming:
Improvinglivevideoingestviaonlinelearning.InSIGCOMM2020.107–125.
[104] TakutoKimura,TatsuakiKimura,ArifumiMatsumoto,andKazuhisaYamagishi.2021.Balancingqualityofexperi-
enceandtrafficvolumeinadaptivebitratestreaming.IEEEAccess9(2021),15530–15547.
[105] TakutoKimura,TatsuakiKimura,andKazuhisaYamagishi.2021.Context-awareadaptivebitratestreamingsystem.
InICC2021.1–7.
[106] VadimKirilin,AdityaSundarrajan,SergeyGorinsky,andRameshK.Sitaraman.2020.RL-Cache:Learning-based
cacheadmissionforcontentdelivery.IEEEJSAC38,10(2020),2372–2385.
[107] DilipKumarKrishnappa,MichaelZink,andRameshK.Sitaraman.2015.Optimizingthevideotranscodingworkflow
incontentdeliverynetworks.InMMSys2015.37–48.
[108] AlexKrizhevsky,IlyaSutskever,andGeoffreyE.Hinton.2017.ImageNetclassificationwithdeepconvolutionalneu-
ralnetworks.CACM60,6(2017),84–90.
[109] JonathanKua,GrenvilleArmitage,andPhilipBranch.2017.Asurveyofrateadaptationtechniquesfordynamic
adaptivestreamingoverHTTP.IEEECOMST19,3(2017),1842–1866.
[110] FatimaLaiche,AsmaBenLetaifa,ImeneElloumi,andTaoufikAguili.2021.Whenmachinelearningalgorithmsmeet
userengagementparameterstopredictvideoQoE.WirelessPersonalCommunications116,3(2021),2723–2741.
[111] AdamLangley,AlistairRiddoch,AlyssaWilk,AntonioVicente,CharlesKrasic,DanZhang,FanYang,FedorKoura-
nov,IanSwett,JanardhanIyengar,etal.2017.TheQUICtransportprotocol:Designandinternet-scaledeployment.
InSIGCOMM2017.183–196.
[112] HoangLe,LiangZhang,AmirSaid,GuillaumeSautiere,YangYang,PranavShrestha,FeiYin,RezaPourreza,and
AukeWiggers.2022.MobileCodec:Neuralinter-framevideocompressiononmobiledevices.InMMSys2022.324–
330.
[113] DayoungLee,JungwooLee,andMinseokSong.2019.Videoqualityadaptationforlimitingtranscodingenergy
consumptioninvideoservers.IEEEAccess7(2019),126253–126264.
[114] Jong-SeokLeeandTouradjEbrahimi.2012.Perceptualvideocompression:Asurvey.IEEEJ-STSP6,6(2012),684–697.
[115] FengLi,JaeChung,andMarkClaypool.2021.Three-yeartrendsinYouTubevideocontentandencoding.InSIGMAP
2021.15–22.
[116] HanchenLi,YihuaCheng,ZiyiZhang,QizhengZhang,AntonArapin,NickFeamster,andAmritaMazumdar.2023.
Optimizingreal-timevideoexperiencewithdatascalablecodec.InEMS2023.15–21.
[117] XiangboLi,MahmoudDarwich,andMagdyBayoumi.2021.Asurveyoncloud-basedvideostreamingservices.Ad-
vancesinComputers123(2021),193–244.
[118] YuanqiLi,ArthiPadmanabhan,PengzhanZhao,YufeiWang,GuoqingHarryXu,andRaviNetravali.2020.Reducto:
On-camerafilteringforresource-efficientreal-timevideoanalytics.InSIGCOMM2020.359–376.
[119] YunlongLi,ShansheWang,XinfengZhang,ChaoZhou,andSiweiMa.2020.Highefficiencylivevideostreaming
withframedropping.InICIP2020.1226–1230.
[120] ZhiLi,AnneAaron,IoannisKatsavounidis,AnushMoorthy,andMeghaManohara.2016.TowardaPracticalPer-
ceptualVideoQualityMetric.TechnologyBlog,Netflix.Retrieved9June2025fromhttps://medium.com/netflix-
techblog/toward-a-practical-perceptual-video-quality-metric-653f208b9652
[121] ZhuqiLi,YaxiongXie,RaviNetravali,andKyleJamieson.2023.Dashlet:Tamingswipeuncertaintyforrobustshort
videostreaming.InNSDI2023.1583–1599.
[122] ZhiLi,XiaoqingZhu,JoshuaGahm,RongPan,HaoHu,AliC.Begen,andDavidOran.2014.Probeandadapt:Rate
adaptationforHTTPvideostreamingatscale.IEEEJSAC32,4(2014),719–733.
[123] MelissaLicciardello,MaximilianGrüner,andAnkitSingla.2020.Understandingvideostreamingalgorithmsinthe
wild.InPAM2020.298–313.
[124] YunzhuoLiu,BoJiang,TianGuo,RameshK.Sitaraman,DonTowsley,andXinbingWang.2020.Grad:Learningfor
overhead-awareadaptivevideostreamingwithscalablevideocoding.InMM2020.349–357.
[125] SalvatoreLoretoandSimonPietroRomano.2014.Real-TimeCommunicationwithWebRTC:Peer-to-PeerintheBrowser.
O’ReillyMedia.
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:34 L.PeroniandS.Gorinsky
[126] ChristianLottermann,SerhanGül,DamienSchroeder,andEckehardSteinbach.2015.Network-awarevideolevel
encodingforuplinkadaptiveHTTPstreaming.InICC2015.6861–6866.
[127] ZhenxiaoLuo,ZelongWang,JinyuChen,MiaoHu,YipengZhou,TomZ.J.Fu,andDiWu.2021.CrowdSR:Enabling
high-qualityvideoingestincrowdsourcedlivecastviasuper-resolution.InNOSSDAV2021.91–97.
[128] AlexMackin,FanZhang,andDavidR.Bull.2015.Astudyofsubjectivevideoqualityatvariousframerates.InICIP
2015.3407–3411.
[129] SharatChandraMadanapalli,AlexMathai,HassanHabibiGharakheili,andVijaySivaraman.2021.ReCLive:Real-
timeclassificationandQoEinferenceoflivevideostreamingservices.InIWQOS2021.1–7.
[130] BruceM.MaggsandRameshK.Sitaraman.2015.Algorithmicnuggetsincontentdelivery.ACMSIGCOMMCCR45,
3(2015),52–66.
[131] HongziMao,RaviNetravali,andMohammadAlizadeh.2017.NeuraladaptivevideostreamingwithPensieve.In
SIGCOMM2017.197–210.
[132] AdityaMavlankar,ZhiLi,LukášKrasula,andChristosBampis.2023.AllofNetflix’sHDRVideoStreamingIsNow
DynamicallyOptimized.TechnologyBlog,Netflix.Retrieved9June2025fromhttps://netflixtechblog.com/all-of-
netflixs-hdr-video-streaming-is-now-dynamically-optimized-e9e0cb15f2ba
[133] GuidoMeardi,SimoneFerrara,LorenzoCiccarelli,GuendalinaCobianchi,StergiosPoularakis,FlorianMaurer,Ste-
fanoBattista,andAhmadByagowi.2020.MPEG-5part2:Lowcomplexityenhancementvideocoding(LCEVC):
Overviewandperformanceevaluation.InApplicationsofDigitalImageProcessingXLIII,AndrewG.Tescherand
TouradjEbrahimi(Eds.).Vol.11510,SPIE.
[134] MarwaMeddeb,MarcoCagnazzo,andBeátricePesquet-Popescu.2014.Region-of-interest-basedratecontrolscheme
forhigh-efficiencyvideocoding.InICASSP2014.7338–7342.
[135] LinghuiMeng,FangyuZhang,LeiBo,HanchengLu,JinQin,andJiangpingHan.2019.Fastconv:Fastlearningbased
adaptivebitratealgorithmforvideostreaming.InGLOBECOM2019.1–6.
[136] ZiliMeng,JingChen,YaningGuo,ChenSun,HongxinHu,andMingweiXu.2019.PiTree:Practicalimplementation
ofABRalgorithmsusingdecisiontrees.InMM2019.2431–2439.
[137] Konstantin Miller, Abdel-Karim Al-Tamimi, and Adam Wolisz. 2016. QoE-based low-delay live streaming using
throughputpredictions.ACMTOMM13,1,article4(2016),1–24.
[138] ChristianMoldovanandFlorianMetzger.2016.BridgingthegapbetweenQoEanduserengagementinHTTPvideo
streaming.InITC2016.103–111.
[139] MatthewK.Mukerjee,DavidNaylor,JunchenJiang,DongsuHan,SrinivasanSeshan,andHuiZhang.2015.Practical,
real-timecentralizedcontrolforCDN-basedlivevideodelivery.InSIGCOMM2015.311–324.
[140] VikramNathan,VibhaalakshmiSivaraman,RavichandraAddanki,MehrdadKhani,PrateeshGoyal,andMohammad
Alizadeh.2019.End-to-endtransportforvideoQoEfairness.InSIGCOMM2019.408–423.
[141] MichaelJ.Neely.2010.StochasticNetworkOptimizationwithApplicationtoCommunicationandQueueingSystems.
MorganandClaypool.
[142] Netflix.2021.ACooperativeApproachToContentDelivery.ANetflixBriefingPaper.Retrieved9June2025from
https://openconnect.netflix.com/Open-Connect-Briefing-Paper.pdf
[143] AntonopoulosNikosandGillamLee.2010.CloudComputing:Principles,SystemsandApplications.Springer.
[144] AndreyNorkin,JanDeCock,AdityaMavlankar,andAnneAaron.2016.MoreEfficientMobileEncodesforNetflix
Downloads.TechnologyBlog,Netflix.Retrieved9June2025fromhttps://netflixtechblog.com/more-efficient-mobile-
encodes-for-netflix-downloads-625d7b082909
[145] AndreyNorkin,JoelSole,MarianaAfonso,KyleSwanson,AgataOpalach,AnushMoorthy,andAnneAaron.2020.
SVT-AV1:Open-SourceAV1EncoderandDecoder.TechnologyBlog,Netflix.Retrieved9June2025fromhttps://
netflixtechblog.com/svt-av1-an-open-source-av1-encoder-and-decoder-ad295d9b5ca2
[146] JanOzer.2021.WhichCodecsDoesYouTubeUse?TechnologyBlog,StreamingLearningCenter.Retrieved9June
2025fromhttps://streaminglearningcenter.com/codecs/which-codecs-does-youtube-use.html
[147] JianliPan,SubharthiPaul,andRajJain.2011.Asurveyoftheresearchonfutureinternetarchitectures.IEEECom-
municationsMagazine49,7(2011),26–36.
[148] HaitianPang,ZhiWang,ChenYan,QinghuaDing,KunYi,JiangchuanLiu,andLifengSun.2019.Contentharvest
network:Optimizingfirstmileforcrowdsourcedlivestreaming.IEEETCSVT29,7(2019),2112–2125.
[149] KyoungjunParkandMyungchulKim.2019.EVSO:Environment-awarevideostreamingoptimizationofpowercon-
sumption.InINFOCOM2019.973–981.
[150] MinHoPark,JungyulChoi,andJunKyunChoi.2017.Anetwork-awareencodingratecontrolalgorithmforreal-time
up-streamingvideoservices.IEEECOMML21,7(2017),1653–1656.
[151] MukaddimPathanandRajkumarBuyya.2008.ATaxonomyofCDNs.Springer.
[152] LeonardoPeroniandSergeyGorinsky.2024.Qualityofexperienceinvideostreaming:Statusquo,pitfalls,andguide-
lines.InCOMSNETS2024.1–10.
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:35
[153] LeonardoPeroni,SergeyGorinsky,FarzadTashtarian,andChristianTimmerer.2023.Empowermentofatypical
viewersvialow-effortpersonalizedmodelingofvideostreamingquality.PACMNET1,CoNEXT3(2023),1–27.
[154] SimonePorcu,AlessandroFloris,andLuigiAtzori.2019.Towardsthepredictionofthequalityofexperiencefrom
facialexpressionandgazedirection.InICIN2019.82–87.
[155] SamiraPouyanfar,SaadSadiq,YilinYan,HaimanTian,YudongTao,MariaPresaReyes,Mei-LingShyu,Shu-Ching
Chen,andS.S.Iyengar.2018.Asurveyondeeplearning:Algorithms,techniques,andapplications.ACMCSUR51,
5(2018),1–36.
[156] ChunyuQiao,JiliangWang,andYunhaoLiu.2021.BeyondQoE:Diversityadaptationinvideostreamingattheedge.
IEEE/ACMToN29,1(2021),289–302.
[157] YanyuanQin,ShuaiHao,KrishnaR.Pattipati,FengQian,SubhabrataSen,BingWang,andChaoqunYue.2019.
Quality-awarestrategiesforoptimizingABRvideostreamingQoEandreducingdatausage.InMMSys2019.189–
200.
[158] YanyuanQin,RuofanJin,ShuaiHao,KrishnaR.Pattipati,FengQian,SubhabrataSen,BingWang,andChaoqunYue.
2017.AcontroltheoreticapproachtoABRvideostreaming:AfreshlookatPID-basedrateadaptation.InINFOCOM
2017.1–9.
[159] AlexanderRaake,JörgenGustafsson,SavvasArgyropoulos,Marie-NeigeGarcia,DavidLindegren,GunnarHeikkilä,
MartinPettersson,PeterList,andBernhardFeiten.2012.IP-basedmobileandfixednetworkaudiovisualmediaser-
vices.IEEESignalProcessingMagazine29,6(2012),163–163.
[160] DezhiRan,YuanxingZhang,WenhanZhang,andKaiguiBian.2020.SSR:Jointoptimizationofrecommendationand
adaptivebitratestreamingforshort-formvideofeed.InMSN2020.418–426.
[161] DevdeepRay,JackKosaian,K.V.Rashmi,andSrinivasanSeshan.2019.Vantage:Optimizingvideouploadfortime-
shiftedviewingofsociallivestreams.InSIGCOMM2019.380–393.
[162] YusufSani,AndreasMauthe,andChristopherEdwards.2017.Adaptivebitrateselection:Asurvey.IEEECOMST19,
4(2017),2985–3014.
[163] YusufSani,DarijoRaca,JasonJ.Quinlan,andCormacJ.Sreenan.2020.SMASH:Asupervisedmachinelearning
approachtoadaptivevideostreamingoverHTTP.InQoMEX2020.2–7.
[164] HeikoSchwarz,DetlevMarpe,andThomasWiegand.2007.Overviewofthescalablevideocodingextensionofthe
H.264/AVCstandard.IEEETCSVT17,9(2007),1103–1120.
[165] RizwanA.Shah,MamoonaN.Asghar,SaimaAbdullah,MartinFleury,andNeelamGohar.2019.Effectivenessof
crypto-transcodingforH.264/AVCandHEVCvideobit-streams.MultimediaToolsandApplications 78,15(2019),
21455–21484.
[166] WanxinShi,QingLi,ChaoWang,GengbiaoShen,WeichaoLi,YuWu,andYongJiang.2019.LEAP:Learning-based
smartedgewithcachingandprefetchingforadaptivevideostreaming.InIWQoS2019.1–10.
[167] MattiSiekkinen,EnricoMasala,andJukkaK.Nurminen.2017.Optimizeduploadstrategiesforlivescalablevideo
transmissionfrommobiledevices.IEEETMC16,4(2017),1059–1072.
[168] LeaSkorin-KapovandMartínVarela.2012.Amulti-dimensionalviewofQoE:TheARCUmodel.InMIPRO2012.
662–666.
[169] RuixingSong,XuewenZeng,XuWang,andRuiHan.2019.PREPARE–playbackrateandpriorityadaptivebitrate
selection.IEEEAccess7(2019),135352–135362.
[170] Achraf Souk. 2019. Using Multiple Content Delivery Networks for Video Streaming – Part 1. Technology Blog,
AWS.Retrieved9June2025fromhttps://aws.amazon.com/blogs/networking-and-content-delivery/using-multiple-
content-delivery-networks-for-video-streaming-part-1/
[171] KevinSpiteri,RahulUrgaonkar,andRameshK.Sitaraman.2020.BOLA:Near-optimalbitrateadaptationforonline
videos.IEEE/ACMToN28,4(2020),1698–1711.
[172] BranislavSredojev,DraganSamardzija,andDraganPosarac.2015.WebRTCtechnologyoverviewandsignaling
solutiondesignandimplementation.InMIPRO2015.1006–1009.
[173] ThomasStockhammer.2011.DynamicadaptivestreamingoverHTTP–standardsanddesignprinciple.InMMSys
2011.133–143.
[174] GaryJ.Sullivan,Jens-RainerOhm,Woo-JinHan,andThomasWiegand.2012.Overviewofthehighefficiencyvideo
coding(HEVC)standard.IEEETCSVT22,12(2012),1649–1668.
[175] LifengSun,MingMa,WenHu,HaitianPang,andZhiWang.2017.Beyond1millionnodes:Acrowdsourcedvideo
contentdeliverynetwork.IEEEMultiMedia24,3(2017),54–63.
[176] LiyangSun,TongyuZong,SiquanWang,YongLiu,andYaoWang.2021.Towardsoptimallow-latencylivevideo
streaming.IEEE/ACMToN29,5(2021),2327–2338.
[177] RichardS.SuttonandAndrewG.Barto.2018.ReinforcementLearning:AnIntroduction.MITPress.
[178] WowzaMediaSystems.2019.VideoStreamingLatencyReport.September2019,Report.WowzaMediaSystems.Re-
trievedfromhttps://www.wowza.com/wp-content/uploads/Streaming-Video-Latency-Report-Interactive-2019.pdf
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:36 L.PeroniandS.Gorinsky
[179] FarzadTashtarian,AbdelhakBentaleb,HadiAmirpour,SergeyGorinsky,JunchenJiang,HermannHellwagner,and
ChristianTimmerer.2024.ARTEMIS:Adaptivebitrateladderoptimizationforlivevideostreaming.InNSDI2024.
[180] FarzadTashtarian,MahdiDolati,DanieleLorenzi,MojtabaMozhganfar,SergeyGorinsky,AhmadKhonsari,Chris-
tianTimmerer,andHermannHellwagner.2025.ALPHAS:Adaptivebitrateladderoptimizationformulti-livevideo
streaming.InINFOCOM2025.1–10.
[181] PankajTopiwala,MadhuKrishnan,andWeiDai.2018.PerformancecomparisonofVVC,AV1,andHEVCon8-Bit
and10-Bitcontent.InApplicationsofDigitalImageProcessingXLI,AndrewG.Tescher(Ed.).Vol.10752,SPIE.
[182] Twitch. 2024. Broadcast Guidelines. Retrieved July 17, 2024 from https://help.twitch.tv/s/article/broadcast-
guidelines?language=en_US.
[183] Twitch.2024.EnhancedBroadcastingwithMultipleEncodes.RetrievedJuly17,2024fromhttps://help.twitch.tv/s/
article/multiple-encodes?language=en_US.
[184] Rahul Vanam and Sriram Sethuraman. 2023. Improving Compression Efficiency Using an Encoder-Aware
Motion Compensated Temporal Filter. Technology Blog, Amazon Science. Retrieved 9 June 2025 from
https://www.amazon.science/publications/improving-compression-efficiency-using-an-encoder-aware-motion-
compensated-temporal-filter
[185] RobertoViola,AngelMartin,JavierMorgade,StefanoMasneri,MikelZorrilla,PabloAngueira,andJonMontalbán.
2021.PredictiveCDNselectionforvideodeliverybasedonLSTMnetworkperformanceforecastsandcost-effective
trade-offs.IEEETransactionsonBroadcasting67,1(2021),145–158.
[186] ChenWang,AndalJayaseelan,andHyongKim.2018.Comparingcloudcontentdeliverynetworksforadaptivevideo
streaming.InCLOUD2018.686–693.
[187] CongWang,AmrRizk,andMichaelZink.2016.SQUAD:Aspectrum-basedqualityadaptationfordynamicadaptive
streamingoverHTTP.InMMSys2016.1–12.
[188] ZhouWang,AlanC.Bovik,HamidSheikh,andEeroSimoncelli.2004.Imagequalityassessment:Fromerrorvisibility
tostructuralsimilarity.IEEETIP13,4(2004),600–612.
[189] ZhihaoWang,JianChen,andStevenC.H.Hoi.2021.Deeplearningforimagesuper-resolution:Asurvey.IEEE
TPAMI43,10(2021),3365–3387.
[190] StefanWilk,RogerZimmermann,andWolfgangEffelsberg.2016.Leveragingtransitionsfortheuploadofuser-
generatedmobilevideo.InMoVid2016.25–30.
[191] Wei-ShiangWung,Guan-TingTing,Ruey-TzerHsu,ChengHsu,Yu-ChienTsai,CalebWang,Yuan-TaiLiu,HsiChen,
andPollyHuang.2021.Twitch’sCDNasanopenpopulationecosystem.InAINTEC2021.56–63.
[192] BoweiXu,HaoChen,andZhanMa.2023.Karma:Adaptivevideostreamingviacausalsequencemodeling.InMM
2023.1527–1535.
[193] MengweiXu,TiantuXu,YunxinLiu,andFelixXiaozhuLin.2021.Videoanalyticswithzero-streamingcameras.In
USENIXATC2021.459–472.
[194] YetingXu,XiangLi,YiYang,ZhenjieLin,LimingWang,andWenzhongLi.2023.FedABR:Apersonalizedfederated
reinforcementlearningapproachforadaptivevideostreaming.InNetworking2023.1–9.
[195] PraveenKumarYadav,ArashShafiei,andWeiTsangOoi.2017.QUETRA:AqueuingtheoryapproachtoDASHrate
adaptation.InMM2017.1130–1138.
[196] FrancisY.Yan,HudsonAyers,ChenzhiZhu,SadjadFouladi,JamesHong,KeyiZhang,PhilipLevis,andKeithWin-
stein.2020.Learninginsitu:Arandomizedexperimentinvideostreaming.InNSDI2020.495–511.
[197] HyunhoYeo,YoungmokJung,JaehongKim,JinwooShin,andDongsuHan.2018.Neuraladaptivecontent-aware
internetvideodelivery.InOSDI2018.645–661.
[198] HyunhoYeo,HwijoonLim,JaehongKim,YoungmokJung,JuncheolYe,andDongsuHan.2022.NeuroScaler:Neural
videoenhancementatscale.InSIGCOMM2022.795–811.
[199] JiaoyangYin,HaoChen,YilingXu,ZhanMa,andXiaozhongXu.2024.Learningaccuratenetworkdynamicsfor
enhancedadaptivevideostreaming.IEEETransactionsonBroadcasting70,3(2024),808–821.
[200] XiaoqiYin,AbhishekJindal,VyasSekar,andBrunoSinopoli.2015.Acontrol-theoreticapproachfordynamicadaptive
videostreamingoverHTTP.InSIGCOMM2015.325–338.
[201] YouTube.2024.ChooseLiveEncoderSettings,Bitrates,andResolutions.YouTubeHelp.RetrievedJuly12,2024from
https://support.google.com/youtube/answer/2853702?hl=en.
[202] HuiYuan,ChenglinGuo,JuLiu,XuWang,andSamKwong.2017.Motion-homogeneous-basedfasttranscoding
methodfromH.264/AVCtoHEVC.IEEETMM19,7(2017),1416–1430.
[203] AhmedH.Zahran,JasonQuinlan,DarijoRaca,CormacJ.Sreenan,EmirHalepovic,RakeshK.Sinha,RittwikJana,and
VijayGopalakrishnan.2016.OSCAR:Anoptimizedstall-cautiousadaptivebitratestreamingalgorithmformobile
networks.InMoVid2016.1–6.
[204] AhmedHamdyZahran,DarijoRaca,andCormacJ.Sreenan.2018.ARBITER+:Adaptiverate-basedintelligentHTTP
streamingalgorithmformobilenetworks.IEEETMC17,12(2018),2716–2728.
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:37
[205] AoyangZhang,QingLi,YingChen,XiaotengMa,LonghaoZou,YongJiang,ZhiminXu,andGabriel-MiroMuntean.
2021.Videosuper-resolutionandcaching–anedge-assistedadaptivevideostreamingsolution.IEEEBC67,4(2021),
799–812.
[206] GuanghuiZhang,JieZhang,KeLiu,JingGuo,JackY.B.Lee,HaiboHu,andVaneetAggarwal.2023.DUASVS:A
mobiledatasavingstrategyinshort-formvideostreaming.IEEETSC16,2(2023),1066–1078.
[207] TongZhang,FengyuanRen,WenxueCheng,XiaohuiLuo,RanShu,andXiaolanLiu.2020.Towardsinfluenceof
chunksizevariationonvideostreaminginwirelessnetworks.IEEEMC19,7(2020),1715–1730.
[208] XuZhang,YiyangOu,SiddharthaSen,andJunchenJiang.2021.SENSEI:Aligningvideostreamingqualitywith
dynamicusersensitivity.InNSDI2021.303–320.
[209] XuZhang,PaulSchmitt,MarshiniChetty,NickFeamster,andJunchenJiang.2022.Enablingpersonalizedvideo
qualityoptimizationwithVidHoc.arXiv:2211.15959.Retrievedfromhttps://arxiv.org/abs/2211.15959
[210] YinjieZhang,YuanxingZhang,YiWu,YuTao,KaiguiBian,PanZhou,LingyangSong,andHuTuo.2020.Improving
qualityofexperiencebyadaptivevideostreamingwithsuper-resolution.InINFOCOM2020.1957–1966.
[211] TiesongZhao,QianLiu,andChangWenChen.2017.QoEinvideotransmission:Auserexperience-drivenstrategy.
IEEECOMST19,1(2017),285–302.
[212] YiminZhou,LingTian,CeZhu,XinJin,andYuSun.2020.Videocodingoptimizationforvirtualreality360-degree
source.IEEEJSTSP14,1(2020),118–129.
[213] ShipingZhuandZiyaoXu.2017.Spatiotemporalvisualsaliencyguidedperceptualhighefficiencyvideocodingwith
neuralnetwork.Neurocomputing275(2017),511–522.
[214] XiaoqingZhu,RongPan,MichaelA.Ramalho,andSergioMenadelaCruz.2020.Network-AssistedDynamicAdapta-
tion(NADA):AUnifiedCongestionControlSchemeforReal-TimeMedia.February2020,RFC8698,IETF.Retrieved
9June2025fromhttps://datatracker.ietf.org/doc/rfc8698/
[215] YiZhu,SharathChandraGuntuku,WeisiLin,GheorghitaGhinea,andJudithA.Redi.2018.Measuringindividual
videoQoE:Asurvey,andproposalforfuturedirectionsusingsocialmedia.ACMTOMM 14,2s,article30(2018),
1–24.
[216] BehrouzZolfaghari,GautamSrivastava,SwapnoneelRoy,HamidR.Nemati,FatemehAfghah,TakeshiKoshiba,Abol-
fazlRazi,KhodakhastBibak,PinakiMitra,andBrijeshKumarRai.2020.Contentdeliverynetworks:Stateoftheart,
trends,andfutureroadmap.ACMCSUR53,2(2020),1–34.
[217] XutongZuo,YishuLi,MohanXu,WeiTsangOoi,JiangchuanLiu,JunchenJiang,XinggongZhang,KaiZheng,and
YongCui.2022.Bandwidth-efficientmulti-videoprefetchingforshortvideostreaming.InMM2022.7084–7088.
[218] XutongZuo,JiayuYang,MoweiWang,andYongCui.2022.Adaptivebitratewithuser-levelQoEpreferenceforvideo
streaming.InINFOCOM2022.1279–1288.
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:38 L.PeroniandS.Gorinsky
Appendices
A Acronyms
Table 6 lists all acronyms in alphanumeric order (left column) along with their expanded forms
(rightcolumn),wherecapitallettersmatchthoseusedintheacronyms.
Table6. AcronymsandTheirExpandedForms
Acronym Expandedform
1D One-Dimensional
2D Two-Dimensional
A2C AdvantageActorCritic
A3C AsynchronousAdvantageActorCritic
ABMA+ AdaptationandBufferManagementAlgorithm
ABR AdaptiveBitRate
AC ActorCritic
ACAA AffectiveContent-AwareAdaptation
ACKTR ActorCriticusingKronecker-factoredTrustRegion
AE AutoEncoder
AIMD Additive-IncreaseMultiplicative-Decrease
ALPHAS AdaptivebitrateLadderoPtimizationformulti-liveHAS
ANT AccurateNetworkThroughput
AP AccessPoint
AR AugmentedReality
ARBITER+ AdaptiveRate-BasedInTElligenthttpstReaming
ARTEMIS AdaptivebitRaTEladderoptiMIzationforlivevideoStreaming
AV1 AomediaVideo1
AVC AdvancedVideoCoding
B-frame Bipredictiveframe
BANQUET BAlaNcingQUalityofExperienceandTraffic
BBA Buffer-BasedAlgorithm
BBR BottleneckBandwidthandRound-trippropagationtime
BO BayesianOptimization
BOLA BufferOccupancybasedLyapunovAlgorithm
CC CongestionControl
CDN ContentDeliveryNetwork
CHN ContentHarvestNetwork
CMCD CommonMediaClientData
CMSD CommonMediaServerData
CNN ConvolutionNeuralNetwork
CP ContentProvider
CTU CodingTreeUnit
CU CodingUnit
D Derivative
DASH DynamicAdaptiveStreamingoverHttp
DCT DiscreteCosineTransform
DD DeepDownscaler
DDPG DeepDeterministicPolicyGradient
(Continued)
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:39
Table6. AcronymsandTheirExpandedForms(Continued)
Acronym Expandedform
DDS Dnn-DrivenStreaming
DNN DeepNeuralNetwork
DO DynamicOptimizer
DP DynamicProgramming
DPPO DistributedProximalPolicyOptimization
DQL DeepQ-Learning
DRL DeepReinforcementLearning
DST DiscreteSineTransform
DT DecisionTree
EA-MCTF Encoder-AwareMotionCompensatedTemporalFilter
ELASTIC fEedbackLinearizationAdaptiveSTreamIngController
ERUDITE dEep neuRal network for optimal tUning of aDaptive vIdeo sTreaming con-
trollErs
EVC EssentialVideoCoding
EVSO Environment-awareVideoStreamingOptimization
FESTIVE Fair,Efficient,andStableadapTIVEalgorithm
FL FederatedLearning
FastTTPS FastvideoTranscodingTimePredictionandScheduling
fps framespersecond
GAN GenerativeAdversarialNetwork
GCC GoogleCongestionControl
GOP GroupOfPictures
GPT GenerativePre-trainedTransformer
GPU GraphicsProcessingUnit
HAS HttpAdaptiveStreaming
HDR HighDynamicRange
HEQUS HEvc-basedQUadtreeSplitting
HEVC HighEfficiencyVideoCoding
HLS HttpLiveStreaming
HMD Head-MountedDisplay
HR High-Resolution
HTTP HyperTextTransferProtocol
HYBJ Jump-enabledHYBridcoding
I-frame Intra-frame
IAA Interest-AwareApproach
IF InfluenceFactor
IL ImitationLearning
ILP IntegerLinearProgramming
INFLOW IntelligentNetworkFLOW
ISP InternetServiceProvider
iLQR iterativeLinearQuadraticRegulator
iMPC ilqrbasedModelPredictiveControl
iQoE individualizedQualityofExperience
LCEVC LowComplexityEnhancementVideoCoding
LEAP Learning-basedEdgewithcAchingandPrefetching
(Continued)
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:40 L.PeroniandS.Gorinsky
Table6. AcronymsandTheirExpandedForms(Continued)
Acronym Expandedform
LNC LayeredNeuralCodec
LO LyapunovOptimization
LOLYPOP LOw-LatencYPredictiOn-basedadaPtation
LR Low-Resolution
LSTM LongShort-TermMemory
LwTE Light-weightTranscodingattheEdge
k-NN k-NearestNeighborsalgorithm
M/D/1/K MarkovianDeterministicSingle-serverfinite-Capacity
MILP Mixed-IntegerLinearProgramming
MINLP Mixed-IntegerNonLinearProgramming
MIP Mixed-IntegerProgramming
ML MachineLearning
MLMP Meta-LearningframeworkforMulti-userPreferences
MLP MultiLayerPerceptron
MOS MeanOpinionScore
MPC ModelPredictiveControl
MPEG MovingPictureExpertsGroup
MR MixedReality
NADA Network-AssistedDynamicAdaptation
NB NaiveBayes
NDN NamedDataNetworking
NP NondeterministicPolynomialtime
NVENC NVidiaENCoder
OSCAR OptimizedStall-CautiousAdaptivebitRate
P-frame Predictiveframe
P2P Peer-To-Peer
PANDA ProbeANDAdapt
PI Proportional-Integral
PIA PId-controlbasedAbrstreaming
PID Proportional-Integral-Derivative
PPO ProximalPolicyOptimization
PREPARE PlaybackRatEandPriorityAdaptivebitRatEselection
PSNR PeakSignal-to-NoiseRatio
QL Q-Learning
QP QuantizationParameter
QT QuadTree
QUAD QUality-AwareData-efficientstreaming
QUETRA QUEuingTheory-basedRateAdaptation
QUIC QuickUdpInternetConnections
QoE QualityofExperience
QoS QualityofService
RF RandomForest
RL ReinforcementLearning
(Continued)
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:41
Table6. AcronymsandTheirExpandedForms(Continued)
Acronym Expandedform
ROI RegionOfInterest
RTMP Real-TimeMessagingProtocol
SAM SequentialAuctionMechanism
SARA Segment-AwareRateAdaptation
SCReAM Self-ClockedRateAdaptationforMultimedia
SDN Software-DefinedNetworking
SL SupervisedLearning
SMASH SupervisedMachinelearningApproachtoadaptivevideoStreamingoverHttp
SQUAD Spectrum-basedQUalityADaptation
SR SuperResolution
SRAVS Super-ResolutionbasedAdaptiveVideoStreaming
SSIM StructuralSimilarityIndexMeasure
SSR Short-formvideoStreamingandRecommendation
ST Space-Time
STALLION STAndardLow-LatencyvIdeocONtrol
SVC ScalableVideoCoding
SVR SupportVectorRegression
TCP TransmissionControlProtocol
TF-IDF TermFrequency-InverseDocumentFrequency
UDP UserDatagramProtocol
UL UnsupervisedLearning
VCE VideoCodingEngine
VDN VideoDeliveryNetwork
VISCA VIdeoSuper-resolutionandCAching
VMAF VideoMultimethodAssessmentFusion
VR VirtualReality
VVC VersatileVideoCoding
Vabis Videoadaptationbitratesystem
VideoATLAS VideoAssessmentofTemporaLArtifactsandStalls
VoD VideoonDemand
WebRTC WebReal-TimeCommunication
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:42 L.PeroniandS.Gorinsky
B Glossary
Table7providesaglossaryofkeytermsinalphanumericorder(leftcolumn)withtheirdefinitions
(rightcolumn),includingtermsdefinedinthemaintextandthoseneedingfurtherexplanation.
Table7. Glossary
Name Definition
A video format that immerses users in a panoramic environment, en-
360-degreevideo
ablingthemtolookaroundinalldirections.
Anon-policymodel-freeRLalgorithmthatextendsACbyincorporating
an advantage function to reduce variance in the critic’s value function
A2C
estimate.Itupdatesbothactorandcriticsimultaneously,usingtheadvan-
tagefunctiontoguidetheactortowardbetteractionchoices.
Anon-policymodel-freeRLalgorithmthatusesmultipleagentsrunning
in parallel in different environments to asynchronously update a global
A3C
model. Each agent computes an advantage estimate, allowing the algo-
rithmtostabilizelearningandimprovescalabilityoverstandardA2C.
A streaming technique where the system divides the video into chunks
andencodeseachatdifferentsize-qualitylevels.Theplayerdynamically
ABR
selectstheappropriatechunkduringplaybacktoensuresmoothstream-
ing,minimizebuffering,andoptimizetheuserexperienceacrossvarying
networkconditions.
An on-policy model-free RL algorithm where the actor selects actions
basedonthecurrentpolicy,andthecriticevaluatesthoseactionsbyes-
AC
timatingthevaluefunction.Thesystemupdatesbothcomponentssimul-
taneouslytoimprovethepolicyandvaluefunction.
An on-policy model-free RL algorithm that extends AC by incorporat-
ingatrustregionmethodwithKronecker-factoredapproximationsofthe
ACKTR
Fisherinformationmatrix.Thismethodoptimizespolicyupdatesmoreef-
ficientlybycontrollingthestepsize,improvingstability,andenhancing
convergence.
A type of neural network for UL that encodes input data into a lower-
dimensional representation and then reconstructs it back to its original
AE
form,commonlyusedfordimensionalityreduction,featurelearning,and
noisereduction.
ACCalgorithmusedincomputernetworksthatgraduallyincreasesthe
datatransmissionrate(additiveincrease)whilenotdetectingcongestion
AIMD
and sharply reduces it (multiplicative decrease) upon detecting conges-
tion,helpingstabilizenetworkthroughputandavoidoverload.
Animmersivemediaexperiencethatoverlaysdigitalelementsontopof
AR thereal-worldview,enhancingtheuser’sinteractionwiththeirphysical
environmentthroughvideocontent.
Anoptimizationmethoddesignedforblack-boxfunctionswithexpensive
BO evaluations.Itusesaprobabilisticmodel,typicallyaGaussianprocess,to
predictthefunction’sbehavior.
(Continued)
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:43
Table7. Glossary(Continued)
Name Definition
Theamountofdataprocessedinavideostreamperunitoftime,typically
measuredinkilobitsormegabitspersecond(KbpsorMbps).Itdirectly
Bitrate
influencesbothvideoqualityanddataconsumption,withhigherbitrates
generallyofferingbetterqualityatthecostofincreaseddatausage.
Asystemofcacheserversdistributedacrosswidegeographicalareasto
CDN improvetheperformanceofcontentdeliveryfromCPstoendusersby
providingdataclosertothefinaluser.
AtypeofDNNdesignedspecificallyforvisualdataprocessing.Itlever-
CNN agesconvolutionallayerstoextractspatialfeaturesfrominputdata,pool-
inglayerstoreducedimensionality,andfullyconnectedlayersforclas-
sificationorregression.
Asmallself-containedsegmentofavideo,encodedatspecificresolution
Chunk
andbitratesettings,allowingindependentdownloadandplayback.
A hardwareorsoftwaretoolthatcompressesanddecompressesdigital
Codec mediabyapplyingspatialandtemporalcompression,reducingdatasize
andenablingefficientstorageandtransmissionofcontent.
Asetoftechniquesusedtomanageandmitigatenetworkcongestion,en-
Congestioncontrol suringefficientdataflowandpreventingnetworkbottlenecks.Itdynam-
icallyadjuststransmissionratesbasedonreal-timenetworkconditions.
Anoff-policymodel-freeAC-basedRLalgorithm,designedforenviron-
mentswithcontinuousactionspaces.Itusesadeterministicpolicyand
DDPG
employsatargetnetworkalongwithexperiencereplaytostabilizelearn-
ing,makingitsuitableforcomplexcontroltasks.
Amathematicaltransformationinvideocompressionthatconvertsspa-
DCT tialdataintofrequencycomponents,allowinglessimportantdatatore-
move.Thisreducesdatasizewhilemaintainingvisualquality.
Atypeofneuralnetworkwithmultiplehiddenlayersbetweentheinput
DNN
and output, enabling it to model complex patterns and relationships in
data.
Anoptimizationmethodthatsolvescomplexproblemsbybreakingthem
DP into smaller overlapping subproblems, solving each subproblem only
once,andstoringtheresultstoavoidredundantcomputations.
AnMLalgorithmusedforSLclassificationandregressiontasks.Itmod-
elsdecisionsandtheirpossibleconsequencesasatreestructure,where
DT
eachinternalnoderepresentsadecisionbasedonafeature,eachbranch
represents the outcome of that decision, and each leaf node represents
thefinalpredictionorclasslabel.
A predefined set of resolutions and bitrates used for encoding a video
Encodingladder
intomultipleversionstobalancebandwidthconsumptionanduserexpe-
rience.
AdecentralizedMLapproachwheremultipledevicesorsystemscollab-
FL orate to train a model while keeping their data local. It enables model
trainingwithoutsharingsensitivedata,ensuringprivacyandsecurity.
(Continued)
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:44 L.PeroniandS.Gorinsky
Table7. Glossary(Continued)
Name Definition
Thenumberofframesdisplayedinavideostreamperunitoftime,typ-
ically measured in frames per second (fps). It directly affects motion
Framerate
smoothnessandvisualfluidity,withhigherframeratesgenerallypro-
vidingsmootherplaybackatthecostofincreasedprocessingandband-
widthrequirements.
Individualstillimagesinavideosequencethat,whendisplayedinrapid
Frames
succession,createtheillusionofmotion.
A type of neural network consisting of two components: a generator
andadiscriminator.Thegeneratorcreatessyntheticdata,whilethedis-
GAN criminatorevaluatesitsauthenticitybycomparingittorealdata,with
bothnetworkscompetingtoimprovetheirperformance.Thisadversar-
ialprocessresultsinthegenerationofrealisticsyntheticdata.
A sequence of video frames that starts with an I-frame, followed by
GOP
dependentframeslikeP-framesandB-frames.
AnMLalgorithmusedforSLtasksthatmodelsdatausingadistribution
overfunctions.Itusesakernelfunctiontodefinecovariancebetween
Gaussianprocesses
data points and makes predictions by calculating a distribution over
possibleoutputs,providingbothameananduncertaintyestimate.
Anoptimizationmethodusedtomaximizeafunctionbyiterativelyad-
Gradientascent
justing its parameters in the direction of the steepest increase of the
function.
Atypeofvideoframethatfunctionsindependentlyofotherframesand
I-frame
servesasareferencefordecodingotherframeswithinaGOP.
AnMLapproachwhereamodellearnstoperformtasksbyobserving
IL
andmimickingexpertdemonstrations.
Anapproachtoprocessingdatawhileittransitsacrossanetwork,typ-
In-transitcomputing ically at intermediary points such as edge devices or network nodes,
insteadofwaitingforittoreachitsfinaldestination.
AnMLalgorithmusedforULthatpartitionsdataintokdistinctclusters
basedonfeaturesimilarity.Itassignsdatapointstothenearestcentroid,
k-meansclustering
updatesthecentroids,andrepeatstheprocessuntilconvergence,aim-
ingtominimizethevariancewithineachcluster.
Acontrolalgorithmusedtodeterminetheoptimalcontrolinputsfora
LQR
lineardynamicsystembyminimizingaquadraticcostfunction.
AtypeofDNNdesignedtohandlelong-termdependenciesinsequen-
LSTM tialdata.Itusesmemoryunitswithgatestoregulatetheflowofinfor-
mation,allowingthemodeltoretainimportantdataovertime.
Amodelingapproachusedtorepresentproblemsthatinvolvebothnon-
MINLP linearrelationshipsandmixedvariabletypes,includingcontinuousand
discrete(integer)variables.
Amodelingapproachusedtorepresentproblemsthatinvolvebothlin-
MIP ear relationships and mixed variable types, including continuous and
discrete(integer)variables.
Atypeoffeedforwardneuralnetworkconsistingofaninputlayer,one
MLP or morehidden layers,and anoutputlayer. Eachneuroninone layer
connectsfullytoneuronsinthesubsequentlayer.
(Continued)
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:45
Table7. Glossary(Continued)
Name Definition
Acontrolalgorithmthatusesasystemmodeltopredictfuturestatesand
MPC optimizecontrolinputsoverafinitetimehorizon.Itsolvesanoptimiza-
tionproblemateachtimestep,takingintoaccountsystemdynamics,con-
straints,anddesiredoutcomes.
A hybrid immersive media experience combining elements of both AR
MR
andVR,wherevirtualandreal-worldobjectscoexistandinteractinreal
time.
Adescriptionofavailablevideochunks,theirbitrates,resolutions,play-
Manifest backorder,andothermetadatasuchascodecinformation,segmentdura-
tion,andsubtitletracks.
A type of video frame encoded by referencing previous frames, storing
P-frame
onlythedifferencestoreducedatasizewhilemaintainingquality.
Acontrolalgorithmthatadjuststhecontrolinputbasedonthreeterms:
proportional,integral,andderivative,whichhelpminimizetheerrorbe-
PID
tweenadesiredsetpointandthemeasuredvaluebyconsideringthecur-
renterror,accumulatedpasterror,andrateofchangeoftheerror.
An on-policy model-free RL algorithm that improves policy updates by
PPO limiting the magnitude of changes using a surrogate objective function.
PPOstrikesabalancebetweenperformanceandstability.
Animagequalitymetricthatcomparestheoriginalandcompressedim-
agespixelbypixelbyevaluatingtheratiobetweenthemaximumpossible
PSNR signalandthenoiseintroduced.Themetricassessesthemeansquareder-
ror between the two images. Higher PSNR values suggest better image
quality,aslessdistortionhasoccurredduringcompression.
Anoff-policymodel-freeRLalgorithmthatlearnsthevalueofstate-action
QL pairsusingaQ-function.ThealgorithmupdatestheQ-valuesiteratively
basedonexpectedfuturerewards.QLextendstocontinuousactionspaces
byusingDNNs.
A subjective measure that captures how satisfied a user is with a ser-
vice, based on individual perceptions and experiences. It evaluates fac-
QoE
tors which contribute to the user’s personal judgment. Unlike objective
metricsthatfocusontechnicalparameters,QoEemphasizesthehuman
perspective.
Anobjectivemeasureoftheperformanceofanetworkorservice,focus-
ingonmeasurablefactorssuchasbandwidth,latency,jitter,andpacket
QoS
loss. Unlike QoE, which is subjective, QoS quantifies the technical per-
formanceofthesystem,ensuringthattheseparametersmeetpredefined
thresholds.
An ML algorithm used for SL that constructs an ensemble of decision
RF trees,eachtrainedonarandomsubsetofthedata.Thealgorithmaggre-
gatestheoutputsofindividualtreestomakethefinalprediction.
(Continued)
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

322:46 L.PeroniandS.Gorinsky
Table7. Glossary(Continued)
Name Definition
An ML approach where an agent learns to make decisions through in-
RL teractionswithanenvironment,aimingtomaximizecumulativerewards
overtimebyexploringandexploitingdifferentactions.
Aselectedareawithinanimageorvideowhereanalysis,processing,or
encodingfocuses.Inencoding,thisregionreceiveshigherprioritytoen-
ROI
hanceitsquality,whileotherlessimportantareascompressmoreaggres-
sively,optimizingbothvisualqualityandcompressionefficiency.
Astallcausedbythedepletionofthebuffer,oftenduetoinsufficientdata
Rebuffering deliveredtomaintaincontinuousplayback,typicallyresultingfrompoor
networkconditionsorinadequatebuffersize.
Thenumberofpixelsineachdimensionthatavideoframecontains,de-
Resolution
terminingitsvisualdetailandquality.
An ML approach where a model learns from labeled data, with each in-
SL putpairedwithacorrespondinggroundtruthorcorrectoutput,enabling
the model to make predictions or classifications based on these learned
associations.
Atechniqueinimageandvideoprocessingtoenhancetheresolutionof
SR
avideoorimagebeyonditsoriginalquality.
Animagequalitymetricthatmeasuresthesimilaritybetweentwoimages
by comparing luminance, contrast, and structural information. It calcu-
SSIM lateslocalpatternsofpixelintensitiesusingaslidingwindow.Themetric
considers the image’s structural components and human visual percep-
tionmoreeffectivelythanmoretraditionalmetricslikePSNR.
AnMLalgorithmusedforSLregressiontasks.Itfindsahyperplanethat
best fits the data while allowing for a margin of errorand predictsnew
SVR
datapointsbasedonthishyperplane.SVRisparticularlyeffectiveinsitu-
ationswithnonlinearrelationshipsbetweenvariablesandhandleshigh-
dimensionalfeaturespaces.
Videocontenttypicallyunderoneminutelong,optimizedforquickcon-
Short-formvideos
sumptionandhighlypopularonsocialmediaplatforms.
Anyinterruptionorpauseinvideoplaybackfromvariouscauses,suchas
Stall bufferdepletion,processingdelays,ordecodingerrors.Astallindicates
thatplaybackisunabletocontinueseamlessly,regardlessofthespecific
reasonbehindit.
A statistical measure used to assess the importance of a word within a
documentrelativetoacollectionofdocuments.Itbalancesthefrequency
TF-IDF
of the word in the document (TF) with how rare the word is across the
entirecorpus(IDF),emphasizingtermsthatareuniqueandrelevanttoa
specificdocument.
Theprocessofconvertingavideofilefromonecodecorformattoanother
toensurecompatibilitywithvariousdevicesorplatforms.Unlikeencod-
Transcoding
ing,whichcompressesrawvideodataintoaspecificformat,transcoding
reformatsanalreadyencodedfile,typicallyforoptimization,qualityad-
justment,orcompatibility.
(Continued)
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.

AnEnd-to-EndPipelinePerspectiveonVideoStreaminginBest-EffortNetworks 322:47
Table7. Glossary(Continued)
Name Definition
AnMLapproachwherethemodelidentifiespatternsorstructuresinun-
UL labeleddatawithoutpredefinedoutcomes,aimingtodiscoverunderlying
relationshipsorgroupingswithinthedata.
AvideoqualitymetricdevelopedbyNetflixthatpredictsperceivedvideo
VMAF qualitybycombiningmultiplequalityassessmentmethods.ItusesanSVR
modeltolearntheoptimalweightsfordifferentqualitymetricsbasedon
humanperception.
Afullyimmersivemediaexperiencewheretheviewerimmersesinavir-
VR tual environment, often using specialized headsets, creating a sense of
beinginsidethecontent.
Received7March2024;revised7February2025;accepted13May2025
ACMComput.Surv.,Vol.57,No.12,Article322.Publicationdate:July2025.